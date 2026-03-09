# A06: Agentic Coding Maturity Curve Projections, 2026–2031

**Research Question:** What is a credible year-by-year maturity projection for agentic coding capabilities through 2031?

**Research Date:** March 2026
**Scope:** Future trajectory only. Current capabilities covered in prior waves. Specific tool feature roadmaps excluded.
**Cross-References:** See [F04: Agentic Coding Capability Projections] for detailed market forecast data and analyst projections. See [D01: AI Researcher Views] for primary-source researcher positions and benchmark data.

---

## Executive Summary

The most rigorous empirical signal for near-term projections — METR's task-horizon benchmark — shows AI agent task-completion time doubling every 88.6 days (approximately 3 months) since 2024, an acceleration from the 196.5-day rate measured across the full 2019–2026 period. At the accelerated rate, frontier models capable of completing multi-week autonomous software projects could emerge by 2027–2028; at the historical rate, that milestone shifts to 2029–2030. Expert probabilistic forecasts for "superhuman coders" span a six-year range — 2027 (Nikola Jurkovic, optimistic) to 2033 (FutureSearch aggregate, pessimistic) — with the most update-adjusted central estimates landing at 2029–2030. The agentic AI market, valued at $6.96 billion in 2025, is projected to reach $57.42 billion by 2031 (CAGR 42.14%), but market growth does not equal maturity: Gartner forecasts over 40% of agentic AI projects will be canceled by end of 2027 due to cost, unclear value, or inadequate governance. The maturity curve is not a smooth ramp but a punctuated trajectory in which near-term capability gains (2026) are already outrunning enterprise governance readiness, and the 2027–2028 window carries the highest uncertainty.

---

## 1. Empirical Baseline: The METR Task-Horizon Trajectory

### 1.1 Core Measurement Framework

[FACT]
METR's "task-completion time horizon" is defined as the human task-completion time at which a model's fitted logistic curve intersects the 50% success probability threshold — i.e., the duration of task at which the agent succeeds half the time.
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 19, 2025

[STATISTIC]
METR's March 2025 study: "The length of tasks AI agents can complete has been consistently exponentially increasing over the past 6 years, with a doubling time of around 7 months."
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 19, 2025

[STATISTIC]
METR Time Horizon 1.1 (January 2026 update, 228 tasks, up from 170): overall doubling time measured at 196.5 days; since 2023, 130.8 days; since 2024, 88.6 days.
URL: https://metr.org/blog/2026-1-29-time-horizon-1-1/
Date: January 29, 2026

[STATISTIC]
METR TH1.1 note: the post-2023 acceleration represents "20% more rapid" growth under the updated methodology.
URL: https://metr.org/blog/2026-1-29-time-horizon-1-1/
Date: January 29, 2026

### 1.2 Historical Model Milestones (METR 50% Task Horizon)

[DATA POINT]
Historical METR task-horizon milestones by model:
- 2019 (GPT-2): near-zero autonomous task completion
- 2023 (GPT-4, original): ~3.5–3.6 minutes at 50% success
- 2024 (Claude 3.5 Sonnet): ~30 minutes
- Early 2025 (Claude 3.7 Sonnet): ~60 minutes [100 minutes under TH1.1]
- 2025 (o3): ~121 minutes [74–201 CI]
- 2025–2026 (Claude Opus 4): ~101 minutes [58–170 CI]
- 2025–2026 (GPT-5): ~214 minutes [117–480 CI]
- Early 2026 (Claude Opus 4.5): ~320 minutes [170–729 CI]
URL: https://metr.org/blog/2026-1-29-time-horizon-1-1/
Date: January 29, 2026

[STATISTIC]
METR: GPT-5.1-Codex-Max point estimate for 50% task horizon: 2 hours 42 minutes (range: 75–350 minutes).
URL: https://evaluations.metr.org/gpt-5-1-codex-max-report/
Date: 2026

[FACT]
METR robustness note: a 10x measurement error in the doubling time estimate shifts arrival-date forecasts for multi-week task horizons by approximately 2 years only.
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

