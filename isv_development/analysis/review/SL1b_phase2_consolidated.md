# SL1b: Phase 2 (Per-Customer Customization) — Consolidated Review Findings

**Synthesis Layer:** SL1b — Phase 2 consolidation across all 4 planes
**Date:** 2026-02-19
**Source Files:** RP1d, RP2a, RP2b, RP3a, RP3b, RP3c, RP4a, CC4, GT2, three_phase_on_prem_ratings.md
**Scope:** Phase 2 ratings only — per-customer effort that repeats for each new deployment
**Responsibility Split:** Customer owns hardware (servers, GPUs, networking, storage, power, cooling). ISV owns ALL software and software-to-hardware adaptation.

---

## Executive Summary

Phase 2 per-customer ratings are broadly accurate across all four planes: no individual Phase 2 cell rating requires a numerical adjustment based on review agent findings. The ratings correctly identify P1 Control Plane (avg RD 3.0, TE 2.9) as the dominant per-customer cost driver at approximately 60% of total Phase 2 effort, while P2 Application Logic (avg RD 1.1, TE 1.2), P3 Data Plane (avg RD 1.6, TE 1.4), and P4 AI Model Plane (avg RD 1.0, TE 1.5) are correctly rated as low-effort configuration work. However, the aggregate Phase 2 effort estimate of 10--21 person-weeks per customer understates reality for two customer segments: (1) hardware-heterogeneous customers where P3 data service tuning reaches 3--6 person-weeks rather than 2--4, and (2) air-gapped or regulated-industry customers where P1 effort reaches 9--18 person-weeks rather than 6--14. Additionally, the Phase 2 section heading requires correction from "Per-Customer Hardware Customization" to "Per-Customer Customization: Software Adaptation to Customer Hardware" per CC4, and the DS9 Phase 3 FTE of 2.0--3.25 is carried from a pre-scope-split estimate and should be recomputed to approximately 0.5--1.0 FTE under customer-owns-GPU assumptions.

---

## 1. Consolidated Phase 2 Findings by Plane

### 1.1 P1 Control Plane (CP-01 through CP-10) — Source: RP1d

P1 Phase 2 is correctly identified as the highest-effort and highest-difficulty plane for per-customer work, with averages of RD 3.0 and TE 2.9. Every subsegment was reviewed individually, and all ten cell ratings were confirmed at their current values.

**CP-01 (K8s Cluster Lifecycle): RD=4, TE=4 — HOLD (M confidence)**
Virtualization heterogeneity (VMware vs. KVM vs. bare metal) generates materially different kubeadm/RKE2 configuration paths per customer. Replicated's Compatibility Matrix documents 65,981+ unique Kubernetes environment configurations across customer deployments. The Shadow-Soft case study provides a lower-bound data point of 4 person-weeks for a single customer deployment, which does not contradict TE=4 for a more complex engagement.
-- Source: RP1d § CP-01; GT1 citing F48, F58

**CP-02 (Network Fabric / Ingress / Mesh): RD=4, TE=4 — HOLD, possibly RD=5 in 2026 (H confidence)**
Network topology is the single most empirically supported source of per-customer variance. Multiple independent sources confirm that firewall rules, proxy requirements, and DNS architecture are categorically unique per site. The Ingress NGINX Controller was retired November 2025 with maintenance ending March 2026, forcing per-customer migration to the Kubernetes Gateway API. This is the most defensible Phase 2 rating in the entire document.
-- Source: RP1d § CP-02; GT1 citing F73, F76

**CP-03 (IAM / RBAC): RD=3, TE=3 — HOLD (M confidence)**
LDAP/SAML/OIDC federation configuration is a known, bounded engineering task. Keycloak-to-Okta SAML integration is documented at under one hour for straightforward cases, but enterprise deployments with custom role mappings scale substantially beyond that baseline. The Apple OPA acquisition (August 2025) creates policy-engine risk for ISVs dependent on OPA/Gatekeeper.
-- Source: RP1d § CP-03; GT1 citing F46

**CP-04 (Secrets / Certs / PKI): RD=3, TE=3 — CONSIDER RAISING to RD=4 for regulated industries (M confidence)**
Current rating is appropriate for the median customer. For customers with their own HSMs, PKCS#11 driver integration varies per vendor (SafeNet vs. Thales vs. nCipher) and is non-trivial per-customer work. FIPS 140-2 certificate validity expires September 2026, forcing FIPS 140-3 transition. Let's Encrypt 45-day certificate validity (effective May 2026) increases rotation frequency and per-customer cert-manager configuration complexity.
-- Source: RP1d § CP-04; GT1 citing F47

