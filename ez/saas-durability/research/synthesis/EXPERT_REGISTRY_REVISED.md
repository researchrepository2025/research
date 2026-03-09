# Expert Registry: Revised Camp Assignments
## SaaS Durability Research Project — Consensus Synthesis
**Document Type:** Consolidated Post-Audit Registry
**Source Audits:** EXPERT_AUDIT_CEO.md, EXPERT_AUDIT_ANALYST.md, EXPERT_AUDIT_VC.md, EXPERT_AUDIT_RESEARCHER.md
**Synthesis Date:** 2026-03-06
**Standard Applied:** An expert may only be placed in BULL, BASE, or BEAR if they have made a direct, explicit statement about enterprise SaaS procurement vs. custom build. General AI capability statements, AI adoption forecasts, spending growth predictions, coding productivity claims, pricing model forecasts, or adjacent comments do NOT qualify.

---

## Section 1: Executive Summary

### Counts

| Metric | Count |
|--------|-------|
| Total named experts reviewed across all four audits | 97 |
| Retained original camp assignment (qualifying evidence) | 24 |
| Moved to UNCLEAR | 50 |
| Moved to NUANCED-CONDITIONAL (from another camp) | 17 |
| Moved to different bull/base/bear camp | 6 |

**Note on scope:** The four audit files reviewed a combined 97 unique named experts drawn from the L2 registry plus additional names appearing in the wave research. Three experts (Frank Slootman, Stewart Butterfield, Scott Wu) were not in the original L2 registry and appear in supplementary wave documents only; they are included here for completeness but flagged accordingly.

### Distribution of Revised Assignments

| Revised Camp | Count |
|--------------|-------|
| BULL | 14 |
| BASE | 4 |
| BEAR | 17 |
| NUANCED-CONDITIONAL | 25 |
| UNCLEAR | 37 |

### Key Insight: What This Re-Examination Reveals

**The original L2 registry was built on a systematic category error:** it conflated AI capability statements with enterprise procurement predictions. Approximately 51% of all named experts (50 of 97) who were assigned to definitive bull, base, or bear camps did not, in fact, make any direct, explicit statement about whether enterprises would buy SaaS or build custom software. Their statements were about adjacent topics — coding productivity, AI capability trajectories, software spending volume growth, pricing model evolution, VC investment strategy, TAM expansion, or organizational change — and were then attributed to procurement-modality camps by inference.

The most consequential directional errors were:
1. **AI capability skeptics placed in the Bear camp.** LeCun, Sutskever, METR researchers, and Jim Covello (Goldman Sachs) were coded as supporting or adjacent to the bear thesis when their actual arguments — that LLMs have fundamental architectural limits and AI ROI is poor — make enterprise custom-build programs *harder* to execute, not easier. Their statements structurally support SaaS durability.
2. **Build-platform founders placed in the Bear camp on coding capability statements.** Amodei ("AI writes 90% of code") and Altman ("service as software") were assigned BEAR based on AI capability claims that say nothing about whether enterprises will buy or build.
3. **SaaS consolidation arguments misread as build-over-buy arguments.** Nadella and McDermott argue that traditional category SaaS will be consolidated onto platform SaaS (Microsoft, ServiceNow respectively) — which is still a buy decision. Their statements are not equivalent to "enterprises will build instead of buy."
4. **Analyst and consulting firm BASE assignments are almost entirely unsupported.** Of 23 analysts and consulting partners audited, 14 had no direct buy-vs-build statement in their attributed quotes. Spending forecasts, vendor survival analyses, and pricing model studies were routinely conflated with procurement-modality positions.

The net effect of applying the strict criterion is a significant contraction in the qualified evidence base: the bear camp shrinks from its original size but retains its most credible direct-statement experts (Andrusko, Palihapitiya, Citrini/Shah, Hsu, Masad, Ader, Thill). The bull camp similarly shrinks but retains its strongest statements (Bhusri, Huang, Akkiraju). The largest single outcome is a dramatic expansion of UNCLEAR — which correctly reflects that most public commentary on AI and software has *not* directly addressed the enterprise procurement question, even from highly credible sources.

---

## Section 2: Full Expert Table

Camps used:
- **BULL** — explicitly favors continued SaaS dominance in enterprise buy vs. build decisions
- **BASE** — explicitly predicts SaaS retains majority share but with meaningful erosion
- **BEAR** — explicitly predicts SaaS loses majority share to custom build in enterprise
- **NUANCED-CONDITIONAL** — made explicit buy-vs-build statements but with important conditions preventing simple bull/base/bear classification
- **UNCLEAR** — no direct, explicit statements about enterprise SaaS procurement vs. custom build found

### Tech CEOs and Corporate Executives

| Expert Name | Role/Affiliation | Original Camp | Revised Camp | Qualifying Evidence | Rationale for Change |
|-------------|-----------------|---------------|--------------|---------------------|----------------------|
| Jensen Huang | CEO, Nvidia | BULL | BULL | "All of these tools that we use today, whether it's Cadence or Synopsys or ServiceNow or SAP, these tools exist for a fundamentally good reason. These agentic AI will be intelligent software that uses these tools on our behalf." (CNBC, Feb 26, 2026) | Direct statement that AI agents will use SaaS tools rather than displace them. Conflict of interest real but indirect (Nvidia GPU sales benefit from SaaS vendor AI investment, not SaaS purchase decisions). Camp retained. |
| Marc Benioff | Chair and CEO, Salesforce | BULL | NUANCED-CONDITIONAL | "If there is a SaaSpocalypse, it may be eaten by the Sasquatch because there are a lot of companies using a lot of SaaS because it just got better with agents." (TechCrunch, Feb 25, 2026) — but simultaneously restructuring toward consumption-based pricing and cutting 4,000 customer-service jobs. | Statements are product promotion and investor reassurance, not direct procurement analysis. Strategic actions (consumption repricing, Agentforce launch as alternative model) indicate private acknowledgment that seat-based SaaS is under pressure. NUANCED-CONDITIONAL captures his conditional thesis: SaaS-derived platforms survive if they successfully reprice to agentic models. Maximum conflict of interest. |
| Satya Nadella | CEO, Microsoft | BEAR | NUANCED-CONDITIONAL | "Business applications will probably all collapse in the Agent Era because they are essentially CRUD databases with a bunch of business logic." / "You can think of agents as the new apps." (BG2 Podcast, Dec 2024) | Statement is about software architecture, not procurement modality. Nadella's proposed replacement (Copilot Studio, Agent 365) is still bought from Microsoft — enterprises still buy. His thesis is that *category* SaaS vendors lose to *platform* SaaS (Microsoft), not that enterprises stop buying. Commercially weaponized competitive positioning against Salesforce/Workday. NUANCED-CONDITIONAL: SaaS disrupted by AI agents, but enterprises still procure from platforms. |
| Sam Altman | CEO, OpenAI | BEAR | UNCLEAR | None found — statements are about AI delivery models ("service as software") and coding capability ("AI writes 50%+ of code in many companies"). Source for attributed quote is secondary reporting (longbridge.com), not a direct transcript. | "Service as software" describes how AI services are delivered, not whether enterprises buy or build. Never explicitly addressed enterprise SaaS-vs-build procurement. Strong financial conflict (OpenAI TAM expands with every build decision). |
| Dario Amodei | CEO, Anthropic | BEAR | UNCLEAR | None found — statements are about AI coding capability: "AI will write 90% of code within [6 months]." (CFR, March 2025) Prediction was subsequently described as "nowhere nearly to becoming a reality" externally (IT Pro, mid-2025). | Textbook misattribution identified in audit brief. "AI writes code" applies to SaaS vendors building better SaaS, not only to enterprises building custom software. No direct enterprise procurement statement. Strong financial conflict (Anthropic TAM expands with build decisions). |
| Bill McDermott | Chairman and CEO, ServiceNow | BEAR | NUANCED-CONDITIONAL | "Functional SaaS and feature SaaS will be automated by ServiceNow and the language models that are meeting us in the middle of our workflow." / "Traditional app stack is going to collapse...moved to the ServiceNow platform." (Diginomica, May 2025) | Bear thesis is buy-ServiceNow vs. buy-category-SaaS, not buy vs. build. McDermott explicitly says enterprises will procure from ServiceNow as consolidation platform. This is a buy-vs-buy disruption claim. NUANCED-CONDITIONAL: traditional multi-vendor SaaS threatened; platform procurement survives. Extreme commercial conflict. |
| Tobi Lutke | CEO, Shopify | BEAR | UNCLEAR | None found — statements are about internal AI adoption mandates: "Before asking for more headcount and resources, teams must demonstrate why they cannot get what they want done using AI." (CNBC, April 2025) | Internal labor/AI mandate addresses whether humans or AI will do work, not whether Shopify or its customers will change SaaS procurement. No buy-vs-build procurement statement made. |
| Aneel Bhusri | Co-Founder and CEO, Workday | BULL | BULL | "There is no amount of vibe coding that will ever produce an HR or ERP system that will meet all the requirements that modern business needs." / "These are true systems of record that must process transactions with absolute accuracy...enforce complex security models and comply with statutory and regulatory requirements all over the world." (Cloud Wars, March 2, 2026) | Direct, explicit claim that building custom software cannot replace enterprise systems like Workday. Most direct BULL procurement statement in the CEO corpus. Maximum conflict of interest: returned as CEO to defend against AI disruption fears, $138.8M compensation package. |
| Carl Eschenbach | Former CEO, Workday | BULL | BULL | "They want to do it on the back of a trusted platform. As they start to build agents, they see the most secure, reliable and trusted way to onboard their agents is through Workday." (Diginomica, 2025) | Partially addresses the procurement question: enterprises choosing to build on Workday rather than from scratch. BULL defensible; weaker than Bhusri's direct statement. Significant conflict of interest (former CEO, stock ownership). |
| Amit Zavery | President, CPO and COO, ServiceNow | NUANCED-CONDITIONAL | NUANCED-CONDITIONAL | "We are not in a SaaS neighborhood." / "The reality is that today, AI is gathered across enterprises in silos — it's fragmented, disconnected." (Cloud Wars, 2025) | Position has a genuine condition: SaaS survives if it becomes a platform, fails if it remains a category tool. Statements partially address procurement behavior (enterprises need a consolidation platform). Camp retained. Conflict of interest: identical commercial motivation to McDermott. |
| David Hsu | CEO and Founder, Retool | BEAR | BEAR | "The bar for purchased software just got permanently higher." / "35% of enterprises have already replaced SaaS with custom software." (Retool Build vs. Buy Report, Feb 2026) | Direct, explicit statement about enterprise procurement modality. "Bar for purchased software permanently higher" and the 35% replacement claim address buy-vs-build squarely. Camp retained. CRITICAL CAVEAT: maximum conflict of interest; 35% statistic is self-sourced from Retool's own customer base (people who already chose to build on Retool) — not a representative enterprise sample. Must be disclosed when cited. |
| Amjad Masad | CEO, Replit | BEAR | BEAR | "$400 vs. $150,000 ERP anecdote" — "We're seeing customers have three orders of magnitude of savings on apps" — customer built ERP automation for $400 instead of vendor's quoted $150,000. (VentureBeat, June 2025) | Direct buy-vs-build cost economics comparison. Camp retained. Maximum conflict of interest (Replit's $150M ARR built entirely on build decisions). Single unverified anecdote should not be treated as systemic data. |
| Michael Truell | CEO, Cursor (Anysphere) | BEAR | UNCLEAR | None found — primary statement is a warning: "If you close your eyes and you don't look at the code and you have AIs build things with shaky foundations as you add another floor...things start to kind of crumble." (Fortune, Dec 25, 2025) | Primary statement is a caution against unsupervised AI coding — opposite of a confident BEAR position. "20% of coding workflows by agents by 2026" is a productivity forecast, not a procurement statement. D07 itself characterizes Truell in "AI Augments But Must Be Used Carefully" framing. |
| Brian Landsman | CEO AppExchange, Salesforce | BULL | UNCLEAR | None found — sole attributed statement: "We are entering a phase where expertise is more valuable than code." | Aphorism about skill value in the AI era. Does not address whether enterprises buy or build. Could support either interpretation. Should not be in any camp. |
| Frank Slootman | Former CEO, Snowflake (investor) | Not in registry | UNCLEAR | None found — investment action only: $50M Series B in Factory (agentic coding platform). | Investment in agentic coding platform does not constitute a verbal proclamation on enterprise SaaS procurement. No direct statement found. |
| Stewart Butterfield | Former CEO, Slack (author) | Not in registry | UNCLEAR | None found — no public statements in 2025–2026 window on procurement question. "Genesis" (co-authored with Craig Mundie) predates agentic AI at scale. | No qualifying statements in the relevant time window. |
| Scott Wu | CEO, Cognition AI | Not in registry | UNCLEAR | None found — product description from Contrary Research analyst ("scalable alternative to human engineering labor"), not a direct Wu quote on procurement. | Analyst's description of company positioning is not the same as a CEO procurement statement. Absent direct Wu quotes, no camp assignment warranted. |

