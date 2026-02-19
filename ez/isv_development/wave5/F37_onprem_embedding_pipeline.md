# F37: On-Premises Embedding Pipeline Operations

## Executive Summary

Operating embedding generation pipelines on-premises requires ISVs to own the full operational stack that managed APIs abstract away: GPU procurement and scheduling, model lifecycle management, failure recovery, and quality monitoring. Self-hosted embedding models such as BGE-M3 and Instructor-XL can match or exceed managed API quality while eliminating per-token charges, but they introduce substantial engineering overhead across four distinct operational domains — model serving, batch orchestration, lifecycle versioning, and observability. The GPU resource contention problem is particularly acute on-premises because embedding workloads must compete with LLM inference for the same physical hardware, requiring deliberate scheduling and partitioning strategies. At scale, re-embedding an entire corpus when an embedding model changes is one of the highest-cost, highest-risk operations in the RAG infrastructure lifecycle and demands a parallel-index migration discipline that does not exist in managed API environments.

---

## 1. Self-Hosted Embedding Models: Deployment and GPU Requirements

### 1.1 Model Landscape

The primary open-source embedding models an ISV would deploy on-premises in 2025 span a wide range of sizes, capabilities, and resource requirements:

| Model | Parameters | Dimensions | MTEB Score | VRAM (fp16) | License |
|-------|-----------|-----------|------------|-------------|---------|
| all-MiniLM-L6-v2 | 22.7M | 384 | ~56 | ~43 MB | Apache 2.0 |
| BGE-M3 | 568M | 1024 | 63.0 | ~1.06 GB | MIT |
| Instructor-XL | 1.5B | 768 | ~66+ | ~3 GB+ | Apache 2.0 |
| Qwen3-Embedding-8B | 8B | 4096 | 70.58 | ~16 GB | Apache 2.0 |

