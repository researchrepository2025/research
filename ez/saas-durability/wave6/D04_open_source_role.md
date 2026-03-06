# D04: The Open-Source Role in the Build-vs-Buy-SaaS Equation Under Agentic Coding

**Research Wave:** Wave 6 — Open-Source Ecosystem
**Date Compiled:** March 2026
**Scope:** How open-source software, combined with agentic coding, shifts the enterprise build-vs-buy calculus for SaaS

---

## Executive Summary

Open-source software now underlies virtually all commercial codebases — Black Duck's 2025 Open Source Security and Risk Analysis (OSSRA) found that 97% of commercial applications contain open-source components, with an average of 911 open-source components per application. Enterprise adoption of open-source alternatives to major SaaS categories (ERP, CRM, project management, collaboration) is accelerating: the open-source ERP market is projected to reach $2.85 billion in 2025 and grow at 10.05% CAGR. Agentic coding is amplifying this dynamic by radically lowering the assembly cost of open-source components into production-grade applications — Retool's February 2026 survey of 817 enterprise builders found 35% have already replaced at least one SaaS tool with a custom build. However, the thesis faces hard structural limits: 86% of applications with open-source components contain vulnerable dependencies, only 34% of enterprises have a defined open-source strategy, and open-source AI models now account for just 13% of enterprise AI workloads (down from 19% six months prior), suggesting that performance gaps and governance deficits continue to push mission-critical workloads toward closed-source vendors.

---

## Section 1: Open-Source Alternatives to Major SaaS Categories — Maturity Assessment

### ERP

[STATISTIC]
"The Open Source ERP Market is expected to reach USD 2.85 billion in 2025 and grow at a CAGR of 10.05% to reach USD 4.60 billion by 2030."
— Mordor Intelligence
URL: https://www.mordorintelligence.com/industry-reports/open-source-erp-market
Date: 2025

[STATISTIC]
"Open source ERP adoption grew 32% globally in 2026 due to rising license costs of proprietary ERPs."
— DevDiligent
URL: https://devdiligent.com/blog/top-open-source-erp-business-software-2026/
Date: 2026

[DATA POINT] Odoo — leading open-source ERP platform:
- 16+ million users globally as of Q1 2026
- 170,000+ active enterprise customers
- €650M revenue in 2025; projected €800M+ in 2026
- 5.77% of global ERP market; 12–15% of SME ERP segment
- 5-year CAGR: 20–25%
- 5-year TCO for 50 users: $315,000–$387,000 (up to 65% lower than SAP/Oracle)
- 60% of core apps AI-enabled
URL: https://www.appverticals.com/blog/odoo-erp-adoption-statistics/
Date: 2026

[FACT] Odoo implementation timeline: 2–4 months for 10–25 users; 6–12 months for 100+ users. Compared to 12–24 months for SAP.
URL: https://www.appverticals.com/blog/odoo-erp-adoption-statistics/
Date: 2026

### CRM

[FACT] Twenty (twentyhq) is "building a modern alternative to Salesforce, powered by the community." The project has "more than 300 contributors in the last year and 20,000 stars on GitHub." Licensed under AGPLv3.
— TechCrunch
URL: https://techcrunch.com/2024/11/18/twenty-is-building-an-open-source-alternative-to-salesforce/
Date: November 2024

[FACT] Self-hosted and open-source CRMs "allow companies to host on their own servers, tweak the code to fit their workflows, keep customer data in-house, and avoid vendor lock-in with no surprise pricing hikes."
URL: https://growcrm.io/2026/01/04/top-20-open-source-self-hosted-crms-in-2025/
Date: January 2026

### Project Management

[FACT] Plane is "an open-source Jira, Linear, Monday, and ClickUp alternative" and "a modern project management platform to manage tasks, sprints, docs, and triage."
URL: https://github.com/makeplane/plane
Date: 2025

### Collaboration / Productivity

