# Infrastructure Technology Signals: Job Posting Analysis
## AI SaaS Company Hiring Patterns as Architecture Proxy

**Research Question:** What infrastructure technologies do AI SaaS companies hire for?

**Signal Type:** PROXY SIGNAL - Job postings indicate technology usage patterns but are not direct architecture evidence

**Date Compiled:** 2026-02-12

---

## Executive Summary

Job posting analysis from Q1-Q2 2025 reveals Kubernetes as the dominant infrastructure skill demand in cloud-native organizations. Among 4,850+ qualified DevOps/Platform Engineering job postings, Docker appears in 59-60% of listings and Kubernetes in 28-100% depending on dataset filtering. Managed Kubernetes services (EKS/AKS/GKE) represent 73% of cloud Kubernetes deployments. Platform Engineering role growth (8-11% of infrastructure jobs) serves as a proxy signal for Kubernetes investment. Limited direct data exists comparing Kubernetes vs serverless hiring ratios; most analyses focus on Kubernetes-filtered datasets.

---

## Data Points

### [DATA POINT 1] Kubernetes Job Market Volume
**Source:** kube.careers
**Date:** Q1 2025, Q2 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q1, https://kube.careers/state-of-kubernetes-jobs-2025-q2

**Finding:**
- Q1 2025: "436 job descriptions" analyzed from 1,200+ postings requiring Kubernetes experience
- Q2 2025: "386 job descriptions" analyzed from 1,200+ postings requiring Kubernetes experience

**Proxy Signal:**
Job volume indicates sustained enterprise demand for Kubernetes skills across hundreds of companies

**Relevance:** High - Direct measurement of Kubernetes-specific hiring demand

**Segment Applicability:** Not segmented by company size in this dataset

---

### [DATA POINT 2] DevOps Technology Stack Demand
**Source:** Brokee / DevOps Statistics Compilation
**Date:** 2025
**URL:** https://brokee.io/blog/essential-devops-statistics-and-trends-for-hiring-in-2024

**Finding:**
"The most in-demand skills in the DevOps tech stack include Docker (42.77%), Kubernetes (28.02%), AWS (12.1%), Linux (9.17%), and Bash (4.44%)"

**Proxy Signal:**
- Docker mentions (42.77%) indicate containerization as baseline
- Kubernetes mentions (28.02%) suggest ~1 in 4 DevOps jobs require orchestration
- Ratio implies Docker-without-K8s scenarios exist (serverless containers, simpler deployments)

**Relevance:** High - Shows relative demand across container technologies

**Segment Applicability:** Not specified by company size

---

### [DATA POINT 3] Kubernetes Job Role Distribution
**Source:** devopscube.com
**Date:** 2025 (analyzing 2024 data)
**URL:** https://devopscube.com/kubernetes-and-devops-job-market/

**Finding:**
Analysis of "4,850 qualified job postings" from 25,000+ total listings:
- "Software Engineers: 41% (2,033 roles)"
- "DevOps Engineers: 10% (499 roles)"
- "Platform Engineers: 8.35% (405 roles)"
- "Site Reliability Engineers: 6% (291 roles)"
- "DevSecOps Engineers: 4.24% (206 roles)"

Container & Orchestration Skills Demand:
- "Docker: 59%"
- "Kubernetes: 100% (all analyzed jobs)"
- "Helm: 9%"

**Proxy Signal:**
- Platform Engineer growth (8.35% of infrastructure roles) signals K8s platform investment
- 100% K8s presence reflects dataset pre-filtered for Kubernetes jobs
- Docker at 59% (not 100%) suggests some K8s jobs assume Docker knowledge

**Relevance:** Medium - Dataset is Kubernetes-filtered, not representative of all infrastructure hiring

**Segment Applicability:** Not specified

---

### [DATA POINT 4] Managed Kubernetes Dominance
**Source:** kube.careers analysis
**Date:** 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q1

**Finding:**
"73% of cloud Kubernetes clusters are built on managed distributions from hyperscalers like AWS EKS, Azure AKS, or GKE"

**Proxy Signal:**
- 73% managed K8s = companies hiring prefer cloud-managed over self-hosted
- 27% self-managed/other indicates non-trivial DIY K8s investment
- Does NOT specify EKS vs AKS vs GKE breakdown

