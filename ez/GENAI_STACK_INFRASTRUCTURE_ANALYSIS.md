# GenAI Stack Infrastructure Analysis 2025

**Research Date:** December 8, 2025
**All sources from 2025 publications**

---

## Executive Summary

This analysis examines infrastructure intensity, on-premises deployment complexity, and regulatory drivers for each layer of the GenAI/Agent technology stack. Key findings:

- **Infrastructure & Hardware** is the most resource-intensive and difficult to deploy on-premises (Difficulty: 5/5)
- **AI Models** and **Deployment & Inference** layers require significant GPU resources but have mature open-source options
- **Middle layers** (frameworks, observability, pipelines) have moderate complexity with good self-hosted alternatives
- **Regulatory drivers** increasingly mandate on-premises for healthcare (HIPAA), financial services (SOX, PCI-DSS), and government (FedRAMP, ITAR)

---

## Infrastructure Intensity Summary

| Layer | Compute Intensity | Compute % | Storage Intensity | Storage % | On-Prem Difficulty | Primary Infrastructure Requirements |
|-------|------------------|-----------|-------------------|-----------|-------------------|-------------------------------------|
| 1. Infrastructure & Hardware | Very High | 15% | Very High | 3% | 5/5 | H100/H200/B200 GPUs, HBM3e (141-192GB), NVMe arrays |
| 2. Deployment & Inference | High | 50% | High | 10% | 2/5 | GPU VRAM (40GB+), KV cache (40GB/user at 128K) |
| 3. AI Models | Very High | 25% | High | 25% | 4/5 | Model storage (35-140GB per 70B model), datasets |
| 4. Data & Storage | Low-Medium (I/O) | 2% | Very High | 30% | 2/5 | Vector DBs (6-12GB/M vectors at 1536-3072 dims), Graph DBs |
| 5. Memory, Agent Tools & Sandboxing | Medium | 3% | Medium | 5% | 3/5 | 15-20x embedding amplification, sandbox filesystems |
| 6. Data Management & Pipelines | Medium | 2% | High | 15% | 3/5 | Feature stores (TBs), model artifacts (7-140GB per model) |
| 7. Agent Frameworks | Medium | 1% | Medium | 2% | 2/5 | State checkpoints, conversation history |
| 8. Observability & Evaluation | Low-Medium | 1% | High | 8% | 2/5 | Traces (~500MB/1M req), prompt/response logs |
| 9. Security & Governance | Low-Medium | 0.5% | Medium | 1.5% | 3/5 | Guardrails (5-15GB), audit logs (6-7yr retention) |
| 10. Agentic UI & Middleware | Low | 0.3% | Low | 0.3% | 2/5 | Session state (1-10GB), CDN assets |
| 11. Dev Environment & SaaS Application Logic | Low-Medium (CPU) | 0.2% | High | 0.2% | N/A | SaaS storage (multi-TB to PB scale) |
| **TOTAL** | | **100%** | | **100%** | | |

---

## Layer-by-Layer Analysis

### Layer 1: Infrastructure & Hardware

**Compute Intensity: Very High**

#### GPU Requirements (2025)
| GPU Model | VRAM | Power (TDP) | AI Performance | Cost |
|-----------|------|-------------|----------------|------|
| NVIDIA A100 | 40/80GB HBM2e | 400W | 312 TFLOPS | $10K-$15K |
| NVIDIA H100 SXM5 | 80GB HBM3 | 700W | 2,000 TFLOPS FP16 | $25K-$40K |
| NVIDIA H200 | 141GB HBM3e | 700W | 4 petaFLOPS | Higher than H100 |
| NVIDIA B200 | Next-gen | 1000W | TBD | TBD |

#### Power & Cooling
- Classic enterprise racks: 5-10 kW
- AI racks (2025): 40-100+ kW per rack
- Next-gen (Blackwell/Rubin): 130-250 kW, potentially 600-900 kW
- Cooling consumes 20-40% of total data center power
- Liquid cooling now mandatory for high-density deployments
- PUE target for AI: <1.3 (vs 1.5-1.6 for traditional)

#### Network Requirements
- Multi-node training: 25 Gbps per GPU (data parallelism), 100+ Gbps (model parallelism)
- 10B+ parameter models: 200 Gbps to 1 Tbps internal cluster bandwidth
- NVLink 5th gen: 1.8 TB/s per GPU
- A4X instances (GB200): up to 2,000 Gbps network bandwidth

#### On-Prem Difficulty: 5/5 (Very Difficult)
- Requires data center-level investment
- Lead times for GPU procurement
- Specialized cooling infrastructure
- Power delivery at scale (three-phase 208V or single-phase 240V)
- Team size: 5-15 FTE for dedicated operations

#### Storage Intensity: Very High

AI infrastructure requires multiple storage tiers with extreme capacity and throughput requirements across GPU memory, high-speed NVMe, and distributed storage systems.

##### GPU Memory (HBM) Requirements

| Model Size | VRAM (FP16) | VRAM (4-bit Quantized) | Training Memory | Use Case |
|------------|-------------|------------------------|-----------------|----------|
| 3B-7B params | 14-16 GB | 3-8 GB | ~69 GB (w/ optimizer) | Small models, fine-tuning |
| 13B params | 24+ GB | 6-12 GB | ~130 GB | Medium models |
| 70B params | 140+ GB | 35+ GB | ~782 GB | Large models, distributed |
| 405B params | 810+ GB | 200+ GB | <100 TB (distributed) | Frontier models |

**HBM Bandwidth Performance:**
- NVIDIA H100 HBM3E: 3.35 TB/s aggregate memory bandwidth
- AMD MI300X: 192 GB HBM3 per GPU
- 2-5x throughput increase vs DDR5/GDDR6 for AI workloads
- HBM3E is the memory standard for 100B+ parameter models in 2025

**Key Finding:** By 2025, 24 GB VRAM is minimum baseline; training and inference of large models require GPUs with 40 GB, 80 GB, and 192 GB+ VRAM configurations.

##### NVMe Storage Requirements

| Storage Type | Throughput | Capacity | Use Case |
|--------------|-----------|----------|----------|
| PCIe Gen4 NVMe (4x) | 10 GB/s read, 5 GB/s write | Several TB | Single-node training |
| PCIe Gen5 NVMe (4x) | 27 GB/s read, 11 GB/s write | Several TB | High-performance training |
| PCIe Gen5 NVMe (8x) | 48 GB/s read, 26 GB/s write | Tens of TB | Distributed training clusters |
| Parallel File Systems | 1.64 TB/s read, 280 GB/s write | 100s of TB to PB | Multi-node training (optimal) |

**Storage Architecture Patterns:**
- **Memory Tiering:** Active KVs in HBM → Infrequent in DDR → Rare in NVMe
- **Direct Access:** DirectStorage and GPU Direct RDMA enable GPUs to access NVMe directly, bypassing CPU
- **Minimum Server Capacity:** Several terabytes baseline; serious projects require tens to hundreds of terabytes

**Distributed Systems:** Large-scale AI projects use Lustre, BeeGFS, or Ceph for massively parallel I/O supporting thousands of concurrent GPU core requests.

##### Model Checkpoint Storage

| Model | Checkpoint Size (Training) | Checkpoint Size (Inference) | Storage Formula |
|-------|---------------------------|----------------------------|-----------------|
| LLaMa 7B | 69 GB | 14 GB (FP16) | ~10 bytes/param (training) |
| LLaMa 70B | 782 GB | 140 GB (FP16) | ~16 bytes/param (inference) |
| 405B model | <100 TB | ~810 GB | Scales with model size, not cluster size |

**Checkpoint Frequency Requirements:**
- 16,000 GPU cluster: 155 checkpoints/day (every 9.3 minutes)
- 100,000 GPU cluster: Checkpoint every 4.4 seconds
- Optimal checkpoint time: ~50 seconds for 13.8 TB model state (with 1.64 TB/s read, 280 GB/s write)

**Storage Technology:** Training phase emphasizes large capacity, high sequential throughput, parallel bandwidth, and persistent write capability. Parallel file systems (Lustre, GPFS) are preferred for synchronous I/O; object storage is increasingly used for training workflows.

##### Data Center Storage Infrastructure

**AI Datacenter Scale (2025):**
- Microsoft AI datacenters: Exabytes of storage, storage systems five football fields in length
- NVIDIA GB200 server clusters: Millions of compute cores supported by dedicated storage infrastructure
- Storage disaggregation: NVMe/parallel file systems for checkpointing, object stores for datasets/models, archive tiers for lineage

**Market Growth:**
- HBM market: 42% annual growth through 2033, reaching $130 billion
- HBM suppliers (SK Hynix, Samsung, Micron): Sold out through calendar year 2025
- Data center infrastructure spending: $290 billion (2024), projected $1 trillion by 2030

**Storage Technology Advances:**
- Seagate Mozaic 4 HAMR platform: 4TB/disk HDDs (sampling May 2025, production 1H 2026)
- AI-optimized SSDs: High endurance for frequent checkpoint writes, model slice distribution, sample pre-processing

##### Storage Performance Requirements Summary

**Training Workloads:**
- Sequential throughput: Multi-TB/s for large clusters
- Parallel bandwidth: Thousands of concurrent I/O requests
- Write endurance: Heavy checkpoint and data pre-processing demands
- Capacity: Petabyte-scale for enterprise AI

**Inference Workloads:**
- Model weights: 140 GB (70B model) to 810 GB (405B model) in FP16
- Latency-sensitive: NVMe enables <50ms TTFT for production serving
- Moderate capacity: TB-scale sufficient for most deployments

**Overall Storage Intensity Rating: Very High**
- Multi-tier storage hierarchy required (HBM → NVMe → Distributed → Archive)
- Extreme bandwidth requirements (TB/s aggregate)
- Petabyte-scale capacity for enterprise deployments
- Specialized storage infrastructure represents significant capital investment alongside GPU costs

