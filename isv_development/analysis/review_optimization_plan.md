# Three-Phase On-Prem Ratings: Review & Optimization Plan

## Purpose

Verify the accuracy of all 228 ratings (38 subsegments x 3 phases x 2 dimensions) in `three_phase_on_prem_ratings.md`, independently re-derive each rating from source data, identify missing dimensions, and produce an executive-ready optimized version with extensive sourcing, interview validation questions, and confidence scoring.

This plan was built because the file was generated in a single pass from conversation context. Independent critical review is needed to catch systematic bias, arithmetic errors, miscategorized subsegments, and unsupported claims.

## Research Parameters

- **Audience:** Mixed executive + technical leadership
- **Focus:** Accuracy verification, quality optimization, and interview validation guide for ISV SaaS deployment difficulty analysis
- **Review Model:** Verify + re-derive + expand — agents independently derive ratings from source data, compare to file, and identify gaps
- **Scope Exclusion:** Do NOT question the 4-plane framework (P1-P4 decomposition accepted as given)
- **Citation Requirement:** Verify existing citations trace to P1-P4/G1/S1 source data. Search for new sources (vendor docs, analyst reports, case studies) that support or contradict ratings. Every file must include inline citations and a Sources section.
- **Output Phases:** (1) Ground truth extraction → (2) Per-plane review with re-derivation → (3) Cross-cutting analysis → (4) Per-phase synthesis → (5) Integration + final outputs

## Agent Summary

| Wave | Agents | Count | Focus |
|------|--------|-------|-------|
| Wave 1 | GT1–GT5 | 5 | Ground truth extraction from source files |
| Wave 2 | RP1a–RP1e | 5 | P1 Control Plane review |
| Wave 3 | RP2a–RP2e | 5 | P2 Application Logic review |
| Wave 4 | RP3a–RP3d | 4 | P3 Data Plane review |
| Wave 5 | RP4a–RP4c | 3 | P4 AI Model Plane review |
| Wave 6 | CC1–CC5 | 5 | Cross-cutting analysis |
| Wave 7 | SL1a–SL1c | 3 | Synthesis Layer 1: Per-phase consolidation |
| Wave 8 | SL2a–SL2c | 3 | Synthesis Layer 2: Integration |
| Wave 9 | SL3a–SL3b | 2 | Synthesis Layer 3: Final outputs |
| **Total** | | **35** | |

## Standard Agent Instructions

CONTEXT: You are reviewing `analysis/three_phase_on_prem_ratings.md`, a file that rates 38 MECE subsegments across 4 planes (P1 Control Plane, P2 Application Logic, P3 Data Plane, P4 AI Model Plane) for 3 deployment phases (Initial Refactoring, Per-Customer Customization, Ongoing Support) on 2 dimensions (Relative Difficulty 1-5, Total Effort 1-5). The file was generated from a multi-session strategic analysis of ISV SaaS deployment difficulty across Cloud-Native, Managed K8s, and On-Premises tiers.

SOURCE FILES (ground truth):
- `analysis/P1_control_plane.md` — P1 subsegment definitions, difficulty ratings per tier, FTE estimates
- `analysis/P2_application_logic.md` — P2 subsegment definitions, difficulty ratings per tier, FTE estimates
- `analysis/P3_data_plane.md` — P3 subsegment definitions, difficulty ratings per tier, FTE estimates
- `analysis/P4_ai_model_plane.md` — P4 subsegment definitions, difficulty ratings per tier, FTE estimates
- `analysis/G1_n_services_multiplier.md` — N-services scaling model
- `analysis/S1_four_plane_synthesis.md` — Cross-plane synthesis, top 10 hardest subsegments, unified causal chain

SCOPE SPLIT (established in prior sessions):
- Customer owns: hardware (servers, GPUs, networking, storage, power, cooling), GPU infrastructure, AI models on GPUs
- ISV owns: ALL software (K8s, databases, message brokers, observability, security tooling, application code, CI/CD)
- ISV may need to customize software to each customer's hardware environment

OUTPUT REQUIREMENTS:
- Write in markdown format
- Begin with a 2-3 sentence executive summary of key findings
- Use clear section headers for each subsegment reviewed
- EVERY factual claim MUST include an inline citation — either to a source file (e.g., "P1_control_plane.md, CP-01 section") or to an external URL
- If searching for new sources, cite with direct URLs
- If you cannot find support for a claim, mark it as [UNVERIFIED] and explain why
- Include a "Sources" section at the end
- Target 1500-2500 words per review file
- For each rating reviewed, provide:
  - **Current rating:** What the file says
  - **Re-derived rating:** What you independently determine from source data
  - **Confidence:** High / Medium / Low (High = multiple source data points agree, Medium = single source or extrapolated, Low = no direct source support)
  - **Verdict:** ACCURATE / ADJUST (with direction and magnitude) / INSUFFICIENT DATA
  - **Interview question:** If confidence is Medium or Low, provide a specific question to ask a specific interviewee role to validate
- End with a "Key Findings" section of 3-5 bullet points

SCOPE DISCIPLINE: Stay strictly within your assigned scope boundary. Do NOT duplicate work assigned to other agents.