**Relevance:** High - Direct indicator of managed vs self-managed preferences

**Segment Applicability:** Not specified by company size

---

### [DATA POINT 5] CI/CD Tool Demand in Kubernetes Jobs
**Source:** kube.careers
**Date:** Q1 2025, Q2 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q1, https://kube.careers/state-of-kubernetes-jobs-2025-q2

**Finding:**
Q1 2025:
- "Jenkins: 38%"
- "GitLab: 25%"
- "GitHub Actions: 12%"

Q2 2025:
- "GitLab: 31%"
- "Jenkins: 29%"
- "GitHub Actions: 16%"
- "Azure DevOps: 6%"

**Proxy Signal:**
- GitLab growth (25% → 31%) may indicate integrated DevOps platform preference
- Azure DevOps at 6% suggests minority AKS-specific hiring
- GitHub Actions growth (12% → 16%) signals cloud-native CI/CD adoption

**Relevance:** Low-Medium - Indicates tooling ecosystem, not architecture choice

**Segment Applicability:** Not specified

---

### [DATA POINT 6] Stack Overflow Developer Survey - Container Adoption
**Source:** Stack Overflow 2025 Developer Survey
**Date:** 2025
**URL:** https://survey.stackoverflow.co/2025/technology

**Finding:**
- "Docker continues to be the most used container technology (71.1%)"
- "Kubernetes is used by 28.5% of respondents"
- "Docker has moved from a popular tool to a near-universal one, experiencing a +17 percentage point jump in usage from 2024 to 2025 (71%)"

**Proxy Signal:**
- Docker at 71% vs Kubernetes at 28.5% = ~2.5x gap
- Indicates Docker-without-K8s scenarios (local dev, serverless containers, simpler deployments)
- K8s at 28.5% suggests significant but minority adoption among all developers

**Relevance:** Medium - Broader developer survey, not filtered for infrastructure roles

**Segment Applicability:** Not specified by company type

---

### [DATA POINT 7] CNCF Kubernetes Adoption by Company Size
**Source:** CNCF / Tigera compilation
**Date:** 2025
**URL:** https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/

**Finding:**
- "34% of Kubernetes users are in companies with over 20,000 employees"
- "another 34% come from companies with 1,000–5,000 employees"
- "23% of Kubernetes users work in companies with 5,000–20,000 staff"
- "only 9% of adopters are companies with 500–1,000 employees"

**Proxy Signal:**
- 68% of K8s users in companies with 1,000-20,000+ employees
- Only 9% in 500-1,000 employee range = smaller companies less likely to use K8s
- Suggests K8s adoption correlates with company scale

**Relevance:** High - Direct company size segmentation

**Segment Applicability:**
- Enterprise (1,000+): 91% of K8s adopters
- SMB (500-1,000): 9% of K8s adopters
- Startups (<500): Not measured in this dataset

---

### [DATA POINT 8] Platform Engineering Role Growth
**Source:** kube.careers, devopscube.com
**Date:** Q1 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q1

**Finding:**
- Q1 2025: "Platform Engineer: 11%"
- 2024 average: "Platform Engineers: 8.35% (405 roles)"

**Proxy Signal:**
- Platform Engineering growth (8.35% → 11%) = +32% YoY increase
- Platform Engineer roles are proxy for K8s platform/IDP investment
- Companies hiring Platform Engineers likely building internal K8s platforms

**Relevance:** High - Role creation indicates infrastructure investment type

**Segment Applicability:** Not specified, but role typically appears in mid-to-large companies

---

### [DATA POINT 9] Remote Work Patterns in K8s Jobs
**Source:** kube.careers
**Date:** Q1-Q2 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q2

**Finding:**
- "Remote jobs averaged 44.69% from Q1 to Q4 2023, declined to an average of 37% for 2024, and averaged 41% in the first two quarters of 2025"
- "Hybrid jobs escalated rapidly after the end of 2023, averaging 28.11% from Q1 2024 to Q2 2025"
- Q2 2025: "Remote (any form): 68.36%"

**Proxy Signal:**
- K8s jobs more remote-friendly (68% allow remote) than average tech jobs
- May indicate cloud-native companies are more distributed
- Not directly relevant to architecture choice

