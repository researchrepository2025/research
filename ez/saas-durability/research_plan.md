# Enterprise SaaS Durability in the Agentic Coding Era — Research Plan

## Purpose

This research tests the hypothesis that enterprise SaaS will remain strategically important in 2-5 years despite agentic coding enabling custom software creation at dramatically lower cost. Rather than a binary "SaaS is dead vs. alive" framing, this research estimates a **range of SaaS share** across scenarios (bull/base/bear), maps expert voices into each scenario camp, and identifies the conditions that would trigger each outcome.

The research will inform C-suite and Board-level decisions about enterprise software strategy, SaaS investment thesis durability, and build-vs-buy portfolio allocation.

## Research Parameters

- **Audience:** C-suite / Board — strategic decision-makers
- **Focus:** Enterprise application-layer SaaS durability vs. custom-built alternatives enabled by agentic coding
- **Comparison Model:** Build-vs-Buy spectrum: 100% custom-built → AI-assisted build → hybrid (SaaS + custom) → fully managed SaaS
- **Analysis Framing:** Primary axis: stakeholder perspective (who is making the argument). Secondary axis: SaaS category (where it naturally surfaces — not forced). Cross-cutting: agentic coding capabilities + TCO/ROIC.
- **Output Phases:** (1) Modular research files → (2) Stakeholder × argument matrix → (3) Scenario-based position paper with SaaS share range estimates
- **Citation Requirement:** ALL output files must have heavy inline citations with direct URLs. 2025-2026 sources only. Priority: named expert individuals → consulting firms (McKinsey, Bain, BCG, Deloitte) → equity research → analyst firms (Gartner, Forrester, IDC). Every file must end with a "Sources" section.
- **Expert Opinion Structure:** Thematic grouping (e.g., "The SaaS-adapts camp"), with named experts and their specific positions within each group.
- **Exclusions:** Consumer/B2C SaaS. Pure infrastructure/IaaS. Open-source alternatives (unless directly relevant to a build-vs-buy argument).

## Agent Summary

| Wave | Focus | Agent Count |
|------|-------|-------------|
| Wave 1 | Foundation — SaaS landscape, agentic coding landscape, key frameworks | 8 |
| Wave 2 | VC / Investor Perspectives | 7 |
| Wave 3 | Enterprise CTO/CIO Perspectives | 7 |
| Wave 4 | SaaS Vendor Perspectives | 7 |
| Wave 5 | Consulting Firm & Analyst Perspectives | 7 |
| Wave 6 | Developer Community & Tech Leader Perspectives | 7 |
| Wave 7 | Equity Research & Financial Analysis | 6 |
| Wave 8 | Agentic Coding Deep Dive (cross-cutting) | 8 |
| Wave 9 | TCO / ROIC Deep Dive (cross-cutting) | 7 |
| **Subtotal** | **Primary research agents** | **64** |
| Synthesis L1 | Wave summaries (parallel) | 9 |
| Synthesis L2 | Cross-stakeholder integration + scenario construction | 4 |
| Synthesis L3 | Final matrix + position paper | 2 |
| **Grand Total** | | **79** |

## Terminology Glossary

- **Agentic coding:** AI systems (e.g., Cursor, GitHub Copilot, Devin, Replit Agent) that can autonomously write, debug, and deploy software with minimal human guidance — beyond autocomplete into multi-step task completion.
- **SaaS replacement:** The thesis that enterprises can use agentic coding to build custom applications that replace purchased SaaS subscriptions.
- **Enterprise-grade:** Software meeting Fortune 500 requirements for security, compliance (SOC 2, HIPAA, GDPR), reliability (99.9%+ uptime), scalability, audit trails, and support SLAs.
- **Build vs. buy:** The enterprise decision framework for whether to develop software internally or purchase from a vendor.
- **AI-native application:** Software designed from the ground up with AI as a core component, not a bolt-on feature.
- **TCO (Total Cost of Ownership):** Full lifecycle cost including development, integration, maintenance, infrastructure, training, security patching, and opportunity cost.
- **ROIC (Return on Invested Capital):** The return generated per dollar invested in building or buying software, including both financial and strategic returns.

## Standard Agent Instructions

CONTEXT: You are researching enterprise SaaS durability in the agentic coding era for a C-suite audience. The core question: what share of enterprise application needs will SaaS fulfill in 2-5 years, and will it remain strategically important even if its share shifts? This is a hypothesis test, not advocacy — present evidence objectively.

OUTPUT REQUIREMENTS:
- Write in markdown format
- Begin with a 3-5 sentence executive summary of key findings
- Use clear section headers for each sub-topic
- EVERY factual claim, statistic, quote, or technical specification MUST include an inline citation with a direct URL
- If you cannot find a citation, mark it as [UNVERIFIED] and explain why
- Include a "Sources" section at the end listing all referenced URLs
- Target 1500-2500 words per research file
- Use tables for comparative data where appropriate
- End with a "Key Takeaways" section of 3-5 bullet points
- Structure expert opinions thematically: group by position/camp, then name individuals within each group with their specific arguments

SCOPE DISCIPLINE: Stay strictly within your assigned scope boundary. Reference other agents for adjacent topics.

SOURCE QUALITY AND PRIORITY:
- Tier 1 (highest): Named expert individuals (Andrej Karpathy, etc.), consulting firms (McKinsey, Bain, BCG, Deloitte), equity research reports
- Tier 2: Analyst firms (Gartner, Forrester, IDC), enterprise surveys, SaaS vendor earnings calls
- Tier 3: Tech press (The Information, TechCrunch, etc.), blog posts from credible practitioners
- Date requirement: 2025-2026 only. If a critical source is older, mark with [PRE-2025] and explain why it's included.

QUANTITATIVE DATA: Include market sizing, adoption percentages, and comparison tables where credible data exists. Do not fabricate estimates — if data is thin, say so explicitly.

EXPERT OPINION FORMAT:
```
### [Thematic Position] Camp
**[Expert Name]**, [Title/Affiliation] — "[Direct quote or paraphrased position]" ([Source](URL), [Date])
**[Expert Name]**, [Title/Affiliation] — "[Position]" ([Source](URL), [Date])
```

CROSS-REFERENCE FORMAT: "See [Agent Title] for detailed coverage of [topic]."

TERMINOLOGY GLOSSARY:
- Agentic coding: AI systems that autonomously write, debug, and deploy software beyond autocomplete
- SaaS replacement: Thesis that enterprises can build custom apps to replace SaaS subscriptions
- Enterprise-grade: Meeting Fortune 500 requirements (security, compliance, reliability, scalability, support SLAs)
- TCO: Full lifecycle cost including dev, integration, maintenance, infra, training, security, opportunity cost
- ROIC: Return per dollar invested in building or buying software

---

## Wave 1 — Foundation

All agents in this wave follow the Standard Agent Instructions above.

### F01: Current Enterprise SaaS Market Landscape

**Research Question:** What is the current state of the enterprise SaaS market in 2025-2026 — size, growth rate, penetration, and key trends?

**Required Sub-Topics:**
- Global enterprise SaaS market size and YoY growth (2024-2026)
- Enterprise SaaS penetration rate (% of total enterprise software spend)
- Top enterprise SaaS categories by revenue (CRM, ERP, HCM, Security, etc.)
- SaaS adoption by enterprise size (large enterprise vs. mid-market)
- Net revenue retention trends across public SaaS companies
- Key market trends: consolidation, platform plays, vertical SaaS

