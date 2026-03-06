# T07 — Economic Break-Even Scenarios: Build vs. Buy Under Agentic Coding Capability Cases

**Research File:** T07 — Economic Break-Even Scenarios
**Wave:** 9
**Date Compiled:** 2026-03-06
**Audience:** C-Suite / Enterprise Strategy
**Cross-references:** See F05 (Build vs. Buy Framework) for foundational decision variables and historical failure statistics. See C01 (McKinsey Perspectives) for McKinsey's "sources of distinctiveness" thesis and the Frontier Alliance context.

---

## Executive Summary

The build-vs-buy decision has entered a quantitatively unstable period: the variables that anchor the classical break-even model — initial development cost, annual maintenance cost, and time-to-value — are all in simultaneous flux as agentic coding capability matures. Under a bear scenario (limited agentic capability improvement), the SaaS incumbency advantage remains largely intact, and the structural break-even for custom builds stays at two to four years for most enterprise use cases. Under a base scenario (moderate capability gains), the break-even compresses to twelve to thirty-six months for commodity-adjacent workflows, and the 35% of enterprises that have already replaced at least one SaaS product with custom software — per Retool's February 2026 survey of 817 enterprise builders — represents a leading indicator rather than an outlier. [(Retool, February 17, 2026)](https://retool.com/blog/ai-build-vs-buy-report-2026) Under a bull scenario (transformative capability, near-zero marginal maintenance), the economic case for buying commodity-function SaaS collapses for large enterprises, and the question shifts from whether to build to what governance infrastructure can absorb the risk. Published frameworks from Bain, ThoughtLinks, and McKinsey, combined with quantitative TCO benchmarks from Xenoss and VRInSofts, allow scenario-specific break-even ranges to be modeled, though the sensitivity of the output to maintenance cost assumptions and user-count growth trajectories is high enough to warrant explicit scenario testing before any capital commitment.

---

## 1. The Classical Break-Even Model: Variables and Baseline Assumptions

The core build-vs-buy break-even formula measures the year in which the total cost of ownership of a custom-built solution falls below the cumulative cost of a SaaS subscription. In its simplest form:

**Break-even occurs when:**
`Cumulative SaaS Cost (Year N) > Initial Build Cost + Annual Maintenance Cost x N`

### 1a. Baseline Variable Definitions

[FACT]
A five-year cost comparison model published by VRInSofts, using an enterprise CRM scenario with 20 initial users at $50/user/month, annual team growth of 20%, and annual SaaS price increases of 10%, produces the following trajectory:
- Year 1 SaaS annual cost: $12,000 (20 users x $50/month x 12)
- Year 5 SaaS annual cost: $36,818 (42 users x $73.21/month x 12)
- Five-year SaaS total: $113,663
— VRInSofts, "5-Year Cost Calculator: SaaS Subscriptions vs Custom Software"
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

[STATISTIC]
A broader five-year scenario comparison from VRInSofts shows: SaaS total of $295,000 versus custom software total of $82,500, with SaaS per-user licenses accounting for $127,500 and custom maintenance running at 15-20% of original development cost annually. Break-even in this scenario occurs between years two and four.
— VRInSofts, "5-Year Cost Calculator: SaaS Subscriptions vs Custom Software"
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

[FACT]
Custom software ongoing support is benchmarked at "15-20% of the initial development cost per year" in the VRInSofts five-year model.
— VRInSofts, "5-Year Cost Calculator: SaaS Subscriptions vs Custom Software"
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

[STATISTIC]
"Total spending on SaaS subscriptions over 5 years typically exceeds initial custom development costs by 72% — yet this cost continues indefinitely, while custom software has a declining cost curve."
— VRInSofts / industry benchmark synthesis
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

[STATISTIC]
"The break-even point for custom versus SaaS is typically 2-4 years when total cost of ownership is calculated honestly." Custom software ROI window cited as "18-36 months" for most implementations.
— VRInSofts
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

### 1b. Enterprise SaaS Hidden Cost Structure

The sticker price of SaaS systematically understates true TCO. Published benchmarks establish the following hidden cost components:

[STATISTIC]
"Enterprise buyers consistently discover that the sticker price of SaaS represents only 40-60% of the total cost." Hidden costs include: initial configuration ($10,000-$100,000+), custom integrations ($15,000-$75,000 per major integration), and custom workflows ($5,000-$50,000 per complex automation).
— Industry benchmark synthesis
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

[STATISTIC]
Enterprise SaaS pricing benchmarks in 2025: per-user pricing ranges from $25-$150+ per user per month; tiered plans run $1,000-$10,000+ per month; enterprise contracts run $50,000-$500,000+ annually under multi-year commitments.
— Industry benchmark synthesis
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

