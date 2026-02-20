# RP2b — P2 Application Logic Review: AL06 Through AL10
## Resilience, Multi-Tenant, Observability, AI Orchestration, and Testing

**Reviewer Role:** Rating Accuracy Auditor — P2 Application Logic (AL06–AL10)
**Date:** 2026-02-19
**Files Under Review:** `analysis/three_phase_on_prem_ratings.md` (P2 Application Logic sections)
**Ground Truth Sources:** `analysis/review/GT2_P2_ground_truth.md`, `analysis/review/GT5_cross_reference_ground_truth.md`
**Scope:** 5 subsegments × 3 phases × 2 dimensions (RD + TE) = 30 ratings reviewed

---

## Executive Summary

The three-phase ratings for AL06 through AL10 are broadly accurate, with the most important finding being a systematic under-rating of AL09 (AI/ML Orchestration) Phase 3 Relative Difficulty. The ground truth establishes AL09 as the hardest on-premises P2 subsegment at difficulty 5/5 (See GT2: P2 §3; GT5: S1 Top 10, Rank 1), yet the three-phase file rates Phase 3 at RD=3 — a two-point gap that understates the ongoing maintenance burden of a rapidly evolving, multi-dependency AI stack. AL07 (Multi-Tenant Isolation) Phase 2 rating of RD=1, TE=1 is the second most consequential finding: ground truth confirms tier-invariant difficulty of 3/5 meaning Phase 2 hardware heterogeneity does not affect isolation logic, but the file's RD=1 accurately reflects the absence of per-customer isolation code changes rather than a reduction in the underlying difficulty of the domain. Two subsegments (AL06, AL08) are accurately rated across all phases with high confidence. AL10 Phase 3 Total Effort is confirmed as legitimately "Scales with N" but the linear scaling claim is directionally correct while the exact rate of scaling is a known data gap in the source corpus.

---

## Rating Methodology Note

Ratings extracted from `analysis/three_phase_on_prem_ratings.md` are the ratings-under-review. Ground truth difficulty scores are sourced from `analysis/P2_application_logic.md` as extracted in `GT2_P2_ground_truth.md`. The three-phase rating file uses a different scale than the source P2 difficulty ratings: the P2 file rates difficulty relative to absolute deployment complexity (1–5 across all tiers), while the three-phase file rates Relative Difficulty (RD) as the delta versus cloud-native baseline. These are not directly numerically comparable but must be logically consistent.

---

## AL06 — Resilience Patterns and Runtime Behavior

### Ground Truth (from GT2)

[STATISTIC] "AL06: CN=2, MK8s=3, OP=4. FTE: CN 0.15–0.3, MK8s 0.3–0.6, OP 0.75–1.5. Tier-sensitive. Delta = 2."
— GT2_P2_ground_truth.md, AL06 section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

[FACT] "Kubernetes Cluster Autoscaler does not support on-premises bare metal because it cannot create or delete VMs. Bare metal node provisioning takes up to 8 minutes."
— GT2_P2_ground_truth.md, AL06 Notable Caveats, citing F72: Application Resilience Patterns
URL: https://github.com/kubernetes/autoscaler/issues/1060

[FACT] "Circuit breakers and health probes are largely application-level (Resilience4j, Polly). Minor adaptation for self-hosted service endpoints."
— `analysis/three_phase_on_prem_ratings.md`, P2 Phase 1, AL06 Notes

### Phase 1 — Initial Refactoring

**Current rating:** RD=2, TE=2

**Re-derived rating:** The P2 source rates the OP-CN delta at 2 points (CN=2, OP=4). For Phase 1, the refactoring work is primarily adapting circuit breaker timeout budgets and health probe configurations from cloud-managed service endpoints to self-hosted equivalents. Resilience4j and Polly are tier-agnostic libraries. The main change is that the ISV must add awareness of self-hosted service startup sequencing (Consul, Vault) and bare metal autoscaling limitations. The P2 source confirms "graceful shutdown and readiness probes are K8s-standard." An RD of 2 (low, same skill set) is consistent with a 2-point tier delta where the work is configuration-level adaptation, not architectural reconstruction. TE=2 (2–8 person-weeks one-time) aligns with the OP FTE range of 0.75–1.5 for ongoing work, with Phase 1 being a bounded one-time task.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=1

**Re-derived rating:** The three-phase file notes "Resilience patterns are application-level. Timeouts may need tuning for customer's network latency profile — minor config." The P2 source confirms resilience patterns operate at the application code level and are tier-invariant at the code layer. Per-customer hardware differences affect network latency between pods, but circuit breaker thresholds are typically set at the application layer via environment variables or configuration files, not per-customer code changes. External research on bare metal Kubernetes confirms "circuit breakers work best when layered with retries and timeouts, which applies universally" but does not indicate hardware-specific code changes are required.

