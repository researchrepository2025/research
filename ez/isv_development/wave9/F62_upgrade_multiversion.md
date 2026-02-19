# F62: Upgrade & Multi-Version Management

**Research Question:** How do ISVs manage multi-version support, coordinated upgrades, and backward compatibility when delivering on-premises software, and what operational overhead does this create?

---

## Executive Summary

On-premises software delivery forces ISVs into a version proliferation trap: enterprise customers running heavily customized installations resist upgrades for years, compelling vendors to simultaneously maintain, test, and ship security fixes across three to five or more active major releases. The canonical example is SAP ECC, where only 39% of 35,000 customers had migrated to S/4HANA by end of 2024, leaving a majority on legacy software that SAP must continue supporting despite a published end-of-maintenance timeline. This version fragmentation creates compounding costs: every additional supported version multiplies the QA matrix, expands the set of required data migration paths, forces backward compatibility maintenance across API, schema, and configuration layers, and demands specialized support staff who understand each older release. In contrast, a SaaS ISV operates a single-version codebase and can deploy improvements multiple times per day, eliminating the version management overhead entirely. The operational and engineering tax imposed by on-premises multi-version support is one of the strongest structural arguments for SaaS or managed cloud delivery models.

---

## 1. Version Proliferation: How Many Concurrent Versions Must an ISV Support?

Enterprise software vendors routinely operate under active support obligations for three to five major release families simultaneously. The range widens when extended support and contractual commitments are included.

### 1.1 Oracle Database

Oracle currently maintains active support across multiple concurrent major versions under a tiered lifecycle model:

[FACT]
Oracle Database 19c (Long Term Support) has Premier Support extended through December 31, 2029, and Extended Support through December 31, 2032 — described as "probably the longest-ever strategic platform" by Martin Biggs, VP at Spinnaker.
URL: https://www.theregister.com/2025/02/18/oracle_extends_19c_support/
Date: February 18, 2025

[STATISTIC]
Oracle Database 19c "is still the primary LTDS (Long-Term Distributed Support) release powering ~70% of enterprise OLTP workloads" as of 2025.
URL: https://red9.com/blog/oracle-19c-23c-overview-2025/
Date: 2025

[FACT]
Oracle supports concurrent patch releases for 19c, 21c, 23ai, and 26ai simultaneously. The October 2025 patch release cycle addressed all four active release lines in a single maintenance window.
URL: https://www.oracledbaonlinetraining.com/post/october-2025-oracle-ru-patch-numbers-every-dba-must-know-19c-21c-23ai-26ai
Date: October 2025

[FACT]
Oracle Database 21c is an Innovation Release with "at least 2 years of Premier Support and there will be no Extended Support or exceptions."
URL: https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html
Date: 2025

[FACT]
Oracle extended 19c support by five additional years beyond originally announced dates. Oracle provided no public explanation for this extension.
URL: https://www.theregister.com/2025/02/18/oracle_extends_19c_support/
Date: February 18, 2025

### 1.2 SAP S/4HANA and ECC

SAP presents the most extensively documented case of version proliferation driven by customer upgrade resistance in the enterprise software industry.

[STATISTIC]
At end of 2024, only 39% (approximately 14,000) of 35,000 SAP ECC customers had migrated to S/4HANA.
URL: https://www.cio.com/article/4000543/nearly-half-of-sap-ecc-customers-may-stick-with-legacy-erp-beyond-2027.html
Date: 2025

[STATISTIC]
Gartner projects 17,000 SAP ECC customers (nearly 50% of the base) will remain on the legacy system by 2027. More than 13,000 customers (over one-third) are expected to remain with legacy ERP through 2030.
URL: https://www.pillsburylaw.com/en/news-and-insights/software-sunsetting-contractual-postcontractual-best-practices.html
Date: 2025

[STATISTIC]
IDC expects 40-45% of SAP ECC users to continue using the older ERP through 2027. Forrester projects over 40% will still be on legacy ECC beyond 2027.
URL: https://www.cio.com/article/4000543/nearly-half-of-sap-ecc-customers-may-stick-with-legacy-erp-beyond-2027.html
Date: 2025

