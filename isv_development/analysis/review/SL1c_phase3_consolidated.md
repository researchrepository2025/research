# SL1c — Phase 3 (Ongoing Support) Consolidated Findings

**Synthesis Date:** 2026-02-19
**Scope:** Phase 3 (Ongoing Software Updates and Support) across all 38 MECE subsegments in 4 planes
**ISV/Customer Scope Split:** Customer owns hardware, GPUs, AI models. ISV owns ALL software.
**Primary File Under Review:** `analysis/three_phase_on_prem_ratings.md` (Phase 3 sections)

---

## Executive Summary

Phase 3 ratings across the 38-subsegment framework are substantially accurate: 30 of 38 subsegments require no rating changes for Phase 3 (79% accuracy rate). Eight subsegments carry recommended adjustments, all at +1 magnitude, concentrated in P1 Control Plane (4 TE increases) and P2 Application Logic (3 RD or TE increases), with one P3 Data Plane TE increase. The single highest-priority correction is the P3 Data Plane FTE aggregate: the stated "~10-18 FTE" is arithmetically incorrect and must be revised to 11.85-19.55 FTE, propagating the Phase 3 grand total from "~49-93 FTE" to approximately 51-95 FTE. Three of four [D] divergence flags applied in Phase 3 are technically misapplied (gap = +1, threshold requires >= 2); only AL02 Phase 3 (gap = +3) correctly qualifies. The P2 systematic divergence of +0.9 average gap (TE exceeding RD) in Phase 3 is arithmetically verified and structurally real, not outlier-driven. Six structural risk categories are absent from the framework entirely, with talent acquisition difficulty and customer communication overhead being the most material gaps for Phase 3 staffing estimates.

---

## 1. Consolidated Phase 3 Findings by Plane

### 1.1 P1 Control Plane (CP-01 through CP-10)

Phase 3 P1 averages: RD 4.0 / TE 4.1. Stated FTE: ~20-38 FTE (deduplicated from 24.85-44.50 raw sum).

P1 Phase 3 is the highest-rated plane across both dimensions and represents the core of on-premises resistance. The review confirmed that CP-01 (K8s Cluster Lifecycle, RD 5/TE 5) and CP-07 (Deploy Lifecycle/Rollback, RD 5/TE 5) are the twin anchors of Phase 3 difficulty, both correctly flagged as "Scales with N: Yes" with linear scaling fully validated by the GT1 ground truth.

**Accurate ratings (6 of 10):** CP-01 (5/5), CP-02 (4/4), CP-04 (4/4, borderline RD 4-5), CP-05 (4/5), CP-07 (5/5), CP-09 (4/4).

**Ratings requiring adjustment (4 of 10):** All four are TE understatements where ground truth FTE ranges exceed the TE rating's ceiling:

- **CP-03 (IAM/RBAC):** Current TE=4 (ceiling 2.5 FTE); GT1 FTE 2.75-4.75 exceeds ceiling. Recommend TE 4 -> 5.
- **CP-06 (CI/CD Pipeline/GitOps):** Current TE=3 (ceiling 1.0 FTE); GT1 FTE 2.0-3.25 maps to TE=4, not TE=3. Recommend TE 3 -> 4.
- **CP-08 (Disaster Recovery/BC):** Current TE=3 (ceiling 1.0 FTE); GT1 FTE 1.5-2.5 exceeds TE=3 ceiling. Recommend TE 3 -> 4.
- **CP-10 (Security Operations):** Current TE=4 (ceiling 2.5 FTE); GT1 FTE floor 2.75 exceeds ceiling. Recommend TE 4 -> 5.

CP-04 Phase 3 RD=4 is borderline 4-5 due to manual Shamir unsealing requirements in air-gapped environments but is not formally recommended for adjustment. CP-05 Phase 3 TE=5 (4.6-7.0 FTE) is the highest single-subsegment FTE in P1 and is confirmed accurate.

**Cross-phase trajectory finding (CC3):** CP-01 and CP-07 are the only subsegments where Phase 3 RD equals Phase 1 RD (both at 5). This is explicitly supported by linear-with-N scaling and is not an error. CP-09 Phase 3 TE (4) exceeds Phase 1 TE (3) — correct due to recurring per-customer compliance evidence regeneration.

