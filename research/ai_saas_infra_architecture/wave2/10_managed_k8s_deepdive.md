# Wave 2 Analysis: Managed Kubernetes Deep Dive for AI SaaS Companies

**Analysis Date:** 2026-02-12
**Analyst Focus:** Managed Kubernetes (AKS, EKS, GKE) adoption among AI SaaS companies
**Inputs:** Wave 1 files 01-08
**Classification System:** Direct | Inferred | Estimated

---

## Executive Summary

Managed Kubernetes (EKS, AKS, GKE) has become the dominant infrastructure pattern for AI SaaS companies at scale. Based on triangulation across 8 Wave 1 data sources, an estimated 60-70% of AI SaaS companies with >$10M ARR use managed Kubernetes for production workloads. Among all K8s deployments in cloud environments, 73% run on managed services (Dynatrace 2023), and among organizations hosting generative AI models, 66% use Kubernetes for inference workloads (CNCF 2024). EKS leads vendor market share at ~37% of managed K8s usage among AI SaaS, followed by GKE at ~33% and AKS at ~25%, though these estimates carry significant uncertainty. Adoption scales sharply with company size: 91% of K8s users are at organizations with 1,000+ employees. Migration patterns in 2024-2025 flow exclusively toward managed K8s (Figma: ECS to EKS, Grammarly: EC2 to EKS), with no documented counter-migrations.

---

## 1. What Percentage of AI SaaS Companies Use Managed K8s?

### Overall Estimate: 60-70% of AI SaaS companies with >$10M ARR

**Classification: Estimated (judgment + reasoning from multiple data points)**

#### Evidence Chain

**Step 1: Kubernetes adoption among all organizations**
- Based on [01_cncf_survey.md, Data Point 1], which shows "Production use of Kubernetes hit 80% in 2024, up from 66% in 2023" among CNCF survey respondents (n=750). **Classification: Direct.**
- Based on [02_analyst_reports.md, Data Point 6], which shows "Kubernetes has joined the mainstream, with 54% of survey respondents having a full or partial implementation" (Gartner). **Classification: Direct.**
- **Reconciliation:** CNCF respondents skew cloud-native (acknowledged in [01_cncf_survey.md, Known Biases]). Gartner captures broader enterprise base. AI SaaS companies are more cloud-native than average enterprise but less than CNCF core community. **Estimate for AI SaaS K8s usage overall: 65-80%.** Classification: Inferred.

**Step 2: Of K8s users, what fraction use managed services?**
- Based on [02_analyst_reports.md, Data Point 1], which shows "73% [of cloud Kubernetes clusters] are built on top of managed distributions from the hyperscalers" (Dynatrace 2023). **Classification: Direct.**
- Based on [01_cncf_survey.md, Data Point 19], which shows "90% of Kubernetes users have turned to cloud-managed services" (Datadog 2021). **Classification: Direct.**
- Based on [06_stackshare_github.md, Managed K8s section], which shows "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022." **Classification: Direct.**
- **Reconciliation:** Cloud-hosted clusters shifted from 45% (2022) to 67-73% (2023-2025). AI SaaS companies are overwhelmingly cloud-based (few on-prem), so managed K8s fraction among AI SaaS K8s users is likely at the upper end: ~80-90%. **Classification: Inferred.**

**Step 3: AI-specific K8s adoption**
- Based on [01_cncf_survey.md, Data Point 21], which shows "66% of organizations hosting generative AI models use Kubernetes to manage some or all of their inference workloads." **Classification: Direct.**
- Based on [01_cncf_survey.md, Data Point 22], which shows "44% of organizations report they do not yet run AI/ML workloads on Kubernetes." **Classification: Direct.**
- Based on [02_analyst_reports.md, Data Point 12], which shows Gartner predicts "more than 75% of all AI/ML deployments will use container technology as the underlying compute environment" by 2027, "a major increase from fewer than 50% in 2024." **Classification: Direct (forecast).**
- Based on [07_sec_earnings.md, Kubernetes Adoption], which shows "Nearly all (98%) of organizations run data-intensive workloads on cloud-native platforms, with AI/ML workloads (54%) being built on Kubernetes" (CNCF Voice of K8s Experts 2024). **Classification: Direct.**

