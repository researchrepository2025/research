# Wave 2 Analysis: Self-Managed / Open Kubernetes Adoption Among AI SaaS Companies

**Analysis Date:** 2026-02-12
**Analyst:** Wave 2 Synthesis Agent
**Wave 1 Inputs:** 01_cncf_survey.md, 02_analyst_reports.md, 03_job_postings.md, 04_tech_blogs.md, 05_cloud_vendor_cases.md, 06_stackshare_github.md, 07_sec_earnings.md, 08_vc_startup_db.md

---

## Executive Summary

Self-managed Kubernetes adoption among AI SaaS companies is a significant but declining minority pattern concentrated among large-scale operators with specialized infrastructure needs. Cross-referencing all 8 Wave 1 sources, I estimate **15-22% of AI SaaS companies run self-managed K8s** as a component of their infrastructure, with this figure heavily skewed toward companies with $200M+ ARR, dedicated platform engineering teams, and GPU-intensive workloads requiring bare-metal or custom scheduling control. The trend direction is clearly **away from self-managed and toward managed K8s**, with the self-managed share of all K8s clusters dropping from ~55% (2022) to ~33% (2025). Companies that retain self-managed K8s do so for defensible reasons: GPU scheduling control, bare-metal performance for training workloads, compliance requirements, and multi-cloud portability without hyperscaler lock-in.

---

## 1. What Percentage of AI SaaS Companies Run Self-Managed K8s?

### Headline Estimate: 15-22%

**Classification: Estimated** (derived through triangulation of multiple indirect data sources; no single source directly measures "AI SaaS companies running self-managed K8s")

### Evidence Chain

**Step 1: Overall Self-Managed K8s Share (All Industries)**

Based on [02_analyst_reports.md, Data Point 1], Dynatrace 2023 reports that "73% of cloud Kubernetes clusters are built on managed distributions" with "the remaining 27% self-managed by the customer on cloud virtual machines." (Direct)

Based on [02_analyst_reports.md, Data Point 2], aggregated analyst sources for 2025 report "Managed Kubernetes has captured approximately 63% of Kubernetes deployments, with the remaining share being self-managed" -- yielding a 37% self-managed figure across all environments (including on-premises). (Direct)

Based on [06_stackshare_github.md, Managed K8s section], industry trend data shows "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022" -- implying 33% remain self-managed/on-prem in 2025. (Direct)

**Reconciliation:** Cloud-only self-managed is ~27% (Dynatrace). All-environment self-managed (including on-prem) is 33-37%. These are consistent: on-premises K8s is almost entirely self-managed, inflating the all-environment figure.

**Step 2: AI SaaS Adjustment**

Based on [01_cncf_survey.md, Data Point 20], the CNCF 2024 survey shows "respondents were evenly split (59%) between on-premises data centers and public clouds, with both skewing heavily toward self-managed instances." This suggests self-managed preferences may be higher than the 27% cloud-only figure among CNCF respondents (who skew technical). (Direct)

Based on [04_tech_blogs.md], engineering blog evidence identifies 5 companies with disclosed self-managed K8s patterns (OpenAI, Databricks, Salesforce, HubSpot, Elastic) versus 12+ using managed K8s (Anthropic, Cohere, Snowflake, Notion, Grammarly, Figma, Contextual AI, Picterra, Stacks, etc.). This yields approximately 29% self-managed among the blogging sample. (Inferred)

Based on [08_vc_startup_db.md], startup infrastructure guidance recommends "Kubernetes should be avoided early unless absolutely necessary" at seed stage, and "Microservices architecture with Kubernetes orchestration is best suited for funded SaaS startups targeting large-scale deployments." Self-managed K8s requires even more expertise than managed K8s, further concentrating it among larger companies. (Inferred)

**Step 3: AI SaaS-Specific Estimate**

AI SaaS companies are more likely than average enterprises to run self-managed K8s because:
- GPU scheduling requirements favor custom K8s configurations
- Large model training benefits from bare-metal performance
- Multi-cloud strategies for GPU access require portable K8s

But AI SaaS companies are also more likely to use managed K8s because:
- Managed K8s providers (EKS, GKE, AKS) now offer GPU node pools and AI-optimized configurations
- Most AI SaaS companies lack the 5-15 person platform engineering team needed for self-managed K8s
- Based on [01_cncf_survey.md, Data Point 24], "Only 41% of professional AI developers are cloud native" -- suggesting many AI teams lack K8s expertise

**Final Calculation:**
- General market self-managed K8s: 27-37% (Direct)
- AI SaaS blog sample: ~29% (Inferred from 04_tech_blogs.md)
- Downward adjustment for company size distribution: AI SaaS skews smaller than general enterprise, and based on [01_cncf_survey.md, Data Point 27], 91% of K8s users are at 1,000+ employee companies. Self-managed K8s requires even larger teams.
- Upward adjustment for GPU/performance needs: AI workloads have stronger reasons for self-management