Sources:
- BGE-M3 parameters and dimensions: [BAAI/bge-m3 Hugging Face Model Card](https://huggingface.co/BAAI/bge-m3)
- BGE-M3 VRAM: [BAAI/bge-m3 Automated Model Memory Requirements](https://huggingface.co/BAAI/bge-m3/discussions/64)
- all-MiniLM-L6-v2 memory: [sentence-transformers/all-MiniLM-L6-v2 Memory Requirements](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/39)
- Instructor-XL GPU test: [hkunlp/instructor-xl OOM discussion](https://huggingface.co/hkunlp/instructor-xl/discussions/14)
- Qwen3-Embedding-8B MTEB score: [Best Embedding Models 2025 — Ailog RAG Guide](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)

[STATISTIC] "BGE-M3: 568 million parameters, 1024-dimensional embeddings, MTEB Score 63.0, free under MIT license"
— [Best Embedding Models 2025](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)
Date: 2025

[STATISTIC] "Qwen3-Embedding-8B scores 70.58 on the MTEB Multilingual leaderboard, with data updated in January 2026"
— [Choosing an Embedding Model — Ailog RAG](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)
Date: 2026

### 1.2 Serving Stack

[FACT] NVIDIA NeMo Retriever Embedding NIM "incorporates CUDA, TensorRT, and Triton to offer out-of-the-box GPU acceleration" and is "optimized for high-performance deep learning inference with NVIDIA TensorRT and NVIDIA Triton Inference Server."
— [NVIDIA NeMo Retriever Embedding NIM Overview](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/overview.html)
Date: 2025

[FACT] For Kubernetes-native self-hosted embedding: "KServe is used to host embedding inference models, Envoy AI Gateway securely exposes the inference model" with InferenceService as the standard resource for deploying models behind a stable URL.
— [Cloud-Native RAG: embeddings + vectors, fully self-hosted — Medium](https://medium.com/h7w/cloud-native-rag-embeddings-vectors-fully-self-hosted-82d57142353e)
Date: 2025

[FACT] NVIDIA NIM throughput optimization: "When set to throughput optimized mode, the NIM optimizes for maximum throughput on long sequence length and high batch size workloads, providing upwards of 2x performance when used with large batches containing 64-1000 long and diverse length sequences."
— [NVIDIA NeMo Retriever Embedding NIM Configuration](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/configuration.html)
Date: 2025

[FACT] "For production deployments, int8 embedding type is recommended and provides a balance of compression and accuracy, while reducing memory usage by a factor of four compared to float embeddings while maintaining high retrieval accuracy."
— [NVIDIA NeMo Retriever Embedding NIM Configuration](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/configuration.html)
Date: 2025

### 1.3 CPU vs GPU Inference Trade-offs

[FACT] For CPU-optimized inference, sentence-transformers with ONNX-qint8 quantization achieves "approximately 3.1x speedup on short texts with int8 quantization" relative to baseline fp32.
— [Speeding up Inference — Sentence Transformers Documentation](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)
Date: 2025

[FACT] A quantized e5-large-v2 ONNX model running on CPU achieves "embedding computation in approximately 10ms — significantly faster than any cloud API."
— [Benchmarking API Latency of Embedding Providers — Nixiesearch](https://nixiesearch.substack.com/p/benchmarking-api-latency-of-embedding)
Date: 2025

[FACT] Sentence-transformers GPU optimization decision framework: "GPU + short text: Use ONNX-O4; GPU + long text: Use PyTorch fp16/bf16; CPU + accuracy critical: OpenVINO baseline; CPU + speed priority: OpenVINO-qint8 or ONNX-qint8."
— [Speeding up Inference — Sentence Transformers Documentation](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)
Date: 2025

[FACT] "Using implementations like Infinity can accelerate BGE-M3 inference speed on GPU around 2-3x by using async tokenization, fp16, flash-attention, torch nested, and torch.compile."
— [BAAI/bge-m3 Optimize Inference Speed — Hugging Face](https://huggingface.co/BAAI/bge-m3/discussions/9)
Date: 2025

### 1.4 Production Serving Target

[STATISTIC] A single NVIDIA L4 GPU (16 GB VRAM) achieves "2,000 text tokens/second" throughput for the gte-Qwen2-7B-instruct embedding model.
— [Large-Scale AI Batch Inference: 9x Faster Embedding Generation — SkyPilot Blog](https://blog.skypilot.co/large-scale-embedding/)
Date: 2025

[STATISTIC] Production targets for sentence-transformers serving: "1,000+ predictions/sec" throughput with "<100ms latency" achieved on single-GPU Kubernetes deployment.
— [MLOps at Scale: Serving Sentence Transformers in Production — Don Simpson's Blog](https://www.donaldsimpson.co.uk/2025/12/11/mlops-at-scale-serving-sentence-transformers-in-production/)
Date: December 2025

---

## 2. Batch Embedding at Scale: Processing Millions of Documents

### 2.1 Architecture Requirements

Batch embedding of large corpora requires a fundamentally different architecture than real-time inference — one built around durable queues, checkpointed progress, GPU job scheduling, and failure isolation.

[FACT] Core batch pipeline components: "Dead-Letter Queues to move messages corresponding to persistently failing files to a separate queue for investigation, quarantine files to an error directory, and notify operators about persistent failures."
— [Best Practices for Error Handling, Monitoring, and Recovery — IJCTT Journal](https://www.ijcttjournal.org/2025/Volume-73%20Issue-4/IJCTT-V73I4P120.pdf)
Date: 2025

[FACT] Checkpoint recovery pattern: "When saving the offset, when the pipeline restarts, it will continue reading from the position where it left off rather than reprocessing all the items in the queue."
— [Dead Letter Queues: The Complete Developer-Friendly Guide](https://swenotes.com/2025/09/25/dead-letter-queues-dlq-the-complete-developer-friendly-guide/)
Date: September 2025

[FACT] For Celery-based GPU embedding workers, "teams must override Celery's default task behavior to load models once per worker process, rather than per task, though this still causes a cold start whenever new workers spin up, and models load multiple times if workers run multiple threads."
— [The Shortcomings of Celery + Redis for ML Workloads — Cerebrium](https://www.cerebrium.ai/articles/celery-redis-vs-cerebrium)
Date: 2025

### 2.2 Throughput at Scale

[STATISTIC] SkyPilot benchmark on ~30 million Amazon Reviews (books partition): single-region throughput of 47 L4 GPUs processing 20+ hours; multi-region scale-out to 406 L4 GPUs across 12 regions reduced processing time to 2.3 hours — a 9x speedup. Token throughput: 797.7k tokens/second. Embedding output: ~120 GB. Cost: $277 vs $710 single-region (61% savings).
— [Large-Scale AI Batch Inference: 9x Faster Embedding Generation — SkyPilot Blog](https://blog.skypilot.co/large-scale-embedding/)
Date: March 2025

[FACT] Model used in the benchmark: "Alibaba-NLP/gte-Qwen2-7B-instruct embedding model." Instance type: "AWS g6.xlarge (L4 GPU)." Embedding dimensions: "768-3072 per vector."
— [Large-Scale AI Batch Inference: 9x Faster Embedding Generation — SkyPilot Blog](https://blog.skypilot.co/large-scale-embedding/)
Date: March 2025

### 2.3 Queue Management Tooling

| Tool | Role | On-Prem Fit |
|------|------|-------------|
| Celery + Redis | Task queue, worker orchestration | Mature, Python-native; GPU model-loading limitations |
| Kafka | High-durability message stream | Best for very high volume; complex ops |
| RabbitMQ | Message broker with DLQ support | Simpler than Kafka; good for mid-scale |
| Kubernetes Jobs/CronJobs | GPU-aware batch job scheduling | Native K8s; requires custom progress tracking |
| NVIDIA Triton | GPU batch inference server | Throughput-optimized; integrates with NIM |

[FACT] "Production configuration includes JSON serialization for security, task acknowledgment after completion, worker prefetch multiplier settings for fair distribution, and result expiration cleanup."
— [Celery Complete Guide — DevToolbox](https://devtoolbox.dedyn.io/blog/celery-complete-guide)
Date: 2026

[FACT] "Automated pipelines can categorize dead-lettered messages by reason, apply automatic fixes where possible, resubmit recoverable messages with loop prevention, archive messages for audit trails, and alert teams when manual review is needed."
— [Kafka Dead Letter Queue Best Practices — Superstream](https://www.superstream.ai/blog/kafka-dead-letter-queue)
Date: 2025

---

## 3. Re-Embedding Workflows: Corpus Migration When Models Change

### 3.1 The Fundamental Problem

[QUOTE] "If we changed the embedding model in an existing search application, for example, the vector generated from a new user query wouldn't map cleanly to a vector space created by an older embedding model."
— [Different Embedding Models, Different Spaces: The Hidden Cost of Model Upgrades — Gary A. Stafford, Medium](https://medium.com/data-science-collective/different-embedding-models-different-spaces-the-hidden-cost-of-model-upgrades-899db24ad233)
Date: 2025

[FACT] "At a multi-million-document scale, a sudden model turndown can be costly" — operational overhead includes "re-embedding cycles, downtime, parallel infrastructure, change management, and downstream testing."
— [Different Embedding Models, Different Spaces — Medium](https://medium.com/data-science-collective/different-embedding-models-different-spaces-the-hidden-cost-of-model-upgrades-899db24ad233)
Date: 2025

### 3.2 Migration Strategies

Three principal strategies exist for corpus re-embedding migrations:

**Strategy 1: Full Re-Embedding**
Re-embed the entire corpus with the new model and rebuild the vector index from scratch. This is the simplest operationally but requires maximum compute time and parallel index capacity.

**Strategy 2: Dual-Index Routing**
Maintain parallel vector indexes — one for the old model, one for the new — routing queries to both during the migration window, then shifting all traffic to the new index when complete.

[FACT] Weaviate-specific implementation: "Collection aliases — switch pointers instantaneously with rollback capability" and "multiple vector versions — store both old and new embeddings in one collection for side-by-side comparison."
— [Different Embedding Models, Different Spaces — Medium](https://medium.com/data-science-collective/different-embedding-models-different-spaces-the-hidden-cost-of-model-upgrades-899db24ad233)
Date: 2025

**Strategy 3: Lazy Re-Embedding**
Embed queries with the new model while keeping old document embeddings, gradually re-embedding documents on access or in batches until the index is fully migrated. Reduces peak compute cost but extends the mixed-model period.

**Strategy 4: Adapter Layers (Emerging)**
[FACT] "Embedding-Converter provides a novel framework for efficiently transforming embeddings between different models, thus avoiding costly 're-embedding'. The system can handle a 50 million document corpus in under two hours, with inference alone taking only 20 minutes with openai-3-small, resulting in cost reductions exceeding 100x compared to directly generating target model embeddings."
— [Embedding-Converter: A Unified Framework for Cross-Model Embedding Transformation — ACL Anthology](https://aclanthology.org/2025.acl-long.1237/)
Date: ACL 2025

### 3.3 Decision Thresholds for Re-Embedding

[FACT] "For high-risk applications (e.g., healthcare, legal), a 5-8% improvement on critical metrics may justify migration, while for standard applications (e.g., customer support, e-commerce), 10-15% gains might be typically needed to warrant re-embedding costs."
— [Weaviate: When Good Models Go Bad](https://weaviate.io/blog/when-good-models-go-bad)
Date: 2025

---

## 4. Embedding Model Versioning: Tracking and Migration

### 4.1 Core Versioning Requirements

[FACT] "Explicit versioning involves tracking which embedding model (and version) generated each embedding. Embeddings should be treated as a versioned dependency: model changes imply re-embedding, migration strategy, and regression tests."
— [Weaviate: When Good Models Go Bad](https://weaviate.io/blog/when-good-models-go-bad)
Date: 2025

Every embedding stored in a vector database must carry metadata identifying:
1. The model name and version (e.g., `bge-m3-v1.5` vs `bge-m3-v2.0`)
2. The quantization type used at embedding time (fp32, fp16, int8)
3. The maximum sequence length used (affects truncation behavior)
4. The instruction prefix, if applicable (Instructor models, E5-Instruct)
5. A timestamp of when the embedding was generated

### 4.2 Model Registry Integration

[FACT] Production MLflow integration for embedding versioning uses: "MLflow for model versioning and registry management" with Kubernetes orchestration and FastAPI inference layer — enabling one-person operation of a 1.7 billion defect record embedding system.
— [MLOps at Scale: Serving Sentence Transformers in Production — Don Simpson's Blog](https://www.donaldsimpson.co.uk/2025/12/11/mlops-at-scale-serving-sentence-transformers-in-production/)
Date: December 2025

### 4.3 Operational Discipline Required

On-premises embedding versioning requires explicit engineering investment in:
- A model registry (MLflow, DVC, or custom) storing model artifacts with version hashes
- Metadata tags written at embedding time to every vector store record
- Automated regression tests comparing retrieval quality across model versions before migration
- Rollback-capable index alias management in the vector database layer

See [F45: Vector Database Operations] for coverage of index alias and schema management patterns.

---

## 5. Real-Time vs Batch: Infrastructure Split

### 5.1 The Two-Pipeline Problem

On-premises embedding infrastructure must typically serve two fundamentally different SLA profiles simultaneously. Combining them on shared hardware without explicit scheduling creates contention.

| Dimension | Real-Time Pipeline | Batch Pipeline |
|-----------|-------------------|----------------|
| Latency target | <100ms p95 | Hours acceptable |
| Trigger | Document ingestion event | Scheduled job or manual trigger |
| GPU allocation | Reserved capacity | Burst/opportunistic |
| Queue depth | Near-zero | 100K–100M documents |
| Failure mode | User-visible latency spike | Silent backlog accumulation |
| Checkpointing | Stateless (per-request) | Stateful (offset tracking) |

[FACT] "Critical user paths typically target 95th percentile latency under 200ms, 99th percentile latency under 500ms, and mean response time under 100ms."
— [Defining SLA/SLO-Driven Monitoring Requirements in 2025 — Uptrace](https://uptrace.dev/blog/sla-slo-monitoring-requirements)
Date: 2025

[FACT] "Batch inference and offline embedding indexing typically support higher latencies (over 100ms) without significantly affecting user experience or operational performance."
— [Solving AI Foundational Model Latency with Telco Infrastructure — arXiv](https://arxiv.org/html/2504.03708v1)
Date: 2025

### 5.2 Infrastructure Separation Patterns

**Pattern A: Dedicated GPU Pools**
Maintain separate Kubernetes node pools — one GPU node pool reserved exclusively for real-time embedding (low queue depth, HPA-controlled), and a second spot-instance pool for batch embedding jobs. This eliminates contention at the cost of peak inefficiency.

**Pattern B: Priority Queue Scheduling**
A single GPU pool with priority-weighted queues: real-time requests pre-empt batch jobs. Requires NVIDIA GPU scheduling primitives and custom scheduler configuration.

[FACT] "In high-traffic scenarios, both bursty inference requests and training tasks compete for shared resources, preempting subsequent inference tasks and risking SLO violations. Co-locating training and inference workloads on shared resources can mitigate inefficiencies inherent in separate resource allocation."
— [LLM Inference Scheduling: A Survey — TechRxiv](https://www.techrxiv.org/users/994660/articles/1355915/)
Date: October 2025

---

## 6. GPU Sharing: Embedding vs LLM Inference Contention

### 6.1 The Contention Problem

On-premises deployments face a structural conflict: LLM inference workloads are memory-bandwidth-bound and occupy large GPU memory partitions (often the full GPU for models >7B parameters), while embedding models are typically small enough to co-reside — but only if the infrastructure explicitly supports it.

### 6.2 NVIDIA GPU Sharing Technologies

[FACT] "MIG partitions single A100/H100 GPUs into up to seven isolated instances, each with dedicated high-bandwidth memory, cache, and compute cores." Hardware-backed isolation prevents LLM inference from starving embedding workloads.
— [GPU Memory Pooling and Sharing — Introl Blog](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025)
Date: 2025

[FACT] "Time-slicing rapidly alternates GPU access between processes but trades memory and fault isolation for broader sharing capability. A crash in one time-sliced workload can impact others, making it unsuitable for production inference requiring strict isolation."
— [GPU Memory Pooling and Sharing — Introl Blog](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025)
Date: 2025

[FACT] "Organizations can layer both technologies — applying time-slicing within MIG partitions for even finer-grained sharing — enabling isolation between different inference services while maximizing compute utilization within each partition."
— [GPU Memory Pooling and Sharing — Introl Blog](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025)
Date: 2025

[FACT] Recommended MIG configuration for mixed embedding and LLM inference: "2×3g.40gb + 1×1g.10gb: Suitable for training + inference scenarios where larger partitions handle LLMs and smaller instances serve embeddings."
— [GPU Memory Pooling and Sharing — Introl Blog](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025)
Date: 2025

### 6.3 MPS Limitations

[FACT] "MPS (Multi-Process Service) facilitates concurrent sharing of a single GPU among multiple CUDA applications" but "performs poorly with respect to latencies." LithOS research shows "13× better latencies" compared to MPS, indicating MPS is inappropriate for latency-sensitive embedding serving.
— [LithOS: An Operating System for Efficient Machine Learning on GPUs — CMU CSD PhD Blog](https://www.cs.cmu.edu/~csd-phd-blog/2025/lithos/)
Date: 2025

[FACT] "MIG provides isolation, but the units are coarse and reconfiguration takes about a second which is too slow for interactive or shifting workloads."
— [LithOS: An Operating System for Efficient Machine Learning on GPUs — CMU CSD PhD Blog](https://www.cs.cmu.edu/~csd-phd-blog/2025/lithos/)
Date: 2025

### 6.4 Kubernetes GPU Operator

[FACT] "The NVIDIA GPU Operator automates GPU driver installation, device plugin deployment, and monitoring" for consistent operations across embedding and LLM inference workloads in Kubernetes.
— [GPU Memory Pooling and Sharing — Introl Blog](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025)
Date: 2025

---

## 7. Quality Monitoring: Drift Detection and Version Comparison

### 7.1 Embedding Drift Defined

[FACT] "If you are using static embeddings in a RAG setup, monitoring shifts in the embedding space can signal changes in query types, document content, or language."
— [RAG Infrastructure: Building Production RAG Systems — Introl Blog](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)
Date: 2025

[FACT] "Declining retrieval quality often indicates embedding drift, corpus staleness, or distribution shift in query patterns. Weekly quality reviews comparing current retrieval against baseline queries catch degradation before users notice."
— [RAG Infrastructure: Building Production RAG Systems — Introl Blog](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)
Date: 2025

### 7.2 Drift Detection Methods

[FACT] Evidently AI implements five embedding drift detection methods: "Euclidean distance, Cosine distance, Domain classifier, Share of drifted components, and Maximum mean discrepancy (MMD)."
— [5 Methods to Detect Drift in ML Embeddings — Evidently AI](https://www.evidentlyai.com/blog/embedding-drift-detection)
Date: 2025

[FACT] "A powerful technique involves monitoring the distribution of document embeddings by selecting a reference window of document embeddings and periodically comparing the distribution of new or current document embeddings against this reference distribution."
— [Monitor RAG Retrieval Drift — apxml.com](https://apxml.com/courses/optimizing-rag-for-production/chapter-6-advanced-rag-evaluation-monitoring/monitoring-retrieval-drift-rag)
Date: 2025

[FACT] "With smaller samples (e.g., <1000), you can apply statistical testing by comparing the measured distance to the possible distance values for the reference data at a set percentile."
— [5 Methods to Detect Drift in ML Embeddings — Evidently AI](https://www.evidentlyai.com/blog/embedding-drift-detection)
Date: 2025

### 7.3 Monitoring Tooling

[FACT] Evidently AI "can be used in any Python environment or as part of a production pipeline, with output available as HTML, JSON, or Python dictionary and integration with tools like Airflow, MLflow, and Grafana."
— [3.4 Monitoring Embeddings Drift — Evidently AI ML Observability Course](https://learn.evidentlyai.com/ml-observability-course/module-3-ml-monitoring-for-unstructured-data/monitoring-embeddings-drift)
Date: 2025

### 7.4 Responses to Drift

[FACT] "Document corpus drift requires re-indexing your knowledge base and updating or fine-tuning your embedding model on the new data distribution, while query drift may require fine-tuning your retriever or using query understanding techniques to normalize new query styles."
— [Embedding Drift: The Silent RAG Breaker Nobody Talks About — Medium](https://medium.com/@nooralamshaikh336/embedding-drift-the-silent-rag-breaker-nobody-talks-about-ca4a268ef0c1)
Date: December 2025

---

## 8. Comparison: Self-Hosted vs Managed Embedding APIs

### 8.1 Managed API Specifications

| Provider | Model | MTEB Score | Dimensions | Price (per 1M tokens) | Latency P90 |
|----------|-------|-----------|-----------|----------------------|-------------|
| OpenAI | text-embedding-3-small | ~62 | 1536 | $0.02 | ~500ms |
| OpenAI | text-embedding-3-large | 64.6 | 3072 | $0.13 | ~500ms |
| Cohere | embed-v4 | 65.2 | 1024 | $0.10 | ~100-300ms |
| Google | gemini-embedding-001 | 68.32 | 3072 | ~$0.004/1K tokens | ~50ms |
| AWS Bedrock | Titan Embeddings V2 | 66.01 | 1024 | $0.10 | [UNVERIFIED] |

Sources:
- OpenAI pricing: [OpenAI API Pricing](https://platform.openai.com/docs/pricing)
- OpenAI text-embedding-3-small: [$0.02 per million tokens](https://platform.openai.com/docs/models/text-embedding-3-small)
- MTEB scores and Cohere/Google pricing: [Best Embedding Models 2025 — Ailog RAG](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)
- Latency benchmarks: [Benchmarking API Latency of Embedding Providers — Nixiesearch](https://nixiesearch.substack.com/p/benchmarking-api-latency-of-embedding)
- AWS Bedrock Titan MTEB score: [Amazon Titan Embeddings — philschmid.de](https://www.philschmid.de/amazon-titan-embeddings)

[STATISTIC] "OpenAI (text-embedding-3-small) P90 latency: ~500ms, P99 latency: ~5 seconds, Error rate: 0.05%."
— [Benchmarking API Latency of Embedding Providers — Nixiesearch](https://nixiesearch.substack.com/p/benchmarking-api-latency-of-embedding)
Date: 2025

[STATISTIC] "Google Vertex AI achieves 0.002% error rate (best reliability)" among embedding API providers. "Estimated batching windows: OpenAI and Jina: ~300ms; Cohere: ~100ms; Google: ~50ms."
— [Benchmarking API Latency of Embedding Providers — Nixiesearch](https://nixiesearch.substack.com/p/benchmarking-api-latency-of-embedding)
Date: 2025

[STATISTIC] "Amazon Titan achieves an average score of 66.01 on MTEB benchmarks, the worst of five evaluated models, while the best open-source model achieves an average of 74.35."
— [Amazon Bedrock: How good (bad) is Titan Embeddings? — philschmid.de](https://www.philschmid.de/amazon-titan-embeddings)
Date: [PRE-2025: 2023] — No 2025+ independent Titan MTEB benchmark found; use with caution.

### 8.2 What Managed APIs Eliminate (Operational Differential)

[FACT] "Cloud APIs remain the entry point for most production teams. These are fully managed, continuously retrained, and wrapped in scalable infrastructure — perfect for anyone who wants high-quality embeddings without touching GPUs or training pipelines. They abstract away complexity but charge for convenience."
— [Top Embedding Models in 2025 — ArtSmart](https://artsmart.ai/blog/top-embedding-models-in-2025/)
Date: 2025

[FACT] "For engineering teams using managed services like AWS Bedrock, it removes the operational overhead of provisioning GPU instances or managing Kubernetes clusters for inference."
— [What are the Cost Considerations for Different Embedding Models? — Zilliz](https://zilliz.com/ai-faq/what-are-the-cost-considerations-for-different-embedding-models)
Date: 2025

The following table maps the operational domains managed APIs eliminate:

| Operational Domain | Self-Hosted Burden | Managed API |
|-------------------|-------------------|-------------|
| GPU procurement/maintenance | Full ISV responsibility | Eliminated |
| Model updates/retraining | ISV-scheduled, disruptive | Automatic (but invisible) |
| Scaling under load | K8s HPA + GPU provisioning | Automatic |
| Drift monitoring | Custom tooling required | Not provided |
| Versioning/migration | Full ISV discipline required | Partially managed |
| API reliability SLA | ISV SRE obligation | Provider SLA |
| Latency P99 | Controllable, predictable | Provider-variable (~5s spikes) |
| Cost at scale | Fixed infrastructure cost | Variable per-token |

### 8.3 The Hidden Managed API Risk

[FACT] "At a multi-million-document scale, a sudden model turndown can be costly" — managed API providers can deprecate embedding models on their own schedule, forcing ISV customers into unplanned re-embedding operations.
— [Different Embedding Models, Different Spaces — Medium](https://medium.com/data-science-collective/different-embedding-models-different-spaces-the-hidden-cost-of-model-upgrades-899db24ad233)
Date: 2025

---

## 9. Operational Difficulty and FTE Estimates

**Assumptions:** Mid-size ISV, 50 enterprise customers, corpus of 50M documents, mixed real-time and batch embedding, single geographic region, on-premises Kubernetes cluster.

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|------------------|-------------|-------------|--------------|
| **Model Serving** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | GPU driver management, CUDA versioning, model loading optimization | K8s + GPU Operator, NIM containers | API call only |
| | TEI, NIM, TorchServe | NIM on EKS/AKS/GKE | OpenAI/Bedrock/Vertex API |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 |
| **Batch Orchestration** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Custom queue + DLQ + checkpoint logic | Kubernetes Jobs + custom queue | Bedrock Batch Jobs, Gemini Batch API |
| | Celery/Kafka/RabbitMQ | Celery on K8s | Cloud-native batch APIs |
| | Est. FTE: 0.5 | Est. FTE: 0.25 | Est. FTE: 0.1 |
| **Model Versioning & Migration** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 3/5 |
| | Full metadata schema, DLQ, parallel index management | Same + cloud storage for model artifacts | API version pinning; provider-driven change |
| | MLflow + custom metadata | MLflow + S3/GCS | Vendor deprecation notices |
| | Est. FTE: 0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **GPU Scheduling/Sharing** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | MIG config, time-slice policy, priority queues, contention monitoring | GPU Operator + MIG on cloud GPUs | Not applicable |
| | NVIDIA GPU Operator, MIG, custom scheduler | NVIDIA GPU Operator | N/A |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0 |
| **Quality Monitoring** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 3/5 |
| | Evidently AI or custom drift detection, retrieval regression suite | Same tooling, cloud-hosted | Same tooling; no provider drift transparency |
| | Evidently AI, Grafana, MLflow | Evidently AI, CloudWatch | LangWatch, Braintrust |
| | Est. FTE: 0.25 | Est. FTE: 0.25 | Est. FTE: 0.25 |

**Total Estimated FTE — On-Premises:** 2.0–3.25 FTE (active) + 0.5 FTE on-call burden
**Total Estimated FTE — Managed Kubernetes:** 1.1–1.5 FTE (active) + 0.25 FTE on-call burden
**Total Estimated FTE — Cloud-Native (managed APIs):** 0.55–0.7 FTE (active) + minimal on-call burden

[UNVERIFIED] FTE estimates above are derived from practitioner-reported staffing in blog case studies and vendor documentation. No Gartner or Forrester benchmark specific to on-premises embedding pipeline operations was found as of February 2026. The estimates reflect observed patterns from production deployments at the scale described.

---

## Key Takeaways

- **GPU contention is the primary operational risk on-premises.** Embedding models and LLM inference compete for the same physical GPUs. Without explicit MIG partitioning or dedicated GPU pools, embedding latency will degrade unpredictably under LLM load. MIG on A100/H100 hardware is the recommended isolation mechanism, but it requires specialized NVIDIA administration skills.

- **Re-embedding operations are the highest-cost lifecycle event.** Switching embedding models on a multi-million-document corpus requires parallel index management, compute equal to the original indexing job, and a migration window that must be engineered in advance. Managed APIs create an additional risk: providers deprecate models on their own schedule, forcing ISV customers into unplanned re-embedding.

- **Self-hosted embedding can achieve lower p99 latency than managed APIs.** A quantized ONNX embedding model on CPU achieves ~10ms, while OpenAI's API shows P99 latencies of ~5 seconds. For on-premises deployments where consistent low latency is a product requirement, self-hosted embedding is technically superior — at the cost of 2–3x operational FTE compared to managed APIs.

- **Embedding versioning metadata is a non-negotiable operational foundation.** Every vector stored must carry the model version, quantization type, and sequence length metadata used at embedding time. Without this, corpus-wide migrations are operationally blind. This metadata discipline must be built before the first document is embedded, not retrofitted later.

- **Managed APIs eliminate six of eight major operational domains but introduce provider dependency risk.** The operational simplicity of OpenAI, Bedrock, and Vertex embedding APIs is substantial — GPU management, model updates, scaling, and reliability SLAs all disappear. The trade-off is per-token cost at scale, latency variability, and loss of control over when the model version changes.

---

## Related — Out of Scope

- **Vector database operations** (indexing strategies, HNSW tuning, FAISS shard management): See [F45: Vector Database Operations].
- **GPU infrastructure procurement** (GPU hardware selection, data center power requirements, networking): See [F39: GPU Infrastructure for On-Premises AI].
- **Embedding architecture design** (choice of embedding model for a given domain, hybrid search architecture, ColBERT vs dense vs sparse): See [F6: Embedding Architecture Design].

---

## Sources

1. [BAAI/bge-m3 — Hugging Face Model Card](https://huggingface.co/BAAI/bge-m3)
2. [BAAI/bge-m3 Automated Model Memory Requirements — Hugging Face](https://huggingface.co/BAAI/bge-m3/discussions/64)
3. [BAAI/bge-m3 Optimize Inference Speed — Hugging Face](https://huggingface.co/BAAI/bge-m3/discussions/9)
4. [sentence-transformers/all-MiniLM-L6-v2 Memory Requirements — Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/discussions/39)
5. [hkunlp/instructor-xl OOM Error Discussion — Hugging Face](https://huggingface.co/hkunlp/instructor-xl/discussions/14)
6. [Speeding up Inference — Sentence Transformers Documentation](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)
7. [Large-Scale AI Batch Inference: 9x Faster Embedding Generation — SkyPilot Blog](https://blog.skypilot.co/large-scale-embedding/)
8. [NVIDIA NeMo Retriever Embedding NIM Overview](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/overview.html)
9. [NVIDIA NeMo Retriever Embedding NIM Configuration](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/configuration.html)
10. [Cloud-Native RAG: Embeddings + Vectors, Fully Self-Hosted — Medium](https://medium.com/h7w/cloud-native-rag-embeddings-vectors-fully-self-hosted-82d57142353e)
11. [MLOps at Scale: Serving Sentence Transformers in Production — Don Simpson's Blog](https://www.donaldsimpson.co.uk/2025/12/11/mlops-at-scale-serving-sentence-transformers-in-production/)
12. [Different Embedding Models, Different Spaces: The Hidden Cost of Model Upgrades — Medium](https://medium.com/data-science-collective/different-embedding-models-different-spaces-the-hidden-cost-of-model-upgrades-899db24ad233)
13. [Weaviate: When Good Models Go Bad](https://weaviate.io/blog/when-good-models-go-bad)
14. [Embedding-Converter: A Unified Framework for Cross-Model Embedding Transformation — ACL Anthology](https://aclanthology.org/2025.acl-long.1237/)
15. [Best Embedding Models 2025: MTEB Scores and Leaderboard — Ailog RAG](https://app.ailog.fr/en/blog/guides/choosing-embedding-models)
16. [Benchmarking API Latency of Embedding Providers — Nixiesearch](https://nixiesearch.substack.com/p/benchmarking-api-latency-of-embedding)
17. [OpenAI API Pricing](https://platform.openai.com/docs/pricing)
18. [OpenAI text-embedding-3-small Model Card](https://platform.openai.com/docs/models/text-embedding-3-small)
19. [5 Methods to Detect Drift in ML Embeddings — Evidently AI](https://www.evidentlyai.com/blog/embedding-drift-detection)
20. [3.4 Monitoring Embeddings Drift — Evidently AI ML Observability Course](https://learn.evidentlyai.com/ml-observability-course/module-3-ml-monitoring-for-unstructured-data/monitoring-embeddings-drift)
21. [Embedding Drift: The Silent RAG Breaker Nobody Talks About — Medium](https://medium.com/@nooralamshaikh336/embedding-drift-the-silent-rag-breaker-nobody-talks-about-ca4a268ef0c1)
22. [RAG Infrastructure: Building Production Retrieval-Augmented Generation Systems — Introl Blog](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)
23. [Monitor RAG Retrieval Drift — apxml.com](https://apxml.com/courses/optimizing-rag-for-production/chapter-6-advanced-rag-evaluation-monitoring/monitoring-retrieval-drift-rag)
24. [GPU Memory Pooling and Sharing: Multi-Tenant Kubernetes 2025 — Introl Blog](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025)
25. [LithOS: An Operating System for Efficient Machine Learning on GPUs — CMU CSD PhD Blog](https://www.cs.cmu.edu/~csd-phd-blog/2025/lithos/)
26. [LLM Inference Scheduling: A Survey of Techniques, Frameworks, and Trade-offs — TechRxiv](https://www.techrxiv.org/users/994660/articles/1355915/)
27. [Best Practices for Error Handling, Monitoring, and Recovery — IJCTT](https://www.ijcttjournal.org/2025/Volume-73%20Issue-4/IJCTT-V73I4P120.pdf)
28. [Dead Letter Queues: The Complete Developer-Friendly Guide](https://swenotes.com/2025/09/25/dead-letter-queues-dlq-the-complete-developer-friendly-guide/)
29. [Kafka Dead Letter Queue Best Practices — Superstream](https://www.superstream.ai/blog/kafka-dead-letter-queue)
30. [Defining SLA/SLO-Driven Monitoring Requirements in 2025 — Uptrace](https://uptrace.dev/blog/sla-slo-monitoring-requirements)
31. [What are the Cost Considerations for Different Embedding Models? — Zilliz](https://zilliz.com/ai-faq/what-are-the-cost-considerations-for-different-embedding-models)
32. [Top Embedding Models in 2025 — ArtSmart](https://artsmart.ai/blog/top-embedding-models-in-2025/)
33. [Celery Complete Guide — DevToolbox](https://devtoolbox.dedyn.io/blog/celery-complete-guide)
34. [Amazon Bedrock: How good (bad) is Titan Embeddings? — philschmid.de](https://www.philschmid.de/amazon-titan-embeddings)
35. [Solving AI Foundational Model Latency with Telco Infrastructure — arXiv](https://arxiv.org/html/2504.03708v1)