[FACT]
METR research note: "task length is highly correlated with agent success rate (R² = 0.83)" across 230 tested tasks from 2019–2026 models.
URL: https://theaidigest.org/time-horizons
Date: 2026

### 1.3 Extrapolated Milestones from METR Trajectory

[STATISTIC]
Extrapolation from theaidigest.org based on METR data (accelerated 4-month doubling):
- 2027: 8-hour work day equivalent task horizon
- 2028: 40-hour work week equivalent task horizon
- 2029: 167-hour work month equivalent task horizon
URL: https://theaidigest.org/time-horizons
Date: 2026

[STATISTIC]
Extrapolation alternative: given 2024–2025 acceleration (doubling every ~3 months), agents could reach month-long task completion by 2027 rather than 2029.
URL: https://theaidigest.org/time-horizons
Date: 2026

[STATISTIC]
METR projection: "in under a decade, we will see AI agents that can independently complete a large fraction of software tasks that currently take humans days or weeks."
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

---

## 2. Expert Predictions Mapped to Timeline

### 2.1 Probabilistic Forecasts for Superhuman Coder Milestone

[FACT]
AI 2027 project definition of "Superhuman Coder (SC)": an AI system accomplishing coding tasks at 30x speed and 30x lower cost than the best company engineers, with capability spanning any researcher's area of expertise.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

| Forecaster | Model | Median | 80% CI | Source |
|---|---|---|---|---|
| Nikola Jurkovic | Time-horizon-extension | 2027 | 2025–2033 | ai-2027.com |
| Nikola Jurkovic | All-things-considered | 2028 | 2026–2040 | ai-2027.com |
| Eli Lifland | Benchmarks-and-gaps | 2028 | 2025–2050 | ai-2027.com |
| Eli Lifland | All-things-considered | 2030 | 2026–2050 | ai-2027.com |
| Daniel Kokotajlo | Updated all-things-considered | 2029 | — | futuresearch.ai |
| Eli Lifland | Updated all-things-considered | ~2032 | — | futuresearch.ai |
| FutureSearch aggregate | All-things-considered | 2033 | 2027–2050 | ai-2027.com |

URL for all rows: https://ai-2027.com/research/timelines-forecast and https://futuresearch.ai/ai-2027-6-months-later/
Date: 2025–2026

[STATISTIC]
AI 2027 project authors' own estimate: "roughly 50% chance 2027 ends without reaching the superhuman coder milestone."
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
Daniel Kokotajlo updated note: "When AI 2027 was published my median was 2028, now it's slipped to 2029" — citing "improved timelines models and slightly slower than expected progress."
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
Eli Lifland: "My median is roughly 2032, but with AGI by 2027 as a serious possibility (~15-20%)"
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
RE-Bench saturation window (the benchmark at which AI surpasses human performance on research engineering tasks): 80% CI September 2025 – January 2031.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

### 2.2 Named Expert Qualitative Timelines

[QUOTE]
"In a few years, AI will be able to perform software engineering tasks that now need a month's worth of labor. And then there'll be very few people needed for software engineering projects."
— Geoffrey Hinton, CNN State of the Union interview
URL: https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
Date: December 28, 2025

[QUOTE]
"AI's progression is such that after every seven months or so, it is able to complete tasks that took twice as long as before."
— Geoffrey Hinton, CNN State of the Union interview
URL: https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
Date: December 28, 2025

[QUOTE]
"A year from now, we will have agents that are 'close' to reliably accepting and completing entire delegated tasks."
— Demis Hassabis, Google DeepMind CEO, interview with Axios' Mike Allen
URL: https://dev.to/aniruddhaadak/the-future-according-to-demis-hassabis-key-predictions-on-agi-agents-and-the-ferocious-race-4313
Date: December 7, 2025

[FACT]
Demis Hassabis gives a 50% probability of AGI (defined as "consistent, cross-domain brilliance in reasoning, creativity, planning, and problem-solving") arriving by 2030.
URL: https://www.cnbc.com/2025/03/17/human-level-ai-will-be-here-in-5-to-10-years-deepmind-ceo-says.html
Date: March 17, 2025

