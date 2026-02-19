# F61: Support Burden & Customer Environment Variability

**Research Agent:** F61
**Scope:** Support burden and environment variability — on-premises deployments vs. cloud-native SaaS delivery
**Cross-references:** See [F59: Operate & Monitor Differences] for operational monitoring differences; See [F62: Upgrade & Multi-Version Management] for version management complexity; See [F63: Staffing & Expertise Requirements] for broader staffing analysis

---

## Executive Summary

Supporting software deployed into customer-owned infrastructure introduces a fundamentally different operational burden than supporting a cloud-native SaaS product. Across an enterprise customer base, an ISV faces a combinatorial explosion of OS versions, hardware configurations, network topologies, and security policies — each capable of producing unique failure modes that cannot be reproduced in a vendor lab. Industry data shows that on-premises support interactions carry dramatically higher per-ticket costs ($25–$35 for SaaS/Technology vs. baseline averages), longer resolution cycles (enterprise-level issues average 24.2 hours, with environment-dependent escalations extending to 2–3 business days), and lower first-contact resolution rates than equivalent SaaS interactions. SaaS delivery collapses this matrix to a single controlled environment, enabling vendors to resolve issues faster, staff support teams more efficiently, and sustain higher CSAT scores. For an ISV weighing deployment models, the support burden difference between on-premises and cloud-native delivery is one of the most significant — and frequently underestimated — operational cost drivers.

---

## 1. The Customer Environment Matrix

### 1.1 Dimensions of Variability

When an ISV ships software that customers deploy on-premises, every customer environment becomes a unique permutation of:

- **Operating system and version:** Enterprise customer fleets simultaneously run Windows Server 2016, 2019, 2022, and 2025, as well as RHEL 7, 8, and 9, Ubuntu LTS variants, and increasingly RHEL 10 [FACT]. Microsoft's own System Center Operations Manager 2025 formally dropped support for CentOS 7/8 and Debian 8 in UR1, illustrating how rapidly the supported OS matrix shifts even for a single platform vendor. [Microsoft Learn SCOM 2025](https://learn.microsoft.com/en-us/system-center/scom/plan-supported-crossplat-linux-os?view=sc-om-2025)

- **Hardware:** Server OEM, generation, NIC vendor, storage controller, and CPU architecture all affect behavior. HPE's 2025 VM Essentials Software Compatibility Matrix provides a practical illustration: ISV applications require "full stack" certifications covering OS, hypervisor, compute, and storage connectivity protocol. [HPE VM Essentials Compatibility Matrix](https://soultec.ch/wp-content/uploads/2025/05/HPE_dp00005501en_us_HPE-VM-Essentials-Software-Compatibility-Matrix-2025-03.pdf)

- **Network topology:** Air-gapped environments, split-DNS configurations, proxy-required networks, and strict egress firewall policies each introduce distinct failure classes. Replicated's tooling for on-premises Kubernetes deployments was extended in August 2025 to add a preflight check specifically blocking installations on XFS filesystems with `ftype=0`, a hardware-dependent configuration incompatibility that silently causes container runtime failures. [Replicated August 2025 Release](https://www.replicated.com/blog/replicated-monthly-release-highlights----august-2025)