**CP-05 (Observability Infrastructure): RD=2, TE=2 — HOLD (H confidence)**
Per-customer work is primarily configuration: storage class sizing, Prometheus memory limits, retention policy setting. Kube-prometheus-stack consumes 15--35 GB of cluster RAM before application workloads; per-customer capacity calculation is bounded.
-- Source: RP1d § CP-05; GT1 citing F55d, F49

**CP-06 (CI/CD Pipeline / GitOps): RD=2, TE=2 — HOLD with air-gapped annotation (M confidence)**
For proxy-accessible customers, RD=2 and TE=2 are appropriate. For air-gapped customers, Replicated data shows a 60x time-to-install multiple (2 weeks vs. 2 hours). Air-gapped deployments should carry a TE=3 annotation for CP-06.
-- Source: RP1d § CP-06; GT1 citing F48, F58; Replicated Time-to-Install data

**CP-07 (Deploy Lifecycle / Rollback): RD=3, TE=3 — HOLD with regulated annotation (M confidence)**
79% of Kubernetes production issues originate from recent system changes. For customers with formal change management boards (government, healthcare), TE could reach 4 due to maintenance window negotiation and rollback drill validation requirements.
-- Source: RP1d § CP-07; Komodor 2025 Enterprise Kubernetes Report

**CP-08 (Disaster Recovery / BC): RD=3, TE=3 — HOLD (M confidence)**
Per-customer DR work is bounded: backup storage target discovery, RTO/RPO negotiation, and validation test execution. This is procedural engineering at Phase 2, not architectural work.
-- Source: RP1d § CP-08; GT1 citing F70

**CP-09 (Compliance Automation): RD=3, TE=3 — HOLD with FedRAMP annotation (M confidence)**
For SOC 2 and HIPAA customers, RD=3/TE=3 is appropriate. FedRAMP customers represent a meaningful outlier where per-customer compliance configuration can consume weeks to months. Data sovereignty enforcement is rated 1/5 difficulty on-premises (data never leaves customer infrastructure), which is a genuine Phase 2 advantage.
-- Source: RP1d § CP-09; GT1 citing F67

**CP-10 (Security Operations): RD=3, TE=2 — HOLD with SIEM annotation (M confidence)**
This is the only Phase 2 cell where TE is rated below RD. 73% of security practitioners cite false positives as the top SIEM challenge. Customers requiring Falco-to-SIEM integration (Splunk, QRadar) could push TE to 3. Customers without SIEM integration requirements fit TE=2.
-- Source: RP1d § CP-10; GT1 citing F71

### 1.2 P2 Application Logic (AL01 through AL10) — Sources: RP2a, RP2b

P2 Phase 2 averages RD 1.1 and TE 1.2, reflecting that application-layer code is architecturally invariant across customers. All ten Phase 2 ratings were confirmed ACCURATE with high or medium confidence.

**AL01--AL05 Phase 2: All RD=1, TE=1 — ACCURATE (H confidence)**
Service decomposition, business logic, API gateway, data access, and background jobs are ISV architecture decisions, not per-customer variables. The AL02 tier-invariance claim is supported: business logic difficulty is 2/5 across all tiers (CN, MK8s, OP) with Delta=0. The only documented on-premises code delta is a startup-sequence awareness pattern (~10--50 lines checking Consul/Vault/database readiness), which does not move Phase 2 ratings.
-- Source: RP2a § AL01--AL05 Phase 2

**AL06 (Resilience Patterns): RD=1, TE=1 — ACCURATE (H confidence)**
Resilience patterns are application-level. Circuit breaker thresholds may need minor tuning for customer network latency profiles, but this is environment variable configuration, not code.
-- Source: RP2b § AL06 Phase 2

**AL07 (Multi-Tenant Isolation): RD=1, TE=1 — ACCURATE (M confidence)**
Multi-tenancy is a software architecture problem rated tier-invariant at difficulty 3/5 across all tiers. Hardware heterogeneity does not affect isolation logic. The M confidence reflects a scope boundary caveat: if platform-layer isolation (namespace policies, network policies) blurs into AL07, the Phase 2 rating could be understated -- but under the current MECE boundary, those tasks belong to P1 CP-01/CP-02.
-- Source: RP2b § AL07 Phase 2; GT2 AL07 section

**AL08 (Observability Instrumentation): RD=1, TE=1 — ACCURATE (H confidence)**
OpenTelemetry instrumentation is standardized. Exporter endpoints are configured by P1, not per-customer application code.
-- Source: RP2b § AL08 Phase 2

**AL09 (AI/ML Orchestration / Agent Pipelines): RD=1, TE=2 — ACCURATE (H confidence)**
Per-customer variation is which models the customer hosts: different model catalogs, context window sizes, endpoint URLs, rate limits. Feature flags for model-dependent capabilities. This is configuration per customer, not code change. TE=2 (2--5 person-days) reflects the real work of mapping model availability to feature flags.
-- Source: RP2b § AL09 Phase 2