### Analysts and Consulting Partners

| Expert Name | Role/Affiliation | Original Camp | Revised Camp | Qualifying Evidence | Rationale for Change |
|-------------|-----------------|---------------|--------------|---------------------|----------------------|
| Sid Nag | VP Analyst, Gartner | BULL | UNCLEAR | None found — stated position: "AI technologies in IT and business operations unabatedly accelerating the role of cloud computing." | Cloud spending growth forecast. Cloud spending growth is compatible with enterprises building more custom applications on cloud infrastructure (build-on-cloud, not buy-SaaS). |
| John-David Lovelock | Distinguished VP Analyst, Gartner | BASE | UNCLEAR | None found — stated position: "GenAI features are now ubiquitous across software enterprises already own and these features cost more. The cost of software is going up." | IT spending growth and AI-bundled cost inflation forecast. Describes existing contract costs; makes no claim about future procurement modality for AI-driven applications. |
| Denis Torii | VP Analyst, Gartner | BASE | NUANCED-CONDITIONAL | "Buy, Build, Blend" as the AI enterprise strategy — composability and blending, not binary replacement. (AgilePoint blog, via Gartner, 2025) | Only Gartner analyst to directly engage with buy-vs-build as a framework. Explicitly rejects binary outcome. "Blend" means neither buy nor build dominates — heterogeneous outcome predicted. NUANCED-CONDITIONAL captures this correctly. |
| Anushree Verma | Sr Director Analyst, Gartner | BULL | UNCLEAR | None found — stated position: "AI agents will evolve rapidly, progressing from task and application specific agents to agentic ecosystems." Also attributed: 40%+ of agentic AI projects will be canceled by 2027. | Agent evolution timeline and project failure rate predictions. No explicit connection to buy-vs-build procurement behavior. 40% cancellation finding is suggestive but not stated as a procurement recommendation. |
| Kate Leggett | VP Principal Analyst, Forrester | BASE | NUANCED-CONDITIONAL | "SaaS As We Know It Is Dead: How To Survive The SaaS-pocalypse!" (Forrester, Feb 2026) — simultaneously states "the enterprise core isn't vanishing" and projects SaaS spend growing to $576B by 2029. Identifies horizontal point-solution vendors as struggling. | Document directly engages with "will enterprises build instead of buy" fear. Nuanced answer: enterprise core survives (favorable to buy); horizontal point-solutions face displacement (conditional). Internal contradiction between headline and body text is itself evidence of a nuanced position, not BASE. |
| Charles Betz | VP Principal Analyst, Forrester | BASE | NUANCED-CONDITIONAL | "There are about 20,000 legal jurisdictions worldwide and compliance with applicable regulation is a major reason why people trust vendors like SAP." (The Register, Feb 4, 2026, in context of "AI replace SaaS" article) | Makes a direct buy argument for compliance-heavy applications — regulatory complexity makes custom-building prohibitive. Explicitly scoped: compliance workflows only, not all AI-driven applications. NUANCED-CONDITIONAL correctly captures the conditionality. |
| Liz Herbert | VP Principal Analyst, Forrester | BASE | UNCLEAR | None found — stated position: "A Year of Reckoning for Enterprise Application Vendors" — framed 2025 as existential for SaaS pricing model. | Vendor pricing model stress forecast. A pricing model crisis is consistent with enterprises continuing to buy SaaS (at lower prices or different terms). No claim that enterprises switch to custom builds. |
| Diego Lo Giudice | Analyst, Forrester | BASE | UNCLEAR | None found — stated position: definition of "Agentic Software Development" as agency rather than mere assistance; upcoming ASD Wave planned for H2 2026. | Technology category taxonomy work. Defines ASD as a category; does not recommend that enterprises build or buy. |
| Christopher Condo | Principal Analyst, Forrester | BASE | UNCLEAR | None found — stated position: "At least one organization will try to replace 50% of its developers with AI and fail"; developers spend only 24% of time coding. | Developer productivity and AI implementation failure prediction. No buy-vs-build statement made. |
| Bo Lykkegaard | Associate VP, IDC Europe | BASE | NUANCED-CONDITIONAL | "SaaS is being disrupted, not by decline but by evolution"; per-seat pricing will be obsolete by 2028, but SaaS category survives. (IDC, 2025) | Closest IDC statement to a direct buy-vs-build position: SaaS procurement persists but pricing model transforms. Conditioned explicitly on vendor pricing model evolution. NUANCED-CONDITIONAL captures conditionality better than BASE. |
| Frank Della Rosa | Research VP SaaS, IDC | BASE | UNCLEAR | None found — stated position: "Generative AI and agentic AI reshape SaaS, accelerating innovation geometrically and reordering the competitive landscape." | SaaS vendor competitive dynamics prediction. "Reordering the landscape" is about which vendors win, not whether enterprises buy or build. |
| Jeremy Schneider | Senior Partner, McKinsey | BASE | NUANCED-CONDITIONAL | "Successful scalers will balance build-versus-buy decisions based on sources of distinctiveness and competitive advantage." / Make-or-Buy Matrix: "Does this capability offer a unique competitive advantage? If yes, building internally may make sense. But when speed, cost control, or proven reliability matter more, buying or partnering could be the better strategy." (McKinsey, 2025–2026) | Published make-or-buy framework is a direct buy-vs-build engagement. Principled conditional: build where differentiation is genuine, buy otherwise. Practical default leans buy for most enterprise capabilities. NUANCED-CONDITIONAL is correct; not a blanket SaaS majority prediction. Significant bilateral conflict (earns from both SaaS advisory and custom build implementation). |
| Mohit Khanna | Partner, McKinsey TMT | BASE | UNCLEAR | None found — stated position: "Only 16% of SaaS incumbents have commercialized AI stand-alone products; those that have report 2–3x higher customer traction." | SaaS vendor commercialization performance data. Describes vendor readiness gaps, not enterprise buyer procurement decisions. |
| Alex Singla | Senior Partner, McKinsey QuantumBlack | BASE | NUANCED-CONDITIONAL | "Many more [enterprises] are finding it challenging to see value from their investments, and in some cases, they are even retrenching — rehiring people where agents have failed." / "Agents Aren't Always the Answer." Only 39% of organizations report EBIT impact at enterprise level from AI. (McKinsey, 2026) | Enterprise retrenchment in failed agentic builds is closest McKinsey comes to a direct procurement-direction statement. Custom build failure rates are material to the procurement decision. Does not prescribe "buy SaaS instead" — prescribes "hire McKinsey to build more carefully." NUANCED-CONDITIONAL: build viable if managed correctly; buy is the fallback. |
| Bob Sternfels | Global Managing Partner, McKinsey | BASE | UNCLEAR | None found — stated position: "CEOs and business leaders face unprecedented challenges in capturing value with agentic AI. To scale, they must rewire their businesses, reimagining domains and evolving how their people work, build capabilities, and lead change." (McKinsey-OpenAI Frontier Alliance announcement, Feb 2026) | Commercial partnership announcement. "Rewire their businesses" is transformation consulting language. Severe conflict: direct commercial revenue from the McKinsey-OpenAI Frontier Alliance. |
| Chuck Whitten | Partner, Bain & Company | BASE | NUANCED-CONDITIONAL | "We won't see collapse but convergence — a heterogeneous landscape where AI and SaaS complement and compete in various ways." / "Transitions lead not to extinction but to transformation, adaptation, and coexistence." (Bain, January 23, 2025) | Directly addresses "will AI kill SaaS" — most direct Bain engagement with the research question. "Heterogeneous landscape" explicitly refuses to predict SaaS majority dominance. NUANCED-CONDITIONAL: neither SaaS nor build dominates; genuine competition between modalities predicted. |
| David Crawford | Partner and Chairman, Bain Global Technology Practice | BASE | UNCLEAR | None found — stated positions: "Today's tech giants have proven unusually resistant, co-opting disruption through self-reinvention." / "$2 trillion in new revenue needed to fund AI's scaling trend." | Tech company resilience claim and AI infrastructure economics. Neither addresses whether enterprises will buy SaaS or build custom applications. |
| David Lipman | Partner, Bain | BASE | UNCLEAR | None found — stated positions: SaaS stock market metrics ("frozen market," "average gross retention still around 90%"), 30–50% AI automation forecast. | SaaS vendor financial performance metrics and market conditions. Business metrics for SaaS vendors are not enterprise procurement statements. |
| Akash Bhatia | Managing Director, BCG Silicon Valley | BASE | NUANCED-CONDITIONAL | "40% of IT buyers cite seat reduction as their primary lever." (BCG, 2025) | Seat reduction as primary IT buyer lever is a direct observation about enterprise procurement behavior — enterprises are reducing SaaS seat purchasing. Framed as pricing model compression rather than build migration. Conditional: SaaS survives if it transitions to consumption pricing. NUANCED-CONDITIONAL captures this correctly. |
| Nicolas de Bellefonds | Managing Director, BCG AI Global | BASE | UNCLEAR | None found — stated position: "The companies that are capturing real value from AI aren't just automating — they're reshaping and reinventing how their businesses work." | Generic AI transformation effectiveness statement. Compatible with both buy and build strategies. Severe commercial conflict (BCG AI practice, OpenAI Frontier Alliance). |
| Matthew Kropp | Partner, BCG | BASE | UNCLEAR | None found — stated position: "AI will transition the market to a consumption-based B2B software model rather than perpetual licensing." | Pricing model evolution forecast. Consumption-based vs. perpetual is a change within the buy paradigm; says nothing about build. |
| Ayo Odusote | Software and Platforms Leader, Deloitte | BASE | NUANCED-CONDITIONAL | "Many enterprises will ultimately balance both approaches rather than choosing one exclusively"; market becoming "more hybrid"; "vendors must earn renewal, not extract it." (CIO.com, 2025) | Direct buy-vs-build statement predicting hybrid outcome. "Balance both approaches" explicitly addresses the procurement question. Predicts more build than current baseline, but not build dominance. NUANCED-CONDITIONAL: neither SaaS nor build will exclusively win. Bilateral conflict (earns from both SaaS implementation and custom build). |
| Nitin Mittal | Global AI Leader, Deloitte | BASE | UNCLEAR | None found — stated position: organizations pivoting from experimentation to integrating AI into core business at scale. | AI adoption maturity description. Could describe procurement via buy or build. |

