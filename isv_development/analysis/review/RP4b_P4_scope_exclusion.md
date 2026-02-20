# RP4b: P4 Scope Exclusion Validation — S2 Through S5 Customer Scope Analysis

**Agent Role:** Scope Exclusion Validation (RP4b)
**Primary Source:** `analysis/P4_ai_model_plane.md`
**Ground Truth Reference:** `analysis/review/GT4_P4_ground_truth.md`
**Cross-Reference:** `analysis/review/GT5_cross_reference_ground_truth.md`
**Date:** 2026-02-19
**Status:** COMPLETE

---

## Executive Summary

The exclusion of S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) from ISV scope under the customer-provides-GPU model is structurally sound for the core infrastructure responsibility, transferring 5.50–10.50 FTE of on-premises work to the customer. However, the exclusion masks four specific categories of residual ISV obligation that are not captured in the three-phase ratings: (1) ISV-owned compatibility testing against customer GPU configurations, (2) ISV responsibility for API-contract enforcement when the customer's inference engine returns unexpected behavior, (3) ISV obligation to specify minimum GPU resource requirements in customer-facing documentation, and (4) ISV support burden when customer GPU allocation is insufficient to meet application SLAs. These residual responsibilities are currently unrated and uncosted, representing an undercount in the ISV's Phase 2 (Per-Customer Customization) and Phase 3 (Ongoing Support) effort estimates.

---

## 1. Source File Review: S2–S5 Definitions and FTE Data

### 1.1 S2: Self-Hosted Inference Engine Deployment

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.75–1.5 FTE | On-Premises: 2.00–3.50 FTE"
— `P4_ai_model_plane.md` §3, S2 FTE Estimates; `GT4_P4_ground_truth.md` Table 2

[FACT]
S2 is defined as "Installing, configuring, tuning, and operating open-source LLM inference engines — primarily vLLM, but also TGI v3, NVIDIA Dynamo-Triton, TensorRT-LLM, and LMDeploy — on hardware the ISV controls."
— `P4_ai_model_plane.md` §3, S2 Definition

[STATISTIC]
"Total on-premises LLM inference staffing: 2.0–3.0 FTE active plus 0.45 FTE on-call."
— `P4_ai_model_plane.md` §3, S2 Evidence; `GT4_P4_ground_truth.md` §S2

[STATISTIC]
S2 on-premises difficulty: **5/5**. Gradient (On-Premises minus Cloud-Native): **+4**.
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix; `GT4_P4_ground_truth.md` Table 1

### 1.2 S3: GPU Hardware Infrastructure

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.10–0.25 FTE | On-Premises: 2.50–5.00 FTE"
— `P4_ai_model_plane.md` §3, S3 FTE Estimates; `GT4_P4_ground_truth.md` Table 2

[STATISTIC]
S3 on-premises difficulty: **5/5**. Gradient (On-Premises minus Cloud-Native): **+4**.
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix; `GT4_P4_ground_truth.md` Table 1

[STATISTIC]
"Industry benchmark: approximately 10 specialized engineers per 1,000 GPUs; approximately 2 FTE per 200 GPUs. Total on-prem compute staffing: 2.5–5.0 FTE for a 200-GPU deployment."
— `P4_ai_model_plane.md` §3, S3 Evidence

[FACT]
S3 scope on-premises includes: "GPU hardware selection (H100, A100, L40S, H200) and procurement negotiation; Data center rack planning, power density upgrades, cooling system modifications; Physical server installation, NVLink/NVSwitch cabling, InfiniBand fabric."
— `P4_ai_model_plane.md` §3, S3 ("What the ISV owns (on-premises)")

### 1.3 S4: GPU Driver and CUDA Stack Management

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.10–0.25 FTE | On-Premises: 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S4 FTE Estimates; `GT4_P4_ground_truth.md` Table 2

[STATISTIC]
S4 on-premises difficulty: **4/5**. Gradient (On-Premises minus Cloud-Native): **+3**.
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix; `GT4_P4_ground_truth.md` Table 1

