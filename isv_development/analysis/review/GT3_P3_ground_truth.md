# GT3: P3 Data Plane — Ground Truth Extraction
## Authoritative Ratings, FTE Estimates, and Operational Characteristics for DS1–DS10

**Source File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P3_data_plane.md`
**Extraction Date:** 2026-02-19
**Scope:** P3 Data Plane only (DS1–DS10). P1, P2, and P4 data excluded.

---

## Executive Summary

The P3 source file covers ten MECE data plane subsegments for a microservices-based AI-driven SaaS application, each defined by a distinct storage medium, failure propagation class, and ISV team owner. Weighted average difficulty scales from 1.5/5 (Cloud-Native) to 2.9/5 (Managed K8s) to 4.4/5 (On-Premises), with corresponding total FTE ranges of 1.55–2.70, 4.10–6.55, and 11.85–19.55 FTE respectively. Six subsegments reach difficulty 5/5 on-premises (DS1, DS6, DS7, DS8, DS9, DS10), each requiring specialist expertise with a documented 6-to-12-month hiring lead time and no viable FTE-substitution path.

---

## Difficulty Rating Scale (Source: P3_data_plane.md § "Difficulty Rating Scale")

| Rating | Label | Operational Meaning |
|:---:|---|---|
| 1 | Trivial | Fully managed; no ISV infrastructure knowledge required; configuration only |
| 2 | Low | Managed with ISV-owned configuration; connection pool tuning, policy setting |
| 3 | Moderate | ISV-operated workloads on managed control plane; StatefulSets, PVCs, operator management |
| 4 | High | Full component ownership; HA scripting, backup, failover, upgrade lifecycle |
| 5 | Very High | Specialist-only; constant operational attention; high failure risk without deep domain expertise |

---

## DS1 — Relational Database HA & Operations

**Source Section:** P3_data_plane.md § "DS1 — Relational Database HA & Operations"

### Difficulty Ratings

[FACT]
- Cloud-Native: 2/5
- Managed K8s: 3/5
- On-Premises: 5/5

Reaches 5/5 on-premises: **YES**

### FTE Ranges

[STATISTIC]
"On-premises FTE: 1.5–3.0 FTE with 24/7 on-call; Managed K8s 0.85–1.25 FTE; Cloud-native 0.25–0.5 FTE"
— Source: F41 (wave6/F41_onprem_relational_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md`

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.25–0.50 |
| Managed K8s | 0.50–0.85 |
| On-Premises | 1.50–3.00 |

### Key Operational Characteristics

[FACT]
"RDS Multi-AZ: 99.95% SLA, less than 35 seconds failover with 2 standbys, PITR to 5-minute granularity (WAL upload every 5 min), up to 15 read replicas"
— Source: F09 (wave2/F09_aws_data.md), citing AWS RDS documentation
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F09_aws_data.md`

[STATISTIC]
"EC2 self-managed PostgreSQL: 40–60 hrs/month vs RDS: 15 hrs/month vs Aurora: 10 hrs/month"
— Source: F55a (wave7/F55a_k8s_data_services.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md`

