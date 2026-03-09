# L1 Wave 8 Summary: Agentic Coding Deep Dive
**Synthesis Layer 1 | Wave 8 Research Files: A01–A08**
**Prepared:** March 2026
**Purpose:** Scenario-construction input for the SaaS durability position paper

---

## 1. Wave Theme

Wave 8's agentic coding deep dive reveals a technology in an acute adolescence: capable enough to be genuinely disruptive in narrow, bounded tasks, yet structurally unable to deliver enterprise-grade production software autonomously. The benchmark story looks dramatic — SWE-bench Verified scores rose from single digits in 2023 to 79%+ by early 2026 — but the enterprise story is more sobering. On SWE-bench Pro, which reflects multi-file, proprietary-codebase complexity, the same top models score 9–46%. On SWE-EVO, which tests long-horizon software evolution rather than one-shot bug fixing, GPT-5 resolves only 21% of tasks. METR's randomized controlled trial with experienced developers on real production codebases found a **19% productivity slowdown**, not speedup. The files collectively document a consistent pattern: agentic tools excel at bounded, verifiable, greenfield tasks — security patching, CRUD scaffolding, migration workloads, test generation — and break down on the dimensions that define enterprise software ownership: ambiguous requirements, cross-repository orchestration, compliance self-certification, post-deployment support, user adoption, and long-term maintainability. The wave's most consequential finding for the SaaS durability question is not the benchmark ceiling but the enterprise-grade gap: agentic tools produce code faster than enterprises can safely operate it, because the non-code attributes of enterprise software — security certification, compliance audit trails, disaster recovery, observability, change management, and contractual liability — must all still be added by humans afterward, recreating a large share of the labor cost the tools were supposed to eliminate.

---

## 2. Key Evidence for Each Scenario

### Bull Case (SaaS remains dominant, 60%+ market share in 5 years)

- [76% of enterprise AI use cases are purchased rather than built internally (up from 53% in 2024)](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/), indicating a buy-over-build preference that is strengthening, not weakening, as AI tooling matures.

