# E05: Enterprise Security and Compliance as a Structural Barrier to Replacing SaaS

**Research Wave:** Wave 3 — SaaS Durability Structural Factors
**Topic:** How enterprise security and compliance requirements affect the feasibility of replacing SaaS with custom-built software
**Audience:** C-suite
**Date:** March 2026
**Word Count:** ~2,200

---

## Executive Summary

Enterprise security and compliance obligations represent one of the most durable structural advantages for established SaaS vendors. Obtaining and maintaining major security certifications — SOC 2, ISO 27001, FedRAMP, HIPAA — costs hundreds of thousands of dollars and requires years of continuous operational discipline that most internal engineering teams are not staffed to deliver. The rise of AI-generated code introduces a new and compounding risk: Veracode's 2025 research found that AI coding tools choose insecure implementations 45% of the time, with Java-based code failing security tests 72% of the time. Simultaneously, IBM's 2026 X-Force Threat Intelligence Index documents a nearly 4x increase in supply chain and third-party compromises since 2020, and Verizon's 2025 DBIR confirms third-party involvement in breaches has doubled to 30%. In regulated industries — financial services, healthcare, and government — the compliance overhead of custom software is not merely expensive; it can be legally prohibitive. SaaS vendors that already hold certifications transfer a significant share of audit burden and liability to themselves. Gartner's cited finding that in 99% of cloud security failures through 2025 the customer — not the platform — bears fault illustrates a sobering corollary: organizations that move from certified SaaS to uncertified custom builds absorb security liability that was previously externalized.

---

## Section 1: The Certification Cost Wall

### SOC 2

[STATISTIC]
"SOC 2 Type 2 audit costs for enterprises usually land between $75,000 and $150,000, and in some complex environments, even $200,000+, because Type 2 looks at how controls perform over time, typically across a 3 to 12-month window."
— dsalta.com
URL: https://www.dsalta.com/resources/articles/soc-2-certification-2025-auditor-cost-timeline-guide
Date: 2025

[STATISTIC]
SOC 2 Type 1 audit spans 4 to 8 weeks; SOC 2 Type 2 runs 6 to 15 months depending on scope, complexity, and readiness.
— dsalta.com
URL: https://www.dsalta.com/resources/articles/soc-2-certification-2025-auditor-cost-timeline-guide
Date: 2025

[FACT]
Compliance platforms for integrations, dashboards, and evidence management add $6,000–$20,000 per year in ongoing overhead on top of audit costs.
— dsalta.com
URL: https://www.dsalta.com/resources/articles/soc-2-certification-2025-auditor-cost-timeline-guide
Date: 2025

[STATISTIC]
"89% of enterprise buyers now require security certifications like SOC 2 before making purchasing decisions."
— Vanta (cited in BD Emerson)
URL: https://www.bdemerson.com/article/top-saas-security-certifications
Date: 2025

### ISO 27001

[STATISTIC]
ISO 27001 certification cost for enterprise-level companies (hundreds of employees) is $75,000 or more, with combined Stage 1 and Stage 2 audit costs of $30,000–$60,000 and preparation costs of $5,000–$75,000 beyond that.
— Rhymetec
URL: https://rhymetec.com/iso-27001-certification-cost-breakdown-2025/
Date: 2025

[FACT]
"Companies with custom infrastructure, multi-cloud environments, or proprietary platforms often require additional effort in terms of documentation and control verification" for ISO 27001 certification.
— StrongDM
URL: https://www.strongdm.com/blog/iso-27001-certification-cost
Date: 2026

[FACT]
ISO 27001 requires surveillance audits annually and a full recertification audit every three years, creating a permanent recurring cost structure.
— Rhymetec
URL: https://rhymetec.com/iso-27001-certification-cost-breakdown-2025/
Date: 2025

### FedRAMP

[STATISTIC]
"FedRAMP compliance will cost $250,000 to $750,000 — though it can go as high as $1.5 million."
— Workstreet
URL: https://www.workstreet.com/blog/fedramp-certification-cost
Date: 2025

