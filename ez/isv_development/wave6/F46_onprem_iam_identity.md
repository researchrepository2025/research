# F46 — On-Premises IAM & Identity
**Research File | Wave 6 | ISV Deployment Model Analysis**
*Prepared: February 2026 | Audience: C-Suite and Technical Leadership*

---

## Executive Summary

Implementing identity and access management entirely on-premises for a multi-tenant SaaS application demands a permanent, specialized team operating a layered stack of interconnected systems — directory services, SSO brokers, policy engines, and audit pipelines — none of which benefit from the elastic scaling or managed-patching guarantees of cloud equivalents. The operational surface is broad: Active Directory or OpenLDAP must be clustered and schema-governed; Keycloak or a similar OIDC/SAML broker must be run at high availability; and per-tenant identity isolation requires either realm-per-tenant or an Organizations extension, each carrying distinct scalability ceilings. Policy enforcement through OPA, Cedar, or OpenFGA adds a further self-hosted decision layer with its own latency, distribution, and version-management requirements. Against managed alternatives — AWS Cognito, Azure AD B2C, Google Cloud Identity — the on-premises model eliminates vendor lock-in and satisfies strict data-residency mandates but substitutes approximately 2.5–4.5 FTE of permanent IAM engineering overhead that cloud services absorb invisibly. ISVs considering this path must treat IAM as a product line, not an infrastructure dependency.

---

## 1. Directory Services: Active Directory and LDAP

### 1.1 Deployment Architecture

