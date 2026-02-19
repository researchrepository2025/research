# F55a: Kubernetes Data Services & Stateful Workloads

**Research Question:** How do Kubernetes-native data services (CloudNativePG, Strimzi Kafka, Redis on K8s) compare to fully managed cloud data services (RDS, MSK, ElastiCache), and what operational gap remains when running stateful workloads on managed K8s?

**Scope:** K8s-native data services vs managed cloud data services. See [F52: K8s Platforms] for K8s platform coverage, [F54: K8s Operators] for general operator patterns, and [F41–F42: On-Prem Data Services] for on-premises equivalents.

---

## Executive Summary

Kubernetes-native data operators — CloudNativePG, Strimzi, and the Redis Operator family — have matured significantly through 2025, reaching functional parity with managed cloud services on most Day 1 capabilities such as provisioning, replication, and automated failover. The critical gap is not feature availability but operational burden: running these operators on managed Kubernetes (EKS/AKS/GKE) requires dedicated platform engineering effort that managed services absorb entirely, and the hidden labor cost frequently erases apparent compute savings. For a mid-size ISV serving 50 enterprise customers, the operational gap between Managed K8s with self-hosted data services and fully managed cloud services equates to roughly 1.5–3.0 additional FTE in ongoing operational effort. The decision hinges on three factors: the need to avoid cloud vendor lock-in, extension or configuration requirements that managed services prohibit, and the organization's existing platform engineering capacity. Data gravity — the cost and latency of moving data once accumulated — further locks workloads into whichever deployment model is selected initially, making the choice largely irreversible at scale.

---

## 1. CloudNativePG vs RDS / Azure SQL / Cloud SQL

### 1.1 CloudNativePG Status and Architecture

[FACT] CloudNativePG was accepted into the CNCF Sandbox on January 15, 2025, and applied for CNCF Incubation on November 12, 2025.
URL: https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/
Date: December 2025

[FACT] CloudNativePG is described as "the only PostgreSQL operator project for Kubernetes that is community-owned and governed under a transparent, vendor-neutral model."
URL: https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/
Date: December 2025

[STATISTIC] CloudNativePG operator image reached 132+ million downloads and grew from 4,900 to 7,700+ GitHub stars through 2025.
URL: https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/
Date: December 2025

[FACT] CloudNativePG v1.26 (May 2025) introduced offline in-place major upgrades and declarative database management; v1.27 (August 2025) added logical decoding slot synchronization for HA in CDC workloads; v1.28 (December 2025) promoted quorum-based failover to stable and added declarative FDW support.
URL: https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/
Date: December 2025

[FACT] CloudNativePG manages storage directly via PVC templates — one PVC per PostgreSQL instance — rather than through StatefulSets. It supports a dedicated Write-Ahead Log (WAL) storage volume; WAL storage cannot be removed after initial configuration.
URL: https://cloudnative-pg.io/documentation/1.20/storage/
Date: 2025

### 1.2 Feature Comparison: CloudNativePG vs RDS

| Capability | CloudNativePG (Managed K8s) | AWS RDS PostgreSQL (Cloud-Native) |
|---|---|---|
| Automatic failover | Yes — quorum-based (stable, v1.28) | Yes — 60–120 sec failover (Multi-AZ) |
| Failover RTO | Sub-minute (operator-managed) | 60–120 seconds (RDS Multi-AZ) |
| Point-in-time recovery | Yes — WAL-based, declarative | Yes — 5-minute granularity (standard) |
| Extension support | Full — any extension loadable | Limited — AWS-approved extensions only |
| Major version upgrades | In-place offline upgrade (v1.26+) | AWS-managed, limited control |
| Custom configurations | Full postgresql.conf control | Parameter group constraints |
| Backup tool | Barman Cloud Plugin (GA 2025) | Native automated backups |
| SLA | Dependent on K8s cluster SLA | 99.95% (Multi-AZ) |

[STATISTIC] AWS RDS Multi-AZ failover time: 60–120 seconds. Aurora failover time: 30–60 seconds. Self-managed/K8s EC2: 2–30+ minutes without operator.
URL: https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql
Date: December 2025

[FACT] AWS RDS and Aurora do not support custom extensions such as TimescaleDB or Citus. EC2 and Kubernetes deployments allow full extension control.
URL: https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql
Date: December 2025

### 1.3 Backup and Recovery Specifics

[FACT] CloudNativePG supports online/hot backups with no downtime required, using continuous physical backup and WAL archiving. The Barman Cloud Plugin reached General Availability in 2025.
URL: https://cloudnative-pg.io/documentation/1.20/backup/
Date: 2025

[STATISTIC] CloudNativePG recovery time benchmarks: for a 45 GB database, backup time is approximately 60–100 minutes; restore time approximately 30–60 minutes depending on compression algorithm.
URL: https://medium.com/@valerykretinin/reliable-postgresql-backup-and-recovery-with-cloudnativepg-and-gcs-e44ad0de13a2
Date: 2025

[FACT] CloudNativePG parallel WAL restore can use up to 8 concurrent jobs to fetch WAL files from archive, reducing recovery time.
URL: https://cloudnative-pg.io/documentation/1.20/recovery/
Date: 2025

