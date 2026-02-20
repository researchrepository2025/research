# RP4c — P4 AI Model Plane: Completeness and Gap Analysis

**Role:** P4 Completeness Review Agent
**Date:** 2026-02-19
**Source Files:** `analysis/P4_ai_model_plane.md`, `analysis/S1_four_plane_synthesis.md`, `analysis/review/GT4_P4_ground_truth.md`, `analysis/review/RP2b_P2_resilience_ai_testing.md`, `analysis/review/RP2e_P2_completeness.md`, `analysis/review/GT5_cross_reference_ground_truth.md`
**Scope:** P4 completeness and AI operational gap analysis only. P1, P2, and P3 boundary items are referenced but not rated here.

---

## Executive Summary

The P4 AI Model Plane (S1–S8) is structurally complete for its stated scope but contains three explicit exclusions — AI Safety/Guardrails, Prompt Management/Caching, and Model Cost Attribution — that constitute genuine operational gaps when evaluated against current ISV AI operations practice. Additionally, the P2/P3/P4 boundary design creates one confirmed coverage gap: per-customer AI cost attribution belongs to no plane with sufficient specificity, making it invisible to planners despite being a top LLMOps operational concern in 2025. Two emerging LLMOps framework taxonomies — the enterprise LLMOps operational model and the AI safety layer model — identify these three areas as first-class ISV operational concerns that warrant explicit subsegment treatment in P4.

---

## 1. Current P4 Framework: Explicit Exclusions Under Review

The P4 source file names three operational concerns as explicitly excluded from scope:

[FACT]
"Explicitly Excluded: AI safety, guardrails, and content filtering (separate security/trust domain); Prompt engineering, prompt caching, and prompt management"
— `P4_ai_model_plane.md` §1, Explicitly Excluded

[FACT]
The P4 source does not name Model Cost Attribution / Chargeback as an exclusion. It appears in the implicit scope of S1 ("Cost tracking and per-customer token attribution" is listed as an ISV ownership item), but no subsegment is dedicated to this operational function.
— `P4_ai_model_plane.md` §3, S1 ("What the ISV owns")

[FACT]
"P4 (AI Model Plane) is nearly eliminated under the customer-provides-GPU-and-models scope. All-phase average of RD 1.3 / TE 1.7. The ISV's AI-related effort is in P2 (agent orchestration) and P3 (embedding/RAG pipelines), not P4."
— `three_phase_on_prem_ratings.md` §8 (Grand Summary, Key Finding 4)

This finding sharpens the gap question: if P4 effort is nearly eliminated under the scope split, any functional concern not housed in P4 must be housed explicitly in P2 or P3 — or it falls into a gap.

---

## 2. Gap Assessment A: AI Safety / Guardrails

### 2.1 Current Classification

The P4 source explicitly excludes AI safety and guardrails as a "separate security/trust domain."

[FACT]
"AI safety, guardrails, and content filtering (separate security/trust domain)" — listed as Explicitly Excluded from P4 scope.
— `P4_ai_model_plane.md` §1, Explicitly Excluded

The P2 source (AL09) does reference guardrail integration as part of AI/ML orchestration:

[FACT]
"On-premises AI agent infrastructure requires 7 distinct platform layers: tool registry, sandboxed execution, state management, workflow orchestration, metering, security sandboxing, GPU scheduling."
— `GT4_P4_ground_truth.md`, citing GT2/RP2b, AL09 Key Operational Characteristics, `F38: On-Premises AI Agent Infrastructure`

[FACT]
The S1 synthesis Top 10 rationale for AL09 (Rank 1) names "LlamaFirewall guardrails" as one of six platform components the ISV must self-host on-premises.
— `S1_four_plane_synthesis.md` §2, Rank 1 row

### 2.2 Current Industry Landscape for Self-Hosted Guardrails

[FACT]
LlamaFirewall is an open-source security-focused guardrail framework published in May 2025, designed as "a final layer of defense against security risks associated with AI Agents" integrating prompt injection mitigation in a layered pipeline.
— arXiv 2505.03574, LlamaFirewall paper
URL: https://arxiv.org/abs/2505.03574

[FACT]
OpenGuardrails is described as "a fully open-source and deployable system" enabling users to "deploy privately within their infrastructure or extend the system for custom development." The OpenGuardrails-Text-2510 model is fine-tuned from a 14B dense base model and quantized via GPTQ to 3.3B parameters.
— arXiv 2510.19169, OpenGuardrails paper
URL: https://arxiv.org/html/2510.19169

[FACT]
NVIDIA NeMo Guardrails is described as "an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems" and "a scalable platform for orchestrating AI guardrails to safeguard generative AI and LLM applications."
— NVIDIA Developer, NeMo Guardrails
URL: https://developer.nvidia.com/nemo-guardrails

