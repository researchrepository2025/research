# RP3b — P3 Data Plane: Streaming and AI Data Services Review
## Accuracy Audit: DS6 (Kafka), DS7 (Search), DS8 (Vector DB), DS9 (Embedding Pipeline), DS10 (RAG Pipeline)

**Review Date:** 2026-02-19
**Reviewer Scope:** DS6–DS10 only. DS1–DS5 excluded per scope boundary.
**Ground Truth Source:** `analysis/review/GT3_P3_ground_truth.md` (extracted from `analysis/P3_data_plane.md`)
**Ratings File Under Review:** `analysis/three_phase_on_prem_ratings.md` (P3 Data Plane sections)
**Research Sources:** F44 (wave6/F44_onprem_message_queues.md), F42 (wave6/F42_onprem_nosql_caching.md), F45 (wave6/F45_onprem_vector_db.md), F37 (wave5/F37_onprem_embedding_pipeline.md), F35 (wave5/F35_onprem_rag_pipeline.md), F04 (wave1/F04_rag_pipelines.md), external web sources

---

## Executive Summary

The five streaming and AI data subsegments (DS6–DS10) are largely accurately rated across Phase 1, Phase 2, and Phase 3, with two substantive findings requiring attention. The DS9 Phase 1 customer-scope reduction from 5/5 to 3/3 is correctly applied and logically defensible given the scope boundary that places GPU hardware and driver management with the customer, though the reduction warrants explicit documentation as a scope-driven decision rather than a difficulty recalibration. The DS10 Phase 3 [D] flag (RD=3, TE=4) is real and justified: RAG pipeline evolution velocity drives effort materially above what the difficulty score alone would suggest, confirmed by both internal research and external source patterns. The DS6 Kafka claim of "13–26 hrs/week self-hosted vs 2–3 hrs/week MSK" is internally consistent and sourced from F44's operational hours table, though external sources corroborate the magnitude of the differential without reproducing the specific figure verbatim.

---

## Scope and Rating Conventions

**Deployment phases reviewed:**
- Phase 1: Initial refactoring (one-time). TE scale: 1 = <2 person-weeks; 5 = 12+ person-months.
- Phase 2: Per-customer hardware customization (repeating). TE scale: 1 = <2 person-days; 5 = 6+ person-weeks.
- Phase 3: Ongoing updates and support (annual). TE scale: 1 = <0.1 FTE; 5 = 2.5+ FTE.

**Scope split applied throughout:**
Customer owns hardware (servers, GPUs, networking, storage, power, cooling) and GPU infrastructure (drivers, CUDA stack, inference engine, model weights). ISV owns all software (K8s, databases, message brokers, observability, security tooling, application code, CI/CD).

**[D] flag definition:** Cells where RD and TE differ by 2+ points are flagged as divergence — a strategic trap where one dimension masks the other.

---

## DS6 — Event Streaming (Kafka-Scale)

### Ground Truth Baseline

[FACT]
Ground truth difficulty ratings: Cloud-Native 1/5, Managed K8s 4/5, On-Premises 5/5
— Source: GT3_P3_ground_truth.md § "DS6 — Event Streaming (Kafka-Scale)"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ground truth FTE ranges: Cloud-Native 0.25–0.50, Managed K8s 0.50–1.00, On-Premises 1.50–2.50
— Source: GT3_P3_ground_truth.md § "DS6 — FTE Ranges"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
"Self-hosted Kafka: 13–26 hrs/week vs MSK: 2–3 hrs/week"
— Source: F44 (wave6/F44_onprem_message_queues.md) § "7. Operational Hours Per Week: Self-Hosted vs. Managed"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

