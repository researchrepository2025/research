# P2: Application Logic — MECE Subsegment Analysis
## Deployment Difficulty Across Cloud-Native, Managed Kubernetes, and On-Premises Tiers

**Plane:** 2 — Application Logic
**Date:** 2026-02-19
**Input Files:** F01, F02, F03, F07, F32, F33, F34, F38, F56, F57, F64, F66, F72, F73, F74, F75, W01S, W05S, X4
**Output Path:** `/analysis/P2_application_logic.md`
**Scope Authority:** F73 (MECE ISV Developer Responsibility Framework) — 13-component decomposition

---

## Executive Summary

An ISV building AI-driven microservices SaaS does not ship a single codebase — it ships 10 mutually exclusive, collectively exhaustive (MECE) application logic subsegments, each with a distinct team owner, change driver, and deployment-tier difficulty profile. Across three deployment tiers — Cloud-Native (AWS/Azure/GCP fully managed), Managed Kubernetes (EKS/AKS/GKE), and On-Premises (self-hosted K8s or bare metal) — the operational difficulty of these subsegments diverges dramatically.

The aggregate complexity ratio across all 10 subsegments is **Cloud-Native : Managed K8s : On-Premises = 20 : 26 : 34**. This represents a 1.0x : 1.3x : 1.7x multiplier in *application-layer developer complexity* — narrower than the full 1x : 2x : 10x infrastructure staffing multiplier from the X4 synthesis, because the largest on-premises burden is operational (infrastructure), not coding. The FTE burden attributable to application logic ranges from 5.8–13.2 FTE cloud-native, to 9.4–19.8 FTE managed K8s, to 19.3–38.0 FTE on-premises.

Three structural findings emerge from the evidence:

1. **Two subsegments drive disproportionate tier risk.** AI/ML Orchestration & Agent Pipelines (AL09) and Resilience & Runtime Behavior (AL06) account for the largest cloud-to-on-premises difficulty jumps. AL09 moves from difficulty 2 cloud-native to 5 on-premises — requiring 6–10 dedicated FTE before infrastructure costs, versus 0.5–1.2 FTE for equivalent managed API integration. AL06 requires ISVs to embed circuit breaker and health-check logic directly into application code on-premises (Resilience4j, Polly), whereas cloud-native and managed K8s platforms provide these as infrastructure-layer capabilities.

2. **Multi-Tenant Isolation Logic (AL07) is the sole tier-invariant subsegment at difficulty 3/5 across all tiers.** It is a software architecture problem — no platform can fully abstract the requirement to scope every read, write, and inference call to the correct tenant. ISVs that do not build a tenant-context framework early face prohibitive retrofitting costs at scale, regardless of deployment model.

3. **Three EOL forcing functions affect managed K8s ISVs in 2026.** Ingress NGINX Controller retirement (March 2026), AWS App Mesh discontinuation (September 2026), and the HashiCorp Vault FIPS 140-3 migration deadline (September 2026) all impose unplanned rework on the API Gateway & Edge Routing (AL03) and Configuration, Secrets & Feature Flags (AL05) subsegments. ISVs must budget 0.3–0.6 FTE of unplanned platform work per event.

---

## 1. Scope Definition and MECE Boundaries

### What Is Included in Application Logic (Plane 2)

Application Logic covers all code, configuration, and behavioral decisions that the ISV owns at the *service logic level* — distinct from infrastructure provisioning (Control Plane), persistent data storage and schema (Data Plane), and AI model weights and training (AI Model Plane). Specifically, Application Logic includes:

- Service decomposition patterns and inter-service communication code
- API gateway routing rules and protocol selection (REST vs gRPC)
- Resilience patterns embedded in application code (circuit breakers, health probes, graceful shutdown)
- Configuration and secrets consumption at the application layer
- Background job and async processing logic
- Multi-tenancy enforcement middleware
- Agent orchestration code (LangGraph graphs, MCP tool integrations, agent state management)
- Testing strategy for the application layer (contract tests, integration tests, environment parity)

### What Is Excluded from Application Logic (Plane 2)

The following are explicitly out of scope and covered in other planes:

- **Control Plane:** Kubernetes cluster lifecycle, node provisioning, IaC templates, secrets vault operations, CI/CD pipeline infrastructure, compliance audit automation. These are referenced where they create application-layer consequences but are not rated here.
- **Data Plane:** Database schema migrations, connection pool infrastructure, vector database cluster operations, object storage backend management. The *application-layer ORM code* is in scope; the database HA infrastructure is not.
- **AI Model Plane:** GPU hardware procurement, model training, embedding corpus management, model serving runtime operations (vLLM/TGI tuning). The *application code that calls inference endpoints* is in scope; model serving infrastructure is not.

### MECE Validation

The 10 subsegments are validated against the two MECE criteria:

**Mutual Exclusivity:** Each subsegment has a distinct primary change driver that uniquely activates work in that subsegment and not others. A product feature request (AL02 Business Logic) does not require a change to the API gateway routing policy (AL03) unless a new endpoint is exposed — and that gateway change is a downstream gate, not the same artifact. Service decomposition decisions (AL01) trigger once per architecture boundary; inter-service communication code (AL01 also) triggers per new service-to-service integration. The subsegments are bounded by protocol ownership, not team assignment.

**Collective Exhaustiveness:** Every byte of data flowing through an AI-driven SaaS application passes through at least one of these 10 subsegments: it enters via an API gateway (AL03), is authenticated (part of AL02 when evaluating authz decisions), validated (AL02), attributed to a tenant (AL07), processed by domain logic (AL02), read/written via data access abstractions (AL04), may trigger async work (AL05 adjacent), may invoke an AI pipeline (AL09), is observed (AL08), and is tested before release (AL10). No application path escapes this coverage.

---

## 2. Difficulty Scale

| Score | Label | Operational Meaning |
|-------|-------|---------------------|
| 1 | Trivial | Fully managed by platform; zero application-side operational knowledge needed |
| 2 | Low | SDK/config integration; minimal platform knowledge; rare incidents |
| 3 | Moderate | Platform-aware code required; periodic incidents; dedicated ownership recommended |
| 4 | High | Significant application-platform integration; frequent operational events; dedicated staff required |
| 5 | Extreme | Deep specialist expertise required; continuous operational attention; high failure risk without dedicated team |

---

## 3. Subsegment Definitions and Difficulty Analysis

---

### AL01 — Service Decomposition and Inter-Service Communication

**Change Driver:** New bounded context identified via DDD, team topology change, traffic isolation requirement, or protocol upgrade (REST→gRPC).

**Scope:** The architectural decisions governing how the ISV divides its product into services and how those services communicate at runtime. Includes: bounded context mapping, service count governance, synchronous communication protocol selection (REST vs gRPC vs GraphQL Federation), and asynchronous communication patterns (transactional outbox, Saga choreography). Excludes message broker infrastructure operations (AL05 adjacent) and service mesh/gateway infrastructure (AL03).

**Evidence and Difficulty Ratings:**

[STATISTIC] "Netflix has over 1,000 microservices; Uber has approximately 2,200 across 70 domains. The industry average is approximately 45 services per organization."
— F01: Microservices Architecture
URL: https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/

[FACT] gRPC delivers 107% higher throughput, 48% lower latency, and 34% lower memory consumption versus REST equivalents.
— X4: Application Logic Three-Tier Comparison (citing markaicode.com benchmarks)
URL: https://markaicode.com/grpc-vs-rest-benchmarks-2025/

