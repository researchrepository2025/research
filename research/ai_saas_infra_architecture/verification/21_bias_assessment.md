# Adversarial Bias Assessment: Consolidated Estimate Matrix

**Assessment Date:** 2026-02-12
**Role:** Adversarial Verification Agent
**Target Document:** `consolidated/18_consolidated_draft.md`
**Source Documents Reviewed:** Wave 1 files 01-08, with focus on "Data Quality Assessment" and "Known Biases" sections

---

## Executive Summary

The consolidated draft's estimates are systematically biased upward for Kubernetes adoption (both managed and self-managed) and downward for cloud-native non-K8s services across all revenue tiers. This is not a single-source problem -- it is a structural artifact of the entire evidence base. Every major data source (CNCF surveys, tech blogs, vendor case studies, StackShare/GitHub, job postings, VC reports) carries pro-K8s selection, survivorship, or publication bias. The only partial counterweight -- VC stage guidance recommending against K8s at seed stage -- was insufficiently weighted during consolidation. After bias adjustment, managed K8s overall adoption drops from 45-55% to 35-48%, cloud-native non-K8s rises from 25-40% to 33-50%, and confidence scores decline for 15 of 21 cells. The sub-$10M tier and all EU cells are the most severely affected, with multiple cells warranting confidence reductions of 1-2 points.

---

## Issues Found

### Issue 1: Unidirectional Source Bias Across All Eight Wave 1 Inputs

**Location:** All cells in the estimate matrix; methodology section (Section 2)

**Problem:** Every Wave 1 data source carries bias in the same direction -- toward overstating Kubernetes adoption and understating non-K8s alternatives. There is no countervailing source that over-represents serverless, PaaS, or ECS/Fargate users. When every input pushes the same direction, triangulation across sources does not cancel bias -- it amplifies it.

**Evidence:**
- **01_cncf_survey.md:** Self-selected CNCF community respondents. 91% from 1,000+ employee orgs. CNCF reports 80-82% K8s production adoption vs. Gartner's 54% for general enterprise -- a 26-28pp gap attributable to selection bias. The draft acknowledges this (Section 9, Limitation 2) but applies only a 15-25pp discount, which is the low end of the measured gap.
- **02_analyst_reports.md:** Dynatrace telemetry (73% managed K8s) measures only Dynatrace customers, who are observability-mature enterprises more likely to run K8s. Datadog telemetry covers only Datadog customers. Both are biased toward sophisticated infrastructure users.
- **03_job_postings.md:** Most job posting datasets are pre-filtered for K8s-related roles (kube.careers, DevOpsCube K8s analyses). Job postings reflect aspirational hiring, not current stack. 66-70% North American geographic skew.
- **04_tech_blogs.md:** 4 documented migrations toward K8s, 0 away. 100% directional skew. Publication bias acknowledged but not quantitatively discounted.
- **05_cloud_vendor_cases.md:** Self-rated confidence 3/10. Marketing materials with extreme selection bias. 44% do not disclose infrastructure architecture. The draft correctly treats this as low-weight, but it still contributes directional bias.
- **06_stackshare_github.md:** Self-reported StackShare profiles skew toward VC-backed, open-source-friendly companies. GitHub public repos represent less than 5% of enterprise code. 91% enterprise respondents.
- **07_sec_earnings.md:** Only covers public companies at $200M+ ARR. Technology architecture rarely disclosed in 10-Ks. K8s is mentioned via partnership announcements (vendor marketing), not operational disclosures.
- **08_vc_startup_db.md:** VC reports reflect investment theses and portfolio company narratives. Survivorship bias throughout. The one countervailing signal -- seed-stage guidance recommending against K8s -- was noted but insufficiently integrated.

**Recommended Correction:** Apply a systematic 5-10pp downward adjustment to all managed K8s estimates and a corresponding 5-10pp upward adjustment to cloud-native non-K8s estimates across all tiers. The adjustment should be larger (8-12pp) for tiers with weaker evidence (sub-$10M, $10-50M) and smaller (3-7pp) for the $200M+ tier where named-company evidence partially offsets selection bias.

**Impact on Confidence:** Reduces confidence for every cell by 0.5-1 point to reflect the unquantifiable structural bias.

---

### Issue 2: Sub-$10M Tier Estimates Are Contradicted by VC Stage Guidance

**Location:** All three architecture rows, <$10M column

