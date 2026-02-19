# F44 — On-Premises Message Queues & Event Streaming

**Research Date:** 2026-02-18
**Scope:** Operational requirements, characteristics, and trade-offs of self-hosting message queues and event streaming platforms (Apache Kafka, RabbitMQ, NATS) on-premises, with comparison to managed equivalents (MSK, Amazon MQ, Azure Event Hubs, GCP Pub/Sub).

---

## Executive Summary

Self-hosting message queues and event streaming platforms delivers maximum control and eliminates vendor lock-in, but imposes an operational burden that is frequently underestimated by ISVs. Apache Kafka's March 2025 release of version 4.0 eliminated ZooKeeper entirely, mandating KRaft mode and requiring a mandatory bridge migration through Kafka 3.9 for any cluster still on ZooKeeper — a non-trivial operational event for on-premises operators. A conservative benchmark places a small-to-medium self-hosted Kafka production environment at approximately 2.0 FTE of sustained engineering effort, versus roughly 0.5 FTE for managed equivalents such as AWS MSK, representing a 4x operational multiplier before accounting for on-call burden. RabbitMQ and NATS carry meaningfully lower operational footprints than Kafka, but still demand dedicated expertise in cluster formation, memory tuning, and schema management that managed offerings abstract away. ISVs deploying to customer on-premises hardware face the additional compounding challenge of operating without cloud provider tooling, making monitoring, rolling upgrades, and disk capacity planning significantly more labor-intensive.

---

## 1. Apache Kafka: Cluster Management and Core Operations

### 1.1 ZooKeeper Removal and KRaft Architecture (2025)

