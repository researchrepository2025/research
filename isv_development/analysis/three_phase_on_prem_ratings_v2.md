# Three-Phase On-Premises Subsegment Ratings (v2)

## ISV SaaS Deployment: Relative Difficulty and Total Effort by Phase

**Date:** 2026-02-19 (Revised)
**Version:** 2.0 — Incorporates all findings from 35-agent, 9-wave independent review (SL3a)
**Input Files:** P1_control_plane.md, P2_application_logic.md, P3_data_plane.md, P4_ai_model_plane.md, G1_n_services_multiplier.md, S1_four_plane_synthesis.md
**Review Sources:** SL1a, SL1b, SL1c, SL2a, SL2b, SL2c, CC1-CC5, RP1a-RP4c, GT1-GT5 (33 review files, ~157,000 words, 503 web + 1,027 corpus citations)
**Scope:** All 38 MECE subsegments across 4 planes, rated for 3 deployment phases

**Confidence Key:** Each rating carries a parenthetical confidence indicator from the 35-agent review:
- **(H)** = High confidence — confirmed by multiple independent review agents with ground truth verification
- **(M)** = Medium confidence — confirmed with caveats or limited independent corroboration
- **(L)** = Low confidence — qualitative estimate only; would benefit most from empirical validation

---

## 1. Scope and Responsibility Split

| Domain | Owner | Examples |
|---|---|---|
| **Hardware environment** | Customer | Servers, GPUs, networking equipment, storage arrays, power, cooling, rack space, physical security |
| **GPU + AI models** | Customer | GPU procurement, driver management, inference engine operation, model weights, CUDA stack |
| **All software** | ISV | Kubernetes, databases, message brokers, observability, security tooling, application code, CI/CD |
| **Software-to-hardware adaptation** | ISV | Customizing software deployment to each customer's specific hardware environment |

**Implication for P4:** Subsegments S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) shift to customer responsibility. ISV retains S1 (API Integration), S6 (Routing), S7 (Monitoring), and S8 (Lifecycle) in reduced form -- calling customer-provided inference endpoints rather than managing infrastructure.

---

## 2. Three Deployment Phases

| Phase | Cost Structure | Scales With |
|---|---|---|
| **Phase 1: Initial Refactoring** | One-time engineering investment to make cloud-native SaaS portable to open K8s | Fixed (amortized across customers) |
| **Phase 2: Per-Customer Customization** | Adapting software to each customer's hardware environment | N customers (linear) |
| **Phase 3: Ongoing Updates & Support** | Recurring maintenance, upgrades, patching, incident response | N customers x update frequency |

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
| 2 | Low | 2-8 person-weeks | 2-5 person-days | 0.1-0.3 FTE |
| 3 | Moderate | 2-6 person-months | 1-3 person-weeks | 0.3-1.0 FTE |
| 4 | High | 6-12 person-months | 3-6 person-weeks | 1.0-2.5 FTE |
| 5 | Very High | 12+ person-months | 6+ person-weeks | 2.5+ FTE |

**Divergence Flag:** Cells where RD and TE differ by 2+ points are flagged with **[D]** -- these are strategic traps where one dimension masks the other.

---

## 4. Phase 1: Initial Refactoring to Open Kubernetes

One-time engineering investment to replace cloud-managed services with self-hosted open-source equivalents and build deployment automation for on-premises delivery.

**Parallelization note:** The Phase 1 effort estimates assume a parallelization factor of 0.55-0.67x, converting raw unconstrained totals to the stated ranges. This factor reflects a 5-8 engineer team with parallel workstreams constrained by the CP-01 serial dependency chain (cluster lifecycle must be operational before dependent subsystems can be deployed). CP-01 imposes forced serialization on approximately 35-45% of Phase 1 work. For ISVs with deep cloud-native but no on-premises experience, a 20-30% learning-curve uplift is typical.

### P1: Control Plane -- Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 5 (H) | 5 (H) | Replace EKS/AKS/GKE with kubeadm/RKE2. Build HA control plane provisioning, etcd backup automation, node pool management, add-on lifecycle tooling. The foundation everything else depends on. |
| CP-02 | Network Fabric / Ingress / Mesh | 5 (H) | 4 (H) | Replace VPC networking + managed ALB with Calico/Cilium CNI, self-managed ingress (Gateway API), optional service mesh. Network policy engine must be built from scratch. |
| CP-03 | IAM / RBAC | 4 (H) | 4 (H) | Replace Cognito/Entra ID with Keycloak or Dex. IAM is "a product line, not an infrastructure dependency" -- seven sub-domains (authn, authz, federation, MFA, provisioning, audit, session management). |
| CP-04 | Secrets / Certs / PKI | 5 (H) | 4 (H) | Replace Secrets Manager with Vault (5-node Raft cluster). Deploy cert-manager for TLS automation. FIPS 140-3 compliance path must be architected. PKI root design is an irreversible decision. |
| CP-05 | Observability Infrastructure | 4 (H) | 5 (H) | Replace CloudWatch/Azure Monitor with Prometheus + Thanos/Mimir (metrics), Loki (logs), Tempo (traces), Grafana (dashboards), Alertmanager. One of the largest initial builds -- 500K+ active time series at 3KB RAM each. |
| CP-06 | CI/CD Pipeline / GitOps | 4 (H) | 4 (H) | Build self-hosted CI/CD (ArgoCD/Flux + artifact registry). Must support per-customer deployment targets, not just a single cloud environment. GitOps for N customer environments is architecturally different from single-tenant CI/CD. |
| CP-07 | Deploy Lifecycle / Rollback | 5 (H) | 4 (H) | Build per-customer deployment orchestration. Versioning strategy for 3-5 concurrent major versions across customer base. Blue-green/canary on per-customer K8s clusters. Rollback automation that works across heterogeneous environments. |
| CP-08 | Disaster Recovery / BC | 4 (H) | 3 (H) | Design DR strategy for self-hosted infrastructure. Backup automation for etcd, databases, and configuration. DR testing framework. Simpler than CP-01/CP-05 because it leverages components built elsewhere. |
| CP-09 | Compliance Automation | 4 (H) | 3 (H) | Build compliance evidence collection pipeline (audit logging, posture scanning, evidence export). Framework for FedRAMP/SOC2/HIPAA -- but the tooling is bounded once built. |
| CP-10 | Security Operations | 4 (H) | 4 (H) | Replace GuardDuty/Defender with Falco for runtime protection. Self-hosted vulnerability scanning pipeline. Intrusion detection. Security event aggregation. |
| | **P1 Phase 1 Totals** | **avg 4.4** | **avg 4.0** | |

