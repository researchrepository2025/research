# GT4: P4 AI Model Plane — Ground Truth Reference

**Agent Role:** Ground Truth Extraction (Agent 4 of 35)
**Source File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P4_ai_model_plane.md`
**Reference File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`
**Date Extracted:** 2026-02-19
**Status:** COMPLETE

---

## Executive Summary

[FACT]
The P4 AI Model Plane covers eight MECE subsegments spanning LLM inference serving, GPU infrastructure, model routing, inference monitoring, and model lifecycle management across three deployment tiers (Cloud-Native, Managed Kubernetes, On-Premises). Original ISV-owned FTE totals range from 0.30–0.80 FTE (Cloud-Native) to 2.20–4.65 FTE (Managed K8s Strategy b) to 8.10–15.30 FTE (On-Premises). Under the customer-provides-GPU-and-models scope split applied in `three_phase_on_prem_ratings.md`, subsegments S2 through S5 transfer to customer responsibility, reducing the ISV's P4 On-Premises FTE to approximately 0.45–2.30 FTE across S1, S6, S7, and S8 only.
— Source: `P4_ai_model_plane.md` §5 (FTE Summary Table), `three_phase_on_prem_ratings.md` §1 (Scope and Responsibility Split)

---

## S1: Managed API Integration

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **1** | Managed K8s: **1** | On-Premises: **2**"
— `P4_ai_model_plane.md` §3, S1 difficulty table

[FACT]
Rationale for On-Premises elevation to 2: "On-prem environments require outbound internet routing, proxy configuration, and air-gapped alternatives. Where network policy blocks public API egress, ISV must maintain a proxy or local API endpoint."
— `P4_ai_model_plane.md` §3, S1 rationale

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0.05–0.15 FTE | Managed K8s: 0.05–0.15 FTE | On-Premises: 0.1–0.3 FTE"
— `P4_ai_model_plane.md` §3, S1 FTE Estimates; §5 FTE Summary Table

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S1 remains **ISV scope** under the customer-provides-GPU model. The scope note in `three_phase_on_prem_ratings.md` §1 states: "ISV retains S1 (API Integration), S6 (Routing), S7 (Monitoring), and S8 (Lifecycle) in reduced form — calling customer-provided inference endpoints rather than managing infrastructure."
— `three_phase_on_prem_ratings.md` §1

### Technology Stack Options

[FACT]
"Amazon Bedrock provides access to approximately 100 serverless foundation models from 12+ providers; the ISV does not manage GPU provisioning, model serving infrastructure, or scaling."
— `P4_ai_model_plane.md` §3, S1, citing F10 (wave2/F10_aws_ai_ml.md)

[FACT]
"Azure OpenAI PTU (Provisioned Throughput Units) start at approximately $2,448/month and use a leaky-bucket utilization algorithm; quota reservation does NOT guarantee capacity — capacity must be verified separately."
— `P4_ai_model_plane.md` §3, S1, citing F18 (wave3/F18_azure_ai_ml.md)

[FACT]
"Vertex AI Gemini API pricing: Gemini 2.5 Pro at $1.25–$10/M tokens; 2.5 Flash at $0.30–$2.50/M; 50% batch discount applies."
— `P4_ai_model_plane.md` §3, S1, citing F26 (wave4/F26_gcp_ai_ml.md)

### Key Operational Characteristics

[FACT]
ISV owns: "API authentication and key rotation (Bedrock IAM, Azure API key/Entra, Vertex SA); Rate limit handling and retry logic (exponential backoff, jitter); Response schema parsing and error normalization across providers; Provider selection, fallback ordering, and SLA monitoring; Cost tracking and per-customer token attribution."
— `P4_ai_model_plane.md` §3, S1 ("What the ISV owns")

---

## S2: Self-Hosted Inference Engine Deployment

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **1** | Managed K8s: **3** | On-Premises: **5**"
— `P4_ai_model_plane.md` §3, S2 difficulty table; §4 Summary Difficulty Matrix

