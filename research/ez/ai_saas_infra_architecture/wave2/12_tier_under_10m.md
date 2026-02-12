# Infrastructure Architecture Analysis: AI SaaS Companies Under $10M ARR

**Analysis Date:** 2026-02-12
**Tier:** Under $10M ARR
**Tier Context:** Early-stage, small engineering teams (5-30 people), cost-sensitive, speed-to-market prioritized. Typically seed through Series A/early Series B. Pre-PMF or early post-PMF.

---

## Executive Summary

AI SaaS companies under $10M ARR overwhelmingly start on cloud-native non-Kubernetes managed services (serverless, PaaS, managed containers). Based on triangulation across 8 Wave 1 sources, the estimated architecture distribution for this tier is: **55-70% cloud-native (non-K8s managed)**, **20-35% managed Kubernetes**, and **2-5% open/self-managed Kubernetes**. These percentages are non-exclusive; approximately 15-25% of companies in this tier use multiple architectures simultaneously.

The data reveals a critical evidence gap: no Wave 1 source directly segments AI SaaS companies by revenue tier. All estimates below are inferred or estimated by combining general adoption data with company-size proxies, stage-specific guidance, and VC portfolio signals. Confidence in the overall direction is moderate; confidence in precise percentages is low.

---

## Architecture Distribution Estimates

### 1. Cloud-Native (Non-K8s Managed): 55-70%

**Classification:** Estimated

**Definition:** Serverless (Lambda, Cloud Functions), PaaS (Heroku, Vercel, Render, Railway, Fly.io), managed containers without Kubernetes (ECS/Fargate, Cloud Run, Azure Container Apps).

**Reasoning and Evidence Chain:**

1. **Startup stage guidance is unanimous.** Based on [08_vc_startup_db.md, Data Point: Maven Solutions startup infrastructure guide], which states: "At the Seed stage... Simple, standard options are recommended, including fully managed platforms like Heroku, Vercel, or Firebase for speed, and choosing serverless options like AWS Lambda to reduce overhead. Kubernetes should be avoided early unless absolutely necessary due to its high adoption barrier." This directly recommends against K8s for the under-$10M tier.

2. **CNCF data shows small companies avoid Kubernetes.** Based on [01_cncf_survey.md, Data Point 27], which shows: "only 9% of adopters are companies with 500-1,000 employees" and companies under 500 employees are not even measured. Based on [01_cncf_survey.md, Data Point 28], "Organizations with over 1,000 employees represent 91% of Kubernetes users." Companies under $10M ARR typically have 5-30 engineers (well under 500 total employees), placing them firmly outside the dominant K8s user base.

3. **Serverless adoption is high among cloud users.** Based on [02_analyst_reports.md, Data Points 14-16], Datadog reports AWS Lambda at 65% of AWS customers, Google Cloud Run at 70% of GCP customers, and Azure App Service at 56% of Azure customers. While these are cross-segment figures, they demonstrate that serverless/PaaS is the default starting point for cloud customers, which skews even higher for small companies that lack dedicated infrastructure teams.

4. **Cloud-native non-K8s services appear in vendor case studies for smaller companies.** Based on [05_cloud_vendor_cases.md, Case Studies 10-14], ECS/Fargate powers companies like Autodesk, BILL, and Smartsheet. Based on [05_cloud_vendor_cases.md, Case Study 18], Azure Container Apps powers Coca-Cola's AI campaign and Replit. These demonstrate that non-K8s managed services handle production AI workloads at scale without Kubernetes.

5. **AI developers lean toward managed services.** Based on [01_cncf_survey.md, Data Point 25], "30% of AI developers use Machine Learning as a Service (MLaaS) platforms, which abstract away infrastructure management." Based on [01_cncf_survey.md, Data Point 24], "Only 41% of professional AI developers are cloud native." This suggests the majority of AI developers -- especially at small companies -- use managed abstractions rather than running their own orchestration.

