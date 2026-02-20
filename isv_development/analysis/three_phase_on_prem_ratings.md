# Three-Phase On-Premises Subsegment Ratings

## ISV SaaS Deployment: Relative Difficulty and Total Effort by Phase

**Date:** 2026-02-19
**Input Files:** P1_control_plane.md, P2_application_logic.md, P3_data_plane.md, P4_ai_model_plane.md, G1_n_services_multiplier.md, S1_four_plane_synthesis.md
**Scope:** All 38 MECE subsegments across 4 planes, rated for 3 deployment phases

---

## 1. Scope and Responsibility Split

| Domain | Owner | Examples |
|---|---|---|
| **Hardware environment** | Customer | Servers, GPUs, networking equipment, storage arrays, power, cooling, rack space, physical security |
| **GPU + AI models** | Customer | GPU procurement, driver management, inference engine operation, model weights, CUDA stack |
| **All software** | ISV | Kubernetes, databases, message brokers, observability, security tooling, application code, CI/CD |
| **Software-to-hardware adaptation** | ISV | Customizing software deployment to each customer's specific hardware environment |

**Implication for P4:** Subsegments S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) shift to customer responsibility. ISV retains S1 (API Integration), S6 (Routing), S7 (Monitoring), and S8 (Lifecycle) in reduced form — calling customer-provided inference endpoints rather than managing infrastructure.

---

## 2. Three Deployment Phases

| Phase | Cost Structure | Scales With |
|---|---|---|
| **Phase 1: Initial Refactoring** | One-time engineering investment to make cloud-native SaaS portable to open K8s | Fixed (amortized across customers) |
| **Phase 2: Per-Customer Customization** | Adapting software to each customer's hardware environment | N customers (linear) |
| **Phase 3: Ongoing Updates & Support** | Recurring maintenance, upgrades, patching, incident response | N customers × update frequency |

---

## 3. Rating Scales

**Relative Difficulty (RD):** How much harder is this task compared to the cloud-native equivalent?

| Rating | Label | Meaning |
|:---:|---|---|
| 1 | Minimal | Near-identical to cloud-native; trivial adaptation |
| 2 | Low | Minor changes; same skill set, slightly more work |
| 3 | Moderate | Meaningful new work; requires platform awareness |
| 4 | High | Substantially harder; requires specialist knowledge |
| 5 | Extreme | Categorically different; requires dedicated expert staff |

**Total Effort (TE):** How much absolute work, regardless of how it compares to cloud-native?

| Rating | Label | Phase 1 (one-time) | Phase 2 (per customer) | Phase 3 (annual) |
|:---:|---|---|---|---|
| 1 | Minimal | < 2 person-weeks | < 2 person-days | < 0.1 FTE |
| 2 | Low | 2–8 person-weeks | 2–5 person-days | 0.1–0.3 FTE |
| 3 | Moderate | 2–6 person-months | 1–3 person-weeks | 0.3–1.0 FTE |
| 4 | High | 6–12 person-months | 3–6 person-weeks | 1.0–2.5 FTE |
| 5 | Very High | 12+ person-months | 6+ person-weeks | 2.5+ FTE |

**Divergence Flag:** Cells where RD and TE differ by 2+ points are flagged with **[D]** — these are strategic traps where one dimension masks the other.

---

## 4. Phase 1: Initial Refactoring to Open Kubernetes

One-time engineering investment to replace cloud-managed services with self-hosted open-source equivalents and build deployment automation for on-premises delivery.

### P1: Control Plane — Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | Replace EKS/AKS/GKE with kubeadm/RKE2. Build HA control plane provisioning, etcd backup automation, node pool management, add-on lifecycle tooling. The foundation everything else depends on. |
| CP-02 | Network Fabric / Ingress / Mesh | 5 | 4 | Replace VPC networking + managed ALB with Calico/Cilium CNI, self-managed ingress (Gateway API), optional service mesh. Network policy engine must be built from scratch. |
| CP-03 | IAM / RBAC | 4 | 4 | Replace Cognito/Entra ID with Keycloak or Dex. IAM is "a product line, not an infrastructure dependency" — seven sub-domains (authn, authz, federation, MFA, provisioning, audit, session management). |
| CP-04 | Secrets / Certs / PKI | 5 | 4 | Replace Secrets Manager with Vault (5-node Raft cluster). Deploy cert-manager for TLS automation. FIPS 140-3 compliance path must be architected. PKI root design is an irreversible decision. |
| CP-05 | Observability Infrastructure | 4 | 5 | Replace CloudWatch/Azure Monitor with Prometheus + Thanos/Mimir (metrics), Loki (logs), Tempo (traces), Grafana (dashboards), Alertmanager. One of the largest initial builds — 500K+ active time series at 3KB RAM each. |
| CP-06 | CI/CD Pipeline / GitOps | 4 | 4 | Build self-hosted CI/CD (ArgoCD/Flux + artifact registry). Must support per-customer deployment targets, not just a single cloud environment. GitOps for N customer environments is architecturally different from single-tenant CI/CD. |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 4 | Build per-customer deployment orchestration. Versioning strategy for 3–5 concurrent major versions across customer base. Blue-green/canary on per-customer K8s clusters. Rollback automation that works across heterogeneous environments. |
| CP-08 | Disaster Recovery / BC | 4 | 3 | Design DR strategy for self-hosted infrastructure. Backup automation for etcd, databases, and configuration. DR testing framework. Simpler than CP-01/CP-05 because it leverages components built elsewhere. |
| CP-09 | Compliance Automation | 4 | 3 | Build compliance evidence collection pipeline (audit logging, posture scanning, evidence export). Framework for FedRAMP/SOC2/HIPAA — but the tooling is bounded once built. |
| CP-10 | Security Operations | 4 | 4 | Replace GuardDuty/Defender with Falco for runtime protection. Self-hosted vulnerability scanning pipeline. Intrusion detection. Security event aggregation. |
| | **P1 Phase 1 Totals** | **avg 4.4** | **avg 4.0** | |

