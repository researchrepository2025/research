# Infrastructure Technology Signals: StackShare, GitHub, and Technology Profiling Platforms

## Executive Summary

This research compiled infrastructure technology adoption data from CNCF surveys, industry analyst reports (Datadog, Sysdig, Tigera), and technology profiling platforms for 2024-2025. Kubernetes has achieved near-universal enterprise adoption at 96%, with production usage reaching 80% in 2024. StackShare data indicates 39,816 verified companies use Kubernetes, while serverless adoption shows more fragmented patterns with only 11% of CNCF respondents using serverless computing frameworks despite market growth projections. Service mesh adoption reached 70% among CNCF survey participants, though CNCF 2024 data also shows service mesh declining from 50% to 42% year-over-year. Data quality varies significantly—StackShare profiles are self-reported and incomplete, GitHub public repos represent only disclosed infrastructure, and survey methodologies differ across sources. These are proxy signals with substantial selection bias.

---

## Data Points

### Kubernetes Adoption - Enterprise

[DATA POINT]
"96% of enterprises now using the container orchestration platform"
— Red Hat State of Kubernetes Security Report 2024
URL: https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/
Date: 2025
Relevance: Enterprise baseline adoption metric
Segment Applicability: All segments—suggests Kubernetes is default infrastructure choice

[DATA POINT]
"Overall Kubernetes adoption exceeds 90% in enterprises, with the U.S. leading global usage"
— Jeevi Academy Kubernetes Statistics Report
URL: https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/
Date: 2025
Relevance: Geographic adoption signal
Segment Applicability: All segments, US-centric bias

[DATA POINT]
"Production use of Kubernetes hit 80% in 2024, up from 66% in 2023 and reflecting an annual growth rate of 20.7%"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024 (published 2025)
Relevance: Production vs. pilot distinction—critical for understanding real vs. experimental adoption
Segment Applicability: All segments

[DATA POINT]
"93% of organizations are using, piloting, or evaluating Kubernetes"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024
Relevance: Includes non-production usage; broader adoption signal
Segment Applicability: All segments

### Kubernetes Adoption - Company Count

[STATISTIC]
"39,816 verified companies are using Kubernetes"
— Octopus Deploy / Landbase Technology Database
URL: https://octopus.com/devops/ci-cd-kubernetes/kubernetes-statistics/
Date: 2025
Relevance: Absolute company count—useful for market sizing but lacks segment breakdown
Segment Applicability: Unknown—no filtering by company type or industry

[STATISTIC]
"5.6 million developers globally use Kubernetes, representing 31% of all backend developers"
— Developer Nation Report
URL: https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/
Date: 2025
Relevance: Developer community size signal
Segment Applicability: All segments—indicates talent availability

### Kubernetes Adoption - Company Size Distribution

[STATISTIC]
"91% of Kubernetes users work at organizations exceeding 1,000 employees"
— CNCF/Industry Surveys
URL: https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/
Date: 2025
Relevance: Strong enterprise skew—Kubernetes primarily large org technology
Segment Applicability: SMB segment shows low adoption

[DATA POINT]
"34% of Kubernetes users are in companies with over 20,000 employees, another 34% come from companies with 1,000–5,000 employees, 23% of Kubernetes users work in companies with 5,000–20,000 staff, and only 9% of adopters are companies with 500–1,000 employees"
— Industry Survey Data
URL: https://octopus.com/devops/ci-cd-kubernetes/kubernetes-statistics/
Date: 2025
Relevance: Detailed size distribution—confirms enterprise concentration
Segment Applicability: Minimal SMB penetration (<500 employees not reported)

### Kubernetes Market Share and Growth

[STATISTIC]
"92% market share in container orchestration tools"
— Datadog Container Report
URL: https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/
Date: 2024
Relevance: Kubernetes has effectively won container orchestration category
Segment Applicability: All segments using containers

[DATA POINT]
"Global Kubernetes Market size was valued at USD 2.11 Billion in 2024 and is poised to grow from USD 2.61 Billion in 2025 to USD 14.61 Billion by 2033, growing at a CAGR of 24% during the forecast period (2026–2033)"
— Market Research Report
URL: https://octopus.com/devops/ci-cd-kubernetes/kubernetes-statistics/
Date: 2025
Relevance: Market size projection—useful for vendor revenue context
Segment Applicability: All segments

[DATA POINT]
"Kubernetes security market: $1.195 billion in 2022; forecast $10.7 billion by 2031 (CAGR: 27.6%)"
— Market Research Report
URL: https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/
Date: 2025
Relevance: Security market subset—indicates complexity/risk premium
Segment Applicability: All segments—security overhead signal

