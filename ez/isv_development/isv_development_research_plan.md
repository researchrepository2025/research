# ISV Software Development: On-Prem vs Cloud-Native Research Plan

## Purpose

Deep-dive research into what makes software development and ongoing management difficult with a 100% on-premises model, compared to cloud-native services and managed Kubernetes. Focused on AI-driven applications (LLM-powered apps and general SaaS with AI features) from the ISV perspective — developing applications deployed to customer on-premises hardware.

## Research Parameters

- **Audience:** Mixed (C-suite + technical leadership), layered with summaries and deep-dives
- **AI Focus:** LLM-powered apps + general SaaS with AI features
- **Comparison Model:** Three-tier (100% on-prem → Managed K8s → Fully cloud-native)
- **Analysis Framing:** Capability domains (primary), SDLC phases (secondary), ISV business impact (tertiary)
- **Output Phases:** (1) Modular research files → (2) Comparison matrix + narrative → (3) Structured research document
- **Citation Requirement:** ALL output files — research agents, wave summaries, integration files, comparison matrix, and final document — must have heavy inline citations with direct URLs for all data, claims, statistics, ratings, and quotes. Citations must be preserved through every synthesis layer; no file may summarize away the source URLs. Every file must end with a "Sources" section listing all referenced URLs.

## Agent Summary

| Wave | Agents | Count | Focus |
|------|--------|-------|-------|
| Wave 1 | F1–F7 | 7 | Foundation application patterns & AI architecture |
| Wave 2 | F8–F15a | 9 | AWS cloud-native managed services |
| Wave 3 | F16–F23a | 9 | Azure cloud-native managed services |
| Wave 4 | F24–F31a | 9 | GCP cloud-native managed services |
| Wave 5 | F32–F38 | 7 | On-prem application pattern operational profiles |
| Wave 6 | F39–F51 | 13 | On-prem infrastructure domain operational profiles |
| Wave 7 | F52–F55d | 8 | Managed K8s middle tier (platforms, delivery, operators, mesh, data, GPU, security, observability) |
| Wave 8 | F56–F60 | 5 | SDLC phase cross-cutting analysis |
| Wave 9 | F61–F66 | 6 | ISV business impact |
| Wave 10 | F67–F71 | 5 | Cross-cutting gaps (compliance, AI safety, training, DR, security ops) |
| **Subtotal** | | **78** | Research agents |
| Synthesis | W1S–W10S, X1–X3, S1, S2 | 15 | Wave summaries (10), cross-domain integration (3), final outputs (2) |
| **Grand Total** | | **93** | |

## Standard Agent Instructions (included with every agent prompt)

```
CONTEXT: You are a fact-finding research agent working on a strategic analysis for an ISV
(independent software vendor) that builds AI-driven SaaS applications. The ISV is evaluating
three deployment models: (1) 100% on-premises deployment to customer hardware, (2) managed
Kubernetes (EKS/AKS/GKE), and (3) fully cloud-native using managed services.

The research audience is mixed — C-suite executives and technical leadership — so findings
must be accessible at a summary level but backed by technical depth.

OUTPUT REQUIREMENTS:
- Write in markdown format
- Begin with a 3-5 sentence executive summary of key findings
- Use clear section headers for each sub-topic
- EVERY factual claim, statistic, quote, or technical specification MUST include an inline
  citation with a direct URL in the format: [description](URL)
- If you cannot find a citation for a claim, explicitly mark it as [UNVERIFIED] and explain
  why you believe it to be true
- Include a "Sources" section at the end listing all referenced URLs
- Target 1500-2500 words per research file
- Use tables for comparative data where appropriate
- End with a "Key Takeaways" section of 3-5 bullet points

SCOPE DISCIPLINE: Stay strictly within your assigned scope boundary. If you encounter
relevant information outside your scope, note it briefly in a "Related — Out of Scope"
section at the end but do NOT investigate it further.

TERMINOLOGY GLOSSARY (use consistently):
- "On-premises" (not "on-prem" in body text; "on-prem" acceptable in tables/headers only)
- "Managed Kubernetes" = cloud-hosted K8s control plane (EKS, AKS, GKE) with self-managed workloads
- "Cloud-native" = fully managed services (serverless, PaaS, SaaS) where the cloud provider manages infrastructure
- "Self-hosted" = software deployed and operated by the ISV or customer on their own infrastructure
- "Operational profile" = the full set of tasks, skills, tools, and time required to run a system
- "ISV" = Independent Software Vendor — a company that builds and sells software products

DIFFICULTY RATING SCALE (use in all comparative sections):
Rate each capability domain on a 1-5 scale for operational difficulty in each deployment model:
  1 = Trivial: Fully managed, no operational knowledge needed (e.g., S3 object storage)
  2 = Low: Managed with minor configuration (e.g., RDS with automated backups)
  3 = Moderate: Requires dedicated expertise, periodic attention (e.g., managed K8s cluster)
  4 = High: Requires specialized staff, significant ongoing effort (e.g., self-hosted Kafka cluster)
  5 = Very High: Requires deep expertise, constant attention, high failure risk (e.g., self-hosted GPU cluster for LLM inference)

FTE ESTIMATION FRAMEWORK:
When estimating operational staffing, use this framework:
- State assumptions (e.g., "for a mid-size deployment serving 50 enterprise customers")
- Express as FTE ranges (e.g., "0.25-0.5 FTE" not "part-time")
- Include on-call burden separately from active work
- Cite industry benchmarks where available (Gartner, Forrester, vendor case studies)

COMPARISON TABLE TEMPLATE (use when comparing deployment models):
| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| [Domain]   | Difficulty: X/5 | Difficulty: X/5 | Difficulty: X/5 |
|            | Key requirements | Key requirements | Key requirements |
|            | Representative tools | Representative tools | Representative services |
|            | Est. FTE: X.X | Est. FTE: X.X | Est. FTE: X.X |

SOURCE QUALITY AND PRIORITY:
- Tier 1 (highest priority): Official vendor documentation, peer-reviewed research, industry reports (Gartner, Forrester, IDC, Bessemer)
- Tier 2: Well-sourced technical blogs (from practitioners at named companies), conference talks with published proceedings, CNCF surveys/reports
- Tier 3: Community blogs, Stack Overflow data, Reddit discussions — use only to corroborate T1/T2 findings
- ALL sources MUST be from 2025 or later (2025-2026). Do NOT use any source published before 2025. If the only available source for a critical claim is pre-2025, mark it as [PRE-2025: YYYY] and explicitly note that no 2025+ source was found — then continue searching for a current source before falling back.
- If T1/T2 sources conflict, report both positions and note the disagreement

CONFLICT HANDLING:
When sources disagree, do NOT silently choose one. Instead:
- State both positions with citations
- Note the likely reason for disagreement (different scale, different use case, dated source)
- If one position has stronger evidence, note that, but present both

CROSS-REFERENCE FORMAT:
When referencing findings from other agents in this research plan, use the format:
"See [F##: Agent Title] for detailed coverage of [topic]."
Do NOT re-research topics covered by other agents — reference them.
```

---

## Wave 1 — Foundation Application Patterns (F1–F7)

All agents in this wave follow the Standard Agent Instructions above, including full inline citation requirements with direct URLs.

### F1: Microservices Architecture Patterns

**Research Question:**

How are modern SaaS applications architecturally decomposed using microservices patterns, and what does this mean for the total number of independently deployable services in a typical enterprise application?

**Required Sub-Topics:**
- Core decomposition patterns: domain-driven design (DDD) bounded contexts, strangler fig, database-per-service
- Communication patterns: synchronous (REST, gRPC) vs asynchronous (event-driven, message queues)
- Data isolation strategies: saga pattern, eventual consistency, CQRS
- Real-world service counts: how many microservices do typical enterprise SaaS products run? (cite specific examples — for example, Salesforce, Adobe, ServiceNow) how many microservices do typical small and medium-sized enterprise SaaS products run? (cite specific examples — for example, Glean, Harvey, Jasper)
- The "microservices tax": what infrastructure does each additional service require (its own CI pipeline, monitoring, logging, health checks, load balancer config, service registry entry)?
- Anti-patterns and complexity thresholds: when does microservices decomposition create more problems than it solves?

**Scope Boundary:** Architecture patterns and decomposition decisions ONLY. Do not cover deployment infrastructure, container orchestration, or cloud services. Do not cover AI-specific patterns.

---

### F2: Event-Driven Architecture & Asynchronous Messaging

**Research Question:**

How do event-driven architecture patterns work in modern distributed applications, and what infrastructure components are required to support them reliably at scale?

**Required Sub-Topics:**
- Core patterns: event sourcing, CQRS, publish-subscribe, event streaming vs message queuing
- Infrastructure requirements: what systems are needed (message brokers, event stores, schema registries, dead-letter queues)?
- Reliability guarantees: exactly-once delivery, ordering guarantees, idempotency — what is required to achieve each?
- Operational complexity: partition management, consumer group coordination, backpressure handling, replay capabilities
- Scale considerations: throughput limits, storage requirements for event logs, retention policies
- Common platforms: Apache Kafka, RabbitMQ, NATS, Apache Pulsar — capabilities and architectural role of each (operational management covered in F44)

**Scope Boundary:** Event-driven patterns and messaging infrastructure architecture ONLY. Do not cover general microservices decomposition (F1), message broker operational management (F44), compute/deployment (F39), or monitoring (F50).

---

### F3: API Gateways & Service Communication

**Research Question:**

How do API gateways, service meshes, and inter-service communication layers work in modern SaaS architectures, and what operational infrastructure do they require?

**Required Sub-Topics:**
- API gateway functions: routing, rate limiting, authentication, request transformation, protocol translation
- Service mesh architecture: sidecar proxies, control plane, data plane — how Envoy/Istio/Linkerd work
- Service discovery mechanisms: DNS-based, registry-based (Consul, etcd), K8s-native
- Load balancing strategies: L4 vs L7, client-side vs server-side, health checking
- mTLS and zero-trust networking: what's required for service-to-service encryption
- GraphQL federation and API composition: how multi-service APIs get presented as unified interfaces
- Operational overhead: configuration management, certificate rotation, proxy resource consumption

**Scope Boundary:** API layer and service-to-service communication ONLY. Do not cover application business logic (F1), networking infrastructure (F40), or security policy (F46).

---

### F4: RAG Pipelines & Retrieval Patterns

**Research Question:**

How are retrieval-augmented generation (RAG) pipelines architecturally constructed in production AI applications, and what infrastructure components does each stage of the pipeline require?

**Required Sub-Topics:**
- Pipeline stages: document ingestion → chunking → embedding generation → vector storage → retrieval → reranking → context assembly → LLM generation
- Infrastructure per stage: what systems/services are needed at each stage (object storage for docs, embedding model endpoints, vector databases, reranking models, LLM endpoints)?
- Chunking strategies: fixed-size, semantic, recursive — trade-offs and computational requirements
- Embedding model management: hosting embedding models, batching, versioning, re-embedding when models change
- Retrieval strategies: dense retrieval, sparse retrieval (BM25), hybrid search, metadata filtering
- Reranking: cross-encoder models, computational cost, latency impact
- Advanced patterns: multi-hop retrieval, agentic RAG, graph-based RAG, corrective RAG
- Scale considerations: document corpus size, index update frequency, query latency targets

**Scope Boundary:** RAG pipeline architecture ONLY. Do not cover LLM model serving (F5), vector database operations (F6), or agent frameworks (F7).

---

### F5: LLM Model Serving & Inference Infrastructure

**Research Question:**

What infrastructure is required to serve large language models for inference in production applications, and what are the operational demands of maintaining model serving at scale?

**Required Sub-Topics:**
- Model hosting options: self-hosted (vLLM, TGI, Triton) vs managed API endpoints (OpenAI, Anthropic, Bedrock, Vertex AI)
- GPU infrastructure requirements: GPU types (A100, H100, L40S), VRAM requirements by model size, multi-GPU serving
- Optimization techniques: quantization (GPTQ, AWQ, GGUF), KV-cache optimization, continuous batching, speculative decoding, tensor parallelism
- Latency management: time-to-first-token, tokens-per-second, batching trade-offs, streaming responses
- Model versioning and A/B testing: serving multiple model versions, traffic splitting, rollback
- Cost economics: GPU cost per token (self-hosted vs API), utilization optimization, spot/preemptible instances
- Multi-model serving: routing between different models based on task complexity, cost, latency
- Failover and redundancy: model endpoint health checking, fallback chains, rate limit management

**Scope Boundary:** Model serving architecture, capabilities, and cost economics ONLY. Focus on what infrastructure exists and how it works, not day-to-day on-prem operational challenges (covered in F36). Do not cover RAG (F4), embeddings/vector DBs (F6), or agent orchestration (F7).

---

### F6: Vector Databases & Embedding Management

**Research Question:**

How do vector databases and embedding workflows operate in production AI applications, and what are the operational requirements for maintaining them at scale?

**Required Sub-Topics:**
- Vector database landscape: Pinecone, Weaviate, Milvus, Qdrant, Chroma, pgvector — capabilities, hosting models, and operational requirements
- Index types: HNSW, IVF, PQ — trade-offs between recall, latency, and memory usage
- Embedding model management: model selection, dimensionality trade-offs, model versioning, re-embedding workflows when models change
- Operational demands: index building time, memory requirements, backup/restore, replication, sharding
- Hybrid search: combining dense vectors with sparse retrieval (BM25), metadata filtering, multi-modal embeddings
- Scale considerations: millions vs billions of vectors, query latency at scale, storage costs
- Data freshness: incremental indexing, real-time vs batch updates, consistency guarantees
- Self-hosted vs managed: operational burden comparison for each major vector DB

**Scope Boundary:** Vector database architecture, design choices, and embedding workflow design ONLY. Focus on architecture and selection criteria, not day-to-day operational pipeline management (F37 for embedding ops, F45 for vector DB ops on-prem). Do not cover RAG pipeline design (F4), model serving (F5), or general database operations (F41-F42).

---

### F7: AI Agent Frameworks & Multi-Agent Orchestration

**Research Question:**

How do AI agent frameworks and multi-agent orchestration systems work, and what infrastructure do they require beyond simple LLM API calls?