6. **YC startup patterns confirm cloud-managed defaults.** Based on [08_vc_startup_db.md, Data Point: YC partnership], "58% of Y Combinator startups accepting Azure credits" and GPU availability drives provider selection, not orchestration sophistication. Based on [08_vc_startup_db.md, Data Point: YC founder], "No one can spend $20,000 to $30,000 a month on infrastructure costs" -- cost constraints push toward simpler, pay-per-use models.

**Confidence:** 6/10 -- Direction is well-supported (small companies default to simpler infrastructure), but precise percentage within the 55-70% range is estimated due to lack of direct AI SaaS tier segmentation.

---

### 2. Managed Kubernetes (EKS/AKS/GKE): 20-35%

**Classification:** Estimated

**Definition:** AWS EKS, Azure AKS, Google GKE, Oracle OKE -- managed control plane with cloud-provider-operated Kubernetes.

**Reasoning and Evidence Chain:**

1. **A minority of sub-$10M AI SaaS companies adopt managed K8s, but the minority is non-trivial.** Based on [01_cncf_survey.md, Data Point 27], companies under 1,000 employees represent only 9% of K8s adopters. However, within the AI SaaS vertical specifically, GPU workload requirements can push even small teams toward K8s earlier. Based on [02_analyst_reports.md, Data Point 8], "66% of organizations hosting generative AI models use Kubernetes to manage some or all of their inference workloads." Even accounting for heavy enterprise skew in that sample, some sub-$10M AI companies that self-host models will use managed K8s for GPU orchestration.

2. **Companies doing model training or self-hosting inference gravitate toward K8s.** Based on [04_tech_blogs.md, Case Study: Sonantic], even a seed-stage AI voice company "transitioned infrastructure to AWS Elastic Kubernetes Service (EKS) with GPU support." Based on [05_cloud_vendor_cases.md, Case Study 22], Stacks -- a startup that "raised EUR 10 million" in 2025 (placing it in this tier) -- uses "GKE Autopilot" for its AI accounting platform. These case studies demonstrate that some companies in this tier do adopt managed K8s, particularly when GPU orchestration is a core requirement.

3. **Managed K8s has become simpler, lowering the adoption barrier.** Based on [06_stackshare_github.md, Data Point: Managed K8s growth], "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022." GKE Autopilot and similar fully managed offerings reduce the operational burden, making K8s more accessible to smaller teams. Based on [02_analyst_reports.md, Data Point 1], "73% of cloud Kubernetes clusters are managed" -- the self-managed option is increasingly uncommon even among K8s users.

4. **The 20-35% range accounts for the subset of sub-$10M AI SaaS that has GPU-intensive or model-hosting requirements.** Not all AI SaaS companies self-host models. Based on [02_analyst_reports.md, Data Point 11], "37% using managed APIs, 25% self-hosting" for AI/ML model hosting. Companies using managed APIs (calling OpenAI, Anthropic, etc.) have no GPU orchestration need and thus no K8s pull. The ~25% that self-host models are more likely to adopt K8s even at small scale, particularly managed K8s for GPU node pools.

**Confidence:** 5/10 -- The range is wide (20-35%) because the driver is workload type (self-hosted models vs. API-only) rather than company size alone. No direct data segments sub-$10M AI SaaS K8s adoption.

---

### 3. Open/Self-Managed Kubernetes: 2-5%

**Classification:** Estimated

**Definition:** Self-hosted Kubernetes without a cloud-managed control plane. Includes k3s, kubeadm, Rancher-managed on bare metal or VMs.

**Reasoning and Evidence Chain:**

1. **Self-managed K8s requires dedicated infrastructure expertise that sub-$10M companies typically lack.** Based on [03_job_postings.md, Data Point 20], "Senior-level: 60%" and "Lead-level: 15%" for DevOps positions -- K8s operations is an expert skill. Based on [03_job_postings.md, Data Point 16], K8s-specific roles command "$166,836 average" salary. A sub-$10M ARR company cannot dedicate 1-2 senior engineers ($300K+ fully loaded) to managing K8s infrastructure when the entire engineering team is 5-30 people.