### 1.4 Storage Requirements

[FACT] CloudNativePG documentation requires that storage performance be benchmarked using `fio` for underlying IOPS and `pgbench` for database-level throughput before production deployment.
URL: https://cloudnative-pg.io/documentation/1.20/storage/
Date: 2025

[FACT] For Ceph and Longhorn deployments, CloudNativePG documentation requires storage classes to be configured with single replica settings to avoid write amplification, because CloudNativePG provides resiliency at the cluster level rather than at the storage layer.
URL: https://cloudnative-pg.io/documentation/1.20/storage/
Date: 2025

[FACT] NVMe-backed volumes are recommended for PostgreSQL on Kubernetes because "PostgreSQL is sensitive to disk latency and IOPS, especially under write-heavy workloads."
URL: https://www.simplyblock.io/blog/choosing-a-kubernetes-postgres-operator/
Date: 2025

### 1.5 Cost Comparison: PostgreSQL Deployment Models

[STATISTIC] Monthly cost estimates for a 100 GB PostgreSQL database in us-east-1 (December 2025): Aurora $800–$1,200+; RDS $450–$650; EC2 self-managed $200–$400 (compute only, before operational labor).
URL: https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql
Date: December 2025

[STATISTIC] Monthly time investment for database operations: Aurora ~10 hours/month; RDS ~15 hours/month; EC2 self-managed ~40–60 hours/month.
URL: https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql
Date: December 2025

[STATISTIC] At an assumed $100/hour engineering rate, EC2 self-managed (and by extension Kubernetes-hosted) PostgreSQL adds $4,000–$6,000/month in hidden labor costs compared to RDS.
URL: https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql
Date: December 2025

### 1.6 Operational Difficulty Rating

| Capability Domain | On-Premises | Managed K8s (CloudNativePG) | Cloud-Native (RDS) |
|---|---|---|---|
| Provisioning | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Manual server setup | Helm chart + CRD | Console/Terraform |
| | DBA + infra team | Platform engineer | No DB expertise needed |
| | Est. FTE: 1.0+ | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 |
| HA / Failover | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Patroni or manual | Operator-managed quorum | Fully managed |
| | DBAs + SRE | Operator + K8s expertise | No config needed |
| | Est. FTE: 0.5 on-call | Est. FTE: 0.25 on-call | Est. FTE: 0.1 on-call |
| Major upgrades | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Full manual process | In-place offline (v1.26+) | AWS-scheduled or triggered |
| | DBA with maintenance window | Platform engineer + window | Minimal engineer time |
| | Est. FTE: 0.5 per event | Est. FTE: 0.25 per event | Est. FTE: 0.1 per event |
| Extension management | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 4/5 |
| | Full control, manual | Full control via OCI images (v1.28+) | AWS-approved list only |
| Monitoring | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-built | Prometheus + operator metrics | CloudWatch integrated |

---

## 2. Strimzi Kafka vs Amazon MSK / Azure Event Hubs / Confluent Cloud

### 2.1 Strimzi Operational State (2025)

[FACT] Strimzi removed support for ZooKeeper-based Kafka clusters starting with version 0.46. To upgrade to Strimzi 0.46 or later, ZooKeeper-based clusters must first be migrated to KRaft mode.
URL: https://strimzi.io/kraft/
Date: 2025

[FACT] Strimzi provides a semi-automated ZooKeeper-to-KRaft migration process triggered by annotating the Kafka resource, but it "is not that straightforward because it requires manual configurations and several rolling updates."
URL: https://strimzi.io/blog/2024/03/22/strimzi-kraft-migration/
Date: 2024 [PRE-2025: 2024 — no 2025 source found for this specific migration procedure detail]

[FACT] Strimzi KRaft upgrade support (Kafka version upgrades on KRaft clusters) has been available since Strimzi 0.39.0.
URL: https://github.com/strimzi/proposals/blob/main/061-kraft-upgrades-and-downgrades.md
Date: 2025

### 2.2 Amazon MSK Pricing (2025)

[STATISTIC] Amazon MSK broker pricing per hour (us-east-1): kafka.t3.small $0.0456/hr; kafka.m5.large $0.21/hr; kafka.m7g.large $0.204/hr; kafka.m5.xlarge $0.42/hr.
URL: https://airbyte.com/data-engineering-resources/apache-kafka-pricing
Date: 2025

[STATISTIC] Amazon MSK Express broker pricing per hour: express.m7g.large $0.408/hr; express.m7g.4xlarge $3.264/hr; express.m7g.16xlarge $13.056/hr.
URL: https://airbyte.com/data-engineering-resources/apache-kafka-pricing
Date: 2025

[STATISTIC] Amazon MSK Serverless pricing: $0.75/cluster-hour; $0.0015/partition-hour; $0.10/GiB storage/month; $0.10/GiB data in; $0.05/GiB data out.
URL: https://airbyte.com/data-engineering-resources/apache-kafka-pricing
Date: 2025