[FACT]
Gradient (On-Premises minus Cloud-Native): **+4**
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.75–1.5 FTE | On-Premises: 2.00–3.50 FTE"
— `P4_ai_model_plane.md` §3, S2 FTE Estimates; §5 FTE Summary Table

[STATISTIC]
"Total on-premises LLM inference staffing: 2.0–3.0 FTE active plus 0.45 FTE on-call."
— `P4_ai_model_plane.md` §3, S2 Evidence, citing F36 (wave5/F36_onprem_llm_inference.md)

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S2 **shifts to customer scope** under the customer-provides-GPU model. `three_phase_on_prem_ratings.md` §1 states: "Subsegments S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) shift to customer responsibility."
— `three_phase_on_prem_ratings.md` §1; confirmed in Phase 1 table (§4), Phase 2 table (§5), Phase 3 table (§6) with notation "Customer scope."

### Technology Stack Options

[FACT]
"Installing, configuring, tuning, and operating open-source LLM inference engines — primarily vLLM, but also TGI v3, NVIDIA Dynamo-Triton, TensorRT-LLM, and LMDeploy — on hardware the ISV controls."
— `P4_ai_model_plane.md` §3, S2 Definition

[STATISTIC]
"vLLM achieves P99 latency of 80ms and 793 tokens/second versus Ollama's 673ms P99 and 41 TPS; vLLM maintains 85–92% GPU utilization under high concurrency."
— `P4_ai_model_plane.md` §3, S2 Evidence, citing F36 and W05S

[STATISTIC]
"KServe v0.15 (June 2025): ships vLLM 0.8.5 backend with KEDA integration for LLM autoscaling."
— `P4_ai_model_plane.md` §3, S2 Evidence, citing F55b (wave7/F55b_k8s_gpu_ai.md)

### Key Operational Characteristics

[STATISTIC]
"Stripe migrated to vLLM and reduced inference costs 73%; handled 50M daily API calls on one-third of the previous GPU fleet."
— `P4_ai_model_plane.md` §3, S2 Evidence, citing F36

[FACT]
"A 70B FP16 model requires 168GB VRAM; AWQ INT4 quantization reduces this to approximately 35GB — fitting on a single A100 80GB or H100."
— `P4_ai_model_plane.md` §3, S2 Evidence, citing F36

[FACT]
"Multi-node LLM inference requires 200–400 Gbps InfiniBand or RoCE interconnect; NVMe at 7GB/s loads a 70B model in approximately 20 seconds; network-attached storage at 500MB/s requires approximately 5 minutes."
— `P4_ai_model_plane.md` §3, S2 Evidence, citing F36

---

## S3: GPU Hardware Infrastructure

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **1** | Managed K8s: **2** | On-Premises: **5**"
— `P4_ai_model_plane.md` §3, S3 difficulty table; §4 Summary Difficulty Matrix

[FACT]
Gradient (On-Premises minus Cloud-Native): **+4**
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.10–0.25 FTE | On-Premises: 2.50–5.00 FTE"
— `P4_ai_model_plane.md` §3, S3 FTE Estimates; §5 FTE Summary Table

[STATISTIC]
"Industry benchmark: approximately 10 specialized engineers per 1,000 GPUs; approximately 2 FTE per 200 GPUs. Total on-prem compute staffing: 2.5–5.0 FTE for a 200-GPU deployment."
— `P4_ai_model_plane.md` §3, S3 Evidence, citing F39 (wave6/F39_onprem_compute.md)

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S3 **shifts to customer scope** under the customer-provides-GPU model. Per `three_phase_on_prem_ratings.md` §1: "GPU + AI models: Customer — GPU procurement, driver management, inference engine operation, model weights, CUDA stack."
— `three_phase_on_prem_ratings.md` §1

### Technology Stack Options

[FACT]
"GPU hardware selection (H100, A100, L40S, H200) and procurement negotiation; Data center rack planning, power density upgrades, cooling system modifications; Physical server installation, NVLink/NVSwitch cabling, InfiniBand fabric."
— `P4_ai_model_plane.md` §3, S3 ("What the ISV owns (on-premises)")