**Scope Boundary:** Do NOT cover agentic coding capabilities (see F03/F04), SaaS vendor strategies (see Wave 4), or financial analysis (see Wave 7).

**Output Path:** wave1/F01_enterprise_saas_market_landscape.md

---

### F02: Enterprise SaaS Adoption Patterns and Buying Behavior

**Research Question:** How do enterprises currently evaluate, procure, and manage SaaS — and how is this changing?

**Required Sub-Topics:**
- Enterprise SaaS procurement processes and decision-makers
- Average number of SaaS applications per enterprise
- SaaS sprawl and rationalization trends
- Shadow IT and developer-led SaaS adoption
- Multi-year contract trends and commitment patterns
- Enterprise SaaS governance and management platforms

**Scope Boundary:** Do NOT cover SaaS vendor strategies (see Wave 4) or TCO analysis (see Wave 9).

**Output Path:** wave1/F02_saas_adoption_patterns.md

---

### F03: Agentic Coding — Current State of the Art

**Research Question:** What can agentic coding tools actually do today (2025-2026) in terms of autonomous software creation?

**Required Sub-Topics:**
- Major agentic coding tools and their capabilities (Cursor, Copilot, Devin, Replit Agent, etc.)
- Types of applications that can be built with current agentic tools
- Success rate and quality benchmarks (SWE-bench, etc.)
- Current limitations and failure modes
- Developer adoption rates and usage patterns
- Enterprise adoption of agentic coding tools

**Scope Boundary:** Do NOT cover projected future capabilities (see F04), TCO implications (see Wave 9), or specific enterprise case studies (see Wave 3).

**Output Path:** wave1/F03_agentic_coding_current_state.md

---

### F04: Agentic Coding — Projected Capabilities (2-5 Year Horizon)

**Research Question:** What are credible projections for agentic coding capabilities in 2027-2031, and what would they need to achieve to meaningfully threaten SaaS?

**Required Sub-Topics:**
- Expert projections for agentic coding capability evolution
- Key technical milestones needed (multi-step reasoning, persistent context, etc.)
- Projected improvements in code quality and reliability
- Expected tooling ecosystem evolution
- What "enterprise-grade" custom software via agentic coding would require
- Optimistic vs. pessimistic timeline scenarios

**Scope Boundary:** Do NOT cover current capabilities (see F03) or TCO projections (see Wave 9).

**Output Path:** wave1/F04_agentic_coding_projections.md

---

### F05: The Build vs. Buy Decision Framework

**Research Question:** How have enterprises historically made build-vs-buy decisions, and what factors determine the outcome?

**Required Sub-Topics:**
- Classical build-vs-buy decision frameworks
- Key decision factors: cost, time-to-value, competitive advantage, core vs. context
- How the decision framework has evolved over the past decade
- The "build trap" — historical failures of enterprises building custom software
- When building makes strategic sense (competitive differentiation, unique workflows)
- How agentic coding changes the variables in the framework

**Scope Boundary:** Do NOT cover specific TCO numbers (see Wave 9) or specific vendor strategies (see Wave 4).

**Output Path:** wave1/F05_build_vs_buy_framework.md

---

### F06: AI-Native vs. AI-Enhanced Applications Taxonomy

**Research Question:** What is the taxonomy of AI-driven enterprise applications, and how does each category relate to the SaaS-vs-build question?

**Required Sub-Topics:**
- AI-enhanced SaaS (existing SaaS with AI features bolted on)
- AI-native SaaS (SaaS built from the ground up around AI)
- AI-generated custom apps (built via agentic coding)
- Hybrid models (SaaS platforms with custom AI extensions)
- Which categories are growing fastest
- Which categories threaten traditional SaaS vs. complement it

**Scope Boundary:** Do NOT cover specific vendor strategies (see Wave 4) or developer tool details (see Wave 6/8).

**Output Path:** wave1/F06_ai_application_taxonomy.md

---

### F07: Historical Precedents — Past Disruptions to Enterprise Software

**Research Question:** What can past technology disruptions (cloud, open source, low-code) teach us about whether agentic coding will displace SaaS?

**Required Sub-Topics:**
- On-premise to SaaS transition: timeline, adoption curve, resistance
- Open source disruption of commercial software: what replaced, what didn't
- Low-code/no-code disruption thesis: what actually happened
- Mobile disruption of enterprise software
- Common patterns: which disruptions displaced incumbents vs. were absorbed
- Lessons for the agentic coding disruption thesis

**Scope Boundary:** Do NOT cover current agentic coding capabilities (see F03/F04) or financial analysis (see Wave 7).

**Output Path:** wave1/F07_historical_precedents.md

---

### F08: The "SaaS is Dead" Narrative — Origin and Evolution

**Research Question:** Where did the "SaaS is dead" narrative originate, how has it evolved, and what are its core claims?

**Required Sub-Topics:**
- Timeline of the "SaaS is dead" narrative emergence (key blog posts, talks, tweets)
- Core claims of the narrative and who originated each
- How the narrative has evolved from early 2024 to mid-2026
- Media amplification and counter-narratives
- Distinction between "SaaS pricing is dead" vs. "SaaS category is dead" arguments
- The role of AI hype cycles in fueling the narrative

**Scope Boundary:** Do NOT cover specific stakeholder positions in depth (see Waves 2-6) — focus on the narrative arc itself.

**Output Path:** wave1/F08_saas_is_dead_narrative.md

---

## Wave 2 — VC / Investor Perspectives

All agents in this wave follow the Standard Agent Instructions above.

### V01: a16z / Andreessen Horowitz on SaaS and AI

**Research Question:** What is Andreessen Horowitz's position on SaaS durability in the agentic coding era, and how has it evolved?

**Required Sub-Topics:**
- Marc Andreessen's stated positions on SaaS and AI
- a16z partner views (Martin Casado, Jennifer Li, etc.) on SaaS disruption
- a16z investment thesis: are they investing in SaaS or SaaS-replacement plays?
- a16z research and blog posts on the topic
- How a16z's position has evolved from 2024-2026
- Specific claims and the evidence they cite

**Scope Boundary:** Do NOT cover other VC firms (see V02-V04) or developer tools in depth (see Wave 6).

**Output Path:** wave2/V01_a16z_positions.md

---

### V02: Top-Tier VC Perspectives (Sequoia, Benchmark, Accel, Lightspeed)

**Research Question:** What are the major top-tier VC firms' positions on enterprise SaaS durability and the build-vs-buy shift?

**Required Sub-Topics:**
- Sequoia partner positions and investment patterns
- Benchmark partner positions (especially re: SaaS portfolio)
- Accel and Lightspeed positions on enterprise software evolution
- Consensus vs. divergence among top-tier VCs
- How VC investment patterns (new deals, follow-ons) reflect their true beliefs
- Notable contrarian positions within these firms

**Scope Boundary:** Do NOT cover a16z (see V01), growth equity (see V03), or public market investors (see V05).

**Output Path:** wave2/V02_top_tier_vc_perspectives.md

---

### V03: Growth Equity and Late-Stage Investor Perspectives

**Research Question:** How are growth equity firms and late-stage investors positioning on enterprise SaaS durability?

**Required Sub-Topics:**
- Insight Partners, General Atlantic, Tiger Global positions
- Thoma Bravo and Vista Equity (PE perspective on SaaS)
- How late-stage SaaS valuations reflect durability expectations
- Growth equity deal flow: SaaS vs. AI-native startups
- Portfolio company strategies being recommended by growth investors
- Down-round and restructuring patterns in SaaS portfolio companies

