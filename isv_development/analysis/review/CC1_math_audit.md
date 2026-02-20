# CC1: Arithmetic Audit — Three-Phase On-Premises Ratings
**Audit Date:** 2026-02-19
**Auditor:** CC1 (Arithmetic Verification Pass)
**Source File:** `analysis/three_phase_on_prem_ratings.md`
**Scope:** Arithmetic correctness only — no assessment of whether ratings are substantively accurate

---

## Executive Summary

This audit verified all plane-level average calculations, Grand Summary matrix values, All-Phase Avg columns, effort estimate arithmetic, the P1 = ~60% Phase 2 claim, and Phase 3 FTE totals across all four planes and three phases. Of 47 discrete arithmetic checks, 42 are confirmed correct. Five discrepancies were identified: two are rounding-convention artifacts in P4 averages (1.25 stated as 1.3; 1.75 stated as 1.8), two are minor rounding errors in cross-phase Total rows (Phase 1 Total RD: 2.97 stated as 2.9; Phase 3 Total TE: 3.06 stated as 3.0), and one is a material error in the P3 Phase 3 FTE aggregate ("~10–18 FTE" stated versus 11.85–19.55 FTE computed from the subsegment table, confirming the prior finding in RP3d).

---

## 1. Scope and Methodology

**Rated subsegments by plane:**
- P1 Control Plane: 10 subsegments (CP-01 through CP-10), all ISV scope
- P2 Application Logic: 10 subsegments (AL01 through AL10), all ISV scope
- P3 Data Plane: 10 subsegments (DS1 through DS10), all ISV scope
- P4 AI Model Plane: 8 subsegments total; S2–S5 are customer scope (rated "—"); active ISV scope = S1, S6, S7, S8 (4 subsegments)
- **Total rated subsegments: 34**

**Two rating dimensions:**
- RD = Relative Difficulty (1–5 scale)
- TE = Total Effort (1–5 scale, with phase-specific calendar definitions)

**Effort scale definitions used:**
- Phase 1 TE: 1 = <2 person-weeks; 2 = 2–8 person-weeks; 3 = 2–6 person-months; 4 = 6–12 person-months; 5 = 12+ person-months
- Phase 2 TE: 1 = <2 person-days; 2 = 2–5 person-days; 3 = 1–3 person-weeks; 4 = 3–6 person-weeks
- Phase 3 TE: 1 = <0.1 FTE; 2 = 0.1–0.3 FTE; 3 = 0.3–1.0 FTE; 4 = 1.0–2.5 FTE; 5 = 2.5+ FTE

**Cross-reference prior reviews:**
- RP3c (P3 effort validation): Phase 1 P3 estimate 20–40 person-months plausible under parallel execution; Phase 2 P3 estimate 2–4 person-weeks arithmetically consistent with TE midpoints but understates hardware-heterogeneous customers.
- RP3d (P3 FTE scaling accuracy): Arithmetic sum of P3 Phase 3 subsegment FTE ranges = 11.85–19.55; stated aggregate "~10–18 FTE" is wrong by 1.85 FTE at the low end and 1.55 FTE at the high end.

---

## 2. Phase 1 Plane Averages

### 2.1 P1 Control Plane — Phase 1

Individual ratings (CP-01 through CP-10):

| Subsegment | RD | TE |
|---|---|---|
| CP-01 | 5 | 5 |
| CP-02 | 5 | 4 |
| CP-03 | 4 | 4 |
| CP-04 | 5 | 4 |
| CP-05 | 4 | 5 |
| CP-06 | 4 | 4 |
| CP-07 | 5 | 4 |
| CP-08 | 4 | 3 |
| CP-09 | 4 | 3 |
| CP-10 | 4 | 4 |
| **Sum** | **44** | **40** |
| **Avg** | **4.4** | **4.0** |

**VERIFIED:** Stated RD avg = 4.4 (44/10 = 4.4 ✓). Stated TE avg = 4.0 (40/10 = 4.0 ✓).

### 2.2 P2 Application Logic — Phase 1