**Required Sub-Topics:**
- Framework landscape: LangChain, LangGraph, CrewAI, AutoGen, Semantic Kernel — architecture and capabilities of each
- Agent patterns: ReAct, function calling, tool use, planning-execution loops, reflection
- Multi-agent coordination: supervisor-worker, debate, handoff patterns, shared state management
- Tool integration: how agents call external APIs, databases, code execution environments — infrastructure needed
- State management: conversation memory, agent state persistence, checkpointing, long-running workflows
- Observability: tracing agent decision chains, debugging multi-step reasoning, cost tracking per agent run
- Infrastructure requirements: what beyond an LLM endpoint is needed — task queues, state stores, tool registries, execution sandboxes
- Production challenges: reliability, error recovery, cost control, latency budgets for multi-step agent chains

**Scope Boundary:** Agent frameworks and multi-agent orchestration ONLY. Do not cover model serving (F5), RAG (F4), or general application architecture (F1).

---

## Wave 2 — AWS Cloud-Native Managed Services (F8–F15)

Each agent covers one capability domain within AWS. For each service: document what it does, what operational burden it eliminates vs self-hosting, pricing model, and key limitations. Include direct URLs to official documentation.

---

### F8: AWS Compute Services

**Research Question:** What managed compute services does AWS provide for running application workloads and AI inference, and what operational burden does each eliminate?

**Required Sub-Topics:**
- AWS Lambda: serverless functions, cold start characteristics, concurrency limits, pricing model, GPU support status
- Amazon ECS + Fargate: container orchestration without managing EC2, task definitions, service auto-scaling
- AWS App Runner: source-to-URL deployment, auto-scaling, limitations vs ECS
- EC2 Auto Scaling: launch templates, scaling policies, spot instances, predictive scaling
- AWS Inferentia/Trainium: custom AI chips, Neuron SDK, supported models, cost vs GPU instances
- GPU instances (P5, G5, G6): instance types, availability, spot pricing, multi-GPU configurations
- AWS Batch: managed batch computing for ML training and data processing

**Scope Boundary:** AWS compute ONLY. No data services, no other providers.

---

### F9: AWS Data Services

**Research Question:** What managed data services does AWS provide for databases, caching, search, and storage, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Amazon RDS: managed PostgreSQL/MySQL, Multi-AZ, read replicas, automated backups, Aurora serverless
- Amazon DynamoDB: serverless NoSQL, auto-scaling, global tables, DAX caching, on-demand pricing
- Amazon ElastiCache: managed Redis/Memcached, cluster mode, replication, failover
- Amazon OpenSearch Service: managed Elasticsearch, UltraWarm storage tiers, serverless option
- Amazon Redshift: data warehouse, Redshift Serverless, ML integration
- Amazon S3: object storage, storage classes, lifecycle policies, versioning, event notifications
- Amazon EFS/FSx: managed file systems, NFS/Lustre/Windows support

**Scope Boundary:** AWS data services ONLY. No messaging (F15), no AI-specific (F10), no other providers.

---

### F10: AWS AI/ML Services

**Research Question:** What managed AI/ML services does AWS provide for LLM inference, embeddings, vector search, and ML pipelines, and what do they abstract away?

**Required Sub-Topics:**
- Amazon Bedrock: managed LLM access (Claude, Llama, Titan), fine-tuning, knowledge bases, agents, guardrails
- Amazon SageMaker: model training, hosting, endpoints, inference pipelines, JumpStart foundation models
- Amazon Titan Embeddings: embedding generation API, dimensions, pricing
- Amazon Kendra: enterprise search with ML ranking, connectors, RAG integration
- Amazon OpenSearch vector search: kNN plugin, vector engine, hybrid search
- Amazon Textract, Comprehend, Rekognition: document processing, NLP, computer vision
- Amazon Q: enterprise AI assistant, code generation
- SageMaker Ground Truth: data labeling, human-in-the-loop

**Scope Boundary:** AWS AI/ML services ONLY. No compute infrastructure (F8), no other providers.

---

### F11: AWS Security Services

**Research Question:** What managed security services does AWS provide for identity, encryption, secrets, and threat detection, and what operational burden does each eliminate?

**Required Sub-Topics:**
- AWS IAM: policies, roles, identity federation, cross-account access, SCPs
- Amazon Cognito: user pools, identity pools, hosted UI, social federation, MFA
- AWS KMS: key management, automatic rotation, envelope encryption, CloudHSM integration
- AWS Secrets Manager: secret rotation, RDS integration, cross-account sharing
- AWS Certificate Manager: free TLS certificates, automatic renewal, ALB integration
- AWS WAF: web application firewall, managed rule groups, bot control, rate limiting
- Amazon GuardDuty: threat detection, anomaly detection, integration with Security Hub
- AWS Security Hub: centralized security findings, compliance checks, automated remediation

**Scope Boundary:** AWS security services ONLY. No networking (F13), no other providers.

---

### F12: AWS Observability Services

**Research Question:** What managed observability services does AWS provide for logging, monitoring, tracing, and alerting, and what do they abstract away?

**Required Sub-Topics:**
- Amazon CloudWatch Logs: log ingestion, retention, Logs Insights query language, cross-account logging
- Amazon CloudWatch Metrics: custom metrics, anomaly detection, dashboards, alarms
- AWS X-Ray: distributed tracing, service map, trace analysis, sampling rules
- Amazon CloudWatch Application Signals: APM, SLO management
- Amazon Managed Grafana: managed Grafana with AWS data source integration
- Amazon Managed Prometheus: managed Prometheus-compatible monitoring, PromQL support
- AWS CloudTrail: API audit logging, event history, organization trails
- AWS Distro for OpenTelemetry: managed OTEL collector distribution

**Scope Boundary:** AWS observability ONLY. No security logging (F11), no other providers.

---

### F13: AWS Networking Services

**Research Question:** What managed networking services does AWS provide for load balancing, DNS, API management, and connectivity, and what do they abstract away?

**Required Sub-Topics:**
- Elastic Load Balancing: ALB (L7), NLB (L4), GWLB — features, health checks, TLS termination
- Amazon Route 53: DNS management, health checks, routing policies (weighted, geolocation, failover)
- Amazon API Gateway: REST and HTTP APIs, WebSocket, throttling, caching, authorization
- Amazon CloudFront: CDN, edge functions, origin shield, real-time logs
- Amazon VPC: subnets, security groups, NACLs, flow logs, VPC peering
- AWS PrivateLink: private connectivity to services, interface endpoints
- AWS Transit Gateway: multi-VPC connectivity, cross-region peering
- AWS App Mesh: managed service mesh, Envoy-based

**Scope Boundary:** AWS networking ONLY. No compute (F8), no other providers.

---

### F14: AWS CI/CD Services

**Research Question:** What managed CI/CD services does AWS provide for build, test, deploy, and artifact management, and what operational burden does each eliminate?

**Required Sub-Topics:**
- AWS CodePipeline: managed CI/CD orchestration, stages, actions, source integrations
- AWS CodeBuild: managed build service, custom build environments, GPU build support, caching
- AWS CodeDeploy: deployment automation, blue/green, canary, rollback
- Amazon ECR: managed container registry, vulnerability scanning, lifecycle policies, cross-region replication
- AWS CodeArtifact: managed artifact repository (npm, Maven, pip, NuGet), upstream proxying
- AWS CodeCommit (deprecated): migration path, alternatives
- AWS Proton: managed delivery service for container and serverless applications
- Integration with GitHub Actions: AWS credential management, OIDC federation

**Scope Boundary:** AWS CI/CD ONLY. No compute (F8), no other providers.

---

### F15: AWS Messaging Services

**Research Question:** What managed messaging and event streaming services does AWS provide, and what operational burden does each eliminate compared to self-hosted alternatives?

**Required Sub-Topics:**
- Amazon SQS: managed message queuing, standard vs FIFO, dead-letter queues, delay queues, long polling
- Amazon SNS: managed pub/sub, topic filtering, fanout patterns, mobile push
- Amazon EventBridge: serverless event bus, schema registry, event replay, partner integrations
- Amazon Kinesis Data Streams: real-time data streaming, sharding, enhanced fan-out, consumer management
- Amazon Kinesis Data Firehose: managed delivery to S3, Redshift, OpenSearch, Splunk
- Amazon MSK (Managed Streaming for Kafka): managed Kafka, Kafka Connect, schema registry
- Amazon MQ: managed ActiveMQ and RabbitMQ, migration from on-prem
- Step Functions: managed state machines for workflow orchestration

**Scope Boundary:** AWS messaging ONLY. No data services (F9), no other providers.

---

### F15a: AWS Per-Service Infrastructure Integration

**Research Question:** How do the 8 per-service infrastructure components integrate with and apply across all AWS managed service domains, and what does a production-ready service onboarding checklist look like for each service type?

**Required Sub-Topics:**
- **CI/CD pipeline per service type:** CodePipeline/CodeBuild/CodeDeploy patterns for Lambda, ECS/Fargate, App Runner, SageMaker endpoints — how deployment pipelines differ by compute model
- **Health-check endpoints:** How each compute service (Lambda, ECS, App Runner) exposes and consumes health-check endpoints (/health, /ready) — ALB target group health checks, Route 53 health checks, ECS container health checks, App Runner automatic health checking
- **Service registry and discovery:** AWS Cloud Map, ECS Service Discovery, App Mesh service discovery — how each compute service registers itself; DNS vs API discovery; integration with load balancers
- **Load balancer and ingress integration:** How each compute service type connects to ALB/NLB — target group registration, weighted routing, path-based routing per service; API Gateway integration patterns
- **Observability instrumentation per service:** Which AWS services emit CloudWatch metrics natively vs require SDK integration; X-Ray auto-instrumentation for Lambda, ECS, App Runner; OTEL collector patterns for each compute type; structured logging patterns per service
- **Container image lifecycle:** ECR integration patterns for ECS, App Runner, Lambda container images — build triggers, vulnerability scanning gates, lifecycle policies, promotion across environments
- **Secrets management integration:** How each service type (compute, data, AI/ML, messaging) accesses Secrets Manager and Parameter Store — ECS task definition secrets, Lambda environment variables, SageMaker endpoint secrets, RDS credential rotation
- **Service-level alerting patterns:** CloudWatch alarm patterns per service type — Lambda error rate and duration, ECS CPU/memory and task health, RDS connection count and replication lag, SageMaker endpoint latency, SQS queue depth — composite alarms for service-level SLOs

**Scope Boundary:** Cross-cutting per-service infrastructure integration across AWS ONLY. Do not re-research individual AWS services in depth (covered by F8-F15). Focus on integration patterns, checklists, and gaps.

---

## Wave 3 — Azure Cloud-Native Managed Services (F16–F23)

Each agent covers one capability domain within Azure. Same output requirements as Wave 2.

---

### F16: Azure Compute Services

**Research Question:** What managed compute services does Azure provide for running application workloads and AI inference, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Azure Functions: serverless, consumption vs premium plans, durable functions, cold start
- Azure Container Apps: managed container orchestration, KEDA scaling, Dapr integration, revision management
- Azure Container Instances: serverless containers, GPU support, virtual node integration
- Azure App Service: PaaS web hosting, deployment slots, auto-scaling, built-in auth
- Azure Kubernetes Service: managed K8s (covered in detail in F52, brief mention here for completeness)
- Azure GPU VMs (NC, ND, NV series): GPU instance types, availability, spot pricing
- Azure Batch: managed batch computing for HPC and ML workloads

**Scope Boundary:** Azure compute ONLY. No data services, no other providers.

---

### F17: Azure Data Services

**Research Question:** What managed data services does Azure provide for databases, caching, search, and storage, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Azure SQL Database: managed SQL Server, elastic pools, serverless tier, geo-replication, auto-tuning
- Azure Cosmos DB: multi-model NoSQL, global distribution, consistency levels, serverless, RU pricing
- Azure Cache for Redis: managed Redis, clustering, geo-replication, Enterprise tier
- Azure AI Search: full-text and vector search, semantic ranking, hybrid search, skillsets
- Azure Synapse Analytics: data warehouse, serverless SQL, Spark integration
- Azure Blob Storage: storage tiers (hot/cool/archive), lifecycle management, versioning, immutability
- Azure Files / Azure NetApp Files: managed file shares, SMB/NFS support

**Scope Boundary:** Azure data services ONLY. No messaging (F23), no AI-specific (F18), no other providers.

---

### F18: Azure AI/ML Services

**Research Question:** What managed AI/ML services does Azure provide for LLM inference, embeddings, vector search, and ML pipelines, and what do they abstract away?

**Required Sub-Topics:**
- Azure OpenAI Service: managed GPT-4/GPT-4o access, fine-tuning, content filtering, provisioned throughput
- Azure Machine Learning: model training, endpoints, MLflow integration, responsible AI dashboard
- Azure AI Search vector search: vector indexing, hybrid search, integrated vectorization
- Azure AI Document Intelligence: document processing, custom models, prebuilt models
- Azure Cognitive Services: speech, vision, language APIs
- Azure AI Studio: unified AI development platform, prompt flow, evaluation
- Azure AI Content Safety: content moderation, prompt shields

**Scope Boundary:** Azure AI/ML services ONLY. No compute infrastructure (F16), no other providers.

---

### F19: Azure Security Services

**Research Question:** What managed security services does Azure provide for identity, encryption, secrets, and threat detection, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Microsoft Entra ID (Azure AD): identity platform, conditional access, PIM, B2B/B2C
- Azure Key Vault: key management, secrets, certificates, managed HSM
- Azure Managed Certificates: free TLS certs for App Service and Front Door
- Microsoft Defender for Cloud: CSPM, CWPP, vulnerability assessment, compliance
- Azure Policy: governance, compliance enforcement, resource constraints
- Azure Sentinel: cloud-native SIEM, threat hunting, automated response
- Azure DDoS Protection: network-level DDoS mitigation
- Azure Confidential Computing: TEE-based workload protection

**Scope Boundary:** Azure security ONLY. No networking (F21), no other providers.

---

### F20: Azure Observability Services

**Research Question:** What managed observability services does Azure provide for logging, monitoring, tracing, and alerting, and what do they abstract away?

**Required Sub-Topics:**
- Azure Monitor: metrics, alerts, autoscale, action groups
- Azure Application Insights: APM, distributed tracing, live metrics, smart detection
- Azure Log Analytics: log ingestion, KQL query language, workspaces, retention
- Azure Managed Grafana: managed Grafana with Azure Monitor integration
- Azure Managed Prometheus: managed Prometheus for AKS, PromQL support
- Azure Monitor Network Insights: network monitoring, connection monitor
- Azure Activity Log: control plane audit logging
- Azure Workbooks: interactive reporting and visualization

