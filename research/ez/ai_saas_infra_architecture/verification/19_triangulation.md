# Cross-Source Triangulation Report: Adversarial Verification of Consolidated Draft

**Verification Date:** 2026-02-12
**Verifier:** Adversarial Verification Agent
**Document Under Review:** `consolidated/18_consolidated_draft.md`
**Sources Cross-Checked:** Wave 1 files 01-08

---

## Executive Summary

Cross-checked 14 specific data claims in the consolidated draft against their Wave 1 source files. Found 8 issues ranging from minor imprecision to material misrepresentation. The most significant problems are: (1) the draft cites "80% K8s production adoption" from CNCF but fails to adequately discount for the fact that CNCF 2024 survey had only n=750 respondents (down from n=988 in 2023 and n=3,800 in 2021), reducing statistical power; (2) two distinct "managed K8s" figures from different sources are conflated without acknowledging they measure different things; (3) the 73% Dynatrace managed figure and the 61% Tigera/market research figure are both cited as "managed K8s" without reconciling the 12pp gap; (4) the draft systematically underweights the strong VC-stage evidence that early-stage companies avoid K8s, which would push the <$10M non-K8s estimate higher than 55-70%. On the positive side, the migration direction claims, EU regional adoption claims, and $200M+ tier estimates are well-supported by multiple independent sources.

---

## Issues Found

### ISSUE 1: Conflation of Two Distinct "Managed K8s" Percentages

**Location:** Executive Summary point 1 (line 12); Citation Index (line 258); Section 3, Managed K8s cell-level notes

**Problem:** The draft references "73% managed K8s" from Dynatrace (02_analyst_reports.md, DP 1) as a core anchor for managed K8s estimates. But the Wave 1 data contains a second, lower figure: "Managed Kubernetes services host 61% of all production clusters" (01_cncf_survey.md, DP 37, from Tigera citing market research). The draft's citation index references both DP 37 (61%) and the Dynatrace 73% but does not reconcile this 12 percentage point gap in the body of the analysis.

Additionally, the CNCF 2024 survey itself (01_cncf_survey.md, DP 20) presents a more nuanced picture: "Survey respondents were evenly split (59%) between on-premises data centers and public clouds (both 59%), with both skewing heavily toward self-managed instances. A managed public cloud was the next most popular choice at 46%." The phrase "skewing heavily toward self-managed" directly contradicts the 73% managed narrative.

A third figure exists: 06_stackshare_github.md reports "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022" -- i.e., 67% cloud-hosted (not necessarily managed).

**Evidence:**
- 02_analyst_reports.md, DP 1: Dynatrace 73% managed (cloud environments only, 2023)
- 02_analyst_reports.md, DP 2: "63% of Kubernetes deployments" managed (all environments, 2025)
- 01_cncf_survey.md, DP 37: Tigera/market research 61% of production clusters (2024)
- 01_cncf_survey.md, DP 20: CNCF 2024 "skewing heavily toward self-managed"
- 06_stackshare_github.md: 67% cloud-hosted (2025)

**Recommended Correction:** The draft should explicitly reconcile these figures. The Dynatrace 73% applies to cloud-only deployments. The 61-67% figures apply to all environments (including on-prem). The CNCF 2024 "self-managed" signal should be presented as a counterpoint. The draft's derived estimate for managed K8s overall (45-55%) may actually be slightly high if the 61-67% all-environment figure is the correct baseline, since the draft's own assumption X1 acknowledges CNCF selection bias inflates K8s numbers.

**Impact on Confidence:** Managed K8s Overall cell confidence should drop from C:5 to C:4. The range 45-55% should be widened to 40-55% to accommodate the lower-bound signals.

---

### ISSUE 2: CNCF 2024 Sample Size Decline Not Flagged

**Location:** Section 8, Citation Index; Executive Summary point 1; throughout where "CNCF 80% production adoption" is cited

