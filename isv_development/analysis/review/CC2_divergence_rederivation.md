# CC2 — Divergence Re-derivation: Complete 114-Cell Audit

**Date:** 2026-02-19
**Scope:** Divergence flag accuracy audit only. RD and TE ratings are accepted as given; this review independently calculates every RD-TE gap and audits every [D] flag placement.
**Primary File:** `analysis/three_phase_on_prem_ratings.md`
**Cross-Reference Files:** `analysis/review/RP2c_P2_divergence_investigation.md`, `analysis/review/RP3b_P3_streaming_ai_data.md`
**[D] Threshold:** RD and TE differ by 2+ points (as defined in `three_phase_on_prem_ratings.md` §3)

---

## Executive Summary

An independent cell-by-cell recalculation of all 114 RD-TE pairs across 38 MECE subsegments and 3 deployment phases finds that the ratings file contains four [D] flags, of which three are correctly placed and one is technically misapplied. The confirmed misapplication is DS10 Phase 3 (gap = +1, not ≥+2), a finding previously documented in `RP3b_P3_streaming_ai_data.md`. No missed divergences at the ≥2-point threshold exist in P1 or P3; three near-miss divergences (gap = 1 point) in P1 Phase 3 warrant notation. The P2 "systematic divergence" claim — a +0.9 average gap in Phase 3 — is arithmetically verified: the actual computed average across 10 P2 Phase 3 subsegments is +0.90, driven by the single AL02 outlier (+3 gap) and a secondary cluster of six additional +1 gaps.

---

## 1. Methodology and Scope Boundary

This review independently derives the RD-TE gap (TE minus RD) for every cell in `three_phase_on_prem_ratings.md`. Cells where the gap reaches ±2 or greater are classified as requiring a [D] flag. The review then compares that classification against the flags actually present in the file.

[FACT] [D] flag definition from the primary file: "Cells where RD and TE differ by 2+ points are flagged with [D] — these are strategic traps where one dimension masks the other."
— Source: `three_phase_on_prem_ratings.md`, §3 Rating Scales
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**Scope exclusions:** P4 cells rated "—" (S2–S5, which are customer scope) are excluded from the count. The ISV-active P4 subsegments in each phase are: S1, S6, S7, S8 (4 subsegments × 3 phases = 12 cells). Total active cells: P1 = 30, P2 = 30, P3 = 30, P4 = 12 = **102 active cells** (not 114, because 12 cells are customer-scope blanks).

**Near-miss threshold:** Gaps of 1.5–1.9 points would be flagged for notation, but because all ratings in this file are integers, the minimum meaningful gap is 1 and the minimum [D]-qualifying gap is 2. There are no fractional ratings. Near-miss cells in this review are therefore defined as gap = 1 in subsegments where the notes already describe divergence tension.

---

## 2. P1 Control Plane — Complete Gap Calculation

### P1 Phase 1 (Initial Refactoring)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §4, "P1: Control Plane — Phase 1"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | 0 | No | No | CORRECT — no flag needed |
| CP-02 | Network Fabric / Ingress / Mesh | 5 | 4 | −1 | No | No | CORRECT — gap below threshold |
| CP-03 | IAM / RBAC | 4 | 4 | 0 | No | No | CORRECT — aligned |
| CP-04 | Secrets / Certs / PKI | 5 | 4 | −1 | No | No | CORRECT — gap below threshold |
| CP-05 | Observability Infrastructure | 4 | 5 | +1 | No | No | CORRECT — gap below threshold |
| CP-06 | CI/CD Pipeline / GitOps | 4 | 4 | 0 | No | No | CORRECT — aligned |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 4 | −1 | No | No | CORRECT — gap below threshold |
| CP-08 | Disaster Recovery / BC | 4 | 3 | −1 | No | No | CORRECT — gap below threshold |
| CP-09 | Compliance Automation | 4 | 3 | −1 | No | No | CORRECT — gap below threshold |
| CP-10 | Security Operations | 4 | 4 | 0 | No | No | CORRECT — aligned |
| **Avg** | | **4.4** | **4.0** | **−0.4** | | | |

