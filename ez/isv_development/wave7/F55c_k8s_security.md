# F55c: Kubernetes Security Posture

**Research Date:** 2026-02-19
**Scope:** Managed Kubernetes (EKS, AKS, GKE) security posture — RBAC, pod security, network policies, image security, secrets management, runtime security, and supply chain security. Gap analysis against cloud-native security services.
**Related Files:** See [F52: K8s Platform Management] for cluster lifecycle and control-plane operations. See [F11/F19/F27: Cloud-Native Security] for GuardDuty, Defender, and SCC full coverage. See [F46/F47/F71: On-Prem Security] for on-premises security operations.

---

## Executive Summary

Securing workloads on managed Kubernetes requires assembling and operating a layered stack of independent tools — RBAC policies, pod security admission controllers, CNI-layer network policies, image signing and scanning pipelines, external secrets integrations, and runtime behavioral monitors — none of which come pre-configured in EKS, AKS, or GKE. This fragmentation creates high operational burden: each layer demands dedicated engineering expertise, separate toolchains, and continuous policy maintenance that scales with cluster and workload count. Cloud-native security services (AWS GuardDuty, Microsoft Defender for Cloud, Google Security Command Center) increasingly close the gap through managed agents and admission controller integrations, but independent research shows detection rates for Kubernetes-specific attack techniques range from 24% (GCP Security Command Center) to 66% (Azure Defender), leaving substantial gaps that K8s-native tooling such as Falco, Kyverno, and Cilium must fill. For an ISV deploying AI-driven SaaS on managed Kubernetes, the aggregate operational investment across all security domains is estimated at 1.5–3.0 FTE for a mid-size deployment, rising steeply with multi-cluster or multi-cloud configurations. On-premises deployments face roughly 2× the burden due to absent managed control-plane security baseline.

---

## 1. RBAC: Role-Based Access Control Architecture

### 1.1 Core K8s RBAC Concepts

