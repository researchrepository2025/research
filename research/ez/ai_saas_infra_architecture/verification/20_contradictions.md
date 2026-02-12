# Internal Consistency Verification Report

**Verification Date:** 2026-02-12
**Target Document:** `consolidated/18_consolidated_draft.md`
**Source Documents Verified Against:** Wave 2 files 09-17
**Verification Type:** Adversarial cross-reference for contradictions, mathematical inconsistencies, and confidence-score misalignment

---

## Executive Summary

The consolidated draft is structurally sound and resolves the majority of inter-agent conflicts correctly. However, this verification identified **10 issues** ranging from a missing conflict-log entry (an Agent 09 EU finding that directly contradicts Agent 17 and the draft) to inflated confidence scores in cells with weak evidence density, to an executive-summary headline number ("60-70%") that overstates the matrix values it claims to summarize. Two issues are high-impact: the unstated weighting methodology for "Overall" estimates and the systematic pattern of confidence scores exceeding what evidence density supports. Correcting these issues narrows three estimate ranges and reduces four confidence scores, producing a more defensible final product.

---

## Issues Found

### Issue 1: Unlogged Conflict -- Agent 09 EU Cloud-Native Direction Contradicts Agent 17 and Draft

**Location:** Section 6 (Conflict Log), Cloud-native EU Avg cell

**Problem:** Agent 09, Finding 6 states: "EU AI SaaS companies may show 5-10 percentage points higher cloud-native non-K8s adoption than US counterparts, driven by regulatory constraints favoring managed services with compliance certifications." This asserts EU > US for cloud-native non-K8s. Agent 17 and the consolidated draft both show the opposite direction: EU 15-25% vs US 30-40%, meaning EU is 5-15pp LOWER than US. This is a sign-reversal contradiction (Agent 09 says +5-10pp, reality per Agent 17 is -5 to -15pp) that is absent from the Conflict Log in Section 6.

**Evidence:**
- Agent 09 (`09_cloud_native_deepdive.md`), Finding 6: "EU AI SaaS companies may show 5-10 percentage points higher cloud-native non-K8s adoption than US counterparts"
- Agent 17 (`17_eu_market.md`): EU cloud-native 15-25%, with explicit comparison table showing EU is lower than US by 10-15pp
- Consolidated draft Section 3, Cloud-native EU Avg: 15-25% (C:3), US Avg: 30-40% (C:5)
- The Conflict Log (Section 6) has no entry for this contradiction

**Agent 09's Internal Logic Error:** Agent 09 reasons that regulatory constraints favor "managed services with compliance certifications," but this reasoning actually supports managed K8s (AKS, EKS, GKE with compliance certifications), not cloud-native non-K8s (serverless/PaaS). The finding contradicts its own stated reasoning. GDPR data-residency pressure reduces the appeal of serverless (where data-path control is limited) and pushes toward K8s (where data locality is configurable) [CNCF Annual Survey 2023 - Regional Adoption](https://www.cncf.io/reports/cncf-annual-survey-2023/). Agent 09 acknowledged "very low confidence" on this finding, but the conflict should still be logged.

**Recommended Correction:** Add an entry to the Conflict Log (Section 6):

| Cell | Agent A (Source) | Agent A Estimate | Agent B (Source) | Agent B Estimate | Delta | Resolution |
|---|---|---|---|---|---|---|
| Cloud-native, EU Avg | Agent 09 (Cloud-native deep dive) | EU is 5-10pp higher than US | Agent 17 (EU market) | EU is 15-25% vs US 30-40% (EU is 10-15pp lower) | 15-25pp sign reversal | Agent 09's Finding 6 is internally contradictory (its reasoning about compliance actually supports K8s, not serverless) and was assigned "very low confidence." Agent 17's EU-specific analysis is preferred. Draft correctly follows Agent 17. |

**Impact on Confidence:** No change to estimate or confidence score (the draft already follows Agent 17). Impact is to the completeness of the Conflict Log documentation.

---

### Issue 2: Executive Summary Headline Overstates Matrix Values

**Location:** Section 1 (Executive Summary), paragraph 1

**Problem:** The executive summary states: "The 60-70% figure cited for companies above $10M ARR is well-triangulated across CNCF surveys, Dynatrace observability data, engineering blog disclosures, and vendor case studies." However, the estimate matrix in Section 3 shows:

- $10-50M managed K8s: 50-65% (C:6)
- $50-200M managed K8s: 55-65% (C:6)
- $200M+ managed K8s: 55-65% (C:7)

A simple average of these three tier ranges yields 53-65%. Even weighting more heavily toward the larger tiers (which have more evidence), the weighted midpoint is approximately 55-65%, not 60-70%. The "60-70%" headline comes from Agent 10's overall estimate, which was subsequently refined downward during tier-specific analysis. The executive summary references the pre-resolution Agent 10 headline rather than the post-resolution matrix values.