**Scope Boundary:** Do NOT cover early-stage VCs (see V01/V02) or public market analysis (see V05/Wave 7).

**Output Path:** wave2/V03_growth_equity_perspectives.md

---

### V04: "SaaS is Dead" VC Voices — Arguments and Evidence

**Research Question:** Which investors are most vocally arguing that SaaS will be disrupted by agentic coding, and what evidence do they cite?

**Required Sub-Topics:**
- Named investors with the strongest "SaaS is dead" positions
- Core arguments: cost compression, speed of custom development, AI-native superiority
- Specific evidence and examples cited by bearish investors
- Investment patterns: are they putting money where their mouths are?
- Rebuttals they face and their responses
- Credibility assessment: track record of these investors' predictions

**Scope Boundary:** Do NOT cover the "SaaS adapts" camp (see V05) or non-investor voices (see Waves 3-6).

**Output Path:** wave2/V04_saas_is_dead_vc_voices.md

---

### V05: "SaaS Adapts" VC Voices — Arguments and Evidence

**Research Question:** Which investors argue that SaaS will adapt and remain dominant, and what evidence do they cite?

**Required Sub-Topics:**
- Named investors with the strongest "SaaS adapts" positions
- Core arguments: moats, data effects, ecosystem lock-in, enterprise inertia
- Specific evidence and examples cited by bullish investors
- Investment patterns: continued SaaS bets and rationale
- How they address the agentic coding challenge
- Credibility assessment: track record of these investors' predictions

**Scope Boundary:** Do NOT cover the "SaaS is dead" camp (see V04) or non-investor voices (see Waves 3-6).

**Output Path:** wave2/V05_saas_adapts_vc_voices.md

---

### V06: VC Investment Flow Analysis — Where is Capital Going?

**Research Question:** What do actual VC investment patterns in 2025-2026 reveal about investor beliefs on SaaS vs. AI-native vs. build tools?

**Required Sub-Topics:**
- VC funding into SaaS startups vs. AI-native startups (2024-2026 trends)
- Funding into agentic coding / developer tools specifically
- Funding into "SaaS replacement" or "SaaS alternative" startups
- Category-level shifts: which SaaS categories see declining vs. stable investment
- Valuation multiple trends for SaaS vs. AI-native startups
- What the money flow says vs. what VCs say publicly

**Scope Boundary:** Do NOT cover public market analysis (see Wave 7) or individual VC positions (see V01-V05).

**Output Path:** wave2/V06_vc_investment_flow.md

---

### V07: VC Nuanced / Conditional Positions

**Research Question:** Which investors hold nuanced, conditional views on SaaS durability — "it depends on X" — and what are their conditions?

**Required Sub-Topics:**
- Named investors with conditional/nuanced positions
- Key conditions identified: SaaS category, enterprise size, complexity level, etc.
- "SaaS shrinks but doesn't die" arguments and who holds them
- "Different categories have different fates" arguments
- Timeline-dependent views (short-term vs. long-term)
- How nuanced positions differ from both bull and bear camps

**Scope Boundary:** Do NOT cover strong bull (see V05) or strong bear (see V04) positions — focus on the middle ground.

**Output Path:** wave2/V07_vc_nuanced_positions.md

---

## Wave 3 — Enterprise CTO/CIO Perspectives

All agents in this wave follow the Standard Agent Instructions above.

### E01: Fortune 500 CTO/CIO Views on Build vs. Buy Shift

**Research Question:** How are Fortune 500 technology leaders thinking about the build-vs-buy equation in the agentic coding era?

**Required Sub-Topics:**
- Named CTO/CIO positions from major enterprises
- Survey data on enterprise build-vs-buy intentions (Gartner, Forrester, etc.)
- How CTO/CIO perspectives differ from VC narratives
- Pilot programs: enterprises experimenting with building SaaS replacements
- Risk tolerance: what Fortune 500 CTOs are willing to build vs. buy
- Board-level conversations about software strategy shifts

**Scope Boundary:** Do NOT cover mid-market enterprises (see E02) or developer-level views (see Wave 6).

**Output Path:** wave3/E01_fortune500_cto_views.md

---

### E02: Mid-Market Enterprise Technology Leaders

**Research Question:** How do mid-market (1,000-10,000 employee) enterprise technology leaders view SaaS durability differently from large enterprises?

**Required Sub-Topics:**
- Mid-market CTO/CIO positions on build vs. buy
- Resource constraints: engineering team size, budget, capability
- Mid-market SaaS dependence levels vs. large enterprise
- Appetite for agentic coding adoption in mid-market
- "Punching above weight" narrative: can mid-market build like Fortune 500?
- Mid-market specific SaaS categories most/least threatened

**Scope Boundary:** Do NOT cover Fortune 500 views (see E01) or SMB (out of scope).

**Output Path:** wave3/E02_midmarket_enterprise_views.md

---

### E03: Enterprise Views on SaaS Vendor Lock-in and Switching Costs

**Research Question:** How do enterprise leaders evaluate the lock-in and switching cost implications of SaaS vs. build decisions?

**Required Sub-Topics:**
- Perceived lock-in costs of current SaaS arrangements
- Data portability concerns and experiences
- Contract and migration friction as a SaaS moat
- Whether agentic coding reduces or increases switching costs
- Enterprise strategies for managing vendor lock-in
- How lock-in perception affects build-vs-buy decisions

**Scope Boundary:** Do NOT cover SaaS vendor moat strategies (see Wave 4) or TCO analysis (see Wave 9).

**Output Path:** wave3/E03_enterprise_lockin_views.md

---

### E04: Enterprise Integration and Platform Complexity

**Research Question:** How does integration complexity and platform sprawl affect enterprise willingness to build custom software vs. buy SaaS?

**Required Sub-Topics:**
- Average enterprise integration complexity (number of systems, APIs, data flows)
- Integration as a barrier to custom-built software
- SaaS platforms as integration hubs vs. integration headaches
- How agentic coding handles integration challenges
- Enterprise architects' views on custom vs. packaged integration
- iPaaS and middleware as enablers/barriers for both paths

**Scope Boundary:** Do NOT cover specific agentic coding capabilities (see Wave 8) or vendor platform strategies (see Wave 4).

**Output Path:** wave3/E04_integration_complexity.md

---

### E05: Enterprise Security and Compliance Requirements

**Research Question:** How do enterprise security and compliance requirements affect the feasibility of replacing SaaS with custom-built software?

**Required Sub-Topics:**
- Security certification requirements (SOC 2, ISO 27001, FedRAMP, etc.)
- Compliance frameworks and how SaaS vendors handle them vs. custom builds
- CISO perspectives on custom-built vs. vendor-managed security
- Liability and risk transfer in SaaS vs. build
- AI-generated code security concerns
- Regulated industry perspectives (financial services, healthcare, government)

**Scope Boundary:** Do NOT cover general agentic coding limitations (see Wave 8) or SaaS vendor security features (see Wave 4).

**Output Path:** wave3/E05_security_compliance.md

---

### E06: Enterprise Talent and Capability Gaps

**Research Question:** Do enterprises have the engineering talent and organizational capability to build and maintain custom software at scale, even with agentic coding?