[FACT] Nextcloud, partnering with Ionos (a German data center provider), launched Nextcloud Workspace as "a super easy-to-use SaaS product, but it is completely European" — an open-source alternative to Microsoft 365. Driven by digital sovereignty demand in 2025.
— Computerworld
URL: https://www.computerworld.com/article/4064116/a-european-alternative-to-m365-nextcloud-looks-to-capitalize-on-digital-sovereignty-interest.html
Date: 2025

[FACT] Mattermost is an "open-source, self-hosted communication and collaboration platform offering secure chat, file sharing, and project coordination tools, helping organizations replace tools like Slack with a fully customizable solution they can host on their own servers."
URL: https://growcrm.io/2026/01/04/top-20-open-source-self-hosted-crms-in-2025/
Date: January 2026

### Open-Source Maturity Summary Table

| SaaS Category | Leading Open-Source Alternative | Maturity Signal |
|---|---|---|
| ERP | Odoo, ERPNext | 16M+ Odoo users; €650M revenue; 10% CAGR market |
| CRM | Twenty, SuiteCRM | 20K GitHub stars; 300+ contributors (Twenty) |
| Project Management | Plane, OpenProject | Direct Jira/Linear replacement feature parity claimed |
| Collaboration / Chat | Mattermost, Rocket.Chat | Enterprise self-hosting available; EU sovereignty driver |
| Cloud Storage / Office | Nextcloud | Active EU government/enterprise deployments |
| Developer Tools | GitLab CE | Mature; used by enterprises as GitHub alternative |
| Backend-as-a-Service | Supabase, PocketBase | Supabase: open-source Firebase alternative on PostgreSQL |

---

## Section 2: Agentic Coding + Open Source as a SaaS Replacement Strategy

### The Retool 2026 Build vs. Buy Signal

[STATISTIC]
"35% of teams have already replaced at least one SaaS tool with a custom-built solution."
— Retool 2026 Build vs. Buy Report (817 enterprise builders surveyed, late 2025)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"78% expect to build more custom internal tools in 2026."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"60% of builders have created tools outside IT oversight in the past year."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"93% use LLMs to code, build, or automate at work."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### SaaS Categories Most Exposed to Custom Build Replacement

[DATA POINT] SaaS categories already being replaced with custom builds (Retool 2026 survey):
- Workflow automation: 35%
- Internal admin tools: 33%
- BI tools: 29%
- CRM and form builders: 25%
- Project management: 23%
- Customer support: 21%
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### The "Buy-to-Build" Framework (Named Expert)

[QUOTE]
"Markets are not repricing software because artificial intelligence exists. They are repricing software because control is shifting."
— Sumeet Chabria, CEO & Founder, ThoughtLinks (strategic advisory firm for C-suite in banking and capital markets; Carnegie Mellon Heinz College executive education faculty)
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

[QUOTE]
"The real danger is not that code can be generated. The danger is that it can be generated faster than an enterprise can govern it."
— Sumeet Chabria, CEO & Founder, ThoughtLinks
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

[FACT] Chabria's "Buy-to-Build" framework classifies SaaS into five buckets. "Bucket C" (regulated scaffolding, orchestration, control plane for digital labor) is categorized as durable if it provides "compliance-grade controls, deep integration into systems of record, auditability, resilience."
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

### Agentic AI Market Size

[STATISTIC]
"The global agentic AI market reached $7.6 billion in 2025, up from $5.4 billion in 2024, with long-term projections showing the market hitting $196.6 billion by 2034."
URL: https://aimultiple.com/agentic-frameworks
Date: 2026

[STATISTIC]
"By 2026, 40% of enterprise applications will feature task-specific AI agents, up from less than 5% in 2025."
— Gartner (cited in source)
URL: https://www.intelligentcio.com/north-america/2025/12/24/enterprise-ai-and-agentic-software-trends-shaping-2026/
Date: December 2025

### Developer Productivity Signal

[DATA POINT] One CTO reported "nearly 90% AI-generated code (via Cursor/Claude), up from 10–15% year prior."
— a16z "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025"
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

