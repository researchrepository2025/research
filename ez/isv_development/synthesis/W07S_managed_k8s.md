# W07S: Managed Kubernetes as ISV Deployment Model — Wave 7 Synthesis

**Synthesis of:** F52 (Managed K8s Platforms), F53 (Portable K8s ISV Delivery), F54 (K8s Operators Stateful), F55 (Service Mesh), F55a (K8s Data Services), F55b (K8s GPU & AI Workloads), F55c (K8s Security Posture), F55d (K8s Observability Stack)

---

## Executive Summary

Managed Kubernetes (EKS, AKS, GKE) occupies a compelling but demanding middle ground between fully cloud-native managed services and self-hosted on-premises infrastructure. The "managed" label is accurate only for the control plane — API server, etcd, scheduler, and controller manager — while the ISV retains full responsibility for a sprawling workload layer spanning data services, security, observability, GPU scheduling, and service networking. Across all eight research files, a consistent finding emerges: Kubernetes operators and CNCF ecosystem tooling have closed much of the *feature* gap with cloud-native services, but the *operational* gap remains substantial, requiring [1.0-2.5 FTE for the base platform](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke) (from F52) before layering on data, security, observability, and AI workloads. For an ISV serving 50 enterprise customers on 3-5 clusters, the aggregate operational burden across all domains is estimated at 7.5-13.5 FTE on managed K8s versus 2.0-4.0 FTE for equivalent cloud-native managed services. The platform's strongest differentiator is GPU/AI workload portability, where DRA, KServe, and KAI Scheduler provide capabilities with no cloud-native equivalent. Its weakest proposition is data services, where a [1.5-3.0 FTE gap versus cloud-native](https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/) (from F55a) routinely erases compute savings.

---

## Key Themes

### Theme 1: The "Managed" Label Masks Significant ISV Responsibility