**Relevance:** Low - Cultural signal, not technical architecture

**Segment Applicability:** Not specified

---

### [DATA POINT 10] Programming Language Demand in K8s Jobs
**Source:** kube.careers
**Date:** Q1-Q2 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q1, https://kube.careers/state-of-kubernetes-jobs-2025-q2

**Finding:**
Q1 2025:
- "Python: 62%"
- "Go: 32%"
- "Java: 37%"
- "Javascript: 36%"

Q2 2025:
- "Python: 62% (up from 57% in 2024)"
- "Go: 36%"
- "Java: 34%"
- "JavaScript: 39%"

**Proxy Signal:**
- Python dominance (62%) suggests data/ML workloads on K8s
- Go growth (32% → 36%) aligns with cloud-native tooling (K8s ecosystem is Go-based)
- Not directly indicative of serverless vs K8s choice

**Relevance:** Low-Medium - Language choice influenced by workload type, not just infrastructure

**Segment Applicability:** Not specified

---

### [DATA POINT 11] AI/ML Workload Deployment on Kubernetes
**Source:** CNCF / Portworx Voice of Kubernetes Experts 2025 Report
**Date:** 2025
**URL:** https://www.cncf.io/blog/2025/08/02/what-500-experts-revealed-about-kubernetes-adoption-and-workloads/

**Finding:**
Survey of 500+ participants from companies with 500+ employees:
- "AI/ML workloads: 60%"
- "Databases: 69%"
- "98% of enterprises say they run data-heavy workloads in their cloud native environments"
- "58% run mission-critical applications in containers"

**Proxy Signal:**
- 60% running AI/ML on K8s suggests enterprise AI companies likely use K8s
- Does NOT indicate what % of AI workloads are on K8s vs serverless
- Sample limited to 500+ employee companies

**Relevance:** High - Directly relevant to AI company infrastructure choices

**Segment Applicability:** Enterprise only (500+ employees)

---

### [DATA POINT 12] DevOps Market Growth and Company Size Distribution
**Source:** Brokee, Mordor Intelligence
**Date:** 2025
**URL:** https://brokee.io/blog/essential-devops-statistics-and-trends-for-hiring-in-2024

**Finding:**
- "22% working in large organizations with over 10,000 employees"
- "By organization size, large enterprises led with 64.05% revenue share in 2025"
- "SMEs post the highest expected CAGR of 21.2% between 2026-2031"
- "The DevOps market is expected to grow from USD 16.13 billion in 2025 to USD 19.57 billion in 2026"

**Proxy Signal:**
- Large enterprises (10,000+ employees) = 22% of DevOps workforce but 64% of market revenue
- SME growth rate (21.2% CAGR) > enterprise suggests smaller companies adopting DevOps later
- Does NOT specify K8s vs serverless preferences by size

**Relevance:** Medium - Company size correlates with infrastructure complexity

**Segment Applicability:**
- Enterprise: 64% market share, slower growth
- SME: 36% market share, 21.2% CAGR

---

### [DATA POINT 13] Cloud Native Adoption Rates
**Source:** CNCF Annual Survey 2025
**Date:** 2025-2026
**URL:** https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/

**Finding:**
- "98% of surveyed organizations reported that they have adopted cloud native techniques"
- "Kubernetes is no longer an emerging technology but the established, reliable foundation for modern enterprise infrastructure"
- "80% of organizations running it in production, up from 66% in 2023"
- "93% of organizations using, piloting, or evaluating it"

**Proxy Signal:**
- 80% production K8s usage among surveyed orgs (likely CNCF-affiliated, biased sample)
- 98% "cloud native" ≠ 80% K8s production = 18% using other cloud-native (serverless, managed services)
- Sample bias: CNCF survey respondents likely more K8s-oriented than general market

**Relevance:** Medium - High adoption but biased sample

**Segment Applicability:** Not specified; likely enterprise-heavy

---

### [DATA POINT 14] LinkedIn Job Posting Volume
**Source:** kube.careers / LinkedIn data
**Date:** 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q1

**Finding:**
- "There are 110,000+ Kubernetes-related job listings on LinkedIn as of 2025"