[STATISTIC] Real-world MSK cost for a small production cluster (3 × kafka.m5.large brokers, 1 TB storage, 100 GB data transfer): approximately $566/month — brokers $453.60, storage $102.40, data transfer $10.00.
URL: https://airbyte.com/data-engineering-resources/apache-kafka-pricing
Date: 2025

[STATISTIC] AWS MSK with Graviton3 (M7g instances) provides up to 24% savings on compute costs compared to equivalent M5 instances, and Tiered Storage reduces overall storage cost by up to 50%.
URL: https://aws.amazon.com/blogs/big-data/amazon-msk-now-provides-up-to-29-more-throughput-and-up-to-24-lower-costs-with-aws-graviton3-support/
Date: 2025

### 2.3 Confluent Cloud Pricing

[STATISTIC] Confluent Cloud pricing tiers: Basic first eCKU free then $0.14/hr; Standard $0.75/hr; Enterprise $2.25/hr. Storage $0.08/GB-month across all tiers.
URL: https://airbyte.com/data-engineering-resources/apache-kafka-pricing
Date: 2025

### 2.4 Staffing and Operational Requirements

[STATISTIC] One organization reported they "would have needed to hire at least 10 more people to manage Kafka themselves" when evaluating the build-vs-buy decision for managed Kafka.
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons
Date: 2025

[STATISTIC] Confluent claims "up to 60% savings with their managed service compared to self-hosted deployments" when total cost of ownership is calculated.
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons
Date: 2025

[FACT] Self-hosted Kafka (including Strimzi on Kubernetes) requires dedicated expertise across 10 operational domains: scalability and resource management; performance tuning; data retention management; monitoring and observability; broker management and failures; security and access control; schema management; data governance and compliance; upgrades and maintenance; and multi-cluster deployments.
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons
Date: 2025

[QUOTE] "Managed services automate these processes, allowing teams to create clusters in minutes rather than days or weeks."
— AutoMQ Blog
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons
Date: 2025

### 2.5 Operational Difficulty Rating

| Capability Domain | On-Premises | Managed K8s (Strimzi) | Cloud-Native (MSK) |
|---|---|---|---|
| Initial provisioning | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Manual broker setup | Helm + KafkaNodePool CRD | Console/Terraform |
| | Kafka/ZooKeeper experts | Platform engineer | No Kafka expertise |
| | Est. FTE: 1.0+ | Est. FTE: 0.5 | Est. FTE: 0.25 |
| KRaft migration | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Full manual migration | Semi-automated, rolling updates required | AWS-managed |
| | Kafka expert required | Platform + Kafka expertise | N/A |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0 |
| Partition rebalancing | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Manual Cruise Control | Manual or operator-assisted | MSK-managed |
| Major version upgrade | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Manual rolling restart | Operator-managed rolling | AWS-scheduled |
| | Est. FTE: 0.5 per event | Est. FTE: 0.25 per event | Est. FTE: 0.1 per event |
| Monitoring | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Custom JMX exporters | Prometheus + Strimzi exporters | CloudWatch integrated |

---

## 3. Redis on Kubernetes vs ElastiCache / Azure Cache / Memorystore

### 3.1 ElastiCache Pricing (2025)

[STATISTIC] Amazon ElastiCache on-demand pricing: cache.t3.micro $0.025/hr ($219/year); cache.t3.small $0.05/hr ($438/year).
URL: https://www.prosperops.com/blog/elasticache-vs-redis/
Date: 2025

[FACT] AWS ElastiCache best practices require two or more replicas across Availability Zones, which increases the cost of memory and nodes by approximately three times. For a 100 GB HA dataset, ElastiCache requires approximately 400 GB provisioned capacity, versus 200 GB for equivalent Redis Cloud alternatives.
URL: https://redis.io/blog/redis-vs-elasticache-which-is-more-cost-effective/
Date: 2025

[FACT] AWS ElastiCache reserves 25% of node memory by default for operations such as backups and replication, reducing usable keyspace to 75% of provisioned capacity.
URL: https://www.prosperops.com/blog/elasticache-vs-redis/
Date: 2025

[STATISTIC] Migrating from Redis to Valkey on ElastiCache can reduce costs by 20–30%. Example: cache r6g.8xlarge costs $3.66/hr with Redis versus $2.93/hr with Valkey.
URL: https://www.pump.co/blog/aws-migrate-redis-to-valkey
Date: 2025

### 3.2 Redis on Kubernetes: Architecture and Persistence

[FACT] Redis supports two persistence methods on Kubernetes: Append-Only File (AOF), which logs every write operation and is more durable, and Redis DataBase (RDB), which generates periodic point-in-time snapshots. AOF results in faster recovery from failure; RDB results in faster startup from a smaller file.
URL: https://www.plural.sh/blog/redis-cluster-on-kubernetes/
Date: 2025

[FACT] Kubernetes persistent volume claims (PVC) must be enabled when AOF or RDB persistence is configured for Redis, or when Redis Cluster mode is used. Recommended storage class is fast SSD.
URL: https://github.com/bitnami/charts/blob/main/bitnami/redis/README.md
Date: 2025