**Scope Boundary:** Azure observability ONLY. No security monitoring (F19), no other providers.

---

### F21: Azure Networking Services

**Research Question:** What managed networking services does Azure provide for load balancing, DNS, API management, and connectivity, and what do they abstract away?

**Required Sub-Topics:**
- Azure Load Balancer: L4 load balancing, health probes, HA ports
- Azure Application Gateway: L7 load balancing, WAF integration, URL routing, SSL termination
- Azure Front Door: global load balancing, CDN, WAF, edge routing
- Azure DNS: DNS hosting, private DNS zones, alias records
- Azure API Management: API gateway, developer portal, policies, rate limiting, caching
- Azure VNet: subnets, NSGs, service endpoints, private endpoints
- Azure Private Link: private connectivity to PaaS services
- Azure ExpressRoute / VPN Gateway: hybrid connectivity

**Scope Boundary:** Azure networking ONLY. No compute (F16), no other providers.

---

### F22: Azure CI/CD Services

**Research Question:** What managed CI/CD services does Azure provide for build, test, deploy, and artifact management, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Azure DevOps Pipelines: managed CI/CD, YAML pipelines, self-hosted vs Microsoft-hosted agents, parallel jobs
- Azure DevOps Repos: managed Git, branch policies, pull request workflows
- Azure Container Registry: managed registry, tasks (automated builds), geo-replication, content trust
- Azure Artifacts: managed feed for npm, NuGet, Maven, pip, Universal packages
- GitHub Actions (Microsoft-owned): integration with Azure, OIDC, larger runners
- Azure Deployment Environments: managed dev infrastructure provisioning
- Azure DevOps Test Plans: managed testing, manual and automated test management
- Azure Resource Manager / Bicep: infrastructure-as-code deployment

**Scope Boundary:** Azure CI/CD ONLY. No compute (F16), no other providers.

---

### F23: Azure Messaging Services

**Research Question:** What managed messaging and event streaming services does Azure provide, and what operational burden does each eliminate compared to self-hosted alternatives?

**Required Sub-Topics:**
- Azure Service Bus: managed message broker, queues and topics, sessions, transactions, dead-lettering
- Azure Event Hubs: managed event streaming (Kafka-compatible), capture to storage, partitions, consumer groups
- Azure Event Grid: serverless event routing, filtering, retry policies, dead-lettering
- Azure Queue Storage: simple queue service, integration with Functions
- Azure Stream Analytics: real-time stream processing, SQL-like queries, windowing functions
- Azure Logic Apps: managed workflow orchestration, 400+ connectors
- Azure Durable Functions: stateful function orchestration, fan-out/fan-in patterns
- Schema Registry (Event Hubs): schema management for event-driven architectures

**Scope Boundary:** Azure messaging ONLY. No data services (F17), no other providers.

---

### F23a: Azure Per-Service Infrastructure Integration

**Research Question:** How do the 8 per-service infrastructure components integrate with and apply across all Azure managed service domains, and what does a production-ready service onboarding checklist look like for each service type?

**Required Sub-Topics:**
- **CI/CD pipeline per service type:** Azure Pipelines/GitHub Actions patterns for Functions, Container Apps, App Service, AKS, Azure ML endpoints — how deployment pipelines differ by compute model
- **Health-check endpoints:** How each compute service (Functions, Container Apps, App Service, AKS) exposes and consumes health-check endpoints — Azure Load Balancer health probes, App Gateway health probes, Container Apps built-in health checks, App Service health check feature, AKS liveness/readiness probes
- **Service registry and discovery:** Container Apps Dapr service discovery, AKS CoreDNS and K8s service discovery, Azure DNS Private Zones for PaaS services, API Management as service facade — how each compute service registers and discovers other services
- **Load balancer and ingress integration:** How each compute service type connects to Azure Load Balancer, App Gateway, Front Door — backend pool configuration, URL routing, traffic splitting per revision, APIM integration patterns
- **Observability instrumentation per service:** Which Azure services emit Azure Monitor metrics natively vs require SDK integration; Application Insights auto-instrumentation for Functions, App Service, Container Apps; OpenTelemetry patterns for each compute type; structured logging to Log Analytics per service
- **Container image lifecycle:** ACR integration patterns for Container Apps, App Service (container), AKS, Functions on containers — ACR Tasks for automated builds, image promotion across environments, vulnerability scanning gates, Notary content trust
- **Secrets management integration:** How each service type accesses Key Vault — Managed Identity for Functions, App Service, Container Apps, AKS (CSI driver); Key Vault references in App Configuration; Cosmos DB and SQL Database connection string management; Event Hubs/Service Bus RBAC vs connection string patterns
- **Service-level alerting patterns:** Azure Monitor alert rule patterns per service type — Functions execution errors and duration, Container Apps replica health and request latency, SQL Database DTU/vCore utilization, Cosmos DB RU consumption, Service Bus queue depth — action groups for service-level SLOs

**Scope Boundary:** Cross-cutting per-service infrastructure integration across Azure ONLY. Do not re-research individual Azure services in depth (covered by F16-F23). Focus on integration patterns, checklists, and gaps.

---

## Wave 4 — GCP Cloud-Native Managed Services (F24–F31)

Each agent covers one capability domain within GCP. Same output requirements as Wave 2.

---

### F24: GCP Compute Services

**Research Question:** What managed compute services does GCP provide for running application workloads and AI inference, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Cloud Functions (2nd gen): serverless functions, event-driven, concurrency, min instances
- Cloud Run: serverless containers, auto-scaling to zero, GPU support, jobs
- GKE Autopilot: fully managed K8s mode (covered in detail in F52, brief mention here)
- Compute Engine: VM instances, preemptible/spot, sole-tenant nodes, custom machine types
- TPU v5e/v5p: tensor processing units for AI training and inference, Pod slices
- GPU instances (A3, G2): GPU types, availability, pricing
- Cloud Batch: managed batch computing for HPC/ML

**Scope Boundary:** GCP compute ONLY. No data services, no other providers.

---

### F25: GCP Data Services

**Research Question:** What managed data services does GCP provide for databases, caching, search, and storage, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Cloud SQL: managed PostgreSQL/MySQL/SQL Server, HA, read replicas, automated backups
- Cloud Spanner: globally distributed relational DB, horizontal scaling, strong consistency
- Firestore: serverless document DB, real-time sync, offline support
- Memorystore: managed Redis/Memcached, HA, auto-failover
- Bigtable: wide-column NoSQL, low-latency at scale
- BigQuery: serverless data warehouse, ML integration, streaming ingestion
- Cloud Storage: object storage, storage classes, lifecycle management, signed URLs
- Filestore: managed NFS file storage

**Scope Boundary:** GCP data services ONLY. No messaging (F31), no AI-specific (F26), no other providers.

---

### F26: GCP AI/ML Services

**Research Question:** What managed AI/ML services does GCP provide for LLM inference, embeddings, vector search, and ML pipelines, and what do they abstract away?

**Required Sub-Topics:**
- Vertex AI: unified ML platform, model garden, custom training, prediction endpoints, pipelines
- Gemini API: managed LLM access, function calling, multimodal, grounding
- Vertex AI Vector Search: managed vector similarity search, streaming updates, filtering
- Document AI: document processing, custom processors, human-in-the-loop
- Vertex AI Agent Builder: RAG, search, conversation agents
- AutoML: no-code model training for vision, text, tabular
- Vertex AI Workbench: managed Jupyter notebooks
- Model Garden: pre-trained model deployment (Llama, Gemma, etc.)

**Scope Boundary:** GCP AI/ML services ONLY. No compute infrastructure (F24), no other providers.

---

### F27: GCP Security Services

**Research Question:** What managed security services does GCP provide for identity, encryption, secrets, and threat detection, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Cloud IAM: roles, policies, workload identity federation, organization policies
- Identity Platform: authentication for applications, multi-tenancy, OIDC/SAML federation
- Cloud KMS: key management, automatic rotation, HSM-backed keys, envelope encryption
- Secret Manager: secret versioning, automatic rotation, IAM-based access control
- Certificate Manager: managed TLS certificates, DNS authorization, load balancer integration
- Security Command Center: vulnerability scanning, threat detection, compliance monitoring
- Cloud Armor: WAF, DDoS protection, adaptive protection, bot management
- BeyondCorp Enterprise: zero-trust access, context-aware access policies

**Scope Boundary:** GCP security ONLY. No networking (F29), no other providers.

---

### F28: GCP Observability Services

**Research Question:** What managed observability services does GCP provide for logging, monitoring, tracing, and alerting, and what do they abstract away?

**Required Sub-Topics:**
- Cloud Logging: log ingestion, log router, log analytics, log-based metrics, retention
- Cloud Monitoring: metrics, dashboards, uptime checks, alerting policies, SLO monitoring
- Cloud Trace: distributed tracing, latency analysis, integration with Cloud Run/GKE
- Error Reporting: automatic error grouping, notification, stack trace analysis
- Managed Prometheus: managed Prometheus for GKE, PromQL, Grafana integration
- Cloud Profiler: continuous CPU and heap profiling in production
- Cloud Debugger (deprecated) → Snapshot Debugger alternatives
- Operations Suite integration: unified view across logging, monitoring, tracing

**Scope Boundary:** GCP observability ONLY. No security logging (F27), no other providers.

---

### F29: GCP Networking Services

**Research Question:** What managed networking services does GCP provide for load balancing, DNS, API management, and connectivity, and what do they abstract away?

**Required Sub-Topics:**
- Cloud Load Balancing: global L7, regional L4, internal, SSL proxy, TCP proxy — unified platform
- Cloud DNS: managed DNS, DNSSEC, private zones, routing policies
- Cloud CDN: content delivery, cache invalidation, signed URLs, edge security
- API Gateway / Apigee: API management, developer portal, analytics, monetization
- VPC: subnets, firewall rules, shared VPC, VPC peering, Private Google Access
- Private Service Connect: private connectivity to Google and third-party services
- Cloud Interconnect / Cloud VPN: hybrid connectivity, dedicated vs partner interconnect
- Traffic Director: managed service mesh control plane, xDS API

**Scope Boundary:** GCP networking ONLY. No compute (F24), no other providers.

---

### F30: GCP CI/CD Services

**Research Question:** What managed CI/CD services does GCP provide for build, test, deploy, and artifact management, and what operational burden does each eliminate?

**Required Sub-Topics:**
- Cloud Build: managed CI/CD, build triggers, custom builders, private pools, build caching
- Artifact Registry: managed artifact and container registry, vulnerability scanning, multi-format support
- Cloud Deploy: managed continuous delivery for GKE, Cloud Run, custom targets, approval gates
- Source Repositories (deprecated): migration path, GitHub/GitLab integration
- Skaffold: local and CI/CD development workflow for Kubernetes
- Integration with GitHub/GitLab: Cloud Build triggers, workload identity federation
- Terraform on GCP: managed Terraform state, deployment automation
- Binary Authorization: container image signature verification

**Scope Boundary:** GCP CI/CD ONLY. No compute (F24), no other providers.

---

### F31: GCP Messaging Services

**Research Question:** What managed messaging and event streaming services does GCP provide, and what operational burden does each eliminate compared to self-hosted alternatives?

**Required Sub-Topics:**
- Cloud Pub/Sub: managed messaging, at-least-once delivery, dead-lettering, ordering keys, BigQuery subscriptions
- Cloud Pub/Sub Lite: zonal messaging for cost-sensitive high-volume use cases
- Cloud Tasks: managed task queues, rate limiting, retry policies, HTTP/App Engine targets
- Dataflow (Apache Beam): managed stream and batch processing, auto-scaling, templates
- Eventarc: event-driven architecture, Cloud Audit Logs triggers, direct/third-party events
- Workflows: managed workflow orchestration, step functions, connectors, error handling
- Cloud Scheduler: managed cron jobs, HTTP/Pub-Sub/App Engine targets
- Managed Kafka (preview): managed Apache Kafka on GCP, compatibility with existing Kafka tools

**Scope Boundary:** GCP messaging ONLY. No data services (F25), no other providers.

---

### F31a: GCP Per-Service Infrastructure Integration

**Research Question:** How do the 8 per-service infrastructure components integrate with and apply across all GCP managed service domains, and what does a production-ready service onboarding checklist look like for each service type?

**Required Sub-Topics:**
- **CI/CD pipeline per service type:** Cloud Build/Cloud Deploy patterns for Cloud Functions, Cloud Run, GKE Autopilot, Vertex AI endpoints — how deployment pipelines differ by compute model
- **Health-check endpoints:** How each compute service (Cloud Functions, Cloud Run, GKE) exposes and consumes health-check endpoints — Cloud Load Balancing health checks (TCP/HTTP/gRPC), Cloud Run automatic health checking, GKE liveness/readiness/startup probes, uptime checks in Cloud Monitoring
- **Service registry and discovery:** GKE CoreDNS and K8s service discovery, Cloud Run service URLs, Traffic Director service mesh discovery, Cloud DNS Private Zones for managed services — how each compute service registers and discovers other services
- **Load balancer and ingress integration:** How each compute service type connects to Cloud Load Balancing — backend services, URL maps, NEGs for serverless, Traffic Director for mesh routing, Apigee as API gateway
- **Observability instrumentation per service:** Which GCP services emit Cloud Monitoring metrics natively vs require SDK integration; Cloud Trace auto-instrumentation for Cloud Run, GKE, Cloud Functions; OpenTelemetry patterns for each compute type; structured logging to Cloud Logging per service
- **Container image lifecycle:** Artifact Registry integration patterns for Cloud Run, GKE, Cloud Functions (2nd gen) — Cloud Build triggers, vulnerability scanning (Container Analysis), Binary Authorization for admission control, image promotion across environments
- **Secrets management integration:** How each service type accesses Secret Manager — Workload Identity for GKE, Secret Manager environment variables for Cloud Run and Cloud Functions, Cloud SQL IAM authentication, Pub/Sub IAM vs service account patterns
- **Service-level alerting patterns:** Cloud Monitoring alerting policy patterns per service type — Cloud Functions execution errors and latency, Cloud Run request latency and container instance count, Cloud SQL CPU and connection count, BigQuery slot utilization, Pub/Sub subscription backlog — SLO monitoring service for service-level objectives

**Scope Boundary:** Cross-cutting per-service infrastructure integration across GCP ONLY. Do not re-research individual GCP services in depth (covered by F24-F31). Focus on integration patterns, checklists, and gaps.

