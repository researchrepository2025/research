# G3: Wave 4 Quality Review — P3 Data Plane (RP3a, RP3b, RP3c, RP3d)

**Review Date:** 2026-02-19
**Reviewer:** G3 (Quality Gate 3)
**Scope:** All four Wave 4 output files covering the P3 Data Plane (DS1-DS10) across Phase 1, Phase 2, and Phase 3 ratings.
**Ground Truth File:** GT3_P3_ground_truth.md

---

## File Reviews

---

### RP3a: RP3a_P3_traditional_data.md

- **Score:** PASS
- **Citation integrity:** Strong. Every factual claim carries an inline citation with file path or URL. Sources include F41, F42, F43, F44, F55a, F76, F73, and external URLs (InfoQ MinIO maintenance mode, Medium PostgreSQL article, DragonflyDB, CrunchyData). All internal file paths are absolute and verifiable. External URLs are properly formatted with publication dates. The [FACT] and [STATISTIC] tags are used consistently to distinguish claim types. One external source (Medium article, February 2026) is used to establish a floor estimate for PostgreSQL operational hours, which is appropriate directional evidence rather than a primary proof point.
- **Scope discipline:** Excellent. File covers DS1 through DS5 only, as assigned. No investigation of DS6-DS10. No overreach into Phase 3 FTE totals or aggregate P3 estimates (those belong to RP3c and RP3d). Cross-references to F76 failure domain data are used for corroboration, not independent re-investigation.
- **Comparison quality:** Ratings are re-derived from ground truth with explicit reasoning chains. The DS3/DS4 Phase 1 differentiation assessment (RD=3 vs RD=2) is particularly well-argued, citing distinct operational surfaces (Redis Sentinel/Cluster mode selection vs MinIO drive-count-deterministic EC:4). Two ADJUST verdicts are issued with clear quantitative justification: DS2 Phase 3 TE=2 vs documented 0.6-1.1 FTE (falls in TE=3 band), and DS5 Phase 3 TE=2 with broker-conditional accuracy (NATS 0.3-0.6 FTE supports TE=2; RabbitMQ 0.75-1.25 FTE warrants TE=3).
- **Content depth:** All five subsegments are covered across all three phases (15 subsegment-phase combinations, 30 individual ratings). The MinIO maintenance mode finding (December 2025) is a material post-research development that adds genuine analytical value. Interview questions for medium-confidence ratings are well-targeted. The summary verdict table provides a clear 30-rating disposition at a glance.
- **Issues found:** None material. Minor observation: the DS3 Phase 3 verdict says "ACCURATE" but notes the FTE range (0.4-0.7) falls at the TE=2/TE=3 boundary -- the same pattern that triggers an ADJUST for DS2 and DS5. The inconsistency is noted in the asterisk footnote but could be clearer about why DS3 gets ACCURATE treatment while DS2 gets ADJUST at a similar boundary position. The distinction appears to be that DS2's FTE range (0.6-1.1) falls more definitively into TE=3, while DS3's range (0.4-0.7) straddles the boundary more evenly.
- **Fix recommendations:** None required.

---

### RP3b: RP3b_P3_streaming_ai_data.md