[QUOTE]
"It will take about a decade to work through all of those issues." [On full human-replacement agent capabilities]
— Andrej Karpathy, Dwarkesh Podcast
URL: https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
Date: October 2025

[QUOTE]
"There's some over-prediction going on in the industry."
— Andrej Karpathy, commenting on 2027 AI takeoff scenario
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[QUOTE]
"my AI timelines are about 5-10X pessimistic w.r.t. what you'll find in your neighborhood SF AI house party"
— Andrej Karpathy
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
Metaculus forecasting platform (as of February 2026): 25% probability of AGI by 2029; 50% probability by 2033.
URL: https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/
Date: March 2025

[STATISTIC]
Samotsvety superforecasters: approximately 28% probability of AGI by 2030.
URL: https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/
Date: March 2025

### 2.3 Algorithmic and Scaling Requirements for Superhuman Coding

[STATISTIC]
Algorithmic speedup required to reach superhuman coder threshold — Eli Lifland estimate: 8.5x (80% CI: 2.5–40.0x); Nikola Jurkovic estimate: 5.5x (80% CI: 2.0–20.0x).
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[STATISTIC]
Time-horizon requirement for superhuman coder milestone (Eli Lifland): AI must reach approximately 1-month task horizon.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[STATISTIC]
Probability of superexponential progress before superhuman coding milestone: Eli Lifland 45%; Nikola Jurkovic 40%. Probability of exponential: Eli 45%, Nikola 50%. Probability of subexponential: Eli 10%, Nikola 10%.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[STATISTIC]
Internal vs. public capability gap (estimate): frontier labs maintain a lead of approximately 1.2 months (80% CI: 0.25–6 months) ahead of publicly released models.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

---

## 3. Year-by-Year Maturity Projections

### 3.1 2026: Near-Term, High Confidence

[STATISTIC]
Gartner: 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from less than 5% in 2025.
URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
Date: August 26, 2025

[STATISTIC]
Anthropic 2026 Agentic Coding Trends Report: developers now use AI in 60% of their work; organizations report 30–79% faster development cycles.
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[FACT]
Anthropic 2026 report identifies extended task horizons — from hours to days — as one of eight core structural shifts in agentic coding practice during 2026.
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[FACT]
Anthropic report: Salesforce reports over 90% of their 20,000+ developers use Cursor, with double-digit improvements in cycle time, PR velocity, and code quality.
URL: https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/
Date: 2026

[FACT]
Anthropic report: TELUS saved 500,000 hours via agentic coding deployment; Zapier reports 97% developer adoption.
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[FACT]
Frontier model task horizons as of early 2026: Claude Opus 4.5 at ~320 minutes (5.3 hours) at 50% success; GPT-5 at ~214 minutes (3.6 hours). This represents the defined near-term (2026) agentic capability floor.
URL: https://metr.org/blog/2026-1-29-time-horizon-1-1/
Date: January 29, 2026

[STATISTIC]
Gartner reported a 1,445% surge in multi-agent system inquiries from Q1 2024 to Q2 2025, signaling the transition from single-agent to orchestrated multi-agent architectures in 2026.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[FACT]
Model Context Protocol (MCP), introduced by Anthropic, had over 1,000 community-built servers by early 2026; Agent2Agent (A2A) protocol launched by Google with 50+ enterprise partners including Salesforce and ServiceNow.
URL: https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/
Date: 2026

[STATISTIC]
2026 governance gap: only 11% of organizations have agents in production; 38% are running pilots; 35% have no agentic strategy at all (Deloitte State of AI in the Enterprise 2026).
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: 2026

[STATISTIC]
Only 21% of companies report having a mature governance model for autonomous agents (Deloitte, 2026).
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: 2026

### 3.2 2027–2028: Medium-Term, Moderate Confidence

[STATISTIC]
Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 due to "escalating costs, unclear business value or inadequate risk controls."
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: June 25, 2025

[STATISTIC]
Gartner: by 2027, one-third of agentic AI implementations will combine agents with different skills to manage complex tasks within application and data environments.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
Gartner: by 2028, 15% of day-to-day work decisions will be made autonomously through agentic AI (up from 0% in 2024); 33% of enterprise software applications will include agentic AI capabilities (up from <1% in 2024).
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

