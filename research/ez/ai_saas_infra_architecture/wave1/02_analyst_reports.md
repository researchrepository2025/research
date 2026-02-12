# Analyst Reports: Cloud Infrastructure & Kubernetes Adoption
## Research Wave 1 - Raw Data Extract

**Research Question:** What percentage of AI SaaS companies use (a) cloud-native non-K8s managed services (serverless, PaaS, ECS/Fargate, Cloud Run), (b) managed Kubernetes (AKS/EKS/GKE), and (c) self-managed open Kubernetes?

**Date Compiled:** 2026-02-12

---

## Executive Summary

Available analyst data from 2024-2025 provides strong baseline metrics for overall Kubernetes and serverless adoption but lacks AI SaaS-specific segmentation. Managed Kubernetes dominates cloud deployments at 73%, while serverless container platforms show rapid growth (68% in Google Cloud). Kubernetes production usage reached 82% among container users. Critical gap: no source directly segments AI SaaS companies from general enterprise data.

---

## Data Points

### CATEGORY: Managed vs Self-Managed Kubernetes Split

#### [DATA POINT 1]
**Source:** Dynatrace, Kubernetes in the Wild Report 2023
**Date:** 2023
**URL:** https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/
**Finding:** "Most Kubernetes clusters in the cloud (73%) are built on top of managed distributions from the hyperscalers like AWS Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), or Google Kubernetes Engine (GKE). The remaining 27% of clusters are self-managed by the customer on cloud virtual machines."
**Relevance:** Direct answer to managed vs self-managed split in cloud environments
**Segment Applicability:** General cloud deployments, not AI SaaS-specific

#### [DATA POINT 2]
**Source:** Multiple analyst sources aggregated
**Date:** 2025
**URL:** https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/
**Finding:** "Managed Kubernetes has captured approximately 63% of Kubernetes deployments, with the remaining share being self-managed"
**Relevance:** Overall managed/self-managed split across all environments (not just cloud)
**Segment Applicability:** All Kubernetes deployments including on-premises and cloud

#### [DATA POINT 3]
**Source:** CNCF Annual Survey 2024
**Date:** 2024
**URL:** https://www.cncf.io/reports/cncf-annual-survey-2024/
**Finding:** "Survey respondents were evenly split between on-premises data centers and public clouds (both 59%), with both skewing heavily toward self-managed instances"
**Relevance:** Shows self-managed preference persists even in public cloud
**Segment Applicability:** CNCF community respondents (likely more technical/DIY-oriented than typical enterprise)

---

### CATEGORY: Kubernetes Production Adoption Rates

#### [DATA POINT 4]
**Source:** CNCF Annual Cloud Native Survey 2025
**Date:** 2026-01-20 (announcement date)
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
**Finding:** "82% of container users now run Kubernetes in production (up from 66% in 2023)"
**Relevance:** Shows Kubernetes as dominant container orchestration platform
**Segment Applicability:** Container users broadly, not limited to AI/SaaS

#### [DATA POINT 5]
**Source:** CNCF Annual Cloud Native Survey 2025
**Date:** 2026-01-20
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
**Finding:** "93% of organizations either running Kubernetes in production or piloting it in test environments"
**Relevance:** Near-universal Kubernetes adoption or evaluation
**Segment Applicability:** All organizations using containers

#### [DATA POINT 6]
**Source:** Gartner (cited in multiple sources)
**Date:** 2024-2025
**URL:** https://www.gartner.com/en/documents/5405263
**Finding:** "Kubernetes has joined the mainstream, with 54% of survey respondents having a full or partial implementation"
**Relevance:** Lower adoption rate than CNCF (54% vs 82%) suggests CNCF respondents skew more cloud-native
**Segment Applicability:** Broader enterprise base than CNCF survey

#### [DATA POINT 7]
**Source:** Red Hat Kubernetes Adoption Survey
**Date:** 2024
**URL:** https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview
**Finding:** "70% of IT leaders surveyed work for organizations that use Kubernetes"
**Relevance:** IT leadership perspective on K8s adoption
**Segment Applicability:** Enterprise IT organizations

---

### CATEGORY: AI/ML Workload Deployment on Kubernetes

