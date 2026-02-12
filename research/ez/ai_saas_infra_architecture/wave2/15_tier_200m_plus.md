# Infrastructure Architecture Analysis: AI SaaS Companies at $200M+ ARR

## Tier Context

**Revenue Tier:** $200M+ ARR
**Characteristics:** Enterprise scale, large platform teams (50-200+ infrastructure engineers), multi-cloud strategies, custom Kubernetes platforms, regulatory requirements, multi-year cloud commitments ($1.95B-$2.5B+), infrastructure spend 25-50% of revenue for AI-first companies.

**Date:** 2026-02-12
**Methodology:** Synthesis of 8 Wave 1 fact-gathering files covering CNCF surveys, analyst reports, job postings, engineering blogs, cloud vendor case studies, StackShare/GitHub signals, SEC/earnings data, and VC/startup database research.

---

## Executive Summary

AI SaaS companies at $200M+ ARR overwhelmingly use Kubernetes as their primary infrastructure orchestration layer, with an estimated 85-95% adoption rate. Managed Kubernetes (EKS/GKE/AKS) is the dominant pattern at 55-65% of companies, while self-managed/open Kubernetes appears at 25-35%. Cloud-native non-K8s managed services (serverless, PaaS, ECS/Fargate, Cloud Run) are used by 40-55% of companies, but nearly always as a secondary architecture alongside Kubernetes rather than as the primary platform. Multi-architecture usage is the norm: an estimated 70-85% of companies in this tier run multiple architecture patterns simultaneously. Infrastructure spend ranges from 25-50% of revenue for AI-first companies versus 10-20% for traditional SaaS at this scale. Engineering teams capable of running self-managed K8s are standard at this tier, with dedicated platform engineering organizations of 20-100+ engineers.

---

## Architecture Adoption Estimates

### 1. Cloud-Native Non-K8s Managed Services (Serverless, PaaS, ECS/Fargate, Cloud Run)

**Estimate: 40-55% of $200M+ AI SaaS companies use non-K8s managed services for SOME workloads**

**Classification:** Estimated (judgment + reasoning from multiple indirect data points)

**Evidence Chain:**

- Based on [02_analyst_reports.md, Data Point 17], which shows "66% of organizations using serverless functions also use container orchestration," I infer that at the $200M+ tier, serverless is used as a complement to Kubernetes, not a replacement. This is consistent with the hybrid pattern.

- Based on [02_analyst_reports.md, Data Points 14-16], which show AWS Lambda at 65% of AWS customers, Google Cloud Run at 70% of GCP customers, and Azure App Service at 56% of Azure customers (Datadog telemetry 2025), I infer that large AI SaaS companies, which are AWS/GCP/Azure customers, have high exposure to serverless services. However, these are organization-level adoption rates, not primary architecture indicators.

- Based on [05_cloud_vendor_cases.md, Case Studies 10-12], which document Autodesk (ECS/Fargate), BILL (ECS/Fargate), and Smartsheet (ECS/Fargate) as SaaS companies using non-K8s container platforms, I note these are traditional SaaS companies, not AI-first. The case studies found zero AI SaaS companies at $200M+ ARR using non-K8s managed services as their PRIMARY architecture.

- Based on [01_cncf_survey.md, Data Points 31-32], which show serverless framework adoption dropping from 22% (2022) to 13% (2023) to 11% (2024) in CNCF surveys, I infer that serverless as a primary framework is declining, though this data reflects CNCF respondents who skew toward K8s users.

- Based on [06_stackshare_github.md, Serverless Adoption data], which shows "Close to 70% of enterprises in North America operate production loads on serverless systems" but "only 11% of CNCF respondents use serverless computing frameworks," I note a significant definitional conflict. The 70% figure likely counts any use of Lambda/Cloud Functions for ancillary workloads, while the 11% figure measures serverless as a primary compute framework.

**Reasoning:** At $200M+ ARR, companies have the engineering maturity and team size to run Kubernetes. Serverless and non-K8s managed services persist for specific workloads (event processing, API gateways, lightweight microservices, data pipelines) but are rarely the primary compute platform for AI inference or model serving at this scale. The GPU requirements of AI workloads further limit serverless utility, since based on [06_stackshare_github.md, Serverless Container Platforms Comparison], "AWS Fargate does not support GPU-based workloads" while "Google Cloud Run and Azure Container Instances both support GPU-based workloads."

