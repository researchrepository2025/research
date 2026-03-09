# L1 Wave 3 Summary: Enterprise CTO/CIO Perspectives on Build vs. Buy
**Synthesis Layer:** 1 | **Source Wave:** 3 | **Documents:** E01–E07
**Date Produced:** 2026-03-06
**Analyst:** Synthesis Layer 1 Agent

---

## 1. Wave Theme

Enterprise CTO and CIO perspectives from 2025–2026 reveal a structural shift in build-vs-buy calculus that is real, directional, and durable — but decisively slower and more bounded than VC narratives suggest. The dominant posture is **hybrid orchestration**: enterprises buy compliance infrastructure, data layers, and certifications from incumbent SaaS vendors while building intelligence, workflow, and differentiated-logic layers internally. Three converging forces are reshaping the equation: AI-assisted development has materially collapsed the cost and time of custom software (35% of enterprises have already replaced at least one SaaS tool, per [Retool's 817-respondent survey](https://retool.com/blog/ai-build-vs-buy-report-2026)); agentic AI is absorbing business logic that once locked organizations into SaaS workflows; and shadow IT at scale — with 60% of builders circumventing IT oversight — is surfacing latent demand that packaged software never fully served. Yet Fortune 500 CIOs are proceeding with deliberate risk calibration. The structural barriers that modulate replacement speed — certification cost walls (FedRAMP alone costs $250K–$1.5M), security debt in AI-generated code (45% failure rate, per [Veracode](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)), a U.S. senior engineering shortfall of 1.2 million developers, and integration complexity across 897-application enterprise estates — are not being eliminated by agentic tools; in some dimensions, they are being worsened. The wave verdict is that enterprise buyers are the critical moderating force between the bull and bear SaaS scenarios: they are moving toward building more, but the pace, category selectivity, and governance constraints they impose mean SaaS displacement will be measured in years, not quarters.

---

## 2. Key Evidence for Each Scenario

### Bull Case: SaaS Remains Dominant (60%+ market share in 5 years)

- [Deloitte found externally-built agentic tools demonstrate nearly double employee usage rates and twice the likelihood of reaching full deployment compared to internally developed solutions](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html), directly undermining the premise that internal builds routinely succeed at scale.

- [Forrester projects global SaaS spending to rise from $318 billion in 2025 to $576 billion by 2029](https://www.cio.com/article/4104365/saas-price-hikes-put-cios-budgets-in-a-bind.html), despite rising lock-in concerns — absolute spend growth points to SaaS remaining the dominant procurement mode.

- [The a16z survey of 100 enterprise CIOs found "a marked shift towards buying third-party applications over the last twelve months as the ecosystem of AI apps has started to mature"](https://a16z.com/ai-enterprise-2025/), and over 90% were testing third-party customer support applications — a category previously earmarked for internal builds.

- [FedRAMP compliance costs $250,000 to $1.5 million; government ATOs require 6–18 months and hundreds of senior engineer-hours](https://www.workstreet.com/blog/fedramp-certification-cost), making regulated-sector SaaS replacement economically prohibitive for all but the largest enterprises.

- [Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) — attrition at this scale removes the supply-side pressure needed to erode SaaS dominance.

- [S&P Global found companies abandoning the majority of AI initiatives before production surged from 17% in 2024 to 42% in 2025](https://www.spglobal.com/market-intelligence/en/news-insights/research/ai-experiences-rapid-adoption-but-with-mixed-outcomes-highlights-from-vote-ai-machine-learning), indicating that the pilot-to-production gap remains wide.

- [Gartner projects global enterprise software spend will grow 14.7% in 2026 to $1.4 trillion](https://www.saastr.com/gartner-business-software-spend-will-grow-a-stunning-14-7-in-2026-to-1-4-trillion-up-from-11-5-in-2025-are-you-grabbing-it/) — rising spend suggests SaaS incumbents are capturing, not losing, the AI transition.

- [Only 2% of businesses have successfully integrated more than half of their applications](https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/), and 95% of IT leaders report integration as a hurdle to AI — making SaaS platforms that already integrate across ecosystems structurally advantaged.

- [Torii's 2026 SaaS Benchmark Report found AI is accelerating software adoption, not cutting it: "There's a growing narrative that AI will replace traditional software. What our data actually shows is the opposite"](https://ai-techpark.com/torii-2026-ai-expands-shadow-it-not-saas-cuts/) — Uri Haramati, CEO, Torii.

### Base Case: SaaS Stays Majority but Declines (45–60% market share)

- [35% of enterprises have already replaced at least one SaaS tool with a custom build, and 78% expect to build more in 2026](https://retool.com/blog/ai-build-vs-buy-report-2026) — directional evidence of real, broad-based displacement already underway across mid-market and enterprise.

- [SaaS categories under the highest replacement pressure include workflow automations (35%), internal admin tools (33%), BI tools (29%), CRMs/form builders (25%), project management (23%), and customer support (21%)](https://retool.com/blog/ai-build-vs-buy-report-2026) — these represent substantial but bounded segments of the total SaaS market.

- [Gartner projects 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from less than 5% in 2025](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025), indicating the SaaS/agent boundary will blur rather than SaaS being wholesale replaced.

- [Deloitte (Ayo Odusote) identifies a "hybrid" trajectory: "Many enterprises will ultimately balance both approaches rather than choosing one exclusively"](https://www.cio.com/article/4131904/saas-isnt-dead-the-market-is-just-becoming-more-hybrid.html), with dev tools, cybersecurity, and industry-specific systems moving at different paces.

- [The EU Data Act effective September 12, 2025 bans exit fees by January 2027, mandates two-month termination rights, and requires machine-readable data transfers](https://www.addleshawgoddard.com/en/insights/insights-briefings/2025/data-protection/eu-data-act-gamechanger-saas-contracts/) — regulatory dismantling of contractual lock-in accelerates selective vendor replacement in EU markets.

- [SaaS inflation is running at 12.2%, 4.5x higher than G7 general inflation at 2.7%](https://www.vertice.one/l/saas-inflation-index-report), and 61% of IT leaders were forced to cut projects due to unplanned SaaS cost increases — pricing pressure is accelerating build decisions in parallel with capability improvements.

- [Mid-market companies (500–10,000 employees) experienced approximately 40% year-over-year per-employee SaaS spend growth in 2025](https://threadgoldconsulting.com/research/saas-spend-per-employee-benchmarks-2025), creating strong economic incentive to replace at least some subscriptions.

- [Goldman Sachs Research forecasts AI agents will account for more than 60% of software economics by 2030](https://www.goldmansachs.com/insights/articles/ai-agents-to-boost-productivity-and-size-of-software-market), though this is a growth share of an expanding market rather than absolute SaaS decline.

- [Bain & Company's "Will Agentic AI Disrupt SaaS?" identifies "battleground" categories (Intercom support, Tipalti invoicing, ADP time-entry) as replaceable while "core strongholds" (Procore, Medidata) remain durable](https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/) — a tiered displacement pattern consistent with the base case.

### Bear Case: SaaS Significantly Eroded (<45% market share)

- [Bill Vass, CTO of Booz Allen Hamilton, stated: "The thing with agentic systems is now you can have agents just read your business policies and generate the software. This is going to disintermediate these SaaS vendors and these ERP vendors"](https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas) — a named senior enterprise leader explicitly predicting structural disintermediation.

- [Tatyana Mamut, Former VP at Salesforce, expects the SaaS market to "majorly shrink" within five years](https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas).

- [Satya Nadella, CEO of Microsoft, stated: "The business logic is all going to these agents. They're not going to discriminate between what the backend is — they'll update multiple databases, and all the logic will be in the AI tier"](https://www.windowscentral.com/microsoft/hey-why-do-i-need-excel-microsoft-ceo-satya-nadella-foresees-a-disruptive-agentic-ai-era-that-could-aggressively-collapse-saas-apps) — effectively predicting the SaaS application layer becomes irrelevant to end users.

- [Capital One built a proprietary multi-agentic Chat Concierge on Llama, reducing latency fivefold and achieving 55% higher lead conversion](https://fortune.com/2025/12/15/agentic-artificial-intelligence-automation-capital-one/) — a production-scale custom build from a regulated financial institution demonstrating the model is technically viable even under heavy compliance constraints.

- [The Retool survey found 64% of shadow IT builders were senior managers and above](https://retool.com/blog/ai-build-vs-buy-report-2026), meaning the build impulse is executive-driven and will not be governed away; it will be formalized upward.

- [ThoughtLinks analysis documented $285 billion erased in a single-day software sector rout (February 3, 2026) and approximately $2 trillion lost from the S&P 500 Software & Services index since October 2025 peak](https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework) — the capital markets have already priced in a significantly disrupted SaaS landscape.

- [Bain & Company estimates that as much as half of overall enterprise technology spending could shift to AI agents running across the enterprise](https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/) — if realized, this represents a structural reallocation away from current SaaS at a scale that would reduce market share below 45%.

- [Agentic coding tools are widening productivity gaps in favor of enterprises that already have strong engineering: senior engineers realize nearly 5x the gains of junior engineers from agentic tools](https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/), meaning Fortune 500 firms with engineering depth (Goldman, JPMorgan, Capital One) will disproportionately build rather than buy.

---

## 3. Named Expert Positions

| Name | Title / Org | Position on SaaS Durability | Source URL |
|------|-------------|----------------------------|------------|
| Marco Argenti | CTO / CIO, Goldman Sachs | Hybrid builder: build multi-LLM internal platforms; remain "plug-and-play" with vendors | https://fortune.com/2025/03/19/goldman-sachs-cio-ai/ |
| Lori Beer | Global CIO, JPMorgan Chase | Buy the AI platform infrastructure; build specific copilots on top; target "fully AI-connected enterprise" | https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html |
| Prem Natarajan | Head of Enterprise AI, Capital One | Build proprietary agentic stack on open-source LLMs for competitive differentiation | https://fortune.com/2025/12/15/agentic-artificial-intelligence-automation-capital-one/ |
| Aditya Bhasin | CTO, Bank of America | AI-driven internal transformation (90% tool adoption, $4B investment); primarily buy-and-augment | https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to |
| David Griffiths | CTO, Citigroup | Deploy at scale (GitHub Copilot to 40,000 developers); agentic as productivity multiplier, not SaaS replacement | https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to |
| John Roese | Global CTO / Chief AI Officer, Dell Technologies | Agent-as-collective-skills strategy; buy into AI-native ecosystems rather than replace SaaS | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html |
| Marie Myers | EVP and CFO, HPE | Cautious governor: select end-to-end process transformation, not point-pain fixes | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html |
| Jason Ballard | VP Digital Innovations, Toyota | Build: agentic AI for pre-shift autonomous preparation; committed to investing | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html |
| Tracey Franklin | Chief People and Digital Technology Officer, Moderna | Hybrid workforce planning; AI as organizational design question, not pure SaaS replacement | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html |
| Brent Collins | Head of Global SI Alliances, Intel | Cautious governor: workflow reimagination before technology layering | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html |
| Maribel Solanas Gonzalez | Group Chief Data Officer, Mapfre | Explicitly hybrid by design; not a SaaS replacement thesis | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html |
| Sumeet Chabria | CEO & Founder, ThoughtLinks (former Global COO Tech/Ops, Bank of America; Global CIO Banking & Markets, HSBC) | Bear-leaning: markets repricing software because control is shifting; CIOs should classify SaaS portfolios and build for proprietary business logic | https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework |
| David Hsu | CEO & Founder, Retool | Bear-leaning: default question shifting from "What should we buy?" to "Can we build this?"; SaaS subscription economics under structural pressure | https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483 |
| Bill Vass | CTO, Booz Allen Hamilton | Bear: agentic systems will disintermediate SaaS and ERP vendors structurally | https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas |
| Tatyana Mamut | Former VP, Salesforce | Bear: SaaS market will "majorly shrink" within five years | https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas |
| Satya Nadella | CEO, Microsoft | Bear on traditional SaaS: business logic migrating to AI tier; "thirty years of change compressed into three years" | https://www.windowscentral.com/microsoft/hey-why-do-i-need-excel-microsoft-ceo-satya-nadella-foresees-a-disruptive-agentic-ai-era-that-could-aggressively-collapse-saas-apps |
| Anushree Verma | Senior Director Analyst, Gartner | Base: agentic AI evolving from embedded assistants to multi-agent ecosystems by 2029; 40%+ projects will be canceled by 2027 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 |
| Ayo Odusote | Software and Platforms Leader, Deloitte | Base: market becoming more hybrid; vendors must earn renewal, not extract it | https://www.cio.com/article/4131904/saas-isnt-dead-the-market-is-just-becoming-more-hybrid.html |
| Uri Haramati | Co-founder and CEO, Torii | Bull: AI is accelerating software adoption across the enterprise, not cutting it | https://ai-techpark.com/torii-2026-ai-expands-shadow-it-not-saas-cuts/ |
| Tamar Yehoshua | Chief Product Officer, Atlassian | Bull: "SaaS isn't disappearing. Organizations still need software and communication tools" | https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas |
| Faisal Masud | EVP Digital Services, HP | Bear on pricing: "SaaS pricing was completely out of bounds for economic buyers" | https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas |
| Alexey Korotich | Chief Product Officer, Wrike | Bull on maintenance moat: "Building dashboards takes an hour, but scaling with features and bug fixes requires team resources" | https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas |
| Nitin Mittal | Global AI Leader, Deloitte | Base: organizations pivoting from experimentation to integrating AI into core business at scale | https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html |
| Steve Chase | U.S. Vice Chair, Global Head of AI and Digital Innovation, KPMG | Base-to-bull: "Results are visible, tangible, and compounding quickly" — but through AI investment, not SaaS displacement | https://kpmg.com/us/en/media/news/q3-ai-pulse.html |
| Hani Arab | CIO, Seymour Whyte Construction | Base: hybrid approaches enabled by low-code, API-first, and microservices architectures | https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html |
| Mark Hughes | Global Managing Partner, Cybersecurity Services, IBM | Bear on security: "Attackers aren't reinventing playbooks, they're speeding them up with AI" — 44% increase in attacks on public-facing applications | https://newsroom.ibm.com/2026-02-25-ibm-2026-x-force-threat-index-ai-driven-attacks-are-escalating-as-basic-security-gaps-leave-enterprises-exposed |
| Borys Aptekar | GTM AI Product Manager, ClickUp | Bear: "We realized we could build these tools ourselves and save on multiple subscriptions" — $200K/year in SaaS eliminated | https://retool.com/blog/ai-build-vs-buy-report-2026 |
| Miles Konstantin | Head of Automation, Harmonic | Bear: replaced $20,000/year SaaS tool by rebuilding in Retool | https://retool.com/blog/ai-build-vs-buy-report-2026 |
| Pierre Yves Calloc'h | Enterprise tools builder, Pernod Ricard | Bull on enterprise-grade moat: "There's no way you can go live with a vibe-coded solution. It might work for demos" | https://retool.com/blog/ai-build-vs-buy-report-2026 |
| Ethan Mollick | Professor, Wharton School | Bear-leaning: "True agents are already here. You're just not using them. But it's doable today" | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html |
| Martin Fowler | Chief Scientist, Thoughtworks | Bull on governance moat: "I still cannot imagine a future where I'm OK being on call for an important application when AI just autonomously wrote and deployed 1,000 lines of code" | https://khiliad.com/blog/real-impact-of-ai-in-development |
| David Cramer | CEO, Sentry | Bull on current limits: "You cannot use these agents to build software today… they don't replace engineering" | https://addyo.substack.com/p/the-reality-of-ai-assisted-software |

---

## 4. Key Data Points for the Position Paper

1. **35% replacement baseline, 78% intend more** — [Retool 2026 Build vs. Buy Report (n=817, late 2025)](https://retool.com/blog/ai-build-vs-buy-report-2026): 35% of enterprises have already replaced at least one SaaS tool with a custom build; 78% expect to build more custom internal tools in 2026. This is the most concrete behavioral signal of the shift underway.

2. **42% of AI initiatives abandoned before production** — [S&P Global, Voice of the Enterprise 2025 (n=1,006 IT and LoB professionals, North America and Europe)](https://www.spglobal.com/market-intelligence/en/news-insights/research/ai-experiences-rapid-adoption-but-with-mixed-outcomes-highlights-from-vote-ai-machine-learning): The share of companies abandoning the majority of AI initiatives before reaching production surged from 17% in 2024 to 42% in 2025. Ambition outpaces execution at nearly 3:1.

3. **AI-generated code introduces security flaws in 45% of cases** — [Veracode 2025 GenAI Code Security Report (100+ LLMs, 80 tasks)](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/): Java code fails at 72%. This is not a vendor claim — it is a controlled multi-LLM study quantifying the structural security cost of the custom-build path.

4. **FedRAMP costs $250K–$1.5M; SOC 2 Type 2 costs $75K–$200K** — [Workstreet](https://www.workstreet.com/blog/fedramp-certification-cost) / [dsalta.com](https://www.dsalta.com/resources/articles/soc-2-certification-2025-auditor-cost-timeline-guide): Certification costs are multi-year moats. Regulated enterprises replacing certified SaaS absorb these costs entirely and independently — no vendor indemnification exists for custom software.

5. **Experienced developers took 19% longer with AI tools** — [METR randomized controlled trial (July 2025, n=16 experienced open-source developers, 246 tasks, repositories averaging 22,000+ stars)](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/): Developers predicted a 24% speedup and still believed AI had helped after the trial. The productivity gains most often cited are real for simple tasks but may not hold for complex enterprise codebases.

6. **Only 25% of organizations have moved 40%+ of AI pilots to production; only 21% have mature governance models** — [Deloitte State of AI 2026 (n=3,235, 24 countries)](https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html). The deployment maturity gap is the primary constraint on build-scenario realization.

7. **Only 2% of businesses have successfully integrated more than half of their applications** — [MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)](https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/): The average enterprise manages 897 applications. Integration failure is the structural constant that both impedes SaaS replacement and maintains SaaS hub value.

8. **Capital One's custom multi-agent build: 5x latency reduction, 55% higher lead conversion** — [VentureBeat / Fortune (2025)](https://venturebeat.com/ai/how-capital-one-built-production-multi-agent-ai-workflows-to-power-enterprise-use-cases): A production-scale regulated-industry proof point that custom agentic builds are not merely theoretical — they work in compliance-constrained environments.

9. **SaaS inflation running at 12.2%, 4.5x general G7 inflation; 61% of IT leaders cut projects due to unplanned SaaS cost increases** — [Vertice SaaS Inflation Index 2026](https://www.vertice.one/l/saas-inflation-index-report) / [Zylo 2026 SaaS Management Index](https://www.prweb.com/releases/zylos-2026-saas-management-index-finds-ai-native-app-adoption-is-surging-with-chatgpt-now-the-most-expensed-app-302673438.html): Vendor pricing behavior is itself an accelerant of the build-vs-buy shift, independent of agentic AI capability.

10. **Gartner: agentic AI to represent 30% of enterprise software revenue (~$450B) by 2035** — [Gartner, via UC Today (August 2025)](https://www.uctoday.com/unified-communications/gartner-predicts-40-of-enterprise-apps-will-feature-ai-agents-by-2026/): This is a growth-share scenario in an expanding market, not an absolute SaaS revenue decline — a critical distinction for framing scenarios. The total application software market itself may reach [$780 billion by 2030 per Goldman Sachs Research](https://www.goldmansachs.com/insights/articles/ai-agents-to-boost-productivity-and-size-of-software-market).

---

## 5. Critical Caveats for Synthesis

### Survey Bias and Respondent Self-Selection

- **Retool survey (n=817)** is the most-cited data source in Wave 3. It surveys Retool's own customer base and self-selected builders — a population structurally predisposed toward building. Headline figures (35% replacement, 78% intent to build more) will overstate the broader enterprise market's behavior. The position paper should present these as upper-bound signals from early adopters, not population means.

- **a16z enterprise CIO survey (n=100)** is directionally credible but small. The "marked shift toward buying" finding conflicts with Retool's headline; the difference is almost certainly sample composition (a16z's 100 CIOs skew toward larger, more technically mature firms evaluating the AI app market).

- **KPMG Q3 2025 survey (n=130, $1B+ revenue organizations)** captures large enterprises only; findings about 95% technology AI agent adoption reflect the most capable segment, not the population.

### Attribution and Methodology Gaps

- Multiple statistics from E02 and E05 are attributed through secondary summaries (Threadgold citing Zylo, Axis Intelligence citing multiple sources) without primary links. These should be treated as indicative, not definitive, in the position paper.

- The **METR RCT** (19% slowdown) had 16 participants and used open-source contributors — not enterprise developers in enterprise codebases. The result is analytically important but may not generalize to enterprise settings where AI tools are configured, customized, and governed.

- **E06's productivity statistics** from Michael Hospedales (hospedales.com) are analyst commentary without disclosed methodology. The figures (89% higher bug rates, 3.4x longer modification time for high-AI code) are internally coherent but lack peer-reviewed status.

### Conflicts and Competing Narratives Within the Wave

- **Torii (2026 Benchmark)** and **Retool (2026 Build vs. Buy)** directly contradict each other on trend direction: Torii finds AI is accelerating SaaS adoption; Retool finds replacement is underway. Both are vendor-produced research with commercial incentives aligned with their respective finding. Neither should be treated as neutral.

- **Security evidence cuts both ways**: the shared responsibility model means SaaS customers already bear most breach risk (Gartner: 99% of cloud security failures are customer-caused), which reduces one argument for keeping SaaS. But custom builds absorb additional code-level and infrastructure security risk that SaaS externalizes.

- **Agentic tools may simultaneously widen and narrow the talent gap**: senior engineers gain 5x more than junior engineers (Anthropic 2026 report) — widening within-enterprise performance gaps while potentially enabling some smaller firms to approximate larger-firm capability on bounded tasks.

- **The lock-in paradox**: agentic workflow prompt engineering creates new LLM-layer lock-in even as EU Data Act dismantles contractual SaaS lock-in. Enterprises may exit SaaS contracts only to enter AI infrastructure dependencies.

### Scope Boundary Gaps

- E01 covers Fortune 500 CTO/CIO views but most named case studies (Rakuten, ClickUp, Harmonic, Fountain) skew toward technology-native firms rather than traditional industrial or regulated enterprises. Manufacturing, healthcare, and government CIO perspectives are underrepresented in the named executive quotation set.

- E02 lacks named mid-market CTO/CIO individuals. All mid-market positions are attributed to analysts and consultants (Futurum, Deloitte, ThoughtLinks) rather than buyers. This leaves the most pivotal segment — where the "punch above weight" thesis lives — with no primary executive testimony.

---

## 6. Wave Verdict

Enterprise buyer perspectives from Wave 3 make the **base case the most empirically supported scenario**: SaaS remains the majority procurement method for enterprise software in five years, but its share declines meaningfully from current levels as selective replacement accelerates in workflow automation, internal tooling, BI, and CRM categories while regulated core systems (ERP, payroll, HCM, cybersecurity) remain structurally durable. The bull case requires that current enterprise execution constraints — a 42% pilot abandonment rate, the integration complexity constant, the certification cost wall, and the AI code security failure rate — persist unchanged, which is improbable given the pace of infrastructure maturation (MCP reaching 97M+ monthly SDK downloads in one year, Deloitte projecting 75% of companies will invest in agentic AI by 2026). The bear case requires Fortune 500 and mid-market enterprises to develop the governance maturity, DevOps sophistication, and security infrastructure to build and maintain production-grade custom software at meaningful scale within five years — which is also possible but faces the hard constraint that [only 21% of organizations currently have mature governance models for agents](https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html) and [approximately 80% of agentic coding tool users are currently getting net-negative value from them](https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/). The enterprise buyer data strongly suggests that the transition will be category-specific, capability-gated, and measured in years — closer to the cloud migration (decade-long) than the SaaS-overthrew-on-premise transition narrative implies. Named enterprise technologists who have actually deployed (Goldman Sachs, JPMorgan, Capital One, Toyota, Walmart) are pursuing hybrid orchestration, not SaaS replacement — and their actual budget allocations carry more predictive weight than either VC proclamations or analyst projections.

---

## Source Files

| File | Topic |
|------|-------|
| E01 | Fortune 500 CTO/CIO views — Goldman Sachs, JPMorgan, Capital One, Bank of America, Citigroup, Dell, HPE, Toyota, Moderna |
| E02 | Mid-market enterprise views — resource constraints, SaaS dependency, agentic adoption appetite |
| E03 | Enterprise lock-in and switching costs — EU Data Act, SaaS inflation, agentic lock-in emergence |
| E04 | Integration complexity — MuleSoft benchmarks, iPaaS market, MCP standard adoption |
| E05 | Security and compliance — certification costs, AI code security failure rates, IBM/Verizon threat data |
| E06 | Talent and capability gaps — METR RCT, DORA, productivity paradox, upskilling costs |
| E07 | Enterprise pilots — Rakuten, ClickUp, Harmonic, Fountain, Walmart WIBEY, S&P Global failure data |
