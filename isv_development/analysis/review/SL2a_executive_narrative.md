# SL2a: Executive Narrative Review — Section 8 Key Findings Assessment

**Synthesis Layer:** SL2a — Executive narrative evaluation and revision
**Date:** 2026-02-19
**Scope:** Section 8 (Grand Summary / Key Findings) of `three_phase_on_prem_ratings.md` only. No re-derivation of ratings.
**Input Sources:** SL1a (Phase 1 consolidated), SL1b (Phase 2 consolidated), SL1c (Phase 3 consolidated), RP2c (P2 divergence investigation), RP4b (P4 scope exclusion), CC2 (divergence rederivation)
**Output Type:** Executive narrative assessment with proposed revisions

---

## Executive Summary

The six key findings in Section 8 of `three_phase_on_prem_ratings.md` are directionally correct but require material qualification after the multi-wave review process. Finding 1 ("P1 dominates") remains the strongest claim, now reinforced by the discovery that four P1 Phase 3 TE ratings are understated. Finding 2 ("P2 systematic divergence") survives scrutiny and is arithmetically verified, but the "planning trap" framing needs sharpening: the trap conceals large routine work, not difficult work. Finding 4 ("P4 nearly eliminated") is the most vulnerable, as it omits four categories of unrated residual ISV obligations that the scope exclusion masks. The executive narrative also suffers from three structural deficiencies: it does not acknowledge the systematic upward direction of all review corrections (no rating was overstated), it does not surface the six structurally absent risk categories, and it presents Phase 3 FTE aggregates that are arithmetically incorrect for P3 Data Plane.

---

## 1. Finding-by-Finding Assessment

### 1.1 Finding 1: "P1 (Control Plane) dominates both dimensions across all three phases"

**Original text (Section 8):** "It is the hardest AND the most effort-intensive in Phase 1, Phase 2, and Phase 3. This is the core of the ISV's on-prem resistance."

**Verdict: SUPPORTED, and strengthened after review.**

The review evidence uniformly reinforces P1 dominance. In Phase 1, all 10 P1 subsegments were confirmed ACCURATE with no adjustments required (SL1a_phase1_consolidated.md, Section 1.1). P1 Phase 1 averages of RD 4.4 / TE 4.0 are arithmetically verified (SL1a_phase1_consolidated.md, Section 3.5). The 80-person-month upper bound for P1 Phase 1 is characterized as "the more defensible planning figure" over the 40-person-month lower bound, which "requires conditions that are unlikely to co-occur" (SL1a_phase1_consolidated.md, Key Finding 2).

In Phase 2, P1 dominance at ~60% of total per-customer effort is "structurally correct" per the consolidated findings (SL1b_phase2_consolidated.md, Key Finding 3). CP-02 (Network Fabric) is confirmed as the single most variable per-customer subsegment with the highest confidence rating in the entire Phase 2 P1 review (SL1b_phase2_consolidated.md, Section 1.1, CP-02).

In Phase 3, P1 dominance is not merely confirmed but amplified. Four P1 subsegments — CP-03, CP-06, CP-08, CP-10 — carry recommended TE increases of +1 each (SL1c_phase3_consolidated.md, Section 2.1). These adjustments raise the P1 Phase 3 average TE from 4.1 to 4.5, widening the gap between P1 and all other planes. The proposed adjustments are driven by ground truth FTE ranges that arithmetically exceed the current TE rating ceilings: CP-03 FTE of 2.75-4.75 exceeds the TE=4 ceiling of 2.5 FTE; CP-10 FTE floor of 2.75 exceeds the TE=4 ceiling (SL1c_phase3_consolidated.md, Section 1.1).

**Assessment for the executive narrative:** Finding 1 is the single strongest claim in the document, and the review evidence makes it stronger. The qualification that should be added is that P1 dominance in Phase 3 is even more pronounced than stated: after adjustments, P1 Phase 3 avg TE rises from 4.1 to 4.5, creating a 1.7-point gap over the next highest plane (P3 at 2.9-3.0). The finding should also note that P1 dominance is understated, not overstated — the systematic direction of corrections runs exclusively upward.

---

### 1.2 Finding 2: "P2 (Application Logic) is the largest systematic divergence"

**Original text:** "Average RD of 1.6 vs average TE of 2.1 — a consistent gap across all three phases. In Phase 3, the gap widens to RD 1.8 vs TE 2.7. An ISV that plans based only on relative difficulty will underestimate P2 ongoing costs by ~50%."

**Verdict: SUPPORTED, arithmetically verified, and survives the RP2c investigation. Framing requires qualification.**

The +0.9 average gap in Phase 3 is arithmetically exact: the sum of gaps across 10 P2 Phase 3 cells is +9, and the average is +0.90 (CC2_divergence_rederivation.md, Section 7). Eight of 10 P2 Phase 3 subsegments show TE >= RD, with zero counter-examples (CC2_divergence_rederivation.md, Section 7). Removing the dominant outlier (AL02, gap = +3) still yields a residual average gap of +0.67 across the remaining 9 cells, confirming the divergence is structural and not outlier-driven (RP2c_P2_divergence_investigation.md, Section 2).

The cross-plane comparison validates that the divergence is unique to P2: P1 all-phase avg gap is -0.1 (near-zero), P3 all-phase avg gap is -0.2 (near-zero), and only P2 (+0.5 all-phase) and P4 (+0.4 all-phase, smaller magnitude) show persistent TE > RD patterns (RP2c_P2_divergence_investigation.md, Section 4). P1 and P3 contain only tier-sensitive subsegments where difficulty and effort track together; P2 contains tier-invariant subsegments (AL02, AL04, AL07) where absolute effort is set by application size, not deployment tier (RP2c_P2_divergence_investigation.md, Section 4).

