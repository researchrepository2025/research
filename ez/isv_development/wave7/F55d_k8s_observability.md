# F55d: Kubernetes Observability Stack

**Research Question:** What are the requirements, operational characteristics, and trade-offs of
running the Kubernetes observability stack (Prometheus Operator, Grafana, Loki, Tempo) on managed
K8s, and how does this compare to cloud-native observability services?

**Scope:** Managed Kubernetes (EKS/AKS/GKE) observability stack only. Cross-references: See
[F12/F20/F28] for cloud-native observability services; [F49-F51] for on-prem observability;
[F52] for K8s platform management.

---

## Executive Summary

The Kubernetes-native observability stack — built on Prometheus Operator, Grafana, Loki, and
Tempo — delivers a powerful, portable, and open-standards-based monitoring solution for ISVs
running on managed Kubernetes. This stack offers genuine multi-cloud portability and avoids
vendor lock-in, but carries meaningful operational overhead: a production-grade deployment
consumes 8–20 GB of cluster RAM before any application workloads are monitored, requires
dedicated expertise in PromQL, LogQL, and TraceQL, and demands active management of high-
availability extensions such as Thanos or Grafana Mimir for long-term metric storage. Cloud-
managed alternatives — Amazon Managed Prometheus, Azure Monitor Managed Prometheus, and GCP
Managed Prometheus — eliminate control-plane operations and retention management but introduce
per-sample ingestion costs that escalate sharply at enterprise scale: AWS charges $0.90 per 10
million samples ingested. The optimal strategy for most ISVs on managed Kubernetes is a hybrid:
use cloud-managed Prometheus for metrics ingestion (eliminating the Thanos/Mimir complexity),
self-managed Loki for cost-controlled log storage, and self-managed Tempo for traces, while
reserving fully cloud-native observability (CloudWatch, Azure Monitor, Cloud Operations Suite)
for environments where operational simplicity is the overriding priority.

---

## 1. Prometheus Operator on Managed Kubernetes

### 1.1 What the Operator Provides

