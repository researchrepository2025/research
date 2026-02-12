# Adversarial Gap Analysis: Consolidated Estimate Matrix

**Analysis Date:** 2026-02-12
**Role:** Adversarial Verification Agent
**Input:** research/ai_saas_infra_architecture/consolidated/18_consolidated_draft.md
**Supporting Evidence Reviewed:** All 9 Wave 2 files (09-17), all 8 Wave 1 files (01-08)

---

## Executive Summary

The consolidated draft is commendably transparent about its limitations, but the analysis understates the severity of several evidence gaps. **Zero cells in the 21-cell estimate matrix have Direct evidence.** Only 3 cells achieve Inferred classification; the remaining 18 are Estimated. Of the 21 cells, 8 are rated "Weak" in evidence density, meaning they rest on a single indirect source or pure estimation. The six EU Avg cells (across all three architectures) are the weakest in the matrix, each depending on a single Wave 2 analysis file (Agent 17) that self-reports 3/10 confidence and draws from only 2 EU-specific case studies across all of Wave 1. Furthermore, the draft systematically extrapolates from general enterprise populations to AI SaaS companies without always flagging the inference gap, and from US-sourced data to EU patterns without adequate acknowledgment that US and EU AI SaaS ecosystems may differ structurally (not just by the 5-15pp adjustment applied). Five cells should have their confidence scores lowered, and all tier-specific cells should be presented as ranges with explicit uncertainty bounds rather than central estimates.

---

## 1. Issues Found

### Issue 1: No Cell Has Direct Evidence -- But Classification Matrix Understates This

**Location:** Section 4 (Classification Matrix), all cells

**Problem:** The consolidated draft correctly states "No cell achieves Direct classification" (line 144). However, the 3 cells classified as Inferred ($50-200M and $200M+ Managed K8s, $200M+ Self-Managed K8s) are closer to Estimated than the label implies. The "Inferred" classification requires "derived through documented logical steps from direct data." But the chain from CNCF 80% K8s production ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/), general enterprise, n=750) to Dynatrace 73% managed ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/), general enterprise) to AI SaaS specifically requires an untested assumption (X2: "AI SaaS companies are more cloud-native than the average enterprise"). This is not a documented logical step -- it is an assumption-based adjustment.

**Evidence:** Agent 10 (Managed K8s deep dive) acknowledges this: "No source directly segments managed K8s vendor share among AI SaaS companies" (Gap G1). The 60-70% managed K8s estimate for >$10M ARR is explicitly classified as "Estimated (judgment + reasoning from multiple data points)" in Agent 10's own analysis. The consolidator upgraded it to Inferred for the $50-200M and $200M+ cells, but the upgrade is not fully justified.

**Recommended Correction:** Reclassify Managed K8s $50-200M from Inferred to Estimated. Retain Inferred for Managed K8s $200M+ and Self-Managed K8s $200M+ only, noting that these cells have named company examples that provide partial Direct evidence.

**Impact on Confidence:** Managed K8s $50-200M should drop from C:6 to C:5. The Inferred label creates a false sense of precision.

---

### Issue 2: EU Cells Rest on a Single Analysis Agent with 3/10 Self-Reported Confidence

**Location:** All EU Avg cells (Cloud-native EU: C:3, Managed K8s EU: C:3, Self-Managed K8s EU: C:3)

**Problem:** All six EU cells across the three architecture rows flow from a single Wave 2 analysis (Agent 17, file 17_eu_market.md). Agent 17 explicitly states: "Almost no direct EU AI SaaS infrastructure data exists. Wave 1 files contain exactly two EU-based AI/ML company case studies (Stacks on GKE Autopilot ([Google Cloud Customers - Stacks](https://cloud.google.com/customers/stacks)), Medigold on Azure OpenAI ([Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/))) and one EU infrastructure mention (HubSpot EU datacenter ([CNCF Case Study - HubSpot](https://www.cncf.io/case-studies/hubspot/)))." Agent 17 self-rates at 3/10 confidence. The consolidated draft assigns C:3 to all EU cells, which is appropriate, but the draft then uses these cells in narrative conclusions (Executive Summary point 4: "EU shows 5-15 percentage points higher Kubernetes adoption") as though the finding has moderate reliability.

**Evidence:** Agent 17's evidence chain for the 5-15pp EU K8s premium rests on: (a) CNCF regional cloud-native maturity data (82% EU vs 70% Americas) ([CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)), which measures cloud-native development intensity, not K8s adoption specifically; (b) a structural argument about GDPR favoring K8s; (c) a single EU startup (Stacks) choosing GKE ([Google Cloud Customers - Stacks](https://cloud.google.com/customers/stacks)). The chain from "higher cloud-native development intensity" to "higher K8s adoption among AI SaaS" requires two untested inference steps.

**Recommended Correction:** Add explicit caveats to Executive Summary point 4: "EU shows 5-15 percentage points higher Kubernetes adoption -- **however, this finding rests on the weakest evidence in the entire analysis (2 EU case studies, self-reported 3/10 confidence) and should be treated as a directional hypothesis, not a finding.**" Consider removing specific percentage-point differentials from the EU cells and replacing with qualitative directional statements.

**Impact on Confidence:** No score change needed (already C:3), but the narrative framing should match the evidence quality.

---

### Issue 3: Population Extrapolation -- General Enterprise to AI SaaS

**Location:** All 21 cells, but most severe in Overall and US Avg columns