[STATISTIC]
Gartner: by 2028, 90% of enterprise software engineers will use AI code assistants, up from less than 14% in early 2024.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
Gartner: at least 36% compounded developer productivity growth by 2028 from systematic adoption of AI code assistants.
URL: https://www.devopsdigest.com/gartner-75-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
Date: April 2024 [PRE-2025 — included as the foundational Gartner baseline figure frequently cited in 2025–2026 reports]

[STATISTIC]
IDC: 10x increase in AI agent usage by 2027 among G2000 companies; 1,000x growth in agent-related API call loads expected by 2027.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
Gartner: by 2028, one-third of user experiences will shift from native applications to agentic front ends, driving new business models and pricing structures.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
arXiv study (2601.13597) on agentic coding adoption in open-source repositories: agent-first repositories show 36.25% increase in commits and 76.59% increase in lines added; static-analysis warnings rise ~18% and cognitive complexity increases ~39% regardless of prior exposure, documenting "agent-induced complexity debt."
URL: https://arxiv.org/html/2601.13597
Date: 2026

[STATISTIC]
AI 2027 optimistic scenario for 2027: "by March 2027 AIs could succeed with 80% reliability on software tasks that would take a skilled human years to complete."
URL: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
Date: 2026

[STATISTIC]
METR (accelerated-rate projection): 8-hour autonomous task horizon expected by approximately 2027; 40-hour work week equivalent by approximately 2028.
URL: https://theaidigest.org/time-horizons
Date: 2026

[STATISTIC]
METR (historical-rate projection): 8-hour autonomous task horizon expected by approximately 2028–2029.
URL: https://theaidigest.org/time-horizons
Date: 2026

[FACT]
Deloitte identifies three structural barriers constraining 2027–2028 enterprise deployment: (1) legacy system integration — traditional systems lack real-time execution capability and modern APIs; (2) data architecture constraints — current ETL processes create friction for agent deployment; (3) governance gaps — organizations lack oversight mechanisms for autonomous decision-making.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

[FACT]
Forrester plans to publish a vendor landscape Wave evaluation for Agentic Software Development in H2 2026 — a market categorization event that typically signals vendor consolidation and enterprise procurement maturity in the following 12–18 months.
URL: https://www.forrester.com/blogs/agentic-software-development-defining-the-next-phase-of-ai-driven-engineering-tools/
Date: 2025

### 3.3 2029–2031: Long-Term, Low Confidence

[STATISTIC]
Mordor Intelligence: agentic AI market estimated at $9.89 billion in 2026; projected to reach $57.42 billion by 2031, at a CAGR of 42.14%.
URL: https://www.mordorintelligence.com/industry-reports/agentic-ai-market
Date: 2026

[STATISTIC]
MarketsandMarkets: AI Agents market projected to grow from $7.84 billion in 2025 to $52.62 billion by 2030, registering a CAGR of 46.3%.
URL: https://www.marketsandmarkets.com/PressReleases/ai-agents.asp
Date: 2025

[STATISTIC]
Gartner best-case scenario: agentic AI could drive approximately 30% of enterprise application software revenue by 2035, surpassing $450 billion, up from 2% in 2025.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

[STATISTIC]
METR (accelerated-rate projection): 167-hour (work month equivalent) autonomous task horizon by approximately 2029.
URL: https://theaidigest.org/time-horizons
Date: 2026

[STATISTIC]
FutureSearch all-things-considered median for superhuman coders: 2033 (80% CI: 2027–2050). FutureSearch "predicted superhuman coders would take approximately 3x longer than other AI Futures forecasters estimated."
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[FACT]
Pessimistic constraint identified by FutureSearch: the full accelerated scenario requires "at least one frontier lab" dedicating a majority of its resources to internal AI research infrastructure — a prerequisite the authors question will materialize.
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
Nikola Jurkovic updated timeline (2026): median AI automating >95% of remote jobs shifted from approximately 3-year to approximately 4-year projection from 2022 baseline.
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

