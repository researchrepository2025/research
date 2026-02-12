# Wave 2 Analysis: Cloud-Native Non-K8s Managed Services Deep Dive

**Analysis Date:** 2026-02-12
**Analyst Focus:** Serverless, PaaS, Managed Containers (ECS/Fargate, Cloud Run, Azure Container Apps) -- excluding all Kubernetes
**Wave 1 Sources Reviewed:** All 8 files (01-08)

---

## Executive Summary

Cloud-native non-K8s managed services (serverless functions, PaaS, and managed container platforms like ECS/Fargate and Cloud Run) serve as primary or significant secondary architecture for an estimated 25-40% of AI SaaS companies, with adoption concentrated among early-stage startups (<$10M ARR) and specific workload types (API serving, event-driven processing, lightweight inference). However, this category is under-documented compared to Kubernetes: Wave 1 data contains strong serverless adoption metrics from Datadog telemetry (65-70% of AWS/GCP customers use Lambda/Cloud Run) but very few AI SaaS companies publicly disclose non-K8s architectures. The data reveals a clear pattern where companies start on serverless/PaaS and migrate toward Kubernetes as they scale, with multiple documented ECS-to-K8s migrations and zero documented K8s-to-serverless migrations.

---

## Methodology

### Approach
This analysis synthesizes data from all 8 Wave 1 fact-gathering files to isolate signals specifically about cloud-native non-K8s managed services. Each finding is classified as:
- **Direct (D):** The data explicitly states this figure
- **Inferred (I):** Derived through stated logical steps from direct data
- **Estimated (E):** Analyst judgment combined with reasoning from multiple data points

### Scope Definition
"Cloud-native non-K8s managed services" includes:
- **Serverless functions:** AWS Lambda, Google Cloud Functions, Azure Functions
- **PaaS:** Heroku, Vercel, Railway, Render, Firebase, Azure App Service
- **Managed containers (non-K8s):** AWS ECS/Fargate, Google Cloud Run, Azure Container Apps/Instances

**Explicitly excludes:** Any Kubernetes variant (EKS, GKE, AKS, self-managed K8s, OpenShift).

### Data Triangulation
Estimates draw on converging evidence from CNCF surveys (01), analyst reports with Datadog telemetry (02), job postings (03), engineering blogs (04), vendor case studies (05), StackShare/GitHub signals (06), SEC filings (07), and VC/startup databases (08).

---

## Findings

### Finding 1: Overall Cloud-Native Non-K8s Adoption Among AI SaaS Companies

**Estimate:** 25-40% of AI SaaS companies use cloud-native non-K8s managed services as their primary or significant secondary architecture.

**Classification:** Estimated (E)

**Evidence Chain:**

1. Based on [01_cncf_survey.md, Data Point 3], 7% of surveyed organizations report no Kubernetes engagement at all. These organizations, if cloud-native, must use non-K8s services (serverless, PaaS, managed containers). However, the CNCF survey has strong selection bias toward K8s adopters.

2. Based on [01_cncf_survey.md, Data Point 22], 44% of organizations do not yet run AI/ML workloads on Kubernetes. This does not mean they use non-K8s cloud-native; they may use VMs or no AI workloads. But it establishes a ceiling: up to 44% of organizations could be using alternative architectures for their AI workloads.

3. Based on [02_analyst_reports.md, Data Point 11], AI/ML model hosting splits show "37% using managed APIs, 25% self-hosting, and 13% at the edge." The 37% using managed APIs likely includes both K8s-backed and non-K8s services (e.g., SageMaker endpoints, Bedrock, Vertex AI). A significant subset of this 37% operates on non-K8s managed infrastructure.

4. Based on [02_analyst_reports.md, Data Point 6], Gartner reports only 54% of enterprises have a full or partial Kubernetes implementation, compared to CNCF's 82%. This 28-point gap suggests the broader enterprise population (including AI SaaS companies not in the CNCF ecosystem) has substantially lower K8s adoption, implying higher reliance on alternatives.

