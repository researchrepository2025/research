"""parse_reports.py — Parse global and EU+CA AI market leader markdown reports into SQLite.

Usage (from the leaders/ directory):
    python -m analysis.parse_reports
    # or, with an explicit db path:
    python -m analysis.parse_reports --db /path/to/market_leaders.db
"""

import re
import sqlite3
import sys
from pathlib import Path

from analysis.schema import create_db

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

REPORTS_DIR = Path(__file__).parent.parent

EUR_TO_USD = 1.08
CAD_TO_USD = 0.73
GBP_TO_USD = 1.27

# ---------------------------------------------------------------------------
# normalize_name: import from analysis.normalize if available; fall back
# to a minimal inline implementation so the module is runnable standalone.
# ---------------------------------------------------------------------------
try:
    from analysis.normalize import normalize_name
except ImportError:
    def normalize_name(name: str) -> str:
        """Minimal canonical-name normaliser used when normalize.py is absent."""
        if not name:
            return name
        # Strip outer whitespace and collapse interior runs
        name = " ".join(name.split())
        # Drop trailing punctuation that occasionally appears in table cells
        name = name.rstrip("*,.")
        return name

# ---------------------------------------------------------------------------
# Segment name map: EU+CA segment header text -> global segment name
# ---------------------------------------------------------------------------

SEGMENT_NAME_MAP: dict[str, str] = {
    # Horizontal
    "Note-Taking / AI Meeting Assistants": "Note-taking / AI Meeting Assistants",
    "Note-taking / AI Meeting Assistants": "Note-taking / AI Meeting Assistants",
    # Departmental
    "Code / Software Development": "Code / Software Development",
    "IT Operations (AIOps / Observability)": "IT Operations",
    "IT Operations": "IT Operations",
    "Customer Success / Customer Service": "Customer Success",
    "Customer Success": "Customer Success",
    "Sales Intelligence / Revenue Operations": "Sales",
    "Sales": "Sales",
    "Human Resources (HR / HCM)": "HR",
    "Human Resources": "HR",
    "HR": "HR",
    "Data Science / ML Platforms": "Data Science & ML Platforms",
    "Data Science & ML Platforms": "Data Science & ML Platforms",
    "Finance + Operations": "Finance + Operations",
    "Finance + Ops": "Finance + Operations",
    # Vertical
    "Creators / Generative Media": "Creators",
    "Creators": "Creators",
    "Government / Public Sector": "Government",
    "Government": "Government",
    "Home Services / Field Service Management": "Home Services",
    "Home Services": "Home Services",
    "Finance (Vertical)": "Finance (Vertical)",
    "Manufacturing + Supply Chain": "Manufacturing + Supply Chain",
    # Exact matches that need no mapping are handled at lookup time
}

# Global segment definitions populated by parse_global_report.
# Maps section-header name (e.g. "Copilots", "Code / Software Development") ->
# {rank, name, category, market_size_usd_m}
# Populated after parse_market_size_table runs and the alias map is resolved.
GLOBAL_SEGMENTS: dict[str, dict] = {}

# Maps segment_number (from ## N. heading) -> canonical section-header name
_SEG_NUM_TO_NAME: dict[int, str] = {}

# Maps market-size table name -> section-header name (built in parse_global_report)
_MKTSIZE_TO_SECTION: dict[str, str] = {
    # market size table name  -> section header name
    "Real Estate (PropTech)":              "Real Estate",
    "Finance (Vertical AI)":               "Finance (Vertical)",
    "HR / HCM":                            "HR",
    "Marketing (AI in Marketing)":         "Marketing",
    "Finance + Operations (Dept.)":        "Finance + Operations",
    "IT Operations (AIOps)":               "IT Operations",
    "Code / SW Dev":                       "Code / Software Development",
    "Home Services (FSM)":                 "Home Services",
}

# ---------------------------------------------------------------------------
# Revenue extraction
# ---------------------------------------------------------------------------

# Patterns that indicate the value is NOT attributable to this company
_PART_OF_RE = re.compile(r"^\s*part\s+of\b", re.IGNORECASE)
# Non-revenue financial indicators — dollar amounts near these words are not revenue
_NON_REVENUE_RE = re.compile(
    r"\b(AUA|AUM|assets?\s+under|valuation|funding|raised|market\s+cap|GMV|GTV|"
    r"loans?\s+originated|mortgage|Series\s+[A-F]|seed\s+round|insured\s+property|"
    r"property\s+value|acquisition|acquired\s+for)\b",
    re.IGNORECASE,
)