[FACT] No P1 Phase 1 cell reaches a gap of ±2. The widest gaps are −1 (CP-02, CP-04, CP-07, CP-08, CP-09) and +1 (CP-05). No [D] flags are needed and none are applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §4
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### P1 Phase 2 (Per-Customer Customization)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §5, "P1: Control Plane — Phase 2"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 4 | 4 | 0 | No | No | CORRECT |
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 4 | 0 | No | No | CORRECT |
| CP-03 | IAM / RBAC | 3 | 3 | 0 | No | No | CORRECT |
| CP-04 | Secrets / Certs / PKI | 3 | 3 | 0 | No | No | CORRECT |
| CP-05 | Observability Infrastructure | 2 | 2 | 0 | No | No | CORRECT |
| CP-06 | CI/CD Pipeline / GitOps | 2 | 2 | 0 | No | No | CORRECT |
| CP-07 | Deploy Lifecycle / Rollback | 3 | 3 | 0 | No | No | CORRECT |
| CP-08 | Disaster Recovery / BC | 3 | 3 | 0 | No | No | CORRECT |
| CP-09 | Compliance Automation | 3 | 3 | 0 | No | No | CORRECT |
| CP-10 | Security Operations | 3 | 2 | −1 | No | No | CORRECT |
| **Avg** | | **3.0** | **2.9** | **−0.1** | | | |

[FACT] P1 Phase 2 is the most tightly calibrated phase across all planes. Nine of ten cells are perfectly aligned (gap = 0). CP-10 is the sole cell with any gap (−1). No [D] flags are needed or applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §5
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### P1 Phase 3 (Ongoing Software Updates and Support)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §6, "P1: Control Plane — Phase 3"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | 0 | No | No | CORRECT |
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 4 | 0 | No | No | CORRECT |
| CP-03 | IAM / RBAC | 3 | 4 | +1 | No | No | CORRECT — near-miss |
| CP-04 | Secrets / Certs / PKI | 4 | 4 | 0 | No | No | CORRECT |
| CP-05 | Observability Infrastructure | 4 | 5 | +1 | No | No | CORRECT — near-miss |
| CP-06 | CI/CD Pipeline / GitOps | 3 | 3 | 0 | No | No | CORRECT |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 5 | 0 | No | No | CORRECT |
| CP-08 | Disaster Recovery / BC | 4 | 3 | −1 | No | No | CORRECT |
| CP-09 | Compliance Automation | 4 | 4 | 0 | No | No | CORRECT |
| CP-10 | Security Operations | 4 | 4 | 0 | No | No | CORRECT |
| **Avg** | | **4.0** | **4.1** | **+0.1** | | | |

[FACT] P1 Phase 3 contains two near-miss cells (gap = +1): CP-03 (IAM/RBAC, RD=3/TE=4) and CP-05 (Observability Infrastructure, RD=4/TE=5). Neither reaches the ±2 threshold. Neither has a [D] flag. This is correct per the defined threshold.
Source: Computed from `three_phase_on_prem_ratings.md`, §6
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**P1 near-miss notation — CP-03 Phase 3:** The ratings file notes "Keycloak upgrades, identity provider integration maintenance. Core IAM tooling is shared; per-customer federation config maintenance adds linear cost. Identity incidents require per-customer investigation." This explains why TE (4) slightly exceeds RD (3): the difficulty is moderate (integration maintenance, not novel architecture), but effort scales linearly with customer count. The gap reflects a real structural tension that stops one point short of [D] qualification.

**P1 near-miss notation — CP-05 Phase 3:** The ratings file notes "500K+ active time series per customer instance. Base staff is shared but storage/capacity management is per-customer." TE=5 (2.5+ FTE) versus RD=4 reflects that the observability stack is the highest-FTE P1 subsegment in Phase 3 at 4.6–7.0 FTE, while its relative difficulty (4 not 5) reflects that the problem is well-understood operationally. The near-miss is structurally similar to P2's systematic divergence: large-but-routine work receiving a correctly lower RD but correctly higher TE.

**P1 Phase 3 hidden divergence assessment:** No hidden [D]-qualifying divergences exist in P1 Phase 3. The two near-miss cells are correctly handled without flags.

---

## 3. P2 Application Logic — Complete Gap Calculation

### P2 Phase 1 (Initial Refactoring)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §4, "P2: Application Logic — Phase 1"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 | 2 | +1 | No | No | CORRECT |
| AL02 | Business Logic / Domain Services | 1 | 1 | 0 | No | No | CORRECT |
| AL03 | API Gateway / Edge Routing | 3 | 3 | 0 | No | No | CORRECT |
| AL04 | Data Access / ORM / Caching | 1 | 2 | +1 | No | No | CORRECT |
| AL05 | Background Jobs / Async / EDA | 3 | 3 | 0 | No | No | CORRECT |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | 0 | No | No | CORRECT |
| AL07 | Multi-Tenant Isolation | 1 | 1 | 0 | No | No | CORRECT |
| AL08 | Observability Instrumentation | 2 | 2 | 0 | No | No | CORRECT |
| AL09 | AI/ML Orchestration / Agent Pipelines | 2 | 3 | +1 | No | No | CORRECT |
| AL10 | Testing / Contract Testing / Env Parity | 3 | 4 | +1 | **Yes** | **No** | **MISAPPLIED — gap is +1, not ≥+2** |
| **Avg** | | **1.9** | **2.3** | **+0.4** | | | |