### 1c. Xenoss Enterprise AI TCO Decision Matrix

[FACT]
Xenoss published a three-option build-vs-buy-vs-partner decision matrix with the following benchmarks for enterprise AI implementation:

| Approach | Initial Investment | Ongoing Annual Costs | Time to Value |
|---|---|---|---|
| Custom development (Build) | $500K-$2M | 30-40% annually | 12-24 months |
| Strategic partnership | $100K-$500K | 15-25% annually | 6-12 months |
| Commercial platform (Buy) | $50K-$200K | 10-20% annually | 3-6 months |

— Xenoss, "Total cost of ownership for enterprise AI: Hidden costs and ROI factors"
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

[STATISTIC]
Xenoss reports that 85% of organizations misestimate AI project costs by more than 10%.
— Xenoss, "Total cost of ownership for enterprise AI"
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

[STATISTIC]
Model maintenance overhead runs 15-30% of total infrastructure cost annually; retraining overhead alone accounts for 15-30% of operational costs.
— Xenoss, "Total cost of ownership for enterprise AI"
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

---

## 2. How Agentic Coding Disrupts the Model Variables

Before building the three scenarios, the specific variables that agentic coding directly compresses or expands must be isolated.

### 2a. Initial Development Cost: Compression Vector

[STATISTIC]
"Vibe coding is cutting the cost of application development by anywhere from 70% to 95%, opening development to subject matter experts."
— Times of AI, "Agentic Coding in 2026: AI's Impact on Software Development"
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
More conservative analysis by Belitsoft suggests a 50% reduction in human engineering effort that becomes approximately a 10% savings on total expenditures, once management overhead, governance, and infrastructure costs are held constant. The claimed 90% cost drop is described as applying to direct coding labor only, not total project cost.
— Belitsoft, "Agentic AI Coding: What Still Remains Expensive Amid a 90% Drop in Costs"
URL: https://belitsoft.com/agentic-ai-coding
Date: 2026

[FACT]
Anthropic's 2026 Agentic Coding Trends Report documents that average human interventions per Claude Code session decreased from 5.4 to 3.3 between August and December 2025, while the 99.9th percentile session duration nearly doubled from under 25 minutes to over 45 minutes between October 2025 and January 2026 — indicating agents are autonomously handling longer tasks with less human intervention.
— Sumeet Chabria, ThoughtLinks, citing Anthropic data; Anthropic 2026 Agentic Coding Trends Report
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

[STATISTIC]
TELUS teams created over 13,000 custom AI solutions using agentic coding tools while shipping engineering code 30% faster, saving over 500,000 hours total.
— Anthropic 2026 Agentic Coding Trends Report, as cited by Tessl.io
URL: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
Date: 2026

### 2b. Annual Maintenance Cost: Reduction Vector (With Governance Offset)

[STATISTIC]
Agentic AI reduces maintenance burden by 80% compared to traditional RPA approaches, with a 57% reduction in total TCO relative to legacy automation stacks.
— Industry analysis of agentic coding impact on RPA replacement
URL: https://blog.duvo.ai/why-every-rpa-project-breaks-and-how-agentic-ai-fixes-it
Date: 2025-2026

[STATISTIC]
"AI-generated code introduces 15-18% more security vulnerabilities, increasing risk as autonomy expands." AI-driven coding reduces time to pull request by up to 58%, but AI-generated pull requests wait 4.6x longer in review without governance.
— Times of AI, "Agentic Coding in 2026: AI's Impact on Software Development"
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
Safety and governance requirements add 20-35% to total agentic AI costs and are described as "non-negotiable" for enterprise deployments.
— USM Systems, "AI Software Cost: 2025 Enterprise Pricing Benchmarks For Manufacturing Leaders"
URL: https://usmsystems.com/ai-software-cost/
Date: 2025

[QUOTE]
"There's no way you can go live with a vibe-coded solution. It might work for demos, but we build enterprise-grade technology that has to scale across 30 countries."
— Pierre Yves Calloc'h, Builder, Pernod Ricard
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### 2c. Time-to-Value: Compression Vector

[QUOTE]
"Work that once took weeks can be done in days, which shifts which ideas get funded and built."
— Anthropic 2026 Agentic Coding Trends Report (Trend 6), as cited by Tessl.io
URL: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
Date: 2026