---

## Wave 5 — On-Prem Application Pattern Challenges (F32–F38)

These agents mirror F1-F7 and address the operational profile of each application-level pattern when implemented 100% on-premises. They focus on the APPLICATION-LEVEL operational characteristics, not the infrastructure operations (covered in Wave 6). All agents follow Standard Agent Instructions including full inline citation requirements with direct URLs.

---

### F32: On-Prem Microservices Lifecycle Management

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of managing dozens to hundreds of microservices in a 100% on-premises environment without cloud-native orchestration, and how does the "microservices tax" compound without managed services?

**Required Sub-Topics:**
- Container orchestration without managed K8s: self-hosted Docker Swarm, Nomad, or bare K8s — what each requires to operate
- Service deployment at scale: deploying updates across 50-500 services without managed CI/CD and container registries
- Service scaling: manual scaling decisions, resource allocation without auto-scaling, capacity planning per service
- Health management: health checks, restart policies, circuit breakers, graceful degradation without cloud-native tooling
- Configuration management: distributing config to hundreds of services — Consul KV, etcd, custom solutions vs cloud parameter stores (service discovery and service-to-service communication covered in F34)
- Dependency management: tracking inter-service dependencies, managing version compatibility across services
- The compounding effect: each additional microservice multiplies operational burden — quantify with examples
- **Per-service infrastructure requirements on-prem (Section 5.1 components):**
  - CI/CD pipeline per service: self-hosted Jenkins/GitLab CI pipeline per microservice — build, test, containerize, deploy; configuration drift across dozens of pipelines
  - Health-check endpoints: implementing /health and /ready endpoints per service without cloud load balancer integration — custom health aggregation, restart policies
  - Service-level alerting rules: configuring Prometheus/Alertmanager rules per service for SLO/SLI monitoring — alert fatigue, rule maintenance at scale
  - Container image and registry: self-hosted Harbor/GitLab Registry per service — image build, tag, push, retention policies, vulnerability scanning without managed ECR/ACR
  - Secrets management per service: distributing API keys and database credentials per service via Vault or manual config — rotation complexity, secret sprawl

**Scope Boundary:** Microservices lifecycle management at the APPLICATION level ONLY. Do not cover service discovery or service-to-service communication (F34), underlying compute infrastructure (F39), networking hardware (F40), or container orchestration platforms (Wave 7). Focus on managing the services themselves (deployment, scaling, health, configuration). For detailed coverage of CI/CD infrastructure see F48, secrets/encryption see F47, monitoring/alerting see F50 — this agent covers the per-service APPLICATION-LEVEL perspective of these infrastructure requirements.

---

### F33: On-Prem Event-Driven Architecture Implementation

**Research Question:**

Beyond operating message brokers (covered in F44), what are the requirements, operational characteristics, and trade-offs of implementing event-driven architecture patterns (event sourcing, CQRS, sagas) in a 100% on-premises environment?

**Required Sub-Topics:**
- Event store implementation: building durable event stores on-prem — Kafka as event store, EventStoreDB, or custom — without managed event services
- Saga orchestration: implementing distributed transactions across services without managed workflow engines (Step Functions, Durable Functions)
- Schema registry operations: running Confluent Schema Registry or Apicurio — schema evolution, compatibility enforcement, without managed registries
- Event replay and reprocessing: rebuilding read models, replaying events for debugging — infrastructure and tooling needed
- Dead letter queue management: handling failed events, retry policies, manual intervention workflows
- Event ordering guarantees: maintaining ordering across partitions, consumer group management, exactly-once semantics
- Cross-service event correlation: tracing events across services without cloud-native correlation tools
- Testing event-driven systems: testing async workflows, event contract testing — infrastructure requirements

**Scope Boundary:** Event-driven ARCHITECTURE PATTERNS on-prem ONLY. Do not cover message broker operations (F44), general microservices management (F32), or compute infrastructure (F39).

---

### F34: On-Prem API Gateway & Service Discovery

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of implementing API gateways, service-to-service communication, and traffic management in a 100% on-premises environment without cloud-native API management and load balancing?

**Required Sub-Topics:**
- Self-hosted API gateways: Kong, Tyk, KrakenD, APISIX — deployment, configuration, HA, plugin management
- Rate limiting and throttling: implementing rate limits without cloud API Gateway — distributed rate limiting across gateway instances
- Authentication at the gateway: JWT validation, OAuth2 integration, API key management without managed auth services
- Request routing and transformation: path-based routing, header manipulation, protocol translation — configuration complexity
- Service-to-service communication: direct gRPC, REST calls with service discovery — retry policies, timeouts, circuit breaking
- Traffic management: canary routing, traffic splitting, A/B testing — without cloud-native traffic management
- API versioning and lifecycle: managing multiple API versions, deprecation, consumer notification without managed developer portals
- Performance: gateway latency overhead, connection pooling, keep-alive management, TLS termination performance

**Scope Boundary:** API gateway, service discovery, and all service-to-service communication at the APPLICATION level ONLY. This agent owns service discovery (Consul, etcd, DNS-based) — F32 does not cover it. Do not cover network infrastructure (F40), K8s service mesh (F55), or general microservices lifecycle management (F32).

---

### F35: On-Prem RAG Pipeline Operations

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of operating a complete RAG pipeline in a 100% on-premises environment, where every stage must be self-hosted without managed AI services?

**Required Sub-Topics:**
- Document ingestion on-prem: processing PDFs, Office docs, web content — self-hosted Apache Tika, Unstructured.io — compute and storage requirements
- Chunking infrastructure: running chunking at scale — CPU requirements, queue management, parallel processing
- Embedding generation on-prem: self-hosting embedding models (sentence-transformers, instructor) — GPU allocation, batching, throughput optimization
- Vector storage and retrieval: connecting self-hosted vector DBs (F45) into the pipeline — index management, query optimization
- Reranking on-prem: self-hosting cross-encoder reranking models — additional GPU requirements, latency impact
- LLM generation on-prem: integrating self-hosted LLM inference (F36) as the generation stage — context window management
- Pipeline orchestration: coordinating all stages — workflow engines, retry logic, error handling without managed orchestration
- End-to-end latency: cumulative latency across self-hosted stages vs cloud-native (Bedrock Knowledge Bases, Azure AI Search + OpenAI)

**Scope Boundary:** RAG pipeline ORCHESTRATION and END-TO-END INTEGRATION on-prem ONLY. For pipeline stages handled by other agents (LLM inference → F36, embedding generation → F37, vector DB → F45), reference them as dependencies with a brief note on integration points but do NOT re-research their operational details. Do not cover RAG architecture design (F4).

---

### F36: On-Prem LLM Inference Operations

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of self-hosting large language model inference in a 100% on-premises environment, covering model deployment, GPU management, optimization, and multi-model serving?

**Required Sub-Topics:**
- Model serving frameworks: vLLM, Text Generation Inference (TGI), Triton Inference Server, Ollama — deployment, configuration, production readiness
- GPU procurement and allocation: obtaining H100/A100/L40S hardware, lead times, sharing GPUs between inference and embedding workloads
- Model optimization: quantization (GPTQ, AWQ, GGUF), Flash Attention, continuous batching — expertise required, quality trade-offs
- Multi-model serving: routing requests to different models (GPT-equivalent, smaller models, specialized models) — traffic management, model registry
- Model updates: deploying new model versions, A/B testing models, rollback — without managed model endpoints
- Cost management: GPU utilization monitoring, right-sizing, batch vs real-time inference trade-offs
- Latency optimization: KV-cache management, speculative decoding, tensor parallelism across GPUs — configuration complexity
- Failover: model endpoint health checking, fallback to smaller models, graceful degradation without managed failover

**Scope Boundary:** LLM inference OPERATIONS on-prem ONLY. Do not cover GPU hardware infrastructure (F39), model architecture/selection (F5), or RAG pipeline integration (F35).

---

### F37: On-Prem Embedding Pipeline Operations

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of operating embedding generation pipelines and managing embedding lifecycle on-premises without managed embedding APIs?

**Required Sub-Topics:**
- Self-hosted embedding models: sentence-transformers, instructor, BGE, Cohere-equivalent open models — deployment, GPU requirements, throughput
- Batch embedding at scale: processing millions of documents — queue management, GPU scheduling, progress tracking, failure recovery
- Re-embedding workflows: when embedding models change, re-embedding entire corpus — compute cost, downtime, parallel index management
- Embedding model versioning: tracking which model version generated which embeddings, migration strategies
- Real-time vs batch: real-time embedding for new documents vs batch for corpus — different infrastructure requirements
- GPU sharing: embedding models compete with LLM inference for GPU resources — scheduling and prioritization
- Quality monitoring: embedding quality metrics, drift detection, comparison between model versions
- Comparison to managed: OpenAI Embeddings API, Bedrock Titan Embeddings, Vertex Embeddings — what disappears with managed?

**Scope Boundary:** Embedding pipeline OPERATIONS ONLY. Do not cover vector database operations (F45), embedding architecture design (F6), or GPU infrastructure (F39).

---

### F38: On-Prem AI Agent Infrastructure

**Research Question:**

What infrastructure is required to run AI agent frameworks and multi-agent systems in a 100% on-premises environment, and what challenges arise without cloud-native orchestration and tool services?

**Required Sub-Topics:**
- Tool registry and execution: self-hosting tool registries, sandboxed code execution environments, API integration without managed function services
- State management: agent conversation state, workflow checkpoints, long-running agent persistence — self-hosted databases and caches
- Orchestration: running multi-agent coordination (supervisor patterns, handoffs) — task queues, state machines without managed workflow services
- Cost and usage tracking: monitoring token consumption, API calls, tool executions per agent run — self-hosted metering
- Security sandboxing: isolating agent tool execution, preventing prompt injection from executing dangerous operations — without cloud sandboxing
- Observability: tracing multi-step agent reasoning, debugging agent failures, logging decision chains — self-hosted tracing (F51) integration
- Scaling: handling concurrent agent sessions, queue management, GPU scheduling for agent LLM calls
- Comparison: LangSmith Cloud, Amazon Bedrock Agents, Azure AI Agent Service — what infrastructure disappears with managed?

**Scope Boundary:** AI agent INFRASTRUCTURE on-prem ONLY. Do not cover agent framework design (F7), LLM inference operations (F36), or general compute infrastructure (F39).

---

## Wave 6 — On-Prem Infrastructure Domain Challenges (F39–F51)

All agents in this wave follow the Standard Agent Instructions above, including full inline citation requirements with direct URLs.

### F39: On-Prem Compute Management

**Research Question:**

What is required to self-manage compute infrastructure (VMs, bare metal servers, and GPU hardware) in a 100% on-premises environment for an AI-SaaS application, and how do the operational characteristics and trade-offs compare to cloud compute services?

**Required Sub-Topics:**
- Hardware procurement and lifecycle: lead times for GPU servers (H100, A100), refresh cycles, capacity planning, vendor relationships
- Hypervisor management: VMware/KVM/Proxmox — licensing, patching, resource allocation, live migration
- GPU management: driver installation and updates, CUDA version management, multi-tenant GPU sharing (MIG, MPS, time-slicing)
- Resource scheduling: how to allocate CPU/memory/GPU across workloads without a cloud scheduler — Nomad, Slurm, manual
- Auto-scaling (or lack thereof): burst capacity, pre-provisioning vs over-provisioning, lead time for new hardware
- High availability: redundant hardware, failover, maintenance windows, hardware failure rates and MTTR
- Power, cooling, and physical infrastructure: data center requirements for GPU-heavy workloads
- Cost model: CapEx vs OpEx, depreciation, utilization rates, total cost of ownership benchmarks

**Scope Boundary:** Compute management ONLY. Do not cover networking (F40), storage (F43), or Kubernetes (Wave 7).

---

### F40: On-Prem Networking

**Research Question:**

What networking infrastructure must an ISV self-manage in a 100% on-premises deployment, and how do the operational characteristics and trade-offs compare to cloud networking services?

**Required Sub-Topics:**
- Load balancing: self-managed HAProxy/Nginx/F5 — configuration, health checking, SSL termination, session persistence
- DNS management: internal DNS, service discovery without cloud DNS, split-horizon DNS, TTL management
- Service discovery: Consul, etcd, or custom — registration, health checking, failure detection
- Ingress control: traffic routing, TLS termination, path-based routing, rate limiting without cloud ALB/NLB
- Network segmentation: VLANs, firewall rules, microsegmentation, east-west traffic control
- Network performance: bandwidth provisioning, latency between racks, jumbo frames, RDMA for GPU interconnects
- VPN and remote access: site-to-site VPN, remote developer access, branch connectivity
- Troubleshooting complexity: network debugging without cloud VPC flow logs, packet capture, distributed tracing of network issues
- **Health-check endpoint design and integration:** How ISVs implement /health and /ready endpoints per microservice and integrate them with self-hosted load balancers (HAProxy, Nginx, F5) and service registries (Consul) — health check polling intervals, failure thresholds, graceful drain, health aggregation dashboards, compared to cloud ALB/NLB automatic health check integration

**Scope Boundary:** Networking ONLY. Do not cover compute (F39), service mesh (F55), or security policy (F46).

---

### F41: On-Prem Relational Databases

**Research Question:**

What are the operational requirements, characteristics, and trade-offs of self-hosting relational databases (PostgreSQL, MySQL) in a production on-premises environment, and how does the operational profile compare to managed services like RDS/Azure SQL/Cloud SQL?

**Required Sub-Topics:**
- Installation and configuration: OS-level tuning, connection pooling (PgBouncer), WAL configuration, memory tuning
- High availability: streaming replication, Patroni/repmgr for automated failover, witness nodes, split-brain prevention
- Backup and recovery: pg_dump, pg_basebackup, WAL archiving, point-in-time recovery, backup testing, RTO/RPO targets
- Scaling: read replicas, connection limits, vertical scaling (downtime), sharding complexity (Citus)
- Patching and upgrades: major version upgrades (pg_upgrade), minor version patches, downtime requirements, testing matrix
- Monitoring: pg_stat_statements, connection monitoring, replication lag, disk space, query performance
- Security: authentication configuration, SSL/TLS, row-level security, audit logging, encryption at rest
- Operational staffing: DBA skills required, on-call burden, incident response for database emergencies

**Scope Boundary:** Relational database operations ONLY. Do not cover NoSQL (F42), application-level data patterns (F1), or backup infrastructure (F43).