[STATISTIC]
As of Q4 2024, 61% of ECC customers had not purchased licenses for S/4HANA according to Gartner research.
URL: https://www.riministreet.com/blog/thanks-but-no-thanks-sap-customers-dont-see-the-value/
Date: 2025

[FACT]
SAP S/4HANA operates a two-year release cycle with a seven-year mainstream maintenance period per release. Individual on-premises releases have staggered end dates: S/4HANA 2020 mainstream maintenance ends 2025, 2021 ends 2026, 2022 ends 2027, 2023 extends through December 2030.
URL: https://news.sap.com/2022/09/new-sap-s4hana-release-maintenance-strategy/
Date: 2022

[FACT]
SAP committed to providing maintenance for the S/4HANA platform until end of 2040, ensuring at least one release is always in mainstream maintenance.
URL: https://support.sap.com/en/release-upgrade-maintenance/maintenance-information/maintenance-strategy/s4hana-business-suite7.html
Date: 2025

### 1.3 VMware vSphere

[FACT]
VMware offers 7 years of support for every new major release: 5 years of General Support followed by 2 years of Technical Guidance.
URL: https://blogs.vmware.com/cloud-foundation/2025/03/31/reminder-vsphere-7-to-reach-end-of-service-october-2-2025/
Date: March 31, 2025

[FACT]
VMware vSphere 7.x reached End of General Support on October 2, 2025, with Broadcom having extended this deadline by six months from the original April 2025 date.
URL: https://blogs.vmware.com/cloud-foundation/2025/03/31/reminder-vsphere-7-to-reach-end-of-service-october-2-2025/
Date: March 31, 2025

### 1.4 Microsoft Ecosystem

[FACT]
Approximately 181 million enterprise devices were still running Windows 10 as of mid-2025, per Nexthink estimates, despite Windows 10 reaching End of Support on October 14, 2025.
URL: https://www.theregister.com/2025/09/04/windows_10_esu_costs/
Date: September 4, 2025

[FACT]
In 2025, approximately 120 Microsoft offerings reached end of support, transitioned to Extended Support, or were retired. The largest was Windows 10.
URL: https://windowsforum.com/threads/microsoft-2025-sunsetting-windows-10-azure-and-apps-end-of-support-guide.377098/
Date: 2025

[FACT]
Microsoft Dynamics 365 Finance + Operations (on-premises) lists 20 active or recently expired service update versions (10.0.30 through 10.0.49) in its current release table, with all versions prior to the most current marked as expired under the Modern Lifecycle Policy.
URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/migration-upgrade/on-prem-version-update-policy
Date: August 20, 2025

---

## 2. Backward Compatibility Burden

### 2.1 API Compatibility

[FACT]
Semantic Versioning 2.0.0 (semver.org) defines the standard: "Major version X (X.y.z | X > 0) MUST be incremented if any backward incompatible changes are introduced to the public API." Minor versions are reserved for backward-compatible additions; patch versions for backward-compatible bug fixes only.
URL: https://semver.org/
Date: Specification document, accessed 2025

[STATISTIC]
A 2025 Postman survey found that over 65% of developers confirm that separate versioned endpoints reduce integration failures significantly, described as "avoiding surprise disruptions for users relying on stable contracts."
URL: https://blog.dreamfactory.com/top-5-api-versioning-strategies-2025-dreamfactory
Date: 2025

[FACT]
Recommended deprecation timelines for API versioning in enterprise settings call for "3-6 months' notice typically allowing consumers adequate time to migrate" before removing older API versions.
URL: https://www.usefulfunctions.co.uk/2025/11/08/api-versioning-strategies-maintaining-backward-compatibility/
Date: November 2025

### 2.2 Database Schema Compatibility

[FACT]
Flyway executes SQL migration scripts in version order, tracking what has been applied in a metadata table. "Each script runs exactly once and checksums prevent modification." Liquibase uses changelogs (XML, YAML, JSON, or SQL) with rollback support.
URL: https://www.red-gate.com/hub/university/learning-pathways/database-devops-learning-pathway/database-versioning-source-control/level-0/the-what-why-and-how-of-database-versioning-with-flyway/
Date: 2025

