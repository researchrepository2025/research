"""analyze.py — Analysis queries and output generation for the AI Market Leaders database.

Usage (from the leaders/ directory):
    python -m analysis.analyze
    # or with an explicit db path:
    python -m analysis.analyze --db /path/to/market_leaders.db
"""

import csv
import sqlite3
import sys
from pathlib import Path

DB_DIR = Path(__file__).parent.parent / "db"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

SCOPE_NAMES = {1: "global", 2: "europe_canada"}


# ---------------------------------------------------------------------------
# Core query functions
# ---------------------------------------------------------------------------

def cross_segment_presence(conn: sqlite3.Connection, scope_id: int) -> list[dict]:
    """Return list of dicts: company, segment_count, segments, avg_rank.

    Only includes companies appearing in more than one segment for the given scope.
    Ordered by segment_count descending, then avg_rank ascending.
    """
    cur = conn.cursor()
    cur.execute(
        """
        SELECT c.canonical_name,
               COUNT(*) AS segment_count,
               GROUP_CONCAT(s.name, '; ') AS segments,
               ROUND(AVG(cs.rank), 1) AS avg_rank
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = ?
        GROUP BY c.canonical_name
        HAVING COUNT(*) > 1
        ORDER BY segment_count DESC, avg_rank ASC
        """,
        (scope_id,),
    )
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def market_share_report(conn: sqlite3.Connection) -> list[dict]:
    """Return list of dicts for all scopes with share estimates.

    Columns: scope, segment, company, rank, revenue_usd_m,
             estimated_share_pct, share_confidence.
    Only includes rows where estimated_share_pct is not NULL.
    Ordered by scope, segment name, estimated_share_pct descending.
    """
    cur = conn.cursor()
    cur.execute(
        """
        SELECT sc.name AS scope,
               s.name AS segment,
               c.canonical_name AS company,
               cs.rank,
               cs.revenue_usd_m,
               cs.estimated_share_pct,
               cs.share_confidence
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        JOIN scopes sc ON s.scope_id = sc.scope_id
        WHERE cs.estimated_share_pct IS NOT NULL
        ORDER BY sc.scope_id, s.name, cs.estimated_share_pct DESC
        """
    )
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def combined_revenue(conn: sqlite3.Connection, scope_id: int) -> list[dict]:
    """Return per-company combined revenue across all segments for a given scope.

    Columns: company, segment_count, summed_segment_revenue_m,
             capped_revenue_m, segments.

    capped_revenue_m: if companies.known_total_revenue_usd_m is set and the
    summed segment revenue exceeds it, cap at the known total. Otherwise use
    the summed value. NULL if no revenue data exists for the company.
    """
    cur = conn.cursor()
    cur.execute(
        """
        SELECT c.canonical_name AS company,
               COUNT(*) AS segment_count,
               SUM(cs.revenue_usd_m) AS summed_segment_revenue_m,
               c.known_total_revenue_usd_m,
               GROUP_CONCAT(s.name, '; ') AS segments
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = ?
        GROUP BY c.canonical_name, c.known_total_revenue_usd_m
        ORDER BY summed_segment_revenue_m DESC NULLS LAST
        """,
        (scope_id,),
    )
    rows = cur.fetchall()

    results = []
    for row in rows:
        company, seg_count, summed, known_total, segments = row
        if summed is not None and known_total is not None and summed > known_total:
            capped = known_total
        else:
            capped = summed
        results.append(
            {
                "company": company,
                "segment_count": seg_count,
                "summed_segment_revenue_m": round(summed, 2) if summed is not None else None,
                "capped_revenue_m": round(capped, 2) if capped is not None else None,
                "segments": segments,
            }
        )
    return results


