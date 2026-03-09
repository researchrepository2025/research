# Content Review: Wave 9, Part A (T01–T04)

**Reviewer:** Content Review Agent
**Date:** 2026-03-06
**Deliverable Context:** Scenario-based position paper (bull/base/bear) on SaaS durability as enterprise procurement method vs. agentic-build alternatives over 2–5 years.

---

### T01_saas_tco.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=3/5 | Citation Quality=4/5 | Scenario Utility=5/5

**Overall:** MINOR_ISSUES

**Summary:** Catalogs the full direct and indirect TCO architecture of enterprise SaaS, covering license fees, implementation, integration, training, administration, compliance, and vendor management. Constructs a composite TCO model showing 1.7x–3.6x multiple over headline license fees for a 5,000–10,000 employee enterprise. Frames waste (53% unused licenses, 40%+ shadow IT, 7.6 duplicate subscriptions) and vendor price inflation (11.4% vs. 2.7% CPI) as structural rather than correctable anomalies.

**Key Strengths:**
- Extremely high specificity throughout: named vendors (Salesforce, Adobe, Slack), named tools (Zylo, BetterCloud, Vertice), specific dollar figures, and specific percentages with dates
- Retains primary-level sourcing for major claims (Zylo 2025 SaaS Management Index, BetterCloud State of SaaS 2025, Training Industry Report 2025, IBM breach data)
- Composite TCO table in Section 8 is directly usable for scenario modeling — provides both low and high estimates with component-level breakdown
- The 385-hours-per-year contract management figure (Vertice, n=1,000 companies) is unusually concrete and independently verifiable
- Strong bear-scenario utility: SaaS price inflation at 4x–5x general CPI provides quantified economic pressure that directly supports the argument that SaaS cost structure is eroding its own durability
- Key Takeaways section is synthesis-ready; each bullet has numeric anchors

**Issues/Gaps:**
- Expert attribution is the weakest dimension. Named analyst or executive voices are almost entirely absent. Gartner is cited repeatedly but always second-hand (via GetMonetizely, SaaStr, GetKnit.dev) rather than from Gartner's own published reports. No CFO, CIO, or analyst is directly quoted with a named position on SaaS durability. This weakens the file's usability in the position paper's "named expert positions" requirement.
- The Forrester claim ("average mid-sized enterprise spends approximately $250,000 annually on SaaS customizations") is attributed via GetMonetizely citing Forrester — a tertiary chain. No Forrester report name or date is provided.
- SaaStr X/Twitter post (Slack price increase) as a citation (line 97-98) is low-quality; X posts are not Tier 1 or Tier 2 sources.
- "Intel Market Research" (iPaaS market projection) at line 188 appears to be a market research data aggregator, not Intel Corporation; the name is misleading and the source tier is unclear.
- GoWorkwize URL contains a typo ("on0boarding") visible in the source URL — flags a possible 404 risk.
- The composite TCO table note explicitly labels itself "illustrative composites," which is honest but means it cannot be cited as a primary empirical finding.

**Scenario Tagging:**
- **Bear scenario (build wins / SaaS erodes):** Primary utility. License waste ($21M average), 11.4% price inflation vs. 2.7% CPI, and 72% of Salesforce ARR growth coming from price increases rather than new customers all directly support the thesis that SaaS economics are deteriorating from the buyer's perspective. The vendor management burden (385 hours/year, 247 renewals/year) quantifies the hidden organizational cost of staying on SaaS.
- **Base scenario (hybrid):** Supports the cost-containment argument for retaining SaaS in categories where integration and compliance overhead would repeat under a build model.
- **Bull scenario:** Limited direct utility; the file is structurally a SaaS critique. Synthesizers should not draw bull-scenario support from this file without explicitly pairing it with T02/T03 counterweights.

---

### T02_custom_build_tco.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=4/5 | Citation Quality=4/5 | Scenario Utility=5/5

**Overall:** MINOR_ISSUES

**Summary:** Documents the full lifecycle cost structure of custom enterprise software, covering development costs under both traditional and agentic approaches, infrastructure, maintenance, talent, and the "hidden iceberg" of technical debt, security exposure, and opportunity cost. Constructs a 5-year illustrative TCO model showing $3.7M–$5.75M against a $500,000 initial build, representing 7.4x–11.5x the contract value. Critically examines where agentic coding reduces costs and where it does not.