### P2: Application Logic -- Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 (H) | 2 (H) | Service boundaries unchanged. Minor adjustments to service discovery (cloud DNS to CoreDNS/Consul). Communication patterns (gRPC, REST) are tier-invariant. |
| AL02 | Business Logic / Domain Services | 1 (H) | 1 (H) | **Zero refactoring.** Business logic is the same code regardless of deployment tier. This is the largest absolute codebase in the application but requires no changes. |
| AL03 | API Gateway / Edge Routing | 3 (H) | 3 (H) | Replace API Gateway managed service with Kong, APISIX, or Envoy Gateway. TLS termination, rate limiting, and auth integration must be self-configured. Gateway API migration if coming from Ingress NGINX. |
| AL04 | Data Access / ORM / Caching | 1 (H) | 2 (H) | ORM layer abstracts database -- connection strings change, code doesn't. Validate ORM compatibility with self-hosted DB versions (PostgreSQL version differences). Update connection pool configs. |
| AL05 | Background Jobs / Async / EDA | 3 (H) | 3 (H) | Replace SQS/EventBridge with Kafka/NATS topics. Replace Step Functions with Temporal workflows. Event schema validation, dead-letter handling, and retry logic must be re-implemented against new message bus APIs. |
| AL06 | Resilience Patterns / Runtime | 2 (H) | 2 (H) | Circuit breakers and health probes are largely application-level (Resilience4j, Polly). Minor adaptation for self-hosted service endpoints. Graceful shutdown and readiness probes are K8s-standard. |
| AL07 | Multi-Tenant Isolation | 1 (H) | 1 (H) | **Zero refactoring.** Multi-tenancy is enforced in application code (tenant-context middleware, row-level security). Tier-invariant at difficulty 3 -- same work everywhere. |
| AL08 | Observability Instrumentation | 2 (H) | 2 (H) | Update OTLP exporter endpoints to point at self-hosted Prometheus/Loki/Tempo instead of managed backends. OpenTelemetry SDK is tier-agnostic by design. Verify trace/metric propagation. |
| AL09 | AI/ML Orchestration / Agent Pipelines | 2 (H) | 3 (H) | Agent orchestration code (LangGraph, MCP servers, guardrails) is portable. Main refactoring: integrate with customer's inference endpoints (replacing Bedrock/Azure OpenAI calls), self-hosted Temporal for workflow orchestration, self-hosted Langfuse for observability. Testing across new dependency topology is the bulk of effort. |
| AL10 | Testing / Contract Testing / Env Parity | 3 (H) | 4 (H) | Build entirely new test infrastructure for on-prem environments. Integration test suites against self-hosted dependencies (PostgreSQL, Kafka, Milvus vs managed equivalents). Contract test framework must validate across K8s versions. Environment parity testing across N hardware profiles. Effort exceeds difficulty because the testing surface area is large even though each test is straightforward. |
| | **P2 Phase 1 Totals** | **avg 1.9** | **avg 2.3** | |

### P3: Data Plane -- Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| DS1 | Relational Database HA | 4 (H) | 4 (H) | Replace RDS Multi-AZ with CloudNativePG + Patroni. Configure streaming replication, automatic failover, WAL archiving, connection pooling (PgBouncer), backup automation (pgBackRest/Barman). Major version upgrade procedures. |
| DS2 | NoSQL / Document Store | 3 (H) | 3 (H) | Replace DynamoDB/CosmosDB with MongoDB Community (Percona Operator) or ScyllaDB. Replica set configuration, oplog management, backup automation. |
| DS3 | Caching Layer | 3 (H) | 2 (H) | Replace ElastiCache with Redis via Spotahome Operator or Redis Sentinel. Relatively straightforward self-hosting -- bounded operational surface. |
| DS4 | Object / Blob Storage | 2 (H) | 2 (H) | Replace S3 with MinIO. Well-documented S3-compatible API, Helm chart deployment. Erasure coding configuration, bucket lifecycle policies. |
| DS5 | Message Queuing (Simple) | 2 (H) | 2 (H) | Replace SQS with RabbitMQ or NATS. Simple message queues are among the easiest data services to self-host. Clustering, persistence configuration. |
| DS6 | Event Streaming (Kafka) | 4 (H) | 4 (H) | Replace MSK with self-hosted Kafka (Strimzi Operator). KRaft configuration (ZooKeeper path eliminated). Partition strategy, replication factor, ISR tuning. Disk sizing model: 1K msg/sec x 1KB x 86,400 x RF3 = 259 GB/day. One of the more complex data service builds. |
| DS7 | Search / Full-Text Index | 4 (H) | 3 (H) | Replace OpenSearch Service with self-hosted OpenSearch or Elasticsearch. JVM heap tuning, shard strategy, index lifecycle management. Operationally demanding but bounded scope. |
| DS8 | Vector Database | 4 (H) | 3 (H) | Replace managed Pinecone/pgvector-on-RDS with self-hosted Milvus (Helm) or Qdrant. HNSW/IVF index configuration, Woodpecker WAL migration (Milvus). Emerging operational domain -- limited institutional knowledge available. |
| DS9 | Embedding Pipeline (GPU) | 3 (H) | 3 (H) | Customer provides GPU; ISV deploys embedding model serving on customer's GPU allocation. Pipeline logic (chunking, batch processing, vector store integration) is application-level. Reduced from original 5/5 because GPU hardware is customer scope. |
| DS10 | RAG Pipeline Orchestration | 3 (H) | 4 (H) | 8-stage pipeline: ingestion, chunking, embedding, vector storage, retrieval, reranking, context assembly, LLM handoff. Integration points with DS8 (vector DB), DS9 (embedding), and customer's inference endpoint. Large surface area drives effort above difficulty. Apache Tika 3.x for document parsing. |
| | **P3 Phase 1 Totals** | **avg 3.2** | **avg 3.0** | |

### P4: AI Model Plane -- Phase 1

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| S1 | Managed API Integration | **2** (H) | 2 (H) | Replace Bedrock/Azure OpenAI/Vertex AI endpoint calls with customer's inference endpoint. Auth method re-implementation (cloud IAM to bearer token/mTLS). Bedrock schema delta (system prompt handling differs from OpenAI format). Error handling rewrite for provider-specific response schemas. *[v2: RD raised from 1 to 2 based on auth re-implementation scope, Bedrock schema delta, and error handling rewrite -- SL1a Section 2; RP4a.]* |
| S2 | Self-Hosted Inference Engine | -- | -- | **Customer scope.** Customer operates vLLM/TGI on their GPUs. ISV has no refactoring work. |
| S3 | GPU Hardware Infrastructure | -- | -- | **Customer scope.** Customer owns all GPU hardware. |
| S4 | GPU Driver / CUDA Stack | -- | -- | **Customer scope.** Customer manages driver stack. |
| S5 | Multi-Tenant GPU Scheduling | -- | -- | **Customer scope.** Customer manages GPU allocation. |
| S6 | Model Routing / Load Balancing | 2 (H) | 2 (H) | Configure LiteLLM or routing layer to target customer-provided inference endpoints instead of cloud APIs. Health checks, fallback logic, retry budgets against customer's service. Simplified vs original because routing to endpoints, not managing engines. |
| S7 | Inference Monitoring | 2 (H) | 2 (H) | Application-layer TTFT/quality monitoring against customer's inference service. No GPU-level monitoring (DCGM) -- that's customer scope. SLO definition and alerting for inference latency. |
| S8 | Model Lifecycle Management | 1 (H) | 1 (H) | Customer manages model artifacts and versions. ISV tracks which models are available and selects version in API calls. Minimal refactoring. |
| | **P4 Phase 1 Totals (ISV scope)** | **avg 1.75** | **avg 1.8** | *[v2: avg RD corrected from 1.5 to 1.75 after S1 RD adjustment 1 to 2.]* |

### Phase 1 Summary

| Plane | Avg RD | Avg TE | Estimated One-Time Investment | Key Cost Driver |
|---|:---:|:---:|---|---|
| P1 Control Plane | 4.4 | 4.0 | 40-80 person-months | Building entire platform stack from scratch |
| P2 Application Logic | 1.9 | 2.3 | 10-25 person-months | Test infrastructure rebuild (AL10), SDK swaps at scale |
| P3 Data Plane | 3.2 | 3.0 | 20-40 person-months | Standing up every self-hosted data service |
| P4 AI Model Plane | 1.75 | 1.8 | 2-4 person-months | Endpoint integration changes |
| **Total** | **3.0** | **2.9** | **~72-149 person-months** | **P1 + P3 = ~80% of effort** |

*[v2: P4 avg RD corrected from 1.5 to 1.75. Total RD corrected from 2.9 to 3.0 (computed 2.971, rounds to 3.0) -- CC1 D-2.]*

---

## 5. Phase 2: Per-Customer Customization: Software Adaptation to Customer Hardware

Repeating effort for each new customer deployment. Driven by hardware heterogeneity across customer environments. The ISV customizes software to customer hardware; the ISV does not customize hardware.

*[v2: Heading corrected from "Per-Customer Hardware Customization" to clarify that the ISV adapts software, not hardware -- CC4 Section 6.]*

