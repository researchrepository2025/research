# AI SaaS Infrastructure Architecture: Engineering Blogs & Conference Presentations

**Research Date:** 2026-02-12
**Source Type:** Engineering blogs, conference presentations, technical case studies
**Methodology:** Web search of public engineering disclosures from AI SaaS companies

---

## Executive Summary

Engineering blogs and conference presentations from 2024-2025 reveal that **Kubernetes (both managed and self-managed) is the dominant infrastructure pattern for AI SaaS companies**. 15+ companies publicly disclosed using Kubernetes-based architectures at scale. Direct quotes document cluster sizes ranging from hundreds to 7,500 nodes. Migration patterns show movement **toward Kubernetes** (Figma: ECS→K8s, Grammarly: EC2→EKS, HubSpot: EC2→K8s) rather than away from it. Scale metrics indicate operational maturity with companies running thousands of clusters managing millions of pods.

---

## Data Points

### [QUOTE] OpenAI - Kubernetes at 7,500 Nodes
**Source:** OpenAI Official Blog
**Date:** 2021 (still referenced in 2024-2025 content)
**URL:** https://openai.com/index/scaling-kubernetes-to-7500-nodes/

**Finding:**
"We've scaled Kubernetes clusters to 7,500 nodes, producing a scalable infrastructure for large models like GPT-3, CLIP, and DALL·E, but also for rapid small-scale iterative research such as Scaling Laws for Neural Language Models."

**Additional Facts:**
- [FACT] OpenAI's largest clusters have approximately 200,000 IP addresses in use at any one time
- [FACT] Primary use case is batch scheduling system with autoscaler for dynamic cluster scaling
- [FACT] Infrastructure built on Azure using Kubernetes for orchestration
- [FACT] Switched from Flannel to native Azure pod networking (Azure CNI) due to throughput scaling issues
- [FACT] Uses Prometheus for metrics collection and Grafana for visualization

**Relevance:** Demonstrates Kubernetes viability at extreme scale for frontier AI research
**Segment Applicability:** Evidence for Open Kubernetes viability for Large AI SaaS ($200M+ ARR)

---

### [STATISTIC] Databricks - Thousands of Kubernetes Clusters
**Source:** Databricks Engineering Blog
**Date:** 2024-2025
**URL:** https://www.databricks.com/blog/managing-cicd-kubernetes-authentication-using-operators

**Finding:**
"Databricks heavily uses Kubernetes to orchestrate containerized workloads for product microservices and data-processing jobs, running thousands of Kubernetes clusters and managing millions of pods across hundreds of product microservices."

**Additional Facts:**
- [FACT] Operates mix of self-managed and cloud-managed Kubernetes (EKS, AKS, GKE)
- [STATISTIC] Achieved 20% reduction in pod count across multiple services through intelligent load balancing
- [STATISTIC] Reduced time to upgrade each Kubernetes cluster by approximately 90%
- [STATISTIC] Incidents due to node upgrade system failures reduced by more than 95%
- [FACT] Service rotates thousands of tokens for hundreds of clusters on hourly basis (CI/CD authentication)

**Relevance:** Demonstrates hybrid managed/self-managed K8s strategy at enterprise scale
**Segment Applicability:** Evidence for Managed K8s + Open K8s hybrid for Large AI SaaS

---

### [MIGRATION] Figma - ECS to Kubernetes in 12 Months
**Source:** Figma Engineering Blog
**Date:** August 8, 2024
**URL:** https://www.figma.com/blog/migrating-onto-kubernetes/
**Author:** Ian VonSeggern, Software Engineering Manager

**Finding:**
"Figma migrated its compute platform from AWS ECS to Kubernetes (EKS) in less than 12 months with minimal customer impact."

**Reasons for Migration:**
- [QUOTE] "The move was dictated by pursuing cost savings, improved developer experience, and increased resiliency."
- [QUOTE] "Primarily to take advantage of the large ecosystem supported by the CNCF"
- [FACT] ECS limitations included lack of support for StatefulSets, Helm charts, and inability to easily run OSS software like Temporal

