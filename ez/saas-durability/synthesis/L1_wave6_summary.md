# L1 Wave 6 Summary: Developer and Tech Community Perspectives on SaaS Durability
**Synthesis Layer 1 | Wave 6 | Produced: 2026-03-06**
**Research Question:** Will SaaS remain the dominant enterprise procurement method (vs. build) for AI-driven applications in 2-5 years, even with agentic coding tools enabling custom software replacement?

---

## 1. Wave Theme

Wave 6 reveals a developer and tech community in genuine transition — not yet revolution. The agentic coding tools are real, adoption is accelerating, and a meaningful fraction of enterprises (35%) have already replaced at least one SaaS tool with a custom build. But the practitioner data consistently separates the narrative from the numbers: 77% of professional developers do not use vibe coding for production work (Stack Overflow 2025), the most rigorous independent productivity study found a 19% slowdown rather than speedup for experienced developers on real codebases (METR, July 2025), and Bain & Company found that 98% more merged PRs from AI-using teams translated to no measurable improvement in company-wide delivery metrics. The developer community's own taxonomy of SaaS durability is the most useful output of this wave: commoditized, narrow, CRUD-style tools face genuine displacement pressure while payment infrastructure, compliance-heavy software, network-effect platforms, and proprietary-dataset products retain durable structural moats. Tech CEOs read from divergent scripts — Nadella and McDermott call SaaS a collapsing category, Benioff dismisses the threat while simultaneously repricing to consumption-based agents, and Jensen Huang argues AI will use SaaS tools rather than replace them. The build-vs-buy question is not binary; the wave's dominant signal is repricing and partial displacement of the weakest SaaS categories while the strongest incumbents adapt their business models.

---

## 2. Key Evidence for Each Scenario

### Bull Case (SaaS remains dominant, 60%+ market share in 5 years)

- [77% of professional developers report vibe coding — generating entire applications from prompts — is "not part of their professional work"](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/), and trust in AI accuracy fell from 40% to 29% year-over-year, creating persistent friction for the build-vs-buy shift.

- [The METR randomized controlled trial (July 2025, n=246 tasks, 16 experienced developers) found AI tools produced a 19% slowdown — not speedup — for experienced developers on large open-source codebases (22,000+ GitHub stars, 1M+ lines of code)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), directly contradicting the "AI eliminates build cost" thesis for complex enterprise software.