---

## Wave 1 — Ground Truth Extraction (GT1–GT5)

All agents in this wave read source files and extract authoritative data points into structured reference documents. These become the standard for plane review agents in subsequent waves.

### GT1: P1 Control Plane Source Data

**Research Question:**
What are the authoritative difficulty ratings, FTE estimates, and operational characteristics for each P1 subsegment (CP-01 through CP-10) across all three deployment tiers?

**Required Sub-Topics:**
- Per-subsegment difficulty rating for Cloud-Native, Managed K8s, and On-Premises tiers
- Per-subsegment FTE range for each tier
- Key operational characteristics that drive tier difficulty deltas
- Scaling behavior (does this subsegment scale with customer count?)
- Critical dependencies between P1 subsegments
- Notable caveats, EOL dates, or technology transitions mentioned in source

**Scope Boundary:** Extract P1 data only. Do NOT interpret or rate the three_phase_on_prem_ratings.md file. Do NOT extract P2, P3, or P4 data (covered by GT2-GT4).

**Output Path:** analysis/review/GT1_P1_ground_truth.md

---

### GT2: P2 Application Logic Source Data

**Research Question:**
What are the authoritative difficulty ratings, FTE estimates, and operational characteristics for each P2 subsegment (AL01 through AL10) across all three deployment tiers?

**Required Sub-Topics:**
- Per-subsegment difficulty rating for Cloud-Native, Managed K8s, and On-Premises tiers
- Per-subsegment FTE range for each tier
- The complexity ratio (1.0:1.3:1.7) and what drives it
- Which subsegments are tier-invariant vs tier-sensitive
- Key dependencies on P1 and P3 components
- Notable technology transitions or EOL events

**Scope Boundary:** Extract P2 data only. Do NOT extract P1, P3, or P4 data.

**Output Path:** analysis/review/GT2_P2_ground_truth.md

---

### GT3: P3 Data Plane Source Data

**Research Question:**
What are the authoritative difficulty ratings, FTE estimates, and operational characteristics for each P3 subsegment (DS1 through DS10) across all three deployment tiers?

**Required Sub-Topics:**
- Per-subsegment difficulty rating for Cloud-Native, Managed K8s, and On-Premises tiers
- Per-subsegment FTE range for each tier
- Which data services reach difficulty 5/5 on-premises
- Self-hosted vs managed service FTE differentials
- Storage and capacity scaling characteristics
- Specialist hiring requirements and lead times

**Scope Boundary:** Extract P3 data only. Do NOT extract P1, P2, or P4 data.

**Output Path:** analysis/review/GT3_P3_ground_truth.md

---

### GT4: P4 AI Model Plane Source Data

**Research Question:**
What are the authoritative difficulty ratings, FTE estimates, and operational characteristics for each P4 subsegment (S1 through S8) across all three deployment tiers, and which subsegments shift to customer scope under the customer-provides-GPU model?

**Required Sub-Topics:**
- Per-subsegment difficulty rating for all three tiers
- Per-subsegment FTE range for each tier
- Which subsegments are ISV scope vs customer scope under the agreed model
- The original (pre-scope-shift) FTE total vs the reduced ISV total
- Dependencies on customer-provided inference endpoints
- Technology stack options for each subsegment (vLLM, TGI, LiteLLM, etc.)

**Scope Boundary:** Extract P4 data only. Do NOT extract P1, P2, or P3 data.

**Output Path:** analysis/review/GT4_P4_ground_truth.md

---

### GT5: Cross-Reference & Scaling Data

**Research Question:**
What are the authoritative cross-plane aggregates, scaling models, and synthesis findings from G1 and S1 that the three-phase ratings file should be consistent with?

**Required Sub-Topics:**
- Per-service marginal FTE by tier from G1 (CN ~0.74, MK8s ~1.24, OP ~2.49)
- Viability thresholds from G1 (N=7-8, N=12)
- Cross-plane difficulty averages from S1 (CN 1.6, MK8s 2.7, OP 4.2)
- FTE ratios from S1 (1.0:2.0:4.6 at N=20)
- Top 10 hardest subsegments list from S1
- Unified causal chain and structural findings from S1
- Any gap assessments or confidence limitations noted

**Scope Boundary:** Extract G1 and S1 data only. Do NOT re-read P1-P4 source files (covered by GT1-GT4).

**Output Path:** analysis/review/GT5_cross_reference_ground_truth.md

---

## Wave 2 — P1 Control Plane Review (RP1a–RP1e)

Depends on: Wave 1 (ground truth). All agents read GT1 ground truth + the ratings file.

### RP1a: Infrastructure Core (CP-01 to CP-03)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for CP-01 (K8s Cluster Lifecycle), CP-02 (Network Fabric), and CP-03 (IAM/RBAC) accurate, and what should they be based on source data and independent analysis?

**Required Sub-Topics:**
- Re-derive each of the 18 ratings (3 subsegments x 3 phases x 2 dimensions) from GT1 ground truth
- Validate Phase 3 FTE ranges against P1 source data
- Assess whether Phase 2 per-customer ratings account for hardware heterogeneity sufficiently
- Search for external sources on K8s migration difficulty, CNI operational burden, Keycloak deployment patterns
- Provide confidence score per rating
- Generate interview questions for Medium/Low confidence ratings