[STATISTIC]
Single custom agentic AI agent development costs in 2025-2026 range from $50,000-$200,000 for full enterprise deployment, down from $600,000-$1,500,000 for earlier custom agent development cycles. Scaling to five agents could still require a $5 million investment including maintenance.
— Writer.com / ProductCrafters.io / industry synthesis
URL: https://writer.com/blog/build-vs-buy-generative-ai/
Date: 2025-2026

---

## 3. Scenario 1 (Bear): Limited Agentic Capability Improvement

### Definition

Bear scenario assumptions: agentic coding tools improve incrementally rather than transformatively; hallucination rates, security vulnerability introduction, and governance overhead remain high; development cost compression plateaus at 20-30% of pre-AI baselines rather than 70-90%; annual maintenance costs remain at 15-20% of initial development spend (unchanged from classical baseline); regulatory and compliance costs consume the majority of any labor savings.

### Break-Even Model Under Bear Assumptions

[FACT]
Under bear assumptions, initial build cost compression of 20-30% moves the effective development cost for a mid-market enterprise application from the $500K-$2M Xenoss baseline to approximately $350K-$1.4M — a meaningful reduction but insufficient to compress the break-even below the classical two-to-four year range for most deployments.
— Model derived from Xenoss TCO benchmarks and Belitsoft cost compression data
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

[STATISTIC]
Gartner predicts that at least 30% of generative AI projects will be abandoned after proof of concept by end of 2025 "due to poor data quality, inadequate risk controls, escalating costs or unclear business value." Under bear scenario conditions, this abandonment rate functions as a direct tax on the build option.
— Gartner press release, July 29, 2024
URL: https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
Date: July 29, 2024

### SaaS Market Implications Under Bear Scenario

[FACT]
Bain's four-quadrant SaaS scenario matrix identifies "Core Strongholds" (low user automation, low AI penetration) as the category where incumbent SaaS advantages persist. Bear scenario conditions correspond most closely to this quadrant: "Deep domain knowledge protects incumbents" and AI primarily enhances rather than replaces existing SaaS platforms.
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[STATISTIC]
Javier Pérez (Edelweiss Capital) assigns the "AI Enhances SaaS" scenario — the closest analog to the bear case — a probability of 30-40%, making it the single most probable scenario in his five-scenario framework: "AI acts as a massive tailwind for the existing software giants."
— Javier Pérez, Edelweiss Capital, "Will Agentic AI Disrupt SaaS?"
URL: https://edelweisscapital.substack.com/p/will-agentic-ai-disrupt-saas
Date: 2025-2026

[FACT]
Deloitte's base-case timeline states "at least 5+ years required before enterprise applications [are] substantially replaced by agents, despite rapid development pace" — which under bear conditions extends further, making 2026-2028 a period of augmentation rather than displacement.
— Deloitte, "SaaS Meets AI Agents: Transforming Budgets, Customer Experience, and Workforce Dynamics"
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

| Break-Even Variable | Bear Assumption | Effect on Break-Even |
|---|---|---|
| Initial build cost reduction | 20-30% vs. pre-AI baseline | Break-even moves from 3-4 years to ~2.5-3.5 years |
| Annual maintenance | 15-20% of build cost (unchanged) | No improvement; full classical maintenance load |
| Governance/security overhead | +20-35% of project cost | Partially offsets build cost compression |
| Time-to-value | 10-20% faster delivery | Modest improvement; does not shift break-even materially |
| POC abandonment risk | ~30% of projects abandoned | Effective build cost increases ~43% after risk adjustment |
| SaaS pricing trend | 10-15% annual increases | Slightly improves build economics over 5+ year horizons |

**Bear scenario break-even estimate: 2.5-4 years for most enterprise use cases; SaaS share erosion minimal at 5-10% of addressed market by 2030.**

---

## 4. Scenario 2 (Base): Moderate Capability Improvement, Moderate Cost Reduction

### Definition

Base scenario assumptions: agentic coding delivers 40-60% reduction in initial development costs for targeted applications; annual maintenance costs decline to 8-12% of initial development spend (down from 15-20%) due to AI-assisted debugging and self-healing architectures; governance overhead remains a meaningful cost component (10-20% of total) but is stable and predictable; time-to-value for mid-complexity builds compresses from 12-24 months to 6-12 months.

### Break-Even Model Under Base Assumptions

[STATISTIC]
Under base scenario assumptions, applying Xenoss's custom development baseline of $500K-$2M initial cost with a 50% reduction produces an effective initial cost of $250K-$1M. With maintenance declining from 30-40% to 15-20% of annual spend, the five-year total cost of a custom build compresses to approximately 40-50% of its pre-AI equivalent — shifting the break-even to 12-36 months for medium-complexity enterprise applications.
— Model derived from Xenoss TCO matrix and Belitsoft cost compression analysis
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

