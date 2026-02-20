# G3 Wave 5 Review: P4 AI Model Plane Review Files

**Reviewer:** G3 Quality Reviewer
**Date:** 2026-02-19
**Wave:** 5 (P4 AI Model Plane)
**Files Reviewed:** RP4a, RP4b, RP4c
**Ground Truth Reference:** GT4_P4_ground_truth.md

---

## RP4a: P4 ISV-Scope Subsegments (S1, S6, S7, S8)

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4a_P4_isv_scope.md`

- **Score:** PASS

- **Citation integrity:** Strong. Every factual claim is traced to either the internal ground truth files (GT4, P4_ai_model_plane.md, three_phase_on_prem_ratings.md) or external URLs. External citations include vLLM docs (https://docs.vllm.ai/en/stable/serving/openai_compatible_server/), LiteLLM docs (https://docs.litellm.ai/docs/proxy/load_balancing, https://docs.litellm.ai/docs/proxy/prod), the Improving.com Bedrock migration article, dataunboxed.io monitoring guide, and apxml.com SLO examples. All URLs are properly formatted and not truncated. Statistics are consistently attributed with [STATISTIC] or [FACT] tags. The arXiv 2511.07424 reference (156 production incidents) is properly sourced through the F76 intermediary. The sources table at the end is comprehensive, listing 12 sources with types and URLs/paths.

- **Scope discipline:** Excellent. The file reviews only S1, S6, S7, S8 as specified. S2-S5 are explicitly marked as out of scope in the header ("S2-S5 are customer scope and are not reviewed here"). Cross-references to RP2b (for AL09 P2/P4 boundary) and GT5 (for cross-plane rankings) are handled via file references rather than re-investigation. The cross-subsegment validation section (lines 448-464) appropriately references P2/P4 boundary findings from RP2b without re-deriving them.

- **Comparison quality:** Excellent. Each of the 24 ratings (4 subsegments x 3 phases x 2 dimensions) is individually re-derived against ground truth data. The re-derivation methodology is transparent: the reviewer extracts the source file's original difficulty ratings, maps them through the scope reduction model, and compares against the three-phase file's ratings. Confidence scores are assigned to each verdict (High or Medium). The only adjustment recommended (S1 Phase 1 RD from 1 to 2) is supported by three independent lines of evidence: (1) auth re-implementation complexity, (2) Bedrock-specific schema delta cited to Improving.com, and (3) error handling rewrite. The FTE calibration tension for S6 and S7 Phase 3 is flagged with appropriate nuance -- noted as within tolerance for small customer bases but potentially understated at the G1 model's 50-customer scale.

- **Content depth:** Excellent. The file addresses all required sub-topics from the agent spec: re-derives all 24 ratings from GT4 ground truth; validates the "calling customer endpoints" model with external evidence from vLLM and LiteLLM documentation; specifically assesses S1 Phase 1 RD=1 with a detailed 5-point argument for adjustment; validates S6/S7 Phase 3 FTE ranges with upper/lower bound analysis; cites external LiteLLM operational evidence (production deployment requirements including Redis, Prisma, health check isolation); includes confidence scores for each rating; and provides interview questions for three subsegments. The Rating Methodology Note (lines 20-37) is a valuable addition that clarifies the distinction between the source file's absolute difficulty scale and the three-phase file's relative difficulty scale -- this prevents a common misinterpretation.

- **Terminology & style:** Executive summary is present (2 substantial sentences covering the main finding and the specific adjustment). Key Findings section has 5 bullets. Section headers are clear and follow a consistent pattern (subsegment > Ground Truth Extraction > Phase N > Current rating > Re-derived rating > Verdict). Glossary terms (RD, TE, [D], Phase 1/2/3) are used consistently throughout. The summary rating table (lines 491-506) provides a clear at-a-glance view.

- **Issues found:** One minor structural observation: The summary rating table shows "2-3*" for S6 Phase 3 TE and S7 Phase 3 TE, with the asterisk explanation below the table. This is clear but could be formalized. No substantive errors found.

- **Fix recommendations:** None required.

---

## RP4b: P4 Scope Exclusion Validation (S2-S5)

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4b_P4_scope_exclusion.md`

