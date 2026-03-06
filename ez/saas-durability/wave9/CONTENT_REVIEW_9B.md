# Content Review: Wave 9, Part B (T05–T07)

**Reviewer:** Content Review Agent
**Date:** 2026-03-06
**Research Project:** Will SaaS remain the dominant enterprise procurement method vs. build for AI-driven applications in 2-5 years?

---

### T05_hidden_costs_build.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=2/5 | Citation Quality=4/5 | Scenario Utility=4/5

**Overall:** MINOR_ISSUES

**Summary:** T05 catalogs six categories of post-launch operational costs that agentic coding tools do not eliminate: security (vulnerability management, pentesting, breach response), compliance certification maintenance (SOC 2, FedRAMP, HIPAA), feature parity erosion, reliability engineering (SRE headcount, on-call burden, DR), documentation and knowledge management, and technical debt. The file's central argument is that agentic coding compresses build cost but leaves the 60/60 rule — 60% of lifecycle cost in maintenance, 60% of engineering time consumed by it — structurally intact. It concludes with a synthesized aggregate cost floor of $608,000–$950,000 annually for a mid-size enterprise running one custom-built application with SOC 2 and FedRAMP Moderate requirements.

**Key Strengths:**
- Exceptionally specific dollar figures across all six cost categories, with named tools (Qualys VMDR at $199–$250/asset/year, Rapid7 InsightVM at $23/asset/year), named frameworks (FedRAMP Moderate at $75K–$200K/year, FedRAMP High at $100K–$300K/year), and named salary benchmarks (ZipRecruiter enterprise software engineer data)
- IBM Cost of a Data Breach 2025 is a Tier 1 primary source; Vanta, Secureframe, Paramify, and Forrester references are credible Tier 2 sources
- The aggregate cost floor table at the end is directly synthesis-ready for a position paper — it creates a single quantitative anchor for the bear/base build cost case
- The MIT Technology Review citation on API economy governance is a meaningful Tier 1 source
- The Forrester knowledge management reference adds institutional credibility to the documentation section
- AI-specific angle on knowledge debt (agentic code generated faster than institutional context can be documented) is a differentiated and well-supported insight

**Issues/Gaps:**
- Expert attribution is weak throughout. The Constellation Research quote is attributed generically; the Canny Blog quote is not attributed to a named person. No named CIO, CTO, CFO, or named analyst is quoted by name. The Forrester reference is a blog post with no named analyst attached. For a C-suite position paper, the absence of named expert voices is a synthesis gap.
- The "ADEVS Tech Journal" citation (the 60/60 rule source) is a Medium post by a company called ADEVS Inc. This is not a Tier 1 or Tier 2 source and is the load-bearing citation for the document's core thesis. This needs to be supplemented or replaced with a primary source (e.g., a Standish Group, Gartner, or peer-reviewed reference for the maintenance cost ratio claim).
- Two data breach statistics within the same IBM report appear to contradict each other: one states the average U.S. breach cost jumped 9% to $10.22M; another states the global average fell 9% from $4.88M to $4.44M. This is likely the U.S. vs. global distinction, but the file presents both without resolving the apparent conflict — a synthesis author could inadvertently misuse them.
- The thewitslab.com citation for the Forrester TEI "78% of lifetime TCO accrues after launch" claim is a secondary blog citing Forrester, not a direct Forrester link. This should be flagged as a secondary source.
- No named SaaS vendor is compared as a counterpoint — the file argues the build case entirely, which is appropriate for its scope, but synthesizers should note it provides no bull-for-SaaS evidence.

**Scenario Tagging:**
- **Bull (SaaS wins) / Bear (build loses):** Strong evidence. The aggregate $608K–$950K annual floor for a single custom application makes the "SaaS is cheaper when hidden costs are counted" argument concrete and usable.
- **Base (hybrid):** Provides the cost categories that define where hybrid makes sense — specifically, organizations that can amortize FedRAMP/SOC 2 costs across multiple systems or already have SRE teams in place.
- **Bear (build wins):** Does not directly support the build-wins case; all evidence points to build costs being underestimated.

---

### T06_hidden_costs_saas.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=4/5 | Citation Quality=4/5 | Scenario Utility=5/5

**Overall:** MINOR_ISSUES

**Summary:** T06 catalogs six categories of hidden SaaS costs that shift the build-vs-buy calculus toward build: vendor lock-in and switching costs, data portability and extraction costs, customization ceiling workarounds, the SaaS tax on unused licenses, vendor pricing power at renewal, and strategic dependency on vendor roadmaps. The file is anchored by Zylo's 2025 dataset (40M+ licenses, $40B in spend), Vertice's SaaS Inflation Index (12.2% annual inflation, 4.5x CPI), and the Retool 2026 survey documenting that 35% of enterprises have already replaced at least one SaaS tool with a custom build.