**Migration Strategy:**
- [FACT] Moved to three Kubernetes clusters for improved reliability
- [FACT] Used Karpenter (open-source CNCF project) for dynamic node scaling
- [FACT] Implemented incremental switchover using weighted DNS entries
- [FACT] Conducted load testing before production rollout

**Results:**
- [FACT] Migration completed by January 2024 for majority of highest priority services
- [FACT] Achieved cost savings by not over-provisioning for deploys
- [FACT] Improved reliability through multi-cluster deployment

**Relevance:** Direct evidence of migration FROM managed containers TO managed Kubernetes
**Segment Applicability:** Counter-evidence to "AI SaaS moving away from K8s" narrative

---

### [STATISTIC] Google Cloud - 130,000-Node GKE Cluster
**Source:** Google Cloud Engineering / WebProNews
**Date:** 2024-2025
**URL:** https://www.webpronews.com/googles-130000-node-kubernetes-colossus-engineering-the-future-of-ai-scale-computing/

**Finding:**
"Google Cloud engineered a record-shattering 130,000-node GKE cluster, doubling prior limits to meet AI's exascale demands."

**Performance Metrics:**
- [STATISTIC] API server QPS peaked at 500,000
- [STATISTIC] etcd writes at 100,000/sec
- [STATISTIC] Pod startup latency under 5 seconds cluster-wide

**Relevance:** Establishes upper bound for Kubernetes scaling in AI workloads
**Segment Applicability:** Evidence for Managed K8s viability at hyperscale

---

### [STATISTIC] Microsoft AKS - 70,000 Nodes Across 80 Clusters
**Source:** AKS Engineering Blog
**Date:** 2025
**URL:** https://blog.aks.azure.com/2025/04/02/Scaling-Kubernetes-for-AI-and-Data-intensive-Workloads

**Finding:**
"Microsoft's AKS demonstrated 80 clusters deployed within a single fleet managed by AKS Fleet Manager, with 70,000 nodes distributed across six geographic regions, effortlessly supporting complex AI-like workloads."

**Relevance:** Demonstrates managed K8s capability for distributed AI workloads
**Segment Applicability:** Evidence for Managed K8s (Azure) for Large AI SaaS

---

### [MIGRATION] Grammarly - EC2 to EKS for ML Infrastructure
**Source:** Grammarly Engineering Blog
**Date:** January 2025
**URL:** https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/

**Finding:**
"Grammarly moved from EC2 to EKS (Kubernetes environment), which allowed them to decouple storage from compute resources and move from personalized to dynamically allocated resources."

**Results:**
- [FACT] Linguists benefit from significantly reduced setup time (multiple hours saved per person per sprint)
- [FACT] ML team members wait much less time for resources through shared pool of large instance resources
- [FACT] Infrastructure now uses Argo CD to automate deployment to Kubernetes
- [FACT] Helm charts deployed involve KubeRay, JupyterLab, VS Code, and SSH servers

**Relevance:** Demonstrates migration TO Kubernetes for ML workloads
**Segment Applicability:** Evidence for Managed K8s adoption for Mid-Market AI SaaS

---

### [FACT] Anthropic - Multi-Cloud Kubernetes Strategy
**Source:** Cloud Native Now, SiliconANGLE, Job Postings
**Date:** 2024-2025
**URL:** https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/

**Finding:**
"Anthropic leverages Google Cloud's GKE to manage mega-scale Kubernetes clusters, orchestrate diverse workloads, and achieve breakthrough efficiency optimizations."

**Additional Facts:**
- [FACT] Building systems and running large Kubernetes clusters using GPU/TPU/Trainium accelerators
- [FACT] Multi-cloud infrastructure: AWS Project Rainier (Trainium2), Google Cloud TPUs, Microsoft Azure
- [FACT] Job posting: "Software Engineer - Kubernetes / Accelerator Infrastructure" (Menlo Ventures Job Board, 2024)
- [FACT] When Kubernetes clusters went down (pod IP exhaustion), used internal tools to diagnose and add new IP pool

**Relevance:** Frontier AI company using managed K8s across multiple clouds
**Segment Applicability:** Evidence for Managed K8s (GKE) for Frontier AI companies

---