- [The METR randomized controlled trial of 16 experienced developers on 246 real tasks found a 19% productivity slowdown when using Cursor Pro + Claude](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — the most rigorous independent evaluation available contradicts vendor productivity claims at the exact developer profile (senior, mature codebase) most relevant to enterprise custom software builds.

- [On SWE-bench Pro — designed to reflect enterprise-level complexity across 41 repositories — the best model (Claude Sonnet 4.5) scores 43.6% on the public set and only 9.1% on the proprietary commercial codebase set](https://arxiv.org/abs/2509.16941). This 9.1% figure is the most relevant benchmark for actual enterprise custom-build success rates.

- [Veracode's test of 100+ LLMs found AI-generated code introduces security vulnerabilities in 45% of cases, with Java failure rates exceeding 70%, and security performance remained flat regardless of model size](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/). Enterprise security review requirements mean every AI-generated codebase requires costly human remediation before production deployment.

- [No agentic coding tool holds FedRAMP authorization as of August 2025](https://www.fedramp.gov/ai/), creating a complete compliance gap for government and regulated-sector enterprises that eliminates custom-build viability in those segments.

- [Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) due to escalating costs, unclear business value, and inadequate risk controls — a near-certain near-term correction that will reset enterprise confidence in DIY agentic builds.

- [MIT NANDA research found a 67% success rate when companies purchase AI tools from specialized vendors vs. only ~33% when building internal solutions](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/), providing empirical grounding for the buy-vs.-build risk differential.

- [Mayer Brown partners confirmed in February 2026 that standard SaaS contracts are structurally inadequate for agentic AI, with legal review finding "only standard disclaimers" and no vendor ownership of custom-built output](https://www.mayerbrown.com/en/insights/publications/2026/02/contracting-for-agentic-ai-solutions-shifting-the-model-from-saas-to-services) — enterprises that build with agentic tools own 100% of operational liability with no vendor backstop.

- [Faros AI telemetry across 1,255 enterprise teams found no significant correlation between AI adoption rates and company-level throughput or quality KPIs](https://www.faros.ai/blog/ai-software-engineering), and AI adoption correlated with a 9% increase in bugs per developer and a 154% increase in average PR size.

- [Digital transformation failure rates average 87.5%, costing $2.3 trillion per year globally, with the dominant cause being poor user adoption rather than poor code quality](https://blog.meltingspot.io/why-digital-transformation-projects-fail/) — the last-mile problem is not solved by faster code generation.

### Base Case (SaaS stays majority but declines, 45–60% market share)

- [35% of enterprises surveyed have already replaced functionality of at least one SaaS tool with a custom build, and 78% expect to build more of their own tools in 2026](https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483) — displacement is occurring in the margins of SaaS, not at the core system level ("Nobody's ripping out Salesforce wholesale").

- [Coding captured $4.0 billion (55% of all enterprise departmental AI spend) in 2025 — a 4.1x year-over-year increase](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/), creating investment momentum that will produce more capable tools over the next 5 years regardless of current limitations.

- [METR's task-completion time horizon has been doubling every 88.6 days since 2024, projecting that agents capable of autonomous 8-hour tasks could emerge by approximately 2027](https://metr.org/blog/2026-1-29-time-horizon-1-1/). At the historical doubling rate of 196.5 days, that milestone shifts to 2028–2029. Either scenario creates meaningfully more capable tools within the 5-year horizon.

- [Devin resolved security vulnerabilities 20x faster than humans and completed repository migrations 10–14x faster than human engineers](https://cognition.ai/blog/devin-annual-performance-review-2025) — for these specific bounded use cases, the economic case for agentic coding is already proven, and these workloads represent potential SaaS displacement at the edge.

- [Gartner projects 33% of enterprise software applications will include agentic AI capabilities by 2028 (up from under 1% in 2024)](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html), and Forrester projects global SaaS spending to grow from $318 billion (2025) to $576 billion (2029) — indicating market transformation, not collapse, under base-case assumptions.

- [Faros AI found that high-AI-adoption enterprise teams complete 21% more tasks and merge 98% more pull requests](https://www.faros.ai/blog/enterprise-ai-coding-assistant-adoption-scaling-guide), suggesting real productivity gains at the team level that will attract continued investment even without company-level proof.

- [Anthropic's 2026 Agentic Coding Trends Report documents organizations reporting 30–79% faster development cycles](https://resources.anthropic.com/2026-agentic-coding-trends-report), with enterprises like Rakuten completing 12.5M-line codebase modifications in 7 hours at 99.9% accuracy. These outcomes, even if vendor-reported and skewed, establish a credible ceiling for what capable enterprises can achieve.

- [41% of all new code is now AI-generated globally, with almost half of companies having at least 50% AI-generated code](https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools) — the volume of AI-assisted development creates accumulated codebase expertise that enterprises will increasingly own and want to maintain independently.

### Bear Case (SaaS significantly eroded, <45% market share)

- [METR's task-completion time horizon is doubling every 88.6 days since 2024; at that rate, agents capable of completing multi-week tasks autonomously could emerge by 2027](https://metr.org/blog/2026-1-29-time-horizon-1-1/). If this acceleration continues, the bear case becomes technically feasible within the 5-year window.

- [Nikola Jurkovic's "superhuman coder" forecast places a median arrival of 2027 (80% CI: 2025–2033)](https://ai-2027.com/research/timelines-forecast), and the AI 2027 project assigns roughly 50% probability that 2027 ends without this milestone — meaning roughly 50% probability that it does occur by 2027. If superhuman coders arrive, custom-build economics invert.

- [Factory Droid customer-reported outcomes include 31x faster feature delivery and 96% shorter migration times, with named enterprise customers including Ernst & Young, MongoDB, and Bayer](https://siliconangle.com/2025/09/25/factory-unleashes-droids-software-agents-50m-fresh-funding/). If enterprise-grade agentic coding platforms mature, the build-vs.-buy economics shift materially.

- [Geoffrey Hinton stated in December 2025 that "in a few years, AI will be able to perform software engineering tasks that now need a month's worth of labor" and "there'll be very few people needed for software engineering projects"](https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/) — the bear case depends on whether top researchers' assessments of capability trajectory prove correct.

- [Gartner projects agentic AI could drive approximately 30% of enterprise application software revenue by 2035, surpassing $450 billion](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/), indicating that even conservative analyst forecasts leave room for significant SaaS displacement in the longer run.

- [The agentic AI market is projected to grow from $6.96 billion (2025) to $57.42 billion by 2031 at a 42.14% CAGR](https://www.mordorintelligence.com/industry-reports/agentic-ai-market). If even a fraction of this growth represents custom-build displacement of SaaS procurement, market share erosion is the result.

- [Demis Hassabis (DeepMind CEO) stated in December 2025 that "a year from now, we will have agents that are 'close' to reliably accepting and completing entire delegated tasks"](https://dev.to/aniruddhaadak/the-future-according-to-demis-hassabis-key-predictions-on-agi-agents-and-the-ferocious-race-4313) and gives a 50% probability of AGI by 2030 — if this trajectory materializes, SaaS displacement accelerates well within the 5-year window.

---

## 3. Named Expert Positions

| Name | Title/Org | Position on Agentic Coding / Build Viability | Source URL |
|------|-----------|----------------------------------------------|------------|
| Johno Whitaker | Answer.AI | Skeptical: "Tasks it can do are so small and well-defined that I may as well do them myself, faster, my way." After 1 month with Devin: 3/20 tasks succeeded. | https://www.answer.ai/posts/2025-01-08-devin.html |
| Isaac Flath | Answer.AI | Skeptical: "I had initial excitement...slowly got frustrated as I had to change more and more." | https://www.answer.ai/posts/2025-01-08-devin.html |
| Hamel Husain | Answer.AI | Skeptical: "Devin struggled to use internal tooling...despite copious documentation." | https://www.answer.ai/posts/2025-01-08-devin.html |
| Brian Armstrong | CEO, Coinbase | Skeptical: "It's not clear how you run an AI-coded codebase." | https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/ |
| John Collison | Co-founder, Stripe | Skeptical: "It's not clear how you run an AI-coded codebase." [NOTE: attributed via Apiiro blog — verify primary source before using in position paper] | https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/ |
| Andrej Karpathy | Independent researcher / former Tesla AI Director | Cautiously optimistic on technical capability, skeptical on timeline hype: "It will take about a decade to work through all of those issues." Also: "Every single nine is the same amount of work" on reliability. Has shifted own coding to 80% agent, but notes 5–10x more pessimistic than "SF AI house party" consensus. | https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/ ; https://futuresearch.ai/ai-2027-6-months-later/ |
| Geoffrey Hinton | AI researcher (Turing Award winner) | Strongly bullish on near-term replacement: "In a few years, AI will be able to perform software engineering tasks that now need a month's worth of labor." Endorses METR's 7-month doubling time. | https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/ |
| Demis Hassabis | CEO, Google DeepMind | Bullish: "A year from now, we will have agents that are 'close' to reliably accepting and completing entire delegated tasks." Gives 50% AGI probability by 2030. | https://dev.to/aniruddhaadak/the-future-according-to-demis-hassabis-key-predictions-on-agi-agents-and-the-ferocious-race-4313 ; https://www.cnbc.com/2025/03/17/human-level-ai-will-be-here-in-5-to-10-years-deepmind-ceo-says.html |
| Yann LeCun | Chief AI Scientist, Meta | Skeptical on LLMs: "I'm not interested in LLMs anymore — they're the past." Believes LLMs cannot reach human-level general intelligence; agentic coding based on LLMs faces structural ceiling. | https://x.com/ylecun/status/1911604721267114206 |
| Ilya Sutskever | CEO, Safe Superintelligence | Skeptical on generalization: "These models somehow just generalize dramatically worse than people. It's a very fundamental thing." | https://www.dwarkesh.com/p/ilya-sutskever-2 |
| Gary Marcus | AI researcher, NYU emeritus | Skeptical on reliability: At 95% per-step accuracy, a 20-step agentic workflow has only 36% completion probability — far below enterprise requirements of 99.9%+. | https://www.project-syndicate.org/magazine/generative-ai-fundamentally-unreliable-and-with-no-apparent-solution-by-gary-marcus-2025-06 |
| Nikola Jurkovic | Forecaster, AI 2027 project | Optimistic: Median "superhuman coder" arrival 2027 (80% CI: 2025–2033); time-horizon extension model. | https://ai-2027.com/research/timelines-forecast |
| Eli Lifland | Forecaster, AI 2027 project | Moderate: Median superhuman coder arrival ~2030–2032; 15–20% probability by 2027. Algorithmic speedup needed: 8.5x (CI: 2.5–40x). | https://ai-2027.com/research/timelines-forecast ; https://futuresearch.ai/ai-2027-6-months-later/ |
| Daniel Kokotajlo | Forecaster, FutureSearch | Moderate, recently pessimistic update: "When AI 2027 was published my median was 2028, now it's slipped to 2029." | https://futuresearch.ai/ai-2027-6-months-later/ |
| Addy Osmani | Engineering lead, Google Chrome | Nuanced practitioner: "The 80% threshold works best in personal/greenfield projects, MVPs prioritizing speed over perfection, and small teams managing comprehension debt. Struggles intensify in mature codebases with complex invariants." | https://addyo.substack.com/p/the-80-problem-in-agentic-coding |
| Eyal Paz | VP of Research, Ox Security | Bearish on maintenance quality: "Functional applications can now be built faster than humans can properly evaluate them." "Code review simply cannot scale to match the new output velocity." | https://www.prnewswire.com/news-releases/ox-report-ai-generated-code-violates-engineering-best-practices-undermining-software-security-at-scale-302592642.html |
| Ana Bildea | Practitioner (cited in InfoQ) | Bearish on maintenance: "Traditional technical debt accumulates linearly...AI technical debt is different. It compounds." "I've watched companies go from 'AI is accelerating our development' to 'we can't ship features because we don't understand our own systems' in less than 18 months." | https://www.infoq.com/news/2025/11/ai-code-technical-debt/ |
| Vicki Abraham | Salesforce | Bearish on current debt trajectory: "2026 is the year of technical debt...we're producing tech debt on top of tech debt." | https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027 |
| Aravind Putrevu | CEO, CodeRabbit | Transitional view: "2025 was the year of AI coding speed, 2026 will be the year of AI coding quality." | https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality |
| Andrew Stiefel | Endor Labs / CSA | Skeptical on security: "AI coding assistants are powerful, but they aren't security tools." Training data reproduces unsafe patterns. | https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code |
| Maryam Ashoori | Director of Product Management, IBM | Cautious practitioner: "For simple use cases, the agents are capable of choosing the correct tool, but for more sophisticated use cases, the technology has yet to mature." | https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality |
| Chris Hay | Distinguished Engineer, IBM | Skeptical on enterprise readiness: "Most organizations aren't agent-ready. What's going to be interesting is exposing the APIs that you have in your enterprises today." | https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality |
| David Hsu | CEO, Retool | Cautiously bullish on displacement, scoped: "Nobody's ripping out Salesforce wholesale. What they're doing is replacing the specific piece of a tool that never quite fit." | https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483 |
| Varin Nair | Factory.ai | Bullish on enterprise agentic coding, documents context window as critical constraint: frontier LLMs cannot hold most enterprise monorepos in a single context window. | https://factory.ai/news/context-window-problem |
| Rohith P. George, Joe Pennell, Brad L. Peterson, Oliver Yaros | Partners, Mayer Brown | Bearish on legal readiness: "Agentic AI does not neatly fit into the SaaS contracting model." Standard SaaS "AS-IS" clauses were written for passive tooling, not autonomous systems. | https://www.mayerbrown.com/en/insights/publications/2026/02/contracting-for-agentic-ai-solutions-shifting-the-model-from-saas-to-services |
| Vasu Jakkal | CVP, Microsoft Security | Descriptive (not normative): "80% of Fortune 500 use active AI agents" as of November 2025. | https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/ |

---

## 4. Key Data Points for the Position Paper

The following are the 8–10 most quotable, benchmark-grounded statistics. Each is rated for verifiability.

1. **The controlled-study productivity gap.** ["When developers use AI tools, they take 19% longer to complete coding tasks" — METR randomized controlled trial, 16 experienced developers, 246 tasks, large mature open-source repositories averaging 22,000+ stars and 1M+ lines of code, using Cursor Pro + Claude 3.5/3.7 Sonnet.](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) Notably, participants expected a 24% speedup and believed they received a 20% speedup even after experiencing the slowdown. **Verifiability: HIGH — primary source, independent RCT, published methodology.**

2. **The benchmark-to-production cliff.** [On SWE-bench Pro's commercial subset (proprietary startup codebases), Claude Sonnet 4.5 achieves 9.1% Pass@1 — versus 43.6% on the public set and 77.2% on SWE-bench Verified.](https://arxiv.org/abs/2509.16941) The 9.1% figure is the most relevant for estimating success rates on real enterprise custom builds. **Verifiability: HIGH — peer-reviewed arXiv, Scale AI SEAL leaderboard.**

3. **The security ceiling (structural, not incidental).** [AI-generated code introduces security vulnerabilities in 45% of cases across 100+ LLMs and 80 coding tasks (Veracode). Java failure rate exceeds 70%. Security performance remained flat regardless of model size — only GPT-5 Mini showed meaningful improvement (72% pass rate)](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/). **Verifiability: HIGH — vendor primary research, published methodology.**

4. **The architectural risk spike paradox.** [Apiiro analysis of Fortune 50 repositories: syntax errors dropped 76% and logic bugs fell 60%, but privilege escalation paths jumped 322% and architectural design flaws spiked 153% — alongside a 10x increase in monthly security findings (1,000/month in December 2024 to 10,000+/month by June 2025).](https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/) NOTE: This is single-study data from a security vendor (Apiiro), not independently replicated. **Verifiability: MEDIUM — commercial research, methodology not fully published.**

5. **The long-horizon evolution collapse.** [On SWE-EVO (long-horizon software evolution benchmark, 48 tasks, averaging 21 files and 610 lines of code edited), GPT-5 resolves only 21% of tasks versus 65% on SWE-bench Verified — "a striking capability gap between isolated bug-fixing and long-horizon evolution tasks."](https://arxiv.org/html/2512.18470v1) **Verifiability: HIGH — peer-reviewed arXiv.**

6. **The task-horizon doubling trajectory.** [METR Time Horizon 1.1 (January 2026, 228 tasks): AI agent task-completion horizon has been doubling every 88.6 days since 2024 (accelerated from the historical 196.5-day rate). Current frontier ceiling: Claude Opus 4.5 at ~320 minutes (50% success), GPT-5 at ~214 minutes.](https://metr.org/blog/2026-1-29-time-horizon-1-1/) **Verifiability: HIGH — METR primary source, published methodology.**

7. **The buy-vs.-build enterprise preference, shifting.** [76% of AI use cases are purchased rather than built internally (up from 53% in 2024), per Menlo Ventures survey of ~500 U.S. enterprise decision-makers.](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) **Verifiability: MEDIUM — survey methodology not independently verified; Menlo Ventures is a VC firm with market interest.**

8. **The organizational productivity paradox.** [Faros AI telemetry across 1,255 enterprise teams (10,000+ developers): no significant correlation between AI adoption rate and company-level throughput or quality KPIs. PR review time increased 91%; average PR size grew 154%; bugs per developer rose 9%.](https://www.faros.ai/blog/ai-software-engineering) **Verifiability: MEDIUM — commercial telemetry vendor, methodology not peer-reviewed.**

9. **The last-mile failure rate.** [MIT NANDA initiative (150 interviews, 350 employee surveys, 300 public AI deployments): 95% of enterprise generative AI pilots fail to achieve rapid revenue acceleration; custom internal AI builds succeed at ~33% vs. 67% for purchased vendor solutions.](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) **Verifiability: MEDIUM — reported by Fortune; original MIT NANDA report should be verified as primary source.**

10. **The legal liability vacuum.** [Mayer Brown partners (February 2026): standard SaaS "AS-IS" disclaimers are structurally inadequate for autonomous agents; legal review of AI agent contracts found "only standard disclaimers" with few addressing agentic-specific risks; federal AI LEAD Act liability framework has not yet passed.](https://www.mayerbrown.com/en/insights/publications/2026/02/contracting-for-agentic-ai-solutions-shifting-the-model-from-saas-to-services) **Verifiability: HIGH — named law firm partners, published analysis, citable.**

---

## 5. Critical Caveats for Synthesis

### Do Not Use Without Verification

- **"73% of AI-built startups fail by month 6"** (A02, Section 4.3): Sourced from a Medium blog post (https://medium.com/@ahmadfiazjan/the-30-000-technical-debt-trap-why-73-of-ai-built-startups-fail-to-scale-7c81ce4602f9). The underlying study of "847 venture-backed startups" with "23% monthly compounding technical debt" cannot be traced to any primary source in the research files. **DO NOT CITE in position paper without primary source verification.**

- **McKinsey statistics in A03** (e.g., "less than 10% of organizations have scaled AI agents in any function"; "nearly two-thirds have not yet begun scaling AI across the enterprise"): Cited through secondary aggregators walkme.com and punku.ai respectively, not directly from McKinsey. The primary McKinsey State of AI 2025 report is available at https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai — verify figures against this source before citing in the position paper.

- **A08 statistics through Meltingspot aggregator** (Section 1 of A08 — adoption gap statistics including "70% of all software implementations fail," "digital transformation failure rates range from 70% to 95%," "$2.3 trillion per year" cost, "45% of employees say new software is introduced without adequate training," "63% will stop using technology," etc.): All trace through https://blog.meltingspot.io/why-digital-transformation-projects-fail/ as a single aggregator. These statistics need primary source verification (Gartner, Bain, Prosci, etc.) before citation. Use the primary sources referenced within the Meltingspot piece if possible.

- **John Collison/Stripe quote** ("It's not clear how you run an AI-coded codebase") in A04: Attributed to John Collison (Stripe co-founder) via the Apiiro blog (https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/). The same quote appears attributed to Brian Armstrong (Coinbase CEO) in A02 — meaning at least one attribution may be incorrect. **Do not use this quote with a named attribution without verifying the original primary source.**

### Single Data Points, Not Independent Confirmations

- **METR 19% slowdown** (A01, A03, A05, A06, A07): Appears in multiple Wave 8 files but all cite the same single METR study (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). It is one RCT of 16 developers, 246 tasks, on large open-source repositories. It is the strongest available independent evidence, but it is a single study with a specific developer profile (experienced, large mature repos). Do not treat its multiple appearances across files as independent replication.

- **Apiiro Fortune 50 data** (privilege escalation +322%, architectural flaws +153%, 10x security findings) appears in A01, A02, A03, A04: All trace to the same Apiiro blog post (https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/). This is commercially motivated research from a security vendor with no independently published methodology. Cite as industry evidence, not as peer-reviewed finding.

- **Gartner's 40% project cancellation by 2027** appears in A01, A04, A05, A06, A07, A08: All trace to the same Gartner press release (https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027). Single analyst forecast, not independent confirmation.

### Source-Tier Reminders

- **Anthropic 2026 Agentic Coding Trends Report** (https://resources.anthropic.com/2026-agentic-coding-trends-report): First-party vendor report. Customer-reported outcomes (TELUS saving 500,000 hours; Rakuten 99.9% accuracy; Zapier 97% adoption) are self-reported and unaudited. Use as directional evidence, not benchmark data.

- **Factory Droid customer outcomes** (31x faster feature delivery, 96% shorter migration times): Vendor-reported, not independently verified. Terminal-Bench leaderboard position is independently verifiable at https://www.tbench.ai/leaderboard/terminal-bench/2.0.

- **Menlo Ventures survey data** (76% buy vs. build, $37B enterprise spend, Anthropic 54% coding market share): Menlo is a VC with portfolio interest in the AI space. Survey of ~500 enterprise decision-makers (methodology not published). Use as market sentiment signal, not authoritative market data.

---

## 6. Wave Verdict

The technical feasibility of the bear case — custom AI builds replacing SaaS at meaningful scale within 5 years — is real but contingent on a specific set of simultaneous resolutions that current evidence does not support happening on that timeline. The strongest evidence against the bear case is structural, not merely a matter of current capability: the enterprise-grade gap between "code that works" and "software that enterprises can safely operate" involves security certification, compliance audit trails, disaster recovery architecture, long-term maintainability, legal liability, and user adoption — none of which agentic coding tools address. The METR productivity slowdown on mature codebases, the 9.1% commercial-codebase success rate on SWE-bench Pro, the 21% rate on SWE-EVO, the flat security performance across 100+ LLMs, and the documented 322% spike in architectural vulnerabilities in Fortune 50 AI-assisted codebases all point to the same conclusion: the tools are far more capable at initial code generation than at the full lifecycle of enterprise software ownership. The bear case requires not just better code generation — it requires the simultaneous maturation of agentic tools' compliance self-certification, autonomous security remediation, cross-repository orchestration, legal framework, and organizational change management capabilities. METR's task-horizon acceleration (doubling every 88.6 days since 2024) is the most credible technical trajectory suggesting these gaps could close within the 5-year horizon, and forecasters like Demis Hassabis and Nikola Jurkovic place non-trivial probability on superhuman coding capability by 2027–2028. But Gartner's projection that 40%+ of current agentic AI projects will be canceled by 2027, Andrej Karpathy's assessment that full human replacement in software engineering will "take about a decade," and the empirical evidence that developer trust in AI accuracy has fallen from 40% to 29% in a single year all suggest the bear case sits closer to a 2029–2033 technical feasibility window, not a 2026–2028 one. In 5 years, the most probable outcome is meaningful displacement at the margins of enterprise SaaS — internal tools, bounded automation workflows, specific migration and testing workloads — while complex, compliance-critical, and high-user-surface SaaS categories remain structurally protected by the enterprise-grade requirements that no agentic coding tool currently closes autonomously.

---

*End of L1 Wave 8 Summary*
*All URLs preserved inline. Flags applied to unverified statistics (A02 Medium blog, A03 McKinsey via aggregators, A08 Meltingspot chain, A04 Collison/Armstrong quote ambiguity). METR 19% slowdown and Apiiro Fortune 50 data identified as single data points appearing in multiple files — not independent confirmations.*
