# SL1a: Phase 1 Consolidated Findings

**Synthesis Date:** 2026-02-19
**Scope:** Phase 1 (Initial Refactoring) only -- all 38 MECE subsegments across 4 planes
**Input Sources:** RP1a, RP1b, RP1c, RP1d, RP1e, RP2a, RP2b, RP3a, RP3b, RP4a, CC1
**Output Type:** Consolidated synthesis for decision-maker review

---

## Executive Summary

Across 34 actively rated ISV-scope subsegments (4 are customer scope), the Phase 1 ratings in `three_phase_on_prem_ratings.md` are substantively accurate: 33 of 34 subsegment RD/TE pairs are confirmed by independent review agents with High or Medium-High confidence, with a single adjustment identified -- S1 (Managed API Integration) Phase 1 Relative Difficulty should increase from 1 to 2, reflecting non-trivial authentication re-implementation, Bedrock schema delta, and error handling rewrite work when migrating from cloud-managed inference APIs to customer-provided vLLM endpoints. The Phase 1 aggregate effort estimate of ~72-149 person-months is arithmetically consistent with the subsegment TE distribution but relies on an undocumented parallelization factor (0.55-0.67x applied to a raw unconstrained total of 64-120 person-months for P1 alone); the upper bound of 80 person-months for P1 Control Plane is the more defensible planning figure, as the 40-person-month lower bound requires conditions -- experienced team, no learning curve, immediate CP-01 execution -- that are unlikely to co-occur in a typical mid-size ISV.

---

## 1. Rating Accuracy by Plane

### 1.1 P1 Control Plane (CP-01 through CP-10)

**Source reviews:** RP1a (CP-01 to CP-03), RP1b (CP-04 to CP-06), RP1c (CP-07 to CP-10), RP1e (effort plausibility)

All 10 P1 subsegments are confirmed ACCURATE for Phase 1 RD and TE assignments. The P1 plane carries the highest average ratings in Phase 1 (RD 4.4, TE 4.0) and represents the single largest investment area -- building the entire platform stack from scratch.

| ID | Subsegment | Phase 1 RD | Phase 1 TE | Verdict | Confidence | Notes |
|:---:|---|:---:|:---:|---|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | ACCURATE | H | Foundational substrate; all other CP subsegments depend on it. kubeadm/RKE2 HA build is unambiguously 12+ person-months. |
| CP-02 | Network Fabric / Ingress / Mesh | 5 | 4 | ACCURATE | H | Calico/Cilium CNI + Gateway API + optional mesh. High end of TE 4 but does not consistently reach TE 5. |
| CP-03 | IAM / RBAC | 4 | 4 | ACCURATE | M | Keycloak/Dex setup is well-documented; highly experienced teams could achieve TE 3. Depends on ISV's prior identity provider familiarity. |
| CP-04 | Secrets / Certs / PKI | 5 | 4 | ACCURATE | M | FIPS 140-3 path and irreversible PKI root design add planning overhead. Greenfield ISVs may approach TE 5. |
| CP-05 | Observability Infrastructure | 4 | 5 | ACCURATE | H | Prometheus + Thanos/Mimir + Loki + Tempo + Grafana + Alertmanager full-stack build. 500K+ active time series at ~2-3 KB RAM each. One of the largest initial builds. |
| CP-06 | CI/CD Pipeline / GitOps | 4 | 4 | ACCURATE | M | ArgoCD/Flux + artifact registry. Well-documented tooling, but per-customer deployment targets add novel architectural complexity. Experienced teams could achieve TE 3. |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 4 | ACCURATE | H | Per-customer deployment orchestration across 3-5 concurrent versions, heterogeneous environments. |
| CP-08 | Disaster Recovery / BC | 4 | 3 | ACCURATE | H | Leverages components built in CP-01 and P3. Bounded once tooled. |
| CP-09 | Compliance Automation | 4 | 3 | ACCURATE | H | Compliance evidence pipeline for SOC2/FedRAMP/HIPAA. Bounded framework build. |
| CP-10 | Security Operations | 4 | 4 | ACCURATE | M | Falco + Trivy + vulnerability scanning. TE depends on whether Phase 1 scope includes 24/7 SOC build or only detection tooling. |

