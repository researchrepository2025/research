# SL3a: Final Review Report — ISV On-Premises Deployment Ratings

**Report Date:** 2026-02-19
**Scope:** Complete consolidated review of `analysis/three_phase_on_prem_ratings.md` — 228 ratings across 38 MECE subsegments, 3 phases, 2 dimensions (Relative Difficulty and Total Effort), 4 planes
**Responsibility Split:** Customer provides hardware + GPUs + AI models; ISV owns ALL software
**Review Methodology:** 35 agents across 9 waves; ~157,000 words of analysis; 503 web + 1,027 corpus citations across 33 completed review files
**Output:** Final review report only. The revised ratings file is produced separately in SL3b.

---

## 1. Executive Summary

### Overall Accuracy Assessment

Of 228 total rating cells in the source file (38 subsegments x 3 phases x 2 dimensions), **approximately 95% are confirmed accurate** by independent review. Of the 102 actively rated cells (excluding customer-scope S2-S5 markers), 10 require numerical adjustment — all upward by +1 magnitude. No rating in the entire file was found to be overstated.

The accuracy rate varies by phase:
- **Phase 1:** 98.5% confirmed. 1 adjustment out of 68 cells (S1 RD 1 to 2). Source: SL1a_phase1_consolidated.md, Section 1.
- **Phase 2:** 100% confirmed. 0 adjustments out of 76 cells. Source: SL1b_phase2_consolidated.md, Key Finding 1.
- **Phase 3:** 79% confirmed at cell level (30 of 38 subsegments need no change). 8 firm +1 adjustments, 1 conditional. Source: SL1c_phase3_consolidated.md, Section 2.1.

### The Three Most Important Findings

1. **Phase 3 Total Effort is systematically understated.** Confirmed from three independent analytical angles: (a) four P1 subsegments have TE ratings whose ceilings fall below ground truth FTE ranges (SL1c, Section 1.1); (b) P2 exhibits a +0.9 systematic divergence where TE exceeds RD across all 10 subsegments (SL1c, Section 5.1; CC2); (c) the P3 FTE aggregate label understates the arithmetic sum by ~2 FTE (CC1 D-7). The convergence of these findings from different planes, different agents, and different methods constitutes the strongest evidence in the review corpus. Source: SL2c_cross_phase_integration.md, Section 5.

2. **P1 Control Plane dominance is understated, not overstated.** Four P1 Phase 3 TE ratings require upward adjustment, widening the gap between P1 and all other planes. After corrections, P1 Phase 3 avg TE rises from 4.1 to 4.5 — a 1.5-point gap above the next-highest plane. P1 is the primary determinant of whether on-premises deployment is economically viable. Source: SL2a_executive_narrative.md, Section 2.

3. **All review corrections run in the same direction: upward.** Of 10 recommended rating adjustments (9 firm + 1 conditional), every one is a +1 increase. No rating was found to be overstated. Additionally, 6 structural risk categories are absent from the framework entirely. The stated costs should be read as floor estimates, not central estimates. Source: SL2a_executive_narrative.md, Section 5.3; SL1c_phase3_consolidated.md, Key Finding 1.

### Top 5 Critical Changes Needed

1. Correct the P3 Phase 3 FTE aggregate label from "~10-18 FTE" to **10.35-17.30 FTE** (after DS9 scope correction). Source: CC1 D-7; SL2c, Section 1.1.
2. Adjust 4 P1 Phase 3 TE ratings upward: CP-03 (4 to 5), CP-06 (3 to 4), CP-08 (3 to 4), CP-10 (4 to 5). Source: SL1c, Section 2.1.
3. Correct DS9 Phase 3 FTE from 2.00-3.25 to **0.50-1.00** (carried from wrong scope assumption). Source: CC4 Section 5; SL2c, Section 1.1.
4. Remove 3 false-positive [D] divergence flags (AL10 Phase 1, AL10 Phase 3, DS10 Phase 3); retain AL09 as sole valid Phase 3 [D] flag after AL09 RD adjustment. Source: SL1c, Section 2.2; CC2.
5. Adjust S1 Phase 1 RD from 1 to **2** (auth re-implementation, Bedrock schema delta, error handling rewrite). Source: SL1a, Section 2; RP4a.

### Bottom Line: Is the Ratings File Reliable for Strategic Decision-Making?

**Yes, with qualifications.** The three-phase framework is structurally sound, the four-plane decomposition is validated by cross-cutting analysis, and the MECE subsegment structure covers the ISV's technical engineering obligations comprehensively. The 10 rating adjustments are all +1 magnitude — none represents a categorical reassessment. However, the file should be used as a **conservative lower bound** on costs, not a central estimate, because: (a) all corrections run upward, (b) Phase 3 TE is systematically understated, (c) 6 structural risk categories are absent, and (d) the Phase 3 FTE estimates assume the ISV can recruit the required specialists — a material assumption given 5.4+ month hiring cycles and 40% of organizations lacking K8s skills (SL1c, Section 5.3; CC5, Section 5).

---

## 2. Methodology

### 2.1 Review Architecture

The review employed a **35-agent, 9-wave architecture** organized in three passes:

**Pass 1 — Ground Truth Extraction (Wave 0):** 5 agents extracted every factual claim, citation, and quantitative assertion from the source planes and cross-reference files, producing GT1 through GT5 ground truth documents. These served as the evidentiary foundation for all subsequent review work.

**Pass 2 — Per-Plane and Cross-Cutting Review (Waves 1-5):**
- Wave 1: RP1a-RP1c (P1 Control Plane infrastructure, security, operations)
- Wave 2: RP1d (P1 Phase 2 deep dive), RP1e (Phase 1 effort plausibility)
- Wave 3: RP2a-RP2b (P2 Application Logic service architecture, resilience/AI/testing)
- Wave 4: RP3a-RP3b (P3 Data Plane traditional and streaming/AI data services)
- Wave 5: RP3c-RP3d (P3 effort validation and FTE scaling), RP4a (P4 ISV scope), RP4b (P4 scope exclusion analysis), RP2c (P2 divergence investigation), RP2e/RP4c (completeness checks)
- Cross-cutting agents: CC1 (math audit), CC2 (divergence rederivation), CC3 (cross-phase trajectory), CC4 (scope consistency), CC5 (missing risks)