2. **Even among all K8s users, self-managed is a minority and shrinking.** Based on [02_analyst_reports.md, Data Point 1], "73% of cloud Kubernetes clusters are managed." Based on [06_stackshare_github.md, Data Point: cloud-hosted clusters], "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022." The trend is strongly away from self-managed.

3. **The few sub-$10M companies running self-managed K8s likely have specific compliance or cost constraints.** Possible scenarios: on-premises GPU hardware (purchased to avoid cloud GPU costs), data sovereignty requirements, or founding teams with deep K8s expertise from prior roles. Based on [04_tech_blogs.md, Case Study: Salesforce], self-managed K8s on bare metal exists at large enterprises (Salesforce), but the operational overhead is untenable for small teams.

4. **CNCF data confirms early adopters struggle.** Based on [01_cncf_survey.md, Data Point 14], "46% of organizations just beginning their cloud native journey identify lack of training as biggest challenge." Sub-$10M AI SaaS companies are by definition early in their infrastructure journey and face this training gap acutely.

**Confidence:** 5/10 -- High confidence that self-managed K8s is very rare at this tier. The 2-5% range is estimated; the true figure could be lower (1-3%).

---

## Typical Patterns and Migration

### Most Common Starting Architecture

**Classification:** Inferred

The most common starting architecture for AI SaaS companies in this tier is a **serverless + managed services stack**:

- **Application layer:** Vercel/Netlify (frontend) + AWS Lambda or Cloud Run (API/backend)
- **AI inference:** Managed API calls to OpenAI/Anthropic/Google (majority) or SageMaker/Bedrock (minority)
- **Data layer:** Managed PostgreSQL (RDS, Cloud SQL) + managed vector database (Pinecone, Weaviate Cloud)
- **If self-hosting models:** Single GPU instance (EC2 p-series, GCP A2/A3) with Docker, possibly ECS/Fargate

**Evidence:**
- Based on [08_vc_startup_db.md, Data Point: Maven Solutions], "Seed stage... Monolithic architecture is recommended as a superpower, rather than prematurely adopting microservices."
- Based on [08_vc_startup_db.md, Data Point: Series A guidance], "Series A is about doubling down on efficiency... moving to structured environments (dev/stage/prod)."
- Based on [02_analyst_reports.md, Data Point 11], 37% of organizations use managed APIs for AI model hosting -- the simplest approach and dominant at this tier.

### Migration Patterns Within the Tier

**Classification:** Inferred

As companies approach $5-10M ARR and scale beyond 20 engineers, a common migration pattern emerges:

1. **$0-2M ARR (Seed):** PaaS/serverless monolith. Single cloud provider. Managed AI APIs exclusively. No containers or minimal Docker usage.

2. **$2-5M ARR (Seed+ / Series A):** Migration to containerized services. Docker on ECS/Fargate or Cloud Run. Some companies begin evaluating managed K8s for GPU workloads. Infrastructure-as-Code introduced (Terraform).

3. **$5-10M ARR (Series A/B):** First K8s adoption for companies with model-hosting needs. Managed K8s (EKS/GKE) for GPU node pools. API-only companies may stay on serverless/ECS. Platform engineering practices begin.

**Evidence for migration toward K8s at scale:**
- Based on [04_tech_blogs.md, Migration: Figma], Figma migrated from ECS to EKS for "cost savings, improved developer experience, and increased resiliency" -- though Figma was well above $10M ARR at migration time.
- Based on [04_tech_blogs.md, Migration: Grammarly], Grammarly moved from EC2 to EKS for ML infrastructure -- also above this tier but illustrative of the pattern.
- Based on [08_vc_startup_db.md, Data Point: Maven Solutions], "Microservices architecture with Kubernetes orchestration is best suited for funded SaaS startups targeting large-scale deployments" -- recommended for later stages.

**Confidence:** 5/10 -- Migration patterns are inferred from case studies of larger companies and prescriptive guidance, not direct observation of sub-$10M companies.

---

## Engineering Team Size and K8s Capability