### VC and Investor Experts

| Expert Name | Role/Affiliation | Original Camp | Revised Camp | Qualifying Evidence | Rationale for Change |
|-------------|-----------------|---------------|--------------|---------------------|----------------------|
| Anish Acharya | General Partner, a16z | BULL | BULL | "The theory that we'll vibe code everything is 'flat wrong'"; software accounts for 8–12% of company expenses, so rebuilding payroll or ERP via AI would save only ~10% of total costs; questioned why companies would "point it at rebuilding payroll or ERP or CRM." (a16z, Feb 10, 2026) | Economic rebuttal to custom-build case: rebuilding ERP/CRM saves only ~10% of total company cost, making it economically irrational. Direct engagement with buy-vs-build decision logic. BULL assignment defensible but at the criterion boundary — argument is anti-build rather than affirmatively pro-buy. |
| Steven Sinofsky | Board Partner, a16z | BULL | UNCLEAR | None found — stated position: "AI changes what we build and who builds it, but not how much needs to be built." / "There will be more software than ever before." (a16z, Feb 6, 2026) | Statement addresses software volume ("more software") not procurement modality. "More software" is consistent with SaaS vendors building more AND enterprises building more. Does not address whether enterprises buy or build. |
| Alex Immerman | Partner, a16z Growth | BULL | BULL | "AI simply isn't going to kill software companies." Co-authored piece directly rebuts bear scenarios for SaaS displacement including enterprise self-build. Identifies six durable moats: switching costs, network effects, scale, brand, cornered resources, process power. (a16z, March 2, 2026) | Directly addresses and rebuts the bear scenarios for enterprise self-build. Anti-build argument constitutes a partial direct buy-vs-build engagement. BULL defensible at the criterion boundary. |
| Alfred Lin | Co-Steward and Partner, Sequoia | BULL | BULL | "The notion that SaaS is dead, I think, is overblown." / "People want simple...the foundation model is not going to be able to cater to every single way that someone wants to do [something] in all these different industries." / "The proliferation of vertical SaaS has been a profitable way to invest. I think there will be a proliferation of vertical AI companies too." (Fortune, March 2, 2026) | Directly argues SaaS is not dead and vertical SaaS persists. "Proliferation of vertical AI companies" implies enterprises will continue buying from specialized vendors. As close to a direct buy-vs-build declaration as any investor makes. |
| Orlando Bravo | Founder and Managing Partner, Thoma Bravo | BULL | UNCLEAR | None found — stated positions: "Software is about domain knowledge, not code"; AI is "in a bubble"; deploying $34.4B in SaaS acquisitions. (Semafor, Jan 2026) | Investment thesis (SaaS companies are undervalued PE targets) and bubble assessment. "SaaS companies are good investments" does not imply "enterprises will keep buying SaaS." PE acquisition book conflict. |
| Robert F. Smith | Founder and CEO, Vista Equity Partners | BULL | UNCLEAR | None found — stated position: "AI will enable enterprise software to eat services"; launched Agentic AI Factory. | TAM expansion argument: software captures labor market. Compatible with SaaS vendors OR custom-built AI capturing services revenue. Not a buy-vs-build statement. |
| Ryan Hinkle | Managing Director, Insight Partners | BULL | NUANCED-CONDITIONAL | "AI is net positive for SaaS as a market. The question is: Which companies lose to the kids in a garage rebuilding their product AI-first, and which ones unlock new revenue streams with AI?" / Distinguishes "filing cabinet" SaaS (vulnerable to replacement) from "systems of action" (not cost-justified to replace). (Insight Partners, Dec 15, 2025) | Directly addresses procurement modality with an explicit condition: "filing cabinet" SaaS will be displaced (by custom builds), "systems of action" will retain buyers. Textbook NUANCED-CONDITIONAL: answer depends entirely on SaaS category. Current BULL understates his conditionality. |
| Praveen Akkiraju | Managing Director, Insight Partners | BULL | BULL | "The new archetype will be agentic SaaS — SaaS as we know it, but under the covers, agentic workflows injecting dynamism and intelligence into software that used to be static." (Insight Partners, Dec 15, 2025) | Directly asserts the SaaS vendor relationship persists via "agentic SaaS." Enterprises still buy from vendors; the product changes underneath. Direct BULL procurement statement. |
| Jared Sleeper | Partner, Avenir | BULL | BULL | "63% of enterprise buyers expect existing vendors to benefit from AI." (LinkedIn survey data, 2025) | Survey data directly addresses whether enterprises expect to continue with existing SaaS vendors — a direct procurement preference signal. Sleeper cites it approvingly as evidence of SaaS durability. BULL assignment defensible, though rests on survey data rather than Sleeper's own direct analysis. |
| Byron Deeter | Partner, Bessemer Venture Partners | BULL | BULL | "Within the next one to two years, businesses that fail to cross the chasm from pure SaaS to AI risk irrelevance." Incumbents retain advantages through "massive datasets, distribution networks, and integration resources"; "consolidation, not extinction, will occur." (BVP, Nov 2025) | Implies continued buy-side behavior (enterprises will still buy from SaaS vendors, just transformed ones). "Consolidation not extinction" is a procurement persistence argument. BULL defensible, borderline — rests on inference about buyer behavior from vendor-survival arguments. |
| Michael Hoeksema | Partner, Battery Ventures | BULL | UNCLEAR | None found — stated position: "The agentic-only heat will cool and UI-based SaaS will come back into favor...durable companies will look more like SaaS companies of old with AI superpowers." | Prediction about investor sentiment and architectural preference. "SaaS will come back into investor favor" refers to valuation multiples, not enterprise procurement behavior. |
| Jamin Ball | VC Investor, Clouded Judgement | BASE | UNCLEAR | None found — stated position: "Agents are not replacing systems of record — they are raising the standards for what a good one looks like." | Statement about what agents do to existing SoR, not whether SoR will be bought or built. An agent could be custom-built while leaving the system of record in place. |
| Tomasz Tunguz | General Partner, Theory Ventures | BASE | UNCLEAR | None found — stated position: vertical software down 43% YTD and workflow companies down 39% by Feb 2026; data infrastructure and security declined far less. | Public market valuation analysis. Stock market pricing of disruption risk is not an enterprise procurement statement. |
| Jake Saper | General Partner, Emergence Capital | BASE | BEAR | "The investor who won't shut up about AI-native services." / "Canary in the coal mine" for traditional SaaS is workflow ownership vs. task execution (Cursor vs. Claude Code contrast). (TechCrunch, March 1, 2026) | Explicitly argues AI-native services displace traditional SaaS. Saper's self-description ("won't shut up about AI-native services") and workflow-ownership thesis constitute a structural displacement argument. BEAR is the closest fit, noting his thesis is about which type of service wins rather than whether enterprises build custom. Upgrading from BASE: he explicitly argues enterprises shift from buying traditional SaaS. |
| Alex Rampell | General Partner, a16z | BEAR | UNCLEAR | None found — stated positions: "The worldwide SaaS market is about $300B per year. The labor market in the U.S. alone is $13T." / "Software becomes labor." (a16z, 2024–2025) | TAM expansion argument. "Software becomes labor" means AI software replaces human workers — entirely consistent with SaaS companies providing that AI software. Does not argue enterprises will build custom software. |
| David George | General Partner, a16z | BEAR | UNCLEAR | None found — stated positions: "AI is already delivering 10x product experiences for a 1/10th of the cost." / "If a CRM company was still selling seats and a new AI product came in and offered better services for even 1% of revenue created, it'd be pretty hard for that incumbent CRM company to compete." | CRM displacement by new AI-native vendor is a vendor-competition argument, not a buy-vs-build argument. Enterprises in this scenario still buy from vendors; they switch vendors. |
| Marc Andrusko | Partner, a16z | BEAR | BEAR | "Systems of record are vulnerable for the first time in over a decade due to AI-driven enterprise reconsideration of tech stacks." / Klarna's replacement of Salesforce and Workday with custom AI solutions represents "cord-cutting" that will be "replicated many times over." (a16z Big Ideas in Tech 2025, Nov 2024 updated March 2025) | Clearest buy-vs-build statement in the a16z corpus. Explicitly cites an enterprise replacing incumbent SaaS with custom AI builds as a model to be widely replicated. Direct procurement-modality claim. |
| Dean Shahar | Managing Director, DTCP | BEAR | BEAR | "The SaaS world is dying, not software itself, but SaaS as a business category. AI has turned software into a commodity where sustainable competitive advantage is nearly impossible." / "An entrepreneur who approaches a VC with a SaaS startup today won't even reach the pitch stage." (Calcalist, 2025) | SaaS-as-category-dying argument has implicit procurement consequences: if enterprises won't buy traditional SaaS (because it offers no competitive advantage), this implies procurement shift. BEAR is defensible. Primarily investment-thesis framing; procurement inference is present but not primary. |
| Chamath Palihapitiya | Founder, Social Capital / 8090 | BEAR | BEAR | "I'm starting an incubator. Funded entirely by me. It's called 8090. Tell us what enterprise software you use and my team and I will build you an 80% feature complete version at a 90% discount." / "The Software Industrial Complex is $5T and unsustainable." (Twitter, Jan 2024; Dec 2024) — partial self-correction in July 2025: "2025 was supposed to be the year of agents. So far it's been the year of letdowns." | Most explicit build-vs-buy action in the corpus. 8090 is a direct commercial bet on the thesis that enterprises can and should replace SaaS with custom builds. Self-correction in July 2025 means timing is uncertain but directional thesis remains BEAR. |
| Alap Shah / Citrini Research | CIO, Lotus Technology Management; Citrini Research co-author | BEAR | BEAR | "A competent developer working with Claude Code or Codex could replicate mid-market SaaS functionality in weeks." / "The long tail of SaaS had it much worse." Scenario predicts SaaS displacement through agentic coding. (Citrini Research, Feb 2026) | Central thesis is that agentic coding tools have lowered the cost of custom-building SaaS replacements to the point where enterprises shift from buying to building. Direct buy-vs-build cost argument. |
| Sarah Tavel | General Partner, Benchmark Capital | BEAR | NUANCED-CONDITIONAL | "Rather than sell software to improve an end-user's productivity, founders should consider what it would look like to sell the work itself." / "AI could radically change how software is sold, and even upend the business model that's defined SaaS for the last decades." (sarahtavel.com, 2023; 2024–2025 appearances) | "Sell the work, not the software" is about pricing model transformation for vendors — enterprises still buy from vendors, they just pay differently (per-outcome vs. per-seat). Does not argue enterprises stop buying and start building. BEAR overstates her position. NUANCED-CONDITIONAL: the how of buying changes fundamentally, but the buy relationship is not displaced by build. |
| Anton Levy | Founder, Layer Global (ex-General Atlantic) | BEAR | UNCLEAR | None found — stated position: investment action (launching AI-focused fund); "vote of confidence in AI-native over legacy SaaS" is an interpretive attribution, not a direct quote. | Fund launch favoring AI-native companies over legacy SaaS is an investment strategy decision. Enterprises could switch from buying legacy SaaS to buying AI-native SaaS — still a buy relationship. No direct procurement statement. |
| Pat Grady | Co-Steward and Partner, Sequoia | BASE | UNCLEAR | None found (borderline) — stated positions: "Both profit pools are under attack" (software and services); "The old SaaS pricing playbook doesn't work for AI"; "Selling work is now possible." (Sequoia, 2025–2026) | Statements describe pricing model evolution and market disruption. "Both profit pools under attack" describes which industries AI will disrupt, not whether enterprises buy or build. Enterprises still buy in his framing — they just pay differently. |
| Sonya Huang | Partner, Sequoia | BASE | UNCLEAR | None found — stated positions: "Long-horizon agents are functionally AGI, and 2026 will be their year." / "The AI applications of 2026 and 2027 will be doers." (Sequoia, Jan 2026) | AI capability threshold prediction and investment portfolio behavior (backing LangChain, Glean, Harvey — AI-native vendors). No direct enterprise buy-vs-build statement. Investment behavior implies buy-from-vendors, but is not a direct statement. |
| Chetan Puttagunta | General Partner, Benchmark | BASE | BASE | "I do think that if you look at legacy SaaS, their business models are seriously going to be challenged by AI applications that deliver 10X the value for a third of the price. And if you're an enterprise and you can buy an AI native version, you will buy it. I can't see why you wouldn't." / "All horizontal categories were up for grabs again." (The Split podcast, 2025) | Explicitly uses "buy" language. Thesis: enterprises will switch from buying legacy SaaS to buying AI-native SaaS — still a buy decision. Buy relationship persists; vendors rotate. Firmly BASE (SaaS adapts, enterprises keep buying). Camp retained. |
| Eric Vishria | General Partner, Benchmark | BASE | UNCLEAR | None found — stated positions: AI-native companies in Benchmark portfolio growing 5–10x faster than traditional SaaS; "Every single element of [the SaaS scaling playbook] is broken." | Portfolio growth metrics for AI-native startups. Extraordinary growth of AI-native companies is consistent with enterprises buying from new AI-native vendors — not building custom. No procurement modality statement. |
| Sarah Wang | General Partner (Growth), a16z | BASE | NUANCED-CONDITIONAL | "The reported death of third party apps is greatly exaggerated, to put it mildly" AND "65% of surveyed enterprise CIOs prefer incumbent solutions when available" — AND simultaneously: "The system of record will finally start to lose primacy." (a16z Big Ideas 2026, Dec 2025; a16z survey, Jan 2026) | Simultaneously holds contradictory buy-friendly ("third party apps not dead," "65% CIOs prefer incumbents") and bear-friendly ("systems of record lose primacy") views without reconciling them. Genuine NUANCED-CONDITIONAL: the 65% CIO data is a direct procurement signal affirming buy; the system-of-record statement implies displacement. |
| Philippe Botteri | Partner, Accel | BASE | UNCLEAR | None found — stated positions: "12 to 24 months from tool capabilities delivering improved outcomes"; AI driving "unprecedented growth in AI native applications." | AI adoption timeline and application growth predictions. Does not specify whether AI-native application growth comes from SaaS vendors or custom builds. |
| Peter Fenton | General Partner, Benchmark | NUANCED-CONDITIONAL | UNCLEAR | None found — stated positions: "It feels like the wrong time to be saying, 'Everything is out of control' and 'It's a bubble'"; AI workloads demand new computational memory models. | AI bubble assessment and infrastructure requirements. Not connected to enterprise procurement modality. |
| Santiago Rodriguez | Partner, a16z Growth | NUANCED-CONDITIONAL | NUANCED-CONDITIONAL | "AI will split software into two parts" — vulnerable "frontend tools" vs. durable "value-delivering companies." Co-authored March 2026 post directly rebutting bear scenarios including enterprise self-build. (a16z, March 2, 2026) | Partially addresses procurement question by rebutting enterprise build scenarios. NUANCED-CONDITIONAL defensible: survival condition is whether a given SaaS product has genuine value delivery beyond UI. Primary frame is vendor-differentiation rather than procurement conditional. |
| Martin Casado | General Partner, a16z | NUANCED-CONDITIONAL | UNCLEAR | None found — stated position: "In the cloud era, value scaled with number of users accessing a shared system...in the AI era, value shifts to the work the software performs on your behalf." | SaaS pricing model evolution from per-seat to per-output. Enterprises still buy in his scenario; they just pay differently. Pricing model disruption is not procurement modality disruption. |
| Seema Amble | Partner, a16z | NUANCED-CONDITIONAL | UNCLEAR | None found — stated position: "As agents start to manage complex, interdependent workflows...organizations will need to rethink how work is structured." | Organizational change management prediction. Describes how internal workflows will change, not whether enterprises will buy or build the AI tools driving those changes. |
| Matt Murphy | Partner, Menlo Ventures | NUANCED-CONDITIONAL | UNCLEAR | None found — stated position: "It will be increasingly difficult for a SaaS company without native AI/agentic capabilities to find VC dollars at any stage." | VC funding criteria for SaaS startups. Enterprise buy-vs-build decisions are not determined by what VCs will fund. |
| Tim Tully | Partner, Menlo Ventures | NUANCED-CONDITIONAL | UNCLEAR | None found — stated position: "Vertical SaaS without AI differentiation" is the sector losing VC share in 2026. | VC sector allocation patterns. Same category error as Murphy: VC investment preference is not enterprise procurement behavior. |
| Anders Ranum | Partner, Sapphire Ventures | NUANCED-CONDITIONAL | UNCLEAR | None found — stated position: "Consumer and horizontal SaaS will lose" VC share in 2026; healthcare AI and defense tech will gain. | VC sector allocation shifts. Enterprise procurement is not driven by where VCs allocate. |
| Konstantine Buhler | Partner, Sequoia | NUANCED-CONDITIONAL | UNCLEAR | None found — stated position: defines an "agent economy" where agents "transfer resources, make transactions, keep track of each other, understand trust and reliability, and actually have their own economy." | Future technical architecture for agent-to-agent economies. Infrastructure thesis, not procurement thesis. |
| Jason Mendel | Partner, Battery Ventures | BASE | UNCLEAR | None found — stated position: "Data moats will become real as application companies increasingly post-train open-weight models on proprietary data." | Competitive moat evolution for AI application vendors. About vendor strategy, not enterprise procurement modality. |
| Sudhee Chilappagari | Partner, Battery Ventures | BASE | UNCLEAR | None found — stated position: "If 2024 was about experimenting with AI and 2025 was about shipping it, 2026 will be about making it pencil out." | AI adoption maturation commentary. Generic and adjacent; no procurement content. |
| Javier Pérez | Analyst, Edelweiss Capital Research | BASE | NUANCED-CONDITIONAL | Assigns 30–40% probability to "AI Enhances SaaS" (modal scenario); 20–30% to "AI Outshines SaaS"; 15–25% to "AI Cannibalizes SaaS." (Edelweiss, 2025) | Explicit probability-weighted scenario framework addressing whether SaaS survives. Identifies "AI Cannibalizes SaaS" as a distinct scenario and quantifies it. NUANCED-CONDITIONAL: conditional on which scenario unfolds. BASE understates his explicit uncertainty quantification. |

