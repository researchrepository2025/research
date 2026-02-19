# F53: Portable Kubernetes for ISV Delivery

**Research Question:** How do portable Kubernetes platforms (OpenShift, Rancher, Tanzu) enable ISVs to deliver software to diverse customer environments, and what are the practical limits and challenges?

---

## Executive Summary

Portable Kubernetes platforms — principally Red Hat OpenShift, SUSE Rancher, and VMware Tanzu (now rebranded as vSphere Kubernetes Service following Broadcom's acquisition) — allow ISVs to ship software to customer-owned infrastructure while targeting a standardized control plane rather than bare hardware. The 2025 CNCF Annual Survey found that [82% of container users run Kubernetes in production](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/), creating strong enterprise pull for K8s-native ISV packaging. However, the practical reality for ISV delivery teams is that customer environments vary enormously across Kubernetes versions, CNI plugins, storage classes, and network policies — and that variability drives significant support, testing, and engineering overhead. Replicated/KOTS has emerged as a dedicated ISV delivery layer that abstracts the worst of this variability for both Helm-based and Operator-based applications. Platform licensing costs — particularly after SUSE's controversial 2025 CPU-based pricing shift — increasingly flow through to ISV pricing models and must be addressed explicitly in commercial strategy. ISVs building for the enterprise on-premises market must choose among three broad paths: certify on the customer's existing platform (OpenShift or Rancher), bundle their own cluster using Replicated Embedded Cluster (built on k0s), or support multiple paths with a compatibility-tested Helm chart library.

---

## 1. Red Hat OpenShift: OCP vs. OKD, Operator Framework, and ISV Certification

### 1.1 OCP vs. OKD

Red Hat ships two variants of OpenShift. OpenShift Container Platform (OCP) is a commercially supported product available via subscription. OKD is the community upstream project. Key differences:

| Attribute | OKD | OCP |
|---|---|---|
| Cost | Free (no subscription) | Paid subscription |
| Operating System | CentOS Stream CoreOS | Red Hat Enterprise Linux CoreOS |
| Support | Community only | Red Hat 24/7 support, SLA |
| Update Cadence | Continuous (community-driven) | Every ~6 months (stabilized minor releases) |
| Operator Ecosystem | OperatorHub community tier | Certified, validated operators |
| ISV Certification | Not eligible | Required for OperatorHub listing |

[FACT] "OKD is a community project whereas Red Hat OpenShift (OCP) is a paid, supported product available via a subscription model." — [Red Hat, OKD vs. OpenShift comparison page](https://www.redhat.com/en/topics/containers/red-hat-openshift-okd)

[FACT] "OKD updates as often as open source developers contribute via git, sometimes as often as several times per week, while Enterprise might update around every six months." — [Red Hat Learning Community, OKD vs OCP](https://learn.redhat.com/t5/Kube-by-Example-KBE/OKD-vs-OCP/td-p/23997)

For ISV delivery purposes, OKD is not a viable commercial target: it lacks the certification pathway, the stable lifecycle, and the enterprise SLAs that corporate customers require. OCP is the target platform.

### 1.2 Operator Framework and ISV Certification Pipeline

Red Hat's certification program for ISV operators requires passing a Tekton-based CI pipeline hosted in the [operator-pipelines GitHub repository](https://github.com/redhat-openshift-ecosystem/operator-pipelines). The pipeline validates an Operator Bundle, installs it onto an OpenShift cluster, and runs preflight checks verifying minimum requirements for Red Hat OpenShift certification.

[FACT] "The Operator CI pipeline is a Tekton pipeline that can be triggered by a partner using on-premise infrastructure, validates an Operator Bundle, builds it and installs it to an OpenShift environment, and after installation, pre-flight tests are executed to validate that the Operator meets minimum requirements for Red Hat OpenShift Certification." — [Red Hat Software Certification 2025 Docs](https://docs.redhat.com/en/documentation/red_hat_software_certification/2025/html-single/red_hat_openshift_software_certification_policy_guide/index)

Operator lifecycle classifications effective from OCP 4.14 onward:
- **Platform Aligned**: Tightly coupled to OpenShift minor version, updated in lockstep
- **Platform Agnostic**: Works across a range of OpenShift versions
- **Rolling Stream**: Continuously updated, not pinned to OpenShift minor release

[FACT] "Red Hat has simplified operator maintenance with three new lifecycle classifications: Platform Aligned, Platform Agnostic, and Rolling Stream, which outline criteria and support timelines that operators should meet." — [OpenShift Operator Life Cycles, Red Hat Customer Portal](https://access.redhat.com/support/policy/updates/openshift_operators)

A significant 2025 development: OLM v1 is adding native Helm support, meaning ISVs will be able to run operators via OLM without creating a full OLM bundle. [FACT] "OLM v1 is adding native support for Helm as a packaging format for controllers, meaning running an Operator via OLM will no longer require creating an OLM bundle." — [Red Hat Developer, Packaging Applications with Kubernetes Operators](https://developers.redhat.com/topics/kubernetes/operators)

### 1.3 OCP Subscription Model and ISV Impact

OCP uses core-pair-based licensing. A core-pair is defined as 2 physical cores or 4 vCPUs. Control plane and infrastructure nodes do not count against subscriptions — only worker nodes matter for licensing purposes.

[FACT] "The core-pair is one of the bases for self-managed OpenShift subscriptions and is defined as 2 physical cores or as 4 virtual central processing units (vCPUs). Control plane nodes and infrastructure nodes do not count for subscriptions." — [Red Hat, Self-Managed OpenShift Subscription Guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide)

[STATISTIC] OCP self-managed subscriptions for six core-pairs with Premium 24/7 SLA range from approximately €12,000–€30,000 per year depending on terms. — [Medium: True Price of OpenShift Success, 2025](https://medium.com/@PlanB./discover-the-true-price-of-openshift-success-estimating-costs-for-your-enterprise-sla-in-2025-e9bbc817c6d7)

For ISVs: customers who already have OCP subscriptions represent a lower-friction deployment target. Customers who do not have OCP subscriptions will incur platform licensing costs in addition to the ISV's own product fees. ISVs must decide whether to require OCP (accessing Red Hat's certified marketplace) or remain platform-agnostic.

---

## 2. Rancher (SUSE): Multi-Cluster Management, RKE2, and Customer Self-Service

### 2.1 Rancher Prime and RKE2 Architecture

SUSE Rancher Prime is the enterprise subscription tier of the Rancher multi-cluster Kubernetes management platform. Rancher manages both self-provisioned clusters (using RKE2 or K3s) and imported third-party clusters.

[FACT] "Rancher is often referred to as a multi-cluster Kubernetes management solution and is a centralized administrative hub with a user accessible interface through GUIs, CLIs and APIs. A key strength of Rancher is the ability to provision new Kubernetes clusters using various engines like Rancher Kubernetes Engine (RKE), RKE2 and K3s and also the ability to import existing Kubernetes clusters regardless of the underlying provider." — [Baytech Consulting, Rancher Enterprise Kubernetes Management 2025](https://www.baytechconsulting.com/blog/rancher-enterprise-kubernetes-management-2025)

RKE2 is SUSE's security-hardened Kubernetes distribution. Key RKE2 characteristics relevant to ISV delivery:
- FIPS 140-2 compliant by default
- CIS Kubernetes Benchmark hardened
- Designed for U.S. Federal Government requirements but increasingly used in regulated enterprise sectors
- Fully CNCF conformant

[FACT] "RKE2 is Rancher's enterprise-ready next-generation Kubernetes distribution. It is a fully conformant Kubernetes distribution that focuses on security and compliance within the U.S. Federal Government sector." — [RKE2 Documentation](https://docs.rke2.io/)

### 2.2 Fleet: GitOps at Scale for ISV Software Distribution

Rancher's Fleet component enables GitOps-based workload deployment across hundreds to thousands of clusters from a central hub.

[FACT] "Fleet is GitOps and HelmOps at scale, designed to manage multiple clusters. Fleet can manage deployments from git of raw Kubernetes YAML, Helm charts, or Kustomize or any combination of the three." — [Rancher Fleet Overview](https://ranchermanager.docs.rancher.com/integrations-in-rancher/fleet/overview)

[FACT] "Fleet is designed to provide management for GitOps for a single Kubernetes cluster, or for large-scale deployments of Kubernetes clusters (up to one million)." — [Rancher Fleet Core Concepts](https://fleet.rancher.io/concepts)

For ISVs whose enterprise customers use Rancher: Fleet is how those customers will likely expect to receive and manage application updates. ISVs should ensure their Helm charts are Fleet-compatible (Fleet supports standard Helm) and provide release channel guidance for Fleet's `GitRepo` targeting mechanism.

### 2.3 SUSE Rancher Pricing Disruption (2025)

SUSE's 2025 pricing change from node-based to CPU/vCPU-based licensing caused severe market disruption with direct ISV implications.

[FACT] "SUSE's new CPU/vCPU-based Rancher Prime pricing model (2025) has caused significant, unexpected cost spikes for enterprises — often 4–9× higher than before. Previously, Rancher licensing was based on one license per node with most enterprises paying roughly $2,000 per node annually for standard support." — [Portainer Blog: SUSE Rancher Price Hike, 2025](https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025)

[STATISTIC] Concrete example of pricing increase: "A 16-core VM (32 vCPUs) that previously cost $2,000/year now requires eight licensing units, totaling approximately $19,200/year for standard support." — [Portainer Blog, 2025](https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025)

[STATISTIC] SUSE Rancher Prime pricing tiers range from $7,594.99 to $41,830.99 annually. — [TrustRadius, SUSE Rancher Pricing 2026](https://www.trustradius.com/products/suse-rancher/pricing)

[FACT] "Search volume for 'Rancher alternatives,' 'Rancher pricing increase,' and related terms has skyrocketed in 2025." — [Portainer Blog, 2025](https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025)

ISV implication: ISVs whose delivery model depends on Rancher-managed customer clusters face two risks — customers migrating away from Rancher (disrupting the expected base), and customers' platform costs rising, increasing total cost of ownership pressure on the ISV's own product.

---

## 3. VMware Tanzu / vSphere Kubernetes Service: Enterprise Customer Fit

### 3.1 Broadcom Acquisition and Rebranding

Following Broadcom's acquisition of VMware, the Tanzu Kubernetes Grid (TKG) brand has been retired within the VMware Cloud Foundation (VCF) stack.

[FACT] "The VMware Tanzu Kubernetes Grid Service and Tanzu Kubernetes were rebranded in early March as the VMware vSphere Kubernetes Service (VKS) and vSphere Kubernetes release (VKr), respectively." — [VMware Cloud Foundation Blog, March 4, 2025](https://blogs.vmware.com/cloud-foundation/2025/03/04/vmware-vsphere-kubernetes-service-3-3-is-now-ga/)

[FACT] "Tanzu Kubernetes Grid v2.5.4 is the final enterprise release of TKG, and users are advised to consult with their Broadcom account team about migrating workloads to vSphere Supervisor and vSphere Kubernetes Service (VKS — formerly known as TKG Service)." — [Broadcom TKG v2.5.x Release Notes](https://techdocs.broadcom.com/us/en/vmware-tanzu/standalone-components/tanzu-kubernetes-grid/2-5/tkg/mgmt-release-notes.html)

[FACT] "The TanzuKubernetesCluster API will be removed no sooner than June 2025. Cluster API is now the default method for bootstrapping, configuring, and managing Kubernetes clusters, replacing TanzuKubernetesCluster API." — [TechTarget, Broadcom VMware Hardens vDefend, 2025](https://www.techtarget.com/searchdatacenter/news/366621962/Broadcom-VMware-hardens-vDefend-drops-Tanzu-branding-in-VCF)

### 3.2 ISV Fit Assessment

Tanzu/VKS is tightly integrated with vSphere and VMware Cloud Foundation. The customer profile for VKS is large enterprises already committed to VMware's virtualization stack. This creates a well-defined but narrow ISV target.

[FACT] "Many existing Tanzu customers use other versions of the Kubernetes runtime to meet specific requirements, and Tanzu will continue to support these versions, but Tanzu Platform is designed to run on any CNCF conformant Kubernetes runtime." — [TechTarget, VMware Tanzu Integration, 2025](https://www.techtarget.com/searchitoperations/news/366608899/VMware-Tanzu-hones-integration-but-faces-Broadcom-backlash)

For ISVs: VKS targets the vSphere installed base, not the general enterprise. If customers are VMware-heavy, VKS/Tanzu is a relevant certification target. However, the naming transition and API migration requirements mean that ISV documentation and support runbooks built for TKG need active refresh against VKS 3.3+ APIs.

TKG operated the N-2 Lifecycle Policy (latest minor release plus two preceding minor releases supported, minimum 12-month support duration). VKS inherits a similar lifecycle. ISVs must track which TKG/VKS versions their software supports and communicate a clear EOL timeline for each.

[FACT] "Tanzu Kubernetes Grid operates the N-2 Lifecycle Policy, wherein the latest minor release and the two minor releases that immediately precede it are supported, with a minimum support duration of 12 months." — [NetApp TKG Overview](https://docs.netapp.com/us-en/netapp-solutions/containers/vtwn_overview_tkg.html)

---

## 4. Replicated/KOTS: Application Packaging and Delivery Platform

Replicated has become the de facto standard ISV delivery layer for commercial Kubernetes software shipped to customer-controlled environments. It abstracts the complexity of diverse K8s environments behind a managed packaging and delivery system.

### 4.1 KOTS: Core Capabilities

KOTS (Kubernetes Off-The-Shelf) is a kubectl plugin and in-cluster Admin Console.

[FACT] "KOTS is a kubectl plugin and an in-cluster Admin Console that provides highly successful installations of Helm charts and Kubernetes applications into customer-controlled environments, including on-prem and air gap environments." — [Replicated KOTS Introduction](https://docs.replicated.com/intro-kots)

Key KOTS capabilities for ISV delivery:
- **Preflight checks**: Validates customer environment meets minimum requirements before installation
- **Air-gap bundles**: Full offline installation bundles downloadable from vendor portal, uploadable via browser or CLI
- **License enforcement**: Customers sync licenses through KOTS; ISVs can require license validation before updates proceed
- **Required releases**: ISVs can mark specific releases as required, preventing customers from skipping critical updates
- **Instance telemetry**: Reports installed version and environment data back to vendor
- **Admin Console**: GUI for customer operations teams — status, updates, configuration

[FACT] September 2025 KOTS release highlights include: "VM network policy controls (beta), Kubernetes 1.33 and SELinux support in Embedded Cluster, smarter updates in KOTS, and registry/SCIM improvements in Vendor Portal." — [Replicated Blog](https://www.replicated.com/blog)

### 4.2 Embedded Cluster: Bundled Kubernetes for Simplified On-Premises Delivery

Replicated Embedded Cluster allows ISVs to ship a K8s distribution alongside their application as a single appliance-style artifact.

[FACT] Embedded Cluster is built on k0s as its underlying Kubernetes distribution and automatically deploys KOTS Admin Console, OpenEBS for persistent storage, Velero for disaster recovery (optional), and an image registry for air-gapped environments. — [Replicated Embedded Cluster Overview](https://docs.replicated.com/vendor/embedded-overview)

[FACT] "Cluster updates are done automatically at the same time as application updates," eliminating separate cluster version management for customers. — [Replicated Embedded Cluster Overview](https://docs.replicated.com/vendor/embedded-overview)

[FACT] "Distributing self-hosted enterprise applications in the most secure environments (airgap, VPC, on-prem) is a complex task, and requiring customers bring Kubernetes works some of the time, but more often than not creates its own set of unique challenges. By embedding Kubernetes in the application, ISVs can have customers just provide a VM or bare metal and remove complex requirements." — [Replicated, Deploy Self-Hosted Kubernetes Apps](https://www.replicated.com/embedded-cluster)

### 4.3 Compatibility Matrix: Cross-Environment Testing Infrastructure

[STATISTIC] The Replicated Compatibility Matrix (CMX) supports testing across 65,981+ unique configuration combinations spanning EKS, AKS, GKE, OpenShift, RKE2, kind, k3s, and kURL. — [Replicated Compatibility Matrix](https://www.replicated.com/compatibility-matrix)

[FACT] "Most clusters provision in under 3 minutes using warm pools of pre-built environments." — [Replicated Compatibility Matrix](https://www.replicated.com/compatibility-matrix)

[FACT] One customer reported: "A single cluster running in Azure just to run integration tests used to cost us between 6...7...8,000 euros a month," whereas the CMX charges only for seconds used. — [Replicated Compatibility Matrix](https://www.replicated.com/compatibility-matrix)

The CMX uses telemetry from the Replicated SDK to identify which environments customers actually use, enabling ISVs to focus testing on real-world adoption distributions rather than theoretical combinations.

---

## 5. Customer Environment Variability: The Core ISV Delivery Challenge

### 5.1 Kubernetes Version Diversity

Kubernetes releases a new minor version every four months. Each managed K8s service (EKS, AKS, GKE) maintains roughly N-2 or N-3 supported versions. Self-managed customer clusters may lag further.

[FACT] Starting from Kubernetes version 1.28, the Kubernetes skew policy allows control plane nodes to be up to three versions ahead of worker nodes. — [Kubernetes Version Skew Policy](https://kubernetes.io/releases/version-skew-policy/)

[FACT] As of Helm 4, Helm is assumed compatible with N-3 versions of Kubernetes it was compiled against. — [Helm Version Support Policy](https://helm.sh/docs/topics/version_skew/)

ISV practical implication: An ISV supporting a 12-month-old enterprise customer deployment may be dealing with Kubernetes versions 1.28–1.30 while current release is 1.33. The ISV's support matrix must be explicit: "We support Kubernetes 1.29 through 1.33," and this range must be actively tested.

### 5.2 CNI Plugin Incompatibilities

CNI (Container Network Interface) plugins — Calico, Cilium, Flannel, Weave, Antrea — expose different network APIs, security models, and IP address management behaviors. ISV applications that use network policies, service mesh features, or rely on specific IP range assumptions can break across CNI variations.

[FACT] "Maintaining compatibility between your CNI plugin, Kubernetes version, and other cluster components is vital for stability, as upgrading Kubernetes or related components without considering CNI compatibility can lead to network disruptions." — [Plural.sh, Kubernetes CNI Guide 2025](https://www.plural.sh/blog/kubernetes-cni-guide/)

[FACT] "A simple plugin like Flannel might introduce performance overhead as the number of pods increases, while other CNIs like Calico or Cilium offer more scalable architectures but introduce additional complexity." — [Plural.sh, Kubernetes CNI Guide 2025](https://www.plural.sh/blog/kubernetes-cni-guide/)

### 5.3 Storage Class Variability

Customer clusters expose different storage classes (ceph-rbd, longhorn, nfs-client, local-path, aws-ebs, azure-disk, vsphere-volume) with different access modes, performance tiers, and reclaim policies. ISV applications requiring persistent storage must either document supported storage classes explicitly or implement dynamic detection logic.

[UNVERIFIED] ISVs frequently discover storage class incompatibilities only at customer install time rather than in pre-sales, because customers often do not know which storage classes they have available until asked. This is a T3 community observation not currently backed by a specific T1/T2 source from 2025; however, the Replicated Compatibility Matrix product's existence (testing storage configurations pre-deployment) corroborates the underlying problem.

### 5.4 Air-Gapped Cluster Requirements

[FACT] "An air-gapped environment is cut off from the public internet and other external networks which means a developer faces many challenges. Air-gapped systems' isolation presents challenges in a Kubernetes environment that was designed to be networked." — [Cloud Native Now, Overcoming Challenges of Air-Gapped Kubernetes](https://cloudnativenow.com/features/overcoming-challenges-of-air-gapped-kubernetes/)

[FACT] "The configuration is hidden deep in the container runtime; you need to have a deep understanding of Kubernetes to manage air-gapped clusters successfully." — [Cloud Native Now, Overcoming Challenges of Air-Gapped Kubernetes](https://cloudnativenow.com/features/overcoming-challenges-of-air-gapped-kubernetes/)

ISV air-gap requirements checklist:
1. All container images bundled into a self-contained archive with versioned manifests
2. Helm charts embedded (not fetched from chart repositories at install time)
3. Operator bundle images included in the air-gap bundle
4. Documentation available offline (PDF or bundled HTML)
5. Update mechanism that transfers a new bundle via physical media or internal file server — not internet pull

[FACT] "For air gap installations, the Embedded Cluster installation assets include an air gap bundle containing images needed for environments with limited or no outbound internet access. New air gap bundles can be uploaded to the Admin Console from the browser or with the Embedded Cluster binary from the command line." — [Replicated Embedded Cluster Release Notes](https://docs.replicated.com/release-notes/rn-embedded-cluster)

---

## 6. Application Packaging: Helm, Kustomize, and Operators — ISV Trade-offs

### 6.1 Helm Charts

Helm is the dominant packaging format for distributing K8s applications. Its key ISV advantages: versioning via chart version and appVersion fields, rollback with `helm rollback`, templating for environment-specific values, and broad ecosystem support.

[FACT] "Helm cuts deployment time to 45 seconds versus 180 seconds for raw YAML, a 75% speedup, thanks to pre-rendered templates." — [Johal.in, Helm Charts for Kubernetes 2025](https://johal.in/helm-charts-for-kubernetes-packaging-ai-models-for-helm-based-deployments-2025/)

[FACT] Helm 4, released in 2025, "marks Helm's 10th anniversary under the guidance of the Cloud Native Computing Foundation (CNCF), aiming to address several challenges around scalability, security, and developer workflow." — [InfoQ, Helm 4 Release 2025](https://www.infoq.com/news/2025/11/helm-4/)

Critical ISV limitation with Helm: CRD management. [FACT] "Helm still does not upgrade or delete CRDs through its normal upgrade process." — [InfoQ, Helm 4 Release, 2025](https://www.infoq.com/news/2025/11/helm-4/) This means ISVs shipping applications that define Custom Resource Definitions must handle CRD upgrades out-of-band, via init containers, pre-upgrade hooks, or an operator.

### 6.2 Kustomize

Kustomize provides configuration layering without templating. It is built into `kubectl` and preferred for environment-specific overlays rather than full application packaging.

[FACT] "Helm treats applications like packages that need lifecycle management, while Kustomize treats them like configurations that need environment-specific tweaks." — [Justin Polidori, Helm vs Kustomize 2025](https://justinpolidori.com/posts/20250815_helm_kustomize/)

For ISV distribution, Kustomize alone is insufficient for commercial delivery because it lacks version management, release channels, and rollback history. The recommended pattern is: Helm for packaging and release management, Kustomize for customer-site environment overlays.

### 6.3 Operators

Kubernetes Operators are the most powerful packaging model but carry the highest development and maintenance cost. Operators encode domain-specific operational knowledge (backup, scaling, failover, schema migration) as Kubernetes controllers.

[FACT] "Operators might supplant Helm as a way of deploying 'packaged' applications from ISVs. If you're an ISV or hardware vendor, you should learn not only operators but how to package for the OLM (Operator Lifecycle Manager)." — [Helm Charts for Kubernetes 2025](https://johal.in/helm-charts-for-kubernetes-packaging-ai-models-for-helm-based-deployments-2025/)

[FACT] "Red Hat recommends managing application lifecycle using Kubernetes-native technologies like Operators or Helm charts for close integration with Red Hat OpenShift. For both Operators and Helm charts, certification covers the packaging format and compatibility with Red Hat OpenShift tools." — [Red Hat OpenShift Certification Policy Guide 2025](https://docs.redhat.com/en/documentation/red_hat_software_certification/2025/html-single/red_hat_openshift_software_certification_policy_guide/index)

| Packaging Format | ISV Distribution Fit | OpenShift Certified | Air-Gap Support | CRD Management | Relative Complexity |
|---|---|---|---|---|---|
| Helm Chart | High — broad ecosystem | Yes (via OLM v1 or direct) | Yes (bundle images) | Manual / hooks | Low |
| Kustomize | Low — overlay only | No standalone path | Yes | Manual | Low |
| Operator (OLM) | High for complex apps | Yes (OperatorHub) | Yes (bundle images) | Automated | High |
| Replicated KOTS | High — ISV-specific | Wraps any of the above | Native support | Delegated to inner format | Medium |

---

## 7. Update and Upgrade Logistics

### 7.1 Pushing Updates to Customer-Managed Clusters

For KOTS-based delivery, updates follow a vendor-controlled channel model. The ISV promotes a new release to a channel (e.g., `stable`, `beta`). Customers with KOTS installed receive a notification in the Admin Console and can apply the update with or without auto-approve.

[FACT] "KOTS now tries to automatically refresh metadata (version labels, release notes, and required status) for pending releases in the same channel as the currently deployed version." — [Replicated KOTS Release Notes](https://docs.replicated.com/release-notes/rn-app-manager)

[FACT] "For Embedded Cluster, the workflow for upgrading to newly available versions includes a wizard where the license is synced, config can be edited, and preflight checks are run before deploying." — [Replicated, Performing Updates in Embedded Clusters](https://docs.replicated.com/enterprise/updating-embedded)

For Helm-only delivery without Replicated: the ISV must instruct customers to pull the new chart version and run `helm upgrade`. There is no push mechanism; the ISV has no visibility into which version customers are actually running unless telemetry is separately implemented.

### 7.2 Deployment Strategies

[FACT] There are three major types of Kubernetes Deployment strategies: blue-green, rolling, and canary. "The main advantage of a blue-green Deployment is the instant rollout/rollback. You avoid versioning issues as you change the entire cluster state at once." — [Acecloud.ai, Kubernetes Deployment Strategies](https://acecloud.ai/blog/kubernetes-deployment-strategies/)

[FACT] Kubernetes 1.33 introduced "control-plane minor-version rollback capability, providing a reliable path to revert a control-plane upgrade and fundamentally changing cluster lifecycle management." — [Google Cloud Blog, Kubernetes Minor Version Rollback](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-gets-minor-version-rollback)

### 7.3 Operator Lifecycle Manager (OLM) for Automated Updates

[FACT] "OLM is a component of the Operator Framework that provides rich update mechanisms to keep Kubernetes native applications (called Operators) up to date automatically. The Operator Lifecycle Manager extends Kubernetes with declarative capabilities for installing, managing, and upgrading operators and their dependencies." — [Operator Lifecycle Manager](https://olm.operatorframework.io/)

OLM update channels (alpha, beta, stable) allow ISVs to control upgrade progression. OLM's upgrade graph enforces upgrade paths, preventing customers from jumping from version 1.0 to 3.0 without passing through 2.0 if that is required.

---

## 8. Support Complexity Across Diverse Customer K8s Environments

### 8.1 The Combinatorial Problem

Every unique combination of Kubernetes distribution, version, CNI, storage class, container runtime, and security policy (PSA, OPA, Kyverno) creates a distinct operational environment. Debugging a customer issue requires first reproducing the environment, which may be time-consuming or impossible without tooling.

[STATISTIC] "Nearly 70% of Kubernetes users report that operational complexity is a top pain point, often citing fragmented tooling, inconsistent cluster management, and lack of standardized best practices." — [Baytech Consulting, Scaling Kubernetes in the Enterprise 2025](https://www.baytechconsulting.com/blog/scaling-kubernetes-in-the-enterprise-2025)

[STATISTIC] The Replicated Compatibility Matrix supports 65,981+ unique configuration combinations — reflecting the actual scale of environment diversity ISVs face. — [Replicated Compatibility Matrix](https://www.replicated.com/compatibility-matrix)

### 8.2 Operational Difficulty by Deployment Model

Assumptions: mid-size ISV serving 50 enterprise customers, applications with stateful components, support team of 4–8 engineers.

| Capability Domain | On-Premises (ISV-Managed Cluster) | Managed K8s (Customer EKS/AKS/GKE) | Portable K8s (OCP/Rancher/Tanzu) |
|---|---|---|---|
| **K8s Version Support Matrix** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 4/5 |
| | ISV controls version; customers resist upgrades | Cloud provider enforces supported range | Vendor lifecycle (N-2) reduces range but adds cert requirements |
| | Replicated Embedded Cluster, k0s | EKS/AKS/GKE managed control plane | OCP/RKE2/VKS release channels |
| | Est. FTE: 0.5–1.0 (upgrade management) | Est. FTE: 0.25–0.5 | Est. FTE: 0.5–1.0 (cert maintenance) |
| **CNI / Networking** | Difficulty: 2/5 | Difficulty: 3/5 | Difficulty: 3/5 |
| | ISV selects CNI in Embedded Cluster | Customer CNI varies; ISV cannot control | Customer CNI varies; OCP enforces OVN-Kubernetes |
| | k0s default CNI (kube-router) | Calico, Cilium, VPC CNI | OVN-K, Calico, Cilium |
| | Est. FTE: 0.1–0.25 | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 |
| **Storage** | Difficulty: 2/5 | Difficulty: 2/5 | Difficulty: 3/5 |
| | OpenEBS bundled via Replicated | EBS/Azure Disk/GCS standard classes | Customer-specific: Longhorn, vSphere, Ceph |
| | OpenEBS, Longhorn | AWS EBS CSI, Azure Disk CSI | Longhorn, vSAN, NetApp Trident |
| | Est. FTE: 0.1 | Est. FTE: 0.1 | Est. FTE: 0.25–0.5 |
| **Air-Gap Support** | Difficulty: 3/5 | Difficulty: 5/5 | Difficulty: 4/5 |
| | Bundle via Replicated Embedded Cluster | Rare use case; requires private registry | Common in regulated industries; requires full bundle |
| | Replicated air-gap bundles | ECR mirroring, private registries | KOTS bundles, OCP disconnected install |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.5–1.0 | Est. FTE: 0.5–1.0 |
| **Security Policy (PSA/OPA)** | Difficulty: 2/5 | Difficulty: 3/5 | Difficulty: 4/5 |
| | ISV controls policy in Embedded Cluster | Customer policy varies | OCP Security Context Constraints (SCC) differ from upstream PSA |
| | Embedded PSA config | OPA Gatekeeper, Kyverno | SCC, OPA, Kyverno |
| | Est. FTE: 0.1–0.25 | Est. FTE: 0.25–0.5 | Est. FTE: 0.5–1.0 |
| **Debugging / Reproducing Issues** | Difficulty: 2/5 | Difficulty: 3/5 | Difficulty: 4/5 |
| | ISV controls full environment | Must replicate cloud config | Must replicate specific OCP/Rancher version + config |
| | CMX, local k0s clusters | CMX EKS/AKS/GKE clusters | CMX OpenShift support; Rancher requires dedicated lab |
| | Est. FTE: 0.5 on-call | Est. FTE: 0.5–1.0 on-call | Est. FTE: 1.0–2.0 on-call |

Note: On-call burden is separate from active work estimates. Assumes one severity-1 incident per customer per quarter requiring 2–4 hours of senior engineering time.

---

## 9. Licensing and Cost: Platform Licensing Passed to Customers

### 9.1 Cost Structure by Platform

| Platform | Licensing Basis | Approximate Cost | Who Pays | ISV Pricing Impact |
|---|---|---|---|---|
| OCP (self-managed) | Core-pairs (2 physical / 4 vCPU) | ~€12,000–€30,000/year per 6 core-pairs | Customer | ISV must size workloads to minimize core count; document recommended cluster sizing |
| SUSE Rancher Prime | CPU/vCPU-based (2025 model) | $7,594–$41,831/year per server | Customer | Pricing shock causing churn from Rancher; ISV software must be portable away from Rancher |
| VMware VKS (TKG) | Included in VCF | Bundled in VCF license | Customer | Only accessible to existing VCF subscribers; not an acquisition cost ISVs can control |
| Replicated (KOTS/Embedded) | Per-customer instance or seat-based | ISV pays Replicated; passes cost through | ISV (absorbed or passed through) | ~$500–$5,000/month depending on number of managed instances [UNVERIFIED exact Replicated pricing — vendor does not publish public price list] |
| OKD | None | Free | N/A | No enterprise support; not viable commercial target |

### 9.2 Cost Impact on ISV Pricing Model

ISVs have three options for handling platform licensing costs:

1. **Require customer-provided platform**: Customer bears OCP/Rancher license cost. ISV prices software independently. Risk: Customer sticker shock on platform cost reduces deal velocity.
2. **Bundle embedded cluster (Replicated)**: ISV absorbs delivery platform cost, prices product to include it. Simplifies customer procurement but reduces ISV margin.
3. **Platform-agnostic Helm delivery**: No platform license cost required. Maximum customer flexibility but maximum support complexity.

[FACT] "With Replicated, software vendors can ship their modern apps into complex diverse customer environments with speed, security, and ease." — [Replicated Introduction](https://docs.replicated.com/intro-replicated)

---

## 10. Comparative Summary: Portable K8s Platforms for ISV Delivery

| Dimension | Red Hat OCP | SUSE Rancher Prime | VMware VKS (TKG) | Replicated/KOTS |
|---|---|---|---|---|
| **Primary Use Case** | Certified ISV distribution; regulated enterprise | Multi-cluster management; GitOps at scale | vSphere-native enterprise K8s | ISV delivery abstraction layer |
| **ISV Certification Program** | Yes (OperatorHub, Helm) | No formal program | No formal program | N/A (wraps other platforms) |
| **Air-Gap Native** | Yes (disconnected install support) | Yes (RKE2 supports air-gap) | Yes (documented) | Yes (Embedded Cluster bundles) |
| **Multi-Cluster Management** | Limited (ACM add-on) | Core strength (Fleet) | Limited (VKS Supervisor) | Via Replicated Vendor Portal telemetry |
| **Customer Self-Service** | Moderate (OCP GUI + CLI) | High (Rancher UI + Fleet) | Moderate (vCenter integration) | High (KOTS Admin Console) |
| **2025 Pricing Risk** | Stable (core-pair model) | High (4–9× increase reported) | Stable (bundled with VCF) | Moderate (Replicated pricing not public) |
| **Kubernetes Conformance** | Yes (CNCF certified) | Yes (CNCF certified) | Yes (CNCF certified) | Embedded Cluster: k0s (CNCF conformant) |
| **ISV Operational Difficulty** | 4/5 (cert maintenance overhead) | 3/5 (customer migration risk) | 3/5 (narrow vSphere base) | 2/5 (abstraction reduces variability) |

---

## Key Takeaways

- **Replicated/KOTS has become the dominant ISV delivery abstraction layer** for commercial software shipped to customer-controlled Kubernetes environments. Its Embedded Cluster (k0s-based) and Compatibility Matrix (65,981+ environment combinations) address the two hardest problems in ISV K8s delivery: environment variability and pre-production testing at scale.

- **Red Hat OpenShift certification provides the strongest enterprise market signal** for ISVs targeting regulated industries, government, and large enterprises. The certification pipeline, OperatorHub listing, and OLM v1 Helm support create a structured path — but require ongoing re-certification per OCP minor release and dedicated engineering investment (est. 0.5–1.0 FTE for a moderately complex operator).

- **SUSE Rancher's 2025 CPU-based pricing shift creates active customer churn risk** for ISVs whose delivery model assumes stable Rancher deployments in customer environments. ISVs should verify that their application packaging (Helm or operator) is portable away from Rancher's management layer, so they can support customers who migrate to alternative platforms.

- **VMware Tanzu/VKS is a narrow but deep target**: the Broadcom acquisition and TKG-to-VKS rebranding introduced API changes (TKC API removal) and customer confusion, but the installed base of vSphere customers remains large. ISVs with strong VMware enterprise relationships should maintain VKS compatibility while ensuring Cluster API is the primary deployment mechanism.

- **Air-gapped delivery is a non-negotiable requirement for regulated enterprise sectors**, and it is the hardest operational scenario for ISV support teams. The Replicated Embedded Cluster air-gap bundle workflow is currently the lowest-friction path to supporting disconnected customer environments, and ISVs entering regulated markets (defense, healthcare, financial services) should build air-gap delivery into their initial architecture rather than retrofitting it later.

---

## Related — Out of Scope

- Managed cloud Kubernetes (EKS, AKS, GKE) as an ISV deployment target — See [F52: Managed Cloud Kubernetes] for detailed coverage of cloud-managed K8s control planes.
- Kubernetes operators as a design pattern (e.g., specific operator frameworks, controller-runtime) — See [F54: Kubernetes Operators for ISV Applications].
- Business impact of deployment model selection on ISV go-to-market, ACV, and sales cycle — See Wave 9 coverage for commercial model analysis.
- CNCF-certified distributions not discussed here (K3s, Talos Linux, Flatcar) — relevant for edge deployments but outside this scope boundary.

---

## Sources

1. [CNCF 2025 Annual Cloud Native Survey](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)
2. [Red Hat OpenShift Software Certification Policy Guide 2025](https://docs.redhat.com/en/documentation/red_hat_software_certification/2025/html-single/red_hat_openshift_software_certification_policy_guide/index)
3. [Red Hat Operator Pipelines GitHub Repository](https://github.com/redhat-openshift-ecosystem/operator-pipelines)
4. [OpenShift Operator Life Cycles, Red Hat Customer Portal](https://access.redhat.com/support/policy/updates/openshift_operators)
5. [The Future of the Red Hat OpenShift Operator SDK](https://www.redhat.com/en/blog/future-red-hat-openshift-operator-sdk)
6. [Red Hat OpenShift vs. OKD](https://www.redhat.com/en/topics/containers/red-hat-openshift-okd)
7. [Red Hat Learning Community: OKD vs OCP](https://learn.redhat.com/t5/Kube-by-Example-KBE/OKD-vs-OCP/td-p/23997)
8. [Red Hat, Self-Managed OpenShift Subscription Guide](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide)
9. [Medium: True Price of OpenShift Success, 2025](https://medium.com/@PlanB./discover-the-true-price-of-openshift-success-estimating-costs-for-your-enterprise-sla-in-2025-e9bbc817c6d7)
10. [Red Hat Developer, Packaging Applications with Kubernetes Operators](https://developers.redhat.com/topics/kubernetes/operators)
11. [RKE2 Documentation](https://docs.rke2.io/)
12. [SUSE Rancher Manager v2.13 Documentation](https://documentation.suse.com/cloudnative/rancher-manager/v2.13/en/cluster-deployment/configuration/rke2.html)
13. [Rancher Fleet Overview](https://ranchermanager.docs.rancher.com/integrations-in-rancher/fleet/overview)
14. [Rancher Fleet Core Concepts](https://fleet.rancher.io/concepts)
15. [Baytech Consulting: Rancher Enterprise Kubernetes Management 2025](https://www.baytechconsulting.com/blog/rancher-enterprise-kubernetes-management-2025)
16. [Portainer Blog: SUSE Rancher Price Hike 2025](https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025)
17. [TrustRadius: SUSE Rancher Pricing 2026](https://www.trustradius.com/products/suse-rancher/pricing)
18. [VMware Cloud Foundation Blog: vSphere Kubernetes Service 3.3 GA, March 2025](https://blogs.vmware.com/cloud-foundation/2025/03/04/vmware-vsphere-kubernetes-service-3-3-is-now-ga/)
19. [TechTarget: Broadcom VMware Hardens vDefend, Drops Tanzu Branding](https://www.techtarget.com/searchdatacenter/news/366621962/Broadcom-VMware-hardens-vDefend-drops-Tanzu-branding-in-VCF)
20. [Broadcom TKG v2.5.x Release Notes](https://techdocs.broadcom.com/us/en/vmware-tanzu/standalone-components/tanzu-kubernetes-grid/2-5/tkg/mgmt-release-notes.html)
21. [TechTarget: VMware Tanzu Integration and Broadcom Backlash](https://www.techtarget.com/searchitoperations/news/366608899/VMware-Tanzu-hones-integration-but-faces-Broadcom-backlash)
22. [NetApp TKG Overview](https://docs.netapp.com/us-en/netapp-solutions/containers/vtwn_overview_tkg.html)
23. [Replicated KOTS Introduction](https://docs.replicated.com/intro-kots)
24. [Replicated Embedded Cluster Overview](https://docs.replicated.com/vendor/embedded-overview)
25. [Replicated Embedded Cluster Release Notes](https://docs.replicated.com/release-notes/rn-embedded-cluster)
26. [Replicated Compatibility Matrix](https://www.replicated.com/compatibility-matrix)
27. [Replicated: Deploy Self-Hosted Kubernetes Apps with Embedded Cluster](https://www.replicated.com/embedded-cluster)
28. [Replicated Introduction](https://docs.replicated.com/intro-replicated)
29. [Replicated KOTS Release Notes](https://docs.replicated.com/release-notes/rn-app-manager)
30. [Replicated Blog](https://www.replicated.com/blog)
31. [Kubernetes Version Skew Policy](https://kubernetes.io/releases/version-skew-policy/)
32. [Helm Version Support Policy](https://helm.sh/docs/topics/version_skew/)
33. [Plural.sh: Kubernetes CNI Guide 2025](https://www.plural.sh/blog/kubernetes-cni-guide/)
34. [Cloud Native Now: Overcoming Challenges of Air-Gapped Kubernetes](https://cloudnativenow.com/features/overcoming-challenges-of-air-gapped-kubernetes/)
35. [InfoQ: Helm 4 Release 2025](https://www.infoq.com/news/2025/11/helm-4/)
36. [Johal.in: Helm Charts for Kubernetes 2025](https://johal.in/helm-charts-for-kubernetes-packaging-ai-models-for-helm-based-deployments-2025/)
37. [Operator Lifecycle Manager](https://olm.operatorframework.io/)
38. [Acecloud.ai: Kubernetes Deployment Strategies](https://acecloud.ai/blog/kubernetes-deployment-strategies/)
39. [Google Cloud Blog: Kubernetes Minor Version Rollback](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-gets-minor-version-rollback)
40. [Baytech Consulting: Scaling Kubernetes in the Enterprise 2025](https://www.baytechconsulting.com/blog/scaling-kubernetes-in-the-enterprise-2025)
41. [Replicated: Testing Releases in Customer-Representative Environments](https://www.replicated.com/blog/testing-releases-in-customer-environments)
42. [Red Hat OpenShift Certification Policy Guide 2025](https://docs.redhat.com/en/documentation/red_hat_software_certification/2025/html-single/red_hat_openshift_software_certification_policy_guide/index)
43. [Kubernetes v1.35 Sneak Peek](https://kubernetes.io/blog/2025/11/26/kubernetes-v1-35-sneak-peek/)
44. [Medium: How Modern Software Vendors Ship Kubernetes Apps to On-Prem Customers (Dec 2025)](https://medium.com/@Kannan91/how-modern-software-vendors-ship-kubernetes-apps-to-on-prem-customers-replicated-kots-air-gap-deec7eb339b0)
