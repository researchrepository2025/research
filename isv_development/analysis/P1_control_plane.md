# P1: Control Plane — MECE Subsegment Analysis
## ISV Deployment Model Comparison: Cloud-Native vs. Managed K8s vs. On-Premises

**Analysis Date:** 2026-02-19
**Analyst:** Strategic Technology Research
**Scope:** Control Plane — Plane 1 of 4 (excludes Application Logic, Data Plane, AI Model Plane)
**Deployment Tiers:** Cloud-Native (AWS/Azure/GCP fully managed) | Managed K8s (EKS/AKS/GKE) | On-Premises (kubeadm/Rancher/OpenShift)

---

## Scope Definition and Boundary Enforcement

The Control Plane is the totality of infrastructure and platform services that govern how containerized workloads are scheduled, secured, connected, observed, and updated — but not what those workloads compute. The boundary is operational: the Control Plane ends where application business logic begins.

**In scope:** Kubernetes cluster lifecycle, networking and ingress, identity and access management, secrets and certificate management, observability infrastructure (not instrumentation code), CI/CD pipeline infrastructure, disaster recovery and backup infrastructure, security operations, compliance automation infrastructure.

**Explicitly excluded:**
- Application Logic Plane: business logic, ORM layers, background job code, AI orchestration framework code (covered in F73)
- Data Plane: PostgreSQL, Redis, Kafka, vector databases, object storage (covered in waves 5–6, F41–F45)
- AI Model Plane: LLM inference serving, GPU scheduling, RAG pipeline architecture (covered in wave 5, F35–F38)

**Why this boundary holds:** The Control Plane components identified below share a common organizational owner (platform/SRE/DevOps teams), a common change driver (infrastructure events rather than product feature requests), and a common failure mode (infrastructure unavailability propagates to all workloads, regardless of what those workloads compute). Application logic components share none of these properties (F73, Section 1.1).

---

## MECE Validation

The ten subsegments below are **mutually exclusive** because each is bounded by a distinct operational actor, a distinct infrastructure concern, and a distinct set of failure modes. No two subsegments share all three. They are **collectively exhaustive** because together they cover every infrastructure pathway a containerized workload traverses from cluster creation through runtime: the cluster must exist (CP-01), workloads must be scheduled and reach each other (CP-02, CP-03), workloads must authenticate and protect secrets (CP-04, CP-05), workloads must be observed and delivered (CP-06, CP-07), data must survive failures (CP-08), the environment must remain compliant (CP-09), and security threats must be detected and contained (CP-10). No production infrastructure event falls outside this set.

---

## Difficulty Scale Reference

| Rating | Label | Operational Meaning | FTE Indicative |
|:---:|---|---|---|
| 1 | Trivial | Fully managed by provider; near-zero operator action | < 0.1 FTE |
| 2 | Low | Minimal configuration required; provider absorbs most operations | 0.1–0.3 FTE |
| 3 | Moderate | Requires active configuration, monitoring, and periodic tuning | 0.3–0.75 FTE |
| 4 | High | Significant ongoing operational effort; specialized knowledge required | 0.75–1.5 FTE |
| 5 | Extreme | Constant attention required; high failure risk without dedicated team; 1.0+ FTE per subsegment | 1.0+ FTE |

---

## Subsegment CP-01: Kubernetes Cluster Lifecycle Management

**Definition:** Provisioning, upgrading, scaling, and decommissioning of the Kubernetes control plane and worker node pools. Encompasses API server, etcd, scheduler, controller manager, node pool management, add-on lifecycle, and cluster version currency.

**MECE boundary:** CP-01 owns the cluster infrastructure itself — the substrate on which all other control plane components run. It does not own the workloads that run inside the cluster (application logic) or the network fabric those workloads use to communicate (CP-02). A Kubernetes version bump triggers CP-01 work; a network policy change triggers CP-02 work. The change drivers are structurally distinct.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Control plane operations | 1 | 1 | 5 |
| Node pool lifecycle | 2 | 2 | 5 |
| Add-on ecosystem management | 1 | 3 | 5 |
| Version currency / upgrade cadence | 1 | 3 | 5 |
| **Composite Rating** | **1** | **3** | **5** |

### Evidence

Cloud-Native: Provider manages the API server, etcd, scheduler, and controller manager entirely. EKS costs $0.10/hour ($73/month per cluster); AKS offers a free control plane. Add-ons (CoreDNS, VPC-CNI, kube-proxy) are managed by the provider.
(Source: F52 — Managed K8s Platforms; W07S)

Managed K8s: The control plane is abstracted, but ISVs must manage at least a dozen add-on components — ingress controllers, RBAC policies, storage classes, network policies, secrets management — requiring 1.0–2.5 FTE for base platform operations across 3–5 clusters serving 50 enterprise customers.
(Source: W07S, Theme 1; F52)

The Ingress NGINX Controller — powering approximately 41% of internet-facing Kubernetes clusters — was officially retired in November 2025, with best-effort maintenance ending March 2026, forcing mandatory migration to the Kubernetes Gateway API. This represents unplanned 0.3–0.6 FTE of platform work for managed K8s ISVs in 2026 regardless of product roadmap priority.
(Source: F73, C03 section; F40, Section on ingress EOL)