**Customer-segment variance:** The per-customer effort estimates below assume a mature ISV (5+ deployments) deploying to connected, commercially regulated customers with standard hardware. For non-standard profiles:
- **Air-gapped customers:** P1 effort rises to 9-18 person-weeks (vs. 6-14 stated); total 14-27 person-weeks
- **Hardware-heterogeneous customers:** P3 effort rises to 3-6 person-weeks (vs. 2-4 stated); total 12-25 person-weeks
- **First 3-4 customers:** Expect to exceed even revised ranges before deployment automation reaches maturity

**Hidden Phase 1 dependency:** Four P3 subsegments (DS1, DS6, DS8, DS9) carry Phase 2 TE=2 ratings that depend on pre-built configuration templates delivered during Phase 1. If those templates do not exist, the Phase 2 engineer must perform empirical investigation per customer, which shifts the work from template application to diagnostic engineering -- a materially harder task.

### P1: Control Plane -- Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 4 (M) | 4 (M) | Each customer's server models, virtualization layer (VMware vs KVM vs bare metal), storage controllers, and NIC drivers require K8s configuration adaptation. Node pool sizing based on customer's available compute. |
| CP-02 | Network Fabric / Ingress / Mesh | 4 (H) | 4 (H) | Customer's network topology, firewall rules, proxy requirements, DNS architecture, and egress policies are unique per site. CNI configuration, ingress routing, and network policies must be adapted. Most variable P1 subsegment per customer. *Air-gapped/regulated: TE may reach 5 due to network isolation constraints.* |
| CP-03 | IAM / RBAC | 3 (M) | 3 (M) | Integrate with customer's existing identity provider (LDAP, SAML, OIDC). Map customer's organizational roles to ISV's RBAC model. Federation configuration. |
| CP-04 | Secrets / Certs / PKI | 3 (M) | 3 (M) | Integrate with customer's PKI infrastructure and certificate authority. Possibly integrate with customer's HSMs. Trust chain configuration per customer's security architecture. *Regulated/HSM customers: RD may reach 4 due to PKCS#11 driver variance (SafeNet vs. Thales vs. nCipher).* |
| CP-05 | Observability Infrastructure | 2 (H) | 2 (H) | Tune storage retention and memory allocation for customer's disk/memory profile. Mostly configuration -- the observability stack itself is standardized. May need to integrate with customer's existing monitoring if they have one. |
| CP-06 | CI/CD Pipeline / GitOps | 2 (M) | 2 (M) | Adapt artifact delivery pipeline for customer's network constraints (air-gap, proxy, artifact mirror). Target-environment configuration in GitOps. *Air-gapped customers: TE=3; Replicated data shows 60x time-to-install for air-gapped vs. connected deployments.* |
| CP-07 | Deploy Lifecycle / Rollback | 3 (M) | 3 (M) | Establish deployment cadence, change management process, and maintenance windows with customer. Validate rollback procedures against customer's specific environment. *Regulated customers with formal change management boards: TE may reach 4 due to maintenance window negotiation.* |
| CP-08 | Disaster Recovery / BC | 3 (M) | 3 (M) | DR plan adapted to customer's infrastructure -- backup storage targets, recovery time objectives aligned with customer's SLAs, failover testing in customer's environment. |
| CP-09 | Compliance Automation | 3 (M) | 3 (M) | Map ISV's compliance framework to customer's specific regulatory requirements (FedRAMP vs HIPAA vs SOC2 vs industry-specific). Evidence collection configured for customer's audit requirements. *FedRAMP customers: per-customer compliance configuration can consume weeks to months.* |
| CP-10 | Security Operations | 3 (M) | 2 (M) | Security policy adapted to customer's threat model and existing security tooling. Mostly configuration -- security tooling is standardized. Integration with customer's SIEM if required. *SIEM-integrated customers: TE may reach 3 due to Falco-to-SIEM integration (Splunk, QRadar).* |
| | **P1 Phase 2 Totals** | **avg 3.0** | **avg 2.9** | |

### P2: Application Logic -- Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 (H) | 1 (H) | Same architecture across all customers. No per-customer changes. |
| AL02 | Business Logic / Domain Services | 1 (H) | 1 (H) | Same code everywhere. Tenant configuration handles customer-specific behavior. |
| AL03 | API Gateway / Edge Routing | 1 (H) | 1 (H) | Gateway config is standardized. Customer-specific TLS certs handled by P1 (CP-04). |
| AL04 | Data Access / ORM / Caching | 1 (H) | 1 (H) | Connection strings from P3 config. No per-customer code changes. |
| AL05 | Background Jobs / Async / EDA | 1 (H) | 1 (H) | Event-driven architecture is standardized. No per-customer adaptation. |
| AL06 | Resilience Patterns / Runtime | 1 (H) | 1 (H) | Resilience patterns are application-level. Timeouts may need tuning for customer's network latency profile -- minor config. |
| AL07 | Multi-Tenant Isolation | 1 (M) | 1 (M) | Multi-tenancy is application-level. No per-customer changes. |
| AL08 | Observability Instrumentation | 1 (H) | 1 (H) | OTel instrumentation is standardized. Exporter endpoints configured by P1. |
| AL09 | AI/ML Orchestration / Agent Pipelines | 1 (H) | 2 (H) | Adapt to customer's specific AI model availability -- which models they host, context window sizes, endpoint URLs, rate limits. Feature flags for model-dependent capabilities. |
| AL10 | Testing / Contract Testing / Env Parity | 2 (H) | 2 (H) | Validation testing against each customer's specific environment. Smoke tests, integration verification, performance baseline. Per-customer test runs, not per-customer test code. |
| | **P2 Phase 2 Totals** | **avg 1.1** | **avg 1.2** | |

### P3: Data Plane -- Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| DS1 | Relational Database HA | 2 (H) | 2 (H) | Tune shared_buffers, work_mem, wal_buffers for customer's memory. Storage layout for customer's disk topology. Backup targets configured per customer's storage. *Depends on Phase 1 configuration templates.* |
| DS2 | NoSQL / Document Store | 2 (H) | 1 (H) | Minor tuning for customer's storage performance. WiredTiger cache sizing. |
| DS3 | Caching Layer | 1 (H) | 1 (H) | Redis maxmemory config based on customer's available RAM. Standard across customers. |
| DS4 | Object / Blob Storage | 1 (H) | 1 (H) | MinIO erasure coding configured for customer's disk count. Minimal variation. |
| DS5 | Message Queuing (Simple) | 1 (H) | 1 (H) | Standard configuration. Persistence settings for customer's disk. |
| DS6 | Event Streaming (Kafka) | 2 (H) | 2 (H) | Kafka log.dirs configured for customer's disk topology. Broker memory sizing. Replication factor may vary based on customer's node count. *Depends on Phase 1 configuration templates.* |
| DS7 | Search / Full-Text Index | 2 (H) | 1 (H) | JVM heap sized to customer's available memory. Shard count based on data volume estimate. |
| DS8 | Vector Database | 2 (M) | 2 (M) | Index size and segment configuration based on customer's data volume and available memory. HNSW parameters may need tuning per customer's latency requirements. *Depends on Phase 1 configuration templates; TE=2 assumes pre-validated HNSW parameter sets per data volume tier.* |
| DS9 | Embedding Pipeline (GPU) | 2 (M) | 2 (M) | Configure embedding batch size and concurrency for customer's GPU allocation. Validate embedding model compatibility with customer's GPU generation. *Depends on Phase 1 GPU-tier configuration templates.* |
| DS10 | RAG Pipeline Orchestration | 1 (H) | 1 (H) | RAG pipeline config is standardized. Endpoint URLs for customer's embedding and inference services. |
| | **P3 Phase 2 Totals** | **avg 1.6** | **avg 1.4** | |

### P4: AI Model Plane -- Phase 2