**Scope Boundary:** CP-01, CP-02, CP-03 only. Do NOT review CP-04 through CP-10 (covered by RP1b, RP1c).

**Output Path:** analysis/review/RP1a_P1_infrastructure_core.md

---

### RP1b: Security & Delivery (CP-04 to CP-06)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for CP-04 (Secrets/Certs/PKI), CP-05 (Observability Infrastructure), and CP-06 (CI/CD Pipeline) accurate?

**Required Sub-Topics:**
- Re-derive each of the 18 ratings from GT1 ground truth
- Validate Phase 3 FTE ranges against source data
- Assess Vault operational burden claims (5-node Raft, seal/unseal, FIPS 140-3)
- Validate observability stack sizing claims (500K+ active time series, 3KB RAM each)
- Assess GitOps per-customer complexity claims
- Search for external sources on Vault operations, Prometheus/Grafana operational costs, ArgoCD at scale
- Confidence scores and interview questions for each rating

**Scope Boundary:** CP-04, CP-05, CP-06 only.

**Output Path:** analysis/review/RP1b_P1_security_delivery.md

---

### RP1c: Operations & Compliance (CP-07 to CP-10)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for CP-07 (Deploy Lifecycle), CP-08 (Disaster Recovery), CP-09 (Compliance Automation), and CP-10 (Security Operations) accurate?

**Required Sub-Topics:**
- Re-derive each of the 24 ratings from GT1 ground truth
- Validate the "linear scaling problem" claim for CP-07 (N customers = N deployment cycles)
- Assess DR cadence and effort claims
- Validate compliance evidence generation burden (FedRAMP, SOC2, HIPAA)
- Search for external sources on multi-customer deployment orchestration, compliance automation tools
- Assess whether CP-08 and CP-09 Phase 1 TE ratings (both 3) are too low given the complexity described
- Confidence scores and interview questions

**Scope Boundary:** CP-07, CP-08, CP-09, CP-10 only.

**Output Path:** analysis/review/RP1c_P1_operations_compliance.md

---

### RP1d: P1 Phase 2 Per-Customer Deep-Dive

**Research Question:**
Are the Phase 2 (per-customer customization) ratings for all 10 P1 subsegments too low, and what does the evidence say about actual per-customer infrastructure adaptation effort?

**Required Sub-Topics:**
- Compare Phase 2 P1 average (RD 3.0, TE 2.9) to real-world per-customer deployment effort data
- Search for case studies or reports on ISV per-customer K8s deployment customization
- Assess whether network heterogeneity (CP-02 rated RD=4) is the right subsegment to rate highest
- Evaluate the 6-14 person-weeks per customer estimate — is this plausible for a complex SaaS platform?
- Identify which subsegments are most sensitive to customer hardware diversity
- Generate interview questions specifically targeting per-customer deployment experience

**Scope Boundary:** Phase 2 ratings for P1 only. Do NOT review Phase 1 or Phase 3 (covered by RP1a-c).

**Output Path:** analysis/review/RP1d_P1_phase2_deep_dive.md

---

### RP1e: P1 Phase 1 Effort Estimate Validation

**Research Question:**
Is the Phase 1 effort estimate of 40-80 person-months for P1 Control Plane initial refactoring plausible, and what external evidence supports or contradicts it?

**Required Sub-Topics:**
- Decompose the 40-80 person-month estimate into per-subsegment contributions
- Search for case studies of cloud-to-on-prem migration timelines (Kubernetes platform builds)
- Compare to known platform engineering team build timelines (how long does it take to build a K8s platform from scratch?)
- Assess whether the TE ratings (avg 4.0) justify the aggregate estimate
- Validate the conversion from TE ratings to person-months — is the rating scale calibrated correctly?
- Identify the weakest assumptions in the estimate

**Scope Boundary:** Phase 1 effort for P1 only. Do NOT review Phase 2/3 or other planes' effort estimates.

**Output Path:** analysis/review/RP1e_P1_phase1_effort.md

---

## Wave 3 — P2 Application Logic Review (RP2a–RP2e)

Depends on: Wave 1 + Wave 2 (P1 findings may inform P2 boundary questions).

### RP2a: Service Architecture & Data Access (AL01 to AL05)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for AL01 (Service Decomposition), AL02 (Business Logic), AL03 (API Gateway), AL04 (Data Access/ORM), and AL05 (Background Jobs/Async/EDA) accurate?

**Required Sub-Topics:**
- Re-derive each of the 30 ratings from GT2 ground truth
- Validate that AL02 is truly RD=1 across all phases — is business logic really tier-invariant?
- Assess AL05 ratings — Kafka vs SQS at application layer, Temporal vs Step Functions migration
- Validate Phase 3 FTE ranges against source data
- Search for external sources on microservice migration patterns, event-driven architecture self-hosting costs
- Confidence scores and interview questions

**Scope Boundary:** AL01 through AL05 only. Do NOT review AL06-AL10.

