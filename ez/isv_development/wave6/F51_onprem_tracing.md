# F51 — On-Premises Distributed Tracing

**Research Domain:** Infrastructure Observability — Distributed Tracing
**Deployment Context:** ISV evaluating on-premises, managed Kubernetes, and cloud-native deployment models
**Date:** 2026-02-18

---

## Executive Summary

Self-hosting distributed tracing infrastructure on-premises is a technically tractable but operationally demanding commitment. The dominant open-source options — Jaeger (now rebuilt on the OpenTelemetry Collector framework in v2) and Grafana Tempo (backed by object storage) — provide enterprise-grade tracing capabilities, but require dedicated engineering effort to size, scale, and maintain storage backends that can grow to terabytes within weeks at moderate service volumes. The OpenTelemetry Collector has emerged as the universal telemetry pipeline layer, and its 2025 consistent probability sampling specification now enables mathematically sound, multi-service sampling without trace incompleteness. Managed cloud services (AWS X-Ray, Azure Application Insights, Google Cloud Trace) eliminate storage management, scaling, and backend maintenance entirely, but introduce per-trace costs that can become prohibitive at high volume and create hard vendor lock-in. For ISVs deploying to customer-controlled environments, the choice of tracing stack is tightly coupled to the customer's existing storage infrastructure and their tolerance for operational overhead.

---

## 1. Jaeger: Deployment Architecture and Storage

### 1.1 Architecture Overview

Jaeger is a CNCF-graduated distributed tracing platform. [Jaeger v2 was released in November 2024](https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/) with a fundamental architectural change: the platform is now built on top of the OpenTelemetry Collector framework rather than maintaining a bespoke pipeline. This consolidates the previously separate v1 binaries — jaeger-agent, jaeger-collector, jaeger-ingester, jaeger-query — into a single configurable binary driven by YAML configuration.

[FACT] Per the CNCF release announcement, "Jaeger v2 consolidates multiple v1 binaries (agent, collector, ingester, query) into one configurable executable," with roles defined through configuration rather than separate command-line tools.
URL: https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/

[FACT] Jaeger v1 will be fully deprecated in January 2026, following a final v1 release in December 2025.
URL: https://www.cncf.io/blog/2025/09/01/jaeger-at-10-forged-in-community-reborn-in-opentelemetry/