**Problem:** The primary data sources (CNCF surveys ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), Dynatrace telemetry ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), Gartner reports ([Gartner Cloud Survey](https://www.gartner.com/en/documents/5405263))) measure general enterprise populations, not AI SaaS companies specifically. The draft acknowledges this (Assumption X2: "AI SaaS companies are more cloud-native than the average enterprise"), but does not consistently flag where extrapolation occurs. Specific instances:

**(a) CNCF 80% K8s production adoption to AI SaaS K8s adoption:** The CNCF figure comes from self-selected cloud-native practitioners (n=750) ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)). Gartner's broader enterprise sample shows 54% ([Gartner Cloud Survey](https://www.gartner.com/en/documents/5405263)). The draft uses an intermediate value for AI SaaS, but the adjustment magnitude is judgment-based. AI SaaS companies range from API-wrapper startups (which may not need K8s at all) to model-hosting companies (which almost certainly use K8s). Without knowing the API-wrapper vs model-hosting split by tier, the adjustment is ungrounded.

**(b) Dynatrace 73% managed K8s to AI SaaS managed K8s:** Dynatrace observability data covers all cloud K8s clusters ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)). AI SaaS companies may have different managed/self-managed ratios due to GPU scheduling requirements. The draft applies this figure without AI SaaS-specific adjustment.

**(c) Employee count to revenue tier mapping:** Assumption X4 maps employee count to revenue tiers using "$200K-$500K ARR per employee." AI SaaS companies -- especially model-hosting ones -- may have different revenue-per-employee ratios. Compute-heavy companies can have high revenue with smaller teams. This mapping error propagates through all tier-specific cells.