[STATISTIC]
"About half of builders who have shipped production software report saving six or more hours per week."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

---

## Section 3: Open-Source AI Models Enabling Custom Software

### Market Share of Open vs. Closed AI Models in Enterprise

[STATISTIC]
"13% of AI workloads currently use open-source models, down from 19% six months prior."
— Menlo Ventures 2025 Mid-Year LLM Market Update
URL: https://menlovc.com/perspective/2025-mid-year-llm-market-update/
Date: Mid-2025

[STATISTIC]
"87% of enterprise workloads now run on closed-source models."
— Menlo Ventures 2025 Mid-Year LLM Market Update
URL: https://menlovc.com/perspective/2025-mid-year-llm-market-update/
Date: Mid-2025

[STATISTIC]
"Open-source models trail frontier closed-source alternatives by 9–12 months in performance."
— Menlo Ventures 2025 Mid-Year LLM Market Update
URL: https://menlovc.com/perspective/2025-mid-year-llm-market-update/
Date: Mid-2025

[STATISTIC] Closed-source enterprise AI market share (Menlo Ventures):
- Anthropic: 32%
- OpenAI: 25%
- Google: 20%
- Meta Llama (open-source): 9%
URL: https://menlovc.com/perspective/2025-mid-year-llm-market-update/
Date: Mid-2025

[QUOTE] One enterprise respondent stated: "Currently, 100% of our production workloads are running on closed-source models. We initially started with Llama and DeepSeek for POCs, but they couldn't keep up with the performance of closed-source over time."
— Menlo Ventures 2025 Mid-Year LLM Market Update
URL: https://menlovc.com/perspective/2025-mid-year-llm-market-update/
Date: Mid-2025

### Meta Llama Adoption Data

[STATISTIC]
"Llama has become the most adopted model, with more than 650 million downloads of Llama and its derivatives."
— AI at Meta
URL: https://ai.meta.com/blog/future-of-ai-built-with-llama/
Date: 2025

[STATISTIC]
"Fortune 500 companies piloting Llama models maintained at 50% throughout 2024 and 2025."
— Menlo Ventures / Quantumrun Foresight (Code Llama Statistics)
URL: https://www.quantumrun.com/consulting/code-llama-statistics/
Date: 2026

[FACT] Goldman Sachs, AT&T, DoorDash, and Shopify deployed Llama-based solutions for customer support automation and code generation.
URL: https://www.quantumrun.com/consulting/code-llama-statistics/
Date: 2026

[FACT] "Llama 4's April 2025 launch 'underwhelmed in real-world settings'" according to Menlo Ventures' mid-year update.
URL: https://menlovc.com/perspective/2025-mid-year-llm-market-update/
Date: Mid-2025

### Mistral AI

[FACT] "Both the base and instruction fine-tuned versions of Mistral Large 3 are available under the Apache 2.0 license, providing a strong foundation for further customization across the enterprise and developer communities."
URL: https://mistral.ai/news/mistral-3
Date: 2025

[FACT] Red Hat AI Inference Server, built on vLLM (60,000+ GitHub stars; 1,700+ contributors), "lets customers run open source LLMs in production environments on premises or in the cloud."
URL: https://developers.redhat.com/articles/2025/12/02/run-mistral-large-3-ministral-3-vllm-red-hat-ai
Date: December 2025

### Enterprise Open-Source AI Use Cases

[FACT] Open-source AI models address three primary enterprise needs (per Red Hat Developer, January 2026):
1. Data Sovereignty: Required in highly regulated sectors (telecommunications, banking) for on-premises deployment
2. Cost Control: Reduced API expenses and predictable infrastructure costs
3. Air-Gapped Deployments: No external connectivity or API key dependencies
URL: https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025
Date: January 7, 2026

[FACT] Open source AI/ML adoption increased from 35% to 40% (5 percentage-point rise since 2024) across enterprise organizations surveyed.
— Linux Foundation / Canonical 2025 State of Global Open Source (851 respondents)
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