### [FACT] Cohere - Oracle Kubernetes Engine (OKE) with GPUs
**Source:** Oracle Case Study
**Date:** 2024
**URL:** https://www.oracle.com/cloud/technical-case-studies/cohere/

**Finding:**
"Cohere had already been using Kubernetes to deploy its workloads, and by using Oracle's OKE (Oracle Kubernetes Engine), it could continue deploying as they were before, but with access to the GPUs they needed."

**Technical Details:**
- [FACT] Used Oracle Cloud Infrastructure Kubernetes Engine (OKE) and GPUs hosted on OCI
- [FACT] Leveraged OCI's highly optimized RDMA networks for efficient scaling of large AI models
- [FACT] Private deployments typically run on Kubernetes (not a firm requirement)
- [FACT] Deployment options: SaaS, cloud of choice, on-prem

**Relevance:** Enterprise AI company choosing managed K8s for GPU access
**Segment Applicability:** Evidence for Managed K8s (OCI) for Mid-Market AI SaaS

---

### [MIGRATION] HubSpot - 400+ MySQL Databases to Kubernetes
**Source:** CNCF Case Study, KubeCon 2018, Speaker Deck
**Date:** 2017-2018 (foundational), updated 2024
**URL:** https://www.cncf.io/case-studies/hubspot/

**Finding:**
"HubSpot migrated all 400+ of their MySQL databases from standalone instances into Kubernetes with the help of the Vitess project."

**Scale Metrics:**
- [STATISTIC] Over 750 Vitess shards per datacenter (US and EU)
- [STATISTIC] Each shard is a 3-instance MySQL cluster
- [STATISTIC] Scaled from ~400 MySQL clusters to 700 while keeping infrastructure team at 3-5 people
- [FACT] Hundreds of databases running on more than 1,000 EC2 instances managed by one person

**Performance Improvements:**
- [FACT] Failover downtime reduced from minutes to seconds
- [FACT] Database provisioning time reduced from days to minutes
- [FACT] Whole cluster upgrades reduced from days to 2 hours

**Recent Infrastructure (2024):**
- [FACT] Traffic routing layer powered by Envoy deployed on Kubernetes
- [FACT] Envoy pods operate as load balancers handling internal and external traffic
- [FACT] System processes billions of customer requests daily
- [FACT] Experienced incident in September 2024 leading to rollback from Envoy to Nginx

**Relevance:** Long-term K8s adoption for data infrastructure at scale
**Segment Applicability:** Evidence for Open/Self-Managed K8s for Mid-Market SaaS

---

### [FACT] Snowflake - Project Joshua with Amazon EKS
**Source:** AWS Architecture Blog
**Date:** 2024
**URL:** https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/

**Finding:**
"Snowflake developed Project Joshua, an internal system that leverages Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Container Registry (ECR), Amazon EC2 Spot Instances, and AWS PrivateLink to run over one hundred thousand of validation and regression tests an hour."

**Technical Implementation:**
- [FACT] Created custom pod scaler (agent scaler) communicating directly with Amazon EKS using Kubernetes API
- [FACT] Utilizes Kubernetes Cluster Autoscaler to dynamically scale worker nodes in minutes
- [FACT] Tests scheduled in parallel across cluster

**Infrastructure Modernization (2024-2025):**
- [FACT] Modernized Kubernetes infrastructure with Karpenter (open source cluster autoscaler)
- [FACT] Integrated Bottlerocket AMIs into EKS environment
- [FACT] Achieved zero downtime during modernization

**Relevance:** Data platform company using managed K8s for large-scale testing
**Segment Applicability:** Evidence for Managed K8s (EKS) for Large SaaS

---

### [FACT] Notion - EKS for Data Infrastructure
**Source:** Notion Engineering Blog
**Date:** May 2024
**URL:** https://www.notion.com/blog/building-and-scaling-notions-data-lake

**Finding:**
"Notion deployed Debezium CDC connectors in an AWS EKS cluster to handle Postgres row changes, with the mature EKS management only requiring a few upgrades over two years and smoothly handling tens of MB/sec of Postgres row changes as of May 2024."