**Proxy Signal:**
- 110,000+ K8s jobs globally indicates large-scale adoption
- Does NOT provide comparison to serverless job volumes
- LinkedIn dataset may have duplicates, expired postings

**Relevance:** Medium - Volume indicator but lacks comparison baseline

**Segment Applicability:** Not specified

---

### [DATA POINT 15] Serverless and Cloud-Native Technology Mentions
**Source:** Refonte Learning / Cloud Engineering Skills 2025
**Date:** 2025
**URL:** https://www.refontelearning.com/blog/cloud-engineering-in-2025-key-skills-employers-demand

**Finding:**
"Lambda, ECS, EKS, Fargate, and microservices will dominate cloud-native development — making related skill sets 'must-haves' for future architects and engineers"

**Proxy Signal:**
- Serverless (Lambda, Fargate) and K8s (EKS) mentioned together as complementary
- Does NOT provide ratio of Lambda vs EKS job postings
- Suggests hybrid architectures common

**Relevance:** Low - Qualitative statement without data

**Segment Applicability:** Not specified

---

### [DATA POINT 16] Salary Differentials by Role
**Source:** kube.careers, devopscube.com
**Date:** Q1-Q2 2025
**URL:** https://kube.careers/state-of-kubernetes-jobs-2025-q1, https://devopscube.com/kubernetes-and-devops-job-market/

**Finding:**
Kubernetes-specific roles:
- Q1 2025 Global Average: "$158,450 (minimum $133,221, maximum $183,680)"
- Q2 2025 Global Average: "$166,836 (min: $138,406 | max: $195,266)"
- North America Q2 2025: "$170,568 average"

DevOps broader market (2024):
- "DevOps Engineers: Overall average: $141,645"
- "Platform Engineers: $170,657 (20% higher than DevOps)"

**Proxy Signal:**
- K8s-specific roles command 17% premium over general DevOps ($166k vs $141k)
- Platform Engineers earn more than DevOps Engineers = market values K8s platform skills
- Not directly indicative of K8s vs serverless adoption

**Relevance:** Low-Medium - Salary premium indicates skill scarcity/value

**Segment Applicability:** Not specified

---

### [DATA POINT 17] AI Skills Growth and Infrastructure Demand
**Source:** Burning Glass Institute / Lightcast, LinkedIn Economic Graph
**Date:** 2025
**URL:** https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23, https://sustainabilitymag.com/news/demand-for-green-skills-is-outstripping-supply-twice-over

**Finding:**
- "Among AI talent specifically, skills like 'operational efficiency' grew by 579% year-on-year, while 'maintenance and repair' shot up by 190%"
- "Energy management became the fastest-growing green skill category globally, with a 17.4% increase over the past year, which reflects surges in demand for AI infrastructure, energy efficiency measures"
- "Only 14% of leaders say they have the right talent to meet their AI goals, with 61% citing shortages in managing specialized infrastructure and 53% now facing deficits in data science roles"

**Proxy Signal:**
- "Specialized infrastructure" shortage (61%) suggests AI companies need infrastructure talent
- "Operational efficiency" and "energy management" growth may indicate GPU cluster/K8s operations
- Does NOT specify K8s vs serverless infrastructure skills

**Relevance:** Medium - AI infrastructure hiring is broad category

**Segment Applicability:** AI companies specifically

---

### [DATA POINT 18] MLOps Role Growth
**Source:** People In AI, The New Stack
**Date:** 2025
**URL:** https://www.peopleinai.com/blog/the-job-market-for-mlops-engineers-in-2025, https://thenewstack.io/tech-hiring-in-2026-the-rise-of-the-specialist/

**Finding:**
- "MLOps engineering has transformed from a niche specialization into one of the fastest-growing roles in tech, with LinkedIn identifying MLOps as a standout with 9.8× growth in five years"
- "AI-related roles growing 3x faster than the average job"

**Proxy Signal:**
- MLOps growth (9.8x in 5 years) indicates AI infrastructure investment
- MLOps roles typically involve K8s for model deployment (but also serverless options exist)
- Does NOT specify infrastructure preferences

**Relevance:** Medium - MLOps roles use infrastructure but choice not specified

**Segment Applicability:** AI/ML companies

---

