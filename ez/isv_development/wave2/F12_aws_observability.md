# F12: AWS Observability Services

**Agent ID:** F12
**Research Question:** What managed observability services does AWS provide for logging, monitoring, tracing, and alerting, and what do they abstract away?
**Scope:** AWS observability only. Security logging covered in F11; other cloud providers are out of scope.

---

## Executive Summary

AWS offers a vertically integrated observability stack — CloudWatch Logs, CloudWatch Metrics, AWS X-Ray, CloudWatch Application Signals, Amazon Managed Grafana, Amazon Managed Service for Prometheus, AWS CloudTrail, and the AWS Distro for OpenTelemetry — that eliminates the need to provision, operate, or scale any observability infrastructure. For ISVs deploying cloud-native SaaS on AWS, this stack abstracts away all storage backends, ingestion pipelines, retention management, and capacity planning that self-hosted alternatives (e.g., the ELK stack, self-managed Prometheus/Grafana, Jaeger) require. A critical strategic signal for ISVs evaluating this stack: AWS announced in October 2025 that the proprietary X-Ray SDKs and Daemon will reach end-of-support on February 25, 2027, directing all new instrumentation toward OpenTelemetry — a vendor-neutral standard — with ADOT (AWS Distro for OpenTelemetry) serving as the managed on-ramp. This convergence on open standards materially reduces lock-in risk while preserving full managed-service benefits. Pricing for the stack is consumption-based with no upfront commitment, but at scale, CloudWatch costs — particularly custom metrics and Logs Insights queries — can become a material line item that requires active cost governance.

---

## 1. Amazon CloudWatch Logs

### 1.1 Log Ingestion

CloudWatch Logs supports two log classes with distinct cost profiles:

[FACT] The **Standard log class** supports all CloudWatch Logs features. The **Infrequent Access log class** incurs ingestion charges approximately 50% lower per GB than the Standard class, but does not support the `pattern`, `diff`, and `unmask` Logs Insights query commands.
— [AWS CloudWatch Log Classes Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)