### P2: Application Logic — Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 | 2 | Service boundaries unchanged. Minor adjustments to service discovery (cloud DNS → CoreDNS/Consul). Communication patterns (gRPC, REST) are tier-invariant. |
| AL02 | Business Logic / Domain Services | 1 | 1 | **Zero refactoring.** Business logic is the same code regardless of deployment tier. This is the largest absolute codebase in the application but requires no changes. |
| AL03 | API Gateway / Edge Routing | 3 | 3 | Replace API Gateway managed service with Kong, APISIX, or Envoy Gateway. TLS termination, rate limiting, and auth integration must be self-configured. Gateway API migration if coming from Ingress NGINX. |
| AL04 | Data Access / ORM / Caching | 1 | 2 | ORM layer abstracts database — connection strings change, code doesn't. Validate ORM compatibility with self-hosted DB versions (PostgreSQL version differences). Update connection pool configs. |
| AL05 | Background Jobs / Async / EDA | 3 | 3 | Replace SQS/EventBridge with Kafka/NATS topics. Replace Step Functions with Temporal workflows. Event schema validation, dead-letter handling, and retry logic must be re-implemented against new message bus APIs. |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | Circuit breakers and health probes are largely application-level (Resilience4j, Polly). Minor adaptation for self-hosted service endpoints. Graceful shutdown and readiness probes are K8s-standard. |
| AL07 | Multi-Tenant Isolation | 1 | 1 | **Zero refactoring.** Multi-tenancy is enforced in application code (tenant-context middleware, row-level security). Tier-invariant at difficulty 3 — same work everywhere. |
| AL08 | Observability Instrumentation | 2 | 2 | Update OTLP exporter endpoints to point at self-hosted Prometheus/Loki/Tempo instead of managed backends. OpenTelemetry SDK is tier-agnostic by design. Verify trace/metric propagation. |
| AL09 | AI/ML Orchestration / Agent Pipelines | 2 | 3 | Agent orchestration code (LangGraph, MCP servers, guardrails) is portable. Main refactoring: integrate with customer's inference endpoints (replacing Bedrock/Azure OpenAI calls), self-hosted Temporal for workflow orchestration, self-hosted Langfuse for observability. Testing across new dependency topology is the bulk of effort. |
| AL10 | Testing / Contract Testing / Env Parity | 3 | 4 | **[D]** Build entirely new test infrastructure for on-prem environments. Integration test suites against self-hosted dependencies (PostgreSQL, Kafka, Milvus vs managed equivalents). Contract test framework must validate across K8s versions. Environment parity testing across N hardware profiles. Effort exceeds difficulty because the testing surface area is large even though each test is straightforward. |
| | **P2 Phase 1 Totals** | **avg 1.9** | **avg 2.3** | |