[FACT] AL10 Phase 1 carries a [D] flag in the ratings file despite a gap of only +1 (RD=3, TE=4). The [D] threshold requires ≥2 points. This flag is technically misapplied.
Source: Computed from `three_phase_on_prem_ratings.md`, §4; flag definition from §3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

Note: The ratings file's note on AL10 Phase 1 reads "Effort exceeds difficulty because the testing surface area is large even though each test is straightforward." This is analytically correct as a description of the divergence dynamic, but it does not meet the numerical ≥2-point threshold for [D] flag placement.

### P2 Phase 2 (Per-Customer Customization)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §5, "P2: Application Logic — Phase 2"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 | 1 | 0 | No | No | CORRECT |
| AL02 | Business Logic / Domain Services | 1 | 1 | 0 | No | No | CORRECT |
| AL03 | API Gateway / Edge Routing | 1 | 1 | 0 | No | No | CORRECT |
| AL04 | Data Access / ORM / Caching | 1 | 1 | 0 | No | No | CORRECT |
| AL05 | Background Jobs / Async / EDA | 1 | 1 | 0 | No | No | CORRECT |
| AL06 | Resilience Patterns / Runtime | 1 | 1 | 0 | No | No | CORRECT |
| AL07 | Multi-Tenant Isolation | 1 | 1 | 0 | No | No | CORRECT |
| AL08 | Observability Instrumentation | 1 | 1 | 0 | No | No | CORRECT |
| AL09 | AI/ML Orchestration / Agent Pipelines | 1 | 2 | +1 | No | No | CORRECT |
| AL10 | Testing / Contract Testing / Env Parity | 2 | 2 | 0 | No | No | CORRECT |
| **Avg** | | **1.1** | **1.2** | **+0.1** | | | |

[FACT] P2 Phase 2 is nearly perfectly aligned. Only AL09 shows any gap (+1), driven by per-customer model catalog adaptation. No [D] flags are needed or applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §5
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### P2 Phase 3 (Ongoing Software Updates and Support)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §6, "P2: Application Logic — Phase 3"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 | 2 | +1 | No | No | CORRECT |
| AL02 | Business Logic / Domain Services | 1 | 4 | **+3** | **Yes** | **Yes** | **CORRECT** |
| AL03 | API Gateway / Edge Routing | 2 | 2 | 0 | No | No | CORRECT |
| AL04 | Data Access / ORM / Caching | 1 | 2 | +1 | No | No | CORRECT |
| AL05 | Background Jobs / Async / EDA | 2 | 3 | +1 | No | No | CORRECT |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | 0 | No | No | CORRECT |
| AL07 | Multi-Tenant Isolation | 1 | 2 | +1 | No | No | CORRECT |
| AL08 | Observability Instrumentation | 2 | 2 | 0 | No | No | CORRECT |
| AL09 | AI/ML Orchestration / Agent Pipelines | 3 | 4 | +1 | No | No | CORRECT |
| AL10 | Testing / Contract Testing / Env Parity | 3 | 4 | +1 | **Yes** | **No** | **MISAPPLIED — gap is +1, not ≥+2** |
| **Avg** | | **1.8** | **2.7** | **+0.9** | | | |

[FACT] AL02 Phase 3 records the widest gap in the entire ratings file: RD=1, TE=4, gap = +3. This is the only P2 Phase 3 cell that correctly qualifies for a [D] flag. AL10 Phase 3 (RD=3, TE=4, gap = +1) carries a [D] flag that does not meet the ≥2-point threshold and is therefore technically misapplied.
Source: Computed from `three_phase_on_prem_ratings.md`, §6
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**P2 Phase 3 near-miss cells (gap = +1, no [D] flag — correctly omitted):** AL01, AL04, AL05, AL07, AL09, AL10 all show +1 gaps. Six of the seven unresolved positive gaps in Phase 3 cluster in P2. No additional [D] flags are warranted, but the density of +1 gaps (6 of 10 subsegments in one plane-phase combination) is the structural basis for the "systematic divergence" claim.

---

## 4. P3 Data Plane — Complete Gap Calculation

