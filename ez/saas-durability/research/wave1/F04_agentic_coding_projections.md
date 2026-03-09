# F04: Agentic Coding Capability Projections, 2027–2031

**Research Question:** What are credible projections for agentic coding capabilities in 2027–2031, and what would they need to achieve to meaningfully threaten SaaS?

**Research Date:** March 2026
**Scope:** Future trajectory only. Current capabilities covered in F03. TCO analysis covered separately.

---

## Executive Summary

Expert and analyst projections for agentic coding capabilities through 2031 span a wide range, from conservative estimates placing human-equivalent autonomous software development in the early 2030s, to optimistic scenarios projecting "superhuman coders" by 2027. The most credible empirical signal—METR's task-horizon measurement, which shows AI task completion time doubling every 4–7 months—projects frontier models reaching multi-week autonomous software task completion by roughly 2028–2029 if the trend holds. Gartner forecasts 90% of enterprise software engineers will use AI code assistants by 2028, but widespread enterprise-grade production deployment of fully autonomous coding agents faces compounding barriers in context reliability, security governance, compliance architecture, and organizational change management that no current roadmap has fully solved. Forrester has declared "SaaS as we know it is dead" in its structural form, while simultaneously projecting global SaaS spending to grow from $318 billion in 2025 to $576 billion by 2029—indicating a market in transformation rather than collapse.

---

## 1. Expert Projections for Agentic Coding Capability Evolution

### 1.1 Named Expert Timelines

[QUOTE]
"In 6 months 90% of code would be written by AI models. Some people think that prediction is wrong, but within Anthropic and within a number of companies that we work with, that is absolutely true."
— Dario Amodei, CEO, Anthropic (originally stated March 10, 2025; referenced again circa late 2025)
URL: https://www.entrepreneur.com/business-news/anthropic-ceo-predicts-ai-will-take-over-coding-in-12-months/488533
Date: 2025

[QUOTE]
"Automated AI research intern by September 2026" and "full [AI] researcher by March 2028"
— Sam Altman, CEO, OpenAI
URL: https://www.yarnit.app/post/what-these-6-ai-leaders-really-think-about-the-future-of-agentic-ai
Date: 2025

[QUOTE]
"Ghost-like" intelligences optimized for commercial rewards; 2025 to 2035 marked as the "Decade of the Agents"
— Andrej Karpathy, co-founder, OpenAI
URL: https://www.yarnit.app/post/what-these-6-ai-leaders-really-think-about-the-future-of-agentic-ai
Date: 2025

[QUOTE]
"The profession is being dramatically refactored as the bits contributed by the programmer are increasingly sparse and between."
— Andrej Karpathy
URL: https://www.thehansindia.com/technology/tech-news/karpathy-says-vibe-coding-is-fading-as-agentic-engineering-becomes-the-new-ai-coding-era-1045758
Date: 2026

[QUOTE]
Current AI architectures "lack world understanding, persistent memory, reasoning, and planning"; human-level intelligence "quite possibly within a decade"; expects fundamental architectural changes within 3–5 years.
— Yann LeCun, Chief AI Scientist, Meta
URL: https://www.yarnit.app/post/what-these-6-ai-leaders-really-think-about-the-future-of-agentic-ai
Date: 2025

[FACT]
Dario Amodei (Anthropic) AGI timeline: "could arrive 2026–2027"; AI writing "90% of code" with significant disruption in 2–5 years for entry-level work.
URL: https://www.yarnit.app/post/what-these-6-ai-leaders-really-think-about-the-future-of-agentic-ai
Date: 2025

### 1.2 Probabilistic Forecasts (AI 2027 Project)

[STATISTIC]
FutureSearch aggregate forecast (3 professional forecasters): median for "superhuman coder" milestone is 2032–2033 (all-things-considered model), with 80% CI from 2027 to >2050.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[STATISTIC]
Forecaster Eli Lifland all-things-considered estimate: median 2030 for superhuman coders (80% CI: 2026 to >2050).
URL: https://ai-2027.com/research/timelines-forecast
Date: May 2025