### P3: Data Plane — Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| DS1 | Relational Database HA | 4 | 4 | Replace RDS Multi-AZ with CloudNativePG + Patroni. Configure streaming replication, automatic failover, WAL archiving, connection pooling (PgBouncer), backup automation (pgBackRest/Barman). Major version upgrade procedures. |
| DS2 | NoSQL / Document Store | 3 | 3 | Replace DynamoDB/CosmosDB with MongoDB Community (Percona Operator) or ScyllaDB. Replica set configuration, oplog management, backup automation. |
| DS3 | Caching Layer | 3 | 2 | Replace ElastiCache with Redis via Spotahome Operator or Redis Sentinel. Relatively straightforward self-hosting — bounded operational surface. |
| DS4 | Object / Blob Storage | 2 | 2 | Replace S3 with MinIO. Well-documented S3-compatible API, Helm chart deployment. Erasure coding configuration, bucket lifecycle policies. |
| DS5 | Message Queuing (Simple) | 2 | 2 | Replace SQS with RabbitMQ or NATS. Simple message queues are among the easiest data services to self-host. Clustering, persistence configuration. |
| DS6 | Event Streaming (Kafka) | 4 | 4 | Replace MSK with self-hosted Kafka (Strimzi Operator). KRaft configuration (ZooKeeper path eliminated). Partition strategy, replication factor, ISR tuning. Disk sizing model: 1K msg/sec × 1KB × 86,400 × RF3 = 259 GB/day. One of the more complex data service builds. |
| DS7 | Search / Full-Text Index | 4 | 3 | Replace OpenSearch Service with self-hosted OpenSearch or Elasticsearch. JVM heap tuning, shard strategy, index lifecycle management. Operationally demanding but bounded scope. |
| DS8 | Vector Database | 4 | 3 | Replace managed Pinecone/pgvector-on-RDS with self-hosted Milvus (Helm) or Qdrant. HNSW/IVF index configuration, Woodpecker WAL migration (Milvus). Emerging operational domain — limited institutional knowledge available. |
| DS9 | Embedding Pipeline (GPU) | 3 | 3 | Customer provides GPU; ISV deploys embedding model serving on customer's GPU allocation. Pipeline logic (chunking, batch processing, vector store integration) is application-level. Reduced from original 5/5 because GPU hardware is customer scope. |
| DS10 | RAG Pipeline Orchestration | 3 | 4 | 8-stage pipeline: ingestion, chunking, embedding, vector storage, retrieval, reranking, context assembly, LLM handoff. Integration points with DS8 (vector DB), DS9 (embedding), and customer's inference endpoint. Large surface area drives effort above difficulty. Apache Tika 3.x for document parsing. |
| | **P3 Phase 1 Totals** | **avg 3.2** | **avg 3.0** | |

### P4: AI Model Plane — Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| S1 | Managed API Integration | 1 | 2 | Replace Bedrock/Azure OpenAI/Vertex AI endpoint calls with customer's inference endpoint. Auth method adaptation (cloud IAM → customer's auth). Error handling for different response schemas. Same pattern, different endpoint. |
| S2 | Self-Hosted Inference Engine | — | — | **Customer scope.** Customer operates vLLM/TGI on their GPUs. ISV has no refactoring work. |
| S3 | GPU Hardware Infrastructure | — | — | **Customer scope.** Customer owns all GPU hardware. |
| S4 | GPU Driver / CUDA Stack | — | — | **Customer scope.** Customer manages driver stack. |
| S5 | Multi-Tenant GPU Scheduling | — | — | **Customer scope.** Customer manages GPU allocation. |
| S6 | Model Routing / Load Balancing | 2 | 2 | Configure LiteLLM or routing layer to target customer-provided inference endpoints instead of cloud APIs. Health checks, fallback logic, retry budgets against customer's service. Simplified vs original because routing to endpoints, not managing engines. |
| S7 | Inference Monitoring | 2 | 2 | Application-layer TTFT/quality monitoring against customer's inference service. No GPU-level monitoring (DCGM) — that's customer scope. SLO definition and alerting for inference latency. |
| S8 | Model Lifecycle Management | 1 | 1 | Customer manages model artifacts and versions. ISV tracks which models are available and selects version in API calls. Minimal refactoring. |
| | **P4 Phase 1 Totals (ISV scope)** | **avg 1.5** | **avg 1.8** | |

### Phase 1 Summary

| Plane | Avg RD | Avg TE | Estimated One-Time Investment | Key Cost Driver |
|---|:---:|:---:|---|---|
| P1 Control Plane | 4.4 | 4.0 | 40–80 person-months | Building entire platform stack from scratch |
| P2 Application Logic | 1.9 | 2.3 | 10–25 person-months | Test infrastructure rebuild (AL10), SDK swaps at scale |
| P3 Data Plane | 3.2 | 3.0 | 20–40 person-months | Standing up every self-hosted data service |
| P4 AI Model Plane | 1.5 | 1.8 | 2–4 person-months | Endpoint integration changes |
| **Total** | **2.9** | **2.9** | **~72–149 person-months** | **P1 + P3 = ~80% of effort** |

---

## 5. Phase 2: Per-Customer Hardware Customization

Repeating effort for each new customer deployment. Driven by hardware heterogeneity across customer environments.