### 1.2 P2 Application Logic (AL01 through AL10)

Phase 3 P2 averages: RD 1.8 / TE 2.7. Stated FTE: 18.6-35.6 FTE.

The defining characteristic of P2 Phase 3 is the systematic divergence: TE exceeds RD by an average of +0.9 across all 10 subsegments. This is the "planning trap" — P2 work in Phase 3 is large but routine, creating a cost center that is invisible to planners who screen only on relative difficulty. The divergence is arithmetically verified (sum of gaps = +9 across 10 cells) and structural: removing the dominant outlier (AL02, gap = +3) still leaves a residual average gap of +0.67.

**Accurate ratings (7 of 10):** AL01 (1/2), AL02 (1/4, [D] correctly applied), AL03 (2/2), AL06 (2/2), AL07 (1/2), AL08 (2/2), AL10 (3/4).

**Ratings requiring adjustment (3 of 10):**

- **AL04 (Data Access/ORM/Caching):** TE 2 -> 3. Patroni and Redis Sentinel application-layer event handling creates meaningful ongoing work beyond the RD=1 assessment. Source: RP2a.
- **AL05 (Background Jobs/Async/EDA):** RD 2 -> 3. Temporal configuration drift, dead-letter queue burden, and 2.0-4.1 FTE ops burden justify moderate (not low) difficulty. Source: RP2a.
- **AL09 (AI/ML Orchestration/Agent Pipelines):** RD 3 -> 4. Ranked #1 hardest subsegment across all four planes in source difficulty. Multi-stack coordination burden (LangGraph + MCP + guardrails + model version compatibility) exceeds the "moderate" RD=3 designation. This is also the only subsegment in the entire dataset where Phase 3 RD exceeds Phase 1 RD (P1 RD=2, P3 RD=3, proposed P3 RD=4). Source: RP2b, CC3.

**AL09 trajectory note (CC3):** The Phase 3 RD exceeding Phase 1 RD is structurally unusual but defensible. The AI/agent ecosystem evolves faster than any other application subsegment, and ongoing maintenance accumulates version-skew debt that the initial build does not face. However, the same ecosystem velocity argument should arguably also inflate Phase 1 RD, which remains at 2. An explanatory annotation is warranted in the source file.

### 1.3 P3 Data Plane (DS1 through DS10)

Phase 3 P3 averages: RD 3.0 / TE 2.9. **Stated FTE: "~10-18 FTE" — INCORRECT. Corrected: 11.85-19.55 FTE.**

The P3 FTE aggregate error is the highest-priority correction in the entire Phase 3 review. The stated "~10-18 FTE" understates the arithmetic sum of subsegment FTE ranges by 1.85 FTE at the low end and 1.55 FTE at the high end. This finding was established independently by RP3d and confirmed by CC1. All 10 individual subsegment FTE values match the GT3 ground truth exactly; only the aggregate summary is wrong.

**Accurate ratings (8 of 10):** DS1 (4/4), DS3 (2/2), DS4 (2/2), DS6 (4/4), DS7 (3/3), DS8 (4/3, borderline TE 3-4), DS9 (3/3), DS10 (3/4).

**Ratings requiring adjustment (2 of 10):**

- **DS2 (NoSQL/Document Store):** TE 2 -> 3. Documented MongoDB FTE range 0.6-1.1 falls entirely within the TE=3 band (0.3-1.0 FTE), with upper bound exceeding it. TE=2 (0.1-0.3 FTE) is a material understatement. Source: RP3a.
- **DS5 (Message Queuing):** TE 2 -> 2-3 (broker-conditional). NATS JetStream (0.3-0.6 FTE) maps to TE=2 boundary; RabbitMQ (0.75-1.25 FTE) maps to TE=3. The composite Research FTE (0.4-0.7) reflects a NATS-weighted blend. If RabbitMQ is primary, TE=3 is warranted. Source: RP3a.

**Borderline findings not formally adjusted:**

- DS8 (Vector Database) Phase 3 TE=3 is at the boundary with TE=4 given the GT3 FTE range of 1.25-1.75 FTE. Milvus rapid release cadence (Woodpecker WAL migration in 2.6) and HNSW recall degradation failure mode suggest operational burden may prove higher. Source: RP3b.
- DS4 (Object/Blob Storage): MinIO community edition entered maintenance mode December 2025. Phase 3 RD=2 may warrant future upward revision. Source: RP3a.