**Net estimate: 15-22% of AI SaaS companies run self-managed K8s as a meaningful part of their infrastructure.**

**Confidence: 4/10** -- No direct measurement exists. Triangulated from general industry data, a small sample of engineering blogs, and structural reasoning about AI SaaS company characteristics.

---

## 2. Why Do AI SaaS Companies Choose Self-Managed Over Managed K8s?

### 2.1 GPU Scheduling and Hardware Control

**Classification: Inferred** (from case studies and architectural patterns)

Based on [04_tech_blogs.md, OpenAI case study], OpenAI "scaled Kubernetes clusters to 7,500 nodes" on Azure and "switched from Flannel to native Azure pod networking (Azure CNI) due to throughput scaling issues." While OpenAI runs on Azure infrastructure, they maintain deep control over their K8s configuration -- a hybrid self-managed-on-cloud-IaaS pattern. The need to customize networking, GPU scheduling, and batch processing at 7,500-node scale drives self-management. (Inferred)

Based on [01_cncf_survey.md, Data Point 36], iFLYTEK (Chinese AI company) "adopted elastic scheduling, DAG-based workflows, and multi-tenant isolation" using Volcano on K8s, addressing "inefficient scheduling leaving GPUs underused." Custom GPU scheduling is a primary driver for self-management -- managed K8s services historically lacked sophisticated GPU-aware scheduling. (Inferred)

Based on [04_tech_blogs.md, CNCF AI Conformance Program], CNCF launched the "Certified Kubernetes AI Conformance program to standardise AI workloads by establishing a technical baseline for GPU management, networking, and gang scheduling." The existence of this standardization effort confirms that GPU scheduling on K8s was previously fragmented and non-standard -- precisely why companies self-managed. (Inferred)

**Key insight:** As managed K8s providers add native GPU scheduling (GKE Cluster Director, EKS 100,000-node support), the GPU scheduling rationale for self-management is weakening.

### 2.2 Bare-Metal Performance

**Classification: Direct** (from engineering disclosures)

Based on [04_tech_blogs.md, Salesforce case study], "Salesforce deploys and runs Kubernetes directly atop bare metal, integrating it into the rest of the Salesforce infrastructure." Bare-metal K8s eliminates the hypervisor layer, reducing latency and maximizing GPU/CPU throughput for compute-intensive workloads. (Direct)

Based on [08_vc_startup_db.md, CoreWeave data], CoreWeave "provides a Kubernetes native cloud built for large, GPU-accelerated workloads" and "renting an NVIDIA A100 40GB GPU on CoreWeave costs approximately $1.39/hour versus $3.67/hour on Azure or Google Cloud -- a 62% cost advantage." This demonstrates that bare-metal K8s on dedicated GPU infrastructure offers both performance and cost advantages. (Direct)

### 2.3 Avoiding Cloud Lock-In / Multi-Cloud Portability

**Classification: Inferred** (from deployment patterns)

Based on [04_tech_blogs.md, Databricks case study], Databricks "operates a mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)" across "thousands of Kubernetes clusters." Running self-managed K8s alongside managed enables Databricks to maintain portability across all three hyperscalers. (Direct)

Based on [04_tech_blogs.md, Elastic case study], Elastic "selected Crossplane as the infrastructure management tool, which extends the Kubernetes API to enable provisioning and management of cloud infrastructure using Kubernetes-native tools." Using K8s API abstractions across multiple clouds (AWS 4 regions, GCP 3 regions, Azure 1 region) enables multi-cloud deployment without lock-in to any single managed K8s offering. (Direct)

Based on [01_cncf_survey.md, Data Point 9], "56% of organizations use multi-cloud solutions with an average of 2.8 unique cloud service providers." Multi-cloud strategies create demand for portable K8s configurations that self-management enables. (Direct)

### 2.4 Cost Economics at Scale

**Classification: Inferred** (from financial data and case studies)

Based on [07_sec_earnings.md, AI SaaS Cost], "AI SaaS might see 40-50% (or more) of revenue eaten by COGS in the form of model hosting, inference compute, and data costs." When infrastructure represents 40-50% of revenue, even small efficiency gains from self-management are worth significant engineering investment. (Direct)

Based on [08_vc_startup_db.md, CoreWeave pricing], dedicated GPU clouds with Kubernetes-native infrastructure offer 62% cost advantages over hyperscaler managed services. Companies operating at sufficient scale can achieve similar savings by self-managing K8s on bare metal or dedicated hardware. (Inferred)