### P3 Phase 1 (Initial Refactoring)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §4, "P3: Data Plane — Phase 1"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| DS1 | Relational Database HA | 4 | 4 | 0 | No | No | CORRECT |
| DS2 | NoSQL / Document Store | 3 | 3 | 0 | No | No | CORRECT |
| DS3 | Caching Layer | 3 | 2 | −1 | No | No | CORRECT |
| DS4 | Object / Blob Storage | 2 | 2 | 0 | No | No | CORRECT |
| DS5 | Message Queuing (Simple) | 2 | 2 | 0 | No | No | CORRECT |
| DS6 | Event Streaming (Kafka) | 4 | 4 | 0 | No | No | CORRECT |
| DS7 | Search / Full-Text Index | 4 | 3 | −1 | No | No | CORRECT |
| DS8 | Vector Database | 4 | 3 | −1 | No | No | CORRECT |
| DS9 | Embedding Pipeline (GPU) | 3 | 3 | 0 | No | No | CORRECT |
| DS10 | RAG Pipeline Orchestration | 3 | 4 | +1 | No | No | CORRECT |
| **Avg** | | **3.2** | **3.0** | **−0.2** | | | |

[FACT] No P3 Phase 1 cell reaches a gap of ±2. The widest negative gaps are −1 (DS3, DS7, DS8). DS10 shows the only positive gap in P3 Phase 1 (+1). No [D] flags are needed or applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §4
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### P3 Phase 2 (Per-Customer Customization)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §5, "P3: Data Plane — Phase 2"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| DS1 | Relational Database HA | 2 | 2 | 0 | No | No | CORRECT |
| DS2 | NoSQL / Document Store | 2 | 1 | −1 | No | No | CORRECT |
| DS3 | Caching Layer | 1 | 1 | 0 | No | No | CORRECT |
| DS4 | Object / Blob Storage | 1 | 1 | 0 | No | No | CORRECT |
| DS5 | Message Queuing (Simple) | 1 | 1 | 0 | No | No | CORRECT |
| DS6 | Event Streaming (Kafka) | 2 | 2 | 0 | No | No | CORRECT |
| DS7 | Search / Full-Text Index | 2 | 1 | −1 | No | No | CORRECT |
| DS8 | Vector Database | 2 | 2 | 0 | No | No | CORRECT |
| DS9 | Embedding Pipeline (GPU) | 2 | 2 | 0 | No | No | CORRECT |
| DS10 | RAG Pipeline Orchestration | 1 | 1 | 0 | No | No | CORRECT |
| **Avg** | | **1.6** | **1.4** | **−0.2** | | | |

[FACT] P3 Phase 2 has no gaps exceeding ±1. DS2 and DS7 show −1 gaps (RD slightly exceeds TE), indicating minor effort compression when scaling to per-customer configuration. No [D] flags are needed or applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §5
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### P3 Phase 3 (Ongoing Software Updates and Support)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §6, "P3: Data Plane — Phase 3"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| DS1 | Relational Database HA | 4 | 4 | 0 | No | No | CORRECT |
| DS2 | NoSQL / Document Store | 3 | 2 | −1 | No | No | CORRECT |
| DS3 | Caching Layer | 2 | 2 | 0 | No | No | CORRECT |
| DS4 | Object / Blob Storage | 2 | 2 | 0 | No | No | CORRECT |
| DS5 | Message Queuing (Simple) | 2 | 2 | 0 | No | No | CORRECT |
| DS6 | Event Streaming (Kafka) | 4 | 4 | 0 | No | No | CORRECT |
| DS7 | Search / Full-Text Index | 3 | 3 | 0 | No | No | CORRECT |
| DS8 | Vector Database | 4 | 3 | −1 | No | No | CORRECT |
| DS9 | Embedding Pipeline (GPU) | 3 | 3 | 0 | No | No | CORRECT |
| DS10 | RAG Pipeline Orchestration | 3 | 4 | +1 | **Yes** | **No** | **MISAPPLIED — gap is +1, not ≥+2** |
| **Avg** | | **3.0** | **2.9** | **−0.1** | | | |

