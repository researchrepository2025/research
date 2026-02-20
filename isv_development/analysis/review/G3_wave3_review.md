# G3 Wave 3 Review: P2 Application Logic (RP2a-RP2e)

**Reviewer:** Quality Review Agent
**Date:** 2026-02-19
**Scope:** Five Wave 3 output files covering P2 Application Logic (AL01-AL10)
**Ground Truth:** GT2_P2_ground_truth.md

---

## File Reviews

---

### RP2a: P2 Service Architecture (AL01-AL05)

- **Score:** PASS
- **Citation integrity:** Strong. Every factual claim carries an inline citation with source attribution and URL. Citations are consistently formatted as `[FACT]` or `[STATISTIC]` tags with attribution lines. External URLs are present for all external claims (softwareseni.com, markaicode.com, gravitee.io, konghq.com, arxiv.org, CNCF, etc.). GT2 is cited as the primary internal ground truth source throughout. The AL02 internal discrepancy between F75 (3/5) and P2 summary matrix (2/5) is transparently documented rather than papered over.
- **Scope discipline:** Excellent. Strictly limited to AL01-AL05 across all three phases. No drift into AL06-AL10 territory. No reclassification of P1 or P3 scope items. The file correctly identifies the AL03 P1/P2 boundary tension (1.5-3.0 FTE spanning infrastructure and application-layer work) but does not attempt to resolve it beyond noting it as an interview question.
- **Analysis/rating quality:** High. All 30 ratings (5 subsegments x 3 phases x 2 dimensions) are individually assessed with GT2 evidence. Two adjustment recommendations are made (AL04 Phase 3 TE: 2 to 3; AL05 Phase 3 RD: 2 to 3), both with specific evidence chains. The AL05 RD adjustment is particularly well-argued, citing Temporal config drift, application-layer DLQ ownership, and the 2.0-4.1 FTE ops burden from GT2. Confidence levels are appropriately differentiated (High for straightforward cases, Medium for boundary cases). The Phase 3 FTE validation table at the end confirms all five FTE ranges match GT2 exactly, providing a structural integrity check.
- **Content depth:** The AL05 analysis is the deepest in the file and appropriately so given it has the second-largest tier delta (Delta=3). The AL02 tier-invariance investigation is thorough, correctly identifying the startup-sequence adaptation as a genuine but bounded code delta. Interview questions are specific and actionable.
- **Issues found:** None material. One minor formatting note: the AL03 Phase 3 verdict text is somewhat long and could be tighter, but this is a style preference, not a quality issue.
- **Fix recommendations:** None required.

---

### RP2b: P2 Resilience, AI & Testing (AL06-AL10)