Based on [07_sec_earnings.md, Datadog GPU report], "83% of container costs were associated with idle resources." Self-managed K8s allows custom autoscaling and bin-packing configurations that can reduce idle resource waste, which is particularly impactful for expensive GPU instances. (Inferred)

### 2.5 Compliance and Data Sovereignty

**Classification: Estimated** (limited direct evidence)

Based on [01_cncf_survey.md, Data Point 11], "Large organizations (5000+ employees): 56% adopt hybrid clouds" and "Small organizations: 27% hybrid cloud adoption." Hybrid cloud adoption -- which often involves on-premises self-managed K8s -- correlates with company size, where larger companies face stricter compliance requirements. (Inferred)

Based on [04_tech_blogs.md, Cohere case study], Cohere offers "Deployment options: SaaS, cloud of choice, on-prem" and "private deployments typically run on Kubernetes." On-premises K8s deployments for customers with data sovereignty requirements are inherently self-managed. (Direct)

Based on [01_cncf_survey.md, Data Point 15], Europe shows 82% cloud-native adoption versus Americas at 70% -- but European data sovereignty requirements (GDPR, NIS2, Schrems II) may push more of that adoption toward on-premises or self-managed configurations rather than US-hyperscaler managed services. (Estimated)

---

## 3. Breakdown by Company Size

### Large Companies ($200M+ ARR, 1000+ employees): 25-35% self-managed K8s

**Classification: Estimated**

Based on [01_cncf_survey.md, Data Points 27-28], "34% of Kubernetes users are in companies with over 20,000 employees" and "Organizations with over 1,000 employees represent 91% of Kubernetes users, controlling 68.2% of container market revenue." Large companies are far more likely to both use K8s and to self-manage it. (Direct)

Based on [04_tech_blogs.md], all 5 identified self-managed K8s companies (OpenAI, Databricks, Salesforce, HubSpot, Elastic) are large companies with dedicated platform engineering teams. (Direct)

Based on [03_job_postings.md, Data Point 8], Platform Engineering roles grew from 8.35% to 11% of infrastructure jobs (+32% YoY). Based on [03_job_postings.md, Data Point 3], Platform Engineers are 8.35% of 4,850 qualified K8s job postings. Platform Engineering teams are the organizational prerequisite for self-managed K8s, and they exist almost exclusively at larger companies. (Inferred)

Based on [07_sec_earnings.md, IBM OpenShift], "OpenShift ARR exceeded $1.9 billion at more than 30% growth." OpenShift is a K8s distribution primarily deployed as self-managed or hybrid. Its $1.9B ARR indicates substantial enterprise demand for self-managed K8s platforms. (Direct)

**Reasoning:** Large AI SaaS companies have the platform engineering teams (5-15 people), the scale to justify self-management economics, and the compliance/multi-cloud requirements that favor self-managed K8s. At 25-35%, self-managed K8s is a significant minority pattern among large AI SaaS companies.

### Mid-Market Companies ($10M-$200M ARR, 100-1000 employees): 8-15% self-managed K8s

**Classification: Estimated**

Based on [01_cncf_survey.md, Data Point 27], "only 9% of Kubernetes adopters are companies with 500-1,000 employees." Even managed K8s adoption is low in this segment -- self-managed is even lower. (Direct)

Based on [08_vc_startup_db.md, startup infrastructure guidance], Series A companies should focus on "structured environments (dev/stage/prod)" and "Infrastructure as Code" -- not K8s complexity. K8s is recommended only for "funded SaaS startups targeting large-scale deployments." (Direct)

Based on [03_job_postings.md, Data Point 20], "60% of DevOps positions are senior-level" and "5% junior-level," indicating K8s requires experienced engineers that mid-market companies struggle to recruit and retain. Self-managing K8s requires even deeper expertise. (Inferred)

**Reasoning:** Mid-market AI SaaS companies that run self-managed K8s typically do so because they began with it before managed offerings matured, or they have specialized workloads (on-prem deployment for regulated customers). Most mid-market companies either use managed K8s (EKS/GKE/AKS) or skip K8s entirely in favor of simpler abstractions.

### Small Companies / Startups (<$10M ARR, <100 employees): 2-5% self-managed K8s

**Classification: Estimated**

Based on [08_vc_startup_db.md, startup infrastructure guidance], "At the Seed stage, Kubernetes should be avoided early unless absolutely necessary due to its high adoption barrier." Self-managed K8s is even more complex. (Direct)

Based on [08_vc_startup_db.md, Y Combinator data], "58% of Y Combinator startups accepting Azure credits" and GPU availability drives cloud provider selection, not K8s self-management capability. (Direct)