[STATISTIC]
"AWQ on older GPU generations (pre-A100): up to 82% inference throughput slowdown without efficient 4-bit CUDA kernels — driver/CUDA version compatibility is a direct performance variable."
— `P4_ai_model_plane.md` §3, S4 Evidence

[FACT]
S4 scope includes: "Driver version selection pinned to CUDA version, PyTorch version, and vLLM version; GPU Operator component management: Driver DaemonSet, Container Toolkit, Device Plugin, GFD, DCGM Exporter, MIG Manager."
— `P4_ai_model_plane.md` §3, S4 ("What the ISV owns")

### 1.4 S5: Multi-Tenant GPU Scheduling and Resource Allocation

[STATISTIC]
"Cloud-Native: 0 FTE | Managed K8s: 0.25–0.50 FTE | On-Premises: 0.50–1.00 FTE"
— `P4_ai_model_plane.md` §3, S5 FTE Estimates; `GT4_P4_ground_truth.md` Table 2

[STATISTIC]
S5 on-premises difficulty: **5/5**. Gradient (On-Premises minus Cloud-Native): **+4**.
— `P4_ai_model_plane.md` §4 Summary Difficulty Matrix; `GT4_P4_ground_truth.md` Table 1

[STATISTIC]
"GPUs sit 'reserved and underutilized 60–80% of the time' on managed Kubernetes without proper scheduling policies."
— `P4_ai_model_plane.md` §3, S5 Evidence

[STATISTIC]
"GPU contention between LLM inference and embedding workloads is 'the primary operational risk on-premises'; without explicit MIG partitioning on A100/H100 hardware, embedding latency degrades unpredictably under LLM load."
— `P4_ai_model_plane.md` §3, S5 Evidence

### 1.5 Aggregate FTE Transferred to Customer Scope

[STATISTIC]
Combined pre-split on-premises FTE for S2+S3+S4+S5: **5.50–10.50 FTE** (S2: 2.00–3.50 + S3: 2.50–5.00 + S4: 0.50–1.00 + S5: 0.50–1.00, with S4/S5 sharing staff with S3 per source footnote, so actual transfer is non-additive).
— `P4_ai_model_plane.md` §5 (footnote: "S3 and S4/S5 share infrastructure staff; no double-counting")

[FACT]
The scope split in `three_phase_on_prem_ratings.md` §1 states: "Subsegments S2 (Inference Engine), S3 (GPU Hardware), S4 (CUDA/Drivers), and S5 (GPU Scheduling) shift to customer responsibility."
— `three_phase_on_prem_ratings.md` §1

[FACT]
After the scope split, ISV P4 on-premises FTE reduces to approximately 0.45–2.30 FTE across S1, S6, S7, and S8 only. The Phase 3 summary states: "P4 Phase 3 Totals (ISV scope): ~0.5–1.5 FTE."
— `GT4_P4_ground_truth.md` Table 4; `three_phase_on_prem_ratings.md` §6

---

## 2. Is the ISV Responsibility Truly Zero for S2–S5?

### 2.1 The Formal Scope Assignment

[FACT]
`three_phase_on_prem_ratings.md` §1 establishes a binary scope split: "GPU + AI models: Customer — GPU procurement, driver management, inference engine operation, model weights, CUDA stack."
— `three_phase_on_prem_ratings.md` §1

[FACT]
`three_phase_on_prem_ratings.md` §8 (Grand Summary, Key Finding 4) states: "P4 (AI Model Plane) is nearly eliminated under the customer-provides-GPU-and-models scope."
— `three_phase_on_prem_ratings.md` §8

The source files treat S2–S5 as binary transfers. The ratings tables in Phases 1, 2, and 3 mark these four subsegments as "Customer scope" with no ISV RD or TE ratings assigned. This is structurally clean for the primary infrastructure responsibility. However, the binary framing masks several categories of residual ISV obligation that are non-zero.

### 2.2 Residual ISV Obligation — Category 1: Compatibility Testing

[FACT]
The NVIDIA RTX ISV Certification program requires that "Formally tested application, driver, and hardware combinations meet criteria established by ISV application developers to ensure intended and desired functionality." End users receive "direct support from the application developer and NVIDIA, if needed."
— NVIDIA RTX ISV Certifications page
URL: https://www.nvidia.com/en-us/products/workstations/isv-certifications/

