# normalize.py - Company name aliases, parent linkage, known revenue caps
import sqlite3

# Maps raw report names -> canonical company name.
# Covers every variant string that appears in table cells across both reports.
COMPANY_ALIASES = {
    # Microsoft variants
    "Microsoft Copilot": "Microsoft",
    "Microsoft Copilot / PowerPoint": "Microsoft",
    "Microsoft Azure AI Foundry": "Microsoft",
    "Microsoft Azure ML": "Microsoft",
    "Microsoft / Nuance DAX": "Microsoft",
    "Microsoft Teams Rooms + Copilot": "Microsoft",

    # Google variants
    "Google Gemini": "Google",
    "Google Slides / Gemini": "Google",
    "Google Vertex AI": "Google",
    "Google for Education": "Google",
    "Google Public Sector": "Google",
    "Google Cloud AI": "Google",

    # Anthropic variants
    "Anthropic Claude": "Anthropic",
    "Anthropic Claude Code": "Anthropic",

    # Amazon variants
    "Amazon Q Developer": "Amazon",
    "AWS GovCloud": "Amazon",

    # Salesforce variants
    "Salesforce Agentforce": "Salesforce",
    "Salesforce Marketing Cloud": "Salesforce",
    "Salesforce Einstein": "Salesforce",

    # ServiceNow variants
    "ServiceNow (Now Assist)": "ServiceNow",

    # SAP variants — both plain name forms used across reports
    "SAP SE": "SAP",
    "SAP SuccessFactors": "SAP",
    "SAP Emarsys": "SAP",

    # Oracle variants
    "Oracle HCM Cloud": "Oracle",

    # Adobe variants
    "Adobe (Marketo + Firefly)": "Adobe",
    "Adobe Firefly": "Adobe",

    # IBM variants
    "IBM (Watson AIOps)": "IBM",

    # Cursor variant
    "Cursor (Anysphere)": "Cursor",

    # Windsurf variant
    "Windsurf / Codeium": "Windsurf",

    # Intercom variant (Fin is the product name)
    "Intercom (Fin)": "Intercom",

    # Zoom variant
    "Zoom (AI Companion)": "Zoom",

    # UiPath variant
    "UiPath (Agentic Automation)": "UiPath",

    # Khan Academy variant
    "Khan Academy / Khanmigo": "Khan Academy",

    # Thomson Reuters variant
    "Thomson Reuters / CoCounsel": "Thomson Reuters",

    # Visa / Featurespace: in the global report this appears as a combined entry;
    # Featurespace is the subsidiary product, Visa is the parent.
    # The global report lists "Visa / Featurespace" as one row; keep it under Featurespace
    # because the EU+CA report treats Featurespace as its own company entry.
    "Visa / Featurespace": "Featurespace",

    # SurveyMonkey variant
    "SurveyMonkey (Momentive)": "SurveyMonkey",

    # OpenAI variant
    "OpenAI / ChatGPT": "OpenAI",

    # European / Canadian company name variants from the EU+CA report
    "Siemens AG": "Siemens",
    "ABB Ltd": "ABB",
    "Dassault Systèmes": "Dassault Systèmes",   # canonical; no alias needed but listed for completeness
    "CGI Group": "CGI",
    "Thales Group": "Thales",
    "Leonardo S.p.A.": "Leonardo",
    "Dayforce (Ceridian)": "Dayforce",
    "IFS AB": "IFS",
    "Scout24 / ImmoScout24": "Scout24",

    # Standalone subsidiaries / products kept as separate canonical names
    "GitHub Copilot": "GitHub Copilot",  # parent = Microsoft
    "Nuance DAX": "Nuance DAX",          # parent = Microsoft
    "Featurespace": "Featurespace",      # parent = Visa (post Dec-2024 acquisition)

    # Other single-name entries present in report tables (no alias, listed for documentation)
    "Beautiful.ai": "Beautiful.ai",
    "Gong": "Gong",
    "H Company": "H Company",
    "Fellow.ai": "Fellow.ai",
}

PARENT_COMPANIES = {
    "GitHub Copilot": "Microsoft",
    "Nuance DAX": "Microsoft",
    "Featurespace": "Visa",
    "YouTube": "Google",
    # Blue Yonder is a Panasonic subsidiary
    "Blue Yonder": "Panasonic",
}