### P1: Control Plane — Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 4 | 4 | Each customer's server models, virtualization layer (VMware vs KVM vs bare metal), storage controllers, and NIC drivers require K8s configuration adaptation. Node pool sizing based on customer's available compute. |
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 4 | Customer's network topology, firewall rules, proxy requirements, DNS architecture, and egress policies are unique per site. CNI configuration, ingress routing, and network policies must be adapted. Most variable P1 subsegment per customer. |
| CP-03 | IAM / RBAC | 3 | 3 | Integrate with customer's existing identity provider (LDAP, SAML, OIDC). Map customer's organizational roles to ISV's RBAC model. Federation configuration. |
| CP-04 | Secrets / Certs / PKI | 3 | 3 | Integrate with customer's PKI infrastructure and certificate authority. Possibly integrate with customer's HSMs. Trust chain configuration per customer's security architecture. |
| CP-05 | Observability Infrastructure | 2 | 2 | Tune storage retention and memory allocation for customer's disk/memory profile. Mostly configuration — the observability stack itself is standardized. May need to integrate with customer's existing monitoring if they have one. |
| CP-06 | CI/CD Pipeline / GitOps | 2 | 2 | Adapt artifact delivery pipeline for customer's network constraints (air-gap, proxy, artifact mirror). Target-environment configuration in GitOps. |
| CP-07 | Deploy Lifecycle / Rollback | 3 | 3 | Establish deployment cadence, change management process, and maintenance windows with customer. Validate rollback procedures against customer's specific environment. |
| CP-08 | Disaster Recovery / BC | 3 | 3 | DR plan adapted to customer's infrastructure — backup storage targets, recovery time objectives aligned with customer's SLAs, failover testing in customer's environment. |
| CP-09 | Compliance Automation | 3 | 3 | Map ISV's compliance framework to customer's specific regulatory requirements (FedRAMP vs HIPAA vs SOC2 vs industry-specific). Evidence collection configured for customer's audit requirements. |
| CP-10 | Security Operations | 3 | 2 | Security policy adapted to customer's threat model and existing security tooling. Mostly configuration — security tooling is standardized. Integration with customer's SIEM if required. |
| | **P1 Phase 2 Totals** | **avg 3.0** | **avg 2.9** | |

### P2: Application Logic — Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 | 1 | Same architecture across all customers. No per-customer changes. |
| AL02 | Business Logic / Domain Services | 1 | 1 | Same code everywhere. Tenant configuration handles customer-specific behavior. |
| AL03 | API Gateway / Edge Routing | 1 | 1 | Gateway config is standardized. Customer-specific TLS certs handled by P1 (CP-04). |
| AL04 | Data Access / ORM / Caching | 1 | 1 | Connection strings from P3 config. No per-customer code changes. |
| AL05 | Background Jobs / Async / EDA | 1 | 1 | Event-driven architecture is standardized. No per-customer adaptation. |
| AL06 | Resilience Patterns / Runtime | 1 | 1 | Resilience patterns are application-level. Timeouts may need tuning for customer's network latency profile — minor config. |
| AL07 | Multi-Tenant Isolation | 1 | 1 | Multi-tenancy is application-level. No per-customer changes. |
| AL08 | Observability Instrumentation | 1 | 1 | OTel instrumentation is standardized. Exporter endpoints configured by P1. |
| AL09 | AI/ML Orchestration / Agent Pipelines | 1 | 2 | Adapt to customer's specific AI model availability — which models they host, context window sizes, endpoint URLs, rate limits. Feature flags for model-dependent capabilities. |
| AL10 | Testing / Contract Testing / Env Parity | 2 | 2 | Validation testing against each customer's specific environment. Smoke tests, integration verification, performance baseline. Per-customer test runs, not per-customer test code. |
| | **P2 Phase 2 Totals** | **avg 1.1** | **avg 1.2** | |

### P3: Data Plane — Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| DS1 | Relational Database HA | 2 | 2 | Tune shared_buffers, work_mem, wal_buffers for customer's memory. Storage layout for customer's disk topology. Backup targets configured per customer's storage. |
| DS2 | NoSQL / Document Store | 2 | 1 | Minor tuning for customer's storage performance. WiredTiger cache sizing. |
| DS3 | Caching Layer | 1 | 1 | Redis maxmemory config based on customer's available RAM. Standard across customers. |
| DS4 | Object / Blob Storage | 1 | 1 | MinIO erasure coding configured for customer's disk count. Minimal variation. |
| DS5 | Message Queuing (Simple) | 1 | 1 | Standard configuration. Persistence settings for customer's disk. |
| DS6 | Event Streaming (Kafka) | 2 | 2 | Kafka log.dirs configured for customer's disk topology. Broker memory sizing. Replication factor may vary based on customer's node count. |
| DS7 | Search / Full-Text Index | 2 | 1 | JVM heap sized to customer's available memory. Shard count based on data volume estimate. |
| DS8 | Vector Database | 2 | 2 | Index size and segment configuration based on customer's data volume and available memory. HNSW parameters may need tuning per customer's latency requirements. |
| DS9 | Embedding Pipeline (GPU) | 2 | 2 | Configure embedding batch size and concurrency for customer's GPU allocation. Validate embedding model compatibility with customer's GPU generation. |
| DS10 | RAG Pipeline Orchestration | 1 | 1 | RAG pipeline config is standardized. Endpoint URLs for customer's embedding and inference services. |
| | **P3 Phase 2 Totals** | **avg 1.6** | **avg 1.4** | |