# Numeric extraction: optional currency prefix, number with optional decimal,
# optional B/M/K suffix, optional + or approx modifiers
_CURRENCY_RE = re.compile(
    r"""
    (?:
        (?P<eur>€)          |
        (?P<gbp>£)          |
        (?P<cad>CA\$|CAD\$) |
        (?P<usd>\$)
    )
    \s*
    (?P<num1>[0-9]+(?:\.[0-9]+)?)   # first number
    \s*
    (?P<unit1>[BMK]?)               # B / M / K
    \s*
    (?:                             # optional range second value
        (?:[–\-—to]+\s*)
        (?P<num2>[0-9]+(?:\.[0-9]+)?)
        \s*
        (?P<unit2>[BMK]?)
    )?
    """,
    re.VERBOSE | re.IGNORECASE,
)

_STANDALONE_PCT_RE = re.compile(
    r"(?P<pct>[0-9]+(?:\.[0-9]+)?)\s*%"
    r"(?:\s+(?:market\s+share|enterprise\s+\w+\s+share|ITSM\s+\w+\s+share|"
    r"HCM\s+share|survey\s+\w+\s+share|ambient\s+\w+\s+share|"
    r"portal\s+traffic|acute.care\s+\w+\s+share|\w+\s+share))?",
    re.IGNORECASE,
)

_MARKET_SHARE_RE = re.compile(
    r"(?P<pct>[0-9]+(?:\.[0-9]+)?)\s*%\s*"
    r"(?:market\s+share|enterprise\s+\w+\s+share|ITSM\s+\w+\s+share|"
    r"HCM\s+share|survey\s+\w+\s+share|ambient\s+\w+\s+share|"
    r"portal\s+traffic|acute.care\s+EHR\s+share|"
    r"(?:\w+\s+)*share)",
    re.IGNORECASE,
)

_SOURCE_URL_RE = re.compile(r"\[(?:[^\]]*)\]\((?P<url>https?://[^\)]+)\)")


def _multiplier(unit: str) -> float:
    """Return numeric multiplier for B/M/K suffix (result in USD millions)."""
    u = unit.upper() if unit else ""
    if u == "B":
        return 1000.0
    if u == "M":
        return 1.0
    if u == "K":
        return 0.001
    # No suffix — assume the raw number is already in millions
    return 1.0


def _convert_to_usd_m(value_in_native: float, unit: str, currency: str) -> float:
    """Convert a value (in native currency units) to USD millions."""
    mult = _multiplier(unit)
    native_millions = value_in_native * mult
    if currency == "eur":
        return native_millions * EUR_TO_USD
    if currency == "gbp":
        return native_millions * GBP_TO_USD
    if currency == "cad":
        return native_millions * CAD_TO_USD
    # default: USD
    return native_millions


def extract_revenue_usd_m(text: str) -> tuple[float | None, str]:
    """Extract revenue in USD millions from a text string.

    Returns ``(revenue_usd_m, raw_label)`` where ``raw_label`` is the
    original matched currency string (e.g. ``"$20B+"``).  ``revenue_usd_m``
    is ``None`` when the value is not attributable to this company alone
    (e.g. "Part of $40B+ Azure revenue").
    """
    if not text or not text.strip():
        return None, text or ""

    raw_label = text.strip()

    # Reject non-attributable values (e.g. "Part of $40B+ Azure annual revenue")
    if _PART_OF_RE.search(text):
        return None, raw_label

    # Reject non-revenue financial metrics (AUA, AUM, valuation, funding, etc.)
    if _NON_REVENUE_RE.search(text) and not re.search(r"\brevenue\b|\bARR\b", text, re.IGNORECASE):
        return None, raw_label

    match = _CURRENCY_RE.search(text)
    if not match:
        return None, raw_label

    # Determine currency
    if match.group("eur"):
        currency = "eur"
    elif match.group("gbp"):
        currency = "gbp"
    elif match.group("cad"):
        currency = "cad"
    else:
        currency = "usd"

    num1 = float(match.group("num1"))
    unit1 = match.group("unit1") or ""

    # Build raw_label from the matched portion only
    raw_label = match.group(0).strip()

    num2_str = match.group("num2")
    if num2_str:
        # Range: take midpoint
        num2 = float(num2_str)
        unit2 = match.group("unit2") or unit1  # fall back to first unit if absent
        val1 = _convert_to_usd_m(num1, unit1, currency)
        val2 = _convert_to_usd_m(num2, unit2, currency)
        return (val1 + val2) / 2.0, raw_label

    return _convert_to_usd_m(num1, unit1, currency), raw_label