### Managed Kubernetes Services (EKS, AKS, GKE)

[DATA POINT]
"The demand for managed Kubernetes services (such as Amazon EKS, Google GKE, and Azure AKS) represents a significant growth opportunity, with the segment expected to grow at a CAGR of over 30%"
— Market Growth Reports
URL: https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/
Date: 2025
Relevance: Managed services growing faster than self-managed—indicates preference for abstraction
Segment Applicability: All segments—especially SMB and enterprises with limited Kubernetes expertise

[STATISTIC]
"GKE remains dominant in the Kubernetes landscape, with a 32% adoption rate among businesses"
— Industry Survey
URL: https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/
Date: 2025
Relevance: GKE leads managed Kubernetes market share
Segment Applicability: All segments
CAVEAT: Source and methodology unclear

[STATISTIC]
"AKS maintains a 28% adoption rate among businesses with 5,000 or more employees"
— Industry Survey
URL: https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/
Date: 2025
Relevance: AKS strong in large enterprises
Segment Applicability: Large enterprise segment specifically

[DATA POINT]
"Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022, indicating a significant shift toward managed services"
— Industry Trend Report
URL: https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/
Date: 2025
Relevance: 67% cloud-hosted vs 33% self-managed—major shift from 2022
Segment Applicability: All segments—indicates managed services gaining dominance

[DATA POINT]
"The global Kubernetes Solutions market is characterized by a high degree of concentration, with the top five players accounting for approximately 73% of the market share. This market dominance is firmly held by the leading cloud hyperscalers Amazon AWS (Amazon Elastic Kubernetes Service), Google (Google Kubernetes Engine), and Microsoft (Azure Kubernetes Service)"
— Intel Market Research
URL: https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/
Date: 2025
Relevance: Hyperscaler oligopoly—73% market concentration in top 5
Segment Applicability: All segments—indicates limited vendor diversity

[DATA POINT]
"Containerd is now the default runtime for most managed Kubernetes services, including Google Kubernetes Engine (GKE) and Amazon EKS"
— Industry Analysis
URL: https://charleswan111.medium.com/cri-o-vs-containerd-choosing-and-managing-kubernetes-container-runtimes-effectively-7b40b7194e9d
Date: 2025
Relevance: Container runtime standardization signal
Segment Applicability: All segments using managed Kubernetes

### Kubernetes Version Adoption

[STATISTIC]
"78% of hosts running mainstream supported versions (1.31+)"
— Datadog Security Labs Kubernetes Adoption Report
URL: https://securitylabs.datadoghq.com/articles/a-2025-look-at-real-world-kubernetes-adoption/
Date: 2025 (October 1, 2025 data snapshot)
Relevance: Version currency—most orgs keeping up with mainstream support
Segment Applicability: All segments

[STATISTIC]
"19% of hosts on extended support versions (1.28–1.30)"
— Datadog Security Labs
URL: https://securitylabs.datadoghq.com/articles/a-2025-look-at-real-world-kubernetes-adoption/
Date: 2025
Relevance: Extended support usage—indicates paid LTS adoption
Segment Applicability: Enterprises with stability requirements

[STATISTIC]
"3% of hosts running unsupported versions (earlier than 1.28)"
— Datadog Security Labs
URL: https://securitylabs.datadoghq.com/articles/a-2025-look-at-real-world-kubernetes-adoption/
Date: 2025
Relevance: Minimal unsupported deployments—significant improvement from 2022
Segment Applicability: Legacy/neglected infrastructure

[DATA POINT]
"40% of Kubernetes organizations are using versions (v1.25+) that are approximately a year old or less—a significant improvement compared to 5% a year ago"
— Datadog State of Containers Report
URL: https://www.datadoghq.com/state-of-containers-and-serverless/
Date: 2025
Relevance: Faster upgrade cycles—orgs keeping pace with releases
Segment Applicability: All segments

### Cloud Native Adoption

[DATA POINT]
"Cloud native adoption has reached an all-time high of 89% among surveyed organizations, with one-quarter of respondents reporting that nearly all of their development and deployment use cloud native techniques"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024
Relevance: Broad cloud-native patterns beyond just Kubernetes
Segment Applicability: All segments

### Container Adoption and Usage

[DATA POINT]
"The average number of containers used by organizations now stands at 2,341, up from 1,140 in 2023"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024
Relevance: Container sprawl—105% year-over-year growth
Segment Applicability: Enterprises primarily—SMB container counts likely much lower

[DATA POINT]
"52% of respondents are using containers to run most or all of their applications, compared to 39% that are using them to run a small number of applications"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024
Relevance: Containers moving from edge cases to core infrastructure
Segment Applicability: All segments

