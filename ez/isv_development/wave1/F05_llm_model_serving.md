# F05: LLM Model Serving & Inference Infrastructure

**Research Question:** What infrastructure is required to serve large language models for inference in production applications, and what are the operational demands of maintaining model serving at scale?

**Scope:** Model serving architecture, capabilities, and cost economics for ISVs evaluating on-premises, managed Kubernetes, and cloud-native deployment models.

---

## Executive Summary

Serving large language models in production requires a fundamentally different infrastructure posture than traditional software. Two structural choices dominate: self-hosting an open-weight model on GPU infrastructure (high upfront cost, maximum control, significant operational burden) or consuming a managed API endpoint from a hyperscaler or frontier lab (pay-per-token, zero infrastructure, but vendor dependency and data-egress concerns). As of 2025, GPU cloud pricing has declined sharply — H100 instances are available for $1.49–$3.90/hour at specialist providers versus $6.98/hour on Azure — while API pricing for equivalent frontier-model performance has dropped 50x since 2022, fundamentally shifting the break-even calculus. Optimization techniques including 4-bit quantization, continuous batching, and speculative decoding can reduce effective inference costs by up to 16x when combined, making self-hosted open-weight models economically viable at moderate scale. Multi-model routing, where simpler queries route to cheaper models and complex queries to frontier models, has demonstrated 85% cost reduction while maintaining 95% of frontier-model performance quality in peer-reviewed research. ISVs must choose their serving architecture with full awareness of the operational profile each model imposes: cloud-native API consumption is trivial to operate but creates vendor and cost exposure, while self-hosted GPU serving is among the most operationally demanding infrastructure tasks in modern software engineering.

---

## 1. Model Hosting Options: Self-Hosted vs Managed API Endpoints

### 1.1 Self-Hosted Inference Runtimes

Three open-source runtimes dominate production self-hosted deployments:

**vLLM**

[vLLM](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html) is the most widely adopted open-source LLM inference engine, implementing two foundational innovations: PagedAttention (a memory management system using a free block queue of KV-cache blocks, with each block storing 16 tokens per layer by default) and continuous batching (mixing prefill and decode requests in the same execution step).