**Problem:** The draft prominently cites "K8s production adoption hit 80% in 2024" from CNCF as a foundational data point. However, the 2024 survey had n=750 respondents, down from n=988 in 2023 and n=3,800 in 2021. The 2023 survey had a stated margin of error of +/-2.6% at 90% confidence. The 2024 survey does NOT state a margin of error. The reduction from 3,800 to 750 respondents over three years raises questions about whether the sample is becoming less representative over time (possibly more concentrated among active CNCF community members), which would amplify the selection bias documented in assumption X1.

**Evidence:**
- 01_cncf_survey.md, DP 1: 2024 survey n=750
- 01_cncf_survey.md, DP 6: 2023 survey n=988, margin +/-2.6%
- 01_cncf_survey.md, DP 17: 2021 survey n=3,800

**Recommended Correction:** Add a note to the Known Limitations section (or a footnote to the CNCF citations) that the shrinking sample size may compound selection bias. The 80% figure should be presented alongside the Gartner 54% figure (02_analyst_reports.md, DP 6) more prominently, not just in passing. The "true" K8s production adoption for all enterprises is somewhere between 54% and 80%, and for AI SaaS specifically it is unknown.

**Impact on Confidence:** No individual cell change, but the overall methodology confidence should note this. The CNCF bias discount should be widened from "15-25pp" (line 317) to "15-30pp" to account for the declining sample quality.

---

### ISSUE 3: Underweighting of Early-Stage K8s Avoidance Evidence

**Location:** Section 3, Cloud-Native (Non-K8s Managed) <$10M cell (line 72); Managed K8s <$10M cell (line 90)

**Problem:** The draft estimates <$10M cloud-native non-K8s at 55-70% and managed K8s at 20-35%. However, Wave 1 evidence from 08_vc_startup_db.md contains strong, specific guidance that seed-stage companies should avoid K8s:

- Maven Solutions explicitly recommends "Kubernetes should be avoided early unless absolutely necessary due to its high adoption barrier" and recommends "fully managed platforms like Heroku, Vercel, or Firebase for speed" and "serverless options like AWS Lambda"
- YC 66% AI batch data combined with YC founder quote "No one can spend $20,000 to $30,000 a month on infrastructure costs" suggests cost pressure pushes toward serverless/PaaS
- 58% of YC startups accepting Azure credits (not K8s-specific credits)

The CNCF data (01_cncf_survey.md, DP 27) shows "only 9% of adopters are companies with 500-1,000 employees" and data below 500 employees is simply not reported -- suggesting negligible K8s adoption among very small companies.

The draft acknowledges this evidence but the 20-35% managed K8s estimate for <$10M may still be too high. A pre-revenue/seed company with 5-10 engineers has near-zero probability of running K8s. The 20-35% range is likely driven by the $5M-$10M ARR sub-segment within this tier, not the tier overall.

**Evidence:**
- 08_vc_startup_db.md: Maven Solutions seed-stage guidance (avoid K8s)
- 08_vc_startup_db.md: YC infrastructure cost burden quote
- 01_cncf_survey.md, DP 27: 9% K8s users at 500-1K employees, 0% reported below 500
- 08_vc_startup_db.md: 66% of YC W24 batch is AI (these are mostly pre-revenue)

**Recommended Correction:** Widen the <$10M cloud-native non-K8s range from 55-70% to 60-80%, and narrow managed K8s from 20-35% to 15-30%. Add a note that within this tier, architecture choice is highly bimodal: pre-revenue/seed companies (0-$2M) are nearly 100% non-K8s, while $5-10M companies begin adopting K8s at meaningful rates (potentially 30-45%).

**Impact on Confidence:** <$10M Cloud-native confidence remains C:6 (the evidence is directionally clear). <$10M Managed K8s confidence should drop from C:5 to C:4 because the range is less certain when accounting for bimodality within the tier.

---