Active Directory (AD) remains the dominant enterprise directory protocol for on-premises deployments. A production-grade AD deployment for a multi-tenant SaaS scenario requires at minimum two domain controllers (DCs) per site for redundancy, with Forest/Domain functional levels aligned to the highest supported Windows Server version across the estate. [Microsoft's Active Directory documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) specifies that multi-site deployments must configure site-link objects and replication intervals carefully to avoid split-brain scenarios under network partition.

For ISVs preferring open-source stacks, OpenLDAP offers a LDAP v3-compliant alternative that can be deployed in a multi-master or provider-consumer replication topology. [IBM Verify's on-premises provisioning documentation](https://docs.verify.ibm.com/verify/docs/on-premises-provisioning) acknowledges that managing accounts with "fine-grained privileges on Cloud-inaccessible targets and applications such as LDAP, Active Directory" represents a sustained operational concern.

### 1.2 Schema Extensions

Schema extensions allow ISV-specific attributes (e.g., tenant identifiers, license tiers, custom entitlements) to be stored natively within AD. Schema changes are forest-wide, irreversible by default, and replicate via a dedicated Schema Master FSMO role. [JumpCloud's schema extension reference](https://jumpcloud.com/it-index/what-is-an-active-directory-schema-extension) notes that schema extensions persist permanently in the directory and cannot be removed once added — only disabled — creating long-term governance obligations.

**2025 Schema Replication Risk.** A confirmed bug emerged in mid-2025 where running Exchange or custom schema-extension steps while the Schema Master resided on a Windows Server 2025 DC produced duplicate values in multi-valued schema attributes (`auxiliaryClass`, `possSuperiors`, `mayContain`). [Microsoft's TechCommunity disclosure](https://techcommunity.microsoft.com/blog/exchange/active-directory-schema-extension-issue-if-you-use-a-windows-server-2025-schema-/4460459/) confirmed the defect and issued a fix in the November 2025 cumulative update. ISVs managing heterogeneous DC fleets (Server 2016/2019/2022 alongside Server 2025) must validate FSMO placement before any schema work as a change-control gate.

### 1.3 Replication and Multi-Site Operations

[TechTarget's coverage of Windows Server 2025 Active Directory features](https://www.techtarget.com/searchwindowsserver/tip/New-Active-Directory-features-coming-in-Windows-Server-2025) identifies schema replication as following "standard AD replication topology but may take additional time due to the critical nature of schema data." In large, geographically distributed environments, replication delays before all DCs receive schema updates are a documented operational hazard requiring monitoring tooling and replication health checks as standard runbook items.

**Operational Rating: On-Prem Directory = 4/5 difficulty.** Schema governance, FSMO management, replication monitoring, and heterogeneous DC fleet management constitute a continuous, non-trivial operational burden.

---

## 2. SSO and Federation: OIDC/SAML with Keycloak and Dex

### 2.1 Keycloak as the SSO Broker

[Keycloak](https://www.keycloak.org/) is the leading open-source identity broker for on-premises OIDC/SAML deployments. Its core feature set includes:

- **Identity Brokering:** authenticating against external OIDC or SAML identity providers
- **Social Login:** Google, GitHub, and other providers via pluggable connectors
- **User Federation:** synchronization with LDAP and Active Directory servers
- **Protocol translation:** bridging SAML and OIDC so applications can migrate gradually without downtime

[SkyCloak's federation guide](https://skycloak.io/blog/bridging-idp-initiated-saml-to-oidc-with-keycloak/) confirms that "with an identity broker like Keycloak, you can bridge the gap between SAML and OIDC, providing a seamless login experience across diverse applications."

For enterprise deployments, [Keycloak's recommended realm architecture](https://medium.com/@z.viveksingh.26/modern-identity-federation-integrating-oidc-and-saml-with-keycloak-01b11357a1a0) uses four logical realms: Master (administration only), Corporate (employee access), Customer (customer-facing), and Partner (third-party integrations with limited scope). This structure maps directly to the ISV's multi-tenant requirement.

### 2.2 Dex as a Lightweight OIDC Connector

[Dex](https://dexidp.io/) is an OpenID Connect identity provider that acts as an intermediary, deferring authentication upstream to LDAP servers, SAML providers, GitHub, Google, and Active Directory via pluggable "connectors." Because Dex stores state in Kubernetes Custom Resource Definitions (CRDs), it requires no external database, making it lightweight for Kubernetes-native deployments. [Canonical's MicroK8s OIDC/Dex documentation](https://microk8s.io/docs/oidc-dex) and [AWS's EKS integration guide](https://aws.amazon.com/blogs/containers/using-dex-dex-k8s-authenticator-to-authenticate-to-amazon-eks/) demonstrate production integration patterns.

Starting with Kubernetes v1.30, two distinct options exist for connecting Dex to the Kubernetes API server, expanding configuration flexibility for on-premises clusters.

### 2.3 High-Availability Production Requirements for Keycloak

[Keycloak's official HA documentation](https://www.keycloak.org/high-availability/introduction) specifies a minimum of two replicas behind a health-checking load balancer, with pods spread across availability zones. Key operational requirements include:

- Java 17 mandatory for Keycloak 26.x
- All communication must use HTTPS/TLS
- A highly available backend database (PostgreSQL cluster recommended)
- Prometheus-integrated metrics and centralized log aggregation
- Load shedding configured via `http-max-queued-requests` to return 503 under overload rather than cascading failures

[A January 2026 production deployment guide for Keycloak 26.5.0](https://medium.com/@elmeslmaney/keycloak-26-5-0-high-availability-production-deployment-e89495773dfb) documents the full HA cluster configuration including StatefulSets, inter-node latency monitoring, and database HA requirements.

---

## 3. Multi-Tenant Authentication: Tenant Isolation and B2B Federation

### 3.1 Multi-Tenancy Patterns in Keycloak

[Phase Two's multi-tenancy analysis](https://phasetwo.io/blog/multi-tenancy-options-keycloak/) identifies two primary patterns in Keycloak for multi-tenant SaaS:

1. **Realm-per-tenant:** Maximum isolation, but degrades performance at hundreds of realms and creates management overhead, duplication of configuration, and limitations on cross-tenant features.
2. **Single realm with Organizations extension:** More scalable and resource-efficient, enabling true multi-tenancy within one realm.

[Keycloak's June 2024 announcement](https://www.keycloak.org/2024/06/announcement-keycloak-organizations) introduced the Organizations feature as a technology preview targeting CIAM use cases including B2B and B2B2C, "with the ultimate goal to make it supported in Keycloak 26." This feature allows per-tenant identity provider assignment — enabling enterprise customers to bring their own corporate SSO (e.g., Okta, Azure AD, ADFS) for employee login.

### 3.2 Custom Identity Providers Per Tenant (B2B Federation)

[Keycloak's multi-tenant extension documentation](https://github.com/anarsultanov/keycloak-multi-tenancy) and [Phase Two's Organizations extension](https://github.com/p2-inc/keycloak-orgs) both support the "identity broker per organization" pattern. As the [Keycloak B2B federation guide](https://documentation.cloud-iam.com/how-to-guides/multitenant-with-keycloak.html) explains: "In many B2B use-cases the customer have their own identity provider with all their employees. Rather than requiring registering employees in Keycloak they would like to integrate with their existing identity provider. This can be achieved by registering an identity broker with the organization."

This pattern is operationally intensive: each new enterprise tenant requires onboarding their IdP (SAML metadata exchange or OIDC client credentials), testing federation flows, and configuring attribute mapping for role assignment.

**Operational Rating: On-Prem Multi-Tenant Auth = 4/5 difficulty.** The Organizations feature is still maturing; realm-per-tenant at scale is a known anti-pattern.

---

## 4. RBAC Implementation: Role Hierarchies, Policy Engines, and Distribution

### 4.1 Policy Engine Options

Three major open-source policy engines are relevant to on-premises ISV deployments:

| Engine | Model | Language | On-Prem Support | 2025 Status |
|--------|-------|----------|-----------------|-------------|
| OPA | General-purpose | Rego | Native | Uncertain — Apple hired OPA maintainers in August 2025 with plans to sunset enterprise offerings ([osohq.com](https://www.osohq.com/learn/opa-vs-cedar-vs-zanzibar)) |
| Cedar | Application-level RBAC/ABAC | Cedar DSL | Native (open source SDK) | Active; AWS-backed |
| OpenFGA | Relationship-based (Zanzibar) | DSL | Native; PostgreSQL storage | Active; CNCF sandbox |

[AWS Prescriptive Guidance on multi-tenant SaaS authorization](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/introduction.html) specifies that for on-premises deployments, "you can build your PDP yourself by using an open source engine such as Cedar or OPA, which would allow for local, on-premises deployment."

[Permit.io's 2025 policy engine comparison](https://www.permit.io/blog/policy-engines) documents Cedar as "designed to allow defining fine-grained, role-based access control (RBAC) and attribute-based access control (ABAC) policies in a safe, fast, and auditable way" and specifically tailored for application-level authorization.

### 4.2 OpenFGA for Fine-Grained Multi-Tenant RBAC

[OpenFGA](https://openfga.dev/) implements the Google Zanzibar relationship-based access control model and is the CNCF-hosted option. It supports on-premises deployment with pluggable storage adapters including PostgreSQL. [OpenFGA's September 2025 release notes](https://openfga.dev/blog/fine-grained-news-2025-09) report the `/check` endpoint is "up to 10x faster in some scenarios" and `/list-objects` "up to 5x faster" — significant improvements for latency-sensitive authorization paths.

[OpenFGA's deployment positioning](https://openfga.dev/) explicitly states it "enables customers that require deploying in different cloud providers, on-premise, in multiple regions, with FedRAMP compliance, or those that have a low tolerance to the risk of delegating authorization to a third party provider."

### 4.3 Policy Distribution in On-Premises Environments

On-premises policy distribution lacks the managed propagation infrastructure of cloud IAM. OPA bundles must be served via a self-hosted bundle server; Cedar policy stores require custom distribution pipelines; OpenFGA requires direct database writes. Policy version management, rollback, and blue/green deployments are entirely ISV-owned responsibilities.

**Operational Rating: On-Prem RBAC/Policy Engine = 3/5 difficulty.** Policy engines themselves are well-documented; the operational gap is distribution, versioning, and monitoring — all of which must be built from scratch.

---

## 5. Service-to-Service Authentication: mTLS, JWT, and SPIFFE/SPIRE

### 5.1 mTLS via Istio

[Istio's security documentation](https://istio.io/latest/docs/concepts/security/) describes how "Istio securely provisions strong identities to every workload with X.509 certificates, with Istio agents running alongside each Envoy proxy working together with istiod to automate key and certificate rotation at scale." For on-premises Kubernetes clusters, Istio provides automatic mTLS between services without requiring application-level code changes.

### 5.2 JWT Validation for Service Accounts

[Microsoft's May 2025 guide on Kubernetes Structured Authentication](https://opensource.microsoft.com/blog/2025/05/08/jwt-it-like-its-hot-a-practical-guide-for-kubernetes-structured-authentication) documents how "starting with Kubernetes 1.21, the API server can act as an OIDC provider, allowing services to validate ServiceAccount tokens directly without requiring Kubernetes API calls or special permissions." ServiceAccount tokens include standard JWT claims (issuer, subject, audience, expiration) validatable via OIDC discovery and JWKS from the API server.

[A November 2025 guide on Kubernetes ServiceAccount token authentication](https://blog.vitalvas.com/post/2025/11/01/using-kubernetes-serviceaccount-token-for-auth-between-microservices/) provides implementation detail for microservice-to-microservice authentication using projected tokens.

### 5.3 SPIFFE/SPIRE for Workload Identity

[SPIFFE and SPIRE](https://spiffe.io/) provide "a single, standardized way to express service identity across practically any environment — on-premises, multi-cloud, container-based, VM-based, or otherwise." The SPIFFE Verifiable Identity Document (SVID) is a short-lived X.509 certificate or JWT issued by the SPIRE Server to workloads, automatically rotated.

[Red Hat's SPIFFE/SPIRE overview](https://www.redhat.com/en/topics/security/spiffe-and-spire) confirms that "a SPIFFE and SPIRE implementation can add integrated security management to a service mesh, allowing service meshes to rely on cryptographically verifiable identities." [Solo.io's analysis](https://www.solo.io/blog/spire-attestable-workload-identity) notes that SPIRE provides "flexible attestation options not available with the default Istio identity management."

**Operational Rating: On-Prem Service-to-Service Auth = 3/5 difficulty.** Istio + SPIRE is a mature combination but requires dedicated expertise for certificate lifecycle management and attestation configuration.

---

## 6. Token Management: Issuance, Rotation, Revocation, and Session Management

### 6.1 JWT Lifecycle Best Practices

[SkyCloak's JWT lifecycle guide](https://skycloak.io/blog/jwt-token-lifecycle-management-expiration-refresh-revocation-strategies/) establishes the production standard: access tokens with a lifespan of 15–60 minutes, refresh tokens of 30–90 days with rotation built in. [Descope's refresh token rotation guide](https://www.descope.com/blog/post/refresh-token-rotation) defines refresh token rotation as "the process where a new refresh token is issued with each access token refresh request, with the old refresh token being rendered void immediately."

The recommended on-premises architecture uses a **hybrid stateless/stateful model**: short-lived access tokens (no database lookup for API calls) plus stateful refresh tokens stored server-side in a database or Redis, enabling revocation and session inspection. [Avatier's enterprise JWT best practices](https://www.avatier.com/blog/jwt-best-practices/) emphasizes the need to "design access + refresh flows that are safe: short-lived access tokens, rotating refresh tokens with reuse detection, device-scoped sessions, and practical revocation strategies."

### 6.2 Revocation Challenges

[MojoAuth's JWT revocation analysis](https://mojoauth.com/ciam-qna/how-to-revoke-jwt-tokens-before-they-expire) documents the core challenge: "JWT revocation presents unique challenges due to the stateless nature of these tokens" and identifies revocation lists or short-lived tokens validated frequently by authorization servers as the primary mitigations. On-premises deployments must self-host the revocation list infrastructure — typically a Redis cluster or database table — and ensure all API gateways and services query it consistently.

**Operational Rating: On-Prem Token Management = 3/5 difficulty.** Redis/PostgreSQL infrastructure for refresh token storage adds operational dependencies; revocation list consistency across distributed services requires disciplined API gateway configuration.

---

## 7. Audit and Compliance: Logging, Access Auditing, and SOC2/HIPAA

### 7.1 SOC 2 and HIPAA Requirements for IAM

[Secureframe's SOC2 + HIPAA guide](https://secureframe.com/hub/hipaa/and-soc-2-compliance) confirms that "SOC 2 does not specifically cover HIPAA, but a SOC 2 report can be tailored to include controls relevant to HIPAA compliance, particularly in the areas of security and privacy," often delivered as a combined SOC 2+ report. [Vanta's compliance resource](https://www.vanta.com/resources/tackle-both-hipaa-and-soc-2-compliance-with-ongoing-security-monitoring) specifies that SOC 2 expects proof of least-privilege enforcement, encryption, monitoring, logging, change control, and incident response.

**2025 HIPAA Evolution.** [IntuitionLabs' HIPAA/SOC2 guide](https://intuitionlabs.ai/articles/hipaa-soc-2-vs-hitrust-guide) notes that "OCR's proposed 2025 rulemaking suggests that HIPAA will soon incorporate a 'zero trust' mindset: every safeguard will be required rather than optional, pushing companies to adopt a least-privilege approach by default." This elevates on-premises IAM audit requirements toward continuous, automated evidence collection rather than periodic manual review.

### 7.2 Audit Logging Architecture

For on-premises environments, authentication and authorization events must be captured from:

- **Directory services:** AD Security Event Log (Event IDs 4624, 4625, 4720–4740 series) forwarded via Windows Event Forwarding or a SIEM agent
- **Keycloak:** Admin REST API audit events and user event streams, exportable via SPI to external log systems
- **Policy engines:** OPA decision logs, OpenFGA audit trails
- **Service mesh:** Istio Envoy access logs for mTLS session records

[CloudNuro's 2025 PAM tools review](https://www.cloudnuro.ai/blog/top-10-privileged-access-management-pam-tools-for-secure-it-environments-in-2025) notes that PAM tools "ensure full auditability and compliance through monitoring and recording all privileged sessions," and that "aggregating findings into a central security account makes audits smoother and satisfies SOC2 CC7 and HIPAA audit requirements."

All log pipelines, retention policies, tamper-proofing (write-once storage), and compliance reporting dashboards are ISV-owned in the on-premises model — there is no managed equivalent of AWS CloudTrail or Azure Monitor.

**Operational Rating: On-Prem Audit/Compliance = 4/5 difficulty.** Every layer of the IAM stack produces separate log streams; correlation and compliance reporting require either a self-hosted SIEM (Elastic, Splunk) or manual aggregation pipelines.

---

## 8. Comparison: On-Premises vs. Managed Cloud IAM Services

### 8.1 Managed Service Capabilities

[Moldstud's AWS Cognito comparison](https://moldstud.com/articles/p-the-future-of-authentication-comparing-aws-cognito-with-leading-services) summarizes the three primary managed alternatives:

- **AWS Cognito:** User pools, SAML 2.0 federation, MFA, user directory management; best fit for AWS-native stacks
- **Azure AD B2C:** Identity governance, risk-based conditional access, ML-based risk scoring, strong Microsoft 365 integration
- **Google Firebase Auth:** Up to 100K monthly active users free; rapid mobile/web setup with fully managed UI components; less enterprise-depth

[Descope's Cognito alternatives analysis](https://www.descope.com/blog/post/cognito-alternatives) notes that Firebase "handles up to 100K monthly active users freely" and "processes social sign-ins, email/password flows, and anonymous logins with minimal setup."

### 8.2 What Disappears with Managed IAM

The table below documents operational responsibilities that cloud-managed IAM services absorb entirely:

| Responsibility | On-Premises Burden | Managed Cloud Equivalent |
|---|---|---|
| Directory server patching | ISV-owned, scheduled maintenance windows | Fully managed by provider |
| SSO broker HA/clustering | Self-configured (Keycloak clusters, load balancers) | Managed HA, 99.9%+ SLA |
| Certificate rotation (mTLS) | Manual or automated via SPIRE; ISV-owned PKI | Automatic via cloud-native ACM/Key Vault |
| Token revocation infrastructure | Self-hosted Redis/DB cluster | Built into Cognito/Azure AD session management |
| Audit log aggregation | Self-built SIEM pipelines | Native CloudTrail, Azure Monitor, Cloud Audit Logs |
| Schema/policy version management | Manual change control processes | Version-controlled via provider APIs |
| Compliance reporting | Custom dashboards / manual evidence | Pre-built compliance dashboards (SOC2, HIPAA) |
| Vulnerability patching | ISV-owned (Keycloak CVEs, OpenLDAP CVEs) | Provider-owned |

[CloudComputing.co's IAM TCO analysis](https://cloudcomputing.co/en/insights/total-cost-of-ownership-considerations-for-on-premises-versus-cloud-iam-solutions/) states that "indirect costs related to personnel, integration, and customization can exceed the initial licensing costs by up to 2.5 times over a three-year period" for enterprise security software.

[Ubisecure's deployment comparison](https://www.ubisecure.com/identity-platform/deploy-iam-cloud-vs-on-premises/) and [Prolifics' cloud vs on-premises IAM guide](https://prolifics.com/usa/resource-center/blog/cloud-vs-on-premises-iam-8-cs-of-identity-and-access-management) both cite a "Gartner 2025 IAM market insight" noting: "The challenge is not avoiding hybrid, but mastering it" — confirming that the industry default position is now cloud-first or hybrid, with pure on-premises reserved for regulatory mandates. [UNVERIFIED: The specific Gartner 2025 quote could not be directly attributed to a primary Gartner report via the sources found; it is cited in secondary sources consistently but the original report requires Gartner subscription access.]

---

## 9. Consolidated Comparison Table

| Capability | On-Premises | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native |
|---|---|---|---|
| **Directory Services** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-managed AD/OpenLDAP clusters, schema governance, multi-site replication | AD on VMs or LDAP in containers; cloud LDAP available (AWS Directory Service) | Azure AD / AWS Directory Service / Google Cloud Identity fully managed |
| | AD DS, OpenLDAP, Samba 4 | AWS Directory Service, LDAP containers | Azure AD, AWS Managed AD, Google Cloud Identity |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **SSO/Federation** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Keycloak HA cluster, Dex; own certificate management; manual IdP onboarding | Keycloak on K8s with Operator; shared control-plane responsibility | AWS Cognito, Azure AD B2C, Firebase Auth; IdP integration via console |
| | Keycloak 26.x, Dex, OIDC/SAML libraries | Keycloak Operator, Helm charts | Cognito, Azure B2C, Firebase |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.15 |
| **Multi-Tenant Auth** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Realm-per-tenant or Organizations extension; custom IdP per tenant; manual onboarding flows | Same patterns on K8s; partial automation via GitOps | Cognito User Pools per tenant; Azure AD B2C tenant isolation; AWS AVP for authz |
| | Keycloak Organizations, keycloak-multi-tenancy, keycloak-orgs | Keycloak Operator, FluxCD/ArgoCD | AWS Cognito + AVP, Azure AD B2C, Auth0 |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **RBAC/Policy Engine** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-hosted OPA/Cedar/OpenFGA; own bundle server; manual policy distribution | Same engines on K8s; admission webhooks; Kyverno option | AWS AVP (Cedar), Azure RBAC, OPA on cloud K8s; partial SaaS authz options |
| | OPA, Cedar SDK, OpenFGA + PostgreSQL | OPA, Kyverno, OpenFGA | AWS Verified Permissions, OPA on GKE/AKS |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Service-to-Service Auth** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Istio mTLS + SPIRE for workload identity; self-hosted PKI; manual attestation configuration | Istio/Linkerd mTLS; cloud-integrated SPIRE; managed cert issuance available | Cloud-native mTLS via ACM/Key Vault; service accounts with automatic rotation |
| | Istio, SPIRE, cert-manager, Vault | Istio Operator, AWS ACM PCA, SPIRE | AWS ACM, Azure Managed Identity, GCP Workload Identity |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.1 |
| **Token Management** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-hosted Redis for refresh token store; own revocation list; custom rotation logic | Redis on K8s; shared cluster management; same revocation patterns | Managed token issuance and rotation; built-in session management; provider-managed revocation |
| | Redis Cluster, PostgreSQL, Keycloak session store | Redis Operator, managed RDS | Cognito session management, Azure AD token cache |
| | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 | Est. FTE: 0.0 |
| **Audit/Compliance** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Multi-source log aggregation (AD, Keycloak, OPA, Istio); self-hosted SIEM; manual compliance reporting | Centralized logging via K8s; same source diversity; partial cloud logging integration | Native audit trails (CloudTrail, Azure Monitor); pre-built compliance dashboards; automated evidence |
| | Elastic SIEM, Splunk, Graylog; custom pipelines | ELK Stack on K8s, Fluentd, cloud SIEM integration | AWS CloudTrail, Azure Monitor, Google Cloud Audit Logs |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |

### FTE Summary

**Assumptions:**
- Mid-sized ISV: 10–50 enterprise tenants, 10,000–100,000 end users
- On-call burden: add 0.25 FTE for pager rotation on IAM stack (separate from day-time FTE)
- Figures represent sustainable steady-state operations, not initial implementation sprints (which may require 2–3x for the first 6 months)

| Model | IAM Engineering FTE (Steady State) | On-Call Burden | Total IAM Headcount |
|---|---|---|---|
| On-Premises | 2.5–4.5 FTE | +0.25 FTE | **2.75–4.75 FTE** |
| Managed Kubernetes | 1.5–2.5 FTE | +0.15 FTE | **1.65–2.65 FTE** |
| Cloud-Native | 0.25–0.75 FTE | +0.05 FTE | **0.30–0.80 FTE** |

[UNVERIFIED: The specific FTE ranges above are derived from aggregating the per-capability estimates in the comparison table and cross-referencing against Identity Management Institute's general guidance ([identitymanagementinstitute.org](https://identitymanagementinstitute.org/building-a-robust-iam-team/)) that IAM teams are "as unique as the organizations and specific projects they're created for." No single published benchmark provides ISV-specific IAM FTE targets at this granularity; the ranges represent analyst synthesis from operational pattern descriptions across multiple sources.]

---

## Key Takeaways

- **On-premises IAM is a product line, not an infrastructure dependency.** The full stack — directory, SSO broker, policy engine, token store, audit pipeline — requires dedicated 2.75–4.75 FTE in steady state, exclusive of initial build. ISVs must staff and budget accordingly before committing to this model.

- **Keycloak Organizations (introduced as technology preview in Keycloak 26) is the viable on-premises path for per-tenant identity provider federation**, but it is still maturing; the realm-per-tenant alternative degrades operationally at hundreds of tenants and should be avoided for fast-growing SaaS.

- **The 2025 OPA uncertainty is a material risk.** Apple's acquisition of the OPA maintainer team with reported plans to sunset enterprise offerings ([osohq.com](https://www.osohq.com/learn/opa-vs-cedar-vs-zanzibar)) means ISVs standardizing on OPA for on-premises policy enforcement should evaluate Cedar or OpenFGA as strategic alternatives now rather than after a disruption.

- **Cloud-native IAM eliminates the entire operational stack** — patching, HA clustering, certificate rotation, audit aggregation, and compliance reporting — at the cost of vendor dependency and potential data-residency constraints. The TCO difference is substantial: cloud IAM indirect costs are absorbed by the provider; on-premises equivalents can exceed initial licensing costs by 2.5x over three years ([cloudcomputing.co](https://cloudcomputing.co/en/insights/total-cost-of-ownership-considerations-for-on-premises-versus-cloud-iam-solutions/)).

- **For ISVs with hard data-residency or air-gap mandates**, the on-premises IAM stack is viable but requires treating SPIFFE/SPIRE for workload identity, Istio for mTLS, OpenFGA for fine-grained authorization, and Keycloak for SSO as a co-owned, continuously maintained platform. Each component has a separate CVE and patch cadence; the combined maintenance burden is the primary hidden cost.

---

## Sources

1. [Microsoft Learn — LDAP authentication with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/architecture/auth-ldap)
2. [IBM Verify — On-Premises Provisioning](https://docs.verify.ibm.com/verify/docs/on-premises-provisioning)
3. [JumpCloud — What is an Active Directory Schema Extension?](https://jumpcloud.com/it-index/what-is-an-active-directory-schema-extension)
4. [Microsoft TechCommunity — Active Directory schema extension issue with Windows Server 2025 Schema Master](https://techcommunity.microsoft.com/blog/exchange/active-directory-schema-extension-issue-if-you-use-a-windows-server-2025-schema-/4460459/)
5. [TechTarget — New Active Directory features in Windows Server 2025](https://www.techtarget.com/searchwindowsserver/tip/New-Active-Directory-features-coming-in-Windows-Server-2025)
6. [Keycloak — Server Administration Guide](https://www.keycloak.org/docs/latest/server_admin/index.html)
7. [Keycloak — High Availability Overview](https://www.keycloak.org/high-availability/introduction)
8. [Keycloak — Configuring for Production](https://www.keycloak.org/server/configuration-production)
9. [SkyCloak — Bridging IdP-Initiated SAML to OIDC with Keycloak](https://skycloak.io/blog/bridging-idp-initiated-saml-to-oidc-with-keycloak/)
10. [Medium / Elmeslmaney — Keycloak 26.5.0 High-Availability Production Deployment (January 2026)](https://medium.com/@elmeslmaney/keycloak-26-5-0-high-availability-production-deployment-e89495773dfb)
11. [Medium / Vivek Kumar — Modern Identity Federation: Integrating OIDC and SAML with Keycloak](https://medium.com/@z.viveksingh.26/modern-identity-federation-integrating-oidc-and-saml-with-keycloak-01b11357a1a0)
12. [Dex Identity Provider — Official Site](https://dexidp.io/)
13. [Canonical — Configure OIDC with Dex for MicroK8s](https://microk8s.io/docs/oidc-dex)
14. [AWS Containers Blog — Using Dex with EKS](https://aws.amazon.com/blogs/containers/using-dex-dex-k8s-authenticator-to-authenticate-to-amazon-eks/)
15. [Keycloak — Organizations Feature Announcement](https://www.keycloak.org/2024/06/announcement-keycloak-organizations)
16. [Phase Two — Multi-Tenancy Options in Keycloak](https://phasetwo.io/blog/multi-tenancy-options-keycloak/)
17. [GitHub — keycloak-multi-tenancy extension](https://github.com/anarsultanov/keycloak-multi-tenancy)
18. [GitHub — keycloak-orgs (Phase Two)](https://github.com/p2-inc/keycloak-orgs)
19. [Cloud-IAM — Handle Multitenant Organization on Keycloak](https://documentation.cloud-iam.com/how-to-guides/multitenant-with-keycloak.html)
20. [AWS Prescriptive Guidance — Multi-tenant SaaS Authorization](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/introduction.html)
21. [osohq — OPA vs Cedar vs Zanzibar: 2025 Policy Engine Guide](https://www.osohq.com/learn/opa-vs-cedar-vs-zanzibar)
22. [Permit.io — Policy Engine Showdown: OPA vs. OpenFGA vs. Cedar](https://www.permit.io/blog/policy-engine-showdown-opa-vs-openfga-vs-cedar)
23. [OpenFGA — Official Site](https://openfga.dev/)
24. [OpenFGA — Fine Grained News: September 2025](https://openfga.dev/blog/fine-grained-news-2025-09)
25. [Istio — Security Concepts](https://istio.io/latest/docs/concepts/security/)
26. [Microsoft Open Source Blog — JWT Kubernetes Structured Authentication (May 2025)](https://opensource.microsoft.com/blog/2025/05/08/jwt-it-like-its-hot-a-practical-guide-for-kubernetes-structured-authentication)
27. [blog.vitalvas.com — Kubernetes ServiceAccount Token for Auth Between Microservices (November 2025)](https://blog.vitalvas.com/post/2025/11/01/using-kubernetes-serviceaccount-token-for-auth-between-microservices/)
28. [SPIFFE — Official Site](https://spiffe.io/)
29. [Red Hat — What are SPIFFE and SPIRE?](https://www.redhat.com/en/topics/security/spiffe-and-spire)
30. [Solo.io — SPIRE: A case for attestable workload identity](https://www.solo.io/blog/spire-attestable-workload-identity)
31. [SkyCloak — JWT Token Lifecycle Management](https://skycloak.io/blog/jwt-token-lifecycle-management-expiration-refresh-revocation-strategies/)
32. [Descope — The Developer's Guide to Refresh Token Rotation](https://www.descope.com/blog/post/refresh-token-rotation)
33. [Avatier — Secure Token Management for Modern Enterprise Security](https://www.avatier.com/blog/jwt-best-practices/)
34. [MojoAuth — How to revoke JWT tokens before they expire](https://mojoauth.com/ciam-qna/how-to-revoke-jwt-tokens-before-they-expire)
35. [Secureframe — SOC 2 + HIPAA Compliance](https://secureframe.com/hub/hipaa/and-soc-2-compliance)
36. [Vanta — SOC 2 and HIPAA compliance: Overlaps and differences](https://www.vanta.com/resources/tackle-both-hipaa-and-soc-2-compliance-with-ongoing-security-monitoring)
37. [IntuitionLabs — HIPAA for Startups: SOC 2 vs HITRUST Compliance Guide](https://intuitionlabs.ai/articles/hipaa-soc-2-vs-hitrust-guide)
38. [CloudNuro — Top 10 PAM Tools for Secure IT Environments in 2025](https://www.cloudnuro.ai/blog/top-10-privileged-access-management-pam-tools-for-secure-it-environments-in-2025)
39. [Moldstud — The Future of Authentication: Comparing AWS Cognito with Leading Services](https://moldstud.com/articles/p-the-future-of-authentication-comparing-aws-cognito-with-leading-services)
40. [Descope — Top 5 Amazon Cognito Alternatives](https://www.descope.com/blog/post/cognito-alternatives)
41. [CloudComputing.co — TCO Considerations for On-Premises Versus Cloud IAM Solutions](https://cloudcomputing.co/en/insights/total-cost-of-ownership-considerations-for-on-premises-versus-cloud-iam-solutions/)
42. [Ubisecure — How to deploy your IAM system: Cloud vs. On-premises](https://www.ubisecure.com/identity-platform/deploy-iam-cloud-vs-on-premises/)
43. [Prolifics — Cloud vs. On-Premises IAM: Which Model Fits Your Enterprise?](https://prolifics.com/usa/resource-center/blog/cloud-vs-on-premises-iam-8-cs-of-identity-and-access-management)
44. [Identity Management Institute — Building a Robust IAM Team](https://identitymanagementinstitute.org/building-a-robust-iam-team/)
45. [WorkOS — Top RBAC providers for multi-tenant SaaS in 2025](https://workos.com/blog/top-rbac-providers-for-multi-tenant-saas-2025)