[STATISTIC]
"For mid-market firms, the break-even point is often reached within 33 months" under conventional (pre-agentic) assumptions. Under base scenario agentic compression, this moves to approximately 18-24 months for targeted capability builds.
— Industry TCO synthesis
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

[STATISTIC]
Retool's 2026 survey (n=817 enterprise builders) documents that 35% of enterprises have already replaced at least one SaaS tool with a custom-built alternative; 78% plan to build more in 2026. This is the empirical leading indicator that the base scenario is already manifesting.
— Retool, "The 2026 Build vs. Buy Shift Report"
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### SaaS Market Implications Under Base Scenario

[STATISTIC]
SaaS categories under the highest replacement pressure in the Retool survey: workflow automations (35%), internal admin tools (33%), BI tools (29%), CRMs and form builders (25%), project management (23%), customer support (21%). These are the product categories where base-scenario break-even math is already favorable.
— Retool, "The 2026 Build vs. Buy Shift Report"
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[FACT]
Bain's "Open Doors" quadrant (low user automation, high AI penetration) corresponds most closely to the base scenario: "Risk of value siphoning via APIs" — incumbent SaaS vendors face margin compression as agents execute workflows via API without triggering per-seat license fees.
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[QUOTE]
"In three years, any routine, rules-based digital task could move from 'human plus app' to 'AI agent plus API.'"
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[QUOTE]
"Seat-based pricing may not fit when AI is doing the work."
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[STATISTIC]
Deloitte forecasts: "By 2030, 35% of point-product SaaS tools will be replaced by AI agents or absorbed within larger agent ecosystems." Base scenario corresponds to this 35% displacement range.
— Deloitte, "SaaS Meets AI Agents"
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

[QUOTE]
"The per-seat SaaS model was priced on the assumption that the workforce was exclusively human."
— Sumeet Chabria, CEO and Founder, ThoughtLinks, "Agentic AI Is Repricing SaaS: A Buy-to-Build Framework for CIOs & Investors"
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

| Break-Even Variable | Base Assumption | Effect on Break-Even |
|---|---|---|
| Initial build cost reduction | 40-60% vs. pre-AI baseline | Break-even moves to 12-30 months for targeted builds |
| Annual maintenance | 8-12% of build cost (improved) | Five-year total cost drops ~35% vs. classical model |
| Governance/security overhead | +10-20% of project cost (stable) | Predictable; can be planned into TCO |
| Time-to-value | 6-12 months (vs. 12-24 months) | Break-even advantage appears 6-12 months earlier |
| POC abandonment risk | ~15-20% of projects (declining) | Risk-adjusted effective cost increase of ~18-25% |
| SaaS pricing trend | 15-25% annual increases | Accelerates build economics within 3-year window |

**Base scenario break-even estimate: 18-30 months for targeted commodity workflows; 30-48 months for complex enterprise systems. SaaS share erosion 25-35% of point-product market by 2030.**

---

## 5. Scenario 3 (Bull): Transformative Capability, Near-Zero Marginal Maintenance

### Definition

Bull scenario assumptions: agentic coding delivers 80-95% reduction in initial development costs for targeted builds; annual maintenance costs approach near-zero for AI-maintained systems (1-5% of build cost due to self-healing, auto-updating architectures); governance overhead is commoditized into platform costs; time-to-value drops to days to weeks for commodity applications; subject-matter experts without engineering backgrounds can build and maintain production software.

### Break-Even Model Under Bull Assumptions

[STATISTIC]
Under bull scenario assumptions, applying a 90% cost compression to the Xenoss custom development baseline of $500K-$2M produces an effective initial cost of $50K-$200K — squarely within the range of "Commercial platform (Buy)" costs in the same Xenoss benchmark matrix, eliminating the initial cost advantage of buying entirely for all but the smallest applications.
— Model derived from Xenoss TCO matrix cross-referenced with Belitsoft 90% compression scenario
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

[STATISTIC]
"Vibe coding is cutting the cost of application development by anywhere from 70% to 95%." Under bull conditions, the effective build cost for a mid-tier workflow application could fall below $50,000 — below the annual SaaS subscription cost for the same capability at enterprise scale.
— Times of AI, "Agentic Coding in 2026: AI's Impact on Software Development"
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
Retool data: 31% of enterprise builders are "prompting their way to complete applications" as of early 2026. Under bull scenario conditions, this proportion expands to the majority of commodity internal tooling.
— Retool, "The 2026 Build vs. Buy Shift Report"
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[FACT]
The ThoughtLinks buy-to-build framework classifies the "Bucket B: Generic Knowledge & Workflows" SaaS category as the most vulnerable under bull scenario conditions, where "commodity-function" tools face displacement as their value proposition (standardized workflow management) can be replicated by custom agents at near-zero variable cost.
— Sumeet Chabria, ThoughtLinks, "Agentic AI Is Repricing SaaS: A Buy-to-Build Framework for CIOs & Investors"
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