**Required Sub-Topics:**
- Current enterprise engineering talent landscape and shortage data
- Skills required to effectively use agentic coding tools
- The "10x developer" myth vs. reality for enterprise teams
- Organizational capability: process, governance, DevOps maturity
- Training and upskilling costs and timelines
- Whether agentic coding closes or widens the talent gap

**Scope Boundary:** Do NOT cover developer community views (see Wave 6) or TCO of talent (see Wave 9).

**Output Path:** wave3/E06_talent_capability_gaps.md

---

### E07: Enterprise Pilot Programs and Early Results

**Research Question:** What concrete results have enterprises seen from pilot programs that use agentic coding to build SaaS replacements or custom applications?

**Required Sub-Topics:**
- Named enterprise case studies of agentic coding pilots
- Categories of applications being piloted (internal tools, customer-facing, etc.)
- Success metrics: time-to-deploy, cost savings, user satisfaction
- Failure cases and reasons for abandonment
- Scale-up challenges from pilot to production
- Enterprise leaders' assessments of pilot results

**Scope Boundary:** Do NOT cover agentic coding tool capabilities generically (see Wave 8) or VC interpretations of these results (see Wave 2).

**Output Path:** wave3/E07_enterprise_pilots.md

---

## Wave 4 — SaaS Vendor Perspectives

All agents in this wave follow the Standard Agent Instructions above.

### S01: Major SaaS Vendor Responses to AI Disruption (Salesforce, ServiceNow, Workday)

**Research Question:** How are the largest enterprise SaaS vendors responding to the agentic coding disruption thesis?

**Required Sub-Topics:**
- Salesforce's AI strategy and public statements on SaaS durability
- ServiceNow's AI strategy and positioning
- Workday's AI strategy and positioning
- Common themes across major vendor responses
- Product changes: AI agents, copilots, platform extensibility
- Earnings call commentary on competitive threats from AI-built alternatives

**Scope Boundary:** Do NOT cover mid-market vendors (see S02), vertical SaaS (see S03), or pricing changes (see S06).

**Output Path:** wave4/S01_major_vendor_responses.md

---

### S02: Mid-Market and Emerging SaaS Vendor Strategies

**Research Question:** How are mid-market and emerging SaaS vendors positioning for the agentic coding era?

**Required Sub-Topics:**
- Mid-market SaaS vendor AI strategies (Monday.com, HubSpot, Notion, etc.)
- Emerging SaaS vendors born in the AI era
- Differentiation strategies: going deeper vs. going broader
- Vulnerability assessment: which mid-market vendors are most at risk?
- M&A and consolidation trends in mid-market SaaS
- How mid-market vendors pitch against "just build it" alternatives

**Scope Boundary:** Do NOT cover major vendors (see S01) or vertical SaaS (see S03).

**Output Path:** wave4/S02_midmarket_vendor_strategies.md

---

### S03: Vertical SaaS Positioning and Domain Expertise Moats

**Research Question:** Are vertical SaaS vendors (industry-specific) more or less threatened by agentic coding than horizontal SaaS?

**Required Sub-Topics:**
- Vertical SaaS examples: healthcare (Epic, Veeva), fintech (Plaid, Stripe), construction (Procore), etc.
- Domain expertise as a moat that agentic coding can't easily replicate
- Regulatory and compliance knowledge embedded in vertical SaaS
- Data network effects in vertical SaaS
- Industry-specific workflow complexity
- Expert views on vertical vs. horizontal SaaS vulnerability

**Scope Boundary:** Do NOT cover horizontal SaaS vendors (see S01/S02) or general compliance analysis (see E05).

**Output Path:** wave4/S03_vertical_saas_moats.md

---

### S04: SaaS Vendor AI Feature Development

**Research Question:** What AI features are SaaS vendors shipping, and do they strengthen or weaken the SaaS value proposition?

**Required Sub-Topics:**
- AI copilot features across major SaaS platforms
- AI agent/automation features being shipped
- AI-native features that couldn't exist in custom-built alternatives
- Data advantage: SaaS vendors' proprietary training data and fine-tuning
- Customer adoption rates of SaaS AI features
- Whether AI features increase or decrease SaaS switching costs

**Scope Boundary:** Do NOT cover agentic coding tools for building software (see Wave 8) or specific vendor strategies (see S01/S02).

**Output Path:** wave4/S04_saas_ai_features.md

---

### S05: SaaS Vendor Moats — Data, Ecosystem, Workflow Embedding

**Research Question:** What are the structural moats that protect SaaS vendors from replacement, and how durable are they?

**Required Sub-Topics:**
- Data network effects and proprietary datasets
- Ecosystem moats: app marketplaces, partner networks, integrations
- Workflow embedding: when SaaS becomes the system of record
- Community and user-generated content moats
- Brand trust and enterprise relationship moats
- Expert assessments of moat durability vs. agentic coding disruption

**Scope Boundary:** Do NOT cover pricing (see S06), vendor-specific strategies (see S01-S03), or enterprise lock-in perception (see E03).

**Output Path:** wave4/S05_saas_vendor_moats.md

---

### S06: SaaS Pricing Model Evolution

**Research Question:** How are SaaS pricing models evolving in response to AI and the build-vs-buy shift?

**Required Sub-Topics:**
- Per-seat to usage-based pricing transitions
- AI feature pricing: included vs. premium tier
- "Outcome-based" pricing models emerging
- Price compression pressure from build alternatives
- SaaS vendor pricing strategy for enterprise retention
- Whether pricing model changes strengthen or weaken the SaaS value proposition

**Scope Boundary:** Do NOT cover TCO analysis (see Wave 9) or vendor strategies beyond pricing (see S01-S03).

**Output Path:** wave4/S06_saas_pricing_evolution.md

---

### S07: SaaS Vendor Platform and Extensibility Strategies

**Research Question:** How are SaaS vendors using platform and extensibility strategies to co-opt the "build" impulse rather than compete with it?

**Required Sub-Topics:**
- Platform strategies: Salesforce Platform, ServiceNow App Engine, etc.
- Low-code/no-code extensibility within SaaS platforms
- AI-powered customization within SaaS platforms
- "Build on top of SaaS" as a middle ground between build and buy
- Developer ecosystem strategies
- Whether platform strategies effectively neutralize the agentic coding threat

**Scope Boundary:** Do NOT cover general agentic coding tools (see Wave 8) or standalone low-code platforms (see F07).

**Output Path:** wave4/S07_saas_platform_strategies.md

---

## Wave 5 — Consulting Firm & Analyst Perspectives

All agents in this wave follow the Standard Agent Instructions above.

### C01: McKinsey Perspectives on Enterprise Software Evolution

**Research Question:** What is McKinsey's published position on enterprise SaaS durability, build-vs-buy shifts, and the impact of AI on software?

**Required Sub-Topics:**
- McKinsey reports and articles on SaaS and AI (2025-2026)
- Named McKinsey partners and their positions
- McKinsey Technology Council or equivalent body views
- Advisory recommendations to enterprise clients
- McKinsey Global Institute research on AI productivity
- How McKinsey's position compares to the VC narrative

**Scope Boundary:** Do NOT cover other consulting firms (see C02-C04) or analyst firms (see C05-C06).

**Output Path:** wave5/C01_mckinsey_perspectives.md

---

### C02: Bain & Company Perspectives

**Research Question:** What is Bain's published position on enterprise SaaS durability and the build-vs-buy equation in the AI era?

