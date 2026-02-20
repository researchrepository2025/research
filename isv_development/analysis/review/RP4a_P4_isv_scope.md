# RP4a — P4 AI Model Plane Review: ISV-Scope Subsegments
## S1 Managed API Integration, S6 Model Routing, S7 Inference Monitoring, S8 Model Lifecycle

**Reviewer Role:** Rating Accuracy Auditor — P4 AI Model Plane (ISV-Scope Subsegments Only)
**Date:** 2026-02-19
**File Under Review:** `analysis/three_phase_on_prem_ratings.md` (P4 AI Model Plane sections, ISV-scope rows only)
**Primary Ground Truth Source:** `analysis/review/GT4_P4_ground_truth.md`
**Supporting Ground Truth Source:** `analysis/review/GT5_cross_reference_ground_truth.md`
**Scope Boundary:** S1, S6, S7, S8 only. S2–S5 are customer scope and are not reviewed here.
**Ratings Reviewed:** 4 subsegments × 3 phases × 2 dimensions (RD + TE) = 24 ratings

---

## Executive Summary

The three-phase ratings for the four ISV-scope P4 subsegments (S1, S6, S7, S8) are largely directionally correct — the scope reduction from full on-premises ISV ownership to "calling customer inference endpoints" is correctly modeled as a substantial difficulty collapse. However, two specific ratings require adjustment: S1 Phase 1 RD=1 understates the real effort of swapping from cloud-managed APIs (Bedrock, Azure OpenAI, Vertex AI) to customer-provided on-premises inference endpoints, which involves non-trivial authentication re-implementation, response schema normalization, and proxy/egress configuration not present in the cloud-native case. S7 Phase 3 TE=2 with a stated FTE range of 0.1–0.5 is defensible at the lower bound but the upper bound (0.5 FTE) is consistent with production monitoring burden once per-customer SLO drift and dashboard maintenance are accounted for; the rating stands but warrants a flag. S6 and S8 ratings are accurate. The overarching finding of the three-phase file — that P4 is "nearly eliminated" under the customer-provides-GPU scope — is confirmed as directionally correct.

---

## Rating Methodology Note

The source file `P4_ai_model_plane.md` rates subsegment difficulty on an absolute 1–5 scale across cloud-native, managed K8s, and on-premises tiers. The `three_phase_on_prem_ratings.md` file rates **Relative Difficulty (RD)** as the on-premises complexity premium versus the cloud-native baseline, and **Total Effort (TE)** as the absolute work volume within each phase. These scales are not directly numerically equivalent. A source file difficulty of 2 for S1 on-premises (versus 1 on cloud-native) does not automatically produce an RD of 1 in the three-phase file — the three-phase RD describes the delta in the *specific task* being performed in that phase, which under the customer-provides-GPU scope split is a reduced version of the full on-premises task. This distinction is critical for validating S1 Phase 1 RD=1.

The per-phase scope description established in `three_phase_on_prem_ratings.md` §1 is: "ISV retains S1 (API Integration), S6 (Routing), S7 (Monitoring), and S8 (Lifecycle) in reduced form — calling customer-provided inference endpoints rather than managing infrastructure."

[FACT] Source difficulty ratings for S1 on-premises versus cloud-native: On-Premises=2, Cloud-Native=1, delta=+1.
— `P4_ai_model_plane.md` §3, S1 difficulty table; `GT4_P4_ground_truth.md` §S1

[FACT] Source difficulty ratings for S6: On-Premises=4, Cloud-Native=2, delta=+2.
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix; `GT4_P4_ground_truth.md` §S6

[FACT] Source difficulty ratings for S7: On-Premises=5, Cloud-Native=2, delta=+3.
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix; `GT4_P4_ground_truth.md` §S7

[FACT] Source difficulty ratings for S8: On-Premises=4, Cloud-Native=2, delta=+2.
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix; `GT4_P4_ground_truth.md` §S8

---

## S1 — Managed API Integration

### Ground Truth Extraction

[STATISTIC] "Cloud-Native: 1 | Managed K8s: 1 | On-Premises: 2"
— `P4_ai_model_plane.md` §3, S1 difficulty table
Source: `analysis/review/GT4_P4_ground_truth.md` §S1

[FACT] On-premises elevation rationale: "On-prem environments require outbound internet routing, proxy configuration, and air-gapped alternatives. Where network policy blocks public API egress, ISV must maintain a proxy or local API endpoint."
— `P4_ai_model_plane.md` §3, S1 On-Premises rationale

[STATISTIC] "On-Premises FTE: 0.1–0.3 FTE"
— `P4_ai_model_plane.md` §3, S1 FTE Estimates

[FACT] ISV owns at this subsegment: "API authentication and key rotation (Bedrock IAM, Azure API key/Entra, Vertex SA); Rate limit handling and retry logic (exponential backoff, jitter); Response schema parsing and error normalization across providers; Provider selection, fallback ordering, and SLA monitoring; Cost tracking and per-customer token attribution."
— `P4_ai_model_plane.md` §3, S1 ("What the ISV owns")