### Team Size at This Tier

**Classification:** Inferred

Based on general SaaS benchmarks and the stage context:

| ARR Range | Typical Total Headcount | Eng Team Size | DevOps/Infra Headcount |
|-----------|------------------------|---------------|----------------------|
| $0-1M | 5-15 | 3-8 | 0 (founders handle it) |
| $1-3M | 10-25 | 5-15 | 0-1 (part-time) |
| $3-5M | 15-40 | 8-20 | 0-1 (dedicated) |
| $5-10M | 25-60 | 12-30 | 1-2 (dedicated) |

### Can They Run Self-Managed K8s?

**Classification:** Inferred

**No, with rare exceptions.**

Based on [03_job_postings.md, Data Point 20], 60% of K8s DevOps positions require senior-level expertise, and only 5% are junior-level. This reflects the genuine complexity of operating Kubernetes. Based on [03_job_postings.md, Data Point 16], K8s specialists command $166K+ average salary (North America Q2 2025: $170K). A sub-$10M company with 0-2 dedicated infrastructure staff cannot:

1. Maintain K8s control plane availability (upgrades, patches, etcd management)
2. Manage node provisioning and autoscaling
3. Handle networking (CNI, ingress, service mesh)
4. Operate monitoring/observability at the cluster level
5. Manage security (RBAC, network policies, pod security)

Based on [06_stackshare_github.md, Data Point: service mesh complexity], "48% of DevOps engineers report struggling with the steep learning curve and management overhead introduced by mesh architectures." If mature DevOps engineers struggle with service mesh alone, a small team has no realistic capacity for self-managed K8s.

**Exception scenarios where self-managed K8s might exist at this tier:**
- Founding team includes ex-Google/Meta/Kubernetes-contributor with deep operational knowledge
- Company has purchased on-premises GPU hardware and needs orchestration
- Specific regulatory requirement for on-premises deployment
- Using lightweight distributions (k3s) for edge deployments

**Managed K8s (EKS/GKE Autopilot) is achievable** at this tier with 1-2 engineers who have moderate K8s experience, because the cloud provider handles control plane operations. GKE Autopilot in particular abstracts away node management entirely.

Based on [05_cloud_vendor_cases.md, Case Study 22], Stacks (EUR 10M funding, founded 2024) uses GKE Autopilot -- demonstrating that fully managed K8s can serve this tier.

**Confidence:** 7/10 -- Strong evidence that self-managed K8s is beyond the capability of most sub-$10M teams. Managed K8s is feasible but requires deliberate team investment.

---

## Infrastructure Spend as Percentage of Revenue

### Estimates by Sub-Tier

**Classification:** Mixed (Direct for general ranges, Estimated for tier-specific)

| Company Type | Infra % of Revenue | Source | Classification |
|---|---|---|---|
| Traditional SaaS (baseline) | 5-15% | [07_sec_earnings.md; 08_vc_startup_db.md] | Direct |
| AI SaaS early-stage (general) | 24-80% | [08_vc_startup_db.md: "Hidden Stack" analysis] | Direct |
| AI SaaS at scale | 40-50% | [07_sec_earnings.md: Monetizely] | Direct |
| AI SaaS sub-$10M (API-only) | 15-30% | Estimated | Estimated |
| AI SaaS sub-$10M (self-hosting models) | 40-80% | Estimated | Estimated |

**Evidence Chain:**

1. Based on [08_vc_startup_db.md, Data Point: "Hidden Stack" AI Infrastructure], "For AI startups, compute costs as a percentage of revenue is a critical metric, with AI startups often starting much higher than traditional software companies -- sometimes in the 50-80% range, versus the 10-15% typical for traditional SaaS businesses."

2. Based on [08_vc_startup_db.md, Data Point: AI cost trajectory], "Compute costs for AI companies went from 24% of revenue to 50% of revenue (versus non-AI SaaS where it more or less stayed at about 18% of revenue over the course of a year)."