**Confidence: 5/10** -- No direct data for AI SaaS at $200M+ ARR. Estimate synthesized from general enterprise adoption rates, vendor case studies, and the structural limitation that serverless cannot serve GPU-heavy AI inference at scale.

---

### 2. Managed Kubernetes (EKS, GKE, AKS)

**Estimate: 55-65% of $200M+ AI SaaS companies use managed Kubernetes as a primary or major architecture**

**Classification:** Inferred (derived through stated logic from multiple data points)

**Evidence Chain:**

- Based on [02_analyst_reports.md, Data Point 1], which shows "73% of cloud Kubernetes clusters are built on top of managed distributions from hyperscalers" (Dynatrace 2023), I establish the baseline that managed K8s is the dominant pattern for cloud Kubernetes deployments across all organizations.

- Based on [04_tech_blogs.md, multiple case studies], which document Anthropic using GKE, Cohere using OKE, Grammarly migrating EC2 to EKS, Figma migrating ECS to EKS, Snowflake using EKS, and Notion using EKS, I identify a strong pattern of AI SaaS and data platform companies choosing managed Kubernetes. These are direct, named company disclosures.

- Based on [05_cloud_vendor_cases.md, Case Studies 1-4], which document Flawless (EKS), Liquid Analytics (EKS), Instabase (EKS), and Sonantic (EKS with GPU) as AI companies using managed K8s, I confirm the pattern extends across company sizes.

- Based on [01_cncf_survey.md, Data Point 37], which shows "Managed Kubernetes services (EKS, GKE, AKS) now host 61% of all production clusters," I note this is a cluster-level metric (not company-level), but directionally supports managed K8s dominance.

- Based on [06_stackshare_github.md, Managed Kubernetes data], which shows "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022," I confirm the accelerating shift toward managed services.

- Based on [03_job_postings.md, Data Point 4], which shows "73% of cloud Kubernetes clusters are built on managed distributions from hyperscalers like AWS EKS, Azure AKS, or GKE," I cross-validate the Dynatrace finding from a job market analysis perspective.

**Reasoning:** At $200M+ ARR, companies have both the scale to justify Kubernetes and the financial resources to use managed services. The engineering economics favor managed K8s: platform teams focus on application-layer tooling (internal developer platforms, ML pipelines, CI/CD) while offloading control plane management to cloud providers. However, the percentage at this tier is likely LOWER than the general 73% managed figure because $200M+ companies are more likely to also run self-managed K8s for specialized workloads (discussed below). Some companies at this tier (like Databricks) use a hybrid of managed and self-managed.

**Confidence: 7/10** -- Strong convergence across multiple independent sources (CNCF, Dynatrace, Datadog, engineering blogs). Named company examples validate the pattern. Adjusted downward from general enterprise rates because $200M+ AI SaaS companies are more likely to supplement managed K8s with self-managed clusters.

---

### 3. Open/Self-Managed Kubernetes

**Estimate: 25-35% of $200M+ AI SaaS companies run self-managed Kubernetes for some workloads**

**Classification:** Inferred (derived through stated logic)

**Evidence Chain:**

- Based on [04_tech_blogs.md, case studies], which document OpenAI running self-managed K8s on Azure at 7,500 nodes, Databricks running a hybrid of self-managed and cloud-managed K8s across "thousands of clusters," Salesforce deploying K8s directly on bare metal, and HubSpot running self-managed K8s, I identify a clear pattern: the largest companies self-manage at least some K8s clusters for control, customization, or cost reasons.

- Based on [02_analyst_reports.md, Data Point 2], which shows "Managed Kubernetes has captured approximately 63% of Kubernetes deployments, with the remaining share being self-managed" (all environments including on-premises), I derive that 37% of K8s deployments are self-managed. At $200M+ ARR, where companies have more infrastructure resources, the self-managed percentage is likely at or above this baseline.

- Based on [01_cncf_survey.md, Data Point 20], which shows "Survey respondents were evenly split (59%) between on-premises data centers and public clouds (both 59%), with both skewing heavily toward self-managed instances," I note the CNCF population (which skews toward advanced practitioners) reports strong self-managed preference.

- Based on [07_sec_earnings.md, IBM Red Hat OpenShift data], which shows "OpenShift ARR exceeded $1.9 billion at more than 30% growth," I infer significant enterprise demand for self-managed Kubernetes platforms like OpenShift, indicating that large companies invest in K8s platforms beyond the hyperscaler managed services.