[STATISTIC]
"Karpenter (EKS), NAP/Karpenter (AKS GA July 2025), and ComputeClasses (GKE Autopilot) provide scale-to-zero GPU economics on managed K8s."
— `P4_ai_model_plane.md` §3, S3 Evidence, citing F55b

### Key Operational Characteristics

[STATISTIC]
"NVIDIA DGX H100 (8-GPU): $373K–$450K retail; a 1,000-GPU cluster costs $30–$50M."
— `P4_ai_model_plane.md` §3, S3 Evidence, citing F39

[STATISTIC]
"H100 enterprise lead times: 9–12 months for standard orders (F36); improved to 5–6 month average in 2025 from 40+ weeks in 2023–2024 (F39)."
— `P4_ai_model_plane.md` §3, S3 Evidence, citing F36 and F39

[STATISTIC]
"Data center modifications for medium-scale AI GPU deployments (AI GPU racks require 30–80 kW per rack versus traditional 8–15 kW): cost $25K–$100K+ for medium-scale deployments."
— `P4_ai_model_plane.md` §3, S3 Evidence, citing F39

---

## S4: GPU Driver and CUDA Stack Management

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **1** | Managed K8s: **2** | On-Premises: **4**"
— `P4_ai_model_plane.md` §3, S4 difficulty table; §4 Summary Difficulty Matrix

[FACT]
Gradient (On-Premises minus Cloud-Native): **+3**
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.10–0.25 FTE | On-Premises: 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S4 FTE Estimates; §5 FTE Summary Table

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S4 **shifts to customer scope** under the customer-provides-GPU model. Per `three_phase_on_prem_ratings.md` §1: "S4 (CUDA/Drivers)" is listed as shifting to customer responsibility.
— `three_phase_on_prem_ratings.md` §1

### Technology Stack Options

[FACT]
"NVIDIA GPU Operator components: GPU Driver DaemonSet, Container Toolkit, Device Plugin, GPU Feature Discovery, DCGM Exporter, MIG Manager — all managed as Kubernetes DaemonSets."
— `P4_ai_model_plane.md` §3, S4 Evidence, citing F55b

[FACT]
"CNCF AI Conformance Program launched November 2025; AKS certified as AI-conformant December 2025 — standardizing GPU operator compatibility across managed K8s distributions."
— `P4_ai_model_plane.md` §3, S4 Evidence, citing F55b

### Key Operational Characteristics

[STATISTIC]
"AWQ on older GPU generations (pre-A100): up to 82% inference throughput slowdown without efficient 4-bit CUDA kernels — driver/CUDA version compatibility is a direct performance variable."
— `P4_ai_model_plane.md` §3, S4 Evidence, citing F36

[FACT]
"NVIDIA GPU failure rates: V100 approximately 1.5%/year; A100 0.8–1.2%/year; H100 estimated <0.8%/year."
— `P4_ai_model_plane.md` §3, S4 Evidence, citing F39

---

## S5: Multi-Tenant GPU Scheduling and Resource Allocation

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **1** | Managed K8s: **3** | On-Premises: **5**"
— `P4_ai_model_plane.md` §3, S5 difficulty table; §4 Summary Difficulty Matrix

[STATISTIC]
"GPU Scheduling/Sharing rated 5/5 on-premises, 3/5 managed K8s, 1/5 cloud-native."
— `P4_ai_model_plane.md` §3, S5 Evidence, citing W05S (synthesis/W05S_onprem_app_patterns.md)

[FACT]
Gradient (On-Premises minus Cloud-Native): **+4**
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.25–0.50 FTE | On-Premises: 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S5 FTE Estimates; §5 FTE Summary Table

[FACT]
"Total GPU scheduling staffing overlaps with S3/S4 (not double-counted): incremental 0.25–0.5 FTE."
— `P4_ai_model_plane.md` §3, S5 On-Premises rationale

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S5 **shifts to customer scope** under the customer-provides-GPU model. Per `three_phase_on_prem_ratings.md` §1: "S5 (GPU Scheduling)" is listed as shifting to customer responsibility.
— `three_phase_on_prem_ratings.md` §1