---

## Section 4: Enterprise Adoption of Open-Source Alternatives to SaaS

### Overall Open-Source Enterprise Adoption Rates

[STATISTIC] Enterprise open-source adoption rates by category (Linux Foundation World of Open Source 2025 Survey, 851 global respondents):
- Operating systems: 55%
- Cloud and container technologies: 49%
- Web and application development: 46%
- Database and data management: 45%
- Development operations: 45%
- AI and machine learning: 40%
URL: https://www.linuxfoundation.org/blog/the-state-of-open-source-software-in-2025
Date: 2025

[STATISTIC]
"96% of organizations reported either increasing or maintaining their use of open source software in the past year. 26% significantly increased their adoption."
— Open Source Initiative, Key insights from the 2025 State of Open Source Report (author: Nick Vidal)
URL: https://opensource.org/blog/key-insights-from-the-2025-state-of-open-source-report
Date: April 10, 2025

[STATISTIC] Reported organizational benefits of open-source software (Linux Foundation 2025 Survey):
- Improves productivity: 86%
- Reduces vendor lock-in: 84%
- Lowers software ownership costs: 84%
- Facilitates innovation: 82%
- Improves software quality: 79%
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

### Digital Sovereignty as an Adoption Driver

[FACT] European enterprises are adopting open-source alternatives partly due to digital sovereignty concerns in 2025. However, "less than 5% say they will stop using services from global public cloud vendors, and despite all the hype, Europe is not abandoning the US providers in droves."
— Computerworld
URL: https://www.computerworld.com/article/4064116/a-european-alternative-to-m365-nextcloud-looks-to-capitalize-on-digital-sovereignty-interest.html
Date: 2025

### Economic Value of Open-Source Ecosystem

[STATISTIC]
"Supply-side value of widely-used open source software: $4.15 billion. Demand-side value: $8.8 trillion. Firms would need to spend 3.5 times more on software than they currently do if OSS did not exist."
— Frank Nagle, Manuel Hoffmann, and Yanuo Zhou, Harvard Business School Working Paper No. 24-038
URL: https://www.hbs.edu/faculty/Pages/item.aspx?num=65230
Date: January 2024

[STATISTIC]
"96% of the demand-side value is created by only 5% of OSS developers."
— Harvard Business School Working Paper No. 24-038
URL: https://www.hbs.edu/faculty/Pages/item.aspx?num=65230
Date: January 2024

---

## Section 5: The "Agentic Coding Assembles Open-Source Components" Thesis

### The Assembly Thesis Stated

[FACT] The build-vs-buy instinct has shifted: Retool's 2026 data shows 35% of enterprise builders already replaced at least one SaaS tool, but it should be noted that "roughly three-quarters of AI use cases now run on vendor products, not internal projects" — suggesting the majority of AI workloads still favor purchase over build.
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[FACT] Microsoft Agent Framework "builds on Semantic Kernel and AutoGen, consolidating their strengths to give developers one foundation to move from experimentation to enterprise deployment." It supports both Agent Orchestration (LLM-driven) and Workflow Orchestration (business-logic driven, deterministic).
URL: https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/
Date: 2025

[FACT] OpenHands is "open source, model-agnostic" and "can be deployed in isolated Docker or Kubernetes environments, self-hosted or cloud," enabling enterprise teams to build and orchestrate custom software agents without SaaS dependency.
URL: https://openhands.dev/
Date: 2025

[FACT] Cline is "a fully open-source, editor-native coding agent purpose-built for real development workflows, running locally, planning multi-step tasks, editing files, and executing terminal commands with permission."
URL: https://cline.bot/
Date: 2025

[FACT] Goose, released by fintech company Block, is "an open-source AI agent framework that can go beyond coding and is designed to be extensible and run entirely locally" — enabling enterprises to build custom workflows without external API dependencies.
URL: https://cline.bot/blog/top-11-open-source-autonomous-agents-frameworks-in-2025
Date: 2025

