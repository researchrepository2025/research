# F63: Staffing & Expertise Requirements
## On-Premises vs. Cloud-Native ISV Delivery

---

## Executive Summary

Building and delivering on-premises AI-enabled software demands a fundamentally different and significantly larger staffing profile than cloud-native delivery. An ISV operating in the on-premises model must employ — or contract — roles that simply do not exist in a cloud-native organization: GPU infrastructure specialists, field deployment engineers, network engineers capable of operating in customer-controlled environments, and security engineers proficient in air-gapped or zero-trust on-premises architectures. The talent market for these roles is acutely constrained: a global shortage of approximately 85,000 GPU engineers exists against annual demand of 97,000, while Kubernetes platform engineers command average North American salaries of $170,568 in 2025. Infrastructure and operations roles are reported as the hardest category to hire for by 36% of IT organizations. Beyond raw scarcity, retention is structurally difficult: 68% of all Kubernetes jobs offer remote work, and engineers with cloud-native skills consistently command more interesting work, greater flexibility, and higher market premiums — making on-premises-focused roles a harder sell in a market where 1 in 3 tech professionals changed jobs in the past two years.

---

## 1. Role Inventory: On-Premises Roles Without Cloud-Native Equivalents

On-premises AI software delivery requires a set of roles that are either entirely absent or radically reduced in a cloud-native ISV. The table below maps these role categories.

| Role Category | On-Premises Required | Managed K8s Required | Cloud-Native Required |
|---|---|---|---|
| GPU Infrastructure Engineer | Yes — full-time per cluster | Partial (cluster config only) | No (managed by cloud provider) |
| Field Deployment / Forward Deployed Engineer | Yes — embedded at customer sites | Rare | Rare |
| Network Engineer (BGP, firewall, VPN) | Yes — per customer environment | Partial (cluster networking) | No |
| Hardware Lifecycle Specialist | Yes | No | No |
| Release Engineer (multi-target packaging) | Yes — per OS/hardware target | Partial | Minimal |
| On-Premises Security Engineer | Yes — per regulatory environment | Partial | Minimal (cloud-native security tools) |
| Customer Environment Specialist / Solutions Architect | Yes — deep customer infra knowledge | Partial | Light-touch |
| DBA (self-managed database operations) | Yes — per deployment | Partial | No (managed DBaaS) |

### Forward Deployed Engineers (FDEs)