**Step 4: Synthesis**
- AI SaaS companies are a subset of "organizations hosting generative AI models" that are also SaaS businesses. They are more infrastructure-mature than the average organization.
- 66% of AI model hosts use K8s for inference; AI SaaS companies likely exceed this given their cloud-native orientation.
- Of those using K8s, 73-90% use managed services.
- Combined estimate: (70-80% K8s adoption) x (80-90% managed) = **56-72% of AI SaaS companies use managed K8s.**
- **Central estimate: 60-70%.** Classification: Estimated.

#### Corroboration from Case Studies
- Based on [04_tech_blogs.md], which documents 12+ companies using managed K8s: Anthropic (GKE), Cohere (OKE), Snowflake (EKS), Notion (EKS), Grammarly (EKS), Figma (EKS), Contextual AI (GKE), Picterra (GKE), Eli Lilly (EKS), Flawless (EKS), Liquid Analytics (EKS), Stacks (GKE Autopilot). **Classification: Direct (individual cases).**
- Based on [05_cloud_vendor_cases.md], which found 9 of 25 documented case studies used managed K8s; however, 44% of case studies omitted infrastructure details entirely. **Classification: Direct (from disclosed subset).**

---

## 2. Vendor Market Share: EKS vs AKS vs GKE Among AI SaaS

### Estimate: EKS ~37%, GKE ~33%, AKS ~25%, Other (OKE, etc.) ~5%

**Classification: Estimated (triangulation from multiple imperfect data points)**

#### Data Points by Source

**CNCF 2021 Survey (general, not AI-specific):**
- Based on [01_cncf_survey.md, Data Point 18], which shows "Amazon Elastic Container Service for Kubernetes (39%), Azure Kubernetes Service (23%), and Azure (AKS) Engine (17%)" among certified hosted platform users. **Classification: Direct (for 2021 general population).**

**Market Share Data 2024 (general):**
- Based on [01_cncf_survey.md, Data Point 38], which shows "Amazon AWS EKS holds the highest share at 22%, Google GCP GKE holds 18% share, Microsoft Azure contributes 19%." **Classification: Direct (market share, not adoption rate).**

**Cluster Count Data:**
- Based on [01_cncf_survey.md, Data Point 39], which shows "GKE operates over 500,000 clusters, EKS manages more than 400,000 clusters, and AKS oversees in excess of 130,000 clusters." **Classification: Direct (cluster counts).**
- GKE leads on cluster count despite EKS leading market share by revenue, suggesting GKE clusters are smaller on average (more startups/smaller workloads) while EKS clusters are larger (enterprise).

**Adoption Rate Among Businesses (Industry Survey):**
- Based on [06_stackshare_github.md, Managed K8s section], which shows "GKE remains dominant in the Kubernetes landscape, with a 32% adoption rate among businesses" and "AKS maintains a 28% adoption rate among businesses with 5,000 or more employees." **Classification: Direct (but source methodology unclear, caveat noted in original).**

**Case Study Evidence (AI-specific):**
- Based on [04_tech_blogs.md] and [05_cloud_vendor_cases.md], AI SaaS companies on managed K8s:
  - **EKS:** Figma, Grammarly, Snowflake, Notion, Eli Lilly, Flawless, Liquid Analytics, Instabase, Sonantic (9 companies)
  - **GKE:** Anthropic, Contextual AI, Picterra, Stacks, Routematic, invos Group (6 companies)
  - **AKS:** Duck Creek, PTC (2 companies, plus OpenAI on Azure K8s but partially self-managed)
  - **OKE:** Cohere (1 company)
  - **Classification: Direct (individual cases, not representative sample).**

#### Synthesis and AI SaaS-Specific Adjustment

The general market data shows EKS leading at 22-39% depending on metric (revenue share vs adoption rate). However, AI SaaS companies show specific patterns:

1. **EKS strength in AI SaaS:** AWS has the deepest ecosystem for SageMaker, Trainium, and inference infrastructure. Case studies show 9 AI SaaS companies on EKS vs 6 on GKE. Based on [05_cloud_vendor_cases.md], AWS EKS supports up to 100,000 nodes and 1.6M Trainium chips per cluster. **Estimated AI SaaS share: ~37%.**

2. **GKE strength with AI-native companies:** Anthropic (one of the largest AI companies) runs on GKE. Google's TPU ecosystem and GKE's demonstrated 130,000-node clusters (based on [04_tech_blogs.md, Google Cloud section]) attract AI-first companies. GKE cluster count exceeds EKS (500K vs 400K per [01_cncf_survey.md, Data Point 39]), suggesting broader adoption among smaller/startup AI companies. GKE Autopilot reduces operational overhead. **Estimated AI SaaS share: ~33%.**

3. **AKS strength in enterprise/regulated AI:** Based on [06_stackshare_github.md], "AKS maintains a 28% adoption rate among businesses with 5,000 or more employees." Azure's sovereign cloud and compliance certifications may boost AKS in EU. OpenAI's $250B Azure commitment (per [05_cloud_vendor_cases.md]) anchors the relationship. AKS certified for Kubernetes AI Conformance (per [05_cloud_vendor_cases.md]). However, fewer AI SaaS startups appear on AKS in case studies. **Estimated AI SaaS share: ~25%.**

4. **Other (OKE, etc.):** Cohere on OKE (per [04_tech_blogs.md]) demonstrates niche alternatives. **Estimated share: ~5%.**

#### Confidence Assessment

**Confidence: 4/10.** These market share estimates are the weakest part of this analysis. No source directly segments managed K8s vendor share among AI SaaS companies. The case study data is biased by vendor publication practices. The general market share data conflates revenue share, adoption rate, and cluster count -- three different metrics that yield different rankings.

---

## 3. Breakdown by Company Size (Revenue Tier)

### Summary Table

| Revenue Tier | Managed K8s Adoption Rate | Primary Vendor | Evidence Quality |
|---|---|---|---|
| <$1M ARR (Pre-seed/Seed) | 10-20% | N/A (serverless/PaaS dominant) | Estimated |
| $1M-$10M ARR (Series A/B) | 25-40% | EKS, GKE | Estimated |
| $10M-$50M ARR (Growth) | 55-70% | EKS, GKE | Inferred |
| $50M-$200M ARR (Scale) | 70-85% | EKS, GKE, AKS | Inferred |
| $200M+ ARR (Enterprise) | 85-95% | EKS, AKS, GKE | Inferred |

**Classification: Estimated (synthesized from employee-count data mapped to revenue tiers)**

#### Evidence

**Enterprise tier ($200M+ ARR / 1,000+ employees):**
- Based on [01_cncf_survey.md, Data Point 27], which shows "34% of Kubernetes users are in companies with over 20,000 employees, another 34% come from companies with 1,000-5,000 employees" and [Data Point 28] "Organizations with over 1,000 employees represent 91% of Kubernetes users." **Classification: Direct (for K8s users by employee count).**
- Based on [06_stackshare_github.md, K8s Company Size], which shows "91% of Kubernetes users work at organizations exceeding 1,000 employees." **Classification: Direct.**
- All documented AI SaaS case studies in [04_tech_blogs.md] at this tier use K8s: OpenAI (7,500 nodes), Databricks (thousands of clusters), Salesforce, Snowflake.
- **Estimate: 85-95% managed K8s adoption.** Classification: Inferred.

**Growth tier ($10M-$50M ARR):**
- Based on [08_vc_startup_db.md, Infrastructure Recommendations], which shows "Microservices architecture with Kubernetes orchestration is best suited for funded SaaS startups targeting large-scale deployments." **Classification: Direct (recommendation, not measurement).**
- Based on [03_job_postings.md, Data Point 7], which shows only "9% of adopters are companies with 500-1,000 employees" for K8s. Companies at $10M-$50M ARR typically have 50-300 employees, smaller than this threshold. **Classification: Direct (for employee count proxy).**
- **Estimate: 55-70%.** Classification: Estimated. Rationale: This is the transition zone. Companies with product-market fit and scaling needs migrate to K8s. Not all have done so.