**Pass 3 — Synthesis (Waves 6-9):**
- Wave 6: SL1a (Phase 1 consolidated), SL1b (Phase 2 consolidated), SL1c (Phase 3 consolidated)
- Wave 7: SL2a (executive narrative evaluation), SL2b (interview validation guide), SL2c (cross-phase integration)
- Wave 8: Quality gates G1 (structural), G2 (citation), G3 (content review)
- Wave 9: SL3a (this report), SL3b (revised ratings file)

### 2.2 Quality Gates

All waves passed three quality gates:
- **G1 Structural:** Every review file covers all subsegments in its assigned scope and follows the standard section template.
- **G2 Citation:** Every factual claim traces to a source file or external URL. Citation chains are maintained: this report cites SL1/SL2 files, which cite RP/CC files, which cite GT/original sources.
- **G3 Content Review:** Cross-cutting consistency checks (CC1-CC5) independently verified arithmetic, divergence flags, cross-phase trajectories, scope boundaries, and structural completeness.

### 2.3 Corpus Statistics

- **503 web citations** across all review files (external evidence: Replicated, Spectro Cloud, Linux Foundation, Komodor, CNCF, vendor documentation)
- **1,027 corpus citations** (internal citations to source plane files, ground truth documents, and cross-reference materials)
- **33 completed review files** (GT1-GT5, RP1a-RP1e, RP2a-RP2c, RP2e, RP3a-RP3d, RP4a-RP4c, CC1-CC5, SL1a-SL1c, SL2a-SL2c)
- **~157,000 words** of analysis across the review corpus
- **47 arithmetic checks** performed by CC1 (42 verified correct, 5 discrepancies identified)

---

## 3. Findings by Plane

### 3.1 P1 Control Plane (10 subsegments: CP-01 through CP-10)

**Summary:** 98.5% of Phase 1 ratings confirmed. Zero Phase 2 adjustments. Four Phase 3 TE understatements. P1 dominance strengthened after review.

**Phase 1:** All 10 subsegments confirmed ACCURATE with High or Medium-High confidence. P1 Phase 1 averages (RD 4.4, TE 4.0) are the highest of any plane and are arithmetically verified (CC1 Section 2.1). The 80-person-month upper bound is the defensible planning figure; the 40-person-month lower bound requires conditions unlikely to co-occur (experienced team, no learning curve, no 2026 migration calendar impact). The parallelization factor of 0.55-0.67x (converting 64-120 raw person-months to 40-80 stated range) is the most consequential undocumented assumption. Source: SL1a, Sections 1.1, 3.2.

**Phase 2:** All 10 confirmed HOLD. P1 dominates at ~60% of total per-customer effort (SL1b, Key Finding 3). CP-02 (Network Fabric) is the single most variable per-customer subsegment. Six subsegments carry customer-segment annotations for air-gapped, regulated, and HSM customers where TE may exceed median-case ratings by +1. Source: SL1b, Sections 1.1, 2.2.

**Phase 3:** Six of 10 ratings confirmed accurate. **Four TE ratings require upward adjustment,** each driven by ground truth FTE ranges that arithmetically exceed the current TE rating ceiling:

| Subsegment | Current TE | Proposed TE | GT1 FTE Range | TE Ceiling | Source |
|---|:---:|:---:|---|---|---|
| CP-03 IAM/RBAC | 4 | **5** | 2.75-4.75 | 2.5 (TE=4) | SL1c Section 1.1; GT1 |
| CP-06 CI/CD/GitOps | 3 | **4** | 2.00-3.25 | 1.0 (TE=3) | SL1c Section 1.1; GT1 |
| CP-08 Disaster Recovery | 3 | **4** | 1.50-2.50 | 1.0 (TE=3) | SL1c Section 1.1; GT1 |
| CP-10 Security Ops | 4 | **5** | 2.75-5.50 | 2.5 (TE=4) | SL1c Section 1.1; GT1 |

After these adjustments, P1 Phase 3 avg TE rises from 4.1 to 4.5 — widening the gap to the next-highest plane (P3 at 2.9-3.0) by 1.5 points. Source: SL2a, Section 2.

### 3.2 P2 Application Logic (10 subsegments: AL01 through AL10)

**Summary:** 95% of Phase 1 ratings confirmed (all 10). 100% of Phase 2 confirmed. Three Phase 3 adjustments. The P2 systematic divergence of +0.9 (TE exceeding RD) in Phase 3 survives all scrutiny.

**Phase 1:** All 10 confirmed ACCURATE with High confidence. P2 is the lowest-effort plane in Phase 1 because most application logic is tier-invariant. Phase 1 work concentrates in AL03 (API Gateway), AL05 (message bus swap), AL09 (AI orchestration), and AL10 (test infrastructure). Source: SL1a, Section 1.2.

**Phase 2:** All 10 confirmed ACCURATE. P2 Phase 2 averages RD 1.1 / TE 1.2 — application code is architecturally invariant across customers. Source: SL1b, Section 1.2.

**Phase 3:** Seven of 10 confirmed accurate. **Three adjustments recommended:**

| Subsegment | Dimension | Current | Proposed | Rationale | Source |
|---|---|:---:|:---:|---|---|
| AL04 Data Access/ORM | TE | 2 | **3** | Patroni and Redis Sentinel application-layer event handling creates meaningful ongoing work | SL1c Section 1.2; RP2a |
| AL05 Background Jobs/EDA | RD | 2 | **3** | Temporal configuration drift, dead-letter queue burden, 2.0-4.1 FTE ops burden | SL1c Section 1.2; RP2a |
| AL09 AI/ML Orchestration | RD | 3 | **4** | Multi-stack coordination burden (LangGraph + MCP + guardrails + model version compatibility); only subsegment where Phase 3 RD exceeds Phase 1 RD | SL1c Section 1.2; RP2b; CC3 |

**The P2 +0.9 divergence pattern** (TE exceeding RD across all 10 Phase 3 subsegments) is arithmetically exact: sum of gaps = +9, average = +0.90. It is not outlier-driven: removing AL02 (gap = +3) leaves a residual average gap of +0.67 across 9 cells. It is unique to P2 among infrastructure planes. After the AL05 RD adjustment, the gap narrows from +0.9 to +0.8 but remains the dominant structural pattern. Source: CC2, Section 7; RP2c, Sections 2-4; SL1c, Section 5.1.