def extract_market_share(text: str) -> float | None:
    """Extract market share percentage from text. Returns float or None."""
    if not text:
        return None
    m = _MARKET_SHARE_RE.search(text)
    if m:
        return float(m.group("pct"))
    return None


def extract_source_url(text: str) -> str | None:
    """Extract the first URL from a markdown link ``[text](url)``.  Returns str or None."""
    if not text:
        return None
    m = _SOURCE_URL_RE.search(text)
    if m:
        return m.group("url")
    return None


# ---------------------------------------------------------------------------
# Market size table parsing (global report)
# ---------------------------------------------------------------------------

def _parse_market_size_value(raw: str) -> float | None:
    """Parse Market Size column value to USD millions.

    Handles:
    - ``$120.49B``                         -> 120490
    - ``$40.19–47.08B``                    -> midpoint 43635
    - ``$44.12B ($34.18B mfg + ...)``      -> 44120 (first number)
    - ``$12.06B (2024 base)``              -> 12060
    - ``$38.36B (2024 base)``              -> 38360
    - ``$10.36–14.99B``                    -> midpoint 12675
    - ``$5.49–5.64B``                      -> midpoint 5565
    - ``$23.86–26.4B``                     -> midpoint 25130
    - ``$36.67–39.34B``                    -> midpoint 37105
    - ``$5.88–7.05B``                      -> midpoint 6465
    - ``$3.11–4.02B``                      -> midpoint 3565
    - ``$3.5B``                            -> 3500
    """
    if not raw or not raw.strip():
        return None

    # Strip parenthetical annotations that are NOT a second range value,
    # e.g. "(2024 base)", "(mfg + supply chain breakdown)"
    # We keep the first currency match only.
    usd_m, _ = extract_revenue_usd_m(raw)
    return usd_m


def parse_market_size_table(lines: list[str]) -> list[dict]:
    """Parse the global report's market size stack ranking table.

    Scans for the pipe-delimited table that starts after the
    "## Market Size Stack Ranking" heading.  Returns a list of dicts:
        {rank, name, category, market_size_usd_m}
    """
    results = []
    in_table = False
    header_seen = False

    for line in lines:
        stripped = line.strip()

        # Enter table mode when we hit the header row
        if not in_table:
            if stripped.startswith("| Rank") and "Segment" in stripped and "Category" in stripped:
                in_table = True
                header_seen = False
                continue

        if not in_table:
            continue

        # Skip separator row
        if stripped.startswith("|---") or stripped.startswith("| ---"):
            header_seen = True
            continue

        # Leave table when we hit a blank line or a non-pipe line
        if not stripped.startswith("|"):
            if in_table and header_seen:
                break
            continue

        parts = [p.strip() for p in stripped.split("|")]
        # parts[0] is empty (before first |), parts[-1] is empty (after last |)
        parts = [p for p in parts if p != ""]

        if len(parts) < 4:
            continue

        # Columns: Rank | Segment | Category | Market Size (2025) | Source
        try:
            rank = int(parts[0])
        except ValueError:
            continue

        name = parts[1].strip()
        category = parts[2].strip()
        market_size_raw = parts[3].strip() if len(parts) > 3 else ""

        market_size_usd_m = _parse_market_size_value(market_size_raw)

        results.append({
            "rank": rank,
            "name": name,
            "category": category,
            "market_size_usd_m": market_size_usd_m,
        })

    return results


# ---------------------------------------------------------------------------
# Global segment and company table parsing
# ---------------------------------------------------------------------------