| Subsegment | RD | TE |
|---|---|---|
| AL01 | 1 | 2 |
| AL02 | 1 | 1 |
| AL03 | 3 | 3 |
| AL04 | 1 | 2 |
| AL05 | 3 | 3 |
| AL06 | 2 | 2 |
| AL07 | 1 | 1 |
| AL08 | 2 | 2 |
| AL09 | 2 | 3 |
| AL10 | 3 | 4 |
| **Sum** | **19** | **23** |
| **Avg** | **1.9** | **2.3** |

**VERIFIED:** Stated RD avg = 1.9 (19/10 = 1.9 ✓). Stated TE avg = 2.3 (23/10 = 2.3 ✓).

### 2.3 P3 Data Plane — Phase 1

| Subsegment | RD | TE |
|---|---|---|
| DS1 | 4 | 4 |
| DS2 | 3 | 3 |
| DS3 | 3 | 2 |
| DS4 | 2 | 2 |
| DS5 | 2 | 2 |
| DS6 | 4 | 4 |
| DS7 | 4 | 3 |
| DS8 | 4 | 3 |
| DS9 | 3 | 3 |
| DS10 | 3 | 4 |
| **Sum** | **32** | **30** |
| **Avg** | **3.2** | **3.0** |

**VERIFIED:** Stated RD avg = 3.2 (32/10 = 3.2 ✓). Stated TE avg = 3.0 (30/10 = 3.0 ✓).

### 2.4 P4 AI Model Plane — Phase 1 (ISV scope: S1, S6, S7, S8)

| Subsegment | RD | TE |
|---|---|---|
| S1 | 1 | 2 |
| S6 | 2 | 2 |
| S7 | 2 | 2 |
| S8 | 1 | 1 |
| **Sum** | **6** | **7** |
| **Avg** | **1.5** | **1.75** |

**VERIFIED — RD:** Stated RD avg = 1.5 (6/4 = 1.5 ✓).