### P4: AI Model Plane — Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| S1 | Managed API Integration | 1 | 2 | Map to customer's inference endpoint URLs, authentication method, and API schema. Each customer may expose different model APIs. |
| S2 | Self-Hosted Inference Engine | — | — | **Customer scope.** |
| S3 | GPU Hardware Infrastructure | — | — | **Customer scope.** |
| S4 | GPU Driver / CUDA Stack | — | — | **Customer scope.** |
| S5 | Multi-Tenant GPU Scheduling | — | — | **Customer scope.** |
| S6 | Model Routing / Load Balancing | 1 | 2 | Configure routing for customer's available models — different customers may have different model catalogs, different capacity, different failover options. |
| S7 | Inference Monitoring | 1 | 1 | Set SLO thresholds based on customer's inference service performance characteristics. |
| S8 | Model Lifecycle Management | 1 | 1 | Inventory which models customer provides. Version compatibility verification. |
| | **P4 Phase 2 Totals (ISV scope)** | **avg 1.0** | **avg 1.5** | |

### Phase 2 Summary

| Plane | Avg RD | Avg TE | Estimated Per-Customer Effort | Key Cost Driver |
|---|:---:|:---:|---|---|
| P1 Control Plane | 3.0 | 2.9 | 6–14 person-weeks | Infrastructure adaptation to customer hardware/network/security |
| P2 Application Logic | 1.1 | 1.2 | 1–2 person-weeks | Validation testing, model availability mapping |
| P3 Data Plane | 1.6 | 1.4 | 2–4 person-weeks | Performance tuning for customer's storage/memory |
| P4 AI Model Plane | 1.0 | 1.5 | 0.5–1 person-weeks | Endpoint configuration, model catalog mapping |
| **Total** | **1.8** | **1.8** | **~10–21 person-weeks per customer** | **P1 = ~60% of per-customer effort** |

---

## 6. Phase 3: Ongoing Software Updates and Support

Recurring annual cost for maintaining and updating ISV software across all deployed customer environments. Scales with N customers × update frequency.

### P1: Control Plane — Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | **Yes** | 3.0–6.0 | 3 minor K8s versions/year, 12–14 month support windows. Each customer on a different version and upgrade schedule. Node drain coordination per customer. Hardware-specific regression risk per customer. The single largest ongoing P1 cost. |
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 4 | **Yes** | 1.75–3.5 | CNI upgrades, network policy updates, ingress controller patches per customer. Gateway API evolution. Network-related incidents are the most common customer-specific issues due to hardware heterogeneity. |
| CP-03 | IAM / RBAC | 3 | 4 | **Partial** | 2.75–4.75 | Keycloak upgrades, identity provider integration maintenance. Core IAM tooling is shared; per-customer federation config maintenance adds linear cost. Identity incidents require per-customer investigation. |
| CP-04 | Secrets / Certs / PKI | 4 | 4 | **Yes** | 2.5–5.0 | Certificate rotation per customer. Vault upgrades across N environments. FIPS 140-3 migration (deadline September 2026) is a one-time event but must be coordinated per customer. Seal/unseal operations during Vault upgrades are per-customer. |
| CP-05 | Observability Infrastructure | 4 | 5 | **Partial** | 4.6–7.0 | Prometheus/Grafana/Loki upgrades across customer environments. Storage management for metrics/logs (grows with time). Jaeger v1→v2 migration. The observability stack requires the most ongoing attention of any P1 subsegment — 500K+ active time series per customer instance. Base staff is shared but storage/capacity management is per-customer. |
| CP-06 | CI/CD Pipeline / GitOps | 3 | 3 | **Partial** | 2.0–3.25 | Pipeline maintenance, artifact registry management. Pipeline logic is shared; delivery targets are per-customer. ArgoCD/Flux version upgrades. |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 5 | **Yes** | 1.5–3.0 | **The linear scaling problem.** N customers = N separate deployment coordination sequences for every release. CVE patches: 50 customers = 50 patch cycles. 3–5 concurrent software versions across customer base. Rollback requires per-customer database state awareness. This subsegment's effort is directly proportional to customer count. |
| CP-08 | Disaster Recovery / BC | 4 | 3 | **Yes** | 1.5–2.5 | DR testing per customer on a regular cadence. Backup verification per customer. Recovery procedure validation. Less frequent than CP-07 but still per-customer. |
| CP-09 | Compliance Automation | 4 | 4 | **Yes** | 2.5–4.0 | Compliance evidence regeneration per audit cycle per customer. Regulatory changes require re-assessment across customer base. SOC2 annual audits, FedRAMP continuous monitoring. |
| CP-10 | Security Operations | 4 | 4 | **Partial** | 2.75–5.5 | Vulnerability scanning, incident response, runtime protection across N environments. Security tooling (Falco) is shared; incident investigation and patch coordination is per-customer. CVE response time pressure. |
| | **P1 Phase 3 Totals** | **avg 4.0** | **avg 4.1** | | **20–38 FTE** | |

