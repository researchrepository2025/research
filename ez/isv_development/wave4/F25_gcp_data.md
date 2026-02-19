# F25 — GCP Data Services
## Managed Databases, Caching, Search, and Storage on Google Cloud Platform

---

## Executive Summary

Google Cloud Platform provides a comprehensive portfolio of fully managed data services that eliminate the operational overhead of provisioning, patching, replication, failover, and capacity planning. Cloud SQL delivers managed relational databases (PostgreSQL, MySQL, SQL Server) with a 99.99% SLA (Enterprise Plus edition, including maintenance), while Cloud Spanner extends this to globally distributed relational workloads with a 99.999% SLA for multi-region configurations. For ISVs, the central value proposition is operational burden transfer: Google manages the undifferentiated infrastructure work—high availability orchestration, backup scheduling, node balancing, and security patching—freeing engineering teams to focus on product differentiation. The storage tier (Cloud Storage, Filestore) complements the database tier with 11-nine durability guarantees and flexible tiering, while BigQuery's serverless warehouse and Bigtable's petabyte-scale NoSQL address analytical and high-throughput operational patterns respectively.

---

## Cloud SQL — Managed PostgreSQL, MySQL, and SQL Server

### Overview

Cloud SQL is Google's fully managed relational database service supporting PostgreSQL, MySQL, and SQL Server. It handles provisioning, patching, backups, and high availability automatically. [Google Cloud SQL product page](https://cloud.google.com/sql)

### Editions and SLA

Two editions are available for Cloud SQL:

| Edition | SLA | Maintenance Behavior | Key Differentiators |
|---|---|---|---|
| Enterprise | 99.95% | Excludes maintenance windows (~30s downtime) | Standard backups, 7-day query insights retention |
| Enterprise Plus | 99.99% | **Includes maintenance** (<1s downtime) | Data cache (up to 4x read perf), 2x write latency improvement, read pool autoscaling, managed connection pooling, 30-day query insights retention, cross-regional DR |

