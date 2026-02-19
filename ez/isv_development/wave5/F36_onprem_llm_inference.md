# F36: On-Premises LLM Inference Operations

## Executive Summary

Self-hosting large language model inference on-premises delivers maximum data control and — for sustained, high-volume workloads — materially lower per-token costs than cloud APIs, but it imposes a significant and persistent operational burden that most ISVs underestimate. The serving framework landscape has matured rapidly: vLLM has emerged as the de facto production standard for high-concurrency workloads, while HuggingFace Text Generation Inference (TGI) v3 offers competitive performance for latency-sensitive single-user patterns, and NVIDIA Dynamo-Triton suits organizations already invested in the NVIDIA enterprise stack. GPU procurement remains a structural constraint — H100 lead times run 9–12 months for standard enterprise orders — forcing ISVs to plan hardware pipelines well ahead of application demand. Quantization (primarily AWQ for GPU deployments, GGUF for CPU-fallback and mixed environments) can reduce VRAM requirements by 50–75% with under 1% accuracy loss on leading benchmarks, but selecting and validating the right quantization strategy requires dedicated ML engineering expertise. End-to-end, a mid-size production on-premises LLM inference stack — covering serving, monitoring, model lifecycle, and failover — demands approximately 2.0–3.5 FTE of specialized engineering staff beyond baseline DevOps.

---

## 1. Model Serving Frameworks

### 1.1 vLLM