[DATA POINT]
FedRAMP cost breakdown by category:
- Third-Party Assessment Organization (3PAO) fees: $50,000–$400,000+
- Consulting and advisory fees: $100,000–$500,000+
- Remediation and engineering: $10,000–$100,000+
- Continuous monitoring (annual, recurring): $50,000–$100,000+
— Workstreet
URL: https://www.workstreet.com/blog/fedramp-certification-cost
Date: 2025

[FACT]
The FedRAMP Moderate impact level — required for approximately 80% of cloud applications handling government data — mandates implementation of 325 security controls.
— Workstreet
URL: https://www.workstreet.com/blog/fedramp-certification-cost
Date: 2025

[FACT]
"KPI standards development for FedRAMP Low and Moderate authorizations is delayed until at least April 2026" due to federal funding cuts and staff shortages.
— Irina Denisenko (CEO, Knox) and Carrie Lee (former CPO and Deputy CIO, Department of Veterans Affairs), Nextgov/FCW
URL: https://www.nextgov.com/ideas/2026/02/navigating-fedramp-20x-and-continuous-compliance-imperative/411300/
Date: February 2026

[FACT]
Government Authority to Operate (ATO) for custom software systems "can take anywhere from 6–18 months (occasionally longer) and can cost six to seven figures in costs and internal resourcing."
— Workstreet
URL: https://www.workstreet.com/blog/what-is-an-ato
Date: 2025

[FACT]
A formal 3PAO audit for a custom Moderate-impact government system "can easily run $50,000–$150,000 or more."
— Cloud.gov / StackArmor
URL: https://stackarmor.com/how-much-does-it-cost-to-get-fedramp-compliant-and-obtain-an-ato/
Date: 2025

---

## Section 2: Compliance Frameworks — SaaS Vendors vs. Custom Builds

### HIPAA (Healthcare)

[FACT]
The 2025 HIPAA Security Rule update is "the most significant change in over a decade, ending the era of ambiguous SaaS-related controls and establishing specific, enforceable requirements that directly impact how organizations govern and secure SaaS applications."
— Grip Security
URL: https://www.grip.security/2025-hipaa-security-rule-requirements
Date: 2025

[FACT]
HIPAA applies equally to both SaaS vendors and custom software developers: "if your code handles Protected Health Information (PHI), even briefly, you're responsible for securing it."
— HIPAA Journal
URL: https://www.hipaajournal.com/hipaa-compliance-for-saas/
Date: 2025

[FACT]
Any third-party developer or vendor handling PHI must sign a Business Associate Agreement (BAA), qualifying them as a Business Associate under HIPAA — a requirement applying equally to custom software teams and SaaS vendors.
— ULAM Labs (Anna Buczak)
URL: https://www.ulam.io/blog/hipaa-compliant-software-requirements-for-healthcare-in-2025---what-engineering-teams-need-to-know
Date: 2025

[STATISTIC]
"Software applications that incorporate data minimization principles from initial design typically require 30–50% less effort to achieve compliance compared to those retrofitted with security controls after development."
— Blaze.tech
URL: https://www.blaze.tech/post/hipaa-compliant-software-requirements
Date: 2025

[STATISTIC]
Healthcare participants saw the costliest data breaches across all industries in 2025, with average breach costs reaching $9.77 million.
— IBM Cost of a Data Breach Report (cited in redsentry.com)
URL: https://redsentry.com/resources/blog/saas-security-risks-2026-misconfigurations-compliance-gaps-and-data-breach-prevention
Date: 2026

### Financial Services (SOX, FINRA, SEC, PCI DSS)

[FACT]
Fintech companies operating in the U.S. must comply with the Consumer Financial Protection Bureau, FDIC, OCC, SEC, FTC, CFTC, FinCEN, and FINRA — requiring custom software teams to maintain audit-ready compliance with each body simultaneously.
— Global Legal Insights
URL: https://www.globallegalinsights.com/practice-areas/fintech-laws-and-regulations/usa/
Date: 2025

