# F42 — On-Premises NoSQL & Caching: Operational Requirements and Trade-offs

**Research File:** F42
**Date:** 2026-02-18
**Scope:** Self-hosted NoSQL databases and caching layers (Redis, MongoDB, Elasticsearch) — operational profiles, HA configuration, tuning requirements, monitoring, and managed-service comparison.

---

## Executive Summary

Self-hosting Redis, MongoDB, and Elasticsearch on-premises delivers maximum control and can reduce licensing costs by 40–60% compared to fully managed equivalents, but imposes significant operational burden across cluster formation, high availability configuration, performance tuning, and ongoing maintenance. Each system carries distinct expertise requirements: Redis demands deep understanding of memory eviction, replication topology, and persistence trade-offs; MongoDB requires careful replica set orchestration, shard key selection, and WiredTiger cache tuning; Elasticsearch demands heap sizing discipline, shard lifecycle governance, and careful GC management to avoid cascading failures. Across all three systems, the hidden costs of self-hosted operations — skilled FTE hours, on-call rotations, and incident remediation — frequently erode or eliminate the raw infrastructure savings. Managed equivalents (ElastiCache, Atlas, OpenSearch Service, Cosmos DB) abstract the majority of this burden at a premium of roughly 30–50% above raw infrastructure cost, a trade-off that is operationally favorable for most ISVs below the scale threshold where dedicated database reliability engineering (DBRE) teams become economically justified.

---

## Section 1: Redis — Cluster Mode, Sentinel, Persistence, and Memory Management

### 1.1 High Availability Topology Choices

Redis offers two primary HA topologies, each with distinct operational profiles.

**Redis Sentinel** provides automated failover for a single primary/replica topology without data sharding. The minimum production configuration requires at least three Sentinel instances; Sentinel nodes listen on TCP port 26379 and require network reachability between all instances. Failover is only authorized when a majority of Sentinels agree, preventing split-brain in network partitions. [Redis Sentinel requires NTP synchronization across all cluster nodes](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/) to maintain consistent quorum decisions.

