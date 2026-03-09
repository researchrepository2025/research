## SECTION 3: 5 Highest-Leverage Variables to Track

These are the variables whose trajectories will most materially determine which scenario — bull, base, or bear — materializes. They are drawn from the Part V analysis in the L3 position paper. Expert disagreement is sharpest here, and a single well-designed study or quarterly data point could shift scenario probabilities by 5–10 percentage points.

---

### Variable 1: Annual Maintenance Cost of AI-Built Software

**Why it matters:** This is the single highest-leverage variable in the entire build-vs-buy TCO model — more impactful on 5-year total cost of ownership than initial build cost compression. Classical enterprise software maintenance costs 15–20% of initial build cost annually. If agentic tools reduce this to 5%, the break-even calculation shifts dramatically in favor of building. If it stays at 15–20% because AI-generated code creates technical debt faster than agentic maintenance can clear it, the economics remain unfavorable for building complex enterprise software.

**Current state (2025):** No independent large-sample study of maintenance costs for AI-built enterprise software exists. The only primary source addressing this directly is a vendor-produced Duvo AI analysis in the RPA context, which is methodologically opaque. METR's RCT found experienced developers took 19% *longer* on complex mature codebases with AI tools — suggesting AI may increase maintenance complexity on legacy code, not reduce it.

**Bull signal:** Evidence that AI-generated code sustains or increases maintenance costs above 15% annually. This keeps the build-vs-buy break-even unfavorable and preserves SaaS incumbency economics.

**Bear signal:** Independent evidence (peer-reviewed or large enterprise survey) showing AI-assisted maintenance reduces effective annual cost below 8%. At this rate, the base-case economics shift toward bear-case territory — the current 43–55% SaaS share projection would become a floor, not a midpoint.

**What to watch:** Enterprise software maintenance cost data from CIO surveys (IDC, Gartner) that specifically separate AI-generated from human-generated code portfolios; public post-mortems from enterprises that built custom agentic tools in 2024–2025 documenting year-two maintenance costs; academic or independent replication of METR's RCT methodology in a maintenance (not greenfield) context. The METR RCT model applied to maintenance is the highest-value research contribution to this question.