### Technology Stack Options

[FACT]
"NVIDIA MIG partitions A100/H100 into up to 7 isolated instances with hardware-level isolation. Example for on-prem LLM + embedding: 1x 3g.40gb (LLM inference 7B–13B) + 2x 2g.20gb (embedding models) on a single H100."
— `P4_ai_model_plane.md` §3, S5 Evidence, citing F36

[FACT]
"Dynamic Resource Allocation (DRA) graduated to GA in Kubernetes 1.34 (August 2025); GA features: Alternative Device Selection, Consumable Capacity, Resource Health Status."
— `P4_ai_model_plane.md` §3, S5 Evidence, citing F55b

[FACT]
"KAI Scheduler v0.10 (October 2025): NVIDIA open-sourced in April 2025; features Topology-Aware Scheduling, Hierarchical PodGroups, Time-based Fairshare, and gang scheduling for distributed inference."
— `P4_ai_model_plane.md` §3, S5 Evidence, citing F55b

### Key Operational Characteristics

[STATISTIC]
"GPUs sit 'reserved and underutilized 60–80% of the time' on managed Kubernetes without proper scheduling policies."
— `P4_ai_model_plane.md` §3, S5 Evidence, citing F55b

[STATISTIC]
"GPU contention between LLM inference and embedding workloads is 'the primary operational risk on-premises'; without explicit MIG partitioning on A100/H100 hardware, embedding latency degrades unpredictably under LLM load."
— `P4_ai_model_plane.md` §3, S5 Evidence, citing W05S

---

## S6: Model Routing and Load Balancing

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **2** | Managed K8s: **3** | On-Premises: **4**"
— `P4_ai_model_plane.md` §3, S6 difficulty table; §4 Summary Difficulty Matrix

[FACT]
Gradient (On-Premises minus Cloud-Native): **+2**
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0.10–0.25 FTE | Managed K8s: 0.20–0.50 FTE | On-Premises: 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S6 FTE Estimates; §5 FTE Summary Table

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S6 remains **ISV scope** under the customer-provides-GPU model, in "reduced form — calling customer-provided inference endpoints rather than managing engines."
— `three_phase_on_prem_ratings.md` §1

[FACT]
Phase 3 revised ISV FTE for S6 under scope split: "0.2–0.5 FTE."
— `three_phase_on_prem_ratings.md` §6, P4 Phase 3 table

### Technology Stack Options

[FACT]
"LiteLLM: unified gateway supporting 100+ LLM API formats; provides health checking, fallback routing, model version A/B testing, and per-customer token attribution."
— `P4_ai_model_plane.md` §3, S6 Evidence, citing F36

[FACT]
"vLLM Router (December 2025): Rust-based high-performance load balancer with Kubernetes-native integration and prefix-aware routing for KV-cache hit rate optimization."
— `P4_ai_model_plane.md` §3, S6 Evidence, citing F05 and F55b

### Key Operational Characteristics

[STATISTIC]
"RouteLLM (ICLR 2025, UC Berkeley/Anyscale/Canva): achieves 85% cost reduction while maintaining 95% GPT-4 performance through complexity-based routing."
— `P4_ai_model_plane.md` §3, S6 Evidence, citing F05 and W01S

[STATISTIC]
"CHWBL (Consistent Hash with Bounded Loads) load-balancing algorithm: 95% TTFT reduction versus Kubernetes default load balancer for LLM inference."
— `P4_ai_model_plane.md` §3, S6 Evidence, citing F05

---

## S7: Inference Monitoring and Observability

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **2** | Managed K8s: **4** | On-Premises: **5**"
— `P4_ai_model_plane.md` §3, S7 difficulty table; §4 Summary Difficulty Matrix

[STATISTIC]
"Domain 9 difficulty ratings from F76: Cloud-Native 2/5, Managed K8s 4/5, On-Premises 5/5."
— `P4_ai_model_plane.md` §3, S7 Evidence, citing F76 (wave11/F76_mece_failure_domain.md)