[FACT]
SEC and FINRA Rule 17a-4 requires electronic records to "be stored in non-rewriteable, non-erasable formats with detailed audit trails and time-stamps, with records typically retained for three to six years."
— Phoenix Strategy Group
URL: https://www.phoenixstrategy.group/blog/fintech-data-storage-compliance-checklist-2025
Date: 2025

[FACT]
FINRA Rules 3110 and 3120 require firms to "establish and maintain a supervisory system and written procedures to ensure compliance with applicable securities laws and regulations when using third-party services," including custom software built by internal teams.
— FINRA 2025 Annual Regulatory Compliance Oversight Report (cited by ACA Group)
URL: https://www.acaglobal.com/industry-insights/2025-finra-annual-regulatory-compliance-oversight-report-2/
Date: 2025

[FACT]
FINRA's 2025 report cites "an increasing reliance on third-party vendors for various operational and compliance activities" as a key risk area, noting firms must conduct due diligence, validate data protection controls in vendor contracts, and manage fourth-party vendor risks.
— ACA Group
URL: https://www.acaglobal.com/industry-insights/2025-finra-annual-regulatory-compliance-oversight-report-2/
Date: 2025

[STATISTIC]
Financial sector data breach costs in 2025 average $6.08 million per incident — "22% higher than the global average."
— IBM (cited in redsentry.com)
URL: https://redsentry.com/resources/blog/saas-security-risks-2026-misconfigurations-compliance-gaps-and-data-breach-prevention
Date: 2026

---

## Section 3: CISO Perspectives on Custom vs. Vendor-Managed Security

[FACT]
"Gartner [found] that in 99% of cloud security failures through 2025, the customer — not the platform — will be at fault."
— Obsidian Security (Scott Young)
URL: https://www.obsidiansecurity.com/blog/saas-security-shared-responsibility-model
Date: July 9, 2025 (updated November 5, 2025)

[QUOTE]
"They secure their platform, not your business."
— Scott Young, Obsidian Security
URL: https://www.obsidiansecurity.com/blog/saas-security-shared-responsibility-model
Date: July 9, 2025

[QUOTE]
"How you use, configure, monitor, and manage access to that platform is squarely your responsibility."
— Scott Young, Obsidian Security
URL: https://www.obsidiansecurity.com/blog/saas-security-shared-responsibility-model
Date: July 9, 2025

[STATISTIC]
Obsidian Security handled 150+ incident responses in the past year related to SaaS compromises, representing a 300% year-over-year increase in SaaS compromise incidents.
— Scott Young, Obsidian Security
URL: https://www.obsidiansecurity.com/blog/saas-security-shared-responsibility-model
Date: July 9, 2025

[STATISTIC]
"SaaS security is now a high priority for 86% of organizations, with 76% increasing budgets" — Cloud Security Alliance / Valence Security survey of 420 IT and security professionals, conducted January 2025.
— CSA State of SaaS Security Report 2025
URL: https://cloudsecurityalliance.org/artifacts/state-of-saas-security-report-2025
Date: 2025

[STATISTIC]
"66 percent of all organizations found the shared responsibility model for SaaS confusing, which can lead to security gaps since the customer is responsible for data and identity management under the typical SaaS shared responsibility model."
— Valence Security / AppOmni (cited in research summaries)
URL: https://www.valencesecurity.com/resources/blogs/understanding-the-shared-responsibility-model-in-saas
Date: 2025

[STATISTIC]
"55% of employees adopt SaaS without security involvement" and "57% of organizations report fragmented administration."
— CSA State of SaaS Security Report 2025 (420 respondents, January 2025)
URL: https://cloudsecurityalliance.org/artifacts/state-of-saas-security-report-2025
Date: 2025

[STATISTIC]
"90% of security and risk management leaders, including CISOs, told Forrester they expect a budget increase in 2025."
— Forrester (cited in Gartner security spending commentary)
URL: https://venturebeat.com/ai/forrester-cybersecurity-budgeting-2025-ciso-fiscal-accountability
Date: 2025

---

## Section 4: Liability and Risk Transfer — SaaS vs. Build