3. Based on [07_sec_earnings.md, Data Point: Monetizely], "an AI SaaS might see 40-50% (or more) of revenue eaten by COGS in the form of model hosting, inference compute, and data costs."

4. Based on [07_sec_earnings.md, Data Point: Replit], "Replit saw its gross margin improve from single-digits into the ~20-30% range" -- demonstrating that some AI SaaS companies at this tier have infrastructure costs exceeding 70% of revenue.

5. Based on [08_vc_startup_db.md, Data Point: Bessemer], "a cohort of fast-scaling AI SaaS startups had only ~25% gross margin on average in early stages" -- implying 75% COGS, with infrastructure as the largest component.

**Critical distinction at this tier:** Companies calling managed APIs (OpenAI, Anthropic) have lower infrastructure costs (15-30% of revenue) because they pay per-token rather than maintaining GPU infrastructure. Companies self-hosting models face 40-80% infrastructure costs. The mix within this tier heavily favors API-only approaches, which keeps the average lower than the self-hosting extreme.

**Confidence:** 6/10 -- General AI SaaS cost ranges are well-documented. The specific API-only vs. self-hosting distinction at sub-$10M is estimated but logically derived.

---

## Decision Drivers for Architecture Choice

### Primary Drivers at This Tier

**Classification:** Inferred (synthesized from multiple Wave 1 sources)

Ranked by importance for sub-$10M AI SaaS companies:

#### 1. Speed to Market (Highest Priority)

At this tier, companies are typically pre-PMF or early post-PMF. Every week spent on infrastructure is a week not spent on product.

- Based on [08_vc_startup_db.md, Data Point: Maven Solutions], "Seed stage... key goals being reaching the next significant funding stage with minimal monthly spending while reaching product-market fit."
- Based on [08_vc_startup_db.md, Data Point: Series A guidance], "Series A is about doubling down on efficiency."
- **Architecture implication:** PaaS and serverless win because deployment takes minutes, not days. K8s clusters take weeks to properly configure and secure.

#### 2. Engineering Team Constraints

With 0-2 infrastructure-capable engineers, the architecture must be operable by generalist backend developers, not K8s specialists.

- Based on [03_job_postings.md, Data Point 20], K8s roles are 60% senior-level and command $166K+ salaries.
- Based on [01_cncf_survey.md, Data Point 14], "46% of organizations just beginning their cloud native journey identify lack of training as biggest challenge."
- **Architecture implication:** Managed services that require zero infrastructure expertise (Lambda, Cloud Run, Vercel) dominate. Managed K8s (GKE Autopilot) is the maximum complexity most teams can handle.

#### 3. Cost (Absolute Spend, Not Efficiency)

At sub-$10M ARR, absolute cloud bills matter more than cost-per-request efficiency. A $5K/month bill on Lambda is acceptable even if K8s would be $3K/month -- the $2K savings does not justify the operational overhead.

- Based on [08_vc_startup_db.md, Data Point: YC founder quote], "No one can spend $20,000 to $30,000 a month on infrastructure costs."
- Based on [07_sec_earnings.md, Data Point: CIO Magazine], "89% of CFOs report that rising cloud costs have negatively impacted gross margins."
- **Architecture implication:** Serverless pay-per-use models align with variable revenue. K8s clusters have fixed base costs (control plane, minimum nodes) that are disproportionate at low scale.

#### 4. GPU Access and AI Workload Requirements

For companies that self-host models, GPU availability and orchestration become a top driver.

- Based on [08_vc_startup_db.md, Data Point: YC founder on Azure], "Azure was the only place where they could find GPUs, with access available within an hour and a half."
- Based on [06_stackshare_github.md, Data Point: serverless GPU support], "Google Cloud Run and Azure Container Instances both support GPU-based workloads while AWS Fargate does not."
- **Architecture implication:** GPU availability drives cloud provider selection first, then architecture selection. Companies needing GPUs may adopt managed K8s (EKS with GPU node pools) earlier than they otherwise would.

#### 5. Scalability Preparedness

Some companies, especially those with VC backing and aggressive growth targets, adopt K8s early to avoid a painful migration later.