The RP2c investigation further validates that the TE scale is not biased against application logic. The divergence arises because the RD scale correctly awards low scores to tier-invariant work that is nevertheless large in absolute FTE terms — this is a structural feature of how the RD scale is defined, not a calibration error (RP2c_P2_divergence_investigation.md, Section 3).

The 50% underestimation claim is directionally supported: a planner using RD alone would assign P2 approximately 15% of total cost weight (1.6 / 10.6 of all-phase RD averages), while P2's actual Phase 3 FTE share is approximately 38% of total (18.6-35.6 FTE out of 49-93 total). The gap between 15% and 38% is the planning trap (RP2c_P2_divergence_investigation.md, Section 6).

**Critical qualification from RP2c:** The "planning trap" framing is accurate but imprecise. The trap does not conceal difficult work — it conceals large but routine work. An ISV that reads P2 as "easy on-premises" is correct about difficulty but incorrect about cost. RP2c characterizes this as follows: "On-premises adoption does not require ISVs to become better application engineers. It requires them to budget for engineers who are already doing the work, at roughly the same absolute cost as they would incur on cloud-native" (RP2c_P2_divergence_investigation.md, Section 6). This nuance matters for executives: P2 costs are not new costs created by on-premises deployment, they are existing costs that on-premises cost models tend to exclude because they appear tier-invariant.

**Post-review adjustment impact:** Three P2 Phase 3 ratings carry recommended adjustments: AL04 TE 2->3, AL05 RD 2->3, AL09 RD 3->4 (SL1c_phase3_consolidated.md, Section 2.1). If accepted, the P2 Phase 3 RD average rises from 1.8 to 2.0, narrowing the RD-TE gap from +0.9 to +0.8. The divergence is slightly reduced but remains the dominant structural pattern. The finding survives.

**Assessment for the executive narrative:** Finding 2 is well-supported but should be reframed. The current "50% underestimation" language implies a planning error in the ratings themselves. The actual risk is that decision-makers will filter on RD (difficulty) alone and conclude P2 is not a material on-premises cost center, when in fact P2 Phase 3 FTE (18.6-35.6) is comparable in magnitude to P1 Phase 3 FTE (20-38). The reframing should emphasize that P2 is a cost that exists regardless of deployment tier, and the planning failure is not in the ratings but in cost models that exclude tier-invariant expenses.

---

### 1.3 Finding 3: "P3 (Data Plane) is accurately calibrated"

**Original text:** "Difficulty and effort align closely across all three phases. Data service operations are hard AND large in roughly equal measure."

**Verdict: SUPPORTED with one material arithmetic correction.**

The cross-plane divergence comparison confirms P3 calibration: all-phase avg gap is -0.2 (near zero), with the widest individual gap being +1 (DS10 in Phase 1 and Phase 3). No P3 cell reaches the +/-2 [D] threshold (CC2_divergence_rederivation.md, Sections 4 and 5). The characterization that "hard things are also large things" in P3 is validated by the data — P3 difficulty and effort track together across all phases (RP2c_P2_divergence_investigation.md, Section 4).

However, the P3 Phase 3 FTE aggregate requires correction. The stated "~10-18 FTE" is arithmetically incorrect: the actual sum of individual subsegment FTE ranges is 11.85-19.55 FTE (SL1c_phase3_consolidated.md, Section 4.1). This is the highest-priority arithmetic correction in the entire Phase 3 review. The error propagates to the Phase 3 grand total, which should be revised from "~49-93 FTE" to approximately "~51-95 FTE" (SL1c_phase3_consolidated.md, Section 4.1).

Additionally, one P3 Phase 3 subsegment carries a recommended TE adjustment: DS2 (NoSQL/Document Store) TE 2->3, driven by MongoDB FTE of 0.6-1.1 which maps to the TE=3 band, not TE=2 (SL1c_phase3_consolidated.md, Section 1.3). A conditional adjustment on DS5 (Message Queuing) TE 2->3 applies if RabbitMQ is the primary broker (SL1c_phase3_consolidated.md, Section 2.1).

**Assessment for the executive narrative:** Finding 3 remains valid — P3 is indeed the best-calibrated plane — but the executive summary should acknowledge the FTE aggregate correction. The narrative implication shifts slightly: P3 ongoing cost is 11.85-19.55 FTE, not "~10-18 FTE," a roughly 10% upward revision at both bounds. This does not change the strategic conclusion but does affect budgeting precision.

---

### 1.4 Finding 4: "P4 (AI Model Plane) is nearly eliminated"

**Original text:** "All-phase average of RD 1.3 / TE 1.7. The ISV's AI-related effort is in P2 (agent orchestration) and P3 (embedding/RAG pipelines), not P4."

**Verdict: PARTIALLY SUPPORTED. The core claim is correct for the rated subsegments, but the scope exclusion masks four categories of unrated residual ISV obligations.**

The S2-S5 scope exclusion is structurally sound for primary infrastructure operations, correctly transferring 5.50-10.50 FTE of on-premises work to the customer (RP4b_P4_scope_exclusion.md, Section 1.5). The ISV P4 Phase 3 FTE after the split is ~0.45-1.45 FTE, compared to 2.60-4.80 FTE without the split — a reduction to approximately 17-30% of the original (SL1c_phase3_consolidated.md, Section 1.4).