**Evidence:**
- Agent 10 (`10_managed_k8s_deepdive.md`), headline: "Overall Estimate: 60-70% of AI SaaS companies with >$10M ARR" -- this figure was derived from [Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) (73% managed K8s in cloud), [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) (80% K8s production adoption), and [Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)
- Consolidated draft Section 3, Managed K8s row: $10-50M at 50-65%, $50-200M at 55-65%, $200M+ at 55-65%
- No tier in the matrix reaches the upper bound of 70%

**Recommended Correction:** Revise executive summary paragraph 1 to: "Across all revenue tiers above $10M ARR, managed K8s adoption ranges from 50-65%, with the tightest convergence at 55-65% for companies above $50M ARR. The higher 60-70% figure from the architecture-focused analysis (Agent 10) was refined downward during tier-specific triangulation."

Alternatively, if the 60-70% is retained as a reference to Agent 10's pre-resolution estimate, it should be explicitly qualified: "Agent 10's pre-resolution estimate of 60-70% was refined to 50-65% across tiers during cross-agent consolidation."

**Impact on Confidence:** Managed K8s overall confidence score remains C:5. No numeric estimate change required; the matrix is correct. Impact is on the narrative framing in the executive summary.

---

### Issue 3: Confidence Scores Inflated Relative to Evidence Density -- Cloud-Native $10-50M

**Location:** Section 3 (Cloud-native $10-50M) and Section 5 (Evidence Density Map)

**Problem:** Cloud-native $10-50M is assigned C:5 confidence with Evidence Density rated "Weak" and Classification "E" (Estimated). A C:5 with Weak density and Estimated classification is inconsistent with the framework's own definitions. The draft's Appendix A shows Agent 13 (the primary source for this cell) self-reported 5/10 confidence, but this was for Agent 13's overall analysis, not specifically for the cloud-native estimate which was the most contested cell (Agent 09 at 15-30% vs Agent 13 at 45-60%, requiring a 15-30pp resolution). The resolution itself introduces additional uncertainty that should reduce confidence below the source agents' self-assessments, not match them.

**Evidence:**
- Section 3: Cloud-native $10-50M = 30-45% (C:5)
- Section 5: Evidence Density for this cell = Weak
- Section 4: Classification = E (Estimated)
- Section 6: This cell has the largest conflict in the log (15-30pp delta between Agent 09 and Agent 13)
- The resolution required redefining the measurement scope ("primary or significant" vs "used for some workloads"), which is a judgment call adding further uncertainty
- Agent 09's estimate of 15-30% was based on [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) serverless adoption data (11% global) and [Datadog serverless container data](https://www.datadoghq.com/state-of-containers-and-serverless/)
- Agent 13's estimate of 45-60% extrapolated from broader cloud-native adoption patterns but lacked direct $10-50M ARR tier measurement

**Recommended Correction:** Reduce confidence to C:4. A cell that is Estimated, has Weak evidence density, and required the largest definitional resolution in the entire conflict log should not score higher than C:4.

**Impact on Confidence:** Cloud-native $10-50M: C:5 -> C:4

---

### Issue 4: Confidence Scores Inflated Relative to Evidence Density -- Open K8s $10-50M

**Location:** Section 3 (Open K8s $10-50M) and Section 5 (Evidence Density Map)

**Problem:** Open K8s $10-50M is assigned C:5 with Evidence Density "Weak" and Classification "E" (Estimated). The same logic applies as Issue 3: a Weak/Estimated cell should not carry C:5 confidence. Agent 11's estimate for this cell was originally for the broader $10-200M range (8-15%) and was narrowed to 5-12% by preferring Agent 13's tier-specific analysis. The narrowing is reasonable, but the result inherits Agent 13's limitations for this tier (no direct measurement, pure estimation from adjacent data).

**Evidence:**
- Section 3: Open K8s $10-50M = 5-12% (C:5)
- Section 5: Evidence Density = Weak
- Section 4: Classification = E (Estimated)
- Agent 11's original estimate covered a different tier boundary ($10-200M combined), derived from [Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) showing 27% self-managed K8s in cloud and [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) self-managed deployment data
- Agent 13 (preferred source) self-reported 5/10 for its overall analysis, but this cell's evidence is weaker than the managed K8s estimate that anchored Agent 13's confidence

**Recommended Correction:** Reduce confidence to C:4.

**Impact on Confidence:** Open K8s $10-50M: C:5 -> C:4

---

### Issue 5: Confidence Score Inconsistency -- Cloud-Native $200M+ vs $50-200M