[QUOTE]
"A lack of control over database versions is most keenly felt in a high failure rate for deployments."
— Redgate (Flyway documentation)
URL: https://www.red-gate.com/hub/university/learning-pathways/database-devops-learning-pathway/database-versioning-source-control/level-0/the-what-why-and-how-of-database-versioning-with-flyway/
Date: 2025

[FACT]
When database versions are not tightly controlled, "weeks of work may have to be abandoned if it turns out that the version that was tested wasn't the release candidate," creating direct productivity loss during upgrade cycles.
URL: https://www.red-gate.com/hub/university/learning-pathways/database-devops-learning-pathway/database-versioning-source-control/level-0/the-what-why-and-how-of-database-versioning-with-flyway/
Date: 2025

[FACT]
Teams must "coordinate application releases with the database changes that support them, and to avoid compatibility, or 'version mismatch' problems" — requiring cross-team synchronization with each on-premises release.
URL: https://www.red-gate.com/hub/university/learning-pathways/database-devops-learning-pathway/database-versioning-source-control/level-0/the-what-why-and-how-of-database-versioning-with-flyway/
Date: 2025

---

## 3. Upgrade Path Complexity

### 3.1 Skip-Version Upgrade Restrictions

[FACT]
Azure Kubernetes Service (AKS) enforces sequential upgrades: "Kubernetes minor versions can't be skipped. To upgrade from 1.27.x → 1.29.x, you need to first upgrade from 1.27.x → 1.28.x, and then upgrade from 1.28.x → 1.29.x."
URL: https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions
Date: 2025

[FACT]
Amazon EKS enforces the same policy: "You can update only one minor version at a time." This applies to both the control plane and, with version skew allowance, the data plane nodes.
URL: https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html
Date: 2025

[FACT]
Cluster API supports skipping up to three minor versions (e.g., v1.6.x can upgrade directly to v1.9.x). "Upgrades outside from version older n-3 might lead to a management cluster in a non-functional state."
URL: https://cluster-api.sigs.k8s.io/reference/versions
Date: 2025

### 3.2 Data Migration and Rollback

[STATISTIC]
"80% of data migration projects run over time or budget, often due to missing strategy and unreliable processes."
URL: https://streamkap.com/resources-and-guides/data-migration-best-practices
Date: 2025

[STATISTIC]
"Legacy data formats and database structures often clash with modern cloud platforms, causing up to 45% of migration failures and data corruption, system downtime, and project delays averaging 3-6 months."
URL: https://www.cloudficient.com/blog/10-common-data-migration-challenges-and-how-to-overcome-them
Date: 2025

[FACT]
Best practice guidance for database upgrade rollback requires: "each migration has a corresponding rollback script," use of descriptive naming conventions distinguishing up (upgrade) and down (rollback) scripts, and sequence-number prefixes ensuring execution order.
URL: https://goframe.org/en/articles/sql-migrate-database-migration
Date: 2025

[FACT]
IBM provides a Pre-Upgrade Verification Tool (PRUV) for IBM i customers. The current release is pruv_7.6.0.20250728 (updated July 28, 2025) and supports IBM i releases from V5R2M0 through current supported releases.
URL: https://www.ibm.com/support/pages/ibm-pre-upgrade-verification-tool-ibm-i
Date: July 2025

[FACT]
VMware Aria Operations provides a Pre-Upgrade Readiness Assessment Tool that performs "impact analysis and validation check results of the system's upgrade ability, scanning content for discontinued or disabled metrics and providing recommended replacements."
URL: https://knowledge.broadcom.com/external/article/369264/using-the-preupgrade-readiness-assessmen.html
Date: 2025

[FACT]
Cisco's ACI Pre-Upgrade Validator application "checks for potential issues that could cause APIC and ACI switch node upgrades to fail and verifies fabric configuration for traffic disruption risks during upgrades."
URL: https://dcappcenter.cisco.com/pre-upgrade-validator.html
Date: 2025

### 3.3 Enterprise Upgrade Project Risk

[STATISTIC]
A McKinsey study found that 66% of enterprise software projects have cost overruns, one-third go beyond the estimated schedule, and approximately 20% fall short of promised benefits.
URL: https://www.forecast.app/blog/66-of-enterprise-software-projects-have-cost-overruns
Date: 2025