### Agentic Framework Adoption

[FACT] Top open-source agentic AI frameworks in use (2026 edition): LangChain, LangGraph, LlamaIndex, CrewAI, Semantic Kernel, AutoGen, Microsoft Agent Framework.
URL: https://aimultiple.com/agentic-frameworks
Date: 2026

[FACT] Composio "simplifies agent interaction with external services by centralizing authentication and execution, enabling seamless integration across diverse tools" — acting as an open-source orchestration layer over both SaaS APIs and custom services.
URL: https://cline.bot/blog/top-11-open-source-autonomous-agents-frameworks-in-2025
Date: 2025

### Shifting AI Development Patterns

[FACT] A16z CIO survey (2025) found: enterprises are "moving from building custom AI applications to purchasing third-party solutions as the ecosystem matures." "We've seen a marked shift towards buying third party applications over the last twelve months." Over 90% of respondents were testing third-party customer support applications.
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

[FACT] Fine-tuning open-source models is declining: "Instead of taking the training data and parameter-efficient fine-tuning, you just dump it into a long context." Companies now prefer prompt engineering for similar results at lower costs.
— A16z CIO Survey 2025
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

---

## Section 6: Limitations — Support, Security, and Compliance for Open Source in Enterprise

### Security Vulnerabilities (Black Duck OSSRA 2025)

[STATISTIC]
"97% of commercial codebases contain open source."
— Black Duck Open Source Security and Risk Analysis (OSSRA) 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[STATISTIC]
"86% of applications examined contained vulnerable open source components."
— Black Duck OSSRA 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[STATISTIC]
"81% had high or critical-risk vulnerabilities."
— Black Duck OSSRA 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[STATISTIC]
"90% contain components more than 10 versions behind the current release."
— Black Duck OSSRA 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[STATISTIC]
"79% contain components with no development activity in the last 24 months."
— Black Duck OSSRA 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[STATISTIC]
"64% of open source components in applications are transitive dependencies — most near impossible to locate or track without automated tooling."
— Black Duck OSSRA 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[STATISTIC]
"77% of all OSS vulnerabilities are found in transitive dependencies."
— Quandary Peak Research, December 2025
URL: https://quandarypeak.com/2025/12/unseen-costs-and-latent-risks-of-oss/
Date: December 2025

### Supply Chain Attack Volume

[STATISTIC]
"700,000+ malicious packages discovered since 2019. Attack numbers doubled in 2024."
— Quandary Peak Research, December 2025
URL: https://quandarypeak.com/2025/12/unseen-costs-and-latent-risks-of-oss/
Date: December 2025

### License and Legal Compliance Risk

[STATISTIC]
"56% of scanned codebases contained OSS license conflicts, typically between a permissive license and a strong copyleft license like the GPL."
— Black Duck OSSRA 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[STATISTIC]
"33% contained components with no discernible license, placing the user in a state of legal ambiguity."
— Black Duck OSSRA 2025
URL: https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
Date: 2025

[FACT] "Major OSS license violations resulted in settlements exceeding $1,000,000, including the Orange v. Entr'ouvert case with damages of €860,000+."
— Quandary Peak Research, December 2025
URL: https://quandarypeak.com/2025/12/unseen-costs-and-latent-risks-of-oss/
Date: December 2025

### Governance Gaps

[STATISTIC]
"Only 34% of enterprises have defined a clear open source strategy (up just 2% year-over-year)."
— Linux Foundation / Canonical State of Global Open Source 2025 (851 respondents)
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

[STATISTIC]
"Only 26% of enterprises have implemented Open Source Program Offices (OSPOs). Large enterprises are 2.4x more likely to have an OSPO (39% vs. 16% for smaller organizations)."
— Linux Foundation State of Open Source 2025
URL: https://www.linuxfoundation.org/blog/the-state-of-open-source-software-in-2025
Date: 2025