[FACT]
SaaS liability caps in enterprise contracts are "a frequent and intensely debated point of negotiation," with many agreements initially proposing caps at "a multiple of the annual subscription fees."
— Irina Beschieriu, Technology Attorney, ATOS, writing for IAPP
URL: https://iapp.org/news/a/uncapping-risk-the-growing-burden-of-data-privacy-liability-in-tech-contracts
Date: 2025

[FACT]
"Organizations now routinely insist on uncapped liability for data breaches" caused by provider "gross negligence, willful misconduct, or failure to comply with applicable data privacy laws."
— Irina Beschieriu, Technology Attorney, ATOS, writing for IAPP
URL: https://iapp.org/news/a/uncapping-risk-the-growing-burden-of-data-privacy-liability-in-tech-contracts
Date: 2025

[STATISTIC]
The global average cost of a data breach fell 9% to $4.44 million in 2025 from $4.88 million in 2024, though the U.S. average grew 9% to $10.22 million.
— IBM Cost of a Data Breach Report (cited across multiple sources)
URL: https://redsentry.com/resources/blog/saas-security-risks-2026-misconfigurations-compliance-gaps-and-data-breach-prevention
Date: 2026

[FACT]
In custom software deployments, all breach liability sits internally — there is no vendor indemnification, no SLA backstop, and no shared audit infrastructure. The organization bears the full cost of investigation, remediation, and regulatory penalties.
— American Bar Association, Business Law Today
URL: https://www.americanbar.org/groups/business_law/resources/business-law-today/2021-november/saas-agreements-key-contractual-provisions/
Date: Referenced 2025 in compliance guidance

[STATISTIC]
Penetration testing for compliance-driven custom software assessments costs an additional 10–25% above standard technical assessments "to reflect added documentation and evidence handling."
- HIPAA-driven pentests: $10,000–$50,000
- SOC 2-driven pentests: $5,000–$20,000
- PCI DSS-driven pentests: $12,000–$25,000
— Deepstrike / SoftwareSecured
URL: https://deepstrike.io/blog/penetration-testing-cost
Date: 2026

---

## Section 5: AI-Generated Code Security Concerns

[STATISTIC]
"AI-generated code introduces security vulnerabilities in 45% of cases." The study analyzed 80 curated coding tasks across more than 100 large language models (LLMs).
— Veracode 2025 GenAI Code Security Report
URL: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
Date: July 30, 2025

[STATISTIC]
Java-based AI-generated code had the highest security failure rate at 72%; Python, C#, and JavaScript logged failure rates between 38% and 45%.
— Veracode 2025 GenAI Code Security Report
URL: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
Date: July 30, 2025

[STATISTIC]
"62% of AI-generated code solutions contain design flaws or known security vulnerabilities" — citing arxiv.org/abs/2502.11844.
— Andrew Stiefel, Endor Labs, Cloud Security Alliance
URL: https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code
Date: July 9, 2025

[STATISTIC]
"24% of production code is now written by AI tools (29% in the US), and 69% of organizations have found AI-introduced vulnerabilities."
— Baytechconsulting.com (citing Veracode and IBM data)
URL: https://www.baytechconsulting.com/blog/ai-vibe-coding-security-risk-2025
Date: 2025

[STATISTIC]
"63% of breached organizations lacked AI governance policies, and shadow AI added $670,000 to breach costs."
— IBM 2025 Cost of a Data Breach Report (cited in Baytechconsulting.com)
URL: https://www.baytechconsulting.com/blog/ai-vibe-coding-security-risk-2025
Date: 2025