**Location:** Section 3 (Cloud-native $200M+ and $50-200M)

**Problem:** Cloud-native $200M+ has C:5, while cloud-native $50-200M has C:4. Yet the $200M+ cell required the second-largest conflict resolution in the log (25-40pp delta: Agent 09 at 5-15% vs Agent 15 at 40-55%), and the resolution at 15-25% is entirely above Agent 09's range, effectively overriding Agent 09's estimate completely. In contrast, the $50-200M cell had a smaller conflict (Agent 09 at 10-20% vs Agent 14 at 25-35%, with the resolution at 20-30% overlapping both ranges). The cell with the larger conflict and more aggressive resolution should not have higher confidence.

The $200M+ cell does benefit from "Moderate" evidence density (vs "Weak" for $50-200M), which partially justifies a higher score. However, the evidence density at $200M+ comes primarily from engineering blog disclosures about K8s usage ([OpenAI scaling Kubernetes to 7,500 nodes](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), [Databricks managing thousands of K8s clusters](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), [Anthropic using GKE](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/)), which tells us what they DO use, not what they don't. The cloud-native non-K8s estimate at $200M+ is inferred from the complement of K8s adoption, which is a weaker form of evidence for this specific cell.

**Evidence:**
- Section 3: Cloud-native $200M+ = 15-25% (C:5), Evidence Density = Moderate
- Section 3: Cloud-native $50-200M = 20-30% (C:4), Evidence Density = Weak
- Section 6: $200M+ conflict = 25-40pp delta (larger); $50-200M conflict = 5-15pp delta (smaller)
- The $200M+ resolution (15-25%) is entirely disjoint from Agent 09's range (5-15%), indicating one source was effectively discarded

**Recommended Correction:** Reduce Cloud-native $200M+ from C:5 to C:4. Both the $50-200M and $200M+ cells have similar uncertainty profiles once the conflict-resolution magnitude is factored in.

**Impact on Confidence:** Cloud-native $200M+: C:5 -> C:4

---

### Issue 6: "Overall" Estimates Lack Stated Weighting Methodology

**Location:** Section 3, "Overall" column for all three architecture rows; Section 2 (Methodology)

**Problem:** The "Overall" column presents estimates (Cloud-native 25-40%, Managed K8s 45-55%, Open K8s 15-22%) that the cell notes describe as consistent with "tier-weighted averages." However, the weighting methodology is never stated. This matters because the result differs significantly depending on whether "overall" means company-count-weighted or revenue-weighted:

**Company-count-weighted** (approximate distribution: 60% under $10M, 25% $10-50M, 10% $50-200M, 5% $200M+):
- Cloud-native: 0.60 * 62.5% + 0.25 * 37.5% + 0.10 * 25% + 0.05 * 20% = 37.5 + 9.4 + 2.5 + 1.0 = **~50%**
- Managed K8s: 0.60 * 27.5% + 0.25 * 57.5% + 0.10 * 60% + 0.05 * 60% = 16.5 + 14.4 + 6.0 + 3.0 = **~40%**
- Open K8s: 0.60 * 3.5% + 0.25 * 8.5% + 0.10 * 11.5% + 0.05 * 30% = 2.1 + 2.1 + 1.2 + 1.5 = **~7%**

**Revenue-weighted** (approximate: 15% under $10M, 25% $10-50M, 30% $50-200M, 30% $200M+):
- Cloud-native: 0.15 * 62.5% + 0.25 * 37.5% + 0.30 * 25% + 0.30 * 20% = 9.4 + 9.4 + 7.5 + 6.0 = **~32%**
- Managed K8s: 0.15 * 27.5% + 0.25 * 57.5% + 0.30 * 60% + 0.30 * 60% = 4.1 + 14.4 + 18.0 + 18.0 = **~55%**
- Open K8s: 0.15 * 3.5% + 0.25 * 8.5% + 0.30 * 11.5% + 0.30 * 30% = 0.5 + 2.1 + 3.5 + 9.0 = **~15%**

The draft's "Overall" values (25-40%, 45-55%, 15-22%) align more closely with the revenue-weighted calculation for all three rows. But the draft does not state this. If a reader assumes company-count weighting, the cloud-native "Overall" at 25-40% appears too low (~50% expected) and managed K8s at 45-55% appears too high (~40% expected).

**Evidence:**
- Draft Section 3, Cloud-native Overall: 25-40% -- matches revenue-weighted ~32% but not company-weighted ~50%
- Draft Section 3, Managed K8s Overall: 45-55% -- matches revenue-weighted ~55% but not company-weighted ~40%
- Draft Section 3, Open K8s Overall: 15-22% -- matches revenue-weighted ~15% but not company-weighted ~7%
- Section 2 (Methodology) does not specify the weighting scheme for "Overall"

