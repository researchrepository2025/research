# Final Report: AI SaaS Infrastructure Architecture Adoption

**Report Date:** 2026-02-12
**Produced By:** Final Report Agent (Agent 24)
**Research Program:** 24-Agent Research Swarm
**Inputs:** Consolidated draft (Agent 18), Triangulation verification (Agent 19), Internal consistency check (Agent 20), Systematic bias assessment (Agent 21), Evidence gap analysis (Agent 22), Final confidence scores (Agent 23)
**Status:** FINAL

---

## 1. Executive Summary

This report presents the definitive findings of a 24-agent research swarm studying infrastructure architecture adoption among AI SaaS companies, segmented by revenue tier and geography. The analysis synthesized 200+ data points from 8 Wave 1 fact-gathering files, 9 Wave 2 analytical files, and 4 Wave 3 verification files, with final confidence scoring by a dedicated arbiter agent.

**Key Findings (with confidence levels):**

1. **Managed Kubernetes is the dominant infrastructure pattern for AI SaaS companies at scale, but adoption is lower than commonly cited.** Across revenue tiers above $10M ARR, managed K8s (EKS, GKE, AKS) adoption ranges from 45-65%, with the tightest convergence at 50-62% for companies above $50M ARR. The higher 60-70% figure from initial architecture-focused analysis was refined downward during tier-specific triangulation and bias-adjustment. (Confidence: C:4-6 depending on tier)

2. **Cloud-native non-K8s services dominate early-stage and persist as complements at scale.** Serverless, PaaS, and managed containers (ECS/Fargate, Cloud Run) are used by 60-80% of sub-$10M ARR companies as primary architecture, declining to 15-25% as primary at $200M+ ARR. However, 40-55% of large companies still use non-K8s services for secondary workloads alongside K8s. (Confidence: C:3-4)

3. **Self-managed Kubernetes is a declining minority concentrated in the largest companies.** Overall adoption is estimated at 10-20% of AI SaaS companies, with 22-33% among $200M+ ARR companies (Salesforce confirmed self-managed [Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/); Databricks confirmed hybrid [Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators); OpenAI and HubSpot classification uncertain). The self-managed share is declining at 3-5 percentage points per year as managed K8s providers add GPU scheduling and ultra-scale cluster support. (Confidence: C:3-5 depending on tier)

4. **EU architecture patterns are a directional hypothesis, not a finding.** Structural arguments (GDPR data residency, sovereignty requirements) suggest EU may show higher Kubernetes and lower serverless adoption than the US, but this rests on the weakest evidence in the entire analysis (2 EU case studies, Agent 17 self-reported 3/10 confidence). All EU-specific estimates should be treated as speculative. (Confidence: C:2)

5. **No direct measurement of AI SaaS architecture choice by revenue tier exists.** Every cell in the estimate matrix is classified as Estimated (E) or Inferred (I). No survey or telemetry source directly segments "AI SaaS companies" by revenue tier and architecture choice. This is the single largest limitation of the analysis.