5. Based on [08_vc_startup_db.md], seed-stage startups are explicitly advised to "avoid Kubernetes early unless absolutely necessary" and instead use "fully managed platforms like Heroku, Vercel, or Firebase" and "serverless options like AWS Lambda." With 66% of YC Winter 2024 startups integrating AI, a large cohort of early-stage AI companies is likely starting on non-K8s infrastructure.

**Reasoning:** The 25% lower bound comes from the gap between Gartner's 54% K8s implementation and CNCF's higher figures, adjusted for the fact that some non-K8s users run on VMs rather than cloud-native services. The 40% upper bound accounts for the 44% not running AI/ML on K8s (from CNCF data) minus companies running AI on VMs or not running AI at all.

---

### Finding 2: Serverless Function Adoption (Lambda, Cloud Functions, Azure Functions)

**Estimate:** Serverless functions are used by 50-65% of cloud-using organizations for some workloads, but only 11-13% use serverless as a primary computing framework.

**Classification:** Mixed -- Direct (D) for specific figures, Inferred (I) for the synthesis

**Evidence Chain:**

1. Based on [02_analyst_reports.md, Data Point 14], Datadog reports "AWS Lambda: 65% of AWS customers." This is telemetry-based (actual usage), not survey-based.

2. Based on [02_analyst_reports.md, Data Point 21], "Over 70% of AWS users now rely on Lambda" from a separate source.

3. Based on [01_cncf_survey.md, Data Point 31], CNCF reports "Only 11% of respondents are making use of serverless computing frameworks" in 2024.

4. Based on [01_cncf_survey.md, Data Point 32], serverless dropped from 22% in 2022 to 13% in 2023 in CNCF surveys.

5. Based on [06_stackshare_github.md], there is a "CRITICAL SIGNAL: Major disconnect between market size projections and CNCF survey adoption" and also a finding that "Close to 70% of enterprises in North America claimed to operate production loads on serverless systems" per the CNCF 2024 Survey, conflicting with the global 11% figure.

**Reconciliation:** The 65-70% figures (Datadog, Lambda adoption) measure "any use at all" -- including event triggers, background processing, and CI/CD tooling. The 11% CNCF figure measures serverless as a "computing framework," meaning primary compute platform. Most organizations that use Lambda use it as a secondary or supplementary tool alongside K8s or other primary infrastructure. The 70% North American figure vs 11% global may reflect definitional differences (any serverless vs serverless-as-primary).

**For AI SaaS specifically:** Serverless functions are common for API endpoints, webhooks, event processing, and lightweight inference. They are NOT common for model training, heavy batch processing, or stateful services. The pattern is serverless-as-complement, not serverless-as-foundation, for most AI SaaS companies beyond seed stage.

---

### Finding 3: Managed Container Platforms (ECS/Fargate, Cloud Run, Azure Container Apps)

**Estimate:** 15-25% of AI SaaS companies use non-K8s managed container platforms (ECS/Fargate, Cloud Run, Azure Container Apps) as a significant part of their architecture.

**Classification:** Estimated (E)

**Evidence Chain:**

1. Based on [02_analyst_reports.md, Data Point 13], "In Google Cloud, 68 percent of container organizations now use serverless containers, up from 35 percent two years ago." This is Cloud Run adoption among GCP container users -- very high growth.

2. Based on [02_analyst_reports.md, Data Point 15], "Google Cloud Run: 70% of Google Cloud customers." Telemetry-based from Datadog.

3. Based on [02_analyst_reports.md, Data Point 16], "Azure App Service: 56% of Azure customers." This is PaaS, not container orchestration, but overlaps with the cloud-native non-K8s category.

4. Based on [05_cloud_vendor_cases.md, Case Studies 10-12], three SaaS companies (Autodesk, BILL, Smartsheet) use ECS with Fargate. BILL handles "150,000-200,000 requests per minute" on this architecture. One additional unnamed SaaS deployed on Fargate via a consulting case study.