[FACT] "Even when using Horizontal Pod Autoscaler or Cluster Autoscaler, errors caused by network latency continue, and autoscaling may worsen the situation by applying more pressure to already impaired downstream dependencies."
— Growin blog, 2025, "How to Build Resilient Backends with Kubernetes: 7 Lessons from 2025"
URL: https://www.growin.com/blog/resilient-backends-kubernetes-2025/

The latency observation supports the RD=1 verdict: the ISV may tune timeout values per customer network profile, but this is configuration, not code. RD=1, TE=1 (less than 2 person-days) is consistent.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=2, TE=2

**Re-derived rating:** The three-phase file rates Phase 3 as "resilience pattern tuning, circuit breaker threshold adjustments. Minor ongoing work." The P2 FTE for OP on this subsegment is 0.75–1.5 FTE annually, classified as "ongoing maintenance." TE=2 corresponds to 0.1–0.3 FTE annually — this is lower than the P2 OP FTE midpoint. However, the P2 FTE of 0.75–1.5 is the absolute OP cost; the three-phase TE scale measures relative to the cloud-native baseline. Cloud-native equivalent for resilience is also non-zero (managed SDK maintenance, SLA monitoring). RD=2 (low tier delta) is consistent with P2's delta=2 across the tier scale. The "Scales with N?" column is marked "No" — consistent with AL06 being application-code-level work that does not vary per customer. The rating is internally consistent.

**Confidence:** High

**Verdict:** ACCURATE

---

## AL07 — Multi-Tenant Isolation Logic

### Ground Truth (from GT2)

[FACT] "Multi-Tenant Isolation Logic is the only tier-invariant component at difficulty 3/5 across all models, because it is a software architecture problem."
— GT2_P2_ground_truth.md, AL07 section, citing F73: MECE ISV Developer Responsibility Framework

[FACT] "AL07 is tier-invariant at difficulty 3 — consistently moderate difficulty because tenant isolation is a software architecture problem that no platform can fully abstract."
— GT2_P2_ground_truth.md, Tier-Invariant Classification Summary, citing P2 §5

[STATISTIC] "AL07 FTE: CN 0.5–1.0, MK8s 0.5–1.0, OP 0.75–1.5. Tier-invariant. Delta = 0."
— GT2_P2_ground_truth.md, AL07 section

[FACT] "No authoritative benchmark exists for the incremental FTE cost of retrofitting a tenant-context framework into an existing production codebase (AL07). The claim that it is 'prohibitively expensive' is supported qualitatively in F73 but lacks a quantitative study."
— GT2_P2_ground_truth.md, AL07 Notable Caveats, citing P2 §7, Known Data Gaps

External research on the hardware heterogeneity question:

[FACT] "Resource spikes from one tenant can degrade performance for others, making traditional namespaces a poor fit for environments with strong isolation, customization, or scalability requirements."
— vCluster blog, "Multi-tenancy in 2025 and beyond"
URL: https://www.vcluster.com/blog/multi-tenancy-in-2025-and-beyond

[FACT] "The fundamental challenge of multi-tenancy is balancing isolation against resource sharing: perfect isolation requires separate clusters per tenant eliminating sharing benefits, while no isolation creates a security and operational nightmare where any tenant can affect others."
— Atmosly, "Kubernetes Multi-Tenancy: Complete Implementation Guide 2025"
URL: https://atmosly.com/blog/kubernetes-multi-tenancy-complete-implementation-guide-2025

### Phase 1 — Initial Refactoring

**Current rating:** RD=1, TE=1

**Re-derived rating:** The three-phase file states "Zero refactoring. Multi-tenancy is enforced in application code (tenant-context middleware, row-level security). Tier-invariant at difficulty 3 — same work everywhere." This is accurate as a statement of Phase 1 scope. The P2 source confirms tier-invariance: the isolation code does not change when moving from cloud-native to on-premises. RD=1 (minimal, trivial adaptation) correctly conveys that no refactoring is required. The "same work everywhere" note is factually consistent with P2's delta=0.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=1

**Re-derived rating:** This is the most analytically significant rating in AL07. The three-phase file claims "Multi-tenancy is application-level. No per-customer changes." The P2 source confirms tier-invariance (the isolation logic is in application code, not infrastructure), and the S1 synthesis notes that "In SaaS multi-tenancy, the tenant does not interface directly with the Kubernetes API; the application is responsible for interfacing with the Kubernetes API on the tenant's behalf."

The specific research question is: does hardware heterogeneity affect multi-tenant isolation logic? The answer requires distinguishing between two layers:

1. **Application-layer isolation code** (tenant-context middleware, row-level security, ABAC/RBAC policies): tier-invariant. No per-customer changes required.
2. **Platform-layer isolation** (namespace quotas, network policies, vCluster): P1 (Control Plane) scope, not AL07.

External research confirms that hardware heterogeneity creates performance isolation challenges at the platform level (noisy neighbor effects, resource contention on heterogeneous NIC or CPU configurations), but these are P1 (CP-01, CP-02) concerns. The application middleware enforcing tenant data isolation does not change based on whether the customer has Dell PowerEdge or HPE ProLiant servers.

