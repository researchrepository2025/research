# F20: Azure Observability Services

**Research Question:** What managed observability services does Azure provide for logging, monitoring, tracing, and alerting, and what do they abstract away?

**Scope:** Azure observability services only. Security monitoring is covered in F19. No other cloud providers are compared here.

---

## Executive Summary

Azure Monitor is a unified, fully managed observability platform that consolidates metrics, logs, distributed traces, and change events into a single data plane — eliminating the need for ISVs to provision, scale, or patch any monitoring backend. For ISVs building AI-driven SaaS on Azure, the managed observability stack (Azure Monitor + Application Insights + Log Analytics + Managed Prometheus + Managed Grafana) provides a complete signals-to-alerts pipeline that would otherwise require 2–4 FTEs to self-host at equivalent scale. Application Insights transitioned to an OpenTelemetry-native model in 2025, standardizing instrumentation across .NET, Java, Node.js, and Python without vendor lock-in. Microsoft announced general availability (GA) of Azure Monitor Dashboards with Grafana at Ignite 2025, delivering native Grafana visualizations inside the Azure portal at no additional cost. The Azure managed observability suite abstracts away server provisioning, storage scaling, high-availability configuration, software upgrades, and retention management — reducing the observability operational burden in Managed Kubernetes deployments to a Difficulty of 2/5 compared to 4–5/5 for equivalent self-hosted stacks.

---

## 1. Azure Monitor: The Unified Observability Platform

### 1.1 What Azure Monitor Is

[FACT]
"Azure Monitor is a comprehensive monitoring solution for collecting, analyzing, and responding to monitoring data from your cloud and on-premises environments."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

[FACT]
"Azure Monitor collects and aggregates the data from every layer and component of your system across multiple Azure and non-Azure subscriptions and tenants. It stores it in a common data platform for consumption by a common set of tools that can correlate, analyze, visualize, and/or respond to the data."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

[FACT]
"There is no on-premises version of Azure Monitor. Azure Monitor is a scalable cloud service that processes and stores large amounts of data, although Azure Monitor can monitor resources that are on-premises and in other clouds."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

### 1.2 Data Platform: Four Pillars

Azure Monitor stores data across four distinct, purpose-optimized stores:

| Data Store | Description |
|------------|-------------|
| Metrics | Time-series database for numerical values at regular intervals; supports native Azure metrics and Prometheus metrics |
| Logs | Structured and unstructured log data of all types, stored in Log Analytics workspaces; queried via KQL |
| Distributed Traces | Trace data from instrumented applications, stored in a separate workspace in Azure Monitor Logs |
| Changes | Change event series tracked via Change Analysis (classic), backed by Azure Resource Graph |

[FACT]
"Azure Monitor's core data platform has stores for metrics, logs, traces, and changes."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

### 1.3 Monitored Resource Types

[FACT]
Azure Monitor can monitor: Applications, Virtual machines, Guest operating systems, Containers including Prometheus metrics, Databases, Security events (with Azure Sentinel), Networking events and health (with Network Watcher), and Custom sources via API.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

### 1.4 Metrics and Alerts

[FACT]
"Metric alert rules provide near-real-time alerts based on collected metrics. Log search alert rules based on logs allow for complex logic across data from multiple sources."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

[FACT]
"Alert rules use action groups, which can perform actions such as sending email or SMS notifications. Action groups can send notifications using webhooks to trigger external processes or to integrate with your IT service management tools."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

[FACT]
Action groups support: voice call, SMS, push notifications, email, webhook, Azure Function triggers.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups
Date: 2025

[FACT]
"Metric alerts in Azure Monitor work on a host of multi-dimensional platform and custom metrics, and notify you when the metric breaches a threshold that was either defined by you or detected automatically."
URL: https://azure.microsoft.com/en-us/blog/monitor-at-scale-in-azure-monitor-with-multi-resource-metric-alerts/
Date: 2025

### 1.5 Autoscale

[FACT]
"Autoscale allows you to dynamically control the number of resources running to handle the load on your application. You can create rules that use Azure Monitor metrics to determine when to automatically add resources when the load increases or remove resources that are sitting idle."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