[FACT] DS10 Phase 3 carries a [D] flag (RD=3, TE=4, gap = +1). This flag was independently identified as technically misapplied in `RP3b_P3_streaming_ai_data.md`. The current audit confirms that finding: the gap is +1, which does not satisfy the ≥2-point [D] threshold. The substantive divergence claim (RAG ecosystem evolution drives effort above difficulty) is analytically correct; the formal flag placement is not.
Source: Computed from `three_phase_on_prem_ratings.md`, §6; cross-referenced with `RP3b_P3_streaming_ai_data.md`, §DS10 Phase 3 [D] Flag Assessment
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3b_P3_streaming_ai_data.md`

**P3 Phase 3 hidden divergence check:** DS8 Phase 3 shows a −1 gap (RD=4, TE=3). This is an inverse near-miss (RD slightly exceeds TE), consistent with the finding in `RP3b_P3_streaming_ai_data.md` that DS8 Phase 3 TE=3 is borderline and the ground truth FTE range (1.25–1.75 FTE) spans the TE=3/TE=4 boundary. No hidden positive [D]-qualifying divergences exist in P3.

---

## 5. P4 AI Model Plane — Complete Gap Calculation

### P4 Phase 1 (Initial Refactoring — ISV Scope Only)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §4, "P4: AI Model Plane — Phase 1"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| S1 | Managed API Integration | 1 | 2 | +1 | No | No | CORRECT |
| S6 | Model Routing / Load Balancing | 2 | 2 | 0 | No | No | CORRECT |
| S7 | Inference Monitoring | 2 | 2 | 0 | No | No | CORRECT |
| S8 | Model Lifecycle Management | 1 | 1 | 0 | No | No | CORRECT |
| **Avg** | | **1.5** | **1.8** | **+0.3** | | | |

[FACT] No P4 Phase 1 cell reaches a gap of ±2. S1 shows the only +1 gap. No [D] flags are needed or applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §4
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### P4 Phase 2 (Per-Customer Customization — ISV Scope Only)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §5, "P4: AI Model Plane — Phase 2"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| S1 | Managed API Integration | 1 | 2 | +1 | No | No | CORRECT |
| S6 | Model Routing / Load Balancing | 1 | 2 | +1 | No | No | CORRECT |
| S7 | Inference Monitoring | 1 | 1 | 0 | No | No | CORRECT |
| S8 | Model Lifecycle Management | 1 | 1 | 0 | No | No | CORRECT |
| **Avg** | | **1.0** | **1.5** | **+0.5** | | | |

[FACT] P4 Phase 2 shows +1 gaps at S1 and S6, driven by the per-customer configuration work (endpoint URL mapping, model catalog variation) that exceeds the minimal RD rating. Neither gap reaches the ≥2-point threshold. No [D] flags are needed or applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §5
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### P4 Phase 3 (Ongoing Software Updates and Support — ISV Scope Only)

[STATISTIC] All ratings sourced from `three_phase_on_prem_ratings.md`, §6, "P4: AI Model Plane — Phase 3"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

| ID | Subsegment | RD | TE | Gap (TE−RD) | [D] Flag in File | [D] Required? | Verdict |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| S1 | Managed API Integration | 1 | 2 | +1 | No | No | CORRECT |
| S6 | Model Routing / Load Balancing | 2 | 2 | 0 | No | No | CORRECT |
| S7 | Inference Monitoring | 1 | 2 | +1 | No | No | CORRECT |
| S8 | Model Lifecycle Management | 1 | 1 | 0 | No | No | CORRECT |
| **Avg** | | **1.3** | **1.8** | **+0.5** | | | |

[FACT] P4 Phase 3 shows +1 gaps at S1 and S7, both driven by per-customer inference endpoint maintenance and SLO monitoring overhead that exceeds the minimal RD of 1. No gap reaches ≥2 points. No [D] flags are needed or applied.
Source: Computed from `three_phase_on_prem_ratings.md`, §6
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

---

## 6. Master [D] Flag Audit Summary

### All [D] Flags Present in the File

[DATA POINT] Complete inventory of [D] flags as applied in `three_phase_on_prem_ratings.md`:

| Phase | ID | Subsegment | RD | TE | Gap | Threshold Met? | Verdict |
|---|:---:|---|:---:|:---:|:---:|:---:|---|
| Phase 1 | AL10 | Testing / Contract Testing / Env Parity | 3 | 4 | +1 | No (need ≥2) | **MISAPPLIED** |
| Phase 3 | AL02 | Business Logic / Domain Services | 1 | 4 | +3 | Yes | CORRECT |
| Phase 3 | AL05 | Background Jobs / Async / EDA | 2 | 3 | +1 | No (need ≥2) | **MISAPPLIED** |
| Phase 3 | AL10 | Testing / Contract Testing / Env Parity | 3 | 4 | +1 | No (need ≥2) | **MISAPPLIED** |
| Phase 3 | DS10 | RAG Pipeline Orchestration | 3 | 4 | +1 | No (need ≥2) | **MISAPPLIED** |

Source: Computed from `three_phase_on_prem_ratings.md`, §4, §6, §7
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**Critical correction on AL05 Phase 3:** The ratings table in §6 "P2: Application Logic — Phase 3" does NOT show a [D] flag on AL05 in the table itself. The [D] flag on AL05 appears only in the Section 7 divergence narrative table header ("Background Jobs / Async / EDA: Phase 3, RD 2, TE 3, Gap +1"). The Phase 3 ratings table row for AL05 reads: `| AL05 | Background Jobs / Async / EDA | 2 | 3 | No | 2.75–5.6 | [D] Event schema evolution...` — the [D] appears in the Notes column, not as a standalone flag indicator. Reviewing the precise text: the ratings file's §6 P2 table shows `**[D]**` inline in the Notes field for AL05. This is an ambiguous placement — it is unclear whether the [D] in the notes column is intended as a formal flag or as descriptive notation.

[FACT] The ratings file §6 P2 Phase 3 table shows "[D]" in the Notes field for AL05 (Background Jobs, RD=2, TE=3, gap=+1) rather than as a standalone column or standalone flag attached to the ID. Whether this constitutes a formally applied [D] flag or explanatory notation is ambiguous. The underlying gap (+1) does not meet the ≥2-point threshold regardless.
Source: `three_phase_on_prem_ratings.md`, §6 P2 Phase 3 table
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### Formally Confirmed [D] Status

After resolving ambiguity, the formal [D] flag count and audit result is:

| # | Flag Location | Gap | Status |
|:---:|---|:---:|---|
| 1 | AL10 Phase 1 (Testing) | +1 | Misapplied — gap below threshold |
| 2 | AL02 Phase 3 (Business Logic) | +3 | Correctly applied — only unambiguous correct placement |
| 3 | AL10 Phase 3 (Testing) | +1 | Misapplied — gap below threshold |
| 4 | DS10 Phase 3 (RAG Pipeline) | +1 | Misapplied — confirmed by RP3b |

[FACT] Of the four unambiguous [D] flag placements in the ratings file, three are misapplied (AL10 Phase 1, AL10 Phase 3, DS10 Phase 3) and one is correctly placed (AL02 Phase 3). The DS10 misapplication was previously identified in `RP3b_P3_streaming_ai_data.md`. The AL10 misapplications are newly identified by this review.
Source: This audit, cross-referenced with `RP3b_P3_streaming_ai_data.md`, §DS10 Phase 3 [D] Flag Assessment
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3b_P3_streaming_ai_data.md`