- Based on [04_tech_blogs.md, CNCF Kubernetes AI Conformance Program], which documents CNCF launching standardization for AI workloads on Kubernetes in November 2025, I note that this program exists partly because companies running self-managed K8s need interoperability guarantees for AI workloads across environments.

**Reasoning:** At $200M+ ARR, companies have the engineering team size and budget to operate self-managed K8s. The drivers for self-management at this tier include: (a) GPU cluster customization requirements that exceed managed K8s defaults, (b) multi-cloud portability (avoiding lock-in to EKS/GKE/AKS-specific features), (c) on-premises or colocation deployments for cost optimization or data sovereignty, (d) extreme scale requiring custom schedulers (as OpenAI demonstrated with 7,500-node clusters), and (e) specific compliance requirements in regulated industries. However, most companies at this tier use self-managed K8s alongside managed K8s, not instead of it.

**Confidence: 6/10** -- Named company examples (OpenAI, Databricks, Salesforce, HubSpot) provide strong directional evidence. The 27-37% self-managed range from general enterprise data is a reasonable baseline. Adjusted upward for $200M+ AI SaaS because of GPU customization needs and engineering team capabilities. However, sample is biased toward companies that publish engineering blogs.

---

## Typical Patterns

### Most Common Starting Architecture

**Finding:** Companies that reached $200M+ ARR typically did NOT start on Kubernetes.

**Classification:** Inferred

**Evidence:**

- Based on [08_vc_startup_db.md, Infrastructure Architecture Recommendations by Stage], which states "At the Seed stage... Kubernetes should be avoided early unless absolutely necessary due to its high adoption barrier" and "Monolithic architecture is recommended as a superpower," I confirm the standard VC guidance is to avoid K8s complexity at early stage.

- Based on [04_tech_blogs.md, migration case studies], which document Figma migrating from ECS to EKS, Grammarly migrating from EC2 to EKS, Salesforce Data Cloud migrating from EC2 to K8s, and HubSpot migrating from EC2 to K8s, I identify a consistent pattern: companies that are now at $200M+ ARR started on simpler architectures (EC2, ECS, PaaS) and migrated to Kubernetes as they scaled.

**Typical progression:**
1. **Seed to Series A ($0-10M ARR):** PaaS (Heroku, Render), serverless (Lambda), or simple EC2/ECS deployments
2. **Series B to C ($10M-100M ARR):** Migration to managed Kubernetes (EKS/GKE/AKS) begins, driven by CNCF ecosystem maturity, hiring of first platform engineers, need for standardized deployment
3. **$100M-200M ARR:** Kubernetes becomes primary orchestration layer; internal developer platforms (IDPs) emerge; some workloads remain on serverless for event-driven tasks
4. **$200M+ ARR:** Multi-architecture environment stabilizes with K8s as backbone; self-managed K8s may emerge for specialized workloads; FinOps and cost optimization become strategic priorities

### Migration Patterns (2024-2025)

**Finding:** All documented migrations at this tier move TOWARD Kubernetes, not away from it.

**Classification:** Direct (from engineering blog evidence)

**Evidence:**

- Based on [04_tech_blogs.md, Migration section], which explicitly states "Migration direction is TOWARD Kubernetes, not away from it" and documents four companies migrating TO K8s (Figma: ECS to EKS, Grammarly: EC2 to EKS, Salesforce Data Cloud: EC2 to K8s, HubSpot: EC2 to K8s) and ZERO companies migrating FROM K8s, the direction is unambiguous in available data.

- Based on [04_tech_blogs.md, Limitations], which acknowledges "No companies disclosed failed K8s migrations or decisions to abandon K8s" and "No engineering blogs disclosed moving FROM K8s TO serverless," I caveat that publication bias heavily favors successful migration stories.

**Confidence: 7/10 for direction, 4/10 for universality** -- The direction is well-supported, but we cannot rule out unpublished cases of companies migrating away from K8s. Publication bias is significant.

---

## Engineering Team Size and Capability

### Platform Engineering Teams at $200M+ ARR

**Estimate: 20-100+ dedicated infrastructure/platform engineers**

**Classification:** Estimated (judgment from indirect signals)

**Evidence:**

