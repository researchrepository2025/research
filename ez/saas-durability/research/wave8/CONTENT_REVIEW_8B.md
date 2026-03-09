# Content Review: Wave 8, Part B (A05–A08)

**Reviewer:** Content Review Agent
**Date:** 2026-03-06
**Project:** SaaS Durability in the Agentic Coding Era
**Deliverable Context:** Scenario-based position paper (bull/base/bear) estimating SaaS market share ranges, 2–5 year horizon

---

### A05_maintenance_evolution.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=4/5 | Citation Quality=4/5 | Scenario Utility=5/5

**Overall:** PASS

**Summary:** Examines whether agentic coding tools can actually maintain enterprise software over time — covering bug-fixing benchmarks, feature evolution benchmarks, technical debt accumulation, dependency management, comprehension debt, and lifecycle cost trajectories. The core argument is that benchmark capability on isolated tasks (76.8% on SWE-bench Verified) collapses dramatically in enterprise maintenance contexts (9.1% on SWE-Bench Pro commercial set; 21% on SWE-EVO long-horizon tasks), and that AI-generated code is accumulating technical debt faster than it is being resolved.

**Key Strengths:**
- Benchmark comparison table with five named benchmarks, specific scores per model, and clear explanations of what each benchmark tests — directly usable in scenario analysis
- GitClear's 211 million changed-line dataset is the strongest empirical data in the file: 4x code clone growth in 2024 and 60% drop in refactoring activity are striking, concrete, and well-sourced
- Ox Security "Army of Juniors" study provides a named primary source (Eyal Paz, VP of Research) with a structured anti-pattern table (10 patterns, prevalence rates)
- arXiv:2510.10165 is an academic primary source documenting the specific mechanism by which AI shifts work from generation to review burden on senior developers (19% drop in original code productivity)
- The "comprehension debt" framing from Allstacks is a distinct analytical construct that adds synthesis value beyond standard technical debt discussion
- Named practitioner quotes with institutional affiliations: Ana Bildea (InfoQ/AI), Vicki Abraham (Salesforce), Addy Osmani, Andrej Karpathy, Boris Cherny
- The 18-month cost curve from Codebridge is directly usable as a narrative device in the bear scenario