---

### F42: On-Prem NoSQL & Caching

**Research Question:**

What are the operational requirements, characteristics, and trade-offs of self-hosting NoSQL databases and caching layers (Redis, MongoDB, Elasticsearch) on-premises, and how does the operational profile compare to managed equivalents?

**Required Sub-Topics:**
- **Redis:** Cluster mode configuration, sentinel for HA, persistence (RDB/AOF), memory management, eviction policies, replication
- **MongoDB:** Replica set management, sharding (config servers, mongos routers), WiredTiger tuning, backup/restore, compaction
- **Elasticsearch:** Cluster formation, shard allocation, index lifecycle management, heap sizing, GC tuning, rolling upgrades, snapshot/restore
- Cross-cutting challenges: version compatibility across cluster nodes, rolling upgrade procedures, data migration
- Memory management: sizing, OOM prevention, swap configuration, NUMA awareness
- Monitoring each system: cluster health, replication status, query performance, resource utilization
- Operational comparison: time and expertise required per system vs DynamoDB/CosmosDB/ElastiCache/OpenSearch Service

**Scope Boundary:** NoSQL and caching operations ONLY. Do not cover relational databases (F41), message queues (F44), or vector databases (F45).

---

### F43: On-Prem Object Storage & File Systems

**Research Question:**

What is required to self-host S3-compatible object storage and distributed file systems on-premises, and how does the operational profile compare to cloud object storage?

**Required Sub-Topics:**
- MinIO: deployment architecture, erasure coding, versioning, bucket policies, replication, hardware requirements
- Ceph: RADOS architecture, OSD management, CRUSH map, pool configuration, maintenance
- Distributed file systems: GlusterFS, Lustre — when needed vs object storage
- Data durability: replication strategies, erasure coding, bit-rot detection, scrubbing
- Performance: IOPS requirements, throughput tuning, caching tiers, NVMe vs HDD tiering
- Capacity management: expansion procedures, rebalancing, decommissioning nodes
- Backup and disaster recovery: cross-site replication, backup to tape/cold storage, RTO/RPO
- Comparison to cloud: S3/Blob/GCS — what ops burden is eliminated (durability, scaling, lifecycle policies, CDN integration)?

**Scope Boundary:** Object storage and file systems ONLY. Do not cover databases (F41-F42), compute (F39), or backup strategy as a whole.

---

### F44: On-Prem Message Queues & Event Streaming

**Research Question:**

What are the operational requirements, characteristics, and trade-offs of self-hosting message queues and event streaming platforms (Kafka, RabbitMQ, NATS) on-premises, and how does the operational profile compare to managed equivalents?

**Required Sub-Topics:**
- **Apache Kafka:** Cluster management (ZooKeeper/KRaft migration), broker configuration, partition rebalancing, ISR management, topic configuration, retention tuning
- **RabbitMQ:** Cluster formation, queue mirroring/quorum queues, memory management, shovel/federation, exchange/binding management
- **NATS:** JetStream configuration, clustering, message retention, consumer management
- Cross-cutting: disk sizing for retention, network bandwidth for replication, rolling upgrades, version compatibility
- Operational complexity: partition leadership election, consumer group rebalancing, dead letter handling, message replay
- Schema management: Schema Registry operation, schema evolution, compatibility checking
- Monitoring: consumer lag, broker health, disk usage, throughput metrics, alerting thresholds
- Comparison: operational hours per week vs MSK/Amazon MQ/Event Hubs/Pub-Sub

**Scope Boundary:** Message queues and event streaming ONLY. Do not cover event-driven architecture patterns (F2), application logic, or general networking (F40).

---

### F45: On-Prem Vector Databases & AI Data Infrastructure

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of self-hosting vector databases and AI data infrastructure on-premises, and how does the operational profile compare to managed AI services?

**Required Sub-Topics:**
- Self-hosted vector DBs: Milvus (etcd + MinIO + Pulsar dependencies), Weaviate (standalone or K8s), Qdrant, Chroma — deployment complexity of each
- Dependency chains: Milvus alone requires etcd, MinIO, and Pulsar — each needing their own operational management
- Index management: HNSW index build times, memory requirements, index persistence, recovery after failure
- Embedding integration: how vector DBs receive and index embeddings from the embedding pipeline (F37) — ingestion APIs, batch loading, real-time upsert
- GPU allocation for vector workloads: GPU-accelerated index operations (where applicable), resource isolation from inference workloads
- Scaling: adding nodes, resharding vector indices, rebalancing — procedures and downtime
- Comparison: Pinecone/Weaviate Cloud/Azure AI Search/Vertex Vector Search — what ops disappears with managed?

**Scope Boundary:** Vector databases and AI data infrastructure in on-prem context ONLY. Do not cover embedding pipeline operations (F37), general databases (F41-F42), model serving (F5), or RAG pipeline design (F4).

---

### F46: On-Prem IAM & Identity

**Research Question:**

What is required to implement identity and access management in a 100% on-premises environment for a multi-tenant SaaS application, and how does the operational profile compare to cloud IAM services?

**Required Sub-Topics:**
- Directory services: Active Directory/LDAP deployment, management, replication, schema extensions
- SSO and federation: OIDC/SAML implementation with Keycloak/Dex, identity provider integration
- Multi-tenant authentication: tenant isolation, custom identity providers per customer, B2B federation
- RBAC implementation: role hierarchies, permission models, policy engines (OPA/Cedar), policy distribution
- Service-to-service authentication: mTLS, JWT validation, API key management, service accounts
- Token management: issuance, rotation, revocation, token storage, session management
- Audit and compliance: authentication logging, access auditing, compliance reporting (SOC2, HIPAA)
- Comparison: AWS IAM + Cognito / Azure AD + B2C / Google IAM + Firebase Auth — what disappears with managed?

**Scope Boundary:** Identity and access management ONLY. Do not cover secrets/encryption (F47), network security (F40), or application-level auth logic.

---

### F47: On-Prem Secrets, Certificates & Encryption

**Research Question:**

What are the operational requirements, characteristics, and trade-offs of self-managing secrets, certificates, and encryption in an on-premises environment, and how does the operational profile compare to cloud KMS and managed certificate services?

**Required Sub-Topics:**
- Secrets management: HashiCorp Vault deployment (storage backend, HA, unsealing), secret rotation, dynamic secrets, policy management
- TLS certificates: internal CA management, cert-manager or manual, certificate rotation, chain of trust, wildcard vs per-service certs
- Encryption at rest: disk encryption (LUKS), database-level encryption (TDE), application-level encryption, key hierarchy
- Encryption in transit: mTLS configuration, TLS termination points, cipher suite management
- Key management: key generation, storage, rotation, backup, disaster recovery of encryption keys
- Hardware security modules: HSM procurement, integration, FIPS compliance requirements
- Certificate lifecycle: expiration tracking, automated renewal, revocation (CRL/OCSP), emergency rotation
- Comparison: AWS KMS + ACM + Secrets Manager / Azure Key Vault + Managed Certs / GCP KMS — what ops burden disappears?

**Scope Boundary:** Secrets, certificates, and encryption ONLY. Do not cover IAM (F46), network security (F40), or compliance frameworks.

---

### F48: On-Prem CI/CD Pipelines

**Research Question:**

What is required to self-host a complete CI/CD pipeline infrastructure on-premises, and how do the operational characteristics and trade-offs compare to managed CI/CD services?

**Required Sub-Topics:**
- CI server management: Jenkins/GitLab CI/Woodpecker — installation, scaling runners, plugin management, security patching
- Container registry: Harbor/GitLab Registry — storage, garbage collection, vulnerability scanning, access control
- Artifact management: Nexus/Artifactory — storage, retention policies, proxy caching, license compliance
- Build infrastructure: dedicated build agents, GPU-enabled build agents for AI workloads, build cache management
- Pipeline authoring: multi-stage pipelines, parallelization, shared libraries, environment promotion
- Testing infrastructure: self-hosted test environments, database fixtures, GPU access for ML model testing
- Air-gapped considerations: dependency mirroring, offline package repositories, image pre-pulling
- Comparison: GitHub Actions/Azure DevOps/Cloud Build + ECR/ACR/Artifact Registry — what ops disappears?

**Scope Boundary:** CI/CD pipeline infrastructure ONLY. Do not cover deployment strategies (F58), application code (F1), or monitoring (F49-F51).

---

### F49: On-Prem Logging & Log Aggregation

**Research Question:**

What is required to self-host centralized logging infrastructure on-premises at production scale, and how does the operational profile compare to managed logging services?

**Required Sub-Topics:**
- **ELK Stack:** Elasticsearch cluster for logs (separate from search), Logstash/Fluentd ingestion, Kibana dashboards — sizing, tuning, maintenance
- **Loki + Grafana:** Loki deployment, label strategy, chunk storage (local vs object store), retention management
- Log collection agents: Fluentd/Fluent Bit/Vector — deployment to every node, configuration management, resource overhead
- Storage scaling: log volume estimation (GB/day), retention policies, hot/warm/cold tiering, compression
- Performance: ingestion rate limits, query performance at scale, index optimization
- Multi-tenant log isolation: tenant-based access control, data segregation, compliance with data residency
- Log pipeline reliability: buffering, backpressure handling, delivery guarantees, dead-letter handling
- Comparison: CloudWatch Logs/Azure Monitor/Cloud Logging — what operational burden disappears (scaling, retention, querying)?

**Scope Boundary:** Logging and log aggregation ONLY. Do not cover monitoring/metrics (F50), tracing (F51), or security audit logs (F46).

---

### F50: On-Prem Monitoring & Alerting

**Research Question:**

What is required to self-host a monitoring and alerting stack on-premises, and how do the operational characteristics and trade-offs compare to managed monitoring services?

**Required Sub-Topics:**
- **Prometheus:** Deployment, storage (local TSDB), scaling (Thanos/Cortex/Mimir for HA and long-term storage), retention, federation
- **Grafana:** Dashboard management, datasource configuration, alerting rules, user management, provisioning
- **Alertmanager:** Routing, grouping, inhibition, silencing, notification channels (PagerDuty/Slack/email integration)
- Metric collection: node-exporter, kube-state-metrics, application metrics, custom exporters — agent deployment at scale
- Storage scaling: metrics cardinality explosion, label management, storage requirements per retention period
- High availability: redundant Prometheus instances, Thanos sidecar/query/store architecture
- Dashboard sprawl: governance, ownership, stale dashboards, performance impact of complex queries
- Comparison: CloudWatch Metrics/Azure Monitor/Cloud Monitoring + managed Prometheus/Grafana — what disappears?

**Scope Boundary:** Metrics, monitoring, and alerting ONLY. Do not cover logging (F49), tracing (F51), or application-level observability.

---

### F51: On-Prem Distributed Tracing

**Research Question:**

What is required to self-host distributed tracing infrastructure on-premises, and how does the operational profile compare to managed tracing services?

**Required Sub-Topics:**
- **Jaeger:** Deployment architecture (collector, query, agent), storage backends (Elasticsearch, Cassandra), scaling
- **Tempo (Grafana):** Object storage backend, search capabilities, TraceQL, integration with Grafana
- **OpenTelemetry:** Collector deployment, SDK instrumentation, protocol support, sampling strategies
- Instrumentation burden: adding tracing to every service, context propagation across service boundaries, auto-instrumentation vs manual
- Sampling strategies: head-based vs tail-based sampling, adaptive sampling, sampling at scale
- Storage: trace storage requirements (often very large), retention policies, cost of storing high-cardinality trace data
- Correlation: connecting traces to logs and metrics, exemplars, service dependency mapping
- Comparison: AWS X-Ray/Azure Application Insights/Cloud Trace — what operational burden disappears?

**Scope Boundary:** Distributed tracing ONLY. Do not cover logging (F49), monitoring (F50), or application instrumentation practices.

---

## Wave 7 — Managed K8s Middle Tier (F52–F55, F55a–F55d)

All agents in this wave follow the Standard Agent Instructions above, including full inline citation requirements with direct URLs.

### F52: Managed Kubernetes Platforms (EKS/AKS/GKE)

**Research Question:**

What do managed Kubernetes services (EKS, AKS, GKE) provide out of the box, what operational burden remains even with managed K8s, and where do they fall short compared to fully managed cloud-native services?

**Required Sub-Topics:**
- What's managed: control plane, etcd, API server upgrades, node auto-scaling, managed node groups
- What's NOT managed: application deployment, service mesh, ingress controllers, persistent storage configuration, RBAC policies, network policies
- Operational burden remaining: cluster upgrades (version skew), node pool management, resource quotas, namespace governance
- Add-on ecosystem: what you still need to install and maintain (cert-manager, external-dns, ingress-nginx, Prometheus stack)
- GPU support: GPU node pools, NVIDIA device plugin, GPU scheduling, multi-instance GPU
- Cost structure: control plane costs, node costs, data transfer, compared to serverless alternatives
- Multi-cluster management: fleet management, GitOps (ArgoCD/Flux), cross-cluster networking
- Gaps vs cloud-native: what managed K8s still can't provide that serverless/PaaS does (zero-ops scaling, managed state, built-in observability)
- **Per-service infrastructure on managed K8s (Section 5.1 components):**
  - Health-check endpoints: K8s liveness, readiness, and startup probes per service — configuration patterns, failure handling, integration with ingress controllers and service mesh health checking
  - Service registry: K8s DNS-based service discovery, CoreDNS, headless services, ExternalName services — how services register and discover each other on managed K8s vs cloud-native service discovery (Cloud Map, Dapr)
  - Load balancer and ingress: ingress-nginx, Traefik, AWS/Azure/GCP ingress controllers — per-service routing rules, TLS termination, canary routing via ingress annotations
  - Container image lifecycle: building, tagging, pushing to ECR/ACR/Artifact Registry, image pull policies, imagePullSecrets, admission controllers for image verification

**Scope Boundary:** Managed K8s platform capabilities and gaps ONLY. Do not cover portable K8s (F53), operators (F54), or service mesh details (F55).

---

### F53: Portable Kubernetes for ISV Delivery

**Research Question:**

How do portable Kubernetes platforms (OpenShift, Rancher, Tanzu) enable ISVs to deliver software to diverse customer environments, and what are the practical limits and challenges?