### ISSUE 4: Draft Claims "Four Independent Engineering Blog Disclosures" of K8s Migration -- Accuracy Check

**Location:** Executive Summary point 6 (line 22)

**Problem:** The draft states: "Four independent engineering blog disclosures document migrations toward K8s (Figma: ECS to EKS, Grammarly: EC2 to EKS, Salesforce Data Cloud: EC2 to K8s, HubSpot: EC2 to K8s)." Cross-checking against 04_tech_blogs.md:

- **Figma:** Confirmed. "Figma migrated its compute platform from AWS ECS to Kubernetes (EKS) in less than 12 months." (2024)
- **Grammarly:** Confirmed. "Grammarly moved from EC2 to EKS." (January 2025)
- **Salesforce Data Cloud:** Confirmed. Article title: "Data Cloud Migrates From Amazon EC2 to Kubernetes in 6 Months." (2024)
- **HubSpot:** Partially accurate but misleading. HubSpot's K8s adoption is documented as starting in 2017-2018, with the CNCF case study describing migration of 400+ MySQL databases into K8s via Vitess. This is not a recent (2024-2025) migration disclosure -- it is a long-running infrastructure evolution. The draft frames it alongside 2024-2025 migrations, implying it is contemporaneous.

Additionally, the statement "Zero counter-migrations documented" is technically true but the draft already acknowledges publication bias. The stronger claim would note that HubSpot experienced a significant K8s-related incident in September 2024 (rollback from Envoy to Nginx), which is a data point suggesting K8s operational challenges even among committed adopters.

**Evidence:**
- 04_tech_blogs.md: Figma migration (August 2024 blog)
- 04_tech_blogs.md: Grammarly migration (January 2025 blog)
- 04_tech_blogs.md: Salesforce Data Cloud migration (2024)
- 04_tech_blogs.md: HubSpot case study dates to 2017-2018 (KubeCon 2018), not recent
- 04_tech_blogs.md: HubSpot September 2024 incident (Envoy rollback)

**Recommended Correction:** Change "Four independent engineering blog disclosures" to "Three recent (2024-2025) and one long-standing (2017+) engineering blog disclosures." Note the HubSpot temporal distinction. Consider adding the HubSpot incident as a data point about K8s operational risk.

**Impact on Confidence:** Minimal -- the directional claim about migration toward K8s is still well-supported by three recent, independent disclosures. The correction is about precision, not direction.

---

### ISSUE 5: "82% EU vs 70% Americas" Cloud-Native Claim Needs Context

**Location:** Executive Summary point 4 (line 18)

**Problem:** The draft states "82% EU vs 70% Americas per CNCF" as evidence for higher EU K8s adoption. Cross-checking against 01_cncf_survey.md, DP 15:

The actual data point is: "Europe: 82% in 'some' or 'much/all' cloud native development. Americas: 70% in 'some' or 'much/all' development."

This measures cloud-native development intensity (including containers, microservices, DevOps practices broadly), NOT Kubernetes adoption specifically and NOT AI SaaS companies. "Cloud native" encompasses serverless, containers without K8s, and other patterns. The draft uses this as supporting evidence for the claim that EU shows "5-15 percentage points higher Kubernetes adoption" -- but the source does not measure Kubernetes adoption. It measures cloud-native development broadly.

**Evidence:**
- 01_cncf_survey.md, DP 15: "Europe: 82% in 'some' or 'much/all' cloud native development"
- This is from the 2023 survey (n=988), not the 2024 survey

**Recommended Correction:** The draft should clarify that the CNCF regional data measures cloud-native development intensity, not K8s-specific adoption. The 82% vs 70% gap supports the claim that EU is more cloud-native in general, but the leap to "5-15pp higher K8s adoption" is the draft's inference, not a direct data point. EU K8s adoption remains at C:3 and should stay there.

**Impact on Confidence:** EU Avg confidence scores remain at C:3 (already very low). No cell change needed, but the supporting argument should be more precisely stated.