However, one nuance exists: on-premises deployments with heterogeneous storage controllers may create performance variance that could cause tenant A's workload to bleed into tenant B's response time SLOs. This is a performance isolation concern, not a data isolation concern. The AL07 scope in P2 covers "application middleware and enforcement code layer only" — not performance isolation. Within that scope, RD=1, TE=1 is accurate.

**Interview Question:** When deploying to a customer with a heterogeneous CPU/storage environment, have you ever needed to modify application-layer tenant context middleware (e.g., request routing, row-level security filters) specifically because of that customer's hardware characteristics? Or have all per-customer hardware adaptations occurred at the infrastructure configuration layer?

**Confidence:** Medium (the scope boundary between application-layer isolation and platform-layer performance isolation is well-defined in the source, but the practical boundary may blur in on-premises deployments where performance isolation bleeds into application-layer timeout and retry behavior that is tenant-specific)

**Verdict:** ACCURATE — within stated scope. The scope boundary (application middleware only, not performance isolation) is the critical assumption. If the ISV's multi-tenant architecture implements per-tenant SLOs at the application layer (e.g., per-tenant circuit breaker thresholds), hardware heterogeneity could cause per-customer application code changes, which would warrant ADJUST upward to RD=2.

---

### Phase 3 — Ongoing Support

**Current rating:** RD=1, TE=2

**Re-derived rating:** "Multi-tenancy framework is stable. Occasional refinement for new data paths or isolation requirements. Same across tiers." TE=2 (0.1–0.3 FTE annually) is lower than the P2 OP FTE of 0.75–1.5. Again, the P2 FTE represents absolute OP cost while the three-phase TE represents relative effort. RD=1 correctly reflects that multi-tenant isolation code maintenance is identical across tiers (delta=0 in P2). The "Scales with N? No" designation is consistent: isolation framework maintenance is a product engineering cost unaffected by customer count.

**Confidence:** High

**Verdict:** ACCURATE

---

## AL08 — Observability Instrumentation and AI Telemetry

### Ground Truth (from GT2)

[STATISTIC] "AL08: CN=2, MK8s=2, OP=3. FTE: CN 0.2–0.4, MK8s 0.3–0.6, OP 0.5–1.0. Tier-sensitive. Delta = 1."
— GT2_P2_ground_truth.md, AL08 section

[FACT] "OpenTelemetry's GenAI Semantic Conventions are now part of the official specification (v1.37+), defining standard attributes for `gen_ai.request.model`, `gen_ai.usage.input_tokens`, and `gen_ai.provider.name`."
— GT2_P2_ground_truth.md, AL08 Key Operational Characteristics, citing F73
URL: https://opentelemetry.io/docs/specs/semconv/gen-ai/

[FACT] "Langfuse self-hosted (for AI telemetry) requires PostgreSQL + ClickHouse + Redis/Valkey + S3 blob storage — a substantial infrastructure commitment."
— GT2_P2_ground_truth.md, AL08 Notable Caveats, citing P2 §3, AL08 Tier Analysis (On-Premises)
URL: https://langfuse.com/self-hosting

[FACT] "OpenTelemetry SDK is tier-agnostic by design."
— `analysis/three_phase_on_prem_ratings.md`, P2 Phase 1, AL08 Notes

### Phase 1 — Initial Refactoring

**Current rating:** RD=2, TE=2

**Re-derived rating:** The three-phase file states "Update OTLP exporter endpoints to point at self-hosted Prometheus/Loki/Tempo instead of managed backends." This precisely describes the Phase 1 scope for AL08: the SDK instrumentation code is unchanged; only the exporter destination changes. The P2 delta of 1 (CN=2, OP=3) reflects the added complexity of verifying that trace/metric propagation works correctly against self-hosted backends. RD=2 (low, same skill set) is consistent with a delta=1 subsegment at Phase 1. The OTel SDK's tier-agnostic design is a well-supported fact.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=1

**Re-derived rating:** "OTel instrumentation is standardized. Exporter endpoints configured by P1." This is a precise scope allocation: the instrumentation code (AL08 scope) does not change per customer, and the exporter endpoint configuration is handled by the P1 observability infrastructure stack (CP-05). The P2 FTE range of 0.5–1.0 OP vs 0.2–0.4 CN includes ongoing instrumentation maintenance, not per-customer changes. RD=1, TE=1 correctly reflects zero per-customer application-layer instrumentation changes.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=2, TE=2