**Key Strengths:**
- Named executives with specific quotes: David Hsu (CEO, Retool) cited directly in Newsweek with a clear attributed statement; Forrester's "SaaS as we know it is dead" declaration is a high-signal named-firm position
- Retool survey (n=817, named methodology, February 2026) is the strongest empirical anchor in any Wave 9B file — directly useful in all three scenarios
- Specific vendor price increase table (Adobe +50%, Slack +20%, Zendesk +15%, Salesforce +6%) is highly usable in the position paper's bear-for-SaaS/bull-for-build case
- SaaStr's Salesforce analysis — 72% of 2025 ARR growth coming from price increases rather than new customers — is a pointed, calculation-based data point that goes beyond headline statistics
- UpperEdge's contractual cumulative price reset analysis (3% x 3-year term = 9% cap applied as a lump) is specific, named, and practically relevant to enterprise procurement
- Zylo data is drawn from a dataset ($40B in spend, 40M+ licenses) that lends statistical credibility above typical vendor surveys
- The EU Data Act regulatory note is appropriately scoped with the caveat that it applies only to EU operations

**Issues/Gaps:**
- The Forrester "pendulum is swinging toward Build" quote is attributed to "Forrester, cited in multiple sources" and links to a 2025 predictions blog — the underlying named analyst is not identified, which weakens the attribution for the position paper
- The Tech Buzz AI citation (SAP -16%, ServiceNow -11% stock drops) links to techbuzz.ai, which is a Tier 3 source. The same data should be retrievable from Reuters, Bloomberg, or Financial Times; the current citation is adequate for context but not for a position paper's primary evidence
- The AI SaaS Writer citation ("aisaaswriter.com") is also a Tier 3 source and should be treated as filler rather than evidence
- The "SaaS as we know it is dead" Forrester quote is correctly attributed but the blog post format means the underlying Forrester research document is not directly accessible — the link appears to be a Forrester blog rather than a published report, which is a citation quality concern for a position paper
- The Binadox source ($1.2M migration wave cost) is a vendor blog, which is Tier 2 at best. This is the primary anchor for data migration costs and should ideally be corroborated by a Gartner or Forrester figure

**Scenario Tagging:**
- **Bear (build wins):** Primary evidence file for this scenario. Provides the cost structure that makes building look attractive: $21M average waste, 12.2% SaaS inflation, 72% of Salesforce growth from pricing not expansion, $1.2M migration exit cost.
- **Base (hybrid):** The EU Data Act section and the customization ceiling analysis support a "build what you customize most, buy what you use at standard" hybrid framework.
- **Bull (SaaS wins):** This file provides no evidence for the bull case. Its inclusion in synthesis requires the counterbalancing material from T05 to avoid one-sidedness.

---

### T07_economic_breakeven_scenarios.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=5/5 | Citation Quality=5/5 | Scenario Utility=5/5

**Overall:** PASS

**Summary:** T07 is the quantitative framework file for the position paper. It constructs a three-scenario (bear/base/bull) break-even model for build vs. buy under agentic coding capability assumptions, grounded in the Xenoss enterprise AI TCO matrix, VRInSofts five-year cost calculator, and Retool's 2026 enterprise survey. It adds scenario-specific market share erosion estimates (bear: 5–10% SaaS point-product erosion by 2030; base: 25–35%; bull: 50–65%), maps each scenario to named frameworks from Bain, ThoughtLinks, McKinsey, and Edelweiss Capital, and includes a sensitivity analysis ranking the variables that most move the break-even point.

**Key Strengths:**
- The richest named-expert attribution of all three files: Javier Pérez (Edelweiss Capital) with specific probability weights per scenario; Sumeet Chabria (ThoughtLinks, named CEO and Founder) with a March 3, 2026 framework; McKinsey with direct quotes and linked reports; Bain with a named 2025 Technology Report; Deloitte with specific 2030 forecasts; Gartner with named press releases and exact dates
- The comparative scenario summary table (Section 6) is immediately position-paper-ready — it presents bear/base/bull side-by-side on eight quantitative dimensions with analyst framework anchors
- Sensitivity analysis (Section 7) adds analytical depth not present in most competitor intelligence files: correctly identifies annual maintenance cost rate as the highest-leverage variable and explicitly argues against the common assumption that initial build cost is the dominant driver
- Gartner citations link to official press releases with exact dates (July 29, 2024; August 26, 2025), which is the correct Tier 1 citation standard
- Belitsoft's conservative counterpoint (90% code cost drop = only 10% total savings when governance is included) is a critical nuance that prevents the bull scenario from being overstated
- The Pierre Yves Calloc'h (Pernod Ricard) direct quote adds a named practitioner voice from a real enterprise deployment context
- TELUS 13,000 custom AI solutions / 500,000 hours saved is a named enterprise data point, not a generalization
- The Anthropic 2026 Agentic Coding Trends Report usage metrics (human interventions per session declining from 5.4 to 3.3; session duration at 99.9th percentile nearly doubling) are specific and time-stamped