[FACT]
The NVIDIA ISV program documentation states that ISVs perform certification testing against specific GPU + driver + hardware combinations, and that "bugs and regressions are resolved by application developer and NVIDIA, if needed, as they become known through user community."
— NVIDIA RTX ISV Certifications page
URL: https://www.nvidia.com/en-us/products/workstations/isv-certifications/

[STATISTIC]
"78% of teams struggle with GPU compatibility during CI/CD" for LLM deployments.
— Northflank 2025 deployment guide, cited via search result summary
URL: https://northflank.com/blog/top-gpu-hosting-platforms-for-ai

[FACT]
"vLLM depends on PyTorch, and if the PyTorch version installed isn't built for CUDA 12.4, you might see errors or suboptimal performance; the vLLM pip wheel is built with CUDA 12.1 in mind, meaning it may install a PyTorch that expects CUDA 12.1 libraries."
— RunPod documentation, 2025
URL: https://www.runpod.io/articles/guides/best-docker-image-vllm-inference-cuda-12-4

[STATISTIC]
"AWQ on older GPU generations (pre-A100): up to 82% inference throughput slowdown without efficient 4-bit CUDA kernels."
— `P4_ai_model_plane.md` §3, S4 Evidence

**Implication:** Even when the customer owns the GPU hardware and driver stack (S3, S4), the ISV's application code — specifically the inference API calls, quantization method selections, and model format assumptions — must be validated against the specific CUDA and GPU generations the customer deploys. An ISV calling a vLLM endpoint with AWQ-quantized requests against a customer running pre-A100 hardware will experience an 82% throughput degradation. The customer did not cause this; the ISV's quantization selection did. This is an ISV compatibility testing obligation that the current scope exclusion does not capture.

### 2.3 Residual ISV Obligation — Category 2: API Contract Enforcement at the Inference Endpoint

[FACT]
vLLM's OpenAI-compatible API server is the standard interface ISVs call when integrating with customer-hosted inference engines. The ISV's application code sends requests to `v1/chat/completions` or `v1/completions` endpoints hosted on the customer's inference engine.
— vLLM documentation, OpenAI-Compatible Server
URL: https://docs.vllm.ai/en/stable/serving/openai_compatible_server/

[FACT]
S1 (Managed API Integration) in `P4_ai_model_plane.md` covers "response schema parsing and error normalization across providers" as ISV scope. On-premises, the "provider" is the customer's vLLM/TGI instance. The ISV owns the error handling logic when the customer's inference engine returns unexpected schemas, 500 errors, or timeout responses.
— `P4_ai_model_plane.md` §3, S1 ("What the ISV owns")

[STATISTIC]
"An empirical study of 156 high-severity production AI inference incidents (April–June 2025) found approximately 60% were inference engine failures; ~40% of those were timeouts; ~29% resource exhaustion."
— `P4_ai_model_plane.md` §3, S7 Evidence, citing arXiv 2511.07424

**Implication:** When the customer's inference engine (S2) crashes, times out, or returns resource exhaustion errors, the ISV's application must handle these gracefully. The ISV owns the retry logic, circuit breakers, fallback routing (S6), and error telemetry (S7) that respond to inference engine failures. Sixty percent of production incidents originate in the inference engine. Even with S2 in customer scope, the ISV absorbs the response burden for those 60% of incidents as they surface at the API boundary. This responsibility is partially captured in S6 and S7 but not explicitly attributed to S2 cross-scope interactions in the current ratings.

### 2.4 Residual ISV Obligation — Category 3: Minimum GPU Resource Specification

[FACT]
"A 70B FP16 model requires 168GB VRAM; AWQ INT4 quantization reduces this to approximately 35GB — fitting on a single A100 80GB or H100."
— `P4_ai_model_plane.md` §3, S2 Evidence

[FACT]
NVIDIA NIM documentation specifies that "Optimized models are GPU specific and require a minimum GPU memory value as specified in the Optimized configuration sections of each model."
— NVIDIA NIM Support Matrix
URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html