[FACT] The Spotahome Redis Operator creates, configures, and manages high-availability Redis with Sentinel-based automatic failover on Kubernetes.
URL: https://github.com/spotahome/redis-operator
Date: 2025

### 3.3 Feature Gap Analysis: Redis on K8s vs ElastiCache

[FACT] Following the release of Redis 7.2, ElastiCache is no longer built on upstream Redis and does not support Redis Search and Query capabilities (FT.SEARCH, FT.INDEX). Redis Enterprise on Kubernetes retains these capabilities.
URL: https://redis.io/compare/elasticache/
Date: 2025

[FACT] ElastiCache restricts configuration customization that is available on self-hosted or Kubernetes-deployed Redis, "which can affect performance" in specialized use cases.
URL: https://www.cloudoptimo.com/blog/redis-vs-amazon-elasticache-a-comprehensive-guide-to-caching-performance-and-scalability/
Date: 2025

[FACT] Redis deployments on Kubernetes offer multi-VPC, multi-account, and hybrid connectivity options not available in ElastiCache's private-only, single-VPC architecture. This becomes relevant for ISVs serving customers across multiple cloud environments.
URL: https://redis.io/blog/redis-vs-elasticache/
Date: 2025

### 3.4 Operational Difficulty Rating

| Capability Domain | On-Premises | Managed K8s (Redis Operator) | Cloud-Native (ElastiCache) |
|---|---|---|---|
| Deployment | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Manual Redis Sentinel | Bitnami Helm or operator | Console/Terraform |
| | Redis expert required | Platform engineer | No Redis expertise |
| | Est. FTE: 0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05 |
| Persistence management | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Manual AOF/RDB config | PVC + operator-managed | AWS-managed |
| Scaling | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Manual cluster expansion | Helm upgrade + PVC | Console scaling |
| HA / Sentinel | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Manual Sentinel config | Operator-managed Sentinel | Fully managed |
| | Est. FTE: 0.25 on-call | Est. FTE: 0.1 on-call | Est. FTE: 0.05 on-call |

---

## 4. Elasticsearch / OpenSearch on Kubernetes vs Managed Equivalents

### 4.1 Kubernetes Deployment: ECK Operator

[FACT] The Elastic Cloud on Kubernetes (ECK) operator manages the full Elasticsearch cluster lifecycle. The default distribution of ECK comes with a basic license; autoscaling support is not available under the basic license.
URL: https://quesma.com/blog/elastic-pricing/
Date: 2025

[FACT] Elasticsearch on Kubernetes memory configuration requires allocating 50% of pod memory to the JVM heap, leaving the remainder for the Lucene filesystem cache.
URL: https://last9.io/blog/elasticsearch-kubernetes-deployment/
Date: 2025

[FACT] With ECK, hot-warm-cold cluster topologies can be deployed on Kubernetes and Index Lifecycle Management (ILM) policies used to move data between node tiers as it ages. ILM is described as "more mature and, for the most part, more feature-rich" than OpenSearch's Index State Management (ISM).
URL: https://sematext.com/blog/kubernetes-elasticsearch-autoscaling/
Date: 2025

### 4.2 AWS OpenSearch Service Pricing (2025)

[STATISTIC] AWS OpenSearch Service on-demand pricing examples: r6g.xlarge.search $0.335/hr; c6g.large.search master node $0.113/hr.
URL: https://cloudchipr.com/blog/aws-opensearch-pricing
Date: 2025

[STATISTIC] AWS OpenSearch Serverless pricing: compute at approximately $0.24/OCU-hour in us-east-1; storage approximately $0.02/GB-month.
URL: https://cloudchipr.com/blog/aws-opensearch-pricing
Date: 2025

[STATISTIC] AWS OpenSearch storage tiers: General Purpose SSD (GP2/GP3) ~$0.135/GB-month; UltraWarm $0.024/GB-month; Cold/Frozen storage uses S3 pricing.
URL: https://cloudchipr.com/blog/aws-opensearch-pricing
Date: 2025

[STATISTIC] AWS OpenSearch production cost example: 3 data nodes + 3 master nodes + UltraWarm storage ≈ $1,604.83/month.
URL: https://cloudchipr.com/blog/aws-opensearch-pricing
Date: 2025

### 4.3 Performance Comparison

[STATISTIC] In 2024–2025 benchmarks, Elasticsearch outperforms OpenSearch by 40–140% faster response times in complex query scenarios, with better resource utilization. For simpler log analytics at moderate scale, OpenSearch performance is described as "solid."
URL: https://www.netdata.cloud/academy/elasticsearch-vs-opensearch/
Date: 2025

### 4.4 Operational Difficulty Rating

| Capability Domain | On-Premises | Managed K8s (ECK) | Cloud-Native (OpenSearch Service) |
|---|---|---|---|
| Cluster deployment | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Manual ES config | ECK operator + Helm | Console/Terraform |
| | ES expert required | Platform + ES expertise | No ES expertise |
| | Est. FTE: 1.0+ | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 |
| Memory management | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Manual JVM tuning | 50% heap rule + PVC sizing | AWS-managed |
| | Est. FTE: 0.25 ongoing | Est. FTE: 0.25 ongoing | Est. FTE: 0.05 |
| Index lifecycle | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Manual ILM policies | ILM via K8s manifests | Managed lifecycle policies |
| Cluster scaling | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Manual node addition | Rolling update via operator | Console scaling |
| | Est. FTE: 0.5 per event | Est. FTE: 0.25 per event | Est. FTE: 0.05 per event |