[STATISTIC]
47% of organizations worldwide experienced cost overruns for ERP implementation projects in 2023.
URL: https://www.statista.com/statistics/526423/worldwide-erp-implementation-projects-cost-overrun/
Date: 2023

[STATISTIC]
SAP ECC-to-S/4HANA migration "can cost as little as $2 million" but "can run up to $1 billion for large enterprises with complex installations."
URL: https://www.cio.com/article/4000543/nearly-half-of-sap-ecc-customers-may-stick-with-legacy-erp-beyond-2027.html
Date: 2025

---

## 4. Customer Upgrade Resistance

### 4.1 Stated Reasons

[QUOTE]
"They will say their ECC environment is very robust, very stable...it does not mean that the ECC environment is...going to stop working."
— Forrester analyst Akshara Naik Lopez
URL: https://www.cio.com/article/4000543/nearly-half-of-sap-ecc-customers-may-stick-with-legacy-erp-beyond-2027.html
Date: 2025

[FACT]
SAP customer resistance to S/4HANA migration centers on: ECC "works well and does what they need it to do"; insufficient "compelling new functionality in EHP6-8 or S/4HANA to warrant all the effort, time and money required"; heavily customized systems creating a "further deterrent to upgrading since upgrades are known to sometimes cause problems."
URL: https://www.riministreet.com/blog/thanks-but-no-thanks-sap-customers-dont-see-the-value/
Date: 2025

[STATISTIC]
40% of SAP ECC customers on enhancement packages 0-5 were not aware of the 2025 support deadline, per SAP User Group data.
URL: https://www.riministreet.com/blog/thanks-but-no-thanks-sap-customers-dont-see-the-value/
Date: 2025

### 4.2 Regulatory Change Freezes

[FACT]
Following a U.S. government shutdown in late 2025, ASTP/ONC granted healthcare entities enforcement discretion, extending HTI-1 Final Rule certification requirements for health IT developers from January 1, 2026 to March 1, 2026. This type of regulatory suspension directly prevents software upgrades that would alter certified system configurations.
URL: https://healthedge.com/resources/blog/4-emerging-healthcare-regulatory-trends-in-2025-and-beyond
Date: 2025

[FACT]
Healthcare organizations participating in ACOs or alternative payment models face regulatory requirements for "use of certified EHR technology for a full calendar year," effectively locking software versions from mid-year changes during a compliance measurement period.
URL: https://healthedge.com/resources/blog/4-emerging-healthcare-regulatory-trends-in-2025-and-beyond
Date: 2025

[FACT]
Financial industry regulations such as PCI-DSS, HIPAA, and ISO 27001 require organizations to use supported software. Running end-of-life systems "can result in audit failures, fines, and even loss of certifications."
URL: https://blog.1password.com/end-of-life-software/
Date: 2025

### 4.3 Legacy IT Budget Constraints

[FACT]
"Legacy systems consuming 60-80% of IT budgets for maintenance leave minimal resources for innovation and growth initiatives."
URL: https://stssoftware.medium.com/enterprise-software-modernization-complete-guide-2025-ca8528b50290
Date: 2025

---

## 5. Testing Overhead: The N-Version QA Matrix

### 5.1 Matrix Dimensions

For an ISV maintaining N supported versions across M supported customer environment configurations, the test matrix grows as N × M. Typical dimensions include:

- Supported software versions (e.g., v3.x, v4.x, v5.x)
- Customer operating systems (RHEL 8, RHEL 9, Windows Server 2019, Windows Server 2022)
- Database backends (PostgreSQL 14, 15, 16; Oracle 19c, 21c; SQL Server 2019, 2022)
- Customer Kubernetes versions if applicable (N-3 window per provider)
- Browser or client versions for UI-bearing components

[FACT]
Compatibility testing best practice structures the test matrix into tiers: Tier A covers ~80% of production traffic and must pass all tests before release; Tier B covers ~15% (critical journeys only); Tier C covers ~5% long-tail configurations using smoke tests only.
URL: https://avekshaa.com/application-performance-engineering/compatibility-testing-in-2025-a-no-nonsense-guide-for-engineering-leaders/
Date: 2025