**Core deployment patterns (from [official Jaeger documentation](https://www.jaegertracing.io/docs/1.28/deployment/)):**

- **All-in-One:** Single binary combining collector, query service, and UI. Defaults to in-memory storage — data is lost on restart. Suitable only for development and light trace volumes.
- **Distributed (Production):** Separate, stateless collector instances plus a query service, each horizontally scalable. Collectors are described as requiring "almost no configuration, except for storage location."
- **Kafka-Buffered:** Collectors write to a Kafka topic; a separate ingester reads from Kafka and writes to persistent storage, providing a buffer against ingestion spikes.

### 1.2 Storage Backends

[STATISTIC] For small-to-medium production Elasticsearch deployments, minimum hardware requirements are 3 Elasticsearch nodes, 8 GB RAM per node, 4 CPU cores per node, and SSD storage.
URL: https://signoz.io/guides/what-database-does-jaeger-use/

**Elasticsearch/OpenSearch (recommended for production):**
Elasticsearch is the officially recommended Jaeger storage backend. It supports versions 7.x and 8.x, requires no schema initialization, and provides full-text search and complex query capabilities that Cassandra cannot match. It integrates naturally with existing ELK stack deployments.

**Cassandra (alternative):**
Cassandra 4.x and 5.x are supported and require schema initialization via `cqlsh`. [Per SigNoz's analysis](https://signoz.io/guides/what-database-does-jaeger-use/), "Cassandra is a key-value database, so it is more efficient for retrieving traces by trace ID, but it does not provide the same powerful search capabilities as Elasticsearch." Cassandra's multi-datacenter replication is an advantage for geographically distributed deployments.

**Kafka (buffer layer only):**
Kafka is used as an intermediary, not as a terminal storage backend. Per [Logz.io's documentation](https://logz.io/blog/jaeger-persistence/), "The collector is configured with SPAN_STORAGE_TYPE=kafka that makes it write all received spans into a Kafka topic," with a separate ingester reading from Kafka to write to Elasticsearch or Cassandra.

### 1.3 Jaeger v2 and OpenTelemetry Integration

[QUOTE] "By building on the OpenTelemetry Collector, Jaeger inherits its rich ecosystem of receivers, processors, and exporters, which allows for advanced data manipulation, from tail-based sampling to PII filtering and seamless integration with other observability tools."
URL: https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/

[FACT] Jaeger v2's Storage V2 architecture natively supports OTLP payloads, eliminating the data model translation overhead that existed between Jaeger's v1 format and storage backends.
URL: https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/

The v2 architecture also introduces batch processing for spans, which the CNCF announcement notes is "particularly beneficial for storage systems like ClickHouse, enhancing throughput and resource usage." This positions Jaeger v2 as a serious candidate for high-throughput on-premises deployments.

---

## 2. Grafana Tempo: Object Storage Backend and TraceQL

### 2.1 Architecture and Components

Grafana Tempo is a high-scale distributed tracing backend that diverges fundamentally from Jaeger's design by using object storage (S3, GCS, Azure Blob) as its primary data store rather than a search database. This architecture choice is its primary operational differentiator for on-premises deployments.

[Per the official Grafana Tempo architecture documentation](https://grafana.com/docs/tempo/latest/introduction/architecture/), Tempo operates through five core components:

| Component | Role |
|-----------|------|
| **Distributor** | Accepts spans in Jaeger, OpenTelemetry, and Zipkin formats; routes via consistent hash ring by traceID |
| **Ingester** | Indexes spans, partitions attributes into Apache Parquet schema, batches into storage blocks |
| **Query Frontend** | Handles user-facing requests; splits queries across Querier instances in parallel |
| **Querier** | Examines object storage blocks and queries Ingesters for recent unwritten data |
| **Compactor** | Compresses, deduplicates, and expires data on scheduled intervals |

An optional **Metrics Generator** component derives RED (Rate, Error, Duration) metrics directly from ingested traces, enabling metric generation without separate instrumentation.

[FACT] Grafana Tempo 2.8 was released on June 12, 2025, introducing "substantial memory optimizations and expanded functionality in its trace query language, TraceQL."
URL: https://www.infoq.com/news/2025/07/grafana-tempo-2-8/

### 2.2 Object Storage for On-Premises Deployments

Tempo supports three object storage APIs: Amazon S3, Google Cloud Storage, and Microsoft Azure Storage. For on-premises deployments, S3-compatible object stores (e.g., Ceph, or historically MinIO) provide the necessary compatibility layer.

[FACT] Per Grafana's documentation, "while you can use local storage, object storage is recommended for production workloads."
URL: https://grafana.com/docs/tempo/latest/introduction/architecture/

**Important note on MinIO:** A significant operational consideration emerged in late 2025. According to [reporting on open-source S3 alternatives](https://medium.com/cubbit/top-minio-and-ceph-s3-alternatives-in-2025-european-gems-inside-b99aa4c6abb6), MinIO entered maintenance mode in late 2025 and was subsequently archived, with features stripped from the community edition and the open-source repository made read-only by early 2026. Production deployments of Tempo requiring self-hosted S3 should evaluate Ceph or commercial MinIO (AIStor) as alternatives. This is a material planning consideration for on-premises ISV deployments.

### 2.3 TraceQL Query Language

TraceQL is Tempo's purpose-built query language for distributed traces, designed with syntax and semantics deliberately aligned with PromQL and LogQL to reduce learning overhead for teams already using the Grafana stack.

[FACT] TraceQL uses curly-bracket selectors `{}` to select sets of spans and supports intrinsic reserved words (`name`, `duration`, `status`) plus arbitrary attribute key-value pairs prefixed with dots (`.http.status_code`, `.service.name`).
URL: https://grafana.com/docs/tempo/latest/traceql/

**Example TraceQL query:**
```
{ .service.name = "checkout" && (duration > 500ms || .http.status_code >= 500) }
```

**2025 TraceQL enhancements ([Grafana Tempo 2.8](https://grafana.com/whats-new/2025-05-08-powerful-new-language-features-for-traceql/)):**
- `topk(n)` and `bottomk(n)` ranking functions for identifying highest/lowest duration spans
- `sum_over_time()` for cumulative aggregation (total bytes, error counts)
- `most_recent` query hint for freshness-prioritized searches across data shards

**TraceQL Metrics** extends the query language to derive Prometheus-compatible metrics directly from trace data, enabling RED metrics without a separate metrics instrumentation layer — a meaningful operational simplification for on-premises deployments. See [Grafana TraceQL metrics documentation](https://grafana.com/docs/tempo/latest/metrics-from-traces/metrics-queries/).

---

## 3. OpenTelemetry Collector: Deployment and Instrumentation

### 3.1 Collector Deployment Patterns

The OpenTelemetry Collector is the universal telemetry pipeline component — a single binary that receives telemetry from instrumented applications, processes it, and exports it to backends. It supports three canonical deployment patterns:

[Per the official OpenTelemetry Collector deployment documentation](https://opentelemetry.io/docs/collector/deploy/):

**Agent Pattern:** Collectors run on each host (or as Kubernetes DaemonSets), collecting telemetry from services on that host plus host-level metrics. Lightweight; handles basic processing and metadata enrichment.

**Gateway Pattern:** A centralized pool of Collector instances receives telemetry from agents or directly from applications. The gateway handles computationally expensive operations: tail-based sampling, PII filtering, fan-out to multiple backends, and protocol translation. Per [ControlTheory's deployment guide](https://www.controltheory.com/resources/opentelemetry-collector-deployment-patterns-a-guide/), a load balancer distributes traffic across gateway instances.

**Hybrid (Agent + Gateway):** The recommended production pattern per [Datadog's OTel deployment guide](https://www.datadoghq.com/blog/otel-deployments/). Agents perform local collection and enrichment; gateways perform heavy processing. This separation allows agents to stay lightweight while gateways handle stateful operations like tail sampling.

[FACT] In Kubernetes, the OTel Collector can be deployed as a DaemonSet (agent mode), a Deployment (gateway mode with horizontal scaling), or as a Sidecar (per-pod agent model).
URL: https://opentelemetry.io/docs/collector/deploy/

[FACT] Tail-based sampling in a multi-instance gateway deployment requires trace-aware load balancing, because "all spans from a trace must reach the same collector instance." This is achieved using a load balancing exporter in a first-tier collector layer, with tail sampling processors in a second tier.
URL: https://opentelemetry.io/docs/concepts/sampling/

### 3.2 Protocol Support

The OTel Collector natively supports OTLP (gRPC and HTTP), Jaeger, Zipkin, and Prometheus as receivers. As exporters, it supports OTLP, Jaeger, Zipkin, Kafka, and numerous vendor-specific destinations. This makes it the standard integration layer for any self-hosted tracing backend.

### 3.3 Sampling Strategies

**Head-Based Sampling:**
Sampling decisions are made at the trace root before any downstream spans exist. [Per the OpenTelemetry sampling documentation](https://opentelemetry.io/docs/concepts/sampling/), "the primary downside to head sampling is that it is not possible to make a sampling decision based on data in the entire trace, for example, you cannot ensure that all traces with an error within them are sampled."

**Tail-Based Sampling:**
The sampling decision is deferred until all (or most) spans in a trace are available. This enables policy-based decisions: sample all traces with errors, sample all traces exceeding a latency threshold, sample only traces from specific services.

[QUOTE] "The component(s) that implement tail sampling must be stateful systems that can accept and store a large amount of data, and depending on traffic patterns, this can require dozens or even hundreds of compute nodes that all utilize resources differently."
URL: https://opentelemetry.io/docs/concepts/sampling/

The OTel Collector's tail sampling processor supports [at least 13 distinct policy types](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md), including error-based, latency-based, probabilistic, rate-limiting, and composite policies.

**2025 Consistent Probability Sampling — Major Specification Update:**

[FACT] In October 2025, OpenTelemetry adopted W3C TraceContext Level 2 as the foundation for a new consistent probability sampling specification, resolving a longstanding "TODO" in the original 1.0 spec that made `TraceIdRatioBased` samplers unsafe for non-root spans.
URL: https://opentelemetry.io/blog/2025/sampling-milestones/

[QUOTE] The specification now enables "users to configure unequal-probability sampling policies within a trace while still expecting complete traces, allowing service owners to configure independent limits on tracing data volume."
URL: https://opentelemetry.io/blog/2025/sampling-milestones/

The mechanism encodes sampling thresholds in the W3C `tracestate` header (`ot=th:fd7` for approximately 1% sampling, with trailing zeros dropped). A "common random value" propagated across all participants enables each service to make consistent, mathematically correlated decisions. This resolves a major gap in multi-service sampling correctness that affected on-premises deployments at scale.

---

## 4. Instrumentation Burden

### 4.1 Auto-Instrumentation vs. Manual Instrumentation

[QUOTE] "Auto-instrumentation injects spans and propagates context without you writing a single line of observability code."
URL: https://cribl.io/blog/manual-vs-auto-instrumentation-opentelemetry-choose-whats-right/

[QUOTE] "Fast time to value: You can instrument an application and emit traces in minutes" with auto-instrumentation.
URL: https://cribl.io/blog/manual-vs-auto-instrumentation-opentelemetry-choose-whats-right/

Auto-instrumentation limitations per [Cribl's analysis](https://cribl.io/blog/manual-vs-auto-instrumentation-opentelemetry-choose-whats-right/):
- Limited ability to customize telemetry at the source
- Risk of collecting excessive data across all instrumented dependencies
- Potential for accidental PII exposure in URIs, request bodies, or SQL parameters

[QUOTE] "While the OpenTelemetry agent excels at propagating context across known libraries, in more bespoke scenarios, traces may become fragmented, making it difficult to follow the complete flow of a request."
URL: https://medium.com/@rahul.fiem/opentelemetry-automatic-vs-manual-instrumentation-which-one-should-you-use-d7ecb1f77515

### 4.2 Context Propagation

Context propagation — the passing of trace and span IDs across service boundaries — is the mechanism that makes distributed tracing coherent. For HTTP and gRPC, auto-instrumentation handles this automatically via W3C Trace Context headers. For custom protocols, message queues, async workflows, and gRPC streaming, manual propagation is required.

[FACT] "For custom communication channels, you'll need to manually propagate context."
URL: https://opentelemetry.io/docs/concepts/instrumentation/

[FACT] "With manual instrumentation, you can even propagate baggage across service boundaries, ensuring that business or customer context follows a request end-to-end."
URL: https://opentelemetry.io/docs/concepts/instrumentation/

**Recommended approach:** Per [Better Stack's OpenTelemetry best practices](https://betterstack.com/community/guides/observability/opentelemetry-best-practices/), the most effective strategy combines both modes: "automatic instrumentation provides broad coverage for common patterns, while manual instrumentation captures business-specific metrics." Start with auto-instrumentation for broad coverage; layer manual instrumentation for critical business paths and custom protocols.

An important note for ISVs: Jaeger itself does not provide tracing instrumentation. Per [Better Stack's Jaeger guide](https://betterstack.com/community/guides/observability/jaeger-guide/), "Jaeger itself doesn't provide tracing instrumentation," meaning OpenTelemetry SDKs or compatible libraries must be separately implemented in every instrumented service.

---

## 5. Storage: Requirements, Retention, and Cardinality

### 5.1 Storage Volume at Scale

Distributed tracing generates substantial data volumes. Unlike metrics (which aggregate) or structured logs (which can be filtered), traces capture full request trees including timing, attributes, and span relationships. High-cardinality attributes — user IDs, session tokens, request IDs — cause trace storage to grow non-linearly.

[QUOTE] "Full sampling offers complete visibility but can be prohibitively expensive at scale; sampled systems reduce storage and ingestion costs but risk missing rare failures."
URL: https://www.apica.io/blog/what-is-distributed-tracing-how-it-works-and-best-practices/

[FACT] For Elasticsearch-backed Jaeger production deployments (small-to-medium scale), minimum hardware is 3 nodes × 8 GB RAM × 4 CPU cores, SSD-backed storage, with scaling required based on trace data volume and retention policy.
URL: https://signoz.io/guides/what-database-does-jaeger-use/

### 5.2 Retention Policies

Trace data retention is typically much shorter than log or metric retention — 7 to 30 days is common in production environments — because individual trace records carry high cardinality metadata that accumulates quickly. Retention policies must be configured at the storage layer (index lifecycle management in Elasticsearch; TTL settings in Cassandra; lifecycle rules on the object store for Tempo).

[QUOTE] "Grafana Tempo is cost-efficient, requiring only object storage to operate, and is optimized for high performance to handle large amounts of tracing data."
URL: https://uptrace.dev/tools/distributed-tracing-tools

### 5.3 Cardinality and Cost Control

[QUOTE] "High cardinality attributes like user IDs can explode storage and query costs."
URL: https://cloudnativenow.com/contributed-content/cost-aware-observability-on-k8s-balancing-scrape-intervals-retention-and-cardinality/

[FACT] "Teams are standardizing on OpenTelemetry, unifying logs, metrics, and traces, and shifting to columnar storage on object stores for speed, flexibility, and lower total cost" as of 2025.
URL: https://www.apica.io/blog/what-is-distributed-tracing-how-it-works-and-best-practices/

Tempo's use of Apache Parquet columnar format for trace storage is a direct response to this cardinality challenge — columnar access patterns allow queriers to read only the columns relevant to a query rather than full trace records, significantly reducing I/O and memory pressure at scale.

---

## 6. Correlation: Traces to Logs and Metrics

### 6.1 Exemplars

Prometheus exemplars are the primary mechanism for linking metric data points to specific traces. A metric counter increment can carry a trace ID as an exemplar, allowing an operator to move directly from a spike in error rate (metrics) to the specific trace that caused it.

[FACT] "Traces can be attached as Prometheus exemplars to time series samples so metrics can be linked to traces. Using traces and exemplars, you can go from a metric data point and get to an associated trace."
URL: https://grafana.com/docs/tempo/latest/introduction/telemetry/

### 6.2 Log-Trace Correlation

Structured logs containing `trace_id` and `span_id` fields — emitted via OTel logging SDKs — enable direct navigation from a log line to the associated trace. Grafana Loki natively supports this via its TraceID field, rendering a link to Tempo in the Grafana UI. Elasticsearch-based log systems achieve the same through trace ID field indexing.

[FACT] "By 2025, leading teams no longer manage these signals in isolation — they unify them through a single telemetry pipeline powered by OpenTelemetry, enabling teams to detect, pinpoint, and resolve issues faster."
URL: https://edgedelta.com/company/knowledge-center/distributed-systems-observability

### 6.3 Service Dependency Mapping

[QUOTE] "Traces have the unique ability to show relationships between services and help identify which services are upstream from your service, which is helpful when you want to understand which services might be negatively impacted by problems in your service."
URL: https://documentation.ubuntu.com/observability/track-2/explanation/telemetry-correlation/

Jaeger's Service Performance Management (SPM) feature and Tempo's Metrics Generator both compute RED metrics from trace data to produce service dependency graphs. For on-premises deployments, these components require additional compute resources beyond the core tracing pipeline.

See [F50: On-Prem Monitoring] for detailed coverage of metrics infrastructure and [F49: On-Prem Logging] for log pipeline architecture.

---

## 7. Deployment Model Comparison

### Difficulty and FTE Estimates

**Assumptions for FTE estimation:**
- Medium-scale ISV: 10–50 microservices, 1,000–50,000 requests/minute
- Kubernetes-based deployment for on-premises and managed K8s models
- FTE = engineering time devoted to tracing infrastructure (not application instrumentation)
- On-call burden estimated separately from steady-state maintenance FTE
- No publicly available industry benchmark explicitly citing FTE for tracing infrastructure; estimates derived from operational complexity of documented component stacks [UNVERIFIED: Specific FTE ranges are author estimates based on component count, storage management complexity, and analogous DevOps infrastructure sizing ratios; no primary source provides explicit FTE benchmarks for tracing infrastructure]

| Capability | On-Premises | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native |
|------------|-------------|-----------------------------------|--------------|
| **Tracing Backend** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Jaeger v2 or Tempo + storage backend (ES cluster or S3-compatible object store) | Jaeger v2 or Tempo via Helm charts; storage on managed ES or object store | AWS X-Ray, Azure Application Insights, or Google Cloud Trace |
| | Full cluster management, schema migrations, storage sizing | Helm + operator lifecycle management; storage managed by cloud provider | No infrastructure; SDK/agent configuration only |
| | Est. FTE: 0.5–1.0 (steady state) | Est. FTE: 0.25–0.5 (steady state) | Est. FTE: 0.1–0.2 (steady state) |
| **OTel Collector** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 2/5 |
| | DaemonSet agents + gateway Deployments; self-managed upgrades | DaemonSet agents + gateway Deployments; cloud-managed node lifecycle | ADOT (AWS), OTel on AKS, or vendor agents; managed by cloud provider |
| | Load balancer config for tail sampling; state management | Same architecture but on managed infra; simpler node failure handling | Vendor agents simplify deployment but reduce pipeline flexibility |
| | Est. FTE: 0.25 | Est. FTE: 0.1–0.2 | Est. FTE: 0.1 |
| **Storage Management** | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Elasticsearch cluster operations + ILM policies OR Ceph/object store + lifecycle rules; capacity planning; index management | Managed Elasticsearch (OpenSearch Service, Elastic Cloud) or S3/Azure Blob; cloud handles node ops | Fully managed retention; configurable via console |
| | Backup, recovery, shard rebalancing, cluster upgrades | Snapshot policies; scaling managed by provider | Provider-managed; retention policies only |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.1 | Est. FTE: 0.0 |
| **Tail Sampling** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Two-tier OTel Collector deployment; stateful gateway; load balancer exporter config; horizontal scaling for traffic spikes | Same architecture; cloud-managed load balancers reduce config burden | Native tail sampling in X-Ray (via sampling rules); limited customization vs OTel policies |
| | 13+ OTel policy types available; complex YAML; stateful memory requirements | Same policy flexibility; simpler infra management | Vendor-defined policies; less flexibility |
| | Est. FTE: 0.25 | Est. FTE: 0.1–0.15 | Est. FTE: 0.05 |
| **Log-Trace Correlation** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Manual trace ID field configuration in log pipeline; Grafana datasource linking | Same configuration; cloud log services (CloudWatch, Azure Monitor) support trace IDs | Native correlation in Application Insights; X-Ray integrates with CloudWatch |
| | Loki + Tempo or Elasticsearch + Jaeger; requires coordinated field naming | Cloud-managed log services; OTel SDK handles field injection | Vendor-native; minimal configuration |
| | Est. FTE: 0.1 | Est. FTE: 0.05 | Est. FTE: 0.0 |
| **Total Estimated FTE** | **1.6–2.5 FTE** | **0.6–1.0 FTE** | **0.2–0.3 FTE** |
| | Plus 0.25–0.5 FTE on-call burden | Plus 0.1–0.2 FTE on-call burden | Plus 0.0–0.05 FTE on-call burden |

---

## 8. Managed Cloud Services: What Operational Burden Disappears?

### 8.1 AWS X-Ray

AWS X-Ray is a managed distributed tracing service with native integration across AWS services (Lambda, ECS, API Gateway, ALB).

**Pricing ([AWS X-Ray pricing page](https://aws.amazon.com/xray/pricing/)):**
- First 100,000 traces recorded per month: free
- Traces recorded (beyond free tier): $5.00 per 1 million traces
- Traces retrieved or scanned: $0.50 per 1 million traces

[FACT] "AWS X-Ray can be very expensive compared to other options, requiring consideration of cost-effectiveness."
URL: https://www.peerspot.com/products/aws-x-ray-pros-and-cons

**What disappears with X-Ray vs. self-hosted:**
- Elasticsearch/Cassandra cluster management
- OTel Collector gateway fleet management
- Storage capacity planning and ILM policy management
- Backend upgrades and schema migrations
- Backup and recovery operations

**What remains:**
- SDK instrumentation of every service
- Sampling rule configuration
- IAM permission configuration for cross-service tracing
- Cross-account trace aggregation configuration

### 8.2 Azure Application Insights

Azure Application Insights provides distributed tracing as part of Azure Monitor, with telemetry stored in Log Analytics workspaces.

**Pricing ([Azure Monitor pricing page](https://azure.microsoft.com/en-us/pricing/details/monitor/)):**
- Pay-As-You-Go: charged per GB of telemetry data ingested
- Commitment Tiers: starting at 100 GB/day with discounted per-GB rates
- 5 GB per month free ingestion credit applies

[FACT] "Sampling is an effective way to reduce charges and stay within your monthly quota" for Application Insights.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/application-insights-faq

Application Insights provides richer analytics capabilities than X-Ray — including dependency tracking, availability tests, and integrated exception reporting — but is more narrowly optimized for Azure workloads. Cross-cloud or multi-cloud ISV deployments face integration friction.

### 8.3 Google Cloud Trace

Google Cloud Trace provides distributed tracing with native integration into GCP services including App Engine, GKE, and Cloud Run. Some GCP services offer automatic instrumentation with minimal configuration.

[QUOTE] "Compared to open-source alternatives like Jaeger or Zipkin, Google Cloud Trace offers advantages in its integration with Google Cloud and reduced operational overhead as a fully managed service."
URL: https://www.dash0.com/knowledge/what-is-google-cloud-trace

Cloud Trace integrates natively with Cloud Monitoring (metrics) and Cloud Logging, enabling correlation without manual configuration. For ISVs deploying exclusively to GCP, this reduces the observability integration burden significantly. For multi-cloud deployments, OpenTelemetry provides the vendor-neutral instrumentation layer.

---

## 9. Comparison Summary Table

| Dimension | On-Premises (Jaeger/Tempo) | Managed Kubernetes | Cloud-Native (X-Ray/AppInsights/Cloud Trace) |
|-----------|---------------------------|-------------------|----------------------------------------------|
| Storage management | Full responsibility (ES cluster or object store fleet) | Cloud-managed storage backends | Zero; provider-managed |
| Scaling | Manual horizontal scaling of collectors and storage | Autoscaling available; simpler ops | Automatic; transparent |
| Tail sampling flexibility | Maximum (13+ OTel policy types) | Same as on-premises | Limited to vendor-defined rules |
| Vendor lock-in | Minimal (CNCF/OTel standards) | Low (OTel + cloud infra) | High (proprietary SDK/API) |
| Per-trace cost | Infrastructure cost only (fixed) | Infrastructure cost only (partially variable) | $5.00/million traces (X-Ray) |
| Cross-cloud support | Full (OTel is cloud-agnostic) | Full | Fragmented (separate tools per cloud) |
| Time to first trace | Days–weeks (infra provisioning) | Hours–days (Helm deployment) | Minutes (SDK + agent) |
| Compliance/data residency | Full control | Partial control | Provider-dependent |

---

## Key Takeaways

- **Jaeger v2's OpenTelemetry-native architecture** (released November 2024, with v1 deprecated January 2026) consolidates the previously multi-binary deployment into a single configurable binary, reducing operational complexity while inheriting the full OTel Collector ecosystem including tail sampling, PII filtering, and fan-out exporters.

- **Grafana Tempo's object storage model** is the most operationally efficient self-hosted tracing backend for high-volume deployments — it eliminates database cluster management by using S3-compatible object storage, but introduces a dependency on a production-grade object store (Ceph or commercial options, following MinIO's open-source archival in late 2025).

- **The 2025 OpenTelemetry consistent probability sampling specification** resolves a long-standing correctness gap that made multi-service independent sampling mathematically unreliable; ISVs building on OTel should adopt this specification to guarantee trace completeness when applying different sampling rates across service tiers.

- **Managed cloud tracing services eliminate storage, scaling, and backend maintenance** entirely, but introduce per-trace costs that scale linearly with request volume and create hard vendor coupling — making them most suitable for single-cloud ISV deployments with predictable, moderate trace volumes, and least suitable for multi-cloud or on-premises-to-customer ISV models.

- **Total on-premises tracing infrastructure burden** for a medium-scale ISV is estimated at **1.6–2.5 FTE steady-state** plus 0.25–0.5 FTE on-call — compared to 0.2–0.3 FTE for a fully cloud-native deployment — representing a significant operational cost differential that must be weighed against data sovereignty requirements and the multi-cloud flexibility that self-hosted, OTel-based tracing provides.

---

## Sources

1. [Jaeger v2 Released: OpenTelemetry in the Core — CNCF](https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/)
2. [Jaeger at 10: Forged in Community, Reborn in OpenTelemetry — CNCF](https://www.cncf.io/blog/2025/09/01/jaeger-at-10-forged-in-community-reborn-in-opentelemetry/)
3. [Jaeger Deployment Documentation — jaegertracing.io](https://www.jaegertracing.io/docs/1.28/deployment/)
4. [What Database Does Jaeger Use — SigNoz](https://signoz.io/guides/what-database-does-jaeger-use/)
5. [Jaeger Persistence with Elasticsearch, Cassandra, Kafka — Logz.io](https://logz.io/blog/jaeger-persistence/)
6. [Grafana Tempo Architecture — Grafana Documentation](https://grafana.com/docs/tempo/latest/introduction/architecture/)
7. [Grafana Tempo 2.8 Released — InfoQ](https://www.infoq.com/news/2025/07/grafana-tempo-2-8/)
8. [Powerful New TraceQL Language Features — Grafana Labs](https://grafana.com/whats-new/2025-05-08-powerful-new-language-features-for-traceql/)
9. [TraceQL Documentation — Grafana Tempo](https://grafana.com/docs/tempo/latest/traceql/)
10. [Get to Know TraceQL — Grafana Labs Blog](https://grafana.com/blog/2023/02/07/get-to-know-traceql-a-powerful-new-query-language-for-distributed-tracing/)
11. [TraceQL Metrics Documentation — Grafana Tempo](https://grafana.com/docs/tempo/latest/metrics-from-traces/metrics-queries/)
12. [Traces and Telemetry — Grafana Tempo Documentation](https://grafana.com/docs/tempo/latest/introduction/telemetry/)
13. [OpenTelemetry Collector Deploy — opentelemetry.io](https://opentelemetry.io/docs/collector/deploy/)
14. [OpenTelemetry Gateway Deployment Pattern — opentelemetry.io](https://opentelemetry.io/docs/collector/deploy/gateway/)
15. [OpenTelemetry Sampling Documentation — opentelemetry.io](https://opentelemetry.io/docs/concepts/sampling/)
16. [OpenTelemetry Sampling Milestones 2025 — opentelemetry.io](https://opentelemetry.io/blog/2025/sampling-milestones/)
17. [Tail Sampling Processor README — opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md)
18. [OpenTelemetry Collector Deployment Patterns — ControlTheory](https://www.controltheory.com/resources/opentelemetry-collector-deployment-patterns-a-guide/)
19. [How to Select Your OTel Deployment — Datadog](https://www.datadoghq.com/blog/otel-deployments/)
20. [Manual vs. Auto Instrumentation OpenTelemetry — Cribl](https://cribl.io/blog/manual-vs-auto-instrumentation-opentelemetry-choose-whats-right/)
21. [OpenTelemetry Automatic vs. Manual Instrumentation — Medium](https://medium.com/@rahul.fiem/opentelemetry-automatic-vs-manual-instrumentation-which-one-should-you-use-d7ecb1f77515)
22. [OpenTelemetry Instrumentation Documentation — opentelemetry.io](https://opentelemetry.io/docs/concepts/instrumentation/)
23. [Demystifying Auto-Instrumentation — OpenTelemetry Blog 2025](https://opentelemetry.io/blog/2025/demystifying-auto-instrumentation/)
24. [OpenTelemetry Best Practices — Better Stack](https://betterstack.com/community/guides/observability/opentelemetry-best-practices/)
25. [Practical Guide to Distributed Tracing with Jaeger — Better Stack](https://betterstack.com/community/guides/observability/jaeger-guide/)
26. [AWS X-Ray Pricing — Amazon Web Services](https://aws.amazon.com/xray/pricing/)
27. [AWS X-Ray Pros and Cons 2025 — PeerSpot](https://www.peerspot.com/products/aws-x-ray-pros-and-cons)
28. [Azure Monitor Pricing — Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/monitor/)
29. [Application Insights FAQ — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/app/application-insights-faq)
30. [What Is Google Cloud Trace — Dash0](https://www.dash0.com/knowledge/what-is-google-cloud-trace)
31. [Distributed Tracing Best Practices 2025 — Apica](https://www.apica.io/blog/what-is-distributed-tracing-how-it-works-and-best-practices/)
32. [Cost-Aware Observability on K8s — Cloud Native Now](https://cloudnativenow.com/contributed-content/cost-aware-observability-on-k8s-balancing-scrape-intervals-retention-and-cardinality/)
33. [Telemetry Correlation: Traces, Metrics, Logs — Ubuntu Observability Docs](https://documentation.ubuntu.com/observability/track-2/explanation/telemetry-correlation/)
34. [Distributed Systems Observability 2025 — EdgeDelta](https://edgedelta.com/company/knowledge-center/distributed-systems-observability)
35. [Top MinIO and Ceph S3 Alternatives 2025 — Cubbit/Medium](https://medium.com/cubbit/top-minio-and-ceph-s3-alternatives-in-2025-european-gems-inside-b99aa4c6abb6)
36. [Open Source Distributed Tracing Tools — Uptrace](https://uptrace.dev/tools/distributed-tracing-tools)
37. [11 Best Distributed Tracing Tools 2025 — Better Stack](https://betterstack.com/community/comparisons/distributed-tracing-tools/)