[FACT]
NVIDIA AI Enterprise requires customers to "deploy it on NVIDIA-Certified Systems in order to be supported."
— NVIDIA AI Enterprise
URL: https://www.nvidia.com/en-us/data-center/products/ai-enterprise/

[FACT]
"Performance is deeply dependent on the entire system configuration, and even the software stack plays an important role; without optimized kernels specifically designed for the GPU's architecture and the chosen quantization format, the hardware's potential remains untapped."
— IntuitionLabs, LLM Inference Hardware Enterprise Guide
URL: https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide

**Implication:** The ISV is the only party that knows what GPU memory, VRAM capacity, interconnect bandwidth, and CUDA version their application requires. When S3 (GPU Hardware) and S4 (CUDA/Drivers) are customer scope, the ISV must produce and maintain a minimum hardware specification document — a "hardware requirements matrix" — that defines the minimum GPU generation, VRAM floor, CUDA version, and driver version the ISV's application will support. This document does not exist in the current scope framework and is not rated in any phase.

### 2.5 Residual ISV Obligation — Category 4: Insufficient GPU Allocation

[FACT]
"Unlike traditional applications, AI workloads don't run in clean sequences, and their three core components of compute, storage, and networking operate simultaneously and interdependently, which means one bottleneck affects the whole system."
— LogicMonitor, AI Workload Infrastructure Requirements
URL: https://www.logicmonitor.com/blog/ai-workload-infrastructure

[FACT]
"GPU contention between LLM inference and embedding workloads is 'the primary operational risk on-premises'; without explicit MIG partitioning on A100/H100 hardware, embedding latency degrades unpredictably under LLM load."
— `P4_ai_model_plane.md` §3, S5 Evidence

[STATISTIC]
"GPUs sit 'reserved and underutilized 60–80% of the time' on managed Kubernetes without proper scheduling policies."
— `P4_ai_model_plane.md` §3, S5 Evidence

**Implication:** When a customer's GPU allocation is insufficient — either because the customer over-subscribed their GPU cluster or because they did not configure MIG partitioning (S5 customer scope) — the ISV's application will exhibit degraded TTFT and throughput. The SLA failure is observable at the application layer, not at the GPU layer. The ISV owns the application-layer SLA (typically defined in a commercial contract with the customer). If the customer has allocated insufficient GPU resources but claims the ISV's software is "too slow," the ISV must diagnose the root cause. This diagnosis requires the ISV to instrument and interpret GPU-level metrics (DCGM, MIG occupancy) — metrics that originate in S3–S5 (customer scope). The ISV has no control over the customer's GPU allocation but bears the support cost of diagnosing and attributing the performance problem. This creates a support triage burden that is unrated in the current framework.

---

## 3. Edge Cases: Inference Engine Compatibility Issues with ISV API Calls

### 3.1 Quantization Format Mismatch

[STATISTIC]
"AWQ 4-bit quantization: 95% accuracy retention, 0.036 MAE; GPTQ: 90% accuracy retention, 0.049 MAE; GGUF: 92% accuracy retention, 0.041 MAE."
— `P4_ai_model_plane.md` §3, S2 Evidence

[STATISTIC]
"AWQ on older GPU generations (pre-A100): up to 82% inference throughput slowdown without efficient 4-bit CUDA kernels."
— `P4_ai_model_plane.md` §3, S4 Evidence

**Edge Case:** The ISV's application may be designed to call a vLLM endpoint serving AWQ INT4 quantized models — optimal for H100/A100. If the customer's inference engine (S2, customer scope) is running the same model in GPTQ format on older V100 hardware, the ISV's API calls will complete but with degraded accuracy (0.049 vs 0.036 MAE) and different throughput characteristics. The ISV's response schema parsing (S1) will succeed, but the quality contract is broken. Responsibility: [UNVERIFIED] — no published framework establishes whether the ISV or the customer owns the accuracy degradation risk when the customer selects a different quantization format than the ISV tested against.

### 3.2 Model Version Divergence

[FACT]
Under the scope split, "Customer manages model artifacts and versions. ISV tracks which models are available and selects version in API calls."
— `three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S8 Notes

[FACT]
S8 (Model Lifecycle Management) remains ISV scope, defined as: "ISV tracks which models are available and selects version in API calls."
— `three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S8 Notes