[FACT]
"Organizations deploy AI across SaaS platforms, cloud infrastructure, and on premises systems, with each deployment surface introducing risk including sensitive data exposure, unauthorized decision making, compliance violations, and reputational damage from biased or harmful outputs."
— Obsidian Security, "AI Guardrails: Enforcing Safety Without Slowing Innovation"
URL: https://www.obsidiansecurity.com/blog/ai-guardrails

[FACT]
Enterprise LLMOps frameworks treat guardrails as a distinct operational layer: "Input guardrails detect prompt injection attempts, jailbreak techniques, and malicious content before processing, while output guardrails score for hallucinations, mask PII, and filter toxic responses."
— ACI Infotech, "Enterprise LLMOps: Scalable, Governed and Cost-Effective GenAI"
URL: https://www.aciinfotech.com/blogs/enterprise-llmops-scalable-governed-cost-effective-genai

### 2.3 Boundary Analysis: Where Does Guardrails Belong?

The classification of guardrails as a "separate security/trust domain" is defensible in theory but operationally incomplete for the following reasons:

**The current plane boundary allocates guardrails to neither P2 nor P4 with sufficient specificity.**

- AL09 (P2) references LlamaFirewall in its infrastructure stack but does not rate the guardrail component independently. The AL09 scope covers "agent orchestration code, LangGraph, guardrails, MCP" as a combined unit. See `RP2b_P2_resilience_ai_testing.md` §AL09 Phase 1.
- CP-10 (P1 Security Operations) covers SOC functions, not application-layer AI content filtering.
- P4 explicitly excludes it.

**On-premises operational reality:** A self-hosted guardrail layer (LlamaFirewall, OpenGuardrails, NeMo Guardrails) is a distinct software component with its own:
- Deployment and version management (separate from the inference engine)
- Inference compute requirements (OpenGuardrails-Text-2510 is a 3.3B parameter model requiring its own GPU allocation)
- Latency SLA impact (guardrail inference adds latency between the application call and the model response)
- Policy management and audit logging requirements

[FACT]
"Guardrailing needs to be part of a broader operational strategy, one that includes structured validation, observability, and feedback loops to ensure performance and safety at scale."
— Swept AI, "Deploying Enterprise LLM Applications: Inference, Guardrails, and Observability"
URL: https://www.swept.ai/post/deploying-enterprise-llm-applications-inference-guardrails-observability

### 2.4 Verdict and Proposed Subsegment

AI Safety / Guardrails is a genuine gap in P4. It is currently diffused across AL09 (where it appears as one item in a seven-component infrastructure list) without an independent rating. The on-premises tier cost differs materially from cloud-native because:

- Cloud-native: AWS Bedrock Guardrails, Azure AI Content Safety, and Vertex AI Safety are fully managed APIs. The ISV calls a safety-check endpoint with no infrastructure ownership.
- On-premises: The ISV must deploy and operate a self-hosted guardrail model (e.g., OpenGuardrails-Text-2510 at 3.3B parameters) or integrate NeMo Guardrails / LlamaFirewall as a sidecar, with its own GPU or CPU compute, latency budget, policy storage, and version management.

**Proposed Subsegment: S9 — AI Safety and Guardrail Operations**

Definition: Deploying, operating, and maintaining AI content safety and guardrail systems that intercept requests before model inference and filter outputs before delivery to users. Includes input guardrails (prompt injection detection, PII filtering, policy enforcement), output guardrails (hallucination scoring, toxicity filtering, compliance assertion), and the operational lifecycle of the guardrail model or rule engine itself.

What the ISV owns:
- Guardrail model or rule engine deployment (LlamaFirewall, NeMo Guardrails, OpenGuardrails, or custom)
- Policy definition, versioning, and audit logging
- Latency budget allocation for guardrail inference
- Integration with customer-specific content policies (regulated industry terms, customer-specific PII definitions)
- Guardrail bypass detection and alert runbooks

**Proposed Difficulty Ratings: S9 — AI Safety and Guardrail Operations**

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **2** | Managed safety APIs (Bedrock Guardrails, Azure AI Content Safety) abstract the model. ISV configures policies, thresholds, and PII patterns via API. No infrastructure. Rated 2 (not 1) because policy management, audit trail requirements, and latency SLA integration require dedicated engineering. |
| Managed K8s | **3** | ISV deploys NeMo Guardrails or LlamaFirewall as a K8s sidecar or gateway component. Adds Helm-managed deployment, versioning, and integration with KServe inference pipeline. Policy storage requires a persistence layer (Redis or PostgreSQL). |
| On-Premises | **4** | All Managed K8s complexity plus: compute allocation for guardrail model inference (OpenGuardrails-Text at 3.3B adds GPU or high-CPU demand), no managed policy management UI (custom-built or open-source), customer-specific policy tuning across N deployments at different compliance regimes, and version coordination with the inference engine upgrade cycle. |