### P2: Application Logic — Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 | 2 | No | 0.8–1.5 | Service communication patterns are stable. Occasional refactoring for new bounded contexts. Same work regardless of tier. |
| AL02 | Business Logic / Domain Services | 1 | 4 | No | 3.0–6.0 | **[D]** The largest absolute FTE in P2 — this is the ISV's core product development. But relative difficulty is 1 because the work is identical on cloud-native. Business logic doesn't change with deployment tier. High effort, minimal tier delta. |
| AL03 | API Gateway / Edge Routing | 2 | 2 | Partial | 1.5–3.0 | Gateway configuration updates with new API versions. Per-customer gateway config validation for major releases. |
| AL04 | Data Access / ORM / Caching | 1 | 2 | No | 0.75–1.5 | ORM maintenance, connection pool tuning. Occasional migration for database version changes (triggered by P3 upgrades). |
| AL05 | Background Jobs / Async / EDA | 2 | 3 | No | 2.75–5.6 | **[D]** Event schema evolution, Temporal workflow version management, dead-letter queue monitoring. High absolute effort because the event-driven architecture is complex regardless of tier. Tier delta is modest (Kafka vs SQS at application layer). |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | No | 0.75–1.5 | Resilience pattern tuning, circuit breaker threshold adjustments. Minor ongoing work. |
| AL07 | Multi-Tenant Isolation | 1 | 2 | No | 0.75–1.5 | Multi-tenancy framework is stable. Occasional refinement for new data paths or isolation requirements. Same across tiers. |
| AL08 | Observability Instrumentation | 2 | 2 | No | 0.5–1.0 | Instrumentation updates as new services or features are added. OTel SDK version upgrades. |
| AL09 | AI/ML Orchestration / Agent Pipelines | 3 | 4 | No | 4.0–7.0 | **Rapidly evolving ecosystem.** LangChain/LangGraph version upgrades, new agent patterns, guardrail policy updates, MCP protocol evolution. High effort because the AI/agent stack changes faster than any other application subsegment. On-prem adds complexity of coordinating self-hosted Temporal and Langfuse upgrades. |
| AL10 | Testing / Contract Testing / Env Parity | 3 | 4 | **Yes** | 3.75–7.0 | **[D]** Test suite maintenance across N customer hardware profiles. Regression testing for each release against multiple K8s versions and hardware configurations. The testing tax is proportional to customer count and hardware diversity. High absolute effort because the test matrix multiplies. |
| | **P2 Phase 3 Totals** | **avg 1.8** | **avg 2.7** | | **18.6–35.6 FTE** | **TE exceeds RD by 0.9 — systematic divergence** |

### P3: Data Plane — Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| DS1 | Relational Database HA | 4 | 4 | **Yes** | 1.5–3.0 | PostgreSQL major version upgrades per customer. Patroni failover verification after upgrades. WAL archiving monitoring. Backup validation per customer. PgBouncer connection pool tuning. The highest-consequence data service to upgrade (ACID guarantees at risk). |
| DS2 | NoSQL / Document Store | 3 | 2 | Partial | 0.6–1.1 | MongoDB operator upgrades, replica set maintenance. Lower operational burden than relational HA. |
| DS3 | Caching Layer | 2 | 2 | Partial | 0.4–0.7 | Redis version updates, Sentinel/cluster maintenance. Bounded operational surface. |
| DS4 | Object / Blob Storage | 2 | 2 | Partial | 0.25–0.6 | MinIO version updates, erasure coding verification, storage capacity management. |
| DS5 | Message Queuing (Simple) | 2 | 2 | Partial | 0.4–0.7 | RabbitMQ/NATS version updates. Simple operational profile. |
| DS6 | Event Streaming (Kafka) | 4 | 4 | **Yes** | 1.5–2.5 | Kafka version upgrades (KRaft is mandatory, irreversible). Partition rebalancing, ISR monitoring, consumer group management. 13–26 hrs/week self-hosted vs 2–3 hrs/week MSK. Per-customer upgrade coordination for schema-breaking changes. |
| DS7 | Search / Full-Text Index | 3 | 3 | Partial | 0.7–1.2 | OpenSearch/Elasticsearch version upgrades, JVM tuning, shard rebalancing. Index re-creation may be required for major version upgrades. |
| DS8 | Vector Database | 4 | 3 | Partial | 1.25–1.75 | Milvus/Qdrant upgrades, Woodpecker WAL migration, index optimization. Emerging technology with rapid release cadence. Limited institutional knowledge for troubleshooting. |
| DS9 | Embedding Pipeline (GPU) | 3 | 3 | Partial | 2.0–3.25 | Embedding model version management. Model version changes may trigger full corpus re-embedding — high-cost event. Pipeline tuning as data volumes grow. Customer GPU allocation changes may require re-tuning. |
| DS10 | RAG Pipeline Orchestration | 3 | 4 | No | 3.25–4.75 | **[D]** RAG patterns are rapidly evolving — chunking strategies, reranking models, context window optimization. High absolute effort because the AI retrieval stack changes frequently. Effort driven by ecosystem evolution, not customer count. |
| | **P3 Phase 3 Totals** | **avg 3.0** | **avg 2.9** | | **~10–18 FTE** | |