**AL10 (Testing / Contract Testing): RD=2, TE=2 — ACCURATE (H confidence)**
Validation testing per customer's specific environment: smoke tests, integration verification, performance baseline. Per-customer test *runs*, not per-customer test *code*. The TE=2 is appropriate for running and validating a pre-built test suite against a new customer environment.
-- Source: RP2b § AL10 Phase 2

### 1.3 P3 Data Plane (DS1 through DS10) — Sources: RP3a, RP3b, RP3c

P3 Phase 2 averages RD 1.6 and TE 1.4, reflecting that per-customer data service work is primarily parameter tuning against customer hardware profiles. All ten individual cell ratings were confirmed ACCURATE, but the aggregate effort estimate of 2--4 person-weeks is understated.

**DS1 (Relational DB HA): RD=2, TE=2 — ACCURATE (H confidence)**
PostgreSQL parameter tuning (shared_buffers, work_mem, wal_buffers) for customer memory profiles, plus storage layout for customer disk topology and backup target configuration. This is bounded DBA work, well within 2--5 person-days when the ISV has pre-built configuration templates.
-- Source: RP3a § DS1 Phase 2

**DS2 (NoSQL / Document Store): RD=2, TE=1 — ACCURATE (H confidence)**
WiredTiger cache sizing is a single-parameter adjustment per customer's available memory. Minor tuning, sub-2 person-days.
-- Source: RP3a § DS2 Phase 2

**DS3 (Caching Layer): RD=1, TE=1 — ACCURATE (H confidence)**
Redis maxmemory config based on customer's available RAM. Standard across customers. Parameter-file configuration.
-- Source: RP3a § DS3 Phase 2

**DS4 (Object / Blob Storage): RD=1, TE=1 — ACCURATE (H confidence)**
MinIO erasure coding configured for customer's disk count. Minimal variation. Parameter-file configuration.
-- Source: RP3a § DS4 Phase 2

**DS5 (Message Queuing): RD=1, TE=1 — ACCURATE (H confidence)**
Standard configuration. Persistence settings for customer's disk. Parameter-file configuration.
-- Source: RP3a § DS5 Phase 2

**DS6 (Event Streaming - Kafka): RD=2, TE=2 — ACCURATE (H confidence)**
Kafka log.dirs configured for customer's disk topology, broker memory sizing, replication factor based on customer's node count. TE=2 is achievable with pre-built configuration templates. Without templates, partition strategy recalculation for customers with different broker node counts (3-node vs. 6-node) is non-trivial reconfiguration, not a parameter swap.
-- Source: RP3b § DS6 Phase 2; RP3c § 5.2

**DS7 (Search / Full-Text Index): RD=2, TE=1 — ACCURATE (H confidence)**
JVM heap sized to customer's available memory. Shard count based on data volume estimate. Bounded configuration work.
-- Source: RP3b § DS7 Phase 2

**DS8 (Vector Database): RD=2, TE=2 — ACCURATE (M confidence)**
Index size and segment configuration based on customer data volume and available memory. HNSW parameters may need tuning per customer latency requirements. HNSW tuning is not a configuration file change when customer vector corpus sizes trigger full re-indexing (3--6 hours per 160M vectors). TE=2 is defensible only if the ISV has pre-defined customer data volume tiers with pre-validated HNSW parameter sets.
-- Source: RP3b § DS8 Phase 2; RP3c § 5.2; F45 citing HNSW build time data

**DS9 (Embedding Pipeline - GPU): RD=2, TE=2 — ACCURATE (M confidence)**
Configure embedding batch size and concurrency for customer's GPU allocation. Validate embedding model compatibility with customer's GPU generation (L4 vs. A100 vs. H100). Batch size and concurrency tuning across GPU generations is empirical work requiring the ISV to have pre-built GPU-tier-specific configuration templates -- a hidden Phase 1 dependency.
-- Source: RP3b § DS9 Phase 2; RP3c § 5.2; F37 citing GPU throughput data

**DS10 (RAG Pipeline Orchestration): RD=1, TE=1 — ACCURATE (H confidence)**
RAG pipeline config is standardized. Endpoint URLs for customer's embedding and inference services. Parameter-file configuration.
-- Source: RP3b § DS10 Phase 2

### 1.4 P4 AI Model Plane (ISV Scope: S1, S6, S7, S8) — Source: RP4a

P4 Phase 2 averages RD 1.0 and TE 1.5 (ISV-scope subsegments only). S2--S5 are customer scope across all phases (confirmed in CC4). All four ISV-scope Phase 2 ratings were confirmed ACCURATE.