- Based on [04_tech_blogs.md, Migration: Figma], even successful migrations from ECS to K8s take 12 months. Avoiding that migration has value.
- Based on [08_vc_startup_db.md, Data Point: Maven Solutions], "Microservices architecture with Kubernetes orchestration is best suited for funded SaaS startups targeting large-scale deployments."
- **Architecture implication:** ~20-35% of well-funded sub-$10M companies adopt managed K8s preemptively, accepting higher current complexity for reduced future migration risk.

#### 6. Compliance and Data Sovereignty

For companies in regulated verticals (healthcare, fintech), compliance requirements may constrain architecture choices.

- Based on [01_cncf_survey.md, Data Point 11], "Small organizations: 27% hybrid cloud adoption" -- lower than large enterprises (56%) but non-trivial.
- Based on [05_cloud_vendor_cases.md, Case Study 4: Sonantic], even seed-stage companies achieved "100% compliance score in AWS Security Hub" on EKS.
- **Architecture implication:** Compliance requirements rarely force K8s at this tier. Most compliance needs can be met with serverless + managed services (SOC 2, HIPAA on AWS/GCP/Azure). Self-managed K8s for compliance is almost exclusively a large-enterprise pattern.

**Confidence:** 7/10 -- The ranking of decision drivers is well-supported by converging evidence across multiple sources.

---

## Multi-Architecture Usage

### Estimated Prevalence: 15-25% of Companies in This Tier

**Classification:** Estimated

**Definition:** Companies running production workloads on two or more architecture categories simultaneously (e.g., Lambda for API backend + EKS for model inference).

**Reasoning:**

1. Based on [02_analyst_reports.md, Data Point 17], "66% of organizations using serverless functions also use container orchestration." This demonstrates that hybrid architectures are common in the general population. At the sub-$10M tier, the prevalence is lower because most companies have not yet reached the complexity requiring multiple orchestration layers.

2. Based on [02_analyst_reports.md, Data Point 29], organizations use an average of 2.4 public cloud providers. Multi-cloud does not necessarily mean multi-architecture, but it increases the likelihood.

3. The most likely hybrid pattern at this tier: **Serverless API layer + managed K8s for GPU inference**. The API and web application run on Lambda/Cloud Run (simple, scalable, cheap), while GPU-intensive model inference runs on an EKS/GKE cluster with GPU node pools. This pattern emerges when companies transition from managed AI APIs to self-hosted models.

4. A secondary pattern: **PaaS for web app + serverless for async processing**. Example: Vercel for Next.js frontend + Lambda for background jobs + SageMaker for occasional batch inference.

**Who uses multiple architectures at this tier:**
- Companies transitioning from API-only to self-hosted models (~10-15% of tier)
- Companies with distinct workload types (web serving vs. batch processing vs. inference) (~5-10% of tier)

**Who does NOT:**
- Pure API-wrapper AI SaaS (calling OpenAI/Anthropic only) -- single serverless architecture suffices
- Very early stage (pre-$1M ARR) -- insufficient complexity to justify multiple architectures

**Confidence:** 4/10 -- This is the least well-supported estimate. No Wave 1 source provides hybrid architecture data segmented by company size or revenue tier.

---

## Assumptions Register