#### [DATA POINT 8]
**Source:** CNCF Annual Cloud Native Survey 2025
**Date:** 2026-01-20
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
**Finding:** "66% of organizations hosting generative AI models use Kubernetes to manage some or all of their inference workloads"
**Relevance:** Direct data on AI workload deployment on Kubernetes
**Segment Applicability:** Organizations hosting generative AI models

#### [DATA POINT 9]
**Source:** CNCF Annual Cloud Native Survey 2025
**Date:** 2026-01-20
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
**Finding:** "Over 90% of surveyed teams expect their Kubernetes AI workloads to increase within 12 months"
**Relevance:** Forward-looking trend for AI on Kubernetes
**Segment Applicability:** Teams currently running AI workloads

#### [DATA POINT 10]
**Source:** CNCF Annual Cloud Native Survey 2025
**Date:** 2026-01-20
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
**Finding:** "44% report they do not yet run AI/ML workloads on Kubernetes"
**Relevance:** Significant portion not using K8s for AI yet
**Segment Applicability:** All survey respondents

#### [DATA POINT 11]
**Source:** CNCF Annual Cloud Native Survey 2025
**Date:** 2026-01-20
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
**Finding:** "Hosting splits show 37% using managed APIs, 25% self-hosting, and 13% at the edge in the context of AI/ML model hosting specifically"
**Relevance:** Shows AI/ML workloads favor managed APIs over self-hosting
**Segment Applicability:** AI/ML model hosting specifically

#### [DATA POINT 12]
**Source:** Gartner (cited in multiple sources)
**Date:** 2024-2025
**URL:** https://azure.microsoft.com/en-us/blog/microsoft-is-a-leader-in-the-2025-gartner-magic-quadrant-for-container-management/
**Finding:** "By 2027, Gartner predicts that more than 75% of all AI/ML deployments will use container technology as the underlying compute environment, a major increase from fewer than 50% in 2024"
**Relevance:** Forecast showing rapid containerization of AI/ML workloads
**Segment Applicability:** All AI/ML deployments

---

### CATEGORY: Serverless Container Adoption

#### [DATA POINT 13]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "In Google Cloud, 68 percent of container organizations now use serverless containers, up from 35 percent two years ago"
**Relevance:** Rapid growth in serverless container adoption on GCP
**Segment Applicability:** Google Cloud container users

#### [DATA POINT 14]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/
**Finding:** "AWS Lambda: 65% of AWS customers"
**Relevance:** Serverless function adoption on AWS
**Segment Applicability:** AWS customers

#### [DATA POINT 15]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/
**Finding:** "Google Cloud Run: 70% of Google Cloud customers"
**Relevance:** Serverless container adoption on GCP
**Segment Applicability:** Google Cloud customers

#### [DATA POINT 16]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/
**Finding:** "Azure App Service: 56% of Azure customers"
**Relevance:** PaaS adoption on Azure
**Segment Applicability:** Azure customers

#### [DATA POINT 17]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/
**Finding:** "66% of organizations using serverless functions also use container orchestration"
**Relevance:** Shows hybrid approach (serverless + containers) is common
**Segment Applicability:** Organizations using serverless

#### [DATA POINT 18]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "In Google Cloud, 66 percent of all serverless organizations now use container-based serverless workloads (Cloud Run and 2nd gen Cloud Functions)"
**Relevance:** Containerized serverless preference on GCP
**Segment Applicability:** Google Cloud serverless users

#### [DATA POINT 19]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "AWS increased to 26 percent of serverless organizations running fully managed container workloads with containerized Lambda functions"
**Relevance:** Growing containerized serverless on AWS
**Segment Applicability:** AWS serverless users

#### [DATA POINT 20]
**Source:** Multiple industry sources
**Date:** 2025
**URL:** https://www.cloudzero.com/blog/cloud-computing-statistics/
**Finding:** "Over 50% of organizations will treat serverless as the standard by the end of 2025"
**Relevance:** Serverless becoming default deployment model
**Segment Applicability:** General enterprise

#### [DATA POINT 21]
**Source:** Multiple industry sources
**Date:** 2025
**URL:** https://atmosly.com/blog/why-kubernetes-is-the-best-infrastructure-for-saas-companies-in-2025
**Finding:** "Over 70% of AWS users now rely on Lambda"
**Relevance:** High Lambda adoption among AWS users
**Segment Applicability:** AWS customers