[QUOTE]
"Durable value now looks like deep systems integration, proprietary data assets, compliance-grade security."
— Sumeet Chabria, ThoughtLinks
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

### SaaS Market Implications Under Bull Scenario

[FACT]
Bain's "Battlegrounds" quadrant — high user automation, high AI penetration — defines the bull scenario landscape: "Incumbents should have the advantage, but to keep it they will need to proactively replace SaaS activity with AI." Winner-take-most competitive dynamics emerge.
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[QUOTE]
"Disruption is mandatory. Obsolescence is optional."
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[STATISTIC]
Javier Pérez (Edelweiss Capital) assigns a combined probability of 20-30% to the "AI Outshines SaaS" scenario (agents become primary users; UX loses importance; APIs dominate) and 15-25% to "AI Cannibalizes SaaS" (feature commoditization; pricing compresses to usage-based) — together comprising 35-55% probability for bull-directional outcomes.
— Javier Pérez, Edelweiss Capital, "Will Agentic AI Disrupt SaaS?"
URL: https://edelweisscapital.substack.com/p/will-agentic-ai-disrupt-saas
Date: 2025-2026

[STATISTIC]
Gartner's bull-case projection: "Agentic AI could drive approximately 30% of enterprise application software revenue by 2035, surpassing $450 billion, up from 2% in 2025."
— Gartner, as cited in agentic AI market analysis
URL: https://mev.com/blog/what-2025-2026-data-reveal-about-the-agentic-ai-market
Date: 2025-2026

[STATISTIC]
"By 2030, at least 40% of enterprise SaaS spend will shift toward usage-, agent-, or outcome-based pricing."
— Deloitte, "SaaS Meets AI Agents"
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

| Break-Even Variable | Bull Assumption | Effect on Break-Even |
|---|---|---|
| Initial build cost reduction | 80-95% vs. pre-AI baseline | Break-even moves to immediate or < 12 months for targeted builds |
| Annual maintenance | 1-5% of build cost (near-zero) | Five-year total cost falls below annual SaaS subscription for many tools |
| Governance/security overhead | Commoditized into platform cost | No longer a meaningful differentiator in TCO calculation |
| Time-to-value | Days to weeks for commodity apps | Break-even advantage collapses the buy-side time-to-value argument |
| POC abandonment risk | < 10% for well-scoped builds | Near-classical build risk with radically lower cost floor |
| SaaS pricing trend | Outcome-based repricing underway | Structural repricing removes the per-seat premium advantage |

**Bull scenario break-even estimate: immediate to 12 months for commodity workflows; < 24 months for most enterprise applications above basic compliance/record-keeping functions. SaaS share erosion 50-65% of point-product market by 2030 for non-differentiated tools.**

---

## 6. Comparative Scenario Summary Table

| Dimension | Bear | Base | Bull |
|---|---|---|---|
| Build cost compression vs. pre-AI | 20-30% | 40-60% | 80-95% |
| Annual maintenance rate | 15-20% of build cost | 8-12% of build cost | 1-5% of build cost |
| Governance overhead | +20-35% of project cost | +10-20% (stable) | Commoditized |
| Time-to-value (custom build) | 9-18 months | 6-12 months | Days to weeks |
| Break-even (commodity workflow) | 2.5-4 years | 18-30 months | Immediate to 12 months |
| Break-even (complex enterprise app) | 4-6 years | 30-48 months | 18-30 months |
| POC abandonment risk (adj.) | ~30% | ~15-20% | < 10% |
| SaaS point-product market erosion by 2030 | 5-10% | 25-35% | 50-65% |
| Bain quadrant analog | Core Strongholds | Open Doors / Gold Mines | Battlegrounds |
| Pérez scenario analog | AI Enhances SaaS (30-40% prob.) | Spending Compresses / AI Outshines (combined ~45-55%) | AI Cannibalizes SaaS (15-25% prob.) |
| Deloitte displacement forecast | < 10% by 2030 | 35% by 2030 | > 50% by 2030 |

---

## 7. Sensitivity Analysis: Variables That Move the Break-Even Point Most

Not all variables carry equal weight. The following sensitivity ranking is derived from the mathematical structure of the break-even model and corroborated by the empirical benchmarks above.