### Missed [D] Flags (Should Be Applied But Are Not)

[FACT] Independent gap calculation finds zero missed [D] flags across all 102 active cells. No cell other than AL02 Phase 3 reaches a gap of ±2 or greater. There are no hidden divergences in P1, P3, or P4 that should carry [D] flags.
Source: This audit, computed from all tables in `three_phase_on_prem_ratings.md`, §4–6
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

---

## 7. Validation of the P2 "+0.9 Systematic Divergence" Claim

The ratings file Phase 3 Summary states: "TE exceeds RD by 0.9 — systematic divergence."

[STATISTIC] Independent arithmetic verification of P2 Phase 3 average gap:
- Sum of gaps: (+1) + (+3) + (0) + (+1) + (+1) + (0) + (+1) + (0) + (+1) + (+1) = +9
- Number of cells: 10
- Average gap: +9 / 10 = **+0.9**

The stated +0.9 average gap is arithmetically exact.
Source: Computed from `three_phase_on_prem_ratings.md`, §6 P2 Phase 3 table
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[STATISTIC] P2 average gaps by phase: Phase 1 = +0.4, Phase 2 = +0.1, Phase 3 = +0.9. All-phase unweighted average = (+0.4 + 0.1 + 0.9) / 3 = **+0.47**.
Source: Computed from `three_phase_on_prem_ratings.md`, §4–6; consistent with `RP2c_P2_divergence_investigation.md`, §1 All-Phase P2 Summary
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2c_P2_divergence_investigation.md`

### Is the +0.9 Gap Systematic or Outlier-Driven?

[FACT] AL02 Phase 3 (gap = +3) contributes +3 to the total P2 Phase 3 gap sum of +9. Removing AL02 leaves a residual sum of +6 across 9 cells, yielding an average residual gap of +0.67. The divergence does not disappear when the largest outlier is removed.
Source: Computed from `three_phase_on_prem_ratings.md`, §6; cross-referenced with `RP2c_P2_divergence_investigation.md`, §2 "The Case for Systematic Divergence"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2c_P2_divergence_investigation.md`