**Seed/Pre-seed tier (<$1M ARR):**
- Based on [08_vc_startup_db.md, Architecture Recommendations], which shows "Kubernetes should be avoided early unless absolutely necessary due to its high adoption barrier" and "seed-stage startup, a monolithic architecture is recommended." **Classification: Direct (prescriptive guidance).**
- Based on [03_job_postings.md, Data Point 20], which shows "60% senior-level" for K8s roles, suggesting K8s requires experienced talent most early startups cannot afford. **Classification: Inferred.**
- **Estimate: 10-20%.** Classification: Estimated. Some AI-native founders with K8s experience may start there, but most use PaaS/serverless.

---

## 4. US vs EU Differences

### Estimate: AKS ~30% share in EU vs ~20% in US; GKE ~25% EU vs ~35% US

**Classification: Estimated (limited direct data)**

#### Evidence

**Regional Cloud-Native Adoption:**
- Based on [01_cncf_survey.md, Data Point 15], which shows "Europe: 82% in 'some' or 'much/all' cloud native development; Americas: 70%." **Classification: Direct.** Europe actually leads the Americas in cloud-native development intensity, contrary to common assumptions.

**Azure/AKS Strength in EU:**
- Based on [06_stackshare_github.md], "AKS maintains a 28% adoption rate among businesses with 5,000 or more employees." Large European enterprises (banking, manufacturing, healthcare) disproportionately favor Microsoft due to existing enterprise agreements and compliance requirements.
- Based on [05_cloud_vendor_cases.md, Case Study 20], Medigold Health (UK) uses Azure OpenAI services.
- Based on [05_cloud_vendor_cases.md, Case Study 22], Stacks (Amsterdam, Netherlands) uses GKE Autopilot -- demonstrating that GKE also has EU presence.
- Azure sovereign cloud offerings (Azure Sovereign Clouds) provide EU data residency guarantees that are particularly relevant for GDPR-sensitive AI SaaS workloads.
- **AKS likely holds ~30% share among EU AI SaaS companies vs ~20% in US.** Classification: Estimated.

**GKE Strength in US AI Startups:**
- Based on [04_tech_blogs.md], Anthropic (US) uses GKE, Contextual AI (US) uses GKE, Midjourney chose Google Cloud.
- Based on [01_cncf_survey.md, Data Point 39], GKE has more clusters (500K) than EKS (400K), with many attributed to US startup ecosystem.
- **GKE likely holds ~35% among US AI SaaS vs ~25% in EU.** Classification: Estimated.

**EKS Position:**
- AWS has the largest overall cloud market share globally (38% IaaS per [07_sec_earnings.md]). EKS likely holds consistent ~35-40% share across both regions.
- **EKS estimated at ~37% US, ~35% EU.** Classification: Estimated.

#### Evidence Gap
- Based on [01_cncf_survey.md, Limitations section], "AI/ML workload adoption by region" and "Managed Kubernetes usage by region" are explicitly noted as missing. No Wave 1 source provides direct managed K8s vendor share by region for AI SaaS companies. **This is the largest evidence gap in this analysis.**

---

## 5. Migration Triggers to Managed K8s

### Key Triggers Identified (with evidence)

#### Trigger 1: Scale Threshold -- Outgrowing ECS/Fargate/PaaS

- Based on [04_tech_blogs.md, Figma Migration], Figma migrated from ECS to EKS in 12 months because of "pursuing cost savings, improved developer experience, and increased resiliency" and "to take advantage of the large ecosystem supported by the CNCF." ECS limitations included "lack of support for StatefulSets, Helm charts, and inability to easily run OSS software like Temporal." **Classification: Direct.**
- Based on [04_tech_blogs.md, Grammarly Migration], Grammarly moved from EC2 to EKS "which allowed them to decouple storage from compute resources and move from personalized to dynamically allocated resources." **Classification: Direct.**
- Based on [04_tech_blogs.md, HubSpot Migration], HubSpot migrated 400+ MySQL databases to K8s, scaling "from ~400 MySQL clusters to 700 while keeping infrastructure team at 3-5 people." **Classification: Direct.**