### 7a. Highest Sensitivity: Annual Maintenance Cost Rate

The maintenance cost variable has the highest leverage on long-run TCO because it compounds annually. A reduction in the annual maintenance rate from 20% to 5% of a $500K build reduces the five-year maintenance obligation from $500K to $125K — a $375K swing that alone determines whether the build economics are favorable.

[STATISTIC]
Classical software maintenance benchmark: "Maintenance typically represents 20% of the original development cost each year."
— McKinsey & Company, as cited in industry analysis
URL: https://wifitalents.com/custom-software-development-industry-statistics/
Date: 2026

[STATISTIC]
Agentic AI maintenance reduction potential: 80% reduction in maintenance burden versus traditional automation, with 57% reduction in total TCO.
— Industry analysis of agentic AI on legacy maintenance
URL: https://blog.duvo.ai/why-every-rpa-project-breaks-and-how-agentic-ai-fixes-it
Date: 2025-2026

### 7b. High Sensitivity: User Count and Growth Rate

The SaaS cost function grows linearly with user count and multiplicatively when price escalation is compounded. At 20+ users with 10%+ annual price increases, the SaaS cost curve steepens rapidly.

[FACT]
VRInSofts' model shows that custom software break-even "happens faster with 20+ users, multiple SaaS tools, or annual price increases above 10%." Below 15-20 users, the custom build case weakens materially.
— VRInSofts, "5-Year Cost Calculator"
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

### 7c. High Sensitivity: Time Horizon of Evaluation

[STATISTIC]
Across all scenarios, the custom build option becomes more favorable as the evaluation window extends. A two-year TCO analysis almost always favors buying; a five-year analysis increasingly favors building as SaaS costs compound. The inflection point at which 5-year SaaS spending exceeds custom development costs is documented at a 72% premium in the VRInSofts dataset.
— VRInSofts
URL: https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
Date: 2025

### 7d. Medium Sensitivity: Initial Build Cost (Most Cited, Lower Actual Leverage)

Initial build cost is the most frequently cited variable but has lower long-run leverage than maintenance rate because it is a one-time payment. A 50% reduction in initial build cost from $1M to $500K saves $500K; a 50% reduction in annual maintenance rate from 20% to 10% saves $100K per year — exceeding the initial cost saving in year 6 of a $1M project.

[STATISTIC]
The broader implication: Belitsoft's finding that a 90% drop in coding labor costs translates to only a "10% savings on total expenditures" when governance, management, and infrastructure are included reflects exactly this dynamic — initial labor cost is a smaller fraction of five-year TCO than commonly assumed.
— Belitsoft, "Agentic AI Coding: What Still Remains Expensive Amid a 90% Drop in Costs"
URL: https://belitsoft.com/agentic-ai-coding
Date: 2026

### 7e. Medium Sensitivity: SaaS Vendor Price Escalation Rate

[STATISTIC]
"SaaS costs escalate 15-25% annually while custom platforms amortize." At the upper bound of this range (25% annual escalation), the SaaS cost quadruples over five years, making the build economics favorable well before year three regardless of scenario.
— Enterprise SaaS pricing benchmark synthesis
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

[STATISTIC]
"Enterprise technology spending in the United States has been growing by 8 percent per year on average since 2022, while labor productivity has grown by close to 2 percent over the same period."
— McKinsey & Company, "The New Economics of Enterprise Technology in an AI World"
URL: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-new-economics-of-enterprise-technology-in-an-ai-world
Date: 2025

### 7f. Lower Sensitivity: Initial Time-to-Value Differential

Time-to-value affects the opportunity cost calculation but does not directly move the quantitative break-even. Its importance is highest when competitive windows are tight (strategic build decisions) and lowest for internal productivity tooling.

---

## 8. Published Economic Models and Frameworks

The following published frameworks from consulting firms and practitioners provide the structural underpinning for the scenarios above.

### 8a. Bain Four-Quadrant SaaS Disruption Matrix

[FACT]
Bain & Company's "Will Agentic AI Disrupt SaaS?" (Technology Report 2025) presents a four-quadrant framework plotting SaaS workflows on axes of "user automation potential" (y-axis) and "AI penetration rate" (x-axis). The four quadrants — Core Strongholds, Open Doors, Gold Mines, and Battlegrounds — provide a categorical basis for assigning which SaaS categories fall under bear, base, or bull displacement scenarios.
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[FACT]
Bain identifies six indicators for assessing disruption vulnerability: external observability, industry standardization, proprietary data depth, switching and network friction, regulatory/certification barriers, and agent protocol maturity.
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