[STATISTIC]
McKinsey: agentic AI could add $2.6–$4.4 trillion annually across business use cases.
URL: https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
Date: 2026

---

## 4. Key Technical Milestones and Estimated Timelines

### 4.1 Milestone Timeline Table

| Milestone | Optimistic Estimate | Central Estimate | Pessimistic Estimate | Primary Source |
|---|---|---|---|---|
| 8-hour autonomous task horizon | 2027 (accelerated rate) | 2027–2028 | 2029 (historical rate) | METR / theaidigest.org |
| 40-hour autonomous task horizon | 2027–2028 | 2028–2029 | 2030–2031 | METR / theaidigest.org |
| 1-month autonomous task horizon | 2027 (accelerated) | 2029 | 2031+ | METR / theaidigest.org |
| Superhuman Coder (SC) threshold | 2027 (Jurkovic) | 2029–2030 (Kokotajlo, Lifland) | 2033 (FutureSearch) | ai-2027.com |
| 90% enterprise engineers using AI assistants | 2027 (early adopter wave) | 2028 (Gartner) | 2030+ (governance barriers) | Gartner |
| 33% enterprise apps include agentic AI | Already 40% partial (Gartner 2026) | 2028 (full capability) | 2030 | Gartner |
| AGI (high-level machine intelligence) | 2026–2027 (Amodei; Metaculus 25% CI) | 2029–2033 (Metaculus 50%) | 2047 (superforecasters) | 80,000 Hours |
| Autonomous enterprise app builds (production-grade) | 2027–2028 | 2029–2031 | 2033+ | Multiple |

Sources: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ ; https://ai-2027.com/research/timelines-forecast ; https://theaidigest.org/time-horizons ; https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/

### 4.2 Key Non-Capability Technical Milestones

[FACT]
Context reliability gap (2026 baseline): Qodo 2025 survey (n=609) — 76.4% of developers experience high hallucinations combined with low confidence in AI-generated code. Only 3.8% achieve the "ideal scenario" of low hallucinations with high confidence.
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: June 2025

[STATISTIC]
Quality benchmark (2025–2026 baseline): AI-generated code contains 1.7x more issues and bugs compared to human-written code; up to 75% more logic and correctness issues in areas likely to cause downstream incidents.
URL: https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality
Date: December 31, 2025

[STATISTIC]
Stanford HAI AI Index 2025: On BigCodeBench, AI systems achieve a 35.5% success rate — well below the human standard of 97%. In short time-horizon settings (2 hours), top AI systems score 4x higher than human experts on programming tasks; at 32-hour time horizons, humans outperform AI 2-to-1.
URL: https://hai.stanford.edu/ai-index/2025-ai-index-report
Date: 2025

[STATISTIC]
METR RCT (July 2025, n=16 experienced developers, 246 issues, large open-source repositories with 22,000+ GitHub stars, 1M+ lines of code, using Cursor Pro with Claude 3.5/3.7 Sonnet): developers using AI tools took 19% longer to complete issues compared to working without AI. Developers expected a 24% speedup; post-task self-assessment still showed perceived +20% boost despite the measured slowdown.
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

[QUOTE]
"2025 was the year when 'ship faster' crystallized into a core performance metric for engineering organizations... The next wave of AI innovation will not be defined by how fast we can generate code. It will be defined by how confidently we can ship it."
— Aravind Putrevu, CodeRabbit
URL: https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality
Date: December 31, 2025

[FACT]
Marcus's mathematical constraint on agent reliability: even at 95% per-step success rate, a 20-step agentic workflow has only a ~36% chance of completing without error. Production enterprise systems typically require 99.9%+ overall reliability.
URL: https://www.project-syndicate.org/magazine/generative-ai-fundamentally-unreliable-and-with-no-apparent-solution-by-gary-marcus-2025-06
Date: June 2025

[FACT]
EU AI Act full enforcement active by 2026; fines up to €35 million or 7% of global revenue for non-compliant high-risk AI systems — creating a hard regulatory floor for enterprise agentic coding deployment timelines.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

---

## 5. Scenarios: Optimistic vs. Pessimistic Capability Curves