[STATISTIC]
Forecaster Nikola Jurkovic all-things-considered estimate: median 2028 for superhuman coders (80% CI: 2026–2040).
URL: https://ai-2027.com/research/timelines-forecast
Date: April 2025

[FACT]
The AI 2027 project's own authors estimate "roughly 50% chance 2027 ends without reaching the superhuman coder milestone."
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
Updated median from Daniel Kokotajlo (AI 2027 project): slipped from 2028 to 2029 median, citing "improved timelines models & slightly slower than expected progress."
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
Metaculus forecasting platform (as of February 2026): 25% probability of AGI by 2029; 50% probability by 2033.
URL: https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/
Date: March 2025

[STATISTIC]
Samotsvety superforecasters (~28% chance of AGI by 2030).
URL: https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/
Date: March 2025

### 1.3 Analyst Firm Projections

[STATISTIC]
Gartner predicts 33% of enterprise software applications will include agentic AI by 2028, up from less than 1% in 2024.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
Gartner best-case scenario: agentic AI could drive approximately 30% of enterprise application software revenue by 2035, surpassing $450 billion, up from 2% in 2025.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
IDC: 10x increase in AI agent usage by 2027 among G2000 companies; 1,000x growth in agent-related API call loads expected by 2027.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
McKinsey: agentic AI could add $2.6–$4.4 trillion annually across business use cases.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

---

## 2. Key Technical Milestones Needed

### 2.1 METR Task-Horizon Research: The Empirical Baseline

[STATISTIC]
"The length of tasks AI agents can complete has been consistently exponentially increasing over the past 6 years, with a doubling time of around 7 months."
— METR (Machine Intelligence Research Institute), March 2025
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 19, 2025

[FACT]
METR methodology: "time horizon" is measured as the human task completion time at which an AI model's fitted logistic curve intersects the 50% success probability threshold.
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 19, 2025

[DATA POINT]
Historical METR time-horizon milestones:
- 2019 (GPT-2): near-zero task completion capacity
- 2023 (GPT-4): ~6-minute task horizon at 50% success
- 2024 (Claude 3.5 Sonnet): ~30-minute capability
- 2025 (Claude 3.7 Sonnet): ~1-hour capability
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

[STATISTIC]
METR: from 2024–2025, time horizons doubled every 4 months (accelerated from the 7-month rate over 2019–2025).
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

[STATISTIC]
METR projection: "in under a decade, we will see AI agents that can independently complete a large fraction of software tasks that currently take humans days or weeks."
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

[STATISTIC]
SWE-Bench Verified analysis shows an even faster doubling time of under 3 months (vs. 4–7 months in the broader METR benchmark suite); methodological differences may explain the gap.
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

[FACT]
METR robustness note: a 10x measurement error in the doubling time estimate shifts arrival-date forecasts by approximately 2 years only.
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

### 2.2 Superhuman Coder Definition and Requirements

[FACT]
AI 2027 project definition of "Superhuman Coder (SC)": An AI system accomplishing coding tasks at 30x speed and 30x lower cost than the best company engineers, with capability across any researcher's expertise area.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[STATISTIC]
Time-horizon requirement for superhuman coder milestone (Eli Lifland estimate): AI must reach 1-month task horizon (from current ~15-minute 80th-percentile horizon as of early 2025).
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[STATISTIC]
Algorithmic speedup required (Nikola Jurkovic estimate): 5.5x (80% CI: 2.0–20.0); Eli Lifland estimate: 8.5x (80% CI: 2.5–40.0).
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[STATISTIC]
Probability of superexponential progress: Eli Lifland 45%, Nikola Jurkovic 40%; probability of exponential progress: Eli 45%, Nikola 50%; probability of subexponential: Eli 10%, Nikola 10%.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

### 2.3 Context and Multi-Step Reasoning Gaps