- Based on [03_job_postings.md, Data Point 8], which shows Platform Engineer roles growing from 8.35% to 11% of infrastructure job postings (32% YoY growth), I infer companies at $200M+ ARR are actively hiring platform engineers, with these roles representing a significant portion of their infrastructure headcount.

- Based on [03_job_postings.md, Data Point 20], which shows "Senior-level: 60%, Lead-level: 15%" for DevOps positions, I infer that K8s/infrastructure teams at this tier are staffed with experienced senior and lead-level engineers, not entry-level practitioners.

- Based on [04_tech_blogs.md, HubSpot case study], which documents "Scaled from ~400 MySQL clusters to 700 while keeping infrastructure team at 3-5 people" using Kubernetes and Vitess, I note that K8s automation enables small teams to manage large-scale infrastructure. However, HubSpot's total platform team is likely much larger than the 3-5 person database sub-team.

- Based on [08_vc_startup_db.md, Platform Engineering data], which shows "55% of global organizations have already adopted platform engineering" and "Over 65% of enterprises have either built or adopted an Internal Developer Platform," I confirm that platform engineering is standard practice at enterprise scale.

**Reasoning:** At $200M+ ARR with typical engineering headcounts of 200-1,000+ engineers, a platform/infrastructure team of 20-100+ is standard (approximately 10-15% of total engineering). These teams are fully capable of operating self-managed Kubernetes clusters, building internal developer platforms, and managing multi-cloud deployments.

**Can they run self-managed K8s?** Based on [03_job_postings.md, Data Point 7], which shows 91% of Kubernetes users are in companies with 1,000+ employees, the answer is definitively yes. Companies at $200M+ ARR have both the team size and talent to operate self-managed K8s. The question is not capability but strategic choice -- whether the engineering investment in self-managing K8s control planes yields sufficient benefit versus using managed services (EKS/GKE/AKS).

**Confidence: 5/10** -- No direct data on infrastructure team sizes by ARR tier. Estimated from job posting distribution data, platform engineering adoption rates, and known company case studies.

---

## Infrastructure Spend as Percentage of Revenue

### AI-First SaaS at $200M+ ARR

**Estimate: 25-50% of revenue on infrastructure (COGS), yielding 50-75% gross margins**

**Classification:** Inferred (from SEC data and analyst benchmarks)

**Evidence:**

- Based on [07_sec_earnings.md, AI SaaS Cost of Revenue], which states "an AI SaaS might see 40-50% (or more) of revenue eaten by COGS in the form of model hosting, inference compute, and data costs," I establish the upper bound for AI-first companies.

- Based on [07_sec_earnings.md, AI SaaS Gross Margin Range], which states "AI-first B2B SaaS companies achieve gross margins of 50-65%," I derive infrastructure COGS of 35-50% of revenue.

- Based on [08_vc_startup_db.md, Infrastructure Spending Benchmarks], which states "Compute costs for AI companies went from 24% of revenue to 50% of revenue" and Bessemer's finding that "fast-scaling AI SaaS startups had only ~25% gross margin on average in early stages, while even steadier-growth AI companies managed around 60% gross margin," I note that companies at $200M+ ARR (which have achieved scale) are likely at the more optimized end of this range.

- Based on [07_sec_earnings.md, Snowflake commitment], which shows a $2.5B 5-year cloud commitment (~$500M/year) for a company with ~$2.8B annual revenue, I calculate approximately 18% of revenue on cloud infrastructure for a data platform company. However, Snowflake is a data warehouse, not an AI model company -- AI inference costs are typically higher.

- Based on [07_sec_earnings.md, Palantir commitment], which shows $160.2M annual cloud commitment for a company with ~$2.9B annual revenue, I calculate approximately 5.5% of revenue. Palantir is analytics-focused, not inference-heavy.

- Based on [07_sec_earnings.md, Traditional SaaS baseline], which states "cloud hosting costs usually account for 6%-12% of SaaS revenue," I establish the non-AI baseline.

**Estimate by sub-segment within $200M+ AI SaaS:**

| Sub-Segment | Infra as % of Revenue | Gross Margin | Basis |
|---|---|---|---|
| Foundation model providers (OpenAI, Anthropic) | 30-50% | 50-70% | Direct: 07_sec_earnings.md, OpenAI/Anthropic data |
| AI-first SaaS (inference-heavy) | 25-40% | 60-75% | Inferred: 07_sec_earnings.md + 08_vc_startup_db.md |
| AI-augmented SaaS (traditional SaaS + AI features) | 12-25% | 75-85% | Inferred: traditional baseline + AI COGS premium |
| Data platform SaaS (Snowflake, Databricks) | 15-25% | 70-80% | Direct: Snowflake commitment data |