Kubernetes RBAC is an allow-only authorization model — it cannot express explicit denials — built on four object types: `Role`, `ClusterRole`, `RoleBinding`, and `ClusterRoleBinding`. Roles are namespace-scoped; ClusterRoles apply cluster-wide. [FACT] Kubernetes RBAC does not support attribute-based access conditions, glob matching, or deny rules — all three are cited architectural limitations as of 2025. Source: [Kubernetes Roles: A Practical Guide for 2025](https://www.plural.sh/blog/kubernetes-roles-rbac-guide/)

**Least-privilege design pattern:**
- Each application pod should run under a dedicated `ServiceAccount` — not the `default` service account. [FACT] The AWS EKS Best Practices Guide states: "Each application should have its own dedicated service account." Source: [Identity and Access Management — Amazon EKS](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)
- Development and production workloads must use separate namespaces with distinct RBAC policies. Source: [Identity and Access Management — Amazon EKS](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)
- Anonymous API server access should be disabled. Source: [Identity and Access Management — Amazon EKS](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)

**Scale problem:** [FACT] "Managing access via raw YAML and kubectl may be feasible in a single cluster, but across a fleet, complexity grows fast" — ensuring consistent and auditable RBAC policies across dozens or hundreds of clusters becomes a major operational challenge. Source: [Kubernetes Roles: A Practical Guide for 2025](https://www.plural.sh/blog/kubernetes-roles-rbac-guide/)

### 1.2 Cloud IAM Integration: IRSA, Pod Identity, and Workload Identity

All three major managed Kubernetes platforms provide a mechanism to bind Kubernetes `ServiceAccounts` to cloud IAM identities via OIDC federation, eliminating the need for long-lived credential files inside containers.

| Platform | Mechanism | OIDC Approach |
|----------|-----------|---------------|
| AWS EKS  | EKS Pod Identity / IRSA | ServiceAccount annotated with IAM Role ARN; OIDC issuer validates token |
| Azure AKS | Workload Identity (Entra ID) | Federated credential links K8s SA to Entra app registration |
| Google GKE | Workload Identity Federation | K8s SA mapped to Google Service Account via IAM binding |

[FACT] "IRSA and RBAC complement each other: IRSA allows secure access to AWS resources from EKS pods, while RBAC controls access to internal cluster resources." Source: [AWS Authentication for K8s: IAM Roles for Service Accounts (IRSA)](https://chamila.dev/blog/2025-03-10_aws-authentication-for-k8s-iam-roles-for-service-accounts-irsa/)

[FACT] For IRSA, the IAM role trust policy "should tightly bind the IAM role to a specific Kubernetes service account in a namespace, meaning only a pod using that exact service account in that namespace can assume the IAM role." Source: [Identity and Access Management — Amazon EKS](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)

[FACT] AWS recommends setting a permissions boundary on IAM roles used with IRSA and EKS Pod Identities "to ensure that roles cannot exceed a maximum level of permissions." Source: [Identity and Access Management — Amazon EKS](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)

[FACT] GKE Workload Identity Federation "lets you use IAM policies to grant Kubernetes workloads in your GKE cluster access to specific Google Cloud APIs without needing manual configuration or less secure methods like service account key files." Source: [About Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)

[FACT] AKS Workload Identity "uses Kubernetes-native capabilities to federate with external identity providers" and requires the cluster to issue OIDC tokens via a published discovery document. Source: [Kubernetes Workload Identity and Access — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/eks-to-aks/workload-identity)

### 1.3 RBAC Operational Summary

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| RBAC & IAM integration | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| Key requirements | Self-managed OIDC IdP, manual API server config | OIDC issuer provided by platform; IRSA/Workload Identity configuration | IAM policies only; no K8s RBAC layer |
| Representative tools | dex, keycloak, manual kubeconfig | IRSA, EKS Pod Identity, AKS Workload Identity, GKE WIF | IAM roles, service account keys, instance profiles |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.1 FTE |

---

## 2. Pod Security: Admission Control and Policy Enforcement

### 2.1 Pod Security Admission (PSA) — Built-In but Limited

[FACT] Pod Security Admission (PSA) replaced PodSecurityPolicy (PSP) as the built-in Kubernetes admission controller. It enforces three standardized profiles: `privileged`, `baseline`, and `restricted`, applied per-namespace. Source: [Kubernetes Pod Security Admission Explained](https://alexandre-vazquez.com/kubernetes-policy-enforcement-understanding-pod-security-admission-psa/)

[FACT] PSA has documented limitations: it "works only on pods, [has] unconfigurable messages, complex access to audit logs, and the lack of a DevOps pipeline." Source: [PSA vs. OPA/Gatekeeper: Customizing Kubernetes Pod Security](https://medium.com/@ghorbelmohamed37/%EF%B8%8Fpodsecurityadmission-psa-vs-78edcefcf3a1)

PSA operates in three modes per namespace: `enforce` (reject non-compliant pods), `audit` (log violations), and `warn` (return warnings). It is the baseline minimum — production clusters require an additional policy engine for custom rules.

### 2.2 OPA/Gatekeeper

[FACT] OPA (Open Policy Agent) is a CNCF **Graduate** project. Gatekeeper is its Kubernetes-native integration layer, implementing a validating webhook. Policies are written in Rego, a purpose-built policy language. Source: [Kubernetes Policy Comparison: Kyverno vs. OPA/Gatekeeper](https://nirmata.com/2025/02/07/kubernetes-policy-comparison-kyverno-vs-opa-gatekeeper/)

Strengths: highly expressive, fast evaluation, cross-platform (usable beyond Kubernetes). Weaknesses: Rego has a steep learning curve; policies feel foreign to Kubernetes-native engineers.

### 2.3 Kyverno

[FACT] Kyverno is a CNCF **Incubating** project as of 2025. It uses YAML for policy definitions — the same format as Kubernetes manifests — and was "built from the ground up for Kubernetes." Source: [Kubernetes Policy Comparison: Kyverno vs. OPA/Gatekeeper](https://nirmata.com/2025/02/07/kubernetes-policy-comparison-kyverno-vs-opa-gatekeeper/)

[FACT] Kyverno "offers a rich library of pre-defined policies, covering everything from Pod Security Standards (PSS) to best practices for Kubernetes configurations." Source: [10 Reasons Why Kubernetes Users Choose Kyverno Over OPA Gatekeeper](https://nirmata.com/2025/04/14/10-reasons-why-kubernetes-users-choose-kyverno-over-opa-gatekeeper/)

Kyverno also provides mutation (auto-patching resources) and generation (creating derived resources) — capabilities OPA/Gatekeeper does not natively provide. Kyverno's native Sigstore image verification integration (see Section 4) makes it the preferred engine for supply chain policy enforcement.

### 2.4 Policy Enforcement Comparison

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Pod security admission | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| Key requirements | Full policy engine deployment and management; no built-in baseline | PSA built-in; Kyverno or Gatekeeper for custom policies | Provider-managed: Defender for Cloud admission webhook |
| Representative tools | OPA/Gatekeeper, Kyverno | Kyverno (preferred), OPA/Gatekeeper | Defender for Cloud gated deployment, GKE Policy Controller |
| Est. FTE | 0.5–0.75 FTE | 0.25–0.5 FTE | 0.05–0.1 FTE |

---

## 3. Network Policies: Microsegmentation and Egress Control

### 3.1 Standard Kubernetes NetworkPolicy Limitations

Standard Kubernetes `NetworkPolicy` objects require a CNI plugin to enforce them — the Kubernetes API accepts the objects but does not enforce them independently. Default behavior in most clusters is **allow-all**. The foundational best practice is default-deny: [FACT] "The single most important security principle for Network Policies is default deny: starting by blocking all traffic, then explicitly allowing only legitimate communication patterns through a whitelist approach." Source: [Kubernetes Network Policies Explained for Production Security](https://atmosly.com/blog/kubernetes-network-policies-security-implementation-guide-2025)

Standard `NetworkPolicy` operates at L3/L4 (IP addresses and ports) only. It cannot filter by HTTP method, URL path, gRPC service, or DNS name.

### 3.2 Calico

[FACT] Calico is "the most popular for network policies and high performance with eBPF dataplane option supporting advanced features like global policies and egress gateways." Source: [Cilium Explained: Components, Use Cases, Limitations and Alternatives](https://www.tigera.io/learn/guides/cilium-vs-calico/cilium/)

[FACT] Calico Enterprise provides "identity-aware microsegmentation for workloads that enables deployment of a scalable, unified microsegmentation model for hosts, VMs, containers, pods, and services across all environments." Source: [Cilium Explained: Components, Use Cases, Limitations and Alternatives](https://www.tigera.io/learn/guides/cilium-vs-calico/cilium/)

[FACT] The Calico Egress Gateway "provides universal firewall integration, enabling Kubernetes resources to securely access endpoints behind a firewall." Source: [Cilium Explained: Components, Use Cases, Limitations and Alternatives](https://www.tigera.io/learn/guides/cilium-vs-calico/cilium/)

### 3.3 Cilium

[FACT] Cilium is eBPF-based with "advanced observability via Hubble and supports Layer 7 policies (HTTP method/path filtering) and DNS-based policies." Source: [Calico vs. Cilium: 9 Key Differences and How to Choose](https://www.tigera.io/learn/guides/cilium-vs-calico/)

[FACT] Cilium's `CiliumNetworkPolicy` CRD "supports specification of policies at Layers 3-7 for both ingress and egress." Source: [Network Policy — Cilium 1.19.1 documentation](https://docs.cilium.io/en/stable/network/kubernetes/policy/)

[FACT] DNS-based policies "allow or deny traffic to FQDNs or wildcard domains (e.g., `api.example.com`, `*.trusted.com`)" and "can be combined with port (L4) and API (L7) rules." Source: [Locking Down External Access with DNS-Based Policies — Cilium 1.19.0 documentation](https://docs.cilium.io/en/stable/security/dns/)

[FACT] Cilium supports "integrated ingress and egress gateway, bandwidth management and service mesh." Source: [cilium/cilium — GitHub](https://github.com/cilium/cilium)

[FACT] Safe production adoption techniques for Cilium in 2025 include "audit mode, default-deny toggles, and L7 allow-all scaffolding, which help validate policy changes before they hit production and reduce the risk of traffic disruptions." Source: [Safely managing Cilium network policies in Kubernetes — CNCF](https://www.cncf.io/blog/2025/11/06/safely-managing-cilium-network-policies-in-kubernetes-testing-and-simulation-techniques/)

### 3.4 Cloud Security Groups vs. K8s Network Policies

Cloud security groups (AWS SGs, Azure NSGs) operate at the VM/node level — they do not provide pod-to-pod microsegmentation within a node. K8s network policies (enforced via Calico or Cilium) operate at the pod level regardless of node placement, providing true workload-level microsegmentation. Both layers should be applied in defense-in-depth. See [F11/F19/F27: Cloud-Native Security] for full cloud SG/NSG coverage.

### 3.5 Network Policy Operational Summary

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Network microsegmentation | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| Key requirements | Manual CNI selection, installation, and policy management; no cloud guard rails | CNI often pre-selected by platform (AKS=Cilium, GKE=Dataplane V2/Cilium); policy authoring required | Security groups + service-mesh policies; simpler but less granular |
| Representative tools | Calico, Cilium, Weave | Calico, Cilium, platform-native (AKS CNI, GKE Dataplane V2) | AWS SGs, Azure NSGs, GCP Firewall Rules + Cloud Armor |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.1–0.2 FTE |

---

## 4. Image Security: Signing, Scanning, and Admission Control

### 4.1 Vulnerability Scanning with Trivy Operator

[FACT] The Trivy Operator "leverages Trivy to continuously scan your Kubernetes cluster for security issues, with scans summarized in security reports as Kubernetes Custom Resource Definitions accessible through the Kubernetes API." Source: [aquasecurity/trivy-operator — GitHub](https://github.com/aquasecurity/trivy-operator)

[FACT] Trivy Operator "automatically discovers and scans all images that are being used in a Kubernetes cluster, including images of application pods and system pods. The Operator watches Kubernetes for state changes and automatically triggers security scans in response." Source: [Automate Kubernetes Image Vulnerability Scanning — Pluralsight](https://www.pluralsight.com/labs/aws/automate-kubernetes-image-vulnerability-scanning)

[FACT] Trivy Operator can be configured as a `ValidatingWebhook` admission controller — "Kubernetes sends requests to the admission server when a Pod creation is initiated, and the admission controller checks the image using Trivy" if the namespace is labeled for validation. Source: [Admission Controller — trivy-operator](https://devopstales.github.io/trivy-operator/2.4/functions/image-validator/)

[FACT] "Integrating with admission controllers can prevent vulnerable workloads from deploying in the first place, serving as your last line of defense." Source: [How to Use Trivy for Kubernetes Security](https://oneuptime.com/blog/post/2026-01-27-trivy-kubernetes-security/view)

### 4.2 Image Signing with Sigstore / Cosign

[FACT] Sigstore is a Linux Foundation project providing "public software signing and transparency to improve open source supply chain security." Cosign is the CLI tool for "signing and verifying container images and files." Source: [Supply Chain Security: Sigstore and Cosign (Part II)](https://blog.gitguardian.com/supply-chain-security-sigstore-and-cosign-part-ii/)

[FACT] Sigstore's Policy Controller "can automatically validate signatures and attestations on container images as well as apply policies against attestations" and "also resolves the image tags to ensure the image being run is not different from when it was admitted." Source: [Kubernetes Policy Controller — Sigstore](https://docs.sigstore.dev/policy-controller/overview/)

[FACT] "Enforcement is configured on a per-namespace basis, and multiple policies are supported." Source: [Kubernetes Policy Controller — Sigstore](https://docs.sigstore.dev/policy-controller/overview/)

[FACT] Keyless signing authenticates "through your GitHub identity via OpenID Connect (OIDC)" — no long-lived private key to manage or rotate. Source: [Signing Containers — Sigstore](https://docs.sigstore.dev/cosign/signing/signing_with_containers/)

**Kyverno + Sigstore integration:** Kyverno's `verifyImages` policy rule natively integrates with Sigstore to enforce that only images signed by a trusted identity can be deployed. Source: [Sigstore — Kyverno](https://main.kyverno.io/docs/policy-types/cluster-policy/verify-images/sigstore/)

### 4.3 Image Security Operational Summary

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Image scanning | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| Image signing | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| Key requirements | Self-hosted registry + scanner; admission webhook setup | Trivy Operator + Kyverno/Policy Controller; registry integration | ECR/ACR/GAR native scanning + Defender gated deployment |
| Representative tools | Trivy, Harbor, Clair | Trivy Operator, Sigstore Policy Controller, Kyverno verifyImages | ECR Enhanced Scanning, Defender for Cloud gated deployment, GAR scanning |
| Est. FTE | 0.5–0.75 FTE | 0.25–0.5 FTE | 0.05–0.1 FTE |

---

## 5. Secrets Management

### 5.1 The Native Kubernetes Secrets Problem

[FACT] "By default, Kubernetes Secrets are stored as Base64-encoded strings in etcd, but Base64 is merely an encoding format, not encryption — it offers no real security." Source: [Kubernetes Secrets Management: Vault vs Sealed Secrets vs External Secrets (2025)](https://atmosly.com/blog/kubernetes-secrets-management-vault-vs-sealed-secrets-vs-external-secrets-2025)

[FACT] "Anyone with access to etcd can easily decode and read your sensitive data. If an attacker gains access to etcd directly through compromised credentials, stolen database backup files, or direct filesystem access to etcd data directories, they can extract every single secret from your entire cluster in plaintext." Source: [Keeping Your Data Safe: ETCD Encryption at Rest in Kubernetes](https://medium.com/@tamerbenhassan/keeping-your-data-safe-etcd-encryption-at-rest-in-kubernetes-a297250e83e7)

[FACT] "Kubernetes encodes Secrets with Base64 but does not encrypt them at rest, so to protect sensitive data, you must enable encryption in etcd manually or use an external secrets manager." Source: [A Practical Guide to Kubernetes Encryption at Rest](https://www.plural.sh/blog/a-practical-guide-to-kubernetes-encryption-at-rest/)

On managed K8s, etcd encryption at rest using KMS (AWS KMS, Azure Key Vault, Google Cloud KMS) is available and recommended but requires explicit enablement.

### 5.2 Secrets Store CSI Driver

[FACT] The Secrets Store CSI Driver "allows Kubernetes to mount multiple secrets, keys, and certs stored in enterprise-grade external secrets stores into their pods as a volume" using a CRD called `SecretProviderClass`. "Secrets are auto-rotated in the pods without any other tooling required." Source: [Secrets Store CSI Driver — Kubernetes SIGs](https://secrets-store-csi-driver.sigs.k8s.io/)

[FACT] The CSI Driver is "a good alternative to other solutions like the External Secrets Operator when you need to avoid secrets being stored in the etcd." Source: [Secrets Store CSI Driver vs. External Secrets Operator](https://www.kubeblog.com/kubernetes/secrets-store-csi-driver-vs-external-secrets-operator/)

[FACT] Azure AKS natively supports the CSI Driver with Key Vault integration: "Use the Azure Key Vault provider for Secrets Store CSI Driver for Azure Kubernetes Service (AKS) secrets." Source: [Use the Azure Key Vault provider for Secrets Store CSI Driver for AKS](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)

### 5.3 External Secrets Operator (ESO)

[FACT] External Secrets Operator "connects the gap between Kubernetes and external secret management systems, allowing you to securely fetch secrets stored in external systems like AWS Secrets Manager, HashiCorp Vault, Google Secret Manager, and Azure Key Vault and insert them into your Kubernetes applications." Source: [List of Secrets Management Tools for Kubernetes in 2025](https://blog.techiescamp.com/secrets-management-tools/)

[FACT] ESO "automatically syncs secrets between external systems and Kubernetes and uses Custom Resource Definitions like `ExternalSecret` to define secrets from external backends." Source: [List of Secrets Management Tools for Kubernetes in 2025](https://blog.techiescamp.com/secrets-management-tools/)

ESO creates native K8s `Secret` objects — easier for application consumption but means secrets land in etcd (mitigated if etcd encryption at rest is enabled). CSI Driver avoids etcd entirely by mounting secrets directly as ephemeral volumes.

### 5.4 HashiCorp Vault Integration

[FACT] The Vault Secrets Operator is "a Kubernetes operator that syncs secrets between Vault and Kubernetes natively without requiring the users to learn details of Vault use." Source: [Manage Kubernetes native secrets with the Vault Secrets Operator](https://developer.hashicorp.com/vault/tutorials/kubernetes-introduction/vault-secrets-operator)

[FACT] The Vault Secrets Store CSI provider "requires the CSI Secret Store Driver to be installed" and "allows pods to consume Vault secrets using Secrets Store CSI volumes." Source: [Vault Secrets Store CSI provider](https://developer.hashicorp.com/vault/docs/deploy/kubernetes/csi)

### 5.5 Secrets Management Operational Summary

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Secrets management | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| Key requirements | Self-hosted Vault cluster or equivalent; etcd encryption manual; no managed KMS integration | ESO or CSI Driver + cloud KMS; etcd encryption must be explicitly enabled | Fully managed (Secrets Manager, Key Vault, Secret Manager) — no etcd risk |
| Representative tools | HashiCorp Vault, Sealed Secrets, manual KMS | ESO, Secrets Store CSI Driver, Vault Secrets Operator, cloud KMS | AWS Secrets Manager, Azure Key Vault, GCP Secret Manager |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.05 FTE |

---

## 6. Runtime Security: Threat Detection on Managed K8s

### 6.1 Falco

[FACT] "Falco is a cloud native security tool that provides runtime security across hosts, containers, Kubernetes, and cloud environments. It leverages custom rules on Linux kernel events and other data sources through plugins, enriching event data with contextual metadata to deliver real-time alerts." Source: [Falco — falco.org](https://falco.org/)

[FACT] Falco "operates at the kernel level and can leverage one of two data collection backends: Kernel module (a traditional approach) or eBPF (extended Berkeley Packet Filter) (a more modern, safer, and increasingly preferred method)." Source: [From Observability to Action: Using Falco for Kubernetes Threat Detection](https://schoenwald.aero/posts/2025-03-29_falco-for-kubernetes-threat-detection/)

[FACT] "Falco can run on many platforms like GKE, EKS, AKS, gVisor and others. It is deployable in Kubernetes with an official Helm chart." Source: [Kubernetes Security Tools: An Overview of Falco](https://medium.com/@noah_h/kubernetes-security-tools-falco-e873831f3d3d)

[FACT] OVHcloud deployed Falco on its managed Kubernetes service in February 2025 using "the latest version of Falco with the k8saudit-ovh and json plugins for OVHcloud managed Kubernetes clusters." Source: [Enhancing Kubernetes Security with Falco on OVHcloud MKS — OVHcloud Blog](https://blog.ovhcloud.com/enhancing-kubernetes-security-detecting-threats-in-ovhcloud-managed-kubernetes-cluster-mks-audit-logs-with-falco/)

**Deployment consideration on managed K8s:** Some managed K8s platforms restrict kernel module installation. eBPF mode (using the eBPF probe or the newer `falco-ebpf` driver) is the standard deployment path on EKS, AKS, and GKE as of 2025.

### 6.2 AWS GuardDuty EKS Runtime Monitoring

[FACT] AWS announced GuardDuty Extended Threat Detection for EKS in June 2025, correlating "multiple security signals across Amazon EKS audit logs, runtime behavior of processes, malware execution, and AWS API activity to detect sophisticated attack patterns." Source: [AWS GuardDuty Extended Threat Detection now supports Amazon EKS](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-guardduty-threat-detection-eks/)

[FACT] eBPF was chosen for GuardDuty EKS Runtime Monitoring "due to its simplicity, safety, portability, and the detailed telemetry it can get from the kernel." A DaemonSet is deployed as a fully managed EKS add-on — "customers do not have to install or maintain the agent." Source: [Amazon GuardDuty expands Extended Threat Detection coverage to Amazon EKS clusters](https://aws.amazon.com/blogs/aws/amazon-guardduty-expands-extended-threat-detection-coverage-to-amazon-eks-clusters/)

### 6.3 Runtime Security Operational Summary

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Runtime threat detection | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| Key requirements | Full Falco/Sysdig deployment + alert routing; kernel access required | Falco via Helm (eBPF mode); OR cloud-provider managed agent (GuardDuty, Defender) | Fully managed — GuardDuty EKS, Defender for Containers |
| Representative tools | Falco, Sysdig, Aqua Security | Falco (Helm), Sysdig Secure, GuardDuty EKS Runtime Monitoring | AWS GuardDuty, Microsoft Defender for Containers, GCP Security Command Center |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.05–0.1 FTE |

---

## 7. Supply Chain Security

### 7.1 SBOM Generation

[FACT] A Software Bill of Materials (SBOM) is "a parts list for software — libraries, versions, licenses, checksums." Source: [Software-Supply-Chain Security in 2025: SBOMs, SLSA & Sigstore](https://faithforgelabs.com/blog_supplychain_security_2025.php)

[FACT] "Open standards have stabilized — SLSA 1.0, SPDX 3, Sigstore — enabling vendor-neutral pipelines. Tooling is mature: cosign, Syft, Kyverno, GUAC, and GitHub OIDC make Level 2 [SLSA] achievable in weeks." Source: [Software Supply Chain Security: SBOM, SLSA, Sigstore (2025)](https://www.elysiate.com/blog/supply-chain-security-sbom-slsa-sigstore-2025)

Syft (by Anchore) is the dominant open-source SBOM generator for container images, producing SPDX or CycloneDX format outputs that can be attached to container image manifests via cosign attestations.

### 7.2 SLSA Framework and Provenance

[FACT] SLSA (Supply chain Levels for Software Artifacts) 1.0 is the current stable standard as of 2025. SLSA Level 2 — requiring a hosted build service producing signed provenance — is the practical enterprise target. Source: [Secure Supply Chain with Sigstore, Cosign & SLSA Framework](https://blog.intelligencex.org/secure-supply-chain-with-sigstore-cosign-slsa-framework)

[FACT] "Kubernetes admission controllers check signatures, SBOM, and pinned digests. Organizations can enforce security policies using Kubernetes Admission Controllers or Kyverno to ensure only signed images are deployed, signatures must be verifiable via Sigstore, and provenance metadata must match build source." Source: [Software-Supply-Chain Security in 2025: SBOMs, SLSA & Sigstore](https://faithforgelabs.com/blog_supplychain_security_2025.php)

### 7.3 Policy-as-Code for Supply Chain

Kyverno is the primary K8s-native tool for enforcing supply chain policies at admission time. A complete supply chain policy gate enforces:
1. Image must be referenced by digest (not mutable tag)
2. Image must carry a valid cosign signature from the CI/CD pipeline identity
3. Image must have an attached SBOM attestation
4. Image provenance must satisfy minimum SLSA level

[FACT] Cosign signs SBOMs: "How to Sign an SBOM with Cosign" — SBOMs are attached as OCI artifacts and signed using the same cosign workflow as image signatures. Source: [How to Sign an SBOM with Cosign — Chainguard Academy](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-an-sbom-with-cosign/)

### 7.4 Supply Chain Operational Summary

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Supply chain security | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| Key requirements | Full self-hosted signing infra (Rekor, Fulcio, or private PKI); SBOM pipeline integration | CI/CD pipeline integration with cosign + Kyverno policy enforcement; registry must support OCI attestations | Cloud registry native signing (ECR, ACR, GAR) + Defender supply chain features |
| Representative tools | cosign, Syft, Rekor (self-hosted), Kyverno | cosign, Syft, Kyverno verifyImages, Sigstore Policy Controller | AWS Signer, Azure Trusted Signing, GCP Binary Authorization |
| Est. FTE | 0.5–0.75 FTE | 0.25–0.5 FTE | 0.1–0.25 FTE |

---

## 8. Gap Analysis: Cloud-Native Security Services vs. K8s-Native Tooling

### 8.1 What Cloud-Native Services Provide

**AWS GuardDuty for EKS:**
- Kubernetes audit log analysis (API server behavior)
- Runtime monitoring via managed eBPF DaemonSet agent
- Multi-stage attack correlation (audit logs + runtime + AWS API activity)
- Fully managed — no agent installation or maintenance by ISV

**Microsoft Defender for Containers:**
[FACT] Defender for Cloud "gated deployment" for Kubernetes is "now generally available" and "enforces container image security at deployment time by using Kubernetes admission control." It supports AKS, EKS, and GKE. Source: [Guarding Kubernetes Deployments: Runtime Gating for Vulnerable Images Now Generally Available](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/guarding-kubernetes-deployments-runtime-gating-for-vulnerable-images-now-general/4484234)

[FACT] "With gated deployment in Defender for Cloud, you can apply the same security rules to both Azure and AWS clusters, and the system will uniformly block non-compliant images on Azure or Amazon Web Services clusters alike, simplifying governance." Source: [Secure Kubernetes Deployments with Gated Container Images — Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/runtime-gated-overview)

**Google Security Command Center:**
Provides threat detection, misconfiguration findings, and container threat detection across GKE — tightly integrated with GKE but with more limited Kubernetes-specific coverage than GuardDuty or Defender.

### 8.2 Detection Rate Benchmarks

[STATISTIC] Independent testing of cloud-native security tools against Kubernetes attack techniques found: Azure Defender for Cloud: **66% detection rate**, AWS GuardDuty: **38% detection rate**, GCP Security Command Center: **24% detection rate**. Source: [Can Cloud Security Tools Protect Kubernetes Environments? — Cymulate](https://cymulate.com/blog/native-cloud-security-kubernetes-defenses/)

[FACT] "Since certain techniques bypass the API server entirely, GuardDuty will never see the attack. The same applies to Azure Defender and GCP's native security offerings, representing a complete blind spot in coverage for these attack vectors." Source: [Can Cloud Security Tools Protect Kubernetes Environments? — Cymulate](https://cymulate.com/blog/native-cloud-security-kubernetes-defenses/)

### 8.3 Structural Gaps in Cloud-Native Services

The table below identifies security domains where K8s-native tooling provides coverage that cloud-native services do not:

| Security Domain | Cloud-Native Services | K8s-Native Gap |
|-----------------|-----------------------|----------------|
| L7 network microsegmentation | Not covered (operates at VM/SG level) | Cilium CiliumNetworkPolicy fills this |
| DNS-based egress filtering | Partial (cloud firewall FQDNs, coarse) | Cilium DNS-aware policies are pod-level |
| Custom admission policies | Limited (provider-defined rules) | Kyverno/Gatekeeper — arbitrary Rego/YAML |
| Image provenance attestations (SLSA) | Not enforced natively | Kyverno verifyImages + cosign attestations |
| SBOM policy enforcement | Not enforced natively | Kyverno + Sigstore Policy Controller |
| Pod-level runtime rules | Managed agent (less customizable) | Falco with custom rule sets |
| Cross-cluster policy consistency | Manual / per-cloud | Kyverno centralized policy management |

### 8.4 The Complementary Model

Cloud-native security services and K8s-native tools are not mutually exclusive — they address different threat vectors. The recommended posture for a managed K8s deployment is:

- **Layer 1 (Cloud-native):** Enable cloud provider runtime monitoring (GuardDuty EKS, Defender for Containers) for managed threat detection with zero operational overhead.
- **Layer 2 (K8s-native):** Deploy Kyverno for admission policy (image signing, PSS enforcement, SBOM), Cilium for L7/DNS network policy, and Trivy Operator for continuous vulnerability scanning.
- **Layer 3 (Runtime):** Deploy Falco for custom behavioral detection rules filling cloud-native detection gaps.

---

## 9. Aggregate FTE Estimation and Operational Model

**Assumptions:** Mid-size ISV; 3–5 managed K8s clusters; 50 enterprise customers; primary deployment on one cloud provider's managed K8s (EKS or AKS or GKE). Does not include CI/CD pipeline engineering (supply chain security pipeline work is partially shared with development FTE).

| Security Domain | On-Premises FTE | Managed K8s FTE | Cloud-Native FTE |
|-----------------|-----------------|-----------------|------------------|
| RBAC & IAM Integration | 0.5–1.0 | 0.25–0.5 | 0.1 |
| Pod Security (Policy Engine) | 0.5–0.75 | 0.25–0.5 | 0.05–0.1 |
| Network Policy | 0.5–1.0 | 0.25–0.5 | 0.1–0.2 |
| Image Scanning | 0.5–0.75 | 0.25–0.5 | 0.05–0.1 |
| Image Signing | 0.5–0.75 | 0.25–0.5 | 0.1–0.25 |
| Secrets Management | 0.5–1.0 | 0.25–0.5 | 0.05 |
| Runtime Security | 0.5–1.0 | 0.25–0.5 | 0.05–0.1 |
| Supply Chain (SBOM/SLSA) | 0.5–0.75 | 0.25–0.5 | 0.1–0.25 |
| **Total (aggregate)** | **4.0–7.0 FTE** | **2.0–4.0 FTE** | **0.6–1.3 FTE** |

[UNVERIFIED — FTE ranges] These FTE estimates are derived from operational difficulty ratings and standard platform engineering staffing ratios. No publicly available Gartner or Forrester benchmark specifically covers Kubernetes security staffing at this granularity for ISVs as of February 2026. The ranges are believed to be reasonable based on practitioner guidance from CNCF, vendor documentation, and reported operational challenges. Organizations should validate against their specific cluster count and compliance requirements.

---

## Key Takeaways

- **Kubernetes security requires deliberate assembly.** No managed K8s platform (EKS, AKS, GKE) ships with a fully configured security stack. RBAC, pod security admission, network policy, image signing, secrets management, and runtime detection each require separate tool selection, deployment, and ongoing maintenance.

- **Kyverno + Cilium + Falco is the emerging K8s-native security baseline for 2025.** Kyverno handles policy enforcement (pod security, image verification, SBOM), Cilium handles L7/DNS-aware microsegmentation, and Falco provides customizable runtime behavioral detection — together covering gaps that cloud-native security services leave open.

- **Cloud-native security services fill the runtime detection baseline but have documented coverage gaps.** Independent testing shows Azure Defender at 66%, GuardDuty at 38%, and GCP SCC at 24% detection rates for K8s attack techniques. Techniques that bypass the API server are blind spots for all three.

- **Secrets management on K8s carries structural risk by default.** Native K8s Secrets are base64-encoded, not encrypted. Every production deployment must either enable etcd encryption-at-rest (with cloud KMS) or use External Secrets Operator / CSI Driver to eliminate secrets from etcd entirely.

- **Supply chain security has reached production-grade maturity in 2025.** SLSA 1.0, SPDX 3, and the Sigstore ecosystem (cosign, Rekor, Fulcio, Kyverno verifyImages) provide a vendor-neutral, keyless-capable pipeline for image signing, SBOM attestation, and policy-gated admission — achievable with 0.25–0.5 FTE on managed K8s.

---

## Related — Out of Scope

- **On-premises host security and hardening** (firewall rules, OS-level controls, physical access): covered in F46, F47, F71.
- **Cloud-native security service deep dives** (full GuardDuty, Defender for Cloud, SCC feature analysis): covered in F11 (AWS), F19 (Azure), F27 (GCP).
- **K8s platform lifecycle** (cluster upgrades, node pool management, control-plane operations): covered in F52.
- **Service mesh security** (mTLS between services via Istio/Linkerd): closely related to network policy but not covered here — warrants its own research file.

---

## Sources

- [Identity and Access Management — Amazon EKS Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)
- [AWS Authentication for K8s: IAM Roles for Service Accounts (IRSA) — chamila.dev, 2025-03-10](https://chamila.dev/blog/2025-03-10_aws-authentication-for-k8s-iam-roles-for-service-accounts-irsa/)
- [Kubernetes Workload Identity: Secure Implementation Guide — GitGuardian](https://www.gitguardian.com/nhi-hub/how-to-implement-secure-workload-identities-in-kubernetes)
- [Kubernetes Roles: A Practical Guide for 2025 — Plural.sh](https://www.plural.sh/blog/kubernetes-roles-rbac-guide/)
- [About Workload Identity Federation for GKE — Google Cloud Documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)
- [Kubernetes Workload Identity and Access — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/eks-to-aks/workload-identity)
- [Learn how EKS Pod Identity grants pods access to AWS services — Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html)
- [Kubernetes Policy Comparison: Kyverno vs. OPA/Gatekeeper — Nirmata, 2025-02-07](https://nirmata.com/2025/02/07/kubernetes-policy-comparison-kyverno-vs-opa-gatekeeper/)
- [10 Reasons Why Kubernetes Users Choose Kyverno Over OPA Gatekeeper — Nirmata, 2025-04-14](https://nirmata.com/2025/04/14/10-reasons-why-kubernetes-users-choose-kyverno-over-opa-gatekeeper/)
- [Kubernetes Pod Security Admission Explained — alexandre-vazquez.com](https://alexandre-vazquez.com/kubernetes-policy-enforcement-understanding-pod-security-admission-psa/)
- [PSA vs. OPA/Gatekeeper: Customizing Kubernetes Pod Security — Medium](https://medium.com/@ghorbelmohamed37/%EF%B8%8Fpodsecurityadmission-psa-vs-78edcefcf3a1)
- [Kubernetes Network Policies Explained for Production Security — Atmosly](https://atmosly.com/blog/kubernetes-network-policies-security-implementation-guide-2025)
- [Calico vs. Cilium: 9 Key Differences and How to Choose — Tigera](https://www.tigera.io/learn/guides/cilium-vs-calico/)
- [Cilium Explained: Components, Use Cases, Limitations and Alternatives — Tigera](https://www.tigera.io/learn/guides/cilium-vs-calico/cilium/)
- [Network Policy — Cilium 1.19.1 documentation](https://docs.cilium.io/en/stable/network/kubernetes/policy/)
- [Locking Down External Access with DNS-Based Policies — Cilium 1.19.0 documentation](https://docs.cilium.io/en/stable/security/dns/)
- [Safely managing Cilium network policies in Kubernetes — CNCF, 2025-11-06](https://www.cncf.io/blog/2025/11/06/safely-managing-cilium-network-policies-in-kubernetes-testing-and-simulation-techniques/)
- [cilium/cilium — GitHub](https://github.com/cilium/cilium)
- [How to Configure Kubernetes Network Policies for Zero-Trust Security — OneUptime, 2026-01-06](https://oneuptime.com/blog/post/2026-01-06-kubernetes-network-policies-zero-trust/view)
- [aquasecurity/trivy-operator — GitHub](https://github.com/aquasecurity/trivy-operator)
- [How to Use Trivy for Kubernetes Security — OneUptime, 2026-01-27](https://oneuptime.com/blog/post/2026-01-27-trivy-kubernetes-security/view)
- [Admission Controller — trivy-operator — devopstales](https://devopstales.github.io/trivy-operator/2.4/functions/image-validator/)
- [Automate Kubernetes Image Vulnerability Scanning — Pluralsight](https://www.pluralsight.com/labs/aws/automate-kubernetes-image-vulnerability-scanning)
- [Kubernetes Policy Controller — Sigstore](https://docs.sigstore.dev/policy-controller/overview/)
- [Signing Containers — Sigstore](https://docs.sigstore.dev/cosign/signing/signing_with_containers/)
- [Sigstore — Kyverno documentation](https://main.kyverno.io/docs/policy-types/cluster-policy/verify-images/sigstore/)
- [Supply Chain Security: Sigstore and Cosign (Part II) — GitGuardian](https://blog.gitguardian.com/supply-chain-security-sigstore-and-cosign-part-ii/)
- [Secrets Store CSI Driver — Kubernetes SIGs](https://secrets-store-csi-driver.sigs.k8s.io/)
- [Secrets Store CSI Driver vs. External Secrets Operator — KubeBlog](https://www.kubeblog.com/kubernetes/secrets-store-csi-driver-vs-external-secrets-operator/)
- [List of Secrets Management Tools for Kubernetes in 2025 — TechiesCamp](https://blog.techiescamp.com/secrets-management-tools/)
- [Kubernetes Secrets Management: Vault vs Sealed Secrets vs External Secrets (2025) — Atmosly](https://atmosly.com/blog/kubernetes-secrets-management-vault-vs-sealed-secrets-vs-external-secrets-2025)
- [Vault Secrets Store CSI provider — HashiCorp Developer](https://developer.hashicorp.com/vault/docs/deploy/kubernetes/csi)
- [Manage Kubernetes native secrets with the Vault Secrets Operator — HashiCorp Developer](https://developer.hashicorp.com/vault/tutorials/kubernetes-introduction/vault-secrets-operator)
- [Use the Azure Key Vault provider for Secrets Store CSI Driver for AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)
- [Keeping Your Data Safe: ETCD Encryption at Rest in Kubernetes — Medium](https://medium.com/@tamerbenhassan/keeping-your-data-safe-etcd-encryption-at-rest-in-kubernetes-a297250e83e7)
- [A Practical Guide to Kubernetes Encryption at Rest — Plural.sh](https://www.plural.sh/blog/a-practical-guide-to-kubernetes-encryption-at-rest/)
- [Falco — Cloud Native Runtime Security](https://falco.org/)
- [From Observability to Action: Using Falco for Kubernetes Threat Detection — schoenwald.aero, 2025-03-29](https://schoenwald.aero/posts/2025-03-29_falco-for-kubernetes-threat-detection/)
- [Enhancing Kubernetes Security with Falco on OVHcloud MKS — OVHcloud Blog, 2025-02-10](https://blog.ovhcloud.com/enhancing-kubernetes-security-detecting-threats-in-ovhcloud-managed-kubernetes-cluster-mks-audit-logs-with-falco/)
- [Kubernetes Security Tools: An Overview of Falco — Medium](https://medium.com/@noah_h/kubernetes-security-tools-falco-e873831f3d3d)
- [Amazon GuardDuty Extended Threat Detection now supports Amazon EKS — AWS, June 2025](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-guardduty-threat-detection-eks/)
- [Amazon GuardDuty expands Extended Threat Detection coverage to Amazon EKS clusters — AWS Blog](https://aws.amazon.com/blogs/aws/amazon-guardduty-expands-extended-threat-detection-coverage-to-amazon-eks-clusters/)
- [GuardDuty Runtime Monitoring — Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html)
- [Guarding Kubernetes Deployments: Runtime Gating for Vulnerable Images Now Generally Available — Microsoft Tech Community](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/guarding-kubernetes-deployments-runtime-gating-for-vulnerable-images-now-general/4484234)
- [Secure Kubernetes Deployments with Gated Container Images — Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/runtime-gated-overview)
- [Can Cloud Security Tools Protect Kubernetes Environments? — Cymulate](https://cymulate.com/blog/native-cloud-security-kubernetes-defenses/)
- [AWS vs. Azure vs. Google Cloud: Security comparison — Sysdig](https://www.sysdig.com/learn-cloud-native/threat-detection-in-the-cloud-defender-vs-guardduty-vs-security-command-center)
- [AWS Introduces Extended Threat Detection for EKS via GuardDuty — InfoQ, June 2025](https://www.infoq.com/news/2025/06/guardduty-eks/)
- [Software-Supply-Chain Security in 2025: SBOMs, SLSA & Sigstore — Faith Forge Labs](https://faithforgelabs.com/blog_supplychain_security_2025.php)
- [Software Supply Chain Security: SBOM, SLSA, Sigstore (2025) — Elysiate](https://www.elysiate.com/blog/supply-chain-security-sbom-slsa-sigstore-2025)
- [Secure Supply Chain with Sigstore, Cosign & SLSA Framework — IntelligenceX](https://blog.intelligencex.org/secure-supply-chain-with-sigstore-cosign-slsa-framework)
- [How to Sign an SBOM with Cosign — Chainguard Academy](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-sign-an-sbom-with-cosign/)
- [Top 5 hard-earned lessons from the experts on managing Kubernetes — CNCF, 2025-11-18](https://www.cncf.io/blog/2025/11/18/top-5-hard-earned-lessons-from-the-experts-on-managing-kubernetes/)
- [Understanding Workload Identity in Kubernetes: AKS, EKS, GKE — Stakater](https://www.stakater.com/post/understanding-workload-identity-in-kubernetes-a-comprehensive-guide-with-examples-for-aks-eks-and)
- [Understanding Kubernetes Security Posture Management (KSPM) — Sysdig](https://www.sysdig.com/learn-cloud-native/what-is-kubernetes-security-posture-management-kspm)
- [Microsoft Security Blog: Understanding the threat landscape for Kubernetes, 2025-04-23](https://www.microsoft.com/en-us/security/blog/2025/04/23/understanding-the-threat-landscape-for-kubernetes-and-containerized-assets/)
- [Best practices for network policies in Azure Kubernetes Service (AKS) — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/network-policy-best-practices)
- [Cedar: A new approach to policy management for Kubernetes — CNCF, 2025-03-28](https://www.cncf.io/blog/2025/03/28/cedar-a-new-approach-to-policy-management-for-kubernetes/)
