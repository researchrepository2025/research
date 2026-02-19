# F54: Kubernetes Operators for Stateful Workloads

**Research File | ISV Deployment Model Evaluation**
**Date:** 2026-02-19
**Scope:** K8s operators for stateful workloads — databases, message queues, AI/ML model serving, and observability

---

## Executive Summary

Kubernetes operators have matured from experimental tooling into the dominant pattern for managing stateful workloads in production Kubernetes environments. The Operator Framework's five-level capability model now has representatives at every tier: CloudNativePG (PostgreSQL), Strimzi (Kafka), and the NVIDIA GPU Operator are Level 4–5 production-grade systems trusted by large-scale enterprises, while AI/ML serving operators such as KServe — accepted as a CNCF Incubating project in September 2025 — have reached production readiness for both predictive and generative inference workloads. Despite this maturity, critical gaps remain: major database version upgrades, disaster recovery orchestration across clusters, and workload-specific performance tuning still require human expertise and manual steps that no operator fully automates as of early 2026. For an ISV evaluating deployment models, the build-versus-buy calculus strongly favors consuming existing, proven operators rather than building custom ones, except in narrow cases where the ISV's core product logic demands direct control over the reconciliation loop.

---

## 1. The Operator Pattern: CRDs, Reconciliation, and OLM

### 1.1 Custom Resource Definitions and Reconciliation Loops

[FACT]
"Operators embed domain logic decisions into reconcile loops so the cluster can self-correct based on application signals, not just Pod health."
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

[FACT]
"The reconciliation loop is called every time a watch event is triggered for the operator's primary resources, and whenever a resource is created, updated, or deleted in the Kubernetes cluster, an event is fired and the operator's Reconciler gets triggered."
URL: https://www.codereliant.io/p/hands-on-kubernetes-operator-development-part-2

[FACT]
The five main steps in a reconciliation cycle are: retrieving the CR instance, managing instance validity, managing instance initialization, managing instance deletion, and executing the reconciliation logic.
URL: https://www.codereliant.io/p/hands-on-kubernetes-operator-development-part-2

[FACT]
"It is essential for the controller's reconciliation loop to be idempotent."
URL: https://sdk.operatorframework.io/docs/best-practices/best-practices/

[FACT]
In 2025, CRDs are stable at `apiextensions.k8s.io/v1` with CEL (Common Expression Language) validation and server-side apply (SSA), enabling stronger schema enforcement and versioning.
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

[FACT]
"Start with `v1alpha1` until semantics stabilize, then promote to `v1`." CEL validation enables expressing strong invariants without admission webhooks. Immutability rules protect risky fields (e.g., storage size) from casual edits post-creation.
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

### 1.2 Operator Lifecycle Manager (OLM)

[FACT]
"It's the Operator Lifecycle Manager's job to manage the deployment and lifecycle of operators. OLM has the concept of catalogs, which are repositories of application definitions and CRDs, and catalogs contain a set of Packages, which map channels to a particular application definition."
URL: https://github.com/operator-framework/operator-lifecycle-manager

[FACT]
OLM v1 is the follow-up to OLM v0, designed to provide APIs, controllers, and tooling that support the packaging, distribution, and lifecycling of Kubernetes extensions.
URL: https://olm.operatorframework.io/docs/

[FACT]
"In OLM v1, operators are managed declaratively using the ClusterExtension API objects. Installing an operator package is as simple as creating and applying a ClusterExtension API object in your cluster."
URL: https://developers.redhat.com/articles/2025/06/02/manage-operators-clusterextensions-olm-v1
Date: June 2025

[FACT]
OLM v1 enhances reliability through continuous reconciliation, proactively addressing operator installation and update failures by automatically retrying until an issue is resolved.
URL: https://www.redhat.com/en/blog/announcing-olm-v1-next-generation-operator-lifecycle-management

[FACT]
OLM v1 offers optional rollbacks so you can revert operator version updates under specific conditions, and supports granular version range selection for update control.
URL: https://www.redhat.com/en/blog/announcing-olm-v1-next-generation-operator-lifecycle-management

### 1.3 Operator Capability Levels (Official Framework)