**Confidence: 6/10** -- Range is wide because the $200M+ tier includes companies with very different AI infrastructure intensity. Foundation model providers have fundamentally different cost structures than SaaS companies that add AI features. Named company commitments (Snowflake, Palantir) provide anchor points, but few companies at this tier disclose granular infrastructure costs.

---

## Decision Drivers for Architecture Choice

### Primary Drivers at $200M+ ARR

Based on synthesis across all 8 Wave 1 files, the decision drivers at this tier (in priority order):

**1. GPU Orchestration Requirements** (Strongest driver toward Kubernetes)

- Based on [04_tech_blogs.md, OpenAI case study], which documents 7,500-node K8s clusters with 200,000 IP addresses for GPU workloads, and [04_tech_blogs.md, Anthropic case study] showing GKE managing "mega-scale Kubernetes clusters using GPU/TPU/Trainium accelerators," the need to orchestrate thousands of GPUs is the primary driver for Kubernetes at this tier.
- Based on [02_analyst_reports.md, Data Point 12], which states "By 2027, Gartner predicts that more than 75% of all AI/ML deployments will use container technology," the trajectory is clear.
- **Classification:** Direct

**2. Multi-Cloud Strategy and Portability**

- Based on [01_cncf_survey.md, Data Point 9], which shows "56% of organizations use multi-cloud solutions" and "Average of 2.8 unique cloud service providers per organization," multi-cloud is standard at enterprise scale.
- Based on [02_analyst_reports.md, Data Point 29], which shows "Organizations are using 2.4 public cloud providers," and [01_cncf_survey.md, Data Point 11], which shows "Large organizations (5000+ employees): 56% adopt hybrid clouds," multi-cloud is even more prevalent at $200M+ ARR.
- Based on [04_tech_blogs.md, Anthropic case study], which documents "Multi-cloud infrastructure: AWS Project Rainier (Trainium2), Google Cloud TPUs, Microsoft Azure," and [04_tech_blogs.md, Databricks case study] showing "mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)," multi-cloud K8s is a concrete pattern at this tier.
- Kubernetes provides workload portability across clouds; serverless does not.
- **Classification:** Inferred

**3. Ecosystem and Tooling (CNCF Ecosystem)**

- Based on [04_tech_blogs.md, Figma migration], which states the move to K8s was "Primarily to take advantage of the large ecosystem supported by the CNCF," access to the K8s ecosystem (Helm, Karpenter, Argo CD, Prometheus, etc.) is a significant driver.
- Based on [04_tech_blogs.md, CNCF AI Conformance Program], CNCF is standardizing AI workload management on K8s, further cementing the ecosystem advantage.
- **Classification:** Direct

**4. Cost Optimization at Scale**

- Based on [04_tech_blogs.md, Figma migration], which states the move was driven by "cost savings, improved developer experience, and increased resiliency," cost is a material factor.
- Based on [08_vc_startup_db.md, CAST AI data], which shows "Kubernetes automation platform that cuts AWS, Azure, and GCP customers' cloud costs by over 50%," K8s enables aggressive cost optimization through bin-packing, spot instances, and autoscaling.
- Based on [07_sec_earnings.md, Cloud Cost data], which shows "89% of CFOs report that rising cloud costs have negatively impacted gross margins," cost pressure drives architecture decisions toward platforms that enable fine-grained resource management.
- Based on [02_analyst_reports.md, Data Point 40], which shows "Across all platforms, most workloads use less than half of their requested memory and less than 25% of their requested CPU," over-provisioning is a major cost problem that K8s autoscaling can address.
- **Classification:** Inferred

**5. Compliance and Data Sovereignty**

- Based on [01_cncf_survey.md, Data Point 11], which shows large organizations at 56% hybrid cloud adoption, regulatory requirements drive companies toward architectures that support both cloud and on-premises deployment.
- Based on [04_tech_blogs.md, Cohere case study], which documents "Private deployments typically run on Kubernetes" and "Deployment options: SaaS, cloud of choice, on-prem," the need to deploy in customer environments drives K8s adoption.
- Self-managed K8s enables deployment in sovereign clouds, government environments, and customer data centers.
- **Classification:** Inferred