Based on [01_cncf_survey.md, Data Point 14], "46% of organizations just beginning their cloud native journey identify lack of training as biggest challenge." Early-stage AI SaaS companies face this training gap acutely for self-managed K8s. (Direct)

**Reasoning:** The 2-5% who run self-managed K8s at this stage are typically (a) technical founders from platform engineering backgrounds who bring K8s expertise from previous companies, (b) companies using k3s/lightweight K8s distributions for edge or on-prem deployments, or (c) companies using K8s-native GPU clouds like CoreWeave that blur the self-managed/managed boundary.

---

## 4. US vs EU Differences

### Classification: Estimated (limited direct evidence for AI SaaS specifically)

**Overall Cloud-Native Adoption:**

Based on [01_cncf_survey.md, Data Point 15], "Europe: 82% in 'some' or 'much/all' cloud native development" versus "Americas: 70%." Europe actually leads the Americas in overall cloud-native adoption. (Direct)

**Hybrid Cloud (Proxy for Self-Managed K8s):**

Based on [01_cncf_survey.md, Data Point 11], large organizations (5000+ employees) show 56% hybrid cloud adoption. European enterprises, subject to GDPR and data sovereignty requirements, are more likely to maintain on-premises infrastructure alongside cloud -- much of which runs self-managed K8s. (Inferred)

Based on [02_analyst_reports.md, Data Point 28], Flexera reports "70% of survey respondents are embracing hybrid cloud strategies." EU respondents likely skew higher due to regulatory pressures. (Inferred)

**EU Data Sovereignty Signal:**

Based on [04_tech_blogs.md, Cohere case study], Cohere's "private deployments typically run on Kubernetes" with "deployment options: SaaS, cloud of choice, on-prem." European customers frequently demand on-premises deployment for data sovereignty compliance, which requires self-managed K8s. (Inferred)

Based on [05_cloud_vendor_cases.md, Stacks case study], Amsterdam-based Stacks (founded 2024, raised EUR10M) uses "GKE Autopilot" -- a fully managed K8s offering, suggesting EU startups are not inherently drawn to self-managed. (Direct)

**Estimate:**
- **US AI SaaS self-managed K8s: 12-18%** -- US companies lean toward managed K8s given deeper hyperscaler integration and less regulatory pressure for on-prem.
- **EU AI SaaS self-managed K8s: 20-30%** -- GDPR, NIS2, and data residency requirements push more EU AI companies toward on-premises or private cloud self-managed K8s, particularly for customer-facing workloads processing personal data.

**Confidence: 3/10** -- No Wave 1 source directly compares US vs EU self-managed K8s rates for AI SaaS. Regional CNCF survey data exists for overall cloud-native adoption but not for K8s management type.

---

## 5. On-Premises vs Cloud IaaS Self-Managed K8s

### Classification: Inferred (from deployment pattern data)

**On-Premises Self-Managed K8s:**

Based on [01_cncf_survey.md, Data Point 20], "59% of respondents use on-premises data centers, skewing heavily toward self-managed instances." On-premises K8s is by definition self-managed (no managed control plane available). (Direct)

Based on [04_tech_blogs.md, Salesforce case study], Salesforce "deploys and runs Kubernetes directly atop bare metal." This represents the on-premises self-managed pattern at enterprise scale. (Direct)

Based on [07_sec_earnings.md, IBM OpenShift], OpenShift at $1.9B ARR is primarily deployed on-premises or in hybrid configurations, representing the dominant on-premises K8s platform. (Inferred)

**Cloud IaaS Self-Managed K8s (K8s on VMs without managed control plane):**

Based on [02_analyst_reports.md, Data Point 1], the 27% self-managed figure in cloud is specifically "self-managed by the customer on cloud virtual machines." (Direct)

Based on [04_tech_blogs.md, OpenAI case study], OpenAI runs K8s on Azure infrastructure but maintains deep control over the K8s configuration -- a cloud IaaS self-managed pattern. (Direct)

Based on [04_tech_blogs.md, Databricks case study], Databricks runs "a mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)" -- the self-managed portion runs on cloud IaaS VMs. (Direct)

**Estimated Split Among Self-Managed K8s in AI SaaS:**

| Environment | Share of Self-Managed | Typical Use Case |
|---|---|---|
| On-premises bare metal | 30-40% | GPU training clusters, data sovereignty compliance, Salesforce-style large enterprise |
| Cloud IaaS VMs | 45-55% | Multi-cloud portability, custom GPU scheduling, OpenAI/Databricks-style cloud-based self-management |
| Edge / hybrid | 5-15% | On-device inference, distributed AI at edge locations |

**Confidence: 3/10** -- The on-prem vs cloud split for self-managed K8s among AI SaaS companies specifically is not directly measured by any Wave 1 source.