### P4: AI Model Plane — Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem, revised) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| S1 | Managed API Integration | 1 | 2 | Partial | 0.1–0.3 | Maintain API integration with each customer's inference endpoints. Handle customer-side model deprecation or endpoint changes. Per-customer API compatibility monitoring. |
| S2 | Self-Hosted Inference Engine | — | — | — | — | **Customer scope.** |
| S3 | GPU Hardware Infrastructure | — | — | — | — | **Customer scope.** |
| S4 | GPU Driver / CUDA Stack | — | — | — | — | **Customer scope.** |
| S5 | Multi-Tenant GPU Scheduling | — | — | — | — | **Customer scope.** |
| S6 | Model Routing / Load Balancing | 2 | 2 | Partial | 0.2–0.5 | Routing configuration updates as customers add/change models. Health check tuning. Cost attribution updates. |
| S7 | Inference Monitoring | 1 | 2 | Partial | 0.1–0.5 | SLO threshold adjustments. Monitoring dashboard maintenance. Per-customer inference quality tracking. |
| S8 | Model Lifecycle Management | 1 | 1 | No | 0.05–0.15 | Track customer model availability. Minimal ISV effort — customer manages artifacts. |
| | **P4 Phase 3 Totals (ISV scope)** | **avg 1.3** | **avg 1.8** | | **~0.5–1.5 FTE** | |

### Phase 3 Summary

| Plane | Avg RD | Avg TE | Annual FTE (research-based) | Key Cost Driver |
|---|:---:|:---:|---|---|
| P1 Control Plane | 4.0 | 4.1 | 20–38 FTE | K8s upgrades, security patching, deploy coordination across N customers |
| P2 Application Logic | 1.8 | 2.7 | 18.6–35.6 FTE | **[D]** Product development (tier-invariant) + per-customer deploy/test logistics |
| P3 Data Plane | 3.0 | 2.9 | ~10–18 FTE | Database and message broker upgrades across N customers |
| P4 AI Model Plane | 1.3 | 1.8 | ~0.5–1.5 FTE | Endpoint maintenance; customer manages infrastructure |
| **Total** | **2.7** | **3.0** | **~49–93 FTE** | **P1 = highest RD and TE; P2 = largest TE-RD divergence** |

---

## 7. Divergence Analysis: Where Difficulty and Effort Disagree

The most strategically important cells are those where relative difficulty and total effort diverge — these are the subsegments most likely to be underestimated or overestimated in planning.

### Subsegments Where Effort Exceeds Difficulty (planning traps — easy to underestimate)

| Phase | ID | Subsegment | RD | TE | Gap | Why |
|---|:---:|---|:---:|:---:|:---:|---|
| Phase 1 | AL10 | Testing / Env Parity | 3 | 4 | +1 | Building on-prem test infrastructure is straightforward per test, but the test matrix across self-hosted dependencies is large |
| Phase 3 | AL02 | Business Logic / Domain Services | 1 | 4 | +3 | The largest ongoing FTE in the application — pure product development. Zero tier difficulty but massive absolute effort. Easy to overlook in on-prem cost models because it looks "tier-invariant" |
| Phase 3 | AL05 | Background Jobs / Async / EDA | 2 | 3 | +1 | Event-driven architecture is complex regardless of tier. Kafka/Temporal event schema management is high-volume ongoing work |
| Phase 3 | AL09 | AI/ML Orchestration / Agent Pipelines | 3 | 4 | +1 | AI/agent ecosystem evolves rapidly. High ongoing rework regardless of tier delta |
| Phase 3 | AL10 | Testing / Contract Testing | 3 | 4 | +1 | Test matrix multiplied by customer count and hardware diversity |
| Phase 3 | DS10 | RAG Pipeline Orchestration | 3 | 4 | +1 | RAG patterns evolving rapidly — continuous rework effort |
| **Phase 3** | **P2 overall** | **Application Logic (all)** | **1.8** | **2.7** | **+0.9** | **Systematic divergence: P2 looks easy on the difficulty scale but is the second-largest FTE block** |