[FACT]
"Scaling can be based on any metric, even metrics from a different resource."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-common-metrics
Date: 2025

### 1.6 AIOps and Intelligent Features

[FACT]
"Artificial Intelligence for IT Operations (AIOps) can improve service quality and reliability by using machine learning to process and automatically act on data you collect from applications, services, and IT resources into Azure Monitor. It automates data-driven tasks, predicts capacity usage, identifies performance issues, and detects anomalies across applications, services, and IT resources."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

### 1.7 Ignite 2025 New Capabilities

[FACT]
At Microsoft Ignite 2025, Azure Monitor announced: Azure Copilot Observability Agent (preview) for full-stack root cause analysis; Agent Details View (public preview) for GenAI application observability; Dynamic Thresholds for Log Search Alerts (public preview) using machine learning; Query-Based Metric Alerts (public preview) for Prometheus, VM Guest OS, and custom OTel metrics; Log Filtering and Transformation (GA); Granular RBAC for Log Analytics workspaces (GA); Azure Monitor Dashboards with Grafana (GA).
URL: https://techcommunity.microsoft.com/blog/azureobservabilityblog/advancing-full-stack-observability-with-azure-monitor-at-ignite-2025/4469041
Date: November 2025

### 1.8 What Azure Monitor Abstracts Away

For ISVs, Azure Monitor eliminates the need to:
- Provision and scale a metrics storage backend (e.g., self-managed InfluxDB or Thanos)
- Build alerting pipelines and notification routing
- Maintain agent software versions across fleets
- Manage time-series data compaction and retention lifecycles
- Build cross-subscription data aggregation

---

## 2. Azure Application Insights: APM and Distributed Tracing

### 2.1 Overview and OpenTelemetry Transition

[FACT]
"Azure Monitor Application Insights is an OpenTelemetry feature of Azure Monitor that offers application performance monitoring (APM) for live web applications. Integrating with OpenTelemetry (OTel) provides a vendor-neutral approach to collecting and analyzing telemetry data, enabling comprehensive observability of your applications."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
Date: Updated 2026-02-11

[FACT]
"Application Insights transformed into an OpenTelemetry feature of Azure Monitor in 2025, offering APM for live web applications."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview
Date: 2025

[FACT]
Microsoft launched Code Optimizations in September 2025, using AI to analyze .NET profiler traces for performance bottlenecks.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
Date: Updated 2026-02-11

### 2.2 Supported Languages (OpenTelemetry Distro)

[FACT]
Application Insights OpenTelemetry Distro supports: ASP.NET Core, .NET, Java, Node.js, Python (server-side); JavaScript with React, React Native, and Angular (client-side).
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
Date: Updated 2026-02-11

### 2.3 Application Insights Experiences

[FACT]
Application Insights provides the following investigation experiences: Application dashboard (at-a-glance health and performance), Application map (visual architecture and component interaction view), Live metrics (real-time analytics dashboard), Search view (transaction diagnosis), Availability view (endpoint availability monitoring), Failures view (failure identification and analysis), Performance view (bottleneck identification), Agents details (unified view for AI agents across Azure AI Foundry, Copilot Studio, and third-party agents).
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
Date: Updated 2026-02-11

### 2.4 Distributed Tracing

[FACT]
"Azure Monitor provides two experiences for consuming distributed trace data: the transaction diagnostics view for a single transaction/request and the application map view to show how systems interact."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
Date: Updated 2026-02-11

[FACT]
"Application Insights is transitioning to W3C Trace-Context, and the latest version of the Application Insights SDK supports the Trace-Context protocol."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/distributed-trace-data
Date: 2025

### 2.5 Smart Detection (Automated Anomaly Detection)

[FACT]
"Smart detection automatically warns you of potential performance problems and failure anomalies in your web application. It performs proactive analysis of the telemetry that your app sends to Application Insights. If there's a sudden rise in failure rates or abnormal patterns in client or server performance, you get an alert. This feature needs no configuration. It operates if your application sends enough telemetry."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/proactive-diagnostics
Date: Updated 2026-01-16

[FACT]
Smart detection detects: Failure Anomalies (using ML to set expected failure rate correlated with load), Performance Anomalies (response time or dependency duration compared to historical baseline), Trace degradation, Memory leak, Abnormal rise in Exception volume, and Security anti-patterns.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/proactive-diagnostics
Date: Updated 2026-01-16