**Scaling classifications:**

- DS1, DS6 "Yes" scaling: confirmed by GT3.
- DS10 "No" scaling: confirmed.
- DS9 "Partial" scaling: weakly supported. Dominant cost drivers (model version changes, re-embedding events) are volume-driven, not customer-count-driven. Source: RP3d.
- DS2-DS5, DS7-DS8 "Partial": plausible but lack direct N-scaling source data.

### 1.4 P4 AI Model Plane (S1, S6, S7, S8 ISV-Scope)

Phase 3 P4 averages: RD 1.3 / TE 1.8. Stated FTE: ~0.5-1.5 FTE (arithmetic: 0.45-1.45).

P4 is correctly characterized as "nearly eliminated" under the customer-provides-GPU scope split. Phase 3 ISV FTE drops from 2.60-4.80 FTE (full on-premises) to 0.45-1.45 FTE — a reduction to approximately 17-30% of the original.

**Accurate ratings (4 of 4 for Phase 3):** S1 (1/2), S6 (2/2), S7 (1/2), S8 (1/1). No Phase 3 P4 ratings require adjustment.

**At-scale caveats (not formal adjustments):**

- S6 Phase 3 TE=2 (0.1-0.3 FTE): stated research FTE 0.2-0.5 extends into TE=3 territory. At N=50 customers with active model churn, 0.3-0.5 FTE is more likely. Source: RP4a.
- S7 Phase 3 TE=2 (0.1-0.3 FTE): stated research FTE 0.1-0.5 extends into TE=3 territory. Same N=50 caveat. Source: RP4a.

**Note:** S1 Phase 1 RD=1 was flagged as too low by RP4a (recommend RD 1 -> 2 for auth re-implementation and Bedrock schema delta), but this is a Phase 1 adjustment, not Phase 3.

---

## 2. Recommended Rating Changes

### 2.1 Recommended Phase 3 Rating Adjustments

| Subsegment | Current RD | Proposed RD | Current TE | Proposed TE | Source | Confidence | FTE Impact |
|:---:|:---:|:---:|:---:|:---:|---|:---:|---|
| CP-03 IAM/RBAC | 3 | 3 | 4 | **5** | RP1a, GT1 | High | 2.75-4.75 exceeds TE=4 ceiling |
| CP-06 CI/CD/GitOps | 3 | 3 | 3 | **4** | RP1b, GT1 | High | 2.0-3.25 maps to TE=4 |
| CP-08 Disaster Recovery | 4 | 4 | 3 | **4** | RP1c, GT1 | High | 1.5-2.5 exceeds TE=3 ceiling |
| CP-10 Security Ops | 4 | 4 | 4 | **5** | RP1c, GT1 | High | FTE floor 2.75 exceeds TE=4 ceiling |
| AL04 Data Access/ORM | 1 | 1 | 2 | **3** | RP2a | Medium | Patroni event handling overhead |
| AL05 Background Jobs | 2 | **3** | 3 | 3 | RP2a | Medium | Temporal config drift, DLQ burden |
| AL09 AI/ML Orchestration | 3 | **4** | 4 | 4 | RP2b, CC3 | High | Multi-stack coordination burden |
| DS2 NoSQL/Document | 3 | 3 | 2 | **3** | RP3a, GT3 | Medium | MongoDB 0.6-1.1 FTE maps to TE=3 |

**Conditional adjustment:**

| Subsegment | Condition | Current TE | Proposed TE | Source |
|:---:|---|:---:|:---:|---|
| DS5 Message Queuing | If RabbitMQ primary | 2 | **3** | RP3a, GT3 |

**Summary:** 8 firm adjustments (4 P1 TE, 2 P2 RD, 1 P2 TE, 1 P3 TE) + 1 conditional P3 TE. All adjustments are +1 magnitude. No rating decreases recommended.

### 2.2 Recommended [D] Flag Changes

The [D] flag threshold is defined as RD-TE gap >= 2 points. Of the four [D] flags applied in Phase 3 (or affecting Phase 3 narrative), three are misapplied:

| Location | Current [D] | RD | TE | Gap | Action | Rationale |
|---|:---:|:---:|:---:|:---:|---|---|
| AL02 Phase 3 | Applied | 1 | 4 | +3 | **RETAIN** | Only correct [D] in Phase 3; largest gap in entire file |
| AL10 Phase 1 | Applied | 3 | 4 | +1 | **REMOVE** | Gap below threshold (CC2) |
| AL10 Phase 3 | Applied | 3 | 4 | +1 | **REMOVE** | Gap below threshold (CC2) |
| DS10 Phase 3 | Applied | 3 | 4 | +1 | **REMOVE** | Gap below threshold (CC2, RP3b) |
| AL05 Phase 3 | Ambiguous (in Notes) | 2 | 3 | +1 | **CLARIFY/REMOVE** | Gap below threshold; [D] in notes column is ambiguous (CC2) |

**Note:** The analytical content behind these [D] flags is correct — effort does exceed difficulty in all flagged cells. The issue is formal threshold compliance. The underlying divergence narratives should be preserved as explanatory prose even if the [D] notation is removed.

---

## 3. Revised Phase 3 Summary Table

All 38 subsegments with current and proposed Phase 3 ratings. Changes marked in bold.

### P1: Control Plane

| ID | Subsegment | Current RD | Proposed RD | Current TE | Proposed TE | Scales with N? | Research FTE | Change? |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|:---:|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | 5 | 5 | Yes | 3.00-6.00 | -- |
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 4 | 4 | 4 | Partial | 1.75-3.50 | -- |
| CP-03 | IAM / RBAC | 3 | 3 | 4 | **5** | Partial | 2.75-4.75 | TE +1 |
| CP-04 | Secrets / Certs / PKI | 4 | 4 | 4 | 4 | Partial | 2.50-5.00 | -- |
| CP-05 | Observability Infrastructure | 4 | 4 | 5 | 5 | Yes | 4.60-7.00 | -- |
| CP-06 | CI/CD Pipeline / GitOps | 3 | 3 | 3 | **4** | Partial | 2.00-3.25 | TE +1 |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 5 | 5 | 5 | Yes | 1.50-3.00 | -- |
| CP-08 | Disaster Recovery / BC | 4 | 4 | 3 | **4** | Partial | 1.50-2.50 | TE +1 |
| CP-09 | Compliance Automation | 4 | 4 | 4 | 4 | Yes | 2.50-4.00 | -- |
| CP-10 | Security Operations | 4 | 4 | 4 | **5** | Yes | 2.75-5.50 | TE +1 |
| **Avg** | | **4.0** | **4.0** | **4.1** | **4.5** | | **~20-38** | |

### P2: Application Logic

| ID | Subsegment | Current RD | Proposed RD | Current TE | Proposed TE | Scales with N? | Research FTE | Change? |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|:---:|
| AL01 | Service Decomposition | 1 | 1 | 2 | 2 | No | 0.80-1.50 | -- |
| AL02 | Business Logic [D] | 1 | 1 | 4 | 4 | No | 3.00-6.00 | -- |
| AL03 | API Gateway / Edge Routing | 2 | 2 | 2 | 2 | Partial | 1.50-3.00 | -- |
| AL04 | Data Access / ORM / Caching | 1 | 1 | 2 | **3** | Partial | 0.75-1.50 | TE +1 |
| AL05 | Background Jobs / Async / EDA | 2 | **3** | 3 | 3 | Partial | 2.75-5.60 | RD +1 |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | 2 | 2 | No | 0.75-1.50 | -- |
| AL07 | Multi-Tenant Isolation | 1 | 1 | 2 | 2 | No | 0.75-1.50 | -- |
| AL08 | Observability Instrumentation | 2 | 2 | 2 | 2 | No | 0.50-1.00 | -- |
| AL09 | AI/ML Orchestration | 3 | **4** | 4 | 4 | Partial | 4.00-7.00 | RD +1 |
| AL10 | Testing / Contract Testing | 3 | 3 | 4 | 4 | Partial | 3.75-7.00 | -- |
| **Avg** | | **1.8** | **2.0** | **2.7** | **2.8** | | **18.6-35.6** | |

### P3: Data Plane