**Required Sub-Topics:**
- Bain reports and articles on SaaS, AI, and enterprise software (2025-2026)
- Named Bain partners and their positions
- Bain's technology practice recommendations
- Advisory patterns: what are they telling enterprise clients?
- Bain's annual technology report findings
- Specific claims and evidence cited

**Scope Boundary:** Do NOT cover McKinsey (see C01), BCG (see C03), or Deloitte (see C04).

**Output Path:** wave5/C02_bain_perspectives.md

---

### C03: BCG Perspectives

**Research Question:** What is BCG's published position on SaaS durability and enterprise software strategy in the agentic era?

**Required Sub-Topics:**
- BCG reports and articles on SaaS, AI, and enterprise software (2025-2026)
- Named BCG partners and their positions
- BCG Henderson Institute research on AI and software
- Advisory recommendations to enterprise clients
- BCG's technology advantage practice views
- Specific claims and evidence cited

**Scope Boundary:** Do NOT cover McKinsey (see C01), Bain (see C02), or Deloitte (see C04).

**Output Path:** wave5/C03_bcg_perspectives.md

---

### C04: Deloitte / Accenture / Big 4 Perspectives

**Research Question:** What are Deloitte, Accenture, and other large consulting/advisory firms' positions on SaaS durability?

**Required Sub-Topics:**
- Deloitte Technology reports and positions (2025-2026)
- Accenture Technology Vision and related reports
- PwC and EY technology advisory positions
- Common themes across Big 4 / large advisory firms
- How these firms' advisory work (implementing SaaS) creates bias
- Specific claims and evidence cited

**Scope Boundary:** Do NOT cover MBB firms (see C01-C03) or pure analyst firms (see C05-C06).

**Output Path:** wave5/C04_big4_perspectives.md

---

### C05: Gartner and Forrester Analyst Predictions

**Research Question:** What are Gartner and Forrester's formal predictions and frameworks for SaaS durability in the AI era?

**Required Sub-Topics:**
- Gartner Magic Quadrant and Hype Cycle positioning of SaaS vs. AI-native
- Forrester Wave reports and market sizing for SaaS categories
- Named analysts and their individual positions
- Formal market forecasts: SaaS growth projections through 2030
- "Composable enterprise" and related Gartner frameworks
- How analyst predictions compare to VC narratives

**Scope Boundary:** Do NOT cover IDC/other analysts (see C06) or consulting firms (see C01-C04).

**Output Path:** wave5/C05_gartner_forrester.md

---

### C06: IDC and Other Analyst Firms

**Research Question:** What are IDC and other analyst firms' positions on enterprise SaaS durability and the impact of AI on software spending?

**Required Sub-Topics:**
- IDC enterprise software spending forecasts (2025-2030)
- IDC AI spending forecasts and where the money goes
- Redpoint / Battery / other VC-analyst firm hybrid views
- CB Insights, PitchBook data on SaaS market trends
- Bloomberg Intelligence and S&P Capital IQ analyst views
- Consensus and divergence among analyst firms

**Scope Boundary:** Do NOT cover Gartner/Forrester (see C05) or consulting firms (see C01-C04).

**Output Path:** wave5/C06_idc_other_analysts.md

---

### C07: Consulting Firm Client Advisory Patterns

**Research Question:** What are consulting firms actually advising enterprise clients to do about SaaS vs. build — beyond their public positions?

**Required Sub-Topics:**
- Patterns in consulting firm engagement types (SaaS implementation vs. custom build)
- "Build a center of excellence" advisory trend
- Consulting firms' own use of agentic coding in client delivery
- Revenue model implications: do consulting firms benefit more from build or buy?
- Anonymized or reported case studies of client advisory outcomes
- Tension between consulting firms' public positions and revenue incentives

**Scope Boundary:** Do NOT cover specific firm positions (see C01-C04) — focus on advisory patterns and incentives across the industry.

**Output Path:** wave5/C07_consulting_advisory_patterns.md

---

## Wave 6 — Developer Community & Tech Leader Perspectives

All agents in this wave follow the Standard Agent Instructions above.

### D01: Andrej Karpathy and AI Researcher Views on Software Creation

**Research Question:** What do prominent AI researchers (Karpathy et al.) say about AI's ability to create software, and how does this inform the SaaS debate?

**Required Sub-Topics:**
- Andrej Karpathy's specific statements on software creation and "software 3.0"
- Other AI researchers' views: Yann LeCun, Demis Hassabis, Ilya Sutskever, etc.
- The "natural language is the new programming language" thesis
- AI researcher projections for coding agent capabilities
- How AI researchers' views differ from practitioners and enterprise leaders
- Credibility and limitations of researcher predictions for enterprise outcomes

**Scope Boundary:** Do NOT cover agentic coding tools specifically (see Wave 8) or VC investor perspectives (see Wave 2).

**Output Path:** wave6/D01_ai_researcher_views.md

---

### D02: Developer Influencer and Thought Leader Positions

**Research Question:** What are prominent developer thought leaders and influencers saying about SaaS durability and the build-vs-buy shift?

**Required Sub-Topics:**
- DHH (David Heinemeier Hansson) and the "leave the cloud" parallel
- Pieter Levels and the "indie hacker replaces SaaS" narrative
- Guillermo Rauch (Vercel), Matt Mullenweg (WordPress), other platform leaders
- Developer Twitter/X discourse patterns on SaaS replacement
- YouTube and podcast thought leaders on the topic
- The "vibe coding" meme and its implications for enterprise software

**Scope Boundary:** Do NOT cover AI researchers (see D01) or enterprise technology leaders (see Wave 3).

**Output Path:** wave6/D02_developer_influencer_views.md

---

### D03: Developer Tool Ecosystem and Its Implications

**Research Question:** How is the developer tool ecosystem evolving to enable or constrain enterprise custom software development?

**Required Sub-Topics:**
- AI-powered IDEs (Cursor, Windsurf, etc.) and their enterprise adoption
- AI coding assistants (GitHub Copilot, Amazon Q) enterprise penetration
- Autonomous coding agents (Devin, Factory, etc.) capability and adoption
- DevOps and deployment tooling for AI-generated applications
- Testing and quality assurance for AI-generated code
- Whether the tool ecosystem favors building vs. buying SaaS

**Scope Boundary:** Do NOT cover tool capabilities in technical depth (see Wave 8) or VC funding for tools (see V06).

**Output Path:** wave6/D03_developer_tool_ecosystem.md

---

### D04: Open Source Community and Its Role in the Build Equation

**Research Question:** How does the open-source ecosystem affect the build-vs-buy-SaaS equation when combined with agentic coding?

**Required Sub-Topics:**
- Open-source alternatives to major SaaS categories (and their maturity)
- Agentic coding + open source as a SaaS replacement strategy
- Open-source AI models enabling custom software (Llama, Mistral, etc.)
- Enterprise adoption of open-source alternatives to SaaS
- The "agentic coding assembles open-source components" thesis
- Limitations: support, security, compliance for open-source in enterprise

**Scope Boundary:** Do NOT cover specific agentic coding tool capabilities (see Wave 8) or enterprise compliance (see E05).

**Output Path:** wave6/D04_open_source_role.md

---

### D05: Platform Engineering Community Views

**Research Question:** How does the platform engineering community view the SaaS-vs-build debate, and what does internal developer platform adoption signal?

**Required Sub-Topics:**
- Internal developer platform (IDP) trends in enterprises
- Platform engineering as an enabler of custom software at scale
- Platform engineers' views on where SaaS is essential vs. replaceable
- Backstage, Humanitec, and other IDP tools as build enablers
- Whether platform engineering teams favor build or buy
- The "golden path" concept and its implications for SaaS replacement