**Inferred Scale Threshold:** Companies typically hit this at 50-200 microservices, 100+ engineers, or $10M+ ARR when PaaS/ECS limitations become binding constraints. **Classification: Estimated.**

#### Trigger 2: GPU/ML Workload Requirements

- Based on [04_tech_blogs.md, Cohere], Cohere chose OKE (managed K8s) specifically for "access to the GPUs they needed." **Classification: Direct.**
- Based on [04_tech_blogs.md, CNCF AI Conformance], CNCF launched the "Certified Kubernetes AI Conformance program to standardise artificial intelligence workloads by establishing a technical baseline for GPU management, networking, and gang scheduling." **Classification: Direct.**
- Based on [02_analyst_reports.md, Data Point 12], Gartner forecasts "more than 75% of all AI/ML deployments will use container technology" by 2027. **Classification: Direct (forecast).**
- Based on [08_vc_startup_db.md, KubeCon], "at least 40 sessions dedicated to AI at KubeCon China 2024, primarily focusing on how to better run large AI models on Kubernetes." **Classification: Direct.**

**Inferred trigger point:** When AI SaaS companies move from calling external model APIs (e.g., Bedrock, Vertex AI) to self-hosting models for cost, latency, or customization reasons, K8s becomes near-mandatory for GPU orchestration. **Classification: Inferred.**

#### Trigger 3: Multi-Service Complexity and CNCF Ecosystem Access

- Based on [04_tech_blogs.md, Figma], "Primarily to take advantage of the large ecosystem supported by the CNCF" -- Figma cited ecosystem access as a primary migration driver. **Classification: Direct.**
- Based on [04_tech_blogs.md, Elastic], Elastic selected Crossplane (K8s-native) for multi-cloud infrastructure management. **Classification: Direct.**
- Based on [06_stackshare_github.md, GitOps], "77% of organizations adopting GitOps principles for deployment" -- GitOps tooling (ArgoCD, Flux) is K8s-native. **Classification: Direct.**

#### Trigger 4: Cost Optimization at Scale

- Based on [05_cloud_vendor_cases.md, Liquid Analytics], EKS deployment achieved "63% savings on compute costs" and "90% reduced CPU waste." **Classification: Direct.**
- Based on [04_tech_blogs.md, Notion], EKS-based data pipeline yielded "over $1 million in savings for 2022." **Classification: Direct.**
- Based on [08_vc_startup_db.md, CAST AI], K8s optimization platform "cuts AWS, Azure, and GCP customers' cloud costs by over 50%." **Classification: Direct (vendor claim).**
- Based on [07_sec_earnings.md, AI SaaS COGS], "an AI SaaS might see 40-50% of revenue eaten by COGS" -- this cost pressure drives companies to optimize via K8s autoscaling (HPA, Karpenter). **Classification: Direct.**

#### Trigger 5: Team Size -- Platform Engineering Maturity

- Based on [03_job_postings.md, Data Point 8], Platform Engineer role growth from 8.35% to 11% of infrastructure roles (+32% YoY). **Classification: Direct.**
- Based on [08_vc_startup_db.md, Platform Engineering], "55% of global organizations surveyed have already adopted platform engineering." **Classification: Direct.**
- Based on [03_job_postings.md, Data Point 20], K8s roles require 60% senior-level hires. **Classification: Direct.**

**Inferred trigger:** Companies adopt managed K8s when they can afford at least 2-3 dedicated platform/infrastructure engineers (typically at $5M+ ARR or 30+ engineering headcount). Below this, the operational overhead is prohibitive. **Classification: Estimated.**

---

## 6. Multi-Cloud K8s Patterns

### Estimate: 20-30% of AI SaaS companies at $50M+ ARR use 2+ managed K8s providers simultaneously