[FACT]
"All smart detection rules, except for rules marked as preview, are configured by default to send email notifications when detections are found."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/proactive-diagnostics
Date: Updated 2026-01-16

### 2.6 Supported Azure Service Integrations

[FACT]
Application Insights natively integrates with: Azure Virtual Machines and Virtual Machine Scale Sets, Azure App Service, Azure Functions, Azure Spring Apps, Azure Cloud Services (web and worker roles).
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
Date: Updated 2026-02-11

### 2.7 What Application Insights Abstracts Away

For ISVs, Application Insights eliminates the need to:
- Build or maintain a custom APM data ingestion pipeline
- Write anomaly detection models for failure rates and latency
- Instrument applications for distributed tracing from scratch (auto-instrumentation available)
- Build a transaction search index
- Manage availability test infrastructure

---

## 3. Azure Log Analytics: Log Ingestion, KQL, and Retention

### 3.1 Workspace Overview

[FACT]
"A Log Analytics workspace is a data store into which you can collect any type of log data from all of your Azure and non-Azure resources and applications. Workspace configuration options let you manage all of your log data in one workspace to meet the operations, analysis, and auditing needs of different personas in your organization."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview
Date: Updated 2025-08-29

[FACT]
"Log Analytics workspaces are based on Azure Data Explorer, using a powerful analysis engine and the rich Kusto query language (KQL). Azure Monitor Logs uses a version of the Kusto Query Language suitable for simple log queries, and advanced functionality such as aggregations, joins, and smart analytics."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
Date: Updated 2025-09-16

### 3.2 Data Retention

[FACT]
"A Log Analytics workspace retains data in two states — interactive retention and long-term retention."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview
Date: Updated 2025-08-29

[FACT]
"Each table in your Log Analytics workspace lets you retain data up to 12 years in low-cost, long-term retention."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview
Date: Updated 2025-08-29

[FACT]
"31 days of analytics retention are included in the ingestion price, lowering the retention period below 31 days doesn't reduce costs."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs
Date: 2025

[FACT]
"Analytics plan tables can retain data for up to 12 years, whilst Basic plan tables max out at 90 days."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs
Date: 2025

### 3.3 Pricing Model

[FACT]
"The default pricing for Log Analytics is a pay-as-you-go model that's based on ingested data volume and data retention."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs
Date: 2025

[FACT]
"Log Analytics has commitment tiers, which can save you as much as 30 percent compared to the pay-as-you-go price for Analytics Logs. With commitment tier pricing, you can commit to buy data ingestion for a workspace, starting at 100 GB per day."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs
Date: 2025

[FACT]
Azure Monitor Logs bills for data ingested in GB (10^9 bytes). Pay-as-you-go pricing is approximately $2.30–$2.76 per GB ingested; includes 5 GB free per billing account per month.
URL: https://azure.microsoft.com/en-us/pricing/details/monitor/
Date: 2025

### 3.4 Ingestion Transformation

[FACT]
"Data collection rules (DCRs) that define data coming into Azure Monitor can include transformations that allow you to filter and transform data before it's ingested into the workspace."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview
Date: Updated 2025-08-29

### 3.5 Activity Log Storage

[FACT]
"There is no data ingestion charges for activity logs. Retention charges for activity logs are only applied to the period extended past the default retention period of 90 days. You can increase the retention period to up to 12 years."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

[FACT]
Activity log data in a Log Analytics workspace is stored in a table called `AzureActivity`.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

### 3.6 What Log Analytics Abstracts Away

For ISVs, Log Analytics eliminates the need to:
- Deploy and scale an Elasticsearch or OpenSearch cluster
- Write index management and shard rotation policies
- Maintain a KQL or Lucene query engine
- Build cross-source log correlation infrastructure
- Manage log compression, tiering, and archival

---

## 4. Azure Managed Grafana

### 4.1 Overview

[FACT]
"Azure Managed Grafana is a data visualization platform built on top of the Grafana software by Grafana Labs. It's built as a fully managed Azure service operated and supported by Microsoft."
URL: https://learn.microsoft.com/en-us/azure/managed-grafana/overview
Date: Updated 2025-09-30