However, RP4b identifies four categories of residual ISV obligation that the current ratings do not capture:

1. **Hardware compatibility matrix authorship (Phase 1).** The ISV must produce and maintain minimum GPU generation, VRAM floor, CUDA version, and inference engine version specifications. Estimated at 2-4 person-weeks initial, 1-2 person-days per major release recurring (RP4b_P4_scope_exclusion.md, Section 5.2, Category 1).

2. **Inference engine version compatibility testing (Phase 1 + Phase 3).** The ISV must test API integration against the range of vLLM, TGI, and Dynamo-Triton versions the customer population deploys. Estimated at 1-3 person-weeks per major vLLM release cycle (RP4b_P4_scope_exclusion.md, Section 5.2, Category 3).

3. **Customer GPU allocation triage support (Phase 3).** The ISV bears the support cost of diagnosing GPU resource insufficiency when customers report degraded TTFT or throughput. Estimated at 0.05-0.10 FTE per customer annually (RP4b_P4_scope_exclusion.md, Section 5.2, Category 2).

4. **Per-customer troubleshooting runbooks (Phase 2 + Phase 3).** The ISV must deliver GPU-layer diagnostic guides to each customer's IT team. Estimated at 1-3 person-days per customer onboarding (RP4b_P4_scope_exclusion.md, Section 5.2, Category 4).

Additionally, RP4b documents a quantified performance failure mode that the scope exclusion does not assign to any owner: an 82% throughput degradation from AWQ quantization on pre-A100 hardware, where the ISV selects the quantization method (S2-adjacent) and the customer selects the GPU (S3), and neither party owns the combined failure (RP4b_P4_scope_exclusion.md, Key Findings, third bullet).

The S1 Phase 1 RD should also increase from 1 to 2, per the SL1a consolidated finding that authentication re-implementation, Bedrock schema delta, and error handling rewrite are non-trivial engineering work (SL1a_phase1_consolidated.md, Section 2).