**Classification: Estimated**

#### Evidence

**General Multi-Cloud Adoption:**
- Based on [01_cncf_survey.md, Data Point 9], which shows "56% of organizations use multi-cloud solutions" and "Average of 2.8 unique cloud service providers per organization." **Classification: Direct (general population).**
- Based on [02_analyst_reports.md, Data Point 29], Flexera shows "On average, organizations are using 2.4 public cloud providers." **Classification: Direct.**
- Based on [02_analyst_reports.md, Data Point 30], "65% of organizations run Kubernetes in multiple environments for portability." **Classification: Direct (general K8s users).**

**AI SaaS Multi-Cloud K8s Examples:**
- Based on [04_tech_blogs.md, Databricks], Databricks "Operates mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)" -- all three major providers simultaneously. **Classification: Direct.**
- Based on [04_tech_blogs.md, Anthropic], Anthropic uses "Multi-cloud infrastructure: AWS Project Rainier (Trainium2), Google Cloud TPUs, Microsoft Azure." **Classification: Direct.**
- Based on [04_tech_blogs.md, Hugging Face], "Hugging Face models can be deployed on Google Kubernetes Engine, Azure Kubernetes Service, and Oracle Container Engine for Kubernetes." **Classification: Direct.**
- Based on [04_tech_blogs.md, Elastic], Elastic runs "Multi-cloud deployment: AWS (4 regions), GCP (3 regions), Azure (1 region)." **Classification: Direct.**
- Based on [08_vc_startup_db.md, CAST AI], "An increasing number of CAST AI customers are using multiple cloud providers (e.g. EKS and AKS)." **Classification: Direct.**

**Patterns Observed:**

| Pattern | Example | Rationale |
|---|---|---|
| Primary + GPU alternative | Anthropic (GKE primary + AWS Trainium + Azure) | Access diverse accelerator ecosystems |
| Full multi-cloud parity | Databricks (EKS + AKS + GKE) | Serve customers on their preferred cloud |
| Deploy-anywhere platform | Hugging Face, Elastic | Product requirement: customers choose cloud |
| Primary + failover | Most companies at scale | Business continuity |

**Why AI SaaS drives multi-cloud K8s more than general SaaS:**
1. GPU scarcity forces sourcing from multiple providers (per [08_vc_startup_db.md], Azure was "the only place where [YC startups] could find GPUs").
2. AI SaaS customers in regulated industries demand deployment on their preferred cloud.
3. Different clouds offer different accelerators (NVIDIA GPUs on AWS/Azure/GCP, TPUs on GCP only, Trainium on AWS only).

---

## Assumptions Register

| # | Assumption | Impact if Wrong | Confidence |
|---|---|---|---|
| A1 | CNCF survey respondents (n=750) are representative of cloud-native tech companies, including AI SaaS. | Adoption rates could be 10-20 percentage points lower if CNCF over-represents K8s adopters. | Medium |
| A2 | AI SaaS companies are more cloud-native than the average CNCF respondent, given their infrastructure-heavy, cloud-first business models. | If wrong, AI SaaS K8s adoption could be lower than 60-70%. But CNCF notes 91% of K8s users are 1,000+ employee companies, while many AI SaaS are smaller. | Medium |
| A3 | Revenue tiers can be mapped from employee count data using typical AI SaaS company ratios (~$200K-$500K revenue per employee). | Size-tier analysis could miscategorize companies. AI companies may have different revenue-per-employee ratios than traditional SaaS. | Medium |
| A4 | Case study companies in [04_tech_blogs.md] and [05_cloud_vendor_cases.md] represent a biased-but-directionally-correct sample of AI SaaS infrastructure choices. | If publication bias is extreme, the true managed K8s adoption rate could be 10-15 percentage points lower than estimated. | Medium-High |
| A5 | Absence of documented migrations AWAY from K8s in engineering blogs reflects actual low K8s abandonment, not just publication bias. | If companies that abandoned K8s simply do not publish about it, the net migration toward K8s may be overstated. | Medium |
| A6 | The 73% managed K8s figure from Dynatrace (2023) applies roughly to AI SaaS companies in 2025-2026, adjusted upward given cloud-first orientation. | If managed K8s share has changed significantly (up or down), vendor share estimates shift accordingly. | Medium-High |
| A7 | AKS outperformance in EU relative to US is driven by Microsoft enterprise relationships and sovereign cloud, based on general Azure market patterns. | No direct data supports AI SaaS AKS share in EU. This is extrapolated from general enterprise Azure adoption. | Low |
| A8 | Multi-cloud K8s adoption among AI SaaS is higher than the general 56% multi-cloud figure because of GPU scarcity and customer deployment requirements. | If AI SaaS is not meaningfully more multi-cloud than average, the 20-30% estimate could be inflated. | Medium |

