# F19: Azure Security Services

**Research Question:** What managed security services does Azure provide for identity, encryption, secrets, and threat detection, and what operational burden does each eliminate?

**Scope:** Azure security services only — identity (Entra ID), secrets and key management (Key Vault), certificate management, posture and workload protection (Defender for Cloud), governance (Azure Policy), SIEM/SOAR (Microsoft Sentinel), network DDoS mitigation, and confidential computing. Networking topology covered in F21.

---

## Executive Summary

Microsoft Azure offers one of the most integrated security service stacks of any cloud provider, spanning identity, key management, posture management, threat detection, and hardware-level workload isolation. For an ISV deploying AI-driven SaaS on Azure, these services collectively eliminate the need to operate a standalone identity provider, certificate authority, HSM fleet, SIEM platform, or DDoS scrubbing infrastructure — capabilities that would require multiple specialized FTEs and substantial capital expenditure in an on-premises or self-hosted model. Microsoft Entra ID (formerly Azure AD) serves as the foundational identity plane, covering workforce SSO, customer-facing CIAM, and privileged access governance through a single platform priced at $6–$9 per user per month at the P1/P2 tier. Azure Key Vault eliminates secrets sprawl and HSM operational burden at transaction-based pricing starting at $0.03 per 10,000 operations. Microsoft Defender for Cloud provides a free foundational CSPM tier with no-configuration secure scoring, while paid tiers add agentless vulnerability scanning, attack path analysis, and workload protection starting at $4.906 per server per month. Across all eight service domains examined, cloud-native deployment on Azure consistently reduces operational difficulty to the 1–2/5 range versus 4–5/5 for equivalent self-hosted implementations.

---

## 1. Microsoft Entra ID: Identity Platform

### Overview

Microsoft Entra ID (rebranded from Azure Active Directory) is Microsoft's cloud identity platform providing authentication, authorization, single sign-on (SSO), and identity governance for both workforce and external identities. It is the Zero Trust policy engine underpinning all Azure access control.

[Microsoft Entra ID overview](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new) — Microsoft Learn

### Pricing Tiers

| Plan | Price | Key Capabilities |
|------|-------|-----------------|
| Free | $0 | Basic SSO, MFA, user/group management |
| P1 | $6.00/user/month | Conditional Access, hybrid identity, SSPR |
| P2 | $9.00/user/month | PIM, Identity Protection, Access Reviews, risk-based Conditional Access |

[FACT] Microsoft Entra ID P1 is priced at $6.00 per user per month and P2 at $9.00 per user per month.
URL: [Microsoft Entra Plans and Pricing](https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing)

[FACT] Microsoft 365 E3 and Business Premium include Entra ID P1; Microsoft 365 E5 includes Entra ID P2, offering bundled pricing advantages for organizations already in the Microsoft ecosystem.
URL: [Microsoft Entra Plans and Pricing](https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing)

### Conditional Access

Conditional Access is described by Microsoft as "the Zero Trust policy engine that integrates signals to secure access to resources." It evaluates user, device, location, application, and risk signals simultaneously to enforce granular access policies.