def segment_heatmap(
    conn: sqlite3.Connection, scope_id: int, min_segments: int = 3
) -> str:
    """Return a fixed-width text table of companies x segment numbers.

    Rows = companies with >= min_segments appearances.
    Columns = every segment_number present in the scope.
    Cell value = rank number if the company appears in that segment, blank if not.
    """
    cur = conn.cursor()

    # Fetch all segment numbers present in this scope, sorted
    cur.execute(
        "SELECT DISTINCT segment_number FROM segments WHERE scope_id = ? ORDER BY segment_number",
        (scope_id,),
    )
    seg_numbers = [row[0] for row in cur.fetchall()]

    if not seg_numbers:
        return "(no segment data)"

    # Fetch companies meeting the minimum-segments threshold
    cur.execute(
        """
        SELECT c.canonical_name, COUNT(*) AS cnt
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = ?
        GROUP BY c.canonical_name
        HAVING COUNT(*) >= ?
        ORDER BY cnt DESC, c.canonical_name
        """,
        (scope_id, min_segments),
    )
    company_rows = cur.fetchall()

    if not company_rows:
        return f"(no companies appear in {min_segments}+ segments)"

    companies = [row[0] for row in company_rows]

    # Build a lookup: company -> {segment_number -> rank}
    cur.execute(
        """
        SELECT c.canonical_name, s.segment_number, cs.rank
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = ?
        """,
        (scope_id,),
    )
    presence: dict[str, dict[int, int | None]] = {}
    for comp, seg_num, rank in cur.fetchall():
        presence.setdefault(comp, {})[seg_num] = rank

    # Determine column widths
    company_col_width = max(len(c) for c in companies)
    company_col_width = max(company_col_width, 7)  # min "Company"

    # Each segment column: width = max(len(str(num)), 2) + padding
    seg_col_widths = {n: max(len(str(n)), 2) for n in seg_numbers}

    # Build header row
    header_parts = [f"{'Company':<{company_col_width}}"]
    for n in seg_numbers:
        w = seg_col_widths[n]
        header_parts.append(f"{str(n):>{w}}")
    header = "  ".join(header_parts)

    separator = "-" * len(header)

    lines = [header, separator]
    for company in companies:
        row_parts = [f"{company:<{company_col_width}}"]
        comp_presence = presence.get(company, {})
        for n in seg_numbers:
            w = seg_col_widths[n]
            if n in comp_presence:
                rank_val = comp_presence[n]
                cell = str(rank_val) if rank_val is not None else "?"
                row_parts.append(f"{cell:>{w}}")
            else:
                row_parts.append(" " * w)
        lines.append("  ".join(row_parts))

    return "\n".join(lines)


def market_share_by_segment(
    conn: sqlite3.Connection, scope_id: int
) -> dict[str, list[tuple[str, float | None, str | None]]]:
    """Return dict mapping segment_name -> list of (company, estimated_share_pct, confidence).

    Only includes rows where estimated_share_pct is not NULL.
    Within each segment, ordered by estimated_share_pct descending.
    """
    cur = conn.cursor()
    cur.execute(
        """
        SELECT s.name AS segment,
               c.canonical_name AS company,
               cs.estimated_share_pct,
               cs.share_confidence
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = ?
          AND cs.estimated_share_pct IS NOT NULL
        ORDER BY s.segment_number, cs.estimated_share_pct DESC
        """,
        (scope_id,),
    )
    result: dict[str, list[tuple[str, float | None, str | None]]] = {}
    for seg_name, company, share, confidence in cur.fetchall():
        result.setdefault(seg_name, []).append((company, share, confidence))
    return result


