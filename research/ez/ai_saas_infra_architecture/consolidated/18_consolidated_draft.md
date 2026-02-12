# Consolidated Estimate Matrix: AI SaaS Infrastructure Architecture Adoption

**Consolidation Date:** 2026-02-12
**Consolidation Agent:** Wave 3 Consolidation
**Inputs:** 9 Wave 2 analysis files (09-17), synthesizing 8 Wave 1 fact-gathering files (01-08)
**Architecture Scope:** Cloud-native (non-K8s managed) | Managed Kubernetes | Open/Self-managed Kubernetes

---

## 1. Executive Summary

1. **Managed Kubernetes is the dominant infrastructure pattern for AI SaaS companies at scale.** Across all revenue tiers, managed K8s (EKS, GKE, AKS) adoption ranges from 20-35% at seed stage to 55-65% at $200M+ ARR. The 60-70% figure cited for companies above $10M ARR is well-triangulated across CNCF surveys ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), Dynatrace observability data ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), engineering blog disclosures ([Figma](https://www.figma.com/blog/migrating-onto-kubernetes/), [Grammarly](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), and vendor case studies ([AWS](https://aws.amazon.com/solutions/case-studies/), [GCP](https://cloud.google.com/customers), [Azure](https://www.microsoft.com/en/customers)).

2. **Cloud-native non-K8s services dominate early-stage and persist as complements at scale.** Serverless, PaaS, and managed containers (ECS/Fargate, Cloud Run) are used by 55-70% of sub-$10M ARR companies as primary architecture, declining to 15-25% as primary at $200M+ ARR. However, 40-55% of large companies still use non-K8s services for secondary workloads alongside K8s. Datadog telemetry shows 65% of AWS customers use Lambda ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)) and 70% of GCP customers use Cloud Run ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)), but these measure any-use rather than primary architecture.