### 3.3 P3 Data Plane (10 subsegments: DS1 through DS10)

**Summary:** Phase 1 and Phase 2 fully confirmed. Two Phase 3 TE upward adjustments. FTE aggregate corrected. DS9 FTE corrected for scope.

**Phase 1:** All 10 confirmed ACCURATE with High confidence. P3 is the second-largest investment area after P1, accounting for 20-40 person-months. Primary cost drivers: DS1 (Patroni PostgreSQL HA), DS6 (Strimzi Kafka), DS10 (RAG pipeline). Source: SL1a, Section 1.3.

**Phase 2:** All 10 confirmed ACCURATE. However, the aggregate effort estimate of 2-4 person-weeks understates effort for hardware-heterogeneous customers; revised to 3-6 person-weeks for non-standard profiles. Four P3 Phase 2 ratings (DS1, DS6, DS8, DS9) carry hidden Phase 1 dependencies on pre-built configuration templates. Source: SL1b, Sections 1.3, 4.3.

**Phase 3:** Eight of 10 confirmed. Two adjustments:

| Subsegment | Dimension | Current | Proposed | Rationale | Source |
|---|---|:---:|:---:|---|---|
| DS2 NoSQL/Document Store | TE | 2 | **3** | MongoDB FTE 0.6-1.1 maps to TE=3 band (0.3-1.0), not TE=2 (0.1-0.3) | SL1c Section 1.3; RP3a; GT3 |
| DS5 Message Queuing | TE | 2 | **2-3** (conditional) | NATS JetStream = TE 2; RabbitMQ = TE 3 (FTE 0.75-1.25) | SL1c Section 1.3; RP3a |

**Critical FTE corrections:**
- **DS9 Phase 3 FTE:** 2.00-3.25 corrected to **0.50-1.00**. The original figure was computed under ISV-manages-GPU assumptions and includes GPU hardware lifecycle tasks (MIG partitioning, NVLink topology, firmware, thermal monitoring, RMA) that are customer scope under the established split. Source: CC4 Section 5; SL2c Section 1.1.
- **P3 Phase 3 FTE aggregate label:** "~10-18 FTE" corrected to **10.35-17.30 FTE** (after DS9 scope correction). Source: CC1 D-7; SL2c Section 1.1.

### 3.4 P4 AI Model Plane (8 subsegments; 4 ISV-scope: S1, S6, S7, S8)

**Summary:** S1 Phase 1 RD adjusted from 1 to 2. S6/S7 Phase 3 TE borderline at scale. Four unrated residual ISV obligations identified in the scope exclusion gap. Two proposed new subsegments.

**Phase 1:** 3 of 4 ISV-scope subsegments confirmed ACCURATE. S1 RD adjusted from 1 to **2** due to authentication re-implementation (cloud IAM to bearer/mTLS), Bedrock schema delta (system prompt handling differs from OpenAI format), and error handling rewrite (provider-specific error schemas). Source: SL1a, Section 2; RP4a.

**Phase 2:** All 4 ISV-scope subsegments confirmed ACCURATE. Source: SL1b, Section 1.4.

**Phase 3:** All 4 ISV-scope subsegments confirmed at current ratings. At-scale caveats: S6 FTE 0.2-0.5 and S7 FTE 0.1-0.5 extend into TE=3 territory at N=50 customers with active model churn. Source: SL1c, Section 1.4.

**Scope exclusion gap (RP4b):** The binary scope exclusion (customer owns S2-S5, ISV owns S1/S6/S7/S8) accurately models primary infrastructure responsibility but masks **four categories of residual ISV obligation** that are currently unrated and uncosted:

1. Hardware compatibility matrix authorship: 2-4 person-weeks initial, 1-2 person-days/release recurring (RP4b Section 5.2, Category 1)
2. Inference engine version compatibility testing: 1-3 person-weeks per major vLLM release (RP4b Section 5.2, Category 3)
3. Customer GPU allocation triage support: 0.05-0.10 FTE per customer annually (RP4b Section 5.2, Category 2)
4. Per-customer troubleshooting runbooks: 1-3 person-days per customer onboarding (RP4b Section 5.2, Category 4)

Additionally, an unassigned 82% throughput degradation failure mode from AWQ quantization on pre-A100 hardware falls in the boundary between ISV and customer scope (RP4b Key Findings, third bullet). Source: SL2a, Section 4.

---

## 4. Findings by Phase

### 4.1 Phase 1: Initial Refactoring (One-Time Investment)

**Accuracy:** 98.5% of Phase 1 cells confirmed (67 of 68 active cells). Source: SL1a, Section 6, Key Finding 1.

**Sole adjustment:** S1 (Managed API Integration) Phase 1 RD 1 to 2. Source: SL1a, Section 2.

**Effort estimates:**

| Plane | Estimated Investment | Status |
|---|---|---|
| P1 Control Plane | 40-80 person-months | Confirmed. 80 pm upper bound is defensible planning figure. |
| P2 Application Logic | 10-25 person-months | Confirmed. AL10 (test infrastructure) is the largest item. |
| P3 Data Plane | 20-40 person-months | Confirmed. Plausible under parallel execution. |
| P4 AI Model Plane | 2-4 person-months | Confirmed. Minimal ISV footprint. |
| **Total** | **~72-149 person-months** | **Arithmetically consistent. P1+P3 = ~80% of effort.** |

**Key undocumented assumption:** The parallelization factor of 0.55-0.67x (converting the P1 raw unconstrained total of 64-120 person-months to the stated 40-80 range) is not documented in the source file. It assumes a 5-8 engineer team with parallel workstreams constrained by CP-01 serial dependency. This factor is the most consequential undocumented assumption and should be made explicit. Source: SL1a, Section 3.2.

**Learning-curve uplift (not included):** For ISVs with deep cloud-native but no on-premises experience, a 20-30% uplift is typical, pushing the range to 48-104 person-months. Source: SL1a, Section 3.2.

### 4.2 Phase 2: Per-Customer Customization

**Accuracy:** 100% of Phase 2 cells confirmed — the strongest validation finding in the entire review. Source: SL1b, Key Finding 1.

**No individual cell rating changes.** However, aggregate effort estimates require revision for non-standard customer profiles:

| Customer Segment | Current Estimate | Revised Estimate | Source |
|---|---|---|---|
| Standard (connected, commercially regulated) | 10-21 person-weeks | 10-21 pw (no change) | SL1b Section 2.1 |
| Hardware-heterogeneous | 10-21 pw | **12-25 pw** | SL1b Section 2.3 |
| Air-gapped / regulated | 10-21 pw | **14-27 pw** | SL1b Section 2.3 |
| First 3-4 customers | N/A | Exceeds even revised ranges | SL1b Section 4.2 |

The customer segments most likely to require on-premises deployment (regulated industries, government, defense) are precisely those where the higher ranges apply. Source: SL2a, Section 1.5.

**Phase 2 heading correction:** "Per-Customer Hardware Customization" should be corrected to "Per-Customer Customization: Software Adaptation to Customer Hardware" per CC4 Section 6. The ISV customizes software to hardware; the ISV does not customize hardware.

### 4.3 Phase 3: Ongoing Updates and Support

**Accuracy:** 79% of Phase 3 subsegments need no change (30 of 38). Eight firm +1 adjustments plus 1 conditional. All adjustments are upward — no rating overstated. Source: SL1c, Key Finding 1.

**THE KEY FINDING: Systematic Phase 3 TE understatement,** confirmed from three independent angles:

1. **P1 TE ceiling violation (SL1c Section 1.1):** Four P1 subsegments have ground truth FTE ranges that exceed the TE rating's mathematical ceiling. This is not interpretive — it is arithmetic.

2. **P2 divergence masking (SL1c Section 5.1; CC2):** The +0.9 average gap (TE > RD) across all 10 P2 subsegments means planners screening on difficulty alone will miss ~19-36 FTE of ongoing cost.

3. **P3 FTE aggregate error (CC1 D-7):** The stated "~10-18 FTE" for P3 understates the arithmetic sum of subsegment FTE ranges. After DS9 scope correction, the true P3 aggregate is 10.35-17.30 FTE.

**Two cost types in Phase 3:**

| Cost Type | Composition | FTE Range | Share |
|---|---|---|---|
| **Type A: Linear-with-N** | P1 + P3 + P4 infrastructure | 30.80-56.75 FTE | ~62% |
| **Type B: Fixed product-development** | P2 application logic | 18.55-35.60 FTE | ~38% |
| **Total** | All planes | ~50-93 FTE | 100% |

Source: SL2c, Section 3.3.

The ~60/40 split means an ISV with a single on-premises customer still carries approximately 40% of the full Phase 3 FTE burden. The fixed cost floor is comparable in magnitude to the variable cost pool, making on-premises deployment economically challenging below a threshold customer count. Source: SL2c, Section 3.3.

**Corrected Phase 3 Grand Total:** ~50-93 FTE (revised from ~49-93 in the original file). Computed: P1 20.0-38.0 + P2 18.55-35.60 + P3 10.35-17.30 + P4 0.45-1.45 = 49.35-92.35, rounding to ~50-93. Source: SL2c, Section 1.1.

---

## 5. Cross-Cutting Findings

### 5.1 Material Math Error: P3 FTE Aggregate

The stated P3 Phase 3 FTE aggregate of "~10-18 FTE" is arithmetically incorrect. The sum of individual subsegment FTE ranges (after DS9 scope correction) is 10.35-17.30 FTE. All 10 individual subsegment FTE values match ground truth exactly; only the summary label is wrong. This error was independently identified by RP3d and confirmed by CC1 (D-7). Source: CC1_math_audit.md; SL2c, Section 1.1.

### 5.2 [D] Divergence Flag Audit: 3 of 4 Are False Positives

The [D] divergence flag is defined as an RD-TE gap of 2+ points. Of the four [D] flags applied in the source file:

| Location | RD | TE | Gap | Verdict | Source |
|---|:---:|:---:|:---:|---|---|
| AL02 Phase 3 | 1 | 4 | +3 | **RETAIN** — only correct [D] in Phase 3 | CC2; SL1c Section 2.2 |
| AL10 Phase 1 | 3 | 4 | +1 | **REMOVE** — gap below threshold | CC2; SL1c Section 2.2 |
| AL10 Phase 3 | 3 | 4 | +1 | **REMOVE** — gap below threshold | CC2; SL1c Section 2.2 |
| DS10 Phase 3 | 3 | 4 | +1 | **REMOVE** — gap below threshold | CC2; SL1c Section 2.2 |

The underlying divergence narratives in these cells are analytically correct (effort genuinely exceeds difficulty), but the formal [D] threshold of >= 2 is not met. The divergence prose should be preserved as explanatory notes even where the [D] flag is removed.

After the AL09 Phase 3 RD adjustment (3 to 4), AL09 becomes a valid [D] candidate (RD 4, TE 4, gap 0) — however, the gap is now 0, so it does not qualify. The sole valid Phase 3 [D] flag is AL02.

### 5.3 DS9 FTE Carry-Over from Wrong Scope Assumption

The DS9 Phase 3 FTE of 2.00-3.25 was computed in `P3_data_plane.md` under ISV-manages-GPU assumptions, including GPU hardware lifecycle tasks (MIG partitioning, NVLink topology management, firmware updates, thermal monitoring, RMA processes). Under the established customer-provides-GPU scope, these tasks transfer to the customer, leaving approximately 0.50-1.00 FTE of ISV-retained work (model serving configuration, batch queue management, model version management, pipeline tuning). This scope error was identified by CC4 Section 5 and confirmed in SL2c Section 1.1.

**Impact:** Reduces P3 Phase 3 FTE from 11.85-19.55 (SL1c pre-scope-fix) to 10.35-17.30 (fully corrected). The magnitude (~1.5-2.25 FTE, or ~2-3% of the Phase 3 grand total) is small but the correction is important as a precedent: scope-boundary decisions propagate through the entire model. Source: SL2c, Section 1.1.

### 5.4 Six Structurally Absent Risk Categories

CC5 identified six risk categories that are completely absent from the 38-subsegment framework. None appears as a rated subsegment or an explicit cost assumption:

| Gap | Severity | Primary Phase Impact | Source |
|---|:---:|---|---|
| 1. Talent acquisition difficulty | High | Phase 3: Can the 50-93 FTE be recruited? 5.4+ month avg hiring cycles, 40% of orgs lack K8s skills | CC5 Section 5 |
| 2. Customer communication overhead | High | Phase 3: Upgrade coordination labor per customer is uncosted in CP-07 | CC5 Section 2 |
| 3. Supply chain security (SBOM, CVE velocity) | High | Phase 3: 40+ OSS components, 40K+ CVEs/year; CP-10 underweights this | CC5 Section 4 |
| 4. Organizational change management | High | Phase 1: ISV team restructuring from cloud-native to hybrid support model | CC5 Section 1 |
| 5. Vendor lock-in reversal cost | Medium-High | Phase 1: Step Functions to Temporal migration cost; bleeding into Phase 3 | CC5 Section 3 |
| 6. Regulatory variance across customers | Medium-High | Phase 3: Code-level compliance divergence not captured in CP-09 | CC5 Section 6 |

The talent acquisition gap is the most material for Phase 3 planning: the FTE estimates answer "what does this cost if staffed?" but not "can it be staffed?" Source: SL1c, Section 5.3; CC5.

### 5.5 Phase 3 TE Systematic Understatement: Three Independent Confirmations

The single most important cross-cutting finding is that Phase 3 TE is systematically understated across P1, P2, and P3. Three independent analytical methods converge on this conclusion:

1. **GT1 FTE-to-TE-ceiling mapping (P1):** Ground truth FTE ranges exceed TE rating ceilings for CP-03, CP-06, CP-08, CP-10. Source: SL1c, Section 1.1.
2. **P2 +0.9 divergence (P2):** Effort consistently exceeds difficulty across all 10 P2 Phase 3 subsegments; planners screening on RD alone will miss 18.6-35.6 FTE. Source: CC2, Section 7; RP2c.
3. **P3 FTE arithmetic error (P3):** Aggregate label understates arithmetic sum. Source: CC1 D-7; RP3d.

The convergence strengthens the conclusion beyond what any single finding would support. Source: SL2c, Section 5.

---

## 6. Recommended Rating Changes

### 6.1 Complete Table of All Proposed Adjustments

| # | Subsegment | Phase | Dimension | Current | Proposed | Justification | Source |
|:---:|---|---|---|:---:|:---:|---|---|
| 1 | S1 Managed API Integration | Phase 1 | RD | 1 | **2** | Auth re-implementation (cloud IAM to bearer/mTLS), Bedrock schema delta, error handling rewrite | SL1a Section 2; RP4a |
| 2 | CP-03 IAM/RBAC | Phase 3 | TE | 4 | **5** | GT1 FTE 2.75-4.75 exceeds TE=4 ceiling (2.5 FTE) | SL1c Section 1.1; GT1 |
| 3 | CP-06 CI/CD Pipeline/GitOps | Phase 3 | TE | 3 | **4** | GT1 FTE 2.00-3.25 maps to TE=4 band (1.0-2.5), not TE=3 (0.3-1.0) | SL1c Section 1.1; GT1 |
| 4 | CP-08 Disaster Recovery/BC | Phase 3 | TE | 3 | **4** | GT1 FTE 1.50-2.50 exceeds TE=3 ceiling (1.0 FTE) | SL1c Section 1.1; GT1 |
| 5 | CP-10 Security Operations | Phase 3 | TE | 4 | **5** | GT1 FTE floor 2.75 exceeds TE=4 ceiling (2.5 FTE) | SL1c Section 1.1; GT1 |
| 6 | AL04 Data Access/ORM/Caching | Phase 3 | TE | 2 | **3** | Patroni and Redis Sentinel application-layer event handling overhead | SL1c Section 1.2; RP2a |
| 7 | AL05 Background Jobs/Async/EDA | Phase 3 | RD | 2 | **3** | Temporal config drift, dead-letter queue burden, 2.0-4.1 FTE ops load | SL1c Section 1.2; RP2a |
| 8 | AL09 AI/ML Orchestration | Phase 3 | RD | 3 | **4** | Multi-stack coordination burden; ranked #1 hardest subsegment in source difficulty; only subsegment where P3 RD > P1 RD | SL1c Section 1.2; RP2b; CC3 |
| 9 | DS2 NoSQL/Document Store | Phase 3 | TE | 2 | **3** | MongoDB FTE 0.6-1.1 maps to TE=3 band (0.3-1.0), not TE=2 (0.1-0.3) | SL1c Section 1.3; RP3a; GT3 |
| 10 | DS5 Message Queuing (conditional) | Phase 3 | TE | 2 | **2-3** | NATS JetStream: TE=2; RabbitMQ: TE=3 (FTE 0.75-1.25) | SL1c Section 1.3; RP3a |

### 6.2 FTE Corrections

| Location | Current | Corrected | Source |
|---|---|---|---|
| DS9 Phase 3 Research FTE | 2.00-3.25 | **0.50-1.00** | CC4 Section 5; SL2c Section 1.1 |
| P3 Phase 3 FTE aggregate label | "~10-18 FTE" | **~10-17 FTE** (10.35-17.30) | CC1 D-7 + DS9 scope correction |
| Phase 3 Grand Total FTE | "~49-93 FTE" | **~50-93 FTE** (49.35-92.35) | SL2c Section 1.1 |

### 6.3 [D] Flag Corrections

| Location | Current | Action | Rationale | Source |
|---|---|---|---|---|
| AL10 Phase 1 | [D] applied | **REMOVE** | Gap = +1, threshold requires >= 2 | CC2; SL1c Section 2.2 |
| AL10 Phase 3 | [D] applied | **REMOVE** | Gap = +1, threshold requires >= 2 | CC2; SL1c Section 2.2 |
| DS10 Phase 3 | [D] applied | **REMOVE** | Gap = +1, threshold requires >= 2 | CC2; SL1c Section 2.2 |
| AL02 Phase 3 | [D] applied | **RETAIN** | Gap = +3, correctly exceeds threshold; sole valid [D] | CC2; SL1c Section 2.2 |

### 6.4 Average Recalculations After All Adjustments