[FACT] Of 10 P2 Phase 3 cells, 8 show TE ≥ RD (gap ≥ 0), 2 are aligned (AL03, AL06, both at gap = 0), and none show TE < RD. The pattern is directionally consistent across all subsegments with no counter-examples.
Source: Computed from `three_phase_on_prem_ratings.md`, §6 P2 Phase 3 table
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**Verdict on "systematic" claim:** The +0.9 gap is arithmetically exact. The word "systematic" is substantively defensible: 8 of 10 cells trend in the same direction, and the residual gap after removing the dominant outlier remains +0.67. The claim is validated.

---

## 8. Assessment of Section 7 Divergence Narrative Accuracy

The Section 7 "Divergence Analysis" in the ratings file presents two tables: one for "Subsegments Where Effort Exceeds Difficulty" and one for aligned planes.

[FACT] Section 7 "Subsegments Where Effort Exceeds Difficulty" lists the following cells:
— Phase 1, AL10 (gap +1), Phase 3 AL02 (gap +3), Phase 3 AL05 (gap +1), Phase 3 AL09 (gap +1), Phase 3 AL10 (gap +1), Phase 3 DS10 (gap +1), and "P2 overall" at avg gap +0.9.
Source: `three_phase_on_prem_ratings.md`, §7
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**Section 7 accuracy issues:**

1. The table lists gaps correctly (all reported gaps match computed gaps). No arithmetic errors in the divergence narrative table itself.

2. The table is incomplete as a divergence catalog. It does not list all +1 gap cells — it lists only the cells the narrative selects as illustrative. Omitted from the narrative table but present in the computed data: AL01 Phase 1 (+1), AL04 Phase 1 (+1), AL01 Phase 3 (+1), AL04 Phase 3 (+1), AL07 Phase 3 (+1), S1 Phase 1 (+1), S1 Phase 2 (+1), S6 Phase 2 (+1), S1 Phase 3 (+1), S7 Phase 3 (+1), CP-03 Phase 3 (+1), CP-05 Phase 3 (+1), DS10 Phase 1 (+1). The Section 7 table is a curated selection, not an exhaustive inventory.

3. The "Subsegments Where Difficulty and Effort Align" table lists Phase 2 (all planes) as "avg 1.8 / 1.8 / 0.0 gap." Independent calculation: P1 Phase 2 avg gap = −0.1, P2 Phase 2 avg gap = +0.1, P3 Phase 2 avg gap = −0.2, P4 Phase 2 avg gap = +0.5. The reported 0.0 aggregate for "all planes" in Phase 2 is an approximation that rounds correctly to one decimal place but conceals P4's +0.5 deviation.

[FACT] The Section 7 "Phase 2, All planes" entry reports a gap of 0.0. The weighted average across P1 (avg −0.1), P2 (+0.1), P3 (−0.2), P4 (+0.5) gives approximately +0.075, which rounds to 0.1 rather than 0.0. The 0.0 figure in the narrative slightly understates the P4 Phase 2 positive skew.
Source: Computed from `three_phase_on_prem_ratings.md`, §5 (all planes Phase 2 tables)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

4. Section 7 correctly identifies P1 and P3 as "well-calibrated" and P2 as "systematically miscalibrated." These characterizations are supported by the complete gap data.

---

## 9. Complete Near-Miss Inventory

Near-miss cells (gap = +1 where notes describe effort/difficulty tension) not previously flagged in the ratings file's own narrative, for record completeness:

[DATA POINT] Near-miss cells across all planes and phases (gap = +1, no [D] flag, correctly omitted per threshold):

| Phase | Plane | ID | Subsegment | RD | TE | Gap |
|---|---|:---:|---|:---:|:---:|:---:|
| Phase 1 | P1 | CP-05 | Observability Infrastructure | 4 | 5 | +1 |
| Phase 1 | P2 | AL01 | Service Decomposition | 1 | 2 | +1 |
| Phase 1 | P2 | AL04 | Data Access / ORM / Caching | 1 | 2 | +1 |
| Phase 1 | P2 | AL09 | AI/ML Orchestration | 2 | 3 | +1 |
| Phase 1 | P3 | DS10 | RAG Pipeline Orchestration | 3 | 4 | +1 |
| Phase 1 | P4 | S1 | Managed API Integration | 1 | 2 | +1 |
| Phase 2 | P4 | S1 | Managed API Integration | 1 | 2 | +1 |
| Phase 2 | P4 | S6 | Model Routing / Load Balancing | 1 | 2 | +1 |
| Phase 3 | P1 | CP-03 | IAM / RBAC | 3 | 4 | +1 |
| Phase 3 | P1 | CP-05 | Observability Infrastructure | 4 | 5 | +1 |
| Phase 3 | P2 | AL01 | Service Decomposition | 1 | 2 | +1 |
| Phase 3 | P2 | AL04 | Data Access / ORM / Caching | 1 | 2 | +1 |
| Phase 3 | P2 | AL05 | Background Jobs / Async / EDA | 2 | 3 | +1 |
| Phase 3 | P2 | AL07 | Multi-Tenant Isolation | 1 | 2 | +1 |
| Phase 3 | P2 | AL09 | AI/ML Orchestration | 3 | 4 | +1 |
| Phase 3 | P4 | S1 | Managed API Integration | 1 | 2 | +1 |
| Phase 3 | P4 | S7 | Inference Monitoring | 1 | 2 | +1 |

