# F47 — On-Premises Secrets, Certificates & Encryption

**Research File | ISV Deployment Model Analysis | Wave 6**
*Scope: Secrets management, TLS certificates, encryption at rest/in transit, key management, HSMs, certificate lifecycle*

---

## Executive Summary

Self-managing secrets, certificates, and encryption in an on-premises environment demands a dedicated operational discipline that cloud-native alternatives largely eliminate. A production-grade HashiCorp Vault deployment with integrated Raft storage requires a minimum three-to-five node cluster with carefully managed unsealing, policy governance, and dynamic secrets pipelines — work that cloud secret managers absorb through managed control planes. Certificate lifecycle management is similarly labor-intensive: internal CA hierarchies, cert-manager automation, and CRL/OCSP revocation infrastructure must all be owned, monitored, and patched by the ISV's engineering team. The encryption surface area in an on-premises environment spans LUKS disk encryption, database-level Transparent Data Encryption (TDE), application-level encryption, and mutual TLS (mTLS) between microservices — each requiring its own key hierarchy and rotation discipline. Hardware Security Modules (HSMs) provide the strongest cryptographic assurance but add procurement complexity, capital expenditure of $5,000–$50,000 per unit, and an impending FIPS 140-2 to FIPS 140-3 migration deadline of September 2026. The aggregate operational burden across all five domains covered in this file represents the single largest infrastructure engineering commitment that differentiates on-premises deployment from cloud-native or Managed Kubernetes alternatives.

---

## 1. Secrets Management: HashiCorp Vault

### 1.1 Storage Backend and High Availability