The [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) creates,
configures, and manages Prometheus clusters atop Kubernetes. It provides a set of Custom
Resource Definitions (CRDs) that allow declarative configuration of metrics sources, alerting
rules, and Alertmanager deployments. The Operator continuously reconciles the scrape and rules
configuration based on the current state of objects in the Kubernetes API server.
[Source: prometheus-operator/prometheus-operator GitHub](https://github.com/prometheus-operator/prometheus-operator)

### 1.2 ServiceMonitor and PodMonitor CRDs

The two primary service-discovery CRDs are:

- **ServiceMonitor** — defines a Prometheus scrape target against a Kubernetes Service object.
  Correct choice when a Service already exists for the pods to be scraped.
- **PodMonitor** — targets Pods directly without requiring a Service object. Used for headless
  workloads or when a Service cannot be created.

[Source: ServiceMonitor & PodMonitor Configuration, DeepWiki](https://deepwiki.com/prometheus-operator/prometheus-operator/4.1-servicemonitor-and-podmonitor-configuration)
[Source: Rancher ServiceMonitor and PodMonitor docs](https://ranchermanager.docs.rancher.com/reference-guides/monitoring-v2-configuration/servicemonitors-and-podmonitors)

The Prometheus resource defines via label and namespace selectors which ServiceMonitor,
PodMonitor, Probe, and PrometheusRule objects should be associated with each Prometheus instance.
The Operator auto-generates scrape configuration from these resources, eliminating hand-crafted
`prometheus.yml` files.

### 1.3 High Availability and Long-Term Storage: Thanos vs. Mimir

Prometheus is single-node by design; scaling for HA and long-term retention requires an
extension layer. In 2025, three solutions dominate: Thanos, Grafana Mimir, and VictoriaMetrics.

**Thanos** uses a sidecar model: a sidecar container runs alongside each Prometheus pod,
uploading 2-hour TSDB blocks to object storage (S3, GCS, Azure Blob). A Thanos Querier fans
out queries across multiple Prometheus instances and against object storage.
[Source: Thanos — Highly available Prometheus setup](https://thanos.io/v0.10/thanos/getting-started.md/)

**Grafana Mimir** is a horizontally scalable, multi-tenant, long-term storage system for
Prometheus metrics. It uses RemoteWrite ingestion (no sidecar required) and stores data in
object storage. Mimir has been tested at 1 billion active series for a single tenant (3 billion
after replication).
[Source: grafana/mimir GitHub](https://github.com/grafana/mimir)

**Performance benchmarks (2025 comparison):**

| Metric | Thanos | Grafana Mimir | VictoriaMetrics |
|---|---|---|---|
| Ingestion throughput | Limited by Prometheus | 500K–2M samples/sec per ingester | Up to 1M samples/sec (single node) |
| 6h query latency | 200–250ms | 80–100ms | 20–50ms (recent data) |
| 7d query latency | 2,000–4,000ms | 80–100ms | 100–500ms |
| Object storage compression | 2–4x | 2–3x | Up to 10x |
| Min. production resource footprint | 4 vCPUs, 8 GB RAM | 8 vCPUs, 16 GB RAM | 2 vCPUs, 4 GB RAM |
| Multi-tenancy | Logical separation | Native tenant isolation | Limited |
| CNCF status | Incubating | Grafana Labs-backed | CNCF sandbox |

[Source: Prometheus Storage Comparison 2025, Onidel](https://onidel.com/blog/prometheus-storage-comparison-2025)
[Source: Thanos vs Mimir community discussion, Grafana Labs Forum](https://community.grafana.com/t/thanos-vs-mimir-choosing-the-right-prometheus-extension/157751)

**Mimir 3.0 (2025):** The new query engine delivers 92% less memory usage and 38% faster
execution compared to the prior version.
[Source: Mimir 3.0 preview, Grafana Labs GrafanaCon 2025](https://grafana.com/events/grafanacon/2025/preview-mimir-3.0-release-for-metrics/)

**ISV recommendation signal:** A production migration from Thanos to Mimir at Wise (fintech)
demonstrated measurable cost savings, improved reliability, and enhanced performance due to
scalability, flexibility, and operational simplicity.
[Source: Grafana Mimir Compaction: From Bottleneck to Savings, Wise Engineering](https://medium.com/wise-engineering/grafana-mimir-compaction-from-bottleneck-to-savings-b26c6b0125a6)

---

## 2. Grafana on Kubernetes

### 2.1 Grafana Operator

The [Grafana Operator](https://github.com/grafana/grafana-operator) (v5.21.4 as of early 2025)
manages Grafana instances, dashboards, and datasources through Kubernetes custom resources. It
enables multi-instance and multi-namespace Grafana deployments and integrates with GitOps
workflows (ArgoCD, Flux CD).
[Source: grafana/grafana-operator GitHub](https://github.com/grafana/grafana-operator)

Key CRDs provided by the Grafana Operator:
- **GrafanaInstance** — deploys and configures a Grafana server
- **GrafanaDashboard** — defines dashboards as code (JSON, Jsonnet, remote URL, or
  grafana.com catalog ID)
- **GrafanaDatasource** — configures datasource connections declaratively
- **GrafanaFolder** — organizes dashboards into folder hierarchies

[Source: Manage folders, datasources, and dashboards using Grafana Operator](https://grafana.com/docs/grafana/latest/as-code/infrastructure-as-code/grafana-operator/operator-dashboards-folders-datasources/)

### 2.2 Dashboard and Alerting Management on K8s

Grafana provisioning allows datasources, dashboards, and alert policies to be defined as YAML
files mounted into the container — fully compatible with Kubernetes ConfigMaps and GitOps
pipelines.
[Source: Provision Grafana, Grafana documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/)

The Grafana Operator can be used to manage Amazon Managed Grafana workspaces from within a
Kubernetes cluster using the same CRD-based workflow — bridging self-hosted and cloud-managed
Grafana models.
[Source: Using Open Source Grafana Operator to manage Amazon Managed Grafana, AWS Blog](https://aws.amazon.com/blogs/mt/using-open-source-grafana-operator-on-your-kubernetes-cluster-to-manage-amazon-managed-grafana/)

---

## 3. Loki on Kubernetes

### 3.1 Architecture

[Grafana Loki](https://grafana.com/oss/loki/) is a horizontally scalable, highly available,
multi-tenant log aggregation system inspired by Prometheus. Its core architectural distinction
is that it **does not index the contents of logs**, only a set of labels for each log stream.
This label-only indexing makes Loki significantly more cost-efficient than full-text indexing
solutions (ElasticSearch, CloudWatch Logs Insights) but shifts query complexity to LogQL filters
on log line content at query time.

### 3.2 Storage Backend

**Supported production backends (2025):**
- Amazon S3
- Google Cloud Storage (GCS)
- Azure Blob Storage
- IBM Cloud Object Storage
- MinIO (S3-compatible, for on-prem or Kubernetes-local object store)

**Deprecated:** Cassandra, BigTable, DynamoDB, BoltDB (no longer recommended as of Loki 2.8+).

[Source: Storage, Grafana Loki documentation](https://grafana.com/docs/loki/latest/configure/storage/)

**Recommended index store:** TSDB (introduced in Loki 2.8). The [TSDB single store](https://grafana.com/docs/loki/latest/operations/storage/tsdb/) stores index files in the same object store as chunks, eliminates the need for a separate index backend, and supports Dynamic Query Sharding based on estimated data volume per shard (target: 300–600 MB per shard). Schema v13 is the current recommended configuration.

### 3.3 Label Strategy

Effective Loki label strategy is critical to avoiding index bloat and query performance
degradation. Best practice (2025):

**Recommended labels (low cardinality):** `namespace`, `pod`, `job`, `env`, `app`

**Anti-pattern (high cardinality — avoid as labels):** `request_id`, `user_id`, `session_id`,
`trace_id` — these should be embedded in log line content and searched via LogQL filter
expressions, not label matchers.

[Source: Grafana Loki Architecture: A Comprehensive Guide, DevOpsCube](https://devopscube.com/grafana-loki-architecture/)

### 3.4 Retention

Retention in Grafana Loki is managed by the [Compactor](https://grafana.com/docs/loki/latest/operations/storage/retention/). By default, `compactor.retention-enabled` is false, meaning logs are retained indefinitely. The Compactor supports granular retention policies at per-tenant or per-stream level. The Compactor must run as a StatefulSet with persistent storage for marker files.

For object storage backends, Loki performs retention-driven deletion natively; bucket lifecycle
rules may be added as a secondary safeguard.

### 3.5 Loki vs. Cloud-Native Logging Services

| Dimension | Loki (self-managed on K8s) | AWS CloudWatch Logs | Azure Monitor / Log Analytics | GCP Cloud Logging |
|---|---|---|---|---|
| Indexing model | Label-only (log content unindexed) | Full-text indexed | KQL full-text indexed | Full-text indexed |
| Query language | LogQL | CloudWatch Logs Insights | KQL (Kusto) | Log Explorer (SQL-like) |
| Multi-cloud portability | Yes | AWS only | Azure + Arc hybrid | GCP only |
| Retention management | Self-managed via Compactor | Configurable, paid per GB-month | Configurable, paid per GB | Configurable, paid per GB |
| Cost model | Object storage cost only | Per GB ingested + stored + queried | Per GB ingested + stored | Per GB ingested + stored |
| Operational burden | High (own the stack) | Low (fully managed) | Low (fully managed) | Low (fully managed) |
| Alert integration | Grafana Alerting | CloudWatch Alarms | Azure Monitor Alerts | Cloud Alerting |

[Source: Amazon CloudWatch Deep Dive, blog.greeden.me](https://blog.greeden.me/en/2025/11/14/amazon-cloudwatch-deep-dive-a-complete-guide-to-monitoring-logs-metrics-design-compared-with-cloud-monitoring-gcp-and-azure-monitor/)
[Source: What Is Grafana Loki? A Guide to Effective Log Aggregation, Middleware.io](https://middleware.io/blog/grafana-loki/)

---

## 4. Grafana Tempo on Kubernetes

### 4.1 Architecture

[Grafana Tempo](https://grafana.com/docs/tempo/latest/) is a high-volume, minimal-dependency
distributed tracing backend. Its defining characteristic is that it **requires only object
storage to operate** — there is no separate index store, making it highly cost-efficient. Tempo
ingests traces in Jaeger, OpenTelemetry, and Zipkin formats.
[Source: Grafana Tempo OSS](https://grafana.com/oss/tempo/)

**Core components in distributed mode:**
- **Distributor** — accepts incoming spans, routes to ingesters via consistent hash ring
- **Ingester** — buffers spans, writes to object storage in blocks
- **Querier** — searches object storage blocks plus in-memory ingester data
- **Query Frontend** — shards queries, caches results
- **Compactor** — merges and compacts blocks in object storage

[Source: Tempo architecture, Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/introduction/architecture/)

### 4.2 Storage Format: vParquet Evolution

Tempo uses [Apache Parquet](https://grafana.com/blog/new-in-grafana-tempo-2-0-apache-parquet-as-the-default-storage-format-support-for-traceql/) as its block format. The current version trajectory:

- **vParquet4** — current default (stable)
- **vParquet5** — production-ready as of Tempo 2.10; opt-in via storage configuration

**vParquet5 improvements:**
- Dedicated columns for array-valued attributes (e.g., HTTP headers)
- Virtual span row numbers accelerate resource-attribute-only filters
- Blob detection for high-cardinality attributes (UUIDs, stack traces) with optimized encoding
- Native `span:childCount` intrinsic support
- No migration of existing data required; Tempo reads vParquet4 blocks while writing vParquet5

[Source: Tempo 2.10 release, Grafana Labs](https://grafana.com/blog/tempo-2-10-release-all-the-latest-features/)
[Source: Version 2.10 release notes, Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/release-notes/v2-10/)

### 4.3 TraceQL

[TraceQL](https://grafana.com/docs/tempo/latest/traceql/) is Tempo's query language, inspired
by PromQL and LogQL. It enables precise span selection and trace retrieval. Key 2025 additions:

- **Nil queries** (`= nil` / `!= nil`) — identify spans with missing attributes for
  instrumentation auditing
- **`span:childCount` intrinsic** — detect N+1 query problems by finding leaf spans
- **`sum_over_time`** — compute cumulative sums (total bytes, error counts) within TraceQL
- **Sampling hints** — `with(sample=true)` for dynamic sampling; benchmarks show reduction from
  7.35s to 2.89s query time, with accuracy trade-off
- **MCP server** (experimental, Tempo 2.9) — LLMs and AI agents can query distributed tracing
  data via TraceQL without leaving the AI environment

[Source: Grafana Tempo 2.8 release, InfoQ](https://www.infoq.com/news/2025/07/grafana-tempo-2-8/)
[Source: Powerful new language features for TraceQL, Grafana Labs](https://grafana.com/whats-new/2025-05-08-powerful-new-language-features-for-traceql/)
[Source: Grafana Tempo 2.9 release notes, Grafana Labs](https://grafana.com/blog/2025/10/22/grafana-tempo-2-9-release-mcp-server-support-traceql-metrics-sampling-and-more/)

### 4.4 Tempo vs. Cloud-Native Tracing Services

| Dimension | Grafana Tempo (self-managed) | AWS X-Ray | Azure Application Insights | GCP Cloud Trace |
|---|---|---|---|---|
| Storage cost model | Object storage only | Per trace segment ingested | Per GB ingested (workspace-based) | Per million spans |
| Query language | TraceQL (powerful, open) | X-Ray Analytics | KQL + App Insights UI | Trace Explorer |
| OpenTelemetry native | Yes (OTLP) | Hybrid (ADOT distro) | SDK + distro integration | Native OTLP (Sept 2025) |
| Service map | Via Tempo metrics-generator | Built-in | Built-in | Built-in |
| Lock-in | None (open format) | AWS-proprietary | Azure-proprietary | GCP-proprietary |
| ML anomaly detection | No | No (CloudWatch integration) | Yes (Smart Detection) | No |
| Operational burden | High | Low | Low | Low |

[Source: Google Cloud Observability Adopts OpenTelemetry Protocol, InfoQ, Sept 2025](https://www.infoq.com/news/2025/09/gcp-opentelemetry-adoption/)
[Source: AWS X-Ray vs Azure Application Insights, StackShare](https://stackshare.io/stackups/aws-x-ray-vs-azure-application-insights)
[Source: End-to-End Distributed Tracing in Kubernetes with Grafana Tempo, Civo](https://www.civo.com/learn/distributed-tracing-kubernetes-grafana-tempo-opentelemetry)

---

## 5. OpenTelemetry on Kubernetes

### 5.1 Collector Deployment Modes

The [OpenTelemetry Operator](https://opentelemetry.io/docs/platforms/kubernetes/operator/) for
Kubernetes manages Collector deployments and application auto-instrumentation. The Collector
`spec.mode` field selects the deployment pattern:

**DaemonSet (Agent) Mode**
- One Collector pod per node
- Collects node-level metrics (CPU, memory, disk, network) via host metrics receiver
- Ideal for infrastructure telemetry and local log collection
- Resource overhead: constant per node, does not scale with pod count

**Sidecar Mode**
- One Collector container per application pod (injected automatically by the Operator)
- Kubernetes 1.29+ uses native sidecar containers: sidecars start before the main container
  and shut down after it
- Provides failure isolation — one misbehaving sidecar does not cascade
- Resource overhead: multiplies with pod count across the cluster
- Enabled by annotation: `sidecar.opentelemetry.io/inject: "true"`

**Deployment/StatefulSet (Gateway) Mode**
- Centralized Collector handling cluster-wide telemetry
- Combines with DaemonSet agents in the recommended two-tier architecture

[Source: OpenTelemetry Operator for Kubernetes](https://opentelemetry.io/docs/platforms/kubernetes/operator/)
[Source: Sidecar or Agent for OpenTelemetry: How to Decide, Last9](https://last9.io/blog/opentelemetry-sidecar-vs-agent/)
[Source: OpenTelemetry Collector deployment modes in Kubernetes, New Relic](https://newrelic.com/blog/how-to-relic/opentelemetry-collector-deployment-modes-in-kubernetes/)

### 5.2 Auto-Instrumentation

The Operator's auto-instrumentation feature injects language-specific SDKs into application pods
without code changes. Supported languages: Java, Python, Node.js, .NET, Go.

Example resource allocation for Python auto-instrumentation injection:
- CPU limit: 500m; CPU request: 50m
- Memory limit: 32Mi; Memory request: 32Mi

[Source: Injecting Auto-instrumentation, OpenTelemetry documentation](https://opentelemetry.io/docs/platforms/kubernetes/operator/automatic/)

### 5.3 Collector Resource Sizing

Throughput-based CPU sizing for a standard pipeline (per Collector instance):

| Throughput | Minimal Pipeline | Standard Pipeline | Complex Pipeline |
|---|---|---|---|
| 1,000 spans/sec | 0.5 cores | 1 core | 2 cores |
| 10,000 spans/sec | 1 core | 2 cores | 4 cores |
| 50,000 spans/sec | 2 cores | 4 cores | 8 cores |
| 100,000 spans/sec | 4 cores | 8 cores | 16 cores |

Production sizing tiers:
- **Small:** 1 core CPU, 512 MB RAM, 2 replicas
- **Medium:** 2 cores CPU, 2 GB RAM, 3 replicas
- **Large:** 4 cores CPU, 4 GB RAM, 5 replicas
- **Very Large:** 8+ cores CPU, 8+ GB RAM, 10+ replicas

DaemonSet agent pattern (recommended for node-level collection): 0.25–0.5 cores and 256–512 MB
memory per node for typical workloads.

[Source: How to Right-Size CPU and Memory for the OpenTelemetry Collector, OneUptime](https://oneuptime.com/blog/post/2026-02-06-right-size-cpu-memory-opentelemetry-collector/view)

---

## 6. Managed Prometheus and Grafana: Cloud-Provider Services

### 6.1 What Managed Services Simplify

All three major cloud providers offer managed Prometheus-compatible metrics services. These
services eliminate:
- Prometheus control plane management and upgrades
- Thanos/Mimir deployment and operation
- Long-term storage backend configuration (object store bucket management)
- HA configuration and replication
- Retention policy enforcement

**What remains ISV-managed:** scrape configuration (via RemoteWrite from self-managed agents or
cloud-native collectors), PromQL dashboards in Grafana, and alerting rules.

### 6.2 Amazon Managed Service for Prometheus (AMP)

- Native PromQL support; integrates with EKS, EC2, and CloudWatch
- Agentless collector option (scrapes EKS workloads without a Prometheus pod)
- Visualization requires separately purchased Amazon Managed Grafana

**Pricing (2025):**

| Dimension | Rate |
|---|---|
| Metric ingestion (first 2B samples/month) | $0.90 per 10 million samples |
| Storage | $0.03 per GB per month |
| Query samples processed | $0.10 per 1 billion samples |
| Agentless collector | $0.04 per collector-hour + $0.03 per 10M samples collected |
| Free tier (monthly) | 40M samples ingested, 200B QSP, 10 GB storage |

[Source: Amazon Managed Service for Prometheus Pricing](https://aws.amazon.com/prometheus/pricing/)
[Source: Amazon Managed Service for Prometheus product page](https://aws.amazon.com/prometheus/)

### 6.3 Azure Monitor Managed Prometheus

- Integrates with AKS and Azure Arc for hybrid environments
- Workspace-based architecture; tight integration with Azure Managed Grafana
- Enterprise security via Azure Active Directory authentication
- 24/7 incident response SLA for enterprise tiers

[Source: Running Prometheus in the Cloud with Managed Services, BinaryScripts 2025](https://binaryscripts.com/prometheus/2025/04/29/prometheus-in-the-cloud-running-prometheus-on-aws-azure-and-google-cloud-with-managed-services.html)

### 6.4 GCP Managed Service for Prometheus

- Native integration with GKE
- Combines PromQL Query API with Monarch's underlying storage
- Can query both Managed Service for Prometheus data and Google Cloud Monitoring data from a
  single PromQL interface

**Pricing comparison (relative, 2025):**
- AWS is approximately 4x more expensive than GCP at lower volumes for comparable metric counts
- GCP is approximately 12x more expensive than Sysdig for managed Prometheus at high volumes

[Source: How Much Does Your Managed Service for Prometheus Cost?, Sysdig](https://www.sysdig.com/blog/managed-service-prometheus)
[Source: Pricing comparison for Managed Prometheus, VictoriaMetrics](https://victoriametrics.com/blog/managed-prometheus-pricing/)

### 6.5 Grafana Operator Integration with Managed Services

The open-source Grafana Operator can manage Amazon Managed Grafana workspaces using the same
CRD-based workflow used for self-hosted Grafana. This enables a consistent GitOps dashboard-
as-code workflow regardless of whether the Grafana backend is self-hosted or cloud-managed.
[Source: Using Open Source Grafana Operator on your Kubernetes cluster to manage Amazon Managed Grafana, AWS Blog](https://aws.amazon.com/blogs/mt/using-open-source-grafana-operator-on-your-kubernetes-cluster-to-manage-amazon-managed-grafana/)

---

## 7. Resource Overhead: Monitoring the Monitors

### 7.1 Prometheus Memory Consumption

The established capacity planning rule of thumb: **3 kilobytes per active time series** (covers
time series data, metadata labels, and indexing structures).

| Active Series | Approximate Memory |
|---|---|
| 1,000 | ~3 MB |
| 100,000 | ~300 MB |
| 1,000,000 | ~3 GB |
| 10,000,000 | ~30 GB |

[Source: How to Reduce Prometheus High Memory Usage, SigNoz](https://signoz.io/guides/why-does-prometheus-consume-so-much-memory/)

**Cardinality explosion warning:** In a documented incident, a Prometheus deployment monitoring
1,000+ external services via ServiceMonitor consumed **10 CPU cores and 25 GB RAM** alongside
liveness errors and restarts. Switching to optimized static file configuration reduced this to
**less than 0.5 cores and 3 GB RAM**.
[Source: High CPU/Memory when monitoring 1000+ ServiceMonitor/Endpoints, GitHub Issues](https://github.com/prometheus-operator/prometheus-operator/issues/2866)

### 7.2 Kube-Prometheus-Stack Full Stack Footprint

The `kube-prometheus-stack` Helm chart deploys 8 components by default:
Prometheus, Prometheus Operator, Grafana, Alertmanager, node-exporter (DaemonSet),
kube-state-metrics, Prometheus Adapter, and Blackbox Exporter.

Representative memory usage for a moderate-scale cluster:
- **Prometheus Operator:** ~420–440 MiB
- **Prometheus server:** ~400–420 MiB (for a moderate metric count; scales with cardinality)
- **General guidance:** 2–4 GB RAM per 100,000 active series

[Source: Kube Prometheus Stack Guide 2025, Atmosly](https://atmosly.com/blog/kube-prometheus-stack-a-comprehensive-guide-for-kubernetes-monitoring)
[Source: How to reduce memory consumption, prometheus-operator GitHub issue](https://github.com/prometheus-operator/prometheus-operator/issues/3812)

### 7.3 Full Observability Stack Resource Budget

For a mid-size ISV deployment on managed Kubernetes (50 enterprise customers, ~500K–1M active
metrics, moderate log and trace volume), estimated cluster resource overhead for the full
self-managed stack:

| Component | CPU (request/limit) | Memory (request/limit) | Notes |
|---|---|---|---|
| Prometheus (2 replicas for HA) | 0.5 / 2 cores each | 2 / 4 GB each | Scales with cardinality |
| Prometheus Operator | 0.1 / 0.5 cores | 128 / 512 MB | Control-plane only |
| Thanos Sidecar (per Prometheus) | 0.1 / 0.5 cores | 128 / 512 MB | Block upload only |
| Thanos Querier | 0.2 / 1 core | 256 MB / 2 GB | Query fan-out |
| Grafana (2 replicas) | 0.2 / 0.5 cores each | 256 / 512 MB each | Dashboard serving |
| Loki (distributed) | 1 / 4 cores | 2 / 8 GB | Depends on log volume |
| Loki Compactor | 0.5 / 1 core | 512 MB / 2 GB | StatefulSet required |
| Tempo (distributed) | 1 / 4 cores | 2 / 8 GB | Depends on trace volume |
| OTel Collector DaemonSet (per node) | 0.25 / 0.5 cores | 256 / 512 MB | Per node overhead |
| Alertmanager (2 replicas) | 0.05 / 0.1 cores | 32 / 128 MB each | Alert routing only |
| **Estimated total (10-node cluster)** | **~8–15 cores** | **~15–35 GB** | **Before application workloads** |

[UNVERIFIED: The aggregate table above is constructed from individual component figures from
cited sources. No single source provides a combined stack resource budget for this exact
deployment profile. The ranges reflect the per-component figures at stated scales.]

---

## 8. Gap Analysis: Cloud-Native Observability vs. Kubernetes-Native Stack

### 8.1 What Cloud-Native Services Provide That K8s-Native Stacks Do Not

| Capability | Self-Managed K8s Stack | Cloud-Native Services |
|---|---|---|
| ML anomaly detection on metrics | Not available (Grafana has basic thresholds) | AWS CloudWatch (statistical ML), Azure Monitor Smart Alerts (WaveNet algorithm), GCP Cloud Monitoring (AI seasonal model) |
| Managed retention enforcement | ISV-operated (Compactor for logs, object store TTLs for metrics/traces) | Fully managed, configurable via UI/API |
| Auto-scaling ingestion pipeline | Manual horizontal scaling (Mimir ingesters, Loki distributors) | Automatic; no capacity planning for ingestion tier |
| Cross-service correlation | Requires Grafana datasource linking (configured by ISV) | Unified in single pane: CloudWatch Container Insights, Azure Monitor Application Insights, GCP Cloud Operations Suite |
| Agent deployment | Manual (OTel Operator, Helm) | Auto-injected via cloud-native mechanisms (EKS Add-ons, AKS extensions, GKE add-ons) |
| SLA / uptime guarantee | None (self-operated) | Covered by cloud provider SLAs |
| AIOps / intelligent alerting | Via third-party integrations (PagerDuty, etc.) | Native: Azure Smart Alerts, CloudWatch Anomaly Detection, GCP intelligent alerting |

[Source: AWS CloudWatch Anomaly Detection documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
[Source: Anomaly detection comparison in AWS vs. Azure vs. Google Cloud, Ternary](https://ternary.app/blog/anomaly-detection-comparison-aws-vs-azure-vs-gcp/)
[Source: How SREs are Using AI to Transform Incident Response, Cloud Native Now](https://cloudnativenow.com/contributed-content/how-sres-are-using-ai-to-transform-incident-response-in-the-real-world/)

**Adoption signal:** According to a 2025 report from 451 Research, 71% of organizations using
observability solutions are using their AI features — up 26% from 2024.
[Source: Grafana Cloud Observability Platform Overview (cites 451 Research)](https://grafana.com/products/cloud/)

### 8.2 What K8s-Native Stacks Provide That Cloud-Native Services Do Not

| Capability | Advantage |
|---|---|
| Multi-cloud portability | Identical stack runs on EKS, AKS, GKE, and on-prem |
| Open query languages | PromQL, LogQL, TraceQL — transferable skills, no vendor training lock-in |
| Data sovereignty | Logs and traces never leave ISV-controlled object storage |
| Cost predictability at scale | Object storage cost (S3/GCS/Azure Blob) is dramatically cheaper than per-GB ingestion fees at multi-TB/month scale |
| Customization | Full pipeline control (processors, transformers, routing) via OTel Collector config |
| Cross-signal correlation | Native within Grafana (metrics → logs → traces via exemplars and derived fields) |

---

## 9. Comparison Table: Operational Difficulty by Deployment Model

| Capability Domain | Managed K8s (Self-Hosted Stack) | Cloud-Native Observability Services |
|---|---|---|
| **Metrics collection** | Difficulty: 3/5 | Difficulty: 1/5 |
| | Prometheus Operator + ServiceMonitors | AMP / Azure Monitor / GCP Managed Prometheus |
| | kube-prometheus-stack Helm chart | Cloud-native collectors, agent auto-injection |
| | Est. FTE: 0.25–0.5 FTE (steady state) | Est. FTE: 0.1 FTE (config only) |
| **Long-term metric storage** | Difficulty: 4/5 | Difficulty: 1/5 |
| | Thanos or Mimir deployment + ops | Managed by cloud provider |
| | Object store bucket + lifecycle config | Configurable retention via UI/API |
| | Est. FTE: 0.25–0.5 FTE | Est. FTE: 0.05 FTE |
| **Log aggregation** | Difficulty: 3/5 | Difficulty: 2/5 |
| | Loki distributed deployment, Compactor ops | CloudWatch Logs / Azure Monitor / Cloud Logging |
| | LogQL, label strategy design | KQL / Logs Insights / Log Explorer |
| | Est. FTE: 0.25 FTE | Est. FTE: 0.1 FTE |
| **Distributed tracing** | Difficulty: 3/5 | Difficulty: 2/5 |
| | Tempo deployment + vParquet block management | X-Ray / App Insights / Cloud Trace |
| | TraceQL query language | Vendor query UIs |
| | Est. FTE: 0.25 FTE | Est. FTE: 0.1 FTE |
| **OTel instrumentation** | Difficulty: 3/5 | Difficulty: 2/5 |
| | OTel Operator + DaemonSet + auto-inject | ADOT / Azure OTel distro / GCP OTLP endpoint |
| | Collector pipeline configuration | Managed distros with preset configs |
| | Est. FTE: 0.25 FTE | Est. FTE: 0.1 FTE |
| **Dashboard and alerting** | Difficulty: 3/5 | Difficulty: 2/5 |
| | Grafana Operator + GitOps pipeline | Managed Grafana / CloudWatch dashboards |
| | Alert rule management in Grafana | Cloud-native alert policies |
| | Est. FTE: 0.25 FTE | Est. FTE: 0.1 FTE |
| **Total estimated FTE (mid-size ISV)** | **1.25–2.0 FTE** | **0.45–0.65 FTE** |

*FTE estimates assume: mid-size deployment serving 50 enterprise customers, 10-node managed K8s
cluster, moderate log/trace volume. Includes on-call burden (~0.25 FTE for K8s stack, ~0.1 FTE
for cloud-native). Does not include initial implementation effort (~3–6 months for full K8s
stack, ~4–8 weeks for cloud-native).*

---

## Key Takeaways

- **The self-managed K8s observability stack (Prometheus Operator + Grafana + Loki + Tempo)
  requires 1.25–2.0 FTE of ongoing operational effort** for a mid-size ISV deployment, consuming
  15–35 GB of cluster RAM before application workloads — approximately 3–4x the operational
  burden of cloud-native managed alternatives.

- **Grafana Mimir is the recommended long-term metric storage backend over Thanos for growth-
  stage ISVs**: it maintains consistent 80–100ms query latency at 7-day history (versus Thanos's
  2,000–4,000ms), with native multi-tenancy and horizontal scalability to 1 billion active
  series per tenant. Thanos remains appropriate for smaller deployments prioritizing simplicity.

- **Loki's label-only indexing model is its key cost advantage over CloudWatch Logs and Azure
  Monitor Log Analytics** at scale — object storage costs (S3/GCS) are a fraction of per-GB
  ingestion fees for high-volume log workloads — but demands deliberate label cardinality
  management and increases query complexity.

- **Cloud-native managed observability services provide capabilities the K8s-native stack cannot
  match without third-party integrations**: ML-based anomaly detection (CloudWatch, Azure Monitor
  WaveNet), auto-scaling ingestion pipelines, and unified cross-signal correlation in a single
  managed pane — particularly relevant for ISVs where observability is not a core competency.

- **The optimal strategy for most ISVs on managed Kubernetes is selective hybridization**: use
  cloud-managed Prometheus (AMP or Azure Monitor Managed Prometheus) to eliminate Thanos/Mimir
  complexity, self-manage Loki for cost-controlled log retention, and self-manage Tempo for
  open-format trace storage — while using Grafana as the unified frontend via the Grafana
  Operator and GitOps pipelines.

---

## Related — Out of Scope

- **On-prem observability architecture** (Prometheus without managed K8s, self-hosted ELK
  stack, Jaeger) — see F49-F51
- **Cloud-native observability services in depth** (CloudWatch, Azure Monitor, Cloud Operations
  Suite features, pricing models) — see F12, F20, F28
- **Kubernetes platform management** (cluster provisioning, upgrade strategies, node pool
  configuration) — see F52
- **Cost modeling for observability at scale** — a full TCO model comparing per-sample AMP costs
  against self-hosted Mimir at various cardinality levels warrants dedicated analysis

---

## Sources

1. [prometheus-operator/prometheus-operator GitHub](https://github.com/prometheus-operator/prometheus-operator)
2. [ServiceMonitor & PodMonitor Configuration, DeepWiki](https://deepwiki.com/prometheus-operator/prometheus-operator/4.1-servicemonitor-and-podmonitor-configuration)
3. [ServiceMonitor and PodMonitor Configuration, Rancher](https://ranchermanager.docs.rancher.com/reference-guides/monitoring-v2-configuration/servicemonitors-and-podmonitors)
4. [Thanos — Getting Started](https://thanos.io/v0.10/thanos/getting-started.md/)
5. [grafana/mimir GitHub](https://github.com/grafana/mimir)
6. [Prometheus Storage Comparison 2025, Onidel](https://onidel.com/blog/prometheus-storage-comparison-2025)
7. [Thanos vs Mimir — Grafana Labs Community Forum](https://community.grafana.com/t/thanos-vs-mimir-choosing-the-right-prometheus-extension/157751)
8. [Mimir 3.0 preview, Grafana Labs GrafanaCon 2025](https://grafana.com/events/grafanacon/2025/preview-mimir-3.0-release-for-metrics/)
9. [Grafana Mimir Compaction: From Bottleneck to Savings, Wise Engineering](https://medium.com/wise-engineering/grafana-mimir-compaction-from-bottleneck-to-savings-b26c6b0125a6)
10. [grafana/grafana-operator GitHub](https://github.com/grafana/grafana-operator)
11. [Manage folders, datasources, and dashboards using Grafana Operator](https://grafana.com/docs/grafana/latest/as-code/infrastructure-as-code/grafana-operator/operator-dashboards-folders-datasources/)
12. [Provision Grafana, Grafana documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/)
13. [Using Open Source Grafana Operator to manage Amazon Managed Grafana, AWS Blog](https://aws.amazon.com/blogs/mt/using-open-source-grafana-operator-on-your-kubernetes-cluster-to-manage-amazon-managed-grafana/)
14. [Grafana Loki OSS](https://grafana.com/oss/loki/)
15. [Storage, Grafana Loki documentation](https://grafana.com/docs/loki/latest/configure/storage/)
16. [Single Store TSDB, Grafana Loki documentation](https://grafana.com/docs/loki/latest/operations/storage/tsdb/)
17. [Log retention, Grafana Loki documentation](https://grafana.com/docs/loki/latest/operations/storage/retention/)
18. [Grafana Loki Architecture: A Comprehensive Guide, DevOpsCube](https://devopscube.com/grafana-loki-architecture/)
19. [What Is Grafana Loki?, Middleware.io](https://middleware.io/blog/grafana-loki/)
20. [Amazon CloudWatch Deep Dive comparison, blog.greeden.me](https://blog.greeden.me/en/2025/11/14/amazon-cloudwatch-deep-dive-a-complete-guide-to-monitoring-logs-metrics-design-compared-with-cloud-monitoring-gcp-and-azure-monitor/)
21. [Grafana Tempo OSS](https://grafana.com/oss/tempo/)
22. [Tempo architecture, Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/introduction/architecture/)
23. [Tempo 2.10 release, Grafana Labs](https://grafana.com/blog/tempo-2-10-release-all-the-latest-features/)
24. [Version 2.10 release notes, Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/release-notes/v2-10/)
25. [TraceQL, Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/traceql/)
26. [Grafana Tempo 2.8 release, InfoQ](https://www.infoq.com/news/2025/07/grafana-tempo-2-8/)
27. [Powerful new language features for TraceQL, Grafana Labs](https://grafana.com/whats-new/2025-05-08-powerful-new-language-features-for-traceql/)
28. [Grafana Tempo 2.9 release, Grafana Labs](https://grafana.com/blog/2025/10/22/grafana-tempo-2-9-release-mcp-server-support-traceql-metrics-sampling-and-more/)
29. [Google Cloud Observability Adopts OpenTelemetry Protocol, InfoQ, Sept 2025](https://www.infoq.com/news/2025/09/gcp-opentelemetry-adoption/)
30. [AWS X-Ray vs Azure Application Insights, StackShare](https://stackshare.io/stackups/aws-x-ray-vs-azure-application-insights)
31. [End-to-End Distributed Tracing in Kubernetes with Grafana Tempo, Civo](https://www.civo.com/learn/distributed-tracing-kubernetes-grafana-tempo-opentelemetry)
32. [OpenTelemetry Operator for Kubernetes](https://opentelemetry.io/docs/platforms/kubernetes/operator/)
33. [Injecting Auto-instrumentation, OpenTelemetry documentation](https://opentelemetry.io/docs/platforms/kubernetes/operator/automatic/)
34. [Sidecar or Agent for OpenTelemetry: How to Decide, Last9](https://last9.io/blog/opentelemetry-sidecar-vs-agent/)
35. [OpenTelemetry Collector deployment modes in Kubernetes, New Relic](https://newrelic.com/blog/how-to-relic/opentelemetry-collector-deployment-modes-in-kubernetes/)
36. [How to Right-Size CPU and Memory for the OpenTelemetry Collector, OneUptime](https://oneuptime.com/blog/post/2026-02-06-right-size-cpu-memory-opentelemetry-collector/view)
37. [Amazon Managed Service for Prometheus Pricing](https://aws.amazon.com/prometheus/pricing/)
38. [Amazon Managed Service for Prometheus product page](https://aws.amazon.com/prometheus/)
39. [How Much Does Your Managed Service for Prometheus Cost?, Sysdig](https://www.sysdig.com/blog/managed-service-prometheus)
40. [Pricing comparison for Managed Prometheus, VictoriaMetrics](https://victoriametrics.com/blog/managed-prometheus-pricing/)
41. [How to Reduce Prometheus High Memory Usage, SigNoz](https://signoz.io/guides/why-does-prometheus-consume-so-much-memory/)
42. [High CPU/Memory when monitoring 1000+ ServiceMonitors, GitHub Issues](https://github.com/prometheus-operator/prometheus-operator/issues/2866)
43. [Kube Prometheus Stack Guide 2025, Atmosly](https://atmosly.com/blog/kube-prometheus-stack-a-comprehensive-guide-for-kubernetes-monitoring)
44. [How to reduce memory consumption, prometheus-operator GitHub issue #3812](https://github.com/prometheus-operator/prometheus-operator/issues/3812)
45. [AWS CloudWatch Anomaly Detection documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
46. [Anomaly detection comparison AWS vs Azure vs GCP, Ternary](https://ternary.app/blog/anomaly-detection-comparison-aws-vs-azure-vs-gcp/)
47. [How SREs are Using AI to Transform Incident Response, Cloud Native Now](https://cloudnativenow.com/contributed-content/how-sres-are-using-ai-to-transform-incident-response-in-the-real-world/)
48. [Grafana Cloud Observability Platform Overview (cites 451 Research 2025)](https://grafana.com/products/cloud/)
49. [Deploying Grafana Tempo Distributed Tracing with Helm, OneUptime](https://oneuptime.com/blog/post/2026-01-17-helm-grafana-tempo-tracing-deployment/view)
50. [Improving HA and long-term storage for Prometheus using Thanos on EKS with S3, AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/improving-ha-and-long-term-storage-for-prometheus-using-thanos-on-eks-with-s3/)