[STATISTIC]
"Only 31% use automated security testing tools; 28% manually review source code; 36% evaluate direct dependencies."
— Canonical / Linux Foundation State of Global Open Source 2025
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

### Enterprise Support Expectations vs. Reality

[STATISTIC]
"71% of organizations expect response times under 12 hours for critical OSS production issues."
— Linux Foundation State of Global Open Source 2025
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

[STATISTIC]
"54% view paid support as essential for mission-critical workloads. In manufacturing: 97%; financial services: 96%; government: 92%; IT: 91%."
— Linux Foundation / Canonical State of Global Open Source 2025
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

[STATISTIC]
"53% expect long-term support guarantees; 47% expect rapid security patching in production."
— Linux Foundation / Canonical State of Global Open Source 2025
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

### Hidden Total Cost of Ownership

[STATISTIC]
"58% of organizations reported lower software ownership costs, and 63% cited higher productivity as a direct benefit of adopting open source."
— OpenLogic 2025 State of Open Source Report
URL: https://www.openlogic.com/resources/state-of-open-source-report
Date: 2025

[DATA POINT] Sample 5-year TCO for a single 3-million-line-of-code OSS framework (Quandary Peak Research):
- Bug fixing: $20,640/year
- OSS obligations: $1,720/year
- Legal checks: $1,038/year
- Compliance scanning: $1,500/year
- Total 5-year TCO: ~$135,498 (including $11,000 setup)
URL: https://quandarypeak.com/2025/12/unseen-costs-and-latent-risks-of-oss/
Date: December 2025

### Maintainer Concentration Risk

[FACT] "17% of the top 50 non-npm projects have one developer, and 40% have one or two developers who accounted for at least 80% of the commits."
— Black Duck OSSRA 2025 / Quandary Peak Research
URL: https://quandarypeak.com/2025/12/unseen-costs-and-latent-risks-of-oss/
Date: December 2025

### Deloitte Expert Position: SaaS Replacement Will Be Slow

[QUOTE]
"Traditional SaaS disruption will take 'at least five years or more' to materialize. Large SaaS providers have 'large footprints across complex workflows that will likely be hard to supplant.'"
— Deloitte Center for Technology, Media & Telecommunications (David Jarvis, Sayantani Mazumder, Girija Krishnamurthy, Gopal Srinivasan, China Widener, Gillian Crossan)
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

[STATISTIC]
"By 2030, 35% of point-product SaaS tools will be replaced by AI agents or absorbed within larger agent ecosystems."
— Deloitte TMT Predictions 2026
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

[STATISTIC]
"By 2030, at least 40% of enterprise SaaS spend will shift toward usage-, agent-, or outcome-based pricing."
— Deloitte TMT Predictions 2026
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

---

## Section 7: Expert Opinion Camps

### Camp A: Open Source + Agentic Coding Will Meaningfully Erode SaaS (Replacement Thesis)

**Sumeet Chabria, CEO & Founder, ThoughtLinks (banking/capital markets C-suite advisory; Carnegie Mellon Heinz faculty)**
- Core argument: "Control is shifting" — agentic AI allows enterprises to build governed, custom workflows that previously required SaaS. The interface layer of SaaS (dashboards, per-seat models) is being bypassed by autonomous agents.
- Evidence cited: ~$285B single-day software sector rout (Feb 3, 2026); $1T+ erased from software stocks within a week (Forrester estimate).
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

**Retool (2026 Report Framing)**
- Core argument: "As large language models have improved and AI-assisted development has become widespread, enterprises can now build custom tools in days rather than months."
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

### Camp B: Open Source Limitations and Governance Deficits Protect SaaS Durability

**Deloitte Center for TMT (Jarvis, Mazumder, Krishnamurthy, Srinivasan, Widener, Crossan)**
- Core argument: "SaaS is far from dead; the winners will combine the agility of AI agents with the reliability of SaaS." Large SaaS providers have "large footprints across complex workflows that will likely be hard to supplant." Replacement will take "at least five years or more."
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