[FACT]
Amazon EKS supports at least three Kubernetes minor versions at any given time (standard support: 14 months per version; extended support: 12 months additional). AKS supports N, N-1, and N-2 in standard support, plus N-3 in platform support.
URL: https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html
Date: 2025

### 5.2 Staffing and Cost Estimates

The following table applies the standard FTE estimation framework to QA overhead for multi-version on-premises support (baseline assumption: mid-size ISV with 3 active software versions, 50 enterprise customers, 4 supported OS/DB combinations per version):

| QA Domain | On-Premises (3 versions) | Managed K8s | Cloud-Native (SaaS) |
|---|---|---|---|
| Regression testing per release | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Full matrix: 3 versions × 4 env combos = 12 test configurations | K8s version window (N-3) managed by cloud provider; workload testing only | Single version; CI/CD pipeline; no version matrix |
| | Manual + automated suites per config | Automated with cluster upgrade testing | Fully automated CI/CD |
| Est. FTE: 1.5–2.5 QA | Est. FTE: 0.75–1.25 QA | Est. FTE: 0.25–0.5 QA |
| Pre-upgrade validation | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Custom pre-flight validators per version pair | Provider pre-upgrade tooling (AKS, EKS upgrade APIs) | Not applicable — no customer-triggered upgrades |
| | Rollback scripts per DB schema version | Limited schema migration scope | Not applicable |
| Est. FTE: 0.5–1.0 | Est. FTE: 0.25 | Est. FTE: 0.0 |
| Compatibility matrix maintenance | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Grows as versions × environments expand | Defined by cloud provider support windows | Not applicable |
| Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0 |

[FACT]
QA setup costs for medium-to-large enterprises "usually range from $50,000–$250,000" with cost influenced by "technology stack, automation tools, infrastructure, and system complexity."
URL: https://thinksys.com/qa-testing/qa-strategy-enterprise-software/
Date: 2025

---

## 6. Deprecation Politics: Sunsetting Old Versions

### 6.1 Contractual Entitlements

[QUOTE]
"Vendors should be contractually obligated to maintain, update and improve the software for the term of the contract, or for a minimum period of time that is specified in the contract."
— Pillsbury Law (Lessons from a Major Software Sunsetting)
URL: https://www.pillsburylaw.com/en/news-and-insights/software-sunsetting-contractual-postcontractual-best-practices.html
Date: 2025

[QUOTE]
"If a vendor sunsets a software solution mid-contract, they should provide and implement a technically and functionally equivalent replacement solution at no additional charge to the client."
— Pillsbury Law
URL: https://www.pillsburylaw.com/en/news-and-insights/software-sunsetting-contractual-postcontractual-best-practices.html
Date: 2025

[QUOTE]
"Vendor promises about continued support or future replacements have limited value unless translated into enforceable contractual obligations."
— Pillsbury Law
URL: https://www.pillsburylaw.com/en/news-and-insights/software-sunsetting-contractual-postcontractual-best-practices.html
Date: 2025

### 6.2 Vendor Behavior Under Deprecation Pressure

[FACT]
SAP announced "SAP ERP, private edition, transition option" available from 2031 through end of 2033 for customers with "large and very complex IT landscapes," requiring enrollment in RISE with SAP cloud migration deals. SAP stated explicitly: "This is not a prolongation of the mainstream maintenance deadlines communicated in 2020."
URL: https://www.theregister.com/2025/01/28/sap_extends_support_deadline/
Date: January 28, 2025

[FACT]
When SAP ECC customers on EHP0-5 had mainstream support end December 31, 2025, they were converted to "customer-specific maintenance, in which SAP no longer updates the release with legal changes." According to SAPinsider, "new fees may be imposed to resolve new problems" under this arrangement.
URL: https://www.riministreet.com/blog/thanks-but-no-thanks-sap-customers-dont-see-the-value/
Date: 2025

[FACT]
SAP extended the end date for compatibility packs in SAP ECC environments from the end of 2025 to the end of May 2026, responding to customer pressure.
URL: https://sapinsider.org/blogs/sap-sets-end-date-for-compatibility-packs-in-sap-ecc/
Date: 2025