**Evidence:** Agent 12 (<$10M tier) explicitly notes: "CNCF data does not measure companies under 500 employees" ([Tigera Kubernetes Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/); [CommandLinux Kubernetes Statistics](https://commandlinux.com/statistics/linux-container-kubernetes-adoption-statistics/)) (Evidence Gap 2). Agent 13 ($10-50M tier) notes: "K8s adoption data stops at 500-1,000 employees. Companies at $10-50M ARR (80-300 employees) are below the measurement threshold" (Evidence Gap 5).

**Recommended Correction:** Add a standardized caveat to every tier-specific cell: "Extrapolated from general enterprise data; no AI SaaS-specific measurement exists." Consider adding a "Population Extrapolation Risk" column to the estimate matrix.

**Impact on Confidence:** All tier-specific cells should note +/-10pp uncertainty from population extrapolation alone.

---

### Issue 4: US Data Used for Overall Estimates Without Adequate Geo-Weighting

**Location:** Overall column (all three architectures)

**Problem:** The Overall estimates (Cloud-native 25-40%, Managed K8s 45-55%, Self-managed K8s 15-22%) are implicitly US-centric because Wave 1 data is predominantly US-sourced. The draft's Overall column does not specify a geographic scope. Is it global? US+EU? The absence of specification means readers may interpret it as global, but the evidence base is approximately 85%+ US-originated.

Agent 17 (EU market) documents: "Wave 1 data has documented US/Americas bias" across jobs data (66-70% North America), engineering blogs (near 100% US companies) ([Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/); [OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/); [Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), SEC filings (100% US), and VC data (100% US). If the Overall column is meant to represent "global AI SaaS," the EU, APAC, and other regions are barely represented.

**Evidence:** The Known Limitations section (item 11) states: "US-centric source bias is pervasive." But this limitation is not reflected in how the Overall column is computed or labeled.

**Recommended Correction:** Rename the "Overall" column to "Overall (US-weighted)" or add a footnote: "Overall estimates are derived primarily from US-sourced data and may not reflect global AI SaaS patterns." Alternatively, present Overall as a simple weighted average of US Avg and EU Avg with stated weights.

**Impact on Confidence:** Overall column confidence should not exceed US Avg confidence (C:5 for Cloud-native, C:5 for Managed K8s, C:4 for Self-managed K8s). Currently, Overall for Cloud-native is C:4 while US Avg is C:5, which is inverted.

---

### Issue 5: Cloud-Native Non-K8s Is Defined by Exclusion, Not Measurement

**Location:** All Cloud-native (non-K8s) cells

**Problem:** The Cloud-native non-K8s architecture category is the hardest to estimate because it is defined negatively (everything cloud-native that is NOT Kubernetes). Agent 09 (Cloud-native deep dive) self-reports 4/10 confidence and describes its core methodology as "gap analysis" -- i.e., "if X% use K8s, then (100-X)% might use non-K8s." This inverse logic is fragile because the remainder includes:
- Companies using VMs (not cloud-native)
- Companies not yet containerized
- Companies using managed ML services (SageMaker, Vertex AI) that blur the K8s/non-K8s boundary
- Companies using hybrid architectures that defy clean categorization

The draft acknowledges this ("Heavy reliance on gap analysis") but does not adjust confidence scores for Cloud-native cells accordingly. All 7 Cloud-native cells are classified as Estimated with evidence densities of Weak to Moderate, yet the confidence scores (C:3 to C:6) are not uniformly lower than Managed K8s cells despite having weaker evidence.

**Evidence:** Agent 09 states: "Unlike Kubernetes adoption (measured by CNCF ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), Datadog ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)), Red Hat ([Red Hat Kubernetes Adoption Survey](https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview)), Gartner ([Gartner Cloud Survey](https://www.gartner.com/en/documents/5405263))), cloud-native non-K8s adoption for AI SaaS has no dedicated survey or telemetry source."

**Recommended Correction:** Lower Cloud-native <$10M from C:6 to C:5. Lower Cloud-native $200M+ from C:5 to C:4. Add a note to the Cloud-native row: "This architecture category is measured indirectly by subtracting K8s adoption from total cloud-native adoption; all estimates carry an additional +/-10pp uncertainty from this indirect measurement method."

**Impact on Confidence:** Two cells need confidence score reductions.

---

### Issue 6: Migration Direction Evidence Suffers from Severe Publication Bias

**Location:** Executive Summary point 6, Finding 8 in Agent 09, Section 6 in Agent 11

**Problem:** The draft presents migration direction as a strong finding: "Four independent engineering blog disclosures document migrations toward K8s... Zero counter-migrations documented." The four documented migrations are: Figma ECS-to-EKS ([Figma Engineering Blog](https://www.figma.com/blog/migrating-onto-kubernetes/)), Grammarly EC2-to-EKS ([Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), HubSpot EC2-to-K8s ([CNCF Case Study - HubSpot](https://www.cncf.io/case-studies/hubspot/)), and Salesforce Data Cloud EC2-to-K8s ([Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/)). The draft adds the caveat "though publication bias likely suppresses negative cases." However, this caveat understates the severity.

Publication bias in engineering blogs is not symmetric. Companies publish blogs about:
- Successful adoptions of popular technologies (K8s is popular, generates conference talks)
- Migrations that improved metrics (cost, reliability, developer experience)

Companies almost never publish about:
- Abandoning a popular technology (invites criticism, signals poor decision-making)
- Staying on "boring" infrastructure (ECS, Fargate, Lambda) because it works fine
- Failed K8s migrations (implies engineering failure)

The 4-to-0 ratio (toward K8s vs away from K8s) is therefore an artifact of the publication incentive structure, not necessarily a reliable measure of actual migration patterns. The true ratio could be 4:2 or 4:4, with the counter-migrations simply unpublished.

**Evidence:** Agent 09 (Assumption A7) rates this assumption's confidence as "Medium" but provides no basis for the medium rating. Agent 11 (Assumption A7) rates confidence as "Low." The draft should use the lower rating.

**Recommended Correction:** Change the migration direction finding from "strongly AWAY FROM" to "net direction likely toward K8s, but the magnitude is unknown due to severe publication bias." Downgrade the migration trend confidence from the implied 7/10 to 5/10.

**Impact on Confidence:** Affects the narrative framing rather than specific cell confidence scores, but reduces confidence in all tier-specific estimates that use migration trends as supporting evidence.

---

### Issue 7: $10-50M Tier Has a 30pp Conflict That Was Resolved by Averaging

**Location:** Cloud-native $10-50M cell, Conflict Log row 1

**Problem:** Agent 09 estimates 15-30% for Cloud-native at Growth Stage, while Agent 13 estimates 45-60%. The conflict resolution states that Agent 09 measures "primary architecture" while Agent 13 measures "used for some production workloads." The consolidation resolves this at 30-45% for "primary or significant."

This resolution introduces a new definitional category ("primary or significant") that neither agent used. The framing is itself an assumption -- "significant" is undefined. A company running 5% of workloads on Lambda alongside K8s could be counted as "significant" or not, depending on interpretation. The 30-45% range sits exactly between the two agents' estimates, suggesting the resolution was a mechanical average rather than an evidence-based determination.

**Evidence:** The Conflict Log documents the issue transparently, but the resolution does not cite additional evidence to justify 30-45% over either agent's original range.

**Recommended Correction:** Widen the range to 20-50% to encompass both agents' estimates, or explicitly define "primary or significant" with a threshold (e.g., ">20% of production compute") and re-derive the estimate under that definition.

**Impact on Confidence:** Cloud-native $10-50M should remain at C:5 or drop to C:4 given the unresolved definitional ambiguity.

---

### Issue 8: Multi-Architecture Overlap Means Columns Do Not Sum to 100%

**Location:** All rows of the Primary Estimate Matrix

**Problem:** The three architecture rows are explicitly non-exclusive (companies use multiple architectures). The draft notes this in specific places but does not provide a reconciliation showing how the non-exclusive percentages map to the actual architecture landscape. For example, at $200M+ ARR:
- Cloud-native non-K8s: 15-25%
- Managed K8s: 55-65%
- Self-managed K8s: 25-35%

These sum to 95-125%, implying 0-25% overlap. But Agent 15 ($200M+ tier) separately estimates "70-85% of companies in this tier run multiple architecture patterns simultaneously." If 70-85% use multiple architectures and the sum is 95-125%, the overlap is concentrated in a large majority of companies. The lack of an explicit overlap model makes it difficult to assess whether the individual cell estimates are internally consistent.

**Evidence:** Agent 13 ($10-50M tier) estimates 40-55% multi-architecture usage. Agent 12 (<$10M tier) estimates 15-25%. These overlap rates have their own uncertainty but are not integrated into the primary matrix. The Datadog finding that "66% of organizations using serverless functions also use container orchestration" ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)) provides direct evidence of multi-architecture overlap.

**Recommended Correction:** Add a fourth row to the estimate matrix: "Multi-architecture overlap %" by tier. This would allow readers to check whether the three architecture rows are mutually consistent.

**Impact on Confidence:** Internal consistency check. If the implied overlap exceeds the estimated multi-architecture rate, some cells need adjustment.

---

### Issue 9: Temporal Mismatch in Source Data

**Location:** All cells, but particularly those citing CNCF and Dynatrace data

**Problem:** The estimate matrix is dated 2026-02-12, but key underlying data sources span 2021-2025:
- CNCF managed K8s provider breakdown: **2021** (5 years old) ([CNCF Annual Survey 2021](https://www.cncf.io/announcements/2022/02/10/cncf-sees-record-kubernetes-and-container-adoption-in-2021-cloud-native-survey/))
- Dynatrace 73% managed K8s: **2023** (3 years old) ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/))
- Datadog 90% managed K8s: **2021** (5 years old) ([Datadog Container Report 2021](https://www.datadoghq.com/container-report-2021/))
- CNCF 80% K8s production: **2024** (2 years old) ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/))
- Gartner 54% K8s implementation: **2025** (1 year old) ([Gartner Cloud Survey](https://www.gartner.com/en/documents/5405263))

The draft acknowledges temporal risk (Known Limitation 10: "All estimates reflect 2024-2025 data") but then states the managed K8s trend direction justifies using older data. However, managed K8s adoption has been accelerating (45% cloud-hosted in 2022 to 67% in 2025 ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/); [Tigera Kubernetes Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/))). Extrapolating 2023 Dynatrace data to 2026 could underestimate managed K8s adoption by 5-10pp.

**Recommended Correction:** Add a "Data Currency" column to the evidence density map noting the most recent source year for each cell. Flag cells where the primary evidence is more than 2 years old.

**Impact on Confidence:** Minor for directional findings; moderate for specific percentage estimates.

---

### Issue 10: The API-Wrapper vs Model-Hosting Split Is Unquantified but Decisive

**Location:** All tier-specific cells

**Problem:** The draft repeatedly identifies the API-wrapper vs model-hosting distinction as critical: API-wrapper companies (calling OpenAI/Anthropic APIs) need minimal infrastructure and rarely use K8s; model-hosting companies need GPU orchestration and almost always use K8s. Assumption X7 rates this as "High" impact. Yet no source quantifies this split by tier.

Agent 02 (analyst reports) provides the only data point: "37% using managed APIs, 25% self-hosting, 13% at the edge" for AI/ML model hosting ([CNCF Annual Cloud Native Survey 2025](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)). But this is not segmented by company size, revenue tier, or AI SaaS specifically. The split almost certainly varies dramatically by tier: most sub-$10M companies likely call APIs, while most $200M+ companies likely self-host.

If the actual split is, for example, 80% API-wrapper at <$10M vs 20% API-wrapper at $200M+, the architecture estimates would shift substantially: K8s adoption at <$10M would be lower than estimated (perhaps 10-20% instead of 20-35%), and cloud-native non-K8s at $200M+ would be lower than estimated (perhaps 5-10% instead of 15-25%).

**Recommended Correction:** Add the API-wrapper vs model-hosting assumption as an explicit sensitivity parameter in each tier cell. State: "These estimates assume approximately X% API-wrapper at this tier; if the actual split is Y%, estimates shift by Z pp."

**Impact on Confidence:** This is the single largest unquantified assumption. All tier-specific cells carry +/-10-15pp uncertainty from this source alone.

---

## 2. Cell Ranking by Evidence Strength

All 21 cells ranked from strongest to weakest evidence, considering: number of independent sources, directness of evidence, presence of named company examples, and self-reported confidence from source agents.

| Rank | Cell | Classification | Evidence Density | Confidence | Source Count | Key Justification |
|------|------|----------------|------------------|------------|-------------|-------------------|
| 1 | Managed K8s, $200M+ | I | Strong | C:7 | 4+ | Named companies (Anthropic/GKE ([Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/)), Snowflake/EKS ([AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/)), Notion/EKS ([Notion Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake)), Figma/EKS ([Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/))), CNCF/Dynatrace convergence, SEC filing infrastructure signals |
| 2 | Self-managed K8s, $200M+ | I | Strong | C:6 | 4+ | Named companies (OpenAI 7500 nodes ([OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)), Databricks hybrid ([Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)), Salesforce bare metal ([Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/)), HubSpot ([CNCF Case Study](https://www.cncf.io/case-studies/hubspot/))), Dynatrace 27% self-managed baseline ([Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)) |
| 3 | Managed K8s, $10-50M | E | Moderate | C:6 | 2-3 | CNCF/Dynatrace convergence ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/); [Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), Agent 10 and 13 overlap at 55-65%, case studies (Jasper ([Jasper Blog](https://www.jasper.ai/blog/devx-renaissance-the-death-of-devops)), Cohere ([Oracle Case Study](https://www.oracle.com/cloud/technical-case-studies/cohere/))) near this tier |
| 4 | Managed K8s, $50-200M | I | Moderate | C:6 | 2-3 | Dynatrace 73% managed applied to tier ([Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)); Figma/Grammarly/Notion case studies ([Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/); [Grammarly Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/); [Notion Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake)); Agent 10/14 convergence after reconciliation |
| 5 | Cloud-native, <$10M | E | Moderate | C:6 | 2 | VC stage guidance (Maven Solutions, SaaStr ([SaaStr](https://www.saastr.com/is-there-a-benchmark-for-of-revenue-that-an-enterprise-saas-business-should-spend-on-systems-infrastructures-like-aws-or-the-equivalent/))), CNCF small company exclusion (91% K8s users at 1000+ employees ([Tigera Kubernetes Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/))), Agents 09/12 converge |
| 6 | Cloud-native, $200M+ | E | Moderate | C:5 | 2 | Agent 09 (5-15% primary) and Agent 15 (40-55% any use) provide different measures; Datadog serverless telemetry supports complementary usage ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)) |
| 7 | Managed K8s, <$10M | E | Weak | C:5 | 1-2 | Agent 10/12 converge at 20-35%; Stacks (GKE ([Google Cloud Customers - Stacks](https://cloud.google.com/customers/stacks))) and Sonantic (EKS ([Bion Consulting Case Study](https://www.bionconsulting.com/case-studies/scaling-ai-driven-voice-technology-with-aws-and-eks))) are only named examples at this tier |
| 8 | Self-managed K8s, <$10M | E | Moderate | C:5 | 2 | Agent 11/12 converge at 2-5%; strong structural argument (team size, expertise requirements) |
| 9 | Self-managed K8s, $10-50M | E | Weak | C:5 | 1-2 | Agent 11/13 overlap; no named companies at this exact tier self-managing K8s |
| 10 | Cloud-native, US Avg | E | Moderate | C:5 | 2 | Agent 16 provides US-weighted estimate; Datadog Lambda 65% corroborates broad serverless usage ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)); CNCF 70% NA serverless ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) |
| 11 | Managed K8s, US Avg | E | Moderate | C:5 | 2 | Agent 16 estimates 55-65% for $10M+; adjusted to 50-60% including sub-$10M; CNCF/case study support ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) |
| 12 | Managed K8s, Overall | E | Moderate | C:5 | 2 | Tier-weighted average; Gartner 54% provides external anchor ([Gartner Cloud Survey](https://www.gartner.com/en/documents/5405263)); CNCF data after bias discount ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) |
| 13 | Cloud-native, $10-50M | E | Weak | C:5 | 1 | 30pp conflict between agents; resolution by definitional compromise; single tier without named non-K8s companies |
| 14 | Cloud-native, Overall | E | Moderate | C:4 | 2 | Derived by subtraction from K8s estimates; Agent 09 headline 25-40%; Gartner gap (100%-54%=46% non-K8s or non-cloud-native) ([Gartner Cloud Survey](https://www.gartner.com/en/documents/5405263)) |
| 15 | Self-managed K8s, Overall | E | Moderate | C:4 | 2 | Agent 11 headline 15-22%; Dynatrace 27% self-managed baseline discounted for AI SaaS company size distribution ([Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)) |
| 16 | Cloud-native, $50-200M | E | Weak | C:4 | 1 | Agent 09 (10-20%) and Agent 14 (25-35%) conflict; no named AI SaaS companies at this tier using non-K8s as primary |
| 17 | Self-managed K8s, $50-200M | E | Weak | C:4 | 1 | Agent 11 gives broad range for $10-200M combined (8-15%); no named self-managed companies at this specific tier |
| 18 | Self-managed K8s, US Avg | E | Weak | C:4 | 1 | Agent 16 estimates 10-18%; derived from global self-managed data minus EU premium; no US-specific measurement |
| 19 | Cloud-native, EU Avg | E | Weak | C:3 | 1 | Agent 17 only; structural argument (no EU serverless providers); 2 EU case studies total; 3/10 self-confidence |
| 20 | Managed K8s, EU Avg | E | Weak | C:3 | 1 | Agent 17 only; AKS EU enterprise strength is inferred from general enterprise data; no EU AI SaaS K8s adoption data |
| 21 | Self-managed K8s, EU Avg | E | Weak | C:3 | 1 | Agent 17 only; GDPR sovereignty argument is structural, not empirical; convergence with Agent 11 at 20-30% but from same reasoning chain |

---

## 3. Sensitivity Analysis: Five Weakest Cells

### Cell 19: Cloud-native, EU Avg (15-25%, C:3)

**Base Estimate:** 15-25% of EU AI SaaS companies use cloud-native non-K8s as primary or significant architecture.

| Scenario | Assumption Change | Revised Estimate | Delta |
|----------|-------------------|------------------|-------|
| A: GDPR does NOT disadvantage serverless | GDPR equally served by serverless with proper configuration (Assumption A2 wrong) | 25-35% | +10pp |
| B: EU cloud adoption catches US | EU enterprise cloud at 60% (vs 45.2% Eurostat 2023 ([Eurostat](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20231208-1))), closing gap | 20-30% | +5pp |
| C: EU follows US startup patterns | EU seed-stage AI SaaS uses PaaS/serverless at same rate as US (Assumption A8 wrong) | 25-40% (matches US) | +10-15pp |
| D: Sovereignty drives EU to on-prem, not K8s | EU companies use VMs/bare metal for sovereignty, not K8s | 20-30% | +5pp (some shift from K8s to non-cloud-native, not to cloud-native non-K8s) |
| E: Base case holds | GDPR + sovereignty pressure + no EU serverless providers | 15-25% | 0 |

**Key Sensitivity:** This cell is most sensitive to Assumption A2 (GDPR favors K8s). If GDPR compliance is equally achievable on serverless, the EU estimate converges toward the US estimate, and the 5-15pp differential disappears.

---

### Cell 20: Managed K8s, EU Avg (40-50%, C:3)

**Base Estimate:** 40-50% of EU AI SaaS companies use managed K8s.

| Scenario | Assumption Change | Revised Estimate | Delta |
|----------|-------------------|------------------|-------|
| A: EU cloud-native maturity does NOT translate to higher K8s | 82% cloud-native figure ([CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)) reflects non-K8s cloud adoption too | 35-45% | -5pp |
| B: AKS EU enterprise dominance overstated | AKS strength is in traditional enterprise, not AI SaaS | 35-45% | -5pp |
| C: EU sovereignty pushes more to self-managed | Self-managed K8s captures 30-40% instead of 20-30% | 35-45% | -5pp (transferred to self-managed) |
| D: EU AI SaaS is smaller/earlier-stage than assumed | Fewer EU companies at $50M+ ARR where K8s dominates | 30-40% | -10pp |
| E: Base case holds | AKS + GKE EU strength + 82% cloud-native maturity ([CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)) | 40-50% | 0 |

**Key Sensitivity:** This cell is most sensitive to whether the CNCF 82% EU cloud-native figure ([CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)) translates specifically to K8s adoption among AI SaaS. If EU cloud-native maturity manifests as PaaS or managed ML services rather than K8s, the estimate drops.

---

### Cell 21: Self-managed K8s, EU Avg (20-30%, C:3)

**Base Estimate:** 20-30% of EU AI SaaS companies use self-managed K8s.

| Scenario | Assumption Change | Revised Estimate | Delta |
|----------|-------------------|------------------|-------|
| A: EU companies use EU-region managed K8s instead | GKE Frankfurt, AKS EU sovereign satisfy sovereignty needs | 10-18% (converges to US) | -10-12pp |
| B: EU AI SaaS is more cloud-first than assumed | EU AI startups behave like US startups on managed infrastructure | 10-15% | -10-15pp |
| C: CLOUD Act concern intensifies | Schrems III-type ruling invalidates EU-US data framework | 30-40% | +10pp |
| D: On-prem K8s is actually VM-based, not K8s | EU companies use VMs for sovereignty, not self-managed K8s | 10-20% | -10pp |
| E: Base case holds | GDPR + Gaia-X + EU-native providers drive self-management | 20-30% | 0 |

**Key Sensitivity:** This cell's most critical assumption is that sovereignty requirements translate to self-managed K8s rather than managed K8s in EU-sovereign regions. If hyperscaler sovereign cloud offerings (AWS European Sovereign Cloud, Azure sovereign regions) satisfy EU requirements, the self-managed premium over US rates largely disappears. A Gartner survey found 61% of Western European CIOs plan to increase reliance on local cloud providers, driven by sovereignty concerns ([Gartner Survey November 2025](https://www.gartner.com/en/newsroom/press-releases/2025-11-12-gartner-survey-reveals-geopolitics-will-drive-61-percent-of-cios-and-information-technology-leaders-in-western-europe-to-increase-reliance-on-local-cloud-providers)).

---

### Cell 16: Cloud-native, $50-200M (20-30%, C:4)

**Base Estimate:** 20-30% of AI SaaS companies at $50-200M use cloud-native non-K8s as primary or significant.

| Scenario | Assumption Change | Revised Estimate | Delta |
|----------|-------------------|------------------|-------|
| A: More companies are API-wrappers at this tier | 50% are API-wrapper (vs assumed ~30%), reducing K8s need | 30-40% | +10pp |
| B: Companies on non-K8s at this tier are there by inertia, not choice | Assumption T5 is wrong; some have not yet migrated | 25-35% | +5pp (higher, but less deliberate) |
| C: GPU serverless matures | Cloud Run/Azure Container Apps GPU support becomes sufficient for inference | 25-35% | +5pp |
| D: All companies at this tier have migrated to K8s | Migration pressure is stronger than estimated; non-K8s is lower | 10-20% | -10pp |
| E: Base case holds | Mix of API-wrappers and deliberate non-K8s architects | 20-30% | 0 |

**Key Sensitivity:** Most sensitive to the API-wrapper vs model-hosting split. If more companies at this tier are API-wrappers than assumed, cloud-native non-K8s adoption would be higher because these companies have no GPU orchestration need. The CNCF survey finding that 37% of organizations use managed APIs for AI/ML model hosting ([CNCF Annual Cloud Native Survey 2025](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)) provides the only available data point on this split.

---

### Cell 17: Self-managed K8s, $50-200M (8-15%, C:4)

**Base Estimate:** 8-15% of AI SaaS companies at $50-200M use self-managed K8s.

| Scenario | Assumption Change | Revised Estimate | Delta |
|----------|-------------------|------------------|-------|
| A: Platform engineering teams at this tier are larger | 8-15 infra engineers (vs assumed 5-15), enabling self-management | 12-20% | +4-5pp |
| B: GPU cloud alternatives (CoreWeave) classified as self-managed | CoreWeave/Lambda Labs users counted as self-managed | 12-20% | +4-5pp |
| C: K8s-native GPU clouds classified as managed | Reclassifying CoreWeave as managed reduces self-managed | 5-10% | -3-5pp |
| D: On-prem deployment for regulated customers drives self-managed | More healthcare/fintech AI SaaS at this tier | 12-18% | +4-3pp |
| E: Base case holds | Small platform teams + managed K8s economics favor managed | 8-15% | 0 |

**Key Sensitivity:** Most sensitive to the CoreWeave/GPU cloud classification (Assumption OK3). These platforms are hybrid -- customers interact with K8s directly but the control plane is managed. Classification choice shifts the estimate by 5-10pp.

---

## 4. Revised Confidence Scores

| Cell | Architecture | Tier/Geo | Draft Confidence | Revised Confidence | Justification |
|------|-------------|----------|------------------|-------------------|---------------|
| 1 | Cloud-native | <$10M | C:6 | **C:5** | Defined by exclusion, not measurement; relies on inverting enterprise K8s data for small companies where no data exists ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) reports 91% of K8s users at 1000+ employees ([Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/))) |
| 2 | Cloud-native | $10-50M | C:5 | C:5 | Retains score; 30pp agent conflict partially mitigated by definitional clarification |
| 3 | Cloud-native | $50-200M | C:4 | C:4 | Retains score; Weak evidence density acknowledged |
| 4 | Cloud-native | $200M+ | C:5 | **C:4** | "Any use" vs "primary" ambiguity unresolved; no named AI SaaS company at this tier uses non-K8s as primary |
| 5 | Cloud-native | US Avg | C:5 | C:5 | Retains score; Datadog telemetry provides reasonable anchor ([Datadog 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)) |
| 6 | Cloud-native | EU Avg | C:3 | C:3 | Retains score; already at appropriate level for evidence available |
| 7 | Cloud-native | Overall | C:4 | C:4 | Retains score; should not exceed US Avg given US-weighted source base |
| 8 | Managed K8s | <$10M | C:5 | C:5 | Retains score; wide range (20-35%) appropriately reflects uncertainty |
| 9 | Managed K8s | $10-50M | C:6 | C:6 | Retains score; two agents converge; case study support ([Jasper](https://www.jasper.ai/blog/devx-renaissance-the-death-of-devops); [Cohere/Oracle](https://www.oracle.com/cloud/technical-case-studies/cohere/)) |
| 10 | Managed K8s | $50-200M | C:6 | **C:5** | Should be reclassified from Inferred to Estimated; the chain from general K8s to AI SaaS managed K8s is assumption-dependent ([Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) measures general enterprise, not AI SaaS) |
| 11 | Managed K8s | $200M+ | C:7 | C:7 | Retains score; strongest cell in the matrix; named company examples ([Anthropic/GKE](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), [Snowflake/EKS](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), [Figma/EKS](https://www.figma.com/blog/migrating-onto-kubernetes/), [Notion/EKS](https://www.notion.com/blog/building-and-scaling-notions-data-lake)) |
| 12 | Managed K8s | US Avg | C:5 | C:5 | Retains score |
| 13 | Managed K8s | EU Avg | C:3 | C:3 | Retains score; already appropriate |
| 14 | Managed K8s | Overall | C:5 | C:5 | Retains score |
| 15 | Self-managed K8s | <$10M | C:5 | C:5 | Retains score; strong structural argument for very low adoption |
| 16 | Self-managed K8s | $10-50M | C:5 | C:5 | Retains score |
| 17 | Self-managed K8s | $50-200M | C:4 | C:4 | Retains score |
| 18 | Self-managed K8s | $200M+ | C:6 | C:6 | Retains score; named company examples provide strong anchor ([OpenAI](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), [Databricks](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), [Salesforce](https://engineering.salesforce.com/tagged/kubernetes/), [HubSpot](https://www.cncf.io/case-studies/hubspot/)) |
| 19 | Self-managed K8s | US Avg | C:4 | C:4 | Retains score |
| 20 | Self-managed K8s | EU Avg | C:3 | C:3 | Retains score; already appropriate |
| 21 | Self-managed K8s | Overall | C:4 | C:4 | Retains score |

**Summary of Changes:**
- 3 cells lowered: Cloud-native <$10M (C:6 to C:5), Cloud-native $200M+ (C:5 to C:4), Managed K8s $50-200M (C:6 to C:5)
- 18 cells retained at draft levels
- 0 cells raised

---

## 5. Recommendations for Further Research

### Priority 1 (Critical -- Would Transform Analysis)

1. **Direct survey of 200+ AI SaaS companies segmented by ARR tier and geography.** This is the single highest-impact research action. It would move all 21 cells from Estimated/Inferred to Direct classification. The survey should ask: (a) Primary infrastructure architecture, (b) Secondary architectures used, (c) API-wrapper vs model-hosting split, (d) Team size and infra spend, (e) Geography (US/EU/APAC).

2. **Datadog or New Relic telemetry segmented for AI/ML companies.** Datadog already provides serverless and K8s adoption metrics ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)). If they could segment by vertical (AI SaaS specifically), multiple cells would move to Direct classification with observability-grade data quality.

### Priority 2 (High -- Would Significantly Improve Precision)

3. **Architecture data for companies under 500 employees.** The invisible population. A CNCF survey expansion to include smaller companies, or VC portfolio infrastructure audits (from a16z, Sequoia, Bessemer), would fill the largest data gap for the <$10M and $10-50M tier cells. Current CNCF data shows 91% of K8s users at organizations exceeding 1,000 employees ([Tigera Kubernetes Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/); [CommandLinux](https://commandlinux.com/statistics/linux-container-kubernetes-adoption-statistics/)).

4. **API-wrapper vs model-hosting split by revenue tier.** A survey question or market analysis determining what percentage of AI SaaS companies at each tier self-host models vs call external APIs would resolve the most impactful unquantified assumption (X7). The only current data point is CNCF's "37% using managed APIs, 25% self-hosting, 13% at the edge" ([CNCF 2025 Survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)), which is not tier-segmented.

5. **EU-specific managed vs self-managed K8s data.** A survey of 50+ EU AI SaaS companies would more than double the EU evidence base (currently 2 case studies). EU cloud adoption stands at 45.2% versus ~68% in the US ([Eurostat 2023](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20231208-1)), and 61% of Western European CIOs plan to increase reliance on local providers ([Gartner November 2025](https://www.gartner.com/en/newsroom/press-releases/2025-11-12-gartner-survey-reveals-geopolitics-will-drive-61-percent-of-cios-and-information-technology-leaders-in-western-europe-to-increase-reliance-on-local-cloud-providers)), but no data resolves the sovereignty-driven architecture hypothesis for AI SaaS specifically.

6. **ECS/Fargate adoption rate for AI workloads.** No equivalent to the Lambda 65% figure ([Datadog 2025](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)) exists for ECS/Fargate. Datadog could likely produce this metric from existing telemetry.

### Priority 3 (Medium -- Would Add Nuance)

7. **K8s failure/abandonment case studies.** Identifying 5-10 companies that tried K8s and reverted would break the survivorship bias and provide a counterweight to the migration-toward-K8s narrative.

8. **TCO comparison: K8s vs serverless for AI inference at different scale points.** Companies make architecture decisions partly on cost. Empirical cost comparisons at $1M, $10M, $50M, and $200M ARR would ground the decision-driver analysis.

9. **CoreWeave/GPU cloud classification study.** Determining whether K8s-native GPU clouds (CoreWeave, Lambda Labs) should be classified as managed or self-managed K8s would resolve Assumption OK3 and shift the self-managed estimates by 5-10pp.

10. **Longitudinal migration tracking.** Following 20-30 AI SaaS companies from founding through $50M ARR, documenting each architecture change and trigger, would validate or refute the assumed migration patterns.

---

## 6. Items Verified as Correct

The following elements of the consolidated draft are verified as well-supported and appropriately presented:

1. **The 3-tier architecture classification (Cloud-native non-K8s, Managed K8s, Self-managed K8s) is appropriate.** These are the correct major categories for the analysis. The non-exclusive framing is also correct -- companies use multiple architectures.

2. **The classification system (Direct / Inferred / Estimated) is sound** and consistently applied. The draft correctly identifies that no cell achieves Direct classification.

3. **The evidence density map ratings are generally accurate.** Strong cells ($200M+ Managed K8s, $200M+ Self-managed K8s) genuinely have the best evidence. Weak cells genuinely have the worst. The relative ordering is correct.

4. **The Conflict Log is thorough and transparent.** All 7 documented conflicts include both agents' estimates, the delta, and a reasoned resolution. The resolutions are defensible even when imperfect.

5. **The Assumptions Register is comprehensive.** 30+ assumptions are documented with impact-if-wrong assessments. No major implicit assumption was found that is not documented.

6. **The Known Limitations section is unusually honest.** The draft explicitly states "No direct measurement exists for the core research question" as limitation #1. This is appropriate and should remain prominent.

7. **The reconciliation of conflicting serverless data (Appendix B) is well-handled.** The 65-70% (any use) ([Datadog 2025](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)), 70% (North America production) ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), and 11% (primary framework) ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) figures are correctly identified as measuring different things, not contradicting each other.

8. **The finding that managed K8s is the dominant pattern at $200M+ ARR is well-supported.** Multiple named companies ([Anthropic/GKE](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), [Snowflake/EKS](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), [Notion/EKS](https://www.notion.com/blog/building-and-scaling-notions-data-lake), [Figma/EKS](https://www.figma.com/blog/migrating-onto-kubernetes/)), convergent survey data ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/); [Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), and SEC filing signals all point the same direction. This is the strongest finding in the analysis.

9. **The finding that self-managed K8s is declining is well-supported.** Multiple independent time-series data points (45% cloud-hosted in 2022 to 67% in 2025 ([Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/); [Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), managed K8s share growing) confirm the directional trend at 7/10 confidence.

10. **The finding that early-stage companies (<$10M ARR) default to non-K8s architectures is well-supported.** VC stage guidance ([SaaStr](https://www.saastr.com/is-there-a-benchmark-for-of-revenue-that-an-enterprise-saas-business-should-spend-on-systems-infrastructures-like-aws-or-the-equivalent/)), CNCF company size data ([Tigera Kubernetes Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), and engineering team size constraints all converge. The direction is clear even if the precise percentage (55-70%) carries uncertainty.

11. **Executive Summary point 7 (multi-architecture is the norm) is an important and well-supported finding.** The Datadog figure (66% of serverless users also use container orchestration) ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)) is Direct evidence that challenges the K8s-vs-serverless framing.

12. **The agent-level confidence scores in Appendix A are appropriate.** The consolidator's assessments match the self-reported scores, and in one case (Agent 12) the consolidator correctly adjusted slightly downward.

---

## 7. Cross-Cutting Observations

### Observation A: The Draft Is More Rigorous Than Most Industry Reports

Despite the gaps identified above, this analysis is substantially more transparent about its limitations than typical analyst reports. The explicit classification system, assumption register, conflict log, and evidence density map are rare in industry research. The main risk is not that the analysis is sloppy -- it is that readers may not read the caveats and take the point estimates as gospel.

### Observation B: The Estimate Ranges Are Appropriately Wide

Most cells have 10-15pp ranges (e.g., 55-65%, 20-30%). This is appropriate given the evidence quality. The temptation to narrow ranges for crispness should be resisted. If anything, several cells should be wider (particularly Cloud-native $10-50M at 30-45%, which could reasonably be 20-50%).

### Observation C: The Analysis Is Implicitly Structural, Not Empirical

The strongest findings in this analysis are structural arguments (e.g., "small teams can't run self-managed K8s," "GPU workloads favor K8s," "migration direction is toward K8s") rather than empirical measurements. This is appropriate given the data available, but should be flagged: the analysis is more confident about WHY companies choose architectures than about WHAT percentage choose each one.

### Observation D: Future Research Should Focus on the Two Biggest Unknowns

The two unknowns that would most improve the entire matrix are: (1) the API-wrapper vs model-hosting split by tier (only data point: CNCF 37% managed APIs / 25% self-hosting ([CNCF 2025 Survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/))), and (2) a direct survey of AI SaaS infrastructure choices by ARR tier. Everything else is refinement.

---

**Analysis Compiled:** 2026-02-12
**Role:** Adversarial Verification Agent
**Methodology:** Systematic review of 18 input files (8 Wave 1 + 9 Wave 2 + 1 consolidated draft)
**Cells Reviewed:** 21 (3 architectures x 7 columns)
**Issues Identified:** 10 material issues
**Confidence Score Revisions:** 3 cells lowered, 0 raised, 18 retained