### 5.1 Optimistic Scenario (Probability: ~20–30% per expert aggregates)

[FACT]
AI 2027 optimistic scenario: "March 2027 marks a critical threshold — the emergence of 'superhuman coders' capable of any coding task the best human engineers perform, but faster and cheaper"; these systems "increase AI research productivity 50-fold — further shortening the path to superintelligence."
URL: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
Date: 2026

[FACT]
AI 2027 optimistic scenario assumes deployment of 200,000 AI copies in parallel, equivalent to "50,000 of the world's best coders operating at 30x speed."
URL: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
Date: 2026

[STATISTIC]
Driver of optimistic scenario: if the 2024–2025 METR acceleration (doubling every ~3 months) continues uninterrupted, frontier systems reach multi-week task horizons by approximately 2027.
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

[STATISTIC]
Optimistic scenario probability anchor: the AI 2027 project assigns "roughly 50% chance 2027 ends without reaching the superhuman coder milestone" — implying roughly 50% that it does not, i.e., roughly 50% that it does occur by 2027.
URL: https://futuresearch.ai/ai-2027-6-months-later/
Date: 2026

**Optimistic Curve Summary (approximate):**
- 2026: Agents complete 4–5 hour tasks reliably; multi-agent orchestration standard
- 2027: Agents complete full-day (8-hour) tasks; superhuman coder threshold possible
- 2028: Agents complete multi-week tasks; autonomous greenfield apps for narrow domains
- 2029: Near-full autonomous software development for well-specified projects
- 2030–2031: Enterprise-grade autonomous coding with governance frameworks mature enough for regulated industries [UNVERIFIED — synthesized from trajectory data, not a named source]

### 5.2 Pessimistic Scenario (Probability: ~30–40% per FutureSearch aggregates)

[QUOTE]
"2025 Was Supposed to Be the Year of the Agent. It Never Arrived."
URL: https://www.reworked.co/digital-workplace/2025-was-supposed-to-be-the-year-of-the-agent-it-never-arrived/
Date: 2025

[FACT]
Pessimistic constraint from AI 2027 research: AI may "fail to overcome issues with ill-defined, high-context work over long time horizons and remain a tool" rather than an autonomous software builder.
URL: https://ai-2027.com/research/timelines-forecast
Date: 2025

[QUOTE]
Yann LeCun: "I'm not interested in LLMs anymore — they're the past. The future is in four more interesting areas: machines that understand the physical world, persistent memory, reasoning, and planning."
URL: https://x.com/ylecun/status/1911604721267114206
Date: April 2025

[QUOTE]
Ilya Sutskever (Safe Superintelligence): "These models somehow just generalize dramatically worse than people. It's a very fundamental thing."
URL: https://www.dwarkesh.com/p/ilya-sutskever-2
Date: November 2025

[FACT]
Pessimistic scenario structural constraint: over 40% of agentic AI projects projected to fail by 2027 (Gartner), and only 6% of organizations have advanced AI security strategies despite agent adoption accelerating — creating a governance crisis that could force regulatory-mandated slowdowns.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

**Pessimistic Curve Summary (approximate):**
- 2026: Current pattern of pilot proliferation without production maturity continues
- 2027: Project cancellation wave (Gartner: 40%+ fail); governance crisis forces re-architecture
- 2028: Rebuilding phase; task horizons reach 8 hours but quality and reliability gaps persist
- 2029–2030: Incremental recovery; 40-hour horizon capability achieved but enterprise adoption lags 2–3 years behind technical capability
- 2031: Mature multi-agent orchestration for greenfield, well-scoped projects; complex enterprise systems still require significant human oversight [UNVERIFIED — synthesized from trajectory data]

### 5.3 Central/Base Case (Probability: ~40–50%)

[STATISTIC]
Base case anchor — Forrester: global SaaS spending projected to grow from $318 billion (2025) to $512 billion (2028) and $576 billion (2029), indicating market transformation rather than collapse even under mid-range agentic coding adoption.
URL: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
Date: 2026