[QUOTE]
Gartner analyst Fabio Di Capua, on SAP not publicly reporting S/4HANA migration numbers: "When I see vendors not reporting numbers immediately, they are not good, because if they were good, they will be the first one to shout."
— Gartner analyst Fabio Di Capua, quoted in CIO.com
URL: https://www.cio.com/article/4000543/nearly-half-of-sap-ecc-customers-may-stick-with-legacy-erp-beyond-2027.html
Date: 2025

[FACT]
Oracle increased support fees 8% in 2022. Customers on perpetual licenses "pay perpetual licenses expecting included upgrades," creating tension when Oracle extends old versions rather than accelerating migration to new ones.
URL: https://www.theregister.com/2025/02/18/oracle_extends_19c_support/
Date: February 18, 2025

### 6.3 Third-Party Support Market

[FACT]
Rimini Street, a third-party support provider for SAP and Oracle, claims to offer customers savings of "up to 50% off of their annual support fees" and "up to 90% on their total cost of ownership" versus continuing with vendor-provided support — creating an alternative pathway that further delays customers from upgrading.
URL: https://www.riministreet.com/blog/thanks-but-no-thanks-sap-customers-dont-see-the-value/
Date: 2025

---

## 7. Feature Gating: Conditional Capabilities Across Versions

### 7.1 Feature Flags in On-Premises Contexts

[FACT]
Feature flags "enable software teams to control the visibility of new features, decouple deployment from release, and facilitate safer, more gradual rollouts" by toggling feature availability without redeployment.
URL: https://launchdarkly.com/blog/what-are-feature-flags/
Date: 2025

[FACT]
Flagsmith offers "SaaS, private cloud, and self-hosted (private cloud and on-prem options) deployment flexibility. Teams working in banking, healthcare, and insurance find it especially useful as it ticks all the boxes needed for security and compliance."
URL: https://www.flagsmith.com/blog/top-7-feature-flag-tools
Date: 2025

[FACT]
Unleash's on-premises deployment option "keeps all feature flag data within your security perimeter and satisfies strict compliance requirements without trusting third-party vendors."
URL: https://www.getunleash.io/
Date: 2025

### 7.2 Version-Gated Feature Delivery

[FACT]
Dynamic targeting in feature flag tools allows enabling features based on "demographic data, geographic location, subscription level, or behavioral patterns." In on-premises contexts, this mechanism can gate features by the detected version of the underlying platform or infrastructure, allowing a single codebase to expose different capabilities depending on customer environment version.
URL: https://launchdarkly.com/blog/what-are-feature-flags/
Date: 2025

[UNVERIFIED — No 2025 primary source found] ISVs shipping AI-dependent features (e.g., GPU-accelerated inference, vector database search) that require infrastructure capabilities unavailable in older customer environments commonly implement capability-detection gates that gracefully degrade or disable those features. This practice is widely described in practitioner engineering blogs but no Tier 1 or Tier 2 source quantifying its prevalence or cost was located. Believed accurate based on standard software engineering practice.

---

## 8. Comparison: SaaS Single-Version Model vs. On-Premises Multi-Version

| Dimension | On-Premises | Managed K8s | Cloud-Native (SaaS) |
|---|---|---|---|
| Active supported versions | 3–5+ concurrent major versions | 3 K8s minor versions (N to N-2) managed by cloud provider | 1 version — all customers on latest |
| Release cadence | 6–18 month major cycles; security patches required for each active version | Quarterly Kubernetes releases; workload releases independent | Daily to multiple times per day deployable |
| Customer upgrade control | Customer controls timing; vendor cannot force upgrade | Cloud provider manages control plane upgrades; workload upgrades customer-controlled | Vendor controls; no customer opt-out of version |
| QA matrix complexity | N versions × M environments | Limited by cloud provider support windows | Single configuration |
| Data migration requirement | Per-version schema migration scripts required | Schema migrations handled by application team; no version forks | Single schema; continuous migration |
| Rollback mechanism | Required for each version upgrade; customer-managed | Provider-managed control plane rollback; application rollback by ISV | Provider-managed; typically within one deployment |
| Feature delivery | Gated by customer's installed version | Gated by workload deployment frequency | Immediate for all customers simultaneously |
| Deprecation complexity | Contractual, regulatory, and political obstacles | Cloud provider EOL drives upgrade windows | Not applicable — vendor retires old behavior centrally |

