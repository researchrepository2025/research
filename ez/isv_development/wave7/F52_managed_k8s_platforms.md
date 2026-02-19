# F52: Managed Kubernetes Platforms (EKS / AKS / GKE)

**Research Question:** What do managed Kubernetes services provide out of the box, what operational burden remains even with managed K8s, and where do they fall short compared to fully managed cloud-native services?

---

## Executive Summary

Managed Kubernetes platforms — Amazon EKS, Azure AKS, and Google GKE — offload control-plane operations (API server, etcd, scheduler, controller manager) to the cloud provider, but ISVs retain full responsibility for everything that runs on top of that control plane: application deployment, service mesh, ingress controllers, persistent storage classes, RBAC policies, network policies, and a growing ecosystem of mandatory add-ons. [Control plane costs differ materially](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke): AKS provides a free control plane, while EKS and GKE each charge $0.10/hour (~$72/month) per cluster. GPU workloads are natively supported through managed node pools, NVIDIA device plugin automation (via the GPU Operator), and Multi-Instance GPU (MIG) partitioning on A100/H100 hardware, making managed K8s the current leading platform for AI inference workloads requiring more control than serverless but less infrastructure burden than fully self-hosted clusters. The remaining operational gap versus fully cloud-native services is significant: managed K8s still requires ISV teams to operate and upgrade at least a dozen add-on components, manage cluster version lifecycle on a roughly four-month cadence, and maintain multi-cluster governance tooling that no cloud provider supplies as a managed service. A mature mid-scale deployment realistically requires 1.0–2.5 FTE of dedicated Kubernetes platform engineering to run safely in production.

---

## 1. What Is Managed: The Managed Control Plane

All three major cloud providers manage the Kubernetes control plane as a multi-AZ, highly available service. The following components are fully operated by the cloud provider and require no ISV involvement beyond version selection:

| Component | EKS | AKS | GKE |
|-----------|-----|-----|-----|
| API Server | Managed, multi-AZ | Managed, free | Managed |
| etcd | Managed | Managed | Managed |
| Controller Manager | Managed | Managed | Managed |
| Scheduler | Managed | Managed | Managed |
| Control plane upgrades | Semi-automatic | Semi-automatic | Automatic (Release channels) |
| CoreDNS | [Managed add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-coredns.html) | Managed | Managed |
| kube-proxy | [Managed add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-kube-proxy.html) | Managed | Managed |
| CNI plugin | VPC CNI (managed add-on) | Azure CNI / Kubenet | Calico / eBPF |

[FACT] "AKS, EKS, and GKE all handle the Kubernetes control plane, and underlying physical infrastructure. Specifically, all three providers deploy and maintain the control plane for you, so you only have to worry about the nodes."
URL: https://www.fairwinds.com/blog/aks-eks-gke-managed-kubernetes-as-a-service

### 1.1 Node Auto-Scaling and Managed Node Groups

Each platform provides managed node groups or equivalent, but the degree of automation varies substantially.

**EKS Managed Node Groups:** AWS manages node AMI selection, rolling updates, and compatibility with the EKS control plane version for nodes in managed node groups. [Karpenter](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html) (OSS, developed by AWS) provides just-in-time node provisioning in under one minute, and is the recommended replacement for Cluster Autoscaler on EKS. EKS Auto Mode (GA 2025) extends this further by automatically provisioning GPU instances when workloads request GPU resources.

[FACT] "Salesforce's migration journey began in mid-2025 with lower-risk environments and progressed through testing and validation phases before production adoption in early 2026, involving over 1,000 EKS clusters."
URL: https://www.infoq.com/news/2026/01/salesforce-eks-karpenter/

**AKS Node Auto-Provisioning (NAP):** NAP became generally available in AKS in mid-July 2025. NAP is Karpenter adapted for AKS via the Azure provider. "NAP looks at pending pods, chooses optimal VMs on the fly, and continually consolidates to cut waste." NAP cannot coexist with Cluster Autoscaler; one must be disabled before enabling the other.
URL: https://blog.aks.azure.com/2025/12/06/node-auto-provisioning-capacity-management

**GKE Autopilot:** Google's most fully managed mode. "In Autopilot mode, Google handles the entire infrastructure stack — nodes, autoscaling, upgrades, security, and networking — so you can deploy containers without managing servers." Billing in Autopilot is per pod resource request, not per node.
URL: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview

**GKE Standard:** Splits responsibilities — Google manages the control plane; the ISV manages node pools, scaling, upgrades, and security. Standard clusters often run at 20–30% node utilization because teams provision for peak capacity.
URL: https://www.kloudstax.com/blog/raah36imow738cpeik0u15musq0qkp

---

## 2. What Is NOT Managed: Remaining ISV Responsibility

Despite the "managed" label, a large surface area of cluster operation remains entirely the ISV's responsibility. [QUOTE] "running a production environment means managing all the hidden add-ons: DNS controllers, networking, storage, monitoring, logging, secrets, security, and more."
URL: https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/

### 2.1 Application Deployment

Kubernetes does not provide deployment strategies beyond RollingUpdate and Recreate. [FACT] "Out-of-box, Kubernetes doesn't support deployment strategies that use 2 or more live environments at the same time — you'll need load balancers, service mesh, or dedicated deployment tools to adopt Blue/green, Canary, A/B testing, and Shadow strategies."
URL: https://octopus.com/devops/kubernetes-deployments/