### Subsegments Where Difficulty and Effort Align (accurately estimated)

| Phase | Plane | Avg RD | Avg TE | Gap |
|---|---|:---:|:---:|:---:|
| Phase 1 | P1 Control Plane | 4.4 | 4.0 | 0.4 |
| Phase 1 | P3 Data Plane | 3.2 | 3.0 | 0.2 |
| Phase 2 | All planes | 1.8 | 1.8 | 0.0 |
| Phase 3 | P1 Control Plane | 4.0 | 4.1 | 0.1 |
| Phase 3 | P3 Data Plane | 3.0 | 2.9 | 0.1 |

**Pattern:** P1 and P3 are well-calibrated — hard things are also large things. P2 is systematically miscalibrated — the difficulty scale understates the effort because application logic is large regardless of deployment tier.

---

## 8. Grand Summary

### Three-Phase × Four-Plane Matrix (Relative Difficulty)

| Plane | Phase 1 RD | Phase 2 RD | Phase 3 RD | All-Phase Avg RD |
|---|:---:|:---:|:---:|:---:|
| P1 Control Plane | **4.4** | **3.0** | **4.0** | **3.8** |
| P2 Application Logic | 1.9 | 1.1 | 1.8 | 1.6 |
| P3 Data Plane | **3.2** | 1.6 | **3.0** | 2.6 |
| P4 AI Model Plane | 1.5 | 1.0 | 1.3 | 1.3 |

### Three-Phase × Four-Plane Matrix (Total Effort)

| Plane | Phase 1 TE | Phase 2 TE | Phase 3 TE | All-Phase Avg TE |
|---|:---:|:---:|:---:|:---:|
| P1 Control Plane | **4.0** | **2.9** | **4.1** | **3.7** |
| P2 Application Logic | 2.3 | 1.2 | **2.7** | 2.1 |
| P3 Data Plane | **3.0** | 1.4 | **2.9** | 2.4 |
| P4 AI Model Plane | 1.8 | 1.5 | 1.8 | 1.7 |

### Key Findings

1. **P1 (Control Plane) dominates both dimensions across all three phases.** It is the hardest AND the most effort-intensive in Phase 1, Phase 2, and Phase 3. This is the core of the ISV's on-prem resistance.

2. **P2 (Application Logic) is the largest systematic divergence.** Average RD of 1.6 vs average TE of 2.1 — a consistent gap across all three phases. In Phase 3, the gap widens to RD 1.8 vs TE 2.7. An ISV that plans based only on relative difficulty will underestimate P2 ongoing costs by ~50%.

3. **P3 (Data Plane) is accurately calibrated.** Difficulty and effort align closely across all three phases. Data service operations are hard AND large in roughly equal measure.

4. **P4 (AI Model Plane) is nearly eliminated** under the customer-provides-GPU-and-models scope. All-phase average of RD 1.3 / TE 1.7. The ISV's AI-related effort is in P2 (agent orchestration) and P3 (embedding/RAG pipelines), not P4.

5. **Phase 2 (per-customer customization) is dominated by P1.** The application code (P2) and data services (P3) are largely standardized across customers. Infrastructure configuration (P1) is what varies — and it's what makes each new customer deployment expensive.

6. **Phase 3 (ongoing support) has two distinct cost types:**
   - **Linear with N customers:** CP-01, CP-02, CP-04, CP-07, DS1, DS6 — these subsegments scale directly with customer count
   - **Fixed/shared:** AL02, AL05, AL09, DS10 — these are product development costs that are the same regardless of customer count but large in absolute terms

---

## 9. Sources and Confidence

| Data Source | Confidence | Coverage |
|---|---|---|
| Phase 3 FTE estimates | **High** | Directly from P1–P4 research (78 files, 390K+ words, 8,740+ citations) |
| Phase 1 difficulty ratings | **High** | Derived from P1–P4 tier deltas — the refactoring work is the delta between cloud-native and on-prem configurations |
| Phase 1 effort estimates | **Medium** | Estimated from FTE data and typical platform build durations; not directly measured |
| Phase 2 ratings | **Medium** | Derived from per-customer deployment patterns documented in CP-07, G1; limited empirical data on hardware heterogeneity impact |
| Phase 2 effort estimates | **Medium-Low** | Industry-informed estimates; no direct per-customer deployment measurement in research corpus |
| P4 scope reduction | **High** | Customer-provides-GPU scope clearly eliminates S2–S5 from ISV responsibility; S1/S6/S7/S8 reduction follows logically |

**What would strengthen this analysis:**
- Empirical Phase 1 build timelines from ISVs that have completed cloud-to-on-prem refactoring
- Per-customer deployment cost data from ISVs operating at N=10+ on-prem customers
- Measurement of hardware heterogeneity impact on Phase 2 effort (how much does network/storage/virtualization variance actually cost per customer?)
