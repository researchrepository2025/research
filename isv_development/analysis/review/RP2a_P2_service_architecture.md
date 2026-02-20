# RP2a — P2 Application Logic Review: Service Architecture Subsegments (AL01–AL05)

**Review Agent:** Accuracy and Attribution Review Agent
**Date:** 2026-02-19
**Scope:** AL01, AL02, AL03, AL04, AL05 — Phase 1, Phase 2, and Phase 3 ratings from `analysis/three_phase_on_prem_ratings.md`
**Ground Truth Reference:** `analysis/review/GT2_P2_ground_truth.md` (extracted from `analysis/P2_application_logic.md`)
**Cross-Reference:** `analysis/review/GT5_cross_reference_ground_truth.md`

---

## Executive Summary

Across the 30 ratings reviewed (5 subsegments × 3 phases × 2 dimensions), 27 are accurate or directionally consistent with source data. Three ratings require attention: AL05 Phase 3 Relative Difficulty (RD=2 is conservative given the source data's Delta=3 classification and 2.0–4.1 FTE ops burden), the AL02 Phase 3 TE=4 rating which is accurately flagged as a divergence but needs stronger substantiation as a strategic finding, and the AL04 Phase 3 TE=2 which understates the on-premises connection topology burden documented in GT2. The AL02 tier-invariance claim (RD=1 across all phases) is substantially supported by source data with one documented caveat: startup-sequence awareness on-premises introduces a genuine, if modest, application-code delta that the current ratings do not capture. AL05's treatment of Kafka vs. SQS and Temporal vs. Step Functions migration is broadly accurate but the Phase 3 RD=2 rating undersells the Temporal configuration-drift burden documented in primary sources.

---

## AL01 — Service Decomposition and Inter-Service Communication

### Phase 1 (Initial Refactoring)

**Current rating:** RD=1, TE=2
**Re-derived rating:** RD=1, TE=2

Source data confirms service boundaries are unchanged during cloud-to-on-premises refactoring. [GT2] documents that CN and MK8s difficulty are both 2/5, rising to 3/5 on-premises — the delta is driven by Consul service discovery integration, not by service boundary redesign. Phase 1 is a one-time refactoring: service decomposition design work is identical across tiers. The only Phase 1 code change is swapping cloud DNS service discovery for Consul SDK libraries or CoreDNS configuration. GT2 quotes the on-premises FTE as "0.5–1.0 (design) + 0.3–0.5 (discovery ops)," which is well within TE=2 (<8 person-weeks one-time).

[STATISTIC] "The industry average is approximately 45 services per organization."
— F01: Microservices Architecture, via GT2
URL: https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/

[FACT] On-premises Consul requires "2–8 GB RAM and 2–4 CPU cores per server node." etcd has "no native DNS and no built-in health checking, requiring CoreDNS and external monitoring."
— P2_application_logic.md §3, AL01 Tier Analysis, via GT2

The Consul SDK integration is bounded refactoring work — it is a configuration surface swap, not an architectural redesign. RD=1 is accurate for the refactoring phase because the service graph is not redrawn.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 2 (Per-Customer Customization)

**Current rating:** RD=1, TE=1
**Re-derived rating:** RD=1, TE=1

The file states: "Same architecture across all customers. No per-customer changes." This is correct. Service decomposition is an ISV architecture decision, not a per-customer variable. The discovery layer (Consul) is configured in Phase 1 and then deployed identically per customer. No source data contradicts this.

[FACT] "REST holds approximately 90% market share; the emerging pattern is hybrid — gRPC internally, REST for external/browser clients."
— X4: Application Logic Three-Tier Comparison, via GT2
URL: https://www.gravitee.io/blog/choosing-right-api-architecture

This communication pattern is set at ISV architecture time, not per-customer. TE=1 (<2 person-days per customer) is consistent with a pure deployment stamp operation.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 3 (Ongoing Support)

**Current rating:** RD=1, TE=2
**Re-derived rating:** RD=1, TE=2

GT2 classifies AL01 as tier-sensitive with a Delta=1 (CN/MK8s at 2, OP at 3). The ongoing support dimension in Phase 3 records RD=1 — meaning the *incremental difficulty vs. cloud-native* is minimal. The TE=2 (0.1–0.3 FTE annual) reflects occasional bounded context refactoring and Consul client library upgrades. GT2 documents the source FTE range as "0.8–1.5" for on-premises ongoing operations, which aligns with TE=2.

[STATISTIC] "42% of organizations are consolidating from microservices" and microservices only deliver net value above 10–15 developers.
— W01S: Wave 1 Synthesis, via GT2
URL: https://www.javacodegeeks.com/2025/12/microservices-vs-modular-monoliths-in-2025-when-each-approach-wins.html

This consolidation trend may reduce AL01 ongoing work over time, but the 1–2 bounded context changes per year estimate embedded in TE=2 is defensible.

**Confidence:** High
**Verdict:** ACCURATE

---

## AL02 — Business Logic, Domain Services, and Request Validation

### The Tier-Invariance Question

The research question specifically asks: *Is AL02 truly RD=1 across all phases?* This requires direct engagement with the source data.

GT2 records AL02 difficulty as 2/5 across all three tiers (CN, MK8s, OP), classifying it as tier-invariant with Delta=0. The three_phase_on_prem_ratings.md translates this to RD=1 for all three phases. These two representations are measuring different things:

- GT2's "difficulty 2" is the absolute tier difficulty (scale: 1–5, where 1=trivial, 5=extreme)
- The three-phase file's RD=1 is the *relative* difficulty versus cloud-native (scale: 1–5, where 1=minimal/near-identical)

An absolute difficulty of 2 on-premises translates correctly to RD=1 relative to cloud-native when the cloud-native absolute difficulty is also 2. The translation is internally consistent.

**The one documented exception:** GT2 notes: "On-premises deployments require application code to implement graceful startup sequences that are aware of self-hosted infrastructure readiness (Consul healthy, Vault unsealed, database primary available)."
— P2_application_logic.md §3, AL02 Tier Analysis

This is a genuine on-premises application-code delta that does not exist cloud-native. However, it is a bounded startup-sequence pattern (typically 10–50 lines of code checking readiness endpoints), not a domain-logic change. The source document itself assigns difficulty 2 to all tiers despite this caveat, indicating the authors judged the delta as insufficient to move the rating. This judgment is reasonable but creates a minor gap: the ratings file documents RD=1 with "Zero refactoring" in Phase 1 and "Same code everywhere" in Phase 2, while the source acknowledges a small startup-sequence adaptation requirement.

[FACT] "Services should exclude HTTP-specific imports, operate using domain models rather than raw data structures, raise domain-specific exceptions (not HTTP exceptions), and remain reusable across different contexts."
— F75: MECE Abstraction Layer Framework, via GT2
URL: https://comp423-25s.github.io/resources/backend-architecture/0-layered-architecture/

[FACT] "Business logic difficulty is 3/5 across all tiers. Domain rules and workflow logic are platform-agnostic by design. The service layer operates independently of HTTP concerns and is equally portable to Lambda, Kubernetes pods, or bare-metal processes."
— F75: MECE Abstraction Layer Framework, via GT2
URL: https://comp423-25s.github.io/resources/backend-architecture/0-layered-architecture/

Note: GT2 itself flags an internal discrepancy — F75 quotes "3/5 across all tiers" while P2's summary matrix records 2/5. GT2 resolves this by treating the P2 §4 summary matrix as authoritative, recording 2/5 for all tiers. This internal inconsistency in the source data is not reflected in the three-phase ratings file.

---

### Phase 1 (Initial Refactoring)

**Current rating:** RD=1, TE=1
**Re-derived rating:** RD=1, TE=1 (with caveat)

The file states: "Zero refactoring. Business logic is the same code regardless of deployment tier." This is substantially accurate. The startup-sequence adaptation (Consul/Vault readiness) is real but bounded. It does not change domain logic, validation schemas, or RBAC policy code. TE=1 (<2 person-weeks) is arguably tight if a complex readiness chain must be built, but the source data does not quantify this work separately and it is partially covered under P1 (Control Plane) infrastructure bringup.

**Confidence:** High
**Verdict:** ACCURATE (with minor caveat on startup-sequence work — see interview question below)

**Interview question:** "When you moved your application to on-premises, did you have to write infrastructure-readiness logic into application startup? How many person-days did that add, and which team owned it — platform or application?"

---

### Phase 2 (Per-Customer Customization)

**Current rating:** RD=1, TE=1
**Re-derived rating:** RD=1, TE=1

GT2 records identical FTE ranges (3.0–6.0) across all three tiers for business logic, confirming per-customer business logic changes are driven by customer requirements, not deployment tier. No source contradicts RD=1, TE=1 for Phase 2.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 3 (Ongoing Support)

**Current rating:** RD=1, TE=4
**Re-derived rating:** RD=1, TE=4

This is the most strategically significant AL02 rating. The file explicitly flags it as **[D]** (divergence): "The largest absolute FTE in P2 — this is the ISV's core product development. But relative difficulty is 1 because the work is identical on cloud-native. Business logic doesn't change with deployment tier. High effort, minimal tier delta."

GT2 records the on-premises Phase 3 FTE as 3.0–6.0 — the largest single FTE block in P2 and identical to cloud-native. The RD=1 is accurate: this is product development cost, not on-premises overhead. The TE=4 (1.0–2.5 FTE annual, scale calibration) understates the actual FTE range (3.0–6.0 from GT2 maps more cleanly to TE=5, Very High, at 2.5+ FTE). However, the TE scale in the file applies to incremental on-premises work, not total work — and the 3.0–6.0 FTE is shared with cloud-native. The divergence flag correctly signals this is a planning trap.

[STATISTIC] "The FTE burden attributable to application logic ranges from 5.8–13.2 FTE cloud-native, to 9.4–19.8 FTE managed K8s, to 19.3–38.0 FTE on-premises."
— P2_application_logic.md §2, Executive Summary, via GT2

Business logic's 3.0–6.0 FTE is constant across all tiers — it is visible in this aggregate but not isolated as a tier cost. The rating is accurate in structure; the TE=4 label may understate the absolute magnitude for an ISV unfamiliar with the divergence flag convention.

**Confidence:** High
**Verdict:** ACCURATE

---

## AL03 — API Gateway, Edge Routing, and Service Mesh Integration

### Phase 1 (Initial Refactoring)

**Current rating:** RD=3, TE=3
**Re-derived rating:** RD=3, TE=3

GT2 records AL03 difficulty as CN=2, MK8s=3, OP=4 (Delta=2). Phase 1 is the one-time refactoring from cloud-native to on-premises. The key refactoring work: replace AWS API Gateway / APIM / Apigee with Kong, Traefik, or Envoy Gateway; configure TLS termination; implement distributed rate limiting via Redis Cluster; integrate Consul service routing. GT2 documents the FTE for on-premises as 1.5–3.0. A one-time build of this scope is consistent with TE=3 (2–6 person-months).

RD=3 is appropriate: this is not RD=4 (the ongoing on-premises absolute difficulty) because Phase 1 refactoring does not include the full ongoing operational burden — it is the initial gateway build and configuration, which is a bounded engineering project. The distinction between Phase 1 build effort and Phase 3 operational difficulty is correctly captured.

[FACT] "Ingress NGINX Controller, powering approximately 41% of internet-facing Kubernetes clusters, was officially retired November 2025, with best-effort maintenance ending March 2026."
— F73/X4, via GT2
URL: https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/

The Ingress NGINX retirement adds unplanned Phase 1 rework for ISVs still on that controller. RD=3 absorbs this without needing adjustment because Gateway API migration is already part of the refactoring scope.

[FACT] "Self-hosted API gateway cost: $10K–$50K+ annually. Managed API gateway starts at $3.50/million API calls (AWS)."
— F03: API Gateways and Service Communication, via GT2
URL: https://www.gravitee.io/blog/managed-vs-self-hosted-api-gateway-costs

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 2 (Per-Customer Customization)

**Current rating:** RD=1, TE=1
**Re-derived rating:** RD=1, TE=1

The file states: "Gateway config is standardized. Customer-specific TLS certs handled by P1 (CP-04)." This is correct per the scope boundary: gateway infrastructure operations are P1 (Control Plane), not AL03. The ISV's gateway configuration is a deployment stamp repeated per customer. Customer-specific TLS and certificate rotation is documented under CP-04 in the three-phase file. The scope split is internally consistent.

[FACT] "Kong achieves 130,014 RPS at P99 6.01ms on a single 16-vCPU node (proxy-only). Each plugin layer reduces Kong throughput 14–33%."
— F34: On-Premises API Gateway, via GT2
URL: https://developer.konghq.com/gateway/performance/benchmarks/

Per-customer gateway performance tuning (plugin selection, rate limit thresholds) is a configuration exercise bounded at TE=1, consistent with this performance data showing Kong's single-node capacity is unlikely to require per-customer architectural changes at typical ISV customer scale.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 3 (Ongoing Support)

**Current rating:** RD=2, TE=2
**Re-derived rating:** RD=2, TE=2

The file notes: "Gateway configuration updates with new API versions. Per-customer gateway config validation for major releases." GT2 records the on-premises FTE as 1.5–3.0 (Phase 3 ongoing), which maps to TE=3 or TE=4 at the high end. However, the TE=2 rating in the three-phase file reflects the *application-layer* gateway work (config updates, new route declarations) rather than infrastructure-layer gateway HA operations, which correctly belong in P1 (CP-02, Network Fabric). The 1.5–3.0 FTE in GT2 spans both infrastructure and application layer; the application-layer portion alone is smaller.

[FACT] "A peer-reviewed study found Istio sidecar adds +166% latency vs baseline, while Istio Ambient mode adds only +8%. Linkerd adds +33% latency and consumes an order of magnitude less CPU and memory than Istio at the data plane level."
— X4: Application Logic Three-Tier Comparison, via GT2
URL: https://arxiv.org/html/2411.02267v1

Service mesh selection in Phase 1 has ongoing Phase 3 consequences. A sidecar-based Istio selection imposes a 166% latency tax that the ISV may need to remediate via Ambient mode migration in Phase 3, adding unplanned effort. The rating does not explicitly call this out.

[FACT] "Service mesh adoption declined from 18% to 8% between Q3 2023 and Q3 2025."
— W01S: Wave 1 Synthesis, via GT2
URL: https://www.cncf.io/wp-content/uploads/2025/11/cncf_report_stateofcloud_111025a.pdf

**Confidence:** Medium
**Verdict:** ACCURATE (application-layer portion) — but the 1.5–3.0 FTE in GT2 spans infrastructure operations; the boundary allocation to P1 vs. AL03 is not fully documented.

**Interview question:** "In your on-premises deployments, what fraction of your API gateway maintenance work (Kong/Traefik plugin upgrades, TLS rotation, routing config updates) is handled by platform engineers vs. backend engineers? This split determines whether it belongs in P1 or AL03."

---

## AL04 — Data Access, ORM Layer, and Caching Integration

### Phase 1 (Initial Refactoring)

**Current rating:** RD=1, TE=2
**Re-derived rating:** RD=1, TE=2

GT2 confirms AL04 is tier-invariant with difficulty 2/5 across all three tiers (Delta=0). The Phase 1 refactoring work is: change connection strings from managed services (RDS Proxy, ElastiCache) to self-hosted equivalents (Patroni + HAProxy, Redis Sentinel); validate ORM compatibility with self-hosted PostgreSQL version; update connection pool configurations. No ORM code changes. GT2 FTE ranges are 0.5–1.0 (CN) vs. 0.75–1.5 (OP) — a marginal increase consistent with TE=2 (<8 person-weeks) for a one-time refactoring.

[FACT] "Prisma provides type-safe, auto-generated database clients with a schema-first approach and is the preferred choice for modern TypeScript backends in 2025. TypeORM's `synchronize: true` option is dangerous in production."
— F73: MECE ISV Developer Responsibility Framework, via GT2
URL: https://www.bytebase.com/blog/prisma-vs-typeorm/

The ORM abstraction layer is the key reason this subsegment is tier-invariant — Prisma and SQLAlchemy generate standard SQL that executes identically against PostgreSQL regardless of HA topology.

[FACT] "Amazon ElastiCache is a fully-managed service where 'all the administrative tasks associated with managing your Redis cluster (including monitoring, patching, backups, and automatic failover), are managed by Amazon.'"
— F75: MECE Abstraction Layer Framework, via GT2
URL: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/amazon-elasticache-and-self-managed-redis.html

The move from ElastiCache to Redis Sentinel involves one-time cache client configuration and failover handling code — bounded refactoring within TE=2.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 2 (Per-Customer Customization)

**Current rating:** RD=1, TE=1
**Re-derived rating:** RD=1, TE=1

The file states: "Connection strings from P3 config. No per-customer code changes." GT2 confirms identical FTE ranges across tiers (0.5–1.0 rising to 0.75–1.5 on-premises). The on-premises marginal FTE increase (0.25 FTE vs. cloud-native) is absorbed in P3 (Data Plane) configuration work, correctly separated from AL04. No source data contradicts this rating.

[FACT] "Spotahome Redis Operator last released January 2022; Bitnami Redis Helm Chart is the actively maintained alternative."
— X4: Application Logic Three-Tier Comparison, via GT2
URL: https://blog.palark.com/failure-with-redis-operator-and-redis-data-analysis-tools/

Per-customer operator selection is a P1/P3 platform decision, not an AL04 application-code decision. RD=1, TE=1 is correctly scoped.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 3 (Ongoing Support)

**Current rating:** RD=1, TE=2
**Re-derived rating:** RD=1, TE=2

The file notes: "ORM maintenance, connection pool tuning. Occasional migration for database version changes (triggered by P3 upgrades)." GT2 records on-premises FTE at 0.75–1.5 vs. cloud-native 0.5–1.0. This 0.25–0.5 FTE delta is the on-premises connection topology management cost (Patroni failover handling, Sentinel event awareness). TE=2 (0.1–0.3 FTE annual) slightly understates the documented 0.75–1.5 FTE range from GT2.

[FACT] "Patroni requires etcd or Consul as the distributed config store plus HAProxy for connection routing. Application code must handle Patroni topology changes and Sentinel failover events."
— P2_application_logic.md §3, AL04 Tier Analysis, via GT2

The Patroni topology-change handling and Sentinel failover event code is an ongoing maintenance item that extends slightly above TE=2. The GT2 range (0.75–1.5 FTE) better maps to TE=3 (0.3–1.0 FTE annual) for the application-code component. This is a minor understatement.

**Confidence:** Medium
**Verdict:** ADJUST (TE: 2 → 3, minor upward, driven by Patroni/Sentinel application-layer event handling documented in GT2)

**Interview question:** "For your on-premises PostgreSQL HA setup with Patroni, how many hours per month does your backend engineering team (not platform team) spend handling connection topology changes, Sentinel failover events, and related ORM-layer issues?"

---

## AL05 — Background Jobs, Async Processing, and Event-Driven Integration

This subsegment requires the most detailed examination because: (1) it has the second-largest tier Delta in the framework (Delta=3, tied with AL09); (2) the Kafka vs. SQS and Temporal vs. Step Functions migration paths are structurally different refactoring tasks; and (3) the Phase 3 RD rating is the most contested among the five subsegments reviewed.

### Phase 1 (Initial Refactoring)

**Current rating:** RD=3, TE=3
**Re-derived rating:** RD=3, TE=3

GT2 records AL05 as CN=1, MK8s=3, OP=4 (Delta=3). Phase 1 refactoring moves from difficulty=1 (cloud-native) to difficulty=4 (on-premises). The key replacements:
- AWS SQS / EventBridge → self-hosted Kafka (Strimzi) or NATS
- AWS Step Functions → Temporal (requiring Cassandra + Elasticsearch for production-scale persistence)
- AWS Glue Schema Registry → self-hosted Schema Registry or Confluent Schema Registry

[FACT] "Self-hosting Temporal requires Cassandra for persistence and Elasticsearch for visibility in production; PostgreSQL is unsuitable for medium-to-large-scale systems — even 100 RPS caused spiked database load beyond 120."
— W05S: On-Premises Application Pattern Challenges, via GT2
URL: https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b

[FACT] Temporal learning curve: "Expect a month before your team is productive."
— F33: On-Premises Event-Driven Architecture, via GT2
URL: https://blog.taigrr.com/blog/setting-up-a-production-ready-temporal-server/

The Temporal migration specifically requires: (1) decomposing Step Functions state machine definitions into Temporal workflow and activity code; (2) standing up Cassandra cluster and Elasticsearch cluster as dependencies; (3) wiring Temporal SDK into existing job runner code. This is 2–4 person-months of refactoring work at minimum. Combined with Kafka (Strimzi) topic reconfiguration and consumer client rewriting, Phase 1 TE=3 (2–6 person-months) is accurate. RD=3 reflects that this is meaningfully harder than cloud-native equivalents but not at the specialist-staff level of Phase 3 OP=4 operations.

[FACT] "In production, on-premises Kafka clusters are difficult to set up, expand, and maintain... organizations must plan clusters of distributed servers to assure availability, maintain data storage and security, set up monitoring, and handle scaling."
— F75: MECE Abstraction Layer Framework, via GT2
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons

External validation: Confluent's migration cost analysis confirms that "engineering hours represent the largest hidden cost of migration, with senior engineers dedicated to planning, writing migration scripts, and testing — a typical migration can consume several person-months of valuable engineering talent."
— Confluent Blog: Cost of Apache Kafka Migrations
URL: https://www.confluent.io/blog/cost-of-kafka-migration/

This corroborates TE=3 (2–6 person-months) for the Kafka refactoring component alone.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 2 (Per-Customer Customization)

**Current rating:** RD=1, TE=1
**Re-derived rating:** RD=1, TE=1

The file states: "Event-driven architecture is standardized. No per-customer adaptation." This is correct. Kafka topic configurations, Temporal workflow definitions, and job queue topologies are ISV-level decisions standardized in Phase 1 and deployed as stamps per customer. No source data suggests per-customer EDA reconfiguration as a normal cost.

[FACT] "Redis with Celery achieves 5,200 tasks per second at 12ms average latency, outperforming RabbitMQ's 3,100 tasks per second at 28ms by 68% in throughput."
— F73: MECE ISV Developer Responsibility Framework, via GT2
URL: https://johal.in/celery-distributed-tasks-redis-broker-configuration-for-scalable-web-background-jobs/

Task throughput parameters are set at ISV architecture time. Per-customer hardware sizing of the broker infrastructure (partition counts, broker memory) is a P1/P3 configuration concern, not an AL05 application-code concern. RD=1, TE=1 is correctly scoped.

**Confidence:** High
**Verdict:** ACCURATE

---

### Phase 3 (Ongoing Support)

**Current rating:** RD=2, TE=3
**Re-derived rating:** RD=3, TE=3 (proposed adjustment)

This is the rating requiring the most scrutiny. The file assigns RD=2 and explicitly flags it as **[D]** with the note: "Event-driven architecture is complex regardless of tier. Kafka/Temporal event schema management is high-volume ongoing work. Tier delta is modest (Kafka vs SQS at application layer)."

GT2 records the on-premises Phase 3 FTE as "0.75–1.5 (app code) + 2.0–4.1 (ops)" — a combined 2.75–5.6 FTE. The classification "Delta=3 (second largest in the framework)" in GT2 applies to the absolute tier difficulty scale (CN=1, MK8s=3, OP=4), not specifically to Phase 3 ongoing support. The current RD=2 applies the *relative* difficulty lens: "how much harder is Phase 3 Kafka/Temporal maintenance on-premises vs. cloud-native?"

**The case for RD=3 (adjust upward):**

GT2 documents two specific ongoing burdens that are qualitatively different from cloud-native equivalents, not merely harder versions of the same work:

1. **Temporal configuration drift:** "The one-month learning curve compounds with ongoing config drift as Temporal frequently changes configuration requirements between versions." This is a qualitatively different operational burden from Step Functions, where AWS manages version compatibility.

2. **On-premises Kafka DLQ is application-layer only — no native DLQ support.** Cloud-native SQS DLQ is infrastructure-managed. On-premises Kafka DLQ requires bespoke application-layer dead-letter handling code that must be maintained per schema change.

[FACT] "On-premises EDA requires 2–4 FTE dedicated solely to EDA pattern operations vs. 0.1–0.6 FTE cloud-native."
— F33: On-Premises Event-Driven Architecture, via GT2

[FACT] "Confluent claims TCO savings of up to 60% with their managed service compared to self-hosted Kafka deployments."
— F75: MECE Abstraction Layer Framework, via GT2
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons

External validation confirms the Kafka self-hosting burden:

[FACT] SecurityScorecard "faced a ballooning operational burden managing their self-hosted Kafka; migrating to Confluent Cloud allowed them to decommission their IaaS cluster and re-assign their platform engineering team away from Kafka maintenance, projected to save over $1 million in operational costs over three years."
— Confluent Blog: Cost of Apache Kafka Migrations
URL: https://www.confluent.io/blog/cost-of-kafka-migration/

The 2.0–4.1 FTE ops burden documented in GT2 is substantively larger than the "modest" tier delta language in the Phase 3 notes suggests. A Delta=3 subsegment on the absolute scale should be expected to produce RD=3 (Moderate) on the relative Phase 3 scale, not RD=2 (Low). The characterization of Kafka vs. SQS application-layer delta as "modest" is an understatement relative to the documented DLQ, schema registry, and Temporal config-drift burdens.

**Confidence:** Medium
**Verdict:** ADJUST (RD: 2 → 3, upward by 1 point, driven by Temporal config drift, application-layer DLQ burden, and the 2.0–4.1 FTE ops documentation in GT2 which exceeds the "modest tier delta" characterization)

**Interview question:** "For your on-premises Temporal deployment, how frequently do Temporal version upgrades require changes to your workflow SDK code or configuration files? And who owns your dead-letter queue handling code — platform engineers or backend engineers?"

---

## Phase 3 FTE Range Validation

### Research FTE Column vs. GT2 Source Data

The `three_phase_on_prem_ratings.md` Phase 3 table includes a "Research FTE (on-prem)" column. The values for AL01–AL05 are validated against GT2 here:

| Subsegment | Three-Phase File FTE | GT2 Source FTE | Match? |
|------------|---------------------|----------------|--------|
| AL01 | 0.8–1.5 | 0.8–1.5 (design 0.5–1.0 + ops 0.3–0.5) | MATCH |
| AL02 | 3.0–6.0 | 3.0–6.0 | MATCH |
| AL03 | 1.5–3.0 | 1.5–3.0 | MATCH |
| AL04 | 0.75–1.5 | 0.75–1.5 | MATCH |
| AL05 | 2.75–5.6 | 0.75–1.5 (app) + 2.0–4.1 (ops) = 2.75–5.6 | MATCH |

All five Phase 3 FTE ranges pass direct validation against GT2. The AL05 composite FTE (app code + ops) is correctly summed and labeled. No FTE fabrication detected.

[STATISTIC] "The aggregate complexity ratio across all 10 subsegments is Cloud-Native : Managed K8s : On-Premises = 20 : 26 : 34. This represents a 1.0x : 1.3x : 1.7x multiplier in application-layer developer complexity."
— P2_application_logic.md §2, Executive Summary, via GT2

[DATA POINT] P2 Application Logic FTE at N=1: CN 5.8–13.2, MK8s 9.4–19.8, OP 19.3–38.0.
— G1_n_services_multiplier.md, via GT5

The Phase 3 P2 total (18.6–35.6 FTE) in the three-phase file is within range of the GT5/G1 OP figure (19.3–38.0 FTE for all of P2), accounting for the N=1 basis in G1 vs. the approximate scaling in the three-phase file. No material discrepancy.

---

## Key Findings

- **AL02 tier-invariance (RD=1) is substantiated by source data across all three phases.** The startup-sequence adaptation required on-premises (Consul/Vault readiness checks) is a genuine but bounded code delta that the source document itself judges insufficient to change the difficulty rating. The GT2 internal discrepancy — F75 citing "3/5" while the P2 summary matrix records "2/5" — is unresolved and represents a documentation gap in the source material.

- **AL05 Phase 3 RD=2 is the strongest adjustment candidate in this review.** GT2 documents a Delta=3 subsegment, a 2.0–4.1 FTE ongoing ops burden, application-layer DLQ ownership, and Temporal configuration drift as qualitatively distinct on-premises burdens. RD=2 ("Low — minor changes; same skill set, slightly more work") does not capture this accurately. RD=3 ("Moderate — meaningful new work; requires platform awareness") is better supported.

- **All five Phase 3 FTE ranges (AL01–AL05) validate exactly against GT2 source data.** No fabricated or drifted FTE figures are present. The composite AL05 FTE (2.75–5.6 = app 0.75–1.5 + ops 2.0–4.1) is correctly constructed and labeled.

- **AL04 Phase 3 TE=2 is a minor understatement.** GT2's on-premises FTE range of 0.75–1.5 maps more precisely to TE=3 (0.3–1.0 FTE) than TE=2 (0.1–0.3 FTE) for the application-layer component. This does not materially affect strategic conclusions but should be noted in a revision.

- **AL03 Phase 3 boundary allocation is the highest-confidence gap.** The 1.5–3.0 FTE in GT2 spans both infrastructure operations (P1 scope) and application-layer gateway config (AL03 scope). The split is undocumented. The Ingress NGINX retirement (March 2026) and Istio sidecar-to-Ambient migration path both have ongoing Phase 3 application-code consequences that may push the application-layer fraction higher than currently rated.

---

## Sources

**Internal Source Files (Ground Truth):**
- `analysis/review/GT2_P2_ground_truth.md` — Primary ground truth; all GT2 citations refer to this file
- `analysis/review/GT5_cross_reference_ground_truth.md` — G1 scaling model and S1 aggregates
- `analysis/P2_application_logic.md` — Original P2 source with tier analyses and FTE tables
- `analysis/three_phase_on_prem_ratings.md` — Document under review

**External URLs Cited:**

| Citation Key | URL | Data Point |
|---|---|---|
| softwareseni.com | https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/ | Industry average 45 services; $5K–$10K/month overhead at 50 services |
| markaicode.com | https://markaicode.com/grpc-vs-rest-benchmarks-2025/ | gRPC 107% higher throughput, 48% lower latency vs REST |
| gravitee.io API architecture | https://www.gravitee.io/blog/choosing-right-api-architecture | REST 90% market share |
| javacodegeeks.com | https://www.javacodegeeks.com/2025/12/microservices-vs-modular-monoliths-in-2025-when-each-approach-wins.html | 42% of organizations consolidating from microservices |
| comp423-25s.github.io | https://comp423-25s.github.io/resources/backend-architecture/0-layered-architecture/ | Business logic platform-agnostic; service layer portable |
| k8s.io ingress-nginx retirement | https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/ | Ingress NGINX retired November 2025, maintenance ending March 2026 |
| konghq.com benchmarks | https://developer.konghq.com/gateway/performance/benchmarks/ | Kong 130,014 RPS at P99 6.01ms; each plugin -14–33% throughput |
| gravitee.io gateway costs | https://www.gravitee.io/blog/managed-vs-self-hosted-api-gateway-costs | Self-hosted API gateway $10K–$50K+ annually; managed $3.50/M calls |
| arxiv.org service mesh | https://arxiv.org/html/2411.02267v1 | Istio sidecar +166% latency; Ambient +8%; Linkerd +33% |
| CNCF cloud native Q3 2025 | https://www.cncf.io/wp-content/uploads/2025/11/cncf_report_stateofcloud_111025a.pdf | Service mesh adoption 18% → 8%, Q3 2023 to Q3 2025 |
| bytebase.com | https://www.bytebase.com/blog/prisma-vs-typeorm/ | Prisma preferred for TypeScript 2025; TypeORM synchronize dangerous |
| AWS ElastiCache whitepaper | https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/amazon-elasticache-and-self-managed-redis.html | ElastiCache fully managed, all admin tasks by Amazon |
| palark.com Redis operator | https://blog.palark.com/failure-with-redis-operator-and-redis-data-analysis-tools/ | Spotahome Redis Operator last released January 2022 |
| johal.in Celery | https://johal.in/celery-distributed-tasks-redis-broker-configuration-for-scalable-web-background-jobs/ | Redis+Celery 5,200 tasks/sec at 12ms; RabbitMQ 3,100/sec at 28ms |
| vymo-engineering Medium | https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b | Temporal + PostgreSQL unsuitable at 100 RPS; requires Cassandra |
| blog.taigrr.com Temporal | https://blog.taigrr.com/blog/setting-up-a-production-ready-temporal-server/ | Temporal learning curve: "Expect a month before your team is productive" |
| automq.com Kafka self-hosted | https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons | Kafka self-hosting operationally demanding; Confluent claims 60% TCO savings managed |
| confluent.io Kafka migration | https://www.confluent.io/blog/cost-of-kafka-migration/ | Migration "can consume several person-months"; SecurityScorecard $1M+ savings from managed Kafka |
| readysetcloud.io Step Functions vs Temporal | https://www.readysetcloud.io/blog/allen.helton/step-functions-vs-temporal/ | Step Functions $0.025/1,000 transitions; Temporal Cloud $25/M actions |