[STATISTIC]
Qodo 2025 State of AI Code Quality Report (n=609 developers): tasks where AI most frequently misses context — refactoring (65%), boilerplate generation (64%), testing/writing/review (~60%).
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[STATISTIC]
Context miss rates by selection method: manual context selection (54% report missed relevance); autonomous selection (33%); persistent/stored context (16%).
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[STATISTIC]
76.4% of developers (Qodo survey) experience high hallucinations combined with low confidence in AI-generated code — described as a "critical barrier."
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[QUOTE]
"The more a task depends on understanding the broader codebase, the more likely AI is to miss the mark. Among developers who say AI degraded quality, 44% blame missing context."
URL: https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality
Date: December 31, 2025

---

## 3. Projected Improvements in Code Quality and Reliability

[QUOTE]
"2025 was the year when 'ship faster' crystallized into a core performance metric for engineering organizations... The next wave of AI innovation will not be defined by how fast we can generate code. It will be defined by how confidently we can ship it."
— Aravind Putrevu, CodeRabbit
URL: https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality
Date: December 31, 2025

[STATISTIC]
AI-generated code contains 1.7x more issues and bugs compared to human-written code; up to 75% more logic and correctness issues in areas likely to cause downstream incidents.
URL: https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality
Date: December 31, 2025

[STATISTIC]
Qodo survey: 82% of developers use AI coding tools daily or weekly; 59% use 3 or more tools; 20% manage 5 or more tools.
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[STATISTIC]
Qodo survey: 65% of developers report AI influences at least 25% of code per commit; 15% report AI influences more than 80%.
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[STATISTIC]
Qodo survey: 78% of developers report productivity improvements from AI tools; 17% claim a 10x productivity boost.
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[STATISTIC]
Qodo survey: only 3.8% of developers achieve low hallucinations combined with high confidence (the "ideal scenario"); low-hallucination developers are 2.5x more likely to merge code without human review (24% vs. 9%).
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[STATISTIC]
Gartner projects at least 36% compounded developer productivity growth by 2028 from systematic adoption of AI code assistants.
URL: https://www.devopsdigest.com/gartner-75-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
Date: April 2024 [PRE-2025: included as the foundational Gartner baseline figure frequently cited in 2025–2026 reports]

[STATISTIC]
Updated Gartner figure (2025): by 2028, 90% of enterprise software engineers will use AI code assistants, up from less than 14% in early 2024.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
McKinsey (State of AI 2025): organizations applying AI across engineering workflows can improve developer productivity by 20–45%, primarily by reducing downstream rework.
URL: https://synoviadigital.com/insights/the-state-of-ai-in-2025-what-mckinseys-data-tells-us-about-2026/
Date: 2025

[STATISTIC]
McKinsey (State of AI 2025, November): 88% of organizations use AI in at least one business function, up from 78% a year earlier; only 6% of respondents qualify as "AI high performers" (>5% of EBIT attributable to AI).
URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
Date: November 2025

---

## 4. Expected Tooling Ecosystem Evolution

### 4.1 Protocol Standardization

[FACT]
Model Context Protocol (MCP), introduced by Anthropic, standardizes how AI models interact with external tools and data; over 1,000 community-built MCP servers exist as of early 2026.
URL: https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/
Date: 2026

[FACT]
Agent2Agent (A2A), launched by Google with 50+ enterprise partners including Salesforce and ServiceNow, handles asynchronous agent-to-agent communication.
URL: https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/
Date: 2026

[STATISTIC]
Gartner reported a 1,445% surge in multi-agent system inquiries from Q1 2024 to Q2 2025.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

### 4.2 Anthropic's 2026 Agentic Coding Trends Report: Eight Identified Shifts

[FACT]
Anthropic 2026 Agentic Coding Trends Report identifies eight trends: (1) tectonic shift in development lifecycle toward agent supervision and system design; (2) multi-agent coordination replacing single-agent workflows; (3) extended task horizons from hours to days; (4) contextual help-seeking where agents escalate to humans at decision points; (5) expansion to legacy languages (COBOL, Fortran) and non-traditional developers; (6) compression of project delivery timelines; (7) non-engineer adoption across sales, legal, marketing, and operations; (8) dual security impact on defensive and offensive capabilities.
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[STATISTIC]
Anthropic report: developers now use AI in 60% of their work; organizations report 30–79% faster development cycles.
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[FACT]
Anthropic report customer data point: TELUS saved 500,000 hours via agentic coding deployment; Zapier reports 97% developer adoption.
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[FACT]
Anthropic report: Salesforce reports over 90% of their 20,000+ developers now use Cursor, with double-digit improvements in cycle time, PR velocity, and code quality.
URL: https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/
Date: 2026