**Data Infrastructure Scale:**
- [STATISTIC] Expanded from 32 physical Postgres instances (480 logical shards total) in 2021
- [STATISTIC] Increased to 96 physical instances in 2023 (480 logical shards maintained)
- [FACT] Set up one Debezium CDC connector per Postgres host deployed in EKS cluster
- [FACT] Pipeline: Postgres → Debezium CDC (EKS) → Kafka → Hudi → Apache Spark → S3

**Results:**
- [STATISTIC] Over $1 million in savings for 2022 with proportionally higher savings in 2023-2024
- [FACT] End-to-end ingestion time reduced from more than a day to a few minutes (small tables) or couple hours (large tables)

**Relevance:** Productivity SaaS using managed K8s for data pipeline
**Segment Applicability:** Evidence for Managed K8s (EKS) for Mid-Market SaaS

---

### [FACT] Salesforce - Kubernetes on Bare Metal
**Source:** Salesforce Engineering Blog
**Date:** 2024
**URL:** https://engineering.salesforce.com/tagged/kubernetes/

**Finding:**
"Salesforce deploys and runs Kubernetes directly atop bare metal, integrating it into the rest of the Salesforce infrastructure."

**Implementation Details:**
- [FACT] Uses GitOps where service owners describe desired state declaratively in git repos
- [FACT] Continuous integration pipelines build container images deployed to Kubernetes via Spinnaker
- [FACT] Transitioned Trino architecture to Kubernetes for enhanced flexibility and efficiency
- [FACT] Incorporates auto-scaling with Horizontal Pod Autoscaler and Cluster Autoscaler
- [FACT] Reduced scale-out time to mere seconds

**Heroku Platform:**
- [FACT] Announced Heroku PaaS environment now runs natively on Kubernetes clusters
- [FACT] Starting with integrations with Amazon EKS

**Data Cloud Migration (2024):**
- [FACT] Article title: "Data Cloud Migrates From Amazon EC2 to Kubernetes in 6 Months"
- [FACT] Developed in-house patching designs for security compliance
- [FACT] Integrated SSD disks for pod access

**Relevance:** Enterprise SaaS running self-managed K8s on bare metal
**Segment Applicability:** Evidence for Open K8s (bare metal) for Large Enterprise SaaS

---

### [FACT] Elastic - Kubernetes with Crossplane for Serverless
**Source:** Elastic Engineering Blog
**Date:** December 2024 (AWS GA), April 2025 (GCP GA), June 2025 (Azure GA)
**URL:** https://www.elastic.co/blog/journey-to-build-elastic-cloud-serverless

**Finding:**
"Elastic selected Crossplane as the infrastructure management tool, which is an open source project that extends the Kubernetes API to enable the provisioning and management of cloud infrastructure and services using Kubernetes-native tools and practices."

**Architecture Decisions:**
- [FACT] Chose Kubernetes for orchestration
- [FACT] Addressed networking challenges with Cilium
- [FACT] Implemented cell-based architecture and canary deployments for scalability
- [FACT] Multi-cloud deployment: AWS (4 regions), GCP (3 regions), Azure (1 region, more planned)

**Product Offering:**
- [FACT] ECK (Elastic Cloud on Kubernetes) simplifies setting up Elastic Stack on Kubernetes
- [FACT] Allows platform engineers to configure and manage Elastic Stack clusters at scale

**Relevance:** Data/search platform using K8s API for multi-cloud infrastructure
**Segment Applicability:** Evidence for Open K8s patterns for Mid-Market SaaS

---

### [FACT] Datadog - Kubernetes Monitoring & Optimization Products
**Source:** Datadog Engineering Blog
**Date:** 2024-2025
**URL:** https://www.datadoghq.com/blog/

**Finding:**
"The vast majority of Kubernetes workloads are overprovisioned, and Datadog Kubernetes Autoscaling provides multi-dimensional rightsizing for applications without impacting stability."

**Product Announcements:**
- [FACT] Launched Kubernetes autoscaling and enhanced cost controls for AWS infrastructure (2025)
- [FACT] Kubernetes Active Remediation helps identify and fix common infrastructure issues
- [FACT] AI-powered explanations provide deeper insights into root cause of issues
- [FACT] Infrastructure-as-Code (IaC) Security detects misconfigurations before production