| ID | Subsegment | Current RD | Proposed RD | Current TE | Proposed TE | Scales with N? | Research FTE | Change? |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|:---:|
| DS1 | Relational Database HA | 4 | 4 | 4 | 4 | Yes | 1.50-3.00 | -- |
| DS2 | NoSQL / Document Store | 3 | 3 | 2 | **3** | Partial | 0.60-1.10 | TE +1 |
| DS3 | Caching Layer | 2 | 2 | 2 | 2 | Partial | 0.40-0.70 | -- |
| DS4 | Object / Blob Storage | 2 | 2 | 2 | 2 | Partial | 0.25-0.60 | -- |
| DS5 | Message Queuing | 2 | 2 | 2 | 2* | Partial | 0.40-0.70 | *Conditional |
| DS6 | Event Streaming (Kafka) | 4 | 4 | 4 | 4 | Yes | 1.50-2.50 | -- |
| DS7 | Search / Full-Text Index | 3 | 3 | 3 | 3 | Partial | 0.70-1.20 | -- |
| DS8 | Vector Database | 4 | 4 | 3 | 3 | Partial | 1.25-1.75 | -- |
| DS9 | Embedding Pipeline | 3 | 3 | 3 | 3 | Partial | 2.00-3.25 | -- |
| DS10 | RAG Pipeline Orchestration | 3 | 3 | 4 | 4 | No | 3.25-4.75 | -- |
| **Avg** | | **3.0** | **3.0** | **2.9** | **3.0** | | **11.85-19.55** | |

*DS5: TE=3 if RabbitMQ is primary broker; TE=2 if NATS JetStream.

### P4: AI Model Plane (ISV Scope)

| ID | Subsegment | Current RD | Proposed RD | Current TE | Proposed TE | Scales with N? | Research FTE | Change? |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|:---:|
| S1 | Managed API Integration | 1 | 1 | 2 | 2 | Partial | 0.10-0.30 | -- |
| S6 | Model Routing | 2 | 2 | 2 | 2 | Partial | 0.20-0.50 | -- |
| S7 | Inference Monitoring | 1 | 1 | 2 | 2 | Partial | 0.10-0.50 | -- |
| S8 | Model Lifecycle Mgmt | 1 | 1 | 1 | 1 | No | 0.05-0.15 | -- |
| **Avg** | | **1.3** | **1.3** | **1.8** | **1.8** | | **~0.5-1.5** | |

### Grand Summary (Proposed Phase 3)

| Plane | Current RD | Proposed RD | Current TE | Proposed TE | Current FTE | Corrected FTE |
|---|:---:|:---:|:---:|:---:|---|---|
| P1 Control Plane | 4.0 | 4.0 | 4.1 | 4.5 | ~20-38 | ~20-38 (no change) |
| P2 Application Logic | 1.8 | 2.0 | 2.7 | 2.8 | 18.6-35.6 | 18.6-35.6 (no change) |
| P3 Data Plane | 3.0 | 3.0 | 2.9 | 3.0 | **~10-18** | **11.85-19.55** |
| P4 AI Model Plane | 1.3 | 1.3 | 1.8 | 1.8 | ~0.5-1.5 | ~0.5-1.5 (no change) |
| **Total** | | | | | **~49-93** | **~51-95** |

---

## 4. Corrected FTE Aggregates

### 4.1 Material Correction: P3 Data Plane

| Metric | Stated Value | Corrected Value | Error Magnitude |
|---|---|---|---|
| P3 Phase 3 FTE low bound | ~10 FTE | 11.85 FTE | +1.85 FTE understated |
| P3 Phase 3 FTE high bound | ~18 FTE | 19.55 FTE | +1.55 FTE understated |
| Phase 3 Grand Total low bound | ~49 FTE | ~51 FTE | +2 FTE |
| Phase 3 Grand Total high bound | ~93 FTE | ~95 FTE | +2 FTE |

The corrected low bound of 11.85 FTE is computed as: DS1 1.50 + DS2 0.60 + DS3 0.40 + DS4 0.25 + DS5 0.40 + DS6 1.50 + DS7 0.70 + DS8 1.25 + DS9 2.00 + DS10 3.25 = 11.85. The corrected high bound of 19.55 FTE is computed as: DS1 3.00 + DS2 1.10 + DS3 0.70 + DS4 0.60 + DS5 0.70 + DS6 2.50 + DS7 1.20 + DS8 1.75 + DS9 3.25 + DS10 4.75 = 19.55. All individual subsegment FTE values match GT3 ground truth exactly; only the summary aggregate is incorrect.

