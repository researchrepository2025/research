# F2: Event-Driven Architecture & Asynchronous Messaging

**Research File:** F02
**Scope:** Event-driven patterns and messaging infrastructure architecture
**Audience:** C-suite executives and technical leadership
**Date:** 2026-02-18

---

## Executive Summary

Event-driven architecture (EDA) is a design paradigm in which system components communicate by producing and consuming discrete, immutable records of state change called events, decoupling producers from consumers and enabling independent scalability. The four principal patterns — event sourcing, CQRS, publish-subscribe, and event streaming — each impose distinct infrastructure requirements: append-only event stores, schema registries, dead-letter queues, and message brokers capable of ordered, durable delivery. Achieving exactly-once delivery semantics is technically possible but requires transactional producer APIs, idempotent consumers, and careful coordination across the entire message path, adding latency and operational overhead. The leading platforms — Apache Kafka, RabbitMQ, NATS, and Apache Pulsar — differ substantially in throughput ceiling, deployment footprint, ordering guarantees, and replay capability, making platform choice an architectural commitment that is difficult to reverse. For ISVs evaluating deployment models, the operational profile of self-hosted event infrastructure is among the highest-complexity domains in distributed systems, while fully managed cloud alternatives substantially reduce that burden at the cost of vendor lock-in and data-egress economics.

---

## 1. Core Patterns

### 1.1 Event Sourcing

[FACT]
"Instead of storing just the current state of the data in a relational database, store the full series of actions taken on an object in an append-only store. The store acts as the system of record and can be used to materialize the domain objects."
— Microsoft Azure Architecture Center
URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Date: 2025-01-15 (updated 2025-12-09)

[FACT]
"Event sourcing is a complex pattern that permeates through the entire architecture and introduces trade-offs to achieve increased performance, scalability, and auditability. Once your system becomes an event sourcing system, all future design decisions are constrained by the fact that this is an event sourcing system. There is a high cost to migrate to or from an event sourcing system."
— Microsoft Azure Architecture Center
URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Date: 2025-01-15

[FACT]
"Treating events as the source of truth. Instead of only storing the current state in a database, every state change is recorded as an event in an immutable log."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

[FACT]
"Because it's relatively expensive to read and replay events, applications typically implement materialized views, read-only projections of the event store that are optimized for querying."
— Microsoft Azure Architecture Center
URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Date: 2025-01-15

[FACT]
"Event publication might be at least once, and so consumers of the events must be idempotent. They must not reapply the update described in an event if the event is handled more than once."
— Microsoft Azure Architecture Center
URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Date: 2025-01-15

**Snapshot optimization:** When event streams grow long, replaying all events to reconstruct current state becomes expensive. Microsoft's documentation notes that systems should "consider creating snapshots at specific intervals such as a specified number of events. The current state of the entity can be obtained from the snapshot and by replaying any events that occurred after that point in time." This snapshot pattern reduces state reconstruction cost but adds a secondary storage system to the operational profile.

### 1.2 CQRS (Command Query Responsibility Segregation)

[FACT]
"The write side handles commands that produce events, while the read side maintains separate models optimized for queries."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

[FACT]
"Event sourcing is commonly combined with the CQRS pattern by performing the data management tasks in response to the events, and by materializing views from the stored events."
— Microsoft Azure Architecture Center
URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Date: 2025-01-15

[FACT]
"When read and write databases are separated, the read data might not show the most recent changes immediately." Ensuring the read model stays up-to-date with the write model is a primary operational challenge of CQRS.
— Upsolver
URL: https://www.upsolver.com/blog/cqrs-event-sourcing-build-database-architecture
Date: [PRE-2025: 2023] — No 2025+ source found with equivalent technical specificity for this claim; Microsoft's 2025 Azure docs corroborate this characteristic indirectly.

[FACT]
"The event store serves as the write model and single source of truth, while the read model generates materialized views from these events in a highly denormalized form."
— Confluent Developer (Event Sourcing and CQRS course)
URL: https://developer.confluent.io/courses/event-sourcing/cqrs/
Date: [UNVERIFIED publication date — course content does not carry an explicit date; architectural claim is corroborated by Microsoft Azure docs dated 2025-01-15]

### 1.3 Publish-Subscribe

[FACT]
"Sophisticated message exchange patterns like publish-subscribe, event sourcing, and CQRS form the foundation of modern event-driven architectures."
— Microservices.io / Chris Richardson
URL: https://microservices.io/patterns/data/event-sourcing.html
Date: [UNVERIFIED — no explicit publication date; widely cited primary reference for microservices patterns]

[FACT]
The publish-subscribe model uses "one producer to many consumers" communication, enabling broader data accessibility, in contrast to message queuing which is "primarily point-to-point (one producer to one consumer)."
— AutoMQ Blog
URL: https://www.automq.com/blog/event-streaming-vs-message-queuing-differences-amp-comparison
Date: 2025

### 1.4 Event Streaming vs. Message Queuing

These two paradigms are frequently conflated but impose different infrastructure requirements and operational profiles.