**Industry Observation:**
- [STATISTIC] Over 80% of container costs are wasted on idle resources (according to Datadog)

**Relevance:** Monitoring SaaS observations on K8s adoption patterns
**Segment Applicability:** Industry data on K8s efficiency challenges

---

### [FACT] MongoDB Atlas - Kubernetes Operator Strategy
**Source:** MongoDB Engineering Blog
**Date:** 2024-2025 (updated March 2025)
**URL:** https://www.mongodb.com/blog/

**Finding:**
"For organizations leveraging Kubernetes, the Atlas Kubernetes Operator provides seamless integration and allows you to deploy and manage Atlas resources using your existing Kubernetes tooling."

**Announcements:**
- [FACT] Multi-Kubernetes cluster deployment support announced October 2024
- [FACT] Enables managing MongoDB across multiple Kubernetes clusters in different regions
- [FACT] Integration with AWS CloudFormation and HashiCorp Terraform
- [FACT] 33+ resources available in CloudFormation Public Registry

**Relevance:** Database SaaS enabling K8s-native deployment
**Segment Applicability:** Evidence for K8s as deployment target for SaaS platforms

---

### [TREND] CNCF - Kubernetes AI Conformance Program
**Source:** CNCF Official Announcements, InfoQ
**Date:** November 2025
**URL:** https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/

**Finding:**
"CNCF launched the Certified Kubernetes AI Conformance program to standardise artificial intelligence workloads by establishing a technical baseline for GPU management, networking, and gang scheduling, aiming to reduce technical debt and prevent vendor lock-in."

**Additional Facts:**
- [FACT] Program sets open standards for making AI workloads predictably deployable on Kubernetes
- [FACT] Azure Kubernetes Service (AKS) certified for Kubernetes AI Conformance
- [QUOTE] "Kubernetes is 'foundational' infrastructure for AI" (CNCF statement)

**Relevance:** Industry standardization around K8s for AI workloads
**Segment Applicability:** Evidence for K8s becoming standard platform for AI SaaS

---

### [INDUSTRY DATA] Container Adoption Statistics
**Source:** The New Stack, Industry Reports
**Date:** 2024-2025
**URL:** https://thenewstack.io/

**Finding:**
[STATISTIC] "82% of container users are running Kubernetes in production, with Kubernetes no longer a niche tool but a core infrastructure layer."

**Additional Industry Observations:**
- [QUOTE] "If 2024 was the year Kubernetes became mainstream, 2025 was the year it became indispensable."
- [FACT] AI fundamentally changed infrastructure economics in 2025
- [FACT] Public cloud GPU costs expanded rapidly, leading enterprises toward private dedicated GPU infrastructure
- [FACT] Platform engineering emerged as significant shift with teams adopting internal developer platforms (IDPs)
- [STATISTIC] Most organizations operate clusters well under 1,000 nodes

**Relevance:** Industry-wide adoption trends for Kubernetes
**Segment Applicability:** Context for overall market movement

---

### [CASE STUDY] Eli Lilly - Enterprise AI on Amazon EKS
**Source:** AWS re:Invent 2024
**Date:** December 2024
**URL:** https://aws.amazon.com/blogs/containers/amazon-eks-and-kubernetes-sessions-at-aws-reinvent-2024/
**Presenters:** Cas Starsiak (AVP Enterprise Research and AI, Lilly), Mike Stefaniak (Sr. Manager Product Management, AWS)

**Finding:**
"The success of Eli Lilly's generative AI platform demonstrates how Amazon EKS can serve as a foundation for enterprise-wide AI adoption, with organizations building on existing Kubernetes expertise and using the rich ecosystem of open-source ML tools."

**Relevance:** Enterprise pharmaceutical using managed K8s for AI
**Segment Applicability:** Evidence for Managed K8s (EKS) in regulated industries

---

### [CASE STUDY] Contextual AI - Google Cloud GKE
**Source:** Google Cloud Case Study
**Date:** 2024-2025
**URL:** https://cloud.google.com/customers/contextualai