[FACT]
"As a fully managed service, Azure Managed Grafana lets you deploy Grafana without having to deal with setup. The service provides high availability, SLA guarantees and automatic software updates."
URL: https://learn.microsoft.com/en-us/azure/managed-grafana/overview
Date: Updated 2025-09-30

### 4.2 Service Tiers

[FACT]
Azure Managed Grafana service tiers:

| Tier | Key Features | SLA |
|------|-------------|-----|
| Essential (preview) — being retired | Core Grafana with Azure data sources only; for evaluation/testing only | None |
| Standard (recommended) | All core plugins, Azure Monitor, Prometheus, Azure Data Explorer, GitHub, JSON API; zone redundancy; private endpoints; alerting; email (SMTP); reporting/image rendering | Yes |
| Standard X2 | All Standard features; 1,000 alert rules (vs. 500 for X1); more memory | Yes |

URL: https://learn.microsoft.com/en-us/azure/managed-grafana/overview
Date: Updated 2025-09-30

[FACT]
"The Essential (preview) service tier for Azure Managed Grafana is being replaced with the Standard service tier and Azure Monitor dashboards with Grafana."
URL: https://learn.microsoft.com/en-us/azure/managed-grafana/overview
Date: Updated 2025-09-30

### 4.3 Azure Monitor Integration

[FACT]
"Azure Managed Grafana is optimized for the Azure environment. It works seamlessly with many Azure services and provides: built-in support for Azure Monitor and Azure Data Explorer; user authentication and access control using Microsoft Entra identities; direct import of existing charts from the Azure portal."
URL: https://learn.microsoft.com/en-us/azure/managed-grafana/overview
Date: Updated 2025-09-30

[FACT]
At Microsoft Ignite 2025, Azure Monitor Dashboards with Grafana reached GA: "delivering rich visualizations and data transformation capabilities on Prometheus metrics, Azure resource metrics, and more" — available in the Azure portal at no additional cost.
URL: https://techcommunity.microsoft.com/blog/azureobservabilityblog/advancing-full-stack-observability-with-azure-monitor-at-ignite-2025/4469041
Date: November 2025

[FACT]
"Azure Monitor dashboards with Grafana will allow customers to create and edit Grafana dashboards directly in the Azure portal without any additional cost and little administrative overhead, with immediate access to preconfigured dashboards for Azure Kubernetes Services, Application Insights, and dozens of other Azure resources, along with the ability to import thousands of dashboards from the Grafana community."
URL: https://grafana.com/blog/2025/05/19/azure-monitor-offers-grafana-dashboards-natively-for-immediate-real-time-operational-monitoring/
Date: May 2025

[FACT]
Azure Monitor Dashboards with Grafana support data sources: Azure Monitor Metrics, Azure Monitor Managed Service for Prometheus, Azure Monitor Logs (queried via KQL), and Azure Monitor Traces.
URL: https://blog.aks.azure.com/2025/09/18/azure-monitor-grafana-dashboards-portal
Date: September 2025

[FACT]
"Grafana dashboards can be managed as native Azure resources, including using Azure RBAC and automation via ARM template and Bicep templates."
URL: https://blog.aks.azure.com/2025/09/18/azure-monitor-grafana-dashboards-portal
Date: September 2025

### 4.4 What Azure Managed Grafana Abstracts Away

For ISVs, Azure Managed Grafana eliminates the need to:
- Deploy and manage Grafana server infrastructure (VMs, containers, load balancers)
- Handle Grafana version upgrades and plugin compatibility
- Configure LDAP/SSO authentication (replaced by Microsoft Entra)
- Manage high availability and failover for the Grafana backend
- Handle dashboard backup and disaster recovery

---

## 5. Azure Monitor Managed Service for Prometheus

### 5.1 Overview

[FACT]
"Azure Monitor provides a fully managed service for Prometheus that enables you to collect, store, and analyze Prometheus metrics without maintaining your own Prometheus server."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

[FACT]
"Azure Monitor managed service for Prometheus provides a fully managed and scalable environment for running Prometheus. It simplifies the deployment, management, and scaling of Prometheus in AKS and Azure Arc-enabled Kubernetes so you can focus on monitoring your applications and infrastructure."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