---

## 5. Storage Considerations for Stateful K8s Workloads

### 5.1 CSI Drivers and Persistent Volumes

[FACT] The Container Storage Interface (CSI) is a standard that enables third-party storage providers to write and deploy plugins exposing arbitrary block and file storage systems to containerized workloads without modifying core Kubernetes code.
URL: https://portworx.com/knowledge-hub/a-complete-guide-to-kubernetes-csi/
Date: 2025

[FACT] CSI exposes snapshotting and cloning as first-class operations through the Kubernetes API, with snapshots capturing point-in-time states of a volume for backup, disaster recovery, and safe rollbacks.
URL: https://portworx.com/knowledge-hub/a-complete-guide-to-kubernetes-csi/
Date: 2025

[FACT] The Amazon EBS CSI driver manages the lifecycle of Amazon EBS volumes as Kubernetes Persistent Volume storage and is managed through the kubernetes-sigs/aws-ebs-csi-driver project.
URL: https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html
Date: 2025

[FACT] AKS (Azure Kubernetes Service) supports volume snapshots through the Azure Disk CSI driver, enabling point-in-time copies of persistent data without interrupting running applications.
URL: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots
Date: 2025

[FACT] In September 2025, Kubernetes released alpha support for a Changed Block Tracking (CBT) API in CSI drivers, enabling identification of changed blocks between snapshots and enabling "faster and more resource-efficient backup operations" without scanning entire volumes.
URL: https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/
Date: September 2025

### 5.2 Backup Tools for Stateful Kubernetes Workloads

[FACT] Velero v1.17.1 and Veeam Kasten 8.0.12 were both released in November 2025. Velero backs up cluster objects by querying the Kubernetes API and storing them as YAML files, while PV data is handled via cloud provider snapshots or CSI.
URL: https://veeamkasten.dev/why-kasten-over-velero
Date: November 2025

[FACT] Veeam Kasten (formerly Kasten K10) provides application-consistent snapshots through deep integration with relational and NoSQL databases, and a rich user interface. It is described as "the leading enterprise grade data management platform for Kubernetes."
URL: https://veeamkasten.dev/why-kasten-over-velero
Date: 2025

[FACT] Veeam Kasten supports granular table-level restore for PostgreSQL databases, which Velero does not natively support.
URL: https://veeamkasten.dev/postgres-kasten-granular-table-restore
Date: 2025

### 5.3 Storage Cost Drivers

[FACT] Storage costs on Kubernetes "can accumulate rapidly in cloud environments, with persistent volumes, especially those with premium storage classes, potentially being a significant cost that increases as application data grows."
URL: https://www.finout.io/blog/top-18-kubernetes-cost-optimization-strategies-in-2026
Date: 2025

[FACT] Optimizing storage for stateful Kubernetes workloads requires coordination between infrastructure and application teams, as "data management decisions directly impact both performance and spending."
URL: https://sedai.io/blog/a-guide-to-kubernetes-capacity-planning-and-optimization
Date: 2025

---

## 6. Data Gravity: When Workloads Resist Containerization

### 6.1 Fundamental Challenges

[FACT] Kubernetes was not originally designed for stateful applications. Its original design philosophy treats "applications meant to be elastic cattle, not fragile pets," with pods that "could be killed, restarted and rescheduled at will."
URL: https://thenewstack.io/stateful-workloads-on-kubernetes-with-container-attached-storage/
Date: 2025

[FACT] Application-specific day-2 operational tasks — including backup, snapshot, failover, patching, and index column operations — "can't be handled natively because every database will do things slightly differently," requiring database-specific operator implementations.
URL: https://blog.palark.com/stateful-in-kubernetes-and-operators/
Date: 2025

[FACT] Messaging and database workloads that "prefer local flash storage to achieve low latency" create a data gravity problem: data persists to nodes, "making it hard to move containers between worker nodes."
URL: https://thenewstack.io/stateful-workloads-on-kubernetes-are-a-thing-but-there-is-a-twist/
Date: 2025

### 6.2 When to Use K8s-Native vs Managed Data Services

The following guidance is drawn from operational patterns observed across practitioner sources (2025):

**Use Kubernetes-native data services when:**
- Multi-cloud portability is required and vendor lock-in must be avoided
- Custom PostgreSQL extensions (TimescaleDB, Citus, custom libraries) are necessary
- Redis Search and Query capabilities (post-Redis 7.2 fork) are required
- On-premises and cloud deployment must use identical tooling
- Regulatory requirements mandate data residency control at the infrastructure layer

**Use managed cloud data services when:**
- The engineering team lacks dedicated database or platform expertise
- RTO requirements are under 60 seconds (Aurora) or 120 seconds (RDS), with minimal configuration
- The workload is entirely within a single cloud provider's ecosystem
- Operational overhead reduction is the primary goal
- Extension requirements are satisfied by the managed service's approved list