[STATISTIC]
Base case anchor — McKinsey (November 2025): 23% of organizations are scaling an agentic AI system in at least one function; 39% have begun experimenting; in any given business function, no more than 10% of respondents say their organizations are scaling AI agents.
URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
Date: November 2025

---

## 6. Structural Headwinds Constraining All Scenarios

[STATISTIC]
Adoption gap (Deloitte 2026): 30% of organizations exploring agentic options; 38% piloting; 14% have deployment-ready solutions; 11% actively in production; 42% still developing strategy roadmaps; 35% have no formal strategy.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

[STATISTIC]
Data architecture headwinds (Deloitte 2026): 48% of organizations cite data searchability as a challenge to AI automation; 47% report data reusability challenges.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

[STATISTIC]
Security maturity gap (ISACA 2025): only 6% of organizations have advanced AI security strategies despite 40% of enterprise applications expected to embed autonomous AI agents by end of 2026.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workshops
Date: 2025

[STATISTIC]
Governance cost floor: initial AI governance setup costs 0.5–1% of total AI-related technology spend; ongoing annual costs average 0.3–0.5% of AI budget.
URL: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
Date: 2025

[STATISTIC]
Agent reliability compound-step problem: at 95% per-step success, a 20-step workflow has ~36% completion probability. Enterprise systems typically require 99.9%+ overall reliability — implying the step-level reliability must reach 99.995%+ for 20-step workflows, a threshold no current system approaches.
URL: https://www.project-syndicate.org/magazine/generative-ai-fundamentally-unreliable-and-with-no-apparent-solution-by-gary-marcus-2025-06
Date: June 2025

[QUOTE]
"Every single nine is the same amount of work." [On reliability from 90% to 99% to 99.9%]
— Andrej Karpathy
URL: https://www.superagent.sh/blog/the-march-of-nines
Date: 2025

---

## Key Takeaways

- The METR task-horizon doubling rate has accelerated from 196.5 days (2019–2026 baseline) to 88.6 days (2024-forward), which, if sustained, projects frontier AI completing 8-hour software tasks autonomously by approximately 2027 and full work-week tasks by approximately 2028. This is the strongest empirical basis for near-term projections.

- Expert probabilistic forecasts for the "superhuman coder" threshold span 2027–2033. The most recently updated central estimates (Kokotajlo: 2029, Lifland: 2032) have both shifted later than original 2025 projections — and the AI 2027 project authors themselves assign only ~50% probability to their headline scenario occurring by end of 2027.

- Gartner's forecast that over 40% of agentic AI projects will be canceled by end of 2027 represents a near-certain near-term correction event: enterprise deployments are outrunning governance infrastructure, and the cancellation wave will reset expectations before a more durable second wave of adoption.

- The quality gap — AI code contains 1.7x more bugs than human-written code (CodeRabbit 2025), METR RCT showed a 19% productivity slowdown on complex real-world tasks — is the primary constraint between benchmark performance and enterprise-grade deployment maturity. Resolving this gap is a precondition for the 2028-onward projections materializing.

- Market size ($9.89 billion in 2026 to $57.42 billion by 2031 at 42.14% CAGR) tracks adoption velocity, not capability maturity. The most consequential enterprise inflection — widespread autonomous coding for production systems — sits in the 2029–2031 window under the central scenario, and depends on simultaneous resolution of reliability, governance, and regulatory compliance barriers that no single roadmap currently guarantees.

---

## Sources