**Scope Boundary:** Do NOT cover general developer tools (see D03) or enterprise CTO views (see Wave 3).

**Output Path:** wave6/D05_platform_engineering_views.md

---

### D06: Developer Experience with Building Enterprise Apps via AI

**Research Question:** What are developers actually experiencing when they try to build enterprise-grade applications using agentic coding tools?

**Required Sub-Topics:**
- Developer blog posts and experience reports on building with AI coding tools
- Common patterns: what works well, what breaks down
- "Demo-quality vs. production-quality" gap in AI-generated apps
- Maintenance burden of AI-generated code (reported experiences)
- Developer satisfaction and productivity claims vs. reality
- Community consensus on what AI coding tools are good/bad at for enterprise use

**Scope Boundary:** Do NOT cover enterprise pilot programs (see E07) or tool capabilities at a technical level (see Wave 8).

**Output Path:** wave6/D06_developer_experience_reports.md

---

### D07: Tech CEO and Founder Perspectives

**Research Question:** What are SaaS CEOs, AI startup founders, and tech company leaders saying about SaaS durability?

**Required Sub-Topics:**
- Satya Nadella (Microsoft) on software creation and SaaS
- Tobi Lutke (Shopify) on AI and commerce SaaS
- Stewart Butterfield (ex-Slack), Frank Slootman (ex-Snowflake) perspectives
- AI startup founders' views on SaaS displacement
- SaaS CEO earnings call commentary on the agentic coding threat
- Public statements vs. strategic actions (product, hiring, M&A)

**Scope Boundary:** Do NOT cover VC investors (see Wave 2) or SaaS vendor product strategies (see Wave 4).

**Output Path:** wave6/D07_tech_ceo_perspectives.md

---

## Wave 7 — Equity Research & Financial Analysis

All agents in this wave follow the Standard Agent Instructions above.

### R01: Wall Street Equity Research on SaaS Sector Outlook

**Research Question:** What is the consensus and divergence in Wall Street equity research on the SaaS sector's 2-5 year outlook?

**Required Sub-Topics:**
- Major bank coverage of SaaS (Morgan Stanley, Goldman Sachs, JP Morgan, etc.)
- Bull vs. bear research notes on SaaS sector
- How analysts are incorporating agentic coding into their models
- Target price and rating distribution for major SaaS stocks
- Key metrics analysts are watching (NRR, growth, margins)
- Notable analyst calls and their reasoning

**Scope Boundary:** Do NOT cover valuation analysis (see R02) or company-specific financials (see R04).

**Output Path:** wave7/R01_equity_research_outlook.md

---

### R02: SaaS Valuation Trends and Market Signals

**Research Question:** What do SaaS company valuations signal about market expectations for SaaS durability?

**Required Sub-Topics:**
- SaaS revenue multiple trends (2023-2026)
- Valuation differential: AI-native vs. traditional SaaS
- Public SaaS company market cap trends
- How markets are pricing SaaS disruption risk
- IPO and de-listing patterns in SaaS
- Comparison: SaaS multiples vs. enterprise software historical averages

**Scope Boundary:** Do NOT cover equity research opinions (see R01) or individual company analysis (see R04).

**Output Path:** wave7/R02_saas_valuation_trends.md

---

### R03: Enterprise IT Budget Allocation Trends

**Research Question:** How are enterprise IT budgets shifting between SaaS, custom development, and AI investments?

**Required Sub-Topics:**
- Total enterprise IT spending trends (2024-2026)
- SaaS as % of total IT spend: trajectory
- Custom software development budget allocation trends
- AI/ML specific budget allocation and where it's sourced from
- CIO survey data on budget reallocation intentions
- Whether AI spending is additive or cannibalistic to SaaS budgets

**Scope Boundary:** Do NOT cover individual company financials (see R04) or TCO analysis (see Wave 9).

**Output Path:** wave7/R03_it_budget_trends.md

---

### R04: Public SaaS Company Financial Performance Signals

**Research Question:** What do public SaaS company financial metrics reveal about the sector's health and vulnerability?

**Required Sub-Topics:**
- Revenue growth trends across public SaaS cohort (2024-2026)
- Net revenue retention rate trends (are customers spending more or less?)
- Gross margin trends (are SaaS economics holding?)
- Customer acquisition cost trends
- Free cash flow and profitability trends
- Churn and downsell patterns — any signal of SaaS replacement?

**Scope Boundary:** Do NOT cover valuation (see R02) or analyst opinions (see R01).

**Output Path:** wave7/R04_public_saas_financials.md

---

### R05: M&A Trends in Enterprise Software

**Research Question:** What do enterprise software M&A patterns reveal about industry expectations for SaaS durability?

**Required Sub-Topics:**
- SaaS M&A volume and valuations (2024-2026)
- PE acquisitions of SaaS companies (Thoma Bravo, Vista, etc.)
- AI company acquisitions by SaaS vendors
- SaaS vendor consolidation patterns
- "Acqui-hire" patterns for AI talent by SaaS companies
- Whether M&A patterns signal SaaS strengthening or decline

**Scope Boundary:** Do NOT cover VC investment (see V06) or individual vendor strategies (see Wave 4).

**Output Path:** wave7/R05_enterprise_software_ma.md

---

### R06: Venture Funding Patterns — SaaS vs. AI-Native Startups

**Research Question:** What do venture funding patterns reveal about where the market believes enterprise software is heading?

**Required Sub-Topics:**
- Total VC funding into SaaS startups vs. AI-native startups (2024-2026)
- New SaaS company formation rates vs. AI-native
- Seed/Series A patterns: are new SaaS companies getting funded?
- Category-specific funding shifts
- Geographic patterns in SaaS vs. AI-native funding
- What funding patterns predict vs. what actually happens (historical accuracy)

**Scope Boundary:** Do NOT cover specific VC firm positions (see Wave 2) or public market analysis (see R01-R04).

**Output Path:** wave7/R06_venture_funding_patterns.md

---

## Wave 8 — Agentic Coding Deep Dive (Cross-Cutting)

All agents in this wave follow the Standard Agent Instructions above. This wave fact-checks and deepens claims made across Waves 2-7.

### A01: Agentic Coding Tool Capabilities Assessment

**Research Question:** What is a rigorous, benchmarked assessment of what current agentic coding tools can and cannot build?

**Required Sub-Topics:**
- Tool-by-tool capability matrix (Cursor, Copilot, Devin, Replit Agent, Factory, etc.)
- Benchmark results: SWE-bench, HumanEval, real-world task completion rates
- Types of applications successfully built end-to-end
- Complexity ceiling: where do tools break down?
- Multi-file, multi-system project handling
- Comparison of tool claims vs. independent evaluations

**Scope Boundary:** Do NOT cover projected capabilities (see A02) or enterprise adoption (see A03). Focus on current, verified capabilities.

**Output Path:** wave8/A01_tool_capabilities_assessment.md

---

### A02: Agentic Coding Limitations and Failure Modes

**Research Question:** What are the systematic limitations and common failure modes of agentic coding for enterprise application development?

**Required Sub-Topics:**
- Hallucination and incorrect code generation rates
- Context window limitations and their impact on large codebases
- Testing and debugging limitations of AI-generated code
- Architecture and design decision limitations
- Security vulnerability introduction rates
- The "works in demo, fails in production" pattern