- **Score:** PASS

- **Citation integrity:** Strong. The file cites 14 external sources with full URLs, including NVIDIA RTX ISV Certifications (nvidia.com/en-us/products/workstations/isv-certifications/), NVIDIA NIM Support Matrix (docs.nvidia.com), vLLM docs, Cloudera AI Inference Service page, Google Distributed Cloud blog, RunPod CUDA documentation, LogicMonitor AI workload guide, IntuitionLabs inference hardware guide, and Northflank GPU hosting guide. Internal citations trace to P4_ai_model_plane.md, three_phase_on_prem_ratings.md, GT4, and GT5. The 78% GPU compatibility struggle statistic (Northflank) is appropriately attributed. The four "UNVERIFIED" tags in section 5.2 are commendable -- the reviewer explicitly marks where they have estimated FTE figures without direct source quantification, distinguishing those from sourced data points.

- **Scope discipline:** Excellent. The file stays within its assigned scope of S2-S5 customer scope validation. References to S1, S6, S7 (ISV-scope subsegments) are made only where they intersect with S2-S5 boundary questions (e.g., S1 error handling when S2 inference engine fails). The Cloudera and GDC edge cases (sections 4.3, 4.4) are appropriate scope expansions that test the boundary assumptions rather than re-investigating ISV-scope subsegments. Cross-references to RP4a are implicit (via the GT4 ground truth) rather than duplicative.

- **Comparison quality:** Strong. The aggregate FTE transfer (5.50-10.50 FTE to customer) is correctly sourced from P4_ai_model_plane.md section 5, with an appropriate footnote about staff sharing between S3 and S4/S5 preventing double-counting. The four residual ISV obligation categories are individually substantiated: (1) hardware compatibility matrix against NVIDIA NIM support matrix template, (2) API contract enforcement against the 60% inference engine incident statistic, (3) minimum GPU resource specification against VRAM requirements data, (4) insufficient GPU allocation triage against the MIG contention evidence. The summary assessment table (section 6) provides a clear correctness judgment per exclusion aspect.

- **Content depth:** Excellent. All required sub-topics are addressed: S2-S5 descriptions are reviewed with full FTE data (section 1); the "zero ISV responsibility" question is explicitly answered as "structurally correct for primary ops but with four unrated residual obligations" (sections 2, 5); edge cases are identified with specificity -- quantization format mismatch (82% throughput degradation), model version divergence, vLLM API drift (sections 3.1-3.3); ISV support responsibilities not captured are enumerated with effort estimates even where unverified (section 4); and alternative ISV models (Cloudera ISV-managed inference, Google Distributed Cloud managed on-premises) are examined as scope boundary challenges (sections 4.3-4.4). The four [UNVERIFIED] effort estimates in section 5.2 are clearly distinguished from verified data.

- **Terminology & style:** Executive summary is 2 sentences covering the main finding (exclusion structurally sound) and the key gap (four unrated residual obligations). Key Findings section has 5 bullets. Section headers are clear. Glossary terms are used consistently. The summary assessment table (section 6) is well-structured with Correctness, Residual ISV Obligation, and Currently Rated columns.

- **Issues found:**
  1. Minor: The aggregate FTE range "5.50-10.50 FTE" in section 1.5 is presented as the sum of S2+S3+S4+S5 (2.00-3.50 + 2.50-5.00 + 0.50-1.00 + 0.50-1.00 = 5.50-10.50). The footnote correctly notes that S3/S4/S5 share staff with no double-counting, but the arithmetic sum still adds them. The text does acknowledge this ("with S4/S5 sharing staff with S3 per source footnote, so actual transfer is non-additive"), which mitigates the issue. The non-additive actual transfer figure is not separately stated.
  2. Minor: The Northflank "78% of teams struggle with GPU compatibility during CI/CD" statistic is attributed to "Northflank 2025 deployment guide, cited via search result summary." This attribution acknowledges the indirect sourcing, which is transparent, but the statistic itself could not be verified against the original source from the provided content.

