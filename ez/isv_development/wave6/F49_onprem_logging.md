# F49 — On-Premises Logging & Log Aggregation

**Research Area:** Self-Hosted Centralized Logging Infrastructure
**Deployment Context:** ISV evaluating on-premises, managed Kubernetes, and cloud-native deployment models
**Date:** 2026-02-18

---

## Executive Summary

Self-hosting centralized logging infrastructure at production scale requires significant hardware investment, specialist engineering capacity, and continuous operational discipline that cloud-managed alternatives abstract entirely. The ELK Stack (Elasticsearch, Logstash/Fluentd, Kibana) remains the dominant self-hosted option, capable of processing upward of 220,000 events per second on a three-node cluster, but demands careful shard sizing, tiered storage architecture, and dedicated engineering time to maintain query performance at scale. Grafana Loki offers a cost-architecture alternative that indexes only metadata rather than full log content, enabling compressed chunk storage on commodity object stores at dramatically lower cost — approximately $300/month versus $1,665/month for 100 GB/day compared to CloudWatch Logs — but shifts operational burden to label schema design and retention compaction management. For ISVs serving multi-tenant SaaS customers, both stacks require deliberate tenant isolation configuration (tenant-scoped indices in Elasticsearch or `X-Scope-OrgID` header enforcement in Loki), and neither eliminates the 2–4 hours per week of active maintenance that managed cloud services remove entirely. The choice between self-hosted logging and managed services is primarily an economics decision anchored to log volume: below 50 GB/day, managed services are generally cost-competitive; above 100 GB/day, self-hosted solutions can achieve 75–90% cost reduction.

---

## ELK Stack: Elasticsearch Cluster Sizing, Tuning, and Maintenance

### Cluster Architecture

The ELK Stack combines Elasticsearch (distributed search and analytics engine), Logstash or Fluentd/Fluent Bit (ingestion and processing), and Kibana (visualization). For production logging workloads, Elastic recommends a minimum of three nodes to achieve quorum for master elections and data redundancy.