Kubernetes releases approximately 3 minor versions per year with 12–14 month support windows. On-premises ISVs must upgrade clusters themselves, coordinate node draining across all customer environments, and validate add-on compatibility. AKS LTS extends Kubernetes version support to 24 months — a meaningful reduction in upgrade frequency pressure for managed K8s deployments.
(Source: F52; W07S, Theme 1)

On-Premises: Full responsibility for all control plane components including etcd backup, API server HA, and control plane node replacement. VMware post-Broadcom-acquisition price increases of 8–15x eliminate the previously dominant hypervisor path. SUSE Rancher CPU-based pricing caused 4–9x cost increases in 2025, driving enterprise migration away from previously stable on-premises Kubernetes distribution choices.
(Source: W06S, Theme 1; W07S, Theme 5; F53)

**FTE Estimates (mid-size ISV, 50 customers, 3–5 clusters):**
- Cloud-Native: 0.0–0.5 FTE
- Managed K8s: 1.0–2.5 FTE
- On-Premises: 3.0–6.0 FTE (including upgrade coordination per customer)

---

## Subsegment CP-02: Network Fabric, Ingress, and Service Mesh

**Definition:** All networking infrastructure governing how traffic enters the cluster (ingress/load balancer), how services discover and reach each other (CNI, DNS, service mesh), and how network security is enforced (NetworkPolicy, mTLS). Covers Layer 3–7 of the network stack within and adjacent to the cluster.

**MECE boundary:** CP-02 owns the network fabric as infrastructure. It does not own API Gateway configuration logic driven by application routing rules (that falls in application logic, F73 C03 for application-layer concerns), nor does it own the TLS certificate lifecycle (CP-05). A CNI misconfiguration triggers CP-02 work; a certificate expiry triggers CP-05 work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Load balancer / ingress provisioning | 1 | 2 | 5 |
| Network segmentation / policy enforcement | 1 | 3 | 5 |
| DNS (internal and external) | 1 | 2 | 4 |
| Service mesh (if adopted) | 3 | 4 | 5 |
| **Composite Rating** | **1** | **3** | **5** |

### Evidence

Cloud-Native: AWS ALB, Azure Application Gateway, and GCP Cloud Load Balancing are fully managed with SLAs. Route 53, Azure DNS, and Cloud DNS are fully managed with 100% SLA targets. DNS failures are uniquely high blast-radius because resolution is a prerequisite for nearly every service-to-service call.
(Source: F76, Domain 2)

Managed K8s: CoreDNS is self-managed; scaling, HPA configuration, and Linux conntrack tuning required. A 2025 EKS incident traced a Linux conntrack management bug in CoreDNS that caused cascading DNS timeouts across all dependent services. CoreDNS v1.11.3 showed intermittent resolution failures affecting both internal and external names.
(Source: F76, Domain 2)

On-Premises networking requires total FTE of 1.75–3.5 (mid-size ISV) for HAProxy, Consul, CoreDNS, Calico/Cilium NetworkPolicy, and manual VLAN segmentation. Network segmentation difficulty is rated 5/5 on-premises. Physical switch failures propagate until redundant paths activate; ECMP and spanning tree convergence times can reach minutes.
(Source: F40; F76, Domain 1)

Service mesh adoption declined from 50% (2023) to 42% (2024) to approximately 8% developer-level adoption by Q3 2025 — reflecting a market correction where sidecar complexity outweighed benefits. Istio sidecar mode adds 166% latency overhead at 3,200 RPS; Istio Ambient mode adds only 8% latency; Linkerd requires 1/8th to 1/9th the resources of Istio. Mesh FTE on-premises: 1.0–2.0 FTE; managed K8s: 0.5–1.0 FTE; cloud-native: 0.25–0.5 FTE.
(Source: F55; W07S, Theme 5)

**FTE Estimates:**
- Cloud-Native: 0.1–0.7 FTE
- Managed K8s: 0.75–1.75 FTE (add 0.5–1.0 FTE if service mesh adopted)
- On-Premises: 1.75–3.5 FTE (add 1.0–2.0 FTE if service mesh adopted)

---

## Subsegment CP-03: Identity, Access Management, and RBAC

**Definition:** All infrastructure governing who can access what — Kubernetes RBAC, cluster-level and namespace-level role bindings, integration with external identity providers (OIDC, SAML, Active Directory), workload identity (service accounts, IRSA, Workload Identity), and policy engines (OPA/Gatekeeper, Kyverno, Cedar).

**MECE boundary:** CP-03 owns the identity infrastructure. It does not own the application-layer authentication code (that is application logic, F73 C01) or the certificate assets used to establish mTLS trust (CP-05). A role binding change triggers CP-03 work; a certificate rotation triggers CP-05 work; a login flow SDK change triggers application logic work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Identity provider operations | 1 | 2 | 4 |
| RBAC / policy engine management | 1 | 3 | 5 |
| Workload identity (service accounts) | 1 | 2 | 4 |
| Directory services (AD/LDAP) | 1 | 2 | 4 |
| **Composite Rating** | **1** | **2** | **4** |

### Evidence

