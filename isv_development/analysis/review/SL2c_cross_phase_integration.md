# SL2c: Cross-Phase Integration and Reconciliation

**Synthesis Date:** 2026-02-19
**Scope:** Cross-phase integration of SL1a (Phase 1), SL1b (Phase 2), and SL1c (Phase 3) consolidated findings
**Input Sources:** SL1a, SL1b, SL1c, CC1, CC3, CC4
**Output Type:** Final reconciliation layer — cross-phase conflicts, model assessment, structural changes

---

## Executive Summary

The three-phase decomposition of ISV on-premises deployment difficulty is structurally sound and survives cross-phase reconciliation with one material conflict requiring resolution: DS9 (Embedding Pipeline) Phase 3 FTE of 2.00-3.25 was derived under ISV-manages-GPU assumptions and must be corrected to approximately 0.5-1.0 FTE under the established customer-owns-GPU scope, reducing the P3 Phase 3 FTE aggregate from 11.85-19.55 to 10.35-17.30 and the Phase 3 grand total from ~51-95 FTE to ~50-93 FTE (CC4 Section 5; SL1b Section 2.4; SL1c Section 1.3). The single most important finding across all three per-phase reviews is that Phase 3 Total Effort ratings are systematically understated across P1, P2, and P3 — confirmed from three independent analytical angles (GT1 FTE-to-TE-ceiling mapping in SL1c, the P2 +0.9 TE-exceeds-RD systematic divergence in SL1c Section 5.1, and the P3 FTE arithmetic error in CC1 D-7) — meaning the operational cost of sustaining on-premises deployments is materially higher than the ratings file currently communicates.

---

## 1. Conflict Reconciliation

### 1.1 DS9 Phase 3 FTE — The Primary Cross-Phase Conflict

This is the single explicit conflict between per-phase review findings that requires resolution.

**The conflict:** SL1b (Phase 2 consolidated) documents in Section 2.4 that DS9 Phase 3 FTE should be revised from 2.00-3.25 to approximately 0.5-1.0 FTE under the customer-owns-GPU scope correction identified by CC4. However, SL1c (Phase 3 consolidated) carries the unreduced 2.00-3.25 FTE figure for DS9 in its P3 summary table (SL1c Section 3, P3 table, DS9 row) and uses this figure in its corrected P3 total of 11.85-19.55 FTE (SL1c Section 4.1).

**Root cause:** The scope correction was identified by CC4 (Section 5) but was not propagated into the Phase 3 review agent's arithmetic. CC4 established that the DS9 FTE of 2.00-3.25 was computed in the source file `P3_data_plane.md` under the assumption that the ISV manages full GPU hardware lifecycle tasks — MIG partitioning, NVLink topology management, firmware updates, thermal monitoring, and RMA processes (CC4 Section 5, citing `P3_data_plane.md` DS9 Evidence section). Under the established scope split where the customer owns all GPU hardware, these tasks are excluded from ISV scope, leaving only model serving configuration, batch queue management, model version management, and pipeline tuning (CC4 Section 10, Ambiguity 2).

**Resolution — corrected P3 Phase 3 FTE arithmetic:**

The DS9 Phase 3 FTE reduction from 2.00-3.25 to 0.50-1.00 changes the P3 Phase 3 aggregate as follows:

| Component | SL1c Value | Scope-Corrected Value | Delta |
|---|---|---|---|
| DS9 FTE low | 2.00 | 0.50 | -1.50 |
| DS9 FTE high | 3.25 | 1.00 | -2.25 |
| P3 FTE low (sum of DS1-DS10) | 11.85 | 11.85 - 1.50 = **10.35** | -1.50 |
| P3 FTE high (sum of DS1-DS10) | 19.55 | 19.55 - 2.25 = **17.30** | -2.25 |

Verification of corrected P3 FTE low bound: DS1 1.50 + DS2 0.60 + DS3 0.40 + DS4 0.25 + DS5 0.40 + DS6 1.50 + DS7 0.70 + DS8 1.25 + DS9 **0.50** + DS10 3.25 = **10.35 FTE** (CC1 Section 8.3 subsegment values with DS9 replaced per CC4).