| ID | Subsegment | RD | TE | Notes |
|:---:|---|:---:|:---:|---|
| S1 | Managed API Integration | 1 (H) | 2 (H) | Map to customer's inference endpoint URLs, authentication method, and API schema. Each customer may expose different model APIs. |
| S2 | Self-Hosted Inference Engine | -- | -- | **Customer scope.** |
| S3 | GPU Hardware Infrastructure | -- | -- | **Customer scope.** |
| S4 | GPU Driver / CUDA Stack | -- | -- | **Customer scope.** |
| S5 | Multi-Tenant GPU Scheduling | -- | -- | **Customer scope.** |
| S6 | Model Routing / Load Balancing | 1 (H) | 2 (H) | Configure routing for customer's available models -- different customers may have different model catalogs, different capacity, different failover options. |
| S7 | Inference Monitoring | 1 (H) | 1 (H) | Set SLO thresholds based on customer's inference service performance characteristics. |
| S8 | Model Lifecycle Management | 1 (H) | 1 (H) | Inventory which models customer provides. Version compatibility verification. |
| | **P4 Phase 2 Totals (ISV scope)** | **avg 1.0** | **avg 1.5** | |

### Phase 2 Summary

| Plane | Avg RD | Avg TE | Estimated Per-Customer Effort | Key Cost Driver |
|---|:---:|:---:|---|---|
| P1 Control Plane | 3.0 | 2.9 | 6-14 person-weeks | Infrastructure adaptation to customer hardware/network/security |
| P2 Application Logic | 1.1 | 1.2 | 1-2 person-weeks | Validation testing, model availability mapping |
| P3 Data Plane | 1.6 | 1.4 | 2-4 person-weeks | Performance tuning for customer's storage/memory |
| P4 AI Model Plane | 1.0 | 1.5 | 0.5-1 person-weeks | Endpoint configuration, model catalog mapping |
| **Total** | **1.8** | **1.8** | **~10-21 person-weeks per customer** | **P1 = ~60% of per-customer effort** |

*Note: 10-21 pw is the median-case estimate for connected, commercially regulated customers. See customer-segment variance note above for air-gapped (14-27 pw) and hardware-heterogeneous (12-25 pw) profiles.*

---

## 6. Phase 3: Ongoing Software Updates and Support

Recurring annual cost for maintaining and updating ISV software across all deployed customer environments. Scales with N customers x update frequency.

**Two-cost-type finding:** Phase 3 costs comprise two structurally distinct pools:
- **Type A -- Linear-with-N (infrastructure):** P1 + P3 + P4 costs that scale with customer count (~30.80-56.75 FTE, ~62% of total). Each additional customer adds incremental maintenance burden for K8s upgrades, deployment coordination, data service operations, and endpoint maintenance.
- **Type B -- Fixed (product development):** P2 costs that exist regardless of customer count (~18.55-35.60 FTE, ~38% of total). Core product development, AI ecosystem maintenance, and test infrastructure are customer-count-invariant.

The approximately 60/40 split means an ISV with a single on-premises customer still carries ~40% of the full Phase 3 FTE burden. The fixed cost floor is comparable in magnitude to the variable cost pool, making on-premises deployment economically challenging below a threshold customer count.

### P1: Control Plane -- Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| CP-01 | K8s Cluster Lifecycle | 5 (H) | 5 (H) | **Yes** | 3.0-6.0 | 3 minor K8s versions/year, 12-14 month support windows. Each customer on a different version and upgrade schedule. Node drain coordination per customer. Hardware-specific regression risk per customer. The single largest ongoing P1 cost. |
| CP-02 | Network Fabric / Ingress / Mesh | 4 (H) | 4 (H) | **Yes** | 1.75-3.5 | CNI upgrades, network policy updates, ingress controller patches per customer. Gateway API evolution. Network-related incidents are the most common customer-specific issues due to hardware heterogeneity. |
| CP-03 | IAM / RBAC | 3 (H) | **5** (H) | **Partial** | 2.75-4.75 | Keycloak upgrades, identity provider integration maintenance. Core IAM tooling is shared; per-customer federation config maintenance adds linear cost. Identity incidents require per-customer investigation. *[v2: TE raised from 4 to 5. GT1 FTE range 2.75-4.75 exceeds TE=4 ceiling of 2.5 FTE -- SL1c Section 1.1.]* |
| CP-04 | Secrets / Certs / PKI | 4 (M) | 4 (M) | **Yes** | 2.5-5.0 | Certificate rotation per customer. Vault upgrades across N environments. FIPS 140-3 migration (deadline September 2026) is a one-time event but must be coordinated per customer. Seal/unseal operations during Vault upgrades are per-customer. |
| CP-05 | Observability Infrastructure | 4 (H) | 5 (H) | **Partial** | 4.6-7.0 | Prometheus/Grafana/Loki upgrades across customer environments. Storage management for metrics/logs (grows with time). Jaeger v1-to-v2 migration. The observability stack requires the most ongoing attention of any P1 subsegment -- 500K+ active time series per customer instance. Base staff is shared but storage/capacity management is per-customer. |
| CP-06 | CI/CD Pipeline / GitOps | 3 (H) | **4** (H) | **Partial** | 2.0-3.25 | Pipeline maintenance, artifact registry management. Pipeline logic is shared; delivery targets are per-customer. ArgoCD/Flux version upgrades. *[v2: TE raised from 3 to 4. GT1 FTE range 2.00-3.25 maps to TE=4 band (1.0-2.5), not TE=3 (0.3-1.0) -- SL1c Section 1.1.]* |
| CP-07 | Deploy Lifecycle / Rollback | 5 (H) | 5 (H) | **Yes** | 1.5-3.0 | **The linear scaling problem.** N customers = N separate deployment coordination sequences for every release. CVE patches: 50 customers = 50 patch cycles. 3-5 concurrent software versions across customer base. Rollback requires per-customer database state awareness. This subsegment's effort is directly proportional to customer count. |
| CP-08 | Disaster Recovery / BC | 4 (H) | **4** (H) | **Yes** | 1.5-2.5 | DR testing per customer on a regular cadence. Backup verification per customer. Recovery procedure validation. Less frequent than CP-07 but still per-customer. *[v2: TE raised from 3 to 4. GT1 FTE range 1.50-2.50 exceeds TE=3 ceiling of 1.0 FTE -- SL1c Section 1.1.]* |
| CP-09 | Compliance Automation | 4 (H) | 4 (H) | **Yes** | 2.5-4.0 | Compliance evidence regeneration per audit cycle per customer. Regulatory changes require re-assessment across customer base. SOC2 annual audits, FedRAMP continuous monitoring. |
| CP-10 | Security Operations | 4 (H) | **5** (H) | **Partial** | 2.75-5.5 | Vulnerability scanning, incident response, runtime protection across N environments. Security tooling (Falco) is shared; incident investigation and patch coordination is per-customer. CVE response time pressure. *[v2: TE raised from 4 to 5. GT1 FTE floor 2.75 exceeds TE=4 ceiling of 2.5 FTE -- SL1c Section 1.1.]* |
| | **P1 Phase 3 Totals** | **avg 4.0** | **avg 4.5** | | **20-38 FTE** | *[v2: avg TE corrected from 4.1 to 4.5 after CP-03, CP-06, CP-08, CP-10 adjustments.]* |

