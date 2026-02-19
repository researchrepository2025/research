# F33: On-Premises Event-Driven Architecture Implementation

## Executive Summary

Implementing event-driven architecture (EDA) patterns — event sourcing, CQRS, and sagas — on 100% on-premises infrastructure imposes a compounding operational burden that extends far beyond message broker management. Where cloud-native platforms abstract event stores, workflow orchestration, schema governance, and correlation tooling into managed services, on-premises teams must build and operate every one of these layers themselves. The result is a pattern of hidden complexity: each individual component (event store, schema registry, saga orchestrator, dead letter queue management, distributed tracer) is individually manageable, but operating them cohesively at production scale requires sustained, specialized staffing that most ISVs underestimate. [MIT Technology Review notes](https://www.technologyreview.com/2025/10/06/1124323/enabling-real-time-responsiveness-with-event-driven-architecture/) that EDA is becoming strategically essential for real-time responsiveness — but it simultaneously identifies that the operational gap between on-premises and cloud implementations is widening as managed services mature. ISVs deploying to customer on-premises environments must plan for the full operational profile described below, or risk systemic reliability issues that cloud-native alternatives would have automated away.

---

## 1. Event Store Implementation

### The Core Choice: Purpose-Built vs. Kafka-as-Store vs. Custom

On-premises event sourcing requires a durable, append-only event store. Three primary architectural choices exist, each with distinct operational characteristics.

#### Option A: EventStoreDB (now Kurrent)

[EventStoreDB](https://eventstore.com/eventstoredb) is a purpose-built event database designed from the ground up for event sourcing. Key production characteristics:

[FACT] EventStoreDB uses a quorum-based replication model with one leader node and multiple follower nodes. [Source: EventStoreDB Clustering Documentation](https://developers.eventstore.com/server/v23.10/cluster)

[FACT] "To tolerate the failure of n nodes, the cluster must be of size (2n + 1). A three node cluster can continue to accept writes if one node is unavailable." — [EventStoreDB Clustering Documentation](https://developers.eventstore.com/server/v23.10/cluster)

[FACT] EventStoreDB supports three node types: Leader (writes and reads), Follower (replication), and ReadOnly (reads only). [Source: EventStoreDB Clustering Documentation](https://developers.eventstore.com/server/v23.10/cluster)

[FACT] "EventStoreDB expects the time on cluster nodes to be in sync within a given tolerance, and if nodes have their clock out of sync exceeding this setting, the gossip is rejected and the node will not be accepted as a cluster member. The default is 60000 milliseconds (one minute)." — [EventStoreDB Clustering Documentation](https://developers.eventstore.com/server/v23.10/cluster)

[FACT] EventStoreDB is written in C# and JavaScript and runs on Windows, Linux, and macOS using .NET Core runtime. [Source: GitHub - kurrent-io/EventStore](https://github.com/EventStore/EventStore)

[FACT] "Writes support an optimistic concurrency check on the version of the stream to which events are written." — [EventStoreDB Clustering Documentation](https://developers.eventstore.com/server/v23.10/cluster)

**Kubernetes deployment constraint:**

[FACT] "A catch-up subscription listener must be extracted into a separate microservice and run in a single replica, and this microservice must not be updated using RollingUpdate Deployment strategy but rather the Recreate Deployment strategy must be used instead when all existing Pods are killed before new ones are created." — [Building Event Sourcing with EventStore and .NET: From Theory to Production](https://developersvoice.com/blog/dotnet/building-event-sourcing-with-eventstore-and-dotnet/)

#### Option B: Kafka as Event Store (with Limitations)

[FACT] "Kafka alone is not an event store, but Kafka and ksqlDB together allow building full-featured event stores." — [GitHub: ksqldb-event-sourcing by eugene-khyst](https://github.com/eugene-khyst/ksqldb-event-souring)

[FACT] Kafka log compaction "does not guarantee there is only one record with the same key at any one time, as there may be multiple records with the same key because compaction timing is non-deterministic." — [Confluent: Key-Based Retention Using Topic Compaction](https://developer.confluent.io/courses/architecture/compaction/)

[FACT] "Compaction, on purpose, removes historical data from an event stream by removing superseded events. This is problematic for use cases like financial transactions, where every single transaction needs to be recorded and stored." — [Kafka Retention Explained: Time, Size & Compaction Rules](https://unanswered.io/guide/kafka-data-retention-explained)

[FACT] "With infinite message retention, all changes to a user's address are maintained in the logs, which can lead to the log growing in size without a bound and involves the risk of outgrowing disk capacity." — [Confluent: Apache Kafka Retention Explained](https://www.confluent.io/learn/kafka-retention/)

[FACT] "Applications reading from compacted topics are not guaranteed to see every value for a given key, as some values may be deleted due to new values being appended before the application sees them." — [Confluent: Kafka Log Compaction](https://docs.confluent.io/kafka/design/log_compaction.html)

**Critical implication for ISVs:** Using Kafka as the sole event store requires additional snapshot infrastructure and custom tooling to compensate for compaction non-determinism. This is engineering work that a managed event sourcing platform (e.g., Azure Event Grid, AWS EventBridge with sourcing patterns) abstracts away.

#### Option C: Axon Server (Framework-Coupled)

[FACT] "Axon Framework is the most widely adopted open-source Java toolkit for building event-driven systems using CQRS and event sourcing with over 70M downloads." — [AxonIQ: Axon Framework](https://www.axoniq.io/framework)

[FACT] "Axon Server provides a distributed command bus, event bus, query bus, and an efficient event store implementation for scalable event sourcing." — [InfoQ: Running Axon Server - CQRS and Event Sourcing in Java](https://www.infoq.com/articles/axon-server-cqrs-event-sourcing-java/)

[FACT] "Services can reliably be deployed on-prem or remotely. Axon Server is an all-in-one solution for CQRS and ES applications written in Java for the Axon Framework." — [AxonIQ](https://www.axoniq.io/)

[FACT] "Axon Server Enterprise Edition adds the ability to run a cluster, but individual nodes can have pretty specific identities with large differences in the provided services." — [CQRS and Event Sourcing with Axon Framework](https://www.intre.it/en/2025/04/14/microservices-cqrs-event-sourcing-axon-framework/)

**Constraint:** Axon Server is tightly coupled to the JVM ecosystem. Non-JVM service meshes require Kafka or EventStoreDB instead.

### Event Store Comparison

| Capability | EventStoreDB | Kafka + ksqlDB | Axon Server |
|---|---|---|---|
| Purpose-built for ES | Yes | No — requires ksqlDB supplement | Yes (JVM only) |
| Infinite retention | Native | Requires explicit config + storage management | Native |
| On-prem cluster HA | 3-node quorum | ZooKeeper/KRaft quorum | Enterprise Edition only |
| Language agnosticism | gRPC (multi-language) | All Kafka clients | JVM primary |
| Compaction risk | None (immutable) | High — must disable compaction on ES topics | None |
| Est. FTE (ops) | 0.25–0.5 FTE | 0.5–1.0 FTE (Kafka + ksqlDB combined) | 0.25–0.5 FTE |

*FTE assumptions: mid-size ISV deployment serving 50 enterprise customers; excludes on-call burden.*

---

## 2. Saga Orchestration: Distributed Transactions Without Managed Engines

### The Problem Space

On-premises environments lack access to managed saga/workflow engines (AWS Step Functions, Azure Durable Functions, Google Cloud Workflows). ISVs must self-host an orchestration engine to coordinate distributed transactions across services with compensating transaction support.

[FACT] "In orchestration, a centralized controller, or orchestrator, handles all the transactions and tells the participants which operation to perform based on events, with the orchestrator performing saga requests, storing and interpreting the states of each task, and handling failure recovery by using compensating transactions." — [AWS Prescriptive Guidance: Saga Orchestration Pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-orchestration.html)

### Self-Hosted Saga Engine Options

#### Temporal

[FACT] Temporal self-hosted production infrastructure requires: Frontend Service (1.5–2 CPU cores, 4 GiB memory), History Service (4 CPU cores, 6+ GiB memory), Matching Service (1 CPU core, 2 GiB memory), and Worker Service (0.5–1 CPU cores, 1 GiB memory). — [Medium: Scaling Temporal with Postgres, Cassandra, and Elasticsearch](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b)

[FACT] "The persistence backend (such as Cassandra, MySQL, or PostgreSQL) is frequently the bottleneck in a Temporal cluster due to its critical role in durability and state management. Monitoring its CPU utilization and keeping it below 80% is important." — [Medium: Scaling Temporal](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b)

[FACT] "Even with small event bursts of around 100 RPS, the load on the PostgreSQL instance spiked beyond 120, leading to failures and shard issues whenever traffic increased, making this setup unsuitable for production. Temporal's official documentation states that PostgreSQL is not ideal for medium-to-large-scale systems." — [Medium: Scaling Temporal](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b)

[FACT] Recommended database strategy: "separating persistence and visibility by using Cassandra for persistence and Elasticsearch for visibility, as this final setup provided the best throughput and scalability." — [Medium: Scaling Temporal](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b)

[FACT] "Self-hosted Temporal infrastructure can become a bottleneck, with chronic reliability issues, availability gaps, and mounting engineering overhead consuming resources that should have been building products. Engineering teams own the entire operational stack, and monitoring cluster health, applying version upgrades, executing database migrations, and troubleshooting performance degradation require specialized expertise and continuous attention." — [Akka: The 10 Best Temporal Alternatives for Enterprise Teams](https://akka.io/blog/temporal-alternatives)

[FACT] "The learning curve for Temporal is significant—expect a month before your team is productive." — [blog.taigrr.com: Temporal Server: Self-hosting a Production-Ready Instance](https://blog.taigrr.com/blog/setting-up-a-production-ready-temporal-server/)

[FACT] "There is significant effort required to deploy and manage multiple horizontal Temporal servers, between certificate rotation and configuration management, especially as Temporal often changes configuration requirements." — [Medium: My Journey Self Hosting a Temporal Cluster](https://medium.com/@mailman966/my-journey-hosting-a-temporal-cluster-237fec22a5ec)

#### Conductor (Netflix OSS)

[FACT] "Conductor supports both synchronous and asynchronous tasks and is open-source and self-hosted, offering flexibility without a commercial license cost. It is best suited for engineering-heavy organizations building resilient microservices architectures that need event-driven orchestration with fine-grained lifecycle control." — [Akka: The 10 Best Temporal Alternatives for Enterprise Teams](https://akka.io/blog/temporal-alternatives)

#### Eventuate Tram Saga

[FACT] "Available frameworks include Eventuate Tram Saga (a saga orchestration framework for Spring Boot and Micronaut-based microservices) and Seata (an open-source distributed transaction framework)." — [Orkes: Saga Pattern in Distributed Systems](https://orkes.io/blog/saga-pattern-in-distributed-systems/)

### Saga Orchestration Operational Profile

| Capability | On-Premises (Temporal) | On-Premises (Conductor) | Cloud-Native (Step Functions) |
|---|---|---|---|
| Difficulty | 5/5 | 4/5 | 1/5 |
| Key requirements | Cassandra + Elasticsearch + 4 Temporal service pods | PostgreSQL + Conductor server | AWS account only |
| Infrastructure | Kubernetes cluster + 3+ databases | Kubernetes + 1 database | Serverless — zero infra |
| Est. FTE | 0.5–1.0 FTE active + 0.25 on-call | 0.25–0.5 FTE active + 0.25 on-call | 0.0–0.1 FTE |

*FTE assumptions: mid-size ISV deployment, 50 enterprise customers, production SLA required. On-call is 24x7 coverage prorated.*

---

## 3. Schema Registry Operations

### Why Schema Registries Are Non-Negotiable

In event-driven systems, producers and consumers are decoupled — they do not share a compile-time contract. Schema registries enforce compatibility guarantees at runtime, preventing schema changes from silently breaking downstream consumers.

[FACT] "Few organizations provide software engineering teams with guidance on which event brokers to use, how to design EDA, or how to manage the life cycle of events, topics and schemas. This lack of guidance creates issues with integration, governance and operations over time." — [Gartner: Choosing Event Brokers](https://www.gartner.com/en/documents/3986571)

### Confluent Schema Registry

[FACT] Confluent Schema Registry supports schema versioning, "ensuring that different versions of the schema can be used simultaneously without causing compatibility issues." — [Confluent Schema Registry Documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)

[FACT] "For on-premises or multi-cloud deployments, Confluent Schema Registry or Apicurio are the primary options." — [AutoMQ: Which Kafka Schema Registry is Right for Your Architecture in 2025?](https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025)

### Apicurio Registry

[FACT] "Apicurio is a standalone registry with a highly pluggable storage architecture that can be configured to store schemas in-memory (for development), in a PostgreSQL database, or using a Kafka topic with its 'KafkaSQL' storage option." — [Apicurio Registry: Introduction](https://www.apicur.io/registry/docs/apicurio-registry/1.3.3.Final/getting-started/assembly-intro-to-the-registry.html)

[FACT] "Apicurio Registry allows you to configure optional rules to govern the evolution of your registry content, including rules to ensure that uploaded content is syntactically and semantically valid, or is backwards and forwards compatible with other versions, with configured rules that must pass before new versions can be uploaded." — [Apicurio Registry: Introduction](https://www.apicur.io/registry/docs/apicurio-registry/1.3.3.Final/getting-started/assembly-intro-to-the-registry.html)

[FACT] "The Apicurio Registry REST API is compatible with the Confluent schema registry REST API, which includes support for Apache Avro, Google Protocol buffers, and JSON Schema artifact types, with applications using Confluent client libraries able to use Apicurio Registry as a drop-in replacement." — [Apicurio: Managing Registry Content Using the REST API](https://www.apicur.io/registry/docs/apicurio-registry/1.3.3.Final/getting-started/assembly-managing-registry-artifacts-api.html)

[FACT] "The Confluent Export Tool is a utility designed to extract all content from a Confluent Schema Registry instance and save it into a format that is compatible with Apicurio Registry." — [Apicurio Blog: Exporting from Confluent Schema Registry to Apicurio Registry, March 2025](https://www.apicur.io/blog/2025/03/20/export-from-confluent)

### Schema Registry Operational Profile

| Capability | On-Prem (Confluent SR) | On-Prem (Apicurio) | Cloud-Native (AWS Glue SR) |
|---|---|---|---|
| Difficulty | 3/5 | 3/5 | 1/5 |
| Storage backend | Kafka topic (internal) | PostgreSQL or KafkaSQL | Fully managed |
| HA configuration | Active-passive pairs | Active-passive, Kubernetes native | Built-in |
| Compatibility modes | BACKWARD, FORWARD, FULL | BACKWARD, FORWARD, FULL | BACKWARD, FORWARD, FULL |
| Migration path | — | Can ingest Confluent SR exports | — |
| Est. FTE | 0.1–0.2 FTE | 0.1–0.2 FTE | 0.0 FTE |

---

## 4. Event Replay and Reprocessing

### Why Replay Is an Operational Capability, Not Just a Feature

Event replay — the ability to reprocess the entire event log to rebuild read models, repair corrupted projections, or migrate to new schema versions — is one of the core value propositions of event sourcing. On-premises, the infrastructure to support replay must be explicitly engineered and maintained.

[FACT] "You should be able to replay your event log to rebuild read models or migrate event formats. You can reset your read-model database, then consume events from Kafka from the earliest offset or from snapshots forward, reprocessing all projection logic to rebuild views." — [LKTechAcademy: Mastering Event Sourcing and CQRS with Apache Kafka and .NET Core, 2025](https://www.lktechacademy.com/2025/10/mastering-event-sourcing-cqrs-kafka-dotnet.html)

[FACT] Two primary replay strategies: "(1) The simplest rebuild we can do is truncate the current state of the read model and then reapply all events through projection logic if we can afford the downtime. (2) Alternatively, if we cannot afford downtime, we can do a blue-green rebuild by setting up a read model in other storage, then reapplying events to this secondary read model, and once we're caught up, switching queries to target the new read model." — [Kurrent: Live Projections for Read Models with Event Sourcing and CQRS](https://www.kurrent.io/blog/live-projections-for-read-models-with-event-sourcing-and-cqrs)

[FACT] "Event sourcing relies on Kafka's ability to preserve the complete history of domain events, enabling system reconstruction from any point in time, and Kafka retention policies directly impact the replayability window for event-driven applications." — [Confluent: Apache Kafka Retention Explained](https://www.confluent.io/learn/kafka-retention/)

[FACT] "Several upcasters can be chained into an upcaster chain which is used during event replaying, and the event replay mechanism takes events, runs them through corresponding upcaster chains and hands them over to the event handlers." — [Kurrent: Live Projections for Read Models](https://www.kurrent.io/blog/live-projections-for-read-models-with-event-sourcing-and-cqrs)

### On-Premises Replay Infrastructure Requirements

Replay at scale requires:

1. **Infinite or near-infinite topic retention** — Kafka topics used as event stores must be configured with `retention.ms=-1` (infinite) or explicitly sized retention windows. This creates unbounded storage growth on on-premises hardware where storage expansion is a procurement process, not an API call.

2. **Snapshot storage** — [FACT] "As the system evolves, to prevent the event stream from growing indefinitely, some form of compaction or storing 'current state' snapshots might come in handy." — [Cloudurable: Kafka Architecture: Log Compaction - 2025 Edition](https://cloudurable.com/blog/kafka-architecture-log-compaction-2025/)

3. **Consumer group isolation** — Replay consumers must use dedicated consumer groups that do not share offsets with production consumers.

4. **Read model secondary storage** — Blue-green replay requires a secondary database provisioned in advance. On-premises, this means pre-provisioned standby hardware.

### Replay Operational Profile

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| Difficulty | 4/5 | 3/5 | 2/5 |
| Key requirements | Infinite retention disk, snapshot store, isolated consumer groups, secondary DB | Same as on-prem but elastic storage | Managed retention, serverless replay triggers |
| Representative tools | Kafka (infinite retention), PostgreSQL/Redis (read models), custom replay scripts | Kafka on K8s, PVCs for retention | EventBridge Replay, DynamoDB Streams |
| Est. FTE | 0.25–0.5 FTE (design + periodic execution) | 0.25 FTE | 0.0–0.1 FTE |

---

## 5. Dead Letter Queue Management

### The DLQ Gap in On-Premises Kafka

Kafka does not natively implement dead letter queues. DLQ behavior must be engineered into consumer application logic and supported by operational tooling.

[FACT] "While Kafka doesn't natively have DLQ support, organizations often implement DLQ as part of their consumer application logic, with Kafka's consumer offset management and retries typically extended to accommodate DLQs." — [Confluent: Apache Kafka Dead Letter Queue](https://www.confluent.io/learn/kafka-dead-letter-queue/)

[FACT] "Configuring a Kafka Dead Letter Queue generally involves creating a separate Kafka topic to store failed messages and implementing error handling in your consumer application to catch message processing failures." — [Confluent: Apache Kafka Dead Letter Queue](https://www.confluent.io/learn/kafka-dead-letter-queue/)

[FACT] "Configure retry logic with exponential backoff and maximum attempt limits to prevent retry loops that can overwhelm brokers while giving transient failures a fair chance to succeed." — [Superstream: Kafka Dead Letter Queue Best Practices](https://www.superstream.ai/blog/kafka-dead-letter-queue)

[FACT] "Track message volume, age, and error type distribution — a sudden spike in DLQ size or concentration of specific error codes often indicates systemic issues upstream." — [Superstream: Kafka Dead Letter Queue Best Practices](https://www.superstream.ai/blog/kafka-dead-letter-queue)

[FACT] "Always implement retry logic with a defined limit before sending messages to the DLQ, which prevents infinite loops and ensures that only irrecoverable messages end up in the DLQ." — [Superstream: Kafka Dead Letter Queue Best Practices](https://www.superstream.ai/blog/kafka-dead-letter-queue)

### Uber's Production DLQ Architecture (Reference Implementation)

[FACT] Uber's published architecture implements a tiered retry-then-DLQ pattern using dedicated retry topics with exponential delay intervals before final DLQ routing. — [Uber Blog: Building Reliable Reprocessing and Dead Letter Queues with Kafka](https://www.uber.com/blog/reliable-reprocessing/)

### DLQ Operational Requirements

On-premises DLQ operations require human intervention workflows that cloud-native services partially automate:

- Manual inspection tooling (Kafka consumer CLI, Kafka UI/AKHQ/Conduktor)
- Replay pipeline to re-inject corrected messages from DLQ topics back to source topics
- Alerting on DLQ depth (Prometheus + Alertmanager)
- Runbooks for each error classification type

| Capability | On-Prem (Kafka) | Managed K8s (Kafka) | Cloud-Native (SQS DLQ) |
|---|---|---|---|
| Difficulty | 4/5 | 3/5 | 1/5 |
| Native DLQ support | No — application-layer only | No — application-layer only | Yes — native |
| Retry logic | Custom consumer code | Custom consumer code | Configurable via console |
| Manual intervention UI | AKHQ, Conduktor, custom | Same | AWS Console / CloudWatch |
| Est. FTE | 0.2–0.4 FTE (build + operate) | 0.2–0.3 FTE | 0.0–0.1 FTE |

---

## 6. Event Ordering Guarantees

### Exactly-Once Semantics and Partition Ordering

[FACT] "The two hardest problems in distributed systems are guaranteeing message order and achieving exactly-once delivery." — [Hevo Data: What is Kafka Exactly Once Semantics?](https://hevodata.com/blog/kafka-exactly-once-semantics/)

[FACT] "Starting with version 0.11.0.0, producers can utilize transactional delivery, requesting acknowledgment that messages were received and successfully replicated, and if resending a message, it resends with idempotency. Producers can write to multiple partitions atomically so that either all writes succeed or all writes fail." — [Confluent: Message Delivery Guarantees for Apache Kafka](https://docs.confluent.io/kafka/design/delivery-semantics.html)

[FACT] "Exactly-once semantics is a poorly understood semantic that requires cooperation between the messaging system itself and the application producing and consuming the messages. Ensuring exactly-once semantics only at the producer side is very tricky because Kafka and the application database are two separate transactional systems, and coordinating them under a single atomic operation is complex." — [Baeldung: Exactly Once Processing in Kafka with Java](https://www.baeldung.com/kafka-exactly-once)

[FACT] "Each message in a topic partition has a sequential identifier called an offset, and all replicas of a partition have the same log with the same offsets." — [Confluent: Message Delivery Guarantees](https://docs.confluent.io/kafka/design/delivery-semantics.html)

[FACT] "Use Kafka partitions to ensure that events that affect the same entity are processed in the same partition and thus in order." — [RisingWave: Practical Guide to Event Sourcing with Kafka](https://risingwave.com/blog/practical-guide-to-event-sourcing-with-kafka/)

### Consumer Group Rebalancing Complexity

[FACT] "Cooperative Sticky (Incremental Cooperative Rebalancing) is the modern default since Kafka 2.4+, allowing consumers to continue processing unaffected partitions during rebalancing, and is the recommended protocol for all new applications in 2025." — [Cloudurable: Kafka Architecture: Consumers - 2025 Edition](https://cloudurable.com/blog/kafka-architecture-consumers-2025/)

[FACT] "Modern Kafka consumers leverage the revolutionary KIP-848 protocol for seamless rebalancing, enabling massive scale without sacrificing availability." — [Cloudurable: Kafka Architecture: Consumers - 2025 Edition](https://cloudurable.com/blog/kafka-architecture-consumers-2025/)

### Ordering Operational Profile

| Capability | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| Difficulty | 4/5 | 3/5 | 2/5 |
| Key requirements | Partition key design, idempotent producers, transactional API, consumer group tuning | Same as on-prem, plus K8s pod affinity for partition consumers | Managed FIFO queues (SQS FIFO, Kinesis) |
| Representative tools | Kafka transactions API, KIP-848 consumer protocol | Same | SQS FIFO, Kinesis Data Streams, EventBridge |
| Est. FTE | 0.25–0.5 FTE (design) + 0.1 ongoing | 0.1–0.25 FTE | 0.0–0.1 FTE |

---

## 7. Cross-Service Event Correlation

### The Tracing Problem in Async Systems

[FACT] "Tracing Event-Driven Architecture (EDA) flows is more complex than Request-Driven Architecture (RDA) flows, as responses do not directly return to the requester. Further complicating the issue is the common practice of deploying APM tools on-premise, preventing direct client log information upload to the APM framework." — [Solace: Building an OpenTelemetry Distributed Tracing Solution](https://solace.com/blog/opentelemetry-distributed-tracing-solution/)

[FACT] "Context propagation allows traces to build causal information about a system across services that are arbitrarily distributed across process and network boundaries." — [OpenTelemetry: Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)

[FACT] "With context propagation, signals (traces, metrics, and logs) can be correlated with each other, regardless of where they are generated." — [OpenTelemetry: Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)

[FACT] "The key enabling technology is correlation IDs and context propagation — unique identifiers that follow requests across service boundaries, implemented in Java via Spring Boot's MDC and OpenTelemetry's W3C Trace Context specification." — [Java Code Geeks: Observability Beyond Monitoring: OpenTelemetry and Distributed Tracing, February 2026](https://www.javacodegeeks.com/2026/02/observability-beyond-monitoring-opentelemetry-and-distributed-tracing.html)

[FACT] "Jaeger leads for cloud-native Kubernetes environments with native OpenTelemetry support in version 2.0, while Zipkin remains viable for simpler Java-centric deployments." — [Monitoring Framework: Jaeger Distributed Tracing Alternative](https://monitoringframework.com/pagina/jaeger-distributed-tracing-alternative)

[FACT] "A comprehensive observability stack using OpenTelemetry for instrumentation, Jaeger for real-time debugging, and Grafana Tempo for long-term storage provides effective solutions for distributed tracing." — [johal.in: Kubernetes Advanced Observability, 2025](https://www.johal.in/kubernetes-advanced-observability-implementing-opentelemetry-jaeger-and-tempo-for-distributed-tracing-2025/)

### On-Premises Correlation Stack

For on-premises event correlation, ISVs must self-host the complete observability pipeline:

| Component | Tool | Function |
|---|---|---|
| Instrumentation | OpenTelemetry SDK | Injects W3C trace context into event headers |
| Trace collection | OpenTelemetry Collector | Receives spans, batches, exports |
| Trace storage + query | Jaeger 2.0 or Grafana Tempo | Long-term trace storage and search |
| Log correlation | Loki or Elasticsearch | Correlates logs via trace ID |
| Visualization | Grafana | Unified view across traces, metrics, logs |

| Capability | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| Difficulty | 4/5 | 3/5 | 1/5 |
| Key requirements | OTel Collector, Jaeger/Tempo, Grafana, storage backend | Same tools, Helm-deployed | AWS X-Ray, CloudWatch, built-in correlation |
| Est. FTE | 0.25–0.5 FTE (setup + maintain) | 0.25 FTE | 0.0 FTE |

---

## 8. Testing Event-Driven Systems On-Premises

### Contract Testing Infrastructure

[FACT] "Modern distributed architectures are increasingly integrated in a decoupled, asynchronous fashion, with message queues such as ActiveMQ, RabbitMQ, SQS, Kafka and Kinesis being common. Pact has support for these use cases, by abstracting away the protocol and focusing on the messages passing between them." — [Pact Docs: Event-Driven Systems](https://docs.pact.io/implementation_guides/javascript/docs/messages)

[FACT] "Pact is a consumer-driven contract testing tool where the API Consumer writes a test to set out its assumptions and needs of its API Provider(s), and by unit testing the API client with Pact, it will produce a contract that can be shared to the Provider to confirm these assumptions and prevent breaking changes." — [Pact Docs: How Pact Works](https://docs.pact.io/getting_started/how_pact_works)

[FACT] "The Pact Broker is an application for sharing consumer driven contracts and verification results. The Pact Broker is an open source tool that requires you to deploy, administer and host it yourself." — [Pact Docs: Pact Broker Introduction](https://docs.pact.io/pact_broker)

[FACT] "Pact retrieves the contracts and replays the requests against a locally running provider. This makes it suitable for on-premises deployments where you control the testing infrastructure locally." — [Pact Docs: How Pact Works](https://docs.pact.io/getting_started/how_pact_works)

[FACT] "Contract testing: a simple solution to event schema chaos in event-driven architectures" — [Medium: Francisco Barril, February 2025](https://medium.com/@barril/contract-testing-a-simple-solution-to-event-schema-chaos-in-event-driven-architectures-9ea3f200ef16)

### On-Premises Testing Infrastructure Requirements

| Test Layer | Tooling | On-Prem Infrastructure Required |
|---|---|---|
| Unit tests | Language-native frameworks | None beyond CI |
| Contract tests | Pact (consumer + provider) | Self-hosted Pact Broker (Docker + PostgreSQL) |
| Schema validation | Schema Registry compatibility checks | Running Schema Registry instance |
| Integration tests | Embedded Kafka (Testcontainers) | Docker daemon on CI runners |
| End-to-end async tests | Custom event assertion harnesses | Full Kafka cluster, all consumers running |
| Event replay tests | Custom scripts against test topics | Separate Kafka cluster or isolated topics |

[FACT] Pact Broker "is an Open Source tool that requires you to deploy, administer, and host it yourself. You can host your own using the open source docker image." — [Pactflow: OSS vs. Self-Hosted Pact Broker](https://pactflow.io/oss/)

### Testing Operational Profile

| Capability | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| Difficulty | 4/5 | 3/5 | 2/5 |
| Key requirements | Self-hosted Pact Broker, Testcontainers CI support, dedicated test Kafka cluster | Same, but K8s-native test namespaces | PactFlow (SaaS), managed test environments |
| Representative tools | Pact OSS, Testcontainers, Kafka CLI | Same + Helm test hooks | PactFlow, AWS EventBridge Sandbox |
| Est. FTE | 0.25–0.5 FTE (build + CI maintenance) | 0.2–0.4 FTE | 0.1–0.2 FTE |

---

## 9. Cumulative Operational Profile

The following table aggregates all EDA pattern domains into a unified staffing estimate for an on-premises deployment serving a mid-size ISV (50 enterprise customers, production SLA).

### Cumulative FTE Summary

| Domain | On-Prem FTE (active) | On-Prem FTE (on-call) | Cloud-Native FTE (active) |
|---|---|---|---|
| Event store operations | 0.25–0.5 | 0.1 | 0.0 |
| Saga orchestration | 0.5–1.0 | 0.25 | 0.0–0.1 |
| Schema registry | 0.1–0.2 | 0.05 | 0.0 |
| Event replay infrastructure | 0.25–0.5 | 0.1 | 0.0–0.1 |
| DLQ management | 0.2–0.4 | 0.1 | 0.0–0.1 |
| Event ordering (design + ops) | 0.25–0.5 | 0.1 | 0.0–0.1 |
| Cross-service tracing | 0.25–0.5 | 0.1 | 0.0 |
| Testing infrastructure | 0.25–0.5 | 0.05 | 0.1–0.2 |
| **TOTAL** | **2.05–4.1 FTE** | **0.85 FTE** | **0.1–0.6 FTE** |

*Note: FTE ranges reflect variability by team experience and automation maturity. On-call burden is prorated 24x7 coverage. This table covers EDA pattern operations only and does not include message broker operations (see F44), compute infrastructure (see F39), or general microservices management (see F32).*

[UNVERIFIED: No single Tier 1 or Tier 2 source publishes a consolidated FTE benchmark specifically for self-hosted EDA pattern operations in 2025. The ranges above are derived by aggregating individual component estimates from multiple practitioner sources. ISVs should validate against their specific service count and event volume.*]

---

## Key Takeaways

- **On-premises EDA requires 2–4 FTE dedicated solely to EDA pattern operations** (excluding message broker, compute, and microservices management), versus 0.1–0.6 FTE for equivalent cloud-native patterns — this delta must be priced into customer contracts and deployment planning.

- **Kafka is not a native event store** — using it for event sourcing requires compensating for non-deterministic compaction, requires disabling compaction on event topics, and necessitates custom snapshot infrastructure; purpose-built alternatives (EventStoreDB, Axon Server) eliminate this class of operational risk but introduce their own cluster management overhead.

- **Saga orchestration carries the single highest on-premises operational burden** — self-hosting Temporal requires Cassandra, Elasticsearch, and four discrete Temporal service pods, with PostgreSQL explicitly documented as unsuitable for medium-to-large-scale production use; plan for 0.5–1.0 active FTE and a one-month team onboarding period.

- **Every cloud-native EDA abstraction has a self-hosted equivalent that demands operational expertise**: schema registries (Apicurio/Confluent SR), distributed tracing (Jaeger + OTel Collector + Grafana Tempo), DLQ management (custom consumer logic + AKHQ/Conduktor), and contract testing (self-hosted Pact Broker) — none of these are fire-and-forget on-premises deployments.

- **The governance gap is the least visible risk**: Gartner documents that few organizations provide guidance on event lifecycle management, schema governance, or topic design — on-premises deployments that lack these policies accumulate integration debt that manifests as outages during schema evolution or replay operations.

---

## Sources

- [EventStoreDB Clustering Documentation](https://developers.eventstore.com/server/v23.10/cluster)
- [Kurrent Docs: Clustering (v22.10)](https://docs.kurrent.io/server/v22.10/cluster)
- [GitHub: kurrent-io/EventStore](https://github.com/EventStore/EventStore)
- [Kurrent: Introduction to Event Sourcing](https://www.kurrent.io/event-sourcing)
- [Kurrent: Guide to Event Stores](https://www.kurrent.io/guide-to-event-stores)
- [Kurrent: Live Projections for Read Models with Event Sourcing and CQRS](https://www.kurrent.io/blog/live-projections-for-read-models-with-event-sourcing-and-cqrs)
- [developersvoice.com: Building Event Sourcing with EventStore and .NET](https://developersvoice.com/blog/dotnet/building-event-sourcing-with-eventstore-and-dotnet/)
- [GitHub: ksqldb-event-sourcing by eugene-khyst](https://github.com/eugene-khyst/ksqldb-event-souring)
- [Confluent: Event Sourcing Using Apache Kafka](https://www.confluent.io/blog/event-sourcing-using-apache-kafka/)
- [Confluent: Event Sourcing, CQRS, Stream Processing and Apache Kafka](https://www.confluent.io/blog/event-sourcing-cqrs-stream-processing-apache-kafka-whats-connection/)
- [Confluent Developer: Event Sourcing and CQRS Course](https://developer.confluent.io/courses/event-sourcing/cqrs/)
- [Confluent: Apache Kafka Retention Explained](https://www.confluent.io/learn/kafka-retention/)
- [Confluent: Kafka Log Compaction](https://docs.confluent.io/kafka/design/log_compaction.html)
- [Confluent Developer: Key-Based Retention Using Topic Compaction](https://developer.confluent.io/courses/architecture/compaction/)
- [Confluent: Message Delivery Guarantees for Apache Kafka](https://docs.confluent.io/kafka/design/delivery-semantics.html)
- [Confluent: Exactly-Once Semantics Are Possible](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/)
- [Confluent Schema Registry Documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)
- [Confluent: Apache Kafka Dead Letter Queue](https://www.confluent.io/learn/kafka-dead-letter-queue/)
- [Confluent: Kafka Connect Deep Dive — Error Handling and Dead Letter Queues](https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/)
- [Cloudurable: Kafka Architecture: Consumers - 2025 Edition](https://cloudurable.com/blog/kafka-architecture-consumers-2025/)
- [Cloudurable: Kafka Architecture: Log Compaction - 2025 Edition](https://cloudurable.com/blog/kafka-architecture-log-compaction-2025/)
- [RisingWave: Practical Guide to Event Sourcing with Kafka](https://risingwave.com/blog/practical-guide-to-event-sourcing-with-kafka/)
- [LKTechAcademy: Mastering Event Sourcing and CQRS with Apache Kafka and .NET Core, 2025](https://www.lktechacademy.com/2025/10/mastering-event-sourcing-cqrs-kafka-dotnet.html)
- [unanswered.io: Kafka Retention Explained: Time, Size & Compaction Rules](https://unanswered.io/guide/kafka-data-retention-explained)
- [Apicurio Registry: Introduction](https://www.apicur.io/registry/docs/apicurio-registry/1.3.3.Final/getting-started/assembly-intro-to-the-registry.html)
- [Apicurio: Managing Registry Content Using the REST API](https://www.apicur.io/registry/docs/apicurio-registry/1.3.3.Final/getting-started/assembly-managing-registry-artifacts-api.html)
- [Apicurio Blog: Exporting from Confluent Schema Registry to Apicurio Registry, March 2025](https://www.apicur.io/blog/2025/03/20/export-from-confluent)
- [AutoMQ: Which Kafka Schema Registry is Right for Your Architecture in 2025?](https://www.automq.com/blog/kafka-schema-registry-confluent-aws-glue-redpanda-apicurio-2025)
- [AWS Prescriptive Guidance: Saga Orchestration Pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-orchestration.html)
- [Microsoft: Saga Design Pattern - Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga)
- [Akka: The 10 Best Temporal Alternatives for Enterprise Teams](https://akka.io/blog/temporal-alternatives)
- [Orkes: Saga Pattern in Distributed Systems](https://orkes.io/blog/saga-pattern-in-distributed-systems/)
- [GitHub: temporalio/temporal](https://github.com/temporalio/temporal)
- [Medium (Vymo Engineering): Scaling Temporal with Postgres, Cassandra, and Elasticsearch](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b)
- [blog.taigrr.com: Temporal Server: Self-hosting a Production-Ready Instance](https://blog.taigrr.com/blog/setting-up-a-production-ready-temporal-server/)
- [Medium: My Journey Self Hosting a Temporal Cluster](https://medium.com/@mailman966/my-journey-hosting-a-temporal-cluster-237fec22a5ec)
- [procycons.com: Workflow Orchestration Platforms: Kestra vs Temporal vs Prefect (2025 Guide)](https://procycons.com/en/blogs/workflow-orchestration-platforms-comparison-2025/)
- [AxonIQ: Axon Framework](https://www.axoniq.io/framework)
- [InfoQ: Running Axon Server - CQRS and Event Sourcing in Java](https://www.infoq.com/articles/axon-server-cqrs-event-sourcing-java/)
- [Java Code Geeks: Implementing CQRS and Event Sourcing with Axon Framework in Spring, 2025](https://www.javacodegeeks.com/2025/06/implementing-cqrs-and-event-sourcing-with-axon-framework-in-spring.html)
- [intre.it: Microservices Architecture with CQRS, Event Sourcing and Axon Framework, 2025](https://www.intre.it/en/2025/04/14/microservices-cqrs-event-sourcing-axon-framework/)
- [OpenTelemetry: Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
- [Solace: Building an OpenTelemetry Distributed Tracing Solution](https://solace.com/blog/opentelemetry-distributed-tracing-solution/)
- [Java Code Geeks: Observability Beyond Monitoring: OpenTelemetry and Distributed Tracing, February 2026](https://www.javacodegeeks.com/2026/02/observability-beyond-monitoring-opentelemetry-and-distributed-tracing.html)
- [johal.in: Kubernetes Advanced Observability: OpenTelemetry, Jaeger, and Tempo, 2025](https://www.johal.in/kubernetes-advanced-observability-implementing-opentelemetry-jaeger-and-tempo-for-distributed-tracing-2025/)
- [Monitoring Framework: Jaeger Distributed Tracing Alternative](https://monitoringframework.com/pagina/jaeger-distributed-tracing-alternative)
- [Jaeger: Open Source Distributed Tracing Platform](https://www.jaegertracing.io/)
- [Pact Docs: Event-Driven Systems](https://docs.pact.io/implementation_guides/javascript/docs/messages)
- [Pact Docs: How Pact Works](https://docs.pact.io/getting_started/how_pact_works)
- [Pact Docs: Pact Broker Introduction](https://docs.pact.io/pact_broker)
- [Pactflow: OSS vs. Self-Hosted Pact Broker](https://pactflow.io/oss/)
- [SoftwareMill: Contract Testing of the Event-Driven System with Kafka and Pact](https://softwaremill.com/contract-testing-of-the-event-driven-system-with-kafka-and-pact/)
- [Solace: How to Use Pact to Contract Test your Event-Driven System](https://solace.com/blog/how-to-use-pact-to-contract-test-your-event-driven-system/)
- [Medium: Francisco Barril — Contract Testing: A Simple Solution to Event Schema Chaos, February 2025](https://medium.com/@barril/contract-testing-a-simple-solution-to-event-schema-chaos-in-event-driven-architectures-9ea3f200ef16)
- [Superstream: Kafka Dead Letter Queue Best Practices](https://www.superstream.ai/blog/kafka-dead-letter-queue)
- [Uber Blog: Building Reliable Reprocessing and Dead Letter Queues with Kafka](https://www.uber.com/blog/reliable-reprocessing/)
- [Baeldung: Exactly Once Processing in Kafka with Java](https://www.baeldung.com/kafka-exactly-once)
- [Hevo Data: What is Kafka Exactly Once Semantics?](https://hevodata.com/blog/kafka-exactly-once-semantics/)
- [Gartner: Choosing Event Brokers: The Foundation of Your Event-Driven Architecture](https://www.gartner.com/en/documents/3986571)
- [Gartner: Maturity Model for Event-Driven Architecture](https://www.gartner.com/en/documents/5593959)
- [MIT Technology Review: Enabling Real-Time Responsiveness with Event-Driven Architecture, October 2025](https://www.technologyreview.com/2025/10/06/1124323/enabling-real-time-responsiveness-with-event-driven-architecture/)
- [event-driven.io: Guide to Projections and Read Models in Event-Driven Architecture](https://event-driven.io/en/projections_and_read_models_in_event_driven_architecture/)
- [dcassisi.com: Why is Kafka not Ideal for Event Sourcing?](https://dcassisi.com/2023/05/06/why-is-kafka-not-ideal-for-event-sourcing/) [PRE-2025: 2023 — no 2025+ primary source found specifically making this consolidated argument; corroborated by multiple 2025 sources above]
- [Baytechconsulting.com: Event Sourcing Explained: The Pros, Cons & Strategic Use Cases for Modern Architects, 2025](https://www.baytechconsulting.com/blog/event-sourcing-explained-2025)
- [microservices.io: Pattern: Event Sourcing](https://microservices.io/patterns/data/event-sourcing.html)
- [microservices.io: Pattern: Saga](https://microservices.io/patterns/data/saga.html)

---

## Related — Out of Scope

- **F44: Message Broker Operations** — Covers Kafka cluster operations, ZooKeeper/KRaft management, broker configuration, and topic administration. This file assumes a functioning Kafka cluster managed per F44's scope.
- **F32: Microservices Management On-Premises** — Covers service mesh (Istio/Linkerd), service discovery, inter-service authentication, and deployment patterns. Event-driven inter-service communication patterns documented here complement but do not replace F32 coverage.
- **F39: Compute Infrastructure On-Premises** — Covers hardware provisioning, VM/bare-metal management, and Kubernetes node operations. Storage and compute requirements noted in this file (e.g., for infinite retention, Cassandra persistence) are sized but not operationalized here.
- **Schema format selection (Avro vs. Protobuf vs. JSON Schema)** — A design-time decision that affects schema registry operations but is an architectural choice outside the operational scope of this file.