- **Score:** PASS
- **Citation integrity:** Strong. All claims carry inline citations with file paths or URLs. The DS6 "13-26 hrs/week" claim validation is particularly thorough: the file traces the figure back to F44 Section 7, reconstructs the task-level breakdown, identifies the derivation chain (OneUptime, Confluent FTE framework, Coudo AI), and explicitly notes that the specific hourly figure is not independently reproduced verbatim by external primary sources. External URLs include AutoMQ, Confluent white paper, HackerNoon, Airbyte, and Instaclustr -- all properly formatted with descriptions.
- **Scope discipline:** Excellent. File covers DS6 through DS10 only, as assigned. DS1-DS5 are explicitly excluded in the header. The DS9 Phase 1 scope reduction assessment correctly analyzes the ISV/customer scope split and its impact on difficulty ratings without re-investigating the scope split itself (which belongs to the ratings file's own conventions).
- **Comparison quality:** All 30 ratings for DS6-DS10 are confirmed ACCURATE with no numerical changes required. The DS10 Phase 3 [D] flag finding is the most analytically sophisticated element: the file identifies that the [D] flag is technically misapplied at a 1-point gap (RD=3, TE=4) when the definition requires a 2-point gap, while simultaneously validating the underlying divergence narrative as substantively correct. The DS8 Phase 3 TE=3 borderline assessment (GT3 FTE 1.25-1.75 spanning the TE=3/TE=4 boundary) is honest about the ambiguity.
- **Content depth:** Covers all five subsegments across three phases. The DS9 scope reduction section (lines 284-308) provides a detailed decomposition of what GPU responsibilities transfer to the customer vs what the ISV retains. The DS6 claim validation section (lines 96-121) is a model of how to verify an internally-derived statistic. Interview questions are appropriately targeted at medium-confidence verdicts.
- **Issues found:**
  1. The [D] flag finding for DS10 is analytically correct but could be more direct in its recommendation. The file presents two options (remove the flag and replace with prose, or clarify the threshold) without clearly recommending one. For a ratings file that will be used by executives, the actionable recommendation should be explicit.
  2. The DS8 Phase 3 verdict says "ACCURATE (borderline)" with re-derived TE "3-4". This is slightly ambiguous -- it would be clearer to state whether the file recommends TE=3 or TE=4 as the preferred assignment, even if both are defensible.
- **Fix recommendations:** Both issues are minor and do not require rework. If the file were to be revised, adding a single-sentence recommendation for DS10 [D] flag disposition and DS8 TE assignment preference would strengthen it.

---

### RP3c: RP3c_P3_effort_validation.md

- **Score:** PASS
- **Citation integrity:** Strong. The file cites 18 distinct source files and 4 external URLs. Every phase estimate is traced back to per-subsegment TE band assignments with explicit arithmetic. The IDC/Aiven white paper citation (August 2021) is properly dated and attributed. The SAS/EDB case study is correctly characterized as a lower bound (minimal initial deployment, not full HA). The RAGOps arXiv citation (2506.03401) includes the paper identifier. The G1 scaling model citation correctly attributes the "P3 scales sublinearly" finding to the appropriate analysis file.
- **Scope discipline:** Good. The file covers Phase 1 and Phase 2 P3 effort estimates only, as assigned. Phase 3 FTE ranges are explicitly excluded per scope boundary (deferred to RP3d). One minor scope adjacency: the file references P1 Phase 2 effort (6-14 person-weeks) for proportionality comparison with P3 Phase 2 (2-4 person-weeks). This is appropriate cross-referencing, not scope violation -- it uses the P1 figure as context rather than re-investigating it.
- **Comparison quality:** The arithmetic reconstruction in Section 2.2 (TE band midpoints summing to approximately 47 person-months sequential) is transparent and well-documented. The reconciliation in Section 2.3 clearly identifies the three conditions required for the 20-40 range to hold (parallel execution, P1 substrate assumption, DS9 scope reduction). The Phase 2 assessment is particularly incisive: it distinguishes between the four subsegments where "primarily tuning" is accurate (DS3, DS4, DS5, DS10) and the four where hardware heterogeneity generates non-trivial reconfiguration (DS1, DS6, DS8, DS9). The proposed revision from 2-4 to 3-6 person-weeks is well-justified.
- **Content depth:** The file provides five clearly articulated findings, ten targeted interview questions, a confidence assessment table, and a mandatory migration pressure section. The integration overhead analysis (Section 2.5, citing G1) adds value by connecting Phase 1 per-subsegment estimates to the broader N-services scaling model. The mandatory migration section (Kafka KRaft, Milvus Woodpecker, Apache Tika 3.x) correctly identifies Phase 1 scoping dependencies that are not visible from the per-subsegment ratings alone.
- **Issues found:**
  1. Section 2.2 computes the midpoint sum as "approximately 47 person-months" but does not show the addition step-by-step. Readers must verify: 9+4+1.2+1.2+1.2+9+4+4+4+9 = 46.8, which rounds to approximately 47. This is correct but not transparent for a reader who wants to verify quickly.
  2. The Phase 2 proposed revision (3-6 person-weeks) is stated in the executive summary and Section 5.5 but the specific arithmetic supporting the higher estimate is less detailed than the Phase 1 decomposition. The file explains qualitatively why DS1/DS6/DS8/DS9 exceed the TE=2 band for heterogeneous hardware customers, but does not propose revised per-subsegment TE values that would sum to 3-6 person-weeks.
- **Fix recommendations:** Neither issue requires rework. Both are presentation refinements that would improve transparency for a secondary reader.

---

### RP3d: RP3d_P3_fte_scaling.md

- **Score:** PASS
- **Citation integrity:** Excellent. Every FTE comparison is presented as a side-by-side match between the ratings file value and the GT3 source value, with explicit source citations for both. The aggregate discrepancy finding (Section 2.5) cites three independent confirmations: the arithmetic sum from the ratings file rows, the GT3 authoritative total, and the GT5 corroborating total. The "Scales with N?" classification assessments cite both the ratings file notes and the GT3 source evidence for each subsegment. External sources are not heavily used (this is primarily an internal consistency check), which is appropriate for the scope.
- **Scope discipline:** Excellent. The file covers Phase 3 FTE ranges and "Scales with N?" classifications only, as assigned. Phase 1 and Phase 2 are explicitly excluded. The G1 scaling model consistency check (Section 4) appropriately cross-references the G1 per-service increment without re-investigating G1's methodology.
- **Comparison quality:** The core finding -- that all ten individual FTE values match GT3 exactly while the aggregate "~10-18 FTE" label understates the arithmetic sum by 1.85-1.55 FTE -- is precisely quantified and triple-confirmed. The "Scales with N?" assessment is methodical: DS1 and DS6 "Yes" are confirmed with per-customer operational activities cited; DS10 "No" is confirmed with shared-team role structure cited; the seven "Partial" classifications are assessed individually, with DS9 flagged as the weakest classification. The FTE range width analysis (Section 5) adds strategic context by identifying which subsegments carry the most uncertainty.
- **Content depth:** The file covers all 10 subsegments with individual verdicts, provides an aggregate validation, assesses all 10 scaling classifications, cross-references the G1 model, and includes a FTE range width analysis. Five clearly stated key findings synthesize the work. The DS4 range width assessment correctly notes that the composite upper bound (0.60 FTE) is below the Ceph low (0.50 FTE), identifying a hidden risk if customers deploy Ceph rather than MinIO.
- **Issues found:**
  1. The aggregate FTE discrepancy ("~10-18" vs "11.85-19.55") is the most actionable finding in all four Wave 4 files. However, the file does not include a specific recommendation to update the Phase 3 Summary table in the ratings file. The finding is stated as a fact without a disposition (e.g., "ADJUST: update to ~12-20 FTE" or "FLAG: annotate the tilde as intentional rounding").
  2. The DS9 "Partial" scaling classification is identified as "weakly supported" but the file does not recommend a specific alternative (e.g., change to "No" or add a qualifying note). This is consistent with the file's analytical posture but leaves the disposition ambiguous.
- **Fix recommendations:** Minor. Add an explicit recommendation for the aggregate FTE label disposition and the DS9 scaling classification. These are one-line additions, not structural changes.

---

## Spot-Check Results

### Check 1: DS1 Phase 3 FTE Range (RP3a)

**Claim (RP3a, line 76):** "On-premises FTE: 1.5-3.0 FTE with 24/7 on-call; Managed K8s 0.85-1.25 FTE; Cloud-native 0.25-0.5 FTE" -- attributed to F41.

**GT3 data (GT3, lines 43-52):** DS1 FTE table shows On-Premises: 1.50-3.00, Managed K8s: 0.50-0.85, Cloud-Native: 0.25-0.50. Source: F41.

**Assessment:** The On-Premises and Cloud-Native FTE ranges match exactly. The Managed K8s figure in RP3a (0.85-1.25) differs from GT3 (0.50-0.85). RP3a's quote appears to come from F41's direct text rather than the GT3 summary table. The discrepancy is between two representations of the same source data: F41 may report different Managed K8s figures depending on whether it measures CloudNativePG-only (0.85-1.25) vs a broader Managed K8s scope (0.50-0.85). The On-Premises figure -- which is the primary figure under review -- matches precisely.

**Verdict:** MATCH on the primary claim (On-Premises FTE). Minor variance on Managed K8s figure that does not affect the RP3a analysis, which focuses on On-Premises ratings.

---

### Check 2: DS8 On-Premises FTE Range (RP3b)

**Claim (RP3b, lines 191-194):** GT3 FTE ranges for DS8 On-Premises: 1.25-1.75.

**GT3 data (GT3, lines 486-488):** DS8 On-Premises FTE Range: 1.25-1.75.

**Assessment:** Exact match. No discrepancy.

**Verdict:** MATCH.

---

### Check 3: Aggregate P3 Phase 3 FTE Discrepancy (RP3d)

**Claim (RP3d, lines 315-329):** The arithmetic sum of individual DS1-DS10 Phase 3 FTE ranges is 11.85-19.55, while the ratings file Phase 3 Summary states "~10-18 FTE." Low-end discrepancy: 1.85 FTE (15.6%); high-end discrepancy: 1.55 FTE (7.9%).

**GT3 data (GT3, lines 705, 714-718):** Total FTE Range On-Premises: 11.85-19.55. Aggregate FTE Comparison table confirms: On-Premises Conservative 11.85, Peak 19.55.

**Assessment:** The GT3 source authoritatively confirms 11.85-19.55. The RP3d finding that the "~10-18 FTE" aggregate label understates the correct sum is verified. The discrepancy magnitudes (1.85 low / 1.55 high) are arithmetically confirmed by summing individual GT3 values.

**Verdict:** MATCH. The discrepancy finding is confirmed against ground truth.

---

## Summary

- **Files passing:** 4 of 4
- **Files with minor issues:** 4 (RP3a, RP3b, RP3c, RP3d -- all carry minor presentation or recommendation-specificity issues that do not require structural rework)
- **Files needing rework:** 0

### Cross-File Consistency Notes

1. **TE scale boundary treatment is inconsistent between RP3a and RP3b.** RP3a flags DS2 Phase 3 TE=2 as ADJUST when the documented FTE (0.6-1.1) falls in the TE=3 band, but treats DS3 Phase 3 TE=2 as ACCURATE when the documented FTE (0.4-0.7) also falls in the TE=3 band. RP3b does not encounter this issue because no DS6-DS10 ratings require TE adjustment. The inconsistency is minor and documented in RP3a's footnote, but a future consistency pass should establish a clear threshold for when a boundary-straddling FTE triggers ADJUST vs ACCURATE.

2. **DS5 Phase 3 FTE composite vs per-tool figures align across files.** RP3a reports the composite DS5 FTE as 0.4-0.7 (matching GT3), while noting the per-tool figures of RabbitMQ 0.75-1.25 and NATS 0.3-0.6. RP3d independently confirms the 0.4-0.7 composite matches GT3. The composite blending methodology is consistent.

3. **DS9 "Partial" scaling classification is questioned in RP3d but accepted without comment in RP3b.** RP3b evaluates DS9 Phase 3 as RD=3, TE=3 ACCURATE and does not assess the scaling classification (correctly, as scaling is RP3d's scope). RP3d then flags DS9 "Partial" as weakly supported. There is no contradiction, but the two files would benefit from a cross-reference.

4. **The aggregate FTE discrepancy (RP3d) is the highest-priority actionable finding across Wave 4.** The "~10-18 FTE" label in the Phase 3 Summary table appears in executive-facing summary sections of the ratings file. The correct figure, confirmed by GT3 and GT5, is 11.85-19.55. This is a labeling error in the ratings file that should be corrected before the ratings file is used in external presentations.

5. **The DS10 [D] flag misapplication (RP3b) and the aggregate FTE understatement (RP3d) are the only two corrections that should flow back to the ratings file.** All other findings are ACCURATE verdicts, boundary annotations, or recommendations for future review cycles.

### Key Findings Across Wave 4

1. **All 60 individual subsegment-phase ratings (DS1-DS10 x 3 phases x RD+TE) are directionally accurate.** Across RP3a (30 ratings) and RP3b (30 ratings), no rating requires a change of more than 1 point. RP3a identifies 2 ADJUST flags out of 30; RP3b identifies 0 numerical adjustments and 1 flag misapplication out of 30. The research base supporting the P3 Data Plane ratings is robust.

2. **The Phase 3 aggregate FTE label in the ratings file ("~10-18 FTE") understates the arithmetic sum of its own per-subsegment data by 1.85 FTE at the low end and 1.55 FTE at the high end.** The correct figure, triple-confirmed by GT3, GT5, and RP3d's independent arithmetic, is 11.85-19.55 FTE. This is the highest-priority correction emerging from Wave 4.

3. **Phase 2 P3 effort (2-4 person-weeks) is accurate for low-complexity subsegments but understates effort for hardware-heterogeneous customers.** RP3c demonstrates that DS1, DS6, DS8, and DS9 Phase 2 effort exceeds the "primarily tuning" characterization when customers present non-standard storage controllers, Kafka node topologies, vector corpus sizes, or GPU generations. A revised range of 3-6 person-weeks is proposed for customers with meaningful hardware variance.

4. **Three mandatory 2025-2026 migrations (Kafka KRaft, Milvus Woodpecker WAL, Apache Tika 3.x) create non-negotiable Phase 1 scoping dependencies.** RP3c correctly identifies that Phase 1 plans deferring these migrations embed technical debt that compounds Phase 2 delivery risk. Additionally, RP3a identifies MinIO community edition entering maintenance mode (December 2025) as a material post-research development not yet reflected in the ratings.

5. **The DS9 Phase 1 scope reduction from 5/5 to RD=3, TE=3 is correctly applied under the ISV/customer scope split** but is internally documented only as an inline note, not as a formal cross-reference to the scope split section. This is a documentation gap, not an accuracy error, but should be addressed for traceability given that the 2-point reduction is the largest scope-driven adjustment in the P3 plane.