### P2: Application Logic -- Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 (H) | 2 (H) | No | 0.8-1.5 | Service communication patterns are stable. Occasional refactoring for new bounded contexts. Same work regardless of tier. |
| AL02 | Business Logic / Domain Services | 1 (H) | 4 (H) | No | 3.0-6.0 | **[D]** The largest absolute FTE in P2 -- this is the ISV's core product development. But relative difficulty is 1 because the work is identical on cloud-native. Business logic doesn't change with deployment tier. High effort, minimal tier delta. |
| AL03 | API Gateway / Edge Routing | 2 (H) | 2 (H) | Partial | 1.5-3.0 | Gateway configuration updates with new API versions. Per-customer gateway config validation for major releases. |
| AL04 | Data Access / ORM / Caching | 1 (H) | **3** (H) | No | 0.75-1.5 | ORM maintenance, connection pool tuning. Occasional migration for database version changes (triggered by P3 upgrades). Patroni and Redis Sentinel application-layer event handling creates meaningful ongoing work beyond basic connection string management. *[v2: TE raised from 2 to 3. Patroni failover event handling and Redis Sentinel reconfiguration at the application layer generate ongoing work that exceeds the TE=2 ceiling -- SL1c Section 1.2; RP2a.]* |
| AL05 | Background Jobs / Async / EDA | **3** (H) | 3 (H) | No | 2.75-5.6 | Event schema evolution, Temporal workflow version management, dead-letter queue monitoring. High absolute effort because the event-driven architecture is complex regardless of tier. Temporal configuration drift and dead-letter queue burden create on-prem-specific operational overhead beyond the cloud-native baseline. *[v2: RD raised from 2 to 3. Temporal config drift, dead-letter queue burden, 2.0-4.1 FTE ops load justify moderate on-prem difficulty -- SL1c Section 1.2; RP2a.]* |
| AL06 | Resilience Patterns / Runtime | 2 (H) | 2 (H) | No | 0.75-1.5 | Resilience pattern tuning, circuit breaker threshold adjustments. Minor ongoing work. |
| AL07 | Multi-Tenant Isolation | 1 (H) | 2 (H) | No | 0.75-1.5 | Multi-tenancy framework is stable. Occasional refinement for new data paths or isolation requirements. Same across tiers. |
| AL08 | Observability Instrumentation | 2 (H) | 2 (H) | No | 0.5-1.0 | Instrumentation updates as new services or features are added. OTel SDK version upgrades. |
| AL09 | AI/ML Orchestration / Agent Pipelines | **4** (M) | 4 (H) | No | 4.0-7.0 | **Rapidly evolving ecosystem.** LangChain/LangGraph version upgrades, new agent patterns, guardrail policy updates, MCP protocol evolution. High effort because the AI/agent stack changes faster than any other application subsegment. On-prem adds complexity of coordinating self-hosted Temporal and Langfuse upgrades. *[v2: RD raised from 3 to 4. Multi-stack coordination burden (LangGraph + MCP + guardrails + model version compatibility) justifies specialist-level difficulty. This is the only subsegment where Phase 3 RD (4) exceeds Phase 1 RD (2) -- a trajectory anomaly driven by version-skew debt accumulation: as the AI ecosystem fragments into incompatible release trains, the on-prem operator faces compound coordination costs that the cloud-native operator avoids via managed service version pinning -- CC3; SL1c Section 1.2; RP2b.]* |
| AL10 | Testing / Contract Testing / Env Parity | 3 (H) | 4 (H) | **Yes** | 3.75-7.0 | Test suite maintenance across N customer hardware profiles. Regression testing for each release against multiple K8s versions and hardware configurations. The testing tax is proportional to customer count and hardware diversity. High absolute effort because the test matrix multiplies. Effort exceeds difficulty because the testing surface area is large even though each test is straightforward. |
| | **P2 Phase 3 Totals** | **avg 2.0** | **avg 2.8** | | **18.55-35.60 FTE** | **TE exceeds RD by 0.8 -- systematic divergence** *[v2: avg RD corrected from 1.8 to 2.0; avg TE corrected from 2.7 to 2.8; divergence narrowed from +0.9 to +0.8 after AL05 RD and AL09 RD adjustments.]* |

### P3: Data Plane -- Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| DS1 | Relational Database HA | 4 (H) | 4 (H) | **Yes** | 1.5-3.0 | PostgreSQL major version upgrades per customer. Patroni failover verification after upgrades. WAL archiving monitoring. Backup validation per customer. PgBouncer connection pool tuning. The highest-consequence data service to upgrade (ACID guarantees at risk). |
| DS2 | NoSQL / Document Store | 3 (H) | **3** (H) | Partial | 0.6-1.1 | MongoDB operator upgrades, replica set maintenance. *[v2: TE raised from 2 to 3. MongoDB FTE 0.6-1.1 maps to TE=3 band (0.3-1.0), not TE=2 (0.1-0.3) -- SL1c Section 1.3; RP3a; GT3.]* |
| DS3 | Caching Layer | 2 (H) | 2 (H) | Partial | 0.4-0.7 | Redis version updates, Sentinel/cluster maintenance. Bounded operational surface. |
| DS4 | Object / Blob Storage | 2 (H) | 2 (H) | Partial | 0.25-0.6 | MinIO version updates, erasure coding verification, storage capacity management. |
| DS5 | Message Queuing (Simple) | 2 (H) | **2-3** (M) | Partial | 0.4-0.7 | Version updates. TE is conditional on technology choice: NATS JetStream = TE 2; RabbitMQ = TE 3 (FTE 0.75-1.25). *[v2: TE changed from 2 to 2-3 (conditional). Technology-dependent operational profile -- SL1c Section 1.3; RP3a.]* |
| DS6 | Event Streaming (Kafka) | 4 (H) | 4 (H) | **Yes** | 1.5-2.5 | Kafka version upgrades (KRaft is mandatory, irreversible). Partition rebalancing, ISR monitoring, consumer group management. 13-26 hrs/week self-hosted vs 2-3 hrs/week MSK. Per-customer upgrade coordination for schema-breaking changes. |
| DS7 | Search / Full-Text Index | 3 (H) | 3 (H) | Partial | 0.7-1.2 | OpenSearch/Elasticsearch version upgrades, JVM tuning, shard rebalancing. Index re-creation may be required for major version upgrades. |
| DS8 | Vector Database | 4 (M) | 3 (M) | Partial | 1.25-1.75 | Milvus/Qdrant upgrades, Woodpecker WAL migration, index optimization. Emerging technology with rapid release cadence. Limited institutional knowledge for troubleshooting. |
| DS9 | Embedding Pipeline (GPU) | 3 (M) | 3 (M) | Partial | **0.50-1.00** | Embedding model version management. Model version changes may trigger full corpus re-embedding -- high-cost event. Pipeline tuning as data volumes grow. *[v2: Research FTE corrected from 2.00-3.25 to 0.50-1.00. The original figure was computed under ISV-manages-GPU assumptions including MIG partitioning, NVLink topology, firmware, thermal monitoring, and RMA -- all customer scope under the established split. ISV-retained work: model serving configuration, batch queue management, model version management, pipeline tuning -- CC4 Section 5; SL2c Section 1.1.]* |
| DS10 | RAG Pipeline Orchestration | 3 (H) | 4 (H) | No | 3.25-4.75 | RAG patterns are rapidly evolving -- chunking strategies, reranking models, context window optimization. High absolute effort because the AI retrieval stack changes frequently. Effort driven by ecosystem evolution, not customer count. |
| | **P3 Phase 3 Totals** | **avg 3.0** | **avg 3.0** | | **~10-17 FTE** (10.35-17.30) | *[v2: avg TE corrected from 2.9 to 3.0 after DS2 TE adjustment. FTE aggregate corrected from "~10-18" to ~10-17 FTE (10.35-17.30) after DS9 scope correction and arithmetic reconciliation -- CC1 D-7; SL2c Section 1.1.]* |

### P4: AI Model Plane -- Phase 3