---

### CATEGORY: Container Adoption Forecasts

#### [DATA POINT 22]
**Source:** Gartner
**Date:** 2023-2029 forecast
**URL:** https://www.gartner.com/en/documents/5405263
**Finding:** "By 2029, 35% of all enterprise applications will run in containers, an increase from less than 15% in 2023"
**Relevance:** Long-term containerization forecast
**Segment Applicability:** All enterprise applications

#### [DATA POINT 23]
**Source:** Gartner
**Date:** 2023-2027 forecast
**URL:** https://azure.microsoft.com/en-us/blog/microsoft-is-a-leader-in-the-2025-gartner-magic-quadrant-for-container-management/
**Finding:** "By 2027, Gartner predicts that over 90% of G2000 organizations will utilize container management tools for their hybrid environments, a significant increase from less than 20% in 2023"
**Relevance:** Near-universal container management adoption forecast for large enterprises
**Segment Applicability:** G2000 organizations

#### [DATA POINT 24]
**Source:** Multiple sources
**Date:** 2025
**URL:** https://atmosly.com/blog/why-kubernetes-is-the-best-infrastructure-for-saas-companies-in-2025
**Finding:** "Container usage in production environments is forecast to rise to 75% of enterprises by 2025"
**Relevance:** High enterprise containerization forecast
**Segment Applicability:** Enterprises

---

### CATEGORY: Cloud-Native Adoption Maturity

#### [DATA POINT 25]
**Source:** CNCF Annual Survey
**Date:** 2024-2025
**URL:** https://thenewstack.io/5-tech-predictions-for-2026-from-ai-inference-to-kubernetes/
**Finding:** "Cloud native adoption has four levels: Explorers (8%), Adopters (32%), Practitioners (34%), and Innovators (25%)"
**Relevance:** Maturity distribution of cloud-native adoption
**Segment Applicability:** Cloud-native technology users

#### [DATA POINT 26]
**Source:** CNCF Annual Cloud Native Survey 2025
**Date:** 2026-01-20
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
**Finding:** "59% of organizations report that 'much' or 'nearly all' of their development and deployment is now cloud native"
**Relevance:** Majority have deep cloud-native adoption
**Segment Applicability:** Organizations using cloud-native techniques

#### [DATA POINT 27]
**Source:** HashiCorp State of Cloud Strategy Survey 2024
**Date:** 2024-2025
**URL:** https://www.hashicorp.com/en/state-of-the-cloud
**Finding:** "Out of nearly 1,200 respondents around the world, only 8% qualified as highly mature"
**Relevance:** Cloud maturity remains low despite high adoption
**Segment Applicability:** Global enterprise IT leaders

---

### CATEGORY: Hybrid and Multi-Cloud Deployment

#### [DATA POINT 28]
**Source:** Flexera State of the Cloud Report 2025
**Date:** 2025
**URL:** https://info.flexera.com/CM-REPORT-State-of-the-Cloud
**Finding:** "70% of survey respondents are embracing hybrid cloud strategies, with data and apps in at least one public and one private cloud"
**Relevance:** Hybrid cloud dominance
**Segment Applicability:** Enterprises and SMBs

#### [DATA POINT 29]
**Source:** Flexera State of the Cloud Report 2025
**Date:** 2025
**URL:** https://info.flexera.com/CM-REPORT-State-of-the-Cloud
**Finding:** "On average, organizations are using 2.4 public cloud providers"
**Relevance:** Multi-cloud is standard practice
**Segment Applicability:** All organizations

#### [DATA POINT 30]
**Source:** Multiple sources
**Date:** 2025
**URL:** https://thenewstack.io/5-tech-predictions-for-2026-from-ai-inference-to-kubernetes/
**Finding:** "65% of organizations run Kubernetes in multiple environments for portability"
**Relevance:** K8s used for multi-environment portability
**Segment Applicability:** Kubernetes users

---

### CATEGORY: Cloud Service Model Revenue Distribution