| Metric | Current | Revised | Source |
|---|---|---|---|
| P4 Phase 1 avg RD | 1.5 | 1.75 | SL1a Section 1.4 |
| P1 Phase 3 avg TE | 4.1 | 4.5 | SL1c Section 4.3 |
| P2 Phase 3 avg RD | 1.8 | 2.0 | SL1c Section 4.3 |
| P2 Phase 3 avg TE | 2.7 | 2.8 | SL1c Section 4.3 |
| P3 Phase 3 avg TE | 2.9 | 3.0 | SL1c Section 4.3 |
| Phase 1 Total RD | 2.9 (stated) | 3.0 (computed 2.971, rounds to 3.0) | CC1 D-2 |
| Phase 3 Total TE | 3.0 (stated) | 3.1+ (was 3.059 before adjustments) | CC1 D-5 + SL1c |

### 6.5 Heading and Vocabulary Corrections

| Location | Current | Corrected | Source |
|---|---|---|---|
| Phase 2 section heading | "Per-Customer Hardware Customization" | "Per-Customer Customization: Software Adaptation to Customer Hardware" | CC4 Section 6 |
| Phase 1 Total RD in summary table | "2.9" | "3.0" | CC1 D-2 |

### 6.6 Structural Additions from SL2c

| Addition | Description | Source |
|---|---|---|
| Phase 1 parallelization factor | Document the 0.55-0.67x factor, CP-01 dependency chain, and derivation of 40-80 from 64-120 raw total | SL1a Section 3.2; SL2c Section 6.6 |
| Phase 2 customer-segment annotations | Annotations on 6 P1 Phase 2 cells for air-gapped, regulated, HSM customer segments | SL1b Section 2.2; SL2c Section 6.6 |
| Phase 3 two-cost-type finding | Explicit articulation of Type A (linear, ~31-57 FTE) vs. Type B (fixed, ~19-36 FTE) | SL2c Section 3; SL2c Section 6.6 |
| AL09 trajectory annotation | Explain why Phase 3 RD (4) > Phase 1 RD (2): version-skew debt accumulation | CC3; SL2c Section 6.6 |
| Phase 2 hidden dependency note | Document 4 P3 subsegments where Phase 2 TE=2 depends on Phase 1 configuration templates | SL1b Section 4.3; SL2c Section 6.6 |

---

## 7. Confidence Map

### 7.1 Confidence Distribution Across All Ratings

| Confidence Level | Phase 1 | Phase 2 | Phase 3 | Total |
|---|:---:|:---:|:---:|:---:|
| **High** | 28 of 34 active cells (82%) | 28 of 34 active cells (82%) | 20 of 34 active cells (59%) | 76 of 102 (75%) |
| **Medium** | 6 of 34 (18%) | 6 of 34 (18%) | 12 of 34 (35%) | 24 of 102 (24%) |
| **Low** | 0 | 0 | 2 of 34 (6%) | 2 of 102 (2%) |

Source: Confidence levels aggregated from SL1a Section 1 (Phase 1), SL1b Section 1 (Phase 2), SL1c Sections 1-2 (Phase 3).

### 7.2 Lowest-Confidence Subsegments

The following subsegments carry the lowest review confidence and would benefit most from empirical validation:

| Subsegment | Phase | Current Rating | Confidence | Uncertainty Source |
|---|---|---|:---:|---|
| CP-01 K8s Cluster Lifecycle | Phase 2 | RD=4, TE=4 | Medium | Customer hardware heterogeneity impact unquantified |
| CP-04 Secrets/Certs/PKI | Phase 3 | RD=4, TE=4 | Medium | Borderline RD 4-5 due to air-gapped Shamir unsealing; FIPS 140-3 transition |
| DS8 Vector Database | Phase 3 | RD=4, TE=3 | Medium | Borderline TE 3-4; Milvus Woodpecker WAL migration; HNSW recall degradation |
| DS9 Embedding Pipeline | Phase 2/3 | Various | Medium | GPU-tier template dependency; scope correction reduces confidence in P3 FTE |
| AL09 AI/ML Orchestration | Phase 3 | RD=3 (proposed 4) | Medium | Only subsegment where P3 RD > P1 RD; ecosystem velocity argument is strong but asymmetrically applied |
| P4 residual obligations | All phases | Unrated | Low | Four unrated ISV obligations from RP4b; FTE estimates marked [UNVERIFIED] |
| CC5 structural gaps | Phase 3 | Unrated | Low | Six absent risk categories; qualitative estimates only |

### 7.3 Where Interview Validation Would Change the Most Ratings

Interview validation would have the highest impact in three areas:

1. **Phase 1 aggregate effort (VE-1):** A single empirical data point on total Phase 1 person-months would validate or invalidate the 72-149 pm range and the undocumented parallelization factor, affecting the interpretation of all P1 and P3 Phase 1 ratings.

2. **Phase 3 FTE headcount (VE-2):** A single empirical data point on actual on-premises support FTE would validate or invalidate the ~50-93 FTE projection and would confirm or refute the P2 systematic divergence.

3. **Phase 2 per-customer deployment time (PE-1, PE-2, DE-1):** Three data points (K8s config time, network config time, data service deployment time) would validate the per-customer effort estimates and the customer-segment variance.

---

## 8. Interview Priorities

### 8.1 Top 10 Must-Ask Questions

These questions are selected for maximum confidence impact: each would resolve uncertainty across 3+ ratings if answered empirically. They are listed in priority order.