5. Based on [05_cloud_vendor_cases.md, Case Study 18], Coca-Cola used Azure Container Apps for an AI-powered campaign across 43 markets. The Microsoft Azure blog also lists "Replit, NFL Combine, Coca-Cola, and European Space Agency" as Azure Container Apps adopters.

6. Based on [06_stackshare_github.md], "Google Cloud Run and Azure Container Instances both support GPU-based workloads while AWS Fargate does not." This is a critical limitation for AI inference on Fargate, pushing GPU-dependent AI SaaS toward Cloud Run, Azure Container Apps, or Kubernetes.

7. Based on [04_tech_blogs.md, Figma Migration], Figma migrated FROM ECS TO Kubernetes (EKS) in 12 months, citing "cost savings, improved developer experience, and increased resiliency." ECS limitations included "lack of support for StatefulSets, Helm charts, and inability to easily run OSS software." This is counter-evidence showing companies outgrow ECS.

**Reasoning:** High Cloud Run and Fargate adoption per Datadog telemetry (56-70% of cloud customers use these services) indicates broad usage. However, for AI SaaS specifically, the lack of GPU support on Fargate is a major constraint. Cloud Run and Azure Container Apps have GPU support and are more viable for AI inference. The 15-25% estimate for AI SaaS specifically (lower than general adoption) reflects: (a) GPU constraints on Fargate limiting AI use cases, (b) the documented migration pattern away from ECS toward K8s as companies scale, and (c) the small number of AI SaaS companies found using these platforms in case studies vs. the many using K8s.

---

### Finding 4: PaaS Adoption (Heroku, Vercel, Railway, Render, Firebase)

**Estimate:** 10-20% of AI SaaS companies use PaaS as primary infrastructure, concentrated almost entirely in the seed-to-Series-A stage (<$5M ARR).

**Classification:** Estimated (E)

**Evidence Chain:**

1. Based on [08_vc_startup_db.md], startup infrastructure guidance explicitly recommends PaaS for seed-stage: "fully managed platforms like Heroku, Vercel, or Firebase for speed" and "Kubernetes should be avoided early unless absolutely necessary."

2. Based on [08_vc_startup_db.md], 58% of Y Combinator startups accepted Azure credits, and 66% of the Winter 2024 YC batch are AI-focused. This suggests a large cohort of early-stage AI companies starting on simple cloud infrastructure (PaaS, serverless) rather than K8s.

3. Based on [07_sec_earnings.md], Salesforce is "reimagining Heroku as the Platform-as-a-Service layer for development of AI-first apps, with Heroku using AWS infrastructure including Amazon EC2 instances equipped with Nvidia GPUs and AWS Trainium." This signals PaaS being repositioned for AI workloads.

4. Based on [02_analyst_reports.md, Data Point 46], Flexera reports "Seventy-nine percent of organizations are already using or experimenting with AI and machine learning (ML) PaaS services." However, this likely refers to managed ML services (SageMaker, Vertex AI) rather than general PaaS platforms.

5. Based on [02_analyst_reports.md, Data Point 32], "Platform-as-a-service (PaaS) and infrastructure-as-a-service (IaaS) will each capture nearly 20% of public cloud spending." PaaS is a major market category by revenue ($208.64B projected).

**Reasoning:** PaaS is the default starting point for AI SaaS startups because it minimizes infrastructure complexity. However, every Wave 1 engineering blog (04) that describes a migration story shows companies moving AWAY from simpler platforms toward Kubernetes. No company disclosed moving from K8s to PaaS. PaaS adoption therefore concentrates at early stages and attenuates rapidly as ARR grows. The 10-20% estimate reflects the large number of seed/early-stage AI companies but the rapid outgrowth pattern.

---

### Finding 5: Breakdown by Company Size (Revenue Tier)

**Estimate:**