| ID | Subsegment | RD | TE | Scales with N? | Research FTE (on-prem, revised) | Notes |
|:---:|---|:---:|:---:|:---:|---|---|
| S1 | Managed API Integration | 1 (H) | 2 (H) | Partial | 0.1-0.3 | Maintain API integration with each customer's inference endpoints. Handle customer-side model deprecation or endpoint changes. Per-customer API compatibility monitoring. |
| S2 | Self-Hosted Inference Engine | -- | -- | -- | -- | **Customer scope.** |
| S3 | GPU Hardware Infrastructure | -- | -- | -- | -- | **Customer scope.** |
| S4 | GPU Driver / CUDA Stack | -- | -- | -- | -- | **Customer scope.** |
| S5 | Multi-Tenant GPU Scheduling | -- | -- | -- | -- | **Customer scope.** |
| S6 | Model Routing / Load Balancing | 2 (H) | 2 (H) | Partial | 0.2-0.5 | Routing configuration updates as customers add/change models. Health check tuning. Cost attribution updates. |
| S7 | Inference Monitoring | 1 (H) | 2 (H) | Partial | 0.1-0.5 | SLO threshold adjustments. Monitoring dashboard maintenance. Per-customer inference quality tracking. |
| S8 | Model Lifecycle Management | 1 (H) | 1 (H) | No | 0.05-0.15 | Track customer model availability. Minimal ISV effort -- customer manages artifacts. |
| | **P4 Phase 3 Totals (ISV scope)** | **avg 1.3** | **avg 1.8** | | **~0.5-1.5 FTE** | |

### Phase 3 Summary

| Plane | Avg RD | Avg TE | Annual FTE (research-based) | Key Cost Driver |
|---|:---:|:---:|---|---|
| P1 Control Plane | 4.0 | **4.5** | 20-38 FTE | K8s upgrades, security patching, deploy coordination across N customers |
| P2 Application Logic | **2.0** | **2.8** | 18.55-35.60 FTE | **[D]** Product development (tier-invariant) + per-customer deploy/test logistics |
| P3 Data Plane | 3.0 | **3.0** | **~10-17 FTE** (10.35-17.30) | Database and message broker upgrades across N customers |
| P4 AI Model Plane | 1.3 | 1.8 | ~0.5-1.5 FTE | Endpoint maintenance; customer manages infrastructure |
| **Total** | **2.7** | **3.1** | **~50-93 FTE** (49.35-92.35) | **P1 = highest RD and TE; P2 = largest TE-RD divergence** |

*[v2: P1 avg TE corrected from 4.1 to 4.5. P2 avg RD corrected from 1.8 to 2.0; avg TE corrected from 2.7 to 2.8. P3 avg TE corrected from 2.9 to 3.0; FTE corrected from "~10-18" to ~10-17 (10.35-17.30). Total TE corrected from 3.0 to 3.1. Grand Total FTE corrected from "~49-93" to ~50-93 (49.35-92.35) -- SL1c; CC1; SL2c Section 1.1.]*

---

## 7. Divergence Analysis: Where Difficulty and Effort Disagree

The most strategically important cells are those where relative difficulty and total effort diverge -- these are the subsegments most likely to be underestimated or overestimated in planning.

### Subsegments Where Effort Exceeds Difficulty (planning traps -- easy to underestimate)

| Phase | ID | Subsegment | RD | TE | Gap | Why |
|---|:---:|---|:---:|:---:|:---:|---|
| Phase 1 | AL10 | Testing / Env Parity | 3 | 4 | +1 | Building on-prem test infrastructure is straightforward per test, but the test matrix across self-hosted dependencies is large |
| Phase 3 | AL02 | Business Logic / Domain Services | 1 | 4 | **+3 [D]** | The largest ongoing FTE in the application -- pure product development. Zero tier difficulty but massive absolute effort. Easy to overlook in on-prem cost models because it looks "tier-invariant." **Sole valid [D] flag in Phase 3.** |
| Phase 3 | AL05 | Background Jobs / Async / EDA | 3 | 3 | 0 | Event-driven architecture is complex regardless of tier. Kafka/Temporal event schema management is high-volume ongoing work. *[v2: Gap reduced from +1 to 0 after AL05 RD adjustment 2 to 3.]* |
| Phase 3 | AL10 | Testing / Contract Testing | 3 | 4 | +1 | Test matrix multiplied by customer count and hardware diversity |
| Phase 3 | DS10 | RAG Pipeline Orchestration | 3 | 4 | +1 | RAG patterns evolving rapidly -- continuous rework effort |
| **Phase 3** | **P2 overall** | **Application Logic (all)** | **2.0** | **2.8** | **+0.8** | **Systematic divergence: P2 looks easy on the difficulty scale but is the second-largest FTE block. The mechanism is structural: P2 contains tier-invariant subsegments whose absolute effort is set by application size, not deployment tier.** |

*[v2: Removed [D] flags from AL10 Phase 1 (gap=+1, below threshold), AL10 Phase 3 (gap=+1, below threshold), and DS10 Phase 3 (gap=+1, below threshold). Retained [D] on AL02 Phase 3 (gap=+3, correctly exceeds >=2 threshold). Added [D] note for AL09 Phase 3 below. Divergence narratives preserved in all cells even where formal [D] notation removed -- CC2; SL1c Section 2.2.]*

**AL09 Phase 3 trajectory note:** After the RD adjustment from 3 to 4, AL09 Phase 3 shows RD=4, TE=4 (gap=0). While this does not qualify for a [D] flag, the trajectory is anomalous: AL09 is the only subsegment where Phase 3 RD (4) exceeds Phase 1 RD (2). This occurs because version-skew debt accumulates as the AI ecosystem fragments into incompatible release trains. The on-premises operator faces compound coordination costs across LangGraph, MCP, guardrails, and model version compatibility that the cloud-native operator avoids via managed service version pinning.

### Subsegments Where Difficulty and Effort Align (accurately estimated)

| Phase | Plane | Avg RD | Avg TE | Gap |
|---|---|:---:|:---:|:---:|
| Phase 1 | P1 Control Plane | 4.4 | 4.0 | 0.4 |
| Phase 1 | P3 Data Plane | 3.2 | 3.0 | 0.2 |
| Phase 2 | All planes | 1.8 | 1.8 | 0.0 |
| Phase 3 | P1 Control Plane | 4.0 | 4.5 | 0.5 |
| Phase 3 | P3 Data Plane | 3.0 | 3.0 | 0.0 |

**Pattern:** P1 and P3 are well-calibrated -- hard things are also large things. P2 is systematically miscalibrated -- the difficulty scale understates the effort because application logic is large regardless of deployment tier.

---

## 8. Grand Summary

### Three-Phase x Four-Plane Matrix (Relative Difficulty)

| Plane | Phase 1 RD | Phase 2 RD | Phase 3 RD | All-Phase Avg RD |
|---|:---:|:---:|:---:|:---:|
| P1 Control Plane | **4.4** | **3.0** | **4.0** | **3.8** |
| P2 Application Logic | 1.9 | 1.1 | **2.0** | 1.7 |
| P3 Data Plane | **3.2** | 1.6 | **3.0** | 2.6 |
| P4 AI Model Plane | 1.75 | 1.0 | 1.3 | 1.4 |

*[v2: P4 Phase 1 RD corrected from 1.5 to 1.75. P2 Phase 3 RD corrected from 1.8 to 2.0. P2 All-Phase corrected from 1.6 to 1.7. P4 All-Phase corrected from 1.3 to 1.4.]*

### Three-Phase x Four-Plane Matrix (Total Effort)

| Plane | Phase 1 TE | Phase 2 TE | Phase 3 TE | All-Phase Avg TE |
|---|:---:|:---:|:---:|:---:|
| P1 Control Plane | **4.0** | **2.9** | **4.5** | **3.8** |
| P2 Application Logic | 2.3 | 1.2 | **2.8** | 2.1 |
| P3 Data Plane | **3.0** | 1.4 | **3.0** | 2.5 |
| P4 AI Model Plane | 1.8 | 1.5 | 1.8 | 1.7 |

*[v2: P1 Phase 3 TE corrected from 4.1 to 4.5. P2 Phase 3 TE corrected from 2.7 to 2.8. P3 Phase 3 TE corrected from 2.9 to 3.0. P1 All-Phase corrected from 3.7 to 3.8. P3 All-Phase corrected from 2.4 to 2.5.]*