| # | Assumption | Impact if Wrong | Confidence |
|---|---|---|---|
| A1 | Companies under $10M ARR have 5-30 engineers | If larger eng teams, K8s adoption would be higher | Medium |
| A2 | Sub-500-employee companies behave differently from the 500-1000 bracket in CNCF data | If similar, K8s adoption at this tier would be ~9% not 2-5% for self-managed | Medium |
| A3 | AI SaaS companies at this tier are primarily on a single cloud provider | If multi-cloud, architecture complexity increases | High |
| A4 | Majority of sub-$10M AI SaaS call managed APIs rather than self-host models | If more self-host, K8s adoption would be higher and cloud-native lower | Medium |
| A5 | VC-backed stage guidance (Maven Solutions, SaaStr) reflects actual behavior, not just recommendations | If companies ignore guidance and adopt K8s early, managed K8s could be 35-45% | Low-Medium |
| A6 | CNCF survey company-size data (91% enterprise) can be inverted to estimate small-company behavior | Inverting enterprise data is imprecise; small companies may have unique patterns | Low |
| A7 | Stacks (GKE Autopilot, EUR 10M raise) is representative of this tier's K8s adopters | It may be an outlier; most sub-$10M companies may not appear in vendor case studies | Low |
| A8 | Infrastructure cost ranges for AI SaaS (24-80%) apply to sub-$10M companies proportionally | Costs could be higher (less optimization) or lower (smaller workloads) at this tier | Medium |
| A9 | The term "AI SaaS" at this tier includes both model-hosting companies and API-wrapper companies | If restricted to model-hosting only, K8s adoption would be significantly higher | High |
| A10 | 2024-2025 data is representative of the current (2026) landscape | AI infrastructure is evolving rapidly; patterns may have shifted | Medium |

---

## Evidence Gaps

### Critical Gaps (Directly Impact Core Estimates)

1. **No direct survey of sub-$10M AI SaaS infrastructure choices exists.** Every architecture percentage in this analysis is estimated or inferred. A survey of 100+ companies in this tier would dramatically improve confidence.

2. **CNCF data does not measure companies under 500 employees.** Based on [01_cncf_survey.md, Data Point 27], the smallest bracket is 500-1,000 employees (9% of K8s users). Sub-$10M ARR companies are typically under 100 employees, an entirely unmeasured population in CNCF surveys.

3. **No data on API-only vs. model-hosting split by revenue tier.** Based on [02_analyst_reports.md, Data Point 11], 37% use managed APIs and 25% self-host, but this is not segmented by company size. The split is likely very different at sub-$10M (more API-only) vs. $100M+ (more self-hosting).

4. **No engineering team size benchmarks specific to AI SaaS by ARR.** General SaaS team-size benchmarks may not apply to AI companies that require more specialized ML/infrastructure talent.

5. **Case study coverage of this tier is minimal.** Based on [04_tech_blogs.md, Data Quality Assessment], "Small AI SaaS (<$10M ARR) underrepresented" in engineering blogs. Based on [05_cloud_vendor_cases.md, Data Quality Assessment], "Very few early-stage startups represented" in vendor case studies. Only one company (Stacks) in the Wave 1 data is clearly in this tier.

### Moderate Gaps (Affect Precision of Estimates)

6. **Serverless vs. managed containers split within "cloud-native non-K8s."** We estimate 55-70% cloud-native, but cannot determine what portion is serverless functions (Lambda) vs. managed containers (Fargate/Cloud Run) vs. PaaS (Heroku/Vercel/Render).

7. **Migration trigger data.** No source documents when sub-$10M companies typically migrate from serverless to K8s. Is it driven by workload requirements, team size, revenue milestones, or compliance needs?

8. **Multi-cloud prevalence at this tier.** Based on [01_cncf_survey.md, Data Point 11], small organizations show 27% hybrid cloud adoption, but "small" is not defined by revenue, and hybrid cloud does not equal multi-architecture.

9. **Geographic variation.** Nearly all Wave 1 data is US-centric. European AI SaaS companies may show different patterns due to GDPR, data sovereignty, and different VC ecosystems.

10. **Cost optimization practices at this tier.** No data on whether sub-$10M AI SaaS companies use reserved instances, spot instances, or committed use discounts. Based on [07_sec_earnings.md], these are documented only for large public companies.

---

## Summary Table