### 4.3 Governance Architecture: "Bounded Autonomy"

[FACT]
The leading enterprise pattern emerging in 2026 is "bounded autonomy": giving agents clear operational limits with mandatory human escalation paths for high-stakes decisions.
URL: https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/
Date: 2026

[QUOTE]
Forrester Analyst Diego Lo Giudice on Agentic Software Development: "Agency, more than assistance. ASD systems can take on tasks, decompose them, execute steps..."
URL: https://www.forrester.com/blogs/agentic-software-development-defining-the-next-phase-of-ai-driven-engineering-tools/
Date: 2025

[FACT]
Forrester plans a vendor landscape Wave evaluation for Agentic Software Development in H2 2026.
URL: https://www.forrester.com/blogs/agentic-software-development-defining-the-next-phase-of-ai-driven-engineering-tools/
Date: 2025

---

## 5. What "Enterprise-Grade" Custom Software Via Agentic Coding Would Require

### 5.1 Governance and Compliance Requirements

[FACT]
EU AI Act requires governance for high-risk AI systems, with full enforcement by 2026; fines up to €35 million or 7% of global revenue.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

[FACT]
Applicable U.S. regulatory requirements for enterprise AI: OCC model risk management for banking AI; FDA for healthcare AI; SEC/CFTC scrutiny for financial services AI.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

[FACT]
Essential enterprise-grade compliance certifications required for production agentic coding systems: SOC 2, ISO 27001, HIPAA, GDPR; data control requirements including VPC deployment.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

[STATISTIC]
Only 6% of organizations have advanced AI security strategies despite 40% of enterprise applications expected to embed autonomous AI agents by end of 2026.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

[STATISTIC]
Only 1 in 5 (21%) companies surveyed by Deloitte report having a mature governance model for autonomous agents (Deloitte State of AI in the Enterprise, 2026).
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: 2026

[STATISTIC]
Initial AI governance setup costs 0.5–1% of total AI-related technology spend; ongoing annual costs average 0.3–0.5% of AI budget.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

### 5.2 Identity and Access Management Requirements

[FACT]
Enterprise agentic systems require agents to have their own unique identity in one of several forms: unique service accounts for tool access, Kubernetes pod identities for containerized deployments, or workload identities in cloud environments — with strict rules on scope of access.
URL: https://www.rippling.com/blog/agentic-ai-security
Date: 2025

[FACT]
Security frameworks for enterprise-grade agentic coding must address four critical parameters: prompt filtering, data protection, external access control, and response enforcement.
URL: https://www.rippling.com/blog/agentic-ai-security
Date: 2025

### 5.3 Current Deployment Gap

[STATISTIC]
Deloitte State of AI in the Enterprise 2026: only 11% of organizations have agents in production; 38% are running pilots; 35% have no agentic strategy at all.
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: 2026

[STATISTIC]
McKinsey (November 2025): 23% of organizations are scaling an agentic AI system in at least one function; 39% have begun experimenting; in any given business function, no more than 10% of respondents say their organizations are scaling AI agents.
URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
Date: November 2025

[STATISTIC]
Gartner prediction: over 40% of agentic AI projects will be canceled by end of 2027, due to "escalating costs, unclear business value or inadequate risk controls."
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: June 25, 2025

---

## 6. Optimistic vs. Pessimistic Timeline Scenarios

### Comparative Timeline Table

