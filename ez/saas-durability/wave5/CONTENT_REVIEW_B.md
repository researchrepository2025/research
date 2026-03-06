# Content Quality Review — Wave 5 Research Files B
**Reviewer:** Content Quality Gate
**Date:** 2026-03-06
**Files Reviewed:** C05, C06, C07

---

## Review Criteria

1. Does the content stay within its stated scope boundary?
2. Are expert opinions attributed with names, titles, and affiliations?
3. Are claims supported with inline citations (not just listed in a sources section)?
4. Is the analysis balanced (not advocacy for one position)?
5. Are key findings substantive and specific (not vague platitudes)?

---

## C05: Gartner & Forrester on SaaS Durability in the AI Era

**File:** `/private/tmp/workspace/saas-durability/research/wave5/C05_gartner_forrester.md`
**Rating: PASS**

**Observations:**

1. Scope is cleanly maintained. The file covers only Gartner and Forrester outputs from 2025–2026, with no drift into IDC, McKinsey, or VC-adjacent sources. The one external citation (The Register, February 4, 2026) is used solely to carry a named Forrester analyst quote (Charles Betz, VP and Principal Analyst) and does not introduce out-of-scope analysis.

2. Attribution meets standard. Named experts include Anushree Verma (Sr Director Analyst, Gartner) and Charles Betz (VP and Principal Analyst, Forrester). The multi-author Forrester blog posts are cited with the full analyst roster including names, titles, and the publishing firm (e.g., Kate Leggett, Vice President Principal Analyst; Linda Ivy-Rosser, VP Research Director). Institutional Gartner forecasts without a named speaker are appropriately attributed to the press release rather than to a phantom individual.

3. Balance is adequate. The file presents Forrester's "$1 trillion market cap erased" and Gartner's "40%+ of agentic AI projects canceled" alongside SaaS spend growth projections ($318B to $576B, 15.2% enterprise software growth). The section "Analyst Positions vs. VC Narratives" explicitly frames divergence rather than advocacy. No single narrative is forwarded as correct.

4. One minor citation gap: The statistic sourced via `saastr.com` (Gartner 15.2% enterprise software growth, Section 3) is a secondary citation to a third-party blog rather than a direct Gartner URL. This is noted for synthesis but does not change the rating because the underlying claim is corroborated by Gartner's own forecasts cited elsewhere in the document and the SaaStr post is a well-known industry aggregator.

---

## C06: IDC & Other Analyst Firms — Enterprise SaaS Durability and AI's Impact on Software Spending

**File:** `/private/tmp/workspace/saas-durability/research/wave5/C06_idc_other_analysts.md`
**Rating: MINOR_ISSUES**

**Observations:**

1. Scope is mostly respected but two source categories are weak. Section 4 ("CB Insights and Market Intelligence Data") contains no actual CB Insights citations — the statistics are sourced from `ai2.work`, `Fortune Business Insights`, and `GlobeNewswire`, none of which are the CB Insights primary source that the section header implies. The section header misrepresents the sourcing and should either be renamed to reflect the actual sources or replaced with genuine CB Insights data. The scope declaration lists "CB Insights" as a named firm, so this gap is a credibility risk for synthesis.

2. Expert attribution is strong for VC-adjacent firms. Battery Ventures quotes carry individual names and titles (Michael Hoeksema, Sudhee Chilappagari, Jason Mendel, Dharmesh Thakker). IDC is attributed at the institutional and product level (Frank Della Rosa, Research VP, SaaS, Business Platforms, and Industry Cloud, IDC). The IDC section is the appropriate format for a firm that often publishes forecasts without individual bylines on press releases.

3. One statistic has a sourcing chain problem: "median revenue multiple for software firms dropped below 5 in early 2026" (Section 4) is attributed to "ai2.work analysis citing market data" — this is a secondary source for a specific, consequential metric. The underlying primary source (Bloomberg, S&P Capital IQ, or CB Insights) is not directly cited. For a C-suite research product, this specific number should trace to a primary market data source. This is the key issue requiring a note for synthesis.

4. Balance is good. The consensus/divergence section (Section 7) explicitly names the tension between IDC aggregate spend growth (16.5% CAGR) and public-market multiple compression below 5x, stating these are "not mutually exclusive." The file does not advocate for either the "SaaS is dying" or "SaaS is fine" framing.

---

## C07: Consulting Advisory Patterns — SaaS vs. Build

**File:** `/private/tmp/workspace/saas-durability/research/wave5/C07_consulting_advisory_patterns.md`
**Rating: PASS**

**Observations:**

1. Scope is correctly set and maintained. The file's stated scope — "advisory patterns and incentives across the consulting industry, not specific firm positions" — is observed throughout. The file covers structural patterns (CoE advisory, billable-hour arbitrage, conflicts of interest) rather than firm-specific strategy positions. The inclusion of Retool survey data in Sections 5 and the Key Takeaways is within scope as evidence of the build-vs-buy trend that consulting firms are responding to, though synthesis authors should note that Retool has an obvious commercial interest in "build" outcomes.

2. Attribution quality is the strongest of the three files. Named sources include Frank S. Scavo (Enterprise Spectator, with affiliation and date) for the conflicts-of-interest analysis; named Battery and Redpoint partners are carried forward from C06. EY dual-role conflict (advising both SaaS vendors and enterprise buyers) is documented with two distinct primary URLs rather than asserted without evidence.

3. The Retool data dependency is the principal limitation. Five of the seven Key Takeaway statistics trace to the same Retool 2026 Build vs. Buy Report. The survey population (n=817) skews toward builders — 64% senior managers and above — which the file does disclose. Synthesis should apply a sourcing concentration note; a single commercial vendor survey should not carry this much evidentiary weight in a C-suite research product without corroborating sources.

4. The Anthropic citation in Section 3 (the "2026 Agentic Coding Trends Report") introduces a potential conflict-of-interest issue that the file does not flag. Anthropic is a primary beneficiary of agentic coding adoption; citing its own trend report as evidence of agentic adoption patterns is circular for a research project on whether SaaS will be displaced by agentic coding. Synthesis should flag this and treat the Anthropic citation as directional only, not as independent evidence.

---

## Summary Table

| File | Rating | Primary Issue |
|------|--------|---------------|
| C05 — Gartner & Forrester | PASS | Minor: one Gartner stat sourced via SaaStr (secondary) |
| C06 — IDC & Other Analysts | MINOR_ISSUES | Section header "CB Insights" misrepresents actual sources; revenue multiple statistic lacks primary source |
| C07 — Consulting Advisory Patterns | PASS | Retool data overrepresented in Key Takeaways; Anthropic citation is not independent evidence |

---

## Synthesis Notes for Wave 5 Integration

- **C05** can be used as-is. The SaaStr secondary citation should be noted as "via SaaStr, citing Gartner" rather than attributed directly to Gartner in the synthesis document.
- **C06** requires the Section 4 header to be corrected from "CB Insights" to reflect actual sources before synthesis. The revenue multiple statistic (<5x) should carry a caveat that it traces to a secondary market commentary source, not a primary data provider. The underlying directional claim is consistent with corroborating market data elsewhere in the file.
- **C07** is usable with two synthesis caveats: (1) Retool survey data should be treated as operator-perspective evidence, not neutral market research; (2) the Anthropic 2026 Agentic Coding Trends Report should be cited as a primary-party perspective, not independent analyst research.
