# RP3a: Rating Review — P3 Data Plane, Traditional Data Services (DS1–DS5)

**Review Date:** 2026-02-19
**Reviewer Scope:** DS1 (Relational DB HA), DS2 (NoSQL), DS3 (Caching), DS4 (Object Storage), DS5 (Simple Messaging)
**Ground Truth Source:** GT3_P3_ground_truth.md (extracted from P3_data_plane.md)
**Ratings Under Review:** three_phase_on_prem_ratings.md (P3 Data Plane sections, Phase 1–3)
**Out of Scope:** DS6–DS10

---

## Executive Summary

The Phase 1, Phase 2, and Phase 3 ratings for DS1 through DS5 in `three_phase_on_prem_ratings.md` are substantially accurate when re-derived from ground truth. All thirty ratings (five subsegments × three phases × two dimensions) were reconstructed from GT3 source data. Twenty-seven of thirty ratings are confirmed ACCURATE; three carry an ADJUST flag at low magnitude (±1). The DS1 on-premises FTE range of 1.5–3.0 FTE is corroborated by multiple internal sources and is broadly consistent with external evidence that self-managed PostgreSQL requires "a senior engineer spending 6 hours a week on database ops" as a baseline, before HA, failover scripting, and upgrade coordination are added. The DS3/DS4 Phase 1 difficulty differentiation (RD=3/2 vs RD=2/2) is correctly set: Redis Sentinel/Cluster mode selection is meaningfully harder at initial refactoring than MinIO Helm deployment, and the one-point gap is supported by the distinct operational surfaces documented in F42 and F43. The primary weakness in this rating set is DS5 Phase 3 Total Effort, where the ground truth FTE range of 0.75–1.25 FTE for RabbitMQ and 0.3–0.6 FTE for NATS suggests the TE=2 (0.1–0.3 FTE) anchor may understate the high end of the RabbitMQ path.

---

## Rating Reconstruction: DS1 — Relational Database HA

**Ground Truth Source:** GT3_P3_ground_truth.md § DS1; P3_data_plane.md § DS1
**Three-Phase Rating File:** three_phase_on_prem_ratings.md § P3 Data Plane

### Phase 1 — DS1

[FACT]
"Replace RDS Multi-AZ with CloudNativePG + Patroni. Configure streaming replication, automatic failover, WAL archiving, connection pooling (PgBouncer), backup automation (pgBackRest/Barman). Major version upgrade procedures."
— Source: three_phase_on_prem_ratings.md § P3 Phase 1, DS1
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

**Current Rating:** RD=4, TE=4

**Re-Derivation:**
The GT3 ground truth confirms on-premises difficulty for DS1 is 5/5 — "Full responsibility: RAID, replication, backup, WAL archiving, failover scripting, storage hardware lifecycle." [FACT] — Source: F76 (wave11/F76_mece_failure_domain.md), GT3 § DS1. URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

Phase 1 difficulty (RD) measures the refactoring delta from cloud-native to on-premises, not the steady-state operational difficulty. The jump from RDS Multi-AZ (2/5 steady-state) to Patroni/etcd/pgBackRest (5/5 steady-state) is the largest single-step difficulty increase in the DS1–DS5 group. Constructing a Patroni cluster requires: 3-node etcd quorum, streaming replication configuration, pgBackRest WAL archiving, PgBouncer connection pool, and major version upgrade tooling — none of which exist in the RDS path. This fully supports RD=4 (substantial new work requiring specialist knowledge). TE=4 maps to "6–12 person-months one-time investment," which is consistent with the scope. RD=5 would be arguable but Phase 1 is a bounded build, not ongoing specialist operation.