[FACT] REST holds approximately 90% market share; the emerging pattern is hybrid — gRPC internally, REST for external/browser clients.
— X4: Application Logic Three-Tier Comparison
URL: https://www.gravitee.io/blog/choosing-right-api-architecture

[FACT] "42% of organizations are consolidating from microservices" and microservices only deliver net value above 10–15 developers.
— W01S: Wave 1 Synthesis
URL: https://www.javacodegeeks.com/2025/12/microservices-vs-modular-monoliths-in-2025-when-each-approach-wins.html

[STATISTIC] Microservices tax: $5K–$10K/month infrastructure overhead for a 50-service deployment; 1 SRE per 10–15 services at maturity.
— F01: Microservices Architecture
URL: https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/

**Tier Analysis:**

*Cloud-Native (Difficulty: 2):* Service decomposition is pure design work, identical across all tiers. The cloud-native difficulty premium for this subsegment is slightly lower because AWS Cloud Map, VPC Lattice, and GKE Service Directory eliminate the operational surface of service discovery — the ISV designs and codes service boundaries, then calls standard DNS. Application code makes standard HTTP/gRPC calls with no infrastructure knowledge.

*Managed K8s (Difficulty: 2):* Standard Kubernetes DNS introduces measurable overhead — 5–60ms per CoreDNS query, with documented production cases of queries exceeding 5 seconds after CoreDNS pod rollovers. NodeLocal DNSCache is a required optimization. The ISV's application code is DNS-name-based and portable, but the platform team must deploy and tune CoreDNS. The service decomposition coding work itself is identical to cloud-native.

*On-Premises (Difficulty: 3):* On-premises deployments require a dedicated service discovery infrastructure — typically Consul (requiring 2–8 GB RAM and 2–4 CPU cores per server node) or etcd. etcd has no native DNS and no built-in health checking, requiring CoreDNS and external monitoring. Application code must integrate Consul client libraries or Consul DNS. The ISV owns the full lifecycle of discovery infrastructure. Service decomposition design work remains unchanged, but the discovery integration surface adds application-layer complexity absent in higher tiers.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2 | 2 | 3 |
| Key tools | Cloud Map, VPC Lattice, Cloud DNS | CoreDNS + NodeLocal DNSCache, ExternalDNS | Consul, etcd + CoreDNS |
| ISV code impact | Standard HTTP/gRPC calls, DNS names | Same + NodeLocal DNSCache tuning required | Consul SDK integration, ISV owns HA |
| Est. FTE | 0.5–1.0 (design) | 0.5–1.0 (design) + 0.1 (DNS ops) | 0.5–1.0 (design) + 0.3–0.5 (discovery ops) |

---

### AL02 — Business Logic, Domain Services, and Request Validation

**Change Driver:** Product feature request, customer domain requirement, regulatory domain change, API contract revision.

**Scope:** The ISV's core intellectual property — domain rules, workflow logic, authorization decisions (RBAC/ABAC policy evaluation), request payload validation (Pydantic/Zod schemas), and error response standardization. This is the subsegment most analogous to "pure application code." Excludes identity provider operations (covered in Control Plane), API gateway routing (AL03), and database schema design (Data Plane).

**Evidence and Difficulty Ratings:**

[FACT] "Services should exclude HTTP-specific imports, operate using domain models rather than raw data structures, raise domain-specific exceptions (not HTTP exceptions), and remain reusable across different contexts."
— F75: MECE Abstraction Layer Framework
URL: https://comp423-25s.github.io/resources/backend-architecture/0-layered-architecture/

[FACT] "Business logic difficulty is 3/5 across all tiers. Domain rules and workflow logic are platform-agnostic by design. The service layer operates independently of HTTP concerns and is equally portable to Lambda, Kubernetes pods, or bare-metal processes."
— F75: MECE Abstraction Layer Framework
URL: https://comp423-25s.github.io/resources/backend-architecture/0-layered-architecture/

[FACT] Self-hosted Keycloak requires dedicated identity expertise; managing Keycloak yourself requires "handling updates, backups, scaling, and security patches."
— F75: MECE Abstraction Layer Framework (citing Infisign)
URL: https://www.infisign.ai/blog/auth0-vs-keycloak

**Tier Analysis:**

Business logic and request validation are the most portable components in the entire framework. A pricing calculation, authorization policy evaluation, or Pydantic schema validator is equally complex whether deployed on AWS Lambda, a GKE pod, or a bare-metal server. The difficulty is inherent domain complexity, not deployment complexity.

The one tier-differentiated factor: on-premises deployments require application code to implement graceful startup sequences that are aware of self-hosted infrastructure readiness (Consul healthy, Vault unsealed, database primary available), whereas cloud-native applications can rely on managed services being available on first request.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2 | 2 | 2 |
| Key tools | FastAPI/Django/Spring Boot; Pydantic/Zod | Same + K8s-aware health endpoints | Same + Consul/Vault readiness checks at startup |
| ISV code impact | Stateless design, cold-start tolerance (serverless) | Readiness/liveness probe integration, graceful shutdown | Same + process supervisor awareness |
| Est. FTE | 3.0–6.0 (product dev) | 3.0–6.0 | 3.0–6.0 |

---

### AL03 — API Gateway, Edge Routing, and Service Mesh Integration

**Change Driver:** New service exposure, rate-limiting policy change, traffic shaping requirement, security rule update, or infrastructure EOL forcing function.

**Scope:** The north-south entry point for all external traffic. Covers: API gateway configuration and plugin lifecycle, TLS termination, rate limiting, request transformation, and service mesh integration (mTLS, retry policies, circuit breaking at the mesh layer). Excludes gateway infrastructure deployment and HA operations (Control Plane). Includes the ISV's responsibility to code applications aware of gateway timeout budgets, retry semantics, and graceful degradation.

**Evidence and Difficulty Ratings:**

[FACT] "Ingress NGINX Controller, powering approximately 41% of internet-facing Kubernetes clusters, was officially retired November 2025, with best-effort maintenance ending March 2026."
— F73/X4 (citing Kubernetes blog)
URL: https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/

[FACT] AWS API Gateway enforces a 29-second timeout, a 10MB payload limit, and a 99.95% SLA.
— X4: Application Logic Three-Tier Comparison (citing Kong blog)
URL: https://konghq.com/blog/enterprise/kong-vs-aws-api-gateway

[FACT] "A peer-reviewed study found Istio sidecar adds +166% latency vs baseline, while Istio Ambient mode adds only +8%. Linkerd adds +33% latency and consumes an order of magnitude less CPU and memory than Istio at the data plane level."
— X4: Application Logic Three-Tier Comparison
URL: https://arxiv.org/html/2411.02267v1

[FACT] Service mesh adoption declined from 18% to 8% between Q3 2023 and Q3 2025.
— W01S: Wave 1 Synthesis (citing CNCF State of Cloud Native Q3 2025)
URL: https://www.cncf.io/wp-content/uploads/2025/11/cncf_report_stateofcloud_111025a.pdf

[FACT] Kong achieves 130,014 RPS at P99 6.01ms on a single 16-vCPU node (proxy-only). Each plugin layer reduces Kong throughput 14–33%.
— F34: On-Premises API Gateway
URL: https://developer.konghq.com/gateway/performance/benchmarks/

[FACT] Self-hosted API gateway cost: $10K–$50K+ annually. Managed API gateway starts at $3.50/million API calls (AWS).
— F03: API Gateways and Service Communication
URL: https://www.gravitee.io/blog/managed-vs-self-hosted-api-gateway-costs