| # | Question | Target Role | Validates | Priority Tier |
|:---:|---|---|---|:---:|
| Q1 | "For your initial on-premises refactoring, how many total person-months did the project consume, over how many calendar months, with how large a team?" | VP Engineering / CTO | Phase 1 aggregate (72-149 pm), parallelization factor, P1 averages | Tier 1 |
| Q2 | "For each new on-premises customer deployment, how many engineer-weeks on K8s cluster configuration specific to that customer's hardware?" | Platform Engineer | CP-01 Phase 2 RD=4/TE=4, Phase 2 P1 aggregate | Tier 1 |
| Q3 | "How much time is consumed specifically by network configuration (firewall, proxy, DNS, CNI) versus all other deployment tasks?" | Platform Engineer / SRE | CP-02 Phase 2 RD=4/TE=4, P1 Phase 2 aggregate | Tier 1 |
| Q4 | "How many FTEs are currently dedicated to on-premises customer support operations? How does this compare to your original staffing model?" | VP Engineering / CTO | Phase 3 grand total (~50-93 FTE), P2 divergence, all Phase 3 FTE ranges | Tier 1 |
| Q5 | "When deploying your data stack to a new customer environment, how much is parameter-file changes versus active investigation of the customer's hardware?" | Data Platform Engineer | DS1/DS6/DS8/DS9 Phase 2 TE=2, hidden Phase 1 template dependency | Tier 1 |
| Q6 | "When upgrading LangGraph or MCP server in on-prem, how many other AI stack components require coordinated testing in the same window?" | Principal Engineer | AL09 Phase 3 RD=3 (proposed 4), CP-07 scope boundary | Tier 1 |
| Q7 | "How many FTE annually on IAM work (Keycloak upgrades, federation maintenance, RBAC policy updates, identity incidents) across on-prem customers?" | VP Engineering | CP-03 Phase 3 TE=4 (proposed 5), deduplication methodology | Tier 1 |
| Q8 | "What is your average time-to-hire for platform engineers with K8s operations experience? Does it exceed 5 months?" | VP Engineering / CTO | CC5 talent acquisition gap, Phase 3 FTE executability | Tier 2 |
| Q9 | "What percentage of customers require air-gapped deployment? What is the engineering time for artifact bundle prep versus a proxy-accessible customer?" | Platform Engineer | CP-06 Phase 2 TE annotation, P1 Phase 2 air-gapped segment | Tier 2 |
| Q10 | "How frequently do Temporal version upgrades require changes to workflow SDK code? Who owns dead-letter queue handling -- platform or backend?" | Principal / Backend Engineer | AL05 Phase 3 RD=2 (proposed 3), Temporal config drift | Tier 2 |

Source: SL2b_interview_guide.md, Top 10 Section.

### 8.2 Minimum Viable Interview Set

If only 3 interviews are possible (~3 hours total):

1. **VP Engineering / CTO (60 min):** Questions VE-1 (Q1), VE-2 (Q4), VE-3 (Q8), VE-8 (Q7), VE-5 (SOC scope). Covers Top 10 Q1, Q4, Q7, Q8.

2. **Platform Engineer / DevOps Lead (60 min):** Questions PE-1 (Q2), PE-2 (Q3), PE-4 (Q9), PE-3 (PKI integration), PE-7 (Vault seal/unseal). Covers Top 10 Q2, Q3, Q9.

3. **Data Platform Engineer / DBA (45 min):** Questions DE-1 (Q5), DE-5 (config templates), DE-2 (Kafka reconfiguration), DE-3 (vector index tuning). Covers Top 10 Q5.

This set addresses 9 of the Top 10 questions. A fourth session with a Principal/Staff Engineer (60 min) would cover the remaining 2 (Q6, Q10). Source: SL2b, Minimum Viable Interview Set.

### 8.3 Cross-Reference: Proposed Changes to Interview Questions

| Proposed Adjustment | Interview Question(s) | Would Confirm If... | Would Reverse If... |
|---|---|---|---|
| S1 Phase 1 RD 1 to 2 | PS-2 (S1 API migration) | Auth rewrite took weeks, not hours | vLLM OpenAI-compatible endpoint required only URL swap |
| CP-03 Phase 3 TE 4 to 5 | VE-8 / Q7 (IAM FTE at scale) | IAM FTE exceeds 2.5 across customer base | IAM work is 1.5-2.0 FTE with mature tooling |
| CP-06 Phase 3 TE 3 to 4 | PE-8 (GitOps architecture pattern) | Per-customer GitOps controller instances, not hub-and-spoke | Hub-and-spoke with strong automation holds TE=3 |
| CP-08 Phase 3 TE 3 to 4 | VE-2 / Q4 (Phase 3 FTE, indirect) | DR testing is per-customer on regular cadence | DR testing is shared/quarterly across all customers |
| CP-10 Phase 3 TE 4 to 5 | SR-4 (CVE triage burden) | CVE triage > 2.5 FTE across N environments | Automated CVE scanning keeps load below 2.0 FTE |
| AL04 Phase 3 TE 2 to 3 | BE-3 (Patroni connection topology) | Backend team spends > 4 hrs/month on Patroni events | Patroni failover is transparent to application layer |
| AL05 Phase 3 RD 2 to 3 | BE-1 / Q10 (Temporal/DLQ ownership) | Temporal upgrades require SDK code changes | Temporal upgrades are configuration-only |
| AL09 Phase 3 RD 3 to 4 | PS-1 / Q6 (AI orchestration coordination) | 3+ components require coordinated testing per upgrade | LangGraph upgrades are isolated from other stack components |
| DS2 Phase 3 TE 2 to 3 | PS-4 (NoSQL technology) | MongoDB replica set operations consume > 0.3 FTE | ScyllaDB or DynamoDB-compatible with lower operational burden |
| DS5 Phase 3 TE 2 to 3 | PS-3 (message broker) | Production broker is RabbitMQ | Production broker is NATS JetStream |
| DS9 FTE 2.00-3.25 to 0.50-1.00 | DE-4 (GPU-tier tuning) | ISV-retained embedding work is 0.5-1.0 FTE | ISV retains more GPU-adjacent work than scope split suggests |

Source: SL2b, Cross-Reference table.

---

## 9. Structural Additions Recommended

### 9.1 Proposed New Subsegments

Three new subsegments have been identified by completeness review agents as structurally absent from the current 38-subsegment framework:

| Proposed ID | Name | Plane | Rationale | Source |
|---|---|---|---|---|
| S9 | AI Safety / Guardrails | P4 | Content filtering, prompt injection defense, output validation, safety policy enforcement. Currently scattered across AL09 and S1 without dedicated coverage. Emerging regulatory requirements (EU AI Act) create Phase 3 compliance obligations. | RP4c |
| S10 | Model Cost Attribution | P4 | Per-customer inference cost metering, token accounting, usage-based billing integration. Currently absent from P4 scope. Critical for ISV business model when customer provides GPU but ISV must track consumption. | RP4c |
| AL11 | Notification / Communication Services | P2 | Push notifications, email delivery, SMS/voice, in-app messaging. Currently absent from the 10 P2 subsegments. Every SaaS product has notification infrastructure; it requires on-premises adaptation (self-hosted email relay, webhook delivery over customer networks). | RP2e |