[FACT] The State of Production Kubernetes 2025 report (Spectro Cloud, 455 respondents, May 2025) found that 88% of organizations reported year-on-year increases in total Kubernetes TCO, and cost overtook skills and security as the number-one challenge at 42%.
URL: https://www.businesswire.com/news/home/20250804240622/en/Spectro-Clouds-2025-State-of-Production-Kubernetes-Report-Finds-AI-Driving-Growth-as-Cost-Pressures-Bite
Date: August 2025

---

## 7. Operational Gap Analysis

### 7.1 What Remains Harder on Managed K8s (Even With Good Operators)

[FACT] The operational gap in Kubernetes stateful workloads is identified as: backup workflows "often cobbled together with multiple tools and scripts," migration of stateful applications between clusters or regions as "error-prone and time-consuming," and limited visibility into volume performance or reliability for developers.
URL: https://devtron.ai/blog/kubernetes-day-two-operations-the-real-challenge/
Date: 2025

[QUOTE] "We spent six months migrating. We've spent two years learning how to actually run the damn thing with stability in production." — Infrastructure lead (quoted in Devtron Day-2 Operations article)
URL: https://devtron.ai/blog/kubernetes-day-two-operations-the-real-challenge/
Date: 2025

[FACT] Kubernetes platform teams face non-linear scaling challenges: "3 clusters with 10 engineers = manageable; 30 clusters with 100 engineers = exponentially harder."
URL: https://devtron.ai/blog/kubernetes-day-two-operations-the-real-challenge/
Date: 2025

[FACT] SUSE identifies zero-downtime Kubernetes upgrade execution as requiring rare, highly specialized skills, with "most teams understaffed, overworked, and one bad deploy away from a very long night."
URL: https://www.suse.com/c/untangling-kubernetes-the-steep-climb-of-deployment-and-day-2-operations/
Date: 2025

### 7.2 Consolidated Operational Gap Summary

| Domain | Managed K8s Gap vs Cloud-Native | Remaining Risk |
|---|---|---|
| Major DB upgrades | Still requires maintenance windows and operator expertise | Data loss on failed upgrade |
| Cross-cluster migration | No native tooling; Velero/Kasten required | Extended RTO, data inconsistency |
| Storage performance tuning | Must benchmark and configure CSI + storage class | I/O bottleneck at scale |
| Kafka partition rebalancing | Manual or third-party (Cruise Control) | Uneven load, broker failure risk |
| Elasticsearch JVM tuning | Must configure per-pod memory allocation | OOMKill, performance degradation |
| Backup consistency | Application-consistent backup requires Kasten or custom hooks | Data corruption on restore |
| Compliance auditing | No native audit log integration with cloud services | Manual log pipeline required |
| Cost visibility | K8s storage + compute costs opaque without dedicated tooling | Cost overruns undetected |

### 7.3 FTE Operational Requirement Summary

Assumptions: Mid-size ISV, 50 enterprise customers, 3 managed K8s clusters across 2 cloud providers, standard HA configurations for each data service.

| Data Service | Cloud-Native FTE | Managed K8s FTE | Delta |
|---|---|---|---|
| PostgreSQL (primary DB) | 0.1–0.25 FTE | 0.25–0.5 FTE | +0.15–0.25 FTE |
| Kafka (event streaming) | 0.25–0.5 FTE | 0.5–1.0 FTE | +0.25–0.5 FTE |
| Redis (caching) | 0.05–0.1 FTE | 0.1–0.25 FTE | +0.05–0.15 FTE |
| OpenSearch (search/log) | 0.1–0.25 FTE | 0.25–0.5 FTE | +0.15–0.25 FTE |
| Backup / DR tooling | 0.05 FTE | 0.25–0.5 FTE | +0.2–0.45 FTE |
| **Total** | **0.55–1.1 FTE** | **1.35–2.75 FTE** | **+0.8–1.65 FTE** |

[UNVERIFIED] The FTE delta estimates above (0.8–1.65 FTE) are triangulated from the PostgreSQL operational time data from CertVanta (40–60 hr/month for self-managed vs 10–15 for managed), the Kafka staffing data from AutoMQ, and general platform engineering benchmarks. No single Tier 1 or Tier 2 source directly quantifies Managed K8s data service staffing as a category.

---

## 8. Cost Comparison Summary

### 8.1 Kafka: Direct Cost Comparison at Scale

| Option | Infrastructure | Operational Staff | Monthly Total (est.) |
|---|---|---|---|
| MSK (3× m5.large, 1 TB storage) | $566 | ~0.25 FTE ($2,500) | ~$3,066 |
| MSK Serverless (50 partitions, 500 GB) | $746 | ~0.1 FTE ($1,000) | ~$1,746 |
| Strimzi on EKS (3× m5.large EC2 + EBS) | ~$400 | ~0.5–1.0 FTE ($5,000–10,000) | ~$5,400–$10,400 |
| Confluent Cloud (Standard) | ~$540 (0.75 eCKU) | ~0.1 FTE ($1,000) | ~$1,540 |