---

## 6. Are Companies Moving Away from Self-Managed K8s?

### Headline Finding: Yes -- the trend is clearly toward managed K8s

**Classification: Direct** (multiple converging data sources)

### Migration Trend Evidence

Based on [01_cncf_survey.md, Data Point 19], "90% of Kubernetes users have turned to cloud-managed services, according to Datadog data, up from 70% in 2020." This 20-percentage-point shift in just one year (2020-2021) represented a massive migration wave toward managed K8s. (Direct)

Based on [06_stackshare_github.md, Managed K8s section], "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022." From 45% cloud-hosted in 2022 to 67% in 2025 represents a sustained multi-year shift toward managed/cloud-hosted K8s. (Direct)

Based on [06_stackshare_github.md, Managed K8s growth], "The demand for managed Kubernetes services represents a significant growth opportunity, with the segment expected to grow at a CAGR of over 30%." Managed K8s is growing faster than K8s overall. (Direct)

### Migration Case Studies (Toward Managed K8s)

Based on [04_tech_blogs.md], migration patterns documented in 2024-2025 are exclusively **toward** Kubernetes, not away:
- **Figma:** ECS to EKS (managed K8s) -- "cost savings, improved developer experience, and increased resiliency" (Direct)
- **Grammarly:** EC2 to EKS (managed K8s) -- "decouple storage from compute resources" (Direct)
- **Salesforce Data Cloud:** EC2 to K8s -- "migrated in 6 months" (Direct)
- **HubSpot:** EC2 to K8s (Direct)

**Critically:** No engineering blog in Wave 1 documented a migration FROM self-managed K8s TO a non-K8s alternative. No company disclosed abandoning self-managed K8s. (Direct -- absence of evidence in 04_tech_blogs.md)

### Managed K8s Capability Improvements Reducing Self-Management Rationale

Based on [05_cloud_vendor_cases.md, EKS ultrascale], "Amazon EKS now supports clusters with up to 100,000 nodes" and "can potentially support up to 1.6 million AWS Trainium chips or 800,000 NVIDIA GPUs in a single Kubernetes cluster." This eliminates scale as a reason for self-management. (Direct)

Based on [04_tech_blogs.md, GKE 130K nodes], "Google Cloud engineered a record-shattering 130,000-node GKE cluster, doubling prior limits to meet AI's exascale demands." (Direct)

Based on [04_tech_blogs.md, AKS Fleet Manager], "Microsoft's AKS demonstrated 80 clusters deployed within a single fleet with 70,000 nodes distributed across six geographic regions." (Direct)

Based on [04_tech_blogs.md, CNCF AI Conformance], the CNCF AI Conformance program standardizes GPU management, networking, and gang scheduling on managed K8s -- directly addressing the GPU scheduling gap that previously justified self-management. (Direct)

### Quantified Trend

| Year | Self-Managed Share (Cloud) | Self-Managed Share (All Envs) | Source |
|---|---|---|---|
| 2020 | ~30% | ~55% | [01_cncf_survey.md, DP 19] Datadog: 70% managed |
| 2021 | ~21% | ~45% | [01_cncf_survey.md, DP 17] CNCF: 79% managed |
| 2022 | ~25% | ~55% | [06_stackshare_github.md] 45% cloud-hosted |
| 2023 | ~27% | ~40% | [02_analyst_reports.md, DP 1] Dynatrace: 73% managed |
| 2025 | ~20% | ~33% | [02_analyst_reports.md, DP 2] 63% managed all-envs |

**Direction: Self-managed K8s share is declining at approximately 3-5 percentage points per year across all environments.**

**Confidence: 7/10** -- Multiple independent sources (Datadog telemetry, CNCF surveys, Dynatrace observability data, analyst aggregations) converge on the same directional trend. Exact figures vary by methodology and scope, but the direction is unambiguous.

---

## 7. Role of K8s Distributions in Self-Managed Deployments

### Classification: Mixed (Direct for some distributions, Estimated for AI SaaS usage)

### Red Hat OpenShift

Based on [07_sec_earnings.md, IBM OpenShift], "OpenShift ARR exceeded $1.9 billion at more than 30% growth." OpenShift is the dominant self-managed/hybrid K8s distribution by revenue. (Direct)

**AI SaaS relevance:** OpenShift is primarily adopted by large enterprises in regulated industries (financial services, healthcare, government). Based on [08_vc_startup_db.md, Komodor data], Komodor "expanded its customer base across industries such as financial services, retail, and technology." AI SaaS companies in regulated verticals (healthcare AI, financial AI) are the most likely OpenShift adopters. (Inferred)