**Sources:** [[https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]] [[https://blog.duvo.ai/why-every-rpa-project-breaks-and-how-agentic-ai-fixes-it]] [[https://xenoss.io/blog/total-cost-of-ownership-for-enterprise-ai]]

---

### Variable 2: METR Task-Horizon Trajectory

**Why it matters:** METR documents AI task-completion time doubling every 88.6 days at the accelerated rate or 196.5 days at the historical rate. At the accelerated rate, agents capable of 8-hour autonomous tasks — the enterprise workday threshold — arrive by late 2026 to early 2027. At the historical rate, they arrive by 2028–2029. This is the most consequential technical variable in the research: it determines whether the bear case timeline fits inside or outside the 5-year window.

**Current state (2025):** The doubling rate has been empirically measured at 88.6 days in METR's January 2026 update. SWE-bench Pro commercial codebase success rate stands at 9.1% — far below enterprise deployment thresholds. Yann LeCun argues LLM architectures have fundamental limitations in world understanding, persistent memory, reasoning, and planning that constrain this trajectory. Gary Marcus's mathematical reliability argument adds a complementary constraint: a 20-step agentic workflow at 95% per-step accuracy has only a 36% probability of full success, far below enterprise requirements of 99.9%+.

**Bull signal:** A verified plateau in METR task-horizon improvement over two consecutive measurement periods — doubling time extending beyond 250 days — would substantially reduce bear case probability and extend the SaaS durability window into the 2030s.

**Bear signal:** Continued doubling at the 88.6-day rate through Q3 2026, producing 8-hour-capable agents by early 2027. If Nikola Jurkovic's median "superhuman coder" arrival of 2027 materializes, bear case probability increases substantially.

**What to watch:** METR's quarterly task-horizon updates (published publicly at metr.org); SWE-bench Pro commercial codebase success rates (current baseline: 9.1%); Aider's agentic coding progress reports; performance on multi-step enterprise simulation benchmarks (GAIA, MIRAGE); whether the 88.6-day doubling rate continues, flattens, or accelerates through mid-2026.

**Sources:** [[https://metr.org/blog/2026-1-29-time-horizon-1-1/]] [[https://arxiv.org/abs/2509.16941]] [[https://www.zdnet.com/article/meta-chief-ai-scientist-llms-not-path-to-human-like-intelligence/]] [[https://ai-2027.com/research/timelines-forecast]]

---

### Variable 3: Enterprise Governance Maturity for Autonomous Agents

**Why it matters:** Governance is the organizational rate-limiter on the build scenario. Even enterprises with sufficient engineering talent cannot deploy custom-built agentic software at scale without frameworks for managing AI errors, human oversight thresholds, liability assignment, and audit trails. The base scenario requires governance maturity to grow from 21% to 45–55% by 2029. The bear scenario requires it to reach 60%+ by 2028. The bull scenario projects it staying below 35% through 2030.

**Current state (2025):** Only 21% of enterprises currently have mature governance models for autonomous agents per Deloitte (n=3,235). 42% of AI initiatives are abandoned before production per S&P Global, up from 17% in 2024. BCG finds only 5% of companies achieving AI value at scale; 60% generating no material value. The EU AI Act's progressive enforcement through 2026 and 2027 creates both governance infrastructure (compliance requirements force documentation) and governance cost (added oversight overhead). This variable currently supports the bull and base scenarios.

**Bull signal:** Deloitte governance maturity metric staying below 30% in the 2026 annual report. Continued high AI project abandonment rates (above 35%) would confirm the governance bottleneck as a durable near-term protector of SaaS procurement share.

**Bear signal:** The Deloitte governance maturity metric rising from 21% to 40%+ in the 2026 annual report would signal the governance bottleneck clearing faster than the base case projects and would increase bear case probability. A meaningful decline in S&P Global's AI project abandonment rate (below 25%) would be a corroborating signal.

**What to watch:** Deloitte State of AI annual report (n=3,235+) governance maturity percentage; Gartner agentic AI maturity model placement (currently at Peak of Inflated Expectations — movement to Slope of Enlightenment would be a bear signal); number of enterprises publicly announcing formal agentic AI governance frameworks; NIST AI Risk Management Framework adoption rates; S&P Global annual AI initiative success/abandonment tracking.

**Sources:** [[https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html]] [[https://www.spglobal.com/market-intelligence/en/news-insights/research/ai-experiences-rapid-adoption-but-with-mixed-outcomes-highlights-from-vote-ai-machine-learning]] [[https://media-publications.bcg.com/The-Widening-AI-Value-Gap-Sept-2025.pdf]] [[https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027]]

---

### Variable 4: AI-Generated Code Security Quality and FedRAMP Certification Pace

**Why it matters:** The 45% security vulnerability rate in AI-generated code is the most concrete quality barrier to enterprise custom-build deployment at scale. Enterprise security teams cannot approve production deployment of code with a 45% vulnerability rate without prohibitive remediation overhead. Simultaneously, FedRAMP certification pace for AI coding tools determines whether the compliance moat protecting regulated-sector SaaS holds or erodes. These two sub-factors interact: a tool can be FedRAMP-authorized (Windsurf achieved this in early 2026, the first major agentic coding assistant to do so) without the code it produces being enterprise-grade secure.

**Current state (2025):** Veracode finds AI-generated code introduces security vulnerabilities in 45% of cases across 100+ LLMs and 80 tasks — a finding that is unusually robust and flat across model sizes. CodeRabbit finds AI-generated pull requests contain 2.74x more XSS vulnerabilities than human-written code. Cloud Security Alliance finds 62% of AI-generated code has design flaws or known vulnerabilities. On FedRAMP: Windsurf (formerly Codeium) achieved authorization in early 2026 — the first agentic coding tool to do so — but GitHub Copilot Enterprise (the larger tool by adoption) has not. Windsurf's FedRAMP authorization resolves the development-tool access barrier for federal environments but does not address the code-quality security deficit.

**Bull signal:** The 45% Veracode vulnerability rate holds or worsens in the 2026 annual report, confirming that model scaling does not resolve the security quality problem. No major agentic coding tool (Copilot Enterprise, Cursor, Claude Code) achieves FedRAMP authorization by end of 2027.

**Bear signal:** A 2026 Veracode update showing vulnerability rates falling below 25% across top models would signal meaningful quality improvement and shift probability toward the base or bear scenario. GitHub Copilot Enterprise or Claude Code achieving FedRAMP authorization would constitute a higher-magnitude trigger than Windsurf's authorization and would warrant a 5–7 percentage point bear-case revision. Additionally, if SaaS platform AI features (Salesforce Agentforce, ServiceNow Now Assist) fail to obtain FedRAMP ATO coverage within 18 months, the temporary certification-lag window tips federal procurement toward custom builds.

**What to watch:** Veracode annual AI code security report (primary indicator — the 45% figure is the binding constraint on enterprise deployment approval); FedRAMP marketplace AI/agentic tool listings (Windsurf now listed; track whether GitHub Copilot Enterprise, Cursor, or Claude Code follow within 2026–2027); SaaS platform vendor announcements of FedRAMP ATO expansions covering AI features (Agentforce, Now Assist, M365 Copilot in GCC) — this is the event that closes the certification-lag window; enterprise CISO survey data on AI code deployment approval rates.

**Sources:** [[https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/]] [[https://www.fedramp.gov/ai/]] [[https://www.workstreet.com/blog/fedramp-certification-cost]] [[https://beancount.io/blog/2026/02/02/vertical-saas-survival-guide-competing-against-ai-giants]]

---

### Variable 5: SaaS Incumbent Pricing Discipline

**Why it matters:** SaaS pricing behavior is the primary commercial driver of build mandates — the mechanism by which vendor pricing decisions convert enterprise CFO frustration into actual custom-build procurement. SaaS inflation at 12.2% annually (4.5x general CPI) means a $55.7M average enterprise SaaS spend grows to $73M over three years without a single additional procurement decision. Salesforce's pattern of extracting 72% of its 2025 ARR growth from price increases rather than new customers directly motivates the build alternative for large captive customers. The EU Data Act's ban on exit fees effective January 2027 will reduce vendor lock-in for European enterprises, lowering the switching cost floor that has historically protected SaaS market share.

**Current state (2025):** Price extraction is continuing at high rates with limited enterprise resistance in aggregate spend data. 60% of vendors are masking price increases through AI feature bundling, and 28% of contracts experienced "shrinkflation." Zylo's finding that 52.7% of SaaS licenses go unused ($21M wasted annually per organization) signals growing procurement attention even without organized resistance. The per-seat pricing model is collapsing across all nine research waves — IDC's 70% vendor refactoring projection is well-corroborated — but pricing model disruption and SaaS category displacement remain analytically distinct.

**Bull signal:** SaaS inflation decelerating to below 8% annually, driven by vendor competition from AI-native alternatives or organized enterprise procurement resistance. This reduces build incentive and supports the bull case for SaaS share retention. Successful SaaS vendor transitions to consumption and outcome-based pricing that deliver CFO-visible value rather than extracting captive-customer rent.

**Bear signal:** SaaS inflation accelerating above 15%, or multiple high-profile price disputes becoming public litigation. The EU Data Act exit-fee ban triggering a measurable switching wave in European enterprise portfolios in 2027 would be a concrete leading indicator of the base-to-bear transition. Any quarter in which Salesforce's NRR drops below 100% in reported earnings would be hard financial confirmation of the pricing-extraction threshold being crossed.

**What to watch:** Vertice quarterly SaaS Inflation Index (current: 12.2% annually — track direction); SaaStr and vendor investor relations announcements for price increase cadence (Salesforce, Microsoft, Google, Atlassian all raised prices in 2025); Zylo annual SaaS Management Index for average enterprise app count and unused license rates; EU Data Act Article 23 exit-fee ban enforcement actions starting January 2027; Salesforce and ServiceNow quarterly NRR in earnings — first drop below 100% would be a significant base-to-bear trigger; CFO survey data on SaaS cost management priorities (Gartner, IDC annual surveys).

**Sources:** [[https://www.vertice.one/l/saas-inflation-index-report]] [[https://www.saastr.com/salesforce-microsoft-google-and-atlassian-all-raise-prices-again-in-2025-hooray/]] [[https://zylo.com/news/2025-saas-management-index/]] [[https://www.vertice.one/insights/saas-inflation-rate]] [[https://www.idc.com/resource-center/blog/is-saas-dead-rethinking-the-future-of-software-in-the-age-of-ai/]]

---

*Variables drawn from L3 Position Paper, Part V ("The Five Highest-Leverage Variables"), cross-referenced with L2 Scenario Architecture scenario conditions and L2 Consensus Divergence contested findings. All probability estimates carry ±8–10 percentage point confidence intervals. Recommended tracking cadence: quarterly through 2027, full reassessment at 2030 horizon.*