[FACT]
Gradient (On-Premises minus Cloud-Native): **+3**
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0.10–0.25 FTE | Managed K8s: 0.50–1.00 FTE + 0.25 on-call | On-Premises: 1.50–2.50 FTE + 0.5 on-call"
— `P4_ai_model_plane.md` §3, S7 FTE Estimates; §5 FTE Summary Table

[STATISTIC]
"Domain 9 FTE from F76: Cloud-Native 0.25 FTE; Managed K8s 0.5–1.0 FTE + 0.25 on-call; On-Premises 1.5–2.5 FTE + 0.5 on-call."
— `P4_ai_model_plane.md` §3, S7 Evidence, citing F76

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S7 remains **ISV scope** under the customer-provides-GPU model, in reduced form. Per `three_phase_on_prem_ratings.md` §4 (Phase 1 P4 table): "Application-layer TTFT/quality monitoring against customer's inference service. No GPU-level monitoring (DCGM) — that's customer scope."
— `three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S7 Notes

[FACT]
Phase 3 revised ISV FTE for S7 under scope split: "0.1–0.5 FTE."
— `three_phase_on_prem_ratings.md` §6, P4 Phase 3 table

### Technology Stack Options

[FACT]
"NVIDIA DCGM Exporter ships as a DaemonSet within GPU Operator and exposes GPU memory utilization, temperature, power draw, and error counters to Prometheus."
— `P4_ai_model_plane.md` §3, S7 Evidence, citing F55b

[FACT]
ISV owns: "DCGM Exporter configuration and Prometheus scrape integration; vLLM and KServe Prometheus metric endpoint configuration; Alert threshold definition for TTFT SLA, queue depth, and GPU memory pressure; Grafana dashboard creation for inference-specific panels."
— `P4_ai_model_plane.md` §3, S7 ("What the ISV owns")

### Key Operational Characteristics

[STATISTIC]
"An empirical study of 156 high-severity production AI inference incidents (April–June 2025) found approximately 60% were inference engine failures; ~40% of those were timeouts; ~29% resource exhaustion. Infrastructure-level GPU hardware failures accounted for approximately 20% of incidents. Approximately 74% were auto-detected via health probes; 28% required hotfixes with the highest time-to-mitigation cost."
— `P4_ai_model_plane.md` §3, S7 Evidence, citing F76 / arXiv 2511.07424

---

## S8: Model Lifecycle Management

### Difficulty Ratings (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: **2** | Managed K8s: **3** | On-Premises: **4**"
— `P4_ai_model_plane.md` §3, S8 difficulty table; §4 Summary Difficulty Matrix

[STATISTIC]
"Model Lifecycle rated 4/5 on-premises, 3/5 managed K8s, 1/5 cloud-native in W05S difficulty table."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing W05S

[STATISTIC]
"C11 (AI/ML Model Serving & Orchestration) in F73 MECE ISV Developer Responsibility framework: Cloud-Native 2/5, Managed K8s 3/5, On-Premises 5/5 — highest on-premises difficulty alongside C10 Security."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing F73 (wave11/F73_mece_isv_developer_responsibility.md)

[FACT]
Gradient (On-Premises minus Cloud-Native): **+2**
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix

### FTE Estimates (Original, Pre-Scope-Split)

[STATISTIC]
"Cloud-Native: 0.05–0.15 FTE | Managed K8s: 0.25–0.50 FTE | On-Premises: 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S8 FTE Estimates; §5 FTE Summary Table

### Scope Classification (Customer-Provides-GPU Model)

[FACT]
S8 remains **ISV scope** under the customer-provides-GPU model, in reduced form. Per `three_phase_on_prem_ratings.md` §4 (Phase 1 P4 table): "Customer manages model artifacts and versions. ISV tracks which models are available and selects version in API calls. Minimal refactoring."
— `three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S8 Notes

[FACT]
Phase 3 revised ISV FTE for S8 under scope split: "0.05–0.15 FTE."
— `three_phase_on_prem_ratings.md` §6, P4 Phase 3 table

### Technology Stack Options