**Required Sub-Topics:**
- **Red Hat OpenShift:** OCP vs OKD, operator framework, subscription model, customer deployment experience
- **Rancher (SUSE):** Multi-cluster management, RKE2, downstream cluster provisioning, customer self-service
- **VMware Tanzu:** Tanzu Kubernetes Grid, integration with vSphere, enterprise customer fit
- **Replicated/KOTS:** Application packaging and delivery platform for K8s-native ISV software
- Customer environment variability: different K8s versions, different CNIs, different storage classes, air-gapped clusters
- Application packaging: Helm charts, Kustomize, operators — trade-offs for ISV distribution
- Update and upgrade logistics: how ISVs push updates to customer-managed clusters, rollback procedures
- Support complexity: debugging issues across diverse customer K8s environments
- Licensing and cost: platform licensing costs passed to customers, impact on ISV pricing model

**Scope Boundary:** Portable K8s for ISV delivery ONLY. Do not cover managed cloud K8s (F52), specific operators (F54), or business impact broadly (Wave 9).

---

### F54: Kubernetes Operators for Stateful Workloads

**Research Question:**

How do Kubernetes operators manage stateful workloads (databases, message queues, AI model serving), how mature are they, and what gaps remain that require manual operations?

**Required Sub-Topics:**
- Operator pattern: custom resource definitions (CRDs), reconciliation loops, operator lifecycle manager (OLM)
- **Database operators:** CloudNativePG, Percona operators, Strimzi (Kafka), Redis operator — maturity, capabilities, limitations
- **AI/ML operators:** KServe, Seldon Core, NVIDIA GPU Operator, Ray Operator — capabilities for model serving and training
- **Monitoring operators:** Prometheus Operator, Grafana Operator — automating observability stack management
- Maturity assessment: which operators are production-ready vs experimental? Operator maturity model
- Gaps: what operations still require manual intervention (major version upgrades, disaster recovery, performance tuning)?
- Operator maintenance: keeping operators updated, CRD version compatibility, operator dependency management
- ISV perspective: should an ISV build custom operators or use existing ones? Build vs buy trade-offs

**Scope Boundary:** K8s operators for stateful workloads ONLY. Do not cover K8s platform management (F52-F53) or service mesh (F55).

---

### F55: Kubernetes Service Mesh & Networking

**Research Question:**

How do Kubernetes service mesh solutions (Istio, Linkerd, Cilium) handle service-to-service communication, and what operational burden do they add or remove?

**Required Sub-Topics:**
- **Istio:** Architecture (Envoy sidecar, istiod), traffic management, security (mTLS), observability, resource overhead
- **Linkerd:** Ultra-lightweight mesh, Rust proxy, simpler operational model, capabilities vs Istio
- **Cilium:** eBPF-based networking, sidecar-less service mesh, network policy enforcement, performance characteristics
- Resource overhead: CPU/memory consumption of sidecar proxies per pod, impact at scale (hundreds/thousands of pods)
- Configuration complexity: VirtualService, DestinationRule, AuthorizationPolicy — configuration surface area
- Troubleshooting: debugging service mesh issues, proxy logs, traffic inspection, common failure modes
- Upgrade challenges: sidecar injection compatibility, control plane upgrades, data plane rolling updates
- When to use vs not use: overhead vs benefit analysis, alternatives (simple mTLS without full mesh)

**Scope Boundary:** K8s service mesh ONLY. Do not cover general networking (F40), API gateways at application level (F3), or K8s platforms (F52).

---

### F55a: Kubernetes Data Services & Stateful Workloads

**Research Question:**

How do Kubernetes-native data services (CloudNativePG, Strimzi Kafka, Redis on K8s) compare to fully managed cloud data services (RDS, MSK, ElastiCache), and what operational gap remains when running stateful workloads on managed K8s?

**Required Sub-Topics:**
- CloudNativePG on EKS/AKS/GKE vs RDS/Azure SQL/Cloud SQL: feature parity, performance, operational burden, backup/restore, HA capabilities
- Strimzi Kafka on K8s vs Amazon MSK/Azure Event Hubs/Confluent Cloud: operational requirements, upgrade procedures, monitoring
- Redis on K8s (Redis Operator) vs ElastiCache/Azure Cache/Memorystore: HA, persistence, scaling differences
- Elasticsearch/OpenSearch on K8s vs managed equivalents: memory management, index lifecycle, cluster scaling
- Storage considerations: persistent volumes, storage classes, CSI drivers, backup strategies for stateful K8s workloads
- Data gravity: why some workloads resist containerization, when to use K8s-native vs managed data services
- Operational gap analysis: what remains harder on K8s even with good operators — quantify with difficulty ratings
- Cost comparison: K8s-native data services (compute + storage + ops) vs managed service pricing

**Scope Boundary:** K8s-native data services vs managed cloud data services ONLY. Do not cover K8s platforms themselves (F52), K8s operators in general (F54), or on-prem data services (F41-F42).

---

### F55b: Kubernetes GPU & AI Workload Management

**Research Question:**

How do GPU scheduling, AI model serving, and ML workloads operate on managed Kubernetes (EKS/AKS/GKE), and what are the requirements, capabilities, and trade-offs compared to cloud-native AI services and on-premises GPU infrastructure?

**Required Sub-Topics:**
- NVIDIA GPU Operator: device plugin, GPU feature discovery, MIG support, driver management on K8s
- GPU scheduling: K8s resource requests/limits for GPUs, multi-instance GPU, time-slicing, topology-aware scheduling
- KServe/Seldon on managed K8s: model serving on K8s vs SageMaker Endpoints/Vertex AI Prediction/Azure ML Endpoints
- Ray on K8s (KubeRay): distributed training and inference, auto-scaling, resource management
- vLLM/TGI on K8s: deploying LLM inference servers as K8s workloads — scaling, GPU allocation, rolling updates
- Node auto-provisioning: Karpenter (EKS), NAP (GKE), KEDA for GPU workloads — scaling GPU nodes on demand
- Cost management: GPU node pools, spot/preemptible GPU instances, cluster autoscaler for GPU nodes
- Gap analysis: what managed K8s GPU workloads still lack compared to cloud-native AI services (auto-optimization, managed endpoints, serverless inference)

**Scope Boundary:** K8s GPU and AI workload management ONLY. Do not cover on-prem GPU hardware (F39), cloud-native AI services (Waves 2-4), or model serving architecture (F5).

---

### F55c: Kubernetes Security Posture

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of securing workloads on managed Kubernetes (RBAC, pod security, network policies, image security), and how does this compare to cloud-native security services and on-prem security operations?

**Required Sub-Topics:**
- RBAC: K8s RBAC design, role/clusterrole management, service accounts, integration with cloud IAM (IRSA, Workload Identity)
- Pod security: Pod Security Admission (PSA), OPA/Gatekeeper, Kyverno — policy enforcement, admission control
- Network policies: Calico, Cilium network policies, microsegmentation, egress control — vs cloud security groups/NSGs
- Image security: admission controllers for signed images, vulnerability scanning (Trivy Operator), image provenance
- Secrets management: K8s Secrets, External Secrets Operator, CSI Secrets Store Driver — integration with Vault, cloud KMS
- Runtime security: Falco on K8s, Sysdig, runtime threat detection — deployment and management on managed K8s
- Supply chain security: SBOM generation, Sigstore/cosign, policy-as-code for supply chain
- Gap analysis: what cloud-native security services (GuardDuty, Defender, SCC) provide that K8s-native security tooling does not

**Scope Boundary:** K8s security posture ONLY. Do not cover general on-prem security (F46-F47, F71), cloud-native security services (F11, F19, F27), or K8s platform management (F52).

---

### F55d: Kubernetes Observability Stack

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of running the Kubernetes observability stack (Prometheus Operator, Grafana, Loki, Tempo) on managed K8s, and how does this compare to cloud-native observability services?

**Required Sub-Topics:**
- Prometheus Operator on managed K8s: deployment, ServiceMonitor/PodMonitor CRDs, Thanos/Mimir for HA and long-term storage
- Grafana on K8s: dashboard management, datasource provisioning, alerting, Grafana Operator
- Loki on K8s: log aggregation, storage backend (object store), retention, label strategies vs CloudWatch Logs/Azure Monitor/Cloud Logging
- Tempo on K8s: distributed tracing, storage, TraceQL vs X-Ray/Application Insights/Cloud Trace
- OpenTelemetry on K8s: Collector deployment (DaemonSet vs Sidecar), auto-instrumentation, resource consumption
- Managed Prometheus/Grafana: cloud-managed alternatives (Amazon Managed Prometheus, Azure Managed Grafana, GCP Managed Prometheus) — what they simplify
- Resource overhead: CPU/memory consumption of observability stack on K8s — monitoring the monitors
- Gap analysis: what cloud-native observability provides that K8s-native stacks do not (managed retention, auto-scaling ingestion, ML anomaly detection)

**Scope Boundary:** K8s observability stack ONLY. Do not cover on-prem observability (F49-F51), cloud-native observability services (F12, F20, F28), or K8s platform management (F52).

---

## Wave 8 — SDLC Phase Cross-Cutting Analysis (F56–F60)

All agents in this wave follow the Standard Agent Instructions above, including full inline citation requirements with direct URLs.

### F56: Design & Architecture Phase Constraints

**Research Question:**

How does the target deployment model (on-prem vs managed K8s vs cloud-native) constrain or alter software architecture decisions during the design phase, specifically for AI-enabled applications?

**Required Sub-Topics:**
- Portable vs cloud-optimized architecture: design trade-offs when you must support on-prem (no vendor-specific services, abstraction layers, increased code complexity)
- Lowest-common-denominator problem: when designing for on-prem, you can't assume any managed service exists — how this inflates architecture
- Database selection: choosing DBs that work everywhere vs cloud-native optimized options
- AI architecture decisions: self-hosted inference vs API calls, embedding pipeline design, vector DB selection based on deployment target
- Abstraction cost: building provider-agnostic abstractions (Terraform, Crossplane, custom adapters) — engineering effort and maintenance
- Twelve-factor app constraints: which factors are easy/hard to achieve on-prem vs cloud
- Architecture review: how on-prem requirements add review gates and compliance checks to the design phase
- Real-world examples: cite specific ISVs that have navigated this (Confluent, Elastic, GitLab, Databricks)

**Scope Boundary:** Architecture design decisions ONLY. Do not cover build/test (F57), deploy (F58), or operations (F59).

---

### F57: Build & Test Phase Differences

**Research Question:**

How does the build and test experience differ when developing for on-prem deployment vs cloud-native, and what additional infrastructure and process is required?

**Required Sub-Topics:**
- Dev environment parity: replicating on-prem customer environments locally — VM sprawl, GPU access, license limitations
- CI/CD for multi-target: building artifacts that work on-prem and cloud — multi-arch builds, air-gapped dependencies, image size
- Integration testing: testing against self-hosted services (Kafka, PostgreSQL, Redis) vs managed service APIs — test environment complexity
- GPU testing: accessing GPU hardware for AI model testing — on-prem GPU lab vs cloud GPU instances
- Compliance testing: validating against customer security requirements, penetration testing, vulnerability scanning
- Test matrix explosion: testing across customer OS versions, K8s versions, hardware configurations, network configurations
- Performance testing: simulating customer hardware limitations, memory constraints, network latency
- Test infrastructure cost: maintaining dedicated test environments that mirror on-prem vs cloud-native test environments

**Scope Boundary:** Build and test phase ONLY. Do not cover architecture design (F56), deployment (F58), or CI/CD infrastructure (F48).

---

### F58: Deploy & Release Phase Differences

**Research Question:**

How do deployment and release strategies differ across on-prem, managed K8s, and cloud-native models, especially for ISVs shipping to customer environments?

**Required Sub-Topics:**
- Deployment strategies: blue/green, canary, rolling — what's possible in each deployment model
- Air-gapped deployments: packaging all dependencies, offline installers, image pre-loading, dependency vendoring
- Customer-site deployment: remote deployment tooling, customer access constraints, change management processes
- Release engineering: building release artifacts (Helm charts, operators, installers), release notes, compatibility matrices
- Rollback procedures: rollback complexity in each model — cloud (instant) vs K8s (Helm rollback) vs on-prem (manual)
- Configuration management: per-customer configuration, environment-specific values, secrets injection
- Multi-version support: maintaining deployment tooling for multiple active versions simultaneously
- Deployment frequency: how deployment model affects release cadence — cloud (continuous) vs on-prem (quarterly/annual)

**Scope Boundary:** Deployment and release ONLY. Do not cover build (F57), operations (F59), or version management business impact (F62).

---

### F59: Operate & Monitor Phase Differences

**Research Question:**

How do day-2 operations differ across on-prem, managed K8s, and cloud-native deployments in terms of requirements, characteristics, and trade-offs for each model?

**Required Sub-Topics:**
- Incident response: remote debugging customer on-prem issues vs cloud-native centralized operations
- Scaling operations: auto-scaling in cloud vs manual capacity planning on-prem — response time to demand spikes
- Failover and disaster recovery: automated cloud failover vs manual on-prem DR procedures
- SLA management: delivering SLAs when you don't control the customer's infrastructure
- Monitoring access: observing application health on customer-managed infrastructure — access limitations, data exfiltration concerns
- Patch management: coordinating security patches across deployed customer instances vs single cloud deployment
- Performance optimization: tuning application performance on variable customer hardware
- On-call burden: staff requirements for supporting on-prem deployments across customer time zones

**Scope Boundary:** Day-2 operations CROSS-CUTTING SYNTHESIS ONLY. This agent should synthesize patterns across Wave 5/6 findings into cross-cutting operational themes (incident response, scaling, SLA management), NOT re-research individual infrastructure domains already covered in F39-F51. Do not cover initial deployment (F58), upgrades (F60), or business staffing impact (F63).

---

### F60: Update, Patch & Scale Phase Differences

**Research Question:**

How do software updates, security patching, and scaling operations differ across deployment models in terms of requirements, processes, and trade-offs for each model?

**Required Sub-Topics:**
- Update delivery: OTA updates vs customer-coordinated maintenance windows vs cloud continuous deployment
- Breaking changes: managing API and schema migrations when you can't control the upgrade timing
- Security patching urgency: CVE response timelines — cloud (hours) vs on-prem (weeks/months of customer coordination)
- Database migrations: schema changes across deployed instances at different versions — migration tooling and compatibility
- Dependency updates: OS, runtime, library updates — testing matrix across customer environments
- Scaling: adding capacity in cloud (API call) vs on-prem (hardware procurement + installation)
- Deprecation and EOL: sunsetting old versions when customers are slow to upgrade
- Compliance: maintaining compliance certifications (SOC2, HIPAA, FedRAMP) across all deployed versions