**Output Path:** analysis/review/RP2a_P2_service_architecture.md

---

### RP2b: Resilience, AI & Testing (AL06 to AL10)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for AL06 (Resilience), AL07 (Multi-Tenant), AL08 (Observability Instrumentation), AL09 (AI/ML Orchestration), and AL10 (Testing) accurate?

**Required Sub-Topics:**
- Re-derive each of the 30 ratings from GT2 ground truth
- Validate AL09 — is the "rapidly evolving ecosystem" claim well-supported? Is Phase 3 RD=3, TE=4 right?
- Validate AL10 Phase 3 — does the test matrix really scale linearly with N customers?
- Assess whether AL07 (multi-tenant isolation) is correctly rated at 1/1 for Phase 2 — does hardware heterogeneity never affect multi-tenant logic?
- Search for external sources on AI agent stack maintenance burden, integration testing across K8s versions
- Confidence scores and interview questions

**Scope Boundary:** AL06 through AL10 only. Do NOT review AL01-AL05.

**Output Path:** analysis/review/RP2b_P2_resilience_ai_testing.md

---

### RP2c: P2 Systematic Divergence Investigation

**Research Question:**
Is the systematic RD-TE divergence in P2 (avg RD 1.6 vs avg TE 2.1 across all phases, widening to 1.8 vs 2.7 in Phase 3) a real phenomenon or an artifact of how the rating scales are defined?

**Required Sub-Topics:**
- Independently calculate the RD-TE gap for every P2 subsegment across all 3 phases
- Assess whether the divergence is driven by a few outliers (AL02, AL05, AL09) or is truly systematic
- Evaluate whether the TE scale itself is biased for application logic (does a "large codebase" automatically get high TE even if the work is routine?)
- Compare P2 divergence pattern to P1 and P3 — are those planes also divergent but in different directions?
- Search for industry analysis on application logic cost vs infrastructure cost in deployment tier migrations
- Recommend whether the "planning trap" framing is accurate or overstated

**Scope Boundary:** P2 divergence analysis only. Do NOT re-derive individual subsegment ratings (covered by RP2a, RP2b).

**Output Path:** analysis/review/RP2c_P2_divergence_investigation.md

---

### RP2d: P1/P2 Subsegment Boundary Analysis

**Research Question:**
Are there any subsegments currently assigned to P1 (Control Plane) that should be in P2 (Application Logic), or vice versa, based on the MECE boundary criteria established in the source files?

**Required Sub-Topics:**
- Read P1 and P2 MECE boundary definitions from source files
- Apply the three boundary criteria: organizational owner, change driver, failure mode
- Evaluate CP-06 (CI/CD) — is this truly "control plane" or is it more "application delivery"?
- Evaluate AL08 (Observability Instrumentation) vs CP-05 (Observability Infrastructure) — is the boundary correctly drawn?
- Evaluate AL03 (API Gateway) — could this be considered control plane infrastructure?
- Evaluate CP-03 (IAM/RBAC) — does application-level authorization belong in P2?
- Propose any reclassifications with full justification

**Scope Boundary:** P1/P2 boundary only. Do NOT evaluate P3/P4 boundaries (P3 and P4 have clearer scope separation).

**Output Path:** analysis/review/RP2d_P1P2_boundary_analysis.md

---

### RP2e: P2 Completeness & Missing Subsegments

**Research Question:**
Are there application logic concerns that should be tracked as subsegments in P2 but are currently missing from the 10-subsegment MECE framework?

**Required Sub-Topics:**
- Review the current 10 P2 subsegments for completeness against common SaaS application architecture patterns
- Assess whether "Configuration Management / Feature Flags" deserves its own subsegment (currently embedded in AL05)
- Assess whether "API Versioning / Backward Compatibility" is adequately covered
- Assess whether "Notification / Communication Services" (email, SMS, push) should be a subsegment
- Search for industry-standard SaaS application component taxonomies to compare against
- If missing subsegments are found, propose their ratings across all 3 phases

**Scope Boundary:** P2 completeness only. Do NOT evaluate P1, P3, or P4 completeness (P1 is handled by RP2d boundary analysis; P3 and P4 are reviewed in their respective waves).

**Output Path:** analysis/review/RP2e_P2_completeness.md

---

## Wave 4 — P3 Data Plane Review (RP3a–RP3d)

Depends on: Wave 1 + Waves 2-3 (may reference P1/P2 findings for cross-plane consistency).

### RP3a: Traditional Data Services (DS1 to DS5)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for DS1 (Relational DB HA), DS2 (NoSQL), DS3 (Caching), DS4 (Object Storage), and DS5 (Simple Messaging) accurate?

**Required Sub-Topics:**
- Re-derive each of the 30 ratings from GT3 ground truth
- Validate DS1 FTE ranges (1.5-3.0 ongoing) against known PostgreSQL HA operational costs
- Assess whether DS3 (Caching) and DS4 (Object Storage) Phase 1 ratings of RD=3/2 and RD=2/2 are correctly differentiated
- Validate Phase 2 ratings — are per-customer tuning requirements accurately captured?
- Search for external sources on self-hosted PostgreSQL HA, Redis, MinIO operational burden
- Confidence scores and interview questions