Cloud-Native: AWS IAM roles for service accounts (IRSA), GKE Workload Identity, and Azure Workload Identity are managed by the provider. Cloud-native difficulty rated 1/5 for directory and 1/5 for RBAC. Total FTE: 0.30–0.80.
(Source: F46; F55c)

Managed K8s: OIDC integration requires configuration; short-lived token rotation is manual or via external-secrets. GKE deprecated Identity Service for GKE for new organizations as of July 1, 2025, mandating migration to Workforce Identity Federation. Total FTE: 1.65–2.65.
(Source: F73, C01; F46)

On-Premises: Self-hosted Keycloak, Authentik, or Active Directory requires HA configuration, patch lifecycle, and dedicated identity expertise. IAM is described as "a product line, not an infrastructure dependency" with seven sub-domains each rated 3–4/5 difficulty. Total IAM FTE on-premises: 2.75–4.75.
(Source: F46; W06S, Theme 2)

OPA uncertainty risk: Apple's acquisition of the OPA maintainer team in August 2025 creates a policy-engine risk for ISVs dependent on OPA/Gatekeeper. Kyverno is the primary alternative with a stable CNCF governance path.
(Source: F46; W06S, Theme 2)

Kubernetes RBAC / IAM on-premises is rated 5/5 difficulty; cloud-native is rated 1/5.
(Source: F55c)

**FTE Estimates:**
- Cloud-Native: 0.30–0.80 FTE
- Managed K8s: 1.65–2.65 FTE
- On-Premises: 2.75–4.75 FTE

---

## Subsegment CP-04: Secrets Management, Certificate Lifecycle, and PKI

**Definition:** All infrastructure that protects sensitive configuration data — secret storage engines (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault), certificate authorities, PKI infrastructure, HSMs, encryption at rest (LUKS, TDE), and automated secret/certificate rotation pipelines.

**MECE boundary:** CP-04 owns the secrets and certificate infrastructure. It does not own the identity policy that governs who accesses which secret (CP-03) or the application code that consumes secrets at runtime (application logic). A certificate expiry or secret rotation event triggers CP-04 work; an RBAC policy change triggers CP-03 work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Secret store operations | 1 | 2 | 5 |
| Certificate authority / PKI | 1 | 2 | 4 |
| HSM integration | 2 | 3 | 5 |
| Rotation automation | 1 | 2 | 4 |
| **Composite Rating** | **1** | **2** | **5** |

### Evidence

Cloud-Native: AWS Secrets Manager, Azure Key Vault, and GCP Secret Manager with automatic rotation. ACM (AWS), Managed Certificates (GCP), and App Gateway (Azure) auto-renew TLS certificates with zero operator action. Total FTE: 0.4–0.85.
(Source: F47; F76, Domain 3)

Managed K8s: cert-manager automates TLS certificate renewal; requires initial installation, ClusterIssuer configuration, and renewal monitoring. External Secrets Operator bridges managed secret stores to Kubernetes Secrets. Native Kubernetes Secrets are base64-encoded rather than encrypted — every production deployment must explicitly enable etcd encryption or use External Secrets Operator. Total FTE: 0.4–0.85 (similar to cloud-native at the managed K8s tier as this domain benefits most from external secret store integration).
(Source: F55c; F76, Domain 3; W07S, Theme 4)

On-Premises: HashiCorp Vault minimum 5-node Raft cluster. FIPS 140-2 certificate validity expires September 2026 — HSM firmware and Vault seal configurations must transition to FIPS 140-3 before that date. HSM hardware costs $5K–$50K per unit. Let's Encrypt announced in December 2025 that certificate validity will decrease to 45 days on May 13, 2026 — increasing rotation frequency requirements for all tiers. Total on-premises FTE: 2.5–5.0.
(Source: F47; W06S, Theme 2; F76, Domain 3)

**FTE Estimates:**
- Cloud-Native: 0.4–0.85 FTE
- Managed K8s: 0.4–0.85 FTE
- On-Premises: 2.5–5.0 FTE

---

## Subsegment CP-05: Observability Infrastructure (Metrics, Logs, Traces)

**Definition:** The infrastructure layer of the observability stack — Prometheus/Thanos/Mimir for metrics, ELK/Loki for logs, Jaeger/Tempo for traces, and Grafana for visualization. This subsegment covers infrastructure operations only: storage management, retention, cardinality governance, backend scalability, and alert routing. It explicitly excludes application-layer instrumentation code (OpenTelemetry SDK wiring, which is application logic per F73 C07).

**MECE boundary:** CP-05 owns the observability backend infrastructure. Application instrumentation code (spans, metrics, logs emitted from application code) is application logic. A Prometheus storage backend upgrade triggers CP-05 work; adding an OTel span to a handler function triggers application logic work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Metrics backend (Prometheus/Thanos/Mimir) | 1 | 3 | 4 |
| Logging backend (ELK/Loki) | 1 | 3 | 4 |
| Tracing backend (Jaeger/Tempo) | 1 | 3 | 5 |
| Storage management and retention | 1 | 2 | 5 |
| Cardinality governance | 1 | 3 | 4 |
| **Composite Rating** | **1** | **3** | **4** |

### Evidence

Cloud-Native: CloudWatch, Azure Monitor, and Google Cloud Logging/Monitoring are fully managed. Total FTE: logging 0.05–0.1; monitoring 0.3–0.6; tracing 0.2–0.3. Combined: approximately 0.55–1.0 FTE.
(Source: F49; F50; F51; F55d)

