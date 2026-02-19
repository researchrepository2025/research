# F11: AWS Security Services
**Research Agent:** F11 | **Topic:** AWS Managed Security Services
**Date:** 2026-02-18 | **Audience:** C-Suite + Technical Leadership

---

## Executive Summary

AWS provides a deeply integrated, managed security stack that eliminates the vast majority of undifferentiated security infrastructure work an ISV would otherwise operate in-house. Across identity (IAM, Cognito, IAM Identity Center), cryptography (KMS, CloudHSM), secrets management (Secrets Manager), certificate lifecycle (ACM), application protection (WAF), and threat detection (GuardDuty, Security Hub), AWS has built services that each absorb one or more full-time engineering roles' worth of operational responsibility. For an ISV building AI-driven SaaS, these services collectively replace a minimum of 3–6 FTE of dedicated security infrastructure staff that would be required in an on-premises deployment, while simultaneously providing capabilities — automatic key rotation, managed TLS renewal, ML-driven threat detection — that are technically impractical for most ISVs to replicate at equivalent quality. Critically, 2025 brought a wave of material enhancements: full IAM policy language in SCPs (September 2025), exportable ACM public certificates (June 2025), GuardDuty Extended Threat Detection for EKS, EC2, and ECS, and a re-architected Security Hub with OCSF support — all signaling that AWS's managed security surface is expanding, not plateauing.

---

## 1. AWS IAM: The Foundation of Cloud Access Control

### 1.1 Core Constructs

AWS Identity and Access Management (IAM) is the zero-cost [FACT] permission control plane for all AWS API access. It operates on three principal constructs:

- **Policies:** JSON documents that define allowed or denied actions. Policy types include identity-based policies, resource-based policies, permissions boundaries, session policies, and service control policies. [Source: [Policies and permissions in AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)]
- **Roles:** Temporary-credential-bearing identities assumed by services, users, or external principals. IAM roles are used for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and EC2 applications. [Source: [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)]
- **Identity Federation:** A federated identity is a user from an enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source, and federated identities assume roles that provide temporary credentials. [Source: [Identity federation in AWS](https://aws.amazon.com/identity/federation/)]

### 1.2 Cross-Account Access

To allow cross-account access, an organization attaches a resource-based policy to the resource to be shared and must also attach an identity-based policy to the identity that acts as the principal in the request. [Source: [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html)]

For ISVs deploying into customer environments, AWS introduced **IAM Temporary Delegation** in 2025, which allows sellers to automate onboarding and deploy required resources directly into a customer's AWS account without needing persistent access or manual permission wrangling. [Source: [Top AWS re:Invent Announcements for Security Teams in 2025](https://www.wiz.io/blog/top-aws-re-invent-announcements-for-security-teams-in-2025)]

### 1.3 Service Control Policies (SCPs) — September 2025 Upgrade

[FACT] On September 19, 2025, AWS Organizations introduced full IAM policy language support for SCPs. SCPs now support conditions, individual resource ARNs, the `NotAction` element with Allow statements, wildcards at the beginning or middle of Action strings, and the `NotResource` element. [Source: [AWS Organizations supports full IAM policy language for SCPs](https://aws.amazon.com/about-aws/whats-new/2025/09/aws-organizations-iam-language-service-control-policies/)]

Previously, SCPs were constrained to a subset of IAM policy syntax, which forced organizations to write verbose, imprecise guardrails. The September 2025 update allows more concise and precise policies to implement sophisticated permissions guardrails across an organization. Existing SCPs require no migration — the enhancement maintains full backward compatibility. [Source: [Unlock new possibilities: AWS Organizations SCP now supports full IAM language](https://aws.amazon.com/blogs/security/unlock-new-possibilities-aws-organizations-service-control-policy-now-supports-full-iam-language/)]

### 1.4 IAM Policy Autopilot (re:Invent 2025)

AWS introduced **IAM Policy Autopilot** at re:Invent 2025. It is an open-source MCP server that analyzes application code and helps AI coding assistants generate AWS IAM identity-based policies. It scans Python, TypeScript, and Go code for S3, Lambda, and DynamoDB calls, outputting valid, functional policies as a baseline. IAM Policy Autopilot continuously reassesses access needs — when teams add features, permissions update automatically; when features disappear, unused permissions are removed. [Source: [AWS launches AI-enhanced security innovations at re:Invent 2025](https://aws.amazon.com/blogs/security/aws-launches-ai-enhanced-security-innovations-at-reinvent-2025/)]

### 1.5 IAM Outbound Identity Federation (2025)

AWS introduced Outbound Identity Federation allowing AWS account administrators to configure the `sts:GetWebIdentityToken` permission in all relevant AWS policy types — including identity policies, SCPs, resource control policies (RCPs), and VPCE policies — to control which IAM principals can generate tokens for external services. [Source: [Simplify access to external services using AWS IAM Outbound Identity Federation](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/)]

### 1.6 Operational Burden Eliminated

| Capability | On-Premises | Managed K8s | Cloud-Native (IAM) |
|---|---|---|---|
| Identity & access management | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-hosted IdP (Keycloak, LDAP) + RBAC | K8s RBAC + external IdP integration | IAM policies + IAM Identity Center |
| | OpenLDAP, Active Directory, Keycloak | Okta/Azure AD OIDC bridge | Native IAM, no server to operate |
| Est. FTE: 1.0–1.5 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |

*Assumptions: Mid-size ISV serving 50 enterprise customers; "FTE" covers policy authoring, auditing, rotation, and incident response. Self-hosted includes server maintenance, patching, HA cluster management.*

---

## 2. Amazon Cognito: Customer Identity and Access Management (CIAM)

### 2.1 Architecture: User Pools vs. Identity Pools

Amazon Cognito is composed of two distinct services that are often deployed together:

- **User Pools:** A user directory with both self-service and administrator-driven user creation, management, and authentication. [Source: [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)]
- **Identity Pools:** Authorize authenticated or anonymous users to access AWS resources and issue AWS credentials for apps to serve resources to users directly. [Source: [What is Amazon Cognito?](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)]

### 2.2 Authentication Capabilities

Cognito supports username/password authentication, social identity providers (Google, Facebook, Amazon, Apple), enterprise federation via SAML 2.0 and OIDC, and passwordless authentication options including passkeys and one-time passwords. [Source: [AWS Cognito Essentials: Everything You Need for Authentication and Identity](https://cloudchipr.com/blog/aws-cognito)]

### 2.3 Managed Login and Hosted UI

Managed login and the classic hosted UI support sign-up, sign-in, and password management, including completing sign-in with MFA and registration of WebAuthn authenticators. Managed login offers additional capabilities not in the classic hosted UI — including passwordless and passkey authentication available only in managed login. [Source: [User pool managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html)]

### 2.4 MFA Options

Users can provide an additional authentication factor with a code from an SMS or email message, or an app that generates MFA codes, and organizations can build mechanisms to set up and process MFA in their application, or let managed login manage it. [Source: [Adding MFA to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)]

### 2.5 Passwordless and Passkeys (2025)

Amazon Cognito launched native passwordless support in November 2024 with general availability expanding through 2025. Passkeys are based on FIDO standards and use public key cryptography, enabling strong, phishing-resistant authentication. Passkey support is an opt-in feature available in all feature plans except for Lite, and is only available in the choice-based authentication flow. [Source: [Amazon Cognito now supports passwordless authentication](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-cognito-passwordless-authentication-low-friction-secure-logins/)]

In March 2025, AWS expanded passwordless support to AWS GovCloud (US) regions. [Source: [Amazon Cognito passwordless authentication in AWS GovCloud](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-cognito-passwordless-authentication-low-friction-secure-logins-aws-govcloud-us-regions/)]

### 2.6 Feature Plans and Pricing

Amazon Cognito introduced three pricing tiers effective December 1, 2024: **Lite**, **Essentials**, and **Plus**. All tiers include social identity providers, SAML/OIDC federation, Lambda triggers, and base features. The Essentials tier adds advanced authentication features including choice-based sign-in and email MFA. [Source: [User pool feature plans](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html)]

[STATISTIC] For SAML/OIDC federated users, pricing above the 50 MAU free tier is $0.015 per MAU. The Lite and Essentials tiers include 10,000 MAUs free for direct or social logins and 50 MAUs free for SAML/OIDC-federated users. [Source: [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing/)]

**ISV Consideration:** Cognito priced on federated MAUs introduces complete unpredictability — the success of customer deployments directly creates financial risk for the platform operator. [Source: [AWS Cognito vs Auth0: Cost, Control, and Caveats](https://securityboulevard.com/2025/09/aws-cognito-vs-auth0-cost-control-and-caveats/)]

| Capability | On-Premises | Managed K8s | Cloud-Native (Cognito) |
|---|---|---|---|
| Customer identity management | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Self-hosted Keycloak/Auth0 alternative | Self-hosted Keycloak on K8s | Fully managed user pools |
| | Keycloak, LDAP, custom federation | Keycloak Helm chart, external IdP | Cognito User/Identity Pools |
| Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 |

---

## 3. AWS KMS: Key Management Service

### 3.1 Core Function

AWS KMS is a managed key management service backed by hardware security modules (HSMs). Each AWS KMS key that you create costs $1 per month (prorated hourly). [Source: [Pricing — AWS Key Management Service](https://aws.amazon.com/kms/pricing/)]

### 3.2 Envelope Encryption

[FACT] AWS services use envelope encryption, where a data key is used to encrypt data, and is itself encrypted under a KMS key stored in AWS KMS. Envelope encryption protects data keys so users can safely store the encrypted data key alongside their encrypted data, and allows re-encrypting only the data keys that protect the raw data — eliminating the need to re-encrypt raw data multiple times with different keys. [Source: [AWS KMS keys — Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)]

### 3.3 Automatic Key Rotation

[FACT] AWS KMS supports automatic rotation of keys in a configurable range from 90 days to 2,560 days (7 years). The `RotateKeyOnDemand` API enables immediate on-demand rotation. If AWS KMS automatically rotates keys, re-encryption of existing data is not required — AWS KMS automatically keeps previous versions of keys to use for decryption of data encrypted under an old version of a key. [Source: [Rotate AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)]

Key rotation is not supported for asymmetric keys, HMAC keys, or keys generated in an AWS CloudHSM cluster using the AWS KMS custom key store feature. [Source: [AWS KMS FAQs](https://aws.amazon.com/kms/faqs/)]

[STATISTIC] Key rotation cost: the first and second rotation of a key each add $1 per month (prorated hourly). Any subsequent rotations beyond the second are not billed. [Source: [Pricing — AWS Key Management Service](https://aws.amazon.com/kms/pricing/)]

### 3.4 API Call Pricing

[STATISTIC] KMS API call pricing per 10,000 requests: symmetric operations (Encrypt, Decrypt, GenerateDataKey) are $0.03; RSA 2048 operations are $0.03; other asymmetric operations (Sign, Verify) are $0.15; ECC GenerateDataKeyPair is $0.10; RSA GenerateDataKeyPair is $12.00. The free tier provides 20,000 requests per month across all regions. [Source: [Pricing — AWS Key Management Service](https://aws.amazon.com/kms/pricing/)]

### 3.5 CloudHSM Custom Key Store Integration

Organizations may create and manage KMS keys in their own AWS CloudHSM cluster. Cryptographic operations under that key are performed in the organization's own AWS CloudHSM cluster. [Source: [AWS KMS FAQs](https://aws.amazon.com/kms/faqs/)]

[FACT] Keys created and protected in the AWS KMS HSMs offer higher performance, lower latency, and a service level agreement for KMS cryptographic operations compared to keys in the custom key store (CloudHSM). [Source: [AWS KMS FAQs](https://aws.amazon.com/kms/faqs/)]

| Capability | On-Premises | Managed K8s | Cloud-Native (KMS) |
|---|---|---|---|
| Cryptographic key management | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | HSM procurement, rack, maintenance | Self-hosted Vault or cloud KMS bridge | Fully managed, API-driven |
| | SafeNet Luna, Thales HSM, HashiCorp Vault | HashiCorp Vault on K8s | AWS KMS ($1/key/month) |
| Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |

---

## 4. AWS Secrets Manager

### 4.1 Core Function and Pricing

AWS Secrets Manager centrally manages the lifecycle of credentials, API keys, and other secrets. [STATISTIC] Storage pricing is $0.40 per secret per month, prorated hourly, across all AWS regions. API requests are charged at $0.05 per 10,000 API calls. [Source: [Pricing — AWS Secrets Manager](https://aws.amazon.com/secrets-manager/pricing/)]

### 4.2 Automatic Rotation

Secrets Manager provides templates for Amazon RDS, Amazon Aurora, Amazon Redshift, and Amazon DocumentDB database secrets in rotation function templates. AWS provides managed rotation functions for RDS, Redshift, and DocumentDB. Amazon RDS managed rotation for master user credentials typically completes within one minute. [Source: [Set up automatic rotation for Amazon RDS secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-db.html)]

[FACT] Secret rotation does not add a per-rotation storage charge. Creating a new version of a secret (the mechanism behind rotation) is not billed separately. Lambda function executions triggered by rotation add approximately $0.000002 per rotation in compute cost. [Source: [Demystifying AWS Secrets Manager Pricing](https://www.oreateai.com/blog/demystifying-aws-secrets-manager-pricing-what-you-pay-for/fdf2f827d3c87e249c9d257512f4a049)]

### 4.3 Rotation Strategies

The alternating users rotation strategy clones the user and then alternates which user's credentials are updated. This strategy provides high availability for the secret, because one of the alternating users has current credentials to the database while the other is being updated. [Source: [Set up alternating users rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_rotation-alternating.html)]

### 4.4 Cross-Account Sharing

Secrets Manager supports cross-account secret sharing through resource-based policies on secrets, enabling multi-tenant ISV architectures where the ISV controls a central secrets plane while granting scoped access to customer accounts. [Source: [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)]

### 4.5 Operational Burden vs. Self-Hosted Alternatives

[STATISTIC] A self-hosted deployment of HashiCorp Vault Enterprise managing 1,000 secrets carries an estimated annual cost of approximately $51,760 — comprising infrastructure (~$1,000), storage (~$120), Vault Enterprise licensing (~$13,140), and 0.25 FTE of staff time (~$37,500). [Source: [Hashicorp Vault Pricing: Complete Guide](https://infisical.com/blog/hashicorp-vault-pricing)]

| Capability | On-Premises | Managed K8s | Cloud-Native (Secrets Manager) |
|---|---|---|---|
| Secrets lifecycle management | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Self-hosted Vault cluster, HA config | Vault on K8s with auto-unseal | Fully managed, automatic rotation |
| | HashiCorp Vault, CyberArk | Vault Helm chart, agent injector | AWS Secrets Manager ($0.40/secret/mo) |
| Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |

---

## 5. AWS Certificate Manager (ACM)

### 5.1 Free Public TLS Certificates

[FACT] Public and private SSL/TLS certificates provisioned through ACM and used exclusively with ACM-integrated services — including Elastic Load Balancing, Amazon CloudFront, and Amazon API Gateway — are free. [Source: [Certificate Manager — AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)]

### 5.2 Automatic Renewal

ACM provides managed renewal for Amazon-issued SSL/TLS certificates. ACM renews certificates automatically for DNS-validated certificates when the CNAME validation record remains in place. For email-validated certificates, ACM sends expiration notices. A certificate is eligible for automatic renewal if it is associated with another AWS service, such as Elastic Load Balancing or CloudFront. [Source: [Managed certificate renewal in AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html)]

Auto-renewal only works if the original validation method remains available. For DNS validation, the validation CNAME records must be kept in DNS configuration permanently. [Source: [AWS Certificate Manager Cheat Sheet](https://tutorialsdojo.com/aws-certificate-manager/)]

### 5.3 ALB Integration

Certificates provided by ACM deployed on an Application Load Balancer can be renewed automatically. ACM attempts to renew certificates before they expire, and renewed certificates are automatically deployed to the associated ALB listener. [Source: [SSL certificates for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html)]

### 5.4 Exportable Public Certificates — June 2025

[FACT] On June 17, 2025, AWS Certificate Manager introduced exportable public certificates, allowing organizations to export public TLS certificates and associated private keys from ACM for use on EC2 instances, EKS pods, on-premises servers, or servers hosted with other cloud providers. [Source: [AWS Certificate Manager introduces public certificates you can use anywhere](https://aws.amazon.com/about-aws/whats-new/2025/06/aws-certificate-manager-public-certificates-use-anywhere/)]

[FACT] ACM public certificates created prior to June 17, 2025 cannot be exported. Exportable public certificates cost $15 per FQDN and $149 per wildcard name, and are valid for 395 days. [Source: [Export an AWS Certificate Manager public certificate](https://docs.aws.amazon.com/acm/latest/userguide/export-public-certificate.html)]

[FACT] As of August 2024, ACM stopped cross-signing public certificates with the legacy Starfield Class 2 root. New certificates chain to Starfield Services G2 to ensure compatibility with modern browsers (Chrome/Mozilla) that will distrust the old root in 2025. [Source: [AWS Certificate Manager now supports exporting public certificates](https://aws.amazon.com/blogs/security/aws-certificate-manager-now-supports-exporting-public-certificates/)]

| Capability | On-Premises | Managed K8s | Cloud-Native (ACM) |
|---|---|---|---|
| TLS certificate lifecycle | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Manual cert-manager, PKI infra, renewals | cert-manager on K8s + Let's Encrypt | Fully managed, zero renewal effort |
| | OpenSSL, Vault PKI, internal CA | cert-manager Helm chart, ACME | ACM (free for integrated services) |
| Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 | Est. FTE: 0.0–0.05 |

---

## 6. AWS WAF: Web Application Firewall

### 6.1 Core Capabilities

AWS WAF protects web applications and APIs against common exploits by inspecting HTTP/HTTPS requests before they reach the origin. It integrates natively with CloudFront, ALB, API Gateway, and AppSync. [Source: [Pricing — AWS WAF](https://aws.amazon.com/waf/pricing/)]

### 6.2 Managed Rule Groups

AWS provides pre-built managed rule groups covering OWASP Top 10 vulnerabilities, known malicious IPs, and common attack patterns, eliminating the need to research and write custom detection rules. Third-party managed rule groups are also available in AWS Marketplace. [Source: [Best practices for intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections-best-practices.html)]

### 6.3 Bot Control

AWS WAF Bot Control allows monitoring, blocking, or rate-limiting of bots including scrapers, scanners, crawlers, status monitors, and search engines. [Source: [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html)]

The Bot Control rule group offers two inspection levels:
- **Common Level:** Detects self-identifying bots using static request data analysis.
- **Targeted Level:** Detects sophisticated bots that do not self-identify, using a combination of rate limiting and CAPTCHA and background browser challenges. [Source: [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html)]

[STATISTIC] The Bot Control managed rule group has a Web Content Unit (WCU) cost of 50. Additional fees apply for this managed rule group beyond baseline WAF pricing. [Source: [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html)]

### 6.4 Rate Limiting

A rate-based rule counts incoming requests and rate-limits them when they arrive too fast a rate, aggregating requests according to configured criteria and counting and rate-limiting the aggregate groupings based on the rule's evaluation window, request limit, and action settings. [Source: [Using rate-based rule statements in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)]

Rate limiting options include both the targeted level of the Bot Control rule group and the AWS WAF rate-based rule statement. [Source: [Options for rate limiting in rate-based rules and targeted Bot Control rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-limiting-options.html)]

### 6.5 Pricing

[STATISTIC] AWS WAF pricing components: $5.00 per Web ACL per month; $1.00 per rule per Web ACL per month; $0.60 per million HTTP requests processed. Managed rule groups add $1.00 per rule group per Web ACL per month plus incremental request charges. [Source: [Pricing — AWS WAF](https://aws.amazon.com/waf/pricing/)]

**ISV Marketplace Note:** ISVs can sell their own custom managed rule groups through AWS Marketplace, setting their own price (e.g., $20.00/month plus $1.20 per million requests). [Source: [Pricing — AWS WAF](https://aws.amazon.com/waf/pricing/)]

| Capability | On-Premises | Managed K8s | Cloud-Native (WAF) |
|---|---|---|---|
| Web application firewall | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-managed ModSecurity, F5, Nginx WAF | Ingress-level WAF (Kong, Nginx) | Managed rules, bot control, rate-limit |
| | ModSecurity, OWASP CRS, F5 BIG-IP | OWASP CRS, Nginx ModSecurity | AWS WAF + managed rule groups |
| Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 |

---

## 7. Amazon GuardDuty: Intelligent Threat Detection

### 7.1 Detection Methodology

GuardDuty uses artificial intelligence (AI), machine learning (ML), anomaly detection, and malicious file discovery, using both AWS and industry-leading threat intelligence to help protect AWS accounts, workloads, and data. It rapidly detects threats using anomaly detection, AI, ML, threat intelligence, and behavioral modeling. [Source: [Intelligent Threat Detection — Amazon GuardDuty](https://aws.amazon.com/guardduty/)]

### 7.2 Data Sources Analyzed

GuardDuty analyzes VPC Flow Logs, DNS logs, CloudTrail management and data events, and (with protection plans enabled) EKS audit logs, ECS runtime telemetry, and EC2 runtime telemetry. Pricing is based on volume of events analyzed, not on findings generated.

[STATISTIC] GuardDuty foundational threat detection pricing for CloudTrail management events: $4.00 per million events per month. EKS audit log analysis is tiered: $1.60/million for the first 100 million events, $0.80/million for the next 100 million, and $0.40/million for over 200 million. [Source: [Intelligent Threat Detection — Amazon GuardDuty Pricing](https://aws.amazon.com/guardduty/pricing/)]

### 7.3 Extended Threat Detection — 2025 Expansions

**EKS Support (June 2025):** [FACT] AWS announced further enhancements to Amazon GuardDuty Extended Threat Detection with coverage for multi-stage attacks targeting Amazon EKS clusters. The new findings build on existing Extended Threat Detection capabilities that already combined sequences involving IAM credential misuse, unusual S3 bucket activity, and EKS cluster compromise. [Source: [Amazon GuardDuty Extended Threat Detection now supports Amazon EKS](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-guardduty-threat-detection-eks/)]

**EC2 and ECS Support (December 2025):** [FACT] AWS announced enhancements to Amazon GuardDuty Extended Threat Detection with new capabilities to detect multistage attacks targeting Amazon EC2 instances and Amazon ECS clusters running on AWS Fargate or Amazon EC2. Two new critical-severity findings were introduced: `AttackSequence:EC2/CompromisedInstanceGroup` and `AttackSequence:ECS/CompromisedCluster`. [Source: [Amazon GuardDuty Extended Threat Detection now supports Amazon EC2 and Amazon ECS](https://aws.amazon.com/about-aws/whats-new/2025/12/guardduty-extended-threat-detection-ec2-ecs/)]

[FACT] Extended Threat Detection analyzes multiple security signals across network activity, process runtime behavior, malware execution, and AWS API activity over extended periods to detect sophisticated attack patterns that might otherwise go unnoticed. [Source: [Amazon GuardDuty adds Extended Threat Detection for Amazon EC2 and Amazon ECS](https://aws.amazon.com/blogs/aws/amazon-guardduty-adds-extended-threat-detection-for-amazon-ec2-and-amazon-ecs/)]

[FACT] Each GuardDuty finding includes a detailed summary, events timeline, mapping to MITRE ATT&CK tactics and techniques, and remediation recommendations. [Source: [Amazon GuardDuty adds Extended Threat Detection for Amazon EC2 and Amazon ECS](https://aws.amazon.com/blogs/aws/amazon-guardduty-adds-extended-threat-detection-for-amazon-ec2-and-amazon-ecs/)]

[FACT] GuardDuty Extended Threat Detection is automatically enabled for GuardDuty customers at no additional cost; its detection comprehensiveness depends on which GuardDuty protection plans are enabled. [Source: [Amazon GuardDuty Extended Threat Detection now supports Amazon EC2 and Amazon ECS](https://aws.amazon.com/about-aws/whats-new/2025/12/guardduty-extended-threat-detection-ec2-ecs/)]

### 7.4 Security Hub Integration

Amazon GuardDuty is available as a standalone threat detection service or integrated with the enhanced AWS Security Hub. When using the enhanced Security Hub, GuardDuty findings are automatically enriched with critical context, allowing organizations to surface critical risks that may only become apparent when analyzed across the entire environment. [Source: [Intelligent Threat Detection — Amazon GuardDuty Features](https://aws.amazon.com/guardduty/features/)]

| Capability | On-Premises | Managed K8s | Cloud-Native (GuardDuty) |
|---|---|---|---|
| Threat detection and behavioral monitoring | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | SIEM + custom rules, log aggregation | Falco, SIEM integration, custom alerts | ML-driven, no rule tuning required |
| | Splunk/ELK + Falco + Snort | Falco on K8s, SIEM pipeline | GuardDuty (pay-per-event analysis) |
| Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 |

---

## 8. AWS Security Hub: Centralized Security Posture Management

### 8.1 Core Function

AWS Security Hub CSPM performs security best practice checks and ingests security findings from AWS security services and partners, combining results from GuardDuty, AWS Config, Amazon Inspector, and Amazon Macie with partner security tool findings to offer automated checks against AWS resources and evaluate security posture. [Source: [Unified Cloud Security Operations Capabilities — AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/)]

### 8.2 Compliance Standards

Security Hub offers security standards aligned to: AWS Foundational Security Best Practices (FSBP), Center for Internet Security (CIS), Payment Card Industry Data Security Standard (PCI DSS), and National Institute of Standards and Technology (NIST). [Source: [AWS Security Hub Best Practices](https://aws.github.io/aws-security-services-best-practices/guides/security-hub/)]

### 8.3 Automated Remediation

Custom automated response, remediation, and enrichment workflows are created using Security Hub CSPM integration with Amazon EventBridge. Findings are automatically sent to EventBridge, enabling EventBridge rules to target AWS Lambda functions, AWS Step Functions, or AWS Systems Manager Automation runbooks. [Source: [Streamline security response at scale with AWS Security Hub automation](https://aws.amazon.com/blogs/security/streamline-security-response-at-scale-with-aws-security-hub-automation/)]

### 8.4 Major 2025 Enhancements

**re:Inforce 2025 Preview / General Availability:** [FACT] At re:Inforce 2025 (June 17, 2025), AWS unveiled an enhanced AWS Security Hub that transforms how organizations prioritize their most critical security issues and respond at scale. The new version uses the Open Cybersecurity Schema Framework (OCSF), a widely adopted open-source schema supported by AWS and partners in the cybersecurity industry. OCSF enables interoperability across multiple security tools and services, both within and outside of the AWS environment. [Source: [AI on Lockdown: AWS Re:Inforce 2025 Delivers Cloud Security Upgrades](https://awsinsider.net/articles/2025/06/24/ai-on-lockdown-aws-re-inforce-2025-delivers-cloud-security-upgrades.aspx)]

[FACT] The enhanced Security Hub delivers near real-time risk analytics and unified security operations by automatically aggregating and correlating findings across GuardDuty, Inspector, Macie, and Security Hub CSPM. [Source: [AWS Security Hub now generally available with near real-time analytics and risk prioritization](https://aws.amazon.com/blogs/aws/aws-security-hub-now-generally-available-with-near-real-time-analytics-and-risk-prioritization/)]

**Partner Ecosystem (OCSF):** [FACT] Partners who have built integrations with the OCSF format for Security Hub include Cribl, CrowdStrike, Databee, DataDog, Dynatrace, Expel, Graylog, Netskope, Securonix, SentinelOne, Splunk (a Cisco company), Sumo Logic, Tines, Upwind Security, Varonis, DTEX, and Zscaler. [Source: [AWS Security Hub now generally available with near real-time analytics and risk prioritization](https://aws.amazon.com/blogs/aws/aws-security-hub-now-generally-available-with-near-real-time-analytics-and-risk-prioritization/)]

**re:Invent 2025:** [FACT] At re:Invent 2025, AWS further strengthened Security Hub alongside GuardDuty improvements. AWS Security Agent was introduced in preview — a frontier agent that proactively secures applications throughout the development lifecycle, conducting automated security reviews tailored to organizational requirements and delivering context-aware penetration testing on demand. [Source: [AWS rolls out Security Agent and strengthens GuardDuty and Security Hub at re:Invent 2025](https://siliconangle.com/2025/12/02/aws-rolls-security-agent-strengthens-guardduty-security-hub-reinvent-2025/)]

| Capability | On-Premises | Managed K8s | Cloud-Native (Security Hub) |
|---|---|---|---|
| Centralized security posture / CSPM | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Manual aggregation, custom SIEM dashboards | Wiz/Prisma Cloud CSPM + K8s | Native CSPM, automated compliance checks |
| | Splunk, ELK, OpenSearch + custom parsers | Aqua Security, Wiz Runtime | Security Hub + EventBridge remediation |
| Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 |

---

## 9. Aggregate Operational Burden Comparison

The following table summarizes estimated staffing requirements across all security domains covered in this report for a mid-size ISV serving approximately 50 enterprise customers, with moderate compliance requirements (SOC 2 Type II, HIPAA or PCI consideration).

*Assumptions: Mid-size ISV; 50 enterprise customers; SOC 2 Type II compliance target; cloud-native figures assume skilled but not deeply specialized engineers.*

| Security Domain | On-Premises Est. FTE | Managed K8s Est. FTE | Cloud-Native Est. FTE |
|---|---|---|---|
| IAM / workforce identity | 1.0–1.5 | 0.5–1.0 | 0.25–0.5 |
| Customer identity (CIAM) | 1.0–2.0 | 0.5–1.0 | 0.1–0.25 |
| Key management (KMS/HSM) | 0.5–1.0 | 0.25–0.5 | 0.05–0.1 |
| Secrets management | 0.25–0.5 | 0.25–0.5 | 0.05–0.1 |
| TLS certificate lifecycle | 0.25–0.5 | 0.1–0.2 | 0.0–0.05 |
| Web application firewall | 0.5–1.0 | 0.25–0.5 | 0.1–0.2 |
| Threat detection / SIEM | 1.0–2.0 | 0.5–1.0 | 0.1–0.25 |
| Security posture / CSPM | 0.5–1.0 | 0.25–0.5 | 0.1–0.2 |
| **Total** | **5.0–9.5 FTE** | **2.6–5.2 FTE** | **0.75–1.65 FTE** |

[UNVERIFIED — Derived Estimate] The FTE ranges above are synthesized from individual service-level estimates in this report, cross-referenced against the self-hosted Vault staffing data point from [Infisical](https://infisical.com/blog/hashicorp-vault-pricing) and the general cloud security operational posture observations from AWS documentation. No single Gartner/Forrester report with equivalent ISV-scale FTE benchmarks was located in 2025 sources.

---

## 10. IAM Identity Center: Workforce Identity Federation

### 10.1 Function

AWS IAM Identity Center is the AWS solution for connecting workforce users to AWS managed applications and AWS resources. It allows connecting an existing identity provider and synchronizing users and groups from an existing directory, or creating and managing users directly in IAM Identity Center. [Source: [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)]

### 10.2 SAML 2.0 and SCIM

AWS IAM Identity Center works with identity providers of choice (e.g., Okta Universal Directory, Azure Active Directory) via SAML 2.0. IAM Identity Center also supports SCIM (System for Cross-domain Identity Management) for automatic provisioning of users and groups from Azure AD or Okta to AWS. [Source: [Identity federation in AWS](https://aws.amazon.com/identity/federation/)]

[FACT] AWS IAM Identity Center only accepts SAML 2.0 for external identity providers; it does not natively accept OIDC for external IdP federation. [Source: [Use the IAM Identity Center with IAM identities for federation](https://repost.aws/knowledge-center/iam-identity-center-federation)]

### 10.3 Attribute-Based Access Control (ABAC)

AWS IAM Identity Center makes it easy to implement ABAC by defining fine-grained permissions based on user attributes defined in the SAML 2.0 IdP. [Source: [Identity federation in AWS](https://aws.amazon.com/identity/federation/)]

---

## Key Takeaways

- **AWS security services collectively eliminate 3–9 FTE** of specialized security infrastructure staffing compared to an equivalent on-premises deployment, with the largest savings in threat detection (GuardDuty vs. self-hosted SIEM), customer identity management (Cognito vs. self-hosted Keycloak), and key management (KMS vs. self-hosted HSM + Vault).

- **2025 was a landmark year for AWS security maturity:** Full IAM policy language in SCPs (September 2025), exportable ACM public certificates for use anywhere (June 2025), GuardDuty Extended Threat Detection expanded to EKS (June), EC2, and ECS (December), and a re-architected Security Hub with OCSF and near-real-time risk analytics (June 2025) all materially close gaps that previously pushed ISVs toward third-party tooling.

- **The services are deeply integrated by design:** GuardDuty findings flow automatically to Security Hub; Security Hub triggers EventBridge for automated remediation via Lambda/Step Functions; KMS encrypts Secrets Manager secrets; ACM certificates deploy automatically to ALB. For an ISV, this integration graph eliminates the glue-code engineering and SLA-bridging that characterizes self-hosted stacks.

- **Cognito pricing unpredictability is a structural ISV risk:** The MAU-based pricing model ($0.015/MAU for federated users above the 50-user free tier) creates direct financial exposure correlated with customer growth — a compounding cost risk for B2B SaaS platforms with large enterprise customer bases. ISV architects should model Cognito MAU growth projections explicitly before committing to it as the long-term CIAM layer.

- **Cloud-native security does not eliminate all security engineering:** Even at cloud-native difficulty ratings of 1–2/5 per domain, aggregate staffing of 0.75–1.65 FTE is still required for policy authoring, IAM governance, GuardDuty tuning, Security Hub rule configuration, and compliance evidence collection. The key shift is from infrastructure operations to security engineering and governance — higher-leverage work that scales with the ISV's product, not with headcount.

---

## Sources

- [Policies and permissions in AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [IAM tutorial: Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)
- [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html)
- [Identity providers and federation into AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
- [Identity federation in AWS](https://aws.amazon.com/identity/federation/)
- [AWS Organizations supports full IAM policy language for SCPs](https://aws.amazon.com/about-aws/whats-new/2025/09/aws-organizations-iam-language-service-control-policies/)
- [Unlock new possibilities: AWS Organizations SCP now supports full IAM language](https://aws.amazon.com/blogs/security/unlock-new-possibilities-aws-organizations-service-control-policy-now-supports-full-iam-language/)
- [Service control policies (SCPs) — AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [Simplify access to external services using AWS IAM Outbound Identity Federation](https://aws.amazon.com/blogs/aws/simplify-access-to-external-services-using-aws-iam-outbound-identity-federation/)
- [AWS launches AI-enhanced security innovations at re:Invent 2025](https://aws.amazon.com/blogs/security/aws-launches-ai-enhanced-security-innovations-at-reinvent-2025/)
- [Top AWS re:Invent Announcements for Security Teams in 2025 — Wiz](https://www.wiz.io/blog/top-aws-re-invent-announcements-for-security-teams-in-2025)
- [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)
- [What is Amazon Cognito?](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
- [User pool managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html)
- [Adding MFA to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)
- [User pool feature plans](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html)
- [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing/)
- [Amazon Cognito now supports passwordless authentication](https://aws.amazon.com/about-aws/whats-new/2024/11/amazon-cognito-passwordless-authentication-low-friction-secure-logins/)
- [Amazon Cognito passwordless authentication in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-cognito-passwordless-authentication-low-friction-secure-logins-aws-govcloud-us-regions/)
- [AWS Cognito Essentials: Everything You Need for Authentication and Identity](https://cloudchipr.com/blog/aws-cognito)
- [AWS Cognito vs Auth0: Cost, Control, and Caveats](https://securityboulevard.com/2025/09/aws-cognito-vs-auth0-cost-control-and-caveats/)
- [AWS KMS keys — Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
- [AWS KMS FAQs](https://aws.amazon.com/kms/faqs/)
- [Rotate AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
- [Pricing — AWS Key Management Service](https://aws.amazon.com/kms/pricing/)
- [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing/)
- [Set up automatic rotation for Amazon RDS secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_turn-on-for-db.html)
- [Set up alternating users rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_rotation-alternating.html)
- [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)
- [Demystifying AWS Secrets Manager Pricing](https://www.oreateai.com/blog/demystifying-aws-secrets-manager-pricing-what-you-pay-for/fdf2f827d3c87e249c9d257512f4a049)
- [Hashicorp Vault Pricing: Complete Guide](https://infisical.com/blog/hashicorp-vault-pricing)
- [Certificate Manager — AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
- [AWS Certificate Manager FAQs](https://aws.amazon.com/certificate-manager/faqs/)
- [Managed certificate renewal in AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html)
- [SSL certificates for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/https-listener-certificates.html)
- [AWS Certificate Manager introduces public certificates you can use anywhere](https://aws.amazon.com/about-aws/whats-new/2025/06/aws-certificate-manager-public-certificates-use-anywhere/)
- [Export an AWS Certificate Manager public certificate](https://docs.aws.amazon.com/acm/latest/userguide/export-public-certificate.html)
- [AWS Certificate Manager now supports exporting public certificates](https://aws.amazon.com/blogs/security/aws-certificate-manager-now-supports-exporting-public-certificates/)
- [AWS Certificate Manager Cheat Sheet — Tutorials Dojo](https://tutorialsdojo.com/aws-certificate-manager/)
- [Pricing — AWS WAF](https://aws.amazon.com/waf/pricing/)
- [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html)
- [AWS WAF Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html)
- [Using rate-based rule statements in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)
- [Options for rate limiting in rate-based rules and targeted Bot Control rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-limiting-options.html)
- [Best practices for intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections-best-practices.html)
- [Intelligent Threat Detection — Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Intelligent Threat Detection — Amazon GuardDuty Features](https://aws.amazon.com/guardduty/features/)
- [Intelligent Threat Detection — Amazon GuardDuty Pricing](https://aws.amazon.com/guardduty/pricing/)
- [Amazon GuardDuty Extended Threat Detection now supports Amazon EKS](https://aws.amazon.com/about-aws/whats-new/2025/06/amazon-guardduty-threat-detection-eks/)
- [Amazon GuardDuty Extended Threat Detection now supports Amazon EC2 and Amazon ECS](https://aws.amazon.com/about-aws/whats-new/2025/12/guardduty-extended-threat-detection-ec2-ecs/)
- [Amazon GuardDuty adds Extended Threat Detection for Amazon EC2 and Amazon ECS](https://aws.amazon.com/blogs/aws/amazon-guardduty-adds-extended-threat-detection-for-amazon-ec2-and-amazon-ecs/)
- [AWS rolls out Security Agent and strengthens GuardDuty and Security Hub at re:Invent 2025](https://siliconangle.com/2025/12/02/aws-rolls-security-agent-strengthens-guardduty-security-hub-reinvent-2025/)
- [Unified Cloud Security Operations Capabilities — AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/)
- [AWS Security Hub Best Practices](https://aws.github.io/aws-security-services-best-practices/guides/security-hub/)
- [Streamline security response at scale with AWS Security Hub automation](https://aws.amazon.com/blogs/security/streamline-security-response-at-scale-with-aws-security-hub-automation/)
- [AI on Lockdown: AWS Re:Inforce 2025 Delivers Cloud Security Upgrades](https://awsinsider.net/articles/2025/06/24/ai-on-lockdown-aws-re-inforce-2025-delivers-cloud-security-upgrades.aspx)
- [AWS Security Hub now generally available with near real-time analytics and risk prioritization](https://aws.amazon.com/blogs/aws/aws-security-hub-now-generally-available-with-near-real-time-analytics-and-risk-prioritization/)
- [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Use the IAM Identity Center with IAM identities for federation](https://repost.aws/knowledge-center/iam-identity-center-federation)
- [Top announcements of AWS re:Invent 2025](https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025/)

---

## Related — Out of Scope

The following topics were encountered during research but are outside the defined scope boundary for this agent:

- **AWS Network Firewall, VPC Security Groups, NACLs:** Network-layer security perimeters. See [F13: AWS Networking] for detailed coverage of networking architecture.
- **AWS Shield Advanced:** DDoS protection layer that integrates with WAF but constitutes a distinct network-layer service.
- **Amazon Detective:** Forensic investigation service that ingests GuardDuty and Security Hub findings for root-cause analysis — distinct from detection covered here.
- **Azure Active Directory Conditional Access, GCP IAM, Okta:** Competitor identity services that could be referenced in a comparative analysis across cloud providers.
- **Compliance Frameworks (SOC 2, HIPAA, PCI DSS):** Security Hub compliance checks surface violations against these frameworks, but the governance frameworks themselves are outside scope.