**Key Strengths:**
- Best citation discipline of the four files: named primary sources include McKinsey/Oxford (two separate studies with distinct sample sizes: 5,400+ projects and 6,000+ projects), Standish Group CHAOS Report 2020, IBM Cost of a Data Breach Report 2025, Flexera 2025 State of the Cloud Report, Anthropic 2026 Agentic Coding Trends Report, METR July 2025 study, and Stack Overflow Developer Survey 2025. Most are Tier 1 or Tier 2.
- The METR study (line 89–92) is the highest-quality counterfactual evidence in all four files: a controlled study showing experienced developers took 19% longer with AI tools, vs. their 20% speed-up self-estimate. This is essential for balanced scenario analysis.
- Named expert voice: Pierre Yves Calloc'h, Builder at Pernod Ricard, provides a direct "no vibe-coding in enterprise" quote with attribution and source (Retool 2026 Build vs. Buy Report).
- FeatureBench benchmark (line 494: Claude 4.5 Opus at 74.4% SWE-bench but only 11.0% on complex feature tasks) is a specific, citable, falsifiable claim that constrains inflated agentic-capability narratives.
- The table in Section 8 (TCO Category vs. Agentic Impact vs. Remaining Risk) is ready to drop into a synthesis document.
- Honest labeling of unverified claims with [UNVERIFIED] flags aids reviewer trust.

**Issues/Gaps:**
- The McKinsey 20% maintenance benchmark (line 165–168) is attributed via WifaTalents citing McKinsey, not directly to a McKinsey report. The specific report name is absent; "McKinsey as cited by multiple industry sources" is not a verifiable chain.
- Sections 3 and 6 lean heavily on second-tier sources (Abbacus Technologies, Leobit, UnifiedInfotech, IdeaLink, Dockyard) for maintenance percentage ranges. While ranges are directionally consistent across sources, none of these are Tier 1/2 research organizations. This creates citation clustering risk if any source is challenged.
- The illustrative 5-year TCO model (Section 7) is explicitly labeled [UNVERIFIED] and carries no empirical grounding as a combined figure — appropriate caveat, but synthesizers must not treat the $3.7M–$5.75M total as a cited finding.
- Agentic-era project failure rate data is entirely absent. The Standish data used in Section 4 and Section 6 is from the 2020 CHAOS Report — pre-agentic-coding era. There is no data on whether failure rates have improved with AI-assisted development, which is a significant gap given the file's central argument about agentic tools changing the TCO stack.

**Scenario Tagging:**
- **Bear scenario (build wins):** Provides quantified cost compression evidence (50–90% initial development cost reduction) and real-world productivity data (TELUS 500,000 hours saved, Rakuten 79% time-to-market reduction, GoTo 30% developer time reduction).
- **Bull scenario (SaaS wins):** Strongest bear-on-build evidence available: METR study (19% slower with AI tools), FeatureBench (11% complex feature success rate), 15–18% more security vulnerabilities from AI-generated code, 4.6x PR review wait times without governance, 30%+ GenAI POC abandonment (Gartner). These are critical inputs to the bull scenario's "build is harder than it looks" argument.
- **Base scenario (hybrid):** The Section 8 table directly supports hybrid — agentic tools move the needle on initial development but leave the dominant cost categories (talent, infrastructure, security, technical debt) largely intact.

---

### T03_tco_comparison_by_category.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=2/5 | Citation Quality=3/5 | Scenario Utility=5/5

**Overall:** MINOR_ISSUES

**Summary:** Provides category-level TCO comparisons across CRM, ERP, HCM/HR, Security/Compliance, and Internal Tools, with specific pricing data for named platforms (Salesforce, Workday, SAP S/4HANA, Oracle Fusion, Microsoft Sentinel) and verdict tables. Concludes that ERP and security/compliance are firmly SaaS-category; internal tools have crossed a build break-even threshold; CRM is contested; HCM is trending toward hybrid.