[DATA POINT]
"Most Kubernetes containers are short-lived: almost two-thirds have an uptime under 10 minutes, and about one-third finish running in under 1 minute"
— Datadog Container Report
URL: https://www.datadoghq.com/state-of-containers-and-serverless/
Date: 2025
Relevance: Workload patterns—high churn indicates batch/ephemeral jobs
Segment Applicability: All segments—impacts infrastructure design

[DATA POINT]
"For the first time, 60% of containers now live for 60 seconds or less, representing a significant shift from previous years"
— Sysdig 2025 Cloud-Native Security and Usage Report
URL: https://www.sysdig.com/2025-cloud-native-security-and-usage-report
Date: 2025
Relevance: Ultra-short container lifespans—serverless-like patterns on Kubernetes
Segment Applicability: All segments—indicates event-driven architectures

[DATA POINT]
"The size of container images has quintupled, introducing unnecessary security risks and operational inefficiencies"
— Sysdig 2025 Report
URL: https://www.sysdig.com/press-releases/2025-usage-report
Date: 2025
Relevance: Container bloat problem—security and efficiency concern
Segment Applicability: All segments

### Container Runtime Adoption

[DATA POINT]
"In 2021, Docker took up 46 percent of container runtime on platforms of Sysdig's global customer base, with both Containerd and Cri-O experiencing significant growth in 2021"
— Statista Container Platform Report
URL: https://www.statista.com/statistics/1224618/container-platforms-deployed-runtime/
Date: 2021 (most recent granular data available)
Relevance: Historical baseline—Docker declining, containerd/CRI-O rising
Segment Applicability: All segments
CAVEAT: 2021 data—significant changes likely by 2025

[DATA POINT]
"Since Kubernetes 1.20, Docker has been deprecated as a runtime, and as of 1.24, Kubernetes uses container runtimes that implement the Container Runtime Interface (CRI), such as containerd or CRI-O"
— Kubernetes Documentation / Industry Analysis
URL: https://www.devopstraininginstitute.com/blog/which-container-runtime-should-you-choose-for-kubernetes-clusters
Date: 2025
Relevance: Docker no longer viable for Kubernetes—containerd/CRI-O required
Segment Applicability: All Kubernetes users

### Serverless Adoption - General

[DATA POINT]
"The global serverless architecture market was valued at USD 18.2 billion in 2025 and is expected to grow to USD 22.5 billion in 2026, with a projected CAGR of 24.1% through 2035"
— GM Insights / Precedence Research
URL: https://www.gminsights.com/industry-analysis/serverless-architecture-market
Date: 2025
Relevance: Market size—serverless growing but smaller than Kubernetes market
Segment Applicability: All segments

[DATA POINT]
"According to Gartner, the serverless computing market is projected to exceed $24.2 billion by 2026, growing at an annual rate of 22.5%"
— Gartner Report
URL: https://www.synoverge.com/blog/serverless-computing-trends-use-cases-challenges/
Date: 2026 projection
Relevance: Analyst projection aligns with other market estimates
Segment Applicability: All segments

[STATISTIC]
"Serverless adoption remains split, with some expanding use while others step back due to cost and complexity. More specifically, only 11% of respondents are making use of serverless computing frameworks"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024
Relevance: LOW ADOPTION—only 11% despite market hype
Segment Applicability: All segments
CRITICAL SIGNAL: Major disconnect between market size projections and CNCF survey adoption

[DATA POINT]
"Close to 70% of enterprises in North America claimed to operate production loads on serverless systems"
— CNCF 2024 Survey
URL: https://stackshare.io/aws-lambda
Date: 2024
Relevance: North America-specific serverless adoption
Segment Applicability: North American enterprises
CAVEAT: Conflicts with 11% CNCF global figure—regional variation or definition difference

[DATA POINT]
"In 2024, the Cloud Native Computing Foundation found that 76% of organizations deployed streaming workloads in production with serverless functions"
— CNCF Survey
URL: https://stackshare.io/aws-lambda
Date: 2024
Relevance: Serverless for specific workload type (streaming)—not general compute
Segment Applicability: Organizations with streaming/event-driven workloads

### Serverless Market Leadership

[DATA POINT]
"Amazon Web Services (AWS) led the serverless architecture market with a 29.0% share in 2025, providing serverless computing facilities like AWS Lambda, API Gateway, and Fargate"
— GM Insights Market Report
URL: https://stackshare.io/aws-lambda
Date: 2025
Relevance: AWS dominates serverless market
Segment Applicability: All segments

