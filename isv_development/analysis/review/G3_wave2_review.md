# G3: Wave 2 Quality Review — P1 Control Plane (RP1a through RP1e)

**Review Date:** 2026-02-19
**Reviewer:** Quality Gate 3
**Scope:** Five Wave 2 output files covering CP-01 through CP-10 across all three deployment phases and both rating dimensions
**Ground Truth Reference:** GT1_P1_ground_truth.md

---

## Per-File Assessments

---

### RP1a: P1 Infrastructure Core (CP-01, CP-02, CP-03)

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1a_P1_infrastructure_core.md`

- **Score:** PASS
- **Citation integrity:** Strong. Every factual claim references either GT1_P1_ground_truth.md with specific section identifiers or external URLs. External sources include authoritative references: kubernetes.io official blog for Ingress NGINX retirement, Portainer blog for SUSE Rancher pricing, Robust Perception (Prometheus maintainer) for memory sizing, Sirius Open Source for Keycloak TCO. URLs are properly formatted and appear functional. One minor note: the arXiv citation (https://arxiv.org/html/2407.01620v1) is used for a general claim about kubeadm requiring more effort, which is a reasonable but somewhat loose citation — the arXiv paper covers deployment options broadly, not effort quantification specifically.
- **Scope discipline:** Excellent. Stays within CP-01, CP-02, CP-03 across all three phases. No encroachment on CP-04 through CP-10. Cross-references to the ratings file and GT1 are appropriate. The Key Findings section does not stray beyond the three assigned subsegments.
- **Rating review quality:** Excellent. Each of the 18 ratings (3 subsegments x 3 phases x 2 dimensions) is individually re-derived with explicit reasoning chains from GT1 data. Confidence levels are justified: Phase 2 ratings consistently receive Medium confidence with a stated reason (no direct per-customer FTE data in GT1), while Phase 1 and Phase 3 ratings with GT1 FTE alignment receive High confidence. The CP-03 Phase 3 TE adjustment recommendation (potential +1 from TE 4 to TE 5) is the most substantive finding and is well-supported by the GT1 FTE range of 2.75-4.75 exceeding the TE 4 ceiling of 2.5. Interview questions are targeted and role-specific.
- **Content depth:** Strong. Goes beyond GT1 data with external Keycloak TCO ($199,200-$211,200 over 3 years), CNI comparison data (Calico vs Cilium operational tradeoffs), and service mesh adoption decline trajectory. The deduplication analysis for CP-03 Phase 3 FTE is an original analytical contribution that demonstrates understanding of the data structure, not just surface reading.
- **Issues found:** The CP-02 Phase 3 analysis notes that TE should be 5 for ISVs with service mesh, but the Key Findings (point 4) could more explicitly recommend whether the ratings file should add a conditional annotation or keep the modal rating. The recommendation is present but could be sharper.
- **Fix recommendations:** None required. Minor: consider adding an explicit recommendation for whether the ratings file should annotate the service mesh conditional or keep the modal rating.

---

### RP1b: P1 Security and Delivery (CP-04, CP-05, CP-06)

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1b_P1_security_delivery.md`