Managed K8s: The kube-prometheus-stack (Prometheus Operator, Grafana, Alertmanager) consumes 15–35 GB of cluster RAM before any application workloads are monitored. Recommended hybrid approach: cloud-managed Prometheus for metrics, self-managed Loki/Tempo for logs and traces — introducing split-stack operational complexity. Total FTE: 1.25–2.0.
(Source: F55d; W07S, Theme 4)

On-Premises: A 100-node cluster can generate 500,000+ active Prometheus time series at approximately 3 KB RAM per series. AWS Managed Prometheus at 1M samples/sec costs approximately $47K/month versus self-hosted approximately $6K/month (7.8x cost differential), creating strong economic pressure to self-host at high ingest volumes. Self-hosted Loki at 100 GB/day costs approximately $300/month versus CloudWatch $1,665/month (75–90% cost reduction). The cost crossover point for logging sits at 50–100 GB/day — below this threshold, managed services are cost-competitive.
(Source: F49; F50; W06S, Theme 4)

Jaeger v1 was deprecated January 2026 — migration to v2 (OTel Collector-based) is required. MinIO entered maintenance mode late 2025 and was archived by early 2026, affecting on-premises tracing storage backends. Combined on-premises FTE for observability: 4.6–7.0 (logging 1.5–2.0 + monitoring 1.5–2.5 + tracing 1.6–2.5).
(Source: F51; W06S, Theme 3 and Theme 4)

OpenTelemetry consistent probability sampling specification was adopted October 2025. OpenTelemetry is the second-highest-velocity CNCF project with 24,000+ contributors as of the 2025 CNCF Annual Survey, confirming vendor-neutral signal emission as the standard path forward for all tiers.
(Source: F51; F77)

**FTE Estimates (combined metrics + logs + traces):**
- Cloud-Native: 0.55–1.0 FTE
- Managed K8s: 1.25–2.0 FTE
- On-Premises: 4.6–7.0 FTE

---

## Subsegment CP-06: CI/CD Pipeline Infrastructure and GitOps

**Definition:** The infrastructure layer of build and deployment pipelines — CI runner capacity, container registry operations (Harbor, ECR, GCR, ACR), artifact signing and provenance (Sigstore/cosign), GitOps controllers (ArgoCD, Flux), and air-gap bundle delivery for on-premises customers. This covers pipeline infrastructure, not pipeline configuration YAML (the latter is application logic per F73 C08).

**MECE boundary:** CP-06 owns the CI/CD infrastructure machines, registries, and GitOps control loops. Pipeline configuration files (Jenkinsfile, GitHub Actions YAML, Helm chart values) belong to application logic. An ArgoCD controller upgrade triggers CP-06 work; a new pipeline stage for a specific service triggers application logic work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| CI runner infrastructure | 1 | 2 | 4 |
| Container registry operations | 1 | 2 | 3 |
| GitOps controller operations | 1 | 2 | 3 |
| Air-gap bundle delivery | N/A | 3 | 5 |
| Artifact signing / supply chain | 2 | 3 | 4 |
| **Composite Rating** | **1** | **3** | **4** |

### Evidence

Cloud-Native: GitHub Actions, AWS CodePipeline, Azure DevOps, and Google Cloud Build eliminate pipeline infrastructure management. ECR, GCR, and ACR handle registry operations. Total FTE: approximately 0.3–0.4.
(Source: F48; F73 C08)

Managed K8s: Argo CD is adopted in 60% of Kubernetes clusters per the 2025 CNCF End User Survey. Flux manages approximately 200 Kubernetes clusters at Deutsche Telekom with just 10 full-time engineers, with plans to scale to thousands of clusters without proportional FTE growth. Total managed K8s FTE: 1.3–1.9.
(Source: F48; F73 C08; W07S)

On-Premises: Self-hosted runners, Harbor container registry, Nexus/Artifactory artifact storage, and Vault secrets injection are all required. Jenkins published nine security advisories in 2025 — a continuous patching cadence. Air-gapped delivery requires fully self-contained .airgap bundles with every image and dependency vendored, covering 65,981+ unique Kubernetes environment configurations in the Replicated Compatibility Matrix. Total on-premises FTE: 2.0–3.25.
(Source: F48; F58; W08S, Theme 1)

Helm 4 was released at KubeCon 2025. OLMv0 to v1 migration has no concrete path as of early 2026, creating operator delivery risk for ISVs using the Operator Lifecycle Manager.
(Source: F58)

**FTE Estimates:**
- Cloud-Native: 0.3–0.4 FTE
- Managed K8s: 1.3–1.9 FTE
- On-Premises: 2.0–3.25 FTE

---

## Subsegment CP-07: Deployment Lifecycle, Rollback, and Release Cadence

**Definition:** The operational mechanics of moving new software versions into production and recovering from failed deployments — rolling updates, blue-green deployments, canary analysis, traffic shifting, rollback procedures, and version fragmentation management across a multi-customer fleet. Distinct from CI/CD infrastructure (CP-06) which concerns the machines and tools; this subsegment concerns the operational procedures applied per-deployment and per-customer.