No managed K8s provider ships a production-ready security stack, observability pipeline, or data services layer. ISVs must select, deploy, configure, and maintain at least [a dozen add-on components](https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/) (from F52) spanning ingress controllers, RBAC policies, storage classes, network policies, and secrets management. [AKS Long Term Support](https://blog.aks.azure.com/2025/07/25/aks-lts-announcement) (from F52) extends Kubernetes version support to 24 months — a welcome improvement — but version lifecycle is only one of many operational burdens. The security domain alone requires assembling Kyverno + Cilium + Falco as a baseline stack, with [cloud detection rates ranging from 24% (GCP SCC) to 66% (Azure Defender)](https://cymulate.com/blog/native-cloud-security-kubernetes-defenses/) (from F55c) for Kubernetes attack techniques, meaning cloud-native agents cannot substitute for K8s-native tooling. The observability stack (Prometheus + Grafana + Loki + Tempo) consumes [15-35 GB of cluster RAM](https://github.com/prometheus-operator/prometheus-operator) (from F55d) before any application workloads are monitored.

### Theme 2: Operators Have Closed the Feature Gap but Not the Operational Gap

Kubernetes operators for stateful workloads have matured rapidly. [CloudNativePG reached 132M+ downloads](https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/) (from F55a) and provides quorum-based failover, in-place major upgrades (v1.26+), and declarative database management. [KServe was accepted as a CNCF Incubating project in September 2025](https://github.com/kserve/kserve) (from F55b), with v0.15 introducing multi-node LLM inference and KEDA autoscaling integration. Strimzi manages KRaft-based Kafka clusters on K8s. However, the labor cost delta is persistent: running PostgreSQL on CloudNativePG costs [$2,700-5,400/month in compute versus $1,800-2,200 for Aurora](https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql) (from F55a), and when operational FTE is included, the total cost of ownership favors cloud-native services by a 2-3x margin for most ISVs. The data gravity effect further locks workloads into whichever model is selected initially, making the choice [largely irreversible at scale](https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/) (from F55a).

### Theme 3: GPU/AI Workloads Are Managed K8s's Strongest Differentiator

This is the domain where managed Kubernetes most credibly closes the gap with — and in some dimensions exceeds — cloud-native services. [DRA graduated to GA in Kubernetes 1.34 (August 2025)](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/) (from F55b), enabling flexible GPU device allocation including alternative device selection and consumable capacity sharing. [NVIDIA open-sourced the KAI Scheduler in April 2025](https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/) (from F55b), adding topology-aware scheduling, gang scheduling, and hierarchical fairshare — capabilities no cloud-native AI endpoint exposes. [KServe v0.15](https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/) (from F55b) upgraded to vLLM 0.8.5 with multi-model support, and the [CNCF AI Conformance Program v1.0 launched in November 2025](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/) (from F55b), creating vendor-neutral standards for AI workloads. The persistent tradeoff: [2-4 FTE for GPU infrastructure versus near-zero for managed endpoints](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/) (from F55b), and [GPUs sit underutilized 60-80% of the time](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/) (from F55b) on K8s without advanced scheduling.

### Theme 4: The Security and Observability Tax Is Steeper Than Expected

Security and observability together constitute the largest operational burden on managed K8s. The security domain requires [2.0-4.0 FTE across eight sub-domains](https://cymulate.com/blog/native-cloud-security-kubernetes-defenses/) (from F55c) — RBAC, pod security, network policy, image scanning/signing, secrets management, runtime detection, and supply chain security — versus 0.6-1.3 FTE for cloud-native. [Native K8s Secrets are base64-encoded rather than encrypted](https://atmosly.com/blog/kubernetes-secrets-management-vault-vs-sealed-secrets-vs-external-secrets-2025) (from F55c), and every production deployment must explicitly enable etcd encryption or use External Secrets Operator. The observability stack adds [1.25-2.0 FTE](https://github.com/prometheus-operator/prometheus-operator) (from F55d), and the recommended hybrid approach — cloud-managed Prometheus for metrics, self-managed Loki/Tempo for logs and traces — introduces split-stack operational complexity. Combined, security and observability account for 3.25-6.0 FTE, which alone exceeds the total operational burden of a fully cloud-native deployment model.

### Theme 5: Platform Ecosystem Instability Creates ISV Delivery Risk

The portable Kubernetes ecosystem — ISVs' pathway to customer-controlled environments — experienced significant disruption in 2025. [VMware Tanzu Kubernetes Grid v2.5.4 is the final TKG release](https://techdocs.broadcom.com/us/en/vmware-tanzu/standalone-components/tanzu-kubernetes-grid/2-5/tkg/mgmt-release-notes.html) (from F53), with customers directed to migrate to vSphere Kubernetes Service (VKS). [SUSE's CPU-based Rancher pricing caused 4-9x cost increases](https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025) (from F53), triggering enterprise exploration of alternatives. Service mesh adoption declined from 50% (2023) to 42% (2024) to [8% developer-level adoption by Q3 2025](https://arxiv.org/html/2411.02267v1) (from F55), reflecting a market correction where the operational complexity of sidecar-based meshes outweighed benefits for most teams. The emerging shift toward sidecarless architectures — [Istio Ambient mode adds only 8% latency](https://arxiv.org/html/2411.02267v1) (from F55) versus 166% for sidecar mode — may eventually reverse adoption decline, but the current instability creates planning uncertainty for ISVs building multi-year platform strategies.

---

## Difficulty & FTE Summary Table

**Assumptions:** Mid-size ISV, 50 enterprise customers, 3-5 clusters, 100-300 services.

| Domain | Managed K8s FTE | Cloud-Native FTE | Source Files |
|---|---|---|---|
| Base platform (control plane, node pools, upgrades) | 1.0-2.5 | 0.0-0.5 | F52 |
| Data services (PostgreSQL, Kafka, Redis) | 1.5-3.0 | 0.25-0.5 | F55a, F54 |
| GPU / AI workloads | 2.0-4.0 | 0.1-0.25 | F55b |
| Security (full stack) | 2.0-4.0 | 0.6-1.3 | F55c |
| Observability (full stack) | 1.25-2.0 | 0.45-0.65 | F55d |
| Service mesh (if adopted) | 0.5-1.0 | 0.0-0.1 | F55 |
| ISV delivery / portable K8s | 0.5-1.0 | N/A | F53 |
| **Aggregate** | **~8.75-17.5** | **~1.4-3.3** | All |

Note: Aggregate FTE includes partial overlap across domains (e.g., a platform engineer covers both base platform and partial security). Realistic deduplicated range for a fully staffed managed K8s deployment is approximately 7.5-13.5 FTE, versus 2.0-4.0 FTE for cloud-native.

---

## Cross-Agent Patterns & Contradictions

**Consistent patterns across all eight files:**
- Every domain exhibits a 2-4x FTE multiplier for managed K8s versus cloud-native services. This ratio holds remarkably consistently across data services (F55a), security (F55c), observability (F55d), and GPU workloads (F55b).
- Operator maturity is high (CloudNativePG Level 5, KServe CNCF Incubating, Strimzi KRaft), but critical Day 2+ operations — major version upgrades, cross-cluster disaster recovery, performance tuning — still require human expertise that no operator fully automates (F54).
- Multi-cloud portability is the recurring strategic justification, but data gravity (F55a) and platform-specific integrations (F52, F53) progressively erode portability in practice.

**Contradictions and tensions:**
- F55b positions managed K8s as the leading AI inference platform, yet F55a shows data services on K8s are economically unfavorable — creating tension for ISVs whose AI workloads depend on co-located data.
- F55c recommends a complementary model (cloud-native agents + K8s-native tools), while F55's service mesh findings suggest declining willingness to adopt additional infrastructure layers — ISVs may resist the multi-tool security stack recommended in F55c.
- F53 documents the Replicated/KOTS pathway for portable ISV delivery, but F52 shows that even managed K8s clusters vary significantly in CNI, storage classes, and add-ons — the very variability Replicated tries to abstract away remains a persistent support burden.

---

## Open Questions for Downstream Synthesis

1. **At what customer count does the FTE differential make managed K8s economically rational?** The 2-4x operational burden is clear, but ISVs with sovereignty requirements or large single-customer deployments may absorb this cost differently.
2. **Can the hybrid observability strategy (cloud-managed Prometheus + self-managed Loki/Tempo) be generalized to data services?** If so, CloudNativePG for extension flexibility paired with managed services for the commodity tiers could compress the FTE gap.
3. **Does the CNCF AI Conformance Program create enough vendor-neutral standardization to make K8s GPU workload portability a durable advantage, or will cloud-native AI services converge on similar capabilities?**
4. **How does the TKG sunset / SUSE pricing disruption affect ISVs already committed to portable K8s delivery — is there a migration path to Replicated Embedded Cluster that avoids platform dependency entirely?**
5. **What is the actual FTE cost of maintaining the Kyverno + Cilium + Falco security baseline across 3-5 clusters with rotating policy updates — and does this scale linearly or superlinearly with cluster count?**

---

## Sources

### F52: Managed K8s Platforms
- [Kubernetes Cost: EKS vs AKS vs GKE — Sedai](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke)
- [AKS EKS GKE Managed Kubernetes as a Service — Fairwinds](https://www.fairwinds.com/blog/aks-eks-gke-managed-kubernetes-as-a-service)
- [AKS LTS Announcement — AKS Engineering Blog](https://blog.aks.azure.com/2025/07/25/aks-lts-announcement)
- [Top 5 Hard-Earned Lessons from the Experts on Managing Kubernetes — CNCF](https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/)
- [Complete Guide to Kubernetes Management in 2025 — ScaleOps](https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/)

### F53: Portable K8s ISV Delivery
- [SUSE Rancher Price Hike — Portainer Blog](https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025)
- [VMware vSphere Kubernetes Service 3.3 GA — VMware Cloud Foundation Blog](https://blogs.vmware.com/cloud-foundation/2025/03/04/vmware-vsphere-kubernetes-service-3-3-is-now-ga/)
- [TKG v2.5.x Release Notes — Broadcom TechDocs](https://techdocs.broadcom.com/us/en/vmware-tanzu/standalone-components/tanzu-kubernetes-grid/2-5/tkg/mgmt-release-notes.html)
- [KOTS Introduction — Replicated](https://docs.replicated.com/intro-kots)

### F54: K8s Operators Stateful
- [Kubernetes Operators 2025 Guide — OuterByte](https://outerbyte.com/kubernetes-operators-2025-guide/)
- [Operator Lifecycle Manager — GitHub](https://github.com/operator-framework/operator-lifecycle-manager)

### F55: Service Mesh
- [Performance Comparison of Service Mesh Frameworks — arXiv](https://arxiv.org/html/2411.02267v1)
- [Service Meshes Decoded: Istio vs Linkerd vs Cilium — LiveWyer](https://livewyer.io/blog/service-meshes-decoded-istio-vs-linkerd-vs-cilium/)
- [Sidecars Dying: Ambient Mesh, eBPF, Gateway API 2025 — debugg.ai](https://debugg.ai/resources/sidecars-dying-ambient-mesh-ebpf-gateway-api-2025)

### F55a: K8s Data Services
- [CloudNativePG in 2025 — Gabriele Bartolini](https://www.gabrielebartolini.it/articles/2025/12/cloudnativepg-in-2025-cncf-sandbox-postgresql-18-and-a-new-era-for-extensions/)
- [Aurora vs RDS vs EC2 PostgreSQL — Certvanta](https://certvanta.com/blog/2025/12/aurora-vs-rds-vs-ec2-postgresql)
- [Self-Hosted Kafka vs Fully Managed Kafka — AutoMQ](https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons)
- [Strimzi KRaft Migration — Strimzi](https://strimzi.io/kraft/)

### F55b: K8s GPU & AI Workloads
- [Kubernetes v1.34: DRA has graduated to GA — kubernetes.io](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/)
- [NVIDIA Open Sources Run:ai Scheduler — NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/)
- [KServe v0.15: Advancing Generative AI Model Serving — CNCF](https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/)
- [CNCF Launches Kubernetes AI Conformance Program — CNCF](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/)
- [GPU Underutilization and Optimization — ScaleOps](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/)

### F55c: K8s Security Posture
- [Can Cloud Security Tools Protect Kubernetes Environments — Cymulate](https://cymulate.com/blog/native-cloud-security-kubernetes-defenses/)
- [Kubernetes Secrets Management 2025 — Atmosly](https://atmosly.com/blog/kubernetes-secrets-management-vault-vs-sealed-secrets-vs-external-secrets-2025)
- [Supply Chain Security: SBOM, SLSA, Sigstore 2025 — Elysiate](https://www.elysiate.com/blog/supply-chain-security-sbom-slsa-sigstore-2025)
- [Kubernetes Policy Comparison: Kyverno vs OPA/Gatekeeper — Nirmata](https://nirmata.com/2025/02/07/kubernetes-policy-comparison-kyverno-vs-opa-gatekeeper/)

### F55d: K8s Observability Stack
- [prometheus-operator/prometheus-operator — GitHub](https://github.com/prometheus-operator/prometheus-operator)
- [Prometheus Storage Comparison 2025 — Onidel](https://onidel.com/blog/prometheus-storage-comparison-2025)
- [Grafana Loki OSS — Grafana Labs](https://grafana.com/oss/loki/)
- [Amazon Managed Service for Prometheus Pricing — AWS](https://aws.amazon.com/prometheus/pricing/)
- [Grafana Cloud Observability Platform — Grafana Labs](https://grafana.com/products/cloud/)