| Milestone | Optimistic Scenario | Central Estimate | Pessimistic Scenario | Source |
|---|---|---|---|---|
| Superhuman coder (SC) | 2027 (Nikola Jurkovic) | 2029–2030 (Eli Lifland, Daniel Kokotajlo) | 2032–2033 (FutureSearch aggregate) | ai-2027.com |
| 90% enterprise eng. using AI assistants | Already partially true at some firms | 2028 (Gartner) | 2030+ (governance barriers) | Gartner |
| 1-month AI task horizon | 2027 (if 4-month doubling holds) | 2028–2029 (7-month doubling rate) | 2031+ (subexponential scenario) | METR |
| AGI (high-level machine intelligence) | 2026–2027 (Amodei; Metaculus 25% CI) | 2029–2033 (Metaculus 50%) | 2047 (superforecasters XPT 2022) | 80,000 Hours |
| Autonomous enterprise app builds | 2027–2028 | 2029–2031 | 2033+ | Multiple |

### 6.1 Optimistic Scenario

[FACT]
AI 2027 optimistic scenario description: "March 2027 marks a critical threshold: the emergence of 'superhuman coders' capable of any coding task the best human engineers perform, but faster and cheaper"; these systems "increase AI research productivity 50-fold — further shortening the path to superintelligence."
URL: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
Date: 2026

[FACT]
AI 2027 optimistic scenario includes: "by March 2027 AIs could succeed with 80% reliability on software tasks that would take a skilled human years to complete."
URL: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
Date: 2026

[FACT]
AI 2027 scenario assumes deployment of 200,000 AI copies in parallel, equivalent to "50,000 of the world's best coders operating at 30x speed."
URL: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
Date: 2026

[STATISTIC]
METR: if the 2024–2025 acceleration (doubling every 4 months) continues, frontier systems may achieve multi-week task horizons by approximately 2027–2029.
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

### 6.2 Pessimistic Scenario

[FACT]
Pessimistic scenario constraint identified by FutureSearch: the full AI 2027 scenario requires "at least one frontier lab" dedicating a majority of its resources to internal AI research infrastructure — a prerequisite the authors question will materialize.
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[FACT]
FutureSearch assessment of AI 2027 scenario as of mid-2026: "FutureSearch predicted superhuman coders would take approximately 3x longer than other AI Futures forecasters estimated," positioning them as more skeptical than median.
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[QUOTE]
"2025 Was Supposed to Be the Year of the Agent. It Never Arrived."
URL: https://www.reworked.co/digital-workplace/2025-was-supposed-to-be-the-year-of-the-agent-it-never-arrived/
Date: 2025

[FACT]
Pessimistic scenario: AI may "fail to overcome issues with ill-defined, high-context work over long time horizons and remain a tool" rather than an autonomous software builder.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

### 6.3 SaaS Market Response Under Both Scenarios

[STATISTIC]
Forrester: global SaaS spending projected to grow from $318 billion (2025) to $512 billion (2028) and $576 billion (2029) — even under current AI disruption pressure.
URL: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
Date: 2026

[STATISTIC]
Forrester: vertical/domain-specific SaaS market projected to grow from $133.5 billion (2025) to $194 billion (2029).
URL: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
Date: 2026

[STATISTIC]
SaaS market capitalization: over $1 trillion erased from software stocks in one week in early February 2026, triggered by rapid AI agent innovation.
URL: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
Date: 2026

[QUOTE]
"The brain of the enterprise remains, the central nervous system is evolving, and the center of gravity is becoming more intelligent."
— Forrester (Kate Leggett et al.)
URL: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
Date: 2026

[QUOTE]
"Horizontal point-solution SaaS vendors with low switching costs and weak, non-embedded enterprise workflows will face challenges and won't scale beyond their current customer base."
— Forrester
URL: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
Date: 2026

---

## Key Takeaways