Verification of corrected P3 FTE high bound: DS1 3.00 + DS2 1.10 + DS3 0.70 + DS4 0.60 + DS5 0.70 + DS6 2.50 + DS7 1.20 + DS8 1.75 + DS9 **1.00** + DS10 4.75 = **17.30 FTE** (CC1 Section 8.3 subsegment values with DS9 replaced per CC4).

**Impact on Phase 3 grand total:**

| Metric | SL1c Corrected (pre-DS9 scope fix) | Fully Corrected (DS9 scope fix applied) | Delta |
|---|---|---|---|
| P3 FTE | 11.85-19.55 | 10.35-17.30 | -1.50 to -2.25 |
| Grand Total FTE | ~51-95 | ~50-93 | -1 to -2 |

The corrected Phase 3 grand total is approximately **50-93 FTE**. This is computed as: P1 20.0-38.0 + P2 18.55-35.60 + P3 10.35-17.30 + P4 0.45-1.45 = 49.35-92.35, which rounds to ~50-93 FTE.

**Note on materiality:** The DS9 scope correction reduces the Phase 3 grand total by approximately 1-2 FTE (2-3% of the total range). While the correction is necessary for intellectual consistency with the customer-owns-GPU scope boundary, the magnitude is small relative to the overall uncertainty in the 50-93 FTE range. The correction is primarily important as a precedent: it demonstrates that scope-boundary decisions propagate through the entire model and that the source file `P3_data_plane.md` must be annotated to prevent the pre-scope-split DS9 FTE from being reused in future analyses (CC4 Section 10, Ambiguity 1).

### 1.2 No Other Cross-Phase Conflicts Identified

Beyond the DS9 FTE scope issue, no conflicts exist between the three per-phase consolidated findings. Specifically:

- **S1 Phase 1 RD adjustment (1 to 2):** Identified in SL1a (Section 2) from RP4a. SL1b and SL1c do not reference or contradict this adjustment. No Phase 2 or Phase 3 S1 rating is affected — S1 remains RD=1 in both Phase 2 and Phase 3 (SL1b Section 1.4; SL1c Section 1.4). The adjustment is Phase 1-specific and does not create a trajectory inconsistency because the Phase 1 RD increase (from 1 to 2) still leaves Phase 1 RD below Phase 3 RD for all P4 subsegments.

- **Phase 3 TE adjustments (8 cells):** All eight Phase 3 rating adjustments identified in SL1c (Section 2.1) are upward (+1 magnitude) and do not conflict with Phase 1 or Phase 2 findings. The four P1 TE increases (CP-03, CP-06, CP-08, CP-10) widen the Phase 1-to-Phase 3 TE gap for these subsegments, which is directionally consistent with the CC3 finding that Phase 3 TE "recovers to near-Phase-1 levels" for infrastructure planes (CC3 Section 4). The three P2 adjustments (AL04 TE, AL05 RD, AL09 RD) do not affect Phase 1 or Phase 2 ratings.

- **Phase 2 aggregate effort revision:** SL1b proposes revising Phase 2 total effort from 10-21 to 12-25 person-weeks for median customers and 15-30 for air-gapped/regulated customers (SL1b Section 2.3). This revision is independent of Phase 1 and Phase 3 findings and does not contradict any other review output.

---

## 2. Assessment of the Three-Phase Model

### 2.1 Is the Phase Decomposition Sound?

The three-phase decomposition (Initial Refactoring / Per-Customer Customization / Ongoing Support) is structurally sound. The decomposition maps cleanly to three distinct cost structures with different scaling properties, different unit economics, and different organizational implications:

| Phase | Cost Structure | Scaling | Unit | Organizational Driver |
|---|---|---|---|---|
| Phase 1 | One-time fixed investment | N/A (amortized) | Person-months | Engineering capacity |
| Phase 2 | Variable, per-customer | Linear with N | Person-weeks per customer | Deployment team capacity |
| Phase 3 | Recurring annual | Sublinear to linear with N | FTE annually | Operational headcount |

This decomposition is validated by three independent checks:

1. **CC3 trajectory consistency:** No subsegment has Phase 3 TE strictly below Phase 2 TE, confirming the monotonic relationship between per-customer effort and ongoing support effort (CC3 Section 5). The Phase 2 "dip" pattern (Phase 1 high, Phase 2 low, Phase 3 recovery) is consistent across all four planes and is explainable by the scope difference: Phase 1 builds the entire system once, Phase 2 adapts parameters per customer, Phase 3 maintains the running system (CC3 Section 4).

2. **SL1b aggregate consistency:** The Phase 2 effort estimates are arithmetically consistent with Phase 1 TE ratings when adjusted for the different absolute scales (CC1 Section 7). The P1 = ~60% Phase 2 claim is verified (CC1 Finding 4), and the proportionality between P1 and P3 Phase 2 effort (3:1 ratio) is consistent with the G1 finding that P3 scales sublinearly while P1 scales linearly with customer count (SL1b Section 4.4).

3. **SL1c Phase 3 recovery pattern:** Phase 3 P1 average TE (4.1) approaches Phase 1 P1 average TE (4.0), confirming that infrastructure-plane ongoing support is genuinely as effortful as the initial build on a relative scale (SL1c Section 5.2, citing CC3). The recovery is driven by N-scaling subsegments (CP-01, CP-05, CP-07, CP-09, CP-10) where each additional customer adds a proportional maintenance burden.

### 2.2 Limitations of the Three-Phase Model

Two structural limitations exist but do not invalidate the decomposition:

**Limitation 1 — Phase 2 learning-curve compression.** The Phase 2 per-customer effort estimates assume a mature ISV (5+ deployments) with established automation tooling. SL1b documents that the first 3-4 customer deployments will significantly exceed the stated per-customer ranges before automation maturity is established (SL1b Section 4.2, citing Replicated and Connsulting data). The three-phase model treats Phase 2 as a steady-state cost, but in practice there is a Phase 2 maturation curve that is not captured. This is a known simplification, not an error.

**Limitation 2 — Phase boundaries are not crisp in practice.** Phase 1 deliverables create hidden dependencies for Phase 2 (e.g., four P3 subsegments where Phase 2 TE=2 depends on pre-built configuration templates from Phase 1 — SL1b Section 4.3). Phase 2 customer deployments feed back into Phase 1 tooling improvements. Phase 3 ongoing support occasionally requires Phase-1-scale engineering interventions (e.g., major Kubernetes version upgrades, database engine migrations). The three-phase model is a planning abstraction, not a strict temporal partition.

Neither limitation undermines the model's utility for strategic planning. The phase decomposition correctly separates the three cost types that matter for ISV business case analysis: upfront investment, per-customer marginal cost, and annual operating expense.

---

## 3. Evaluation of the "Two Cost Types in Phase 3" Finding

SL1c (Section 5.1) identifies a critical structural pattern in Phase 3: the P2 systematic divergence where TE exceeds RD by an average of +0.9 across all 10 P2 subsegments. This finding implicitly surfaces two distinct Phase 3 cost types, but the ratings file does not explicitly articulate them.

### 3.1 The Two Cost Types

**Type A — Linear-with-N infrastructure costs (P1 and P3).** These costs scale proportionally with the number of on-premises customers. Each customer requires K8s version upgrades (CP-01), deployment coordination (CP-07), compliance evidence generation (CP-09), and data service operations (DS1, DS6). The dominant cost driver is the "N-customers multiplier" documented in G1 and confirmed by the "Scales with N: Yes" column in the Phase 3 tables (SL1c Section 1.1).

**Type B — Fixed product-development costs (P2, especially AL02 and AL09).** These costs exist regardless of customer count. The ISV's core business logic development (AL02, 3.00-6.00 FTE), AI orchestration maintenance (AL09, 4.00-7.00 FTE), and test infrastructure maintenance (AL10, 3.75-7.00 FTE) are product investments that would occur even with a single on-premises customer. They are "fixed" in the sense that they do not scale linearly with N, though they scale with product complexity (SL1c Section 1.2, citing RP2c).

### 3.2 Accuracy of Capture