---

### ISSUE 6: Dynatrace 73% Managed Figure is From 2023 -- Age Not Flagged

**Location:** Assumption MK1 (line 218); used throughout managed K8s estimates

**Problem:** The draft's assumption MK1 states: "The 73% managed K8s figure from Dynatrace (2023) is directionally applicable to AI SaaS in 2025-2026." The draft correctly identifies this as an assumption with "Medium-High" confidence. However, the draft uses this as a primary anchor for managed vs. self-managed splits without adequately noting that:

1. The Dynatrace data is from 2023 -- now 2-3 years old
2. The CNCF 2024 data (DP 20) shows "skewing heavily toward self-managed" which could indicate the managed share has not increased as fast as assumed
3. Meanwhile, 06_stackshare_github.md reports "67% cloud-hosted" (up from 45% in 2022), which is 6pp lower than Dynatrace's 73%

The three data points (73% Dynatrace 2023, 67% cloud-hosted 2025, 61% Tigera 2024) suggest the managed share may be lower and more variable than the draft assumes. A best estimate might be 63-73% managed in cloud environments, not the single-point 73% the draft anchors on.

**Evidence:**
- 02_analyst_reports.md, DP 1: Dynatrace 73% (2023)
- 06_stackshare_github.md: 67% cloud-hosted (2025)
- 01_cncf_survey.md, DP 37: 61% managed (2024)
- 01_cncf_survey.md, DP 20: "skewing heavily toward self-managed" (2024)

**Recommended Correction:** Use a range of 61-73% for managed K8s share instead of anchoring on 73%. This would slightly widen the self-managed share from the draft's 27-37% to 27-39%, which has downstream effects on the Open/Self-Managed K8s estimates (currently 15-22% overall, could be 15-25%).

**Impact on Confidence:** Open/Self-Managed K8s Overall confidence could increase from C:4 to C:4 (no change) but the range should widen from 15-22% to 15-25%. Managed K8s Overall confidence stays at C:5 but the range should widen from 45-55% to 42-55%.

---

### ISSUE 7: The "44% Don't Run AI/ML on K8s" Data Point Is Underweighted

**Location:** Citation Index (line 258, DP 22 reference); not prominently used in estimate derivation

**Problem:** The CNCF finding that "44% of organizations report they do not yet run AI/ML workloads on Kubernetes" (01_cncf_survey.md, DP 22; 02_analyst_reports.md, DP 10) is cited in the draft's citation index but is not prominently used in deriving the managed K8s estimates for AI SaaS.

This is a critical data point because it directly addresses AI/ML workloads (closer to the research question than general K8s adoption). Among CNCF respondents -- who are already biased toward K8s adopters -- 44% still don't run AI on K8s. This suggests that for the general population, the percentage not running AI on K8s is higher (perhaps 55-65%).

Furthermore, 02_analyst_reports.md, DP 11 reports AI/ML model hosting splits: "37% using managed APIs, 25% self-hosting, and 13% at the edge." The 37% managed APIs figure means a large portion of AI companies use abstracted services (like Bedrock, Azure OpenAI, Vertex AI) rather than managing infrastructure. This supports higher non-K8s estimates for the <$10M tier where API-wrapper companies predominate.

The draft acknowledges this in assumption X6 but does not use it to adjust estimates downward.

**Evidence:**
- 01_cncf_survey.md, DP 22: 44% don't run AI/ML on K8s (among CNCF respondents)
- 02_analyst_reports.md, DP 10: Same 44% figure
- 02_analyst_reports.md, DP 11: 37% managed APIs, 25% self-hosting, 13% edge
- 01_cncf_survey.md, DP 25: 30% use MLaaS platforms