**S1 (Managed API Integration): RD=1, TE=2 — ACCURATE (H confidence)**
Map to customer's inference endpoint URLs, authentication method (bearer token, mTLS, basic auth vs. cloud IAM), and API schema. Each customer may expose different model APIs. TE=2 (2--5 person-days) reflects the real work of per-customer endpoint configuration and auth method adaptation.
-- Source: RP4a § S1 Phase 2

**S6 (Model Routing / Load Balancing): RD=1, TE=2 — ACCURATE (H confidence)**
Configure LiteLLM routing for customer's available models -- different model catalogs, capacity, failover options. This is model-list configuration per customer, not routing logic redesign.
-- Source: RP4a § S6 Phase 2

**S7 (Inference Monitoring): RD=1, TE=1 — ACCURATE (H confidence)**
Set SLO thresholds based on customer's inference service performance characteristics. Threshold configuration per customer.
-- Source: RP4a § S7 Phase 2

**S8 (Model Lifecycle Management): RD=1, TE=1 — ACCURATE (H confidence)**
Inventory which models the customer provides. Version compatibility verification. Documentation and validation work, minimal engineering effort.
-- Source: RP4a § S8 Phase 2

---

## 2. Recommended Rating Changes

### 2.1 Individual Phase 2 Cell Ratings

No individual Phase 2 cell rating requires a numerical adjustment. All 38 Phase 2 ratings (including S2--S5 customer-scope markers) were confirmed ACCURATE or HOLD by their respective review agents.

### 2.2 Annotations Required

The following cells should carry annotations for specific customer segments:

| Subsegment | Current RD/TE | Annotation | Affected Customer Segment | Source |
|---|:---:|---|---|---|
| CP-02 | 4/4 | RD may warrant elevation to 5 in 2026 | All customers (Ingress NGINX EOL) | RP1d |
| CP-04 | 3/3 | Consider RD=4, TE=3 | Regulated industries with HSMs | RP1d |
| CP-06 | 2/2 | TE=3 for air-gapped customers | Air-gapped deployments | RP1d |
| CP-07 | 3/3 | TE could reach 4 | Regulated customers (CAB, maintenance windows) | RP1d |
| CP-09 | 3/3 | TE could reach 4 | FedRAMP customers | RP1d |
| CP-10 | 3/2 | TE=3 when SIEM integration required | Customers with Splunk/QRadar | RP1d |

### 2.3 Aggregate Effort Estimate Adjustments

| Plane | Current Estimate | Proposed Revision | Basis | Source |
|---|---|---|---|---|
| P3 Data Plane | 2--4 person-weeks | 3--6 person-weeks | Hardware-heterogeneous customers with novel storage topologies, atypical broker node counts, large vector corpora, or GPU generations outside pre-tested matrix | RP3c |
| P1 Control Plane | 6--14 person-weeks | 9--18 person-weeks (air-gapped); 6--14 retained for connected | Air-gapped deployments add ~60x to install time per Replicated data | RP1d |
| **Total** | **10--21 person-weeks** | **12--25 person-weeks (median); 15--30 person-weeks (air-gapped/regulated)** | P3 upward revision plus customer-segment annotations | RP1d, RP3c |

### 2.4 Document Corrections Required

| Item | Current Text | Proposed Correction | Source |
|---|---|---|---|
| Phase 2 section heading | "Per-Customer Hardware Customization" | "Per-Customer Customization: Software Adaptation to Customer Hardware" | CC4 |
| DS9 Phase 3 FTE | 2.0--3.25 FTE | ~0.5--1.0 FTE (ISV-scope only, excluding GPU hardware lifecycle tasks that are customer scope) | CC4 |

---

## 3. Revised Phase 2 Summary Table

### All 38 Subsegments — Phase 2 Ratings

**P1: Control Plane**

| ID | Subsegment | RD | TE | Review Verdict | Confidence | Annotations |
|:---:|---|:---:|:---:|---|---|---|
| CP-01 | K8s Cluster Lifecycle | 4 | 4 | HOLD | M | -- |
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 4 | HOLD | H | RD may reach 5 in 2026 (Ingress NGINX EOL) |
| CP-03 | IAM / RBAC | 3 | 3 | HOLD | M | OPA policy-engine risk (Apple acquisition) |
| CP-04 | Secrets / Certs / PKI | 3 | 3 | HOLD | M | Consider RD=4 for HSM customers; FIPS 140-3 transition |
| CP-05 | Observability Infrastructure | 2 | 2 | HOLD | H | -- |
| CP-06 | CI/CD Pipeline / GitOps | 2 | 2 | HOLD | M | Air-gapped = TE=3 |
| CP-07 | Deploy Lifecycle / Rollback | 3 | 3 | HOLD | M | Regulated customers: TE could reach 4 |
| CP-08 | Disaster Recovery / BC | 3 | 3 | HOLD | M | -- |
| CP-09 | Compliance Automation | 3 | 3 | HOLD | M | FedRAMP customers: TE could reach 4 |
| CP-10 | Security Operations | 3 | 2 | HOLD | M | SIEM integration customers: TE=3 |
| | **P1 Phase 2 Averages** | **3.0** | **2.9** | | | **6--14 pw (connected); 9--18 pw (air-gapped)** |