**Menlo Ventures (2025 Mid-Year LLM Market Update)**
- Core argument: Open-source AI models' share of enterprise production workloads fell from 19% to 13% in six months — performance gaps versus frontier closed-source models are driving consolidation toward vendors. "Builders prioritize performance over cost, choosing frontier models despite cheaper alternatives."
URL: https://menlovc.com/perspective/2025-mid-year-llm-market-update/
Date: Mid-2025

**a16z (Enterprise CIO Survey 2025)**
- Core argument: "We've seen a marked shift towards buying third party applications over the last twelve months." Regulated industries maintain higher build rates due to compliance requirements. Switching costs rising as agentic workflows deepen integration.
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

### Camp C: Hybrid — Open Source Lowers the Floor, But Enterprise Grade Still Requires Paid Layer

**Linux Foundation / Canonical (State of Global Open Source 2025)**
- Core argument: "The most significant IT cost savings emerge when organizations combine free software innovation with enterprise-grade support, governance, and active engagement." 54% of enterprises say paid OSS support is essential for mission-critical workloads; 71% expect sub-12-hour SLA response.
URL: https://canonical.com/blog/state-of-global-open-source-2025
Date: 2025

---

## Key Takeaways

- **Open-source components are already inside virtually all enterprise software**: 97% of commercial codebases contain open-source components (Black Duck OSSRA 2025), giving the ecosystem foundational leverage — but this ubiquity also means the security and governance liability is already present regardless of build/buy decisions.

- **Agentic coding is shifting the assembly cost curve, but not eliminating it**: Retool's 2026 survey finds 35% of enterprises have replaced at least one SaaS tool with a custom build, but 93% still use LLMs primarily for code snippets within larger projects (not end-to-end applications), and only 8% deploy AI-generated code without modification. The "assemble open-source components with AI agents" thesis is early-stage, not mainstream.

- **Open-source AI models are losing ground in production**: Enterprise open-source model share fell from 19% to 13% of AI workloads in six months (Menlo Ventures), with one respondent stating "they couldn't keep up with the performance of closed-source over time." Data sovereignty and on-premise compliance needs represent the strongest remaining pull toward open-source AI.

- **The governance gap is the open-source enterprise's Achilles heel**: Only 34% of enterprises have a defined open-source strategy; only 26% have an OSPO; 56% of codebases have license conflicts; and 86% contain vulnerable components. These structural deficits impose real TCO that narrows — but does not eliminate — the cost advantage over commercial SaaS.

- **Mature open-source SaaS alternatives (Odoo, Mattermost, GitLab, Nextcloud, Plane) are accelerating toward enterprise viability, but primarily in the SME and mid-market tier**: Odoo's 65% TCO advantage over SAP/Oracle is significant, and its 20–25% CAGR signals genuine displacement — but the 12–24 month SAP implementation comparison versus 6–12 months for Odoo still implies a non-trivial enterprise integration burden that favors incumbent SaaS vendors for the most complex operational environments.

---

## Sources