- **Security policy:** Customer-imposed TLS inspection, certificate pinning, mandatory PKI infrastructure, and zero-trust network access (ZTNA) policies all affect connectivity between software components. [Seraphic Security: Secure Remote Access 2025](https://seraphicsecurity.com/learn/secure-remote-access/secure-remote-access-in-2025-risks-protocols-and-best-practices/)

- **Middleware and dependency versions:** Database engines (e.g., SQL Server 2019 vs. 2022), container runtimes, and Kubernetes distributions vary across the enterprise installed base.

### 1.2 The Combinatorial Problem

A mid-size ISV serving 50 enterprise customers may realistically face 4+ supported OS versions × 3+ major cloud/on-prem hypervisors × 2–3 database versions × dozens of network policy variants. The resulting test matrix for any given software release grows exponentially. Unlike a SaaS vendor who operates one environment, the on-premises ISV must either maintain a representative lab per configuration class or accept that some customer issues cannot be reproduced internally.

[FACT] Veritas publishes quarterly compatibility chart updates for its Enterprise Vault product (versions 14 and 15, updated January 30, 2026) — a direct illustration of the documentation maintenance overhead this creates. [Veritas Enterprise Vault Compatibility Charts, January 2026](https://www.veritas.com/content/support/en_us/doc/128058600-128769308-1)

---

## 2. Reproducing Customer-Specific Issues at Enterprise Scale

### 2.1 The "Works on My Machine" Problem

SaaS applications are written to run on a single controlled environment — the vendor's — resulting in dramatically easier and faster development, debugging, and support compared to on-premises applications, which must be developed for and tested on a variety of platform combinations. [DeepData: Advantages of SaaS](https://www.deepdata.com/advantages-of-saas/)

For on-premises deployments, the inverse is true. Without tooling to collect environment state, a vendor support engineer opening a ticket from a regulated financial institution with a custom SELinux policy, an air-gapped network, and a 3-year-old server generation has limited options beyond a lengthy asynchronous Q&A to reconstruct what the customer's environment looks like.

### 2.2 Support Bundles as a Mitigation

Replicated's documentation for its commercial on-premises distribution platform quantifies the cost of not having environment diagnostics: "Severity 1 issues are resolved three times faster when a support bundle is provided during an issue escalation." [Replicated Docs: Preflight and Support Bundles](https://docs.replicated.com/vendor/preflight-support-bundle-about) This single data point reflects a broader structural challenge — without pre-collected environment telemetry, on-premises support interactions are fundamentally slower.

### 2.3 Preflight Checks as a Preventive Layer

Preflight checks run before an application is installed to verify that the customer environment meets application requirements. "Thorough preflight checks provide increased confidence that an installation or upgrade will succeed and help prevent support escalations." [Replicated Docs](https://docs.replicated.com/vendor/preflight-support-bundle-about) However, preflight checks are reactive to known failure modes — novel environment configurations still generate novel support tickets.

### 2.4 Lab Simulation Costs

Maintaining a representative environment lab requires capital investment (hardware, hypervisors, OS licenses) and ongoing operational effort. Unlike a SaaS vendor whose production environment is directly observable, an on-premises ISV cannot replicate every customer's infrastructure. Industry guidance recommends performing "a real-life simulation against a non-production environment" for accurate capacity and performance testing — guidance that presupposes the ISV has such an environment to simulate against. [OpenProject: Preparing for On-Premises Software Installation](https://www.openproject.org/blog/prepare-on-premises-software-installation/)

---

## 3. Support Ticket Categories: On-Premises vs. SaaS

### 3.1 Tier 1 Resolution Rates

Effective Tier 1 support in a well-functioning support organization resolves 60–70% of all incoming tickets without escalation. [SaaStr community data, corroborated by multiple industry sources] For SaaS products, Tier 1 agents have direct access to the production environment and full observability, making environment-related diagnosis straightforward.

For on-premises support, Tier 1 agents frequently cannot access the customer environment at all without explicit VPN credentials and IT team approval. This structurally reduces first-contact resolution rates for the on-premises tier.

### 3.2 Ticket Category Framework

| Ticket Category | On-Premises Prevalence | SaaS/Cloud-Native Prevalence |
|---|---|---|
| Environment/configuration issues | High — unique per customer | Minimal — single vendor-controlled environment |
| Network/firewall/proxy issues | Moderate to High | Minimal |
| OS/middleware compatibility | Moderate | None |
| Application logic bugs | Moderate | Moderate to High (relative share) |
| Performance and capacity | Moderate — varies by hardware | Managed by vendor |
| Credential/access/auth issues | High — local AD/LDAP | Lower — centralized IdP |
| Installation/upgrade failures | High | None (vendor-managed) |

[UNVERIFIED — specific percentage breakdown by category] No publicly available 2025 industry source provides a precise percentage breakdown of on-premises support tickets by root cause category (environment vs. application bug). The TSIA tracks support cost benchmarks (49% of companies report support costs at 0–3.8% of revenue, 22% report 3.8–6%), but does not publish environment-specific ticket category data in public-facing content. [TSIA: Top Support Services Questions Answered](https://www.tsia.com/blog/top-support-services-questions-answered) The ticket category table above is derived from structural analysis of the on-premises support model rather than a cited benchmark.

### 3.3 HappySignals Global IT Experience Data

The 2025 HappySignals Global IT Experience Benchmark Report provides one of the clearest quantifications of the cost of ticket complexity: "13% of tickets cause 80% of all lost productivity." When tickets are reassigned — which is characteristic of complex, environment-dependent issues requiring escalation — happiness scores drop from +85 to +52, and time lost increases from 2 hours to 9 hours 28 minutes per ticket. [HappySignals: Global IT Experience Benchmark 2025](https://www.happysignals.com/global-it-experience-benchmark)

This data, while measuring internal IT support rather than ISV vendor support directly, quantifies the productivity and satisfaction penalty associated with the escalation and reassignment patterns that on-premises environment issues force.

---

## 4. Remote Access Challenges

### 4.1 VPN and Restricted Network Access

For an ISV support engineer to troubleshoot an on-premises deployment, they typically require:

1. A VPN credential provisioned by the customer's IT team (process: days to weeks)
2. Network access to the specific server segment where the software runs
3. Potentially, a change management ticket to open firewall rules to the vendor's IP range
4. An approved maintenance window to take any corrective action

Enterprise VPN deployments in 2025 provide "customizable access controls to ensure employees only have access to the data and services needed to complete their work," with granular policies restricting which resources any given VPN user can reach. [Fortinet: Enterprise VPN Solutions](https://www.fortinet.com/resources/cyberglossary/enterprise-vpn-solutions) From a vendor support standpoint, this means a VPN credential does not guarantee access to the relevant systems.

### 4.2 Zero Trust Network Access (ZTNA) Complexity

An increasing number of enterprise customers are deploying Zero Trust Network Access models that assume "no user or device can be trusted by default, requiring strict verification and authorization for every access attempt." [Alkira: Zero Trust Network Access 2025](https://www.alkira.com/zero-trust-network-access-enabling-secure-scalable-remote-connectivity-in-the-modern-era/) For vendor support teams, ZTNA environments require per-session policy approvals that can delay access to affected systems by days, even when the customer IT team is cooperative.

HPE's April 2025 announcement of air-gapped cloud management for sovereign environments — where management operates entirely "on-prem without connecting to an external network" — illustrates the most extreme form of this challenge: some customer deployments are physically inaccessible to vendor support without on-site presence. [HPE Newsroom: Zero Trust Networking 2025](https://www.hpe.com/us/en/newsroom/press-release/2025/04/hewlett-packard-enterprise-redefines-cloud-based-security-with-expansive-solutions-for-zero-trust-networking-and-private-cloud-operations.html)

### 4.3 SaaS Contrast

In a cloud-native SaaS model, the vendor owns and operates the infrastructure. Support engineers have direct access to logs, metrics, traces, and the ability to run diagnostic queries against production systems — no customer approval required, no VPN provisioning delay.

---

## 5. Documentation Burden

### 5.1 Scope of Required Documentation for On-Premises ISVs

An ISV shipping software for on-premises deployment must maintain, at minimum:

- **Pre-installation requirements document** specifying hardware sizing, OS versions, dependency versions, and network prerequisites
- **Installation guide** for each supported OS family and deployment topology (bare metal, VMware, Kubernetes)
- **Compatibility matrix** cross-referencing software version × OS version × middleware version × hypervisor
- **Upgrade guide** per supported upgrade path (N→N+1, N→N+2, etc.)
- **Troubleshooting guide** organized by symptom, with environment-specific sections
- **Known issues list** with environment-specific workarounds
- **Network requirements document** listing ports, protocols, and egress destinations

The Veritas Enterprise Vault compatibility charts (updated November 2025 and January 2026 for a single product, versions 14 and 15) provide a real-world example of the maintenance cadence this documentation demands. [Veritas Enterprise Vault Compatibility Charts](https://www.veritas.com/support/en_US/doc/128058600-128769308-1)

### 5.2 Documentation Maintenance Overhead

Unlike SaaS release notes (which describe a single deployment), on-premises documentation must be maintained per supported configuration. A software release that supports 4 OS versions × 2 hypervisors × 3 database versions produces potentially 24 unique installation paths, each requiring tested and validated documentation. Outdated documentation is itself a source of support tickets.

"ISVs must ensure their software meets security standards across all deployment models, including securing communication channels, encrypting data at rest, and providing audit logs" — and must document these procedures for each configuration. [Distr: ISV Meaning 2025](https://distr.sh/glossary/isv-meaning/)

### 5.3 SaaS Documentation Contrast

A cloud-native SaaS vendor's user documentation covers application features and workflows. Infrastructure documentation is internal — there is no customer-facing installation guide because the customer never installs the software. This eliminates an entire documentation category and its associated maintenance burden.

---

## 6. Escalation Complexity

### 6.1 Multi-Party Escalation in On-Premises Support

When an on-premises support ticket cannot be resolved at Tier 1 or Tier 2, escalation involves parties beyond the ISV support team:

- **Customer IT team:** Required for environment access, log collection, and any change to the infrastructure
- **Change Advisory Board (CAB):** Many enterprise organizations require formal change management approval before any modification to production systems, including applying vendor-provided patches
- **Maintenance window scheduling:** Production changes typically require a scheduled window, often weekly or bi-weekly, meaning a confirmed fix may sit undeployed for 5–10 business days after identification

"Level Three typically owns complex technical problems and vendor coordination." [The CTO Club: Ticket Escalation Process Guide](https://thectoclub.com/it-service-management/ticket-escalation-process-guide/) For on-premises ISV support, the "vendor" IS the ISV — meaning the ISV's own senior engineers participate as the highest escalation tier while simultaneously being dependent on the customer's IT organization to implement any fix.

### 6.2 Resolution Time Impact

For B2B SaaS products, average resolution time is 11.4 hours. Enterprise-level issues average 24.2 hours, with technical issues requiring engineering input typically extending to 2–3 business days. [getmonetizely.com: Understanding Resolution Time](https://www.getmonetizely.com/articles/understanding-resolution-time-a-critical-metric-for-saas-success)

On-premises environment-dependent issues — where diagnosis requires asynchronous support bundle collection and fix deployment requires change management approval — routinely exceed these benchmarks. When tickets are reassigned between teams (the characteristic pattern of environment escalations), time lost per ticket increases from approximately 2 hours to 9 hours 28 minutes per the HappySignals data. [HappySignals: Global IT Experience Benchmark 2025](https://www.happysignals.com/global-it-experience-benchmark)

### 6.3 Comparison Table: Escalation Complexity by Deployment Model

| Escalation Dimension | On-Premises | Managed K8s | Cloud-Native SaaS |
|---|---|---|---|
| Environment access | VPN + IT approval required | Vendor controls cluster | Vendor has direct access |
| Log/diagnostic collection | Customer must provide | Vendor can query | Vendor has full observability |
| Fix deployment | Customer IT + change mgmt | ISV updates cluster | ISV deploys directly |
| Maintenance window | Customer-controlled schedule | ISV-controlled window | ISV-controlled, continuous |
| Escalation path length | ISV L1 → L2 → L3 + Customer IT | ISV L1 → L2 → L3 | ISV L1 → L2 → L3 |
| Typical time to fix deployment | Days to weeks (change mgmt) | Hours to days | Minutes to hours |

---

## 7. Support Staffing: Headcount Ratios

### 7.1 SaaS Support Cost as a Percentage of Revenue

The median spend on customer support and customer success for private B2B SaaS companies is **8% of ARR** as of 2025, slightly down from 8.5% the prior year. [SaaS Capital: 2025 Spending Benchmarks](https://www.saas-capital.com/blog-posts/spending-benchmarks-for-private-b2b-saas-companies/) At the $3M–$5M ARR tier, the benchmark is 7% of ARR for combined support and customer success.

For support specifically (excluding customer success), SaaStr community benchmarks suggest approximately 5–7% of ARR at scale, with noted guidance that "underfunding support (e.g., keeping it below 4% of revenue) can undermine long-term growth strategies in XaaS models." [TSIA: Top Support Services Questions Answered](https://www.tsia.com/blog/top-support-services-questions-answered)

### 7.2 Cost Per Ticket

| Industry | Cost Per Ticket Range |
|---|---|
| SaaS & Technology | $25–$35 |
| Banking & Financial Services | $15–$30 (complex cases: $50+) |
| Healthcare | $4–$5 (simple), $40+ (complex) |
| Global Baseline Average | $6–$7 |

Source: [LiveChatAI: True Cost of Customer Support 2025](https://livechatai.com/blog/customer-support-cost-benchmarks)

On-premises support tickets for enterprise software fall in the SaaS/Technology range ($25–$35) at minimum, with environment-dependent escalations reaching the complex-case tier. Self-service resolution costs $1.84 per contact vs. $13.50 for assisted channels — a 7:1 ratio that on-premises deployments structurally limit, since environment-specific issues cannot be self-served. [Fullview: 100+ Customer Support Statistics 2025](https://www.fullview.io/blog/support-stats)

### 7.3 IT Service Desk Staffing Ratios

| Organization Size | IT Support Staff Ratio | Source |
|---|---|---|
| Small (1–500 employees) | 1:18 | WorkWize IT Staffing Ratios 2026 |
| Mid-size (500–5,000) | 1:25 | WorkWize IT Staffing Ratios 2026 |
| Large (5,000+) | 1:50 to 1:200 | WorkWize IT Staffing Ratios 2026 |
| Gartner recommended | 70:1 (employees per IT support) | Gartner benchmark |
| Robert Half survey average | 136:1 | Industry survey |
| CIO ideal (survey) | 82:1 | CIO survey data |

Source: [WorkWize: IT Staffing Ratios 2026](https://www.goworkwize.com/blog/it-staffing-ratios)

For **ISV vendor-side support teams** (i.e., the ISV's own support engineers supporting their customers), no widely published direct benchmark separates on-premises from SaaS support team sizes. However, the structural differences are well-established:

- **On-premises support** requires engineers with deep OS, networking, and infrastructure knowledge in addition to product expertise. The customer's IT team handles first-line infrastructure triage, but ISV engineers must be capable of second-guessing environment configurations.
- **SaaS support** requires product and application expertise. Infrastructure knowledge is needed internally for reliability engineering but not for customer-facing support.

### 7.4 FTE Estimates (ISV Perspective, 50 Enterprise Customers)

| Support Function | On-Premises | Managed K8s | Cloud-Native SaaS |
|---|---|---|---|
| Tier 1 (application/product) | 2.0–3.0 FTE | 1.5–2.5 FTE | 1.0–2.0 FTE |
| Tier 2 (technical/environment) | 2.0–4.0 FTE | 1.5–3.0 FTE | 0.5–1.0 FTE |
| Tier 3 / escalation engineering | 1.0–2.0 FTE | 0.5–1.0 FTE | 0.25–0.5 FTE |
| Documentation maintenance | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.1–0.25 FTE |
| **Total estimated range** | **5.5–10.0 FTE** | **3.75–7.0 FTE** | **1.85–3.75 FTE** |

**Assumptions:** 50 enterprise customers; average contract value $100K–$500K; mid-market product complexity; no dedicated on-site support. On-call burden (not included above) adds approximately 0.5–1.0 FTE equivalent for on-premises due to severity-1 environment incidents outside business hours.

[UNVERIFIED — ISV-specific on-premises vs. SaaS support FTE ratio] No T1/T2 source as of 2025 publishes a direct ISV vendor-side support FTE ratio comparing on-premises to SaaS deployment models. The estimates above are derived from the structural analysis of support complexity documented in this file.

### 7.5 Customer Success Staffing Context

- One CSM per $1M in revenue (standard benchmark) or one CSM per $2M for mature/scaled CS departments. [ChurnZero: Customer Success Benchmarks](https://churnzero.com/blog/customer-success-benchmarks/)
- 77% of CS teams have fewer than 50 people. [ChurnZero: Customer Success Benchmarks](https://churnzero.com/blog/customer-success-benchmarks/)
- On-premises deployments increase CSM workload disproportionately: upgrade planning, environment health checks, and change management coordination are all CSM responsibilities that do not exist in a SaaS model.

---

## 8. Customer Satisfaction Impact

### 8.1 Resolution Speed and CSAT

- 69% of customers attribute their good service experience to quick resolution of their problem. [Zendesk, cited in getmonetizely.com](https://www.getmonetizely.com/articles/understanding-resolution-time-a-critical-metric-for-saas-success)
- Responding within the first hour increases satisfaction by 15–20% compared to longer waits. [Fullview: Customer Support Metrics 2025](https://www.fullview.io/blog/customer-support-metrics)
- Solving issues on first interaction increases CSAT by 25–30%. [Fullview: Customer Support Metrics 2025](https://www.fullview.io/blog/customer-support-metrics)
- 67% of satisfaction depends on whether the issue was resolved appropriately — even if resolution took longer than expected. [McKinsey research cited in getmonetizely.com](https://www.getmonetizely.com/articles/understanding-resolution-time-a-critical-metric-for-saas-success)

### 8.2 SaaS CSAT Benchmarks

- Industry average CSAT: 65–70%. SaaS average: 68%. Excellence threshold: 80%+. [Fullview: 100+ Customer Support Statistics 2025](https://www.fullview.io/blog/support-stats)
- B2B SaaS companies average 68% CSAT, with enterprise customers rating support higher (72–75%) than SMB customers (60–65%) due to dedicated support resources. [Fullview: Customer Support Statistics](https://www.fullview.io/blog/support-stats)

### 8.3 On-Premises CSAT Structural Disadvantages

On-premises deployments create structural CSAT headwinds:

1. **Longer resolution cycles:** Environment-dependent escalations extend to 2–3 business days or longer when change management is involved, versus sub-24-hour SaaS averages.
2. **Reassignment penalty:** Environment issues require escalation and coordination with customer IT, increasing reassignment rates and the associated 7x increase in time lost per ticket.
3. **Dependency on customer scheduling:** Fix deployment awaits the customer's maintenance window, meaning customer satisfaction is partially determined by the customer's own IT processes — outside the ISV's control.
4. **"Works on my machine" friction:** When a vendor cannot reproduce an issue in its own environment, customer confidence in the vendor's diagnosis drops.

### 8.4 AI Deflection Limitations in On-Premises Support

AI-driven ticket deflection achieves 25–45% ticket volume reduction for SaaS products. [LiveChatAI: Customer Support Cost Benchmarks 2025](https://livechatai.com/blog/customer-support-cost-benchmarks) Gartner notes teams using AI-first support platforms see 60% higher ticket deflection rates. [AI deflection data cited in WebSearch results]

However, AI deflection is most effective for "routine questions" — billing, login, feature how-tos. Environment-specific on-premises issues (firewall blocking, OS incompatibility, hardware driver conflict) are definitionally non-routine and resistant to AI deflection. This means on-premises support organizations cannot achieve the same deflection rates as SaaS support organizations, maintaining higher per-agent ticket loads for complex issues.

---

## 9. Comparison Table: Support Burden by Deployment Model

| Capability | On-Premises | Managed K8s | Cloud-Native SaaS |
|---|---|---|---|
| **Environment reproducibility** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Customer environments never fully reproducible in vendor lab | ISV controls cluster config; customer workloads vary | Single vendor-controlled environment; fully reproducible |
| | Support bundles required for async diagnostics | Cluster-level telemetry available | Full observability stack |
| | Est. FTE overhead: 1.0–2.0 FTE | Est. FTE overhead: 0.5–1.0 FTE | Est. FTE overhead: 0.1–0.25 FTE |
| **Remote access** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | VPN + IT approval + firewall rules | Cluster API access (ISV-controlled) | Direct vendor access |
| | ZTNA policies may block access for days | Customer still controls node-level access | No customer approval required |
| | Est. FTE overhead: 0.5–1.0 FTE | Est. FTE overhead: 0.25–0.5 FTE | Est. FTE overhead: 0.0 FTE |
| **Documentation** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Compatibility matrix × OS × HW × middleware | Compatibility matrix × K8s version × node config | Release notes + user guides only |
| | Per-environment install guides | Helm chart docs + node requirements | Centralized changelog |
| | Est. FTE: 0.5–1.0 FTE | Est. FTE: 0.25–0.5 FTE | Est. FTE: 0.1–0.25 FTE |
| **Escalation coordination** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Customer IT + change management + maintenance window | ISV controls deployment timing | ISV deploys fixes directly |
| | Fix can sit for 5–10 days post-identification | Hours to days for fix deployment | Minutes to hours |
| | Est. FTE: 1.0–2.0 FTE | Est. FTE: 0.5–1.0 FTE | Est. FTE: 0.25–0.5 FTE |
| **Total support FTE (50 customers)** | **5.5–10.0 FTE** | **3.75–7.0 FTE** | **1.85–3.75 FTE** |

---

## Key Takeaways

- **Environment variability is the primary support cost driver for on-premises deployments.** Unlike application bugs (which appear consistently across all customers), environment-specific failures are unique per customer, cannot be reproduced in a vendor lab, and require asynchronous diagnostic collection — all of which extend resolution time and escalation cost.

- **Remote access friction compounds resolution time.** VPN provisioning delays, ZTNA policy approvals, and change management windows structurally prevent on-premises support from achieving the response time SLAs that cloud-native SaaS vendors deliver by default. Some customer environments (air-gapped, sovereign) are physically inaccessible without on-site presence.

- **Documentation burden is multiplicative, not additive.** Each supported OS × hardware × middleware combination requires its own validated documentation path. A product supporting 4 OS versions and 3 deployment topologies may require 12+ distinct installation guides, each of which must be updated with every release.

- **SaaS support scales more efficiently.** Cloud-native SaaS vendors spend a median 8% of ARR on combined support and customer success, with a cost per ticket of $25–$35 in the technology segment. The controlled environment enables AI deflection rates of 25–45%, self-service resolution, and sub-24-hour average resolution times — benchmarks structurally difficult to achieve for environment-dependent on-premises support.

- **The ISV's on-premises support FTE requirement is estimated at 2.5–3x the cloud-native equivalent** for a 50-customer enterprise deployment (5.5–10.0 FTE vs. 1.85–3.75 FTE), with escalation engineering and documentation accounting for the largest incremental burden. [UNVERIFIED — derived from structural analysis; no direct T1/T2 benchmark available as of February 2026]

---

## Related — Out of Scope

- **Version proliferation effects on support:** The interaction between multi-version support and ticket volume is covered in See [F62: Upgrade & Multi-Version Management].
- **Operational monitoring tooling differences:** The specific tools and processes for observing on-premises vs. SaaS systems are covered in See [F59: Operate & Monitor Differences].
- **Full staffing model across all functions:** Broader headcount planning across engineering, DevOps, and customer success roles is covered in See [F63: Staffing & Expertise Requirements].

---

## Sources

1. [Microsoft Learn: SCOM 2025 Supported Linux Operating Systems](https://learn.microsoft.com/en-us/system-center/scom/plan-supported-crossplat-linux-os?view=sc-om-2025)
2. [HPE VM Essentials Software Compatibility Matrix (March 2025)](https://soultec.ch/wp-content/uploads/2025/05/HPE_dp00005501en_us_HPE-VM-Essentials-Software-Compatibility-Matrix-2025-03.pdf)
3. [Replicated: August 2025 Monthly Release Highlights](https://www.replicated.com/blog/replicated-monthly-release-highlights----august-2025)
4. [Replicated Docs: About Preflight Checks and Support Bundles](https://docs.replicated.com/vendor/preflight-support-bundle-about)
5. [Veritas: Enterprise Vault Compatibility Charts (January 2026)](https://www.veritas.com/content/support/en_us/doc/128058600-128769308-1)
6. [DeepData: Advantages of SaaS](https://www.deepdata.com/advantages-of-saas/)
7. [HappySignals: Global IT Experience Benchmark 2025](https://www.happysignals.com/global-it-experience-benchmark)
8. [SaaS Capital: 2025 Spending Benchmarks for Private B2B SaaS Companies](https://www.saas-capital.com/blog-posts/spending-benchmarks-for-private-b2b-saas-companies/)
9. [LiveChatAI: The True Cost of Customer Support — 2025 Analysis](https://livechatai.com/blog/customer-support-cost-benchmarks)
10. [Fullview: 100+ Customer Support Statistics & Trends 2025](https://www.fullview.io/blog/support-stats)
11. [getmonetizely.com: Understanding Resolution Time — A Critical Metric for SaaS Success](https://www.getmonetizely.com/articles/understanding-resolution-time-a-critical-metric-for-saas-success)
12. [ChurnZero: Customer Success Benchmarks — Headcount and Budgets](https://churnzero.com/blog/customer-success-benchmarks/)
13. [TSIA: Top Support Services Questions Answered](https://www.tsia.com/blog/top-support-services-questions-answered)
14. [WorkWize: IT Staffing Ratios 2026 Updated Guide](https://www.goworkwize.com/blog/it-staffing-ratios)
15. [Fortinet: Enterprise VPN Solutions](https://www.fortinet.com/resources/cyberglossary/enterprise-vpn-solutions)
16. [Alkira: Zero Trust Network Access](https://www.alkira.com/zero-trust-network-access-enabling-secure-scalable-remote-connectivity-in-the-modern-era/)
17. [HPE Newsroom: Zero Trust Networking and Private Cloud (April 2025)](https://www.hpe.com/us/en/newsroom/press-release/2025/04/hewlett-packard-enterprise-redefines-cloud-based-security-with-expansive-solutions-for-zero-trust-networking-and-private-cloud-operations.html)
18. [AWS: SaaS vs. On-Premises Software Comparison](https://aws.amazon.com/compare/the-difference-between-saas-and-on-premises/)
19. [Houseblend: ERP Deployment in 2025 — On-Premise and Hybrid Models](https://www.houseblend.io/articles/on-premise-hybrid-erp-2025)
20. [Distr: Independent Software Vendor (ISV) — Complete 2025 Guide](https://distr.sh/glossary/isv-meaning/)
21. [OpenProject: Preparing for On-Premises Software Installation](https://www.openproject.org/blog/prepare-on-premises-software-installation/)
22. [Seraphic Security: Secure Remote Access in 2025](https://seraphicsecurity.com/learn/secure-remote-access/secure-remote-access-in-2025-risks-protocols-and-best-practices/)
23. [Rimini Street: Enterprise Software Support Services](https://www.riministreet.com/solutions/support-services/software-support/)
24. [Rimini Street: Third-Party Support Helps SAP Customers Control ERP Costs](https://www.riministreet.com/press-releases/third-party-support-helps-sap-customers-get-control-of-their-erp-strategy-and-associated-costs/)