[vLLM](https://github.com/vllm-project/vllm) has become the dominant open-source LLM inference engine for production deployments. It was developed at UC Berkeley and is now backed by 15+ full-time contributors across 6+ organizations including Neural Magic, Anyscale, IBM, AMD, Intel, and NVIDIA.

**Growth and adoption (as of January 2025):**

[FACT] vLLM GitHub stars grew from 14,000 to 32,600 (2.3x) over 2024; monthly downloads grew from 6,000 to 27,000 (4.5x), and GPU hours consumed by the project grew approximately 10x over six months.
URL: https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html
Date: January 10, 2025

[FACT] vLLM powers production deployments including Amazon Rufus and LinkedIn AI features.
URL: https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html
Date: January 10, 2025

[FACT] vLLM supports nearly 100 model architectures spanning LLMs, multimodal systems, encoder-decoder models, and state-space models, with hardware support across NVIDIA (V100+), AMD (MI200/MI300), Google TPUs (v4–v6e), AWS Inferentia/Trainium, Intel Gaudi, and x86/ARM/PowerPC CPUs.
URL: https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html
Date: January 10, 2025

**Core architecture:**

[FACT] vLLM's PagedAttention divides GPU memory into fixed-size pages (typically 16 tokens each), enabling non-contiguous storage that eliminates the KV cache memory fragmentation that plagues traditional allocators — eliminating "60–80% memory waste from KV cache fragmentation."
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

[FACT] Continuous batching in vLLM operates at the iteration level rather than the request level, accepting new requests immediately when sequences complete rather than waiting for fixed batch boundaries, keeping GPU utilization at 85–92% under high concurrency.
URL: https://arxiv.org/html/2511.17593v1
Date: November 2025

**Production deployment requirements:**

- Linux OS required; Python >= 3.8, CUDA 12.0+, NVIDIA GPU driver >= 525
- Kubernetes deployment supported via Helm charts (vLLM Production Stack)
- Key configuration parameters: `replica_count`, `enableChunkedPrefill`, `enablePrefixCaching`, `maxModelLen`, `dtype` (typically `bfloat16`), `tensor_parallel_size`

[FACT] vLLM maintains P99 latency of 80ms versus Ollama's 673ms at equivalent setups, and achieves 793 tokens per second compared to Ollama's 41 tokens per second.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

[FACT] Stripe reduced inference costs by 73% after migrating to vLLM while handling 50 million daily API calls on one-third their previous GPU fleet.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

**vLLM Production Stack (released January 2025):**

[FACT] The vLLM Production Stack is a Kubernetes-native reference deployment providing 3–10x lower response delay and 2–5x higher throughput compared to baseline vLLM + KServe configurations, through prefix-aware routing and KV-cache sharing via the LMCache project.
URL: https://blog.vllm.ai/2025/01/21/stack-release.html
Date: January 21, 2025

[FACT] The vLLM Production Stack comprises four components: KV cache sharing and storage (LMCache), prefix-aware routing, observability (TTFT, TBT, throughput metrics), and Kubernetes-based autoscaling.
URL: https://blog.vllm.ai/2025/01/21/stack-release.html
Date: January 21, 2025

### 1.2 HuggingFace Text Generation Inference (TGI)

[FACT] TGI v3.0 brings "up to 13x faster inference on long prompts compared to vLLM" for conversations exceeding 200,000 tokens; a reply that takes 27.5 seconds in vLLM can be served in approximately 2 seconds in TGI v3 on that specific workload.
URL: https://compute.hivenet.com/post/vllm-vs-tgi-vs-tensorrt-llm-vs-ollama

[FACT] TGI offers built-in telemetry via OpenTelemetry and Prometheus metrics natively, which researchers and practitioners cite as more "production-ready out of the box" relative to baseline vLLM.
URL: https://www.inferless.com/learn/vllm-vs-tgi-the-ultimate-comparison-for-speed-scalability-and-llm-performance

**Benchmark comparison (from peer-reviewed study, November 2025):**

[STATISTIC] At 100 concurrent requests on LLaMA-2-7B, vLLM achieved 15,243 tokens/second versus TGI's 4,156 tokens/second — a 3.67x advantage that widens to 24x under extreme load (200 concurrent requests).
URL: https://arxiv.org/abs/2511.17593
Date: November 2025

[STATISTIC] Memory efficiency at 50 concurrent requests: vLLM consumed 19–27% less GPU memory than TGI across model sizes (7B: vLLM 24.3GB vs TGI 31.7GB; 13B: vLLM 42.8GB vs TGI 54.2GB; 70B: vLLM 68.9GB vs TGI 76.4GB per GPU).
URL: https://arxiv.org/html/2511.17593v1
Date: November 2025

[STATISTIC] Latency at 25 concurrent users: TGI showed lower Time-To-First-Token at low percentiles (7B: TGI 0.18s median vs vLLM 0.24s median) but vLLM maintained better P99 total latency (7B: vLLM 14.18s vs TGI 23.47s) due to faster per-token generation speed.
URL: https://arxiv.org/html/2511.17593v1
Date: November 2025

**Recommendation pattern:** vLLM for high-concurrency workloads (100+ concurrent users, throughput-sensitive); TGI for latency-sensitive interactive applications with moderate concurrency or when the existing tooling is fully HuggingFace-aligned.

### 1.3 NVIDIA Dynamo-Triton (formerly Triton Inference Server)

[FACT] As of March 18, 2025, NVIDIA Triton Inference Server was renamed to NVIDIA Dynamo-Triton and is now part of the NVIDIA Dynamo Platform.
URL: https://developer.nvidia.com/dynamo-triton

[FACT] Dynamo-Triton supports deployment across NVIDIA GPUs, non-NVIDIA accelerators, x86 and ARM CPUs, and integrates with Kubernetes for scaling and Prometheus for monitoring. It supports TensorRT, PyTorch, ONNX, OpenVINO, Python, and RAPIDS FIL backends.
URL: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html

[FACT] NVIDIA also released NVIDIA Dynamo alongside Dynamo-Triton specifically for LLM inference; Dynamo adds disaggregated serving, prefix caching, and key-value caching to storage as LLM-specific optimizations that complement Dynamo-Triton.
URL: https://www.nvidia.com/en-us/ai/dynamo-triton/

**Operational profile:** Dynamo-Triton requires familiarity with NVIDIA's toolchain (TensorRT-LLM model compilation, config.pbtxt model repository format). It is best suited for organizations running mixed workloads (CV, NLP, classical ML) on NVIDIA hardware who want a unified serving tier. The compilation step for TensorRT-LLM models is a one-time overhead but requires GPU-specific re-compilation on hardware upgrades.

### 1.4 Ollama

[FACT] Ollama "is not intended for high-concurrency workloads or optimized inference pipelines, typically found in enterprise-scale use cases" — it is suited for individual developers, early-stage prototyping, and rapid prompt iteration.
URL: https://developers.redhat.com/articles/2025/07/08/ollama-or-vllm-how-choose-right-llm-serving-tool-your-use-case
Date: July 8, 2025

[FACT] Known production limitations of Ollama include: model re-downloads on every restart, model eviction from memory when not recently used (causing cold-start latency spikes), and the inability to share a model in memory across multiple concurrent instances — each instance loads its own copy.
URL: https://collabnix.com/is-ollama-ready-for-production/

[FACT] Ollama targets "small to medium" models (8B–13B parameters) while vLLM handles "small to very large" (70B+) models.
URL: https://developers.redhat.com/articles/2025/07/08/ollama-or-vllm-how-choose-right-llm-serving-tool-your-use-case
Date: July 8, 2025

**ISV guidance:** Ollama is not appropriate for production on-premises inference serving for any multi-user workload. It is a viable developer tooling choice for local testing of small models before deploying on vLLM or TGI.

### Framework Comparison Table

| Capability | vLLM | TGI (v3) | Dynamo-Triton | Ollama |
|------------|------|-----------|----------------|--------|
| Production readiness | Yes | Yes | Yes | No |
| High-concurrency (100+ users) | Excellent | Good | Good | Not suitable |
| Long-context performance | Good | Excellent (13x faster for >200K tokens) | Good | Poor |
| Memory efficiency | Highest | Moderate | Moderate | Low |
| Multi-GPU tensor parallelism | Yes | Yes | Yes | No |
| Observability (built-in) | Prometheus + Grafana | OpenTelemetry + Prometheus | Prometheus | Minimal |
| Model architecture coverage | ~100 architectures | HuggingFace Hub models | NVIDIA-optimized models | GGUF format |
| Ops complexity (1–5 scale) | 3/5 | 3/5 | 4/5 | 1/5 |
| Est. FTE to operate | 0.5–1.0 FTE | 0.5–1.0 FTE | 1.0–1.5 FTE | 0.1 FTE |

---

## 2. GPU Procurement and Allocation

### 2.1 H100 and A100 Lead Times

[FACT] Enterprise H100 system lead times run 9–12 months for standard configurations. Enterprise pre-orders typically face 4–8 month lead times. Secondary market units trade at "double their retail cost" — approximately $90,000 versus the official ~$40,000 MSRP in early 2025.
URL: https://uvation.com/articles/h100-availability-the-silent-crisis-threatening-enterprise-ai-plans

[FACT] Alternative configurations with shorter lead times: Supermicro AS-8125GS-TNHR (10–14 weeks), Dell PowerEdge R760xa with L40S GPUs (4–6 weeks).
URL: https://uvation.com/articles/h100-availability-the-silent-crisis-threatening-enterprise-ai-plans

[FACT] List price for a single NVIDIA H100 GPU (PCIe 80GB variant) is approximately $25,000–$30,000 as of early 2025; an 8-GPU server costs $200,000–$320,000.
URL: https://www.gmicloud.ai/blog/2025-cost-of-renting-or-uying-nvidia-h100-gpus-for-data-centers

[FACT] The H200 with 141GB HBM3e is now widely available ($30,000–$40,000 purchase, $2.15–$6.00/hr cloud), enabling single-GPU serving of 70B models that previously required two H100s.
URL: https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide

[FACT] Enterprises are advised to account for 30–50% premiums on top-tier GPUs and to order hardware well in advance of planning cycles, as "position in the queue is now a critical asset."
URL: https://uvation.com/articles/h100-availability-the-silent-crisis-threatening-enterprise-ai-plans

### 2.2 GPU Sharing: MIG and Workload Co-location

[FACT] NVIDIA Multi-Instance GPU (MIG) technology partitions a single A100 or H100 GPU into up to seven isolated instances, each with dedicated high-bandwidth memory, cache, and compute cores.
URL: https://docs.cast.ai/docs/gpu-sharing-mig

[FACT] MIG is appropriate for workloads that do not fully utilize the GPU's compute capacity — including small-model inference and embedding generation — while providing complete hardware-level memory and fault isolation between partitions.
URL: https://www.redhat.com/en/blog/sharing-caring-how-make-most-your-gpus-part-2-multi-instance-gpu

**Practical allocation pattern for ISVs:** On an H100 80GB, a common split is: one MIG 3g.40gb partition running a full-precision 7B–13B LLM inference workload, and two MIG 2g.20gb partitions running embedding models (e.g., `text-embedding-3-small` equivalents) or smaller classification models. This eliminates the need for dedicated GPU hardware per workload type and improves utilization on partially loaded hardware.

**Memory requirements for reference models:**

[FACT] A 70B parameter model in FP16 precision requires 140GB of GPU memory, necessitating multi-GPU tensor parallelism. In INT4 quantization, the same model fits in 35GB, enabling single-A100 80GB or single-H100 deployment.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

[FACT] NVMe storage at 7GB/s loads a 70B model in approximately 20 seconds; network-attached storage at 500MB/s requires approximately 5 minutes for the same model.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

[FACT] Multi-node deployments require 200–400 Gbps InfiniBand or RoCE networking for efficient pipeline parallelism across GPUs.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

---

## 3. Model Optimization: Quantization and Attention

### 3.1 Quantization Methods

Three primary post-training quantization formats are in active production use for on-premises LLM inference: GPTQ, AWQ, and GGUF. They differ in hardware target, accuracy, and conversion complexity.

**Accuracy benchmarks (MMLU, GSM8K, HumanEval combined; 4-bit quantization vs FP16 baseline):**

[STATISTIC] AWQ 4-bit: Llama 3.1 8B retains 86.8% accuracy (0.7% loss from FP16); Mistral 7B retains 84.6% accuracy (0.7% loss) — lowest accuracy loss of the three methods tested.
URL: https://localaimaster.com/blog/quantization-explained

[STATISTIC] GGUF Q4_K_M: Llama 3.1 8B retains 85.9% accuracy (1.6% loss); Mistral 7B retains 83.8% accuracy (1.5% loss).
URL: https://localaimaster.com/blog/quantization-explained

[STATISTIC] GPTQ 4-bit: Llama 3.1 8B retains 84.7% accuracy (2.8% loss); Mistral 7B retains 83.1% accuracy (2.2% loss).
URL: https://localaimaster.com/blog/quantization-explained

[FACT] AWQ's median absolute error across benchmarks is 0.036 (lowest), versus GGUF Q4_K_M at 0.041 and GPTQ 4-bit at 0.049.
URL: https://localaimaster.com/blog/quantization-explained

[FACT] GPTQ 4-bit on older GPU architectures can paradoxically result in an 82% slowdown despite 41% VRAM reduction, because quantized weights are up-cast to higher precision during inference on hardware that lacks efficient 4-bit compute kernels.
URL: https://www.e2enetworks.com/blog/which-quantization-method-is-best-for-you-gguf-gptq-or-awq

[FACT] GGUF format achieves over 18x improvement in inference throughput compared to FP16 baseline on CPU-only inference, making it the practical choice for CPU-fallback or air-gapped edge deployments.
URL: https://www.ionio.ai/blog/llms-on-cpu-the-power-of-quantization-with-gguf-awq-gptq

[FACT] Over 20% of vLLM deployments currently utilize quantization methods.
URL: https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html
Date: January 10, 2025

**Hardware-to-format recommendation map:**

| Hardware | Recommended Format | Rationale |
|----------|--------------------|-----------|
| NVIDIA H100/A100 (CUDA) | AWQ 4-bit | Lowest accuracy loss, best GPU kernel support |
| NVIDIA RTX 3060/3070 | GPTQ 4-bit | +20% throughput with Marlin kernels on CUDA |
| AMD ROCm | AWQ 4-bit via vLLM | Best ROCm compatibility |
| CPU fallback / air-gapped | GGUF Q4_K_M | Cross-platform, 18x throughput improvement on CPU |
| Apple Silicon (dev/test) | GGUF Q4_K_M | Native metal support |

Source: https://localaimaster.com/blog/quantization-explained

### 3.2 Flash Attention

[FACT] FlashAttention-3 achieves up to 75% GPU utilization on H100s — up from 35% with previous implementations — and delivers 1.5–2.0x faster throughput than FlashAttention-2 on FP16 workloads, reaching up to 740 TFLOPS.
URL: https://www.together.ai/blog/flashattention-3

[FACT] With FP8 precision, FlashAttention-3 reaches close to 1.2 PFLOPS with 2.6x smaller numerical error than baseline FP8 attention.
URL: https://pytorch.org/blog/flashattention-3/

**Operational note:** FlashAttention-3 requires H100-generation hardware; it is not compatible with A100 or earlier architectures. Enabling it requires explicit compilation of the flash-attention wheel against the correct CUDA toolkit version — this is a one-time setup cost but is a source of version-mismatch failures when upgrading CUDA.

### 3.3 Operational Difficulty — Optimization

| Optimization Domain | Difficulty | Key Requirements |
|---------------------|------------|------------------|
| AWQ quantization (GPU) | 2/5 | Pre-quantized weights available from HuggingFace; minimal calibration needed |
| GPTQ quantization | 3/5 | Requires calibration dataset; GPU-specific kernel tuning |
| GGUF conversion | 2/5 | llama.cpp toolchain; straightforward CLI workflow |
| FlashAttention-3 enablement | 3/5 | H100 required; CUDA version pinning; compilation step |
| Speculative decoding setup | 4/5 | Draft model selection; compatibility constraints with pipeline parallelism |
| Multi-GPU tensor parallelism | 4/5 | InfiniBand/RoCE networking; NCCL tuning; hardware topology awareness |

---

## 4. Latency Optimization

### 4.1 KV Cache Management

[FACT] vLLM implements a hierarchical KV cache: GPU memory first, CPU memory second, then remote KV connectors (e.g., network-attached cache stores). On cache miss, it progresses through the hierarchy before generating from scratch.
URL: https://docs.vllm.ai/en/latest/features/spec_decode/

[FACT] Cross-instance KV cache sharing via the LMCache project delivers 3–10x latency reduction for repetitive workloads (e.g., shared system prompts, document-grounded Q&A).
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

[FACT] The vLLM production stack's prefix-aware routing directs requests to the backend instance already holding the relevant cached KV data, maximizing reuse and reducing TTFT.
URL: https://blog.vllm.ai/2025/01/21/stack-release.html
Date: January 21, 2025

### 4.2 Speculative Decoding

[FACT] vLLM's speculative decoding uses a small, fast "draft" model (or an n-gram lookup method) to propose the next several tokens; the main model verifies these tokens in one parallel pass, delivering 2–3x acceleration for predictable output patterns.
URL: https://docs.vllm.ai/en/latest/features/spec_decode/

[FACT] Speculative decoding in vLLM is not compatible with pipeline parallelism; EAGLE-based draft models must be run with `draft_tensor_parallel_size` set to 1, though the main model can still use tensor parallelism.
URL: https://docs.vllm.ai/en/latest/features/spec_decode/

**Operational constraint:** Speculative decoding requires careful draft model selection and quality validation on the ISV's specific workload distribution. For code generation or structured output (high predictability), gains are maximized. For open-ended creative generation, gains are minimal and the overhead of the draft model may reduce net throughput.

### 4.3 Tensor Parallelism

[FACT] Tensor parallelism in vLLM (`tensor_parallel_size`) shards model weights across GPUs on the same node, with each GPU holding a subset of weights. Increasing tensor_parallel_size allows each GPU more memory capacity for KV cache allocation, which increases maximum concurrent request capacity.
URL: https://docs.vllm.ai/en/stable/configuration/optimization/

[FACT] Pipeline parallelism splits model layers across devices, enabling parallel stage execution across nodes; it requires 200–400 Gbps InfiniBand or RoCE between nodes.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

---

## 5. Multi-Model Serving and Routing

### 5.1 Architecture Pattern

On-premises multi-model serving requires three components: (1) individual model endpoints (one vLLM or TGI process per model, or MIG partition), (2) a routing/gateway layer, and (3) a model registry.

[FACT] The enterprise LLM landscape is moving from single-model deployments to orchestrated multi-model architectures that route prompts dynamically across models based on latency, cost, data sovereignty, and accuracy requirements.
URL: https://www.gurustartups.com/reports/enterprise-llm-reference-architecture-for-multi-model-routing

[FACT] vLLM Production Stack supports multi-model deployment via the `modelSpec` field in its Helm chart `values.yaml`, enabling different vLLM instances to serve different models on different GPUs within the same Kubernetes cluster.
URL: https://blog.vllm.ai/production-stack/tutorials/04-launch-multiple-model.html

### 5.2 Routing and Gateway: LiteLLM

[FACT] LiteLLM acts as a unified gateway supporting 100+ LLM API formats (OpenAI-compatible), enabling organizations to manage, monitor, and optimize LLM usage across cloud and on-premises environments with cost tracking, guardrails, load balancing, and logging.
URL: https://github.com/BerriAI/litellm

[FACT] LiteLLM proxy supports models assigned an `order` parameter for fallback priority: higher priority models are tried first; lower priority models are invoked when higher-priority ones are unavailable (requires `enable_pre_call_checks: true`).
URL: https://docs.litellm.ai/docs/proxy/reliability

[FACT] RouteLLM, from LMSYS, is an open-source framework for LLM routing that has demonstrated 85% cost reduction while maintaining 95% of GPT-4-level performance on widely-used benchmarks.
URL: https://github.com/lm-sys/RouteLLM

### 5.3 Model Registry

[FACT] Best practices for multi-model on-premises deployments include maintaining a registry of available models with their attributes (cost, latency, known strengths and weaknesses) that the router consults at request time; this registry must be updatable as models evolve without application code changes.
URL: https://www.gurustartups.com/reports/enterprise-llm-reference-architecture-for-multi-model-routing

[FACT] MLflow 3.0 extended its model registry to handle generative AI applications and AI agents, connecting models to exact code versions, prompt configurations, evaluation runs, and deployment metadata.
URL: https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025

**Practical implementation:** On-premises ISVs commonly implement a three-tier model portfolio: (1) a full-size frontier-equivalent model (70B+) for complex reasoning tasks, (2) a mid-size model (13B–34B) for standard query handling, and (3) a small model (7B or smaller) for classification, routing decisions, and high-volume low-complexity tasks. The gateway layer applies rules-based or ML-based routing (complexity scoring, PII detection, latency budget) to assign requests.

---

## 6. Model Lifecycle: Updates, A/B Testing, and Rollback

### 6.1 Deployment Patterns

On-premises environments lack the managed model endpoint abstractions available in cloud platforms (SageMaker, Vertex AI). ISVs must implement their own blue-green or canary deployment workflows.

[FACT] Cloud-native platforms like AWS SageMaker use blue-green deployments — spinning up a new model version (green) alongside the old (blue) and shifting traffic gradually, with automated monitors to trigger rollback to blue if anomalies occur. On-premises implementations must replicate this pattern manually using Kubernetes traffic splitting (Istio, NGINX, or Argo Rollouts).
URL: https://www.dynatrace.com/news/blog/the-rise-of-agentic-ai-part-6-introducing-ai-model-versioning-and-a-b-testing-for-smarter-llm-services/

[FACT] TrueFoundry is a Kubernetes-native platform for MLOps teams that provides GPU-optimized model serving, fine-tuning pipelines, and AI Gateway across AWS, GCP, Azure, on-premises, and air-gapped environments with consistent tooling.
URL: https://www.truefoundry.com/blog/on-prem-llms

### 6.2 Health Monitoring and Rollback Triggers

[FACT] vLLM health checks should execute actual inference on test prompts rather than simply verifying process status, to detect model-level degradation (e.g., corrupt quantized weights, KV cache corruption) that process-level checks would miss.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

[FACT] Rolling updates on Kubernetes should use Pod Disruption Budgets to ensure minimum replica survival during version transitions, maintaining availability during model swaps.
URL: https://introl.com/blog/vllm-production-deployment-inference-serving-architecture

**Recommended rollback triggers for on-premises model deployments:**
- P99 TTFT exceeds threshold (typically 2–3x baseline)
- Error rate on test prompt suite drops below quality threshold
- GPU OOM events per hour exceed baseline
- Token throughput drops below minimum SLA

### 6.3 A/B Testing Without Managed Endpoints

Without cloud-managed endpoints, A/B testing requires the gateway layer (LiteLLM, custom NGINX) to split a percentage of production traffic to the candidate model while the remainder continues to the incumbent. The registry must track which requests were routed to which model version to enable proper metric attribution.

[FACT] Sophisticated prompt management systems can handle A/B testing of different model and prompt versions, gradual rollouts of changes, and quick rollbacks when new configurations produce unexpected results.
URL: https://www.dynatrace.com/news/blog/the-rise-of-agentic-ai-part-6-introducing-ai-model-versioning-and-a-b-testing-for-smarter-llm-services/

---

## 7. Failover and Graceful Degradation

### 7.1 Health Checking Architecture

[FACT] LiteLLM provides four health monitoring endpoints: `/health/liveliness` (basic alive check), `/health/readiness` (verifies DB connectivity), `/health` (makes actual API calls to each configured model), and `/health/services` (integration health checks). Background health checks run at configurable intervals (default: 300 seconds).
URL: https://docs.litellm.ai/docs/proxy/health

[FACT] LiteLLM supports shared health check state across multiple proxy pods via Redis, preventing duplicate health check API calls in multi-replica gateway deployments on Kubernetes.
URL: https://docs.litellm.ai/docs/proxy/shared_health_check

### 7.2 Fallback and Graceful Degradation Patterns

[FACT] LiteLLM supports content-specific and general fallbacks across all configured model endpoints, with customizable retry policies for different exception types (rate limit, timeout, model error).
URL: https://docs.litellm.ai/docs/proxy/reliability

[FACT] Graceful degradation in self-hosted LLM pipelines means the application continues operating at reduced functionality — for example, routing complex reasoning requests to a smaller model when the primary large model endpoint is unavailable — rather than failing completely.
URL: https://latitude.so/blog/fault-tolerance-llm-pipelines-techniques/

**Failover priority chain (recommended pattern for on-premises ISV deployments):**

1. Primary: Full-size model endpoint (70B, FP16 or AWQ)
2. Fallback 1: Mid-size model endpoint (13B–34B, quantized)
3. Fallback 2: Small model endpoint (7B, GGUF or INT4)
4. Fallback 3: Cloud API endpoint (OpenAI, Anthropic) — requires network egress, used only when all on-premises endpoints fail
5. Terminal: Cached response or pre-computed fallback text

**Difficulty rating for failover implementation:**

| Failover Capability | Difficulty | Key Requirements |
|---------------------|------------|------------------|
| Basic process restart (systemd/K8s liveness probe) | 1/5 | Standard K8s configuration |
| Multi-model fallback via LiteLLM | 2/5 | LiteLLM proxy config; model priority ordering |
| Cross-instance health state via Redis | 3/5 | Redis deployment; shared health check configuration |
| Blue-green model version switching | 4/5 | Istio or Argo Rollouts; traffic splitting policy; metric-based rollback automation |
| Full graceful degradation with quality monitoring | 5/5 | Custom evaluation harness; automated routing policy updates; on-call runbook |

---

## 8. Cost Management and GPU Utilization

### 8.1 Economics

[FACT] On-premises infrastructure can provide LLM inferencing 2.9x to 4.1x more cost-effectively than API-based cloud services (65–75% cost reduction) for sustained, high-volume workloads.
URL: https://www.delltechnologies.com/asset/en-in/solutions/business-solutions/industry-market/esg-inferencing-on-premises-with-dell-technologies-analyst-paper.pdf

[FACT] Power, cooling, and maintenance costs for on-premises typically add 20–30% to operational hardware expenses.
URL: https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis

[FACT] All-in self-hosted inference cost, including hardware amortization over a 2-year lifespan, is approximately $0.02–$0.09 per million tokens depending on GPU tier and utilization.
URL: https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide

**Break-even analysis by model size (from academic cost-benefit study, September 2025):**

[STATISTIC] Small models (30–32B parameters): Break-even versus commercial APIs ranges from 0.3–3 months on approximately $2,000 hardware (single RTX 5090 class GPU), with $13.20/month electricity cost.
URL: https://arxiv.org/html/2509.18101v1
Date: September 2025

[STATISTIC] Medium models (70–120B parameters): Break-even ranges from 2.3–34 months on $15,000–$30,000 hardware (dual A100 GPUs), with $7.92–$15.84/month electricity.
URL: https://arxiv.org/html/2509.18101v1
Date: September 2025

[STATISTIC] Large models (235B–1T parameters): Break-even ranges from 4.3–69+ months on $60,000–$240,000 hardware (4–16 A100 GPUs), viable primarily at workloads exceeding 50M tokens/month.
URL: https://arxiv.org/html/2509.18101v1
Date: September 2025

### 8.2 GPU Utilization Monitoring

[FACT] GPU metrics are collected via NVIDIA DCGM and DCGM-Exporter, which exposes power draw, SM utilization, memory bandwidth, and temperature through a Prometheus-compatible endpoint.
URL: https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/

[FACT] Continuous batching maintains 85–92% GPU utilization under high concurrency, compared to approximately 40% with static batching.
URL: https://arxiv.org/html/2511.17593v1
Date: November 2025

### 8.3 Batch vs. Real-Time Inference Trade-offs

[FACT] Speculative decoding accelerates real-time inference by 2–3x without additional hardware, using small draft models to generate token candidates that large models verify in parallel.
URL: https://introl.com/blog/cost-per-token-llm-inference-optimization

[FACT] Dynamic batching maximizes hardware utilization by combining requests with varying lengths; inflight batching is particularly effective for autoregressive inference, allowing sequences at various stages to be processed within the same batch.
URL: https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/

**Decision rule:** For ISV SaaS applications with primarily synchronous user-facing inference (chat, copilot), optimize for TTFT and P99 latency using continuous batching and speculative decoding. For background document processing, ETL, or batch evaluation workloads, disable speculative decoding and maximize batch size to maximize token throughput per GPU-hour.

---

## 9. Staffing and Operational Profile

### 9.1 Required Skill Sets

[FACT] Operating a production-grade on-premises LLM inference stack requires "specialized skills across DevOps, InferenceOps and MLOps," with such expertise being "hard to hire and often more expensive than general engineering talent."
URL: https://bentoml.com/llm/infrastructure-and-operations/on-prem-llms

[FACT] On-premises LLM teams must own autoscaling, system upgrades, monitoring, and GPU procurement directly, as opposed to cloud deployments where the provider manages the control plane.
URL: https://bentoml.com/llm/infrastructure-and-operations/on-prem-llms

### 9.2 FTE Estimates

**Assumptions:** Mid-size ISV serving 50 enterprise customers, 2–4 model endpoints, one production GPU cluster (4–8 GPUs), no dedicated ML platform team.

| Role Domain | Active FTE | On-Call Burden | Notes |
|-------------|------------|----------------|-------|
| Inference infrastructure (vLLM/TGI ops, K8s, GPU monitoring) | 0.75–1.0 | 0.25 FTE equivalent | Covers deployment, scaling, health checks, patching |
| Model lifecycle (quantization, version management, A/B testing) | 0.5–0.75 | 0.1 FTE equivalent | Requires ML engineering background |
| Gateway and routing (LiteLLM/RouteLLM, failover config) | 0.25–0.5 | 0.1 FTE equivalent | Can overlap with platform engineering |
| Observability and cost optimization (DCGM, Prometheus, Grafana) | 0.25–0.5 | — | Can overlap with existing SRE function |
| Security and compliance (network isolation, audit logging) | 0.25 | — | See F39 and F4 for full coverage |
| **Total** | **2.0–3.0 FTE** | **+0.45 FTE on-call** | Assumes no managed ML platform |

[UNVERIFIED] The 2.0–3.0 FTE range is a synthesis from operational descriptions in BentoML's LLM Infrastructure Handbook, Latitude's cost analysis, and the academic cost-benefit paper (arxiv 2509.18101), none of which publish explicit FTE ranges. No 2025 Gartner or Forrester report with specific FTE benchmarks for on-premises LLM inference staffing was located.

---

## Consolidated Operational Difficulty Summary

| Capability Domain | On-Premises Difficulty | Key Operational Requirements | Representative Tools |
|-------------------|------------------------|------------------------------|----------------------|
| Serving framework deployment | 3/5 | Linux, CUDA, Docker/K8s, GPU driver management | vLLM, TGI, Dynamo-Triton |
| GPU procurement and allocation | 4/5 | 9–12 month lead times; MIG configuration; NVLink/InfiniBand | NVIDIA MIG, DCGM |
| Quantization management | 3/5 | Model format selection; calibration dataset; hardware validation | AWQ, GPTQ, GGUF toolchains |
| Flash Attention / advanced kernels | 3/5 | H100-specific; CUDA version pinning | FlashAttention-3, vLLM backends |
| Multi-model routing | 3/5 | Gateway config; model registry; traffic split policies | LiteLLM, RouteLLM, Istio |
| Model lifecycle (update/rollback) | 4/5 | Blue-green K8s deployments; evaluation harness; automated rollback triggers | MLflow, Argo Rollouts |
| Failover and graceful degradation | 4/5 | Multi-tier fallback config; Redis health state; runbooks | LiteLLM fallbacks, K8s PDB |
| GPU utilization and cost optimization | 3/5 | DCGM metrics; Prometheus; batch policy tuning | DCGM-Exporter, Grafana |

---

## Key Takeaways

- **vLLM is the production default** for on-premises multi-user LLM inference, achieving 85–92% GPU utilization under high concurrency and 24x throughput advantage over TGI under extreme load; TGI v3 is preferred for latency-sensitive single-user interactive workloads with 200K+ token contexts.

- **Quantization is operationally necessary at scale**: AWQ 4-bit delivers under 1% accuracy loss on NVIDIA GPU hardware and reduces VRAM requirements by approximately 50%, making 70B-parameter models deployable on single H100 80GB or H200 GPUs without meaningful quality degradation.

- **GPU procurement is a long-lead strategic constraint**: Standard H100 enterprise orders carry 9–12 month lead times; ISVs planning on-premises LLM capacity must commit to hardware procurement one to two planning cycles ahead of application demand, or accept L40S or H200 alternatives with shorter lead times.

- **The gateway layer is the operational linchpin**: LiteLLM or an equivalent multi-model gateway is required to manage health checking, fallback routing, model version A/B testing, and graceful degradation — without it, multi-model on-premises deployments are operationally fragile and require bespoke application-layer failover logic.

- **Total operational staffing is 2.0–3.5 FTE** for a mid-size production on-premises LLM stack: this is a persistent, ongoing cost (not a one-time setup cost) that covers inference infrastructure, model lifecycle, gateway operations, and observability — and the specialized skills required command salary premiums relative to general software engineering roles.

---

## Related — Out of Scope

The following topics were encountered during research but are explicitly outside this agent's scope boundary:

- **GPU hardware infrastructure** (data center power, cooling, rack density, networking hardware selection): See [F39: On-Prem GPU Hardware Infrastructure] for detailed coverage of physical infrastructure requirements.
- **Model selection and architecture trade-offs** (choosing between Llama 3.3, Mistral, Qwen, etc.): See [F5: LLM Model Selection] for detailed coverage of model architecture decisions.
- **RAG pipeline integration** (how inference endpoints connect to vector databases and retrieval layers): See [F35: RAG Pipeline Operations] for detailed coverage of retrieval-augmented generation operational patterns.
- **Security hardening for on-premises AI workloads** (network isolation, model weight encryption, audit logging): See [F4: Security Risk and Compliance] for detailed coverage.

---

## Sources

1. vLLM 2024 Retrospective and 2025 Vision — https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html
2. vLLM Production Stack Release — https://blog.vllm.ai/2025/01/21/stack-release.html
3. vLLM Production Deployment Architecture — https://introl.com/blog/vllm-production-deployment-inference-serving-architecture
4. vLLM Optimization and Tuning Documentation — https://docs.vllm.ai/en/stable/configuration/optimization/
5. vLLM Speculative Decoding Documentation — https://docs.vllm.ai/en/latest/features/spec_decode/
6. vLLM Production Stack Multi-Model Tutorial — https://blog.vllm.ai/production-stack/tutorials/04-launch-multiple-model.html
7. vLLM Production Stack Documentation — https://docs.vllm.ai/en/stable/deployment/integrations/production-stack/
8. Comparative Analysis of vLLM and HuggingFace TGI (arXiv 2511.17593) — https://arxiv.org/abs/2511.17593
9. vLLM vs TGI vs TensorRT-LLM vs Ollama (Hivenet) — https://compute.hivenet.com/post/vllm-vs-tgi-vs-tensorrt-llm-vs-ollama
10. vLLM vs TGI Comparison (Inferless) — https://www.inferless.com/learn/vllm-vs-tgi-the-ultimate-comparison-for-speed-scalability-and-llm-performance
11. Ollama vs vLLM: How to Choose (Red Hat Developer) — https://developers.redhat.com/articles/2025/07/08/ollama-or-vllm-how-choose-right-llm-serving-tool-your-use-case
12. Is Ollama Ready for Production? (Collabnix) — https://collabnix.com/is-ollama-ready-for-production/
13. NVIDIA Dynamo-Triton — https://developer.nvidia.com/dynamo-triton
14. NVIDIA Triton Inference Server Documentation — https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html
15. NVIDIA Dynamo-Triton Product Page — https://www.nvidia.com/en-us/ai/dynamo-triton/
16. FlashAttention-3 Blog (Together AI) — https://www.together.ai/blog/flashattention-3
17. FlashAttention-3 PyTorch Blog — https://pytorch.org/blog/flashattention-3/
18. AWQ vs GPTQ vs GGUF Quantization Comparison 2025 — https://localaimaster.com/blog/quantization-explained
19. GGUF, GPTQ, AWQ — Which Quantization Method? (E2E Networks) — https://www.e2enetworks.com/blog/which-quantization-method-is-best-for-you-gguf-gptq-or-awq
20. LLMs on CPU: GGUF, AWQ, GPTQ (Ionio AI) — https://www.ionio.ai/blog/llms-on-cpu-the-power-of-quantization-with-gguf-awq-gptq
21. H100 Availability Crisis (Uvation) — https://uvation.com/articles/h100-availability-the-silent-crisis-threatening-enterprise-ai-plans
22. NVIDIA H100 GPU Pricing 2025 (GMI Cloud) — https://www.gmicloud.ai/blog/2025-cost-of-renting-or-uying-nvidia-h100-gpus-for-data-centers
23. H100 GPU Pricing: Cloud vs. On-Premise (GMI Cloud) — https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis
24. LLM Inference Hardware Enterprise Guide (IntuitionLabs) — https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide
25. GPU MIG for Kubernetes (CAST AI) — https://docs.cast.ai/docs/gpu-sharing-mig
26. MIG: Making the Most of GPUs Part 2 (Red Hat) — https://www.redhat.com/en/blog/sharing-caring-how-make-most-your-gpus-part-2-multi-instance-gpu
27. Cost-Benefit Analysis of On-Premises LLM Deployment (arXiv 2509.18101) — https://arxiv.org/html/2509.18101v1
28. On-Prem LLM Deployments — BentoML LLM Handbook — https://bentoml.com/llm/infrastructure-and-operations/on-prem-llms
29. Dell Technologies ESG On-Premises Inferencing Analyst Paper — https://www.delltechnologies.com/asset/en-in/solutions/business-solutions/industry-market/esg-inferencing-on-premises-with-dell-technologies-analyst-paper.pdf
30. LLM Inference Optimization (NVIDIA Technical Blog) — https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/
31. Enterprise LLM Reference Architecture for Multi-Model Routing (Guru Startups) — https://www.gurustartups.com/reports/enterprise-llm-reference-architecture-for-multi-model-routing
32. RouteLLM Framework (LMSYS) — https://github.com/lm-sys/RouteLLM
33. LiteLLM GitHub — https://github.com/BerriAI/litellm
34. LiteLLM Health Checks Documentation — https://docs.litellm.ai/docs/proxy/health
35. LiteLLM Shared Health Check Documentation — https://docs.litellm.ai/docs/proxy/shared_health_check
36. LiteLLM Fallbacks and Reliability Documentation — https://docs.litellm.ai/docs/proxy/reliability
37. Fault Tolerance in LLM Pipelines (Latitude) — https://latitude.so/blog/fault-tolerance-llm-pipelines-techniques/
38. AI Model Versioning and A/B Testing (Dynatrace) — https://www.dynatrace.com/news/blog/the-rise-of-agentic-ai-part-6-introducing-ai-model-versioning-and-a-b-testing-for-smarter-llm-services/
39. Model Versioning Infrastructure (Introl) — https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025
40. TrueFoundry On-Prem LLMs — https://www.truefoundry.com/blog/on-prem-llms
41. Cost Per Token Analysis (Introl) — https://introl.com/blog/cost-per-token-llm-inference-optimization
42. KV Caching with vLLM, LMCache, and Ceph — https://ceph.io/en/news/blog/2025/vllm-kv-caching/