### [DATA POINT 19] Hybrid Work Mode Trends
**Source:** devopscube.com
**Date:** 2025 (analyzing 2024 data)
**URL:** https://devopscube.com/kubernetes-and-devops-job-market/

**Finding:**
DevOps Roles Work Mode Distribution:
- "In-office required: 39.4%"
- "Remote (within country): 33.1%"
- "Hybrid: 27.3%"
- "Remote (timezone flexible): 0.2%"

Platform Engineers:
- "Platform Engineers most remote-friendly: 41% remote positions"

**Proxy Signal:**
- Platform Engineers (K8s-heavy roles) have highest remote % (41%)
- May indicate cloud-native companies are more distributed
- Not directly relevant to architecture choice

**Relevance:** Low - Cultural signal

**Segment Applicability:** Not specified

---

### [DATA POINT 20] Experience Level Requirements
**Source:** devopscube.com
**Date:** 2025 (analyzing 2024 data)
**URL:** https://devopscube.com/kubernetes-and-devops-job-market/

**Finding:**
DevOps positions breakdown:
- "Senior-level: 60%"
- "Lead-level: 15%"
- "Mid-level: 11%"
- "Principal-level: 7.2%"
- "Junior-level: 5%"

**Proxy Signal:**
- 60% senior-level indicates K8s/DevOps is not entry-level skill
- 5% junior-level suggests limited training pipeline for K8s
- Complexity barrier may favor simpler alternatives (serverless) for smaller teams

**Relevance:** Low-Medium - Skill complexity indicator

**Segment Applicability:** Not specified

---

## Preliminary Estimates

### [ESTIMATE 1] Kubernetes vs Docker-Only Adoption (INDIRECT)

**Data Source:** Stack Overflow 2025, Brokee DevOps Skills
**Calculation:**
- Docker usage: 71% (Stack Overflow) / 42.77% (DevOps jobs)
- Kubernetes usage: 28.5% (Stack Overflow) / 28.02% (DevOps jobs)
- Ratio: ~2.5x more Docker-only than K8s+Docker

**Estimate Label:** INDIRECT (derived from general developer surveys, not AI SaaS specific)

**Limitation:** Does NOT account for serverless container services (Fargate, Cloud Run) which use Docker without K8s

---

### [ESTIMATE 2] Managed Kubernetes Market Share (DIRECT)

**Data Source:** kube.careers
**Statistic:** "73% of cloud Kubernetes clusters are built on managed distributions from hyperscalers like AWS EKS, Azure AKS, or GKE"

**Estimate Label:** DIRECT

**Limitation:** Does NOT break down EKS vs AKS vs GKE percentages

---

### [ESTIMATE 3] Enterprise vs SMB Kubernetes Adoption (DIRECT)

**Data Source:** CNCF/Tigera
**Calculation:**
- Enterprise (1,000+ employees): 91% of K8s adopters
- SMB (500-1,000 employees): 9% of K8s adopters

**Estimate Label:** DIRECT

**Limitation:** Sample may be biased toward CNCF member organizations (K8s-heavy)

---

### [ESTIMATE 4] AI/ML Workload K8s Adoption (DIRECT)

**Data Source:** CNCF/Portworx Survey
**Statistic:** "60% of enterprises (500+ employees) run AI/ML workloads in containers"

**Estimate Label:** DIRECT (for enterprise only)

**Limitation:**
- Does NOT specify K8s vs other container platforms
- Enterprise-only sample (500+ employees)
- Does NOT measure what % of total AI workloads this represents

---

### [ESTIMATE 5] Platform Engineering as K8s Proxy (INDIRECT)

**Data Source:** kube.careers, devopscube.com
**Calculation:**
- Platform Engineer role growth: 8.35% (2024) → 11% (Q1 2025) = +32% YoY
- Assumption: Platform Engineers primarily work with K8s/IDP

**Estimate Label:** INDIRECT (role growth as proxy for technology adoption)

**Limitation:** Platform Engineering may also involve serverless platforms, not exclusively K8s

---

## Data Quality Assessment

### Completeness: 6/10
- **Available:** K8s job volumes, role distribution, salary data, managed K8s dominance, company size segmentation
- **Missing:** Direct K8s vs serverless job posting ratio, EKS vs AKS vs GKE breakdown, AI SaaS company-specific data (most data is general tech market)