# Maps global section heading names to the canonical name used in GLOBAL_SEGMENTS
_GLOBAL_CATEGORY_MAP = {
    "HORIZONTAL AI": "Horizontal",
    "DEPARTMENTAL AI": "Departmental",
    "VERTICAL AI": "Vertical",
}

# Header pattern for global segment sections: ## N. Segment Name
_GLOBAL_SEG_HEADER_RE = re.compile(r"^##\s+(\d+)\.\s+(.+)$")

# Full match for a table data row (not separator, not header)
_TABLE_ROW_RE = re.compile(r"^\|(?!\s*[-:]+\s*\|)")


def _parse_table_row_global(line: str) -> dict | None:
    """Parse a single data row from a global-report segment table.

    Expected columns: Rank | Company | Key Metric | Source
    Returns dict with keys: rank, company, key_metric, source_url
    or None if the line isn't a valid data row.
    """
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    parts = [p.strip() for p in stripped.split("|")]
    parts = [p for p in parts if p != ""]
    if len(parts) < 3:
        return None

    # Skip header row
    if parts[0].lower() == "rank":
        return None
    # Skip separator row
    if parts[0].startswith("---") or parts[0].startswith(":--"):
        return None

    try:
        rank = int(parts[0])
    except ValueError:
        return None

    company = parts[1].strip() if len(parts) > 1 else ""
    key_metric = parts[2].strip() if len(parts) > 2 else ""
    source_cell = parts[3].strip() if len(parts) > 3 else ""

    # Source cell may contain multiple links separated by " / "
    source_url = extract_source_url(source_cell)

    return {
        "rank": rank,
        "company": company,
        "key_metric": key_metric,
        "source_url": source_url,
    }


def get_or_create_company(conn: sqlite3.Connection, name: str, hq: str | None = None) -> int:
    """Get existing company_id or create new company. Returns company_id."""
    canonical = normalize_name(name)
    cur = conn.cursor()
    cur.execute("SELECT company_id FROM companies WHERE canonical_name = ?", (canonical,))
    row = cur.fetchone()
    if row:
        if hq:
            cur.execute(
                "UPDATE companies SET hq_location = ? WHERE company_id = ? AND hq_location IS NULL",
                (hq, row[0]),
            )
        return row[0]
    cur.execute(
        "INSERT INTO companies (canonical_name, hq_location) VALUES (?, ?)",
        (canonical, hq),
    )
    conn.commit()
    return cur.lastrowid  # type: ignore[return-value]


def _get_or_create_segment(
    conn: sqlite3.Connection,
    segment_number: int,
    name: str,
    category: str,
    market_size_usd_m: float | None,
    scope_id: int,
) -> int:
    """Upsert a segment row and return segment_id."""
    cur = conn.cursor()
    cur.execute(
        "SELECT segment_id FROM segments WHERE segment_number = ? AND scope_id = ?",
        (segment_number, scope_id),
    )
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute(
        """INSERT INTO segments (segment_number, name, category, market_size_usd_m, scope_id)
           VALUES (?, ?, ?, ?, ?)""",
        (segment_number, name, category, market_size_usd_m, scope_id),
    )
    conn.commit()
    return cur.lastrowid  # type: ignore[return-value]