**Key Strengths:**
- Category-level granularity is essential for scenario analysis — the paper cannot just make blanket claims about "SaaS vs. build"; it needs to differentiate by application type, and this file enables that
- Specific platform pricing data (Salesforce at $175/user/month, Oracle Fusion at $625/user/year with 20-user floor, Microsoft Sentinel at $35,700/month for 500GB/day) gives the synthesis document concrete anchors
- The Retool 2026 Build vs. Buy Report (n=817) is used extensively and cited with sample size, which is the correct citation practice; the BusinessWire press release is also cited as corroboration
- ERP failure rate data (55–75% failure rate, 215% average cost overrun in discrete manufacturing) is well-sourced and creates a compelling argument that SaaS ERP wins by default not on merit but on the absence of a viable alternative
- The insurance domain TCO comparison (sandis.io: custom build $3.375M vs. SaaS $1.02M over 5 years in compliance-heavy vertical) is the most direct apples-to-apples quantitative comparison in the file
- Category verdicts are editorially clear and synthesis-ready

**Issues/Gaps:**
- Expert attribution is the lowest-scoring dimension across the Wave 9A set. No named analyst, CIO, executive, or researcher is quoted with a stated position. The Retool data is survey-based but no individual spokesperson or analyst is named. This is a meaningful gap for the position paper's requirement for "named expert positions."
- Citation quality is mixed: sandis.io, americanchase.com, noeldcosta.com, godlan.com, kpcteam.com, and supportfinity.com are second-or-third-tier sources. These are used for material TCO claims that ideally would be backed by Tier 1 sources (Gartner, Forrester, IDC, direct vendor data, academic research). The Gartner ERP failure rate claim (line 102) is cited via Godlan.com, not from Gartner directly.
- The HCM custom build TCO is explicitly marked "[UNVERIFIED] — no primary study found for full custom HCM." This is an honest disclosure but leaves a gap in the verdict table that synthesizers must not paper over.
- The Forrester "67% of software projects fail because of wrong build vs. buy choices" claim (line 341) is attributed via maddevs.io citing Forrester — a tertiary citation chain with no report name or date.
- The AI agent build cost ranges (Azilen.com: simple chatbot <$50K, multi-agent orchestration $150K–$400K+) are sourced from an AI development consultancy with commercial interest in build projects. The Gartner "$750K–$1M for RAG systems" figure is also cited via Azilen rather than from Gartner directly.
- No mention of switching costs between SaaS vendors, which is relevant to the verdict in the CRM and HCM categories.

**Scenario Tagging:**
- **Bear scenario (build wins / SaaS erodes):** Section 5 (Internal Tools) is the clearest bear-scenario evidence: 35% replacement already underway, 78% planning more, 25% of frequent shadow builders are senior managers (signaling upstream budget reallocation). CRM section supports build-wins-at-scale argument.
- **Bull scenario (SaaS wins):** ERP verdict ("build is not a credible alternative") and Security/Compliance verdict ("most resistant to build") are strong bull-scenario anchors. The insurance domain comparison showing SaaS 70% cheaper over 5 years in compliance-heavy vertical is directly usable.
- **Base scenario (hybrid):** HCM verdict ("SaaS wins for full-stack; build wins for workflow layer") is the clearest articulation of the hybrid pattern in Wave 9A. The framing of "thinner SaaS core plus custom workflow layer" is synthesis-ready.

---

### T04_roic_analysis.md

**Scores:** Relevance=5/5 | Specificity=4/5 | Expert Attribution=3/5 | Citation Quality=3/5 | Scenario Utility=5/5

**Overall:** REWORK_NEEDED

**Summary:** Applies a formal ROIC framework to build-vs-buy decisions, covering breakeven analysis, time-to-value benchmarks, scale effects, competitive advantage premium, and risk-adjusted expected returns. Introduces a probability-weighted expected ROIC model showing ~15% expected return at base enterprise failure rates vs. ~96.5% with high-governance delivery, making organizational capability the decisive variable. Identifies specific conditions under which build generates superior risk-adjusted ROIC.

**Key Strengths:**
- The ROIC framework itself is the most analytically rigorous construct in Wave 9A; treating custom builds as capital deployment decisions (not just cost comparisons) is the correct framing for a C-suite position paper
- Risk-adjusted expected ROIC table (Section 6) is high-value for scenario analysis — the delta between 15% (base governance) and 96.5% (high governance) is the most important quantitative finding in the Wave for the position paper's bull/bear framing
- The breakeven inflation arithmetic (Section 2, $500K build eliminating $200K/year SaaS bill growing at 12% annually = $1.27M PV avoided costs over 5 years = 154% ROIC) is clearly flagged [UNVERIFIED] and demonstrates the analytical approach even where primary data is absent
- Conditions matrix (Section 7) is the most synthesis-ready table in Wave 9A; directly maps scenario conditions to ROIC confidence levels
- Named organization examples: Rakuten (79% time-to-market reduction), TELUS (500K hours saved, 13,000 custom AI solutions), with source (Anthropic 2026 Agentic Coding Trends Report)
- BCG study of 850 companies (35% of digital transformations reach stated goals) and Bain 2024 study (88% of transformations fail) are named primary sources for failure rate data