**MECE boundary:** CP-07 owns deployment mechanics and rollback execution. CI/CD infrastructure (runners, registries) belongs to CP-06. Application architecture decisions about deployment patterns belong to application logic. A canary analysis failure requiring manual rollback triggers CP-07 work; a registry push failure triggers CP-06 work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Deployment strategy execution | 1 | 2 | 4 |
| Rollback procedures | 1 | 3 | 5 |
| Version fragmentation management | 1 | 3 | 5 |
| Release cadence / customer coordination | 1 | 2 | 5 |
| **Composite Rating** | **1** | **3** | **5** |

### Evidence

Cloud-Native: All tenants run the same version simultaneously; rollback occurs in seconds via traffic switching. Release cadence: daily to weekly with no customer coordination. Elite performers deploy 182x more frequently with 8x lower change failure rates and 127x faster change lead times than low performers (DORA 2024).
(Source: F58; W08S, Theme 3)

Managed K8s: Argo Rollouts and Flux provide progressive delivery; Helm rollback takes minutes but fails on CRD changes, representing a material operational risk for ISVs deploying Kubernetes Operators. Release cadence: bi-weekly to monthly for customer-deployed clusters. The Komodor 2025 Enterprise Kubernetes Report found that 79% of Kubernetes production issues originate from a recent system change, and median MTTR exceeds 50 minutes.
(Source: F58; F76, Domain 10; F77)

On-Premises: Release cadence enforced to quarterly-to-annual feature releases, consistent with SAP's annual S/4HANA on-premises release cycle and Microsoft's annual Configuration Manager cadence. ISVs routinely carry 3–5 concurrent major versions across their on-premises customer base. Each active version multiplies the compatibility matrix, air-gap bundles, rollback procedures, and compliance audit surfaces. On-premises rollback can consume days and require database restores.
(Source: F58; W08S, Theme 3)

A critical CVE patch that takes hours to deploy across a cloud-native fleet requires 50 separate customer coordination sequences for an on-premises fleet of 50 customers — notification, scheduling, pre-patch validation, execution, verification, and rollback preparation for each.
(Source: W08S, Theme 2; F59)

**FTE Estimates:**
- Cloud-Native: 0.1–0.35 FTE
- Managed K8s: 0.35–0.75 FTE
- On-Premises: 1.5–3.0 FTE

---

## Subsegment CP-08: Disaster Recovery and Business Continuity Infrastructure

**Definition:** All infrastructure and procedures for recovering from major failures — backup systems (Velero, Kasten K10), cross-region replication, RPO/RTO target definition and testing, failover automation, and business continuity runbooks. Covers infrastructure-level recovery; does not cover application-layer data migration logic.

**MECE boundary:** CP-08 owns the backup and recovery infrastructure and procedures. Database infrastructure HA and replication (Patroni, Aurora Multi-AZ) belongs to the Data Plane. Application-layer data migration code belongs to application logic. A Velero backup schedule configuration triggers CP-08 work; a Patroni failover triggers Data Plane work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| Backup infrastructure | 2 | 3 | 4 |
| Recovery time objective (RTO) achievement | 2 | 3 | 5 |
| Cross-region / cross-site failover | 2 | 3 | 5 |
| DR testing and runbook maintenance | 2 | 3 | 4 |
| **Composite Rating** | **2** | **3** | **5** |

### Evidence

Cloud-Native: Aurora Global DB provides sub-1-second replication and sub-1-minute promotion. AWS DRS (Disaster Recovery Service) automates cross-region replication. Overall DR difficulty: 2/5 cloud-native. Total FTE: 0.25–0.5.
(Source: F70)

Managed K8s: Velero with Restic integration can reduce RTO by 75% and achieve RPO to seconds through deduplicated, incremental backups across multi-cluster setups. CSI volume snapshot classes, PVC backup, and cross-cluster restore require active configuration. 68% of organizations experienced data loss from disasters at an average cost of $4.5 million per incident. Total FTE: 0.5–1.0.
(Source: F70; F77, Phase 9)

On-Premises: On-premises hardware costs $50K–$500K+ for large enterprise DR sites. Ransomware attacks increased 49% in H1 2025, amplifying the stakes of DR gaps. DR consumes 15–25% of total IT budget. 79% of SaaS providers offer no failover guarantees. Overall DR difficulty: 5/5 on-premises. Total on-premises FTE: 1.5–2.5.
(Source: F70)

**FTE Estimates:**
- Cloud-Native: 0.25–0.5 FTE
- Managed K8s: 0.5–1.0 FTE
- On-Premises: 1.5–2.5 FTE

---

## Subsegment CP-09: Compliance and Regulatory Automation Infrastructure

**Definition:** Infrastructure and tooling that collect, maintain, and demonstrate compliance evidence across regulatory frameworks — SOC 2, HIPAA, FedRAMP 20x, ISO 27001, GDPR, EU AI Act. Covers continuous control monitoring platforms, audit evidence collection pipelines, compliance-as-code tooling (OSCAL), and data sovereignty enforcement mechanisms. Does not cover the compliance policies themselves (which are business requirements) or application-layer data handling logic.