**Issues/Gaps:**
- Several statistics route through secondary aggregators: the "41% rise in bugs" figure cites index.dev, not the original study; the "$1.5 trillion in technical debt" figure cites DEV Community (paulthedev), a personal blog post — neither is Tier 1. These should be flagged as unverified if used in the paper
- Pixelmojo is cited multiple times for Gartner and Forrester predictions (40% AI project cancellations; 75% of tech leaders facing severe technical debt by 2026) but Pixelmojo is a secondary site. The Gartner figure has a direct press release URL in A06/A07; the Forrester figure should be verified at the primary source before use
- The "256 billion lines of AI code generated globally in 2024" and "41% of all new code is AI-generated" statistics (Pixelmojo) lack a traceable primary source and feel aggregated — use with caution in the paper
- Rakuten/vLLM case (12.5M line codebase in 7 hours) is cited through Augment Code's marketing blog rather than Rakuten directly — a vendor-interested source
- Section 2.2 (Andrej Karpathy's workflow shift to 80% agent coding) and Boris Cherny's claims are from a secondary analysis (Addy Osmani's substack) rather than primary statements

**Scenario Tagging:**

- **Bear (build struggles / SaaS wins):** Primary evidence file. The SWE-bench Pro commercial set score (9.1%), SWE-EVO performance (21%), 4x code clone growth, Codebridge 18-month cost curve, 4x maintenance cost by year two, and the comprehension debt framing all support the bear case that custom-built AI codebases degrade faster than SaaS alternatives maintained by specialized vendors.
- **Base (hybrid):** The Rakuten case and Karpathy/Cherny adoption data support a base case where agentic tools excel at well-scoped, greenfield work but struggle with enterprise-grade maintenance — pointing to selective build rather than wholesale SaaS replacement.
- **Bull (build wins):** The 76.8% SWE-bench Verified figure and falling dependency management costs provide the bull counterpoint, though A05 frames these as insufficient for the maintenance layer.

---

### A06_maturity_curve_projections.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=5/5 | Citation Quality=5/5 | Scenario Utility=5/5

**Overall:** PASS

**Summary:** Provides a year-by-year maturity projection for agentic coding capabilities through 2031, anchored to METR's task-horizon benchmark (doubling time of 88.6 days since 2024), probabilistic forecasts from named researchers (Jurkovic, Lifland, Kokotajlo), and analyst forecasts from Gartner, Deloitte, McKinsey, and Forrester. The file explicitly structures optimistic, pessimistic, and central scenario curves with probability estimates attached.

**Key Strengths:**
- METR task-horizon data is the single strongest empirical anchor in Wave 8B: primary source (metr.org), dated, with specific doubling times at three measurement windows (196.5 days overall, 130.8 days since 2023, 88.6 days since 2024) — directly converts to scenario timeline ranges
- Named forecasters with specific probability estimates and confidence intervals: Nikola Jurkovic (2027 median, 2025–2033 80% CI), Eli Lifland (2030 median, 2026–2050 CI), Daniel Kokotajlo (2029 updated), FutureSearch aggregate (2033, 80% CI 2027–2050) — this is the strongest expert attribution set across all four files
- Updated positions documented: Kokotajlo's median slipped from 2028 to 2029; Lifland's update to ~2032 — the temporal tracking of forecast drift is analytically valuable
- Gartner press release URLs are direct (not routed through secondary sites): both the "40% of enterprise apps feature AI agents by 2026" and "40% of agentic projects canceled by 2027" citations link to gartner.com/newsroom
- Milestone timeline table (Section 4.1) is immediately usable as the scenario backbone in the position paper
- METR RCT (July 2025, n=16, 246 issues) — a randomized controlled trial showing 19% productivity slowdown on large real-world codebases — is a gold-standard empirical data point that appears in both A06 and A07
- The agent reliability compound-step math (Marcus: 95% per-step = 36% 20-step completion) is a clean, replicable analytic frame
- Deloitte governance gap statistics (11% in production, 21% with mature governance) from a named primary source
- The Forrester SaaS growth projection ($318B → $512B → $576B, 2025–2029) is a direct base-case anchor for the position paper's market share range estimates

**Issues/Gaps:**
- The optimistic and pessimistic scenario summaries in Sections 5.1 and 5.2 explicitly mark synthesized timeline points as "[UNVERIFIED — synthesized from trajectory data, not a named source]" — this is transparent and appropriate, but the paper's authors should treat these bullet points as interpretive scaffolding, not citable data
- Demis Hassabis quote ("A year from now, we will have agents...") is cited through dev.to (community post), not the original Axios interview — should be sourced to the Axios primary if used in the paper
- Andrej Karpathy quotes appear across A05, A06, and potentially other waves — the paper should consolidate these rather than repeating them
- The McKinsey base-case anchor (Section 5.3: 23% scaling agentic AI) is from November 2025 and may be the most recent available, but a March 2026 update would strengthen this anchor if available
- One URL inconsistency: the ISACA source appears twice with slightly different URL suffixes (`.../agentic-ai-workflows` vs. `.../agentic-ai-workshops`) — minor but should be checked

**Scenario Tagging:**

- **Bull (build wins):** METR accelerated doubling rate (88.6 days) projects 8-hour autonomous tasks by 2027; AI 2027 optimistic scenario (50% chance superhuman coder by end-2027); Gartner 40% enterprise app AI agent adoption; Anthropic report (30–79% faster dev cycles at Salesforce, TELUS 500K hours saved)
- **Base (hybrid):** METR historical rate projects 8-hour tasks by 2028–2029; Kokotajlo/Lifland central estimates at 2029–2032; McKinsey 23% scaling; Forrester SaaS growth trajectory continuing through 2029
- **Bear (SaaS wins):** Gartner 40%+ project cancellations by 2027; METR RCT productivity slowdown; 36% compound step reliability floor; FutureSearch 2033 aggregate; Deloitte governance gap (only 11% in production); Gary Marcus reliability math; Yann LeCun and Ilya Sutskever skeptic positions

---

### A07_integration_complexity.md

**Scores:** Relevance=5/5 | Specificity=5/5 | Expert Attribution=4/5 | Citation Quality=4/5 | Scenario Utility=5/5

**Overall:** PASS

**Summary:** Examines why enterprise integration is the most durable structural barrier to replacing SaaS via custom builds — covering API performance cliffs (FeatureBench: 74% → 5.2–12.5%), data pipeline automation limits, multi-system orchestration gaps, identity/auth architecture mismatch (NHIs outnumber humans 82:1), real-time synchronization requirements, and the comparison between agentic coding and pre-built iPaaS connector libraries.

**Key Strengths:**
- FeatureBench (arXiv:2602.10975v1, February 2026) is the most directly relevant benchmark in Wave 8B: it measures complex, multi-file feature development (790 LOC avg, 29 functions, 15 files) and shows top models resolving only 5.2–12.5% of tasks — a dramatic cliff from SWE-bench's 74%
- FeatureBench task parameter comparison table (790 vs. 32 LOC; 62.7 vs. 9.1 test points; 15.7 vs. 1.7 files) provides a concrete, quotable illustration of the benchmark-to-production gap
- The non-human identity (NHI) data is unique and powerful: 82:1 NHI-to-human ratio (Rubrik Zero Labs/WEF), 75% of AI platform connections still using static API keys (Okta), only 10% of organizations with an NHI governance strategy (Okta) — all from named, Tier 1 sources
- iPaaS competitive landscape table (Boomi 2,000+, Workato 1,000+, MuleSoft unlimited) with Forrester confirmation that all three announced agent-building capabilities in 2025 — supports the "iPaaS absorbs agentic" narrative rather than displacement
- SAP Joule Studio GA (December 2025) is a named, dated product event that signals SaaS vendor defensive response
- IBM and Bain named-executive quotes (Maryam Ashoori, Vyoma Gajjar, Chris Hay) provide institutional attribution that is stronger than anonymous "industry experts say"
- The Deloitte "60% cite legacy integration as primary challenge" and "35% as most significant barrier to scaling" are high-quality, titled-survey statistics
- Capability summary table at the end is directly usable as a structured evidence exhibit in the position paper

**Issues/Gaps:**
- FeatureBench score discrepancy: the executive summary cites "11%" for complex multi-file tasks, but Section 1.2 cites "5.2% on the shared repository subset" and "12.5% on the full benchmark" — these reflect different subsets of the same benchmark and should be clearly distinguished in the paper (the 5.2% is specifically the "shared repository" subset where collaborative context is absent)
- The "65–86% time savings" from Stanford HAI and MIT CSAIL (Section 6.4) is cited through blog.arcade.dev, not directly — the primary study citations should be verified; arcade.dev is a vendor with interests in positive AI adoption data
- Gartner's "1,445% surge in multi-agent system inquiries" (Section 3.1) is cited through joget.com, not directly from Gartner; this secondary-site citation should be flagged
- The "40% faster pipeline development" average (Tredence, Section 2.1) comes from Tredence's own blog — a consulting firm with commercial interest in positive AI adoption metrics; should be noted as vendor-sourced
- The integration cost baselines ($3.5M average, $4.7M anecdotal) in Section 6.1 cite appseconnect.com — an iPaaS vendor — which is a conflicted source for integration cost estimates; the range is plausible but should be corroborated with a neutral source
- Several MCP facts (Section 4) route through a personal blog (guptadeepak.com) rather than primary sources; MCP download figures and connector counts should be verified against Anthropic's primary communications

**Scenario Tagging:**

- **Bear (SaaS wins):** FeatureBench cliff (5–12% on complex tasks), NHI identity crisis (75% static keys, 10% governance), 60% citing legacy integration as primary barrier, Gartner 40% project cancellation, IBM and Bain quotes on enterprise unreadiness, polling/batch ETL mismatch for real-time data
- **Base (hybrid):** Greenfield REST API integration showing "strong" performance; iPaaS vendors absorbing agentic orchestration (not being replaced); MCP spec maturation; SAP and MuleSoft building agent layers — hybrid of SaaS+agents vs. custom replacement
- **Bull (build wins):** Prophecy/Tredence pipeline acceleration data; Stanford HAI/MIT CSAIL 65–86% time savings on well-defined tasks; MCP growth (100K to 8M downloads in 5 months)

---

### A08_last_mile_problem.md

**Scores:** Relevance=5/5 | Specificity=4/5 | Expert Attribution=3/5 | Citation Quality=3/5 | Scenario Utility=5/5

**Overall:** MINOR_ISSUES

**Summary:** Catalogs the post-code-generation costs of custom enterprise software — user adoption failure rates, UI/UX quality gaps, training costs, change management friction, documentation maintenance, and help desk burden. The central argument is that lowering the cost of generating code does not lower the adoption and operational costs that follow, and that these costs are systematically underestimated in build-vs-buy analyses.

**Key Strengths:**
- The MIT NANDA study (150 interviews, 350 employee surveys, 300 AI deployments, Fortune/August 2025) is a strong independent research source with a direct, usable comparative finding: 67% success rate for vendor purchases vs. 33% for custom builds — this is the single most important data point in the file for the position paper
- Feature utilization table (Section 7) aggregates four named sources — Standish Group, Pendo 2019, Gartner 2024, and a Pendo analysis — providing convergent evidence that 64–80% of software features go unused regardless of whether AI built them
- David Hsu (CEO, Retool) quotes via Newsweek provide named executive evidence with institutional credibility, and the 35% SaaS replacement / 78% expecting to build more statistic from the Retool survey is directly useful for the bear and base scenarios
- Deloitte's "five years or more" timeline for full enterprise app replacement is a headline-ready quote from a named Tier 1 analyst firm
- Ivanti 2025 Digital Employee Experience Report provides consistent, granular quantification of support burden ($4M productivity loss, 3.6 interruptions/month, 49% self-help preference)
- McKinsey change management data (48% more adoption with training, 5.3x success with cultural investment) from a named primary source
- The "60% of builders outside IT oversight" statistic (Retool survey) is a specifically relevant fact for a scenario analysis about whether custom builds actually get managed after deployment

**Issues/Gaps:**
- Heavy concentration on a single secondary source: Meltingspot's "Digital Transformation Failure Rate" blog post is cited for at least 9 separate statistics in Sections 1 and 4 (70% failure rate, 87.5% average, 70–95% range, $2.3 trillion cost, Bain 88%, 45% inadequate training, 63% stopping use, 70% can't track usage, 40% resentment, 69% negative experience, 60% resistance, 60% outdated change management). This is a single blog aggregator, not a primary study — the paper should not treat these as independent data points. The Bain 88% figure should be verified directly; the Gartner 67% unused features figure cited in Section 7 has a better trail (via userlane.com citing Gartner 2024)
- Expert attribution is the weakest dimension of this file. The Nielsen Norman Group, McKinsey, IBM, Deloitte, and Bain are named institutional sources, but there are no named individual researchers, analysts, or executives quoted with titles beyond David Hsu (Retool). The UX/NNGroup citations lack named authors. The Prosci data is not attributed to a named researcher
- The Nielsen Norman Group citations (Sections 2) are solid institutional sources but the quotes used are somewhat generic ("AI prototyping tools follow general directions but lack the judgment...") rather than specific to the enterprise custom-build problem; the connection to SaaS durability is inferential rather than direct
- The help desk market sizing from Data Insights Market ($15B → $40B, Section 6) is from a market research firm with no named methodology and should be treated as directional only
- The IDC "30-50% support ticket reduction" figure (Section 6) is from a 2023 IDC report cited through Userlane (a digital adoption platform vendor) — a dated and vendor-interested secondary citation
- The Pendo 2019 Feature Adoption Report (Section 7) is from 2019 — now 7 years old. While the structural pattern likely persists, any position paper should acknowledge the pre-agentic vintage of this data point
- No academic or peer-reviewed sources in this file — all citations are practitioner reports, surveys, or blog aggregators

**Scenario Tagging:**

- **Bear (SaaS wins):** Primary evidence file for this scenario. MIT NANDA 33% vs. 67% build vs. buy success rate; 64–80% unused feature rates (Standish, Pendo, Gartner); $1,000–$2,500 per-user training cost with no vendor subsidy; Deloitte "five years or more" for full enterprise app replacement; 87.5% digital transformation failure rate; shadow IT as signal of custom build adoption failure
- **Base (hybrid):** David Hsu (Retool) quote — "nobody's ripping out Salesforce wholesale...replacing the specific piece that never quite fit" — is the clearest articulation of the base/hybrid scenario in Wave 8B; 35% SaaS replacement for specific functionality (not wholesale) supports selective build
- **Bull (build wins):** The 78% expecting to build more and David Hsu quote on collapsed build cost ("working prototype in a day or two") provide the bull case framing, though the surrounding evidence strongly undercuts it

---

## Wave 8B Summary

| File | Overall | Primary Scenario | Critical Data Points |
|---|---|---|---|
| A05_maintenance_evolution | PASS | Bear/Base | SWE-bench Pro commercial 9.1%; SWE-EVO 21%; GitClear 4x code clone growth; comprehension debt framing; 4x maintenance cost by year 2 |
| A06_maturity_curve_projections | PASS | All Three (Scenario Backbone) | METR TH doubling times (88.6d since 2024); Jurkovic/Lifland/Kokotajlo probabilistic forecasts; Gartner cancellation + adoption stats; Forrester SaaS growth trajectory |
| A07_integration_complexity | PASS | Bear/Base | FeatureBench 5–12% cliff; 82:1 NHI ratio; 75% static API keys; iPaaS not being replaced; Deloitte 60% legacy integration barrier |
| A08_last_mile_problem | MINOR_ISSUES | Bear | MIT NANDA 33% vs. 67% build/buy success; Retool "nobody's ripping out Salesforce"; Standish/Pendo/Gartner 64–80% unused features; Deloitte "five years or more" |

### Files Requiring Remediation Before Synthesis

**A08 (MINOR_ISSUES):** The Meltingspot aggregation problem is the primary concern. Before the paper's synthesis phase, the researcher should verify at least the Bain 88% figure, the Gartner 67% unused features figure, and the $2.3 trillion cost figure against their primary sources. If primaries cannot be confirmed, these statistics should be cited as "Meltingspot (2025) citing [source]" with a caveat, rather than as independent data points. The lack of named individual experts in A08 is also noticeable given the strength of expert attribution in A06 — consider pulling a direct Deloitte or McKinsey analyst name from the cited reports to improve credibility.

### Cross-File Observations

1. **METR data appears in both A05 and A06** (RCT slowdown study, July 2025) and should be cited once in the paper with cross-references rather than reprinted.

2. **Gartner's dual prediction** (40% of enterprise apps will feature AI agents by 2026 AND 40% of agentic projects will be canceled by 2027) appears in A06, A07, and A08. This pairing is analytically significant — rapid adoption followed by a near-certain correction wave — and should be presented as a single exhibit in the position paper rather than distributed across sections.

3. **The bear case has the strongest evidentiary density across these four files.** A05 (maintenance failure), A07 (integration barriers), and A08 (adoption/last-mile failure) all build the same argument from three independent angles: AI code degrades faster than SaaS (A05), can't integrate at enterprise scale even if generated (A07), and wouldn't get adopted even if deployed (A08). The bull case is primarily concentrated in A06's METR projections and adoption velocity metrics.

4. **The base/hybrid scenario is implicitly supported by A08's Retool data** ("replacing the specific piece that never quite fit") and A07's iPaaS expansion narrative (SaaS vendors absorbing agentic capabilities). The paper should make this explicit: the base scenario is selective displacement of SaaS edge functions via custom build, not wholesale replacement.

5. **Citation quality divergence:** A06 is the strongest file on citation quality (direct Gartner/Deloitte/METR primary URLs, academic arXiv sources, named forecasters with quantified probabilities). A08 is the weakest (heavy Meltingspot aggregation, 2019 Pendo data, vendor-interested sources). Synthesis should weight A06 data more heavily for quantitative claims and use A08 primarily for qualitative framing and structural patterns.

6. **No file directly addresses the enterprise procurement decision process** — specifically, who decides to build vs. buy and on what criteria. This may be covered in other waves, but it is a gap in Wave 8B taken in isolation. The position paper should either source this from elsewhere in the research corpus or acknowledge it as a gap.
