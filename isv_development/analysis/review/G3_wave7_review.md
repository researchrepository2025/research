# G3: Wave 7 Synthesis Layer 1 — Quality Review

**Reviewer:** G3 Quality Reviewer
**Date:** 2026-02-19
**Files Reviewed:** SL1a (Phase 1 Consolidated), SL1b (Phase 2 Consolidated), SL1c (Phase 3 Consolidated)
**Ratings Source:** `analysis/three_phase_on_prem_ratings.md`
**Scope:** Synthesis quality, internal consistency, completeness, citation integrity, actionability, and spot-check verification across all three per-phase consolidation files

---

## SL1a: SL1a_phase1_consolidated.md

- **Score:** PASS
- **Synthesis quality:** Excellent. SL1a correctly consolidates findings from 11 source reviews (RP1a, RP1b, RP1c, RP1d, RP1e, RP2a, RP2b, RP3a, RP3b, RP4a, CC1) into a coherent Phase 1 narrative. The single recommended rating change (S1 Phase 1 RD 1 to 2) is accurately traced to RP4a with the three-part rationale (authentication re-implementation, Bedrock schema delta, error handling rewrite) faithfully reproduced. The effort plausibility assessment (Section 3) correctly synthesizes RP1e's finding about the undocumented parallelization factor (0.55-0.67x) and correctly positions the 80-person-month upper bound as the more defensible planning figure. The TE confidence analysis (Section 3.3) correctly identifies CP-03, CP-06, and CP-10 as the three Medium-confidence subsegments from RP1e. All plane-level averages are independently verified against CC1.
- **Completeness:** Complete. All 38 subsegments are present in the Phase 1 summary table (Section 5): 10 CP, 10 AL, 10 DS, 4 ISV-scope S, and 4 customer-scope S entries. Every active subsegment (34 of 38) has a verdict, confidence rating, and explanatory note. The interview questions (Section 4) are organized by role and limited to Phase 1 scope as specified.
- **Citation integrity:** Strong. Every subsegment verdict cites its source review file by ID (e.g., "Source reviews: RP1a (CP-01 to CP-03), RP1b (CP-04 to CP-06), RP1c (CP-07 to CP-10)"). The CC1 arithmetic verification is cited at each plane summary with specific discrepancy IDs (D-1, D-2). The source table (Section 6) provides 16 document paths with role descriptions. No uncited claims were found.
- **Actionability:** High. The single proposed change is presented as an exact before/after table (S1 RD 1/2 to 2/2) with impact on aggregate averages computed (P4 RD from 1.5 to 1.75; Total RD from 2.971 to 3.000). The revised Phase 1 summary table (Section 5) provides complete current and proposed ratings for all 38 subsegments, enabling direct implementation.
- **Spot-check result:** VERIFIED. The S1 Phase 1 RD adjustment 1 to 2 is explicitly captured in Section 1.4 (line 89: "S1 | Managed API Integration | 1 -> **2** | 2 | **ADJUST** | M"), in Section 2 (rating change table with before/after values and source attribution to RP4a), in Section 2 rationale (three-factor justification), and in the revised summary table (Section 5, line 299: "S1 | Managed API Integration | 1 | **2** | 2 | 2 | **RD +1**"). The adjustment was independently verified against the RP4a source file, which states "ADJUST RD 1->2" for S1 Phase 1 with matching rationale. The impact on averages (P4 RD from 1.5 to 1.75) is arithmetically correct: original sum 6/4 = 1.5, adjusted sum 7/4 = 1.75.
- **Issues found:** None material. One minor observation: the source list (Section 6) includes "RP1d" in the header line 5, but RP1d is a Phase 2 deep dive, not a Phase 1 source. However, examining the body of the document, RP1d is not actually cited in any Phase 1 rating verdict — it appears only in the header's "Input Sources" line. This is a minor header over-inclusion that does not affect any finding.

---

## SL1b: SL1b_phase2_consolidated.md