# Known corporate total revenue in $M (for double-count cap).
# Values are approximate FY2024/2025 figures drawn from the source reports.
KNOWN_CORPORATE_REVENUE = {
    "Microsoft": 245_000,
    "Google": 350_000,
    "Amazon": 640_000,
    "Meta": 165_000,
    "Salesforce": 38_000,
    "SAP": 40_000,
    "Oracle": 56_000,
    "ServiceNow": 12_000,
    "Adobe": 21_000,
    "Workday": 8_500,
    "IBM": 62_000,
    "Siemens": 95_000,
    "ABB": 33_200,
    "Dassault Systèmes": 7_000,
    "CGI": 11_000,
    "Thales": 24_000,
    "Leonardo": 19_000,
    "Zoom": 4_700,
    "UiPath": 1_400,
    "Intuit": 16_500,
    "HubSpot": 2_600,
    "Palantir": 2_900,
    "Visa": 35_900,
    "Thomson Reuters": 7_200,
}


# Revenue figures that are corporate-wide totals or data quality errors.
# These should NOT be used for market share estimation.
# Maps (canonical_company_name, segment_name) -> True
CORPORATE_WIDE_REVENUES = {
    # GLOBAL — corporate-wide totals (revenue is for entire company, not AI segment)
    ("Datadog", "IT Operations"),          # $2.6B total observability platform
    ("ZoomInfo", "Sales"),                 # $1.25B total data platform
    ("Workday", "HR"),                     # $8B total HCM+Finance ERP
    ("Snowflake", "Data Science & ML Platforms"),  # $5B total data warehouse
    ("Qualtrics", "Market Research"),       # $1.53B total XM suite
    ("Epic Systems", "Healthcare"),         # $5.7B total EHR platform
    ("GE Healthcare", "Healthcare"),        # $19.6B total medical devices
    ("Canva", "Creators"),                 # $4B total design suite
    ("Coursera", "Education"),             # $757M total MOOC platform
    ("GoHighLevel", "Home Services"),       # Marketing CRM, wrong segment
    ("Angi", "Home Services"),             # Marketplace leads, not FSM AI
    ("FICO", "Finance (Vertical)"),        # $1.99B total (credit scores + analytics)
    ("Zillow", "Real Estate"),             # $2.2B total marketplace
    ("CoStar Group", "Real Estate"),       # $2.74B total RE data platform
    ("Compass", "Real Estate"),            # $7B brokerage commissions
    ("Siemens", "Manufacturing + Supply Chain"),  # $90B industrial conglomerate
    ("C3.ai", "Manufacturing + Supply Chain"),    # Multi-vertical enterprise AI
    ("CCC Intelligent Solutions", "Insurance"),   # $945M total claims workflow
    ("Lemonade", "Insurance"),             # $527M insurance premiums, not AI tech
    ("Upstart", "Finance (Vertical)"),     # $1B loan origination fees
    ("Blue Yonder", "Manufacturing + Supply Chain"),  # $1.36B includes non-AI legacy

    # GLOBAL — data quality errors (wrong metric parsed as revenue)
    ("EvenUp", "Legal"),                   # $2B is VALUATION, not revenue
    ("ZestyAI", "Insurance"),             # "$3T decisions" corrupt extraction
    ("Fathom", "Note-taking / AI Meeting Assistants"),  # $17M is Series A funding

    # EU+CA — corporate-wide totals
    ("Coveo", "Copilots"),                 # $141M total used across 3 segments
    ("Coveo", "Marketing"),
    ("Coveo", "Customer Success"),
    ("Celonis", "Agent Platforms"),         # $900M total used across 3 segments
    ("Celonis", "Finance + Operations"),
    ("Celonis", "Manufacturing + Supply Chain"),
    ("Cohere", "Code / Software Development"),  # $240M total across 4 segments (Copilots is primary)
    ("Cohere", "Data Science & ML Platforms"),
    ("Cohere", "Government"),
    ("Dayforce", "HR"),                    # $1.76B total HCM across 2 segments
    ("Dayforce", "Finance + Operations"),
    ("SAP", "Finance + Operations"),       # €36.8B ERP conglomerate
    ("Mentimeter", "Presentations"),        # Polling platform, not AI slides
    ("JetBrains", "Code / Software Development"),  # $593M total multi-IDE suite
    ("OpenText", "IT Operations"),         # $5.17B total info mgmt conglomerate
    ("Synthesia", "Marketing"),            # AI video, not marketing automation
    ("Brandwatch", "Market Research"),      # Social listening platform
    ("Léger", "Market Research"),           # Traditional polling firm
    ("Kahoot!", "Education"),              # $168M total edtech platform
    ("D2L (Desire2Learn)", "Education"),   # $205M total LMS suite
    ("IFS", "Home Services"),              # €1.228B total ERP+FSM
    ("Geotab", "Home Services"),           # Fleet telematics, wrong segment
    ("Planon", "Home Services"),           # IWMS for commercial, not home services
    ("Thales", "Government"),              # €22.1B defense conglomerate
    ("Leonardo", "Government"),            # €17.8B defense conglomerate
    ("CGI", "Government"),                 # CA$14.7B IT services conglomerate
    ("Sopra Steria", "Government"),        # €5.6B IT services firm
    ("MDA Space", "Government"),           # Space/satellite company
    ("Siemens", "Manufacturing + Supply Chain"),  # EU+CA entry too
    ("ABB", "Manufacturing + Supply Chain"),  # $33.2B industrial conglomerate
    ("Dassault Systèmes", "Manufacturing + Supply Chain"),  # €6.24B PLM platform
    ("Scout24", "Real Estate"),            # €650M portal, AI is feature
    ("Rightmove", "Real Estate"),          # £425.1M portal, AI is feature
    ("Featurespace*", "Finance (Vertical)"),  # $950M is acquisition price
    ("Tessl", "Code / Software Development"),  # $125M is funding, pre-revenue
    ("Genesy AI", "Sales"),                # $5.4M is seed round
    ("Freepik / Slidesgo", "Presentations"),  # $115M total creative assets
}