def _insert_company_segment(
    conn: sqlite3.Connection,
    company_id: int,
    segment_id: int,
    rank: int,
    revenue_usd_m: float | None,
    revenue_label: str,
    market_share_pct: float | None,
    key_metric_raw: str,
    source_url: str | None,
) -> None:
    """Insert a company_segments row (ignore if already exists)."""
    cur = conn.cursor()
    cur.execute(
        """INSERT OR IGNORE INTO company_segments
               (company_id, segment_id, rank, revenue_usd_m, revenue_label,
                market_share_pct, key_metric_raw, source_url)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            company_id,
            segment_id,
            rank,
            revenue_usd_m,
            revenue_label,
            market_share_pct,
            key_metric_raw,
            source_url,
        ),
    )
    conn.commit()


def parse_global_segments(lines: list[str], conn: sqlite3.Connection, scope_id: int = 1) -> None:
    """Parse all 23 segment tables from the global report.

    State machine:
      - Scans for ``## N. Segment Name`` headers.
      - Within each section, locates the company table
        (header: ``| Rank | Company | Key Metric | Source |``).
      - Reads table rows until a blank line or next ``##`` heading.
    Inserts into ``segments`` and ``company_segments`` tables.
    """
    current_seg_num: int | None = None
    current_seg_name: str | None = None
    in_company_table = False
    table_header_seen = False

    for line in lines:
        stripped = line.strip()

        # Detect global segment header: ## N. Name
        seg_match = _GLOBAL_SEG_HEADER_RE.match(stripped)
        if seg_match:
            current_seg_num = int(seg_match.group(1))
            current_seg_name = seg_match.group(2).strip()
            in_company_table = False
            table_header_seen = False
            continue

        if current_seg_num is None:
            continue

        # Detect the company table header row
        if (
            not in_company_table
            and stripped.startswith("| Rank")
            and "Company" in stripped
            and "Key Metric" in stripped
        ):
            in_company_table = True
            table_header_seen = False
            continue

        if not in_company_table:
            continue

        # Separator row
        if stripped.startswith("|---") or stripped.startswith("| ---"):
            table_header_seen = True
            continue

        # End of table: blank line or new heading
        if not stripped.startswith("|"):
            if table_header_seen:
                in_company_table = False
                table_header_seen = False
            continue

        if not table_header_seen:
            continue

        row = _parse_table_row_global(line)
        if row is None:
            continue

        # Look up segment definition from the market size table parse
        seg_info = GLOBAL_SEGMENTS.get(current_seg_name) or {}
        category = seg_info.get("category", "Unknown")
        market_size_usd_m = seg_info.get("market_size_usd_m")

        segment_id = _get_or_create_segment(
            conn,
            segment_number=current_seg_num,
            name=current_seg_name,
            category=category,
            market_size_usd_m=market_size_usd_m,
            scope_id=scope_id,
        )

        company_id = get_or_create_company(conn, row["company"])
        revenue_usd_m, revenue_label = extract_revenue_usd_m(row["key_metric"])
        market_share_pct = extract_market_share(row["key_metric"])

        _insert_company_segment(
            conn,
            company_id=company_id,
            segment_id=segment_id,
            rank=row["rank"],
            revenue_usd_m=revenue_usd_m,
            revenue_label=revenue_label,
            market_share_pct=market_share_pct,
            key_metric_raw=row["key_metric"],
            source_url=row["source_url"],
        )


# ---------------------------------------------------------------------------
# EU+CA report: Top 25 table parsing (for HQ enrichment)
# ---------------------------------------------------------------------------

def parse_eu_ca_top25(lines: list[str], conn: sqlite3.Connection) -> None:
    """Parse the Top 25 table from the EU+CA report to enrich company HQ locations.

    Table columns: Rank | Company | HQ | Segment | Revenue/ARR | Valuation
    Does not create segment entries.
    """
    in_table = False
    header_seen = False

    for line in lines:
        stripped = line.strip()

        if not in_table:
            if (
                stripped.startswith("| Rank")
                and "Company" in stripped
                and "HQ" in stripped
                and "Segment" in stripped
            ):
                in_table = True
                header_seen = False
                continue

        if not in_table:
            continue

        if stripped.startswith("|---") or stripped.startswith("| ---"):
            header_seen = True
            continue

        if not stripped.startswith("|"):
            if header_seen:
                break
            continue

        if not header_seen:
            continue

        parts = [p.strip() for p in stripped.split("|")]
        parts = [p for p in parts if p != ""]
        if len(parts) < 3:
            continue

        # Skip sub-header rows
        if parts[0].lower() == "rank":
            continue

        try:
            int(parts[0])
        except ValueError:
            continue

        company_name = parts[1].strip() if len(parts) > 1 else ""
        hq = parts[2].strip() if len(parts) > 2 else None

        if company_name:
            get_or_create_company(conn, company_name, hq=hq or None)


# ---------------------------------------------------------------------------
# EU+CA report: per-segment table parsing
# ---------------------------------------------------------------------------

# EU+CA section header patterns:
#   ## Horizontal AI / ## Departmental AI / ## Vertical AI
_EUCAT_CAT_HEADER_RE = re.compile(r"^##\s+(Horizontal AI|Departmental AI|Vertical AI)\s*$", re.IGNORECASE)

# Segment subsection: ### Segment Name
_EUCAT_SEG_HEADER_RE = re.compile(r"^###\s+(.+)$")

_CATEGORY_NAME_MAP = {
    "horizontal ai": "Horizontal",
    "departmental ai": "Departmental",
    "vertical ai": "Vertical",
}


def _parse_table_row_eu_ca(line: str) -> dict | None:
    """Parse a single data row from an EU+CA segment table.

    Expected columns: Rank | Company | HQ | Revenue/ARR | Valuation | Key Product
    Returns dict or None.
    """
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None

    parts = [p.strip() for p in stripped.split("|")]
    parts = [p for p in parts if p != ""]

    if len(parts) < 3:
        return None

    if parts[0].lower() == "rank":
        return None
    if parts[0].startswith("---") or parts[0].startswith(":--"):
        return None

    try:
        rank = int(parts[0])
    except ValueError:
        return None

    company = parts[1].strip() if len(parts) > 1 else ""
    hq = parts[2].strip() if len(parts) > 2 else None
    revenue_arr = parts[3].strip() if len(parts) > 3 else ""
    # valuation = parts[4] — not stored in this pass
    # key_product = parts[5] — stored as key_metric_raw

    key_product = parts[5].strip() if len(parts) > 5 else ""

    # Source URL: EU+CA tables don't have a Source column; use None
    return {
        "rank": rank,
        "company": company,
        "hq": hq or None,
        "revenue_arr": revenue_arr,
        "key_product": key_product,
        "source_url": None,
    }


def _resolve_eu_ca_segment(seg_header_name: str, conn: sqlite3.Connection) -> tuple[int | None, str, str]:
    """Resolve an EU+CA segment header to (segment_number, canonical_name, category).

    The segment_number returned is the document-ordering number from the global
    report's ``## N.`` headings (stored in scope_id=1 rows), NOT the market-size
    TAM rank.  This ensures EU+CA segment_number values are consistent with
    global ones.

    Returns (None, name, category) when unresolved; callers insert with number=0.
    """
    # Normalise the header name through the alias mapping
    canonical = SEGMENT_NAME_MAP.get(seg_header_name, seg_header_name)

    # Look up the already-inserted global segment by name to get document number
    cur = conn.cursor()
    cur.execute(
        "SELECT segment_number, category FROM segments WHERE name = ? AND scope_id = 1",
        (canonical,),
    )
    row = cur.fetchone()
    if row:
        return row[0], canonical, row[1]

    # Case-insensitive fallback
    canonical_lower = canonical.lower()
    cur.execute("SELECT segment_number, name, category FROM segments WHERE scope_id = 1")
    for seg_num, name, cat in cur.fetchall():
        if name.lower() == canonical_lower:
            return seg_num, name, cat

    # No match found
    seg_info = GLOBAL_SEGMENTS.get(canonical, {})
    return None, canonical, seg_info.get("category", "Unknown")


def parse_eu_ca_segments(lines: list[str], conn: sqlite3.Connection, scope_id: int = 2) -> None:
    """Parse all 23 segment tables from the EU+CA report.

    State machine:
      - Scans for ``## Horizontal AI`` / ``## Departmental AI`` / ``## Vertical AI``.
      - Within each category, scans for ``### Segment Name`` sub-headings.
      - Within each subsection, locates the company table and reads rows.
    Inserts into ``segments`` and ``company_segments`` tables.
    EU+CA segments get NULL market_size (the EU+CA report has no market size table).
    """
    current_category: str = "Unknown"
    current_seg_header: str | None = None
    in_company_table = False
    table_header_seen = False

    for line in lines:
        stripped = line.strip()

        # Category-level headings: ## Horizontal AI etc.
        cat_match = _EUCAT_CAT_HEADER_RE.match(stripped)
        if cat_match:
            current_category = _CATEGORY_NAME_MAP.get(cat_match.group(1).lower(), "Unknown")
            current_seg_header = None
            in_company_table = False
            table_header_seen = False
            continue

        # Segment-level headings: ### Segment Name
        seg_match = _EUCAT_SEG_HEADER_RE.match(stripped)
        if seg_match:
            current_seg_header = seg_match.group(1).strip()
            in_company_table = False
            table_header_seen = False
            continue

        if current_seg_header is None:
            continue

        # Detect the company table header row
        if (
            not in_company_table
            and stripped.startswith("| Rank")
            and "Company" in stripped
            and "HQ" in stripped
            and "Revenue" in stripped
        ):
            in_company_table = True
            table_header_seen = False
            continue

        if not in_company_table:
            continue

        # Separator row
        if stripped.startswith("|---") or stripped.startswith("| ---"):
            table_header_seen = True
            continue

        # End of table
        if not stripped.startswith("|"):
            if table_header_seen:
                in_company_table = False
                table_header_seen = False
            continue

        if not table_header_seen:
            continue

        row = _parse_table_row_eu_ca(line)
        if row is None:
            continue

        seg_num, canonical_seg_name, category = _resolve_eu_ca_segment(current_seg_header, conn)
        # Override category with the one from the global report when available;
        # fall back to the current_category derived from the EU+CA heading.
        if category == "Unknown":
            category = current_category

        segment_id = _get_or_create_segment(
            conn,
            segment_number=seg_num if seg_num is not None else 0,
            name=canonical_seg_name,
            category=category,
            market_size_usd_m=None,  # EU+CA report has no market size table
            scope_id=scope_id,
        )

        company_id = get_or_create_company(conn, row["company"], hq=row["hq"])
        revenue_usd_m, revenue_label = extract_revenue_usd_m(row["revenue_arr"])
        market_share_pct = extract_market_share(row["revenue_arr"])

        _insert_company_segment(
            conn,
            company_id=company_id,
            segment_id=segment_id,
            rank=row["rank"],
            revenue_usd_m=revenue_usd_m,
            revenue_label=revenue_label,
            market_share_pct=market_share_pct,
            key_metric_raw=row["revenue_arr"],
            source_url=row["source_url"],
        )


# ---------------------------------------------------------------------------
# Top-level report entry points
# ---------------------------------------------------------------------------

def parse_global_report(conn: sqlite3.Connection) -> None:
    """Main entry: parse the global report file."""
    path = REPORTS_DIR / "ai-market-leaders-2026.md"
    lines = path.read_text(encoding="utf-8").splitlines()

    # 1. Parse market size table.
    #    The market size table uses slightly different names from the ## N. section
    #    headers (e.g. "Real Estate (PropTech)" vs "Real Estate").  We normalise
    #    here so GLOBAL_SEGMENTS is keyed by the section-header name that
    #    parse_global_segments will encounter.
    market_size_rows = parse_market_size_table(lines)

    # Build a name->data dict keyed by the section-header name.
    for row in market_size_rows:
        mktsize_name = row["name"]
        section_name = _MKTSIZE_TO_SECTION.get(mktsize_name, mktsize_name)
        GLOBAL_SEGMENTS[section_name] = {
            "rank": row["rank"],        # market-size rank (TAM ordering)
            "name": section_name,
            "category": row["category"],
            "market_size_usd_m": row["market_size_usd_m"],
        }

    # 2. Parse per-segment company tables.
    #    parse_global_segments reads ## N. headers for the actual segment_number
    #    and uses GLOBAL_SEGMENTS to fill market_size_usd_m and category.
    parse_global_segments(lines, conn, scope_id=1)


def parse_eu_ca_report(conn: sqlite3.Connection) -> None:
    """Main entry: parse the EU+CA report file."""
    path = REPORTS_DIR / "ai-market-leaders-europe-canada-2026.md"
    lines = path.read_text(encoding="utf-8").splitlines()

    # 1. Parse top 25 for HQ enrichment
    parse_eu_ca_top25(lines, conn)

    # 2. Parse per-segment company tables
    parse_eu_ca_segments(lines, conn, scope_id=2)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main(db_path: str | None = None) -> None:
    """Parse both reports and load into SQLite."""
    conn = create_db(db_path=db_path)
    print("Parsing global report…")
    parse_global_report(conn)
    print("Parsing EU+CA report…")
    parse_eu_ca_report(conn)
    conn.close()
    print("Done.")


if __name__ == "__main__":
    db_arg = None
    if len(sys.argv) == 3 and sys.argv[1] == "--db":
        db_arg = sys.argv[2]
    main(db_path=db_arg)
