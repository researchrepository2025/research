# F60: Update, Patch & Scale Phase Differences

**Research File:** F60
**Wave:** 8 — Operational Lifecycle
**Scope:** Updates, patching, and scaling across On-Premises, Managed Kubernetes, and Cloud-Native deployment models
**Date:** 2026-02-19

---

## Executive Summary

The three deployment models examined in this research plan diverge most sharply during the ongoing operational phases of software updates, security patching, and capacity scaling — not during initial deployment. Cloud-native ISVs can deliver security patches within hours of CVE disclosure and scale capacity with a single API call, while on-premises deployments require weeks or months of customer coordination to apply equivalent patches and hardware procurement cycles that span weeks. Managed Kubernetes occupies a middle position: rolling updates and horizontal pod autoscaling provide operational agility, but the ISV still depends on customer change-management windows for node-pool and cluster-level upgrades. The gap in security patching speed is particularly acute: in 2025, [roughly 28% of exploited CVEs were weaponized within one day of disclosure](https://deepstrike.io/blog/vulnerability-statistics-2025), yet [77% of enterprises require more than one week to deploy patches](https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025) — a mismatch with severe compliance and liability implications for ISVs shipping on-premises software. Compliance certification maintenance (SOC 2, HIPAA, FedRAMP) compounds these differences, requiring ISVs to maintain audit evidence across every deployed version, effectively multiplying compliance overhead in proportion to the number of distinct customer versions in the field.

---

## 1. Update Delivery Models

### 1.1 Cloud-Native: Continuous Deployment

Cloud-native ISVs operate a single shared infrastructure under their direct control. Updates are deployed via CI/CD pipelines using blue-green or canary strategies with no customer coordination required.

[FACT] Blue-green deployment switches all traffic from an old environment to a new one with near-zero downtime by maintaining two identical environments simultaneously.
URL: [https://www.webapper.com/saas-blue-green-deployments/](https://www.webapper.com/saas-blue-green-deployments/)

[FACT] Canary releases route a small percentage of user traffic to the new version first, allowing validation before full rollout.
URL: [https://circleci.com/blog/canary-vs-blue-green-downtime/](https://circleci.com/blog/canary-vs-blue-green-downtime/)

Deployment frequency in cloud-native SaaS is limited only by the ISV's CI/CD pipeline maturity. There are no customer-side change advisory boards, no maintenance windows to schedule, and no version fragmentation across the install base. All tenants run the same version at all times.

**Difficulty (Update Delivery):** 1/5 — Fully under ISV control; tooling (GitHub Actions, ArgoCD, Flux) is mature and managed.

### 1.2 Managed Kubernetes: Rolling Updates with Coordination

Managed Kubernetes (EKS/AKS/GKE) enables zero-downtime application updates via Kubernetes rolling update strategies.

[FACT] "Rolling updates allow Deployments' updates to take place with zero downtime by incrementally updating Pods instances with new ones."
URL: [https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)

Application-layer updates can be pushed by the ISV when the customer grants cluster access or uses a GitOps pull model. However, Kubernetes control-plane and node-pool upgrades remain customer-coordinated, as they involve potential node reboots and are classified as significant infrastructure changes. Cluster upgrades follow the managed service provider's support calendar.

[FACT] Amazon EKS is committed to offering support for at least three Kubernetes versions at any given time; end-of-standard-support dates are announced at least 60 days in advance. EKS provides 26 months of total support (14 months standard + 12 months extended, paid).
URL: [https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)

[FACT] AKS Long Term Support versions receive a 24-month support commitment from their GA dates (announced July 2025).
URL: [https://blog.aks.azure.com/2025/07/25/aks-lts-announcement](https://blog.aks.azure.com/2025/07/25/aks-lts-announcement)

**Difficulty (Update Delivery):** 3/5 — Application updates are largely automated; cluster/node upgrades require customer scheduling.

### 1.3 On-Premises: Customer-Coordinated Maintenance Windows

On-premises deployments give the ISV no direct path to update customer infrastructure.

[QUOTE] "Deploying updates, patches, and new features across hundreds or thousands of customer installations—each with different configurations, network constraints, and change management policies—becomes a logistical nightmare."
— Distr ISV Guide
URL: [https://distr.sh/glossary/isv-meaning/](https://distr.sh/glossary/isv-meaning/)

[QUOTE] "Without automated update systems, customers run different software versions, making it difficult for ISVs to support legacy versions while pushing customers toward current releases."
— Distr ISV Guide
URL: [https://distr.sh/glossary/isv-meaning/](https://distr.sh/glossary/isv-meaning/)

The result is a fragmented install base where the ISV must maintain and support multiple concurrent versions — each with its own dependency matrix, security posture, and compatibility profile. See [F53: Portable K8s ISV Delivery] for multi-version packaging approaches.

**Difficulty (Update Delivery):** 5/5 — Each update is a coordinated release event requiring customer acceptance, internal testing, and scheduled maintenance.

---

## 2. Security Patching Urgency and CVE Response

This is the domain where the deployment model gap is most operationally dangerous.

### 2.1 The Shrinking Exploitation Window

[STATISTIC] In 2025, roughly 28% of exploited CVEs were weaponized within 1 day of their disclosure.
URL: [https://deepstrike.io/blog/vulnerability-statistics-2025](https://deepstrike.io/blog/vulnerability-statistics-2025)

[STATISTIC] More than 48,000 CVEs were tracked in 2025, up approximately 20% from 2024 and 66% from 2023.
URL: [https://jerrygamblin.com/2026/01/01/2025-cve-data-review/](https://jerrygamblin.com/2026/01/01/2025-cve-data-review/)

[QUOTE] "The era of 'patch available, but we can wait a few weeks' is over, given current attack velocities."
— DeepStrike Vulnerability Statistics 2025
URL: [https://deepstrike.io/blog/vulnerability-statistics-2025](https://deepstrike.io/blog/vulnerability-statistics-2025)

[STATISTIC] Within the first week of a CVE release, over 54% of critical vulnerabilities face active exploitation.
URL: [https://deepstrike.io/blog/vulnerability-statistics-2025](https://deepstrike.io/blog/vulnerability-statistics-2025)

[FACT] Google Project Zero announced plans to cut vulnerability disclosure timelines to 7 days in 2025, putting further pressure on vendors to patch immediately.
URL: [https://www.webpronews.com/google-project-zero-to-cut-vulnerability-disclosures-to-7-days-in-2025/](https://www.webpronews.com/google-project-zero-to-cut-vulnerability-disclosures-to-7-days-in-2025/)

### 2.2 Enterprise Patching Reality vs. Requirement

[STATISTIC] 77% of organizations need more than a week to deploy patches (Adaptiva 2025 State of Patch Management Report, survey of 250+ security and IT professionals).
URL: [https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025](https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025)

[STATISTIC] 59% of organizations say it takes at least two weeks to begin deployment after a patch has been released (Adaptiva 2025).
URL: [https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025](https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025)

[STATISTIC] 98% of IT and security professionals say patching disrupts their work and forces resource reallocation (Adaptiva 2025).
URL: [https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025](https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025)

### 2.3 CISA KEV Mandatory Timelines

[FACT] CISA's Known Exploited Vulnerabilities (KEV) catalog reached 1,484 entries by end of 2025, growing 20% year-over-year.
URL: [https://www.securityweek.com/cisa-kev-catalog-expanded-20-in-2025-topping-1480-entries/](https://www.securityweek.com/cisa-kev-catalog-expanded-20-in-2025-topping-1480-entries/)

[FACT] Recent CISA KEV additions in late 2025 mandated Federal Civilian Executive Branch (FCEB) agencies patch within 1-2 weeks of catalog addition; for example, CVE-2025-59718 (Fortinet) was added December 16, 2025 with a remediation deadline of December 23, 2025.
URL: [https://www.cisa.gov/news-events/alerts/2025/12/16/cisa-adds-one-known-exploited-vulnerability-catalog](https://www.cisa.gov/news-events/alerts/2025/12/16/cisa-adds-one-known-exploited-vulnerability-catalog)

### 2.4 CVE Response Time Comparison by Deployment Model

| Model | ISV Patch Deploy Time | Customer Patch Adoption | Net Exposure Window |
|---|---|---|---|
| Cloud-Native | Hours (same-day CI/CD) | Automatic (no customer action) | Hours |
| Managed K8s | Hours (app layer) / Days (node layer) | Days–weeks (cluster change window) | Days–weeks |
| On-Premises | Days (package build) | Weeks–months (customer scheduling) | Weeks–months |

**Difficulty (Security Patching):**
- Cloud-Native: 1/5 — ISV patches immediately; tenants are automatically protected.
- Managed K8s: 2/5 — Application patches deploy quickly; node/OS patches require coordination.
- On-Premises: 5/5 — ISV cannot enforce patch timing; customers with slow change management remain exposed.

---

## 3. Breaking Changes: API and Schema Migrations

### 3.1 The Multi-Version Problem on On-Premises

When ISVs cannot control upgrade timing, they must ensure that every breaking change is backward compatible with every supported deployed version.

[QUOTE] "You need to adapt the database in a way that the old and the new version of your application can work with the database, meaning that all migrations need to be backward-compatible as long as you're running at least one instance of the old version of your application."
— Thorben Janssen, thorben-janssen.com
URL: [https://thorben-janssen.com/update-database-schema-without-downtime/](https://thorben-janssen.com/update-database-schema-without-downtime/)

### 3.2 API Versioning and Deprecation Timelines

[FACT] B2B SaaS API deprecation best practice calls for a 6-month announcement period, 12 months of active migration support, and 18-24 months total before removal for enterprise clients.
URL: [https://www.wudpecker.io/blog/api-versioning-strategies-for-b2b-saas](https://www.wudpecker.io/blog/api-versioning-strategies-for-b2b-saas)

[FACT] Qualys announced in August 2025 that customers would receive an overall 12 months to shift to the latest API versions.
URL: [https://notifications.qualys.com/api/2025/08/17/updates-on-api-versioning-standards-deprecation-timelines](https://notifications.qualys.com/api/2025/08/17/updates-on-api-versioning-standards-deprecation-timelines)

[FACT] The Sunset HTTP Header (RFC 8594) is now recommended as standard practice to alert API consumers about upcoming deprecations directly through their API interactions.
URL: [https://apidog.com/blog/api-versioning-deprecation-strategy/](https://apidog.com/blog/api-versioning-deprecation-strategy/)

On-premises ISVs supporting N-1 or N-2 versions must maintain API compatibility across all those versions simultaneously — a constraint that cloud-native ISVs can eliminate by controlling the upgrade cadence themselves.

---

## 4. Database Migrations Across Deployed Versions

### 4.1 Schema Migration Tooling

[FACT] Flyway uses a linear database versioning system that increments on each versioned change; rollback is enterprise-only (Community edition does not support rollback).
URL: [https://www.bytebase.com/blog/flyway-vs-liquibase/](https://www.bytebase.com/blog/flyway-vs-liquibase/)

[FACT] Liquibase supports rollback via `rollback-one-changeset` or full rollback, with enhanced Rollback Reports in paid tiers; it supports XML, YAML, JSON, and SQL migration formats.
URL: [https://www.bytebase.com/blog/flyway-vs-liquibase/](https://www.bytebase.com/blog/flyway-vs-liquibase/)

[FACT] In 2025, Liquibase added a backup-based baseline approach and enhanced flow capabilities with conditionals and advanced orchestration features.
URL: [https://www.bytebase.com/blog/flyway-vs-liquibase/](https://www.bytebase.com/blog/flyway-vs-liquibase/)

### 4.2 Zero-Downtime Migration Pattern

For deployments where the ISV cannot guarantee all instances are on the same version, the recommended pattern is the expand-contract (parallel-change) approach:

1. **Expand phase** — Add new schema elements while preserving old ones; deploy new application version that reads both.
2. **Migrate phase** — Backfill data to new structure while old version runs.
3. **Contract phase** — Remove old schema elements only after all instances have upgraded.

[QUOTE] "You need to break these operations into a backward-compatible part which you perform before you update your application and a second part that you execute after you updated all application instances."
— Thorben Janssen
URL: [https://thorben-janssen.com/update-database-schema-without-downtime/](https://thorben-janssen.com/update-database-schema-without-downtime/)

See [F41: On-Prem Relational DB] for detailed database operational coverage.

### 4.3 Difficulty by Deployment Model

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| DB Schema Migration | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
|  | Expand-contract mandatory; multi-version state persists for months | Rolling upgrades reduce window; tenant isolation possible | Single schema version at all times; migrations execute under ISV control |
|  | Flyway/Liquibase with versioned migrations; manual coordination | Flyway/Liquibase in init containers; GitOps-triggered | Managed DB migration tools; automated pre-deploy hooks |
|  | Est. FTE: 0.5–1.0 (shared across versions) | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |

*FTE estimates assume a mid-size ISV serving 50 enterprise customers; estimates cover migration authoring, testing, rollout coordination, and rollback readiness.*

---

## 5. Dependency Updates: OS, Runtime, and Library

### 5.1 Testing Matrix Complexity

On-premises deployments force ISVs to maintain a multi-dimensional testing matrix: every supported OS version, every supported runtime (e.g., JVM, Python, Node.js), and every supported database version must be validated against every application version in active support.

[FACT] The average on-premises enterprise endpoint has nearly 3,000 applications installed, each potentially introducing dependency conflicts when updated.
URL: [https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025](https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025)

In cloud-native and managed Kubernetes models, the ISV controls the base container image, OS, and runtime. All customers run on the same dependency stack at all times, collapsing the testing matrix to a single version.

### 5.2 Container Images and OS Patching in Managed Kubernetes

Managed Kubernetes node pools use managed OS images (Amazon Linux 2023, Ubuntu, Windows Server) that are patched by the cloud provider. Application container images remain the ISV's responsibility.

[FACT] AKS patch versions can be introduced as they become available; once available, patches have a two-month minimum lifecycle.
URL: [https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions)

Container image OS patching requires ISVs to rebuild and redeploy base images on a regular cadence — typically triggered by upstream OS or runtime CVE advisories. See [F47: On-Prem Secrets & Certs] for certificate rotation, which is a parallel dependency lifecycle concern.

---

## 6. Scaling: Adding Capacity Across Deployment Models

### 6.1 Cloud-Native: API-Driven Instantaneous Scaling

[FACT] Cloud environments enable resources to be provisioned "within minutes or seconds" in response to demand, automatically scaling up and down without manual intervention.
URL: [https://www.nops.io/blog/cloud-scalability/](https://www.nops.io/blog/cloud-scalability/)

[FACT] For most AWS Auto Scaling groups, it takes approximately 5 minutes to spin up a new EC2 instance; with Warm Pools pre-configured, launch time drops from over 4 minutes to approximately 36 seconds.
URL: [https://aws.amazon.com/blogs/compute/scaling-your-applications-faster-with-ec2-auto-scaling-warm-pools/](https://aws.amazon.com/blogs/compute/scaling-your-applications-faster-with-ec2-auto-scaling-warm-pools/)

[FACT] The default ECS instance warmup period is 300 seconds (5 minutes).
URL: [https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-scaling-behavior.html](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-scaling-behavior.html)

Serverless cloud-native architectures (AWS Lambda, Azure Functions, Google Cloud Run) scale to zero and to thousands of concurrent instances with no ISV operational involvement.

### 6.2 Managed Kubernetes: Pod and Node Autoscaling

[FACT] Kubernetes Horizontal Pod Autoscaler (HPA) automatically adjusts the number of pod replicas in response to observed metrics; metric reporting delays in production surges often stretch to 15–30 seconds.
URL: [https://scaleops.com/blog/hpa-vs-vpa-understanding-kubernetes-autoscaling-and-why-its-not-enough-in-2025/](https://scaleops.com/blog/hpa-vs-vpa-understanding-kubernetes-autoscaling-and-why-its-not-enough-in-2025/)

[FACT] When HPA scales pods but nodes are full, Cluster Autoscaler adding capacity can take a few minutes (new node provisioning).
URL: [https://www.atlantbh.com/how-hpa-vpa-and-cluster-autoscaler-work-together-in-kubernetes-and-where-they-clash/](https://www.atlantbh.com/how-hpa-vpa-and-cluster-autoscaler-work-together-in-kubernetes-and-where-they-clash/)

[FACT] HPA and VPA can conflict when deployed simultaneously: HPA scales out because pods look overloaded while VPA increases CPU requests, causing HPA to scale back in — creating an oscillating scaling loop.
URL: [https://scaleops.com/blog/hpa-vs-vpa-understanding-kubernetes-autoscaling-and-why-its-not-enough-in-2025/](https://scaleops.com/blog/hpa-vs-vpa-understanding-kubernetes-autoscaling-and-why-its-not-enough-in-2025/)

Node pool autoscaling in managed K8s (EKS Managed Node Groups, AKS Node Autoprovisioner, GKE Autopilot) provides elastic capacity up to the limits configured by the customer's cloud account quotas.

### 6.3 On-Premises: Hardware Procurement as the Bottleneck

[FACT] Standard server delivery timelines in 2025: Dell 4–6 weeks, Lenovo 6–8 weeks, HP 5–7 weeks.
URL: [https://inteleca.com/it-industry-news/hpc-hardware-procurement-strategies/](https://inteleca.com/it-industry-news/hpc-hardware-procurement-strategies/)

[FACT] High-end GPU server lead times in 2025 range from 6 to 12 months due to supply chain constraints.
URL: [https://inteleca.com/it-industry-news/hpc-hardware-procurement-strategies/](https://inteleca.com/it-industry-news/hpc-hardware-procurement-strategies/)

[FACT] Scaling from a small data center to a larger one may involve several months of lead time for new hardware and infrastructure.
URL: [https://primesecured.com/cloud-vs-on-premises-it-infrastructure/](https://primesecured.com/cloud-vs-on-premises-it-infrastructure/)

On-premises customers must also plan for physical rack space, power, cooling, and network capacity — all of which require capital expenditure approval and physical installation time separate from the hardware procurement cycle.

### 6.4 Scaling Comparison Table

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| Scaling | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| Speed to capacity | Weeks–months (hardware procurement) | Minutes (node autoscaling) | Seconds–minutes (auto-scaling groups, serverless) |
| ISV involvement | None (customer's problem) | Config/tuning guidance | Fully managed by ISV |
| Key tooling | Physical data center ops | HPA, VPA, Cluster Autoscaler, Karpenter | AWS Auto Scaling, GCP Cloud Run, Azure VMSS |
| Est. FTE: ISV side | 0 (customer bears cost) | 0.25–0.5 | 0.1–0.25 |

---

## 7. Deprecation and End-of-Life: Sunsetting Old Versions

[FACT] In 2025, approximately 120 Microsoft software offerings reached end-of-support, end-of-servicing, or retirement.
URL: [https://learn.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2025](https://learn.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2025)

[FACT] Industry standards including PCI-DSS, HIPAA, and ISO 27001 require organizations to use supported software; running end-of-life systems can result in audit failures, fines, and loss of certifications.
URL: [https://ezo.io/assetsonar/blog/end-of-life-vs-end-of-support-it-compliance-guide/](https://ezo.io/assetsonar/blog/end-of-life-vs-end-of-support-it-compliance-guide/)

[FACT] End-of-life announcements for on-premises software are accelerating as vendors move toward cloud-first recurring revenue models.
URL: [https://listedtech.com/blog/end-of-life-announcements-and-the-inevitable-move-to-the-cloud/](https://listedtech.com/blog/end-of-life-announcements-and-the-inevitable-move-to-the-cloud/)

For on-premises ISVs, sunsetting a version is not a unilateral decision. Enterprise customers may resist upgrades due to:
- Internal testing requirements before approving new software versions
- Dependency on the old version's behavior (undocumented integration assumptions)
- Budget cycles that do not align with the ISV's deprecation timeline
- Air-gapped or regulated environments that slow change approval

[FACT] A phased deprecation model for on-premises enterprise software typically follows: 6-month announcement, 12 months of active migration support, 18–24 months total before removal.
URL: [https://www.wudpecker.io/blog/api-versioning-strategies-for-b2b-saas](https://www.wudpecker.io/blog/api-versioning-strategies-for-b2b-saas)

Cloud-native ISVs control upgrade timing entirely. Version sunset is an internal engineering decision with no customer dependency, though API deprecations still require customer-facing notification for integrations.

---

## 8. Compliance: Maintaining Certifications Across All Deployed Versions

### 8.1 SOC 2 Scope Across Deployment Models

[FACT] SOC 2 was designed for service providers that store client data in the cloud; it is specifically scoped to systems and organizational controls within the service provider's boundary.
URL: [https://www.strongdm.com/blog/fisma-vs-fedramp-nist-vs-iso-soc2-vs-hipaa-iso27001-vs-soc2](https://www.strongdm.com/blog/fisma-vs-fedramp-nist-vs-iso-soc2-vs-hipaa-iso27001-vs-soc2)

For cloud-native ISVs, SOC 2 scope is well-defined and stable: it covers the ISV's production cloud environment. A single audit covers all customers because all customers are on the same infrastructure.

For on-premises ISVs, the audit boundary is harder to define. Each customer deployment is a separate system with its own controls, configurations, and operational procedures. The ISV can only attest to the software they ship — not how it is operated by the customer. Evidence collection must account for every supported version.

[FACT] SOC 2 audit preparation in 2025 requires continuous evidence collection throughout the review period — not just point-in-time snapshots.
URL: [https://www.complyjet.com/blog/soc-2-compliance-guide](https://www.complyjet.com/blog/soc-2-compliance-guide)

### 8.2 FedRAMP Continuous Monitoring Requirements

[FACT] FedRAMP continuous monitoring in 2025 requires some controls to be validated on a minute-by-minute basis; policy controls may be validated quarterly or semi-annually depending on control type.
URL: [https://www.carahsoft.com/blog/regscale-fedramp-20x-modernizing-cloud-security-authorization-through-automation-and-continuous-assurance-blog-2025](https://www.carahsoft.com/blog/regscale-fedramp-20x-modernizing-cloud-security-authorization-through-automation-and-continuous-assurance-blog-2025)

[FACT] FedRAMP 20x modernization requires compliance controls to be technically engineered into CI/CD pipelines — a "compliance-as-code" approach.
URL: [https://www.carahsoft.com/blog/regscale-fedramp-20x-modernizing-cloud-security-authorization-through-automation-and-continuous-assurance-blog-2025](https://www.carahsoft.com/blog/regscale-fedramp-20x-modernizing-cloud-security-authorization-through-automation-and-continuous-assurance-blog-2025)

[FACT] FedRAMP classifies software updates that are "likely to affect the security state of the system" as significant changes, requiring security impact analysis and formal change process documentation before deployment.
URL: [https://www.fedramp.gov/resources/documents/Continuous_Monitoring_Playbook.pdf](https://www.fedramp.gov/resources/documents/Continuous_Monitoring_Playbook.pdf)

[FACT] New FedRAMP Security Inbox Requirements apply to all cloud service providers beginning January 5, 2026.
URL: [https://www.fedramp.gov/2025-11-18-fedramp-shutdown-updates/](https://www.fedramp.gov/2025-11-18-fedramp-shutdown-updates/)

### 8.3 Compliance Difficulty Table

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| SOC 2 / HIPAA / FedRAMP | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| Scope definition | Fragmented; ISV attests only to software, not deployment | Partially shared; customer controls node/cluster; ISV controls app | Single boundary; ISV controls all evidence |
| Evidence collection | Manual; per-customer; per-version | Semi-automated; cloud provider inherits some controls | Automated; single environment |
| Version risk | Every version in the field is a separate audit surface | Fewer versions due to rolling updates | Single version; no version fragmentation |
| Est. FTE: compliance | 0.5–1.5 FTE (scales with version count) | 0.5–1.0 FTE | 0.25–0.5 FTE |

*FTE estimates for a mid-size ISV serving 50 enterprise customers; includes evidence collection, control monitoring, and audit response.*

---

## 9. Master Comparison Table

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Update Delivery** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Customer maintenance windows; version fragmentation | Rolling updates for app; cluster upgrades require scheduling | Continuous deployment; all tenants on single version |
| | Manual package distribution; ISV tooling (SCCM, Helm chart releases) | Helm/ArgoCD/FluxCD | ArgoCD, GitHub Actions, cloud-native CI/CD |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |
| **Security Patching** | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | 59% of customers take 2+ weeks; ISV has no enforcement lever | App patches in hours; node patches in days | Same-day patches; customers auto-protected |
| | CVE response measured in weeks | CVE response: hours (app), days (nodes) | CVE response: hours |
| | Est. FTE: 0.5–1.0 (build/release only) | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **DB Schema Migration** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Expand-contract required; months of multi-version state | Rolling upgrades reduce window | Single schema; ISV-controlled timing |
| | Flyway/Liquibase with manual coordination | Flyway/Liquibase in init containers | Managed migration tools |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Scaling** | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Hardware procurement: 4–12 weeks | Node autoscaling: minutes | API call: seconds–minutes |
| | Physical infrastructure ops | HPA, Cluster Autoscaler, Karpenter | AWS Auto Scaling, GCP Cloud Run, Azure VMSS |
| | Est. FTE: 0 (customer-borne) | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Compliance** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Fragmented audit surface; per-customer, per-version | Partial inheritance; shared responsibility | Single boundary; fully automated evidence |
| | Manual evidence; scales with install base | Semi-automated | Compliance-as-code via CI/CD |
| | Est. FTE: 0.5–1.5 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |

*FTE assumptions: mid-size ISV serving 50 enterprise customers; includes active work and on-call burden; excludes initial deployment.*

---

## Key Takeaways

- **Security patching is the most time-critical asymmetry.** With 28% of CVEs exploited within 24 hours of disclosure and 77% of enterprises taking more than a week to deploy patches, on-premises ISVs face an irreconcilable gap between exploit velocity and customer patch adoption speed. Cloud-native ISVs close this gap entirely; managed Kubernetes closes it at the application layer.

- **Version fragmentation is the root cause of on-premises operational complexity.** Every operational concern — DB migrations, API deprecation, compliance evidence, dependency testing — becomes multiplicatively harder when customers run different versions simultaneously. Cloud-native ISVs eliminate this problem by definition.

- **Scaling in the cloud is an API call; scaling on-premises is a capital project.** Standard server lead times of 4–8 weeks (and GPU server lead times of 6–12 months) mean that on-premises customers cannot respond to traffic spikes in meaningful time. Cloud-native environments scale in seconds to minutes with no ISV involvement.

- **Compliance certification scope is proportional to version count.** SOC 2, HIPAA, and FedRAMP audit surfaces expand with every deployed version in the field. Cloud-native ISVs maintain a single, well-bounded audit scope; on-premises ISVs may need to account for dozens of distinct configurations across their customer base.

- **Managed Kubernetes is a credible middle path but not a free lunch.** Application-layer updates and horizontal scaling approach cloud-native speed, but cluster and node upgrades remain customer-coordinated, creating a two-tier patching problem that must be explicitly managed in SLAs and deployment contracts.

---

## Related — Out of Scope

- **Initial deployment complexity** (covered in F58) — the first-install process and how it differs across models is a prerequisite to, but distinct from, the ongoing update/patch/scale lifecycle described here.
- **Day-2 operational tooling** (covered in F59) — monitoring, alerting, log aggregation, and incident response overlap with but extend beyond the patch/update scope defined for this file.
- **Business impact of version fragmentation** (deferred to Wave 9) — the cost and revenue implications (support contract overhead, churn risk from delayed patches) are out of scope for this technical file.
- **CI/CD pipeline construction** (covered in F48) — the mechanics of building the update artifact and pushing it through a pipeline are a prerequisite; this file covers what happens after the artifact is built.

---

## Sources

1. [Distr ISV Guide: ISV Meaning and Deployment Challenges](https://distr.sh/glossary/isv-meaning/)
2. [DeepStrike: Vulnerability Statistics 2025](https://deepstrike.io/blog/vulnerability-statistics-2025)
3. [Adaptiva: 2025 State of Patch Management Report](https://adaptiva.com/blog/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025)
4. [Adaptiva: 2025 State of Patch Management Report (PR Release)](https://www.prnewswire.com/news-releases/adaptivas-report-reveals-automation-as-a-top-priority-for-patch-management-in-2025-302349897.html)
5. [Jerry Gamblin: 2025 CVE Data Review](https://jerrygamblin.com/2026/01/01/2025-cve-data-review/)
6. [WebPronews: Google Project Zero 7-Day Disclosure Policy](https://www.webpronews.com/google-project-zero-to-cut-vulnerability-disclosures-to-7-days-in-2025/)
7. [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
8. [CISA: Adds One Known Exploited Vulnerability (CVE-2025-59718)](https://www.cisa.gov/news-events/alerts/2025/12/16/cisa-adds-one-known-exploited-vulnerability-catalog)
9. [SecurityWeek: CISA KEV Catalog Expanded 20% in 2025](https://www.securityweek.com/cisa-kev-catalog-expanded-20-in-2025-topping-1480-entries/)
10. [Kubernetes: Rolling Update Introduction](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
11. [Kubernetes: Patch Releases Cadence](https://kubernetes.io/releases/patch-releases/)
12. [Amazon EKS: Kubernetes Version Lifecycle](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)
13. [AKS: Long Term Support 24-Month Announcement (July 2025)](https://blog.aks.azure.com/2025/07/25/aks-lts-announcement)
14. [AKS: Supported Kubernetes Versions](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions)
15. [GKE: Release Channels Documentation](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
16. [CircleCI: Canary vs Blue-Green Deployment](https://circleci.com/blog/canary-vs-blue-green-downtime/)
17. [Webapper: SaaS Blue/Green Deployments](https://www.webapper.com/saas-blue-green-deployments/)
18. [Thorben Janssen: Update Database Schema Without Downtime](https://thorben-janssen.com/update-database-schema-without-downtime/)
19. [Bytebase: Flyway vs Liquibase 2026 Comparison](https://www.bytebase.com/blog/flyway-vs-liquibase/)
20. [Wudpecker: API Versioning Strategies for B2B SaaS](https://www.wudpecker.io/blog/api-versioning-strategies-for-b2b-saas)
21. [Qualys: Updates on API Versioning Standards & Deprecation Timelines (August 2025)](https://notifications.qualys.com/api/2025/08/17/updates-on-api-versioning-standards-deprecation-timelines)
22. [APIdog: API Versioning and Deprecation Strategy](https://apidog.com/blog/api-versioning-deprecation-strategy/)
23. [nOps: Cloud Scalability — Types and Benefits](https://www.nops.io/blog/cloud-scalability/)
24. [AWS: Scaling Applications Faster with EC2 Auto Scaling Warm Pools](https://aws.amazon.com/blogs/compute/scaling-your-applications-faster-with-ec2-auto-scaling-warm-pools/)
25. [AWS: ECS Managed Scaling Behavior](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-scaling-behavior.html)
26. [ScaleOps: HPA vs VPA — Kubernetes Autoscaling 2025](https://scaleops.com/blog/hpa-vs-vpa-understanding-kubernetes-autoscaling-and-why-its-not-enough-in-2025/)
27. [Atlantbh: How HPA, VPA and Cluster Autoscaler Work Together](https://www.atlantbh.com/how-hpa-vpa-and-cluster-autoscaler-work-together-in-kubernetes-and-where-they-clash/)
28. [Inteleca: HPC Hardware Procurement Strategies 2025](https://inteleca.com/it-industry-news/hpc-hardware-procurement-strategies/)
29. [PrimeSecured: Cloud vs On-Premises Infrastructure](https://primesecured.com/cloud-vs-on-premises-it-infrastructure/)
30. [Microsoft: End of Support 2025 Products](https://learn.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2025)
31. [EZO/AssetSonar: End of Life vs End of Support 2025](https://ezo.io/assetsonar/blog/end-of-life-vs-end-of-support-it-compliance-guide/)
32. [ListEdTech: EOL Announcements and the Move to Cloud](https://listedtech.com/blog/end-of-life-announcements-and-the-inevitable-move-to-the-cloud/)
33. [StrongDM: HIPAA, NIST, ISO, FedRAMP, FISMA, SOC2 Comparison](https://www.strongdm.com/blog/fisma-vs-fedramp-nist-vs-iso-soc2-vs-hipaa-iso27001-vs-soc2)
34. [ComplyJet: SOC 2 Compliance Guide 2025](https://www.complyjet.com/blog/soc-2-compliance-guide)
35. [Carahsoft: FedRAMP 20x Modernization and Compliance-as-Code](https://www.carahsoft.com/blog/regscale-fedramp-20x-modernizing-cloud-security-authorization-through-automation-and-continuous-assurance-blog-2025)
36. [FedRAMP: Continuous Monitoring Playbook v1.0 (November 2025)](https://www.fedramp.gov/resources/documents/Continuous_Monitoring_Playbook.pdf)
37. [FedRAMP: Post-Shutdown Updates November 2025](https://www.fedramp.gov/2025-11-18-fedramp-shutdown-updates/)
38. [Linford & Co: FedRAMP 2025 Overhaul Key Updates](https://linfordco.com/blog/fedramp-2025-overhaul-updates/)