The "Forward Deployed Engineer" role has emerged as a formalized function that combines software engineering with deep on-site customer deployment work. Job postings for this role [surged more than 800% between January and September 2025](https://beam.ai/agentic-insights/agent-deployment-engineers-the-evolution-of-deployment-roles-in-enterprise-software). These engineers own the full lifecycle of customer solutions from discovery and scoping through build, deployment, and post-launch iteration. Companies like [Palantir expect approximately 25% of FDE time to be spent on-site with customers](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers), while healthcare-sector deployments can require up to 50% on-site presence.

### Release Engineers for Multi-Target Delivery

On-premises software must be packaged for heterogeneous target environments — different Linux distributions, hardware configurations, air-gapped networks, and customer-mandated version constraints. Google's SRE book documents that [release engineers work with software engineers to define all the steps required to release software, from source code storage to build rules, testing, packaging, and deployment](https://sre.google/sre-book/release-engineering/). In cloud-native delivery, this complexity collapses to a single target environment managed by the ISV.

---

## 2. Skill Depth Requirements for On-Premises Delivery

### 2.1 GPU Infrastructure Expertise

On-premises AI delivery involving GPU-accelerated inference or training requires a dedicated, multi-level team. The [NVIDIA AI Infrastructure Professional (NCP-AII) certification](https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-professional/) requires candidates to demonstrate 2–3 years of operational experience in a data center with NVIDIA hardware. The exam tests proficiency in: GPU and DPU installation, hardware validation, system optimization for AI and HPC workloads, MIG configuration, BlueField DPU operating system deployment, and integration of NVIDIA's cloud-native stack with Docker and NVIDIA NGC.

Skill levels required by tier, per [Introl's GPU infrastructure team analysis](https://introl.com/blog/ai-infrastructure-team-nvidia-certification-2025):

| Level | Experience | Skills Required |
|---|---|---|
| Foundation (L1) | 0–6 months | Basic Linux administration, networking fundamentals, hardware concepts, basic CUDA |
| Operational (L2) | 6–12 months | GPU driver management, basic cluster operations, monitoring setup, single-node deployment |
| Professional (L3) | 1–2 years | Multi-node cluster management, advanced CUDA, performance tuning |
| Expert (L4) | 2–4 years | Architecture design, large-scale optimization, custom kernel development |
| Architect (L5) | 4+ years | Enterprise-scale infrastructure strategy, data center design |

### 2.2 Kubernetes Operations Expertise

For on-premises deployments using self-managed Kubernetes, the [kube.careers Q2 2025 State of Kubernetes Jobs report](https://kube.careers/state-of-kubernetes-jobs-2025-q2) identifies the in-demand technical stack: Docker (60.62% of job postings), Python (62%), Go (36%), CI/CD pipelines (GitLab 31%, Jenkins 29%), and observability tooling (Prometheus 21%, Grafana 20%, Datadog 14%). These are not entry-level skills. The [Outplane cloud-native architecture guide](https://outplane.com/blog/cloud-native-architecture-small-teams) notes that "managing a production Kubernetes cluster requires 2 to 3 full-time engineers on average" and that "Kubernetes proficiency requires 6 to 12 months" to develop.

### 2.3 Networking Expertise

On-premises enterprise deployments require network engineers capable of operating in customer-controlled network environments with routing protocols, security policies, and compliance constraints the ISV does not control. Required skills include BGP routing, OSPF, VPN configuration, firewall management (Cisco Firepower, ASA), and network segmentation. [BGP Network Engineer positions in 2025 range from $89,000 to $175,000](https://www.ziprecruiter.com/Jobs/Bgp-Network-Engineer), with Cisco CCNP or CCIE certification typical for senior roles. The [average CCIE-certified engineer salary is $145,000](https://blog.cloudmylab.com/network-engineer-certifications-career-paths).

### 2.4 Database Administration Expertise

Self-hosted database instances in customer environments require hands-on DBA expertise for tuning, backup, recovery, and patch management — tasks fully abstracted by managed database services (RDS, Cloud SQL, Azure Database) in cloud-native delivery. [The average DBA salary in the United States as of December 2025 is $107,875](https://www.salary.com/research/salary/listing/database-administrator-salary), with MS SQL Server DBA specialists ranging from $105,000 to $110,000 annually. On-premises deployments typically require at least 0.5 FTE DBA coverage per major customer environment.

### 2.5 Security Engineering Expertise

On-premises AI deployments for regulated industries require security engineers with deep knowledge of network segmentation, identity and access management, air-gapped environments, and zero-trust architectures. [Zero Trust Engineer positions in 2025 range from $63,000 to $200,000](https://www.ziprecruiter.com/Jobs/Zero-Trust-Engineer), with typical compensation for experienced professionals between $104,000 and $166,000. The [ISC2 2025 Cybersecurity Workforce Study](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study) reports that 59% of organizations have critical or significant cybersecurity skills shortages (up from 44% in 2024), and 88% experienced at least one significant security event due to skills shortages. Cloud security and AI security are now cited as the two most critical skill needs.

---

## 3. Market Scarcity and Salary Benchmarks

### 3.1 GPU Infrastructure Engineers

[FACT] [An 85,000 GPU engineer shortage exists globally, with NVIDIA certifying only 12,000 engineers annually against an annual demand of 97,000](https://introl.com/blog/ai-infrastructure-team-nvidia-certification-2025).

[STATISTIC] GPU infrastructure salary ranges by level (United States, 2025), per [Introl](https://introl.com/blog/ai-infrastructure-team-nvidia-certification-2025):

| Level | Salary Range |
|---|---|
| Foundation (L1) | $75,000–$95,000 |
| Operational (L2) | $95,000–$125,000 |
| Professional (L3) | $125,000–$175,000 |
| Expert (L4) | $175,000–$250,000 |
| Architect (L5) | $250,000–$400,000 |

[FACT] [Organizations are offering premium pay 15–25% above market rates with annual retention bonuses tied to team stability to compete for GPU infrastructure talent](https://introl.com/blog/ai-infrastructure-team-nvidia-certification-2025).

[STATISTIC] [NVIDIA's 2025 job postings show base salary ranges of $104,000–$172,500 for Level 1 positions and $120,000–$189,750 for Level 2 positions](https://jobs.anitab.org/companies/nvidia/jobs/59811167-gpu-and-hpc-infrastructure-engineer-new-college-grad-2025).

### 3.2 Kubernetes / Platform Engineers

[STATISTIC] [Average Kubernetes job salary in North America for Q2 2025: $170,568 (range: $141,280 minimum to $199,856 maximum)](https://kube.careers/state-of-kubernetes-jobs-2025-q2).

[STATISTIC] [56% of North American Kubernetes jobs pay between $100,000 and $180,000; 28% pay between $180,000 and $240,000; 6.88% pay between $240,000 and $300,000; 2.47% pay above $300,000](https://kube.careers/state-of-kubernetes-jobs-2025-q2).

[STATISTIC] [Platform engineers receive the highest average Kubernetes-related salary at $172,038, which is approximately 20% higher than DevOps roles and 14% higher than software engineer roles](https://kube.careers/state-of-kubernetes-jobs-2025-q2).

### 3.3 Network Engineers

[STATISTIC] [Median total pay for a network engineer in 2025 is $122,000 according to Glassdoor](https://www.coursera.org/articles/network-engineer-salary). BGP specialist roles range from $89,000 to $175,000, with positions in high-cost markets (e.g., Sunnyvale, CA) reaching $104,000–$225,000.

### 3.4 Security Engineers

[STATISTIC] [Cybersecurity engineers in 2025 have compensation ranging from $116,000 to $143,000, plus bonuses and stock options](https://www.refontelearning.com/blog/how-much-can-you-earn-in-cybersecurity). Zero-trust architect roles command $104,000–$200,000. The [U.S. Bureau of Labor Statistics projects a 32% increase in cybersecurity positions through 2032](https://www.ziprecruiter.com/Jobs/Zero-Trust-Engineer).

### 3.5 Database Administrators

[STATISTIC] [Average DBA salary in the United States as of December 2025: $107,875 per year ($52/hour), per Salary.com](https://www.salary.com/research/salary/listing/database-administrator-salary). Glassdoor reports $105,618. Senior MS SQL Server DBA specialists earn $105,000–$110,000 at the 25th–75th percentile.

---

## 4. Team Size: Minimum Viable Staffing Comparison

The following estimates assume a mid-size ISV serving 25–50 enterprise customers, with a mix of regulated and non-regulated sectors. FTE ranges reflect active work only; on-call burden is listed separately.

### 4.1 On-Premises ISV Delivery — Minimum Viable Team

| Role | FTE Range | On-Call Burden | Notes |
|---|---|---|---|
| GPU Infrastructure Engineer | 1.0–2.0 | 0.25 FTE | Required for each unique hardware platform |
| Field Deployment / Forward Deployed Engineer | 2.0–4.0 | 0.5 FTE | Palantir model: ~25% on-site; healthcare: ~50% |
| Release / Packaging Engineer | 1.0–2.0 | 0.1 FTE | Multi-target OS/hardware builds |
| Network Engineer (on-prem environments) | 1.0 | 0.25 FTE | Customer environment variability (see F61) |
| Security Engineer (on-prem/zero-trust) | 1.0–1.5 | 0.25 FTE | Regulated sector compliance requirements |
| DBA (self-hosted database operations) | 0.5–1.0 | 0.25 FTE | Per major database cluster managed |
| K8s Platform Engineer (self-managed) | 2.0–3.0 | 0.5 FTE | Per Outplane benchmark: 2–3 FTE per cluster |
| **Total (active work)** | **8.5–14.5 FTE** | **~2.1 FTE on-call** | Excludes product engineering, PM, QA |

Assumptions: 25–50 enterprise customers; 3–5 distinct hardware environments; regulated-sector presence (healthcare, finance, or government); 24/7 SLA required.

[FACT] [Managing a production Kubernetes cluster alone requires 2 to 3 full-time engineers on average; for a 10-person engineering team, that represents 20% of total engineering capacity](https://outplane.com/blog/cloud-native-architecture-small-teams).

[STATISTIC] [Two engineers managing Kubernetes represent $300,000 to $500,000 in annual salary costs — 10 to 20 person-months of engineering time that could build product features instead](https://outplane.com/blog/cloud-native-architecture-small-teams).

### 4.2 Cloud-Native ISV Delivery — Minimum Viable Team

| Role | FTE Range | On-Call Burden | Notes |
|---|---|---|---|
| Platform / DevOps Engineer | 1.0–2.0 | 0.25 FTE | Managed K8s or PaaS; provider handles control plane |
| Security Engineer (cloud-native) | 0.5–1.0 | 0.1 FTE | Cloud-native tooling (GuardDuty, Defender, SCC) |
| SRE / Reliability Engineer | 0.5–1.0 | 0.25 FTE | Monitoring, alerting, incident response |
| **Total (active work)** | **2.0–4.0 FTE** | **~0.6 FTE on-call** | Excludes product engineering, PM, QA |

[FACT] [For a team running fully on PaaS, 0 dedicated infrastructure engineers are required for the core infrastructure layer — freeing approximately one senior engineer's annual salary worth of capacity for product development](https://outplane.com/blog/cloud-native-architecture-small-teams).

The differential between on-premises and cloud-native minimum viable teams is approximately **6–11 additional FTE** for infrastructure and delivery functions alone, at an additional annual cost of approximately $900,000–$1.8 million in loaded compensation (assuming $150,000–$180,000 average fully-loaded cost per infrastructure engineer).

---

## 5. Training Investment: On-Premises vs. Cloud-Native

### 5.1 Cloud Certification Costs and ROI

Cloud certifications provide a relatively standardized, modular training path with measurable market ROI.

[STATISTIC] [AWS certification exam costs range from $100 (Cloud Practitioner) to $300 (Solutions Architect Professional)](https://timinsight.com/aws-azure-gcp-certifications-comparison-en/). Azure exams cost up to $165. GCP certifications are also in the $200–$300 range.

[STATISTIC] [A Forrester study commissioned by AWS found that AWS training and certification can provide up to a 234% ROI by upskilling an existing workforce](https://timinsight.com/aws-azure-gcp-certifications-comparison-en/).

[STATISTIC] [AWS and Azure certifications are valid for 3 years; GCP certifications are valid for 2 years](https://pluralsight.com/resources/blog/cloud/cloud-certification-faqs-aws-vs-azure-vs-google-cloud-certs-compared). Renewal paths exist and are often lower-cost than initial certification.

[STATISTIC] [2025 research indicates AWS AI certifications can bring salary increases of up to 47%](https://timinsight.com/aws-azure-gcp-certifications-comparison-en/).

### 5.2 On-Premises / GPU Infrastructure Training Costs

On-premises AI infrastructure training — particularly for GPU clusters — involves significantly higher investment with less standardized renewal cycles.

[STATISTIC] [NVIDIA AI infrastructure bootcamp cost: $15,000–$25,000 per participant](https://introl.com/blog/ai-infrastructure-team-nvidia-certification-2025). For a team of 4 covering a small GPU deployment (10–100 GPUs), total bootcamp investment is $60,000–$100,000.

[FACT] The [NVIDIA NCA-AIIO (Associate) certification](https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/) is valid for two years from issuance. The professional-level NCP-AII requires 2–3 years of hands-on data center experience before candidacy — meaning the training investment is largely time-in-role rather than courseware.

Hardware vendor certifications (Cisco CCIE for networking: typically $1,500+ for lab and exam fees; [Cisco CCNP recommended for enterprise network engineering](https://blog.cloudmylab.com/network-engineer-certifications-career-paths)) add further cost. Security certifications for on-premises roles (CISSP, CEH) add $500–$700 per exam plus preparatory training.

| Training Type | Approximate Cost per Engineer | Renewal Cycle |
|---|---|---|
| AWS/Azure/GCP Professional Cert | $200–$500 (exam) + prep | Every 2–3 years |
| NVIDIA NCP-AII (GPU Professional) | $15,000–$25,000 bootcamp + exam | Every 2 years |
| Cisco CCNP (Networking) | $1,500–$3,000 (exam + lab) | Every 3 years |
| CISSP (Security) | $700–$1,500 (exam + prep) | Every 3 years |
| On-premises DBA cert (Oracle/MS SQL) | $500–$2,000 | Every 2–3 years |

### 5.3 Technology Currency Problem

On-premises infrastructure stacks change at the hardware vendor's release cycle, which is decoupled from software release cycles. GPU architectures (e.g., H100 to B200 transitions), networking silicon generations, and firmware compatibility matrices require ongoing training investment not captured in certification renewal cycles alone. Cloud-native infrastructure, by contrast, abstracts these changes behind managed APIs, reducing the ISV's training burden.

---

## 6. Outsourcing Options: Managed Services and Consulting Partners

### 6.1 Managed IT Services Pricing (General)

[STATISTIC] [Average managed IT services cost in 2025: $100–$149 per user per month for standard packages; $150–$400 per user per month for comprehensive packages including 24/7 support, advanced cybersecurity, and IT consulting](https://www.sterling-technology.com/blog/managed-it-services-pricing).

[STATISTIC] [Per-device pricing for on-premises infrastructure managed services: $100–$400 per server; $50–$100 per workstation; $30–$75 per firewall; $15–$40 per switch](https://thenetworkinstallers.com/blog/managed-it-services-cost/).

[STATISTIC] [Outsourcing IT services through managed service providers is typically 25–45% cheaper than maintaining equivalent in-house IT capabilities; a basic two-person in-house IT department costs approximately $185,000 annually (before infrastructure and tools), while managed services providing equivalent coverage costs $60,000–$84,000 yearly for a 50-employee company](https://thenetworkinstallers.com/blog/managed-it-services-cost/).

### 6.2 On-Premises AI Infrastructure — Outsourcing Limitations

For general IT managed services, outsourcing is cost-effective. However, specialized on-premises AI infrastructure support has significant limitations:

- **GPU cluster expertise**: The 85,000-engineer shortage means that MSPs with certified GPU infrastructure capabilities are rare. Most general MSPs cannot support NVIDIA HGX or DGX deployments.
- **Customer site access**: On-premises deployments in air-gapped or regulated environments (defense, healthcare, finance) often prohibit third-party MSP access, requiring the ISV to maintain in-house clearance-eligible or credentialed staff.
- **Deep product integration**: Tier-2/3 support for on-premises AI applications requires engineers who understand both the ISV's product internals and the customer's infrastructure — a combination unlikely to be available through a general MSP.

[FACT] [On-premises infrastructure adds cost to managed services because providers must send engineers on-site, increasing expense for the ISV or customer versus cloud-only engagements](https://www.sterling-technology.com/blog/managed-it-services-pricing).

### 6.3 System Integrators and Consulting Partners

Large system integrators (Accenture, Deloitte, SAIC, Leidos, Booz Allen Hamilton) operate practices for on-premises enterprise software deployment, particularly in regulated industries. [SAIC's Senior Network Engineer roles in 2025 require active security clearances and command $130,000+ for cleared, on-premises network engineering](https://jobs.saic.com/jobs/16305692-senior-network-engineer). These rates add a premium of 2–3x over base salary when engaged as third-party consultants.

---

## 7. Talent Retention: Structural Difficulty of On-Premises Teams

### 7.1 Market-Wide Retention Context

[STATISTIC] [ISACA's 2025 Tech Workplace and Culture Survey (7,726 respondents globally) found that 1 in 3 (33%) technology professionals changed jobs in the past two years; 74% of organizations are concerned about attracting and retaining tech talent](https://www.isaca.org/about-us/newsroom/press-releases/2025/1-in-3-tech-pros-switched-jobs-leaving-74-of-firms-worried-about-it-talent-retention).

[STATISTIC] [Top reasons technology professionals stay in roles: work-life balance (41%), hybrid/remote work options (40%), enjoying job duties (37%), interesting work (36%), compensation (34%) — ISACA 2025](https://www.isaca.org/about-us/newsroom/press-releases/2025/1-in-3-tech-pros-switched-jobs-leaving-74-of-firms-worried-about-it-talent-retention).

[STATISTIC] [42% of IT professionals are actively or passively seeking new roles, per Info-Tech Research Group's IT Talent Trends 2025 report (survey of 500+ IT professionals)](https://www.infotech.com/research/42-of-it-professionals-are-exploring-new-jobs-it-talent-trends-2025-report-from-info-tech-research-group-spotlights-retention-risks-and-opportunities).

[STATISTIC] [Job-change rates by age group: Under 35: 42%; Ages 35–44: 35%; Ages 45–54: 29% — ISACA 2025](https://www.isaca.org/about-us/newsroom/press-releases/2025/1-in-3-tech-pros-switched-jobs-leaving-74-of-firms-worried-about-it-talent-retention).

### 7.2 On-Premises Work as a Retention Disadvantage

On-premises ISV delivery creates compounding retention risks:

**Remote work restrictions**: [68% of all Kubernetes jobs allow some form of remote work](https://kube.careers/state-of-kubernetes-jobs-2025-q2). On-premises deployment roles — particularly field deployment engineers and customer environment specialists — frequently require on-site presence, directly conflicting with the top retention driver (work-life balance, 41%) and second-ranked driver (hybrid/remote options, 40%).

**Repetitive infrastructure toil**: [64% of engineers report that repetitive infrastructure tasks sap their energy and creativity; 47% say DevOps overload contributes directly to burnout or frustration — DuploCloud AI + DevOps Report 2025 (135+ engineers, platform leads, and CTOs surveyed)](https://duplocloud.com/blog/burnout-by-a-thousand-tickets/). On-premises deployments are disproportionately toil-heavy: manual patching, hardware maintenance, and environment-specific configuration drift all generate repetitive work that cloud-native automation eliminates.

**Burnout from on-call burden**: [The Catchpoint 2025 report indicates that almost 70% of SREs report that on-call stress impacted burnout and attrition](https://devops.com/aiops-for-sre-using-ai-to-reduce-on-call-fatigue-and-improve-reliability/). On-premises deployments spread on-call burden across more diverse failure modes (hardware, networking, OS, application) than cloud-native deployments, where the provider absorbs infrastructure failure detection.

**Skills market signal**: [36% of IT organizations report that infrastructure and operations roles are the most difficult to hire for, per Info-Tech Research Group 2025](https://www.infotech.com/research/42-of-it-professionals-are-exploring-new-jobs-it-talent-trends-2025-report-from-info-tech-research-group-spotlights-retention-risks-and-opportunities). Engineers who have invested in on-premises infrastructure skills (CCIE, NVIDIA NCP-AII, clearance-required roles) know they command premiums but also know those skills are transferable to larger system integrators, defense contractors, and cloud providers who can offer better compensation and more modern work environments.

### 7.3 Career Preference Signal

[STATISTIC] [Over 85% of DevOps/SRE respondents report working on the cloud or currently migrating; less than 15% work strictly on premises — DuploCloud Platform Engineering Survey](https://duplocloud.com/blog/platform-engineering-survey-summary/). This signals that the majority of actively employed infrastructure engineers have oriented their careers toward cloud-native work and may view on-premises-heavy ISV roles as a career step backward.

---

## 8. Geographic Considerations

### 8.1 On-Premises Delivery Requires Geographic Presence

On-premises enterprise AI software delivery introduces two geographic staffing requirements that cloud-native delivery does not:

**Customer time zone coverage**: [ISVs with on-premises customer bases spanning multiple time zones require staff working 24/7 to monitor and address issues as they arise](https://www.graphon.com/blog/isv-hosting-options). A cloud-native ISV can centralize operations teams in a single time zone and use automated alerting and self-healing infrastructure to cover off-hours. An on-premises ISV must either staff follow-the-sun teams or pay on-call premiums.

**Physical site access**: Regulated-sector on-premises deployments frequently require security clearances, health sector credentialing, or in-country citizenship requirements. [FDE roles at some defense-adjacent companies require visits to unconventional workplaces including factory floors and air-gapped environments](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers). These requirements eliminate remote hiring from lower-cost geographies.

**GDPR and data residency**: [Regulations like GDPR require certain data to remain within specific geographic boundaries](https://www.houseblend.io/articles/on-premise-hybrid-erp-2025), meaning on-premises deployments in the EU require locally-based support staff capable of operating in-country — adding geographic fragmentation to staffing costs.

### 8.2 Cloud-Native Delivery Enables Centralized Operations

Cloud-native ISVs can operate globally from a single operations center, with support engineers working in one time zone handling incidents across all customer tenants. [Kubernetes jobs allow remote work in 68% of postings, with North America dominating at 66.89% of all positions](https://kube.careers/state-of-kubernetes-jobs-2025-q2). This geographic flexibility enables cloud-native ISVs to hire from lower-cost markets, use asynchronous operations practices, and avoid the headcount multiplication that multi-time-zone on-premises support requires.

---

## 9. Difficulty Rating Summary

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **GPU Infrastructure Staffing** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Requires: NVIDIA-certified specialists, hardware ops, firmware management | Requires: GPU node management, cluster config | Cloud provider manages GPU hardware |
| | Tools: NVIDIA DCGM, InfiniBand, NCCL | Tools: NVIDIA device plugins, K8s node labels | Services: AWS Trainium, Azure NDv5, GCP A3 |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.0–0.25 |
| **Network Engineering** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Requires: Customer-env BGP, firewall expertise | Requires: CNI config, service mesh | Cloud provider manages networking |
| | Tools: Cisco IOS, Juniper JunOS, Palo Alto | Tools: Calico, Cilium, Istio | Services: VPC, Security Groups, Cloud Load Balancers |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **Field Deployment / FDE** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Requires: On-site customer embedding, travel, environment variability | Rare; mostly remote deployment | Minimal; tenant onboarding only |
| | Est. FTE: 2.0–4.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |
| **Security Engineering** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Requires: Zero-trust, air-gap, compliance per customer | Requires: K8s RBAC, network policy, compliance | Cloud-native security services with policy config |
| | Est. FTE: 1.0–1.5 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |
| **Database Operations** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted per customer; manual backup/recovery | Self-hosted in cluster; operator-managed | Fully managed DBaaS |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **Release Engineering** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Multi-target OS/hardware packaging | Container-based; single artifact type | Single artifact; cloud provider CI/CD |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |

---

## Key Takeaways

- **On-premises AI delivery requires 6–11 additional infrastructure and delivery FTE** compared to a cloud-native ISV of equivalent scale, at an estimated incremental annual cost of $900,000–$1.8 million in compensation alone — before travel, tooling, and on-call premiums.
- **GPU infrastructure talent is the scarcest and most expensive specialized role**: an 85,000-engineer global shortage, annual demand exceeding NVIDIA's certification throughput by 8x, and architect-level salaries reaching $400,000 make this the highest-risk staffing dependency for on-premises AI delivery.
- **Retention is structurally harder in on-premises roles**: the two top reasons engineers stay in jobs — remote/hybrid work and work-life balance — are directly undermined by on-site customer deployment requirements, with 68% of K8s jobs offering remote work versus the on-premises deployment reality.
- **Training investment for on-premises infrastructure runs 10–50x higher per engineer** than cloud certification paths: $15,000–$25,000 for GPU infrastructure bootcamps versus $200–$500 for cloud certification exams, with on-premises certifications requiring 2–3 years of hands-on experience as a prerequisite.
- **Outsourcing provides partial relief only**: general MSPs can absorb commodity on-premises IT management at 25–45% lower cost than in-house, but specialized AI GPU infrastructure, regulated-sector compliance, and deep product integration requirements cannot realistically be outsourced — requiring the ISV to maintain in-house capability regardless.

---

## Related — Out of Scope

- Operational staffing and support ticket handling for on-premises customer environments: See [F61: Support Burden & Customer Environment Variability]
- Engineering allocation impacts and time-to-market effects of infrastructure staffing burden: See [F64: Time-to-Market & Competitive Dynamics]
- Operational monitoring, observability tooling, and SRE practices by deployment model: See [F59: Operate & Monitor Differences]
- Business economics of on-premises vs. cloud-native delivery (cost structures, margin impacts): See [F64–F66]

---

## Sources

- [ISV Hosting Options in 2025 — GO-Global / GraphOn](https://www.graphon.com/blog/isv-hosting-options)
- [AI Infrastructure Capacity Planning: GPU Requirements 2025–2030 — Introl Blog](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030)
- [NVIDIA Certification 2025: Build Your AI Team — Introl Blog](https://introl.com/blog/ai-infrastructure-team-nvidia-certification-2025)
- [GPU and HPC Infrastructure Engineer New College Grad 2025 — NVIDIA / AnitaB.org](https://jobs.anitab.org/companies/nvidia/jobs/59811167-gpu-and-hpc-infrastructure-engineer-new-college-grad-2025)
- [NVIDIA AI Infrastructure Professional (NCP-AII) Certification](https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-professional/)
- [NVIDIA AI Infrastructure and Operations Associate (NCA-AIIO) Certification](https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/)
- [New NVIDIA Certifications — NVIDIA Blog](https://blogs.nvidia.com/blog/professional-certification-ai-infrastructure-operations/)
- [State of Kubernetes Jobs Q2 2025 — kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q2)
- [State of Kubernetes Jobs Q1 2025 — kube.careers](https://kube.careers/state-of-kubernetes-jobs-2025-q1)
- [Cloud-Native Architecture for Small Teams — Outplane](https://outplane.com/blog/cloud-native-architecture-small-teams)
- [Agent Deployment Engineers in Enterprise — Beam.ai](https://beam.ai/agentic-insights/agent-deployment-engineers-the-evolution-of-deployment-roles-in-enterprise-software)
- [What are Forward Deployed Engineers — Pragmatic Engineer Newsletter](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)
- [Google SRE Book: Release Engineering](https://sre.google/sre-book/release-engineering/)
- [BGP Network Engineer Jobs — ZipRecruiter](https://www.ziprecruiter.com/Jobs/Bgp-Network-Engineer)
- [Network Engineer Salary 2026 Guide — Coursera](https://www.coursera.org/articles/network-engineer-salary)
- [Network Engineer Certifications and Career Paths — CloudMyLab](https://blog.cloudmylab.com/network-engineer-certifications-career-paths)
- [Database Administrator Salary — Salary.com (December 2025)](https://www.salary.com/research/salary/listing/database-administrator-salary)
- [Database Administrator (DBA) with MS SQL Server — PayScale](https://www.payscale.com/research/US/Job=Database_Administrator_(DBA)/Salary/38d7acea/Microsoft-SQL-Server)
- [Zero Trust Engineer Jobs — ZipRecruiter](https://www.ziprecruiter.com/Jobs/Zero-Trust-Engineer)
- [Cybersecurity Salary Benchmarks 2025 — Refonte Learning](https://www.refontelearning.com/blog/how-much-can-you-earn-in-cybersecurity)
- [2025 ISC2 Cybersecurity Workforce Study](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)
- [ISACA: 1 in 3 Tech Pros Switched Jobs — Press Release 2025](https://www.isaca.org/about-us/newsroom/press-releases/2025/1-in-3-tech-pros-switched-jobs-leaving-74-of-firms-worried-about-it-talent-retention)
- [ISACA Tech Workplace and Culture 2025 Report](https://www.isaca.org/resources/reports/tech-workplace-and-culture-2025-report)
- [42% of IT Professionals Exploring New Jobs — Info-Tech Research Group 2025](https://www.infotech.com/research/42-of-it-professionals-are-exploring-new-jobs-it-talent-trends-2025-report-from-info-tech-research-group-spotlights-retention-risks-and-opportunities)
- [Burnout by a Thousand Tickets — DuploCloud AI + DevOps Report 2025](https://duplocloud.com/blog/burnout-by-a-thousand-tickets/)
- [Platform Engineering Survey — DuploCloud](https://duplocloud.com/blog/platform-engineering-survey-summary/)
- [AIOps for SRE: On-Call Fatigue — DevOps.com / Catchpoint 2025](https://devops.com/aiops-for-sre-using-ai-to-reduce-on-call-fatigue-and-improve-reliability/)
- [Cloud Certifications 2025: AWS vs Azure vs GCP — TimInsight](https://timinsight.com/aws-azure-gcp-certifications-comparison-en/)
- [Cloud Certification FAQs — Pluralsight](https://pluralsight.com/resources/blog/cloud/cloud-certification-faqs-aws-vs-azure-vs-google-cloud-certs-compared)
- [Managed IT Services Pricing 2025 — Sterling Technology](https://www.sterling-technology.com/blog/managed-it-services-pricing)
- [Managed IT Services Cost — The Network Installers](https://thenetworkinstallers.com/blog/managed-it-services-cost/)
- [ERP Deployment in 2025: On-Premise and Hybrid Models — Houseblend](https://www.houseblend.io/articles/on-premise-hybrid-erp-2025)
- [Robert Half: 2025 Tech and IT Job Market Outlook](https://www.roberthalf.com/us/en/insights/salary-hiring-trends/demand-for-skilled-talent/tech-it)
- [Robert Half: 2026 Technology Job Market — In-Demand Roles](https://www.roberthalf.com/us/en/insights/research/data-reveals-which-technology-roles-are-in-highest-demand)
- [SAIC Senior Network Engineer Job Listing (Washington, DC — 2025)](https://jobs.saic.com/jobs/16305692-senior-network-engineer)
- [Gartner: Top Trends Impacting Infrastructure and Operations for 2025](https://www.gartner.com/en/newsroom/press-releases/2024-12-11-gartner-identifies-the-top-trends-impacting-infrastructure-and-operations-for-2025)
- [State of Cloud Native Development Q1 2025 — CNCF](https://www.cncf.io/reports/state-of-cloud-native-development-q1-2025/)