- **Fix recommendations:** None required. The non-additive FTE acknowledgment is sufficient. The Northflank citation transparency is adequate.

---

## RP4c: P4 Completeness & Missing AI Concerns

**File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4c_P4_completeness.md`

- **Score:** PASS

- **Citation integrity:** Strong. The file cites 16 external sources with full URLs, including arXiv papers (2505.03574 for LlamaFirewall, 2510.19169 for OpenGuardrails), NVIDIA NeMo Guardrails developer page, enterprise LLMOps sources (ACI Infotech, Swept AI, Bitrock, Radicalbit), cost tracking tooling (Langfuse docs, ngrok blog, Sylphai, Caylent, Medium), and Gartner press release. Internal citations reference 7 source files with section numbers. The Gartner "40% of agentic AI projects will be canceled by end of 2027" statistic is properly attributed with the specific press release date (2025-06-25) and URL. The prompt caching cost data ("cache writes cost 1.25x to 2x standard input tokens" and "cache hits approximately 10% of standard input token cost") is attributed to the ngrok blog.

- **Scope discipline:** Excellent. The file stays within P4 completeness and AI gap analysis. References to P2 (AL09, RP2b, RP2e) and P3 (DS9) are made only to identify boundary gaps, not to re-investigate those subsegments. The RP2e cross-reference for the API Versioning partial gap treatment (section 3.3) is appropriate methodology borrowing. The proposed subsegments S9 and S10 are scoped to P4 and do not encroach on P2/P3 territory -- the prompt management finding explicitly concludes "no new subsegment required in P4" and recommends scope note clarifications in S6 and AL09 instead.

- **Comparison quality:** Good. The proposed difficulty ratings for S9 and S10 follow the established tier structure (Cloud-Native / Managed K8s / On-Premises) and are individually justified with rationale. The three-phase ratings for both proposed subsegments include RD and TE with notes. The S9 on-premises difficulty of 4/5 is justified by the compute requirement for guardrail models (OpenGuardrails-Text at 3.3B parameters), the lack of managed policy management UI, and customer-specific policy tuning. The S10 on-premises difficulty of 4/5 is justified by the absence of provider cost APIs and the requirement to build attribution from gateway instrumentation through Langfuse to customer reporting. These ratings are plausible but inherently less grounded than RP4a's re-derivations of existing ratings, because S9 and S10 are proposed (not existing) subsegments.

- **Content depth:** Excellent. All required sub-topics are addressed: AI Safety/Guardrails gap assessment spans current classification, industry landscape (three self-hosted frameworks cited), boundary analysis, and a proposed subsegment with full ratings (section 2); Prompt Management/Caching analysis distinguishes Level 1 (KV-cache routing, covered in S6) from Level 2 (semantic cache and template management, partially covered) and correctly concludes scope note clarification is sufficient (section 3); Model Cost Attribution analysis examines cloud-native vs on-premises structural differences and identifies the end-to-end pipeline gap (section 4); P2/P3/P4 boundary gap analysis identifies three gaps with severity assessments (section 5); emerging LLMOps frameworks are mapped to the current P4 framework (section 6.1); and the five MECE frameworks convergence on AI safety is cited from the S1 synthesis (section 6.2).

- **Terminology & style:** Executive summary is 2 sentences. Key Findings section has 5 bullets. Section headers are clear and follow a consistent gap assessment pattern (Current Classification > Industry Evidence > Boundary Analysis > Verdict). The gap classification table (section 7.1) and revised subsegment count table (section 7.2) are well-structured. Glossary terms are used consistently.

- **Issues found:**
  1. Minor: In section 2.3, the statement "AL09 (P2) references LlamaFirewall in its infrastructure stack but does not rate the guardrail component independently" relies on RP2b's analysis of AL09. This is a valid cross-reference but RP4c does not quote the specific RP2b finding -- it characterizes it. The characterization appears accurate based on the RP2b file content reviewed in Wave 3.
  2. Minor: The proposed FTE estimate for S9 on-premises ("0.3-0.8 FTE annually") is presented without a direct external benchmark. The file acknowledges this implicitly by not tagging it as a [STATISTIC], but it would benefit from an explicit [UNVERIFIED] tag as RP4b uses for its estimated figures.
  3. Minor: The proposed FTE estimate for S10 on-premises ("0.2-0.5 FTE annually") has the same issue -- no direct external benchmark and no [UNVERIFIED] tag.

- **Fix recommendations:** Consider adding [UNVERIFIED] tags to the S9 and S10 FTE estimates to maintain consistency with RP4b's practice of explicitly marking estimated figures.

---

## Spot-Check Results

### Data Point 1: S1 Phase 1 RD Rating and FTE Range

**GT4 ground truth states:**
- S1 original difficulty ratings: Cloud-Native 1, Managed K8s 1, On-Premises 2 (GT4, S1 Difficulty Ratings section)
- S1 original FTE: Cloud-Native 0.05-0.15, Managed K8s 0.05-0.15, On-Premises 0.10-0.30 (GT4, S1 FTE Estimates section)
- S1 remains ISV scope under scope split (GT4, Table 3)

**Three-phase ratings file states:**
- S1 Phase 1: RD=1, TE=2 (three_phase_on_prem_ratings.md, P4 Phase 1 table, line 116)
- Notes: "Replace Bedrock/Azure OpenAI/Vertex AI endpoint calls with customer's inference endpoint. Auth method adaptation (cloud IAM to customer's auth). Error handling for different response schemas. Same pattern, different endpoint."

**RP4a reports:**
- Current rating: RD=1, TE=2 (line 70) -- MATCHES three-phase file
- Re-derived RD: 2 (line 90) -- ADJUSTMENT recommended
- TE=2 confirmed accurate (line 88)
- S1 original on-premises difficulty: 2, cloud-native: 1, delta: +1 (line 26-27) -- MATCHES GT4

**Verdict: MATCH.** RP4a accurately extracts the current rating from the three-phase file (RD=1, TE=2), accurately cites the GT4 ground truth data (On-Premises=2, Cloud-Native=1, delta=+1), and its recommended adjustment (RD 1 to 2) is evidence-based. The S1 FTE of 0.1-0.3 for on-premises is correctly cited from GT4.

### Data Point 2: S6 Phase 3 FTE Range

**GT4 ground truth states:**
- S6 original FTE: Cloud-Native 0.10-0.25, Managed K8s 0.20-0.50, On-Premises 0.50-1.00 (GT4, Table 2)
- S6 Phase 3 revised ISV FTE under scope split: 0.2-0.5 FTE (GT4, citing three_phase_on_prem_ratings.md section 6)

**Three-phase ratings file states:**
- S6 Phase 3: RD=2, TE=2, Research FTE 0.2-0.5 (three_phase_on_prem_ratings.md, P4 Phase 3 table, line 277)

**RP4a reports:**
- S6 Phase 3 stated FTE range: 0.2-0.5 FTE (line 162, line 227) -- MATCHES GT4 and three-phase file
- S6 pre-scope-split on-premises FTE: 0.50-1.00 FTE (line 153) -- MATCHES GT4 Table 2
- RP4a notes calibration tension: TE=2 scale is 0.1-0.3 FTE but research range upper bound is 0.5 FTE which corresponds to TE=3 (line 229-231)

**Verdict: MATCH.** RP4a accurately cites the S6 Phase 3 FTE range as 0.2-0.5 FTE, matching both GT4 and the three-phase file. The calibration tension observation (TE=2 scale midpoint vs. stated 0.5 FTE upper bound) is a valid analytical finding, not a data mismatch.

### Data Point 3: S2-S5 Scope Exclusion Rationale

**GT4 ground truth states:**
- S2 shifts to customer scope: "Subsegments S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) shift to customer responsibility." (GT4, Table 3, citing three_phase_on_prem_ratings.md section 1)
- Scope basis: "GPU + AI models: Customer -- GPU procurement, driver management, inference engine operation, model weights, CUDA stack." (GT4, S3 Scope Classification section)
- Combined pre-split S2+S3+S4+S5 on-premises FTE: S2 2.00-3.50 + S3 2.50-5.00 + S4 0.50-1.00 + S5 0.50-1.00 = total 5.50-10.50 FTE (GT4, Table 2)
- After scope split, ISV P4 FTE reduces to approximately 0.45-2.30 FTE (GT4, Table 4)

**Three-phase ratings file states:**
- Section 1 scope split table: "GPU + AI models: Customer -- GPU procurement, driver management, inference engine operation, model weights, CUDA stack" (line 16)
- S2, S3, S4, S5 all marked "Customer scope" in Phase 1, 2, and 3 tables with "--" for RD and TE

**RP4b reports:**
- Aggregate FTE transferred: 5.50-10.50 FTE (line 95) -- MATCHES GT4 Table 2
- Post-split ISV P4 FTE: approximately 0.45-2.30 FTE (line 103) -- MATCHES GT4 Table 4
- Scope split quote: "Subsegments S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) shift to customer responsibility." (line 99) -- MATCHES GT4 and three-phase file
- Correctly identifies the four residual ISV obligations not captured in the binary scope exclusion

**Verdict: MATCH.** RP4b accurately reports the S2-S5 scope exclusion rationale, aggregate FTE transfer, and post-split ISV FTE, all matching GT4 and the three-phase source file.

---

## Summary

- **Files passing:** 3 of 3
- **Files with minor issues:** 1 (RP4c -- missing [UNVERIFIED] tags on proposed S9/S10 FTE estimates)
- **Files needing rework:** 0

### Cross-File Consistency Notes

1. **RP4a and RP4b are internally consistent on the scope split model.** RP4a validates the ISV-scope subsegments (S1, S6, S7, S8) and confirms the scope reduction is "directionally correct." RP4b validates the customer-scope exclusion (S2-S5) and confirms the exclusion is "structurally correct for primary ops." Neither file contradicts the other's scope characterization.

2. **RP4a's S1 Phase 1 RD adjustment (1 to 2) is consistent with RP4b's finding of residual ISV obligations.** RP4a argues the auth re-implementation and schema delta justify RD=2. RP4b identifies API contract enforcement at the inference endpoint as an unrated residual obligation. These findings reinforce each other: the S1 Phase 1 task is harder than "trivial" precisely because the ISV must handle the interface complexity that RP4b identifies as a cross-scope interaction.

3. **RP4a and RP4c are consistent on the P2/P4 boundary.** RP4a notes that "AI-related ISV effort correctly lives in P2 (AL09) and P3 (DS9, DS10), not P4" and cites AL09 as the #1 hardest on-premises subsegment. RP4c identifies that guardrails (currently housed implicitly in AL09) and cost attribution (currently fragmented across S1, S6, S7, AL09) need clearer homes. These findings are complementary: RP4a validates the existing P4 ratings as accurate, and RP4c identifies what is missing from P4 that should be added.

4. **FTE totals are consistent across all three files.** RP4a cites Phase 3 ISV P4 FTE as 0.45-1.45 FTE (S1+S6+S7+S8 lower and upper bounds). RP4b cites the post-split ISV P4 FTE as "approximately 0.45-2.30 FTE." GT4 Table 4 states "~0.45-2.30 FTE" for the reduced ISV total and "~0.5-1.5 FTE" for Phase 3 specifically. The slight variation in upper bounds (1.45 vs 1.5 vs 2.30) is explained by rounding and the difference between the sum-of-Phase-3-FTEs (RP4a) versus the broader reduced-ISV-total (RP4b/GT4).

5. **No contradictions detected between the three files.** RP4a, RP4b, and RP4c reference the same ground truth data points and arrive at consistent conclusions. Where findings overlap (e.g., the "nearly eliminated" characterization of P4), all three files confirm rather than contradict it.

6. **Wave 5 quality assessment: High.** All three files demonstrate strong citation discipline, clear scope boundaries, evidence-based analysis, and appropriate use of cross-references. The only actionable recommendation is for RP4c to add [UNVERIFIED] tags to proposed FTE estimates for internal consistency with RP4b's practice. No files require rework.