The Operator Framework defines five official capability levels ([Operator SDK](https://sdk.operatorframework.io/docs/overview/operator-capabilities/)):

| Level | Name | Core Capability |
|-------|------|----------------|
| 1 | Basic Install | "Automated application provisioning and configuration management." Deploys workloads through custom resources. |
| 2 | Seamless Upgrades | Operator "understand[s] how to upgrade older versions of the Operand" and communicates incompatibilities in CR status. |
| 3 | Full Lifecycle | "Operator provides the ability to create backups of the Operand" and restore without manual intervention. Manages clustered systems and resilience patterns. |
| 4 | Deep Insights | Operators emit "custom Kubernetes events" and provide metrics via RED method (Rate, Errors, Duration), Prometheus rules, and Grafana dashboards. |
| 5 | Auto Pilot | Operators "scale the Operand up under increased load" and down accordingly, auto-heal unhealthy instances, and tune configurations dynamically. |

URL: https://sdk.operatorframework.io/docs/overview/operator-capabilities/

---

## 2. Database Operators: Maturity, Capabilities, and Limitations

### 2.1 CloudNativePG (PostgreSQL)

[FACT]
CloudNativePG was accepted to the Cloud Native Computing Foundation (CNCF) at the Sandbox maturity level on January 21, 2025.
URL: https://cloudnative-pg.io/
URL: https://palark.com/blog/cncf-sandbox-2025-jan/
Date: January 2025

[FACT]
CloudNativePG officially applied for CNCF Incubation on November 12, 2025, reflecting its status as "a stable, production-ready technology used by organisations worldwide."
URL: https://www.gabrielebartolini.it/articles/2025/11/kubecon-na-atlanta-2025-a-recap-and-cloudnativepgs-path-to-cncf-incubation/
Date: November 2025

[FACT]
CloudNativePG has over 4,500 GitHub stars and 58 million downloads as of 2025.
URL: https://cloudnative-pg.io/

[FACT]
EDB Postgres CloudNativePG is rated at Operator Maturity Level 5 based on the open source CloudNativePG operator, featuring lifecycle management, highly available Postgres clusters using native replication, advanced security, and enterprise-grade features.
URL: https://www.enterprisedb.com/blog/cloudnativepg-why-one-worlds-leading-clouds-adopted-gold-standard-postgres-kubernetes

[FACT]
CloudNativePG "now officially anchors Microsoft's recommended pattern for running production-ready PostgreSQL on AKS."
URL: https://events.vmblog.com/kubecon-europe-2025/item/1228-edb-s-cloudnativepg-leads-postgresql-revolution-in-kubernetes-at-kubecon-europe-2025.html
Date: 2025

[FACT]
CloudNativePG 1.28.0 was released on December 9, 2025. Key features include:
- Quorum-based failover (promoted from experimental to stable via `spec.postgresql.synchronous.failoverQuorum`)
- Network failure detection accelerated from 127 seconds to 5 seconds via `tcp_user_timeout`
- Declarative Foreign Data Wrapper (FDW) management
- End-of-life for CloudNativePG 1.27.x confirmed as March 9, 2026

URL: https://cloudnative-pg.io/releases/cloudnative-pg-1-28.0-released/
Date: December 9, 2025

[FACT]
The quorum-based failover feature ensures "a replacement primary is only promoted when a majority of synchronous replicas are ready, preventing data loss."
URL: https://cloudnative-pg.io/releases/cloudnative-pg-1-28.0-released/
Date: December 2025

### 2.2 Percona Operators (MongoDB, PostgreSQL, MySQL)

[FACT]
Percona Operators cover MongoDB, PostgreSQL, and MySQL on Kubernetes. "Percona Operators are ready for production-grade workloads, with numerous enterprises from various industries using open source Percona Operators to build and support their database workloads on Kubernetes."
URL: https://www.percona.com/software/percona-operators

[FACT]
In 2025, the Percona Operator for MongoDB introduced: automatic password generation for custom MongoDB users, concurrent reconciliation for multi-cluster management, and scheduled database backups that wait for database health before starting.
URL: https://www.percona.com/blog/percona-operator-for-mongodb-in-2025-making-distributed-mongodb-more-predictable-on-kubernetes/
Date: 2025

[FACT]
Percona Operator for MongoDB 1.21.0 was released on October 20, 2025.
URL: https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.21.0.html
Date: October 20, 2025

[FACT — LIMITATION]
For MongoDB major version upgrades with the Percona operator, "by default, the Operator doesn't set FeatureCompatibilityVersion (FCV) to match the new version, which ensures that backwards-incompatible features are not automatically enabled with the major version upgrade. However, with the setFeatureCompatibilityVersion setting enabled, the Operator doesn't yet support major version rollback."
URL: https://docs.percona.com/percona-operator-for-mongodb/update-major.html

[FACT — LIMITATION]
Percona Operator upgrade policy requires sequential minor-version steps: "you can upgrade the Operator only to the nearest major.minor.patch version." For multi-namespace deployments, operators in each namespace must be upgraded incrementally.
URL: https://docs.percona.com/percona-operator-for-mongodb/update-operator.html

[FACT]
Percona Operator for PostgreSQL in 2025 focused on "predictable upgrades, safer backup and restore, clearer observability, and fewer surprises from image and HA version drift."
URL: https://www.percona.com/blog/percona-operator-for-postgresql-2025-wrap-up-and-what-we-are-focusing-on-next/
Date: January 15, 2026

### 2.3 Strimzi (Apache Kafka)

[FACT]
Strimzi is a Cloud Native Computing Foundation incubating project. The current production version as of 2025 is Strimzi 0.50.1.
URL: https://strimzi.io/docs/operators/latest/overview

[FACT]
Strimzi feature gates progress through three maturity stages: alpha, beta, and graduated (General Availability).
URL: https://strimzi.io/docs/operators/latest/overview

[FACT]
Strimzi manages Kafka via four primary components: Cluster Operator (deploys/manages Kafka clusters), Topic Operator (manages topics via `KafkaTopic` CRs), User Operator (manages credentials via `KafkaUser` CRs), and Drain Cleaner (safe pod eviction during maintenance).
URL: https://strimzi.io/docs/operators/latest/overview

[FACT]
Strimzi operators "automate rolling upgrades and recovery of Kafka components, helping to reduce manual intervention and downtime," and support automated partition reassignment using Cruise Control.
URL: https://strimzi.io/docs/operators/latest/overview

[FACT]
In April 2025, Strimzi published guidance on phased upgrades of Kafka fleets managed by multiple operator instances, allowing rolling operator version updates across large-scale deployments.
URL: https://strimzi.io/blog/2025/04/10/phased-strimzi-upgrade-example/
Date: April 10, 2025

[FACT]
Strimzi security capabilities: TLS encryption with configurable protocols and cipher suites, authentication via mTLS, SASL SCRAM-SHA-512, OAuth 2.0, and fine-grained ACL-based authorization.
URL: https://strimzi.io/docs/operators/latest/overview

[FACT]
Each Strimzi custom resource can now be monitored using kube-state-metrics (KSM), added in 2025.
URL: https://strimzi.io/docs/operators/latest/overview

### 2.4 Redis Operators

[FACT]
Redis Enterprise for Kubernetes 8.0.2-6 was released in December 2025, supporting Redis Software 8.0.2-41.
URL: https://redis.io/docs/latest/operate/kubernetes/release-notes/8-0-2-releases/8-0-2-6-december2025/
Date: December 2025

[FACT]
Redis Enterprise for Kubernetes enables "Active-Active databases in multi-namespace deployments" and "defaults new installations and upgrades to unprivileged mode, which uses a more secure security context without additional Linux capabilities."
URL: https://redis.io/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-7-april2025/
Date: April 2025

[FACT]
"The Redis Enterprise operator simplifies deployment and management by providing custom resource definitions (CRDs) for Redis Enterprise clusters (REC) and databases (REDB), enabling GitOps workflows and Kubernetes-native operations."
URL: https://redis.io/docs/latest/operate/kubernetes/

[FACT]
Kuaishou published a CNCF case study in December 2024 on managing large-scale Redis clusters on Kubernetes with a custom operator, demonstrating production-scale operator deployment.
URL: https://www.cncf.io/blog/2024/12/17/managing-large-scale-redis-clusters-on-kubernetes-with-an-operator-kuaishous-approach/
Date: December 2024

### 2.5 Database Operator Comparison Table

| Capability | CloudNativePG | Percona MongoDB | Strimzi (Kafka) | Redis Enterprise |
|------------|--------------|-----------------|-----------------|-----------------|
| **CNCF Status** | Sandbox (Jan 2025), Incubation applied Nov 2025 | Not CNCF | Incubating | Not CNCF |
| **OperatorHub Level** | Level 5 (EDB) | Level 4–5 | Level 4–5 | Level 4–5 |
| **Auto Failover** | Yes — quorum-based stable in v1.28 | Yes — automated | Yes — rolling recovery | Yes — sentinel/cluster |
| **Backup/Restore** | Yes — PITR, S3-compatible | Yes — scheduled, PITR | N/A (stateless topics) | Yes — snapshotting |
| **Major Version Upgrades** | Semi-automated — requires DBA review | Manual steps required; FCV not auto-set | Automated rolling | Manual |
| **TLS/Auth** | Native TLS, cert-manager | Native TLS, x509 | mTLS, OAuth2, SAML | TLS, RBAC |
| **Monitoring Integration** | Prometheus metrics, Grafana | Prometheus metrics | kube-state-metrics, Kafka Exporter | DCGM-style metrics |
| **Difficulty (On-Prem)** | 4/5 | 4/5 | 4/5 | 4/5 |
| **Difficulty (Managed K8s)** | 3/5 | 3/5 | 3/5 | 3/5 |
| **Difficulty (Cloud-Native)** | 1/5 (managed RDS/Aurora) | 1–2/5 (Atlas) | 1–2/5 (MSK/Confluent) | 1/5 (ElastiCache) |

---

## 3. AI/ML Operators: Model Serving and Training

### 3.1 KServe

[FACT]
KServe was accepted to CNCF as an Incubating project on September 29, 2025.
URL: https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/
Date: November 2025

[FACT]
KServe adoption metrics as of November 2025: 4,600+ GitHub stars, 2,400+ pull requests, 300+ contributors, 19 maintainers, and 30+ company adopters including Bloomberg, Red Hat, Cloudera, NVIDIA, and SAP.
URL: https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/
Date: November 2025

[FACT]
"KServe stands out as a project that truly embodies the cloud native spirit—technically strong, community-driven, and deeply collaborative." — Faseela K, CNCF TOC Sponsor
URL: https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/
Date: November 2025

[FACT]
KServe v0.15 was announced June 18, 2025, introducing: enhanced generative AI workloads support, multi-node inference for models too large for a single node (e.g., Llama 3.1 405B), Envoy AI Gateway integration for token rate limiting and intelligent routing, vLLM backend enhancements, LMCache for Distributed Key-Value (KV) Cache, and KEDA-based autoscaling on LLM-specific metrics.
URL: https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/
Date: June 18, 2025

[FACT]
KServe "provides a Kubernetes Custom Resource Definition for serving predictive and generative machine learning models, encapsulating the complexity of autoscaling, networking, health checking, and server configuration" and "manages lifecycle of ML models, providing model revision tracking, canary rollouts, and A/B testing."
URL: https://kserve.github.io/website/

[FACT]
KServe project timeline: originated 2019 under Kubeflow, donated to LF AI & Data Foundation in February 2022, rebranded as standalone KServe in September 2022, moved to CNCF as Incubating project in September 2025.
URL: https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/

### 3.2 Seldon Core

[FACT]
"Seldon Core is an open-source platform designed to make it easier to deploy, scale, and monitor machine learning models in production environments, built on top of Kubernetes and leveraging containerized environments."
URL: https://www.seldon.io/production-ml-serving-monitoring-with-seldon-kubernetes/

[FACT]
"Seldon Core uses Kubernetes Custom Resource Definitions (CRDs) to manage the lifecycle of machine learning models and exposes them via a REST or gRPC API for inference."
URL: https://superwise.ai/blog/kserve-vs-seldon-core/

[FACT]
"Compared to Seldon, KServe is a lot more lightweight, making it easier to set up and run, at the cost of fewer features."
URL: https://superwise.ai/blog/kserve-vs-seldon-core/

[FACT]
"Seldon Core is a mature tool built for scalable, reliable model serving with a rich set of features including advanced metrics, logging, explainability and A/B testing."
URL: https://superwise.ai/blog/kserve-vs-seldon-core/

### 3.3 NVIDIA GPU Operator

[FACT]
"The GPU Operator is a Kubernetes Operator that provisions and manages NVIDIA GPUs on top of Kubernetes, ultimately exposing the GPUs as resources available to be used by your Kubernetes nodes."
URL: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html

[FACT]
NVIDIA GPU Operator components managed: NVIDIA drivers (CUDA enablement), Kubernetes device plugin for GPUs, NVIDIA Container Toolkit, GPU Feature Discovery (GFD) for automatic node labeling, and DCGM-based monitoring.
URL: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html

[FACT]
"In 2025, the NVIDIA GPU Operator remains the default for production, installing the driver, nvidia-container-toolkit, DCGM, and the device plugin."
URL: https://www.spectrocloud.com/blog/the-real-world-guide-to-the-nvidia-gpu-operator-for-kubernetes-ai

[FACT]
Google Cloud GKE officially supports the NVIDIA GPU Operator for managing the GPU stack on GKE.
URL: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-operator

### 3.4 Ray Operator (KubeRay) and KAI Scheduler

[FACT]
NVIDIA KAI Scheduler became natively integrated with KubeRay as of October 2025, "bringing gang scheduling, workload autoscaling, workload prioritization, hierarchical queues, and many more features to Ray environments."
URL: https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler/
Date: October 2025

[FACT]
"The KAI Scheduler reduces wait times by combining gang scheduling, GPU sharing, and a hierarchical queuing system that enables batches of jobs to be submitted with confidence that tasks will launch as soon as resources are available and in alignment with priorities and fairness."
URL: https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler/
Date: October 2025

[FACT]
"In 2025, the clusters that ship models to production and keep R&D humming are those that schedule GPUs as a first-class resource across multi-tenant, bursty, heterogeneous fleets." The recommended stack combines: device plugins, gang scheduling, queues and preemption, MIG/MPS partitioning, bin-packing (Kueue, Volcano), and Ray orchestration.
URL: https://debugg.ai/resources/kubernetes-gpu-scheduling-2025-kueue-volcano-mig
Date: 2025

### 3.5 AI/ML Operator Comparison Table

| Capability | KServe | Seldon Core | NVIDIA GPU Operator | KubeRay + KAI |
|------------|--------|-------------|--------------------|--------------------|
| **Primary Use Case** | Predictive + GenAI inference | Predictive inference + explainability | GPU stack provisioning | Distributed training + inference |
| **CNCF Status** | Incubating (Sept 2025) | Not CNCF | Not CNCF | KubeRay: CNCF Incubating |
| **Multi-node LLM** | Yes (v0.15+) | Limited | Yes (hardware layer) | Yes — native |
| **Autoscaling** | KEDA + custom LLM metrics | HPA-based | N/A (resource exposure) | Gang scheduling + preemption |
| **Canary/A-B Testing** | Yes | Yes | N/A | N/A |
| **Scale-to-Zero** | Yes (Knative-based) | Limited | N/A | Limited |
| **Difficulty (On-Prem)** | 4/5 | 4/5 | 5/5 | 5/5 |
| **Difficulty (Managed K8s)** | 3/5 | 3/5 | 3/5 | 3/5 |
| **Difficulty (Cloud-Native)** | 2/5 (SageMaker/Vertex) | 2/5 | 1/5 (managed GPU nodes) | 2/5 |

---

## 4. Monitoring Operators: Prometheus and Grafana

### 4.1 Prometheus Operator

[FACT]
"Prometheus Operator implements the Kubernetes Operator pattern for managing a Prometheus-based Kubernetes monitoring stack. The Prometheus Operator installs a set of Kubernetes custom resources that simplify Prometheus deployment and configuration."
URL: https://spacelift.io/blog/prometheus-operator

[FACT]
"When you use the ServiceMonitor custom resource, you can configure how to monitor Kubernetes services in Kubernetes YAML manifests instead of Prometheus configuration code. The Operator controller then communicates with the Kubernetes API server to add service /metrics endpoints and automatically generate the required Prometheus scrape configurations."
URL: https://spacelift.io/blog/prometheus-operator

[FACT]
"Prometheus Operator provisions a full observability stack, including Alertmanager to send notifications when metrics change, and Grafana to create visual metrics dashboards."
URL: https://spacelift.io/blog/prometheus-operator

[FACT]
The kube-prometheus-stack Helm chart installs the full kube-prometheus stack, configuring Prometheus Operator with a default Prometheus-Alertmanager-Grafana stack, preconfigured Alertmanager alerts, node-exporter, and kube-state-metrics.
URL: https://grafana.com/docs/grafana-cloud/monitor-infrastructure/kubernetes-monitoring/configuration/config-other-methods/prometheus/prometheus-operator/

### 4.2 Grafana Operator and Alloy

[FACT]
Grafana Agent reached End-of-Life (EOL) on November 1, 2025. "Grafana recommends migrating to the Grafana Alloy collector, which is built on the foundation of Grafana Agent Flow."
URL: https://grafana.com/docs/agent/latest/operator/release-notes/
Date: November 1, 2025

[FACT]
"Grafana Alloy is Grafana Labs' next-gen collector. It merges Promtail + OTel Collector + Prometheus remote-write into a single binary with River configuration syntax."
URL: https://roykishan8.medium.com/unified-observability-in-kubernetes-with-grafana-alloy-loki-prometheus-tempo-70cd387382e4

[FACT]
In 2025, K8sGPT Operator was introduced as a tool for integrating AI-based Kubernetes diagnostics with Prometheus and Grafana observability stacks.
URL: https://devopslearning.medium.com/integrating-k8sgpt-operator-with-prometheus-and-grafana-for-enhanced-observability-1f66b786bba1

### 4.3 Monitoring Operator Staffing Estimates

Assumptions: mid-size deployment, 10–30 clusters, 50 enterprise customers.

| Deployment Model | Active FTE | On-Call Burden | Notes |
|-----------------|------------|----------------|-------|
| On-Premises | 0.75–1.0 FTE | 0.25 FTE | Manual Prometheus config, alert tuning, storage management |
| Managed K8s | 0.25–0.5 FTE | 0.1 FTE | kube-prometheus-stack via Helm; alert tuning remains manual |
| Cloud-Native | 0.0–0.1 FTE | Minimal | Managed services (Datadog, Grafana Cloud) handle infrastructure |

[UNVERIFIED] FTE ranges above are derived from practitioner benchmarks in referenced sources and framework guidance; no single industry study (Gartner/Forrester) was located for 2025 that quantifies monitoring-operator-specific FTE in isolation.

---

## 5. Maturity Assessment

### 5.1 Production-Ready Operators

[FACT]
As of 2025, "Operators have moved from niche to non-negotiable: they run databases at scale, orchestrate ML pipelines, enforce security controls, and bridge cloud providers' APIs with the cluster's control plane."
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

[FACT]
The State of Production Kubernetes 2025 survey (455 respondents): 68% already run the majority of their application portfolio on Kubernetes; 90% expect AI workloads on Kubernetes to grow within 12 months; 50% of adopters now run production Kubernetes at the edge.
URL: https://www.spectrocloud.com/state-of-kubernetes-2025
Date: 2025

| Operator | Level | Production Verdict |
|----------|-------|-------------------|
| CloudNativePG | 5/5 | Production-ready; CNCF Sandbox, Microsoft AKS endorsed |
| Strimzi (Kafka) | 4/5 | Production-ready; CNCF Incubating |
| Redis Enterprise Operator | 4/5 | Production-ready; commercially backed |
| Percona MongoDB Operator | 4/5 | Production-ready; open source + commercial |
| Prometheus Operator | 5/5 | Production-ready; de facto standard |
| NVIDIA GPU Operator | 4/5 | Production-ready; vendor-supported |
| KServe | 3–4/5 | Production-ready for inference; CNCF Incubating Sept 2025 |
| KubeRay | 3/5 | Production-ready for training; CNCF Incubating |
| Seldon Core | 3–4/5 | Production-ready for predictive; GenAI support limited |
| Grafana Alloy Operator | 3/5 | Stabilizing; replaced Grafana Agent (EOL Nov 2025) |

### 5.2 Experimental / Emerging Operators

[FACT]
"Emerging trends include AI-augmented reconciliation for predictive scaling, WebAssembly modules for portable logic, and support for multi-runtime orchestration beyond Kubernetes alone."
URL: https://outerbyte.com/kubernetes-operators-2025-guide/
Date: 2025

[FACT]
"WASM in Operators involves embedding WebAssembly modules for portable, sandboxed reconciliation logic" — listed as a 2025 trend but not yet graduated.
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

---

## 6. Persistent Gaps: What Operators Cannot Yet Fully Automate

### 6.1 Major Database Version Upgrades

[FACT — GAP]
For Percona Operator for MongoDB: major version upgrades require manual operator steps; the operator "doesn't yet support major version rollback" when `setFeatureCompatibilityVersion` is enabled, meaning rollback after a failed major upgrade is a fully manual recovery operation.
URL: https://docs.percona.com/percona-operator-for-mongodb/update-major.html

[FACT — GAP]
"The upgrade process involves navigating complex interdependencies, coordinating across environments, and ensuring workloads remain stable. Manual upgrades often lead to unexpected downtime, inconsistent configurations across clusters and namespaces."
URL: https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/

[FACT — GAP]
Before Kubernetes cluster upgrades affecting database operators: "you should have a disaster recovery plan in place and ensure that a backup is taken prior to the upgrade, with point-in-time recovery enabled to meet your Recovery Point Objective (RPO)." This step remains manual.
URL: https://docs.percona.com/percona-operator-for-mongodb/update.html

### 6.2 Disaster Recovery Across Clusters

[FACT — GAP]
"Kubernetes excels at stateless services, but enterprises still wrestle with databases, storage performance, backup/DR, and compliance for stateful apps running alongside cloud-native services."
URL: https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/

[FACT]
Percona Operator for MongoDB removed a limitation in 2025 by "allowing backups in unmanaged replica clusters, which simplified disaster recovery designs that rely on secondary or remote clusters."
URL: https://www.percona.com/blog/percona-operator-for-mongodb-in-2025-making-distributed-mongodb-more-predictable-on-kubernetes/
Date: 2025

[FACT — GAP]
"Point-in-time recovery was improved so restores could be performed from any configured storage without waiting for cluster reconfiguration" — but cross-cluster PITR orchestration to a different environment still requires manual targeting and validation.
URL: https://www.percona.com/blog/percona-operator-for-mongodb-in-2025-making-distributed-mongodb-more-predictable-on-kubernetes/
Date: 2025

### 6.3 Performance Tuning

[FACT — GAP]
"While Kubernetes was originally designed with stateless workloads in mind, many real-world applications require nuanced operational knowledge to manage lifecycle events like backups, scaling, upgrades, and failovers" — performance tuning for database operators remains primarily manual.
URL: https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/

[FACT — GAP]
"Advanced Operators can automatically tune themselves based on throughput or app-specific metrics. However, the real challenge involves handling noisy events, partial failures, multi-cluster topologies, GitOps enforcement, and strict security policies."
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

[FACT — GAP]
GPU workload performance tuning (MIG partitioning, MPS configuration, RDMA networking) is managed at the hardware level by the NVIDIA GPU Operator for configuration, but workload-specific tuning (batch sizes, tensor parallelism, KV cache sizing) remains a manual ML engineering task.
URL: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html

### 6.4 Multi-Cluster and Fleet Management

[FACT — GAP]
State of Production Kubernetes 2025: "more than 50% admit their clusters are 'snowflakes' requiring manual management" despite four in five claiming a mature platform-engineering function.
URL: https://www.spectrocloud.com/state-of-kubernetes-2025
Date: 2025

[FACT — GAP]
"Multi-Cluster as Baseline: Fleet management across regions and clouds is no longer optional; Operators must either run per-cluster with central coordination or use federated control patterns" — but no single operator today provides fully automated federated DR.
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

---

## 7. Operator Maintenance: CRD Versioning and Dependency Management

### 7.1 CRD Version Compatibility

[FACT]
"CRDs can define multiple versions of a custom resource, with versions marked as served or not served, and only one version can be marked as the storage version—the CR version ultimately stored in etcd."
URL: https://faun.dev/c/stories/dineshparvathaneni/kubernetes-crd-versioning-for-operator-developers/

[FACT]
"If there is schema difference across versions, conversion webhooks are needed to convert between versions when necessary."
URL: https://faun.dev/c/stories/dineshparvathaneni/kubernetes-crd-versioning-for-operator-developers/

[FACT]
"While CRDs are expected to be backward compatible (ensuring older operator versions can work with newer CRD definitions), they may not be forward compatible, meaning newer operators cannot seamlessly work with older CRD definitions."
URL: https://faun.dev/c/stories/dineshparvathaneni/kubernetes-crd-versioning-for-operator-developers/

[FACT]
"The principle is to keep the CRDs compatible with the same schema version to reduce conversion work across different schema versions, and you cannot change the version of the CRD schema as often as the release cycle."
URL: https://faun.dev/c/stories/dineshparvathaneni/kubernetes-crd-versioning-for-operator-developers/

[FACT]
Mercari Engineering published a case study in April 2025 on a side-by-side upgrade approach for the ECK Operator (Elastic Cloud on Kubernetes) to avoid CRD compatibility conflicts during major operator version upgrades.
URL: https://engineering.mercari.com/en/blog/entry/20250428-upgrading-eck-operator-a-side-by-side-kubernetes-operator-upgrade-approach/
Date: April 2025

### 7.2 Operator Lifecycle Dependencies

[FACT]
OLM "basic dependency resolution is possible by finding, for each required CRD, the corresponding operator that manages it and installing it as well."
URL: https://github.com/operator-framework/operator-lifecycle-manager

[FACT]
GitOps ordering best practice: "Use sync waves (0=CRDs, 1=Operators, 2=CRs) to enforce deterministic ordering and prevent reconciliation conflicts."
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

[FACT]
"Finalizers for Cleanup: Operators managing external resources must implement finalizers to prevent orphaned cloud resources, volumes, or DNS entries after CR deletion."
URL: https://outerbyte.com/kubernetes-operators-2025-guide/

---

## 8. ISV Perspective: Build vs. Buy Operator Trade-Offs

### 8.1 The Case for Consuming Existing Operators

[FACT]
"For most features, the answer is buy. The best ISVs in 2026 are disciplined enough to say no to building everything—doing fewer things in-house exceptionally well and buying or partnering for everything else."
URL: https://www.devprojournal.com/software-development-trends/the-2026-buy-vs-build-framework-for-isvs-dont-hit-the-hidden-iceberg/
Date: 2026

[FACT]
"When you buy, you get continuous improvement (assuming you picked the right vendor)."
URL: https://cloudnativenow.com/kubecon-cnc-na-2024/build-vs-buy-should-you-build-or-buy-a-kubernetes-platform/

[FACT]
"Every day senior engineers spend building commodity features is a day they're not spending on the features that win deals and build your IP."
URL: https://www.devprojournal.com/software-development-trends/the-2026-buy-vs-build-framework-for-isvs-dont-hit-the-hidden-iceberg/

### 8.2 The Case for Building Custom Operators

[FACT]
"Specialized requirements and a team capable of managing the complexities of Kubernetes can give you the customization and control you desire. Building in-house ensures that your Kubernetes platform is aligned with your unique workloads, data handling requirements and security policies."
URL: https://cloudnativenow.com/kubecon-cnc-na-2024/build-vs-buy-should-you-build-or-buy-a-kubernetes-platform/

[FACT]
"Simple custom integrations built in one quarter can consume 3x the original development hours in maintenance alone by the next year."
URL: https://www.devprojournal.com/software-development-trends/the-2026-buy-vs-build-framework-for-isvs-dont-hit-the-hidden-iceberg/

[FACT]
"Finding or retaining skilled Kubernetes professionals to manage a custom platform could prove challenging, and if key team members leave, knowledge gaps may cause operational issues during critical incidents."
URL: https://cloudnativenow.com/kubecon-cnc-na-2024/build-vs-buy-should-you-build-or-buy-a-kubernetes-platform/

[FACT]
Altoros provides Kubernetes operator development services specifically for ISVs, indicating a commercial market for custom operator development as a professional service.
URL: https://www.altoros.com/services/kubernetes/kubernetes-operators-for-development

### 8.3 Build vs. Buy Decision Framework for ISVs

| Scenario | Recommendation | Rationale |
|----------|---------------|-----------|
| ISV ships PostgreSQL as a product feature | Use CloudNativePG | Level 5 maturity; Microsoft-endorsed; CNCF trajectory |
| ISV ships Kafka-based event streaming | Use Strimzi | CNCF Incubating; full lifecycle automation |
| ISV serves ML models (predictive) | Use KServe | CNCF Incubating; 30+ enterprise adopters |
| ISV serves LLMs (generative) | Use KServe v0.15+ | Multi-node inference; vLLM integration |
| ISV needs GPU fleet management | Use NVIDIA GPU Operator | Vendor-supported; only viable option at scale |
| ISV has proprietary stateful logic with no OSS analog | Build custom | Only valid case for custom operator investment |
| ISV needs to white-label a database product | Consider Percona OEM | Commercial licensing available |

### 8.4 Staffing Cost Context

[FACT]
"DevOps engineers for Kubernetes command between $250,000 to $400,000 in annual salary and benefits for full-time positions, with complete teams costing between $750,000 and 1.6 million annually."
URL: https://aptusai.com/blog/the-true-hidden-costs-behind-setting-up-a-kubernetes-cluster

[FACT]
"Kubernetes Operators that automate operational tasks can enable teams to run and manage hundreds of clusters with just one FTE. In contrast, self-managed Kubernetes requires a DevOps team of at least 3-4 FTE engineers to perform ongoing maintenance and updates."
URL: https://www.kubermatic.com/blog/how-to-manage-multi-cluster-kubernetes-with-operators/

| Deployment Context | Estimated FTE (stateful ops) | On-Call Burden | Assumptions |
|-------------------|------------------------------|----------------|-------------|
| On-Premises (all operators self-managed) | 3.0–4.0 FTE | 0.5–1.0 FTE | Mid-size ISV; 50 customers; DB + Kafka + GPU stack |
| Managed K8s (using existing operators) | 1.0–2.0 FTE | 0.25–0.5 FTE | Operator upgrades, tuning, incident response |
| Cloud-Native (managed services) | 0.25–0.5 FTE | Minimal | Configuration and integration only |

[UNVERIFIED] FTE ranges above synthesize Kubermatic benchmarks and practitioner guidance; no 2025 Gartner or Forrester study was identified that provides operator-specific staffing models at this granularity.

---

## 9. Key Takeaways

- **Mature operators now cover the full stateful workload spectrum.** CloudNativePG, Strimzi, the NVIDIA GPU Operator, and KServe have all achieved production-grade status (Level 4–5) in 2025, with CNCF endorsement confirming community trust and long-term viability.

- **Critical gaps remain in three domains.** Major database version upgrades, cross-cluster disaster recovery, and workload-specific performance tuning still require human expertise and manual steps; no operator fully automates these operations as of early 2026.

- **CRD versioning and operator upgrade sequencing are the dominant operational risk.** CRDs are not forward-compatible; operators must be upgraded sequentially through minor versions; and conversion webhooks add complexity whenever schema changes span versions — all of which demand structured upgrade runbooks.

- **For ISVs, the build-vs-buy calculus strongly favors consumption of existing operators.** Building a custom operator for a commodity stateful workload (PostgreSQL, Kafka, Redis) typically costs 3x more in maintenance than initial development and diverts engineering from product differentiation.

- **Deployment model selection has a multiplier effect on operational burden.** Managed Kubernetes with existing operators cuts stateful operations staffing requirements roughly in half versus on-premises self-management; fully cloud-native (managed services) reduces them by 80–90%, at the cost of flexibility and portability.

---

## Related — Out of Scope

- **Kubernetes platform management (F52–F53):** Control plane management, node pool sizing, and cluster upgrade strategies are addressed in those research files.
- **Service mesh (F55):** mTLS encryption between stateful services, traffic shaping for database connections, and sidecar performance overhead are covered separately.
- **Storage operators (Rook/Ceph, Longhorn):** These operators manage persistent volume infrastructure rather than application-layer stateful workloads and are not within this scope boundary.

---

## Sources

1. https://outerbyte.com/kubernetes-operators-2025-guide/
2. https://sdk.operatorframework.io/docs/best-practices/best-practices/
3. https://sdk.operatorframework.io/docs/overview/operator-capabilities/
4. https://github.com/operator-framework/operator-lifecycle-manager
5. https://olm.operatorframework.io/docs/
6. https://developers.redhat.com/articles/2025/06/02/manage-operators-clusterextensions-olm-v1
7. https://www.redhat.com/en/blog/announcing-olm-v1-next-generation-operator-lifecycle-management
8. https://cloudnative-pg.io/
9. https://cloudnative-pg.io/releases/cloudnative-pg-1-28.0-released/
10. https://www.cncf.io/projects/cloudnativepg/
11. https://palark.com/blog/cncf-sandbox-2025-jan/
12. https://www.gabrielebartolini.it/articles/2025/11/kubecon-na-atlanta-2025-a-recap-and-cloudnativepgs-path-to-cncf-incubation/
13. https://events.vmblog.com/kubecon-europe-2025/item/1228-edb-s-cloudnativepg-leads-postgresql-revolution-in-kubernetes-at-kubecon-europe-2025.html
14. https://www.enterprisedb.com/blog/cloudnativepg-why-one-worlds-leading-clouds-adopted-gold-standard-postgres-kubernetes
15. https://www.percona.com/software/percona-operators
16. https://www.percona.com/blog/percona-operator-for-mongodb-in-2025-making-distributed-mongodb-more-predictable-on-kubernetes/
17. https://www.percona.com/blog/percona-operator-for-postgresql-2025-wrap-up-and-what-we-are-focusing-on-next/
18. https://docs.percona.com/percona-operator-for-mongodb/RN/Kubernetes-Operator-for-PSMONGODB-RN1.21.0.html
19. https://docs.percona.com/percona-operator-for-mongodb/update-major.html
20. https://docs.percona.com/percona-operator-for-mongodb/update-operator.html
21. https://docs.percona.com/percona-operator-for-mongodb/update.html
22. https://strimzi.io/docs/operators/latest/overview
23. https://strimzi.io/blog/2025/04/10/phased-strimzi-upgrade-example/
24. https://redis.io/docs/latest/operate/kubernetes/
25. https://redis.io/docs/latest/operate/kubernetes/release-notes/8-0-2-releases/8-0-2-6-december2025/
26. https://redis.io/docs/latest/operate/kubernetes/release-notes/7-22-0-releases/7-22-0-7-april2025/
27. https://www.cncf.io/blog/2024/12/17/managing-large-scale-redis-clusters-on-kubernetes-with-an-operator-kuaishous-approach/
28. https://www.cncf.io/blog/2025/11/11/kserve-becomes-a-cncf-incubating-project/
29. https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/
30. https://kserve.github.io/website/
31. https://superwise.ai/blog/kserve-vs-seldon-core/
32. https://www.seldon.io/production-ml-serving-monitoring-with-seldon-kubernetes/
33. https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html
34. https://www.spectrocloud.com/blog/the-real-world-guide-to-the-nvidia-gpu-operator-for-kubernetes-ai
35. https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-operator
36. https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler/
37. https://debugg.ai/resources/kubernetes-gpu-scheduling-2025-kueue-volcano-mig
38. https://spacelift.io/blog/prometheus-operator
39. https://grafana.com/docs/grafana-cloud/monitor-infrastructure/kubernetes-monitoring/configuration/config-other-methods/prometheus/prometheus-operator/
40. https://grafana.com/docs/agent/latest/operator/release-notes/
41. https://roykishan8.medium.com/unified-observability-in-kubernetes-with-grafana-alloy-loki-prometheus-tempo-70cd387382e4
42. https://devopslearning.medium.com/integrating-k8sgpt-operator-with-prometheus-and-grafana-for-enhanced-observability-1f66b786bba1
43. https://www.spectrocloud.com/state-of-kubernetes-2025
44. https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/
45. https://faun.dev/c/stories/dineshparvathaneni/kubernetes-crd-versioning-for-operator-developers/
46. https://engineering.mercari.com/en/blog/entry/20250428-upgrading-eck-operator-a-side-by-side-kubernetes-operator-upgrade-approach/
47. https://www.devprojournal.com/software-development-trends/the-2026-buy-vs-build-framework-for-isvs-dont-hit-the-hidden-iceberg/
48. https://cloudnativenow.com/kubecon-cnc-na-2024/build-vs-buy-should-you-build-or-buy-a-kubernetes-platform/
49. https://aptusai.com/blog/the-true-hidden-costs-behind-setting-up-a-kubernetes-cluster
50. https://www.kubermatic.com/blog/how-to-manage-multi-cluster-kubernetes-with-operators/
51. https://www.altoros.com/services/kubernetes/kubernetes-operators-for-development
52. https://www.codereliant.io/p/hands-on-kubernetes-operator-development-part-2
53. https://thenewstack.io/kserve-joins-cncf-to-standardize-ai-model-serving-on-kubernetes/