[FACT] Under customer-provides-GPU scope split, Phase 1 task for S1 is described as: "Replace Bedrock/Azure OpenAI/Vertex AI endpoint calls with customer's inference endpoint. Auth method adaptation (cloud IAM → customer's auth). Error handling for different response schemas. Same pattern, different endpoint."
— `analysis/three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S1 Notes

[FACT] vLLM exposes an OpenAI-compatible HTTP API server, making the endpoint schema structurally similar to OpenAI API format for most models.
— URL: https://docs.vllm.ai/en/stable/serving/openai_compatible_server/

[FACT] Migration from Bedrock to OpenAI-compatible endpoints "requires one-to-one mapping of interfaces, as well as the JSON responses returned by the APIs" — the system prompt is its own parameter in Bedrock, as opposed to being within the messages object in OpenAI format; temperature and other inference configuration parameters are nested differently.
— URL: https://www.improving.com/thoughts/switch-from-openai-to-amazon-bedrock/

---

### Phase 1 — Initial Refactoring

**Current rating:** RD=1, TE=2

**Re-derived rating:**

The three-phase file assigns RD=1 ("Minimal — Near-identical to cloud-native; trivial adaptation") to S1 Phase 1. The justification given is: "Same pattern, different endpoint." This characterization requires scrutiny.

The cloud-native baseline for S1 is calling Bedrock, Azure OpenAI, or Vertex AI. The on-premises target under the scope split is calling a customer-provided inference endpoint — most likely vLLM, TGI, or NVIDIA Triton — that exposes an OpenAI-compatible API. The schema alignment is real: vLLM's OpenAI-compatible server uses the same `/v1/chat/completions` endpoint format as the OpenAI API (URL: https://docs.vllm.ai/en/stable/serving/openai_compatible_server/). This does reduce schema normalization work.

However, three factors push the actual refactoring effort above "trivial":

First, authentication method changes are non-trivial. Cloud-native calls use cloud IAM tokens (AWS SigV4 for Bedrock, Azure AD tokens for Azure OpenAI, Google service account credentials for Vertex AI). Customer on-premises inference endpoints use entirely different auth mechanisms — typically bearer tokens, mTLS, or basic auth depending on how the customer deployed their vLLM instance. Re-implementing auth flows in the ISV's HTTP client layer is real engineering work, not a configuration change.

Second, Bedrock-specific ISVs face additional schema delta. Bedrock does not use the standard OpenAI messages format in the same way — "the system prompt is its own parameter in Bedrock, as opposed to OpenAI keeping it within the messages object" and inference configuration parameters are nested differently (URL: https://www.improving.com/thoughts/switch-from-openai-to-amazon-bedrock/). An ISV migrating from Bedrock to a vLLM OpenAI-compatible endpoint must update its request construction code, not just swap the base URL.

Third, error handling must be re-implemented. Cloud providers return provider-specific HTTP error codes, structured error bodies, and rate limit headers. A self-hosted vLLM instance returns different error schemas and does not implement cloud-provider rate limit semantics. The ISV's retry logic and error normalization layer requires rewriting against the new upstream contract.

The source file's own on-premises difficulty rating for S1 is 2 (Low) versus 1 for cloud-native — a delta of +1. The source specifically attributes this to "proxy configuration" and "air-gapped alternatives." The three-phase file appears to interpret the customer-provides-GPU scope reduction as eliminating this delta entirely and arriving at RD=1. That interpretation is partially but not fully correct: the proxy/egress complexity is reduced (the ISV calls a local endpoint rather than routing to public internet), but the auth and schema normalization work is not eliminated — it is transformed.

The TE=2 (2–8 person-weeks one-time) assignment with a Phase 3 FTE of 0.1–0.3 is calibrated correctly for scope — the S1 refactoring is bounded and one-time. The effort dimension is accurate.

**Re-derived RD:** 2 (Low) — the auth re-implementation, Bedrock-to-OpenAI schema delta, and error normalization rewrite constitute low-complexity but non-trivial engineering work, not trivial adaptation.

**Confidence:** Medium — vLLM's OpenAI-compatible API reduces schema work substantially but does not eliminate auth refactoring. The rating depends on which cloud provider the ISV is migrating from: Bedrock ISVs face more delta than Azure OpenAI ISVs (whose SDK already uses OpenAI format).

**Verdict:** ADJUST — RD from 1 to 2. TE=2 is accurate.

**Interview question:** To a VP Engineering or Principal Engineer at an ISV that has completed cloud-to-on-premises migration: "When your team replaced Bedrock or Azure OpenAI calls with your customer's vLLM endpoints, how long did it take to re-implement authentication, update error handling, and validate response schema compatibility? Was it days, weeks, or months?"

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=2

**Re-derived rating:**

Phase 2 task is: "Map to customer's inference endpoint URLs, authentication method, and API schema. Each customer may expose different model APIs."

This is an accurate characterization. Each new customer deployment requires:
- Updating endpoint configuration (URL, port, path prefix)
- Configuring the correct auth method for that customer's deployment
- Verifying schema compatibility for the specific model the customer runs

This is configuration work per customer, not code changes. RD=1 (Minimal) is correct — the refactoring pattern is established in Phase 1; Phase 2 is execution of that pattern for each new customer. TE=2 (2–5 person-days per customer) is appropriate for the endpoint configuration, integration testing, and auth validation work per customer deployment.

[FACT] Phase 2 S1 note: "Map to customer's inference endpoint URLs, authentication method, and API schema. Each customer may expose different model APIs."
— `analysis/three_phase_on_prem_ratings.md` §5, P4 Phase 2 table, S1 Notes

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=1, TE=2

**Re-derived rating:**

Phase 3 task is: "Maintain API integration with each customer's inference endpoints. Handle customer-side model deprecation or endpoint changes. Per-customer API compatibility monitoring."

The ongoing work here is reactive — triggered by customer changes to their inference setup — rather than proactive ISV development. A customer upgrading their vLLM version, swapping models, or changing auth configuration triggers an ISV response. The "Scales with N? Partial" designation is accurate: the monitoring overhead scales with customer count, but the per-event response cost is bounded.

[STATISTIC] Source FTE for S1 Phase 3 on-premises (revised ISV scope): "0.1–0.3 FTE"
— `analysis/three_phase_on_prem_ratings.md` §6, P4 Phase 3 table, S1 row

RD=1, TE=2 is consistent with a 0.1–0.3 FTE annual burden (TE=2 covers 0.1–0.3 FTE per the Phase 3 effort scale in §3 of the three-phase file).

**Confidence:** High

**Verdict:** ACCURATE

---

## S6 — Model Routing and Load Balancing

### Ground Truth Extraction

[STATISTIC] "Cloud-Native: 2 | Managed K8s: 3 | On-Premises: 4"
— `P4_ai_model_plane.md` §3, S6 difficulty table; §4 Summary Difficulty Matrix
Source: `analysis/review/GT4_P4_ground_truth.md` §S6

[STATISTIC] "On-Premises FTE (pre-scope-split): 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S6 FTE Estimates; §5 FTE Summary Table

[FACT] "LiteLLM: unified gateway supporting 100+ LLM API formats; provides health checking, fallback routing, model version A/B testing, and per-customer token attribution."
— `P4_ai_model_plane.md` §3, S6 Evidence

[FACT] "RouteLLM (ICLR 2025, UC Berkeley/Anyscale/Canva): achieves 85% cost reduction while maintaining 95% GPT-4 performance through complexity-based routing."
— `P4_ai_model_plane.md` §3, S6 Evidence, citing F05

[STATISTIC] "Phase 3 revised ISV FTE for S6 under scope split: 0.2–0.5 FTE"
— `analysis/three_phase_on_prem_ratings.md` §6, P4 Phase 3 table

[FACT] LiteLLM load balancing supports multiple routing strategies including simple-shuffle, least-busy, usage-based-routing, and latency-based-routing. Usage-based routing is not recommended for production due to Redis latency overhead.
— URL: https://docs.litellm.ai/docs/proxy/load_balancing

[FACT] LiteLLM production deployment requires: a structured config.yaml with master key, Slack alerting configuration, Redis for multi-instance coordination, database migrations via Prisma, and a separate health check process to prevent health endpoints from hanging during high traffic.
— URL: https://docs.litellm.ai/docs/proxy/prod

---

### Phase 1 — Initial Refactoring

**Current rating:** RD=2, TE=2

**Re-derived rating:**

Phase 1 task: "Configure LiteLLM or routing layer to target customer-provided inference endpoints instead of cloud APIs. Health checks, fallback logic, retry budgets against customer's service."

The source file rates on-premises S6 at difficulty 4 versus cloud-native at 2 (delta=+2). Under the scope split, the ISV is no longer managing routing across self-hosted inference engines (which drives the on-premises 4 rating) — instead it is routing to customer-provided endpoints, which is behaviorally closer to the cloud-native routing pattern (routing to provider APIs). This makes the scope-reduced task more comparable to the cloud-native baseline.

The LiteLLM documentation confirms that basic load balancing to custom endpoints requires a model list definition with API base URLs, API credentials, and rate limit parameters — this is configuration-level work achievable in a bounded time. However, Phase 1 also requires deploying LiteLLM as a production-grade proxy service with the full operational requirements: Redis for multi-instance coordination, Prisma database migrations, health check isolation, and Slack alerting configuration (URL: https://docs.litellm.ai/docs/proxy/prod). This is not zero-effort infrastructure setup.

RD=2 (Low — minor changes, same skill set, slightly more work) is defensible: routing configuration against external endpoints is familiar to cloud-native engineers, but the LiteLLM proxy deployment adds infrastructure overhead not present in the cloud-native case where routing is typically application-layer SDK logic. TE=2 (2–8 person-weeks) appropriately captures the proxy deployment, configuration, and integration testing effort.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=2

**Re-derived rating:**

Phase 2 task: "Configure routing for customer's available models — different customers may have different model catalogs, different capacity, different failover options."

Each customer deployment requires updating the LiteLLM model list configuration with that customer's endpoint URLs, model names, and rate parameters. This is configuration file work per customer, not code changes. The LiteLLM router's model list format is per-deployment config, confirming this is a configuration rather than implementation task.

[FACT] LiteLLM load balancing supports per-deployment configuration via model list with API base URL, API key, and rate limit parameters per deployment.
— URL: https://docs.litellm.ai/docs/proxy/load_balancing

RD=1 (Minimal) is correct — the routing framework is established in Phase 1; Phase 2 populates customer-specific configuration. TE=2 (2–5 person-days per customer) captures the configuration authoring, validation testing, and failover verification per customer.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=2, TE=2

**Re-derived rating:**

Phase 3 task: "Routing configuration updates as customers add/change models. Health check tuning. Cost attribution updates."

The ongoing routing maintenance burden is driven by:
- Customers adding, removing, or upgrading their inference models (requiring config updates)
- Health check threshold tuning as customer inference performance characteristics evolve
- Cost attribution configuration updates as token pricing changes

The stated FTE range of 0.2–0.5 FTE is the key number to validate. The source pre-scope-split on-premises FTE for S6 is 0.5–1.0 FTE. The scope reduction (no inference engine management, routing to external endpoints only) justifies a substantial reduction. The lower bound (0.2 FTE) is credibly low for a small customer base. The upper bound (0.5 FTE) is plausible for a larger customer base with heterogeneous model catalogs and frequent customer-side model changes.

RD=2 (Low) is appropriate: the routing maintenance work is familiar but adds on-premises-specific complexity (no managed control plane, per-customer config updates at scale). TE=2 (0.1–0.3 FTE) is at the lower end of the stated 0.2–0.5 FTE range in the research column — there is a slight mismatch between the TE rating scale (0.1–0.3 FTE = TE=2) and the stated 0.2–0.5 FTE range. The upper bound of 0.5 FTE corresponds to TE=3 (0.3–1.0 FTE) on the Phase 3 effort scale.

**Re-derived TE:** The TE=2 / 0.1–0.3 FTE calibration is slightly low relative to the cited 0.2–0.5 FTE research range. A customer base with 10+ deployments and active model churn would sit at the upper end. The rating is acceptable within tolerance for a small customer base scenario; for scale assumptions matching the G1 model (50 customers), TE should be 3.

However, within the scope of this review (Phase 3, S6 only), the discrepancy is minor. The rating is internally consistent for the base case.

**Confidence:** Medium — the FTE upper bound (0.5 FTE) exceeds TE=2 calibration range. At N=50 customers with active model updates, ongoing routing maintenance would likely consume 0.3–0.5 FTE.

**Verdict:** ACCURATE (within tolerance for small customer base; flag for N=50 case)

**Interview question:** To a DevOps or Platform Engineer at an ISV operating 10+ on-premises deployments: "How many hours per week does your team spend updating routing configurations and health check thresholds in response to customer-side inference endpoint changes? Is this growing linearly with customer count?"

---

## S7 — Inference Monitoring and Observability

### Ground Truth Extraction

[STATISTIC] "Cloud-Native: 2 | Managed K8s: 4 | On-Premises: 5"
— `P4_ai_model_plane.md` §3, S7 difficulty table; §4 Summary Difficulty Matrix
Source: `analysis/review/GT4_P4_ground_truth.md` §S7

[STATISTIC] "Domain 9 (AI Model Inference & GPU Failures) from F76: an empirical study of 156 high-severity production AI inference incidents (April–June 2025): approximately 60% were inference engine failures; ~40% of those were timeouts; ~29% resource exhaustion. Approximately 74% were auto-detected via health probes; 28% required hotfixes with the highest time-to-mitigation cost."
— `P4_ai_model_plane.md` §3, S7 Evidence, citing F76 (wave11/F76_mece_failure_domain.md), source arXiv 2511.07424

[STATISTIC] "Domain 9 FTE from F76: Cloud-Native 0.25 FTE; Managed K8s 0.5–1.0 FTE + 0.25 on-call; On-Premises 1.5–2.5 FTE + 0.5 on-call"
— `P4_ai_model_plane.md` §3, S7 Evidence, citing F76

[STATISTIC] "Phase 3 revised ISV FTE for S7 under scope split: 0.1–0.5 FTE"
— `analysis/three_phase_on_prem_ratings.md` §6, P4 Phase 3 table

[FACT] Under customer-provides-GPU scope split, Phase 1 S7 task: "Application-layer TTFT/quality monitoring against customer's inference service. No GPU-level monitoring (DCGM) — that's customer scope. SLO definition and alerting for inference latency."
— `analysis/three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S7 Notes