**Finding:**
"Contextual AI needed robust and highly scalable infrastructure and chose Google Cloud due to its high-performance GPUs and experience as an AI leader."

**Additional GKE AI Innovations (Google Cloud Next 2025):**
- [STATISTIC] New inference capabilities in GKE can reduce serving costs by up to 30%
- [STATISTIC] Decrease tail latency by up to 60%
- [STATISTIC] Increase throughput by up to 40%
- [FACT] Cluster Director for GKE generally available for deploying large clusters of accelerated VMs

**Other GKE AI Customers:**
- [FACT] Picterra adopted GKE to power platform for geospatial AI workloads
- [FACT] invos Group deploys all FinTech/MarTech services in GKE with Terraform and Argo CD
- [FACT] Routematic migrated entire infrastructure to GKE in 8 months with zero downtime

**Relevance:** Multiple AI companies choosing managed K8s on Google Cloud
**Segment Applicability:** Evidence for Managed K8s (GKE) for AI SaaS

---

### [FACT] Jasper AI - Kubernetes with Developer Experience Focus
**Source:** Jasper Blog
**Date:** 2024-2025
**URL:** https://www.jasper.ai/blog/devx-renaissance-the-death-of-devops

**Finding:**
"Jasper has built the JasperCLI, a tool their engineers can use to deploy ephemeral testing environments, spin up a Kubernetes stack, safely connect to their production and staging databases, and more."

**DevX Philosophy:**
- [FACT] Security-first mentality maintained without compromising developer workflows
- [FACT] Access controls for database connections and Kubernetes clusters transparent to developers
- [FACT] Focus on seamless developer experience interacting with infrastructure

**Relevance:** AI SaaS using K8s with abstraction layer for developer productivity
**Segment Applicability:** Evidence for K8s adoption pattern prioritizing DevEx

---

### [FACT] Hugging Face - Multi-Cloud Kubernetes Deployment
**Source:** Hugging Face Blog, Partner Announcements
**Date:** 2024-2025
**URL:** https://huggingface.co/blog/

**Finding:**
"Hugging Face models can be deployed on Google Kubernetes Engine, Azure Kubernetes Service, and Oracle Container Engine for Kubernetes."

**Technical Resources:**
- [FACT] Published guides for deploying LLMs on Azure Kubernetes Service using vLLM (November 2024)
- [FACT] Guide for launching models from Hugging Face Hub with TGI (Text Generation Inference) on AWS EKS
- [FACT] HUGS (Hugging Face Generative AI Services) can be deployed on Kubernetes
- [FACT] Partnership with Google Cloud for GKE integration
- [FACT] Documentation covers Helm charts, Docker containers, GPU configuration, production patterns

**Relevance:** AI model platform enabling K8s deployment across clouds
**Segment Applicability:** Evidence for K8s as standard deployment target for AI models

---

## Preliminary Estimates

### Direct Evidence for Architecture Segments:

**Managed Kubernetes (EKS/GKE/AKS/OKE):**
- Companies: Anthropic, Cohere, Snowflake, Notion, Grammarly, Figma (post-migration), Eli Lilly, Contextual AI, Picterra, Routematic, invos Group, Hugging Face (deployment option)
- Scale: Demonstrated at 70,000+ nodes (AKS Fleet), 130,000 nodes (GKE)
- **Segment Prevalence Estimate:** HIGH across all revenue tiers

**Open/Self-Managed Kubernetes:**
- Companies: OpenAI (Azure-based), Databricks (hybrid), Salesforce (bare metal), HubSpot, Elastic (with Crossplane)
- Scale: Demonstrated at 7,500 nodes (OpenAI), thousands of clusters (Databricks)
- **Segment Prevalence Estimate:** MEDIUM-HIGH for Large SaaS ($200M+), MEDIUM for Mid-Market

**Hybrid Managed + Self-Managed:**
- Companies: Databricks (explicit hybrid strategy)
- **Segment Prevalence Estimate:** MEDIUM for Large SaaS with multi-cloud requirements

**Migration Patterns (2024-2025):**
- **TO Kubernetes:** Figma (ECS→EKS), Grammarly (EC2→EKS), Salesforce Data Cloud (EC2→K8s), HubSpot (EC2→K8s)
- **FROM Kubernetes:** No engineering blog disclosures found
- **Observation:** Migration direction is TOWARD Kubernetes, not away from it