**Redis Cluster** distributes data across shards using hash slots (16,384 total) and is the preferred topology for horizontally scaled, write-heavy workloads. The minimum viable production cluster is six nodes: three masters and three replicas, one replica per master. [Redis Cluster does not support clusters with more than 35 nodes](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/). Static IP addresses are required — dynamic IPs are not supported because nodes must remain identifiable after reboots. Linux swap must be disabled on all cluster nodes to prevent latency spikes. [Hardware minimums for production Redis Enterprise nodes are 4 CPU cores and 15 GB RAM per node, with 8+ cores and 32+ GB RAM recommended](https://redis.io/docs/latest/embeds/hardware-requirements-embed/).

### 1.2 Persistence: RDB vs. AOF

Redis supports two persistence mechanisms with distinct durability/performance trade-offs.

**RDB (Redis Database snapshots):** Periodic point-in-time snapshots written to disk at configurable intervals. RDB offers fast restarts with large datasets and lower I/O overhead during normal operation, but creates a data-loss window equal to the snapshot interval — typically minutes. [RDB allows faster restarts with big datasets compared to AOF](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/).

**AOF (Append-Only File):** Logs every write operation. With `appendfsync everysec`, AOF provides at most one second of data loss exposure. [AOF with `appendfsync everysec` offers a good compromise between performance and durability](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/). AOF files grow over time and require periodic rewriting (BGREWRITEAOF) to compact them.

**Combined persistence** (both RDB and AOF enabled) is recommended when data durability requirements approach those of a primary database rather than a pure cache. [The general indication you should use both persistence methods is if you want a degree of data safety comparable to what PostgreSQL can provide](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/).

### 1.3 Memory Management and Eviction Policies

Redis is an entirely in-memory data structure store. Operators must configure `maxmemory` and an eviction policy to control behavior when memory is exhausted. [When the size of your cache exceeds the limit set by maxmemory, Redis will enforce your chosen eviction policy to prevent any further growth of the cache](https://redis.io/docs/latest/develop/reference/eviction/).

Key eviction policies:

| Policy | Behavior | Best For |
|--------|----------|----------|
| `allkeys-lru` | Evict least-recently-used key across all keys | General caching — most common default |
| `volatile-lru` | LRU only among keys with a TTL set | Mixed cache + persistent key workloads |
| `volatile-ttl` | Evict keys closest to expiration first | TTL-heavy workloads |
| `noeviction` | Return error when memory full | Durable data where loss is unacceptable |

[Most teams do well with allkeys-lru, which quietly removes the least-used keys as data grows](https://redis.io/docs/latest/develop/reference/eviction/). When replication or persistence is enabled, operators should [set maxmemory to leave RAM free to store replication and persistence buffers](https://redis.io/docs/latest/develop/reference/eviction/).

**NUMA and swap considerations:** On multi-socket servers, NUMA topology causes non-local memory accesses that degrade Redis latency. MongoDB documentation explicitly notes that NUMA and Linux do not work harmoniously and [suggests NUMA can be disabled](https://fromdual.com/do-not-underestimate-performance-impacts-of-swapping-on-numa-database-systems) — the same principle applies to Redis. Linux swappiness should be set to `1` or `0` on Redis hosts; swap activity causes severe latency spikes that trigger false-positive Sentinel failovers.

### 1.4 Monitoring Redis

Critical monitoring metrics for production Redis clusters:

- `used_memory` vs. `maxmemory`: ratio indicates eviction pressure
- `ReplicationLag` / `master_repl_offset` minus `slave_repl_offset`: measures replication health
- `master_link_status`: binary indicator of replica connectivity
- `keyspace_hits` / `keyspace_misses`: cache effectiveness ratio
- `instantaneous_ops_per_sec`: throughput baseline

[High replication lag alerts should trigger when lag exceeds 10,000 bytes for 5+ minutes; memory alerts should fire when usage exceeds 80% for caching workloads or 90% for primary storage workloads](https://www.mindfulchase.com/explore/troubleshooting-tips/databases/troubleshooting-redis-memory-limits,-replication-lag,-cluster-failures,-and-performance-bottlenecks.html).

Recommended tooling: [Redis Cluster monitoring with OpenTelemetry](https://oneuptime.com/blog/post/2026-02-06-redis-cluster-node-status-replication/view) covers node status, slot coverage, and replication health. Datadog, Grafana + Prometheus with `redis_exporter`, and AWS CloudWatch (for ElastiCache) are the primary production observability stacks.

---

## Section 2: MongoDB — Replica Sets, Sharding, WiredTiger, and Backup

### 2.1 Replica Set Operations

A MongoDB replica set is a group of mongod instances that maintain the same dataset, providing redundancy and high availability. [Replication lag is a delay between an operation on the primary and the application of that operation from the oplog to the secondary](https://www.mongodb.com/blog/post/replica-set-health-is-more-than-just-replication). The "replication oplog window" — the time difference between oldest and newest oplog entries — defines how long a secondary can be offline before requiring a full resync rather than incremental catch-up.

Key operational concerns for replica sets:
- Oplog sizing: too small an oplog window forces full resyncs after brief network partitions
- Election timeouts and priority settings affect failover behavior under failure scenarios
- Hidden members and delayed members have specialized operational overhead
- [Alert conditions should trigger when replication lag exceeds 60 seconds, when the oplog window falls below your recovery time objective, or when a node becomes unreachable](https://oneuptime.com/blog/post/2026-02-06-mongodb-replica-set-oplog-wiredtiger/view)

### 2.2 Sharding Architecture

MongoDB sharding distributes data horizontally across multiple shards. A production sharded cluster requires three distinct component types:

- **Config servers (CSRS):** Store cluster metadata and chunk routing information. [For a production deployment, deploy a config server replica set with at least three members](https://www.mongodb.com/docs/manual/tutorial/deploy-shard-cluster/). Config servers are deployed as a replica set (CSRS).
- **Mongos routers:** Stateless query routers that direct client traffic to the correct shard. Multiple mongos instances provide HA for the routing layer. [Mongos routers communicate frequently with config servers; as the number of routers increases, performance may degrade](https://www.mongodb.com/docs/manual/core/sharded-cluster-components/).
- **Shards:** Each shard is itself a replica set. [Each shard must be deployed as a replica set in production](https://www.mongodb.com/docs/manual/tutorial/deploy-shard-cluster/).

**Shard key selection is the highest-leverage and highest-risk decision in a MongoDB sharding deployment.** [A poor shard key can lead to data hotspots, uneven distribution, and performance degradation](https://kinsta.com/blog/mongodb-sharding/). Shard keys are immutable after collection creation in pre-5.0 MongoDB; changing shard keys requires full data migration. [MongoDB puts the burden on the user to manually place replica set members across nodes to avoid concentration of primaries — users either make errors or over-provision hardware](https://www.yugabyte.com/blog/overcoming-mongodb-sharding-and-replication-limitations-with-yugabyte-db/).

[For production deployments, sharded cluster replica sets should be deployed across at least three data centers](https://www.mongodb.com/docs/manual/tutorial/deploy-shard-cluster/) to tolerate data center failure.

### 2.3 WiredTiger Storage Engine Tuning

WiredTiger is the default and only supported storage engine for new MongoDB deployments. Key tuning parameters:

- **Cache size:** [A general rule is to allocate 50% of available RAM to WiredTiger cache](https://www.mongodb.com/docs/manual/core/wiredtiger/); setting it too high causes memory competition and swapping, while too low causes frequent cache eviction and increased latency.
- **Journal compression:** Snappy is the default; zlib and zstd offer higher compression ratios at higher CPU cost.
- **Compaction:** [WiredTiger blocks all operations during compaction with a database-level lock; run compact operation when storage reaches 80% of disk capacity](https://learnmongodbthehardway.com/schema/wiredtiger/).

**Checkpointing and journaling:** [Checkpoints provide consistent snapshots used during recovery; journaling logs all changes since the last checkpoint](https://www.mongodb.com/docs/manual/core/wiredtiger/). Both must be enabled for full durability guarantees.

### 2.4 Backup and Restore

Self-hosted MongoDB backup strategies include:

1. **mongodump/mongorestore:** Logical backup suitable for small datasets; slow on large clusters due to serialization overhead
2. **Filesystem snapshots (LVM/EBS):** Fast point-in-time snapshots; requires flushing writes first
3. **MongoDB Ops Manager / Cloud Manager:** Agent-based continuous backup with point-in-time restore capability — requires additional infrastructure and licensing

Restore testing is a frequently overlooked operational burden. An untested backup is not a backup. Validating restore procedures under load adds significant operational overhead to self-hosted deployments that managed services handle automatically.

---

## Section 3: Elasticsearch — Cluster Formation, ILM, Heap, and Upgrades

### 3.1 Cluster Formation and Shard Allocation

Elasticsearch clusters consist of master-eligible nodes (controlling cluster state), data nodes (storing and serving indexed data), and optionally ingest nodes and coordinating nodes. Cluster formation requires quorum among master-eligible nodes — a minimum of three master-eligible nodes is required to prevent split-brain.

**Shard sizing is a primary operational challenge.** [Target shard sizes in the 10–50 GB range; too many small shards cause high JVM heap pressure, slower cluster state updates, and painful restarts — a condition called "shard explosion"](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards). Elasticsearch uses its desired balance allocator to distribute shards based on data stream writes, shard counts, and disk usage heuristics. Poorly planned shard allocation leads to hot nodes, uneven resource utilization, and degraded search latency.

### 3.2 Heap Sizing and JVM Garbage Collection

Heap configuration is arguably the single most operationally critical parameter for Elasticsearch:

- [Set heap size to a maximum of 50% of available RAM](https://www.elastic.co/search-labs/blog/elasticsearch-heap-size-jvm-garbage-collection)
- [Beyond 32 GB, the JVM loses compressed OOPs (Ordinary Object Pointers), effectively doubling pointer sizes and reducing cache efficiency](https://www.elastic.co/search-labs/blog/elasticsearch-heap-size-jvm-garbage-collection) — heap must be kept at or below 31 GB
- [Always set `-Xms` and `-Xmx` to the same value to prevent dynamic heap resizing, which can trigger long garbage collections](https://www.sachith.co.uk/elasticsearch-opensearch-sizing-mappings-performance-tuning-guide-practical-guide-nov-2-2025/)

**Garbage collection tuning:** [Modern Elasticsearch defaults to the G1 Garbage Collector (G1GC), which is generally the best choice for large, multi-core systems](https://devops.aibit.im/article/jvm-tuning-elasticsearch-performance). Healthy GC targets: [young GC should complete within 50ms and occur approximately every 10 seconds; old GC should complete within 1 second and occur no more than once per 10 minutes](https://devops.aibit.im/article/jvm-tuning-elasticsearch-performance). GC pauses exceeding these thresholds cause cluster instability — nodes may be ejected from the cluster if they fail to respond to master pings during a stop-the-world GC pause.

### 3.3 Index Lifecycle Management (ILM)

ILM automates index management across five phases: hot, warm, cold, frozen, and delete. [ILM policies automate rollover, retention, and deletion to optimize performance, reliability, and storage costs for time-based indices](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management).

Operational requirements for ILM:
- All nodes in a cluster must run the same version for ILM policies to work reliably. [Although it might be possible to create and apply policies in a mixed-version cluster, there is no guarantee they will work as intended](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management).
- [ILM policies are stored in global cluster state and can be included in snapshots by setting `include_global_state: true`](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-and-snapshots.html).
- A restored index's `min_age` is calculated from when it was originally created or rolled over, not from the restoration time — an operationally significant nuance affecting post-restore behavior.

### 3.4 Rolling Upgrades

Elasticsearch supports rolling upgrades (upgrading one node at a time while the cluster remains operational), but the process carries meaningful operational risk:

- Cluster must be on the same major version before upgrading to the next major version
- ILM policies may fail in mixed-version states during the upgrade window
- Upgrade sequence: disable shard allocation → upgrade node → re-enable allocation → wait for green cluster state → proceed to next node
- Coordinating nodes and master-eligible nodes carry additional sequencing requirements

This process requires operator presence throughout the upgrade window. For large clusters, a rolling upgrade can span hours to days.

### 3.5 Snapshot and Restore

[Snapshot lifecycle management (SLM) automates backup of indices and manages snapshot retention](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-and-snapshots.html). Self-hosted operators must provision and manage a snapshot repository (S3-compatible object storage, NFS, or GCS). Snapshot restoration is the primary disaster recovery path; testing restores under load is an essential but operationally expensive obligation.

---

## Section 4: Cross-Cutting Operational Challenges

### 4.1 Version Compatibility and Rolling Upgrades

All three systems impose version homogeneity constraints that complicate maintenance:

- Redis Cluster requires all nodes to run compatible versions during upgrades
- MongoDB replica sets can tolerate a brief mixed-version state during rolling upgrades, but write operations targeting new features must wait until all members are upgraded
- Elasticsearch requires same-major-version homogeneity for ILM policies to function correctly

Version drift — where cluster nodes run different versions due to failed upgrades or deferred maintenance — is a significant operational debt item in self-hosted environments. Managed services handle version upgrades transparently or with a single API call.

### 4.2 Data Migration

Moving data between self-hosted clusters (e.g., scaling from a replica set to a sharded cluster in MongoDB, or rebalancing Elasticsearch shard allocation after adding nodes) requires operational windows, careful sequencing, and often causes temporary performance degradation. There are no general-purpose zero-downtime data migration tools across these three systems — each requires system-specific procedures.

### 4.3 Memory Management: OOM Prevention and Swap

OOM (Out of Memory) kill events are catastrophic for all three systems:
- Redis: OOM kill of a primary triggers an unplanned failover; persistence files may be corrupt if killed mid-write
- MongoDB: OOM kill during a write operation can require oplog-based recovery or resync
- Elasticsearch: OOM kill ejects a node from the cluster, triggering shard reallocation that can cascade across remaining nodes

Prevention requires:
- Configuring OS-level memory limits (`cgroups` / `systemd` memory limits) to allow graceful termination before OOM
- Setting `vm.overcommit_memory = 1` on Redis hosts (required by Redis) [UNVERIFIED: While widely recommended in Redis operational guides, the exact kernel parameter interaction with modern cgroup v2 configurations in 2025+ kernels requires environment-specific validation]
- Setting `vm.swappiness = 1` on Elasticsearch and MongoDB hosts to minimize swap use without eliminating it entirely

---

## Section 5: Operational Comparison — Self-Hosted vs. Managed Services

### 5.1 Comparison Table

| Capability | On-Premises (Self-Hosted) | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native (Managed Services) |
|------------|--------------------------|-----------------------------------|----------------------------------|
| **Redis / Caching** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Full cluster config, Sentinel/Cluster topology, persistence tuning, memory management, NUMA/swap | Redis Operator (Bitnami/Redis Enterprise), Kubernetes scheduling adds complexity | AWS ElastiCache, Azure Cache for Redis, GCP Memorystore |
| | redis-sentinel, redis-cli, Prometheus redis_exporter, Grafana | Helm charts, kubectl, redis_exporter sidecar | CloudWatch, Azure Monitor, Cloud Monitoring |
| | Est. FTE: 0.3–0.5 steady-state + 0.1 on-call | Est. FTE: 0.2–0.3 steady-state + 0.05 on-call | Est. FTE: 0.05–0.1 steady-state |
| **MongoDB / Document DB** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Replica set management, shard key selection, WiredTiger tuning, mongos/config server ops, backup procedures | MongoDB Community Operator or Percona Operator, PVC management | MongoDB Atlas, AWS DocumentDB, Azure Cosmos DB for MongoDB |
| | mongod, mongos, Ops Manager, Percona PMM, mongodump | Helm, kubectl, Percona PMM, k8s snapshots | Atlas monitoring, CloudWatch, Azure Monitor |
| | Est. FTE: 0.4–0.7 steady-state + 0.2 on-call | Est. FTE: 0.3–0.4 steady-state + 0.1 on-call | Est. FTE: 0.05–0.15 steady-state |
| **Elasticsearch / Search** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Cluster formation, heap/GC tuning, ILM configuration, shard allocation, rolling upgrades, snapshot repos | ECK (Elastic Cloud on Kubernetes) operator, complex JVM tuning still required | AWS OpenSearch Service, Elastic Cloud, Azure AI Search |
| | elasticsearch, kibana, Filebeat, Metricbeat, curator | ECK operator, kubectl, Helm, Prometheus ES exporter | CloudWatch, Kibana (managed), Elastic Observability |
| | Est. FTE: 0.5–0.8 steady-state + 0.2 on-call | Est. FTE: 0.4–0.6 steady-state + 0.15 on-call | Est. FTE: 0.1–0.2 steady-state |

**FTE Estimation Assumptions:**
- Steady-state FTE includes: monitoring review, patching cadence, capacity planning, backup validation, quarterly upgrade cycles
- On-call FTE is expressed as a fractional share of one engineer's time (e.g., 0.1 FTE on-call = one engineer sharing on-call rotation for this system among others)
- Estimates assume a medium-scale deployment (3–6 node clusters, 100 GB–1 TB data) with a single environment (production); multi-environment deployments multiply steady-state burden by ~1.5x
- Industry benchmarks: [self-hosted Elasticsearch estimated at 10–20 hours/month of operations labor at baseline](https://oneuptime.com/blog/post/2026-01-21-elastic-cloud-vs-self-hosted/view); MongoDB self-hosting is estimated to [reduce costs 40–60% but requires dedicated DevOps capacity](https://thedbadmin.com/blog/mongodb-atlas-vs-self-hosted-comparison)

### 5.2 Cost Context: Self-Hosted vs. Managed

**MongoDB:**
[Self-hosted MongoDB can provide monthly savings of approximately $7,500 (55%) compared to MongoDB Atlas in representative configurations](https://klouddb.io/case-study-on-running-mongodb-on-atlas-v-s-self-managed/). However, this ignores the FTE cost of dedicated DBA/DevOps hours. At US market rates ($120–$180/hr for senior database engineers), 40 FTE hours/month of dedicated MongoDB operational work costs $4,800–$7,200/month — largely eliminating the raw infrastructure savings. [Once database costs exceed 15% of infrastructure spend or $10,000/month, systematic evaluation of self-hosting alternatives is warranted](https://thedbadmin.com/blog/mongodb-atlas-vs-self-hosted-comparison).

**Elasticsearch:**
[Managed services (Elastic Cloud) charge a premium of approximately 30–50% above underlying infrastructure cost](https://pulse.support/kb/elastic-pricing-cloud-vs-self-managed). [Self-hosted Elasticsearch on AWS with 3x m5.large instances and 500 GB storage totals approximately $390/month in infrastructure, versus $500–$2,000+/month for comparable Elastic Cloud tiers](https://airbyte.com/data-engineering-resources/elasticsearch-pricing). [When engineering time, operational risk, downtime, and long-term maintenance are factored in, Elastic Cloud is cheaper for most organizations on a total cost of ownership basis](https://oneuptime.com/blog/post/2026-01-21-elastic-cloud-vs-self-hosted/view).

**Redis:**
[ElastiCache abstracts away most operational overhead by handling provisioning, patching, backups, and automatic failover, integrating natively with CloudWatch and other AWS services](https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/amazon-elasticache-and-self-managed-redis.html). [Self-hosted Redis is preferable when cost is the primary constraint and the team has operational expertise; ElastiCache is preferable when operational simplicity and seamless maintenance are prioritized](https://dzone.com/articles/elasticache-or-self-hosted-redis-on-ec2-which-is-t).

### 5.3 Managed Service Operational Profile

[Amazon DynamoDB requires no hardware provisioning, software patching, or server management, with zero-downtime maintenance as a serverless architecture](https://aws.amazon.com/blogs/database/key-considerations-when-choosing-a-database-for-your-generative-ai-applications/). [Amazon OpenSearch Service eliminates the operational overhead of managing underlying infrastructure, including cluster provisioning, scaling, and rolling updates](https://aws.amazon.com/opensearch-service/). [Amazon ElastiCache integrates seamlessly with other AWS services, offering scaling, patch management, monitoring, and cross-AZ high availability natively](https://dzone.com/articles/elasticache-or-self-hosted-redis-on-ec2-which-is-t).

The managed service model shifts operational focus from infrastructure maintenance to configuration optimization and cost governance — a substantially smaller and more tractable operational surface for ISV teams.

---

## Section 6: Monitoring Summary by System

| System | Cluster Health Metrics | Replication Metrics | Performance Metrics | Recommended Tooling |
|--------|----------------------|--------------------|--------------------|---------------------|
| Redis | Node availability, slot coverage (Cluster), quorum count (Sentinel) | `master_link_status`, `ReplicationLag`, `slave_repl_offset` vs `master_repl_offset` | `instantaneous_ops_per_sec`, hit/miss ratio, `used_memory`/`maxmemory` | Prometheus + `redis_exporter`, Grafana, Datadog |
| MongoDB | Replica set member states, election frequency, oplog window duration | `replication lag` (seconds), oplog window (hours), `rs.printSecondaryReplicationInfo()` | WiredTiger cache hit ratio, query execution stats, index usage | Percona PMM, MongoDB Ops Manager, Prometheus + `mongodb_exporter` |
| Elasticsearch | Cluster status (green/yellow/red), node availability, shard allocation state | N/A (not a primary/replica model — uses segment replication) | Heap usage %, GC pause duration, query latency p95/p99, indexing throughput | Kibana Monitoring, Prometheus + `elasticsearch_exporter`, Elastic APM |

---

## Key Takeaways

- **Operational complexity is highest for Elasticsearch (5/5) and substantial for MongoDB and Redis (4/5) in self-hosted on-premises deployments.** The expertise required to correctly size JVM heap, tune WiredTiger cache, and configure Redis eviction policies is scarce and expensive — typically requiring engineers at the senior/staff level.

- **The FTE cost of self-hosted operations often matches or exceeds managed service premiums at medium scale.** At common US market rates, 40+ FTE hours/month of database operational work eliminates the 40–60% infrastructure cost savings that self-hosting delivers on paper. The economic case for self-hosting strengthens only at large scale (multi-TB, dedicated DBRE team) or in regulated environments where managed services are not permitted.

- **Managed Kubernetes (EKS/AKS/GKE) is not a shortcut to managed-service simplicity.** Running Redis, MongoDB, or Elasticsearch via Kubernetes operators (ECK, Percona Operator, Bitnami charts) reduces infrastructure management burden by approximately one difficulty point but does not eliminate JVM tuning, shard allocation management, or persistence configuration requirements.

- **Shard key selection in MongoDB and shard sizing in Elasticsearch are irreversible decisions with major long-term consequences.** Both require domain expertise at design time and are the most common root cause of performance crises in self-hosted NoSQL deployments.

- **For ISVs in early-to-mid growth stages, the risk-adjusted total cost of ownership strongly favors managed services** (Atlas, ElastiCache, OpenSearch Service, Cosmos DB). The operational simplicity premium of 30–50% above infrastructure cost is justified by the elimination of on-call burden, upgrade risk, and the need to hire specialized database engineers. See [F41: Relational Database Operations] for comparative context on self-hosted RDBMS operational profiles.

---

## Sources

1. [Redis Sentinel High Availability — Official Redis Documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)
2. [Redis Cluster Scaling — Official Redis Documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/)
3. [Redis Persistence (RDB and AOF) — Official Redis Documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
4. [Redis Key Eviction — Official Redis Documentation](https://redis.io/docs/latest/develop/reference/eviction/)
5. [Redis Hardware Requirements (Production) — Redis Docs](https://redis.io/docs/latest/embeds/hardware-requirements-embed/)
6. [Redis Cluster Specification — Redis Docs](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)
7. [Deploy a Self-Managed MongoDB Sharded Cluster — MongoDB Docs](https://www.mongodb.com/docs/manual/tutorial/deploy-shard-cluster/)
8. [MongoDB Sharded Cluster Components — MongoDB Docs](https://www.mongodb.com/docs/manual/core/sharded-cluster-components/)
9. [WiredTiger Storage Engine — MongoDB Docs](https://www.mongodb.com/docs/manual/core/wiredtiger/)
10. [MongoDB Replica Set Health — MongoDB Blog](https://www.mongodb.com/blog/post/replica-set-health-is-more-than-just-replication)
11. [MongoDB Replica Set Monitoring (OpenTelemetry) — OneUptime Blog, 2026](https://oneuptime.com/blog/post/2026-02-06-mongodb-replica-set-oplog-wiredtiger/view)
12. [Elasticsearch Index Lifecycle Management — Elastic Docs](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management)
13. [Elasticsearch Heap Size and JVM GC — Elastic Search Labs](https://www.elastic.co/search-labs/blog/elasticsearch-heap-size-jvm-garbage-collection)
14. [Elasticsearch Sizing and Mappings Performance Tuning Guide (Nov 2025) — Sachith Dassanayake](https://www.sachith.co.uk/elasticsearch-opensearch-sizing-mappings-performance-tuning-guide-practical-guide-nov-2-2025/)
15. [JVM Tuning for Elasticsearch — DevOps Knowledge Hub](https://devops.aibit.im/article/jvm-tuning-elasticsearch-performance)
16. [Size Your Shards — Elastic Docs](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards)
17. [ILM and Snapshots — Elastic Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-and-snapshots.html)
18. [Redis Cluster Node Status and Replication with OpenTelemetry — OneUptime Blog, 2026](https://oneuptime.com/blog/post/2026-02-06-redis-cluster-node-status-replication/view)
19. [Troubleshooting Redis: Memory Limits, Replication Lag, Cluster Failures — Mindful Chase](https://www.mindfulchase.com/explore/troubleshooting-tips/databases/troubleshooting-redis-memory-limits,-replication-lag,-cluster-failures,-and-performance-bottlenecks.html)
20. [Elastic Cloud vs Self-Hosted Elasticsearch — OneUptime Blog, January 2026](https://oneuptime.com/blog/post/2026-01-21-elastic-cloud-vs-self-hosted/view)
21. [Elasticsearch Pricing Guide: Cloud & Self-Managed — Airbyte](https://airbyte.com/data-engineering-resources/elasticsearch-pricing)
22. [Elasticsearch Pricing: Cloud vs Self-Managed — Pulse Support](https://pulse.support/kb/elastic-pricing-cloud-vs-self-managed)
23. [MongoDB Atlas vs Self-Hosted Comparison 2025 — TheDBAdmin Blog](https://thedbadmin.com/blog/mongodb-atlas-vs-self-hosted-comparison)
24. [Cost Savings: MongoDB Atlas vs Self-Managed — KloudDB Case Study](https://klouddb.io/case-study-on-running-mongodb-on-atlas-v-s-self-managed/)
25. [MongoDB Sharding Operational Complexity — Kinsta Blog](https://kinsta.com/blog/mongodb-sharding/)
26. [Overcoming MongoDB Sharding and Replication Limitations — YugaByte Blog](https://www.yugabyte.com/blog/overcoming-mongodb-sharding-and-replication-limitations-with-yugabyte-db/)
27. [ElastiCache vs Self-Hosted Redis on EC2 — DZone](https://dzone.com/articles/elasticache-or-self-hosted-redis-on-ec2-which-is-t)
28. [Amazon ElastiCache and Self-Managed Redis — AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/amazon-elasticache-and-self-managed-redis.html)
29. [Key Considerations for Choosing a Database for Generative AI Applications — AWS Blog](https://aws.amazon.com/blogs/database/key-considerations-when-choosing-a-database-for-your-generative-ai-applications/)
30. [Amazon OpenSearch Service — AWS](https://aws.amazon.com/opensearch-service/)
31. [WiredTiger Storage Engine Overview — Learn MongoDB the Hard Way](https://learnmongodbthehardway.com/schema/wiredtiger/)
32. [NUMA and Swapping Performance Impact on Databases — FromDual](https://fromdual.com/do-not-underestimate-performance-impacts-of-swapping-on-numa-database-systems)
33. [WiredTiger Compaction Operational Notes — MongoDB Ampere Tuning Guide](https://amperecomputing.com/en/tuning-guides/mongoDB-tuning-guide)
34. [Redis OSS vs Enterprise vs ElastiCache Managed Service Comparison — OneUptime Blog, January 2026](https://oneuptime.com/blog/post/2026-01-21-redis-oss-vs-enterprise-vs-elasticache/view)