- **Score:** PASS
- **Citation integrity:** Strong. Systematic use of `[FACT]` and `[STATISTIC]` tags with URLs for external claims (Growin blog, vCluster, Atmosly, GitHub releases, LangGraph issues, Replicated, Gartner, Langfuse, OTel specs). Internal GT2 and GT5 citations are consistently sourced with section references. The AL09 analysis cites the LangGraph GitHub release page directly and documents a specific breaking change (langgraph-prebuilt 1.0.2 Issue #6363) as independent verification of ecosystem volatility.
- **Scope discipline:** Excellent. Strictly limited to AL06-AL10 across all three phases. No overlap with RP2a's AL01-AL05 territory. The file correctly defers multi-stack upgrade coordination boundary questions (AL09 vs. CP-07) rather than resolving them outside scope.
- **Analysis/rating quality:** High. 28 of 30 ratings confirmed accurate. The single adjustment recommendation (AL09 Phase 3 RD: 3 to 4) is the most consequential finding in Wave 3. It is well-supported: AL09 is ranked #1 hardest on-premises subsegment across all 38 subsegments (GT5, S1 Rank 1), has an absolute OP difficulty of 5/5, and requires coordinating six independent software stack upgrades across N customer environments. The argument that RD=3 ("moderate") understates a subsegment rated 5/5 absolute difficulty is logically sound. The AL07 Phase 2 analysis correctly identifies the scope boundary between application-layer isolation and platform-layer performance isolation, awarding ACCURATE with a clearly stated caveat. The AL10 linear scaling analysis is nuanced, distinguishing between linear validation coverage and potentially sub-linear FTE scaling depending on automation maturity.
- **Content depth:** The AL09 Phase 3 analysis is the standout section, with independent external research (LangGraph release cadence, prebuilt breaking change documentation) going beyond GT2. The "Validation of the Rapidly Evolving Ecosystem Claim" section is a dedicated verification exercise that adds independent evidentiary weight. The summary scorecard table provides a clear at-a-glance view of all 30 ratings.
- **Issues found:** None material. The AL07 Phase 2 confidence level is rated "Medium" with a scope caveat that is somewhat speculative (per-tenant SLOs at the application layer bleeding into hardware-dependent code). This is properly flagged as a caveat, not treated as a finding.
- **Fix recommendations:** None required.

---

### RP2c: P2 Systematic Divergence Investigation

- **Score:** PASS
- **Citation integrity:** Strong. All RD-TE gap calculations cite the specific sections of three_phase_on_prem_ratings.md. Cross-plane comparisons cite GT1, GT2, GT3, and GT5 ground truth files with section references. External sources include a diverse set: Google SRE ratio (zeet.co), software effort estimation research (Wikipedia citing Jorgensen et al.), testing effort underestimation (forecast.app), Last 10% Trap (DevIQ), on-premises TCO personnel costs (michaelskenny.com), and cloud TCO statistics (datastackhub.com). Each external claim is attributed with URL.
- **Scope discipline:** Excellent. The file explicitly declares its scope boundary on line 4: "Individual subsegment ratings not re-derived per scope boundary." It consistently adheres to this, analyzing the divergence pattern without attempting to re-rate any individual cell (which is RP2a/RP2b's responsibility). The cross-plane comparison (P1, P2, P3, P4) is analytically necessary to establish that P2's divergence is structurally distinct, not a scale defect.
- **Analysis/rating quality:** Excellent. This is the most analytically rigorous file in the Wave 3 set. The methodology is clear: independently calculate all RD-TE gaps, test whether the pattern is outlier-driven or systematic (by removing AL02 and observing the gap drops from +0.9 to +0.7 but persists), compare cross-plane to determine structural vs. artifactual divergence, and verify the TE scale is not biased. The finding that P1 (gap -0.1) and P3 (gap -0.2) show near-zero divergence while P2 (+0.5) and P4 (+0.4) show persistent positive divergence is the key structural insight. The explanation that tier-invariant subsegments in P2 (AL02, AL04, AL07) carry large absolute FTE at low RD by design is convincing and well-supported.
- **Content depth:** The "planning trap" qualification is the most original analytical contribution: "The trap does not hide difficult work. It hides large but routine work." This reframing is more precise than the ratings file's original framing and adds genuine strategic insight. The 50% underestimation calculation (15% budget allocation via RD vs. 38% actual FTE share) is concrete and actionable.
- **Issues found:** One minor issue: the file states the Divergence Flag definition as "RD and TE differ by 2+ points" and then notes AL10 Phase 1 is flagged with [D] despite only a +1 gap. This is an accurate observation about the ratings file's own application of its flagging rule, not an error in RP2c. The observation is correctly framed as an inconsistency in the ratings file.
- **Fix recommendations:** None required.

---

### RP2d: P1/P2 Boundary Analysis

- **Score:** PASS
- **Citation integrity:** Strong. The three boundary criteria (organizational owner, change driver, failure mode) are extracted with direct quotes from P1_control_plane.md and P2_application_logic.md. Each subsegment evaluation systematically applies all three criteria with supporting citations. GT1 and GT2 are cited for detailed subsegment characteristics. External URLs are present where relevant (CNCF reports, Kubernetes blog, Kong benchmarks, AWS App Mesh deprecation).
- **Scope discipline:** Excellent. The file explicitly limits scope to "P1 Control Plane (CP-01 through CP-10) and P2 Application Logic (AL01 through AL10) boundary only. P3 and P4 boundaries are explicitly out of scope." It examines exactly the four subsegments listed in its assignment (CP-06, AL08/CP-05, AL03, CP-03) and does not stray.
- **Analysis/rating quality:** Excellent. The three-criteria framework provides a systematic, reproducible methodology. Each of the four subsegments is evaluated against all three criteria with explicit verdicts. The finding that "No full reclassifications are warranted" is well-supported by the evidence. The two proposed scope clarifications (CP-06/AL10 pipeline artifact cross-reference; AL03 shared EOL trigger documentation) are practical and specific without overreaching. The CP-05/AL08 observability split is correctly identified as "the most precisely drawn boundary in the framework" with the complementary boundary statements from both source files.
- **Content depth:** The CP-06 evaluation is particularly thorough, addressing the common perception that CI/CD is "application delivery" rather than "control plane" and showing why the infrastructure-scoped definition satisfies P1 criteria. The AL03 analysis correctly identifies the mixed change driver set (product events + infrastructure EOL events) and explains why this does not violate the P2 classification because the work output is application-layer configuration. The risk analysis of what would happen if AL03 were moved to P1 (creating a boundary collision with CP-02) demonstrates analytical rigor.
- **Issues found:** None material.
- **Fix recommendations:** None required.

---

### RP2e: P2 Completeness

- **Score:** PASS
- **Citation integrity:** Strong. Industry-standard taxonomies are cited with URLs: AWS SaaS Lens (docs.aws.amazon.com), EnterpriseReady.io, Martin Fowler's Feature Toggles article, Stripe Engineering blog. Self-hosting evidence for Novu (docs.novu.co), SMTP deliverability (healthchecks.io blog), and notification architecture (Meerako) are all properly attributed. GT2 is cited for the "AL05 adjacent" status of Configuration/Feature Flags. The Statsig and FullScale feature flag references add practical depth.
- **Scope discipline:** Excellent. Strictly limited to P2 completeness analysis. The file does not attempt to re-rate existing subsegments (RP2a/RP2b's scope) or analyze divergence patterns (RP2c's scope). The boundary with P1 is respected: infrastructure for self-hosted notification backends is explicitly noted as P1/P3 scope.
- **Analysis/rating quality:** High. Three gap candidates are assessed with descending severity: Notification/Communication Services (absent -- genuine gap), Configuration Management/Feature Flags (embedded at insufficient granularity -- genuine gap), API Versioning/Backward Compatibility (diffuse but present -- labeling gap). The distinctions between absent, insufficiently granular, and unlabeled coverage are analytically precise. Four additional candidates (Billing, Audit Logging, Webhook Delivery, Tenant Onboarding) are assessed and correctly determined to be adequately covered. The proposed AL11 ratings are grounded in the self-hosting evidence (Novu requirements, SMTP operational burden, push notification cloud-only constraints).
- **Content depth:** The Martin Fowler feature toggle taxonomy (Release, Experiment, Ops, Permissioning) provides a compelling argument that feature flag management is a distinct engineering discipline, not a subset of AL05's async processing scope. The Novu self-hosting requirements (MongoDB + 2x Redis + S3 + significant compute) are a concrete illustration of on-premises tier impact. The framework impact assessment shows the proposed AL11 changes the aggregate complexity ratio only marginally (1.7x to 1.76x), correctly framing it as a coverage gap rather than a complexity driver.
- **Issues found:** One minor formatting issue: the FullScale URL at the bottom of the sources section is missing its closing parenthesis. This is a purely cosmetic issue.
- **Fix recommendations:** Fix the broken URL in the sources section (missing closing parenthesis on the FullScale link).

---

## Spot-Check Results

### Spot-Check 1: AL09 Difficulty Ratings and FTE Ranges

**Claim (RP2b):** "AL09: CN=2, MK8s=3, OP=5. FTE: CN 0.5-1.2, MK8s 2.0-4.0, OP 6.0-10.0 (stated), 4.0-7.0 (deduplicated). Tier-sensitive. Delta = 3 (largest in framework, tied with AL05)."

**GT2 verification:** GT2 records AL09 difficulty ratings as CN=2 (with a caveat that custom multi-provider pipelines can reach 4), MK8s=3, OP=5. FTE ranges are CN 0.5-1.2, MK8s 2.0-4.0, OP 6.0-10.0. Delta=3. The summary table in GT2 confirms these exact values.

**Ratings file verification:** three_phase_on_prem_ratings.md Phase 3 AL09 row shows RD=3, TE=4, FTE 4.0-7.0. The 4.0-7.0 figure represents the deduplicated net orchestration layer FTE.

**Result:** VERIFIED. All factual claims match GT2 exactly. The distinction between the stated 6.0-10.0 FTE and deduplicated 4.0-7.0 FTE is correctly documented.

---

### Spot-Check 2: AL05 Phase 3 FTE Composition

**Claim (RP2a):** "GT2 records the on-premises Phase 3 FTE as '0.75-1.5 (app code) + 2.0-4.1 (ops)' -- a combined 2.75-5.6 FTE."

**GT2 verification:** GT2 AL05 section records OP FTE Range as "0.75-1.5 (app code) + 2.0-4.1 (ops)." The Notable Caveats section states: "On-premises Kafka DLQ is application-layer only -- no native DLQ support. Total EDA operations FTE: 2.0-4.1 FTE active plus 0.85 FTE on-call."

**Ratings file verification:** three_phase_on_prem_ratings.md Phase 3 AL05 row shows RD=2, TE=3, FTE 2.75-5.6. This matches the sum of app code + ops from GT2.

**Result:** VERIFIED. The composite FTE (0.75-1.5 + 2.0-4.1 = 2.75-5.6) is correctly constructed. RP2a also correctly cites the external F33 figure of "2-4 FTE dedicated solely to EDA pattern operations vs. 0.1-0.6 FTE cloud-native" which is consistent with the 2.0-4.1 ops range.

---

### Spot-Check 3: AL02 Tier-Invariance at Difficulty 2/5

**Claim (RP2a):** "GT2 records AL02 difficulty as 2/5 across all three tiers (CN, MK8s, OP), classifying it as tier-invariant with Delta=0."

**GT2 verification:** GT2 AL02 section records CN=2, MK8s=2, OP=2. FTE ranges are 3.0-6.0 across all three tiers. Tier-invariant, Delta=0. GT2 also documents the internal discrepancy: F75 quotes "3/5 across all tiers" while the P2 summary matrix records 2/5, with GT2 treating the P2 section 4 summary matrix as authoritative.

**Ratings file verification:** three_phase_on_prem_ratings.md Phase 3 AL02 row shows RD=1, TE=4, FTE 3.0-6.0 with [D] flag and the note "relative difficulty is 1 because the work is identical on cloud-native."

**RP2c cross-verification:** RP2c independently calculates the AL02 Phase 3 gap as +3 (TE 4 minus RD 1) and identifies it as the widest divergence of any single cell in the entire 38-subsegment, 3-phase ratings file.

**Result:** VERIFIED. All three files (GT2, RP2a, RP2c) are consistent on the AL02 tier-invariance finding. The F75 discrepancy (3/5 vs. 2/5) is transparently documented in both GT2 and RP2a.

---

## Cross-File Consistency

### Do the 5 files tell a coherent story about P2 Application Logic accuracy?

Yes. The five files form a coherent and non-contradictory picture of P2:

1. **RP2a and RP2b** independently review all 60 ratings (10 subsegments x 3 phases x 2 dimensions). Of 60 total ratings, 55 are confirmed accurate, 3 have adjustment recommendations (AL04 Phase 3 TE, AL05 Phase 3 RD, AL09 Phase 3 RD), 1 has a medium-confidence accuracy with scope caveat (AL07 Phase 2), and 1 has a medium-confidence accuracy with data gap caveat (AL10 Phase 3). The adjustment recommendations are all upward by 1 point, indicating a modest systematic conservatism in the ratings file rather than any major calibration error.

2. **RP2c's divergence analysis aligns with RP2a/RP2b's individual findings.** RP2c identifies the Phase 3 RD-TE gap of +0.9 as systematic, not outlier-driven. RP2a independently confirms the largest outlier (AL02 Phase 3 gap +3) and validates it as structurally intentional. RP2b's AL09 adjustment recommendation (RD 3 to 4) would narrow the AL09 Phase 3 gap from +1 to 0, which is consistent with but does not contradict RP2c's finding that the systematic pattern persists even with adjustments.

3. **RP2d's boundary analysis does not raise issues that affect RP2a/RP2b's ratings.** RP2d confirms all examined subsegments are correctly classified. The two scope clarifications proposed (CP-06/AL10 pipeline artifact cross-reference, AL03 shared EOL triggers) are documentation improvements, not reclassifications that would change ratings.

4. **RP2e's completeness analysis identifies gaps that RP2a/RP2b could not have caught.** The three missing/underrepresented concerns (Notification Services, Configuration/Feature Flags, API Versioning) are genuinely outside the scope of individual subsegment rating reviews. RP2e correctly identifies these as coverage gaps in the framework itself, not rating accuracy issues within existing subsegments. RP2a's reference to the AL05 scope including "Vault configuration for secrets management" is consistent with RP2e's observation that feature flag management is "AL05 adjacent" but insufficiently granulated.

### Are there contradictions between files?

No material contradictions were found. One potential minor tension exists:

- RP2a recommends adjusting AL05 Phase 3 RD from 2 to 3. RP2c calculates the Phase 3 AL05 gap as +1 (TE 3 minus RD 2). If RP2a's adjustment is applied, the gap would become 0 (TE 3 minus RD 3). This does not contradict RP2c because RP2c explicitly does not re-rate individual subsegments and its systematic finding (8 of 10 subsegments show TE >= RD in Phase 3) would still hold with the adjustment.

### Cross-file reinforcement patterns:

- All three rating-review files (RP2a, RP2b, RP2c) independently validate the AL02 Phase 3 [D] flag as the most strategically significant divergence in P2.
- RP2b's AL09 Phase 3 RD adjustment recommendation (3 to 4) reinforces RP2c's finding that Phase 3 divergence is structural, not artifactual -- if the hardest subsegment in the framework (GT5 Rank 1) is under-rated on RD, the systematic TE > RD pattern has an identifiable cause beyond scale mechanics.
- RP2d's confirmation that the CP-05/AL08 boundary is clean supports RP2a's and RP2b's treatment of observability as correctly split between infrastructure (CP-05) and application instrumentation (AL08) without FTE leakage.
- RP2e's observation that feature flags are "AL05 adjacent" is consistent with RP2a's decision not to flag any AL05 scope concerns beyond the rating adjustment.

---

## Summary

- **Files passing:** 5 of 5
- **Files with minor issues:** 1 (RP2e -- broken URL in sources section, purely cosmetic)
- **Files needing rework:** 0

### Aggregate findings across all five files:

| Finding | Source File(s) | Severity |
|---|---|---|
| AL09 Phase 3 RD should be 4, not 3 | RP2b | Adjustment recommended |
| AL05 Phase 3 RD should be 3, not 2 | RP2a | Adjustment recommended |
| AL04 Phase 3 TE should be 3, not 2 | RP2a | Minor adjustment recommended |
| P2 RD-TE divergence (+0.5 all-phase average) is real, structural, and P2-specific | RP2c | Confirmed finding |
| All P1/P2 boundaries correctly drawn; no reclassifications needed | RP2d | No action required |
| Notification/Communication Services is a genuine gap (propose AL11) | RP2e | Framework enhancement recommended |
| Configuration/Feature Flags needs explicit subsegment or scope clarification | RP2e | Scope clarification recommended |
| API Versioning needs explicit scope notes in AL02 and AL03 | RP2e | Labeling clarification recommended |

### Cross-file consistency notes:

All five files are internally consistent, mutually non-contradictory, and form a coherent analytical picture. The three adjustment recommendations from RP2a/RP2b are all upward by exactly 1 point on the same dimension (Relative Difficulty or Total Effort), indicating the ratings file has a modest conservative bias on 3 of 60 ratings (5%). The remaining 57 ratings (95%) are confirmed accurate. The divergence analysis (RP2c), boundary analysis (RP2d), and completeness analysis (RP2e) each contribute distinct analytical dimensions that the individual rating reviews could not have surfaced, validating the multi-agent review design.