[STATISTIC] Standard log ingestion pricing for US East (N. Virginia): **$0.50 per GB** for the first 10 TB/month, stepping down to **$0.25/GB** (next 20 TB), **$0.10/GB** (next 20 TB), and **$0.05/GB** (above 50 TB/month). Infrequent Access mirrors at approximately half those rates: **$0.25/GB** for the first 10 TB/month.
— [AWS CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/), [CloudWatch Pricing Explained Guide 2025](https://cloudchipr.com/blog/cloudwatch-pricing)

[FACT] The free tier includes **5 GB of log ingestion per month**.
— [AWS CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)

**What this abstracts away:** The ISV does not manage ingestion pipelines, message brokers, or ingest-side buffer capacity. AWS handles durability, fan-out to multiple subscribers (Lambda, Kinesis Data Streams, OpenSearch), and compression.

### 1.2 Log Retention

[FACT] By default, CloudWatch log groups retain logs **indefinitely**. Retention policies can be set per log group to any period from **1 day to 10 years (3,653 days)**.
— [Amazon CloudWatch Logs — What Is CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

[STATISTIC] Log storage pricing (both Standard and Infrequent Access log classes): **$0.03 per GB per month**.
— [AWS CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)

### 1.3 Logs Insights Query Language

[FACT] CloudWatch Logs Insights supports three query languages: (1) the native **Logs Insights QL** with commands including `filter`, `stats`, `sort`, `limit`, `parse`, `pattern`, `diff`, and `unmask`; (2) **OpenSearch Piped Processing Language (PPL)**; and (3) **OpenSearch SQL**.
— [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)

[FACT] As of June 2025, CloudWatch Logs Insights launched **Query Results Summarization** — a generative AI feature that produces a natural language summary of query results — and enhanced OpenSearch PPL with new commands including `JOIN`, `SubQuery`, `Fillnull`, `Expand`, `Flatten`, `Cidrmatch`, and JSON functions.
— [AWS What's New: CloudWatch Logs Insights Query Results Summarization, June 2025](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-cloudwatch-logs-insights-query-results-summarization-opensearch-ppl-enhancements/)

[FACT] As of August 2025, AWS launched **natural language query generation for OpenSearch PPL and SQL** in CloudWatch Logs Insights, enabling users to generate queries from plain English prompts.
— [AWS What's New: Natural Language Query Generation for OpenSearch PPL and SQL, August 2025](https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-cloudwatch-natural-language-query-generation-opensearch-ppl-sql/)

[STATISTIC] Logs Insights query pricing: **$0.005 per GB scanned**.
— [AWS CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)

### 1.4 Cross-Account Logging

[FACT] CloudWatch cross-account observability uses a **monitoring account / source account** model. A monitoring account can be linked to up to **100,000 source accounts**. Each source account can share data with up to **5 monitoring accounts**.
— [CloudWatch Cross-Account Observability Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)

[FACT] Cross-account observability enables searching log groups across multiple accounts, running cross-account Logs Insights queries, and viewing metrics, traces, Application Signals services, and SLOs from linked accounts without switching account contexts.
— [CloudWatch Cross-Account Observability Best Practices](https://aws-observability.github.io/observability-best-practices/guides/cloudwatch_cross_account_observability/)

[FACT] As of April 2025, cross-account observability was extended to **AWS GovCloud (US) Regions**.
— [AWS What's New: CloudWatch Cross-Account Observability in GovCloud, April 2025](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-cloudwatch-cross-account-observability-govcloud/)

[FACT] There is **no additional charge** for cross-account observability for logs, metrics, and the first trace copy. Standard per-service charges apply to the underlying data.
— [CloudWatch Cross-Account Observability Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)

---

## 2. Amazon CloudWatch Metrics

### 2.1 Custom Metrics

[FACT] Custom metrics can be published using the `PutMetricData` API at standard resolution (60-second granularity) or **high resolution down to 1-second granularity** per metric data point.
— [Publish Custom Metrics — Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)

[STATISTIC] Custom metrics pricing: **$0.30 per custom metric per month** for the first 10,000 metrics, with volume discounts at higher tiers.
— [AWS CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)

[FACT] CloudWatch also supports **Embedded Metric Format (EMF)** for extracting high-resolution custom metrics (up to 1-second granularity) from structured log events, enabling metric generation without additional `PutMetricData` API calls.
— [AWS What's New: High-Resolution Metric Extraction from Structured Logs](https://aws.amazon.com/about-aws/whats-new/2023/02/amazon-cloudwatch-high-resolution-metric-extraction-structured-logs/)

### 2.2 Anomaly Detection

[FACT] CloudWatch anomaly detection applies **machine learning algorithms** to a metric's historical data to model expected values, accounting for hourly, daily, and weekly patterns. The resulting band can be used to trigger alarms when actual values fall above, below, or outside the band.
— [Using CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

[FACT] A new anomaly detection model requires **up to 3 hours** for the initial band to appear in graphs and **up to 2 weeks** for the model to fully train on historical data.
— [Using CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

[FACT] Anomaly detection is also supported on **metric math expressions**, allowing alarms on derived composite metrics.
— [Using CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

[FACT] Anomaly detection alarms incur extra charges for the upper and lower band metrics generated by the detection model.
— [CloudWatch Pricing Explained Guide 2025](https://cloudchipr.com/blog/cloudwatch-pricing)

### 2.3 Dashboards

[FACT] CloudWatch dashboards support cross-Region metric visualization within a single dashboard, providing a global architecture view. Widgets include time-series graphs, single value, gauge, bar chart, pie chart, text, alarm status, and metric tables.
— [Amazon CloudWatch Metrics and Dashboards Guide](https://trailhead.salesforce.com/content/learn/modules/monitoring-on-aws/monitor-your-architecture-with-amazon-cloudwatch)

[FACT] **Metrics Insights** — a SQL-like query language for CloudWatch Metrics — is integrated with CloudWatch Dashboards to enable analysis of metrics at scale across namespaces and dimensions.
— [Advanced Features of Amazon CloudWatch](https://medium.com/cloud-native-daily/advanced-features-of-amazon-cloudwatch-d0cf9cc13bab)

### 2.4 Alarms

[FACT] CloudWatch alarms can evaluate metrics at **standard resolution (60 seconds)** or at **high resolution (10-second evaluation period)** for custom high-resolution metrics.
— [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)

[FACT] Alarms support multi-condition evaluation using composite alarms, which combine multiple CloudWatch alarms using Boolean logic (AND/OR/NOT) to reduce alarm noise.
— [AWS Observability Best Practices — Alarms](https://aws-observability.github.io/observability-best-practices/tools/alarms/)

---

## 3. AWS X-Ray

### 3.1 Distributed Tracing and Service Map

[FACT] AWS X-Ray collects request trace data across services and generates a **trace map** (service graph) showing client, front-end, and backend services. The trace map can display up to **10,000 nodes**; environments exceeding this may encounter display errors.
— [Using the X-Ray Trace Map](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-servicemap.html)

[FACT] X-Ray generates **segments** (one per service) and **subsegments** (for individual downstream calls, SQL queries, or annotated code blocks). These are assembled into a **trace** — a complete record of a request's path through the system.
— [AWS X-Ray Concepts](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)

### 3.2 Sampling Rules

[FACT] The X-Ray default sampling rule records **the first request each second plus 5% of any additional requests** per service.
— [Configuring Sampling Rules — AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html)

[FACT] Custom sampling rules are defined in the X-Ray console and evaluated by the service. AWS manages the **reservoir** (fixed request count per second) centrally and distributes quotas to each running service instance, preventing over-sampling when multiple instances of a service are running simultaneously.
— [Configuring Sampling Rules — AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html)

[FACT] Sampling rules can be updated **without redeploying application code**, applying changes dynamically across EC2, ECS, Lambda, and on-premises environments.
— [Dynamically Adjusting X-Ray Sampling Rules — AWS Blog](https://aws.amazon.com/blogs/mt/dynamically-adjusting-x-ray-sampling-rules/)

### 3.3 OpenTelemetry Transition (Critical Strategic Signal)

[FACT] AWS announced in October 2025 that **AWS X-Ray SDKs and X-Ray Daemon will enter maintenance mode on February 25, 2026 and reach end-of-support on February 25, 2027**. Between those dates, only critical bug fixes and security patches will be issued; no new features will be developed for the X-Ray SDKs or Daemon.
— [Announcing AWS X-Ray SDKs/Daemon End-of-Support and OpenTelemetry Migration — AWS Blog](https://aws.amazon.com/blogs/mt/announcing-aws-x-ray-sdks-daemon-end-of-support-and-opentelemetry-migration/)

[FACT] AWS recommends migrating to **OpenTelemetry-based instrumentation** (via ADOT or upstream OTel) as the path forward for sending traces to X-Ray. The X-Ray console, trace storage, and analysis experience remain fully supported indefinitely.
— [AWS X-Ray SDKs/Daemon Migration to OpenTelemetry — AWS Blog](https://aws.amazon.com/blogs/mt/aws-x-ray-sdks-daemon-migration-to-opentelemetry/)

[FACT] InfoQ reported in November 2025: "AWS Distributed Tracing Service X-Ray Transitions to OpenTelemetry."
— [InfoQ: AWS X-Ray Transitions to OpenTelemetry, November 2025](https://www.infoq.com/news/2025/11/aws-opentelemetry/)

---

## 4. Amazon CloudWatch Application Signals

### 4.1 APM Capabilities

[FACT] CloudWatch Application Signals provides **application performance monitoring (APM)** by automatically instrumenting applications using the AWS Distro for OpenTelemetry (ADOT). It collects standard application metrics — latency, error rate, throughput, availability, and fault — without requiring manual instrumentation code changes for supported runtimes.
— [Application Observability (APM) — CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/features/application-observability-apm/)

[FACT] Auto-instrumentation is supported with ADOT SDKs for **Java, Python, Node.js, and .NET**. **PHP and Ruby** are also supported using standard (non-ADOT) OpenTelemetry SDKs with zero-code instrumentation.
— [CloudWatch Application Signals Supported Systems](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-supportmatrix.html)

[FACT] Application Signals is tested and supported on **Amazon EKS, Amazon ECS, Amazon EC2, and AWS Lambda**.
— [Application Performance Monitoring (APM) — Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html)

### 4.2 SLO Management

[FACT] Application Signals supports creating and tracking **Service Level Objectives (SLOs)** based on either rolling-window intervals or calendar-month intervals, with a maximum interval of **12 months**.
— [Improve Application Reliability with Effective SLOs — AWS Blog](https://aws.amazon.com/blogs/mt/improve-application-reliability-with-effective-slos/)

[FACT] As of March 2025, Application Signals added **SLO exclusion time windows**, enabling teams to pause/resume SLO measurement during planned maintenance or deployments. Multiple SLOs can be configured with an exclusion window simultaneously. Start time, duration, and end time are all configurable.
— [AWS What's New: SLO Exclusion Time Windows, March 2025](https://aws.amazon.com/about-aws/whats-new/2025/03/slo-exclusion-time-windows-cloudwatch-application-signals/)

[FACT] Application Signals also enables **APM for Lambda functions**, allowing SLO tracking for serverless workloads.
— [Monitoring Lambda SLOs with CloudWatch Application Signals](https://developer.mamezou-tech.com/en/blogs/2024/12/15/aws-app-signals-lambda/)

---

## 5. Amazon Managed Grafana

### 5.1 Service Overview and AWS Data Source Integration

[FACT] Amazon Managed Grafana (AMG) is a fully managed Grafana workspace service. AWS manages Grafana software upgrades, patching, scaling, and high availability. The service integrates natively with **Amazon CloudWatch, Amazon OpenSearch Service, AWS X-Ray, AWS IoT SiteWise, Amazon Timestream, and Amazon Managed Service for Prometheus** as first-party data sources with permission provisioning.
— [What Is Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html)

[FACT] AWS IAM Identity Center (formerly AWS SSO) and **SAML 2.0** identity providers are supported for authentication, enabling integration with Azure Active Directory, Okta, OneLogin, Ping Identity, and CyberArk. Team Sync keeps user group membership synchronized with IdP directories.
— [Amazon Managed Grafana Features](https://aws.amazon.com/grafana/features/)

### 5.2 Enterprise Plugins

[FACT] Enterprise plugins (available as an upgrade add-on) enable connecting to third-party enterprise data sources including **AppDynamics, Atlassian Jira, Datadog, Dynatrace, GitLab, Honeycomb, MongoDB, New Relic, Oracle Database, Salesforce, SAP HANA, ServiceNow, Snowflake, and VMware Tanzu Observability**.
— [Centralize Observability with Amazon Managed Grafana Enterprise Plugins — AWS Blog](https://aws.amazon.com/blogs/mt/centralize-observability-with-amazon-managed-grafana-enterprise-plugins/)

### 5.3 Pricing

[FACT] Amazon Managed Grafana pricing (US East):
- **Editor/Administrator user license:** $9 per active user per workspace per month
- **Viewer user license:** $5 per active user per workspace per month
- **Enterprise Plugins add-on:** $45 per active user per workspace per month (additional)

There are no upfront fees, no minimum commitments, and no long-term contracts.
— [Amazon Managed Grafana Pricing](https://aws.amazon.com/grafana/pricing/)

[FACT] When querying AWS data sources such as CloudWatch from Grafana, the underlying CloudWatch API calls (e.g., `ListMetrics`, `GetMetricData`) incur standard CloudWatch API charges in addition to Grafana license fees.
— [Amazon Managed Grafana Pricing Documentation](https://docs.aws.amazon.com/grafana/latest/userguide/cloudwatch-pricing.html)

**What this abstracts away:** Grafana server provisioning, Grafana version upgrades, plugin management, high-availability configuration, database backend (Grafana config store), and SSO integration plumbing.

---

## 6. Amazon Managed Service for Prometheus (AMP)

### 6.1 Service Overview and PromQL Support

[FACT] Amazon Managed Service for Prometheus (AMP) is a **Prometheus-compatible** managed monitoring service. It uses the same open-source Prometheus data model and supports the full **PromQL** query language without modification.
— [What Is Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)

[FACT] AMP supports ingestion from **150+ Prometheus exporters** maintained by the open-source community, as well as from the AWS Distro for OpenTelemetry (ADOT) and the Prometheus remote-write protocol.
— [Amazon Managed Service for Prometheus Features](https://aws.amazon.com/prometheus/features/)

### 6.2 Scalability

[FACT] AMP automatically scales ingestion, storage, and query capacity as workloads scale up and down. The maximum active series per workspace is **1 billion** (requestable via quota increase). As of July 2025, the **default active series limit was increased to 50 million per workspace**, removing the need for quota increase requests at that threshold.
— [AWS What's New: AMP 50M Default Active Series Limit, July 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-managed-service-prometheus-50M-default-activeserieslimit/)

[FACT] As of April 2025, AMP added support for **label-based active series limits**, enabling fine-grained cardinality control per label set rather than only at the workspace level.
— [AWS What's New: AMP Label-Based Active Series Limits, April 2025](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-managed-service-prometheus-label-based-series-limits/)

### 6.3 Pricing

[FACT] AMP pricing has three components (US East):
- **Metric Ingestion:** tiered, starting at ~$0.90 per 10 million metric samples for the first 2 billion samples/month
- **Query Samples Processed (QSP):** $0.10 per billion samples processed via PromQL
- **Storage:** charged per GB (calculated from metric samples at typically 1–2 bytes each, plus metadata)

There are no upfront fees or minimum commitments.
— [Amazon Managed Service for Prometheus Pricing](https://aws.amazon.com/prometheus/pricing/)

**What this abstracts away:** Prometheus server provisioning, storage backend management (typically Cortex or Thanos in self-hosted deployments), compaction jobs, block storage management, high-availability ring configuration, and retention management.

---

## 7. AWS CloudTrail

### 7.1 API Audit Logging and Event History

[FACT] AWS CloudTrail records actions taken by users, roles, and AWS services as **events**, including API calls made via the AWS Management Console, AWS CLI, SDKs, and programmatic API calls. Events are recorded per AWS Region.
— [What Is AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

[FACT] **Event history** provides a viewable, searchable, downloadable, and immutable record of the past **90 days** of management events per AWS Region. Access to event history incurs **no CloudTrail charges**.
— [Working with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)

[FACT] CloudTrail captures three event types: **management events** (control-plane operations such as `CreateBucket`, `RunInstances`), **data events** (data-plane operations such as S3 `GetObject`, Lambda `Invoke` — opt-in), and **network activity events** (API calls through VPC Interface Endpoints — opt-in, introduced in 2025).
— [Understanding CloudTrail Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html)

### 7.2 Organization Trails

[FACT] An **organization trail** consolidates CloudTrail events from all AWS accounts within an AWS Organization into a single S3 bucket and optionally into CloudWatch Logs or Amazon EventBridge. It can be configured as single-Region or multi-Region.
— [What Is AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

### 7.3 CloudTrail Lake

[FACT] **AWS CloudTrail Lake** is an immutable managed event data store that converts JSON event records to **Apache ORC** columnar format, optimized for fast SQL query retrieval. It supports all valid **Trino SELECT** statements and functions, including cross-event-data-store SQL `JOIN` operations.
— [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)

[FACT] CloudTrail Lake event data stores retain events for up to **3,653 days (~10 years)** with the One-year extendable retention pricing option, or up to **2,557 days (~7 years)** with the Seven-year retention option.
— [CloudTrail Lake Event Data Stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html)

[FACT] CloudTrail Lake includes a **query generator** that produces ready-to-use Trino SQL queries from natural language (English) prompts using generative AI.
— [Create CloudTrail Lake Queries from Natural Language Prompts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html)

---

## 8. AWS Distro for OpenTelemetry (ADOT)

### 8.1 Service Overview

[FACT] The **AWS Distro for OpenTelemetry (ADOT)** is an AWS-supported, production-hardened distribution of the CNCF OpenTelemetry project. It provides open-source APIs, libraries, and agents for collecting **logs, metrics, and traces**, validated and distributed by Amazon.
— [AWS Distro for OpenTelemetry](https://aws-otel.github.io/)

[FACT] The **ADOT Collector** is an AWS-supported version of the upstream OpenTelemetry Collector. It can be deployed as a **managed EKS add-on**, on EC2, ECS (including Fargate), Lambda, AWS App Runner, and in on-premises data centers.
— [AWS Distro for OpenTelemetry — Introduction](https://aws-otel.github.io/docs/introduction/)

### 8.2 Backend Integration

[FACT] ADOT supports sending telemetry data to **Amazon Managed Service for Prometheus, Amazon CloudWatch, AWS X-Ray, Amazon OpenSearch Service**, any **OTLP-compliant** backend, and Amazon MSK — from a single instrumentation point.
— [AWS Distro for OpenTelemetry FAQs](https://aws.amazon.com/otel/faqs/)

[FACT] When used with Amazon Managed Service for Prometheus, ADOT serves as the **remote-write agent**, replacing the standard Prometheus server's scraping and remote-write configuration. The ADOT collector is configured to scrape Prometheus endpoints and forward metric samples to AMP via the Prometheus remote-write protocol with SigV4 authentication.
— [Using AWS Distro for OpenTelemetry as a Collector — AMP Documentation](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-with-adot.html)

### 8.3 Strategic Role

[FACT] ADOT is the **recommended instrumentation path for all new AWS observability instrumentation** following the deprecation of X-Ray SDKs/Daemon announced October 2025. ADOT enables a single instrumentation layer to send correlated signals to multiple backends simultaneously, supporting hybrid and multi-cloud observability architectures without re-instrumentation.
— [Build an Observability Solution Using Managed AWS Services and the OpenTelemetry Standard — AWS Blog](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/)

---

## 9. Comparative Operational Profile — AWS Managed Observability Stack

The table below rates the operational difficulty of running observability infrastructure for a mid-size ISV serving approximately 50 enterprise customers.

| Capability Domain | On-Premises | Managed K8s (Self-Hosted Stack) | Cloud-Native (AWS Managed) |
|---|---|---|---|
| **Log Ingestion & Storage** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | ELK or Loki cluster, disk provisioning, index management | Loki/ELK as in-cluster workload, PV management | CloudWatch Logs: zero provisioning, consumption billing |
| | Elasticsearch, Logstash, Filebeat | Promtail, Fluentd, or Fluent Bit to Loki | CloudWatch Agent or ADOT Collector |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **Metrics Collection & Storage** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-managed Prometheus + Thanos/Cortex, object storage backend | Prometheus Operator, Thanos sidecar, PVC management | Amazon Managed Service for Prometheus + ADOT |
| | Prometheus, Thanos, node exporters | kube-prometheus-stack Helm chart | AMP, ADOT EKS Add-on |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **Dashboards & Visualization** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-managed Grafana, PostgreSQL config DB, HA setup | Grafana as in-cluster deployment, ingress config | Amazon Managed Grafana: AWS handles HA, upgrades |
| | Grafana OSS, PostgreSQL | Grafana Helm chart, persistent storage | Amazon Managed Grafana |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |
| **Distributed Tracing** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-managed Jaeger or Zipkin, Cassandra/Elasticsearch backend | Jaeger or Tempo as in-cluster workload | AWS X-Ray via ADOT: zero backend provisioning |
| | Jaeger, Cassandra/Elasticsearch | Jaeger Operator, Tempo Helm chart | ADOT Collector, AWS X-Ray |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **APM and SLO Tracking** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Commercial APM (Dynatrace/Datadog self-hosted), custom SLO tooling | Self-managed Sloth or Pyrra for SLOs, custom dashboards | CloudWatch Application Signals: auto-instrumentation + SLO UI |
| | Dynatrace Managed, custom tooling | Sloth, Pyrra, custom Prometheus rules | CloudWatch Application Signals |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 |
| **API Audit Logging** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Custom audit log pipeline, SIEM integration | Kubernetes audit log collection, custom routing | AWS CloudTrail: automatic, immutable, zero provisioning |
| | Falco, custom log shippers, SIEM | Falco, Fluent Bit to SIEM | AWS CloudTrail, CloudTrail Lake |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.05 |

**FTE Assumption:** Mid-size deployment, ~50 enterprise customers, typical multi-service SaaS application with 10–20 microservices. On-call burden (estimated 0.25 FTE equivalent for cloud-native; 0.5–1.0 FTE for self-managed stacks) is included in the estimates above.

---

## 10. Cost Governance Considerations for ISVs

[FACT] At scale, CloudWatch custom metrics pricing can become significant. AWS charges **$0.30 per custom metric per month** with a free tier of only 10 metrics. An ISV publishing 1,000 custom metrics incurs approximately **$300/month** in metric fees alone, before alarms or dashboards.
— [AWS CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)

[FACT] Amazon Managed Service for Prometheus uses a tiered ingestion pricing model where initial usage incurs higher per-sample costs. The cost structure rewards scale — high-volume customers benefit from decreasing per-sample rates.
— [Understand and Optimize Costs in Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-costs.html), [How Much Does Your Managed Service for Prometheus Cost? — Sysdig](https://www.sysdig.com/blog/managed-service-prometheus)

[FACT] AWS published prescriptive guidance in 2025 recommending that ISVs "redirect engineering effort from infrastructure maintenance to customer-centric innovation" when adopting managed services, citing operational overhead reduction as a primary benefit.
— [Stage 2: Implement Observability — AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/implement-observability.html)

---

## Key Takeaways

- **AWS managed observability eliminates all infrastructure operations** for logging, metrics, tracing, and dashboarding. CloudWatch Logs, AMP, AMG, and X-Ray abstract away storage backends, ingestion pipelines, retention management, and capacity planning — reducing observability operational FTE from 2–5 FTE (self-hosted) to 0.25–0.5 FTE (cloud-native) for a typical mid-size ISV deployment.

- **The X-Ray SDK/Daemon deprecation (end-of-support: February 25, 2027) is a mandatory migration.** ISVs should adopt ADOT-based instrumentation for all new services immediately, and plan migration of existing X-Ray SDK-instrumented services before the end-of-support date. ADOT's vendor-neutral OTel foundation also reduces future lock-in risk.

- **Cross-account observability at no additional charge** enables ISVs running multi-account SaaS architectures (a common per-tenant isolation pattern) to aggregate logs, metrics, traces, and SLOs into a central monitoring account without additional tooling or data movement costs.

- **CloudWatch Logs Insights now supports three query languages** (native Logs Insights QL, OpenSearch PPL, OpenSearch SQL) with AI-assisted query generation (August 2025), materially lowering the query skill barrier for operations teams and accelerating time-to-insight during incidents.

- **Cost governance is required at scale.** CloudWatch custom metrics ($0.30/metric/month), Logs Insights scan charges ($0.005/GB), and AMP ingestion tiering can accumulate substantially in high-cardinality SaaS deployments. ISVs should adopt EMF for metric extraction from logs, use the Infrequent Access log class for non-critical logs (50% ingestion discount), and instrument AMP label-based series limits (April 2025) to control cardinality costs proactively.

---

## Related — Out of Scope

- **Security logging with CloudWatch and CloudTrail** (including GuardDuty, Security Hub, and detective controls): covered in F11.
- **Observability services from Azure (Azure Monitor, Log Analytics) and GCP (Cloud Monitoring, Cloud Logging)**: covered in parallel provider research files.
- **Self-hosted observability stacks** (ELK, Prometheus/Thanos, Jaeger): referenced in comparison table above for difficulty baseline; not investigated further per scope boundary.
- **Cost optimization tooling** (AWS Cost Explorer, CloudWatch cost dashboards): out of scope for observability research; relevant to the ISV financial modeling workstream.

---

## Sources

1. [Amazon CloudWatch Logs — What Is CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
2. [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)
3. [Analyzing Log Data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
4. [CloudWatch Logs Insights QL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_LogsInsights.html)
5. [Use Natural Language to Generate CloudWatch Logs Insights Queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Assist.html)
6. [AWS What's New: CloudWatch Logs Insights Query Results Summarization and PPL Enhancements, June 2025](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-cloudwatch-logs-insights-query-results-summarization-opensearch-ppl-enhancements/)
7. [AWS What's New: CloudWatch Natural Language Query Generation for OpenSearch PPL and SQL, August 2025](https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-cloudwatch-natural-language-query-generation-opensearch-ppl-sql/)
8. [Log Classes — Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)
9. [New Amazon CloudWatch Log Class for Infrequent Access Logs — AWS Blog](https://aws.amazon.com/blogs/aws/new-amazon-cloudwatch-log-class-for-infrequent-access-logs-at-a-reduced-price/)
10. [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)
11. [CloudWatch Pricing Explained: Ultimate Guide 2025](https://cloudchipr.com/blog/cloudwatch-pricing)
12. [CloudWatch Cross-Account Observability Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)
13. [CloudWatch Cross-Account Observability Best Practices](https://aws-observability.github.io/observability-best-practices/guides/cloudwatch_cross_account_observability/)
14. [AWS What's New: CloudWatch Cross-Account Observability in GovCloud, April 2025](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-cloudwatch-cross-account-observability-govcloud/)
15. [Publish Custom Metrics — Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
16. [Using CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
17. [Create Alarms for Custom Metrics Using CloudWatch Anomaly Detection — AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection.html)
18. [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)
19. [AWS Observability Best Practices — Alarms](https://aws-observability.github.io/observability-best-practices/tools/alarms/)
20. [Amazon CloudWatch Metrics and Dashboards Guide](https://trailhead.salesforce.com/content/learn/modules/monitoring-on-aws/monitor-your-architecture-with-amazon-cloudwatch)
21. [AWS What's New: High-Resolution Metric Extraction from Structured Logs, 2023](https://aws.amazon.com/about-aws/whats-new/2023/02/amazon-cloudwatch-high-resolution-metric-extraction-structured-logs/)
22. [Advanced Features of Amazon CloudWatch](https://medium.com/cloud-native-daily/advanced-features-of-amazon-cloudwatch-d0cf9cc13bab)
23. [AWS X-Ray Concepts](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)
24. [What Is AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
25. [Configuring Sampling Rules — AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html)
26. [Using the X-Ray Trace Map](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-servicemap.html)
27. [Dynamically Adjusting X-Ray Sampling Rules — AWS Blog](https://aws.amazon.com/blogs/mt/dynamically-adjusting-x-ray-sampling-rules/)
28. [Announcing AWS X-Ray SDKs/Daemon End-of-Support and OpenTelemetry Migration — AWS Blog](https://aws.amazon.com/blogs/mt/announcing-aws-x-ray-sdks-daemon-end-of-support-and-opentelemetry-migration/)
29. [AWS X-Ray SDKs/Daemon Migration to OpenTelemetry — AWS Blog](https://aws.amazon.com/blogs/mt/aws-x-ray-sdks-daemon-migration-to-opentelemetry/)
30. [InfoQ: AWS X-Ray Transitions to OpenTelemetry, November 2025](https://www.infoq.com/news/2025/11/aws-opentelemetry/)
31. [Application Observability (APM) — CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/features/application-observability-apm/)
32. [Application Performance Monitoring (APM) — Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html)
33. [CloudWatch Application Signals Supported Systems](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-supportmatrix.html)
34. [AWS What's New: SLO Exclusion Time Windows, March 2025](https://aws.amazon.com/about-aws/whats-new/2025/03/slo-exclusion-time-windows-cloudwatch-application-signals/)
35. [Improve Application Reliability with Effective SLOs — AWS Blog](https://aws.amazon.com/blogs/mt/improve-application-reliability-with-effective-slos/)
36. [Four APM Features to Elevate Your Observability Experience — AWS Blog](https://aws.amazon.com/blogs/mt/four-apm-features-to-elevate-your-observability-experience/)
37. [Application Monitoring with Amazon CloudWatch Application Signals, April 2025](https://www.terminalworks.com/blog/post/2025/04/28/application-monitoring-with-amazon-cloudwatch-application-signals)
38. [What Is Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html)
39. [Amazon Managed Grafana Pricing](https://aws.amazon.com/grafana/pricing/)
40. [Amazon Managed Grafana FAQs](https://aws.amazon.com/grafana/faqs/)
41. [Amazon Managed Grafana Features](https://aws.amazon.com/grafana/features/)
42. [Centralize Observability with Amazon Managed Grafana Enterprise Plugins — AWS Blog](https://aws.amazon.com/blogs/mt/centralize-observability-with-amazon-managed-grafana-enterprise-plugins/)
43. [What Is Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html)
44. [Amazon Managed Service for Prometheus Pricing](https://aws.amazon.com/prometheus/pricing/)
45. [Amazon Managed Service for Prometheus Features](https://aws.amazon.com/prometheus/features/)
46. [Amazon Managed Service for Prometheus FAQs](https://aws.amazon.com/prometheus/faqs/)
47. [AWS What's New: AMP 50M Default Active Series Limit, July 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-managed-service-prometheus-50M-default-activeserieslimit/)
48. [AWS What's New: AMP Label-Based Active Series Limits, April 2025](https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-managed-service-prometheus-label-based-series-limits/)
49. [Understand and Optimize Costs in Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-costs.html)
50. [How Much Does Your Managed Service for Prometheus Cost? — Sysdig](https://www.sysdig.com/blog/managed-service-prometheus)
51. [What Is AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
52. [Working with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
53. [Understanding CloudTrail Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-events.html)
54. [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)
55. [CloudTrail Lake Event Data Stores](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html)
56. [Create CloudTrail Lake Queries from Natural Language Prompts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html)
57. [AWS Distro for OpenTelemetry](https://aws-otel.github.io/)
58. [AWS Distro for OpenTelemetry — Introduction](https://aws-otel.github.io/docs/introduction/)
59. [AWS Distro for OpenTelemetry FAQs](https://aws.amazon.com/otel/faqs/)
60. [Using AWS Distro for OpenTelemetry as a Collector — AMP Documentation](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ingest-with-adot.html)
61. [AWS Distro for OpenTelemetry and AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html)
62. [Build an Observability Solution Using Managed AWS Services and the OpenTelemetry Standard — AWS Blog](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/)
63. [Stage 2: Implement Observability — AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/implement-observability.html)
64. [Choosing an AWS Monitoring and Observability Service](https://docs.aws.amazon.com/decision-guides/latest/monitoring-on-aws-how-to-choose/monitoring-on-aws-how-to-choose.html)
65. [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/guides/)
66. [Comprehensive Guide to Amazon Managed Service for Prometheus — StackPioneers, June 2025](https://stackpioneers.com/2025/06/05/comprehensive-guide-to-amazon-managed-service-for-prometheus/)
67. [How to Use AWS CloudWatch Application Signals with OpenTelemetry on ECS Fargate and Lambda](https://awsfundamentals.com/blog/cloudwatch-application-signals-otel)
68. [AWS What's New: AMP Default Active Series Limit Increase, July 2025](https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-managed-service-prometheus-50M-default-activeserieslimit/)