### 5.2 Core Capabilities

[FACT]
"As a fully managed service, it provides high availability, service-level agreement (SLA) guarantees, automatic software updates, and a highly scalable metrics store that retains data for up to 18 months."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

[FACT]
"Azure Monitor managed service for Prometheus provides preconfigured alerts, rules, and dashboards. It fully supports Prometheus Query Language (PromQL) and provides tools in the Azure portal for interactively querying and visualizing Prometheus metrics."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

### 5.3 PromQL Querying Tools

[FACT]
Available tools for querying Managed Prometheus: Container insights (Kubernetes cluster drill-down), Azure Monitor metrics explorer with PromQL (preview), Azure Monitor workbooks with PromQL queries, Grafana dashboards (native in Azure portal at no cost, or Azure Managed Grafana), Prometheus query API (REST-based PromQL).
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

### 5.4 Data Collection Mechanism

[FACT]
"Azure Monitor managed service for Prometheus currently collects data directly from AKS and Azure Arc-enabled Kubernetes. Azure Monitor provides an onboarding process that installs the Azure Monitor agent in your cluster and creates a data collection rule (DCR) that defines the data collection process and directs the data to the appropriate workspace."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

[FACT]
"Azure Monitor managed service for Prometheus supports recording rules and alert rules using PromQL queries."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

### 5.5 Self-Managed Prometheus Integration

[FACT]
"Remote_write is a feature in Prometheus that allows you to send metrics from a local Prometheus instance to remote storage or to another Prometheus instance. Use this feature to send metrics from self-managed Prometheus running in your Kubernetes cluster or virtual machines to an Azure Monitor workspace used by Managed Prometheus."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

### 5.6 Pricing

[FACT]
"There's no direct cost to Azure Monitor managed service for Prometheus or creating an Azure Monitor workspace. Pricing is based on ingestion and query of collected data. Data is stored for 18 months at no additional cost."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview
Date: Updated 2026-02-03

### 5.7 What Managed Prometheus Abstracts Away

For ISVs, Azure Managed Prometheus eliminates the need to:
- Deploy and maintain Prometheus server pods in AKS
- Configure and tune Prometheus storage (TSDB compaction, WAL settings)
- Implement Prometheus HA using Thanos or Cortex
- Handle scrape configuration at scale across multiple clusters
- Manage 18-month metric retention (included free)

---

## 6. Azure Monitor Network Insights

### 6.1 Overview

[FACT]
"Azure Monitor Network Insights provides a comprehensive and visual representation through topology, health and metrics for all deployed network resources, without requiring any configuration."
URL: https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview
Date: Updated 2025-09-10

### 6.2 Core Components

[FACT]
Azure Monitor Network Insights is structured around five key monitoring areas: Topology, Network health and metrics, Connectivity, Traffic, and Diagnostic Toolkit.
URL: https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview
Date: Updated 2025-09-10

[FACT]
"Topology provides a visualization of Azure virtual networks and connected resources for understanding network topology. Topology provides an interactive interface to view resources and their relationships in Azure across multiple subscriptions, regions, and resource groups."
URL: https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview
Date: Updated 2025-09-10

### 6.3 Connection Monitor

[FACT]
"Connection monitor provides unified and continuous network connectivity monitoring, enabling users to detect anomalies, identify the specific network component responsible for issues, and troubleshoot with actionable insights in Azure and hybrid cloud environments."
URL: https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview
Date: 2025

[FACT]
"Connection monitor tests measure aggregated packet loss and network latency metrics across TCP, ICMP, and HTTP pings."
URL: https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview
Date: 2025

[FACT]
"Connection monitor supports the Azure Monitor agent extension, which eliminates any dependency on the legacy Log Analytics agent."
URL: https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview
Date: 2025

### 6.4 Onboarded Network Resource Types

[FACT]
Resources with full Network Insights topology and built-in metrics workbooks: Application Gateway, Azure Bastion, Azure Firewall, Azure Front Door, Azure NAT Gateway, ExpressRoute, Load Balancer, Local Network Gateway, Network Interface, Network Security Group, Private Link, Public IP address, Route table / UDR, Traffic Manager, Virtual Hub, Virtual Network, Virtual Network Gateway (ExpressRoute and VPN), Virtual WAN.
URL: https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview
Date: Updated 2025-09-10