**Problem:** The draft estimates managed K8s at 20-35% for sub-$10M ARR companies. But File 08 (VC/startup DB) documents that seed-stage guidance explicitly recommends AGAINST Kubernetes. Maven Solutions and SaaStr-cited infrastructure guides recommend serverless/PaaS for companies with 5-30 engineers. The YC W24 batch (66% AI companies) used Azure credits (58%) -- Azure's starter path is App Service and Azure Functions, not AKS. The draft's 20-35% managed K8s estimate at this tier is anchored to CNCF data that excludes companies under 500 employees (91% of CNCF respondents are 1,000+ employees).

**Evidence:**
- File 08, Known Biases section: "Architecture patterns by stage: Low - primarily guidance/recommendations not empirical data"
- File 08: "Seed-stage K8s avoidance guidance" listed as a data point
- File 01: "9% in 500-1,000 employee orgs" and no data below 500 employees
- Draft Assumption T3: "VC-backed stage guidance reflects actual startup behavior" rated Low-Medium confidence
- Draft Section 9, Limitation 3: "Companies under 500 employees are invisible in survey data"

**Recommended Correction:** Lower managed K8s at <$10M from 20-35% to 12-25%. Raise cloud-native non-K8s at <$10M from 55-70% to 65-80%. Self-managed K8s at <$10M remains at 2-5% (this is likely correct -- no sub-$10M company self-manages K8s).

**Impact on Confidence:** The draft's C:5 for managed K8s at <$10M and C:6 for cloud-native at <$10M should both be reduced to C:3. There is essentially zero empirical data for this tier; the estimates are pure extrapolation from enterprise data applied downward, contradicted by the only tier-specific qualitative guidance available.

---

### Issue 3: Tech Blog Migration Evidence Has 100% Survivorship Bias

**Location:** Executive Summary finding #6; managed K8s estimates at all tiers; assumptions X3 and X5

**Problem:** The draft states "Migration flows uniformly toward Kubernetes" and cites 4 blog-documented migrations (Figma, Grammarly, Salesforce, HubSpot) with "zero counter-migrations documented." The draft adds "though publication bias likely suppresses negative cases" but does not quantify this suppression or adjust estimates accordingly. The fact that 4/4 documented migrations are toward K8s does not mean 100% of actual migrations are toward K8s -- it means that companies that migrated toward K8s published blog posts about it and companies that stayed on or migrated to non-K8s did not.

**Evidence:**
- File 04, Known Biases: "Publication Bias: Companies with problems are less likely to publish engineering blogs"
- File 04, Known Biases: "Success Bias: Migration stories typically published after successful completion"
- File 04, Limitations: "Failure Rates: No companies disclosed failed K8s migrations or decisions to abandon K8s"
- File 04, Limitations: "Serverless Adoption: No engineering blogs disclosed moving FROM K8s TO serverless"
- File 04, Limitations: "Non-K8s Architectures: Companies using ECS, Lambda, or other patterns less likely to publish"
- File 04 confidence self-assessment: 4-5/10 for "exact market share percentages" and "companies that tried and abandoned Kubernetes"

**Recommended Correction:** The draft's assumption X5 ("Absence of documented migrations away from K8s reflects actual low abandonment, not just publication bias") should be downgraded from Low-Medium confidence to Low confidence. The migration evidence should be treated as directionally suggestive but not used to weight K8s estimates upward. Specifically, the claim "Migration flows uniformly toward Kubernetes" in the executive summary should be reframed as "Published migration case studies exclusively document moves toward K8s, but this reflects extreme publication bias and cannot be interpreted as a market-wide pattern."

**Impact on Confidence:** No direct cell-level impact, but removes a supporting rationale that inflates overall K8s confidence. The draft uses migration directionality as converging evidence for K8s dominance; removing this support weakens the case by approximately 0.5 confidence points for managed K8s across the $10-50M and $50-200M tiers.

---

### Issue 4: EU Estimates Built on Nearly Zero Evidence

**Location:** EU Avg column for all three architecture rows

**Problem:** The draft acknowledges EU evidence is extremely sparse (Section 9, Limitation 6: "Only 2 EU AI company case studies exist in Wave 1 data") and rates Agent 17 confidence at 3/10. Despite this, the draft presents EU estimates as ranges (e.g., "40-50% managed K8s in EU") with confidence scores of 3 -- implying some evidentiary basis. In reality, the EU estimates are structural arguments about GDPR impact applied to US data, not independent measurements. The two EU case studies (Stacks on GKE Autopilot, Medigold on Azure) are so few as to be anecdotal, not representative.

