# P4: AI Model Plane — MECE Subsegment Analysis

**Plane:** AI Model Plane (Plane 4 of 4)
**Scope:** LLM inference serving, GPU infrastructure, model routing and load balancing, inference monitoring, and model lifecycle management
**Deployment Tiers Evaluated:** Cloud-Native (Tier 1), Managed Kubernetes (Tier 2), On-Premises (Tier 3)
**Date:** 2026-02-19
**Status:** COMPLETE

---

## 1. Scope Definition and Exclusions

The AI Model Plane covers the infrastructure and operational responsibilities required to make language model inference available, reliable, and cost-efficient within an ISV's SaaS application. It begins where the application logic plane ends (at the LLM API call boundary) and ends where the underlying compute infrastructure begins (OS, virtualization, physical hardware procurement).

**In Scope:**
- Consuming managed LLM API endpoints (Bedrock, Azure OpenAI, Vertex AI)
- Deploying and operating self-hosted inference engines (vLLM, TGI, Triton, Dynamo)
- GPU hardware procurement planning and physical/virtual resource management
- GPU driver, CUDA stack, and container toolkit management
- Multi-tenant GPU scheduling and resource allocation (MIG, time-slicing, DRA, KAI Scheduler)
- Model routing and load balancing across replicas, models, and providers
- Inference monitoring and latency management (TTFT, TPS, queue depth, DCGM metrics)
- Model lifecycle management (downloads, storage, version switching, A/B testing, rollback)

**Explicitly Excluded:**
- Model training and fine-tuning pipelines
- AI safety, guardrails, and content filtering (separate security/trust domain)
- AI agent orchestration and tool-calling frameworks (covered in Application Logic Plane)
- Embedding pipelines, vector databases, and RAG orchestration (Data Plane scope)
- Prompt engineering, prompt caching, and prompt management
- General Kubernetes control-plane and node operations (covered in Control Plane)

---

## 2. MECE Subsegment Identification

Eight subsegments are identified. Each is **Mutually Exclusive**: no ISV operational responsibility overlaps between subsegments. Collectively they are **Exhaustive**: every ISV activity within the AI Model Plane scope maps to exactly one subsegment.

### MECE Validation

| Subsegment | Exclusive Boundary | Exhaustiveness Claim |
|---|---|---|
| S1: Managed API Integration | Ends at API call; S2 begins at inference engine binary | Covers all managed-endpoint consumption patterns |
| S2: Self-Hosted Inference Engine Deployment | Bounded below by OS/CUDA (S4) and above by routing (S6) | All inference engine install, tune, and serve operations |
| S3: GPU Hardware Infrastructure | Physical/virtual hardware only; excludes driver software (S4) | All procurement, rack, power, and cooling decisions |
| S4: GPU Driver and CUDA Stack Management | Driver layer only; excludes scheduling policy (S5) | All driver, toolkit, and firmware operations |
| S5: Multi-Tenant GPU Scheduling and Resource Allocation | Scheduling policy only; excludes hardware (S3) and driver (S4) | All isolation, partitioning, and allocation decisions |
| S6: Model Routing and Load Balancing | Traffic distribution only; excludes serving engine internals (S2) | All routing, failover, and cost-optimization patterns |
| S7: Inference Monitoring and Observability | Observability data collection only; excludes routing decisions (S6) | All metrics, alerting, and inference-specific tracing |
| S8: Model Lifecycle Management | Storage, versioning, and promotion only; excludes serving config (S2) | All model artifact management operations |

**MECE Confirmation:** An ISV choosing cloud-native tier will engage S1, S6 (at gateway level), S7 (application-level metrics), and S8 (version selection). S2, S3, S4, and S5 reduce to zero effort at this tier. An ISV on-premises engages all eight subsegments simultaneously, with no overlap between them.

---

## 3. Subsegment Difficulty Ratings

**Scale:** 1 = Trivial | 2 = Low | 3 = Moderate | 4 = High | 5 = Very High

**Managed K8s Bifurcation Note:** For the Managed K8s tier, ISVs have two strategies: (a) consume managed APIs through the Kubernetes workload (equivalent to Tier 1 difficulty for S1 and negligible for S3–S5), or (b) self-host inference engines on GPU node pools. The ratings below represent Strategy (b) — self-hosting on GPU node pools — which is the differentiated K8s posture. Strategy (a) collapses S2–S5 to the same ratings as Cloud-Native.

---

### S1: Managed API Integration

**Definition:** Consuming cloud-provider LLM API endpoints (Amazon Bedrock, Azure OpenAI Service/Foundry Models, Vertex AI Gemini API) as the inference backend. The ISV writes requests to HTTP endpoints and manages API keys, quota, rate limits, fallback logic, and response parsing. No GPU, no serving engine, no model weights.

**What the ISV owns:**
- API authentication and key rotation (Bedrock IAM, Azure API key/Entra, Vertex SA)
- Rate limit handling and retry logic (exponential backoff, jitter)
- Response schema parsing and error normalization across providers
- Provider selection, fallback ordering, and SLA monitoring
- Cost tracking and per-customer token attribution

**Evidence:**

[FACT]
"Amazon Bedrock provides access to approximately 100 serverless foundation models from 12+ providers; the ISV does not manage GPU provisioning, model serving infrastructure, or scaling."
— F10 (wave2/F10_aws_ai_ml.md)