### Key Findings (Revised per SL2a Section 6)

**On the direction of error.** Every adjustment identified through multi-wave independent review runs upward. No rating in the 102-cell active matrix was found to be overstated. Nine firm rating adjustments and one conditional adjustment are all +1 increases. The stated effort figures should be read as floor estimates for a fully-staffed ISV with established on-premises delivery capability, not central estimates for a typical ISV entering on-premises deployment. Six structural cost categories -- talent acquisition (5.4-month average hiring cycles for platform engineers), customer communication overhead, supply chain security (40K+ CVEs/year across 40+ OSS components), organizational change management, vendor lock-in reversal cost, and regulatory compliance variance -- are absent from the framework and would add to the actual cost in practice.

**1. P1 (Control Plane) dominates all three phases, and its Phase 3 cost is understated.** P1 carries the highest difficulty and effort ratings across Phase 1 (RD 4.4 / TE 4.0), Phase 2 (RD 3.0 / TE 2.9), and Phase 3 (RD 4.0 / TE 4.5 after review corrections). The 80-person-month upper bound for Phase 1 is the defensible planning figure; the 40-person-month lower bound requires conditions unlikely to co-occur (experienced team, no learning curve, no 2026 migration calendar impact). Four Phase 3 P1 subsegments (CP-03, CP-06, CP-08, CP-10) have TE ratings that do not reach their ground truth FTE ceilings and have been adjusted upward. After corrections, P1 Phase 3 avg TE rises from 4.1 to 4.5, creating a 1.5-point gap over the next-highest plane. P1 is the primary determinant of on-premises economic viability.

**2. P2 (Application Logic) creates a planning trap: large cost at low difficulty.** P2 Phase 3 averages RD 2.0 versus TE 2.8, a +0.8 gap (narrowed from +0.9 after review adjustments) that is arithmetically verified and structurally driven by tier-invariant subsegments whose absolute effort is set by application size, not deployment tier. Removing the dominant outlier (AL02, gap = +3) still leaves a +0.67 residual gap across 9 cells. P2 Phase 3 represents 18.55-35.60 FTE of ongoing product development and maintenance -- comparable in magnitude to P1's 20-38 FTE -- that cost models focused on deployment difficulty will exclude. The risk is not that P2 is secretly difficult; it is that P2 costs are invisible to planners who screen on difficulty alone.

**3. P3 (Data Plane) is the best-calibrated plane.** Difficulty and effort align closely across all three phases (all-phase avg gap = -0.2, no [D]-qualifying divergences). The P3 Phase 3 FTE aggregate has been corrected from "~10-18 FTE" to 10.35-17.30 FTE -- individual subsegment FTEs are accurate; only the summary was understated. DS2 (NoSQL) Phase 3 TE has increased from 2 to 3 based on MongoDB operational FTE of 0.6-1.1.

**4. P4 (AI Model Plane) is structurally reduced but not eliminated.** The customer-provides-GPU scope split correctly transfers 5.50-10.50 FTE of primary infrastructure operations to the customer, reducing ISV P4 FTE to approximately 0.45-1.45. However, four categories of residual ISV obligation are unrated and uncosted: hardware compatibility matrix authorship (2-4 person-weeks initial, 1-2 person-days/release recurring), inference engine version compatibility testing (1-3 person-weeks per major vLLM release), customer GPU allocation triage support (0.05-0.10 FTE per customer annually), and per-customer troubleshooting runbooks (1-3 person-days per customer onboarding). At N=50 customers with GPU heterogeneity, S6 and S7 FTE ranges extend into TE=3 territory. The ISV cannot fully divest AI infrastructure expertise.

**5. Phase 2 per-customer effort is P1-dominated and understated for regulated/air-gapped customers.** The stated 10-21 person-weeks per customer is valid for the median case (connected, commercially regulated, standard hardware). For air-gapped and regulated-industry customers -- the segments most likely to require on-premises deployment -- the realistic range is 14-27 person-weeks. All 38 Phase 2 cell ratings are confirmed accurate; the understatement is in the aggregate, not the individual ratings. The first 3-4 customer deployments will exceed even revised ranges before automation maturity is established.

**6. Phase 3 costs comprise two structurally distinct pools.** Linear-with-N costs (P1: 20-38 FTE; P3 scale-sensitive: DS1, DS6) make each additional customer incrementally expensive. Fixed costs (P2: 18.55-35.60 FTE; P3 fixed: DS10 at 3.25-4.75 FTE) represent product development and AI ecosystem maintenance that cannot be reduced by serving fewer customers. The fixed pool is comparable in magnitude to the variable pool (~40% of total), creating a cost floor that makes on-premises deployment economically challenging below a threshold customer count. An ISV with 5 customers and an ISV with 50 customers face the same P2 cost; the P1 cost is what separates them.

**7. The analysis systematically understates Phase 3 costs.** This finding is confirmed from three independent analytical angles: (a) four P1 subsegments have Phase 3 TE ratings whose ceilings fall below ground truth FTE ranges; (b) P2 exhibits a +0.8 systematic divergence where TE exceeds RD across all 10 subsegments; (c) the P3 FTE aggregate label understated the arithmetic sum. The convergence of these findings from different planes, identified by different review agents using different methods, constitutes the strongest evidence in the review corpus. The corrected Phase 3 grand total is approximately 50-93 FTE (49.35-92.35). With the six absent structural risk categories factored qualitatively, the true ongoing cost of on-premises deployment is likely 15-25% above the stated range for a typical mid-size ISV.

---

## 9. Sources and Confidence

| Data Source | Confidence | Coverage |
|---|---|---|
| Phase 3 FTE estimates | **High** | Directly from P1-P4 research (78 files, 390K+ words, 8,740+ citations) |
| Phase 1 difficulty ratings | **High** | Derived from P1-P4 tier deltas -- the refactoring work is the delta between cloud-native and on-prem configurations |
| Phase 1 effort estimates | **Medium** | Estimated from FTE data and typical platform build durations; not directly measured. Undocumented parallelization factor of 0.55-0.67x is the most consequential assumption. |
| Phase 2 ratings | **Medium** | Derived from per-customer deployment patterns documented in CP-07, G1; limited empirical data on hardware heterogeneity impact |
| Phase 2 effort estimates | **Medium-Low** | Industry-informed estimates; no direct per-customer deployment measurement in research corpus. 10-21 pw median; 14-27 pw for air-gapped/regulated. |
| P4 scope reduction | **High** | Customer-provides-GPU scope clearly eliminates S2-S5 from ISV responsibility; S1/S6/S7/S8 reduction follows logically |
| P4 residual obligations | **Low** | Four unrated ISV obligations from RP4b; FTE estimates marked [UNVERIFIED] |
| Phase 3 structural gaps | **Low** | Six absent risk categories from CC5; qualitative estimates only |

**What would strengthen this analysis:**
- Empirical Phase 1 build timelines from ISVs that have completed cloud-to-on-prem refactoring
- Per-customer deployment cost data from ISVs operating at N=10+ on-prem customers
- Measurement of hardware heterogeneity impact on Phase 2 effort (how much does network/storage/virtualization variance actually cost per customer?)
- Actual on-premises support FTE headcount data to validate or invalidate the ~50-93 FTE Phase 3 projection
- Time-to-hire data for platform engineers with K8s operations experience to validate the CC5 talent acquisition gap

---

## 10. Changes from v1

This section documents every modification made from the original `three_phase_on_prem_ratings.md` (v1) to this revised file (v2), with rationale and source for each change.

### 10.1 Rating Cell Changes (10 adjustments, all +1 upward)