**Scope Boundary:** DS1 through DS5 only.

**Output Path:** analysis/review/RP3a_P3_traditional_data.md

---

### RP3b: Streaming, Search & AI Data (DS6 to DS10)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for DS6 (Kafka), DS7 (Search), DS8 (Vector DB), DS9 (Embedding Pipeline), and DS10 (RAG Pipeline) accurate?

**Required Sub-Topics:**
- Re-derive each of the 30 ratings from GT3 ground truth
- Validate DS6 Kafka claim: "13-26 hrs/week self-hosted vs 2-3 hrs/week MSK"
- Assess DS9 Phase 1 ratings — source file rated on-prem at 5/5 but ratings file shows RD=3, TE=3 citing customer-scope reduction. Is this reduction correctly applied?
- Validate DS10 Phase 3 [D] flag — is the RAG pipeline divergence (RD=3, TE=4) real?
- Search for external sources on self-hosted Kafka operational costs, Milvus/Qdrant operations, RAG pipeline maintenance
- Confidence scores and interview questions

**Scope Boundary:** DS6 through DS10 only.

**Output Path:** analysis/review/RP3b_P3_streaming_ai_data.md

---

### RP3c: P3 Phase 1 + Phase 2 Effort Validation

**Research Question:**
Are the P3 Phase 1 effort estimate (20-40 person-months) and Phase 2 per-customer estimate (2-4 person-weeks) plausible?

**Required Sub-Topics:**
- Decompose Phase 1 estimate into per-subsegment contributions
- Search for case studies on standing up self-hosted data service stacks (PostgreSQL HA + Kafka + Redis + MinIO + vector DB)
- Compare to known data platform team build timelines
- Assess Phase 2 claim that data service per-customer effort is primarily "tuning" — is this accurate for stateful services?
- Validate whether 2-4 person-weeks captures the true effort of deploying 10 data services to a new customer environment
- Interview questions for data platform engineers

**Scope Boundary:** P3 Phase 1 and Phase 2 effort estimates only.

**Output Path:** analysis/review/RP3c_P3_effort_validation.md

---

### RP3d: P3 FTE Range & Scaling Accuracy

**Research Question:**
Do the Phase 3 FTE ranges for P3 subsegments (total ~10-18 FTE) accurately reflect the source data, and are the "Scales with N?" classifications correct?

**Required Sub-Topics:**
- Compare each Phase 3 FTE range in the ratings file to the FTE data in P3_data_plane.md source
- Verify the "Scales with N?" classification for each subsegment
- Assess whether "Partial" scaling is accurately applied (what does "partial" actually mean for DS2, DS3, DS4, DS5, DS7?)
- Validate the total FTE range (~10-18) by summing individual subsegment ranges
- Check whether the FTE ranges from G1 scaling model are consistent with P3 Phase 3 data
- Identify any subsegments where the FTE range seems too narrow or too wide

**Scope Boundary:** P3 Phase 3 FTE data only.

**Output Path:** analysis/review/RP3d_P3_fte_scaling.md

---

## Wave 5 — P4 AI Model Plane Review (RP4a–RP4c)

Depends on: Wave 1 + Waves 2-4.

### RP4a: ISV-Scope Subsegments (S1, S6, S7, S8)

**Research Question:**
Are the Phase 1, Phase 2, and Phase 3 ratings for the 4 ISV-scope P4 subsegments (S1 Managed API Integration, S6 Model Routing, S7 Inference Monitoring, S8 Model Lifecycle) accurate?

**Required Sub-Topics:**
- Re-derive each of the 24 ratings from GT4 ground truth
- Validate the reduction from original source difficulty levels to the "calling customer endpoints" model
- Assess whether S1 Phase 1 RD=1 is correct — is swapping from Bedrock/Azure OpenAI to customer inference endpoints truly trivial?
- Validate S6/S7 Phase 3 FTE ranges (0.2-0.5 and 0.1-0.5) — are these too low for production monitoring?
- Search for external sources on LiteLLM operations, inference endpoint monitoring patterns
- Confidence scores and interview questions

**Scope Boundary:** S1, S6, S7, S8 only. Do NOT review S2-S5 (customer scope).

**Output Path:** analysis/review/RP4a_P4_isv_scope.md

---

### RP4b: Customer Scope Exclusion Validation

**Research Question:**
Is the exclusion of S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) from ISV scope correctly applied, and are there any hidden ISV responsibilities that the exclusion masks?

**Required Sub-Topics:**
- Review the original P4 source file's S2-S5 descriptions and FTE data
- Assess whether ISVs truly have ZERO responsibility for these under the customer-provides-GPU model
- Identify edge cases: What if the customer's inference engine has compatibility issues with the ISV's API calls?
- What if the customer's GPU allocation is insufficient — whose problem is that?
- Are there ISV support responsibilities (documentation, compatibility testing, troubleshooting guides) not captured?
- Search for ISV-on-prem deployment models where the ISV does retain some inference engine responsibility

**Scope Boundary:** S2-S5 customer scope validation only.