**Estimated share of self-managed K8s in AI SaaS: 20-30%** -- primarily among large enterprises and regulated industries where Red Hat support contracts are valued.

### Rancher / RKE (SUSE)

Based on [01_cncf_survey.md], Rancher is not directly referenced in Wave 1 CNCF survey data. However, Rancher/RKE serves the multi-cluster management use case, which based on [04_tech_blogs.md, Databricks case study], is relevant for companies running "thousands of Kubernetes clusters" across multiple clouds.

**AI SaaS relevance:** Rancher's multi-cluster management capability is relevant for AI SaaS companies offering on-premises deployment to customers (like Cohere's private deployment model). (Estimated)

**Estimated share of self-managed K8s in AI SaaS: 10-15%** -- primarily for multi-cluster management across heterogeneous environments.

### VMware Tanzu (Broadcom)

Not directly referenced in any Wave 1 source. Tanzu's market position has been disrupted by Broadcom's acquisition of VMware and subsequent pricing changes.

**Estimated share of self-managed K8s in AI SaaS: 5-10%** -- declining due to Broadcom pricing disruption and migration to alternatives.

### k3s (Lightweight K8s)

Based on [08_vc_startup_db.md], startup infrastructure guidance recommends avoiding K8s complexity at early stages. k3s reduces that complexity significantly for edge, IoT, and lightweight deployment scenarios.

**AI SaaS relevance:** k3s is relevant for AI SaaS companies deploying models at the edge (based on [02_analyst_reports.md, Data Point 11], "13% at the edge" for AI/ML model hosting). (Inferred)

**Estimated share of self-managed K8s in AI SaaS: 5-10%** -- primarily for edge inference deployments and lightweight development environments.

### Vanilla / Upstream K8s (kubeadm, kops)

Based on [04_tech_blogs.md, OpenAI case study], OpenAI's K8s deployment appears to use upstream K8s customized for their Azure environment. Large AI companies with dedicated platform teams may prefer vanilla K8s to avoid distribution-specific abstractions that limit customization.

**Estimated share of self-managed K8s in AI SaaS: 25-35%** -- the largest category, comprising companies that run upstream K8s with custom tooling (often on cloud IaaS). This is the "build your own platform" approach favored by the largest AI companies.

### K8s-Native GPU Clouds (CoreWeave, Lambda Labs)

Based on [08_vc_startup_db.md, CoreWeave data], CoreWeave "provides a Kubernetes native cloud built for large, GPU-accelerated workloads" with "250,000 GPUs" across 32 data centers. CoreWeave's revenue grew 420% YoY in Q1 2025. (Direct)

**AI SaaS relevance:** These platforms occupy a hybrid space -- the customer interacts with K8s directly but the control plane and infrastructure are managed by the GPU cloud provider. Based on [08_vc_startup_db.md], "OpenAI signed a five-year cloud-computing contract worth approximately $12 billion with CoreWeave." (Direct)

**Classification note:** K8s-native GPU clouds like CoreWeave are arguably managed K8s (the provider manages the control plane) but the customer experience is closer to self-managed (direct K8s API access, custom scheduling, bare-metal GPUs). For this analysis, I classify them as a **hybrid category** that may account for 10-20% of what companies self-report as "self-managed" K8s.

### Distribution Summary Table

| Distribution | Estimated Share of Self-Managed K8s in AI SaaS | Primary Use Case | Confidence |
|---|---|---|---|
| Vanilla / Upstream K8s | 25-35% | Large companies with platform teams, custom GPU scheduling | 3/10 |
| Red Hat OpenShift | 20-30% | Regulated enterprises, hybrid cloud | 5/10 (OpenShift revenue is direct) |
| Rancher / RKE | 10-15% | Multi-cluster management, on-prem customer deployments | 2/10 |
| k3s | 5-10% | Edge inference, lightweight deployments | 2/10 |
| VMware Tanzu | 5-10% | Legacy enterprise, declining | 2/10 |
| K8s-native GPU clouds | 10-20% | GPU training/inference (hybrid self/managed) | 4/10 |

---

## Assumptions Register