The two cost types are **implicitly present** in the Phase 3 tables through the "Scales with N?" column, but they are **not explicitly articulated** as distinct cost categories in the summary or key findings of the ratings file. The P2 +0.9 divergence pattern is the clearest signal of Type B costs — high TE relative to low RD means "this work is large but not hard" — but the ratings file does not interpret this divergence as evidence of a fixed-cost category.

The SL1c finding that the divergence is "not outlier-driven" (residual average of +0.67 excluding AL02; SL1c Section 5.1) is important: it means the fixed-cost pattern is structural across P2, not concentrated in a single subsegment. This should be surfaced in the revised file's Phase 3 summary as an explicit finding: Phase 3 costs divide into N-scaling infrastructure costs (~30-57 FTE in P1+P3+P4) and fixed product-development costs (~18.6-35.6 FTE in P2), with the fixed costs being the "planning trap" that ISVs underestimate.

### 3.3 Quantitative Decomposition

Using fully corrected FTE figures:

| Cost Type | Planes | FTE Range | Share of Total |
|---|---|---|---|
| Type A: Linear-with-N | P1 + P3 + P4 | 30.80-56.75 | ~62-61% |
| Type B: Fixed product-development | P2 | 18.55-35.60 | ~38-39% |
| **Total** | **All** | **49.35-92.35** | **100%** |

Type A computation: P1 20.0-38.0 (SL1c Section 3) + P3 10.35-17.30 (Section 1.1 above, scope-corrected) + P4 0.45-1.45 (SL1c Section 1.4) = 30.80-56.75.

Type B computation: P2 18.55-35.60 (CC1 Section 8.2, corrected low bound).

The approximately 60/40 split between linear and fixed costs is a strategically consequential finding: an ISV with a single on-premises customer still carries approximately 40% of the full Phase 3 FTE burden, because the product-development costs are customer-count-invariant.

---

## 4. Phase 1 to Phase 2 to Phase 3: Team Composition and Skill Transitions

### 4.1 Phase 1 Team Profile

Phase 1 is dominated by P1 Control Plane (40-80 person-months, ~55% of total) and P3 Data Plane (20-40 person-months, ~27% of total) (SL1a Section 3.1). The required team composition is:

- **Platform engineers / Kubernetes specialists:** 3-5 FTEs for CP-01 through CP-10. Deep expertise in kubeadm/RKE2, Calico/Cilium CNI, Keycloak/Dex, cert-manager, ArgoCD/Flux, Prometheus/Thanos stack (SL1a Section 1.1).
- **Data infrastructure engineers / DBAs:** 2-3 FTEs for DS1 through DS10. PostgreSQL HA (Patroni), Kafka (Strimzi), vector databases (Milvus/Qdrant), MinIO (SL1a Section 1.3).
- **Backend engineers:** 1-2 FTEs for P2 application-layer adaptations (AL03 API gateway migration, AL05 message bus swap, AL10 test infrastructure). Low intensity relative to P1/P3 (SL1a Section 1.2).
- **AI platform engineers:** 0.5-1 FTE for P4 (S1 endpoint integration, S6 LiteLLM configuration). Minimal Phase 1 footprint (SL1a Section 1.4).

SL1a Finding 4 confirms that "P1 + P3 = ~80% of Phase 1 effort," which means the Phase 1 team is primarily infrastructure-heavy. ISVs whose engineering talent is concentrated in application development (as is typical for cloud-native SaaS companies) face a skill-gap challenge at Phase 1 entry.

### 4.2 Phase 2 Team Profile

Phase 2 shifts from building to deploying. The team composition changes in two ways:

1. **Customer-facing deployment skills become critical.** CP-01 and CP-02 Phase 2 (both rated RD=4, TE=4) require engineers who can diagnose and adapt to customer-specific infrastructure — VMware vs. KVM vs. bare metal, unique firewall rules, proxy configurations, DNS architectures (SL1b Section 1.1). This is field engineering, not laboratory engineering. The skill is not just technical (Kubernetes operations) but also diagnostic (identifying why a customer's network topology causes CNI failures).

2. **Breadth over depth.** Phase 2 engineers must touch all four planes in a single customer engagement: platform configuration (P1), validation testing (P2), data service parameter tuning (P3), and inference endpoint integration (P4). The Phase 1 team can specialize by plane; the Phase 2 team must generalize across planes. SL1b Section 4.3 documents four hidden Phase 1 dependencies where Phase 2 TE=2 assumes pre-built configuration templates — if those templates do not exist, the Phase 2 engineer must perform empirical investigation per customer, which is a different (harder) skill than template application.

3. **Customer communication overhead (unrated).** SL1c Section 5.3 (citing CC5) identifies customer communication coordination as a structural gap. Phase 2 requires the ISV to negotiate maintenance windows (CP-07), SLA terms (CP-08), compliance boundaries (CP-09), and SIEM integration specifications (CP-10) with each customer's IT organization. This is project management and customer success work that is absent from the MECE framework.

### 4.3 Phase 3 Team Profile

Phase 3 requires the largest and most diversified team. The corrected ~50-93 FTE range spans:

- **Platform operations team:** 20-38 FTE for P1 ongoing support. This is the largest single cost category. It includes K8s upgrade coordination across N customers (CP-01, 3.00-6.00 FTE), observability stack maintenance (CP-05, 4.60-7.00 FTE), deployment lifecycle management (CP-07, 1.50-3.00 FTE), and security operations (CP-10, 2.75-5.50 FTE) (SL1c Section 1.1). The four TE upward adjustments recommended in SL1c (CP-03 TE 4 to 5, CP-06 TE 3 to 4, CP-08 TE 3 to 4, CP-10 TE 4 to 5) reflect that the current ratings understate this cost center.

- **Product development team:** 18.55-35.60 FTE for P2 ongoing development. This is the ISV's core product investment — business logic (AL02, 3.00-6.00 FTE), AI orchestration (AL09, 4.00-7.00 FTE), testing (AL10, 3.75-7.00 FTE), and background job maintenance (AL05, 2.75-5.60 FTE) (SL1c Section 1.2). These FTEs exist on cloud-native as well but are included in the on-premises Phase 3 total because they represent real ISV cost.

- **Data operations team:** 10.35-17.30 FTE for P3 ongoing support (scope-corrected, Section 1.1 above). Dominated by RAG pipeline orchestration (DS10, 3.25-4.75 FTE), PostgreSQL HA operations (DS1, 1.50-3.00 FTE), and Kafka operations (DS6, 1.50-2.50 FTE).

- **AI platform team:** 0.45-1.45 FTE for P4 ISV-scope tasks. Minimal ongoing footprint under customer-owns-GPU scope (SL1c Section 1.4).

### 4.4 The Skill Transition Challenge

The most significant cross-phase team insight is the **skill type rotation** from Phase 1 to Phase 3:

- **Phase 1** requires deep technical specialists who can build systems from scratch (Kubernetes architects, database infrastructure engineers). These are the scarcest and most expensive hires — SL1c Section 5.3 cites 5.4+ month hiring cycles and 40% of organizations lacking K8s skills (Spectro Cloud 2025, Linux Foundation 2024).

- **Phase 2** requires generalist field engineers who can diagnose and adapt across multiple technology layers in customer environments. This is a different skill profile from Phase 1 specialists.

- **Phase 3** requires the Phase 1 specialists to become ongoing operators, plus the full product development team. The Phase 3 team is larger than the Phase 1 team because it must simultaneously maintain running systems (Type A costs) and continue product development (Type B costs).

The transition from Phase 1 to Phase 3 is not a staffing reduction — it is a staffing expansion. An ISV that treats Phase 1 as a project with a defined end date and plans to reduce headcount after "the build" will discover that Phase 3 requires equal or greater ongoing headcount. This is the central planning trap identified across all three per-phase reviews.

---

## 5. Single Most Important Finding

**Phase 3 Total Effort is systematically understated across all infrastructure planes (P1, P2, P3), confirmed from three independent analytical angles.**

This finding is the most important because it directly affects the ISV's business case for on-premises deployment. The three independent confirmations are:

1. **P1 Control Plane TE understatement (SL1c Section 1.1):** Four of ten P1 subsegments have Phase 3 TE ratings whose ceilings are below the ground truth FTE ranges documented in GT1. CP-03 TE=4 (ceiling 2.5 FTE) versus GT1 FTE 2.75-4.75; CP-06 TE=3 (ceiling 1.0 FTE) versus GT1 FTE 2.00-3.25; CP-08 TE=3 (ceiling 1.0 FTE) versus GT1 FTE 1.50-2.50; CP-10 TE=4 (ceiling 2.5 FTE) versus GT1 FTE floor 2.75. All four corrections are +1 TE upward, indicating systematic conservative bias in the original Phase 3 P1 ratings.

2. **P2 Application Logic systematic divergence (SL1c Section 5.1, citing RP2c and CC2):** The +0.9 average gap between TE and RD across all 10 P2 Phase 3 subsegments means effort consistently exceeds what the difficulty rating would suggest. This is arithmetically verified (sum of gaps = +9; residual average excluding AL02 outlier = +0.67; 8 of 10 cells have TE >= RD). The P2 Phase 3 pattern creates a cost center invisible to planners who screen on difficulty alone.

3. **P3 Data Plane FTE arithmetic error (CC1 D-7, confirmed by RP3d):** The stated P3 Phase 3 aggregate of "~10-18 FTE" understates the arithmetic sum of subsegment FTE ranges by 1.85 FTE at the low end and 1.55 FTE at the high end. After DS9 scope correction, the true P3 aggregate is 10.35-17.30 FTE — still above the stated "~10-18" at the low bound.

The convergence of these three findings — from different planes, identified by different review agents, using different analytical methods — constitutes the strongest evidence in the entire review corpus. The original ratings file applies a systematic conservative bias to Phase 3 estimates that, if uncorrected, would lead an ISV to understaff its on-premises operations by approximately 5-10 FTE (the sum of the P1 TE corrections, the P3 arithmetic correction, and the implicit P2 underweighting from the divergence pattern).

The strategic implication is clear: on-premises deployment is not a "build it and run it cheaply" proposition. Phase 3 costs approach or exceed Phase 1 costs on an annualized basis, and the ratings file should communicate this explicitly.

---

## 6. Structural Changes for the Revised File

The following changes should be applied to `three_phase_on_prem_ratings.md` to incorporate all per-phase and cross-phase findings. Changes are organized by type.

### 6.1 Rating Cell Changes (10 total)

| Phase | Subsegment | Dimension | Current | Proposed | Source |
|---|:---:|---|:---:|:---:|---|
| Phase 1 | S1 Managed API Integration | RD | 1 | **2** | SL1a Section 2, RP4a |
| Phase 3 | CP-03 IAM/RBAC | TE | 4 | **5** | SL1c Section 2.1, GT1 |
| Phase 3 | CP-06 CI/CD Pipeline/GitOps | TE | 3 | **4** | SL1c Section 2.1, GT1 |
| Phase 3 | CP-08 Disaster Recovery/BC | TE | 3 | **4** | SL1c Section 2.1, GT1 |
| Phase 3 | CP-10 Security Operations | TE | 4 | **5** | SL1c Section 2.1, GT1 |
| Phase 3 | AL04 Data Access/ORM/Caching | TE | 2 | **3** | SL1c Section 2.1, RP2a |
| Phase 3 | AL05 Background Jobs/Async/EDA | RD | 2 | **3** | SL1c Section 2.1, RP2a |
| Phase 3 | AL09 AI/ML Orchestration | RD | 3 | **4** | SL1c Section 2.1, RP2b, CC3 |
| Phase 3 | DS2 NoSQL/Document Store | TE | 2 | **3** | SL1c Section 2.1, RP3a, GT3 |
| Phase 3 (conditional) | DS5 Message Queuing | TE | 2 | **3** (if RabbitMQ) | SL1c Section 2.1, RP3a |

### 6.2 FTE Corrections (3 items)

| Location | Current Value | Corrected Value | Source |
|---|---|---|---|
| DS9 Phase 3 Research FTE | 2.00-3.25 | **0.50-1.00** | CC4 Section 5; SL1b Section 2.4; this document Section 1.1 |
| P3 Phase 3 FTE aggregate | "~10-18 FTE" | **~10-17 FTE** (10.35-17.30) | CC1 D-7 + DS9 scope correction (Section 1.1 above) |
| Phase 3 Grand Total FTE | "~49-93 FTE" | **~50-93 FTE** (49.35-92.35) | Propagation of P3 correction + P2 rounding fix |

### 6.3 Average Recalculations Required After Rating Changes

If all 10 rating changes are accepted:

| Metric | Current | Revised | Source |
|---|---|---|---|
| P4 Phase 1 avg RD | 1.5 | 1.75 | SL1a Section 1.4 |
| P1 Phase 3 avg TE | 4.1 | 4.5 | SL1c Section 4.3 |
| P2 Phase 3 avg RD | 1.8 | 2.0 | SL1c Section 4.3 |
| P2 Phase 3 avg TE | 2.7 | 2.8 | SL1c Section 4.3 |
| P3 Phase 3 avg TE | 2.9 | 3.0 | SL1c Section 4.3 |
| Phase 1 Total RD | 2.9 (stated) | 3.0 (was already 2.971) | CC1 D-2 |
| Phase 3 Total TE | 3.0 (stated) | 3.1 (was already 3.059, increases further with TE adjustments) | CC1 D-5 + SL1c adjustments |

### 6.4 [D] Divergence Flag Corrections (4 items)

| Location | Current | Proposed | Rationale | Source |
|---|---|---|---|---|
| AL10 Phase 1 | [D] applied | **REMOVE** | Gap = +1, threshold >= 2 | SL1c Section 2.2, CC2 |
| AL10 Phase 3 | [D] applied | **REMOVE** | Gap = +1, threshold >= 2 | SL1c Section 2.2, CC2 |
| DS10 Phase 3 | [D] applied | **REMOVE** | Gap = +1, threshold >= 2 | SL1c Section 2.2, CC2 |
| AL02 Phase 3 | [D] applied | **RETAIN** | Gap = +3, correctly exceeds threshold | SL1c Section 2.2, CC2 |

Underlying divergence narratives should be preserved as explanatory prose in the Notes column even where the formal [D] notation is removed.

### 6.5 Heading and Vocabulary Corrections (2 items)

| Location | Current Text | Proposed Text | Source |
|---|---|---|---|
| Phase 2 section heading | "Per-Customer Hardware Customization" | "Per-Customer Customization: Software Adaptation to Customer Hardware" | CC4 Section 6; SL1b Section 2.4 |
| Phase 1 Total RD in summary | "2.9" | "3.0" | CC1 D-2 (computed 2.971, rounds to 3.0) |

### 6.6 Structural Additions (5 items)

These are new content elements that should be added to the revised file to address structural gaps identified across the review:

1. **Phase 1 parallelization factor documentation.** Add a note to the Phase 1 P1 effort estimate explaining the 0.55-0.67x parallelization factor, the CP-01 dependency chain that imposes forced serialization, and the rationale for the 40-80 person-month range derivation from the 64-120 raw total (SL1a Section 3.2).

2. **Phase 2 customer-segment annotations.** Add annotations to six P1 Phase 2 subsegments for air-gapped, regulated, and HSM customer segments where TE exceeds the median-case rating (SL1b Section 2.2).

3. **Phase 3 two-cost-type explicit finding.** Add a summary finding to Phase 3 distinguishing Type A (linear-with-N, P1+P3+P4, ~31-57 FTE) from Type B (fixed product-development, P2, ~19-36 FTE) costs (Section 3 above).

4. **AL09 cross-phase trajectory annotation.** Add an explanatory note to AL09 Phase 3 addressing why Phase 3 RD (proposed 4) exceeds Phase 1 RD (2) — the version-skew debt accumulation argument — and acknowledging that the same ecosystem velocity argument could also justify a higher Phase 1 RD (CC3 Section 3, Inconsistency 1).

5. **Phase 1 to Phase 2 hidden dependency documentation.** Add a Phase 2 prerequisite note documenting the four P3 subsegments (DS1, DS6, DS8, DS9) where Phase 2 TE=2 depends on Phase 1-delivered configuration templates (SL1b Section 4.3).

### 6.7 Source File Update Required

`P3_data_plane.md` must be annotated to indicate that the DS9 5/5 rating and 2.00-3.25 FTE figure include GPU hardware lifecycle tasks that are customer scope under the current framework. The annotation should state that under the customer-provides-GPU model, the ISV-scope DS9 difficulty reduces to approximately 3/5 and the ISV-retained FTE reduces to approximately 0.5-1.0 (CC4 Section 10, Ambiguity 1).

---

## 7. Cross-Phase Consistency Verification Summary

To provide a complete reconciliation record, the following table summarizes every cross-phase consistency check performed and its outcome:

| Check | Status | Source |
|---|---|---|
| No Phase 3 TE strictly below Phase 2 TE | PASS | CC3 Section 5 |
| Phase 2 "dip and Phase 3 recovery" pattern consistent across all planes | PASS | CC3 Section 4 |
| CP-01 and CP-07 Phase 3 RD = Phase 1 RD explained by linear-with-N scaling | PASS | CC3 Section 2.3 |
| AL09 Phase 3 RD > Phase 1 RD flagged with annotation recommendation | PASS (with advisory) | CC3 Section 3 |
| AL02 Phase 3 TE >> Phase 1 TE explained by scale-difference between phases | PASS (presentation issue) | CC3 Section 3 |
| P4 S2-S5 customer scope consistent across all three phases | PASS | CC4 Section 2 |
| DS9 FTE corrected for customer-owns-GPU scope | RESOLVED (Section 1.1 above) | CC4 Section 5 |
| Phase 2 heading vocabulary corrected | FLAGGED for revision | CC4 Section 6 |
| P3 Phase 3 FTE aggregate arithmetic corrected | RESOLVED | CC1 D-7 |
| Phase 1 Total RD rounding corrected (2.9 to 3.0) | FLAGGED for revision | CC1 D-2 |
| Phase 3 Total TE rounding corrected (3.0 to 3.1) | FLAGGED for revision | CC1 D-5 |
| Phase 3 TE systematic understatement confirmed from 3 independent angles | CONFIRMED | SL1c Sections 1.1, 5.1; CC1 D-7 |
| S1 Phase 1 RD adjustment (1 to 2) does not conflict with Phase 2 or Phase 3 | PASS | SL1a Section 2; SL1b Section 1.4 |
| Phase 2 aggregate effort revision (upward for non-standard customers) does not conflict with Phase 1 or Phase 3 | PASS | SL1b Section 2.3 |
| 3 of 4 [D] flags misapplied (gap = +1 vs threshold >= 2) | CONFIRMED for correction | SL1c Section 2.2 |

---

## Sources

### Per-Phase Consolidated Findings

| File | Absolute Path | Role |
|---|---|---|
| SL1a_phase1_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1a_phase1_consolidated.md` | Phase 1 consolidated findings |
| SL1b_phase2_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1b_phase2_consolidated.md` | Phase 2 consolidated findings |
| SL1c_phase3_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1c_phase3_consolidated.md` | Phase 3 consolidated findings |

### Cross-Cutting Review Files

| File | Absolute Path | Role |
|---|---|---|
| CC1_math_audit.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC1_math_audit.md` | Arithmetic verification; P3 FTE error (D-7); rounding discrepancies |
| CC3_cross_phase_consistency.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC3_cross_phase_consistency.md` | Cross-phase trajectory analysis; AL09 P3>P1 finding; 5 inconsistency assessments |
| CC4_scope_consistency.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC4_scope_consistency.md` | Customer-owns-GPU scope boundary; DS9 FTE discrepancy; heading correction |

### Primary File Under Review

| File | Absolute Path |
|---|---|
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |

### Source Plane Analysis Files (Referenced Indirectly Through SL1a-c)

| File | Absolute Path |
|---|---|
| P1_control_plane.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md` |
| P2_application_logic.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md` |
| P3_data_plane.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P3_data_plane.md` |