**6. Developer Experience and Productivity**

- Based on [04_tech_blogs.md, Jasper AI case study], which documents building "JasperCLI" for "ephemeral testing environments, spin up a Kubernetes stack," and [04_tech_blogs.md, Grammarly migration] showing "significantly reduced setup time (multiple hours saved per person per sprint)," developer productivity is a significant driver.
- Based on [08_vc_startup_db.md, Platform Engineering data], which shows "71% of leading adopters of platform engineering indicated they have significantly accelerated their time to market," platform engineering (typically built on K8s) improves developer velocity.
- **Classification:** Direct

---

## Multi-Architecture Usage

### Estimate: 70-85% of $200M+ AI SaaS companies use MULTIPLE architectures simultaneously

**Classification:** Estimated (judgment + reasoning)

**Evidence:**

- Based on [02_analyst_reports.md, Data Point 17], which shows "66% of organizations using serverless functions also use container orchestration," I establish that hybrid architectures are the norm at enterprise scale.

- Based on [01_cncf_survey.md, Data Point 20], which shows organizations selecting MULTIPLE deployment types (59% on-premises, 59% public cloud, 46% managed public cloud, 40% private cloud, 39% hybrid), the data directly supports multi-architecture usage as standard.

- Based on [04_tech_blogs.md, Databricks case study], which explicitly documents a "mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)" across "thousands of Kubernetes clusters," hybrid managed/self-managed K8s is documented at this tier.

- Based on [04_tech_blogs.md, Anthropic case study], which documents multi-cloud infrastructure spanning AWS, Google Cloud, and Microsoft Azure with different accelerator types, even within Kubernetes there are multiple deployment patterns.

- Based on [07_sec_earnings.md, Zoom case study], which documents AWS primary cloud + Oracle Cloud + 29 colocation data centers, the combination of cloud managed services and self-managed infrastructure is standard at $200M+ ARR.

**Typical multi-architecture pattern at $200M+ ARR:**

| Workload Type | Typical Architecture | Reasoning |
|---|---|---|
| AI model training | Self-managed or managed K8s with GPUs | Custom scheduling, large clusters, GPU affinity |
| AI model inference (production) | Managed K8s (EKS/GKE/AKS) | Scaling, reliability, managed control plane |
| API gateway / edge | Serverless (Lambda, Cloud Run) or managed containers | Event-driven, variable traffic, low latency |
| Data pipelines | Managed K8s or managed services (EMR, Dataflow) | Batch processing, resource isolation |
| Internal tools / microservices | Managed K8s | Standardized deployment, CNCF ecosystem |
| Customer-deployed (on-prem) | Self-managed K8s | Portability, sovereignty, customer requirements |

**Confidence: 6/10** -- Strong directional evidence from multiple sources that multi-architecture is the norm. Specific percentages are estimated. The 70-85% range accounts for the possibility that some $200M+ companies have fully standardized on a single architecture (likely K8s).

---

## Assumptions Register

| # | Assumption | Impact if Wrong | Mitigation |
|---|---|---|---|
| A1 | Companies at $200M+ ARR have engineering teams of 200+ with 20+ platform engineers | If smaller teams, self-managed K8s estimate would be too high | Cross-reference with LinkedIn headcount data |
| A2 | Engineering blog publications are roughly representative of actual architecture choices at $200M+ tier | If publication bias is extreme, self-managed K8s could be over-counted (companies with notable scale publish more) | Validated by CNCF survey data showing 27-37% self-managed across all orgs |
| A3 | AI-first SaaS companies at $200M+ have higher K8s adoption than general enterprise due to GPU requirements | If AI companies use managed ML services (SageMaker, Vertex AI) instead of K8s, K8s estimate would be too high | Supported by CNCF 2024 showing 66% of GenAI orgs use K8s for inference |
| A4 | Multi-cloud adoption at $200M+ ARR is higher than the 56% general enterprise rate | If single-cloud is more common at this tier, multi-architecture estimate would be too high | Supported by named examples (Anthropic, Databricks, Snowflake all multi-cloud) |
| A5 | Serverless is primarily a complement to K8s at this tier, not a replacement | If companies use Lambda/Cloud Run as primary compute (not just ancillary), cloud-native non-K8s estimate would be too low | Supported by serverless GPU limitations and declining serverless framework adoption |
| A6 | Infrastructure cost percentages from Monetizely/Bessemer research apply to $200M+ ARR companies | If economies of scale significantly reduce infra costs at $200M+, estimates would be too high | Partially validated by Snowflake/Palantir SEC data showing lower % at extreme scale |
| A7 | CNCF survey data (biased toward K8s adopters) can be directionally applied if adjusted for known biases | If CNCF bias is larger than estimated, all K8s adoption figures would be overstated | Compared against Gartner (54% K8s) and Red Hat (70% K8s) for calibration |