- **Score:** PASS
- **Synthesis quality:** Strong. SL1b correctly consolidates Phase 2 findings from 8 source reviews (RP1d, RP2a, RP2b, RP3a, RP3b, RP3c, RP4a, CC4) plus GT2 and the primary ratings file. The key finding — that no individual Phase 2 cell rating requires numerical adjustment but the aggregate effort estimates understate reality for two customer segments — is well-structured and internally consistent. The six P1 annotation recommendations (CP-02 Ingress NGINX EOL, CP-04 HSM customers, CP-06 air-gapped, CP-07 regulated maintenance, CP-09 FedRAMP, CP-10 SIEM integration) are correctly traced to RP1d with customer segment specificity. The CC4 heading correction ("Per-Customer Hardware Customization" to "Per-Customer Customization: Software Adaptation to Customer Hardware") and DS9 FTE inconsistency (2.0-3.25 to 0.5-1.0 FTE under customer-owns-GPU) are both captured in Section 2.4.
- **Completeness:** Complete. All 38 subsegments are present in the Phase 2 tables (Section 3): 10 CP with individual verdicts and confidence ratings, 10 AL with individual verdicts, 10 DS with individual verdicts, and 4 ISV-scope S with verdicts plus 4 customer-scope markers. The hidden Phase 1 dependency analysis (Section 4.3) covering DS1, DS6, DS8, DS9 is a valuable synthesis that consolidates findings scattered across RP3a, RP3b, and RP3c. The interview questions (Section 5) are organized by five roles and correctly scoped to Phase 2 validation.
- **Citation integrity:** Strong. Every subsegment cites its source review with section-level specificity (e.g., "Source: RP3b DS6 Phase 2; RP3c 5.2"). The external sources table (Section 7) provides 7 URLs with the specific data points used and which review agent cited them. One minor note: the RP3c reference for the 3-6 person-weeks revision (Section 2.3) correctly attributes the finding to RP3c. Cross-referencing against the RP3c source file confirms the finding exists and the attribution is accurate.
- **Actionability:** High. The aggregate effort revision is presented as exact ranges with customer segmentation: standard customers retain 10-21 person-weeks, hardware-heterogeneous customers 14-27 person-weeks, and air-gapped/regulated customers 15-30 person-weeks. The annotation table (Section 2.2) specifies exact affected customer segments and source files for each annotation. The document corrections table (Section 2.4) provides exact before/after text for the heading and DS9 FTE.
- **Spot-check result:** VERIFIED. The Phase 2 effort estimate finding for heterogeneous customers is captured in Section 2.3 (line 180: "P3 Data Plane | 2--4 person-weeks | 3--6 person-weeks | Hardware-heterogeneous customers...") and in Section 4.2 (line 285: "RP3c proposes a revised P3 Phase 2 range of **3--6 person-weeks** for hardware-heterogeneous customers"). Cross-referencing against the RP3c source file confirms the finding: RP3c states "Achievable with pre-built configuration templates; understated for hardware-heterogeneous customers" and rates the 2-4 person-weeks aggregate as "Medium-Low" confidence, noting it "does not capture the fat tail of hardware-heterogeneous customers."
- **Issues found:** One minor inconsistency. The revised Phase 2 summary (Section 3, line 267) states the total for hardware-heterogeneous/regulated customers as "~14--27 pw/customer," computed as P1 (9-18) + P2 (1-2) + P3 (3-6) + P4 (0.5-1) = 13.5-27. The low bound rounds to 14, which is acceptable as an approximation, but the stated "standard customer" total of "~10--21 pw/customer" should be P1 (6-14) + P2 (1-2) + P3 (2-4) + P4 (0.5-1) = 9.5-21. The stated low bound of 10 is again a rounded-up approximation. Both are within acceptable approximation range and match the original ratings file convention.

---

## SL1c: SL1c_phase3_consolidated.md