Note: EKS control plane costs (~$144/month) are shared infrastructure and excluded from per-service comparison. FTE costs assumed at $100/hr, 50% allocation to Kafka operations for Strimzi.

[STATISTIC] Google Cloud Managed Kafka pricing: $1,100/month at 10 MiB/s bandwidth; $11,000/month at 100 MiB/s bandwidth.
URL: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons
Date: 2025

### 8.2 PostgreSQL: Direct Cost Comparison

| Option | Infrastructure | Labor (monthly) | Total |
|---|---|---|---|
| AWS Aurora (100 GB, Multi-AZ) | $800–$1,200 | ~$1,000 (10 hr) | ~$1,800–$2,200 |
| AWS RDS (100 GB, Multi-AZ) | $450–$650 | ~$1,500 (15 hr) | ~$1,950–$2,150 |
| K8s/EC2 self-managed (100 GB) | $200–$400 | ~$4,000–$6,000 (40–60 hr) | ~$4,200–$6,400 |
| CloudNativePG on EKS | $200–$400 + EKS share | ~$2,500–$5,000 (25–50 hr) | ~$2,700–$5,400 |

Source for infrastructure costs: [CertVanta PostgreSQL Comparison](https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql), December 2025. CloudNativePG operational hours estimated at 60–70% of raw EC2 self-managed, based on operator automation of failover, backup, and configuration management.

---

## Key Takeaways

- **Operator maturity is real, but operational gap persists.** CloudNativePG (CNCF Sandbox, January 2025), Strimzi KRaft, and Redis Operator deployments have reached feature parity with managed services on Day 1 capabilities. The gap lies in Day 2 operations: backup consistency, cross-cluster migration, Kafka partition rebalancing, and Elasticsearch JVM tuning remain harder on K8s and require specialist expertise not needed with managed services.

- **The labor cost is the dominant cost driver.** Infrastructure savings from K8s-native data services are real (20–50% lower compute for equivalent workloads) but are routinely erased by the 0.8–1.65 additional FTE required. At $200,000/FTE all-in, this represents $160,000–$330,000 annually — well above the compute savings at mid-scale deployments.

- **Strimzi's ZooKeeper removal is a forcing function.** Strimzi 0.46+ requires KRaft migration, and the migration procedure requires manual configuration and multiple rolling updates. ISVs on older Strimzi versions must plan a migration sprint or evaluate MSK, which abstracts this entirely.

- **K8s-native data services are the right choice when lock-in costs exceed operational costs.** The primary legitimate use case is multi-cloud portability — particularly for ISVs whose customers require on-premises or sovereign deployments alongside cloud deployments and need identical tooling. The extension flexibility of K8s PostgreSQL (custom extensions, full `postgresql.conf` control) is a secondary but real differentiator for analytics-heavy ISV applications.

- **Data gravity makes this choice largely irreversible.** Once a large stateful workload (Kafka topic data, PostgreSQL primary, Elasticsearch index corpus) accumulates in a deployment model, migration costs — in engineering time, downtime risk, and cross-cloud data transfer fees — are high. ISVs should make the Managed K8s vs Cloud-Native data service decision explicitly at architecture inception, not retroactively.

---

## Related — Out of Scope

- K8s platform selection (EKS vs AKS vs GKE) — See F52
- Kubernetes Operator patterns in general — See F54
- On-premises database deployments (PostgreSQL bare metal, Kafka on-prem) — See F41–F42
- Network storage class performance benchmarking (Longhorn, Portworx, Rook/Ceph) — potentially relevant to F53

---

## Sources

