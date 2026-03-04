#!/usr/bin/env python3
"""Pipeline orchestrator: schema -> parse -> normalize -> estimate -> analyze"""

import sys
import time
from pathlib import Path

# Ensure the leaders/ directory is on sys.path so `from analysis.X import Y` works
LEADERS_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(LEADERS_DIR))

from analysis.schema import create_db
from analysis.parse_reports import parse_global_report, parse_eu_ca_report
from analysis.normalize import apply_normalization, nullify_corporate_revenues
from analysis.estimate import run_all_estimates
from analysis.analyze import export_csvs, generate_report


def main():
    start = time.time()

    print("=" * 60)
    print("AI Market Leaders — Cross-Segment Analysis Pipeline")
    print("=" * 60)

    # Step 1: Create DB + schema
    print("\n[1/6] Creating database and schema...")
    conn = create_db()
    print("  OK Database created")

    # Step 2: Parse global report
    print("\n[2/6] Parsing global report...")
    parse_global_report(conn)
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM company_segments cs"
        " JOIN segments s ON cs.segment_id = s.segment_id"
        " WHERE s.scope_id = 1"
    )
    global_count = cur.fetchone()[0]
    cur.execute(
        "SELECT COUNT(DISTINCT cs.company_id) FROM company_segments cs"
        " JOIN segments s ON cs.segment_id = s.segment_id"
        " WHERE s.scope_id = 1"
    )
    global_companies = cur.fetchone()[0]
    print(f"  OK {global_count} company-segment entries, {global_companies} unique companies")

    # Step 3: Parse EU+CA report
    print("\n[3/6] Parsing Europe + Canada report...")
    parse_eu_ca_report(conn)
    cur.execute(
        "SELECT COUNT(*) FROM company_segments cs"
        " JOIN segments s ON cs.segment_id = s.segment_id"
        " WHERE s.scope_id = 2"
    )
    euca_count = cur.fetchone()[0]
    cur.execute(
        "SELECT COUNT(DISTINCT cs.company_id) FROM company_segments cs"
        " JOIN segments s ON cs.segment_id = s.segment_id"
        " WHERE s.scope_id = 2"
    )
    euca_companies = cur.fetchone()[0]
    print(f"  OK {euca_count} company-segment entries, {euca_companies} unique companies")

    # Step 4: Normalize company names
    print("\n[4/6] Normalizing company names...")
    apply_normalization(conn)
    cur.execute("SELECT COUNT(*) FROM companies")
    total_companies = cur.fetchone()[0]
    print(f"  OK {total_companies} unique companies after normalization")

    # Step 4b: Nullify corporate-wide revenues
    print("  Nullifying corporate-wide / misclassified revenues...")
    nullified = nullify_corporate_revenues(conn)
    print(f"  OK {nullified} revenue entries nullified")

    # Step 5: Estimate market shares
    print("\n[5/6] Estimating market shares...")
    estimates = run_all_estimates(conn)
    print(
        f"  OK Stated: {estimates['stated']},"
        f" Revenue-derived: {estimates['revenue_derived']},"
        f" Rank heuristic: {estimates['rank_heuristic']}"
    )

    # Step 6: Generate outputs
    print("\n[6/6] Generating analysis outputs...")
    export_csvs(conn)
    generate_report(conn)
    print("  OK CSV files and analysis report written to output/")

    # Summary
    elapsed = time.time() - start
    print("\n" + "=" * 60)
    print(f"Pipeline complete in {elapsed:.1f}s")
    print("=" * 60)

    print("\nQuick Summary:")
    print(f"  Global: {global_count} entries across {global_companies} companies in 23 segments")
    print(f"  EU+CA:  {euca_count} entries across {euca_companies} companies in 23 segments")

    # Top multi-segment companies (Global)
    cur.execute("""
        SELECT c.canonical_name, COUNT(*) as cnt
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = 1
        GROUP BY c.canonical_name
        HAVING cnt > 1
        ORDER BY cnt DESC
        LIMIT 5
    """)
    print("\n  Top multi-segment companies (Global):")
    for name, cnt in cur.fetchall():
        print(f"    {name}: {cnt} segments")

    # Top multi-segment companies (EU+CA)
    cur.execute("""
        SELECT c.canonical_name, COUNT(*) as cnt
        FROM company_segments cs
        JOIN companies c ON cs.company_id = c.company_id
        JOIN segments s ON cs.segment_id = s.segment_id
        WHERE s.scope_id = 2
        GROUP BY c.canonical_name
        HAVING cnt > 1
        ORDER BY cnt DESC
        LIMIT 5
    """)
    print("\n  Top multi-segment companies (EU+CA):")
    for name, cnt in cur.fetchall():
        print(f"    {name}: {cnt} segments")

    conn.close()


if __name__ == "__main__":
    main()