#### [DATA POINT 31]
**Source:** Multiple analyst sources
**Date:** 2025
**URL:** https://www.cloudzero.com/blog/cloud-computing-statistics/
**Finding:** "SaaS is expected to remain the dominant cloud service model, with revenues reaching approximately $390.5 billion, surpassing the projected revenues for Platform as a Service (PaaS) at $208.64 billion and Infrastructure as a Service (IaaS) at $180 billion"
**Relevance:** Revenue breakdown by service model
**Segment Applicability:** Public cloud market

#### [DATA POINT 32]
**Source:** Multiple analyst sources
**Date:** 2025
**URL:** https://www.cloudzero.com/blog/cloud-computing-statistics/
**Finding:** "Platform-as-a-service (PaaS) and infrastructure-as-a-service (IaaS) will each capture nearly 20% of public cloud spending"
**Relevance:** IaaS and PaaS each ~20% of spending
**Segment Applicability:** Public cloud spending

#### [DATA POINT 33]
**Source:** Multiple analyst sources
**Date:** 2025
**URL:** https://www.cloudzero.com/blog/cloud-computing-statistics/
**Finding:** "IaaS has the second highest growth rate among all public cloud services segments in 2025 at 32.8%, after DaaS at 30.7%, while PaaS has a growth rate of 28.6%, and SaaS has the lowest growth rate at 14.8%"
**Relevance:** Growth rate comparison across service models
**Segment Applicability:** Public cloud market

#### [DATA POINT 34]
**Source:** Omdia
**Date:** 2025
**URL:** https://omdia.tech.informa.com/pr/2025/dec/global-cloud-infrastructure-spending-hits-102point6-billion-dollars-up-25percent-in-q3-2025
**Finding:** "Omdia defines cloud infrastructure services as the sum of bare metal as a service (BMaaS), infrastructure-as-a-service (IaaS), platform-as-a-service (PaaS) and container-as-a-service (CaaS) and serverless that are hosted by third-party providers"
**Relevance:** CaaS and serverless are counted within infrastructure services
**Segment Applicability:** Cloud infrastructure market definition

---

### CATEGORY: Cloud Budget and Spending

#### [DATA POINT 35]
**Source:** Flexera State of the Cloud Report 2025
**Date:** 2025
**URL:** https://info.flexera.com/CM-REPORT-State-of-the-Cloud
**Finding:** "Cloud spend expected to increase by 28% in the coming year"
**Relevance:** Continued cloud investment growth
**Segment Applicability:** All cloud users

#### [DATA POINT 36]
**Source:** Flexera State of the Cloud Report 2025
**Date:** 2025
**URL:** https://info.flexera.com/CM-REPORT-State-of-the-Cloud
**Finding:** "Organizations are exceeding budgets by 17%"
**Relevance:** Cloud cost overruns common
**Segment Applicability:** All cloud users

#### [DATA POINT 37]
**Source:** SQ Magazine (cited)
**Date:** 2025
**URL:** https://americanchase.com/future-of-serverless-computing/
**Finding:** "23% of cloud budgets in 2025 are directed toward cloud-native development, including serverless computing"
**Relevance:** Cloud-native development budget allocation
**Segment Applicability:** Cloud budget allocation

---

### CATEGORY: Enterprise Company Size and K8s Adoption

#### [DATA POINT 38]
**Source:** Red Hat
**Date:** 2024
**URL:** https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview
**Finding:** "Kubernetes adoption is highest among larger organizations, with 34% of Kubernetes users in companies with over 20,000 employees and another 34% from companies with 1,000–5,000 employees"
**Relevance:** Company size correlation with K8s adoption
**Segment Applicability:** Kubernetes users by company size

---

### CATEGORY: Workload Characteristics

#### [DATA POINT 39]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "Almost two-thirds of Kubernetes containers have an uptime under 10 minutes, and about one-third finish running in under 1 minute"
**Relevance:** K8s used heavily for short-lived workloads (jobs/batch)
**Segment Applicability:** Kubernetes workloads

#### [DATA POINT 40]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "Across Azure Container Apps, Google Cloud Run, Amazon ECS Fargate, AWS Lambda, and Kubernetes, most workloads use less than half of their requested memory and less than 25% of their requested CPU"
**Relevance:** Significant resource over-provisioning across all platforms
**Segment Applicability:** All containerized and serverless platforms

---

### CATEGORY: Kubernetes Autoscaling