**P1 Phase 1 Averages (verified by CC1):** RD = 4.4 (44/10), TE = 4.0 (40/10). Both confirmed arithmetically correct.

### 1.2 P2 Application Logic (AL01 through AL10)

**Source reviews:** RP2a (AL01-AL05), RP2b (AL06-AL10)

All 10 P2 subsegments are confirmed ACCURATE for Phase 1. P2 is the lowest-effort plane in Phase 1 because most application logic is tier-invariant -- the business logic code runs identically regardless of deployment tier. Phase 1 work concentrates in AL03 (API Gateway migration), AL05 (message bus swap), AL09 (AI orchestration endpoint integration), and AL10 (test infrastructure rebuild).

| ID | Subsegment | Phase 1 RD | Phase 1 TE | Verdict | Confidence | Notes |
|:---:|---|:---:|:---:|---|:---:|---|
| AL01 | Service Decomposition | 1 | 2 | ACCURATE | H | Service boundaries unchanged. Cloud DNS to CoreDNS/Consul swap only. |
| AL02 | Business Logic / Domain | 1 | 1 | ACCURATE | H | Zero refactoring. Largest codebase, no changes needed. Minor startup-sequence caveat for on-premises infrastructure readiness. |
| AL03 | API Gateway / Edge Routing | 3 | 3 | ACCURATE | H | Replace managed API Gateway with Kong/APISIX/Envoy Gateway. TLS termination and auth integration must be self-configured. |
| AL04 | Data Access / ORM / Caching | 1 | 2 | ACCURATE | H | ORM abstracts database; connection strings change, code does not. |
| AL05 | Background Jobs / Async / EDA | 3 | 3 | ACCURATE | H | Replace SQS/EventBridge with Kafka/NATS; Step Functions with Temporal. Event schema and dead-letter handling re-implementation. |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | ACCURATE | H | Circuit breakers and health probes are application-level. Minor adaptation for self-hosted endpoints. |
| AL07 | Multi-Tenant Isolation | 1 | 1 | ACCURATE | H | Zero refactoring. Tenant isolation is application-code-level (middleware, row-level security). |
| AL08 | Observability Instrumentation | 2 | 2 | ACCURATE | H | Update OTLP exporter endpoints. OpenTelemetry SDK is tier-agnostic by design. |
| AL09 | AI/ML Orchestration | 2 | 3 | ACCURATE | H | Agent orchestration code (LangGraph, MCP, guardrails) is portable. Main work: integrate with customer inference endpoints, self-hosted Temporal, self-hosted Langfuse. Testing across new dependency topology is the bulk of effort. |
| AL10 | Testing / Contract Testing | 3 | 4 | ACCURATE | H | **[D]** flag. Build entirely new test infrastructure for on-prem environments. Large surface area drives effort above difficulty. |

**P2 Phase 1 Averages (verified by CC1):** RD = 1.9 (19/10), TE = 2.3 (23/10). Both confirmed arithmetically correct.

### 1.3 P3 Data Plane (DS1 through DS10)

**Source reviews:** RP3a (DS1-DS5), RP3b (DS6-DS10)