**Re-derived rating:** "Instrumentation updates as new services or features are added. OTel SDK version upgrades." The P2 source notes AL08 is tier-sensitive with delta=1. The ongoing maintenance differential is driven by the self-hosted AI telemetry stack (Langfuse + ClickHouse + Redis + PostgreSQL + S3) requiring more instrumentation coordination than cloud-native managed equivalents. TE=2 (0.1–0.3 FTE annually) is consistent with the P2 OP FTE range of 0.5–1.0, given that the three-phase scale measures the delta over cloud-native. "Scales with N? No" is accurate: instrumentation code maintenance is a fixed product engineering cost. The OTel AI Agent observability semantic conventions are "under active development" (GT2 cites the CNCF #otel-genai-instrumentation working group), which adds ongoing SDK update burden, supporting TE=2.

**Confidence:** High

**Verdict:** ACCURATE

---

## AL09 — AI/ML Orchestration, Agent Pipelines, and MCP Integration

### Ground Truth (from GT2 and GT5)

[STATISTIC] "AL09: CN=2, MK8s=3, OP=5. FTE: CN 0.5–1.2, MK8s 2.0–4.0, OP 6.0–10.0 (stated), 4.0–7.0 (deduplicated). Tier-sensitive. Delta = 3 (largest in framework, tied with AL05)."
— GT2_P2_ground_truth.md, AL09 section

[FACT] "AL09 is ranked #1 hardest on-premises subsegment across all 38 subsegments in S1."
— GT5_cross_reference_ground_truth.md, Section 3: S1 Top 10 Hardest Subsegments, Rank 1
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

[FACT] "On-premises AI agent infrastructure requires 7 distinct platform layers: tool registry, sandboxed execution, state management, workflow orchestration, metering, security sandboxing, GPU scheduling."
— GT2_P2_ground_truth.md, AL09 Key Operational Characteristics, citing F38: On-Premises AI Agent Infrastructure

[FACT] "LangGraph 1.0 reached stable release October 2025; 6.17 million monthly downloads."
— GT2_P2_ground_truth.md, AL09 Key Operational Characteristics, citing F07: AI Agent Frameworks
URL: https://blog.langchain.com/langchain-langgraph-1dot0/

[FACT] "Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027."
— GT2_P2_ground_truth.md, AL09 Key Operational Characteristics, citing W01S
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

External research on release cadence and maintenance burden:

[STATISTIC] "LangGraph: 47+ pages of GitHub release history. Current pace approximately 12–15 releases per month (8 releases in first 19 days of February 2026 alone). LangGraph 1.0 policy: no breaking changes until 2.0, with minor releases every 2–3 months."
— GitHub releases page: https://github.com/langchain-ai/langgraph/releases (observed 2026-02-19)

[FACT] "langgraph-prebuilt==1.0.2 (released October 29, 2025) introduced a breaking change by adding a required runtime parameter to ToolNode.afunc, affecting users upgrading from 1.0.1 to 1.0.2."
— GitHub issue #6363, langchain-ai/langgraph
URL: https://github.com/langchain-ai/langgraph/issues/6363

[FACT] "LangGraph comes with learning curve and maintenance overhead; orchestration, deployment, and governance are on you unless paired with platforms."
— Langflow blog, "The Complete Guide to Choosing an AI Agent Framework in 2025"
URL: https://www.langflow.org/blog/the-complete-guide-to-choosing-an-ai-agent-framework-in-2025

[FACT] "The 'rapidly evolving ecosystem' claim: LangGraph 1.0 represents a commitment to stability with no breaking changes until 2.0. Minor releases every 2–3 months. Patch releases up to a few times per week."
— LangChain release policy documentation
URL: https://docs.langchain.com/oss/python/release-policy

### Phase 1 — Initial Refactoring

**Current rating:** RD=2, TE=3

**Re-derived rating:** The three-phase file notes "Agent orchestration code (LangGraph, MCP servers, guardrails) is portable. Main refactoring: integrate with customer's inference endpoints (replacing Bedrock/Azure OpenAI calls), self-hosted Temporal for workflow orchestration, self-hosted Langfuse for observability. Testing across new dependency topology is the bulk of effort." This accurately reflects the Phase 1 scope distinction: the orchestration code (AL09 scope) is largely portable; the infrastructure dependencies (vLLM, Langfuse, Temporal) require integration work. The P2 source rates OP at 5/5 for the full on-prem stack, but Phase 1 is only the refactoring from cloud-native to open K8s, not the standing up of all infrastructure. TE=3 (2–6 person-months one-time) is consistent with the complexity of re-pointing a LangGraph + MCP + Langfuse stack from cloud-managed APIs to self-hosted endpoints, including integration testing. RD=2 (low relative difficulty — same code, different endpoints) is justified because the orchestration logic itself does not change, only its dependencies.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=1, TE=2

**Re-derived rating:** "Adapt to customer's specific AI model availability — which models they host, context window sizes, endpoint URLs, rate limits. Feature flags for model-dependent capabilities." This is correct: the per-customer variation in AL09 is which models the customer provides (aligning with the customer-owns-GPU scope). The orchestration code uses feature flags and configuration to adapt, not per-customer code branches. TE=2 (2–5 person-days) is reasonable for mapping model availability and configuring endpoint URLs per customer. The P2 FTE of 4.0–7.0 (deduplicated) represents the full annual ongoing cost at cloud-native scale, not per-customer Phase 2 work.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=3, TE=4

**Re-derived rating:** This is the most significant finding in this review. The three-phase file rates Phase 3 RD=3 ("Moderate — meaningful new work; requires platform awareness") with the note "Rapidly evolving ecosystem. LangChain/LangGraph version upgrades, new agent patterns, guardrail policy updates, MCP protocol evolution. High effort because the AI/agent stack changes faster than any other application subsegment."

The ground truth establishes AL09 as OP=5/5 — the single hardest on-premises subsegment in the entire 38-subsegment framework (See GT5, Rank 1). The ongoing maintenance burden includes:

1. LangGraph version upgrades (patch releases up to several times per week; breaking changes documented even within minor releases: e.g., langgraph-prebuilt 1.0.2 breaking change)
2. Temporal upgrades across N customer environments (each requiring Cassandra + Elasticsearch coordination)
3. Langfuse upgrades (PostgreSQL + ClickHouse + Redis/Valkey + S3 stack)
4. LiteLLM routing layer updates for new model APIs
5. MCP protocol evolution (donated to Linux Foundation AAIF December 2025; specification still evolving)
6. Guardrail policy updates (LlamaFirewall / OpenGuardrails)

The three-phase file itself acknowledges "the AI/agent stack changes faster than any other application subsegment" and marks it as a divergence case (TE exceeds RD by 1). However, if the AI stack changes faster than any other subsegment, and the underlying on-premises difficulty is rated 5/5 (extreme) in the source, then RD=3 (moderate) appears to understate the relative difficulty of keeping this stack current on-premises vs. cloud-native.

Cloud-native AL09 maintenance: LangGraph SDK updates applied once; Bedrock/Azure OpenAI model APIs are managed (automatic version transitions, no infrastructure upgrades).

On-premises AL09 maintenance: LangGraph SDK updates applied across N customer environments each running self-hosted Temporal + Langfuse + LiteLLM + guardrail stacks at different versions, requiring tested upgrade paths per customer's K8s version.

The delta between cloud-native and on-premises Phase 3 maintenance is closer to RD=4 (high — substantially harder; requires specialist knowledge) than RD=3, given that the on-premises ISV must coordinate six distinct software stack upgrades (LangGraph, Temporal, Langfuse, LiteLLM, guardrails, MCP tooling) across N customer environments, while the cloud-native ISV upgrades only the orchestration SDK.

The "rapidly evolving ecosystem" claim is well-supported externally. LangGraph 1.0 reached GA in October 2025 but the overall AI agent ecosystem including MCP, guardrail frameworks, and vector DB integrations continues rapid evolution independent of LangGraph's stability commitment.

TE=4 (1.0–2.5 FTE annually) is consistent with the P2 OP FTE of 4.0–7.0 (which includes P3/P4 overlap; deduplicated net to the orchestration layer alone is lower). The three-phase file's Phase 3 FTE range of "4.0–7.0" for this row in the research FTE column aligns with the P2 source directly.

**Confidence:** Medium (the RD=3 vs RD=4 question hinges on how much of the multi-stack upgrade coordination burden falls to AL09 vs CP-07 Deploy Lifecycle; if deployment coordination is fully absorbed by CP-07, AL09 Phase 3 RD=3 may be defensible)

**Verdict:** ADJUST — consider RD upward from 3 to 4. The on-premises Phase 3 maintenance burden for the AI/agent stack is materially higher than "moderate" given the simultaneous versioning requirements across LangGraph, Temporal, Langfuse, LiteLLM, and guardrail components, each with independent release cycles, and the requirement to validate across multiple K8s versions per customer.

**Interview Question:** In practice, when you upgrade LangGraph or a MCP server version in a customer's on-premises deployment, how many other software components in the AI orchestration stack (Temporal, Langfuse, LiteLLM, guardrails) require coordinated testing or updates in the same maintenance window? Does this coordination work fall on the AL09 team or the CP-07 deployment team?

---

## AL10 — Testing Strategy, Contract Testing, and Environment Parity

### Ground Truth (from GT2)

[STATISTIC] "AL10: CN=2, MK8s=3, OP=4. FTE: CN 0.7–1.65, MK8s 2.0–4.0, OP 3.75–7.0. Tier-sensitive. Delta = 2."
— GT2_P2_ground_truth.md, AL10 section

[STATISTIC] "Replicated Compatibility Matrix: 65,981+ unique Kubernetes configuration combinations. Most ISVs test only a few combinations; problems are typically discovered in live customer accounts."
— GT2_P2_ground_truth.md, AL10 Key Operational Characteristics, citing F57: Build and Test Differences
URL: https://www.replicated.com/compatibility-matrix

[STATISTIC] "On-premises GPU test lab: approximately $500K capital cost (8x H100s). Cloud H100: $1.49–$3.90/hour (AWS cut 44% in June 2025)."
— GT2_P2_ground_truth.md, AL10 Key Operational Characteristics, citing F57

[STATISTIC] "Total build/test FTE: On-Premises = 3.75–7.0 FTE; Managed K8s = 2.0–4.0 FTE; Cloud-Native = 0.7–1.65 FTE."
— GT2_P2_ground_truth.md, AL10 Key Operational Characteristics, citing F57

[FACT] "QEMU cross-architecture builds for ARM64 targets inflate 4-minute builds to 40+ minutes."
— GT2_P2_ground_truth.md, AL10 Notable Caveats, citing P2 §3, AL10 Tier Analysis (On-Premises)

[FACT] "The 65,981+ Replicated compatibility matrix figure represents the theoretical test surface for AL10; empirical data on what fraction of these combinations ISVs actually test is unavailable."
— GT2_P2_ground_truth.md, AL10 Notable Caveats, citing P2 §7, Known Data Gaps

External research confirming the Replicated figure:

[STATISTIC] "65,981+ unique configuration combinations. Supports EKS, AKS, GKE, OpenShift, RKE2, kind, k3s, kURL distros and recent Kubernetes versions (1.28, 1.29, 1.30, 1.31, etc.)."
— Replicated Compatibility Matrix product page
URL: https://www.replicated.com/compatibility-matrix

[FACT] "With every new PR, teams test the latest patch version of all available Kubernetes minor versions, for every distribution that Compatibility Matrix currently supports. Testing pipelines complete in just a couple of hours due to concurrent distribution tests."
— Replicated blog, "How Replicated uses the Compatibility Matrix"
URL: https://www.replicated.com/blog/how-replicated-uses-the-compatibility-matrix-to-continuously-test

### Phase 1 — Initial Refactoring

**Current rating:** RD=3, TE=4

**Re-derived rating:** The three-phase file notes "[D] Build entirely new test infrastructure for on-prem environments. Integration test suites against self-hosted dependencies (PostgreSQL, Kafka, Milvus vs managed equivalents). Contract test framework must validate across K8s versions. Environment parity testing across N hardware profiles. Effort exceeds difficulty because the testing surface area is large even though each test is straightforward." This is flagged as a Divergence case (RD=3, TE=4 — effort exceeds difficulty by 1). The P2 source rates OP at 4/5 absolute difficulty. For Phase 1, building a test infrastructure from scratch against self-hosted dependencies is meaningfully harder than adapting cloud-native test infrastructure (hence RD=3, not RD=1 or RD=2). TE=4 (6–12 person-months one-time) is consistent with the P2 OP FTE of 3.75–7.0 annually — the one-time infrastructure build is larger than the annual steady-state because it includes designing the test framework, not just running it.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Customization

**Current rating:** RD=2, TE=2

**Re-derived rating:** "Validation testing against each customer's specific environment. Smoke tests, integration verification, performance baseline. Per-customer test runs, not per-customer test code." This scope clarification is important: Phase 2 AL10 represents running the existing test suite against the customer's specific K8s version, hardware, and network configuration — not writing new tests. The distinction between per-customer test runs vs. per-customer test code correctly limits the scope. RD=2 (low — same skill set, slightly more work) reflects that the testers use the same tools but must validate against each customer's environment. TE=2 (2–5 person-days) is consistent with running smoke tests and integration verification per customer.

**Confidence:** High

**Verdict:** ACCURATE

---

### Phase 3 — Ongoing Support

**Current rating:** RD=3, TE=4

**Re-derived rating:** The specific research question is whether the test matrix scales linearly with N customers. The three-phase file states "Test suite maintenance across N customer hardware profiles. Regression testing for each release against multiple K8s versions and hardware configurations. The testing tax is proportional to customer count and hardware diversity. High absolute effort because the test matrix multiplies." "Scales with N? Yes" is flagged.

The linear scaling claim analysis: Each new customer adds:
- One new hardware profile (CPU/storage/NIC combination) to the regression test matrix
- Potentially one new K8s version/distribution combination
- One additional environment against which each release must be smoke-tested

However, the 65,981+ Replicated figure represents the theoretical combinatorial surface, not the actual number of environments tested per release. In practice, ISVs use telemetry-driven canary testing against their actual installed customer configurations, not the full combinatorial matrix. Replicated's own documentation states that "canary tests are made against N environments where N = the sum of unique environments that represent an ISV's paying customers' full configuration as reported through telemetry."

This means the actual scaling is:
- **Linear in N customers** for per-release smoke testing (each customer = one environment to validate)
- **Sub-linear** for regression test suite maintenance (the test code itself is shared; it is the execution matrix that scales)

The claim of linear scaling is directionally correct but the rate of scaling depends on automation maturity. An ISV using Replicated CMX or equivalent tooling can parallelize validation across N customer environments, making the wall-clock time roughly constant while the computational/infrastructure cost scales linearly. The FTE scaling depends on how much of the per-customer validation is manual vs. automated.

[FACT] "ISV Testing Strategies for Reliability and Compatibility: Canary tests should be made when a release is promoted to the Beta channel and will be tested against N environments where N = the sum of unique environments that represent an ISV's paying customers' full configuration."
— Replicated blog, "ISV Testing Strategies for Reliability and Compatibility"
URL: https://www.replicated.com/blog/isv-testing-for-reliability-compatibility

RD=3 (moderate) and TE=4 (1.0–2.5 FTE annually, or in the Phase 3 table: high effort) is consistent with the P2 OP FTE of 3.75–7.0 for the full build/test function. The Divergence flag ([D]) is appropriate: the work is not technically sophisticated per test (RD=3, not RD=5), but the volume and coordination across N customers creates high total effort.

**Interview Question:** For a release deployed to 20 on-premises customers, how many distinct K8s versions or hardware profiles do you actually test against before general availability? Is this validation fully automated (e.g., via Replicated CMX or similar), and if so, what is the actual FTE cost of managing the automated test infrastructure vs. the manual per-customer validation work?

**Confidence:** Medium (the linear scaling claim is supported directionally but the scaling rate is dependent on automation tooling maturity, which is a known data gap in the source corpus — GT2 §7 explicitly identifies this)

**Verdict:** ACCURATE — directionally. The linear scaling designation is correct; the specific rate of scaling is a data gap. The [D] Divergence flag is correctly applied.

---

## Summary Scorecard — All 30 Ratings

| Subsegment | Phase | RD (File) | TE (File) | RD Verdict | TE Verdict | Confidence |
|---|:---:|:---:|:---:|---|---|---|
| AL06 Resilience | 1 | 2 | 2 | ACCURATE | ACCURATE | High |
| AL06 Resilience | 2 | 1 | 1 | ACCURATE | ACCURATE | High |
| AL06 Resilience | 3 | 2 | 2 | ACCURATE | ACCURATE | High |
| AL07 Multi-Tenant | 1 | 1 | 1 | ACCURATE | ACCURATE | High |
| AL07 Multi-Tenant | 2 | 1 | 1 | ACCURATE | ACCURATE | Medium |
| AL07 Multi-Tenant | 3 | 1 | 2 | ACCURATE | ACCURATE | High |
| AL08 Observability | 1 | 2 | 2 | ACCURATE | ACCURATE | High |
| AL08 Observability | 2 | 1 | 1 | ACCURATE | ACCURATE | High |
| AL08 Observability | 3 | 2 | 2 | ACCURATE | ACCURATE | High |
| AL09 AI Orchestration | 1 | 2 | 3 | ACCURATE | ACCURATE | High |
| AL09 AI Orchestration | 2 | 1 | 2 | ACCURATE | ACCURATE | High |
| AL09 AI Orchestration | 3 | **3** | 4 | **ADJUST (→4)** | ACCURATE | Medium |
| AL10 Testing | 1 | 3 | 4 | ACCURATE | ACCURATE | High |
| AL10 Testing | 2 | 2 | 2 | ACCURATE | ACCURATE | High |
| AL10 Testing | 3 | 3 | 4 | ACCURATE | ACCURATE | Medium |

**Rating totals:** 28 of 30 accurate. 1 adjustment recommended (AL09 Phase 3 RD). 1 medium-confidence accurate with scope caveat (AL07 Phase 2).

---

## Validation of the "Rapidly Evolving Ecosystem" Claim (AL09)

The three-phase file's note that AL09 involves a "rapidly evolving ecosystem" is well-supported by external evidence:

[STATISTIC] "LangGraph: approximately 12–15 patch/minor releases per month based on February 2026 release cadence. 47+ pages of release history."
— GitHub releases: https://github.com/langchain-ai/langgraph/releases (observed 2026-02-19)

[FACT] "LangGraph 1.0's policy commits to no breaking changes until 2.0; minor versions every 2–3 months. However, langgraph-prebuilt 1.0.2 introduced a breaking change in a required parameter within 30 days of the 1.0 GA announcement."
— GitHub issue #6363: https://github.com/langchain-ai/langgraph/issues/6363

[FACT] "MCP donated to Linux Foundation (AAIF) December 2025."
— GT2_P2_ground_truth.md, citing F07 and W01S
URL: https://blog.equinix.com/blog/2025/08/06/what-is-the-model-context-protocol-mcp-how-will-it-enable-the-future-of-agentic-ai/

The MCP protocol is still being standardized at the Linux Foundation level as of early 2026, making it genuinely more volatile than mature protocols like gRPC or REST (See GT2, AL01 section). The ecosystem volatility claim is accurate, but the Phase 3 RD=3 rating does not fully account for the on-premises coordination multiplier when upgrading a multi-stack AI orchestration deployment versus cloud-native.

---

## Validation of AL10 Linear Scaling Claim

The specific claim that "the testing tax is proportional to customer count" in AL10 Phase 3 is validated as directionally accurate with the following precision note:

[FACT] "Problems are typically discovered in live customer accounts" for ISVs that cannot test all 65,981+ Replicated combinations.
— GT2_P2_ground_truth.md, citing F57: Build and Test Differences

[FACT] "Canary tests are made against N environments where N = the sum of unique environments that represent an ISV's paying customers' full configuration."
— Replicated, "ISV Testing Strategies for Reliability and Compatibility"
URL: https://www.replicated.com/blog/isv-testing-for-reliability-compatibility

The implication: each additional on-premises customer adds one environment to the canary test matrix per release. This is linear growth in the number of validation runs. Whether it is linear in FTE depends on automation tooling. The three-phase file correctly marks "Scales with N? Yes" and correctly notes "the testing tax is proportional to customer count and hardware diversity." The claim is well-supported. The linear FTE scaling assumption is a modeling simplification — in practice, ISVs with mature Replicated CMX integration may see sub-linear FTE scaling as automation absorbs per-environment validation overhead.

---

## Key Findings

- **AL09 Phase 3 RD is under-rated.** The file rates RD=3 (moderate) for ongoing AI/ML orchestration maintenance, but the ground truth establishes AL09 as the hardest on-premises subsegment at 5/5 (See GT2; GT5 Rank 1), and the multi-stack upgrade coordination burden (LangGraph + Temporal + Langfuse + LiteLLM + guardrails + MCP) across N customer environments constitutes high difficulty (RD=4), not moderate. The "rapidly evolving ecosystem" rationale in the file itself supports the upward adjustment. TE=4 is accurate.

- **AL07 Phase 2 is accurate within its scope boundary.** The RD=1, TE=1 rating correctly reflects that application-layer multi-tenant isolation code does not change per customer due to hardware heterogeneity. The caveat is that ISVs implementing per-tenant SLOs at the application layer (rather than purely at the platform layer) could see hardware heterogeneity bleed into application-layer configuration, warranting RD=2. External research confirms that hardware heterogeneity creates performance isolation challenges, but these are platform-layer (P1) concerns, not application-layer (AL07) concerns.

- **AL10 linear scaling is directionally correct but automation-dependent.** The claim that the test matrix scales linearly with N customers is validated by Replicated's own canary testing model. The actual FTE scaling rate depends on automation maturity — ISVs with Replicated CMX or equivalent tooling may achieve sub-linear FTE scaling while maintaining linear validation coverage.

- **AL06 and AL08 are well-calibrated across all three phases.** Both subsegments have clear scope boundaries (application-level code only; infrastructure backend is P1 scope), and the ratings accurately reflect the tier delta without over-attributing infrastructure complexity to the application layer.

- **The systematic TE-RD divergence in P2 Phase 3 is confirmed.** The ground truth establishes that AL02 (product development), AL05 (EDA maintenance), AL09 (AI stack), and AL10 (test matrix) all exhibit TE > RD patterns. This review validates that for AL06–AL10, the divergence is accurately flagged for AL09 and AL10 and correctly absent for AL06, AL07, and AL08.

---

## Sources

| Source | Type | Path / URL |
|---|---|---|
| GT2_P2_ground_truth.md | Internal ground truth | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md` |
| GT5_cross_reference_ground_truth.md | Internal ground truth | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` |
| three_phase_on_prem_ratings.md | File under review | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| LangGraph 1.0 GA announcement | External | https://blog.langchain.com/langchain-langgraph-1dot0/ |
| LangGraph release page | External | https://github.com/langchain-ai/langgraph/releases |
| LangChain release policy | External | https://docs.langchain.com/oss/python/release-policy |
| LangGraph prebuilt breaking change (Issue #6363) | External | https://github.com/langchain-ai/langgraph/issues/6363 |
| Replicated Compatibility Matrix | External | https://www.replicated.com/compatibility-matrix |
| Replicated ISV Testing Strategies | External | https://www.replicated.com/blog/isv-testing-for-reliability-compatibility |
| Replicated CMX documentation | External | https://docs.replicated.com/vendor/testing-about |
| Kubernetes Cluster Autoscaler bare metal limitation | External | https://github.com/kubernetes/autoscaler/issues/1060 |
| vCluster multi-tenancy 2025 | External | https://www.vcluster.com/blog/multi-tenancy-in-2025-and-beyond |
| Atmosly Kubernetes multi-tenancy guide 2025 | External | https://atmosly.com/blog/kubernetes-multi-tenancy-complete-implementation-guide-2025 |
| Growin resilient backends Kubernetes 2025 | External | https://www.growin.com/blog/resilient-backends-kubernetes-2025/ |
| Langflow AI agent framework guide 2025 | External | https://www.langflow.org/blog/the-complete-guide-to-choosing-an-ai-agent-framework-in-2025 |
| Gartner agentic AI cancellation prediction | External | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 |
| OTel GenAI Semantic Conventions | External | https://opentelemetry.io/docs/specs/semconv/gen-ai/ |
| Langfuse self-hosting requirements | External | https://langfuse.com/self-hosting |
| MCP / Linux Foundation AAIF | External | https://blog.equinix.com/blog/2025/08/06/what-is-the-model-context-protocol-mcp-how-will-it-enable-the-future-of-agentic-ai/ |