[QUOTE] "Organizations can reduce complexity and accelerate their Zero Trust path by extending adaptive conditional access policies across identities, agents, endpoints, devices, and networks."
— Microsoft Entra Conditional Access documentation
URL: [Microsoft Entra Conditional Access: Zero Trust Policy Engine](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

[FACT] The Conditional Access Optimization Agent in Microsoft Entra (2025) monitors for new users or apps not covered by existing policies, identifies necessary updates to close security gaps, and recommends quick fixes for identity teams.
URL: [What's new in Microsoft Entra — June 2025](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-%E2%80%93-june-2025/4352579)

### Privileged Identity Management (PIM)

PIM provides just-in-time (JIT) privileged access with time-bound role activation, approval workflows, MFA enforcement on elevation, and a full audit trail.

[QUOTE] "Privileged Identity Management (PIM) is a service in Microsoft Entra ID that enables you to manage, control, and monitor access to important resources in your organization. With PIM you can provide as-needed and just-in-time access to Azure resources, Microsoft Entra resources, and other Microsoft online services like Microsoft 365 or Microsoft Intune."
— Microsoft Learn
URL: [What is Privileged Identity Management?](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)

[FACT] PIM provides time-based and approval-based role activation to mitigate the risks of excessive, unnecessary, or misused access permissions. PIM sends notifications when roles are activated and maintains an audit history for compliance and review purposes.
URL: [Plan a Privileged Identity Management deployment](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan)

[FACT] PIM meets ISO 27001, PCI-DSS, and NIST privileged access requirements by providing clear trails for internal audits, external assessments, and breach investigations.
URL: [Implementing Privileged Identity Management (PIM): Enhancing Security Through Just-in-Time Access](https://techcommunity.microsoft.com/discussions/microsoft-365/implementing-privileged-identity-management-pim-enhancing-security-through-just-/4430502)

**Operational burden eliminated:** Without PIM, ISVs must manually track who holds standing privileged access to production resources, conduct periodic access reviews manually, and enforce MFA for privileged operations through separate tooling. PIM automates all of these workflows within the existing identity platform at no additional per-feature cost (included in P2).

### External Identities (B2B / B2C / CIAM)

[FACT] Microsoft Entra External ID is the next-generation CIAM solution that consolidates B2B collaboration and B2C customer identity into a single unified platform. Effective May 1, 2025, Azure AD B2C P1/P2 are no longer available for new customers; all new deployments must use Entra External ID.
URL: [Microsoft to End Sale of Azure AD B2B/B2C on May 1, 2025](https://envisionit.com/resources/articles/microsoft-to-end-sale-of-azure-ad-b2bb2c-on-may-1-2025-shifting-to-entra-id-external-identities/)

[FACT] Microsoft Entra External ID is free for the first 50,000 monthly active users (MAU). Beyond this threshold, pricing is $0.03 per MAU.
URL: [External ID pricing — Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-identities-pricing)

[FACT] Entra External ID provides self-service registration, adaptive access, SSO, and bring-your-own-identity (BYOI) capabilities for external user scenarios including customers, partners, and citizens.
URL: [Microsoft Entra External ID overview](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview)

### Operational Profile: Entra ID

| Dimension | On-Premises (LDAP/AD) | Managed K8s + Self-Hosted IdP | Cloud-Native (Entra ID) |
|---|---|---|---|
| Difficulty | 4/5 | 4/5 | 2/5 |
| Key requirements | AD DS infrastructure, PKI for LDAPS, federation servers | Keycloak/Dex deployment, cert rotation, HA config | Tenant configuration, policy authoring |
| Representative tools | Active Directory, ADFS, Shibboleth | Keycloak, Dex, OIDC providers | Entra ID, Conditional Access, PIM |
| Est. FTE | 1.0–2.0 FTE (dedicated IAM engineer) | 0.5–1.0 FTE | 0.25–0.5 FTE |

*FTE assumption: mid-size ISV serving 50 enterprise customers with ~500 internal workforce identities.*

---

## 2. Azure Key Vault: Key Management, Secrets, and Certificates

### Overview

Azure Key Vault is a cloud service for securely storing and accessing secrets (API keys, passwords, connection strings), cryptographic keys, and TLS/SSL certificates. It eliminates secrets sprawl, hardcoded credentials, and the operational burden of managing dedicated HSM hardware.

[QUOTE] "Azure Key Vault lets you easily provision, manage, and deploy public and private TLS/SSL certificates for use with Azure and your internal connected resources."
— Microsoft Learn
URL: [About Azure Key Vault certificates](https://learn.microsoft.com/en-us/azure/key-vault/certificates/about-certificates)

### Service Tiers and Pricing

| Tier | Use Case | Key Cost | Operations Cost |
|------|----------|----------|-----------------|
| Standard | Software-protected keys, secrets | No per-key charge | $0.03/10,000 operations |
| Premium | HSM-protected keys (FIPS 140-2 Level 2) | RSA-2048: $1.00/key/month | $0.03/10,000 operations |
| Managed HSM | Single-tenant FIPS 140-3 Level 3 HSM | — | $3.20/hour per HSM pool (Standard B1) |

[STATISTIC] Azure Key Vault Standard and Premium tier: secrets operations cost $0.03 per 10,000 transactions. Certificate renewals are billed at $3.00 per renewal request.
URL: [Azure Key Vault Pricing: Complete Guide](https://infisical.com/blog/azure-key-vault-pricing)

[STATISTIC] Azure Key Vault Premium tier: RSA-2048 HSM-protected keys cost $1.00 per key per month plus $0.03 per 10,000 transactions. RSA-3072, RSA-4096, and ECC keys cost $5.00 per key per month (first 250 keys).
URL: [Azure Key Vault Pricing: Complete Guide](https://infisical.com/blog/azure-key-vault-pricing)

[STATISTIC] Azure Managed HSM is billed at a fixed hourly rate of approximately $3.20 per hour per HSM pool (Standard B1), not on a per-transaction basis.
URL: [Azure Managed HSM Overview](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview)

[FACT] Secrets, Keys, and Certificates stored in Key Vault are not charged for storage — only operations are billed.
URL: [Azure Key Vault Pricing: Complete Guide](https://infisical.com/blog/azure-key-vault-pricing)

### Managed HSM

[QUOTE] "Azure Key Vault Managed HSM is a fully managed, highly available, single-tenant, standards-compliant cloud service that enables you to safeguard cryptographic keys for your cloud applications, using FIPS 140-3 Level 3 validated HSMs."
— Microsoft Learn
URL: [Azure Managed HSM Overview](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview)

[FACT] Each Managed HSM instance is dedicated to a single customer and consists of a cluster of multiple HSM partitions. Each HSM cluster uses a separate customer-specific security domain that cryptographically isolates each customer's HSM cluster.
URL: [Azure Managed HSM Overview](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview)

[FACT] Managed HSM handles HSM provisioning, configuration, patching, and maintenance automatically. If hardware fails, member partitions are automatically migrated to healthy nodes.
URL: [Azure Managed HSM Overview](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview)

### Operational Burden Eliminated

[QUOTE] "Instead of scattered configuration files across different environments, you get a single source of truth for all your secrets, which eliminates the common problem of 'secret sprawl,' where teams lose track of where sensitive information is stored."
— Azure Key Vault Tutorial, DataCamp
URL: [Azure Key Vault Tutorial: A Beginner's Guide to Cloud Secret Management](https://www.datacamp.com/tutorial/azure-key-vault-tutorial)

[FACT] Using Azure Managed Identities for app and service connections to Key Vault eliminates hardcoded credentials and removes the need for explicit credential management in application code.
URL: [Secure your Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault)

[FACT] Key Vault enables automatic certificate renewal for integrated CAs (DigiCert, GlobalSign), eliminating the manual rotation burden that causes certificate expiry incidents. Certificates can be configured to renew before expiration automatically.
URL: [About Azure Key Vault certificates](https://learn.microsoft.com/en-us/azure/key-vault/certificates/about-certificates)

### Operational Profile: Azure Key Vault

| Dimension | On-Premises | Managed K8s (External Secrets Operator) | Cloud-Native (Key Vault) |
|---|---|---|---|
| Difficulty | 5/5 | 3/5 | 1/5 |
| Key requirements | HSM hardware procurement, rack/stack, firmware mgmt, FIPS audit | ESO deployment, sync config, IAM binding per namespace | Policy assignment, managed identity binding |
| Representative tools | Thales Luna, Utimaco HSMs; Vault by HashiCorp | External Secrets Operator, HashiCorp Vault | Azure Key Vault, Managed HSM |
| Est. FTE | 0.5–1.0 FTE (HSM ops) | 0.25–0.5 FTE | 0.05–0.1 FTE |

---

## 3. Azure Managed Certificates: Free TLS for App Service and Front Door

### App Service Managed Certificates

[FACT] The App Service Managed Certificate is a free, turn-key solution for securing custom DNS names in Azure App Service. Certificates are issued by DigiCert and renewed automatically by Azure as long as DNS prerequisites remain in place.
URL: [App Service Managed Certificate (ASMC) Changes — July 28, 2025](https://learn.microsoft.com/en-us/azure/app-service/app-service-managed-certificate-changes-july-2025)

[FACT] Starting July 28, 2025, Azure App Service Managed Certificates use HTTP Token validation for both apex and subdomains (via `https://<hostname>/.well-known/pki-validation/fileauth.txt`), driven by industry-wide Multi-Perspective Issuance Corroboration (MPIC) compliance requirements from DigiCert's migration to a new validation platform.
URL: [App Service Managed Certificate (ASMC) Changes — July 28, 2025](https://learn.microsoft.com/en-us/azure/app-service/app-service-managed-certificate-changes-july-2025)

### Azure Front Door Managed Certificates

[FACT] There is no additional cost for Azure Front Door-managed TLS certificates in the Premium tier. Certificates are issued, installed, and renewed automatically by Microsoft.
URL: [Do the managed certificates in Azure Front Door Premium have any cost?](https://learn.microsoft.com/en-us/answers/questions/5560015/do-the-managed-certificates-in-azure-front-door-pr)

[FACT] For Azure Front Door Classic and Azure CDN Classic, managed certificates will no longer be supported starting August 15, 2025. Customers must switch to Bring Your Own Certificate (BYOC) or migrate to Azure Front Door Standard/Premium before this date.
URL: [Changes to the Managed TLS Feature](https://docs.azure.cn/en-us/security/fundamentals/managed-tls-changes)

**Operational burden eliminated:** Zero manual certificate issuance, installation, or renewal for App Service and Front Door workloads. Eliminates the class of outage caused by expired certificates — a top-5 source of SaaS availability incidents in self-managed environments.

---

## 4. Microsoft Defender for Cloud: CSPM and CWPP

### Overview

Microsoft Defender for Cloud is a cloud-native application protection platform (CNAPP) combining Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP) functions. It covers Azure, AWS, and GCP resources from a single pane.

[QUOTE] "Microsoft Defender for Cloud provides advanced security posture capabilities including agentless vulnerability scanning, attack path analysis, integrated data-aware security posture, code to cloud contextualization, and an intelligent cloud security graph."
— Microsoft Azure
URL: [Microsoft Defender for Cloud — CSPM and CWPP](https://azure.microsoft.com/en-us/products/defender-for-cloud)

### CSPM Tiers and Pricing

| Tier | Price | Capabilities |
|------|-------|-------------|
| Foundational CSPM | Free | Continuous assessments, security recommendations, Secure Score, Microsoft Cloud Security Benchmark across Azure/AWS/GCP |
| Defender CSPM | Pay-as-you-go per resource | Agentless vulnerability scanning, attack path analysis, data-aware posture, code-to-cloud, cloud security graph |

[FACT] Foundational CSPM is free and provides continuous security assessments, Secure Score, and the Microsoft Cloud Security Benchmark across Azure, AWS, and GCP with no configuration required beyond enabling Defender for Cloud on a subscription.
URL: [What is Cloud Security Posture Management (CSPM)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management)

[FACT] Defender CSPM billing is based only on Server, Storage account, Database, and Serverless resource counts. Billing for Serverless resources begins on February 27, 2026, where 1 billable resource = 8 functions and/or web apps.
URL: [Pricing — Microsoft Defender for Cloud](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/)

### Secure Score

[FACT] The Cloud Secure Score aggregates security findings into a single score so organizations can assess, at a glance, their current security situation — the higher the score, the lower the identified risk level.
URL: [Cloud secure score in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls)

[FACT] In 2025, Microsoft introduced a new risk-based Cloud Secure Score available in the Microsoft Defender portal that incorporates asset risk factors and asset criticality for more accurate prioritization of high-risk recommendations.
URL: [What's new in Microsoft Defender for Cloud features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes)

[FACT] Defender for Cloud calculates each security control every eight hours for each Azure subscription or each AWS/GCP cloud connector.
URL: [Cloud secure score in Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls)

### Vulnerability Assessment

[FACT] Defender for Cloud vulnerability assessment is deployed for virtual machines, containers, and SQL databases to identify security weaknesses across all resource types. As of 2025, it includes open-source dependency vulnerability scanning powered by Trivy in filesystem mode to automatically detect OS and library vulnerabilities across GitHub and Azure DevOps repositories.
URL: [What's new in Microsoft Defender for Cloud features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes)

### CWPP Workload Protection Pricing

| Workload | Plan | Price |
|----------|------|-------|
| Servers | Plan 1 | $4.906/server/month |
| Servers | Plan 2 | $14.60/server/month |
| App Service | — | $14.60/instance/month |
| SQL Databases | — | $15/instance/month |
| Storage | — | $10/storage account/month |

[STATISTIC] Microsoft Defender for Servers Plan 1 is priced at $4.906 per server per month. Plan 2 is $14.60 per server per month.
URL: [Pricing — Microsoft Defender for Cloud](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/)

[FACT] Organizations can save up to 22% when pre-purchasing Microsoft Defender for Cloud Commit Units versus pay-as-you-go pricing.
URL: [Pricing — Microsoft Defender for Cloud](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/)

### Operational Profile: Defender for Cloud

| Dimension | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| Difficulty | 5/5 | 3/5 | 1/5 (Foundational) / 2/5 (Advanced) |
| Key requirements | OpenSCAP/Qualys deployment, agent management, correlation logic | Kubernetes security scanner (Falco, Trivy), manual policy authoring | Enable subscription-level plan, review recommendations |
| Representative tools | Qualys, Rapid7, OpenSCAP, Wazuh | Falco, Trivy, kube-bench | Defender for Cloud, Defender CSPM |
| Est. FTE | 1.0–1.5 FTE | 0.5–0.75 FTE | 0.1–0.25 FTE |

---

## 5. Azure Policy: Governance and Compliance Enforcement

### Overview

Azure Policy is a governance service that enforces organizational standards and assesses compliance at scale. It operates at the control-plane level — preventing non-compliant resource deployments and auto-remediating existing drift.

[QUOTE] "Azure Policy helps to enforce organizational standards and to assess compliance at-scale. Through its compliance dashboard, it provides an aggregated view to evaluate the overall state of the environment, with the ability to drill down to the per-resource, per-policy granularity."
— Microsoft Learn
URL: [Overview of Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

[FACT] Azure Policy is offered at no additional cost to Azure subscribers.
URL: [Azure Policy Cloud and Compliance Management](https://azure.microsoft.com/en-us/products/azure-policy)

### Key Capabilities

[FACT] Azure Policy integrates natively with GitHub and Azure DevOps to manage policies-as-code and surface policy compliance assessments in deployment workflows (CI/CD pipeline gates).
URL: [Everything New in Azure Governance @ Build 2025](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/everything-new-in-azure-governance--build-2025/4415414)

[FACT] Azure Policy supports bulk remediation for existing non-compliant resources and automatic remediation for new resources, eliminating the need to manually correct configuration drift.
URL: [Overview of Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview)

[FACT] 2025 additions include user-based exemptions, caller-type based enforcement (user or service principal), and IP filtering — currently in private preview ahead of general availability.
URL: [Everything New in Azure Governance @ Build 2025](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/everything-new-in-azure-governance--build-2025/4415414)

[FACT] Azure Policy includes SSH Posture Control via new built-in policies that enable declarative management of SSH configuration settings at scale, enforcing compliance with industry standards across VM fleets.
URL: [Everything New in Azure Governance @ Build 2025](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/everything-new-in-azure-governance--build-2025/4415414)

**Operational burden eliminated:** In on-premises or self-managed environments, compliance enforcement requires dedicated tooling (Chef InSpec, Puppet, Ansible playbooks for drift detection) and periodic manual audits. Azure Policy enforces and remediates continuously at zero incremental cost, with coverage extending to multi-cloud (AWS, GCP via Arc).

### Operational Profile: Azure Policy / Governance

| Dimension | On-Premises | Managed K8s (OPA/Gatekeeper) | Cloud-Native (Azure Policy) |
|---|---|---|---|
| Difficulty | 4/5 | 3/5 | 1/5 |
| Key requirements | Configuration management tooling, audit scripts, manual review cycles | OPA Gatekeeper deployment, rego policy authoring, admission controller mgmt | Policy assignment, initiative grouping |
| Representative tools | Chef InSpec, Puppet, Ansible | OPA Gatekeeper, Kyverno | Azure Policy, Azure Blueprints |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.05–0.1 FTE |

---

## 6. Microsoft Sentinel: Cloud-Native SIEM and SOAR

### Overview

Microsoft Sentinel is a cloud-native Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platform built on Azure Log Analytics. It eliminates the need to deploy, scale, and maintain on-premises SIEM infrastructure.

### Pricing

[STATISTIC] Microsoft Sentinel Pay-As-You-Go pricing is approximately $4.30–$5.20 per GB of data ingested (varies by region).
URL: [Microsoft Sentinel Pricing in 2025](https://underdefense.com/industry-pricings/microsoft-sentinel-pricing/)

[STATISTIC] Commitment tier pricing for Microsoft Sentinel starts at approximately $296 per 100 GB/day for organizations with predictable high-volume ingestion, providing discounted rates versus PAYG.
URL: [Plan costs and understand pricing and billing — Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/billing)

[FACT] New workspaces can enable Microsoft Sentinel with the first 10 GB/day ingested on Analytics logs free for 31 days, with both Log Analytics data ingestion and Microsoft Sentinel analysis charges waived during the trial period.
URL: [Plan costs and understand pricing and billing — Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/billing)

[FACT] Certain data sources — including Azure Activity Logs and Office 365 Audit Logs — can be ingested into Sentinel at no additional cost.
URL: [Plan costs and understand pricing and billing — Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/billing)

### SOAR Playbooks

[FACT] Microsoft Sentinel's SOAR capabilities use automation rules and playbooks in response to security threats to increase SOC effectiveness and save time and resources.
URL: [Automate Threat Response with Playbooks in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/automate-responses-with-playbooks)

[FACT] In Microsoft Sentinel, playbooks are based on workflows built in Azure Logic Apps. This gives playbooks access to all Logic Apps integration and orchestration capabilities and easy-to-use visual design tools across 900+ connectors.
URL: [Automation in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation)

[FACT] Starting in July 2025, new Microsoft Sentinel customers are automatically onboarded and redirected to the Microsoft Defender portal as the primary interface, unifying Sentinel's SIEM capabilities with Defender XDR.
URL: [Automation in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation)

### Threat Hunting

[FACT] Microsoft Sentinel automation rules allow users to manage incident handling automation from a central location — automatically tagging, assigning, or closing incidents, and applying playbooks across multiple analytics rules at once.
URL: [Automation in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation)

**Operational burden eliminated:** Self-hosting a SIEM (Splunk, IBM QRadar, or an ELK stack) requires infrastructure provisioning, index cluster management, license renewal, parser/connector development, and 24/7 availability engineering. Sentinel scales automatically with ingestion volume and requires no index infrastructure management.

### Operational Profile: Microsoft Sentinel vs. Self-Hosted SIEM

| Dimension | On-Premises SIEM | Managed K8s (ELK/OpenSearch) | Cloud-Native (Sentinel) |
|---|---|---|---|
| Difficulty | 5/5 | 4/5 | 2/5 |
| Key requirements | SIEM hardware, license mgmt, parser dev, HA cluster ops | ELK cluster deployment, index lifecycle mgmt, Logstash pipelines | Log source connectors, analytic rule authoring |
| Representative tools | Splunk Enterprise, IBM QRadar, ArcSight | Elasticsearch, OpenSearch, Logstash | Microsoft Sentinel, Logic Apps |
| Est. FTE | 1.5–2.0 FTE (SIEM engineer + analyst) | 1.0–1.5 FTE | 0.25–0.5 FTE (analyst only; no platform ops) |

---

## 7. Azure DDoS Protection: Network-Level DDoS Mitigation

### Tiers and Pricing

[FACT] Azure DDoS Protection offers two tiers: IP Protection and Network Protection.
URL: [About Azure DDoS Protection Tier Comparison](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-sku-comparison)

| Tier | Price | Best For |
|------|-------|----------|
| IP Protection | $199/month per public IP | Fewer than 15 public IPs |
| Network Protection | $2,944/month (up to 100 IPs) + $29.50/additional IP | More than 15 public IPs; includes DRR, cost protection, WAF discounts |

[STATISTIC] Azure DDoS Network Protection is priced at $2,944 per month for up to 100 public IP resources, with $29.50 per additional IP beyond 100.
URL: [Azure DDoS Protection Pricing](https://azure.microsoft.com/en-us/pricing/details/ddos-protection/)

[STATISTIC] Azure DDoS IP Protection is priced at $199 per month per protected public IP address.
URL: [Azure DDoS Protection Pricing](https://azure.microsoft.com/en-us/pricing/details/ddos-protection/)

[FACT] IP Protection is the more cost-effective option for fewer than 15 public IP resources; Network Protection becomes more cost-effective above 15 public IPs.
URL: [Compare pricing between Azure DDoS Protection tiers](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-pricing-guide)

### SLA and Mitigation Capabilities

[FACT] Azure DDoS Protection service is covered by a 99.99% SLA.
URL: [Azure DDoS Protection Overview](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview)

[FACT] All L3/L4 attack vectors can be mitigated by Azure DDoS Protection, with global capacity to protect against the largest known DDoS attacks. Application traffic patterns are monitored 24 hours a day, 7 days a week, looking for indicators of DDoS attacks.
URL: [Azure DDoS Protection features](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-features)

[FACT] Azure DDoS Network Protection includes DDoS Protection Rapid Response (DRR) — access to a dedicated rapid-response team within a 15-minute SLA for attack investigation, custom mitigation, and analysis.
URL: [Azure DDoS Protection features](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-features)

[FACT] Network Protection provides cost protection: if a protected resource scales out during a documented DDoS attack, Azure provides service credits for those scale-out resource costs.
URL: [Azure DDoS Protection features](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-features)

**Operational burden eliminated:** Self-managed DDoS mitigation requires either dedicated scrubbing infrastructure (Arbor, Radware appliances), upstream transit provider mitigation contracts, or manual traffic rerouting during attack events — all requiring 24/7 NOC coverage. Azure DDoS Protection is fully managed, with detection and mitigation firing automatically with no operator intervention required.

### Operational Profile: DDoS Protection

| Dimension | On-Premises | Managed K8s (Cloud, No DDoS Plan) | Cloud-Native (Azure DDoS) |
|---|---|---|---|
| Difficulty | 5/5 | 3/5 | 1/5 |
| Key requirements | Scrubbing appliances, transit agreements, 24/7 NOC | Cloud provider basic protection only; WAF rules | Enable DDoS plan on VNet |
| Representative tools | Arbor TMS, Radware DefensePro, upstream provider | Cloudflare Magic Transit, cloud-native basic | Azure DDoS IP/Network Protection |
| Est. FTE | 0.5–1.0 FTE (NOC on-call burden) | 0.1–0.25 FTE | 0.0–0.05 FTE (review alerts only) |

---

## 8. Azure Confidential Computing: TEE-Based Workload Protection

### Overview

Azure Confidential Computing encrypts data in memory using hardware-based Trusted Execution Environments (TEEs), protecting workloads even from the cloud provider's hypervisor, host management code, and administrators.

[QUOTE] "Azure confidential computing encrypts data in memory in hardware-based trusted execution environments and processes it only after the cloud environment is verified. TEEs are hardware-backed, attested environments that help prevent unauthorized access or modification of applications and data while in use."
— Microsoft Learn
URL: [Azure Confidential Computing Overview](https://learn.microsoft.com/en-us/azure/confidential-computing/overview)

### TEE Hardware Options

[FACT] Azure offers two TEE hardware options for confidential VMs: AMD SEV-SNP (generally available) and Intel Trust Domain Extensions (TDX) (in preview as of 2025).
URL: [Azure Confidential VM options](https://learn.microsoft.com/en-us/azure/confidential-computing/virtual-machine-options)

[FACT] AMD SEV-SNP-based confidential VMs (DCasv5 and ECasv5 series) and Intel TDX-based confidential VMs (DCesv5 and ECesv5 series) both support rehosting of existing workloads without code changes by encrypting the entire VM memory footprint.
URL: [About Azure confidential VMs](https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview)

[FACT] DCesv6-series VMs are powered by Intel 5th Generation Xeon Scalable processors (3.0 GHz all-core turbo) with Intel TDX, denying the hypervisor, other host management code, and administrators access to VM memory and state.
URL: [DCesv6-series sizes — Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dcesv6-series)

### Confidential GPU and AI Workloads

[FACT] Azure offers NCCadsH100v5 confidential VMs with linked CPU and GPU Trusted Execution Environments (TEEs), using NVIDIA H100 GPUs to protect sensitive data during AI and machine learning tasks while the GPU accelerates computations. This VM series was in preview as of early 2025.
URL: [Azure Confidential Computing: Confidential GPUs and AI](https://thomasvanlaere.com/posts/2025/03/azure-confidential-computing-confidential-gpus-and-ai/)

[FACT] Microsoft's 2025 update to Azure Confidential Computing implements a zero-trust framework specifically designed for AI workloads: every AI agent request is verified, every data access is authenticated, and nothing is inherently trusted — even within the same tenant environment.
URL: [Securing Multi-Tenant AI Agents: Microsoft Azure's Confidential Computing Update (2025)](https://markaicode.com/azure-confidential-computing-ai-agents-2025/)

[FACT] 2025 performance optimizations for Azure Confidential Computing reduced the previous 25-30% performance overhead penalty to more manageable levels, making confidential computing practical for production AI workloads.
URL: [Securing Multi-Tenant AI Agents: Microsoft Azure's Confidential Computing Update (2025)](https://markaicode.com/azure-confidential-computing-ai-agents-2025/)

### Attestation

[FACT] Azure Confidential Computing provides remote attestation so workloads can verify the TEE's hardware and software measurements before releasing secrets or handling sensitive data, supporting auditable and policy-driven operations.
URL: [Trusted Execution Environment (TEE) — Azure](https://learn.microsoft.com/en-us/azure/confidential-computing/trusted-execution-environment)

**ISV relevance:** For ISVs handling regulated data (healthcare, financial services) or multi-tenant AI inference, confidential computing provides cryptographic proof that the cloud provider cannot access customer data in memory — a differentiated trust guarantee not achievable with conventional encryption.

### Operational Profile: Confidential Computing

| Dimension | On-Premises | Managed K8s | Cloud-Native (Confidential VMs) |
|---|---|---|---|
| Difficulty | 5/5 | 4/5 | 2/5 |
| Key requirements | Dedicated SGX/SEV-SNP hardware procurement, firmware mgmt, attestation service deployment | TEE-capable node pools, attestation integration, limited K8s support | Select DCasv5/ECasv5 VM SKU, configure attestation policy |
| Representative tools | Intel SGX, AMD SEV hardware; Microsoft Open Enclave SDK | Confidential containers (preview), kata containers | Azure Confidential VMs, Azure Attestation |
| Est. FTE | 1.0–2.0 FTE (specialized security engineer) | 0.5–1.0 FTE | 0.1–0.25 FTE |

---

## Consolidated Operational Difficulty Summary

| Security Domain | On-Premises | Managed K8s | Cloud-Native (Azure) |
|---|---|---|---|
| Identity (Entra ID / IAM) | 4/5 | 4/5 | 2/5 |
| Key / Secrets Management | 5/5 | 3/5 | 1/5 |
| TLS Certificate Management | 4/5 | 3/5 | 1/5 |
| CSPM / Posture Management | 5/5 | 3/5 | 1–2/5 |
| Governance / Compliance Enforcement | 4/5 | 3/5 | 1/5 |
| SIEM / Threat Detection | 5/5 | 4/5 | 2/5 |
| DDoS Protection | 5/5 | 3/5 | 1/5 |
| Confidential Computing / TEE | 5/5 | 4/5 | 2/5 |
| **Composite Security FTE Estimate** | **4.5–10.5 FTE** | **2.4–5.5 FTE** | **0.75–1.75 FTE** |

*FTE estimates reflect a mid-size ISV deployment serving 50 enterprise customers. Composite includes on-call burden prorated across domains.*

---

## Key Takeaways

- **Identity is zero-marginal-cost for M365 shops.** ISVs already in the Microsoft 365 ecosystem receive Entra ID P1 (Conditional Access, hybrid identity, MFA) at no additional cost in E3/Business Premium. This eliminates a $6/user/month line item versus purchasing standalone.

- **Key Vault eliminates the HSM capital expenditure problem.** A self-hosted HSM cluster (Thales Luna, Utimaco) costs $40,000–$150,000 in hardware alone before staffing. Azure Managed HSM delivers FIPS 140-3 Level 3 compliance at ~$3.20/hour per pool, removing procurement, firmware management, and physical security overhead entirely.

- **Foundational CSPM at zero cost removes the "no budget for posture management" excuse.** The free Foundational CSPM tier provides multi-cloud secure scoring and benchmark alignment across Azure, AWS, and GCP with no configuration — a capability that would cost $15,000–$60,000/year in standalone tooling (Prisma Cloud, Wiz) for equivalent coverage.

- **Sentinel pricing scales with log volume, not infrastructure.** Unlike self-hosted SIEM platforms that require capacity planning for peak-event indexing throughput, Sentinel auto-scales to any ingest rate at $4.30–$5.20/GB PAYG, removing the need for SIEM platform engineering and cluster operations entirely.

- **Confidential Computing is the emerging differentiator for regulated AI workloads.** The 2025 GPU-TEE capability (NCCadsH100v5 with linked CPU+GPU TEEs) enables ISVs to offer cryptographically verifiable data isolation for AI inference — a competitive moat for healthcare, financial services, and government verticals that on-premises and standard cloud deployments cannot match without equivalent specialized hardware procurement.

---

## Related — Out of Scope

- **Azure Virtual Network, Private Link, NSGs, Azure Firewall** — covered in F21 (Azure Networking). These form the network perimeter within which the security services above operate.
- **AWS equivalent security services (IAM, Secrets Manager, GuardDuty, Security Hub)** — covered in F11 (AWS Security).
- **GCP equivalent security services (Secret Manager, Security Command Center, Chronicle)** — covered in a parallel wave3 file.
- **Microsoft Purview** (data governance, information protection, compliance center) — adjacent to Azure Policy and Sentinel but focused on data classification, eDiscovery, and insider risk — not covered in this file's scope.

---

## Sources

| # | Source | URL |
|---|--------|-----|
| 1 | Microsoft Entra releases and announcements — Microsoft Learn | https://learn.microsoft.com/en-us/entra/fundamentals/whats-new |
| 2 | What's new in Microsoft Entra — June 2025 | https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-%E2%80%93-june-2025/4352579 |
| 3 | Microsoft Entra Conditional Access: Zero Trust Policy Engine | https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview |
| 4 | What is Privileged Identity Management? | https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure |
| 5 | Plan a Privileged Identity Management deployment | https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan |
| 6 | Implementing PIM: Enhancing Security Through Just-in-Time Access | https://techcommunity.microsoft.com/discussions/microsoft-365/implementing-privileged-identity-management-pim-enhancing-security-through-just-/4430502 |
| 7 | Microsoft Entra Plans and Pricing | https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing |
| 8 | External ID pricing — Microsoft Entra External ID | https://learn.microsoft.com/en-us/entra/external-id/external-identities-pricing |
| 9 | Microsoft Entra External ID overview | https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview |
| 10 | Microsoft to End Sale of Azure AD B2B/B2C on May 1, 2025 | https://envisionit.com/resources/articles/microsoft-to-end-sale-of-azure-ad-b2bb2c-on-may-1-2025-shifting-to-entra-id-external-identities/ |
| 11 | Azure Managed HSM Overview | https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview |
| 12 | About Azure Key Vault certificates | https://learn.microsoft.com/en-us/azure/key-vault/certificates/about-certificates |
| 13 | Azure Key Vault Pricing: Complete Guide | https://infisical.com/blog/azure-key-vault-pricing |
| 14 | Azure Key Vault Tutorial — DataCamp | https://www.datacamp.com/tutorial/azure-key-vault-tutorial |
| 15 | Secure your Azure Key Vault | https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault |
| 16 | App Service Managed Certificate Changes — July 28, 2025 | https://learn.microsoft.com/en-us/azure/app-service/app-service-managed-certificate-changes-july-2025 |
| 17 | Do managed certificates in Azure Front Door Premium have any cost? | https://learn.microsoft.com/en-us/answers/questions/5560015/do-the-managed-certificates-in-azure-front-door-pr |
| 18 | Changes to the Managed TLS Feature | https://docs.azure.cn/en-us/security/fundamentals/managed-tls-changes |
| 19 | What is Cloud Security Posture Management (CSPM) | https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management |
| 20 | Microsoft Defender for Cloud — CSPM and CWPP | https://azure.microsoft.com/en-us/products/defender-for-cloud |
| 21 | Pricing — Microsoft Defender for Cloud | https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/ |
| 22 | Cloud secure score in Microsoft Defender for Cloud | https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls |
| 23 | What's new in Microsoft Defender for Cloud features | https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes |
| 24 | Overview of Azure Policy | https://learn.microsoft.com/en-us/azure/governance/policy/overview |
| 25 | Azure Policy Cloud and Compliance Management | https://azure.microsoft.com/en-us/products/azure-policy |
| 26 | Everything New in Azure Governance @ Build 2025 | https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/everything-new-in-azure-governance--build-2025/4415414 |
| 27 | Plan costs and understand pricing and billing — Microsoft Sentinel | https://learn.microsoft.com/en-us/azure/sentinel/billing |
| 28 | Microsoft Sentinel Pricing in 2025 | https://underdefense.com/industry-pricings/microsoft-sentinel-pricing/ |
| 29 | Automate Threat Response with Playbooks in Microsoft Sentinel | https://learn.microsoft.com/en-us/azure/sentinel/automation/automate-responses-with-playbooks |
| 30 | Automation in Microsoft Sentinel | https://learn.microsoft.com/en-us/azure/sentinel/automation/automation |
| 31 | Azure DDoS Protection Overview | https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview |
| 32 | Azure DDoS Protection features | https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-features |
| 33 | Azure DDoS Protection Pricing | https://azure.microsoft.com/en-us/pricing/details/ddos-protection/ |
| 34 | Compare pricing between Azure DDoS Protection tiers | https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-pricing-guide |
| 35 | About Azure DDoS Protection Tier Comparison | https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-sku-comparison |
| 36 | Azure Confidential Computing Overview | https://learn.microsoft.com/en-us/azure/confidential-computing/overview |
| 37 | Azure Confidential VM options | https://learn.microsoft.com/en-us/azure/confidential-computing/virtual-machine-options |
| 38 | About Azure confidential VMs | https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview |
| 39 | DCesv6-series sizes — Azure Virtual Machines | https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dcesv6-series |
| 40 | Azure Confidential Computing: Confidential GPUs and AI | https://thomasvanlaere.com/posts/2025/03/azure-confidential-computing-confidential-gpus-and-ai/ |
| 41 | Securing Multi-Tenant AI Agents: Microsoft Azure Confidential Computing Update (2025) | https://markaicode.com/azure-confidential-computing-ai-agents-2025/ |
| 42 | Trusted Execution Environment (TEE) — Azure | https://learn.microsoft.com/en-us/azure/confidential-computing/trusted-execution-environment |
| 43 | Expert Explains Conditional Access and Zero Trust Implementation in Microsoft Entra | https://virtualizationreview.com/articles/2025/11/06/expert-explains-conditional-access-and-zero-trust-implementation-in-microsoft-entra.aspx |
| 44 | Microsoft Entra External ID — Pricing | https://www.microsoft.com/en-us/security/pricing/microsoft-entra-external-id |