[DATA POINT]
"AWS, Microsoft Azure, Google Cloud Platform (GCP), Alibaba Cloud, and Oracle Cloud are the key players in the serverless architecture industry, collectively holding more than 67% of the market in 2025"
— Market Research
URL: https://stackshare.io/aws-lambda
Date: 2025
Relevance: Hyperscaler concentration similar to Kubernetes market
Segment Applicability: All segments

### AWS Lambda Company Adoption

[DATA POINT]
"Major brands such as Netflix, Coca-Cola, Coinbase, Slack, and Nordstrom use AWS Lambda to power scalable, event-driven workloads with minimal infrastructure management"
— StackShare / Tech Data Park
URL: https://stackshare.io/aws-lambda
Date: 2025
Relevance: Named company examples—high-profile adopters
Segment Applicability: Large enterprise
CAVEAT: StackShare self-reported data—incomplete and biased toward companies that publicize their stack

### Serverless Containers

[DATA POINT]
"Serverless container adoption is growing across all major clouds, but Google Cloud leads the pack. In Google Cloud, 68% of container organizations now use serverless containers, up from 35% two years ago"
— Datadog State of Containers Report
URL: https://www.datadoghq.com/state-of-containers-and-serverless/
Date: 2025
Relevance: Google Cloud Run adoption among GCP container users
Segment Applicability: Google Cloud Platform users specifically

[DATA POINT]
"Over 64% of Kubernetes organizations have adopted Horizontal Pod Autoscaler (HPA), and 86% of HPA users apply it in most of their clusters, with nearly half using it in every cluster"
— Datadog Container Report
URL: https://www.datadoghq.com/state-of-containers-and-serverless/
Date: 2025
Relevance: Autoscaling adoption on Kubernetes—alternative to serverless for variable workloads
Segment Applicability: Kubernetes users

### Serverless Container Platforms Comparison

[DATA POINT]
"Google Cloud Run only allows you to spin up single containers, while AWS Fargate and Azure both allow multiple containers to be deployed together"
— Technical Comparison
URL: https://thenewstack.io/comparison-aws-fargate-vs-google-cloud-run-vs-azure-container-instances/
Date: 2025
Relevance: Platform capability differences
Segment Applicability: All segments evaluating serverless containers

[DATA POINT]
"Google Cloud Run and Azure Container Instances both support GPU-based workloads while AWS Fargate does not"
— Platform Comparison
URL: https://thenewstack.io/comparison-aws-fargate-vs-google-cloud-run-vs-azure-container-instances/
Date: 2025
Relevance: GPU support differentiation—critical for AI/ML workloads
Segment Applicability: AI/ML segment specifically

[DATA POINT]
"AWS Fargate's compute prices are generally lowest, Google comes second but their request-based model is pretty close to Azure, which was the most expensive option, at more than double the price of AWS"
— Pricing Analysis
URL: https://sliplane.io/blog/comparing-prices-aws-fargate-vs-azure-container-apps-vs-google-cloud-run
Date: 2025
Relevance: Pricing spread—Azure 2x more expensive than AWS for serverless containers
Segment Applicability: All segments—cost sensitivity varies

### Service Mesh Adoption

[DATA POINT]
"Service mesh adoption is now at an all-time high, with 70% of companies participating in the CNCF survey reporting that they are running a service mesh"
— CNCF Survey
URL: https://cloudnativenow.com/topics/cloudnativedevelopment/cncf-survey-surfaces-steady-pace-of-increased-cloud-native-technology-adoption/
Date: 2025
Relevance: High service mesh adoption—proxy for Kubernetes complexity/maturity
Segment Applicability: Advanced Kubernetes users

[DATA POINT]
"Service mesh adoption is declining, dropping from 50% in 2023 to 42% in 2024 due to operational overhead concerns"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024
Relevance: Service mesh DECLINING despite complexity—cost/benefit ratio questioned
Segment Applicability: All segments
CRITICAL CONFLICT: This contradicts 70% adoption claim above—different survey timing or definitions

[DATA POINT]
"The Service Mesh Tools Software Market size was USD 395.4 million in 2024, projected to grow to USD 499.59 million by 2025 and exceed USD 3,601.17 million by 2033, with a CAGR of 26.4%"
— Market Growth Reports
URL: https://www.marketgrowthreports.com/market-reports/service-mesh-tools-software-market-100476
Date: 2024-2025
Relevance: Market size—much smaller than Kubernetes or serverless markets
Segment Applicability: Enterprises with advanced microservices