**MECE boundary:** CP-09 owns compliance automation infrastructure. Application-layer data privacy code (data masking, consent management) belongs to application logic. The Security Operations Center infrastructure for threat detection belongs to CP-10. A SOC 2 audit evidence pipeline failure triggers CP-09 work; a SIEM alert triggers CP-10 work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| SOC 2 / ISO 27001 evidence collection | 2 | 3 | 5 |
| HIPAA / FedRAMP control implementation | 2 | 3 | 5 |
| Data sovereignty enforcement | 3 | 2 | 1 |
| EU AI Act / GPAI compliance | 3 | 3 | 4 |
| **Composite Rating** | **2** | **3** | **5** |

### Evidence

Cloud-Native: AWS supports 143 security standards and provides CloudTrail, Security Hub, Config, and GuardDuty for near-automated SOC 2 evidence collection. Cloud-native providers absorb the majority of infrastructure-level controls, reducing ISV compliance burden significantly. Total FTE: 0.5–1.0.
(Source: F67)

Note: Data sovereignty is inverted — on-premises (difficulty 1/5) is easiest because data physically never leaves customer infrastructure, while cloud-native (difficulty 3/5) requires careful region selection, data residency configuration, and contractual mechanisms. Sovereign cloud market is growing from $154B (2025) to a projected $823B by 2032.
(Source: F67)

Managed K8s: SOC 2 compliance for private clouds in 2025 increasingly integrates AI automation and DevSecOps tooling. FedRAMP 20x continuous monitoring requires some controls validated minute-by-minute — difficult to achieve on managed K8s without dedicated tooling. Total FTE: 1.25–2.0.
(Source: F67; F60)

On-Premises: On-premises carries the highest compliance burden because control evidence must be collected manually or via custom automation, and the ISV is responsible for demonstrating control implementation that cloud providers certify on behalf of cloud tenants. FedRAMP costs $250K–$2M+ for initial authorization. EU AI Act GPAI obligations became active August 2025. Total on-premises FTE: 2.5–4.0.
(Source: F67; W08S, Theme 3)

**FTE Estimates:**
- Cloud-Native: 0.5–1.0 FTE
- Managed K8s: 1.25–2.0 FTE
- On-Premises: 2.5–4.0 FTE

---

## Subsegment CP-10: Security Operations Infrastructure

**Definition:** The infrastructure for continuous threat detection, incident response, forensic capability, and runtime security — SIEM platforms (Wazuh, Splunk, ELK Security), IDS/IPS (Suricata, Falco), vulnerability scanning (Trivy, Grype), penetration test remediation tracking, and SOC operational tooling. Covers the security monitoring infrastructure, not the security policies enforced at provisioning time (CP-03, CP-04, CP-09).

**MECE boundary:** CP-10 owns active threat detection and response infrastructure. Identity policy enforcement belongs to CP-03. Certificate lifecycle belongs to CP-04. Compliance evidence collection belongs to CP-09. A Falco runtime alert triggering incident response triggers CP-10 work; a Vault secret rotation triggers CP-04 work; a SOC 2 audit scheduled review triggers CP-09 work.

### Difficulty Ratings

| Dimension | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| SIEM operations | 2 | 3 | 4 |
| IDS/IPS and runtime security | 1 | 3 | 4 |
| Incident response / forensics | 3 | 4 | 5 |
| Vulnerability management | 1 | 2 | 4 |
| **Composite Rating** | **2** | **3** | **5** |

### Evidence

Cloud-Native: CloudWatch, AWS GuardDuty, Azure Sentinel, and Google Security Command Center provide managed SIEM capabilities. Cloud detection rates for Kubernetes attack techniques range from 24% (GCP SCC) to 66% (Azure Defender) — cloud-native agents cannot substitute for K8s-native tooling (Falco, Trivy), meaning managed K8s deployments still require K8s-specific security tools even when using cloud-native SIEM. Total FTE: 0.25–1.2.
(Source: F71; F55c)

Managed K8s: Falco, Kyverno, and Trivy are required for K8s-native runtime security. SIEM at managed K8s difficulty: 3/5. IR/Forensics at managed K8s difficulty: 4/5. Total FTE: 2.25–4.5.
(Source: F71)

On-Premises: A 24/7 Security Operations Center requires a minimum of 12 FTE and costs $1.5M–$5M annually. 73% of security practitioners cite false positives as the top challenge in on-premises SIEM environments. On-premises incident response and forensics is rated 5/5 because access must be physically coordinated with customer IT staff, memory acquisition and log preservation requires on-site tools, and the ISV has no direct infrastructure access. Total on-premises SecOps FTE: 2.75–5.5.
(Source: F71)

28% of CVEs are weaponized within one day of disclosure. 77% of enterprises take more than one week to deploy patches. CISA Known Exploited Vulnerabilities catalog grew 20% year-over-year to 1,484 entries in 2025, with some mandated remediation timelines as short as seven days. This gap between exploit velocity and patch deployment speed is most dangerous for on-premises deployments where patch delivery requires customer coordination.
(Source: F60; W08S, Theme 2)

**FTE Estimates:**
- Cloud-Native: 0.25–1.2 FTE
- Managed K8s: 2.25–4.5 FTE
- On-Premises: 2.75–5.5 FTE

---

## Summary Difficulty Matrix