**Scope Boundary:** Do NOT cover current tool features (see A01) or enterprise-specific requirements (see A04).

**Output Path:** wave8/A02_limitations_failure_modes.md

---

### A03: Enterprise Adoption of Agentic Coding — Current State

**Research Question:** What is the actual enterprise adoption rate of agentic coding tools, and how are they being used?

**Required Sub-Topics:**
- Enterprise adoption rates by company size and industry
- Use cases: where enterprises are deploying agentic coding tools
- Developer satisfaction and productivity metrics in enterprise settings
- Organizational resistance and change management challenges
- IT governance and security review processes for AI coding tools
- Comparison: enterprise adoption vs. individual developer adoption

**Scope Boundary:** Do NOT cover tool capabilities (see A01) or enterprise pilots for SaaS replacement specifically (see E07).

**Output Path:** wave8/A03_enterprise_adoption_agentic.md

---

### A04: Enterprise-Grade Requirements Gap

**Research Question:** What is the gap between what agentic coding can produce and what enterprises require for production software?

**Required Sub-Topics:**
- Security requirements: vulnerability scanning, penetration testing, secure coding
- Compliance: SOC 2, HIPAA, GDPR, FedRAMP compliance in AI-generated code
- Reliability: uptime guarantees, disaster recovery, failover
- Scalability: handling enterprise-scale load
- Observability: logging, monitoring, alerting in AI-generated applications
- Support: who supports custom-built AI-generated software?

**Scope Boundary:** Do NOT cover enterprise security perspectives (see E05) or SaaS vendor security (see Wave 4).

**Output Path:** wave8/A04_enterprise_grade_gap.md

---

### A05: Agentic Coding for Maintenance and Evolution

**Research Question:** Can agentic coding tools maintain and evolve software over time, or does the advantage only apply to initial creation?

**Required Sub-Topics:**
- Bug fixing and patching with agentic tools
- Feature evolution and iteration capabilities
- Technical debt accumulation in AI-generated codebases
- Dependency management and updates
- Code comprehension: can AI tools understand and modify existing AI-generated code?
- Lifecycle cost implications: creation cost vs. maintenance cost trajectory

**Scope Boundary:** Do NOT cover initial creation capabilities (see A01) or TCO modeling (see Wave 9).

**Output Path:** wave8/A05_maintenance_evolution.md

---

### A06: Agentic Coding Maturity Curve — Projected Capabilities by Year

**Research Question:** What is a credible year-by-year maturity projection for agentic coding capabilities through 2031?

**Required Sub-Topics:**
- 2026 projected capabilities (near-term, high confidence)
- 2027-2028 projected capabilities (medium-term, moderate confidence)
- 2029-2031 projected capabilities (long-term, low confidence)
- Key technical milestones and their estimated timelines
- Expert predictions mapped to timeline
- Scenarios: optimistic vs. pessimistic capability curves

**Scope Boundary:** Do NOT cover current capabilities (see A01) or specific tool roadmaps (see A01/D03).

**Output Path:** wave8/A06_maturity_curve_projections.md

---

### A07: Integration Complexity — APIs, Data Pipelines, Multi-System Workflows

**Research Question:** How well can agentic coding handle the integration complexity that enterprise applications require?

**Required Sub-Topics:**
- API integration capabilities of current agentic tools
- Data pipeline construction and management
- Multi-system workflow orchestration
- Authentication, authorization, and SSO integration
- Real-time data synchronization challenges
- Comparison: integration effort for custom build vs. SaaS marketplace connectors

**Scope Boundary:** Do NOT cover enterprise integration architecture views (see E04) or SaaS platform extensibility (see S07).

**Output Path:** wave8/A07_integration_complexity.md

---

### A08: The "Last Mile" Problem — UI/UX, User Training, Change Management

**Research Question:** Beyond code generation, what are the "last mile" challenges of deploying custom-built enterprise software?

**Required Sub-Topics:**
- UI/UX quality of AI-generated applications vs. SaaS
- User training and onboarding for custom-built tools
- Change management costs when replacing familiar SaaS
- Documentation generation and maintenance
- User support and help desk implications
- The "it works but nobody uses it" pattern in custom enterprise software

**Scope Boundary:** Do NOT cover code quality (see A02) or enterprise organizational factors (see E06).

**Output Path:** wave8/A08_last_mile_problem.md

---

## Wave 9 — TCO / ROIC Deep Dive (Cross-Cutting)

All agents in this wave follow the Standard Agent Instructions above. This wave provides the economic analysis foundation for the final scenarios.

### T01: True TCO of Enterprise SaaS

**Research Question:** What is the true total cost of ownership of enterprise SaaS when all direct and indirect costs are included?

**Required Sub-Topics:**
- License/subscription costs (per-seat, usage-based, platform fees)
- Implementation and customization costs
- Integration costs (iPaaS, custom connectors, middleware)
- Training and change management costs
- Ongoing administration and management costs
- Vendor management overhead and contract negotiation costs

**Scope Boundary:** Do NOT cover custom-build TCO (see T02) or pricing model evolution (see S06).

**Output Path:** wave9/T01_saas_tco.md

---

### T02: True TCO of Custom-Built Enterprise Applications

**Research Question:** What is the true total cost of ownership of building and maintaining custom enterprise software, including with agentic coding?

**Required Sub-Topics:**
- Development costs: with traditional teams vs. with agentic coding
- Infrastructure costs: cloud hosting, DevOps, monitoring
- Maintenance costs: bug fixes, security patches, dependency updates
- Talent costs: hiring, retention, training of engineering team
- Opportunity cost: engineering time diverted from core business
- The "hidden iceberg": costs that enterprises consistently underestimate

**Scope Boundary:** Do NOT cover SaaS TCO (see T01) or agentic coding capabilities (see Wave 8).

**Output Path:** wave9/T02_custom_build_tco.md

---

### T03: TCO Comparison Framework — SaaS vs. Build by Category

**Research Question:** How does the TCO comparison between SaaS and build vary across different enterprise application categories?

**Required Sub-Topics:**
- CRM: SaaS TCO vs. build TCO
- ERP: SaaS TCO vs. build TCO
- HCM/HR: SaaS TCO vs. build TCO
- Security/Compliance: SaaS TCO vs. build TCO
- Internal tools and productivity: SaaS TCO vs. build TCO
- Category-level verdict: where does build win, where does SaaS win?

**Scope Boundary:** Do NOT cover individual cost components (see T01/T02) — focus on category-level comparisons.

**Output Path:** wave9/T03_tco_comparison_by_category.md

---

### T04: ROIC Analysis — When Does Building Make Economic Sense?

**Research Question:** Under what conditions does building custom enterprise software generate a superior return on invested capital compared to buying SaaS?

**Required Sub-Topics:**
- ROIC framework for build-vs-buy decisions
- Breakeven analysis: investment required vs. SaaS cost avoided
- Time-to-value: how long until custom-build generates returns
- Scale effects: does ROIC improve with company size?
- Competitive advantage premium: when custom software drives revenue
- Risk-adjusted ROIC: accounting for failure probability

**Scope Boundary:** Do NOT cover TCO components (see T01/T02) or strategic factors beyond economics (see Wave 3).

**Output Path:** wave9/T04_roic_analysis.md

---

### T05: Hidden Costs of Build — Security, Compliance, Feature Parity

**Research Question:** What are the systematically underestimated costs of building custom enterprise software that erode the agentic coding cost advantage?