---

## Evidence Gaps

### Critical Gaps (Would Significantly Change Estimates)

1. **No direct survey of AI SaaS infrastructure by ARR tier.** Every Wave 1 source noted the absence of "AI SaaS company" segmentation. All estimates are inferred from general enterprise data and named company examples. A survey of 50-100 AI SaaS CTOs/VPs Engineering at $200M+ ARR would dramatically improve confidence.

2. **No data on companies that tried and abandoned Kubernetes.** Based on [04_tech_blogs.md, Limitations], "No companies disclosed failed K8s migrations or decisions to abandon K8s." This creates survivorship bias in the migration pattern analysis. The true failure/abandonment rate for K8s at this tier is unknown.

3. **No granular infrastructure cost breakdown by architecture type.** Based on [07_sec_earnings.md, Limitations], "Specific technology choices (Kubernetes, serverless, container platforms) rarely disclosed in 10-Ks." We cannot determine whether K8s-based architectures are more or less cost-efficient than alternatives at this tier.

4. **No data on infrastructure team sizing by ARR.** Based on [08_vc_startup_db.md, Limitations], "How many infrastructure engineers at different ARR levels? Not covered." Team size estimates are judgment-based.

### Moderate Gaps (Would Refine Estimates)

5. **Limited EKS vs GKE vs AKS market share data for AI SaaS.** Based on [01_cncf_survey.md, Data Point 38], market share data exists (EKS 22%, AKS 19%, GKE 18%) but is not segmented for AI SaaS companies. Different cloud providers may dominate at different tiers.

6. **No workload-level architecture data.** Based on [06_stackshare_github.md, Limitation 5], "Surveys measure technology adoption at org level, not workload level." We cannot determine what percentage of compute cycles at a $200M+ company run on K8s vs serverless vs bare metal.

7. **Limited non-US data.** Based on [03_job_postings.md, Limitation 7], "66-70% of K8s job data is North America." Architecture patterns in EU and APAC may differ due to data sovereignty requirements and cloud provider availability.

8. **No data on K8s platform costs (operational overhead).** The total cost of operating Kubernetes (platform team salaries + tooling licenses + cloud provider K8s fees) at $200M+ ARR is undocumented. This is critical for comparing managed vs self-managed economics.

---

## Summary Estimates Table

| Architecture | Adoption % at $200M+ ARR | Classification | Confidence | Primary Evidence |
|---|---|---|---|---|
| Cloud-native non-K8s (serverless, PaaS, ECS/Fargate, Cloud Run) | 40-55% (for some workloads) | Estimated | 5/10 | Datadog serverless adoption, vendor case studies, GPU limitations |
| Managed Kubernetes (EKS/GKE/AKS) | 55-65% (primary or major) | Inferred | 7/10 | Dynatrace 73% managed, engineering blogs, CNCF surveys, vendor cases |
| Open/Self-managed Kubernetes | 25-35% (for some workloads) | Inferred | 6/10 | OpenAI/Databricks/Salesforce blogs, CNCF 27-37% self-managed |
| Multiple architectures simultaneously | 70-85% | Estimated | 6/10 | CNCF multi-deployment data, Datadog hybrid patterns |

**Note:** Percentages are non-exclusive and independent. A single company can appear in multiple categories (e.g., using both managed K8s and serverless).

---

## Key Takeaways for $200M+ ARR Tier

1. **Kubernetes is the dominant infrastructure layer.** An estimated 85-95% of $200M+ AI SaaS companies use some form of Kubernetes (managed, self-managed, or hybrid). This is supported by engineering blog evidence (every disclosed $200M+ AI company uses K8s), CNCF survey data (80% production K8s), and the structural requirement for GPU orchestration at scale.

2. **Managed K8s is the primary pattern, but self-managed is significant.** The typical company uses managed K8s (EKS/GKE/AKS) for most workloads but may self-manage specialized clusters for GPU training, on-premises deployments, or extreme customization. Databricks explicitly documents this hybrid approach.