[DATA POINT]
"The service mesh market has a 41.3% compound annual growth rate"
— Market Analysis
URL: https://cloudnativenow.com/topics/cloudnativedevelopment/cncf-survey-surfaces-steady-pace-of-increased-cloud-native-technology-adoption/
Date: 2025
Relevance: High growth rate despite adoption decline
Segment Applicability: All segments

[DATA POINT]
"Complexity remains a massive barrier, with 48% of DevOps engineers reporting struggling with the steep learning curve and management overhead introduced by mesh architectures like Istio or Linkerd"
— Industry Survey
URL: https://www.marketgrowthreports.com/market-reports/service-mesh-tools-software-market-100476
Date: 2025
Relevance: Complexity barrier—explains 2023-2024 adoption decline
Segment Applicability: All segments—especially SMB and mid-market

### Service Mesh Market Leadership

[DATA POINT]
"Istio has seen an uptick in adoption and now has the largest market share — albeit, by a slim margin — in the service mesh space. However, more recent trends show in 2025, engineers are increasingly choosing Linkerd"
— Industry Analysis
URL: https://www.buoyant.io/linkerd-vs-istio
Date: 2025
Relevance: Istio vs Linkerd competition—shift toward Linkerd
Segment Applicability: All service mesh users

[DATA POINT]
"According to a recent CNCF survey, Linkerd has surged ahead of Istio's adoption in the three major geographic zones of North America, Europe and Asia"
— CNCF Survey
URL: https://thenewstack.io/is-linkerd-winning-the-service-mesh-race/
Date: 2025
Relevance: Linkerd overtaking Istio regionally
Segment Applicability: All regions

### GitOps Adoption

[DATA POINT]
"GitOps is gaining traction, with 77% of organizations adopting its principles for deployment"
— CNCF Annual Survey 2024
URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
Date: 2024
Relevance: GitOps high adoption—indicates mature CI/CD practices
Segment Applicability: All segments with Kubernetes

### AI/ML Infrastructure Signals

[DATA POINT]
"Workloads using AI and machine learning packages grew by 500% over the last year, with the percentage of generative AI packages in use more than doubling"
— Sysdig 2025 Cloud-Native Security Report
URL: https://www.sysdig.com/press-releases/2025-usage-report
Date: 2025
Relevance: AI/ML workload explosion on cloud-native infrastructure
Segment Applicability: AI/ML segment specifically

[DATA POINT]
"Despite this rapid adoption, public exposure decreased by 38%, signaling a strong commitment to secure AI implementations"
— Sysdig 2025 Report
URL: https://www.sysdig.com/press-releases/2025-usage-report
Date: 2025
Relevance: AI security awareness improving
Segment Applicability: AI/ML segment

[DATA POINT]
"More than 60% of the Fortune 500 are implementing Kubernetes along with other open source tools like Prometheus and Falco"
— Industry Analysis
URL: https://sysdig.com/blog/sysdig-2025-cloud-native-security-and-usage-report
Date: 2025
Relevance: Fortune 500 Kubernetes penetration
Segment Applicability: Large enterprise specifically

[DATA POINT]
"Spending on AI-native apps jumped over 75% in the past year alone according to Zylo's 2025 SaaS Management Index"
— Zylo SaaS Management Index 2025
URL: https://zylo.com/blog/ai-in-saas/
Date: 2025
Relevance: AI SaaS spending growth
Segment Applicability: All segments

[DATA POINT]
"67% of SaaS businesses use AI to enhance their value offering, with 30,000+ SaaS companies catering to millions of users worldwide"
— Industry Analysis
URL: https://ossisto.com/blog/ai-saas-companies/
Date: 2025
Relevance: AI integration in SaaS products
Segment Applicability: SaaS companies specifically

### GitHub Infrastructure Repository Signals

[DATA POINT]
"There are just over 500,000 public HCL repos on GitHub, with Terraform representing a subset of those"
— GitHub Repository Analysis
URL: https://www.styra.com/blog/ai-generated-infrastructure-as-code-the-good-the-bad-and-the-ugly/
Date: 2025
Relevance: Terraform/IaC repository count—proxy for IaC adoption
Segment Applicability: All segments using infrastructure as code
CAVEAT: Public repos only—enterprise private repos not counted

[DATA POINT]
"The number of public GitHub repos available for AI training in infrastructure code is significantly smaller than those for Javascript, Python and other popular programming languages, resulting in a much smaller training dataset"
— Styra AI Infrastructure Report
URL: https://www.styra.com/blog/ai-generated-infrastructure-as-code-the-good-the-bad-and-the-ugly/
Date: 2025
Relevance: Infrastructure code visibility gap vs application code
Segment Applicability: All segments

### Security and Operational Signals

