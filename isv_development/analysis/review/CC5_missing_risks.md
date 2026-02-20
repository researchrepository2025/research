# CC5 — Missing Risks and Underweighted Dynamics in the Three-Phase On-Premises Ratings

**Role:** Cross-Cutting Gap Analysis — Missing Risks
**Date:** 2026-02-19
**Primary Source:** `analysis/three_phase_on_prem_ratings.md`
**Cross-References:** `analysis/review/RP4c_P4_completeness.md`, `analysis/review/RP2e_P2_completeness.md`, `analysis/review/RP1a_P1_infrastructure_core.md`
**Scope:** Gap identification only. No existing ratings are re-derived or modified in this document.

---

## Executive Summary

The three-phase on-premises ratings framework (`analysis/three_phase_on_prem_ratings.md`) accurately captures the technical engineering cost of cloud-to-on-premises refactoring across 38 MECE subsegments but contains six structurally absent or severely underweighted risk categories: organizational change management for the ISV's own support team, customer communication and upgrade coordination overhead, vendor lock-in reversal cost during Phase 1, supply chain security for self-hosted open source components, talent acquisition difficulty for on-premises specialists, and regulatory variance across a heterogeneous customer base. None of these six categories appears as a rated subsegment or an explicit cost assumption in the existing framework, creating planning blind spots that are invisible to readers of the ratings tables. Each gap is documented below with direct citations to source files and external evidence.

---

## 1. Organizational Change Management — ISV Team Restructuring

### 1.1 What the Framework Currently Captures

The ratings file describes Phase 1 as a "one-time engineering investment" and Phase 3 as "recurring annual cost for maintaining and updating ISV software across all deployed customer environments."

[FACT]
"Phase 3 (Ongoing Updates & Support): Recurring maintenance, upgrades, patching, incident response. Scales with N customers × update frequency."
— `analysis/three_phase_on_prem_ratings.md` §2, Three Deployment Phases table

[FACT]
"P1 (Control Plane) dominates both dimensions across all three phases. It is the hardest AND the most effort-intensive in Phase 1, Phase 2, and Phase 3. This is the core of the ISV's on-prem resistance."
— `analysis/three_phase_on_prem_ratings.md` §8, Key Finding 1

### 1.2 What the Framework Does Not Capture

The ratings assume the ISV already has a team capable of executing the rated work. The framework does not capture the cost of building that team — including the organizational restructuring required when a cloud-native SaaS company decides to support on-premises deployments.

A cloud-native ISV support model is fundamentally different from an on-premises support model:

- Cloud-native: SRE teams access shared infrastructure; incidents are resolved centrally; customers interact only at the application layer
- On-premises: Field engineers must be embedded with customers, or remote support must be augmented with customer-side access protocols; each customer's environment is isolated

[FACT]
"Transitioning from perpetual licensing to SaaS restructures ISV cash flows and metrics. Annual Recurring Revenue (ARR) and Net Revenue Retention (NRR) replace one-time bookings as key indicators."
— AWS Blogs, "Accelerating SaaS Migration Success"
URL: https://aws.amazon.com/blogs/migration-and-modernization/accelerating-saas-migration-success-aws-programs-tools-and-expertise-that-drive-isv-growth/

The reverse direction — a SaaS ISV adding on-premises support — requires equivalent restructuring: new engineering titles (Field Engineer, Solutions Architect for On-Premises, Platform Engineer), new escalation paths that account for customer network isolation, new deployment runbooks for each customer environment, and new service-level agreements that account for the ISV's inability to push hotfixes without customer coordination.

[FACT]
"Level 3 support comprises specialists like software engineers and technical support specialists. These support personnel have access to the company's higher-level systems and architecture. They are well-versed in technical troubleshooting and often encounter bugs, relay them to the company's developers and interface with customers to troubleshoot."
— FullView.io, "How to Structure a SaaS Customer Support Team"
URL: https://www.fullview.io/blog/how-to-structure-your-saas-support-team-as-your-company-grows

For on-premises ISVs, this Level 3 function must be staffed by engineers who understand both the ISV's software stack and the customer's hardware environment — a combined skill profile that is not required for cloud-native SaaS support and is expensive to recruit (see §5 on talent acquisition).

### 1.3 Gap Classification

