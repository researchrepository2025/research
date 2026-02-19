# F09: AWS Data Services
**Agent ID:** F09 | **Scope:** AWS managed data services — databases, caching, search, storage, file systems

---

## Executive Summary

AWS offers the broadest portfolio of managed data services in the cloud, spanning relational databases, NoSQL, caching, search, data warehousing, object storage, and file systems. For ISVs evaluating deployment models, AWS managed data services systematically eliminate the most operationally intensive tasks — patching, hardware provisioning, replication setup, backup orchestration, and failover management — tasks that require dedicated database administrator (DBA) staff in self-hosted or on-premises environments. Amazon RDS with Multi-AZ delivers automatic failover in as few as 35 seconds with a 99.95% uptime SLA, compared to the 99.5% SLA for single-AZ configurations, while DynamoDB Global Tables raise the availability commitment to 99.999% for multi-Region deployments. Across the full AWS data services portfolio, the primary ISV value proposition is operational burden offload: the cloud provider assumes responsibility for undifferentiated heavy lifting — patching, replication, storage scaling, and hardware failures — freeing engineering teams to focus on application differentiation.

---

## 1. Amazon RDS: Managed Relational Database Service

### 1.1 Core Service Overview

Amazon RDS is a fully managed relational database service supporting PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2. The service [automates database provisioning, software patching, automatic backups, storage scaling, and failover handling](https://aws.amazon.com/rds/) without requiring DBA intervention for these routine operations.

### 1.2 Multi-AZ High Availability

RDS Multi-AZ provides synchronous replication of the primary database to one or two standby instances in separate Availability Zones.

[FACT] Amazon RDS Multi-AZ with one standby delivers "automatic database failover that completes as quickly as 60 seconds with zero data loss" — [AWS, Amazon RDS Multi-AZ Features Page](https://aws.amazon.com/rds/features/multi-az/)

[FACT] Amazon RDS Multi-AZ DB clusters with two readable standbys (available for PostgreSQL and MySQL) deliver automatic failover "typically under 35 seconds" — [AWS, Amazon RDS Multi-AZ Features Page](https://aws.amazon.com/rds/features/multi-az/)

[STATISTIC] RDS Multi-AZ delivers a **99.95% monthly uptime SLA**, compared to **99.5%** for Single-AZ deployments — [AWS RDS SLA](https://aws.amazon.com/rds/sla/)

[FACT] During Multi-AZ deployments, backups are taken from the standby instance, so there is no I/O suspension on the primary database during backup windows — [AWS RDS Automated Backups Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

[FACT] The two-standby Multi-AZ configuration delivers "up to 2x faster transaction commit latency compared to single-standby deployments" — [AWS, Amazon RDS Multi-AZ Features Page](https://aws.amazon.com/rds/features/multi-az/)

### 1.3 Read Replicas

[FACT] Amazon RDS for MySQL, MariaDB, and PostgreSQL support up to **15 read replicas** for a given source DB instance — [AWS RDS Read Replicas](https://aws.amazon.com/rds/features/read-replicas/)

[FACT] RDS uses asynchronous replication to keep read replicas current with the primary instance, updated on every change to the primary DB instance — [AWS RDS Read Replicas Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

### 1.4 Automated Backups and Point-in-Time Recovery

[FACT] RDS automated backup retention can be configured from **0 to 35 days** (0 disables automated backups; Multi-AZ DB clusters require a minimum of 1 day) — [AWS RDS Backup Retention Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html)

[FACT] RDS supports point-in-time recovery "to any second during your retention period, up to the Latest Restorable Time," which is "typically within the last five minutes" — [AWS RDS Automated Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

[FACT] RDS uploads transaction logs to Amazon S3 every **5 minutes**, enabling sub-5-minute RPO for point-in-time recovery — [AWS RDS Automated Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

[FACT] The default backup retention period when creating an instance via the AWS console is **7 days**; via API or CLI the default is **1 day** — [AWS RDS Backup Retention Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html)

### 1.5 Aurora Serverless v2

Amazon Aurora Serverless v2 is an on-demand auto-scaling configuration for Aurora (MySQL-compatible and PostgreSQL-compatible editions).

[FACT] Aurora Serverless v2 "scales instantly to hundreds of thousands of transactions in a fraction of a second" using fine-grained capacity increments — [AWS Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/)

[FACT] Aurora Serverless v2 scales in increments as small as **0.5 ACUs** (Aurora Capacity Units), with 1 ACU providing approximately 2 GB of memory — [AWS Aurora Serverless v2 Performance Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.setting-capacity.html)

[FACT] Aurora Serverless v2 introduced **scale-to-zero** capability (auto-pause feature), allowing idle databases to stop incurring compute charges — [AWS Blog: Introducing scaling to 0 with Aurora Serverless v2](https://aws.amazon.com/blogs/database/introducing-scaling-to-0-capacity-with-amazon-aurora-serverless-v2/)

[FACT] AWS claims potential savings of "up to 90% of your database cost compared to the cost of provisioning capacity for peak load" with Aurora Serverless v2 — [AWS Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/)

[FACT] Aurora Serverless v2 "reduces the administrative effort for planning, resizing DB instances in a cluster, simplifying consistent capacity management and reducing operational overhead" — [AWS Aurora Serverless v2 How It Works](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html)

### 1.6 RDS Analyst Recognition

[FACT] Gartner awarded Amazon RDS an **industry-best score of 95** in its Solution Scorecard, including 100% of required criteria for an operational database platform as a service (dbPaaS) — [AWS Database Blog: Gartner recognizes Amazon RDS](https://aws.amazon.com/blogs/database/gartner-recognizes-amazon-rds-in-new-report/)

---

## 2. Amazon DynamoDB: Serverless NoSQL Database

### 2.1 Core Service Overview

Amazon DynamoDB is a fully managed, serverless NoSQL key-value and document database designed for single-digit millisecond latency at any scale. The service automatically handles infrastructure management, scaling, and high availability without user configuration of servers, clusters, or replication topology.

### 2.2 Auto-Scaling and Capacity Modes

DynamoDB offers two capacity modes:

**On-Demand Mode:** Pay-per-request pricing with automatic scaling, billed per read or write request consumed, with no capacity planning required.

[STATISTIC] Effective November 1, 2024, DynamoDB reduced prices for on-demand throughput by **50%** and global tables by **up to 67%** — [AWS Blog: DynamoDB lowers pricing for on-demand throughput and global tables](https://aws.amazon.com/blogs/database/new-amazon-dynamodb-lowers-pricing-for-on-demand-throughput-and-global-tables/)

[STATISTIC] On-demand mode pricing: **$0.25 per million write request units** (1 WRU = 1 KB write) — [AWS DynamoDB On-Demand Pricing](https://aws.amazon.com/dynamodb/pricing/on-demand/)

**Provisioned Mode:** Users specify read/write capacity units per second; charged on hourly reserved capacity. DynamoDB auto-scaling can dynamically adjust provisioned capacity based on utilization targets.

### 2.3 Global Tables

[FACT] DynamoDB Global Tables provides "active-active replication across regions" with "up to 99.999% availability" — [AWS DynamoDB Global Tables](https://aws.amazon.com/dynamodb/global-tables/)

[STATISTIC] Using Global Tables raises the DynamoDB SLA from **99.99%** (single-Region) to **99.999%** (multi-Region) — [AWS DynamoDB SLA](https://aws.amazon.com/dynamodb/sla/)

[FACT] Global Tables introduced multi-Region strong consistency (MRSC) in **June 2025**, which "synchronously replicates item changes to at least one other Region before the write operation returns a successful response" — [AWS DynamoDB Global Tables Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.html)

[FACT] MRSC provides an **RPO of zero**; multi-Region eventual consistency (MREC) provides RPO and RTO "measured in seconds" — [AWS DynamoDB Global Tables Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.html)

[FACT] Global Tables conflict resolution in MREC mode uses a **last-writer-wins** mechanism based on write operation timestamps — [AWS DynamoDB Global Tables How It Works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)

[FACT] Local read/write operations on DynamoDB Global Tables achieve **single-digit millisecond latency** regardless of global scale — [AWS DynamoDB Global Tables](https://aws.amazon.com/dynamodb/global-tables/)

### 2.4 DAX: DynamoDB Accelerator

[FACT] DAX is a DynamoDB-compatible in-memory caching service that delivers "up to a 10x performance improvement" for read-heavy and bursty workloads — [AWS DynamoDB FAQs](https://aws.amazon.com/dynamodb/faqs/)

[STATISTIC] A three-node t2.small DAX cluster costs **$0.12 per hour** ($0.04 × 3 nodes), with no long-term commitments required — [Cloud Ex Machina: DynamoDB Pricing Survival Manual](https://www.cloudexmachina.io/blog/dynamodb-pricing)

---

## 3. Amazon ElastiCache: Managed In-Memory Caching

### 3.1 Core Service Overview

Amazon ElastiCache is a fully managed in-memory data store and cache service supporting Valkey (a Redis OSS fork), Redis OSS, and Memcached. The service eliminates operational tasks including cluster provisioning, patching, monitoring, node replacement, and replication configuration.

### 3.2 Cluster Mode, Replication, and Failover

[FACT] ElastiCache replication groups allow grouping of 2 to 6 nodes, with 1 to 5 read-only replica nodes containing replicated data of the group's single read/write primary node — [AWS ElastiCache Replication Documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.html)

[FACT] "Typically, start to finish, automatic failover events complete within **six minutes**" for ElastiCache — [AWS ElastiCache Auto Failover Documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)

[FACT] ElastiCache automatic failover "flips the DNS record for your cache node to point at the read replica, which is in turn promoted to become the new primary" with no manual intervention — [iCompaas: ElastiCache Auto Failover](https://support.icompaas.com/support/solutions/articles/62000233598-ensure-elasticache-redis-clusters-have-automatic-failover-enabled)

[FACT] After failover, "available read replicas automatically resume replication once failover has completed, acquiring updates from the newly promoted replica" — [AWS ElastiCache Replication Documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.html)

### 3.3 Valkey: Cost Reduction and New Capabilities

In 2024, AWS introduced ElastiCache for Valkey, a fork of Redis OSS 7.2. Valkey is now the recommended default for new ElastiCache deployments.

[STATISTIC] ElastiCache Serverless for Valkey is priced **33% lower** than ElastiCache Serverless for Redis OSS; node-based clusters are priced **20% lower** — [AWS Blog: Reduce ElastiCache costs by up to 60% with Valkey](https://aws.amazon.com/blogs/database/reduce-your-amazon-elasticache-costs-by-up-to-60-with-valkey-and-cudos/)

[STATISTIC] MemoryDB for Valkey is priced **30% lower** than MemoryDB on Redis — [AWS Blog: Reduce ElastiCache costs by up to 60% with Valkey](https://aws.amazon.com/blogs/database/reduce-your-amazon-elasticache-costs-by-up-to-60-with-valkey-and-cudos/)

[FACT] Upgrading to ElastiCache for Valkey achieves "up to 40% memory reduction, 230% scaling improvements" — [AWS Blog: Reduce ElastiCache costs by up to 60% with Valkey](https://aws.amazon.com/blogs/database/reduce-your-amazon-elasticache-costs-by-up-to-60-with-valkey-and-cudos/)

[FACT] ElastiCache for Valkey can be started for "as low as $6/month" in Serverless mode — [AWS ElastiCache Pricing](https://aws.amazon.com/elasticache/pricing/)

[FACT] AWS announced in 2025 that ElastiCache connectors allow Valkey to serve as "short-term agentic memory through frameworks such as Mem0, LMCache, and LangGraph" — [AWS ElastiCache re:Invent 2025 Recap](https://aws.amazon.com/blogs/database/amazon-elasticache-reinvent-2025-recap/)

[FACT] ElastiCache for Valkey delivers "lowest latency vector search with highest throughput and best price-performance at 95% recall rate among popular vector databases on AWS" — [AWS ElastiCache re:Invent 2025 Recap](https://aws.amazon.com/blogs/database/amazon-elasticache-reinvent-2025-recap/)

---

## 4. Amazon OpenSearch Service: Managed Search and Analytics

### 4.1 Core Service Overview

Amazon OpenSearch Service is a fully managed service for deploying, operating, and scaling OpenSearch and legacy Elasticsearch clusters. The service handles cluster provisioning, software patches, node monitoring and replacement, storage scaling, and cross-node replication.

[FACT] Amazon OpenSearch Service supports deployment and operation of "the latest versions of OpenSearch and 19 versions of ALv2 Elasticsearch (7.10 and earlier)" — [AWS OpenSearch Features](https://aws.amazon.com/opensearch-service/features/)

### 4.2 UltraWarm Storage Tier

UltraWarm is a fully managed warm storage tier that uses Amazon S3 as backing storage with an intelligent caching layer, rather than EBS volumes attached to hot data nodes.

[STATISTIC] UltraWarm reduces cost per GB by **nearly 90%** compared to the hot storage tier — [AWS OpenSearch UltraWarm Documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ultrawarm.html)

[STATISTIC] Cold storage (detached indexes, queryable on-demand) is priced at **$0.024 per GB per month** — [AWS OpenSearch Multi-tier Storage Documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/multi-tier-storage.html)

[FACT] UltraWarm is "compatible with OpenSearch, Elasticsearch (until version 7.10), OpenSearch Dashboards, and Kibana (until version 7.10)" — [AWS OpenSearch UltraWarm Documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ultrawarm.html)

[FACT] The three-tier architecture (hot / UltraWarm / cold) allows retaining "up to 3 PB of data in a single Amazon OpenSearch Service cluster while reducing cost per GB by nearly 90% compared to the hot storage tier" — [AWS OpenSearch Serverless](https://aws.amazon.com/opensearch-service/features/serverless/)

[FACT] In December 2025, AWS announced a new **writable warm tier** for OpenSearch, available on OpenSearch 3.3 and above — [AWS: Amazon OpenSearch Service now offers a new multi-tier storage](https://aws.amazon.com/about-aws/whats-new/2025/12/writeable-warm-tier-opensearch-optimized-instances/)

### 4.3 OpenSearch Serverless

Amazon OpenSearch Serverless eliminates the need to provision, configure, or tune OpenSearch clusters.

[FACT] OpenSearch Serverless enables developers to "run petabyte-scale workloads without configuring, managing, and scaling OpenSearch clusters" — [AWS OpenSearch Serverless Features](https://aws.amazon.com/opensearch-service/features/serverless/)

[FACT] OpenSearch Serverless "automatically provisions and continually adjusts to get fast data ingestion rates" while scaling down during low-demand periods — [AWS OpenSearch Serverless Features](https://aws.amazon.com/opensearch-service/features/serverless/)

[FACT] OpenSearch Serverless supports vector embeddings for "generative AI applications with simple, scalable, and high-performing vector search" — [AWS OpenSearch Serverless Features](https://aws.amazon.com/opensearch-service/features/serverless/)

[FACT] OpenSearch Serverless delivers "millisecond response times comparable to standard OpenSearch Service" — [AWS OpenSearch Serverless Documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html)

---

## 5. Amazon Redshift: Managed Data Warehouse

### 5.1 Core Service Overview

Amazon Redshift is a fully managed, petabyte-scale data warehouse service. It eliminates the operational overhead of database software installation, configuration, patching, and hardware management for analytical workloads.

### 5.2 Redshift Serverless

[FACT] Amazon Redshift Serverless "automatically and proactively provisions and scales data warehouse capacity" using AI-driven optimization — [AWS Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/)

[FACT] Redshift Serverless measures capacity in Redshift Processing Units (RPUs), where "each RPU provides 16 GB of memory" — [AWS Redshift Serverless What It Is](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html)

[STATISTIC] Redshift Serverless base capacity is configurable from **4 to 1,024 RPUs** — [AWS Redshift Serverless Billing](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-billing.html)

[STATISTIC] Redshift Serverless pricing is **$0.375 per RPU-hour**, billed per second with a 60-second minimum — [AWS Redshift Pricing](https://aws.amazon.com/redshift/pricing/)

[STATISTIC] Serverless Reservations reduce Redshift Serverless compute costs by **up to 24%** — [AWS Blog: Save on Redshift Serverless with Reservations](https://aws.amazon.com/blogs/big-data/save-up-to-24-on-amazon-redshift-serverless-compute-costs-with-reservations/)

[FACT] Redshift Serverless AI-driven scaling "learns customer workload patterns across key dimensions, such as concurrent queries, query complexity, influx of data volume, and ETL patterns" — [AWS Redshift](https://aws.amazon.com/redshift/)

### 5.3 ML Integration

[FACT] Redshift ML allows users to "build, train, and deploy machine learning models using simple SQL commands" by integrating directly with Amazon SageMaker — [AWS Redshift ML](https://aws.amazon.com/redshift/features/redshift-ml/)

[FACT] Redshift ML provides **two free CREATE MODEL requests per month for the first two months**, each handling up to 100,000 cells; beyond the free tier, pricing starts at **$20 per million cells** — [Navigating Amazon Redshift Serverless Pricing 2025](https://www.oreateai.com/blog/navigating-amazon-redshift-serverless-pricing-understanding-rpus-and-costs-in-2025/4000f61af1460fbe4709691b4f1bf303)

### 5.4 Zero-ETL Integrations

[FACT] Redshift features zero-ETL integrations that "seamlessly move transactional data from databases like Amazon Aurora, RDS, and DynamoDB into Redshift without performance impact" — [AWS Redshift Zero-ETL Integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html)

[FACT] Redshift can ingest high-volume real-time data from Amazon Kinesis and Amazon MSK through native streaming integration — [AWS: Get maximum value from Amazon Redshift](https://www.amazonaws.cn/en/blog-selection/get-maximum-value-out-of-your-cloud-data-warehouse-with-amazon-redshift/)

[FACT] Amazon Q in Redshift enables "SQL authoring through natural language" — [AWS Redshift](https://aws.amazon.com/redshift/)

---

## 6. Amazon S3: Object Storage

### 6.1 Core Service Overview

Amazon S3 is the foundational object storage service in AWS, offering unlimited storage capacity with no provisioning required. S3 stores data redundantly across a minimum of three Availability Zones for all standard storage classes.

### 6.2 Durability and Availability SLA

[STATISTIC] Amazon S3 is designed to provide **99.999999999% (eleven nines) data durability** — [AWS S3 Data Protection Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)

[STATISTIC] S3 Standard storage class is designed for **99.99% availability**; S3 Standard-IA, Intelligent-Tiering, and Glacier Instant Retrieval are designed for **99.9% availability** — [AWS S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)

[FACT] S3 stores data "redundantly across a minimum of 3 Availability Zones by default" — [AWS S3 FAQs](https://aws.amazon.com/s3/faqs/)

### 6.3 Storage Classes and Pricing

| Storage Class | Use Case | Price (US East, per GB/month) |
|---|---|---|
| S3 Standard | Frequently accessed data | $0.023 |
| S3 Standard-IA | Infrequent access, immediate retrieval | Lower than Standard |
| S3 Intelligent-Tiering | Unknown or changing access patterns | Monitoring fee + tiered storage |
| S3 Glacier Instant Retrieval | Archive, millisecond retrieval | $0.004 |
| S3 Glacier Flexible Retrieval | Infrequent archive, hours retrieval | Lower than Instant Retrieval |
| S3 Glacier Deep Archive | Long-term archive, 12-hour retrieval | $0.00099 |

Source: [AWS S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/), [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/)

[STATISTIC] S3 Glacier Deep Archive at **$0.00099 per GB per month** represents a reduction from S3 Standard ($0.023) of **approximately 96%** — [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/)

### 6.4 Intelligent-Tiering

[FACT] S3 Intelligent-Tiering "automatically stores objects in three access tiers: one tier optimized for frequent access, a 40% lower-cost tier optimized for infrequent access, and a 68% lower-cost tier optimized for rarely accessed data" — [AWS S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)

[FACT] "There are no retrieval charges in S3 Intelligent-Tiering" — [AWS S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)

[STATISTIC] S3 Intelligent-Tiering with the Deep Archive Access tier activated can achieve "up to 95% in storage cost savings" for rarely accessed data — [AWS S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)

### 6.5 Lifecycle Policies and Versioning

[FACT] S3 Lifecycle configuration allows automatic transitioning of objects to less expensive storage classes or deletion; for example, "objects to the S3 Standard-IA storage class 30 days after creating them, or archive objects to the S3 Glacier Flexible Retrieval storage class one year after creating them" — [AWS S3 Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

[FACT] The `NoncurrentVersionTransition` lifecycle action allows lifecycle management of non-current object versions (prior versions retained after overwrite) to cheaper tiers — [AWS S3 Lifecycle Examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)

### 6.6 Event Notifications

[FACT] S3 supports the `s3:LifecycleTransition` event type to send notification "when an object is transitioned from one Amazon S3 storage class to another by an S3 Lifecycle configuration" — [AWS S3 Lifecycle Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configure-notification.html)

[FACT] S3 `LifecycleExpiration` event types send notifications "whenever Amazon S3 deletes an object based on your S3 Lifecycle configuration" — [AWS S3 Lifecycle Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configure-notification.html)

---

## 7. Amazon EFS and FSx: Managed File Systems

### 7.1 Amazon EFS: Elastic File System (NFS)

Amazon EFS provides fully managed NFS (NFSv4) file storage for use with EC2 instances, containers, and serverless compute. EFS file systems are distributed across Availability Zones automatically.

[FACT] Amazon EFS supports "secure access for thousands of connections for Amazon EC2 instances, as well as AWS container and serverless compute services" — [AWS EFS Features](https://aws.amazon.com/efs/features/)

[FACT] EFS uses NFS version 4 protocol and supports "traditional file permissions model, file locking, and hierarchical directory structure" — [Amazon EFS FAQs](https://www.amazonaws.cn/en/efs/faq/)

**EFS Throughput Modes:**

[FACT] EFS Elastic Throughput (the default mode) "automatically scales up or down to meet the needs of your workload activity" and is "ideal for spiky and unpredictable workloads with performance requirements that are difficult to forecast" — [AWS EFS Performance Documentation](https://docs.aws.amazon.com/efs/latest/ug/performance.html)

[FACT] EFS Provisioned Throughput allows specification of up to **1 GiB/second** of provisioned throughput for each file system — [AWS EFS Managing Throughput](https://docs.aws.amazon.com/efs/latest/ug/managing-throughput.html)

### 7.2 Amazon FSx: Specialized File Systems

Amazon FSx provides a family of managed file system services for specialized workload requirements: FSx for Windows File Server, FSx for Lustre, FSx for NetApp ONTAP, and FSx for OpenZFS.

[FACT] "Amazon FSx is for those who want the benefits of third-party file systems without their operational baggage" — [AWS: Help Me Choose an Amazon FSx File System](https://aws.amazon.com/fsx/when-to-choose-fsx/)

**FSx for Windows File Server:**

[FACT] FSx for Windows runs "Windows Server Message Block (SMB)-based file services" and is "compatible with any server application designed for on-premises Windows Server environments" — [AWS: EFS vs FSx for Windows vs FSx for Lustre](https://tutorialsdojo.com/amazon-efs-vs-amazon-fsx-for-windows-vs-amazon-fsx-for-lustre/)

**FSx for Lustre:**

[FACT] FSx for Lustre "provides the fastest storage performance for GPU instances in the cloud with up to terabytes per second of throughput, millions of IOPS, sub-millisecond latencies" — [AWS FSx for Lustre](https://aws.amazon.com/fsx/lustre/)

[STATISTIC] With Elastic Fabric Adapter (EFA) and NVIDIA GPUDirect Storage (GDS), FSx for Lustre achieves "up to **1,200 Gbps** throughput per client instance," representing "twelve times more throughput than previously" when using P5 GPU instances — [AWS Blog: FSx for Lustre unlocks full network bandwidth and GPU performance](https://aws.amazon.com/blogs/aws/amazon-fsx-for-lustre-unlocks-full-network-bandwidth-and-gpu-performance/)

[FACT] FSx for Lustre is integrated with Amazon S3: SageMaker ML training jobs can be "accelerated by eliminating the initial S3 download step" with jobs "started as soon as the FSx for Lustre file system is linked with the S3 bucket" — [AWS FSx for Lustre](https://aws.amazon.com/fsx/lustre/)

[STATISTIC] FSx for Lustre delivers "up to 34% better price performance compared to on-premises HDD file storage and up to 70% better price performance compared to other high-performance file systems in the cloud" — [AWS FSx for Lustre Features](https://aws.amazon.com/fsx/lustre/features/)

[FACT] The highest-performance FSx for Lustre PERSISTENT-1000 deployment type provides "up to 1000 MB/s per TiB storage capacity for disk throughput, and 2,600 MBps per TiB of storage capacity for network throughput" — [AWS FSx for Lustre FAQs](https://aws.amazon.com/fsx/lustre/faqs/)

---

## 8. Operational Burden Comparison

The following table applies the standardized Difficulty Rating Scale (1–5) to the operational profile of each AWS managed data service across the three ISV deployment models. Assumptions: mid-size ISV serving 50 enterprise customers, with a production-grade deployment per service.

| Service / Capability | On-Premises (Self-Hosted) | Managed K8s (Self-Operated) | Cloud-Native (AWS Managed) |
|---|---|---|---|
| **Relational DB (PostgreSQL/MySQL)** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | HW provisioning, OS patching, replication config, failover scripting, backup orchestration | Operator pattern (CloudNativePG), storage class tuning, manual HA setup | RDS automates patching, Multi-AZ failover, backups, scaling |
| | pg_auto_failover, Patroni, Barman | CloudNativePG, Velero | Amazon RDS, Aurora Serverless v2 |
| | Est. FTE: 1.5–2.0 (dedicated DBA) | Est. FTE: 0.75–1.0 | Est. FTE: 0.25–0.5 |
| **NoSQL / Key-Value** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Cassandra or MongoDB: ring management, compaction tuning, replication factor config | Kubernetes StatefulSets, PVCs, custom operator for scaling | DynamoDB: zero infrastructure management; auto-scaling, Global Tables, DAX caching all managed |
| | Cassandra, MongoDB Ops Manager | MongoDB Atlas Operator, StatefulSets | Amazon DynamoDB + DAX |
| | Est. FTE: 1.0–1.5 | Est. FTE: 0.5–0.75 | Est. FTE: 0.1 |
| **In-Memory Cache** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Redis Sentinel or Redis Cluster: topology management, failover scripting, AOF/RDB tuning | Redis Operator, PVCs for persistence, manual replication topology | ElastiCache: cluster mode, replication, automatic failover all managed |
| | Redis Sentinel, Redis Cluster | Redis Operator for K8s | Amazon ElastiCache (Valkey/Redis OSS) |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Search / Full-Text Index** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Elasticsearch self-hosted: JVM tuning, shard rebalancing, index lifecycle policies, upgrade coordination | ECK Operator, custom storage class, manual scaling | OpenSearch Service: cluster scaling, patching, storage tiers managed |
| | Elasticsearch, Solr | ECK (Elasticsearch on K8s) | Amazon OpenSearch Service / Serverless |
| | Est. FTE: 1.0–1.5 | Est. FTE: 0.5–0.75 | Est. FTE: 0.25 |
| **Data Warehouse** | Difficulty: 5/5 | Difficulty: 5/5 | Difficulty: 2/5 |
| | Self-hosted Greenplum or Vertica: MPP cluster management, vacuuming, storage expansion | Not recommended: MPP systems not designed for containers | Redshift Serverless: AI-driven scaling, zero-ETL integrations, SQL ML |
| | Greenplum, Vertica, ClickHouse | N/A (impractical at scale) | Amazon Redshift / Redshift Serverless |
| | Est. FTE: 2.0–3.0 | Est. FTE: N/A | Est. FTE: 0.25–0.5 |
| **Object Storage** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted MinIO or Ceph: cluster health monitoring, erasure coding config, S3 API compatibility management | MinIO Operator on K8s, PV management | S3: zero infrastructure management; lifecycle, versioning, events all declarative |
| | MinIO, Ceph RADOS | MinIO Operator | Amazon S3 |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05 |
| **Shared File System** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | NFS server management, Lustre cluster tuning, SMB configuration, HA setup | NFS StorageClass, CSI drivers, ReadWriteMany PVC coordination | EFS/FSx: managed HA, automatic throughput scaling |
| | NFS, Lustre (self-installed), Windows File Server | NFS CSI driver, Azure Files CSI | Amazon EFS, FSx for Windows/Lustre |
| | Est. FTE: 0.5–0.75 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |

**FTE Estimation Notes:**
- On-premises FTE estimates assume dedicated infrastructure staff and include on-call burden of 0.25–0.5 FTE per service per team
- Managed K8s estimates assume Kubernetes-native operators are configured and functioning; unplanned incidents add burst FTE
- Cloud-native estimates reflect configuration-only management via IaC (Terraform, CDK); on-call burden is near-zero for core infrastructure failures (handled by AWS)
- All FTE estimates are for a mid-size ISV serving approximately 50 enterprise customers; scale up proportionally for larger deployments

---

## 9. What Each AWS Managed Service Eliminates

The following table lists the specific operational tasks that AWS managed services eliminate, compared to self-hosted alternatives.

| AWS Service | Eliminated Operational Tasks |
|---|---|
| **Amazon RDS** | Hardware procurement and racking; OS installation and patching; database binary installation; storage volume management; replication topology configuration (Patroni, Barman); backup scheduling and verification; failover scripting; performance schema monitoring; minor and major version upgrade coordination |
| **Aurora Serverless v2** | All of the above PLUS: capacity planning for peak load; manual scale-up/scale-down operations; idle resource cost during off-hours |
| **Amazon DynamoDB** | Cluster management; shard rebalancing; compaction tuning; replica set management; index building; hardware scaling; global replication setup; conflict resolution logic; global traffic routing |
| **Amazon ElastiCache** | Redis/Valkey installation and configuration; Sentinel setup; replication group topology; AOF/RDB persistence tuning; node replacement on failure; upgrade coordination |
| **Amazon OpenSearch Service** | JVM heap tuning; shard allocation and rebalancing; hot-warm-cold lifecycle policy scripting; snapshot management; index rollover policies; node certificate management; cross-cluster replication setup |
| **Amazon Redshift Serverless** | Cluster provisioning; node type selection; vacuum scheduling; ANALYZE operations; concurrency scaling configuration; capacity monitoring; ETL pipeline engineering for source databases |
| **Amazon S3** | Object storage cluster management (Ceph, MinIO); erasure coding configuration; storage health monitoring; capacity expansion; S3 API compatibility testing; cross-site replication configuration |
| **Amazon EFS** | NFS server provisioning and HA configuration; RAID or multi-server setup; NFS export management; capacity monitoring and expansion |
| **Amazon FSx for Lustre** | Lustre MDS/OSS node management; network topology for high-bandwidth clients; storage target allocation; MDT/OST rebalancing; integration scripting for ML training pipelines |

---

## Key Takeaways

- **Operational leverage is extreme at the data tier.** Self-hosted databases and file systems represent the highest FTE concentration in an on-premises ISV operational profile. AWS managed data services convert recurring, specialized DBA and storage engineering work (estimated at 7–12 FTE total across the full on-premises data stack) into configuration-only operations (estimated at 1–2 FTE across the equivalent cloud-native stack).

- **DynamoDB and S3 have the lowest operational difficulty (1/5) of any cloud-native data services.** Both are fully managed with no cluster topology to operate, no patching to schedule, and no capacity ceilings to provision against. They are the default choice for any ISV application layer requiring key-value storage or object storage.

- **RDS Multi-AZ and Aurora Serverless v2 eliminate the most consequential on-premises risk: unplanned database downtime.** Automatic failover in 35–60 seconds with zero data loss replaces manual DBA intervention, which in self-hosted environments often requires 15–60 minutes during off-hours incidents.

- **ElastiCache for Valkey represents a 2024–2025 cost-efficiency step change.** The combination of Valkey's 20–33% lower pricing, 40% memory reduction, and 230% scaling improvements — plus emerging AI agent memory use cases — makes Valkey the preferred ElastiCache engine for new ISV deployments as of 2025.

- **Redshift Serverless and OpenSearch Serverless extend the managed-service model to workloads historically requiring dedicated clusters.** Both services eliminate the capacity planning and cluster sizing exercise that previously required data engineering expertise, allowing ISVs to deploy analytics and search capabilities without dedicated operations staff.

---

## Related — Out of Scope

- **AWS messaging services (SQS, SNS, Kinesis, MSK):** Referenced in Redshift zero-ETL context; detailed coverage in See [F15: AWS Messaging Services].
- **AWS AI/ML data services (SageMaker Feature Store, Bedrock Knowledge Bases):** Redshift ML integration with SageMaker noted; detailed coverage in See [F10: AWS AI Services].
- **Cost optimization tooling (Savings Plans, Cost Explorer, Compute Optimizer):** Relevant to RDS and Redshift reserved capacity; out of scope for this agent.
- **Aurora global database architecture:** Related to Aurora Serverless v2 but involves cross-region replication patterns beyond the scope of data services operational profiles.

---

## Sources

1. [AWS RDS Multi-AZ Features Page](https://aws.amazon.com/rds/features/multi-az/)
2. [AWS RDS FAQs](https://aws.amazon.com/rds/faqs/)
3. [AWS RDS for PostgreSQL Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
4. [AWS RDS Read Replicas](https://aws.amazon.com/rds/features/read-replicas/)
5. [AWS RDS Read Replicas Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
6. [AWS RDS Automated Backups Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
7. [AWS RDS Backup Retention Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html)
8. [AWS RDS SLA](https://aws.amazon.com/rds/sla/)
9. [AWS RDS Backup and Recovery Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/rds.html)
10. [AWS RDS Main Page](https://aws.amazon.com/rds/)
11. [AWS Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/)
12. [AWS Blog: Introducing scaling to 0 with Aurora Serverless v2](https://aws.amazon.com/blogs/database/introducing-scaling-to-0-capacity-with-amazon-aurora-serverless-v2/)
13. [AWS Aurora Serverless v2 Performance Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.setting-capacity.html)
14. [AWS Aurora Serverless v2 How It Works](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html)
15. [AWS Database Blog: Gartner recognizes Amazon RDS](https://aws.amazon.com/blogs/database/gartner-recognizes-amazon-rds-in-new-report/)
16. [AWS DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/)
17. [AWS DynamoDB On-Demand Pricing](https://aws.amazon.com/dynamodb/pricing/on-demand/)
18. [AWS DynamoDB Provisioned Pricing](https://aws.amazon.com/dynamodb/pricing/provisioned/)
19. [AWS DynamoDB FAQs](https://aws.amazon.com/dynamodb/faqs/)
20. [AWS DynamoDB Global Tables](https://aws.amazon.com/dynamodb/global-tables/)
21. [AWS DynamoDB Global Tables Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.html)
22. [AWS DynamoDB Global Tables How It Works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html)
23. [AWS DynamoDB SLA](https://aws.amazon.com/dynamodb/sla/)
24. [AWS Blog: DynamoDB lowers pricing for on-demand throughput and global tables](https://aws.amazon.com/blogs/database/new-amazon-dynamodb-lowers-pricing-for-on-demand-throughput-and-global-tables/)
25. [Cloud Ex Machina: DynamoDB Pricing Survival Manual](https://www.cloudexmachina.io/blog/dynamodb-pricing)
26. [AWS ElastiCache](https://aws.amazon.com/elasticache/)
27. [AWS ElastiCache FAQs](https://aws.amazon.com/elasticache/faqs/)
28. [AWS ElastiCache Pricing](https://aws.amazon.com/elasticache/pricing/)
29. [AWS ElastiCache Replication Documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.html)
30. [AWS ElastiCache Auto Failover Documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)
31. [AWS Blog: Reduce ElastiCache costs by up to 60% with Valkey](https://aws.amazon.com/blogs/database/reduce-your-amazon-elasticache-costs-by-up-to-60-with-valkey-and-cudos/)
32. [AWS ElastiCache re:Invent 2025 Recap](https://aws.amazon.com/blogs/database/amazon-elasticache-reinvent-2025-recap/)
33. [AWS: Redis OSS vs. Valkey](https://aws.amazon.com/elasticache/redis/)
34. [AWS OpenSearch Service Features](https://aws.amazon.com/opensearch-service/features/)
35. [AWS OpenSearch Serverless Features](https://aws.amazon.com/opensearch-service/features/serverless/)
36. [AWS OpenSearch Serverless Documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html)
37. [AWS OpenSearch UltraWarm Documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ultrawarm.html)
38. [AWS OpenSearch Multi-tier Storage Documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/multi-tier-storage.html)
39. [AWS: Amazon OpenSearch Service now offers a new multi-tier storage](https://aws.amazon.com/about-news/whats-new/2025/12/writeable-warm-tier-opensearch-optimized-instances/)
40. [AWS Blog: Choose the right storage tier for OpenSearch Service](https://aws.amazon.com/blogs/big-data/choose-the-right-storage-tier-for-your-needs-in-amazon-opensearch-service/)
41. [AWS Redshift](https://aws.amazon.com/redshift/)
42. [AWS Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/)
43. [AWS Redshift Serverless What It Is](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html)
44. [AWS Redshift Serverless Billing](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-billing.html)
45. [AWS Redshift Pricing](https://aws.amazon.com/redshift/pricing/)
46. [AWS Redshift ML](https://aws.amazon.com/redshift/features/redshift-ml/)
47. [AWS Redshift Zero-ETL Integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html)
48. [AWS Blog: Save on Redshift Serverless with Reservations](https://aws.amazon.com/blogs/big-data/save-up-to-24-on-amazon-redshift-serverless-compute-costs-with-reservations/)
49. [Navigating Amazon Redshift Serverless Pricing 2025](https://www.oreateai.com/blog/navigating-amazon-redshift-serverless-pricing-understanding-rpus-and-costs-in-2025/4000f61af1460fbe4709691b4f1bf303)
50. [AWS S3](https://aws.amazon.com/s3/)
51. [AWS S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)
52. [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/)
53. [AWS S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)
54. [AWS S3 FAQs](https://aws.amazon.com/s3/faqs/)
55. [AWS S3 Data Protection Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)
56. [AWS S3 Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
57. [AWS S3 Lifecycle Examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)
58. [AWS S3 Lifecycle Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configure-notification.html)
59. [AWS EFS Features](https://aws.amazon.com/efs/features/)
60. [AWS EFS Performance Documentation](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
61. [AWS EFS Managing Throughput](https://docs.aws.amazon.com/efs/latest/ug/managing-throughput.html)
62. [Amazon EFS FAQs](https://www.amazonaws.cn/en/efs/faq/)
63. [AWS: Help Me Choose an Amazon FSx File System](https://aws.amazon.com/fsx/when-to-choose-fsx/)
64. [AWS FSx for Lustre](https://aws.amazon.com/fsx/lustre/)
65. [AWS FSx for Lustre Features](https://aws.amazon.com/fsx/lustre/features/)
66. [AWS FSx for Lustre FAQs](https://aws.amazon.com/fsx/lustre/faqs/)
67. [AWS Blog: FSx for Lustre unlocks full network bandwidth and GPU performance](https://aws.amazon.com/blogs/aws/amazon-fsx-for-lustre-unlocks-full-network-bandwidth-and-gpu-performance/)
68. [AWS: EFS vs FSx for Windows vs FSx for Lustre — Tutorials Dojo](https://tutorialsdojo.com/amazon-efs-vs-amazon-fsx-for-windows-vs-amazon-fsx-for-lustre/)
69. [iCompaas: ElastiCache Auto Failover](https://support.icompaas.com/support/solutions/articles/62000233598-ensure-elasticache-redis-clusters-have-automatic-failover-enabled)
70. [AWS Blog: How Tradeshift boosted efficiency with Amazon RDS](https://aws.amazon.com/blogs/database/how-tradeshift-boosted-operational-efficiency-and-scalability-with-amazon-rds/)