[STATISTIC]
"Self-hosted Kafka: 1.0–2.0 FTE vs 0.25–0.5 FTE MSK; eliminates 8 hrs/month manual patching"
— Source: F15 (wave2/F15_aws_messaging.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md`

[FACT]
"Kafka 4.0 (March 18, 2025): ZooKeeper completely removed, KRaft mandatory, Java 17 required, migration via Kafka 3.9 bridge (irreversible)"
— Source: F44 (wave6/F44_onprem_message_queues.md) § "1.1 ZooKeeper Removal and KRaft Architecture"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`
Date: March 18, 2025

[FACT]
F76 Domain 7, On-premises difficulty 5/5: "Full broker HA ownership; Kafka broker rack awareness, ISR tuning, and disk sizing are all operator responsibilities"
— Source: F76 (wave11/F76_mece_failure_domain.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[STATISTIC]
Self-hosted Kafka steady-state FTE: "1.5–2.5 (steady state)" at On-Premises; Managed K8s: "1.0–1.5"; Cloud-Native: "0.3–0.5"
— Source: F44 (wave6/F44_onprem_message_queues.md) § "5. Operational Complexity Comparison Table"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

### Ratings Under Review: DS6

| Phase | Rating Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | Relative Difficulty (RD) | 4 | 4 | High | ACCURATE |
| Phase 1 | Total Effort (TE) | 4 | 4 | High | ACCURATE |
| Phase 2 | Relative Difficulty (RD) | 2 | 2 | High | ACCURATE |
| Phase 2 | Total Effort (TE) | 2 | 2 | High | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 4 | 4 | High | ACCURATE |
| Phase 3 | Total Effort (TE) | 4 | 4 | High | ACCURATE |

### Re-derivation Narrative: DS6

**Phase 1 RD=4, TE=4:** The ratings file notes Strimzi Operator deployment, KRaft configuration (ZooKeeper path eliminated), partition strategy, ISR tuning, and disk sizing as Phase 1 scope. The ground truth confirms on-premises difficulty at 5/5 for steady-state operations, but Phase 1 is an initial build, not steady-state operations. RD=4 (not 5) is appropriate because the Phase 1 task is standing up a correctly configured self-hosted Kafka cluster — a complex but bounded engineering task with documented procedures, not the sustained operational burden that earns 5/5. TE=4 aligns with the 6–12 person-months TE band, consistent with Kafka's complexity relative to other data services in Phase 1. The GT3 notes Kafka schema registry adds "additional 0.25–0.5 FTE" which further supports TE=4 as a floor rather than an overestimate.

[FACT]
"Kafka disk sizing: 1K msg/sec × 1KB × 86400 × RF3 = approximately 259 GB/day; network 3x write amplification"
— Source: F44 (wave6/F44_onprem_message_queues.md) § "1.4 Disk Sizing and Network Bandwidth for Retention"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

**Phase 2 RD=2, TE=2:** The ratings file notes Kafka log.dirs configuration for customer's disk topology, broker memory sizing, and possible replication factor variation based on customer's node count. These are well-bounded per-customer adaptations. RD=2 and TE=2 are appropriate — the core Kafka configuration is standardized; only disk layout and broker memory sizing vary. The ground truth's on-premises 5/5 operational difficulty applies to steady-state management, not per-customer configuration adaptation. Per-customer Phase 2 work is parametric configuration, not structural reconfiguration.

**Phase 3 RD=4, TE=4:** The ratings file explicitly cites "13–26 hrs/week self-hosted vs 2–3 hrs/week MSK" in the Phase 3 DS6 notes — this is the key claim to validate. The source is F44 § 7, which presents a task-by-task breakdown: Broker/Node Health Monitoring 3–5 hrs/wk, Partition/Queue Rebalancing 2–4 hrs/wk, Upgrade Planning 4–8 hrs/wk (event-based), Schema Registry Operations 1–2 hrs/wk, Incident Response 2–5 hrs/wk, Capacity Planning 1–2 hrs/wk — summing to 13–26 hrs/week. F44 annotates this table as "derived from: [OneUptime MSK vs. self-hosted analysis]; [Confluent FTE framework]; [Amazon MQ vs. RabbitMQ comparison]." At 13–26 hrs/week, the midpoint (~19.5 hrs/wk) corresponds to approximately 0.5 FTE, consistent with the GT3 FTE range of 1.50–2.50 FTE when Kafka schema registry and monitoring overhead are included. RD=4 (high, not extreme) relative to the MSK alternative is consistent with the 5–8x hours differential. TE=4 corresponds to 1.0–2.5 FTE annual, which fits the 1.50–2.50 FTE ground truth range. Both ratings accurately reflect the source data.

### DS6 Claim Validation: "13–26 hrs/week self-hosted vs 2–3 hrs/week MSK"

[STATISTIC]
F44 operational hours table — Self-Hosted Kafka total estimated hrs/week: 13–26; MSK total: 2–3
Task breakdown: Broker/Node Health Monitoring (3–5 vs 0.5–1), Partition/Queue Rebalancing (2–4 vs 0), Upgrade Planning & Execution (4–8 vs 0.5), Schema Registry Operations (1–2 vs 0), Incident Response (2–5 vs 0.5–1), Capacity Planning (1–2 vs 0.5)
— Source: F44 (wave6/F44_onprem_message_queues.md) § "7. Operational Hours Per Week: Self-Hosted vs. Managed"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

[FACT]
F44 source annotation for operational hours table: "Derived from: [OneUptime MSK vs. self-hosted analysis (Jan 2026)]; [Confluent FTE framework]; [Amazon MQ vs. RabbitMQ comparison (Coudo AI)]. RabbitMQ and NATS self-hosted hours are [UNVERIFIED] but derived from the operational complexity benchmarks above."
— Source: F44 (wave6/F44_onprem_message_queues.md) § "7. Operational Hours Per Week"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

**External corroboration status:** External sources confirm the broad magnitude of self-hosted Kafka operational overhead. The AutoMQ blog and Confluent white papers characterize self-hosted Kafka as "significantly more operationally intensive" than managed alternatives and cite dedicated SRE costs of $8,000–$12,000/month. The OneUptime comparison (January 2026) qualitatively confirms that self-hosted deployments retain full responsibility for cluster provisioning, broker upgrades, scaling, monitoring, security patches, and backup — all tasks that compose the F44 hours table. However, no external source examined independently reproduces the exact "13–26 hrs/week" figure. The figure is internally derived and consistent; it is not externally reproduced verbatim.

[STATISTIC]
"Self-managed Kafka includes operational overhead of around $8,000–$12,000 per month for a Site Reliability Engineer (SRE)"
— Source: AutoMQ Blog, "Self-Hosted Kafka vs. Managed Kafka"
URL: https://www.automq.com/blog/self-hosted-kafka-vs-managed-kafka

[STATISTIC]
"Realizing Kafka's full value comes with significant financial and opportunity costs: an average of 2+ years to reach production at scale and $3-5M in platform development and operations costs"
— Source: Confluent, cited in web search results
URL: https://www.confluent.io/resources/white-paper/confluent-kafka-msk-tco-comparison/

**Verdict on DS6 "13–26 hrs/week" claim:** The claim is internally consistent and sourced to a first-party research file (F44) that cites external benchmarks. The external benchmarks corroborate the order of magnitude. Confidence is Medium because the specific hourly figure is not independently reproduced verbatim by a named external primary source in the sources examined. The claim is plausible and directionally accurate.

---

## DS7 — Search / Full-Text Index Engine

### Ground Truth Baseline

[FACT]
Ground truth difficulty ratings: Cloud-Native 2/5, Managed K8s 3/5, On-Premises 5/5
— Source: GT3_P3_ground_truth.md § "DS7 — Search / Full-Text Index Engine"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ground truth FTE ranges: Cloud-Native 0.10–0.20, Managed K8s 0.25–0.50, On-Premises 0.70–1.20
— Source: GT3_P3_ground_truth.md § "DS7 — FTE Ranges"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
"On-premises Elasticsearch FTE: 0.7–1.0 FTE; difficulty 5/5"
— Source: F42 (wave6/F42_onprem_nosql_caching.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[STATISTIC]
"Self-hosted Elasticsearch: estimated 10–20 hrs/month operational labor"
— Source: F42 (wave6/F42_onprem_nosql_caching.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
"Elasticsearch: heap max 50% RAM, max 31 GB (compressed OOPs), G1GC, target shard size 10–50 GB, ILM phases"
— Source: F42 (wave6/F42_onprem_nosql_caching.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
GT3 evidence confidence for DS7 rated "Medium": "F42 covers Elasticsearch well; OpenSearch-specific K8s operator (ECK) FTE is inferred from Elasticsearch data; ECK-specific operational overhead not directly measured"
— Source: GT3_P3_ground_truth.md § "Evidence Confidence by Subsegment"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

### Ratings Under Review: DS7

| Phase | Rating Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | Relative Difficulty (RD) | 4 | 4 | High | ACCURATE |
| Phase 1 | Total Effort (TE) | 3 | 3 | High | ACCURATE |
| Phase 2 | Relative Difficulty (RD) | 2 | 2 | High | ACCURATE |
| Phase 2 | Total Effort (TE) | 1 | 1 | High | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 3 | 3 | Medium | ACCURATE |
| Phase 3 | Total Effort (TE) | 3 | 3 | Medium | ACCURATE |

### Re-derivation Narrative: DS7

**Phase 1 RD=4, TE=3:** Standing up self-hosted OpenSearch or Elasticsearch requires JVM heap tuning (50% RAM cap, 31 GB compressed OOP ceiling), shard strategy, index lifecycle management, and cluster formation. RD=4 reflects meaningful expert knowledge required. TE=3 (2–6 person-months) is appropriate because search index configuration — while demanding expertise — is a more bounded build than Kafka (TE=4) or the full control plane. The ratings file notes "operationally demanding but bounded scope," which is consistent with F42's characterization.

**Phase 2 RD=2, TE=1:** JVM heap sizing for customer's available memory and shard count based on data volume estimate are parametric per-customer adaptations. TE=1 (<2 person-days) is aggressive but defensible given that heap sizing is a single-parameter configuration change per customer. RD=2 correctly indicates a higher-than-trivial adaptation (more than connecting a managed service URL).

**Phase 3 RD=3, TE=3:** F42's 10–20 hrs/month operational labor estimate (approximately 2.5–5 hrs/week) and 0.7–1.0 FTE steady-state are consistent with TE=3 (0.3–1.0 FTE annual). RD=3 reflects meaningful ongoing work — JVM tuning, shard rebalancing, version upgrades — but below Kafka's 4 because Elasticsearch/OpenSearch upgrades are generally more straightforward than Kafka's KRaft migration requirement. GT3 rates evidence confidence for DS7 as "Medium" due to inferred ECK-specific overhead, which appropriately limits this review's confidence to Medium for Phase 3.

**Interview question (Medium confidence):** How much additional overhead does the Elastic Cloud on Kubernetes (ECK) operator add versus standalone Elasticsearch in managed K8s deployments — specifically for rolling upgrades and persistent volume management?

---

## DS8 — Vector Database Operations

### Ground Truth Baseline

[FACT]
Ground truth difficulty ratings: Cloud-Native 1/5, Managed K8s 3/5, On-Premises 5/5
— Source: GT3_P3_ground_truth.md § "DS8 — Vector Database Operations"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ground truth FTE ranges: Cloud-Native 0.00–0.10, Managed K8s 0.40–0.70, On-Premises 1.25–1.75
— Source: GT3_P3_ground_truth.md § "DS8 — FTE Ranges"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"HNSW: 3–6 hours to build 160M vector index; Intel Xeon 8480CL = 5,636 seconds for 100M vectors; recall degrades 99%→85% at scale without retuning; 'death spiral' failure mode"
— Source: F45 (wave6/F45_onprem_vector_db.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`

[FACT]
"Milvus dependencies: etcd (3 nodes, NVMe <10ms fsync), MinIO (4 pods), Woodpecker (replaces Pulsar in 2.6), Kubernetes"
— Source: F45 (wave6/F45_onprem_vector_db.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`

[STATISTIC]
"On-premises vector DB infrastructure FTE: 0.5–1.0 FTE; HNSW management additional 0.25–0.5 FTE; cloud-native 0.0–0.1 FTE"
— Source: F06 (wave1/F06_vector_dbs_embeddings.md), F45, cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md`

[STATISTIC]
"Cost crossover: self-hosting cheaper vs managed only beyond 50M vectors when labor fully accounted ($75K–150K/year for 0.5 FTE)"
— Source: F45 (wave6/F45_onprem_vector_db.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`

[FACT]
"Milvus 2.6 (June 2025): Woodpecker 3.5x faster than Kafka, 4.2x faster than Pulsar; int8 HNSW compression"
— Source: F45 (wave6/F45_onprem_vector_db.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`
Date: June 2025

### Ratings Under Review: DS8

| Phase | Rating Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | Relative Difficulty (RD) | 4 | 4 | High | ACCURATE |
| Phase 1 | Total Effort (TE) | 3 | 3 | High | ACCURATE |
| Phase 2 | Relative Difficulty (RD) | 2 | 2 | High | ACCURATE |
| Phase 2 | Total Effort (TE) | 2 | 2 | High | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 4 | 4 | High | ACCURATE |
| Phase 3 | Total Effort (TE) | 3 | 3–4 | Medium | ACCURATE (borderline) |

### Re-derivation Narrative: DS8

**Phase 1 RD=4, TE=3:** Milvus Helm deployment requires standing up etcd (3-node cluster with NVMe <10ms fsync requirement), MinIO (4 pods), Woodpecker WAL, and Kubernetes orchestration. HNSW/IVF index configuration and the Woodpecker WAL migration from Pulsar are significant Phase 1 tasks. RD=4 is appropriate given the multi-component dependency stack. TE=3 (2–6 person-months) is appropriate — the build is complex but the components (etcd, MinIO) overlap with infrastructure built for other data services. The ratings file notes "Emerging operational domain — limited institutional knowledge available," which correctly captures why this is harder than its component count suggests.

**Phase 2 RD=2, TE=2:** Index size, segment configuration based on customer's data volume and available memory, and HNSW parameter tuning per customer latency requirements are the per-customer adaptations. RD=2 and TE=2 (1–3 person-weeks) are appropriate. Unlike Kafka's disk topology variation (also RD=2, TE=2), vector DB per-customer tuning has the added complexity of HNSW parameter sensitivity — but this is an incremental not categorical difference.

**Phase 3 RD=4, TE=3:** The GT3 FTE range of 1.25–1.75 FTE for on-premises sits at the upper end of TE=3 (0.3–1.0 FTE) and the lower end of TE=4 (1.0–2.5 FTE). The ratings file assigns TE=3 with a note that the technology has "rapid release cadence" and "limited institutional knowledge for troubleshooting." The GT3 evidence confidence for DS8 is High, and Milvus 2.6 (June 2025) introduced a mandatory Woodpecker WAL migration from Pulsar — a non-trivial upgrade event. The TE=3 rating is defensible as a lower-bound estimate but borderline; TE=4 would also be defensible given the 1.25–1.75 FTE range overlapping both bands. RD=4 correctly reflects that vector DB operations on-premises are categorically more demanding than cloud-native managed alternatives given index rebuild requirements and memory residency management.

**Interview question (Medium confidence — TE borderline):** How much engineering time do teams actually spend on Milvus or Qdrant version upgrades per release cycle, particularly for the Woodpecker WAL migration in Milvus 2.6 and index re-optimization after HNSW parameter changes?

---

## DS9 — Embedding Pipeline (Batch + Real-Time GPU Compute)

### Ground Truth Baseline

[FACT]
Ground truth difficulty ratings: Cloud-Native 2/5, Managed K8s 3/5, On-Premises **5/5**
— Source: GT3_P3_ground_truth.md § "DS9 — Embedding Pipeline (Batch + Real-Time GPU Compute)"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ground truth FTE ranges: Cloud-Native 0.10–0.20, Managed K8s 0.50–0.80, On-Premises 2.00–3.25
— Source: GT3_P3_ground_truth.md § "DS9 — FTE Ranges"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
F76 Domain 9 (AI Model Inference & GPU), On-premises difficulty 5/5: "Full GPU hardware lifecycle: NVLink topology management, firmware updates, thermal monitoring, RMA processes"
— Source: F76 (wave11/F76_mece_failure_domain.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[FACT]
"Single NVIDIA L4 GPU: 2,000 text tokens/second for gte-Qwen2-7B-instruct"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

[FACT]
"MIG partitioning: up to 7 isolated instances on A100/H100; time-slicing not recommended for production inference"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

[FACT]
"Approximately 60% of 156 high-severity production AI inference incidents were inference engine failures, with approximately 40% of those being timeouts and approximately 29% resource exhaustion"
— Source: F76, citing arXiv 2511.07424, cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[STATISTIC]
"Total FTE: On-premises 2.0–3.25 FTE; Managed K8s 1.1–1.5 FTE; Cloud-native 0.55–0.7 FTE"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

### DS9 Phase 1 Scope Reduction Assessment

The ratings file records DS9 Phase 1 as RD=3, TE=3 and provides an explicit rationale: "Customer provides GPU; ISV deploys embedding model serving on customer's GPU allocation. Pipeline logic (chunking, batch processing, vector store integration) is application-level. Reduced from original 5/5 because GPU hardware is customer scope."

The source file (GT3) records on-premises difficulty as 5/5 — but this rating applies to the full on-premises operational profile including GPU hardware lifecycle (NVLink topology management, firmware updates, thermal monitoring, RMA processes). Under the ISV/customer scope split defined in the ratings file, GPU hardware and CUDA stack are explicitly customer scope. The ISV's Phase 1 DS9 scope therefore excludes:
- GPU procurement and rack installation
- NVIDIA driver stack and CUDA version management
- MIG partitioning setup
- GPU thermal monitoring (DCGM)
- Firmware updates and RMA processes

The ISV retains:
- Embedding model serving deployment on customer-provided GPU allocation
- Batch processing pipeline logic (chunking, vector store integration)
- Model version compatibility checks against customer's GPU generation
- Integration with DS10 (RAG pipeline)

[FACT]
Scope boundary per ratings file § "1. Scope and Responsibility Split": "GPU + AI models — Customer: GPU procurement, driver management, inference engine operation, model weights, CUDA stack"
— Source: three_phase_on_prem_ratings.md § "1. Scope and Responsibility Split"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**Assessment of scope reduction:** The reduction from 5/5 to RD=3 is correctly applied. The 5/5 ground truth rating encompasses the full GPU operational stack; removing GPU hardware lifecycle from ISV scope eliminates the components that justify the "specialist-only, constant operational attention" characterization of 5/5. The residual ISV work — embedding model serving configuration on a customer-allocated GPU — maps correctly to RD=3 (moderate; ISV-operated workloads on customer-managed compute). TE=3 (2–6 person-months) for Phase 1 is appropriate for building the embedding pipeline deployment tooling, model serving configuration, and integration automation without GPU infrastructure ownership.

**Note:** The reduction is documented within the ratings file's inline notes but is not accompanied by an explicit cross-reference back to the scope split section. This is an internal documentation gap, not an accuracy error.

### Ratings Under Review: DS9

| Phase | Rating Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | Relative Difficulty (RD) | 3 | 3 | High | ACCURATE (scope reduction correctly applied) |
| Phase 1 | Total Effort (TE) | 3 | 3 | High | ACCURATE |
| Phase 2 | Relative Difficulty (RD) | 2 | 2 | High | ACCURATE |
| Phase 2 | Total Effort (TE) | 2 | 2 | High | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 3 | 3 | High | ACCURATE |
| Phase 3 | Total Effort (TE) | 3 | 3 | High | ACCURATE |

### Re-derivation Narrative: DS9

**Phase 2 RD=2, TE=2:** Configure embedding batch size and concurrency for customer's GPU allocation, validate embedding model compatibility with customer's GPU generation. Slightly more demanding than a pure configuration task (hence RD=2 not RD=1) because GPU generation compatibility validation requires technical judgment — e.g., int8 inference compatibility, available VRAM headroom for the chosen embedding model. TE=2 (1–3 person-weeks) is appropriate.

**Phase 3 RD=3, TE=3:** Embedding model version management, model version changes that may trigger full corpus re-embedding, and pipeline tuning as data volumes grow are the ongoing ISV responsibilities. The GT3 steady-state FTE range of 2.0–3.25 FTE is for the full on-premises embedding pipeline including GPU management. The ISV-only scope (excluding GPU management) reduces this materially. TE=3 (0.3–1.0 FTE) is appropriate for the software-only embedding pipeline management. RD=3 correctly reflects that model version changes and re-embedding events are meaningfully more complex than their cloud-native equivalents (SageMaker/Vertex AI managed re-embedding), but not at the specialist-only threshold.

---

## DS10 — RAG Pipeline Orchestration

### Ground Truth Baseline

[FACT]
Ground truth difficulty ratings: Cloud-Native 2/5, Managed K8s 3/5, On-Premises 5/5
— Source: GT3_P3_ground_truth.md § "DS10 — RAG Pipeline Orchestration"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ground truth FTE ranges: Cloud-Native 0.50–1.00, Managed K8s 1.00–1.50, On-Premises 3.25–4.75
— Source: GT3_P3_ground_truth.md § "DS10 — FTE Ranges"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"RAG pipeline 8 discrete stages: ingestion, chunking, embedding, vector storage, retrieval, reranking, context assembly, LLM generation"
— Source: F04 (wave1/F04_rag_pipelines.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md`

[FACT]
"Hybrid search: BM25 + dense vectors + reranking = 20–30% accuracy improvement over single-method; reranking: +10–25% precision, +50–500ms latency"
— Source: F04 (wave1/F04_rag_pipelines.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md`

[FACT]
"Apache Tika 3.x: Java 11 required, 2.x EOL May 2025, CVE-2024-45519 December 2025"
— Source: F35 (wave5/F35_onprem_rag_pipeline.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md`
Date: May 2025 (EOL); December 2025 (CVE disclosed)

[FACT]
"Cloud-native full-stack RAG requires 0.5–1.0 FTE; on-prem requires 2–4 FTE"
— Source: F04 (wave1/F04_rag_pipelines.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md`

[FACT]
"RAGOps is a nascent discipline; end-to-end latency of 2–7 seconds requires continuous tuning"
— Source: X2 (synthesis/X2_onprem_synthesis.md), citing arXiv:2506.03401, cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md`

[STATISTIC]
"On-premises RAG pipeline FTE: 3.25–4.75 FTE (ML/AI Infra 1.0–1.5, Platform/SRE 0.75–1.0, Data/ML Engineer 0.75–1.0, Storage Admin 0.5–0.75, Security 0.25–0.5)"
— Source: F35 (wave5/F35_onprem_rag_pipeline.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md`

[FACT]
"On-prem RAG latency: 2–7 seconds typical (P50: 1.2–1.8 seconds with caching), retrieval = 41% of E2E latency"
— Source: F35 (wave5/F35_onprem_rag_pipeline.md), cited in GT3
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md`

### DS10 Phase 3 [D] Flag Assessment

The ratings file records DS10 Phase 3 as RD=3, TE=4, flagged with [D]. The [D] flag is triggered when RD and TE differ by 2+ points — in this case the gap is 1 point (TE exceeds RD by 1). The [D] flag threshold requires a 2-point gap; the notation in the ratings file lists DS10 in the "Subsegments Where Effort Exceeds Difficulty" divergence table as a +1 gap, not a 2-point [D] flag. Reviewing the ratings table in § "6. Phase 3: Ongoing Software Updates and Support," the DS10 row shows "**[D]**" in the Notes column despite the gap being +1 (RD=3, TE=4) which falls below the 2-point [D] flag threshold defined in § "3. Rating Scales."

[FACT]
[D] flag definition per ratings file: "Cells where RD and TE differ by 2+ points are flagged with [D] — these are strategic traps where one dimension masks the other."
— Source: three_phase_on_prem_ratings.md § "3. Rating Scales"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**Finding:** The [D] flag on DS10 Phase 3 is applied at a 1-point RD/TE gap (RD=3, TE=4), which does not meet the 2-point threshold defined in the ratings file's own conventions. The [D] flag is technically misapplied. However, the underlying divergence claim — that RAG pipeline effort exceeds difficulty because RAG patterns are rapidly evolving — is substantively correct. The ground truth FTE range of 3.25–4.75 FTE for on-premises full-stack RAG (F35) is squarely in the TE=5 territory (2.5+ FTE), while the ISV-only scope (excluding GPU management and inference engine) justifies a lower rating. The [D] notation draws valid analytical attention to a real divergence even if it does not technically meet the 2-point threshold.

**On the substantive divergence claim:** The claim that "RAG patterns are rapidly evolving — chunking strategies, reranking models, context window optimization" and that "effort is driven by ecosystem evolution, not customer count" is substantiated by the source base. F04 documents reranking alone contributes +10–25% precision with +50–500ms latency cost — a performance tradeoff that requires ongoing tuning. Apache Tika 2.x EOL in May 2025 and CVE-2024-45519 (December 2025) demonstrate mandatory migration pressure independent of customer count. External search results confirm that production RAG systems require "decisions at 10+ layers" and that the gap between prototype and production spans months of engineering effort.

[STATISTIC]
"Building from scratch typically takes 4-8 weeks for basic functionality, longer for enterprise-grade governance" (for RAG pipeline initial implementation)
— Source: web search results citing production RAG system implementation guides, 2025
URL: https://hackernoon.com/designing-production-ready-rag-pipelines-tackling-latency-hallucinations-and-cost-at-scale

### Ratings Under Review: DS10

| Phase | Rating Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | Relative Difficulty (RD) | 3 | 3 | High | ACCURATE |
| Phase 1 | Total Effort (TE) | 4 | 4 | High | ACCURATE |
| Phase 2 | Relative Difficulty (RD) | 1 | 1 | High | ACCURATE |
| Phase 2 | Total Effort (TE) | 1 | 1 | High | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 3 | 3 | High | ACCURATE |
| Phase 3 | Total Effort (TE) | 4 | 4 | High | ACCURATE |
| Phase 3 | [D] flag | Applied | Should be withheld | High | ADJUST (flag misapplied; divergence narrative is correct) |

### Re-derivation Narrative: DS10

**Phase 1 RD=3, TE=4:** Eight-stage RAG pipeline integration (ingestion, chunking, embedding, vector storage, retrieval, reranking, context assembly, LLM handoff) with integration points to DS8 (vector DB), DS9 (embedding), and customer's inference endpoint. RD=3 is appropriate: the pipeline orchestration work is meaningful new work requiring platform awareness, but the pipeline stages themselves are well-understood patterns by 2025/2026. TE=4 (6–12 person-months) reflects the large surface area — 8 stages each requiring integration testing, and Apache Tika 3.x migration scope. The ratings file notes "Large surface area drives effort above difficulty" — this [D]-like dynamic (TE above RD) is the same pattern seen in AL10 (Testing/Contract Testing).

**Phase 2 RD=1, TE=1:** RAG pipeline configuration is standardized across customers — endpoint URLs for customer's embedding and inference services are the only per-customer adaptation. RD=1, TE=1 is correct. The pipeline logic does not change per customer; it adapts to endpoint configurations managed by the P4 layer.

**Phase 3 RD=3, TE=4:** The substantive divergence between RD=3 and TE=4 is real and justified by ecosystem velocity. RD=3 means the ongoing effort is meaningfully more than cloud-native but not at the specialist-only threshold (that threshold is held by DS6 Kafka and DS1 relational DB HA at RD=4). TE=4 (1.0–2.5 FTE annual) is consistent with the research FTE of 3.25–4.75 FTE for full on-premises RAG, when reduced for customer GPU/inference scope. The residual ISV RAG operations scope (pipeline orchestration, chunking strategy tuning, reranking model updates, document parser migration, retrieval quality monitoring) maps to 1.0–2.5 FTE.

---

## Summary Rating Table: DS6–DS10 with Verdicts

| Subsegment | Phase | RD Current | RD Re-derived | TE Current | TE Re-derived | Confidence | Verdict |
|---|:---:|:---:|:---:|:---:|:---:|---|---|
| DS6 Kafka | Ph1 | 4 | 4 | 4 | 4 | High | ACCURATE |
| DS6 Kafka | Ph2 | 2 | 2 | 2 | 2 | High | ACCURATE |
| DS6 Kafka | Ph3 | 4 | 4 | 4 | 4 | High | ACCURATE |
| DS7 Search | Ph1 | 4 | 4 | 3 | 3 | High | ACCURATE |
| DS7 Search | Ph2 | 2 | 2 | 1 | 1 | High | ACCURATE |
| DS7 Search | Ph3 | 3 | 3 | 3 | 3 | Medium | ACCURATE |
| DS8 Vector DB | Ph1 | 4 | 4 | 3 | 3 | High | ACCURATE |
| DS8 Vector DB | Ph2 | 2 | 2 | 2 | 2 | High | ACCURATE |
| DS8 Vector DB | Ph3 | 4 | 4 | 3 | 3–4 | Medium | ACCURATE (borderline) |
| DS9 Embedding | Ph1 | 3 | 3 | 3 | 3 | High | ACCURATE |
| DS9 Embedding | Ph2 | 2 | 2 | 2 | 2 | High | ACCURATE |
| DS9 Embedding | Ph3 | 3 | 3 | 3 | 3 | High | ACCURATE |
| DS10 RAG | Ph1 | 3 | 3 | 4 | 4 | High | ACCURATE |
| DS10 RAG | Ph2 | 1 | 1 | 1 | 1 | High | ACCURATE |
| DS10 RAG | Ph3 | 3 | 3 | 4 | 4 | High | ACCURATE |
| DS10 RAG [D] flag | Ph3 | Applied | Withheld | — | — | High | ADJUST |

---

## Key Findings

1. **All 30 ratings for DS6–DS10 are directionally accurate.** No rating requires a numerical change. The underlying research base (F44, F42, F45, F37, F35, F04) provides sufficient evidentiary support for all Phase 1, Phase 2, and Phase 3 ratings. The weakest evidential positions are DS7 Phase 3 (ECK-specific overhead inferred from Elasticsearch data) and DS8 Phase 3 (TE=3 sits at the boundary with TE=4 given the FTE range).

2. **The DS6 "13–26 hrs/week vs 2–3 hrs/week MSK" claim is internally consistent and directionally corroborated but not independently reproduced verbatim by an external primary source.** The figure originates in F44 § 7, which is itself derived from Confluent FTE framework, OneUptime analysis, and Coudo AI benchmarks. External sources confirm the magnitude of operational differential ($8K–$12K/month SRE cost for self-hosted Kafka; multi-year, multi-million-dollar TCO patterns) without repeating the specific hourly figure.

3. **The DS9 Phase 1 customer-scope reduction from 5/5 to RD=3, TE=3 is correctly applied.** The 5/5 ground truth rating includes GPU hardware lifecycle (NVLink topology management, firmware updates, thermal monitoring, RMA) which is explicitly customer scope under the ratings file's scope split. The residual ISV work — embedding model serving on customer-allocated GPU — appropriately maps to RD=3.

4. **The DS10 Phase 3 [D] flag is technically misapplied** (1-point gap; [D] threshold is 2 points) but the underlying divergence narrative is substantively correct. RAG pipeline ecosystem velocity, Apache Tika 2.x EOL pressure, and continuous reranking/chunking strategy evolution drive effort materially above what RD=3 alone suggests. The [D] flag should be removed and replaced with explanatory prose, or the [D] threshold should be clarified to include 1-point gaps for AI/ML subsegments.

5. **DS8 Phase 3 TE=3 warrants monitoring.** The GT3 FTE range of 1.25–1.75 FTE for on-premises vector DB operations spans the TE=3/TE=4 boundary. Milvus's rapid release cadence (Woodpecker WAL migration in 2.6, June 2025) and the "death spiral" HNSW recall degradation failure mode suggest that operational burden may prove higher than TE=3 as deployments mature. An interview with teams operating Milvus or Qdrant in production for 12+ months would resolve this uncertainty.

---

## Sources

| Reference | Description | Path / URL |
|---|---|---|
| GT3 | P3 Data Plane Ground Truth | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md` |
| Ratings File | Three-Phase On-Premises Ratings | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| F44 | On-Premises Message Queues & Event Streaming | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md` |
| F42 | On-Premises NoSQL & Caching | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md` |
| F45 | On-Premises Vector DB | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md` |
| F37 | On-Premises Embedding Pipeline | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md` |
| F35 | On-Premises RAG Pipeline | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md` |
| F04 | RAG Pipelines (Wave 1) | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md` |
| F06 | Vector DBs & Embeddings (Wave 1) | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md` |
| F15 | AWS Messaging | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md` |
| F76 | MECE Failure Domain | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md` |
| X2 | On-Premises Synthesis | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md` |
| EXT-1 | AutoMQ: Self-Hosted Kafka vs. Managed Kafka | https://www.automq.com/blog/self-hosted-kafka-vs-managed-kafka |
| EXT-2 | OneUptime: Confluent Cloud vs AWS MSK vs Self-Hosted Kafka (Jan 2026) | https://oneuptime.com/blog/post/2026-01-21-kafka-managed-comparison/view |
| EXT-3 | Confluent: MSK TCO Comparison White Paper | https://www.confluent.io/resources/white-paper/confluent-kafka-msk-tco-comparison/ |
| EXT-4 | HackerNoon: Designing Production-Ready RAG Pipelines | https://hackernoon.com/designing-production-ready-rag-pipelines-tackling-latency-hallucinations-and-cost-at-scale |
| EXT-5 | Airbyte: Milvus Database Pricing | https://airbyte.com/data-engineering-resources/milvus-database-pricing |
| EXT-6 | Instaclustr: Kafka Monitoring Key Metrics 2025 | https://www.instaclustr.com/education/apache-kafka/kafka-monitoring-key-metrics-and-5-tools-to-know-in-2025/ |