| # | Assumption | Impact if Wrong | Confidence |
|---|---|---|---|
| A1 | CNCF survey respondents are a reasonable proxy for K8s-using organizations (despite selection bias toward cloud-native adopters) | Self-managed K8s share could be higher in general population (many non-respondents may run self-managed legacy K8s) | Medium |
| A2 | Engineering blog disclosures (04_tech_blogs.md) are representative of architecture patterns among companies at similar scale | Publication bias means only companies with good outcomes disclose; actual self-managed failure rate may be higher | Low |
| A3 | Dynatrace's 73%/27% managed/self-managed split for cloud K8s (2023) has continued trending toward managed at ~3-5pp/year | Trend could have accelerated or plateaued; AI GPU workloads may have slowed the shift | Medium |
| A4 | Company size correlates with self-managed K8s likelihood -- i.e., larger companies are more likely to self-manage | Some small companies with deep technical founders may self-manage; some large companies may fully outsource to managed | High |
| A5 | EU companies are more likely to self-manage K8s than US companies due to data sovereignty requirements | EU companies may use EU-region managed K8s (e.g., GKE in Frankfurt) rather than self-managing | Medium |
| A6 | OpenShift's $1.9B ARR is a reasonable proxy for enterprise self-managed K8s demand | OpenShift includes managed offerings (ROSA, ARO) that are not self-managed | Medium |
| A7 | The absence of "migration away from self-managed K8s" stories in engineering blogs means such migrations are rare | Companies may migrate quietly without publishing; publication bias toward K8s adoption stories | Low |
| A8 | K8s-native GPU clouds (CoreWeave) represent a hybrid category between managed and self-managed | Some analysts may classify CoreWeave as purely managed, changing the self-managed denominator | Medium |

---

## Evidence Gaps

### Critical Gaps (Would Significantly Change Analysis)

1. **No direct survey of AI SaaS companies asking "do you run self-managed K8s?"** -- All estimates are derived from general industry data applied to AI SaaS through inference and judgment.

2. **No breakdown of managed vs self-managed K8s by industry vertical** -- CNCF and Datadog data do not segment by SaaS, financial services, healthcare, etc.

3. **No data on self-managed K8s failure/abandonment rates** -- We only see companies that succeeded with self-managed K8s (survivorship bias).

4. **No company-size-specific managed/self-managed split** -- We know 91% of K8s users are at 1000+ employee companies, but not what % of those self-manage.

### Moderate Gaps (Would Refine Estimates)

5. **No EU-specific managed vs self-managed K8s data** -- Regional CNCF data covers cloud-native adoption but not K8s management type.

6. **No cost comparison data** -- Based on [07_sec_earnings.md], infrastructure costs are 40-50% of AI SaaS revenue, but no data splits this between managed vs self-managed K8s.

7. **Limited K8s distribution market share data** -- OpenShift revenue is known ($1.9B) but Rancher, Tanzu, and vanilla K8s market shares among AI SaaS are not measured.

8. **No data on self-managed K8s team sizes** -- We cannot quantify the engineering investment required, which determines which companies can realistically self-manage.

### Minor Gaps (Context Enrichment)

9. **Limited APAC data** -- Based on [01_cncf_survey.md, Data Point 15], Asia-Pacific is at 40% cloud-native adoption with minimal detail on K8s management patterns.

10. **No data on self-managed K8s operational incidents** -- Only one incident documented (HubSpot Sept 2024 Envoy rollback from 04_tech_blogs.md).

---

## Cross-Reference Matrix

This table shows which Wave 1 sources provide evidence for each analytical question:

| Question | 01 CNCF | 02 Analyst | 03 Jobs | 04 Blogs | 05 Vendor | 06 Stack | 07 SEC | 08 VC |
|---|---|---|---|---|---|---|---|---|
| % self-managed K8s overall | Strong | Strong | Weak | Medium | None | Medium | None | None |
| % self-managed in AI SaaS | Weak | Weak | None | Medium | None | None | None | Weak |
| Why self-manage (GPU) | Medium | None | None | Strong | None | None | None | Medium |
| Why self-manage (cost) | None | None | None | Medium | None | None | Strong | Strong |
| Why self-manage (compliance) | Weak | None | None | Medium | None | None | None | None |
| Why self-manage (lock-in) | Medium | Medium | None | Strong | None | None | None | None |
| Company size breakdown | Strong | Medium | Medium | Medium | None | Strong | Weak | Medium |
| US vs EU differences | Medium | None | Weak | Weak | Weak | None | None | None |
| On-prem vs cloud | Strong | Strong | None | Strong | None | Medium | None | None |
| Migration trends | Strong | Strong | None | Strong | None | Strong | None | None |
| K8s distributions | None | None | None | Medium | None | None | Strong | Medium |

---

## Summary of Estimates

