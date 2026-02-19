# F56: Design & Architecture Phase Constraints

**Research Question:** How does the target deployment model (on-prem vs managed Kubernetes vs cloud-native) constrain or alter software architecture decisions during the design phase, specifically for AI-enabled applications?

---

## Executive Summary

The choice of target deployment model is not a post-design infrastructure decision — it is a first-principle constraint that fundamentally reshapes how AI-enabled SaaS products are architected. On-premises support forces ISVs to eliminate all cloud-managed service dependencies at design time, replace them with self-hosted equivalents, and build abstraction layers across the entire stack — database, messaging, storage, inference, and observability. This "lowest-common-denominator" effect inflates codebase complexity, increases the initial design cycle by requiring additional architecture review gates for compliance and data residency validation, and binds the product to a portable-but-suboptimal architecture. Managed Kubernetes reduces but does not eliminate this constraint, as the K8s control plane is managed but workloads remain self-operated. Cloud-native architectures permit the greatest design velocity by delegating infrastructure concerns to managed services, but create deep vendor coupling that is expensive to reverse. For AI-enabled applications specifically, the on-premises constraint is especially severe: every component of the RAG pipeline — embedding generation, vector storage, LLM inference — must be re-architected around self-hosted alternatives that carry significant GPU infrastructure, MLOps, and operational overhead costs.

---

## 1. Portable vs Cloud-Optimized Architecture: The Core Design Trade-Off

### The Abstraction Dilemma

When an ISV must support on-premises deployment alongside cloud delivery, every architectural decision bifurcates. Cloud-native designs freely use managed services — Aurora, DynamoDB, SQS, Bedrock — that have no direct on-premises equivalents. A design that targets portability must instead build against open interfaces and self-hosted components from day one.