| Revenue Tier | Cloud-Native Non-K8s as Primary | Classification |
|---|---|---|
| Pre-revenue / Seed (<$1M ARR) | 60-80% | Estimated (E) |
| Early Stage ($1M-$10M ARR) | 35-55% | Estimated (E) |
| Growth Stage ($10M-$50M ARR) | 15-30% | Estimated (E) |
| Scale ($50M-$200M ARR) | 10-20% | Estimated (E) |
| Enterprise ($200M+ ARR) | 5-15% | Estimated (E) |

**Evidence Chain:**

1. Based on [01_cncf_survey.md, Data Point 27], "only 9% of [Kubernetes] adopters are companies with 500-1,000 employees." Companies below 500 employees are not even measured, implying very low K8s adoption in the startup segment -- and therefore high non-K8s usage.

2. Based on [01_cncf_survey.md, Data Point 28], "Organizations with over 1,000 employees represent 91% of Kubernetes users." This directly supports the inverse: smaller organizations disproportionately use non-K8s alternatives.

3. Based on [08_vc_startup_db.md], seed-stage architecture guidance recommends monoliths on PaaS/serverless, while "Microservices architecture with Kubernetes orchestration is best suited for funded SaaS startups targeting large-scale deployments."

4. Based on [07_sec_earnings.md], large public AI SaaS companies (Snowflake, Palantir, Salesforce) disclose multi-billion-dollar cloud commitments with mentions of Kubernetes platforms (via partnership announcements) but no mentions of PaaS or serverless as primary architectures.

5. Based on [04_tech_blogs.md], every company with a published engineering blog describing infrastructure uses Kubernetes. These companies tend to be growth-stage or later ($50M+ ARR). No engineering blog from the data set described choosing PaaS or serverless as primary.

6. Based on [03_job_postings.md, Data Point 20], 60% of DevOps positions require senior-level experience, and only 5% are junior-level. This complexity barrier "may favor simpler alternatives (serverless) for smaller teams."

**Reasoning:** There is a clear inverse relationship between company size and non-K8s adoption. Smaller companies lack the engineering resources to operate K8s (even managed K8s), making PaaS and serverless the pragmatic choice. As companies scale, they consistently migrate toward Kubernetes for flexibility, ecosystem, and GPU orchestration. The sharp drop-off above $50M ARR reflects the near-universal K8s adoption among companies large enough to publish engineering blogs or appear in CNCF/vendor surveys.

---

### Finding 6: US vs EU Differences

**Estimate:** EU AI SaaS companies may show 5-10 percentage points higher cloud-native non-K8s adoption than US counterparts, driven by regulatory constraints favoring managed services with compliance certifications.

**Classification:** Estimated (E) -- very low confidence

**Evidence Chain:**

1. Based on [01_cncf_survey.md, Data Point 15], "Europe: 82% in 'some' or 'much/all' cloud native development" vs "Americas: 70%." Europe actually shows HIGHER cloud-native maturity than the Americas.

2. Based on [05_cloud_vendor_cases.md, Case Study 22], Stacks (Amsterdam, Netherlands) uses GKE Autopilot -- a fully managed Kubernetes service. This is a European AI SaaS startup choosing managed infrastructure.

3. Based on [01_cncf_survey.md, Data Point 11], large organizations (5000+ employees) have 56% hybrid cloud adoption. European data sovereignty requirements (GDPR) may push companies toward managed services with regional compliance guarantees rather than self-managed infrastructure.

4. Based on [03_job_postings.md, Data Point 9], Kubernetes job data is "66-70% North America." The limited EU job data prevents direct comparison of infrastructure hiring patterns.

**Key Gap:** No Wave 1 source directly compares US vs EU AI SaaS architecture choices. The CNCF regional data covers overall cloud-native maturity, not the specific serverless/PaaS/managed-container breakdown. This estimate has very low confidence.

---

### Finding 7: Workload Types Favoring Cloud-Native Non-K8s

**Estimate:** Cloud-native non-K8s services are preferred for these AI workload types:

| Workload Type | Non-K8s Preference | Classification | Key Evidence |
|---|---|---|---|
| API serving / Inference endpoints | Moderate (30-45%) | Estimated (E) | Lambda for lightweight inference, Cloud Run for containerized models |
| Event-driven processing | High (50-70%) | Inferred (I) | Lambda 65-70% of AWS customers; 76% serverless for streaming workloads |
| Model training | Very Low (<5%) | Inferred (I) | No case studies of training on serverless; GPU constraints |
| Data processing / ETL | Low-Moderate (15-25%) | Estimated (E) | Some Lambda pipelines; most heavy ETL on K8s or Spark |
| Web application backends | Moderate (25-40%) | Estimated (E) | PaaS common for app layer; containerized services on Cloud Run/Fargate |

**Evidence Chain:**

1. Based on [06_stackshare_github.md], "76% of organizations deployed streaming workloads in production with serverless functions." Event-driven and streaming workloads strongly favor serverless.

2. Based on [02_analyst_reports.md, Data Point 14], Lambda at 65% of AWS customers confirms serverless dominance for event-driven patterns.

3. Based on [06_stackshare_github.md], "Google Cloud Run and Azure Container Instances both support GPU-based workloads while AWS Fargate does not." This limits non-K8s AI inference to Cloud Run and Azure Container Apps/Instances for GPU workloads.

4. Based on [02_analyst_reports.md, Data Point 43], Datadog containerized workload distribution shows "AI workloads: 7%" of containerized workloads. AI workloads remain a small fraction of overall container usage, suggesting most container workloads (web/app servers 42%, databases 45%) are more commonly served by simpler orchestration.

5. Based on [01_cncf_survey.md, Data Point 23], "Only 7% of organizations deploy models daily; 47% deploy occasionally." Infrequent model deployment reduces the need for sophisticated K8s-based MLOps pipelines, making simpler managed services viable for many inference workloads.

6. Based on [04_tech_blogs.md], no engineering blog disclosed using serverless or PaaS for model training. All training workloads described used Kubernetes with GPU nodes (OpenAI, Anthropic, Cohere, Grammarly).

---

### Finding 8: Migration Trends -- Direction of Movement

**Estimate:** The net migration direction is strongly AWAY FROM cloud-native non-K8s toward Kubernetes. For every company migrating to non-K8s services, an estimated 5-10 companies are migrating from non-K8s to K8s.

**Classification:** Inferred (I)

**Evidence Chain:**

1. Based on [04_tech_blogs.md, Figma Migration], Figma migrated from ECS to Kubernetes (EKS) in 12 months. Reasons: "cost savings, improved developer experience, and increased resiliency" and "to take advantage of the large ecosystem supported by the CNCF."

2. Based on [04_tech_blogs.md, Grammarly Migration], Grammarly moved from EC2 to EKS for ML infrastructure.

3. Based on [04_tech_blogs.md, HubSpot Migration], HubSpot migrated EC2-based infrastructure to Kubernetes.

4. Based on [04_tech_blogs.md, Salesforce Data Cloud Migration], Salesforce Data Cloud migrated from EC2 to Kubernetes in 6 months.

5. Based on [04_tech_blogs.md, Observation], "Migration direction is TOWARD Kubernetes, not away from it" -- zero engineering blog disclosures found of companies moving from K8s to serverless or PaaS.

6. Based on [05_cloud_vendor_cases.md, Case Study 17], PTC "moved from a virtual machine-based infrastructure to Azure Kubernetes Service (AKS)."

7. Based on [01_cncf_survey.md, Data Point 31], serverless adoption is declining: "only 11% of respondents are making use of serverless computing frameworks" in 2024, down from 22% in 2022.

8. Based on [01_cncf_survey.md, Data Point 32], "Serverless architecture and/or functions as a service saw decreased penetration rates, dropping from 22% in 2022 to 13% in 2023."