[STATISTIC]
Bedrock FTE for inference operations alone: 0.0–0.1 FTE; comparison on-premises: 1.0–2.0 FTE.
— F10 (wave2/F10_aws_ai_ml.md)

[FACT]
Azure OpenAI PTU (Provisioned Throughput Units) start at approximately $2,448/month and use a leaky-bucket utilization algorithm; quota reservation does NOT guarantee capacity — capacity must be verified separately.
— F18 (wave3/F18_azure_ai_ml.md)

[FACT]
Vertex AI Gemini API pricing: Gemini 2.5 Pro at $1.25–$10/M tokens; 2.5 Flash at $0.30–$2.50/M; 50% batch discount applies.
— F26 (wave4/F26_gcp_ai_ml.md)

[STATISTIC]
Aggregate FTE for full Azure OpenAI operations (ongoing): 0.1–0.25 FTE.
— F18 (wave3/F18_azure_ai_ml.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **1** | Call an HTTPS endpoint. Provider handles GPU, serving, scaling, failover, and model versioning. ISV manages API keys, rate-limit handling, and token cost attribution — standard software engineering. |
| Managed K8s | **1** | Managed API calls from within a K8s pod require no additional infrastructure beyond a network egress path. Difficulty is identical to Cloud-Native for this subsegment. |
| On-Premises | **2** | On-prem environments require outbound internet routing, proxy configuration, and air-gapped alternatives. Where network policy blocks public API egress, ISV must maintain a proxy or local API endpoint. Minor elevation only. |

**FTE Estimates:**
- Cloud-Native: 0.05–0.15 FTE (API key rotation, rate-limit tuning, cost dashboards)
- Managed K8s: 0.05–0.15 FTE (same as cloud-native; no added K8s complexity)
- On-Premises: 0.1–0.3 FTE (proxy management, egress policy, air-gap workarounds)

---

### S2: Self-Hosted Inference Engine Deployment

**Definition:** Installing, configuring, tuning, and operating open-source LLM inference engines — primarily vLLM, but also TGI v3, NVIDIA Dynamo-Triton, TensorRT-LLM, and LMDeploy — on hardware the ISV controls. Covers initial deployment, engine parameter tuning, quantization configuration, HA topology, rolling upgrades, and engine-level observability integration.

**What the ISV owns:**
- Engine selection and version pinning
- Continuous batching parameter tuning (max-batch-size, max-tokens-per-batch)
- PagedAttention configuration and KV-cache sizing
- Quantization method selection (AWQ, GPTQ, GGUF) and accuracy validation
- Multi-node tensor-parallel deployment (InfiniBand/RoCE configuration)
- Rolling upgrade and zero-downtime restart procedures
- Engine crash recovery and health probe configuration

**Evidence:**

[STATISTIC]
vLLM achieves P99 latency of 80ms and 793 tokens/second versus Ollama's 673ms P99 and 41 TPS; vLLM maintains 85–92% GPU utilization under high concurrency.
— F36 (wave5/F36_onprem_llm_inference.md), W05S (synthesis/W05S_onprem_app_patterns.md)

[FACT]
Stripe migrated to vLLM and reduced inference costs 73%; handled 50M daily API calls on one-third of the previous GPU fleet.
— F36 (wave5/F36_onprem_llm_inference.md)

[STATISTIC]
vLLM Production Stack (released January 2025): 3–10x lower response latency and 2–5x higher throughput versus baseline vLLM + KServe through prefix-aware routing and LMCache KV-cache sharing.
— F05 (wave1/F05_llm_model_serving.md)

[STATISTIC]
AWQ 4-bit quantization: 95% accuracy retention, 0.036 MAE; GPTQ: 90% accuracy retention, 0.049 MAE; GGUF: 92% accuracy retention, 0.041 MAE.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
A 70B FP16 model requires 168GB VRAM; AWQ INT4 quantization reduces this to approximately 35GB — fitting on a single A100 80GB or H100.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
Multi-node LLM inference requires 200–400 Gbps InfiniBand or RoCE interconnect; NVMe at 7GB/s loads a 70B model in approximately 20 seconds; network-attached storage at 500MB/s requires approximately 5 minutes.
— F36 (wave5/F36_onprem_llm_inference.md)

[STATISTIC]
KServe v0.15 (June 2025): ships vLLM 0.8.5 backend with KEDA integration for LLM autoscaling.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[STATISTIC]
Total on-premises LLM inference staffing: 2.0–3.0 FTE active plus 0.45 FTE on-call.
— F36 (wave5/F36_onprem_llm_inference.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **1** | Not applicable — cloud-native ISVs do not self-host inference engines. Managed providers (Bedrock, Azure OpenAI, Vertex AI) fully abstract the engine layer. Difficulty rating represents the absence of this burden. |
| Managed K8s | **3** | KServe v0.15 + vLLM on GPU node pools is a supported, documented path. Helm charts, GPU Operator integration, and KEDA autoscaling reduce the setup burden. However, continuous batching tuning, quantization validation, multi-node tensor-parallel configuration, and zero-downtime rolling upgrades require ML infrastructure expertise. Estimated 4–8 weeks initial setup; ongoing 1.0–1.5 FTE. |
| On-Premises | **5** | All of Managed K8s complexity plus: multi-node InfiniBand/RoCE provisioning (200–400 Gbps), NVMe model storage tuning (7GB/s vs. 500MB/s network-attached), tensor-parallel topology configuration, and manual health probe management. vLLM Production Stack configuration (prefix-aware routing, LMCache) adds additional operational surface. 2.0–3.0 FTE active plus 0.45 FTE on-call. |

**FTE Estimates:**
- Cloud-Native: 0 FTE (engine managed by provider)
- Managed K8s: 0.75–1.5 FTE (KServe + vLLM operations)
- On-Premises: 2.0–3.5 FTE (full engine + network + quantization ops)

---

### S3: GPU Hardware Infrastructure

**Definition:** Procurement, physical installation, power and cooling provisioning, and virtualization/cloud GPU instance lifecycle management. On-premises: physical GPU servers, racks, power density planning. Cloud/K8s: GPU instance type selection, node group configuration, spot/reserved capacity strategy.

**What the ISV owns (on-premises):**
- GPU hardware selection (H100, A100, L40S, H200) and procurement negotiation
- Data center rack planning, power density upgrades, cooling system modifications
- Physical server installation, NVLink/NVSwitch cabling, InfiniBand fabric
- Hardware lifecycle management, firmware updates, RMA processing
- Spare unit inventory and hot-standby planning

**What the ISV owns (cloud/K8s):**
- GPU instance type selection for workload fit (A10G vs. A100 vs. H100)
- Node group sizing, reserved capacity commitments, and spot interrupt handling
- GPU fleet capacity forecasting and cost commitment decisions

**Evidence:**

[STATISTIC]
NVIDIA DGX H100 (8-GPU): $373K–$450K retail; a 1,000-GPU cluster costs $30–$50M.
— F39 (wave6/F39_onprem_compute.md)

[STATISTIC]
H100 enterprise lead times: 9–12 months for standard orders (F36); improved to 5–6 month average in 2025 from 40+ weeks in 2023–2024 (F39).
— F36 (wave5/F36_onprem_llm_inference.md), F39 (wave6/F39_onprem_compute.md)

[STATISTIC]
Secondary market H100 units trade at approximately $90K — roughly 2x retail price.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
Data center modifications for medium-scale AI GPU deployments (AI GPU racks require 30–80 kW per rack versus traditional 8–15 kW): cost $25K–$100K+ for medium-scale deployments.
— F39 (wave6/F39_onprem_compute.md)

[STATISTIC]
AWS H100 cloud pricing: $1.49–$6.98/hour; AWS implemented a 44% price cut in June 2025.
— F05 (wave1/F05_llm_model_serving.md)

[STATISTIC]
On-premises GPU utilization break-even: cost-advantageous over cloud at 60–70%+ sustained utilization over 3+ years; at 80% utilization, on-premises = $0.48/GPU-hour versus $0.75/GPU-hour cloud.
— F39 (wave6/F39_onprem_compute.md)

[STATISTIC]
Spot GPU instances on AWS and Azure: up to 90% savings.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[STATISTIC]
Karpenter (EKS), NAP/Karpenter (AKS GA July 2025), and ComputeClasses (GKE Autopilot) provide scale-to-zero GPU economics on managed K8s.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[STATISTIC]
Industry benchmark: approximately 10 specialized engineers per 1,000 GPUs; approximately 2 FTE per 200 GPUs. Total on-prem compute staffing: 2.5–5.0 FTE for a 200-GPU deployment.
— F39 (wave6/F39_onprem_compute.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **1** | Zero hardware burden. ISV selects GPU-backed model tiers through the API; provider manages physical GPU fleet, capacity, and hardware lifecycle. No procurement, no rack, no power planning. |
| Managed K8s | **2** | ISV configures GPU node groups (instance type, node count, autoscaler policy) and selects between on-demand and spot capacity. Node auto-provisioners (Karpenter, NAP, ComputeClasses) automate much of this. Spot interrupt handling and capacity reservation commitments require judgment but no hardware expertise. |
| On-Premises | **5** | Full hardware ownership: procurement cycles of 5–12 months, $373K–$450K per DGX H100 unit, data center modifications costing $25K–$100K+, 30–80 kW/rack power density requirements, NVLink/InfiniBand cabling, and 2–5 FTE dedicated infrastructure staff. Secondary market procurement at 2x retail is the only alternative to multi-month lead times. |

**FTE Estimates:**
- Cloud-Native: 0 FTE (hardware owned by provider)
- Managed K8s: 0.1–0.25 FTE (node group configuration, capacity planning)
- On-Premises: 2.5–5.0 FTE (dedicated compute infrastructure team)

---

### S4: GPU Driver and CUDA Stack Management

**Definition:** Installing, versioning, and maintaining the NVIDIA driver stack on GPU nodes: kernel drivers, CUDA toolkit, container toolkit (nvidia-container-runtime), and firmware. Includes managing driver compatibility matrices across CUDA versions, ML frameworks (PyTorch, JAX), and inference engine releases. On Kubernetes: GPU Operator lifecycle management.

**What the ISV owns:**
- Driver version selection pinned to CUDA version, PyTorch version, and vLLM version
- GPU Operator component management: Driver DaemonSet, Container Toolkit, Device Plugin, GFD, DCGM Exporter, MIG Manager
- Kernel driver update and node drain procedures
- Container runtime configuration for GPU passthrough
- Firmware update scheduling and validation

**Evidence:**

[FACT]
NVIDIA GPU Operator components: GPU Driver DaemonSet, Container Toolkit, Device Plugin, GPU Feature Discovery, DCGM Exporter, MIG Manager — all managed as Kubernetes DaemonSets.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[FACT]
CNCF AI Conformance Program launched November 2025; AKS certified as AI-conformant December 2025 — standardizing GPU operator compatibility across managed K8s distributions.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[STATISTIC]
AWQ on older GPU generations (pre-A100): up to 82% inference throughput slowdown without efficient 4-bit CUDA kernels — driver/CUDA version compatibility is a direct performance variable.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
NVIDIA GPU failure rates: V100 approximately 1.5%/year; A100 0.8–1.2%/year; H100 estimated <0.8%/year.
— F39 (wave6/F39_onprem_compute.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **1** | Provider manages all GPU drivers, CUDA versions, and firmware. ISV does not interact with the driver stack; model API responses are independent of driver state. |
| Managed K8s | **2** | GPU Operator installed via Helm chart manages the driver DaemonSet, Container Toolkit, and Device Plugin automatically. CNCF AI Conformance certification (AKS December 2025) reduces compatibility uncertainty. ISV must still pin GPU Operator version and validate compatibility on node image updates. |
| On-Premises | **4** | Full CUDA compatibility matrix ownership: driver version must align with CUDA toolkit, PyTorch, vLLM, and TensorRT versions simultaneously. Node drain procedures for driver updates require coordination with inference scheduling. Firmware updates require vendor engagement. AWQ performance on older GPU generations requires kernel version validation. |

**FTE Estimates:**
- Cloud-Native: 0 FTE
- Managed K8s: 0.1–0.25 FTE (GPU Operator version tracking, compatibility validation)
- On-Premises: 0.5–1.0 FTE (driver management, firmware, CUDA stack ownership)

---

### S5: Multi-Tenant GPU Scheduling and Resource Allocation

**Definition:** Configuring and operating policies that allocate GPU resources among multiple concurrent workloads, tenants, or inference replicas. Includes NVIDIA MIG partitioning, GPU time-slicing, Dynamic Resource Allocation (DRA), gang scheduling, topology-aware scheduling, and queue-level fairshare policies. The objective: maximize GPU utilization while providing predictable, isolated performance per tenant.

**What the ISV owns:**
- MIG partition configuration (per-GPU profile selection and reconfiguration)
- DRA ResourceClaim design and scheduling policy
- KAI Scheduler configuration for topology-aware and gang scheduling
- Time-slicing policy for lower-isolation multi-tenant scenarios
- Fairshare queue policies and priority preemption rules

**Evidence:**

[FACT]
NVIDIA MIG partitions A100/H100 into up to 7 isolated instances with hardware-level isolation. Example for on-prem LLM + embedding: 1x 3g.40gb (LLM inference 7B–13B) + 2x 2g.20gb (embedding models) on a single H100.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
Dynamic Resource Allocation (DRA) graduated to GA in Kubernetes 1.34 (August 2025); GA features: Alternative Device Selection, Consumable Capacity, Resource Health Status.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[FACT]
KAI Scheduler v0.10 (October 2025): NVIDIA open-sourced in April 2025; features Topology-Aware Scheduling, Hierarchical PodGroups, Time-based Fairshare, and gang scheduling for distributed inference.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[STATISTIC]
GPUs sit "reserved and underutilized 60–80% of the time" on managed Kubernetes without proper scheduling policies.
— F55b (wave7/F55b_k8s_gpu_ai.md)

[STATISTIC]
W05S: GPU contention between LLM inference and embedding workloads is "the primary operational risk on-premises"; without explicit MIG partitioning on A100/H100 hardware, embedding latency degrades unpredictably under LLM load.
— W05S (synthesis/W05S_onprem_app_patterns.md)

[STATISTIC]
GPU Scheduling/Sharing rated 5/5 on-premises, 3/5 managed K8s, 1/5 cloud-native.
— W05S (synthesis/W05S_onprem_app_patterns.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **1** | Provider allocates GPU compute per request. ISV has no scheduling surface. Multi-tenancy is the provider's SLA responsibility. |
| Managed K8s | **3** | DRA (K8s 1.34 GA) and KAI Scheduler provide a Kubernetes-native scheduling layer, but require explicit ResourceClaim design, taint/toleration configuration, and node topology awareness. MIG profiles must be configured before workload scheduling. Without these, GPUs are underutilized 60–80% of the time. |
| On-Premises | **5** | MIG profile reconfiguration requires node drain (hot reconfiguration not always supported). Contention between LLM inference and embedding workloads must be resolved manually via explicit MIG partitions. DRA and KAI Scheduler configuration complexity increases with heterogeneous GPU fleet (mixed A100/H100/L40S). Total GPU scheduling staffing overlaps with S3/S4 (not double-counted): incremental 0.25–0.5 FTE. |

**FTE Estimates:**
- Cloud-Native: 0 FTE
- Managed K8s: 0.25–0.5 FTE (DRA policy, KAI Scheduler, MIG profiles)
- On-Premises: 0.5–1.0 FTE (MIG management, contention resolution, heterogeneous fleet)

---

### S6: Model Routing and Load Balancing

**Definition:** Distributing inference requests across replicas, model variants, and providers to optimize cost, latency, and reliability. Includes replica-level load balancing (CHWBL, round-robin, least-connections), multi-model routing (routing cheap vs. expensive models based on query complexity), provider failover (cloud API fallback chains), A/B traffic splitting for model versions, and prefix-aware routing for KV-cache hit rate optimization.

**What the ISV owns:**
- Routing algorithm selection and configuration (CHWBL, prefix-aware, cost-weighted)
- Provider fallback chain definition and health check configuration
- LiteLLM or vLLM Router gateway deployment and tuning
- RouteLLM classifier training or configuration for complexity-based routing
- Traffic split management for A/B model evaluation in production
- Timeout, retry budget, and circuit breaker policy per upstream

**Evidence:**

[STATISTIC]
RouteLLM (ICLR 2025, UC Berkeley/Anyscale/Canva): achieves 85% cost reduction while maintaining 95% GPT-4 performance through complexity-based routing.
— F05 (wave1/F05_llm_model_serving.md), W01S (synthesis/W01S_foundation_patterns.md)

[STATISTIC]
CHWBL (Consistent Hash with Bounded Loads) load-balancing algorithm: 95% TTFT reduction versus Kubernetes default load balancer for LLM inference.
— F05 (wave1/F05_llm_model_serving.md)

[FACT]
LiteLLM: unified gateway supporting 100+ LLM API formats; provides health checking, fallback routing, model version A/B testing, and per-customer token attribution.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
vLLM Router (December 2025): Rust-based high-performance load balancer with Kubernetes-native integration and prefix-aware routing for KV-cache hit rate optimization.
— F05 (wave1/F05_llm_model_serving.md), F55b (wave7/F55b_k8s_gpu_ai.md)

[FACT]
Azure ML Managed Online Endpoints: supports traffic split routing, mirror traffic (shadow mode), and KEDA autoscaling — managed routing surface for Azure-based ISVs.
— F18 (wave3/F18_azure_ai_ml.md)

[FACT]
W01S: multi-model routing should be treated as a "default production configuration rather than optional enhancement" based on the 85% cost reduction evidence.
— W01S (synthesis/W01S_foundation_patterns.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **2** | LiteLLM or a simple SDK-level fallback chain handles provider routing. RouteLLM complexity-routing requires classifier configuration but no infrastructure ownership. The ISV deploys a routing layer as application code or a lightweight sidecar — no GPU, no distributed system. Traffic split A/B testing requires API-level logic. Rated 2 (not 1) because production routing requires explicit retry budgets, circuit breakers, and cost attribution. |
| Managed K8s | **3** | vLLM Router (Kubernetes-native, December 2025) or LiteLLM deployed as a K8s Service adds a managed load-balancing layer. Prefix-aware routing requires router configuration aligned with KServe backend. KEDA autoscaling for routers adds operational surface. Health probe integration with Kubernetes service discovery requires explicit configuration. |
| On-Premises | **4** | All of Managed K8s complexity plus: routing layer must be deployed as an HA service (2–3 replicas), integrated with the on-premises service discovery mechanism (Consul or Kubernetes), and configured with explicit circuit breakers for self-hosted upstream failures. Multi-provider failover to cloud APIs requires outbound network policy, credential management, and latency-aware routing logic. No managed control plane to absorb misconfiguration. |

**FTE Estimates:**
- Cloud-Native: 0.1–0.25 FTE (LiteLLM config, provider fallback tuning, A/B splits)
- Managed K8s: 0.2–0.5 FTE (vLLM Router + KEDA, prefix routing, health probes)
- On-Premises: 0.5–1.0 FTE (HA routing deployment, circuit breakers, provider fallback chains)

---

### S7: Inference Monitoring and Observability

**Definition:** Collecting, aggregating, and alerting on inference-specific metrics: Time to First Token (TTFT), Inter-Token Latency (ITL), Tokens Per Second (TPS), Goodput, request queue depth, GPU memory utilization, and engine health status. Includes integration of DCGM Exporter for GPU hardware metrics, vLLM/KServe Prometheus endpoints, and production incident detection for the inference degradation cascade (Domain 9 in F76).

**What the ISV owns:**
- DCGM Exporter configuration and Prometheus scrape integration
- vLLM and KServe Prometheus metric endpoint configuration
- Alert threshold definition for TTFT SLA, queue depth, and GPU memory pressure
- Grafana dashboard creation for inference-specific panels
- Incident response runbooks for OOM, engine crash, and GPU fault scenarios
- Capacity planning dashboards for token throughput forecasting

**Evidence:**

[STATISTIC]
Domain 9 (AI Model Inference & GPU Failures) from F76: an empirical study of 156 high-severity production AI inference incidents (April–June 2025) found approximately 60% were inference engine failures; ~40% of those were timeouts; ~29% resource exhaustion. Infrastructure-level GPU hardware failures accounted for approximately 20% of incidents. Approximately 74% were auto-detected via health probes; 28% required hotfixes with the highest time-to-mitigation cost.
— F76 (wave11/F76_mece_failure_domain.md), source: arXiv 2511.07424

[STATISTIC]
Domain 9 difficulty ratings from F76: Cloud-Native 2/5, Managed K8s 4/5, On-Premises 5/5.
— F76 (wave11/F76_mece_failure_domain.md)

[STATISTIC]
Domain 9 FTE from F76: Cloud-Native 0.25 FTE; Managed K8s 0.5–1.0 FTE + 0.25 on-call; On-Premises 1.5–2.5 FTE + 0.5 on-call.
— F76 (wave11/F76_mece_failure_domain.md)

[FACT]
Inference Degradation Spiral cascade (F76 Domain 9 → 8 → 11): GPU exhaustion at bursty load → HTTP 429/500 errors → background retraining jobs failing → CPU exhaustion from fallback logic. The arXiv study confirms GPU capacity pressure causes cascading HTTP 429/500 errors.
— F76 (wave11/F76_mece_failure_domain.md)

[FACT]
Key LLM inference metrics: TTFT (Time to First Token), ITL (Inter-Token Latency), TPOT (Time Per Output Token), Goodput — all require custom instrumentation beyond standard HTTP metrics.
— F05 (wave1/F05_llm_model_serving.md)

[FACT]
NVIDIA DCGM Exporter ships as a DaemonSet within GPU Operator and exposes GPU memory utilization, temperature, power draw, and error counters to Prometheus.
— F55b (wave7/F55b_k8s_gpu_ai.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **2** | Provider exposes aggregate latency and throughput metrics via CloudWatch (Bedrock), Azure Monitor (Azure OpenAI), or Cloud Monitoring (Vertex AI). ISV must still instrument application-layer TTFT, per-request token counts, and per-customer cost attribution — not zero effort. No GPU-level metrics available. NVIDIA GROVE provides managed inference observability on cloud K8s (F76). |
| Managed K8s | **4** | GPU Operator's DCGM Exporter provides GPU hardware metrics. vLLM and KServe expose Prometheus endpoints. However, the ISV must configure scrape jobs, create Grafana dashboards for TTFT/ITL/Goodput, define alert thresholds for inference SLA, and integrate GPU fault detection (OOM, hardware error) with incident response runbooks. This is a distinct engineering effort from general K8s monitoring. |
| On-Premises | **5** | All of Managed K8s complexity plus: no managed health probe integration (all probes custom-built), NVLink topology health monitoring required for multi-node inference, thermal and power monitoring via IPMI/BMC, and manual RMA coordination for GPU hardware faults. GPU hardware failure MTTR of 30–120 minutes (F39) requires runbook investment. The 28% of incidents requiring hotfixes (arXiv 2511.07424) demand deep inference-engine expertise. |

**FTE Estimates:**
- Cloud-Native: 0.1–0.25 FTE (provider metric dashboards, application-layer TTFT instrumentation)
- Managed K8s: 0.5–1.0 FTE + 0.25 on-call (DCGM Exporter, Prometheus, Grafana, alert runbooks)
- On-Premises: 1.5–2.5 FTE + 0.5 on-call (full GPU hardware + inference engine observability stack)

---

### S8: Model Lifecycle Management

**Definition:** Managing the storage, distribution, versioning, and promotion of model weight artifacts. Includes model download and caching from Hugging Face/NVIDIA NGC/proprietary registries, NVMe-backed model storage, version pinning in inference engine configuration, blue-green or canary model promotions, A/B testing of model versions in production traffic, and rollback procedures when a model version degrades inference quality.

**What the ISV owns:**
- Model artifact storage (S3, NVMe, shared filesystem) and access controls
- Download automation and checksum validation
- Model version registry and promotion workflow
- A/B traffic split configuration for model evaluation
- Rollback trigger definition (latency SLA breach, quality score threshold)
- Model storage capacity planning (LLaMA 3.1 70B INT4 ≈ 35GB, FP16 ≈ 168GB)

**Evidence:**

[FACT]
Model Lifecycle rated 4/5 on-premises, 3/5 managed K8s, 1/5 cloud-native in W05S difficulty table.
— W05S (synthesis/W05S_onprem_app_patterns.md)

[FACT]
LiteLLM provides model version A/B testing, routing to different model versions, and fallback chains — applicable across all tiers.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
NVMe at 7GB/s loads a 70B model in approximately 20 seconds; network-attached storage at 500MB/s requires approximately 5 minutes — storage architecture directly determines model hot-swap latency.
— F36 (wave5/F36_onprem_llm_inference.md)

[FACT]
Vertex AI Model Garden provides 160+ foundation models including Gemma 3 and Llama available via vLLM pre-built Docker images — managed model registry for GCP ISVs.
— F26 (wave4/F26_gcp_ai_ml.md)

[FACT]
Azure OpenAI and Vertex AI handle model versioning, deprecation scheduling, and rollover on the provider's cadence — ISV cannot control the deprecation timeline.
— F18 (wave3/F18_azure_ai_ml.md), F26 (wave4/F26_gcp_ai_ml.md)

[FACT]
W05S: "Managed API providers can deprecate embedding models on their own schedule, forcing unplanned re-embedding" — analogous risk applies to LLM model version deprecation forcing ISV prompt/response schema changes.
— W05S (synthesis/W05S_onprem_app_patterns.md)

[STATISTIC]
C11 (AI/ML Model Serving & Orchestration) in F73 MECE ISV Developer Responsibility framework: Cloud-Native 2/5, Managed K8s 3/5, On-Premises 5/5 — highest on-premises difficulty alongside C10 Security.
— F73 (wave11/F73_mece_isv_developer_responsibility.md)

| Tier | Difficulty | Rationale |
|---|:---:|---|
| Cloud-Native | **2** | Provider manages all model weights, storage, and versioning. ISV selects a model version string in the API call. Model deprecation is a migration risk (provider-controlled schedule) requiring ISV prompt schema updates and integration testing — rated 2 not 1 because deprecation events require active ISV engineering response. |
| Managed K8s | **3** | Model artifacts pulled from Hugging Face or NVIDIA NGC into shared persistent volumes or NVMe node storage. Version pinning in KServe InferenceService manifests; blue-green rollout via traffic split. Storage capacity planning is an active concern (35–168GB per model version). A/B testing possible via KServe traffic split, but requires GitOps-managed manifest changes. |
| On-Premises | **4** | All Managed K8s complexity plus: ISV must operate a local model registry (no provider-hosted option), manage NVMe storage arrays for hot model cache (7GB/s load speed), coordinate model swaps across multi-node inference clusters, and implement rollback automation. Model checksum validation, access control, and audit logging for regulatory compliance are fully owned. |

**FTE Estimates:**
- Cloud-Native: 0.05–0.15 FTE (version monitoring, deprecation migration planning)
- Managed K8s: 0.25–0.5 FTE (PVC management, version promotion, A/B split configuration)
- On-Premises: 0.5–1.0 FTE (local model registry, NVMe storage ops, rollback automation)

---

## 4. Summary Difficulty Matrix

**Scale:** 1 = Trivial | 2 = Low | 3 = Moderate | 4 = High | 5 = Very High

| # | Subsegment | Cloud-Native | Managed K8s | On-Premises | Gradient (On-Prem minus Cloud) |
|---|---|:---:|:---:|:---:|:---:|
| S1 | Managed API Integration | **1** | **1** | **2** | +1 |
| S2 | Self-Hosted Inference Engine Deployment | **1** | **3** | **5** | +4 |
| S3 | GPU Hardware Infrastructure | **1** | **2** | **5** | +4 |
| S4 | GPU Driver and CUDA Stack Management | **1** | **2** | **4** | +3 |
| S5 | Multi-Tenant GPU Scheduling and Resource Allocation | **1** | **3** | **5** | +4 |
| S6 | Model Routing and Load Balancing | **2** | **3** | **4** | +2 |
| S7 | Inference Monitoring and Observability | **2** | **4** | **5** | +3 |
| S8 | Model Lifecycle Management | **2** | **3** | **4** | +2 |
| | **Plane Average** | **1.4** | **2.6** | **4.3** | **+2.9** |

---

## 5. FTE Summary by Subsegment and Tier

| # | Subsegment | Cloud-Native FTE | Managed K8s FTE | On-Premises FTE |
|---|---|---|---|---|
| S1 | Managed API Integration | 0.05–0.15 | 0.05–0.15 | 0.10–0.30 |
| S2 | Self-Hosted Inference Engine | 0 | 0.75–1.50 | 2.00–3.50 |
| S3 | GPU Hardware Infrastructure | 0 | 0.10–0.25 | 2.50–5.00 |
| S4 | GPU Driver and CUDA Stack | 0 | 0.10–0.25 | 0.50–1.00 |
| S5 | GPU Scheduling and Allocation | 0 | 0.25–0.50 | 0.50–1.00 |
| S6 | Model Routing and Load Balancing | 0.10–0.25 | 0.20–0.50 | 0.50–1.00 |
| S7 | Inference Monitoring | 0.10–0.25 | 0.50–1.00 | 1.50–2.50 |
| S8 | Model Lifecycle Management | 0.05–0.15 | 0.25–0.50 | 0.50–1.00 |
| | **Plane Total** | **0.30–0.80 FTE** | **2.20–4.65 FTE** | **8.10–15.30 FTE** |

*Note: On-premises FTE includes 0.45 FTE on-call for S2 (F36) and 0.5 FTE on-call for S7 (F76). S3 and S4/S5 share infrastructure staff; no double-counting — S3 covers physical hardware, S4 covers driver software, S5 covers scheduling policy.*

*Managed K8s FTE assumes Strategy (b): self-hosting vLLM on GPU node pools. Strategy (a) — consuming managed APIs from within Kubernetes — reduces Managed K8s total to approximately 0.30–0.80 FTE, identical to Cloud-Native.*

---

## 6. Cross-Cutting Observations

**Observation 1: The Managed K8s Bifurcation Is the Dominant Decision Point**

The AI Model Plane is unique among the four planes in that the Managed K8s tier has two operationally distinct strategies whose FTE requirements differ by nearly 6x (0.30–0.80 FTE vs. 2.20–4.65 FTE). Strategy selection — managed API consumption vs. self-hosted inference on GPU node pools — is an irreversible architectural commitment in the sense that migrating from self-hosted to managed API requires rewriting inference integration code, abandoning custom quantization tuning, and accepting provider pricing economics. ISVs should establish explicit decision criteria before committing to Strategy (b).

[FACT]
W05S documents: "F36 notes that on-premises LLM inference is 2.9x–4.1x more cost-effective than cloud APIs for sustained workloads, while F37 notes that managed embedding APIs eliminate six of eight major operational domains. This creates a split decision."
— W05S (synthesis/W05S_onprem_app_patterns.md)

**Observation 2: S3 (GPU Hardware) and S2 (Inference Engine) Are the Primary On-Premises Cost Drivers**

S3 and S2 together account for approximately 55–65% of on-premises AI Model Plane FTE and 100% of the capital expenditure. These two subsegments alone justify the 4.3 average on-premises difficulty score. No other subsegment approaches this magnitude.

[STATISTIC]
W01S: "Self-hosted GPU clusters require 2–4 FTE for initial deployment over 3–6 months at a total cost of $200K–$300K loaded."
— W01S (synthesis/W01S_foundation_patterns.md)

**Observation 3: S7 (Inference Monitoring) Carries Asymmetric Risk**

S7 is rated 4/5 on Managed K8s — higher than S2 (3/5) at the same tier — because 74% of inference incidents are auto-detected through health probes that must be correctly configured by the ISV, and the 28% requiring hotfixes have the highest MTTR. Underinvestment in S7 on Managed K8s is a common failure pattern.

[STATISTIC]
"Approximately 74% of incidents were auto-detected via health probes; 28% required hotfixes with the highest time-to-mitigation cost."
— F76 (wave11/F76_mece_failure_domain.md), source: arXiv 2511.07424

**Observation 4: S6 (Routing) Delivers the Highest ROI Per FTE Invested Across All Tiers**

RouteLLM complexity-based routing achieves 85% cost reduction at 95% quality parity. This is achievable on all three tiers. At Cloud-Native, the marginal cost of implementing RouteLLM or LiteLLM-based routing is 0.1–0.25 FTE — the highest per-FTE return of any subsegment in the plane. W01S explicitly flags this as a "default production configuration rather than optional enhancement."

[STATISTIC]
"RouteLLM: 85% cost reduction maintaining 95% GPT-4 performance."
— F05 (wave1/F05_llm_model_serving.md)

**Observation 5: The AI Model Plane Is Collectively Exhaustive With Adjacent Planes**

- **Control Plane (P1)** boundary: Kubernetes control plane, node operations, and cluster networking are P1 scope. GPU node group configuration (S3) is at the boundary — the node group belongs to P1 but the GPU capacity planning decision belongs to P4. This document treats GPU instance type selection and capacity forecasting as S3 (P4) while treating node pool creation mechanics as P1.
- **Application Logic Plane (P2)** boundary: Agent orchestration, prompt engineering, and LLM API call logic are P2. S1 in this document covers the infrastructure for consuming the API endpoint — not the prompt construction or response parsing business logic.
- **Data Plane (P3)** boundary: Embedding pipelines, vector databases, and RAG orchestration are P3. GPU contention between embedding and LLM inference (documented in S5) is at the boundary — this document treats GPU scheduling policy as S5 (P4), while embedding model serving and pipeline operations belong to P3.

---

## 7. Sources

All ratings are derived from primary research files. Every difficulty rating above is accompanied by at least one inline citation.

| Source File | Key Contributions to This Analysis |
|---|---|
| F05: wave1/F05_llm_model_serving.md | RouteLLM 85% cost reduction; CHWBL 95% TTFT reduction; vLLM Production Stack 3–10x latency improvement; H100 cloud pricing $1.49–$6.98/hour; initial deployment FTE $200K–$300K loaded |
| F10: wave2/F10_aws_ai_ml.md | Amazon Bedrock ~100 serverless models; Bedrock FTE 0.0–0.1; managed API baseline difficulty evidence |
| F18: wave3/F18_azure_ai_ml.md | Azure OpenAI PTU $2,448/month; 0.1–0.25 FTE ongoing; managed routing via Managed Online Endpoints |
| F26: wave4/F26_gcp_ai_ml.md | Vertex AI pricing $0.15–$10/M tokens; 50% batch discount; 160+ Model Garden models |
| F36: wave5/F36_onprem_llm_inference.md | vLLM P99 80ms, 793 TPS; Stripe 73% cost reduction; H100 lead times 9–12 months; multi-node InfiniBand; 2.0–3.0 FTE inference ops; 2.9x–4.1x cost advantage over APIs |
| F39: wave6/F39_onprem_compute.md | DGX H100 $373K–$450K; GPU failure rates V100 1.5%/year, A100 0.8–1.2%/year; 5–6 month lead times 2025; 2.5–5.0 FTE per 200 GPUs; MTTR 30–120 minutes |
| F55b: wave7/F55b_k8s_gpu_ai.md | GPU Operator components; DRA GA K8s 1.34 August 2025; KAI Scheduler v0.10 October 2025; KServe v0.15 June 2025; Karpenter/NAP scale-to-zero; CNCF AI Conformance November 2025; 2–4 FTE managed K8s GPU ops |
| F73: wave11/F73_mece_isv_developer_responsibility.md | C11 AI/ML Model Serving: Cloud-Native 2/5, Managed K8s 3/5, On-Premises 5/5 |
| F76: wave11/F76_mece_failure_domain.md | Domain 9 difficulty ratings: Cloud-Native 2/5, Managed K8s 4/5, On-Premises 5/5; 156 production incidents 60% engine failures; FTE Cloud 0.25, K8s 0.5–1.0+0.25, On-Prem 1.5–2.5+0.5 |
| W01S: synthesis/W01S_foundation_patterns.md | 3–10x FTE differential on-prem vs. cloud-native; GPU as universal bottleneck; routing as default production config |
| W05S: synthesis/W05S_onprem_app_patterns.md | GPU contention primary on-prem risk; LLM inference 2.0–3.5 FTE on-prem; Model Lifecycle 4/5 on-prem; managed API vs. self-hosted split decision |