**P2: Application Logic**

| ID | Subsegment | RD | TE | Review Verdict | Confidence | Annotations |
|:---:|---|:---:|:---:|---|---|---|
| AL01 | Service Decomposition / Comm | 1 | 1 | ACCURATE | H | -- |
| AL02 | Business Logic / Domain | 1 | 1 | ACCURATE | H | Startup-sequence caveat (minor) |
| AL03 | API Gateway / Edge Routing | 1 | 1 | ACCURATE | H | -- |
| AL04 | Data Access / ORM / Caching | 1 | 1 | ACCURATE | H | -- |
| AL05 | Background Jobs / Async / EDA | 1 | 1 | ACCURATE | H | -- |
| AL06 | Resilience Patterns / Runtime | 1 | 1 | ACCURATE | H | Minor timeout tuning for network latency |
| AL07 | Multi-Tenant Isolation | 1 | 1 | ACCURATE | M | Scope boundary caveat (platform vs. app isolation) |
| AL08 | Observability Instrumentation | 1 | 1 | ACCURATE | H | -- |
| AL09 | AI/ML Orchestration / Pipelines | 1 | 2 | ACCURATE | H | Model availability mapping per customer |
| AL10 | Testing / Contract Testing | 2 | 2 | ACCURATE | H | Per-customer test runs, not code |
| | **P2 Phase 2 Averages** | **1.1** | **1.2** | | | **1--2 person-weeks** |

**P3: Data Plane**

| ID | Subsegment | RD | TE | Review Verdict | Confidence | Annotations |
|:---:|---|:---:|:---:|---|---|---|
| DS1 | Relational Database HA | 2 | 2 | ACCURATE | H | Requires pre-built config templates for TE=2 |
| DS2 | NoSQL / Document Store | 2 | 1 | ACCURATE | H | -- |
| DS3 | Caching Layer | 1 | 1 | ACCURATE | H | -- |
| DS4 | Object / Blob Storage | 1 | 1 | ACCURATE | H | -- |
| DS5 | Message Queuing (Simple) | 1 | 1 | ACCURATE | H | -- |
| DS6 | Event Streaming (Kafka) | 2 | 2 | ACCURATE | H | Partition strategy recalc for atypical node counts |
| DS7 | Search / Full-Text Index | 2 | 1 | ACCURATE | H | -- |
| DS8 | Vector Database | 2 | 2 | ACCURATE | M | HNSW re-index risk for large corpora (3--6 hrs/160M vectors) |
| DS9 | Embedding Pipeline (GPU) | 2 | 2 | ACCURATE | M | GPU-tier templates are hidden Phase 1 dependency |
| DS10 | RAG Pipeline Orchestration | 1 | 1 | ACCURATE | H | -- |
| | **P3 Phase 2 Averages** | **1.6** | **1.4** | | | **2--4 pw (standard); 3--6 pw (hardware-heterogeneous)** |

**P4: AI Model Plane**

| ID | Subsegment | RD | TE | Review Verdict | Confidence | Annotations |
|:---:|---|:---:|:---:|---|---|---|
| S1 | Managed API Integration | 1 | 2 | ACCURATE | H | Auth method adaptation per customer endpoint |
| S2 | Self-Hosted Inference Engine | -- | -- | Customer scope | -- | -- |
| S3 | GPU Hardware Infrastructure | -- | -- | Customer scope | -- | -- |
| S4 | GPU Driver / CUDA Stack | -- | -- | Customer scope | -- | -- |
| S5 | Multi-Tenant GPU Scheduling | -- | -- | Customer scope | -- | -- |
| S6 | Model Routing / Load Balancing | 1 | 2 | ACCURATE | H | Model catalog config per customer |
| S7 | Inference Monitoring | 1 | 1 | ACCURATE | H | SLO threshold config per customer |
| S8 | Model Lifecycle Management | 1 | 1 | ACCURATE | H | Model inventory per customer |
| | **P4 Phase 2 Averages (ISV)** | **1.0** | **1.5** | | | **0.5--1 person-weeks** |

### Revised Phase 2 Summary