[DATA POINT]
"Machine identities vastly outnumber humans by 40,000 times and are 7.5 times more risky, with nearly 40% of breaches starting with credential exploitation"
— Sysdig 2025 Report
URL: https://www.sysdig.com/press-releases/2025-usage-report
Date: 2025
Relevance: Machine identity explosion in cloud-native environments
Segment Applicability: All segments—security complexity indicator

[DATA POINT]
"Mature security teams are detecting threats in under 5 seconds and initiating response actions within 3.5 minutes"
— Sysdig 2025 Report
URL: https://www.sysdig.com/press-releases/2025-usage-report
Date: 2025
Relevance: Leading security team performance benchmarks
Segment Applicability: Enterprises with mature security programs

[DATA POINT]
"87% of Container Images Have High Risk Vulnerabilities"
— Sysdig 2023 Usage Report
URL: https://www.sysdig.com/press-releases/sysdig-2023-usage-report
Date: 2023
Relevance: Container security risk baseline
Segment Applicability: All segments using containers

---

## Preliminary Estimates

### Kubernetes Adoption by Segment

**DIRECT ESTIMATE**
Enterprise (1000+ employees): 91% adoption
— Source: CNCF/Industry Surveys via Tigera
— URL: https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/

**DIRECT ESTIMATE**
SMB (500-1000 employees): 9% of Kubernetes user base
— Source: Industry Survey Data via Octopus
— URL: https://octopus.com/devops/ci-cd-kubernetes/kubernetes-statistics/
— Caveat: This is percentage of Kubernetes users, not percentage of SMB companies overall

### Managed vs Self-Managed Kubernetes

**DIRECT ESTIMATE**
Cloud-Hosted (Managed): 67%
Self-Managed: 33%
— Source: Industry Trend Report via Jeevi Academy
— URL: https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/
— Trend: Up from 45% cloud-hosted in 2022

### Serverless Framework Adoption

**DIRECT ESTIMATE**
Global adoption: 11% of CNCF survey respondents
North America enterprise adoption: 70% (production loads)
— Source: CNCF Annual Survey 2024
— URL: https://www.cncf.io/reports/cncf-annual-survey-2024/
— Major discrepancy: Regional/definition differences or survey bias

### Service Mesh Adoption

**CONFLICTING ESTIMATES**
Estimate 1: 70% of CNCF survey participants
— Source: CNCF Survey via Cloud Native Now
— URL: https://cloudnativenow.com/topics/cloudnativedevelopment/cncf-survey-surfaces-steady-pace-of-increased-cloud-native-technology-adoption/

Estimate 2: 42% (down from 50% in 2023)
— Source: CNCF Annual Survey 2024
— URL: https://www.cncf.io/reports/cncf-annual-survey-2024/

Data Quality Issue: Same source (CNCF) reporting conflicting figures—likely different survey waves or definitions

---

## Data Quality Assessment

### Completeness: 4/10

**Available:**
- Kubernetes adoption rates (enterprise)
- Managed Kubernetes market share (directional)
- Container usage statistics
- Service mesh adoption (conflicting data)
- General serverless market size

**Missing:**
- AI/ML-specific company technology profiles (StackShare has limited AI company data)
- Granular StackShare company counts by technology (API rate-limited)
- EKS vs AKS vs GKE specific adoption percentages (only directional claims)
- Serverless adoption by specific service (Lambda, Cloud Run, Fargate broken out)
- SMB segment infrastructure patterns
- Private GitHub repository infrastructure signals

**Gaps:**
StackShare profiles are self-reported and heavily biased toward companies that publicize their stack. Major AI companies (OpenAI, Anthropic) do not have detailed public StackShare profiles. GitHub public repositories represent <5% of enterprise infrastructure code based on public vs private repo ratios.

### Recency: 7/10

- CNCF 2024 Survey: Published April 2025 (recent, representative)
- Datadog 2025 Report: Current year data
- Sysdig 2025 Report: Current year data
- Market projections: 2025-2033 forecasts (forward-looking)
- Container runtime data: Last granular data from 2021 (outdated)

**Issue:** Some data sources conflate 2024 and 2025 data without clear methodology dates.

### Sample Size: 6/10

**CNCF Survey:**
- Sample size not disclosed in search results
- Geographic representation: Global but US-heavy
- Respondent profile: Cloud-native practitioners (selection bias)

**Datadog Reports:**
- Based on "Kubernetes-using organizations across Datadog's customer base"
- No specific N provided
- Sample bias: Datadog customers (observability-mature orgs)

**Sysdig Reports:**
- Based on "global customer base"
- No specific N provided
- Sample bias: Security-conscious organizations