- **Score:** PASS
- **Citation integrity:** Strong. External sources are high-authority: HashiCorp Developer Documentation (Vault Raft reference architecture, FIPS 140-3 compliance), Let's Encrypt official announcement (45-day certificate validity), Robust Perception (Prometheus RAM sizing), CNCF End User Survey 2025 (ArgoCD 60% adoption), FluxCD official site (Deutsche Telekom case study). The review independently confirms the ArgoCD 60% statistic from both GT1 and the CNCF primary source. The Let's Encrypt timeline is precisely cited with the phased rollout dates (May 13, 2026 opt-in; February 10, 2027 default change; February 16, 2028 full implementation). The Robust Perception citation for Prometheus memory sizing is from the original Prometheus maintainer, which is the most authoritative source available.
- **Scope discipline:** Excellent. Stays within CP-04, CP-05, CP-06. The Phase 3 FTE Range Validation section (lines 316-333) appropriately cross-references the aggregate P1 total for context but does not re-derive ratings outside scope. No overlap with RP1a or RP1c territories.
- **Rating review quality:** Strong. The CP-04 Phase 3 RD borderline flag (4 vs 4-5) is well-reasoned: GT1 rates on-premises CP-04 at 5/5 composite, but the review correctly notes the Phase 3 scale is relative-to-cloud-native, not absolute. The interview question for Vault auto-unseal vs manual Shamir key entry is operationally precise and would resolve the ambiguity. The CP-06 Phase 3 TE 3 flag is the most important quantitative finding: GT1 FTE of 2.0-3.25 maps more naturally to TE 4 than TE 3 on the Phase 3 scale. This is correctly identified as the primary tension.
- **Content depth:** Strong. The Prometheus 3 KB per-series claim is validated against the authoritative Robust Perception source and correctly noted as slightly conservative (cardinality-only is closer to 2 KB). The FIPS 140-3 analysis traces the compliance chain from Vault Enterprise version requirements through to licensing implications (Enterprise Plus with HSMs required). The Deutsche Telekom Flux case study is triple-sourced (FluxCD.io, GitHub telekom/das-schiff, Weaveworks blog) with appropriate caveats about applicability to the ISV use case.
- **Issues found:**
  1. The CP-06 Phase 3 TE 3 finding (Key Finding #4) identifies TE 3 as potentially one point optimistic, but the rating assessment table still shows "ACCURATE (borderline)" rather than "ADJUST." Given that the GT1 FTE range of 2.0-3.25 sits entirely above the TE 3 Phase 3 ceiling of 1.0 FTE, this warrants a stronger flag. The quantitative evidence supports ADJUST rather than ACCURATE (borderline).
  2. The Phase 3 FTE Range Validation table (line 329) shows CP-04 at "1.0-2.5 FTE scale" for TE 4, but GT1's 2.5-5.0 FTE range extends well above that ceiling. The text notes "Low end of GT1 range; conservative" — this is accurate but the implication (CP-04 Phase 3 TE may also be understated) deserves equal prominence to the CP-06 finding.
- **Fix recommendations:** Minor: Strengthen the CP-06 Phase 3 TE verdict from "ACCURATE (borderline)" to "ADJUST (borderline)" for consistency with the quantitative analysis in Key Finding #4.

---

### RP1c: P1 Operations and Compliance (CP-07, CP-08, CP-09, CP-10)

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1c_P1_operations_compliance.md`

- **Score:** PASS
- **Citation integrity:** Strong. External sources are well-selected: Replicated (commercial software distribution lifecycle), Octopus Deploy (DORA metrics), Paramify (FedRAMP cost 2026), Secureframe (FedRAMP cost), Expel (SOC build cost), Lumifi (SOC staffing cost), Falco CNCF project page. FedRAMP cost range ($250K-$2M+) is confirmed by two independent external sources (Paramify: $150K-$2M+; Secureframe: $100K-$300K+ for 3PAO assessments alone). SOC staffing floor (8-12 FTE, $2.5M/year) is confirmed by two external sources (Expel, Lumifi). The Replicated citation for per-customer deployment overhead is correctly positioned as corroborating evidence for the linear scaling claim rather than as a direct proof.
- **Scope discipline:** Excellent. Stays within CP-07, CP-08, CP-09, CP-10 across all three phases. The review explicitly addresses the task scope question about CP-08 and CP-09 Phase 1 TE 3 ratings (lines 222-229), providing a definitive conclusion ("Neither TE 3 rating is clearly wrong. Both sit at the high-risk boundary between TE 3 and TE 4.").
- **Rating review quality:** Strong. CP-07 Phase 3 (RD 5 / TE 5) is the most thoroughly validated rating in the entire Wave 2 corpus, with GT1 evidence, DORA metrics, SAP/Microsoft release cadence comparisons, and Replicated commercial platform evidence all converging. The CP-10 Phase 3 TE 4 upper-bound risk flag is well-quantified: GT1 FTE floor of 2.75 exceeds TE 4 ceiling of 2.5, supported by external SOC staffing data. The CP-09 data sovereignty inversion (on-premises 1/5, cloud-native 3/5) is correctly identified as the single anomaly in P1 — an insightful observation that demonstrates cross-subsegment awareness.
- **Content depth:** Strong. The analysis correctly identifies the conditional nature of the CP-08 and CP-09 Phase 1 TE 3 ratings (tooling-only vs. broader scope). The CP-10 Phase 2 RD/TE divergence (RD 3 / TE 2) is called out as the sharpest gap in the cluster with a useful strategic implication for ISV staffing ("staff with specialists but budget configuration-level time"). FedRAMP authorization cost is distinguished from FedRAMP infrastructure tooling cost — an important analytical distinction.
- **Issues found:**
  1. CP-08 Phase 3 TE 3 appears to be understated. The review notes (line 149) that GT1's 1.5 FTE lower bound is above the TE 3 Phase 3 ceiling of 1.0 FTE, which corresponds to TE 4. The review acknowledges the mismatch but rationalizes it as the Phase 3 TE 3 rating reflecting "an averaged single-customer annual cadence rather than fleet-wide totals." However, the Phase 3 TE scale is defined as annual FTE for the full fleet (the ratings file Phase 3 column header is "Phase 3 (annual)"), not per-customer. This interpretation may be incorrect. The GT1 data supports TE 4 for CP-08 Phase 3, not TE 3.
  2. The Lumifi URL in the Sources table (line 331) shows `the-true-cost-of-setting-up-and-operating-a-security-operations-center` but the in-text reference (line 282) cites `the-true-cost-of-setting-up-and-operating-a-24x7-security-operations-center` — minor URL discrepancy that should be reconciled.
- **Fix recommendations:** Minor: Re-examine the CP-08 Phase 3 TE 3 verdict. If the Phase 3 TE scale represents annual fleet-wide FTE (as the ratings file defines it), and GT1 records CP-08 on-premises at 1.5-2.5 FTE, then TE 4 (1.0-2.5 FTE) is a closer fit than TE 3 (0.3-1.0 FTE). This may warrant an ADJUST recommendation. Also reconcile the Lumifi URL discrepancy.

---

### RP1d: P1 Phase 2 Per-Customer Deep Dive (CP-01 through CP-10, Phase 2 only)

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1d_P1_phase2_deep_dive.md`

- **Score:** PASS
- **Citation integrity:** Strong. External sources are particularly well-chosen for Phase 2 validation: Shadow-Soft ISV deployment case study (160 hours / 4 person-weeks — the single most directly relevant external data point for per-customer effort), Replicated Time-to-Install data (2 hours online vs 2 weeks air-gapped), Connsulting on-premises revenue trap (6-month initial deployment cycles, 30-40% engineering time diversion), Spectro Cloud 2025 (50%+ snowflake clusters), Komodor 2025 (79% issues from system changes, MTTR >50 min), Tigera (on-premises K8s network HA design), Groundcover (overlay network requirements). The Keycloak/Okta SAML integration citation (https://maybeitdepends.com/keycloak-integration-with-okta) is from a community blog rather than an authoritative source — acceptable for a single data point but lower-tier than other citations.
- **Scope discipline:** Excellent. Strictly Phase 2 only across all 10 subsegments. Does not re-derive Phase 1 or Phase 3 ratings. Appropriately references Phase 1 infrastructure as prerequisites without re-evaluating Phase 1 ratings. The "6-14 Person-Week Per-Customer Estimate: Plausibility Assessment" section is correctly scoped to aggregate Phase 2 validation.
- **Rating review quality:** Strong. Each of the 10 subsegments receives a re-derived rating with confidence level and verdict. The analysis correctly identifies CP-02 as the highest-rated and most defensible Phase 2 subsegment. The 6-14 person-week aggregate estimate is validated against three independent external data points (Shadow-Soft 4 weeks, Replicated 2 weeks air-gapped, Connsulting 6-month initial cycle). The finding that 6-14 person-weeks is plausible for a mature ISV (5+ deployments) but likely understates first-customer effort is a valuable original insight. The hardware diversity sensitivity ranking (CP-02 > CP-01 > CP-04 > CP-05/CP-08) is well-supported.
- **Content depth:** Strong. The air-gapped customer distinction is the most important analytical contribution: Replicated's 60x time-to-install differential between online and air-gapped deployments supports creating a separate Phase 2 cost tier. The Connsulting "on-premises revenue trap" data (30-40% engineering time diversion, 50-85% personnel cost share) adds an ISV-specific business context that enriches the purely technical rating analysis. The Shadow-Soft 160-hour case study is correctly positioned as a lower bound (professional services with specialized tooling) rather than a representative figure.
- **Issues found:**
  1. CP-04 Phase 2: The review suggests "CONSIDER RAISING to RD=4, TE=3 for customers in regulated industries with HSMs" but does not commit to an ADJUST verdict. Given the FIPS 140-3 deadline (September 2026) and Let's Encrypt 45-day certificates (May 2026), both occurring during the review period, a firmer recommendation would be more actionable.
  2. The interview questions are uniformly strong, but CP-05 does not include one (it is the only subsegment without an interview question). Given the M confidence for all Phase 2 ratings overall, CP-05 would benefit from at least a brief probe about per-customer observability sizing effort.
- **Fix recommendations:** Minor: (1) Commit to a specific verdict for CP-04 Phase 2 (HOLD with annotation vs. ADJUST) given the 2026 regulatory timeline. (2) Add an interview question for CP-05 Phase 2 for completeness.

---

### RP1e: P1 Phase 1 Effort Estimate Validation (40-80 Person-Month Aggregate)

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1e_P1_phase1_effort.md`

- **Score:** PASS
- **Citation integrity:** Strong. External sources include practitioner benchmarks: Northflank (6-12 month IDP build timeline), PlatformEngineering.org (35.2% deliver value in 6 months, 40.9% cannot demonstrate value within first year), Gcore (2-3 engineers per self-hosted K8s cluster), Komodor 2025 (via Cloud Native Now — 34 workdays lost annually, 5 engineers per incident), Hostkey (15-month sovereign cloud migration), Shadow-Soft (6-month FedRAMP environment build), Intellyx/Replicated (70 of Fortune 100). The Cloud Native Now source for Komodor data is a secondary report; the primary BusinessWire press release is also cited in the RP1d file. The TRG International cloud repatriation source (83% CIO repatriation plans) is a trend article — lower authority than the other sources but acceptable for directional context.
- **Scope discipline:** Excellent. Strictly Phase 1, P1 Control Plane aggregate estimate. Does not re-derive individual Phase 1 ratings in depth (defers to RP1a, RP1b, RP1c for those) but provides a useful summary table of all 10 subsegment TE assignments with per-subsegment contribution estimates. The dependency constraint analysis (CP-01 gates all others; CP-03 -> CP-04 -> CP-02 -> CP-06 -> CP-07 chain) is an original analytical contribution within scope.
- **Rating review quality:** Strong. The reverse-engineering of the 40-80 person-month range from TE distributions is the central analytical contribution. The derivation is transparent: raw sum 64-120 person-months with a 0.55-0.67x parallelization factor yields 40-80 person-months — arithmetically consistent. The identification of five weak assumptions (undocumented parallelization factor, CP-01 as gating constraint, no learning-curve factor, concurrent technology migrations, fixed customer count assumption) is thorough and actionable. The per-subsegment TE re-derivation table (lines 187-198) provides 8/10 High or Medium-High confidence confirmations, with CP-03 and CP-06 as the two borderline cases — consistent with RP1a's and RP1b's findings for those subsegments.
- **Content depth:** Strong. The dependency constraint analysis (lines 63-80) adds genuine architectural insight — the serial critical path through CP-01, CP-04, CP-02, CP-06, CP-07 constrains effective parallelization in ways the raw TE sum does not capture. The calibration notes for each external benchmark are careful to distinguish build estimates from steady-state operations (e.g., Gcore's 2-3 engineers is operations, not build; Deutsche Telekom's 10 FTE / 200 clusters is steady-state, not initial build). This analytical discipline strengthens the assessment's credibility.
- **Issues found:**
  1. The parallelization factor (0.55-0.67x) is described as "undocumented" in the ratings file, and this is correctly flagged. However, RP1e does not provide a specific recommendation for whether the ratings file should document it. Given this is one of the five identified weak assumptions, a concrete recommendation to add a "Methodology Notes" section to the ratings file would be more actionable.
  2. The learning-curve factor (20-30% uplift for teams without on-premises experience) is stated without citation. While this is a reasonable engineering judgment, it would benefit from a supporting reference — platform engineering ramp-up time data from Gartner or similar would strengthen it.
- **Fix recommendations:** None required. Minor: (1) Recommend that the ratings file document the parallelization assumption. (2) Consider citing a source for the 20-30% learning-curve uplift estimate.

---

## Spot-Check Results

### Spot-Check 1: CP-04 On-Premises Composite Difficulty Rating

**Claim (RP1b, line 32-33):** "GT1 records the on-premises composite difficulty for CP-04 as 5/5, sourced from P1_control_plane.md."

**GT1 Verification:** GT1_P1_ground_truth.md, Summary Table (line 596): "CP-04 | Secrets Management, Certificate Lifecycle, and PKI | 1 | 2 | **5**"

GT1 Difficulty Ratings table (line 200) shows: Secret store operations 5/5, Certificate authority/PKI 4/5, HSM integration 5/5, Rotation automation 4/5, Composite Rating 5/5 on-premises.

**Result: CONFIRMED.** The claim accurately reflects GT1 data. The composite 5/5 is correctly sourced.

### Spot-Check 2: CP-06 On-Premises FTE Range

**Claim (RP1b, line 228-229):** "GT1 records on-premises FTE range for CP-06 as 2.0-3.25 FTE."

**GT1 Verification:** GT1_P1_ground_truth.md, CP-06 FTE Ranges (line 319): "[STATISTIC] On-Premises: 2.0-3.25 FTE"

GT1 Summary FTE table (line 615): "CP-06 | CI/CD Infrastructure / GitOps | 0.3-0.4 | 1.3-1.9 | **2.0-3.25**"

**Result: CONFIRMED.** The FTE range is exactly reproduced from GT1. RP1b's Key Finding #4 correctly flags that this 2.0-3.25 FTE range is above the TE 3 Phase 3 ceiling (0.3-1.0 FTE), supporting the borderline adjustment recommendation.

### Spot-Check 3: CP-10 On-Premises FTE Range and SOC Staffing Floor

**Claim (RP1c, line 273):** "A 24/7 Security Operations Center requires a minimum of 12 FTE and costs $1.5M-$5M annually [on-premises]."

**GT1 Verification:** GT1_P1_ground_truth.md, CP-10 Key Operational Characteristics (line 556-557): "[FACT] 'A 24/7 Security Operations Center requires a minimum of 12 FTE and costs $1.5M-$5M annually [on-premises].'"

**Claim (RP1c, line 278-279):** External corroboration: "You need at least 8-12 people operating in a SOC to maintain 24x7 shift coverage. An intermediate SOC will cost $2.5M per year."

**GT1 Verification:** The GT1 figure (minimum 12 FTE) sits at the top of the Expel external source's range (8-12 FTE). The cost ranges overlap ($1.5M-$5M GT1 vs $2.5M Expel intermediate). This is consistent — the GT1 figure may represent a fully staffed SOC rather than an entry-level build.

**FTE claim (RP1c, line 244):** CP-10 on-premises FTE 2.75-5.5. GT1 Summary table (line 619): "CP-10 | Security Operations | 0.25-1.2 | 2.25-4.5 | **2.75-5.5**"

**Result: CONFIRMED.** All three data points match GT1. The external SOC staffing data is directionally consistent with GT1's SOC cost floor. The RP1c analysis correctly identifies the tension between GT1's 2.75 FTE floor and the TE 4 ceiling of 2.5 FTE.

---

## Cross-File Consistency

### Coherent Narrative Assessment

The five files present a coherent and internally consistent picture of P1 Control Plane rating accuracy. The central narrative across all files is:

1. **Phase 1 ratings are largely accurate** (RP1a, RP1b, RP1e all confirm). The 40-80 person-month aggregate is internally consistent with the TE distribution. CP-01 (TE 5) and CP-05 (TE 5) are the two largest builds, confirmed independently by RP1a and RP1b respectively, and confirmed by RP1e's aggregate analysis.

2. **Phase 2 ratings carry lower confidence** due to sparse empirical data on per-customer deployment effort. RP1a, RP1b, RP1c, and RP1d all consistently assign Medium confidence to Phase 2 ratings for the same reason: GT1 provides platform-level difficulty data but not per-customer Phase 2 FTE measurements. RP1d's aggregate 6-14 person-week estimate is validated against external sources and explicitly noted as a mature-ISV figure.

3. **Phase 3 ratings have specific quantitative tensions** where GT1 FTE ranges exceed the TE scale thresholds. This finding recurs across files:
   - RP1a: CP-03 Phase 3 TE 4 may understate effort (GT1: 2.75-4.75 FTE vs TE 4 ceiling 2.5)
   - RP1b: CP-06 Phase 3 TE 3 is at the optimistic floor (GT1: 2.0-3.25 FTE vs TE 3 ceiling 1.0)
   - RP1c: CP-08 Phase 3 TE 3 sits below GT1 range (GT1: 1.5-2.5 FTE vs TE 3 ceiling 1.0)
   - RP1c: CP-10 Phase 3 TE 4 has upper-bound risk (GT1: 2.75-5.5 FTE vs TE 4 ceiling 2.5)

### Cross-File Contradiction Check

**No material contradictions found.** Specific alignment checks:

- **CP-01 Phase 2 (RD 4, TE 4):** RP1a and RP1d both confirm this rating. RP1d adds the Shadow-Soft 4 person-week external data point that RP1a does not cite, but both reach the same conclusion. No conflict.

- **CP-04 Phase 2:** RP1b assigns confidence Medium with verdict ACCURATE for RD 3, TE 3. RP1d re-derives RD=3-4, TE=3-4 and recommends CONSIDER RAISING for regulated-industry customers. These are compatible — RP1d's recommendation is a refinement, not a contradiction, of RP1b's median-case assessment.

- **CP-07 Phase 3 (RD 5, TE 5):** RP1c assigns High confidence. RP1e references CP-07 as a confirmed TE 4 build for Phase 1, appropriately distinguishing Phase 1 and Phase 3. No conflict.

- **CP-03 Phase 1 TE:** RP1a assigns TE 4 with High confidence. RP1e assigns TE 3-4 with Medium confidence, noting that a highly experienced team could achieve TE 3. This is a legitimate difference in assessed confidence but not a contradiction — RP1e is assessing from a team-capability variance perspective, while RP1a assesses from a GT1-data perspective. Both agree that TE 4 is the correct rating for the reference baseline.

### RP1d Phase 2 Alignment with RP1a-c Phase 2 Coverage

RP1d covers all 10 CP subsegments for Phase 2. RP1a covers CP-01, CP-02, CP-03 Phase 2; RP1b covers CP-04, CP-05, CP-06 Phase 2; RP1c covers CP-07, CP-08, CP-09, CP-10 Phase 2. The Phase 2 ratings and verdicts are consistent across all overlapping assessments:

| Subseg | RP1a/b/c Verdict | RP1d Verdict | Aligned? |
|--------|-----------------|--------------|----------|
| CP-01 Ph2 | ACCURATE (RP1a) | HOLD (RP1d) | Yes |
| CP-02 Ph2 | ACCURATE (RP1a) | HOLD with RD=5 note (RP1d) | Yes — RP1d adds the 2026 Ingress NGINX conditional |
| CP-03 Ph2 | ACCURATE (RP1a) | HOLD (RP1d) | Yes |
| CP-04 Ph2 | ACCURATE (RP1b) | CONSIDER RAISING (RP1d) | Compatible — RP1d adds regulated-industry conditional |
| CP-05 Ph2 | ACCURATE (RP1b) | HOLD (RP1d) | Yes |
| CP-06 Ph2 | ACCURATE (RP1b) | HOLD with air-gap annotation (RP1d) | Yes — RP1d adds air-gap conditional |
| CP-07 Ph2 | ACCURATE (RP1c) | HOLD with note (RP1d) | Yes — RP1d adds regulated maintenance window conditional |
| CP-08 Ph2 | ACCURATE (RP1c) | HOLD (RP1d) | Yes |
| CP-09 Ph2 | ACCURATE (RP1c) | HOLD with FedRAMP note (RP1d) | Yes — RP1d adds FedRAMP conditional |
| CP-10 Ph2 | ACCURATE (RP1c) | HOLD with SIEM note (RP1d) | Yes — RP1d adds SIEM integration conditional |

RP1d consistently adds customer-segment conditionals (regulated, air-gapped, SIEM-equipped) that the per-subsegment reviews assess at the median case. This is a productive division of analytical labor, not a source of conflict.

### RP1e Effort Estimate Alignment with RP1a-c Per-Subsegment Ratings

RP1e derives the 40-80 person-month aggregate from the 10-subsegment TE distribution. The TE assignments RP1e uses match those confirmed by RP1a (CP-01 TE 5, CP-02 TE 4, CP-03 TE 4), RP1b (CP-04 TE 4, CP-05 TE 5, CP-06 TE 4), and RP1c (CP-07 TE 4, CP-08 TE 3, CP-09 TE 3, CP-10 TE 4). RP1e's three Medium-confidence subsegments (CP-03, CP-06, CP-10) overlap with RP1a's Medium confidence on CP-03 Phase 1 (but for different reasons — RP1e questions team familiarity, RP1a questions Phase 3 FTE), RP1b's Medium confidence on CP-06 Phase 3 TE 3, and RP1c's Medium confidence on CP-10 Phase 3 upper bound. This convergence of Medium-confidence flags on the same subsegments from independent analytical angles strengthens confidence that these are genuine areas of uncertainty rather than random noise.

---

## Summary

- **Files passing:** 5 of 5
- **Files with minor issues:** 3 (RP1b, RP1c, RP1d)
  - **RP1b:** CP-06 Phase 3 TE verdict should be ADJUST rather than ACCURATE (borderline) given quantitative evidence. Minor fix.
  - **RP1c:** CP-08 Phase 3 TE 3 may be understated relative to GT1 data (1.5-2.5 FTE vs TE 3 ceiling 1.0 FTE). The review acknowledges the mismatch but may have misinterpreted the Phase 3 TE scale as per-customer rather than fleet-wide annual. Minor URL discrepancy in sources.
  - **RP1d:** CP-04 Phase 2 verdict could be more decisive; CP-05 lacks an interview question for completeness.
- **Files needing rework:** 0
- **Cross-file consistency notes:**
  - No material contradictions found across the five files.
  - All five files converge on the same core narrative: Phase 1 and Phase 3 RD ratings are well-supported; Phase 2 carries lower confidence universally; specific Phase 3 TE ratings (CP-03, CP-06, CP-08, CP-10) have quantitative tensions where GT1 FTE ranges push against TE scale boundaries.
  - RP1d enriches RP1a-c Phase 2 analyses with customer-segment conditionals (regulated, air-gapped, SIEM-equipped) that are compatible with, not contradictory to, the per-subsegment median-case assessments.
  - RP1e's aggregate validation confirms internal arithmetic consistency of the 40-80 person-month estimate and identifies the parallelization factor as the key undocumented assumption.
  - The most actionable cross-file finding is the pattern of Phase 3 TE understatement across 4 subsegments (CP-03, CP-06, CP-08, CP-10), all driven by the same structural issue: GT1 FTE ranges sit at or above the assigned TE scale ceiling. This is a systematic finding that warrants a single ratings-file-level correction pass, not per-subsegment patches.