[STATISTIC]
SaaS companies using DevOps automation can achieve "daily or hourly deployments." Some SaaS companies "deploy 50+ updates per day without downtime."
URL: https://medium.com/atmosly/how-us-saas-companies-use-devops-automation-to-scale-faster-2025-guide-d0a243135a17
Date: December 2025

[STATISTIC]
"Companies that implement DevOps deploy code 30 times more frequently, have 200 times shorter lead times and recover from failure 168 times faster compared to traditional approaches."
URL: https://www.teravisiontech.com/blog/devops-for-saas-teams-faster-delivery
Date: 2025

[FACT]
Traditional on-premises software had release cycles running "6-18 months with teams spending months in requirements gathering, developers building in isolation for quarters, and QA testing exhaustively before launch."
URL: https://blog.cerebralops.in/why-saas-delivery-is-different-from-traditional-software-development/
Date: 2025

[QUOTE]
"All operational and security responsibilities are transferred to vendor" in a SaaS model, versus on-premises where "Customer is completely responsible for compliance, security, or operational efficiency."
— Gleecus analysis
URL: https://gleecus.com/blogs/picking-software-deployment-model/
Date: 2025

[FACT]
"With SaaS's single version model, all customers run on the same base version of the software, which creates operational efficiency for the business and helps serve customers more effectively."
URL: https://www.symphonyai.com/resources/blog/financial-services/saas-vs-on-premise-software/
Date: 2025

[FACT]
DORA research (2018 and 2019) found that "elite performers were more than 23 times more likely to have met all five essential cloud characteristics than low performers." Only 29% of organizations claiming cloud adoption actually met all five essential cloud characteristics.
URL: https://dora.dev/capabilities/flexible-infrastructure/
Date: 2025 (research accessed)

---

## Key Takeaways

- **Version proliferation is the default, not the exception.** Major on-premises ISVs — Oracle, SAP, Microsoft, VMware — routinely maintain three to five or more concurrently supported major release families. Oracle currently patches 19c, 21c, 23ai, and 26ai in a single monthly release cycle. SAP supports S/4HANA releases from 2020 through 2023 under staggered mainstream maintenance windows extending to 2030.

- **Customer upgrade resistance is structural and measurable.** Only 39% of SAP ECC customers had migrated to S/4HANA by end of 2024 despite a 2027 end-of-maintenance deadline. 181 million enterprise devices were still running Windows 10 within weeks of its October 2025 EOL date. Customization complexity, risk aversion, regulatory change freezes, and contractual entitlements to continued support all compound to make this resistance durable.

- **Backward compatibility is a multi-layer obligation.** ISVs must maintain API compatibility (avoiding breaking changes across semver major versions), database schema compatibility (sequential migration scripts with rollback coverage per version), and configuration compatibility across three dimensions simultaneously. Every new feature must be evaluated for its impact on each supported release branch.

- **QA matrix complexity grows multiplicatively.** The test burden for an ISV supporting three major software versions across four OS/DB configuration families is at minimum 12 discrete test configurations per release cycle. This scales directly with the number of supported versions and customer environment permutations. SaaS eliminates this entirely by operating a single-version, single-configuration target.

- **SaaS removes version management overhead at the architectural level.** SaaS ISVs operate a single codebase at a single version for all customers simultaneously, enabling deployment cadences of multiple times per day versus 6-18 month on-premises release cycles. The operational, QA, compatibility, and deprecation overhead described throughout this file is structurally absent from a cloud-native delivery model, representing the single largest operational leverage point in the ISV deployment model decision.

---

## Related — Out of Scope

- **Deployment mechanics for on-premises releases** (e.g., installer packaging, air-gap delivery, silent install scripting): See [F58: Deploy & Release Differences]
- **Support burden and customer environment variability** (e.g., ticket volume by version, support staffing ratios): See [F61: Support Burden & Customer Environment Variability]
- **Patch and security update delivery processes** (e.g., CVE response time by deployment model, patch distribution logistics): See [F60: Update, Patch & Scale]
- **Licensing structures and entitlement enforcement across versions** (e.g., perpetual vs. subscription models, license audits): See [F65: Licensing]