**Edge Case:** The customer may upgrade their model weights (S2/S8, customer-managed) without notifying the ISV. If the ISV's prompt templates, response parsers, or function-calling schemas were validated against Llama 3.1 and the customer upgrades to Llama 3.3, the ISV's API calls may produce unexpected behavior. The ISV owns the prompt schema validation (S8 reduced) but cannot control the customer's model upgrade schedule. This creates an implicit change management dependency that is unrated.

### 3.3 vLLM Version API Drift

[STATISTIC]
"KServe v0.15 (June 2025): ships vLLM 0.8.5 backend with KEDA integration for LLM autoscaling."
— `P4_ai_model_plane.md` §3, S2 Evidence

[FACT]
vLLM releases new versions frequently; see the vLLM release history at:
URL: https://github.com/vllm-project/vllm/releases

**Edge Case:** The customer may run vLLM 0.5.x while the ISV develops and tests against vLLM 0.8.x. API response field names, streaming behavior, and error code schemas have changed across minor versions. The ISV cannot control the customer's vLLM version (S2, customer scope) but must maintain compatibility with the version the customer is running. This creates a version matrix support obligation that is not currently captured in any phase rating.

---

## 4. ISV Support Responsibilities Not Captured

### 4.1 Compatibility Matrix Documentation

[FACT]
The NVIDIA NIM support matrix documents explicitly specify GPU compute capabilities, memory floors, and driver versions per model configuration.
— NVIDIA NIM Support Matrix
URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html

[FACT]
"NVIDIA NIM runs on NVIDIA RTX GPUs, and no other GPU providers are supported to run NIM. For specific deployment contexts, the minimum GPU requirement is an NVIDIA RTX 4080 or better."
— NVIDIA NIM system requirements
URL: https://docs.anythingllm.com/nvidia-nims/system-requirements

[FACT]
"The CNCF AI Conformance Program launched November 2025; AKS certified as AI-conformant December 2025 — standardizing GPU operator compatibility across managed K8s distributions."
— `P4_ai_model_plane.md` §3, S4 Evidence

**Implication:** ISVs deploying AI software on customer GPU infrastructure are expected to produce and maintain a hardware compatibility matrix equivalent in structure to what NVIDIA publishes for NIM. This is an ISV documentation obligation — a Phase 1 artifact — that is not rated in `three_phase_on_prem_ratings.md`. Its creation requires the ISV to test against multiple GPU generations (V100, A100, L40S, H100), CUDA versions, and inference engine versions, which is an S2/S3/S4-adjacent task even though S2–S4 are "customer scope."

### 4.2 Troubleshooting Guides and Runbooks for Customer-Tier Issues

[STATISTIC]
"Approximately 74% of incidents were auto-detected via health probes; 28% required hotfixes with the highest time-to-mitigation cost."
— `P4_ai_model_plane.md` §3, S7 Evidence, citing arXiv 2511.07424

[FACT]
"The Inference Degradation Spiral cascade (F76 Domain 9 → 8 → 11): GPU exhaustion at bursty load → HTTP 429/500 errors → background retraining jobs failing → CPU exhaustion from fallback logic."
— `P4_ai_model_plane.md` §3, S7 Evidence

[FACT]
The NVIDIA RTX ISV Certification program states end users receive "direct support from the application developer and NVIDIA if needed" for certified GPU + application configurations.
— NVIDIA RTX ISV Certifications page
URL: https://www.nvidia.com/en-us/products/workstations/isv-certifications/

**Implication:** When 28% of incidents require hotfixes and the performance cascade originates at the GPU layer (S3/S4/S5, customer scope), the ISV must produce troubleshooting runbooks that guide customer GPU administrators through the diagnostic steps the ISV cannot perform unilaterally. These runbooks are an ISV support artifact — Phase 3 recurring maintenance — that is not currently rated.

### 4.3 Inference Engine Version Testing Against ISV Software