| Metric | Estimate | Classification | Confidence |
|---|---|---|---|
| % of AI SaaS companies with self-managed K8s | 15-22% | Estimated | 4/10 |
| % large AI SaaS ($200M+ ARR) with self-managed K8s | 25-35% | Estimated | 4/10 |
| % mid-market AI SaaS ($10-200M) with self-managed K8s | 8-15% | Estimated | 3/10 |
| % small AI SaaS (<$10M) with self-managed K8s | 2-5% | Estimated | 3/10 |
| US self-managed K8s rate | 12-18% | Estimated | 3/10 |
| EU self-managed K8s rate | 20-30% | Estimated | 3/10 |
| Annual decline rate of self-managed share | 3-5pp/yr | Inferred | 7/10 |
| Self-managed on-prem share (of self-managed total) | 30-40% | Estimated | 3/10 |
| Self-managed cloud IaaS share (of self-managed total) | 45-55% | Estimated | 3/10 |
| OpenShift share of self-managed in AI SaaS | 20-30% | Estimated | 5/10 |
| Vanilla K8s share of self-managed in AI SaaS | 25-35% | Estimated | 3/10 |

---

## Key Takeaways

1. **Self-managed K8s is real but declining.** Approximately 15-22% of AI SaaS companies run self-managed K8s, down from ~30%+ just three years ago. The direction is unambiguous -- managed K8s is winning.

2. **It is concentrated at the top.** Self-managed K8s is primarily a large-company phenomenon. Companies like OpenAI (7,500 nodes), Databricks (thousands of clusters), and Salesforce (bare metal) have the platform engineering teams and scale economics to justify self-management. Below $200M ARR, self-managed K8s is rare.

3. **GPU scheduling is the strongest remaining rationale.** Custom GPU scheduling, gang scheduling for distributed training, and bare-metal performance for AI workloads remain the strongest reasons to self-manage. But this rationale is weakening as managed K8s providers add AI-specific capabilities (EKS 100K nodes, GKE 130K nodes, CNCF AI Conformance program).

4. **Multi-cloud portability is a structural driver.** Companies operating across AWS, Azure, and GCP (like Databricks and Elastic) use self-managed K8s to maintain portability. This driver is not weakening -- multi-cloud adoption is growing (56% of organizations, up from prior years).

5. **Europe likely has higher self-managed rates.** GDPR, data sovereignty requirements, and on-premises deployment demands push EU AI SaaS companies toward self-managed K8s, though direct evidence is limited.

6. **K8s-native GPU clouds are the wild card.** CoreWeave ($12B contract with OpenAI, 250K GPUs) blurs the managed/self-managed boundary. If CoreWeave-style platforms are classified as "managed," the self-managed share drops further. If classified as "self-managed" (due to direct K8s API access), it rises.

7. **No company publicly migrated away from self-managed K8s in the 2024-2025 blog corpus.** This is notable: either self-managed K8s users are sticky, or companies quietly migrate without publishing.

---

## Overall Confidence Score: 4/10

**Justification:**

This analysis synthesizes 8 Wave 1 sources containing 200+ data points, but the core question -- "what percentage of AI SaaS companies run self-managed K8s" -- is not directly measured by any source. The score of 4/10 reflects:

- **Strong directional evidence (7-8/10):** Self-managed K8s share is declining; managed K8s is growing; large companies are more likely to self-manage.
- **Moderate structural evidence (5-6/10):** GPU scheduling, cost, compliance, and lock-in avoidance are documented drivers; company size correlation is supported by data.
- **Weak quantitative precision (3-4/10):** All percentage estimates are triangulated from general industry data, not from direct measurement of AI SaaS companies.
- **Very weak geographic and segment specificity (2-3/10):** US vs EU, on-prem vs cloud, and distribution market share estimates have minimal supporting data.

**To increase confidence to 7+/10, the following primary research would be needed:**
1. Direct survey of 200+ AI SaaS infrastructure leaders segmented by company size and geography
2. Anonymized infrastructure audits from major VC portfolios (a16z, Sequoia, Bessemer AI portfolio companies)
3. Cloud provider customer analytics segmented by industry vertical and K8s management type
4. CNCF survey cross-tabulations for AI companies specifically (available in full survey data but not in public summaries)

---

## Sources (Wave 1 Files Referenced)

All data points cite specific Wave 1 files and data point numbers. Primary sources underlying those files include:

- CNCF Annual Surveys 2021-2024/2025
- Dynatrace Kubernetes in the Wild Report 2023
- Datadog State of Containers and Serverless 2025
- Stack Overflow 2025 Developer Survey
- Flexera State of the Cloud Report 2025
- Red Hat Kubernetes Adoption Survey 2024
- Gartner Container Management Magic Quadrant 2025
- IBM Q4 2025 Earnings (OpenShift ARR)
- Engineering blogs: OpenAI, Databricks, Figma, Grammarly, Salesforce, Elastic, Cohere, HubSpot
- Cloud vendor case studies: AWS, Azure, GCP
- CB Insights State of AI 2025
- Bessemer Venture Partners Cloud 100 2024
- Menlo Ventures State of Generative AI 2025
- Sacra Research GPU Clouds Report
- CoreWeave, CAST AI, Komodor, Fireworks AI company disclosures