- [Bain & Company found that while AI-using developers merged 98% more pull requests, company-wide delivery metrics showed no measurable improvement in throughput or quality — and PR review time jumped 91% as AI-generated PR volume surged](https://www.faros.ai/blog/bain-technology-report-2025-why-ai-gains-are-stalling), suggesting organizational bottlenecks downstream of coding absorb all apparent gains.

- [Gartner warns that over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027), and Forrester projects enterprises will defer 25% of planned AI spend to 2027 as "the gap between inflated vendor promises and value delivered is widening."

- [Enterprise open-source AI model share of production workloads fell from 19% to 13% in six months (Menlo Ventures, mid-2025)](https://menlovc.com/perspective/2025-mid-year-llm-market-update/), with one enterprise respondent stating "they couldn't keep up with the performance of closed-source over time" — indicating that building custom software still requires purchasing frontier AI infrastructure.

- [Salesforce closed 29,000 Agentforce deals by Q4 FY2026 (up 50% quarter-over-quarter), generated $2.9 billion in AI and Data annual recurring revenue, and posted full-year guidance of $45.8–$46.2 billion](https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Fourth-Quarter-Fiscal-2026-Results/default.aspx) — the strongest SaaS incumbent is growing into agentic pricing rather than losing revenue.

- [Jensen Huang, on the day Nvidia posted 73% year-over-year revenue growth, stated "the markets got it wrong" and that AI agents "will be intelligent software that uses these tools [SAP, ServiceNow, Cadence] on our behalf"](https://www.cnbc.com/2026/02/26/nvidia-jensen-huang-gpu-ai-threat-software-companies-saas-earnings-chips.html) — framing agentic AI as SaaS augmentation, not replacement.

- [Deloitte's Center for Technology, Media and Telecommunications predicts SaaS displacement will take "at least five years or more" and that large SaaS providers have "large footprints across complex workflows that will likely be hard to supplant"](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html).

- [Yann LeCun identifies four structural LLM limitations for enterprise software — lack of physical-world understanding, persistent memory, reasoning, and complex planning — arguing these are fundamental, not incremental gaps](https://www.newsweek.com/nw-ai/ai-impact-interview-yann-lecun-llm-limitations-analysis-2054255), exactly the capabilities required to autonomously build and maintain enterprise-grade software.

### Base Case (SaaS stays majority but declines, 45-60% market share)

- [35% of enterprise teams have already replaced at least one SaaS tool with a custom build (Retool 2026 Build vs. Buy Report, n=817 builders)](https://retool.com/blog/ai-build-vs-buy-report-2026), with the categories most exposed being workflow automations (35%), internal admin tools (33%), and BI tools (29%) — narrow, CRUD-adjacent categories.

- [78% of enterprise respondents expect to build more custom internal tools in 2026](https://retool.com/blog/ai-build-vs-buy-report-2026), and 60% have already built tools outside IT oversight in the past year, indicating a structural shift in behavior even if wholesale SaaS replacement is not occurring.

- [GitHub Copilot is used by 90% of the Fortune 100 and Cursor by 64% of Fortune 500 companies, with Cursor generating 100M+ enterprise lines of code daily](https://cursor.com/enterprise) — the tooling ecosystem has crossed the threshold from experiment to standard infrastructure, permanently lowering the cost basis for custom building.

- [Goldman Sachs piloted Devin alongside its 12,000 human developers, targeting a 20% efficiency gain equivalent to 2,400 additional developers, and described the initiative as creating a "hybrid workforce"](https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html) — validating the enterprise agent deployment model at Tier 1 financial institutions.

- [Deloitte predicts that by 2030, 35% of point-product SaaS tools will be replaced by AI agents or absorbed within larger agent ecosystems, and at least 40% of enterprise SaaS spend will shift toward usage-, agent-, or outcome-based pricing](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html) — structural repricing without total collapse.

- [IDC projects that by 2028, "pure seat-based pricing will be obsolete, with 70% of software vendors refactoring their pricing strategies around new value metrics"](https://www.idc.com/resource-center/blog/is-saas-dead-rethinking-the-future-of-software-in-the-age-of-ai/) — indicating the revenue model changes while the vendor relationships persist.

- [Andrej Karpathy himself acknowledged in October 2025 (Dwarkesh Podcast) that agents are limited to "boilerplate stuff" and tasks common on the internet, and that complex codebases cause systematic misunderstanding](https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/) — the author of the "Software 3.0" thesis imposes a decade-scale timeline on full agent capability.

- [Guillermo Rauch (Vercel) predicts "kingdoms collapse" for companies that cannot adapt their UI to agentic interfaces within three years, but frames this as platform displacement (dashboard SaaS losing to agentic interfaces) rather than custom-build displacement of all SaaS](https://sequoiacap.com/podcast/training-data-guillermo-rauch/).

- [Forrester predicts "vibe coding" will evolve into "vibe engineering" in 2026, encompassing the full SDLC rather than just code generation — suggesting agentic software development becomes the dominant paradigm but remains disciplined professional work, not a free build signal](https://sdtimes.com/softwaredev/forrester-shares-its-predictions-for-how-ai-will-continue-to-shape-software-development-in-2026/).

### Bear Case (SaaS significantly eroded, less than 45% market share)

- [Satya Nadella stated that SaaS/business applications "will all collapse," framing them as "CRUD databases with business logic" that AI agents will manage across apps rather than requiring separate SaaS subscriptions](https://www.windowscentral.com/microsoft/hey-why-do-i-need-excel-microsoft-ceo-satya-nadella-foresees-a-disruptive-agentic-ai-era-that-could-aggressively-collapse-saas-apps) — the most explicit collapse thesis from a major incumbent CEO.

- [Bill McDermott (ServiceNow) stated that "functional SaaS and feature SaaS will be automated by ServiceNow and the language models" and declared "we don't live in the SaaS neighborhood"](https://fortune.com/2026/01/28/servicenow-q4-earnings-beat-ceo-bill-mcdermott-interview/), explicitly targeting Salesforce and Workday as categories facing automated reduction.

- [Replit's CEO Amjad Masad cited a customer who built a working ERP automation application for $400 versus a vendor quote of $150,000 — citing "three orders of magnitude of savings"](https://venturebeat.com/ai/for-replits-ceo-the-future-of-software-is-agents-all-the-way-down) — and Replit Agent produced more than 2 million apps in six months without users writing a single line of code.

- [Replit's annualized revenue grew from approximately $2.8 million to $150 million in less than one year](https://replit.com/news/funding-announcement), with the company raising $250M at a $3B valuation, indicating the no-code/agentic app creation market is experiencing genuine hyper-growth adoption.

- [The software sector lost approximately $2 trillion in market capitalization between January and February 2026 as AI agent concerns escalated](https://www.digitalapplied.com/blog/saaspocalypse-ai-agents-software-industry-analysis), with Atlassian declining approximately 35% and Salesforce approximately 28% — market pricing in significant SaaS displacement risk.

- [Sumeet Chabria (ThoughtLinks, Carnegie Mellon Heinz faculty) argues "markets are not repricing software because AI exists; they are repricing software because control is shifting" and that "the real danger is that code can be generated faster than an enterprise can govern it"](https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework), framing governance lag as the decisive variable enabling rapid SaaS displacement.

- [SWE-bench performance jumped from 4.4% (2023) to 71.7% (2024), and Stanford HAI AI Index 2025 documents a 16x improvement in benchmark coding capability in one year](https://hai.stanford.edu/ai-index/2025-ai-index-report) — if this trajectory holds even partially, the capability gap constraining custom builds narrows rapidly within 2-5 years.

- [DHH, the most prominent developer ideologue advocating SaaS alternatives, stated in January 2026 that AI agents are "fully capable of producing production-grade contributions to real-life code bases" and called it "the most exciting thing we've made computers do since we connected them to the internet in the '90s"](https://world.hey.com/dhh/promoting-ai-agents-3ee04945) — a former skeptic whose conversion adds intellectual credibility to the bear case.

---

## 3. Named Expert Positions

| Name | Title/Org | Position | Source URL |
|------|-----------|----------|------------|
| Andrej Karpathy | Co-founder OpenAI (independent researcher) | "Software 3.0" — LLMs are new computers programmable in English; "Decade of Agents" (2025-2035); but full human-replacement agents are a decade away and agents fail on complex/rare codebases | https://www.latent.space/p/s3 |
| Dario Amodei | CEO, Anthropic | AI writes 90%+ of code internally at Anthropic; externally, his prediction was "nowhere nearly to becoming a reality" per IT Pro at 6-month mark | https://officechai.com/ai/dario-amodei-had-predicted-90-of-code-would-be-written-by-ai-but-now-at-anthropic-its-effectively-100-anthropic-cpo/ |
| Yann LeCun | Founder, AMI Labs (ex-Meta) | LLMs are structural dead-end; four fundamental limitations (memory, planning, reasoning, physical world) make them unsuitable for reliable enterprise software; new architectures needed in 3-5 years | https://www.newsweek.com/nw-ai/ai-impact-interview-yann-lecun-llm-limitations-analysis-2054255 |
| Ilya Sutskever | CEO, Safe Superintelligence | Scaling plateau reached; models "excel on benchmarks yet falter in real-world settings"; generalization failure is fundamental | https://www.dwarkesh.com/p/ilya-sutskever-2 |
| Geoffrey Hinton | Independent (ex-Google Brain) | AI progressing faster than expected; "in a few years, AI will perform software engineering tasks that now need a month's worth of labor" | https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/ |
| Demis Hassabis | CEO, Google DeepMind | Agents "close" to reliably accepting and completing entire delegated tasks by end of 2026; 50% probability of AGI by 2030 | https://dev.to/aniruddhaadak/the-future-according-to-demis-hassabis-key-predictions-on-agi-agents-and-the-ferocious-race-4313 |
| Gary Marcus | Cognitive scientist / AI critic | Agents "mostly been a dud"; at 95% per-step reliability, a 20-step workflow has only 36% chance of success — production enterprise requires 99.9%+ | https://garymarcus.substack.com/p/ai-agents-have-so-far-mostly-been |
| Sam Altman | CEO, OpenAI | AI already writes past 50% of code "in many companies"; each software engineer will "do much, much more for a while" before headcount declines | https://www.entrepreneur.com/business-news/sam-altman-mastering-ai-tools-is-the-new-learn-to-code/488885 |
| David Heinemeier Hansson (DHH) | Co-founder, 37signals | January 2026: AI agents "fully capable of producing production-grade contributions to real-life codebases" and "most exciting thing since connecting computers to the internet"; but "pure vibe coding remains an aspirational dream for professional work" | https://world.hey.com/dhh/promoting-ai-agents-3ee04945 |
| Pieter Levels | Founder, Nomad List / Photo AI | Personifies the solo-developer-replaces-SaaS thesis; ~$3M/year revenue, zero employees, builds complete products in hours using AI tools | https://buildloop.ai/how-pieter-levels-runs-multiple-1m-ai-products-with-automation-zero-team/ |
| Simon Willison | Creator, Datasette / co-creator Django | Coined "vibe engineering" as disciplined alternative to vibe coding; "vibe coding your way to a production codebase is clearly risky" for evolving existing systems | https://simonwillison.net/2025/Oct/7/vibe-engineering/ |
| Guillermo Rauch | CEO, Vercel | "Kingdoms collapse" for SaaS companies that cannot adapt to agentic interfaces within 3 years; "Team Fully Generative Software forever"; but platform infrastructure becomes more important | https://sequoiacap.com/podcast/training-data-guillermo-rauch/ |
| Matt Mullenweg | CEO, Automattic / WordPress | AI coding democratization extends WordPress's mission; "as writing code becomes easier, designing software becomes more important"; managing complexity is the new hard problem | https://ma.tt/2026/02/wp-ai/ |
| Martin Alderson | Co-founder, catchmetrics.io | "Software ate the world. Agents are going to eat SaaS." — but high-uptime, network-effect, and regulated SaaS categories are structurally durable | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |
| Satya Nadella | CEO, Microsoft | SaaS business applications will "collapse"; "agents are the new apps"; Microsoft Dynamics aggressively targeting competitor SaaS backend displacement | https://www.windowscentral.com/microsoft/hey-why-do-i-need-excel-microsoft-ceo-satya-nadella-foresees-a-disruptive-agentic-ai-era-that-could-aggressively-collapse-saas-apps |
| Bill McDermott | CEO, ServiceNow | "Functional SaaS and feature SaaS will be automated"; "we don't live in the SaaS neighborhood"; positioned as consolidation platform | https://fortune.com/2026/01/28/servicenow-q4-earnings-beat-ceo-bill-mcdermott-interview/ |
| Marc Benioff | CEO, Salesforce | Dismisses "SaaSpocalypse" narratives; SaaS "got better with agents"; 29,000 Agentforce deals; but simultaneously restructuring to consumption pricing and cutting 4,000 customer service jobs | https://techcrunch.com/2026/02/25/salesforce-ceo-marc-benioff-this-isnt-our-first-saaspocalypse/ |
| Jensen Huang | CEO, Nvidia | "Markets got it wrong" on AI threat to SaaS; "agentic AI will be intelligent software that uses these tools on our behalf" — AI agents are SaaS users, not SaaS replacements (stated same day as 73% revenue growth quarter) | https://www.cnbc.com/2026/02/26/nvidia-jensen-huang-gpu-ai-threat-software-companies-saas-earnings-chips.html |
| Tobi Lutke | CEO, Shopify | Mandatory AI usage before headcount; "reflexive AI usage is now a baseline expectation"; launched Agentic Storefronts and Universal Commerce Protocol | https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html |
| Amjad Masad | CEO, Replit | SaaS displacement already happening at "three orders of magnitude" savings; customer built ERP automation for $400 vs. $150,000 vendor quote; agents produced 2M+ apps in six months | https://venturebeat.com/ai/for-replits-ceo-the-future-of-software-is-agents-all-the-way-down |
| Michael Truell | CEO, Cursor (Anysphere) | AI coding is powerful and growing ($500M ARR, $29.3B valuation) but warns "shaky foundations" risk when AI builds unsupervised; expects 20% of coding workflows handled by agents by 2026 | https://fortune.com/2025/12/25/cursor-ceo-michael-truell-vibe-coding-warning-generative-ai-assistant/ |
| David Hsu | CEO, Retool | "The cost of building custom software has collapsed"; "nobody's ripping out Salesforce wholesale — they're replacing the specific piece that never quite fit"; "the bar for purchased software just got permanently higher" | https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483 |
| Sumeet Chabria | CEO, ThoughtLinks (Carnegie Mellon Heinz faculty) | "Markets are repricing software because control is shifting"; the danger is code can be generated faster than enterprises can govern it; structured Buy-to-Build framework for CIOs | https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework |
| Mitch Ashley | VP and Practice Leader, Futurum | "2026 will be the year platform engineering shifts from automation to agent-based and agentic workflows" | https://futurumgroup.com/press-release/platform-engineers-critical-to-ai-adoption-in-2026/ |
| Gergely Orosz | Technology writer (The Pragmatic Engineer) | "So far, the only people I've heard using parallel agents successfully are senior+ engineers" — multi-agent orchestration is not democratized | https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/ |
| Pierre Yves Calloc'h | Digital Platforms Director, Pernod Ricard | "There's no way you can go live with a vibe-coded solution. It might work for demos, but we build enterprise-grade technology that has to scale across 30 countries" | https://retool.com/blog/ai-build-vs-buy-report-2026 |
| Deloitte TMT team (Jarvis, Mazumder, Krishnamurthy, Srinivasan, Widener, Crossan) | Deloitte Center for TMT | Traditional SaaS disruption will take "at least five years or more"; by 2030 only 35% of point-product SaaS tools replaced; "SaaS is far from dead" | https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html |

---

## 4. Key Data Points for the Position Paper

1. **METR RCT (July 2025):** [Experienced developers using AI tools (Cursor Pro with Claude 3.5/3.7 Sonnet) took 19% longer to complete 246 issues on large open-source repositories — the opposite of vendor claims — while still believing AI had sped them up by 20%](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). The 40-percentage-point perception-reality gap is the sharpest evidence against uncritical build-cost-collapse arguments.

2. **Retool 2026 Build vs. Buy Report (n=817):** [35% of enterprise teams have already replaced at least one SaaS tool with a custom build; 78% plan to build more in 2026; but only 51% of builders have shipped production software currently in use, and replacement pressure concentrates in workflow automations (35%), internal admin tools (33%), and BI tools (29)](https://retool.com/blog/ai-build-vs-buy-report-2026). The 49% of builders who haven't shipped to production yet represents the risk in projecting forward from intent to outcome.

3. **Bain & Company, Technology Report 2025:** [Developers using AI completed 21% more tasks and merged 98% more PRs, but company-wide delivery showed no measurable throughput or quality improvement. PR review time jumped 91% to absorb the volume surge](https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/). The organizational bottleneck finding is the strongest counterpoint to the "AI cuts build cost therefore SaaS loses" chain of reasoning.

4. **CodeRabbit (December 2025, 470 PRs analyzed):** [AI-generated pull requests contain 1.7x more issues overall than human-only PRs, including 2.74x more XSS vulnerabilities, 3x more readability problems, 2x more error handling failures, and 8x more excessive I/O operations](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report). Enterprise security requirements make these defect rates disqualifying without significant human review overhead.

5. **Stack Overflow 2025 Developer Survey:** [Trust in AI accuracy fell from 40% to 29% year-over-year. 72% of professional developers report vibe coding is not part of their production work. 66% spend more time fixing "almost-right" AI-generated code. Only 29% believe AI handles complex tasks effectively](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/). The declining trust curve runs counter to the accelerating adoption narrative.

6. **SWE-bench trajectory (Stanford HAI AI Index 2025):** [AI systems solved 4.4% of benchmark coding problems in 2023, jumping to 71.7% in 2024 — a 16x improvement in one year](https://hai.stanford.edu/ai-index/2025-ai-index-report). However, on BigCodeBench, AI achieves only 35.5% versus a human standard of 97%, and at 32-hour time horizons humans outperform AI 2-to-1 despite AI outperforming 4x at 2-hour horizons.

7. **Salesforce Q4 FY2026 results:** [29,000 Agentforce deals (up 50% QoQ); $2.9 billion AI and Data ARR; full-year guidance $45.8–$46.2 billion (10-11% growth); consumption-based pricing shift underway](https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Fourth-Quarter-Fiscal-2026-Results/default.aspx). The largest horizontal SaaS incumbent is growing revenue into the agentic era, not losing it — though the business model is structurally evolving.

8. **Gartner agentic AI project cancellation forecast:** [Over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027). This is the single most damaging projection for bear-case scenarios that assume agentic coding translates smoothly to enterprise production deployment.

9. **Black Duck OSSRA 2025:** [97% of commercial codebases contain open-source components; 86% contain vulnerable dependencies; 81% have high or critical-risk vulnerabilities; only 34% of enterprises have a defined open-source strategy](https://www.blackduck.com/blog/qa-open-source-software-risk-2025.html). The security governance deficit in the existing software supply chain is amplified, not reduced, when AI coding agents assemble open-source components at speed.

10. **Replit revenue trajectory (September 2025):** [ARR grew from approximately $2.8 million to $150 million in less than one year; Replit Agent produced more than 2 million apps in six months without users writing a single line of code](https://replit.com/news/funding-announcement). This is the bear case's most credible concrete evidence: agentic app creation at consumer scale is already a high-growth market.

---

## 5. Critical Caveats for Synthesis

- **Retool 2026 Build vs. Buy Report (n=817, vendor-sponsored) — treat as directional only.** Retool is a low-code platform with commercial interest in the "build" narrative. The survey population was self-selected builders, not a representative cross-section of enterprise software buyers. The 35% replacement figure and 78% build-intent figure should be weighted against this conflict. The report nonetheless contains the most granular category-level data on which SaaS tools face displacement pressure.

- **Cursor's "64% of Fortune 500" is self-reported vendor marketing — not independently verified.** Cursor's enterprise page also claims "100M+ lines of enterprise code written daily," "93% of engineers prefer Cursor in head-to-head evaluations," and "50,000+ enterprises choose to build with Cursor" — all unaudited self-reported claims. The independently verified fact is Cursor's $1B ARR and $29.3B valuation, which implies significant genuine adoption without confirming specific penetration percentages.

- **David Hsu (Retool CEO) is the dominant quoted voice in D05 — seven substantive quotes across the platform engineering section.** Every quote favors the "build is accelerating" narrative. His commercial conflict of interest (Retool benefits directly if enterprises build custom tools instead of buying SaaS) must be flagged at every point of use. His quotes are strategic marketing dressed as market analysis.

- **The $1.5T technical debt projection from DEV Community blog (Tier 3 source, D06) must not be weighted equally with primary research.** This figure appears in a practitioner blog post with no sourcing chain to a primary study. Do not use it as a standalone data point; use the GitClear, arXiv 2510.10165, and Forrester technical debt projections (Tier 1-2 sources) instead.

- **Scott Wu (Cognition) and Replit's Amjad Masad sections use company metrics and CEO public statements to press, not independently audited figures.** Devin's ARR trajectory ($1M → $73M in nine months), Cognition's "25% of own code produced by Devin" claim, and Masad's "$400 vs. $150,000 ERP" anecdote are single-source claims from company principals with direct financial interest in their validation. Treat as indicative of the directional trend, not as audited enterprise evidence.

- **Gary Marcus's 36% workflow success rate calculation (20 steps at 95% per-step reliability) is mathematically correct but assumes independence of errors.** Real agentic workflows with error recovery, human checkpoints, and task decomposition may perform better or worse depending on implementation. The pure probabilistic calculation is useful as a floor estimate, not a definitive ceiling.

- **Nadella and McDermott's "SaaS will collapse/be automated" statements are competitive positioning by platform companies seeking to capture SaaS displacement revenue.** Neither Microsoft (Copilot Studio, Dynamics 365, Agent 365) nor ServiceNow is a disinterested party — both stand to gain if traditional SaaS categories consolidate onto their platforms. Their predictions are strategic communications, not analyst forecasts.

- **The IDEsaster security research (100% of tested AI IDEs vulnerable) is from a single security researcher in December 2025 and has not been independently replicated.** The 30+ CVEs are documented and real, but the "100% vulnerable" framing should be read as a snapshot of a rapidly changing security landscape rather than a permanent structural condition.

---

## 6. Wave Verdict

The developer and tech community perspective collectively supports the **base case** as the most probable 2-5 year outcome, with significant uncertainty spread toward the bear case if capability trajectories accelerate faster than governance and quality control mechanisms. The bull case (SaaS dominant at 60%+) is structurally supported by the persistent gap between individual developer enthusiasm and organizational deployment outcomes — the Bain finding that 98% more PRs produces no measurable company-level delivery improvement is the single most important empirical constraint on the build-as-SaaS-replacement thesis. The bear case (below 45%) requires resolving two hard problems that the current evidence suggests are not close to resolution: (1) AI-generated code quality deficits (1.7x more issues, 2.74x more XSS vulnerabilities per CodeRabbit) must reach parity with human code for enterprise security teams to approve wholesale deployment without costly review overhead; and (2) the organizational bottleneck problem (downstream from coding) must be solved, not just the coding problem itself. The developer community's own taxonomy of durable vs. replaceable SaaS is the most actionable output: commoditized CRUD tools, workflow automations, internal admin panels, and narrow BI dashboards face genuine 2-5 year displacement pressure from agentic coding; payment infrastructure, compliance-heavy software (HIPAA, SOX, GDPR), network-effect platforms, and proprietary-dataset products retain structural moats that current agentic tools cannot overcome regardless of build cost. The SaaS market is repricing and partially unbundling, not collapsing — and the infrastructure enabling custom builds (Cursor, Retool, Port, Devin, GitHub Copilot) is itself a SaaS market growing at 25-500% year-over-year rates, creating a recursive dependency on SaaS that the pure "build replaces buy" narrative ignores entirely.

---

## Source Index (Wave 6 Files)

- D01: AI Researcher Views — `/private/tmp/workspace/saas-durability/research/wave6/D01_ai_researcher_views.md`
- D02: Developer Influencer Views — `/private/tmp/workspace/saas-durability/research/wave6/D02_developer_influencer_views.md`
- D03: Developer Tool Ecosystem — `/private/tmp/workspace/saas-durability/research/wave6/D03_developer_tool_ecosystem.md`
- D04: Open Source Role — `/private/tmp/workspace/saas-durability/research/wave6/D04_open_source_role.md`
- D05: Platform Engineering Views — `/private/tmp/workspace/saas-durability/research/wave6/D05_platform_engineering_views.md`
- D06: Developer Experience Reports — `/private/tmp/workspace/saas-durability/research/wave6/D06_developer_experience_reports.md`
- D07: Tech CEO Perspectives — `/private/tmp/workspace/saas-durability/research/wave6/D07_tech_ceo_perspectives.md`