**Assessment for the executive narrative:** "Nearly eliminated" is an overstatement. A more accurate framing is "P4 primary infrastructure obligations are transferred to the customer, but the ISV retains non-trivial cross-boundary responsibilities." The current language risks misleading executives into believing the ISV has near-zero AI infrastructure exposure, when in fact the ISV owns the support triage burden for every GPU-related performance incident that surfaces at the application layer (where 60% of production AI inference incidents originate per RP4b's arXiv citation — RP4b_P4_scope_exclusion.md, Section 2.3). The finding should be reframed as a risk transfer, not a risk elimination.

---

### 1.5 Finding 5: "Phase 2 (per-customer customization) is dominated by P1"

**Original text:** "The application code (P2) and data services (P3) are largely standardized across customers. Infrastructure configuration (P1) is what varies — and it's what makes each new customer deployment expensive."

**Verdict: SUPPORTED with aggregate effort revision for non-standard customers.**

All 38 Phase 2 cell ratings were confirmed ACCURATE or HOLD — no individual Phase 2 subsegment requires a numerical rating change (SL1b_phase2_consolidated.md, Key Finding 1). P1 at avg RD 3.0 / TE 2.9 versus P2 at avg RD 1.1 / TE 1.2 confirms the dominance claim (SL1b_phase2_consolidated.md, Section 3).

However, the aggregate Phase 2 effort estimate requires upward revision for non-standard customer profiles. The stated 10-21 person-weeks per customer is valid for mature ISVs deploying to connected, commercially regulated customers with standard hardware. For air-gapped customers, P1 rises to 9-18 person-weeks (vs. stated 6-14), and for hardware-heterogeneous customers, P3 rises to 3-6 person-weeks (vs. stated 2-4). The realistic range for non-standard customers is 14-27 person-weeks per customer (SL1b_phase2_consolidated.md, Key Finding 2).

The finding correctly identifies that the first 3-4 customer deployments will exceed even the revised ranges before automation maturity is established — a finding corroborated by Replicated's 90-day-to-8-hour improvement trajectory and Connsulting's 6-month initial deployment cycle (SL1b_phase2_consolidated.md, Section 4.2).

**Assessment for the executive narrative:** Finding 5 is sound. The revision should acknowledge the customer-segment variance in Phase 2 effort, since the 10-21 person-week range is defensible only for the median-case customer. The executive audience is likely to encounter air-gapped and regulated customers disproportionately (these are the customers most likely to require on-premises deployment in the first place), making the 14-27 person-week range the more relevant planning figure.

---

### 1.6 Finding 6: "Phase 3 (ongoing support) has two distinct cost types"

**Original text:** Lists "Linear with N customers" subsegments (CP-01, CP-02, CP-04, CP-07, DS1, DS6) and "Fixed/shared" subsegments (AL02, AL05, AL09, DS10).

**Verdict: SUPPORTED. The linear/fixed taxonomy is validated by scaling classifications in the ground truth data.**

The Phase 3 consolidated review confirms that CP-01, CP-02, CP-07 are "Yes" scaling (fully linear with N), and CP-04, CP-05, CP-09, CP-10 are "Yes" or "Partial" scaling (SL1c_phase3_consolidated.md, Section 1.1; three_phase_on_prem_ratings.md, Section 6). The fixed-cost subsegments (AL02 at 3.0-6.0 FTE, DS10 at 3.25-4.75 FTE) are confirmed as not scaling with customer count (SL1c_phase3_consolidated.md, Section 1.2, Section 1.3).

The finding could be strengthened by noting the total FTE breakdown: linear-with-N costs are concentrated in P1 (20-38 FTE) and scale-sensitive portions of P3 (DS1, DS6), while fixed costs are concentrated in P2 (18.6-35.6 FTE) and scale-insensitive portions of P3. This creates an asymmetric cost curve: the marginal cost of each additional customer is driven by P1, while the fixed cost floor is driven by P2.

**Assessment for the executive narrative:** Finding 6 is valid and strategically important. The improvement would be to make the FTE magnitude explicit: the fixed cost floor is approximately 19-36 FTE (P2) and cannot be reduced by adding fewer customers, while the variable cost is approximately 20-38 FTE (P1) at the current assumed customer count. An ISV with 5 customers and an ISV with 50 customers face the same P2 cost; the P1 cost is what separates them.

---

## 2. The "P1 Dominates" Finding After Rating Adjustments

The P1 dominance claim is not merely sustained after review — it is strengthened. The cumulative evidence:

**Phase 1:** No P1 adjustments. All 10 subsegments confirmed ACCURATE. P1 averages RD 4.4 / TE 4.0 are the highest of any plane (SL1a_phase1_consolidated.md, Section 1.1). The 80-person-month upper bound is the defensible planning figure (SL1a_phase1_consolidated.md, Key Finding 2).

**Phase 2:** No P1 adjustments. All 10 confirmed HOLD. P1 at avg RD 3.0 / TE 2.9 remains the dominant plane at ~60% of per-customer effort (SL1b_phase2_consolidated.md, Key Finding 3).

**Phase 3:** Four P1 TE ratings adjusted upward: CP-03 TE 4->5, CP-06 TE 3->4, CP-08 TE 3->4, CP-10 TE 4->5 (SL1c_phase3_consolidated.md, Section 2.1). After adjustment, P1 Phase 3 avg TE rises from 4.1 to 4.5. This widens the gap between P1 and the next-highest plane:

| Plane | Current Phase 3 TE | Proposed Phase 3 TE | Gap to P1 |
|---|:---:|:---:|:---:|
| P1 Control Plane | 4.1 | **4.5** | -- |
| P2 Application Logic | 2.7 | 2.8 | 1.7 |
| P3 Data Plane | 2.9 | 3.0 | 1.5 |
| P4 AI Model Plane | 1.8 | 1.8 | 2.7 |

(Source: SL1c_phase3_consolidated.md, Section 3, Grand Summary table)

The review's most significant meta-finding reinforces P1 dominance from a different angle: all corrections across all planes run in the same direction — upward. No rating in the entire 102-cell active matrix was found to be overstated. The systematic understatement is most concentrated in P1 Phase 3, where the 4 adjusted subsegments represent 40% of P1 Phase 3 cells (SL1c_phase3_consolidated.md, Key Finding 1). This creates a conservative bias in the source file that, when corrected, makes P1 dominance even more pronounced.

---

## 3. The "P2 Systematic Divergence" Finding After the RP2c Investigation

The RP2c investigation was specifically designed to stress-test whether the P2 divergence is real or a scale artifact. The investigation's conclusions are unambiguous:

**The divergence is real, not a scale artifact.** The TE scale accurately measures absolute work quantum. A tier-invariant subsegment (like AL02 Business Logic) correctly receives RD=1 (identical to cloud-native) and TE=4 (large absolute FTE). The divergence appears because the RD scale correctly awards low scores to tier-invariant work that is genuinely large. The scale is functioning as designed (RP2c_P2_divergence_investigation.md, Section 3).

**The divergence is systematic, not outlier-driven.** The residual average gap after removing AL02 is +0.67 across 9 cells. Six of 10 P2 Phase 3 subsegments independently show +1 gaps (RP2c_P2_divergence_investigation.md, Section 2). No P2 Phase 3 subsegment shows TE < RD.

**The divergence is unique to P2 (and at smaller scale, P4).** P1 and P3 contain no tier-invariant subsegments, so the structural mechanism that produces large-TE / low-RD cells does not exist in those planes (RP2c_P2_divergence_investigation.md, Section 4).

**Post-RP2c qualification:** The three recommended P2 Phase 3 adjustments (AL04 TE +1, AL05 RD +1, AL09 RD +1) slightly narrow the gap from +0.9 to +0.8, but do not eliminate it (SL1c_phase3_consolidated.md, Section 2.1). The AL05 RD adjustment raises the difficulty of one divergent subsegment, reducing its individual gap from +1 to 0, but the eight other positive-gap subsegments remain unchanged. The finding survives.

---

## 4. The "P4 Nearly Eliminated" Finding Against the RP4b Scope Exclusion Analysis

This is the finding that requires the most significant revision. The RP4b analysis reveals that the binary scope exclusion — customer owns S2-S5, ISV owns S1/S6/S7/S8 — accurately models primary infrastructure responsibility but masks a non-trivial cross-boundary interface.

**What the scope exclusion gets right (RP4b_P4_scope_exclusion.md, Section 5.1):**
- The 5.50-10.50 FTE transfer to the customer is accurately sized
- The ISV P4 Phase 3 FTE reduces to ~0.45-1.45 FTE for the rated subsegments
- S1 retention correctly captures ISV API integration; S6/S7 correctly capture routing and monitoring

**What the scope exclusion misses (RP4b_P4_scope_exclusion.md, Section 5.2):**
- 4 unrated residual ISV obligations (hardware compatibility matrix, inference engine version testing, GPU allocation triage, troubleshooting runbooks)
- An unassigned 82% throughput degradation failure mode from AWQ/GPU generation mismatch
- At-scale caveats: S6 and S7 Phase 3 FTE ranges (0.2-0.5 and 0.1-0.5 respectively) extend into TE=3 territory at N=50 customers (SL1c_phase3_consolidated.md, Section 1.4)

The RP4b investigation also surfaces an alternative commercial model — the Cloudera-style "ISV-managed inference appliance" where the ISV retains S2 — that is not modeled in the current framework but represents a viable deployment pattern for ISVs seeking unified support scope (RP4b_P4_scope_exclusion.md, Section 4.3). The Google Distributed Cloud model represents yet a third configuration where neither ISV nor customer manages S2-S5 (RP4b_P4_scope_exclusion.md, Section 4.4).

**Assessment:** "Nearly eliminated" is the claim in Section 8 that most needs revision. The rated P4 subsegments are indeed low-effort, but the cross-boundary support burden, the unrated compatibility testing obligation, and the at-scale TE=3 territory for S6/S7 collectively mean that P4 is "structurally reduced" rather than "nearly eliminated." For an executive audience, the distinction matters: "nearly eliminated" implies the ISV can safely ignore P4 in staffing models, while "structurally reduced with residual obligations" implies a smaller but non-zero staffing requirement that scales with customer count and GPU heterogeneity.

---

## 5. Storytelling Arc Assessment

### 5.1 Current Arc Structure

The current Section 8 follows a descending-impact arc:
1. P1 dominates (highest RD and TE) — the primary cost center
2. P2 diverges (TE exceeds RD) — the hidden planning trap
3. P3 calibrates (RD and TE align) — the well-estimated plane
4. P4 disappears (scope exclusion) — the non-issue
5. Phase 2 is P1-dominated — the per-customer cost story
6. Phase 3 has two cost types — the scaling economics

### 5.2 Arc Strengths

The arc is well-structured for an executive audience. It opens with the most consequential finding (P1 dominance), introduces the subtlest finding second (P2 planning trap), confirms a baseline expectation third (P3 calibration), and resolves the AI/GPU question fourth (P4 reduction). Findings 5 and 6 provide operational specificity that connects the ratings to staffing and budgeting decisions.

The progression from "what is hardest" (Finding 1) to "what is deceptively easy" (Finding 2) to "what is accurately estimated" (Finding 3) creates a credibility anchor: the reader sees that the framework can distinguish between planes where it trusts its own estimates (P3) and planes where the estimates contain structural surprises (P2). This differentiates the analysis from a generic "everything is hard" assessment.

### 5.3 Arc Weaknesses

**Weakness 1: The arc does not communicate the direction of error.** Every review correction runs upward. No rating was found to be overstated. This systematic conservative bias is the most important meta-finding for executives — it means the stated costs are floor estimates, not central estimates — but the current narrative does not surface this pattern. An executive reading the six findings would not learn that the analysis consistently underestimates rather than overestimates difficulty and effort.

**Weakness 2: Finding 4 creates false comfort on AI infrastructure.** The "nearly eliminated" language for P4 is the most dangerous claim for an executive audience, because it may lead to the conclusion that the ISV has zero AI infrastructure risk in on-premises deployments. In reality, 60% of production AI inference incidents originate at the inference engine layer (RP4b_P4_scope_exclusion.md, Section 2.3), and the ISV absorbs the support burden for every one of those incidents that surfaces at the application API boundary — even when the root cause is in customer-scope S2-S5. An executive who reads "P4 is nearly eliminated" may de-prioritize the ISV's need for AI infrastructure expertise.

**Weakness 3: The six absent risk categories are invisible.** The framework rates 38 subsegments but does not model talent acquisition difficulty, customer communication overhead, regulatory compliance cost variance, vendor lock-in migration cost, opportunity cost of on-prem specialization, or technical debt accumulation (SL1c_phase3_consolidated.md, Section 5.3). The talent acquisition gap is the most material: the Phase 3 FTE estimates answer "what does this cost if staffed?" but not "can it be staffed?" — a critical distinction when 40% of organizations lack K8s skills and the average hiring cycle for platform engineers exceeds 5 months (SL1c_phase3_consolidated.md, Section 5.3, citing Spectro Cloud 2025 and Linux Foundation 2024).

**Weakness 4: The P3 FTE aggregate error undermines precision claims.** The stated "~10-18 FTE" for P3 Phase 3 should be 11.85-19.55 FTE (SL1c_phase3_consolidated.md, Section 4.1). While the magnitude of the error (~10% at both bounds) is not strategically decisive, it is the only material arithmetic error in the document and undermines the reader's confidence in other aggregate figures.

**Weakness 5: Phase 3 TE understatement is not acknowledged.** The systematic cross-plane finding — that Phase 3 TE is understated in P1, P2, and P3 — is the strongest pattern in the entire review (8 of 8 recommended rating adjustments across all planes are +1 TE or RD increases; SL1c_phase3_consolidated.md, Section 2.1). The current narrative does not tell the reader that Phase 3 costs are systematically understated.

### 5.4 Technical Defensibility Assessment

The narrative is defensible for a technical audience with three exceptions:

1. **The [D] flag misapplication.** Three of four [D] flags are applied below the stated threshold (gap = +1 where threshold = 2). Only AL02 Phase 3 (gap = +3) correctly qualifies (CC2_divergence_rederivation.md, Section 6). A technical reviewer will immediately spot this inconsistency. The underlying divergence narratives are analytically correct — effort does exceed difficulty in all flagged cells — but the formal threshold is not met.

2. **The P3 FTE aggregate.** A technical reviewer who sums the individual subsegment FTEs will arrive at 11.85-19.55, not "~10-18" (SL1c_phase3_consolidated.md, Section 4.1). This is the kind of error that erodes trust.

3. **The "50% underestimation" claim for P2.** The claim conflates two different metrics: the RD-TE gap within the ratings framework and the budget allocation error a planner would make. The 50% figure is directionally correct but its derivation (comparing RD-based cost weight allocation to FTE-based cost weight) is not explicit in Section 8 (RP2c_P2_divergence_investigation.md, Section 6). A rigorous technical reader will want the derivation shown.

---

## 6. Proposed Revisions to Key Findings

### Revised Finding 1

**Current:** "P1 (Control Plane) dominates both dimensions across all three phases. It is the hardest AND the most effort-intensive in Phase 1, Phase 2, and Phase 3. This is the core of the ISV's on-prem resistance."

**Proposed:** "P1 (Control Plane) dominates both dimensions across all three phases, and this dominance is understated in the original ratings. After review, four P1 Phase 3 TE ratings require upward adjustment (CP-03, CP-06, CP-08, CP-10), raising the P1 Phase 3 average TE from 4.1 to 4.5. P1 represents the highest difficulty and the highest effort in every phase. It is the primary source of on-premises resistance and the primary determinant of whether on-premises deployment is economically viable."

**Rationale:** Incorporates the review's most significant P1 finding (4 TE understatements) and connects the rating to the business decision. Sources: SL1a_phase1_consolidated.md Key Finding 2; SL1c_phase3_consolidated.md Section 2.1.

### Revised Finding 2

**Current:** "P2 (Application Logic) is the largest systematic divergence. Average RD of 1.6 vs average TE of 2.1... An ISV that plans based only on relative difficulty will underestimate P2 ongoing costs by ~50%."

**Proposed:** "P2 (Application Logic) exhibits systematic divergence between difficulty and effort: average RD 1.6 versus average TE 2.1 across all phases, widening to RD 1.8 versus TE 2.7 in Phase 3 (arithmetically verified: sum of gaps = +9 across 10 cells). This divergence is structural, not outlier-driven — removing the largest outlier (AL02, gap = +3) leaves a residual average gap of +0.67 across 9 cells. The mechanism is that P2 contains tier-invariant subsegments (AL02, AL04, AL07) whose absolute effort is set by application size, not deployment tier. The planning risk is not that P2 is secretly difficult; it is that P2 represents 18.6-35.6 FTE of ongoing product development and maintenance that cost models focused on deployment-tier difficulty will exclude."

**Rationale:** Replaces the vague "50%" figure with the specific FTE range. Sharpens the "planning trap" framing per RP2c's qualification: the trap conceals large routine work, not difficult work. Sources: CC2_divergence_rederivation.md Section 7; RP2c_P2_divergence_investigation.md Sections 2, 6.

### Revised Finding 3

**Current:** "P3 (Data Plane) is accurately calibrated. Difficulty and effort align closely across all three phases."

**Proposed:** "P3 (Data Plane) is the best-calibrated plane: difficulty and effort align closely across all three phases (all-phase avg gap = -0.2). However, the P3 Phase 3 FTE aggregate requires correction from '~10-18 FTE' to 11.85-19.55 FTE — the individual subsegment FTEs are correct, but the summary understates their sum. Additionally, DS2 (NoSQL) Phase 3 TE should increase from 2 to 3 based on MongoDB operational FTE of 0.6-1.1."

**Rationale:** Preserves the calibration claim while disclosing the arithmetic correction. Sources: SL1c_phase3_consolidated.md Section 4.1; CC2_divergence_rederivation.md Section 4.

### Revised Finding 4

**Current:** "P4 (AI Model Plane) is nearly eliminated under the customer-provides-GPU-and-models scope."

**Proposed:** "P4 (AI Model Plane) primary infrastructure obligations are transferred to the customer under the customer-provides-GPU scope split, reducing ISV P4 FTE from 5.50-10.50 to approximately 0.45-1.45. However, the scope exclusion masks four categories of residual ISV obligation: hardware compatibility matrix authorship, inference engine version compatibility testing, customer GPU allocation triage, and troubleshooting runbook delivery. These are currently unrated and uncosted. At N=50 customers with GPU heterogeneity, S6 and S7 FTE ranges extend into TE=3 territory. The characterization 'nearly eliminated' should be read as 'structurally reduced with residual cross-boundary obligations' — the ISV cannot fully divest AI infrastructure expertise."

**Rationale:** Incorporates RP4b's four unrated obligations and at-scale caveats. Reframes from "risk elimination" to "risk transfer with residual exposure." Sources: RP4b_P4_scope_exclusion.md Sections 5.1-5.2; SL1c_phase3_consolidated.md Section 1.4.

### New Finding 5 (replaces current Finding 5)

**Current:** "Phase 2 (per-customer customization) is dominated by P1."

**Proposed:** "Phase 2 per-customer effort is dominated by P1 infrastructure adaptation (~60% of total), and this dominance is structurally correct: hardware, network, and security environments are categorically unique per customer site. All 38 Phase 2 cell ratings are confirmed accurate. However, the stated 10-21 person-weeks per customer understates effort for the customer segments most likely to require on-premises deployment: air-gapped customers (revised to 14-27 pw) and regulated-industry customers with HSMs, formal change management boards, and SIEM integration (individual P1 subsegments may each add +1 TE). The first 3-4 customer deployments will exceed even revised ranges before deployment automation reaches maturity."

**Rationale:** Connects the customer segments most likely to need on-premises with the effort ranges that apply to them. Sources: SL1b_phase2_consolidated.md Key Findings 1-3; SL1b_phase2_consolidated.md Section 4.2.

### New Finding 6 (replaces current Finding 6)

**Current:** Lists linear vs. fixed cost subsegments.

**Proposed:** "Phase 3 ongoing costs comprise two structurally distinct cost pools: (a) Linear-with-N costs concentrated in P1 Control Plane (CP-01, CP-02, CP-04, CP-07) and P3 Data Plane (DS1, DS6) — these scale directly with customer count and make each additional customer incrementally expensive; and (b) Fixed/shared costs concentrated in P2 Application Logic (AL02, AL05, AL09) and P3 (DS10) — these represent product development and AI ecosystem maintenance that exist regardless of customer count. The fixed pool (P2: 18.6-35.6 FTE) is comparable in magnitude to the variable pool (P1: 20-38 FTE), creating a cost floor that cannot be reduced by serving fewer customers."

**Rationale:** Makes the FTE magnitudes explicit and connects the cost structure to business decisions. Sources: three_phase_on_prem_ratings.md Section 6, Phase 3 Summary table; SL1c_phase3_consolidated.md Section 3.

### New Finding 7 (addition)

**Proposed:** "All review corrections run in the same direction: upward. Of 8 recommended Phase 3 rating adjustments, all are +1 increases. Of 1 recommended Phase 1 adjustment, it is +1. No rating in the 102-cell active matrix was found to be overstated. Additionally, six structural risk categories — talent acquisition, customer communication overhead, regulatory compliance cost, vendor lock-in migration cost, opportunity cost of on-premises specialization, and technical debt accumulation — are absent from the framework entirely. The stated FTE figures should be read as floor estimates for a fully-staffed ISV with established on-premises delivery capability, not central estimates for a typical ISV entering on-premises deployment."

**Rationale:** This is the most consequential meta-finding for executives. The systematic direction of all corrections, combined with the absent risk categories, means the stated costs are lower bounds. Sources: SL1c_phase3_consolidated.md Key Findings 1, 5; SL1a_phase1_consolidated.md Section 2.

---

## 7. Draft Improved Executive Summary Section

The following is a proposed replacement for Section 8 (Grand Summary / Key Findings) in the ratings file. It retains the existing summary matrices and adds a revised key findings section.

---

### Key Findings (Revised)

**On the direction of error.** Every adjustment identified through multi-wave independent review runs upward. No rating in the 102-cell active matrix was found to be overstated. Eight Phase 3 ratings require +1 increases (4 in P1, 2 in P2, 1 in P3, plus 1 conditional), and one Phase 1 rating requires a +1 increase (P4 S1 RD). The stated effort figures are floor estimates for a fully-staffed ISV with established on-premises delivery capability. Six structural cost categories — talent acquisition (5.4-month average hiring cycles for platform engineers), customer communication overhead, regulatory compliance cost, vendor lock-in reversal cost, opportunity cost of on-premises specialization, and technical debt accumulation — are absent from the framework and would add to the actual cost in practice.

**1. P1 (Control Plane) dominates all three phases, and its Phase 3 cost is understated.** P1 carries the highest difficulty and effort ratings across Phase 1 (RD 4.4 / TE 4.0), Phase 2 (RD 3.0 / TE 2.9), and Phase 3 (RD 4.0 / TE 4.1, proposed 4.5 after review corrections). The 80-person-month upper bound for Phase 1 is the defensible planning figure; the 40-person-month lower bound requires conditions unlikely to co-occur. Four Phase 3 P1 subsegments (CP-03, CP-06, CP-08, CP-10) have TE ratings that do not reach their ground truth FTE ceilings and should be adjusted upward. P1 is the primary determinant of on-premises economic viability.

**2. P2 (Application Logic) creates a planning trap: large cost at low difficulty.** P2 Phase 3 averages RD 1.8 versus TE 2.7, a +0.9 gap that is arithmetically verified (sum of gaps = +9 across 10 cells) and structurally driven by tier-invariant subsegments whose absolute effort is set by application size, not deployment tier. Removing the dominant outlier (AL02, gap = +3) still leaves a +0.67 residual gap across 9 cells. P2 Phase 3 represents 18.6-35.6 FTE of ongoing product development and maintenance — comparable in magnitude to P1's 20-38 FTE — that cost models focused on deployment difficulty will exclude. The risk is not that P2 is secretly difficult; it is that P2 costs are invisible to planners who screen on difficulty alone.

**3. P3 (Data Plane) is the best-calibrated plane, with one arithmetic correction required.** Difficulty and effort align closely across all three phases (all-phase avg gap = -0.2, no [D]-qualifying divergences). The P3 Phase 3 FTE aggregate should be corrected from "~10-18 FTE" to 11.85-19.55 FTE (individual subsegment FTEs are accurate; only the summary is understated). DS2 (NoSQL) Phase 3 TE should increase from 2 to 3.

**4. P4 (AI Model Plane) is structurally reduced but not eliminated.** The customer-provides-GPU scope split correctly transfers 5.50-10.50 FTE of primary infrastructure operations to the customer, reducing ISV P4 FTE to approximately 0.45-1.45. However, four categories of residual ISV obligation are unrated: hardware compatibility matrix authorship, inference engine version testing, customer GPU allocation triage, and troubleshooting runbook delivery. The ISV bears the support burden for 60% of production AI inference incidents that originate at the inference engine layer (customer scope) but surface at the application API boundary (ISV scope). At N=50 customers with GPU heterogeneity, S6 and S7 extend into TE=3 territory. The ISV cannot fully divest AI infrastructure expertise.

**5. Phase 2 per-customer effort is P1-dominated and understated for regulated/air-gapped customers.** The stated 10-21 person-weeks per customer is valid for the median case. For air-gapped and regulated-industry customers — the segments most likely to require on-premises deployment — the realistic range is 14-27 person-weeks. All 38 Phase 2 cell ratings are confirmed accurate; the understatement is in the aggregate, not the individual ratings. The first 3-4 customer deployments will exceed even revised ranges before automation maturity is established.

**6. Phase 3 costs comprise two structurally distinct pools.** Linear-with-N costs (P1: 20-38 FTE; P3 scale-sensitive: DS1, DS6) make each additional customer incrementally expensive. Fixed costs (P2: 18.6-35.6 FTE; P3 fixed: DS10 at 3.25-4.75 FTE) represent product development and AI ecosystem maintenance that cannot be reduced by serving fewer customers. The fixed pool is comparable in magnitude to the variable pool, creating a cost floor that makes on-premises deployment economically challenging below a threshold customer count.

**7. The analysis systematically understates Phase 3 costs.** Cross-plane, the Phase 3 TE ratings exhibit conservative bias: 8 of 8 recommended adjustments are +1 increases (no overstated ratings found), the P3 FTE aggregate is understated by ~2 FTE at both bounds, and 3 of 4 [D] divergence flags are misapplied below the stated threshold. The corrected Phase 3 grand total is approximately 51-95 FTE (revised from ~49-93). With the six absent structural risk categories factored qualitatively, the true ongoing cost of on-premises deployment is likely 15-25% above the stated range for a typical mid-size ISV.

---

## 8. Confidence and Limitations

This assessment is based on the consolidated findings of three synthesis layers (SL1a, SL1b, SL1c), three spot-check investigations (RP2c, RP4b, CC2), and the underlying review agent reports they cite. The assessment does not re-derive any individual ratings and is bounded by the evidence those review agents documented.

**Highest-confidence assessments:**
- P1 dominance (Finding 1): confirmed by all review agents across all phases
- P2 systematic divergence (Finding 2): arithmetically verified by CC2 and structurally validated by RP2c
- P3 FTE correction: independently identified by RP3d and confirmed by CC1

**Lower-confidence assessments:**
- P4 residual obligation sizing (Finding 4): RP4b's FTE estimates for unrated obligations are marked [UNVERIFIED] in the source
- Phase 3 "15-25% above stated" (Finding 7): qualitative extrapolation from absent risk categories, not derived from quantified data
- Air-gapped customer effort multiplier: based on Replicated data (60x time-to-install) with limited independent corroboration

---

## Sources

### Primary Input Files

| Source | Absolute Path | Sections Referenced |
|---|---|---|
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` | Section 8 (Key Findings); Section 6 (Phase 3 tables); Section 7 (Divergence Analysis) |
| SL1a_phase1_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1a_phase1_consolidated.md` | All sections: Phase 1 rating accuracy, effort estimates, interview questions, key findings |
| SL1b_phase2_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1b_phase2_consolidated.md` | All sections: Phase 2 rating accuracy, aggregate effort revision, key findings |
| SL1c_phase3_consolidated.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/SL1c_phase3_consolidated.md` | All sections: Phase 3 rating adjustments, FTE corrections, structural gaps, key findings |

### Spot-Check Investigation Files

| Source | Absolute Path | Sections Referenced |
|---|---|---|
| RP2c_P2_divergence_investigation.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2c_P2_divergence_investigation.md` | Sections 1-6: All-phase gap calculations, outlier analysis, scale bias assessment, cross-plane comparison, planning trap framing |
| RP4b_P4_scope_exclusion.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4b_P4_scope_exclusion.md` | Sections 1-6: S2-S5 FTE data, residual ISV obligations, edge cases, support gap analysis |
| CC2_divergence_rederivation.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC2_divergence_rederivation.md` | Sections 1-9: Complete 102-cell gap calculation, [D] flag audit, +0.9 verification, near-miss inventory |

### Underlying Review Agent Files (cited through SL1a/SL1b/SL1c)

| Source | Key Contribution |
|---|---|
| RP1a, RP1b, RP1c | P1 subsegment-level Phase 1-3 verdicts |
| RP1d | P1 Phase 2 deep dive; air-gapped deployment data |
| RP1e | Phase 1 effort plausibility; parallelization factor analysis |
| RP2a, RP2b | P2 subsegment-level Phase 1-3 verdicts |
| RP3a, RP3b, RP3c, RP3d | P3 subsegment-level verdicts; FTE aggregate error; scaling audit |
| RP4a | P4 ISV-scope subsegment verdicts; S1 RD adjustment |
| CC1 | Arithmetic verification across all phases |
| CC3 | Cross-phase trajectory consistency |
| CC5 | Six structurally absent risk categories |
| GT1, GT2, GT3, GT4, GT5 | Ground truth extractions for all four planes |