**Scope Boundary:** Updates, patches, and scaling ONLY. Do not cover initial deployment (F58), day-2 ops (F59), or business impact (Wave 9).

---

## Wave 9 — ISV Business Impact (F61–F66)

All agents in this wave follow the Standard Agent Instructions above, including full inline citation requirements with direct URLs.

### F61: Support Burden & Customer Environment Variability

**Research Question:**

How does the ISV support model differ between on-premises deployments (with customer environment variability) and cloud-native SaaS delivery, in terms of costs, ticket profiles, team requirements, and trade-offs?

**Required Sub-Topics:**
- Environment matrix: diversity of OS versions, hardware configurations, network topologies, security policies across customer base
- "Works on my machine" at enterprise scale: reproducing customer-specific issues, environment simulation
- Support ticket categories: what percentage of on-prem support tickets are environment-specific vs application bugs? (cite industry data)
- Remote access challenges: VPN access to customer environments, restricted networks, approval processes for troubleshooting
- Documentation burden: installation guides, compatibility matrices, troubleshooting guides per environment configuration
- Escalation complexity: engaging customer IT teams, change management processes, maintenance window coordination
- Support staffing: headcount ratios for on-prem vs SaaS support teams (cite industry benchmarks)
- Customer satisfaction impact: resolution time differences between on-prem and SaaS support models

**Scope Boundary:** Support burden and environment variability ONLY. Do not cover technical operations (Wave 5/6), version management (F62), or staffing beyond support roles (F63).

---

### F62: Upgrade & Multi-Version Management

**Research Question:**

How do ISVs manage multi-version support, coordinated upgrades, and backward compatibility when delivering on-premises software, and what operational overhead does this create?

**Required Sub-Topics:**
- Version proliferation: how many concurrent versions must an ISV support for on-prem customers? (cite real examples — Oracle, SAP, VMware)
- Backward compatibility burden: maintaining API compatibility, data format compatibility, configuration compatibility across versions
- Upgrade path complexity: skip-version upgrades, data migration scripts, pre-upgrade validators, rollback procedures
- Customer upgrade resistance: why customers delay upgrades, regulatory change freezes, risk aversion
- Testing overhead: QA matrix for N supported versions × M supported environments
- Deprecation politics: sunsetting old versions when enterprise customers are contractually entitled to support
- Feature gating: shipping features that only work in newer environments, conditional capabilities
- Comparison: SaaS single-version model — one codebase, one deployment, continuous delivery

**Scope Boundary:** Version management and upgrades ONLY. Do not cover deployment mechanics (F58), support burden (F61), or licensing (F65).

---

### F63: Staffing & Expertise Requirements

**Research Question:**

What specialized technical skills does an ISV need to build and deliver on-premises AI-enabled software compared to cloud-native, and what are the talent market realities?

**Required Sub-Topics:**
- Role inventory: what roles are needed for on-prem delivery that cloud-native doesn't require (infrastructure engineers, release engineers, customer deployment specialists, hardware specialists)?
- Skill depth: DBA expertise, networking expertise, GPU infrastructure expertise, K8s operations expertise — depth required for on-prem
- Market scarcity: salary benchmarks and availability for specialized roles (GPU infrastructure engineers, K8s platform engineers, security engineers)
- Team size: minimum viable team for on-prem ISV delivery vs cloud-native ISV delivery (cite benchmarks or real examples)
- Training investment: ongoing training required to keep up with on-prem technology stack vs cloud certifications
- Outsourcing options: managed services providers, consulting partners — availability and cost for on-prem delivery support
- Talent retention: difficulty retaining infrastructure talent that prefers cloud-native work
- Geographic considerations: needing staff in customer time zones for on-prem support vs centralized cloud operations

**Scope Boundary:** Staffing and expertise ONLY. Do not cover support operations (F61), business economics (F64-F66), or technical details of the infrastructure.

---

### F64: Time-to-Market & Competitive Dynamics

**Research Question:**

How does the choice of deployment model (on-prem vs managed K8s vs cloud-native) affect an ISV's feature development velocity, time-to-market, and competitive positioning in the AI application market, and what are the trade-offs of each model?

**Required Sub-Topics:**
- Feature velocity: engineering time spent on infrastructure compatibility vs feature development — cite industry benchmarks or surveys
- Engineering allocation: how engineering effort is distributed between infrastructure work (packaging, testing, support) and product innovation in each deployment model
- Competitive response time: how quickly can an ISV ship a new AI capability (new model support, new integration) in each model?
- Market timing: AI market moves fast — risk of missing market windows due to on-prem delivery complexity
- Customer acquisition: how deployment model affects sales cycle length, POC complexity, deal size
- Developer experience: impact on developer productivity and satisfaction when building for on-prem targets
- Open source competition: on-prem OSS alternatives vs proprietary SaaS — competitive dynamics
- On-prem competitive advantages: market segments where on-prem delivery is a competitive differentiator (regulated industries, sovereign cloud, data-sensitive customers)
- Case studies: ISVs across the spectrum — those that shifted from on-prem to cloud-native, those that maintain hybrid delivery, and those that lead with on-prem (cite specific companies)

**Scope Boundary:** Time-to-market and competitive dynamics ONLY. Do not cover staffing (F63), pricing (F65), or technical architecture decisions (F56).

---

### F65: Licensing & Pricing Model Complexity

**Research Question:**

How do software licensing models, pricing structures, and commercial terms differ for on-premises vs SaaS AI application delivery, and what complexity does on-prem licensing introduce?

**Required Sub-Topics:**
- License models: perpetual vs subscription vs consumption-based — what works for on-prem vs cloud
- Metering challenges: tracking usage on customer-controlled infrastructure, phone-home mechanisms, air-gapped metering
- GPU/compute licensing: how AI workload licensing works when the ISV doesn't control the hardware (per-GPU, per-core, per-node pricing)
- Third-party licensing: passing through GPU driver licenses (NVIDIA GRID), database licenses, OS licenses — complexity and cost
- Revenue recognition: perpetual license vs SaaS subscription revenue — accounting and investor implications
- Contract complexity: SLAs, support tiers, upgrade entitlements, custom terms per customer
- Price competition: on-prem pricing vs cloud consumption pricing — customer cost comparison and negotiation dynamics
- Margin impact: on-prem delivery costs (support, engineering, infrastructure) eating into margins vs SaaS margin structure

**Scope Boundary:** Licensing and pricing ONLY. Do not cover support operations (F61), staffing costs (F63), or competitive dynamics beyond pricing (F64).

---

### F66: Multi-Tenancy & SaaS Operational Leverage

**Research Question:**

How do multi-tenancy models differ across cloud-native (shared infrastructure), managed K8s (namespace isolation), and on-premises (per-customer deployment), and what are the operational and economic trade-offs of each for ISV unit economics?

**Required Sub-Topics:**
- Multi-tenancy architectures: shared infrastructure, shared application/isolated data, fully isolated — trade-offs and cloud enablers
- Operational leverage: one deployment serving N customers vs N separate on-prem deployments — staffing, infrastructure, maintenance ratios
- Infrastructure efficiency: resource sharing, bin-packing, auto-scaling across tenants — utilization rates vs dedicated on-prem hardware
- Data advantages: centralized data for ML training, cross-tenant analytics (anonymized), faster model improvement
- Observability advantages: single pane of glass for all customers vs per-customer monitoring
- Upgrade simplicity: one codebase, one deployment, all customers on latest version simultaneously
- Unit economics: cost-per-customer trend line for SaaS vs on-prem — cite industry benchmarks (Bessemer, OpenView)
- Noisy neighbor mitigation: rate limiting, resource quotas, tenant isolation in shared infrastructure — cloud-native tools
- On-prem isolation advantages: complete data isolation, dedicated resources, customer control — scenarios where per-customer deployment is preferred or required

**Scope Boundary:** Multi-tenancy and SaaS leverage ONLY. Do not cover specific cloud services (Waves 2-4), pricing models (F65), or technical architecture patterns (F1).

---

## Wave 10 — Cross-Cutting Gap Coverage (F67–F71)

These agents address critical domains that cut across multiple waves and were identified as gaps in the initial plan review. All agents follow Standard Agent Instructions including full inline citation requirements with direct URLs.

---

### F67: Compliance & Regulatory Requirements Across Deployment Models

**Research Question:**

What are the compliance and regulatory requirements (GDPR, HIPAA, FedRAMP, EU AI Act, SOC 2, ISO 27001) for AI-enabled applications across on-premises, managed K8s, and cloud-native deployment models, and how does each model affect compliance posture?

**Required Sub-Topics:**
- Regulatory landscape: GDPR data residency, HIPAA BAAs, FedRAMP authorization levels, EU AI Act risk classifications, SOC 2 Type II controls
- Cloud compliance inheritance: what compliance certifications are inherited from cloud providers vs what the ISV must achieve independently
- On-premises compliance: full compliance responsibility — audit trail, access controls, encryption, data handling — all self-managed
- Managed K8s compliance: shared responsibility model — what the platform covers vs what the ISV owns
- Data sovereignty: requirements for data to remain in specific jurisdictions — how each deployment model addresses this
- Audit readiness: maintaining audit logs, evidence collection, continuous monitoring — infrastructure requirements per model
- Compliance automation: tools for continuous compliance (Cloud Custodian, OPA/Gatekeeper, cloud-native compliance services) — availability per model
- Cost of compliance: FTE, tooling, and certification costs across deployment models — cite industry benchmarks

**Scope Boundary:** Compliance and regulatory frameworks ONLY. Do not cover security implementation details (F46-F47), general IAM (F46), or business licensing (F65).

---

### F68: AI Safety, Guardrails & Content Moderation On-Premises

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of implementing AI safety guardrails, content moderation, and responsible AI practices in a 100% on-premises environment, and how does this compare to cloud-native AI safety services?

**Required Sub-Topics:**
- Guardrail frameworks: Llama Guard, NeMo Guardrails, Guardrails AI, custom rule engines — deployment requirements and capabilities
- Content filtering: input/output content filtering, PII detection, toxicity detection — self-hosted models and infrastructure
- Prompt injection defense: prompt injection detection, input sanitization, output validation — on-prem implementation requirements
- Responsible AI tooling: bias detection, fairness metrics, model cards, explanation tools — self-hosted vs cloud-native (Azure AI Content Safety, Bedrock Guardrails)
- Red teaming infrastructure: adversarial testing, automated red teaming pipelines — what's needed on-prem
- Monitoring and audit: tracking guardrail triggers, false positives, model behavior drift — observability requirements
- Regulatory alignment: mapping guardrails to EU AI Act requirements, industry-specific AI governance
- Comparison: AWS Bedrock Guardrails, Azure AI Content Safety, Google Vertex AI safety — what operational burden disappears with managed safety services

**Scope Boundary:** AI safety and guardrails ONLY. Do not cover general security (F46-F47), model serving (F36), or compliance frameworks broadly (F67).

---

### F69: Model Training, Fine-Tuning & Experiment Tracking On-Premises

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of conducting model training, fine-tuning (LoRA, QLoRA, full fine-tuning), and experiment tracking in a 100% on-premises environment, and how does this compare to cloud-native ML platforms?

**Required Sub-Topics:**
- Fine-tuning approaches: LoRA, QLoRA, full fine-tuning, RLHF/DPO — compute requirements, GPU memory needs, training duration per approach
- Training infrastructure: multi-GPU training (DeepSpeed, FSDP), distributed training across nodes — networking (NCCL, InfiniBand) and storage requirements
- Experiment tracking: MLflow, Weights & Biases (self-hosted), ClearML — deployment, storage, collaboration features
- Data pipeline for training: data labeling, preprocessing, validation — infrastructure requirements (Argilla, Label Studio)
- Model registry: versioning trained models, promoting to production, rollback — self-hosted solutions
- Hyperparameter optimization: Optuna, Ray Tune — compute scheduling and resource management
- Cost and time: training cost per model size, GPU-hours, comparison to cloud fine-tuning services (SageMaker, Vertex AI, Azure ML)
- Comparison: SageMaker Training, Vertex AI Training, Azure ML — what infrastructure and operational burden disappears with managed training

**Scope Boundary:** Model training and fine-tuning ONLY. Do not cover model inference/serving (F36), RAG pipelines (F35), or GPU hardware procurement (F39).

---

### F70: Disaster Recovery & Business Continuity Across Deployment Models

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of implementing disaster recovery (DR) and business continuity (BC) for AI-enabled applications across on-premises, managed K8s, and cloud-native deployment models?

**Required Sub-Topics:**
- DR fundamentals: RPO/RTO targets, disaster classification, recovery strategies (active-active, active-passive, pilot light, backup-restore)
- Cloud-native DR: multi-region deployment, automated failover, cross-region replication — what cloud providers offer natively
- On-premises DR: multi-site replication, backup infrastructure, manual failover procedures — hardware, networking, storage requirements
- Managed K8s DR: cluster-level DR (Velero, Kasten), etcd backup, cross-cluster failover
- Data tier DR: database replication, object storage replication, vector DB backup/restore — requirements per deployment model
- AI-specific DR: model artifact backup, training data backup, embedding index recovery, GPU failover
- Testing: DR drill procedures, automation, RTO validation — complexity per deployment model
- Cost: DR infrastructure cost (standby hardware, reserved capacity, cross-region replication) — comparison across models

**Scope Boundary:** Disaster recovery and business continuity ONLY. Do not cover individual infrastructure component operations (Waves 5-6), security incidents (F67), or day-to-day monitoring (F59).

---

### F71: On-Premises Security Operations (SOC)

**Research Question:**

What are the requirements, operational characteristics, and trade-offs of running security operations (SIEM, IDS/IPS, vulnerability scanning, incident response, runtime security) in a 100% on-premises environment, and how does this compare to cloud-native security operations services?