| Plane | Avg RD | Avg TE | Standard Customer Effort | Hardware-Heterogeneous / Regulated | Key Cost Driver |
|---|:---:|:---:|---|---|---|
| P1 Control Plane | 3.0 | 2.9 | 6--14 person-weeks | 9--18 pw (air-gapped) | Infrastructure adaptation to customer hardware/network/security |
| P2 Application Logic | 1.1 | 1.2 | 1--2 person-weeks | 1--2 pw (no change) | Validation testing, model availability mapping |
| P3 Data Plane | 1.6 | 1.4 | 2--4 person-weeks | 3--6 pw (novel hardware) | Performance tuning for customer's storage/memory |
| P4 AI Model Plane | 1.0 | 1.5 | 0.5--1 person-weeks | 0.5--1 pw (no change) | Endpoint configuration, model catalog mapping |
| **Total** | **1.8** | **1.8** | **~10--21 pw/customer** | **~14--27 pw/customer** | **P1 = ~60% of per-customer effort** |

---

## 4. Phase 2 Effort Estimate Consolidation

### 4.1 Current Estimate Assessment

The current total Phase 2 estimate of 10--21 person-weeks per customer is arithmetically consistent with the per-subsegment TE ratings. RP3c verified the arithmetic: applying TE band midpoints (TE=1 = 1 person-day; TE=2 = 3.5 person-days) across all 10 P3 subsegments yields approximately 20 person-days = 4 person-weeks sequential / 2 person-weeks parallel, consistent with the stated 2--4 range.

### 4.2 Where the Estimate Understates

**P3 Data Plane (RP3c finding):** The 2--4 person-week range is defensible for customers whose hardware profiles fall within a pre-tested configuration matrix. It understates effort by 25--50% for customers with:
- Novel storage topologies (non-standard RAID configurations affecting DS1)
- Atypical broker node counts requiring partition strategy recalculation (DS6)
- Large vector corpora requiring empirical HNSW tuning with multi-hour re-index cycles (DS8)
- GPU generations outside the ISV's pre-tested set requiring fresh batch-size/concurrency calibration (DS9)

RP3c proposes a revised P3 Phase 2 range of **3--6 person-weeks** for hardware-heterogeneous customers.

**P1 Control Plane (RP1d finding):** The 6--14 person-week range is plausible for a mature ISV (5+ deployments) with good automation tooling. It likely understates effort for:
- **First 3--4 customers:** Connsulting's 6-month initial deployment cycle and Replicated's 90-day-to-under-8-hour improvement trajectory both suggest automation ROI is non-linear. The estimate assumes the mature end of the curve.
- **Air-gapped customers:** Replicated data shows air-gapped installations require approximately 2 weeks vs. approximately 2 hours for online installations -- a 60x time multiple. RP1d proposes 9--18 person-weeks for air-gapped P1 Phase 2.
- **Regulated customers:** CP-04 (HSM integration), CP-07 (formal change management), CP-09 (FedRAMP authorization boundary), and CP-10 (SIEM integration) each individually could push their TE up by 1 point. Cumulative effect for a FedRAMP customer with HSMs and SIEM could add 2--4 person-weeks to the P1 total.

### 4.3 Key Dependencies Embedded in Phase 2 Estimates

Four Phase 2 TE=2 ratings in P3 carry hidden Phase 1 dependencies that, if unmet, inflate Phase 2 effort:

| Subsegment | Phase 2 TE | Hidden Dependency | If Unmet |
|---|:---:|---|---|
| DS1 | 2 | Pre-built PostgreSQL config templates for hardware tiers | DBA investigation per customer |
| DS6 | 2 | Kafka partition strategy templates for broker node counts | Full recalculation per customer |
| DS8 | 2 | Pre-validated HNSW parameter sets for data volume tiers | Empirical tuning + multi-hour re-index |
| DS9 | 2 | GPU-tier-specific batch/concurrency templates | Fresh empirical calibration per GPU model |

### 4.4 Proportionality Check

The 3:1 ratio of P1 Phase 2 effort (6--14 pw) to P3 Phase 2 effort (2--4 pw) is internally consistent with the G1 finding that P3 scales sublinearly while P1 scales linearly with customer count. This ratio holds as long as data service configuration templates are well-maintained between Phase 1 and Phase 2.
-- Source: RP3c § 5.4; G1_n_services_multiplier.md

---

## 5. Phase 2 Interview Questions by Role

The following questions are consolidated from all review agents and organized by target interview role. These are designed to elicit empirical validation of Phase 2 effort estimates from practitioners with direct per-customer deployment experience.

### 5.1 VP Engineering / Principal Engineer (Strategic Effort Validation)

1. **CP-01 (RP1d):** "For your most recent on-premises customer deployment, how many engineer-hours did initial Kubernetes cluster configuration take -- from first infrastructure access to a healthy control plane -- and which virtualization layer was involved?"

2. **CP-03 (RP1d):** "When you integrate with a new on-premises customer's identity provider -- whether LDAP, SAML, or OIDC -- how many engineer-days does the federation configuration and role mapping typically require, and what percentage of integrations require multiple iterations due to customer directory structure complexity?"