| Characteristic | Message Queuing | Event Streaming |
|---|---|---|
| Persistence model | Messages removed after consumption | Events retained for a configurable period |
| Replay capability | Not available (queue-based) | Available — consumers can re-read from any offset |
| Communication model | Point-to-point | Publish-subscribe (one-to-many) |
| Throughput design | Moderate; optimized for reliability | High; designed for massive data volumes |
| Scaling model | Vertical and limited horizontal | Designed for horizontal scalability |
| Complexity | Generally straightforward | More features and configuration options |
| Canonical use cases | Task distribution, order processing, load leveling | Real-time analytics, event sourcing, IoT, high-volume data |

[SOURCE] AutoMQ Blog — Event Streaming vs. Message Queuing
URL: https://www.automq.com/blog/event-streaming-vs-message-queuing-differences-amp-comparison

[FACT]
"Event streaming tools are generally harder to learn and manage than message queues. But managed platforms like Confluent Cloud and Redpanda massively simplify the effort of handling event streams."
— AutoMQ Blog
URL: https://www.automq.com/blog/event-streaming-vs-message-queuing-differences-amp-comparison
Date: 2025

---

## 2. Infrastructure Requirements

### 2.1 Message Brokers

The message broker is the central infrastructure component in any event-driven system. It receives events from producers, durably stores them, and delivers them to one or more consumers. Selection of the broker is an architectural commitment — the broker's delivery semantics, ordering guarantees, and replay model constrain every downstream design decision.

### 2.2 Event Stores

[FACT]
"The event store is the permanent source of information, and so the event data should never be updated. The only way to update an entity or undo a change is to add a compensating event to the event store."
— Microsoft Azure Architecture Center
URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Date: 2025-01-15