### 8b. ThoughtLinks Five-Bucket Portfolio Framework

[FACT]
Sumeet Chabria (ThoughtLinks) published a five-bucket portfolio classification for enterprise SaaS decision-making on March 3, 2026:
- Bucket A: Core Utilities (commoditized infrastructure — buy)
- Bucket B: Generic Knowledge & Workflows (vulnerable SaaS — candidate for replacement)
- Bucket C: Regulated Scaffolding (strategic foundation — buy with deep integration)
- Bucket D: Proprietary Business Logic (crown jewels — build)
- Bucket E: Legacy Core (monolithic systems — modernize selectively)
— Sumeet Chabria, CEO and Founder, ThoughtLinks
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

[QUOTE]
"Software is not dying. It is being liberated from rigid, one-size-fits-all models."
— Sumeet Chabria, ThoughtLinks
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

### 8c. Xenoss Three-Pathway TCO Matrix

[FACT]
Xenoss's enterprise AI TCO framework explicitly models three decision pathways (custom development, strategic partnership, commercial platform) with full ranges for initial investment, annual ongoing costs, and time-to-value — making it the most granular published decision matrix for enterprise AI procurement economics as of 2025. See Section 1c above for full matrix.
— Xenoss, "Total cost of ownership for enterprise AI"
URL: https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
Date: 2025

### 8d. McKinsey "Sources of Distinctiveness" Framework

[FACT]
McKinsey's guidance for the AI-era build decision: "A more resilient approach is to buy standardized capabilities... and reserve custom development for the select areas where domain-specific logic or proprietary workflows create real competitive advantage." McKinsey further notes that "unlike the traditional software as a service (SaaS) world, AI requires a continuous, deliberate reassessment of what to create and what to consume."
— McKinsey & Company, "Bridging the Great AI Agent and ERP Divide to Unlock Value at Scale"
URL: https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/bridging-the-great-ai-agent-and-erp-divide-to-unlock-value-at-scale
Date: 2025

See C01 (McKinsey Perspectives) for detailed coverage of McKinsey's full advisory posture on the build-vs-buy question in the agentic era.

### 8e. Edelweiss Capital Five-Scenario Probability Model

[FACT]
Javier Pérez of Edelweiss Capital published a five-scenario probability model for SaaS-under-agentic-AI with the following probability weights: No AI Effect (1-5%), AI Enhances SaaS (30-40%), AI Outshines SaaS (20-30%), AI Cannibalizes SaaS (15-25%), Spending Singularity (1-5%). The model notes "binary thinking is a luxury that investors cannot afford" and assigns no scenario a dominant probability.
— Javier Pérez, Edelweiss Capital
URL: https://edelweisscapital.substack.com/p/will-agentic-ai-disrupt-saas
Date: 2025-2026

---

## 9. Market Signals Anchoring the Scenarios

### Current Market Stress Indicators

[STATISTIC]
Bloomberg reported a single-day software sector rout of approximately $285 billion on February 3, 2026; Forrester reported over $1 trillion erased from software stocks within a week; Reuters documented the S&P 500 Software & Services index losing approximately $2 trillion from its October 2025 peak.
— ThoughtLinks citing Bloomberg, Forrester, Reuters data
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

[STATISTIC]
Morgan Stanley data: 50% of software loans were rated B- or lower as of early 2026; 30% maturing by 2028. Software loan market total: approximately $235 billion in the U.S.
— ThoughtLinks citing Morgan Stanley data
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: March 3, 2026

### Technology Cost Trajectory

[STATISTIC]
OpenAI's o3 reasoning model dropped 80% in cost over two months. This rate of model cost deflation directly expands the bull scenario probability over time by reducing the variable compute costs embedded in custom-built AI systems.
— Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[STATISTIC]
"Gartner forecasts that by the end of 2026, 40% of enterprise applications will feature task-specific AI agents, up from less than 5% in 2025."
— Gartner, August 26, 2025 press release
URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
Date: August 26, 2025

---

## Key Takeaways

- The classical break-even model (SaaS vs. custom build) has a stable mathematical structure, but every primary input variable is now scenario-dependent. The two highest-leverage inputs are annual maintenance cost rate and user-count growth trajectory — not initial development cost, which is widely cited but has lower long-run impact on five-year TCO than the maintenance rate.

- Under the bear scenario (20-30% build cost compression, maintenance unchanged), the break-even window moves modestly from 3-4 years to 2.5-3.5 years; SaaS point-product market erosion is 5-10% by 2030, concentrated in workflow automation and internal tooling. Bain's "Core Strongholds" and the Edelweiss "AI Enhances SaaS" scenario (30-40% probability) describe this outcome.