[STATISTIC] vLLM achieves 14–24x higher throughput than Hugging Face Transformers and 2.2–3.5x higher throughput than early TGI for LLaMA models on NVIDIA GPUs.
— [Comparative Analysis of LLM Inference Serving Systems, arXiv 2511.17593](https://arxiv.org/html/2511.17593v1)

vLLM supports tensor parallelism, pipeline parallelism, data parallelism, and expert parallelism (for MoE models). The recommended configuration for multi-node deployments is: [tensor parallel size = number of GPUs per node] × [pipeline parallel size = number of nodes]. For example, 16 GPUs across 2 nodes uses tensor parallel size 8 and pipeline parallel size 2. [Source: [vLLM Distributed Inference Docs](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/)]

vLLM V1 implements speculative decoding via n-gram, EAGLE, and Medusa draft methods, enabling "up to k+1 tokens" per large-model pass through acceptance-rejection sampling. Prefix caching reuses KV blocks from previously computed shared prompt prefixes, avoiding recomputation across requests with common beginnings. [Source: [Inside vLLM: Anatomy of a High-Throughput LLM Inference System](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html)]

**Text Generation Inference (TGI)**

[STATISTIC] TGI v3 processes approximately 3x more tokens and is up to 13x faster than vLLM on long-prompt workloads (200,000+ token contexts) when prefix caching is enabled.
— [Comparing the Top 6 Inference Runtimes for LLM Serving in 2025, MarkTechPost](https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/)

TGI v3's long prompt pipeline and prefix caching make it the preferred engine for conversation-heavy, long-context workloads. A specific benchmark showed: a conversation reply that takes 27.5 seconds in vLLM can be served in approximately 2 seconds in TGI v3 — a 13x speedup on that workload type. [Source: [MarkTechPost Inference Runtime Comparison 2025](https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/)]

**NVIDIA Triton Inference Server**

Triton is a general-purpose model serving framework that uses vLLM as a backend for LLM workloads. vLLM was integrated into Triton starting with the 23.10 release. Triton adds enterprise-grade features: multi-model serving from a single GPU, model ensemble pipelines, and production-grade health checking. [Source: [vLLM vs Triton: Competing or Complementary, Bizety](https://bizety.com/2025/09/29/vllm-vs-triton-competing-or-complementary/)]

**LMDeploy**

[STATISTIC] LMDeploy delivers up to 1.8x higher request throughput than vLLM through persistent batching and optimized kernels, and can reach higher tokens-per-second than vLLM under comparable latency constraints at high concurrency.
— [Comparing the Top 6 Inference Runtimes for LLM Serving in 2025, MarkTechPost](https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/)

**TensorRT-LLM**

NVIDIA's TensorRT-LLM provides the highest throughput on NVIDIA hardware via compiled CUDA kernels but requires model-specific compilation and is hardware-tied (NVIDIA only). Many production teams use TensorRT-LLM for high-volume proprietary chat endpoints while using vLLM or TGI for experimental or open-model workloads. [Source: [vLLM vs TensorRT-LLM: Deep Technical Comparison, MarkTechPost](https://www.marktechpost.com/2025/11/19/vllm-vs-tensorrt-llm-vs-hf-tgi-vs-lmdeploy-a-deep-technical-comparison-for-production-llm-inference/)]

### 1.2 Managed API Endpoints

| Provider | Key Models | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
|---|---|---|---|
| Anthropic Claude API | Claude Haiku 4.5 | $1.00 | $5.00 |
| Anthropic Claude API | Claude Sonnet 4.5 | $3.00 | $15.00 |
| Anthropic Claude API | Claude Opus 4.5 | $5.00 | $25.00 |
| OpenAI | GPT-4o | $5.00 | $20.00 |
| OpenAI | GPT-4o mini | $0.60 | $2.40 |
| Google Vertex AI | Gemini (mid-tier) | $1.25 | $10.00 |
| Introl/Market (Dec 2025) | Gemini Flash-Lite | $0.075 | $0.30 |
| Introl/Market (Dec 2025) | DeepSeek R1 | $0.55 | $2.19 |
| Introl/Market (Dec 2025) | Claude Opus 4 | $15.00 | $75.00 |

Sources: [Anthropic Pricing Docs](https://platform.claude.com/docs/en/about-claude/pricing) | [IntuitionLabs LLM API Pricing Comparison 2025](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025) | [Introl Inference Unit Economics Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide) | [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)

[FACT] AWS implemented a 44% price reduction on H100 instances in June 2025.
— [IntuitionLabs H100 Rental Prices Cloud Comparison](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)

[FACT] Equivalent GPT-4 performance now costs $0.40/million tokens versus $20 in late 2022 — a 50x cost reduction in approximately three years.
— [Introl Inference Unit Economics Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)

[FACT] Claude 4.5 prompt caching enables up to 90% savings on repeated context; the Claude batch API provides a 50% discount.
— [Anthropic Claude API Pricing Docs](https://platform.claude.com/docs/en/about-claude/pricing)

---

## 2. GPU Infrastructure Requirements

### 2.1 GPU Type Specifications

| GPU | VRAM | Architecture | Key Use Case |
|---|---|---|---|
| NVIDIA H100 | 80 GB HBM3 | Hopper | Largest frontier models, highest throughput |
| NVIDIA A100 | 80 GB HBM2e | Ampere | Large production models, strong ecosystem |
| NVIDIA L40S | 48 GB GDDR6 | Ada Lovelace | Cost-efficient inference for mid-size models |
| NVIDIA RTX 4090 | 24 GB GDDR6X | Ada Lovelace | Small models (≤7B), developer workstations |

Source: [WhiteFiber Best GPUs for LLM Inference 2025](https://www.whitefiber.com/compare/best-gpus-for-llm-inference-in-2025) | [RunPod GPU Comparison: H100, A100, L40S](https://www.runpod.io/articles/comparison/choosing-gpus)

[STATISTIC] The H100 offers up to 30x better inference and 9x better training performance compared to the A100.
— [RunPod GPU Comparison Guide](https://www.runpod.io/articles/comparison/choosing-gpus)

### 2.2 VRAM Requirements by Model Size

The baseline formula for VRAM estimation at FP16 precision is: **VRAM = (Parameters × 2 bytes) × 1.2** (adding 20% overhead for activations and KV-cache). [Source: [Hyperstack: How Much VRAM Do You Need for LLMs](https://www.hyperstack.cloud/blog/case-study/how-much-vram-do-you-need-for-llms)]

Precision conversions:
- FP32: 4 bytes per parameter
- FP16 / BF16: 2 bytes per parameter
- Int8: 1 byte per parameter
- Int4: 0.5 bytes per parameter

| Model Size | FP16 VRAM (est.) | Int4 VRAM (est.) | Minimum GPU Config |
|---|---|---|---|
| 7B | ~17 GB | ~5 GB | 1x RTX 4090 (Int4) or 1x L40S |
| 13B | ~31 GB | ~8 GB | 1x L40S (FP16) or 1x RTX 4090 (Int4) |
| 34B | ~82 GB | ~21 GB | 2x A100 80GB (FP16) or 1x A100 (Int4) |
| 70B | ~168 GB | ~42 GB | 2–4x A100/H100 (FP16) or 1x H100 (Int4) |
| 405B+ | ~900 GB+ | ~225 GB | 8–16x H100 (Int4 minimum) |

Source: [Hyperstack VRAM Guide](https://www.hyperstack.cloud/blog/case-study/how-much-vram-do-you-need-for-llms) | [BentoML LLM Inference Handbook: Choosing the Right GPU](https://bentoml.com/llm/getting-started/choosing-the-right-gpu)

[FACT] For a Llama 70B model loaded in 16-bit format: 70B × 2 bytes × 1.2 = 168 GB VRAM required.
— [Hyperstack: How Much VRAM Do You Need for LLMs](https://www.hyperstack.cloud/blog/case-study/how-much-vram-do-you-need-for-llms)

[FACT] Normal fine-tuning typically demands 3 to 4 times more memory than inference at the same precision level.
— [Hyperstack: How Much VRAM Do You Need for LLMs](https://www.hyperstack.cloud/blog/case-study/how-much-vram-do-you-need-for-llms)

### 2.3 Multi-GPU Serving Configuration

vLLM multi-GPU serving recommendations from official documentation:
- **Within a node**: Prefer tensor parallelism (requires fast NVLink interconnect)
- **Across nodes**: Use pipeline parallelism (tolerates slower InfiniBand interconnect)
- **MoE models**: Expert parallelism (EP) acts as a modifier flag on top of TP or DP
- Multi-node inference requires Ray; single-node can use Python native multiprocessing

[Source: [vLLM Parallelism and Scaling Docs](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/)]

---

## 3. Optimization Techniques

### 3.1 Quantization (GPTQ, AWQ, GGUF)

Quantization reduces model weights from FP16 to lower-bit representations, reducing VRAM footprint and often increasing throughput.

[STATISTIC] All 4-bit quantization formats achieve approximately 75% file size reduction versus FP16.
— [LocalAIMaster: AWQ vs GPTQ vs GGUF Quantization Comparison 2025](https://localaimaster.com/blog/quantization-explained)

**Accuracy Retention at 4-bit:**

| Method | Accuracy Retention | Median Absolute Error | Llama 3.1 8B Quality Loss vs FP16 |
|---|---|---|---|
| AWQ 4-bit | 95% | 0.036 | -0.7% |
| GGUF Q4_K_M | 92% | 0.041 | -1.6% |
| GPTQ 4-bit | 90% | 0.049 | -2.8% |

Source: [LocalAIMaster Quantization Comparison](https://localaimaster.com/blog/quantization-explained) | [Jarvislabs vLLM Quantization Benchmarks](https://docs.jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks)

**Throughput at 4-bit (with optimized kernels):**
- Marlin-AWQ: 741 tokens/second output throughput
- Marlin-GPTQ: 712 tokens/second output throughput
- AWQ without Marlin kernel: 67 tokens/second (10.9x slower than with the Marlin kernel)

[Source: [Jarvislabs vLLM Quantization Complete Guide with Benchmarks](https://docs.jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks)]

**Hardware-appropriate quantization selection:**
- 8 GB laptops / CPU inference: GGUF Q4_K_S (via llama.cpp/Ollama)
- Linux CUDA inference servers (RTX 3060/3070): GPTQ 4-bit
- High-performance GPU serving (RTX 4070–4090, A100, H100): AWQ 4-bit with Marlin kernel
- Apple Silicon: GGUF Q4_K_M with Metal backend

[Source: [LocalAIMaster Quantization Comparison](https://localaimaster.com/blog/quantization-explained)]

[FACT] Both the 4-bit GPTQ version and 5-bit GGUF (Q5_K_M) fully retained 0.99 accuracy in a specific code-generation benchmark, but 4-bit GGUF (Q4_K_M) dropped to 0.89 — demonstrating that bit-width choices significantly impact accuracy.
— [Jarvislabs vLLM Quantization Complete Guide](https://docs.jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks)

### 3.2 KV-Cache Optimization and Continuous Batching

vLLM's PagedAttention stores KV-cache in non-contiguous blocks (default: 16 tokens per layer), with block tables mapping logical to physical memory — enabling near-zero memory waste compared to static allocation. Prefix caching reuses computed KV blocks for requests sharing common prompt prefixes, eliminating redundant computation. [Source: [Inside vLLM: Anatomy of a High-Throughput Inference System](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html)]

Continuous batching mixes prefill (compute-bound, processing all prompt tokens) and decode (memory-bandwidth-bound, single token per step) requests in the same execution step, achieving significantly higher GPU utilization than static batching. [Source: [Inside vLLM: Anatomy of a High-Throughput Inference System](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html)]

### 3.3 Speculative Decoding

Speculative decoding uses a small draft model to predict multiple tokens ahead; the large model then verifies or rejects them in a single pass. vLLM V1 supports n-gram, EAGLE, and Medusa draft methods.

[STATISTIC] Speculative decoding achieves 2–3x latency reduction.
— [Introl Inference Unit Economics Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)

[FACT] FlashInfer (a kernel optimization library compatible with vLLM) reduced inter-token latency by 29–69% in measured benchmarks.
— [SWFTE: Intelligent LLM Routing Multi-Model AI](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)

### 3.4 Combined Optimization Impact

[STATISTIC] The combination of quantization (4-8x model size reduction), continuous batching (2x improvement), and speculative decoding (2–3x latency reduction) yields a potential 16x effective cost reduction in total.
— [Introl Inference Unit Economics Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)

---

## 4. Latency Management

### 4.1 Key Latency Metrics

| Metric | Full Name | Definition |
|---|---|---|
| TTFT | Time to First Token | Submission-to-first-token latency (includes queue + prefill + network) |
| ITL | Inter-Token Latency | Time between consecutive output tokens |
| TPOT | Time Per Output Token | Average ITL across all output tokens |
| Goodput | Goodput | Throughput meeting defined SLO bounds (e.g., max TTFT threshold) |

Source: [Anyscale LLM Serving Metrics Docs](https://docs.anyscale.com/llm/serving/benchmarking/metrics) | [NVIDIA NIM LLM Benchmarking Metrics](https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html)

### 4.2 Prefill vs. Decode Characteristics

From vLLM's official architecture documentation:
- **Prefill phase**: "compute-bound" — processes all prompt tokens in parallel; latency scales with prompt length
- **Decode phase**: "memory-bandwidth-bound" — generates one token per step; latency is nearly flat below saturation batch size (B_sat); grows roughly linearly with batch size beyond B_sat

[Source: [Inside vLLM: Anatomy of a High-Throughput Inference System](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html)]

### 4.3 Streaming Responses

Streaming token delivery (server-sent events) masks TTFT from the user experience — the perceptible latency becomes time-to-first-visible-token rather than time-to-complete-response. All major serving runtimes (vLLM, TGI, Triton) and all major managed APIs (OpenAI, Anthropic, Bedrock, Vertex AI) support streaming. [Source: [BentoML LLM Inference Handbook: Metrics](https://bentoml.com/llm/inference-optimization/llm-inference-metrics)]

[FACT] The CHWBL load-balancing algorithm achieved a 95% reduction in Time-To-First-Token versus Kubernetes default load balancing.
— [SWFTE: Intelligent LLM Routing Multi-Model AI](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)

---

## 5. Model Versioning and A/B Testing

### 5.1 Serving Multiple Model Versions

Production model serving requires simultaneous operation of multiple model versions to support:
- Canary rollouts (gradual traffic migration to new versions)
- A/B testing (comparing model performance on live traffic)
- Rollback capability (reverting on quality regression)
- Parallel development environments

Traffic splitting allows configuring the percentage of traffic each model version receives. Header-based traffic redirection enables routing test prompts with specific HTTP headers to newer model variants without affecting production traffic. [Source: [TrueFoundry: Multi-Model Routing](https://www.truefoundry.com/blog/multi-model-routing)]

### 5.2 Observability for A/B Testing

[FACT] Dynatrace introduced AI Model Versioning and A/B testing features in September 2025, enabling built-in comparison across models (GPT-5, Claude, Vertex AI, Azure AI Foundry) using metrics including response time, token consumption, cost, and relevancy.
— [Dynatrace: AI Model Versioning and A/B Testing](https://www.dynatrace.com/news/blog/the-rise-of-agentic-ai-part-6-introducing-ai-model-versioning-and-a-b-testing-for-smarter-llm-services/)

[FACT] Production model versioning strategies must support: multiple model versions simultaneously, gradual traffic migration, and rollback capabilities using semantic versioning for models and maintaining backward-compatible APIs.
— [Dynatrace Docs: AI Model Versioning and A/B Testing](https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/ab-model-testing)

---

## 6. Cost Economics

### 6.1 GPU Hardware and Cloud Rental Costs

**Hardware Purchase (amortized over 3 years):**
- NVIDIA H100 GPU (single card): $25,000–$40,000
- Complete 8×H100 server system: $200,000–$400,000

[Source: [IntuitionLabs NVIDIA AI GPU Pricing Guide](https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide) | [Introl Inference Unit Economics Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)]

**Cloud H100 Rental (on-demand, per GPU-hour, November 2025):**

| Provider | H100 80GB $/hr | Notes |
|---|---|---|
| Vast.ai (marketplace) | $1.49–$1.87 | Spot/marketplace pricing |
| Cudo Compute | $1.80 | Specialist cloud |
| RunPod (community) | $1.99 | Per-minute billing |
| Lambda Labs | $2.99 | Reserved capacity from $1.85–$1.90 |
| AWS EC2 (P5) | $3.90 | Post-44% price cut June 2025 |
| Google Cloud (A3-high) | $3.00 | Committed use available |
| CoreWeave | $6.16 | Enterprise SLA |
| Microsoft Azure (NC H100 v5) | $6.98 | Enterprise SLA |

Source: [IntuitionLabs H100 Rental Prices Cloud Comparison](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison) | [RunPod Pricing](https://www.runpod.io/pricing) | [Lambda AI Pricing](https://lambda.ai/pricing)

[FACT] A100 GPUs are now sub-$1/GPU-hour in the open market as newer chips have dominated supply.
— [IntuitionLabs H100 Rental Prices Cloud Comparison](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)

[FACT] Infrastructure management overhead adds approximately $2–$7/hour to raw GPU rental, bringing true operational costs to $8–$15/hour for 8×H100 systems.
— [Introl Inference Unit Economics Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)

### 6.2 Self-Hosted vs. API Break-Even Analysis

[STATISTIC] Self-hosted open models save 60–70% versus OpenAI API at sufficient utilization.
— [SkyWork AI: LLM Cost Comparison 2025](https://skywork.ai/skypage/en/LLM-Cost-Comparison-2025-A-Deep-Dive-into-Managing-Your-AI-Budget/1975592241004736512)

Break-even utilization thresholds:
- 7B models: require approximately **50% GPU utilization** to cost less than GPT-3.5 Turbo API
- 13B models: achieve cost parity with GPT-4 Turbo API at only **10% GPU utilization**
- Minimum viable scale: **more than 8,000 conversations per day** for self-hosted infrastructure to undercut managed API solutions

[Source: [Introl Inference Unit Economics Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)]

[STATISTIC] A minimal internal self-hosted deployment can easily cost $125,000–$190,000 per year in total cost of ownership.
— [SkyWork AI: LLM Cost Comparison 2025](https://skywork.ai/skypage/en/LLM-Cost-Comparison-2025-A-Deep-Dive-into-Managing-Your-AI-Budget/1975592241004736512)

### 6.3 Staffing Costs (FTE Estimation Framework)

Assumptions: Mid-size deployment serving 50 enterprise customers; single region; one serving cluster of 4–8 GPUs.

| Deployment Model | Initial Engineering | Ongoing Operations | On-Call Burden |
|---|---|---|---|
| On-premises (self-hosted GPU cluster) | 2–4 FTE for 3–6 months | 1.0–1.25 FTE | 0.25–0.5 FTE |
| Managed Kubernetes (EKS/AKS/GKE + self-hosted runtime) | 1–2 FTE for 2–3 months | 0.5–0.75 FTE | 0.1–0.25 FTE |
| Cloud-native (managed API only) | 0.25 FTE for 1–2 weeks | 0.1–0.25 FTE | Minimal |

Source: [Azumo: Self-Hosting LLMs Hidden Costs](https://azumo.com/artificial-intelligence/ai-insights/self-hosting-llms-cost) | [Aimprosoft: Cost to Host Private LLM 2025](https://www.aimprosoft.com/blog/cost-to-host-private-llm-2025/)

[STATISTIC] Staff costs average $135,000/year for MLOps engineers; compliance overhead adds 5–15% for regulated industries. Initial deployment phases require 2–4 full-time engineers for 3–6 months, at a loaded cost of $200,000–$300,000.
— [Azumo: Self-Hosting LLMs Hidden Costs](https://azumo.com/artificial-intelligence/ai-insights/self-hosting-llms-cost)

---

## 7. Multi-Model Serving and Routing

### 7.1 Enterprise Adoption

[STATISTIC] 37% of enterprises use 5 or more models in production environments.
— [SWFTE: Intelligent LLM Routing Multi-Model AI](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)

[STATISTIC] IDC predicts 60% of enterprise applications will include multi-agent AI by 2026.
— [SWFTE: Intelligent LLM Routing Multi-Model AI](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)

[STATISTIC] Enterprise LLM spending reached $8.4 billion by mid-2025, up from $3.5 billion in late 2024.
— [SWFTE: Intelligent LLM Routing Multi-Model AI](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)

### 7.2 Routing Cost and Performance Impact

**RouteLLM** (published at ICLR 2025, UC Berkeley/Anyscale/Canva):

[STATISTIC] RouteLLM achieved cost reductions of over 85% on MT Bench, 45% on MMLU, and 35% on GSM8K compared to using only GPT-4, while still achieving 95% of GPT-4's performance.
— [RouteLLM: Learning to Route LLMs from Preference Data, ICLR 2025 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html)

[FACT] RouteLLM router models reduce costs by over 2x without substantially compromising quality, using human preference data and data augmentation to train routing models that generalize to LLM pairs not seen during training.
— [RouteLLM ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)

**General Routing Impact Ranges:**
- Routing simple queries to smaller models: 10–30% cost savings
- Comprehensive smart routing strategies: 30–80% cost reduction
- Amazon Bedrock demonstrated: up to 30% cost reduction without compromising accuracy; internal testing showed 60% cost savings
- Semantic caching reduces redundant API calls by up to 40%

[Source: [SWFTE: Intelligent LLM Routing Multi-Model AI](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)]

### 7.3 Production Multi-Model Deployments

Named organizations using multi-model routing in production: Atlassian (20+ models), Salesforce, Microsoft, Walmart, DoorDash, and Vodafone. [Source: [SWFTE: Intelligent LLM Routing Multi-Model AI](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)]

Routing strategies in production:
- **Latency-based routing**: Routes to fastest-responding endpoint
- **Cost-based routing**: Routes to cheapest endpoint that meets quality threshold
- **Quality-based routing**: Routes based on task complexity classification
- **Task-specific routing**: Routes to specialist models (e.g., code model for code tasks)

[Source: [AWS: Multi-LLM Routing Strategies for Generative AI Applications](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)]

---

## 8. Failover and Redundancy

### 8.1 Core Failover Strategies

Modern LLM gateways implement four core failover patterns:

1. **Error-based failover**: If the primary provider returns errors, requests automatically retry on a backup provider. Example: GPT-4o returns 503 → request instantly re-sent to Claude Sonnet.

2. **HTTP status code handling**: 429 (rate limit) triggers immediate rerouting to secondary provider; 500-level errors trigger cross-provider retries.

3. **Latency threshold failover**: Responses exceeding a configurable timeout (example: 2–3 seconds) trigger parallel requests to secondary providers; the first responder wins.

4. **Proactive load distribution**: Traffic splits across providers (example ratio: 70/30) reducing single-provider dependency.

[Source: [Portkey: Failover Routing Strategies for LLMs in Production](https://portkey.ai/blog/failover-routing-strategies-for-llms-in-production/)]

### 8.2 Uptime Reality

[FACT] Even "99.99% uptime" translates to approximately 52 minutes of downtime annually — sufficient to cause user-facing disruptions at scale.
— [Portkey: Failover Routing Strategies for LLMs in Production](https://portkey.ai/blog/failover-routing-strategies-for-llms-in-production/)

### 8.3 LLM Gateway Pattern

An LLM gateway (also called LLM proxy or AI control plane) sits between the application and model endpoints, providing:
- Adaptive load balancing across providers based on real-time latency, error rates, and throughput limits
- Multi-tier fallback chains for automatic switching between primary, secondary, and tertiary providers
- Health-aware routing with circuit breaking that removes failing providers
- Rate limit budget enforcement and cost governance

[Source: [Portkey: Retries, Fallbacks, and Circuit Breakers in LLM Apps](https://portkey.ai/blog/retries-fallbacks-and-circuit-breakers-in-llm-apps/) | [Maxim: Top 5 LLM Gateways in 2025](https://www.getmaxim.ai/articles/top-5-llm-gateways-in-2025-the-definitive-guide-for-production-ai-applications/)]

[FACT] DIY failover requires managing: diverse error formats across providers, normalized authentication, timeout handling, rate-limit variance, and observability infrastructure — typically necessitating custom wrapper code that becomes operationally fragile at scale.
— [Portkey: Failover Routing Strategies for LLMs in Production](https://portkey.ai/blog/failover-routing-strategies-for-llms-in-production/)

### 8.4 Achieving Zero-Downtime

[FACT] Achieving zero-downtime for LLM-powered applications requires: multi-provider load balancing, intelligent caching, automated health checks, proactive failover, and tight observability.
— [Requesty: Implementing Zero-Downtime LLM Architecture](https://www.requesty.ai/blog/implementing-zero-downtime-llm-architecture-beyond-basic-fallbacks)

---

## 9. Deployment Model Comparison

| Capability | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Model Hosting** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Self-hosted runtime (vLLM/TGI/Triton); customer GPU procurement | vLLM/TGI on EKS/AKS/GKE node pools; ISV manages runtime | OpenAI, Anthropic, Bedrock, Vertex AI API calls |
| | vLLM, TGI, TensorRT-LLM | vLLM on Kubernetes, Ray Serve | OpenAI API, Anthropic API, AWS Bedrock |
| | Est. FTE: 1.0–1.25 (ops) + 0.5 (on-call) | Est. FTE: 0.5–0.75 (ops) + 0.25 (on-call) | Est. FTE: 0.1–0.25 |
| **GPU Infrastructure** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Physical GPU procurement, CUDA driver management, cooling/power | GPU node groups via managed K8s; cloud manages hardware | Provider manages all GPU infrastructure |
| | On-premises H100/A100 clusters | EKS GPU node groups, AKS NDm A100 v4, GKE A3 | Abstracted — no GPU management |
| | Est. FTE: 0.5–1.0 (infra) | Est. FTE: 0.25–0.5 (infra) | Est. FTE: 0 |
| **Optimization (Quantization, Batching)** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Full control; requires MLOps expertise to configure and maintain | Runtime-level configuration; cloud autoscaling for throughput | Managed by provider; limited user control |
| | AWQ/GPTQ/GGUF selection, kernel tuning, batch size tuning | Runtime flags in Kubernetes deployments | Prompt caching, batch API toggles |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05 |
| **Latency Management** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Network routing fully controlled; tuning required for TTFT SLOs | K8s ingress + HPA for autoscaling; regional deployment | Provider SLA-based; rate limits apply |
| | Custom load balancers, RDMA networking | KEDA/HPA, Istio, regional node pools | API gateway rate limits, streaming |
| | Est. FTE: 0.25 | Est. FTE: 0.1 | Est. FTE: 0.05 |
| **Model Versioning & A/B Testing** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Custom routing logic required; full control of traffic splits | K8s traffic splitting via Istio/NGINX; Argo Rollouts | LLM gateway layer (Portkey, LiteLLM, Requesty) |
| | Custom inference routers, Istio VirtualService | Argo Rollouts, Flagger, Istio | Portkey, LiteLLM, custom proxy |
| | Est. FTE: 0.25 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |
| **Failover & Redundancy** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | All failover logic self-built; no upstream provider redundancy | K8s-native health checks + pod restarts; cross-zone replication | LLM gateway handles provider failover; circuit breaking built in |
| | Custom health checks, keepalived, load balancers | Kubernetes liveness/readiness probes, multi-AZ | Portkey, LiteLLM, OpenRouter |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05 |

---

## Key Takeaways

- **Self-hosted GPU inference is operationally the most demanding workload in the ISV stack.** Initial deployment requires 2–4 FTE for 3–6 months; ongoing operations require 1.0–1.25 FTE plus on-call burden. The break-even versus managed APIs requires consistently above 50% GPU utilization (for 7B models) or above 10% (for 13B+ models) — thresholds many ISVs will not consistently achieve.

- **GPU cloud pricing has declined sharply in 2025.** H100 instances are available for $1.49–$3.90/hour at specialist providers versus $6.98/hour on Azure. A100s are now sub-$1/GPU-hour on the open market. This reduces the cost case for purchasing on-premises GPU hardware significantly.

- **Quantization is a first-class optimization, not a compromise.** AWQ 4-bit quantization retains 95% quality fidelity while delivering 75% file size reduction and enabling Marlin-kernel throughput of 741 tokens/second — often outperforming un-optimized FP16 baselines. For most ISV use cases, AWQ 4-bit is the correct default for self-hosted serving.

- **Multi-model routing (intelligent LLM routing) should be treated as a core platform capability, not an afterthought.** RouteLLM demonstrated 85% cost reduction while maintaining 95% of GPT-4 performance quality in peer-reviewed research at ICLR 2025. 37% of enterprises already use 5 or more models in production. ISVs should architect for multi-model routing from day one.

- **An LLM gateway layer is mandatory for production deployments regardless of deployment model.** Failover, rate-limit handling, fallback chains, observability, and A/B testing require a unified control plane above individual model endpoints. DIY failover implementations become operationally fragile at scale; purpose-built LLM gateways (Portkey, LiteLLM, Requesty, OpenRouter) solve these problems with minimal operational overhead.

---

## Related — Out of Scope

- **RAG pipeline infrastructure** (retrieval-augmented generation, chunking, embedding generation): See [F4: RAG Pipeline Infrastructure] for detailed coverage.
- **Vector database selection and operations**: See [F6: Embeddings and Vector Databases] for detailed coverage.
- **Agent orchestration frameworks** (LangChain, LlamaIndex, CrewAI): See [F7: Agent Orchestration] for detailed coverage.
- **Day-to-day on-premises GPU cluster operations** (hardware failure rates, datacenter power/cooling requirements, firmware management): See [F36: On-Premises Operational Profile] for detailed coverage.

---

## Sources

1. [arXiv 2511.17593: Comparative Analysis of LLM Inference Serving Systems](https://arxiv.org/html/2511.17593v1)
2. [MarkTechPost: Comparing the Top 6 Inference Runtimes for LLM Serving in 2025](https://www.marktechpost.com/2025/11/07/comparing-the-top-6-inference-runtimes-for-llm-serving-in-2025/)
3. [MarkTechPost: vLLM vs TensorRT-LLM vs HF TGI vs LMDeploy Deep Technical Comparison](https://www.marktechpost.com/2025/11/19/vllm-vs-tensorrt-llm-vs-hf-tgi-vs-lmdeploy-a-deep-technical-comparison-for-production-llm-inference/)
4. [Bizety: vLLM vs Triton — Competing or Complementary](https://bizety.com/2025/09/29/vllm-vs-triton-competing-or-complementary/)
5. [vLLM Blog: Inside vLLM — Anatomy of a High-Throughput LLM Inference System](https://blog.vllm.ai/2025/09/05/anatomy-of-vllm.html)
6. [vLLM Docs: Parallelism and Scaling](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/)
7. [vLLM Docs: Distributed Inference and Serving v0.8.0](https://docs.vllm.ai/en/v0.8.0/serving/distributed_serving.html)
8. [Anthropic: Claude API Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
9. [IntuitionLabs: LLM API Pricing Comparison 2025](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025)
10. [Amazon Bedrock Pricing — AWS](https://aws.amazon.com/bedrock/pricing/)
11. [Google Vertex AI Generative AI Pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
12. [Introl: Inference Unit Economics — True Cost Per Million Tokens Guide](https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide)
13. [SkyWork AI: LLM Cost Comparison 2025](https://skywork.ai/skypage/en/LLM-Cost-Comparison-2025-A-Deep-Dive-into-Managing-Your-AI-Budget/1975592241004736512)
14. [IntuitionLabs: H100 Rental Prices Cloud Comparison November 2025](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)
15. [IntuitionLabs: NVIDIA AI GPU Pricing Guide](https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide)
16. [RunPod: Pricing](https://www.runpod.io/pricing)
17. [Lambda AI: Pricing](https://lambda.ai/pricing)
18. [RunPod: GPU Comparison — H100, A100, L40S](https://www.runpod.io/articles/comparison/choosing-gpus)
19. [Hyperstack: How Much VRAM Do You Need for LLMs](https://www.hyperstack.cloud/blog/case-study/how-much-vram-do-you-need-for-llms)
20. [WhiteFiber: Best GPUs for LLM Inference 2025](https://www.whitefiber.com/compare/best-gpus-for-llm-inference-in-2025)
21. [BentoML LLM Inference Handbook: Choosing the Right GPU](https://bentoml.com/llm/getting-started/choosing-the-right-gpu)
22. [BentoML LLM Inference Handbook: Key Metrics](https://bentoml.com/llm/inference-optimization/llm-inference-metrics)
23. [NVIDIA NIM LLM Benchmarking Metrics](https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html)
24. [Anyscale: LLM Serving Benchmarking Metrics Docs](https://docs.anyscale.com/llm/serving/benchmarking/metrics)
25. [LocalAIMaster: AWQ vs GPTQ vs GGUF Quantization Comparison 2025](https://localaimaster.com/blog/quantization-explained)
26. [Jarvislabs: vLLM Quantization Complete Guide with Benchmarks](https://docs.jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks)
27. [Cast AI: Practical Guide to LLM Quantization Methods](https://cast.ai/blog/demystifying-quantizations-llms/)
28. [E2E Networks: GGUF vs GPTQ vs AWQ Quantization Guide](https://www.e2enetworks.com/blog/which-quantization-method-is-best-for-you-gguf-gptq-or-awq)
29. [ICLR 2025 Proceedings: RouteLLM — Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html)
30. [RouteLLM Paper PDF — ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
31. [SWFTE: Intelligent LLM Routing — How Multi-Model AI Cuts Costs by 85%](https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai)
32. [TrueFoundry: Multi-Model Routing — Why One LLM Isn't Enough](https://www.truefoundry.com/blog/multi-model-routing)
33. [TrueFoundry: LLM Load Balancing](https://www.truefoundry.com/blog/llm-load-balancing)
34. [AWS: Multi-LLM Routing Strategies for Generative AI Applications](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)
35. [Portkey: Failover Routing Strategies for LLMs in Production](https://portkey.ai/blog/failover-routing-strategies-for-llms-in-production/)
36. [Portkey: Retries, Fallbacks, and Circuit Breakers in LLM Apps](https://portkey.ai/blog/retries-fallbacks-and-circuit-breakers-in-llm-apps/)
37. [Requesty: Implementing Zero-Downtime LLM Architecture](https://www.requesty.ai/blog/implementing-zero-downtime-llm-architecture-beyond-basic-fallbacks)
38. [Maxim: Top 5 LLM Gateways in 2025](https://www.getmaxim.ai/articles/top-5-llm-gateways-in-2025-the-definitive-guide-for-production-ai-applications/)
39. [Dynatrace: AI Model Versioning and A/B Testing Blog](https://www.dynatrace.com/news/blog/the-rise-of-agentic-ai-part-6-introducing-ai-model-versioning-and-a-b-testing-for-smarter-llm-services/)
40. [Dynatrace Docs: AI Model Versioning and A/B Testing](https://docs.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/ab-model-testing)
41. [Azumo: Self-Hosting LLMs — Hidden Costs You're Missing](https://azumo.com/artificial-intelligence/ai-insights/self-hosting-llms-cost)
42. [Aimprosoft: Cost to Host and Scale a Private LLM in 2025](https://www.aimprosoft.com/blog/cost-to-host-private-llm-2025/)
43. [Pynomial: Building Scalable LLM Inference Architectures](https://pynomial.com/2025/09/building-scalable-llm-inference-architectures/)
44. [Red Hat Developer: Distributed Inference with vLLM](https://developers.redhat.com/articles/2025/02/06/distributed-inference-with-vllm)
45. [FutureAGI: Compare 11 LLM API Providers 2025](https://futureagi.com/blogs/top-11-llm-api-providers-2025)