**Recommendation:** S9 and S10 should be added to P4 as rated subsegments. AL11 should be evaluated for P2 inclusion. None of these additions would change the existing 38-subsegment ratings; they would extend the framework.

### 9.2 New Risk Categories to Model

The six structural gaps identified by CC5 (Section 5.4 of this report) should be addressed through one of two mechanisms:

**Option A — Framework extension:** Add rated subsegments or cost multipliers for talent acquisition, customer communication, supply chain security, organizational change management, vendor lock-in reversal, and regulatory variance.

**Option B — Qualitative overlay (recommended):** Add a "Risk Factors Not Captured in Ratings" section to the source file that describes each gap qualitatively, with directional FTE impact estimates where available. This preserves the MECE integrity of the 38-subsegment framework while ensuring readers are aware of the gaps.

Directional estimates from CC5:
- Talent acquisition: 5.4+ month avg hiring cycles; 40% of organizations lack K8s skills (Spectro Cloud 2025, Linux Foundation 2024)
- Customer communication: Hidden multiplier on CP-07 and CP-10 Phase 3 effort
- Supply chain security: 40K+ CVEs/year across 40+ OSS components
- Organizational change: Pre-Phase-1 restructuring cost; no quantified estimate available
- Vendor lock-in reversal: Bleeding Phase 1 cost (e.g., Step Functions to Temporal migration)
- Regulatory variance: Potential for mutually incompatible customer compliance requirements requiring feature flags

Source: CC5; SL1c, Section 5.3.

### 9.3 Heading Corrections and [D] Flag Corrections

**Heading corrections:**
1. Phase 2 section heading: "Per-Customer Hardware Customization" to "Per-Customer Customization: Software Adaptation to Customer Hardware" (CC4 Section 6)
2. Phase 1 Total RD: "2.9" to "3.0" (CC1 D-2)

**[D] flag corrections:**
1. Remove [D] from AL10 Phase 1 (gap = +1, below >= 2 threshold)
2. Remove [D] from AL10 Phase 3 (gap = +1, below >= 2 threshold)
3. Remove [D] from DS10 Phase 3 (gap = +1, below >= 2 threshold)
4. Retain [D] on AL02 Phase 3 (gap = +3, correctly exceeds threshold)
5. Preserve divergence narratives in Notes column for all removed [D] flags

Source: CC2; SL1c, Section 2.2.

---

## Sources

### Synthesis Layer Files (Direct Inputs to This Report)

| File | Absolute Path | Sections Used |
|---|---|---|
| SL1a_phase1_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1a_phase1_consolidated.md` | Phase 1 accuracy, effort estimates, S1 adjustment, key findings |
| SL1b_phase2_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1b_phase2_consolidated.md` | Phase 2 accuracy, aggregate revision, customer-segment annotations |
| SL1c_phase3_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1c_phase3_consolidated.md` | Phase 3 adjustments, FTE corrections, divergence analysis, structural gaps |
| SL2a_executive_narrative.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL2a_executive_narrative.md` | Narrative evaluation, finding-by-finding assessment, revised key findings |
| SL2b_interview_guide.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL2b_interview_guide.md` | Top 10 questions, role-by-role guide, minimum viable interview set |
| SL2c_cross_phase_integration.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL2c_cross_phase_integration.md` | DS9 conflict resolution, two-cost-type decomposition, structural changes catalog |

### Cross-Cutting Review Files (Referenced Through SL1/SL2)

| File | Absolute Path | Key Contribution |
|---|---|---|
| CC1_math_audit.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC1_math_audit.md` | 47 arithmetic checks; P3 FTE error (D-7); rounding discrepancies |
| CC2_divergence_rederivation.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC2_divergence_rederivation.md` | Complete 102-cell gap calculation; [D] flag audit; +0.9 verification |
| CC3_cross_phase_consistency.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC3_cross_phase_consistency.md` | Cross-phase trajectory; AL09 P3>P1 finding |
| CC4_scope_consistency.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC4_scope_consistency.md` | Customer-owns-GPU scope boundary; DS9 FTE discrepancy; heading correction |
| CC5_missing_risks.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC5_missing_risks.md` | 6 structural gaps: talent, communication, supply chain, org change, lock-in, regulatory |

### Per-Plane Review Files (Referenced Through SL1a-c)

| File | Key Contribution |
|---|---|
| RP1a_P1_infrastructure_core.md | CP-01 to CP-03 all-phase verdicts |
| RP1b_P1_security_delivery.md | CP-04 to CP-06 all-phase verdicts |
| RP1c_P1_operations_compliance.md | CP-07 to CP-10 all-phase verdicts |
| RP1d_P1_phase2_deep_dive.md | P1 Phase 2 customer-segment analysis; air-gapped data |
| RP1e_P1_phase1_effort.md | Phase 1 effort plausibility; parallelization factor |
| RP2a_P2_service_architecture.md | AL01-AL05 all-phase verdicts; AL04/AL05 Phase 3 adjustments |
| RP2b_P2_resilience_ai_testing.md | AL06-AL10 all-phase verdicts; AL09 Phase 3 adjustment |
| RP2c_P2_divergence_investigation.md | P2 +0.9 divergence validation; scale bias assessment |
| RP2e_P2_completeness.md | AL11 notification subsegment proposal |
| RP3a_P3_traditional_data.md | DS1-DS5 all-phase verdicts; DS2/DS5 Phase 3 adjustments |
| RP3b_P3_streaming_ai_data.md | DS6-DS10 all-phase verdicts; DS10 [D] flag finding |
| RP3c_P3_effort_validation.md | P3 Phase 2 aggregate revision; hidden dependency analysis |
| RP3d_P3_fte_scaling.md | P3 FTE aggregate error; scaling classification audit |
| RP4a_P4_isv_scope.md | S1/S6/S7/S8 all-phase verdicts; S1 RD adjustment |
| RP4b_P4_scope_exclusion.md | 4 unrated residual ISV obligations; scope gap analysis |
| RP4c_P4_completeness.md | S9/S10 new subsegment proposals |

### Ground Truth Files

| File | Absolute Path |
|---|---|
| GT1_P1_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md` |
| GT2_P2_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md` |
| GT3_P3_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md` |
| GT4_P4_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT4_P4_ground_truth.md` |
| GT5_cross_reference_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` |

### Primary File Under Review

| File | Absolute Path |
|---|---|
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