- **Score:** PASS
- **Synthesis quality:** Strong. SL1c correctly consolidates Phase 3 findings from the largest source set (RP1a, RP1b, RP1c, RP2a, RP2b, RP2c, RP3a, RP3b, RP3d, RP4a, CC1, CC2, CC3, CC5, GT1, GT3, GT5). The eight recommended rating adjustments are well-organized with clear before/after values, source citations, and FTE impact statements. The P2 +0.9 systematic divergence finding (Section 5.1) is correctly attributed to CC2 and RP2c with the arithmetic verification (sum of gaps = +9, average = +0.90, residual without AL02 = +0.67) faithfully reproduced. The six structural gaps from CC5 (Section 5.3) are correctly summarized with severity ratings and affected subsegment mapping. The [D] flag audit (Section 2.2) correctly identifies three misapplied flags and one correctly applied flag, matching CC2 findings.
- **Completeness:** Complete. All 38 subsegments are present in the Phase 3 tables (Section 3): 10 CP, 10 AL, 10 DS, 4 ISV-scope S. Every subsegment has current ratings, proposed ratings, scaling classification, Research FTE, and change indicator. The grand summary table (Section 3) correctly shows current and corrected FTE for all four planes plus the corrected total.
- **Citation integrity:** Strong. The source tables (Section 7) provide absolute file paths for all 10 review agent files, 4 cross-cutting review files, and 3 ground truth files. Every adjustment in Section 2.1 cites its source review and confidence level. The P3 FTE aggregate correction (Section 4.1) shows complete arithmetic working with all 10 subsegment values, enabling independent verification. Cross-cutting findings cite the appropriate CC files (CC2 for divergence, CC3 for trajectory, CC5 for structural gaps).
- **Actionability:** High. The rating adjustment table (Section 2.1) provides exact before/after values for all 8 firm adjustments plus 1 conditional adjustment. The FTE correction table (Section 4.1) provides exact stated versus corrected values with error magnitudes. The impact of rating changes on averages (Section 4.3) is computed for each affected plane. The conditional DS5 adjustment is clearly labeled with its triggering condition (RabbitMQ vs. NATS JetStream as primary broker).
- **Spot-check result:** VERIFIED (3 of 3 sub-checks).
  1. **P3 FTE aggregate correction:** The stated "~10-18 FTE" correction to 11.85-19.55 FTE is captured in the executive summary (line 12), Section 1.3 header (line 55), Section 4.1 (lines 210-221) with complete arithmetic working, and Key Finding 2 (line 320). Independent arithmetic verification: low bound 1.50+0.60+0.40+0.25+0.40+1.50+0.70+1.25+2.00+3.25 = 11.85 (confirmed). High bound 3.00+1.10+0.70+0.60+0.70+2.50+1.20+1.75+3.25+4.75 = 19.55 (confirmed). Cross-referenced against RP3d source file, which independently computes the same values and confirms both GT3 and GT5 authoritative ranges at 11.85-19.55.
  2. **Four P1 Phase 3 TE adjustments:** All four are captured in Section 1.1 (lines 28-31) and the adjustment table (Section 2.1, lines 101-104): CP-03 TE 4 to 5 (GT1 FTE 2.75-4.75 exceeds TE=4 ceiling of 2.5), CP-06 TE 3 to 4 (GT1 FTE 2.0-3.25 maps to TE=4), CP-08 TE 3 to 4 (GT1 FTE 1.5-2.5 exceeds TE=3 ceiling of 1.0), CP-10 TE 4 to 5 (GT1 FTE floor 2.75 exceeds TE=4 ceiling). Cross-referenced against source files: RP1a confirms CP-03 TE understatement with GT1 FTE 2.75-4.75; RP1b confirms CP-06 FTE of 2.0-3.25 spanning TE=3 to TE=4 bands; RP1c confirms CP-08 and CP-10 Phase 3 TE findings (CP-10 FTE floor 2.75 exceeding TE=4 ceiling of 2.5).
  3. **Grand total propagation:** The corrected grand total is computed as ~51-95 FTE (line 206), correctly reflecting the P3 correction (11.85-19.55 replaces ~10-18) propagating +2 FTE at both bounds through the total (~49-93 to ~51-95). Arithmetic: 20+18.6+11.85+0.5 = 50.95 (rounds to 51); 38+35.6+19.55+1.5 = 94.65 (rounds to 95). Confirmed.
- **Issues found:**
  1. *Minor: DS9 Phase 3 FTE of 2.00-3.25 may carry scope inconsistency.* SL1c (line 182) reports DS9 Phase 3 Research FTE as 2.00-3.25. SL1b (Section 2.4, line 189) identifies that DS9 Phase 3 FTE "2.0-3.25 is carried from a pre-scope-split estimate and should be recomputed to approximately 0.5-1.0 FTE under customer-owns-GPU assumptions" per CC4. However, SL1c does not flag this same DS9 FTE scope issue. SL1c's P3 FTE arithmetic (11.85-19.55) uses the unreduced 2.00-3.25 figure for DS9, which may overstate the P3 total by 1.0-2.25 FTE if the CC4 scope correction is applied. This discrepancy exists between SL1b and SL1c and represents the only material cross-file inconsistency found. However, this may be intentional: SL1c may be reporting the current state of the ratings file (which uses 2.00-3.25) while SL1b documents the correction as pending. The SL1c document does not explicitly address this choice.
  2. *Minor: The proposed P1 Phase 3 TE average after adjustments.* Section 3, P1 table (line 152) shows the proposed TE average as 4.5. Verification: current TE sum = 41 (5+4+4+4+5+3+5+3+4+4); proposed TE sum = 45 (5+4+5+4+5+4+5+4+4+5); 45/10 = 4.5. Confirmed correct.