### Recency: 8/10
- **Strength:** Q1-Q2 2025 data from kube.careers, Stack Overflow 2025 survey, CNCF 2025-2026 reports
- **Weakness:** Some analyses reference 2024 data aggregated in 2025 reports

### Sample Size: 7/10
- **Strong datasets:**
  - kube.careers: 436-386 K8s-specific jobs per quarter
  - devopscube.com: 4,850 qualified DevOps job postings
  - CNCF: 500+ enterprise survey respondents
  - LinkedIn: 110,000+ K8s job listings
- **Limitation:** Most datasets pre-filtered for K8s, not representative of all infrastructure hiring

### Known Biases:
1. **K8s-filtered datasets:** Most job analyses focus on K8s-required positions, not comparing K8s vs serverless volumes
2. **CNCF survey bias:** CNCF respondents likely more K8s-oriented than general market
3. **Enterprise bias:** Company size data skews toward larger organizations (500+ employees)
4. **Geographic bias:** 66-70% North America in K8s job data
5. **No AI SaaS segmentation:** Data covers general tech market, not specifically AI SaaS companies

---

## Limitations — What This Source CANNOT Tell Us

### [LIMITATION 1] Direct K8s vs Serverless Hiring Ratio
**Gap:** No dataset provides head-to-head comparison of job postings requiring "Kubernetes" vs "Lambda/Fargate/Cloud Run"

**Why it matters:** Cannot directly calculate what % of infrastructure jobs are K8s vs serverless

**Workaround:** Stack Overflow data (Docker 71% vs K8s 28.5%) suggests ~2.5x gap, but this includes non-infrastructure developers

---

### [LIMITATION 2] EKS vs AKS vs GKE Breakdown
**Gap:** While "73% managed K8s" is known, no dataset breaks down AWS EKS vs Azure AKS vs Google GKE percentages

**Why it matters:** Cannot infer cloud provider preferences from hiring data

**Workaround:** Other data sources (CNCF surveys, market share reports) may provide this breakdown

---

### [LIMITATION 3] AI SaaS Company-Specific Infrastructure Hiring
**Gap:** No dataset segments job postings by company type (AI SaaS vs general tech vs enterprise)

**Why it matters:** AI SaaS companies may have different infrastructure preferences than traditional SaaS

**Workaround:** MLOps role growth (9.8x in 5 years) suggests AI companies hiring infrastructure, but tech stack not specified

---

### [LIMITATION 4] Hybrid Architecture Signals
**Gap:** Job postings mention "Lambda, ECS, EKS, Fargate" together but don't specify if companies use K8s AND serverless or one vs the other

**Why it matters:** Cannot determine if companies are choosing K8s OR serverless, or using both

**Workaround:** Qualitative analysis of job descriptions may reveal hybrid patterns

---

### [LIMITATION 5] Startup Infrastructure Hiring (<500 employees)
**Gap:** CNCF data stops at 500-1,000 employees (9% of K8s users); no data for <500 employee startups

**Why it matters:** AI SaaS startups may have different infrastructure choices than established enterprises

**Workaround:** Infer from SME growth rate (21.2% CAGR) that smaller companies adopting DevOps later, likely with simpler tools

---

### [LIMITATION 6] Temporal Trends
**Gap:** Limited year-over-year comparison data for K8s vs serverless hiring

**Why it matters:** Cannot determine if K8s demand is growing/stable/declining relative to serverless

**Workaround:** MLOps growth (9.8x), Platform Engineering growth (+32% YoY) suggest K8s-related roles increasing

---

### [LIMITATION 7] Geographic Segmentation
**Gap:** 66-70% of K8s job data is North America; limited visibility into EMEA/APAC patterns

**Why it matters:** Infrastructure preferences may vary by region (data sovereignty, cloud availability)

**Workaround:** Europe salary data exists (€91k average) but tech stack preferences not detailed

---

## Confidence Score: 6/10

### Justification:

**Strengths (+):**
- Large sample sizes (4,850-110,000+ job postings analyzed)
- Recent data (Q1-Q2 2025, Stack Overflow 2025)
- Multiple independent sources (kube.careers, devopscube.com, CNCF, Stack Overflow)
- Direct measurement of technology mentions in job postings
- Company size segmentation available (CNCF data)