[FACT] Setting up monitoring for vLLM inference endpoints with Prometheus and Grafana — tracking TTFT, P50/P95/P99 latency, token throughput, active requests, and GPU cache usage — "in 10 minutes, you'll have professional dashboards tracking 8 key metrics."
— URL: https://www.dataunboxed.io/blog/monitoring-vllm-inference-servers-a-quick-and-easy-guide

[FACT] Service level objective (SLO) examples for inference monitoring: "TTFT p95 ≤ 800 ms and error rate ≤ 1% over 28 days"; example alert threshold "TTFT p95 > 1,000 ms for 5 minutes at steady RPS."
— URL: https://apxml.com/courses/mlops-for-large-models-llmops/chapter-5-llm-monitoring-observability-maintenance/llm-performance-metrics

[FACT] Key LLM inference metrics requiring custom instrumentation: "TTFT (Time to First Token), ITL (Inter-Token Latency), TPOT (Time Per Output Token), Goodput — all require custom instrumentation beyond standard HTTP metrics."
— `P4_ai_model_plane.md` §3, S7, citing F05

---

### Phase 1 — Initial Refactoring

**Current rating:** RD=2, TE=2

**Re-derived rating:**

Phase 1 task: "Application-layer TTFT/quality monitoring against customer's inference service. No GPU-level monitoring (DCGM) — that's customer scope. SLO definition and alerting for inference latency."