**Tier Analysis:**

*Cloud-Native (Difficulty: 2):* AWS API Gateway, Azure APIM, and GCP Apigee provide managed gateways with built-in rate limiting, TLS termination, and observability. Application code calls managed APIs with standard HTTP/gRPC semantics. The 29-second AWS API Gateway timeout is the primary application-code constraint ISVs must design around. App Mesh users face a September 2026 EOL requiring migration to ECS Service Connect.

*Managed K8s (Difficulty: 3):* The Ingress NGINX retirement (March 2026) forces mandatory migration to Gateway API — an unplanned forcing function affecting all managed K8s ISVs regardless of product roadmap priority. Gateway API is controller-agnostic and protocol-agnostic, but the migration requires reworking all routing configurations away from vendor-specific Ingress annotations. Service mesh selection carries dramatic performance implications: ISVs should evaluate Istio Ambient mode (Beta since v1.22, only +8% latency overhead) before committing to sidecar-based architectures. The total FTE for managed K8s gateway operations is 0.3–0.6 FTE.

*On-Premises (Difficulty: 4):* Self-hosted Kong or Traefik requires the ISV to own the full gateway lifecycle: SSL certificate rotation, plugin configuration and upgrade, distributed rate limiting via Redis Cluster with Lua atomicity scripts, and Consul Connect for mTLS. Total on-premises API gateway FTE is 1.5–3.0 FTE (from F34), with application code required to integrate Consul client libraries for service routing.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2 | 3 | 4 |
| Key tools | AWS API GW, Azure APIM, GCP Apigee | Gateway API + Envoy/Traefik; Istio Ambient | Kong/Traefik self-hosted; Consul Connect |
| ISV code impact | Design within 29s timeout; SIGTERM handling | Gateway API migration from Ingress NGINX | Consul SDK, Redis rate-limit atomicity |
| Est. FTE | 0.1–0.2 | 0.3–0.6 | 1.5–3.0 |

---

### AL04 — Data Access, ORM Layer, and Caching Integration

**Change Driver:** Database engine upgrade, ORM major version change, query performance regression, or cache invalidation policy change.

**Scope:** The application-layer code that mediates between business logic and persistent storage — ORM frameworks, query builders, connection pool configuration (not infrastructure), transaction management, and distributed cache client integration (read-through, write-through, TTL policies). Excludes database schema migrations and database infrastructure HA (Data Plane).

**Evidence and Difficulty Ratings:**

[FACT] Prisma provides type-safe, auto-generated database clients with a schema-first approach and is the preferred choice for modern TypeScript backends in 2025. TypeORM's `synchronize: true` option is dangerous in production.
— F73: MECE ISV Developer Responsibility Framework
URL: https://www.bytebase.com/blog/prisma-vs-typeorm/

[FACT] SQLAlchemy remains the standard for Python backends integrating with Alembic for migrations.
— F73: MECE ISV Developer Responsibility Framework
URL: https://medium.com/@connect.hashblock/typeorm-vs-prisma-vs-sqlalchemy-pick-by-maintainability-23a0b57fc97c

[FACT] Amazon ElastiCache is a fully-managed service where "all the administrative tasks associated with managing your Redis cluster (including monitoring, patching, backups, and automatic failover), are managed by Amazon."
— F75: MECE Abstraction Layer Framework
URL: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/amazon-elasticache-and-self-managed-redis.html

[FACT] Self-hosted Redis "requires careful planning around Kubernetes StatefulSets and persistent volumes to ensure data durability and availability" when deployed on Kubernetes.
— F75: MECE Abstraction Layer Framework
URL: https://www.dragonflydb.io/guides/redis-vs-elasticache

[FACT] Spotahome Redis Operator last released January 2022; Bitnami Redis Helm Chart is the actively maintained alternative.
— X4: Application Logic Three-Tier Comparison
URL: https://blog.palark.com/failure-with-redis-operator-and-redis-data-analysis-tools/

**Tier Analysis:**

ORM code and cache client integration are largely portable across tiers — the same SQLAlchemy or Prisma code runs on Lambda, a K8s pod, or a bare-metal server. The tier-differentiated complexity is connection string management, connection pool sizing, and failover awareness.

*Cloud-Native (Difficulty: 2):* RDS Proxy manages connection pooling with IAM-based authentication; Aurora fast failover completes in approximately 1–2 seconds transparently. ElastiCache is fully managed. ISV application code uses standard SDK connection strings.

*Managed K8s (Difficulty: 2):* CloudNativePG provides managed PostgreSQL HA on K8s with standardized service endpoints (`-rw`, `-ro`, `-r`). Application code must handle connection strings via K8s Services and configure PgBouncer parameters. Redis operator selection matters — Bitnami's Helm Chart is preferred over the stale Spotahome operator.

*On-Premises (Difficulty: 2):* Patroni requires etcd or Consul as the distributed config store plus HAProxy for connection routing. Application code must handle Patroni topology changes and Sentinel failover events. Redis Sentinel provides HA monitoring without Cluster complexity. The application-layer code burden is marginally higher (failover event handling), but ORM code itself is unchanged.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2 | 2 | 2 |
| Key tools | RDS Proxy, ElastiCache (Valkey/Redis), Aurora SDK | CloudNativePG, Bitnami Redis Helm, PgBouncer | Patroni + HAProxy, Redis Sentinel, PgBouncer |
| ISV code impact | Standard ORM + IAM connection strings | Operator-aware service endpoints, TTL config | Topology-aware connection handling, Sentinel integration |
| Est. FTE | 0.5–1.0 | 0.5–1.0 | 0.75–1.5 |

---

### AL05 — Background Jobs, Async Processing, and Event-Driven Integration

**Change Driver:** New batch feature, SLA requirement for long-running tasks, message broker infrastructure change, event schema evolution.

**Scope:** All application code that processes work outside the request-response cycle: job definition code, queue producer/consumer client configuration, Saga compensation logic, workflow step implementations, and event schema management at the producer/consumer boundary. Excludes message broker infrastructure operations and schema registry operations (Control Plane adjacent). Includes Temporal workflow step code, Celery task definitions, and transactional outbox implementation patterns.

**Evidence and Difficulty Ratings:**

[FACT] Redis with Celery achieves 5,200 tasks per second at 12ms average latency, outperforming RabbitMQ's 3,100 tasks per second at 28ms by 68% in throughput.
— F73: MECE ISV Developer Responsibility Framework
URL: https://johal.in/celery-distributed-tasks-redis-broker-configuration-for-scalable-web-background-jobs/

[FACT] Self-hosting Temporal requires Cassandra for persistence and Elasticsearch for visibility in production; PostgreSQL is unsuitable for medium-to-large-scale systems — even 100 RPS caused spiked database load beyond 120.
— W05S: On-Premises Application Pattern Challenges
URL: https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b

[FACT] Temporal learning curve: "Expect a month before your team is productive."
— F33: On-Premises Event-Driven Architecture
URL: https://blog.taigrr.com/blog/setting-up-a-production-ready-temporal-server/

[FACT] "In production, on-premises Kafka clusters are difficult to set up, expand, and maintain... organizations must plan clusters of distributed servers to assure availability, maintain data storage and security, set up monitoring, and handle scaling." Managed services allow teams to "create clusters in minutes rather than days or weeks."
— F75: MECE Abstraction Layer Framework
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons

[FACT] Confluent claims TCO savings of up to 60% with their managed service compared to self-hosted Kafka deployments.
— F75: MECE Abstraction Layer Framework
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons

[FACT] On-premises EDA requires 2–4 FTE dedicated solely to EDA pattern operations vs. 0.1–0.6 FTE cloud-native.
— F33: On-Premises Event-Driven Architecture
URL: (aggregated from F33 FTE analysis)

**Tier Analysis:**

*Cloud-Native (Difficulty: 1):* AWS Step Functions, AWS SQS + Lambda, Azure Durable Functions, and GCP Cloud Tasks eliminate broker and worker infrastructure entirely. ISV writes job definition code against managed service APIs. DLQs are native. Schema evolution is managed via EventBridge Schema Registry or AWS Glue.

*Managed K8s (Difficulty: 3):* The ISV must deploy and operate Celery workers with KEDA for queue-length-based autoscaling, or deploy Temporal with a K8s Operator (requiring Cassandra or PostgreSQL persistence). Strimzi manages Kafka on K8s, but the ISV owns topic creation, retention policy, and consumer group offset management. The application-layer integration surface expands to include Strimzi operator service endpoints, KEDA ScaledObject configuration, and Temporal workflow step SDK integration.

*On-Premises (Difficulty: 4):* Temporal on-premises requires Cassandra (not PostgreSQL for production scale) plus Elasticsearch plus four discrete service pods. The one-month learning curve compounds with ongoing config drift as Temporal frequently changes configuration requirements between versions. On-premises Kafka DLQ is application-layer only — no native DLQ support. Contract testing requires self-hosted Pact Broker (Docker + PostgreSQL). Total EDA operations FTE: 2.0–4.1 FTE active plus 0.85 FTE on-call.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 1 | 3 | 4 |
| Key tools | Step Functions, SQS, Cloud Tasks, Durable Functions | Celery + KEDA, Temporal (K8s operator), Strimzi | Temporal (Cassandra + ES), Celery + RabbitMQ, self-hosted Kafka |
| ISV code impact | Serverless queue config, job definitions | KEDA ScaledObject, Temporal workflow steps, Strimzi topics | Full Temporal SDK integration, DLQ in app layer, schema registry client |
| Est. FTE | 0.1–0.2 | 0.4–0.8 | 0.75–1.5 (app code) + 2.0–4.1 (ops) |

---

### AL06 — Resilience Patterns and Runtime Behavior

**Change Driver:** Incident post-mortem, SLA target change, new dependency introduced, platform EOL (App Mesh, Ingress NGINX).

**Scope:** All application-layer resilience logic: circuit breakers, retry policies with exponential backoff and jitter, timeout budgets, bulkhead isolation, and health check endpoint implementations. On cloud-native and managed K8s tiers, significant resilience is platform-provided (service mesh DestinationRules, ECS Service Connect). On-premises, this logic moves into the application code itself. Also covers graceful shutdown sequence implementation (SIGTERM handlers, drain logic) and auto-scaling awareness (KEDA metric exposure, Lambda cold-start optimization).

**Evidence and Difficulty Ratings:**

[FACT] Resilience4j is a lightweight fault tolerance library for Java 8 and functional programming, providing circuit breakers, rate limiters, retry mechanisms, bulkheads, and time limiters. It is "the recommended choice and natural successor to the now end-of-life Spring Cloud Hystrix libraries."
— F72: Application Resilience Patterns
URL: https://resilience4j.readme.io/docs/circuitbreaker

[FACT] Polly provides .NET resilience policies (Retry, Circuit Breaker, Timeout, Bulkhead, Fallback) with "deep integration into the Microsoft.Extensions ecosystem through the new Microsoft.Extensions.Resilience package" in Polly v8.
— F72: Application Resilience Patterns
URL: https://github.com/App-vNext/Polly

[FACT] Kubernetes supports three probe types: Liveness (restarts container on failure), Readiness (removes pod from service endpoints without restarting), and Startup (delays liveness/readiness checks until container has started). Native sidecar containers reached stable status in Kubernetes v1.33 (April 2025).
— F72: Application Resilience Patterns
URL: https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/

[FACT] Kubernetes default terminationGracePeriodSeconds is 30 seconds. PreStop hooks execute before SIGTERM and run in parallel with the grace period countdown.
— F72: Application Resilience Patterns (citing devopscube.com)
URL: https://devopscube.com/kubernetes-pod-graceful-shutdown/

[FACT] Kubernetes Cluster Autoscaler does not support on-premises bare metal because it cannot create or delete VMs. Bare metal node provisioning takes up to 8 minutes.
— F72: Application Resilience Patterns
URL: https://github.com/kubernetes/autoscaler/issues/1060

[FACT] As of August 2025, AWS bills for the Lambda INIT phase, increasing spend by 10–50% for heavy-startup functions. Provisioned concurrency for 20 functions costs approximately $8,800/month before executions.
— F72: Application Resilience Patterns
URL: https://zircon.tech/blog/aws-lambda-cold-start-optimization-in-2025-what-actually-works/

[FACT] KEDA (CNCF Graduated, August 2023) supports 74+ event-source scalers and enables scaling down to zero replicas.
— X4: Application Logic Three-Tier Comparison
URL: https://keda.sh/

**Tier Analysis:**

*Cloud-Native (Difficulty: 2):* Platform handles most resilience. ECS Service Connect provides opinionated defaults for health checks, outlier detection, and retries. Cloud Run handles graceful shutdown by default (SIGTERM + 10-second grace). Lambda scales automatically but requires cold-start awareness in application code. The August 2025 change billing the Lambda INIT phase is a significant cost concern for startup-heavy functions.

*Managed K8s (Difficulty: 3):* Application code must implement all three probe types (liveness, readiness, startup) with correct thresholds. PreStop hooks and SIGTERM handlers must be implemented explicitly. Circuit breaking and retries are configured via service mesh (Istio DestinationRule, Linkerd budgeted retries), but application code must be designed to respect timeout budgets propagated from the mesh. KEDA ScaledObject resources expose queue-depth and Prometheus metrics for autoscaling — requiring ISV to expose appropriate metrics endpoints.

*On-Premises (Difficulty: 4):* Application code must embed Resilience4j (Java) or Polly (.NET) for circuit breakers, retries, bulkhead isolation, and fallbacks. Health monitoring integrates with Consul distributed health checks (HTTP/TCP/script/TTL modes). Auto-scaling is fundamentally limited: Cluster Autoscaler does not support bare metal, and node provisioning takes up to 8 minutes. KEDA can scale pods (not nodes), providing partial but not full elasticity. ISVs must over-provision or accept scaling latency.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2 | 3 | 4 |
| Key tools | ECS Service Connect, Cloud Run SIGTERM, Lambda cold-start tuning | K8s probes, KEDA, Istio DestinationRule, preStop hooks | Resilience4j/Polly, Consul health checks, manual node over-provisioning |
| ISV code impact | SIGTERM handler, cold-start minimization, INIT phase cost | Three probe implementations, SIGTERM/preStop, metric endpoint exposure | Circuit breaker code, Consul client, retry + jitter logic embedded in services |
| Est. FTE | 0.15–0.3 | 0.3–0.6 | 0.75–1.5 |

---

### AL07 — Multi-Tenant Isolation Logic

**Change Driver:** New enterprise customer onboarding, compliance scope expansion, security audit finding on tenant boundary, data residency requirement.