### 6.5 Diagnostic Toolkit

[FACT]
Diagnostic Toolkit within Network Insights provides: packet capture, VPN troubleshoot, connection troubleshoot, next hop, and IP flow verify.
URL: https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview
Date: Updated 2025-09-10

---

## 7. Azure Activity Log: Control Plane Audit Logging

### 7.1 Overview

[FACT]
"The Azure Monitor activity log is a platform log for control plane events from Azure resources. It includes information like when a resource is modified or when a deployment error occurs."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

[FACT]
"Entries in the activity log are collected by default with no required configuration. They're system generated and can't be changed or deleted."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

### 7.2 Retention

[FACT]
"Activity log events are retained in Azure for 90 days and then deleted. There's no charge for entries during this time regardless of volume."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

### 7.3 Export Destinations

[FACT]
Activity log entries can be exported to: Log Analytics workspace (stored in `AzureActivity` table; retention extensible to 12 years), Azure Event Hubs (JSON format; for SIEM integration), Azure Storage account (for long-term archival; blob naming by date/hour).
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

### 7.4 Change History

[FACT]
"For some events, you can view the change history, which shows what changes happened during that event time. Select an event from the activity log you want to look at more deeply. Select the Change history tab to view any changes on the resource up to 30 minutes before and after the time of the operation."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

### 7.5 Activity Log Insights Workbook

[FACT]
"Activity log insights is a workbook that provides a set of dashboards that monitor the changes to resources and resource groups in a subscription. The dashboards also present data about which users or services performed activities in the subscription and the activities' status."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log
Date: Updated 2025-12-19

---

## 8. Azure Workbooks: Interactive Reporting and Visualization

### 8.1 Overview

[FACT]
"Workbooks provide a flexible canvas for data analysis and the creation of rich visual reports within the Azure portal. They allow you to tap into multiple data sources from across Azure and combine them into unified interactive experiences."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview
Date: Updated 2025-06-19

[FACT]
"Workbooks combine text, log queries, metrics, and parameters into rich interactive reports."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview
Date: Updated 2025-06-19

### 8.2 Data Sources

[FACT]
Workbooks can query data from multiple Azure sources including: Log Analytics workspaces (KQL), Azure Monitor Metrics, Azure Resource Graph, Azure Data Explorer, Azure Resource Manager, and other sources. Data from different sources can be combined in a single report.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview
Date: Updated 2025-06-19

### 8.3 Visualization Types

[FACT]
Azure Workbooks visualization gallery includes: time series charts, grids, pie charts, gauges, maps, and logs views. Interactive visualizations support parameter-driven dropdowns, date pickers, and row-click parameter export to downstream charts.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-visualizations
Date: 2025

### 8.4 Template Gallery

[FACT]
The Workbooks gallery has four tabs: All (top items), Workbooks (saved workbooks shared with the user), Public Templates (Microsoft-published, ready-to-use templates grouped by category), and My Templates (user-created templates).
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview
Date: Updated 2025-06-19

### 8.5 Access Control

[FACT]
Standard Azure RBAC roles for workbooks: Monitoring Reader (read/view access), Monitoring Contributor (read and write), Workbook Contributor (save shared workbooks via `microsoft.insights/workbooks/write` permission).
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview
Date: Updated 2025-06-19

---

## 9. Operational Complexity Comparison

The table below rates each observability capability domain across the three ISV deployment models. Assumptions: mid-size ISV serving 50 enterprise customers; moderate log ingestion volume (50–500 GB/day); AKS-based application workloads.