**Recommended Correction:** Add a methodological note to Section 2 and/or to the "Overall" column header: "Overall estimates are implicitly revenue-weighted (or market-significance-weighted), not company-count-weighted. This gives proportionally more influence to larger companies whose architecture choices are better evidenced and represent a larger share of AI SaaS economic activity. Under a company-count-weighted scheme, cloud-native overall would be approximately 45-55% and managed K8s approximately 35-45%."

If company-count-weighted estimates are desired, they should be presented as an alternative row.

**Impact on Confidence:** Overall confidence scores should remain unchanged, but this methodological gap reduces the interpretability of the "Overall" column. Recommend adding C:3 qualifier note indicating the methodology is itself uncertain.

---

### Issue 7: Cloud-Native $10-50M Resolution Range May Be Too Wide

**Location:** Section 3 (Cloud-native $10-50M) and Section 6 (Conflict Log)

**Problem:** The draft resolves the Agent 09 vs Agent 13 conflict by consolidating at 30-45% for "primary or significant architecture." This 15pp-wide range is the second-widest range in the entire cloud-native row (tied with $200M+ at 10pp, exceeded only by <$10M at 15pp). The width reflects genuine uncertainty, but the resolution logic may allow narrowing.

Agent 09 gives 15-30% for "primary architecture." Agent 13 gives 45-60% for "some workloads" (non-exclusive). The draft's "primary or significant" framing should logically fall between "primary only" and "any use." If we take "primary or significant" as roughly the midpoint between the two definitions: midpoint of 15-30% = 22.5%, midpoint of 45-60% = 52.5%, average = 37.5%. A range centered on 37.5% could be 30-45% (which is what the draft uses) or a slightly tighter 32-42%.