[FACT]
"Events should be stored in infinite retention topics to make rebuilding the read side or creating new views from scratch possible."
— Confluent Developer (Event Sourcing course)
URL: https://developer.confluent.io/courses/event-sourcing/cqrs/
Date: [UNVERIFIED publication date — corroborated by Confluent Cloud's "Infinite Storage" feature announcement]

[FACT]
Confluent Cloud offers "Infinite Kafka Data Storage" as a product feature, enabling unlimited retention periods.
— Confluent Blog
URL: https://www.confluent.io/blog/infinite-kafka-data-storage-in-confluent-cloud/
Date: [PRE-2025 publication; feature remains current as of 2025]

### 2.3 Schema Registries

A schema registry enforces the contract between event producers and consumers. Without it, a producer-side schema change can silently break downstream consumers. Four major options exist in 2025:

| Registry | Deployment Model | Storage Backend | Key Operational Characteristic |
|---|---|---|---|
| Confluent Schema Registry | Standalone service | Kafka topic (durable, replicated) | Single-primary write architecture; separate deployment overhead |
| AWS Glue Schema Registry | Fully managed / serverless | AWS-native; encrypted at rest | No servers to manage; IAM-based auth; AWS-only |
| Redpanda Schema Registry | Integrated per broker | Internal compacted Kafka topic (Raft-replicated) | Eliminates separate cluster; any broker handles reads/writes |
| Apicurio Registry | Standalone; self-hosted | PostgreSQL, Kafka topic, or in-memory | Broadest format support (Avro, OpenAPI, AsyncAPI, GraphQL) |

[FACT]
Confluent Schema Registry is "a standalone service that runs separately from your Kafka brokers" using "a Kafka topic as a durable and replicated backend" with "single-primary architecture, where one node is elected as the primary to handle all write operations." Con: "requires its own deployment, management, and monitoring, which adds to the operational overhead."
— AutoMQ Blog
URL: https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025
Date: 2025

[FACT]
AWS Glue Schema Registry is "a fully managed, serverless component" with "no servers to manage, patch, or scale." Schemas are "stored durably within the AWS ecosystem, encrypted at rest, and accessed via HTTPS endpoints."
— AutoMQ Blog
URL: https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025
Date: 2025

[FACT]
Apicurio Registry is "a standalone registry with a highly pluggable storage architecture" that can be configured with "in-memory (for development), in a PostgreSQL database, or using a Kafka topic." Beyond Kafka schemas, it supports "OpenAPI, AsyncAPI, GraphQL, WSDL, and XML Schema."
— AutoMQ Blog
URL: https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025
Date: 2025

### 2.4 Dead-Letter Queues (DLQs)

[FACT]
"A Kafka Dead Letter Queue (DLQ) is a special type of Kafka topic where messages that fail to be processed by downstream consumers are routed. These messages might fail for a variety of reasons, such as schema validation errors, malformed data, or application logic failures. The DLQ ensures that failed messages do not block the processing pipeline, allowing the system to continue operating smoothly while giving operators a place to inspect and reprocess erroneous messages."
— Confluent (Learn: Kafka Dead Letter Queue)
URL: https://www.confluent.io/learn/kafka-dead-letter-queue/
Date: [UNVERIFIED publication date; Confluent primary documentation]

[FACT]
DLQ mitigation strategies in event-driven systems include: "Kafka holds messages until consumers catch up," "Consumers can apply throttling to avoid overload," and "Dead-letter queues (DLQs): Unprocessable events are moved aside, preventing them from blocking the stream."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

### 2.5 Transactional Outbox Pattern

The outbox pattern addresses a fundamental reliability gap: it is impossible to atomically write to a database and publish a message to a broker in a single operation without distributed transactions.

[FACT]
"The transactional outbox pattern resolves the dual write operations issue that occurs in distributed systems when a single operation involves both a database write operation and a message or event notification. The advantage of the transactional outbox pattern is it avoids the dual-write problem. The state, and the outbox table, will always be updated in a transactional fashion."
— AWS Prescriptive Guidance
URL: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
Date: [UNVERIFIED publication date; AWS official documentation]

[FACT]
"The Outbox Table is an additional database table used to temporarily store events that need to be published. This table resides in the same database as the service's core data and is written to in the same transaction. A relay process periodically polls the outbox table for unsent events and publishes them to the messaging system."
— nitrobox.com / Outbox Pattern article
URL: https://www.nitrobox.com/outbox-pattern-reliable-message-processing-in-event-driven-architecture/
Date: [UNVERIFIED publication date; technical claim corroborated by AWS Prescriptive Guidance above]

Infrastructure required for the transactional outbox: the primary relational database (the outbox table), a polling relay process (or CDC — Change Data Capture — connector such as Debezium), and the message broker. This adds two additional operational components to the deployment.

---

## 3. Reliability Guarantees

### 3.1 Delivery Semantics Overview

Three delivery guarantee levels exist in all major messaging platforms. Each has distinct infrastructure requirements and performance trade-offs.

| Delivery Guarantee | Definition | Infrastructure Requirement | Performance Impact |
|---|---|---|---|
| At-most-once | Message delivered 0 or 1 times; loss possible | None beyond basic broker | Lowest latency; highest throughput |
| At-least-once | Message delivered 1+ times; duplicates possible | Producer acks + consumer manual commits | Moderate overhead |
| Exactly-once | Message delivered exactly 1 time | Idempotent producers + transactional API + idempotent consumers | Highest latency; most complex |

[FACT]
"At-most-once risks data loss," "at-least-once risks duplicates," and "exactly-once adds cost and complexity."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

[FACT] — Kafka exactly-once:
"Messages are delivered once and only once. Messages are never lost or read twice even if some part fails." Achieved via "transactional delivery" introduced in Kafka version 0.11.0.0, with "higher latency, but the most durability." Requires configuration of `read_committed` isolation level on consumers.
— Confluent Documentation (Kafka Delivery Semantics)
URL: https://docs.confluent.io/kafka/design/delivery-semantics.html
Date: [UNVERIFIED publication date; official Confluent/Kafka documentation]

[FACT] — Kafka idempotent producer:
"The idempotent delivery option guarantees that resending a message will not result in duplicate entries in the log." Available since Kafka version 0.11.0.0. "The broker assigns each producer an ID and deduplicates messages using a sequence number sent by the producer with every message."
— Confluent Documentation
URL: https://docs.confluent.io/kafka/design/delivery-semantics.html
Date: [UNVERIFIED publication date; official documentation]

[FACT] — RabbitMQ:
"RabbitMQ provides at-least-once delivery guarantees with optional publisher confirms and consumer acknowledgments. In RabbitMQ, exactly-once delivery is not supported due to the combination of complex routing and the push-based delivery."
— NATS JetStream vs. RabbitMQ vs. Kafka benchmarks, Onidel
URL: https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks
Date: 2025

[FACT] — NATS delivery spectrum:
"At most once, at least once, and exactly once is available in JetStream."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats
Date: [UNVERIFIED specific publication date; official NATS documentation]

[FACT] — RabbitMQ replay:
RabbitMQ "supported queue-based semantics (vs log), so no message replay is available."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats

### 3.2 Ordering Guarantees

[FACT]
"Events with a specific key will always land in a specific partition in the order they are sent, and consumers will always read them from that specific partition in that exact order." Most message brokers (Kafka, AWS Kinesis, Azure Event Hubs) "guarantee ordering within a partition."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

[FACT]
"Total ordering guarantees that all events in the system occur in the same order on all nodes, while partial ordering only guarantees that some events are ordered with respect to each other. Total ordering is critical in systems where the order of events is critical, such as in financial transactions, where order of events determines account balance."
— Prompts.ai (Event Ordering in Distributed Systems)
URL: https://www.prompts.ai/en/blog/event-ordering-in-distributed-systems
Date: [UNVERIFIED publication date]

[FACT]
"Combining acks=all, producer idempotence, and keyed events results in a powerful end-to-end ordering guarantee."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

[FACT]
"Multi-threaded applications and multiple instances of applications might be storing events in the event store. Adding a timestamp to every event can help to avoid issues. Another common practice is to annotate each event resulting from a request with an incremental identifier."
— Microsoft Azure Architecture Center
URL: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
Date: 2025-01-15

**Practical implication for ISVs:** True global ordering (total order) across all partitions is not achievable in Kafka without collapsing to a single partition, eliminating parallelism. The standard practice is to scope ordering guarantees to a logical entity (e.g., all events for a given customer ID or order ID route to the same partition via partition key), accepting that inter-entity ordering is not guaranteed.

### 3.3 Idempotency Requirements

[FACT]
"The way exactly-once delivery is achieved in practice is by 'faking it' — either messages should be idempotent (can be applied multiple times without adverse effects) or deduplication is performed."
— Estuary.dev (What is Exactly-Once Delivery)
URL: https://estuary.dev/blog/exactly-once-delivery/
Date: [UNVERIFIED publication date; corroborated by Microsoft and Confluent primary sources]

[FACT]
"Making processing logic itself idempotent means even if the same message is handled twice, it won't cause a bad result — for example, setting values to specific states like 'paid' or using upserts in a database instead of inserts."
— Estuary.dev
URL: https://estuary.dev/blog/exactly-once-delivery/
Date: [UNVERIFIED publication date]

---

## 4. Operational Complexity

### 4.1 Partition Management

[FACT]
"As a guideline for optimal performance, you should not have more than 4,000 partitions per broker and not more than 200,000 partitions in a cluster."
— Confluent (How to Choose the Number of Topics/Partitions)
URL: https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster/
Date: [PRE-2025: no explicit date found; this guidance predates KRaft but remains cited as the ZooKeeper-era limit]

[FACT]
"KRaft can support the creation of Kafka clusters with more partitions than ZooKeeper — potentially 1 million or more partitions. Confluent conducted a lab experiment on a Kafka cluster running 2 million partitions, which is 10 times the maximum number of partitions for a cluster running ZooKeeper."
— Instaclustr Blog
URL: https://www.instaclustr.com/blog/apache-kafka-kraft-abandons-the-zookeeper-part-3-maximum-partitions-and-conclusions/
Date: [UNVERIFIED specific publication date; references Kafka 3.x KRaft capabilities]

[FACT]
"KRaft mode is production ready for new clusters as of Apache Kafka 3.3. For AWS MSK specifically, with the introduction of KRaft mode in Amazon MSK starting with version 3.7, Amazon MSK now enables the creation of clusters with up to 60 brokers vs. the default quota of 30 brokers in ZooKeeper mode."
— AWS Big Data Blog
URL: https://aws.amazon.com/blogs/big-data/introducing-support-for-apache-kafka-on-raft-mode-kraft-with-amazon-msk-clusters/
Date: [UNVERIFIED specific publication date; AWS official blog]

[FACT]
"Running Kafka clusters with large numbers of partitions is challenging. Increasing partitions with RF=3 [replication factor 3] results in higher background CPU load on the cluster, and eventually a reduction in cluster throughput, requiring much more cluster resources."
— AWS re:Post community answer
URL: https://repost.aws/questions/QUErK0_S3eRqKXBtL0kTjIRw/maximum-number-of-partitions-in-kraft-msk
Date: [UNVERIFIED specific publication date]

### 4.2 Consumer Group Coordination

[FACT]
"A group coordinator facilitates the equal distribution of partitions among consumer group members even when there are changes in group membership. The group coordinator is part of the Kafka broker."
— Redpanda Guides (Kafka Consumer Group)
URL: https://www.redpanda.com/guides/kafka-architecture-kafka-consumer-group
Date: [UNVERIFIED specific publication date]

[FACT]
"When a consumer joins or leaves a group, the group coordinator reassigns partitions among the remaining consumers using a rebalancing algorithm. The group coordinator monitors consumer status by receiving periodic signals from them called heartbeats. If a consumer fails to send a heartbeat within a specified timeout period, the group coordinator marks it as inactive and triggers a rebalance."
— Redpanda Guides
URL: https://www.redpanda.com/guides/kafka-architecture-kafka-consumer-group
Date: [UNVERIFIED specific publication date]

[FACT]
"The rule in Kafka is a maximum of 1 consumer per partition (as each partition must only be allocated to 1 consumer)."
— AWS Big Data Blog
URL: https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/
Date: Updated November 2025

### 4.3 Backpressure Handling

[FACT]
"Backpressure is a phenomenon that occurs when a system component — such as a Kafka consumer — cannot process incoming data as fast as it is being produced or delivered. If producers generate events faster than consumers can process them, the system risks collapse."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

[FACT]
Backpressure mitigation techniques include: "dynamically pausing the poll loop when RejectedExecutionException occurs, using heartbeat messages to maintain group membership, and resuming consumption when queue utilization drops below 90%."
— Hazal Keçoglu, Medium (Optimizing Kafka Consumer Performance: Commit Strategies and Backpressure Handling, November 2025)
URL: https://hazalkecoglu.medium.com/optimizing-kafka-consumer-performance-commit-strategies-and-backpressure-handling-0c3d38166d0a
Date: November 2025

### 4.4 Replay Capabilities

[FACT]
"If the system had infinite log retention, and every change was logged, the state of the system at every moment from when it started would be captured. Using this log, the system could be restored to any point in time by replaying the first N records in the log."
— Confluent (Infinite Storage blog)
URL: https://www.confluent.io/blog/infinite-kafka-data-storage-in-confluent-cloud/
Date: [PRE-2025 publication; feature remains current]

[FACT] — NATS replay model:
"Messages can be replayed by time, count, or sequence number, and durable subscriptions are supported."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats

[FACT] — Kafka replay model:
"Messages can be replayed by specifying an offset, and durable subscriptions are supported."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats

[FACT] — RabbitMQ:
RabbitMQ "supported queue-based semantics (vs log), so no message replay is available."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats

### 4.5 Debugging and Observability Overhead

[FACT]
"Troubleshooting a single business transaction may span dozens of events traversing multiple services."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

[FACT]
EDA observability requires "adoption of correlation IDs, distributed tracing frameworks (e.g. OpenTelemetry, Jaeger), and visualization tools to tie together logs, metrics, and traces."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

---

## 5. Scale Considerations

### 5.1 Throughput Limits by Platform

| Platform | Producer Throughput | Consumer Throughput | Latency Profile | Source |
|---|---|---|---|---|
| Apache Kafka | 500K–1M+ msgs/sec (with batching) | 500K–1M+ msgs/sec | 10–50ms (batching overhead) | [Onidel Benchmarks 2025](https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks) |
| Apache Pulsar | 1M msgs/sec | 2.6M msgs/sec | Sub-5ms | [StreamNative Comparison](https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream) |
| NATS JetStream | 200K–400K msgs/sec (with persistence) | 160K msgs/sec | Sub-ms to 1–5ms | [Onidel Benchmarks 2025](https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks) |
| RabbitMQ | 50K–100K msgs/sec | 48K msgs/sec | 5–20ms | [Onidel Benchmarks 2025](https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks) |

[FACT] — Pulsar topic scaling advantage:
Apache Pulsar "maintained 200K msgs/s for up to 20K topics" while "competitors handled only 500 topics" at equivalent throughput levels.
— StreamNative (Pulsar vs. RabbitMQ vs. NATS JetStream comparison)
URL: https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream
Date: [UNVERIFIED specific publication date]

[FACT] — Real-world scale examples:
"Shopify" processes "66 million messages per second" and "LinkedIn uses partitioning and sharding in Kafka to process trillions of events daily."
— Growin Engineering Blog
URL: https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/
Date: 2025

### 5.2 Kafka Partition Throughput Formula

[FACT]
"A single partition can typically handle 5–10 MB/s of throughput, depending on disk I/O and network conditions. In general, more partitions in a Kafka cluster leads to higher throughput, as the topic partition is the unit of parallelism in Kafka."
— AWS Big Data Blog
URL: https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/
Date: Updated November 2025

[FACT]
"If your target throughput is t, then you need to have at least max(t/p, t/c) partitions" where p = throughput per producer partition and c = throughput per consumer partition.
— Confluent Blog (How to Choose Partitions)
URL: https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster/
Date: [PRE-2025: no explicit recent date; standard sizing formula remains current]

### 5.3 Storage Requirements and Retention Policies

[FACT]
"Kafka retains messages for 7 days (168 hours)" by default. "log.retention.bytes=-1" indicates unlimited storage by default (no size-based limit unless configured).
— AutoMQ Blog (Kafka Retention Policy)
URL: https://www.automq.com/blog/kafka-retention-policy-concept-best-practices
Date: 2025

[FACT]
"Kafka can only delete closed (inactive) segments. The active segment remains untouched by cleanup processes, regardless of retention settings."
— AutoMQ Blog
URL: https://www.automq.com/blog/kafka-retention-policy-concept-best-practices
Date: 2025

[FACT]
"If the defined retention period for a topic is too short, important data could be removed before it is consumed, leading to data loss. But if it is set for too long, the ever-growing data volume poses local storage concerns which can crash a broker — and eventually the cluster."
— AutoMQ Blog
URL: https://www.automq.com/blog/kafka-retention-policy-concept-best-practices
Date: 2025

[FACT]
Best practice: "both time and size-based retention limits, monitor storage usage proactively, and consider scaling storage horizontally" to prevent rapid exhaustion of disk space in high-throughput environments.
— AutoMQ Blog
URL: https://www.automq.com/blog/kafka-retention-policy-concept-best-practices
Date: 2025

---

## 6. Platform Comparison: Capabilities and Architectural Role

### 6.1 Apache Kafka

[FACT]
"Apache Kafka is a distributed messaging platform designed for real-time data pipelines and streaming applications, designed for high-throughput and low-latency."
— Redpanda (Kafka Alternatives Guide)
URL: https://www.redpanda.com/guides/kafka-alternatives
Date: [UNVERIFIED specific publication date]

[FACT]
"Apache Kafka is a distributed streaming platform that offers four key APIs: the Producer API, Consumer API, Streams API, and Connector API."
— Instaclustr (Apache Kafka Architecture 2025)
URL: https://www.instaclustr.com/education/apache-kafka/apache-kafka-architecture-a-complete-guide-2025/
Date: Updated October 21, 2025

[FACT] — Deployment hardware requirements (self-hosted):
Kafka requires "eight cores, 64 GB to 128 GB of RAM, two or more 8-TB SAS/SSD disks, and a 10-Gig NIC" per broker for production workloads.
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats
Date: [UNVERIFIED specific publication date; hardware spec cited from Kafka documentation]

**Architectural role:** Log-based event streaming platform. Primary choice for high-throughput event sourcing, audit logs, stream processing (via Kafka Streams), and systems requiring long-term replay. De-facto standard for enterprise event-driven data pipelines.

### 6.2 RabbitMQ

[FACT]
"RabbitMQ is a traditional message broker, best suited for reliable delivery and message routing. It is mature and widely used, supports multiple protocols like AMQP, MQTT, STOMP, and offers advanced routing patterns via exchanges."
— Confluent (Kafka vs. Pulsar)
URL: https://www.confluent.io/kafka-vs-pulsar/
Date: [UNVERIFIED specific publication date]

[FACT]
"The core of RabbitMQ's architecture is the message exchange, which includes direct, topic, headers, and fanout exchanges."
— StreamNative (Pulsar vs. RabbitMQ vs. NATS JetStream)
URL: https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream
Date: [UNVERIFIED specific publication date]

[FACT]
RabbitMQ is a "good choice if you have simple applications where message durability, ordering, replay, and retention are not critical."
— StreamNative
URL: https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream

**Architectural role:** Traditional message broker for work queues, task distribution, and complex routing logic. Lacks event replay. Not suitable for event sourcing implementations that require history reconstruction.

### 6.3 NATS / NATS JetStream

[FACT]
"NATS is an open-source, lightweight, high-performance messaging system known for its simplicity, performance, and ease of use. It is built to be a simple, secure, and scalable solution for modern cloud-native and IoT applications."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats
Date: [UNVERIFIED specific publication date]

[FACT]
"NATS utilizes a single-server architecture, which makes it easy to deploy and manage, particularly in resource-constrained environments." NATS is deployable "from large instances in the cloud to resource constrained devices like a Raspberry Pi."
— StreamNative; NATS Official Documentation
URL: https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream; https://docs.nats.io/nats-concepts/overview/compare-nats

[FACT]
Core NATS provides "at-most-once" delivery; NATS JetStream (the persistence layer) adds "at-least-once and exactly-once" via consumer acknowledgment and deduplication based on message IDs.
— NATS Official Documentation; Onidel Benchmarks 2025
URL: https://docs.nats.io/nats-concepts/overview/compare-nats; https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks

**Architectural role:** Lightweight, low-latency pub-sub for microservices and IoT. JetStream layer adds persistence and delivery guarantees comparable to Kafka but at lower throughput ceilings. Best fit for smaller-scale deployments or edge/embedded environments.

### 6.4 Apache Pulsar

[FACT]
"Apache Pulsar combines high-performance streaming (which Apache Kafka pursues) and flexible traditional queuing (which RabbitMQ pursues) into a unified messaging model and API."
— HashStudioz Blog (Pulsar vs. Kafka vs. RabbitMQ)
URL: https://www.hashstudioz.com/blog/apache-pulsar-vs-kafka-vs-rabbitmq-choosing-the-right-messaging-system/
Date: [UNVERIFIED specific publication date]

[FACT]
"Pulsar separates computing and storage" via a Broker (compute layer) and Apache BookKeeper (storage layer). This "allows for lower latency by decoupling compute and storage."
— StreamNative; HashStudioz
URL: https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream

[FACT]
Pulsar supports "tiered storage including file, Amazon S3 or Google Cloud Storage (GCS)" and "can replay messages from a specific position."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats

[FACT]
Pulsar minimum production deployment requires "at least 6 Linux machines or VMs: 3 running ZooKeeper, 3 running a Pulsar broker and a BookKeeper bookie."
— NATS Official Documentation (Compare NATS)
URL: https://docs.nats.io/nats-concepts/overview/compare-nats

**Architectural role:** Unified streaming and queuing platform with tiered storage and multi-tenancy built-in. Architecturally suited for multi-cloud ISV deployments requiring both high throughput and flexible storage offload. Higher minimum deployment complexity than Kafka.

### 6.5 Summary Comparison Table

| Capability | Apache Kafka | RabbitMQ | NATS JetStream | Apache Pulsar |
|---|---|---|---|---|
| **Delivery guarantee** | At-most, at-least, exactly-once | At-most, at-least | At-most, at-least, exactly-once | At-most, at-least, exactly-once |
| **Message replay** | Yes (by offset) | No | Yes (by time/count/seq) | Yes (by position) |
| **Tiered / cloud storage** | Via Confluent / AutoMQ (not native OSS) | No | No | Yes (S3, GCS native) |
| **Max producer throughput** | 500K–1M+ msgs/sec | 50K–100K msgs/sec | 200K–400K msgs/sec | 1M msgs/sec |
| **Typical latency** | 10–50ms | 5–20ms | Sub-ms to 5ms | Sub-5ms |
| **Min. self-hosted deployment** | 3 brokers + ZooKeeper or KRaft nodes | Single node possible | Single NATS server | 6 VMs (3 ZK + 3 broker/bookie) |
| **Protocols supported** | Kafka native | AMQP, MQTT, STOMP | NATS, WebSocket | Kafka, AMQP, MQTT, WebSocket |
| **Exactly-once cross-system** | Yes (Kafka Streams / transactional API) | No | Partial (JetStream consumer acks) | Idempotent writes only |

[SOURCES] Onidel Benchmarks 2025 (https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks); NATS Documentation (https://docs.nats.io/nats-concepts/overview/compare-nats); StreamNative (https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream)

---

## 7. Deployment Model Difficulty Ratings

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Message broker operation** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Self-hosted Kafka/Pulsar cluster; hardware provisioning; capacity planning; broker upgrades | Operator-managed (Strimzi, Pulsar Helm); K8s storage class tuning; rebalancing | MSK, Confluent Cloud, Google Pub/Sub, Azure Event Hubs; provider manages brokers |
| | Kafka, Pulsar, RabbitMQ self-hosted | Strimzi Operator, Pulsar Helm Chart, RabbitMQ Operator | AWS MSK, Confluent Cloud, Azure Event Hubs |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 |
| **Schema registry** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Confluent or Apicurio; separate HA deployment; PostgreSQL or Kafka backend | Containerized Confluent/Apicurio; K8s-managed persistence | AWS Glue Schema Registry (serverless); Confluent Cloud (managed) |
| | Confluent OSS, Apicurio | Confluent/Apicurio in K8s | AWS Glue, Confluent Cloud |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.05 |
| **Event store / retention mgmt** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Manual disk provisioning; retention tuning to prevent broker crashes; log compaction management | StorageClass-backed PVCs; manual retention policy management; node disk pressure monitoring | Provider-managed; tiered storage (S3) offload; pay-per-GB model |
| | Direct disk management, Kafka log configuration | Kubernetes PVC, node storage monitoring | Confluent Cloud tiered storage, S3-backed Pulsar |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |
| **Dead-letter queue management** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | DLQ topics must be manually configured and monitored; reprocessing pipelines self-built | Same as on-premises for DLQ logic; K8s deployment of processing tooling | Managed DLQ routing in event-hub services; some providers offer built-in reprocessing |
| | Kafka DLQ topics, custom relay services | K8s-deployed DLQ processors | AWS SQS DLQ, Azure Event Hubs capture, Confluent Cloud |
| | Est. FTE: 0.1–0.25 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |

**FTE Assumptions:** Estimates assume a mid-size ISV deployment serving 30–50 enterprise customers with moderate event throughput (50K–500K msgs/sec peak). On-call burden (evenings/weekends) adds approximately 0.1–0.2 FTE equivalent on top of active work estimates for all models except Cloud-Native at the low end.

---

## Key Takeaways

- **Event-driven architecture is an architectural commitment, not a feature.** Microsoft's Azure Architecture Center explicitly warns that "once your system becomes an event sourcing system, all future design decisions are constrained" and that "there is a high cost to migrate to or from" it. ISVs should adopt EDA incrementally, starting with pub-sub patterns before committing to event sourcing.

- **Exactly-once delivery requires infrastructure beyond the broker.** Achieving it demands idempotent producers (Kafka 0.11+), transactional APIs, `read_committed` consumer isolation, and idempotent business logic — each adding latency and operational surface area. Most production systems accept at-least-once delivery and implement idempotent consumers instead.

- **Partition key design determines ordering scope.** No major platform provides global total ordering at scale. Ordering is scoped to a partition; partition key design (e.g., customer ID, order ID) determines which events are ordered relative to each other. This is a domain modeling decision, not an infrastructure one.

- **Platform selection creates a hard throughput and replay ceiling.** RabbitMQ's queue-based model eliminates replay capability entirely, making it unsuitable for event sourcing. Kafka and Pulsar are the dominant choices for systems requiring event replay; NATS JetStream is viable for lower-throughput deployments prioritizing operational simplicity and low latency.

- **Self-hosted event infrastructure is among the highest-complexity operational domains.** A self-hosted Kafka cluster (hardware provisioning, partition management, consumer group rebalancing, retention tuning, schema registry operation) requires 1.0–2.0 FTE of dedicated expertise. Managed services (MSK, Confluent Cloud, Pub/Sub) reduce this to 0.1–0.25 FTE but introduce vendor dependency and data-egress cost considerations.

---

## Related — Out of Scope

- **F44 (Message Broker Operational Management):** The day-to-day operational tasks for running Kafka, RabbitMQ, Pulsar, and NATS in production — including upgrade procedures, monitoring configuration, broker failure recovery, and capacity planning — are covered in F44. This file covers architectural capabilities only.
- **F1 (Microservices Decomposition):** Service boundary design and domain decomposition strategy that determines where event-driven patterns are applied.
- **F39 (Compute and Deployment):** Container orchestration and compute infrastructure on which message brokers run.
- **F50 (Monitoring and Observability):** Specific tooling and configurations for observing event-driven systems (Prometheus, Grafana, OpenTelemetry).

---

## Sources

| # | Source | URL | Tier |
|---|---|---|---|
| 1 | Microsoft Azure Architecture Center — Event Sourcing Pattern | https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing | T1 |
| 2 | Microsoft Azure Architecture Center — CQRS Pattern | https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs | T1 |
| 3 | Confluent Documentation — Kafka Delivery Semantics | https://docs.confluent.io/kafka/design/delivery-semantics.html | T1 |
| 4 | NATS Official Documentation — Compare NATS | https://docs.nats.io/nats-concepts/overview/compare-nats | T1 |
| 5 | AWS Big Data Blog — Kafka Cluster Sizing Best Practices | https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/ | T1 |
| 6 | AWS Prescriptive Guidance — Transactional Outbox Pattern | https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html | T1 |
| 7 | AWS Big Data Blog — KRaft Mode on Amazon MSK | https://aws.amazon.com/blogs/big-data/introducing-support-for-apache-kafka-on-raft-mode-kraft-with-amazon-msk-clusters/ | T1 |
| 8 | Confluent Blog — Kafka Retention | https://www.confluent.io/learn/kafka-retention/ | T1 |
| 9 | Confluent Blog — Infinite Kafka Data Storage | https://www.confluent.io/blog/infinite-kafka-data-storage-in-confluent-cloud/ | T1 |
| 10 | Confluent Blog — How to Choose Partitions | https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster/ | T1 |
| 11 | Confluent Developer — Event Sourcing and CQRS | https://developer.confluent.io/courses/event-sourcing/cqrs/ | T1 |
| 12 | Confluent Learn — Kafka Dead Letter Queue | https://www.confluent.io/learn/kafka-dead-letter-queue/ | T1 |
| 13 | Growin Engineering Blog — EDA Done Right 2025 | https://www.growin.com/blog/event-driven-architecture-scale-systems-2025/ | T2 |
| 14 | Instaclustr — Kafka KRaft Maximum Partitions | https://www.instaclustr.com/blog/apache-kafka-kraft-abandons-the-zookeeper-part-3-maximum-partitions-and-conclusions/ | T2 |
| 15 | Instaclustr — Kafka Architecture Complete Guide 2025 | https://www.instaclustr.com/education/apache-kafka/apache-kafka-architecture-a-complete-guide-2025/ | T2 |
| 16 | StreamNative — Pulsar vs. RabbitMQ vs. NATS JetStream | https://streamnative.io/blog/comparison-of-messaging-platforms-apache-pulsar-vs-rabbitmq-vs-nats-jetstream | T2 |
| 17 | AutoMQ Blog — Kafka Schema Registry Comparison 2025 | https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025 | T2 |
| 18 | AutoMQ Blog — Kafka Retention Policy | https://www.automq.com/blog/kafka-retention-policy-concept-best-practices | T2 |
| 19 | AutoMQ Blog — Event Streaming vs. Message Queuing | https://www.automq.com/blog/event-streaming-vs-message-queuing-differences-amp-comparison | T2 |
| 20 | Onidel — NATS JetStream vs. RabbitMQ vs. Kafka Benchmarks 2025 | https://onidel.com/blog/nats-jetstream-rabbitmq-kafka-2025-benchmarks | T2 |
| 21 | Redpanda — Kafka Consumer Group Guide | https://www.redpanda.com/guides/kafka-architecture-kafka-consumer-group | T2 |
| 22 | Hazal Keçoglu — Kafka Consumer Backpressure (Medium, Nov 2025) | https://hazalkecoglu.medium.com/optimizing-kafka-consumer-performance-commit-strategies-and-backpressure-handling-0c3d38166d0a | T2 |
| 23 | Estuary.dev — What is Exactly-Once Delivery | https://estuary.dev/blog/exactly-once-delivery/ | T2 |
| 24 | nitrobox.com — Outbox Pattern | https://www.nitrobox.com/outbox-pattern-reliable-message-processing-in-event-driven-architecture/ | T2 |
| 25 | Microservices.io — Event Sourcing Pattern | https://microservices.io/patterns/data/event-sourcing.html | T2 |
| 26 | HashStudioz — Pulsar vs. Kafka vs. RabbitMQ | https://www.hashstudioz.com/blog/apache-pulsar-vs-kafka-vs-rabbitmq-choosing-the-right-messaging-system/ | T2 |
| 27 | AWS re:Post — KRaft MSK Partition Limits | https://repost.aws/questions/QUErK0_S3eRqKXBtL0kTjIRw/maximum-number-of-partitions-in-kraft-msk | T3 |