---

## Data Quality Assessment

### Completeness: 7/10
- **Strengths:**
  - Direct quotes from 15+ companies across revenue tiers
  - Specific cluster sizes and performance metrics
  - Migration timelines and reasons documented
  - Mix of frontier AI (OpenAI, Anthropic) and enterprise SaaS (Salesforce, HubSpot)

- **Gaps:**
  - Limited financial data (only Notion disclosed $1M+ savings)
  - No disclosures from: Writer AI, Jasper (limited), Stability AI, Replicate (limited)
  - Geographic distribution unclear (most appear US-based)
  - Small AI SaaS (<$10M ARR) underrepresented

### Recency: 9/10
- Majority of sources from 2024-2025
- Several announcements from Q4 2024 and Q1 2025
- CNCF AI Conformance Program (November 2025) is very recent
- OpenAI data from 2021 but still referenced as foundational

### Sample Size: 6/10
- 15+ companies with direct disclosures
- Represents mix of segments but not statistically representative
- Missing many mid-market AI SaaS companies (no public engineering blogs)
- Over-indexed on companies with mature engineering blog culture

### Known Biases:
1. **Publication Bias:** Companies with problems are less likely to publish engineering blogs
2. **Maturity Bias:** Companies publishing detailed engineering content tend to be larger/more mature
3. **Success Bias:** Migration stories typically published after successful completion
4. **Geographic Bias:** US-based companies over-represented (limited EU/APAC disclosures)
5. **Vendor Bias:** Cloud providers (Google, AWS, Azure) publish customer case studies of successes
6. **Selection Bias:** Companies with notable scale achievements more likely to share publicly

---

## Limitations — What This Source CANNOT Tell Us

### Cannot Determine:
1. **Failure Rates:** No companies disclosed failed K8s migrations or decisions to abandon K8s
2. **Total Cost Comparison:** Only Figma mentioned "cost savings" and Notion disclosed "$1M+ savings" but no direct K8s vs. alternatives cost analysis
3. **Small Company Reality:** Engineering blogs skewed toward companies with resources for content marketing
4. **Private Company Data:** Many AI SaaS companies do not publish engineering blogs
5. **Quantitative Adoption Rates:** Cannot calculate "X% of AI SaaS use K8s" from blog posts
6. **Decision Criteria:** Most blogs explain "what" and "how" but limited insight into decision-making process
7. **Operational Costs:** No disclosure of team size required to operate K8s infrastructure
8. **Downtime/Reliability Data:** Limited disclosure of incidents (HubSpot Sept 2024 exception)
9. **Serverless Adoption:** No engineering blogs disclosed moving FROM K8s TO serverless
10. **Non-K8s Architectures:** Companies using ECS, Lambda, or other patterns less likely to publish

### Cannot Validate:
- Whether disclosed architectures represent majority of workloads or showcase examples
- Current state (2026) vs. historical blog posts (some 2021-2023 content)
- Whether companies maintain these architectures or have since migrated
- Representativeness of blogging companies vs. non-blogging companies

---

## Confidence Score: 7.5/10

### Justification:

**High Confidence (8-9/10) for:**
- Kubernetes is widely adopted by AI SaaS companies that publish engineering blogs
- Managed Kubernetes (EKS, GKE, AKS) is common deployment pattern
- Large-scale K8s is viable (7,500-130,000 nodes demonstrated)
- Migration trend in 2024-2025 is TOWARD Kubernetes, not away from it
- Major cloud providers investing heavily in K8s for AI workloads

**Medium Confidence (6-7/10) for:**
- Relative prevalence of managed vs. self-managed (sample size limitations)
- Applicability to companies <$50M ARR (underrepresented in blogs)
- Cost-effectiveness claims (limited quantitative data)
- Operational complexity (limited disclosure of team sizes, incident rates)

**Low Confidence (4-5/10) for:**
- Exact market share percentages (publication bias, sample size)
- EU/APAC adoption patterns (geographic bias in sources)
- Small AI SaaS company (<$10M ARR) infrastructure choices
- Companies that tried and abandoned Kubernetes (negative results unpublished)