[SOURCE: Cloud SQL for PostgreSQL editions overview](https://docs.cloud.google.com/sql/docs/postgres/editions-intro)

### High Availability Architecture

[FACT] Cloud SQL HA uses synchronous replication to persistent disks in both zones before a transaction is reported as committed. A primary and a standby instance exist in separate zones within the same region. [SOURCE: About high availability — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/high-availability)

[FACT] "When a failover occurs, you can expect the instance to be unavailable for about sixty seconds," though actual duration varies by environment. [SOURCE: About high availability — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/high-availability)

[FACT] As of January 13, 2025, the legacy HA configuration is deprecated for all instances; it is no longer possible to create instances with legacy HA or enable it on existing instances. [SOURCE: Cloud SQL high availability documentation](https://docs.cloud.google.com/sql/docs/postgres/high-availability)

[FACT] Without HA configured, administrators "must restore any zonal instances manually" following outages; HA-configured instances fail over automatically without requiring application changes or connection string reconfiguration. [SOURCE: About high availability — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/high-availability)

### Read Replicas

[FACT] "The read replica is an exact copy of the primary instance, with data and other changes on the primary instance updated in almost real time on the read replica." Read replicas handle queries, read requests, and analytics traffic to reduce load on the primary instance. [SOURCE: Manage read replicas — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas)

[FACT] Regular read replicas are not automatic failover targets; HA or DR replica patterns must be used when controlled failover semantics are required. [SOURCE: About replication in Cloud SQL — PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication)

### Automated Backups and PITR

[FACT] Cloud SQL supports automated backups on a scheduled cadence (hourly, daily, weekly, or monthly) while the instance is running. [SOURCE: Cloud SQL backups overview — MySQL](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups)

[FACT] For newly PITR-enabled instances, write-ahead logs used for point-in-time recovery are stored in Google Cloud Storage rather than consuming instance disk storage; they are retrieved on demand during a restore. [SOURCE: Point-in-time recovery without impacting instance storage — Google Cloud Blog](https://cloud.google.com/blog/products/databases/point-in-time-recovery-without-impacting-instance-storage)

### Instance Scale (Enterprise Plus)

[FACT] Cloud SQL Enterprise Plus supports up to 128 vCPUs and 864 GiB of memory on Performance-optimized N2 and C4A machine series instances. [SOURCE: Choose a machine series — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview)

### Operational Burden Eliminated (Difficulty Rating)

| Task | Self-Hosted Difficulty (1-5) | Cloud SQL Burden |
|---|---|---|
| Failover orchestration | 4 | Fully automated |
| Backup scheduling and retention | 3 | Fully automated |
| Point-in-time recovery | 4 | One-click restore |
| OS/engine patching | 3 | Fully automated |
| Read replica provisioning | 3 | Managed via console/API |
| HA standby management | 4 | Fully automated |
| Connection pooling (Enterprise Plus) | 3 | Managed Connection Pooling |

---

## Cloud Spanner — Globally Distributed Relational Database

### Overview

Cloud Spanner is Google's globally distributed, horizontally scalable relational database combining ACID transactions with external consistency across regions and continents. It was awarded the [2025 ACM SIGMOD Systems Award](https://cloud.google.com/blog/products/databases/spanner-wins-the-2025-acm-sigmod-systems-award).

[STATISTIC] Spanner handles over 6 billion queries per second at peak and more than 17 exabytes of data. [SOURCE: Spanner wins the 2025 ACM SIGMOD Systems Award — Google Cloud Blog](https://cloud.google.com/blog/products/databases/spanner-wins-the-2025-acm-sigmod-systems-award)

### Editions and SLA

| Edition | SLA | Configurations | Key Features |
|---|---|---|---|
| Standard | 99.99% | Regional only | GoogleSQL + PostgreSQL, PITR (7-day), BigQuery federation |
| Enterprise | 99.99% | Regional + custom read replicas | Spanner Graph, full-text search, vector search (KNN/ANN), columnar engine, incremental backups, tiered storage |
| Enterprise Plus | **99.999%** | Multi-region | Geo-partitioning, all Enterprise features |

[SOURCE: Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview)

[FACT] Commitment discounts available: "20% for 1 year, 40% for 3 years" across all Spanner editions. [SOURCE: Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview)

### Horizontal Scaling Architecture

[FACT] "Spanner decouples compute resources from data storage, making it possible to increase, decrease, or reallocate processing resources without changes to storage, allowing horizontal upscaling with a single click or API call to serve higher operations per second capacity." [SOURCE: Google Cloud Spanner product page](https://cloud.google.com/spanner)

[FACT] Automatic database sharding ensures optimal data distribution; geo-partitioning brings data closer to users for lower latency. [SOURCE: Google Cloud Spanner product page](https://cloud.google.com/spanner)

[FACT] Spanner leverages "synchronous, Paxos-based replication across multiple zones or regions" to maintain strong consistency. [SOURCE: Google Cloud Spanner — talent500.com analysis](https://talent500.com/blog/google-cloud-spanner-global-scale-data-management/)

[FACT] Spanner "is the first system to distribute data at global scale and support externally-consistent distributed transactions." [SOURCE: Spanner: Google's Globally-Distributed Database — Google Research](https://research.google/pubs/spanner-googles-globally-distributed-database-2/)

### Operational Burden Eliminated

[FACT] Spanner eliminates "manual sharding or eventual consistency" management, reducing risk and downtime with "zero maintenance" automated operations. [SOURCE: Google Cloud Spanner product page](https://cloud.google.com/spanner)

| Task | Self-Hosted (Distributed DB) Difficulty (1-5) | Spanner Burden |
|---|---|---|
| Global data sharding | 5 | Fully automated |
| Cross-region replication | 5 | Fully automated (Paxos) |
| Horizontal scaling | 4 | Single click / API call |
| Strong consistency enforcement | 5 | Built-in external consistency |
| Schema changes with zero downtime | 4 | Online schema changes |
| Failover across regions | 5 | Fully automated |

---

## Cloud Firestore — Serverless Document Database

### Overview

Cloud Firestore is a fully managed, serverless NoSQL document database providing real-time data synchronization, offline client support, and automatic scaling. Google was named "a Leader, positioned furthest in vision in the 2025 Gartner Magic Quadrant for Cloud Database Management Systems." [SOURCE: Google Cloud Firestore product page](https://cloud.google.com/products/firestore)

### Availability and Performance

[FACT] Firestore provides "industry-leading high availability of up to 99.999% SLA" with multi-region replication and strong consistency. [SOURCE: Cloud Firestore product page](https://firebase.google.com/products/firestore)

[FACT] Firestore delivers "single-digit milliseconds read performance" for standard read operations. [SOURCE: Cloud Firestore product page](https://cloud.google.com/products/firestore)

### Real-Time Sync and Offline Support

[FACT] "Cloud Firestore keeps your data in sync across client apps through realtime listeners and offers offline support for mobile and web so you can build responsive apps that work regardless of network latency or Internet connectivity." [SOURCE: Firebase Firestore documentation](https://firebase.google.com/docs/firestore)

[FACT] Real-time listeners retrieve "only the new changes" on data updates, minimizing bandwidth consumption. [SOURCE: Firebase Firestore documentation](https://firebase.google.com/docs/firestore)

### 2025 Feature: MongoDB Compatibility

[FACT] At Google Cloud Next 2025, Google announced preview of "Firestore with MongoDB compatibility, introducing support for the MongoDB API and query language to store and query semi-structured JSON data." This is backed by "a serverless infrastructure featuring single-digit-millisecond read performance, automatic scaling, and high availability." [SOURCE: Google Cloud announces Firestore with MongoDB compatibility — InfoQ, April 2025](https://www.infoq.com/news/2025/04/google-firestore-mongodb/)

### Pricing Model

| Operation | Rate (us-central1) | Free Daily Tier |
|---|---|---|
| Reads | $0.03 per 100,000 | 50,000 reads/day |
| Writes | $0.09 per 100,000 | 20,000 writes/day |
| Deletes | $0.01 per 100,000 | 20,000 deletes/day |
| Storage | Per GB stored | 1 GB/month |

[SOURCE: Understand Cloud Firestore billing — Firebase](https://firebase.google.com/docs/firestore/pricing)

### Operational Burden Eliminated

| Task | Self-Hosted Difficulty (1-5) | Firestore Burden |
|---|---|---|
| Server provisioning | 3 | Fully eliminated (serverless) |
| Capacity planning | 4 | Fully eliminated (auto-scales) |
| Replication management | 4 | Fully automated (multi-region) |
| Offline sync infrastructure | 5 | Built into SDK |
| Real-time push infrastructure | 4 | Built-in realtime listeners |
| Schema migrations | 3 | Schema-less (flexible) |

---

## Memorystore — Managed Redis and Memcached

### Overview

Memorystore is GCP's fully managed in-memory data service supporting Redis (standard), Redis Cluster, Memcached, and Valkey (the open-source Redis fork). It automates "provisioning, replication, failover, and monitoring" as well as "patching, 24x7 threat monitoring, failure detection, and automatic failover." [SOURCE: Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)

### Memorystore for Redis (Standard)

[FACT] Supported Redis versions: 7.2, 7.0, 6.x, 5.0, 4.0, and 3.2. [SOURCE: Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)

[FACT] Instance capacity tiers: M1 (1-4 GB), M2 (5-10 GB), M3 (11-35 GB), M4 (36-100 GB), M5 (101-300 GB). Maximum capacity: 300 GB. [SOURCE: Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)

[FACT] Maximum write throughput: 16 Gbps. Read throughput scales independently per replica node at 16 Gbps per node. [SOURCE: Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)

[FACT] Standard Tier SLA: 99.9% availability with cross-zone replication and automatic failover. [SOURCE: Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)

[FACT] "If the primary instance fails, then the instance fails over automatically to a replica." For Standard Tier, during a failover, "the primary instance and read endpoint redirect automatically to the new primary instance and replicas." [SOURCE: High availability for Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/high-availability-for-memorystore-for-redis)

[FACT] "The instance is unavailable for an average of 30 seconds during automated repairs, and 15 seconds for maintenance events." [SOURCE: High availability for Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/high-availability-for-memorystore-for-redis)

### Memorystore for Valkey (GA — 2025)

[FACT] Memorystore for Valkey reached general availability in 2025. Valkey 8.0 "delivers better throughput and achieves up to 2x Queries Per Second (QPS) of Memorystore for Redis Cluster at microseconds latency." [SOURCE: High availability and replicas — Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas)

[FACT] Memorystore for Valkey supports instances with 0-5 replicas per node. "Memorystore for Valkey distributes the primary and replica VMs of shards across multiple zones to safeguard against a zonal outage." [SOURCE: High availability and replicas — Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas)

[FACT] Memorystore for Valkey is backed by a 99.99% availability SLA. [SOURCE: Announcing general availability of Memorystore for Valkey — Google Cloud Blog](https://cloud.google.com/blog/products/databases/announcing-general-availability-of-memorystore-for-valkey)

[FACT] Memorystore for Valkey and Redis Cluster "scale without downtime to support up to 250 nodes, terabytes of keyspace, and 60x more throughput than Memorystore for Redis with microsecond latencies." [SOURCE: Memorystore cross-region replication and single-shard clusters — Google Cloud Blog](https://cloud.google.com/blog/products/databases/memorystore-cross-region-replication-and-single-shard-clusters)

### Pricing Model

[FACT] Billing is capacity-based: "you are billed by the hour for the capacity (GB) that you provision," with per-minute granularity for short-term usage. [SOURCE: Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)

### Operational Burden Eliminated

| Task | Self-Hosted Difficulty (1-5) | Memorystore Burden |
|---|---|---|
| Redis cluster provisioning | 3 | Fully automated |
| Sentinel / failover configuration | 4 | Fully automated |
| Patching and version upgrades | 3 | Fully automated |
| Cross-zone HA topology | 4 | Fully automated |
| 24x7 threat monitoring | 3 | Included |
| Read replica scaling | 3 | API-driven |

---

## Bigtable — Wide-Column NoSQL at Scale

### Overview

Cloud Bigtable is a fully managed, wide-column, key-value NoSQL database designed for large analytical and operational workloads at petabyte scale with single-digit millisecond latency. [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

### Scale and Performance

[FACT] Bigtable "can scale to billions of rows and thousands of columns" and handle "terabytes or even petabytes of data." [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

[FACT] Throughput scales with nodes: "each node provides up to 10,000 operations per second (read and write)." [SOURCE: Cloud Bigtable: NoSQL Wide-Column Database Service — K21 Academy](https://k21academy.com/google-cloud/bigtable/)

[FACT] Bigtable "scales in direct proportion to the number of machines in your cluster." Bigtable can be configured to "continuously monitor cluster CPU capacity and automatically adjust the number of nodes in a cluster when necessary." [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

[FACT] Latency target: single-digit milliseconds for read and write operations. [SOURCE: How BIG is Cloud Bigtable? — Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/how-big-cloud-bigtable)

### Replication and Durability

[FACT] Replication is self-configuring: "add a second cluster to your instance, and replication starts automatically." Multi-cluster deployments provide "eventual consistency" by default, or "read-your-writes consistency or strong consistency, depending on the workload and app profile settings." [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

### Operational Tasks Eliminated

[FACT] "Bigtable handles upgrades and restarts transparently." [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

[FACT] "Bigtable manages the splitting, merging, and rebalancing automatically." [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

[FACT] Data compaction occurs "automatically" without configuration options required from operators. [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

[FACT] Bigtable "automatically maintains high data durability." [SOURCE: Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)

| Task | Self-Hosted HBase Difficulty (1-5) | Bigtable Burden |
|---|---|---|
| Tablet splitting / merging | 5 | Fully automated |
| Compaction scheduling | 4 | Fully automated |
| Cluster node balancing | 4 | Fully automated |
| Replication setup | 4 | Automatic on cluster add |
| Upgrade management | 3 | Transparent |
| Capacity auto-scaling | 4 | Autoscaling available |

### Primary Use Cases

[FACT] Bigtable is suited for "IoT, AdTech, FinTech, gaming and ML based personalizations" — workloads requiring "a specific amount of scale or throughput with strict latency requirements." [SOURCE: Google Cloud Bigtable: NoSQL for High-Performance Workloads — Medium](https://medium.com/@teja.ravi474/google-cloud-bigtable-nosql-for-high-performance-workloads-e8e637bdcfd2)

---

## BigQuery — Serverless Data Warehouse

### Overview

BigQuery is Google Cloud's fully managed, serverless enterprise data warehouse. "BigQuery's serverless infrastructure lets you focus on your data instead of resource management." [SOURCE: BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)

### Query Performance

[FACT] BigQuery can "query terabytes in seconds and petabytes in minutes" using a separated compute and storage architecture that allows independent resource allocation. [SOURCE: BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)

### ML Integration

[FACT] BigQuery ML supports natively within SQL: linear regression, logistic regression (binary and multiclass), k-means clustering, time series forecasting (ARIMA+, TimesFM), text generation (generative AI), and embeddings. [SOURCE: BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)

[FACT] "With native Vertex AI integration, you can easily connect your data to Google's industry leading AI without leaving BigQuery." [SOURCE: Serverless Data Analytics with Google: BigQuery in 2025 — Hexaware](https://hexaware.com/blogs/serverless-data-analytics-with-google-cloud-platform-why-bigquery-stands-out-in-2025/)

### Streaming Ingestion — Storage Write API

[FACT] The BigQuery Storage Write API default quota is 3 GB/s (three times the 1 GB/s quota of the legacy streaming API). Additional quota can be provisioned on request. [SOURCE: BigQuery Storage Write API at scale — Medium/Brachi Packter](https://medium.com/@bravnic/bigquery-storage-write-api-at-scale-7affcc2d7a93)

[FACT] Latency for data to become queryable via committed stream type: 3–5 seconds. [SOURCE: BigQuery data ingestion methods — Google Cloud Community](https://medium.com/google-cloud/bigquery-data-ingestion-methods-tradeoffs-e1f15c6ca2f6)

[FACT] "A single connection supports at least 1 MBps of throughput" with upper limits depending on "network bandwidth, the schema of the data, and server load." [SOURCE: Introduction to the BigQuery Storage Write API](https://docs.cloud.google.com/bigquery/docs/write-api)

[FACT] The Storage Write API provides up to 2 TiB per month of free ingestion. [SOURCE: Introduction to the BigQuery Storage Write API](https://docs.cloud.google.com/bigquery/docs/write-api)

[FACT] "If you exceed 40-50 calls per second, the latency of the API calls grows substantially (>25s)." Use non-blocking `AppendRows` for highest throughput. [SOURCE: BigQuery Storage Write API best practices](https://docs.cloud.google.com/bigquery/docs/write-api-best-practices)

### Pricing Model

[FACT] BigQuery pricing has two modes: on-demand (pay-per-query) and capacity-based (reservations). Storage is billed separately. BigQuery ML, BI Engine, and Data Transfer Service carry distinct pricing. [SOURCE: BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)

### Operational Burden Eliminated

[FACT] BigQuery provides "zero infrastructure management" — no resource provisioning, manual scaling, or maintenance required. [SOURCE: BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)

| Task | Self-Hosted DW Difficulty (1-5) | BigQuery Burden |
|---|---|---|
| Cluster provisioning | 4 | Fully eliminated (serverless) |
| Index management | 4 | Fully automated |
| Vacuuming / compaction | 3 | Fully automated |
| Partition management | 3 | Declarative configuration |
| ML model infrastructure | 5 | In-database SQL-based ML |
| Storage/compute scaling | 4 | Fully separated and serverless |

---

## Cloud Storage — Object Storage

### Overview

Cloud Storage is GCP's globally durable object storage service with no minimum object size, unlimited capacity, and multiple storage classes optimized for access frequency. [SOURCE: Cloud Storage product page](https://cloud.google.com/storage)

### Durability and Availability

[FACT] Cloud Storage is "designed for at least 99.999999999% (11 9's) annual durability, regardless of storage class and location type." Google achieves this through "erasure coding" storing data pieces redundantly across multiple devices. [SOURCE: Data availability and durability — Cloud Storage](https://docs.cloud.google.com/storage/docs/availability-durability)

### Storage Classes

| Class | API Name | Min. Retention | Retrieval Fee | Use Case |
|---|---|---|---|---|
| Standard | `STANDARD` | None | None | Frequently accessed ("hot") data or brief storage |
| Nearline | `NEARLINE` | 30 days | Yes | Data accessed ~once per month or less |
| Coldline | `COLDLINE` | 90 days | Yes | Data accessed at most once per quarter |
| Archive | `ARCHIVE` | 365 days | Yes | Data accessed less than once per year |

[SOURCE: Storage classes — Google Cloud](https://docs.cloud.google.com/storage/docs/storage-classes)

### Availability SLAs by Class and Location

| Storage Class | Multi-Region / Dual-Region SLA | Regional SLA |
|---|---|---|
| Standard | 99.95% | 99.9% |
| Nearline / Coldline / Archive | 99.9% | 99.0% |

[SOURCE: Storage classes — Google Cloud](https://docs.cloud.google.com/storage/docs/storage-classes)

### Lifecycle Management

[FACT] Object Lifecycle Management (OLM) lets operators "define rules that automatically perform actions on objects in a bucket based on certain conditions — like how old the object is or what storage class it's in." Actions include `SetStorageClass` (automatic tiering) and `AbortIncompleteMultipartUpload`. [SOURCE: Object Lifecycle Management — Cloud Storage](https://docs.cloud.google.com/storage/docs/lifecycle)

[FACT] As of 2025, the limit for the maximum number of prefixes and suffixes when using `matchesPrefix` and `matchesSuffix` lifecycle conditions across all rules on a bucket was increased from 50 to 1,000. [SOURCE: Cloud Storage release notes](https://cloud.google.com/storage/docs/release-notes)

### Signed URLs

[FACT] Maximum signed URL expiration is "604800 seconds (7 days)." [SOURCE: Signed URLs — Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)

[FACT] Signed URLs enable access without requiring a Google account: "Anyone who knows the URL can access the resource until the expiration time for the URL is reached or the key used to sign the URL is rotated." [SOURCE: Signed URLs — Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)

[FACT] Signed URLs function "exclusively through XML API endpoints and cannot be used with other Cloud Storage access methods." [SOURCE: Signed URLs — Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)

[FACT] Primary use cases for signed URLs: "uploads and downloads" — scenarios where operators "might not want to require your users to have their own account in order to access Cloud Storage, but you still want to control access using your application-specific logic." [SOURCE: Signed URLs — Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)

### Operational Burden Eliminated

| Task | Self-Hosted Object Storage Difficulty (1-5) | Cloud Storage Burden |
|---|---|---|
| Hardware provisioning | 4 | Fully eliminated |
| Erasure coding configuration | 4 | Built-in |
| Storage tiering automation | 3 | Lifecycle rules (declarative) |
| CDN / global distribution | 3 | Built-in multi-region buckets |
| Capacity management | 3 | Fully eliminated (unlimited) |
| Access token management | 3 | Signed URL API |

---

## Filestore — Managed NFS File Storage

### Overview

Cloud Filestore is a fully managed NFS file storage service designed for applications requiring a shared filesystem. It is compatible with Kubernetes (GKE CSI driver) and traditional enterprise workloads. [SOURCE: Filestore overview](https://docs.cloud.google.com/filestore/docs/overview)

### Service Tiers and Performance

| Tier | Capacity Range | Read Throughput | Write Throughput | Read IOPS | Write IOPS | Notes |
|---|---|---|---|---|---|---|
| Basic HDD | 1–63.9 TiB | 100–180 MiB/s | — | 600–1,000 | — | Scales with capacity above 10 TiB |
| Basic SSD | 2.5–63.9 TiB | **1,200 MiB/s** | — | **60,000** | — | Fixed performance regardless of capacity |
| Zonal (1–9.75 TiB) | 1–9.75 TiB | 260 MiB/s per TiB | 88 MiB/s per TiB | 9,200 per TiB | 2,600 per TiB | High-performance computing |
| Zonal (10–100 TiB) | 10–100 TiB | Scales with capacity | — | — | — | Cost-effective large capacity |
| Regional (1–9.75 TiB) | 100 GiB–9.75 TiB | 120 MiB/s per TiB | 100 MiB/s per TiB | 12,000 per TiB | 4,000 per TiB | Zone-outage resilient |
| Enterprise | 1–10 TiB | — | — | — | — | Kubernetes multishares, GKE CSI driver |

[SOURCE: Instance performance — Filestore](https://docs.cloud.google.com/filestore/docs/performance) | [Service tiers — Filestore](https://docs.cloud.google.com/filestore/docs/service-tiers)

### High Availability

[FACT] "Regional and enterprise-tier Filestore instances are regional resources that continue to serve data and accept new writes in the event of a zone failure, making the zone failure transparent to clients." [SOURCE: Service tiers — Filestore](https://docs.cloud.google.com/filestore/docs/service-tiers)

### Custom Performance Configuration

[FACT] Filestore supports custom performance configuration "according to your workload needs independently of specified capacity, either specifying an IOPS per TiB ratio or setting a fixed number of IOPS." [SOURCE: Instance performance — Filestore](https://docs.cloud.google.com/filestore/docs/performance)

### Primary Use Cases

| Tier | Use Cases |
|---|---|
| Zonal | Genome sequencing, financial trading, high-performance computing |
| Regional | Enterprise applications requiring zone-outage resilience |
| Enterprise | Kubernetes workloads, GKE CSI driver, multishare configurations |
| Basic | File sharing, software development, cost-sensitive GKE workloads |

[SOURCE: Service tiers — Filestore](https://docs.cloud.google.com/filestore/docs/service-tiers)

### Operational Burden Eliminated

| Task | Self-Hosted NFS Difficulty (1-5) | Filestore Burden |
|---|---|---|
| NFS server provisioning | 3 | Fully automated |
| HA / zone failover | 4 | Automated (Regional/Enterprise tiers) |
| Capacity expansion | 3 | Online resize |
| Patch management | 3 | Fully automated |
| Performance tuning | 3 | Custom IOPS configuration |
| Kubernetes integration | 3 | Native GKE CSI driver |

---

## Cross-Service Comparison Summary

| Service | Category | SLA (Max) | Operational Model | Difficulty Self-Hosted (1-5) | Primary ISV Trigger |
|---|---|---|---|---|---|
| Cloud SQL | Relational DB | 99.99% | Managed, zonal/regional | 4 | Drop-in PostgreSQL/MySQL/SQL Server |
| Cloud Spanner | Global Relational | 99.999% | Fully managed, global | 5 | Horizontal scale + ACID globally |
| Firestore | Document DB | 99.999% | Serverless | 4 | Mobile/web real-time sync |
| Memorystore (Redis) | In-memory cache | 99.9% | Managed | 3 | Session caching, Pub/Sub patterns |
| Memorystore (Valkey) | In-memory cache | 99.99% | Managed | 3 | High-throughput cache, Redis fork |
| Bigtable | Wide-column NoSQL | Not published | Managed | 5 | IoT, time-series, AdTech at petabyte scale |
| BigQuery | Data Warehouse | Not published | Serverless | 4 | Analytics, ML, streaming ingestion |
| Cloud Storage | Object Storage | 99.95% | Fully managed | 3 | Blob/artifact storage, CDN origin |
| Filestore | NFS File Storage | Not published | Managed | 3 | Shared filesystem, GKE persistent volumes |

---

## Key Takeaways

- **Cloud SQL (Enterprise Plus) and Cloud Spanner represent GCP's managed relational offering at two tiers**: Cloud SQL provides a 99.99% SLA (including maintenance) for conventional workloads up to 128 vCPUs/864 GiB, while Spanner delivers 99.999% SLA for globally distributed, horizontally scaled ACID workloads handling 6 billion+ queries per second at peak — the choice between them is driven by global distribution requirements and tolerance for schema migration complexity.

- **The serverless tier (Firestore, BigQuery) eliminates all infrastructure decisions**: Both services scale to zero and back without provisioning events, removing capacity planning and failover engineering entirely. BigQuery's 3 GB/s streaming ingest quota and in-database ML (including Vertex AI integration) make it GCP's most integrated analytics layer for ISVs building data-driven products.

- **Memorystore's 2025 Valkey GA introduction delivers a 99.99% SLA and up to 2x QPS versus Redis Cluster**, a significant reliability and performance upgrade for ISVs using Memorystore for caching and session layers; Valkey scales to 250 nodes and terabytes of keyspace without downtime.

- **Cloud Storage's 11-nine durability guarantee and lifecycle management automation** make it the default choice for ISV artifact, media, and backup storage — signed URLs (7-day max expiration, possession-based access) eliminate the need to expose storage credentials to end-users directly, a common ISV pattern for secure file delivery.

- **Operational burden reduction across GCP data services is asymmetric**: The most significant savings come in tasks rated Difficulty 4-5 on self-hosted infrastructure — global sharding (Spanner), tablet compaction (Bigtable), HA failover orchestration (all services), and real-time sync infrastructure (Firestore) — areas where ISV engineering teams would otherwise require deep specialized expertise to operate reliably.

---

## Sources

1. [Google Cloud SQL product page](https://cloud.google.com/sql)
2. [About high availability — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/high-availability)
3. [About high availability — Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/high-availability)
4. [Cloud SQL for PostgreSQL editions overview](https://docs.cloud.google.com/sql/docs/postgres/editions-intro)
5. [Manage read replicas — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas)
6. [About replication in Cloud SQL — PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication)
7. [Cloud SQL backups overview — MySQL](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups)
8. [Point-in-time recovery without impacting instance storage — Google Cloud Blog](https://cloud.google.com/blog/products/databases/point-in-time-recovery-without-impacting-instance-storage)
9. [Choose a machine series — Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview)
10. [Google Cloud Spanner product page](https://cloud.google.com/spanner)
11. [Spanner wins the 2025 ACM SIGMOD Systems Award — Google Cloud Blog](https://cloud.google.com/blog/products/databases/spanner-wins-the-2025-acm-sigmod-systems-award)
12. [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview)
13. [Spanner: Google's Globally-Distributed Database — Google Research](https://research.google/pubs/spanner-googles-globally-distributed-database-2/)
14. [Cloud Spanner SLA](https://cloud.google.com/spanner/sla)
15. [Google Cloud Firestore product page](https://cloud.google.com/products/firestore)
16. [Firebase Firestore product page](https://firebase.google.com/products/firestore)
17. [Firebase Firestore documentation](https://firebase.google.com/docs/firestore)
18. [Google Cloud announces Firestore with MongoDB compatibility — InfoQ, April 2025](https://www.infoq.com/news/2025/04/google-firestore-mongodb/)
19. [Understand Cloud Firestore billing — Firebase](https://firebase.google.com/docs/firestore/pricing)
20. [Memorystore product page](https://cloud.google.com/memorystore)
21. [Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)
22. [High availability for Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/high-availability-for-memorystore-for-redis)
23. [High availability and replicas — Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas)
24. [High availability and replicas — Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/ha-and-replicas)
25. [Announcing general availability of Memorystore for Valkey — Google Cloud Blog](https://cloud.google.com/blog/products/databases/announcing-general-availability-of-memorystore-for-valkey)
26. [Memorystore cross-region replication and single-shard clusters — Google Cloud Blog](https://cloud.google.com/blog/products/databases/memorystore-cross-region-replication-and-single-shard-clusters)
27. [Bigtable: Fast, Flexible NoSQL — Google Cloud](https://cloud.google.com/bigtable)
28. [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview)
29. [How BIG is Cloud Bigtable? — Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/how-big-cloud-bigtable)
30. [Cloud Bigtable: NoSQL Wide-Column Database Service — K21 Academy](https://k21academy.com/google-cloud/bigtable/)
31. [BigQuery product page](https://cloud.google.com/bigquery)
32. [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)
33. [Introduction to the BigQuery Storage Write API](https://docs.cloud.google.com/bigquery/docs/write-api)
34. [BigQuery Storage Write API best practices](https://docs.cloud.google.com/bigquery/docs/write-api-best-practices)
35. [BigQuery data ingestion methods — Google Cloud Community](https://medium.com/google-cloud/bigquery-data-ingestion-methods-tradeoffs-e1f15c6ca2f6)
36. [Serverless Data Analytics with Google: BigQuery in 2025 — Hexaware](https://hexaware.com/blogs/serverless-data-analytics-with-google-cloud-platform-why-bigquery-stands-out-in-2025/)
37. [Cloud Storage product page](https://cloud.google.com/storage)
38. [Storage classes — Google Cloud](https://docs.cloud.google.com/storage/docs/storage-classes)
39. [Object Lifecycle Management — Cloud Storage](https://docs.cloud.google.com/storage/docs/lifecycle)
40. [Data availability and durability — Cloud Storage](https://docs.cloud.google.com/storage/docs/availability-durability)
41. [Signed URLs — Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/signed-urls)
42. [Cloud Storage release notes](https://cloud.google.com/storage/docs/release-notes)
43. [Filestore product page](https://cloud.google.com/filestore)
44. [Filestore overview](https://docs.cloud.google.com/filestore/docs/overview)
45. [Service tiers — Filestore](https://docs.cloud.google.com/filestore/docs/service-tiers)
46. [Instance performance — Filestore](https://docs.cloud.google.com/filestore/docs/performance)
