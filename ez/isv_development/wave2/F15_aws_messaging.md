# F15: AWS Messaging Services
**Agent ID:** F15 | **Scope:** AWS Managed Messaging and Event Streaming | **Audience:** C-Suite + Technical Leadership

---

## Executive Summary

AWS offers a comprehensive portfolio of eight managed messaging and event streaming services that collectively eliminate the most expensive and failure-prone aspects of running messaging infrastructure: provisioning, patching, scaling, and high-availability cluster management. For an ISV evaluating deployment models, these services represent a qualitative shift in operational profile — cloud-native deployments offload messaging operations almost entirely to AWS, while managed Kubernetes deployments can consume these services as external dependencies with minimal operational burden. On-premises deployments require self-hosting equivalent open-source systems (RabbitMQ, Kafka, ActiveMQ), which industry data shows demands between 0.5 and 10+ FTE depending on scale and complexity. The breadth of AWS messaging options — from simple queuing (SQS) to full Kafka compatibility (MSK) to serverless workflow orchestration (Step Functions) — means ISVs can select precisely the right abstraction level for each architectural requirement rather than over-engineering a single unified bus.

---

## Amazon SQS: Managed Message Queuing

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that eliminates the need to manage and operate message-oriented middleware.

### Standard vs. FIFO Queues

[AWS SQS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html) describes two queue types with distinct guarantees:

| Feature | Standard Queue | FIFO Queue |
|---|---|---|
| Throughput | Nearly unlimited API calls/second ([source](https://aws.amazon.com/sqs/features/)) | Up to 70,000 msg/sec with high-throughput mode ([source](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html)) |
| Ordering | Best-effort; occasional out-of-order delivery | Strict first-in, first-out |
| Delivery | At-least-once (rare duplicates possible) | Exactly-once processing |
| Use Case | Maximum throughput, order-tolerant | Financial transactions, order processing |
| In-flight msg limit | ~120,000 | 20,000 ([source](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-fifo.html)) |

**High-throughput FIFO mode:** When enabled, FIFO deduplication scope is set to Message Group and throughput limit is set Per Message Group ID. [AWS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html) notes that increasing the number of message groups scales capacity further.

### Dead-Letter Queues (DLQ)

[AWS SQS DLQ documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) specifies:

- DLQs isolate unconsumed messages for debugging after processing failures
- `maxReceiveCount` in the redrive policy controls how many receive attempts occur before message moves to DLQ
- DLQ type must match source queue type (Standard DLQ for Standard source; FIFO DLQ for FIFO source)
- Redrive allow policy supports up to 10 source queues using the `byQueue` option
- FIFO DLQ redrive is supported but breaks strict message ordering

### Delay Queues and Message Timers

[AWS delay queue documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html) states:

- Delay queues make messages invisible to consumers for a configurable period
- `DelaySeconds`: minimum 0 seconds, maximum **900 seconds (15 minutes)**
- Delay queues hide messages on arrival; visibility timeouts hide messages after consumption — these are distinct mechanisms
- For scheduling beyond 15 minutes, [AWS recommends](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html) EventBridge Scheduler

### Long Polling

[AWS long polling documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html):

- Long polling activates when `ReceiveMessage` wait time is set to any value greater than 0
- Maximum long polling wait time: **20 seconds**
- Reduces empty responses and lowers API costs vs. short polling
- Visibility timeout default: 30 seconds; range: 0 seconds to 12 hours

### Operational Profile Comparison — SQS

| Capability | On-Prem (RabbitMQ) | Managed K8s (ext. SQS) | Cloud-Native (SQS) |
|---|---|---|---|
| Queue Infrastructure | Difficulty: 4/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| Key requirements | HA cluster setup, disk config | IAM + SDK integration | IAM + SDK integration |
| Representative tools | RabbitMQ cluster, Erlang OTP | AWS SDK, SQS client | AWS SDK, SQS client |
| Est. FTE | 0.5–1.0 FTE | 0.05–0.1 FTE | 0.05–0.1 FTE |

*FTE assumptions: mid-size ISV, single production queue cluster, ~50 enterprise customers. On-premises FTE includes HA configuration, patching, monitoring, and incident response.*

---

## Amazon SNS: Managed Pub/Sub

Amazon Simple Notification Service (SNS) is a fully managed pub/sub messaging service enabling fanout to large numbers of subscribers.

### Topic Filtering

[AWS SNS message filtering documentation](https://aws.amazon.com/blogs/compute/simplify-pubsub-messaging-with-amazon-sns-message-filtering/) describes:

- Publishers set message attributes; each subscriber sets a subscription filter policy
- SNS matches incoming message attributes to each subscriber's filter policy
- Only matching subscribers receive messages — reducing downstream processing costs
- Eliminates the need for publishers to maintain per-subscriber routing logic

### Fanout Patterns

[AWS prescriptive guidance on pub/sub](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/publish-subscribe.html) and [SNS fanout documentation](https://aws.amazon.com/blogs/compute/messaging-fanout-pattern-for-serverless-architectures-using-amazon-sns/) describe the canonical pattern:

- SNS topic publishes to multiple SQS queues simultaneously
- Downstream microservices consume from dedicated SQS queues
- Lambda functions triggered from each SQS queue process messages independently
- Enables parallel, decoupled processing at scale without point-to-point connections

### Mobile Push Notifications

[AWS SNS mobile push documentation](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-notifications.html) specifies supported push notification platforms:

- **Apple Push Notification Service (APNS)** — iOS and macOS
- **Firebase Cloud Messaging (FCM) HTTP v1 API** — Android (v1 API now supported per [2024 update](https://docs.aws.amazon.com/sns/latest/dg/sns-fcm-authentication-methods.html))
- Amazon Device Messaging (ADM), Baidu, MPNS, WNS also supported
- SNS manages device token registration, endpoint lifecycle, and delivery retry

### SNS FIFO High-Throughput Mode (2025)

[AWS announcement, January 2025](https://aws.amazon.com/about-aws/whats-new/2025/01/high-throughput-mode-amazon-sns-fifo-topics/): SNS FIFO topics received a high-throughput mode upgrade, significantly increasing ordered message delivery rates for applications requiring strict sequencing at scale.

### Operational Profile Comparison — SNS

| Capability | On-Prem (Self-hosted) | Managed K8s (ext. SNS) | Cloud-Native (SNS) |
|---|---|---|---|
| Pub/Sub Infrastructure | Difficulty: 4/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| Key requirements | Broker cluster, routing logic | IAM + topic configuration | IAM + topic configuration |
| Representative tools | RabbitMQ exchanges, ActiveMQ | AWS SDK | AWS SDK |
| Est. FTE | 0.3–0.75 FTE | 0.05 FTE | 0.05 FTE |

---

## Amazon EventBridge: Serverless Event Bus

Amazon EventBridge is a serverless, fully managed event bus connecting AWS services, SaaS partners, and custom applications through event-driven architectures.

### Schema Registry

[AWS EventBridge features page](https://aws.amazon.com/eventbridge/features/) describes the Schema Registry:

- Stores event schemas searchable by developers across the organization
- Schema discovery: when enabled on an event bus, schemas are automatically detected and added to the registry without manual schema creation
- Generates code bindings in Java, Python, and TypeScript directly in IDE integrations
- Reduces integration friction by making event contracts discoverable

### Event Replay

[AWS EventBridge documentation](https://aws.amazon.com/eventbridge/features/) specifies Event Replay:

- Allows reprocessing of past events back to an event bus or specific EventBridge rule
- Supports debugging by isolating and replaying historical events
- Enables extending applications by hydrating new targets with historic event data
- Supports error recovery without requiring producers to resend events

### EventBridge Pipes

[AWS EventBridge Pipes documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) describes point-to-point event integration:

- Pipes connect event sources to targets with optional filtering, enrichment, and transformation
- Only charged for events that match the filter — not all inbound events
- Input transformation via `InputTemplate` supports inline JSON path expressions
- Sources include SQS, Kinesis, DynamoDB Streams, Kafka, and others

### SaaS Partner Integrations

[AWS EventBridge integrations page](https://aws.amazon.com/eventbridge/integrations/) and [March 2025 GovCloud announcement](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-eventbridge-saas-partner-integrations-aws-govcloud-us-regions/):

- Integrates with over 100 AWS services and 10+ SaaS partners
- Named partners include Salesforce, Zendesk, Datadog, PagerDuty, OneLogin, SailPoint, and others
- GovCloud support for SaaS partner integrations added in March 2025, extending regulated-industry coverage
- No custom integration code required for supported partners

### Operational Profile Comparison — EventBridge

| Capability | On-Prem (Self-hosted) | Managed K8s (ext. EventBridge) | Cloud-Native (EventBridge) |
|---|---|---|---|
| Event Bus Infrastructure | Difficulty: 5/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| Key requirements | Custom event routing, schema mgmt | IAM + rule configuration | IAM + rule configuration |
| Representative tools | Kafka + schema registry + custom code | AWS SDK, EventBridge rules | AWS SDK, EventBridge rules |
| Est. FTE | 1.0–2.0 FTE | 0.05–0.1 FTE | 0.05–0.1 FTE |

*No equivalent fully managed open-source alternative exists for EventBridge's SaaS integrations and schema registry combination; on-premises equivalents require significant custom engineering.*

---

## Amazon Kinesis Data Streams: Real-Time Streaming

Amazon Kinesis Data Streams is a managed, real-time data streaming service supporting sub-second latency at arbitrary scale.

### Sharding and Throughput

[AWS Kinesis quotas documentation](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html) and [key concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html):

- Each shard supports **1 MB/sec write** and **2 MB/sec read** throughput
- On-demand Advantage mode supports up to **10 GiB/s** instant throughput capacity ([AWS blog, 2025](https://aws.amazon.com/blogs/big-data/amazon-kinesis-data-streams-launches-on-demand-advantage-for-instant-throughput-increases-and-streaming-at-scale/))
- On-demand mode auto-scales shards; Provisioned mode requires manual shard management

### Enhanced Fan-Out

[AWS announcement, November 2025](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-kinesis-data-streams-enhanced-fan-out-consumers/):

- Enhanced fan-out provides **dedicated 2 MB/sec per shard** per consumer (vs. shared throughput in standard reads)
- **On-demand Advantage mode**: up to **50 enhanced fan-out consumers** per stream
- **On-demand Standard and Provisioned**: up to **20 enhanced fan-out consumers** per stream
- Each consumer receives its own dedicated throughput pipe, independent of other consumers
- Reduces read-side contention common in high-consumer-count architectures

### Consumer Management

[AWS enhanced consumers documentation](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html):

- Enhanced fan-out consumers use HTTP/2 push-based delivery (lower latency than polling)
- Standard consumers use `GetRecords` API polling (shared 2 MB/sec read throughput across all consumers)
- AWS manages shard-level load balancing and consumer registration

### Operational Profile Comparison — Kinesis Data Streams

| Capability | On-Prem (Self-hosted Kafka) | Managed K8s (ext. KDS) | Cloud-Native (KDS) |
|---|---|---|---|
| Stream Infrastructure | Difficulty: 5/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| Key requirements | Broker cluster, ZooKeeper/KRaft, storage | IAM + shard configuration | IAM + shard configuration |
| Representative tools | Apache Kafka, Zookeeper/KRaft | AWS SDK, Kinesis client | AWS SDK, Kinesis client |
| Est. FTE | 1.0–2.0 FTE | 0.1–0.2 FTE | 0.1–0.2 FTE |

---

## Amazon Data Firehose: Managed Stream Delivery

Amazon Data Firehose (formerly Kinesis Data Firehose) is a fully managed service for delivering streaming data to storage and analytics destinations with zero infrastructure management.

### Supported Destinations

[AWS Data Firehose documentation](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) lists current delivery targets:

- **Storage:** Amazon S3, Amazon Redshift
- **Search/Analytics:** Amazon OpenSearch Service, Apache Iceberg tables (S3)
- **Third-party:** Splunk, Snowflake, Datadog, New Relic, Dynatrace, Sumo Logic, LogicMonitor, MongoDB
- **Custom:** HTTP endpoints

### Managed Capabilities Included

[AWS Firehose features](https://www.amazonaws.cn/en/firehose/features/):

- **Automatic scaling:** throughput scales up and down without operator intervention
- **Format conversion:** converts JSON to Apache Parquet or Apache ORC before S3 delivery (reduces storage and analytics costs)
- **Dynamic partitioning:** partitions S3 output by static or dynamic keys (e.g., `customer_id`, `transaction_id`) enabling efficient downstream queries
- **Batching, compression, and encryption:** applied automatically before delivery
- **Retry logic:** built-in delivery retry to handle transient destination failures

### Operational Eliminated vs. Self-Hosted Pipelines

Self-hosted equivalents (Logstash, Fluentd, custom Kafka consumers writing to S3) require:
- Provisioning and scaling delivery pipeline infrastructure
- Managing buffer configuration, retry policies, and dead-letter handling
- Monitoring pipeline health and throughput
- Patching and updating pipeline software

[AWS documentation](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) states Firehose "requires no ongoing administration" — all of the above tasks are eliminated.

### Operational Profile Comparison — Data Firehose

| Capability | On-Prem (Logstash/Fluentd) | Managed K8s (ext. Firehose) | Cloud-Native (Firehose) |
|---|---|---|---|
| Delivery Pipeline | Difficulty: 4/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| Key requirements | Pipeline cluster, buffer config, retry | IAM + stream configuration | IAM + stream configuration |
| Representative tools | Logstash, Fluentd, custom consumers | AWS SDK, Firehose API | AWS SDK, Firehose API |
| Est. FTE | 0.5–1.0 FTE | 0.05 FTE | 0.05 FTE |

---

## Amazon MSK: Managed Streaming for Apache Kafka

Amazon Managed Streaming for Apache Kafka (MSK) provides a fully managed Apache Kafka service with full wire-level Kafka API compatibility.

### Managed Operational Tasks

[AWS MSK features page](https://aws.amazon.com/msk/features/) specifies that MSK manages:

- Cluster provisioning and broker lifecycle management
- Automated OS and Kafka security patching (previously requiring [8 hours/month of manual effort](https://aws.amazon.com/blogs/big-data/how-bazaarvoice-modernized-their-apache-kafka-infrastructure-with-amazon-msk/))
- Node failure recovery and EBS storage degradation handling — resolved within minutes without operator involvement
- Version upgrade automation for dev/test workloads
- Multi-AZ replication and availability zone failover

### MSK Serverless vs. MSK Provisioned

[AWS blog: choosing the right MSK cluster type](https://aws.amazon.com/blogs/big-data/how-to-choose-the-right-amazon-msk-cluster-type-for-you/):

| Feature | MSK Serverless | MSK Provisioned |
|---|---|---|
| Capacity management | Automatic — no shard/broker sizing | Manual — broker count and type |
| Pricing model | Per partition/hour + per GB in/out | Per broker-hour + storage |
| Kafka version control | AWS-managed; version not selectable | Customer-selectable |
| Custom configuration | Limited | Full |
| Best for ISV use | Variable, unpredictable workloads | Stable, predictable high-throughput |

### MSK Connect (Kafka Connect)

[AWS MSK Connect documentation](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html):

- Eliminates operational burden of patching, provisioning, and scaling Kafka Connect clusters
- Continuously monitors Connect cluster health and automates patching and version upgrades without disruption
- Limitation: MSK Connect provides the infrastructure but customers must bring, manage, and maintain their own connectors ([Confluent comparison, 2025](https://www.confluent.io/confluent-cloud-vs-amazon-msk/))

### Schema Registry Integration

[AWS blog on MSK + Glue Schema Registry](https://aws.amazon.com/blogs/big-data/build-an-end-to-end-change-data-capture-with-amazon-msk-connect-and-aws-glue-schema-registry/):

- MSK integrates with AWS Glue Schema Registry for schema governance
- Enforces schema compatibility during producer/consumer registration
- Supports schema evolution policies (backward, forward, full compatibility)

### Self-Hosted Kafka FTE Requirements

[Airbyte Kafka pricing guide](https://airbyte.com/data-engineering-resources/apache-kafka-pricing) and [AutoMQ analysis](https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons):

- Typical team: **0.5–1.0 FTE** for smaller production deployments
- Global-scale operations: **7–10 engineers**
- Production-grade operational costs (infrastructure + staffing): **$12,800–$42,800+/month** for conservative estimates

[MSK vs. self-hosted cost comparison (oneuptime.com, January 2026)](https://oneuptime.com/blog/post/2026-01-21-kafka-managed-comparison/view):

- 6-broker MSK Provisioned: ~$5,256/month brokers + $500 storage + ~$2,500/month (0.5 FTE) = **~$8,256/month total**
- Self-managed equivalent: infrastructure + **$8,000–$12,000/month SRE cost**

### Operational Profile Comparison — MSK

| Capability | On-Prem (Self-hosted Kafka) | Managed K8s (ext. MSK) | Cloud-Native (MSK) |
|---|---|---|---|
| Kafka Cluster | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 2/5 |
| Key requirements | Brokers, ZooKeeper/KRaft, storage, monitoring | MSK config, IAM, VPC peering | MSK config, IAM, VPC |
| Representative tools | Apache Kafka, ZooKeeper/KRaft, JMX exporters | MSK + Glue Schema Registry | MSK + Glue Schema Registry |
| Est. FTE | 1.0–2.0 FTE | 0.25–0.5 FTE | 0.25–0.5 FTE |

*MSK Managed K8s and Cloud-Native FTE are similar because MSK is consumed as an external service in both cases; the primary operational tasks (cluster sizing, IAM, monitoring integration) are identical. Difficulty rating reflects MSK Provisioned; MSK Serverless reduces difficulty by ~1 point in both columns.*

---

## Amazon MQ: Managed ActiveMQ and RabbitMQ

Amazon MQ provides managed message broker service for legacy-protocol applications using Apache ActiveMQ or RabbitMQ.

### Migration from On-Premises

[AWS MQ migration guide](https://docs.aws.amazon.com/amazon-mq/latest/migration-guide/concept-chapter-about.html) and [RabbitMQ migration documentation](https://docs.aws.amazon.com/amazon-mq/latest/migration-guide/rabbitmq-migration-guide.html):

- **ActiveMQ:** Compatible with JMS, AMQP, MQTT, OpenWire, STOMP — minimal code changes for migration
- **RabbitMQ:** Supports Federation and Shovel plugins for migrating messages from self-managed brokers; queue, exchange, user, and policy definitions can be exported and imported
- Phased migration approach: bridge connectivity between on-premises broker and Amazon MQ, validate, then cut over — reducing disruption risk
- [IBM MQ migration path also documented](https://aws.amazon.com/blogs/compute/migrating-from-ibm-mq-to-amazon-mq-using-a-phased-approach/)

### Operational Tasks Eliminated

[AWS MQ features](https://aws.amazon.com/amazon-mq/features/) and [AWS MQ FAQs](https://aws.amazon.com/amazon-mq/faqs/):

- OS and broker software patching handled by AWS (automatic minor version upgrades on configurable maintenance windows)
- Multi-AZ high availability: Amazon MQ automatically manages broker policies for classic mirroring across all nodes
- AZ failover: if an Availability Zone outage occurs, Amazon MQ automatically relocates affected RabbitMQ nodes to a different AZ — no operator action required
- Cluster rebalancing after AZ recovery is automated

### Real-World Migration Outcome

[Detectify migration case study (2025)](https://blog.detectify.com/best-practices/migrating-critical-messaging-from-self-hosted-rabbitmq-to-amazon-mq/): "The day-to-day firefighting around clustering issues and mysterious failures has mostly gone away" after migrating from self-hosted RabbitMQ to Amazon MQ.

### Self-Hosted Challenges

[RabbitMQ official clustering documentation](https://www.rabbitmq.com/docs/clustering) notes that self-hosted clusters require:
- All nodes to run compatible RabbitMQ and Erlang versions
- Pre-shared authentication secrets managed by deployment tooling
- Monitoring via `rabbitmq-diagnostics` and `rabbitmqctl` CLI across all nodes
- Manual quorum queue management for HA guarantees

[StackPioneers guide (July 2025)](https://stackpioneers.com/2025/07/15/amazon-mq-the-complete-guide-to-managed-message-brokers/): "RabbitMQ message brokers require significant investment in the expertise needed for creating and patching complex clustered deployments."

### Operational Profile Comparison — Amazon MQ

| Capability | On-Prem (Self-hosted) | Managed K8s (ext. MQ) | Cloud-Native (Amazon MQ) |
|---|---|---|---|
| Broker Cluster | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 2/5 |
| Key requirements | HA clustering, Erlang/JVM tuning, patching | VPC config, IAM, broker sizing | VPC config, IAM, broker sizing |
| Representative tools | RabbitMQ/ActiveMQ cluster + monitoring | Amazon MQ SDK/AMQP | Amazon MQ SDK/AMQP |
| Est. FTE | 0.5–1.0 FTE | 0.1–0.25 FTE | 0.1–0.25 FTE |

*Amazon MQ is the appropriate migration path for ISVs with existing AMQP/JMS application code. New greenfield architectures should favor SQS/SNS for simpler operational profile.*

---

## AWS Step Functions: Managed Workflow Orchestration

AWS Step Functions is a serverless visual workflow service for orchestrating distributed application components and long-running business processes.

### State Machine Architecture

[AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html) and [workflow states](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-states.html):

- Integrates with **14,000+ API actions across 220+ AWS services**
- State types: Choice (conditional branching), Wait (timed pause), Map (parallel iteration), Parallel (concurrent branches), Task (service integration)
- Default query language shifted from JSONPath to **JSONata** at re:Invent 2024 for new state machines
- [February 2025 quota increase](https://aws.amazon.com/about-aws/whats-new/2025/02/aws-step-functions-100-000-state-machines-activities-account/): default maximum state machines per account increased from 10,000 to **100,000**

### Standard vs. Express Workflows

[AWS Step Functions pricing](https://aws.amazon.com/step-functions/pricing/) and [workflow type documentation](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html):

| Feature | Standard Workflows | Express Workflows |
|---|---|---|
| Pricing | $0.025 per 1,000 state transitions | $1 per 1M requests + duration/memory |
| Max duration | 1 year | 5 minutes |
| Execution rate | >2,000 executions/second | >100,000 executions/second |
| Execution model | Exactly-once | At-least-once |
| History | Full execution history via API | CloudWatch Logs only |
| Use case | Long-running, auditable workflows | High-volume event processing, IoT |
| Free tier | 4,000 state transitions/month (perpetual) | Not included |

[Cost comparison example](https://aws.amazon.com/step-functions/pricing/): 1,000 Standard Workflow executions cost approximately $0.42; 1,000 Express Workflow executions cost approximately $0.01.

### Operational Burden Eliminated

[AWS Step Functions features page](https://aws.amazon.com/step-functions/features/):

- No workflow infrastructure to provision, scale, or patch
- Built-in error handling, retry logic, and timeout management
- Automated state persistence — no custom database required for workflow state
- Execution history and audit trail included without additional tooling
- Equivalent self-hosted alternatives (Apache Airflow, Temporal, Prefect) require significant operational overhead for cluster management, high availability, and state persistence

### Operational Profile Comparison — Step Functions

| Capability | On-Prem (Self-hosted Airflow/Temporal) | Managed K8s (Self-hosted on K8s) | Cloud-Native (Step Functions) |
|---|---|---|---|
| Workflow Orchestration | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| Key requirements | Cluster mgmt, DB for state, HA config | Helm charts, persistent volumes | IAM + state machine definition |
| Representative tools | Airflow, Temporal, Prefect | Airflow/Temporal on K8s | AWS SDK, Step Functions console |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.05–0.1 FTE |

---

## Cross-Service Operational Burden Summary

The table below aggregates the operational burden across all eight AWS messaging services, comparing total estimated FTE requirements per deployment model for a mid-size ISV serving ~50 enterprise customers.

| Service | Self-Hosted Equivalent | On-Prem FTE | Managed K8s FTE | Cloud-Native FTE |
|---|---|---|---|---|
| SQS | RabbitMQ queuing | 0.5–1.0 | 0.05–0.10 | 0.05–0.10 |
| SNS | RabbitMQ exchanges / custom fanout | 0.3–0.75 | 0.05 | 0.05 |
| EventBridge | Custom event router + schema registry | 1.0–2.0 | 0.05–0.10 | 0.05–0.10 |
| Kinesis Data Streams | Apache Kafka | 1.0–2.0 | 0.10–0.20 | 0.10–0.20 |
| Data Firehose | Logstash / Fluentd + S3 sink | 0.5–1.0 | 0.05 | 0.05 |
| MSK | Self-hosted Kafka cluster | 1.0–2.0 | 0.25–0.50 | 0.25–0.50 |
| Amazon MQ | Self-hosted RabbitMQ / ActiveMQ | 0.5–1.0 | 0.10–0.25 | 0.10–0.25 |
| Step Functions | Airflow / Temporal | 0.5–1.0 | 0.25–0.50 | 0.05–0.10 |
| **Total Range** | | **5.3–10.75 FTE** | **0.90–1.70 FTE** | **0.70–1.35 FTE** |

*Assumptions: mid-size ISV, production-grade deployments, 24/7 availability requirements, on-call burden distributed across team. On-premises figures include patching, HA management, incident response, and capacity planning. FTEs are additive only if all services are deployed simultaneously; most ISVs use a subset.*

---

## Key Takeaways

- **On-premises messaging carries a staffing premium of 4–8x** compared to cloud-native or managed Kubernetes deployments. A full stack of self-hosted messaging services (Kafka, RabbitMQ, workflow orchestration, and stream delivery) requires 5–10 FTE for a mid-size ISV — a cost that cloud-native managed services reduce to under 1.5 FTE for equivalent functionality.

- **AWS messaging services are composable, not monolithic.** ISVs should select services based on the specific abstraction needed: SQS/SNS for simple decoupling, EventBridge for event-driven cross-service integration, Kinesis for real-time streaming analytics, MSK for Kafka-compatible workloads requiring ecosystem compatibility, and Step Functions for complex workflow orchestration.

- **MSK and Amazon MQ are migration bridges, not greenfield-first choices.** MSK is the appropriate choice when Kafka ecosystem compatibility (connectors, consumer groups, existing producers) is required. Amazon MQ is the right path when migrating AMQP/JMS applications from on-premises to avoid rewriting message passing logic. New architectures should default to SQS/SNS/EventBridge.

- **Step Functions provides the largest relative operational advantage** in cloud-native vs. Managed Kubernetes deployments (from 0.25–0.5 FTE on K8s to 0.05–0.1 FTE fully managed), because self-hosted workflow engines like Airflow and Temporal carry non-trivial K8s operational burden even when running on managed Kubernetes.

- **Kinesis Data Streams enhanced fan-out expansion in November 2025 (up to 50 consumers in On-demand Advantage mode)** removes a previously significant architectural constraint for high-consumer-count real-time processing pipelines, making KDS competitive with MSK for read-heavy streaming workloads where Kafka protocol compatibility is not required.

---

## Related — Out of Scope

- **Amazon SES / Amazon Pinpoint / AWS End User Messaging:** Transactional email and SMS delivery — these are end-user messaging services, not application messaging infrastructure. Outside F15 scope.
- **AWS IoT Core messaging:** IoT-specific MQTT broker service — relevant for IoT workloads but not covered in this agent's scope.
- **Amazon DynamoDB Streams:** Change data capture streaming — overlaps with messaging patterns but is classified as a data service. See [F9: AWS Data Services] for coverage.
- **Confluent Cloud vs. MSK:** Comparative analysis of Kafka-as-a-service providers outside AWS is out of scope for this agent.

---

## Sources

- [Amazon SQS Dead-Letter Queues Documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- [Amazon SQS Queue Types Documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html)
- [Amazon SQS FIFO Queue Quotas](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-fifo.html)
- [Amazon SQS High-Throughput FIFO Mode](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.html)
- [Amazon SQS Features Page](https://aws.amazon.com/sqs/features/)
- [Amazon SQS Delay Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html)
- [Amazon SQS Message Timers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-timers.html)
- [Amazon SQS Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html)
- [AWS SNS Message Filtering Blog](https://aws.amazon.com/blogs/compute/simplify-pubsub-messaging-with-amazon-sns-message-filtering/)
- [Amazon SNS Fanout Pattern Blog](https://aws.amazon.com/blogs/compute/messaging-fanout-pattern-for-serverless-architectures-using-amazon-sns/)
- [AWS Pub/Sub Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/publish-subscribe.html)
- [Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-notifications.html)
- [Amazon SNS FCM v1 API Authentication](https://docs.aws.amazon.com/sns/latest/dg/sns-fcm-authentication-methods.html)
- [Amazon SNS FIFO High-Throughput Mode Announcement — January 2025](https://aws.amazon.com/about-aws/whats-new/2025/01/high-throughput-mode-amazon-sns-fifo-topics/)
- [Amazon EventBridge Features](https://aws.amazon.com/eventbridge/features/)
- [Amazon EventBridge Integrations](https://aws.amazon.com/eventbridge/integrations/)
- [Amazon EventBridge SaaS GovCloud Announcement — March 2025](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-eventbridge-saas-partner-integrations-aws-govcloud-us-regions/)
- [Amazon EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html)
- [Amazon EventBridge Pipes Event Filtering](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-filtering.html)
- [Amazon EventBridge Pipes Input Transformation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-input-transformation.html)
- [Amazon Kinesis Data Streams Service Quotas](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
- [Amazon Kinesis Data Streams Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)
- [Amazon Kinesis Data Streams Enhanced Fan-Out](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html)
- [Amazon Kinesis Data Streams — 50 Enhanced Fan-Out Consumers Announcement — November 2025](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-kinesis-data-streams-enhanced-fan-out-consumers/)
- [Amazon Kinesis Data Streams On-Demand Advantage Blog](https://aws.amazon.com/blogs/big-data/amazon-kinesis-data-streams-launches-on-demand-advantage-for-instant-throughput-increases-and-streaming-at-scale/)
- [Amazon Data Firehose What Is Documentation](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
- [Amazon Data Firehose FAQs](https://aws.amazon.com/firehose/faqs/)
- [Amazon MSK Features](https://aws.amazon.com/msk/features/)
- [Amazon MSK FAQs](https://aws.amazon.com/msk/faqs/)
- [Amazon MSK Connect Documentation](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html)
- [Amazon MSK + Glue Schema Registry Blog](https://aws.amazon.com/blogs/big-data/build-an-end-to-end-change-data-capture-with-amazon-msk-connect-and-aws-glue-schema-registry/)
- [Bazaarvoice MSK Migration Case Study](https://aws.amazon.com/blogs/big-data/how-bazaarvoice-modernized-their-apache-kafka-infrastructure-with-amazon-msk/)
- [How to Choose the Right MSK Cluster Type](https://aws.amazon.com/blogs/big-data/how-to-choose-the-right-amazon-msk-cluster-type-for-you/)
- [MSK Serverless Documentation](https://docs.aws.amazon.com/msk/latest/developerguide/serverless.html)
- [Confluent Cloud vs. Amazon MSK Comparison](https://www.confluent.io/confluent-cloud-vs-amazon-msk/)
- [Airbyte: Apache Kafka Pricing Guide](https://airbyte.com/data-engineering-resources/apache-kafka-pricing)
- [AutoMQ: Self-Hosted vs Fully Managed Kafka](https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons)
- [OneUptime: Confluent Cloud vs AWS MSK vs Self-Hosted Kafka — January 2026](https://oneuptime.com/blog/post/2026-01-21-kafka-managed-comparison/view)
- [Amazon MQ Features](https://aws.amazon.com/amazon-mq/features/)
- [Amazon MQ FAQs](https://aws.amazon.com/amazon-mq/faqs/)
- [Amazon MQ Migration Guide](https://docs.aws.amazon.com/amazon-mq/latest/migration-guide/concept-chapter-about.html)
- [Migrating to Amazon MQ for RabbitMQ](https://docs.aws.amazon.com/amazon-mq/latest/migration-guide/rabbitmq-migration-guide.html)
- [Migrating from IBM MQ to Amazon MQ](https://aws.amazon.com/blogs/compute/migrating-from-ibm-mq-to-amazon-mq-using-a-phased-approach/)
- [Amazon MQ RabbitMQ Cluster Deployment](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-broker-architecture-cluster.html)
- [Detectify: Migrating from Self-Hosted RabbitMQ to Amazon MQ (2025)](https://blog.detectify.com/best-practices/migrating-critical-messaging-from-self-hosted-rabbitmq-to-amazon-mq/)
- [StackPioneers: Amazon MQ Complete Guide — July 2025](https://stackpioneers.com/2025/07/15/amazon-mq-the-complete-guide-to-managed-message-brokers/)
- [RabbitMQ Clustering Documentation](https://www.rabbitmq.com/docs/clustering)
- [AWS Step Functions Features](https://aws.amazon.com/step-functions/features/)
- [AWS Step Functions Pricing](https://aws.amazon.com/step-functions/pricing/)
- [AWS Step Functions Workflow Types](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html)
- [AWS Step Functions State Machines](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html)
- [AWS Step Functions Workflow States](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-states.html)
- [AWS Step Functions — 100,000 State Machines Quota Announcement — February 2025](https://aws.amazon.com/about-aws/whats-new/2025/02/aws-step-functions-100-000-state-machines-activities-account/)