3. **S1 (RP4a):** "When your team replaced Bedrock or Azure OpenAI calls with your customer's vLLM endpoints, how long did it take to re-implement authentication, update error handling, and validate response schema compatibility? Was it days, weeks, or months?"

4. **AL02 (RP2a):** "When you moved your application to on-premises, did you have to write infrastructure-readiness logic into application startup? How many person-days did that add, and which team owned it -- platform or application?"

### 5.2 Platform Engineer / DevOps Engineer (Per-Customer Deployment)

5. **CP-02 (RP1d):** "When deploying to a new on-premises customer site, how much time is consumed specifically by network configuration -- firewall rules, proxy bypass, DNS integration, and CNI configuration -- versus all other deployment tasks?"

6. **CP-04 (RP1d):** "For customers with their own PKI infrastructure or HSMs, how many engineer-hours does the certificate authority trust chain integration and Vault-to-HSM seal configuration typically require per customer, and have you encountered customers where PKI integration became a deployment blocker?"

7. **CP-06 (RP1d):** "What percentage of your on-premises customers require air-gapped deployment, and what is the total engineering time consumed by artifact bundle preparation and delivery for an air-gapped customer versus a proxy-accessible customer?"

8. **CP-07 (RP1d):** "When establishing the first deployment and rollback procedures with a new on-premises customer, how much time is consumed negotiating maintenance windows, change management processes, and validating the first rollback drill -- and does this differ materially between regulated and commercial customers?"

9. **S6 (RP4a):** "How many hours per week does your team spend updating routing configurations and health check thresholds in response to customer-side inference endpoint changes? Is this growing linearly with customer count?"

10. **CP-09 (RP1d):** "When deploying for a customer under FedRAMP versus a customer under SOC 2 only, how does the compliance configuration engineering time differ per deployment -- and does your team treat FedRAMP as a distinct deployment track with separate per-customer cost accounting?"

### 5.3 Data Platform Engineer / DBA (Data Service Tuning)

11. **DS1 (RP3c):** "When you deploy your data stack to a new customer environment, how much of the work is parameter-file changes vs. active investigation of the customer's storage controller, memory profile, or network topology?"

12. **DS6 (RP3c):** "Have you encountered customers where the disk configuration or node topology required non-trivial Kafka broker reconfiguration? How long did that take?"

13. **DS8 (RP3c):** "For customers with different data volumes, how much time does vector index HNSW parameter tuning add per customer deployment? Have you encountered recall degradation requiring full re-index?"

14. **DS9 (RP3c):** "For customers with different GPU generations (L4 vs. A100 vs. H100), how much time does embedding pipeline tuning add per customer deployment?"

15. **General (RP3c):** "Does your team have pre-built configuration templates for different hardware tiers, or do you calibrate parameters fresh for each customer? How does that choice affect per-customer deployment time?"

16. **General (RP3c):** "What is your actual per-customer deployment time for data services only -- excluding application code and Kubernetes platform setup -- for a new customer with a hardware profile you haven't seen before?"

### 5.4 SRE / AI Platform Engineer (Monitoring and Operations)

17. **CP-10 (RP1d):** "When integrating with a customer's existing SIEM -- Splunk, QRadar, or similar -- how many engineer-days does the Falco-to-SIEM integration, alert rule tuning, and false positive suppression require per customer?"

18. **S7 (RP4a):** "How much time per week does your team spend tracking inference quality and TTFT compliance across customer endpoints -- specifically excluding GPU-level monitoring that the customer owns? Does that effort scale linearly with customer count, or does automation absorb most of it?"

### 5.5 Backend Engineer (Application-Layer Validation)

19. **AL03 (RP2a):** "In your on-premises deployments, what fraction of your API gateway maintenance work (Kong/Traefik plugin upgrades, TLS rotation, routing config updates) is handled by platform engineers vs. backend engineers?"

20. **AL04 (RP2a):** "For your on-premises PostgreSQL HA setup with Patroni, how many hours per month does your backend engineering team (not platform team) spend handling connection topology changes, Sentinel failover events, and related ORM-layer issues?"

21. **AL05 (RP2a):** "For your on-premises Temporal deployment, how frequently do Temporal version upgrades require changes to your workflow SDK code or configuration files? And who owns your dead-letter queue handling code -- platform engineers or backend engineers?"

---

## 6. Key Findings

1. **All 38 Phase 2 cell ratings are confirmed ACCURATE or HOLD at their current values.** No individual Phase 2 subsegment requires a numerical rating change. The review agents achieved consensus across P1 (RP1d), P2 (RP2a, RP2b), P3 (RP3a, RP3b), and P4 (RP4a) that every cell is defensible against ground truth and external evidence. This is the strongest validation finding in the review.