[FACT]
"LiteLLM provides model version A/B testing, routing to different model versions, and fallback chains — applicable across all tiers."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing F36

[FACT]
"Vertex AI Model Garden provides 160+ foundation models including Gemma 3 and Llama available via vLLM pre-built Docker images — managed model registry for GCP ISVs."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing F26

### Key Operational Characteristics

[FACT]
"Azure OpenAI and Vertex AI handle model versioning, deprecation scheduling, and rollover on the provider's cadence — ISV cannot control the deprecation timeline."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing F18 and F26

[FACT]
"NVMe at 7GB/s loads a 70B model in approximately 20 seconds; network-attached storage at 500MB/s requires approximately 5 minutes — storage architecture directly determines model hot-swap latency."
— `P4_ai_model_plane.md` §3, S8 Evidence, citing F36

---

## Summary Tables

### Table 1: Original Difficulty Ratings — All Eight Subsegments (Pre-Scope-Split)

Source: `P4_ai_model_plane.md` §4 (Summary Difficulty Matrix)

| # | Subsegment | Cloud-Native | Managed K8s | On-Premises | Gradient (OP − CN) |
|---|---|:---:|:---:|:---:|:---:|
| S1 | Managed API Integration | 1 | 1 | 2 | +1 |
| S2 | Self-Hosted Inference Engine Deployment | 1 | 3 | 5 | +4 |
| S3 | GPU Hardware Infrastructure | 1 | 2 | 5 | +4 |
| S4 | GPU Driver and CUDA Stack Management | 1 | 2 | 4 | +3 |
| S5 | Multi-Tenant GPU Scheduling and Resource Allocation | 1 | 3 | 5 | +4 |
| S6 | Model Routing and Load Balancing | 2 | 3 | 4 | +2 |
| S7 | Inference Monitoring and Observability | 2 | 4 | 5 | +3 |
| S8 | Model Lifecycle Management | 2 | 3 | 4 | +2 |
| | **Plane Average** | **1.4** | **2.6** | **4.3** | **+2.9** |

Scale: 1 = Trivial | 2 = Low | 3 = Moderate | 4 = High | 5 = Very High

---

### Table 2: Original FTE Ranges — All Eight Subsegments (Pre-Scope-Split)

Source: `P4_ai_model_plane.md` §5 (FTE Summary by Subsegment and Tier)

| # | Subsegment | Cloud-Native FTE | Managed K8s FTE | On-Premises FTE |
|---|---|---|---|---|
| S1 | Managed API Integration | 0.05–0.15 | 0.05–0.15 | 0.10–0.30 |
| S2 | Self-Hosted Inference Engine | 0 | 0.75–1.50 | 2.00–3.50 |
| S3 | GPU Hardware Infrastructure | 0 | 0.10–0.25 | 2.50–5.00 |
| S4 | GPU Driver and CUDA Stack | 0 | 0.10–0.25 | 0.50–1.00 |
| S5 | GPU Scheduling and Allocation | 0 | 0.25–0.50 | 0.50–1.00 |
| S6 | Model Routing and Load Balancing | 0.10–0.25 | 0.20–0.50 | 0.50–1.00 |
| S7 | Inference Monitoring | 0.10–0.25 | 0.50–1.00 (+0.25 on-call) | 1.50–2.50 (+0.5 on-call) |
| S8 | Model Lifecycle Management | 0.05–0.15 | 0.25–0.50 | 0.50–1.00 |
| | **Plane Total** | **0.30–0.80** | **2.20–4.65** | **8.10–15.30** |

Note: On-premises S7 FTE includes 0.5 FTE on-call. Managed K8s S7 FTE includes 0.25 FTE on-call. Managed K8s total assumes Strategy (b) — self-hosting vLLM on GPU node pools. Strategy (a) — consuming managed APIs from within K8s — reduces Managed K8s total to approximately 0.30–0.80 FTE. Source note verbatim: "S3 and S4/S5 share infrastructure staff; no double-counting — S3 covers physical hardware, S4 covers driver software, S5 covers scheduling policy."
— `P4_ai_model_plane.md` §5, footnote