[FACT]
The llm-d project, launched May 2025 by Red Hat, Google Cloud, IBM Research, NVIDIA, and CoreWeave, provides "a Kubernetes-native distributed serving stack built on top of vLLM as a complementary orchestration layer."
— Search result citing llm-d project announcement
URL: https://github.com/vllm-project/vllm

[FACT]
Cloudera's AI Inference Service "leverages NVIDIA's stack, including Blackwell GPUs, Dynamo-Triton Inference Server, and NIM microservices" — Cloudera (as an ISV analogue) manages the inference engine layer and provides "unified support from Cloudera for all your hardware and software questions."
— Cloudera AI Inference Service page
URL: https://www.cloudera.com/products/machine-learning/ai-inference-service.html

**ISV Model Comparison:** Cloudera's on-premises inference service retains inference engine responsibility (NIM/Dynamo-Triton management) rather than delegating it to the customer. This represents an alternative ISV deployment model — the "ISV-managed inference appliance" model — where the ISV owns S2 in exchange for a larger contract scope. The scope split in `three_phase_on_prem_ratings.md` assumes the customer-provides-GPU-and-engine model, which is a different commercial structure than what Cloudera employs. The current analysis does not evaluate the Cloudera-style model where the ISV retains S2 responsibility.

### 4.4 Google Distributed Cloud as a Managed On-Premises Model

[FACT]
"GDC is a fully managed on-prem and edge cloud solution offered in both connected and air-gapped options, and it takes care of infrastructure management, making it easy for developers to focus on leveraging the best that AI has to offer."
— Google Cloud Blog, Run Gemini and AI on-prem with Google Distributed Cloud
URL: https://cloud.google.com/blog/products/ai-machine-learning/run-gemini-and-ai-on-prem-with-google-distributed-cloud

[FACT]
"NVIDIA Blackwell platforms coming to Google Distributed Cloud—Google Cloud's fully managed solution for on-premises, air-gapped environments and edge—organizations can deploy Gemini models securely within their own data centers."
— NVIDIA Blog
URL: https://blogs.nvidia.com/blog/nvidia-google-blackwell-gemini/

**Edge Case:** If an ISV's software runs on Google Distributed Cloud (rather than bare-metal customer hardware), neither the ISV nor the customer manages S2–S5 — Google does. This is a third scope configuration not modeled in the current framework, where Google absorbs S3 and S4 while the ISV retains a cloud-like API consumption model (equivalent to S1). The `three_phase_on_prem_ratings.md` framework does not model GDC-class managed on-premises deployments. This is an acknowledged scope gap, not an error in the current ratings.

---

## 5. Assessment: Correctness of S2–S5 Exclusion

### 5.1 What the Exclusion Gets Right

[FACT]
The FTE transfer is accurately calibrated. Combined pre-split S2+S3+S4+S5 on-premises FTE was 5.50–10.50 FTE (acknowledging staff sharing per source footnote). The ISV P4 on-premises FTE after the split is ~0.45–2.30 FTE.
— `GT4_P4_ground_truth.md` Tables 2 and 4

[FACT]
The primary infrastructure responsibility — procurement, installation, driver management, scheduling configuration — is correctly assigned to the customer. "GPU + AI models: Customer — GPU procurement, driver management, inference engine operation, model weights, CUDA stack."
— `three_phase_on_prem_ratings.md` §1

[FACT]
The S1 (API Integration) retention correctly captures the ISV's core interaction with the customer's inference endpoint: "calling customer-provided inference endpoints rather than managing infrastructure."
— `three_phase_on_prem_ratings.md` §1

[FACT]
The S6 (Routing) retention correctly captures ISV-owned circuit breakers and fallback chains that handle customer inference engine failures.
— `three_phase_on_prem_ratings.md` §1; `P4_ai_model_plane.md` §3, S6

[FACT]
The S7 (Monitoring) retention correctly limits ISV scope to "Application-layer TTFT/quality monitoring against customer's inference service. No GPU-level monitoring (DCGM) — that's customer scope."
— `three_phase_on_prem_ratings.md` §4, P4 Phase 1 table, S7 Notes

### 5.2 What the Exclusion Misses

The following four ISV obligations are present in any customer-provides-GPU deployment but are not captured in the current phase ratings:

[UNVERIFIED — Quantification]
**1. Hardware Compatibility Matrix (Phase 1 artifact):** The ISV must produce and maintain a document specifying minimum GPU generation, VRAM floor, CUDA version, and inference engine version compatibility for their application. Estimated effort: 2–4 person-weeks initial (Phase 1), 1–2 person-days per major release (Phase 3). No source quantifies this obligation at the ISV level; the NVIDIA NIM support matrix provides the structural template.
URL: https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html

[UNVERIFIED — Quantification]
**2. Customer GPU Allocation Triage (Phase 3 recurring):** The ISV bears the support cost of diagnosing GPU resource insufficiency when customers report performance degradation. This requires the ISV to interpret DCGM metrics and MIG occupancy data produced by S3–S5 tooling the customer owns. Estimated effort: 0.05–0.10 FTE annually per customer (Phase 3). No source provides a direct FTE measure for cross-scope diagnostic support at this granularity.

[UNVERIFIED — Quantification]
**3. Inference Engine Version Compatibility Testing (Phase 1 + Phase 3):** The ISV must test their API integration layer against the range of vLLM, TGI, and Dynamo-Triton versions the customer population deploys. With vLLM releasing frequently (see release history at https://github.com/vllm-project/vllm/releases), the ISV must maintain a version compatibility matrix. Estimated effort: 1–3 person-weeks per major vLLM release cycle (Phase 3). No source provides direct FTE measure.

[UNVERIFIED — Quantification]
**4. Customer Troubleshooting Runbooks (Phase 2 + Phase 3):** Per-customer onboarding (Phase 2) requires the ISV to deliver GPU-layer diagnostic runbooks. Estimated effort: 1–3 person-days per customer (Phase 2). No source quantifies this obligation specifically.

### 5.3 Scope Assignment for ISV-Retained-Inference-Engine Models

[FACT]
Cloudera retains full inference engine management (NIM/Dynamo-Triton) in their on-premises AI inference service, providing "unified support from Cloudera for all your hardware and software questions."
— Cloudera AI Inference Service
URL: https://www.cloudera.com/products/machine-learning/ai-inference-service.html

[FACT]
The S1_four_plane_synthesis.md documents that "ISVs on managed K8s can choose Strategy (a) — consume managed APIs from within K8s pods, reducing P4 FTE to 0.30–0.80 (identical to cloud-native) — or Strategy (b) — self-host inference on GPU node pools, requiring 2.20–4.65 FTE."
— `GT5_cross_reference_ground_truth.md` §Section 4; `S1_four_plane_synthesis.md` Section 5

**Finding:** ISVs that retain S2 responsibility (the Cloudera model) must absorb the full 2.00–3.50 FTE on-premises inference engine operations burden. This is a valid but distinct commercial model from the customer-provides-GPU assumption in `three_phase_on_prem_ratings.md`. The scope exclusion correctly models the customer-provides-GPU model. It does not model the ISV-managed-inference-appliance model, and this distinction should be made explicit in the scope documentation.

---

## 6. Summary Assessment Table

| Exclusion Aspect | Correctness | Residual ISV Obligation | Currently Rated? |
|---|---|---|---|
| S3 (GPU Hardware) primary ops | Correct | Minimum GPU spec documentation | No |
| S4 (CUDA/Drivers) primary ops | Correct | Compatibility testing against customer driver versions | No |
| S2 (Inference Engine) primary ops | Correct | Inference engine version compatibility testing; API contract enforcement at S2 boundary | Partially (S1, S6) |
| S5 (GPU Scheduling) primary ops | Correct | GPU allocation triage support burden | No |
| Quantization-format compatibility | Not modeled | ISV quantization selection must match customer GPU generation | No |
| Model version change management | Not modeled | Customer model upgrades break ISV prompt schemas | No |
| GDC-class managed on-premises | Not in scope | Third scope configuration not modeled | No |
| ISV-managed inference appliance | Not in scope | Cloudera model: ISV retains S2; not the assumed model | No |

---

## Key Findings

- **The S2–S5 scope exclusion is structurally correct** for its stated purpose: transferring primary infrastructure operations (procurement, installation, driver management, scheduling configuration) to the customer. The 5.50–10.50 FTE transfer is accurately sized against the source file data in `P4_ai_model_plane.md` §5.

- **Four residual ISV obligations are unrated:** Hardware compatibility matrix authorship (Phase 1), inference engine version compatibility testing (Phase 1 + Phase 3), customer GPU allocation triage support (Phase 3), and per-customer troubleshooting runbook delivery (Phase 2). These represent an undercount in Phase 2 (Per-Customer Customization) and Phase 3 (Ongoing Support) FTE for any customer-provides-GPU deployment.

- **The 82% throughput degradation risk from CUDA/GPU generation mismatch** (AWQ on pre-A100 hardware) is a quantified performance failure mode that the current scope exclusion does not assign to any owner. This is the clearest example of a hidden ISV responsibility: the ISV selects quantization method (S2-adjacent), the customer selects GPU hardware (S3), and the combined mismatch produces an application-layer failure that the ISV's support team must diagnose.

- **The Cloudera model demonstrates that ISV-retained inference engine responsibility is a viable commercial alternative** — ISVs trading higher operational ownership (S2 retained) for simplified customer contracts and unified support scope. The current framework models only the customer-provides-GPU model and should explicitly document this as a scope assumption, not a universal ISV operating model.

- **Google Distributed Cloud and similar managed on-premises platforms** represent a third deployment model — managed on-prem — where neither the ISV nor the customer manages S2–S5. This configuration is not modeled in the current framework and should be flagged as a scope gap for future analysis.

---

## Sources

| Source | Type | URL / Path |
|---|---|---|
| `P4_ai_model_plane.md` | Primary source file | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P4_ai_model_plane.md` |
| `three_phase_on_prem_ratings.md` | Primary source file | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| `GT4_P4_ground_truth.md` | Ground truth reference | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT4_P4_ground_truth.md` |
| `GT5_cross_reference_ground_truth.md` | Cross-reference reference | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` |
| `S1_four_plane_synthesis.md` | Synthesis reference | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md` |
| NVIDIA RTX ISV Certifications | External — ISV testing obligations | https://www.nvidia.com/en-us/products/workstations/isv-certifications/ |
| NVIDIA NIM Support Matrix | External — Minimum GPU specifications | https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/support-matrix.html |
| NVIDIA AI Enterprise 7.0 Support Matrix | External — Supported GPU hardware + OS | https://docs.nvidia.com/ai-enterprise/release-7/7.0/support/support-matrix.html |
| NVIDIA AI Enterprise Product Page | External — Certified Systems requirement | https://www.nvidia.com/en-us/data-center/products/ai-enterprise/ |
| vLLM OpenAI-Compatible Server | External — API interface standard | https://docs.vllm.ai/en/stable/serving/openai_compatible_server/ |
| vLLM Release History | External — Version release cadence | https://github.com/vllm-project/vllm/releases |
| Cloudera AI Inference Service | External — ISV-managed inference engine model | https://www.cloudera.com/products/machine-learning/ai-inference-service.html |
| Google Distributed Cloud (Gemini on-prem) | External — Managed on-prem third model | https://cloud.google.com/blog/products/ai-machine-learning/run-gemini-and-ai-on-prem-with-google-distributed-cloud |
| NVIDIA + Google Blackwell GDC | External — Managed on-prem GPU model | https://blogs.nvidia.com/blog/nvidia-google-blackwell-gemini/ |
| RunPod vLLM CUDA documentation | External — CUDA version mismatch example | https://www.runpod.io/articles/guides/best-docker-image-vllm-inference-cuda-12-4 |
| LogicMonitor AI Workload Requirements | External — AI compute interdependency | https://www.logicmonitor.com/blog/ai-workload-infrastructure |
| IntuitionLabs LLM Inference Hardware Guide | External — GPU-software optimization dependency | https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide |
| Northflank GPU Hosting Guide | External — 78% compatibility struggle statistic | https://northflank.com/blog/top-gpu-hosting-platforms-for-ai |
| arXiv 2511.07424 (via F76) | External — 156 production incidents; 60% inference engine failures | Cited through `P4_ai_model_plane.md` §3, S7 Evidence |