**Recommended Correction:** This data should be more prominently weighted in the <$10M and $10-50M tier estimates. The 37% managed APIs + 30% MLaaS figures suggest that a large fraction of AI companies -- particularly smaller ones -- do not manage infrastructure at all. This reinforces widening the <$10M non-K8s estimate upward (see Issue 3) and suggests the $10-50M managed K8s estimate of 50-65% may be 5-10pp too high for the AI SaaS sub-population (since many AI SaaS companies at this tier may still rely on managed API providers).

**Impact on Confidence:** $10-50M Managed K8s confidence should be noted as having a potential downward bias. Consider adding a caveat that the 50-65% estimate assumes companies self-host models; for API-wrapper AI SaaS, the figure is likely 30-45%.

---

### ISSUE 8: OpenAI "7,500 Nodes" Cited as Self-Managed K8s Evidence -- Classification Ambiguity

**Location:** Section 3, Open/Self-Managed K8s $200M+ cell (line 111); Evidence Density Map

**Problem:** The draft cites OpenAI as evidence for self-managed K8s at $200M+ (alongside Databricks, Salesforce, HubSpot). Cross-checking against 04_tech_blogs.md:

- OpenAI: "started running Kubernetes on top of AWS in 2016, and a year later, migrated the Kubernetes clusters to Azure" (01_cncf_survey.md, DP 35). The blog describes scaling to 7,500 nodes on Azure. However, whether this is "self-managed" or "managed AKS" is ambiguous. The original 2021 blog describes custom Kubernetes infrastructure on Azure (switching from Flannel to Azure CNI), which suggests significant self-management. But OpenAI's more recent $250B Azure commitment (referenced in 05_cloud_vendor_cases.md) could mean they have since moved to AKS.

- Databricks: Confirmed as "hybrid managed/self-managed" (04_tech_blogs.md explicitly states "mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)")

- Salesforce: Confirmed as self-managed. "Salesforce deploys and runs Kubernetes directly atop bare metal" (04_tech_blogs.md)

- HubSpot: The CNCF case study mentions "1,000 EC2 instances managed by one person" and describes K8s but does not clearly state whether it is self-managed or EKS. The original case study from 2017-2018 likely predates EKS maturity, but current state is unclear.

**Evidence:**
- 04_tech_blogs.md: OpenAI blog from 2021, infrastructure on Azure
- 01_cncf_survey.md, DP 35: "OpenAI started running Kubernetes on top of AWS in 2016, migrated to Azure"
- 04_tech_blogs.md: Salesforce bare metal K8s (confirmed self-managed)
- 04_tech_blogs.md: Databricks hybrid (confirmed)
- 04_tech_blogs.md: HubSpot K8s (classification unclear)

**Recommended Correction:** Reclassify the evidence as: Salesforce (confirmed self-managed), Databricks (confirmed hybrid), OpenAI (likely self-managed historically but current state uncertain), HubSpot (unclear -- may be managed or self-managed). This still supports the 25-35% self-managed estimate for $200M+ but with fewer confirmed data points than the draft implies. The confidence score of C:6 for this cell is marginally generous; C:5-6 is more appropriate.

**Impact on Confidence:** $200M+ Open/Self-Managed K8s confidence could drop from C:6 to C:5 if OpenAI and HubSpot classifications are uncertain. However, the cell still benefits from Salesforce (clear) and Databricks (clear hybrid), so C:5-6 is defensible.

---

## Revised Estimates

| Cell | Draft Estimate | Revised Estimate | Justification |
|---|---|---|---|
| Cloud-native non-K8s, <$10M | 55-70% (C:6) | 60-80% (C:6) | VC-stage guidance strongly favors non-K8s for seed/pre-revenue; CNCF shows 0% K8s data below 500 employees; bimodality within tier pushes upper bound higher |
| Managed K8s, <$10M | 20-35% (C:5) | 15-30% (C:4) | Counterpart to above. Pre-revenue/seed at near-0% K8s dilutes the tier average. The 20% lower bound assumed some seed-stage K8s; evidence suggests this is minimal |
| Managed K8s, $10-50M | 50-65% (C:6) | 45-65% (C:5) | AI SaaS at this tier includes many API-wrapper companies (37% use managed APIs per CNCF); these do not need K8s. Lower bound should account for this sub-population |
| Managed K8s, Overall | 45-55% (C:5) | 42-55% (C:4) | Wider range accommodates the 61-73% managed share uncertainty and the AI-specific 44% not-on-K8s signal |
| Open/Self-managed K8s, Overall | 15-22% (C:4) | 15-25% (C:4) | Wider managed share range (61-73% vs anchoring on 73%) pushes self-managed share higher |