The key scope reduction here is the elimination of GPU-level monitoring (DCGM Exporter, NVLink health, thermal/power monitoring via IPMI). This is the major complexity driver for the full on-premises S7 rating of 5/5. Under the scope split, the ISV only monitors application-layer metrics: TTFT, error rate, queue depth, and response quality at the HTTP boundary.

External evidence confirms that setting up Prometheus + Grafana dashboards for vLLM TTFT monitoring is achievable quickly — one source describes it as a "10-minute" setup for basic dashboards covering 8 key metrics (URL: https://www.dataunboxed.io/blog/monitoring-vllm-inference-servers-a-quick-and-easy-guide). However, defining production SLOs, configuring alerting rules, writing incident response runbooks, and integrating with the ISV's existing observability stack (built in P1 Phase 1) adds meaningful Phase 1 effort beyond dashboard setup.

The source file rates cloud-native S7 at 2/5 — the ISV must still instrument application-layer TTFT and per-customer cost attribution even in cloud-native. The on-premises (scope-reduced) task is structurally similar: TTFT monitoring against an external endpoint. The delta from cloud-native is: (a) the endpoint is customer-managed and may have different metric exposure formats, (b) no managed observability integration (CloudWatch, Azure Monitor) is available, and (c) the ISV must integrate with its self-hosted Prometheus stack rather than a managed backend.

RD=2 (Low) is appropriate for Phase 1: the work requires platform awareness but uses the same skill set as cloud-native monitoring. TE=2 (2–8 person-weeks) captures the SLO definition, alert rule authoring, dashboard creation, and runbook writing — this is well within 2–8 person-weeks for the bounded scope-reduced task.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=1

**Re-derived rating:**

Phase 2 task: "Set SLO thresholds based on customer's inference service performance characteristics."

This is fundamentally a configuration task: adjusting TTFT alert thresholds based on the baseline latency profile observed for each customer's inference endpoint. Some customers will have faster hardware; others slower. The SLO definition framework (Prometheus rules, Grafana alerting) is built in Phase 1. Phase 2 tunes the thresholds.

RD=1 (Minimal) is correct — no new monitoring capability is built per customer; only threshold configuration changes. TE=1 (less than 2 person-days per customer) is appropriate for reading baseline latency data and updating alert threshold configuration files.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=1, TE=2

**Re-derived rating:**

Phase 3 task: "SLO threshold adjustments. Monitoring dashboard maintenance. Per-customer inference quality tracking." Stated FTE: 0.1–0.5 FTE.

This is the rating requiring the most scrutiny per the research question. The research directive specifically asks: "Validate S7 Phase 3 FTE ranges (0.1–0.5) — are these too low for production monitoring?"

The production on-premises S7 FTE from the source file (pre-scope-split) is 1.5–2.5 FTE + 0.5 FTE on-call. The scope reduction eliminates GPU-level monitoring (DCGM), NVLink topology monitoring, thermal/IPMI monitoring, and GPU hardware RMA coordination. Under the scope split, the ISV only monitors:
- Application-layer TTFT and error rate per customer endpoint
- Dashboard maintenance as the ISV's products evolve
- SLO threshold adjustments as customer inference performance drifts

The F76 empirical study (156 production incidents, arXiv 2511.07424) found approximately 60% of high-severity incidents were inference engine failures, with 28% requiring hotfixes with the highest time-to-mitigation cost. Under the scope split, the ISV does not own the inference engine — the customer does. This means the ISV's monitoring responsibility is limited to detecting the symptom (elevated TTFT, increased error rate at the application boundary) and escalating to the customer. The ISV does not diagnose or remediate GPU-level or engine-level failures.

This substantially reduces the ongoing monitoring burden. The 0.1–0.5 FTE range spans:
- Lower bound (0.1 FTE): A small customer base (5–10 deployments) with stable inference performance, where monitoring is largely automated via Prometheus alerting and only requires attention on alert fires.
- Upper bound (0.5 FTE): A larger customer base (25–50 deployments) with heterogeneous inference performance, active per-customer SLO drift, and regular dashboard maintenance as the ISV's product evolves.

At 50 customers (the G1 model baseline), per-customer inference quality tracking adds overhead linearly. Each customer requires:
- Monitoring for endpoint availability and TTFT SLO compliance
- Escalation coordination when customer inference degrades
- Periodic SLO threshold re-calibration as customer hardware or model versions change

The 0.1–0.5 FTE range is plausible but the upper bound may still be conservative at the G1 model scale of 50 customers. However, the scope reduction from GPU monitoring is substantial enough that the stated range is defensible.

RD=1 (Minimal) is appropriate: application-layer TTFT monitoring is not meaningfully harder than cloud-native inference monitoring. The ISV monitors an HTTP endpoint in both cases. TE=2 (0.1–0.3 FTE per the Phase 3 TE scale) is at the lower half of the stated 0.1–0.5 FTE research range — the same calibration tension noted for S6.

[STATISTIC] At cloud-native tier, the source estimates 0.1–0.25 FTE for S7 ongoing (provider metric dashboards, application-layer TTFT instrumentation). The on-premises scope-reduced equivalent is estimated at 0.1–0.5 FTE — a 2x upper-bound increase that captures per-customer overhead without GPU infrastructure burden.
— `P4_ai_model_plane.md` §3, S7 FTE Estimates; `analysis/three_phase_on_prem_ratings.md` §6

**Re-derived TE:** TE=2 (0.1–0.3 FTE) is accurate for the median case (15–25 customers) but understates the upper-bound case (50+ customers, 0.4–0.5 FTE). The overall rating is within acceptable calibration tolerance given the three-phase file's explicit "Partial" scaling designation.

**Confidence:** Medium — the 0.1–0.5 FTE range is directionally correct but the TE=2 calibration (0.1–0.3 FTE) does not fully capture the upper bound of the stated research range. For a 50-customer deployment at the G1 scale, 0.5 FTE is more appropriate than the TE=2 midpoint of ~0.2 FTE.

**Verdict:** ACCURATE (within tolerance; note calibration tension between TE=2 scale midpoint and stated 0.5 FTE upper bound)

**Interview question:** To a Site Reliability Engineer or AI Platform Engineer at an ISV with 20+ on-premises customer deployments: "How much time per week does your team spend tracking inference quality and TTFT compliance across customer endpoints — specifically excluding GPU-level monitoring that the customer owns? Does that effort scale linearly with customer count, or does automation absorb most of it?"

---

## S8 — Model Lifecycle Management

### Ground Truth Extraction

[STATISTIC] "Cloud-Native: 2 | Managed K8s: 3 | On-Premises: 4"
— `P4_ai_model_plane.md` §3, S8 difficulty table; §4 Summary Difficulty Matrix
Source: `analysis/review/GT4_P4_ground_truth.md` §S8

[STATISTIC] "On-Premises FTE (pre-scope-split): 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S8 FTE Estimates; §5 FTE Summary Table

[FACT] Under customer-provides-GPU scope split, S8 ISV task: "Customer manages model artifacts and versions. ISV tracks which models are available and selects version in API calls. Minimal refactoring."
— `analysis/three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S8 Notes

[STATISTIC] "Phase 3 revised ISV FTE for S8 under scope split: 0.05–0.15 FTE"
— `analysis/three_phase_on_prem_ratings.md` §6, P4 Phase 3 table

[FACT] "Azure OpenAI and Vertex AI handle model versioning, deprecation scheduling, and rollover on the provider's cadence — ISV cannot control the deprecation timeline."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing F18 and F26

[FACT] "Model Lifecycle rated 4/5 on-premises, 3/5 managed K8s, 1/5 cloud-native in W05S difficulty table."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing W05S

[FACT] The scope reduction for S8 is maximal: customer owns "model artifact storage (S3, NVMe, shared filesystem) and access controls; download automation and checksum validation; model version registry and promotion workflow; A/B traffic split configuration; rollback trigger definition; model storage capacity planning."
— `P4_ai_model_plane.md` §3, S8 ("What the ISV owns") versus scope split

---

### Phase 1 — Initial Refactoring

**Current rating:** RD=1, TE=1

**Re-derived rating:**

Phase 1 task: "Customer manages model artifacts and versions. ISV tracks which models are available and selects version in API calls. Minimal refactoring."

The full on-premises S8 task includes operating a local model registry, managing NVMe storage arrays, coordinating model swaps across multi-node inference clusters, implementing rollback automation, and managing model checksum validation and audit logging. Under the scope split, all of this transfers to the customer. The ISV's residual task is:
- Discovering which models the customer exposes at their inference endpoint
- Updating API call configuration to specify the correct model version string

This is configuration-level work. The cloud-native analog (selecting a model version string in the API call) is essentially the same task. RD=1 (Minimal) correctly describes this. TE=1 (less than 2 person-weeks) is appropriate — the work is bounded and low-complexity.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=1

**Re-derived rating:**

Phase 2 task: "Inventory which models customer provides. Version compatibility verification."

Per customer: the ISV must discover which model versions the customer runs (e.g., Llama 3.1 70B, Mixtral 8x7B), verify that its application is tested against those model versions, and document any capability limitations (context window size, feature support). This is documentation and testing work, not engineering.

RD=1, TE=1 is correct — per-customer model inventory is a bounded discovery task.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=1, TE=1

**Re-derived rating:**

Phase 3 task: "Track customer model availability. Minimal ISV effort — customer manages artifacts." Stated FTE: 0.05–0.15 FTE. "Scales with N? No."

The "No" scaling designation requires attention. If a customer upgrades their model (e.g., from Llama 3.1 70B to Llama 3.3 70B), the ISV must:
- Verify its application still functions correctly with the new model version
- Update any model-version-specific prompts, response parsing, or capability checks
- Potentially update feature flags for model-dependent capabilities

This is reactive work triggered by customer model changes, not ISV-controlled. The "No" scaling designation is plausible because the ISV does not proactively manage model versions — it reacts to customer notifications. The per-event cost is low, and events are infrequent.

The 0.05–0.15 FTE range is very low — it implies roughly 1–3 hours per week of model lifecycle tracking. This is credible for a customer base where model versions are stable and customers change models infrequently (once or twice per year per customer). For customers with aggressive model update cadences, the per-customer maintenance cost could be higher, but "No" scaling is defensible as a median-case assumption.

RD=1, TE=1 (under 0.1 FTE) is at the edge of what the research FTE range (0.05–0.15 FTE) supports — the TE=1 calibration is "< 0.1 FTE" which aligns with the lower bound of 0.05 FTE but is below the midpoint of the stated range (0.10 FTE).

**Confidence:** High

**Verdict:** ACCURATE

---

## Cross-Subsegment Validation: The Scope Reduction Model

The three-phase file's central claim is that P4 is "nearly eliminated" under the customer-provides-GPU-and-models scope, with an all-phase average of RD 1.3 / TE 1.7 across S1, S6, S7, S8.

[FACT] Grand Summary Key Finding 4: "P4 (AI Model Plane) is nearly eliminated under the customer-provides-GPU-and-models scope. All-phase average of RD 1.3 / TE 1.7. The ISV's AI-related effort is in P2 (agent orchestration) and P3 (embedding/RAG pipelines), not P4."
— `analysis/three_phase_on_prem_ratings.md` §8

This finding is directionally confirmed. The source pre-scope-split FTE for S1, S6, S7, S8 on-premises totals 0.10–0.30 + 0.50–1.00 + 1.50–2.50 + 0.50–1.00 = 2.60–4.80 FTE. The post-scope-split Phase 3 FTE is 0.45–1.45 FTE — a reduction to approximately 17–30% of the original. The "nearly eliminated" characterization is substantiated.

[FACT] Reduced ISV P4 FTE after scope split: S1 (0.1–0.3) + S6 (0.2–0.5) + S7 (0.1–0.5) + S8 (0.05–0.15) = 0.45–1.45 FTE total Phase 3 ongoing.
— `analysis/three_phase_on_prem_ratings.md` §6, P4 Phase 3 table; `analysis/review/GT4_P4_ground_truth.md` §Table 4

The boundary with P2 (AL09 Agentic AI Orchestration) is relevant here. See `RP2b_P2_resilience_ai_testing.md` §AL09: AL09 is rated Phase 3 RD=3, TE=4 — substantially higher than any P4 ISV-scope subsegment in Phase 3. The three-phase file's assertion that "AI-related effort is in P2 not P4" under the scope split is consistent with the RP2b review findings. The P2/P4 boundary is drawn at: "Agent orchestration code (LangGraph, MCP servers, guardrails) is portable [P2]. Main refactoring: integrate with customer's inference endpoints (replacing Bedrock/Azure OpenAI calls)" — the endpoint integration piece crosses into P4/S1. See [file: RP2b_P2_resilience_ai_testing.md §AL09 Phase 1].

[FACT] AL09 (AI/ML Orchestration, P2) rates on-premises at 5/5 difficulty with 4.0–7.0 FTE, ranked #1 hardest on-premises subsegment across all four planes (deduplicated). S6, S7, S8 in their reduced ISV-scope form do not appear in the Top 10 hardest subsegments list.
— `analysis/review/GT5_cross_reference_ground_truth.md` §Section 3, Top 10 Hardest Subsegments table

---

## S1 Phase 1 RD=1: The Trivial Swap Question

The research question asks specifically: "Is S1 Phase 1 RD=1 correct — is swapping from Bedrock/Azure OpenAI to customer inference endpoints truly trivial?"

**Finding: No. RD=1 is too low. The correct rating is RD=2.**

The evidence against RD=1:

1. **Authentication re-implementation is non-trivial.** Bedrock uses AWS SigV4 signatures. Azure OpenAI uses Azure AD bearer tokens. Vertex AI uses Google service account credentials. A customer's vLLM endpoint uses bearer token, API key, or mTLS — a fundamentally different auth pattern. Replacing cloud IAM auth with customer-defined auth requires re-implementing the HTTP client authentication layer in the ISV's codebase. This is not a configuration change.

2. **Bedrock schema delta is not zero.** The Bedrock API "requires one-to-one mapping of interfaces, as well as the JSON responses returned by the APIs." The system prompt is a separate parameter in Bedrock, not within the messages array as in OpenAI format. This delta is real code that must change (URL: https://www.improving.com/thoughts/switch-from-openai-to-amazon-bedrock/).

3. **Error handling is provider-specific.** Cloud provider error codes, retry-after headers, and quota exhaustion responses differ from self-hosted vLLM error responses. The ISV's retry and circuit-breaker logic must be re-implemented against the new upstream's error contract.

4. **The source file itself rates on-premises S1 at 2/5 (not 1/5).** The delta from cloud-native is +1, indicating "Low" difficulty increase. RD=2 in the three-phase file language means "Minor changes; same skill set, slightly more work" — which precisely matches the +1 source delta and the bounded-but-real engineering work described above.

5. **The mitigating factor is vLLM's OpenAI compatibility.** vLLM exposes `/v1/chat/completions` in OpenAI format (URL: https://docs.vllm.ai/en/stable/serving/openai_compatible_server/). If the ISV was originally built against the OpenAI API (not Bedrock), the schema delta is near-zero and only auth + error handling change. This would bring the task close to RD=1. However, the research corpus focuses on cloud-native ISVs using Bedrock/Azure OpenAI/Vertex AI — not OpenAI direct — making the schema delta real for a significant proportion of ISVs.

**Verdict:** RD=1 understates the Phase 1 S1 refactoring effort for ISVs migrating from Bedrock or Vertex AI. RD=2 is correct.

---

## Summary Rating Table

| Subsegment | Phase | Current RD | Re-derived RD | Current TE | Re-derived TE | Verdict |
|---|:---:|:---:|:---:|:---:|:---:|---|
| S1 Managed API Integration | 1 | 1 | **2** | 2 | 2 | **ADJUST RD 1→2** |
| S1 Managed API Integration | 2 | 1 | 1 | 2 | 2 | ACCURATE |
| S1 Managed API Integration | 3 | 1 | 1 | 2 | 2 | ACCURATE |
| S6 Model Routing | 1 | 2 | 2 | 2 | 2 | ACCURATE |
| S6 Model Routing | 2 | 1 | 1 | 2 | 2 | ACCURATE |
| S6 Model Routing | 3 | 2 | 2 | 2 | 2–3* | ACCURATE (flag at scale) |
| S7 Inference Monitoring | 1 | 2 | 2 | 2 | 2 | ACCURATE |
| S7 Inference Monitoring | 2 | 1 | 1 | 1 | 1 | ACCURATE |
| S7 Inference Monitoring | 3 | 1 | 1 | 2 | 2–3* | ACCURATE (flag at scale) |
| S8 Model Lifecycle | 1 | 1 | 1 | 1 | 1 | ACCURATE |
| S8 Model Lifecycle | 2 | 1 | 1 | 1 | 1 | ACCURATE |
| S8 Model Lifecycle | 3 | 1 | 1 | 1 | 1 | ACCURATE |

*At N=50 customers (G1 model scale), TE for S6 Phase 3 and S7 Phase 3 may be more accurately calibrated at TE=3 (0.3–1.0 FTE) rather than TE=2 (0.1–0.3 FTE). The stated research FTE ranges in the three-phase file already capture this (0.2–0.5 for S6, 0.1–0.5 for S7), but the TE rating does not align with the upper bound of those ranges.

**Count:** 1 ADJUST, 11 ACCURATE (10 confirmed, 2 flagged with at-scale caveats)

---

## Key Findings

1. **S1 Phase 1 RD=1 is incorrect and should be adjusted to RD=2.** Swapping from Bedrock or Vertex AI to a customer's vLLM inference endpoint is not trivial — it requires auth re-implementation (cloud IAM to customer-defined auth), request schema updates (especially for Bedrock migrants), and error handling re-implementation against a different upstream error contract. vLLM's OpenAI-compatible API reduces schema delta for OpenAI-native ISVs but does not eliminate the auth and error-handling work.

2. **The scope reduction model is correctly implemented.** Transferring S2–S5 to customer scope and retaining S1, S6, S7, S8 in reduced form accurately reflects the ISV's residual P4 burden. The characterization of P4 as "nearly eliminated" is substantiated: Phase 3 ISV FTE drops from 2.60–4.80 FTE (full on-premises) to 0.45–1.45 FTE under the scope split.

3. **S6 and S7 Phase 3 FTE upper bounds (0.5 FTE) are plausible but create calibration tension with the TE=2 rating (0.1–0.3 FTE scale).** At the G1 model scale of 50 customers, ongoing routing configuration maintenance (S6) and per-customer TTFT tracking (S7) would likely consume 0.3–0.5 FTE each — the upper bound of the stated ranges aligns better with TE=3. This is a flag, not a correction, because the three-phase file's explicit "Partial" scaling notation acknowledges the uncertainty.

4. **The AI-related ISV effort correctly lives in P2 (AL09) and P3 (DS9, DS10), not P4.** AL09 (Agentic AI Orchestration) is the #1 hardest on-premises subsegment across all four planes at RD=5 (source difficulty). Under the customer-provides-GPU scope, the ISV's P4 ISV-scope subsegments remain at RD≤2 across all phases. This asymmetry is strategically significant: ISVs planning on-premises deployments should budget for AI agent orchestration complexity (P2/AL09) and embedding pipeline complexity (P3/DS9–DS10), not P4 routing and monitoring.

5. **External production evidence supports the LiteLLM and inference monitoring ratings.** LiteLLM production deployment complexity is real but bounded — a structured config.yaml, Redis for multi-instance coordination, and a separate health-check process are the primary production requirements (URL: https://docs.litellm.ai/docs/proxy/prod). TTFT monitoring via Prometheus and Grafana is achievable quickly for basic setups (URL: https://www.dataunboxed.io/blog/monitoring-vllm-inference-servers-a-quick-and-easy-guide), confirming that Phase 1 S7 RD=2 and TE=2 are appropriate for the scope-reduced ISV task.

---

## Sources

| Source | Type | URL / Path |
|---|---|---|
| `P4_ai_model_plane.md` §3–§5 | Primary ground truth | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P4_ai_model_plane.md` |
| `analysis/three_phase_on_prem_ratings.md` §4–§8 | File under review | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| `analysis/review/GT4_P4_ground_truth.md` | Ground truth extraction | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT4_P4_ground_truth.md` |
| `analysis/review/GT5_cross_reference_ground_truth.md` | Cross-plane reference | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` |
| `analysis/review/RP2b_P2_resilience_ai_testing.md` §AL09 | P2/P4 boundary reference | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP2b_P2_resilience_ai_testing.md` |
| vLLM OpenAI-compatible API documentation | External — schema compatibility | https://docs.vllm.ai/en/stable/serving/openai_compatible_server/ |
| Improving.com: Switch from OpenAI to Amazon Bedrock | External — Bedrock schema delta | https://www.improving.com/thoughts/switch-from-openai-to-amazon-bedrock/ |
| LiteLLM load balancing documentation | External — routing configuration complexity | https://docs.litellm.ai/docs/proxy/load_balancing |
| LiteLLM production best practices documentation | External — production operational requirements | https://docs.litellm.ai/docs/proxy/prod |
| dataunboxed.io: Monitoring vLLM Inference Servers | External — TTFT monitoring setup effort | https://www.dataunboxed.io/blog/monitoring-vllm-inference-servers-a-quick-and-easy-guide |
| apxml.com: LLM Performance Metrics and SLO definition | External — TTFT SLO examples | https://apxml.com/courses/mlops-for-large-models-llmops/chapter-5-llm-monitoring-observability-maintenance/llm-performance-metrics |
| arXiv 2511.07424 (via F76) | External — 156 production inference incidents | Referenced via `P4_ai_model_plane.md` §3, S7 Evidence |
| TrueFoundry: LiteLLM Review 2026 | External — LiteLLM operational context | https://www.truefoundry.com/blog/a-detailed-litellm-review-features-pricing-pros-and-cons-2026 |