HashiCorp Vault is the de facto open-source standard for on-premises secrets management. The recommended production storage backend is the [Integrated Storage (Raft) backend](https://developer.hashicorp.com/vault/docs/internals/integrated-storage), which eliminates dependency on external systems like Consul by keeping all configuration and data within the Vault cluster itself, with data replication across nodes via the Raft Consensus Algorithm.

The [reference architecture for a production Vault cluster](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-reference-architecture) recommends five nodes distributed across three availability zones — a configuration that can tolerate the loss of two nodes while maintaining quorum. For Raft consensus, quorum requires at least `ceil((N + 1) / 2)` members: a five-node cluster requires three nodes to remain operational. Deployment across only two availability zones creates a 50% probability of quorum loss if one zone fails.

[High Availability in Vault](https://developer.hashicorp.com/vault/docs/internals/high-availability) operates on an active/standby model: only one Vault instance is active at any time, with standby instances redirecting all requests to the active leader.

### 1.2 Unsealing

Every Vault restart requires an unseal operation before the cluster can serve requests. Vault supports two unsealing modes:

- **Shamir's Secret Sharing (manual):** The master key is split into shares; a quorum of key holders must present shares at restart. This creates an operational dependency on human key holders and is impractical for automated infrastructure.
- **Auto-Unseal:** Vault delegates the unseal key storage to a trusted external KMS. [Supported auto-unseal providers](https://developer.hashicorp.com/vault/docs/concepts/seal) include AWS KMS, Azure Key Vault, GCP Cloud KMS, and the Vault Transit secrets engine (for air-gapped on-premises deployments).

For on-premises environments that cannot use cloud KMS, [Transit auto-unseal](https://developer.hashicorp.com/vault/docs/configuration/seal/transit-best-practices) uses a second "transit" Vault cluster to hold the unseal key — creating a circular dependency that must be carefully architected for DR. Seal High Availability (Seal HA) allows online migration between auto-unseal types without downtime.

### 1.3 Dynamic Secrets

Vault's [database secrets engine](https://developer.hashicorp.com/vault/docs/secrets/databases) generates database credentials dynamically on demand rather than storing static credentials. When a static database user is onboarded, Vault immediately and automatically rotates the user's password. The [PKI secrets engine](https://developer.hashicorp.com/vault/tutorials/db-credentials/database-secrets) issues TLS certificates on-demand, bypassing the traditional CSR-submission-and-approval workflow.

Dynamic secrets dramatically reduce credential exposure windows — a short-lived credential issued for a single deployment pipeline run cannot be stolen and reused after expiration. The operational trade-off is that every application must be instrumented to request and cache credentials from Vault at startup, adding integration complexity proportional to the number of services in the ISV's deployment.

### 1.4 Policy Management

Vault policies use HCL (HashiCorp Configuration Language) to define fine-grained ACLs on secret paths. Policy governance at scale requires a dedicated workflow: policy-as-code stored in version control, peer review processes, and automated testing pipelines to prevent privilege escalation through misconfigured policies. This is engineering work with no managed equivalent in a self-hosted deployment.

---

## 2. TLS Certificates: Internal CA and cert-manager

### 2.1 Internal CA Management

On-premises environments require a private Certificate Authority hierarchy. As [cert-manager documentation](https://cert-manager.io/docs/configuration/ca/) notes, "The CA issuer represents a Certificate Authority whose certificate and private key are stored inside the cluster as a Kubernetes Secret. Certificates issued by a CA issuer will not be publicly trusted." This means every consuming application must be configured to trust the internal CA's root certificate — an often-overlooked bootstrapping problem that grows with fleet size.

Enterprise deployments typically deploy a two-tier CA hierarchy: an offline root CA (air-gapped, rarely used) and one or more online intermediate CAs that issue end-entity certificates. The root CA's private key should be stored in an HSM or encrypted offline storage and accessed only for signing new intermediate CA certificates.

[cert-manager](https://cert-manager.io/docs/) automates TLS certificate issuance and renewal within Kubernetes, integrating with issuers including internal CAs, HashiCorp Vault's PKI engine, Let's Encrypt, and Venafi. cert-manager handles the full lifecycle: CSR generation, submission to the configured issuer, certificate storage as Kubernetes Secrets, and automated renewal before expiration.

### 2.2 Wildcard vs. Per-Service Certificates

Two certificate issuance strategies apply to on-premises multi-service deployments:

| Strategy | Advantages | Disadvantages |
|---|---|---|
| **Wildcard** (`*.internal.example.com`) | One certificate secures all subdomains; simpler ingress config | Compromise of one service's private key compromises all; must rotate entire wildcard on breach |
| **Per-service** (one cert per microservice) | Blast radius limited to one service; enables per-service rotation cadence | Certificate inventory multiplies with service count; higher management overhead |

cert-manager supports [wildcard certificate generation](https://medium.com/@harsh.manvar111/wild-card-certificate-using-cert-manager-in-kubernetes-3406b042d5a2) via DNS-01 ACME challenge. For dynamic workloads that scale automatically, wildcard certificates reduce the complexity of managing individual certificates — but at the cost of a wider blast radius on compromise.

### 2.3 Certificate Rotation

cert-manager automates renewal before expiration, configurable via `renewBefore` duration. However, rotation is only half the problem: applications must be instrumented to pick up rotated certificates without requiring restarts. Services that cache TLS certificates in memory at startup and never reload them will continue using the expired certificate even after cert-manager has rotated it — a common source of outages in on-premises microservice deployments.

---

## 3. Encryption at Rest

### 3.1 Disk Encryption: LUKS

[Linux Unified Key Setup (LUKS)](https://wiki.archlinux.org/title/Data-at-rest_encryption) is the standard block-level encryption layer for Linux on-premises deployments. LUKS stores cryptographic metadata — cipher, encrypted master key, and key derivation parameters — in the blockdevice header, abstracting partition and key management and providing protection against brute-force and dictionary attacks through key derivation functions (PBKDF2/Argon2).

LUKS protects against physically stolen disks but does not protect data from processes running on the same host — encryption is transparent to the operating system kernel once the volume is mounted. The operational requirement is managing LUKS passphrases or key files through a secrets manager (typically Vault) to avoid storing plaintext credentials on the host.

[Percona's MySQL on LUKS implementation guide](https://www.percona.com/blog/mysql-encryption-at-rest-part-1-luks/) demonstrates a common pattern: LUKS volumes holding database data directories, with the LUKS key retrieved from Vault at boot time.

### 3.2 Database-Level Encryption: TDE

[Transparent Data Encryption (TDE)](https://www.akeyless.io/blog/what-is-transparent-data-encryption-tde/) encrypts database data files, transaction logs, and backups using a Database Encryption Key (DEK) protected by a key hierarchy: DEK → Certificate or asymmetric key → Service Master Key → instance-level master key. TDE is effective against the risk of physically stolen storage media.

Key hierarchy in a self-hosted TDE deployment:

```
Database Encryption Key (DEK)
    └── Protected by: Certificate (stored in master DB) or EKM module
            └── Protected by: Service Master Key
                    └── Protected by: Instance Master Key / HSM
```

TDE can be used with an HSM so that the HSM manages the Key Encryption Key (KEK) rather than the DEK itself, keeping the most sensitive material in tamper-evident hardware. The operational requirement is that the HSM must be available at database startup — an HSM outage can prevent database startup entirely.

### 3.3 Application-Level Encryption

Application-level encryption is performed by the application before writing data to the database or storage layer, meaning data is encrypted regardless of whether TDE or disk encryption is in place — providing defense-in-depth. The operational challenge is key management: application encryption keys must be retrieved from Vault or a KMS at runtime, and the application must handle key rotation without decrypting and re-encrypting all existing data in a single atomic operation.

---

## 4. Encryption in Transit

### 4.1 mTLS in Service Meshes

[Mutual TLS (mTLS)](https://blog.gitguardian.com/mutual-tls-mtls-authentication/) cryptographically authenticates both parties in a connection — not just the server (as in standard TLS) but also the client — providing zero-trust lateral authentication between microservices. In on-premises deployments, mTLS is typically implemented at the service mesh layer using Istio or Linkerd, which inject sidecar proxies that handle certificate negotiation transparently without requiring application code changes.

[Istio's security model](https://istio.io/latest/docs/concepts/security/) uses SPIFFE (Secure Production Identity Framework for Everyone) identities encoded in X.509 certificates for service-to-service authentication. Each sidecar proxy holds a short-lived certificate issued by Istio's internal CA (Istiod). In on-premises deployments, Istiod must be deployed and maintained as a critical infrastructure component — an Istiod outage prevents new certificate issuance and blocks new service deployments.

### 4.2 TLS Termination Points

On-premises deployments have multiple TLS termination points, each requiring certificate and cipher management:

- **Ingress layer:** NGINX or HAProxy ingress controller terminates external TLS, presenting a certificate to external clients
- **Service mesh:** Sidecar proxies terminate and re-encrypt within the cluster (mTLS)
- **Database connections:** Application-to-database TLS using database server certificates
- **Vault API:** Vault's own listener requires a TLS certificate

### 4.3 Cipher Suite Management

[NGINX ingress controllers](https://medium.com/kranus-health-engineering/on-tls-cipher-suites-and-staying-sane-and-compliant-with-cert-manager-and-nginx-ingress-1717ec82d8b0) support cipher suite configuration via the `ssl-ciphers` ConfigMap parameter. A representative FIPS-aligned cipher suite for TLS 1.2/1.3:

```
ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384
```

A notable operational caveat: [TLS 1.3 cipher suites cannot be configured via the standard NGINX cipher string](https://github.com/kubernetes/ingress-nginx/issues/8507) — they are hardcoded into the TLS 1.3 specification. This creates compliance audit complexity when demonstrating cipher suite control to auditors who expect explicit enumeration.

---

## 5. Key Management: Generation, Rotation, Backup, and DR

### 5.1 Key Lifecycle

A comprehensive on-premises key management program covers six lifecycle phases:

1. **Generation:** Keys must be generated using a cryptographically secure random source; HSMs provide the highest assurance (true hardware random number generators)
2. **Storage:** Keys stored in Vault or HSM; never on filesystem as plaintext
3. **Rotation:** Regular rotation cadence per key type; Vault supports automated rotation schedules
4. **Backup/Escrow:** [Encrypted backups of HSM key material](https://cpl.thalesgroup.com/encryption/backup-hsm-cryptographic-key-protection) must be stored off-site on encrypted, offline storage devices
5. **DR Testing:** [Regular disaster recovery drills](https://phoenixnap.com/blog/encryption-key-management-best-practices) using non-production HSM instances to validate key recovery workflows
6. **Destruction:** Cryptographic erasure procedures for decommissioned key material

### 5.2 Key Ceremony

A formal key ceremony establishes the root of trust for the key hierarchy. Best practice requires multi-person (M-of-N) control: no single individual should have the ability to generate, export, or use root key material unilaterally. The ceremony must be documented, witnessed, and audited — creating a compliance artifact for regulated workloads.

[Best practices](https://whisperit.ai/blog/encryption-key-management-best-practices) require keeping security domain private keys on encrypted, offline storage devices such as encrypted USB drives stored in separate geographical locations in physical safes or lock boxes, and never on internet-connected computers.

### 5.3 Disaster Recovery

DR for encryption keys is the highest-stakes operational scenario: a lost master key means permanent, irrecoverable data loss. Recovery requirements include:

- Geographically distributed encrypted backups of all key material
- Documented and tested recovery runbooks
- Regular recovery drills (at minimum annually) using non-production environments
- Split-knowledge controls so no single operator can restore keys unilaterally

---

## 6. Hardware Security Modules (HSMs)

### 6.1 Procurement and Vendors

Major on-premises HSM vendors include [Thales (nShield)](https://cpl.thalesgroup.com/encryption/hardware-security-modules), [Entrust](https://www.entrust.com/products/hsm), [Futurex](https://www.futurex.com/products/hardware-security-modules), and [Fortanix](https://www.fortanix.com/platform/data-security-manager/hardware-security-module). HSMs are available as rack-mounted appliances, PCIe cards, and USB-attached devices. On-premises HSMs from vendors like Thales or Entrust [typically range from $5,000 to $50,000 per unit](https://www.ssl.com/article/on-premises-vs-cloud-hsms-a-comparison/) for initial purchase, plus annual maintenance fees of 15–20% of the hardware cost. Over a three-year period, on-premises setups may total $20,000–$200,000 depending on scale.

### 6.2 FIPS Compliance: Critical 2026 Deadline

FIPS 140-2 and FIPS 140-3 are NIST standards specifying cryptographic module security requirements. A critical procurement constraint is that [NIST has announced all existing FIPS 140-2 certificates will remain valid only until September 2026](https://tuxcare.com/blog/understanding-fips-140-3-and-why-it-matters-for-agencies/), after which only FIPS 140-3-validated modules will be accepted for new federal procurements. ISVs serving government or regulated-industry customers must ensure any HSMs procured now are FIPS 140-3 validated to avoid forced hardware replacement before 2027.

Fortanix offers FIPS 140-2 Level 3 validated HSMs. Entrust nShield HSMs are available in [FIPS 140-2 and 140-3 certified form factors](https://www.entrust.com/products/hsm). ISVs should confirm 140-3 certification explicitly before purchasing.

### 6.3 Vault HSM Integration

[Vault's HSM integration via seal wrap](https://developer.hashicorp.com/vault/tutorials/archive/seal-wrap) uses the HSM to wrap Vault's master key, providing hardware-rooted key protection. Vault communicates with HSMs via PKCS#11 (the industry-standard cryptographic token interface). The operational requirement is deploying and maintaining PKCS#11 drivers on all Vault nodes — driver compatibility with the host OS and HSM firmware versions must be validated before upgrades.

---

## 7. Certificate Lifecycle: Expiration, Renewal, Revocation

### 7.1 Expiration Tracking

Certificate expiration is the single most common cause of self-inflicted outages in on-premises PKI environments. Organizations need to [automate and centrally manage their digital certificates](https://www.keyfactor.com/blog/what-is-a-certificate-revocation-list-crl-vs-ocsp/) to avoid costly outages from expiration. Tools for certificate inventory and expiration monitoring include:

- **cert-manager** (Kubernetes-native): Prometheus metrics expose certificate expiry dates; Grafana dashboards can alert at configurable thresholds
- **Keyfactor, Venafi, AppViewX:** Enterprise certificate lifecycle management platforms with discovery, inventory, and automated renewal
- **Smallstep step-ca:** [Open-source CA](https://smallstep.com/docs/step-ca/revocation/) with built-in ACME support for automated renewal

### 7.2 CRL vs. OCSP Revocation

On-premises PKI must implement a certificate revocation mechanism to handle compromised or prematurely expired certificates:

- **Certificate Revocation List (CRL):** A periodically published list of revoked certificates. [For internal PKI, passive revocation via CRL](https://smallstep.com/docs/step-ca/revocation/) is a good option because it avoids the complexity of real-time third-party OCSP responder infrastructure.
- **OCSP (Online Certificate Status Protocol):** Real-time revocation status checking. The industry is shifting: as of [May 7, 2025, Let's Encrypt removed OCSP URLs from newly issued certificates entirely](https://shop.trustico.com/blogs/stories/ssl-certificate-revocation-explained-what-the-end-of-ocsp-means-for-website-security) and added CRL URLs instead. The CA/Browser Forum voted in August 2023 to make OCSP support optional for CAs while making CRL support mandatory.

For on-premises internal PKI serving internal services only, CRL-based revocation is operationally simpler and does not require a continuously available OCSP responder. The trade-off is that CRL checking is periodic rather than real-time — a revoked certificate may be accepted until the next CRL refresh.

### 7.3 Emergency Rotation

Emergency certificate rotation (in response to private key compromise) requires executing the full rotation workflow on a compressed timeline. Pre-built runbooks, automation scripts, and tested Vault/cert-manager configurations are required to execute emergency rotation without service downtime. Without pre-built automation, emergency rotation of certificates across a large microservice fleet can take hours — during which the compromised certificate remains in use.

---

## 8. Cloud Comparison: What Operational Burden Disappears?

The following table quantifies the operational profile across all three deployment models for the secrets, certificates, and encryption domain.

| Capability | On-Premises | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native |
|---|---|---|---|
| **Secrets Management** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Vault cluster; Raft HA; unseal automation; policy-as-code pipeline | Vault on Kubernetes (Helm); or cloud secret store CSI driver integration | AWS Secrets Manager / Azure Key Vault / GCP Secret Manager — fully managed, auto-rotated |
| | PKCS#11, dynamic secrets, Vault Agent sidecar | cert-manager + ExternalSecrets Operator | Native IAM-gated secret access; no rotation functions to maintain |
| | Est. FTE: 1.0–1.5 | Est. FTE: 0.5–0.75 | Est. FTE: 0.1–0.2 |
| **TLS Certificates** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Internal CA hierarchy; cert-manager; CRL/OCSP infrastructure; chain-of-trust distribution | cert-manager with cloud CA integration (ACM PCA, GCP CAS) | AWS ACM / Azure Managed Certs / GCP CAS — auto-issued, auto-renewed, zero operator touch |
| | Wildcard vs. per-service tradeoff; rotation reload testing | Automated but still requires PKI design decisions | Public certs automatically renewed; private certs via managed CA service |
| | Est. FTE: 0.5–0.75 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |
| **Encryption at Rest** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | LUKS volume management; TDE with key hierarchy; HSM integration; application-level envelope encryption | Node disk encryption (provider-managed); DB encryption with cloud KMS | Cloud-provider-managed KMS; RDS/managed DB encryption is one checkbox; keys auto-rotated |
| | Key hierarchy design; rotation without downtime | Key materials in cloud KMS; operator manages access policies | Est. FTE: 0.05–0.1 |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | |
| **Encryption in Transit / mTLS** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Istio/Linkerd deployment and Istiod maintenance; cipher suite configuration per ingress; certificate reload | Managed service mesh options (ASM, Istio on EKS); cloud LB with managed TLS | Cloud load balancer terminates TLS; service-to-service encryption via provider mesh or sidecar |
| | Internal mTLS SPIFFE identity lifecycle | SPIFFE/SPIRE or cloud-native identity | Est. FTE: 0.1–0.2 |
| | Est. FTE: 0.5–0.75 | Est. FTE: 0.25–0.5 | |
| **HSM** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Physical procurement ($5K–$50K/unit); FIPS 140-3 migration by Sept 2026; PKCS#11 driver management; firmware updates | Cloud HSM via provider (AWS CloudHSM, Azure Managed HSM) on dedicated hardware; no physical management | AWS CloudHSM / Azure Managed HSM / GCP Cloud HSM — provider manages hardware; pay-per-use |
| | Key ceremony; DR drills; geographically distributed backups | Key ceremony still required; DR partially managed | Est. FTE: 0.1–0.25 |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | |

**FTE Estimation Assumptions:**
- Assumes an ISV operating a mid-size SaaS product with 20–50 microservices and 5–20 customer tenants
- On-premises FTE estimates cover: initial design, deployment, ongoing operations, incident response, and annual DR testing
- "On-call burden" not included in FTE estimates; add 0.25 FTE equivalent for on-call rotation coverage across secrets/certs domain
- Cloud-native FTE reflects integration engineering and IAM policy management only — no infrastructure operations
- Estimates are professional judgment based on industry practice; specific benchmarks are [UNVERIFIED] due to absence of published peer-reviewed staffing data for this precise scope

---

## 9. Cloud Service Equivalents: Operational Burden Analysis

### 9.1 AWS KMS + ACM + Secrets Manager

[AWS Secrets Manager](https://aws.amazon.com/blogs/security/how-to-choose-the-right-aws-service-for-managing-secrets-and-configurations/) provides automated rotation for RDS credentials, API keys, and OAuth tokens with no rotation functions to maintain by the operator. Access control is enforced via IAM with multi-layered policies: resource-based policies, resource control policies, service control policies, and attribute-based access control.

[AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/) simplifies provisioning, managing, and deploying publicly trusted TLS certificates for AWS services, with automated renewal. Private certificate management is available via ACM Private CA (a managed subordinate CA service). Operators retain responsibility for PKI hierarchy design but eliminate all infrastructure operations.

[AWS KMS](https://docs.aws.amazon.com/decision-guides/latest/cryptography-on-aws-how-to-choose/guide.html) provides fully managed key storage, rotation, and audit logging via CloudTrail. Hardware-backed keys (using AWS HSMs) are available without direct HSM management.

### 9.2 Azure Key Vault + Managed Certificates

[Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates) manages keys, secrets, and certificates in a multi-tenant service with hardware HSM backing. Certificate owners create policies that direct Key Vault to manage the full certificate lifecycle including renewal notifications and automated renewal from supported CAs.

[Azure Key Vault has latency under 10ms within Azure regions](https://sslinsights.com/azure-key-vault-vs-hashicorp-vault/) with throughput of approximately 2,000 requests per second on the Premium tier. Self-hosted Vault can achieve 10,000+ requests/second with horizontal scaling — a trade-off relevant only for very high-throughput secret access patterns.

Azure offers a spectrum of managed HSM options: [Key Vault (multi-tenant), Managed HSM (single-tenant, FIPS 140-3 Level 3), Cloud HSM (dedicated hardware), and Payment HSM](https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management-choose) — allowing graduated levels of isolation without physical hardware management.

### 9.3 GCP Cloud KMS + Certificate Authority Service

[GCP's Certificate Authority Service (CAS)](https://cloud.google.com/security/products/certificate-authority-service) can reduce PKI deployment time from months to minutes. The service supports issuing [up to 25 certificates per second per CA (DevOps tier)](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview), capable of issuing millions of certificates per CA.

Cloud-based PKI costs organizations [approximately $305,000 less over a comparable lifecycle versus on-premises managed PKI](https://www.encryptionconsulting.com/cloud-based-public-key-infrastructure-architecture/) when factoring in staffing, hardware, and operational overhead. GCP stores private CA keys using Cloud HSM, which is [FIPS 140-2 Level 3 validated](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) and available across Americas, Europe, and Asia Pacific regions.

A limitation: GCP CAS [works best inside Google Cloud](https://www.securew2.com/blog/google-cloud-certificate-authorities-service-alternative); multi-cloud and hybrid enterprises face limited integrations across identity providers, MDMs, and non-GCP services.

---

## Sources

- [Seal/Unseal | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/docs/concepts/seal)
- [Transit auto-unseal best practices | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/docs/configuration/seal/transit-best-practices)
- [High Availability | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/docs/internals/high-availability)
- [Vault with integrated storage reference architecture | HashiCorp Developer](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-reference-architecture)
- [Raft integrated storage | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/docs/internals/integrated-storage)
- [HSM integration - seal wrap | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/tutorials/archive/seal-wrap)
- [Database secrets engine | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/docs/secrets/databases)
- [Dynamic secrets for database credential management | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/tutorials/db-credentials/database-secrets)
- [cert-manager Documentation](https://cert-manager.io/docs/)
- [CA issuer - cert-manager Documentation](https://cert-manager.io/docs/configuration/ca/)
- [Data-at-rest encryption - ArchWiki](https://wiki.archlinux.org/title/Data-at-rest_encryption)
- [MySQL Encryption at Rest – Part 1 (LUKS) | Percona](https://www.percona.com/blog/mysql-encryption-at-rest-part-1-luks/)
- [What is Transparent Data Encryption (TDE)? | Akeyless](https://www.akeyless.io/blog/what-is-transparent-data-encryption-tde/)
- [Hardware Security Modules | Futurex](https://www.futurex.com/products/hardware-security-modules)
- [FIPS 140-2 Level 3 HSM | Fortanix](https://www.fortanix.com/resources/datasheets/fips-140-2-level-3-hardware-security-module-hsm)
- [Hardware Security Modules | Entrust](https://www.entrust.com/products/hsm)
- [Understanding FIPS 140-3 and Why It Matters for Agencies | TuxCare](https://tuxcare.com/blog/understanding-fips-140-3-and-why-it-matters-for-agencies/)
- [Mutual TLS (mTLS) Authentication - A Complete Guide | GitGuardian](https://blog.gitguardian.com/mutual-tls-mtls-authentication/)
- [Istio Security Concepts](https://istio.io/latest/docs/concepts/security/)
- [On TLS cipher suites with cert-manager and nginx-ingress | Medium](https://medium.com/kranus-health-engineering/on-tls-cipher-suites-and-staying-sane-and-compliant-with-cert-manager-and-nginx-ingress-1717ec82d8b0)
- [TLSv1.3 ciphers cannot be changed - kubernetes/ingress-nginx #8507](https://github.com/kubernetes/ingress-nginx/issues/8507)
- [What is a Certificate Revocation List (CRL) vs OCSP? | Keyfactor](https://www.keyfactor.com/blog/what-is-a-certificate-revocation-list-crl-vs-ocsp/)
- [Certificate Revocation Management | Smallstep step-ca](https://smallstep.com/docs/step-ca/revocation/)
- [SSL Certificate Revocation - End of OCSP | Trustico](https://shop.trustico.com/blogs/stories/ssl-certificate-revocation-explained-what-the-end-of-ocsp-means-for-website-security)
- [10 Essential Encryption Key Management Best Practices | Whisperit](https://whisperit.ai/blog/encryption-key-management-best-practices)
- [16 Encryption Key Management Best Practices | phoenixNAP](https://phoenixnap.com/blog/encryption-key-management-best-practices)
- [Backup HSM Cryptographic Key Protection | Thales](https://cpl.thalesgroup.com/encryption/backup-hsm-cryptographic-key-protection)
- [On-Premises vs. Cloud HSMs | SSL.com](https://www.ssl.com/article/on-premises-vs-cloud-hsms-a-comparison/)
- [Cloud-Based vs On-Premises HSMs | Encryption Consulting](https://www.encryptionconsulting.com/cloud-based-versus-on-premise-hsm/)
- [Key Management Systems: Cloud-Based vs On-Premises | Futurex](https://www.futurex.com/blog/key-management-systems-software-vs-hardware)
- [How to choose the right AWS service for secrets | AWS Security Blog](https://aws.amazon.com/blogs/security/how-to-choose-the-right-aws-service-for-managing-secrets-and-configurations/)
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
- [Choosing an AWS cryptography service](https://docs.aws.amazon.com/decision-guides/latest/cryptography-on-aws-how-to-choose/guide.html)
- [Azure Key Vault Keys, Secrets, and Certificates Overview | Microsoft Learn](https://learn.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates)
- [How to choose the right Azure key management solution | Microsoft Learn](https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management-choose)
- [Azure Key Vault vs HashiCorp Vault 2025 Comparison | SSL Insights](https://sslinsights.com/azure-key-vault-vs-hashicorp-vault/)
- [Certificate Authority Service | Google Cloud](https://cloud.google.com/security/products/certificate-authority-service)
- [Certificate Authority Service Overview | GCP Docs](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)
- [Cloud-based PKI - GCP, AWS, and Azure | Encryption Consulting](https://www.encryptionconsulting.com/cloud-based-public-key-infrastructure-architecture/)
- [Google Cloud CAS Alternative | SecureW2](https://www.securew2.com/blog/google-cloud-certificate-authorities-service-alternative)
- [Wild card certificate using cert-manager in Kubernetes | Medium](https://medium.com/@harsh.manvar111/wild-card-certificate-using-cert-manager-in-kubernetes-3406b042d5a2)

---

## Key Takeaways

- **Aggregate FTE burden is 2.5–5.0 FTEs on-premises vs. 0.4–0.85 for Managed Kubernetes and 0.4–0.85 for Cloud-Native** across secrets, certificates, encryption at rest, encryption in transit, and HSM management — representing the highest operational cost differential of any single capability domain in the on-premises model.
- **HashiCorp Vault is the de facto on-premises secrets platform**, but it requires a minimum five-node Raft cluster, a carefully designed auto-unseal strategy (which on pure on-premises deployments creates a chicken-and-egg dependency), policy-as-code governance, and continuous operational attention — none of which is eliminated even with Vault on Kubernetes (Managed K8s column).
- **The FIPS 140-2 end-of-life deadline of September 2026 is an immediate procurement risk:** any ISV procuring on-premises HSMs today must explicitly verify FIPS 140-3 certification or face forced hardware replacement within 18 months.
- **Cloud-native secret and certificate services eliminate nearly all infrastructure operations** — AWS Secrets Manager, Azure Key Vault, and GCP CAS handle rotation, renewal, revocation, and HSM hardware management automatically, reducing the ISV's responsibility to IAM policy design and integration engineering.
- **Certificate expiration remains the top self-inflicted outage cause in on-premises PKI:** cert-manager automates issuance and renewal, but application-side certificate reloading (without restarts) must be explicitly engineered into each service — a requirement that has no managed equivalent and scales linearly with service count.