3. **Serverless and non-K8s services are complements, not alternatives.** At $200M+ ARR, serverless (Lambda, Cloud Run, Fargate) serves specific use cases (event processing, API gateways, lightweight microservices) but is NOT the primary compute platform for AI inference workloads.

4. **Infrastructure costs are a strategic concern.** AI-first companies at this tier spend 25-50% of revenue on infrastructure -- significantly higher than the 6-12% traditional SaaS baseline. This drives investment in K8s optimization (CAST AI reports 50%+ savings), reserved instance/savings plan strategies, and potentially self-managed infrastructure for cost control.

5. **Multi-cloud and multi-architecture are standard.** Companies at this tier typically use 2-3 cloud providers and multiple architecture patterns simultaneously. Kubernetes provides the abstraction layer that makes multi-cloud viable.

6. **Teams at this tier CAN run self-managed K8s; the question is whether they SHOULD.** With 20-100+ platform engineers, capability is not the constraint. The decision is economic and strategic: does the customization benefit justify the operational investment versus managed K8s?

---

## Cross-Reference Matrix: Wave 1 Sources Used

| Source File | Key Data Points Used | Relevance to $200M+ Tier |
|---|---|---|
| 01_cncf_survey.md | K8s production at 80%, managed K8s 61-79%, multi-cloud 56%, serverless 11%, AI inference on K8s 66% | High -- baseline adoption rates, size segmentation |
| 02_analyst_reports.md | Managed K8s 73% of cloud clusters, serverless container adoption, AI workload forecasts, resource over-provisioning | High -- analyst benchmarks for managed vs self-managed |
| 03_job_postings.md | Platform Engineer growth 32% YoY, K8s company size distribution (91% at 1000+), managed K8s 73% | Medium -- proxy signal for hiring patterns |
| 04_tech_blogs.md | OpenAI 7,500 nodes, Databricks hybrid K8s, Figma/Grammarly migrations, Anthropic multi-cloud | Very High -- direct evidence from named $200M+ companies |
| 05_cloud_vendor_cases.md | EKS/GKE/AKS AI case studies, ECS/Fargate SaaS case studies, infrastructure non-disclosure pattern | Medium -- vendor bias but validates architecture patterns exist |
| 06_stackshare_github.md | K8s 96% enterprise adoption, managed K8s 67% cloud-hosted, serverless adoption conflicts | Medium -- confirms enterprise K8s dominance |
| 07_sec_earnings.md | Snowflake $2.5B commitment, Palantir $1.95B commitment, AI SaaS 40-50% COGS, gross margins 50-65% | Very High -- financial data anchors for cost analysis |
| 08_vc_startup_db.md | AI infra investment $225.8B, infra costs 24-50% of revenue, platform engineering 55%, stage-based architecture guidance | High -- economic benchmarks and stage progression |

---

## Overall Confidence Assessment: 6/10

**Justification:**

The 6/10 reflects:

- **Strong directional confidence (8/10):** Kubernetes dominance at $200M+ ARR is well-supported by multiple independent sources. Every named AI company at this tier uses K8s. Migration direction is unambiguously toward K8s.

- **Moderate precision confidence (5/10):** Specific percentage ranges (55-65% managed, 25-35% self-managed, 40-55% serverless) are educated estimates, not direct measurements. No source segments AI SaaS companies by ARR tier.

- **Low cost/economics confidence (4/10):** Infrastructure spend ranges (25-50% of revenue) are wide and depend heavily on whether a company is inference-heavy vs AI-augmented. Few companies disclose granular infrastructure costs.

- **Very low failure/negative data confidence (2/10):** We have zero data on K8s failures, abandonments, or companies that chose non-K8s architectures and succeeded at $200M+ ARR in AI SaaS. This is a significant blind spot.

To improve confidence to 8/10+ would require: (a) a purpose-built survey of 50+ AI SaaS CTOs at $200M+ ARR, (b) anonymized cloud provider data on AI SaaS customer architecture choices, or (c) access to VC portfolio infrastructure audits.

---

**Analysis Compiled:** 2026-02-12
**Sources:** 8 Wave 1 research files (01-08) covering CNCF surveys, analyst reports, job postings, engineering blogs, cloud vendor case studies, StackShare/GitHub, SEC filings, and VC/startup databases
**Analyst:** Wave 2 Analysis Agent