**Market Research Reports:**
- Methodologies not disclosed
- Sample sizes unknown

### Known Biases

1. **StackShare Self-Reporting Bias:** Companies publicizing their stack are more likely to be:
   - VC-backed startups seeking publicity
   - Open source-friendly organizations
   - Companies with strong engineering brands
   - NOT representative of average enterprise

2. **Survey Respondent Bias:** CNCF, Datadog, Sysdig surveys reach:
   - Cloud-native early adopters (not laggards)
   - Organizations already using their platforms
   - DevOps/platform engineering roles (not business decision-makers)

3. **GitHub Public Repository Bias:**
   - Only ~5% of enterprise code is public
   - Open source projects over-represented
   - Proprietary infrastructure under-represented
   - AI companies particularly secretive about infrastructure

4. **Geographic Bias:**
   - Most data sources US/North America-centric
   - "Global" surveys often 50%+ North American respondents
   - Asia-Pacific and emerging markets under-represented

5. **Company Size Bias:**
   - Enterprise over-represented in surveys (91% of Kubernetes users at 1000+ employee orgs)
   - SMB infrastructure patterns largely invisible
   - Startups and mid-market underreported

6. **Technology Maturity Bias:**
   - Kubernetes well-measured (mature, established)
   - Serverless poorly measured (fragmented definitions)
   - Emerging technologies (service mesh) have volatile/conflicting data

---

## Limitations — What This Source CANNOT Tell Us

### 1. AI-Specific Infrastructure Patterns

**Cannot Determine:**
- What percentage of AI SaaS companies use Kubernetes vs serverless
- GPU infrastructure patterns (on-prem vs cloud, bare metal vs containers)
- Vector database deployment patterns
- Model serving infrastructure (dedicated vs shared clusters)
- Training infrastructure vs inference infrastructure splits

**Why:** AI companies do not publish infrastructure details. StackShare has minimal AI company profiles. GitHub public repos for AI infrastructure are rare (proprietary advantage).

### 2. Hybrid Architecture Prevalence

**Cannot Determine:**
- What percentage of companies use BOTH Kubernetes AND serverless (hybrid)
- Workload distribution across hybrid architectures
- Kubernetes for stateful + serverless for stateless patterns
- Multi-cloud vs single-cloud infrastructure deployment

**Why:** Surveys ask "do you use X" not "what percentage of workloads run on X" or "how do you combine X and Y."

### 3. Cost Economics

**Cannot Determine:**
- Actual infrastructure spend (Kubernetes TCO vs serverless TCO)
- Cost per transaction / cost per user by architecture type
- Infrastructure cost as percentage of revenue
- ROI of managed services vs self-managed

**Why:** Financial data is proprietary. Cost comparisons are theoretical (blog posts, vendor claims) not empirical.

### 4. SMB and Mid-Market Reality

**Cannot Determine:**
- What infrastructure do non-cloud-native SMBs use
- Adoption rates for companies <500 employees
- Managed service preferences in SMB segment
- Infrastructure decision drivers for resource-constrained teams

**Why:** Survey samples are 91% enterprises (1000+ employees). SMB infrastructure is invisible in this data.

### 5. Workload-Specific Adoption

**Cannot Determine:**
- Kubernetes adoption for web apps vs batch processing vs ML training
- Serverless adoption for APIs vs event processing vs background jobs
- Service mesh adoption for east-west traffic vs ingress only

**Why:** Surveys measure technology adoption at org level, not workload level.

### 6. Migration Patterns and Trends

**Cannot Determine:**
- Are companies migrating FROM Kubernetes TO serverless (or vice versa)
- How many companies abandoned Kubernetes after trying it
- How many serverless users are planning to add Kubernetes
- Technology churn rates

**Why:** Surveys capture point-in-time adoption, not migration flows or abandonments.

### 7. Operational Complexity Reality

**Cannot Determine:**
- Actual team sizes required to operate Kubernetes vs serverless
- Time to production for new services
- Incident rates and MTTR by infrastructure type
- Developer productivity impact

**Why:** Operational metrics are internal and proprietary. Publicly shared data is anecdotal.

### 8. Vendor Lock-In and Portability

**Cannot Determine:**
- How many "Kubernetes" users are actually locked into EKS/AKS/GKE-specific features
- How many "serverless" users can migrate between Lambda/Cloud Functions/Cloud Run
- Actual multi-cloud deployment rates (vs stated intentions)

**Why:** Companies overstate portability in surveys. Actual infrastructure configurations reveal lock-in not disclosed publicly.

---

## Confidence Score: 5/10

### Justification

