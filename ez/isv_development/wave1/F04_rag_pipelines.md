# F4: RAG Pipelines & Retrieval Patterns

**Research Area:** Infrastructure Architecture for AI SaaS ISVs
**Scope:** RAG pipeline architecture, stage-by-stage infrastructure requirements, retrieval strategies, and advanced patterns
**Out of Scope:** LLM model serving (F5), vector database operations (F6), agent frameworks (F7)

---

## Executive Summary

Retrieval-augmented generation (RAG) has emerged as the dominant architecture for grounding LLM outputs in enterprise knowledge, with [51% of enterprise AI systems now incorporating RAG](https://www.nimbleway.com/blog/rag-pipeline-guide) — up from 31% the prior year. A production RAG pipeline spans eight discrete stages — document ingestion, chunking, embedding generation, vector storage, retrieval, reranking, context assembly, and LLM generation — each carrying distinct infrastructure requirements that differ materially across on-premises, Managed Kubernetes, and cloud-native deployment models. Retrieval accuracy is the dominant quality lever: hybrid search (combining dense vector search with BM25 sparse retrieval) outperforms single-method approaches by [20–30%](https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking), and cross-encoder reranking delivers an additional [10–25% precision gain](https://app.ailog.fr/en/blog/guides/reranking) at a latency cost of 50–500ms. At enterprise scale — corpora of 1 million or more documents, thousands of concurrent users — sub-second query latency is achievable but requires GPU-accelerated vector indexes, multi-tier caching, and careful operational investment that varies substantially by deployment model. The [RAG market reached $1.85 billion in 2024 and is growing at 49% CAGR](https://www.morphik.ai/blog/retrieval-augmented-generation-strategies), reflecting the shift from experimental deployments to production-grade infrastructure decisions.

---

## Section 1: Pipeline Stage Architecture

A RAG pipeline is not a single system — it is a sequence of eight distinct processing stages, each with separate compute, storage, and orchestration requirements. Understanding these stages is prerequisite to infrastructure sizing.

### 1.1 Stage Map

| Stage | Function | Primary Output |
|---|---|---|
| 1. Document Ingestion | Load, parse, and normalize raw source documents | Structured text + metadata |
| 2. Chunking | Divide documents into retrieval-sized units | Chunks with provenance metadata |
| 3. Embedding Generation | Encode chunks as dense vectors | Float32/FP8 embedding vectors |
| 4. Vector Storage | Persist and index vectors for ANN search | Queryable vector index |
| 5. Retrieval | Execute dense, sparse, or hybrid search | Candidate chunk set (top-K) |
| 6. Reranking | Score candidates by query-chunk relevance | Ranked, pruned candidate set |
| 7. Context Assembly | Format retrieved chunks into LLM prompt | Assembled prompt string |
| 8. LLM Generation | Generate response conditioned on context | Natural language output |

[FACT] "Production systems process PDFs, HTML, Word documents, Slack messages, and database records through format-specific parsers."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

[STATISTIC] Production initial backfill scale: "100,000 to 10 million documents during initial backfill, with daily incremental loads of 1,000 to 50,000 new documents."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

### 1.2 Stage-Level Latency Budgets

For interactive RAG applications, the following latency allocations apply across the query path:

| Stage | Typical Latency Range | Notes |
|---|---|---|
| Retrieval (dense/sparse) | 50–200ms | Depends on index size and hardware |
| Reranking | 50–500ms | Model size and candidate count |
| LLM Generation | 1–5 seconds | Model size and output length |
| End-to-end target | < 3 seconds | For interactive use cases |

[STATISTIC] "Retriever Latency: Low (~50-200ms). Ranker Latency: Medium (~100-500ms). Generator Latency: High (~1-5 seconds). Mean Time to Answer: < 3 seconds for interactive use."
URL: https://www.morphik.ai/blog/retrieval-augmented-generation-strategies

[FACT] "Customer service chatbot use case requires TTFT under 2 seconds (TTFT <2s) and end-to-end response time under 20 seconds."
URL: https://developer.nvidia.com/blog/enabling-horizontal-autoscaling-of-enterprise-rag-components-on-kubernetes

---

## Section 2: Infrastructure Per Stage

### 2.1 Document Ingestion — Object Storage + Parsing Layer

**Infrastructure required:**
- Object storage (S3, Azure Blob, GCS, or on-premises MinIO/Ceph) as the source-of-truth document store
- Document parsing services: PDF parsers, HTML extractors, OCR engines for scanned content
- A metadata extraction layer to preserve document ID, title, timestamp, and provenance
- Message queue (Redis, SQS, RabbitMQ) for async ingestion job dispatch

[FACT] "Modern RAG engines must support hybrid retrieval (vector + keyword + metadata filtering)" and require "metadata extraction capabilities" that "maintain document structure information."
URL: https://www.nimbleway.com/blog/rag-pipeline-guide

**Deployment model comparison:**

| Capability | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| Object storage | MinIO/Ceph self-hosted | S3/Blob via cloud APIs | S3/Blob/GCS managed |
| Parser workers | Self-managed containers | K8s Jobs/CronJobs | Lambda/Cloud Functions |
| Queue | Self-hosted Redis/RabbitMQ | Managed Redis (ElastiCache) | SQS/Pub-Sub managed |
| Difficulty | 4/5 | 3/5 | 1/5 |
| Est. FTE | 0.5–1.0 | 0.25–0.5 | 0.1–0.25 |

*FTE assumption: mid-size deployment serving 50 enterprise customers with daily incremental ingestion of 5,000–10,000 documents.*

### 2.2 Chunking — Compute Workers

Chunking is a stateless transformation step. Infrastructure requirements are modest relative to embedding generation, but the algorithmic choice has outsized impact on downstream retrieval quality.

[STATISTIC] "Most production systems use 400-512 token chunks with 50-100 token overlap, achieving 85-90% recall in benchmark tests."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

[STATISTIC] "Semantic chunking improves recall by up to 9% for narrative content like documentation, FAQs, and conversational data."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

**Infrastructure required:**
- CPU-based compute workers (chunking is not GPU-bound)
- Access to the document store for reading parsed text
- Write access to an intermediate staging store for chunks before embedding
- Python-based NLP libraries (spaCy, NLTK, or LangChain text splitters) for semantic/recursive chunking

### 2.3 Embedding Generation — GPU Compute (or API Endpoints)

Embedding generation is the most compute-intensive preprocessing stage. It can be served via managed API or self-hosted model endpoint.

[STATISTIC] Embedding cost range: "$0.02 to $0.18 per million tokens depending on model selection."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

[STATISTIC] Baseten embedding inference benchmark: FP8 quantization achieves "2.05x more throughput" vs. bfloat16, with ">99% cosine similarity" preserved. Tested on single H100 GPU at 256 sentences per request, 512 tokens per sentence.
URL: https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference/

[STATISTIC] TensorRT-LLM integration achieves "at least a 15% speedup" for embedding inference.
URL: https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference/

[STATISTIC] Caching strategies can "reduce embedding costs 40-60%."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

**Infrastructure required:**
- GPU-equipped worker nodes OR managed embedding API (OpenAI, Cohere, Voyage AI, AWS Bedrock)
- Batching layer: Hugging Face TEI (Text Embedding Inference) or equivalent supports batch requests to increase GPU utilization
- Vector staging storage before upsert into the vector database
- Model registry/versioning system (MLflow 3.0 or equivalent) to track embedding model version with corpus version

[FACT] "MLflow 3.0 extended its model registry to handle generative AI applications and AI agents, connecting models to exact code versions, prompt configurations, evaluation runs, and deployment metadata."
URL: https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025

**Deployment model comparison:**

| Capability | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| Embedding compute | Self-hosted GPU servers | GPU node pools (EKS, AKS, GKE) | Bedrock/OpenAI/Cohere APIs |
| Batching | Self-managed TEI/vLLM | K8s Deployment + HPA | API handles batching |
| Model versioning | MLflow self-hosted | MLflow on K8s | SageMaker / Vertex AI |
| Re-embedding on model change | Full corpus re-run, manual | K8s batch jobs | API call update (no self-management) |
| Difficulty | 5/5 | 3/5 | 2/5 |
| Est. FTE | 0.5–1.0 | 0.25–0.5 | 0.05–0.1 |

### 2.4 Vector Storage — See F6 (Vector Database Operations)

See [F6: Vector Database Operations] for detailed coverage of vector index management, ANN algorithm selection (HNSW, IVF-PQ, CAGRA), and operational requirements. This section covers only what the pipeline requires at the storage interface.

[STATISTIC] "A 10-million document corpus with 1024-dimensional embeddings requires approximately 40GB of vector storage."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

[STATISTIC] "Quantization storage reduction: 4-8x with minimal accuracy loss."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

### 2.5 Retrieval — Query Execution Layer

The retrieval stage executes a search against the vector index (and optionally a BM25/sparse index) to surface a candidate set of chunks for a given query embedding.

**Infrastructure required:**
- Query embedding endpoint (same infrastructure as ingestion-time embedding, but must be low-latency)
- Vector database query interface
- Optional: BM25 index (Elasticsearch, OpenSearch, Tantivy, or built-in sparse retrieval in Qdrant/Weaviate)
- Score fusion layer (Reciprocal Rank Fusion engine) for hybrid search

[STATISTIC] Hybrid search retrieval accuracy improvement: "20-30% compared to single methods."
URL: https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking

[STATISTIC] "A recent IBM research paper compared various combinations of retrieval methods, concluding that using three-way retrieval (BM25 + dense vectors + sparse vectors) is the optimal option for RAG."
URL: https://medium.com/@robertdennyson/dense-vs-sparse-vs-hybrid-rrf-which-rag-technique-actually-works-1228c0ae3f69

[FACT] "Hybrid search with RRF achieves NDCG of 0.85, compared to 0.72 for dense-only approaches in mixed queries."
URL: https://medium.com/@robertdennyson/dense-vs-sparse-vs-hybrid-rrf-which-rag-technique-actually-works-1228c0ae3f69

### 2.6 Reranking — Cross-Encoder Model Endpoint

The reranking stage applies a cross-encoder model to score each (query, chunk) pair with higher fidelity than the embedding-based retrieval approximation. This is a separate model endpoint from the embedding service.

[STATISTIC] Cross-encoder reranking precision improvement: "10-25% accuracy improvement over pure retrieval."
URL: https://app.ailog.fr/en/blog/guides/reranking

[STATISTIC] "Reranking typically adds 50 to 500ms of latency." Specific model benchmarks: "TinyBERT adds ~50ms for 20 documents"; "Cohere Rerank adds ~200ms (including API call)"; "LLM-based reranking (GPT-4, Claude) can add 1-3 seconds."
URL: https://app.ailog.fr/en/blog/guides/reranking

[STATISTIC] Cohere Rerank API pricing: "approximately $1 per 1,000 reranking requests."
URL: https://app.ailog.fr/en/blog/guides/reranking

[STATISTIC] Self-hosted cross-encoder model ms-marco-MiniLM-L6-v2: "Size: 80MB, Speed: ~50ms per batch."
URL: https://app.ailog.fr/en/blog/guides/reranking

[FACT] "Always overfetch for reranking: Retrieve 3-5x the final k." Standard production pattern: retrieve top 20–100 candidates, rerank to top 5–10 for LLM context.
URL: https://app.ailog.fr/en/blog/guides/reranking

**Three-tier retrieval funnel (from production deployments):**

| Tier | Input | Operation | Output |
|---|---|---|---|
| Coarse filtering | Full corpus (e.g., 10M chunks) | Metadata filters + ANN approximation | ~100,000 candidates |
| Vector search | 100,000 candidates | Dense/sparse/hybrid ANN | Top 100 results |
| Reranking | Top 100 results | Cross-encoder scoring | Top 5–10 for LLM context |

URL: https://zenvanriel.nl/ai-engineer-blog/rag-architecture-patterns-that-scale/

**Deployment model comparison:**

| Capability | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| Reranking model | Self-hosted (Triton/vLLM) | K8s Deployment, GPU node pool | Cohere Rerank API / AWS Bedrock |
| Autoscaling | Manual / self-managed HPA | K8s HPA on GPU utilization | API auto-scales transparently |
| Autoscaling trigger | [UNVERIFIED — no on-prem spec found] | GPU utilization >75% per NVIDIA reference | API-managed |
| Difficulty | 4/5 | 3/5 | 1/5 |
| Est. FTE | 0.25–0.5 | 0.1–0.25 | 0.05 |

*[UNVERIFIED]: On-premises autoscaling triggers for reranking servers are not documented in available sources. Estimate based on general GPU server management norms.*

### 2.7 Context Assembly — Orchestration Layer

Context assembly is typically handled by the RAG orchestration framework (LangChain, LlamaIndex, or custom) and does not require dedicated infrastructure beyond the application layer.

**Infrastructure required:**
- Application server where orchestration logic runs
- Prompt template registry (version-controlled)
- Token budget management to avoid exceeding LLM context window

This stage is low-infrastructure; the operational profile is dominated by software configuration rather than hardware provisioning.

### 2.8 LLM Generation

See [F5: LLM Model Serving] for detailed coverage of LLM inference infrastructure. The RAG pipeline interfaces with LLM generation via an API endpoint (self-hosted or managed).

---

## Section 3: Chunking Strategies

### 3.1 Strategy Comparison

| Strategy | Description | Chunk Size | Recall (Benchmark) | Compute Cost | Best For |
|---|---|---|---|---|---|
| Fixed-size | Split by token/character count, ignoring structure | Configurable | 85.4–89.5% at 400 tokens | Very low (CPU) | Simple corpora, baseline |
| Recursive | Hierarchical split: sections → paragraphs → sentences | Configurable | 88.1–89.5% at 400 tokens | Low (CPU) | Most production RAG workloads |
| Semantic | Groups related content by meaning; variable length | Variable | ~91% (highest in class) | High (requires embedding model at chunk time) | Narrative docs, FAQs, conversational data |

[STATISTIC] "Chroma research found performance varied by up to 9% in recall across methods, with LLMSemanticChunker achieving 0.919 recall and RecursiveCharacterTextSplitter hitting 85.4-89.5% (best at 400 tokens: 88.1-89.5%)."
URL: https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide

[STATISTIC] Domain-specific chunk size guidance from production deployments: "Patents: 1,000-1,500 token chunks. Chat logs: 200-400 token chunks."
URL: https://www.morphik.ai/blog/retrieval-augmented-generation-strategies

### 3.2 Production Trade-offs

[FACT] "Every chunking strategy trades off context preservation against retrieval precision — smaller chunks match queries more precisely but lose surrounding context, while larger chunks preserve relationships between ideas but dilute relevance in embeddings."
URL: https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide

[FACT] "For production decisions, test whether semantic chunking justifies the cost — if recursive splitting gives 88% recall and semantic gives 91%, is the 3% improvement worth 10x processing time and embedding costs?"
URL: https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide

**Recommended production starting point:** [RecursiveCharacterTextSplitter at 400–512 tokens with 10–20% overlap](https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide), graduating to semantic chunking only when quality metrics justify the additional compute cost.

---

## Section 4: Embedding Model Management

### 4.1 Model Selection and Hosting

[STATISTIC] "Voyage-3-large outperforming OpenAI text-embedding-3-large by 9.74% and Cohere embed-v3-english by 20.71%."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

[FACT] "Voyage AI supports 32K-token context windows (compared to 8K for OpenAI and 512 for older Cohere models)."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

### 4.2 Batching Strategy

[FACT] "Text Embedding Inference (TEI) supports batch requests, which allows you to send multiple documents at the same time to increase utilization of your endpoint. The batch manager packs individual tokenized sentences into batches up to a maximum sequence size, using a scheduling policy to maximize GPU utilization, minimize tail effects, and preserve request order."
URL: https://huggingface.co/blog/inference-endpoints-embeddings

[FACT] "Batching multiple inputs per API call slashes request overhead by ~10×."
URL: https://huggingface.co/blog/inference-endpoints-embeddings

Baseten's BEI system uses token-based limits (rather than request-based limits) to prevent OOM errors, with memory buffers allocated at startup for predictable resource management.
URL: https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference/

### 4.3 Versioning and Re-Embedding

Re-embedding is one of the highest-cost operational events in a RAG pipeline's lifecycle: when an embedding model is upgraded, all existing chunks must be re-embedded and the vector index rebuilt.

[FACT] "RAG systems require versioning of embedding models, chunking strategies, and retrieval parameters."
URL: https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025

[FACT] "Running batch re-embedding jobs during off-peak or low-carbon hours is a recommended practice for production systems. Monitor index drift — changes in embeddings require partial rebuilds."
URL: https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025

**Operational requirement:** Maintain parallel indexes during embedding model transitions to avoid retrieval quality degradation. This requires additional vector storage capacity (approximately 2x) during transition windows. [UNVERIFIED: No primary source quantifies the exact capacity multiple; estimate based on operational logic of maintaining a live index during rebuild.]

---

## Section 5: Retrieval Strategies

### 5.1 Dense Retrieval (Vector Search)

Dense retrieval encodes both query and chunks as high-dimensional vectors and uses approximate nearest neighbor (ANN) search to find semantically similar chunks.

- Default approach in most RAG implementations
- Performs well for semantic queries, paraphrases, and conceptual matches
- Underperforms on exact-match queries (product codes, names, abbreviations)

### 5.2 Sparse Retrieval (BM25 / Lexical)

BM25 is a term-frequency weighting algorithm that scores documents by keyword overlap, adjusted for document length and corpus frequency.

[FACT] "BM25 (Sparse/Lexical): Matches exact words and is best for structured text, names, quotes, or identifiers."
URL: https://medium.com/@dewasheesh.rana/bm25-vs-sparse-vs-hybrid-search-in-rag-from-layman-to-pro-e34ff21c4ada

Infrastructure: Requires a full-text search index (Elasticsearch, OpenSearch, or built-in BM25 in Weaviate/Qdrant). Storage overhead is additive to the vector index.

### 5.3 Hybrid Search (Dense + Sparse Fusion)

Hybrid search runs both dense and sparse retrieval in parallel and fuses results using score normalization and Reciprocal Rank Fusion (RRF).

[FACT] RRF formula: "RRF(d) = Σ 1/(k + r(d)) — ranks documents by inverse position across both retrieval methods."
URL: https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking

[FACT] "Hybrid search can boost RAG retrieval accuracy by 20-30% compared to single methods."
URL: https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking

[STATISTIC] Recommended production hybrid weighting: "BM25 (0.3 weight) + dense embeddings (0.7 weight) for optimal recall and precision."
URL: https://www.morphik.ai/blog/retrieval-augmented-generation-strategies

**Supported databases:** Weaviate, Pinecone, Elasticsearch, Qdrant, Apache Cassandra offer native hybrid search support.
URL: https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking

**Infrastructure note:** "Not all vector databases support hybrid search." Hybrid search also "may be slower than semantic search when executing on a large knowledge corpus" due to dual-index traversal.
URL: https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking

### 5.4 Metadata Filtering

Metadata filtering pre-filters the candidate space before ANN search by applying structured predicates (e.g., `customer_id = X`, `date >= 2025-01-01`). This reduces search space and enables multi-tenant isolation.

**Infrastructure requirement:** The vector database must support filtered ANN search without full index scans. This capability varies by database and is covered in [F6: Vector Database Operations].

---

## Section 6: Reranking — Cross-Encoder Models

### 6.1 Architecture

Cross-encoders jointly encode the query and each candidate chunk through a single transformer pass, producing a relevance score. This is fundamentally different from bi-encoder (embedding) models, which encode query and document independently and use cosine similarity.

[FACT] "The two-stage pipeline consists of retrieval (fast, scales to billions) then reranking (accurate, on small sets)."
URL: https://app.ailog.fr/en/blog/guides/reranking

### 6.2 Computational Cost

[STATISTIC] "The computational cost of reranking is 2-10x higher than retrieval alone. Cost scales linearly with the number of candidates, with doubling the candidate size doubling processing costs, though diminishing relevance returns typically occur beyond 100 candidates."
URL: https://customgpt.ai/rag-reranking-techniques/

[STATISTIC] NVIDIA Kubernetes autoscaling reference: reranking/embedding services scaled from 1 to 3 pod replicas; autoscaling triggers at GPU utilization >75%.
URL: https://developer.nvidia.com/blog/enabling-horizontal-autoscaling-of-enterprise-rag-components-on-kubernetes

### 6.3 Latency vs. Accuracy Trade-off

[STATISTIC] Reranking latency ranges: TinyBERT (~50ms for 20 documents), Cohere Rerank API (~200ms), LLM-based reranking (1–3 seconds).
URL: https://app.ailog.fr/en/blog/guides/reranking

[STATISTIC] "Studies show +33-40% accuracy improvement for only +120ms latency on average."
URL: https://customgpt.ai/rag-reranking-techniques/

**Production recommendation:** For most ISV applications, ms-marco-MiniLM-L6-v2 (80MB, ~50ms per batch, free excluding GPU compute) provides the best latency-accuracy trade-off for self-hosted deployments. Use Cohere Rerank API for cloud-native deployments where operational simplicity outweighs per-request cost.

---

## Section 7: Advanced RAG Patterns

### 7.1 Multi-Hop Retrieval

Multi-hop retrieval enables reasoning across multiple documents when no single document answers a complex query. The system executes sequential retrieval steps, using intermediate results to form the next query.

[FACT] "Advanced RAG systems introduce multi-hop retrieval mechanisms, enabling reasoning across multiple documents for complex queries. Adaptive RAG dynamically selects retrieval strategies: straightforward queries bypass retrieval entirely, simple queries use single-step retrieval, and complex queries activate multi-step processes with iterative refinement."
URL: https://arxiv.org/html/2501.09136v1

**Infrastructure impact:** Each hop adds 50–200ms retrieval latency plus LLM call latency for intermediate reasoning. Multi-hop queries can easily consume 10–30 seconds end-to-end.

### 7.2 Agentic RAG

Agentic RAG combines traditional RAG with LLM-driven decision-making: agents dynamically decide which sources to retrieve from, whether to refine the query, and when retrieved context is sufficient.

[FACT] "A single agent manages the retrieval, routing, and integration of information through dynamic routing across structured databases, semantic search, web search, and recommendation systems."
URL: https://arxiv.org/html/2501.09136v1

[FACT] Multi-agent systems "distribute specialized tasks across agents operating in parallel, with a coordinator delegating queries. This enables task specialization and scalability while introducing coordination complexity and data integration challenges."
URL: https://arxiv.org/html/2501.09136v1

**Frameworks supporting agentic RAG:** LangChain, LlamaIndex, CrewAI, AutoGen.
URL: https://arxiv.org/html/2501.09136v1

**Infrastructure impact:** Agentic RAG multiplies LLM API call volume. [FACT] "Request frequency potentially increases by one to two orders of magnitude higher than human requests in the traditional search era."
URL: https://ragflow.io/blog/rag-review-2025-from-rag-to-context

### 7.3 Graph-Based RAG (GraphRAG)

GraphRAG represents knowledge as an entity-relationship graph rather than a flat chunk collection, enabling structure-aware multi-hop reasoning.

[FACT] "GraphRAG is a new paradigm that addresses traditional RAG limitations through graph-structured knowledge representation capturing entity relationships, graph-aware retrieval mechanisms enabling multi-hop reasoning, and structure-guided knowledge search algorithms."
URL: https://medium.com/@phoenixarjun007/beyond-vanilla-rag-the-7-modern-rag-architectures-every-ai-engineer-must-know-af18679f5108

[STATISTIC] "GraphRAG achieves up to 99% search precision for structured domains."
URL: https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide

**Infrastructure impact:** Requires a graph database (Neo4j, Amazon Neptune, or similar) alongside the vector database. Graph traversal queries add a distinct infrastructure dependency and operational profile. This substantially increases on-premises complexity.

### 7.4 Corrective RAG (CRAG)

Corrective RAG introduces a retrieval quality evaluator between the retrieval and generation stages. If retrieved documents are assessed as irrelevant or low-confidence, the system reformulates the query or falls back to web search.

[FACT] "Corrective Retrieval-Augmented Generation (CRAG) is a framework designed to improve robustness when dealing with inaccuracies in retrieved data, introducing a lightweight retrieval evaluator to assess document quality and enable adaptive responses to incorrect, ambiguous, or irrelevant information."
URL: https://arxiv.org/html/2501.09136v1

**Infrastructure impact:** Adds a classification model endpoint (retrieval evaluator) and optionally a web search API dependency. The corrective loop can trigger additional LLM calls, increasing cost and latency unpredictability.

### 7.5 Advanced Pattern Infrastructure Summary

| Pattern | Additional Infrastructure | Latency Impact | Operational Difficulty Added |
|---|---|---|---|
| Multi-Hop | None (reuses existing pipeline) | +50–200ms per hop | Low |
| Agentic RAG | Orchestration framework, tool registry | +1–5s per agentic step | Moderate |
| GraphRAG | Graph database (Neo4j/Neptune) | +100–500ms graph traversal | High (new DB technology) |
| Corrective RAG | Classifier model endpoint, web search API | +200–500ms per correction | Moderate |

---

## Section 8: Scale Considerations

### 8.1 Corpus Scale Thresholds

[STATISTIC] "Enterprise RAG systems handle massive knowledge bases exceeding 1 million documents, with expectations to scale to tens or hundreds of millions of documents."
URL: https://www.deepchecks.com/build-high-performance-rag-pipelines-scale/

[STATISTIC] ColPali tensor storage calculation at million-document scale: "the tensor data for a single page occupies ~512KB. For a million-page document base, the index size expands to TB levels."
URL: https://ragflow.io/blog/rag-review-2025-from-rag-to-context

[STATISTIC] "GPU-accelerated vector search (e.g., FAISS-GPU, RAFT cuVS) pushing retrieval down to <50ms even at billion-scale."
URL: https://www.deepchecks.com/build-high-performance-rag-pipelines-scale/

### 8.2 Query Latency Requirements

[FACT] "Sub-second latency is no longer optional" for interactive enterprise RAG applications.
URL: https://www.deepchecks.com/build-high-performance-rag-pipelines-scale/

[STATISTIC] GPU resource sizing: "A single A100-40GB or two L4 GPUs typically handle 10K daily RAG calls with sub-second latency when embeddings are cached."
URL: https://www.morphik.ai/blog/retrieval-augmented-generation-strategies

[STATISTIC] Multi-layer caching delivers "2–5x speedups." Query embedding caches achieve "30-50% hit rates" in production.
URL: https://zenvanriel.nl/ai-engineer-blog/rag-architecture-patterns-that-scale/

### 8.3 Index Update Frequency

[FACT] "Incremental updates implement differential update mechanisms to avoid computationally expensive full index reconstructions."
URL: https://www.deepchecks.com/build-high-performance-rag-pipelines-scale/

[FACT] "Continuous improvement cycle follows a 3-step loop: log comprehensive retrieval telemetry, analyze weekly to identify performance degradation, then retrain and update based on insights."
URL: https://www.deepchecks.com/build-high-performance-rag-pipelines-scale/

### 8.4 Deployment Model Comparison at Scale

| Capability | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| Corpus scale | Limited by storage hardware | Storage scales via node pools | Effectively unlimited (S3 + managed vector DB) |
| Index update | Manual job scheduling | K8s CronJobs / Argo Workflows | Managed pipelines (Bedrock, Vertex) |
| Query autoscaling | Manual/VMware DRS | HPA + Karpenter | Transparent (API or serverless) |
| GPU provisioning | Capital purchase required | On-demand GPU nodes | On-demand GPU instances |
| Latency at scale | Hardware-bound | Configurable with right instance types | Managed SLAs available |
| Difficulty (full stack) | 5/5 | 3/5 | 2/5 |
| Est. FTE (full stack) | 2.0–4.0 | 1.0–2.0 | 0.5–1.0 |

*FTE assumption: full-stack RAG pipeline (ingestion through generation) for a mid-size ISV serving 50 enterprise customers, 1–5M document corpus, 10K+ daily queries. Excludes LLM serving (F5) and vector DB operations (F6) FTE.*

---

## Sources

- [Nimbleway: Step-by-step Guide to Building a RAG Pipeline](https://www.nimbleway.com/blog/rag-pipeline-guide)
- [Introl Blog: RAG Infrastructure — Production Retrieval-Augmented Generation Guide](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)
- [Introl Blog: Model Versioning Infrastructure — MLOps Artifact Management Guide 2025](https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025)
- [RAGFlow Blog: From RAG to Context — 2025 Year-End Review](https://ragflow.io/blog/rag-review-2025-from-rag-to-context)
- [Ailog RAG: Reranking for RAG — +40% Accuracy with Cross-Encoders (2025 Guide)](https://app.ailog.fr/en/blog/guides/reranking)
- [Ailog RAG: Cross-Encoder Reranking for RAG Precision](https://app.ailog.fr/en/blog/guides/cross-encoder-reranking)
- [CustomGPT: RAG Reranking Techniques for Better Search](https://customgpt.ai/rag-reranking-techniques/)
- [Superlinked VectorHub: Optimizing RAG with Hybrid Search and Reranking](https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking)
- [Medium (Dewasheesh Rana): BM25 vs Sparse vs Hybrid Search in RAG](https://medium.com/@dewasheesh.rana/bm25-vs-sparse-vs-hybrid-search-in-rag-from-layman-to-pro-e34ff21c4ada)
- [Medium (Robert Dennyson): Dense vs Sparse vs Hybrid RRF](https://medium.com/@robertdennyson/dense-vs-sparse-vs-hybrid-rrf-which-rag-technique-actually-works-1228c0ae3f69)
- [Langcopilot: Document Chunking for RAG — 9 Strategies Tested (70% Accuracy Boost 2025)](https://langcopilot.com/posts/2025-10-11-document-chunking-for-rag-practical-guide)
- [Firecrawl: Best Chunking Strategies for RAG in 2025](https://www.firecrawl.dev/blog/best-chunking-strategies-rag-2025)
- [Morphik Blog: RAG in 2025 — 7 Proven Strategies to Deploy at Scale](https://www.morphik.ai/blog/retrieval-augmented-generation-strategies)
- [DeepChecks: Build High-Performance RAG Pipelines That Scale](https://www.deepchecks.com/build-high-performance-rag-pipelines-scale/)
- [Zen van Riel: RAG Architecture Patterns That Scale](https://zenvanriel.nl/ai-engineer-blog/rag-architecture-patterns-that-scale/)
- [NVIDIA Technical Blog: Enabling Horizontal Autoscaling of Enterprise RAG Components on Kubernetes](https://developer.nvidia.com/blog/enabling-horizontal-autoscaling-of-enterprise-rag-components-on-kubernetes)
- [Hugging Face Blog: Deploy Embedding Models with Inference Endpoints](https://huggingface.co/blog/inference-endpoints-embeddings)
- [Baseten Blog: How We Built BEI — High-Throughput Embedding Inference](https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference/)
- [arXiv 2501.09136: Agentic Retrieval-Augmented Generation — A Survey on Agentic RAG](https://arxiv.org/html/2501.09136v1)
- [Medium (phoenixarjun007): Beyond Vanilla RAG — 7 Modern RAG Architectures](https://medium.com/@phoenixarjun007/beyond-vanilla-rag-the-7-modern-rag-architectures-every-ai-engineer-must-know-af18679f5108)
- [Neo4j Blog: Advanced RAG Techniques](https://neo4j.com/blog/genai/advanced-rag-techniques/)
- [AWS Storage Blog: Building Self-Managed RAG Applications with EKS and S3 Vectors](https://aws.amazon.com/blogs/storage/building-self-managed-rag-applications-with-amazon-eks-and-amazon-s3-vectors/)

---

## Key Takeaways

- **Eight discrete stages, eight infrastructure decisions.** A production RAG pipeline spans document ingestion through LLM generation. Each stage has distinct compute, storage, and operational requirements. Conflating them in infrastructure planning leads to bottlenecks — particularly at the embedding generation and reranking stages, which carry the highest per-query compute cost.

- **Hybrid search is the production standard.** Single-method retrieval (dense-only or BM25-only) is increasingly insufficient for enterprise corpora. Three-way retrieval (BM25 + dense + sparse) with Reciprocal Rank Fusion is backed by IBM research as optimal, delivering 20–30% accuracy gains over dense-only approaches.

- **Reranking delivers measurable ROI at acceptable latency.** Cross-encoder reranking adds 50–500ms of latency while delivering 10–25% precision improvements. For ISVs serving high-stakes enterprise use cases, the accuracy gain reduces LLM token waste and hallucination rates, creating cost offsets that can justify the latency and compute investment.

- **Embedding model changes are high-cost operational events.** Any upgrade to the embedding model triggers full corpus re-embedding — a compute and time-intensive operation. ISVs must maintain model version registries, plan for 2x storage capacity during transitions, and implement incremental differential updates to minimize downtime.

- **On-premises full-stack RAG requires 2–4 FTE; cloud-native reduces this to 0.5–1.0 FTE.** The operational profile gap between deployment models is widest for GPU-dependent stages (embedding generation, reranking). Cloud-native managed APIs abstract these entirely; on-premises deployments require specialized ML infrastructure engineers and ongoing hardware management. Advanced patterns (GraphRAG, agentic RAG) add further infrastructure dependencies — particularly graph databases and orchestration frameworks — that amplify this operational gap.

---

## Related — Out of Scope

- **Vector database internal operations** (HNSW tuning, index sharding, ANN algorithm selection): See [F6: Vector Database Operations]
- **LLM inference infrastructure** (model serving, GPU scheduling, KV cache management): See [F5: LLM Model Serving]
- **Agent framework orchestration** (LangChain, LlamaIndex, CrewAI architecture and deployment): See [F7: Agent Frameworks]
- **Observability and RAG evaluation tooling** (RAGAS, LangSmith, tracing pipelines): Not assigned to this wave but referenced by F4 findings as operationally critical for production deployments