[FACT]
"Major upgrades: pg_upgrade offline; logical replication for zero-downtime requires highest DBA expertise"
— Source: F41 (wave6/F41_onprem_relational_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md`

[FACT]
"CloudNativePG on EKS: $2,700–5,400/month total vs RDS $1,950–2,150/month vs Aurora $1,800–2,200/month"
— Source: F55a (wave7/F55a_k8s_data_services.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md`

[FACT]
"CloudNativePG provides full extension control vs AWS-approved only; RDS Multi-AZ 60–120 seconds failover vs K8s sub-minute"
— Source: F55a (wave7/F55a_k8s_data_services.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md`

[FACT]
F76 Domain 5 (Database & Storage), On-premises difficulty 5/5: "Full responsibility: RAID, replication, backup, WAL archiving, failover scripting, storage hardware lifecycle"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

### Specialist Requirements

[FACT]
"PostgreSQL DBA $48–76/hr market rate"
— Source: F41 (wave6/F41_onprem_relational_db.md), citing ZipRecruiter 2025
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md`
Date: 2025

### Representative Tools

- Cloud-Native: Amazon RDS Multi-AZ, Aurora PostgreSQL, RDS Proxy
- Managed K8s: CloudNativePG (CNCF Sandbox Jan 15 2025, 132M+ downloads), Barman Cloud Plugin GA 2025
- On-Premises: Patroni, etcd, pgBackRest, PgBouncer (max 200 direct connections), pg_upgrade

---

## DS2 — NoSQL / Document Store Operations

**Source Section:** P3_data_plane.md § "DS2 — NoSQL / Document Store Operations"

### Difficulty Ratings

[FACT]
- Cloud-Native: 1/5
- Managed K8s: 3/5
- On-Premises: 4/5

Reaches 5/5 on-premises: **NO** (peaks at 4/5)

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.10 |
| Managed K8s | 0.40–0.70 |
| On-Premises | 0.60–1.10 |

### Key Operational Characteristics

[STATISTIC]
"DynamoDB: 99.999% Global Tables SLA, on-demand pricing cut 50% November 2024, DAX 10x performance"
— Source: F09 (wave2/F09_aws_data.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F09_aws_data.md`
Date: November 2024

[FACT]
"MongoDB Atlas saves approximately 55% infrastructure vs self-hosted but FTE costs erode savings"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[STATISTIC]
"On-premises MongoDB: 0.6–0.9 FTE; estimated 10–20 hrs/month for Elasticsearch operations labor"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
"WiredTiger 50% RAM cache; shard key immutable pre-5.0"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
F76 Domain 5, Managed K8s difficulty 3/5: "StatefulSets, PVCs, storage classes, backup operators (Velero) are ISV-managed; CSI driver compatibility matrix required"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

### Evidence Confidence Note

[FACT] Evidence confidence rated "Medium" for DS2: "primary source F42 covers MongoDB/Elasticsearch; Cassandra on-premises FTE not directly measured"
— Source: P3_data_plane.md § "Gaps and Confidence Assessment"

---

## DS3 — Caching Layer Operations

**Source Section:** P3_data_plane.md § "DS3 — Caching Layer Operations"

### Difficulty Ratings

[FACT]
- Cloud-Native: 2/5
- Managed K8s: 3/5
- On-Premises: 4/5

Reaches 5/5 on-premises: **NO** (peaks at 4/5)

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.10 |
| Managed K8s | 0.25 |
| On-Premises | 0.40–0.70 |

### Key Operational Characteristics

[STATISTIC]
"ElastiCache Valkey: 33% lower cost than Redis OSS serverless, 40% memory reduction, 230% scaling improvement"
— Source: F09 (wave2/F09_aws_data.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F09_aws_data.md`

[FACT]
"Redis Cluster: 6+ nodes, 16,384 hash slots, maximum 35 nodes"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
"Redis hardware minimum: 4 CPU, 15 GB RAM per node"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[STATISTIC]
"On-premises Redis: 0.4–0.6 FTE"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
"Redis Pub/Sub-based invalidation is best-effort and non-persistent — services that are down during a publish miss the message"
— Source: F76 (wave11/F76_mece_failure_domain.md), citing Redis documentation
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[FACT]
F76 Domain 6 (Cache Invalidation), On-premises difficulty 4/5: "Full Redis HA stack ownership; network partition between cache replicas can cause silent split-brain"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[FACT]
"Applications leveraging event-driven invalidation see a 70% reduction in stale data events"
— Source: F76, citing Redis Cache Invalidation Glossary
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

---

## DS4 — Object / Blob Storage Operations

**Source Section:** P3_data_plane.md § "DS4 — Object / Blob Storage Operations"

### Difficulty Ratings

[FACT]
- Cloud-Native: 1/5
- Managed K8s: 2/5
- On-Premises: 3/5

Reaches 5/5 on-premises: **NO** (peaks at 3/5)

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.05–0.10 |
| Managed K8s | 0.10–0.20 |
| On-Premises | 0.25–0.60 |

### Storage and Capacity Scaling Characteristics

[FACT]
"S3: 11-nines durability, $0.023/GB/month standard, $0.00099/GB/month Glacier Deep Archive"
— Source: F09 (wave2/F09_aws_data.md), F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F09_aws_data.md`

[FACT]
"MinIO: Reed-Solomon EC:4 default (4+ drives), HighwayHash bit-rot detection, minimum 4 nodes, AGPL v3 / AIStor commercial at $96K/year for 400TiB"
— Source: F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md`

[FACT]
"MinIO benchmark: 183.2 GB/sec read, 171.3 GB/sec write on 32 NVMe nodes"
— Source: F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md`

[FACT]
"Ceph: RADOS architecture, CRUSH map, 9+ OSD nodes recommended, deep scrub I/O impact"
— Source: F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md`

[STATISTIC]
"MinIO ongoing on-premises: 2/5 difficulty, 0.25–0.5 FTE; Ceph ongoing: 4/5 difficulty, 0.5–1.5 FTE"
— Source: F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md`

[FACT]
F73 C06 (File & Blob Storage) difficulty: Cloud-native 1/5, Managed K8s 2/5, On-premises 3/5
— Source: F73 (wave11/F73_mece_isv_developer_responsibility.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F73_mece_isv_developer_responsibility.md`

[FACT]
"MinIO 2025 licensing changes removed GUI dashboard features from community edition"
— Source: F73, citing MinIO licensing change
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F73_mece_isv_developer_responsibility.md`
Date: 2025

### Calibration Note

[FACT]
DS4 on-premises rated 3/5 (not 4–5/5) because MinIO with EC:4 is operationally tractable for teams with Linux storage experience. Ceph approaches 4/5 but is a less common ISV deployment choice. Composite rating reflects MinIO as primary ISV on-premises path.
— Source: P3_data_plane.md § "DS4 — Note on difficulty calibration"

---

## DS5 — Message Queuing (Simple / Async)

**Source Section:** P3_data_plane.md § "DS5 — Message Queuing (Simple / Async)"

### Difficulty Ratings

[FACT]
- Cloud-Native: 1/5
- Managed K8s: 2/5
- On-Premises: 3/5

Reaches 5/5 on-premises: **NO** (peaks at 3/5)

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.10 |
| Managed K8s | 0.20–0.30 |
| On-Premises | 0.40–0.70 |

### Key Operational Characteristics

[FACT]
"SQS: standard (unlimited TPS) vs FIFO (70K msg/sec with high-throughput), DLQ support, 15-minute max delay"
— Source: F15 (wave2/F15_aws_messaging.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md`

[FACT]
"RabbitMQ: Quorum Queues (Raft, minimum 3 nodes, odd number), classic mirrored queues deprecated"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

[FACT]
"NATS JetStream: minimum 2 vCPU / 4 GB RAM, 200K–400K msg/sec with persistence vs Kafka's 500K–1M+"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

[FACT]
"A single-replica RabbitMQ StatefulSet pod failure caused the entire message queue infrastructure to become unavailable, triggering cascading failures across all downstream microservices"
— Source: F76 (wave11/F76_mece_failure_domain.md), citing 2025 production incident report
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`
Date: 2025

[FACT]
F76 Domain 7 (Message Queue), Cloud-native difficulty 1/5: "Amazon SQS/SNS, Azure Service Bus, Google Pub/Sub are fully managed with at-least-once delivery guarantees"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[STATISTIC]
"On-premises RabbitMQ FTE: 0.75–1.25 FTE; NATS FTE: 0.3–0.6 FTE"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

---

## DS6 — Event Streaming (Kafka-Scale)

**Source Section:** P3_data_plane.md § "DS6 — Event Streaming (Kafka-Scale)"

### Difficulty Ratings

[FACT]
- Cloud-Native: 1/5
- Managed K8s: 4/5
- On-Premises: 5/5

Reaches 5/5 on-premises: **YES**

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.25–0.50 |
| Managed K8s | 0.50–1.00 |
| On-Premises | 1.50–2.50 |

### Self-Hosted vs Managed Service FTE Differential

[STATISTIC]
"Self-hosted Kafka: 1.0–2.0 FTE vs 0.25–0.5 FTE MSK; eliminates 8 hrs/month manual patching"
— Source: F15 (wave2/F15_aws_messaging.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md`

[STATISTIC]
"Self-hosted Kafka: 13–26 hrs/week vs MSK: 2–3 hrs/week"
— Source: F44 (wave6/F44_onprem_message_queues.md) / F15 (wave2/F15_aws_messaging.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

[STATISTIC]
"Full stack on-premises messaging: 5.3–10.75 FTE total; cloud-native: 0.70–1.35 FTE"
— Source: F15 (wave2/F15_aws_messaging.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md`

### Storage and Capacity Scaling Characteristics

[FACT]
"Kafka 4.0 (March 18, 2025): ZooKeeper completely removed, KRaft mandatory, Java 17 required, migration via Kafka 3.9 bridge (irreversible)"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`
Date: March 18, 2025

[FACT]
"Kafka disk sizing: 1K msg/sec × 1KB × 86400 × RF3 = approximately 259 GB/day; network 3x write amplification"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

[FACT]
"Strimzi 0.46+: ZooKeeper removed, requires KRaft migration (semi-automated but manual steps required)"
— Source: F55a (wave7/F55a_k8s_data_services.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md`

[FACT]
F76 Domain 7, Managed K8s difficulty 4/5: "Kafka on K8s requires persistent volume management, ZooKeeper/KRaft quorum, and consumer lag monitoring"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[FACT]
F76 Domain 7, On-premises difficulty 5/5: "Full broker HA ownership; Kafka broker rack awareness, ISR tuning, and disk sizing are all operator responsibilities"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[FACT]
"Kafka schema registry: additional 0.25–0.5 FTE"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

---

## DS7 — Search / Full-Text Index Engine

**Source Section:** P3_data_plane.md § "DS7 — Search / Full-Text Index Engine"

### Difficulty Ratings

[FACT]
- Cloud-Native: 2/5
- Managed K8s: 3/5
- On-Premises: 5/5

Reaches 5/5 on-premises: **YES**

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.10–0.20 |
| Managed K8s | 0.25–0.50 |
| On-Premises | 0.70–1.20 |

### Key Operational Characteristics

[FACT]
"OpenSearch UltraWarm: 90% cost reduction vs hot storage"
— Source: F09 (wave2/F09_aws_data.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F09_aws_data.md`

[FACT]
"Elasticsearch: heap max 50% RAM, max 31 GB (compressed OOPs), G1GC, target shard size 10–50 GB, ILM phases"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[STATISTIC]
"Self-hosted Elasticsearch: estimated 10–20 hrs/month operational labor"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[STATISTIC]
"On-premises Elasticsearch FTE: 0.7–1.0 FTE; difficulty 5/5"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
X2 Category A: "Elasticsearch clusters with JVM heap tuning at the 32 GB compressed OOP ceiling" listed as core stateful platform burden
— Source: X2 (synthesis/X2_onprem_synthesis.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md`

### Evidence Confidence Note

[FACT] Evidence confidence rated "Medium" for DS7: "F42 covers Elasticsearch well; OpenSearch-specific K8s operator (ECK) FTE is inferred from Elasticsearch data; ECK-specific operational overhead not directly measured"
— Source: P3_data_plane.md § "Gaps and Confidence Assessment"

---

## DS8 — Vector Database Operations

**Source Section:** P3_data_plane.md § "DS8 — Vector Database Operations"

### Difficulty Ratings

[FACT]
- Cloud-Native: 1/5
- Managed K8s: 3/5
- On-Premises: 5/5

Reaches 5/5 on-premises: **YES**

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.00–0.10 |
| Managed K8s | 0.40–0.70 |
| On-Premises | 1.25–1.75 |

### Storage and Capacity Scaling Characteristics

[FACT]
"HNSW: 3–6 hours to build 160M vector index; Intel Xeon 8480CL = 5,636 seconds for 100M vectors; recall degrades 99%→85% at scale without retuning; 'death spiral' failure mode"
— Source: F45 (wave6/F45_onprem_vector_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`

[FACT]
"HNSW: 1.5–2x RAM overhead; 64 GB RAM for 1B vectors; IVF-PQ 4–8x memory reduction"
— Source: F06 (wave1/F06_vector_dbs_embeddings.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md`

[FACT]
"GPU acceleration: 21x speedup for index building; 8 DGX H100: 56 minutes vs 6.22 days CPU for IVF-PQ on large dataset"
— Source: F45 (wave6/F45_onprem_vector_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`

[FACT]
"Embedding model upgrades trigger full re-indexing; Drift-Adapter achieves 95–99% recall recovery with 100x cost reduction"
— Source: F06 (wave1/F06_vector_dbs_embeddings.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md`

### Specialist Requirements

[FACT]
"Milvus dependencies: etcd (3 nodes, NVMe <10ms fsync), MinIO (4 pods), Woodpecker (replaces Pulsar in 2.6), Kubernetes"
— Source: F45 (wave6/F45_onprem_vector_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`

[FACT]
"Qdrant: runnable on 0.5 CPU / 1 GB RAM; Rust implementation; 50–100K vectors/sec ingestion; 41.47 QPS at 50M vectors at 99% recall"
— Source: F06 (wave1/F06_vector_dbs_embeddings.md), F45
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md`

[FACT]
"Milvus 2.6 (June 2025): Woodpecker 3.5x faster than Kafka, 4.2x faster than Pulsar; int8 HNSW compression"
— Source: F45 (wave6/F45_onprem_vector_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`
Date: June 2025

[STATISTIC]
"Cost crossover: self-hosting cheaper vs managed only beyond 50M vectors when labor fully accounted ($75K–150K/year for 0.5 FTE)"
— Source: F45 (wave6/F45_onprem_vector_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md`

[STATISTIC]
"On-premises vector DB infrastructure FTE: 0.5–1.0 FTE; HNSW management additional 0.25–0.5 FTE; cloud-native 0.0–0.1 FTE"
— Source: F06 (wave1/F06_vector_dbs_embeddings.md), F45
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md`

---

## DS9 — Embedding Pipeline (Batch + Real-Time GPU Compute)

**Source Section:** P3_data_plane.md § "DS9 — Embedding Pipeline (Batch + Real-Time GPU Compute)"

### Difficulty Ratings

[FACT]
- Cloud-Native: 2/5
- Managed K8s: 3/5
- On-Premises: 5/5

Reaches 5/5 on-premises: **YES**

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.10–0.20 |
| Managed K8s | 0.50–0.80 |
| On-Premises | 2.00–3.25 |

### Key Operational Characteristics

[FACT]
"Single NVIDIA L4 GPU: 2,000 text tokens/second for gte-Qwen2-7B-instruct"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

[FACT]
"NVIDIA NIM: throughput mode 2x performance on large batches; int8 type = 4x memory reduction"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

[FACT]
"MIG partitioning: up to 7 isolated instances on A100/H100; time-slicing not recommended for production inference"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

[FACT]
"Re-embedding: Embedding-Converter (ACL 2025) handles 50M docs in <2 hours, 100x cost reduction vs full re-embed"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`
Date: ACL 2025

[STATISTIC]
"Total FTE: On-premises 2.0–3.25 FTE; Managed K8s 1.1–1.5 FTE; Cloud-native 0.55–0.7 FTE"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

### Specialist Requirements

[FACT]
F76 Domain 9 (AI Model Inference & GPU), On-premises difficulty 5/5: "Full GPU hardware lifecycle: NVLink topology management, firmware updates, thermal monitoring, RMA processes"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[FACT]
"Approximately 60% of 156 high-severity production AI inference incidents were inference engine failures, with approximately 40% of those being timeouts and approximately 29% resource exhaustion"
— Source: F76, citing arXiv 2511.07424
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

[FACT]
Model landscape: "Qwen3-Embedding-8B: 8B params, approximately 16GB VRAM, MTEB 70.58"
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

[DATA POINT]
Model landscape detail: all-MiniLM-L6-v2 (22.7M params, 43MB VRAM); BGE-M3 (568M params, 1.06GB VRAM); Qwen3-Embedding-8B (8B params, ~16GB VRAM)
— Source: F37 (wave5/F37_onprem_embedding_pipeline.md) via P3_data_plane.md § "DS9 — Representative Tools"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md`

---

## DS10 — RAG Pipeline Orchestration

**Source Section:** P3_data_plane.md § "DS10 — RAG Pipeline Orchestration"

### Difficulty Ratings

[FACT]
- Cloud-Native: 2/5
- Managed K8s: 3/5
- On-Premises: 5/5

Reaches 5/5 on-premises: **YES**

### FTE Ranges

| Tier | FTE Range |
|---|---|
| Cloud-Native | 0.50–1.00 |
| Managed K8s | 1.00–1.50 |
| On-Premises | 3.25–4.75 |

### Key Operational Characteristics

[FACT]
"RAG pipeline 8 discrete stages: ingestion, chunking, embedding, vector storage, retrieval, reranking, context assembly, LLM generation"
— Source: F04 (wave1/F04_rag_pipelines.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md`

[FACT]
"Hybrid search: BM25 + dense vectors + reranking = 20–30% accuracy improvement over single-method; reranking: +10–25% precision, +50–500ms latency"
— Source: F04 (wave1/F04_rag_pipelines.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md`

[FACT]
"Apache Tika 3.x: Java 11 required, 2.x EOL May 2025, CVE-2024-45519 December 2025"
— Source: F35 (wave5/F35_onprem_rag_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md`
Date: May 2025 (EOL); December 2025 (CVE disclosed)

[FACT]
"On-prem RAG latency: 2–7 seconds typical (P50: 1.2–1.8 seconds with caching), retrieval = 41% of E2E latency"
— Source: F35 (wave5/F35_onprem_rag_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md`

[FACT]
"Cisco FlashStack + NVIDIA NIM CVD: 6x Cisco UCS X210c M7, 4x NVIDIA L40S, Pure Storage FlashBlade"
— Source: F35 (wave5/F35_onprem_rag_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md`

[FACT]
"Cloud-native full-stack RAG requires 0.5–1.0 FTE; on-prem requires 2–4 FTE"
— Source: F04 (wave1/F04_rag_pipelines.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md`

[FACT]
"RAGOps is a nascent discipline; end-to-end latency of 2–7 seconds requires continuous tuning"
— Source: X2 (synthesis/X2_onprem_synthesis.md), citing arXiv:2506.03401
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md`

### Specialist Requirements (On-Premises Role Breakdown)

[STATISTIC]
"On-premises RAG pipeline FTE: 3.25–4.75 FTE (ML/AI Infra 1.0–1.5, Platform/SRE 0.75–1.0, Data/ML Engineer 0.75–1.0, Storage Admin 0.5–0.75, Security 0.25–0.5)"
— Source: F35 (wave5/F35_onprem_rag_pipeline.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md`

[FACT]
X2 Rank 7: RAG pipeline operations rated 5/5 difficulty, 3.25–4.75 FTE
— Source: X2 (synthesis/X2_onprem_synthesis.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md`

---

## Summary Table: All Ratings and FTE Ranges

**Source:** P3_data_plane.md § "Summary Difficulty Matrix"

| Subsegment | CN Difficulty | MK8s Difficulty | OP Difficulty | Reaches 5/5 OP | CN FTE | MK8s FTE | OP FTE |
|---|:---:|:---:|:---:|:---:|---|---|---|
| DS1 — Relational Database HA | 2 | 3 | 5 | YES | 0.25–0.50 | 0.50–0.85 | 1.50–3.00 |
| DS2 — NoSQL / Document Store | 1 | 3 | 4 | NO | 0.10 | 0.40–0.70 | 0.60–1.10 |
| DS3 — Caching Layer | 2 | 3 | 4 | NO | 0.10 | 0.25 | 0.40–0.70 |
| DS4 — Object / Blob Storage | 1 | 2 | 3 | NO | 0.05–0.10 | 0.10–0.20 | 0.25–0.60 |
| DS5 — Message Queuing (Simple) | 1 | 2 | 3 | NO | 0.10 | 0.20–0.30 | 0.40–0.70 |
| DS6 — Event Streaming (Kafka) | 1 | 4 | 5 | YES | 0.25–0.50 | 0.50–1.00 | 1.50–2.50 |
| DS7 — Search / Full-Text Index | 2 | 3 | 5 | YES | 0.10–0.20 | 0.25–0.50 | 0.70–1.20 |
| DS8 — Vector Database | 1 | 3 | 5 | YES | 0.00–0.10 | 0.40–0.70 | 1.25–1.75 |
| DS9 — Embedding Pipeline (GPU) | 2 | 3 | 5 | YES | 0.10–0.20 | 0.50–0.80 | 2.00–3.25 |
| DS10 — RAG Pipeline Orchestration | 2 | 3 | 5 | YES | 0.50–1.00 | 1.00–1.50 | 3.25–4.75 |
| **Weighted Average Difficulty** | **1.5** | **2.9** | **4.4** | — | — | — | — |
| **Total FTE Range** | — | — | — | — | **1.55–2.70** | **4.10–6.55** | **11.85–19.55** |

**Abbreviations:** CN = Cloud-Native | MK8s = Managed Kubernetes | OP = On-Premises

---

## Aggregate FTE Comparison (Source: P3_data_plane.md § "Aggregate FTE Comparison")

[STATISTIC]
| Deployment Tier | Data Plane FTE (Conservative) | Data Plane FTE (Peak) | Ratio to Cloud-Native |
|---|---|---|---|
| Cloud-Native | 1.55 | 2.70 | 1.0x |
| Managed K8s | 4.10 | 6.55 | 2.6x |
| On-Premises | 11.85 | 19.55 | 7.6x |

[STATISTIC]
Annual Data Plane Personnel Cost (at $150K–$200K/FTE fully loaded):
| Tier | Annual Cost Low | Annual Cost High |
|---|---|---|
| Cloud-Native | $232K | $540K |
| Managed K8s | $615K | $1.31M |
| On-Premises | $1.78M | $3.91M |

— Source: P3_data_plane.md § "Aggregate FTE Comparison"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P3_data_plane.md`

---

## Subsegments Reaching 5/5 On-Premises (Summary)

[FACT] The P3 source file identifies six subsegments reaching difficulty 5/5 on-premises:
1. DS1 — Relational Database HA (Patroni/etcd/pgBackRest stack)
2. DS6 — Event Streaming / Kafka (KRaft quorum, ISR tuning, disk sizing)
3. DS7 — Search / Full-Text Index (JVM heap, G1GC, ILM lifecycle)
4. DS8 — Vector Database (HNSW index management, RAM residency, re-indexing cycles)
5. DS9 — Embedding Pipeline (GPU lifecycle, MIG partitioning, model versioning)
6. DS10 — RAG Pipeline Orchestration (multi-stage coordination, RAGOps, Tika migration)

— Source: P3_data_plane.md § "Summary Difficulty Matrix" and individual subsegment sections

**Note:** The source file executive summary states "Four subsegments reach difficulty 5/5 on-premises" but the summary matrix and individual analyses enumerate six subsegments at 5/5. The matrix data is authoritative; the executive summary appears to undercount.
— Source: P3_data_plane.md § "Executive Summary" vs § "Summary Difficulty Matrix"

---

## High-Leverage Managed Service FTE Differentials

[STATISTIC]
Amazon MSK vs self-hosted Kafka: eliminates 1.5–2.5 FTE of on-premises overhead (computed from 1.0–2.0 FTE self-hosted vs 0.25–0.5 FTE MSK differential)
— Source: F15 (wave2/F15_aws_messaging.md), cited in P3_data_plane.md § "High-Leverage Managed Service Differentials"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md`

[STATISTIC]
Amazon RDS Multi-AZ vs EC2 self-managed PostgreSQL: eliminates 1.5–3.0 FTE of on-premises overhead
— Source: F55a (wave7/F55a_k8s_data_services.md), F41 (wave6/F41_onprem_relational_db.md), cited in P3_data_plane.md § "High-Leverage Managed Service Differentials"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md`

[FACT]
"These two services alone account for 2.25–4.5 FTE of recoverable on-premises overhead — equivalent to the entire cloud-native data plane staffing requirement."
— Source: P3_data_plane.md § "High-Leverage Managed Service Differentials"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P3_data_plane.md`

---

## Mandatory Migration Pressures with Data Plane Impact

[FACT]
Data plane migrations required before end of 2026:
- Kafka 4.0 KRaft (DS6): migration via Kafka 3.9 bridge, irreversible; affects Managed K8s (Strimzi 0.46+) and On-Premises
- Milvus Woodpecker WAL (DS8): replaces Pulsar dependency in Milvus 2.6; affects Managed K8s and On-Premises
- Apache Tika 2.x EOL May 2025 (DS10): migration to Tika 3.x required (Java 11 minimum); CVE-2024-45519 disclosed December 2025

— Source: X2 (synthesis/X2_onprem_synthesis.md), cited in P3_data_plane.md § "Mandatory Migration Pressures (2025–2026)"
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md`

---

## Evidence Confidence by Subsegment

Source: P3_data_plane.md § "Gaps and Confidence Assessment"

| Subsegment | Confidence | Documented Gap |
|---|---|---|
| DS1 — Relational DB HA | High | None identified |
| DS2 — NoSQL / Document Store | Medium | Cassandra on-premises FTE unquantified |
| DS3 — Caching Layer | High | None identified |
| DS4 — Object / Blob Storage | High | Ceph vs MinIO split not fully resolved; MinIO used as primary path |
| DS5 — Message Queuing | Medium | Celery-as-broker on-premises FTE not separately measured |
| DS6 — Event Streaming | High | None identified |
| DS7 — Search / Full-Text | Medium | ECK-specific overhead not directly measured; inferred from Elasticsearch |
| DS8 — Vector Database | High | Qdrant self-hosted K8s FTE understudied vs Milvus |
| DS9 — Embedding Pipeline | High | GPU procurement lead times (9–12 months for H100) not captured in FTE |
| DS10 — RAG Pipeline | High | RAGOps tooling maturity nascent (arXiv June 2025); estimates may improve |

---

## Sources

All data extracted from:

**Primary Source (this extraction):**
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P3_data_plane.md` — P3 Data Plane MECE Subsegment Analysis, dated 2026-02-19

**Original Research Files Cited in P3 Source:**

| Reference ID | File Path |
|---|---|
| F04 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md` |
| F06 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md` |
| F09 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F09_aws_data.md` |
| F15 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md` |
| F35 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md` |
| F37 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md` |
| F41 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md` |
| F42 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md` |
| F43 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md` |
| F44 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md` |
| F45 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md` |
| F55a | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md` |
| F73 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F73_mece_isv_developer_responsibility.md` |
| F76 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md` |
| X2 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md` |