#### [DATA POINT 41]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "64% of Kubernetes organizations use Horizontal Pod Autoscaler (up from ~55% in Q1 2024)"
**Relevance:** Growing HPA adoption for auto-scaling
**Segment Applicability:** Kubernetes organizations

#### [DATA POINT 42]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "80% scale on CPU or memory; only 20% use custom metrics"
**Relevance:** Basic metrics still dominate autoscaling decisions
**Segment Applicability:** Kubernetes HPA users

---

### CATEGORY: Containerized Workload Types

#### [DATA POINT 43]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "Databases: 45%, Web/app servers: 42%, CI/CD tools: 27%, AI workloads: 7%"
**Relevance:** AI workloads are emerging but still small portion of containerized workloads
**Segment Applicability:** Containerized workload distribution

---

### CATEGORY: GPU and AI Infrastructure

#### [DATA POINT 44]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "GPU adoption increased from ~4.5% to just over 6% of organizations (Oct 2023 - Oct 2025)"
**Relevance:** Slow but steady GPU adoption growth
**Segment Applicability:** All organizations in Datadog customer base

#### [DATA POINT 45]
**Source:** Datadog State of Containers and Serverless 2025
**Date:** 2025
**URL:** https://www.datadoghq.com/state-of-containers-and-serverless/
**Finding:** "GPU instance hours grew roughly threefold over two years, though still under 3% of total CPU instance hours"
**Relevance:** GPU usage growing faster than adoption rate
**Segment Applicability:** Cloud infrastructure users

---

### CATEGORY: AI/ML PaaS Adoption

#### [DATA POINT 46]
**Source:** Flexera State of the Cloud Report 2025
**Date:** 2025
**URL:** https://info.flexera.com/CM-REPORT-State-of-the-Cloud
**Finding:** "Seventy-nine percent of organizations are already using or experimenting with AI and machine learning (ML) PaaS services"
**Relevance:** High AI/ML PaaS adoption
**Segment Applicability:** All organizations

---

## Preliminary Estimates

### Direct Estimates (Supported by Data)

**Managed Kubernetes vs Self-Managed Split (Cloud Environments):**
- Managed K8s: 73% (Dynatrace 2023)
- Self-managed K8s: 27% (Dynatrace 2023)

**Managed Kubernetes vs Self-Managed Split (All Environments):**
- Managed K8s: 63% (Multiple sources 2025)
- Self-managed K8s: 37% (Multiple sources 2025)

**Serverless Adoption by Cloud Provider:**
- AWS Lambda: 65-70% of AWS customers
- Google Cloud Run: 68-70% of GCP customers
- Azure App Service: 56% of Azure customers

**AI/ML Workload Hosting:**
- Managed APIs: 37%
- Self-hosting: 25%
- Edge: 13%
- Not specified/other: 25%

**Kubernetes for AI Inference:**
- Using K8s for some/all AI inference: 66%
- Not using K8s for AI/ML: 44%

### Indirect Estimates (Inferred, Requires Validation)

**IMPORTANT:** No analyst report provides a direct breakdown for "AI SaaS companies" specifically. All data is for general enterprises, cloud-native organizations, or container users broadly.

**Hypothetical AI SaaS Infrastructure Distribution (UNVALIDATED):**
Based on available data, a rough estimate for AI SaaS companies might be:
- (a) Cloud-native non-K8s managed services: 30-40% (serverless, PaaS, Fargate, Cloud Run)
- (b) Managed Kubernetes: 40-50% (EKS/AKS/GKE)
- (c) Self-managed Kubernetes: 15-25%

**Confidence in this estimate:** 2/10 - This is speculative synthesis, not supported by direct data.

---

## Data Quality Assessment

### Completeness
**Score:** 6/10

**Strengths:**
- Strong data on overall Kubernetes adoption (82% production usage)
- Clear managed vs self-managed split for cloud K8s (73%/27%)
- Good serverless adoption metrics by cloud provider
- AI/ML workload data from CNCF 2025 survey

**Gaps:**
- No AI SaaS-specific segmentation in any source
- Limited breakdowns by company size for serverless
- Missing direct comparison of PaaS vs CaaS vs self-managed K8s
- No data on ECS/Fargate vs Cloud Run vs AKS Container Apps adoption rates
- Limited longitudinal data (most sources are single snapshots)

### Recency
**Score:** 8/10