**Issues/Gaps:**
- VRInSofts is a software development vendor, not an independent analyst firm. Multiple key statistics (the "72% premium" for SaaS over five years, the "33-month mid-market break-even") originate from this single vendor-produced source. The analysis would be strengthened if any of these numbers were corroborated by a Gartner, Forrester, or IDC benchmark.
- The duvo.ai source ("80% reduction in maintenance burden vs. traditional RPA") is a vendor blog, and the 80% and 57% figures appear without clear primary research methodology. These numbers are high-impact in the model but are Tier 3 sourced.
- The Morgan Stanley software loan data (50% rated B- or lower; $235B market) is cited via ThoughtLinks rather than directly from Morgan Stanley, making it a secondary citation. For a position paper using this in capital markets context, a direct MS source would be preferable.
- The market stress section (Bloomberg $285B rout, Reuters $2T S&P index decline) is also sourced via ThoughtLinks rather than the original outlets — same secondary citation concern.
- No file in Wave 9B covers the SaaS bull case explicitly (why SaaS will retain dominance despite these pressures). T07 addresses it by mapping the bear scenario to the Bain "Core Strongholds" quadrant, but the position paper will need Wave 9 or other wave content to build out the bull-for-SaaS argument independently.

**Scenario Tagging:**
- **Bull (SaaS wins):** Bear scenario section (Section 3) provides the SaaS-wins case: 2.5–4 year break-even unchanged, Gartner 30% POC abandonment, Deloitte "5+ years required" for substantial replacement, Edelweiss 30–40% probability for "AI Enhances SaaS"
- **Base (hybrid):** Section 4 is the primary base-case evidence: 18–30 month break-even for commodity workflows, 30–48 months for complex systems, Deloitte 35% point-product displacement by 2030, Retool 35% already replacing one SaaS tool
- **Bear (build wins):** Section 5 provides the bull-for-build case: immediate to 12-month break-even, $50K–$200K effective build cost falling below annual SaaS subscriptions, 50–65% SaaS point-product erosion by 2030

---

## Wave 9B Summary

| File | Overall | Primary Scenario Support |
|---|---|---|
| T05_hidden_costs_build.md | MINOR_ISSUES | Bull-for-SaaS / Bear-for-build hidden cost evidence |
| T06_hidden_costs_saas.md | MINOR_ISSUES | Bear-for-build primary evidence file |
| T07_economic_breakeven_scenarios.md | PASS | All three scenarios; quantitative framework |

### Cross-File Observations

**Complementarity is strong.** T05 and T06 are intentionally symmetric — T05 argues build costs are underestimated, T06 argues SaaS costs are underestimated. T07 synthesizes both into scenario-specific break-even ranges. Together they form a coherent economic argument that neither pure-SaaS nor pure-build is the rational default — which supports the base/hybrid scenario as the synthesis position.

**The Retool 2026 survey (n=817) appears in both T06 and T07** with consistent figures (35% replaced, 78% plan to build more). This is the single most cited empirical anchor in Wave 9B and should be prominently positioned in the position paper. Synthesizers should verify the Retool blog URL (retool.com/blog/ai-build-vs-buy-report-2026) matches the BusinessWire press release URL cited in T07 — both are listed as sources and should cross-reference correctly.

**Named expert attribution is uneven.** T07 has excellent named-expert density (Pérez, Chabria, Calloc'h, plus named firm reports from Bain, McKinsey, Deloitte, Gartner). T06 has adequate attribution (David Hsu/Retool CEO; Forrester firm-level). T05 is the weakest — no named individual analyst or executive is quoted, which will create an asymmetry in the position paper if T05 evidence is used without supplementation.

**Tier 3 source concentration in specific claims:**
- T05: The ADEVS/Medium citation for the 60/60 rule is the highest-risk citation in all three files — it is the load-bearing source for the document's thesis and is a company blog post.
- T06: Tech Buzz AI and AI SaaS Writer citations should be treated as supporting color, not primary evidence.
- T07: VRInSofts vendor-sourced break-even numbers and duvo.ai maintenance reduction claims need Tier 1/2 corroboration before being cited in the final position paper.

**No file addresses the SaaS bull case from the SaaS incumbent perspective.** The strongest evidence for SaaS durability — network effects, multi-tenant R&D amortization, compliance certification amortization, and ecosystem integration depth — is present implicitly in T05 and T07 but is not assembled as a standalone bull-for-SaaS argument. If a dedicated bull-for-SaaS file does not exist elsewhere in the research corpus, Wave 9B is structurally incomplete for writing a balanced three-scenario paper.

**Market share ranges are now available for all three scenarios** (T07 Section 6): bear 5–10% erosion, base 25–35% erosion, bull 50–65% erosion of SaaS point-product market by 2030. These are model-derived, not analyst-consensus figures, and should be labeled accordingly in the position paper. They are corroborated at the directional level by Deloitte (35% by 2030) and Edelweiss Capital (scenario probability weights), which is adequate for scenario framing but not for a hard market share forecast.