**Issues/Gaps — Citation Density (Primary Concern):**

The file was flagged for having only 54 inline citation URLs against a 60-URL threshold. Upon review, this count is accurate. The citation gaps cluster in the following areas:

1. **Section 5 (Competitive Advantage Premium):** The McKinsey "companies with custom-built digital systems outperform by 2.7x in innovation and 1.8x in efficiency" claim (line 215) is attributed to "McKinsey 2025, cited by multiple sources" with the URL pointing to Baytech Consulting's blog, not to a McKinsey report. No McKinsey report name, author, or URL is provided. This is a material citation failure for a quantitative claim of this specificity.

2. **Section 5:** The "organizations 2.5x more likely to outperform competitors" claim (line 221) is attributed to "Titani Solutions, citing McKinsey 2023 data" — again a secondary source citing McKinsey without a primary URL. Two major McKinsey claims in a row with no direct McKinsey sourcing is a pattern that undermines the section.

3. **Section 6 (Risk-Adjusted ROIC):** The high-governance probability table (40% full success, 45% partial, 15% cancellation) is explicitly marked [UNVERIFIED] with no source. This is the most consequential table in the file — it drives the 96.5% expected ROIC conclusion — and it has no empirical grounding. The McKinsey 5.3x success multiplier is used to derive these numbers but the derivation methodology is not shown, and the multiplier itself is cited via MeltingSpot citing McKinsey, not from a McKinsey report directly.

4. **Section 1 (Benchmark ROIC Ranges):** The CRM example showing 1,243% ROI and 249.8% IRR (Baytech Consulting, Bryan Reynolds, CEO) is sourced entirely from a single custom software vendor's blog. Baytech has a direct commercial interest in promoting high build-ROI figures. This source requires either corroboration from a neutral party or a conflict-of-interest disclosure in synthesis.

5. **Section 4 (Scale Effects):** The SaaS Pricing Benchmark Study 2025 (GetMonetizely, line 165) is cited for the $175/user/month benchmark used in the per-seat amortization calculation — the same figure already established in T03, but the GetMonetizely citation is a Tier 3 source for a calculation that drives the entire Section 4 analysis.

6. **Missing citations for forward projections:** The breakeven projection in Section 2 ($1.27M PV at 12% SaaS inflation) is documented as [UNVERIFIED]. The section should either be elevated with a citable projection model or explicitly scoped as an illustrative calculation in synthesis.

**Additional Issues Beyond Citation Density:**

- Expert attribution is limited. Bryan Reynolds (CEO, Baytech Consulting) is named in the source list but not quoted directly in the body. No named analyst from Gartner, Forrester, IDC, or a recognized neutral research firm is cited with a stated position on build ROIC. The "75% of IT decision-makers believe bespoke software leads to better business outcomes" TechRepublic survey is cited via Baytech — the original TechRepublic article is not directly referenced.
- The file relies heavily on Reproto Technologies (a custom software development firm) for time-to-value benchmarks and the change management multiplier data. Like Baytech, Reproto has a commercial interest in promoting build ROI. Two primary quantitative sources in this file have aligned commercial interests in overstating build returns.
- The Standish CHAOS data used in Section 4 and Section 6 is from the 2020 report and is cited via tigosolutions.com rather than from the Standish Group directly. The 9% large-company full success rate is a foundational number for the risk-adjusted model; it should have a primary-source citation.

**Scenario Tagging:**
- **Bear scenario (build wins):** Section 2 breakeven analysis (154% ROIC on $500K build replacing rising SaaS bill), Section 5 competitive advantage premium (1,243% ROI on custom CRM), and the conditions matrix (Section 7) where 5 of 8 conditions favor build with "High" confidence are strong bear-scenario inputs.
- **Bull scenario (SaaS wins):** Section 6 risk-adjusted model is the most powerful bull-scenario evidence: at base enterprise failure rates, expected build ROIC is only ~15%, making the known cost of SaaS preferable. The 9% large-company full success rate (Standish) is the single most effective counter to naive "build is now easy" arguments.
- **Base scenario (hybrid):** The conditions matrix (Section 7) is directly usable to define the hybrid scenario: build wins in revenue-critical, differentiated, 500+ user, governed organizations; SaaS wins in generic, low-user-count, governance-poor, rapidly-evolving domains.