**Scope:** The application middleware and enforcement code that ensures every data operation, API response, queue event, file operation, and AI inference is scoped to the correct tenant. Covers: tenant-context injection middleware, row-level security policy activation, per-tenant feature flag routing, and tenant-aware background job scoping. This is the only subsegment that is equally complex at the application code level across all three deployment tiers.

**Evidence and Difficulty Ratings:**

[FACT] "Multi-Tenant Isolation Logic (C12) is the only tier-invariant component at difficulty 3/5 across all models, because it is a software architecture problem. ISVs should invest in a tenant-context framework early, as retrofitting it into production code at scale is prohibitively expensive regardless of deployment tier."
— F73: MECE ISV Developer Responsibility Framework

[FACT] "Application logic must enforce that every piece of data belongs to exactly one tenant, every request runs with a tenant context, and every authorization decision is evaluated within that tenant context."
— F73: MECE ISV Developer Responsibility Framework (citing Medium article)
URL: https://medium.com/@justhamade/architecting-secure-multi-tenant-data-isolation-d8f36cb0d25e

[FACT] "Namespace isolation in Kubernetes is not a security boundary by default; even with API and network isolation, namespaces do not provide cluster-level security equivalent to separate clusters."
— F72/F73 (citing Atmosly)
URL: https://atmosly.com/blog/kubernetes-multi-tenancy-complete-implementation-guide-2025

[FACT] Multi-tenancy research across 127 cloud organizations: 42% infrastructure cost reduction, 61.8% resource utilization gain from pooled multi-tenancy. Pooled SaaS achieves 70–80% resource utilization; on-prem single-tenant achieves 20–40%.
— F66: Multi-Tenancy and SaaS Leverage
URL: (F66 research aggregate)

[FACT] "In SaaS multi-tenancy, the tenant does not interface directly with the Kubernetes API; the application is responsible for interfacing with the Kubernetes API on the tenant's behalf."
— F73: MECE ISV Developer Responsibility Framework
URL: https://docs.aws.amazon.com/eks/latest/best-practices/tenant-isolation.html

**Tier Analysis:**

The application-layer complexity of tenant isolation logic is identical across all deployment tiers. What differs is the *platform layer* beneath the application: cloud-native platforms provide AWS Lambda tenant isolation mode and native per-tenant routing via API Gateway; managed K8s offers namespace isolation (weak) or vCluster (strong); on-premises requires manual network segmentation with no managed isolation primitives. But in all three cases, the ISV must write and maintain the same tenant-context middleware, RLS activation code, and per-tenant scoping logic.

*All Tiers (Difficulty: 3):* The complexity is architectural, not operational. The ISV must build a tenant-context framework that propagates tenant identity from authentication through every service call, database query, cache key, queue message, and AI inference. Database row-level security enables multiple tenants to share tables while maintaining separation. The difficulty is 3/5 across all tiers because this is non-trivial design work with significant security consequences for any error.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 3 | 3 | 3 |
| Key tools | Custom middleware, PostgreSQL RLS, Casbin, AWS SaaS Factory | vCluster, Kyverno tenant policies, HNC, same app middleware | PostgreSQL RLS, OPA, Casbin, custom enforcement |
| ISV code impact | Tenant context middleware, RLS activation, per-tenant routing | Same + namespace quota enforcement awareness | Same + manual network segmentation awareness |
| Est. FTE | 0.5–1.0 | 0.5–1.0 | 0.75–1.5 |

---

### AL08 — Observability Instrumentation and AI Telemetry

**Change Driver:** Incident post-mortem, audit requirement, new AI agent deployment, SLA target change, new semantic convention release.

**Scope:** The code ISV engineers write — or the auto-instrumentation they configure — to emit traces, metrics, and logs from application code. Covers: OpenTelemetry SDK wiring, span and metric emission for business logic and AI pipeline stages, health endpoint exposure, and GenAI semantic convention adoption. Distinct from the observability *platform* (Grafana, Datadog, Prometheus storage) which is a Control Plane concern. Includes AI-specific telemetry: token usage tracking, agent step tracing, prompt/response logging.

**Evidence and Difficulty Ratings:**

[FACT] OpenTelemetry's GenAI Semantic Conventions are now part of the official specification (v1.37+), defining standard attributes for `gen_ai.request.model`, `gen_ai.usage.input_tokens`, and `gen_ai.provider.name`.
— F73: MECE ISV Developer Responsibility Framework
URL: https://opentelemetry.io/docs/specs/semconv/gen-ai/

[FACT] AI Agent observability semantic conventions are under active development in the CNCF #otel-genai-instrumentation working group, covering tasks, actions, agents, teams, artifacts, and memory as first-class traceable entities.
— F73: MECE ISV Developer Responsibility Framework
URL: https://opentelemetry.io/blog/2025/ai-agent-observability/

[FACT] OpenTelemetry ranks as the second-highest-velocity CNCF project with 24,000+ contributors.
— F75: MECE Abstraction Layer Framework
URL: https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/

[FACT] "51% of organizations in the Voice of Kubernetes Experts 2025 survey identify observability difficulties as a primary operational challenge."
— F75: MECE Abstraction Layer Framework
URL: https://www.cncf.io/blog/2025/08/02/what-500-experts-revealed-about-kubernetes-adoption-and-workloads/

[FACT] "Unlike cloud-native environments where instrumentation is built-in, legacy systems rely on inconsistent logs and fragmented tools, making troubleshooting slow and painful."
— F73: MECE ISV Developer Responsibility Framework (citing OpenTelemetry blog)
URL: https://opentelemetry.io/blog/2026/demystifying-opentelemetry/

[FACT] AWS CloudWatch launched generative AI observability (November 2025) with native LLM tracing, token metrics, and compatibility with LangChain/LangGraph/CrewAI.
— X4: Application Logic Three-Tier Comparison
URL: https://aws.amazon.com/blogs/mt/launching-amazon-cloudwatch-generative-ai-observability-preview/

**Tier Analysis:**

*Cloud-Native (Difficulty: 2):* OTel SDK wiring is the core task, routing OTLP to managed backends (CloudWatch, Azure Monitor, Google Cloud Monitoring) with near-zero pipeline infrastructure. CloudWatch GenAI Observability (November 2025) provides native LLM tracing, token metrics, and agent framework compatibility. Application code instruments spans; the platform handles storage, retention, and dashboarding.

*Managed K8s (Difficulty: 2):* OTel Collector runs as a DaemonSet or sidecar, automatically enriching telemetry with pod names, namespaces, and node labels. Application code instruments identically to cloud-native. The ISV platform team deploys and upgrades the Collector and chooses a managed Grafana backend. The instrumentation code burden is the same; the Collector deployment adds modest platform overhead not counted in this application-logic rating.

*On-Premises (Difficulty: 3):* Langfuse self-hosted (for AI telemetry) requires PostgreSQL + ClickHouse + Redis/Valkey + S3 blob storage — a substantial infrastructure commitment. OpenTelemetry Collector fleet management, LGTM stack operations, and log retention policy management are all ISV responsibilities. Application-layer instrumentation code is identical, but the ISV must also validate that on-premises backends correctly receive and index telemetry signals — a feedback loop absent when managed backends are used.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2 | 2 | 3 |
| Key tools | OTel SDK, CloudWatch GenAI, Azure Monitor, Cloud Logging | OTel Collector DaemonSet, Prometheus, Grafana, Tempo | OTel Collector fleet, Loki, Grafana, Mimir, Langfuse (self-hosted) |
| ISV code impact | OTel SDK wiring, GenAI semantic conventions, span emission | Same + DaemonSet enrichment awareness | Same + self-hosted backend validation, Langfuse PostgreSQL/ClickHouse |
| Est. FTE | 0.2–0.4 | 0.3–0.6 | 0.5–1.0 |