The organizational change management cost is a pre-Phase 1 or parallel-to-Phase-1 investment that is not captured in the CP or AL subsegments. It appears nowhere in the 38-subsegment framework as a rated cost. It is most acute when the ISV first commits to on-premises support (the organizational transformation cost), and recurs as a training and documentation overhead as N customers grows. [UNVERIFIED: No published ISV case study with quantified organizational change management cost for cloud-to-on-premises support model transition was located. This claim rests on structural reasoning from support model literature rather than empirical data.]

---

## 2. Customer Communication Overhead — Upgrade Coordination and Incident Response

### 2.1 What the Framework Currently Captures

The framework acknowledges customer-specific upgrade coordination at CP-07 (Deploy Lifecycle / Rollback):

[FACT]
"N customers = N separate deployment coordination sequences for every release. CVE patches: 50 customers = 50 patch cycles. 3–5 concurrent software versions across customer base. Rollback requires per-customer database state awareness. This subsegment's effort is directly proportional to customer count."
— `analysis/three_phase_on_prem_ratings.md` §6, CP-07 Phase 3 Notes

[FACT]
"CP-07 | Deploy Lifecycle / Rollback | Phase 3: RD 5 / TE 5 / Scales with N: Yes"
— `analysis/three_phase_on_prem_ratings.md` §6, P1 Control Plane Phase 3 table

### 2.2 What the Framework Does Not Capture

The CP-07 rating captures the engineering labor of performing deployments but does not capture the coordination labor of scheduling, communicating, and managing customer expectations around those deployments. These are distinct activities:

- Engineering labor: writing code, building pipelines, executing deployment scripts, validating smoke tests
- Coordination labor: scheduling change windows with customer IT teams, sending pre-deployment notifications, holding go/no-go calls, drafting post-deployment status reports, managing customer escalations when a deployment causes application-layer issues visible to end users

At scale, coordination labor can equal or exceed engineering labor for each deployment event. In regulated industries (FedRAMP, HIPAA, financial services), change management processes may require:
- Formal change requests submitted 5–10 business days in advance
- Customer IT security review of every deployment package
- Post-deployment evidence collection for audit trails

[FACT]
"Large enterprises with IT operations spread across multiple regions and time zones face incident collaboration challenges, especially when different teams use different communication tools, resulting in delays and slower resolution times."
— Squadcast, "The Complete Enterprise Incident Management Playbook"
URL: https://medium.com/@squadcast/the-complete-enterprise-incident-management-playbook-a-comprehensive-guide-for-2024-cc0f843657b2

[FACT]
"Effective enterprise incident management demands seamless communication between technical teams, business stakeholders, and leadership."
— TaskCall, "Enterprise Incident Management"
URL: https://taskcallapp.com/blog/enterprise-incident-management

For on-premises deployments specifically, the ISV cannot self-authorize a patch deployment. Every change requires customer approval, scheduling, and post-change verification — creating a communication thread per deployment event per customer that has no equivalent in cloud-native SaaS operations.

### 2.3 Gap Classification

The RP2e completeness review (`analysis/review/RP2e_P2_completeness.md`) identified the absence of a Notification and Communication Services subsegment at the application layer. The gap identified here is distinct: it is not about notification infrastructure but about the human coordination protocol between the ISV and each customer for every maintenance event. This coordination overhead is absent from all 38 subsegments and from the FTE estimates in Phase 3. It is most plausibly a hidden multiplier on CP-07 (Deploy Lifecycle) and CP-10 (Security Operations) Phase 3 effort — specifically, the "per-customer" fraction of each of those subsegments is underestimated because it only accounts for technical execution, not coordination.

[FACT]
"Identity incidents require per-customer investigation."
— `analysis/three_phase_on_prem_ratings.md` §6, CP-03 Phase 3 Notes

This note confirms the pattern — but the investigation coordination cost (scheduling access, obtaining logs, communicating findings, waiting for customer IT team availability) is not rated as effort.

---

## 3. Vendor Lock-In Reversal Cost — Phase 1 Cloud API Extraction

### 3.1 What the Framework Currently Captures

Phase 1 addresses cloud-to-on-premises refactoring at the infrastructure level. P4 (AI Model Plane) receives S1 (Managed API Integration) with:

[FACT]
"Replace Bedrock/Azure OpenAI/Vertex AI endpoint calls with customer's inference endpoint. Auth method adaptation (cloud IAM → customer's auth). Error handling for different response schemas. Same pattern, different endpoint."
— `analysis/three_phase_on_prem_ratings.md` §4, S1 Phase 1 Notes