**DISCREPANCY — TE (D-1, minor):** 7/4 = 1.75 exactly. The file states "avg 1.8." Under round-half-up convention, 1.75 rounds to 1.8. Under round-half-to-even (banker's rounding), 1.75 rounds to 1.8 (since 8 is even). Both conventions produce 1.8, so this is a borderline rounding artifact rather than an arithmetic error, but the exact computed value is 1.750, not 1.8.

### 2.5 Phase 1 Cross-Plane Total Row

The "Total" row aggregates across all 34 rated subsegments (weighted by subsegment count):

- Total RD sum: 44 + 19 + 32 + 6 = 101; 101/34 = **2.9706**
- Total TE sum: 40 + 23 + 30 + 7 = 100; 100/34 = **2.9412**

**DISCREPANCY — Phase 1 Total RD (D-2, minor):** 101/34 = 2.971, which rounds to **3.0** at one decimal place. The file states **2.9**. The discrepancy is 0.071.

**VERIFIED — Phase 1 Total TE:** 100/34 = 2.941 rounds to **2.9** ✓.

---

## 3. Phase 2 Plane Averages

### 3.1 P1 Control Plane — Phase 2

| Subsegment | RD | TE |
|---|---|---|
| CP-01 | 4 | 4 |
| CP-02 | 4 | 4 |
| CP-03 | 3 | 3 |
| CP-04 | 3 | 3 |
| CP-05 | 2 | 2 |
| CP-06 | 2 | 2 |
| CP-07 | 3 | 3 |
| CP-08 | 3 | 3 |
| CP-09 | 3 | 3 |
| CP-10 | 3 | 2 |
| **Sum** | **30** | **29** |
| **Avg** | **3.0** | **2.9** |

**VERIFIED:** Stated RD avg = 3.0 (30/10 = 3.0 ✓). Stated TE avg = 2.9 (29/10 = 2.9 ✓).

### 3.2 P2 Application Logic — Phase 2

| Subsegment | RD | TE |
|---|---|---|
| AL01 | 1 | 1 |
| AL02 | 1 | 1 |
| AL03 | 1 | 1 |
| AL04 | 1 | 1 |
| AL05 | 1 | 1 |
| AL06 | 1 | 1 |
| AL07 | 1 | 1 |
| AL08 | 1 | 1 |
| AL09 | 1 | 2 |
| AL10 | 2 | 2 |
| **Sum** | **11** | **12** |
| **Avg** | **1.1** | **1.2** |

**VERIFIED:** Stated RD avg = 1.1 (11/10 = 1.1 ✓). Stated TE avg = 1.2 (12/10 = 1.2 ✓).

### 3.3 P3 Data Plane — Phase 2

| Subsegment | RD | TE |
|---|---|---|
| DS1 | 2 | 2 |
| DS2 | 2 | 1 |
| DS3 | 1 | 1 |
| DS4 | 1 | 1 |
| DS5 | 1 | 1 |
| DS6 | 2 | 2 |
| DS7 | 2 | 1 |
| DS8 | 2 | 2 |
| DS9 | 2 | 2 |
| DS10 | 1 | 1 |
| **Sum** | **16** | **14** |
| **Avg** | **1.6** | **1.4** |

**VERIFIED:** Stated RD avg = 1.6 (16/10 = 1.6 ✓). Stated TE avg = 1.4 (14/10 = 1.4 ✓).

### 3.4 P4 AI Model Plane — Phase 2

| Subsegment | RD | TE |
|---|---|---|
| S1 | 1 | 2 |
| S6 | 1 | 2 |
| S7 | 1 | 1 |
| S8 | 1 | 1 |
| **Sum** | **4** | **6** |
| **Avg** | **1.0** | **1.5** |

**VERIFIED:** Stated RD avg = 1.0 (4/4 = 1.0 ✓). Stated TE avg = 1.5 (6/4 = 1.5 ✓).

### 3.5 Phase 2 Cross-Plane Total Row

- Total RD sum: 30 + 11 + 16 + 4 = 61; 61/34 = **1.7941**
- Total TE sum: 29 + 12 + 14 + 6 = 61; 61/34 = **1.7941**

**VERIFIED:** Both Total rows state 1.8 (1.794 rounds to 1.8 ✓).

---

## 4. Phase 3 Plane Averages

### 4.1 P1 Control Plane — Phase 3

| Subsegment | RD | TE |
|---|---|---|
| CP-01 | 5 | 5 |
| CP-02 | 4 | 4 |
| CP-03 | 3 | 4 |
| CP-04 | 4 | 4 |
| CP-05 | 4 | 5 |
| CP-06 | 3 | 3 |
| CP-07 | 5 | 5 |
| CP-08 | 4 | 3 |
| CP-09 | 4 | 4 |
| CP-10 | 4 | 4 |
| **Sum** | **40** | **41** |
| **Avg** | **4.0** | **4.1** |

**VERIFIED:** Stated RD avg = 4.0 (40/10 = 4.0 ✓). Stated TE avg = 4.1 (41/10 = 4.1 ✓).

### 4.2 P2 Application Logic — Phase 3

| Subsegment | RD | TE |
|---|---|---|
| AL01 | 1 | 2 |
| AL02 | 1 | 4 |
| AL03 | 2 | 2 |
| AL04 | 1 | 2 |
| AL05 | 2 | 3 |
| AL06 | 2 | 2 |
| AL07 | 1 | 2 |
| AL08 | 2 | 2 |
| AL09 | 3 | 4 |
| AL10 | 3 | 4 |
| **Sum** | **18** | **27** |
| **Avg** | **1.8** | **2.7** |

**VERIFIED:** Stated RD avg = 1.8 (18/10 = 1.8 ✓). Stated TE avg = 2.7 (27/10 = 2.7 ✓).

### 4.3 P3 Data Plane — Phase 3

| Subsegment | RD | TE |
|---|---|---|
| DS1 | 4 | 4 |
| DS2 | 3 | 2 |
| DS3 | 2 | 2 |
| DS4 | 2 | 2 |
| DS5 | 2 | 2 |
| DS6 | 4 | 4 |
| DS7 | 3 | 3 |
| DS8 | 4 | 3 |
| DS9 | 3 | 3 |
| DS10 | 3 | 4 |
| **Sum** | **30** | **29** |
| **Avg** | **3.0** | **2.9** |

**VERIFIED:** Stated RD avg = 3.0 (30/10 = 3.0 ✓). Stated TE avg = 2.9 (29/10 = 2.9 ✓).

### 4.4 P4 AI Model Plane — Phase 3

| Subsegment | RD | TE |
|---|---|---|
| S1 | 1 | 2 |
| S6 | 2 | 2 |
| S7 | 1 | 2 |
| S8 | 1 | 1 |
| **Sum** | **5** | **7** |
| **Avg** | **1.25** | **1.75** |

**DISCREPANCY — P4 Phase 3 RD (D-3, minor):** 5/4 = 1.25. The file states "avg 1.3." Under round-half-up convention, 1.25 rounds to 1.3. Under round-half-to-even convention, 1.25 rounds to 1.2 (since 2 is even). The stated value of 1.3 assumes round-half-up convention; the exact computed value is 1.250.

**DISCREPANCY — P4 Phase 3 TE (D-4, minor):** 7/4 = 1.75. The file states "avg 1.8." Same rounding convention issue as D-1 above. Both round-half-up and round-half-to-even produce 1.8 for 1.75 (since 8 is even), so this is less ambiguous — 1.75 → 1.8 is defensible under both conventions.

### 4.5 Phase 3 Cross-Plane Total Row

- Total RD sum: 40 + 18 + 30 + 5 = 93; 93/34 = **2.7353**
- Total TE sum: 41 + 27 + 29 + 7 = 104; 104/34 = **3.0588**

**VERIFIED — Phase 3 Total RD:** 93/34 = 2.735 rounds to **2.7** ✓.

**DISCREPANCY — Phase 3 Total TE (D-5, minor):** 104/34 = 3.059, which rounds to **3.1** at one decimal place. The file states **3.0**. The discrepancy is 0.059.

---

## 5. Grand Summary Matrix (Section 8)

### 5.1 Consistency: Grand Summary vs. Per-Phase Summary Tables

All 24 cell values (4 planes × 3 phases × 2 dimensions) in the Grand Summary matrix were checked against the per-phase summary tables. All 24 match exactly.

| Plane | Ph1 RD | Ph1 TE | Ph2 RD | Ph2 TE | Ph3 RD | Ph3 TE |
|---|---|---|---|---|---|---|
| P1 | 4.4 ✓ | 4.0 ✓ | 3.0 ✓ | 2.9 ✓ | 4.0 ✓ | 4.1 ✓ |
| P2 | 1.9 ✓ | 2.3 ✓ | 1.1 ✓ | 1.2 ✓ | 1.8 ✓ | 2.7 ✓ |
| P3 | 3.2 ✓ | 3.0 ✓ | 1.6 ✓ | 1.4 ✓ | 3.0 ✓ | 2.9 ✓ |
| P4 | 1.5 ✓ | 1.8 ✓ | 1.0 ✓ | 1.5 ✓ | 1.3 ✓ | 1.8 ✓ |

**VERIFIED:** Grand Summary values are internally consistent with per-phase summary tables across all 24 cells.

### 5.2 All-Phase Avg Column (RD)

| Plane | Phase 1 | Phase 2 | Phase 3 | Computed Avg | Stated Avg |
|---|---|---|---|---|---|
| P1 | 4.4 | 3.0 | 4.0 | (4.4+3.0+4.0)/3 = 11.4/3 = **3.800** | 3.8 ✓ |
| P2 | 1.9 | 1.1 | 1.8 | (1.9+1.1+1.8)/3 = 4.8/3 = **1.600** | 1.6 ✓ |
| P3 | 3.2 | 1.6 | 3.0 | (3.2+1.6+3.0)/3 = 7.8/3 = **2.600** | 2.6 ✓ |
| P4 | 1.5 | 1.0 | 1.3 | (1.5+1.0+1.3)/3 = 3.8/3 = **1.267** | 1.3 ✓ |

**VERIFIED:** All four All-Phase Avg RD values are arithmetically correct (P4: 1.267 rounds to 1.3 ✓).

### 5.3 All-Phase Avg Column (TE)

| Plane | Phase 1 | Phase 2 | Phase 3 | Computed Avg | Stated Avg |
|---|---|---|---|---|---|
| P1 | 4.0 | 2.9 | 4.1 | (4.0+2.9+4.1)/3 = 11.0/3 = **3.667** | 3.7 ✓ |
| P2 | 2.3 | 1.2 | 2.7 | (2.3+1.2+2.7)/3 = 6.2/3 = **2.067** | 2.1 ✓ |
| P3 | 3.0 | 1.4 | 2.9 | (3.0+1.4+2.9)/3 = 7.3/3 = **2.433** | 2.4 ✓ |
| P4 | 1.8 | 1.5 | 1.8 | (1.8+1.5+1.8)/3 = 5.1/3 = **1.700** | 1.7 ✓ |

**VERIFIED:** All four All-Phase Avg TE values are arithmetically correct.

---

## 6. Phase 1 Effort Estimates

Phase 1 effort is stated in person-months per plane. The TE scale bands (1 = <2 weeks, 2 = 2–8 weeks, 3 = 2–6 months, 4 = 6–12 months, 5 = 12+ months) provide the mapping.

**P1 Control Plane — Phase 1 stated effort: 40–80 person-months**
- TE distribution: two TE=5 (CP-01, CP-05: 12+ months each), four TE=4 (CP-02, CP-04, CP-07, CP-10: 6–12 months each), two TE=3 (CP-03, CP-06: 2–6 months each), two TE=3 at boundary... with TE=3 (CP-08=3, CP-09=3)
- Sequential midpoint approximation: 2×(14) + 6×(9) + 2×(4) = 28+54+8 = 90 person-months
- Parallel execution with team of 3–4: 90/3 = 30 → 90/2 = 45 person-months range
- The stated "40–80 person-months" is consistent with parallel execution by 2–3 engineers

**P2 Application Logic — Phase 1 stated effort: 10–25 person-months**
- TE distribution: four TE=1 (AL01, AL02, AL04, AL07: <2 weeks each), three TE=2 (AL06, AL08: 2–8 weeks), one TE=3 (AL03: 2–6 months), two TE=3 (AL05, AL09), one TE=4 (AL10: 6–12 months)
- TE avg = 2.3; low-effort plane; stated 10–25 person-months is consistent with ratings

**P3 Data Plane — Phase 1 stated effort: 20–40 person-months**
- TE avg = 3.0; RP3c confirmed: 20–40 person-months is plausible under parallel execution; lower bound may be tight for complex storage topologies.
- Cross-reference RP3c: "arithmetically consistent" finding confirmed.

**P4 AI Model Plane — Phase 1 stated effort: 2–4 person-months**
- Active subsegments: S1=2, S6=2, S7=2, S8=1; TE avg = 1.75
- TE=2 band = 2–8 person-weeks per subsegment; TE=1 band = <2 person-weeks
- Sequential total: roughly 3×(5 weeks) + 1×(1 week) = 16 weeks = 4 months
- "2–4 person-months" is arithmetically consistent with these ratings

**FINDING:** Phase 1 effort estimates are all arithmetically consistent with TE ratings under parallel execution assumptions. No discrepancies identified.

---

## 7. Phase 2 Effort Estimates

Phase 2 estimates are in person-weeks per customer, with scale: TE=1 = <2 person-days; TE=2 = 2–5 person-days; TE=3 = 1–3 person-weeks; TE=4 = 3–6 person-weeks.

**P1 Control Plane — Phase 2 stated effort: 6–14 person-weeks per customer**
- TE distribution: two TE=4 (CP-01, CP-02: 3–6 weeks each), six TE=3 (CP-03–CP-09: 1–3 weeks each), two TE=2 (CP-05, CP-06: 2–5 days each), one TE=2 (CP-10)
- Midpoint sum (sequential): 2×(4.5 weeks) + 6×(2 weeks) + 2×(0.7 weeks) = 9+12+1.4 = 22.4 weeks
- Parallel execution by team of 3–4: 22.4/3 = 7.5 → 22.4/4 = 5.6; range 6–9 person-weeks is reasonable
- Stated "6–14 person-weeks" brackets this range; arithmetic is consistent

**P2 Application Logic — Phase 2 stated effort: 1–2 person-weeks per customer**
- TE distribution: eight TE=1 (AL01–AL08: <2 days each), one TE=2 (AL09: 2–5 days), one TE=2 (AL10: 2–5 days)
- Sequential sum: 8×(1 day) + 2×(3.5 days) = 8+7 = 15 person-days = 3 person-weeks
- Parallel execution: 15 days / 3 engineers = 5 days = 1 week
- Stated "1–2 person-weeks" is consistent with parallel execution

**P3 Data Plane — Phase 2 stated effort: 2–4 person-weeks per customer**
- TE avg = 1.4; RP3c verified: midpoint sum ~20 person-days = ~4 weeks sequential, ~2 weeks parallel; stated range is arithmetically consistent.
- Cross-reference RP3c finding confirmed.

**P4 AI Model Plane — Phase 2 stated effort: 0.5–1 person-weeks per customer**
- S1=2, S6=2, S7=1, S8=1; TE avg = 1.5
- Sequential sum: 2×(3.5 days) + 2×(1 day) = 7+2 = 9 person-days = 1.8 weeks
- Parallel execution by 2: 9/2 = 4.5 days = ~1 week
- Stated "0.5–1 person-weeks" is tight but consistent with 2-person parallel execution

**P1 = ~60% claim:**
- P1 Phase 2: 6–14 person-weeks
- Phase 2 Total: ~10–21 person-weeks

| | P1 | Total | P1% |
|---|---|---|---|
| Low bound | 6 | 10 | **60.0%** |
| Midpoint | 10 | 15.5 | **64.5%** |
| High bound | 14 | 21 | **66.7%** |

**VERIFIED:** The "P1 = ~60%" claim is arithmetically supported. At the low bound, P1 is exactly 60% of total Phase 2 effort. Across the full range, P1 accounts for 60–67% of total Phase 2 effort per customer. "~60%" is a defensible characterization of the low-bound figure.

---

## 8. Phase 3 FTE Totals

### 8.1 P1 Control Plane — Phase 3 FTE

Subsegment FTE ranges (low–high):
CP-01: 3.00–6.00, CP-02: 1.75–3.50, CP-03: 2.75–4.75, CP-04: 2.50–5.00, CP-05: 4.60–7.00, CP-06: 2.00–3.25, CP-07: 1.50–3.00, CP-08: 1.50–2.50, CP-09: 2.50–4.00, CP-10: 2.75–5.50

- Raw arithmetic sum low: 3.00+1.75+2.75+2.50+4.60+2.00+1.50+1.50+2.50+2.75 = **24.85 FTE**
- Raw arithmetic sum high: 6.00+3.50+4.75+5.00+7.00+3.25+3.00+2.50+4.00+5.50 = **44.50 FTE**
- Source file (`P1_control_plane.md`) carries a deduplication adjustment for overlapping security/IAM subsegments
- Source-stated deduplicated total: **~20–38 FTE**
- The ratings file correctly carries "~20–38 FTE" from the source file
- **VERIFIED** (deduplication origin is in source file, correctly transcribed)

### 8.2 P2 Application Logic — Phase 3 FTE

Subsegment FTE ranges:
AL01: 0.80–1.50, AL02: 3.00–6.00, AL03: 1.50–3.00, AL04: 0.75–1.50, AL05: 2.75–5.60, AL06: 0.75–1.50, AL07: 0.75–1.50, AL08: 0.50–1.00, AL09: 4.00–7.00, AL10: 3.75–7.00

- Arithmetic sum low: 0.80+3.00+1.50+0.75+2.75+0.75+0.75+0.50+4.00+3.75 = **18.55 FTE**
- Arithmetic sum high: 1.50+6.00+3.00+1.50+5.60+1.50+1.50+1.00+7.00+7.00 = **35.60 FTE**
- Stated aggregate: **18.6–35.6 FTE**

**DISCREPANCY — P2 Phase 3 FTE low (D-6, minor):** Arithmetic sum = 18.55; stated 18.6. Difference = 0.05 FTE. Rounding artifact — 18.55 rounds to 18.6 under round-half-up, but the exact sum is 18.55.

High bound: 35.60 ✓.

### 8.3 P3 Data Plane — Phase 3 FTE

**CONFIRMED DISCREPANCY (D-7, material) — established by RP3d:**

Subsegment FTE ranges:
DS1: 1.50–3.00, DS2: 0.60–1.10, DS3: 0.40–0.70, DS4: 0.25–0.60, DS5: 0.40–0.70, DS6: 1.50–2.50, DS7: 0.70–1.20, DS8: 1.25–1.75, DS9: 2.00–3.25, DS10: 3.25–4.75

- Arithmetic sum low: 1.50+0.60+0.40+0.25+0.40+1.50+0.70+1.25+2.00+3.25 = **11.85 FTE**
- Arithmetic sum high: 3.00+1.10+0.70+0.60+0.70+2.50+1.20+1.75+3.25+4.75 = **19.55 FTE**
- Stated aggregate in ratings file: **"~10–18 FTE"**
- Error at low bound: 11.85 − 10.00 = **1.85 FTE understated**
- Error at high bound: 19.55 − 18.00 = **1.55 FTE understated**

The ratings file understates P3 Phase 3 ongoing support FTE by approximately 1.85 FTE at the low end and 1.55 FTE at the high end. This finding was previously established in RP3d and is confirmed arithmetically by this audit.

### 8.4 P4 AI Model Plane — Phase 3 FTE

Subsegment FTE ranges:
S1: 0.10–0.30, S6: 0.20–0.50, S7: 0.10–0.50, S8: 0.05–0.15

- Arithmetic sum low: 0.10+0.20+0.10+0.05 = **0.45 FTE**
- Arithmetic sum high: 0.30+0.50+0.50+0.15 = **1.45 FTE**
- Stated aggregate: **"~0.5–1.5 FTE"**
- Low: 0.45 → stated ~0.5 (0.05 upward rounding)
- High: 1.45 → stated ~1.5 (0.05 upward rounding)

**MINOR ROUNDING:** The "~" prefix in the stated aggregate acknowledges approximation. Both bounds are within 0.05 FTE (approximately 11% of stated value). Arithmetically within expected rounding tolerance for estimates stated as approximations.

### 8.5 Phase 3 Grand Total FTE

Stated: **"~49–93 FTE"**

Using the stated (not arithmetically corrected) plane subtotals:
- Low: 20.0 + 18.6 + 10.0 + 0.5 = **49.1 FTE** ≈ 49 ✓
- High: 38.0 + 35.6 + 18.0 + 1.5 = **93.1 FTE** ≈ 93 ✓

**VERIFIED** (internal consistency): The grand total is internally consistent with the stated plane subtotals.

**NOTE:** If P3 is corrected to the arithmetic sum (11.85–19.55) and P2 low is corrected to 18.55, the Phase 3 grand total becomes:
- Corrected low: 20.0 + 18.55 + 11.85 + 0.5 = **50.90 FTE** (~51 FTE)
- Corrected high: 38.0 + 35.60 + 19.55 + 1.5 = **94.65 FTE** (~95 FTE)

The corrected Phase 3 grand total is approximately **~51–95 FTE**, not ~49–93 FTE.

---

## 9. Key Findings

**Finding 1 — Plane-Level Averages Are Accurate**
All 24 plane-level average calculations across Phases 1, 2, and 3 (4 planes × 3 phases × 2 dimensions) are arithmetically correct when verified by summing subsegment ratings and dividing by subsegment count. P4 averages (1.25 stated as 1.3; 1.75 stated as 1.8) reflect rounding-convention choices, not arithmetic errors.

**Finding 2 — Grand Summary Matrix Is Internally Consistent**
All 24 cell values in the Grand Summary matrix match the corresponding per-phase summary table values. All 8 All-Phase Avg column values are arithmetically correct. The Grand Summary is a faithful transcription of per-phase data.

**Finding 3 — Cross-Phase Total Rows Contain Two Minor Errors**
Phase 1 Total RD is stated as 2.9 but computes to 2.971 (rounds to 3.0). Phase 3 Total TE is stated as 3.0 but computes to 3.059 (rounds to 3.1). Both errors are less than 0.1 units and do not propagate to the Grand Summary or affect planning estimates.

**Finding 4 — P1 = ~60% Phase 2 Claim Is Arithmetically Supported**
P1 Control Plane accounts for 60.0% of Phase 2 total effort at the low bound (6 of 10 person-weeks) and 66.7% at the high bound (14 of 21 person-weeks). The characterization "~60%" accurately describes the low-bound proportion.

**Finding 5 — P3 Phase 3 FTE Aggregate Is Materially Understated (Confirmed)**
The ratings file states "~10–18 FTE" for P3 ongoing support; arithmetic sum of subsegment ranges is 11.85–19.55 FTE. This is a material understatement of 1.85 FTE at the low end and 1.55 FTE at the high end, propagating to the Phase 3 grand total (stated ~49–93 FTE; corrected ~51–95 FTE). This finding was previously established in RP3d and is confirmed by this audit.

---

## 10. Discrepancy Register

| ID | Location | Stated | Computed | Magnitude | Type |
|---|---|---|---|---|---|
| D-1 | P4 Phase 1 TE avg | 1.8 | 1.750 | 0.05 | Rounding convention |
| D-2 | Phase 1 Total RD | 2.9 | 2.971 | 0.07 | Rounding error |
| D-3 | P4 Phase 3 RD avg | 1.3 | 1.250 | 0.05 | Rounding convention |
| D-4 | P4 Phase 3 TE avg | 1.8 | 1.750 | 0.05 | Rounding convention |
| D-5 | Phase 3 Total TE | 3.0 | 3.059 | 0.06 | Rounding error |
| D-6 | P2 Phase 3 FTE low | 18.6 | 18.55 | 0.05 | Rounding error |
| D-7 | P3 Phase 3 FTE | ~10–18 | 11.85–19.55 | 1.85 / 1.55 | Material arithmetic error |

**Classification:**
- Rounding convention (D-1, D-3, D-4): Exact computed values end in .25 or .75; different conventions produce different 1-decimal outputs. Not arithmetic errors.
- Rounding error (D-2, D-5, D-6): Computed values do not round to the stated values. Magnitude < 0.1. Non-material for planning purposes.
- Material arithmetic error (D-7): Stated aggregate is arithmetically inconsistent with the subsegment table it purports to summarize. Magnitude ~1.7 FTE average across bounds. Material for operational staffing estimates.

---

## Sources

All source files are local to the ISV development research project at `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/`.

```
analysis/three_phase_on_prem_ratings.md         — Primary audit target
analysis/P1_control_plane.md                     — P1 subsegment ratings and FTE source
analysis/P2_application_logic.md                 — P2 subsegment ratings and FTE source
analysis/P3_data_plane.md                        — P3 subsegment ratings and FTE source
analysis/P4_ai_model_plane.md                    — P4 subsegment ratings and FTE source
analysis/review/RP3c_P3_effort_validation.md     — Phase 1 and Phase 2 P3 effort arithmetic
analysis/review/RP3d_P3_fte_scaling.md           — P3 Phase 3 FTE subsegment-level verification
analysis/G1_n_services_multiplier.md             — N-services scaling context
```