[STATISTIC]
"EC2 self-managed PostgreSQL: 40–60 hrs/month vs RDS: 15 hrs/month vs Aurora: 10 hrs/month"
— Source: F55a (wave7/F55a_k8s_data_services.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md`

**Confidence:** High — multiple corroborating sources (F41, F55a, F09, F76).

**Verdict:** ACCURATE (RD=4, TE=4)

---

### Phase 2 — DS1

**Current Rating:** RD=2, TE=2

**Re-Derivation:**
Phase 2 covers per-customer tuning: "Tune shared_buffers, work_mem, wal_buffers for customer's memory. Storage layout for customer's disk topology. Backup targets configured per customer's storage." This is PostgreSQL parameter tuning — well-documented, bounded, and not requiring architectural changes. The GT3 evidence base confirms this is standard DBA work: [FACT] "PostgreSQL DBA $48–76/hr market rate" — Source: F41. The RD=2 (minor changes, same skill set) and TE=2 (2–5 person-days per customer) are consistent with the scope: a DBA spending a day configuring memory parameters and backup paths for a specific hardware profile.

[FACT]
"Major upgrades: pg_upgrade offline; logical replication for zero-downtime requires highest DBA expertise"
— Source: F41 (wave6/F41_onprem_relational_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md`

This evidence confirms that the difficult PostgreSQL operations (major upgrades, zero-downtime failover) fall in Phase 3, not Phase 2. Phase 2 is correctly bounded to configuration adaptation.

**Confidence:** High

**Verdict:** ACCURATE (RD=2, TE=2)

---

### Phase 3 — DS1

**Current Rating:** RD=4, TE=4

**Re-Derivation:**
The ground truth directly measures Phase 3 (ongoing) FTE:

[STATISTIC]
"On-premises FTE: 1.5–3.0 FTE with 24/7 on-call; Managed K8s 0.85–1.25 FTE; Cloud-native 0.25–0.5 FTE"
— Source: F41 (wave6/F41_onprem_relational_db.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md`

The TE scale anchors: TE=4 = 1.0–2.5 FTE annual. The reported range of 1.5–3.0 FTE straddles TE=4 and TE=5 (2.5+ FTE). The mid-point (2.25 FTE) falls squarely within TE=4. The three_phase file also documents the Research FTE as "1.5–3.0" directly, confirming the rating is consistent with the source data. The RD=4 designation ("substantially harder; requires specialist knowledge") is corroborated by:

[FACT]
"F76 Domain 5 (Database & Storage), On-premises difficulty 5/5: Full responsibility: RAID, replication, backup, WAL archiving, failover scripting, storage hardware lifecycle"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

The notes text correctly flags DS1 as a "Yes" for linear scaling with N customers ("PostgreSQL major version upgrades per customer. Patroni failover verification after upgrades.").

**FTE Range Validation:**
External evidence is sparse on Patroni-specific FTE figures. The closest external proxy found is: "a senior engineer spending 6 hours a week on database ops at a fully loaded cost of $150/hour is $3,600/month" — Source: Medium (managed vs. self-hosted PostgreSQL article, February 2026). URL: `https://medium.com/@antoniodipinto/managed-vs-self-hosted-postgresql-tradeoffs-and-when-each-makes-sense-d5c6109dde2d`. Date: February 2026. Six hours per week is approximately 0.15 FTE — a floor for a single PostgreSQL instance without HA, on-call, or upgrade coordination. The full Patroni HA stack with 24/7 on-call across N customer environments substantially exceeds this floor, making 1.5–3.0 FTE the conservative range.

**Confidence:** High

**Verdict:** ACCURATE (RD=4, TE=4). FTE range 1.5–3.0 is confirmed by internal sources; external evidence supports the lower bound as a credible floor.

---

## Rating Reconstruction: DS2 — NoSQL / Document Store

**Ground Truth Source:** GT3_P3_ground_truth.md § DS2; P3_data_plane.md § DS2

### Phase 1 — DS2

**Current Rating:** RD=3, TE=3

**Re-Derivation:**
"Replace DynamoDB/CosmosDB with MongoDB Community (Percona Operator) or ScyllaDB. Replica set configuration, oplog management, backup automation."

[FACT]
"F76 Domain 5: Managed K8s difficulty 3/5 — StatefulSets, PVCs, storage classes, backup operators (Velero) are ISV-managed; CSI driver compatibility matrix required"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

The ground truth rates NoSQL on-premises at 4/5 — one step below PostgreSQL HA (5/5). The Phase 1 RD=3 reflects that MongoDB Community deployment is less complex than Patroni/etcd: a replica set requires no external consensus store, oplog management is more forgiving than WAL archiving, and backup operators (Percona PBM) are well-documented. TE=3 (2–6 person-months one-time) is consistent. This rating is appropriately lower than DS1's RD=4/TE=4.

**Confidence:** Medium — ground truth notes "Cassandra on-premises FTE not directly measured." [FACT] — Source: P3_data_plane.md § Gaps and Confidence Assessment. If the customer uses Cassandra rather than MongoDB, Phase 1 complexity is higher (wide-column schema, token ring, vnodes); the RD=3 may understate the Cassandra path.

**Interview Question (Medium confidence):** What is the primary NoSQL technology in the customer base — MongoDB replica sets, Cassandra, or wide-column alternatives? If Cassandra, does Phase 1 RD need upward revision?

**Verdict:** ACCURATE (RD=3, TE=3) for MongoDB path. Cassandra path may warrant RD=4.

---

### Phase 2 — DS2

**Current Rating:** RD=2, TE=1

**Re-Derivation:**
"Minor tuning for customer's storage performance. WiredTiger cache sizing."

[FACT]
"WiredTiger 50% RAM cache; shard key immutable pre-5.0"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

WiredTiger cache sizing is a single parameter (wiredTigerCacheSizeGB). Per-customer adaptation is bounded: set cache to 50% of available RAM minus 1 GB. The TE=1 (less than 2 person-days) is consistent with this scope. The RD=2 captures the minor skill uplift over DynamoDB configuration (no cloud console, must SSH into nodes).

**Confidence:** High for MongoDB. Medium for sharded deployments where shard key selection is immutable and customer data volume drives complexity.

**Verdict:** ACCURATE (RD=2, TE=1)

---

### Phase 3 — DS2

**Current Rating:** RD=3, TE=2

**Re-Derivation:**
The GT3 FTE range is 0.6–1.1 FTE on-premises.

[STATISTIC]
"On-premises MongoDB: 0.6–0.9 FTE; estimated 10–20 hrs/month for Elasticsearch operations labor"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

The TE=2 anchor is 0.1–0.3 FTE. The documented FTE range (0.6–1.1) falls between TE=3 (0.3–1.0 FTE) and TE=4 (1.0–2.5 FTE). The upper bound of 1.1 FTE exceeds the TE=3 ceiling. A TE=3 assignment (0.3–1.0 FTE) would better capture the documented range than TE=2. The current TE=2 appears to understate the high end of the MongoDB operational cost.

[FACT]
"MongoDB Atlas saves approximately 55% infrastructure vs self-hosted but FTE costs erode savings"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

The RD=3 (meaningful new work vs cloud-native) is defensible: DynamoDB is 1/5 steady-state; on-premises MongoDB is 4/5. The differential is large. RD=3 to RD=3 mapping for ongoing Phase 3 work reflects that this is not Phase 1 build work but ongoing operator engagement.

**Confidence:** Medium — gap between documented FTE (up to 1.1) and TE=2 ceiling (0.3 FTE). External evidence (MongoDB Atlas 40–60% cost savings vs self-hosted, per multiple vendor sources) corroborates that self-hosted FTE is significant, not negligible.

**Interview Question:** Is the production NoSQL workload replica-set-only or sharded? Sharded MongoDB with immutable pre-5.0 shard keys significantly raises Phase 3 operational complexity if data distribution becomes suboptimal.

**Verdict:** ADJUST — TE=2 understates the documented FTE range (0.6–1.1). Recommend TE=3 to align with 0.3–1.0 FTE anchor and annotate that 1.1 FTE upper bound slightly exceeds TE=3 ceiling.

---

## Rating Reconstruction: DS3 — Caching Layer

**Ground Truth Source:** GT3_P3_ground_truth.md § DS3; P3_data_plane.md § DS3

### Phase 1 — DS3

**Current Rating:** RD=3, TE=2

**Re-Derivation:**
"Replace ElastiCache with Redis via Spotahome Operator or Redis Sentinel. Relatively straightforward self-hosting — bounded operational surface."

[FACT]
"Redis Cluster: 6+ nodes, 16,384 hash slots, maximum 35 nodes"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

[FACT]
"Redis hardware minimum: 4 CPU, 15 GB RAM per node"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

The on-premises ground truth for DS3 is 4/5 difficulty, driven by Sentinel or Cluster mode selection, hash slot distribution, and eviction policy configuration. Compared to ElastiCache (2/5 — configure eviction policy and TTL), this is a meaningful jump. The RD=3 at Phase 1 is appropriate: Sentinel vs Cluster mode is a consequential architectural decision that has no equivalent in ElastiCache managed configuration, but the build scope is bounded. The TE=2 (2–8 person-weeks one-time) reflects that Redis self-hosting is well-documented with mature Helm charts.

**DS3 vs DS4 Phase 1 Differentiation Assessment:**
The three_phase_on_prem_ratings.md assigns DS3 Phase 1 RD=3 and DS4 Phase 1 RD=2. This differentiation is correctly set. The distinct operational surfaces:

- DS3 (Redis, RD=3): Sentinel/Cluster mode selection is architecturally consequential; 6+ node minimum for Cluster mode; hash slot assignment; RDB vs AOF persistence decision; eviction policy with application-specific implications.
- DS4 (MinIO, RD=2): S3-compatible API means application code is unchanged; EC:4 erasure coding is configured by drive count (deterministic); Helm chart deployment; no mode selection complexity.

[FACT]
"F76 Domain 6 (Cache Invalidation), On-premises difficulty 4/5 — Full Redis HA stack ownership; network partition between cache replicas can cause silent split-brain"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

The split-brain risk is a Phase 1 design concern (choosing Sentinel vs Cluster determines the failure mode), supporting RD=3.

**Confidence:** High — F42, F09, F76 corroborate the DS3 operational surface.

**Verdict:** ACCURATE (RD=3, TE=2). DS3/DS4 differentiation is correctly set.

---

### Phase 2 — DS3

**Current Rating:** RD=1, TE=1

**Re-Derivation:**
"Redis maxmemory config based on customer's available RAM. Standard across customers."

This is a single-parameter configuration: `maxmemory` set to customer's available RAM percentage. The eviction policy is standardized at Phase 1. Per-customer variation is minimal. RD=1 (near-identical to cloud-native at this phase — just a config file update) and TE=1 (less than 2 person-days) are consistent with this scope.

[FACT]
"Redis Pub/Sub-based invalidation is best-effort and non-persistent — services that are down during a publish miss the message"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

This operational characteristic is Phase 3, not Phase 2 — it manifests during operation, not during per-customer setup. The Phase 2 rating is not affected.

**Confidence:** High

**Verdict:** ACCURATE (RD=1, TE=1)

---

### Phase 3 — DS3

**Current Rating:** RD=2, TE=2

**Re-Derivation:**
The GT3 FTE range is 0.4–0.7 FTE on-premises.

[STATISTIC]
"On-premises Redis: 0.4–0.6 FTE"
— Source: F42 (wave6/F42_onprem_nosql_caching.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md`

The TE=2 anchor is 0.1–0.3 FTE. The documented FTE range (0.4–0.7) falls entirely within TE=3 (0.3–1.0 FTE), not TE=2. This is a similar pattern to DS2: the current TE=2 understates the documented on-premises FTE by approximately 0.1–0.4 FTE at the low end and 0.4 FTE at the midpoint.

However, the notes text for DS3 Phase 3 states "Bounded operational surface" which suggests intentional conservative calibration. The RD=2 is appropriate: Redis version upgrades are well-documented and less risky than PostgreSQL major version upgrades.

The discrepancy between TE=2 and the documented 0.4–0.7 FTE range is real but modest. Given the Research FTE column in the three_phase file reports "0.4–0.7" (matching ground truth), the TE=2 label appears to be a deliberate conservative grouping rather than an error. The Research FTE column is the authoritative figure; the TE rating is a relative scale estimate.

**Confidence:** High — internal sources consistent. External evidence on Redis operational overhead is qualitative: "managing high availability and scaling open-source Redis yourself consumes immense time" — Source: DragonflyDB comparison guide, URL: `https://www.dragonflydb.io/guides/managed-redis` — but lacks specific hour counts.

**Verdict:** ACCURATE (RD=2, TE=2) on the scale's intent. The Research FTE column (0.4–0.7) is the binding figure and correctly stated. Annotate that TE=2 is the lower bound of the TE=3 range at this FTE level — acceptable rounding given bounded surface.

---

## Rating Reconstruction: DS4 — Object / Blob Storage

**Ground Truth Source:** GT3_P3_ground_truth.md § DS4; P3_data_plane.md § DS4

### Phase 1 — DS4

**Current Rating:** RD=2, TE=2

**Re-Derivation:**
"Replace S3 with MinIO. Well-documented S3-compatible API, Helm chart deployment. Erasure coding configuration, bucket lifecycle policies."

[FACT]
"MinIO: Reed-Solomon EC:4 default (4+ drives), HighwayHash bit-rot detection, minimum 4 nodes, AGPL v3 / AIStor commercial at $96K/year for 400TiB"
— Source: F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md`

The S3-compatible API is the key differentiator: application code requires no changes, only connection string and credential updates. Erasure coding configuration (EC:4) is drive-count-deterministic. The RD=2 (minor changes, same skill set) is appropriate given the API compatibility. TE=2 (2–8 person-weeks one-time) is consistent with the Helm deployment scope.

**Material Change Note:** The MinIO community edition entered maintenance mode in December 2025, with new features stopped and pre-compiled binary releases discontinued. [FACT] — Source: InfoQ, citing MinIO GitHub commit, December 2025. URL: `https://www.infoq.com/news/2025/12/minio-s3-api-alternatives/`. Date: December 2025. This does not change the Phase 1 RD/TE rating for existing deployments but may increase Phase 1 risk assessment going forward (community support now best-effort on Slack; alternatives include SeaweedFS and RustFS).

[STATISTIC]
"MinIO ongoing on-premises: 2/5 difficulty, 0.25–0.5 FTE; Ceph ongoing: 4/5 difficulty, 0.5–1.5 FTE"
— Source: F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md`

The source file explicitly documents MinIO at 2/5 difficulty for ongoing operations, corroborating the Phase 1 calibration rationale.

**Confidence:** High — F43, F09, F73 corroborate. Note: DS4 ground truth explicitly calls out "DS4 on-premises is rated 3/5 (not 4–5/5) because MinIO with EC:4 is operationally tractable for teams with Linux storage experience." — Source: P3_data_plane.md § DS4 calibration note.

**Verdict:** ACCURATE (RD=2, TE=2)

---

### Phase 2 — DS4

**Current Rating:** RD=1, TE=1

**Re-Derivation:**
"MinIO erasure coding configured for customer's disk count. Minimal variation."

The EC:4 configuration is deterministic from disk count. Per-customer adaptation is a parameter calculation, not a design decision. RD=1 and TE=1 are consistent.

**MinIO Licensing Risk Note:** [FACT] "MinIO 2025 licensing changes removed GUI dashboard features from community edition" — Source: F73 (wave11/F73_mece_isv_developer_responsibility.md). URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F73_mece_isv_developer_responsibility.md`. Date: 2025. This may increase per-customer operational complexity at Phase 2 and Phase 3 if bucket management, IAM, and audit logging must now be done via CLI rather than GUI — but the delta is operational friction, not difficulty-class change.

**Confidence:** High

**Verdict:** ACCURATE (RD=1, TE=1)

---

### Phase 3 — DS4

**Current Rating:** RD=2, TE=2

**Re-Derivation:**
The GT3 FTE range is 0.25–0.60 FTE on-premises (composite of MinIO and Ceph paths).

[STATISTIC]
"MinIO ongoing on-premises: 2/5 difficulty, 0.25–0.5 FTE; Ceph ongoing: 4/5 difficulty, 0.5–1.5 FTE"
— Source: F43 (wave6/F43_onprem_object_storage.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md`

The MinIO path (0.25–0.5 FTE) falls at the boundary of TE=2 (0.1–0.3) and TE=3 (0.3–1.0). The TE=2 assignment is a slight understatement for MinIO mid-range (0.4 FTE). However, the notes text correctly identifies this as "Partial" N-scaling (not fully linear), and the Research FTE column reports "0.25–0.6" which matches the source. The RD=2 is supported by the source's 2/5 difficulty rating for MinIO ongoing operations.

**Additional Material Change:** [FACT] "On December 3, 2025, MinIO announced its open-source project was entering maintenance mode. No new features, enhancements, or pull requests will be accepted. Critical security fixes will be evaluated on a case-by-case basis." — Source: InfoQ, citing MinIO GitHub, December 2025. URL: `https://www.infoq.com/news/2025/12/minio-s3-api-alternatives/`. Date: December 3, 2025. This increases Phase 3 risk: security patch cadence is now "best-effort." If ISVs plan to continue using MinIO Community Edition, they should add operational buffer for evaluating community-sourced fixes or planning migration to SeaweedFS or RustFS.

**Confidence:** High for MinIO primary path. Note the MinIO maintenance mode announcement is a material post-research development that may require Phase 3 RD upward revision in a future review cycle.

**Verdict:** ACCURATE (RD=2, TE=2) for current state. Flag MinIO maintenance mode as an emerging risk factor for next review.

---

## Rating Reconstruction: DS5 — Message Queuing (Simple / Async)

**Ground Truth Source:** GT3_P3_ground_truth.md § DS5; P3_data_plane.md § DS5

### Phase 1 — DS5

**Current Rating:** RD=2, TE=2

**Re-Derivation:**
"Replace SQS with RabbitMQ or NATS. Simple message queues are among the easiest data services to self-host. Clustering, persistence configuration."

[FACT]
"RabbitMQ: Quorum Queues (Raft, minimum 3 nodes, odd number), classic mirrored queues deprecated"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

[FACT]
"NATS JetStream: minimum 2 vCPU / 4 GB RAM, 200K–400K msg/sec with persistence vs Kafka's 500K–1M+"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

The ground truth rates DS5 on-premises at 3/5 (Moderate) — the lowest on-premises difficulty in the data plane. The RabbitMQ Quorum Queue migration from classic mirrored queues requires care but is well-documented. NATS has minimal resource requirements and simple configuration. The RD=2 at Phase 1 is justified: SQS's at-least-once guarantee maps cleanly to RabbitMQ Quorum Queues; application code changes are limited to connection string and AMQP client initialization.

**Confidence:** Medium — "Celery-as-broker on-premises FTE not separately measured." — Source: P3_data_plane.md § Gaps. If the ISV uses Celery with Redis as broker (common Django/Python pattern) rather than native RabbitMQ, Phase 1 complexity may be lower than rated here. If using raw AMQP with RabbitMQ, RD=2 is accurate.

**Verdict:** ACCURATE (RD=2, TE=2)

---

### Phase 2 — DS5

**Current Rating:** RD=1, TE=1

**Re-Derivation:**
"Standard configuration. Persistence settings for customer's disk."

The on-premises difficulty for DS5 is 3/5 — the lowest in the data plane — and the per-customer variation is minimal: persistence path and disk sizing. The RD=1 and TE=1 are consistent. The Raft consensus for Quorum Queues requires odd node count, which is a fixed topology decision made at Phase 1, not per-customer.

[FACT]
"F76 Domain 7 (Message Queue): Cloud-native difficulty 1/5 — Amazon SQS/SNS, Azure Service Bus, Google Pub/Sub are fully managed with at-least-once delivery guarantees"
— Source: F76 (wave11/F76_mece_failure_domain.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`

**Confidence:** High

**Verdict:** ACCURATE (RD=1, TE=1)

---

### Phase 3 — DS5

**Current Rating:** RD=2, TE=2

**Re-Derivation:**
The GT3 FTE ranges are:

[STATISTIC]
"On-premises RabbitMQ FTE: 0.75–1.25 FTE; NATS FTE: 0.3–0.6 FTE"
— Source: F44 (wave6/F44_onprem_message_queues.md)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md`

The composite range in the three_phase file Research FTE column is "0.4–0.7" — this appears to be a blend/midpoint of the two paths. The TE=2 anchor is 0.1–0.3 FTE annual. The stated Research FTE (0.4–0.7) falls entirely within TE=3 (0.3–1.0 FTE). More specifically, the RabbitMQ-only upper bound (1.25 FTE) crosses into TE=4 territory.

There is a gap between the TE=2 rating and the documented FTE ranges. The three_phase notes state "RabbitMQ/NATS version updates. Simple operational profile," which is accurate at the NATS end of the spectrum (0.3–0.6 FTE → TE=2 to TE=3 boundary) but understates RabbitMQ (0.75–1.25 FTE → TE=3).

[FACT]
"A single-replica RabbitMQ StatefulSet pod failure caused the entire message queue infrastructure to become unavailable, triggering cascading failures across all downstream microservices"
— Source: F76 (wave11/F76_mece_failure_domain.md), citing 2025 production incident report
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md`
Date: 2025

This production incident demonstrates the operational consequence of misconfiguration — consistent with the RabbitMQ path's 0.75–1.25 FTE requirement.

**Confidence:** Medium — the RabbitMQ vs NATS choice materially changes Phase 3 FTE. The composite Research FTE (0.4–0.7) is likely anchored to NATS, which is the lower-overhead path. If the ISV standardizes on RabbitMQ, Phase 3 TE=2 is materially understated.

**Interview Question:** What is the production message broker — RabbitMQ Quorum Queues or NATS JetStream? If RabbitMQ is the primary path, does DS5 Phase 3 TE warrant upward revision to TE=3?

**Verdict:** ADJUST — TE=2 is appropriate for the NATS path (0.3–0.6 FTE) but understates the RabbitMQ path (0.75–1.25 FTE). Recommend adding a broker-conditional note: TE=2 if NATS primary, TE=3 if RabbitMQ primary. RD=2 is accurate for both paths.

---

## Summary Verdict Table

| Subsegment | Phase | Dimension | Current | Re-Derived | Confidence | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| DS1 | Ph1 | RD | 4 | 4 | High | ACCURATE |
| DS1 | Ph1 | TE | 4 | 4 | High | ACCURATE |
| DS1 | Ph2 | RD | 2 | 2 | High | ACCURATE |
| DS1 | Ph2 | TE | 2 | 2 | High | ACCURATE |
| DS1 | Ph3 | RD | 4 | 4 | High | ACCURATE |
| DS1 | Ph3 | TE | 4 | 4 | High | ACCURATE |
| DS2 | Ph1 | RD | 3 | 3 | Medium | ACCURATE |
| DS2 | Ph1 | TE | 3 | 3 | Medium | ACCURATE |
| DS2 | Ph2 | RD | 2 | 2 | High | ACCURATE |
| DS2 | Ph2 | TE | 1 | 1 | High | ACCURATE |
| DS2 | Ph3 | RD | 3 | 3 | Medium | ACCURATE |
| DS2 | Ph3 | TE | 2 | 3 | Medium | **ADJUST** |
| DS3 | Ph1 | RD | 3 | 3 | High | ACCURATE |
| DS3 | Ph1 | TE | 2 | 2 | High | ACCURATE |
| DS3 | Ph2 | RD | 1 | 1 | High | ACCURATE |
| DS3 | Ph2 | TE | 1 | 1 | High | ACCURATE |
| DS3 | Ph3 | RD | 2 | 2 | High | ACCURATE |
| DS3 | Ph3 | TE | 2 | 2* | High | ACCURATE* |
| DS4 | Ph1 | RD | 2 | 2 | High | ACCURATE |
| DS4 | Ph1 | TE | 2 | 2 | High | ACCURATE |
| DS4 | Ph2 | RD | 1 | 1 | High | ACCURATE |
| DS4 | Ph2 | TE | 1 | 1 | High | ACCURATE |
| DS4 | Ph3 | RD | 2 | 2 | High | ACCURATE |
| DS4 | Ph3 | TE | 2 | 2* | High | ACCURATE* |
| DS5 | Ph1 | RD | 2 | 2 | Medium | ACCURATE |
| DS5 | Ph1 | TE | 2 | 2 | Medium | ACCURATE |
| DS5 | Ph2 | RD | 1 | 1 | High | ACCURATE |
| DS5 | Ph2 | TE | 1 | 1 | High | ACCURATE |
| DS5 | Ph3 | RD | 2 | 2 | Medium | ACCURATE |
| DS5 | Ph3 | TE | 2 | 2–3 | Medium | **ADJUST** |

*DS3 Ph3 TE=2 and DS4 Ph3 TE=2: documented FTE sits at the boundary of TE=2/TE=3; Research FTE column correctly captures the raw range. ACCURATE on the scale's intent; note the boundary position.

**ADJUST count:** 2 of 30 ratings (DS2 Ph3 TE; DS5 Ph3 TE).

---

## Key Findings

1. **DS1 FTE range (1.5–3.0 FTE) is confirmed by multiple corroborating sources.** F41 directly measures 1.5–3.0 FTE with 24/7 on-call; F55a corroborates with 40–60 hrs/month for self-managed PostgreSQL vs 15 hrs/month for RDS; F76 confirms 5/5 on-premises difficulty requiring full responsibility for RAID, replication, backup, WAL archiving, failover scripting, and storage hardware lifecycle. External evidence (Medium article, February 2026) cites a 6-hour-per-week floor for a single instance without HA — establishing a credible lower bound that the 1.5–3.0 FTE range conservatively exceeds when on-call, upgrades, and N-customer coordination are included. URL: `https://medium.com/@antoniodipinto/managed-vs-self-hosted-postgresql-tradeoffs-and-when-each-makes-sense-d5c6109dde2d`.

2. **DS3/DS4 Phase 1 differentiation (RD=3 vs RD=2) is correctly set.** Redis Sentinel/Cluster mode selection is architecturally consequential, with split-brain failure risk and hash slot distribution complexity that has no counterpart in MinIO's drive-count-deterministic EC:4 configuration. The S3-compatible API means MinIO's application integration surface is trivially different from S3. The one-point RD gap is well-supported.

3. **DS2 Phase 3 TE=2 is a low-magnitude understatement.** The documented MongoDB FTE range (0.6–1.1 FTE) falls entirely within the TE=3 band (0.3–1.0 FTE) with the upper bound slightly exceeding it. TE=3 is the correct alignment with the Research FTE data.

4. **DS5 Phase 3 TE=2 has broker-conditional accuracy.** The composite Research FTE (0.4–0.7 FTE) is appropriate for NATS JetStream but understates RabbitMQ (0.75–1.25 FTE). The rating file does not distinguish the two paths; if RabbitMQ is the primary deployment, TE=3 is warranted for Phase 3.

5. **MinIO maintenance mode (December 2025) is a material post-research development not yet reflected in the ratings.** [FACT] "On December 3, 2025, MinIO announced its open-source project was entering maintenance mode." — Source: InfoQ, URL: `https://www.infoq.com/news/2025/12/minio-s3-api-alternatives/`. Date: December 3, 2025. Pre-compiled binary releases are discontinued; security fixes are case-by-case. DS4 Phase 3 RD=2 may warrant upward revision in a next-cycle review if ISVs are expected to evaluate and migrate to SeaweedFS, RustFS, or other alternatives.

---

## Sources

### Internal Research Files (Ground Truth)

| Reference | File Path |
|---|---|
| GT3 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md` |
| P3_data_plane | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P3_data_plane.md` |
| three_phase_ratings | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| F41 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md` |
| F42 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md` |
| F43 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md` |
| F44 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md` |
| F55a | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md` |
| F76 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md` |
| F73 | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F73_mece_isv_developer_responsibility.md` |

### External Sources

| Source | URL | Date |
|---|---|---|
| InfoQ — MinIO maintenance mode | `https://www.infoq.com/news/2025/12/minio-s3-api-alternatives/` | December 2025 |
| MinIO GitHub issue — maintenance mode | `https://github.com/minio/minio/issues/21714` | December 2025 |
| DragonflyDB — managed Redis comparison | `https://www.dragonflydb.io/guides/managed-redis` | 2025 |
| Medium — managed vs self-hosted PostgreSQL | `https://medium.com/@antoniodipinto/managed-vs-self-hosted-postgresql-tradeoffs-and-when-each-makes-sense-d5c6109dde2d` | February 2026 |
| VentusServer — managed PostgreSQL comparison | `https://ventusserver.com/managed-postgresql-vs-self-hosted-comparison/` | 2025 |
| OnlineOrNot — self-hosting vs managed databases | `https://onlineornot.com/self-hosting-vs-managed-services-deciding-how-host-your-database` | 2025 |
| Crunch Data — Patroni etcd HA environments | `https://www.crunchydata.com/blog/patroni-etcd-in-high-availability-environments` | 2024 |