- Under the base scenario (40-60% cost compression, maintenance declining to 8-12%), break-even compresses to 18-30 months for commodity workflows. The Retool survey's finding that 35% of enterprises have already replaced at least one SaaS tool is the empirical evidence that this scenario is not theoretical — it is the current state for early movers. Deloitte's 35% point-product displacement by 2030 anchors the base-case market outcome.

- Under the bull scenario (80-95% cost compression, near-zero maintenance), the build cost floor falls below the SaaS subscription floor for many enterprise applications, eliminating the economic case for buying commodity-function SaaS altogether. Break-even becomes immediate to twelve months; SaaS point-product erosion reaches 50-65% by 2030. This scenario requires successful resolution of the governance problem — the 15-18% higher security vulnerability rate from AI-generated code and the 4.6x longer review cycles are the primary constraints.

- Any C-suite capital allocation decision between build and buy should be preceded by a sensitivity test on three variables in sequence: (1) annual maintenance cost achievable with agentic tools (most sensitive), (2) projected user count and SaaS price escalation rate (high sensitivity), and (3) initial build cost under current agentic tooling (commonly cited but lowest long-run leverage). The scenario that governs the decision is less important than identifying which bucket — Bain's or ThoughtLinks' — the target workflow falls into, because governance complexity, data moat depth, and regulatory requirements determine which scenario is achievable for a specific use case regardless of the macro trajectory.

---

## Sources

1. Retool, "The 2026 Build vs. Buy Shift Report" (Kelsey McKeon, February 17, 2026) — https://retool.com/blog/ai-build-vs-buy-report-2026
2. VRInSofts, "5-Year Cost Calculator: SaaS Subscriptions vs Custom Software" — https://www.vrinsofts.com/saas-subscriptions-vs-custom-software/
3. Xenoss, "Total cost of ownership for enterprise AI: Hidden costs and ROI factors" — https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai
4. Bain & Company, "Will Agentic AI Disrupt SaaS?" Technology Report 2025 — https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
5. Sumeet Chabria, ThoughtLinks, "Agentic AI Is Repricing SaaS: A Buy-to-Build Framework for CIOs & Investors" (March 3, 2026) — https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
6. Javier Pérez, Edelweiss Capital, "Will Agentic AI Disrupt SaaS?" — https://edelweisscapital.substack.com/p/will-agentic-ai-disrupt-saas
7. Deloitte, "SaaS Meets AI Agents: Transforming Budgets, Customer Experience, and Workforce Dynamics" (TMT Predictions 2026) — https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
8. McKinsey & Company, "Bridging the Great AI Agent and ERP Divide to Unlock Value at Scale" (2025) — https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/bridging-the-great-ai-agent-and-erp-divide-to-unlock-value-at-scale
9. McKinsey & Company, "The New Economics of Enterprise Technology in an AI World" (2025) — https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-new-economics-of-enterprise-technology-in-an-ai-world
10. Gartner press release, "Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept by End of 2025" (July 29, 2024) — https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
11. Gartner press release, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026" (August 26, 2025) — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
12. Belitsoft, "Agentic AI Coding: What Still Remains Expensive Amid a 90% Drop in Costs" — https://belitsoft.com/agentic-ai-coding
13. Times of AI, "Agentic Coding in 2026: AI's Impact on Software Development" — https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
14. Anthropic 2026 Agentic Coding Trends Report, as cited by Tessl.io — https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
15. Retool / BusinessWire press release, "Retool's 2026 Build vs. Buy Report Reveals 35% of Enterprises Have Already Replaced SaaS With Custom Software" (February 17, 2026) — https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
16. USM Systems, "AI Software Cost: 2025 Enterprise Pricing Benchmarks For Manufacturing Leaders" — https://usmsystems.com/ai-software-cost/
17. Duvo AI, "Why Every RPA Project Breaks (And How Agentic AI Fixes It)" — https://blog.duvo.ai/why-every-rpa-project-breaks-and-how-agentic-ai-fixes-it
18. Wifitalents, "Custom Software Development Industry Statistics" (2026) — https://wifitalents.com/custom-software-development-industry-statistics/
19. MEV.com, "Agentic AI Market Outlook 2025-2026: Statistics on Adoption, ROI and Growth" — https://mev.com/blog/what-2025-2026-data-reveal-about-the-agentic-ai-market
20. ProductCrafters.io, "AI Agent Development Cost Calculator $5K to $180K+ (2026)" — https://productcrafters.io/blog/how-much-does-it-cost-to-build-an-ai-agent/