2. **The aggregate Phase 2 effort estimate should be revised upward for non-standard customer profiles.** The current 10--21 person-weeks per customer is valid for a mature ISV deploying to a connected, commercially regulated customer with standard hardware. For air-gapped customers (P1 rises to 9--18 pw) and hardware-heterogeneous customers (P3 rises to 3--6 pw), the realistic range is 14--27 person-weeks per customer. The first 3--4 customer deployments will exceed even this range before automation maturity is established.

3. **P1 Control Plane dominates Phase 2 cost at ~60% of total effort, and this is structurally correct.** Infrastructure adaptation to each customer's hardware, network, and security environment is categorically customer-specific and cannot be fully automated without advance knowledge of the customer's environment. CP-02 (Network Fabric) is the single most variable subsegment, confirmed by the highest confidence rating (H) in the entire Phase 2 P1 table.

4. **Six P1 subsegments require customer-segment annotations rather than rating changes.** CP-02 (Ingress NGINX EOL), CP-04 (HSM customers), CP-06 (air-gapped), CP-07 (regulated maintenance windows), CP-09 (FedRAMP), and CP-10 (SIEM integration) all have well-defined customer segments where Phase 2 effort exceeds the median-case rating. The annotation approach preserves the median-case rating while documenting the tail risk.

5. **Four P3 Phase 2 ratings carry hidden Phase 1 dependencies on pre-built configuration templates.** DS1, DS6, DS8, and DS9 are each rated TE=2 (2--5 person-days) under the assumption that Phase 1 delivered hardware-tier-specific configuration templates. Without that Phase 1 investment, each becomes empirical reconfiguration work that could push individual cells to TE=3. This dependency should be documented in the Phase 1 deliverables checklist.

---

## 7. Sources

| Source File | Path | Phase 2 Data Contributed |
|---|---|---|
| RP1d: P1 Phase 2 Deep Dive | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1d_P1_phase2_deep_dive.md` | All CP-01--CP-10 Phase 2 reviews, effort estimate validation, 7 interview questions |
| RP2a: P2 Service Architecture | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2a_P2_service_architecture.md` | AL01--AL05 Phase 2 reviews, AL02 tier-invariance validation, 4 interview questions |
| RP2b: P2 Resilience/AI/Testing | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2b_P2_resilience_ai_testing.md` | AL06--AL10 Phase 2 reviews, AL07 scope boundary caveat |
| RP3a: P3 Traditional Data | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3a_P3_traditional_data.md` | DS1--DS5 Phase 2 reviews |
| RP3b: P3 Streaming/AI Data | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3b_P3_streaming_ai_data.md` | DS6--DS10 Phase 2 reviews |
| RP3c: P3 Effort Validation | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP3c_P3_effort_validation.md` | P3 Phase 2 aggregate effort revision (2--4 to 3--6 pw), hidden dependency analysis, 10 interview questions |
| RP4a: P4 ISV Scope | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4a_P4_isv_scope.md` | S1/S6/S7/S8 Phase 2 reviews, 3 interview questions |
| CC4: Scope Consistency | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/CC4_scope_consistency.md` | Phase 2 heading correction, DS9 FTE inconsistency, scope vocabulary check |
| GT2: P2 Ground Truth | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md` | P2 tier-invariance data, complexity ratios |
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` | Primary file under review -- all Phase 2 ratings and summary tables |

### External Sources Referenced by Review Agents

| Source | URL | Data Used By |
|---|---|---|
| Shadow-Soft ISV K8s Deployment | https://shadow-soft.com/content/msp-isv-kubernetes-deployment-160-hours | RP1d (4 pw deployment data point) |
| Replicated Time-to-Install | https://www.replicated.com/blog/instance-insights-time-to-install | RP1d (air-gap 60x multiple) |
| Replicated State of Self-Hosted 2025 | https://www.replicated.com/blog/introducing-the-state-of-self-hosted-survey-2025 | RP1d (90-day to 8-hour improvement) |
| Connsulting On-Premises Revenue Trap | https://www.connsulting.io/blog/the-on-prem-revenue-trap | RP1d (6-month initial cycle) |
| Spectro Cloud State of K8s 2025 | https://www.spectrocloud.com/state-of-kubernetes-2025 | RP1d (snowflake clusters) |
| Komodor Enterprise K8s Report 2025 | https://komodor.com/blog/komodor-2025-enterprise-kubernetes-report-finds-nearly-80-of-production-outages/ | RP1d (79% change-driven incidents) |
| vLLM OpenAI-Compatible Server | https://docs.vllm.ai/en/stable/serving/openai_compatible_server/ | RP4a (schema alignment for S1) |