[FACT]
"Phase 1: Initial Refactoring — One-time engineering investment to replace cloud-managed services with self-hosted open-source equivalents."
— `analysis/three_phase_on_prem_ratings.md` §4, Phase 1 description

### 3.2 What the Framework Does Not Capture

The framework treats cloud API replacement as a primarily technical task: swap endpoint URLs, adapt auth methods, update error handling. This framing underweights the extraction cost from cloud-specific APIs that have no open-source equivalent or that provide proprietary behavioral guarantees which self-hosted equivalents cannot replicate.

[FACT]
"Cloud APIs are not yet standardized, making it complex for customers to change providers."
— Cloudflare, "What is vendor lock-in?"
URL: https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/

[FACT]
"Many SaaS platforms store data in proprietary formats that aren't easily exportable, with most offering only incomplete data or unusable formats, trapping valuable business data within the platform."
— CloudEagle, "What Is Vendor Lock-In?"
URL: https://www.cloudeagle.ai/resources/glossaries/what-is-vendor-lock-in

[FACT]
"The cost of cloud migration ranges from $5,000 to $100,000 depending on the scope of needed application modification. Migration requiring application re-architecting typically falls between $20,000 and $100,000."
— ScienceSoft, "Cloud Migration Guide: Steps, Platforms, Costs in 2025"
URL: https://www.scnsoft.com/cloud/migration

The specific vendor lock-in reversal risks not captured in the current Phase 1 ratings include:

**AWS-specific API behaviors with no OSS equivalent:**
- DynamoDB Global Tables (multi-region active-active) → MongoDB or CockroachDB (different consistency semantics, not a drop-in replacement)
- SQS FIFO queues (exactly-once processing guarantees) → RabbitMQ or NATS (different delivery semantics requiring application code changes)
- Step Functions (AWS-proprietary state machine DSL) → Temporal (requires rewriting all workflow definitions in Temporal's Go/Java/TypeScript SDK)
- Lambda function chains → custom worker processes (architectural pattern change, not a config swap)

[FACT]
"Replace Step Functions with Temporal workflows. Event schema validation, dead-letter handling, and retry logic must be re-implemented against new message bus APIs."
— `analysis/three_phase_on_prem_ratings.md` §4, AL05 Phase 1 Notes

The AL05 rating of RD 3 / TE 3 treats the Step Functions → Temporal migration as moderate difficulty. This may underweight the depth of the rewrite for ISVs with complex Step Functions state machines. A multi-year cloud-native ISV may have hundreds of Step Functions workflows with AWS-proprietary branching, error handling, and retry semantics. Temporal's SDK is not a translation layer; it requires rewriting the workflow logic in application code.

### 3.3 Gap Classification

The vendor lock-in reversal cost is partially captured in AL05 and DS6 (Kafka migration) but is systematically underweighted because the framework treats cloud-to-OSS substitution as equivalent-capability replacement. For ISVs with deep investment in AWS-proprietary services (Step Functions, DynamoDB Streams, Kinesis Firehose, AWS EventBridge Pipes) or Azure-proprietary services (Azure Service Bus sessions, Durable Functions, Azure Event Grid custom topics with advanced routing), the Phase 1 effort could be materially higher than rated. The RP1a review (`analysis/review/RP1a_P1_infrastructure_core.md`) noted that SUSE Rancher and VMware pricing disruptions have already forced ISVs to re-evaluate their K8s distribution toolchain; cloud API lock-in is an analogous forcing function at the application layer.

---

## 4. Supply Chain Security — Self-Hosted Open Source CVE Response Velocity

### 4.1 What the Framework Currently Captures

CP-10 (Security Operations) covers Phase 1 and Phase 3 security posture:

[FACT]
"Replace GuardDuty/Defender with Falco for runtime protection. Self-hosted vulnerability scanning pipeline. Intrusion detection. Security event aggregation."
— `analysis/three_phase_on_prem_ratings.md` §4, CP-10 Phase 1 Notes

[FACT]
"Vulnerability scanning, incident response, runtime protection across N environments. Security tooling (Falco) is shared; incident investigation and patch coordination is per-customer. CVE response time pressure."
— `analysis/three_phase_on_prem_ratings.md` §6, CP-10 Phase 3 Notes

### 4.2 What the Framework Does Not Capture

The framework captures the operational security tooling for on-premises environments (Falco, vulnerability scanners) but does not capture the supply chain security risk introduced by the on-premises component stack itself. An on-premises ISV ships 40+ self-hosted open source components (Kubernetes, Kafka, PostgreSQL, Redis, MinIO, Milvus, Prometheus, Grafana, Loki, Tempo, Vault, Keycloak, Temporal, ArgoCD, and more). Each of these is a CVE surface.

[FACT]
"CVE growth has grown 463% in the last decade."
— Sonatype, "10th Annual State of the Software Supply Chain Report" (2024)
URL: https://www.sonatype.com/state-of-the-software-supply-chain/2024/scale

[FACT]
"In 2024, over 40,000 CVEs were published — a 38% increase year-over-year, with more than 20,000 having CVSS scores ≥ 7.0 (high or above), and over 4,400 being critical (CVSS 9-10)."
— SecurityWeek, "Cyber Insights 2025: Open Source and the Software Supply Chain"
URL: https://www.securityweek.com/cyber-insights-2025-open-source-and-the-software-supply-chain/

[FACT]
"Nearly a quarter (~23.6%) of Known Exploited Vulnerabilities (KEVs) are now being exploited on or before their public disclosure, with attackers moving faster than security teams can respond."
— SecurityWeek, "Cyber Insights 2025: Open Source and the Software Supply Chain"
URL: https://www.securityweek.com/cyber-insights-2025-open-source-and-the-software-supply-chain/

[FACT]
"The number of malicious packages has grown by 156% year-over-year."
— Sonatype, "10th Annual State of the Software Supply Chain Report" (2024), press release
URL: https://www.globenewswire.com/news-release/2024/10/10/2961239/0/en/Sonatype-s-10th-Annual-State-of-the-Software-Supply-Chain-Report-Reveals-156-Surge-in-Open-Source-Malware.html

The supply chain security gap for on-premises ISVs has three dimensions not rated in CP-10:

**Dimension 1 — SBOM generation and delivery.** CISA guidance (2024) requires that ISVs shipping software to enterprise customers — especially government customers (FedRAMP, CMMC) — produce Software Bill of Materials for all distributed components. For an on-premises ISV shipping 40+ open source components, SBOM generation, maintenance, and customer delivery is a non-trivial ongoing engineering function.

[FACT]
"For software that is installed on systems at the customer premises, the SBOM metadata can be distributed along with the binary, and along with the software."
— CISA, "Securing the Software Supply Chain: Recommended Practices for SBOM Consumption" (2024)
URL: https://www.cisa.gov/sites/default/files/2024-08/SECURING_THE_SOFTWARE_SUPPLY_CHAIN_RECOMMENDED_PRACTICES_FOR_SOFTWARE_BILL_OF_MATERIALS_CONSUMPTION-508.pdf

**Dimension 2 — CVE response velocity across N customer environments.** When a critical CVE is published for a component the ISV distributes (e.g., a Kafka or PostgreSQL CVE), the ISV must patch N customer environments. In cloud-native SaaS, the ISV patches its own infrastructure once. In on-premises, patching requires scheduling a maintenance window with each customer, obtaining change control approval, and executing the patch per-customer. The CP-07 Phase 3 rating (RD 5 / TE 5) partially captures deployment coordination, but does not specifically account for the time-pressure dimension of CVE response — where exploited vulnerabilities may require emergency patches within 24–72 hours regardless of customer availability.

**Dimension 3 — Artifact registry security for air-gapped environments.** On-premises customers who operate air-gapped networks require the ISV to maintain a local artifact mirror (container images, Helm charts, OS packages) that has been scanned and signed. The ISV's Phase 1 CP-06 build (CI/CD Pipeline / GitOps) includes artifact registry, but the security scanning, signing, and vulnerability management of that mirror is a distinct ongoing function not rated separately.

[FACT]
"An SBOM has emerged as a key building block in software security and software supply chain risk management. An SBOM is a nested inventory, a list of ingredients that make up software components."
— CISA, SBOM page
URL: https://www.cisa.gov/sbom

### 4.3 Gap Classification

Supply chain security is mentioned in CP-10 as "CVE response time pressure" but is not rated as a separate effort dimension. The three sub-dimensions above (SBOM generation, CVE response velocity across N environments, and artifact mirror security) are collectively underweighted. The RP1a review noted that "air-gapped customers [are] a distinct cost tier" for CP-06, but did not rate the supply chain security implications of that air-gap requirement.

[FACT]
"Air-gapped customers as distinct cost tier."
— `analysis/review/RP1a_P1_infrastructure_core.md`, referenced in the prompt cross-reference context for this document

---

## 5. Talent Acquisition Difficulty — On-Premises Specialist Roles

### 5.1 What the Framework Currently Captures

The FTE estimates in Phase 3 state total headcount requirements (e.g., "20–38 FTE" for P1 Control Plane) but contain no assumption about:
- How long it takes to recruit those FTEs
- What premium salary those FTEs command relative to cloud-native generalists
- What happens to delivery timelines if those roles cannot be filled

[FACT]
"P1 Control Plane Phase 3: Annual FTE (research-based) 20–38 FTE. Key Cost Driver: K8s upgrades, security patching, deploy coordination across N customers."
— `analysis/three_phase_on_prem_ratings.md` §6, Phase 3 Summary table

### 5.2 What the Framework Does Not Capture

The specific specializations required for the on-premises support model — platform engineers with self-hosted Kubernetes expertise, Kafka operators, Vault administrators, and security engineers with on-premises tooling experience — are among the scarcest technical roles in the market.

[FACT]
"More than a third of respondents in a new Spectro Cloud study say it's difficult to find Kubernetes experts to achieve cloud native goals."
— Spectro Cloud, "2025 State of Production Kubernetes" report
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

[FACT]
"40% say they lack the skills and headcount to manage Kubernetes."
— Spectro Cloud, "2025 State of Production Kubernetes" (455 professionals surveyed, May 2025, organizations ≥250 employees)
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

[FACT]
"Three quarters of businesses that use Kubernetes today say their adoption has been inhibited by the complexity of managing it, and by difficulties accessing the right talent and skills."
— Spectro Cloud, "2025 State of Production Kubernetes" (2025)
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

[FACT]
"The talent shortage is especially acute in strategic domains: AI and ML engineering (68%), cybersecurity and compliance (65%), FinOps and cost optimization (61%), cloud computing (59%), and platform engineering (56%)."
— Linux Foundation, "2024 State of Tech Talent Report" (released April 16, 2024)
URL: https://www.linuxfoundation.org/blog/the-2024-state-of-tech-talent-report

[FACT]
"Organizations spend an average of 5.4 months on recruitment, with 64% taking over four months to fill open positions. SRE/platform engineers require among the longest recruitment periods."
— Linux Foundation, "2024 State of Tech Talent Report"
URL: https://www.linuxfoundation.org/blog/the-2024-state-of-tech-talent-report

[FACT]
"The average salary for Kubernetes engineers falls between $140,000 and $160,000 per year, with the median salary close to $140,000, and salaries generally ranging between $100,000 and $180,000, though top professionals can exceed $200,000 annually."
— Bluelight, "Kubernetes Engineer Salary Guide"
URL: https://bluelight.co/blog/kubernetes-salary-guide

For the 20–38 FTE Phase 3 P1 estimate to be achievable, the ISV must recruit platform engineers, database operators, security engineers, and K8s specialists — all in the top-scarcity tiers of the 2024-2025 talent market, with 5+ month average hiring cycles and $140K–$200K+ salaries. Neither the hiring timeline nor the salary premium appears in the ratings framework. An ISV that plans to hire 30 platform engineers to staff Phase 3 operations but does not model a 6–18 month ramp-up period will face an execution gap between planned and actual support capacity.

### 5.3 Gap Classification

The talent acquisition difficulty for on-premises specializations is fully absent from all 38 subsegments. The ratings treat FTE as an output (how many FTEs are required) rather than as a constrained input (how many FTEs are available and at what cost). This is a systematic planning gap: the framework answers "what does this cost if staffed?" but not "what happens if this cannot be staffed on the required timeline?"

---

## 6. Regulatory Variance Across Customers — Phase 2 and Phase 3

### 6.1 What the Framework Currently Captures

CP-09 (Compliance Automation) addresses per-customer regulatory mapping:

[FACT]
"Map ISV's compliance framework to customer's specific regulatory requirements (FedRAMP vs HIPAA vs SOC2 vs industry-specific). Evidence collection configured for customer's audit requirements."
— `analysis/three_phase_on_prem_ratings.md` §5, CP-09 Phase 2 Notes

[FACT]
"CP-09 | Compliance Automation | Phase 2: RD 3 / TE 3"
— `analysis/three_phase_on_prem_ratings.md` §5, P1 Control Plane Phase 2 table

[FACT]
"Compliance evidence regeneration per audit cycle per customer. Regulatory changes require re-assessment across customer base. SOC2 annual audits, FedRAMP continuous monitoring."
— `analysis/three_phase_on_prem_ratings.md` §6, CP-09 Phase 3 Notes

### 6.2 What the Framework Does Not Capture

The CP-09 ratings treat regulatory compliance as a configuration and evidence collection problem. They do not capture the depth of divergence between regulatory frameworks — specifically, the engineering consequences when two customers have mutually incompatible compliance requirements, or when a new regulation requires a material change to the ISV's software (not just its configuration or audit evidence).

[FACT]
"EU regulators issued €1.2 billion in fines in 2024 for GDPR violations."
— Encryption Consulting, "Compliance Trends of 2025"
URL: https://www.encryptionconsulting.com/compliance-trends-of-2025/

[FACT]
"HIPAA was amended in 2024 to address new challenges in healthcare data security, establishing security standards for telehealth platforms and reducing the breach notification period to 10 days while increasing penalties for non-compliance."
— Scrut.io, "How to master SaaS compliance in 2025"
URL: https://www.scrut.io/post/saas-compliance

[FACT]
"19 U.S. states enacted comprehensive privacy laws by 2025."
— Encryption Consulting, "Compliance Trends of 2025"
URL: https://www.encryptionconsulting.com/compliance-trends-of-2025/

Specific regulatory variance scenarios not captured in the CP-09 ratings:

**Scenario A — FedRAMP vs. GDPR conflict.** A US government customer (FedRAMP) requires all data to remain on US soil and forbids encryption key escrow to foreign parties. A European financial services customer (GDPR + DORA) requires the ISV to support data subject deletion requests within 30 days. These two requirements coexist in the same ISV product but may require different database configurations (data residency enforcement in the relational DB), different logging behaviors (audit log retention periods differ), and different key management configurations (FIPS vs. EU eIDAS). The CP-09 Phase 2 rating of RD 3 / TE 3 does not account for cases where two customers' compliance requirements require code-level changes to the ISV's product — not just configuration changes.

**Scenario B — CMMC Level 2 vs. HIPAA.** The Cybersecurity Maturity Model Certification (CMMC Level 2, mandatory for DoD suppliers by 2025) requires specific network segmentation, multi-factor authentication configurations, and controlled unclassified information (CUI) access controls. HIPAA requires different audit log formats, different ePHI access patterns, and different data encryption scope. An ISV serving both defense contractors and healthcare systems must maintain two distinct compliance posture configurations in its software — which may require feature flags, tenant-level configuration, or separate deployment variants.

**Scenario C — Emerging state-level AI regulations.** Colorado SB 22-205, Texas HB 4337, and analogous state AI bills impose transparency, explainability, and bias testing requirements that vary by state. An ISV serving enterprise customers in multiple US states with AI-powered features must track and implement per-customer compliance with an evolving patchwork of state laws — a Phase 3 ongoing maintenance burden not reflected in any current subsegment.

[FACT]
"SaaS providers dealing with overlapping regulations like FedRAMP, ISO 27001, SOC 2, and NIST 800-53 can use OSCAL to map security controls across different standards."
— Appinventiv, "Cloud Compliance Requirements: What You Need to Know"
URL: https://appinventiv.com/blog/cloud-regulatory-compliances-guide/

### 6.3 Gap Classification

The CP-09 Phase 2 and Phase 3 ratings treat compliance as a mapping and evidence collection problem at RD 3 / TE 3. The ratings do not account for the subset of customers whose regulatory requirements force code-level changes to the ISV's product — a qualitatively different and higher-effort scenario. The RP4c review (`analysis/review/RP4c_P4_completeness.md`) identified cost attribution as a gap; regulatory compliance for AI outputs (explainability, audit logging of model decisions) is an adjacent gap not covered there or in CP-09.

---

## 7. On-Premises Deployment Failure Mode Evidence

Published analyses of on-premises enterprise software deployment failures identify several risk patterns that are absent from or underweighted in the three-phase framework:

[FACT]
"Safe software deployment practices include variations such as 'blue/green' deployment models or splitting customers into 'Stable' and 'Early Access' groups, allowing them to match access to new features with their risk tolerance. Controlled rollout prevents sudden, widespread failures."
— CISA/IC3, "Safe Software Deployment: How Software Manufacturers Can Ensure Reliability for Customers" (October 24, 2024)
URL: https://www.ic3.gov/CSA/2024/241024.pdf

The CISA 2024 safe deployment guidance was triggered by incidents including the CrowdStrike Falcon sensor update (July 19, 2024) that caused 8.5 million Windows systems to blue screen globally. The guidance is directly applicable to ISVs distributing software to on-premises environments: a bad update pushed to N customer environments simultaneously could cause N simultaneous production outages, with the ISV responsible for coordinating recovery at each site.

[FACT]
"Organizations may consider whether the appropriate velocity of a deployment for urgent security fixes differs compared to more routine content deployments."
— CISA/IC3, "Safe Software Deployment" (October 24, 2024)
URL: https://www.ic3.gov/CSA/2024/241024.pdf

The current CP-07 Phase 3 rating (RD 5 / TE 5) rates the deployment coordination effort but does not capture the failure mode risk of simultaneous multi-customer outages caused by a bad ISV-distributed update. The blast radius of a defective release in on-premises deployments is bounded to each customer's environment (unlike cloud SaaS where the ISV can roll back centrally), but the recovery cost scales with N customers because each requires a separate rollback coordination sequence.

---

## 8. Gap Summary

| Gap Category | Framework Section(s) Affected | Severity | Evidence Type |
|---|---|:---:|---|
| Organizational change management (ISV team restructuring) | None — absent entirely | High | Structural reasoning + support model literature |
| Customer communication overhead (upgrade/incident coordination) | CP-07 Phase 3 (underweighted) | High | Enterprise incident management research |
| Vendor lock-in reversal cost (cloud API extraction) | AL05 Phase 1, S1 Phase 1 (underweighted) | Medium-High | Cloud migration cost data; API standardization literature |
| Supply chain security (SBOM, CVE velocity, artifact mirror) | CP-10 Phase 3 (underweighted) | High | Sonatype 2024; CISA 2024; SecurityWeek 2025 |
| Talent acquisition difficulty (on-premises specialists) | Phase 3 FTE tables (absent as constraint) | High | Spectro Cloud 2025; Linux Foundation 2024 |
| Regulatory variance across customers (code-level compliance divergence) | CP-09 Phase 2/3 (underweighted) | Medium-High | Multi-jurisdictional compliance literature |

---

## Key Findings

- **Organizational change management is entirely absent from the 38-subsegment framework.** The ratings answer "what does this work cost if the team is in place?" but not "what does it cost to build, restructure, and train the team that will execute this work?" A cloud-native SaaS ISV adding on-premises support requires a qualitatively different support organization — including field engineering, embedded deployment support, and per-customer environment documentation — that is not rated in any Phase 1, 2, or 3 subsegment. This is most likely the largest underweighted cost for an ISV making its first on-premises commitment.

- **Customer communication and upgrade coordination overhead is absorbed into CP-07's engineering FTE but is structurally different from engineering effort.** At 50 customers, N=50 coordination sequences per release means 50 scheduling calls, 50 change control submissions, and 50 post-deployment status reports per major release cycle. For regulated customers (FedRAMP, HIPAA), change management protocols may require formal submissions 5–10 business days before each deployment window. This coordination burden has no dedicated subsegment and no FTE allocation in the current framework.

- **Supply chain security for the self-hosted open source component stack is underweighted in CP-10.** With 40,000+ CVEs published in 2024 (38% YoY increase) and 23.6% of Known Exploited Vulnerabilities being exploited on or before public disclosure, an ISV distributing 40+ open source components must maintain SBOM documentation, CVE triage capacity, and emergency patching capability across N customer environments simultaneously. CP-10 notes "CVE response time pressure" but does not rate SBOM generation, artifact signing, or the emergency patch coordination protocol across N environments as distinct effort categories.

- **Talent acquisition difficulty for on-premises specialist roles represents an unmodeled execution constraint.** The Phase 3 P1 Control Plane estimate of 20–38 FTE assumes those FTEs can be recruited. The Spectro Cloud 2025 State of Production Kubernetes report (455 respondents, May 2025) finds that 40% of organizations lack the skills and headcount to manage Kubernetes, and the Linux Foundation 2024 State of Tech Talent report finds platform engineering roles take 5.4+ months to fill on average. The salary range for Kubernetes engineers ($140K–$200K+) creates a material cost assumption embedded in the FTE figures that is never made explicit. An ISV that cannot hire at the required pace faces a support capacity gap that is not captured by the ratings.

- **Regulatory variance across customers can force code-level ISV product changes that are not captured by CP-09's configuration-level framing.** Customers in FedRAMP, HIPAA, CMMC Level 2, GDPR, and state-level AI regulation regimes may have mutually divergent requirements for data residency, audit log formats, encryption configurations, and AI explainability. When two customers' requirements are irreconcilable in a single software configuration, the ISV must implement feature flags, tenant-level conditional logic, or separate deployment variants — a product engineering cost, not a compliance configuration cost. CP-09 Phase 2 (RD 3 / TE 3) does not capture this scenario.

---

## Sources

**Internal Source Files:**

| File | Path | Sections Used |
|---|---|---|
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` | §2 (phases), §4 (Phase 1), §5 (Phase 2), §6 (Phase 3), §8 (Key Findings) |
| RP4c_P4_completeness.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4c_P4_completeness.md` | Key Findings; Gap Table §7.1 |
| RP2e_P2_completeness.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2e_P2_completeness.md` | §3.3 (Notification gap); Key Findings |
| RP1a_P1_infrastructure_core.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1a_P1_infrastructure_core.md` | CP-01, CP-02, CP-03 all phases; Key Findings |

**External Sources:**

- [Sonatype — 2024 State of the Software Supply Chain: Scale of Open Source](https://www.sonatype.com/state-of-the-software-supply-chain/2024/scale)
- [Sonatype — 10th Annual State of the Software Supply Chain press release (156% malware surge)](https://www.globenewswire.com/news-release/2024/10/10/2961239/0/en/Sonatype-s-10th-Annual-State-of-the-Software-Supply-Chain-Report-Reveals-156-Surge-in-Open-Source-Malware.html)
- [SecurityWeek — Cyber Insights 2025: Open Source and the Software Supply Chain](https://www.securityweek.com/cyber-insights-2025-open-source-and-the-software-supply-chain/)
- [CISA — Safe Software Deployment: How Software Manufacturers Can Ensure Reliability for Customers (October 24, 2024)](https://www.ic3.gov/CSA/2024/241024.pdf)
- [CISA — SBOM: Software Bill of Materials](https://www.cisa.gov/sbom)
- [CISA — Securing the Software Supply Chain: Recommended Practices for SBOM Consumption (2024)](https://www.cisa.gov/sites/default/files/2024-08/SECURING_THE_SOFTWARE_SUPPLY_CHAIN_RECOMMENDED_PRACTICES_FOR_SOFTWARE_BILL_OF_MATERIALS_CONSUMPTION-508.pdf)
- [Spectro Cloud — 2025 State of Production Kubernetes Report](https://www.spectrocloud.com/state-of-kubernetes-2025)
- [Linux Foundation — The 2024 State of Tech Talent Report](https://www.linuxfoundation.org/blog/the-2024-state-of-tech-talent-report)
- [Bluelight — Kubernetes Engineer Salary Guide](https://bluelight.co/blog/kubernetes-salary-guide)
- [Squadcast — The Complete Enterprise Incident Management Playbook (2024)](https://medium.com/@squadcast/the-complete-enterprise-incident-management-playbook-a-comprehensive-guide-for-2024-cc0f843657b2)
- [TaskCall — Enterprise Incident Management](https://taskcallapp.com/blog/enterprise-incident-management)
- [Cloudflare — What is vendor lock-in?](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/)
- [CloudEagle — What Is Vendor Lock-In?](https://www.cloudeagle.ai/resources/glossaries/what-is-vendor-lock-in)
- [ScienceSoft — Cloud Migration Guide: Steps, Platforms, Costs in 2025](https://www.scnsoft.com/cloud/migration)
- [AWS Blogs — Accelerating SaaS Migration Success](https://aws.amazon.com/blogs/migration-and-modernization/accelerating-saas-migration-success-aws-programs-tools-and-expertise-that-drive-isv-growth/)
- [FullView.io — How to Structure a SaaS Customer Support Team](https://www.fullview.io/blog/how-to-structure-your-saas-support-team-as-your-company-grows)
- [Encryption Consulting — Compliance Trends of 2025](https://www.encryptionconsulting.com/compliance-trends-of-2025/)
- [Scrut.io — How to master SaaS compliance in 2025](https://www.scrut.io/post/saas-compliance)
- [Appinventiv — Cloud Compliance Requirements: What You Need to Know](https://appinventiv.com/blog/cloud-regulatory-compliances-guide/)
- [Andela — Talent Shortages Shouldn't Kill Your Cloud Native Journey](https://enterprise.andela.com/blog-posts/talent-shortages-shouldnt-kill-your-cloud-native-journey)