| Capability | On-Premises | Managed Kubernetes (AKS) | Cloud-Native |
|------------|-------------|--------------------------|--------------|
| **Metrics Collection** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-host Prometheus + Thanos or Cortex for HA; manage scrape configs, storage compaction, retention | Azure Managed Prometheus auto-provisioned with AKS; DCR-based collection; 18-month retention included | Same as Managed K8s; Azure Monitor platform metrics auto-collected from all PaaS services |
| | Prometheus, VictoriaMetrics, Grafana | Azure Managed Prometheus + Managed Grafana | Azure Monitor Metrics (automatic) |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |
| **Log Management** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-host ELK or OpenSearch; manage index lifecycle, shard tuning, cluster scaling | Log Analytics workspace; KQL query language; managed ingestion; 12-year retention available | Same as Managed K8s; all PaaS services auto-emit to Log Analytics |
| | Elasticsearch, Logstash, Kibana | Azure Log Analytics + KQL | Azure Log Analytics (auto-wired) |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.1 |
| **APM / Distributed Tracing** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-host Jaeger or Zipkin; instrument all services; manage trace storage and sampling rules | Application Insights with OTel SDK or auto-instrumentation; smart detection included | Same as Managed K8s; auto-instrumentation for App Service, Functions, AKS |
| | Jaeger, Zipkin, OpenTelemetry Collector | Azure Application Insights (OTel-native) | Azure Application Insights (portal-enabled) |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.2 | Est. FTE: 0.0–0.1 |
| **Alerting** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-manage Alertmanager or PagerDuty integrations; build routing rules | Azure Monitor Alerts with action groups; metric, log, and activity log alert rules | Same as Managed K8s; autoscale and alerts pre-wired to managed services |
| | Prometheus Alertmanager, OpsGenie | Azure Monitor Alerts + Action Groups | Azure Monitor Alerts (pre-configured) |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.15 | Est. FTE: 0.05–0.1 |
| **Dashboards / Visualization** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-host Grafana; manage plugins, upgrades, DB backend, authentication | Azure Managed Grafana or native Grafana in Azure portal (GA at Ignite 2025); Azure Workbooks | Azure Workbooks (built-in); Azure Monitor Dashboards with Grafana (GA, no-cost) |
| | Self-managed Grafana, Kibana | Azure Managed Grafana (Standard tier), Azure Workbooks | Azure Workbooks, Grafana in portal |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.15 | Est. FTE: 0.0–0.05 |
| **Network Observability** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-manage network tap, flow export, and analysis tools | Azure Monitor Network Insights (zero config topology and health); Connection Monitor | Same as Managed K8s; flow logs and traffic analytics available |
| | Wireshark, ntopng, custom NetFlow exporters | Azure Network Insights + Connection Monitor | Azure Network Insights (auto-enabled) |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 | Est. FTE: 0.0–0.05 |
| **Audit / Compliance Logs** | Difficulty: 3/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| | Build custom audit log pipeline; manage retention compliance manually | Activity Log (auto-collected, 90-day free retention; 12-year via Log Analytics export) | Same as Managed K8s; Activity Log is always-on |
| | Custom syslog + SIEM | Azure Activity Log + Log Analytics export | Azure Activity Log (always-on) |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.05 | Est. FTE: 0.0–0.05 |

---

## 10. Summary: What the Azure Managed Stack Abstracts Away

The following operational responsibilities are eliminated or substantially reduced when using the Azure managed observability suite versus self-hosted equivalents:

| Self-Hosted Responsibility | Azure Managed Equivalent | Abstracted |
|---------------------------|--------------------------|-----------|
| Prometheus server deployment and HA (Thanos/Cortex) | Azure Managed Prometheus | Fully |
| TSDB compaction, WAL management, storage scaling | Azure Monitor workspace | Fully |
| 18-month metric data retention | Included in Managed Prometheus pricing | Fully |
| Grafana server, plugin management, database backend | Azure Managed Grafana (Standard) | Fully |
| Grafana authentication (LDAP/SAML) | Microsoft Entra identity | Fully |
| ELK/OpenSearch cluster management | Log Analytics workspace | Fully |
| Log index lifecycle and shard tuning | Azure Log Analytics (managed) | Fully |
| APM backend (Jaeger, Zipkin trace storage) | Application Insights | Fully |
| Anomaly detection model training and operation | Smart Detection (ML built-in) | Fully |
| Network flow monitoring infrastructure | Azure Network Insights | Fully |
| Control plane audit log collection | Activity Log (zero config) | Fully |
| Alertmanager routing and deduplication | Azure Monitor Action Groups | Fully |