- The most rigorous empirical measurement of AI capability growth (METR's task-horizon research) projects doubling of task-completion time every 4–7 months; if the trend holds, AI agents capable of completing multi-week software projects autonomously could emerge by 2028–2029, though the trend's persistence is not guaranteed.
- Expert forecasts for "superhuman coders" span a 6-year range from 2027 (optimistic: Nikola Jurkovic, Dario Amodei) to 2033 (pessimistic: FutureSearch aggregate), with the most update-adjusted central estimates landing at 2029–2030; the AI 2027 project itself assigns only a 50% probability to reaching the milestone by end of 2027.
- Enterprise-grade custom software via agentic coding requires solving compounding non-technical barriers: EU AI Act compliance architecture, agent identity and access management, SOC 2/ISO 27001 certification of AI-generated outputs, and governance frameworks — only 21% of enterprises currently have a mature model for autonomous agent governance (Deloitte, 2026).
- Gartner projects over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls — suggesting a near-term correction before enterprise-scale deployment normalizes.
- SaaS spending forecasts ($318B in 2025 → $576B in 2029) indicate the market is adapting rather than collapsing; Forrester's named threat is specifically horizontal point-solution SaaS with low switching costs, not the vertical, deeply-integrated SaaS platforms that represent the largest enterprise contracts.

---

## Sources

1. Gartner — 40% of enterprise apps feature AI agents by 2026: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
2. Gartner — 40% of agentic AI projects canceled by 2027: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
3. Gartner — 75%/90% enterprise engineers using AI code assistants by 2028: https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
4. Gartner strategic software engineering trends 2025+: https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond
5. METR — Measuring AI ability to complete long tasks: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
6. METR — Task completion time horizons: https://metr.org/time-horizons/
7. AI 2027 — Timelines forecast: https://ai-2027.com/research/timelines-forecast
8. AI 2027 — Takeoff forecast: https://ai-2027.com/research/takeoff-forecast
9. FutureSearch — AI 2027 scenario revisited: https://futuresearch.ai/ai-2027-6-months-later/
10. Anthropic — 2026 Agentic Coding Trends Report: https://resources.anthropic.com/2026-agentic-coding-trends-report
11. Anthropic — 2026 Agentic Coding Trends Report (PDF): https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
12. Tessl — 8 trends from Anthropic's report: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
13. Forrester — Agentic Software Development (Diego Lo Giudice): https://www.forrester.com/blogs/agentic-software-development-defining-the-next-phase-of-ai-driven-engineering-tools/
14. Forrester — SaaS as we know it is dead: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
15. Forrester — Predictions 2026: AI Agents and Enterprise Software: https://www.forrester.com/blogs/predictions-2026-ai-agents-changing-business-models-and-workplace-culture-impact-enterprise-software/
16. McKinsey — State of AI 2025 (Agents, innovation, transformation): https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
17. McKinsey — State of AI 2025 (PDF): https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf
18. Deloitte — State of AI in the Enterprise 2026 (press release): https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
19. Deloitte — Tech Trends 2026 press release: https://www.deloitte.com/us/en/about/press-room/deloitte-tech-trends-2026.html
20. Deloitte — Agentic AI strategy (Tech Trends 2026): https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
21. Qodo — State of AI Code Quality 2025: https://www.qodo.ai/reports/state-of-ai-code-quality/
22. CodeRabbit — 2025 speed, 2026 quality: https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality
23. Joget — AI agent adoption data (Gartner, IDC): https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
24. Yarnit — AI leaders on agentic AI future (Karpathy, Altman, LeCun, Amodei): https://www.yarnit.app/post/what-these-6-ai-leaders-really-think-about-the-future-of-agentic-ai
25. 80,000 Hours — Expert AGI forecasts: https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/
26. Entrepreneur — Amodei predicts AI takes over coding in 12 months: https://www.entrepreneur.com/business-news/anthropic-ceo-predicts-ai-will-take-over-coding-in-12-months/488533
27. Karpathy — Agentic engineering as next AI coding era: https://www.thehansindia.com/technology/tech-news/karpathy-says-vibe-coding-is-fading-as-agentic-engineering-becomes-the-new-ai-coding-era-1045758
28. ISACA — Safeguarding enterprise agentic AI workflows: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
29. Rippling — Agentic AI security guide 2025: https://www.rippling.com/blog/agentic-ai-security
30. Reworked — 2025 was supposed to be the year of the agent: https://www.reworked.co/digital-workplace/2025-was-supposed-to-be-the-year-of-the-agent-it-never-arrived/
31. Innobu — AI 2027 superintelligence scenario analysis: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
32. Synoviadigital — McKinsey State of AI 2025 implications for 2026: https://synoviadigital.com/insights/the-state-of-ai-in-2025-what-mckinseys-data-tells-us-about-2026/
