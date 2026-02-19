# F50 — On-Premises Monitoring & Alerting

**Research Area:** Self-Hosted Monitoring Stack — Operational Characteristics and Trade-offs
**Scope:** Metrics, monitoring, and alerting only. Logging covered in F49; tracing in F51.
**Date:** 2025-02-18

---

## Executive Summary

Self-hosting a production-grade monitoring and alerting stack — anchored by Prometheus, Grafana, and Alertmanager — carries substantial operational depth that is routinely underestimated. At small scale (tens of nodes), a vanilla Prometheus deployment is tractable; at enterprise scale (hundreds of nodes, millions of active time series), the stack demands dedicated engineering investment in high-availability architecture (Thanos or Mimir), cardinality governance, and storage capacity planning. The single largest hidden cost is not software licensing but ongoing operational engineering: cardinality explosions, dashboard sprawl, and on-call rotation for the monitoring infrastructure itself. Managed alternatives (Amazon Managed Service for Prometheus, Azure Monitor Managed Prometheus, Google Cloud Managed Prometheus) eliminate infrastructure management entirely but introduce per-sample pricing that can become prohibitive at very high ingest volumes. ISVs must weigh the total cost of engineering time against the predictable dollar cost of managed services against their data-gravity and sovereignty constraints.

---

## 1. Prometheus — Core Deployment and Local TSDB

### 1.1 Deployment Model

Prometheus scrapes metrics from instrumented targets on a pull model. It is deployed as a single stateful binary with an embedded time-series database (TSDB). Node-level deployment via DaemonSet (node-exporter) and cluster-state collection via kube-state-metrics are the two foundational scrape targets in any Kubernetes environment. Application metrics are exposed on `/metrics` endpoints and scraped at configurable intervals (default: 15s).