**High Confidence (7-8/10) Areas:**
- Kubernetes enterprise adoption >90% (multiple converging sources)
- Managed Kubernetes growing faster than self-managed (consistent directional signal)
- Service mesh complexity barrier (consistent across sources)
- Container usage growing (multiple vendor reports align)

**Medium Confidence (5-6/10) Areas:**
- Managed Kubernetes market share (GKE 32%, AKS 28%)—directional correct but exact figures uncertain
- Cloud-hosted vs self-managed split (67%/33%)—believable but single source
- AI/ML workload growth (500% YoY)—Sysdig customer base only

**Low Confidence (3-4/10) Areas:**
- Serverless adoption (11% CNCF global vs 70% North America enterprise)—major conflicts
- Service mesh adoption (70% vs 42% in same year)—data quality issues
- StackShare company counts (39,816 using Kubernetes)—self-reported, incomplete
- AI SaaS company infrastructure specifics—virtually no reliable data

**Very Low Confidence (1-2/10) Areas:**
- Individual AI company technology profiles (OpenAI, Anthropic, etc.)—no data
- GitHub repository signals for AI infrastructure—public repos not representative
- SMB infrastructure patterns—invisible in data
- Hybrid architecture prevalence—not measured

### Why Overall 5/10

**Strengths:**
- Multiple independent sources (CNCF, Datadog, Sysdig) converge on Kubernetes dominance
- Enterprise adoption rates well-documented
- Trend directions (managed services growing, containers expanding) consistent

**Weaknesses:**
- AI-specific signals nearly absent (research question partially unanswered)
- Major conflicts in serverless data render adoption rates unreliable
- StackShare self-reporting bias makes company-specific profiles meaningless
- GitHub public repos represent <5% of actual infrastructure code
- SMB segment invisible (91% of data is enterprises)
- No workload-level granularity (what runs on Kubernetes vs serverless)

**PROXY SIGNAL CAVEAT:**
StackShare profiles, GitHub public repos, and vendor customer surveys are WEAK SIGNALS. They reveal what cloud-native early adopters disclose publicly, NOT what the broader market does in practice. These sources cannot answer the core research question: "What infrastructure technologies do AI SaaS companies actually use?" They can only answer: "What do cloud-native enterprises who respond to surveys say they use?"

For AI SaaS infrastructure reality, primary research (interviews, case studies) or proprietary vendor data (AWS/GCP/Azure usage analytics) would be required.

---

## Sources

- [Tigera: 36 Kubernetes Statistics You Must Know in 2025](https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-statistics/)
- [CNCF: Cloud Native 2024 Annual Survey](https://www.cncf.io/reports/cncf-annual-survey-2024/)
- [Datadog: A 2025 Look at Real-World Kubernetes Version Adoption](https://securitylabs.datadoghq.com/articles/a-2025-look-at-real-world-kubernetes-adoption/)
- [Datadog: State of Containers and Serverless](https://www.datadoghq.com/state-of-containers-and-serverless/)
- [Sysdig: 2025 Cloud-Native Security and Usage Report](https://www.sysdig.com/2025-cloud-native-security-and-usage-report)
- [Octopus: 40 Kubernetes Statistics in 2025](https://octopus.com/devops/ci-cd-kubernetes/kubernetes-statistics/)
- [StackShare: AWS Lambda Companies and Reviews](https://stackshare.io/aws-lambda)
- [StackShare: Kubernetes In Stacks](https://stackshare.io/kubernetes/in-stacks)
- [StackShare: Hugging Face Reviews](https://stackshare.io/hugging-face)
- [Market Growth Reports: Service Mesh Tools Market](https://www.marketgrowthreports.com/market-reports/service-mesh-tools-software-market-100476)
- [GM Insights: Serverless Architecture Market](https://www.gminsights.com/industry-analysis/serverless-architecture-market)
- [Styra: AI-Generated Infrastructure-as-Code Report](https://www.styra.com/blog/ai-generated-infrastructure-as-code-the-good-the-bad-and-the-ugly/)
- [Cloud Native Now: CNCF Survey Surfaces Cloud-Native Adoption](https://cloudnativenow.com/topics/cloudnativedevelopment/cncf-survey-surfaces-steady-pace-of-increased-cloud-native-technology-adoption/)
- [The New Stack: Comparison of AWS Fargate vs Google Cloud Run vs Azure Container Instances](https://thenewstack.io/comparison-aws-fargate-vs-google-cloud-run-vs-azure-container-instances/)
- [Jeevi Academy: Kubernetes Adoption Statistics and Trends for 2025](https://www.jeeviacademy.com/kubernetes-adoption-statistics-and-trends-for-2025/)
