Here is the complete validation report.

---

**Validation Report: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/leaders/ai-market-leaders-2026.md`**

---

**COMPLETENESS**

No issues. All 23 segments are present, each with exactly 5 ranked companies (115 companies total). All 23 sections have a Market Size line, a Competitive Landscape paragraph, and at least one source URL. The three category blocks (Horizontal 4, Departmental 9, Vertical 10) with Menlo VC totals are all present.

---

**STACK RANKING ACCURACY**

1. **Ranks 5 and 6 are inverted.** Rank 5 (HR/HCM) shows $34.12B and Rank 6 (Manufacturing + Supply Chain) shows $34.18B (manufacturing alone, before adding the $9.94B supply chain component). On the stated figures, $34.18B > $34.12B, so Manufacturing + Supply Chain should rank above HR, not below it. The combined Manufacturing + Supply Chain figure ($34.18B + $9.94B = $44.12B) makes the inversion even more severe — that combined figure would rank it second behind Data Science.

2. **Ranks 12 and 13 ordering is questionable.** Rank 12 (IT Operations) = $11.16B. Rank 13 (Insurance) = $10.36–14.99B. The midpoint of the Insurance range is ~$12.68B, which exceeds IT Operations' $11.16B. The lower bound of Insurance ($10.36B) is also close enough to IT Ops that the ordering cannot be stated confidently. The ranking treats the lower bound as the canonical figure without documenting that choice.

3. **Ranks 21 and 22 ordering is questionable.** Rank 21 (Note-taking) = $3.5B. Rank 22 (Legal) = $3.11–4.02B. The Legal upper bound ($4.02B) exceeds Note-taking ($3.5B) and the ranges overlap. The ordering is unresolvable from the data as presented.

4. **Finance (Vertical) market size is a 2024 figure, not a 2025 estimate.** The ranking table header states "2025 estimates," but Section 20 explicitly labels its $38.36B figure as "(2024 base)." This makes the Rank 3 entry non-comparable to the rest of the table.

---

**URL INTEGRITY**

5. **Presentations source label is wrong in both the ranking table and Section 4.** The link text reads `[Research and Markets]` but the URL points to `globenewswire.com`, which is a press release hosting site, not the Research and Markets firm. The label should read something like `[Globe Newswire / Research and Markets]` consistent with how Globe Newswire links are labeled elsewhere in the document (e.g., Creators, Rank 20).

6. **OpenAI CNBC source URL is stale relative to the stated metric.** The CNBC URL slug is `openai-hits-10-billion-in-annualized-revenue` (a June 2025 article), but the key metric states `$20B+ ARR`. The article the link points to documents a $10B ARR milestone, not the $20B+ claim. The SaaStr URL similarly references `openai-crosses-12-billion-arr`, also below the $20B+ claim. Neither cited source supports the stated figure.

7. **Section 3 Note-taking market size projection has no source.** The market size line ends with `| Projected $15–34B by 2032–2035 at 25–35% CAGR` with no URL cited for this projection. Every other section cites a source for projection figures.

---

**DATA CONSISTENCY**

8. **Customer Success market size is labeled 2024 base in the section but implied to be 2025 in the ranking table.** The ranking table header says "2025 estimates." Section 8 explicitly says `$12.06B (2024 base)`. This is a year mismatch for that entry.

9. **Gong ARR is inconsistent across sections.** Section 3 (Note-taking, Rank 1) states `$300M+ ARR`. Section 9 (Sales, Rank 3) states `~$298M ARR (2024)`. These reference different time periods and different precision levels and should be reconciled to a single consistent figure.

10. **Salesforce Agentforce ARR figure differs between sections.** Section 2 (Agent Platforms, Rank 1) states `$500M+ ARR`. Section 8 (Customer Success, Rank 1) states `$500M ARR` (no plus sign). Minor but inconsistent.

11. **Agent Platforms Menlo VC enterprise spend math does not add up.** Section 2 states Agent Platforms represents `$750M (10% of horizontal AI)`. But 10% of the stated Menlo horizontal total ($8.4B) = $840M, not $750M. Conversely, $750M / $8.4B = 8.93%, not 10%. One of the three figures (the dollar amount, the percentage, or the total) is wrong.

12. **Section 12 (Finance + Operations) Workday source URL is a mismatched reference.** Row 3 cites Workday with a source URL pointing to `fortunebusinessinsights.com/industry-reports/human-capital-management-hcm-market-100240`, which is an HCM market report — the same HR source used in Section 10. There is no Finance/Operations-relevant source cited for Workday's appearance in that segment.

---

**DUPLICATES / CROSS-SEGMENT LISTINGS**

13. **Salesforce Agentforce appears as Rank 1 in both Section 2 (Agent Platforms) and Section 8 (Customer Success).** This is a legitimate cross-segment listing given the product spans both categories, but it warrants a note or disambiguation so readers understand it is the same product revenue being counted in two segments.

14. **ServiceNow appears in three segments:** Rank 2 in Section 2 (Agent Platforms), Rank 1 in Section 6 (IT Operations), and Rank 3 in Section 8 (Customer Success). Again cross-segment, not a same-section duplicate, but potentially inflating apparent coverage of the space.

15. **Workday appears in two segments:** Rank 1 in Section 10 (HR) and Rank 3 in Section 12 (Finance + Operations). Cross-segment, but Section 12's citation uses the HR-specific source URL (see Issue 12 above).

16. **Gong appears in two segments:** Rank 1 in Section 3 (Note-taking / AI Meeting Assistants) and Rank 3 in Section 9 (Sales). Gong's primary product category is revenue intelligence and sales conversation intelligence, not general-purpose note-taking. Ranking it #1 in Note-taking above Otter.ai and Fireflies.ai (which are purpose-built for meeting transcription) is a likely segment misclassification.

---

**SECTION NUMBERING vs. STACK RANKING ORDER**

17. **Section numbers do not match stack rank order, and this is undocumented.** The sections are organized by category group (Horizontal 1–4, Departmental 5–13, Vertical 14–23), not by market size rank. Data Science & ML Platforms is the #1 ranked segment by market size but is Section 11. Real Estate is Rank 2 but is Section 21. The document does not explain this numbering convention, which creates confusion when readers try to reconcile the ranking table against the section numbers.

---

**Summary counts:** 17 issues total — 4 stack ranking accuracy issues, 3 URL integrity issues, 5 data consistency issues, 4 duplicate/cross-segment issues, 1 numbering/documentation issue.