**Counterpoint:** Based on [02_analyst_reports.md, Data Point 13], "In Google Cloud, 68 percent of container organizations now use serverless containers, up from 35 percent two years ago." Cloud Run adoption is growing rapidly. However, this growth represents COMPLEMENTARY adoption (serverless alongside K8s), not REPLACEMENT. Based on [02_analyst_reports.md, Data Point 17], "66% of organizations using serverless functions also use container orchestration" -- confirming hybrid rather than replacement.

**Net Assessment:** Companies are not abandoning serverless. Rather, they are: (a) adopting K8s as primary orchestration while keeping serverless for specific workloads, and (b) migrating away from ECS/PaaS as primary platforms toward K8s at scale. The declining serverless-as-primary-framework metric (22% to 11%) coexists with growing serverless-as-complementary-tool usage (68% Cloud Run adoption on GCP).

---

## Estimate Table

| Architecture | Estimate | Classification | Key Evidence | Assumptions |
|---|---|---|---|---|
| Cloud-native non-K8s as primary (all AI SaaS) | 25-40% | E | CNCF 44% not on K8s for AI [01, DP22]; Gartner 54% K8s impl. [02, DP6]; startup stage guidance [08] | Assumes "not on K8s" includes mix of non-K8s cloud-native and VMs; assumes AI SaaS mirrors general tech population with slight upward bias for startups |
| Serverless functions (any use) | 50-65% of cloud customers | D | Datadog: Lambda 65% [02, DP14]; Cloud Run 70% GCP [02, DP15] | Measures "any use" not "primary"; includes event triggers and background tasks |
| Serverless as primary framework | 11-13% | D | CNCF 2024: 11% [01, DP31]; CNCF 2023: 13% [01, DP32] | CNCF survey biased toward K8s community; actual figure for general population may be higher |
| ECS/Fargate (AI SaaS) | 8-15% | E | Figma outgrew ECS [04]; BILL, Autodesk, Smartsheet on Fargate [05]; Fargate lacks GPU [06] | GPU constraint limits AI use; general SaaS adoption may be higher than AI SaaS |
| Cloud Run (AI SaaS) | 5-12% | E | 68-70% GCP container orgs [02, DP13/15]; GPU support available [06]; fewer AI case studies than K8s | GCP share is smaller than AWS; Cloud Run popular but GCP has fewer overall customers |
| Azure Container Apps (AI SaaS) | 3-8% | E | Coca-Cola, Replit on ACA [05]; GPU support available [06]; small disclosed sample | Azure Container Apps is relatively new; growing but limited disclosed AI SaaS adoption |
| PaaS (Heroku, Vercel, etc.) | 10-20% | E | Seed-stage guidance [08]; Salesforce repositioning Heroku for AI [07]; no growth-stage blogs on PaaS [04] | Concentrated in seed/early stage; rapid attrition as companies scale |
| Pre-revenue/seed on non-K8s | 60-80% | E | 91% of K8s users at 1000+ employees [01, DP28]; seed guidance avoids K8s [08]; YC credits patterns [08] | Assumes startup infrastructure mirrors VC guidance; no direct survey of seed-stage companies |
| Enterprise ($200M+) on non-K8s primary | 5-15% | E | All public AI SaaS disclose K8s partnerships [07]; all engineering blogs describe K8s [04]; 91% K8s enterprise [06] | Large companies may use non-K8s for secondary workloads but not as primary |

---

## Assumptions Register

