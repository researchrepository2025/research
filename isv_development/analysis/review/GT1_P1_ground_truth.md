# GT1: P1 Control Plane — Ground Truth Extraction
## Authoritative Data Reference for 35-Agent Strategic Review
**Extraction Date:** 2026-02-19
**Source File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`
**Extraction Scope:** P1 Control Plane only (CP-01 through CP-10). P2, P3, and P4 data excluded per scope boundary.
**Reference Baseline:** Mid-size ISV, 50 enterprise customers, 3–5 clusters.

---

## Executive Summary

The P1 Control Plane source file (P1_control_plane.md, dated 2026-02-19) defines ten MECE subsegments governing all infrastructure between cluster creation and application business logic, covering cluster lifecycle, networking, identity, secrets, observability, CI/CD, deployment mechanics, disaster recovery, compliance, and security operations. Composite difficulty ratings span 1–5 across three deployment tiers, with cloud-native averaging 1.3/5, managed K8s averaging 2.8/5, and on-premises averaging 4.7/5; the corresponding aggregate FTE ranges are approximately 2.5–6.5 (cloud-native), 9–16 (managed K8s), and 20–38 (on-premises) for the reference ISV baseline. Six of ten subsegments are rated 5/5 on-premises (CP-01, CP-02, CP-04, CP-07, CP-08, CP-09, CP-10), and the source explicitly states that on-premises operational work scales linearly with customer count while cloud-native scales sub-linearly.

---

## Difficulty Scale Reference

Source: P1_control_plane.md, "Difficulty Scale Reference" section.

| Rating | Label | FTE Indicative |
|:---:|---|---|
| 1 | Trivial | < 0.1 FTE |
| 2 | Low | 0.1–0.3 FTE |
| 3 | Moderate | 0.3–0.75 FTE |
| 4 | High | 0.75–1.5 FTE |
| 5 | Extreme | 1.0+ FTE per subsegment |

---

## CP-01: Kubernetes Cluster Lifecycle Management

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-01: Kubernetes Cluster Lifecycle Management — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Control plane operations | 1 | 1 | 5 |
| Node pool lifecycle | 2 | 2 | 5 |
| Add-on ecosystem management | 1 | 3 | 5 |
| Version currency / upgrade cadence | 1 | 3 | 5 |
| **Composite Rating** | **1** | **3** | **5** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-01 — FTE Estimates (mid-size ISV, 50 customers, 3–5 clusters)"

[STATISTIC] Cloud-Native: 0.0–0.5 FTE
[STATISTIC] Managed K8s: 1.0–2.5 FTE
[STATISTIC] On-Premises: 3.0–6.0 FTE (including upgrade coordination per customer)

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-01 — Evidence"

[FACT] "Provider manages the API server, etcd, scheduler, and controller manager entirely. EKS costs $0.10/hour ($73/month per cluster); AKS offers a free control plane."
— P1_control_plane.md, CP-01 Evidence (citing F52, W07S)

[FACT] "ISVs must manage at least a dozen add-on components — ingress controllers, RBAC policies, storage classes, network policies, secrets management — requiring 1.0–2.5 FTE for base platform operations across 3–5 clusters serving 50 enterprise customers."
— P1_control_plane.md, CP-01 Evidence (citing W07S Theme 1, F52)

[FACT] "Kubernetes releases approximately 3 minor versions per year with 12–14 month support windows."
— P1_control_plane.md, CP-01 Evidence (citing F52, W07S Theme 1)

[FACT] "AKS LTS extends Kubernetes version support to 24 months — a meaningful reduction in upgrade frequency pressure for managed K8s deployments."
— P1_control_plane.md, CP-01 Evidence (citing F52, W07S Theme 1)

[FACT] "VMware post-Broadcom-acquisition price increases of 8–15x eliminate the previously dominant hypervisor path. SUSE Rancher CPU-based pricing caused 4–9x cost increases in 2025, driving enterprise migration away from previously stable on-premises Kubernetes distribution choices."
— P1_control_plane.md, CP-01 Evidence (citing W06S Theme 1, W07S Theme 5, F53)

### Scaling Behavior
[FACT] On-premises upgrade coordination scales per customer — each customer environment requires separate node draining, validation, and coordination sequences.
Source: P1_control_plane.md, CP-01 Evidence

### Dependencies
CP-01 is the foundational substrate for CP-02 through CP-10. All other control plane components run on the cluster infrastructure it defines.
Source: P1_control_plane.md, CP-01 MECE boundary

### Notable Caveats / Technology Transitions
[FACT] "The Ingress NGINX Controller — powering approximately 41% of internet-facing Kubernetes clusters — was officially retired in November 2025, with best-effort maintenance ending March 2026, forcing mandatory migration to the Kubernetes Gateway API."
— P1_control_plane.md, CP-01 Evidence (citing F73 C03, F40)

[STATISTIC] "This represents unplanned 0.3–0.6 FTE of platform work for managed K8s ISVs in 2026 regardless of product roadmap priority."
— P1_control_plane.md, CP-01 Evidence (citing F73 C03, F40)

---

## CP-02: Network Fabric, Ingress, and Service Mesh

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-02: Network Fabric, Ingress, and Service Mesh — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Load balancer / ingress provisioning | 1 | 2 | 5 |
| Network segmentation / policy enforcement | 1 | 3 | 5 |
| DNS (internal and external) | 1 | 2 | 4 |
| Service mesh (if adopted) | 3 | 4 | 5 |
| **Composite Rating** | **1** | **3** | **5** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-02 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.1–0.7 FTE
[STATISTIC] Managed K8s: 0.75–1.75 FTE (add 0.5–1.0 FTE if service mesh adopted)
[STATISTIC] On-Premises: 1.75–3.5 FTE (add 1.0–2.0 FTE if service mesh adopted)

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-02 — Evidence"

[FACT] "AWS ALB, Azure Application Gateway, and GCP Cloud Load Balancing are fully managed with SLAs. Route 53, Azure DNS, and Cloud DNS are fully managed with 100% SLA targets."
— P1_control_plane.md, CP-02 Evidence (citing F76 Domain 2)

[FACT] "CoreDNS is self-managed; scaling, HPA configuration, and Linux conntrack tuning required. A 2025 EKS incident traced a Linux conntrack management bug in CoreDNS that caused cascading DNS timeouts across all dependent services."
— P1_control_plane.md, CP-02 Evidence (citing F76 Domain 2)

[FACT] "On-Premises networking requires total FTE of 1.75–3.5 (mid-size ISV) for HAProxy, Consul, CoreDNS, Calico/Cilium NetworkPolicy, and manual VLAN segmentation."
— P1_control_plane.md, CP-02 Evidence (citing F40, F76 Domain 1)

[FACT] "Physical switch failures propagate until redundant paths activate; ECMP and spanning tree convergence times can reach minutes."
— P1_control_plane.md, CP-02 Evidence (citing F40, F76 Domain 1)

### Scaling Behavior
[FACT] DNS failures carry "uniquely high blast-radius because resolution is a prerequisite for nearly every service-to-service call."
Source: P1_control_plane.md, CP-02 Evidence (citing F76 Domain 2)

### Dependencies
CP-02 depends on CP-01 (the cluster substrate). CP-02 explicitly excludes TLS certificate lifecycle — that belongs to CP-04 (CP-04 boundary stated in CP-02 MECE section).
Source: P1_control_plane.md, CP-02 MECE boundary

### Notable Caveats / Technology Transitions
[STATISTIC] "Service mesh adoption declined from 50% (2023) to 42% (2024) to approximately 8% developer-level adoption by Q3 2025."
— P1_control_plane.md, CP-02 Evidence (citing F55, W07S Theme 5)

[FACT] "Istio sidecar mode adds 166% latency overhead at 3,200 RPS; Istio Ambient mode adds only 8% latency; Linkerd requires 1/8th to 1/9th the resources of Istio."
— P1_control_plane.md, CP-02 Evidence (citing F55, W07S Theme 5)

[FACT] Ingress NGINX EOL March 2026 — mandatory migration to Kubernetes Gateway API. Affects CP-02 directly.
Source: P1_control_plane.md, Cross-Subsegment Pattern 3 (citing F73 C03, F40)

---

## CP-03: Identity, Access Management, and RBAC

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-03: Identity, Access Management, and RBAC — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Identity provider operations | 1 | 2 | 4 |
| RBAC / policy engine management | 1 | 3 | 5 |
| Workload identity (service accounts) | 1 | 2 | 4 |
| Directory services (AD/LDAP) | 1 | 2 | 4 |
| **Composite Rating** | **1** | **2** | **4** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-03 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.30–0.80 FTE
[STATISTIC] Managed K8s: 1.65–2.65 FTE
[STATISTIC] On-Premises: 2.75–4.75 FTE

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-03 — Evidence"

[FACT] "AWS IAM roles for service accounts (IRSA), GKE Workload Identity, and Azure Workload Identity are managed by the provider. Cloud-native difficulty rated 1/5 for directory and 1/5 for RBAC."
— P1_control_plane.md, CP-03 Evidence (citing F46, F55c)

[FACT] "Self-hosted Keycloak, Authentik, or Active Directory requires HA configuration, patch lifecycle, and dedicated identity expertise. IAM is described as 'a product line, not an infrastructure dependency' with seven sub-domains each rated 3–4/5 difficulty."
— P1_control_plane.md, CP-03 Evidence (citing F46, W06S Theme 2)

[FACT] "Kubernetes RBAC / IAM on-premises is rated 5/5 difficulty; cloud-native is rated 1/5."
— P1_control_plane.md, CP-03 Evidence (citing F55c)

### Scaling Behavior
[FACT] On-premises carries 50 separate compliance audit surfaces for a 50-customer fleet — each customer environment represents a distinct identity domain requiring independent verification.
Source: P1_control_plane.md, Cross-Subsegment Pattern 2 (citing W08S Theme 5, F59)

### Dependencies
CP-03 depends on CP-04 for certificate assets used to establish mTLS trust (boundary stated explicitly). A role binding change triggers CP-03 work; a certificate rotation triggers CP-04 work.
Source: P1_control_plane.md, CP-03 MECE boundary

### Notable Caveats / Technology Transitions
[FACT] "GKE deprecated Identity Service for GKE for new organizations as of July 1, 2025, mandating migration to Workforce Identity Federation."
— P1_control_plane.md, CP-03 Evidence (citing F73 C01, F46)

[FACT] "Apple's acquisition of the OPA maintainer team in August 2025 creates a policy-engine risk for ISVs dependent on OPA/Gatekeeper. Kyverno is the primary alternative with a stable CNCF governance path."
— P1_control_plane.md, CP-03 Evidence (citing F46, W06S Theme 2)

---

## CP-04: Secrets Management, Certificate Lifecycle, and PKI

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-04: Secrets Management, Certificate Lifecycle, and PKI — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Secret store operations | 1 | 2 | 5 |
| Certificate authority / PKI | 1 | 2 | 4 |
| HSM integration | 2 | 3 | 5 |
| Rotation automation | 1 | 2 | 4 |
| **Composite Rating** | **1** | **2** | **5** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-04 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.4–0.85 FTE
[STATISTIC] Managed K8s: 0.4–0.85 FTE
[STATISTIC] On-Premises: 2.5–5.0 FTE

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-04 — Evidence"

[FACT] "AWS Secrets Manager, Azure Key Vault, and GCP Secret Manager with automatic rotation. ACM (AWS), Managed Certificates (GCP), and App Gateway (Azure) auto-renew TLS certificates with zero operator action."
— P1_control_plane.md, CP-04 Evidence (citing F47, F76 Domain 3)

[FACT] "Native Kubernetes Secrets are base64-encoded rather than encrypted — every production deployment must explicitly enable etcd encryption or use External Secrets Operator."
— P1_control_plane.md, CP-04 Evidence (citing F55c, F76 Domain 3, W07S Theme 4)

[FACT] "HashiCorp Vault minimum 5-node Raft cluster."
— P1_control_plane.md, CP-04 Evidence (citing F47, W06S Theme 2, F76 Domain 3)

[FACT] "HSM hardware costs $5K–$50K per unit."
— P1_control_plane.md, CP-04 Evidence (citing F47, W06S Theme 2, F76 Domain 3)

### Scaling Behavior
[FACT] Certificate rotation frequency is a universal cross-tier concern that scales with Let's Encrypt policy changes affecting all certificate holders simultaneously regardless of deployment tier.
Source: P1_control_plane.md, CP-04 Evidence and Cross-Subsegment Pattern 3

### Dependencies
CP-04 depends on CP-03 for the identity policy governing who accesses which secret (stated in MECE boundary). Shares FTE overlap with CP-03 and CP-10 in security cluster — source estimates 1.0–2.0 FTE deduplication across the three.
Source: P1_control_plane.md, CP-04 MECE boundary; Summary FTE table deduplication note

### Notable Caveats / Technology Transitions
[FACT] "FIPS 140-2 certificate validity expires September 2026 — HSM firmware and Vault seal configurations must transition to FIPS 140-3 before that date."
— P1_control_plane.md, CP-04 Evidence (citing F47, W06S Theme 2, F76 Domain 3)

[FACT] "Let's Encrypt announced in December 2025 that certificate validity will decrease to 45 days on May 13, 2026 — increasing rotation frequency requirements for all tiers."
— P1_control_plane.md, CP-04 Evidence (citing F47, W06S Theme 2, F76 Domain 3)

---

## CP-05: Observability Infrastructure (Metrics, Logs, Traces)

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-05: Observability Infrastructure — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Metrics backend (Prometheus/Thanos/Mimir) | 1 | 3 | 4 |
| Logging backend (ELK/Loki) | 1 | 3 | 4 |
| Tracing backend (Jaeger/Tempo) | 1 | 3 | 5 |
| Storage management and retention | 1 | 2 | 5 |
| Cardinality governance | 1 | 3 | 4 |
| **Composite Rating** | **1** | **3** | **4** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-05 — FTE Estimates (combined metrics + logs + traces)"

[STATISTIC] Cloud-Native: 0.55–1.0 FTE
[STATISTIC] Managed K8s: 1.25–2.0 FTE
[STATISTIC] On-Premises: 4.6–7.0 FTE (logging 1.5–2.0 + monitoring 1.5–2.5 + tracing 1.6–2.5)

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-05 — Evidence"

[FACT] "The kube-prometheus-stack (Prometheus Operator, Grafana, Alertmanager) consumes 15–35 GB of cluster RAM before any application workloads are monitored."
— P1_control_plane.md, CP-05 Evidence (citing F55d, W07S Theme 4)

[STATISTIC] "A 100-node cluster can generate 500,000+ active Prometheus time series at approximately 3 KB RAM per series."
— P1_control_plane.md, CP-05 Evidence (citing F49, F50, W06S Theme 4)

[STATISTIC] "AWS Managed Prometheus at 1M samples/sec costs approximately $47K/month versus self-hosted approximately $6K/month (7.8x cost differential)."
— P1_control_plane.md, CP-05 Evidence (citing F49, F50, W06S Theme 4)

[STATISTIC] "Self-hosted Loki at 100 GB/day costs approximately $300/month versus CloudWatch $1,665/month (75–90% cost reduction). The cost crossover point for logging sits at 50–100 GB/day."
— P1_control_plane.md, CP-05 Evidence (citing F49, F50, W06S Theme 4)

[FACT] "Recommended hybrid approach: cloud-managed Prometheus for metrics, self-managed Loki/Tempo for logs and traces — introducing split-stack operational complexity."
— P1_control_plane.md, CP-05 Evidence (citing F55d, W07S Theme 4)

### Scaling Behavior
[FACT] Observability storage and cardinality requirements scale with cluster node count. A 100-node cluster generates 500,000+ active time series.
Source: P1_control_plane.md, CP-05 Evidence (citing F49, F50, W06S Theme 4)

### Dependencies
CP-05 is strictly the observability backend infrastructure. Application instrumentation code (OpenTelemetry SDK spans and metrics) is application logic per F73 C07 — explicitly out of CP-05 scope.
Source: P1_control_plane.md, CP-05 MECE boundary

### Notable Caveats / Technology Transitions
[FACT] "Jaeger v1 was deprecated January 2026 — migration to v2 (OTel Collector-based) is required."
— P1_control_plane.md, CP-05 Evidence (citing F51, W06S Theme 3 and Theme 4)

[FACT] "MinIO entered maintenance mode late 2025 and was archived by early 2026, affecting on-premises tracing storage backends."
— P1_control_plane.md, CP-05 Evidence (citing F51, W06S Theme 3 and Theme 4)

[FACT] "OpenTelemetry consistent probability sampling specification was adopted October 2025. OpenTelemetry is the second-highest-velocity CNCF project with 24,000+ contributors as of the 2025 CNCF Annual Survey."
— P1_control_plane.md, CP-05 Evidence (citing F51, F77)

---

## CP-06: CI/CD Pipeline Infrastructure and GitOps

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-06: CI/CD Pipeline Infrastructure and GitOps — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| CI runner infrastructure | 1 | 2 | 4 |
| Container registry operations | 1 | 2 | 3 |
| GitOps controller operations | 1 | 2 | 3 |
| Air-gap bundle delivery | N/A | 3 | 5 |
| Artifact signing / supply chain | 2 | 3 | 4 |
| **Composite Rating** | **1** | **3** | **4** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-06 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.3–0.4 FTE
[STATISTIC] Managed K8s: 1.3–1.9 FTE
[STATISTIC] On-Premises: 2.0–3.25 FTE

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-06 — Evidence"

[FACT] "GitHub Actions, AWS CodePipeline, Azure DevOps, and Google Cloud Build eliminate pipeline infrastructure management. ECR, GCR, and ACR handle registry operations."
— P1_control_plane.md, CP-06 Evidence (citing F48, F73 C08)

[STATISTIC] "Argo CD is adopted in 60% of Kubernetes clusters per the 2025 CNCF End User Survey."
— P1_control_plane.md, CP-06 Evidence (citing F48, F73 C08, W07S)

[FACT] "Flux manages approximately 200 Kubernetes clusters at Deutsche Telekom with just 10 full-time engineers, with plans to scale to thousands of clusters without proportional FTE growth."
— P1_control_plane.md, CP-06 Evidence (citing F48, F73 C08, W07S)

[FACT] "Self-hosted runners, Harbor container registry, Nexus/Artifactory artifact storage, and Vault secrets injection are all required [on-premises]. Jenkins published nine security advisories in 2025 — a continuous patching cadence."
— P1_control_plane.md, CP-06 Evidence (citing F48, F58, W08S Theme 1)

[STATISTIC] "Air-gapped delivery requires fully self-contained .airgap bundles with every image and dependency vendored, covering 65,981+ unique Kubernetes environment configurations in the Replicated Compatibility Matrix."
— P1_control_plane.md, CP-06 Evidence (citing F48, F58, W08S Theme 1)

### Scaling Behavior
[FACT] GitOps controllers (Flux, ArgoCD) are cited as sub-linear in FTE scaling — Deutsche Telekom example: 200 clusters managed by 10 FTE with plans to scale to thousands without proportional FTE growth.
Source: P1_control_plane.md, CP-06 Evidence (citing F48, F73 C08, W07S)

### Dependencies
CP-06 owns CI/CD infrastructure machines, registries, and GitOps control loops. Pipeline configuration files (Jenkinsfile, GitHub Actions YAML, Helm values) belong to application logic. CP-07 (deployment mechanics) depends on CP-06 (delivery infrastructure) being operational.
Source: P1_control_plane.md, CP-06 MECE boundary

### Notable Caveats / Technology Transitions
[FACT] "Helm 4 was released at KubeCon 2025."
— P1_control_plane.md, CP-06 Evidence (citing F58)

[FACT] "OLMv0 to v1 migration has no concrete path as of early 2026, creating operator delivery risk for ISVs using the Operator Lifecycle Manager."
— P1_control_plane.md, CP-06 Evidence (citing F58)

---

## CP-07: Deployment Lifecycle, Rollback, and Release Cadence

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-07: Deployment Lifecycle, Rollback, and Release Cadence — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Deployment strategy execution | 1 | 2 | 4 |
| Rollback procedures | 1 | 3 | 5 |
| Version fragmentation management | 1 | 3 | 5 |
| Release cadence / customer coordination | 1 | 2 | 5 |
| **Composite Rating** | **1** | **3** | **5** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-07 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.1–0.35 FTE
[STATISTIC] Managed K8s: 0.35–0.75 FTE
[STATISTIC] On-Premises: 1.5–3.0 FTE

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-07 — Evidence"

[FACT] "All tenants run the same version simultaneously [cloud-native]; rollback occurs in seconds via traffic switching. Release cadence: daily to weekly with no customer coordination."
— P1_control_plane.md, CP-07 Evidence (citing F58, W08S Theme 3)

[STATISTIC] "Elite performers deploy 182x more frequently with 8x lower change failure rates and 127x faster change lead times than low performers (DORA 2024)."
— P1_control_plane.md, CP-07 Evidence (citing F58, W08S Theme 3)

[FACT] "Helm rollback takes minutes but fails on CRD changes, representing a material operational risk for ISVs deploying Kubernetes Operators."
— P1_control_plane.md, CP-07 Evidence (citing F58, F76 Domain 10, F77)

[STATISTIC] "79% of Kubernetes production issues originate from a recent system change, and median MTTR exceeds 50 minutes. (Komodor 2025 Enterprise Kubernetes Report)"
— P1_control_plane.md, CP-07 Evidence (citing F58, F76 Domain 10, F77)

[FACT] "Release cadence enforced to quarterly-to-annual feature releases [on-premises], consistent with SAP's annual S/4HANA on-premises release cycle and Microsoft's annual Configuration Manager cadence."
— P1_control_plane.md, CP-07 Evidence (citing F58, W08S Theme 3)

[FACT] "ISVs routinely carry 3–5 concurrent major versions across their on-premises customer base."
— P1_control_plane.md, CP-07 Evidence (citing F58, W08S Theme 3)

[FACT] "On-premises rollback can consume days and require database restores."
— P1_control_plane.md, CP-07 Evidence (citing F58, W08S Theme 3)

### Scaling Behavior
[FACT] "A critical CVE patch that takes hours to deploy across a cloud-native fleet requires 50 separate customer coordination sequences for an on-premises fleet of 50 customers — notification, scheduling, pre-patch validation, execution, verification, and rollback preparation for each."
— P1_control_plane.md, CP-07 Evidence (citing W08S Theme 2, F59)

CP-07 on-premises workload scales **linearly** with customer count. Cloud-native scales sub-linearly.
Source: P1_control_plane.md, Cross-Subsegment Pattern 2 (citing W08S Theme 5, F59)

### Dependencies
CP-07 depends on CP-06 (CI/CD infrastructure) for delivery. Registry push failures trigger CP-06 work; canary analysis failures triggering manual rollback trigger CP-07 work. Distinct operational domains per MECE boundary.
Source: P1_control_plane.md, CP-07 MECE boundary

### Notable Caveats
[FACT] "Each active version multiplies the compatibility matrix, air-gap bundles, rollback procedures, and compliance audit surfaces."
— P1_control_plane.md, CP-07 Evidence (citing F58, W08S Theme 3)

---

## CP-08: Disaster Recovery and Business Continuity Infrastructure

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-08: Disaster Recovery and Business Continuity Infrastructure — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Backup infrastructure | 2 | 3 | 4 |
| Recovery time objective (RTO) achievement | 2 | 3 | 5 |
| Cross-region / cross-site failover | 2 | 3 | 5 |
| DR testing and runbook maintenance | 2 | 3 | 4 |
| **Composite Rating** | **2** | **3** | **5** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-08 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.25–0.5 FTE
[STATISTIC] Managed K8s: 0.5–1.0 FTE
[STATISTIC] On-Premises: 1.5–2.5 FTE

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-08 — Evidence"

[FACT] "Aurora Global DB provides sub-1-second replication and sub-1-minute promotion. AWS DRS (Disaster Recovery Service) automates cross-region replication. Overall DR difficulty: 2/5 cloud-native."
— P1_control_plane.md, CP-08 Evidence (citing F70)

[FACT] "Velero with Restic integration can reduce RTO by 75% and achieve RPO to seconds through deduplicated, incremental backups across multi-cluster setups."
— P1_control_plane.md, CP-08 Evidence (citing F70, F77 Phase 9)

[STATISTIC] "68% of organizations experienced data loss from disasters at an average cost of $4.5 million per incident."
— P1_control_plane.md, CP-08 Evidence (citing F70, F77 Phase 9)

[STATISTIC] "On-premises hardware costs $50K–$500K+ for large enterprise DR sites."
— P1_control_plane.md, CP-08 Evidence (citing F70)

[STATISTIC] "DR consumes 15–25% of total IT budget [on-premises]."
— P1_control_plane.md, CP-08 Evidence (citing F70)

[STATISTIC] "79% of SaaS providers offer no failover guarantees."
— P1_control_plane.md, CP-08 Evidence (citing F70)

### Scaling Behavior
[FACT] On-premises DR sites require dedicated hardware per site. Hardware and runbook complexity does not amortize across customers — each customer environment requires independent DR validation.
Source: P1_control_plane.md, CP-08 Evidence (citing F70)

### Dependencies
CP-08 boundary is explicitly distinct from database-layer HA (Patroni, Aurora Multi-AZ), which belongs to the Data Plane. A Velero backup schedule configuration triggers CP-08 work; a Patroni failover triggers Data Plane work.
Source: P1_control_plane.md, CP-08 MECE boundary

### Notable Caveats
[STATISTIC] "Ransomware attacks increased 49% in H1 2025, amplifying the stakes of DR gaps."
— P1_control_plane.md, CP-08 Evidence (citing F70)

---

## CP-09: Compliance and Regulatory Automation Infrastructure

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-09: Compliance and Regulatory Automation Infrastructure — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| SOC 2 / ISO 27001 evidence collection | 2 | 3 | 5 |
| HIPAA / FedRAMP control implementation | 2 | 3 | 5 |
| Data sovereignty enforcement | 3 | 2 | 1 |
| EU AI Act / GPAI compliance | 3 | 3 | 4 |
| **Composite Rating** | **2** | **3** | **5** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-09 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.5–1.0 FTE
[STATISTIC] Managed K8s: 1.25–2.0 FTE
[STATISTIC] On-Premises: 2.5–4.0 FTE

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-09 — Evidence"

[FACT] "AWS supports 143 security standards and provides CloudTrail, Security Hub, Config, and GuardDuty for near-automated SOC 2 evidence collection."
— P1_control_plane.md, CP-09 Evidence (citing F67)

[FACT] "Data sovereignty is inverted — on-premises (difficulty 1/5) is easiest because data physically never leaves customer infrastructure, while cloud-native (difficulty 3/5) requires careful region selection, data residency configuration, and contractual mechanisms."
— P1_control_plane.md, CP-09 Evidence (citing F67)

[STATISTIC] "Sovereign cloud market is growing from $154B (2025) to a projected $823B by 2032."
— P1_control_plane.md, CP-09 Evidence (citing F67)

[FACT] "FedRAMP 20x continuous monitoring requires some controls validated minute-by-minute — difficult to achieve on managed K8s without dedicated tooling."
— P1_control_plane.md, CP-09 Evidence (citing F67, F60)

[STATISTIC] "FedRAMP costs $250K–$2M+ for initial authorization [on-premises]."
— P1_control_plane.md, CP-09 Evidence (citing F67, W08S Theme 3)

### Scaling Behavior
[FACT] On-premises carries 50 separate compliance audit surfaces for a 50-customer fleet. Each version multiplies compliance audit surfaces.
Source: P1_control_plane.md, CP-07 Evidence and Cross-Subsegment Pattern 2

### Dependencies
CP-09 boundary is distinct from CP-10 (active threat detection). A SOC 2 audit evidence pipeline failure triggers CP-09 work; a SIEM alert triggers CP-10 work.
Source: P1_control_plane.md, CP-09 MECE boundary

### Notable Caveats / Technology Transitions
[FACT] "EU AI Act GPAI obligations became active August 2025."
— P1_control_plane.md, CP-09 Evidence (citing F67, W08S Theme 3)

[DATA POINT] Data sovereignty dimension in CP-09 is the **single exception** in the entire P1 dataset where on-premises is rated easier than managed K8s, which is easier than cloud-native (1/5 vs. 2/5 vs. 3/5).
Source: P1_control_plane.md, Key Takeaways section

---

## CP-10: Security Operations Infrastructure

### Difficulty Ratings
Source: P1_control_plane.md, "Subsegment CP-10: Security Operations Infrastructure — Difficulty Ratings"

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| SIEM operations | 2 | 3 | 4 |
| IDS/IPS and runtime security | 1 | 3 | 4 |
| Incident response / forensics | 3 | 4 | 5 |
| Vulnerability management | 1 | 2 | 4 |
| **Composite Rating** | **2** | **3** | **5** |

### FTE Ranges
Source: P1_control_plane.md, "Subsegment CP-10 — FTE Estimates"

[STATISTIC] Cloud-Native: 0.25–1.2 FTE
[STATISTIC] Managed K8s: 2.25–4.5 FTE
[STATISTIC] On-Premises: 2.75–5.5 FTE

### Key Operational Characteristics
Source: P1_control_plane.md, "Subsegment CP-10 — Evidence"

[FACT] "Cloud detection rates for Kubernetes attack techniques range from 24% (GCP SCC) to 66% (Azure Defender) — cloud-native agents cannot substitute for K8s-native tooling (Falco, Trivy), meaning managed K8s deployments still require K8s-specific security tools even when using cloud-native SIEM."
— P1_control_plane.md, CP-10 Evidence (citing F71, F55c)

[FACT] "Falco, Kyverno, and Trivy are required for K8s-native runtime security. SIEM at managed K8s difficulty: 3/5. IR/Forensics at managed K8s difficulty: 4/5."
— P1_control_plane.md, CP-10 Evidence (citing F71)

[FACT] "A 24/7 Security Operations Center requires a minimum of 12 FTE and costs $1.5M–$5M annually [on-premises]."
— P1_control_plane.md, CP-10 Evidence (citing F71)

[STATISTIC] "73% of security practitioners cite false positives as the top challenge in on-premises SIEM environments."
— P1_control_plane.md, CP-10 Evidence (citing F71)

[FACT] "On-premises incident response and forensics is rated 5/5 because access must be physically coordinated with customer IT staff, memory acquisition and log preservation requires on-site tools, and the ISV has no direct infrastructure access."
— P1_control_plane.md, CP-10 Evidence (citing F71)

### Scaling Behavior
[STATISTIC] "28% of CVEs are weaponized within one day of disclosure. 77% of enterprises take more than one week to deploy patches."
— P1_control_plane.md, CP-10 Evidence (citing F60, W08S Theme 2)

[FACT] "CISA Known Exploited Vulnerabilities catalog grew 20% year-over-year to 1,484 entries in 2025, with some mandated remediation timelines as short as seven days."
— P1_control_plane.md, CP-10 Evidence (citing F60, W08S Theme 2)

[FACT] Patch delivery velocity gap is most dangerous for on-premises deployments where patch delivery requires customer coordination — scales linearly with customer count.
Source: P1_control_plane.md, CP-10 Evidence (citing F60, W08S Theme 2)

### Dependencies
CP-10 is downstream of CP-03 (identity policy enforcement), CP-04 (certificate lifecycle), and CP-09 (compliance evidence). A Falco runtime alert triggering incident response triggers CP-10 work; a Vault secret rotation triggers CP-04 work; a SOC 2 scheduled review triggers CP-09 work.
Source: P1_control_plane.md, CP-10 MECE boundary

### Notable Caveats
[FACT] CP-03 + CP-04 + CP-10 together require "8.0–15.25 FTE on-premises — representing 32–40% of total Control Plane on-premises FTE."
— P1_control_plane.md, Cross-Subsegment Pattern 4 (citing F46, F47, F71, W06S Theme 2)

---

## Summary Table: All Ratings and FTE Ranges

Source: P1_control_plane.md, "Summary Difficulty Matrix" and "Aggregate FTE Ranges" sections.

### Composite Difficulty Ratings

| ID | Subsegment | CN Rating | MK8s Rating | OP Rating | Primary Sources |
|:---:|---|:---:|:---:|:---:|---|
| CP-01 | Kubernetes Cluster Lifecycle Management | 1 | 3 | 5 | F52, F53, W07S |
| CP-02 | Network Fabric, Ingress, and Service Mesh | 1 | 3 | 5 | F40, F55, F76 |
| CP-03 | Identity, Access Management, and RBAC | 1 | 2 | 4 | F46, F55c, F73 |
| CP-04 | Secrets Management, Certificate Lifecycle, and PKI | 1 | 2 | 5 | F47, F55c, F76 |
| CP-05 | Observability Infrastructure (Metrics, Logs, Traces) | 1 | 3 | 4 | F49, F50, F51, F55d |
| CP-06 | CI/CD Pipeline Infrastructure and GitOps | 1 | 3 | 4 | F48, F58, W08S |
| CP-07 | Deployment Lifecycle, Rollback, and Release Cadence | 1 | 3 | 5 | F58, F59, F60, W08S |
| CP-08 | Disaster Recovery and Business Continuity Infrastructure | 2 | 3 | 5 | F70, F77 |
| CP-09 | Compliance and Regulatory Automation Infrastructure | 2 | 3 | 5 | F67, F60 |
| CP-10 | Security Operations Infrastructure | 2 | 3 | 5 | F71, F55c, F60 |
| | **Aggregate Score** | **13** | **28** | **47** | |
| | **Average Difficulty** | **1.3** | **2.8** | **4.7** | |

### FTE Ranges (mid-size ISV, 50 enterprise customers, 3–5 clusters)

| ID | Subsegment | CN FTE | MK8s FTE | OP FTE |
|:---:|---|---|---|---|
| CP-01 | Cluster Lifecycle | 0.0–0.5 | 1.0–2.5 | 3.0–6.0 |
| CP-02 | Network / Ingress / Mesh | 0.1–0.7 | 0.75–1.75 | 1.75–3.5 |
| CP-03 | IAM / RBAC | 0.3–0.8 | 1.65–2.65 | 2.75–4.75 |
| CP-04 | Secrets / Certs / PKI | 0.4–0.85 | 0.4–0.85 | 2.5–5.0 |
| CP-05 | Observability Infrastructure | 0.55–1.0 | 1.25–2.0 | 4.6–7.0 |
| CP-06 | CI/CD Infrastructure / GitOps | 0.3–0.4 | 1.3–1.9 | 2.0–3.25 |
| CP-07 | Deploy Lifecycle / Rollback | 0.1–0.35 | 0.35–0.75 | 1.5–3.0 |
| CP-08 | Disaster Recovery | 0.25–0.5 | 0.5–1.0 | 1.5–2.5 |
| CP-09 | Compliance Automation | 0.5–1.0 | 1.25–2.0 | 2.5–4.0 |
| CP-10 | Security Operations | 0.25–1.2 | 2.25–4.5 | 2.75–5.5 |
| | **Total (raw sum)** | **2.75–7.3** | **10.75–19.9** | **24.85–44.5** |
| | **Deduplicated estimate** | **~2.5–6.5** | **~9–16** | **~20–38** |

[FACT] "Deduplication note: Raw sums include partial scope overlap between CP-03 (IAM), CP-04 (Secrets/Certs), and CP-10 (SecOps) due to mTLS, workload identity, and security monitoring boundaries. Deduplicated estimates remove approximately 1.0–2.0 FTE from the security cluster per tier."
— P1_control_plane.md, Summary FTE table deduplication note (citing W06S)

### Aggregate Difficulty Ratios
Source: P1_control_plane.md, "Key Takeaways" section

[STATISTIC] Difficulty ratio (1–5 scale): 1.0 : 2.2 : 3.6 (Cloud-Native : Managed K8s : On-Premises)
[STATISTIC] Difficulty averages: 1.3 : 2.8 : 4.7 (Cloud-Native : Managed K8s : On-Premises)
[STATISTIC] FTE ratio (approximate): 1 : 3 : 8 (Cloud-Native : Managed K8s : On-Premises)

---

## Cross-Subsegment Dependency Map

Source: P1_control_plane.md, MECE boundary sections for each subsegment and Cross-Subsegment Patterns section.

| Dependency | Direction | Nature |
|---|---|---|
| CP-01 → CP-02 through CP-10 | Foundational | Cluster substrate required before all other CP components can operate |
| CP-03 → CP-04 | Identity policy governs secret access | Role binding determines who accesses which secret |
| CP-04 → CP-02 | Certificate assets establish mTLS | CP-04 issues certificates CP-02 uses for mTLS enforcement |
| CP-06 → CP-07 | Infrastructure enables mechanics | Registry and runner availability precondition for deployment execution |
| CP-09 → CP-10 | Compliance policy informs SecOps | Audit requirements define threat detection thresholds |
| CP-03 + CP-04 + CP-10 | Security cluster FTE overlap | 1.0–2.0 FTE deduplication required across trio |

---

## Mandatory Technology Migrations Catalog (2025–2026)

Source: P1_control_plane.md, Cross-Subsegment Pattern 3 (citing W06S Theme 3, F73 C03, F51, F47, F46).

| Migration | Affected Subsegment | Deadline | Scope |
|---|---|---|---|
| Ingress NGINX EOL | CP-02 | March 2026 (maintenance ends) | Managed K8s and On-Premises |
| Jaeger v1 deprecated | CP-05 | January 2026 | On-Premises (primarily) |
| FIPS 140-2 certificate expiry | CP-04 | September 2026 | All tiers with HSM or FIPS certs |
| Let's Encrypt 45-day cert validity | CP-04 | May 13, 2026 | All tiers |
| OPA maintainer uncertainty (Apple acquisition) | CP-03 | August 2025 (event date) | Managed K8s and On-Premises |
| GKE Identity Service deprecation | CP-03 | July 1, 2025 (new orgs) | Managed K8s (GKE) |
| MinIO archived | CP-05 | Early 2026 | On-Premises |

[FACT] "Each migration consumes FTE from the same limited platform engineering pool. Cloud-native ISVs are largely shielded: providers absorb networking migrations (CP-02), certificate rotation (CP-04), and monitoring backend changes (CP-05) without ISV action."
— P1_control_plane.md, Cross-Subsegment Pattern 3

---

## Sources

**Primary Source File:**
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md` — Analysis Date 2026-02-19