**Reasoning for 7.5/10 Overall:**
The data provides strong directional evidence with specific quotes, metrics, and migration patterns. Quality is high but sample is biased toward companies with mature engineering communication culture. The consistency of findings across independent sources increases confidence, but absence of negative cases and quantitative market data limits ability to make precise prevalence claims.

---

## Sources

- [Scaling Kubernetes to 7,500 nodes | OpenAI](https://openai.com/index/scaling-kubernetes-to-7500-nodes/)
- [Intelligent Kubernetes Load Balancing at Databricks](https://www.databricks.com/blog/intelligent-kubernetes-load-balancing-databricks)
- [How We Migrated onto K8s in Less Than 12 months | Figma Blog](https://www.figma.com/blog/migrating-onto-kubernetes/)
- [Figma Moves from ECS to Kubernetes - InfoQ](https://www.infoq.com/news/2024/09/figma-ecs-kubernetes-eks/)
- [Google's 130,000-Node Kubernetes Colossus - WebProNews](https://www.webpronews.com/googles-130000-node-kubernetes-colossus-engineering-the-future-of-ai-scale-computing/)
- [Limitless Kubernetes Scaling for AI | AKS Engineering Blog](https://blog.aks.azure.com/2025/04/02/Scaling-Kubernetes-for-AI-and-Data-intensive-Workloads)
- [How We Upgraded Our ML Infrastructure | Grammarly Engineering Blog](https://www.grammarly.com/blog/engineering/ml-infrastructure-research-experimentation/)
- [How Anthropic Dogfoods On Claude Code - Cloud Native Now](https://cloudnativenow.com/editorial-calendar/best-of-2025/how-anthropic-dogfoods-on-claude-code-2/)
- [Cohere trains and deploys on OCI | Oracle](https://www.oracle.com/cloud/technical-case-studies/cohere/)
- [HubSpot Case Study | CNCF](https://www.cncf.io/case-studies/hubspot/)
- [MySQL and Vitess at HubSpot - Speaker Deck](https://speakerdeck.com/jfg956/mysql-and-vitess-and-kubernetes-at-hubspot)
- [Snowflake: Running Millions of Tests with EKS | AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/snowflake-running-millions-of-simulation-tests-with-amazon-eks/)
- [Modernizing Snowflake's Kubernetes Infrastructure | AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/modernizing-snowflake-corporates-kubernetes-infrastructure-with-bottlerocket-and-karpenter/)
- [Building and Scaling Notion's Data Lake](https://www.notion.com/blog/building-and-scaling-notions-data-lake)
- [Salesforce Engineering Blog - Kubernetes](https://engineering.salesforce.com/tagged/kubernetes/)
- [Elastic's Journey to Build Serverless | Elastic Blog](https://www.elastic.co/blog/journey-to-build-elastic-cloud-serverless)
- [DASH 2025 New Feature Roundup | Datadog](https://www.datadoghq.com/blog/dash-2025-new-feature-roundup-act/)
- [MongoDB Atlas Kubernetes Integration](https://www.mongodb.com/blog/)
- [CNCF Kubernetes AI Conformance Program](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/)
- [CNCF: Kubernetes is 'foundational' for AI - The New Stack](https://thenewstack.io/cncf-kubernetes-is-foundational-infrastructure-for-ai/)
- [Amazon EKS at AWS re:Invent 2024](https://aws.amazon.com/blogs/containers/amazon-eks-and-kubernetes-sessions-at-aws-reinvent-2024/)
- [How GKE powers AI innovation | Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/how-gke-powers-ai-innovation)
- [Contextual AI case study | Google Cloud](https://cloud.google.com/customers/contextualai)
- [DevX Renaissance: Death of DevOps | Jasper Blog](https://www.jasper.ai/blog/devx-renaissance-the-death-of-devops)
- [Hugging Face Engineering Blog](https://huggingface.co/blog/)
- [InfoQ - Kubernetes News](https://www.infoq.com/kubernetes/)
- [The New Stack - AI Infrastructure](https://thenewstack.io/)