---

## Key Takeaways

- **Azure Monitor is a zero-footprint observability platform.** ISVs pay for data ingestion and retention; they do not provision, patch, scale, or operate any monitoring backend infrastructure.

- **Application Insights is now OpenTelemetry-native (2025).** The transition away from the Classic API SDK to the Azure Monitor OpenTelemetry Distro means ISVs can instrument once and emit to Azure or any OTel-compatible backend, reducing future vendor risk.

- **Managed Prometheus and Managed Grafana remove the most operationally intensive self-hosted components.** Self-hosting Prometheus HA with Thanos and Grafana with a backend database is a 0.5–1.5 FTE burden; the managed equivalents reduce this to approximately 0.1–0.3 FTE for configuration and alerting tuning.

- **Native Grafana in the Azure portal reached GA at Ignite 2025.** AKS teams can now access preconfigured Grafana dashboards inside the Azure portal at no additional cost, eliminating the need for a dedicated Azure Managed Grafana instance for most AKS monitoring scenarios.

- **The Activity Log is always-on with zero configuration and zero ingestion cost.** All control plane events (creates, updates, deletes) are captured automatically for 90 days, with 12-year extensibility via Log Analytics — making compliance and change audit logging trivial in any Azure deployment model.

---

## Related — Out of Scope

- **Azure Defender for Cloud / Microsoft Sentinel:** Security event monitoring and SIEM capabilities. Covered in F19.
- **AWS CloudWatch / GCP Cloud Monitoring:** Equivalent observability stacks on competing clouds. Out of scope for this file.
- **Azure Monitor pricing calculator specifics by workload size:** Per-GB ingestion rates change by region and commitment tier; consult the [Azure Monitor pricing page](https://azure.microsoft.com/en-us/pricing/details/monitor/) for current rates.

---

## Sources

| # | Source | URL | Date |
|---|--------|-----|------|
| 1 | Azure Monitor overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/overview | Updated 2025-09-16 |
| 2 | Application Insights OpenTelemetry overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview | Updated 2026-02-11 |
| 3 | Smart detection in Application Insights — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/proactive-diagnostics | Updated 2026-01-16 |
| 4 | Log Analytics workspace overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview | Updated 2025-08-29 |
| 5 | Azure Monitor Logs cost calculations — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs | 2025 |
| 6 | Azure Monitor pricing page — Microsoft Azure | https://azure.microsoft.com/en-us/pricing/details/monitor/ | 2025 |
| 7 | What is Azure Managed Grafana — Microsoft Learn | https://learn.microsoft.com/en-us/azure/managed-grafana/overview | Updated 2025-09-30 |
| 8 | Azure Monitor with Prometheus overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview | Updated 2026-02-03 |
| 9 | Network Insights overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/network-watcher/network-insights-overview | Updated 2025-09-10 |
| 10 | Connection Monitor overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/network-watcher/connection-monitor-overview | 2025 |
| 11 | Azure Monitor Activity Log — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/platform/activity-log | Updated 2025-12-19 |
| 12 | Azure Workbooks overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview | Updated 2025-06-19 |
| 13 | Advancing Full-Stack Observability at Ignite 2025 — Microsoft Tech Community | https://techcommunity.microsoft.com/blog/azureobservabilityblog/advancing-full-stack-observability-with-azure-monitor-at-ignite-2025/4469041 | November 2025 |
| 14 | Azure Monitor Grafana Dashboards in Portal — AKS Engineering Blog | https://blog.aks.azure.com/2025/09/18/azure-monitor-grafana-dashboards-portal | September 2025 |
| 15 | Azure Monitor offers Grafana dashboards natively — Grafana Labs Blog | https://grafana.com/blog/2025/05/19/azure-monitor-offers-grafana-dashboards-natively-for-immediate-real-time-operational-monitoring/ | May 2025 |
| 16 | Azure Monitor Alerts overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview | 2025 |
| 17 | Action groups in Azure Monitor — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups | 2025 |
| 18 | Autoscale common metrics — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-common-metrics | 2025 |
| 19 | Application Insights OpenTelemetry data collection — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview | 2025 |
| 20 | Workbook visualizations — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-visualizations | 2025 |