**Source Files Referenced Within P1_control_plane.md (as cited in Evidence sections):**

| Cited File | Wave | Subsegments Supported |
|---|---|---|
| F40 — On-Prem Networking | Wave 6 | CP-02 |
| F46 — On-Prem IAM/Identity | Wave 6 | CP-03 |
| F47 — On-Prem Secrets/Certs | Wave 6 | CP-04 |
| F48 — On-Prem CI/CD | Wave 6 | CP-06 |
| F49 — On-Prem Logging | Wave 6 | CP-05 |
| F50 — On-Prem Monitoring | Wave 6 | CP-05 |
| F51 — On-Prem Tracing | Wave 6 | CP-05 |
| F52 — Managed K8s Platforms | Wave 7 | CP-01 |
| F53 — Portable K8s ISV Delivery | Wave 7 | CP-01, CP-06 |
| F55 — K8s Service Mesh | Wave 7 | CP-02 |
| F55c — K8s Security Posture | Wave 7 | CP-03, CP-04, CP-10 |
| F55d — K8s Observability Stack | Wave 7 | CP-05 |
| F58 — Deploy/Release Differences | Wave 8 | CP-07 |
| F59 — Operate/Monitor Differences | Wave 8 | CP-07, CP-10 |
| F60 — Update/Patch/Scale | Wave 8 | CP-07, CP-09, CP-10 |
| F67 — Compliance/Regulatory | Wave 10 | CP-09 |
| F70 — Disaster Recovery/BC | Wave 10 | CP-08 |
| F71 — On-Prem Security Ops | Wave 10 | CP-10 |
| F73 — MECE ISV Dev Responsibility | Wave 11 | Boundary enforcement (all) |
| F76 — MECE Failure Domain | Wave 11 | CP-02, CP-04, CP-07 |
| F77 — MECE Runtime Lifecycle | Wave 11 | CP-06, CP-08 |
| W06S — On-Prem Infrastructure Synthesis | Synthesis | CP-01, CP-03, CP-04, CP-10 |
| W07S — Managed K8s Synthesis | Synthesis | CP-01, CP-02, CP-05, CP-06 |
| W08S — SDLC Differences Synthesis | Synthesis | CP-07, CP-09 |