**Weaknesses (-):**
- Most datasets pre-filtered for Kubernetes jobs (not representative of all infrastructure hiring)
- No direct K8s vs serverless comparison
- No AI SaaS company segmentation (data covers general tech market)
- CNCF survey bias (K8s-oriented respondents)
- Missing EKS/AKS/GKE breakdown
- Limited startup data (<500 employees)

**Overall Assessment:**
Job posting data provides STRONG signal for Kubernetes demand but WEAK signal for comparative adoption vs serverless. Data confirms K8s is dominant in enterprise (1,000+ employees) and among infrastructure specialists (DevOps/Platform/SRE roles), but cannot definitively measure what % of AI SaaS companies choose K8s vs serverless. Best used in combination with other data sources (architecture surveys, market share data, vendor revenue).

---

## Sources

- [Tech Job Market & Hiring Trends in 2026 - Qubit Labs](https://qubit-labs.com/tech-hiring-trends/)
- [DevOps Job Market Trends 2025 - Scale.jobs](https://scale.jobs/blog/devops-job-market-trends)
- [Essential DevOps Statistics 2025 - Brokee](https://brokee.io/blog/essential-devops-statistics-and-trends-for-hiring-in-2024)
- [Top 47 DevOps Statistics 2026 - Spacelift](https://spacelift.io/blog/devops-statistics)
- [The Burning Glass Institute](https://www.burningglassinstitute.org/research)
- [New Lightcast Report: AI Skills - Lightcast](https://lightcast.io/resources/blog/beyond-the-buzz-press-release-2025-07-23)
- [State of AI Infrastructure Report 2025 - Flexential](https://www.flexential.com/resources/report/2025-state-ai-infrastructure)
- [Top 10 High-Paying AWS Jobs 2025 - K21 Academy](https://k21academy.com/aws-cloud/top-10-high-paying-aws-jobs-in-2026-aws-salary/)
- [Cloud Engineering 2025 Key Skills - Refonte Learning](https://www.refontelearning.com/blog/cloud-engineering-in-2025-key-skills-employers-demand)
- [Tech Hiring in 2026: Rise of the Specialist - The New Stack](https://thenewstack.io/tech-hiring-in-2026-the-rise-of-the-specialist/)
- [The DevOps Job Market in 2025 - Prepare.sh](https://prepare.sh/articles/the-devops-job-market-in-2025-trends-tools-and-how-to-stand-out)
- [Top DevOps Companies Hiring 2025 - DevOps Projects HQ](https://devopsprojectshq.com/role/top-devops-companies-2025/)
- [MLOps Engineers 2025 - People In AI](https://www.peopleinai.com/blog/the-job-market-for-mlops-engineers-in-2025)
- [AI Merging With Platform Engineering 2026 - The New Stack](https://thenewstack.io/in-2026-ai-is-merging-with-platform-engineering-are-you-ready/)
- [The State of Kubernetes Jobs 2025 Q1 - kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q1)
- [The State of Kubernetes Jobs 2025 Q2 - kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q2)
- [Kubernetes And DevOps Job Market 2025 - DevOpsCube](https://devopscube.com/kubernetes-and-devops-job-market/)
- [36 Kubernetes Statistics 2025 - Tigera](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)
- [Kubernetes Job Market Surges - The New Stack](https://thenewstack.io/kubernetes-job-market-surges-hybrid-roles-take-the-lead-with-160k-average-salary/)
- [2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/)
- [Stack Overflow 2025 Technology](https://survey.stackoverflow.co/2025/technology)
- [CNCF: What 500+ Experts Revealed About Kubernetes](https://www.cncf.io/blog/2025/08/02/what-500-experts-revealed-about-kubernetes-adoption-and-workloads/)
- [CNCF: Kubernetes as AI Operating System](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)
- [DevOps Job Market Report H2 2025 - DevOps Projects HQ](https://devopsprojectshq.com/role/devops-market-h2-2025/)
- [Green Skills Demand Growing - Sustainability Magazine](https://sustainabilitymag.com/news/demand-for-green-skills-is-outstripping-supply-twice-over)
- [Top Jobs to Watch 2025 - Lightcast](https://lightcast.io/resources/blog/top-jobs-to-watch-2025)