**Strengths:**
- CNCF 2025 survey published Jan 2026 (very recent)
- Datadog 2025 report covers Oct 2025 data
- Flexera 2025 State of Cloud report available
- Gartner 2025 Magic Quadrant published Aug 2025

**Limitations:**
- Some foundational data (Dynatrace) from 2023
- AI SaaS segment may be moving faster than general enterprise data

### Sample Size and Methodology
**Score:** 7/10

**Strengths:**
- Datadog: tens of thousands of customers (actual usage telemetry, not survey)
- CNCF survey: broad cloud-native community participation
- Flexera: 759 global cloud decision-makers
- HashiCorp: nearly 1,200 global respondents

**Limitations:**
- CNCF respondents likely skew more technical/cloud-native than typical enterprise
- Datadog customer base may not represent all market segments
- Survey-based data subject to self-reporting bias

### Known Biases
**Score:** 6/10

**Identified Biases:**
- CNCF survey respondents are cloud-native practitioners (82% K8s adoption vs 54% Gartner)
- Datadog telemetry only covers Datadog customers
- Gartner/Forrester reports often gated behind paywalls (limited public data)
- "AI SaaS companies" not distinguished from general SaaS or AI companies
- Geographic bias: most surveys US/Europe-heavy
- Company size bias: larger enterprises overrepresented in some surveys

---

## Limitations — What This Source CANNOT Tell Us

1. **AI SaaS Segmentation:** No source differentiates "AI SaaS companies" from general SaaS, AI companies, or enterprises. All data is aggregated.

2. **Infrastructure Architecture Mix:** Data shows adoption rates for each technology but not how companies *combine* them (e.g., "what % use K8s AND serverless" vs "K8s INSTEAD OF serverless").

3. **Workload Distribution:** We know 66% use K8s for AI inference, but not what % of their AI workloads run on K8s vs serverless vs other platforms.

4. **Company Stage:** No breakdown by startup vs growth vs mature SaaS companies. Infrastructure choices likely vary significantly by stage.

5. **Vertical Industry:** Limited data on infrastructure choices by industry vertical (fintech, healthcare, etc.).

6. **Regional Differences:** Most data is global aggregates; regional infrastructure patterns unclear.

7. **Cost-Driven vs Performance-Driven Choices:** Data shows what companies use but not why they chose that approach.

8. **Migration Trends:** Limited data on companies moving between infrastructure models (e.g., K8s to serverless or vice versa).

9. **Actual vs Intended Use:** Some data (like "79% using/experimenting with AI PaaS") conflates production use with experimentation.

10. **Private Cloud PaaS:** Focus is on public cloud managed services; private cloud K8s platforms (OpenShift, Rancher, etc.) less represented.

---

## Confidence Score: 7/10

### Justification

**High Confidence (8-9/10) For:**
- Overall Kubernetes production adoption: 82% (CNCF 2025)
- Managed vs self-managed K8s in cloud: 73%/27% (Dynatrace)
- Serverless adoption by major cloud providers (Datadog telemetry)
- AI/ML workload K8s adoption: 66% (CNCF 2025)

**Medium Confidence (6-7/10) For:**
- General enterprise K8s adoption: 54-70% range (variance across sources)
- Managed K8s overall: 63% (source aggregation methodology unclear)
- Cloud-native maturity distribution (survey bias concerns)

**Low Confidence (3-5/10) For:**
- AI SaaS-specific infrastructure choices (no direct data)
- PaaS vs CaaS vs self-managed distribution (overlapping definitions)
- Company size and stage correlations (limited data)

**Very Low Confidence (1-2/10) For:**
- Hypothetical AI SaaS infrastructure distribution estimate (purely speculative)
- Migration trends and directional momentum
- Regional and industry vertical variations

### Overall Assessment

The analyst data provides a **strong foundation** for understanding general Kubernetes and serverless adoption patterns but **cannot directly answer** the specific research question about AI SaaS company infrastructure choices. Additional primary research (surveys, interviews with AI SaaS CTOs/infrastructure leads) would be required to segment this population accurately.