**Required Sub-Topics:**
- SIEM: self-hosted SIEM (Wazuh, ELK-based, Splunk) — deployment, tuning, log correlation, storage requirements, alert management
- IDS/IPS: network-based (Suricata, Snort) and host-based intrusion detection — deployment, rule management, false positive tuning
- Vulnerability scanning: infrastructure scanning (Nessus, OpenVAS), container scanning (Trivy, Grype), dependency scanning — scheduling, remediation workflows
- Runtime security: container runtime protection (Falco, Sysdig), process monitoring, file integrity monitoring
- Incident response: playbooks, forensics infrastructure, evidence collection, chain of custody — on-prem requirements
- Threat intelligence: threat feed integration, IOC management, hunting queries — self-managed infrastructure
- Penetration testing: internal red team infrastructure, testing environments, tools
- Comparison: AWS GuardDuty + Security Hub + Inspector, Azure Sentinel + Defender, GCP SCC — what operational burden disappears with managed security operations

**Scope Boundary:** Security operations (detection, response, monitoring) ONLY. Do not cover IAM/authentication (F46), encryption/secrets (F47), or compliance frameworks (F67).

---

## Synthesis Phase

### Layer 1: Wave-Level Summaries (W1S–W10S)

After each wave completes, produce a summary file that distills key findings from that wave's agents. Each wave summary should:

- Be 800-1200 words
- Synthesize findings across the wave's agents into unified themes
- Highlight key difficulty ratings, FTE estimates, and trade-offs discovered
- Identify cross-agent patterns and contradictions within the wave
- List any open questions or unresolved conflicts for downstream synthesis
- Reference specific agent files for detailed evidence
- **CITATION REQUIREMENT:** Every claim, statistic, difficulty rating, and FTE estimate in a summary MUST include an inline citation tracing it back to the specific agent file AND the original source URL. Use the format: [claim](original-URL) (from F##). If a summary aggregates across agents, cite each contributing agent and their original sources. Include a "Sources" section at the end listing all referenced URLs.

| Summary | Input Agents | Focus |
|---------|--------------|-------|
| W1S | F1–F7 | Foundation architecture patterns and infrastructure requirements |
| W2S | F8–F15 | AWS managed services capabilities and operational elimination |
| W3S | F16–F23 | Azure managed services capabilities and operational elimination |
| W4S | F24–F31 | GCP managed services capabilities and operational elimination |
| W5S | F32–F38 | On-prem application-level operational patterns and trade-offs |
| W6S | F39–F51 | On-prem infrastructure domain operational profiles |
| W7S | F52–F55d | Managed K8s capabilities, gaps, and middle-tier positioning |
| W8S | F56–F60 | SDLC phase differences across deployment models |
| W9S | F61–F66 | ISV business impact across deployment models |
| W10S | F67–F71 | Cross-cutting gaps (compliance, AI safety, training, DR, security ops) |

### Layer 2: Cross-Domain Integration Files (X1–X3)

After all wave summaries are complete, produce three cross-domain integration files that bridge multiple waves.

**CITATION REQUIREMENT FOR ALL LAYER 2 FILES:** Every claim, comparison, rating, and estimate MUST include inline citations tracing back to the original source URLs from the underlying agent files. Use the format: [claim](original-URL) (from F##, F##). When synthesizing across waves, preserve the full citation chain — do not summarize away the URLs. Each integration file MUST include a "Sources" section at the end listing all referenced URLs organized by wave.

**X1: Cloud Managed Services Comparison** (consumes W2S, W3S, W4S)
- Side-by-side comparison of AWS, Azure, GCP across all 8 capability domains
- Identify where providers diverge in capability, maturity, or pricing
- Produce a provider-neutral "cloud-native capabilities profile" for use by S1
- All service capabilities and pricing claims must cite official vendor documentation URLs

**X2: On-Premises Operational Synthesis** (consumes W5S, W6S, W10S)
- Aggregate on-prem difficulty ratings across all domains
- Identify the top-10 hardest operational domains with evidence
- Map FTE requirements by domain and produce an aggregate staffing model
- Synthesize compliance, DR, and security ops findings from Wave 10
- Every difficulty rating and FTE estimate must trace back to the original cited source

**X3: Three-Tier Comparison Draft** (consumes W7S, W8S, W9S, X1, X2)
- Draft the three-tier comparison (on-prem → managed K8s → cloud-native)
- Identify where managed K8s closes the gap with cloud-native vs where it doesn't
- Map SDLC and business impact findings to the three tiers
- Produce a conflicts register listing any contradictions across waves with citations for both sides

### S1: Comparison Matrix

After Layer 2 integration files are complete (consuming X1, X2, X3 rather than raw wave files), synthesize a side-by-side comparison matrix:

- **Rows:** Every capability domain identified across waves (compute, networking, databases, AI/ML, security, observability, CI/CD, etc.)
- **Columns:** On-Prem | Managed K8s | Cloud-Native
- **Cell content:** Difficulty rating (1-5), key challenges, representative tools/services, estimated operational FTE burden
- **Annotations:** SDLC phase where each challenge manifests most acutely
- **Summary rows:** Total estimated operational headcount, time-to-market impact, relative cost

**CITATION REQUIREMENT:** Every cell in the comparison matrix must be traceable. Each difficulty rating, FTE estimate, and tool/service claim must include an inline citation to the original source URL, referenced via the agent file that produced it (e.g., "4/5 — [self-hosted Kafka requires 0.5-1.0 FTE](URL) (F44)"). Include a "Sources" section at the end of the matrix file listing all referenced URLs.

### S2: Structured Research Document

Final narrative document synthesizing all findings (consuming S1, X1-X3, and wave summaries W1S-W10S; referencing raw agent files only for citation-level detail):

1. **Executive Summary** (1 page): Key findings, strategic implications, recommended positioning
2. **How Modern AI-SaaS Development Works** (synthesize Wave 1)
3. **The On-Premises Challenge: A Categorical Analysis** (synthesize Waves 5-6, 10)
4. **The Managed K8s Middle Ground** (synthesize Wave 7)
5. **SDLC Impact Analysis** (synthesize Wave 8)
6. **ISV Business Impact** (synthesize Wave 9)
7. **Three-Tier Comparison** (incorporate S1 matrix)
8. **Conclusions and Strategic Implications**

**CITATION REQUIREMENT:** The final research document must maintain full citation traceability. Every factual claim, statistic, comparison, difficulty rating, and FTE estimate in the narrative MUST include an inline citation with the original source URL in the format: [description](URL). Do NOT strip citations during synthesis — they are the evidentiary foundation of the document. Each section must end with a "Section Sources" listing, and the document must end with a consolidated "All Sources" appendix organized by wave/domain. Any claim that cannot be traced to a cited source must be marked [UNVERIFIED].

---

## Quality Gates

Quality gates are checkpoints between execution phases that ensure research quality before proceeding to the next phase.

### G1: Per-Wave File Completeness (after each wave completes)

Before marking a wave complete, verify for each agent output file:
- [ ] File exists at the expected path
- [ ] Word count is within target range (1500-2500 words)
- [ ] All required sections are present: Executive Summary, sub-topic sections, Key Takeaways, Sources
- [ ] Minimum 10 inline citations with URLs
- [ ] Comparison table is present (if applicable to the agent's scope)
- [ ] Difficulty ratings are included using the 1-5 scale from Standard Agent Instructions
- [ ] "Related — Out of Scope" section exists (even if empty)

**Action if gate fails:** Return file to agent for revision with specific deficiency notes.

### G2: Per-Agent Citation & Source Quality (during wave execution)

For each agent output, validate:
- [ ] All inline citations include working URLs (not just descriptive text)
- [ ] At least 60% of citations are Tier 1 or Tier 2 sources (per Standard Agent Instructions)
- [ ] No more than 3 claims marked [UNVERIFIED] per file
- [ ] ALL sources are from 2025 or later; any pre-2025 fallback is marked [PRE-2025: YYYY] with justification
- [ ] No citations to paywalled content without noting the paywall

**Action if gate fails:** Agent must find replacement citations or explicitly justify [UNVERIFIED] claims.

### G3: Cross-Reference Consistency (after all primary waves complete, before Layer 1 summaries)

After Waves 1-10 are all complete, check:
- [ ] Cross-references between agents use correct format: "See [F##: Title]"
- [ ] No agent re-researches topics explicitly assigned to another agent
- [ ] Difficulty ratings for the same domain are consistent across agents (±1 point)
- [ ] FTE estimates for overlapping domains are consistent or discrepancies are explained
- [ ] Terminology matches the glossary in Standard Agent Instructions

**Action if gate fails:** Identify specific inconsistencies and route to the responsible agent for correction before proceeding to synthesis.

### G4: Pre-Synthesis Coverage Checklist (before Layer 2 integration files)

Before starting X1-X3 integration files:
- [ ] All 10 wave summaries (W1S-W10S) are complete and pass G1 criteria
- [ ] Every wave summary contains inline citations with original source URLs (not just agent file references)
- [ ] Every wave summary includes a "Sources" section listing all referenced URLs
- [ ] Coverage check: every capability domain in the Comparison Table Template has at least one agent covering it
- [ ] Conflicts register: all contradictions between agents are documented with both positions and citations
- [ ] No critical [UNVERIFIED] claims remain in areas that feed directly into the comparison matrix

**Action if gate fails:** Identify coverage gaps, missing citations, or unresolved conflicts and assign corrective work before synthesis begins.

### G5: Pre-Final Synthesis Readiness (before S1 and S2)

Before starting the final Comparison Matrix (S1) and Structured Research Document (S2):
- [ ] All Layer 2 files (X1, X2, X3) are complete
- [ ] Every Layer 2 file contains inline citations with original source URLs preserved from agent files
- [ ] Every Layer 2 file includes a "Sources" section organized by wave listing all referenced URLs
- [ ] Conflicts register from G4 is resolved (all contradictions have a resolution or are flagged as "unresolved — present both")
- [ ] Difficulty ratings have been normalized across waves (same 1-5 scale, consistent anchor examples)
- [ ] FTE estimates have been aggregated and sanity-checked (total should be plausible for a mid-size ISV)
- [ ] All three deployment models (on-prem, managed K8s, cloud-native) have balanced coverage (no model under-researched)
- [ ] Citation chain integrity: spot-check 10 claims across X1-X3 to verify URLs trace back to original sources

**Action if gate fails:** Return to Layer 2 agents with specific gaps or broken citation chains to address before final synthesis.

---

## Output Structure

```
research/build/isv_development/
├── wave1/
│   ├── F01_microservices_architecture.md
│   ├── F02_event_driven_architecture.md
│   ├── F03_api_gateways_service_comm.md
│   ├── F04_rag_pipelines.md
│   ├── F05_llm_model_serving.md
│   ├── F06_vector_dbs_embeddings.md
│   └── F07_ai_agent_frameworks.md
├── wave2/
│   ├── F08_aws_compute.md
│   ├── F09_aws_data.md
│   ├── F10_aws_ai_ml.md
│   ├── F11_aws_security.md
│   ├── F12_aws_observability.md
│   ├── F13_aws_networking.md
│   ├── F14_aws_cicd.md
│   └── F15_aws_messaging.md
├── wave3/
│   ├── F16_azure_compute.md
│   ├── F17_azure_data.md
│   ├── F18_azure_ai_ml.md
│   ├── F19_azure_security.md
│   ├── F20_azure_observability.md
│   ├── F21_azure_networking.md
│   ├── F22_azure_cicd.md
│   └── F23_azure_messaging.md
├── wave4/
│   ├── F24_gcp_compute.md
│   ├── F25_gcp_data.md
│   ├── F26_gcp_ai_ml.md
│   ├── F27_gcp_security.md
│   ├── F28_gcp_observability.md
│   ├── F29_gcp_networking.md
│   ├── F30_gcp_cicd.md
│   └── F31_gcp_messaging.md
├── wave5/
│   ├── F32_onprem_microservices_lifecycle.md
│   ├── F33_onprem_event_driven.md
│   ├── F34_onprem_api_gateway.md
│   ├── F35_onprem_rag_pipeline.md
│   ├── F36_onprem_llm_inference.md
│   ├── F37_onprem_embedding_pipeline.md
│   └── F38_onprem_ai_agent_infra.md
├── wave6/
│   ├── F39_onprem_compute.md
│   ├── F40_onprem_networking.md
│   ├── F41_onprem_relational_dbs.md
│   ├── F42_onprem_nosql_caching.md
│   ├── F43_onprem_object_storage.md
│   ├── F44_onprem_message_queues.md
│   ├── F45_onprem_vector_dbs_ai_data.md
│   ├── F46_onprem_iam_identity.md
│   ├── F47_onprem_secrets_certs.md
│   ├── F48_onprem_cicd.md
│   ├── F49_onprem_logging.md
│   ├── F50_onprem_monitoring.md
│   └── F51_onprem_tracing.md
├── wave7/
│   ├── F52_managed_k8s_platforms.md
│   ├── F53_portable_k8s_isv.md
│   ├── F54_k8s_operators_stateful.md
│   ├── F55_k8s_service_mesh.md
│   ├── F55a_k8s_data_services.md
│   ├── F55b_k8s_gpu_ai_workloads.md
│   ├── F55c_k8s_security_posture.md
│   └── F55d_k8s_observability_stack.md
├── wave8/
│   ├── F56_sdlc_design_architecture.md
│   ├── F57_sdlc_build_test.md
│   ├── F58_sdlc_deploy_release.md
│   ├── F59_sdlc_operate_monitor.md
│   └── F60_sdlc_update_patch_scale.md
├── wave9/
│   ├── F61_isv_support_burden.md
│   ├── F62_isv_upgrade_versioning.md
│   ├── F63_isv_staffing_expertise.md
│   ├── F64_isv_time_to_market.md
│   ├── F65_isv_licensing_pricing.md
│   └── F66_isv_multi_tenancy.md
├── wave10/
│   ├── F67_compliance_regulatory.md
│   ├── F68_ai_safety_guardrails.md
│   ├── F69_model_training_finetuning.md
│   ├── F70_disaster_recovery_bc.md
│   └── F71_security_operations.md
├── summaries/
│   ├── W01S_foundation_patterns.md
│   ├── W02S_aws_services.md
│   ├── W03S_azure_services.md
│   ├── W04S_gcp_services.md
│   ├── W05S_onprem_app_patterns.md
│   ├── W06S_onprem_infrastructure.md
│   ├── W07S_managed_k8s.md
│   ├── W08S_sdlc_phases.md
│   ├── W09S_isv_business_impact.md
│   └── W10S_crosscutting_gaps.md
├── integration/
│   ├── X1_cloud_services_comparison.md
│   ├── X2_onprem_operational_synthesis.md
│   └── X3_three_tier_comparison_draft.md
└── synthesis/
    ├── comparison_matrix.md
    └── structured_research_document.md
```