---

## Summary

- **Files passing:** 3 of 3
- **Cross-file consistency:** One inconsistency identified. The DS9 Phase 3 FTE scope correction documented in SL1b (Section 2.4: revise 2.0-3.25 FTE to 0.5-1.0 FTE per CC4 customer-owns-GPU scope) is not reflected in SL1c's Phase 3 tables, where DS9 FTE remains at 2.00-3.25. This means SL1c's corrected P3 total of 11.85-19.55 FTE may itself be overstated by approximately 1.0-2.25 FTE if the DS9 scope correction is applied. If corrected, the P3 Phase 3 total would be approximately 10.35-17.30 FTE, and the grand total approximately 49.7-92.9 FTE. This cross-file tension should be resolved explicitly: either SL1c should apply the DS9 scope correction to its FTE arithmetic, or an explanatory note should state that the 2.00-3.25 figure is retained pending interview validation of the actual DS9 ISV-scope effort boundary.

  Beyond this DS9 issue, cross-file consistency is strong:
  - SL1a's S1 Phase 1 RD adjustment (1 to 2) is correctly acknowledged in SL1c (line 91) as a "Phase 1 adjustment, not Phase 3."
  - SL1b's Phase 2 ratings (no individual changes) are consistent with SL1a's Phase 1 and SL1c's Phase 3, which both identify adjustments — confirming Phase 2 as the most stable phase in the review.
  - The scope split (customer owns hardware/GPUs/AI models, ISV owns all software) is consistently stated across all three files.
  - The customer-scope treatment of S2-S5 is consistent across SL1a (Section 1.4), SL1b (Section 1.4), and SL1c (Section 1.4).
  - Rating trajectories are cross-phase consistent: no subsegment has a Phase 2 rating in SL1b that contradicts the Phase 1 (SL1a) or Phase 3 (SL1c) direction.

- **Spot-check results:** 3 of 3 verified.
  - SL1a: S1 Phase 1 RD 1 to 2 adjustment confirmed present and correctly attributed to RP4a.
  - SL1b: Phase 2 P3 effort estimate revision (2-4 person-weeks to 3-6 person-weeks for hardware-heterogeneous customers) confirmed present and correctly attributed to RP3c.
  - SL1c: P3 FTE aggregate correction (10-18 to 11.85-19.55) confirmed with independent arithmetic verification. Four P1 Phase 3 TE adjustments (CP-03, CP-06, CP-08, CP-10) confirmed present with correct source attribution and FTE justification.

---

## Cumulative Context Verification

The following cumulative context items from prior waves were checked against the SL1 outputs:

| Context Item | Expected Location | Found? | Accurate? |
|---|---|:---:|:---:|
| 228 ratings across 38 subsegments x 3 phases x 2 dimensions | All three files | Yes | Yes — each file covers 38 subsegments for its respective phase across RD and TE |
| Phase 3 TE systematically understated across P1, P2, P3 | SL1c | Yes | Yes — SL1c identifies 4 P1 TE understatements, 1 P2 TE understatement, 1 P3 TE understatement, plus 2 P2 RD understatements. All adjustments are upward (+1). Key Finding 1 (line 318) explicitly states "No rating is overstated; all corrections are upward." |
| P3 FTE aggregate "~10-18" should be 11.85-19.55 | SL1c | Yes | Yes — Section 4.1 with complete arithmetic working |
| S1 Phase 1 RD adjusted 1 to 2 | SL1a | Yes | Yes — Section 2 with three-part rationale |
| 3 false [D] divergence flags identified | SL1c | Yes | Yes — Section 2.2 identifies AL10 Phase 1, AL10 Phase 3, and DS10 Phase 3 as misapplied, plus AL05 Phase 3 as ambiguous |
| 6 structural risk gaps identified by CC5 | SL1c | Yes | Yes — Section 5.3 lists all 6 gaps with severity and affected subsegments |