### 4.2 Minor Rounding Corrections

| Metric | Stated | Computed | Magnitude | Type |
|---|---|---|---|---|
| P4 Phase 3 RD avg | 1.3 | 1.250 | 0.05 | Rounding convention |
| P4 Phase 3 TE avg | 1.8 | 1.750 | 0.05 | Rounding convention |
| Phase 3 Total TE | 3.0 | 3.059 | 0.06 | Rounding error |
| P2 Phase 3 FTE low | 18.6 | 18.55 | 0.05 | Rounding error |

These are non-material for planning purposes.

### 4.3 Impact of Rating Changes on Averages

If all 8 proposed TE/RD adjustments are accepted:

- P1 Phase 3 TE avg: 4.1 -> 4.5 (four TE +1 adjustments across 10 subsegments)
- P2 Phase 3 RD avg: 1.8 -> 2.0 (two RD +1 adjustments); TE avg: 2.7 -> 2.8 (one TE +1)
- P3 Phase 3 TE avg: 2.9 -> 3.0 (one TE +1)
- P4 Phase 3: unchanged

**Note:** FTE ranges are not affected by TE rating adjustments because the Research FTE column in the source file is derived from ground truth, not from the TE scale. The TE ratings are relative-scale labels applied to the FTE figures; adjusting the TE label to better match the FTE range does not change the FTE range itself.

---

## 5. Divergence and Cross-Phase Findings

### 5.1 P2 Phase 3 Systematic Divergence

The +0.9 average gap between TE and RD in P2 Phase 3 is the most significant structural finding across the entire review. Key properties:

- **Arithmetically exact:** Sum of gaps = +9 across 10 cells; average = +0.90. Source: CC2.
- **Not outlier-driven:** Removing AL02 (gap = +3) leaves residual average of +0.67 across 9 cells. Source: CC2, RP2c.
- **Unique to P2 Phase 3:** P1 Phase 3 avg gap = +0.1; P3 Phase 3 avg gap = -0.1; P4 Phase 3 avg gap = +0.5. Only P2 exhibits a systematic positive pattern.
- **8 of 10 cells trend positive:** No P2 Phase 3 subsegment has TE < RD. AL03 and AL06 are aligned (gap = 0); all others have TE >= RD.
- **Planning trap interpretation confirmed:** The source file's characterization of P2 Phase 3 as "easy to underestimate in cost planning" is validated. Application-layer work (business logic, background jobs, testing) is large but routine — planners who screen on difficulty alone will miss the effort dimension.

### 5.2 Cross-Phase Trajectory Findings Relevant to Phase 3

From CC3 (Cross-Phase Trajectory Consistency Review):

- **AL09 is the only subsegment where Phase 3 RD > Phase 1 RD** (P1 RD=2, P3 RD=3, proposed P3 RD=4). The ecosystem velocity argument (LangChain/LangGraph version upgrades, MCP protocol evolution, guardrail policy updates) is defensible but asymmetrically applied — the same velocity argument should inflate Phase 1 RD as well. An explanatory note is warranted.
- **AL02 exhibits the largest cross-phase TE jump** (P1 TE=1, P3 TE=4, delta = +3). This is not a trajectory error — it reflects that Phase 1 TE measures one-time person-weeks while Phase 3 TE measures annual FTE. AL02 requires zero business logic refactoring (TE=1) but is the ISV's largest ongoing product development investment (TE=4). The trajectory is presentation-inconsistent, not logically inconsistent.
- **No subsegment has Phase 3 TE strictly below Phase 2 TE.** The dataset passes this fundamental consistency check.
- **Phase 3 recovers to near-Phase-1 levels for infrastructure planes.** P1 Phase 3 avg TE (4.1) approaches P1 Phase 1 avg TE (4.0). P3 Phase 3 avg TE (2.9) approaches P3 Phase 1 avg TE (3.0). This is correct for N-scaling subsegments.