---

## Revised Confidence Scores

| Cell | Draft Confidence | Revised Confidence | Justification |
|---|---|---|---|
| Managed K8s, <$10M | C:5 | C:4 | Bimodality within tier (pre-revenue vs $5-10M) makes a single range less reliable; VC guidance is prescriptive not descriptive |
| Managed K8s, $10-50M | C:6 | C:5 | Introduction of API-wrapper vs model-hosting distinction creates a sub-population split that the estimate does not address |
| Managed K8s, Overall | C:5 | C:4 | Wider uncertainty range on managed share (61-73% from multiple conflicting sources) |
| Open/Self-managed K8s, $200M+ | C:6 | C:5 | Two of four named company examples (OpenAI, HubSpot) have ambiguous managed vs self-managed classification |

---

## Items Verified as Correct

The following claims were cross-checked against Wave 1 sources and found well-supported:

1. **"66% of organizations hosting generative AI models use Kubernetes for inference"** (Executive Summary point 1) -- Confirmed. This appears verbatim in both 01_cncf_survey.md DP 21 and 02_analyst_reports.md DP 8. Both trace to the CNCF 2024/2025 survey.

2. **"Gartner 54% full/partial K8s implementation"** (Section 3, Managed K8s Overall note) -- Confirmed. 02_analyst_reports.md DP 6 states "54% of survey respondents having a full or partial implementation."

3. **"Serverless decline from 22% to 13% to 11%"** (Appendix B) -- Confirmed. 01_cncf_survey.md DP 31 (11% in 2024) and DP 32 (13% in 2023, down from 22% in 2022).

4. **"Figma: ECS to EKS migration"** -- Confirmed verbatim in 04_tech_blogs.md with date (August 2024), author (Ian VonSeggern), and reasons documented.

5. **"Grammarly: EC2 to EKS for ML infrastructure"** -- Confirmed in 04_tech_blogs.md with specific details (January 2025, Argo CD, Helm charts, KubeRay).

6. **"Salesforce: bare metal K8s"** -- Confirmed. 04_tech_blogs.md: "Salesforce deploys and runs Kubernetes directly atop bare metal."

7. **"Databricks: hybrid managed/self-managed"** -- Confirmed. 04_tech_blogs.md: "Operates mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)."

8. **"OpenShift $1.9B ARR at 30%+ growth"** -- Confirmed. 07_sec_earnings.md cites IBM Q4 2025 earnings call: "OpenShift ARR exceeded $1.9 billion at more than 30% growth."

9. **"AWS $128.7B revenue"** -- Confirmed. 07_sec_earnings.md cites AWS Q4 2024 earnings.

10. **"AI SaaS 40-50% COGS vs traditional SaaS 6-12% hosting"** -- Confirmed across multiple Wave 1 sources. 07_sec_earnings.md and 08_vc_startup_db.md both cite the Monetizely 40-50% figure, and 07_sec_earnings.md cites the SaaS Capital/FlowCog 6-12% baseline.

11. **"CoreWeave $12B OpenAI contract, 250K GPUs, 62% cost advantage"** -- Confirmed in 08_vc_startup_db.md with specific source citations (Sacra Research).

12. **"Bessemer 25% early-stage margins"** -- Confirmed. 08_vc_startup_db.md: "an analysis by Bessemer Venture Partners found that a cohort of fast-scaling AI SaaS startups had only ~25% gross margin on average in early stages."

