"""Market share estimation logic for the AI Market Leaders database.

Fills in estimated_share_pct and share_confidence columns in company_segments
using a three-tier approach:
  Tier 1: Stated market share (highest confidence)
  Tier 2: Revenue-derived from segment market size (medium confidence)
  Tier 3: Rank-based heuristic distribution (lowest confidence)

Requires SQLite 3.33+ for UPDATE...FROM syntax (standard on macOS Python 3.9+).
"""

import sqlite3


def estimate_stated_shares(conn: sqlite3.Connection) -> int:
    """Tier 1: Copy explicit market_share_pct to estimated_share_pct.

    Only updates rows where market_share_pct is already set and
    estimated_share_pct has not yet been filled (preserves any manual overrides).
    """
    cur = conn.cursor()
    cur.execute("""
        UPDATE company_segments
        SET estimated_share_pct = market_share_pct,
            share_confidence = 'stated'
        WHERE market_share_pct IS NOT NULL
          AND estimated_share_pct IS NULL
    """)
    conn.commit()
    return cur.rowcount


def estimate_revenue_derived(conn: sqlite3.Connection) -> int:
    """Tier 2: Compute share from revenue_usd_m / market_size_usd_m.

    Only runs on rows where:
      - revenue_usd_m is populated (bundled/unclear revenues are left NULL by parser)
      - the segment has a known market_size_usd_m (global scope segments only)
      - estimated_share_pct is still NULL

    Caps result at 100.0 to guard against data quality issues.

    Uses UPDATE...FROM syntax requiring SQLite >= 3.33 (macOS ships 3.39+).
    """
    cur = conn.cursor()
    cur.execute("""
        UPDATE company_segments
        SET estimated_share_pct = (company_segments.revenue_usd_m / s.market_size_usd_m) * 100.0,
            share_confidence = 'revenue_derived'
        FROM segments s
        WHERE company_segments.segment_id = s.segment_id
          AND company_segments.revenue_usd_m IS NOT NULL
          AND s.market_size_usd_m IS NOT NULL
          AND s.market_size_usd_m > 0
          AND company_segments.estimated_share_pct IS NULL
          AND company_segments.revenue_usd_m <= s.market_size_usd_m * 0.5
    """)
    conn.commit()
    return cur.rowcount


# Default rank-weight distribution for Tier 3.
# Ranks beyond 5 fall through to the diminishing formula in the loop.
# Weights sum to 87 (not 100) to reflect realistic concentration spread —
# the remaining budget is further trimmed by the long-tail reserve below.
_DEFAULT_RANK_WEIGHTS: dict[int, int] = {1: 30, 2: 22, 3: 16, 4: 11, 5: 8}


def _weight_for_rank(rank: int | None) -> int:
    """Return a numeric weight for a given rank position.

    Ranks 1-5 use the calibrated default distribution.
    Ranks 6+ use a diminishing linear formula floored at 1.
    NULL rank gets a modest default so the company still receives some share.
    """
    if rank is None:
        return 5
    if rank in _DEFAULT_RANK_WEIGHTS:
        return _DEFAULT_RANK_WEIGHTS[rank]
    # Rank 6 → 8, 7 → 6, 8 → 4, 9 → 2, 10+ → 1
    return max(1, 10 - (rank - 5) * 2)