The table below presents all ten Control Plane subsegments with composite difficulty ratings across three deployment tiers.

**Difficulty Scale:** 1 = Trivial | 2 = Low | 3 = Moderate | 4 = High | 5 = Extreme

| ID | Subsegment | Cloud-Native | Managed K8s | On-Premises | Primary Source Files |
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
| | **Aggregate Score** | **13** | **28** | **47** |  |
| | **Average Difficulty** | **1.3** | **2.8** | **4.7** |  |

### Aggregate FTE Ranges (mid-size ISV, 50 enterprise customers)

| Subsegment | Cloud-Native FTE | Managed K8s FTE | On-Premises FTE |
|---|---|---|---|
| CP-01 Cluster Lifecycle | 0.0–0.5 | 1.0–2.5 | 3.0–6.0 |
| CP-02 Network / Ingress / Mesh | 0.1–0.7 | 0.75–1.75 | 1.75–3.5 |
| CP-03 IAM / RBAC | 0.3–0.8 | 1.65–2.65 | 2.75–4.75 |
| CP-04 Secrets / Certs / PKI | 0.4–0.85 | 0.4–0.85 | 2.5–5.0 |
| CP-05 Observability Infrastructure | 0.55–1.0 | 1.25–2.0 | 4.6–7.0 |
| CP-06 CI/CD Infrastructure / GitOps | 0.3–0.4 | 1.3–1.9 | 2.0–3.25 |
| CP-07 Deploy Lifecycle / Rollback | 0.1–0.35 | 0.35–0.75 | 1.5–3.0 |
| CP-08 Disaster Recovery | 0.25–0.5 | 0.5–1.0 | 1.5–2.5 |
| CP-09 Compliance Automation | 0.5–1.0 | 1.25–2.0 | 2.5–4.0 |
| CP-10 Security Operations | 0.25–1.2 | 2.25–4.5 | 2.75–5.5 |
| **Total (raw sum)** | **2.75–7.3** | **10.75–19.9** | **24.85–44.5** |
| **Deduplicated estimate** | **~2.5–6.5** | **~9–16** | **~20–38** |

**Deduplication note:** Raw sums include partial scope overlap between CP-03 (IAM), CP-04 (Secrets/Certs), and CP-10 (SecOps) due to mTLS, workload identity, and security monitoring boundaries. Deduplicated estimates remove approximately 1.0–2.0 FTE from the security cluster per tier, consistent with the W06S security domain de-duplication guidance.

---

## Cross-Subsegment Patterns

### Pattern 1: The "Managed" Label Masks ISV Responsibility

The aggregate Managed K8s difficulty (2.8 average) is closer to On-Premises (4.7) than to Cloud-Native (1.3) in absolute FTE terms — a 9–16 FTE managed K8s range versus 2.5–6.5 cloud-native. The control plane label ("managed K8s") is accurate only for CP-01 (where the API server and etcd are truly managed); across CP-02 through CP-10, ISVs retain significant or full operational responsibility. The W07S synthesis confirms: security (CP-10) and observability (CP-05) together account for 3.25–6.0 FTE on managed K8s — alone exceeding the total operational burden of a fully cloud-native deployment.
(Source: W07S, Theme 4; F55c; F55d)

### Pattern 2: On-Premises Operational Work Scales Linearly with Customer Count

On-premises incident response, patch coordination, SLA management, and on-call burden each scale linearly with customer count, while cloud-native operations scale sub-linearly as automation absorbs per-customer overhead. An ISV with 50 on-premises customers faces 50 separate incident response chains, 50 patch coordination sequences, and 50 compliance audit surfaces — each requiring customer access provisioning, collaborative diagnosis with customer IT, and change approval before resolution can begin. The same ISV on cloud-native manages a single observability stack and deployment pipeline.
(Source: W08S, Theme 5; F59)

### Pattern 3: Mandatory Technology Migrations Compound Risk in 2025–2026

Multiple Control Plane components face simultaneous mandatory migrations creating compounding risk for on-premises and managed K8s ISVs:
- Ingress NGINX EOL March 2026 (affects CP-02)
- Jaeger v1 deprecated January 2026 (affects CP-05)
- FIPS 140-2 certificate expiry September 2026 (affects CP-04)
- Let's Encrypt 45-day certificate validity (May 2026) — affects CP-04 rotation automation at all tiers
- OPA maintainer uncertainty post Apple acquisition August 2025 (affects CP-03)

Each migration consumes FTE from the same limited platform engineering pool. Cloud-native ISVs are largely shielded: providers absorb networking migrations (CP-02), certificate rotation (CP-04), and monitoring backend changes (CP-05) without ISV action.
(Source: W06S, Theme 3; F73 C03; F51; F47; F46)

### Pattern 4: Security and Identity Are Disproportionately FTE-Intensive On-Premises

CP-03 (IAM/RBAC) + CP-04 (Secrets/PKI) + CP-10 (SecOps) together require 8.0–15.25 FTE on-premises — representing 32–40% of total Control Plane on-premises FTE. IAM is described in source research as "a product line, not an infrastructure dependency" with seven sub-domains each rated 3–4/5 difficulty. A 24/7 SOC requires a minimum of 12 FTE and $1.5M–$5M annually on-premises.
(Source: F46; F47; F71; W06S, Theme 2)