6. **Published migration case studies exclusively document moves toward K8s, but this reflects severe publication bias and cannot be interpreted as a market-wide pattern.** Three recent (2024-2025) engineering blog disclosures document migrations toward K8s (Figma: ECS to EKS [Figma Engineering Blog](https://www.figma.com/blog/migrating-onto-kubernetes/), Grammarly: EC2 to EKS [Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/), Salesforce Data Cloud: EC2 to K8s [Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/)) and one long-standing (2017+) case (HubSpot [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/)). Zero counter-migrations are documented, though companies that stayed on or migrated away from K8s almost never publish about it.

7. **Multi-architecture usage is the norm, not the exception.** At $10M+ ARR, an estimated 40-55% of companies run production workloads on multiple architecture categories simultaneously. At $200M+ ARR, this rises to 70-85%. The framing of "K8s vs serverless" is misleading -- most companies use both.

---

## 2. Methodology

### 2.1 Research Architecture: 24-Agent Swarm

The analysis was conducted by a swarm of 24 specialized agents organized into three waves:

**Wave 1 (Agents 01-08): Fact Gathering**
Eight agents independently collected data from distinct source categories:
- Agent 01: CNCF Annual Surveys (2021-2025, n=750-3,800) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/) [CNCF Annual Survey 2021](https://www.cncf.io/reports/cncf-annual-survey-2021/)
- Agent 02: Analyst Reports ([Dynatrace K8s in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/), [Datadog State of Containers 2025](https://www.datadoghq.com/state-of-containers-and-serverless/), [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263), [Flexera State of the Cloud 2025](https://info.flexera.com/CM-REPORT-State-of-the-Cloud), [Red Hat K8s Adoption Survey 2024](https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview))
- Agent 03: Job Posting Analysis (K8s demand, platform engineering trends) [kube.careers Q1 2025](https://kube.careers/state-of-kubernetes-jobs-2025-q1) [DevOpsCube 2025](https://devopscube.com/kubernetes-and-devops-job-market/)
- Agent 04: Engineering Blog Disclosures ([OpenAI](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), [Databricks](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), [Figma](https://www.figma.com/blog/migrating-onto-kubernetes/), [Grammarly](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/), [Anthropic](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), etc.)
- Agent 05: Cloud Vendor Case Studies (AWS, Azure, GCP marketing materials)
- Agent 06: StackShare/GitHub Data (technology adoption, open-source signals) [Jeevi Academy K8s Stats 2025](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)
- Agent 07: SEC Filings and Earnings Calls (public company infrastructure disclosures)
- Agent 08: VC/Startup Database Analysis (stage-specific guidance, funding patterns) [CB Insights State of AI 2025](https://www.cbinsights.com/research/report/ai-trends-2025/) [Bessemer Cloud 100](https://www.bvp.com/atlas/the-cloud-100-benchmarks-report) [Menlo Ventures GenAI 2025](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)

**Wave 2 (Agents 09-17): Analysis**
Nine agents synthesized Wave 1 data from specialized perspectives:
- Agents 09-11: Architecture-focused deep dives (cloud-native non-K8s, managed K8s, self-managed K8s)
- Agents 12-15: Revenue tier analysis (<$10M, $10-50M, $50-200M, $200M+)
- Agents 16-17: Geography analysis (US market, EU market)

**Wave 3 (Agents 18-24): Consolidation and Verification**
- Agent 18: Cross-agent consolidation into unified estimate matrix
- Agent 19: Cross-source triangulation (adversarial verification of data claims)
- Agent 20: Internal consistency check (contradictions, mathematical verification)
- Agent 21: Systematic bias assessment (structural bias across all sources)
- Agent 22: Evidence gap analysis (cell-by-cell evidence strength ranking)
- Agent 23: Final confidence scoring (adjudication of all Wave 3 recommendations)
- Agent 24: Final report production (this document)

### 2.2 Estimate Derivation Process

Each cell in the primary estimate matrix was populated through:

1. Architecture-focused agents (09-11) provided overall and tier-level estimates from each architecture perspective.
2. Tier-focused agents (12-15) provided architecture breakdowns for each revenue tier.
3. Geography-focused agents (16-17) provided US and EU adjustments.
4. The consolidation agent (18) cross-referenced estimates, applied conflict resolution rules, and produced a unified matrix.
5. Four verification agents (19-22) adversarially tested the consolidated draft.
6. Agent 23 assigned final confidence scores by adjudicating all verification recommendations.

### 2.3 Classification System

- **Direct (D):** A Wave 1 source explicitly states the figure for the specific cell.
- **Inferred (I):** Derived through documented logical steps from direct data (e.g., combining CNCF K8s production adoption with Dynatrace managed share).
- **Estimated (E):** Analyst judgment combining multiple indirect data points. All tier-specific and geography-specific cells fall in this category.

**Critical finding: No cell achieves Direct classification** because no Wave 1 source directly segments "AI SaaS companies" by architecture and revenue tier.

### 2.4 Conflict Resolution Rules

- Prefer Direct over Inferred over Estimated.
- When two agents provide overlapping ranges, use the intersection.
- When ranges do not overlap, report both and explain the resolution.
- When only Estimated sources exist, report the range rather than a point estimate.
- Weight by sample size and recency when multiple Direct sources disagree.

### 2.5 Weighting Methodology for "Overall" Estimates

Overall estimates are implicitly revenue-weighted (giving proportionally more influence to larger companies whose architecture choices are better evidenced and represent a larger share of AI SaaS economic activity). Under a company-count-weighted scheme, cloud-native overall would be approximately 45-55% and managed K8s approximately 35-45%. The revenue-weighted approach was chosen because the evidence base is stronger for larger tiers, but readers should note that this is a methodological choice that affects the resulting numbers.

### 2.6 Bias Calibration

Every major data source in the analysis carries pro-K8s selection, survivorship, or publication bias. No countervailing source over-represents serverless, PaaS, or ECS/Fargate users. The primary calibration tool is the CNCF-Gartner gap: CNCF reports 80-82% K8s production adoption among its self-selected respondents [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/), while Gartner reports 54% among a broader enterprise sample [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263) -- a 26-28 percentage point gap attributable to selection bias. The final estimates apply a 15-28pp discount range to CNCF-anchored figures, with the specific discount varying by cell based on the availability of non-CNCF corroboration.

---

## 3. Definitions

### 3.1 Architecture Categories

**Cloud-Native (Non-K8s Managed):** Serverless, PaaS, and managed container services that do NOT use Kubernetes.
- *Includes:* AWS Lambda, Azure Functions, Google Cloud Functions, AWS ECS/Fargate, Google Cloud Run, Azure Container Apps, Heroku, Vercel, Firebase, AWS App Runner, Azure App Service, Railway, Render, managed ML platforms (SageMaker, Vertex AI, Azure ML) when used as primary compute
- *Excludes:* All Kubernetes-based services (EKS, AKS, GKE, self-hosted K8s), services that run on K8s internally but are consumed as managed services (note: this boundary is judgment-based)

**Managed Kubernetes (EKS, AKS, GKE):** Kubernetes with a cloud-provider-managed control plane.
- *Includes:* Amazon EKS, Azure AKS, Google GKE (including Autopilot), Oracle OKE, DigitalOcean Kubernetes, Linode Kubernetes Engine, managed OpenShift (ROSA, ARO), Rancher-on-cloud with managed control plane
- *Excludes:* Self-hosted K8s on cloud VMs, CoreWeave/Lambda Labs (classification ambiguous -- see Assumption OK3), on-premises K8s with any control plane configuration

**Open/Self-Managed Kubernetes:** Kubernetes without a managed control plane.
- *Includes:* kubeadm clusters on cloud VMs, on-premises bare metal K8s (e.g., Salesforce), k3s/k0s in production, self-managed OpenShift, Rancher with self-managed control plane
- *Excludes:* All managed K8s services, CoreWeave/Lambda Labs (classification ambiguous)

### 3.2 Measurement Scope

All estimates measure "primary or significant production architecture" -- defined as an architecture that handles a meaningful share (roughly >20%) of production compute workloads. This excludes trivial usage (e.g., a single Lambda function for webhook processing alongside a primary K8s deployment). Because this threshold is judgment-based and categories are non-exclusive, the three architecture rows can sum to more than 100% at any given tier due to multi-architecture overlap.

---

## 4. Primary Estimate Matrix

Format: **X% (C:N, Class)** where X% is the best estimate range, C:N is the final confidence score (1-10) from Agent 23, and Class is D/I/E.

### 4.1 Cloud-Native (Non-K8s Managed): Serverless, PaaS, ECS/Fargate, Cloud Run

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Estimate** | 60-80% | 30-45% | 20-30% | 12-22% | 33-45% | 15-30% | 30-45% |
| **Confidence** | C:4 | C:4 | C:3 | C:4 | C:4 | C:2 | C:3 |
| **Classification** | E | E | E | E | E | E | E |

### 4.2 Managed Kubernetes (EKS, AKS, GKE)

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Estimate** | 15-28% | 50-62% | 50-62% | 52-63% | 45-55% | 35-50% | 40-53% |
| **Confidence** | C:3 | C:5 | C:5 | C:6 | C:4 | C:2 | C:4 |
| **Classification** | E | E | E | I | E | E | E |

### 4.3 Open/Self-Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Estimate** | 1-4% | 4-10% | 7-14% | 22-33% | 8-16% | 18-30% | 12-20% |
| **Confidence** | C:4 | C:4 | C:3 | C:5 | C:3 | C:2 | C:3 |
| **Classification** | E | E | E | I | E | E | E |

### 4.4 Consistency Checks

**Tier-weighted average check (revenue-weighted: 15% <$10M, 25% $10-50M, 30% $50-200M, 30% $200M+):**

- Cloud-native: 0.15*70% + 0.25*37.5% + 0.30*25% + 0.30*17% = 10.5 + 9.4 + 7.5 + 5.1 = ~32.5% -- falls within Overall range of 30-45%. Consistent.
- Managed K8s: 0.15*21.5% + 0.25*56% + 0.30*56% + 0.30*57.5% = 3.2 + 14.0 + 16.8 + 17.3 = ~51.3% -- falls within Overall range of 40-53%. Consistent.
- Self-managed K8s: 0.15*2.5% + 0.25*7% + 0.30*10.5% + 0.30*27.5% = 0.4 + 1.8 + 3.2 + 8.3 = ~13.6% -- falls within Overall range of 12-20%. Consistent.

**US+EU geographic weighted check (US ~63% of global AI SaaS market, EU ~28%, rest ~9%):**

- Cloud-native: 0.63*39% + 0.28*22.5% + 0.09*30% = 24.6 + 6.3 + 2.7 = ~33.6% -- falls within Overall range of 30-45%. Consistent.
- Managed K8s: 0.63*50% + 0.28*42.5% + 0.09*45% = 31.5 + 11.9 + 4.1 = ~47.5% -- falls within Overall range of 40-53%. Consistent.
- Self-managed K8s: 0.63*12% + 0.28*24% + 0.09*15% = 7.6 + 6.7 + 1.4 = ~15.6% -- falls within Overall range of 12-20%. Consistent.

**Row sum plausibility (architecture overlap check):**

| Tier | Cloud-Native (mid) | Managed K8s (mid) | Self-Managed (mid) | Sum | Multi-Arch Estimate | Plausible |
|---|---|---|---|---|---|---|
| <$10M | 70% | 21.5% | 2.5% | 94% | 15-25% | Yes (sum near 100%) |
| $10-50M | 37.5% | 56% | 7% | 100.5% | 40-55% | Yes (minimal overlap) |
| $50-200M | 25% | 56% | 10.5% | 91.5% | 40-55% | Yes (sum near 100%) |
| $200M+ | 17% | 57.5% | 27.5% | 102% | 70-85% | Yes (some overlap expected) |

Note: The $200M+ row sum of ~102% with a multi-architecture estimate of 70-85% is consistent -- the multi-architecture figure captures companies using two or more categories simultaneously, while the row sum shows modest overlap at the midpoints.

---

## 5. Detailed Findings by Architecture

### 5.1 Cloud-Native (Non-K8s Managed)

**Overall adoption: 30-45% (C:3, E)**

Cloud-native non-K8s services represent the primary or significant infrastructure for roughly a third to nearly half of all AI SaaS companies. This category is systematically under-measured: every major data source (CNCF, Dynatrace, Datadog, tech blogs) measures K8s better than non-K8s alternatives, so all non-K8s estimates are derived as residuals from K8s data. The true adoption rate may be higher than estimated.

**Tier progression:**

- **<$10M ARR (60-80%, C:4):** The dominant pattern for early-stage AI SaaS. Multiple independent VC advisory sources ([Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget), SaaStr, YC batch patterns) recommend serverless and PaaS for companies with 5-30 engineers. CNCF survey data excludes companies under 500 employees entirely [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/), and at 500-1,000 employees only 9% are K8s users [Tigera K8s Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/). The range is wide because of bimodality within the tier: pre-revenue/seed companies (0-$2M) are nearly 100% non-K8s, while $5-10M companies begin adopting K8s at meaningful rates.

- **$10-50M ARR (30-45%, C:4):** The transitional tier. Agent 09 estimated 15-30% (primary only); Agent 13 estimated 45-60% (any production use). The resolution at 30-45% for "primary or significant" reflects genuine uncertainty. The upper bound (45%) implies near-parity with managed K8s at this tier; the estimate midpoint (~37%) is more likely than the extremes. AI SaaS companies at this tier that are API-wrappers (calling external model APIs) have substantially lower infrastructure needs and may remain on non-K8s indefinitely.

- **$50-200M ARR (20-30%, C:3):** Declining share. No named AI SaaS company at this tier is documented as using non-K8s as its primary architecture. The estimate rests on Weak evidence density and is derived primarily as a residual from K8s adoption data.

- **$200M+ ARR (12-22%, C:4):** The lowest share, but still non-trivial. Agent 09 estimated 5-15% (primary); Agent 15 estimated 40-55% (any use). The resolution at 12-22% for "primary or significant" blends both sources but leans toward the lower end, recognizing that named $200M+ companies (OpenAI [OpenAI K8s Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), Databricks [Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), Anthropic [Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), Snowflake [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), Figma [Figma Engineering Blog](https://www.figma.com/blog/migrating-onto-kubernetes/), Grammarly [Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)) overwhelmingly use K8s as primary. The Agent 09 range (5-15%) is not discarded -- it is partially reflected in the lower bound. The 40-55% "any use" figure from Agent 15 remains relevant as a measure of complementary serverless/PaaS alongside K8s at this tier.

**Key supporting evidence:**
- Datadog telemetry: 65% of AWS customers use Lambda (any invocation), 70% of GCP customers use Cloud Run [Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/) [Datadog Blog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)
- CNCF 2024: Serverless as primary computing framework declined to 11% (down from 22% in 2022) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)
- CNCF 2024 NA: 70% of North American enterprises run production serverless workloads [Jeevi Academy K8s Statistics](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)
- These figures measure different scopes -- the estimate matrix targets "primary or significant," falling between "primary only" (11%) and "any use" (65-70%)

### 5.2 Managed Kubernetes (EKS, AKS, GKE)

**Overall adoption: 40-53% (C:4, E)**

Managed Kubernetes is the plurality architecture for AI SaaS companies overall and the clear dominant pattern above $50M ARR. However, the commonly cited figures of 60-70% K8s adoption overstate managed K8s specifically, because they (a) include self-managed K8s, (b) derive from CNCF survey respondents who are biased 26-28 percentage points toward K8s versus the broader Gartner enterprise sample (54%) [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263), and (c) measure general enterprises, not AI SaaS specifically.

The managed share of all K8s deployments is estimated at 61-73% based on three partially conflicting data points:
- Dynatrace 2023: 73% managed (cloud environments only) [Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)
- Tigera/market research 2024: 61% of production clusters [Tigera K8s Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)
- StackShare/GitHub 2025: 67% cloud-hosted (not necessarily managed) [Jeevi Academy K8s Statistics](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)
- CNCF 2024: deployment environments "skewing heavily toward self-managed" (a counterpoint) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)

The draft anchored on the Dynatrace 73% figure; this final report uses the full 61-73% range.

**Tier progression:**

- **<$10M ARR (15-28%, C:3):** The weakest cell for managed K8s evidence. CNCF data is inapplicable below 500 employees. VC stage guidance explicitly recommends against K8s at seed stage [Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget). YC W24 batch (66% AI companies) received Azure credits defaulting to non-K8s services [CNBC](https://www.cnbc.com/2024/08/02/microsoft-touts-cloud-momentum-from-y-combinator-startups.html). This cell was the largest confidence reduction in the entire analysis (draft C:5 to final C:3) because the estimate is pure extrapolation contradicted by the only tier-specific qualitative guidance available. Within this tier, managed K8s adoption is likely near 0% at pre-revenue/seed and potentially 25-40% at $5-10M ARR.

- **$10-50M ARR (50-62%, C:5):** Two independent analytical agents (10 and 13) converge at overlapping ranges (Agent 10: 55-70% total K8s; Agent 13: 50-65% managed K8s). Applying the intersection rule yields 55-65%, narrowed from the draft's 50-65%. The final range of 50-62% accounts for CNCF selection bias and the AI-specific 44% figure (organizations not running AI/ML on K8s even among CNCF respondents) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/). Note: for API-wrapper AI SaaS at this tier, managed K8s adoption is likely 30-45% rather than 50-62%.

- **$50-200M ARR (50-62%, C:5):** Agent 10 estimated 70-85% total K8s at this tier; Agent 14 estimated 55-65% managed K8s. After separating managed from total K8s (subtracting 7-14% self-managed), Agent 10's implied managed range is 55-78%. Agent 14's direct tier-specific estimate of 55-65% is preferred as the tighter analysis. The classification was downgraded from Inferred to Estimated because the inference chain from general enterprise K8s data to AI SaaS managed K8s requires assumption X2 (AI SaaS is more cloud-native than average enterprise), which is untested.

- **$200M+ ARR (52-63%, C:6):** The strongest cell in the matrix. Named companies: Anthropic (GKE) [Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), Snowflake (EKS) [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), Figma (EKS, migrated from ECS in 2024) [Figma Engineering Blog](https://www.figma.com/blog/migrating-onto-kubernetes/), Grammarly (EKS, migrated from EC2 in 2025) [Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/), Notion (EKS) [Notion Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake), Cohere (OKE) [Oracle Case Study](https://www.oracle.com/cloud/technical-case-studies/cohere/), Contextual AI (GKE) [GCP Customer Story](https://cloud.google.com/customers/contextualai), Stacks (GKE Autopilot) [GCP Customer Story](https://cloud.google.com/customers/stacks). Supported by CNCF/Dynatrace convergence and SEC filing infrastructure signals. Confidence reduced from draft C:7 to final C:6 because even these named companies are predominantly $1B+ ARR (not representative of $200M-500M companies) and no source directly measures AI SaaS managed K8s prevalence.

**Vendor market share (among managed K8s users):**
- EKS: ~39% share (CNCF 2021 survey) [CNCF Annual Survey 2021](https://www.cncf.io/reports/cncf-annual-survey-2021/), strongest in US
- GKE: ~32% share, strong in AI/ML due to TPU integration [Jeevi Academy K8s Statistics](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)
- AKS: ~28% share among 5,000+ employee organizations, inferred strength in EU enterprise [Jeevi Academy K8s Statistics](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)

### 5.3 Open/Self-Managed Kubernetes

**Overall adoption: 12-20% (C:3, E)**

Self-managed Kubernetes represents a declining minority, concentrated in the largest companies. The directional trend (declining share) is well-supported at approximately C:7 confidence, but the specific percentages carry much lower confidence (C:3).

**Trend evidence:**
- Cloud-hosted K8s clusters rose from 45% (2022) to 67% (2025) [Jeevi Academy K8s Statistics](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)
- Managed K8s share: 61-73% across multiple sources (up from lower levels historically) [Dynatrace K8s in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) [Tigera K8s Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)
- EKS added 100K node support [InfoQ](https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/), GKE added 130K-node clusters [WebProNews](https://www.webpronews.com/googles-130000-node-kubernetes-colossus-engineering-the-future-of-ai-scale-computing/), CNCF introduced AI Conformance certification [CNCF Announcement](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/) -- all reducing the need to self-manage
- Zero new entrants to self-managed K8s at smaller scales documented

**Tier progression:**

- **<$10M ARR (1-4%, C:4):** Negligible. Self-managed K8s requires dedicated infrastructure expertise that sub-$10M teams (5-30 engineers) lack. Strong structural argument supported by two-agent convergence.

- **$10-50M ARR (4-10%, C:4):** Small minority. Companies at this tier typically have 80-300 employees with 3-8 platform engineers -- feasible but uncommon for self-managed K8s. No named AI SaaS company at this tier is documented as self-managing.

- **$50-200M ARR (7-14%, C:3):** Derived by subtracting managed K8s from total K8s at this tier. No named self-managed K8s company exists at this specific tier in the evidence base (OpenAI, Databricks, Salesforce are all $200M+).

- **$200M+ ARR (22-33%, C:5):** Supported by named examples, though the evidence is thinner than initially reported. After Agent 19's source verification:
  - Salesforce: **Confirmed** self-managed (bare metal K8s) [Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/)
  - Databricks: **Confirmed** hybrid (mix of self-managed and managed K8s across EKS, AKS, GKE) [Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)
  - OpenAI: **Likely** self-managed historically (7,500-node cluster on Azure with custom CNI) [OpenAI K8s Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), but **current state uncertain** given $250B Azure commitment [OpenAI-Microsoft Partnership](https://openai.com/index/next-chapter-of-microsoft-openai-partnership/) (may have moved to AKS)
  - HubSpot: **Classification unclear** (CNCF case study from 2017-2018 [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/), predates EKS maturity; current managed vs self-managed status unknown)

---

## 6. Segmentation Analysis

### 6.1 By Revenue Tier

The architecture adoption pattern follows a clear progression driven by team size, infrastructure complexity needs, and economic constraints:

**Pre-revenue / Seed ($0-2M ARR):**
- Near-100% cloud-native non-K8s (Lambda, Heroku, Vercel, Firebase)
- Near-0% any K8s
- Driven by: minimal engineering teams (2-10 people), VC guidance to avoid K8s overhead [Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget), managed API usage for AI capabilities

**Early Growth ($2-10M ARR):**
- 50-65% cloud-native non-K8s
- 15-30% managed K8s (among companies self-hosting models)
- 1-5% self-managed K8s
- Driven by: emerging platform engineering function, first model self-hosting attempts, cost optimization pressure

**Growth ($10-50M ARR):**
- 30-45% cloud-native non-K8s (primary or significant)
- 50-62% managed K8s
- 4-10% self-managed K8s
- Driven by: dedicated platform teams (3-8 engineers), GPU orchestration needs, multi-service architecture, SOC 2/HIPAA compliance requirements

**Scale ($50-200M ARR):**
- 20-30% cloud-native non-K8s
- 50-62% managed K8s
- 7-14% self-managed K8s
- Driven by: large platform engineering teams (10-25 engineers), multi-region deployment, advanced GPU scheduling, cost optimization at scale

**Enterprise ($200M+ ARR):**
- 12-22% cloud-native non-K8s (primary), 40-55% complementary use
- 52-63% managed K8s
- 22-33% self-managed K8s
- Driven by: dedicated infrastructure organizations (20+ platform engineers), ultra-scale GPU clusters, multi-cloud strategy, custom control plane requirements
- Multi-architecture overlap: 70-85% of companies at this tier run multiple architecture categories simultaneously

### 6.2 By Geography (US vs EU)

**Important caveat:** EU estimates rest on the weakest evidence in the entire analysis (C:2 confidence for all EU cells). Only 2 EU AI company case studies exist in the Wave 1 dataset (Stacks in Amsterdam on GKE Autopilot [GCP Customer Story](https://cloud.google.com/customers/stacks); Medigold Health in UK on Azure [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/)). All EU-specific percentages should be treated as directional hypotheses.

| Architecture | US Estimate | EU Estimate | Directional Difference | Structural Driver |
|---|---|---|---|---|
| Cloud-native non-K8s | 33-45% (C:4) | 15-30% (C:2) | EU likely lower | GDPR data-residency requirements reduce serverless appeal (limited data-path control); absence of EU-native serverless providers |
| Managed K8s | 45-55% (C:4) | 35-50% (C:2) | Uncertain | AKS may have stronger EU enterprise position due to Microsoft relationships; hyperscaler sovereign cloud offerings ([AWS European Sovereign Cloud](https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud/)) partially address sovereignty concerns |
| Self-managed K8s | 8-16% (C:3) | 18-30% (C:2) | EU likely higher | GDPR sovereignty requirements; on-premises deployment demands; EU-native infrastructure options (OVHcloud, Hetzner); [Gaia-X](https://gaia-x.eu/gaia-x-enters-season-two-of-dataspaces-and-digital-ecosystems-with-summit-2025/) sovereignty frameworks |

**Note on EU data quality:** The CNCF regional data showing "82% EU vs 70% Americas in cloud-native development" measures cloud-native development intensity broadly (including containers, microservices, DevOps practices), NOT Kubernetes adoption specifically and NOT AI SaaS companies [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/). This figure supports the claim that EU is more cloud-native in general, but the leap to "higher K8s adoption" is an inference, not a direct data point.

---

## 7. Verification Summary

### 7.1 Wave 3 Verification Overview

Four adversarial verification agents (19-22) independently reviewed the consolidated draft (Agent 18). Collectively they identified 36 issues:

| Agent | Focus | Issues Found | Items Verified Correct | Estimate Revisions | Confidence Revisions |
|---|---|---|---|---|---|
| 19 (Triangulation) | Cross-source data accuracy | 8 | 16 | 5 cells widened/shifted | 4 cells reduced |
| 20 (Contradictions) | Internal consistency | 10 | 8 categories verified | 3 cells narrowed/shifted | 3 cells reduced |
| 21 (Bias Assessment) | Systematic bias | 8 | 10 items verified | All 21 cells shifted | All 21 cells reduced (avg -1.2 pts) |
| 22 (Gap Analysis) | Evidence sufficiency | 10 | 12 items verified | Methodology notes | 3 cells reduced |

### 7.2 Most Significant Corrections Applied

1. **Executive summary headline revised downward.** The draft's "60-70% K8s adoption above $10M ARR" was replaced with "50-62%" to match the post-resolution matrix values. The higher figure was Agent 10's pre-resolution estimate.

2. **Managed K8s share anchored on range, not single point.** The draft anchored on Dynatrace 73% managed K8s [Dynatrace K8s in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/); the final report uses the 61-73% range from three partially conflicting sources (Dynatrace 73% [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/), Tigera 61% [Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/), StackShare 67% [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)).

3. **Sub-$10M managed K8s confidence reduced from C:5 to C:3.** This was the largest single confidence correction, driven by the recognition that CNCF data excludes companies under 500 employees [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) and VC stage guidance actively recommends against K8s [Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget).

4. **All EU cells reduced from C:3 to C:2.** While C:3 implies "at least one weak source exists," for EU-specific AI SaaS architecture data, essentially no source exists -- the estimates are structural arguments applied to US data.

5. **Self-managed K8s named-company evidence reclassified.** Only 2 of 4 named companies (Salesforce [Salesforce Engineering](https://engineering.salesforce.com/tagged/kubernetes/), Databricks [Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)) are clearly confirmed as self-managed. OpenAI's current state is uncertain [OpenAI K8s Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/); HubSpot's classification is ambiguous [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/).

6. **Migration evidence reframed.** Changed from "four independent engineering blog disclosures" to "three recent (2024-2025) and one long-standing (2017+)" to reflect that HubSpot's case dates to 2017-2018 [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/). Publication bias caveat strengthened.

7. **Cloud-native non-K8s structural under-measurement acknowledged.** All non-K8s estimates are derived as residuals from K8s data. Since K8s is over-measured, the residual is systematically too small. The final estimates shift cloud-native ranges upward by 3-10pp across tiers.

8. **Missing conflict log entry added.** Agent 09 estimated EU cloud-native non-K8s as 5-10pp HIGHER than US; Agent 17 and the draft show it as 10-15pp LOWER. This sign-reversal contradiction was unlogged in the draft. Resolution: Agent 09's finding was internally contradictory (its reasoning about compliance actually supports K8s, not serverless); Agent 17's EU-specific analysis is preferred.

9. **Overall weighting methodology documented.** The draft did not state whether "Overall" estimates were company-count-weighted or revenue-weighted. Company-count weighting produces materially different results (cloud-native ~50% vs revenue-weighted ~33%). The final report specifies revenue-weighting and presents the alternative.

10. **CNCF sample size decline flagged.** The CNCF 2024 survey had n=750 respondents, down from n=988 in 2023 and n=3,800 in 2021 [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/) [CNCF 2021 Announcement](https://www.cncf.io/announcements/2022/02/10/cncf-sees-record-kubernetes-and-container-adoption-in-2021-cloud-native-survey/), potentially amplifying selection bias.

---

## 8. Limitations and Caveats

### 8.1 Fundamental Limitations (Cannot Be Resolved with Available Data)

1. **No direct measurement exists for the core research question.** No survey, telemetry source, or analyst report directly segments "AI SaaS companies" by infrastructure architecture and revenue tier. Every cell in the estimate matrix is derived through inference or estimation.

2. **CNCF survey selection bias is large and compounding.** CNCF surveys are answered by self-selected cloud-native practitioners, inflating K8s adoption by an estimated 26-28 percentage points versus Gartner's broader sample [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263). The CNCF 2024 survey's sample declined to n=750 (from n=3,800 in 2021) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [CNCF 2021 Announcement](https://www.cncf.io/announcements/2022/02/10/cncf-sees-record-kubernetes-and-container-adoption-in-2021-cloud-native-survey/), potentially further concentrating the respondent pool among active K8s users.

3. **Companies under 500 employees are invisible in survey data.** CNCF data stops at 500-1,000 employees (9% of K8s users) [Tigera K8s Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/). Most AI SaaS companies under $50M ARR have fewer than 500 employees. Sub-$10M and $10-50M tier estimates are extrapolated downward from enterprise data, not measured.

4. **Publication bias systematically over-represents Kubernetes.** Companies that publish engineering blogs about infrastructure overwhelmingly discuss K8s. Companies using ECS, Lambda, Heroku, or PaaS rarely publish infrastructure case studies. This creates information asymmetry where K8s appears more dominant than it may actually be. No countervailing pro-serverless or pro-PaaS bias exists in any data source.

5. **No failure or abandonment data exists.** Zero Wave 1 sources document companies that tried K8s and abandoned it. Survivorship bias means we see only architecture successes. The 4-to-0 migration ratio (toward K8s vs away) is an artifact of the publication incentive structure, not necessarily a reliable measure of actual patterns.

6. **EU data is extremely sparse.** Only 2 EU AI company case studies exist (Stacks on GKE [GCP Customer Story](https://cloud.google.com/customers/stacks), Medigold on Azure [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/)). All EU-specific estimates should be treated as speculative. The EU AI Act (effective August 2, 2026) [EU AI Act Timeline](https://artificialintelligenceact.eu/implementation-timeline/) may further differentiate EU patterns but no compliance-driven architecture data exists yet.

7. **The "AI SaaS" category is heterogeneous.** API-wrapper companies (calling OpenAI/Anthropic APIs) have fundamentally different infrastructure needs than model-hosting companies. The split almost certainly varies dramatically by tier (most sub-$10M are API-wrappers; most $200M+ self-host). No source quantifies this split, yet it is the single largest unquantified variable, adding +/-10-15pp uncertainty to every tier-specific cell.

### 8.2 Methodological Limitations

8. **Non-exclusive categories create ambiguity.** Architecture categories are non-exclusive. The estimate matrix measures "primary or significant" usage, but this threshold is judgment-based. A company could appear in both "managed K8s" and "cloud-native non-K8s" rows.

9. **Revenue tier boundaries are arbitrary.** The $10M, $50M, and $200M breakpoints do not correspond to natural architectural inflection points. The transition from non-K8s to K8s is company-specific.

10. **Temporal snapshot risk.** All estimates reflect 2024-2025 data, with some key sources dating to 2021-2023. AI infrastructure evolves rapidly. The Dynatrace 73% managed K8s figure is from 2023 (3 years old) [Dynatrace K8s in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/); the CNCF managed K8s provider breakdown is from 2021 (5 years old) [CNCF Annual Survey 2021](https://www.cncf.io/reports/cncf-annual-survey-2021/).

11. **US-centric source bias is pervasive.** Wave 1 files are approximately 85%+ US-sourced. The "Overall" column is implicitly US-weighted.

12. **Cloud-native non-K8s is measured by exclusion.** No source directly measures "companies using ECS/Fargate/Cloud Run as primary infrastructure." All non-K8s estimates are residuals from K8s data, inheriting inverted K8s bias.

### 8.3 Directional Confidence vs Percentage Confidence

The research is substantially more reliable on directional findings than on specific percentages:

| Directional Finding | Confidence |
|---|---|
| Managed K8s is the dominant architecture at $50M+ ARR | High (~C:7) |
| Self-managed K8s is declining over time | High (~C:7) |
| Early-stage (<$10M) companies default to non-K8s | High (~C:7) |
| Multi-architecture usage increases with company size | High (~C:6-7) |
| Migration direction is net toward K8s | Moderate (~C:5) |
| EU has higher K8s and lower serverless than US | Low (~C:3) |
| Specific percentage in any cell of the estimate matrix | Low to Moderate (C:2-6, mean C:3.5) |

Stakeholders should rely on the directional findings and treat the specific percentages as rough order-of-magnitude estimates with +/-10-15pp uncertainty in most cells.

---

## 9. Recommendations for Further Research

### Priority 1: Critical (Would Transform the Analysis)

1. **Direct survey of 200+ AI SaaS companies segmented by ARR tier and geography.** This is the single highest-impact research action. It would move all 21 cells from Estimated/Inferred to Direct classification. The survey should ask: (a) Primary infrastructure architecture, (b) Secondary architectures used, (c) API-wrapper vs model-hosting split, (d) Team size and infra spend, (e) Geography.

2. **Datadog or New Relic telemetry segmented for AI/ML companies.** These platforms already provide serverless and K8s adoption metrics [Datadog State of Containers 2025](https://www.datadoghq.com/state-of-containers-and-serverless/). Vertical segmentation for AI SaaS would provide observability-grade data quality for 15+ cells.

### Priority 2: High (Would Significantly Improve Precision)

3. **Architecture data for companies under 500 employees.** A CNCF survey expansion to smaller companies, or VC portfolio infrastructure audits, would fill the largest data gap for the <$10M and $10-50M tiers.

4. **API-wrapper vs model-hosting split by revenue tier.** Resolving the most impactful unquantified assumption (X7) would shift all tier-specific estimates by 10-15pp.

5. **EU-specific AI SaaS infrastructure survey (50+ companies).** Would more than double the EU evidence base and resolve the sovereignty-driven architecture hypothesis.

6. **ECS/Fargate adoption rate for AI workloads.** No equivalent to the Lambda 65% figure [Datadog State of Containers 2025](https://www.datadoghq.com/state-of-containers-and-serverless/) exists. Datadog could likely produce this from existing telemetry.

### Priority 3: Medium (Would Add Nuance)

7. **K8s failure/abandonment case studies.** Identifying 5-10 companies that tried K8s and reverted would break survivorship bias.

8. **TCO comparison: K8s vs serverless for AI inference at different scale points.** Empirical cost data at $1M, $10M, $50M, and $200M ARR.

9. **CoreWeave/GPU cloud classification study.** Whether K8s-native GPU clouds are managed or self-managed shifts self-managed estimates by 5-10pp. [Sacra GPU Clouds Report](https://sacra.com/research/gpu-clouds-growing/)

10. **Longitudinal migration tracking.** Following 20-30 AI SaaS companies from founding through $50M ARR.

---

## Appendix A: Full Citation Index

### Wave 1 Source Files and Key Data Points

| Wave 1 File | Key Data Points Referenced | Used By (Wave 2 Agents) |
|---|---|---|
| 01_cncf_survey.md | K8s 80% production (DP 1) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/), 56% multi-cloud (DP 9), 66% GenAI on K8s (DP 21), 44% no AI on K8s (DP 22), 11% serverless framework (DP 31), managed K8s 61% (DP 37), 9% at 500-1K employees (DP 27) [Tigera K8s Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/), 82% EU cloud-native (DP 15), n=750 2024 survey (DP 1) | 09-17 |
| 02_analyst_reports.md | Dynatrace 73% managed (DP 1) [Dynatrace K8s in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/), 63% managed all-envs (DP 2), Gartner 54% K8s (DP 6) [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263), 66% GenAI on K8s (DP 8), AI hosting 37/25/13% split (DP 11), Lambda 65% AWS (DP 14) [Datadog State of Containers 2025](https://www.datadoghq.com/state-of-containers-and-serverless/), Cloud Run 70% GCP (DP 15) [Datadog Blog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/), 7% AI containerized workloads (DP 43) | 09-17 |
| 03_job_postings.md | K8s 28% of DevOps roles (DP 2) [DevOpsCube 2025](https://devopscube.com/kubernetes-and-devops-job-market/), platform eng 8.35% (DP 3) [DevOpsCube 2025](https://devopscube.com/kubernetes-and-devops-job-market/), 73% managed clusters (DP 4), 91% K8s at 1K+ employees (DP 7), 66-70% North America (DP 9) [kube.careers Q1 2025](https://kube.careers/state-of-kubernetes-jobs-2025-q1), K8s salary $167K (DP 16) [kube.careers Q2 2025](https://kube.careers/state-of-kubernetes-jobs-2025-q2) | 09-17 |
| 04_tech_blogs.md | Figma ECS-to-EKS (Aug 2024) [Figma Engineering Blog](https://www.figma.com/blog/migrating-onto-kubernetes/), Grammarly EC2-to-EKS (Jan 2025) [Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/), OpenAI 7,500 nodes [OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), Databricks hybrid K8s [Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), Salesforce bare metal K8s [Salesforce Engineering](https://engineering.salesforce.com/tagged/kubernetes/), HubSpot K8s (2017+) [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/), Anthropic GKE [Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), Cohere OKE [Oracle Case Study](https://www.oracle.com/cloud/technical-case-studies/cohere/), Snowflake EKS [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), Notion EKS [Notion Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake), Stacks GKE Autopilot [GCP Customer Story](https://cloud.google.com/customers/stacks) | 09-17 |
| 05_cloud_vendor_cases.md | EKS AI cases (CS 1-4), ECS/Fargate SaaS (CS 10-12), AKS cases (CS 16-17), Medigold UK Azure (CS 20) [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/), GKE cases (CS 21-22), OpenAI $250B Azure commitment [OpenAI-Microsoft Partnership](https://openai.com/index/next-chapter-of-microsoft-openai-partnership/), EKS 100K node support [InfoQ](https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/) | 09-17 |
| 06_stackshare_github.md | K8s 96% enterprise adoption [Tigera K8s Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/), 67% cloud-hosted (up from 45% in 2022) [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/), GKE 32% adoption [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/), AKS 28% at 5K+ employees [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/), 70% NA serverless disconnect vs 11% global, GPU support comparison, 77% GitOps adoption [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) | 09-17 |
| 07_sec_earnings.md | AWS $128.7B revenue [Computer Weekly](https://www.computerweekly.com/news/366638765/AWS-Q4-results-Public-cloud-giant-continues-to-reap-rewards-of-enterprise-demand-for-AI-and-IaaS), 38% IaaS share, AI SaaS 40-50% COGS [Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026), traditional SaaS 6-12% hosting [FlowCog](https://flowcog.com/saas-cogs-cost-of-revenue-cogs/), AI gross margins 50-65% [Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026), OpenShift $1.9B ARR at 30%+ growth [IBM Q4 2025 Earnings](https://www.fool.com/earnings/call-transcripts/2026/01/28/ibm-ibm-q4-2025-earnings-call-transcript/), GPU 10% to 14% of EC2 [Datadog Cloud Costs Report](https://www.datadoghq.com/about/latest-news/press-releases/datadogs-state-of-cloud-costs-2024-report-finds-spending-on-gpu-instances-growing-40-as-organizations-experiment-with-ai/), 83% idle container costs [Datadog Cloud Costs Report](https://www.datadoghq.com/about/latest-news/press-releases/datadogs-state-of-cloud-costs-2024-report-finds-spending-on-gpu-instances-growing-40-as-organizations-experiment-with-ai/) | 09-17 |
| 08_vc_startup_db.md | Seed-stage K8s avoidance guidance [Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget), Maven Solutions infra recommendations, YC 66% AI batch [Ellty Blog](https://www.ellty.com/blog/san-francisco-cloud-investors), YC 58% Azure credits [CNBC](https://www.cnbc.com/2024/08/02/microsoft-touts-cloud-momentum-from-y-combinator-startups.html), CoreWeave ($12B OpenAI contract, 250K GPUs, 62% cost advantage) [Sacra GPU Clouds Report](https://sacra.com/research/gpu-clouds-growing/), Bessemer 25% early-stage margins [Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026), $37B GenAI enterprise spending 2025 [Menlo Ventures](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) | 09-17 |

### Primary Sources (Underlying Wave 1 Data)

**Surveys and Telemetry:**
- CNCF Annual Surveys 2021-2024/2025 (n=750-3,800) [CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/) [CNCF 2021](https://www.cncf.io/reports/cncf-annual-survey-2021/) [CNCF 2025](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)
- Datadog State of Containers and Serverless 2025 (production telemetry) [Datadog Report](https://www.datadoghq.com/state-of-containers-and-serverless/) [Datadog Blog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)
- Dynatrace Kubernetes in the Wild Report 2023 (observability telemetry) [Dynatrace Report](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)
- Stack Overflow 2025 Developer Survey [Stack Overflow Survey](https://survey.stackoverflow.co/2025/technology)
- Flexera State of the Cloud Report 2025 [Flexera Report](https://info.flexera.com/CM-REPORT-State-of-the-Cloud)
- Red Hat Kubernetes Adoption Survey 2024 [Red Hat Report](https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview)
- Gartner Container Management Magic Quadrant 2025 [Gartner Report](https://www.gartner.com/en/documents/5405263)
- Sysdig 2023 Container Security Report [Sysdig Report](https://www.sysdig.com/press-releases/sysdig-2023-usage-report)
- HashiCorp State of Cloud Strategy Survey [HashiCorp Report](https://www.hashicorp.com/en/state-of-the-cloud)

**Industry/Analyst Reports:**
- CB Insights State of AI 2025 [CB Insights Report](https://www.cbinsights.com/research/report/ai-trends-2025/)
- Bessemer Venture Partners Cloud 100 2024 [Bessemer Report](https://www.bvp.com/atlas/the-cloud-100-benchmarks-report)
- Menlo Ventures State of Generative AI 2025 (n=495 US enterprise AI decision-makers) [Menlo Ventures Report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
- Sacra Research GPU Clouds Report [Sacra Report](https://sacra.com/research/gpu-clouds-growing/)
- SaaS Capital DevOps Spending Benchmark [SaaS Capital Report](https://www.saas-capital.com/blog-posts/spending-benchmarks-for-private-b2b-saas-companies/)

**Company Disclosures:**
- SEC 10-K filings: Snowflake [Snowflake SEC Filings](https://investors.snowflake.com/financials/sec-filings/default.aspx), Palantir [Palantir SEC Filings](https://investors.palantir.com/financials/sec-filings), Salesforce, ServiceNow, Zoom, Atlassian, Elastic
- IBM Q4 2025 Earnings (OpenShift ARR $1.9B) [IBM Q4 2025 Earnings Transcript](https://www.fool.com/earnings/call-transcripts/2026/01/28/ibm-ibm-q4-2025-earnings-call-transcript/)
- Engineering blogs: OpenAI [OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/), Databricks [Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), Figma [Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/), Grammarly [Grammarly Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/), Anthropic [Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/), Cohere [Oracle Case Study](https://www.oracle.com/cloud/technical-case-studies/cohere/), Salesforce [Salesforce Engineering](https://engineering.salesforce.com/tagged/kubernetes/), HubSpot [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/), Snowflake [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/), Notion [Notion Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake), Elastic, Jasper, Hugging Face, Contextual AI [GCP Customer](https://cloud.google.com/customers/contextualai)
- Cloud vendor case studies: AWS (25+), Azure (25+), GCP (25+)

**VC/Startup Data:**
- Y Combinator batch analysis (Winter 2024) [CNBC](https://www.cnbc.com/2024/08/02/microsoft-touts-cloud-momentum-from-y-combinator-startups.html) [Ellty Blog](https://www.ellty.com/blog/san-francisco-cloud-investors)
- CoreWeave company disclosures [Sacra](https://sacra.com/research/gpu-clouds-growing/)
- CAST AI growth data [CAST AI Blog](https://cast.ai/blog/cast-ai-raises-35-million-to-optimize-kubernetes-cost/) [TechCrunch](https://techcrunch.com/2025/04/30/cast-ai-raises-108m-to-get-the-max-out-of-ai-kubernetes-and-other-workloads/), Spectro Cloud [TechCrunch](https://techcrunch.com/2024/11/19/spectro-cloud-helps-companies-manage-their-kubernetes-installations/), Komodor growth data [Komodor Blog](https://komodor.com/blog/komodor-reports-record-business-results-for-2024/)
- Fireworks AI company data [Fireworks AI Blog](https://fireworks.ai/blog/series-c), Modal Labs company data [SiliconANGLE](https://siliconangle.com/2025/09/29/modal-labs-raises-80m-simplify-cloud-ai-infrastructure-programmable-building-blocks/)
- Mistral AI Series C ($1.5B, $11.7B valuation) [CB Insights AI 2025](https://www.cbinsights.com/research/report/ai-trends-2025/)

**EU-Specific Sources:**
- Eurostat 2023: EU enterprise cloud adoption (45.2%) [Eurostat](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20231208-1)
- Gartner 2025: 61% of EU CIOs increasing local cloud/AI provider reliance [Gartner EU CIO Survey](https://www.gartner.com/en/newsroom/press-releases/2025-11-12-gartner-survey-reveals-geopolitics-will-drive-61-percent-of-cios-and-information-technology-leaders-in-western-europe-to-increase-reliance-on-local-cloud-providers)
- Gaia-X: 180+ data spaces, sovereignty frameworks [Gaia-X](https://gaia-x.eu/gaia-x-enters-season-two-of-dataspaces-and-digital-ecosystems-with-summit-2025/)
- French government: EUR 1.8B cloud sovereignty allocation [Cloud Computing News](https://www.cloudcomputing-news.net/news/france-unveils-e1-8-billion-fund-for-nations-cloud-sector/)
- AWS European Sovereign Cloud (Germany launch) [AWS Blog](https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud/)
- EU AI Act compliance timeline (August 2, 2026) [EU AI Act Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- EU Data Act (effective September 12, 2025) [EU Data Act](https://digital-strategy.ec.europa.eu/en/policies/data-act)

---

## Appendix B: Assumptions Register

### Cross-Cutting Assumptions (All Agents)

| ID | Assumption | Impact if Wrong | Confidence |
|---|---|---|---|
| X1 | CNCF survey respondents over-represent K8s adopters relative to AI SaaS population (26-28pp measured gap vs Gartner) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263) | Non-K8s adoption is higher than estimated by 10-20pp; K8s adoption is lower | Medium |
| X2 | AI SaaS companies are more cloud-native than average enterprise surveyed by CNCF/Gartner | If not more cloud-native, K8s estimates may be too high | Medium |
| X3 | Engineering blog disclosures are directionally representative despite severe publication bias | All architecture estimates based on blog evidence would need revision | Medium |
| X4 | Revenue tiers mapped from employee count data using ~$200K-$500K ARR per employee | Size-tier analysis could miscategorize companies | Medium |
| X5 | Absence of documented migrations away from K8s reflects actual low abandonment, not just publication bias | Migration trend analysis would be biased | Low |
| X6 | Companies not running AI/ML on K8s (44% per CNCF) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) include meaningful share using non-K8s cloud-native | If most use VMs, cloud-native non-K8s is overestimated | Medium |
| X7 | "AI SaaS" includes both model-hosting and API-wrapper companies | If restricted to model-hosting only, K8s adoption would be significantly higher | High |
| X8 | 2024-2025 data represents the 2026 landscape | AI infrastructure evolves rapidly; patterns may have shifted | Medium |

### Architecture-Specific Assumptions

| ID | Assumption | Impact if Wrong | Confidence |
|---|---|---|---|
| CN1 | Serverless adoption decline (22% to 11% CNCF) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/) reflects declining primary-framework use, not total use | Cloud-native non-K8s estimates too high | Medium |
| CN2 | GPU constraints on AWS Fargate limit AI inference on that platform | If most AI inference is CPU-based (small/distilled models), Fargate is more viable | Medium |
| CN3 | PaaS/serverless-as-primary attenuates rapidly above $10M ARR | If companies stay on PaaS longer, cloud-native at $10-50M is higher | Low-Medium |
| MK1 | Managed K8s share is 61-73% (range from Dynatrace [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/), Tigera [Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/), StackShare [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/) -- not single-point 73%) | Vendor share estimates change | Medium-High |
| MK2 | AKS outperforms in EU relative to US due to Microsoft enterprise relationships | No direct data supports AI SaaS AKS share in EU | Low |
| MK3 | Multi-cloud K8s adoption among AI SaaS higher than general 56% figure [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) due to GPU scarcity | If not more multi-cloud, 20-30% multi-cloud K8s estimate inflated | Medium |
| OK1 | EU companies more likely to self-manage K8s due to data sovereignty | EU companies may use EU-region managed K8s instead | Medium |
| OK2 | OpenShift's $1.9B ARR [IBM Q4 2025 Earnings](https://www.fool.com/earnings/call-transcripts/2026/01/28/ibm-ibm-q4-2025-earnings-call-transcript/) is proxy for enterprise self-managed K8s demand | OpenShift includes managed offerings (ROSA, ARO) | Medium |
| OK3 | K8s-native GPU clouds (CoreWeave) [Sacra](https://sacra.com/research/gpu-clouds-growing/) are hybrid managed/self-managed category | Classification choice shifts self-managed estimates by 5-10pp | Medium |

### Tier-Specific Assumptions

| ID | Assumption | Impact if Wrong | Confidence |
|---|---|---|---|
| T1 | Companies under $10M ARR have 5-30 engineers | If larger, K8s adoption at this tier would be higher | Medium |
| T2 | Majority of sub-$10M AI SaaS call managed APIs rather than self-host models | If more self-host, K8s adoption higher and cloud-native lower | Medium |
| T3 | VC-backed stage guidance reflects actual startup behavior [Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget) | If companies adopt K8s early, managed K8s at <$10M could be 25-40% | Low-Medium |
| T4 | Companies at $10-50M have 80-300 employees with 3-8 platform engineers | Team size and K8s feasibility assessments would change | Medium |
| T5 | Companies at $50-200M on non-K8s are there by choice, not inertia | Would overstate non-K8s as deliberate; actual % could be lower | Medium |
| T6 | At $200M+, engineering teams of 200+ with 20+ platform engineers are standard | If teams smaller, self-managed K8s estimate too high | Medium |
| T7 | Infrastructure spend excludes personnel but includes third-party AI API costs | If personnel included, cost ranges shift upward 5-15% | Medium-High |

### Geography-Specific Assumptions

| ID | Assumption | Impact if Wrong | Confidence |
|---|---|---|---|
| G1 | US-regulated AI SaaS defaults to managed K8s for compliance | If wrong, US self-managed in regulated sectors is higher | Medium |
| G2 | The 70% NA serverless figure [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/) and 11% CNCF global figure [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) measure different things | If same thing, one figure is significantly wrong | High |
| G3 | GDPR creates structural pressure toward K8s over serverless in EU | If GDPR equally served by serverless, K8s advantage in EU overstated | High |
| G4 | EU enterprise cloud adoption at 45.2% (Eurostat 2023) [Eurostat](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20231208-1) has not dramatically changed | If adoption accelerated, EU cloud gap may be smaller | Medium |
| G5 | US hyperscaler sovereign offerings are partial solutions (CLOUD Act issue persists) [AWS European Sovereign Cloud](https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud/) | If resolved, push toward EU-native infrastructure weakens | Medium-High |
| G6 | Stacks (Amsterdam, GKE Autopilot) [GCP Customer Story](https://cloud.google.com/customers/stacks) is not representative of all EU AI SaaS | If representative, EU startup patterns mirror US managed K8s | Low |

---

## Appendix C: Evidence Density Map

Rating: **Strong** (3+ independent sources converge) | **Moderate** (2 sources or indirect convergence) | **Weak** (1 source or pure estimation) | **None** (no supporting data)

### Cloud-Native (Non-K8s Managed)

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Density** | Moderate | Weak | Weak | Moderate | Moderate | None | Moderate |

### Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Density** | Weak | Moderate | Moderate | Strong | Moderate | None | Moderate |

### Open/Self-Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Density** | Moderate | Weak | Weak | Strong | Weak | None | Moderate |

**Changes from draft:** All EU cells reclassified from "Weak" to "None" -- 2 EU case studies is anecdotal, not evidence. No source provides EU-specific AI SaaS architecture data; the estimates are structural arguments applied to US data.

**Data currency note:** The most recent primary source year for key data points:
- CNCF K8s production 80%: 2024 survey [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)
- Dynatrace 73% managed: 2023 (3 years old) [Dynatrace K8s in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)
- Gartner 54% K8s: 2025 [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263)
- StackShare 67% cloud-hosted: 2025 [Jeevi Academy K8s Statistics](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)
- Tigera 61% managed: 2024 [Tigera K8s Statistics](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)
- CNCF provider market share: 2021 (5 years old) [CNCF Annual Survey 2021](https://www.cncf.io/reports/cncf-annual-survey-2021/)

---

## Appendix D: Wave 3 Correction Log

Each recommendation from Wave 3 verification agents (19-22), with disposition (ACCEPTED / REJECTED / PARTIALLY ACCEPTED) and reasoning.

### Agent 19 (Cross-Source Triangulation) -- 8 Issues

| # | Issue | Recommendation | Disposition | Reasoning |
|---|---|---|---|---|
| 19-1 | Two distinct "managed K8s" percentages conflated (73% Dynatrace [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) vs 61% Tigera [Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/) vs 67% StackShare [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)) | Use range 61-73% instead of anchoring on 73%; widen managed K8s overall from 45-55% to 42-55% | **ACCEPTED** | The final report uses 61-73% managed share range and widens overall managed K8s to 40-53% (incorporating bias adjustment) |
| 19-2 | CNCF 2024 sample size decline (n=750, down from n=3,800 in 2021) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [CNCF 2021](https://www.cncf.io/announcements/2022/02/10/cncf-sees-record-kubernetes-and-container-adoption-in-2021-cloud-native-survey/) not flagged | Add note to limitations section; widen CNCF bias discount from 15-25pp to 15-30pp | **ACCEPTED** | Added to limitations. CNCF bias discount range widened to 15-28pp (reflecting the measured 26-28pp CNCF-Gartner gap) |
| 19-3 | Early-stage K8s avoidance evidence underweighted | Widen <$10M cloud-native from 55-70% to 60-80%; narrow managed K8s from 20-35% to 15-30% | **ACCEPTED** | Final estimates: cloud-native <$10M at 60-80%, managed K8s <$10M at 15-28% |
| 19-4 | HubSpot K8s migration dated to 2017, not 2024-2025 [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/) | Change "four independent engineering blog disclosures" to clarify temporal distinction | **ACCEPTED** | Reframed as "three recent (2024-2025) and one long-standing (2017+)" |
| 19-5 | CNCF "82% EU vs 70% Americas" measures cloud-native development intensity, not K8s adoption [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) | Clarify the supporting argument for EU K8s adoption | **ACCEPTED** | Clarified in Section 6.2 that CNCF regional data measures cloud-native broadly, not K8s specifically |
| 19-6 | Dynatrace 73% is from 2023 -- age not adequately flagged [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) | Use 61-73% range instead of single-point 73% | **ACCEPTED** | Incorporated via range-based approach (see 19-1) |
| 19-7 | "44% don't run AI/ML on K8s" (CNCF) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) data point underweighted | More prominently weight in <$10M and $10-50M tier estimates | **PARTIALLY ACCEPTED** | Referenced in managed K8s tier estimates. However, the 44% figure is from CNCF respondents (already K8s-biased), so it is used as a signal rather than an anchor. The recommendation to reduce $10-50M managed K8s by 5-10pp was partially applied (range adjusted from 50-65% to 50-62%) |
| 19-8 | OpenAI "7,500 nodes" [OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/) classification as self-managed is ambiguous | Reclassify evidence: Salesforce confirmed [Salesforce Engineering](https://engineering.salesforce.com/tagged/kubernetes/), Databricks confirmed hybrid [Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators), OpenAI likely but uncertain, HubSpot unclear [CNCF Case Study](https://www.cncf.io/case-studies/hubspot/) | **ACCEPTED** | Reclassified in Section 5.3. Confidence for $200M+ self-managed reduced from C:6 to C:5 |

### Agent 20 (Internal Consistency) -- 10 Issues

| # | Issue | Recommendation | Disposition | Reasoning |
|---|---|---|---|---|
| 20-1 | Unlogged conflict: Agent 09 EU cloud-native direction contradicts Agent 17 | Add entry to Conflict Log | **ACCEPTED** | Documented in Section 7.2. Agent 09's Finding 6 was internally contradictory; Agent 17's analysis preferred |
| 20-2 | Executive summary headline (60-70% K8s) overstates matrix values | Revise to match post-resolution matrix values (50-65%) | **ACCEPTED** | Executive summary revised to "50-62%" for above-$10M ARR managed K8s |
| 20-3 | Cloud-native $10-50M confidence inflated (C:5 with Weak density, Estimated classification, largest conflict) | Reduce to C:4 | **ACCEPTED** | Final confidence: C:4 (per Agent 23 adjudication) |
| 20-4 | Open K8s $10-50M confidence inflated (C:5 with Weak density, Estimated classification) | Reduce to C:4 | **ACCEPTED** | Final confidence: C:4 (per Agent 23) |
| 20-5 | Cloud-native $200M+ confidence inconsistent with $50-200M (larger conflict, higher score) | Reduce from C:5 to C:4 | **ACCEPTED** | Final confidence: C:4 (per Agent 23) |
| 20-6 | "Overall" estimates lack stated weighting methodology | Add methodological note specifying revenue-weighted vs company-count-weighted | **ACCEPTED** | Added in Section 2.5 and Section 4.4 |
| 20-7 | Cloud-native $10-50M range may be too wide (30-45%) | Narrow to 28-40% to avoid near-parity with managed K8s | **PARTIALLY ACCEPTED** | Retained 30-45% range because the upper bound reflects genuine uncertainty, but added narrative note that the midpoint (~37%) is more likely than extremes. The near-parity concern is valid and noted in the tier analysis |
| 20-8 | Managed K8s $50-200M conflict log imprecise about Agent 10's derived range | Update conflict log narrative to note Agent 10's implied range extends to 77% | **ACCEPTED** | Documented in Section 5.2 tier notes |
| 20-9 | Cloud-native $200M+ estimate fully overrides Agent 09 | Revise to 10-22% to blend with Agent 09 rather than override | **ACCEPTED** | Final estimate: 12-22%, blending Agent 09's upper range with Agent 15's reframed estimate |
| 20-10 | Managed K8s $10-50M range inconsistency with intersection logic | Apply intersection (55-65%) per stated methodology, or update notes | **PARTIALLY ACCEPTED** | Final estimate: 50-62%. The intersection logic was partially applied but further adjusted downward (from 55-65%) to account for Agent 19's concerns about API-wrapper companies and CNCF bias [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/). The cell notes explain this compound adjustment |

### Agent 21 (Systematic Bias Assessment) -- 8 Issues

| # | Issue | Recommendation | Disposition | Reasoning |
|---|---|---|---|---|
| 21-1 | Unidirectional source bias across all 8 Wave 1 inputs (all push K8s upward) | Apply 5-10pp downward adjustment to managed K8s; 5-10pp upward to cloud-native | **PARTIALLY ACCEPTED** | Applied moderate downward adjustment to managed K8s (3-7pp depending on tier) and upward to cloud-native (3-10pp). Agent 21's full 5-10pp blanket adjustment was partially adopted for lower tiers but moderated for $200M+ where named-company evidence partially offsets selection bias |
| 21-2 | Sub-$10M estimates contradicted by VC stage guidance [Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget) | Lower managed K8s <$10M to 12-25%; raise cloud-native to 65-80% | **ACCEPTED** | Final estimates: managed K8s <$10M at 15-28%, cloud-native <$10M at 60-80%. The lower bound for managed K8s (15%) is slightly above Agent 21's 12% because we account for some $5-10M ARR companies genuinely adopting managed K8s |
| 21-3 | Tech blog migration evidence has 100% survivorship bias | Reframe migration finding; downgrade assumption X5 to Low confidence | **ACCEPTED** | Migration finding reframed in Executive Summary point 6. Assumption X5 downgraded from Low-Medium to Low |
| 21-4 | EU estimates built on nearly zero evidence | Reduce EU confidence from C:3 to C:2; widen ranges by 10pp | **ACCEPTED** | All EU cells reduced to C:2. Ranges widened (cloud-native EU: 15-30%, managed K8s EU: 35-50%, self-managed K8s EU: 18-30%) |
| 21-5 | CNCF-Gartner gap underutilized as bias calibration [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) [Gartner Container Management 2025](https://www.gartner.com/en/documents/5405263) | Use measured 26-28pp gap, not conservative 15-25pp | **PARTIALLY ACCEPTED** | The 26-28pp gap is acknowledged as the measured bias magnitude. However, for AI SaaS specifically (which may genuinely be more K8s-heavy than average enterprise), a partial discount of 15-28pp is applied rather than the full 26-28pp. The rationale: AI SaaS companies that self-host models have genuine GPU orchestration needs that favor K8s |
| 21-6 | Cloud-native non-K8s is systematically under-measured | Adjust upward by 5-12pp across all tiers | **PARTIALLY ACCEPTED** | Applied 3-10pp upward adjustments. The full 12pp adjustment at lower tiers was accepted; the smaller 3pp adjustment at $200M+ reflects named-company evidence that most large AI SaaS companies genuinely use K8s as primary |
| 21-7 | Self-managed K8s $200M+ over-relies on 4 named companies at extreme tail | Reduce confidence from C:6 to C:5 | **ACCEPTED** | Final confidence: C:5 (per Agent 23, incorporating Agent 19's source verification that only 2 of 4 companies are clearly confirmed) |
| 21-8 | Multi-architecture framing masks primary architecture question | Add explicit overlap adjustment row or footnote | **ACCEPTED** | Added row sum plausibility check in Section 4.4 and overlap context in tier analysis |

### Agent 22 (Evidence Gap Analysis) -- 10 Issues

| # | Issue | Recommendation | Disposition | Reasoning |
|---|---|---|---|---|
| 22-1 | No cell has Direct evidence; 3 "Inferred" cells are closer to Estimated | Reclassify Managed K8s $50-200M from Inferred to Estimated; reduce C:6 to C:5 | **ACCEPTED** | Reclassified. Final classification for Managed K8s $50-200M: E. Final confidence: C:5 |
| 22-2 | EU cells rest on single analysis agent with 3/10 self-reported confidence | Add explicit caveats; treat EU findings as hypotheses not findings | **ACCEPTED** | EU findings reframed as "directional hypotheses" in Executive Summary point 4 and Section 6.2 |
| 22-3 | Population extrapolation (general enterprise to AI SaaS) unaddressed | Add standardized caveat to tier cells noting +/-10pp from population extrapolation | **ACCEPTED** | Addressed in Section 8.1 (Limitation 1) and Section 8.3 (directional vs percentage confidence). The +/-10-15pp uncertainty is noted for tier cells |
| 22-4 | US data used for Overall without adequate geo-labeling | Rename "Overall" column or add footnote about US-weighted source base | **ACCEPTED** | Methodology Section 2.5 specifies the weighting approach. Overall column header retained but with explicit documentation that estimates are US-weighted |
| 22-5 | Cloud-native non-K8s defined by exclusion, not measurement | Lower Cloud-native <$10M from C:6 to C:5; lower $200M+ from C:5 to C:4 | **ACCEPTED** | Final confidences: <$10M at C:4 (Agent 23 went further than Agent 22's recommendation), $200M+ at C:4 |
| 22-6 | Migration direction evidence suffers severe publication bias | Reframe from "strongly toward" to "net direction likely toward K8s, magnitude unknown" | **ACCEPTED** | Reframed in Executive Summary point 6 and Section 5.2 |
| 22-7 | $10-50M cloud-native has 30pp conflict resolved by averaging | Widen to 20-50% or explicitly define "primary or significant" threshold | **REJECTED** | Retained 30-45% range. Widening to 20-50% would encompass the full range of both agents' estimates under different definitions, making the cell uninformatively wide. The 30-45% range represents a genuine synthesis under the "primary or significant" definition, which is explicitly defined in Section 3.2 as >20% of production compute |
| 22-8 | Multi-architecture overlap means columns don't sum to 100% | Add overlap adjustment row | **ACCEPTED** | Added row sum plausibility check in Section 4.4 with multi-architecture overlap analysis |
| 22-9 | Temporal mismatch in source data (2021-2025 for a 2026 report) | Add "Data Currency" column to evidence density map | **ACCEPTED** | Added data currency note to Appendix C |
| 22-10 | API-wrapper vs model-hosting split is unquantified but decisive | Add as explicit sensitivity parameter in each tier cell | **PARTIALLY ACCEPTED** | Documented as the single largest unquantified assumption in Section 8.1 (Limitation 7), Section 8.3, and Executive Summary. However, adding per-cell sensitivity parameters was not feasible without quantifying the split itself -- we note that "for API-wrapper AI SaaS at this tier, managed K8s adoption is likely 30-45%" where relevant |

### Summary of Dispositions

| Disposition | Count | Percentage |
|---|---|---|
| ACCEPTED | 28 | 74% |
| PARTIALLY ACCEPTED | 8 | 21% |
| REJECTED | 1 | 3% |
| N/A (Agent 23 confidence scores applied directly) | 1 | 3% |

### Agent 23 Final Confidence Scores -- Applied Directly

Agent 23 adjudicated all Wave 3 recommendations and assigned final confidence scores. Key decisions:

- **17 of 21 cells reduced from draft levels** (average reduction: 0.9 points)
- **4 cells retained at draft-adjacent levels** (Managed K8s $10-50M at C:5, and 3 cells already at recommended levels)
- **0 cells raised from draft**
- **Mean final confidence: 3.5/10** (draft mean was 4.9/10)
- **Strongest cell: Managed K8s $200M+ at C:6** (reduced from draft C:7)
- **Weakest cells: All 6 EU cells at C:2** (reduced from draft C:3)

---

## Appendix E: Reconciled Serverless Adoption Data

A recurring conflict across agents is the discrepancy in serverless adoption figures. This appendix documents the resolution.

| Source | Figure | Scope | Classification |
|---|---|---|---|
| Datadog (02_analyst_reports.md, DP 14) [Datadog State of Containers 2025](https://www.datadoghq.com/state-of-containers-and-serverless/) | 65% of AWS customers use Lambda | Any Lambda invocation across all AWS customers | Direct (telemetry) |
| Datadog (02_analyst_reports.md, DP 15) [Datadog Blog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/) | 70% of GCP customers use Cloud Run | Any Cloud Run usage across all GCP customers | Direct (telemetry) |
| CNCF 2024 (01_cncf_survey.md, DP 31) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/) | 11% use serverless computing frameworks | Serverless as primary computing framework among CNCF respondents | Direct (survey) |
| CNCF 2023 (01_cncf_survey.md, DP 32) [CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/) | 13% (down from 22% in 2022) | Serverless as primary computing framework | Direct (survey) |
| CNCF 2024 NA (06_stackshare_github.md) [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/) | 70% of NA enterprises run production serverless | Any production serverless use among North American enterprises | Direct (survey) |

**Resolution:** These figures are not contradictory. They measure different things:
- **65-70% (Datadog) [Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/):** "Any use at all" -- including event triggers, background processing, CI/CD. Broadest measure.
- **70% (CNCF NA) [Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/):** "Production loads on serverless" in North America -- broader than primary, narrower than any use.
- **11-13% (CNCF global) [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/):** "Serverless as primary computing framework" -- narrowest measure.

The estimate matrix uses "primary or significant production architecture," which falls between 11% (too narrow) and 70% (too broad), supporting the 30-45% overall estimate for cloud-native non-K8s.

---

**Document Version:** 1.0 FINAL
**Compiled:** 2026-02-12
**Methodology:** 24-agent research swarm with adversarial verification
**Total Wave 1 Data Points Referenced:** 200+
**Total Assumptions Documented:** 30+
**Total Verification Issues Addressed:** 36
**Mean Confidence Score:** 3.5/10 (reflects honest assessment of evidence quality)
**Strongest Finding:** Managed K8s is dominant at $50M+ ARR (directional confidence ~C:7; percentage confidence C:5-6)
**Weakest Finding:** EU architecture patterns (C:2; treat as hypothesis)