def estimate_rank_heuristic(conn: sqlite3.Connection) -> int:
    """Tier 3: Apply rank-based distribution for remaining NULL estimates.

    For each segment:
      1. Sum shares already set by Tiers 1 and 2 (the "anchor").
      2. remaining = max(0, 100 - anchor_sum)
      3. Reserve 35% of remaining for long-tail competitors (rank 6+) not
         explicitly modelled; only distribute the heuristic_budget (65%).
      4. Assign each unestimated company a weight based on its rank.
      5. Distribute heuristic_budget proportionally, then cap each company
         at its per-rank maximum, iteratively redistributing excess to
         uncapped companies (up to 3 passes). Excess that cannot be
         redistributed stays in the long-tail reserve.

    If a segment's anchor already sums to >= 100 there is nothing left to
    distribute; those rows are left NULL.

    If a segment has no unestimated rows, it is silently skipped.
    """
    LONG_TAIL_RESERVE = 0.35
    # Maximum share any single company can receive from the heuristic, by rank
    _MAX_HEURISTIC_BY_RANK = {1: 25.0, 2: 20.0, 3: 15.0, 4: 12.0, 5: 10.0}
    DEFAULT_MAX = 8.0  # for ranks 6+

    cur = conn.cursor()

    cur.execute("SELECT DISTINCT segment_id FROM company_segments")
    segment_ids: list[int] = [row[0] for row in cur.fetchall()]

    count = 0
    for seg_id in segment_ids:
        # --- Sum of shares already estimated in this segment ---
        cur.execute("""
            SELECT COALESCE(SUM(estimated_share_pct), 0.0)
            FROM company_segments
            WHERE segment_id = ?
              AND estimated_share_pct IS NOT NULL
        """, (seg_id,))
        estimated_sum: float = cur.fetchone()[0]
        remaining: float = max(0.0, 100.0 - estimated_sum)

        if remaining <= 0.0:
            # Anchor already at or above 100%; nothing left to distribute.
            # Leave estimated_share_pct NULL so the caller can decide how to
            # handle over-allocated segments rather than silently zeroing out.
            continue

        # Apply long-tail reserve — only distribute 65% of remaining space
        heuristic_budget: float = remaining * (1.0 - LONG_TAIL_RESERVE)

        # --- Fetch unestimated rows for this segment ---
        cur.execute("""
            SELECT cs_id, rank
            FROM company_segments
            WHERE segment_id = ?
              AND estimated_share_pct IS NULL
            ORDER BY CASE WHEN rank IS NULL THEN 9999 ELSE rank END
        """, (seg_id,))
        unestimated: list[tuple[int, int | None]] = cur.fetchall()

        if not unestimated:
            continue

        # --- Build weight map ---
        weights: dict[int, float] = {
            cs_id: _weight_for_rank(rank)
            for cs_id, rank in unestimated
        }
        total_weight: float = sum(weights.values())

        if total_weight == 0:
            continue

        # --- Initial proportional allocation from budget ---
        # allocations: cs_id -> (rank, share)
        allocations: dict[int, tuple[int | None, float]] = {}
        for cs_id, rank in unestimated:
            share = heuristic_budget * weights[cs_id] / total_weight
            allocations[cs_id] = (rank, share)

        # --- Apply per-rank caps, iteratively redistribute excess (max 3 passes) ---
        for _pass in range(3):
            excess = 0.0
            capped: set[int] = set()
            for cs_id, (rank, share) in allocations.items():
                cap = _MAX_HEURISTIC_BY_RANK.get(rank, DEFAULT_MAX) if rank else DEFAULT_MAX
                if share > cap:
                    excess += share - cap
                    allocations[cs_id] = (rank, cap)
                    capped.add(cs_id)

            if excess <= 0.01:
                break

            # Redistribute excess to uncapped companies proportionally
            uncapped = {k: v for k, v in allocations.items() if k not in capped}
            if not uncapped:
                break  # all companies capped; excess returns to long-tail reserve
            uncapped_weight = sum(weights[cs_id] for cs_id in uncapped)
            if uncapped_weight <= 0:
                break
            for cs_id in uncapped:
                rank, share = allocations[cs_id]
                allocations[cs_id] = (rank, share + excess * weights[cs_id] / uncapped_weight)

        # --- Write allocations ---
        for cs_id, (rank, share) in allocations.items():
            cur.execute("""
                UPDATE company_segments
                SET estimated_share_pct = ?,
                    share_confidence = 'rank_heuristic'
                WHERE cs_id = ?
            """, (round(share, 2), cs_id))
            count += 1

    conn.commit()
    return count


def run_all_estimates(conn: sqlite3.Connection) -> dict[str, int]:
    """Run all three estimation tiers in order.

    Returns a dict with row-counts for each tier:
      {'stated': N, 'revenue_derived': N, 'rank_heuristic': N}
    """
    return {
        "stated": estimate_stated_shares(conn),
        "revenue_derived": estimate_revenue_derived(conn),
        "rank_heuristic": estimate_rank_heuristic(conn),
    }