def key_observations(conn: sqlite3.Connection) -> list[str]:
    """Derive key observations from the data. Return list of human-readable strings."""
    cur = conn.cursor()
    observations = []

    # Which company appears in the most segments (global)?
    cur.execute(
        """
        SELECT c.canonical_name, COUNT(*) AS cnt
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = 1
        GROUP BY c.canonical_name
        ORDER BY cnt DESC
        LIMIT 1
        """
    )
    row = cur.fetchone()
    if row:
        observations.append(
            f"Most cross-segment presence (global): {row[0]} appears in {row[1]} segments."
        )

    # Which segment has the highest concentration (top 1 company share, global)?
    cur.execute(
        """
        SELECT s.name, c.canonical_name, cs.estimated_share_pct
        FROM company_segments cs
        JOIN segments s ON cs.segment_id = s.segment_id
        JOIN companies c ON cs.company_id = c.company_id
        WHERE s.scope_id = 1
          AND cs.estimated_share_pct IS NOT NULL
        ORDER BY cs.estimated_share_pct DESC
        LIMIT 1
        """
    )
    row = cur.fetchone()
    if row:
        observations.append(
            f"Highest single-company concentration (global): {row[1]} holds an estimated "
            f"{row[2]:.1f}% share in '{row[0]}'."
        )

    # Which segment has the most even distribution (global, min stdev among top-5)?
    # Proxy: segment where the gap between rank-1 and rank-5 estimated share is smallest.
    cur.execute(
        """
        SELECT s.name,
               MAX(cs.estimated_share_pct) - MIN(cs.estimated_share_pct) AS spread
        FROM company_segments cs
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = 1
          AND cs.estimated_share_pct IS NOT NULL
          AND cs.rank BETWEEN 1 AND 5
        GROUP BY s.segment_id
        HAVING COUNT(*) >= 4
        ORDER BY spread ASC
        LIMIT 1
        """
    )
    row = cur.fetchone()
    if row:
        observations.append(
            f"Most even competitive distribution (global): '{row[0]}' has the smallest "
            f"spread ({row[1]:.1f}pp) between rank-1 and rank-5 estimated shares."
        )

    # Total unique companies per scope
    for scope_id, scope_name in SCOPE_NAMES.items():
        cur.execute(
            """
            SELECT COUNT(DISTINCT cs.company_id)
            FROM company_segments cs
            JOIN segments s ON cs.segment_id = s.segment_id
            WHERE s.scope_id = ?
            """,
            (scope_id,),
        )
        count = cur.fetchone()[0]
        observations.append(
            f"Total unique companies in {scope_name} scope: {count}."
        )

    # Companies that appear in both scopes
    cur.execute(
        """
        SELECT c.canonical_name
        FROM companies c
        WHERE EXISTS (
            SELECT 1 FROM company_segments cs
            JOIN segments s ON cs.segment_id = s.segment_id
            WHERE cs.company_id = c.company_id AND s.scope_id = 1
        )
        AND EXISTS (
            SELECT 1 FROM company_segments cs
            JOIN segments s ON cs.segment_id = s.segment_id
            WHERE cs.company_id = c.company_id AND s.scope_id = 2
        )
        ORDER BY c.canonical_name
        """
    )
    both_scope = [row[0] for row in cur.fetchall()]
    if both_scope:
        observations.append(
            f"Companies present in both global and EU+CA scopes ({len(both_scope)}): "
            + ", ".join(both_scope[:20])
            + ("..." if len(both_scope) > 20 else ".")
        )
    else:
        observations.append("No companies appear in both global and EU+CA scopes.")

    # Segment count for each scope
    for scope_id, scope_name in SCOPE_NAMES.items():
        cur.execute(
            "SELECT COUNT(*) FROM segments WHERE scope_id = ?", (scope_id,)
        )
        count = cur.fetchone()[0]
        observations.append(
            f"Total segments tracked in {scope_name} scope: {count}."
        )

    return observations


# ---------------------------------------------------------------------------
# CSV export
# ---------------------------------------------------------------------------