### 2.2 Service Mesh

No managed K8s provider includes a service mesh. [FACT] "To deploy a service mesh, you have to install external software such as Istio, Traefik Mesh, Consul or Linkerd, to name just a few popular open source service meshes."
URL: https://konghq.com/blog/engineering/using-service-mesh-in-kubernetes-enviroment

See [F55: Service Mesh Details] for comprehensive coverage of service mesh operational overhead.

### 2.3 Ingress Controllers

No managed K8s platform provides a configured ingress controller by default. The ISV must select, install, configure, and upgrade an ingress controller. Common options:

- **ingress-nginx** (community): most widely deployed, supports canary routing, TLS termination, and per-service routing via annotations
- **AWS Load Balancer Controller** (EKS): provisions ALB/NLB per Ingress resource
- **Azure Application Gateway Ingress Controller (AGIC)** (AKS): integrates with Azure Application Gateway
- **GKE Gateway Controller** (GKE): uses the Kubernetes Gateway API; managed by Google as optional add-on

### 2.4 Persistent Storage Configuration

All three platforms provide CSI drivers as managed add-ons (EBS CSI, Azure Disk CSI, GCP Persistent Disk CSI), but StorageClass definitions, PersistentVolumeClaim templates, volume expansion policies, and backup policies are entirely the ISV's responsibility. [FACT] "Kubernetes tried to bridge this with StatefulSets and PersistentVolumeClaims that gave operators some guardrails: Sticky identities, ordered deployment and predictable storage mappings. But those tools don't solve the hardest part: Live migration."
URL: https://cloudnativenow.com/features/stateful-microservice-migration-the-live-state-challenge-in-kubernetes/

### 2.5 RBAC Policies

Kubernetes RBAC roles and bindings are not pre-configured beyond system defaults. ISVs must define: ClusterRoles, Roles, ClusterRoleBindings, RoleBindings, and ServiceAccount assignments for every workload and human operator. Each cloud provider offers an IAM integration layer (EKS: AWS IAM Roles for Service Accounts / IRSA; AKS: Azure Workload Identity; GKE: Workload Identity Federation), but the K8s-side RBAC objects remain the ISV's responsibility.

### 2.6 Network Policies

Default behavior in all managed K8s clusters is open inter-pod communication (no NetworkPolicy resources exist at cluster creation). ISVs must define NetworkPolicy objects to implement namespace isolation, tenant separation, and egress restrictions. [FACT] "A best practice to isolate each tenant is to apply a default Network Policy to all tenant namespaces, which blocks access from other namespaces."
URL: https://d2iq.com/blog/key-multi-tenancy-challenges-in-the-public-cloud-and-how-to-solve-for-them-100-11

---

## 3. Operational Burden: Cluster Lifecycle

### 3.1 Version Upgrade Cadence and Support Policy

The upstream Kubernetes project releases approximately three minor versions per year (roughly every 4 months). Each cloud provider's support window:

| Provider | Standard Support Window | Extended Support | Notes |
|----------|------------------------|------------------|-------|
| EKS | 14 months per version | +12 months (additional cost) | [Source](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) |
| AKS | 12 months (GA); 24 months via LTS | LTS GA July 2025 | [Source](https://blog.aks.azure.com/2025/07/25/aks-lts-announcement) |
| GKE | ~14 months (Standard channel) | Varies by release channel | — |
| Community | N to N-2 only (~12 months) | None | [Source](https://endoflife.date/kubernetes) |

[FACT] "AKS Long Term Support is a support plan that provides 24 months of support for Kubernetes versions from their GA date in AKS, compared to the standard 12-14 month support lifecycle. Every currently supported AKS Kubernetes version is now also available for long term support."
URL: https://blog.aks.azure.com/2025/07/25/aks-lts-announcement

[QUOTE] "Tech debt piles up until a CVE forces a massive, risky, and time-consuming jump across several versions at once."
URL: https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/

**Version skew policy (Kubernetes 1.28+):** EKS and AKS both support up to 3 minor version skew between control plane and data plane nodes (previously 2), providing more flexibility in upgrade sequencing.
URL: https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html

### 3.2 Upgrade Patterns

[FACT] Three upgrade patterns with distinct risk profiles:

1. **Blue/Green Immutable Upgrade:** Create a new cluster at target version, sync via GitOps, shift traffic once proven. Provides instant rollback but is "cost prohibitive for large, multi-tenant deployments."
2. **In-Place Rolling Upgrade:** Nodes upgraded in place via managed node group rolling replace. Requires mature workload safety primitives (PodDisruptionBudgets, topologySpreadConstraints, PriorityClasses).
3. **N-2 Doctrine:** A mature organization should keep "no production cluster more than two minor versions behind the latest stable Kubernetes release."

URL: https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/

### 3.3 Resource Quotas and Namespace Governance

No managed K8s provider delivers pre-configured multi-tenancy governance. ISVs must implement:

- **ResourceQuota** per namespace (CPU, memory, object count limits)
- **LimitRange** defaults for containers without explicit requests/limits
- **Namespace lifecycle management** (creation, labeling, deletion policies)
- **Pod Security Standards** (admission configuration for baseline/restricted profiles)

[FACT] "Managing cluster upgrades, network configurations, service meshes, security policies, and multi-cluster environments requires deep expertise and significant investment in automation and governance."
URL: https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/

### 3.4 Operational Difficulty Ratings and FTE Estimates

Assumptions: mid-scale ISV serving 50 enterprise customers, 3–5 production clusters, 100–300 services.

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| **Control Plane** | Difficulty: 5/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| | Full self-operation of API server, etcd, scheduler | Cloud provider operates; ISV selects version | No K8s control plane exposure |
| | kubeadm, kops, or RKE | Console or IaC (Terraform) | Provider-managed entirely |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.0 | Est. FTE: 0.0 |
| **Node Pool Management** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Full hardware + OS + kubelet management | Managed node groups, auto-scaling | No node exposure (Fargate/Autopilot/Container Apps) |
| | Physical servers or VMs + OS patching | Karpenter / NAP / Cluster Autoscaler | Provider manages fully |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0 |
| **Cluster Upgrades** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Manual etcd backup, kubeadm upgrade, full drain | Control plane auto; node rolling upgrade still ISV | No version management |
| | High risk of breakage; long maintenance windows | Requires testing, PDBs, add-on compatibility checks | Provider handles entirely |
| | Est. FTE: 0.25–0.5 (per upgrade cycle) | Est. FTE: 0.1–0.25 (per upgrade cycle) | Est. FTE: 0.0 |
| **RBAC & Network Policy** | Difficulty: 4/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Full policy authoring + enforcement | Same K8s API; cloud IAM integration adds complexity | IAM policies replace most K8s RBAC |
| | OPA/Kyverno for admission control | OPA/Kyverno/PSA for admission control | Cloud-native IAM |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 |
| **Add-on Ecosystem** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | All add-ons self-hosted, self-upgraded | Most add-ons ISV-managed; some cloud-managed options | Observability, DNS, LB all cloud-managed |
| | cert-manager, external-dns, ingress, Prometheus | cert-manager, ingress controller, Prometheus stack | CloudWatch, Azure Monitor, Cloud Monitoring |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |

---

## 4. Add-On Ecosystem: What the ISV Must Install and Maintain

Even on fully managed K8s, the following components are not provided by any cloud vendor and must be installed, configured, and individually upgraded by ISV platform teams. Each add-on has its own release cadence, breaking change history, and compatibility matrix with Kubernetes core.

### 4.1 cert-manager

Automates TLS certificate issuance and renewal from ACME providers (Let's Encrypt), internal CAs, and cloud certificate services. Must be installed as a Helm chart or operator. [FACT] "By combining ExternalDNS, Ingress, and Cert-Manager, you can fully automate the setup of public DNS and TLS for Kubernetes workloads."
URL: https://januschung.github.io/blog/2025/05/30/automated-tls-and-dns-in-kubernetes-with-externaldns-ingress-and-lets-encrypt/

Known operational issue: "A potential conflict between external-dns and cert-manager where external-dns attempts to create records for hosts defined in internal cert-manager resources and fails to do so, stopping the external-dns process early."
URL: https://januschung.github.io/blog/2025/05/30/automated-tls-and-dns-in-kubernetes-with-externaldns-ingress-and-lets-encrypt/

### 4.2 external-dns

Synchronizes Kubernetes Ingress and Service resources to external DNS providers (Route 53, Azure DNS, Cloud DNS). Not managed by any cloud provider as a built-in add-on.

### 4.3 ingress-nginx

The community ingress controller (kubernetes/ingress-nginx) is not a managed service on any cloud. ISVs must deploy, configure, and upgrade it. Supports:

- Per-service routing rules via Ingress spec host/path matching
- TLS termination via Kubernetes Secrets (typically populated by cert-manager)
- [Canary routing via annotations](https://kubernetes.github.io/ingress-nginx/examples/canary/): `nginx.ingress.kubernetes.io/canary: "true"`, `canary-weight`, `canary-by-header`, `canary-by-cookie`

[FACT] "Canary rules are evaluated in order of precedence: canary-by-header → canary-by-cookie → canary-weight."
URL: https://kubernetes.github.io/ingress-nginx/examples/canary/

### 4.4 Prometheus Stack (kube-prometheus-stack)

The standard observability stack (Prometheus, Alertmanager, Grafana, node-exporter, kube-state-metrics) is a multi-component Helm chart that ISVs must self-manage. Cloud providers offer managed alternatives (Amazon Managed Prometheus/Grafana, Azure Managed Prometheus, Google Cloud Managed Service for Prometheus), but migration from self-hosted to cloud-managed requires significant reconfiguration.

### 4.5 Add-On Upgrade Surface

[QUOTE] "You must constantly manage updates to maintain security and stability across Kubernetes core, which now releases three times yearly, plus independent add-ons like CoreDNS and CNI components."
URL: https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/

---

## 5. GPU Support on Managed Kubernetes

### 5.1 GPU Node Pools

All three platforms support GPU-enabled node pools using NVIDIA hardware:

| Platform | GPU Instance Types | MIG Support | Notes |
|----------|--------------------|-------------|-------|
| EKS | G4, G5, P3, P4, P5 instances | A100, H100 via MIG Manager | [NVIDIA GPU Operator manages driver + device plugin](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/amazon-eks.html) |
| AKS | NC-series, ND-series (H100, A100) | Standard_NC40ads_H100_v5, ND96isr_H100_v5, A100 VM sizes | [MIG profile set at node pool creation; cannot change at runtime](https://learn.microsoft.com/en-us/azure/aks/gpu-multi-instance) |
| GKE | A100, H100, L4, T4 | A100, H100 MIG partitioning | Nodes labeled automatically per MIG profile |

### 5.2 NVIDIA Device Plugin and GPU Operator

The NVIDIA GPU Operator automates the entire GPU software stack on Kubernetes nodes:

[FACT] "The NVIDIA GPU Operator manages upgrades of the driver and other software components including the NVIDIA device plugin, NVIDIA Container Toolkit, and NVIDIA MIG Manager."
URL: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/amazon-eks.html

On EKS and GKE, the GPU Operator is the recommended installation path. On AKS, [Azure Linux managed AKS now provides built-in GPU features](https://blog.aks.azure.com/2025/11/18/azure-linux-gpu-on-aks) including MIG support and built-in GPU metrics in Azure Managed Prometheus and Grafana (as of November 2025).

### 5.3 Multi-Instance GPU (MIG)

[FACT] "NVIDIA's Multi-Instance GPU (MIG) technology enables a single GPU, such as an A100 or H100, to be split into several GPU instances, with each instance behaving like a standalone GPU with its own memory, cache, and compute cores."
URL: https://www.nvidia.com/en-us/technologies/multi-instance-gpu/

[STATISTIC] "MIG can partition the GPU into as many as seven instances, each fully isolated with its own high-bandwidth memory, cache, and cache cores."
URL: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/

[FACT] "By using the smallest MIG profile, 1g.5gb, the A100 can be partitioned into seven GPU instances."
URL: https://aws.amazon.com/blogs/containers/maximizing-gpu-utilization-with-nvidias-multi-instance-gpu-mig-on-amazon-eks-running-more-pods-per-gpu-for-enhanced-performance/

AKS operational constraint: "Multi-Instance GPU (MIG) profiles must be set when you create the node pool and you cannot change the profile at run time."
URL: https://learn.microsoft.com/en-us/azure/aks/gpu-multi-instance

### 5.4 GPU Scheduling

With the device plugin installed, workloads request GPU resources via standard Kubernetes resource requests:

```yaml
resources:
  limits:
    nvidia.com/gpu: 1        # whole GPU
    nvidia.com/mig-1g.10gb: 1  # MIG slice (H100)
```

[FACT] "90% of teams expect their AI workloads on K8s to grow in the next 12 months."
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

---

## 6. Cost Structure

### 6.1 Control Plane Costs

| Provider | Control Plane Cost | Per Month (1 cluster) | Source |
|----------|-------------------|-----------------------|--------|
| EKS | $0.10/hour per cluster | ~$72/month | [AWS EKS Pricing](https://aws.amazon.com/eks/pricing/) |
| AKS | Free | $0 | [Sedai](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke) |
| GKE Standard (zonal) | Free (first cluster) | $0 | [Sedai](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke) |
| GKE Standard (regional) | $0.10/hour per cluster | ~$72/month | [Sedai](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke) |
| GKE Autopilot | Free | $0 (billed per pod) | [Sedai](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke) |

### 6.2 Node / Compute Costs

| Provider | Entry-Level Node | Notes |
|----------|-----------------|-------|
| EKS | $0.0126/hour (t2.micro) to $13.338/hour (large compute) | EC2 on-demand pricing; Spot instances available |
| AKS | $0.008/hour (basic instances) | Azure VM pricing |
| GKE | $0.010/hour (general purpose) | GCE pricing |

URL: https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke

### 6.3 Data Transfer / Egress Costs

| Provider | Outbound Egress Rate |
|----------|---------------------|
| EKS | $0.09/GB |
| AKS | $0.087/GB |
| GKE | $0.085/GB |

URL: https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke

### 6.4 Storage Costs

| Provider | General Purpose SSD |
|----------|---------------------|
| EKS (EBS gp3) | $0.10/GB/month |
| GKE (Persistent Disk) | $0.04/GB/month |
| AKS (Azure Disk) | Mid-range |

URL: https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke

### 6.5 Estimated Total Cost at Scale

[STATISTIC] "For enterprise-scale deployments: EKS ~$10,000+/month; AKS ~$9,000+/month (most cost-efficient); GKE ~$10,000+/month."
URL: https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke

[FACT] AKS offers the most competitive pricing across deployment sizes due to its free control plane and lower VM base pricing.
URL: https://intercept.cloud/en-gb/blogs/kubernetes-cost-eks-vs-aks-vs-gke

---

## 7. Multi-Cluster Management

### 7.1 The Multi-Cluster Reality

[STATISTIC] Enterprises at scale are "running more than 20 clusters and more than 1,000 nodes across five-plus clouds and environments."
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

[STATISTIC] 68% of surveyed enterprises already operate the majority of their application estate on Kubernetes.
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

[QUOTE] "Over 50% admit their clusters are 'snowflakes' requiring highly manual operations."
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

No managed K8s provider includes a production-grade multi-cluster management plane. ISVs must deploy and operate third-party tooling.

### 7.2 GitOps: ArgoCD and Flux

**ArgoCD** uses a declarative, Git-based model. The hub-and-spoke architecture places a single ArgoCD instance on a central cluster (hub) that manages all remote clusters (spokes). "This topology provides platform teams with a single pane of glass to orchestrate deployments across an entire fleet of clusters — whether they're in different regions, accounts, or have private Kubernetes API endpoints."
URL: https://aws.amazon.com/blogs/containers/deep-dive-streamlining-gitops-with-amazon-eks-capability-for-argo-cd/

**ArgoCD Agent (2025):** A newer agent-based architecture where "lightweight agents reach back to a central hub" rather than requiring the hub to reach into remote clusters. This eliminates the need for VPC peering, Transit Gateways, or complex IAM role chaining between clusters.
URL: https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops

**Flux** is a GitOps controller that continuously reconciles cluster state against Git. Unlike ArgoCD's dashboard-centric model, Flux is purely controller-based.

GKE provides a fleet-argocd-plugin that "automatically imports GKE Fleet cluster lists into Argo CD and maintaining synchronized cluster information."
URL: https://cloud.google.com/blog/products/containers-kubernetes/building-a-fleet-with-argocd-and-gke

### 7.3 Cross-Cluster Networking

No managed K8s platform provides built-in cross-cluster networking. Options include:

- **VPC peering / VNet peering**: Cloud-native L3 connectivity between cluster VPCs; requires ISV configuration
- **Service mesh federation** (Istio multi-cluster, Linkerd multi-cluster): See [F55: Service Mesh Details]
- **Submariner** (CNCF): Open-source cross-cluster network connectivity
- **Network tunnels** (inlets, Cloudflare Tunnel): For clusters without mutual API server access

### 7.4 Fleet Management Staffing

[FACT] "Using Kubernetes Operators that automate operational tasks enables managing hundreds of clusters with just one FTE" — though this represents an optimistic ceiling achievable only with significant prior automation investment.
URL: https://atmosly.com/blog/best-kubernetes-management-platforms-in-2025-top-15-compared

[FACT] "Open-source platforms have free software but infrastructure costs of $5-10k/year plus 1-2 FTE for operations ($120k-280k total)."
URL: https://atmosly.com/blog/best-kubernetes-management-platforms-in-2025-top-15-compared

---

## 8. Per-Service Infrastructure on Managed Kubernetes

### 8.1 Health-Check Endpoints: Liveness, Readiness, and Startup Probes

Kubernetes provides three probe types that every service must configure individually:

- **Liveness probe:** Determines if a container should be restarted. Failure triggers pod restart.
- **Readiness probe:** Determines if a container is ready to receive traffic. Failure removes the pod from Service endpoints (no restart). [FACT] "Readiness probes should be more comprehensive than liveness probes and verify that all the components your application depends on are available and functioning, including checking database connections, cache availability, or confirming that specific application features are working correctly."
  URL: https://betterstack.com/community/guides/monitoring/kubernetes-health-checks/
- **Startup probe:** Delays liveness/readiness evaluation until application initialization completes. Essential for slow-starting services.

**Integration with ingress and load balancers:**

[FACT] "Each backend service in Kubernetes Ingress corresponds to a Kubernetes Service and must reference a health check, with load balancer health checks being specified per backend service."
URL: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress-health-checks

[FACT] "The health check is different from a Kubernetes liveness or readiness probe because the health check is implemented outside of the cluster."
URL: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress-health-checks

On GKE, the ingress controller infers health check parameters from Pod readiness probe attributes when a BackendConfig CRD is not explicitly specified.
URL: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress-health-checks

On AKS with AGIC, health probes are configured via Ingress annotations or the Pod's defined health endpoints.
URL: https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-add-health-probes

**Best practice:** "Liveness probes and readiness probes should be different and independent (or at least with different timeout values)."
URL: https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/probes-checks.html

### 8.2 Service Registry: Kubernetes DNS-Based Service Discovery

Kubernetes uses **CoreDNS** as the default cluster DNS server. CoreDNS replaced kube-dns as the default DNS provider and is now managed as a versioned add-on by all three cloud providers.

[FACT] "CoreDNS facilitates service discovery by automatically updating DNS records as services and pods are added, removed, or modified within the cluster. This dynamic updating ensures that applications can consistently locate the services they depend on, even in a rapidly changing environment."
URL: https://kubernetes.io/docs/tasks/administer-cluster/coredns/

**Service DNS patterns on managed K8s:**

| Service Type | DNS Pattern | Use Case |
|-------------|------------|----------|
| ClusterIP | `<service>.<namespace>.svc.cluster.local` | Standard internal service-to-service |
| Headless | `<pod>.<service>.<namespace>.svc.cluster.local` | Returns all pod IPs; stateful workloads |
| ExternalName | Maps to external CNAME | Routing to cloud-managed databases, external APIs |

[FACT] "Unlike regular services that use a single virtual IP for load balancing, headless services do not have an allocated virtual IP, allowing direct access to each pod's IP. This is particularly beneficial for stateful applications that require persistent connections to specific pods."
URL: https://last9.io/blog/kubernetes-service-discovery/

**Cloud-native alternative — Cloud DNS for GKE:** GKE offers Cloud DNS as a replacement for cluster-hosted CoreDNS. "Cloud DNS provides Pod and Service DNS resolution without a cluster-hosted DNS provider like kube-dns. The Cloud DNS controller automatically provisions DNS records for pods and services in Cloud DNS."
URL: https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery

**vs. Cloud-native service registries:** Cloud Map (AWS), Azure Service Registry, and Dapr's service discovery abstraction provide managed service registries that do not require running a DNS server inside the cluster, eliminating CoreDNS as an operational dependency.

### 8.3 Load Balancer and Ingress

**Ingress-nginx canary routing** is configured entirely via annotations, with no GUI or managed service:

```yaml
nginx.ingress.kubernetes.io/canary: "true"
nginx.ingress.kubernetes.io/canary-weight: "10"        # 10% of traffic to canary
nginx.ingress.kubernetes.io/canary-by-header: "X-Canary"
nginx.ingress.kubernetes.io/canary-by-cookie: "canary"
```

[FACT] "Canary rules are evaluated in order of precedence: canary-by-header → canary-by-cookie → canary-weight."
URL: https://kubernetes.github.io/ingress-nginx/examples/canary/

**TLS termination:** Ingress controllers handle TLS decryption at the cluster edge. [FACT] "SSL/TLS termination secures traffic by decrypting it at the Ingress controller, requiring a TLS certificate stored as a Kubernetes secret."
URL: https://kubernetes.github.io/ingress-nginx/examples/tls-termination/

**Cloud-provider ingress controllers** (ALB/NLB Controller on EKS, AGIC on AKS, GKE Gateway Controller) provision cloud load balancers per-Ingress resource. This avoids running ingress-nginx but creates per-service LB costs ($15–25/month per ALB on AWS) and tighter cloud-provider lock-in.

### 8.4 Container Image Lifecycle

**Registry integration per platform:**

| Platform | Native Registry | Auth Mechanism |
|----------|----------------|----------------|
| EKS | Amazon ECR | IRSA-based IAM roles for pod-level ECR pull |
| AKS | Azure Container Registry (ACR) | AcrPull role assigned to managed identity of agent pool |
| GKE | Artifact Registry | Workload Identity Federation; node SA has reader access |

[FACT] "The AKS to ACR integration assigns the AcrPull role to the Microsoft Entra ID managed identity associated with the agent pool in your AKS cluster."
URL: https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration

**Image pull policies:**

- `Always`: kubelet pulls image on every pod start (ensures latest; increases startup latency)
- `IfNotPresent`: Uses cached image if tag exists on node (default for non-`:latest` tags)
- `Never`: Never pulls; image must pre-exist on node

**Admission controllers for image verification:**

[FACT] "The AlwaysPullImages admission controller can be enabled, and Kubernetes admission controllers such as Kyverno can be used to verify attestations. Additionally, there are third-party admission controllers that mutate Pods when they are created, so that the running workload is defined based on an image digest rather than a tag."
URL: https://aws.github.io/aws-eks-best-practices/security/docs/image/

**Image lifecycle risk:** [FACT] "If the image for a long running application is purged from ECR, it can cause image pull errors when the application is redeployed or scaled horizontally. When using image lifecycle policies, be sure you have good CI/CD practices in place to keep deployments and the images that they reference up to date."
URL: https://aws.github.io/aws-eks-best-practices/security/docs/image/

---

## 9. Gaps vs. Cloud-Native: What Managed K8s Cannot Provide

| Capability | Managed K8s | Cloud-Native Equivalent |
|-----------|-------------|------------------------|
| **Zero-ops scaling to zero** | Requires Knative or KEDA add-on; not built-in | Lambda, Azure Functions, Cloud Run — native scale-to-zero |
| **Managed stateful services** | PVCs + StatefulSets with ISV-managed backups | RDS, Cosmos DB, Cloud Spanner — fully managed |
| **Built-in distributed tracing** | Must install Jaeger/Tempo + OpenTelemetry Collector | CloudWatch X-Ray, Azure Monitor, Cloud Trace — native |
| **Serverless container billing** | Fargate (EKS), Virtual Nodes (AKS), Autopilot (GKE) — partial | Cloud Run, Azure Container Apps — per-request billing |
| **Fully managed ingress / API gateway** | ISV installs and operates ingress controller | API Gateway (AWS), APIM (Azure), Cloud Endpoints (GCP) |
| **Zero cluster upgrade burden** | ISV must still plan, test, and execute node upgrades | No cluster version concept |
| **Built-in secrets management** | Secrets Stores CSI driver + external secret operator required | AWS Secrets Manager, Azure Key Vault, Secret Manager — native |

[FACT] "Knative features autoscaling to zero to minimize infrastructure waste." Knative graduated from the CNCF in October 2025.
URL: https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/

[FACT] "Integrating Kubernetes and Serverless requires skilled teams who can design workflows, manage observability, and ensure security across platforms, as monitoring distributed systems across multiple environments can be complex."
URL: https://blog.eduonix.com/2025/09/kubernetes-vs-serverless-finding-the-right-hybrid-architecture/

---

## 10. Talent and Staffing

[QUOTE] "The percentage of technologists who have genuinely deep, real-world experience running Kubernetes in a production environment is small," creating both scarcity and elevated salary expectations for qualified operators.
URL: https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/

[STATISTIC] Survey of 455 respondents (engineers, architects, executives): "four in five claim a mature platform-engineering function," yet "over 50% admit their clusters are 'snowflakes' requiring highly manual operations."
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

**ISV FTE summary (managed K8s, mid-scale ISV, 3–5 clusters, 50 enterprise customers):**

| Function | Est. FTE | On-Call Burden |
|----------|----------|----------------|
| Cluster lifecycle & upgrades | 0.25–0.5 | Low (scheduled) |
| Add-on management | 0.25–0.5 | Low |
| RBAC, network policy, namespace governance | 0.25–0.5 | Low |
| Ingress / TLS / DNS | 0.25 | Medium |
| Observability stack (Prometheus/Grafana) | 0.25 | Medium |
| GPU node pool management | 0.25–0.5 | Medium–High |
| Multi-cluster GitOps | 0.25–0.5 | Medium |
| **Total** | **1.0–2.5 FTE** | **0.5–1.0 FTE on-call** |

[UNVERIFIED] FTE estimates are author-derived from practitioner accounts and vendor case studies. No single peer-reviewed benchmarking study exists for managed K8s staffing at ISV scale as of February 2026. The Spectro Cloud 2025 report (455 respondents) and the CNCF 2025 practitioner blog are the closest available T1/T2 corroborating sources.

---

## Key Takeaways

- **The "managed" label covers only the control plane.** EKS, AKS, and GKE relieve ISVs of operating the API server, etcd, and scheduler — but leave the entire workload layer (ingress, service mesh, RBAC, network policy, observability, add-ons, cluster upgrades) as ISV responsibility. A realistic managed K8s deployment requires 1.0–2.5 dedicated platform engineering FTE.

- **Version lifecycle is the largest recurring operational risk.** Kubernetes releases three minor versions per year; each cloud provider's standard support window is 12–14 months. ISVs that fall behind accumulate technical debt that compounds into high-risk multi-version jump upgrades under CVE pressure.

- **GPU support on managed K8s is production-ready.** MIG partitioning (up to 7 slices on A100/H100), the NVIDIA GPU Operator, and cloud-provider GPU node pools make managed K8s the leading platform for AI/ML inference workloads — superior to fully cloud-native serverless for workloads requiring GPU access and more manageable than self-hosted for most ISVs.

- **AKS offers the strongest cost profile** due to its free control plane (saving ~$72/month per cluster vs. EKS and regional GKE), but EKS's Karpenter ecosystem (the only cloud-native autoscaler with official K8s maintainer backing) and GKE Autopilot's pod-billed model present valid alternatives depending on workload patterns and existing cloud ecosystem.

- **The gap to cloud-native is real and growing.** Managed K8s cannot match serverless/PaaS for scale-to-zero, fully managed state, zero upgrade burden, or per-request billing economics. Hybrid architectures — managed K8s for stateful/GPU workloads, serverless for event-driven/stateless functions — represent the emerging ISV deployment pattern for 2025–2026.

---

## Related — Out of Scope

- **Portable / self-hosted K8s distributions** (k3s, RKE2, Talos): See [F53: Portable Kubernetes]
- **Kubernetes Operators for stateful workloads** (databases, message queues): See [F54: Kubernetes Operators]
- **Service mesh implementation details** (Istio, Linkerd, Cilium): See [F55: Service Mesh Details]
- **Security posture and compliance scanning** for K8s clusters: Adjacent to F52 but not investigated here

---

## Sources

1. [EKS vs GKE vs AKS: Best Managed Kubernetes Platform (2026) — Atmosly](https://atmosly.com/blog/eks-vs-gke-vs-aks-which-managed-kubernetes-is-best-2025)
2. [What You Get with AKS, EKS, GKE vs. Managed Kubernetes-as-a-Service — Fairwinds](https://www.fairwinds.com/blog/aks-eks-gke-managed-kubernetes-as-a-service)
3. [Kubernetes Pricing 2026: EKS vs AKS vs GKE Comparison Guide — Sedai](https://sedai.io/blog/kubernetes-cost-eks-vs-aks-vs-gke)
4. [The True Cost of Managed Kubernetes — Intercept Cloud](https://intercept.cloud/en-gb/blogs/kubernetes-cost-eks-vs-aks-vs-gke)
5. [Amazon EKS Pricing — AWS Official](https://aws.amazon.com/eks/pricing/)
6. [Understand the Kubernetes version lifecycle on EKS — AWS Docs](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)
7. [AKS Long Term Support: 24-Month Support Announcement — AKS Engineering Blog](https://blog.aks.azure.com/2025/07/25/aks-lts-announcement)
8. [Supported Kubernetes Versions in AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions)
9. [Navigating Capacity Challenges on AKS with Node Auto Provisioning — AKS Engineering Blog](https://blog.aks.azure.com/2025/12/06/node-auto-provisioning-capacity-management)
10. [Fully Managed GPU workloads with Azure Linux on AKS — AKS Engineering Blog](https://blog.aks.azure.com/2025/11/18/azure-linux-gpu-on-aks)
11. [Create a multi-instance GPU node pool in AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/gpu-multi-instance)
12. [NVIDIA GPU Operator with Amazon EKS — NVIDIA Docs](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/amazon-eks.html)
13. [NVIDIA GPU Operator with Azure AKS — NVIDIA Docs](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/microsoft-aks.html)
14. [Multi-Instance GPU (MIG) — NVIDIA](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/)
15. [MIG User Guide — NVIDIA](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/)
16. [Maximizing GPU utilization with NVIDIA MIG on Amazon EKS — AWS Containers Blog](https://aws.amazon.com/blogs/containers/maximizing-gpu-utilization-with-nvidias-multi-instance-gpu-mig-on-amazon-eks-running-more-pods-per-gpu-for-enhanced-performance/)
17. [Running multi-instance GPUs on GKE — Google Cloud Docs](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi)
18. [GKE Autopilot Overview — Google Cloud Docs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
19. [GKE Autopilot vs Standard: TCO Reality Check — KloudStax](https://www.kloudstax.com/blog/raah36imow738cpeik0u15musq0qkp)
20. [About GKE Modes of Operation — Google Cloud Docs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
21. [Scale cluster compute with Karpenter and Cluster Autoscaler — AWS EKS Docs](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html)
22. [Salesforce Migrates 1,000+ EKS Clusters to Karpenter — InfoQ](https://www.infoq.com/news/2026/01/salesforce-eks-karpenter/)
23. [EKS Auto Mode and NodePools Explained — Medium](https://medium.com/@ananthchaitanya17/eks-auto-mode-and-nodepools-explained-whats-new-in-2025-257602b663b3)
24. [EKS Best Practices: Karpenter — AWS](https://aws.github.io/aws-eks-best-practices/karpenter/)
25. [Top 5 Hard-Earned Lessons from Experts on Managing Kubernetes — CNCF Blog](https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/)
26. [Managing Kubernetes in 2025: 7 Pillars — ScaleOps](https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/)
27. [State of Production Kubernetes 2025 — Spectro Cloud](https://www.spectrocloud.com/state-of-kubernetes-2025)
28. [Mastering Kubernetes Fleet Management — Komodor](https://komodor.com/blog/mastering-kubernetes-fleet-management-for-multi-cluster-success/)
29. [Deep dive: Streamlining GitOps with Amazon EKS and Argo CD — AWS Containers Blog](https://aws.amazon.com/blogs/containers/deep-dive-streamlining-gitops-with-amazon-eks-capability-for-argo-cd/)
30. [Multi-cluster GitOps with the Argo CD Agent — Red Hat Blog](https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops)
31. [Building a Fleet with ArgoCD and GKE — Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/building-a-fleet-with-argocd-and-gke)
32. [Argo CD vs Flux CD — Zignuts](https://www.zignuts.com/blog/argo-cd-vs-flux-cd--comparison)
33. [Configure Liveness, Readiness and Startup Probes — Kubernetes Docs](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
34. [Kubernetes Health Checks and Probes — Better Stack](https://betterstack.com/community/guides/monitoring/kubernetes-health-checks/)
35. [Troubleshoot Ingress Health Checks — GKE Docs](https://cloud.google.com/kubernetes-engine/docs/troubleshooting/ingress-health-checks)
36. [Configure Probes and Load Balancer Health Checks — AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/ha-resiliency-amazon-eks-apps/probes-checks.html)
37. [Add Health Probes to AKS Pods — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-add-health-probes)
38. [Kubernetes Service Discovery — Last9](https://last9.io/blog/kubernetes-service-discovery/)
39. [Using CoreDNS for Service Discovery — Kubernetes Docs](https://kubernetes.io/docs/tasks/administer-cluster/coredns/)
40. [Service Discovery and DNS on GKE — Google Cloud Docs](https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery)
41. [Canary Deployments — ingress-nginx Docs](https://kubernetes.github.io/ingress-nginx/examples/canary/)
42. [TLS Termination — ingress-nginx Docs](https://kubernetes.github.io/ingress-nginx/examples/tls-termination/)
43. [Automated TLS and DNS in Kubernetes — Janus Chung Blog](https://januschung.github.io/blog/2025/05/30/automated-tls-and-dns-in-kubernetes-with-externaldns-ingress-and-lets-encrypt/)
44. [Integrate ACR with AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration)
45. [Image Security — EKS Best Practices](https://aws.github.io/aws-eks-best-practices/security/docs/image/)
46. [Kubernetes Image Pull — Kubernetes Docs](https://kubernetes.io/docs/concepts/containers/images/)
47. [Knative Graduation Announcement — CNCF](https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/)
48. [Kubernetes vs Serverless: Finding the Right Hybrid Architecture — Eduonix](https://blog.eduonix.com/2025/09/kubernetes-vs-serverless-finding-the-right-hybrid-architecture/)
49. [Best Kubernetes Management Platforms 2025 — Atmosly](https://atmosly.com/blog/best-kubernetes-management-platforms-in-2025-top-15-compared)
50. [Kubernetes Version Support Across Major Cloud Providers — PerfectScale](https://www.perfectscale.io/blog/kubernetes-version-support-across-major-cloud-providers)
51. [Multi-tenancy Challenges in Public Cloud — D2iQ](https://d2iq.com/blog/key-multi-tenancy-challenges-in-the-public-cloud-and-how-to-solve-for-them-100-11)
52. [Stateful Microservice Migration in Kubernetes — Cloud Native Now](https://cloudnativenow.com/features/stateful-microservice-migration-the-live-state-challenge-in-kubernetes/)
53. [Kubernetes Deployment Strategies — Octopus Deploy](https://octopus.com/devops/kubernetes-deployments/)