1. Black Duck Open Source Security and Risk Analysis (OSSRA) 2025 — https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html
2. Black Duck OSSRA 2026 Report page — https://www.blackduck.com/resources/analyst-reports/open-source-security-risk-analysis.html
3. Quandary Peak Research, "A Multi-faceted Analysis: The Unseen Costs and Latent Risks of Open Source Software" (December 2025) — https://quandarypeak.com/2025/12/unseen-costs-and-latent-risks-of-oss/
4. Linux Foundation, "The State of Open Source Software in 2025" — https://www.linuxfoundation.org/blog/the-state-of-open-source-software-in-2025
5. Linux Foundation / Canonical, "State of Global Open Source 2025" (851 respondents) — https://canonical.com/blog/state-of-global-open-source-2025
6. Open Source Initiative, "Key insights from the 2025 State of Open Source Report" (Nick Vidal, April 10, 2025) — https://opensource.org/blog/key-insights-from-the-2025-state-of-open-source-report
7. OpenLogic, "2025 State of Open Source Report" — https://www.openlogic.com/resources/state-of-open-source-report
8. Retool, "The Build vs. Buy Shift: AI, Shadow IT, and the SaaS Replacement Era" (2026 Build vs. Buy Report, 817 respondents, February 17, 2026) — https://retool.com/blog/ai-build-vs-buy-report-2026
9. BusinessWire, Retool 2026 Build vs. Buy Report Press Release (February 17, 2026) — https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
10. Sumeet Chabria / ThoughtLinks, "Agentic AI Is Repricing SaaS: A Buy-to-Build Framework for CIOs & Investors" — https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
11. Deloitte Center for TMT, "SaaS meets AI agents: Transforming budgets, customer experience, and workforce dynamics" (David Jarvis et al., 2026) — https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
12. Menlo Ventures, "2025 Mid-Year LLM Market Update: Foundation Model Landscape + Economics" — https://menlovc.com/perspective/2025-mid-year-llm-market-update/
13. Andreessen Horowitz (a16z), "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025" — https://a16z.com/ai-enterprise-2025/
14. Harvard Business School Working Paper No. 24-038 (Frank Nagle, Manuel Hoffmann, Yanuo Zhou), "The Value of Open Source Software" (January 2024) — https://www.hbs.edu/faculty/Pages/item.aspx?num=65230
15. Red Hat Developer, "The state of open source AI models in 2025" (January 7, 2026) — https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025
16. Red Hat Developer, "Run Mistral Large 3 & Ministral 3 on vLLM with Red Hat AI" (December 2025) — https://developers.redhat.com/articles/2025/12/02/run-mistral-large-3-ministral-3-vllm-red-hat-ai
17. Meta AI Blog, "The future of AI: Built with Llama" — https://ai.meta.com/blog/future-of-ai-built-with-llama/
18. Mistral AI, "Introducing Mistral 3" — https://mistral.ai/news/mistral-3
19. AppVerticals, "Odoo ERP Market Share & Adoption Statistics 2026" — https://www.appverticals.com/blog/odoo-erp-adoption-statistics/
20. Mordor Intelligence, "Open Source ERP Market" — https://www.mordorintelligence.com/industry-reports/open-source-erp-market
21. DevDiligent, "Top Open Source ERP Business Software 2026" — https://devdiligent.com/blog/top-open-source-erp-business-software-2026/
22. TechCrunch, "Twenty is building an open source alternative to Salesforce" (November 18, 2024) — https://techcrunch.com/2024/11/18/twenty-is-building-an-open-source-alternative-to-salesforce/
23. GitHub, makeplane/plane — https://github.com/makeplane/plane
24. Computerworld, "A European alternative to M365? Nextcloud looks to capitalize on digital sovereignty interest" (2025) — https://www.computerworld.com/article/4064116/a-european-alternative-to-m365-nextcloud-looks-to-capitalize-on-digital-sovereignty-interest.html
25. Microsoft Foundry Blog, "Introducing Microsoft Agent Framework" — https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/
26. OpenHands — https://openhands.dev/
27. Cline, "Top 11 Open-Source Autonomous Agents & Frameworks in 2025" — https://cline.bot/blog/top-11-open-source-autonomous-agents-frameworks-in-2025
28. AIMultiple, "Top 5 Open-Source Agentic AI Frameworks in 2026" — https://aimultiple.com/agentic-frameworks
29. Intelligent CIO North America, "Enterprise AI and agentic software trends shaping 2026" (December 24, 2025) — https://www.intelligentcio.com/north-america/2025/12/24/enterprise-ai-and-agentic-software-trends-shaping-2026/
30. Quantumrun Foresight, "Code Llama Statistics And User Trends [2026]" — https://www.quantumrun.com/consulting/code-llama-statistics/
31. GrowCRM, "Top 20 Open-Source, Self-Hosted CRMs in 2026" (January 4, 2026) — https://growcrm.io/2026/01/04/top-20-open-source-self-hosted-crms-in-2025/