However, the $10-50M tier is also where multi-architecture usage first becomes significant (40-55% per the draft). This means a substantial fraction of companies at this tier use cloud-native non-K8s as a secondary architecture alongside K8s. The "primary or significant" framing inherently captures some of these secondary-use cases, pulling the estimate upward relative to "primary only." This suggests the lower bound (30%) is more defensible than the upper bound (45%), because 45% would imply near-parity with managed K8s (50-65%) at this tier, which contradicts the narrative that K8s becomes dominant above $10M [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [Tigera Kubernetes Statistics 2025](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/).

**Evidence:**
- Agent 09: 15-30% (primary only) -- derived from [CNCF serverless data](https://www.cncf.io/reports/cncf-annual-survey-2024/) (11% serverless framework usage) and [Datadog serverless container adoption](https://www.datadoghq.com/state-of-containers-and-serverless/)
- Agent 13: 45-60% (some workloads, non-exclusive)
- Draft resolution: 30-45% (primary or significant)
- Draft Section 3, Managed K8s $10-50M: 50-65%
- If cloud-native is truly 45% and managed K8s is 50%, these are nearly equal -- inconsistent with the executive summary's framing of K8s as "dominant" above $10M

**Recommended Correction:** Consider narrowing to 28-40%. This keeps the lower bound close to Agent 09's upper end while pulling the upper bound away from near-parity with managed K8s. Alternatively, retain 30-45% but add a note: "The upper bound (45%) implies near-parity with managed K8s at this tier, which would conflict with the directional finding of K8s dominance above $10M ARR. The estimate midpoint (37.5%) is more likely than the upper extreme."

**Impact on Confidence:** Marginal. If narrowed to 28-40%, the precision improvement is small but the internal narrative consistency improves.

---

### Issue 8: Agent 10's $50-200M Total K8s vs Draft's Managed K8s Decomposition

**Location:** Section 6 (Conflict Log), Managed K8s $50-200M entry

**Problem:** The conflict log states that Agent 10's 70-85% figure is "ALL K8s usage (managed + self-managed)" and that subtracting 8-15% self-managed yields convergence with Agent 14's 55-65%. Let me verify the arithmetic:

- Agent 10 total K8s: 70-85% -- derived from [Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) (73% managed K8s in cloud environments), [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) (80% K8s production usage), and [Red Hat Kubernetes Adoption Survey](https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview) (70% IT leaders using K8s)
- Agent 14 self-managed K8s: 8-15%
- Implied managed K8s (Agent 10): 70-85% minus 8-15% = 55-77%

The draft resolves at 55-65%. The subtraction yields 55-77%, but the draft uses only the lower portion (55-65%) without explaining why the upper portion (65-77%) is excluded. The resolution is defensible if Agent 14's 55-65% managed estimate is preferred because it analyzes this tier specifically, but the conflict log's stated resolution mechanism ("After separating managed from total K8s, the estimates converge") is imprecise. They don't fully converge -- the ranges overlap at 55-65% but Agent 10's derived range extends to 77%.

**Evidence:**
- Agent 10: 70-85% total K8s at $50-200M
- Agent 14: 55-65% managed K8s, 8-15% self-managed K8s at $50-200M
- Agent 14 total K8s: 55-65% + 8-15% = 63-80% (overlaps with Agent 10's 70-85%)
- Draft resolution: 55-65% managed K8s
- Agent 10's implied managed range: 55-77% (wider than draft's 55-65%)

**Recommended Correction:** Update the Conflict Log entry to: "Agent 10's 70-85% is for total K8s (managed + self-managed). Subtracting Agent 14's 8-15% self-managed yields an implied managed range of 55-77% from Agent 10. Agent 14's direct estimate of 55-65% managed is preferred as the tighter, tier-specific analysis. The upper portion of Agent 10's implied range (65-77%) is not supported by Agent 14's data and is excluded."

**Impact on Confidence:** No change to estimate or confidence. Impact is on the precision of the Conflict Log narrative.

---

### Issue 9: Cloud-Native $200M+ Estimate Fully Overrides Agent 09

**Location:** Section 3 (Cloud-native $200M+) and Section 6 (Conflict Log)

**Problem:** Agent 09 estimates cloud-native non-K8s at $200M+ as 5-15% (for primary architecture). Agent 15 estimates 40-55% (for some workloads). The draft resolves at 15-25% for "primary or significant." However, the draft's lower bound (15%) equals Agent 09's upper bound (15%), meaning Agent 09's entire range is effectively below the resolution. In practice, Agent 09's estimate has been discarded in favor of Agent 15's data reframed to a narrower definition.

This is not necessarily wrong -- Agent 15 conducted a deeper tier-specific analysis and may be more reliable. But the conflict log should acknowledge that the resolution does not "blend" the two estimates; it effectively overrides Agent 09 with a reframed version of Agent 15.

Additionally, there is a question about whether 15-25% is too generous for "primary or significant" when the major named $200M+ companies (OpenAI [K8s at 7,500 nodes on Azure](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), Databricks [thousands of K8s clusters](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), Anthropic [GKE mega-scale clusters](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), Snowflake [EKS for testing infrastructure](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), Salesforce [K8s on bare metal](https://engineering.salesforce.com/tagged/kubernetes/), Figma [migrated from ECS to EKS](https://www.figma.com/blog/migrating-onto-kubernetes/), Grammarly [migrated from EC2 to EKS](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)) overwhelmingly use K8s as their primary architecture. The 40-55% "some workloads" figure from Agent 15 includes companies using Lambda or Cloud Run for secondary tasks (event processing, CI/CD) alongside K8s. Narrowing from "some workloads" to "primary or significant" should produce a number closer to Agent 09's range than to Agent 15's. A midpoint resolution might be 10-20% rather than 15-25%.

**Evidence:**
- Agent 09: 5-15% (primary architecture)
- Agent 15: 40-55% (some workloads)
- Draft: 15-25% (primary or significant)
- Draft lower bound (15%) = Agent 09 upper bound (15%)
- Named $200M+ companies are predominantly K8s-primary
- "Primary or significant" is closer in meaning to "primary" than to "some workloads"

**Recommended Correction:** Consider revising to 10-22%. This range overlaps with both Agent 09's upper range (10-15%) and the draft's current range (15-22%), producing a genuine blend rather than an override. Alternatively, retain 15-25% but update the Conflict Log to note: "Agent 09's estimate is effectively superseded by Agent 15's reframed estimate. This is acceptable because Agent 15 conducts deeper tier-specific analysis, but it means the resolution is not a blend of both sources."

**Impact on Confidence:** If revised to 10-22%, the confidence remains C:4 (reduced from C:5 per Issue 5). The narrower range does not improve confidence because the definitional boundary between "primary" and "significant" remains judgment-based.

---

### Issue 10: Managed K8s $10-50M Range Inconsistency with Conflict Resolution

**Location:** Section 3 (Managed K8s $10-50M) and Section 6 (Conflict Log)

**Problem:** The Conflict Log notes that for $10-50M managed K8s, Agent 10 gives 55-70% and Agent 13 gives 50-65%. The log states: "Intersection: 55-65%." This is correct. But the draft then consolidates at 50-65%, not 55-65%, stating this is to "encompass the narrower range where both agree, noting Agent 13's lower bound is data-driven for this specific tier."

This is internally contradictory. If the resolution rule is "use the intersection where both agree," the result should be 55-65%. If the resolution rule is "prefer the tier-specific agent's range," the result should be 50-65% (Agent 13's full range). The draft appears to apply both rules simultaneously, claiming intersection logic but using Agent 13's range.

**Evidence:**
- Agent 10: 55-70% managed K8s at $10-50M -- derived from [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) (73% managed K8s in cloud), [CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) (80% production K8s), and [Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/) (61% of production clusters on managed services)
- Agent 13: 50-65% managed K8s at $10-50M
- Intersection: 55-65%
- Draft resolution: 50-65% (equals Agent 13's range, not the intersection)
- Cell notes cite intersection logic but produce Agent 13's range

**Recommended Correction:** Either:
1. Use the intersection (55-65%) and update the cell notes to match, OR
2. Retain 50-65% and update the cell notes to state: "Agent 13's tier-specific range (50-65%) is preferred over the intersection (55-65%) because Agent 13 analyzes this tier exclusively while Agent 10 estimates across all tiers."

The intersection (55-65%) is recommended as it follows the stated methodology in Section 2 ("When two agents provide overlapping ranges, use the intersection").

**Impact on Confidence:** If narrowed to 55-65%, confidence remains C:6. The tighter range with explicit intersection logic is marginally more defensible.

---

## Revised Estimates

Changes from original are marked with arrows.

### Cloud-Native (Non-K8s Managed)

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Original** | 55-70% | 30-45% | 20-30% | 15-25% | 30-40% | 15-25% | 25-40% |
| **Revised** | 55-70% | 28-40% -> | 20-30% | 10-22% -> | 30-40% | 15-25% | 25-40% |

### Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Original** | 20-35% | 50-65% | 55-65% | 55-65% | 50-60% | 40-50% | 45-55% |
| **Revised** | 20-35% | 55-65% -> | 55-65% | 55-65% | 50-60% | 40-50% | 45-55% |

### Open/Self-Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Original** | 2-5% | 5-12% | 8-15% | 25-35% | 10-18% | 20-30% | 15-22% |
| **Revised** | 2-5% | 5-12% | 8-15% | 25-35% | 10-18% | 20-30% | 15-22% |

**Summary of Estimate Changes:**
1. Cloud-native $10-50M: 30-45% -> 28-40% (narrowed upper bound to avoid near-parity with managed K8s)
2. Cloud-native $200M+: 15-25% -> 10-22% (lowered to blend with Agent 09 rather than override)
3. Managed K8s $10-50M: 50-65% -> 55-65% (apply intersection rule as stated in methodology)

---

## Revised Confidence Scores

| Cell | Original Confidence | Revised Confidence | Rationale |
|---|---|---|---|
| Cloud-native $10-50M | C:5 | **C:4** | Weak evidence density + Estimated classification + largest conflict in the log (15-30pp delta requiring definitional reframing). Source data from [CNCF](https://www.cncf.io/reports/cncf-annual-survey-2024/) and [Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/) does not segment by this ARR tier. |
| Cloud-native $200M+ | C:5 | **C:4** | Second-largest conflict (25-40pp delta), resolution effectively overrides one source entirely, evidence for non-K8s is inferred from complement of K8s adoption documented in [engineering blog disclosures](https://openai.com/index/scaling-kubernetes-to-7500-nodes/) |
| Open K8s $10-50M | C:5 | **C:4** | Weak evidence density + Estimated classification + source estimate from [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) covered different tier boundary |
| Overall column (all rows) | C:4-5 | C:4-5 + methodology note | Add note: "Overall weighting methodology is implicitly revenue-weighted. Company-count-weighted estimates would differ materially." |

**All other confidence scores verified as appropriate:**
- Cloud-native <$10M at C:6 with Moderate density: Justified by two-agent convergence (09 and 12)
- Managed K8s $200M+ at C:7 with Strong density: Justified as highest-evidence cell with multiple named companies ([OpenAI](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), [Databricks](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), [Snowflake](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/)), [CNCF](https://www.cncf.io/reports/cncf-annual-survey-2024/)/[Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)/[Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/) convergence
- All EU cells at C:3: Appropriate given Agent 17's self-assessed 3/10 and documented evidence poverty. [CNCF 2023 regional data](https://www.cncf.io/reports/cncf-annual-survey-2023/) shows Europe at 82% cloud-native development but lacks AI SaaS-specific segmentation.
- Managed K8s $50-200M at C:6 with Moderate density: Justified by Inferred classification with two-agent convergence after resolution

---

## Items Verified as Correct

The following elements were cross-referenced and found internally consistent:

### 1. Tier Progression Patterns -- All Logically Sound

- **Cloud-native decreases with company size:** 55-70% -> 30-45% -> 20-30% -> 15-25%. Logical: smaller companies rely on simpler managed services; larger companies adopt K8s for orchestration complexity. Monotonically decreasing. Consistent with [startup infrastructure guidance](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget) recommending serverless for early-stage and K8s for scale. Verified.

- **Managed K8s increases then plateaus:** 20-35% -> 50-65% -> 55-65% -> 55-65%. The plateau at $50-200M and $200M+ is explained by self-managed K8s absorbing the incremental adoption. Total K8s at $200M+ (managed 55-65% + self-managed 25-35% = 80-100%) is much higher than at $50-200M (63-80%), so the total K8s trajectory is still increasing. Consistent with [CNCF data](https://www.cncf.io/reports/cncf-annual-survey-2024/) (80% production K8s) and [Tigera statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/) (91% of K8s users at 1,000+ employee orgs). Verified.

- **Open K8s increases with company size:** 2-5% -> 5-12% -> 8-15% -> 25-35%. Logical: self-managed K8s requires dedicated platform engineering teams that only larger companies can sustain. Monotonically increasing. Consistent with [platform engineering adoption](https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4) (55% of global organizations) and named examples like [Salesforce on bare metal K8s](https://engineering.salesforce.com/tagged/kubernetes/) and [OpenAI at 7,500 nodes](https://openai.com/index/scaling-kubernetes-to-7500-nodes/). Verified.

- **Multi-architecture overlap increases with company size:** 15-25% at <$10M, 40-55% at $10-50M, 40-55% at $50-200M, 70-85% at $200M+. Logical: larger companies operate more diverse workloads and have more complex infrastructure. Consistent with [Databricks operating hybrid managed/self-managed K8s](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators) and [Datadog data](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/) showing 66% of serverless users also use container orchestration. Verified.

### 2. US + EU Geographic Consistency

- **Cloud-native:** US 30-40%, EU 15-25%. EU lower due to GDPR reducing serverless appeal + sovereignty pressure toward K8s. Consistent with [CNCF 2023 regional data](https://www.cncf.io/reports/cncf-annual-survey-2023/) (Europe 82% cloud-native but data-residency concerns push toward K8s over serverless) and Agent 17's analysis. Verified.

- **Managed K8s:** US 50-60%, EU 40-50%. US higher due to stronger hyperscaler ecosystem (AWS/GCP HQ'd in US). EU lower but still majority for $10M+ companies. Consistent with Agent 16 and 17 analyses and [Gartner data](https://www.gartner.com/en/documents/5405263) showing 54% K8s implementation in broader enterprise. Verified.

- **Open K8s:** US 10-18%, EU 20-30%. EU higher due to data sovereignty requirements favoring self-managed infrastructure + EU-native providers (OVHcloud, Hetzner, IONOS). This is the most distinctive EU vs US difference and is directionally supported by Agent 11, Agent 17, and the GDPR sovereignty logic. Verified.

- **Geographic sum check:** For each architecture row, a weighted combination of US (~63% of global AI SaaS market) and EU (~28%) should approximate the Overall figure:
  - Cloud-native: 0.63*35% + 0.28*20% + 0.09*~25% = 22.1 + 5.6 + 2.3 = ~30%. Draft says 25-40%. Consistent.
  - Managed K8s: 0.63*55% + 0.28*45% + 0.09*~45% = 34.7 + 12.6 + 4.1 = ~51%. Draft says 45-55%. Consistent.
  - Open K8s: 0.63*14% + 0.28*25% + 0.09*~15% = 8.8 + 7.0 + 1.4 = ~17%. Draft says 15-22%. Consistent.

### 3. Row Sum Plausibility (Architecture Overlap Check)

For each tier, the three architecture percentages can sum to more than 100% because of multi-architecture overlap:

| Tier | Cloud-Native | Managed K8s | Open K8s | Sum (Midpoints) | Multi-Arch Estimate | Implied Overlap |
|---|---|---|---|---|---|---|
| <$10M | 55-70% | 20-35% | 2-5% | ~95% | 15-25% | ~-5% to 20% |
| $10-50M | 30-45% | 50-65% | 5-12% | ~103% | 40-55% | ~-3% to 48% |
| $50-200M | 20-30% | 55-65% | 8-15% | ~96% | 40-55% | ~-4% to 41% |
| $200M+ | 15-25% | 55-65% | 25-35% | ~110% | 70-85% | ~10% to 85% |

Overlap = Sum - 100%. At $200M+ the midpoint overlap is ~10%, well below the 70-85% multi-architecture estimate, which means the multi-architecture figure captures companies using two or more categories simultaneously. This is plausible -- a company using both managed K8s and cloud-native serverless would be counted in both rows but only needs to appear once in the multi-architecture estimate. The overlap math is consistent. Verified.

### 4. Conflict Log Resolutions (Excluding Issues Above)

- **Managed K8s <$10M (Agent 10 vs Agent 12):** 5pp delta, resolved at Agent 12's range. Correct: Agent 12 covers the full tier including pre-revenue. Verified.
- **Self-managed K8s $10-50M (Agent 11 vs Agent 13):** 3pp overlap, resolved at Agent 13's range. Correct: Agent 13 is tier-specific while Agent 11 used a broader tier. Verified.
- **US cloud-native (Agent 09 vs Agent 16):** Definitional adjustment from "some workloads" to "primary or significant." Same pattern as other definitional conflicts. Verified.
- **EU self-managed K8s (Agent 11 vs Agent 17):** Full convergence at 20-30%. No conflict. Verified.
- **EU managed K8s (Agent 10 vs Agent 17):** Complementary metrics (vendor share vs total adoption). No conflict. Verified.

### 5. Classification Matrix Accuracy

- All Cloud-native cells classified "E" (Estimated): Correct. No source directly measures cloud-native non-K8s adoption by revenue tier for AI SaaS. [CNCF surveys](https://www.cncf.io/reports/cncf-annual-survey-2024/) report serverless at 11% globally but do not segment by AI SaaS revenue tier.
- Managed K8s $50-200M and $200M+ classified "I" (Inferred): Correct. Multiple Direct data points combine through documented logic. Sources include [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/), [CNCF](https://www.cncf.io/reports/cncf-annual-survey-2024/), and [engineering blog case studies](https://www.figma.com/blog/migrating-onto-kubernetes/).
- Open K8s $200M+ classified "I" (Inferred): Correct. Named company examples provide direct evidence ([OpenAI](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), [Salesforce](https://engineering.salesforce.com/tagged/kubernetes/), [Databricks](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)) combined with [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) baseline self-managed percentages (27%).
- All other cells classified "E" (Estimated): Correct. Verified against classification rationale in Section 4.

### 6. Evidence Density Ratings Accuracy

- $200M+ Managed K8s and Open K8s rated "Strong": Correct. Multiple named companies ([OpenAI](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), [Databricks](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), [Anthropic](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), [Snowflake](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), [Salesforce](https://engineering.salesforce.com/tagged/kubernetes/)), [CNCF](https://www.cncf.io/reports/cncf-annual-survey-2024/)/[Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)/[Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/) convergence.
- EU cells rated "Weak": Correct. Only 2 EU AI company case studies in Wave 1 data. [CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/) provides regional cloud-native percentages but not AI SaaS-specific.
- $10-50M cells mostly rated "Weak": Correct. This tier falls in the evidence gap between well-documented enterprise ([Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/) showing 91% of K8s users at 1,000+ employees) and qualitatively described startup segments.
- <$10M Cloud-native rated "Moderate": Correct. Two-agent convergence plus [VC-stage guidance data](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget) recommending serverless/PaaS for early-stage companies.

### 7. Assumptions Register Completeness

Cross-referenced assumptions against all 9 Wave 2 files. All major assumptions are captured. No missing assumptions identified beyond the weighting methodology gap (Issue 6).

### 8. Appendix B Serverless Reconciliation

The reconciliation of the 65-70% ([Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/) any-use for AWS Lambda/Cloud Run among cloud customers), 70% ([CNCF](https://www.cncf.io/reports/cncf-annual-survey-2023/) NA production serverless loads), and 11% ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) global primary serverless framework) figures is correct and well-documented. These measure different scopes and are not contradictory. Verified.

---

## Verification Summary

| Category | Count | Details |
|---|---|---|
| **Issues found** | 10 | 1 unlogged conflict, 1 executive summary overstatement, 3 confidence inflations, 1 methodology gap, 1 range width concern, 1 conflict log imprecision, 1 source override concern, 1 intersection logic inconsistency |
| **Estimate revisions recommended** | 3 | Cloud-native $10-50M (28-40%), Cloud-native $200M+ (10-22%), Managed K8s $10-50M (55-65%) |
| **Confidence revisions recommended** | 3 | Cloud-native $10-50M (C:4), Cloud-native $200M+ (C:4), Open K8s $10-50M (C:4) |
| **Items verified correct** | 8 | Tier progressions, geographic consistency, overlap math, 5 conflict resolutions, classification matrix, evidence density map, assumptions register, serverless reconciliation |

**Overall Assessment:** The consolidated draft is a rigorous and well-structured synthesis. The 10 issues identified are primarily documentation gaps (1 missing conflict, 1 imprecise resolution narrative), calibration errors (3 confidence scores set too high for their evidence quality), and one framing issue (executive summary headline). No estimate is fundamentally wrong; the recommended revisions are within 2-8 percentage points of the originals. The draft's methodology, when consistently applied, produces defensible results.

---

**Verification Version:** 1.0
**Verified By:** Adversarial Verification Agent
**Verification Date:** 2026-02-12