**Three-Phase On-Premises Ratings for S9:**

| Phase | RD | TE | Notes |
|---|:---:|:---:|---|
| Phase 1 (Initial Refactoring) | 3 | 3 | Deploy guardrail sidecar, integrate with customer's inference endpoint, configure baseline policies. Latency budget integration is the primary challenge. |
| Phase 2 (Per-Customer) | 2 | 2 | Per-customer policy customization: industry-specific terms, customer PII definitions, output filtering thresholds. Config-level changes, not code changes. |
| Phase 3 (Ongoing Support) | 3 | 3 | Policy updates as threat landscape evolves. Guardrail model version upgrades (independent release cycle from inference engine). Ongoing latency monitoring and SLA validation. |

---

## 3. Gap Assessment B: Prompt Management / Caching

### 3.1 Current Classification

[FACT]
"Prompt engineering, prompt caching, and prompt management" — listed as Explicitly Excluded from P4 scope.
— `P4_ai_model_plane.md` §1, Explicitly Excluded

[FACT]
AL09 in P2 covers prompt-adjacent concerns as part of AI/ML orchestration. The P2 file defines AL09's scope as covering "agent orchestration code, LangGraph, guardrails, MCP" but does not explicitly rate prompt management or prompt caching as independent concerns within AL09.
— `RP2b_P2_resilience_ai_testing.md` §AL09 Phase 1, three-phase file notes

### 3.2 Industry Evidence for Prompt Caching as a Distinct ISV Operational Concern

[FACT]
"Prompt caching can cut LLM costs by 90% and reduce latency by 75%."
— Sylphai, "The Complete Guide to Prompt Caching: Cut LLM Costs by 90%"
URL: https://sylphai.substack.com/p/the-complete-guide-to-prompt-caching

[FACT]
"Cache writes cost 1.25x to 2x standard input tokens depending on the provider and cache duration, while cache hits are dramatically cheaper at approximately 10% of standard input token cost."
— ngrok blog, "Prompt caching: 10x cheaper LLM tokens, but how?"
URL: https://ngrok.com/blog/prompt-caching/

[FACT]
Amazon Bedrock Prompt Caching reduces costs for repeated system prompts and long-context inputs; the ISV must configure cache scope, cache lifetime, and cache-key design within the API call structure.
— Caylent, "Amazon Bedrock Prompt Caching: Saving Time and Money in LLM Applications"
URL: https://caylent.com/blog/prompt-caching-saving-time-and-money-in-llm-applications

[FACT]
The vLLM Router (December 2025) includes "prefix-aware routing for KV-cache hit rate optimization" — making prompt caching behavior a function of the routing layer configuration, not the inference engine alone.
— `P4_ai_model_plane.md` §3, S6 Evidence, citing F05 and F55b

### 3.3 Boundary Analysis: Is Prompt Caching Adequately Covered?

The P4 exclusion of prompt caching is partially addressed in S6 (Model Routing), where prefix-aware routing for KV-cache hit rate is cited as a routing concern. However, there is a distinction between two levels of prompt caching:

**Level 1 — KV-cache prefix routing (currently covered in S6):** The routing layer directs requests with shared prefixes to the same inference engine replica to maximize KV-cache hit rates. This is an infrastructure routing concern and is correctly housed in S6.

**Level 2 — Prompt template management and semantic cache (currently not covered in P4 or P2):** The management of prompt templates across product versions, per-customer prompt customizations, and semantic caching (where semantically similar but not identical prompts are served from cache) is an application-layer concern. This is adjacent to AL09 in P2 but is not rated there either.

**Assessment:** The Level 1 (KV-cache routing) is adequately covered in S6. Level 2 (prompt template management, semantic cache, per-customer prompt variants) is partially housed in AL09 by implication but is not explicitly rated. Given that:

- Prompt template management is application code (P2 scope)
- Semantic caching at the gateway layer falls in S6 (P4 scope)
- Neither subsegment explicitly surfaces this concern at sufficient granularity

This constitutes a partial gap — similar in character to the API Versioning gap identified in RP2e_P2_completeness.md. The appropriate remediation is a scope note clarification in S6 to explicitly claim semantic caching configuration, and a scope note in AL09 to explicitly claim prompt template lifecycle management. A new P4 subsegment is not warranted for prompt management alone; the concern distributes across existing boundaries rather than constituting a standalone infrastructure domain.

See [file: RP2e_P2_completeness.md §3.2] for the analogous treatment of API Versioning as a labeling/visibility gap rather than an absent-coverage gap.

**Verdict:** Prompt Management / Caching is a partial gap with a distribution across S6 and AL09. No new subsegment required in P4; scope note clarifications in S6 and AL09 are the appropriate remediation.