### 5.3 Structural Gaps Affecting Phase 3 (CC5)

Six risk categories are structurally absent from the 38-subsegment framework:

| Gap | Severity | Phase 3 Impact | Most Affected Subsegments |
|---|:---:|---|---|
| Organizational change management (ISV team restructuring) | High | FTE estimates assume team is in place; does not model recruitment/ramp-up time | All Phase 3 FTE tables |
| Customer communication overhead (upgrade coordination) | High | CP-07 captures engineering labor but not scheduling/coordination labor per customer | CP-07, CP-10 |
| Supply chain security (SBOM, CVE velocity, artifact mirror) | High | 40+ OSS components, 40K+ CVEs/year; CP-10 "CVE response time pressure" is underweighted | CP-10, CP-06 |
| Talent acquisition difficulty (on-premises specialists) | High | 5.4-month avg hiring cycle for platform engineers; $140K-$200K+ K8s engineer salaries | All P1 Phase 3 FTE |
| Vendor lock-in reversal cost | Medium-High | Primarily Phase 1, but Step Functions -> Temporal ongoing maintenance bleeds into Phase 3 | AL05 |
| Regulatory variance across customers | Medium-High | Code-level compliance divergence not captured in CP-09's configuration-level framing | CP-09 |

The talent acquisition gap is the most material for Phase 3 planning: the 20-38 FTE P1 Control Plane estimate assumes those FTEs can be recruited. The Spectro Cloud 2025 report found 40% of organizations lack K8s skills and headcount. The Linux Foundation 2024 report found 5.4+ month average hiring cycles for platform engineering roles.

---

## 6. Phase 3 Interview Questions by Role

### VP Engineering / CTO

1. How many FTEs are currently dedicated to on-premises customer support operations? How does this compare to the 51-95 FTE range projected here?
2. What is the ISV's average time-to-hire for platform engineers with K8s operations experience? Does it exceed 5 months?
3. Is the organization structured with separate cloud-native and on-premises support teams, or is there a shared team? What was the organizational change cost?
4. How many concurrent Kubernetes minor versions do you support across the customer base? Does the 3-5 concurrent version assumption in CP-07 match reality?

### Principal Engineer / Staff Engineer

5. When your team replaced Bedrock or Azure OpenAI calls with customer vLLM endpoints, how long did auth re-implementation, error handling, and schema validation take? (S1 Phase 1 RD validation)
6. Is the production message broker RabbitMQ Quorum Queues or NATS JetStream? (DS5 Phase 3 TE conditional)
7. What is the primary NoSQL technology — MongoDB replica sets or Cassandra? (DS2 Phase 3 TE validation)
8. How much engineering time do teams spend on Milvus or Qdrant version upgrades, particularly for the Woodpecker WAL migration? (DS8 Phase 3 TE boundary)
9. Does AL09 (AI/ML orchestration) Phase 3 difficulty genuinely exceed Phase 1 difficulty given the same ecosystem velocity applies to both?

### SRE / Platform Engineer

10. How many hours per week does the team spend coordinating deployment windows with customer IT teams, versus executing the actual deployment? (CC5 communication overhead gap)
11. How much time per week is spent tracking inference quality and TTFT compliance across customer endpoints — specifically excluding GPU-level monitoring the customer owns? (S7 Phase 3 FTE validation)
12. How many hours per week go to routing configuration updates and health check threshold tuning in response to customer inference endpoint changes? (S6 Phase 3 FTE validation)
13. What fraction of CP-10 Phase 3 effort is CVE triage and emergency patching across N customer environments, versus routine security operations? (CC5 supply chain security gap)

### Compliance / Security Lead

14. Have two customers' regulatory requirements ever been mutually incompatible in a single software configuration, requiring feature flags or deployment variants? (CC5 regulatory variance gap)
15. Do you currently produce and deliver SBOMs for all distributed open-source components? What is the FTE burden? (CC5 supply chain security gap)

---

## Key Findings

1. **Phase 3 accuracy rate is 79% (30 of 38 subsegments) with all adjustments at +1 magnitude.** No rating is overstated; all corrections are upward. The systematic direction of error — consistent understatement — suggests the source file applies a conservative bias to Phase 3 estimates. Four P1 Control Plane TE ratings are the most clearcut corrections, each driven by GT1 FTE ranges that arithmetically exceed the current TE rating's ceiling.