| Question | Estimate | Classification | Confidence |
|---|---|---|---|
| % Cloud-native (non-K8s managed) | 55-70% | Estimated | 6/10 |
| % Managed Kubernetes | 20-35% | Estimated | 5/10 |
| % Open/Self-managed Kubernetes | 2-5% | Estimated | 5/10 |
| Most common starting architecture | Serverless + managed APIs | Inferred | 7/10 |
| Can teams run self-managed K8s? | No (with rare exceptions) | Inferred | 7/10 |
| Infrastructure spend % of revenue (API-only) | 15-30% | Estimated | 6/10 |
| Infrastructure spend % of revenue (self-hosting) | 40-80% | Direct/Estimated | 6/10 |
| Top decision driver | Speed to market | Inferred | 7/10 |
| % using multiple architectures | 15-25% | Estimated | 4/10 |

---

## Cross-Reference Matrix: Wave 1 Source Utilization

| Wave 1 File | Key Data Used | Relevance to This Tier |
|---|---|---|
| 01_cncf_survey.md | K8s adoption by company size (DP 27-28), serverless decline (DP 31-32), AI developer cloud-native rates (DP 24-25), training challenges (DP 14) | High -- company size data is most directly applicable proxy |
| 02_analyst_reports.md | Managed vs self-managed K8s split (DP 1-3), serverless adoption by cloud (DP 13-16), AI model hosting split (DP 11), hybrid serverless+K8s (DP 17) | High -- provides architecture distribution baselines |
| 03_job_postings.md | K8s role seniority (DP 20), salary data (DP 16), company size distribution (DP 7), platform engineering growth (DP 8) | Medium -- salary/skill data informs team capability assessment |
| 04_tech_blogs.md | Migration patterns (Figma ECS->K8s, Grammarly EC2->EKS), Stacks GKE Autopilot case, Sonantic seed-stage EKS | High -- case studies provide qualitative validation |
| 05_cloud_vendor_cases.md | Stacks (EUR 10M, GKE Autopilot), Sonantic (seed-stage, EKS), ECS/Fargate case studies, Azure Container Apps | Medium -- limited tier coverage but provides counterexamples |
| 06_stackshare_github.md | K8s enterprise adoption 96%, serverless framework adoption 11%, cloud-hosted K8s trend (45%->67%), service mesh complexity | Medium -- enterprise skew limits direct applicability |
| 07_sec_earnings.md | AI SaaS COGS 40-50%, traditional SaaS COGS 15-30%, Replit margin data, cloud spend as % revenue | High -- cost economics directly applicable |
| 08_vc_startup_db.md | Stage-specific guidance (Maven Solutions), AI infra costs 24-80%, YC GPU access, Bessemer gross margins, K8s platform VC funding | High -- most directly relevant to this tier |

---

## Methodology Notes

This analysis synthesized 8 Wave 1 research files containing 200+ data points from CNCF surveys, analyst reports (Gartner, Datadog, Dynatrace), engineering blogs, cloud vendor case studies, StackShare/GitHub signals, SEC filings, job posting analysis, and VC/startup databases.

**Approach:** Because no Wave 1 source directly segments AI SaaS companies by the sub-$10M ARR tier, this analysis applied a triangulation methodology:
1. Identified the most relevant proxy signals (company size from CNCF, stage guidance from VCs, cost data from SEC/analyst reports)
2. Applied downward adjustments to enterprise K8s adoption rates based on company size and team capacity data
3. Applied upward adjustments to serverless/PaaS estimates based on startup stage guidance and cost constraints
4. Validated directional estimates against the small number of case studies in this tier (Stacks, Sonantic)
5. Explicitly flagged every assumption and evidence gap

**What would improve this analysis:**
- A direct survey of 100+ sub-$10M AI SaaS companies about their infrastructure choices
- Portfolio infrastructure audits from major AI-focused VCs (a16z, Bessemer, Lightspeed)
- Cloud provider usage data segmented by customer ARR (available to cloud providers but not public)
- Longitudinal case studies tracking infrastructure evolution from founding through $10M ARR

---

**Analysis Compiled:** 2026-02-12
**Analyst:** Wave 2 Analysis Agent (Tier: Under $10M ARR)
**Sources:** 8 Wave 1 research files (01-08)
**Overall Confidence:** 5.5/10 -- Directional estimates are well-supported; precise percentages are low-confidence due to fundamental evidence gaps at this tier.