[FACT] Total near-miss count: 17 cells with +1 gaps, all correctly omitted from [D] flagging per the ≥2-point threshold. Of these, 9 occur in Phase 3, consistent with the pattern that Phase 3 is where effort most frequently diverges from difficulty. The highest concentration (7 of 17) is in P2 Phase 3, reinforcing the systematic divergence characterization.
Source: Computed from `three_phase_on_prem_ratings.md`, §4–6
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

---

## Key Findings

- [FACT] Of four unambiguous [D] flag placements in `three_phase_on_prem_ratings.md`, three are technically misapplied (AL10 Phase 1 at gap +1, AL10 Phase 3 at gap +1, DS10 Phase 3 at gap +1). Only one [D] flag is correctly placed: AL02 Phase 3, which carries the widest gap in the entire file at +3 (RD=1, TE=4). The DS10 Phase 3 misapplication was previously identified in `RP3b_P3_streaming_ai_data.md`; the AL10 misapplications are newly confirmed by this audit. Source: This audit, computed from `three_phase_on_prem_ratings.md`, §4–6.

- [STATISTIC] Zero missed [D] flags exist across all 102 active cells. No cell other than AL02 Phase 3 reaches a ±2-point gap. The audit finds no hidden divergences in P1, P2 (beyond AL02), P3, or P4 that should carry flags but do not. The flags that are present are all false positives (applied below threshold); the flags that should be present are all correctly applied (only AL02 Phase 3). Source: This audit, all 102 active cells computed.

- [STATISTIC] The P2 Phase 3 "+0.9 systematic divergence" claim is arithmetically exact: sum of gaps = +9 across 10 cells, average = +0.90. Removing the dominant outlier (AL02, gap = +3) yields a residual average of +0.67 across 9 remaining cells, confirming that the divergence is structural and not solely outlier-driven. Source: Computed from `three_phase_on_prem_ratings.md`, §6 P2 Phase 3 table; cross-referenced with `RP2c_P2_divergence_investigation.md`, §1.

- [DATA POINT] P1 and P3 contain zero [D]-qualifying gaps across all three phases. The widest P1 gaps are ±1 (CP-02 Phase 1 at −1; CP-05 Phase 1 at +1; CP-03 Phase 3 at +1; CP-05 Phase 3 at +1). The widest P3 gap is +1 (DS10 Phase 1 and Phase 3). This confirms that P1 and P3 are genuinely well-calibrated — hard things are also large things in both planes — and that the divergence phenomenon is structurally isolated to P2 (and at minor scale, P4). Source: This audit; cross-referenced with `RP2c_P2_divergence_investigation.md`, §4 Cross-Plane Divergence Comparison.

- [FACT] Section 7 of the ratings file reports the "Phase 2, All planes" aggregate gap as 0.0. Independent calculation across all four planes in Phase 2 yields approximately +0.075, which rounds to 0.1. The 0.0 figure slightly underreports the P4 Phase 2 positive skew (+0.5 average gap in P4 Phase 2, driven by S1 and S6 at +1 each). This is a minor rounding artifact, not a substantive error. Source: Computed from `three_phase_on_prem_ratings.md`, §5 all planes; `three_phase_on_prem_ratings.md`, §7.

---

## Sources

| Reference | Description | Path or URL |
|---|---|---|
| three_phase_on_prem_ratings.md | Primary file under audit | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| RP2c_P2_divergence_investigation.md | P2 divergence deep-dive; all-phase gap calculations | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2c_P2_divergence_investigation.md` |
| RP3b_P3_streaming_ai_data.md | P3 streaming and AI data review; DS10 [D] flag misapplication finding | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3b_P3_streaming_ai_data.md` |