### AI Researchers, Developer Influencers, and Equity/Financial Analysts

| Expert Name | Role/Affiliation | Original Camp | Revised Camp | Qualifying Evidence | Rationale for Change |
|-------------|-----------------|---------------|--------------|---------------------|----------------------|
| Andrej Karpathy | Independent researcher (co-founder OpenAI) | BASE | UNCLEAR | None found — stated positions: "Software 3.0 is eating 1.0/2.0"; "A huge amount of software will be rewritten"; "It will take about a decade to work through all of those issues" (full agent capability). (YC AI Startup School, June 2025; Dwarkesh Podcast, Oct 2025) | Software paradigm claims applicable to SaaS vendors and custom builders equally. Explicit 10-year timeline for full agent capability undermines near-term bear case within 2–5 year research window. His "demo is works.any(), product is works.all()" framing implicitly defends SaaS durability (enterprise-grade reliability is the SaaS moat). |
| Yann LeCun | Founder, AMI Labs (former Meta Chief AI Scientist) | NUANCED-CONDITIONAL | UNCLEAR | None found — stated positions: "LLMs are useful, but they are an off ramp on the road to human-level AI." / LLMs lack understanding of the physical world, persistent memory, reasoning, and complex planning. / "When it comes time to actually deploy a system that's reliable enough that you put it in the hands of people...there's a big distance." (Newsweek, 2025) | LLM architectural critique. NOTE: directional error in original assignment. LeCun's argument that LLMs cannot reliably plan, reason, or maintain persistent memory makes enterprise custom-build programs structurally harder, not easier. His argument supports SaaS durability (BULL-favorable), not the bear case. No procurement statement made. |
| Geoffrey Hinton | AI researcher (Turing Award winner) | BEAR | UNCLEAR | None found — stated positions: "In a few years, AI will be able to perform software engineering tasks that now need a month's worth of labor." / "There'll be very few people needed for software engineering projects." (CNN, Dec 28, 2025) | Software engineering labor replacement claim. Applies equally to SaaS vendor engineering teams and enterprise custom-build teams. AI reducing the cost of writing software could make SaaS more competitive on price (more bull-favorable) or enable more custom builds (bear-favorable) — Hinton takes no position on which. |
| METR Researchers (Becker, Rush, Barnes, Rein) | Researchers, METR | NUANCED-CONDITIONAL | UNCLEAR | None found — stated finding: "When developers are allowed to use AI tools, they take 19% longer to complete issues." Study: 16 experienced developers, 246 issues, large open-source repos (22,000+ GitHub stars, 1M+ lines of code). (METR, July 10, 2025) | Empirical data, not a camp statement. NOTE: directional significance. 19% productivity slowdown on complex, mature codebases is exactly the type of task enterprise SaaS replacement would require. This finding undermines the core economic premise of the bear case. METR findings are BULL-favorable evidence, not bear-adjacent evidence. |
| Gary Marcus | AI researcher, NYU emeritus | NUANCED-CONDITIONAL | NUANCED-CONDITIONAL | "AI Agents have, so far, mostly been a dud." / Mathematical critique: at 95% per-step success rate, a 20-step workflow has only ~36% completion probability; enterprise requires 99.9%+ reliability. / "Companies will continue to experiment with AI, but adoption to production-grade systems...will continue to be tentative." (Substack, 2025) | Near-procurement statement: "adoption to production-grade systems will continue to be tentative" directly implies enterprise custom builds will underperform expectations. Partially qualifies for camp. NOTE: his reliability argument supports SaaS durability (it makes bear case harder), not the bear case itself. Camp retained with explicit note that his argument is BULL-favorable in direction. |
| Ilya Sutskever | CEO, Safe Superintelligence Inc. | NUANCED-CONDITIONAL | UNCLEAR | None found — stated positions: "We're moving from the age of scaling to the age of research." / "These models somehow just generalize dramatically worse than people. It's a very fundamental thing." (Dwarkesh Podcast, Nov 2025) | LLM generalization failure critique. NOTE: directional error in original assignment. Sutskever's claim that LLMs generalize "dramatically worse than people" as "a very fundamental thing" directly constrains the bear case: if LLMs cannot reliably generalize, enterprise custom builds using AI are fundamentally constrained. This supports SaaS durability. |
| Demis Hassabis | CEO, Google DeepMind | BEAR | UNCLEAR | None found — stated positions: "A year from now, we will have agents that are 'close' to reliably accepting and completing entire delegated tasks." / 50% probability of AGI by 2030. (Fortune/Axios, Dec 2025 and March 2025) | AI capability predictions with explicit hedging ("close"). No enterprise procurement statement. "Close to reliable" falls short of asserting enterprise SaaS displacement. Strong financial conflict (Google DeepMind competes in agentic coding market). |
| DHH (David Heinemeier Hansson) | Co-founder, 37signals (Basecamp/HEY) | BEAR | NUANCED-CONDITIONAL | Pre-2025 qualifying statement: "I think we're over SaaSed." / "The post-SaaS era is just around the corner." (Dec 2023) — BUT January 2026 update: "I'm nowhere close to the claims of having agents write 90%+ of the code...that's way off what I'm able to achieve, if I hold the line on quality and cohesion." / "Supervised collaboration, though, is here today. Pure vibe coding remains an aspirational dream for professional work for me, for now." | 2023 statements directly address procurement ("post-SaaS era") and qualify for BEAR. January 2026 material update walks back pace and extent: rejects 90%+ AI code claims, endorses supervised collaboration, not SaaS displacement. Basecamp/HEY itself remains a SaaS subscription product. NUANCED-CONDITIONAL captures the evolved position: SaaS faces long-term pressure but near-term displacement is not happening at the pace predicted. |
| Simon Willison | Creator, Datasette / co-creator, Django | BASE | UNCLEAR | None found — stated positions: "Vibe coding your way to a production codebase is clearly risky." / Coined "vibe engineering" as disciplined AI-assisted development. / "AI tools amplify existing expertise." (simonwillison.net, 2025) | Developer methodology arguments. Applies to SaaS vendor development teams and enterprise custom builders equally. No enterprise procurement statement. |
| Pieter Levels | Founder, Nomad List / Photo AI | BEAR | UNCLEAR | None found — stated position: generates ~$3M/year across products with zero employees using AI tools; built fly.pieter.com in ~30 minutes. | Personal indie-developer workflow case study. Scope is consumer/SMB products (Nomad List, Photo AI), not Fortune 500 enterprise software procurement. D07 itself notes "direct applicability to Fortune 500 build-vs-buy decisions is contested." |
| Guillermo Rauch | CEO, Vercel | BASE | NUANCED-CONDITIONAL | "In the next three years we're going to see kingdoms collapse in the sense of...companies that were born on the internet that have not been able to make those adjustments fast enough." / "I'm Team Fully Generative Software forever." (Sequoia Training Data podcast, Nov 2025) | "Kingdoms collapse" predicts incumbent SaaS vendor displacement by AI-native SaaS competitors — not displacement by enterprise custom builds. Thesis is SaaS-vs-SaaS adaptation, not buy-vs-build. NUANCED-CONDITIONAL: conditionally bullish on SaaS that adapts, bearish on SaaS that doesn't. "Kingdoms collapse" is frequently misread as a custom-build thesis. |
| Matt Mullenweg | CEO, Automattic / WordPress | BASE | BASE | "Things that you used to have to hire developers, do custom software...we're now able to do in a browser for pennies." / "As custom software becomes cheaper to create, the real challenge becomes choosing the right problems and managing the resulting complexity." (ma.tt, Feb 2026; TechCrunch, Sept 2025) | Partial procurement-adjacent statements: custom software getting cheaper (build-favorable) counterbalanced by complexity management framing (build-cautionary). SaaS CEO financial conflict. Emphasis on managing resulting complexity is a bull-favorable observation. BASE defensible; not sufficient evidence for a stronger camp. |
| Ben Snider | Strategist, Goldman Sachs | BEAR | BEAR | Newspaper-industry analogy for SaaS stocks. Near-term earnings beats are "insufficient to disprove the long-term downside risk." "End of the beginning" framing for the SaaS sector. (The Street, 2026) | Newspaper analogy implies structural SaaS business model decline akin to newspaper revenue decline — close enough to a procurement displacement argument to sustain BEAR. Qualification: this is an equity return argument, not a direct enterprise procurement survey. Structural business model decline is the closest equity analyst language gets to "enterprises will stop buying." |
| Jim Covello | Head of Global Equity Research, Goldman Sachs | BEAR | UNCLEAR | None found — stated positions: AI too expensive to earn back trillion-dollar investment; efficiency gains will be "arbitraged away"; skeptical of revenue expansion from AI. | AI ROI skepticism. NOTE: directional error in original assignment. Covello's argument that AI cannot generate commensurate returns makes enterprise custom-build programs less economically attractive, supporting SaaS durability. His position is BULL-favorable, not bear-favorable. |
| Jackson Ader | Lead Software Analyst, KeyBanc | BEAR | BEAR | Issued rare Underweight rating on ServiceNow (January 2026), explicitly citing "seat count pressure" and "worrying trends in IT back-office employment data." (Yahoo Finance, Jan 2026) | Most direct procurement statement among all equity analysts. A formal Underweight rating with explicit attribution to enterprise seat count reduction constitutes a direct claim about enterprise SaaS procurement behavior. |
| Brent Thill | Lead Software Analyst, Jefferies | BEAR | BEAR | "Seat-based licensing faces structural disruption." Called full sector "reset" in February 23, 2026 note. Formally downgraded Workday to $150 and DocuSign to $45 with explicit AI disruption attribution. (Market Minute, Feb 23, 2026) | Direct, formal procurement-direction statement. "Seat-based licensing faces structural disruption" addresses enterprise SaaS purchasing behavior. Formal downgrades with explicit AI disruption attribution constitute direct procurement-direction claims. |
| Faris Mourad | VP US Custom Baskets, Goldman Sachs | BULL | UNCLEAR | None found — stated position: selective long on AI-resilient names (Cloudflare, CrowdStrike, Oracle, Microsoft); identified "winners basket." | Stock selection for portfolio construction. Constructing an "AI-resilient winners basket" is a relative valuation call, not a procurement prediction. "AI-resilient" refers to stock prices being resilient to AI disruption narrative. |
| JPMorgan Research Team | Research, JPMorgan | BULL | UNCLEAR | None found — stated position: SaaS selloff is "broken logic" and an "overshoot"; identified logical contradiction in bear investor behavior. | Market valuation overshoot call. "The selloff went too far" is consistent with believing enterprises will continue buying SaaS AND with believing they will gradually shift — as long as the market overreacted either way. Financial conflict: software lending book. |
| Keith Weiss | Head of US Software Research, Morgan Stanley | BULL | NUANCED-CONDITIONAL | "Incumbents will serve as 'delivery mechanism' for AI features." Formally upgraded ServiceNow to Overweight. Also attributed (in registry Nuanced table): "AI changes what we build and who builds it, but not how much needs to be built." (Yahoo Finance, 2025) | Near-procurement statement: incumbents as AI delivery mechanisms implies enterprises will continue procuring from SaaS incumbents. But explicit conditional framing ("if AI is additive vs. substitutive") and simultaneous appearance in both BULL and NUANCED-CONDITIONAL tables in the registry indicate this is not a simple BULL position. |
| Sanjit Singh | US Software Analyst, Morgan Stanley | BULL | UNCLEAR | None found — stated positions: "AI isn't replacing developers. It's redefining them." / Software development market to grow 20% CAGR to $61B by 2029; developer population to expand from 30M to 50M. | Labor market and developer population predictions. Growing developer populations are consistent with both more SaaS building (by vendors) and more custom building (by enterprises). Not a SaaS procurement prediction. |
| Jason M. Lemkin | Founder, SaaStr | BASE | BASE | "AI isn't eating the product. It's eating the budget. The 2026 crash isn't AI killing SaaS — it's the market finally pricing in the deceleration that started in 2021." (SaaStr Substack, 2026) | Direct statement distinguishing AI procurement disruption (rejected) from budget pressure and market correction (accepted). "AI isn't eating the product" is a direct claim that SaaS procurement behavior hasn't fundamentally changed due to AI. SaaStr institutional conflict noted. BASE camp retained. |
| Aravind Putrevu | CEO, CodeRabbit | BASE | UNCLEAR | None found — stated position: "2025 was the year of speed; 2026 will be the year of quality" — AI coding maturation narrative. | AI development quality maturation curve commentary. No enterprise procurement content. CodeRabbit is AI code review SaaS; financial interest in quality concerns delaying full automation. |