def nullify_corporate_revenues(conn):
    """Set revenue_usd_m = NULL for entries identified as corporate-wide or data errors.
    Must run AFTER normalization (so canonical names match) and BEFORE estimation."""
    cur = conn.cursor()
    count = 0
    for (company, segment) in CORPORATE_WIDE_REVENUES:
        cur.execute("""
            UPDATE company_segments
            SET revenue_usd_m = NULL
            WHERE company_id IN (SELECT company_id FROM companies WHERE canonical_name = ?)
              AND segment_id IN (SELECT segment_id FROM segments WHERE name = ?)
              AND revenue_usd_m IS NOT NULL
        """, (company, segment))
        count += cur.rowcount
    conn.commit()
    return count


def normalize_name(raw_name):
    """Return canonical company name for a raw report name."""
    raw_name = raw_name.strip()
    return COMPANY_ALIASES.get(raw_name, raw_name)


def apply_normalization(conn):
    """
    Merge duplicate company records after parsing.

    Steps:
    1. For each alias pair, find if both raw and canonical exist as separate rows
       in the companies table.  If so, re-point all company_segments FK references
       from the raw row to the canonical row, then delete the raw row.
       If only the raw row exists (canonical not yet created), rename it in place.
    2. Set parent_company links from PARENT_COMPANIES.
    3. Set known_total_revenue_usd_m from KNOWN_CORPORATE_REVENUE.
    """
    cur = conn.cursor()

    # Step 1: Merge aliases
    for raw_name, canonical in COMPANY_ALIASES.items():
        if raw_name == canonical:
            continue

        cur.execute("SELECT company_id FROM companies WHERE canonical_name = ?", (raw_name,))
        raw_row = cur.fetchone()
        cur.execute("SELECT company_id FROM companies WHERE canonical_name = ?", (canonical,))
        canon_row = cur.fetchone()

        if raw_row and canon_row:
            raw_id, canon_id = raw_row[0], canon_row[0]
            if raw_id != canon_id:
                # Move company_segments from raw to canonical; ignore conflicts
                # (same segment already attributed to canonical).
                cur.execute(
                    "UPDATE OR IGNORE company_segments SET company_id = ? WHERE company_id = ?",
                    (canon_id, raw_id),
                )
                # Drop any remaining rows that caused UNIQUE conflicts
                cur.execute("DELETE FROM company_segments WHERE company_id = ?", (raw_id,))
                cur.execute("DELETE FROM companies WHERE company_id = ?", (raw_id,))
        elif raw_row and not canon_row:
            # Canonical company not yet in DB — just rename
            cur.execute(
                "UPDATE companies SET canonical_name = ? WHERE canonical_name = ?",
                (canonical, raw_name),
            )

    # Step 2: Set parent companies
    for child, parent in PARENT_COMPANIES.items():
        cur.execute(
            "UPDATE companies SET parent_company = ? WHERE canonical_name = ?",
            (parent, child),
        )

    # Step 3: Set known corporate revenue caps
    for company, revenue_m in KNOWN_CORPORATE_REVENUE.items():
        cur.execute(
            "UPDATE companies SET known_total_revenue_usd_m = ? WHERE canonical_name = ?",
            (revenue_m, company),
        )

    conn.commit()