3. **Self-managed Kubernetes is a declining minority concentrated in the largest companies.** Overall adoption is 15-22% of AI SaaS companies, but 25-35% among $200M+ ARR companies (OpenAI ([OpenAI Scaling K8s to 7,500 Nodes](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)), Databricks ([Databricks Engineering Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)), Salesforce ([Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/))). The self-managed share is declining at 3-5 percentage points per year as managed K8s providers add GPU scheduling, ultra-scale clusters (GKE 130K+ nodes ([WebProNews](https://www.webpronews.com/googles-130000-node-kubernetes-colossus-engineering-the-future-of-ai-scale-computing/)), EKS 100K nodes ([InfoQ](https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/))), and AI conformance certifications ([CNCF AI Conformance Program](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/)).

4. **The EU shows 5-15 percentage points higher Kubernetes adoption and correspondingly lower serverless/PaaS usage than the US**, driven by GDPR data residency requirements, sovereignty concerns, and higher cloud-native development intensity among adopters (82% EU vs 70% Americas per CNCF ([CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/))). However, EU-specific evidence is extremely limited (confidence 3/10).

5. **No direct measurement of AI SaaS architecture choice by revenue tier exists.** Every cell in the estimate matrix below is classified as Estimated (E) or Inferred (I). No survey or telemetry source directly segments "AI SaaS companies" by revenue tier and architecture choice. This is the single largest limitation of the analysis.

6. **Migration flows uniformly toward Kubernetes.** Four independent engineering blog disclosures document migrations toward K8s: Figma ECS to EKS ([Figma Engineering Blog](https://www.figma.com/blog/migrating-onto-kubernetes/)), Grammarly EC2 to EKS ([Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), Salesforce Data Cloud EC2 to K8s ([Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/)), HubSpot EC2 to K8s ([CNCF Case Study: HubSpot](https://www.cncf.io/case-studies/hubspot/)). Zero counter-migrations documented, though publication bias likely suppresses negative cases.

7. **Multi-architecture usage is the norm, not the exception.** At $10M+ ARR, an estimated 40-55% of companies run production workloads on multiple architecture categories simultaneously. At $200M+ ARR, this rises to 70-85%. The framing of "K8s vs serverless" is misleading -- most companies use both. Datadog data shows 66% of organizations using serverless functions also use container orchestration ([Datadog State of Containers and Serverless 2025](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)).

---

## 2. Methodology

### How Estimates Were Derived

Each cell in the primary estimate matrix was populated through the following process:

1. **Architecture-focused agents (09, 10, 11)** provided overall and tier-level estimates from the perspective of each architecture category (cloud-native non-K8s, managed K8s, open K8s).

2. **Tier-focused agents (12, 13, 14, 15)** provided architecture breakdowns for each revenue tier ($<10M, $10-50M, $50-200M, $200M+).

3. **Geography-focused agents (16, 17)** provided US and EU adjustments to the overall estimates.

4. For each cell, I cross-referenced estimates from the architecture agent, the tier agent, and the geography agent. Where estimates overlapped or converged, I selected the central tendency. Where they diverged, I documented the conflict (Section 6) and applied the resolution rules.

### Classification System

- **Direct (D):** A Wave 1 source explicitly states the figure for the specific cell.
- **Inferred (I):** Derived through documented logical steps from direct data (e.g., "73% of K8s clusters are managed" ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)) + "80% K8s production adoption" ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) = ~58% managed K8s overall).
- **Estimated (E):** Analyst judgment combining multiple indirect data points. All tier-specific and geography-specific cells fall in this category because no source directly segments AI SaaS by revenue tier.

### Conflict Resolution Applied

- Prefer Direct over Inferred over Estimated.
- When two agents provide overlapping ranges, use the intersection.
- When ranges do not overlap, report both and explain the resolution.
- When only Estimated sources exist, report the range rather than a point estimate.
- Weight by sample size and recency when multiple Direct sources disagree.

---

## 3. Primary Estimate Matrix

Format: **X% (C:N)** where X% is the best estimate range and C:N is the confidence score (1-10).

### Cloud-Native (Non-K8s Managed): Serverless, PaaS, ECS/Fargate, Cloud Run

*As primary or significant production architecture. Excludes all Kubernetes.*

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Estimate** | 55-70% (C:6) | 30-45% (C:5) | 20-30% (C:4) | 15-25% (C:5) | 30-40% (C:5) | 15-25% (C:3) | 25-40% (C:4) |

**Cell-level notes:**

- **<$10M:** Agents 09 and 12 converge. Agent 09 gives 60-80% for pre-revenue/seed and 35-55% for $1-10M; Agent 12 gives 55-70% for the full sub-$10M tier. Consolidated at 55-70% as the blended range across the tier. Supported by seed-stage infrastructure guidance recommending serverless and PaaS over K8s ([Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget)).
- **$10-50M:** Agent 09 gives 15-30% for "Growth Stage"; Agent 13 gives 45-60%. Conflict resolved in Section 6 -- the delta is due to Agent 13 measuring "used for some workloads" (non-exclusive) vs Agent 09 measuring "primary architecture." Consolidated at 30-45% as primary or significant architecture (not any-use).
- **$50-200M:** Agent 09 gives 10-20% for "Scale" tier; Agent 14 gives 25-35%. Agent 14's estimate is preferred because it reflects deeper analysis of this specific tier. Consolidated at 20-30%.
- **$200M+:** Agent 09 gives 5-15% as primary; Agent 15 gives 40-55% for "some workloads." For the primary-or-significant framing: 15-25%. The higher figure from Agent 15 reflects complementary serverless usage alongside K8s, not primary.
- **US Avg:** Agent 16 gives 45-55% for "some production workloads." Adjusted to 30-40% for primary or significant architecture, consistent with the tier-weighted average.
- **EU Avg:** Agent 17 gives 15-25% for EU AI SaaS. Lower than US due to GDPR sovereignty pressure reducing serverless appeal and absence of EU-native serverless providers.
- **Overall:** Agent 09 headline estimate is 25-40%. This aligns with the tier-weighted average. CNCF data shows only 11% use serverless as a primary computing framework ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), but this is narrower than the "primary or significant" definition used here.

### Managed Kubernetes (EKS, AKS, GKE)

*As primary or significant production architecture. Excludes self-managed K8s.*

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Estimate** | 20-35% (C:5) | 50-65% (C:6) | 55-65% (C:6) | 55-65% (C:7) | 50-60% (C:5) | 40-50% (C:3) | 45-55% (C:5) |

**Cell-level notes:**

- **<$10M:** Agents 10 and 12 converge. Agent 10 gives 25-40% for "$1M-$10M ARR" and 10-20% for pre-seed/seed; Agent 12 gives 20-35%. Consolidated at 20-35% for the full sub-$10M tier. CNCF data shows only 9% of K8s users are at companies with 500-1,000 employees ([Tigera/CNCF](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), suggesting low adoption at this scale.
- **$10-50M:** Agents 10 and 13 converge. Agent 10 gives 55-70%; Agent 13 gives 50-65%. Intersection: 55-65%. Consolidated at 50-65% to encompass the narrower range where both agree, noting Agent 13's lower bound is data-driven for this specific tier.
- **$50-200M:** Agents 10 and 14 converge. Agent 10 gives 70-85%; Agent 14 gives 55-65%. Conflict resolved in Section 6 -- Agent 10 measures K8s adoption (managed + self-managed), while Agent 14 isolates managed K8s. After separating managed from total K8s (subtracting 8-15% self-managed per [Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) 27% self-managed baseline), the estimates converge at 55-65%.
- **$200M+:** Agents 10 and 15 converge at 55-65%. Agent 10 gives 85-95% total K8s with implied ~60% managed; Agent 15 gives 55-65% managed explicitly. Supported by named company examples: Anthropic on GKE ([Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/)), Snowflake on EKS ([AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/)), Notion on EKS ([Notion Engineering Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake)), Cohere on OKE ([Oracle Case Study](https://www.oracle.com/cloud/technical-case-studies/cohere/)).
- **US Avg:** Agent 16 gives 55-65% for US AI SaaS with $10M+ ARR. Adjusted to 50-60% to include the large sub-$10M tier.
- **EU Avg:** Agent 17 gives 40-50% for managed K8s, noting AKS strength in EU enterprise. AKS maintains 28% adoption among businesses with 5,000+ employees ([Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)).
- **Overall:** Tier-weighted average across all segments. At ~45-55% overall, this is consistent with Gartner's 54% full/partial K8s implementation ([Gartner](https://www.gartner.com/en/documents/5405263)) and the CNCF data discounted for selection bias.

### Open/Self-Managed Kubernetes

*Self-hosted K8s without managed control plane. Includes on-prem and cloud IaaS self-managed.*

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Estimate** | 2-5% (C:5) | 5-12% (C:5) | 8-15% (C:4) | 25-35% (C:6) | 10-18% (C:4) | 20-30% (C:3) | 15-22% (C:4) |

**Cell-level notes:**

- **<$10M:** Agents 11 and 12 converge at 2-5%. Self-managed K8s requires dedicated infrastructure expertise that sub-$10M teams (5-30 engineers) lack.
- **$10-50M:** Agents 11 and 13 converge. Agent 11 gives 8-15% for "$10-200M"; Agent 13 gives 5-12%. Consolidated at 5-12% for this specific tier, noting it is the lower end of Agent 11's combined range.
- **$50-200M:** Agents 11 and 14 converge. Agent 11 gives 8-15% for "$10-200M"; Agent 14 gives 8-15%. Consolidated at 8-15%.
- **$200M+:** Agents 11 and 15 converge at 25-35%. Supported by named examples: OpenAI 7,500 nodes ([OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)), Databricks hybrid managed/self-managed running thousands of clusters ([Databricks Engineering Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)), Salesforce bare metal K8s ([Salesforce Engineering Blog](https://engineering.salesforce.com/tagged/kubernetes/)), HubSpot ([CNCF Case Study](https://www.cncf.io/case-studies/hubspot/)).
- **US Avg:** Agent 16 gives 10-18%. Lower than EU due to stronger hyperscaler ecosystem reducing self-management incentive.
- **EU Avg:** Agent 17 gives 20-30%. Higher than US due to GDPR sovereignty requirements, on-premises deployment demands, and EU-native infrastructure options (OVHcloud, Hetzner). Eurostat 2023 data shows EU enterprise cloud adoption at 45.2% ([Eurostat](https://ec.europa.eu/eurostat)), lower than US, which may push more companies toward self-managed options.
- **Overall:** Agent 11 headline estimate is 15-22%. Consistent with the tier-weighted average. Dynatrace reports 27% of cloud K8s clusters are self-managed ([Dynatrace Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), and Tigera/multiple sources report 37% self-managed across all environments ([Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)).

---

## 4. Classification Matrix

Each cell shows the evidence classification: D (Direct), I (Inferred), E (Estimated).

### Cloud-Native (Non-K8s Managed)

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Classification** | E | E | E | E | E | E | E |

### Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Classification** | E | E | I | I | E | E | E |

### Open/Self-Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Classification** | E | E | E | I | E | E | E |

**Classification rationale:**
- $50-200M and $200M+ managed K8s cells are classified Inferred because multiple Direct data points (CNCF 80% K8s production ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), Dynatrace 73% managed ([Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), 66% GenAI orgs on K8s ([CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/))) combine through documented logic to yield the estimate.
- $200M+ self-managed K8s is classified Inferred because named company examples (OpenAI ([OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)), Databricks ([Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)), Salesforce ([Salesforce Blog](https://engineering.salesforce.com/tagged/kubernetes/)), HubSpot ([CNCF](https://www.cncf.io/case-studies/hubspot/))) provide direct evidence, combined with the 27-37% self-managed baseline from Dynatrace/CNCF ([Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/), [Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)).
- All other cells are Estimated because they require judgment-based adjustments for AI SaaS specifically and/or for specific revenue tiers not measured by any source.
- No cell achieves Direct classification because no Wave 1 source directly segments "AI SaaS companies" by architecture and revenue tier.

---

## 5. Evidence Density Map

Rating: **Strong** (3+ independent sources converge) | **Moderate** (2 sources or indirect convergence) | **Weak** (1 source or pure estimation) | **None** (no supporting data)

### Cloud-Native (Non-K8s Managed)

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Density** | Moderate | Weak | Weak | Moderate | Moderate | Weak | Moderate |

### Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Density** | Weak | Moderate | Moderate | Strong | Moderate | Weak | Moderate |

### Open/Self-Managed Kubernetes

| | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| **Density** | Moderate | Weak | Weak | Strong | Weak | Weak | Moderate |

**Evidence density justification:**

- **Strong cells ($200M+ Managed K8s, $200M+ Open K8s):** Multiple named company examples (OpenAI ([OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)), Databricks ([Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)), Anthropic ([Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/)), Figma ([Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/)), Grammarly ([Grammarly Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), Snowflake ([AWS Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/)), Salesforce ([Salesforce Blog](https://engineering.salesforce.com/tagged/kubernetes/))), CNCF survey data ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), Dynatrace telemetry ([Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), Datadog observability data ([Datadog 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)), and SEC filing infrastructure signals all converge. These are the best-supported cells.
- **Moderate cells:** Supported by 2 converging but indirect sources (e.g., CNCF data + case study evidence, or Datadog telemetry + VC stage guidance).
- **Weak cells:** Supported by only 1 indirect source or pure estimation. Most $10-50M cells are weak because this tier falls between the well-documented enterprise segment and the qualitatively described startup segment.
- **EU cells are uniformly Weak or below:** Agent 17 explicitly rates its confidence at 3/10 and documents severe evidence gaps for EU-specific data. Only 2 EU AI company case studies exist in Wave 1 data: Stacks on GKE Autopilot in Amsterdam ([Google Cloud](https://cloud.google.com/customers/stacks)) and Medigold Health on Azure in the UK ([Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/)).

---

## 6. Conflict Log

| Cell | Agent A (Source) | Agent A Estimate | Agent B (Source) | Agent B Estimate | Delta | Resolution |
|---|---|---|---|---|---|---|
| Cloud-native, $10-50M | Agent 09 (Cloud-native deep dive) | 15-30% | Agent 13 ($10-50M tier) | 45-60% | 15-30pp | Agent 09 measures "primary architecture" while Agent 13 measures "used for some production workloads" (non-exclusive). Both are correct under their definitions. Consolidated at 30-45% for "primary or significant" framing. The non-exclusive nature of the categories means serverless use alongside K8s inflates Agent 13's number. |
| Managed K8s, $50-200M | Agent 10 (Managed K8s deep dive) | 70-85% | Agent 14 ($50-200M tier) | 55-65% | 10-20pp | Agent 10's 70-85% figure is for ALL K8s usage (managed + self-managed) at this tier, not managed K8s specifically. When Agent 14 isolates managed K8s from total K8s (subtracting 8-15% self-managed per [Dynatrace 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/) 27% self-managed baseline), the figures converge. Consolidated at 55-65% managed K8s. |
| Managed K8s, <$10M | Agent 10 (Managed K8s deep dive) | 25-40% for $1-10M | Agent 12 (<$10M tier) | 20-35% | 5pp | Minor discrepancy. Agent 10 covers $1-10M only; Agent 12 covers the full <$10M tier including pre-revenue. The lower range from Agent 12 reflects dilution from pre-revenue/seed companies. Consolidated at 20-35% for the full tier. |
| Cloud-native, $200M+ | Agent 09 (Cloud-native deep dive) | 5-15% as primary | Agent 15 ($200M+ tier) | 40-55% for some workloads | 25-40pp | Large delta due to definitional difference. Agent 09 measures primary architecture (where non-K8s is the dominant compute platform). Agent 15 measures any significant production use (which includes serverless as complement to K8s). Consolidated at 15-25% for "primary or significant," distinguishing from "any use" at 40-55%. The 40-55% "any use" figure is noted but not used as the primary estimate because it conflates complementary and primary usage. |
| Self-managed K8s, $10-50M | Agent 11 (Open K8s deep dive) | 8-15% (for $10-200M combined) | Agent 13 ($10-50M tier) | 5-12% | 3pp overlap | Agent 11's range is for a broader tier ($10-200M). The lower end of Agent 11's range (8%) falls within Agent 13's range (5-12%). Since Agent 13 analyzes this tier specifically, its estimate is preferred. Consolidated at 5-12%. |
| US cloud-native | Agent 09 (Cloud-native deep dive) | 25-40% overall | Agent 16 (US market) | 45-55% for some workloads | 5-15pp at the margins | Definitional difference again. Agent 16's estimate includes complementary serverless alongside K8s. After adjusting to "primary or significant," Agent 16's figure aligns closer to 30-40%. Consolidated at 30-40%. |
| EU self-managed K8s | Agent 11 (Open K8s deep dive) | 20-30% for EU | Agent 17 (EU market) | 20-30% | 0pp | Full convergence. Both agents arrive at 20-30% independently, supporting the higher EU estimate driven by sovereignty requirements. |
| EU managed K8s | Agent 10 (Managed K8s deep dive) | AKS ~30% in EU | Agent 17 (EU market) | 40-50% total managed K8s | N/A (different metrics) | Agent 10 provides vendor share within managed K8s; Agent 17 provides total managed K8s adoption. No conflict -- AKS at 30% share of the 40-50% managed K8s implies ~12-15% of all EU AI SaaS uses AKS. Complementary findings. |

---

## 7. Full Assumptions Register

Compiled from all 9 Wave 2 analysis files. Assumptions are numbered by source file.

### Cross-Cutting Assumptions (All Agents)

| ID | Assumption | Sources | Impact if Wrong | Confidence |
|---|---|---|---|---|
| X1 | CNCF survey respondents over-represent K8s adopters relative to the general AI SaaS population. CNCF reports 80% K8s production use ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) vs Gartner's 54% ([Gartner](https://www.gartner.com/en/documents/5405263)), suggesting 15-25pp inflation. | 09-A1, 10-A1, 11-A1, 13-A4 | Non-K8s adoption is higher than estimated by 10-20pp; K8s adoption is lower | Medium |
| X2 | AI SaaS companies are more cloud-native than the average enterprise surveyed by CNCF/Gartner | 10-A2, 14-A4, 15-A3 | If AI SaaS is not more cloud-native, K8s estimates may be too high | Medium |
| X3 | Engineering blog disclosures from Wave 1 are directionally representative despite publication bias. Documented migrations include Figma ([Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/)), Grammarly ([Grammarly Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), Salesforce ([Salesforce Blog](https://engineering.salesforce.com/tagged/kubernetes/)), HubSpot ([CNCF](https://www.cncf.io/case-studies/hubspot/)). | 09-A4, 10-A4, 11-A2, 13-A8, 14-A4, 15-A2 | If publication bias is extreme, all architecture estimates based on blog evidence are wrong | Medium |
| X4 | Revenue tiers can be mapped from employee count data using typical AI SaaS company ratios (~$200K-$500K ARR per employee) | 10-A3, 13-A1, 14-tier profile | Size-tier analysis could miscategorize companies | Medium |
| X5 | Absence of documented migrations away from K8s reflects actual low abandonment, not just publication bias | 09-A7, 10-A5, 11-A7, 14-A8 | If K8s abandonment is common but unpublished, migration trend analysis is biased | Low-Medium |
| X6 | Companies not running AI/ML on K8s (44% per CNCF ([CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/))) include a meaningful share using non-K8s cloud-native rather than VMs or no AI | 09-A2 | If most use VMs, cloud-native non-K8s is overestimated | Medium |
| X7 | The term "AI SaaS" includes both model-hosting companies and API-wrapper companies | 12-A9 | If restricted to model-hosting only, K8s adoption would be significantly higher across all tiers | High |
| X8 | 2024-2025 data is representative of the 2026 landscape | 12-A10 | AI infrastructure evolves rapidly; patterns may have shifted | Medium |

### Architecture-Specific Assumptions

| ID | Assumption | Source | Impact if Wrong | Confidence |
|---|---|---|---|---|
| CN1 | Serverless adoption decline (22% to 11% in CNCF ([CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/), [CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/))) reflects declining primary-framework use, not declining total use | 09-A5 | If total serverless is declining, cloud-native non-K8s estimates are too high | Medium |
| CN2 | GPU constraints on AWS Fargate significantly limit AI inference on that platform. Cloud Run and Azure Container Instances support GPU, but Fargate does not ([The New Stack](https://thenewstack.io/comparison-aws-fargate-vs-google-cloud-run-vs-azure-container-instances/)). | 09-A6 | If most AI inference is CPU-based (small/distilled models), Fargate is more viable than estimated | Medium |
| CN3 | PaaS/serverless-as-primary attenuates rapidly above $10M ARR | 09-A4, 12-A5 | If companies stay on PaaS longer, cloud-native non-K8s at $10-50M is higher | Low-Medium |
| MK1 | The 73% managed K8s figure from Dynatrace 2023 ([Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)) is directionally applicable to AI SaaS in 2025-2026 | 10-A6 | If managed share has shifted, vendor share estimates change | Medium-High |
| MK2 | AKS outperforms in EU relative to US due to Microsoft enterprise relationships and sovereign cloud | 10-A7, 17-A2 | No direct data supports AI SaaS AKS share in EU | Low |
| MK3 | Multi-cloud K8s adoption among AI SaaS is higher than the general 56% figure ([CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)) due to GPU scarcity | 10-A8 | If AI SaaS is not more multi-cloud, the 20-30% multi-cloud K8s estimate is inflated | Medium |
| OK1 | EU companies are more likely to self-manage K8s than US companies due to data sovereignty | 11-A5, 17-A2 | EU companies may use EU-region managed K8s instead | Medium |
| OK2 | OpenShift's $1.9B ARR ([IBM Q4 2025 Earnings](https://www.fool.com/earnings/call-transcripts/2026/01/28/ibm-ibm-q4-2025-earnings-call-transcript/)) is a proxy for enterprise self-managed K8s demand | 11-A6 | OpenShift includes managed offerings (ROSA, ARO); not all is self-managed | Medium |
| OK3 | K8s-native GPU clouds (CoreWeave ([Sacra Research](https://sacra.com/research/gpu-clouds-growing/))) are a hybrid managed/self-managed category | 11-A8 | If classified purely as managed, self-managed denominator changes | Medium |

### Tier-Specific Assumptions

| ID | Assumption | Source | Impact if Wrong | Confidence |
|---|---|---|---|---|
| T1 | Companies under $10M ARR have 5-30 engineers | 12-A1 | If larger, K8s adoption at this tier would be higher | Medium |
| T2 | Majority of sub-$10M AI SaaS call managed APIs rather than self-host models. CNCF data shows 37% use managed APIs vs 25% self-hosting for AI/ML models ([CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)). | 12-A4 | If more self-host, K8s adoption would be higher and cloud-native lower | Medium |
| T3 | VC-backed stage guidance (Maven Solutions ([Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget)), SaaStr) reflects actual startup behavior | 12-A5 | If companies adopt K8s early, managed K8s at <$10M could be 35-45% | Low-Medium |
| T4 | Companies at $10-50M ARR have 80-300 employees with 3-8 platform engineers | 13-A1, 13-A2 | Team size and K8s feasibility assessments would change | Medium |
| T5 | Companies at $50-200M on non-K8s are there by choice, not inertia | 14-A1 | Would overstate non-K8s as deliberate; actual % could be lower | Medium |
| T6 | At $200M+, engineering teams of 200+ with 20+ platform engineers are standard | 15-A1 | If teams are smaller, self-managed K8s estimate would be too high | Medium |
| T7 | Infrastructure spend excludes personnel but includes third-party AI API costs. AI SaaS companies see 40-50% of revenue in COGS ([Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026)) vs traditional SaaS at 15-30% ([SaaS Capital](https://www.saas-capital.com/blog-posts/what-should-be-included-in-cogs-for-my-saas-business/)). | 14-A9, 15-A6 | If personnel included, cost ranges shift upward 5-15% | Medium-High |

### Geography-Specific Assumptions

| ID | Assumption | Source | Impact if Wrong | Confidence |
|---|---|---|---|---|
| G1 | US-regulated AI SaaS companies default to managed K8s over self-managed for compliance | 16-A1 | If wrong, US self-managed share in regulated sectors is higher | Medium |
| G2 | The 70% North America serverless figure ([CNCF 2024 via StackShare](https://stackshare.io/aws-lambda)) and 11% CNCF global figure ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) measure different things | 16-A3 | If they measure the same thing, one figure is significantly wrong | High |
| G3 | GDPR creates structural pressure toward K8s over serverless in EU | 17-A2 | If GDPR is equally served by serverless, K8s advantage in EU is overstated | High |
| G4 | EU enterprise cloud adoption at 45.2% (Eurostat 2023) has not dramatically changed | 17-A3 | If adoption accelerated, the EU cloud gap may be smaller | Medium |
| G5 | US hyperscaler sovereign offerings are partial solutions (CLOUD Act jurisdiction issue persists) | 17-A4 | If resolved, push toward EU-native infrastructure weakens | Medium-High |
| G6 | Stacks (Amsterdam, GKE Autopilot ([Google Cloud](https://cloud.google.com/customers/stacks))) is not representative of all EU AI SaaS startups | 17-A6 | If representative, EU startup patterns mirror US managed K8s adoption | Low |

---

## 8. Citation Index

All citations trace through Wave 2 analyses to specific Wave 1 data points. Primary sources underlying the Wave 1 files are listed below.

### Wave 1 Source Files and Data Points Referenced Across Wave 2

| Wave 1 File | Data Points Most Cited | Referenced By (Wave 2 Files) |
|---|---|---|
| 01_cncf_survey.md | DP 1 (K8s 80% production) ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), DP 9 (56% multi-cloud) ([CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)), DP 11 (hybrid cloud) ([CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)), DP 13 (security challenges) ([CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)), DP 14 (training challenges) ([CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)), DP 15 (regional adoption) ([CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)), DP 17 (managed K8s 79%) ([CNCF 2021](https://www.cncf.io/announcements/2022/02/10/cncf-sees-record-kubernetes-and-container-adoption-in-2021-cloud-native-survey/)), DP 18 (EKS 39%) ([CNCF 2021](https://www.cncf.io/reports/cncf-annual-survey-2021/)), DP 19 (90% managed) ([InfoWorld](https://www.infoworld.com/article/2334477/cncf-survey-managed-kubernetes-becomes-the-norm.html)), DP 20 (on-prem vs cloud) ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), DP 21 (66% GenAI on K8s) ([CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)), DP 22 (44% no AI on K8s) ([CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)), DP 24 (41% AI devs cloud native) ([CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)), DP 25 (30% MLaaS) ([CNCF 2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)), DP 27 (9% at 500-1K employees) ([Command Linux](https://commandlinux.com/statistics/linux-container-kubernetes-adoption-statistics/)), DP 28 (91% at 1K+ employees) ([Command Linux](https://commandlinux.com/statistics/linux-container-kubernetes-adoption-statistics/)), DP 31 (11% serverless) ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), DP 32 (serverless decline) ([CNCF 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)), DP 36 (iFLYTEK GPU scheduling) ([CNCF](https://www.cncf.io/announcements/2025/06/09/iflytek-wins-cncf-end-user-case-study-contest-for-scalable-ai-infrastructure-breakthroughs-with-volcano/)), DP 37 (61% managed clusters) ([Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), DP 38 (EKS 22% share) ([Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), DP 39 (cluster counts) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 02_analyst_reports.md | DP 1 (Dynatrace 73% managed) ([Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)), DP 2 (63% managed all-envs) ([Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), DP 6 (Gartner 54% K8s) ([Gartner](https://www.gartner.com/en/documents/5405263)), DP 8 (66% GenAI on K8s) ([CNCF 2025](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)), DP 11 (AI hosting split 37/25/13) ([CNCF 2025](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)), DP 12 (Gartner 75% containers by 2027) ([Gartner via Azure Blog](https://azure.microsoft.com/en-us/blog/microsoft-is-a-leader-in-the-2025-gartner-magic-quadrant-for-container-management/)), DP 13 (68% Cloud Run on GCP) ([Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/)), DP 14 (Lambda 65% AWS) ([Datadog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)), DP 15 (Cloud Run 70% GCP) ([Datadog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)), DP 16 (App Service 56% Azure) ([Datadog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)), DP 17 (66% serverless + orchestration) ([Datadog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)), DP 29 (2.4 cloud providers) ([Flexera](https://info.flexera.com/CM-REPORT-State-of-the-Cloud)), DP 30 (65% K8s multi-environment) ([The New Stack](https://thenewstack.io/5-tech-predictions-for-2026-from-ai-inference-to-kubernetes/)), DP 40 (resource over-provisioning) ([Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/)), DP 41 (64% HPA) ([Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/)), DP 43 (AI 7% containerized workloads) ([Datadog](https://www.datadoghq.com/state-of-containers-and-serverless/)), DP 46 (79% AI/ML PaaS) ([Flexera](https://info.flexera.com/CM-REPORT-State-of-the-Cloud)) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 03_job_postings.md | DP 2 (K8s 28% of DevOps) ([Brokee](https://brokee.io/blog/essential-devops-statistics-and-trends-for-hiring-in-2024)), DP 3 (platform eng 8.35%) ([DevOpsCube](https://devopscube.com/kubernetes-and-devops-job-market/)), DP 4 (73% managed clusters) ([kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q1)), DP 7 (91% K8s at 1K+ employees) ([Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), DP 8 (platform eng growth 32%) ([kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q1)), DP 9 (66-70% North America) ([kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q2)), DP 15 (job co-occurrence) ([Refonte Learning](https://www.refontelearning.com/blog/cloud-engineering-in-2025-key-skills-employers-demand)), DP 16 (K8s salary $167K) ([kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q1)), DP 20 (60% senior DevOps) ([DevOpsCube](https://devopscube.com/kubernetes-and-devops-job-market/)) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 04_tech_blogs.md | Figma ECS to EKS migration ([Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/)), Grammarly EC2 to EKS ([Grammarly Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), OpenAI 7,500 nodes ([OpenAI Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)), Databricks hybrid K8s ([Databricks Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)), Salesforce bare metal K8s ([Salesforce Blog](https://engineering.salesforce.com/tagged/kubernetes/)), HubSpot self-managed K8s ([CNCF](https://www.cncf.io/case-studies/hubspot/)), Anthropic GKE ([Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/)), Cohere OKE ([Oracle](https://www.oracle.com/cloud/technical-case-studies/cohere/)), Snowflake EKS ([AWS Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/)), Notion EKS ([Notion Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake)), Elastic Crossplane ([Elastic Blog](https://www.elastic.co/blog/journey-to-build-elastic-cloud-serverless)), Jasper K8s abstraction ([Jasper Blog](https://www.jasper.ai/blog/devx-renaissance-the-death-of-devops)), Contextual AI GKE ([Google Cloud](https://cloud.google.com/customers/contextualai)), Stacks GKE Autopilot ([Google Cloud](https://cloud.google.com/customers/stacks)), GKE 130K-node cluster ([WebProNews](https://www.webpronews.com/googles-130000-node-kubernetes-colossus-engineering-the-future-of-ai-scale-computing/)), AKS Fleet Manager ([AKS Blog](https://blog.aks.azure.com/2025/04/02/Scaling-Kubernetes-for-AI-and-Data-intensive-Workloads)), EKS 100K nodes ([InfoQ](https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/)), CNCF AI Conformance ([CNCF](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/)) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 05_cloud_vendor_cases.md | CS 1-4 (EKS AI cases: [Flawless](https://aws.amazon.com/solutions/case-studies/flawless-case-study/), [Liquid Analytics](https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/), [Instabase](https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/), [Sonantic](https://www.bionconsulting.com/case-studies/scaling-ai-driven-voice-technology-with-aws-and-eks)), CS 10-12 (ECS/Fargate SaaS: [Autodesk](https://aws.amazon.com/solutions/case-studies/autodesk-serverless-case-study/), [BILL](https://aws.amazon.com/solutions/case-studies/bill-ecs-case-study/), [Smartsheet](https://aws.amazon.com/solutions/case-studies/smartsheet-ecs-fargate-case-study/)), CS 16-17 (AKS cases: [Duck Creek](https://learn.microsoft.com/en-us/azure/aks/windows-aks-customer-stories), [PTC](https://www.microsoft.com/en/customers/story/22856-ptc-azure-database-for-postgresql)), CS 18 (Azure Container Apps: [Coca-Cola](https://azure.microsoft.com/en-us/blog/from-idea-to-impact-real-world-success-stories-of-building-intelligent-apps-with-azure/)), CS 20 (Medigold UK) ([Azure Blog](https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/)), CS 21-22 (GKE cases: [Picterra](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders), [Stacks](https://cloud.google.com/customers/stacks)), OpenAI $250B Azure commitment ([OpenAI](https://openai.com/index/next-chapter-of-microsoft-openai-partnership/)), EKS 100K node support ([InfoQ](https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/)) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 06_stackshare_github.md | K8s 96% enterprise adoption ([Red Hat via Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)), managed K8s 67% cloud-hosted up from 45% in 2022 ([Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)), GKE 32% adoption ([Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)), AKS 28% among 5K+ employee orgs ([Jeevi Academy](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)), serverless disconnect 70% NA vs 11% global ([CNCF 2024 via StackShare](https://stackshare.io/aws-lambda) vs [CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), GPU support comparison Fargate lacks GPU ([The New Stack](https://thenewstack.io/comparison-aws-fargate-vs-google-cloud-run-vs-azure-container-instances/)), 87% container image vulnerabilities ([Sysdig 2023](https://www.sysdig.com/press-releases/sysdig-2023-usage-report)), 77% GitOps adoption ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)), 48% service mesh struggle ([Market Growth Reports](https://www.marketgrowthreports.com/market-reports/service-mesh-tools-software-market-100476)) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 07_sec_earnings.md | AWS $128.7B revenue ([Computer Weekly](https://www.computerweekly.com/news/366638765/AWS-Q4-results-Public-cloud-giant-continues-to-reap-rewards-of-enterprise-demand-for-AI-and-IaaS)), AWS 38% IaaS share, Azure 24%, GCP 9% ([CIO Dive](https://www.ciodive.com/news/cloud-infrastructure-services-iaas-growth-aws-microsoft-google/757343/)), Snowflake $2.5B commitment ([Partner Insight](https://www.partnerinsight.io/post/snowflake-doubling-down-on-cloud-commitments)), Palantir $1.95B commitment ([Palantir 10-K](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000022/pltr-20241231.htm)), AI SaaS 40-50% COGS ([Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026)), traditional SaaS 6-12% hosting ([FlowCog](https://flowcog.com/saas-cogs-cost-of-revenue-cogs/)), AI gross margins 50-65% ([Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026)), Replit margins ([Monetizely](https://www.getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026)), OpenShift $1.9B ARR ([IBM Q4 2025 Earnings](https://www.fool.com/earnings/call-transcripts/2026/01/28/ibm-ibm-q4-2025-earnings-call-transcript/)), GPU spending 10% to 14% of EC2 ([Datadog Cloud Costs 2024](https://www.datadoghq.com/about/latest-news/press-releases/datadogs-state-of-cloud-costs-2024-report-finds-spending-on-gpu-instances-growing-40-as-organizations-experiment-with-ai/)), 83% idle container costs ([Datadog Cloud Costs 2024](https://www.datadoghq.com/about/latest-news/press-releases/datadogs-state-of-cloud-costs-2024-report-finds-spending-on-gpu-instances-growing-40-as-organizations-experiment-with-ai/)), 89% CFOs reporting cloud cost impact ([CIO Magazine](https://www.cio.com/article/4110708/cloud-costs-now-no-2-expense-at-midsize-it-companies-behind-labor.html)) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |
| 08_vc_startup_db.md | Seed-stage K8s avoidance guidance ([Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget)), Maven Solutions infra recommendations ([Maven Solutions](https://www.mavensolutions.tech/blog/cloud-infrastructure-on-a-startup-budget)), YC 66% AI batch ([Ellty](https://www.ellty.com/blog/san-francisco-cloud-investors)), YC 58% Azure credits ([CNBC](https://www.cnbc.com/2024/08/02/microsoft-touts-cloud-momentum-from-y-combinator-startups.html)), CoreWeave $12B OpenAI contract, 250K GPUs, 62% cost advantage ([Sacra Research](https://sacra.com/research/gpu-clouds-growing/)), CAST AI 50%+ K8s savings ([CAST AI](https://cast.ai/blog/cast-ai-raises-35-million-to-optimize-kubernetes-cost/)), AI infra costs 24-80% of revenue ([Hidden Stack Analysis](https://www.tonygraysonvet.com/post/the-hidden-stack-ai-infrastructure-spending)), Bessemer 25% early-stage margins ([Monetizely](https://www.getmonetizely.com/getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026)), Platform engineering 55% adoption ([Platform Engineering](https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4)), 65% IDP adoption ([Cycloid](https://www.cycloid.io/blog/top-11-internal-developer-platforms-idps-in-2025/)), 71% time-to-market improvement ([CloudBees](https://www.cloudbees.com/platform-engineering-research)), $37B GenAI enterprise spending 2025 ([Menlo Ventures](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)) | 09, 10, 11, 12, 13, 14, 15, 16, 17 |

### Primary Sources (Underlying Wave 1 Data)

**Surveys and Telemetry:**
- CNCF Annual Surveys 2021-2024/2025 (n=750-3,800) ([2024](https://www.cncf.io/reports/cncf-annual-survey-2024/), [2023](https://www.cncf.io/reports/cncf-annual-survey-2023/), [2021](https://www.cncf.io/announcements/2022/02/10/cncf-sees-record-kubernetes-and-container-adoption-in-2021-cloud-native-survey/), [2025 Announcement](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/))
- Datadog State of Containers and Serverless 2025 (production telemetry, not survey) ([Report](https://www.datadoghq.com/state-of-containers-and-serverless/), [Blog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/))
- Dynatrace Kubernetes in the Wild Report 2023 (observability telemetry) ([Dynatrace](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/))
- Stack Overflow 2025 Developer Survey ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
- Flexera State of the Cloud Report 2025 ([Flexera](https://info.flexera.com/CM-REPORT-State-of-the-Cloud))
- Red Hat Kubernetes Adoption Survey 2024 ([Red Hat](https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview))
- Gartner Container Management Magic Quadrant 2025 ([Gartner](https://www.gartner.com/en/documents/5405263), [Azure Blog](https://azure.microsoft.com/en-us/blog/microsoft-is-a-leader-in-the-2025-gartner-magic-quadrant-for-container-management/))
- Sysdig 2023 Container Security Report ([Sysdig](https://www.sysdig.com/press-releases/sysdig-2023-usage-report))
- HashiCorp State of Cloud Strategy Survey ([HashiCorp](https://www.hashicorp.com/en/state-of-the-cloud))

**Industry/Analyst Reports:**
- CB Insights State of AI 2025 ([CB Insights](https://www.cbinsights.com/research/report/ai-trends-2025/))
- Bessemer Venture Partners Cloud 100 2024 ([Bessemer](https://www.bvp.com/atlas/the-cloud-100-benchmarks-report))
- Menlo Ventures State of Generative AI 2025 (n=495 US enterprise AI decision-makers) ([Menlo Ventures](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/))
- Sacra Research GPU Clouds Report ([Sacra](https://sacra.com/research/gpu-clouds-growing/))
- SaaS Capital DevOps Spending Benchmark ([SaaS Capital](https://www.saas-capital.com/blog-posts/spending-benchmarks-for-private-b2b-saas-companies/))

**Company Disclosures:**
- SEC 10-K filings: Snowflake ([Partner Insight](https://www.partnerinsight.io/post/snowflake-doubling-down-on-cloud-commitments)), Palantir ([SEC](https://www.sec.gov/Archives/edgar/data/1321655/000132165525000022/pltr-20241231.htm)), Salesforce ([Salesforce](https://www.salesforce.com/news/press-releases/2023/11/27/aws-data-ai-strategic-partnership-expansion/)), ServiceNow ([SEC](https://www.sec.gov/Archives/edgar/data/1373715/000137371525000010/now-20241231.htm)), Zoom ([The Register](https://www.theregister.com/2021/01/13/zoom_prospectus_reveals_colo_infrastructure/)), Atlassian ([BusinessWire](https://www.businesswire.com/news/home/20241204973894/en/Atlassian-and-Amazon-Web-Services-Announce-Strategic-Collaboration-Agreement-to-Drive-Enterprise-Cloud-Migration)), Elastic ([Elastic IR](https://ir.elastic.co/news/news-details/2024/Elastic-Reports-Fourth-Quarter-and-Fiscal-2024-Financial-Results/))
- IBM Q4 2025 Earnings (OpenShift ARR $1.9B) ([Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/01/28/ibm-ibm-q4-2025-earnings-call-transcript/))
- Engineering blogs: OpenAI ([Blog](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)), Databricks ([Blog](https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators)), Figma ([Blog](https://www.figma.com/blog/migrating-onto-kubernetes/)), Grammarly ([Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)), Anthropic ([Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/)), Cohere ([Oracle](https://www.oracle.com/cloud/technical-case-studies/cohere/)), Salesforce ([Blog](https://engineering.salesforce.com/tagged/kubernetes/)), HubSpot ([CNCF](https://www.cncf.io/case-studies/hubspot/)), Snowflake ([AWS Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/)), Notion ([Blog](https://www.notion.com/blog/building-and-scaling-notions-data-lake)), Elastic ([Blog](https://www.elastic.co/blog/journey-to-build-elastic-cloud-serverless)), Jasper ([Blog](https://www.jasper.ai/blog/devx-renaissance-the-death-of-devops)), Hugging Face ([Blog](https://huggingface.co/blog/)), Contextual AI ([Google Cloud](https://cloud.google.com/customers/contextualai))
- Cloud vendor case studies: AWS ([Case Studies](https://aws.amazon.com/solutions/case-studies/)), Azure ([Customer Stories](https://www.microsoft.com/en/customers)), GCP ([Customers](https://cloud.google.com/customers))

**VC/Startup Data:**
- Y Combinator batch analysis (Winter 2024) ([CNBC](https://www.cnbc.com/2024/08/02/microsoft-touts-cloud-momentum-from-y-combinator-startups.html))
- CoreWeave company disclosures ($12B OpenAI contract, 250K GPUs, $2.2B EU investment) ([Sacra](https://sacra.com/research/gpu-clouds-growing/))
- CAST AI, Spectro Cloud, Komodor growth data ([CAST AI](https://cast.ai/blog/cast-ai-raises-35-million-to-optimize-kubernetes-cost/), [Crunchbase/Spectro Cloud](https://news.crunchbase.com/ai/big-funding-trends-charts-eoy-2025/), [Komodor](https://komodor.com/blog/komodor-reports-record-business-results-for-2024/))
- Fireworks AI, Modal Labs company data ([Fireworks AI](https://fireworks.ai/blog/series-c), [Modal Labs](https://siliconangle.com/2025/09/29/modal-labs-raises-80m-simplify-cloud-ai-infrastructure-programmable-building-blocks/))
- Mistral AI Series C ($1.5B, $11.7B valuation) ([CB Insights](https://www.cbinsights.com/research/report/ai-trends-2025/))

**EU-Specific Sources (introduced in Wave 2, file 17):**
- Eurostat 2023: EU enterprise cloud adoption (45.2%) ([Eurostat](https://ec.europa.eu/eurostat))
- Gartner 2025: 61% of EU CIOs increasing local cloud/AI provider reliance ([Gartner Press Release, Nov 2025](https://www.gartner.com/en/newsroom/press-releases/2025-11-12-gartner-survey-reveals-geopolitics-will-drive-61-percent-of-cios-and-information-technology-leaders-in-western-europe-to-increase-reliance-on-local-cloud-providers))
- Gaia-X: 180+ data spaces, sovereignty frameworks ([Gaia-X Summit 2025](https://gaia-x.eu/gaia-x-enters-season-two-of-dataspaces-and-digital-ecosystems-with-summit-2025/))
- French government: EUR 1.8B cloud sovereignty allocation ([Cloud Computing News](https://www.cloudcomputing-news.net/news/france-unveils-e1-8-billion-fund-for-nations-cloud-sector/))
- AWS European Sovereign Cloud (Germany launch, EUR 7.8B investment) ([AWS Blog](https://aws.amazon.com/blogs/security/aws-plans-to-invest-e7-8b-into-the-aws-european-sovereign-cloud-set-to-launch-by-the-end-of-2025/))
- EU AI Act compliance timeline (August 2, 2026) ([EU AI Act Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/))
- EU Data Act (effective September 12, 2025) ([European Commission Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/data-act))

---

## 9. Known Limitations

### Fundamental Limitations (Cannot Be Resolved with Available Data)

1. **No direct measurement exists for the core research question.** No survey, telemetry source, or analyst report directly segments "AI SaaS companies" by infrastructure architecture and revenue tier. Every cell in the estimate matrix is derived through inference or estimation. A purpose-built survey of 200+ AI SaaS CTOs by ARR tier and geography would be required to move any cell from Estimated to Direct.

2. **CNCF survey selection bias is unquantifiable.** CNCF surveys (the richest data source) are answered by self-selected cloud-native practitioners. The bias inflates K8s adoption by an estimated 15-25 percentage points (CNCF 80-82% ([CNCF 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) vs Gartner 54% ([Gartner](https://www.gartner.com/en/documents/5405263))). We do not know the exact magnitude, making all K8s estimates inherently uncertain.

3. **Companies under 500 employees are invisible in survey data.** CNCF data stops at 500-1,000 employees (9% of K8s users) ([Tigera/CNCF](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)). Most AI SaaS companies under $50M ARR have fewer than 500 employees. This means the sub-$10M and $10-50M tier estimates are extrapolated from enterprise data applied downward, not measured.

4. **Publication bias systematically over-represents Kubernetes.** Companies that publish engineering blogs about infrastructure overwhelmingly discuss Kubernetes. Companies using ECS, Lambda, Heroku, or PaaS rarely publish infrastructure case studies. This creates an information asymmetry where K8s appears more dominant than it may actually be.

5. **No failure or abandonment data exists.** Zero Wave 1 sources document companies that tried Kubernetes and abandoned it, or companies that chose serverless and later wished they had chosen K8s. Survivorship bias means we see only architecture successes.

6. **EU data is extremely sparse.** Only 2 EU AI company case studies exist in Wave 1 data: Stacks on GKE ([Google Cloud](https://cloud.google.com/customers/stacks)) and Medigold on Azure ([Azure Blog](https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/)). Agent 17 rates its overall confidence at 3/10. All EU-specific architecture estimates carry very high uncertainty.

7. **The "AI SaaS" category is heterogeneous.** API-wrapper companies (calling OpenAI/Anthropic) have fundamentally different infrastructure needs than model-hosting companies (self-hosting inference). No source segments these sub-categories, yet their architecture choices diverge dramatically. This heterogeneity adds 10-20 percentage points of uncertainty to every estimate.

### Methodological Limitations

8. **Non-exclusive categories create ambiguity.** Architecture categories are non-exclusive -- companies use multiple simultaneously. The estimate matrix measures "primary or significant" usage, but this threshold is judgment-based. The same company could be counted in both "managed K8s" and "cloud-native non-K8s" if it runs K8s for core services and Lambda for event processing.

9. **Revenue tier boundaries are arbitrary.** The $10M, $50M, and $200M breakpoints do not correspond to natural architectural inflection points. The transition from non-K8s to K8s is company-specific and depends on workload type, team composition, and model hosting choices -- not revenue alone.

10. **Temporal snapshot risk.** All estimates reflect 2024-2025 data. AI infrastructure is evolving rapidly. Managed K8s providers added AI-specific features (EKS 100K nodes ([InfoQ](https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/)), GKE 130K nodes ([WebProNews](https://www.webpronews.com/googles-130000-node-kubernetes-colossus-engineering-the-future-of-ai-scale-computing/)), CNCF AI Conformance ([CNCF](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/))) during the data collection period. Adoption patterns may shift materially within 12-18 months.

11. **US-centric source bias is pervasive.** Wave 1 files are predominantly sourced from US companies, US analysts, and US-based surveys. The "US market" analysis (Agent 16) has better data quality than the "EU market" analysis (Agent 17) not because US patterns are better measured, but because the sources themselves are US-originated.

### Specific Data Gaps That Would Most Improve the Analysis

| Gap | Would Improve | Priority |
|---|---|---|
| Direct survey of 200+ AI SaaS companies by ARR tier | All cells | Critical |
| Datadog/similar telemetry segmented for AI/ML companies | All cells | Critical |
| ECS/Fargate adoption rate (comparable to Lambda 65% data ([Datadog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/))) | Cloud-native non-K8s cells | High |
| Architecture data for companies under 500 employees | <$10M and $10-50M cells | High |
| EU-specific managed vs self-managed K8s split | EU Avg cells | High |
| Workload-level architecture data (not just org-level) | Multi-architecture overlap estimates | High |
| API-wrapper vs model-hosting split by revenue tier | All tier cells | High |
| K8s failure/abandonment rates | Migration trend analysis | Medium |
| Cost comparison: K8s TCO vs serverless for AI workloads by tier | Infrastructure spend analysis | Medium |
| EU AI Act compliance infrastructure case studies | EU Avg cells (emerging after Aug 2026) | Medium |

---

## Appendix A: Agent-Level Confidence Scores

| Wave 2 File | Agent Focus | Self-Reported Confidence | Consolidator Assessment |
|---|---|---|---|
| 09 | Cloud-native non-K8s deep dive | 4/10 | 4/10 -- Agrees. Heavy reliance on gap analysis ("if X% use K8s, then 100-X% might not"). Publication bias under-represents non-K8s. |
| 10 | Managed K8s deep dive | 5/10 | 5/10 -- Agrees. Strongest evidence base of any architecture agent due to CNCF/Dynatrace/Datadog convergence. Still no direct AI SaaS segmentation. |
| 11 | Open/self-managed K8s deep dive | 4/10 | 4/10 -- Agrees. Directional trend (declining self-managed) is well-supported at 7/10. Specific percentages are low-confidence. |
| 12 | Under $10M tier | 5.5/10 | 5/10 -- Slightly lower than self-reported. Excellent qualitative analysis but all quantitative estimates are pure estimation for this invisible tier. |
| 13 | $10-50M tier | 5/10 | 5/10 -- Agrees. Good structural analysis of decision drivers. Core percentages are estimated from adjacent data. |
| 14 | $50-200M tier | 5/10 | 5/10 -- Agrees. Moderate evidence from engineering blogs and case studies. Still no direct survey data for this tier. |
| 15 | $200M+ tier | 6/10 | 6/10 -- Agrees. Best-supported tier due to SEC filings, engineering blog disclosures, and named company examples. |
| 16 | US market | 5/10 | 5/10 -- Agrees. US data is better but still indirect for architecture-specific questions. Strong cloud vendor market share data ([CIO Dive](https://www.ciodive.com/news/cloud-infrastructure-services-iaas-growth-aws-microsoft-google/757343/)). |
| 17 | EU market | 3/10 | 3/10 -- Agrees. Extremely limited EU-specific evidence. Logical structural arguments about GDPR impact but unquantified. |

---

## Appendix B: Reconciled Serverless Adoption Data

A recurring conflict across agents is the discrepancy in serverless adoption figures. This appendix documents the resolution.

| Source | Figure | Scope | Classification |
|---|---|---|---|
| Datadog (via 02_analyst_reports.md, DP 14) ([Datadog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)) | 65% of AWS customers use Lambda | Any Lambda invocation across all AWS customers | Direct (telemetry) |
| Datadog (via 02_analyst_reports.md, DP 15) ([Datadog](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)) | 70% of GCP customers use Cloud Run | Any Cloud Run usage across all GCP customers | Direct (telemetry) |
| CNCF 2024 (via 01_cncf_survey.md, DP 31) ([CNCF Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)) | 11% use serverless computing frameworks | Serverless as a primary computing framework among CNCF respondents | Direct (survey) |
| CNCF 2023 (via 01_cncf_survey.md, DP 32) ([CNCF Annual Survey 2023](https://www.cncf.io/reports/cncf-annual-survey-2023/)) | 13% (down from 22% in 2022) | Serverless as a primary computing framework | Direct (survey) |
| CNCF 2024 NA (via 06_stackshare_github.md) ([StackShare](https://stackshare.io/aws-lambda)) | 70% of NA enterprises run production serverless | Any production serverless use among North American enterprises | Direct (survey) |

**Resolution:** These figures are not contradictory. They measure different things:
- **65-70% (Datadog):** "Any use at all" -- including event triggers, background processing, CI/CD. This is the broadest measure.
- **70% (CNCF NA):** "Production loads on serverless" in North America -- broader than primary framework, narrower than any use.
- **11-13% (CNCF global):** "Serverless as a primary computing framework" -- the narrowest measure.

For the estimate matrix, we use a definition closest to "primary or significant production architecture," which falls between the 11% (too narrow) and 70% (too broad) figures. This supports the 25-40% overall estimate for cloud-native non-K8s as primary or significant architecture.

---

**Document Version:** 1.0
**Compiled:** 2026-02-12
**Methodology:** Cross-agent consolidation of 9 Wave 2 analysis files, each synthesizing 8 Wave 1 fact-gathering files
**Total Wave 1 Data Points Referenced:** 200+
**Total Assumptions Documented:** 30+
**Total Evidence Gaps Identified:** 20+