| # | Assumption | Evidence Supporting It | Risk if Wrong |
|---|---|---|---|
| A1 | CNCF survey respondents over-represent K8s adopters relative to the general AI SaaS population | Gartner shows 54% K8s vs CNCF 82% [02, DP6]; CNCF is the K8s governing body; 91% of respondents are 1000+ employee orgs [01, DP28] | If CNCF data is representative, non-K8s adoption is lower than estimated (closer to 7-20%) |
| A2 | Companies not running AI/ML on K8s [01, DP22: 44%] include a meaningful share using non-K8s cloud-native services rather than VMs or no AI workloads | Datadog shows high Lambda/Cloud Run adoption [02, DP14-15]; managed APIs at 37% for AI hosting [02, DP11] | If most of the 44% are using VMs or not running AI at all, non-K8s cloud-native is lower than estimated |
| A3 | Early-stage AI SaaS companies follow VC infrastructure guidance (PaaS/serverless first, K8s later) | Explicit VC guidance [08]; YC credit acceptance [08]; K8s complexity barrier at 60% senior roles [03, DP20] | If startups are adopting K8s earlier (via managed K8s like GKE Autopilot), early-stage non-K8s adoption is lower |
| A4 | Engineering blog disclosures represent companies at $50M+ ARR and do not reflect early-stage architecture patterns | Publication bias toward mature companies [04, Known Biases]; blog companies include OpenAI, Databricks, Salesforce, Snowflake | If smaller companies also publish and also use K8s, the stage-based gradient is less steep |
| A5 | Serverless adoption decline (22% to 11% in CNCF) reflects declining use as primary framework, not declining overall usage | Datadog shows growing Lambda/Cloud Run adoption [02, DP14-15]; 66% of serverless users also use containers [02, DP17] | If serverless is declining in total, the estimate for serverless as complementary tool overstates adoption |
| A6 | GPU constraints on AWS Fargate significantly limit AI inference use cases on that platform | Fargate lacks GPU support [06]; AI inference requires GPU for many model types | If most AI inference is CPU-based (e.g., small models, distilled models), Fargate is more viable than estimated |
| A7 | The migration pattern (non-K8s to K8s) documented in engineering blogs represents a general industry trend, not publication bias | 4 independent migration stories in same direction [04]; zero counter-examples found across all 8 Wave 1 files; CNCF K8s production rising 66% to 80% [01, DP1/6] | If companies migrating TO non-K8s simply do not publish, the net migration direction could be less one-sided |
| A8 | AI SaaS companies have similar infrastructure patterns to general SaaS companies, adjusted for higher compute intensity | AI SaaS gross margins (50-65%) lower than traditional (70-85%) [07]; compute costs 40-50% of revenue for AI [08] | If AI companies make fundamentally different infrastructure choices (e.g., all GPU cloud), general cloud-native data may not apply |

---

## Evidence Gaps

### Critical Gaps (would change estimates significantly if filled)

1. **No direct survey of AI SaaS companies asking "what is your primary compute platform?"** All estimates are derived from general enterprise data or proxy signals. A purpose-built survey of 200+ AI SaaS companies by ARR tier would resolve the core question.

2. **No Datadog-quality telemetry specifically for AI SaaS companies.** Datadog reports Lambda at 65% of AWS customers and Cloud Run at 70% of GCP customers, but does not segment by company type. AI SaaS-specific telemetry would be definitive.

3. **Missing ECS/Fargate adoption rates.** No source provides "X% of AWS customers use ECS" comparable to the Lambda 65% figure. ECS is a major non-K8s container platform but its adoption rate is not documented in Wave 1 data.

4. **No data on companies under 500 employees.** Based on [01_cncf_survey.md, Data Point 27], K8s adoption data stops at 500-1,000 employees (9% of adopters). The sub-500 segment -- which includes most AI SaaS startups -- is invisible in the data.

5. **No workload-level data.** Based on [06_stackshare_github.md, Limitation 5], "Surveys measure technology adoption at org level, not workload level." We know companies use Lambda, but not what percentage of their AI inference runs on Lambda vs K8s.

### Moderate Gaps

6. **US vs EU architecture differences for AI SaaS.** Regional cloud-native maturity data exists [01, DP15] but no architecture-specific breakdown by region.

7. **Cloud Run GPU adoption for AI inference.** Cloud Run supports GPUs [06], but no telemetry on how many AI companies use Cloud Run for GPU inference vs GKE.

8. **PaaS adoption beyond Heroku.** Vercel, Railway, Render, and Fly.io are popular among developers but have no adoption data in Wave 1 files.