---

### Table 3: Scope Assignment Under Customer-Provides-GPU Model

Source: `three_phase_on_prem_ratings.md` §1 (Scope and Responsibility Split)

| # | Subsegment | Scope Owner | Basis |
|---|---|---|---|
| S1 | Managed API Integration | **ISV** | ISV calls customer-provided inference endpoints |
| S2 | Self-Hosted Inference Engine Deployment | **Customer** | Customer operates vLLM/TGI on their GPUs |
| S3 | GPU Hardware Infrastructure | **Customer** | Customer owns all GPU hardware |
| S4 | GPU Driver and CUDA Stack Management | **Customer** | Customer manages driver stack |
| S5 | Multi-Tenant GPU Scheduling and Resource Allocation | **Customer** | Customer manages GPU allocation |
| S6 | Model Routing and Load Balancing | **ISV** (reduced) | Routing to customer endpoints, not managing engines |
| S7 | Inference Monitoring and Observability | **ISV** (reduced) | Application-layer TTFT only; no GPU-level (DCGM) monitoring |
| S8 | Model Lifecycle Management | **ISV** (reduced) | ISV tracks available models; customer manages artifacts |

---

### Table 4: Original ISV Total vs. Reduced ISV Total After Scope Split (On-Premises)

Source: `P4_ai_model_plane.md` §5; `three_phase_on_prem_ratings.md` §1 and Phase 3 table (§6)

| Metric | Original ISV Total (all 8 subsegments) | Reduced ISV Total (S1, S6, S7, S8 only) |
|---|---|---|
| On-Premises FTE (research-based annual) | 8.10–15.30 FTE | ~0.45–2.30 FTE |
| On-Premises Difficulty Average | 4.3 / 5 | ~2.25 / 5 (S1=2, S6=4, S7=5, S8=4) |
| Subsegments Retained by ISV | 8 of 8 | 4 of 8 |
| Phase 3 FTE (three_phase file) | N/A (pre-split) | ~0.5–1.5 FTE |

[FACT]
Phase 3 reduced ISV FTE stated directly in `three_phase_on_prem_ratings.md` §6: "P4 Phase 3 Totals (ISV scope): ~0.5–1.5 FTE"
— `three_phase_on_prem_ratings.md` §6, Phase 3 Summary table

[FACT]
The reduced ISV On-Premises FTE range of ~0.45–2.30 FTE is derived by summing post-scope-split FTE from the Phase 3 table: S1 (0.1–0.3) + S6 (0.2–0.5) + S7 (0.1–0.5) + S8 (0.05–0.15) + S2/S3/S4/S5 (0).
— `three_phase_on_prem_ratings.md` §6, P4 Phase 3 individual subsegment rows

[FACT]
`three_phase_on_prem_ratings.md` §8 (Grand Summary, Key Finding 4) states: "P4 (AI Model Plane) is nearly eliminated under the customer-provides-GPU-and-models scope. All-phase average of RD 1.3 / TE 1.7. The ISV's AI-related effort is in P2 (agent orchestration) and P3 (embedding/RAG pipelines), not P4."
— `three_phase_on_prem_ratings.md` §8

---

### Table 5: Technology Stack Options by Subsegment

Source: `P4_ai_model_plane.md` §3 (per-subsegment definitions and evidence sections)