---

## 4. Gap Assessment C: Model Cost Attribution / Chargeback

### 4.1 Current Coverage State

S1 (Managed API Integration) lists "Cost tracking and per-customer token attribution" as an ISV ownership item:

[FACT]
ISV owns in S1: "Cost tracking and per-customer token attribution."
— `P4_ai_model_plane.md` §3, S1 ("What the ISV owns")

However, this is listed as a task within S1, not as the definition of S1. S1's primary scope is "consuming cloud-provider LLM API endpoints." Cost attribution is a secondary concern embedded in the subsegment, not rated independently.

Under the customer-provides-GPU scope split, S1 remains ISV-owned (reduced form), and the cost attribution concern does not disappear — it changes character:

- Cloud-native: ISV attributes token costs to customers based on API provider billing (Bedrock, Azure OpenAI, Vertex AI all provide per-request cost data)
- On-premises: Customer pays for GPU hardware; ISV needs to attribute compute-hour consumption and model inference time to individual tenants without provider-side billing integration

### 4.2 Industry Evidence for Cost Attribution as a Distinct ISV Operational Concern

[FACT]
"Precise cost attribution enables organizations to pinpoint exactly which business unit, application, or user is driving the highest costs, thereby enabling accurate internal chargebacks and granular budget planning."
— Bitrock, "LLMOps Cost Control and Performance Optimization with the AI Gateway"
URL: https://bitrock.it/blog/llmops-cost-control-and-performance-optimization-with-the-ai-gateway.html

[FACT]
"A single abusive tenant can quietly run up four figures in a weekend, highlighting the need for per-tenant budget guardrails."
— Medium, "LLM Cost Dashboards for Backends: Token Budgets, Cache Hit Rates, and Alerts"
URL: https://medium.com/@2nick2patel2/llm-cost-dashboards-for-backends-token-budgets-cache-hit-rates-and-alerts-29b2185a5202

[FACT]
Langfuse provides "Model Usage and Cost Tracking for LLM applications" including per-user, per-session, and per-tenant token attribution as a self-hosted observability capability.
— Langfuse documentation, "Model Usage and Cost Tracking"
URL: https://langfuse.com/docs/observability/features/token-and-cost-tracking

[FACT]
LiteLLM provides "per-customer token attribution" as a gateway capability supporting multi-tenant cost visibility.
— `P4_ai_model_plane.md` §3, S1, citing F36

[FACT]
"Organizations implement chargeback or showback by reporting monthly cost by product area and customer segment to align incentives."
— Radicalbit, "LLM Cost Control: Practical LLMOps Strategies for Monitoring API Spend"
URL: https://radicalbit.ai/resources/blog/cost-control/

### 4.3 On-Premises Tier Impact Analysis

On-premises cost attribution is structurally different from cloud-native:

**Cloud-native:** The provider (Bedrock, Azure OpenAI, Vertex AI) produces per-request cost data including token counts and pricing tier. The ISV aggregates this data per tenant by passing tenant identifiers in API call metadata. Cost attribution is a data aggregation and dashboard problem.