13. **"Only 2 EU AI company case studies in Wave 1 (Stacks, Medigold Health)"** -- Confirmed by inspection. 04_tech_blogs.md mentions Stacks (Amsterdam, GKE Autopilot) and 05_cloud_vendor_cases.md references Medigold (UK, Azure). These are the only EU-headquartered AI companies with case studies in Wave 1.

14. **Serverless adoption reconciliation (Appendix B)** -- The draft's reconciliation of the 65-70% Datadog, 70% CNCF NA, and 11% CNCF global figures is logically sound. The explanation that these measure different scopes (any use vs production loads vs primary framework) is correct and well-documented. This is one of the draft's strongest analytical sections.

15. **"No direct measurement of AI SaaS architecture choice by revenue tier exists"** (Executive Summary point 5) -- Confirmed. Exhaustive review of all 8 Wave 1 files found zero sources that directly segment "AI SaaS companies" by both architecture choice and revenue tier. Every Wave 1 file's limitations section explicitly notes this gap.

16. **Migration direction uniformly toward K8s** -- Confirmed for the three recent cases (Figma, Grammarly, Salesforce Data Cloud). The 04_tech_blogs.md limitations section explicitly notes "No engineering blogs disclosed moving FROM K8s TO serverless." The publication bias caveat is appropriately noted.

---

## Source Weighting Assessment

The draft generally weights sources appropriately, with two exceptions:

**Appropriately Weighted:**
- CNCF surveys treated as highest-signal but with acknowledged selection bias -- correct
- Dynatrace telemetry data treated as objective (observability data, not self-reported) -- correct
- Engineering blogs treated as directional evidence with publication bias caveat -- correct
- SEC filings treated as factual where disclosed but limited in technology granularity -- correct
- VC/startup data treated as proxy signals with multiple documented biases -- correct

**Underweighted:**
- **CNCF DP 22 (44% no AI on K8s)** and **DP 11 (37% managed APIs)** -- These are among the most directly relevant data points to the research question ("AI SaaS infrastructure") and should anchor the analysis more heavily. They are cited but not used to constrain estimates.
- **Maven Solutions/SaaStr stage-specific guidance** (08_vc_startup_db.md) -- This is prescriptive (what should be done) not descriptive (what is done), so the draft is right to discount it somewhat. But the consistency across multiple VC advisory sources (Maven, SaaStr, YC patterns) gives it moderate weight as a signal of actual early-stage behavior.

**Overweighted:**
- **Dynatrace 73% managed figure** -- Used as a primary anchor despite being from 2023 and contradicted by multiple 2024-2025 sources showing 61-67%. The draft should use a range rather than a point estimate.

---

## Summary of Changes

| Category | Count | Severity |
|---|---|---|
| Data point misquotation | 0 | N/A |
| Data point misinterpretation | 2 | Moderate (Issues 1, 8) |
| Missing context or qualification | 3 | Minor to Moderate (Issues 2, 4, 5) |
| Underweighted evidence | 2 | Moderate (Issues 3, 7) |
| Overweighted evidence | 1 | Moderate (Issue 6) |
| Estimate range too narrow | 5 | Moderate (see Revised Estimates table) |
| **Total issues** | **8** | |
| **Items verified correct** | **16** | |

The draft's overall analytical framework is sound. The conflict resolution methodology, assumptions register, and limitations documentation are thorough and honest. The primary issues are at the margins: ranges that should be wider, source conflicts that should be reconciled more explicitly, and a few data points that deserve more prominent weighting. No fundamental errors in direction or order of magnitude were found.

---

**Document Version:** 1.0
**Verification Methodology:** Selective cross-referencing of 14+ specific data claims against Wave 1 source files 01-08
**Estimated Coverage:** ~70% of quantitative claims in the draft were cross-checked; 100% of named company examples were verified