[FACT]
AI coding assistants identify four primary failure modes: insecure pattern repetition (reproducing SQL injection patterns from training data), security-ignorant optimization (choosing `eval()` over safe alternatives), missing control omission (skipping authorization checks when prompts don't specify them), and subtle logic errors (role-checking code that fails with multi-role users).
— Andrew Stiefel, Endor Labs, Cloud Security Alliance
URL: https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code
Date: July 9, 2025

[QUOTE]
"Attackers aren't reinventing playbooks, they're speeding them up with AI."
— Mark Hughes, Global Managing Partner for Cybersecurity Services, IBM
URL: https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed
Date: February 25, 2026

[STATISTIC]
IBM 2026 X-Force Threat Intelligence Index reports a 44% increase in attacks exploiting public-facing applications, driven by "missing authentication controls and AI-enabled vulnerability discovery."
— IBM X-Force
URL: https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed
Date: February 25, 2026

[STATISTIC]
Vulnerability exploitation became "the leading cause of attacks, accounting for 40% of incidents observed by X-Force in 2025."
— IBM X-Force Threat Intelligence Index 2026
URL: https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed
Date: February 25, 2026

[STATISTIC]
IBM X-Force documents a "nearly 4X increase in large supply chain or third-party compromises since 2020, mainly driven by attackers exploiting trust relationships and CI/CD automation across development workflows and SaaS integrations."
— IBM X-Force Threat Intelligence Index 2026
URL: https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed
Date: February 25, 2026

[STATISTIC]
"AI-generated code is now the cause of one in five breaches, and AI-generated code introduces 15–18% more security vulnerabilities than human-written code."
— IT Pro (Emma Woollacott)
URL: https://www.itpro.com/software/development/ai-generated-code-is-fast-becoming-the-biggest-enterprise-security-risk-as-teams-struggle-with-the-illusion-of-correctness
Date: February 5, 2026

---

## Section 6: Regulated Industry Perspectives

### Government / Public Sector

[FACT]
FedRAMP 20x replaces manual System Security Plans with continuous validation via Key Security Indicators (KSIs), but "moving faster comes at the expense of universal, cross-platform utility — creating new technical and financial debt."
— Irina Denisenko (CEO, Knox) and Carrie Lee (former CPO and Deputy CIO, Department of Veterans Affairs)
URL: https://www.nextgov.com/ideas/2026/02/navigating-fedramp-20x-and-continuous-compliance-imperative/411300/
Date: February 2026

[FACT]
Mission-specific custom environments such as the "US Marine Corps Operation Stormbreaker software factory" and "DHS ICE Cloud" enable rapid deployment but "create fragmentation" and new technical and financial debt.
— Irina Denisenko and Carrie Lee, Nextgov/FCW
URL: https://www.nextgov.com/ideas/2026/02/navigating-fedramp-20x-and-continuous-compliance-imperative/411300/
Date: February 2026

[FACT]
Obtaining government ATO "will often take hundreds, if not thousands, of hours from your most senior engineers, plus IT, security, and legal."
— Ad Hoc / StackArmor
URL: https://adhoc.team/ato/
Date: 2025

### Healthcare

[STATISTIC]
"Compromised credentials account for 34% of breaches, and SaaS identities are one of the most common entry points into healthcare environments."
— Grip Security
URL: https://www.grip.security/2025-hipaa-security-rule-requirements
Date: 2025

### Cross-Sector

[STATISTIC]
Verizon's 2025 Data Breach Investigations Report analyzed over 22,000 security incidents, including 12,195 confirmed data breaches. "Third-party involvement in breaches has doubled to 30%, and exploitation of vulnerabilities has surged by 34%."
— Verizon Business
URL: https://www.verizon.com/about/news/2025-data-breach-investigations-report
Date: April 2025

[STATISTIC]
"60% of breaches involved the human element" per the Verizon 2025 DBIR, with "credential abuse (22%) and exploitation of vulnerabilities (20%)" as the leading initial attack vectors.
— Verizon Business
URL: https://www.verizon.com/about/news/2025-data-breach-investigations-report
Date: April 2025

[STATISTIC]
"75% of technology decision-makers will see their technical debt rise to a moderate or high level of severity by 2026" due to "rapid development of AI solutions, which are adding complexity to IT landscapes."
— Forrester 2025 Technology and Security Predictions
URL: https://investor.forrester.com/news-releases/news-release-details/forresters-technology-security-predictions-2025-tech-leaders/
Date: 2025

[STATISTIC]
"79% of technology decision-makers in US organizations reported an increase in their software costs over the past year."
— Kate Leggett, VP Principal Analyst, and Liz Herbert, VP Principal Analyst, Forrester
URL: https://www.forrester.com/blogs/predictions-2025-enterprise-software/
Date: 2025

[STATISTIC]
Global spending on information security and risk management is forecasted to reach $213 billion in 2025 and $244.2 billion in 2026, a 13.3% year-over-year increase.
— Gartner (cited in National CIO Review)
URL: https://nationalcioreview.com/articles-insights/gartner-forecasts-213-billion-in-2025-security-spending/
Date: 2025

---

## Key Takeaways

1. **Certification costs create a multi-year moat.** Achieving SOC 2 Type 2 costs $75,000–$200,000; ISO 27001 costs $50,000–$200,000; FedRAMP costs $250,000–$1.5 million. These are not one-time investments — each requires annual audits, continuous monitoring, and dedicated security personnel. Custom-built software must absorb every dollar of this cost independently.

2. **AI-generated code degrades the security baseline of custom builds.** Veracode's research across 100+ LLMs found that 45% of AI-generated code choices are insecure, with Java failure rates at 72%. With 24% of production code now AI-generated, enterprises building custom software with agentic tools are systematically introducing vulnerabilities that SaaS vendors with established security programs are not.

3. **Regulated industries face legal — not just financial — barriers.** Healthcare organizations must sign BAAs with every custom software vendor-as-developer, maintain NIST-compliant encryption (AES-256, TLS 1.2+), and now comply with materially strengthened 2025 HIPAA Security Rule requirements. Financial services firms must satisfy eight or more federal regulatory bodies simultaneously. Government agencies require ATOs that can take 6–18 months and cost seven figures for custom deployments.

4. **Liability transfers asymmetrically.** When a certified SaaS vendor is at fault for a breach caused by their negligence, enterprises increasingly win uncapped liability and indemnification. When custom software has a vulnerability, the organization holds 100% of the liability with no contractual backstop. The IBM 2025 breach cost average of $10.22 million in the U.S. makes this asymmetry consequential.

5. **The shared responsibility model cuts both ways.** Gartner's finding that 99% of cloud failures are customer-caused means SaaS does not eliminate security risk — it partitions it. Enterprises replacing SaaS with custom builds move from managing configuration risk to owning platform, application, and infrastructure security simultaneously. The Obsidian Security-documented 300% year-over-year surge in SaaS compromise incidents reflects the configuration risk; custom software adds code-level and infrastructure-level risk on top.

---

## Sources

- [SOC 2 Certification 2025: Auditor, Cost & Timeline Guide — dsalta.com](https://www.dsalta.com/resources/articles/soc-2-certification-2025-auditor-cost-timeline-guide)
- [ISO 27001 Certification Cost Breakdown 2025 — Rhymetec](https://rhymetec.com/iso-27001-certification-cost-breakdown-2025/)
- [ISO 27001 Certification Cost in 2026 — StrongDM](https://www.strongdm.com/blog/iso-27001-certification-cost)
- [How Much Does FedRAMP Certification Cost? — Workstreet](https://www.workstreet.com/blog/fedramp-certification-cost)
- [What Is an ATO? A Guide to Authority to Operate — Workstreet](https://www.workstreet.com/blog/what-is-an-ato)
- [How Much Does It Cost to Get FedRAMP Compliant and Obtain an ATO? — StackArmor](https://stackarmor.com/how-much-does-it-cost-to-get-fedramp-compliant-and-obtain-an-ato/)
- [Navigating FedRAMP 20x and the Continuous Compliance Imperative — Nextgov/FCW](https://www.nextgov.com/ideas/2026/02/navigating-fedramp-20x-and-continuous-compliance-imperative/411300/)
- [8 Top SaaS Security Certifications for SaaS Providers (2026) — BD Emerson](https://www.bdemerson.com/article/top-saas-security-certifications)
- [2025 HIPAA Security Rule Requirements — Grip Security](https://www.grip.security/2025-hipaa-security-rule-requirements)
- [HIPAA Compliance for SaaS — HIPAA Journal](https://www.hipaajournal.com/hipaa-compliance-for-saas/)
- [HIPAA Compliant Software Requirements for Healthcare in 2025 — ULAM Labs](https://www.ulam.io/blog/hipaa-compliant-software-requirements-for-healthcare-in-2025---what-engineering-teams-need-to-know)
- [Fintech Data Storage: Compliance Checklist 2025 — Phoenix Strategy Group](https://www.phoenixstrategy.group/blog/fintech-data-storage-compliance-checklist-2025)
- [2025 FINRA Annual Regulatory Compliance Oversight Report — ACA Group](https://www.acaglobal.com/industry-insights/2025-finra-annual-regulatory-compliance-oversight-report-2/)
- [Fintech Laws and Regulations 2025 USA — Global Legal Insights](https://www.globallegalinsights.com/practice-areas/fintech-laws-and-regulations/usa/)
- [SaaS Security Shared Responsibility Model — Obsidian Security (Scott Young)](https://www.obsidiansecurity.com/blog/saas-security-shared-responsibility-model)
- [The State of SaaS Security Report 2025 — Cloud Security Alliance / Valence Security](https://cloudsecurityalliance.org/artifacts/state-of-saas-security-report-2025)
- [Understanding the Shared Responsibility Model in SaaS — Valence Security](https://www.valencesecurity.com/resources/blogs/understanding-the-shared-responsibility-model-in-saas)
- [Uncapping Risk: The Growing Burden of Data Privacy Liability in Tech Contracts — IAPP (Irina Beschieriu)](https://iapp.org/news/a/uncapping-risk-the-growing-burden-of-data-privacy-liability-in-tech-contracts)
- [Penetration Testing Cost 2026 — Deepstrike](https://deepstrike.io/blog/penetration-testing-cost)
- [Veracode 2025 GenAI Code Security Report](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)
- [AI-Generated Code Poses Major Security Risks in Nearly Half of All Development Tasks — Veracode / BusinessWire](https://www.businesswire.com/news/home/20250730694951/en/AI-Generated-Code-Poses-Major-Security-Risks-in-Nearly-Half-of-All-Development-Tasks-Veracode-Research-Reveals)
- [Understanding Security Risks in AI-Generated Code — Andrew Stiefel, Endor Labs, CSA](https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code)
- [AI-Generated Code Is Fast Becoming the Biggest Enterprise Security Risk — IT Pro (Emma Woollacott)](https://www.itpro.com/software/development/ai-generated-code-is-fast-becoming-the-biggest-enterprise-security-risk-as-teams-struggle-with-the-illusion-of-correctness)
- [AI Vibe Coding: Why 45% of AI-Generated Code Is a Security Risk — Baytechconsulting.com](https://www.baytechconsulting.com/blog/ai-vibe-coding-security-risk-2025)
- [IBM 2026 X-Force Threat Intelligence Index — IBM Newsroom (Mark Hughes)](https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed)
- [Verizon 2025 Data Breach Investigations Report](https://www.verizon.com/about/news/2025-data-breach-investigations-report)
- [Verizon 2025 DBIR: Third-Party Risk Explosion — Kiteworks](https://www.kiteworks.com/third-party-risk/verizon-2025-dbir-third-party-risk-explosion/)
- [SaaS Security Risks 2026 — Red Sentry](https://redsentry.com/resources/blog/saas-security-risks-2026-misconfigurations-compliance-gaps-and-data-breach-prevention)
- [Forrester Technology and Security Predictions 2025](https://investor.forrester.com/news-releases/news-release-details/forresters-technology-security-predictions-2025-tech-leaders/)
- [Predictions 2025: Enterprise Software — Kate Leggett and Liz Herbert, Forrester](https://www.forrester.com/blogs/predictions-2025-enterprise-software/)
- [Gartner Forecasts $213 Billion in 2025 Security Spending — National CIO Review](https://nationalcioreview.com/articles-insights/gartner-forecasts-213-billion-in-2025-security-spending/)
- [Why 2025's Agentic AI Boom Is a CISO's Worst Nightmare — CSO Online](https://www.csoonline.com/article/4132860/why-2025s-agentic-ai-boom-is-a-cisos-worst-nightmare.html)
- [ATO Authorization to Operate Field Guide — Ad Hoc](https://adhoc.team/ato/)