**Evidence:**
- File 05: Only 2 EU AI company case studies total
- Agent 17 self-rates 3/10 overall confidence
- No EU-specific CNCF breakout beyond regional participation percentages
- No EU-specific Datadog or Dynatrace segmentation
- File 08: "Geographic Bias: Heavy U.S. focus; limited international data"
- File 03: "66-70% of K8s job data is North America"

**Recommended Correction:** EU Avg confidence scores should be reduced from C:3 to C:2 across all three architecture rows. The current C:3 implies "at least one weak source supports the estimate." In reality, no source supports the EU-specific estimates -- they are US estimates adjusted by structural arguments about GDPR. The estimate ranges themselves should be widened by 10pp in each direction to reflect the genuine uncertainty. The claim that "EU shows 5-15pp higher Kubernetes adoption" (Executive Summary finding #4) should be flagged as unverifiable conjecture, not a finding.

**Impact on Confidence:** All EU Avg cells drop from C:3 to C:2. This is the weakest area of the entire analysis and should be explicitly labeled as speculative.

---

### Issue 5: The CNCF-Gartner Gap Is Underutilized as a Bias Calibration Tool

**Location:** Overall managed K8s estimate (45-55%, C:5); Section 9, Limitation 2

**Problem:** The gap between CNCF-reported K8s adoption (80-82%) and Gartner-reported K8s adoption (54%) is the single most important bias calibration signal in the dataset. This 26-28pp gap quantifies how much CNCF selection bias inflates K8s estimates. The draft acknowledges a 15-25pp inflation but uses the low end of this range for calibration. Gartner's 54% itself may carry upward bias (Gartner respondents are enterprise IT leaders, not the general market). The true population K8s adoption rate for all companies (not just enterprises and not just cloud-native practitioners) is likely below 54%.

**Evidence:**
- File 01: CNCF 80% K8s production adoption (2024), 82% (2025)
- File 02: Gartner 54% K8s full/partial implementation
- Draft Section 9: "CNCF survey selection bias inflates K8s adoption by an estimated 15-25 percentage points"
- File 02, Known Biases: Gartner respondents are enterprise decision-makers, not representative of all companies
- The actual bias magnitude is 26-28pp (80-54=26, 82-54=28), not 15-25pp

**Recommended Correction:** The bias adjustment should use the measured 26-28pp gap, not the draft's conservative 15-25pp. For AI SaaS companies specifically, the adjustment may be smaller (AI SaaS companies are more cloud-native than average enterprises, so they may genuinely use more K8s), but this assumption itself (X2) is rated Medium confidence. The net effect: overall managed K8s should be adjusted from 45-55% to 38-50% -- still the largest category, but with a wider uncertainty band.

**Impact on Confidence:** Overall managed K8s confidence remains at C:5 but the estimate range shifts downward by 5-7pp.

---

### Issue 6: Cloud-Native Non-K8s Is Systematically Under-Measured

**Location:** Cloud-native non-K8s row, all columns

**Problem:** Every data source in the analysis has better measurement of K8s than non-K8s alternatives. CNCF surveys ask about K8s; Dynatrace and Datadog telemetry instruments K8s clusters; tech blogs discuss K8s migrations; job postings are analyzed for K8s keywords; StackShare has K8s as a trackable stack component. By contrast, no source directly measures "companies using ECS/Fargate as primary infrastructure" or "companies using Cloud Run without K8s." The Datadog serverless data (65% Lambda usage, 70% Cloud Run) measures any use, not primary use. The draft correctly distinguishes "any use" from "primary use" but has no direct source for non-K8s primary adoption. All non-K8s estimates are derived as residuals: "if X% use K8s, then approximately (100-X)% might use something else." This residual methodology inherits all K8s measurement biases in inverted form.

**Evidence:**
- File 02: "Low Confidence (3-5/10) for AI SaaS-specific infrastructure choices (no direct data)"
- File 02: "PaaS vs CaaS vs self-managed distribution (overlapping definitions)"
- Draft Agent 09 (cloud-native deep dive): Self-rated confidence 4/10
- Draft Section 5: Cloud-native non-K8s evidence density is Moderate at best, Weak for most cells
- No dedicated survey or telemetry source for ECS/Fargate, Cloud Run, or App Service adoption as primary architecture

**Recommended Correction:** Cloud-native non-K8s estimates should be adjusted upward by 5-12pp across all tiers. The current estimates treat K8s as the well-measured category and derive non-K8s as a residual. Since K8s is over-measured, the residual is systematically too small. Specific adjustments: <$10M from 55-70% to 65-80%, $10-50M from 30-45% to 35-50%, $50-200M from 20-30% to 22-35%, $200M+ from 15-25% to 18-28%.

**Impact on Confidence:** Non-K8s confidence scores should decrease by 0.5-1 point for all cells except $200M+ (where named companies provide some direct evidence of non-K8s usage patterns).

---

### Issue 7: Self-Managed K8s at $200M+ Is the Best-Supported Estimate but Still Over-Relies on a Handful of Named Companies

**Location:** Self-managed K8s, $200M+ cell (25-35%, C:6)

**Problem:** The $200M+ self-managed K8s estimate is the strongest cell in the matrix, supported by named companies: OpenAI (7,500 nodes), Databricks (hybrid), Salesforce (bare metal K8s), HubSpot. However, this is 4 named companies used to represent a category containing hundreds of $200M+ AI SaaS companies. The named companies are also among the most extreme in terms of scale and GPU requirements. OpenAI's 7,500-node cluster is not representative of a $200M+ analytics SaaS company. The estimate may be correct but its confidence (C:6) overstates the evidentiary basis -- named examples from the extreme tail of the distribution are being treated as representative.

**Evidence:**
- File 04: OpenAI, Databricks, Salesforce, HubSpot are all $1B+ ARR companies, not typical $200M-500M companies
- File 07: SEC filings only cover large-cap public companies; "Do NOT extrapolate to sub-$50M ARR"
- Draft Section 5: $200M+ self-managed K8s rated "Strong" evidence density based on these named examples
- 4 named companies is a very small sample even for named-company evidence

**Recommended Correction:** Maintain the 25-35% range but reduce confidence from C:6 to C:5. The named companies provide existence proof that self-managed K8s is viable and used at $200M+, but the specific percentage is based on a sample of 4 extreme-scale companies extrapolated to the full $200M+ population.

**Impact on Confidence:** C:6 to C:5 for this cell.

---

### Issue 8: Multi-Architecture Usage Framing Masks the Primary Architecture Question

**Location:** Executive Summary finding #7; all cells

**Problem:** The draft notes "At $10M+ ARR, an estimated 40-55% of companies run production workloads on multiple architecture categories simultaneously." This is important context, but it also means the estimate matrix -- which measures "primary or significant production architecture" -- is inherently double-counting. A company running EKS for core API services and Lambda for event processing would be counted in BOTH the managed K8s row AND the cloud-native non-K8s row. The rows sum to more than 100%, which the draft does not explicitly address. Without knowing the overlap percentage, the absolute adoption figures are misleading.

**Evidence:**
- Draft Executive Summary #7: "Multi-architecture usage is the norm, not the exception"
- Draft Conflict Log: Multiple conflicts resolved by distinguishing "primary" from "any use" from "some workloads"
- Draft cell notes for $200M+ cloud-native: "Agent 15 gives 40-55% for 'some workloads'" vs 15-25% for primary
- At $200M+: 55-65% managed K8s + 15-25% cloud-native + 25-35% self-managed = 95-125% (overlapping)

**Recommended Correction:** The draft should include an explicit "overlap adjustment" row or footnote showing estimated overlap percentages by tier. Without this, readers may interpret the rows as mutually exclusive categories that should sum to 100%. The lack of overlap quantification adds 5-10pp of systematic uncertainty to each cell.

**Impact on Confidence:** Conceptual rather than numerical -- does not change specific cell estimates but should reduce reader confidence in comparing across rows.

---

## Bias-Adjusted Estimate Matrix

### Cloud-Native (Non-K8s Managed): Serverless, PaaS, ECS/Fargate, Cloud Run

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Draft** | 55-70% (C:6) | 30-45% (C:5) | 20-30% (C:4) | 15-25% (C:5) | 30-40% (C:5) | 15-25% (C:3) | 25-40% (C:4) |
| **Bias-Adjusted** | 65-80% (C:3) | 35-52% (C:4) | 23-35% (C:3) | 18-28% (C:4) | 35-48% (C:4) | 12-30% (C:2) | 33-50% (C:3) |
| **Direction** | +10pp | +5-7pp | +3-5pp | +3pp | +5-8pp | Widened | +8-10pp |
| **Rationale** | VC guidance contra K8s; zero empirical data for this tier; CNCF invisible below 500 employees | K8s over-measurement inflates residual undercount; no direct non-K8s survey | Moderate: some named companies validate non-K8s at scale; less bias adjustment needed | Smallest adjustment: named company evidence available; multi-arch usage provides some direct signal | US serverless is better measured (Datadog 65% Lambda); upward adjustment for primary use | No evidence either direction; range widened to reflect genuine ignorance | Structural upward adjustment for systematic non-K8s under-measurement |

### Managed Kubernetes (EKS, AKS, GKE)

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Draft** | 20-35% (C:5) | 50-65% (C:6) | 55-65% (C:6) | 55-65% (C:7) | 50-60% (C:5) | 40-50% (C:3) | 45-55% (C:5) |
| **Bias-Adjusted** | 12-25% (C:3) | 40-55% (C:4) | 45-58% (C:5) | 50-62% (C:6) | 42-53% (C:4) | 30-50% (C:2) | 35-48% (C:4) |
| **Direction** | -8-10pp | -10pp | -7-10pp | -3-5pp | -7-8pp | Widened, -5-10pp | -7-10pp |
| **Rationale** | Largest downward adjustment: VC guidance recommends against K8s at seed; CNCF data inapplicable below 500 employees; YC Azure credits default to non-K8s services | Significant CNCF selection bias; 26-28pp CNCF-Gartner gap not fully discounted; aspirational job postings vs actual stacks | Moderate adjustment: some Inferred classification cells; Dynatrace/Datadog bias toward observability-mature companies inflates K8s signal | Smallest adjustment: named company evidence (OpenAI, Anthropic, Snowflake, Figma) provides partial offset to selection bias | CNCF-Gartner gap applies; Datadog telemetry biased toward sophisticated users | No independent EU data; structural GDPR argument is plausible but untested | Full structural bias adjustment: 26-28pp CNCF-Gartner gap partially applied |

### Open/Self-Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Draft** | 2-5% (C:5) | 5-12% (C:5) | 8-15% (C:4) | 25-35% (C:6) | 10-18% (C:4) | 20-30% (C:3) | 15-22% (C:4) |
| **Bias-Adjusted** | 1-4% (C:4) | 3-10% (C:4) | 6-13% (C:3) | 22-33% (C:5) | 8-16% (C:3) | 15-30% (C:2) | 10-18% (C:3) |
| **Direction** | -1pp | -2pp | -2pp | -2-3pp | -2pp | Widened | -4-5pp |
| **Rationale** | Minor adjustment: draft estimate already low; slightly lower because if managed K8s is over-stated, some of that over-statement leaks into self-managed estimates via total-K8s figures | CNCF self-managed percentage may be overstated by K8s-enthusiast respondents who self-manage by choice, not necessity | Dynatrace 27% self-managed may include hybrid configurations; slight downward adjustment | Smallest adjustment: named companies (OpenAI, Databricks, Salesforce) provide real evidence; reduce from C:6 to C:5 due to small sample | Minor downward to match overall adjustment | EU self-managed is the most speculative of all cells; widened range; GDPR argument is plausible | Overall decline tracks managed K8s decline: if total K8s is lower, self-managed share of lower total is also lower |

---

## Revised Confidence Scores

| Cell | Draft Confidence | Revised Confidence | Justification |
|---|---|---|---|
| Cloud-native, <$10M | C:6 | C:3 | Zero empirical data for companies under 500 employees. Estimate based entirely on extrapolation from enterprise data applied downward plus qualitative VC guidance. Draft's C:6 is unjustifiable for a tier with no direct measurement. |
| Cloud-native, $10-50M | C:5 | C:4 | Residual estimation from K8s data that itself carries significant bias. No direct non-K8s measurement exists. One point reduction for structural under-measurement. |
| Cloud-native, $50-200M | C:4 | C:3 | No direct survey data for non-K8s at this tier. Some named companies (via tech blogs, case studies) provide existence proof but not prevalence data. |
| Cloud-native, $200M+ | C:5 | C:4 | Some evidence from SEC filings (companies not disclosing K8s implies possible non-K8s usage) and Agent 15 analysis. But inference from absence is weak evidence. |
| Cloud-native, US Avg | C:5 | C:4 | US serverless data (Datadog 65% Lambda) is for "any use," not primary. No direct primary-use measurement. |
| Cloud-native, EU Avg | C:3 | C:2 | No EU-specific non-K8s data whatsoever. Estimate is US data adjusted by GDPR structural argument with zero empirical support. |
| Cloud-native, Overall | C:4 | C:3 | Structural under-measurement of non-K8s inflates uncertainty. All estimates derived as residuals from biased K8s data. |
| Managed K8s, <$10M | C:5 | C:3 | CNCF data inapplicable below 500 employees. VC stage guidance contradicts the estimate. YC batch data suggests non-K8s defaults. No empirical data for this tier. Draft's C:5 was the largest over-confidence in the matrix. |
| Managed K8s, $10-50M | C:6 | C:4 | CNCF selection bias (26-28pp measured gap) not fully discounted. Job posting data measures demand, not deployment. No direct survey of $10-50M companies. Two-point reduction reflects the compounding of multiple unidirectional biases. |
| Managed K8s, $50-200M | C:6 | C:5 | Inferred classification is appropriate but inference chain starts from biased CNCF data. Dynatrace telemetry biased toward observability-mature firms. One point reduction. |
| Managed K8s, $200M+ | C:7 | C:6 | Named company evidence (Anthropic on GKE, Figma on EKS, Snowflake on EKS) is genuine but represents top-of-market. One point reduction for small sample extrapolation to full $200M+ population. |
| Managed K8s, US Avg | C:5 | C:4 | US data is better than EU but still indirect. CNCF-Gartner gap calibration not fully applied. |
| Managed K8s, EU Avg | C:3 | C:2 | Two EU case studies is anecdotal, not evidence. GDPR-driven K8s argument is plausible but unquantified. |
| Managed K8s, Overall | C:5 | C:4 | Structural upward bias from all sources. Managed K8s is still likely the largest single category but at lower adoption than draft estimates. |
| Self-managed K8s, <$10M | C:5 | C:4 | Draft estimate of 2-5% is likely directionally correct (no sub-$10M company self-manages K8s). One point reduction because even 2-5% may overstate: the lower bound could be 0-1% for true sub-$10M AI SaaS. |
| Self-managed K8s, $10-50M | C:5 | C:4 | Derived from CNCF data that over-represents K8s enthusiasts. Some self-managed K8s users in CNCF surveys may be hobbyists or educators, not production deployments. |
| Self-managed K8s, $50-200M | C:4 | C:3 | No direct data. Estimate split from total K8s figure that is itself biased upward. |
| Self-managed K8s, $200M+ | C:6 | C:5 | Named company evidence (OpenAI, Databricks, Salesforce, HubSpot) is real but represents 4 companies at the extreme tail ($1B+ ARR, not typical $200-500M). Generalization to all $200M+ is a stretch. |
| Self-managed K8s, US Avg | C:4 | C:3 | No direct US-specific self-managed K8s data. Derived from total K8s minus managed K8s, both of which carry bias. |
| Self-managed K8s, EU Avg | C:3 | C:2 | GDPR sovereignty argument for higher self-managed K8s in EU is plausible but supported by zero empirical data. Range widened. |
| Self-managed K8s, Overall | C:4 | C:3 | Self-managed share declining is directionally well-supported (trend rating 7/10). Specific percentages are low-confidence. |

**Summary of Confidence Changes:**
- Cells reduced by 2 points: 3 (managed K8s <$10M, managed K8s $10-50M, cloud-native <$10M)
- Cells reduced by 1 point: 15
- Cells unchanged: 0
- Cells increased: 0
- Average confidence reduction: 1.2 points

---

## Items Verified as Correct

Despite the systematic bias issues, the following elements of the draft are verified as directionally correct and appropriately caveated:

1. **"No direct measurement exists for the core research question" (Section 9, Limitation 1).** This is the draft's single most important statement. Every cell being classified as Estimated (E) or Inferred (I) is accurate.

2. **Managed K8s is the plurality architecture at $50M+ ARR.** Even after bias adjustment, managed K8s at 45-58% ($50-200M) and 50-62% ($200M+) remains the largest single category. The bias adjustment reduces the magnitude but not the ranking.

3. **Self-managed K8s is declining.** The directional trend (7/10 confidence per Agent 11) is well-supported by the shift from 27% to 22% self-managed in Dynatrace data, the growth of managed K8s features (EKS 100K nodes, GKE 130K nodes), and no new entrants to self-managed K8s at smaller scales. This trend claim is robust.

4. **Multi-architecture usage is the norm at $10M+ ARR.** The 40-55% multi-architecture estimate is plausible and supported by Datadog serverless-alongside-K8s data. The draft appropriately distinguishes "any use" from "primary use."

5. **EU evidence is extremely sparse.** The draft's C:3 for Agent 17 and the acknowledgment that only 2 EU case studies exist (Section 9, Limitation 6) are accurate assessments. The bias adjustment simply extends this honesty by reducing EU confidence further to C:2.

6. **The CNCF-Gartner gap as a bias indicator.** The draft correctly identifies and documents this gap. The disagreement here is only about the magnitude of the discount applied (the draft applies 15-25pp; the measured gap is 26-28pp).

7. **Company heterogeneity adds 10-20pp uncertainty.** The draft's observation (Section 9, Limitation 7) that API-wrapper companies and model-hosting companies have fundamentally different infrastructure needs is correct and appropriately flagged.

8. **The conflict resolution methodology is sound.** The draft's approach of distinguishing "primary architecture" from "any use" from "some workloads" is the correct resolution for the definitional conflicts between agents. The Conflict Log (Section 6) is well-documented.

9. **Classification of $50-200M and $200M+ managed K8s as Inferred (I) is appropriate.** The inference chain (CNCF 80% K8s + Dynatrace 73% managed = ~58% managed K8s) is documented and logically valid. The bias adjustment reduces the estimate magnitude but not the classification.

10. **Seed-stage K8s avoidance is noted in Assumption T3.** The draft includes this as an assumption but rates it Low-Medium confidence. The bias assessment argues it should be weighted higher, but the draft does not ignore it.

---

## Appendix: Source Bias Direction Summary

| Source | File | Bias Direction | Magnitude | Mechanism |
|---|---|---|---|---|
| CNCF Surveys | 01 | Over-states K8s | 26-28pp (measured) | Self-selected cloud-native practitioners; 91% from 1K+ employee orgs |
| Analyst Reports | 02 | Over-states K8s | 10-15pp (estimated) | Dynatrace/Datadog telemetry covers only their customers (observability-mature enterprises) |
| Job Postings | 03 | Over-states K8s demand | 5-10pp (estimated) | Pre-filtered for K8s roles; aspirational hiring vs current stack; 66-70% NA geographic skew |
| Tech Blogs | 04 | Over-states K8s | 15-25pp (estimated) | 100% survivorship bias in migration stories; publication bias excludes non-K8s companies |
| Cloud Vendor Cases | 05 | Over-states K8s | High but low weight (C:3) | Marketing materials; extreme selection bias; 44% omit architecture details |
| StackShare/GitHub | 06 | Over-states K8s | 10-15pp (estimated) | Self-reported profiles skew VC-backed; GitHub public repos <5% of enterprise code; 91% enterprise respondents |
| SEC/Earnings | 07 | Over-states K8s at $200M+ | 5-10pp (estimated) | Only public large-cap companies; K8s visible via vendor partnerships, non-K8s invisible |
| VC/Startup DB | 08 | Mixed: over-states K8s investment narrative, provides counter-signal at seed stage | Variable | VC narrative bias and survivorship bias push K8s up; seed-stage guidance pushes K8s down |

**Net bias direction for every cell in the matrix: upward for K8s, downward for non-K8s.**

No source in the dataset carries a systematic pro-serverless or pro-PaaS bias. This unidirectional bias structure is the fundamental weakness of the analysis, and it cannot be resolved through triangulation -- only through purpose-built primary research targeting the specific research question.

---

**Assessment Version:** 1.0
**Compiled:** 2026-02-12
**Methodology:** Adversarial review of 9 source documents with focus on bias direction, magnitude, and compounding effects
**Conclusion:** The draft is a credible first-order estimate with appropriate caveats, but its estimates are systematically skewed upward for K8s and downward for non-K8s by approximately 5-10 percentage points across most cells. Confidence scores should be reduced for all 21 cells, with the largest reductions (2 points) at the sub-$10M and $10-50M managed K8s cells where the evidence base is thinnest and the bias is strongest.