---

## Wave 9A Summary

| File | Overall | Primary Issues |
|---|---|---|
| T01_saas_tco.md | MINOR_ISSUES | No named expert voices; Gartner cited third-hand; one suspicious URL (GoWorkwize typo); X/Twitter citation for Slack pricing |
| T02_custom_build_tco.md | MINOR_ISSUES | Standish data is pre-agentic (2020); maintenance % benchmarks from Tier 3 sources; McKinsey maintenance claim cited via WifaTalents |
| T03_tco_comparison_by_category.md | MINOR_ISSUES | Heavy Tier 3 sourcing for major TCO claims; no named experts; HCM custom build TCO unverified; Gartner ERP failure rate cited via Godlan |
| T04_roic_analysis.md | REWORK_NEEDED | Below citation density threshold (54 vs. 60 required); two McKinsey claims with no direct McKinsey source; high-governance ROIC table entirely unverified; primary quantitative sources (Baytech, Reproto) have commercial conflict of interest |

### Cross-File Observations

**1. Expert attribution is a systemic gap across all four files.** None of the files contain direct quotes from named Gartner, Forrester, or IDC analysts. No CIO, CFO, or named enterprise executive is quoted stating a position on SaaS durability or build-vs-buy strategy — which is a requirement for the final deliverable. Wave 9B or synthesis work will need to source named expert positions independently (e.g., Forrester VP-level analyst notes, Gartner Magic Quadrant commentary, named exec quotes from earnings calls or CIO forums).

**2. Gartner is cited pervasively but almost never from a primary Gartner source.** Across T01, T02, T03, and T04, Gartner is cited approximately 10 times. In the majority of instances the citation chain is Gartner → third-party blog → this file. The exceptions are: T01 (Gartner IT Spending Forecast, direct URL to gartner.com newsroom), T02 (Gartner GenAI POC abandonment, direct URL to gartner.com newsroom press release). All other Gartner citations should be upgraded to primary sources for synthesis.

**3. The Retool 2026 Build vs. Buy Report (n=817) is the most-cited primary survey across T03 and T04.** This is appropriate — it is a Tier 2 source with a clear methodology — but synthesizers should note the sample is biased toward Retool's customer base (enterprise builders and developers already using low-code/no-code tools). This population is more predisposed toward building than a random enterprise population, which inflates the "78% plan to build more" figure relative to a cross-industry survey. This bias should be disclosed in the position paper.

**4. T01 and T04 share several overlapping statistics (Salesforce price increases, SaaS inflation rates) without cross-referencing each other.** This is a documentation consistency issue, not a factual problem, but synthesis authors should reconcile the figures: T01 cites 11.4% SaaS price increase (SaaStr), T04 cites 12.2% (SoftwareSeni citing Vertice). These are from different methodologies covering slightly different time periods; synthesis should use the higher-quality primary source (Vertice SaaS Inflation Index, as cited in T04) and acknowledge the range.

**5. The agentic-coding productivity claim range is wide and inconsistently bounded.** Across the four files, development time compression is cited as: "50% reduction in human engineering effort" (Belitsoft, T02), "30% faster" (GoTo via Anthropic, T02), "30–79% faster" (Anthropic, T04), and "70–95% cost reduction" (Times of AI, T02). The METR study's contradictory finding (19% slower in controlled conditions) appears only in T02. For scenario analysis, the position paper must present this as a range with the METR result as the lower bound and the vendor-reported figures as the upper bound — not as a settled number.

**6. T04 requires focused rework before synthesis.** The two [UNVERIFIED] McKinsey competitive advantage claims and the unsupported high-governance probability table are load-bearing for the ROIC conclusions. If left as-is, they expose the position paper to challenge on its most analytically distinctive section. Recommended fix: either source direct McKinsey report URLs for those claims, replace with citable alternatives (Forrester TEI studies, IDC ROI surveys), or explicitly scope the high-governance table as a modeled scenario rather than an empirical finding.