All 10 P3 subsegments are confirmed ACCURATE for Phase 1. P3 is the second-largest investment area after P1, accounting for approximately 20-40 person-months of one-time engineering. The difficulty distribution spans a wider range than P1 (RD 2-4 versus P1's 4-5), with the primary cost drivers being DS1 (Patroni PostgreSQL HA), DS6 (Strimzi Kafka), and DS10 (RAG pipeline orchestration).

| ID | Subsegment | Phase 1 RD | Phase 1 TE | Verdict | Confidence | Notes |
|:---:|---|:---:|:---:|---|:---:|---|
| DS1 | Relational Database HA | 4 | 4 | ACCURATE | H | Replace RDS Multi-AZ with CloudNativePG + Patroni. Streaming replication, automatic failover, WAL archiving, PgBouncer, pgBackRest. |
| DS2 | NoSQL / Document Store | 3 | 3 | ACCURATE | H | Replace DynamoDB/CosmosDB with MongoDB Community (Percona Operator) or ScyllaDB. |
| DS3 | Caching Layer | 3 | 2 | ACCURATE | H | Replace ElastiCache with Redis Sentinel/Cluster. Relatively straightforward, bounded surface. RD correctly one point above DS4. |
| DS4 | Object / Blob Storage | 2 | 2 | ACCURATE | H | Replace S3 with MinIO. Well-documented S3-compatible API, Helm deployment. |
| DS5 | Message Queuing (Simple) | 2 | 2 | ACCURATE | H | Replace SQS with RabbitMQ or NATS. Simplest data service to self-host. |
| DS6 | Event Streaming (Kafka) | 4 | 4 | ACCURATE | H | Replace MSK with Strimzi Kafka. KRaft configuration, partition strategy, ISR tuning. 259 GB/day disk at reference throughput. |
| DS7 | Search / Full-Text Index | 4 | 3 | ACCURATE | H | Replace OpenSearch Service with self-hosted OpenSearch/Elasticsearch. JVM heap tuning, shard strategy. Operationally demanding but bounded. |
| DS8 | Vector Database | 4 | 3 | ACCURATE | H | Replace managed Pinecone/pgvector with self-hosted Milvus or Qdrant. HNSW/IVF index config. Emerging domain with limited institutional knowledge. |
| DS9 | Embedding Pipeline (GPU) | 3 | 3 | ACCURATE | H | Customer provides GPU; ISV deploys embedding model serving. Correctly reduced from original 5/5 because GPU hardware is customer scope. |
| DS10 | RAG Pipeline Orchestration | 3 | 4 | ACCURATE | H | 8-stage pipeline with integration points across DS8, DS9, and customer inference. Large surface area drives effort above difficulty. |

**P3 Phase 1 Averages (verified by CC1):** RD = 3.2 (32/10), TE = 3.0 (30/10). Both confirmed arithmetically correct.

### 1.4 P4 AI Model Plane (S1 through S8)

**Source review:** RP4a (S1, S6, S7, S8)

S2-S5 are customer scope (hardware, GPU drivers, inference engine, GPU scheduling) and rated "---" in the ratings file. Of the 4 active ISV-scope subsegments, 3 are confirmed ACCURATE and 1 requires adjustment.

| ID | Subsegment | Phase 1 RD | Phase 1 TE | Verdict | Confidence | Notes |
|:---:|---|:---:|:---:|---|:---:|---|
| S1 | Managed API Integration | 1 -> **2** | 2 | **ADJUST** | M | Auth re-implementation, Bedrock schema delta, error handling rewrite. See Section 2 below. |
| S2 | Self-Hosted Inference Engine | --- | --- | Customer scope | N/A | Customer operates vLLM/TGI. |
| S3 | GPU Hardware Infrastructure | --- | --- | Customer scope | N/A | Customer owns all GPU hardware. |
| S4 | GPU Driver / CUDA Stack | --- | --- | Customer scope | N/A | Customer manages driver stack. |
| S5 | Multi-Tenant GPU Scheduling | --- | --- | Customer scope | N/A | Customer manages GPU allocation. |
| S6 | Model Routing / Load Balancing | 2 | 2 | ACCURATE | H | LiteLLM proxy deployment + configuration. Production requirements (Redis, Prisma, health checks) add infrastructure overhead. |
| S7 | Inference Monitoring | 2 | 2 | ACCURATE | H | Application-layer TTFT/quality monitoring. SLO definition and alerting. No GPU-level monitoring (customer scope). |
| S8 | Model Lifecycle Management | 1 | 1 | ACCURATE | H | Customer manages model artifacts. ISV tracks availability and selects version in API calls. Minimal work. |

**P4 Phase 1 Averages (verified by CC1):** RD = 1.5 (6/4), TE = 1.75 (7/4, stated as 1.8 -- rounding convention artifact per CC1 D-1). After S1 adjustment: RD = 1.75 (7/4), TE = 1.75 (7/4).

---

## 2. Recommended Rating Changes

Only one Phase 1 rating adjustment was identified across all 34 active subsegments:

| Subsegment | Current RD/TE | Proposed RD/TE | Direction | Magnitude | Source | Confidence |
|---|:---:|:---:|---|:---:|---|:---:|
| S1 Managed API Integration | 1/2 | **2**/2 | RD upward | +1 | RP4a | Medium |

### Rationale for S1 RD 1 -> 2

The three-phase file characterizes S1 Phase 1 as "Same pattern, different endpoint," which understates the actual engineering work. Three factors drive the adjustment:

1. **Authentication re-implementation.** Cloud-native calls use cloud IAM tokens (AWS SigV4 for Bedrock, Azure AD tokens for Azure OpenAI, Google service account credentials for Vertex AI). Customer on-premises inference endpoints use fundamentally different auth mechanisms -- bearer tokens, mTLS, or basic auth depending on deployment. Re-implementing auth flows in the ISV's HTTP client layer is real engineering work, not a configuration change.

2. **Bedrock schema delta.** The Bedrock API does not use the standard OpenAI messages format -- the system prompt is a separate parameter, and inference configuration parameters are nested differently. ISVs migrating from Bedrock to vLLM's OpenAI-compatible endpoint must update request construction code, not just swap the base URL.

3. **Error handling rewrite.** Cloud providers return provider-specific HTTP error codes, structured error bodies, and rate limit headers. Self-hosted vLLM returns different error schemas without cloud-provider rate limit semantics. Retry logic and error normalization layers require rewriting.

**Mitigating factor:** vLLM's OpenAI-compatible API (`/v1/chat/completions`) reduces schema delta for ISVs already built against the OpenAI API format. ISVs migrating from Azure OpenAI (which uses OpenAI SDK format) face less delta than those migrating from Bedrock.

**Impact on aggregates:** S1 RD adjustment changes P4 Phase 1 average RD from 1.5 to 1.75. Phase 1 Total RD changes from 2.971 to 2.999 (both round to 3.0). The impact on effort estimates is negligible -- S1 TE remains 2.

---

## 3. Phase 1 Effort Estimates

### 3.1 Stated Estimates

| Plane | Avg RD | Avg TE | Estimated One-Time Investment | Key Cost Driver |
|---|:---:|:---:|---|---|
| P1 Control Plane | 4.4 | 4.0 | 40-80 person-months | Building entire platform stack from scratch |
| P2 Application Logic | 1.9 | 2.3 | 10-25 person-months | Test infrastructure rebuild (AL10), SDK swaps |
| P3 Data Plane | 3.2 | 3.0 | 20-40 person-months | Standing up every self-hosted data service |
| P4 AI Model Plane | 1.5 | 1.8 | 2-4 person-months | Endpoint integration changes |
| **Total** | **2.9** | **2.9** | **~72-149 person-months** | **P1 + P3 = ~80% of effort** |

### 3.2 Effort Plausibility Assessment (from RP1e)

**P1 Control Plane -- the dominant cost center:**

The 40-80 person-month range for P1 is derived from the TE distribution across 10 subsegments:

| TE Rating | Count | Band (person-months) | Subtotal Range |
|:---:|:---:|---|---|
| TE 5 | 2 (CP-01, CP-05) | 12+ months each | 24-36 |
| TE 4 | 6 (CP-02, CP-04, CP-06, CP-07, CP-10, CP-03) | 6-12 months each | 36-72 |
| TE 3 | 2 (CP-08, CP-09) | 2-6 months each | 4-12 |
| **Raw unconstrained total** | | | **64-120 person-months** |

The stated 40-80 range implies a **parallelization factor of 0.55-0.67x** applied to the raw total. This factor is plausible (5-8 engineer team with serial dependencies from CP-01) but **is not documented** in the ratings file.

**Dependency constraints on parallelization:**

The CP-01 dependency chain imposes forced serialization:
1. CP-01 (K8s foundation) must complete before CP-02 through CP-10 can be installed
2. CP-03 (IAM) must provide certificates to CP-04 (PKI)
3. CP-04 must issue certificates before CP-02 (mTLS) can enforce traffic policies
4. CP-06 (CI/CD) must be operational before CP-07 (deploy lifecycle) can be validated end-to-end

**Critical assessment of the range bounds:**

- **Lower bound (40 person-months):** Requires a 5-7 engineer team with strong pre-existing Kubernetes operations expertise, no learning-curve overhead, immediate CP-01 execution start, and no scope expansion from the 2026 mandatory technology migration calendar (Ingress NGINX EOL March 2026, Jaeger v1 EOL January 2026, FIPS 140-2 expiry September 2026). This is a best-case scenario, not a planning baseline.

- **Upper bound (80 person-months):** Assumes parallel workstreams with specialist staffing across security, networking, and observability domains. This is the more defensible planning estimate for a typical mid-size ISV. External evidence supports this: platform engineering build consensus is 12 months minimum with dedicated teams of 6-10 engineers (72-120 person-months), and the Shadow-Soft FedRAMP case study achieved a subset of the Phase 1 build in 6 months with an experienced partner.

- **Learning-curve uplift (not included):** For an ISV whose engineers have deep cloud-native experience but no prior on-premises delivery exposure, a 20-30% learning-curve uplift is typical, pushing the range to 48-104 person-months.

**Weakest assumption:** The parallelization factor. If the ISV team is smaller (3-4 engineers) or serial dependencies are more constraining than modeled, elapsed calendar time increases even if total person-months stays constant. The ratings file does not document this conversion.

### 3.3 TE Confidence by Subsegment (from RP1e)

Three P1 subsegments carry Medium confidence TE assignments that could shift the aggregate by +/-10-15%:

| ID | Current TE | Re-derived TE | Confidence | Direction if Adjusted |
|:---:|:---:|:---:|:---:|---|
| CP-03 | 4 | 3-4 | M | Experienced IAM teams could achieve TE 3 (downward) |
| CP-06 | 4 | 3-4 | M | Mature CI/CD tooling could achieve TE 3 (downward) |
| CP-10 | 4 | 4 | M | Confirmed, but scope depends on SOC inclusion |

If CP-03 and CP-06 are adjusted to TE 3 (for experienced teams), the P1 average TE drops from 4.0 to approximately 3.8, reducing the aggregate estimate by 15-20%.

### 3.4 Other Planes

**P2 (10-25 person-months):** Arithmetically consistent with TE distribution (CC1 verified). Four subsegments at TE 1 (zero or minimal refactoring), four at TE 2-3, two at TE 3-4. The largest single item is AL10 (test infrastructure rebuild, TE 4).

**P3 (20-40 person-months):** Confirmed plausible under parallel execution by RP3c. Lower bound may be tight for complex storage topologies. The largest items are DS1 (Patroni, TE 4), DS6 (Strimzi Kafka, TE 4), and DS10 (RAG pipeline, TE 4).

**P4 (2-4 person-months):** Arithmetically consistent. Three subsegments at TE 2 (2-8 person-weeks each), one at TE 1. Sequential total approximately 4 months; parallel execution compresses to 2-4 months.

### 3.5 Arithmetic Verification (from CC1)

| Check | Stated | Computed | Status |
|---|---|---|---|
| P1 Phase 1 avg RD | 4.4 | 44/10 = 4.4 | Verified |
| P1 Phase 1 avg TE | 4.0 | 40/10 = 4.0 | Verified |
| P2 Phase 1 avg RD | 1.9 | 19/10 = 1.9 | Verified |
| P2 Phase 1 avg TE | 2.3 | 23/10 = 2.3 | Verified |
| P3 Phase 1 avg RD | 3.2 | 32/10 = 3.2 | Verified |
| P3 Phase 1 avg TE | 3.0 | 30/10 = 3.0 | Verified |
| P4 Phase 1 avg RD | 1.5 | 6/4 = 1.5 | Verified |
| P4 Phase 1 avg TE | 1.8 | 7/4 = 1.75 | Minor rounding (D-1) |
| Phase 1 Total RD | 2.9 | 101/34 = 2.971 | Minor rounding error (D-2): rounds to 3.0, stated as 2.9 |
| Phase 1 Total TE | 2.9 | 100/34 = 2.941 | Verified |

**Summary:** All Phase 1 plane-level averages are arithmetically correct. One minor rounding discrepancy exists (Total RD: 2.971 stated as 2.9, should round to 3.0). The effort estimates are arithmetically consistent with the TE ratings under parallel execution assumptions.

---

## 4. Phase 1 Interview Questions

The following questions were generated by review agents to validate Medium-confidence findings. They are organized by interview target role and limited to Phase 1 scope.

### 4.1 VP Engineering / CTO

1. **Phase 1 aggregate effort (RP1e):** "For your initial on-premises refactoring -- the one-time engineering investment to make your cloud-native SaaS portable to customer-hosted Kubernetes -- how many total person-months did the project consume, and over how many calendar months? How large was the team?"

2. **CP-03 IAM familiarity (RP1e):** "What is the ISV's current identity provider familiarity -- have they previously operated Keycloak or Dex in production? Did this prior experience materially reduce the Phase 1 IAM build timeline?"

3. **CP-10 SOC scope (RP1e):** "Does the ISV plan to build 24/7 SOC capability in Phase 1, or is CP-10 scoped to runtime detection tooling plus incident runbooks?"

### 4.2 Principal Engineer / Platform Architecture

4. **S1 API migration (RP4a):** "When your team replaced Bedrock or Azure OpenAI calls with your customer's vLLM endpoints, how long did it take to re-implement authentication, update error handling, and validate response schema compatibility? Was it days, weeks, or months?"

5. **AL02 startup sequence (RP2a):** "When you moved your application to on-premises, did you have to write infrastructure-readiness logic into application startup? How many person-days did that add, and which team owned it -- platform or application?"

6. **AL05 Temporal migration (RP2a):** "For your on-premises Temporal deployment, how frequently do Temporal version upgrades require changes to your workflow SDK code or configuration files? And who owns your dead-letter queue handling code -- platform engineers or backend engineers?"

### 4.3 Platform Engineering Director

7. **CP-04 PKI greenfield (RP1e):** "Does the ISV have a pre-existing PKI hierarchy or is this greenfield? Greenfield pushes toward TE 5."

8. **CP-06 GitOps scale (RP1e):** "How many target deployment environments does the GitOps architecture need to support at Phase 1 completion -- 3 environments or 50?"

9. **AL03 gateway ownership (RP2a):** "In your on-premises deployments, what fraction of your API gateway maintenance work (Kong/Traefik plugin upgrades, TLS rotation, routing config updates) is handled by platform engineers vs. backend engineers? This split determines whether it belongs in P1 or AL03."

### 4.4 Site Reliability Engineer / AI Platform Engineer

10. **S6 routing maintenance (RP4a):** "How many hours per week does your team spend updating routing configurations and health check thresholds in response to customer-side inference endpoint changes? Is this growing linearly with customer count?"

11. **S7 TTFT monitoring (RP4a):** "How much time per week does your team spend tracking inference quality and TTFT compliance across customer endpoints -- specifically excluding GPU-level monitoring that the customer owns? Does that effort scale linearly with customer count, or does automation absorb most of it?"

12. **AL04 connection topology (RP2a):** "For your on-premises PostgreSQL HA setup with Patroni, how many hours per month does your backend engineering team (not platform team) spend handling connection topology changes, Sentinel failover events, and related ORM-layer issues?"

### 4.5 Data Engineer / DBA

13. **DS8 vector DB operations (RP3b):** "How much engineering time do teams actually spend on Milvus or Qdrant version upgrades per release cycle, particularly for the Woodpecker WAL migration in Milvus 2.6 and index re-optimization after HNSW parameter changes?"

14. **DS7 search engine operations (RP3b):** "How much additional overhead does the Elastic Cloud on Kubernetes (ECK) operator add versus standalone Elasticsearch in managed K8s deployments -- specifically for rolling upgrades and persistent volume management?"

---

## 5. Revised Phase 1 Summary Table

Incorporating the single S1 RD adjustment and CC1 arithmetic corrections. Customer-scope subsegments (S2-S5) shown as "---" per original.

### All 38 Subsegments -- Phase 1 Ratings

| ID | Subsegment | Current RD | Proposed RD | Current TE | Proposed TE | Change |
|:---:|---|:---:|:---:|:---:|:---:|---|
| **P1 Control Plane** | | | | | | |
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | 5 | 5 | -- |
| CP-02 | Network Fabric / Ingress / Mesh | 5 | 5 | 4 | 4 | -- |
| CP-03 | IAM / RBAC | 4 | 4 | 4 | 4 | -- |
| CP-04 | Secrets / Certs / PKI | 5 | 5 | 4 | 4 | -- |
| CP-05 | Observability Infrastructure | 4 | 4 | 5 | 5 | -- |
| CP-06 | CI/CD Pipeline / GitOps | 4 | 4 | 4 | 4 | -- |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 5 | 4 | 4 | -- |
| CP-08 | Disaster Recovery / BC | 4 | 4 | 3 | 3 | -- |
| CP-09 | Compliance Automation | 4 | 4 | 3 | 3 | -- |
| CP-10 | Security Operations | 4 | 4 | 4 | 4 | -- |
| | **P1 Averages** | **4.4** | **4.4** | **4.0** | **4.0** | -- |
| **P2 Application Logic** | | | | | | |
| AL01 | Service Decomposition | 1 | 1 | 2 | 2 | -- |
| AL02 | Business Logic / Domain | 1 | 1 | 1 | 1 | -- |
| AL03 | API Gateway / Edge Routing | 3 | 3 | 3 | 3 | -- |
| AL04 | Data Access / ORM / Caching | 1 | 1 | 2 | 2 | -- |
| AL05 | Background Jobs / Async / EDA | 3 | 3 | 3 | 3 | -- |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | 2 | 2 | -- |
| AL07 | Multi-Tenant Isolation | 1 | 1 | 1 | 1 | -- |
| AL08 | Observability Instrumentation | 2 | 2 | 2 | 2 | -- |
| AL09 | AI/ML Orchestration | 2 | 2 | 3 | 3 | -- |
| AL10 | Testing / Contract Testing | 3 | 3 | 4 | 4 | -- [D] |
| | **P2 Averages** | **1.9** | **1.9** | **2.3** | **2.3** | -- |
| **P3 Data Plane** | | | | | | |
| DS1 | Relational Database HA | 4 | 4 | 4 | 4 | -- |
| DS2 | NoSQL / Document Store | 3 | 3 | 3 | 3 | -- |
| DS3 | Caching Layer | 3 | 3 | 2 | 2 | -- |
| DS4 | Object / Blob Storage | 2 | 2 | 2 | 2 | -- |
| DS5 | Message Queuing (Simple) | 2 | 2 | 2 | 2 | -- |
| DS6 | Event Streaming (Kafka) | 4 | 4 | 4 | 4 | -- |
| DS7 | Search / Full-Text Index | 4 | 4 | 3 | 3 | -- |
| DS8 | Vector Database | 4 | 4 | 3 | 3 | -- |
| DS9 | Embedding Pipeline (GPU) | 3 | 3 | 3 | 3 | -- |
| DS10 | RAG Pipeline Orchestration | 3 | 3 | 4 | 4 | -- |
| | **P3 Averages** | **3.2** | **3.2** | **3.0** | **3.0** | -- |
| **P4 AI Model Plane** | | | | | | |
| S1 | Managed API Integration | 1 | **2** | 2 | 2 | **RD +1** |
| S2 | Self-Hosted Inference Engine | --- | --- | --- | --- | Customer scope |
| S3 | GPU Hardware Infrastructure | --- | --- | --- | --- | Customer scope |
| S4 | GPU Driver / CUDA Stack | --- | --- | --- | --- | Customer scope |
| S5 | Multi-Tenant GPU Scheduling | --- | --- | --- | --- | Customer scope |
| S6 | Model Routing / Load Balancing | 2 | 2 | 2 | 2 | -- |
| S7 | Inference Monitoring | 2 | 2 | 2 | 2 | -- |
| S8 | Model Lifecycle Management | 1 | 1 | 1 | 1 | -- |
| | **P4 Averages (ISV scope)** | **1.5** | **1.75** | **1.75** | **1.75** | RD +0.25 |

### Revised Phase 1 Summary

| Plane | Avg RD (current) | Avg RD (proposed) | Avg TE | Estimated Investment | Status |
|---|:---:|:---:|:---:|---|---|
| P1 Control Plane | 4.4 | 4.4 | 4.0 | 40-80 person-months | No change |
| P2 Application Logic | 1.9 | 1.9 | 2.3 | 10-25 person-months | No change |
| P3 Data Plane | 3.2 | 3.2 | 3.0 | 20-40 person-months | No change |
| P4 AI Model Plane | 1.5 | 1.75 | 1.75 | 2-4 person-months | S1 RD +1 |
| **Total** | **2.97** | **3.00** | **2.94** | **~72-149 person-months** | Negligible impact |

**Note on Total RD:** The original stated Total RD of 2.9 was a minor rounding error identified by CC1 (D-2): the computed value is 2.971, which rounds to 3.0. After the S1 adjustment, the computed Total RD is 102/34 = 3.000 exactly.

---

## 6. Key Findings

1. **Phase 1 ratings are remarkably stable under review.** Of 68 Phase 1 rating cells (34 subsegments x 2 dimensions), only 1 requires adjustment (S1 RD: 1 to 2). This represents a 98.5% confirmation rate across all four planes, indicating the original ratings were well-calibrated against source material.

2. **The 80-person-month upper bound for P1 is more defensible than the 40-person-month lower bound.** The lower bound requires conditions (experienced team, no learning curve, immediate CP-01 execution, no 2026 migration calendar impact) that are unlikely to co-occur in a typical mid-size ISV. External evidence from platform engineering build timelines and migration case studies corroborates the upper-bound estimate. For planning purposes, the 80-person-month figure should be the reference point.

3. **The parallelization factor (0.55-0.67x) is the most consequential undocumented assumption.** The raw unconstrained total for P1 alone is 64-120 person-months. The conversion to 40-80 person-months depends on parallel execution assumptions that are sensitive to team size, serial dependency constraints (CP-01 gates everything), and the ISV's organizational structure. This factor should be documented explicitly in the ratings file.

4. **P1 + P3 = ~80% of Phase 1 effort is confirmed.** P1 (40-80 pm) + P3 (20-40 pm) = 60-120 person-months out of ~72-149 total. At the midpoint, this ratio is 81%. The cost concentration in infrastructure (P1) and data services (P3) drives the strategic implication: ISVs planning on-premises deployments need platform engineers and data infrastructure specialists, not additional application developers.

5. **Three M-confidence P1 subsegments (CP-03, CP-04, CP-10) could shift the P1 aggregate by +/-10-15%.** Interview validation of IAM experience (CP-03), PKI greenfield status (CP-04), and SOC scope inclusion (CP-10) would tighten the confidence interval on the P1 effort estimate. These are the highest-value interview targets for Phase 1 calibration.

---

## Sources

All source files are local to the ISV development research project unless otherwise noted.

| Document | Path | Role |
|---|---|---|
| three_phase_on_prem_ratings.md | `analysis/three_phase_on_prem_ratings.md` | Primary file under review |
| GT1_P1_ground_truth.md | `analysis/review/GT1_P1_ground_truth.md` | P1 ground truth extraction |
| GT2_P2_ground_truth.md | `analysis/review/GT2_P2_ground_truth.md` | P2 ground truth extraction |
| GT3_P3_ground_truth.md | `analysis/review/GT3_P3_ground_truth.md` | P3 ground truth extraction |
| GT4_P4_ground_truth.md | `analysis/review/GT4_P4_ground_truth.md` | P4 ground truth extraction |
| GT5_cross_reference_ground_truth.md | `analysis/review/GT5_cross_reference_ground_truth.md` | Cross-plane reference |
| RP1a_P1_infrastructure_core.md | `analysis/review/RP1a_P1_infrastructure_core.md` | CP-01 to CP-03 review |
| RP1b_P1_security_delivery.md | `analysis/review/RP1b_P1_security_delivery.md` | CP-04 to CP-06 review |
| RP1c_P1_operations_compliance.md | `analysis/review/RP1c_P1_operations_compliance.md` | CP-07 to CP-10 review |
| RP1e_P1_phase1_effort.md | `analysis/review/RP1e_P1_phase1_effort.md` | Phase 1 effort plausibility |
| RP2a_P2_service_architecture.md | `analysis/review/RP2a_P2_service_architecture.md` | AL01-AL05 review |
| RP2b_P2_resilience_ai_testing.md | `analysis/review/RP2b_P2_resilience_ai_testing.md` | AL06-AL10 review |
| RP3a_P3_traditional_data.md | `analysis/review/RP3a_P3_traditional_data.md` | DS1-DS5 review |
| RP3b_P3_streaming_ai_data.md | `analysis/review/RP3b_P3_streaming_ai_data.md` | DS6-DS10 review |
| RP4a_P4_isv_scope.md | `analysis/review/RP4a_P4_isv_scope.md` | S1, S6, S7, S8 review |
| CC1_math_audit.md | `analysis/review/CC1_math_audit.md` | Arithmetic verification |

All file paths are relative to: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/`