Apache Kafka 4.0, released on [March 18, 2025](https://www.confluent.io/blog/latest-apache-kafka-release/), represents the most significant architectural change in Kafka's history: [ZooKeeper mode has been completely removed](https://github.com/AutoMQ/automq/wiki/Apache-Kafka-4.0:-KRaft,-New-Features,-and-Migration). All clusters must now run in KRaft mode, where Kafka manages its metadata internally in a topic called `@metadata`, replicated across a quorum of controller nodes.

For on-premises ISV deployments, the operational impact is substantial. Any cluster still running on ZooKeeper must first migrate to KRaft using [Kafka 3.9 as a mandatory bridge release](https://kafka.apache.org/40/getting-started/upgrade/). The migration process involves multiple sequential phases — a hybrid phase, a dual-write phase, and a final KRaft-only cutover — each requiring operator coordination and monitoring. Critically, [reverting to ZooKeeper after migration is not supported](https://kafka.apache.org/41/operations/kraft/), making the migration irreversible. Additionally, [Kafka 4.0 dropped support for Java 8; brokers and tools now require Java 17](https://www.infoq.com/news/2025/04/kafka-4-kraft-architecture/).

The KRaft architecture provides operational benefits once complete. [Eliminating ZooKeeper removes a second distributed system that operators had to provision, monitor, and scale separately](https://developer.confluent.io/learn/kraft/), and produces faster, more deterministic controller leader elections. However, the migration itself is a high-risk operational event for on-premises teams without managed rollback tooling.

### 1.2 Broker Configuration and ISR Management

Kafka's durability model depends on In-Sync Replicas (ISR). [A replica is considered in-sync if it has fetched the leader's latest messages within the `replica.lag.time.max.ms` window (default: 30 seconds)](https://docs.cloudera.com/runtime/7.1.1/kafka-performance-tuning/topics/kafka-tune-broker-tuning-isr.html). If a replica falls behind, it is removed from the ISR, which reduces fault tolerance until it catches up.

[Unclean leader election is disabled by default](https://www.lydtechconsulting.com/blog/kafka-replication), meaning that if no in-sync replica is available when a leader fails, Kafka will halt writes to that partition until an in-sync replica recovers. Enabling unclean leader election restores availability but risks data loss — a CAP theorem trade-off that on-premises operators must explicitly configure and monitor.

Kafka 4.0 introduces Eligible Leader Replicas (ELR) via [KIP-966](https://developers.redhat.com/blog/2025/04/01/kafka-monthly-digest-march-2025), which tracks replicas that are not in the ISR but are safe to promote without data loss. This reduces the risk of prolonged unavailability in failure scenarios but requires operators to understand a new layer of replica state.

### 1.3 Partition Rebalancing and Topic Configuration

Partition rebalancing is a persistent operational task in self-hosted Kafka. When brokers are added, removed, or disk imbalance accumulates, operators must manually trigger partition reassignment using `kafka-reassign-partitions.sh` or a third-party tool such as [Cruise Control](https://www.conduktor.io/glossary/kafka-capacity-planning). During reassignment, inter-broker replication traffic increases significantly, which can saturate network links.

Consumer group rebalancing occurs whenever consumers join or leave a group or when partition counts change. [During a rebalancing event, all message processing for the consumer group pauses](https://www.confluent.io/learn/kafka-dead-letter-queue/). Kafka's cooperative sticky rebalancing protocol (introduced in earlier versions and now default in 4.x) minimizes the scope of reassignments, but on-premises operators must monitor for excessive rebalancing events that indicate consumer instability.

### 1.4 Disk Sizing and Network Bandwidth for Retention

Disk is the primary resource constraint in Kafka. A practical sizing formula from [AWS best practices](https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/) is:

```
Daily Storage = Messages/sec × Message Size (bytes) × 86,400 × Replication Factor
```

For example: 1,000 messages/sec × 1 KB × 86,400 seconds × replication factor 3 = **~259 GB/day**, or approximately **1.8 TB** per topic for a 7-day retention window. A 20-30% headroom buffer is required for log segment metadata and operational safety.

Network bandwidth requirements are multiplicative. [In a 3-broker cluster with a single topic, replication factor 3, one producer, and one consumer: for every 75 MB written to the partition leader, 150 MB is transmitted for replication and 75 MB to the consumer — a 3x write amplification factor](https://jbcodeforce.github.io/kafka-studies/sizing/). [Best practice is to target actual throughput at no more than 80% of theoretical sustained NIC capacity](https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/).

### 1.5 Rolling Upgrades and Version Compatibility

[Upgrading within the Kafka 3.x line allows normal rolling upgrades with strong backwards compatibility](https://www.openlogic.com/blog/upgrade-kafka-4-planning). Upgrading to 4.0 is substantially more complex: [clients including Streams and Connect must be on version 2.1 or higher before upgrading brokers to 4.0](https://kafka.apache.org/40/getting-started/upgrade/), and the metadata version must be at least 3.3.x.

In Kubernetes on-premises environments, rolling upgrades are particularly challenging. [Teams face complex issues with statefulness, leader rebalancing, and possible downtime when upgrading Kafka in Kubernetes](https://www.automq.com/blog/kafka-upgrades-in-kubernetes). On-premises operators without a managed Kubernetes control plane must also coordinate upgrade scheduling manually.

---

## 2. RabbitMQ: Cluster Formation and Queue Management

### 2.1 Cluster Formation and Quorum Queues

RabbitMQ clustering uses Erlang's distributed systems primitives. Classic mirrored queues — the legacy HA mechanism — are being deprecated in favor of Quorum Queues, which use the Raft consensus protocol. [The RabbitMQ team documented the migration path and benefits in July 2025](https://www.rabbitmq.com/blog/2025/07/29/latest-benefits-of-rmq-and-migrating-to-qq-along-the-way).

[Quorum Queues require a minimum of 3 nodes and must be deployed in an odd-node configuration (3, 5, or 7) to ensure Raft consensus](https://www.rabbitmq.com/docs/quorum-queues). Unlike classic mirrored queues, replicas of a quorum queue are explicitly managed by the operator. [When a new node is added to the cluster, it hosts no quorum queue members unless the operator explicitly adds it to the membership list](https://www.rabbitmq.com/docs/quorum-queues) — a counter-intuitive behavior that frequently causes on-premises operators to believe scaling is complete when it is not.

[Quorum Queues require more disk and memory than classic queues due to replication overhead, and assume reasonably stable I/O latency; network-attached storage may not provide this consistently](https://www.rabbitmq.com/docs/production-checklist).

### 2.2 Memory Management

Memory pressure is the most common RabbitMQ production incident. [By default, RabbitMQ blocks all publisher connections when memory usage exceeds 60% of available RAM (the `vm_memory_high_watermark` setting), which defaults to 0.6 in RabbitMQ 4.0](https://www.rabbitmq.com/docs/memory). The [recommended production range for `vm_memory_high_watermark.relative` is 0.4 to 0.7](https://www.rabbitmq.com/docs/memory), though this requires careful tuning based on workload patterns.

[In containerized or Kubernetes-based on-premises environments, using a relative memory threshold is not recommended; an absolute threshold is preferred](https://docs.vmware.com/en/VMware-RabbitMQ-for-Kubernetes/1/rmq/memory.html). [Nodes hosting RabbitMQ should have at least 256 MiB of memory available at all times; on systems with 4 GB or less total RAM, the risk of OOM-kill increases significantly](https://www.rabbitmq.com/docs/memory).

### 2.3 Shovel, Federation, and Exchange Management

RabbitMQ's Shovel and Federation plugins enable message routing across clusters or data centers — a capability relevant for ISVs deploying to geographically distributed customer sites. Shovel provides point-to-point message forwarding between brokers (useful for data migration or multi-site routing), while Federation provides broader, topology-aware exchange and queue linking. Both require explicit configuration, ongoing monitoring for link health, and operator understanding of AMQP exchange/binding semantics. [Amazon MQ simplifies this management layer by handling the underlying infrastructure and providing built-in monitoring dashboards](https://www.coudo.ai/blog/amazon-mq-vs-rabbitmq-a-comprehensive-guide), which self-hosted RabbitMQ operators must replicate manually.

### 2.4 Rolling Upgrades and Version Compatibility

RabbitMQ rolling upgrades require careful attention to Erlang version compatibility. Each RabbitMQ release specifies a supported Erlang version range; upgrading RabbitMQ often requires a coordinated Erlang upgrade. The [RabbitMQ production checklist](https://www.rabbitmq.com/docs/production-checklist) recommends testing upgrades in a staging environment that mirrors production topology before applying to live clusters. [The RabbitMQ clustering guide](https://www.rabbitmq.com/docs/clustering) documents the required node quorum maintenance during rolling restarts for quorum queues.

---

## 3. NATS: JetStream Configuration and Cluster Management

### 3.1 JetStream Clustering Architecture

NATS with JetStream uses an optimized Raft implementation for distributed consensus. [JetStream clustering is based on Raft, but uses a NATS-optimized Raft algorithm that combines the data plane for replicating messages with control plane consensus messages, reducing the typical high traffic overhead of standard Raft implementations](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering).

[Cluster sizes of 3 or 5 JetStream-enabled servers are recommended. For a 3-node cluster, at least 2 servers must be available to store new messages; for a 5-node cluster, at least 3 are required](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering). Each stream creates its own Raft group, meaning a cluster hosting many streams carries a proportional control-plane overhead.

[A hybrid topology is possible and sometimes recommended: dedicated storage-optimized machines run JetStream, while compute-optimized nodes handle non-persistent NATS traffic](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering). This separation can reduce operational costs but adds topological complexity.

### 3.2 Resource Requirements vs. Kafka and RabbitMQ

NATS is significantly more resource-efficient than Kafka. [A production NATS JetStream node requires a minimum of 2 vCPU and 4 GB RAM, compared to Kafka's 8+ cores and 64-128 GB RAM recommendation for production workloads](https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks). [Each NATS server node must have a unique `server_name` configured; this is required for JetStream cluster participation](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering).

On a 4 vCPU, 8 GB RAM VPS benchmark, [NATS JetStream achieved 200,000–400,000 messages/second with persistence, compared to Kafka's 500,000–1,000,000+ with batching and RabbitMQ's 50,000–100,000 with durability guarantees](https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks). For ISV workloads that do not require Kafka-scale throughput, NATS's lower operational footprint is a meaningful advantage.

### 3.3 Message Retention and Consumer Management

JetStream provides configurable message retention policies (limits-based, interest-based, or workqueue-based) at the stream level. Consumer state tracking is server-side, eliminating the separate consumer offset management that Kafka operators must perform. Dead-letter and retry workflows in NATS are handled via consumer deliver-policy and nack configurations rather than separate DLQ topics, simplifying the operational model for message replay scenarios.

---

## 4. Cross-Cutting Operational Topics

### 4.1 Dead Letter Handling and Message Replay

In Kafka, [a Dead Letter Queue (DLQ) is implemented as a separate Kafka topic to which failed messages are routed by consumer logic](https://www.confluent.io/learn/kafka-dead-letter-queue/). [Kafka Connect does not provide native replay support; operators require a custom script or lightweight replay service to reprocess DLQ messages](https://www.superstream.ai/blog/kafka-dead-letter-queue). A critical operational risk is [blind replay, which can re-trigger side effects such as duplicate payments or duplicate API writes](https://skey.uk/post/kafka-dead-letter-queue-troubleshooting-guide/). Self-hosted operators must build DLQ monitoring, retry-limit enforcement, and replay tooling independently.

In RabbitMQ, dead-lettering is a first-class feature configurable per-queue via the `x-dead-letter-exchange` argument. In NATS, consumer nack policies and max-delivery limits provide equivalent behavior without separate topic management.

### 4.2 Schema Registry: Self-Hosted Operation

Schema management is an often-overlooked operational component for Kafka-based pipelines. [Confluent Schema Registry stores schemas in a Kafka topic as a durable, replicated backend and uses a single-primary architecture where one node handles writes while all nodes serve reads](https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025). Self-hosting requires operators to deploy, monitor, and maintain this as a separate HA component.

[The default compatibility mode is BACKWARD, meaning new schema versions can read data written by previous versions](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html). Operators must actively govern compatibility transitions, particularly for FORWARD or FULL compatibility, and must avoid deleting required fields or changing field types without default values. [As a self-hosted solution, you are fully responsible for deployment, high availability, monitoring, and backups of the schema registry](https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025).

[Apicurio Registry is a fully open-source CNCF-governed alternative that supports pluggable storage backends (PostgreSQL, in-memory, or KafkaSQL) and extends beyond Kafka to OpenAPI, AsyncAPI, and GraphQL schemas](https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025), making it relevant for ISVs with polyglot API landscapes.

### 4.3 Monitoring: Key Metrics and Alerting Thresholds

Self-hosted message queue monitoring requires a custom observability stack. The core metrics for Kafka are: [consumer lag (records-lag-max), under-replicated partitions, offline partitions, MessagesInPerSec, BytesOutPerSec, CPU usage, disk I/O, and network throughput](https://www.instaclustr.com/education/apache-kafka/kafka-monitoring-key-metrics-and-5-tools-to-know-in-2025/).

[The recommended alerting approach uses dynamic, context-aware thresholds rather than static values — alerts should only fire when a metric exceeds threshold for 5 or more minutes, reducing false positives. SLO alignment is critical: if the delivery SLO is 5 seconds, end-to-end latency must be tracked accordingly](https://www.instaclustr.com/education/apache-kafka/kafka-monitoring-key-metrics-and-5-tools-to-know-in-2025/).

[Burrow, developed by LinkedIn, evaluates consumer lag dynamically over a sliding window rather than using static thresholds, reducing false positives for bursty workloads](https://sematext.com/blog/kafka-consumer-lag-offsets-monitoring/). [Prometheus with PromQL and Datadog with prebuilt Kafka dashboards are the two most commonly cited commercial and open-source monitoring solutions in 2025](https://cubeapm.com/blog/top-kafka-monitoring-tools/). On-premises ISV deployments without access to cloud-native monitoring must deploy and maintain this stack independently.

---

## 5. Operational Complexity Comparison Table

| Capability | On-Premises (Self-Hosted) | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native (MSK/Amazon MQ/Event Hubs/Pub-Sub) |
|---|---|---|---|
| **Kafka Cluster Management** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Full broker lifecycle, KRaft migration, partition rebalancing, ISR management | Strimzi/Confluent Operator; K8s adds StatefulSet complexity | AWS MSK/Confluent Cloud handle broker provisioning and patching |
| | Cruise Control, `kafka-reassign-partitions.sh`, custom runbooks | Helm charts, rolling update strategies | AWS Console, Confluent Control Center |
| | Est. FTE: 1.5–2.5 (steady state) | Est. FTE: 1.0–1.5 | Est. FTE: 0.3–0.5 |
| **RabbitMQ Cluster Management** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Quorum queue membership management, memory watermark tuning, Erlang version coordination | RabbitMQ Operator for K8s; simplifies rolling upgrades | Amazon MQ handles patching, HA failover, and broker configuration |
| | rabbitmqctl, Prometheus/Grafana, manual shovel config | Helm + operator reconciliation | AWS Console, CloudWatch integration |
| | Est. FTE: 0.75–1.25 | Est. FTE: 0.5–0.75 | Est. FTE: 0.2–0.4 |
| **NATS JetStream Management** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Cluster node naming, Raft quorum management, stream/consumer configuration | NATS Helm chart; simpler StatefulSet needs than Kafka | Synadia Cloud (managed NATS); minimal operator involvement |
| | nats CLI, NATS Surveyor, Prometheus exporter | K8s native probes + NATS Surveyor | Synadia Cloud dashboard |
| | Est. FTE: 0.3–0.6 | Est. FTE: 0.2–0.4 | Est. FTE: 0.05–0.15 |
| **Schema Registry** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Deploy, HA, backup, and monitor as separate component; schema evolution governance | Deploy via Helm; K8s health probes available | AWS Glue Schema Registry or Confluent Cloud SR (fully managed) |
| | Confluent SR or Apicurio + PostgreSQL | Confluent Operator includes SR | AWS Glue API |
| | Est. FTE: 0.25–0.5 (shared with Kafka FTE) | Est. FTE: 0.1–0.25 | Est. FTE: ~0.05 |
| **Monitoring and Alerting** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Full observability stack deployment (Prometheus, Grafana, Burrow, alertmanager) | Managed K8s metrics server + Prometheus operator | Built-in CloudWatch/Azure Monitor/GCP Cloud Monitoring |
| | JMX exporters, custom dashboards, on-call runbooks | Helm-based Prometheus stack | Cloud-native alerting policies |
| | Est. FTE: 0.5 (shared DevOps) | Est. FTE: 0.25 | Est. FTE: ~0.1 |
| **Rolling Upgrades** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Manual broker-by-broker restart sequencing; KRaft migration is irreversible | Rolling update via StatefulSet; Strimzi automates Kafka upgrades | Managed upgrade windows; operator-initiated with one click |
| | Custom runbooks, pre-upgrade checklist, manual rollback | Operator-managed; requires K8s expertise | MSK/Event Hubs version management |
| | Est. FTE: Absorbed into cluster FTE above | Est. FTE: Absorbed into cluster FTE | Est. FTE: Minimal |

---

## 6. FTE Estimation Framework

**Assumptions:**
- Production environment: 3-broker Kafka cluster with 3-node Schema Registry, 3-node RabbitMQ cluster, 3-node NATS JetStream cluster
- "Steady-state" FTE excludes initial setup (which carries a one-time 2–6 week burst per platform)
- On-call burden is estimated separately as 0.1–0.2 FTE for on-premises (covering paging, incident response, and postmortems)
- FTE ranges reflect small-to-medium ISV deployments; enterprise scale adds roughly 0.5–1.0 FTE per platform

| Platform | On-Prem FTE (Steady State) | On-Prem On-Call FTE | Managed K8s FTE | Cloud-Native FTE | Benchmark Source |
|---|---|---|---|---|---|
| Apache Kafka (full stack) | 1.5–2.5 | +0.15–0.25 | 1.0–1.5 | 0.3–0.5 | [Confluent / AutoMQ analysis](https://www.automq.com/blog/self-hosted-kafka-vs-managed-kafka); [OneUptime comparison](https://oneuptime.com/blog/post/2026-01-21-kafka-managed-comparison/view) |
| RabbitMQ | 0.75–1.25 | +0.10–0.15 | 0.5–0.75 | 0.2–0.4 | [UNVERIFIED — derived from relative complexity vs. Kafka] |
| NATS JetStream | 0.3–0.6 | +0.05–0.10 | 0.2–0.4 | 0.05–0.15 | [UNVERIFIED — derived from resource requirement benchmarks] |
| Schema Registry (Kafka add-on) | +0.25–0.5 | +0.05 | +0.1–0.25 | ~+0.05 | [AutoMQ Schema Registry guide](https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025) |

[UNVERIFIED items: RabbitMQ and NATS FTE estimates are derived from relative operational complexity benchmarks rather than directly cited published studies. The Kafka FTE figures are consistent across multiple industry sources (Confluent, AutoMQ, OneUptime). The RabbitMQ and NATS figures are believed to be directionally accurate based on the significantly lower infrastructure requirements and configuration surface area of both platforms versus Kafka.]

---

## 7. Operational Hours Per Week: Self-Hosted vs. Managed

| Task Category | Self-Hosted Kafka (hrs/wk) | MSK (hrs/wk) | Self-Hosted RabbitMQ (hrs/wk) | Amazon MQ (hrs/wk) |
|---|---|---|---|---|
| Broker/Node Health Monitoring | 3–5 | 0.5–1 | 2–3 | 0.5 |
| Partition/Queue Rebalancing | 2–4 | 0 (automated) | 1–2 | 0 |
| Upgrade Planning & Execution | 4–8 (event-based) | 0.5 (per version, managed) | 2–4 (event-based) | 0 (managed) |
| Schema Registry Operations | 1–2 | 0 (Glue) | N/A | N/A |
| Incident Response (avg/wk) | 2–5 | 0.5–1 | 1–3 | 0.5 |
| Capacity Planning | 1–2 | 0.5 | 0.5–1 | 0.25 |
| **Total Estimated hrs/wk** | **13–26** | **2–3** | **6–13** | **1.25–2** |

[Operational hours are derived from: [OneUptime MSK vs. self-hosted analysis](https://oneuptime.com/blog/post/2026-01-21-kafka-managed-comparison/view); [Confluent FTE framework](https://www.confluent.io/blog/understanding-and-optimizing-your-kafka-costs-part-2-development-and-operations/); [Amazon MQ vs. RabbitMQ comparison](https://www.coudo.ai/blog/amazon-mq-vs-rabbitmq-benchmarking-messaging-platforms-for-2025). RabbitMQ and NATS self-hosted hours are [UNVERIFIED] but derived from the operational complexity benchmarks above.]

---

## 8. Infrastructure Specifications Summary

| Platform | Min. Production vCPU | Min. Production RAM | Typical Storage | Network Requirement |
|---|---|---|---|---|
| Apache Kafka (per broker) | 8+ cores | 64–128 GB | 8 TB SAS/SSD per broker | 10 GbE NIC recommended |
| RabbitMQ (per node) | 4+ | 8 GB | Dependent on queue depth | 1 GbE minimum; 10 GbE for high throughput |
| NATS JetStream (per node) | 2+ | 4 GB | Dependent on stream retention | 1 GbE minimum |

Sources: [NATS JetStream vs. RabbitMQ vs. Kafka benchmarks (2025)](https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks); [Kafka hardware recommendations](https://sanj.dev/post/nats-kafka-rabbitmq-messaging-comparison); [NATS docs](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering)

---

## Key Takeaways

- **Kafka 4.0 on-premises is a migration commitment, not just an upgrade.** The mandatory ZooKeeper-to-KRaft migration via the 3.9 bridge release is irreversible, requires careful phasing, and carries temporary CPU/memory overhead during transition. ISVs deploying to customer hardware must build migration runbooks and communicate the operational window clearly. See F40 (Networking) for network capacity requirements during replication-heavy events.

- **Self-hosted Kafka demands approximately 4x the operational FTE of managed equivalents.** Published estimates place a small-to-medium self-hosted Kafka cluster at 1.5–2.5 FTE steady-state versus 0.3–0.5 FTE for MSK, with the differential widest for partition management, rolling upgrades, and schema registry operations. ISVs must price this labor into on-premises deployment contracts or accept the risk of underfunded operations.

- **RabbitMQ's quorum queue migration is non-optional for new production deployments** and requires a minimum 3-node cluster with explicit replica membership management. Memory watermark tuning is the most common source of production incidents and requires node-specific calibration that managed Amazon MQ handles automatically.

- **NATS JetStream offers the lowest self-hosted operational burden** of the three platforms, with production clusters viable on 2 vCPU / 4 GB RAM nodes and an estimated 0.3–0.6 FTE steady-state. For ISV workloads that do not require Kafka-scale throughput (>500K msg/sec), NATS represents a materially lower operational risk profile for on-premises deployment.

- **Monitoring and schema governance are hidden operational costs.** On-premises operators must deploy and maintain a complete observability stack (Prometheus, Grafana, Burrow, alertmanager) that managed services provide as built-in capabilities. Schema Registry adds a separate HA component requiring its own deployment, monitoring, and backup discipline. These costs are frequently excluded from on-premises TCO estimates but represent 0.5–1.0 FTE of shared DevOps capacity in practice.

---

## Sources

1. [Apache Kafka 4.0 Upgrade Guide — kafka.apache.org](https://kafka.apache.org/40/getting-started/upgrade/)
2. [Apache Kafka 4.0: KRaft, New Features, and Migration — AutoMQ/GitHub Wiki](https://github.com/AutoMQ/automq/wiki/Apache-Kafka-4.0:-KRaft,-New-Features,-and-Migration)
3. [KRaft Operations — Apache Kafka 4.1 Docs](https://kafka.apache.org/41/operations/kraft/)
4. [KRaft Developer Overview — Confluent](https://developer.confluent.io/learn/kraft/)
5. [Apache Kafka 4.0 Release Blog — Confluent](https://www.confluent.io/blog/latest-apache-kafka-release/)
6. [Kafka 4.0: KRaft Simplifies Architecture — InfoQ (April 2025)](https://www.infoq.com/news/2025/04/kafka-4-kraft-architecture/)
7. [Kafka Monthly Digest: March 2025 — Red Hat Developer](https://developers.redhat.com/blog/2025/04/01/kafka-monthly-digest-march-2025)
8. [Exploring Kafka 4: Changes and Upgrade Considerations — OpenLogic](https://www.openlogic.com/blog/upgrade-kafka-4-planning)
9. [Upgrading Kafka in Kubernetes — AutoMQ Blog](https://www.automq.com/blog/kafka-upgrades-in-kubernetes)
10. [Deep Dive into Apache Kafka's KRaft Protocol — Red Hat Developer (Sept 2025)](https://developers.redhat.com/articles/2025/09/17/deep-dive-apache-kafkas-kraft-protocol)
11. [RabbitMQ Quorum Queues — Official Docs](https://www.rabbitmq.com/docs/quorum-queues)
12. [Migrating from Classic Mirrored Queues to Quorum Queues (July 2025) — RabbitMQ Blog](https://www.rabbitmq.com/blog/2025/07/29/latest-benefits-of-rmq-and-migrating-to-qq-along-the-way)
13. [RabbitMQ Production Deployment Guidelines — Official Docs](https://www.rabbitmq.com/docs/production-checklist)
14. [RabbitMQ Memory Threshold Configuration — Official Docs](https://www.rabbitmq.com/docs/memory)
15. [VMware RabbitMQ for Kubernetes — Memory Alarms Docs](https://docs.vmware.com/en/VMware-RabbitMQ-for-Kubernetes/1/rmq/memory.html)
16. [RabbitMQ Clustering Guide — Official Docs](https://www.rabbitmq.com/docs/clustering)
17. [NATS JetStream Clustering Docs — docs.nats.io](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering)
18. [NATS JetStream Concepts — docs.nats.io](https://docs.nats.io/nats-concepts/jetstream)
19. [NATS JetStream vs. RabbitMQ vs. Kafka Benchmarks 2025 — onidel.com](https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks)
20. [NATS vs. Apache Kafka Compared — Synadia](https://www.synadia.com/blog/nats-and-kafka-compared)
21. [Confluent Cloud vs. AWS MSK vs. Self-Hosted Kafka — OneUptime (Jan 2026)](https://oneuptime.com/blog/post/2026-01-21-kafka-managed-comparison/view)
22. [Self-Hosted Kafka vs. Managed Kafka — AutoMQ Blog](https://www.automq.com/blog/self-hosted-kafka-vs-managed-kafka)
23. [Best Practices for Right-Sizing Apache Kafka Clusters — AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/)
24. [Kafka Capacity Planning — Conduktor](https://www.conduktor.io/glossary/kafka-capacity-planning)
25. [Kafka Sizing — jbcodeforce.github.io](https://jbcodeforce.github.io/kafka-studies/sizing/)
26. [Which Kafka Schema Registry Is Right for Your Architecture in 2025? — AutoMQ Blog](https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025)
27. [Schema Evolution and Compatibility — Confluent Docs](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html)
28. [Kafka Monitoring: Key Metrics and 5 Tools in 2025 — Instaclustr](https://www.instaclustr.com/education/apache-kafka/kafka-monitoring-key-metrics-and-5-tools-to-know-in-2025/)
29. [Top Kafka Monitoring Tools 2025 — CubeAPM](https://cubeapm.com/blog/top-kafka-monitoring-tools/)
30. [Kafka Consumer Lag Monitoring — Sematext](https://sematext.com/blog/kafka-consumer-lag-offsets-monitoring/)
31. [Kafka Dead Letter Queue Best Practices — Superstream](https://www.superstream.ai/blog/kafka-dead-letter-queue)
32. [Kafka DLQ Troubleshooting Guide — skey.uk](https://skey.uk/post/kafka-dead-letter-queue-troubleshooting-guide/)
33. [Kafka Dead Letter Queue — Confluent Learn](https://www.confluent.io/learn/kafka-dead-letter-queue/)
34. [Kafka Replication and Min In-Sync Replicas — lydtechconsulting.com](https://www.lydtechconsulting.com/blog/kafka-replication)
35. [ISR Management — Cloudera Docs](https://docs.cloudera.com/runtime/7.1.1/kafka-performance-tuning/topics/kafka-tune-broker-tuning-isr.html)
36. [Amazon MQ vs. RabbitMQ Benchmarking for 2025 — Coudo AI](https://www.coudo.ai/blog/amazon-mq-vs-rabbitmq-benchmarking-messaging-platforms-for-2025)
37. [Amazon MQ vs. RabbitMQ Comprehensive Guide — Coudo AI](https://www.coudo.ai/blog/amazon-mq-vs-rabbitmq-a-comprehensive-guide)
38. [NATS vs. RabbitMQ vs. NSQ vs. Kafka — Gcore](https://gcore.com/learning/nats-rabbitmq-nsq-kafka-comparison)