2. **The P3 Data Plane FTE aggregate "~10-18 FTE" must be corrected to 11.85-19.55 FTE.** This is the only material arithmetic error in Phase 3, propagating the grand total from ~49-93 to ~51-95 FTE. All 10 individual subsegment FTE values are correct; only the summary is wrong.

3. **P2 Phase 3 systematic divergence of +0.9 (TE exceeding RD) is the most significant structural pattern.** It is arithmetic, not interpretive: 8 of 10 P2 subsegments have TE >= RD, the residual gap excluding the AL02 outlier is still +0.67, and no other plane exhibits this pattern. P2 Phase 3 is a "planning trap" where large-but-routine work creates hidden cost for ISVs who screen only on difficulty.

4. **Three of four Phase 3 [D] flags are misapplied** (AL10, DS10, and ambiguously AL05 — all gap = +1 against a threshold of >= 2). Only AL02 Phase 3 (gap = +3) correctly qualifies. The underlying divergence narratives are analytically correct; the formal flag threshold is not met. Recommendation: either remove the flags and preserve the narratives as explanatory prose, or revise the [D] threshold to include +1 gaps for subsegments with documented effort/difficulty tension.

5. **Six structural gaps are absent from the framework, with talent acquisition and customer communication overhead being the most material.** The Phase 3 FTE estimates answer "what does this cost if staffed?" but not "can it be staffed?" Given 40% of organizations lack K8s skills (Spectro Cloud 2025) and 5.4+ month hiring cycles for platform engineers (Linux Foundation 2024), the 20-38 FTE P1 estimate carries execution risk not modeled in the ratings.

---

## Sources

### Review Agent Files

| File | Absolute Path | Key Phase 3 Contributions |
|---|---|---|
| RP1a_P1_infrastructure_core.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1a_P1_infrastructure_core.md` | CP-01 through CP-03 Phase 3 verdicts |
| RP1b_P1_security_delivery.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1b_P1_security_delivery.md` | CP-04 through CP-06 Phase 3 verdicts |
| RP1c_P1_operations_compliance.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1c_P1_operations_compliance.md` | CP-07 through CP-10 Phase 3 verdicts |
| RP2a_P2_service_architecture.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2a_P2_service_architecture.md` | AL01-AL05 Phase 3 verdicts |
| RP2b_P2_resilience_ai_testing.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2b_P2_resilience_ai_testing.md` | AL06-AL10 Phase 3 verdicts |
| RP2c_P2_divergence_investigation.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2c_P2_divergence_investigation.md` | P2 +0.9 systematic divergence analysis |
| RP3a_P3_traditional_data.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3a_P3_traditional_data.md` | DS1-DS5 Phase 3 verdicts |
| RP3b_P3_streaming_ai_data.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3b_P3_streaming_ai_data.md` | DS6-DS10 Phase 3 verdicts; DS10 [D] flag finding |
| RP3d_P3_fte_scaling.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3d_P3_fte_scaling.md` | P3 FTE aggregate error; scaling classification audit |
| RP4a_P4_isv_scope.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4a_P4_isv_scope.md` | S1, S6, S7, S8 Phase 3 verdicts; scope reduction validation |

### Cross-Cutting Review Files

| File | Absolute Path | Key Phase 3 Contributions |
|---|---|---|
| CC1_math_audit.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC1_math_audit.md` | Phase 3 arithmetic verification; P3 FTE error confirmed |
| CC2_divergence_rederivation.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC2_divergence_rederivation.md` | All 102 RD-TE gaps computed; [D] flag audit; +0.9 verified |
| CC3_cross_phase_consistency.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC3_cross_phase_consistency.md` | Cross-phase trajectory; AL09 P3>P1 finding; 5 most inconsistent trajectories |
| CC5_missing_risks.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC5_missing_risks.md` | 6 structural gaps; talent acquisition; communication overhead |

### Ground Truth Files

| File | Absolute Path |
|---|---|
| GT1_P1_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md` |
| GT3_P3_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md` |
| GT5_cross_reference_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` |

### Primary File Under Review

| File | Absolute Path |
|---|---|
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