**Required Sub-Topics:**
- Security: ongoing vulnerability management, penetration testing, incident response
- Compliance: maintaining certifications, audit readiness, regulatory updates
- Feature parity: keeping up with SaaS vendor feature releases
- Reliability engineering: on-call, incident management, disaster recovery
- Documentation and knowledge management
- Vendor relationship management for underlying infrastructure and APIs

**Scope Boundary:** Do NOT cover SaaS hidden costs (see T06) or general TCO models (see T01/T02).

**Output Path:** wave9/T05_hidden_costs_build.md

---

### T06: Hidden Costs of SaaS — Lock-in, Data Portability, Customization Limits

**Research Question:** What are the systematically underestimated costs and risks of SaaS that make building more attractive?

**Required Sub-Topics:**
- Vendor lock-in costs: switching cost estimates by category
- Data portability: extraction, migration, and transformation costs
- Customization ceiling: cost of working around SaaS limitations
- "SaaS tax": paying for features you don't use
- Price increase risk: SaaS vendor pricing power over locked-in customers
- Strategic risk: dependency on vendor roadmap alignment

**Scope Boundary:** Do NOT cover build hidden costs (see T05) or enterprise lock-in perception (see E03).

**Output Path:** wave9/T06_hidden_costs_saas.md

---

### T07: Economic Modeling — Break-Even and Scenario Analysis

**Research Question:** What economic models can estimate the break-even point for build-vs-buy decisions under different agentic coding capability scenarios?

**Required Sub-Topics:**
- Break-even model: variables, assumptions, sensitivity analysis
- Scenario 1 (Bear on agentic): limited capability improvement, high maintenance cost
- Scenario 2 (Base): moderate capability improvement, moderate cost reduction
- Scenario 3 (Bull on agentic): dramatic capability improvement, near-zero marginal cost
- Key variables that swing the outcome: developer productivity, maintenance burden, compliance cost
- Model outputs: under what conditions does build become cheaper than SaaS?

**Scope Boundary:** Do NOT cover specific TCO inputs (see T01-T06) — use their outputs as model inputs.

**Output Path:** wave9/T07_economic_modeling.md

---

## Quality Gates

### Structural Check: Per-Wave File Completeness
- All expected files exist at correct paths
- Each file has: executive summary, numbered sections, key takeaways, sources
- Word count within 1500-2500 range

### Citation Quality: Per-Agent Citation Quality
- Inline citations with URLs present (minimum 10 per file)
- Sources section with numbered entries
- No orphaned [UNVERIFIED] without explanation
- Source dates within 2025-2026 (or marked [PRE-2025] with justification)

### Expert Attribution Check (Custom Gate)
- Named expert claims are correctly attributed with dates and context
- No misquotes or stale positions (verified against source)
- Expert affiliations and titles are current
- Positions are not taken out of context

### Content Review (post-wave)
- Dispatch review agent to check: claims supported, ratings justified, scope discipline, terminology consistency, cross-references correct
- Score per file: PASS | MINOR_ISSUES | REWORK_NEEDED

### Coverage Check: Pre-Synthesis Coverage Checklist (after all primary waves)
- All research files complete and passing Structural Check + Citation Quality
- Every stakeholder group has representation
- Both bull and bear positions represented in each wave
- Cross-wave contradictions documented
- No critical [UNVERIFIED] claims in areas feeding scenario analysis

### Readiness Check: Pre-Final Synthesis Readiness (after Layer 2)
- All synthesis files complete with citation chains
- Conflicts resolved or flagged
- Expert positions consistently attributed
- Spot-check 10+ claims for URL traceability

## Gap Analysis Checkpoints

**After Wave 7** (all stakeholder + financial waves complete): Check coverage of all major voices represented. Are there stakeholder groups or notable experts missing? Are both sides of the debate adequately represented? Are any SaaS categories notably absent despite relevance?

**After Wave 9** (deep dives complete): Check that technical claims from stakeholder waves are grounded. Are agentic coding capability claims verified? Are TCO claims backed by data? Are there logical gaps that would undermine the scenario analysis?

## Synthesis

### Layer 1: Wave Summaries (parallel)

| Agent | Output File | Input Files | Focus |
|-------|-------------|-------------|-------|
| Wave 1 Summary | synthesis/wave-01-summary_foundation.md | F01-F08 | Key landscape facts and frameworks |
| Wave 2 Summary | synthesis/wave-02-summary_vc_investors.md | V01-V07 | VC consensus, divergence, and investment signals |
| Wave 3 Summary | synthesis/wave-03-summary_enterprise_leaders.md | E01-E07 | Enterprise technology leader consensus and actions |
| Wave 4 Summary | synthesis/wave-04-summary_saas_vendors.md | S01-S07 | Vendor strategies and moat assessment |
| Wave 5 Summary | synthesis/wave-05-summary_consultants_analysts.md | C01-C07 | Advisory consensus and forecast synthesis |
| Wave 6 Summary | synthesis/wave-06-summary_developers_tech.md | D01-D07 | Developer and tech leader perspectives |
| Wave 7 Summary | synthesis/wave-07-summary_financial.md | R01-R06 | Financial signals and market expectations |
| Wave 8 Summary | synthesis/wave-08-summary_agentic_deepdive.md | A01-A08 | Verified agentic coding capability and gap assessment |
| Wave 9 Summary | synthesis/wave-09-summary_tco_roic.md | T01-T07 | Economic analysis and break-even conditions |

Target: 800-1200 words each. Themed synthesis, not sequential summaries.
Citation: trace to agent file AND original URL.

### Layer 2: Cross-Stakeholder Integration

| Agent | Output File | Inputs | Focus |
|-------|-------------|--------|-------|
| Stakeholder × Argument Matrix | synthesis/integration-stakeholder_matrix.md | All L1 summaries | Map each argument to which stakeholders hold it and their evidence |
| Cross-Stakeholder Consensus | synthesis/integration-consensus_divergence.md | All L1 summaries | What do all groups agree on? Where do they diverge? Why? |
| Scenario Construction | synthesis/integration-scenario_construction.md | All L1 summaries, wave-08, wave-09 | Build bull/base/bear scenarios with conditions and evidence |
| Expert Mapping to Scenarios | synthesis/integration-expert_scenario_map.md | All L1 summaries | Sort named experts into scenarios with their key arguments |

Dependencies: First two integration agents parallel. Scenario Construction depends on both. Expert Mapping depends on Scenario Construction.

### Layer 3: Final Outputs (sequential)

| Agent | Output File | Inputs | Focus |
|-------|-------------|--------|-------|
| Comparison Matrix | synthesis/comparison_matrix.md | All integration files | Stakeholder × argument × scenario matrix |
| Final Position Paper | synthesis/final_position_paper.md | comparison_matrix, all synthesis | Scenario-based position paper with SaaS share range estimates, conditions for each scenario, probability assessment, and experts sorted into each camp |

Final Position Paper Structure:
1. Executive Summary (SaaS share range estimate with confidence)
2. The Three Scenarios (Bull/Base/Bear with conditions and probabilities)
3. Evidence Assessment (strongest arguments for and against SaaS durability)
4. Stakeholder Consensus Map (who believes what and why)
5. Expert Voice Directory (named experts sorted by scenario camp)
6. The Category View (where SaaS is most/least durable)
7. The Timeline View (how the picture evolves year by year)
8. Strategic Implications (what C-suite should do under each scenario)
9. Conclusion and Confidence Assessment