The 7/10 confidence score reflects:
- High-quality data sources (Datadog telemetry, CNCF surveys, Gartner/Forrester)
- Recent and comprehensive coverage of container/K8s/serverless landscape
- Critical gap: no AI SaaS segmentation in any source
- Methodology variations across sources create some uncertainty
- Strong directional indicators but insufficient precision for the specific target segment

---

## Recommended Next Steps

1. **Primary Research:** Survey or interview 50-100 AI SaaS infrastructure leaders about their deployment choices
2. **Case Study Analysis:** Analyze infrastructure architectures of 20-30 publicly known AI SaaS companies
3. **Job Posting Analysis:** Scan AI SaaS company job postings for infrastructure technology mentions
4. **VC Portfolio Analysis:** Review infrastructure choices across AI SaaS companies in major VC portfolios
5. **Cloud Provider Customer Case Studies:** Analyze AWS/GCP/Azure case studies filtering for AI SaaS customers
6. **GitHub/StackShare Analysis:** Review infrastructure stacks of open-source AI SaaS projects and StackShare profiles

---

## Sources Reference List

1. [Gartner - Cloud Survey Reveals Divergent Kubernetes Adoption Trends](https://www.gartner.com/en/documents/5405263)
2. [Microsoft - Leader in 2025 Gartner Magic Quadrant for Container Management](https://azure.microsoft.com/en-us/blog/microsoft-is-a-leader-in-the-2025-gartner-magic-quadrant-for-container-management/)
3. [Forrester - Serverless Development Platforms Landscape Q1 2025](https://www.forrester.com/report/the-serverless-development-platforms-landscape-q1-2025/RES181964)
4. [AWS - Leader in 2025 Forrester Wave: Serverless Development Platforms](https://aws.amazon.com/blogs/compute/aws-named-a-leader-in-the-2025-forrester-wave-serverless-development-platforms/)
5. [Flexera - State of the Cloud Report 2025](https://info.flexera.com/CM-REPORT-State-of-the-Cloud)
6. [Datadog - State of Containers and Serverless 2025](https://www.datadoghq.com/state-of-containers-and-serverless/)
7. [Datadog - Key Learnings from Containers and Serverless Study](https://www.datadoghq.com/blog/containers-and-serverless-2025-study-learnings/)
8. [HashiCorp - 2024 State of Cloud Strategy Survey](https://www.hashicorp.com/en/state-of-the-cloud)
9. [HashiCorp - 2025 Cloud Complexity Report](https://www.hashicorp.com/en/cloud-complexity-report)
10. [CNCF - Kubernetes Production Use Hits 82% in 2025 Survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)
11. [CNCF - Annual Survey 2024](https://www.cncf.io/reports/cncf-annual-survey-2024/)
12. [The New Stack - 5 Tech Predictions for 2026](https://thenewstack.io/5-tech-predictions-for-2026-from-ai-inference-to-kubernetes/)
13. [Red Hat - Kubernetes Adoption Security Market Trends](https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview)
14. [Tigera - 36 Kubernetes Statistics for 2025](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)
15. [Dynatrace - Kubernetes in the Wild 2023](https://www.dynatrace.com/news/blog/kubernetes-in-the-wild-2023/)
16. [CloudZero - 90+ Cloud Computing Statistics 2025](https://www.cloudzero.com/blog/cloud-computing-statistics/)
17. [Omdia - Global Cloud Infrastructure Spending Q3 2025](https://omdia.tech.informa.com/pr/2025/dec/global-cloud-infrastructure-spending-hits-102point6-billion-dollars-up-25percent-in-q3-2025)
18. [Atmosly - Why Kubernetes is Best for SaaS Companies 2025](https://atmosly.com/blog/why-kubernetes-is-the-best-infrastructure-for-saas-companies-in-2025)
19. [American Chase - Future of Serverless Computing 2026](https://americanchase.com/future-of-serverless-computing/)
20. [Forrester - Announcing AI Infrastructure Solutions Wave Q4 2025](https://www.forrester.com/blogs/announcing-the-forrester-wave-ai-infrastructure-solutions-q4-2025/)

---

**Document Version:** 1.0
**Compiled By:** Research Agent (Claude Code)
**Methodology:** Web search aggregation of public analyst reports and industry surveys
**Data Sources:** 20+ analyst reports and industry surveys from 2023-2026
**Known Limitations:** No direct segmentation for AI SaaS companies in any source analyzed