---

## Sources

- https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html
- https://www.theregister.com/2025/02/18/oracle_extends_19c_support/
- https://red9.com/blog/oracle-19c-23c-overview-2025/
- https://www.oracledbaonlinetraining.com/post/october-2025-oracle-ru-patch-numbers-every-dba-must-know-19c-21c-23ai-26ai
- https://mikedietrichde.com/2025/10/14/oracle-ai-database-26ai-replaces-oracle-database-23ai/
- https://dbvisit.com/blog/oracle-support-extended-for-19c-and-23ai
- https://www.cio.com/article/4000543/nearly-half-of-sap-ecc-customers-may-stick-with-legacy-erp-beyond-2027.html
- https://www.riministreet.com/blog/thanks-but-no-thanks-sap-customers-dont-see-the-value/
- https://www.theregister.com/2025/01/28/sap_extends_support_deadline/
- https://sapinsider.org/blogs/sap-sets-end-date-for-compatibility-packs-in-sap-ecc/
- https://news.sap.com/2022/09/new-sap-s4hana-release-maintenance-strategy/
- https://support.sap.com/en/release-upgrade-maintenance/maintenance-information/maintenance-strategy/s4hana-business-suite7.html
- https://www.pillsburylaw.com/en/news-and-insights/software-sunsetting-contractual-postcontractual-best-practices.html
- https://blogs.vmware.com/cloud-foundation/2025/03/31/reminder-vsphere-7-to-reach-end-of-service-october-2-2025/
- https://www.theregister.com/2025/09/04/windows_10_esu_costs/
- https://windowsforum.com/threads/microsoft-2025-sunsetting-windows-10-azure-and-apps-end-of-support-guide.377098/
- https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/migration-upgrade/on-prem-version-update-policy
- https://semver.org/
- https://blog.dreamfactory.com/top-5-api-versioning-strategies-2025-dreamfactory
- https://www.usefulfunctions.co.uk/2025/11/08/api-versioning-strategies-maintaining-backward-compatibility/
- https://www.red-gate.com/hub/university/learning-pathways/database-devops-learning-pathway/database-versioning-source-control/level-0/the-what-why-and-how-of-database-versioning-with-flyway/
- https://streamkap.com/resources-and-guides/data-migration-best-practices
- https://www.cloudficient.com/blog/10-common-data-migration-challenges-and-how-to-overcome-them
- https://goframe.org/en/articles/sql-migrate-database-migration
- https://www.ibm.com/support/pages/ibm-pre-upgrade-verification-tool-ibm-i
- https://knowledge.broadcom.com/external/article/369264/using-the-preupgrade-readiness-assessmen.html
- https://dcappcenter.cisco.com/pre-upgrade-validator.html
- https://www.forecast.app/blog/66-of-enterprise-software-projects-have-cost-overruns
- https://www.statista.com/statistics/526423/worldwide-erp-implementation-projects-cost-overrun/
- https://healthedge.com/resources/blog/4-emerging-healthcare-regulatory-trends-in-2025-and-beyond
- https://blog.1password.com/end-of-life-software/
- https://stssoftware.medium.com/enterprise-software-modernization-complete-guide-2025-ca8528b50290
- https://thinksys.com/qa-testing/qa-strategy-enterprise-software/
- https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html
- https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions
- https://cluster-api.sigs.k8s.io/reference/versions
- https://launchdarkly.com/blog/what-are-feature-flags/
- https://www.flagsmith.com/blog/top-7-feature-flag-tools
- https://www.getunleash.io/
- https://medium.com/atmosly/how-us-saas-companies-use-devops-automation-to-scale-faster-2025-guide-d0a243135a17
- https://www.teravisiontech.com/blog/devops-for-saas-teams-faster-delivery
- https://blog.cerebralops.in/why-saas-delivery-is-different-from-traditional-software-development/
- https://gleecus.com/blogs/picking-software-deployment-model/
- https://www.symphonyai.com/resources/blog/financial-services/saas-vs-on-premise-software/
- https://dora.dev/capabilities/flexible-infrastructure/