The fractal.cloud analysis of cloud-agnostic development names this directly: [QUOTE] "Chasing the 'run anywhere' myth leads companies to build bland, lowest-common-denominator systems that fail to leverage the true power of any cloud." — [What "Cloud-Agnostic" Really Means in 2025](https://fractal.cloud/blog/what-cloud-agnostic-really-means-in-2025-and-why-it-s-not-what-you-think)

The same source characterizes the maintenance burden: [QUOTE] "You end up building a complex system that doesn't excel anywhere and requires a massive maintenance effort just to remain 'agnostic.'" — [What "Cloud-Agnostic" Really Means in 2025](https://fractal.cloud/blog/what-cloud-agnostic-really-means-in-2025-and-why-it-s-not-what-you-think)

This is the core architectural trade-off: pursuing implementation portability means paying cloud costs and cloud operational overhead without extracting cloud-native value. The practical alternative, advocated by the same source, is **architecture standardization** — defining provider-agnostic conceptual patterns (e.g., "message queue," "object store") and mapping them to provider-specific implementations — shifting lock-in from the architectural level to the implementation level where it is more negotiable. [Source: fractal.cloud](https://fractal.cloud/blog/what-cloud-agnostic-really-means-in-2025-and-why-it-s-not-what-you-think)

### Dual-Track Architecture Cost

The binmile comparison of cloud-native vs cloud-agnostic frameworks notes that maintaining abstraction layers demands [QUOTE] "broader skills requirements (teams need knowledge beyond a single provider) and troubleshooting challenges, as debugging cross-cloud failures can be harder and introduce unique issues such as observability gaps." — [Cloud Agnostic vs Cloud Native: Which is Better in 2025](https://binmile.com/blog/cloud-native-vs-cloud-agnostic/)

The practical reality for ISVs: [UNVERIFIED — engineering consensus, no single citable study] supporting three deployment targets (on-premises, managed K8s, cloud-native) with a single codebase typically requires 20–40% additional engineering effort at the design phase to define service interfaces, select portable backing services, and establish the abstraction layer contract before any feature code is written.

---

## 2. The Lowest-Common-Denominator Problem

### What On-Premises Eliminates at Design Time

When designing for on-premises deployment, the following managed services cannot be assumed and must each be replaced with a self-hosted equivalent or abstracted behind an interface:

| Managed Service Category | Cloud-Native Option | On-Premises Self-Hosted Equivalent |
|--------------------------|---------------------|------------------------------------|
| Relational Database | Amazon Aurora, Azure SQL, Cloud SQL | PostgreSQL, MySQL on VMs |
| Object Storage | S3, GCS, Azure Blob | MinIO, Ceph |
| Message Queue / Streaming | SQS, Pub/Sub, Event Hubs | Apache Kafka, RabbitMQ |
| Secrets Management | AWS Secrets Manager, Azure Key Vault | HashiCorp Vault |
| Observability | CloudWatch, Azure Monitor | Prometheus + Grafana stack |
| Serverless Compute | AWS Lambda, Azure Functions | Knative, OpenFaaS on K8s |
| LLM Inference | Amazon Bedrock, Azure OpenAI | vLLM, Ollama, TGI on GPU nodes |
| Vector Database | Pinecone, Weaviate Cloud | Milvus, Qdrant, pgvector |
| Embedding API | OpenAI Embeddings, Cohere Embed | Self-hosted BGE, E5 via vLLM |

Each row represents a design-phase decision that the team must make before writing feature code. Cloud-agnostic development literature describes this as requiring "abstracted service layers" — a pattern that [QUOTE] "encapsulates provider-specific service implementations, offering a unified interface to consumers." — [Abstracted Service Layers Pattern, Software Patterns Lexicon](https://softwarepatternslexicon.com/cloud-computing/hybrid-cloud-and-multi-cloud-strategies/abstracted-service-layers/)

### Architecture Inflation

The absence of managed services does not simply add components — it adds entire operational domains. A cloud-native design where object storage is `s3.put_object()` becomes, on-premises, a MinIO cluster requiring: HA configuration decisions, network topology planning, TLS certificate management, backup strategy, and capacity planning — all resolved at design time, not at deploy time.

[FACT] Elastic's on-premises reference architecture specifies that data nodes require "8-32+ cores" with "32-128+ GB RAM" and "1-4+ TB SSD/NVMe" storage, with an explicit warning to [QUOTE] "Avoid network storage (NAS) due to potential latency issues." — [Elastic On-Premises Reference Architecture, DeepWiki](https://deepwiki.com/elastic/reference-architecture-docs/3.1-on-premises-deployments)

This level of hardware specification must be locked at design time when supporting on-premises customers — creating hardware sizing documents, reference configurations, and minimum requirements that a cloud-native design simply delegates to the cloud provider.

---

## 3. Database Selection: Portable vs Cloud-Optimized

### The Portability Anchor

Database selection is the single most consequential portability decision made at design time. Cloud-native databases (Aurora, Cosmos DB, Spanner, DynamoDB) provide compelling performance and operational advantages but have no on-premises equivalents. Designing around them forecloses on-premises support entirely.

[STATISTIC] PostgreSQL holds a 45.55% usage rate among developers in 2025, compared to MySQL's 41.09%, and is described as [QUOTE] "a flexible tool that works well across a wide range of platforms and, thanks to an extensible architecture, can support most workloads." — [PostgreSQL vs MySQL 2025, nucamp.co](https://www.nucamp.co/blog/coding-bootcamp-backend-with-python-2025-postgresql-vs-mysql-in-2025-choosing-the-best-database-for-your-backend)

PostgreSQL is the dominant portable-first database choice for ISVs for this reason: it runs identically on bare metal, VMs, managed K8s (via CloudNativePG or Zalando operator), and cloud-managed services (RDS for PostgreSQL, Cloud SQL, Azure Database for PostgreSQL). The same schema, queries, and extensions work across all deployment targets.

### Cloud-Native Database Advantages Foregone

Choosing PostgreSQL for portability means consciously forfeiting:

- **Aurora Serverless v2**: automatically scales from 0.5 to 128 ACUs, zero-ops capacity management — [AWS Aurora](https://aws.amazon.com/rds/aurora/)
- **AlloyDB**: [FACT] "can process millions of queries per second across hybrid environments" with PostgreSQL wire compatibility — [AlloyDB Omni, InfoWorld](https://www.infoworld.com/article/4093191/azure-horizondb-microsoft-goes-big-with-postgresql.html)
- **Cosmos DB**: globally distributed, multi-model, sub-10ms reads — unavailable on-premises without Azure Stack

### Hybrid DBaaS Options

[FACT] Nutanix Database Service is a hybrid multi-cloud DBaaS that supports on-premises and cloud (AWS, Azure) deployments, covering Oracle, SQL Server, MySQL, PostgreSQL, MongoDB, and vector databases — [dbvis.com, Best DBaaS Solutions 2025](https://www.dbvis.com/thetable/best-database-as-a-service-dbaas-solutions-of-2025/)

For ISVs requiring portability, PostgreSQL with the pgvector extension presents an especially efficient choice for AI workloads at moderate scale, since it collapses the relational database and vector store into a single self-hostable system.

---

## 4. AI Architecture Decisions by Deployment Target

### LLM Inference: API Call vs Self-Hosted

The choice of deployment target determines the permissible LLM inference architecture. Cloud-native designs can call managed inference endpoints (Amazon Bedrock, Azure OpenAI Service, Google Vertex AI) with zero infrastructure overhead. On-premises designs must self-host model weights, GPU drivers, and serving frameworks.

[FACT] Self-hosted LLM deployments require: "High-performance computing resources (GPUs/TPUs), maintained drivers and serving frameworks (vLLM, TGI), NVMe SSDs for reduced latency, high-speed networking infrastructure, and Kubernetes or cloud architecture expertise." — [deepsense.ai, LLM Inference Decision Guide](https://deepsense.ai/blog/llm-inference-as-a-service-vs-self-hosted-which-is-right-for-your-business/)

[FACT] Self-hosted LLMs provide [QUOTE] "full control over models and hardware" and enable [QUOTE] "advanced customization techniques tailored to specific business requirements including fine-tuning for model alignment." — [bentoml.com, Serverless vs Self-Hosted LLM Inference](https://bentoml.com/llm/llm-inference-basics/serverless-vs-self-hosted-llm-inference)

[FACT] Cloud API services are [QUOTE] "subject to external API rate limits or sudden policy changes" while self-hosted systems require [QUOTE] "managing DevOps time for setup and maintenance" and implementing [QUOTE] "monitoring and alerting systems including LLM-specific metrics." — [bentoml.com, Serverless vs Self-Hosted LLM Inference](https://bentoml.com/llm/llm-inference-basics/serverless-vs-self-hosted-llm-inference)

[DATA POINT] As of early 2026, self-hosted LLMs running on Blackwell GPUs demonstrated "cost parity with cloud APIs within 1-4 months at moderate usage (30M tokens/day), with subsequent operations 40-200% cheaper than budget-tier cloud models." — [dasroot.net, Self-Hosted LLMs vs Cloud APIs Cost Comparison](https://dasroot.net/posts/2026/01/self-hosted-llm-vs-cloud-apis-cost-performance/)

| Inference Architecture | On-Premises | Managed K8s | Cloud-Native |
|------------------------|-------------|-------------|--------------|
| Design complexity | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| Key requirements | GPU nodes, vLLM/TGI, MLOps team | GPU node pools, serving stack | API key, SDK integration |
| Representative tools | vLLM, Ollama, TGI, Triton | vLLM on K8s, KServe | Bedrock, Azure OpenAI, Vertex |
| Est. FTE (design phase) | 1.0-2.0 FTE | 0.5-1.0 FTE | 0.1-0.25 FTE |

*FTE estimates assume mid-scale deployment for 50 enterprise customers; on-call burden excluded from design-phase estimates.*

### Embedding Pipeline Architecture

Embedding generation sits upstream of every RAG query. The deployment target determines whether embeddings are generated via API call or via self-hosted model inference — a decision that is architecturally locked at design time because [QUOTE] "Changing chunking approaches post-deployment requires complete re-ingestion and re-embedding." — [introl.com, RAG Infrastructure Production Guide](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)

[FACT] On-premises embedding pipelines use open-source models: "BGE, E5, and GTE open-source models enable self-hosted embedding at scale, with organizations processing billions of documents often deploying these models on internal GPU infrastructure to eliminate per-token costs, though self-hosting requires managing model updates, capacity planning, and inference optimization." — [greennode.ai, Best Embedding Models for RAG](https://greennode.ai/blog/best-embedding-models-for-rag)

[FACT] BGE-M3 supports "over 100 languages" and "both dense and sparse embeddings for hybrid search," deployable via vLLM with Kubernetes using "float16 dtype, GPU memory utilization of 0.85, and max-model-len of 4096 tokens." — [artsmart.ai, Top Embedding Models 2025](https://artsmart.ai/blog/top-embedding-models-in-2025/)

[FACT] Commercial embedding APIs (Voyage AI) offer "32K-token context windows" at "$0.06 per million tokens — 2.2x cheaper than OpenAI" for cloud deployments, available only as external API services. — [introl.com, RAG Infrastructure Production Guide](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)

[QUOTE] "Embedding drift degrades retrieval quality over time when embedding models change," requiring "version tracking and migration planning for all architectures" — a design-time concern regardless of deployment model. — [introl.com, RAG Infrastructure Production Guide](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)

### Vector Database Selection by Deployment Target

Vector database selection is tightly coupled to deployment model because several leading options are cloud-only managed services.

[FACT] "Pinecone offers a fully managed SaaS-only service...designed for developers who want to focus on building AI applications without worrying about the underlying database infrastructure." On-premises deployment is not available. — [firecrawl.dev, Best Vector Databases 2025](https://www.firecrawl.dev/blog/best-vector-databases-2025)

[FACT] For on-premises deployments: "Milvus OSS or Qdrant OSS are recommended." Both support Helm/Docker deployment into self-managed environments. — [firecrawl.dev, Best Vector Databases 2025](https://www.firecrawl.dev/blog/best-vector-databases-2025)

[DATA POINT] Performance comparison at 50M vectors: Qdrant achieves 41.47 QPS at 99% recall; pgvectorscale achieves 471 QPS — "an order of magnitude difference." Postgres/pgvector "realistically maxes out at 10–100 million vectors before it slows unacceptably." — [firecrawl.dev, Best Vector Databases 2025](https://www.firecrawl.dev/blog/best-vector-databases-2025)

[FACT] Self-hosted vector databases offer "70% cost savings versus managed alternatives but require data engineering expertise for configuration and troubleshooting." — [firecrawl.dev, Best Vector Databases 2025](https://www.firecrawl.dev/blog/best-vector-databases-2025)

| Vector DB | On-Premises | Managed K8s | Cloud-Native | Notes |
|-----------|-------------|-------------|--------------|-------|
| Pinecone | Not available | Not available | Native SaaS | Design-time exclusion for on-prem |
| Milvus OSS | Supported | Supported | Self-deploy only | Apache 2.0 license |
| Qdrant | Supported | Supported | Managed cloud available | Rust-based, compact footprint |
| Weaviate | Docker/K8s OSS | Helm chart | Managed cloud available | Hybrid search built-in |
| pgvector | Supported | Supported | Aurora, AlloyDB | Collapses DB + vector store |

See [F06: Vector Databases] for detailed performance benchmarks and selection criteria.

---

## 5. Abstraction Cost: Provider-Agnostic Infrastructure Layers

### IaC Tool Selection

The infrastructure-as-code layer is where deployment portability is mechanized. Two primary tools serve ISVs targeting multiple deployment models:

[FACT] Terraform supports "over 3,000 providers, from major cloud platforms to smaller services" — including on-premises targets via VMware, Nutanix, and bare-metal providers. — [platformengineering.org, Terraform vs Pulumi vs Crossplane](https://platformengineering.org/blog/terraform-vs-pulumi-vs-crossplane-iac-tool)

[FACT] Crossplane "graduated from the Cloud Native Computing Foundation" in November 2025, marking production maturity for building internal platforms and managing multi-cloud environments. Named production users include "Nike, Autodesk, NASA Science Cloud, Elastic, SAP, IBM, and Nokia." — [InfoQ, Crossplane Graduates CNCF](https://www.infoq.com/news/2025/11/crossplane-grad/)

[FACT] Crossplane's "Composite Resource Definitions enable standardized self-service across heterogeneous infrastructure — trading flexibility for operational consistency." Early adopters reported "a steep learning curve and debugging challenges when compositions or providers misbehaved." — [platformengineering.org, Terraform vs Pulumi vs Crossplane](https://platformengineering.org/blog/terraform-vs-pulumi-vs-crossplane-iac-tool)

[FACT] Terraform's state management approach means "State management becomes tricky when multiple team members work on the same infrastructure," requiring "external coordination mechanisms (CI/CD, pull requests, shared backends)." — [platformengineering.org, Terraform vs Pulumi vs Crossplane](https://platformengineering.org/blog/terraform-vs-pulumi-vs-crossplane-iac-tool)

### Engineering Effort for Abstraction Layers

The Software Patterns Lexicon defines the abstracted service layer pattern's best practices as: "Design using standardized APIs to ensure compatibility and ease of integration," "Focus on common features and capabilities that are prevalent across cloud providers," "Implement in modular fashion to facilitate easier updates and maintenance," and "Conduct regular testing against provider-specific changes and updates." — [Software Patterns Lexicon, Abstracted Service Layers](https://softwarepatternslexicon.com/cloud-computing/hybrid-cloud-and-multi-cloud-strategies/abstracted-service-layers/)

Each of these recommendations represents ongoing engineering work that does not exist in a cloud-native-only design. The abstraction layer must be:
- Designed at the architecture phase (interface contracts)
- Implemented for each deployment target (concrete adapters)
- Tested against each target (integration test matrices)
- Maintained as upstream services evolve (provider API changes)

[UNVERIFIED — engineering consensus] Maintaining a dual-target abstraction layer (cloud + on-premises) for a mid-size AI SaaS product adds approximately 0.5–1.0 FTE to the engineering team on an ongoing basis, primarily in platform/infrastructure engineering roles. No published benchmark for this specific figure was located in 2025 sources; Gartner and Forrester do not publish ISV-specific abstraction overhead estimates.

---

## 6. Twelve-Factor App Constraints by Deployment Model

The twelve-factor app methodology describes portable, scalable SaaS architecture. However, several factors are materially harder to achieve on-premises than in cloud-native environments.

| Factor | On-Premises Difficulty | Managed K8s Difficulty | Cloud-Native Difficulty |
|--------|----------------------|----------------------|------------------------|
| III. Config (env vars) | Moderate: secrets injection requires Vault or custom tooling | Low: K8s Secrets/ConfigMaps | Trivial: native secrets managers |
| IV. Backing Services (attach/detach) | High: no service catalog; manual configuration | Moderate: Helm-based service wiring | Trivial: managed service URIs |
| VIII. Concurrency (scale out) | High: manual horizontal scaling, node provisioning | Moderate: HPA available, node pool limits | Trivial: auto-scaling managed |
| IX. Disposability (fast startup) | High: VM provisioning cycles, no elasticity | Low: Pod scheduling is fast | Trivial: instant serverless cold starts |
| X. Dev/Prod Parity | Very High: infrastructure heterogeneity | Moderate: cluster differences persist | Low: IaC + managed services enforce parity |
| XI. Logs (treat as event streams) | High: requires separate log shipper/aggregator | Moderate: requires Fluentd/Loki stack | Trivial: CloudWatch, Stackdriver built-in |

[FACT] The twelve-factor methodology's requirements for disposability, concurrency, and dev/prod parity "assume stateless, distributed architecture designed for elastic, ephemeral computing — fundamentally misaligned with traditional on-premises infrastructure patterns that prioritize stability and persistent resource allocation." — [bmc.com, 12-Factor App Methodology Explained](https://www.bmc.com/blogs/twelve-factor-app/)

[FACT] Factor X (Dev/Prod Parity) requires "maintaining identical environments across development, staging, and production" which "becomes significantly harder on-premises due to infrastructure heterogeneity and manual resource provisioning, whereas cloud providers offer standardized, reproducible environments." — [bmc.com, 12-Factor App Methodology Explained](https://www.bmc.com/blogs/twelve-factor-app/)

The practical design implication: ISVs targeting on-premises must design compensating mechanisms for Factors VIII, IX, X, and XI at design time — adding architecture complexity for capabilities the cloud provides automatically.

---

## 7. Architecture Review: Additional Gates for On-Premises Designs

### Formal Review Requirements

On-premises support introduces compliance and security review gates that cloud-native designs can defer or skip. An Architecture Review Board (ARB) for on-premises software must address:

- **Data residency verification**: confirming no data egresses to external APIs (LLM, embedding, telemetry) without customer opt-in
- **Air-gap compatibility**: verifying all dependencies can be bundled (container images, model weights, package mirrors)
- **Hardware compatibility matrix**: validating architecture runs on declared minimum hardware specifications
- **License compliance**: confirming all bundled open-source components permit on-premises redistribution

[FACT] AWS Architecture Blog describes ARB reviews as occurring [QUOTE] "after the design phase — before a build or purchase decision — and again before deployment to validate that the reviewed architecture matches the solution that was built." — [AWS Architecture Blog, Build and Operate an Effective ARB](https://aws.amazon.com/blogs/architecture/build-and-operate-an-effective-architecture-review-board/)

[FACT] "Effective ARBs maintain 4–5 core members, never exceeding 10. Beyond 10 people, decision-making quality degrades exponentially." — [hava.io, Architecture Review Board Checklist](https://www.hava.io/blog/architecture-review-board-checklist)

[FACT] TOGAF's Architecture Compliance Review process defines compliance review as ensuring "alignment" between the architecture and enterprise standards — a process that is substantially more involved when the architecture must certify compatibility with customer-controlled infrastructure. — [TOGAF ADM Architecture Compliance, visual-paradigm.com](https://togaf.visual-paradigm.com/2025/02/17/architecture-compliance-in-togaf-adm-ensuring-alignment-and-success/)

### Air-Gap Constraints on AI Architecture

For regulated on-premises customers (defense, government, healthcare), air-gap compatibility is a hard requirement that eliminates any architecture relying on external API calls — including LLM inference, embedding APIs, model download registries, and telemetry endpoints. This forces the following design decisions at the architecture phase:

- All container images must be bundled and signed in a private registry
- Model weights must be pre-downloaded and included in the deployment bundle
- License validation must work offline (no phone-home)
- Observability data must stay within the customer perimeter

[FACT] GitLab identifies healthcare, financial institutions, government agencies, and defense contractors operating in "air-gapped environments where cloud-only solutions are technically or legally infeasible" as its primary self-managed customer segments. — [GitLab Blog, Atlassian ending Data Center](https://about.gitlab.com/blog/atlassian-ending-data-center-as-gitlab-maintains-deployment-choice/)

---

## 8. Real-World ISV Examples

### Confluent: Portability as a Core Design Principle

Confluent explicitly architected its platform for deployment across "SaaS, on-prem, edge, hybrid, stretched across data centers, multi-cloud, [and] BYOC" — a deliberate design choice that required maintaining Confluent Platform (self-managed) as a separate product line alongside Confluent Cloud. — [kai-waehner.de, Past Present Future of Confluent and Databricks](https://www.kai-waehner.de/blog/2025/05/02/the-past-present-and-future-of-confluent-the-kafka-company-and-databricks-the-spark-company/)

[FACT] Confluent Platform "can be deployed for on-premise and private cloud workloads" while Confluent Cloud runs as fully managed SaaS. The on-premises architecture requires separate engineering investment to keep parity with cloud features. — [instaclustr.com, Kafka vs Confluent](https://www.instaclustr.com/education/apache-kafka/kafka-vs-confluent-6-differences-pros-cons-and-how-to-choose/)

[DATA POINT] Confluent Platform on-premises in 2025 supports "up to 400K partitions, refresh end-to-end metrics within 2-3 minutes, and cut start-up times to just 1 minute" — performance characteristics that required dedicated engineering investment separate from the cloud product. — [Confluent Documentation, Platform Overview](https://docs.confluent.io/platform/current/get-started/platform.html)

### Databricks: Cloud-Only Architecture Constraint

Databricks chose the opposite path. [FACT] "Databricks runs only in the cloud" — its platform "is not built for event-driven data distribution across hybrid environments." — [peerspot.com, Confluent vs Databricks 2025](https://www.peerspot.com/products/comparisons/confluent_vs_databricks)

This is a deliberate architectural decision: by removing on-premises from the design target, Databricks can fully exploit cloud-native managed services, auto-scaling, and serverless compute — achieving design velocity impossible in a portable architecture. The cost is that customers with on-premises or hybrid requirements must use Confluent for streaming and connect to Databricks, rather than using Databricks end-to-end. — [kai-waehner.de, Confluent vs Databricks Data Integration](https://www.kai-waehner.de/blog/2025/05/05/confluent-data-streaming-platform-vs-databricks-data-intelligence-platform-for-data-integration-and-processing/)

### Elastic: Hybrid Design via Cloud Connect

Elastic navigated the design tension differently — building a primary self-managed architecture (Elastic Stack) alongside Elastic Cloud, and recently bridging the two via Cloud Connect. [FACT] "Self-managed clusters can keep their existing architecture and data in place while securely offloading embedding generation and search inference to Elastic Cloud's managed GPU fleet." — [businesswire.com, Elastic Delivers GPU Infrastructure via Cloud Connect](https://www.businesswire.com/news/home/20260202349548/en/Elastic-Delivers-GPU-Infrastructure-to-Self-Managed-Elasticsearch-Customers-via-Cloud-Connect)

This "hybrid gateway" pattern — running core data on-premises while offloading inference to managed cloud endpoints — is an architectural middle path that requires design-time planning for data classification (what can egress), network security controls, and fallback behavior when the cloud endpoint is unreachable.

### GitLab: Reference Architecture as Design Artifact

GitLab publishes formal reference architectures for each deployment model, with distinct hardware and service topology requirements per scale tier. [FACT] GitLab's documentation states: "Running stateful components in Kubernetes, such as Postgres and Redis, is not supported" — a design constraint that forces on-premises and managed K8s deployments to route stateful services to VMs or dedicated nodes. — [GitLab Docs, Reference Architectures](https://docs.gitlab.com/administration/reference_architectures/)

[FACT] GitLab recommends "for environments serving 3,000 or more users, we generally recommend using an HA strategy" — a design decision that must be embedded in the reference architecture before deployment. — [GitLab Docs, Reference Architectures](https://docs.gitlab.com/administration/reference_architectures/)

[QUOTE] "GitLab remains committed to supporting the deployment choices that match your business needs." — [GitLab Blog, Atlassian ending Data Center](https://about.gitlab.com/blog/atlassian-ending-data-center-as-gitlab-maintains-deployment-choice/)

This commitment has a design cost: GitLab maintains three distinct architecture modes (Linux Package/Omnibus, Cloud Native Hybrid, Cloud Native First) — each requiring validated reference configurations, separate upgrade paths, and feature parity testing. — [GitLab Docs, Reference Architectures](https://docs.gitlab.com/administration/reference_architectures/)

---

## Comparison Table: Design-Phase Difficulty by Deployment Model

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|-------------------|-------------|-------------|--------------|
| **Database selection** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | PostgreSQL/MySQL on VMs | PostgreSQL via operator | Aurora, AlloyDB, Cosmos DB |
| | Manual HA design required | Helm-based HA operators | Auto-managed HA |
| | Est. FTE: 0.5 | Est. FTE: 0.25 | Est. FTE: 0.1 |
| **LLM Inference** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | GPU nodes, vLLM, MLOps | GPU pools, KServe/vLLM | API key + SDK |
| | Full hardware spec at design | Node pool sizing | Usage-based pricing |
| | Est. FTE: 1.5-2.0 | Est. FTE: 0.75-1.0 | Est. FTE: 0.1 |
| **Embedding pipeline** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted BGE/E5 + GPU | Self-hosted on GPU pools | OpenAI/Cohere API |
| | Model versioning + drift mgmt | Same + K8s deployment | Managed model updates |
| | Est. FTE: 0.75-1.0 | Est. FTE: 0.5 | Est. FTE: 0.1 |
| **Vector database** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Milvus/Qdrant OSS self-hosted | Helm-deployed Milvus/Qdrant | Pinecone/Weaviate Cloud |
| | Cluster tuning, index planning | K8s storage class selection | Index type only |
| | Est. FTE: 0.25-0.5 | Est. FTE: 0.1-0.25 | Est. FTE: 0.05 |
| **IaC / Abstraction layer** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Terraform multi-provider | Terraform + Helm | Terraform single-provider |
| | Full provider-agnostic design | K8s-native + cloud bridges | Cloud-native modules |
| | Est. FTE: 0.5-1.0 | Est. FTE: 0.25-0.5 | Est. FTE: 0.1-0.25 |
| **Observability stack** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Prometheus+Grafana+Loki stack | Same stack on K8s | CloudWatch/Azure Monitor |
| | Log routing, retention design | Helm-based deployment | Native integration |
| | Est. FTE: 0.25-0.5 | Est. FTE: 0.1-0.25 | Est. FTE: 0.05 |

*FTE estimates represent design-phase architect/engineering time for a mid-size deployment. On-call burden is excluded.*

---

## Key Takeaways

- **On-premises support is a first-principle design constraint, not a deployment option.** It must be decided before technology selection, as it eliminates cloud-native managed services (Pinecone, Bedrock, Aurora, serverless compute) from the design palette and replaces them with self-hosted equivalents requiring explicit hardware, HA, and operational design at architecture time.

- **AI applications face the harshest on-premises design penalty.** LLM inference, embedding generation, and vector storage are each designed for cloud API consumption in modern RAG pipelines. Targeting on-premises forces all three components to self-hosted alternatives, each requiring GPU infrastructure planning, MLOps expertise, and model lifecycle management — representing 2.5–4.0 FTE of design-phase and ongoing operational overhead that cloud-native designs avoid entirely.

- **The lowest-common-denominator problem is real and measurable.** Confluent (portable-first) and Databricks (cloud-only) represent opposite ends of this trade-off: Confluent maintains separate product lines and architecture tracks, while Databricks extracts maximum cloud-native value at the cost of on-premises feasibility. Neither path is universally correct — the decision must be driven by the target customer's deployment constraints.

- **Abstraction layers reduce but do not eliminate the portability tax.** Provider-agnostic patterns (Terraform multi-provider, Crossplane Composite Resources, service interface abstractions) enable code reuse across deployment targets but require 0.5–1.0 FTE of ongoing platform engineering and introduce observability gaps and debugging complexity absent in single-target architectures.

- **Architecture review gates multiply for on-premises targets.** Data residency verification, air-gap compatibility testing, hardware compatibility matrices, and license compliance reviews are all design-phase deliverables required for on-premises customers that cloud-native designs do not need — adding 1–4 weeks to design phase timelines for teams without established on-premises reference architectures.

---

## Related — Out of Scope

- **Build/test pipeline differences by deployment model** — See [F57] for CI/CD and testing constraints
- **Deployment automation and packaging** (Helm, Operator patterns, air-gap bundle construction) — See [F58]
- **Operational monitoring, incident response, upgrade procedures** by deployment model — See [F59]
- **K8s platform selection comparison** (EKS vs AKS vs GKE) — See [F52: Managed K8s Platforms]
- **ISV portability patterns and packaging strategies** — See [F53: Portable K8s ISV Delivery]
- **RAG pipeline architecture patterns** — See [F04: RAG Pipelines]
- **LLM model serving architecture** — See [F05: LLM Model Serving]
- **Vector database performance benchmarks** — See [F06: Vector Databases]

---

## Sources

1. [What "Cloud-Agnostic" Really Means in 2025 — fractal.cloud](https://fractal.cloud/blog/what-cloud-agnostic-really-means-in-2025-and-why-it-s-not-what-you-think)
2. [Cloud Agnostic vs Cloud Native: Which is Better in 2025 — binmile.com](https://binmile.com/blog/cloud-native-vs-cloud-agnostic/)
3. [Abstracted Service Layers Pattern — Software Patterns Lexicon](https://softwarepatternslexicon.com/cloud-computing/hybrid-cloud-and-multi-cloud-strategies/abstracted-service-layers/)
4. [LLM Inference as a Service vs Self-Hosted — deepsense.ai](https://deepsense.ai/blog/llm-inference-as-a-service-vs-self-hosted-which-is-right-for-your-business/)
5. [Serverless vs Self-Hosted LLM Inference — bentoml.com](https://bentoml.com/llm/llm-inference-basics/serverless-vs-self-hosted-llm-inference)
6. [Self-Hosted LLMs vs Cloud APIs Cost Comparison — dasroot.net](https://dasroot.net/posts/2026/01/self-hosted-llm-vs-cloud-apis-cost-performance/)
7. [RAG Infrastructure Production Guide — introl.com](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)
8. [Best Vector Databases 2025 — firecrawl.dev](https://www.firecrawl.dev/blog/best-vector-databases-2025)
9. [Best Embedding Models for RAG — greennode.ai](https://greennode.ai/blog/best-embedding-models-for-rag)
10. [Top Embedding Models 2025 — artsmart.ai](https://artsmart.ai/blog/top-embedding-models-in-2025/)
11. [PostgreSQL vs MySQL 2025 — nucamp.co](https://www.nucamp.co/blog/coding-bootcamp-backend-with-python-2025-postgresql-vs-mysql-in-2025-choosing-the-best-database-for-your-backend)
12. [Best DBaaS Solutions 2025 — dbvis.com](https://www.dbvis.com/thetable/best-database-as-a-service-dbaas-solutions-of-2025/)
13. [Terraform vs Pulumi vs Crossplane IaC Tool — platformengineering.org](https://platformengineering.org/blog/terraform-vs-pulumi-vs-crossplane-iac-tool)
14. [Crossplane Graduates CNCF — InfoQ](https://www.infoq.com/news/2025/11/crossplane-grad/)
15. [Past, Present, and Future of Confluent and Databricks — kai-waehner.de](https://www.kai-waehner.de/blog/2025/05/02/the-past-present-and-future-of-confluent-the-kafka-company-and-databricks-the-spark-company/)
16. [Confluent vs Databricks Data Integration — kai-waehner.de](https://www.kai-waehner.de/blog/2025/05/05/confluent-data-streaming-platform-vs-databricks-data-intelligence-platform-for-data-integration-and-processing/)
17. [Confluent vs Databricks 2025 — peerspot.com](https://www.peerspot.com/products/comparisons/confluent_vs_databricks)
18. [Confluent Platform Overview — docs.confluent.io](https://docs.confluent.io/platform/current/get-started/platform.html)
19. [Kafka vs Confluent — instaclustr.com](https://www.instaclustr.com/education/apache-kafka/kafka-vs-confluent-6-differences-pros-cons-and-how-to-choose/)
20. [Elastic Delivers GPU Infrastructure via Cloud Connect — businesswire.com](https://www.businesswire.com/news/home/20260202349548/en/Elastic-Delivers-GPU-Infrastructure-to-Self-Managed-Elasticsearch-Customers-via-Cloud-Connect)
21. [Elastic On-Premises Reference Architecture — DeepWiki](https://deepwiki.com/elastic/reference-architecture-docs/3.1-on-premises-deployments)
22. [GitLab Reference Architectures — docs.gitlab.com](https://docs.gitlab.com/administration/reference_architectures/)
23. [GitLab Blog: Atlassian ending Data Center — about.gitlab.com](https://about.gitlab.com/blog/atlassian-ending-data-center-as-gitlab-maintains-deployment-choice/)
24. [Build and Operate an Effective ARB — AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/build-and-operate-an-effective-architecture-review-board/)
25. [Architecture Review Board Checklist — hava.io](https://www.hava.io/blog/architecture-review-board-checklist)
26. [Architecture Compliance in TOGAF ADM — visual-paradigm.com](https://togaf.visual-paradigm.com/2025/02/17/architecture-compliance-in-togaf-adm-ensuring-alignment-and-success/)
27. [12-Factor App Methodology Explained — bmc.com](https://www.bmc.com/blogs/twelve-factor-app/)
28. [The Twelve-Factor App — 12factor.net](https://12factor.net/)
29. [Top 9 Vector Databases February 2026 — shakudo.io](https://www.shakudo.io/blog/top-9-vector-databases)
30. [AlloyDB Omni / Azure HorizonDB PostgreSQL — InfoWorld](https://www.infoworld.com/article/4093191/azure-horizondb-microsoft-goes-big-with-postgresql.html)