[Prometheus official storage documentation](https://prometheus.io/docs/prometheus/latest/storage/) describes the TSDB as a local, append-only database organized in two-hour blocks on disk, with the most recent data held in an in-memory write-ahead log (WAL).

### 1.2 Storage: Local TSDB Characteristics

The Prometheus TSDB compresses time-series data efficiently. The official formula for estimating disk requirements is:

```
needed_disk_space = retention_time_seconds × ingested_samples_per_second × bytes_per_sample
```

[FACT] Prometheus official documentation specifies approximately 1–2 bytes per sample after compression, with 1.5 bytes recommended as a planning baseline.
— Source: [Robust Perception — How much disk space do Prometheus blocks use?](https://www.robustperception.io/how-much-disk-space-do-prometheus-blocks-use/)

Practical storage estimates for a 100-node Kubernetes cluster ingesting 100,000 samples/second:

| Retention Period | Estimated Disk Requirement |
|-----------------|---------------------------|
| 15 days (default) | ~195 GB |
| 90 days | ~1.17 TB |
| 1 year | ~4.73 TB |

[FACT] The official recommendation is to set the retention size limit to at most 80–85% of allocated disk space to provide a buffer against peak cardinality events.
— Source: [Better Stack — How to Increase Prometheus Storage Retention](https://betterstack.com/community/guides/monitoring/prometheus-storage-retention/)

### 1.3 Memory Requirements

[FACT] A general production planning estimate is approximately 3 kB RAM per active time series; a cluster with 1 million active series requires roughly 3 GB RAM for the data plane alone, excluding query overhead.
— Source: [SigNoz — How to Reduce Prometheus High Memory Usage](https://signoz.io/guides/why-does-prometheus-consume-so-much-memory/)

[FACT] A documented production case involved a Prometheus instance with over 5 million active time series that required a machine with 1,024 GB RAM.
— Source: [GitHub — Prometheus issue #13584, high memory usage with 1200+ ServiceMonitors](https://github.com/prometheus/prometheus/issues/13584)

[FACT] The `prometheus_tsdb_head_series` metric is the primary cardinality indicator. A rule of thumb for the upper limit of in-memory series is total available physical memory divided by 10,000 (e.g., approximately 6 million memory series on a 64 GiB server).
— Source: [Palark — Understanding and optimizing resource consumption in Prometheus](https://palark.com/blog/prometheus-resource-consumption-optimization/)

---

## 2. High Availability — Thanos, Mimir, and Cortex

### 2.1 Baseline HA with Redundant Prometheus Instances

The foundational HA pattern is deploying two or more identical Prometheus instances scraping the same targets using identical `scrape_configs`. Each instance operates independently; there is no replication between them. This eliminates single-point-of-failure on the scrape path but does not provide a unified query layer.

[FACT] Thanos Query communicates with Thanos Sidecar instances via gRPC and de-duplicates metrics across all Prometheus replicas when executing a query, using the `--query.replica-label` flag to identify and collapse duplicate series.
— Source: [InfraCloud — Prometheus HA with Thanos Sidecar or Receiver?](https://www.infracloud.io/blogs/prometheus-ha-thanos-sidecar-receiver/)

### 2.2 Thanos Architecture

Thanos adds long-term storage and global query capability to existing Prometheus deployments through a composable component model:

- **Sidecar**: Runs alongside each Prometheus pod; uploads completed 2-hour TSDB blocks to object storage (S3, GCS, Azure Blob, or S3-compatible on-premises stores); exposes StoreAPI to the Querier
- **Querier**: Stateless, horizontally scalable; fans out PromQL queries across all StoreAPI endpoints; deduplicates replicated series
- **Store Gateway**: Serves historical data from object storage blocks, enabling queries beyond local retention
- **Compactor**: Applies downsampling (5-minute and 1-hour resolution) and merges blocks in object storage; runs as a single non-HA instance
- **Ruler**: Evaluates recording and alerting rules against the global Thanos query layer

[FACT] Thanos Sidecar requires Prometheus to be configured with `--storage.tsdb.min-block-duration=2h` and `--storage.tsdb.max-block-duration=2h` so that only complete blocks are uploaded to object storage.
— Source: [Thanos — Getting Started documentation](https://thanos.io/tip/thanos/getting-started.md/)

[FACT] Thanos is a CNCF Incubating project; it works in Kubernetes and on bare metal. The Sidecar component is designed to be added to an existing Prometheus deployment without scrape-path disruption.
— Source: [GitHub — thanos-io/thanos repository](https://github.com/thanos-io/thanos)

### 2.3 Grafana Mimir

Grafana Mimir is a fork of Cortex, purpose-built for multi-tenant, horizontally scalable long-term Prometheus storage.

[FACT] Grafana Mimir supports three deployment modes: (1) Monolithic — all components in a single binary; (2) Read-Write — experimental split of read and write paths; (3) Microservices/Distributed — each component (Distributor, Ingester, Querier, Query Frontend, Compactor, Store Gateway, Ruler) deployed independently.
— Source: [Medium — Grafana Mimir as a long-term storage for Prometheus metrics, Part 1](https://medium.com/@kedarnath93/grafana-mimir-as-a-long-term-storage-for-prometheus-metrics-part-1-7aa00144fae3)

[FACT] Grafana Mimir is compatible with AWS S3, Google Cloud Storage, Azure Blob Storage, OpenStack Swift, and any S3-compatible object storage, making on-premises deployment possible with Ceph, MinIO, or similar S3-compatible systems.
— Source: [GitHub — grafana/mimir repository](https://github.com/grafana/mimir)

[FACT] "Mimir is multitenant from day 1, whereas this is a relatively new thing in Thanos."
— Source: [GitHub Discussion — What's the difference between Mimir and Thanos? grafana/mimir #3380](https://github.com/grafana/mimir/discussions/3380)

### 2.4 Thanos vs. Mimir Decision Framework

| Dimension | Thanos | Grafana Mimir |
|-----------|--------|---------------|
| Migration path | Smoothest — sidecar attaches to existing Prometheus | Requires remote-write reconfiguration |
| Multi-tenancy | Retroactively added | Native from inception |
| Operational complexity | Moderate — 5–6 discrete components | High — 8+ microservices in distributed mode |
| HA for compaction | Single compactor (non-HA) | Distributed compactor with ring |
| Object storage backend | S3, GCS, Azure, Filesystem | Same, plus OpenStack Swift |
| Best fit | Teams with existing Prometheus, moderate scale | ISVs requiring strict tenant isolation or >100M series |

Source: [onidel.com — Thanos vs VictoriaMetrics vs Grafana Mimir Performance Comparison 2025](https://onidel.com/blog/prometheus-storage-comparison-2025)

---

## 3. Federation and Scale Patterns

### 3.1 Hierarchical Federation

For organizations unable to adopt Thanos or Mimir, Prometheus native federation (`/federate` endpoint) provides a hierarchical aggregation pattern.

[FACT] Flipkart used hierarchical federation to manage approximately 2,000 API Gateway instances each emitting roughly 40,000 metrics, resulting in 80 million raw time-series. Local Prometheus servers applied recording rules to drop high-cardinality instance labels, collapsing 80 million raw series into tens of thousands of cluster-level metrics exposed via `/federate`.
— Source: [InfoQ — Flipkart Scales Prometheus to 80 Million Metrics Using Hierarchical Federation, October 2025](https://www.infoq.com/news/2025/10/flipkart-prometheus-80million/)

[FACT] The Flipkart approach cautions that hierarchical federation loses per-instance debugging fidelity and is less suitable when per-instance anomaly detection across clusters is required.
— Source: [Medium — Scaling With Prometheus: Managing 80M Metrics Smoothly](https://kapillamba4.medium.com/hierarchical-federation-in-prometheus-managing-millions-of-metrics-cleanly-8d8bac940ff3)

---

## 4. Cardinality Management

### 4.1 The Cardinality Explosion Problem

Cardinality in Prometheus is defined by the number of unique time series — each unique combination of metric name and label values creates a separate time series stored, indexed, and queried independently.

[FACT] "A cardinality explosion can quickly exhaust available resources and bring down your monitoring system. When an excessive number of time series is created due to high variation in label values, it makes it difficult for Prometheus to efficiently process or store the data. In extreme cases, this can exhaust memory, causing the server to crash."
— Source: [Last9 — How to Manage High Cardinality Metrics in Prometheus](https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/)

[FACT] A 100-node Kubernetes cluster with 2,000 pods can expose more than 500,000 unique time-series metrics, with each metric scraped every 15–30 seconds, producing millions of data points per minute.
— Source: [atmosly.com — Kubernetes Metrics: What to Monitor and Why (2025 Guide)](https://atmosly.com/blog/kubernetes-metrics-what-to-monitor-and-why-2025)

### 4.2 Label Management Best Practices

[FACT] Core anti-patterns that trigger cardinality explosions include: using user IDs, request IDs, session tokens, or timestamps as label values; unbounded HTTP path labels (e.g., `/api/users/{id}`); and per-pod labels without aggregation.
— Source: [SigNoz — What are the Limitations of Prometheus Labels?](https://signoz.io/guides/what-are-the-limitations-of-prometheus-labels/)

[FACT] Prometheus relabeling (`metric_relabel_configs`) can be used at scrape time to drop high-cardinality labels before they are ingested into the TSDB, preventing cardinality growth at the source rather than after ingestion.
— Source: [Grafana Labs Blog — How to manage high cardinality metrics in Prometheus and Kubernetes](https://grafana.com/blog/2022/10/20/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/)

[FACT] The metric `prometheus_tsdb_head_series` is the primary cardinality health indicator. Sudden jumps in this metric indicate a cardinality event requiring immediate investigation.
— Source: [Medium — Mastering Prometheus: Taming the Cardinality Beast, September 2025](https://medium.com/@kyberneees/mastering-prometheus-taming-the-cardinality-beast-01484a5a7267)

---

## 5. Metric Collection — Exporters and Agent Deployment

### 5.1 Core Exporters

**node-exporter**: Deployed as a Kubernetes DaemonSet — one instance per node — collecting hardware and OS-level metrics: CPU, memory, disk I/O, network, filesystem.

[FACT] "Node exporter is deployed on all the Kubernetes nodes as a daemonset. Daemonset makes sure one instance of node-exporter is running in all the nodes."
— Source: [DevOpsCube — How to Setup Prometheus Node Exporter on Kubernetes](https://devopscube.com/node-exporter-kubernetes/)

**kube-state-metrics (KSM)**: A cluster-level deployment (typically a single replica or sharded for large clusters) that generates metrics about the state of Kubernetes objects: Pods, Deployments, StatefulSets, Nodes, Jobs, PersistentVolumes.

[FACT] "Resource usage for kube-state-metrics changes with the Kubernetes objects (Pods/Nodes/Deployments/Secrets etc.) size of the cluster. To some extent, the Kubernetes objects in a cluster are in direct proportion to the node number of the cluster."
— Source: [GitHub — kubernetes/kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)

[FACT] For large-scale deployments, KSM supports sharding — multiple KSM instances monitoring different subsets of namespaces or clusters — to prevent a single KSM instance from becoming a bottleneck.
— Source: [Spacelift — Kubernetes Observability With Kube-State-Metrics: Guide](https://spacelift.io/blog/kube-state-metrics)

**Application metrics**: Custom exporters expose domain-specific metrics via Prometheus client libraries (Go, Python, Java, Rust). Each application service adds its own `/metrics` endpoint to the Prometheus scrape configuration.

### 5.2 Operational Complexity at Scale

At 100+ nodes, the scrape target list and service discovery configuration become significant management artifacts. The Prometheus Operator (CRD-based) or Agent mode reduces this burden by generating scrape configurations declaratively from `ServiceMonitor` and `PodMonitor` CRDs.

[FACT] Managing Prometheus configurations across many clusters manually is error-prone and leads to configuration drift; GitOps-based management using PrometheusRule CRDs and Helm templates is the recommended pattern for enterprise-scale deployments.
— Source: [Aviator — Manage Prometheus alerts in Kubernetes With GitOps](https://www.aviator.co/blog/managing-prometheus-alerts-in-kubernetes-using-gitops/)

---

## 6. Grafana — Dashboard Management and Provisioning

### 6.1 Alerting Architecture

Grafana's unified alerting layer (introduced as default in Grafana 9+) consolidates alert rule management, contact points, and notification policies within Grafana itself, using Alertmanager as the backend routing engine.

[FACT] Grafana includes built-in support for Alertmanager implementations from Prometheus and Mimir, allowing users to view and manage silences, contact points, and notification policies from a single UI.
— Source: [Grafana documentation — Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)

### 6.2 Provisioning and Infrastructure as Code

[FACT] Grafana 12 introduces a "Git Sync" feature that stores dashboard files in a GitHub repository and synchronizes changes with Grafana, enabling version control, branching, and pull requests natively within Grafana.
— Source: [Grafana Labs Blog — Observability as code: automate observability workflows and manage dashboards as code in Grafana 12](https://grafana.com/blog/observability-as-code-grafana-12/)

[FACT] IaC tooling available for Grafana in 2025 includes: (1) Terraform provider for managing dashboards, alerts, and collectors; (2) Grafana Operator — a Kubernetes operator for provisioning Grafana resources; (3) grafanactl — a CLI tool designed for REST API-based management in CI/CD pipelines.
— Source: [Grafana documentation — Provision Grafana Cloud with infrastructure as code](https://grafana.com/docs/grafana/latest/as-code/infrastructure-as-code/)

### 6.3 User Management — RBAC, SSO, and LDAP

[FACT] Grafana RBAC provides granular permission management for dashboards, reports, and administrative settings. Grafana Enterprise supports custom roles in addition to fixed system roles (Viewer, Editor, Admin).
— Source: [Grafana documentation — Role-based access control (RBAC)](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/)

[FACT] Grafana Enterprise supports SSO via OAuth 2.0 and SAML, LDAP group-to-team synchronization, multi-factor authentication (MFA), and audit logging as enterprise-tier features.
— Source: [Grafana Labs — An overview of Grafana SSO: Benefits, recent updates, and best practices](https://grafana.com/blog/an-overview-of-grafana-sso-benefits-recent-updates-and-best-practices-to-get-started/)

### 6.4 Dashboard Sprawl and Governance

Dashboard sprawl is a chronic operational problem in self-hosted Grafana deployments. Without governance, organizations accumulate hundreds of dashboards with overlapping scope, no designated owners, and complex PromQL queries that degrade Grafana and Prometheus performance under load.

[UNVERIFIED] Typical enterprise Grafana installations without governance controls accumulate 200–500+ dashboards within 18–24 months, with an estimated 40–60% stale or duplicative. This estimate is based on practitioner reports from SRE community forums and aligns with the general pattern of observability tool sprawl documented in the 2025 SRE Report, but no peer-reviewed or vendor-published statistic was located for this specific claim.

Mitigation patterns include:
- Provisioning all dashboards via code (GitOps) so ad-hoc creation is blocked or tracked
- Mandatory folder ownership with Grafana RBAC enforcing write permissions per team
- Dashboard aging policies: auto-archival of dashboards not accessed within 90 days
- Recording rules to pre-compute expensive PromQL expressions, reducing per-query load

---

## 7. Alertmanager — Routing, Grouping, and Notification

### 7.1 Core Alertmanager Functions

[FACT] Alertmanager receives alerts from Prometheus (or Grafana), handles deduplication, grouping, routing, inhibition, and silencing, and dispatches notifications to receivers including PagerDuty, Slack, email, OpsGenie, and webhooks.
— Source: [Prometheus Alertmanager — GitHub repository](https://github.com/prometheus/alertmanager)

### 7.2 Routing Tree

The routing tree is the core configuration artifact in Alertmanager, determining which alerts go to which receivers and how they are grouped.

[FACT] Alertmanager routing configuration supports three key timing parameters: `group_wait` (how long to wait before sending the first notification for a new group), `group_interval` (how long to wait before sending notification for newly added alerts to an existing group), and `repeat_interval` (how long to wait before re-sending an ongoing alert notification).
— Source: [DoHost — Understanding Alertmanager's Core Concepts: Grouping, Routing, and Inhibition, September 2025](https://dohost.us/index.php/2025/09/28/understanding-alertmanagers-core-concepts-grouping-routing-and-inhibition/)

### 7.3 Inhibition and Silencing

[FACT] Inhibition suppresses downstream alert notifications when a higher-severity upstream alert is already firing, using label matchers. Example: suppress all disk-space warnings on a node where a `NodeNotReady` critical alert is active.
— Source: [Sysdig — Prometheus Alertmanager Best Practices](https://www.sysdig.com/blog/prometheus-alertmanager)

[FACT] Recommended severity-based routing pattern: `severity=critical` AND `env=prod` routes to PagerDuty plus team Slack channel; `severity=warning` routes to Slack only with strict grouping and repeat intervals; `env!=prod` routes to quiet channels with no after-hours notifications.
— Source: [Medium/DataOps.tech — Routing alerts in Slack/PagerDuty by severity, so noise doesn't kill you](https://medium.com/dataops-tech/routing-alerts-in-slack-pagerduty-by-severity-so-noise-doesnt-kill-you-874060ef2996)

---

## 8. Comparison: Self-Hosted vs. Managed Monitoring Services

### 8.1 What Managed Services Eliminate

| Responsibility | On-Premises | Managed K8s (self-hosted stack) | Cloud-Native (managed services) |
|---------------|-------------|--------------------------------|--------------------------------|
| Prometheus version upgrades | Manual, operator-managed | Manual, operator-managed | Eliminated |
| TSDB disk provisioning | Manual LVM/storage ops | PVC management | Eliminated |
| HA/failover configuration | Thanos/Mimir architecture | Same, but on managed K8s | Eliminated |
| Cardinality governance | Entirely self-managed | Entirely self-managed | Partially managed (quotas) |
| Alertmanager HA | Requires mesh or Mimir | Same | Eliminated |
| Certificate/TLS management | Manual | Cert-manager or manual | Eliminated |
| Object storage backend | On-prem Ceph/MinIO | Cloud bucket | Managed |
| Retention enforcement | Manual flag + storage ops | Same | Automatic |
| Dashboard hosting | Self-hosted Grafana | Self-hosted or managed | Grafana Cloud or native |

### 8.2 Managed Service Pricing (2025)

[FACT] Amazon Managed Service for Prometheus pricing: $0.90 per 10,000,000 metric samples ingested (first 2 billion samples); storage charged per GB of metric samples and metadata retained; query samples processed (QSP) billed separately. No upfront fees or minimums.
— Source: [AWS — Amazon Managed Service for Prometheus Pricing](https://aws.amazon.com/prometheus/pricing/)

[FACT] Cost comparison at very high scale: VictoriaMetrics analysis found that ingesting 1 million samples/second at equivalent performance cost approximately $6,000/month on self-hosted infrastructure, while Amazon Managed Service for Prometheus at the same ingest rate would cost approximately $47,000/month (approximately 7.8x higher), and Google Cloud Managed Service for Prometheus approximately $327,000/month (approximately 54x higher).
— Source: [VictoriaMetrics — Pricing comparison for Managed Prometheus](https://victoriametrics.com/blog/managed-prometheus-pricing/)

[FACT] Managed Prometheus services from all three major clouds guarantee SLAs of 99.9% uptime or higher, with automatic multi-availability-zone replication and failover — capabilities that require explicit Thanos or Mimir architecture to replicate self-hosted.
— Source: [Last9 — Self-managed Prometheus vs Managed Prometheus](https://last9.io/blog/self-managed-prometheus-vs-managed-prometheus/)

### 8.3 What Does NOT Disappear with Managed Services

Even when adopting fully managed monitoring services (CloudWatch Metrics, Azure Monitor, Google Cloud Monitoring), ISVs retain responsibility for:

- Instrument application code with correct metrics, labels, and cardinality discipline
- Design alerting rules and notification routing policies
- Build and maintain dashboards (though Grafana Cloud or native console is managed)
- Manage alert fatigue and on-call processes
- Define retention policies and control costs via cardinality and scrape interval tuning

---

## 9. Operational Profiles and FTE Estimates

**Assumptions:**
- Medium deployment: 50–200 nodes, 1–5 million active time series, 90-day local retention or Thanos with S3 backend
- Large deployment: 200+ nodes, 5–50 million active time series, Thanos or Mimir, multi-cluster
- FTE estimates represent dedicated platform/SRE engineering capacity for the monitoring domain only
- On-call burden is stated separately as it represents shared responsibility (not full-time allocation)

### Comparison Table

| Capability | On-Premises | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native (Managed Services) |
|------------|-------------|-----------------------------------|----------------------------------|
| **Prometheus Deployment** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Manual binary/systemd or Helm | Prometheus Operator + Helm | No deployment required |
| | Storage provisioning, upgrade runbooks | PVC management, operator upgrades | AWS AMP / Azure Monitor / GCP Managed Prometheus |
| | Est. FTE: 0.5 (medium), 1.0 (large) | Est. FTE: 0.3 (medium), 0.7 (large) | Est. FTE: 0.1 (any scale) |
| **HA / Long-Term Storage** | Difficulty: 4/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Thanos or Mimir + on-prem object storage | Thanos or Mimir + cloud object storage | Included in managed service SLA |
| | Compactor, Store Gateway, Querier ops | Same, K8s simplifies pod management | No architecture required |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.3–0.7 | Est. FTE: 0.0 |
| **Cardinality Governance** | Difficulty: 4/5 | Difficulty: 4/5 | Difficulty: 3/5 |
| | Label auditing, relabeling rules, quotas | Same | Quotas exist but design discipline still required |
| | prometheus_tsdb_head_series monitoring | Same | Vendor-side quotas help but cost exposure remains |
| | Est. FTE: 0.2–0.5 | Est. FTE: 0.2–0.5 | Est. FTE: 0.1–0.3 |
| **Grafana Operations** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-hosted, version upgrades, plugin management | Helm + Grafana Operator | Grafana Cloud managed |
| | SSO/LDAP configuration, RBAC setup | Same | Included in Grafana Cloud Enterprise |
| | Est. FTE: 0.3–0.5 | Est. FTE: 0.2–0.3 | Est. FTE: 0.1 |
| **Alertmanager Operations** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Routing tree design, HA mesh config | Same, K8s manages availability | Managed within Grafana Cloud or native alerting |
| | PagerDuty/Slack webhook management | Same | Same — policy design remains |
| | Est. FTE: 0.2–0.3 | Est. FTE: 0.1–0.2 | Est. FTE: 0.1 |
| **Dashboard Governance** | Difficulty: 4/5 | Difficulty: 4/5 | Difficulty: 3/5 |
| | GitOps provisioning, sprawl control, ownership | Same | Same — problem is organizational, not infrastructure |
| | Grafana-as-code (Terraform, grafanactl) | Same | Same tools available |
| | Est. FTE: 0.2–0.4 | Est. FTE: 0.2–0.4 | Est. FTE: 0.1–0.2 |

**Total FTE Estimates:**

| Scale | On-Premises | Managed Kubernetes | Cloud-Native |
|-------|------------|-------------------|--------------|
| Medium (50–200 nodes) | 1.5–2.5 FTE | 1.0–1.7 FTE | 0.3–0.6 FTE |
| Large (200+ nodes) | 2.5–4.0 FTE | 1.7–2.7 FTE | 0.5–1.0 FTE |
| **On-call burden (additional)** | 0.5–1.0 FTE equivalent | 0.3–0.5 FTE equivalent | 0.1–0.2 FTE equivalent |

[FACT] "The burden of operational tasks has grown for the first time in five years among most SRE teams, with the expectation that AI would reduce toil rather than exacerbate it. The median percentage of work SREs spend on operational toil has risen to 30%."
— Source: [Catchpoint — The SRE Report 2025](https://www.catchpoint.com/press-releases/the-sre-report-2025-highlighting-critical-trends-in-site-reliability-engineering)

[FACT] "Startups with two SREs have no appetite for 3 a.m. Thanos upgrades, and a managed backend is rational" — practitioner characterization of the operational threshold at which managed monitoring becomes structurally superior.
— Source: [Spectro Cloud — Choosing the right Kubernetes monitoring stack in 2025](https://www.spectrocloud.com/blog/choosing-the-right-kubernetes-monitoring-stack)

---

## 10. Cross-References

- See F49 (Logging) for log aggregation stack (Loki, Elasticsearch) — separate from metrics pipeline discussed here
- See F51 (Distributed Tracing) for Jaeger/Tempo/OpenTelemetry trace pipeline — Prometheus metrics and traces share exporters but diverge at the collector level
- See F04 (Infrastructure Compute) for on-premises server sizing and storage provisioning that underlies the disk and RAM requirements stated in Sections 1.2 and 1.3

---

## Key Takeaways

- **Cardinality is the primary operational risk in self-hosted Prometheus.** A 100-node cluster can trivially generate 500,000+ active time series; without label governance and relabeling rules, cardinality explosions crash the monitoring system — i.e., the monitoring system itself becomes the outage. This risk exists in all three deployment models but is entirely the ISV's responsibility in on-premises and managed Kubernetes deployments.

- **HA and long-term storage require a second architectural layer.** A single Prometheus instance is not HA. Thanos (moderate complexity, best migration path) or Grafana Mimir (higher complexity, native multi-tenancy) must be deployed and operated as distinct infrastructure. This adds 0.5–1.5 FTE operational burden on-premises or on managed Kubernetes. Cloud-native managed services include HA by default with 99.9%+ SLAs.

- **Managed monitoring services are cost-effective at low-to-medium scale but can become expensive at very high ingest volumes.** At 1 million samples/second, Amazon Managed Service for Prometheus has been benchmarked at approximately 7.8x the cost of equivalent self-hosted infrastructure, and Google Cloud at approximately 54x. ISVs above ~500,000 samples/second should model total cost of ownership carefully against operational FTE savings.

- **Dashboard sprawl and Alertmanager routing discipline are organizational problems that persist across all deployment models.** Moving to managed Prometheus or Grafana Cloud does not resolve stale dashboards, alert fatigue, or poorly designed routing trees — these require explicit governance policies, GitOps-enforced provisioning, and assigned dashboard ownership regardless of infrastructure model.

- **GitOps is the 2025 standard for monitoring configuration management.** PrometheusRule CRDs, Grafana Terraform providers, and grafanactl CLI tools enable monitoring-as-code workflows that eliminate configuration drift across multi-cluster environments. The Grafana 12 Git Sync feature is a milestone for native dashboard version control without external tooling.

---

## Sources

1. [Prometheus — Storage documentation](https://prometheus.io/docs/prometheus/latest/storage/)
2. [Robust Perception — How much disk space do Prometheus blocks use?](https://www.robustperception.io/how-much-disk-space-do-prometheus-blocks-use/)
3. [Robust Perception — Configuring Prometheus storage retention](https://www.robustperception.io/configuring-prometheus-storage-retention/)
4. [Better Stack — How to Increase Prometheus Storage Retention](https://betterstack.com/community/guides/monitoring/prometheus-storage-retention/)
5. [Last9 — How to Configure and Optimize Prometheus Data Retention](https://last9.io/blog/prometheus-data-retention/)
6. [SigNoz — How to Reduce Prometheus High Memory Usage](https://signoz.io/guides/why-does-prometheus-consume-so-much-memory/)
7. [GitHub — prometheus/prometheus issue #13584 high memory usage](https://github.com/prometheus/prometheus/issues/13584)
8. [Palark — Understanding and optimizing resource consumption in Prometheus](https://palark.com/blog/prometheus-resource-consumption-optimization/)
9. [Thanos — Getting Started documentation](https://thanos.io/tip/thanos/getting-started.md/)
10. [GitHub — thanos-io/thanos repository](https://github.com/thanos-io/thanos)
11. [InfraCloud — Prometheus HA with Thanos Sidecar or Receiver?](https://www.infracloud.io/blogs/prometheus-ha-thanos-sidecar-receiver/)
12. [GitHub — grafana/mimir repository](https://github.com/grafana/mimir)
13. [GitHub Discussion — Mimir vs Thanos, grafana/mimir #3380](https://github.com/grafana/mimir/discussions/3380)
14. [Medium — Grafana Mimir as long-term storage, Part 1](https://medium.com/@kedarnath93/grafana-mimir-as-a-long-term-storage-for-prometheus-metrics-part-1-7aa00144fae3)
15. [onidel.com — Thanos vs VictoriaMetrics vs Grafana Mimir Performance Comparison 2025](https://onidel.com/blog/prometheus-storage-comparison-2025)
16. [InfoQ — Flipkart Scales Prometheus to 80 Million Metrics, October 2025](https://www.infoq.com/news/2025/10/flipkart-prometheus-80million/)
17. [Medium — Scaling With Prometheus: Managing 80M Metrics Smoothly](https://kapillamba4.medium.com/hierarchical-federation-in-prometheus-managing-millions-of-metrics-cleanly-8d8bac940ff3)
18. [Last9 — How to Manage High Cardinality Metrics in Prometheus](https://last9.io/blog/how-to-manage-high-cardinality-metrics-in-prometheus/)
19. [atmosly.com — Kubernetes Metrics: What to Monitor and Why (2025 Guide)](https://atmosly.com/blog/kubernetes-metrics-what-to-monitor-and-why-2025)
20. [SigNoz — What are the Limitations of Prometheus Labels?](https://signoz.io/guides/what-are-the-limitations-of-prometheus-labels/)
21. [Grafana Labs Blog — How to manage high cardinality metrics in Prometheus and Kubernetes](https://grafana.com/blog/2022/10/20/how-to-manage-high-cardinality-metrics-in-prometheus-and-kubernetes/)
22. [Medium — Mastering Prometheus: Taming the Cardinality Beast, September 2025](https://medium.com/@kyberneees/mastering-prometheus-taming-the-cardinality-beast-01484a5a7267)
23. [DevOpsCube — How to Setup Prometheus Node Exporter on Kubernetes](https://devopscube.com/node-exporter-kubernetes/)
24. [GitHub — kubernetes/kube-state-metrics repository](https://github.com/kubernetes/kube-state-metrics)
25. [Spacelift — Kubernetes Observability With Kube-State-Metrics](https://spacelift.io/blog/kube-state-metrics)
26. [Aviator — Manage Prometheus alerts in Kubernetes With GitOps](https://www.aviator.co/blog/managing-prometheus-alerts-in-kubernetes-using-gitops/)
27. [Grafana documentation — Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)
28. [Grafana Labs Blog — Observability as code: Grafana 12](https://grafana.com/blog/observability-as-code-grafana-12/)
29. [Grafana documentation — Infrastructure as code](https://grafana.com/docs/grafana/latest/as-code/infrastructure-as-code/)
30. [Grafana documentation — RBAC](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/)
31. [Grafana Labs — Overview of Grafana SSO](https://grafana.com/blog/an-overview-of-grafana-sso-benefits-recent-updates-and-best-practices-to-get-started/)
32. [GitHub — prometheus/alertmanager repository](https://github.com/prometheus/alertmanager)
33. [DoHost — Understanding Alertmanager's Core Concepts, September 2025](https://dohost.us/index.php/2025/09/28/understanding-alertmanagers-core-concepts-grouping-routing-and-inhibition/)
34. [Sysdig — Prometheus Alertmanager Best Practices](https://www.sysdig.com/blog/prometheus-alertmanager)
35. [Medium/DataOps.tech — Routing alerts in Slack/PagerDuty by severity](https://medium.com/dataops-tech/routing-alerts-in-slack-pagerduty-by-severity-so-noise-doesnt-kill-you-874060ef2996)
36. [AWS — Amazon Managed Service for Prometheus Pricing](https://aws.amazon.com/prometheus/pricing/)
37. [VictoriaMetrics — Pricing comparison for Managed Prometheus](https://victoriametrics.com/blog/managed-prometheus-pricing/)
38. [Last9 — Self-managed Prometheus vs Managed Prometheus](https://last9.io/blog/self-managed-prometheus-vs-managed-prometheus/)
39. [Catchpoint — The SRE Report 2025](https://www.catchpoint.com/press-releases/the-sre-report-2025-highlighting-critical-trends-in-site-reliability-engineering)
40. [Spectro Cloud — Choosing the right Kubernetes monitoring stack in 2025](https://www.spectrocloud.com/blog/choosing-the-right-kubernetes-monitoring-stack)