**Output Path:** analysis/review/RP4b_P4_scope_exclusion.md

---

### RP4c: P4 Completeness & Missing AI Concerns

**Research Question:**
Are there AI-model-related operational concerns that are missing from the P4 framework entirely, or that are split between P2/P3/P4 in a way that creates gaps?

**Required Sub-Topics:**
- Assess whether "AI Safety / Guardrails" should have a P4 subsegment (currently excluded in source — noted as "separate security/trust domain")
- Assess whether "Prompt Management / Caching" is adequately covered (excluded in P4 source, partially in P2's AL09)
- Check if "Model Cost Attribution / Chargeback" is a missing operational concern
- Evaluate whether the P2/P3/P4 boundary for AI responsibilities creates any gaps (AL09 in P2 vs DS9/DS10 in P3 vs S1-S8 in P4)
- Search for emerging ISV AI operations frameworks to compare against
- If gaps found, propose subsegments and rate them

**Scope Boundary:** P4 completeness and AI gap analysis only.

**Output Path:** analysis/review/RP4c_P4_completeness.md

---

## Wave 6 — Cross-Cutting Analysis (CC1–CC5)

Depends on: Waves 1-5 (all plane reviews complete).

### CC1: Mathematical Consistency Audit

**Research Question:**
Are all averages, totals, summary matrices, and FTE ranges in the ratings file arithmetically correct?

**Required Sub-Topics:**
- Verify every plane average (RD and TE) for each phase by summing and dividing subsegment ratings
- Verify the Grand Summary matrices (Section 8) match the per-phase summary tables
- Verify the "All-Phase Avg" column is correctly calculated
- Check that Phase 1 effort estimates (person-months) are consistent with the TE ratings and the TE scale definitions
- Check that Phase 2 effort estimates (person-weeks) are internally consistent
- Verify the P1 = ~60% claim for Phase 2 is arithmetically supported
- Check that Phase 3 FTE totals (sum of subsegment ranges) match the stated totals

**Scope Boundary:** Arithmetic only. Do NOT assess whether the ratings themselves are correct — only whether the math is right.

**Output Path:** analysis/review/CC1_math_audit.md

---

### CC2: Divergence Analysis Re-Derivation

**Research Question:**
Are all [D] divergence flags correctly placed, and are there any missed divergences where RD and TE differ significantly but no flag was applied?

**Required Sub-Topics:**
- Independently calculate RD-TE gap for every subsegment across all 3 phases (114 cells)
- Apply the [D] threshold (gap >= 2 points) and compare to the file's [D] flags
- Check for near-miss divergences (gap = 1.5-1.9) that should be noted
- Validate the "P2 systematic divergence" claim — is the +0.9 gap real and systematic?
- Assess the divergence analysis narrative (Section 7) for accuracy
- Check whether any P1 or P3 subsegments have hidden divergences not flagged

**Scope Boundary:** Divergence analysis only. Do NOT re-derive the underlying ratings.

**Output Path:** analysis/review/CC2_divergence_rederivation.md

---

### CC3: Cross-Phase Consistency

**Research Question:**
Do the ratings for each subsegment tell a logically consistent story across the three phases, and are there any contradictions where a subsegment gets harder in Phase 2 than Phase 1 without explanation?

**Required Sub-Topics:**
- For each of the 38 subsegments, trace the RD and TE trajectory across Phase 1 → Phase 2 → Phase 3
- Flag any subsegment where Phase 2 > Phase 1 on either dimension (should be rare — per-customer customization is usually a subset of the initial build)
- Flag any subsegment where Phase 3 < Phase 2 (ongoing support should generally equal or exceed per-customer customization)
- Assess whether Phase 1 → Phase 3 trajectories make sense (one-time build vs ongoing operations)
- Identify the 5 most inconsistent cross-phase trajectories and explain why they are problematic

**Scope Boundary:** Cross-phase trajectory analysis only. Do NOT re-derive individual ratings.

**Output Path:** analysis/review/CC3_cross_phase_consistency.md

---

### CC4: Customer vs ISV Scope Consistency

**Research Question:**
Is the customer-owns-hardware / ISV-owns-software scope split consistently applied across all 4 planes, all 3 phases, and all 38 subsegments?

**Required Sub-Topics:**
- Check every subsegment for any note or rating that implies ISV hardware responsibility
- Verify P4 S2-S5 are consistently marked as customer scope in all 3 phases
- Check whether any P1 or P3 subsegment descriptions inadvertently assume the ISV manages hardware (e.g., "rack space" or "power")
- Assess whether Phase 2 descriptions properly frame customization as "software adaptation to customer hardware" not "hardware provisioning"
- Check that DS9 (Embedding Pipeline) correctly reflects customer-provides-GPU scope
- Identify any scope ambiguities that need clarification

**Scope Boundary:** Scope consistency only.

**Output Path:** analysis/review/CC4_scope_consistency.md

---

### CC5: Missing Risks & Dynamics

**Research Question:**
What risks, dynamics, or operational concerns does the three-phase analysis miss entirely or significantly underweight?

**Required Sub-Topics:**
- Assess whether "organizational change management" (ISV team restructuring for on-prem support) is captured
- Assess whether "customer communication overhead" (coordination for upgrades, incidents) is captured
- Evaluate whether "vendor lock-in reversal cost" (extracting from cloud-specific APIs) is adequately reflected in Phase 1
- Check for missing security risks (supply chain security for self-hosted components, CVE response velocity)
- Assess whether "talent acquisition difficulty" for self-hosted specializations is captured
- Check whether "regulatory variance across customers" is adequately captured in Phase 2/3
- Search for published on-prem deployment failure modes or risk analyses

**Scope Boundary:** Gap identification only. Do NOT re-derive any existing ratings.

**Output Path:** analysis/review/CC5_missing_risks.md

---

## Wave 7 — Synthesis Layer 1: Per-Phase Consolidation (SL1a–SL1c)

Depends on: Waves 1-6 (all reviews and cross-cutting analysis complete).

### SL1a: Phase 1 Consolidated Findings

**Research Question:**
Across all plane reviews and cross-cutting analyses, what are the consolidated findings about Phase 1 (Initial Refactoring) accuracy, and what changes should be made?

**Required Sub-Topics:**
- Consolidate all Phase 1 findings from RP1a-e, RP2a-b, RP3a-b, RP4a across all 4 planes
- List every rating that review agents recommend adjusting (with direction and magnitude)
- Consolidate Phase 1 effort estimate findings from RP1e, RP3c
- Synthesize interview questions related to Phase 1
- Propose a revised Phase 1 summary table with adjusted ratings and effort estimates
- Executive summary of Phase 1 accuracy assessment

**Scope Boundary:** Phase 1 findings only. Reference but do not duplicate Phase 2/3 work.

**Output Path:** analysis/review/SL1a_phase1_consolidated.md

---

### SL1b: Phase 2 Consolidated Findings

**Research Question:**
What are the consolidated findings about Phase 2 (Per-Customer Customization) accuracy, and what changes should be made?

**Required Sub-Topics:**
- Consolidate all Phase 2 findings from RP1d, RP2a-b, RP3a-c, RP4a
- List every Phase 2 rating that review agents recommend adjusting
- Consolidate Phase 2 effort estimate findings (are the per-customer person-weeks estimates too low?)
- Synthesize interview questions related to per-customer deployment experience
- Propose a revised Phase 2 summary table
- Executive summary of Phase 2 accuracy assessment

**Scope Boundary:** Phase 2 findings only.

**Output Path:** analysis/review/SL1b_phase2_consolidated.md

---

### SL1c: Phase 3 Consolidated Findings

**Research Question:**
What are the consolidated findings about Phase 3 (Ongoing Support) accuracy, and what changes should be made?

**Required Sub-Topics:**
- Consolidate all Phase 3 findings from RP1a-c, RP2a-b, RP3a-b/d, RP4a
- List every Phase 3 rating and FTE range that review agents recommend adjusting
- Consolidate the "Scales with N?" classification accuracy from RP3d and CC3
- Synthesize the divergence investigation findings from RP2c and CC2 into Phase 3 implications
- Propose a revised Phase 3 summary table with adjusted ratings, FTEs, and scaling classifications
- Executive summary of Phase 3 accuracy assessment

**Scope Boundary:** Phase 3 findings only.

**Output Path:** analysis/review/SL1c_phase3_consolidated.md

---

## Wave 8 — Synthesis Layer 2: Integration (SL2a–SL2c)

Depends on: Wave 7 (per-phase consolidation complete).

### SL2a: Executive Narrative Evaluation

**Research Question:**
Are the 6 key findings in Section 8 of the ratings file well-supported by the underlying data, and how should the executive narrative be improved for a mixed audience?

**Required Sub-Topics:**
- Evaluate each of the 6 key findings against the review evidence
- Assess whether the "P1 dominates" finding is still accurate after rating adjustments
- Assess whether the "P2 systematic divergence" finding survives the RP2c investigation
- Evaluate the "P4 nearly eliminated" finding against RP4b scope exclusion analysis
- Assess the storytelling arc — does it flow logically for executives while being defensible for technical audiences?
- Propose revisions to the key findings based on review evidence
- Draft an improved executive summary section

**Scope Boundary:** Executive narrative and key findings only. Do not re-derive any ratings.

**Output Path:** analysis/review/SL2a_executive_narrative.md

---

### SL2b: Consolidated Interview Validation Guide

**Research Question:**
What is the complete set of interview questions needed to validate Medium and Low confidence ratings, organized by interviewee role?

**Required Sub-Topics:**
- Collect all interview questions from all review agent outputs (RP1a-e, RP2a-b, RP3a-d, RP4a-c)
- Organize by interviewee role (Platform Engineer, SRE, Application Developer, Data Engineer, AI/ML Engineer, VP Engineering, CTO)
- Prioritize by confidence impact — which questions would change the most ratings if answered?
- Include context for each question (why this matters, what rating it validates)
- Suggest interview format (structured vs open-ended, estimated time per role)
- Identify the minimum viable interview set (which 10 questions are most important?)

**Scope Boundary:** Interview guide only.

**Output Path:** analysis/review/SL2b_interview_guide.md

---

### SL2c: Cross-Phase Integration & Reconciliation

**Research Question:**
How do the per-phase findings (SL1a-c) interact, and what cross-phase insights emerge from the reconciled review data?

**Required Sub-Topics:**
- Reconcile any conflicts between per-phase findings (e.g., a rating adjustment in Phase 1 that contradicts Phase 3 assessment)
- Assess the overall accuracy of the three-phase model — is the phase decomposition itself sound?
- Evaluate whether the "two cost types in Phase 3" finding (linear vs fixed) is accurately captured
- Assess the transition from Phase 1 → Phase 2 → Phase 3 in terms of team composition and skill requirements
- Identify the single most important finding across all reviews
- Draft the structural changes needed for the revised file

**Scope Boundary:** Cross-phase integration only. Do not duplicate per-phase findings.

**Output Path:** analysis/review/SL2c_cross_phase_integration.md

---

## Wave 9 — Synthesis Layer 3: Final Outputs (SL3a–SL3b)

Depends on: Wave 8 (integration complete). Sequential: SL3a must complete before SL3b.

### SL3a: Final Review Report

**Research Question:**
What is the complete, consolidated review report covering all findings, recommendations, confidence assessments, and interview validation priorities?

**Required Sub-Topics:**
- Executive summary (1 page): overall accuracy assessment, most important findings, critical changes needed
- Methodology section: how the review was conducted (35 agents, 9 waves, verify + re-derive + expand)
- Findings by plane: consolidated accuracy assessment for P1, P2, P3, P4
- Findings by phase: consolidated accuracy assessment for Phase 1, Phase 2, Phase 3
- Cross-cutting findings: math errors, divergence analysis, scope consistency, missing risks
- Recommended rating changes: complete table of all proposed adjustments with before/after and justification
- Confidence map: visual summary of confidence levels across all 228 ratings
- Interview priorities: top 10 validation questions with expected impact

**Scope Boundary:** Final report synthesis only. Do NOT generate the revised ratings file (that is SL3b).

**Output Path:** analysis/review/SL3a_final_review_report.md

---

### SL3b: Revised Three-Phase On-Prem Ratings v2

**Research Question:**
Based on all review findings and approved changes, what should the revised `three_phase_on_prem_ratings_v2.md` look like?

**Required Sub-Topics:**
- Apply all recommended rating adjustments from the review report
- Update all averages, totals, and summary matrices to reflect changes
- Add confidence scores to each rating (parenthetical: H/M/L)
- Expand notes with sourced explanations
- Add an "Interview Validation" column in Phase 3 tables where applicable
- Update the divergence analysis with any new or removed [D] flags
- Update the key findings to reflect review-informed conclusions
- Add a "Changes from v1" section documenting all modifications with rationale
- Recalculate all effort estimates based on adjusted ratings

**Scope Boundary:** Produce the complete revised file. Do NOT include review methodology or agent-level findings (that's in SL3a).

**Output Path:** analysis/three_phase_on_prem_ratings_v2.md

---

## Quality Gates

### G1: Per-Wave File Completeness
- All expected files exist at correct paths
- Each file has: executive summary, structured sections, sources section
- Word count within 1500-2500 range

### G2: Per-Agent Citation Quality
- Inline citations present (minimum 5 per file — either to source files or external URLs)
- Sources section with all references listed
- No orphaned [UNVERIFIED] without explanation

### G3: Content Review (post-wave)
- Dispatch review agent to check: findings are substantive (not rubber-stamps), confidence scores justified, interview questions are specific and actionable, re-derived ratings show independent thought
- Score per file: PASS | MINOR_ISSUES | REWORK_NEEDED

### G4: Coverage Check (after all plane review waves)
- All 38 subsegments have been reviewed across all 3 phases
- Every Medium/Low confidence rating has an associated interview question
- Cross-cutting agents have covered all 5 assigned dimensions

### G5: Pre-Synthesis Readiness (after Wave 6)
- All review files complete and passing G1+G2
- Rating adjustment recommendations are specific (not vague)
- No critical conflicts between plane review findings
- Math audit has been completed

### Gap Analysis Checkpoints
- After Wave 1: Verify ground truth extraction is complete and internally consistent
- After Wave 2: Check P1 coverage and initial findings quality
- After Wave 3: Check P2 coverage, validate boundary analysis approach
- After Wave 4: Check P3 coverage
- After Wave 5: Check P4 coverage, verify scope exclusion analysis
- After Wave 6: Full coverage check before synthesis

---

## Sources and Confidence

| Data Source | Role in Review |
|---|---|
| P1_control_plane.md | Ground truth for CP-01 to CP-10 |
| P2_application_logic.md | Ground truth for AL01 to AL10 |
| P3_data_plane.md | Ground truth for DS1 to DS10 |
| P4_ai_model_plane.md | Ground truth for S1 to S8 |
| G1_n_services_multiplier.md | Scaling model validation |
| S1_four_plane_synthesis.md | Cross-plane aggregate validation |
| External web sources | Independent corroboration and contradiction |