1. [CloudNativePG in 2025: CNCF Sandbox, PostgreSQL 18, and a new era for extensions](https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/) — Gabriele Bartolini, December 2025
2. [CloudNativePG CNCF Project Page](https://www.cncf.io/projects/cloudnativepg/) — CNCF, 2025
3. [CloudNativePG Storage Documentation v1.20](https://cloudnative-pg.io/documentation/1.20/storage/) — CloudNativePG, 2025
4. [CloudNativePG Backup Documentation v1.20](https://cloudnative-pg.io/documentation/1.20/backup/) — CloudNativePG, 2025
5. [CloudNativePG Recovery Documentation v1.20](https://cloudnative-pg.io/documentation/1.20/recovery/) — CloudNativePG, 2025
6. [Aurora vs RDS PostgreSQL vs EC2: Costs, Performance & Multi-Region Compared (2025)](https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql) — CertVanta, December 2025
7. [Reliable PostgreSQL Backup and Recovery with CloudNativePG and GCS](https://medium.com/@valerykretinin/reliable-postgresql-backup-and-recovery-with-cloudnativepg-and-gcs-e44ad0de13a2) — Medium, 2025
8. [Strimzi KRaft Adoption and ZooKeeper Removal](https://strimzi.io/kraft/) — Strimzi, 2025
9. [Strimzi KRaft Migration Blog](https://strimzi.io/blog/2024/03/22/strimzi-kraft-migration/) — Strimzi, March 2024
10. [Strimzi KRaft Upgrades and Downgrades Proposal](https://github.com/strimzi/proposals/blob/main/061-kraft-upgrades-and-downgrades.md) — Strimzi GitHub, 2025
11. [Apache Kafka Pricing Guide: Open Source vs Managed Services](https://airbyte.com/data-engineering-resources/apache-kafka-pricing) — Airbyte, 2025
12. [Self-Hosted Kafka vs Fully Managed Kafka: Pros & Cons](https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons) — AutoMQ, 2025
13. [Amazon MSK Graviton3 Throughput and Cost Improvements](https://aws.amazon.com/blogs/big-data/amazon-msk-now-provides-up-to-29-more-throughput-and-up-to-24-lower-costs-with-aws-graviton3-support/) — AWS, 2025
14. [Amazon MSK Pricing](https://aws.amazon.com/msk/pricing/) — AWS, 2025
15. [Redis vs ElastiCache Cost Effectiveness](https://redis.io/blog/redis-vs-elasticache-which-is-more-cost-effective/) — Redis, 2025
16. [Redis vs ElastiCache Feature Comparison](https://redis.io/compare/elasticache/) — Redis, 2025
17. [ElastiCache vs Redis Comprehensive Comparison](https://www.prosperops.com/blog/elasticache-vs-redis/) — ProsperOps, 2025
18. [AWS ElastiCache Migrate to Valkey](https://www.pump.co/blog/aws-migrate-redis-to-valkey) — Pump, 2025
19. [Redis on Kubernetes Deployment Guide](https://www.plural.sh/blog/redis-cluster-on-kubernetes/) — Plural, 2025
20. [Redis vs ElastiCache Networking and VPC](https://redis.io/blog/redis-vs-elasticache/) — Redis, 2025
21. [Spotahome Redis Operator GitHub](https://github.com/spotahome/redis-operator) — Spotahome, 2025
22. [Bitnami Redis Chart README](https://github.com/bitnami/charts/blob/main/bitnami/redis/README.md) — Bitnami, 2025
23. [How to Run Elasticsearch on Kubernetes](https://last9.io/blog/elasticsearch-kubernetes-deployment/) — Last9, 2025
24. [Autoscaling Elasticsearch for Logs with a Kubernetes Operator](https://sematext.com/blog/kubernetes-elasticsearch-autoscaling/) — Sematext, 2025
25. [AWS OpenSearch Pricing Deep Dive](https://cloudchipr.com/blog/aws-opensearch-pricing) — CloudChipr, 2025
26. [OpenSearch vs Elasticsearch 2025](https://www.netdata.cloud/academy/elasticsearch-vs-opensearch/) — Netdata, 2025
27. [Elasticsearch Pricing Understanding](https://quesma.com/blog/elastic-pricing/) — Quesma, 2025
28. [Kubernetes CSI Complete Guide](https://portworx.com/knowledge-hub/a-complete-guide-to-kubernetes-csi/) — Portworx, 2025
29. [CSI Changed Block Tracking API Alpha](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/) — Kubernetes, September 2025
30. [Amazon EBS CSI Driver for EKS](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) — AWS Documentation, 2025
31. [GKE Volume Snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots) — Google Cloud, 2025
32. [Why Kasten Over Velero](https://veeamkasten.dev/why-kasten-over-velero) — Veeam Kasten, November 2025
33. [Postgres Kasten Granular Table Restore](https://veeamkasten.dev/postgres-kasten-granular-table-restore) — Veeam Kasten, 2025
34. [Stateful Workloads on Kubernetes with Container Attached Storage](https://thenewstack.io/stateful-workloads-on-kubernetes-with-container-attached-storage/) — The New Stack, 2025
35. [Stateful Apps in Kubernetes: Operators](https://blog.palark.com/stateful-in-kubernetes-and-operators/) — Palark, 2025
36. [Kubernetes Day 2 Operations: The Real Challenge](https://devtron.ai/blog/kubernetes-day-two-operations-the-real-challenge/) — Devtron, 2025
37. [Untangling Kubernetes: Day 2 Operations](https://www.suse.com/c/untangling-kubernetes-the-steep-climb-of-deployment-and-day-2-operations/) — SUSE, 2025
38. [State of Production Kubernetes 2025 Press Release](https://www.businesswire.com/news/home/20250804240622/en/Spectro-Clouds-2025-State-of-Production-Kubernetes-Report-Finds-AI-Driving-Growth-as-Cost-Pressures-Bite) — BusinessWire / Spectro Cloud, August 2025
39. [Kubernetes Storage Solutions 2025](https://www.simplyblock.io/blog/5-storage-solutions-for-kubernetes-in-2025/) — Simplyblock, 2025
40. [Choosing a Kubernetes PostgreSQL Operator](https://www.simplyblock.io/blog/choosing-a-kubernetes-postgres-operator/) — Simplyblock, 2025
41. [Kubernetes Cost Optimization Strategies 2026](https://www.finout.io/blog/top-18-kubernetes-cost-optimization-strategies-in-2026) — Finout, 2025
42. [Google Cloud Managed Kafka Pricing](https://www.automq.com/blog/managed-apache-kafka-as-service) — AutoMQ, 2025