| # | Subsegment | Primary Technology Options |
|---|---|---|
| S1 | Managed API Integration | Amazon Bedrock, Azure OpenAI / Foundry Models, Vertex AI Gemini API, LiteLLM (unified gateway) |
| S2 | Self-Hosted Inference Engine | vLLM (primary), TGI v3, NVIDIA Dynamo-Triton, TensorRT-LLM, LMDeploy; KServe v0.15 (K8s orchestration) |
| S3 | GPU Hardware Infrastructure | H100, A100, L40S, H200 (NVIDIA); Karpenter / NAP / ComputeClasses (K8s node provisioning) |
| S4 | GPU Driver and CUDA Stack | NVIDIA GPU Operator (DaemonSet stack); CNCF AI Conformance-certified distributions (AKS Dec 2025) |
| S5 | Multi-Tenant GPU Scheduling | NVIDIA MIG (A100/H100), GPU time-slicing, DRA (K8s 1.34 GA Aug 2025), KAI Scheduler v0.10 (Oct 2025) |
| S6 | Model Routing and Load Balancing | LiteLLM, vLLM Router (Rust, Dec 2025), RouteLLM (CHWBL, complexity routing), Azure ML Managed Online Endpoints |
| S7 | Inference Monitoring | DCGM Exporter (GPU), Prometheus + Grafana, vLLM / KServe metric endpoints, NVIDIA GROVE (cloud K8s) |
| S8 | Model Lifecycle Management | LiteLLM (A/B testing), Hugging Face Hub, NVIDIA NGC, Vertex AI Model Garden (160+ models), NVMe local cache |

---

## Sources

| Source File | Subsegments Covered | Key Data Contributed |
|---|---|---|
| `P4_ai_model_plane.md` §3 | S1–S8 | Per-subsegment difficulty ratings, FTE estimates, ISV ownership definitions, evidence citations |
| `P4_ai_model_plane.md` §4 | S1–S8 | Summary Difficulty Matrix (all tiers, all gradients, plane averages) |
| `P4_ai_model_plane.md` §5 | S1–S8 | FTE Summary Table (all tiers, plane totals, on-call breakout, Strategy a/b note) |
| `three_phase_on_prem_ratings.md` §1 | S2–S5 (customer scope) | Scope and Responsibility Split definition |
| `three_phase_on_prem_ratings.md` §4 | S1, S6, S7, S8 | Phase 1 ISV post-split difficulty and effort ratings |
| `three_phase_on_prem_ratings.md` §5 | S1, S6, S7, S8 | Phase 2 ISV post-split difficulty and effort ratings |
| `three_phase_on_prem_ratings.md` §6 | S1, S6, S7, S8 | Phase 3 ISV post-split FTE (0.5–1.5 FTE total) |
| `three_phase_on_prem_ratings.md` §8 | P4 overall | Grand Summary Key Finding 4: P4 "nearly eliminated" under scope split |
| F05: wave1/F05_llm_model_serving.md | S2, S6 | RouteLLM 85% cost reduction; CHWBL 95% TTFT reduction; vLLM Production Stack 3–10x |
| F10: wave2/F10_aws_ai_ml.md | S1 | Bedrock ~100 models; 0.0–0.1 FTE inference ops |
| F18: wave3/F18_azure_ai_ml.md | S1, S8 | Azure OpenAI PTU $2,448/month; 0.1–0.25 FTE ongoing |
| F26: wave4/F26_gcp_ai_ml.md | S1, S8 | Vertex AI pricing; Model Garden 160+ models |
| F36: wave5/F36_onprem_llm_inference.md | S2, S3, S5, S6, S8 | vLLM benchmarks; Stripe 73% cost reduction; 2.0–3.0 FTE inference ops; H100 lead times |
| F39: wave6/F39_onprem_compute.md | S3, S4 | DGX H100 $373K–$450K; GPU failure rates; 2.5–5.0 FTE per 200 GPUs |
| F55b: wave7/F55b_k8s_gpu_ai.md | S2, S4, S5, S7 | GPU Operator; DRA GA K8s 1.34; KAI Scheduler v0.10; KServe v0.15; CNCF AI Conformance |
| F73: wave11/F73_mece_isv_developer_responsibility.md | S8 | C11 AI/ML Model Serving difficulty ratings |
| F76: wave11/F76_mece_failure_domain.md | S7 | 156 production incidents; Domain 9 difficulty 2/4/5; FTE 0.25/0.5–1.0/1.5–2.5 |
| W01S: synthesis/W01S_foundation_patterns.md | S6 | 85% cost reduction routing evidence; routing as default production config |
| W05S: synthesis/W05S_onprem_app_patterns.md | S2, S5, S8 | GPU contention as primary on-prem risk; Model Lifecycle 4/5 on-prem |