**Sources:** [LLM GPU VRAM Requirements 2025](https://www.propelrc.com/llm-gpu-vram-requirements-explained/), [AMD VRAM FAQs 2025](https://www.amd.com/en/blogs/2025/faqs-amd-variable-graphics-memory-vram-ai-model-sizes-quantization-mcp-more.html), [AI Servers Hardware 2025](https://unihost.com/blog/ai-servers-2025-hardware/), [Wevolver HBM Guide 2025](https://www.wevolver.com/article/hbm-memory-complete-engineering-guide-design-optimization-2025), [DeepNVMe PyTorch 2025](https://pytorch.org/blog/deepnvme-affordable-i-o-scaling-for-deep-learning-applications/), [SemiAnalysis HBM Roadmap 2025](https://semianalysis.com/2025/08/12/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm/), [VAST Data LLM Checkpoints 2025](https://www.vastdata.com/blog/a-checkpoint-on-checkpoints-in-llms), [Omdia AI Storage 2025](https://omdia.tech.informa.com/blogs/2025/sep/the-storage-that-feeds-ai-training-and-modeling-for-high-impact-ai), [Blocks and Files Object Storage 2025](https://blocksandfiles.com/2025/02/04/very-large-ai-model-training-uses-object-storage/), [Microsoft AI Datacenter 2025](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/)

#### Regulatory Drivers
- **FedRAMP IL6+**: Required for Secret classified data
- **CMMC 2.0**: Physical security for CUI/FCI processing
- **Air-gapped requirements**: Complete isolation for classified environments
- **Data sovereignty**: EU AI Act, China PIPL require in-jurisdiction processing

**Sources:** [Introl GPU Comparison 2025](https://introl.com/blog/h100-vs-h200-vs-b200-choosing-the-right-nvidia-gpus-for-your-ai-workload), [CMU Cooling Research 2025](https://www.cmu.edu/news/stories/archives/2025/february/slashing-ai-data-center-cooling-cost-and-gpucpu-power-use)

---

### Layer 2: Deployment & Inference

**Compute Intensity: High**

#### Inference Framework Comparison
| Framework | Throughput | TTFT | Best For | Complexity |
|-----------|------------|------|----------|------------|
| Ollama | 1-3 req/sec | 200-400ms | Local dev/prototyping | Low |
| vLLM | 120-160 req/sec | 50-80ms | Production serving | Medium |
| TensorRT-LLM | 180-220 req/sec | 35-50ms | Maximum performance | High |

#### Resource Requirements
- 70B model minimum: 40 GB GPU memory (70B × 4 bits + overhead)
- Single A100 GPU: $10K-$15K purchase, $2K-$3K/month cloud
- TensorRT-LLM: 1.7x speedup over vLLM but requires model compilation

#### On-Prem Difficulty: 3/5 (Complex)
- **Ollama**: Single command install, hours to deploy
- **vLLM**: OpenAI-compatible API, production-ready
- **TensorRT-LLM**: Weeks to configure, NVIDIA GPUs only

#### Storage Intensity: High

**Rating Justification:** LLM inference requires substantial storage for model weights (3.5GB-280GB per model) and significant memory/VRAM for KV cache (up to 40GB per user for long contexts). Storage intensity is rated **High** due to the combination of large model files, dynamic KV cache requirements that scale with concurrent users, and inference engine overhead.

##### Key Storage Metrics

| Component | Storage Requirements | Memory/VRAM Requirements | Notes |
|-----------|---------------------|-------------------------|-------|
| **Model Weights (FP16)** | 7B: ~14GB<br/>70B: ~140GB | Loaded into VRAM | Standard inference precision |
| **Model Weights (FP8)** | 7B: ~7GB<br/>70B: ~70GB | Loaded into VRAM | 50% reduction, <1% accuracy loss |
| **Model Weights (INT4)** | 7B: ~3.5GB<br/>70B: ~35GB | Loaded into VRAM | 75% reduction vs FP16 |
| **KV Cache (per request)** | N/A | LLaMA-2 13B: ~1MB/token<br/>Llama 3 70B: 40GB per 128K context | Scales linearly with users |
| **Inference Engine (vLLM)** | Container: ~4.8GB | Memory: 4.8-14.2GB | PagedAttention reduces fragmentation |
| **Inference Engine (TensorRT-LLM)** | Container: Variable | Memory: 13.8GB | FP8 on H100: 10K+ tokens/sec |
| **Inference Engine (Ollama)** | Container: ~175MB (minimal) | Memory: 4.8GB | Single-command deployment |

##### Model Storage by Precision Format

| Precision | Bytes/Parameter | 7B Model | 70B Model | Use Case |
|-----------|----------------|----------|-----------|----------|
| FP32 | 4 bytes | ~28GB | ~280GB | Training only |
| FP16/BF16 | 2 bytes | ~14GB | ~140GB | Standard inference |
| INT8/FP8 | 1 byte | ~7GB | ~70GB | Production serving |
| INT4 | 0.5 bytes | ~3.5GB | ~35GB | Edge deployment |

##### KV Cache Memory Scaling

**Per-Token Requirements:**
- LLaMA-2 13B: ~1MB cache per output token
- 4K context window: ~4GB per sequence (comparable to model size)
- Llama 3.1 70B at 128K context: 40GB memory for single user
- Memory consumption increases from 5GB (short sequences) to 40GB (128K sequences)

**2025 Optimizations:**
- **PagedAttention (vLLM)**: Reduces KV memory fragmentation from ~70% to <4%
- **NVFP4 KV Cache (Blackwell GPUs)**: 50% memory footprint reduction, <1% accuracy loss
- **KV Cache Offloading**: 14x faster TTFT vs recalculating from scratch

##### Production Deployment Storage Requirements

**Small Scale (Single GPU):**
- Model weights: 7-14GB (7B model, FP8-FP16)
- KV cache: 5-20GB (depends on concurrent users and context length)
- Container/engine: 5-10GB
- Total: 20-50GB storage, 16-40GB VRAM

**Medium Scale (Multi-GPU Cluster):**
- Model weights: 70-140GB (70B model, FP8-FP16)
- KV cache: 40GB+ per concurrent user at 128K context
- Production serving: 40GB+ GPU memory minimum
- Container/engine: 10-20GB
- Total: 100-500GB storage, 80GB+ VRAM per GPU

**Enterprise Scale:**
- Multiple model versions for A/B testing
- Checkpoint storage: Can reach terabytes for large-scale training
- Batch processing: Memory scales linearly with batch size
- Total: 1-10TB+ storage, petabyte-scale for training clusters

##### Infrastructure Bottlenecks

1. **VRAM Constraints:** Single A100 (80GB) can serve Llama 3 70B but limited to ~2 concurrent users at full 128K context
2. **Batch Size Impact:** Memory requirements scale linearly with concurrent requests
3. **Context Length:** Longer contexts consume exponentially more KV cache (5GB → 40GB for Llama 3.1)
4. **Multi-GPU Required:** 70B+ models need multi-GPU setups for production-scale concurrency

##### Throughput vs Storage Trade-offs

| Configuration | Storage | VRAM | Throughput | Best For |
|---------------|---------|------|------------|----------|
| Ollama (FP16) | ~14GB | 16GB | ~95 tokens/sec | Local development |
| vLLM (FP8) | ~7GB | 24GB | ~168 tokens/sec | Production serving |
| TensorRT-LLM (FP8) | ~7GB | 24GB | ~185 tokens/sec | Maximum performance |
| H100 + NVFP4 KV | ~7GB | 80GB | 10K+ tokens/sec | Enterprise scale |

**Sources:**
- [LLM Model Size Comparison 2025](https://labelyourdata.com/articles/llm-fine-tuning/llm-model-size)
- [NVIDIA LLM Quantization Guide 2025](https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/)
- [KV Caching Comprehensive Review 2025](https://www.rohan-paul.com/p/kv-caching-in-llm-inference-a-comprehensive)
- [NVIDIA KV Cache Offloading 2025](https://developer.nvidia.com/blog/accelerate-large-scale-llm-inference-and-kv-cache-offload-with-cpu-gpu-memory-sharing/)
- [vLLM Performance Tuning Guide 2025](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration)
- [NVIDIA NVFP4 KV Cache 2025](https://bitcoinethereumnews.com/tech/nvidias-nvfp4-kv-cache-revolutionizes-inference-efficiency/)
- [vLLM vs Ollama vs TensorRT Comparison 2025](https://itecsonline.com/post/vllm-vs-ollama-vs-llama.cpp-vs-tgi-vs-tensort)
- [Docker vLLM Integration 2025](https://www.docker.com/blog/docker-model-runner-integrates-vllm/)
- [LLM VRAM Requirements Guide 2025](https://www.propelrc.com/llm-gpu-vram-requirements-explained/)
- [GPU Selection for LLM Inference 2025](https://compute.hivenet.com/post/best-gpu-for-llm-inference-2025)

#### Self-Hosted Options
| Tool | License | Production Ready | GPU Support |
|------|---------|-----------------|-------------|
| Ollama | Open-source | Dev only | NVIDIA, AMD, CPU |
| vLLM | Open-source | Yes | NVIDIA, AMD, Intel, TPU |
| TensorRT-LLM | Open-source | Yes | NVIDIA only |

#### Regulatory Drivers
- **HIPAA (Jan 2025)**: Enhanced technical safeguards for PHI processing
- **FDA AI Device Guidance**: Runtime monitoring for medical devices
- **PCI-DSS v4.0.1**: Real-time processing without data retention
- **Zero Trust**: Continuous verification of all AI interactions

**Sources:** [ITECS vLLM Comparison 2025](https://itecsonline.com/post/vllm-vs-ollama-vs-llama.cpp-vs-tgi-vs-tensort), [Hivenet TensorRT Guide](https://compute.hivenet.com/post/vllm-vs-tgi-vs-tensorrt-llm-vs-ollama)

---

### Layer 3: AI Models

**Compute Intensity: Very High**

#### Model Hardware Requirements
| Model Size | Minimum VRAM | Recommended GPU | Fine-tuning Memory |
|------------|--------------|-----------------|-------------------|
| 3B-7B | 8-16 GB | RTX 4060 Ti | 16 GB VRAM/billion params |
| 13B-30B | 28+ GB | RTX 3090/4080 | Multi-GPU required |
| 70B+ | 40+ GB | A100/H100 | 8x A100/H100 recommended |

#### Open-Source Model Options (2025)
- **Llama 3.3** (Meta): Apache 2.0, industry benchmark
- **Mistral Large 3**: 675B total params, 41B active (MoE)
- **Qwen 2.5** (Alibaba): Strong multilingual
- **DeepSeek-V3**: Emerging competitor
- **Ministral 3**: Edge deployment (3B, 8B, 14B variants)

#### Parameter-Efficient Fine-Tuning
- **LoRA**: 10,000x reduction in trainable parameters
- **QLoRA**: 13B model on single RTX 4090
- Storage: Fast NVMe SSDs essential (datasets often 100s of GB)

#### On-Prem Difficulty: 4/5 (High)
- Well-established open-source ecosystem (software readily available)
- **However:** Requires GPU infrastructure from Layer 1 (H100/A100 clusters)
- 70B models need 40GB+ VRAM, multi-GPU setups for fine-tuning
- Model deployment is simple; underlying infrastructure is the challenge
- 40% cost savings vs proprietary options achievable if infrastructure exists

#### Storage Intensity: High

AI model storage requirements in 2025 present significant infrastructure challenges due to model size growth, multiple format variants, and fine-tuning workflows.

##### Base Model Storage Requirements

| Model Size Category | Base Model (FP16) | GGUF Q4 Quantized | AWQ/GPTQ 4-bit | Notes |
|---------------------|-------------------|-------------------|----------------|-------|
| 3B-7B parameters | 14-28 GB | 4-5 GB | 4-6 GB | Single GPU capable |
| 13B-32B parameters | 52-128 GB | 8-22 GB | 10-20 GB | Moderate storage |
| 70B parameters | 140 GB | 40-45 GB | 35-40 GB | High storage needs |
| 675B parameters (Mistral Large 3 MoE) | 1,350+ GB | Split across multiple files | Varies by quantization | Extreme storage requirements |

**Quantization Storage Impact:**
- **INT8 quantization**: 50% reduction vs FP16
- **INT4 quantization**: 75% reduction vs FP16 (most common for deployment)
- **Example**: Llama 3.3 70B reduces from 140GB (FP16) to ~35GB (Q4), enabling deployment on consumer hardware

##### Model Format Storage Overhead

| Format | Use Case | Storage Efficiency | Conversion Overhead |
|--------|----------|-------------------|---------------------|
| **Safetensors** | Training, fine-tuning | Baseline (100%) | Native format |
| **GGUF** | CPU/GPU inference (llama.cpp, Ollama) | 25-50% of FP16 | Requires conversion from safetensors |
| **GGML** | Legacy format | Similar to GGUF | Being phased out |
| **ONNX** | Cross-platform inference | 10-20% larger than safetensors | Additional conversion step |
| **AWQ/GPTQ** | GPU-accelerated quantized inference | 25% of FP16 | Requires calibration dataset |

**Key Storage Considerations:**
- Organizations typically store **multiple format variants** of the same model (safetensors + GGUF + AWQ)
- Model registries require versioning, adding **storage multiplicative factor** (3-10x for version history)
- Large models >50GB split into multiple files, complicating storage management

##### Fine-Tuning Storage Requirements

| Training Approach | Trainable Parameters | Adapter Storage | Dataset Storage (Typical) | Total VRAM During Training |
|-------------------|---------------------|-----------------|---------------------------|----------------------------|
| **Full Fine-Tuning** | 100% of model | Full model copy | 60-256 MB (small), 10+ GB (large) | 16 GB VRAM/billion params |
| **LoRA (r=8-64)** | 0.5-5% of model | 10-100 MB for 7B model | 60-256 MB | 10x reduction vs full |
| **QLoRA** | 0.5-5% of model | 10-100 MB for 7B model | 60-256 MB | 20x reduction vs full |

**LoRA/QLoRA Adapter Efficiency:**
- LoRA adapters: **~1% of base model parameters**, enabling massive storage savings
- Example: Llama 3.2 70B LoRA adapters: **~700 MB** vs 140 GB full model
- QLoRA achieves **4x memory reduction** vs LoRA through quantized training
- Adapter weights allow **sharing base model** across multiple fine-tuned variants

**Fine-Tuning Dataset Storage:**
- Small datasets: 60-256 MB (typical instruction-tuning)
- Large datasets: 10-100+ GB (continued pre-training, domain adaptation)
- Datasets >1 GB may cause longer processing times
- Format requirement: JSONL with 'prompt' and 'completion' columns

##### Model Registry & Versioning Storage

**MLflow Model Registry:**
- Tracks multiple versions per model with full lineage
- Version history creates storage multiplication (each version = full model copy)
- Metadata storage: Minimal (PostgreSQL backend)
- Artifact storage: Dominant cost factor

**DVC (Data Version Control):**
- Content-addressable storage avoids redundancy
- Stores only deltas, not full duplicates
- `.dvc/cache` grows with commit history (recommend commit history limits)
- Most storage-efficient for large model versioning

**Typical Registry Storage Growth:**
- **Single model lifecycle**: 3-10 versions over development
- **Storage multiplier**: 3-10x base model size for full version history
- **Example**: 70B model with 5 versions = 700 GB (FP16) or 175-225 GB (quantized)

##### Hardware Storage Recommendations (2025)

| Scale | SSD Type | Capacity | Use Case |
|-------|----------|----------|----------|
| **Development** | NVMe SSD | 1-2 TB | Single model experimentation |
| **Small Team** | NVMe SSD | 4-8 TB | Multiple models, limited versions |
| **Production** | NVMe RAID | 20-50 TB | Model registry, multiple versions |
| **Enterprise** | Object Storage (S3-compatible) | 100+ TB | Full MLOps platform, extensive versioning |

**Critical Infrastructure Requirements:**
- **NVMe SSDs essential**: Loading 30-70 GB models from HDD creates severe bottlenecks
- **Read/write speeds**: NVMe (3,000+ MB/s) vs SATA SSD (550 MB/s) vs HDD (120 MB/s)
- **Object storage**: MinIO or S3-compatible for model registry artifact storage
- **Deduplication**: Reduces redundant storage by 30-50% across model variants

##### Storage Intensity Rating Justification

**Rating: High** (not "Very High" due to mitigation strategies)

**Rationale:**
1. **Base model sizes**: 70B models require 35-140 GB storage depending on quantization
2. **Format proliferation**: Organizations store 2-4 format variants per model (safetensors, GGUF, AWQ)
3. **Version management**: Model registries multiply storage 3-10x for version history
4. **Fine-tuning datasets**: 10-100+ GB for domain-specific training data
5. **Mitigation available**: Quantization (75% reduction), LoRA adapters (99% reduction), DVC deduplication

**Comparison to Other Layers:**
- **Higher than**: Data & Storage Layer 4 (vector embeddings are smaller than full models)
- **Lower than**: Infrastructure Layer 1 (which includes training storage requirements at petabyte scale)
- **Similar to**: Deployment & Inference Layer 2 (both require substantial fast storage)

**2025 Trends:**
- Model sizes growing: 675B MoE models now common (Mistral Large 3)
- Quantization adoption increasing: 4-bit quantization standard for deployment
- Storage costs decreasing: But not keeping pace with model size growth
- Enterprise adoption: Model registries becoming standard, increasing version sprawl

**Sources:**
- [Llama Model Size Storage 2025](https://www.byteplus.com/en/topic/464544)
- [Understanding Model Sizes 2025 - Enclave AI](https://enclaveai.app/blog/2025/08/13/understanding-model-sizes-in-2025/)
- [Qwen 2.5 Quantization Guide - DeepWiki](https://deepwiki.com/QwenLM/Qwen2.5/4.1-model-quantization)
- [PC Requirements Qwen 2025 - Apatero](https://apatero.com/blog/pc-requirements-qwen-wan-local-setup-guide-2025)
- [Fine-Tuning Landscape 2025 - Medium](https://medium.com/@pradeepdas/the-fine-tuning-landscape-in-2025-a-comprehensive-analysis-d650d24bed97)
- [LoRA vs QLoRA 2025 - Modal](https://modal.com/blog/lora-qlora)
- [AI Storage Best Practices 2025 - TierPoint](https://www.tierpoint.com/blog/ai-data-storage/)
- [Google Cloud AI Storage Architecture](https://cloud.google.com/architecture/ai-ml/storage-for-ai-ml)
- [MLflow Model Registry Documentation](https://mlflow.org/docs/latest/ml/model-registry/)
- [DVC Model Versioning 2025 - CodezUp](https://codezup.com/ml-model-versioning-mlflow-dvc/)

#### Regulatory Drivers
- **EU AI Act GPAI (Aug 2025)**: Transparency reports, training data documentation
- **Supply Chain Security**: Model signing, SPDX 3.0 AI profiles
- **ITAR**: Defense-related model access restrictions
- **NIST AI RMF**: Threat categories for model security

**Sources:** [Red Hat Mistral Deployment 2025](https://developers.redhat.com/articles/2025/12/02/run-mistral-large-3-ministral-3-vllm-red-hat-ai), [SuperAnnotate Fine-tuning Guide](https://www.superannotate.com/blog/llm-fine-tuning)

---

### Layer 4: Data & Storage

**Compute Intensity: Low-Medium (I/O Bound)**

*Note: Vector and graph databases are primarily I/O and memory-bound, not compute-intensive. O(log n) queries and k-NN searches run in single-digit milliseconds due to efficient indexing, not heavy computation.*

#### Vector Database Comparison
| Database | Deployment | Best For | Performance |
|----------|------------|----------|-------------|
| Pinecone | Managed only | Enterprise, compliance | O(log n) queries |
| Weaviate | Self-hosted/Cloud | Hybrid search | 10-NN in single-digit ms |
| Qdrant | Self-hosted/Cloud | Cost-sensitive | Lower resource requirements |
| ChromaDB | Embedded | Prototyping | Zero-config |
| Milvus | Self-hosted | Billion-scale | 35K+ GitHub stars |

#### Graph Database Comparison
| Database | Architecture | Best For | Performance |
|----------|--------------|----------|-------------|
| Neo4j | Disk-based (Java) | Large historic graphs | Established ecosystem |
| Memgraph | In-memory (C++) | Real-time, streaming | 5-6x faster reads than Neo4j |

#### On-Prem Difficulty: 2/5 (Moderate)
- Mature Helm charts for Kubernetes deployment
- Docker support across all major platforms
- Milvus requires data engineering expertise
- Neo4j has longer track record; Memgraph trades maturity for speed

#### Storage Intensity: High

Vector and graph databases require substantial storage due to high-dimensional embeddings, index overhead, and replication requirements. Production deployments commonly experience 10x data expansion from raw text to indexed vectors.

##### Storage Per Million Vectors

| Database Type | Dimensions | Storage/Million Vectors | Index Overhead | Notes |
|---------------|------------|-------------------------|----------------|-------|
| Vector DB (OpenAI ada-002) | 1,536 | ~6 GB raw | +1-20% HNSW | 4 bytes/float32 |
| Vector DB (text-embedding-3-large) | 3,072 | ~12 GB raw | +1-20% HNSW | Doubled dimensions = 2x storage |
| Vector DB (Qwen-3) | 4,096 | ~16 GB raw | +1-20% HNSW | Latest models trending higher |
| Graph DB (Neo4j) | N/A | Varies by relationships | Disk-based | Trillions of nodes possible |
| Graph DB (Memgraph) | N/A | Hundreds of millions | In-memory (higher cost) | Single-digit billions max |

**Storage Calculation Formula:** `(vectors × dimensions × 4 bytes) / 1024³ = GB`

**Real-World Example:** 10 million documents with text-embedding-3-large (3,072 dimensions) = ~116 GB embeddings alone, before indexing.

##### Index Storage Overhead

HNSW (Hierarchical Navigable Small World) indexes add significant storage overhead:

- **Memory overhead range:** 1-20% of raw vector data for uncompressed float32
- **Link storage:** 16-32 bytes per vector for graph connections (M neighbors × 4-8 bytes each)
- **Parameter impact:** Larger `m` values (bi-directional links) increase overhead proportionally
- **Example:** 1M vectors at 128 dimensions might consume hundreds of MB for HNSW index alone
- **Compression trade-off:** Binary quantization (4-8x savings) or scalar quantization reduces storage but may degrade accuracy

##### Production Deployment Storage

| Scale | Vector Count | Raw Storage | With Index | With 3x Replication | Total Production Storage |
|-------|--------------|-------------|------------|---------------------|-------------------------|
| Small | 1M | 6 GB | 7-8 GB | 21-24 GB | ~25 GB |
| Medium | 50M | 300 GB | 330-360 GB | 990-1,080 GB | ~1 TB |
| Large | 100M | 600 GB | 660-720 GB | 1,980-2,160 GB | ~2 TB |
| Enterprise | 1B | 6 TB | 6.6-7.2 TB | 19.8-21.6 TB | ~20 TB |

**Data Expansion:** Production systems commonly see **10x expansion** from raw text to indexed vectors due to:
- Embedding storage (6-16 GB per million vectors)
- Index files (almost 50% of total in some Milvus deployments)
- Replication factor of 3x (industry standard for high availability)
- Backup snapshots (incremental, but still substantial)

##### Backup and Replication Storage

**Replication Overhead:**
- Standard replication factor: 3x (triples storage requirements)
- Storing precomputed indexes alongside raw vectors: 2x storage increase (faster restore)
- Asynchronous replication: Lower latency, risk of temporary inconsistency
- Synchronous replication: Guaranteed consistency, higher write latency

**Backup Strategies:**
- Incremental snapshots every 15 minutes to object storage (industry best practice)
- Retain daily full backups for 30 days
- Log-based change tracking to capture only deltas since last backup
- Example: Milvus uses log broker for incremental updates, avoiding full backups

**Cloud Cost Comparison (AWS, 2025):**
- Traditional vector DB (10M vectors): ~$300-$1,105/month (Pinecone Enterprise, Qdrant, Weaviate)
- AWS S3 Vectors (10M vectors): ~$30/month storage + query costs
- AWS claims up to 90% cost reduction vs specialized vector databases
- S3 Vectors pricing: $0.20/GB upload, $0.06/GB/month storage, plus query charges

**Production Best Practices:**
- Pin "hot" indices on NVMe for performance
- Offload long-tail/cold vectors to cheaper block storage
- Prune stale vectors regularly (inactive users/products)
- Use tiered storage to optimize cost vs performance

##### Vector Database Scale Limits (2025)

| Database | Typical Production Scale | Maximum Theoretical | Architecture |
|----------|-------------------------|---------------------|--------------|
| ChromaDB | <1M vectors | ~10M vectors | Best for prototyping; not production-scale |
| Qdrant | Millions to billions | Billions | Resource-tunable, efficient at scale |
| Weaviate | Efficient <50M | 100M+ (needs planning) | Resource-intensive above 100M |
| Pinecone | Billions | No stated limit | Fully managed, consistent at scale |
| Milvus | Hundreds of millions | Trillions | Cloud-native, horizontal scaling |

**Graph Database Storage:**
- Neo4j: Disk-based, can handle gigantic historic graphs (quadrillions theoretical limit)
- Memgraph: In-memory, typical deployments = hundreds of millions of nodes/edges, largest = single-digit billions
- Memory cost consideration: Storing data in RAM is orders of magnitude more expensive than disk

**Sources:**
- [Microsoft Azure Vector Index Limits 2025](https://learn.microsoft.com/en-us/azure/search/vector-search-index-size)
- [Vicki Boykis Embedding Size Analysis 2025](https://vickiboykis.com/2025/09/01/how-big-are-our-embeddings-now-and-why/)
- [Pure Storage Vector Database Blog 2025](https://blog.purestorage.com/purely-technical/managing-vector-storage-bloat-insights-for-scalable-systems/)
- [Zilliz Large Embeddings Storage 2025](https://zilliz.com/ai-faq/what-are-the-storage-requirements-for-large-embeddings)
- [Milvus Backup and Replication 2025](https://milvus.io/ai-quick-reference/how-do-vector-databases-handle-backup-and-restore-or-replication-for-very-large-datasets-and-what-impact-does-that-have-on-system-design-in-terms-of-time-and-storage-overhead)
- [AWS S3 Vectors GA Announcement 2025](https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance/)
- [Zilliz Milvus vs ChromaDB 2025](https://zilliz.com/blog/milvus-vs-chroma)
- [Memgraph vs Neo4j Production Scale 2025](https://medium.com/decoded-by-datacast/memgraph-vs-neo4j-in-2025-real-time-speed-or-battle-tested-ecosystem-66b4c34b117d)

#### Regulatory Drivers
- **GDPR**: Data minimization, right to erasure for embeddings
- **HIPAA**: AES-256 encryption, minimum necessary access
- **China PIPL**: "Important data" must remain in-country
- **EU AI Act**: Training data residency for high-risk systems

**Sources:** [LiquidMetal Vector DB Comparison 2025](https://liquidmetal.ai/casesAndBlogs/vector-comparison/), [Memgraph vs Neo4j 2025](https://memgraph.com/blog/neo4j-vs-memgraph)

---

### Layer 5: Memory, Agent Tools & Sandboxing

**Compute Intensity: Medium**

#### Memory Systems
| System | Token Usage | Latency | Self-Hosted |
|--------|-------------|---------|-------------|
| Mem0 | 7K tokens/conv | 1.44s | Sparse docs, challenging |
| Mem0g (graph) | 14K tokens/conv | 2.6s | Sparse docs |
| Zep (Graphiti) | 600K+ tokens | Higher | Community Edition available |

#### Code Execution Sandboxes
| Platform | Isolation | Cold Start | Self-Hosted |
|----------|-----------|------------|-------------|
| E2B | Firecracker microVMs | 150ms | Experimental |
| Modal | gVisor | 2-5+ seconds | No |
| SkyPilot | Self-managed | Fastest | Yes (2.6x faster than E2B) |

#### Browser Automation
- **Browserbase**: Managed Playwright/Selenium, 4 vCPUs/browser
- Concurrency limits and rate limiting apply
- SOC-2 Type 1 and HIPAA compliance

#### On-Prem Difficulty: 3/5 (Complex)
- Memory systems: Mem0 SaaS focus, Zep community edition viable
- Sandboxing: Self-hosted faster but requires control plane management
- Browser automation: On-prem options less mature

#### Storage Intensity: Medium

| Component | Storage per Session | Persistence Type | Scale Characteristics |
|-----------|---------------------|------------------|----------------------|
| **Mem0** | 7K tokens/conversation | Vector + Graph | 80% token reduction via compression |
| **Mem0g (Graph)** | 14K tokens/conversation | Neo4j graph | 2x token usage vs base Mem0 |
| **Zep (Graphiti)** | 600K+ tokens | Temporal knowledge graph | Full context caching |
| **E2B Sandbox** | <5 MiB memory overhead/microVM | Ephemeral (24h max) | High-density deployments |
| **Modal Sandbox** | Up to 1 GiB writes | Ephemeral Volumes | 5 min default, 24 hr max |
| **Browserbase Contexts** | 10s-100s MB | Optional persistence | Caching speeds up page loads |

**Key Finding (2025):** Embedding-based memory systems require 30x storage amplification (10x for embeddings, 3x for indices). Enterprise deployments with 1M+ sessions reach 100+ TB with vector indices and graph storage.

**Sources:** [Mem0 ArXiv 2025](https://arxiv.org/html/2504.19413v1), [Zep Temporal Knowledge Graph 2025](https://arxiv.org/html/2501.13956v1), [E2B Sandbox 2025](https://modal.com/blog/top-code-agent-sandbox-products)

#### Regulatory Drivers
- **AI Agent Security**: AWS/IBM recommend sandboxing (Firecracker/gVisor)
- **Insider Threat**: AI agents as new threat category
- **Attorney-Client Privilege**: Closed environments safest
- **Zero Trust**: Continuous verification for tool access

**Sources:** [Graphlit Memory Survey 2025](https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks), [Modal Sandbox Products 2025](https://modal.com/blog/top-code-agent-sandbox-products)

---

### Layer 6: Data Management & Pipelines

**Compute Intensity: Medium**

#### Orchestration Platform Comparison
| Platform | Monthly Downloads | Self-Hosted | Cloud Offering |
|----------|-------------------|-------------|----------------|
| Apache Airflow 3.0 | 30M+ | Yes | Managed options |
| Dagster | Growing | Yes | Dagster Cloud |
| Prefect | Growing | Yes | Prefect Cloud |

#### Feature Store Options
| Platform | Deployment | Key Features |
|----------|------------|--------------|
| Feast | Self-hosted | Modular, Kubernetes via feast-operator |
| Tecton | Managed | Feature-platform-as-a-service |
| Hopsworks | Both | Full ML platform |

#### On-Prem Difficulty: 3/5 (Complex)
- Airflow: Industry standard but database bottlenecks at scale
- Dagster: Asset-centric, requires paradigm understanding
- Prefect: Developer-friendly, hybrid execution model
- Feast: Minimal infrastructure, pluggable architecture

#### Key Infrastructure Requirements
- PostgreSQL/Redis for state management
- S3-compatible storage for artifacts
- Worker nodes for distributed execution
- Moderate deployment (500 DAGs): 2-5GB metadata/month

#### Storage Intensity: High

| Component | Storage Requirements | Growth Rate | Retention Needs |
|-----------|---------------------|-------------|-----------------|
| **Orchestration Metadata** | Small: 1-2GB/mo; Medium (500 DAGs): 2-5GB/mo; Large: 10-50GB/mo | Linear with DAG count + execution frequency | 3-12 months (prunable) |
| **Feature Store - Offline** | Terabytes of historical data (S3/BigQuery/Delta Lake) | Continuous append | Months to years |
| **Feature Store - Online** | Current state only (Redis/Aerospike) | Stable (overwrites) | Real-time serving |
| **ML Model Artifacts** | 250GB-1TB per large model; multiple versions | 16GB VRAM/billion params | 1-7 years (compliance) |
| **Artifact Storage (S3/Blob)** | 10-50TB (small); 100-500TB (medium); PB-scale (enterprise) | Dataset growth + versioning | Varies by compliance |

**Key Finding (2025):** Global data pipeline market growing at 20% CAGR (2025-2032). ML-driven retention policies can reduce storage by 60% (400GB savings in research cases). Feature stores represent offline (TBs historical) + online (current state) split.

**Sources:** [Astronomer Airflow Database 2025](https://www.astronomer.io/docs/learn/airflow-database), [Tecton Feature Store 2025](https://www.tecton.ai/blog/what-is-a-feature-store/), [Google Cloud Model Artifacts 2025](https://cloud.google.com/blog/topics/developers-practitioners/scalable-ai-starts-with-storage-guide-to-model-artifact-strategies)

**Sources:** [ZenML Orchestration Comparison 2025](https://www.zenml.io/blog/orchestration-showdown-dagster-vs-prefect-vs-airflow), [Gocodeo Feature Stores 2025](https://www.gocodeo.com/post/top-5-feature-stores-in-2025-tecton-feast-and-beyond)

---

### Layer 7: Agent Frameworks

**Compute Intensity: Low to Medium**

#### Framework Comparison
| Framework | Architecture | Scaling | Self-Hosted |
|-----------|--------------|---------|-------------|
| LangGraph | Graph-based state machines | Horizontal scaling | Yes + Cloud/Hybrid |
| CrewAI | Role-based collaboration | Moderate scale | Yes |
| AutoGen | Multi-agent conversation | Varies | Yes |

#### Deployment Options (LangGraph)
- **Cloud SaaS**: Fully managed
- **Hybrid (BYOC)**: SaaS control plane + self-hosted data plane
- **Fully Self-Hosted**: Enterprise plan only, Helm charts on EKS

#### On-Prem Difficulty: 2/5 (Moderate)
- Primary costs are LLM API calls, not infrastructure
- Orchestration overhead relatively low
- Multi-agent coordination can create token usage spikes
- Production use validated by LinkedIn, Uber, Klarna

#### Storage Intensity: Medium

Agent frameworks require persistent storage for state management, conversation history, and checkpoints. Storage needs vary significantly by framework architecture and production scale.

##### Storage by Framework

| Framework | State Storage Backend | Per-Conversation Estimate | Checkpoint Frequency | Production Scale Considerations |
|-----------|----------------------|---------------------------|---------------------|--------------------------------|
| **LangGraph** | PostgreSQL (recommended), Redis, SQLite, MongoDB, Couchbase | Varies by state complexity; stores only changed values per checkpoint | Every superstep (automatic) | Optimized for production: stores channel values separately and versioned |
| **CrewAI** | SQLite (long-term), ChromaDB (short-term, entity) | Default local storage via appdirs | Task completion | Limited scalability with default SQLite/ChromaDB; challenging for multi-tenant production |
| **AutoGen** | In-memory (default), Mem0, MemGPT, custom stores | Depends on implementation; no native persistence in 0.4 | Manual save_state() calls | Conversation history not persisted by default; requires external memory integration |

##### LangGraph Production Storage

**PostgreSQL Checkpointer Architecture:**
- Stores each channel value separately and versioned
- Each checkpoint only stores values that changed (delta storage)
- Large channel values stored in `checkpoint_blobs` table (not inline JSONB)
- Pipeline mode reduces database round-trips for improved write throughput
- **ShallowPostgresSaver** option: Stores only latest checkpoint per thread (reduced storage for apps not needing history)

**Checkpoint Frequency:**
- Automatic checkpoint at every superstep (graph execution step)
- Scales linearly with number of active nodes
- Constant on length of history (only deals with latest checkpoint)
- Constant on number of threads (threads are independent)

**Production Best Practices (2025):**
- Don't store large data (>10MB) in state; store references instead (e.g., S3 keys for PDFs)
- Redis checkpointing enables horizontal scaling (any worker can pick up any workflow)
- LangGraph Platform (now "LangSmith Deployment"): Includes robust PostgreSQL checkpointer out-of-the-box

##### CrewAI Storage Architecture

**Storage Backends:**
- **Short-Term Memory:** ChromaDB with RAG for current session context
- **Long-Term Memory:** SQLite3 for task results across sessions
- **Entity Memory:** RAG-based tracking of people, places, concepts

**Storage Location:**
- Default: Platform-specific directory via `appdirs` library
- macOS: `~/Library/Application Support/CrewAI/{project_name}/`
- Customizable via `CREWAI_STORAGE_DIR` environment variable

**Production Deployment Challenges:**
- Default SQLite/ChromaDB not designed for multi-tenant production scale
- Azure App Service incompatibility: ChromaDB requires newer SQLite than Azure provides (~v3.35.0)
- Workaround: Containerization with custom Docker image controlling SQLite version
- Alternative: External databases (Azure SQL, Cosmos DB) for scalability and concurrency

##### AutoGen Memory Management

**Current State (AutoGen 0.4):**
- No native conversation history persistence across sessions
- Agents start each run without prior session history (reported issue as of April-May 2025)
- State can be saved via `save_state()` call on `AssistantAgent`

**Memory Options for Persistence:**
1. **ListMemory** (built-in): Basic in-memory context storage
2. **Mem0 Integration:** Smart memory layer with hybrid database (vector + key-value + graph); associates memories with unique identifiers; up to 90% token cost reduction
3. **MemGPT:** Stateful interaction with configurable context retention
4. **Teachability:** Persists user teachings in vector database across chat boundaries

**Token Management:**
- MessageHistoryLimiter restricts total messages for context history
- Essential for managing token limits (8K to 1M+ tokens depending on model)

##### Storage Performance Characteristics

**Context and Token Limits:**
- Small conversations: 8K tokens sufficient for simple Q&A
- Complex multi-turn: 128K+ tokens required for troubleshooting, personalization
- Largest available (2025): 1M+ token context windows
- Multi-agent systems consume ~15x tokens compared to single-chat applications (Anthropic)

**Memory Architecture Layers (Google ADK Pattern):**
- **Working Context:** Immediate prompt (temporary)
- **Session:** Durable log of user messages, agent replies, tool calls, errors
- **Memory:** Long-lived searchable knowledge outliving single sessions
- **Artifacts:** Large binary/textual data (images, files, logs) addressed by name/version

**Storage Growth Considerations:**
- Hierarchical summarization compresses inter-agent communication efficiently
- Avoids storing complete conversation transcripts; creates layered summaries
- Storage needs vary with conversation length, artifacts (images, files), and compression strategies

##### Overall Storage Intensity Rating: Medium

**Justification:**
- **Lower than GPU/model layers:** State storage measured in MB-GB per conversation vs TB-PB for model weights and training
- **Higher than observability layers:** Continuous checkpointing creates persistent storage growth
- **Production critical:** State persistence enables fault tolerance, human-in-the-loop, and time-travel debugging
- **Framework-dependent:** LangGraph optimized for production scale; CrewAI/AutoGen require additional architecture for enterprise deployment
- **Manageable costs:** PostgreSQL/Redis infrastructure standard; primary costs remain LLM API calls, not storage

**Recommended Production Stack:**
- LangGraph with PostgreSQL checkpointer for production agents
- ShallowPostgresSaver for applications not requiring checkpoint history
- Object storage (S3) for artifacts referenced in state (not stored inline)
- Redis for horizontal scaling and low-latency state access

**Sources:** [Mastering LangGraph Checkpointing 2025](https://sparkco.ai/blog/mastering-langgraph-checkpointing-best-practices-for-2025), [LangGraph & Redis Blog 2025](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/), [CrewAI Memory Docs](https://docs.crewai.com/en/concepts/memory), [AutoGen Memory Management Medium 2025](https://medium.com/@shmilysyg/memory-management-within-autogen-1-2-1e6303ba5d7a), [Agent Memory Comparative Analysis 2025](https://dev.to/foxgem/ai-agent-memory-a-comparative-analysis-of-langgraph-crewai-and-autogen-31dp), [Google ADK Architecture 2025](https://developers.googleblog.com/en/architecting-efficient-context-aware-multi-agent-framework-for-production/), [LangGraph Platform GA 2025](https://blog.langchain.com/langgraph-platform-ga/), [Benchmarking AI Agent Memory 2025](https://www.letta.com/blog/benchmarking-ai-agent-memory), [Agent Framework Comparison 2025](https://langwatch.ai/blog/best-ai-agent-frameworks-in-2025-comparing-langgraph-dspy-crewai-agno-and-more)

#### Regulatory Drivers
- **CCPA ADMT (Jan 2027)**: Automated decisionmaking transparency
- **Colorado AI Act (June 2026)**: Duty of care against algorithmic discrimination
- **EU AI Act**: High-risk system documentation, human oversight

**Sources:** [Softcery AI Agent Frameworks 2025](https://softcery.com/lab/top-14-ai-agent-frameworks-of-2025-a-founders-guide-to-building-smarter-systems), [LangChain Platform GA 2025](https://blog.langchain.com/langgraph-platform-ga/)

---

### Layer 8: Observability & Evaluation

**Compute Intensity: Low to Medium**

#### Platform Comparison
| Platform | Self-Hosted | Typical Cost | Setup Time |
|----------|-------------|--------------|------------|
| Langfuse | Yes (MIT) | $50-500/mo infra | 5 min (Docker) |
| Arize Phoenix | Yes (Free) | $50-500/mo infra | 2-4 hours |
| LangSmith | SaaS only | Subscription | 15 min |
| Helicone | SaaS only | Subscription | 15 min |

#### Langfuse Architecture (Self-Hosted)
- 2 application containers (Web + Worker)
- PostgreSQL (transactional)
- ClickHouse (OLAP for traces)
- Redis/Valkey (cache/queue)
- S3/Blob storage

#### On-Prem Difficulty: 2/5 (Moderate)
- Langfuse: June 2025 open-sourced commercial modules under MIT
- Thousands of active self-hosted deployments
- Can handle tens of thousands of events/minute
- VPC or on-premises deployment for high-security

#### Storage Intensity: High

| Data Type | Storage per 1M Requests | Retention Requirements | Compression Ratio |
|-----------|-------------------------|------------------------|-------------------|
| **Trace Data (OpenTelemetry)** | ~500 MB | 14-400 days | 6.5x with Tracezip |
| **Prompt/Response History** | 1-5 GB | 30-400 days | 10:1 with context compression |
| **Evaluation Datasets** | 100 MB - 1 GB | Indefinite | Minimal |
| **Metrics (Time-Series)** | 50-200 MB | 30-90 days | Variable |
| **ClickHouse Analytics** | Workload-dependent | 30+ days with TTL | Up to 90% reduction |

**Platform Storage Requirements:**
- **Langfuse (Self-Hosted)**: Min 100 GB disk; MinIO and ClickHouse grow fastest; 1 MB trace truncation limit
- **LangSmith (SaaS)**: Base traces 14-day retention ($0.50/1K); Extended 400-day ($4.50/1K)
- **Arize Phoenix**: PostgreSQL 14+ required; 8 GiB PV in Kubernetes example
- **ClickHouse**: 1,000+ Langfuse v3 deployments; up to 90% storage reduction via columnar compression

**Key Finding (2025):** Tracezip compression achieves 6.46x compression ratios for trace data (35-44% improvement over traditional compression). ClickHouse emerged as industry standard for LLM trace storage.

**Sources:** [Langfuse Scaling Docs](https://langfuse.com/self-hosting/scaling), [LangSmith Concepts](https://docs.smith.langchain.com/observability/concepts), [Tracezip Paper 2025](https://arxiv.org/html/2502.06318v1), [ClickHouse LLM Observability](https://clickhouse.com/engineering-resources/llm-observability)

#### Regulatory Drivers
- **EU AI Act**: Continuous performance monitoring for high-risk AI
- **NIST AI RMF**: Monitor performance, trustworthiness, risks
- **SOX (2025)**: Real-time ICFR metrics, control execution monitoring

**Sources:** [Getmaxim Platform Comparison 2025](https://www.getmaxim.ai/articles/choosing-the-right-ai-evaluation-and-observability-platform-an-in-depth-comparison-of-maxim-ai-arize-phoenix-langfuse-and-langsmith/), [Langfuse Self-Hosting Docs](https://langfuse.com/self-hosting)

---

### Layer 9: Security & Governance

**Compute Intensity: Low to Medium**

#### Guardrails Options
| Platform | Type | Key Features |
|----------|------|--------------|
| OpenGuardrails | Open-source | Modular, enterprise-ready |
| Llama Guard (Meta) | Open-source | Content moderation |
| Granite Guardian (IBM) | Open-source | Enterprise AI safety |
| Amazon Bedrock Guardrails | Managed | 6 safeguard policies |
| NeMo Guardrails (NVIDIA) | Framework | Conversational AI |

#### Security Context (2025)
- Average US data breach cost: $10.22M (IBM 2025)
- 97% of AI-related breaches occurred without access controls
- Real-time validation can slow AI workflows

#### On-Prem Difficulty: 3/5 (Complex)
- Multi-layer defense-in-depth approach required
- Continuous learning systems need MLOps infrastructure
- Primary bottleneck: latency from real-time validation
- Modular open-source options can run privately

#### Storage Intensity: Medium to High

Security and governance layer storage requirements scale based on compliance obligations, audit retention policies, and enterprise deployment scale. While individual guardrails models are relatively small (2-280 GB), audit logs and compliance documentation drive long-term storage demands.

**Guardrails Model Storage Requirements:**

| Component | Model Size | Notes | Source |
|-----------|-----------|-------|--------|
| Llama Guard (7B) | 13-14 GB | FP16 precision; 4 GB with 4-bit quantization | [Byteplus Llama Storage 2025](https://www.byteplus.com/en/topic/464544) |
| Llama Guard (70B) | 70-90 GB | 8-bit quantization; 280 GB at 32-bit | [Hardware Corner 2025](https://www.hardware-corner.net/guides/computer-to-run-llama-ai-model/) |
| Granite Guardian 3.2 | 3.5-5 GB | 30% smaller than v3.1; reduced via pruning | [IBM Granite Guardian 2025](https://www.ibm.com/granite/docs/models/guardian) |
| NeMo Guardrails | <2 GB | Embedding models + configurations | [NVIDIA NeMo Requirements 2025](https://docs.nvidia.com/nemo/microservices/latest/requirements.html) |

**Audit Log Storage Requirements:**

| Storage Type | Retention Period | Growth Rate | Source |
|-------------|------------------|-------------|--------|
| AI Audit Logs (General) | 1-2 years minimum | Scales with query volume | [Latitude Audit Logs 2025](https://latitude-blog.ghost.io/blog/audit-logs-in-ai-systems-what-to-track-and-why/) |
| Healthcare (HIPAA) | 6 years | Baseline + 6-12 months for behavioral analysis | [AuditBoard Security Log 2025](https://auditboard.com/blog/security-log-retention-best-practices-guide) |
| Financial Services | 7+ years | Regulatory mandated | [AuditBoard Security Log 2025](https://auditboard.com/blog/security-log-retention-best-practices-guide) |
| EU AI Act (High-Risk) | Varies by risk tier | Articles 12, 19, 72 compliance | [Logdy EU AI Act 2025](https://logdy.dev/blog/post/eu-ai-act-implications-for-log-management-systems-and-compliance) |

**Key Audit Log Elements to Track:**
- User access and authentication events
- Prompt inputs and AI-generated outputs
- Model versioning and system configuration changes
- Decision-making processes and routing logic
- Security incidents and anomaly detection

**Policy & Configuration Storage:**
- Policy-as-code implementations: <100 MB (configuration files, Colang scripts, YAML)
- Configuration store options: PostgreSQL (default), External DB, or NFS
- Version control for model configurations: Minimal (<50 MB per version)
- Source: [NVIDIA NeMo Configuration Store 2025](https://docs.nvidia.com/nemo/microservices/latest/guardrails/manage-guardrail-configs/configuration-store.html)

**Compliance Documentation Storage:**
- Model training documentation: 90-day minimum retention (longer if regulated)
- Risk assessment reports: Annual requirements for VLOPs/VLOSEs under DSA
- Performance metrics and test results: Lifecycle-based retention
- Data lineage and audit trails: Permanent for compliance verification
- Source: [Gimmal Data Retention AI Era 2025](https://gimmal.com/data-retention-policies-in-the-ai-era-whats-changing/)

**Enterprise Storage Growth Rates:**
- Unstructured data growth: 55-65% CAGR (26.4% per IDC)
- Object storage dominance: 70-75% of cloud-native enterprise data
- 30% of cloud object deployments exceed 10 PB
- Source: [MinIO Enterprise Storage 2025](https://www.min.io/learn/enterprise)

**Storage Architecture Best Practices:**
- Tiered storage: Recent logs on high-performance storage, older logs archived to cost-effective systems
- Compression and archiving: Reduce requirements while maintaining searchability
- Centralized repositories: Consolidate audit artifacts, test results, compliance docs
- Tamper-proof systems: Maintain log integrity for regulatory audits
- Source: [Medium Audit Logging AI 2025](https://medium.com/@pranavprakash4777/audit-logging-for-ai-what-should-you-track-and-where-3de96bbf171b)

**2025 Regulatory Context:**
- EU AI Act fines: Up to 7% of global annual revenue for non-compliance
- 85% of organizations using AI, but governance lags behind technology evolution
- By 2026: 50% of world governments expect AI law adherence
- Source: [Wiz AI Compliance 2025](https://www.wiz.io/academy/ai-compliance)

**Summary:** Storage intensity is rated **Medium to High** because while guardrails models themselves are compact (2-90 GB), enterprise-scale audit logging, compliance documentation, and regulatory retention requirements drive total storage into the multi-terabyte range over time. Organizations in heavily regulated industries (healthcare, finance) face higher storage burdens due to 6-7+ year retention mandates. The shift toward "delete what you legally can" in 2025 helps mitigate runaway growth, but baseline compliance requirements remain substantial.

#### Regulatory Drivers
- **HIPAA**: Technical safeguards for PHI
- **PCI-DSS**: Content moderation for payment data
- **EU AI Act**: Prohibited practices, high-risk controls
- **NIST AI RMF**: Threat categories and mitigations

**Sources:** [IBM AI Guardrails 2025](https://www.ibm.com/think/topics/ai-guardrails), [Help Net Security OpenGuardrails](https://www.helpnetsecurity.com/2025/11/06/openguardrails-open-source-make-ai-safer/)

---

### Layer 10: Agentic UI & Middleware

**Compute Intensity: Low**

#### MCP Server Requirements
| Scale | CPU Cores | RAM | Storage |
|-------|-----------|-----|---------|
| Small | 4-8 | 16-32 GB | 256-512 GB |
| Medium | 16-32 | 64-128 GB | 1-2 TB |

#### Protocol Updates (2025)
- **June 2025**: OAuth-based authorization, elicitation for server-initiated interactions
- **2025-03-26 spec**: Streamable HTTP transport for serverless compatibility
- Transport: JSON-RPC 2.0 over stdio or HTTP (+SSE)
- Security concerns: Prompt injection, tool permissions (April 2025 analysis)

#### Vercel AI SDK 5 (July 2025)
- SSE as standard for streaming
- Agentic Loop Control (stopWhen, prepareStep)
- Lightweight Agent class
- Text-to-speech and transcription support

#### On-Prem Difficulty: 2/5 (Moderate)
- Minimal infrastructure overhead
- Any Node.js platform can host MCP servers
- Newer transport protocols enable serverless
- Security considerations require careful implementation

#### Storage Intensity: Low

Layer 10 represents the lowest storage intensity in the GenAI stack, focused primarily on ephemeral session state and lightweight middleware coordination rather than large-scale data persistence.

##### Storage Requirements by Component

| Component | Storage Size | Persistence Duration | Scaling Considerations |
|-----------|--------------|---------------------|----------------------|
| MCP Server State | 100-500 MB per server | Session-scoped (ephemeral) | In-memory dictionaries; lost on restart |
| MCP Server State (Production) | 1-10 GB per deployment | Short-term (hours to days) | Redis/Firestore for distributed systems |
| UI Session Storage | 1-5 MB per session | Active session only | Automatic cleanup on disconnect |
| Vercel AI SDK Cache | Varies by usage | TTL-based (minutes to hours) | KV store (Upstash/Redis); cache hit 95-98% |
| Frontend Assets (CDN) | 10-100 MB per app | Long-term (months to years) | Edge caching, instant invalidation |
| WebSocket/SSE State | <1 MB per connection | Connection lifetime | No persistent state needed for SSE |

##### Storage Architecture Details

**MCP Server State Management:**
- **Development/Testing**: In-memory storage using dictionaries and objects with zero persistence
- **Production**: External stores (Redis, Firestore) for cross-server context sharing
- **Credentials Storage**: 88% of 5,200+ MCP servers require credentials, typically stored as environment variables (not in persistent storage)
- **Data Retention**: Background jobs periodically archive old context to cold storage (S3, Google Cloud Storage) based on TTL policies

**Vercel AI SDK Caching:**
- **Language Model Middleware**: Caches responses in KV storage (Upstash Redis recommended)
- **Cache Storage**: Tool-level caching for Anthropic prompt caching reduces token usage by 60-80% in long sessions
- **Vercel 2025 Marketplace Shift**: First-party KV/Postgres sunset; now integrates with Neon, Upstash, Supabase
- **Cache Hit Rates**: 95-98% with simple-cached-firestore wrapper, significantly reducing read costs

**Session Storage Patterns:**
- **Agentic Systems (Google ADK)**: In-memory for development; Redis/Firestore for production with per-request state retrieval
- **Microsoft Agent Framework**: SQLite for chat history with periodic state snapshots per session
- **Solace Agent Mesh**: Multiple backends (Filesystem, Redis, SQL, MongoDB) for session persistence
- **Storage Size**: Short-term memory stores "last few thousand tokens"; long-term via vector DBs (covered in Layer 4)

**WebSocket vs SSE Storage:**
- **WebSocket**: Requires persistent connection state management, pub/sub infrastructure, sticky sessions for scaling
- **SSE (2025 Comeback)**: No persistent connection state; uses standard HTTP infrastructure; auto-reconnection reduces state complexity
- **Memory Efficiency**: SSE discards processed messages vs WebSocket buffering entire response history
- **Scaling**: SSE leverages existing CDNs/load balancers; WebSocket needs dedicated pub/sub controller

**Frontend Asset Storage:**
- **Cloud Storage Backbone**: AWS S3, Google Cloud Storage, Azure Blob (industry standard for static assets)
- **CDN Requirements**: Global edge caching (Cloudflare, Akamai, AWS CloudFront) for latency reduction
- **Asset Types**: JavaScript bundles, images, stylesheets, videos (10-100 MB total per application)
- **Cache Control**: Netlify/Vercel provide granular TTL policies with atomic deploys and instant cache invalidation
- **Security**: WAF, DDoS protection, CSP headers for XSS prevention

**MCP Gateway Middleware:**
- **Centralized Routing**: Unified gateway endpoint for all agent requests
- **Session Continuity**: Shared memory and scoped session data for context tracking
- **Storage Backend**: Minimal overhead; primarily in-memory routing with optional Redis for distributed deployments

##### Storage Scaling Metrics (2025 Context)

**Agentic AI Network Impact:**
- Agentic AI queries generate **25x more network traffic** than chatbots, but storage remains minimal
- KV cache strategies and storage optimization central to multi-agent performance
- Primary bottleneck is **throughput and latency**, not storage capacity

**Infrastructure Comparison:**
- **Layer 10 (UI/Middleware)**: 1-10 GB typical deployment
- **Layer 4 (Vector/Graph DBs)**: 100s of GB to TBs (100-1000x more storage)
- **Layer 3 (AI Models)**: 10-100 GB per model, hundreds of GB for datasets

##### Cost and Deployment Considerations

**Storage Costs (Minimal):**
- Redis/Upstash KV: $10-50/month for typical session storage
- CDN/S3 for assets: $5-20/month for small-to-medium apps
- Firestore: Often within free tier for session-only storage (auto-deletion reduces costs vs long-term storage)

**Serverless Compatibility:**
- 2025 MCP streamable HTTP transport enables serverless deployment
- SSE works natively with serverless functions (no persistent connection state)
- Frontend asset hosting on Netlify/Vercel: automatic scaling, zero storage management

**On-Premises Storage Impact:**
- Negligible storage infrastructure required beyond existing Redis/PostgreSQL
- CDN optional for on-prem; can use local asset serving
- Primary challenge is **networking/bandwidth**, not storage capacity

##### Key 2025 Insights

1. **Storage is Not the Constraint**: Layer 10 focuses on coordination and streaming; heavy data persistence occurs in Layers 4 (vector DBs) and 3 (models)

2. **Ephemeral by Design**: SSE/WebSocket connections and MCP server state are session-scoped; automatic cleanup prevents storage bloat

3. **Caching as Performance Tool**: Vercel AI SDK caching reduces LLM API costs (50% savings) through smart KV storage, not as primary data store

4. **2025 SSE Renaissance**: Server-Sent Events eliminate persistent connection state requirements, reducing storage/memory overhead vs WebSocket

5. **Middleware Storage Minimal**: MCP Gateway and AG-UI protocol add negligible storage; routing and session tracking use in-memory structures

**Sources:**
- [Apipark MCP Server Setup 2025](https://apipark.com/techblog/en/how-to-set-up-your-own-mcp-server-a-step-by-step-guide/)
- [Astrix MCP Security Report 2025](https://astrix.security/learn/blog/state-of-mcp-server-security-2025/)
- [SuperAGI MCP Performance Optimization 2025](https://superagi.com/top-10-advanced-techniques-for-optimizing-mcp-server-performance-in-2025/)
- [Medium: MCP Memory and State Management 2025](https://medium.com/@parichay2406/mcp-memory-and-state-management-8738dd920e16)
- [Vercel AI SDK Caching Docs](https://ai-sdk.dev/docs/advanced/caching)
- [Vercel AI SDK 5 Announcement](https://vercel.com/blog/ai-sdk-5)
- [Vercel Storage Marketplace 2025](https://community.vercel.com/t/news-cache-2025-10-27/26236)
- [DEV: SSE vs WebSockets 2025](https://dev.to/haraf/server-sent-events-sse-vs-websockets-vs-long-polling-whats-best-in-2025-5ep8)
- [PortalZINE: SSE's Comeback 2025](https://portalzine.de/sses-glorious-comeback-why-2025-is-the-year-of-server-sent-events/)
- [Debut Infotech Real-Time Web Apps 2025](https://www.debutinfotech.com/blog/real-time-web-apps)
- [AG-UI Protocol GitHub](https://github.com/ag-ui-protocol/ag-ui)
- [Solace Agent Mesh Memory 2025](https://solace.com/blog/long-term-memory-agentic-ai-systems/)
- [Google Cloud ADK Architecture](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)
- [Microsoft Semantic Kernel AG-UI 2025](https://devblogs.microsoft.com/semantic-kernel/the-golden-triangle-of-agentic-development-with-microsoft-agent-framework-ag-ui-devui-opentelemetry-deep-dive/)
- [Microsoft Research Magentic-UI 2025](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/07/magentic-ui-report.pdf)
- [MCP Gateway Research 2025](https://research.aimultiple.com/mcp-gateway/)
- [Last9 Azure CDN 2025](https://last9.io/blog/azure-cdn-for-static-assets-apis-and-front-door/)
- [Cloudinary Advanced CDN Docs](https://cloudinary.com/documentation/advanced_url_delivery_options)
- [SiliconANGLE Agentic AI Storage 2025](https://siliconangle.com/2025/08/13/supermicro-partners-tackle-storage-challenges-agentic-ai-openstoragesummit/)
- [AWS Agentic AI Innovations 2025](https://www.aboutamazon.com/news/aws/aws-summit-agentic-ai-innovations-2025)
- [DigitalDefynd Scaling Agentic AI 2025](https://digitaldefynd.com/IQ/challenges-in-scaling-agentic-ai-systems/)
- [Medium: AI Agent Memory Management 2025](https://medium.com/@nomannayeem/building-ai-agents-that-actually-remember-a-developers-guide-to-memory-management-in-2025-062fd0be80a1)
- [TransOrg Conversational State 2025](https://www.transorg.ai/blog/conversational-state-and-memory-in-generative-ai-agents/)
- [Google Cloud Firestore Sessions](https://cloud.google.com/nodejs/getting-started/session-handling-with-firestore)
- [Google Cloud Memorystore](https://cloud.google.com/memorystore)
- [Medium: Simplified Firestore with Redis](https://medium.com/weekly-webtips/simplified-firestore-with-redis-3dc54cdc3ce9)

#### Regulatory Drivers
- **Shadow AI Risks**: 66 GenAI apps per enterprise average, 10% high-risk
- **CCPA/GDPR**: Consumer-facing transparency, opt-out
- **Attorney-Client Privilege**: Public AI platforms pose disclosure risks
- **State AI Laws**: Disclosure requirements for government/healthcare AI

**Sources:** [SimpleScraper MCP Guide 2025](https://simplescraper.io/blog/how-to-mcp), [Auth0 MCP Spec Update 2025](https://auth0.com/blog/mcp-specs-update-all-about-auth/), [Vercel AI SDK 5](https://vercel.com/blog/ai-sdk-5)

---

### Layer 11: Development Environment & SaaS Application Logic

**Compute Intensity: Low-Medium (CPU-Based)**

*Note: Unlike GPU-intensive LLM inference (Layer 2) or model training (Layer 3), SaaS application logic runs on standard CPU infrastructure. Relative to other layers: 4/10 intensity vs 10/10 for LLM inference.*

#### The Reality: Cloud-Only in 2025

Modern SaaS platforms (Databricks, Snowflake, Salesforce) have **eliminated true on-premise deployment** in favor of cloud-native architectures.

| Platform | On-Prem Available? | Hybrid Options | Notes |
|----------|-------------------|----------------|-------|
| Databricks | **NO** | VNet injection + ExpressRoute | Data stays in customer VPC |
| Snowflake | **NO** | Virtual Private Snowflake | Still cloud-hosted, dedicated infrastructure |
| Salesforce Hyperforce | **NO** | None | Pure cloud model, eliminated on-prem hardware 2025 |
| ServiceNow | **NO** | VPN connectivity | Cloud-only since 2019 |

#### Infrastructure Requirements (If Self-Hosting Equivalent)

| Component | Small | Medium | Enterprise |
|-----------|-------|--------|------------|
| CPU Cores | 32-64 | 128-256 | 512+ |
| RAM | 128-256 GB | 512 GB - 1 TB | 2+ TB |
| Storage | 10-50 TB NVMe | 100-500 TB | Petabyte-scale |
| Network | 10 Gbps | 25-40 Gbps | 100+ Gbps |
| Kubernetes Clusters | 1-2 | 3-5 | 10+ |

#### On-Prem Difficulty: 5/5 (Extremely Difficult/Not Available)

**Why vendors don't offer on-prem:**
- **Architecture complexity**: These platforms are built cloud-native with hundreds of microservices
- **Continuous updates**: SaaS model allows weekly/daily releases; on-prem requires manual patching
- **Support burden**: On-prem requires dedicated customer success engineering
- **Economies of scale**: Multi-tenant cloud is 2-5x more cost-efficient

**What customers must manage if self-hosting alternatives:**
- Full Kubernetes cluster administration
- Database administration (PostgreSQL, distributed stores)
- Networking, load balancing, service mesh
- Security patching and vulnerability management
- Disaster recovery and backup
- Team: 5-15+ FTEs for equivalent self-managed platform

#### Storage Intensity: Medium to High

Development environment and SaaS application logic layers require diverse storage types spanning platform data storage, container registries, application databases, logs/metrics, and CI/CD artifacts. Storage demands scale significantly with enterprise deployment.

##### SaaS Platform Storage Requirements

| Platform | Storage Type | Pricing (2025) | Typical Enterprise Scale | Data Growth Characteristics |
|----------|-------------|----------------|--------------------------|----------------------------|
| **Snowflake** | Active data storage | $23-40/TB/month (compressed) | Multi-TB to PB scale | 3-5x compression; Time Travel + Fail-safe add 2-3x overhead |
| **Databricks** | Workspace + Unity Catalog | DBU + cloud storage costs | Exabyte-scale (Microsoft deployments) | Delta Lake ACID transactions; frequent checkpoint writes |
| **Salesforce** | Data + File storage | $125/500MB data; $33/10GB file | 10GB base + 20MB/user (data); 10GB + 2-612MB/user (file) | Storage alerts at 100%; impacts record creation at limit |

**Snowflake Storage Details:**
- **Active storage:** $23/TB/month (US regions, compressed)
- **Time Travel storage:** Same as active storage rates; 90-day retention can triple costs
- **Fail-safe storage:** ~$25/TB/month for 7-day post-Time Travel recovery
- **Data transfer (egress):** $90/TB (AWS US East), $87.50/TB (Azure East US 2), $120-190/TB (GCP US East 4)
- **Compression efficiency:** 3-5x reduction vs uncompressed data
- **Typical workload split:** 80% compute costs, 20% storage/transfer costs

**Databricks Storage Details:**
- **Workspace storage:** Default storage for notebooks, job runs, command results, Spark logs
- **Unity Catalog:** Centralized governance for data/AI assets across workspaces
- **Serverless workspaces (2025):** Pre-configured with serverless compute and default storage
- **Lakehouse architecture:** Delta Lake provides ACID transactions on data lakes
- **Pricing model:** DBU (compute) + DSU (storage) consumption-based billing
- **Enterprise scale:** Microsoft AI datacenters use exabytes of storage for Databricks workloads

**Salesforce Storage Details:**
- **Default allocation:** 10GB data + 10GB file storage per org
- **Per-user allocation:** 20MB data/user + 2MB-2GB file/user (license-dependent)
- **Additional storage costs:** $125/month per 500MB data block; $33/month per 10GB file block
- **Storage limit enforcement:** 110% soft limit triggers alerts; 100% hard limit blocks record creation/editing
- **Big Objects:** 1 million records included per org for large datasets

##### Container Registry Storage

| Registry Type | Storage Requirements | Image Lifecycle Management | Enterprise Considerations |
|--------------|---------------------|---------------------------|--------------------------|
| **Harbor (Self-hosted)** | 40GB+ baseline | Retention policies, tag expiration | 2 vCPU, 4GB RAM minimum; CNCF graduated project |
| **JFrog Artifactory** | TB-scale for largest enterprises | Automatic cleanup, lifecycle rules | Powers TBs of data/day for Fortune 500 |
| **Amazon ECR** | Pay-per-GB stored | Configurable lifecycle policies | S3-backed, multi-AZ replication, cross-region support |
| **Docker Hub** | Free tier limited | Manual cleanup required | Rate limits necessitate enterprise tiers |

**Storage Growth Drivers:**
- Frequent CI/CD builds create image sprawl without lifecycle policies
- Base images + layer caching strategies impact total storage
- Multi-architecture images (amd64, arm64) multiply storage requirements
- Vulnerability scanning metadata adds overhead

**Best Practices:**
- Retention policies: Auto-expire untagged images after 7-30 days
- Tag strategies: Semantic versioning reduces orphaned images
- Scheduled cleanup: CI workflows or cron jobs prune unused artifacts
- Registry quotas: Prevent runaway growth from misconfigured pipelines

##### Application Database Storage

| Database | Storage Architecture | Performance Profile | Enterprise Scale |
|----------|---------------------|-------------------|------------------|
| **PostgreSQL** | Disk-based (ACID) | Efficient caching (shared buffers); most queries avoid disk with proper tuning | 100s GB to multi-TB; can cache in-memory for hot data |
| **Redis** | In-memory (optional persistence) | Millions of ops/sec; sub-millisecond latency | GB to 100s GB; can scale to 1M+ RPS with ElastiCache Serverless |

**Hybrid Usage Pattern (2025 Best Practice):**
- **PostgreSQL:** Primary transactional database for e-commerce, CMS, financial apps
- **Redis:** Caching layer for SQL query results, session storage, pub/sub messaging
- **Combined approach:** Redis reduces PostgreSQL load by 50-80% for read-heavy workloads
- **Benchmark context:** Modern PostgreSQL can serve 7,425 req/sec (>500M req/day) on 10-year-old hardware for caching use cases

**Scaling Strategies:**
- **PostgreSQL:** Connection pooling (PgBouncer), read replicas, logical replication
- **Redis:** Horizontal scaling via auto-sharding; ElastiCache doubles capacity every 10 minutes
- **Data persistence:** Redis RDB snapshots and AOF logs add storage overhead

##### Log Aggregation & Metrics Storage

| System | Storage Backend | Retention Strategy | Enterprise Scale |
|--------|----------------|-------------------|------------------|
| **Grafana Loki** | Object storage (S3, GCS, Azure Blob) | Petabyte-scale with compression | Indexes metadata only (not log contents); 10x cheaper than full-text indexing |
| **Grafana Mimir** | Object storage (Prometheus TSDB) | 1 billion+ active series | Long-term metrics storage with high availability |
| **ELK Stack** | Elasticsearch (columnar + inverted index) | Tiered storage (hot/warm/cold) | 10+ PB deployments (30% of cloud object stores); 60% log field reduction possible |
| **Prometheus** | Local TSDB | Configurable retention (default 15 days) | Time series database optimized for metrics, not logs |

**Grafana Enterprise Stack (2025):**
- **Loki:** Stores compressed, unstructured logs with metadata-only indexing
- **Mimir:** Scalable, multi-tenant TSDB for long-term Prometheus metrics
- **Storage efficiency:** 100% persistence to object storage (S3, GCS, Blob)
- **Retention policies:** Critical for cost control; indefinite retention causes disk bloat
- **Integration:** Native Prometheus/K8s integration for seamless metrics-logs-traces

**ELK Stack (2025):**
- **Elasticsearch:** Columnar store for numerical time series + inverted index for full-text search
- **Storage scale:** 70-75% of cloud-native enterprise data in object storage
- **Compression:** Essential for long-term log retention
- **AWS integration:** CloudWatch, Lambda, Elasticsearch Service for centralized logging
- **Success metrics:** Wells Fargo minimized log fields by 60%; Equinox reduced observability costs by 80%

**Storage Best Practices:**
- **Retention policies:** 30-90 days for operational logs; 1-7+ years for compliance logs
- **Tiered storage:** Recent logs on NVMe/SSD; archived logs on object storage
- **Compression:** Loki/ELK both compress logs; Loki avoids full-text indexing overhead
- **Query optimization:** Metadata-based queries (Loki) vs full-text search (ELK) trade-offs

##### CI/CD Artifact Storage

| Platform | Default Storage Location | Size Limits (2025) | Retention Policies | Production Considerations |
|----------|-------------------------|-------------------|-------------------|--------------------------|
| **GitLab CI/CD** | `/var/opt/gitlab/gitlab-rails/shared/artifacts` | 100MB per artifact file | 30 days default expiration | Object storage (S3, Azure Blob) recommended; most recent successful pipeline artifacts kept indefinitely |
| **Jenkins** | Workspace directories | No default limit | Manual cleanup required | Requires external Artifactory (JFrog) for enterprise artifact management |
| **GitHub Actions** | GitHub-hosted storage | Varies by plan | Configurable per workflow | Artifact retention tied to workflow configuration |
| **JFrog Artifactory** | Configurable backend | Enterprise-scale (TBs) | Lifecycle policies | Centralized artifact repository for Docker, Maven, npm, etc. |

**GitLab Artifacts:**
- **Storage path:** Configurable via `gitlab_rails['artifacts_path']` (default: `/var/opt/gitlab/...`)
- **Size limit:** 100MB per artifact file (configurable)
- **Expiration:** Default 30 days; individual jobs can override via `expire_in`
- **Retention exception:** Most recent successful pipeline artifacts kept regardless of expiration
- **Object storage:** Recommended for production (S3, GCS, Azure Blob)

**Jenkins vs GitLab:**
- **Jenkins:** Uses `stash`/`unstash` for pipeline binaries; requires external Artifactory for persistence
- **GitLab:** Native `artifacts` concept with integrated storage backend
- **Migration pattern:** Jib containerization → JFrog Artifactory for versioned .jar files

**Storage Growth Drivers:**
- Build frequency: Daily builds accumulate artifacts rapidly
- Artifact types: Docker images, compiled binaries, test reports, code coverage
- Retention policies: Critical for preventing unbounded growth
- Multi-environment deployments: Dev/staging/production artifacts multiply storage needs

##### Storage Performance Summary

| Storage Component | Throughput Requirements | Latency Sensitivity | Capacity Range |
|------------------|------------------------|-------------------|----------------|
| **SaaS Platform Storage** | Moderate (batch analytics) | Low (query latency <5s acceptable) | TB to PB scale |
| **Container Registry** | High (parallel image pulls during deployment) | Medium (image pull time impacts deployment speed) | 100s GB to TB |
| **PostgreSQL** | High (OLTP workloads) | High (sub-100ms query targets) | 10s GB to TB |
| **Redis** | Very High (millions ops/sec) | Very High (sub-ms latency) | GB to 100s GB |
| **Log/Metrics Storage** | Moderate (streaming ingestion) | Low (historical queries) | TB to PB scale |
| **CI/CD Artifacts** | Moderate (build artifact storage) | Medium (deployment retrieval) | 100s GB to TB |

##### Overall Storage Intensity Rating: Medium to High

**Justification:**
- **Lower than GPU/model layers:** No multi-TB model weights or petabyte training datasets
- **Higher than observability/UI layers:** SaaS platforms (Snowflake, Databricks) require multi-TB to PB storage at enterprise scale
- **Significant growth rates:** Unstructured data grows 26-65% annually (IDC/enterprise surveys)
- **Diverse storage tiers:** Requires hot storage (Redis, PostgreSQL), warm storage (container registries, logs), and cold storage (archives, compliance)
- **Cost drivers:** Snowflake Time Travel can triple storage costs; ELK full-text indexing is 10x more expensive than Loki metadata indexing
- **Enterprise scale examples:** Microsoft AI datacenters (exabytes for Databricks); 30% of cloud deployments exceed 10 PB

**Key 2025 Findings:**
- **Cloud-native dominance:** 70-75% of enterprise data in object storage
- **Compression critical:** Snowflake achieves 3-5x compression; Loki stores compressed unstructured logs
- **Lifecycle management:** Retention policies prevent runaway growth (GitLab 30-day default, Salesforce 110% soft limits)
- **Hybrid patterns:** PostgreSQL (primary) + Redis (cache) reduces storage and improves performance
- **Regulatory impact:** HIPAA (6 years), financial services (7+ years), EU AI Act drive long-term storage requirements

**Sources:** [Snowflake Pricing Guide 2025](https://mammoth.io/blog/snowflake-pricing/), [Snowflake Storage Costs 2025](https://www.chaosgenius.io/blog/snowflake-storage-costs/), [Keebo Snowflake Pricing 2025](https://keebo.ai/2025/01/28/snowflake-pricing/), [Databricks Pricing 2025](https://mammoth.io/blog/databricks-pricing/), [Databricks Data Management 2025](https://www.integrate.io/blog/mastering-data-lifecycle-databricks-data-management-demystified/), [Bain Databricks Summit 2025](https://www.bain.com/insights/databricks-data-and-ai-summit-2025-enterprise-intelligence-platforms-come-into-view/), [Salesforce Storage Limits 2025](https://www.owndata.com/blog/best-ways-to-manage-salesforce-storage-limits), [Gearset Salesforce Storage 2025](https://gearset.com/blog/how-to-reduce-and-manage-your-salesforce-data-storage-costs/), [Harbor Container Registry 2025](https://www.cncf.io/blog/2025/12/08/harbor-enterprise-grade-container-registry-for-modern-private-cloud/), [Shipyard Container Registries 2025](https://shipyard.build/blog/container-registries/), [JFrog Container Registry 2025](https://jfrog.com/container-registry/), [Redis vs PostgreSQL 2025](https://www.movestax.com/post/redis-vs-postgresql-which-database-fits-your-needs), [PostgreSQL Caching 2025](https://dizzy.zone/2025/09/24/Redis-is-fast-Ill-cache-in-Postgres/), [Red Hat Redis PostgreSQL 2025](https://developers.redhat.com/articles/2025/08/06/intro-redis-and-postgresql-red-hat-sap-environments), [GitLab CI/CD Artifacts 2025](https://docs.gitlab.com/ci/jobs/job_artifacts/), [GitLab Artifacts Admin 2025](https://docs.gitlab.com/administration/cicd/job_artifacts/), [DevOps CI/CD Pipelines 2025](https://www.kunal-chowdhury.com/2025/07/devops-ci-cd-pipelines.html), [Grafana Loki 2025](https://grafana.com/oss/loki/), [Grafana Mimir 2025](https://grafana.com/oss/mimir/), [Loki Prometheus Retention 2025](https://medium.com/@faithsodipe/log-and-metric-retention-in-loki-and-prometheus-57e81bbad023), [Elastic Observability 2025](https://www.elastic.co/observability), [ELK Stack Guide 2025](https://prepare.sh/articles/the-definitive-guide-to-the-elk-stack-in-2025-from-zero-to-production-ready-observability), [MinIO Enterprise Storage 2025](https://www.min.io/learn/enterprise)

#### Total Cost of Ownership Comparison

| Model | Year 1 | Year 3 | Notes |
|-------|--------|--------|-------|
| Cloud SaaS | $100K-$500K | $300K-$1.5M | Predictable, fully managed |
| On-Prem Equivalent | $500K-$2M | $1.5M-$6M | Hardware + 50-85% personnel costs |
| Hybrid/Repatriation | $300K-$1M | $900K-$3M | Select workloads only |

**Key insight:** Personnel costs represent 50-85% of on-prem TCO, making self-hosting >2x cloud SaaS.

#### Drivers for On-Prem/Repatriation (Despite Difficulty)

| Driver | % of CIOs | Example Companies |
|--------|-----------|-------------------|
| Cloud cost overruns | 86% planning repatriation | GEICO (2.5x cost increase) |
| Data sovereignty | 97% mid-market (EU) | Barclays survey |
| AI data gravity | Growing | 463 exabytes/day generated |
| Security concerns | 71% (healthcare) | Health IT leaders |
| Cost optimization at scale | Significant | 37signals ($2M/yr savings), Akamai (~$100M/yr) |

**Reality check:** <10% do full repatriation; most repatriate **select workloads only**
- Cloud: Elastic/bursty workloads
- On-prem: Steady high-utilization, latency-sensitive, regulated workloads

#### Regulatory Drivers for On-Prem/Private Cloud

| Regulation | Requirement | Affected Industries |
|------------|-------------|---------------------|
| EU DORA (2025) | ICT risk management, third-party oversight | Financial services |
| EU NIS2 (2025) | Critical infrastructure cybersecurity | Energy, transport, health |
| EU Data Act (2025) | Data portability, cloud switching | All industries |
| China PIPL | "Important data" in-country processing | China operations |
| HIPAA | PHI protection, BAA requirements | Healthcare |
| FedRAMP IL4+ | Government data residency | Government contractors |

#### Hybrid Deployment Patterns

**Pattern 1: Control Plane Cloud / Data Plane On-Prem**
- Databricks VNet injection: Platform logic in cloud, data stays in customer VPC
- Reduces data egress costs and sovereignty concerns

**Pattern 2: Workload-Based Split**
- Bursty/experimental: Cloud
- Steady-state production: On-prem
- Example: 37signals moved steady workloads, kept burst capacity in cloud

**Pattern 3: Managed Private Cloud**
- Dedicated single-tenant cloud infrastructure
- Snowflake Virtual Private Snowflake, Salesforce Hyperforce
- Cloud-managed but isolated

**Sources:** [Barclays Cloud Repatriation Survey 2025](https://research.barclays.com), [37signals Cloud Exit 2025](https://world.hey.com/dhh/we-have-left-the-cloud-251760fb), [Gartner Cloud Repatriation 2025](https://www.gartner.com/en/articles/cloud-repatriation), [EU DORA Compliance 2025](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/information-and-communication-technology-ict)

---

## Regulatory Requirements Matrix

### When On-Premises is Required

| Requirement | Affected Layers | Regulations |
|-------------|-----------------|-------------|
| Classified data (IL6+) | 1, 2, 3, 4, 5, 9, 11 | FedRAMP, ITAR |
| PHI processing (training) | 1, 2, 3, 4, 6, 9, 11 | HIPAA |
| Payment card data | 2, 4, 9, 10, 11 | PCI-DSS v4.0.1 |
| China "important data" | 1, 3, 4, 11 | PIPL |
| Attorney-client privilege | 2, 3, 4, 5, 9, 11 | Bar ethics rules |
| Defense AI models | 1, 2, 3, 11 | ITAR |
| Air-gapped environments | All | Various |
| EU DORA/NIS2 compliance | 1, 4, 9, 11 | EU Digital regulations |

### When On-Premises is Strongly Recommended

| Requirement | Affected Layers | Regulations |
|-------------|-----------------|-------------|
| EU high-risk AI systems | 3, 4, 7, 8, 9 | EU AI Act |
| Proprietary trading algorithms | 2, 3, 4, 7 | SEC, OCC |
| SOX-controlled AI | 3, 7, 8 | SOX |
| Healthcare clinical trials | 2, 3, 4, 6 | HIPAA, FDA |
| High-volume ADMT (CA/CO) | 4, 7, 9, 10 | CCPA, Colorado AI Act |

### Cloud Acceptable with Controls

| Use Case | Required Controls |
|----------|-------------------|
| General business analytics | Standard enterprise security |
| Customer service (non-privileged) | BAA if applicable |
| Marketing/sales AI | Privacy policy compliance |
| Public-facing applications | Content moderation |
| Development/testing | Non-sensitive data only |
| Unclassified government | FedRAMP authorization |

---

## Recommendations for Hybrid Deployment

### Prioritize On-Premises
1. **AI Models** - For IP protection and data sovereignty
2. **Data & Storage** - For regulated data (PHI, PII, payment)
3. **Security & Governance** - For audit compliance and control

### Cloud-Friendly Layers
1. **Agent Frameworks** - Low infrastructure overhead
2. **Observability** - SaaS options mature and cost-effective
3. **Agentic UI** - Serverless-compatible with newer protocols

### Hybrid Approach
1. **Deployment & Inference** - Scale-out in cloud, sensitive workloads on-prem
2. **Data Pipelines** - Control plane SaaS, workers on-prem
3. **Memory Systems** - Depends on data sensitivity

---

## Key 2025 Sources

### Infrastructure
- [Introl GPU Deployment Guide 2025](https://introl.com/blog/h100-vs-h200-vs-b200-choosing-the-right-nvidia-gpus-for-your-ai-workload)
- [CMU AI Data Center Cooling 2025](https://www.cmu.edu/news/stories/archives/2025/february/slashing-ai-data-center-cooling-cost-and-gpucpu-power-use)

### Regulatory
- [EU AI Act Implementation 2025](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [HIPAA Security Rule Update (Jan 2025)](https://www.sprypt.com/blog/hipaa-compliance-ai-in-2025-critical-security-requirements)
- [FedRAMP 20x Initiative (Aug 2025)](https://www.gsa.gov/about-us/newsroom/news-releases/gsa-fedramp-prioritize-20x-authorizations-for-ai-08252025)
- [NIST AI RMF 2025 Updates](https://www.ispartnersllc.com/blog/nist-ai-rmf-2025-updates-what-you-need-to-know-about-the-latest-framework-changes/)

### On-Premises Deployment
- [vLLM vs TensorRT-LLM Comparison 2025](https://itecsonline.com/post/vllm-vs-ollama-vs-llama.cpp-vs-tgi-vs-tensort)
- [Langfuse Self-Hosting Guide 2025](https://langfuse.com/self-hosting)
- [LangGraph Platform GA 2025](https://blog.langchain.com/langgraph-platform-ga/)

---

*This analysis consolidates research from 6 specialized agents examining 2025 sources across 11 infrastructure layers, deployment complexity, and regulatory compliance.*
