# F58: Deploy & Release Phase Differences

**Research Question:** How do deployment and release strategies differ across on-prem, managed K8s, and cloud-native models, especially for ISVs shipping to customer environments?

---

## Executive Summary

Deployment and release strategy diverges sharply across the three models an ISV evaluates. Cloud-native deployments enable on-demand, sub-hour release cadences with instant, API-driven rollback; managed Kubernetes (EKS/AKS/GKE) adds progressive delivery tooling (Argo Rollouts, Flagger) that approximates cloud-native agility while tolerating customer-owned clusters; on-premises delivery imposes the most friction, requiring ISVs to package every dependency into offline-installable bundles, coordinate change-control windows with customer IT, and accept annual-to-quarterly update cadences driven by enterprise procurement and compliance cycles. The 2025 CNCF Annual Cloud Native Survey found that [82% of container users now run Kubernetes in production](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/), confirming that managed K8s has become the dominant self-managed delivery target; yet air-gapped and on-premises requirements remain non-negotiable for regulated sectors including defense, financial services, and healthcare. ISVs serving heterogeneous customer bases must therefore maintain parallel release engineering pipelines — one optimized for continuous cloud delivery and one for discrete, fully bundled offline releases — resulting in material engineering and support overhead that grows with the number of active major versions in the field.

---

## 1. Deployment Strategies: Blue/Green, Canary, and Rolling

### Cloud-Native