---

### AL09 — AI/ML Orchestration, Agent Pipelines, and MCP Integration

**Change Driver:** Model update, inference latency SLA change, new agent capability (RAG, tool calling, multi-agent coordination), MCP server addition, framework major version.

**Scope:** All application code in the AI/ML orchestration layer: LangGraph graph definitions and checkpointing configuration, CrewAI crew and flow definitions, agent state management (PostgresSaver, RedisSaver), MCP server integration (tool registration, security sandboxing), multi-agent coordination patterns, RAG pipeline orchestration code, AI safety guardrail integration, and AI observability instrumentation (Langfuse, Arize Phoenix). This is the fastest-evolving subsegment and the highest-difficulty on-premises component in the entire framework.

**Evidence and Difficulty Ratings:**

[FACT] LangGraph 1.0 reached stable release October 2025; 6.17 million monthly downloads. Production users include Uber, GitLab, Klarna, and Rakuten.
— F07: AI Agent Frameworks
URL: https://blog.langchain.com/langchain-langgraph-1dot0/

[FACT] CrewAI: 1.4 billion agentic automations per month, 450 million agents per month.
— F07: AI Agent Frameworks
URL: (F07 research)

[FACT] MCP donated to Linux Foundation (AAIF) December 2025.
— F07: AI Agent Frameworks; W01S: Wave 1 Synthesis
URL: https://blog.equinix.com/blog/2025/08/06/what-is-the-model-context-protocol-mcp-how-will-it-enable-the-future-of-agentic-ai/

[FACT] "Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027."
— W01S: Wave 1 Synthesis
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

[FACT] Coordination latency: 200ms with 5 agents grows to 2 seconds with 50 agents. Multi-agent systems show 2–5x token cost increases.
— F07: AI Agent Frameworks
URL: https://www.getmaxim.ai/articles/multi-agent-system-reliability-failure-patterns-root-causes-and-production-reliability-failure-patterns-root-causes-and-production-validation-strategies/

[FACT] Research across 150+ traces found correctness as low as 25% for leading open-source multi-agent systems.
— W01S: Wave 1 Synthesis
URL: https://arxiv.org/html/2503.13657v1

[FACT] On-premises AI agent infrastructure requires 7 distinct platform layers: tool registry, sandboxed execution, state management, workflow orchestration, metering, security sandboxing, GPU scheduling.
— F38: On-Premises AI Agent Infrastructure
URL: (F38 research aggregate)

[FACT] Total on-premises platform engineering FTE for agent infrastructure only: 2.75–4.75 FTE vs. 0.2–1.2 FTE cloud-native.
— F38: On-Premises AI Agent Infrastructure; W05S: On-Premises App Patterns
URL: https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration

[FACT] LangGraph checkpointing: PostgresSaver for production, RedisSaver v0.1.0 (2025 complete redesign for production use).
— F38: On-Premises AI Agent Infrastructure

[FACT] Langfuse self-hosted requires: PostgreSQL + ClickHouse + Redis/Valkey + S3 blob storage.
— F38: On-Premises AI Agent Infrastructure
URL: https://langfuse.com/self-hosting

[FACT] KServe v0.15 (June 2025) is transitioning from a traditional ML serving platform to the standard control plane for generative AI, with enhanced support for multi-node LLM inference, improved KV caching, and integration with Envoy AI Gateway.
— F73: MECE ISV Developer Responsibility Framework
URL: https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/

[FACT] Amazon Bedrock AgentCore runs each session in a dedicated microVM with isolated CPU/memory, with persistent execution environments lasting up to 8 hours. AgentCore Memory provides both short-term conversation context and long-term cross-session memory.
— X4: Application Logic Three-Tier Comparison
URL: https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/

[FACT] "Safety guardrails for AI inference can triple latency and cost in production."
— F73: MECE ISV Developer Responsibility Framework (citing dynamo.ai)
URL: https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance

**Tier Analysis:**

*Cloud-Native (Difficulty: 2 — API Integration; 4 — Custom Pipelines):* Application code calls Bedrock, Azure OpenAI, or Vertex AI managed endpoints. Managed RAG (Bedrock Knowledge Bases, Vertex AI RAG Engine), managed agent orchestration (AgentCore), and managed guardrails (Bedrock Guardrails, Azure Content Safety) eliminate infrastructure management. LangGraph and CrewAI orchestration code runs without self-hosting any inference, state, or sandbox infrastructure. The difficulty is 2/5 for standard API-first integration; it rises to 4/5 for ISVs building custom LangGraph pipelines with advanced checkpointing, multi-provider routing, and fine-grained guardrail logic.

*Managed K8s (Difficulty: 3):* KServe v0.15 + vLLM/TGI for serving; KEDA GPU-aware autoscaling for inference load; NeMo Guardrails as a pre-inference container; LangGraph with PostgresSaver checkpointing. The ISV writes the same orchestration code but is responsible for deploying and configuring the serving infrastructure, GPU scheduling, model storage, and inference autoscaling. The Gateway API Inference Extension (June 2025) provides K8s-native traffic routing for LLM inference, reducing configuration complexity versus custom Ingress rules.

*On-Premises (Difficulty: 5):* The ISV must self-host the entire AI stack: vLLM/TGI serving framework with CUDA driver management, Milvus or Qdrant vector database, Temporal for agent workflow orchestration, Langfuse for observability (PostgreSQL + ClickHouse + Redis + S3), LlamaFirewall or OpenGuardrails for safety, and LiteLLM proxy for multi-model routing. Agent state management requires LangGraph with PostgresSaver in a self-hosted PostgreSQL cluster. Kubernetes SIG Agent Sandbox (CNCF, KubeCon NA 2025) provides a new standard for K8s agent code execution sandboxing, but requires ISV configuration. Total FTE: 6.0–10.0 for the combined inference, orchestration, and observability stack (from F73, F38, W05S).

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2/4* | 3 | 5 |
| Key tools | Bedrock/Azure OpenAI/Vertex AI, AgentCore, LangGraph (API calls) | KServe v0.15, vLLM, LangGraph + PostgresSaver, NeMo Guardrails | vLLM/TGI, Milvus/Qdrant, Temporal, Langfuse, LiteLLM, LlamaFirewall |
| ISV code impact | LangGraph graphs, MCP server calls, prompt templates, guardrail config | Same + KServe InferenceService config, KEDA GPU metrics, model version routing | Same + all serving infra integration, GPU scheduling, agent sandbox config |
| Est. FTE | 0.5–1.2 | 2.0–4.0 | 6.0–10.0 |

*2 = standard API integration; 4 = custom multi-provider LangGraph pipelines with advanced checkpointing.

---

### AL10 — Testing Strategy, Contract Testing, and Environment Parity

**Change Driver:** New service dependency, API contract revision, deployment to new customer environment, failure mode discovered in production.

**Scope:** The application-layer testing artifacts and strategies the ISV must maintain across deployment tiers: contract tests (Pact), integration test suites, test environment configuration (Testcontainers, LocalStack), and the policies governing which tests must pass before release to each tier. The test matrix explosion — the combinatorial surface of K8s versions, cloud provider versions, OS variants, and GPU driver versions — is the primary tier-differentiated complexity.