---

## Evidence Gaps

| # | Gap | Severity | Impact on Analysis |
|---|---|---|---|
| G1 | No Wave 1 source directly segments managed K8s vendor share among AI SaaS companies. | Critical | Vendor share estimates (EKS 37%, GKE 33%, AKS 25%) are low-confidence triangulations. |
| G2 | No data on AI SaaS companies <500 employees in CNCF surveys. | High | Size-tier analysis for seed/Series A companies is largely speculative. |
| G3 | Regional breakdown (US vs EU) of managed K8s usage is not available for AI SaaS or even general K8s users. | High | US/EU vendor share differences are inferred from general Azure/GCP market positioning, not measured. |
| G4 | No data on companies that tried managed K8s and reverted to other platforms. | Medium | Survivorship bias may overstate managed K8s success. |
| G5 | EKS vs AKS vs GKE revenue breakdown for AI/ML customer segment not available from any cloud vendor. | High | Vendor share analysis lacks a primary data source. |
| G6 | Multi-cloud K8s adoption rate not directly measured for AI SaaS specifically. | Medium | Multi-cloud estimate extrapolated from general multi-cloud data + AI SaaS case studies. |
| G7 | Migration trigger thresholds (ARR, team size, microservice count) are estimated from case studies, not measured across a representative sample. | Medium | Triggers are plausible but thresholds may vary significantly by company context. |
| G8 | Self-managed K8s usage among AI SaaS not cleanly separable from managed K8s in most data sources. | Medium | The 60-70% managed K8s estimate may include some companies running both managed and self-managed simultaneously. |

---

## Confidence Scores by Section

| Section | Confidence | Justification |
|---|---|---|
| Overall managed K8s adoption (60-70%) | 5/10 | Multiple converging data points but no direct measurement of AI SaaS segment. CNCF bias acknowledged. |
| Vendor market share (EKS/GKE/AKS) | 4/10 | No direct AI SaaS data. Triangulated from general market share + biased case studies. |
| Size tier breakdown | 5/10 | Strong data at enterprise tier (91% of K8s users >1,000 employees). Weak data below $10M ARR. |
| US vs EU differences | 3/10 | Almost entirely estimated. Regional K8s vendor share data does not exist in Wave 1. |
| Migration triggers | 7/10 | Multiple direct case studies with specific quotes and metrics. Triggers are well-documented even if thresholds are estimated. |
| Multi-cloud patterns | 6/10 | Strong individual case studies (Databricks, Anthropic, Elastic). General multi-cloud data supports the pattern. |

**Overall Analysis Confidence: 5/10**

This analysis provides a reasonable directional estimate of managed K8s adoption among AI SaaS companies but cannot achieve high precision. The core finding -- that managed K8s is the dominant infrastructure pattern for AI SaaS at scale -- is well-supported (confidence 7-8/10). The specific percentages and vendor shares carry much more uncertainty (confidence 3-5/10).

---

## Key Findings Summary

1. **Managed K8s is the dominant pattern for AI SaaS at scale.** An estimated 60-70% of AI SaaS companies with >$10M ARR use managed K8s in production. This is supported by CNCF data (80% K8s production usage), Dynatrace data (73% managed among cloud K8s), AI inference data (66% of AI model hosts on K8s), and 15+ company case studies.