Cloud-native platforms expose deployment strategy as a first-class managed service capability. In July 2025, [Amazon ECS launched built-in blue/green deployments](https://www.infoq.com/news/2025/07/aws-blue-green-ecs/) that operate directly within the ECS service, eliminating the need to configure AWS CodeDeploy. The ECS-native approach provides six lifecycle hooks (pre-scale-up, post-scale-up, production traffic shift, test traffic shift, post-production traffic shift, and post-test traffic shift) that invoke Lambda functions for validation before cutover. AWS CodeDeploy remains available for teams requiring fine-grained canary or linear traffic shifting policies orchestrated through CodePipeline. The ISV operational profile for cloud-native deployments is minimal: traffic shifting, bake time, and validation logic are configured in service definitions rather than in custom tooling.

### Managed Kubernetes

Managed Kubernetes unlocks the full spectrum of advanced deployment strategies through the Kubernetes ecosystem. [Argo Rollouts](https://argoproj.github.io/rollouts/) is a Kubernetes controller and set of CRDs that provides blue-green, canary, canary analysis, experimentation, and progressive delivery features to Kubernetes clusters. A canary rollout releases a new version to a small percentage of production traffic, then [increases exposure in steps when results look healthy](https://akuity.io/blog/automating-blue-green-and-canary-deployments-with-argo-rollouts). Argo Rollouts integrates with ingress controllers and service meshes to leverage their traffic shaping abilities, and queries metrics providers (Prometheus, Datadog, etc.) to drive automated promotion or rollback.

[Rolling update](https://acecloud.ai/blog/kubernetes-deployment-strategies/) is the Kubernetes default — it updates pods gradually by replacing old instances with new ones without downtime. Blue-green requires maintaining two full replica sets simultaneously, doubling resource cost during cutover. The [2025 CNCF End User Survey found Argo CD running in nearly 60% of Kubernetes clusters for application delivery](https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/), with 97% of survey respondents using it in production.

### On-Premises

On-premises deployments have no native traffic-splitting infrastructure. Blue-green deployments require the customer to provision duplicate server capacity and a load balancer capable of weighted routing — conditions rarely guaranteed at customer sites. Canary deployments are effectively infeasible in traditional on-premises environments without a service mesh or ingress layer. Rolling updates are achievable if the ISV ships an installer that updates nodes sequentially, but coordination with customer IT to sequence the update without service interruption is manual. The operative deployment strategy defaults to a maintenance-window, all-at-once replacement.

### Comparison Table

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Deployment Strategies** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| Available strategies | Rolling (manual), blue-green (manual, if infra permits) | Rolling, blue-green, canary, progressive delivery | Rolling, blue-green, canary, linear — platform-managed |
| Representative tools | Ansible, shell scripts, custom installers | Argo Rollouts, Flagger, Helm | AWS CodeDeploy, ECS native B/G, GCP Cloud Deploy |
| Est. FTE | 0.5–1.0 FTE (per deployment event) | 0.25–0.5 FTE (ongoing ops) | 0.1–0.25 FTE (pipeline maintenance) |

---

## 2. Air-Gapped Deployments

Air-gapped environments — networks with no outbound internet access — are non-negotiable requirements for defense, government, and classified financial workloads.

### Packaging Requirements

[Replicated's air gap documentation](https://www.replicated.com/air-gap) defines the core artifact as an `.airgap` bundle: a self-contained archive that carries all container images and dependent subcharts needed to install and run a specific release with no internet access. The ISV must configure the `builder` key in the KOTS HelmChart custom resource to ensure all conditionally-deployed component images are included even when those features are disabled by default in the chart values. [Replicated can transition companies from Helm chart to air gap support in as little as an hour](https://www.replicated.com/air-gap), and 70 of the Fortune 100 companies use Replicated for application management.

The [Replicated Embedded Cluster](https://docs.replicated.com/enterprise/installing-existing-cluster-airgapped) supports installation in existing clusters in air gap mode; alternatively, ISVs can provide assets for a VM/bare metal install via the Embedded Cluster Installer. [Wrapping a Helm chart for air-gap distribution](https://docs.replicated.com/vendor/helm-packaging-airgap-bundles) consists of packaging it into a tar.gz file that includes all container images and dependent subcharts; the resulting file can be distributed through any medium and later unwrapped into a destination OCI registry.

### Dependency Vendoring

All third-party container images referenced in the chart (sidecars, init containers, operator images, monitoring exporters) must be explicitly enumerated and included. ISVs typically maintain a manifest of all image digests per release to enable deterministic air-gap bundle construction. Dependencies that pull images dynamically at runtime (some operators, admission webhooks that fetch external images) must be refactored to use pre-loaded registry references.

### Image Pre-Loading

The bundle is transferred to the customer's environment via physical media (USB, DVD) or a managed transfer process. Customers push the image archive to a private internal registry accessible by the cluster. [Air gap installation with KOTS in an existing cluster](https://docs.replicated.com/enterprise/installing-existing-cluster-airgapped) requires the artifacts to be accessible through a private registry before the install command is executed.

### Offline Installers

For VM/bare metal targets without Kubernetes, ISVs using the Replicated Embedded Cluster ship a standalone installer binary alongside the air-gap bundle. The installer bootstraps a minimal Kubernetes distribution, applies the bundle, and surfaces a web-based admin console for configuration. This approach eliminates the customer's need to pre-provision Kubernetes.

---

## 3. Customer-Site Deployment: Access, Constraints, and Change Management

### Remote Deployment Tooling

ISVs deploying to customer-owned infrastructure must negotiate access in advance. Common access patterns include:

- **VPN + bastion host**: The ISV engineer connects to the customer's VPN, then jumps through an approved bastion node with audit logging enabled.
- **Screen-share / remote desktop**: For regulated environments where no external access is permitted, the ISV's engineer talks a customer engineer through the deployment steps.
- **Deployment runbook delivery**: The ISV provides a detailed, tested runbook and the customer's internal team executes it independently, with the ISV available on a call bridge.

### Customer Access Constraints

[On-premises hosting imposes significant constraints](https://www.graphon.com/blog/isv-hosting-options): "scaling an on-premises infrastructure is complex and expensive" and changes to infrastructure prove "slow and cumbersome, limiting your ability to adjust to changing business needs." Enterprise customers in regulated sectors require every deployment to pass a formal change advisory board (CAB) review before execution. This adds weeks to the lead time for even minor patch releases.

### Change Management Processes

Enterprise IT organizations operating on ITIL frameworks classify software version changes as "standard," "normal," or "emergency" changes, each with different approval timelines. Standard changes (pre-approved, low-risk, documented procedures) can proceed with as little as 24-hour notice. Normal changes require CAB approval, which is typically scheduled weekly or bi-weekly. Emergency changes require emergency CAB convening, which can still take hours.

The ISV must supply documentation sufficient for the CAB submission: architecture diagrams, rollback procedures, estimated downtime windows, and test evidence. ISVs that fail to provide this package extend their time-to-deployment by weeks.

---

## 4. Release Engineering: Artifacts, Release Notes, and Compatibility Matrices

### Release Artifact Types by Model

| Artifact | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| Primary delivery unit | Installer binary + air-gap bundle OR Helm chart + KOTS | Helm chart (OCI registry) / Operator | Container image + Terraform / CDK / IaC |
| Packaging tool | Replicated KOTS, custom shell scripts | Helm 4, Operator SDK | Docker BuildKit, GitHub Actions |
| Distribution channel | Customer download portal, physical media | OCI registry, Artifact Hub | Cloud Marketplace, CI/CD pipeline |
| Signing requirement | Required (GPG / Sigstore) | Required (Helm provenance, cosign) | Optional but recommended |

[Helm 4 was released at KubeCon + CloudNativeCon North America 2025](https://www.cncf.io/announcements/2025/11/12/helm-marks-10-years-with-release-of-version-4/) — the first major update in six years. Helm 4 retains backward compatibility with Helm 3 charts (v2 API charts remain supported) and introduces WebAssembly-based plugins with cross-platform portability. For ISVs, the key improvement is a chart versioning path that lets vendors introduce breaking changes to packages while maintaining stability for existing users.

### Compatibility Matrices

ISVs shipping to on-premises and managed K8s environments must publish and maintain compatibility matrices that document which release version is validated against which version of:

- Kubernetes (e.g., 1.28–1.33)
- The target cloud distribution (EKS, AKS, GKE, OpenShift)
- Dependent operators or infrastructure components
- The customer's OS baseline

[Red Hat OpenShift certification policy](https://docs.redhat.com/en/documentation/red_hat_software_certification/2025/html-single/red_hat_openshift_software_certification_policy_guide/index) illustrates the complexity: ISV certification tools support odd-numbered minor releases for longer lifecycle, and dual-certification across two RHOCP versions is required when the ISV software supports direct upgrades between major application versions.

### Release Notes

On-premises release notes must include: a migration guide, known-issue list, upgrade pre-requisites (disk space, memory requirements, API deprecations), manual steps for CRD upgrades (Helm does not upgrade CRDs automatically), and rollback procedures. Cloud-native release notes are less prescriptive because the platform handles infrastructure state.

---

## 5. Rollback Procedures

Rollback complexity is one of the sharpest differentiators across deployment models.

### Cloud-Native: Near-Instant Rollback

Cloud-native platforms expose rollback as a first-class API operation. AWS ECS blue-green deployments enable [immediate rollback capability by switching traffic back to the previous environment](https://www.featbit.co/articles2025/modern-deploy-rollback-strategies-2025). The previous task definition remains running throughout the deployment window and receives 100% of traffic within seconds of a rollback invocation. No ISV action is required beyond triggering the rollback via the platform API or console. Difficulty: 1/5.

### Managed Kubernetes: Helm Rollback

[`helm rollback`](https://helm.sh/docs/helm/helm_rollback/) rolls a release back to a previous revision using Helm's stored release history. Each `helm upgrade` creates a new revision; the `helm history` command shows all revisions available for rollback. The command is: `helm rollback <release-name> <revision>`. Helm stores release state in Kubernetes Secrets by default, providing persistence. [Automated rollback based on Prometheus or log metrics](https://blog.container-solutions.com/automated-rollback-helm-releases-based-logs-metrics) is achievable via Argo Rollouts' analysis framework, which can trigger rollback if a key KPI degrades below a threshold during a canary step.

[Helm rollback failure modes](https://www.netdata.cloud/academy/helm-chart-rollback-failures/) include stuck states (pending-rollback), revision conflicts, and CRD drift. Because Helm does not manage CRD rollback, schema changes in CRDs applied during an upgrade persist even after a Helm rollback, which can leave the cluster in an inconsistent state unless the ISV ships an explicit CRD rollback procedure. Difficulty: 2–3/5 (2 for stateless apps; 3 when CRDs or persistent storage are involved).

### On-Premises: Manual Rollback

On-premises rollback is the highest-complexity scenario. [Microsoft's documentation for on-premises Dynamics deployments](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/apply-updates-on-premises) describes a process that requires manually downloading rollback packages, restoring database backups, and scheduling another maintenance window. [Database rollbacks are often the most complex and risky type, as data isn't easily reversible, especially if destructive operations like deletes or schema migrations have occurred.](https://www.myshyft.com/blog/deployment-rollback-planning/)

ISVs must document rollback procedures in advance, test them in staging, and include specific version targets, role/responsibility assignments, and stakeholder communication protocols. [Enterprise upgrades can take 6 months or more depending on customization complexity.](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/apply-updates-on-premises) Difficulty: 4–5/5.

### Rollback Comparison Table

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Rollback** | Difficulty: 4–5/5 | Difficulty: 2–3/5 | Difficulty: 1/5 |
| Mechanism | Manual: restore backup, re-execute installer | `helm rollback <release> <revision>` | Platform API / console (traffic switch) |
| Database rollback | Manual restore from backup snapshot | Manual or operator-managed | Managed (Aurora point-in-time, etc.) |
| Time to rollback | Hours to days | Minutes to 30 minutes | Seconds to minutes |
| Automated rollback | Not feasible without custom tooling | Yes — Argo Rollouts + metrics analysis | Yes — platform health checks + CodeDeploy |
| Est. FTE per event | 1.0–2.0 FTE (planned), 2.0+ FTE (emergency) | 0.1–0.25 FTE | 0.0–0.1 FTE (automated) |

---

## 6. Configuration Management: Per-Customer Values and Secrets

### Per-Customer Configuration

ISVs routinely serve dozens to hundreds of enterprise customers, each with unique configuration requirements: ingress hostnames, TLS certificates, database connection strings, feature flags, resource limits, and integration endpoints. The configuration management strategy must scale without requiring ISV engineers to directly edit per-customer files for each deployment.

**Cloud-Native:** Configuration is typically injected via environment variables, AWS Parameter Store, Azure App Configuration, or GCP Secret Manager. Infrastructure as Code (Terraform, CDK) parameterizes per-customer deployments through variable files or workspaces. Automated pipelines apply per-customer stacks from a single parameterized template.

**Managed K8s:** [Helm values files](https://infisical.com/blog/kubernetes-secrets-management-2025) are the standard mechanism. ISVs maintain a `values-<customer>.yaml` per customer, stored in a private Git repository. GitOps tools (Argo CD, Flux) apply the customer-specific values file against the shared chart. [The External Secrets Operator](https://infisical.com/blog/kubernetes-secrets-management-2025) integrates external vaults and secret management systems, pulling secrets from external providers into Kubernetes secrets with automatic rotation and centralized audit logging.

**On-Premises:** Configuration at customer sites arrives via the deployment runbook or via the KOTS admin console (if using Replicated). [KOTS provides a browser-based config screen](https://docs.replicated.com/vendor/releases-about) where customers enter environment-specific values during initial install; those values are persisted and reused during upgrades. Air-gapped deployments cannot use external secrets managers that require internet connectivity, so secrets must either be entered manually into the admin console or injected by the customer's internal secrets vault (HashiCorp Vault Enterprise, CyberArk) if available.

### Secrets Injection Approaches

[For multi-tenancy specifically](https://www.redhat.com/en/blog/a-guide-to-secrets-management-with-gitops-and-kubernetes), the recommended approach uses namespace-scoped `SecretStore` resources with namespace-local credentials, so each tenant authenticates to the secrets vault with its own service account rather than shared credentials. [Secrets (database credentials, API keys) should never be stored directly in Git, even in private repositories.](https://microsoft.github.io/code-with-engineering-playbook/CI-CD/gitops/secret-management/)

[The `helm-secrets` plugin](https://blog.gitguardian.com/how-to-handle-secrets-in-helm/) enables encrypted Helm chart values using SOPS (Secrets OPerationS), which offloads cryptographic work while keeping encrypted secrets in Git. The Secrets Store CSI Driver integrates HashiCorp Vault, AWS Secrets Manager, and Azure Key Vault directly into the pod filesystem.

---

## 7. Multi-Version Support: Maintaining Tooling for Multiple Active Versions

ISVs in enterprise markets routinely carry 3–5 major versions simultaneously in customer production environments. This creates a release engineering burden distinct from the development backlog.

### Version Lifecycle with Channels

[Replicated's channel architecture](https://docs.replicated.com/vendor/releases-about) is the reference model for ISV multi-version management. A release is promoted to one or more channels (Unstable, Beta, Stable, or custom channels). Customers assigned to a channel can only install releases promoted to that channel. An ISV can simultaneously maintain:

- A `stable-v2` channel for customers on the prior major version
- A `stable-v3` channel for customers on the current major version
- A `beta` channel for early adopters of the next major version

[Once promoted, a release cannot be edited](https://docs.replicated.com/vendor/releases-about), ensuring immutability. Vendors can archive releases to hide them from new installs while existing deployments continue to function. [October 2025 Replicated release highlights](https://www.replicated.com/blog/replicated-monthly-release-highlights----october-2025) include major usability upgrades to release management and customer views in the Vendor Portal.

### OLM and Operator-Based Multi-Version

For Kubernetes Operator-based delivery, the [Operator Lifecycle Manager (OLM)](https://olm.operatorframework.io/) manages upgrades through update channels and a `replaces` field in the ClusterServiceVersion (CSV). OLM upgrades operators one version at a time along a defined upgrade graph until the channel head is reached, preventing skipped versions that could leave the cluster in an unsupported state. The migration from OLMv0 to OLMv1 currently [has no concrete migration strategy due to conceptual differences between the two versions](https://github.com/operator-framework/operator-lifecycle-manager), representing an active risk for ISVs invested in OLM-based delivery.

### Compatibility Matrix Maintenance Cost

Each active major version requires the ISV to:
1. Maintain a separate Helm chart branch or operator bundle
2. Validate the chart against all supported Kubernetes versions in the compatibility matrix
3. Publish distinct air-gap bundles for each active release
4. Test rollback procedures for each active version
5. Update release notes and runbooks

At 3 active major versions × 4 supported Kubernetes minor versions, an ISV faces a 12-cell compatibility matrix requiring ongoing validation. [Red Hat's OpenShift certification guidance](https://docs.redhat.com/en/documentation/red_hat_software_certification/2025/html-single/red_hat_openshift_software_certification_policy_guide/index) advises dual-certification on adjacent RHOCP versions to support EUS-to-EUS upgrade paths.

---

## 8. Deployment Frequency: How the Model Shapes Release Cadence

### Cloud-Native: Continuous Delivery

[The 2024 DORA Report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) documents that elite DevOps performers deploy on demand — multiple times per day. [Elite performers deploy 182x more frequently, with 8x lower change failure rates, and 127x faster change lead times](https://octopus.com/devops/metrics/dora-metrics/) compared to low performers. Cloud-native deployment removes infrastructure gate functions: there are no change windows, no customer IT coordination requirements, no packaging steps. The ISV ships code when it is ready.

[GitOps is expected to be further entrenched as the primary delivery model in 2025](https://cloudnativenow.com/contributed-content/implementing-ci-cd-for-cloud-native-applications-the-right-way/), with stronger integrations for policy, security, and cost governance. [77% of respondents have to some degree adopted GitOps as a software engineering methodology](https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/) according to the CNCF End User Survey.

### Managed Kubernetes: Weekly to Monthly

Managed Kubernetes allows ISVs to ship frequently to their own managed clusters. However, when Managed Kubernetes is deployed into customer environments (the ISV installs the software into customer-owned EKS/AKS/GKE clusters), the customer change management process re-introduces friction. Major version upgrades still require customer approval and scheduling. Patch releases and security updates can often be applied on a weekly cadence with customer-pre-approved "standard change" status. An ISV serving enterprise customers on managed K8s should plan for 2–4 week average cycle time from release to customer deployment for minor versions, and 6–12 weeks for major versions.

### On-Premises: Quarterly to Annual

[SAP's on-premises S/4HANA product updates annually with new features](https://www.houseblend.io/articles/on-premise-hybrid-erp-2025), illustrating the industry norm. [Banking and financial services typically operate on quarterly release cycles due to regulatory requirements and security concerns.](https://www.eltegra.ai/blog/software-release-frequency-how-often-should-you-deploy-in-2025) For ISVs, this means:

- Feature work completed in Q1 may not reach on-premises customers until Q3 or Q4
- Security patches must be handled through an emergency release track with a compressed (but still manual) packaging and distribution process
- The ISV must maintain the capability to patch multiple active versions simultaneously when a CVE is disclosed

[Microsoft announced an annual release cadence for Configuration Manager](https://techcommunity.microsoft.com/blog/configurationmanagerblog/announcing-the-annual-release-cadence-for-microsoft-configuration-manager/4464794), signaling that even major platform vendors are rationalizing on-premises release complexity by reducing cadence.

### Deployment Frequency Comparison

| Dimension | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Typical feature release cadence** | Quarterly–Annual | Bi-weekly–Monthly | Daily–Weekly |
| **Security patch cadence** | Days–Weeks (emergency track) | Hours–Days | Hours (automated) |
| **Change coordination required** | Yes — CAB, maintenance window | Partial — customer approval for major | No |
| **Customer deployment lag** | Weeks–Months after release | Days–Weeks | Minutes–Hours |
| **Deployment frequency difficulty** | 4/5 | 2/5 | 1/5 |

---

## Key Takeaways

- **Air-gapped delivery is a distinct engineering discipline.** ISVs targeting regulated sectors must build and maintain a parallel release pipeline capable of producing fully self-contained `.airgap` bundles — every image, every dependency, no internet assumptions. Platforms like [Replicated](https://www.replicated.com/air-gap) reduce this from months of custom engineering to hours, but the ISV still owns the manifest discipline and testing matrix.

- **Rollback complexity is the sharpest risk differentiator.** Cloud-native rollback is seconds via traffic switch; Helm rollback is minutes but breaks on CRD changes; on-premises rollback can consume days and requires a pre-tested runbook, a maintenance window, and often a database restore. ISVs must design upgrade procedures with rollback testability as a first-class requirement, especially for stateful workloads.

- **Deployment frequency is inversely proportional to deployment model complexity.** Cloud-native supports multiple deployments per day; managed K8s in customer environments realistically achieves bi-weekly patch cadence; on-premises enforces quarterly-to-annual feature releases. ISVs must set customer expectations and SLA structures accordingly — customers on on-premises should not expect cloud-native feature velocity.

- **Multi-version support is a compounding operational cost.** Each active major version multiplies the number of Helm chart branches, air-gap bundles, compatibility matrix cells, and rollback procedures the ISV must maintain. Replicated's channel architecture and OLM's upgrade graph each provide structural tools for managing this, but the ISV must deliberately plan version end-of-life dates and customer migration timelines to prevent the support surface from growing unboundedly.

- **Release engineering for Kubernetes is maturing rapidly.** [Helm 4, released in November 2025](https://www.cncf.io/announcements/2025/11/12/helm-marks-10-years-with-release-of-version-4/), delivers WebAssembly-based plugins, server-side apply, and a future-proof chart versioning path while maintaining backward compatibility with all Helm 3 charts. [Argo CD is running in nearly 60% of Kubernetes clusters](https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/) for application delivery, establishing GitOps as the de-facto ISV delivery model for Kubernetes targets in 2025.

---

## Related — Out of Scope

- **Build pipeline construction** (CI systems, artifact signing, SBOM generation) — See [F57: Build Phase].
- **Operational monitoring, alerting, and SRE practices post-deployment** — See [F59: Operations].
- **Business impact of multi-version support** (support contracts, EOL policy, revenue implications) — See [F62: Version Management Business Impact].
- **Secrets and certificate management infrastructure** — See [F47: On-Prem Secrets & Certs].
- **Kubernetes packaging patterns in detail** — See [F53: Portable K8s ISV Delivery].
- **Operator internals and CRD lifecycle** — See [F54: K8s Operators].
- **CI/CD pipeline infrastructure for on-premises targets** — See [F48: On-Prem CI/CD].

---

## Sources

- [Argo Rollouts — Kubernetes Progressive Delivery Controller](https://argoproj.github.io/rollouts/)
- [Automating Blue-Green & Canary Deployments with Argo Rollouts — Akuity](https://akuity.io/blog/automating-blue-green-and-canary-deployments-with-argo-rollouts)
- [Kubernetes Deployment Strategies: Rolling, Blue-Green & Canary — AceCloud](https://acecloud.ai/blog/kubernetes-deployment-strategies/)
- [AWS Introduces Built-in Blue-Green Deployment Capability for ECS — InfoQ, July 2025](https://www.infoq.com/news/2025/07/aws-blue-green-ecs/)
- [CodeDeploy blue/green deployments for Amazon ECS — AWS Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html)
- [Distribute Self-Hosted Software to Air-Gapped Environments — Replicated](https://www.replicated.com/air-gap)
- [Package Air Gap Bundles for Helm Charts — Replicated Docs](https://docs.replicated.com/vendor/helm-packaging-airgap-bundles)
- [Air Gap Installation in Existing Clusters with KOTS — Replicated Docs](https://docs.replicated.com/enterprise/installing-existing-cluster-airgapped)
- [About Channels and Releases — Replicated Docs](https://docs.replicated.com/vendor/releases-about)
- [Replicated Monthly Release Highlights — October 2025](https://www.replicated.com/blog/replicated-monthly-release-highlights----october-2025)
- [Enterprise Helm Chart Best Practices for ISVs — Replicated](https://www.replicated.com/enterprise-helm)
- [Helm Marks 10 Years With Release of Version 4 — CNCF, November 2025](https://www.cncf.io/announcements/2025/11/12/helm-marks-10-years-with-release-of-version-4/)
- [Helm Rollback Documentation — helm.sh](https://helm.sh/docs/helm/helm_rollback/)
- [Helm Chart Rollback Failures — Netdata Academy](https://www.netdata.cloud/academy/helm-chart-rollback-failures/)
- [Automated Rollback of Helm Releases Based on Logs or Metrics — Container Solutions](https://blog.container-solutions.com/automated-rollback-helm-releases-based-logs-metrics)
- [Modern Deployment Rollback Techniques for 2025 — Featbit](https://www.featbit.co/articles2025/modern-deploy-rollback-strategies-2025)
- [Enterprise Rollback Strategies — MyShyft](https://www.myshyft.com/blog/deployment-rollback-planning/)
- [Apply Updates to On-Premises Deployments — Microsoft Learn (Dynamics 365)](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/deployment/apply-updates-on-premises)
- [Kubernetes Established as the De Facto Operating System for AI — CNCF 2025 Annual Survey, January 2026](https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/)
- [CNCF End User Survey: Argo CD as Majority Adopted GitOps Solution — CNCF, July 2025](https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/)
- [Announcing the 2024 DORA Report — Google Cloud](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)
- [Understanding The 4 DORA Metrics — Octopus Deploy](https://octopus.com/devops/metrics/dora-metrics/)
- [Cloud-Native 2024: CNCF Annual Survey](https://www.cncf.io/reports/cncf-annual-survey-2024/)
- [Implementing CI/CD for Cloud-Native Applications — Cloud Native Now](https://cloudnativenow.com/contributed-content/implementing-ci-cd-for-cloud-native-applications-the-right-way/)
- [Red Hat OpenShift Software Certification Policy Guide 2025](https://docs.redhat.com/en/documentation/red_hat_software_certification/2025/html-single/red_hat_openshift_software_certification_policy_guide/index)
- [Operator Lifecycle Manager — operator-framework.github.io](https://operator-framework.github.io/operator-controller/)
- [OLM GitHub — operator-framework/operator-lifecycle-manager](https://github.com/operator-framework/operator-lifecycle-manager)
- [Kubernetes Secrets Management in 2025 — Infisical](https://infisical.com/blog/kubernetes-secrets-management-2025)
- [A Guide to Secrets Management with GitOps and Kubernetes — Red Hat](https://www.redhat.com/en/blog/a-guide-to-secrets-management-with-gitops-and-kubernetes)
- [Secrets Management with GitOps — Microsoft Engineering Fundamentals Playbook](https://microsoft.github.io/code-with-engineering-playbook/CI-CD/gitops/secret-management/)
- [Helm Secrets: Secure Kubernetes Secrets Management Guide — GitGuardian](https://blog.gitguardian.com/how-to-handle-secrets-in-helm/)
- [ERP Deployment in 2025: On-Premise and Hybrid Models — Houseblend](https://www.houseblend.io/articles/on-premise-hybrid-erp-2025)
- [Software Release Frequency 2025: Industry Benchmarks — EltegraAI](https://www.eltegra.ai/blog/software-release-frequency-how-often-should-you-deploy-in-2025)
- [Announcing the Annual Release Cadence for Microsoft Configuration Manager — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/configurationmanagerblog/announcing-the-annual-release-cadence-for-microsoft-configuration-manager/4464794)
- [ISV Hosting Options in 2025 — GO-Global / Graphon](https://www.graphon.com/blog/isv-hosting-options)
- [Argo CD vs Flux CD — Zignuts](https://www.zignuts.com/blog/argo-cd-vs-flux-cd--comparison)
- [How ISVs and Startups Scale on DigitalOcean Kubernetes — DigitalOcean](https://www.digitalocean.com/blog/how-isvs-startups-scale-digitalocean-kubernetes-best-practices)
- [Blue/Green ECS Deployments with CloudFormation — Shine Solutions, November 2025](https://shinesolutions.com/2025/11/17/blue-green-ecs-deployments-with-cloudformation/)