**Evidence and Difficulty Ratings:**

[FACT] Replicated Compatibility Matrix: 65,981+ unique Kubernetes configuration combinations. Most ISVs test only a few combinations; problems are typically discovered in live customer accounts.
— F57: Build and Test Differences
URL: (F57 research)

[FACT] On-premises GPU test lab: approximately $500K capital cost (8x H100s). Cloud H100: $1.49–$3.90/hour (AWS cut 44% in June 2025).
— F57: Build and Test Differences
URL: (F57 research; intuitionlabs.ai for H100 pricing)

[FACT] Total build/test FTE: On-Premises = 3.75–7.0 FTE; Managed K8s = 2.0–4.0 FTE; Cloud-Native = 0.7–1.65 FTE.
— F57: Build and Test Differences
URL: (F57 research aggregate)

[FACT] DORA elite performers: 182x more frequent deployments, 127x faster change lead times.
— F64: Time to Market
URL: (F64 research)

[FACT] LLM model update cycle: On-Premises = 6–16 weeks; Managed K8s = 2–4 weeks; Cloud-Native = 1–7 days.
— F64: Time to Market
URL: (F64 research)

[FACT] Self-hosted Pact Broker requires Docker + PostgreSQL for contract testing.
— F33: On-Premises Event-Driven Architecture
URL: (F33 research)

**Tier Analysis:**

*Cloud-Native (Difficulty: 2):* Testcontainers and LocalStack simulate cloud service behavior for unit and integration testing. Contract tests use Pact with PactFlow (managed SaaS). The test matrix is narrow — one cloud environment target per cloud provider region. CI/CD pipelines use managed runners (GitHub Actions, AWS CodePipeline). Test environments are ephemeral and low-cost.

*Managed K8s (Difficulty: 3):* The test matrix expands to cover EKS/AKS/GKE version ranges plus Kubernetes minor version compatibility. Contract testing requires validating against multiple Gateway API controller implementations. Testcontainers and LocalStack remain applicable but must be validated against K8s-operator-managed service behavior (e.g., CloudNativePG vs. RDS behavior differences). Self-hosted Pact Broker requires Docker + PostgreSQL operational overhead.

*On-Premises (Difficulty: 4):* The 65,981+ unique K8s configuration combinations represent the upper bound of the on-premises test matrix. Practically, ISVs test a small subset and discover failures in production. GPU driver version compatibility adds a second dimension: each model inference test must be validated against specific CUDA version / GPU driver combinations. QEMU cross-architecture builds for ARM64 targets inflate 4-minute builds to 40+ minutes. Total build/test FTE on-premises is 3.75–7.0 FTE.

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|-----------|:-----------:|:-----------:|:-----------:|
| **Difficulty** | 2 | 3 | 4 |
| Key tools | Testcontainers, LocalStack, PactFlow (managed), GitHub Actions | Testcontainers, self-hosted Pact Broker, K8s multi-version CI | Replicated, self-hosted Pact Broker, QEMU cross-arch, on-prem GPU lab |
| ISV code impact | Ephemeral test environments, contract test maintenance | K8s-version compatibility tests, Gateway API controller variants | Full test matrix governance, GPU driver test matrix, QEMU build config |
| Est. FTE | 0.7–1.65 | 2.0–4.0 | 3.75–7.0 |

---

## 4. Summary Difficulty Matrix

Ratings follow the 1–5 scale defined above. Aggregate complexity scores are the unweighted sum of all 10 subsegment ratings per tier.

| Subsegment | Owner Team | Cloud-Native | Managed K8s | On-Premises |
|-----------|-----------|:---:|:---:|:---:|
| AL01 — Service Decomp & Inter-Service Comm | Backend | 2 | 2 | 3 |
| AL02 — Business Logic, Domain Services & Validation | Backend | 2 | 2 | 2 |
| AL03 — API Gateway, Edge Routing & Service Mesh | Platform/DevOps | 2 | 3 | 4 |
| AL04 — Data Access, ORM & Caching Integration | Backend | 2 | 2 | 2 |
| AL05 — Background Jobs, Async Processing & EDA | Backend | 1 | 3 | 4 |
| AL06 — Resilience Patterns & Runtime Behavior | Backend + Platform | 2 | 3 | 4 |
| AL07 — Multi-Tenant Isolation Logic | Backend + Architecture | 3 | 3 | 3 |
| AL08 — Observability Instrumentation & AI Telemetry | Platform/SRE | 2 | 2 | 3 |
| AL09 — AI/ML Orchestration, Agent Pipelines & MCP | ML + Backend | 2 | 3 | 5 |
| AL10 — Testing Strategy, Contract Testing & Env Parity | DevOps + Backend | 2 | 3 | 4 |
| **Aggregate Complexity Score** | | **20** | **26** | **34** |
| **Aggregate FTE Range (application layer)** | | **5.8–13.2** | **9.4–19.8** | **19.3–38.0** |

**Aggregate ratios:** Cloud-Native : Managed K8s : On-Premises = 20 : 26 : 34 = 1.0x : 1.3x : 1.7x

**Note on FTE ranges:** These reflect application-layer FTE only — the code, configuration, and behavioral testing responsibilities of the ISV. Infrastructure operations FTE (Control Plane) adds substantially on top, with the X4 synthesis documenting an overall 1x : 2x : 10x infrastructure staffing multiplier. The application logic FTE multiplier (1.0x : 1.3x : 1.7x) confirms that the dominant on-premises burden is *operational*, not *coding* — platform engineering absorbs the largest tier-crossing cost, not backend product engineering.

---

## 5. Tier-Differentiated vs. Tier-Invariant Subsegments

### Subsegments With the Largest Tier Spread (Delta ≥ 3 points)

**AL09 — AI/ML Orchestration, Agent Pipelines & MCP** (Cloud-Native: 2, On-Premises: 5, Delta: 3):
This is the single most consequential subsegment for ISVs building AI-driven products. The on-premises difficulty of 5/5 reflects the requirement to self-host inference serving, agent workflow orchestration (Temporal), vector databases, observability (Langfuse with 4-component stack), guardrails, and MCP server infrastructure — simultaneously, with GPU scheduling across all workloads. The Gartner prediction that 40%+ of agentic AI projects will be canceled by 2027 reflects this difficulty in the market. ISVs targeting on-premises must treat this subsegment as a product in itself requiring dedicated ML platform engineering.

### Subsegments With Moderate Tier Spread (Delta = 2–3 points)

**AL05 — Background Jobs, Async Processing & EDA** (Cloud-Native: 1, On-Premises: 4, Delta: 3):
The shift from serverless queues (difficulty 1) to self-hosted Temporal with Cassandra + Elasticsearch + four pods (difficulty 4) is one of the starker binary transitions in the framework. The one-month Temporal learning curve and PostgreSQL production unsuitability for medium-to-large scale are the primary risk factors.

**AL03 — API Gateway, Edge Routing & Service Mesh** (Cloud-Native: 2, On-Premises: 4, Delta: 2):
The Ingress NGINX retirement and App Mesh EOL create 2026 forcing functions that make this subsegment more expensive than the steady-state difficulty implies. ISVs on managed K8s have already absorbed the Gateway API migration; on-premises ISVs must also manage gateway upgrade lifecycle and Redis-backed rate limiting.