def _write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    """Write a list of dicts to a CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def export_csvs(conn: sqlite3.Connection) -> None:
    """Write all four CSV files to OUTPUT_DIR."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. cross_segment_global.csv
    global_rows = cross_segment_presence(conn, scope_id=1)
    _write_csv(
        OUTPUT_DIR / "cross_segment_global.csv",
        global_rows,
        ["canonical_name", "segment_count", "segments", "avg_rank"],
    )

    # 2. cross_segment_europe_canada.csv
    eu_rows = cross_segment_presence(conn, scope_id=2)
    _write_csv(
        OUTPUT_DIR / "cross_segment_europe_canada.csv",
        eu_rows,
        ["canonical_name", "segment_count", "segments", "avg_rank"],
    )

    # 3. market_share_estimates.csv
    share_rows = market_share_report(conn)
    _write_csv(
        OUTPUT_DIR / "market_share_estimates.csv",
        share_rows,
        ["scope", "segment", "company", "rank", "revenue_usd_m", "estimated_share_pct", "share_confidence"],
    )

    # 4. combined_revenue.csv  — one file, both scopes
    all_revenue_rows = []
    for scope_id, scope_name in SCOPE_NAMES.items():
        for row in combined_revenue(conn, scope_id):
            row["scope"] = scope_name
            all_revenue_rows.append(row)
    _write_csv(
        OUTPUT_DIR / "combined_revenue.csv",
        all_revenue_rows,
        ["scope", "company", "segment_count", "summed_segment_revenue_m", "capped_revenue_m", "segments"],
    )


# ---------------------------------------------------------------------------
# Report-section builders
# ---------------------------------------------------------------------------

def _fmt_table(headers: list[str], rows: list[list]) -> str:
    """Format a simple markdown pipe table."""
    col_widths = [len(h) for h in headers]
    str_rows = []
    for row in rows:
        str_row = [str(v) if v is not None else "" for v in row]
        str_rows.append(str_row)
        for i, cell in enumerate(str_row):
            col_widths[i] = max(col_widths[i], len(cell))

    def fmt_row(cells):
        return "| " + " | ".join(c.ljust(col_widths[i]) for i, c in enumerate(cells)) + " |"

    sep = "| " + " | ".join("-" * w for w in col_widths) + " |"
    lines = [fmt_row(headers), sep]
    for row in str_rows:
        lines.append(fmt_row(row))
    return "\n".join(lines)


def _section_cross_segment(conn: sqlite3.Connection) -> str:
    lines = ["## Section 1: Cross-Segment Presence", ""]

    for scope_id, scope_label in [(1, "Global"), (2, "EU+Canada")]:
        rows = cross_segment_presence(conn, scope_id)
        lines.append(f"### Top 10 Multi-Segment Companies — {scope_label}")
        lines.append("")
        if not rows:
            lines.append("_No data._")
        else:
            top10 = rows[:10]
            table_rows = [
                [i + 1, r["canonical_name"], r["segment_count"], r["avg_rank"], r["segments"]]
                for i, r in enumerate(top10)
            ]
            lines.append(
                _fmt_table(
                    ["#", "Company", "Segments", "Avg Rank", "Segment List"],
                    table_rows,
                )
            )
        lines.append("")

    return "\n".join(lines)


def _section_revenue_concentration(conn: sqlite3.Connection) -> str:
    lines = ["## Section 2: Revenue Concentration", ""]

    for scope_id, scope_label in [(1, "Global"), (2, "EU+Canada")]:
        rows = combined_revenue(conn, scope_id)
        lines.append(f"### Top 15 Companies by Combined Revenue — {scope_label}")
        lines.append("")
        # Filter to those with revenue data; revenue-less companies sort to bottom
        rows_with_rev = [r for r in rows if r["capped_revenue_m"] is not None]
        rows_no_rev = [r for r in rows if r["capped_revenue_m"] is None]
        top15 = (rows_with_rev + rows_no_rev)[:15]
        if not top15:
            lines.append("_No data._")
        else:
            table_rows = [
                [
                    i + 1,
                    r["company"],
                    r["segment_count"],
                    f"${r['summed_segment_revenue_m']:,.0f}M" if r["summed_segment_revenue_m"] is not None else "—",
                    f"${r['capped_revenue_m']:,.0f}M" if r["capped_revenue_m"] is not None else "—",
                ]
                for i, r in enumerate(top15)
            ]
            lines.append(
                _fmt_table(
                    ["#", "Company", "Segments", "Summed Revenue", "Capped Revenue"],
                    table_rows,
                )
            )
        lines.append("")

    lines.append(
        "> **Note:** *Summed Revenue* adds all segment-level revenue figures for the company "
        "(which may count the same underlying revenue in multiple segments). "
        "*Capped Revenue* is floored at the company's known total corporate revenue where "
        "that figure is available, preventing double-counting inflation."
    )
    lines.append("")
    return "\n".join(lines)