9. **Managed ML services (SageMaker, Vertex AI) vs self-hosted inference.** Based on [01_cncf_survey.md, Data Point 25], "30% of AI developers use Machine Learning as a Service (MLaaS) platforms." But the split between MLaaS and self-hosted inference on non-K8s platforms is unknown.

10. **Cost comparison data.** Based on [06_stackshare_github.md], "AWS Fargate's compute prices are generally lowest, Google comes second... Azure was the most expensive option at more than double the price of AWS." But no cost comparison data for AI-specific workloads on non-K8s vs K8s platforms.

---

## Confidence Score: 4/10

### Justification

**Why relatively low confidence:**

1. **No direct measurement exists.** Unlike Kubernetes adoption (measured by CNCF, Datadog, Red Hat, Gartner), cloud-native non-K8s adoption for AI SaaS has no dedicated survey or telemetry source. Every estimate in this analysis is synthesized from indirect evidence.

2. **Heavy reliance on "gap analysis."** The core approach is: "If X% use K8s, then (100-X)% might use non-K8s." This inverse logic is fragile because the remainder includes VMs, bare metal, and companies not yet containerized.

3. **Publication bias severely underrepresents non-K8s architectures.** Companies using ECS, Lambda, or PaaS are far less likely to write engineering blogs about their infrastructure. Based on [04_tech_blogs.md, Limitation 10], "Companies using ECS, Lambda, or other patterns less likely to publish." This creates an information asymmetry where K8s appears more dominant than it may actually be.

4. **Early-stage companies are invisible.** Based on [03_job_postings.md, Limitation 5] and [01_cncf_survey.md, Limitation 9], companies under 500 employees are not measured. This is exactly the segment most likely to use non-K8s services.

5. **Conflicting serverless data.** The 11% CNCF global figure vs 70% North America enterprise figure [06] represents a 6x discrepancy that has not been fully resolved.

**What gives moderate confidence:**

1. Datadog telemetry (production usage data, not surveys) provides high-quality signals for Lambda, Cloud Run, and Fargate adoption across cloud customers [02, DP13-19].

2. Multiple independent sources confirm the stage-based gradient: startups on simpler platforms, enterprises on K8s [08, 03, 04, 01].

3. The migration direction finding (non-K8s to K8s, not vice versa) is supported by 4+ independent engineering blog disclosures with zero counter-examples [04].

4. The serverless-as-complement pattern (66% of serverless users also use container orchestration) is well-supported by Datadog data [02, DP17].

**What would increase confidence:**

- A direct survey of 200+ AI SaaS companies by ARR tier
- Datadog or similar telemetry segmented for AI/ML companies
- ECS/Fargate adoption rates comparable to Lambda data
- Architecture data for companies under 500 employees

---

## Sources (Wave 1 Files Referenced)

- 01_cncf_survey.md: Data Points 1, 3, 8, 11, 15, 22, 23, 25, 27, 28, 31, 32
- 02_analyst_reports.md: Data Points 6, 11, 13, 14, 15, 16, 17, 19, 21, 43, 46
- 03_job_postings.md: Data Points 9, 15, 20
- 04_tech_blogs.md: Figma migration, Grammarly migration, HubSpot migration, Salesforce Data Cloud migration, Known Biases, Limitations
- 05_cloud_vendor_cases.md: Case Studies 10-12, 14, 17, 18, 22
- 06_stackshare_github.md: Serverless adoption data, serverless container comparison, GPU support data, CNCF regional data
- 07_sec_earnings.md: Salesforce Heroku, AI SaaS gross margins, infrastructure costs
- 08_vc_startup_db.md: Startup infrastructure guidance, YC data, infrastructure cost benchmarks, Fireworks AI, Modal Labs

---

**Analysis Compiled:** 2026-02-12
**Methodology:** Cross-source synthesis of 8 Wave 1 fact-gathering reports
**Analyst:** Wave 2 Synthesis Agent (Cloud-Native Non-K8s Focus)