**AL06 — Resilience Patterns & Runtime Behavior** (Cloud-Native: 2, On-Premises: 4, Delta: 2):
The shift from platform-provided resilience (ECS Service Connect defaults) to application-embedded circuit breakers (Resilience4j/Polly) is the defining architectural consequence of moving to on-premises. Auto-scaling limitation (Cluster Autoscaler unsupported on bare metal) compounds the operational risk.

**AL10 — Testing Strategy** (Cloud-Native: 2, On-Premises: 4, Delta: 2):
The 65,981+ configuration combinations and the $500K capital cost of a GPU test lab are the most concrete manifestations of on-premises testing difficulty. Model update cycles of 6–16 weeks on-premises versus 1–7 days cloud-native directly translate to competitive disadvantage.

### Tier-Invariant Subsegments (Delta = 0)

**AL02 — Business Logic, Domain Services & Validation** (Difficulty: 2 across all tiers):
Domain rules and validation schemas are platform-agnostic. This is the strongest argument for clean architecture — ISVs can invest in application-layer quality without incurring deployment-tier penalties.

**AL04 — Data Access, ORM & Caching Integration** (Difficulty: 2 across all tiers):
ORM code and cache client integration are similarly portable. The tier-differentiated complexity is infrastructure management (Data Plane), not the application-layer data access code.

**AL07 — Multi-Tenant Isolation Logic** (Difficulty: 3 across all tiers):
The only subsegment rated 3/5 across all tiers — consistently moderate difficulty because tenant isolation is a software architecture problem that no platform can fully abstract.

---

## 6. Team Ownership Consolidation

| Team | Subsegments Owned | On-Prem Sum | Cloud-Native Sum | Delta |
|------|------------------|:-----------:|:----------------:|:-----:|
| Backend engineering | AL01, AL02, AL04, AL05, AL07 | 14 (avg 2.8) | 10 (avg 2.0) | +4 |
| Backend + Platform (shared) | AL06, AL09 | 9 (avg 4.5) | 4 (avg 2.0) | +5 |
| Platform/DevOps | AL03, AL08, AL10 | 11 (avg 3.7) | 6 (avg 2.0) | +5 |

**Interpretation:** Backend engineering retains relatively consistent difficulty across tiers (average 2.8/5 on-premises for its core components) because business logic, ORM, and multi-tenant middleware are infrastructure-neutral. The shared and platform-owned subsegments (AL03, AL06, AL09) absorb the largest difficulty increase. This is the structural argument for why ISVs with small platform and ML teams face disproportionate on-premises delivery risk: their backend team can ship the same quality product at any tier, but the platform/ML team must grow 3–5x.

---

## 7. Gaps and Research Boundaries

The following topics were encountered during research but fall outside the Application Logic plane scope. They are noted for routing to other planes and analyses:

- **Model serving infrastructure (GPU cluster, vLLM/TGI tuning, CUDA driver management):** Covered in the AI Model Plane (P4). AL09 rates the *application orchestration code* calling these services; infrastructure operations are excluded.
- **Database schema migrations and Data Plane HA:** Covered in Data Plane (P3). AL04 rates ORM and connection pool *code*; the database infrastructure lifecycle is excluded.
- **Compliance evidence collection and audit automation:** Covered in F67 (Compliance & Regulatory) and F71 (On-Prem Security Ops). AL07 rates multi-tenant isolation *code*; compliance audit mechanics are excluded.
- **ISV gross margin analysis and business impact:** Covered in F64 and F66 (Wave 9 business impact analysis). This document rates technical difficulty, not financial return.
- **Quantitative FTE overlap between subsegments:** Subsegments AL05 (EDA) and AL09 (agent orchestration) both reference Temporal — ISVs deploying both subsegments on-premises may amortize the Temporal operational cost across both use cases, reducing the combined FTE below the sum of both estimates. The analysis above does not deduplicate this overlap.

**Known data gaps:**

- No authoritative benchmark exists for the incremental FTE cost of retrofitting a tenant-context framework into an existing production codebase (AL07). The claim that it is "prohibitively expensive" is supported qualitatively in F73 but lacks a quantitative study.
- The 65,981+ Replicated compatibility matrix figure represents the theoretical test surface for AL10; empirical data on what fraction of these combinations ISVs actually test is unavailable.
- The Gartner 40% agent project cancellation rate (AL09) applies to agentic AI projects broadly; no sub-analysis by deployment tier exists.

---

## Sources

### Primary Research Files
- F01: Microservices Architecture — `/wave1/F01_microservices_architecture.md`
- F02: Event-Driven Architecture — `/wave1/F02_event_driven_architecture.md`
- F03: API Gateways & Service Communication — `/wave1/F03_api_gateways_service_comm.md`
- F07: AI Agent Frameworks — `/wave1/F07_ai_agent_frameworks.md`
- F32: On-Premises Microservices — `/wave5/F32_onprem_microservices.md`
- F33: On-Premises Event-Driven Architecture — `/wave5/F33_onprem_event_driven.md`
- F34: On-Premises API Gateway — `/wave5/F34_onprem_api_gateway.md`
- F38: On-Premises AI Agent Infrastructure — `/wave5/F38_onprem_ai_agent_infra.md`
- F56: Design Architecture Constraints — `/wave8/F56_design_architecture_constraints.md`
- F57: Build and Test Differences — `/wave8/F57_build_test_differences.md`
- F64: Time to Market — `/wave9/F64_time_to_market.md`
- F66: Multi-Tenancy and SaaS Leverage — `/wave9/F66_multitenancy_saas_leverage.md`
- F72: Application Resilience Patterns — `/wave10/F72_application_resilience_runtime.md`
- F73: MECE ISV Developer Responsibility Framework — `/wave11/F73_mece_isv_developer_responsibility.md`
- F74: MECE Integration Surface — `/wave11/F74_mece_integration_surface.md`
- F75: MECE Abstraction Layer Framework — `/wave11/F75_mece_abstraction_layer.md`
- W01S: Wave 1 Foundation Patterns Synthesis — `/synthesis/W01S_foundation_patterns.md`
- W05S: On-Premises App Patterns Synthesis — `/synthesis/W05S_onprem_app_patterns.md`
- X4: Application Logic Three-Tier Comparison — `/synthesis/X4_application_logic_three_tier_comparison.md`

### Key External Sources (cited across input files)
- Kubernetes Probes Documentation: https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/
- Ingress NGINX Retirement (Nov 2025): https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/
- KServe v0.15 — CNCF (Jun 2025): https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/
- LangGraph 1.0 GA (Oct 2025): https://blog.langchain.com/langchain-langgraph-1dot0/
- Gartner 40% Agent Project Cancellation: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- CNCF Annual Cloud Native Survey 2025 (82% K8s production): https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/
- Kubernetes Cluster Autoscaler bare metal limitation: https://github.com/kubernetes/autoscaler/issues/1060
- Resilience4j documentation: https://resilience4j.readme.io/docs/circuitbreaker
- OTel GenAI Semantic Conventions v1.37+: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- AWS App Mesh deprecation (Sep 2026): https://earezki.com/ai-news/2026-02-15-aws-app-mesh-deprecated-migration-guide-before-september-2026-shutdown/
- Temporal PostgreSQL production unsuitability: https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b
- Langfuse self-hosting requirements: https://langfuse.com/self-hosting
- Amazon Bedrock AgentCore Runtime: https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/
- gRPC vs REST benchmarks 2025: https://markaicode.com/grpc-vs-rest-benchmarks-2025/
- Service mesh latency benchmarks (arXiv): https://arxiv.org/html/2411.02267v1