[Elastic's benchmarking guidance](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics) provides the following tier-specific node configurations:

- **Small deployment (1 GB/day, 9-month retention):** 3 data nodes, 8 GB memory each
- **Large deployment (100 GB/day):** 5 hot-zone nodes (64 GB RAM, 30-day retention) + 10 warm-zone nodes (64 GB RAM, 12-month retention)

### Heap and Memory Sizing

JVM heap should be set to 50% of available RAM, with the remainder reserved for OS filesystem cache. The 32 GB ceiling on JVM heap is a hard constraint driven by the JVM's compressed ordinary object pointers (OOPs) limit. A node with 64 GB RAM allocates 30 GB to heap and 34 GB to OS cache — the [Elastic cluster sizing guide](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics) models this explicitly.

### Shard Sizing

[Elastic's official shard sizing documentation](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards) establishes:

- Target physical shard size: **10 GB to 50 GB**
- Maximum document count per shard: **200 million documents**
- Maximum non-frozen shards per node: **1,000**
- Master-eligible node heap requirement: **at least 1 GB per 3,000 indices**

For time-series log data, the recommended practice is to calculate primary shard count by dividing daily ingest volume by target shard size. For 80 GB/day at a 40 GB target, this yields 2 primary shards per daily index. The `max_primary_shard_size` ILM rollover condition is preferred over `max_age` to prevent creation of empty or undersized indices.

### Ingestion Performance Benchmarks

[Elastic's published benchmarks](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics) show the following throughput on a three-node cluster:

| Dataset | Optimal Bulk Size | Max Throughput |
|---------|------------------|----------------|
| Metricbeat (1.2 GB) | 12,000 documents | 62,000 events/sec |
| HTTP Server Logs (31.1 GB) | 16,000 documents | 220,000 events/sec |
| Combined indexing + search | — | ~173,000 events/sec + 1,000 queries/sec |

Elasticsearch 8.8 demonstrated a **13% ingestion speed improvement** over version 8.6 on realistic multi-dataset logging benchmarks, with throughput increasing from approximately 22,500 to 25,500 docs/sec on the same hardware per the [Elastic engineering blog](https://www.elastic.co/blog/data-ingestion-elasticsearch).

### Storage Calculation Formula

The [Elastic sizing guide](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics) defines total storage requirements as:

```
Total Storage = Raw Data (GB/day) × Retention Days × (Replicas + 1) × 1.25
```

The 1.25 multiplier accounts for the 15% disk watermark threshold and a 10% error margin. This formula is the baseline for all hot-tier capacity planning.

---

## Loki + Grafana: Deployment, Label Strategy, and Storage

### Architecture Overview

Grafana Loki indexes only log metadata labels, not log content, and stores compressed chunks in object stores (S3, GCS, Azure Blob) or local filesystem. [Grafana's Loki documentation](https://grafana.com/docs/loki/latest/) describes this as making Loki "incredibly cost-efficient and easy to scale" relative to full-text indexing systems.

Loki's stack consists of three components as of 2025: **Grafana Alloy** (log agent, replacing deprecated Promtail), **Loki** (storage and query engine), and **Grafana** (visualization). Alloy replaced Promtail because Promtail was deemed feature-complete, with all future log collection development consolidated into Alloy per the [Grafana Loki GitHub repository](https://github.com/grafana/loki).

### Deployment Modes

[Grafana's deployment modes documentation](https://grafana.com/docs/loki/latest/get-started/deployment-modes/) defines two production-relevant modes:

**Simple Scalable Deployment (SSD):**
- Default Helm chart configuration
- Separates execution into three independently scalable targets: write (Distributor + Ingester StatefulSet), read (Query Frontend + Querier Deployment), and backend (Compactor, Index Gateway, Query Scheduler)
- Scales to approximately **1 TB of logs per day**
- Requires a reverse proxy in front of Loki to route API requests to read or write nodes
- Note: SSD mode is scheduled for deprecation before Loki 4.0

**Microservices Mode:**
- Intended for deployments exceeding ~1 TB/day
- Runs 12+ distinct processes independently
- Most complex to operate; designed specifically for Kubernetes
- Enables the most granular independent component scaling

### Label Strategy

Loki's cost structure is directly determined by label cardinality. A small index with low-cardinality labels (e.g., `namespace`, `app`, `pod`, `env`) plus highly compressed chunks is the operational target. [Loki's storage documentation](https://grafana.com/docs/loki/latest/configure/storage/) notes that "a small index and highly compressed chunks simplifies the operation and significantly lowers the cost."

High-cardinality labels (user IDs, trace IDs, request IDs) should never be used as Loki labels; they belong in structured log lines queried via LogQL filter expressions. This is the single most consequential operational decision in a Loki deployment.

### Chunk Storage and Retention

Starting with Loki 2.8, [the TSDB index is the recommended schema](https://grafana.com/docs/loki/latest/configure/storage/), storing indexes in object storage alongside chunks and enabling better retention handling. Larger chunks reduce object storage API call costs, with [advanced deployments targeting 5–10 minute chunk windows](https://medium.com/@sre999/loki-advanced-concepts-scaling-logs-like-a-pro-retention-cost-optimization-advanced-logql-55cd954bad58) versus the default 1–2 minutes.

Retention is managed through the Compactor process. [Grafana's retention documentation](https://grafana.com/docs/loki/latest/operations/storage/retention/) specifies that when retention is enabled, the Compactor identifies data outside the configured retention period, removes corresponding index entries, and deletes underlying chunk objects asynchronously. The `retention_delete_delay` parameter provides a safety buffer before actual deletion executes.

Per-tenant retention overrides allow ISVs to enforce different retention periods per customer — a critical capability for multi-tier SaaS offerings.

---

## Log Collection Agents: Fluent Bit, Fluentd, and Vector

### Agent Deployment Pattern

Log collection agents run as DaemonSets on every Kubernetes node, reading container log files from the node filesystem and forwarding to a central aggregator or directly to the storage backend. [Fluent Bit's Kubernetes documentation](https://docs.fluentbit.io/manual/installation/downloads/kubernetes) describes it as designed for "high-performance log forwarding at every Kubernetes node."

### Resource Overhead Comparison

[A 2025 benchmark study by Onidel](https://onidel.com/blog/log-shipping-benchmark-2025) measured the following per-agent resource profiles:

| Agent | Memory Footprint | CPU Usage | Architecture |
|-------|-----------------|-----------|-------------|
| Fluent Bit | 50–100 MB RAM | 5–15% CPU | C, optimized for edge/constrained environments |
| Vector | 100–200 MB RAM | 10–20% CPU | Rust, balanced with advanced transformation |
| Logstash | 500 MB–2 GB RAM | 20–40% CPU | JVM (Ruby + Java), richest plugin ecosystem |

Fluent Bit's binary footprint is approximately **650 KB**, making it the standard choice for Kubernetes node agents. [Vector's capacity planning documentation](https://vector.dev/docs/setup/going-to-prod/sizing/) reports:

- Unstructured log throughput: **~10 MiB/s per vCPU**
- Structured log throughput: **~25 MiB/s per vCPU**
- Recommended aggregator instance: 8 vCPUs, 16 GiB RAM (AWS c6i.2xlarge equivalent)

### Real-World Migration Data

A [documented migration from Fluentd to Vector](https://vdubov.dev/posts/fluentd-to-vector/) showed:
- Before: 9× m5.large + 5× r5.large EC2 instances — approximately **$1,060+/month**
- After: 6× t3.small instances — under **$100/month**
- Reduction: **over 90%** in log collection infrastructure cost

### Configuration Management at Scale

All three agents support configuration via Kubernetes ConfigMaps, enabling GitOps-managed agent configuration. Fluent Bit and Fluentd both support [multi-pipeline configurations](https://medium.com/@bavicnative/logging-in-kubernetes-fluentd-fluent-bit-loki-a-deep-dive-into-centralized-logging-0f384326a560) where different log streams route to different backends, enabling per-tenant log routing from the agent layer.

---

## Storage Scaling: Volume Estimation, Retention, and Tiering

### Log Volume Estimation

Raw log volumes vary significantly by application type. A rule-of-thumb baseline for SaaS applications is 0.5–2 KB per log event, with high-throughput microservices generating 500–2,000 events per second per pod. For a 50-pod deployment averaging 1 KB events at 500 events/sec, raw volume is approximately **25 GB/hour** before compression. Elasticsearch achieves compression ratios of approximately 3:1 to 5:1 on structured JSON logs, reducing effective storage to 5–8 GB/hour.

Using [Elastic's storage formula](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics), a deployment logging 50 GB/day with 30-day retention and one replica requires:

```
50 GB/day × 30 days × 2 replicas × 1.25 = 3,750 GB total hot storage
```

### Hot-Warm-Cold-Frozen Tiering

[Elasticsearch data tier documentation](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers) defines four tiers:

| Tier | Access Pattern | Hardware Profile | Memory:Data Ratio |
|------|---------------|------------------|-------------------|
| Hot | Active writes + frequent reads | Fast NVMe SSDs, high CPU | 1:30 |
| Warm | Read-only, frequent queries | Moderate SSDs, less CPU | 1:160 |
| Cold | Infrequent reads, searchable snapshots | HDD or object-backed | ~50% reduction vs warm with replica |
| Frozen | Rare reads, on-demand load | Object storage only | Up to 20× capacity vs warm |

[The Elasticsearch ILM documentation](https://www.elastic.co/blog/implementing-hot-warm-cold-in-elasticsearch-with-index-lifecycle-management) notes that hot-warm-cold architecture "can reduce costs by 40–70% compared to all-hot architecture." ILM policies automate the transition between tiers based on age, size, or document count thresholds, including rollover, force-merge, shrink, and delete actions.

### Compression

Elasticsearch applies LZ4 compression by default; best_compression (DEFLATE) is configurable for cold/warm tiers at the cost of additional CPU during decompression. Loki applies gzip compression to chunks by default before writing to object storage, achieving compression ratios that make S3 storage costs negligible at scale.

---

## Performance: Ingestion Rates, Query Optimization, and Index Tuning

### Ingestion Throughput Limits

A single Logstash pipeline worker is CPU-bound and typically processes 10,000–20,000 events per second. Horizontal scaling via multiple Logstash instances behind a load balancer or message queue (Kafka, Redis) is required for sustained high-volume ingestion. [Logstash's deployment guide](https://www.elastic.co/guide/en/logstash/8.19/deploying-and-scaling.html) recommends this pattern for production deployments.

The [Elasticsearch benchmark suite](https://elasticsearch-benchmarks.elastic.co/) provides nightly benchmark data against the main branch, measuring throughput, latency, error rates, and resource utilization. For HTTP log data specifically, the optimal bulk index request size is **16,000 documents** before performance plateaus.

### Query Performance at Scale

Combined indexing + query workloads reduce individual throughput: in the [Elastic three-node benchmark](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics), running 1,000 search operations/sec concurrently with bulk indexing dropped indexing throughput from 220K to approximately 173K events/sec.

[Opster's query optimization guidance for 2025](https://queryquotient.com/blog/elasticsearch-query-performance-optimization-guide-2025) identifies the following primary query performance levers:
- Shard count aligned to data volume (avoid oversharding)
- Force-merge warm/cold indices to 1 segment per shard
- Use `filter` context (not `query` context) for non-relevance log searches to exploit caching
- Field data types: use `keyword` not `text` for log fields queried with terms aggregations

### Loki Query Characteristics

Loki's LogQL queries scan chunks rather than an inverted index. Query performance is therefore label-selectivity-dependent: a query filtering on `namespace="production"` that matches 10% of stored chunks will complete in seconds; a query on a high-cardinality label that matches 90% of chunks will scan nearly all stored data. This characteristic makes label schema design the primary query performance lever in Loki, not hardware configuration.

---

## Multi-Tenant Log Isolation

### Elasticsearch Multi-Tenancy Patterns

Elasticsearch supports two primary multi-tenancy models for ISVs:

1. **Index-per-tenant:** Each tenant's logs stored in dedicated indices (e.g., `logs-tenant-a-2025.02.18`). Provides complete data isolation, independent retention, and per-tenant ILM policies. Increases total shard count proportionally to tenant count — a critical constraint at the 1,000-shard-per-node limit.

2. **Shared index with document-level filtering:** A `tenant_id` field on every document with Elasticsearch Document Level Security (DLS) enforces row-level access. Reduces shard overhead but requires Elastic Security or Elasticsearch's native DLS feature, both available only in licensed tiers.

For ISVs with data residency requirements, the index-per-tenant model is the only viable option, as it enables tenant data placement on specific nodes via custom allocation rules.

### Loki Multi-Tenancy

Loki's multi-tenancy is enforced via HTTP header. [Grafana's multi-tenancy documentation](https://grafana.com/docs/loki/latest/operations/multi-tenancy/) specifies:

- Enabled by setting `auth_enabled: true` in Loki configuration
- Every API request must include `X-Scope-OrgID: <tenant-id>` header
- Requests and data for tenant A are isolated from tenant B at the ingestion and query layers
- Tenant IDs support alphanumeric characters plus `!`, `-`, `_`, `.`, `*`, `'`, `(`, `)` up to **150 bytes**
- Multi-tenant queries spanning tenants are supported with pipe-delimited headers (e.g., `X-Scope-OrgID: A|B`) when `multi_tenant_queries_enabled: true`

An [AWS Open Source blog post on regulated multi-tenant Loki environments](https://aws.amazon.com/blogs/opensource/how-to-manage-grafana-and-loki-in-a-regulated-multitenant-environment/) documents the pattern of using kube-rbac-proxy in front of the Loki query endpoint to enforce Kubernetes RBAC-based authentication before tenant-scoped queries reach Loki.

Per-tenant configuration overrides in Loki's `limits_config` section allow ISVs to set independent ingestion rate limits, burst sizes, max active streams, and retention periods per customer — a critical capability for enforcing SLA tiers.

### Data Residency Compliance

For ISVs subject to GDPR, HIPAA, or sovereignty mandates, Elasticsearch's index-per-tenant model combined with node allocation filtering provides a verifiable data residency boundary. Loki's object storage backend (S3 with region locking, for example) provides equivalent guarantees when tenants are mapped to separate storage buckets or prefixes. [UNVERIFIED: Neither Elastic nor Grafana Labs publishes a formal data residency compliance certification specific to their logging products; customers must rely on infrastructure-level controls and their own attestations.]

---

## Log Pipeline Reliability: Buffering, Backpressure, and Delivery Guarantees

### Logstash Persistent Queue

[Elastic's persistent queue documentation](https://www.elastic.co/docs/reference/logstash/persistent-queues) defines the delivery guarantee model:

- **Guarantee type:** At-least-once delivery
- **Mechanism:** Events are written to disk before processing; an event is acknowledged only after filters and outputs have completed
- **Durability setting:** `queue.checkpoint.writes: 1` required for full at-least-once guarantee (each write is checkpointed immediately)
- **Trade-off:** Higher durability increases disk I/O overhead; default checkpointing batches writes for performance

Blocked pipelines result from backpressure when output plugins cannot keep up with input rate. [Logstash's pipeline health metrics](https://github.com/elastic/logstash/issues/14463) expose a `queue_backpressure` flow metric that quantifies time inputs spend blocked pushing to the queue.

### Logstash Dead Letter Queue (DLQ)

The [Logstash DLQ](https://www.elastic.co/guide/en/logstash/8.19/dead-letter-queues.html) captures events that encounter processing errors and stores them in a separate on-disk location for later inspection and replay. Events in the DLQ retain their original data plus diagnostic fields indicating failure reason. The DLQ prevents malformed events from blocking the primary pipeline while preserving data for forensic recovery.

### Fluentd and Fluent Bit Buffering

[Atatus's Fluentd vs Logstash comparison (2025)](https://www.atatus.com/blog/fluentd-vs-logstash/) notes that Fluentd includes "built-in buffering, retry logic, and backpressure handling" with both memory and file buffer options, configurable retry intervals, and explicit backpressure propagation upstream. This makes Fluentd's reliability model more granular than Logstash's persistent queue approach.

Fluent Bit supports both in-memory and disk-backed buffering. For production deployments, file-backed buffering is required to survive pod restarts without log loss. Buffer sizing should account for expected downstream unavailability windows — a 10-minute buffer at 50 MB/sec requires 30 GB of disk buffer capacity.

### Vector Backpressure

[Vector's documentation](https://vector.dev/docs/setup/going-to-prod/sizing/) recommends provisioning disk buffers at **2× expected maximum throughput** to prevent bottlenecks during downstream degradation. Vector applies backpressure upstream when disk buffers reach capacity, creating a signal chain from storage layer back to sources. [A documented issue in Vector's GitHub](https://github.com/vectordotdev/vector/issues/23783) shows the backpressure mechanism operating correctly when disk buffers on sinks are configured — sources see reduced ingestion rates matching the constrained output path.

---

## Operational Comparison: Self-Hosted vs Managed Logging Services

### Capability Comparison Table

| Capability | On-Premises | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native |
|------------|-------------|-----------------------------------|--------------|
| **Ingestion Scaling** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
|  | Manual Logstash/Loki horizontal scaling; capacity planning required | HPA for Loki read path; Elasticsearch requires manual data node scaling | Auto-scales transparently (CloudWatch, Azure Monitor, Cloud Logging) |
|  | Kafka/Redis as message queue buffer | Kafka on EKS as buffer layer | Managed intake (Kinesis, Event Hub) |
|  | Est. FTE: 0.5 dedicated | Est. FTE: 0.3 | Est. FTE: 0.0 |
| **Storage Management** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
|  | Hot/warm/cold tiering; ILM policy authoring; disk provisioning; snapshot management | S3/GCS as Loki chunk backend; EBS for Elasticsearch hot tier | Per-GB billing with configurable retention; no capacity planning |
|  | Elasticsearch ILM, Curator | Loki compactor + S3 lifecycle | CloudWatch retention policies; Azure Monitor data retention settings |
|  | Est. FTE: 0.3 | Est. FTE: 0.2 | Est. FTE: 0.0 |
| **Query Performance** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
|  | Shard optimization; force-merge scheduling; index template tuning | Same as on-premises for Elasticsearch; Loki chunk scan performance | Managed query engines (CloudWatch Logs Insights, Log Analytics) |
|  | Kibana, Elasticsearch query DSL | Grafana + LogQL; Kibana | CloudWatch Logs Insights; Azure Log Analytics; GCP Log Explorer |
|  | Est. FTE: 0.2 | Est. FTE: 0.2 | Est. FTE: 0.0 |
| **Multi-Tenant Isolation** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
|  | Index-per-tenant or DLS; custom allocation rules for data residency | Loki X-Scope-OrgID + kube-rbac-proxy; namespace-scoped collection | IAM/RBAC policies; workspace isolation (Log Analytics workspaces) |
|  | Elasticsearch security, Kibana Spaces | Loki multi-tenancy config; Grafana RBAC | AWS Organizations, Azure RBAC, GCP IAM |
|  | Est. FTE: 0.2 | Est. FTE: 0.15 | Est. FTE: 0.05 |
| **Pipeline Reliability** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
|  | Persistent queue tuning; DLQ monitoring; buffer sizing; agent upgrades | Same pipeline complexity; K8s restarts add agent lifecycle management | Managed intake; no buffer sizing; SLA-backed delivery |
|  | Logstash PQ; Fluentd file buffers; Kafka | Vector disk buffers; Fluent Bit on nodes | CloudWatch agent; Azure Monitor agent |
|  | Est. FTE: 0.3 | Est. FTE: 0.2 | Est. FTE: 0.0 |
| **Cost at 100 GB/day** | Difficulty: 2/5 (after setup) | Difficulty: 2/5 | Difficulty: 1/5 (operational) |
|  | Hardware: $500–1,500/month; very low per-GB variable cost | Compute + S3: ~$300–600/month | CloudWatch: ~$1,665/month; Azure Monitor: ~$230/month (at $2.30/GB) |
|  | 3–5 Elasticsearch data nodes or Loki + object store | Loki on managed K8s | Pay-as-you-go; no infra management |
|  | Est. FTE: 1.5–2.0 total | Est. FTE: 1.0–1.3 total | Est. FTE: 0.05–0.1 total |

### What Managed Services Eliminate

**CloudWatch Logs** ([pricing source](https://cloudchipr.com/blog/cloudwatch-pricing)):
- Ingestion: $0.50/GB standard; $0.25/GB infrequent access
- Storage: $0.03/GB/month
- Queries: $0.005/GB scanned
- Free tier: 5 GB/month ingestion + storage + queries combined
- Eliminates: capacity planning, cluster upgrades, shard management, agent lifecycle, DLQ monitoring, ILM policy authoring

**Azure Monitor Logs** ([Microsoft pricing](https://azure.microsoft.com/en-us/pricing/details/monitor/)):
- Analytics Logs: approximately $2.30/GB ingested
- Commitment tiers save up to 30% vs pay-as-you-go
- Eliminates: same operational surface as CloudWatch; adds deep Azure service integration

**Google Cloud Logging** ([GCP pricing](https://cloud.google.com/products/observability/pricing)):
- No charge for logs stored in the Required log bucket
- Charges apply for _Default bucket and user-defined buckets
- Eliminates: storage management, retention policy enforcement, cluster maintenance

**[Comparison source: oneuptime.com Loki vs CloudWatch, 2026](https://oneuptime.com/blog/post/2026-01-21-loki-vs-cloudwatch/view):**
- Self-hosted Loki at 100 GB/day: ~$300/month (compute $200–400 + S3 ~$7)
- CloudWatch at 100 GB/day: ~$1,665/month
- Self-hosted advantage: **75–90% cost reduction at scale**
- Self-hosted maintenance burden: **2–4 hours/week**

At 1 TB/day: CloudWatch ~$16,650/month vs Loki self-hosted ~$1,500/month.

### FTE Estimation Summary

**Assumptions:**
- Mid-size ISV: 20–50 application pods, 3–10 customers (tenants), 10–100 GB/day log volume
- On-call burden: 0.1–0.2 FTE equivalent factored into ranges
- Excludes initial setup/migration effort (typically 4–8 weeks of 1 FTE for ELK; 2–4 weeks for Loki)

| Deployment Model | Steady-State FTE (Logging Only) | On-Call Burden | Notes |
|-----------------|--------------------------------|----------------|-------|
| On-Premises (ELK) | 1.5–2.0 | 0.2 | Cluster upgrades, ILM tuning, hardware provisioning |
| On-Premises (Loki) | 1.0–1.5 | 0.15 | Label schema management, compactor monitoring, object store ops |
| Managed Kubernetes (Loki + S3) | 0.8–1.2 | 0.1 | K8s managed; Loki ops remain; agent lifecycle on nodes |
| Cloud-Native (CloudWatch/Azure Monitor) | 0.05–0.1 | 0.02 | Alert configuration, retention policy review only |

[UNVERIFIED: FTE ranges are synthesized from industry practitioner discussions and vendor sizing guides, not from a single published benchmarking study. Actual staffing depends heavily on team Elasticsearch/Loki expertise, degree of IaC automation, and customer SLA requirements.]

---

## Key Takeaways

- **ELK Stack at production scale demands dedicated engineering capacity.** A 100 GB/day deployment requires 15 Elasticsearch nodes across hot and warm tiers, active ILM policy management, and shard sizing discipline — the three-node benchmark ceiling of 220,000 events/sec requires optimal bulk sizing (16,000 docs/request) and degrades measurably under concurrent query load. ([Elastic Blog](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics))

- **Loki achieves 75–90% cost reduction versus CloudWatch at 100+ GB/day, but operational burden does not disappear.** Self-hosted Loki at 100 GB/day costs approximately $300/month versus $1,665/month for CloudWatch Logs, but requires 2–4 hours/week of maintenance including label schema governance, compactor monitoring, and object store retention management. ([oneuptime.com](https://oneuptime.com/blog/post/2026-01-21-loki-vs-cloudwatch/view))

- **Agent selection has measurable infrastructure cost impact.** Migrating from Fluentd to Vector reduced one organization's log collection EC2 spend by over 90% ($1,060/month to under $100/month). Fluent Bit remains the preferred Kubernetes node agent at 50–100 MB RAM and 5–15% CPU; Logstash's JVM footprint (500 MB–2 GB RAM) makes it inappropriate as a per-node DaemonSet. ([vdubov.dev](https://vdubov.dev/posts/fluentd-to-vector/), [onidel.com](https://onidel.com/blog/log-shipping-benchmark-2025))

- **Multi-tenant ISVs must architect for isolation from day one.** Elasticsearch's index-per-tenant model and Loki's `X-Scope-OrgID` header enforcement are both production-viable, but retrofitting tenant isolation into a shared logging deployment is expensive. The shard count growth (1,000 non-frozen shards per node limit) in Elasticsearch requires capacity planning proportional to tenant count, not just log volume. ([Elastic shard sizing docs](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards), [Grafana Loki multi-tenancy docs](https://grafana.com/docs/loki/latest/operations/multi-tenancy/))

- **The operational crossover point is approximately 50–100 GB/day.** Below 50 GB/day, managed services (CloudWatch, Azure Monitor) are cost-competitive when operational FTE is monetized at $150–200/hour. Above 100 GB/day, self-hosted solutions generate meaningful savings that justify the engineering investment — but only when the ISV already has Kubernetes and observability engineering capacity available, not as a net-new staffing requirement.

---

## Sources

1. [Benchmarking and sizing your Elasticsearch cluster for logs and metrics — Elastic Blog](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics)
2. [Elasticsearch data tiers: hot, warm, cold, and frozen storage explained — Elastic Docs](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers)
3. [Size your shards — Elastic Docs](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards)
4. [How we sped up data ingestion in Elasticsearch 8.6, 8.7, and 8.8 — Elastic Blog](https://www.elastic.co/blog/data-ingestion-elasticsearch)
5. [Implementing Hot-Warm-Cold in Elasticsearch with Index Lifecycle Management — Elastic Blog](https://www.elastic.co/blog/implementing-hot-warm-cold-in-elasticsearch-with-index-lifecycle-management)
6. [Persistent queues (PQ) — Logstash Reference, Elastic Docs](https://www.elastic.co/docs/reference/logstash/persistent-queues)
7. [Dead letter queues (DLQ) — Logstash Reference 8.19, Elastic](https://www.elastic.co/guide/en/logstash/8.19/dead-letter-queues.html)
8. [Deploying and Scaling Logstash — Logstash Reference 8.19, Elastic](https://www.elastic.co/guide/en/logstash/8.19/deploying-and-scaling.html)
9. [Grafana Loki documentation — Grafana Labs](https://grafana.com/docs/loki/latest/)
10. [Loki deployment modes — Grafana Loki documentation](https://grafana.com/docs/loki/latest/get-started/deployment-modes/)
11. [Storage — Grafana Loki documentation](https://grafana.com/docs/loki/latest/configure/storage/)
12. [Log retention — Grafana Loki documentation](https://grafana.com/docs/loki/latest/operations/storage/retention/)
13. [Manage tenant isolation — Grafana Loki documentation](https://grafana.com/docs/loki/latest/operations/multi-tenancy/)
14. [Grafana Loki GitHub repository](https://github.com/grafana/loki)
15. [Loki vs CloudWatch Logs: Self-Hosted vs Managed Logging — oneuptime.com (2026)](https://oneuptime.com/blog/post/2026-01-21-loki-vs-cloudwatch/view)
16. [Vector sizing and capacity planning — Vector documentation](https://vector.dev/docs/setup/going-to-prod/sizing/)
17. [Cutting Cloud Costs: Migrating from Fluentd to Vector.dev — vdubov.dev](https://vdubov.dev/posts/fluentd-to-vector/)
18. [Log Shipping Benchmark 2025: Fluent Bit vs Vector vs Logstash — onidel.com](https://onidel.com/blog/log-shipping-benchmark-2025)
19. [Fluent Bit Kubernetes documentation — Fluent Bit Manual](https://docs.fluentbit.io/manual/installation/downloads/kubernetes)
20. [Fluentd vs Logstash: In-Depth Comparison 2025 — Atatus](https://www.atatus.com/blog/fluentd-vs-logstash/)
21. [Kubernetes Logging with Fluentd, Fluent Bit & Loki — Medium/@bavicnative](https://medium.com/@bavicnative/logging-in-kubernetes-fluentd-fluent-bit-loki-a-deep-dive-into-centralized-logging-0f384326a560)
22. [How to Manage Grafana and Loki in a Regulated Multitenant Environment — AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/how-to-manage-grafana-and-loki-in-a-regulated-multitenant-environment/)
23. [Loki Advanced Concepts: Scaling Logs Like a Pro — Medium/@sre999](https://medium.com/@sre999/loki-advanced-concepts-scaling-logs-like-a-pro-retention-cost-optimization-advanced-logql-55cd954bad58)
24. [CloudWatch Pricing Explained: Ultimate Guide 2025 — cloudchipr.com](https://cloudchipr.com/blog/cloudwatch-pricing)
25. [Azure Monitor Pricing — Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/monitor/)
26. [Google Cloud Logging Pricing — Google Cloud](https://cloud.google.com/products/observability/pricing)
27. [Elasticsearch Query Optimization Guide 2025 — queryquotient.com](https://queryquotient.com/blog/elasticsearch-query-performance-optimization-guide-2025)
28. [Elasticsearch Benchmarks — elastic.co](https://elasticsearch-benchmarks.elastic.co/)
29. [Vector backpressure issue documentation — vectordotdev/vector GitHub](https://github.com/vectordotdev/vector/issues/23783)
30. [Setting up Multi-Tenant Logging with Loki on Kubernetes — konst.fish](https://konst.fish/blog/Multi-Tenant-Loki-on-Kubernetes)