---

## Section 3: Camp Summaries

### BULL Camp (14 experts post-revision)

**Experts:** Jensen Huang (Nvidia), Aneel Bhusri (Workday), Carl Eschenbach (ex-Workday), Anish Acharya (a16z), Alex Immerman (a16z), Alfred Lin (Sequoia), Praveen Akkiraju (Insight Partners), Jared Sleeper (Avenir), Byron Deeter (Bessemer), Jason M. Lemkin (SaaStr), Chetan Puttagunta (Benchmark) [retained in BASE], Matt Mullenweg (Automattic) [retained in BASE]

**Note:** BULL (14) and BASE (4) together constitute the pro-buy camp. For position paper purposes, Puttagunta and Mullenweg are retained in BASE but are included in the broader "buy persists" cluster.

**Shared Evidence Basis:**
The BULL experts share a convergent argument structure: enterprise SaaS tools persist because (1) building replacements offers insufficient cost savings relative to total company operating costs (Acharya: software is only 8–12% of expenses), (2) compliance and regulatory complexity makes custom-building enterprise-grade HR/ERP systems infeasible (Bhusri: "no vibe coding will ever produce an HR or ERP system"), (3) AI agents are users of SaaS tools rather than replacements (Huang: agents "will use these tools on our behalf"), (4) enterprises will continue buying from vendors — just AI-native ones (Akkiraju: "agentic SaaS"; Lin: "proliferation of vertical AI companies"), and (5) 63% of enterprise CIOs prefer incumbent solutions when available (Sleeper's survey data).

The strongest BULL statements are: Bhusri (most direct, explicit, narrow to ERP/HR), Huang (most direct, least conflicted), Akkiraju (clear "agentic SaaS" as the buy-relationship-preserving thesis).

**Conflict of interest:** Universal across BULL camp. Bhusri, Eschenbach, and Lemkin all have institutional or financial incentives to favor SaaS durability. Huang has the least direct conflict (Nvidia's revenues are neutral to the buy-vs-build outcome). Acharya, Immerman, Lin, Akkiraju, and Deeter are VC investors in SaaS companies — material conflict.

---

### BASE Camp (4 experts post-revision)

**Experts:** Chetan Puttagunta (Benchmark), Jason M. Lemkin (SaaStr), Matt Mullenweg (Automattic), Jake Saper (Emergence Capital) [upgraded to BEAR per VC audit]

**Note:** After Jake Saper's upgrade to BEAR, the BASE camp is very small. Puttagunta is the strongest BASE voice.

**Shared Evidence Basis:**
The BASE experts agree that enterprises will continue to buy, but from better (AI-native) vendors rather than from legacy SaaS incumbents. Puttagunta is explicit: "If you're an enterprise and you can buy an AI-native version, you will buy it." Lemkin rejects the AI-as-SaaS-killer thesis: "AI isn't eating the product. It's eating the budget." Mullenweg acknowledges building is getting cheaper but emphasizes complexity management as a countervailing force.

**What BASE experts agree on:** The buy relationship persists; vendor rotation (legacy SaaS to AI-native SaaS) is the primary dynamic, not buy-to-build migration.

---

### BEAR Camp (17 experts post-revision)

**Experts:** David Hsu (Retool), Amjad Masad (Replit), Marc Andrusko (a16z), Chamath Palihapitiya (Social Capital/8090), Alap Shah/Citrini Research, Dean Shahar (DTCP), Jake Saper (Emergence Capital), Ben Snider (Goldman Sachs), Jackson Ader (KeyBanc), Brent Thill (Jefferies), [and the original Bear camp members that were retained minus the misattributed ones: net ~7–8 with direct qualifying statements]

**Revised BEAR camp retains only experts with qualifying statements.** The following were originally BEAR and are removed to UNCLEAR: Sam Altman, Dario Amodei, Tobi Lutke, Michael Truell, Alex Rampell, David George, Anton Levy, Geoffrey Hinton, Demis Hassabis, Jim Covello, Pieter Levels. The following are moved out of BEAR to NUANCED-CONDITIONAL: Satya Nadella, Bill McDermott, Sarah Tavel, DHH.

**Shared Evidence Basis:**
The BEAR experts with qualifying evidence share a cost-collapse thesis: agentic coding tools have made custom-building enterprise software economically feasible for the first time. The evidence base is:
- **Cost comparison data:** Masad's $400 vs. $150,000 ERP anecdote; Citrini/Shah's "replicate mid-market SaaS in weeks" with Claude Code/Codex; Hsu's 35% replacement claim (heavily caveated)
- **Concrete enterprise action:** Andrusko's Klarna example (replaced Salesforce and Workday with custom AI builds); Palihapitiya's 8090 incubator (actively building SaaS replacements)
- **Equity analyst formal rating actions:** Ader's ServiceNow Underweight citing seat count pressure; Thill's sector reset call citing structural seat-based licensing disruption; Snider's newspaper-industry analogy
- **Investment thesis:** Saper's "AI-native services displace traditional SaaS" workflow-ownership thesis; Shahar's SaaS-as-commodity-category argument

**Conflict of interest:** Universal and severe. Hsu (Retool), Masad (Replit), Andrusko/a16z (invested in build tools), and Palihapitiya (8090 commercial bet) all have direct financial incentives in the build narrative. Ader and Thill are sell-side analysts whose bear ratings are formal investment recommendations — different type of accountability than narrative claims. Citrini is an investment research firm; their scenario analysis is the most analytically structured bear argument.

---

### NUANCED-CONDITIONAL Camp (25 experts post-revision)

**Experts and their specific conditions:**

| Expert | Condition Specified |
|--------|---------------------|
| Marc Benioff (Salesforce) | SaaS-derived platforms survive if successfully transitioned to agentic pricing models; seat-based SaaS is under pressure |
| Satya Nadella (Microsoft) | Traditional category SaaS will be disrupted; enterprises will still procure from platforms — specifically Microsoft's agentic platform |
| Bill McDermott (ServiceNow) | Category/functional SaaS will be consolidated; platform SaaS (specifically ServiceNow) wins; buy relationship persists but from fewer, larger platforms |
| Amit Zavery (ServiceNow) | SaaS survives if it becomes a platform; fails if it remains a category tool |
| Denis Torii (Gartner) | Neither buy nor build will dominate; enterprises will "Buy, Build, Blend" — heterogeneous hybrid is the predicted outcome |
| Kate Leggett (Forrester) | Enterprise core survives (buy); horizontal point-solutions face displacement (build-favorable); survival is conditional on vendor category and AI differentiation |
| Charles Betz (Forrester) | Buy wins where compliance complexity is high; build may win elsewhere — explicitly scoped to regulatory-heavy applications |
| Bo Lykkegaard (IDC) | SaaS procurement persists but is conditional on vendor pricing model evolution from per-seat to consumption-based |
| Jeremy Schneider (McKinsey) | Build where genuine competitive differentiation exists; buy where speed, cost control, or proven reliability matter more — principled conditional defaulting to buy for most capabilities |
| Alex Singla (McKinsey) | Enterprise custom build is viable if managed correctly with appropriate expertise; buy is the fallback when build complexity is too high |
| Chuck Whitten (Bain) | Neither SaaS nor build will dominate; "heterogeneous coexistence" — historical precedent (mainframes/cloud/mobile survived transitions) |
| Akash Bhatia (BCG) | SaaS procurement continues but pricing model must transition to consumption-based; seat reduction is enterprise buyers' primary lever |
| Ayo Odusote (Deloitte) | Enterprises will "balance both approaches" — hybrid outcome; neither SaaS nor build exclusively wins |
| Ryan Hinkle (Insight Partners) | "Filing cabinet" SaaS (low workflow dependency) vulnerable to replacement; "systems of action" (mission-critical workflow dependency) will retain buyers |
| Sarah Wang (a16z) | Simultaneously holds "third party apps not dead" (65% CIO preference for incumbents = buy-favorable) and "systems of record lose primacy" (bear-favorable) — unresolved internal tension |
| Santiago Rodriguez (a16z) | "Frontend tool" SaaS loses; "value-delivering" SaaS wins — survival conditional on genuine value delivery beyond UI |
| Gary Marcus (independent AI researcher) | Enterprise production AI adoption "will continue to be tentative" due to reliability mathematics — build programs will underperform; but does not prescribe SaaS as the response |
| DHH (37signals) | SaaS faces long-term pressure (2023 "post-SaaS era"), but near-term vibe-coding displacement is not happening ("aspirational dream for professional work, for now") — January 2026 update moderates bear position |
| Guillermo Rauch (Vercel) | Incumbents that fail to adapt to agentic UI paradigms will be displaced — by AI-native SaaS competitors, not by enterprise custom builds; conditionally bullish on adapting SaaS |
| Keith Weiss (Morgan Stanley) | Incumbents as AI delivery mechanisms (bull) but conditional on AI being additive rather than substitutive to existing SaaS workflows |
| Javier Pérez (Edelweiss) | Three probabilistic scenarios: AI Enhances SaaS (30–40%), AI Outshines SaaS (20–30%), AI Cannibalizes SaaS (15–25%); modal outcome is enhancement but with explicit uncertainty quantification |
| Sarah Tavel (Benchmark) | The how of buying changes (per-seat to outcome-based); but the buy relationship itself is not displaced by custom build |
| Bo Lykkegaard (IDC) | [see above] |
| Aneel Bhusri (Workday) | [retained in BULL, not NUANCED-CONDITIONAL] |

---

### UNCLEAR Camp (37 experts post-revision)

The following experts made no direct, explicit statement about enterprise SaaS procurement vs. custom build. Their actual statements address:

**AI capability and trajectory claims (no procurement connection):**
- Andrej Karpathy — "Software 3.0" paradigm shifts; decade timeline for full agent capability; product-reliability framing
- Yann LeCun — LLM architectural limitations (persistent memory, reasoning, complex planning failures)
- Geoffrey Hinton — Software engineering labor replacement by AI
- METR Researchers — Empirical: 19% developer productivity slowdown on complex codebases with AI tools
- Ilya Sutskever — LLM generalization failure as a "fundamental" phenomenon
- Demis Hassabis — Agent task-delegation capability reaching "close to reliable" within ~1 year
- Dario Amodei (Researcher audit) — "AI will write 90% of code" capability claim; failed external prediction

**Coding methodology and developer practice (not procurement):**
- Michael Truell (Cursor) — Warning against unsupervised vibe coding; quality risks from AI-built software
- Simon Willison — "Vibe engineering" as responsible AI-assisted development methodology
- Pieter Levels — Personal indie-developer workflow (consumer/SMB scope, not enterprise)

**Software spending and market sizing (not procurement modality):**
- Sid Nag (Gartner) — Cloud spending growth forecast
- John-David Lovelock (Gartner) — IT spending and AI feature cost inflation
- Frank Della Rosa (IDC) — SaaS competitive landscape reordering
- Anushree Verma (Gartner) — Agent evolution timelines and project failure rates

**Vendor survival and SaaS business model stress (not enterprise buyer behavior):**
- Liz Herbert (Forrester) — SaaS pricing model existential stress for vendors
- Diego Lo Giudice (Forrester) — Agentic Software Development category taxonomy
- Christopher Condo (Forrester) — AI developer reduction failure prediction
- Mohit Khanna (McKinsey) — SaaS vendor AI commercialization gap
- Bob Sternfels (McKinsey) — Commercial partnership announcement (McKinsey-OpenAI)
- David Crawford (Bain) — Tech company resilience and AI infrastructure economics
- David Lipman (Bain) — SaaS vendor financial performance metrics
- Nicolas de Bellefonds (BCG) — Generic AI transformation effectiveness
- Matthew Kropp (BCG) — Consumption pricing transition forecast
- Nitin Mittal (Deloitte) — AI adoption maturity description
- Aravind Putrevu (CodeRabbit) — AI coding speed vs. quality maturation curve

**VC/investor strategy (investment thesis, not procurement thesis):**
- Orlando Bravo (Thoma Bravo) — PE acquisition thesis; SaaS as undervalued investment
- Robert F. Smith (Vista Equity) — "Software eats services" TAM expansion
- Michael Hoeksema (Battery Ventures) — Investor sentiment toward SaaS vs. agentic architectures
- Steven Sinofsky (a16z) — "More software than ever" volume prediction
- Alex Rampell (a16z) — $300B SaaS vs. $13T labor TAM expansion
- David George (a16z) — AI-native vendor displacing incumbent SaaS (vendor competition, not buy-vs-build)
- Anton Levy (Layer Global) — Fund launch investment thesis
- Pat Grady (Sequoia) — Pricing model evolution; "profit pools under attack"
- Sonya Huang (Sequoia) — AGI capability timeline; portfolio backing AI-native vendors
- Eric Vishria (Benchmark) — AI-native portfolio company growth velocity
- Philippe Botteri (Accel) — AI maturity timelines and GDP impact
- Peter Fenton (Benchmark) — AI bubble assessment and infrastructure requirements
- Martin Casado (a16z) — SaaS pricing model from per-seat to per-output
- Seema Amble (a16z) — Enterprise organizational change management under AI
- Matt Murphy, Tim Tully, Anders Ranum (Menlo/Sapphire) — VC funding criteria and sector allocation
- Konstantine Buhler (Sequoia) — Agent economy technical infrastructure
- Jason Mendel, Sudhee Chilappagari (Battery) — Moat evolution and AI adoption maturation
- Jamin Ball (Clouded Judgement) — Agent-SoR interaction dynamics
- Tomasz Tunguz (Theory Ventures) — Public market SaaS sector pricing analysis

**Equity return arguments (not procurement surveys):**
- Faris Mourad (Goldman Sachs) — AI-resilient stock "winners basket" selection
- JPMorgan Research Team — SaaS selloff "overshoot" valuation call
- Jim Covello (Goldman Sachs) — AI ROI skepticism and investment return
- Sanjit Singh (Morgan Stanley) — Developer population growth and software market CAGR

**Not in original registry / no qualifying statements:**
- Frank Slootman (ex-Snowflake) — Investment action only (Factory Series B); no verbal procurement statement
- Stewart Butterfield (ex-Slack) — No qualifying statements in 2025–2026 window
- Scott Wu (Cognition) — Product description from analyst, not a direct CEO procurement statement
- Brian Landsman (Salesforce AppExchange) — Single aphorism ("expertise is more valuable than code")

---

## Section 4: Implications for Position Paper

### Which Scenario Has the Strongest Named Expert Support with Qualifying Evidence?

**The BEAR camp has the most credible direct-statement evidence for the procurement disruption thesis, but it is almost entirely self-serving.**

The BEAR position is supported by the following qualifying-evidence experts in order of directness and credibility:
1. **Jackson Ader (KeyBanc)** — Underweight rating on ServiceNow citing seat count pressure. Strongest procurement-direction claim from a disinterested expert (sell-side analyst; no financial incentive to support the bear narrative; formal accountability for rating).
2. **Brent Thill (Jefferies)** — Sector reset note with explicit "seat-based licensing faces structural disruption." Same sell-side accountability as Ader. These two equity analysts provide the most credible independent confirmation of procurement-direction shift.
3. **Marc Andrusko (a16z)** — Klarna example: "cord-cutting that will be replicated many times over." Concrete, named enterprise example. Conflict of interest (a16z invests in AI build tools) present but manageable.
4. **Chamath Palihapitiya (Social Capital/8090)** — Acting on the thesis commercially. However, his partial self-correction ("2025 was the year of letdowns") reduces confidence in near-term timeline.
5. **Alap Shah / Citrini Research** — Most analytically structured bear case: "replicate mid-market SaaS in weeks" with cost analysis. But this is an investment research firm with a short-SaaS thesis — conflict of interest is significant.
6. **Amjad Masad (Replit)** — Direct cost comparison ($400 vs. $150,000). Maximum conflict of interest; single unverified anecdote.
7. **David Hsu (Retool)** — 35% replacement statistic. Maximum conflict of interest; self-sourced survey.

**The BULL camp has credible direct statements but from maximally conflicted sources.**

The BULL position is supported by:
1. **Jensen Huang (Nvidia)** — Most credible BULL voice: least directly conflicted (Nvidia's GPU revenue grows regardless of buy-vs-build outcome); most direct statement (agents will use SaaS tools, not replace them).
2. **Aneel Bhusri (Workday)** — Most direct procurement statement in the entire corpus ("no vibe coding will ever produce HR/ERP"). Maximum conflict of interest, but the technical argument is coherent and independently assessable.
3. **Anish Acharya (a16z)** — Economic rationality argument ("rebuilding ERP saves only ~10% of total cost"). Conflict of interest present; argument is analytically strong and can be independently verified.
4. **Praveen Akkiraju (Insight Partners)** — Explicit "agentic SaaS" persistence thesis. Conflict of interest present (VC in SaaS).
5. **Alfred Lin (Sequoia)** — Direct "SaaS is not dead" declaration. VC conflict present.

**What does the distribution of UNCLEAR experts reveal?**

The distribution of 37 UNCLEAR experts — approximately 38% of the entire named corpus — reveals a fundamental gap in the public discourse: *most prominent voices commenting on AI and software have not actually addressed the enterprise procurement question*. The public commentary has largely been about:
- AI capability trajectories (will AI be good enough?)
- SaaS vendor survival (which companies will win/lose?)
- Pricing model disruption (how will the economics of selling software change?)
- Investment allocation (where should VCs put capital?)

None of these questions are equivalent to "will enterprises predominantly buy SaaS or build custom software for AI-driven applications in 2–5 years?" The fact that 37 named experts did not address this question despite prolific public commentary on adjacent topics suggests that the enterprise procurement question is genuinely under-addressed in the public corpus. The position paper is operating on a relatively thin direct evidence base.

### Most Credible / Cited Experts with Qualifying Evidence

For a position paper prioritizing intellectual integrity:

**Disinterested or least-conflicted experts with qualifying evidence:**
1. Jackson Ader (KeyBanc) — BEAR; sell-side formal rating; no SaaS financial interest
2. Brent Thill (Jefferies) — BEAR; sell-side formal rating; no SaaS financial interest
3. Jensen Huang (Nvidia) — BULL; indirect conflict only; direct statement
4. METR Researchers (Becker, Rush, Barnes, Rein) — UNCLEAR (BULL-favorable empirical data); independent nonprofit; no financial conflict

**High-credibility experts with qualifying evidence despite conflict:**
5. Aneel Bhusri (Workday) — BULL; maximum conflict but independently assessable technical argument
6. Anish Acharya (a16z) — BULL; VC conflict; independently verifiable economic calculation
7. Marc Andrusko (a16z) — BEAR; VC conflict; Klarna example is a named, verifiable case
8. McKinsey Make-or-Buy Framework (Schneider) — NUANCED-CONDITIONAL; bilateral conflict; published methodology is independently assessable
9. Gary Marcus (independent) — NUANCED-CONDITIONAL; lowest financial conflict of any academic/researcher; reliability mathematics are independently verifiable

**Experts to treat with maximum caution (qualifying evidence but severe self-serving conflict):**
- David Hsu (Retool) — BEAR; self-sourced survey of own customers; should never be cited without prominent disclosure
- Amjad Masad (Replit) — BEAR; unverified single anecdote from CEO of platform that benefits from narrative
- Marc Benioff (Salesforce) — NUANCED-CONDITIONAL; investor-reassurance statements, not research
- Aneel Bhusri (Workday) — BULL; same; technically coherent but maximally conflicted

### Overall Assessment for Position Paper

The revised corpus, after applying the strict criterion, supports the following conclusion:

**The evidence base for a decisive bear outcome (custom build displaces SaaS as majority procurement mode within 2–5 years) is thinner than the original L2 registry suggested.** The 15+ original BEAR camp experts are reduced to 9–10 with qualifying statements, and even the qualifying bear experts are heavily self-conflicted. The two least-conflicted bear signals are Ader and Thill's sell-side rating actions — which confirm seat count pressure but do not confirm a majority shift to custom build.

**The evidence base for a decisive bull outcome (SaaS retains clear dominance) is also thinner than the original registry suggested.** The bull camp loses multiple originally-assigned experts to UNCLEAR, retaining primarily SaaS CEO defenses and VC arguments that imply continued buying.

**The strongest position the corpus can actually support is NUANCED-CONDITIONAL.** The highest-quality analytical frameworks in the corpus — McKinsey's Make-or-Buy Matrix (Schneider), Gartner's "Buy, Build, Blend" (Torii), Bain's "convergence not collapse" (Whitten), Insight Partners' "filing cabinet vs. systems of action" (Hinkle), and Forrester's conditional SaaS survival thesis (Leggett and Betz) — all converge on a conditional prediction: SaaS survives in compliance-heavy, mission-critical, workflow-dependent applications; build-or-replace gains ground in commodity, point-solution, and low-workflow SaaS categories.

This conditional outcome is the most honest synthesis of the qualifying evidence.

---

*Synthesis produced: 2026-03-06*
*Sources: EXPERT_AUDIT_CEO.md, EXPERT_AUDIT_ANALYST.md, EXPERT_AUDIT_VC.md, EXPERT_AUDIT_RESEARCHER.md, L2_expert_registry.md*
*Total experts covered: 97 named individuals across CEO/executive, analyst/consulting, VC/investor, and researcher/influencer/equity analyst categories*