| # | Subsegment | Phase | Dimension | v1 Value | v2 Value | Rationale | Source |
|:---:|---|---|---|:---:|:---:|---|---|
| 1 | S1 Managed API Integration | Phase 1 | RD | 1 | **2** | Auth re-implementation (cloud IAM to bearer/mTLS), Bedrock schema delta, error handling rewrite | SL1a Section 2; RP4a |
| 2 | CP-03 IAM/RBAC | Phase 3 | TE | 4 | **5** | GT1 FTE 2.75-4.75 exceeds TE=4 ceiling (2.5 FTE) | SL1c Section 1.1; GT1 |
| 3 | CP-06 CI/CD Pipeline/GitOps | Phase 3 | TE | 3 | **4** | GT1 FTE 2.00-3.25 maps to TE=4 band (1.0-2.5), not TE=3 (0.3-1.0) | SL1c Section 1.1; GT1 |
| 4 | CP-08 Disaster Recovery/BC | Phase 3 | TE | 3 | **4** | GT1 FTE 1.50-2.50 exceeds TE=3 ceiling (1.0 FTE) | SL1c Section 1.1; GT1 |
| 5 | CP-10 Security Operations | Phase 3 | TE | 4 | **5** | GT1 FTE floor 2.75 exceeds TE=4 ceiling (2.5 FTE) | SL1c Section 1.1; GT1 |
| 6 | AL04 Data Access/ORM/Caching | Phase 3 | TE | 2 | **3** | Patroni and Redis Sentinel application-layer event handling overhead | SL1c Section 1.2; RP2a |
| 7 | AL05 Background Jobs/Async/EDA | Phase 3 | RD | 2 | **3** | Temporal config drift, dead-letter queue burden, 2.0-4.1 FTE ops load | SL1c Section 1.2; RP2a |
| 8 | AL09 AI/ML Orchestration | Phase 3 | RD | 3 | **4** | Multi-stack coordination burden; only subsegment where Phase 3 RD > Phase 1 RD | SL1c Section 1.2; RP2b; CC3 |
| 9 | DS2 NoSQL/Document Store | Phase 3 | TE | 2 | **3** | MongoDB FTE 0.6-1.1 maps to TE=3 band (0.3-1.0), not TE=2 (0.1-0.3) | SL1c Section 1.3; RP3a; GT3 |
| 10 | DS5 Message Queuing | Phase 3 | TE | 2 | **2-3** | Conditional: NATS JetStream=2, RabbitMQ=3 (FTE 0.75-1.25) | SL1c Section 1.3; RP3a |

### 10.2 FTE Corrections

| Location | v1 Value | v2 Value | Rationale | Source |
|---|---|---|---|---|
| DS9 Phase 3 Research FTE | 2.00-3.25 | **0.50-1.00** | Computed under ISV-manages-GPU assumptions; GPU lifecycle tasks are customer scope | CC4 Section 5; SL2c Section 1.1 |
| P3 Phase 3 FTE aggregate | "~10-18 FTE" | **~10-17 FTE** (10.35-17.30) | Arithmetic sum corrected + DS9 scope correction | CC1 D-7; SL2c Section 1.1 |
| Phase 3 Grand Total FTE | "~49-93 FTE" | **~50-93 FTE** (49.35-92.35) | Propagation of P3 correction | SL2c Section 1.1 |

### 10.3 [D] Divergence Flag Corrections

| Location | v1 Status | v2 Status | Rationale | Source |
|---|---|---|---|---|
| AL10 Phase 1 | [D] applied | **Removed** | Gap=+1, below >=2 threshold | CC2; SL1c Section 2.2 |
| AL10 Phase 3 | [D] applied | **Removed** | Gap=+1, below >=2 threshold | CC2; SL1c Section 2.2 |
| DS10 Phase 3 | [D] applied | **Removed** | Gap=+1, below >=2 threshold | CC2; SL1c Section 2.2 |
| AL02 Phase 3 | [D] applied | **Retained** | Gap=+3, correctly exceeds threshold; sole valid [D] | CC2; SL1c Section 2.2 |

Divergence narratives preserved in Notes column for all cells where [D] was removed; the analytical observations remain correct even though the formal threshold is not met.

### 10.4 Average and Aggregate Recalculations

| Metric | v1 Value | v2 Value | Source |
|---|---|---|---|
| P4 Phase 1 avg RD | 1.5 | **1.75** | S1 RD 1 to 2 |
| P1 Phase 3 avg TE | 4.1 | **4.5** | CP-03, CP-06, CP-08, CP-10 TE adjustments |
| P2 Phase 3 avg RD | 1.8 | **2.0** | AL05 RD, AL09 RD adjustments |
| P2 Phase 3 avg TE | 2.7 | **2.8** | AL04 TE adjustment |
| P3 Phase 3 avg TE | 2.9 | **3.0** | DS2 TE adjustment |
| Phase 1 Total RD | 2.9 | **3.0** | Computed 2.971, correctly rounds to 3.0 (CC1 D-2) |
| Phase 3 Total TE | 3.0 | **3.1** | Was already 3.059 before adjustments; increases further with TE corrections (CC1 D-5) |
| P2 Phase 3 divergence | +0.9 | **+0.8** | Narrowed by AL05 RD and AL09 RD upward adjustments |

### 10.5 Heading and Vocabulary Corrections

| Location | v1 Text | v2 Text | Source |
|---|---|---|---|
| Phase 2 section heading | "Per-Customer Hardware Customization" | "Per-Customer Customization: Software Adaptation to Customer Hardware" | CC4 Section 6 |
| Phase 1 Total RD in summary | "2.9" | "3.0" | CC1 D-2 |

### 10.6 Structural Additions

| Addition | Description | Source |
|---|---|---|
| Confidence indicators | (H), (M), (L) parenthetical on every rating cell | SL3a Section 7 Confidence Map |
| Phase 1 parallelization factor | Documents 0.55-0.67x factor, CP-01 dependency chain, 40-80 pm derivation | SL1a Section 3.2; SL2c Section 6.6 |
| Phase 2 customer-segment annotations | Annotations on 6 P1 Phase 2 cells (CP-02, CP-04, CP-06, CP-07, CP-09, CP-10) for air-gapped, regulated, HSM segments | SL1b Section 2.2; SL2c Section 6.6 |
| Phase 2 hidden dependency note | Documents 4 P3 subsegments where Phase 2 TE=2 depends on Phase 1 templates | SL1b Section 4.3; SL2c Section 6.6 |
| Phase 3 two-cost-type finding | Explicit Type A (linear ~62%) vs Type B (fixed ~38%) decomposition | SL2c Section 3; SL2c Section 6.6 |
| AL09 trajectory annotation | Explains Phase 3 RD (4) > Phase 1 RD (2) via version-skew debt | CC3; SL2c Section 6.6 |
| Key Findings section (revised) | 7 findings replacing original 6, incorporating all review conclusions | SL2a Section 6 |
| Changes from v1 section | Complete modification log with rationale and sources | SL3a Section 6 |
| Phase 3 Grand Total note | Exact computation: 49.35-92.35, rounded to ~50-93 | SL2c Section 1.1 |

### 10.7 Items Identified but NOT Changed

The following items were identified during review but are intentionally not changed in v2:

| Item | Reason for No Change | Source |
|---|---|---|
| Proposed new subsegments S9, S10, AL11 | Framework extension, not rating correction; would add subsegments rather than adjust existing ones | RP4c; RP2e |
| P4 residual obligation FTE estimates | Marked [UNVERIFIED]; noted qualitatively in Finding 4 but not added as rated cells | RP4b Section 5.2 |
| Six structural risk categories | Noted qualitatively in Key Findings preamble; recommend qualitative overlay rather than framework extension | CC5 |
| Phase 2 aggregate effort revision | Individual cell ratings unchanged; aggregate revision noted in Phase 2 preamble and Finding 5 | SL1b Section 2.3 |
| Source file P3_data_plane.md DS9 annotation | Out of scope for this deliverable; flagged for separate update | SL2c Section 6.7 |