1. METR — Measuring AI Ability to Complete Long Tasks (March 2025): https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
2. METR — Time Horizon 1.1 Update (January 29, 2026): https://metr.org/blog/2026-1-29-time-horizon-1-1/
3. METR — Task Completion Time Horizons (main): https://metr.org/time-horizons/
4. METR — GPT-5.1-Codex-Max Evaluation: https://evaluations.metr.org/gpt-5-1-codex-max-report/
5. METR — RCT Study on Experienced Developer Productivity (July 10, 2025): https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
6. Epoch AI — METR Time Horizons Benchmark: https://epoch.ai/benchmarks/metr-time-horizons
7. AI Digest — "A New Moore's Law for AI Agents": https://theaidigest.org/time-horizons
8. AI 2027 — Timelines Forecast: https://ai-2027.com/research/timelines-forecast
9. FutureSearch — AI 2027 Six Months Later: https://futuresearch.ai/ai-2027-6-months-later/
10. Innobu — AI 2027 Superintelligence Scenario Analysis: https://www.innobu.com/en/articles/ai-2027-superintelligence-scenario-analysis
11. Anthropic — 2026 Agentic Coding Trends Report: https://resources.anthropic.com/2026-agentic-coding-trends-report
12. Tessl — 8 Trends from Anthropic's 2026 Report: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
13. Gartner — 40% of Enterprise Apps Feature AI Agents by 2026 (August 26, 2025): https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
14. Gartner — 40% of Agentic AI Projects Canceled by 2027 (June 25, 2025): https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
15. Joget — AI Agent Adoption 2026 (Gartner, IDC data): https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/
16. Deloitte — Tech Trends 2026 / Agentic AI Strategy: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
17. Deloitte — State of AI in the Enterprise 2026 (press release): https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
18. McKinsey — The State of AI (November 2025): https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
19. Forrester — SaaS as We Know It Is Dead: https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/
20. Forrester — Agentic Software Development (Diego Lo Giudice, 2025): https://www.forrester.com/blogs/agentic-software-development-defining-the-next-phase-of-ai-driven-engineering-tools/
21. Mordor Intelligence — Agentic AI Market 2026–2031: https://www.mordorintelligence.com/industry-reports/agentic-ai-market
22. MarketsandMarkets — AI Agents Market (2025–2030): https://www.marketsandmarkets.com/PressReleases/ai-agents.asp
23. Stanford HAI — AI Index Report 2025: https://hai.stanford.edu/ai-index/2025-ai-index-report
24. Qodo — State of AI Code Quality 2025 (June 2025): https://www.qodo.ai/reports/state-of-ai-code-quality/
25. CodeRabbit — 2025 Was the Year of AI Speed (December 31, 2025): https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality
26. ISACA — Safeguarding Enterprise Agentic AI Workflows (2025): https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows
27. The New Stack — 5 Key Trends Shaping Agentic Development in 2026: https://thenewstack.io/5-key-trends-shaping-agentic-development-in-2026/
28. 80,000 Hours — When Do Experts Expect AGI to Arrive (March 2025): https://80000hours.org/2025/03/when-do-experts-expect-agi-to-arrive/
29. Geoffrey Hinton — CNN State of the Union (Fortune, December 28, 2025): https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
30. Demis Hassabis — Human-Level AI in 5–10 Years (CNBC, March 17, 2025): https://www.cnbc.com/2025/03/17/human-level-ai-will-be-here-in-5-to-10-years-deepmind-ceo-says.html
31. Andrej Karpathy — Dwarkesh Podcast (October 2025): https://www.dwarkesh.com/p/andrej-karpathy
32. Andrej Karpathy — Simon Willison notes on "AGI is still a decade away" (October 18, 2025): https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
33. Ilya Sutskever — Dwarkesh Podcast (November 2025): https://www.dwarkesh.com/p/ilya-sutskever-2
34. Yann LeCun — "Not Interested in LLMs" (X, April 2025): https://x.com/ylecun/status/1911604721267114206
35. Gary Marcus — AI Reliability Crisis (Project Syndicate, June 2025): https://www.project-syndicate.org/magazine/generative-ai-fundamentally-unreliable-and-with-no-apparent-solution-by-gary-marcus-2025-06
36. Superagent — The March of Nines (Karpathy reliability quote, 2025): https://www.superagent.sh/blog/the-march-of-nines
37. Reworked — "2025 Was Supposed to Be the Year of the Agent" (2025): https://www.reworked.co/digital-workplace/2025-was-supposed-to-be-the-year-of-the-agent-it-never-arrived/
38. arXiv — AI IDEs or Autonomous Agents? Measuring Impact of Coding Agents (2601.13597): https://arxiv.org/html/2601.13597
39. Devopsdigest — Gartner: 75%/90% Enterprise Engineers Using AI Code Assistants by 2028: https://www.devopsdigest.com/gartner-75-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