2. **EKS leads, GKE is close, AKS trails among AI SaaS.** EKS benefits from AWS market dominance (~37%). GKE is disproportionately strong among AI-native companies due to TPU ecosystem and startup adoption (~33%). AKS is stronger in large enterprise and EU markets (~25%). These shares are low-confidence estimates.

3. **Adoption scales sharply with company size.** 91% of K8s users are at 1,000+ employee organizations. Below $10M ARR, PaaS and serverless dominate. The transition to managed K8s typically occurs at $5M-$20M ARR when companies can support 2-3 platform engineers.

4. **Migration flows toward managed K8s, not away from it.** In 2024-2025, documented migrations include Figma (ECS to EKS), Grammarly (EC2 to EKS), Salesforce Data Cloud (EC2 to K8s), and HubSpot (EC2 to K8s). Zero counter-migrations documented. Based on [04_tech_blogs.md]: "Migration direction is TOWARD Kubernetes, not away from it."

5. **GPU/AI workloads are accelerating managed K8s adoption.** The CNCF Certified Kubernetes AI Conformance program, 66% of AI model hosts using K8s for inference, and rapid growth in AI workloads on cloud-native platforms (500% YoY per Sysdig) all point to K8s becoming the standard for AI infrastructure.

6. **Multi-cloud K8s is a distinct pattern among large AI SaaS.** Databricks, Anthropic, Elastic, and Hugging Face all run K8s across multiple clouds. This is driven by GPU scarcity, customer deployment requirements, and accelerator diversity (TPU vs Trainium vs NVIDIA).

---

## Recommendations for Wave 3

1. **Primary research needed:** Survey 50-100 AI SaaS infrastructure leaders to get direct managed K8s adoption data segmented by revenue tier, geography, and vendor.

2. **Regional analysis:** Investigate EU sovereign cloud requirements and their impact on AKS vs EKS vs GKE selection among EU AI SaaS companies.

3. **Migration threshold analysis:** Detailed case studies of 10-15 companies that migrated from serverless/PaaS to managed K8s, documenting the specific ARR, team size, and technical triggers.

4. **Cost comparison:** Analyze managed K8s TCO vs serverless/PaaS for AI inference workloads at different scale points.

5. **Self-managed K8s deep dive:** Separate analysis needed for the ~15-25% of AI SaaS K8s users running self-managed clusters (OpenAI, Salesforce, etc.) -- what drives this choice over managed?

---

## Sources Cross-Reference

All claims trace to specific Wave 1 data points:

| Wave 1 File | Key Data Points Used |
|---|---|
| 01_cncf_survey.md | DP 1, 9, 15, 17, 18, 19, 20, 21, 22, 27, 28, 31, 38, 39 |
| 02_analyst_reports.md | DP 1, 6, 11, 12, 13, 17, 29, 30, 46 |
| 03_job_postings.md | DP 4, 7, 8, 11, 20 |
| 04_tech_blogs.md | OpenAI, Databricks, Figma, Google Cloud, AKS, Grammarly, Anthropic, Cohere, HubSpot, Snowflake, Notion, Elastic, CNCF AI Conformance, Contextual AI, Jasper, Hugging Face sections |
| 05_cloud_vendor_cases.md | Case Studies 1-4 (EKS), 16-17 (AKS), 21-22 (GKE), infrastructure signals |
| 06_stackshare_github.md | K8s adoption enterprise, company size, managed K8s services, serverless, AI/ML signals |
| 07_sec_earnings.md | Snowflake commitment, AI SaaS COGS, K8s adoption stats, AWS revenue/market share |
| 08_vc_startup_db.md | Infrastructure cost benchmarks, K8s platform funding (CAST AI, Spectro Cloud), architecture by stage, multi-cloud patterns, YC data |

---

**Report Compiled:** 2026-02-12
**Analyst:** Wave 2 Synthesis Agent (Managed Kubernetes Focus)
**Methodology:** Cross-source triangulation of 8 Wave 1 fact-gathering outputs
**Total Wave 1 Data Points Referenced:** 60+