**On-premises (customer-provides-GPU scope):** The ISV does not pay for inference compute — the customer owns the hardware. However, the ISV is still responsible for:
- Attributing model inference load per tenant (which tenant's requests consumed how much GPU time)
- Enforcing per-tenant rate limits and budget caps
- Providing the customer with per-tenant AI consumption reports (for the customer's own internal chargeback or compliance purposes)
- Managing per-tenant token quotas within the customer's shared inference cluster

This is a distinct concern from S7 (Inference Monitoring), which covers TTFT/TPS/GPU health metrics, not per-tenant consumption accounting.

### 4.4 Boundary Analysis: Which Plane Owns Cost Attribution?

| Concern | Current Location | Adequacy |
|---|---|---|
| Provider-side API cost ingestion | S1 (implied) | Partially covered; not independently rated |
| Per-tenant token count aggregation | S7 (inference monitoring) or AL09 (orchestration) | Not explicitly covered in either |
| Per-tenant budget enforcement / rate limiting | S6 (routing layer) | Partially covered (rate limiting in gateway config) |
| Customer-facing cost reporting | None | Gap |
| On-premises GPU-hour attribution per tenant | None | Gap |

**Verdict:** Model Cost Attribution / Chargeback is a genuine operational gap. It is partially embedded in S1 (as an ISV ownership task) and partially in S6 (rate limiting at the gateway), but no subsegment owns the end-to-end cost attribution pipeline. Under the on-premises scope split, this gap is most acute because provider-side billing integration is unavailable.

**Proposed Subsegment: S10 — AI Cost Attribution and Consumption Governance**

Definition: Collecting, aggregating, and reporting per-tenant AI inference consumption — token counts, GPU compute-hours, and cache-hit rates — for internal chargeback, per-tenant rate limiting, and customer-facing consumption reporting. Includes integration with the gateway layer for budget enforcement and quota management, and with the observability stack for cost trend analysis.

What the ISV owns:
- Per-request token count capture and tenant tagging (at gateway or orchestration layer)
- Aggregation pipeline from raw token events to per-tenant cost reports (daily/monthly)
- Per-tenant budget cap configuration and enforcement (hard limits vs. soft alerts)
- Customer-facing consumption dashboard or API (reporting tokens used, quota remaining)
- On-premises GPU-hour attribution model (when customer owns compute and ISV needs to report load share)

**Proposed Difficulty Ratings: S10 — AI Cost Attribution and Consumption Governance**

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **2** | Provider APIs return per-request cost data. ISV aggregates via LiteLLM or Langfuse, tags by tenant ID, and surfaces in a cost dashboard. Standard data pipeline work. Rated 2 (not 1) because multi-tenant aggregation, budget enforcement logic, and customer reporting require dedicated engineering. |
| Managed K8s | **3** | Same as cloud-native if using managed APIs (Strategy a). If self-hosting inference (Strategy b): must aggregate from vLLM Prometheus metrics (no native cost data), convert GPU utilization to cost equivalents, and build custom attribution models. Significantly more complex than cloud-native. |
| On-Premises | **4** | No provider cost APIs. ISV must instrument every inference call at the gateway (LiteLLM), aggregate token events via custom pipeline (or Langfuse self-hosted), build GPU-hour attribution from DCGM Exporter metrics, and implement per-tenant quota enforcement without provider-side guardrails. Customer reporting must be built and maintained by the ISV. N customers = N reporting configurations to manage. |

**Three-Phase On-Premises Ratings for S10:**

| Phase | RD | TE | Notes |
|---|:---:|:---:|---|
| Phase 1 (Initial Refactoring) | 3 | 3 | Build cost attribution pipeline: instrument gateway for per-request token capture, configure Langfuse self-hosted (PostgreSQL + ClickHouse + Redis + S3) or equivalent, establish tenant-tagging schema. |
| Phase 2 (Per-Customer) | 2 | 2 | Configure per-tenant rate limits and budget caps. Set up customer-specific consumption report format. Map customer's internal cost center structure to tenant IDs. |
| Phase 3 (Ongoing Support) | 3 | 3 | Ongoing: attribution pipeline maintenance as token pricing or GPU cost models change, Langfuse version upgrades, per-customer quota tuning as usage patterns evolve. Scales with N customers (new customer = new attribution config). |

---

## 5. P2/P3/P4 Boundary Analysis: AI Responsibility Gaps

### 5.1 The Three-Layer AI Stack and Its Current Boundary Allocations

The framework distributes AI responsibilities across three planes:

| Concern | Plane | Subsegment(s) |
|---|---|---|
| Agent orchestration, LangGraph, MCP, tool-calling | P2 | AL09 |
| Embedding pipelines and embedding model serving | P3 | DS9 |
| RAG pipeline orchestration | P3 | DS10 |
| Vector database operations | P3 | DS8 |
| LLM inference serving (self-hosted) | P4 | S2 |
| GPU hardware | P4 | S3 (customer scope) |
| Model routing | P4 | S6 |
| Inference monitoring (application layer) | P4 | S7 (reduced) |
| Model lifecycle management | P4 | S8 (reduced) |

[FACT]
"AL09 is ranked #1 hardest on-premises subsegment across all 38 subsegments in S1."
— `GT5_cross_reference_ground_truth.md` §3, S1 Top 10 Hardest Subsegments, Rank 1

[FACT]
"Must self-host vLLM/TGI serving, Milvus/Qdrant vector DB, Temporal workflow orchestration (Cassandra+ES+4 pods), Langfuse observability (PostgreSQL+ClickHouse+Redis+S3), LlamaFirewall guardrails, and LiteLLM routing — all simultaneously with GPU scheduling."
— `S1_four_plane_synthesis.md` §2, Rank 1 row (AL09 rationale)

### 5.2 Confirmed Gaps in the Boundary Design

**Gap 1: Guardrail operations are named in AL09's stack but not rated as a distinct component.**

The S1 synthesis explicitly lists "LlamaFirewall guardrails" in AL09's on-premises stack. However, RP2b confirms that AL09 Phase 3 RD is already under-rated at 3 (should be 4), meaning the current rating absorbs a partial guardrail burden without surfacing it. If guardrail operations are extracted to a dedicated S9 subsegment (proposed above), AL09's Phase 3 RD would remain at the proposed 4 but with a cleaner scope boundary. See `RP2b_P2_resilience_ai_testing.md` §AL09 Phase 3, ADJUST verdict.

**Gap 2: Cost attribution spans S1, S6, S7, and AL09 without a clear owner.**

Per-tenant token attribution is listed in S1's ISV ownership. Per-tenant rate limiting exists in S6's circuit breaker configuration. Per-tenant inference metrics are captured in S7's observability scope. None of these subsegments owns the end-to-end cost attribution pipeline. This gap is most visible under the on-premises scope split because provider-side billing integration disappears and the ISV must build the attribution layer from scratch.

**Gap 3: Embedding model serving (DS9) and LLM inference serving (S2) share GPU contention that is attributed to S5, but the boundary at the customer-scope split creates a blind spot.**

[FACT]
"GPU contention between LLM inference and embedding workloads is 'the primary operational risk on-premises'; without explicit MIG partitioning on A100/H100 hardware, embedding latency degrades unpredictably under LLM load."
— `P4_ai_model_plane.md` §3, S5 Evidence, citing W05S (synthesis/W05S_onprem_app_patterns.md)

Under the customer-provides-GPU scope split, S5 (GPU Scheduling) moves to customer scope. This removes the ISV's visibility into the GPU contention problem between DS9 (embedding) and the customer's LLM inference workloads. The ISV must communicate GPU allocation requirements to the customer for the embedding pipeline (DS9, ISV-owned) to coexist with the customer's inference workloads (S2/S3/S5, customer-owned). This interface requirement — ISV specifying GPU allocation requirements to the customer — has no explicit home in the current framework. It is a coordination protocol gap, not an FTE gap.

**Verdict on Gap 3:** This is a scope note gap, not a subsegment gap. The appropriate remediation is an explicit note in DS9 that the embedding pipeline's GPU resource requirements must be communicated to the customer as part of the on-premises deployment specification.

---

## 6. Comparison Against Emerging LLMOps Frameworks

### 6.1 Enterprise LLMOps Operational Model (2025)

The enterprise LLMOps model as described in industry sources defines the following operational layers:

[FACT]
"LLMOps adds disciplined prompt management, multi-layer evaluation, controlled rollouts, optimized serving, continuous monitoring, and compliance-first governance."
— ACI Infotech, "Enterprise LLMOps: Scalable, Governed and Cost-Effective GenAI"
URL: https://www.aciinfotech.com/blogs/enterprise-llmops-scalable-governed-cost-effective-genai

Mapping these LLMOps layers to the current P4 framework:

| LLMOps Layer | Current P4 Coverage | Gap? |
|---|---|---|
| Prompt management | Excluded (P4 §1) | Partial gap (see §3 above) |
| Multi-layer evaluation (guardrails) | Excluded (P4 §1) | Gap (proposed S9) |
| Controlled rollouts (model versions) | S8 (Model Lifecycle Management) | Covered |
| Optimized serving (routing, KV-cache) | S6 (Model Routing) | Covered |
| Continuous monitoring | S7 (Inference Monitoring) | Covered |
| Compliance-first governance / cost attribution | S1 (partial) | Gap (proposed S10) |

### 6.2 Five MECE Frameworks Convergence on AI Safety

[FACT]
"AI/ML inference and security/compliance are unanimously identified by all five MECE frameworks as the two highest-difficulty, highest-risk on-premises domains, requiring dedicated specialist teams that have no generalist substitution path."
— `S1_four_plane_synthesis.md` §8, Key Takeaway 4; citing F79_mece_meta_analysis.md §5

This convergence supports the case for a dedicated AI safety/guardrails subsegment (S9). If five independent MECE frameworks consistently identify security/compliance as a highest-difficulty AI concern, and the current P4 framework explicitly excludes it, the exclusion represents a deliberate deferral rather than a justified omission.

### 6.3 Gartner AI Project Cancellation Rates

[FACT]
"Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027."
— Gartner press release, 2025-06-25
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

This Gartner figure, previously cited in RP2b for AL09, has direct relevance to P4 completeness. ISVs managing guardrail and cost attribution operations as undefined/unrated concerns are more likely to encounter budget overruns (untracked AI spend) and safety incidents (unrated guardrail maintenance) that contribute to project cancellation. Explicit subsegment treatment of S9 and S10 reduces this planning blind spot.

---

## 7. Summary: Gaps Found and Proposed Subsegments

### 7.1 Gap Classification

| Gap | Type | Current Location | Severity | Proposed Action |
|---|---|---|---|---|
| AI Safety / Guardrails | Missing subsegment | AL09 (embedded, unrated) | High — operational in every LLM deployment | New P4 subsegment: S9 |
| Model Cost Attribution / Chargeback | Missing subsegment | S1 (partial) | High — critical for ISV multi-tenant billing | New P4 subsegment: S10 |
| Prompt Caching (semantic) | Scope boundary gap | S6 (infrastructure) + AL09 (application) | Medium — partially covered; needs scope note | Scope note in S6 and AL09 |
| DS9/S5 GPU coordination interface | Coordination gap | No home under scope split | Low — planning artifact, not FTE gap | Scope note in DS9 |

### 7.2 Revised P4 Subsegment Count

Under the proposed additions, P4 expands from 8 to 10 subsegments:

| ID | Subsegment | ISV Scope (On-Premises) | Status |
|---|---|---|---|
| S1 | Managed API Integration | ISV (reduced) | Existing |
| S2 | Self-Hosted Inference Engine Deployment | Customer scope | Existing |
| S3 | GPU Hardware Infrastructure | Customer scope | Existing |
| S4 | GPU Driver and CUDA Stack Management | Customer scope | Existing |
| S5 | Multi-Tenant GPU Scheduling | Customer scope | Existing |
| S6 | Model Routing and Load Balancing | ISV (reduced) | Existing |
| S7 | Inference Monitoring and Observability | ISV (reduced) | Existing |
| S8 | Model Lifecycle Management | ISV (reduced) | Existing |
| S9 | AI Safety and Guardrail Operations | ISV | **Proposed** |
| S10 | AI Cost Attribution and Consumption Governance | ISV | **Proposed** |

### 7.3 Proposed Ratings Summary for S9 and S10

**S9 — AI Safety and Guardrail Operations**

| Phase | Relative Difficulty (On-Prem) | Total Effort (On-Prem) | Notes |
|---|:---:|:---:|---|
| Phase 1 (Initial Refactoring) | 3 | 3 | Sidecar deployment, policy integration, latency budget |
| Phase 2 (Per-Customer) | 2 | 2 | Per-customer policy customization |
| Phase 3 (Ongoing Support) | 3 | 3 | Policy updates, guardrail model version management |

Difficulty by tier: Cloud-Native 2 / Managed K8s 3 / On-Premises 4
FTE estimate (on-premises): 0.3–0.8 FTE annually (guardrail model ops + policy management)

**S10 — AI Cost Attribution and Consumption Governance**

| Phase | Relative Difficulty (On-Prem) | Total Effort (On-Prem) | Notes |
|---|:---:|:---:|---|
| Phase 1 (Initial Refactoring) | 3 | 3 | Attribution pipeline build, gateway instrumentation, Langfuse |
| Phase 2 (Per-Customer) | 2 | 2 | Per-tenant rate limits, reporting format, quota configuration |
| Phase 3 (Ongoing Support) | 3 | 3 | Pipeline maintenance, Langfuse upgrades, quota tuning (scales with N) |

Difficulty by tier: Cloud-Native 2 / Managed K8s 3 / On-Premises 4
FTE estimate (on-premises): 0.2–0.5 FTE annually (attribution pipeline maintenance)

---

## Key Findings

- **AI Safety / Guardrails is a genuine P4 gap.** The P4 exclusion of guardrails as a "separate security/trust domain" leaves a self-hosted guardrail stack (LlamaFirewall, NeMo Guardrails, OpenGuardrails) as an unrated ISV operational burden. Under the customer-provides-GPU scope, this burden remains entirely ISV-owned. Three independent open-source guardrail frameworks with self-hosting deployment models exist as of 2025, confirming this is an active operational domain requiring dedicated treatment. Proposed subsegment S9 with on-premises difficulty 4/5. See `P4_ai_model_plane.md` §1 (exclusion); arXiv 2505.03574 (LlamaFirewall); arXiv 2510.19169 (OpenGuardrails).

- **Model Cost Attribution / Chargeback is a genuine P4 gap.** Per-tenant token attribution is listed as an ISV ownership task in S1 but is not rated as an independent subsegment. On-premises, provider-side billing APIs are unavailable, requiring the ISV to build a full attribution pipeline from gateway instrumentation through Langfuse aggregation to customer-facing reporting. This gap is most acute under the customer-provides-GPU scope split. Proposed subsegment S10 with on-premises difficulty 4/5. See `P4_ai_model_plane.md` §3, S1; [Langfuse cost tracking](https://langfuse.com/docs/observability/features/token-and-cost-tracking).

- **Prompt Management / Caching is a partial gap requiring scope clarifications, not a new subsegment.** KV-cache prefix routing is adequately covered in S6. Semantic caching configuration and prompt template lifecycle management are distributed across S6 and AL09 without explicit ownership. Scope note clarifications are the appropriate remediation. See `P4_ai_model_plane.md` §3, S6; `RP2b_P2_resilience_ai_testing.md` §AL09.

- **The P2/P3/P4 boundary creates two coordination gaps.** First, guardrail operations are named in AL09's stack (S1 synthesis Rank 1 rationale) but are unrated; proposing S9 resolves this. Second, per-tenant AI cost attribution spans S1, S6, S7, and AL09 without a clear owner; proposing S10 resolves this. A third gap — GPU allocation coordination between DS9 (embedding) and customer-owned inference infrastructure — is a scope note gap, not an FTE gap. See `S1_four_plane_synthesis.md` §2, Rank 1; `GT5_cross_reference_ground_truth.md` §3.

- **Five independent MECE frameworks unanimously identify AI safety/compliance as a highest-difficulty on-premises domain, supporting the addition of S9.** The current P4 framework is the only framework among the five that explicitly excludes AI safety/guardrails. This exclusion is architecturally defensible but operationally incomplete for ISVs deploying AI applications to regulated enterprise customers. See `S1_four_plane_synthesis.md` §8, Key Takeaway 4; `GT5_cross_reference_ground_truth.md` §5.2.

---

## Sources

**Internal Source Files:**

| File | Absolute Path | Sections Used |
|---|---|---|
| P4_ai_model_plane.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P4_ai_model_plane.md` | §1 (exclusions), §3 (S1–S8 definitions and evidence), §5 (FTE table) |
| S1_four_plane_synthesis.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md` | §2 (Top 10), §3 (Causal Chain), §6 (AL09 overlap), §8 (Key Takeaways) |
| GT4_P4_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT4_P4_ground_truth.md` | Tables 1–5 |
| GT5_cross_reference_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` | §3 (Top 10), §5 (Confidence) |
| RP2b_P2_resilience_ai_testing.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2b_P2_resilience_ai_testing.md` | §AL09 (all phases, ADJUST verdict) |
| RP2e_P2_completeness.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2e_P2_completeness.md` | §3.2 (API Versioning partial gap treatment) |
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` | §1 (scope split), §8 (Grand Summary) |

**External Sources:**

- [LlamaFirewall: An open source guardrail system for building secure AI agents — arXiv 2505.03574](https://arxiv.org/abs/2505.03574)
- [OpenGuardrails: A Configurable, Unified, and Scalable Guardrails Platform — arXiv 2510.19169](https://arxiv.org/html/2510.19169)
- [NVIDIA NeMo Guardrails](https://developer.nvidia.com/nemo-guardrails)
- [Swept AI: Deploying Enterprise LLM Applications — Inference, Guardrails, and Observability](https://www.swept.ai/post/deploying-enterprise-llm-applications-inference-guardrails-observability)
- [Obsidian Security: AI Guardrails — Enforcing Safety Without Slowing Innovation](https://www.obsidiansecurity.com/blog/ai-guardrails)
- [ACI Infotech: Enterprise LLMOps — Scalable, Governed and Cost-Effective GenAI](https://www.aciinfotech.com/blogs/enterprise-llmops-scalable-governed-cost-effective-genai)
- [Bitrock: LLMOps Cost Control and Performance Optimization with the AI Gateway](https://bitrock.it/blog/llmops-cost-control-and-performance-optimization-with-the-ai-gateway.html)
- [Radicalbit: LLM Cost Control — Practical LLMOps Strategies for Monitoring API Spend](https://radicalbit.ai/resources/blog/cost-control/)
- [Langfuse: Model Usage and Cost Tracking for LLM Applications](https://langfuse.com/docs/observability/features/token-and-cost-tracking)
- [Langfuse: LLM Security and Guardrails](https://langfuse.com/docs/security-and-guardrails)
- [ngrok blog: Prompt caching — 10x cheaper LLM tokens, but how?](https://ngrok.com/blog/prompt-caching/)
- [Sylphai: The Complete Guide to Prompt Caching — Cut LLM Costs by 90%](https://sylphai.substack.com/p/the-complete-guide-to-prompt-caching)
- [Caylent: Amazon Bedrock Prompt Caching — Saving Time and Money in LLM Applications](https://caylent.com/blog/prompt-caching-saving-time-and-money-in-llm-applications)
- [Medium — LLM Cost Dashboards for Backends: Token Budgets, Cache Hit Rates, and Alerts](https://medium.com/@2nick2patel2/llm-cost-dashboards-for-backends-token-budgets-cache-hit-rates-and-alerts-29b2185a5202)
- [Gartner: Over 40% of Agentic AI Projects Will Be Canceled by End of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- [Datadog: LLM guardrails — Best practices for deploying LLM apps securely](https://www.datadoghq.com/blog/llm-guardrails-best-practices/)
- [Medium — LLMOps: Architecting Enterprise LLMOps for Scalable, Governed AI (Pratik Vyas)](https://medium.com/@pratik.vyas_10544/llmops-architecting-enterprise-llmops-for-scalable-governed-and-cost-effective-ai-9d57995ddb39)