def _section_heatmap(conn: sqlite3.Connection) -> str:
    lines = [
        "## Section 3: Segment Coverage Heatmap (Global)",
        "",
        "Companies appearing in 3+ global segments. "
        "Cell value = rank within that segment; blank = not present.",
        "",
        "```",
    ]
    heatmap = segment_heatmap(conn, scope_id=1, min_segments=3)
    lines.append(heatmap)
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def _section_market_share(conn: sqlite3.Connection) -> str:
    lines = ["## Section 4: Market Share Distribution (Global)", ""]

    share_by_seg = market_share_by_segment(conn, scope_id=1)

    if not share_by_seg:
        lines.append("_No estimated share data available._")
        lines.append("")
        return "\n".join(lines)

    # Fetch segment numbers for ordering
    cur = conn.cursor()
    cur.execute(
        "SELECT name, segment_number FROM segments WHERE scope_id = 1 ORDER BY segment_number"
    )
    seg_order = {name: num for name, num in cur.fetchall()}

    sorted_segments = sorted(share_by_seg.keys(), key=lambda n: seg_order.get(n, 999))

    for seg_name in sorted_segments:
        entries = share_by_seg[seg_name]
        seg_num = seg_order.get(seg_name, "?")
        total_share = sum(e[1] for e in entries if e[1] is not None)
        over_100 = total_share > 100.5

        flag = " ⚠ shares sum > 100%" if over_100 else ""
        lines.append(f"### {seg_num}. {seg_name}{flag}")
        lines.append("")

        top5 = entries[:5]
        table_rows = [
            [
                i + 1,
                company,
                f"{share:.1f}%" if share is not None else "—",
                confidence or "—",
            ]
            for i, (company, share, confidence) in enumerate(top5)
        ]
        lines.append(
            _fmt_table(["#", "Company", "Est. Share", "Confidence"], table_rows)
        )
        if over_100:
            lines.append(
                f"> Data quality note: all companies in this segment sum to "
                f"{total_share:.1f}% — likely due to overlapping revenue attribution "
                f"or double-counted market share figures in source data."
            )
        lines.append("")

    return "\n".join(lines)


def _section_observations(conn: sqlite3.Connection) -> str:
    lines = ["## Section 5: Key Observations", ""]
    obs = key_observations(conn)
    for o in obs:
        lines.append(f"- {o}")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Report entry point
# ---------------------------------------------------------------------------

def generate_report(conn: sqlite3.Connection) -> None:
    """Write analysis_report.md to OUTPUT_DIR."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sections = [
        "# AI Market Leaders — Analysis Report\n",
        "_Generated from the AI Market Leaders 2026 database. "
        "All revenue figures in USD millions unless noted._\n",
        "---\n",
        _section_cross_segment(conn),
        "---\n",
        _section_revenue_concentration(conn),
        "---\n",
        _section_heatmap(conn),
        "---\n",
        _section_market_share(conn),
        "---\n",
        _section_observations(conn),
    ]

    report_path = OUTPUT_DIR / "analysis_report.md"
    report_path.write_text("\n".join(sections), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _get_conn(db_path: str | None = None) -> sqlite3.Connection:
    if db_path is None:
        db_path = str(DB_DIR / "market_leaders.db")
    if not Path(db_path).exists():
        print(
            f"Error: database not found at {db_path}\n"
            "Run `python -m analysis.parse_reports` first to build the database.",
            file=sys.stderr,
        )
        sys.exit(1)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def main(db_path: str | None = None) -> None:
    conn = _get_conn(db_path)
    print("Exporting CSVs…")
    export_csvs(conn)
    print("Generating report…")
    generate_report(conn)
    conn.close()
    print(f"Done. Outputs written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    db_arg = None
    if len(sys.argv) == 3 and sys.argv[1] == "--db":
        db_arg = sys.argv[2]
    main(db_path=db_arg)