### Pattern 5: AI Workloads Amplify Every On-Premises Control Plane Penalty

ISVs deploying AI-SaaS features face the highest on-premises Control Plane burden because GPU nodes add complexity across CP-01 (GPU node pool management, DRA scheduling), CP-02 (high-bandwidth networking for NVLink), CP-05 (GPU metric cardinality from DCGM Exporter), CP-06 (GPU-aware CI/CD pipelines), and CP-07 (GPU-constrained rollback). High-end GPU server lead times reach 6–12 months versus seconds-to-minutes for cloud auto-scaling. An on-premises GPU test lab requires approximately $500,000 in capital versus cloud H100 GPU instances starting at $1.49/hour with break-even below 60–70% utilization.
(Source: W08S, Theme 4; F60; F55b; W07S, Theme 3)

---

## Key Takeaways

1. **The aggregate difficulty ratio is 1.0 : 2.2 : 3.6 (Cloud-Native : Managed K8s : On-Premises)** on the 1–5 scale (1.3 : 2.8 : 4.7 average). In FTE terms the ratio widens further to approximately 1 : 3 : 8, because high-difficulty subsegments compound nonlinearly into staffing requirements.

2. **No Control Plane subsegment is easier on-premises than on managed K8s, and no subsegment is easier on managed K8s than cloud-native**, with the single exception of data sovereignty enforcement in CP-09 (where on-premises is easiest because data never leaves customer infrastructure).

3. **Four subsegments are rated 5/5 on-premises** (CP-02, CP-04, CP-07, CP-08, CP-09, CP-10 — six total reach 5/5), confirming that the dominant operational mode for on-premises Control Plane is extreme complexity requiring dedicated specialist staff with no viable generalist-substitution strategy.

4. **The most consequential near-term forcing function** is the Ingress NGINX retirement (November 2025, maintenance ending March 2026): it requires mandatory CP-02 rework for any managed K8s or on-premises ISV currently using Ingress NGINX, adding 0.3–0.6 FTE of unplanned platform work regardless of product roadmap priority.

5. **The FTE gap between cloud-native and on-premises is structural, not solvable by tooling alone.** The W08S synthesis documents that on-premises operational work scales linearly with customer count while cloud-native scales sub-linearly — meaning the FTE gap widens as the ISV grows its customer base, compounding the business case for cloud-native deployment.

---

## Source File Reference Index

| File | Wave | Primary Contribution |
|---|---|---|
| F40 — On-Prem Networking | Wave 6 | CP-02 networking difficulty and FTE |
| F46 — On-Prem IAM/Identity | Wave 6 | CP-03 IAM difficulty and FTE |
| F47 — On-Prem Secrets/Certs | Wave 6 | CP-04 secrets and PKI difficulty and FTE |
| F48 — On-Prem CI/CD | Wave 6 | CP-06 CI/CD infrastructure difficulty and FTE |
| F49 — On-Prem Logging | Wave 6 | CP-05 logging backend difficulty, FTE, cost crossover |
| F50 — On-Prem Monitoring | Wave 6 | CP-05 metrics backend difficulty, FTE, cardinality |
| F51 — On-Prem Tracing | Wave 6 | CP-05 tracing backend difficulty, Jaeger EOL |
| F52 — Managed K8s Platforms | Wave 7 | CP-01 platform difficulty and FTE baseline |
| F53 — Portable K8s ISV Delivery | Wave 7 | CP-01, CP-06 ISV delivery complexity |
| F55 — K8s Service Mesh | Wave 7 | CP-02 service mesh difficulty and adoption trends |
| F55c — K8s Security Posture | Wave 7 | CP-03, CP-04, CP-10 Kubernetes security difficulty |
| F55d — K8s Observability Stack | Wave 7 | CP-05 managed K8s observability FTE and RAM |
| F58 — Deploy/Release Differences | Wave 8 | CP-07 deployment strategies and rollback |
| F59 — Operate/Monitor Differences | Wave 8 | CP-07, CP-10 day-2 operations and on-call scaling |
| F60 — Update/Patch/Scale | Wave 8 | CP-07, CP-09, CP-10 patching velocity and CVE risk |
| F67 — Compliance/Regulatory | Wave 10 | CP-09 compliance difficulty and FTE |
| F70 — Disaster Recovery/BC | Wave 10 | CP-08 DR difficulty and FTE |
| F71 — On-Prem Security Ops | Wave 10 | CP-10 SecOps difficulty and SOC FTE |
| F73 — MECE ISV Dev Responsibility | Wave 11 | MECE boundary enforcement, application logic exclusion |
| F76 — MECE Failure Domain | Wave 11 | Failure domain patterns, blast radius, cascade chains |
| F77 — MECE Runtime Lifecycle | Wave 11 | Lifecycle phase difficulty matrix, FTE ratios |
| W06S — On-Prem Infrastructure Synthesis | Synthesis | Aggregate FTE, cross-domain patterns, deduplication |
| W07S — Managed K8s Synthesis | Synthesis | Managed K8s FTE, ecosystem instability, GPU differentiator |
| W08S — SDLC Differences Synthesis | Synthesis | Portability tax, patching asymmetry, release velocity |
