# F35: On-Premises RAG Pipeline Operations

**Research Assignment:** F35 — On-Premises RAG Pipeline Operations
**Scope:** Pipeline orchestration and end-to-end integration of a complete RAG pipeline on self-hosted infrastructure, excluding stage-specific deep dives covered by sibling agents.
**Audience:** C-suite executives and technical leadership
**Date:** 2026-02-18

---

## Executive Summary

Operating a complete RAG pipeline on 100% on-premises infrastructure requires coordinating six to eight discrete self-hosted subsystems — document ingestion, chunking, embedding generation, vector storage, reranking, LLM generation, and pipeline orchestration — none of which benefit from managed-service abstractions available in cloud-native deployments. Each stage introduces its own compute, storage, and operational requirements, and failures at any stage can cascade without the automatic retry and observability tooling that cloud platforms provide out of the box. End-to-end query latency for a well-tuned on-premises RAG system ranges from 2–7 seconds under typical production load, comparable to cloud-native offerings for most workloads, but achieving that performance demands significant GPU investment and specialized MLOps expertise. A mid-size enterprise deployment serving 50 customers requires an estimated 3.0–5.0 FTE of dedicated operational staff across infrastructure, ML engineering, and platform reliability roles. The operational profile of an on-premises RAG pipeline is a 4–5/5 difficulty rating — it is viable for regulated industries and data-sovereign requirements, but carries substantially higher operational burden than managed Kubernetes or cloud-native alternatives.

---

## 1. Document Ingestion On-Premises

### 1.1 Apache Tika: Self-Hosted Text Extraction

Apache Tika is the primary open-source document parsing engine for on-premises RAG pipelines, capable of extracting text and metadata from over 1,000 file formats including PDF, DOCX, XLSX, and HTML. [Tika 3.x requires Java 11](https://idp-software.com/guides/apache-tika-guide/), with the 2.x branch having reached end-of-life in May 2025. Development builds require Java 17 and Maven 3.

**Deployment modes for enterprise use:**

- **Standalone JAR**: Suitable for development and low-volume workloads
- **RESTful Tika Server**: Language-agnostic HTTP interface for microservice integration
- **Docker/Kubernetes**: Horizontal scaling with load balancing via pod replicas
- **tika-pipes**: Asynchronous, queue-backed module for high-volume document processing

**Enterprise tuning requirements:** JVM heap sizing is a critical variable. The [Apache Tika Developer Guide](https://idp-software.com/guides/apache-tika-guide/) documents a recommended JVM configuration of `-Xmx4g -Xms2g -XX:+UseG1GC -XX:MaxGCPauseMillis=200` for high-throughput deployments. Enterprise deployments require memory management tuning, parser selection optimization, and caching strategies.

**OCR-specific considerations:** Tesseract-backed OCR is resource-intensive and can significantly degrade throughput. The Wellcome Trust's documented implementation for processing millions of grant documents revealed that [disabling Tesseract's default multithreading](https://idp-software.com/guides/apache-tika-guide/) prevents resource contention when processing in parallel. For high-OCR workloads, dedicated container pools separated from native-text parsers are required.

**Security note:** In December 2025, a critical vulnerability (CVE-2024-45519) was disclosed affecting the tika-parser-pdf-module. [Users who upgraded tika-parser-pdf-module but did not upgrade tika-core to >= 3.2.2 remain vulnerable](https://www.theregister.com/2025/12/08/infosec_news_in_brief). Teams operating Tika in production must maintain coordinated version upgrades across all modules.

### 1.2 Unstructured.io: Self-Hosted Enterprise Document ETL

[Unstructured.io](https://unstructured.io/) provides an enterprise-grade document ETL platform specifically built for AI preprocessing, with support for native partitioning, OCR, Vision-Language Model (VLM)-based content extraction, and multimodal content handling (tables, charts, images).

**Self-hosted deployment model:** Organizations must [sign a self-hosting agreement with Unstructured](https://docs.unstructured.io/self-hosted/overview) before deploying. Self-hosted instances can run in AWS, Azure, GCP VPCs, or on bare metal. The server enforces a minimum of [2GB available host memory (UNSTRUCTURED_MEMORY_FREE_MINIMUM_MB = 2048)](https://docs.unstructured.io/self-hosted/overview) and will return HTTP 503 if memory drops below this threshold.

**NVIDIA Blackwell acceleration:** In 2025, Unstructured partnered with NVIDIA to enable Blackwell GPU acceleration for on-premises deployments. [Unstructured integrated with NVIDIA NeMo Retriever microservices achieves up to 15x faster processing than legacy approaches, with up to 50% fewer inaccuracies](https://unstructured.io/blog/accelerating-on-premises-ai-with-unstructured-and-nvidia-blackwell) for multimodal content extraction from complex enterprise PDFs.

**Scale claim:** The Unstructured on-premises platform can ["adeptly handle hundreds of thousands of documents"](https://unstructured.io/blog/accelerating-on-premises-ai-with-unstructured-and-nvidia-blackwell) through its horizontally scalable, fault-tolerant pipeline architecture running entirely on-premises.

### 1.3 Storage Requirements for Raw Document Corpus

Enterprise RAG implementations face a significant storage scaling challenge: [RAG-based databases can expand to more than 10x larger than the original text documents and their associated metadata](https://developer.nvidia.com/blog/scaling-enterprise-rag-with-accelerated-ethernet-networking-and-networked-storage/), requiring storage systems to account for raw documents, chunked representations, embeddings, and vector index artifacts.

**Storage protocol preference:** For on-premises RAG, file-based protocols are commonly used. [In RAG and knowledge base implementations, file storage is frequently chosen — particularly in on-premises environments where low-latency, high-performance file systems running in traditional environments are preferred over cloud-native options](https://siliconangle.com/2025/08/27/enterprise-rag-ai-supermicro-openstoragesummit/). NFS and SMB protocols are supported by enterprise all-flash platforms including Pure Storage FlashBlade//S and Infinidat's InfiniBox.

**Networking impact on ingestion throughput:** NVIDIA's published benchmark demonstrates that [network-connected all-flash storage accelerates 1M-vector data ingestion by 36% over direct-attached storage (DAS)](https://developer.nvidia.com/blog/scaling-enterprise-rag-with-accelerated-ethernet-networking-and-networked-storage/), reducing processing time from 338 seconds (DAS) to 216 seconds (networked storage) on a single DGX node with 8x A100 GPUs.

---

## 2. Chunking Infrastructure

### 2.1 CPU Requirements and Parallelism

Chunking — segmenting documents into retrieval-optimized units — is CPU-bound when performed without GPU acceleration. [Most production systems use 400–512 token chunks with 10–20% overlap](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide).

**Scale illustration:** A [10-million document corpus at 500 tokens per chunk requires generating 5 billion tokens in embedding-ready chunks](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide). Even without embedding costs, the chunking compute for this corpus at scale requires distributed parallel processing to complete in operationally acceptable timeframes.

**Advanced chunking trade-offs:** [Context-aware chunking methods that provide good retrieval results require additional pre-processing to segment text, which adds computational requirements that can slow the chunking process](https://www.firecrawl.dev/blog/best-chunking-strategies-rag-2025). Semantic chunking strategies that use embedding similarity to detect boundaries add a GPU dependency to what would otherwise be a pure CPU operation.

### 2.2 Queue Management

On-premises chunking pipelines require explicit queue management — there are no managed services to absorb backpressure. Production patterns recommend [using distributed stream processing frameworks like Apache Kafka or Apache Flink for high-throughput document ingestion, and implementing asynchronous workflows for document chunking, embedding generation, and vector storage to enhance system responsiveness](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide).

**Backfill patterns:** [Backfill operations should parallelize across multiple GPU nodes, processing documents in batches of 100–1,000](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide).

---

## 3. Embedding Generation On-Premises

See [F37: Embedding Generation On-Premises] for detailed coverage of model selection, GPU allocation, batching strategy, and throughput benchmarks.

**Integration point for F35:** The embedding service is a downstream dependency of the chunking stage. The pipeline orchestrator must handle backpressure from the embedding service — if the embedding GPU cluster is saturated, the chunking queue must buffer pending work without data loss.

**Key hardware context:** [A state-of-the-art 7B parameter embedding model can run on a single 24GB GPU](https://medium.com/data-science/running-a-sota-7b-parameter-embedding-model-on-a-single-gpu-bb9b071e2238). Standard sentence-transformer models (22M–567M parameters) operate across a range of batch sizes: all-MiniLM-L6-v2 at batch sizes up to 256, bge-m3 at batch sizes 2–32 due to its 567M parameter footprint. [GPU float16 precision delivers approximately 1.54x faster inference than fp32 baseline on an RTX 3090](https://sbert.net/docs/sentence_transformer/usage/efficiency.html).

**Throughput scaling context:** [Static embedding models achieve 10x–25x faster inference on GPUs and 100x–400x faster on CPUs compared to common alternatives like all-mpnet-base-v2](https://huggingface.co/blog/static-embeddings).

---

## 4. Vector Storage and Retrieval Integration

See [F45: Self-Hosted Vector Databases] for detailed coverage of Milvus, Qdrant, Weaviate, and pgvector operational characteristics.

**Integration point for F35:** The pipeline orchestrator routes embedded chunks to the vector store during ingestion, and issues ANN (approximate nearest neighbor) queries against the vector store during retrieval. The Cisco/Pure Storage FlashStack Validated Design uses [Milvus deployed on OpenShift with object storage persistence on FlashBlade](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/UCS_CVDs/flashstack_rag_nim.html), demonstrating the standard on-premises integration pattern.

**Storage sizing reference:** [A 10-million document corpus with 1024-dimensional embeddings requires approximately 40GB of vector storage](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide). [Quantization techniques reduce storage requirements by 4–8x with minimal accuracy loss](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide).

**Query latency reference:** [Vector search adds 100–500ms of latency in a typical RAG pipeline](https://hackernoon.com/designing-production-ready-rag-pipelines-tackling-latency-hallucinations-and-cost-at-scale) on self-hosted infrastructure, though in-memory architectures at billion-vector scale can achieve single-digit millisecond P95 latencies with appropriate hardware.

---

## 5. Reranking On-Premises

### 5.1 Model Options and GPU Requirements

Self-hosted reranking uses cross-encoder models that score query-document pairs jointly rather than independently, producing more accurate relevance scores than bi-encoder retrieval alone.

**Primary self-hosted reranking models:**

| Model | Parameters | Architecture | Latency Profile |
|-------|-----------|--------------|-----------------|
| [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) | 568M | LoRA + Flash Attention | Fast; multilingual |
| [ms-marco-MiniLM-L6-v2](https://app.ailog.fr/en/blog/guides/reranking) | ~80MB model | Cross-encoder | ~50ms per batch |
| TinyBERT cross-encoder | <50M | Distilled BERT | ~50ms for 20 docs |
| LLM-based reranking (e.g., Llama-3.x) | 7B+ | Decoder-only | 1–3 seconds |

**GPU requirements:** The bge-reranker-v2-m3 has [under 600 million parameters, allowing it to run efficiently on common hardware including consumer GPUs](https://app.ailog.fr/en/blog/guides/reranking). For production deployments serving hundreds of concurrent queries, a dedicated A10G (24GB VRAM) or L40S (48GB VRAM) GPU per reranker replica is the validated enterprise pattern, as documented in the [Cisco FlashStack CVD using NVIDIA L40S GPUs](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/UCS_CVDs/flashstack_rag_nim.html).

**Throughput constraint:** [Each document rerank requires a full forward pass. If a system handles thousands of queries per second and cross-encodes 100 documents per query, this produces significant GPU usage and latency](https://app.ailog.fr/en/blog/guides/reranking). Production systems typically limit the candidate set passed to the reranker to 20–50 documents selected by the upstream ANN retrieval stage.

### 5.2 Latency Impact

Reranking adds measurable but bounded latency to the retrieval pipeline:

- [TinyBERT: ~50ms for 20 documents](https://app.ailog.fr/en/blog/guides/reranking)
- [MiniLM: ~50ms per batch](https://app.ailog.fr/en/blog/guides/reranking)
- [General range: 50–500ms depending on model and number of documents](https://app.ailog.fr/en/blog/guides/reranking)
- [Reranking adds 50–100ms latency when evaluating 50 candidates with cross-encoder models](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)

**Accuracy benefit:** Cross-encoder reranking delivers [10–25% additional precision and reduces hallucinations](https://app.ailog.fr/en/blog/guides/reranking) compared to retrieval without reranking. A published study reports up to [+40% accuracy improvement over pure retrieval](https://app.ailog.fr/en/blog/news/reranking-cross-encoders-study) with cross-encoders.

**Optimization via TensorRT:** [Baseten's BEI runtime, leveraging TensorRT-LLM, achieves 2x higher throughput](https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference/) for embedding and reranker models compared to standard inference, offering a path to higher reranker throughput on existing GPU hardware.

---

## 6. LLM Generation Integration On-Premises

See [F36: Self-Hosted LLM Inference] for detailed coverage of vLLM, Ollama, llama.cpp, and NVIDIA NIM inference engine configurations.

**Integration point for F35:** The pipeline orchestrator assembles the retrieved and reranked context into a prompt and dispatches it to the self-hosted LLM inference endpoint. The primary orchestration challenge at this stage is context window management.

### 6.1 Context Window Management

**The "lost in the middle" problem:** [Mechanically stuffing lengthy text into an LLM's context window scatters the model's attention, significantly degrading answer quality — termed the "lost in the middle" or "information flooding" effect](https://ragflow.io/blog/rag-review-2025-from-rag-to-context). This limits effective chunk count per query irrespective of the model's nominal context window.

**Context window limits by model:** [Llama-3.1-405B performance begins decreasing after 32k tokens; GPT-4-0125-preview after 64k tokens](https://www.databricks.com/blog/long-context-rag-performance-llms) in RAG retrieval scenarios. Self-hosted models at the 7B–70B scale face similar degradation patterns at lower thresholds.

**Cost contrast:** [There is roughly a two-order-of-magnitude gap in cost between relying solely on long-context capability versus employing a full RAG architecture](https://arxiv.org/pdf/2509.21361). KV Cache cost for long-context approaches remains at least one order of magnitude higher than RAG.

**SLA targets for LLM generation stage (from NVIDIA's RAG autoscaling CVD):**

| Use Case | Concurrent Requests | TTFT Target | E2E Latency Target |
|----------|--------------------|--------------|--------------------|
| Customer service chatbot | 100–300 | < 2 seconds | < 20 seconds |
| Email summarization | ~100 | < 10 seconds | < 40 seconds |
| Research agent | ~25 | Not specified | < 120 seconds |

Source: [NVIDIA RAG Kubernetes HPA autoscaling guide](https://developer.nvidia.com/blog/enabling-horizontal-autoscaling-of-enterprise-rag-components-on-kubernetes)

**NIM performance reference:** [NVIDIA NIM delivers 2.6x higher throughput vs an off-the-shelf H100 deployment (1,201 vs 613 tokens/sec on Llama 3.1 8B)](https://introl.com/blog/nvidia-nim-inference-microservices-enterprise-deployment-guide-2025), demonstrating that inference engine selection materially affects pipeline throughput.

---

## 7. Pipeline Orchestration On-Premises

### 7.1 Orchestration Tool Selection

On-premises RAG pipelines require explicit workflow orchestration — there is no managed equivalent to AWS Step Functions, Azure Logic Apps, or GCP Cloud Workflows. The dominant self-hostable options are:

| Tool | Model | Self-Host | Strengths for RAG |
|------|-------|-----------|-------------------|
| [Apache Airflow 3.0](https://airflow.apache.org/) | DAG-based | Yes (full) | DAG versioning, event-driven scheduling, Kubernetes Executor |
| [Prefect](https://www.prefect.io/) | Flow-based | Yes (agent) | Python-native, lighter footprint |
| [Dagster](https://dagster.io/) | Asset-based | Yes | Asset lineage tracking for data quality |
| [Temporal](https://temporal.io/) | Durable execution | Yes | Durable workflow state, complex retry logic |

**Apache Airflow 3.0 (April 2025 release):** Key additions relevant to RAG pipelines include [DAG versioning (natively tracking changes, enabling reproducible reruns and compliance audit trails)](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html), [event-driven scheduling (executing tasks based on real-time events like file uploads or API responses)](https://pirgee.com/blogs/apache-airflow-in-2025-enhancements-in-workflow-orchestration), and a [client-server task execution model that lets tasks run outside the core cluster using the new Task SDK, with Python and Go support](https://www.astronomer.io/press-releases/astronomer-celebrates-the-release-of-apache-airflow-3/).

[Airflow 3 supports remote execution across public and private clouds, on-premises data centers, and edge devices](https://airflowsummit.org/sessions/2025/introducing-apache-airflow-3/).

### 7.2 Retry Logic and Dead Letter Queue Patterns

On-premises RAG pipelines must implement retry and dead letter queue (DLQ) patterns in the application layer — there are no managed DLQ equivalents like AWS SQS or Azure Service Bus without self-hosting these components.

**Core DLQ pattern:** [A Dead Letter Queue (DLQ) is a dedicated queue where messages go when the system cannot process them successfully after a defined number of retries or due to validation/format issues](https://swenotes.com/2025/09/25/dead-letter-queues-dlq-the-complete-developer-friendly-guide/).

**Retry best practices:** [Configure retry logic with exponential backoff and maximum attempt limits to prevent retry loops that overwhelm brokers while giving transient failures a fair chance to succeed before messages land in the DLQ](https://www.superstream.ai/blog/kafka-dead-letter-queue). [Retry should only be used for temporary, external, or environmental failures — not for errors caused by code, data, logic, or user actions](https://swenotes.com/2025/09/25/dead-letter-queues-dlq-the-complete-developer-friendly-guide/).

**Kafka-based DLQ implementation:** [Kafka does not have native DLQ support — the pattern must be implemented in the application layer using frameworks like Spring Kafka, Kafka Connect, or Kafka Streams](https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/).

**Observability enrichment:** [Enriching failed messages with metadata — timestamps, partition details, offset, stack traces, and error codes — provides the breadcrumbs engineers need for debugging and root cause analysis](https://swenotes.com/2025/09/25/dead-letter-queues-dlq-the-complete-developer-friendly-guide/).

### 7.3 RAGOps: The Emerging Operational Discipline

A June 2025 arXiv paper formally introduced [RAGOps](https://arxiv.org/abs/2506.03401) as a framework extending LLMOps to manage the continuous data lifecycle of RAG systems. Key operational capabilities defined:

- **Monitorability:** Clear metrics for detecting performance degradation and data source changes
- **Observability:** Comprehensive visibility via detailed logging of queries, responses, and component interactions, including anomaly detection (e.g., prompt injection attacks)
- **Traceability:** Audit trails for query-response pairs and component interactions
- **Reliability:** Mechanisms for maintaining SLA adherence under dynamic data conditions

On-premises deployments must build all of these capabilities from scratch. Cloud-native RAG services (Bedrock Knowledge Bases, Azure AI Search) provide these as managed features.

---

## 8. End-to-End Latency: On-Premises vs. Cloud-Native

### 8.1 Stage-by-Stage Latency Breakdown

The following table shows the latency contribution of each RAG pipeline stage in a production on-premises deployment:

| Stage | On-Premises Latency | Notes |
|-------|---------------------|-------|
| Query preprocessing | 50–200ms | CPU-bound; normalization, query expansion |
| Query embedding | 20–80ms (GPU) | Self-hosted sentence-transformer; batched |
| Vector search (ANN) | 100–500ms | Self-hosted Milvus/Qdrant; index-dependent |
| Document fetch | 200–1,000ms | Depends on storage I/O and chunk count |
| Reranking (cross-encoder) | 50–500ms | Model size and candidate count dependent |
| LLM generation | 1,000–5,000ms | Token count and GPU throughput dependent |
| **Total P50 (typical)** | **2–7 seconds** | Optimized pipelines: 1.2–1.8s |
| **Total P95 (typical)** | **< 3 seconds** | Requires GPU acceleration and caching |

Sources: [HackerNoon production RAG latency guide](https://hackernoon.com/designing-production-ready-rag-pipelines-tackling-latency-hallucinations-and-cost-at-scale); [Introl RAG infrastructure guide](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)

**Retrieval dominates TTFT:** [Retrieval makes up 41% of end-to-end latencies and 45–47% of time-to-first-token (TTFT) latencies](https://arxiv.org/html/2412.11854v1) in production RAG scenarios, making vector store performance the most impactful single variable for query responsiveness.

### 8.2 Cloud-Native Comparison

| Dimension | On-Premises Self-Hosted | Managed K8s (EKS/AKS/GKE) | Cloud-Native (Bedrock/Azure AI) |
|-----------|------------------------|---------------------------|----------------------------------|
| E2E query latency | 2–7s typical | 1.5–5s typical | Sub-second retrieval; 2–5s total |
| Ingestion throughput | Manual scale; GPU-gated | Autoscaled; GPU-gated | Automatically scaled |
| Reranking | Self-hosted GPU required | Self-hosted GPU required | Managed (Cohere, Azure AI) |
| DLQ/retry | Self-implemented (Kafka/RabbitMQ) | Self-implemented | Managed (SQS, Azure SB) |
| Observability | Custom (Prometheus/Grafana) | Custom + cloud metrics | Native dashboards |
| Data sovereignty | Full | Partial (cloud control plane) | Cloud-dependent |
| Customization | Maximum | High | Limited (black-box chunking/retrieval) |

**Cloud-native latency context:** [Amazon Bedrock Knowledge Bases delivers sub-second latency retrieval for typical RAG workloads](https://aws.amazon.com/bedrock/knowledge-bases/), including the S3 Vectors option introduced in late 2025 offering [up to 90% savings compared to traditional vector databases at sub-second latency](https://aws.plainenglish.io/implementing-rag-with-amazon-bedrock-knowledge-bases-agents-guardrails-pricing-explained-4c7b7c8ea9a2).

**Cloud-native flexibility constraint:** [Bedrock Knowledge Bases lock users into specific chunking strategies and vector stores. Teams requiring advanced retrieval techniques — hybrid search, custom semantic chunking, or reranking logic — frequently end up rebuilding their own RAG pipelines on OpenSearch or Pinecone to regain control over retrieval accuracy](https://www.truefoundry.com/blog/our-honest-review-of-amazon-bedrock-2026-edition).

---

## 9. Validated Enterprise Reference Architecture

The [Cisco FlashStack + NVIDIA NIM RAG CVD (published 2025, GA Q1 2026)](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/UCS_CVDs/flashstack_rag_nim.html) provides a vendor-validated on-premises RAG hardware stack:

**Compute:**
- 6x Cisco UCS X210c M7 compute nodes (1024GB RAM each for worker nodes)
- 4x NVIDIA L40S GPUs (via 2x UCS X440p PCIe nodes)
- 100G Ethernet fabric (Cisco UCS 6536 fabric interconnects)

**Storage:**
- Block: Pure Storage FlashArray//XL170 (Portworx Enterprise backend)
- Object: FlashBlade//S200 (S3-compatible, 7–10 blades, up to 300TB/blade)
- Storage networking: Redundant 100GbE

**Software stack:**
- Orchestration: Red Hat OpenShift 4.17
- Storage abstraction: Portworx Enterprise 3.1.6
- AI inference: NVIDIA NIM Operator (LLM + embedding NIM: Snowflake Arctic-Embed-L + reranking NIM)
- Vector DB: Milvus on OpenShift (FlashBlade persistence)

**Design principle:** ["A resilient design across all layers of infrastructure with no single point of failure"](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/UCS_CVDs/flashstack_rag_nim.html)

---

## 10. Operational Staffing Model

### Assumptions

- Mid-size ISV deployment: 50 enterprise customers, 500K–2M documents in corpus
- Steady-state operation with quarterly re-indexing cycles
- GPU cluster: 4–8 GPUs (embedding + reranking + LLM inference)
- No existing ML infrastructure team

### FTE Estimates by Role

| Role | FTE Range | Responsibilities |
|------|-----------|-----------------|
| ML/AI Infrastructure Engineer | 1.0–1.5 | GPU cluster management, NIM deployment, model updates |
| Platform/SRE Engineer | 0.75–1.0 | Pipeline orchestration, Kafka/Airflow ops, on-call |
| Data/ML Engineer | 0.75–1.0 | Chunking strategy, embedding quality, reranker tuning |
| Storage/Systems Administrator | 0.5–0.75 | NFS/object storage, vector DB capacity planning |
| Security/Compliance (shared) | 0.25–0.5 | CVE patching (Tika, model containers), access controls |
| **Total** | **3.25–4.75 FTE** | Plus 1–2 on-call rotations per week |

**Basis for estimates:** [Self-hosted RAG solutions require teams with machine learning expertise who accept the operational complexity](https://latenode.com/blog/ai/frameworks-tech/best-rag-frameworks-2025-complete-enterprise-and-open-source-comparison). [Self-hosted Milvus requires significant data engineering expertise and SRE capacity](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide). Note: No Gartner-published FTE benchmarks specific to on-premises RAG pipelines were available in 2025+ sources; these estimates are derived from practitioner guidance and validated architecture documentation. [UNVERIFIED against a T1 analyst benchmark — recommend validating against Gartner's XOps staffing framework once subscription access is available.]

---

## 11. Comparative Difficulty Ratings

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|------------------|-------------|-------------|--------------|
| **Document Ingestion** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Tika server ops, OCR tuning, CVE patching | Containerized; autoscale with HPA | Fully managed (Bedrock, Azure AI) |
| | Apache Tika, Unstructured.io | Same tools, K8s-hosted | Native connectors |
| | Est. FTE: 0.5–0.75 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 |
| **Chunking Pipeline** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Queue self-managed, backpressure manual | Queue managed via K8s | Automated (no exposure) |
| | Kafka, custom chunker | Kafka on K8s | Managed service |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **Embedding Generation** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | GPU provisioning, model ops, batching | GPU node pools, autoscale | API call (Bedrock Titan, Azure) |
| | sentence-transformers, NVIDIA NIM | Same + K8s HPA | Managed embedding API |
| | Est. FTE: 0.5–0.75 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0 |
| **Reranking** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Dedicated GPU, model lifecycle ops | GPU node pools, HPA | Cohere Rerank API, Azure |
| | BGE reranker, MiniLM, TensorRT-LLM | Same + autoscale | Managed API |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05 |
| **Pipeline Orchestration** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | DLQ, retry, versioning all self-built | K8s-managed, but self-operated | Step Functions, Logic Apps |
| | Airflow 3.0, Prefect, Temporal + Kafka | Same tools on K8s | Managed orchestration |
| | Est. FTE: 0.5–0.75 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 |
| **Observability/RAGOps** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Full custom stack required | Partial managed metrics | Native dashboards |
| | Prometheus, Grafana, Langfuse | Same + cloud metrics | CloudWatch, Azure Monitor |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05 |

---

## 12. Key Takeaways

- **On-premises RAG is operationally viable but expensive in labor.** A complete self-hosted pipeline spanning ingestion, chunking, embedding, vector retrieval, reranking, and LLM generation requires an estimated 3.25–4.75 FTE of dedicated MLOps and infrastructure staff, compared to 0.5–1.0 FTE for equivalent cloud-native deployments.

- **End-to-end query latency is competitive with cloud when GPU-accelerated.** Well-tuned on-premises pipelines achieve 2–7 second end-to-end latency (P50: 1.2–1.8 seconds with caching); cloud-native services (Bedrock Knowledge Bases) deliver sub-second retrieval but lock users into fixed chunking and retrieval strategies with limited customization.

- **Retrieval latency is the dominant TTFT bottleneck.** Retrieval accounts for 41% of total end-to-end latency and 45–47% of TTFT. Vector store selection and hardware (networked all-flash storage reduces ingestion time 36% vs DAS) are the highest-leverage performance variables on-premises.

- **Pipeline orchestration is the highest-complexity domain.** Retry logic, dead letter queues, DAG versioning, and observability must all be self-built on-premises. Apache Airflow 3.0 (April 2025) adds native DAG versioning and event-driven scheduling that meaningfully reduce this gap, but the operational burden remains at 5/5 difficulty compared to managed alternatives.

- **Validated reference architectures exist and reduce deployment risk.** The Cisco FlashStack + NVIDIA NIM CVD (GA Q1 2026) provides a fully validated on-premises RAG stack with Cisco UCS compute, NVIDIA L40S GPUs, Pure Storage FlashBlade object storage, Red Hat OpenShift, and NVIDIA NIM microservices — offering a proven starting point for enterprises with strict data sovereignty requirements.

---

## Related — Out of Scope

The following topics were encountered during research but are covered by sibling agents:

- **LLM inference engine selection and configuration (vLLM, Ollama, NVIDIA NIM):** See [F36: Self-Hosted LLM Inference]
- **Embedding model selection, GPU allocation, and throughput benchmarks:** See [F37: Embedding Generation On-Premises]
- **Vector database operational characteristics (Milvus, Qdrant, Weaviate, pgvector):** See [F45: Self-Hosted Vector Databases]
- **RAG architecture design patterns (Naive RAG, Advanced RAG, GraphRAG):** See [F4: RAG Architecture Design]

---

## Sources

1. [Apache Tika Official Site](https://tika.apache.org/)
2. [Apache Tika Developer Guide — Intelligent Document Processing](https://idp-software.com/guides/apache-tika-guide/)
3. [Unstructured.io Self-Hosted Overview](https://docs.unstructured.io/self-hosted/overview)
4. [Accelerating On-Premises AI with Unstructured and NVIDIA Blackwell — Unstructured Blog](https://unstructured.io/blog/accelerating-on-premises-ai-with-unstructured-and-nvidia-blackwell)
5. [The Register: Apache Tika 10.0-rated Vulnerability (December 2025)](https://www.theregister.com/2025/12/08/infosec_news_in_brief)
6. [Scaling Enterprise RAG with Accelerated Ethernet Networking and Networked Storage — NVIDIA Technical Blog](https://developer.nvidia.com/blog/scaling-enterprise-rag-with-accelerated-ethernet-networking-and-networked-storage/)
7. [FlashStack for Enterprise RAG Pipeline with NVIDIA NIM — Cisco CVD](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/UCS_CVDs/flashstack_rag_nim.html)
8. [Enabling Horizontal Autoscaling of Enterprise RAG Components on Kubernetes — NVIDIA Technical Blog](https://developer.nvidia.com/blog/enabling-horizontal-autoscaling-of-enterprise-rag-components-on-kubernetes)
9. [Reranking for RAG: +40% Accuracy with Cross-Encoders — Ailog RAG Guide](https://app.ailog.fr/en/blog/guides/reranking)
10. [New Research: Cross-Encoder Reranking Improves RAG Accuracy by 40% — Ailog RAG](https://app.ailog.fr/en/blog/news/reranking-cross-encoders-study)
11. [Top 7 Rerankers for RAG — Analytics Vidhya (June 2025)](https://www.analyticsvidhya.com/blog/2025/06/top-rerankers-for-rag/)
12. [BAAI/bge-reranker-v2-m3 — Hugging Face Model Card](https://huggingface.co/BAAI/bge-reranker-v2-m3)
13. [How We Built BEI: High-Throughput Embedding and Reranker Inference — Baseten Blog](https://www.baseten.co/blog/how-we-built-bei-high-throughput-embedding-inference/)
14. [Speeding up Inference — Sentence Transformers Documentation](https://sbert.net/docs/sentence_transformer/usage/efficiency.html)
15. [Train 400x Faster Static Embedding Models — Hugging Face Blog](https://huggingface.co/blog/static-embeddings)
16. [Running a SOTA 7B Parameter Embedding Model on a Single GPU — Medium/TDS Archive](https://medium.com/data-science/running-a-sota-7b-parameter-embedding-model-on-a-single-gpu-bb9b071e2238)
17. [RAG Infrastructure: Building Production RAG Systems — Introl Blog](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)
18. [Designing Production-Ready RAG Pipelines — HackerNoon](https://hackernoon.com/designing-production-ready-rag-pipelines-tackling-latency-hallucinations-and-cost-at-scale)
19. [Long-Context RAG Performance of LLMs — Databricks Blog](https://www.databricks.com/blog/long-context-rag-performance-llms)
20. [LONG-CONTEXT LLMS MEET RAG — ICLR 2025 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf)
21. [The Maximum Effective Context Window for Real-World Applications — arXiv](https://arxiv.org/pdf/2509.21361)
22. [RAGOps: Operating and Managing Retrieval-Augmented Generation Pipelines — arXiv (June 2025)](https://arxiv.org/abs/2506.03401)
23. [Towards Understanding Systems Trade-offs in RAG Model Inference — arXiv](https://arxiv.org/html/2412.11854v1)
24. [Kafka Dead Letter Queue Best Practices — Superstream Blog](https://www.superstream.ai/blog/kafka-dead-letter-queue)
25. [Dead Letter Queue Complete Developer-Friendly Guide — SWE Notes (September 2025)](https://swenotes.com/2025/09/25/dead-letter-queues-dlq-the-complete-developer-friendly-guide/)
26. [Kafka Connect Deep Dive: Error Handling and DLQs — Confluent Blog](https://www.confluent.io/blog/kafka-connect-deep-dive-error-handling-dead-letter-queues/)
27. [Introducing Apache Airflow 3 — Airflow Summit 2025](https://airflowsummit.org/sessions/2025/introducing-apache-airflow-3/)
28. [Apache Airflow 3.0 Features — Pirgee Blog](https://pirgee.com/blogs/apache-airflow-in-2025-enhancements-in-workflow-orchestration)
29. [Astronomer: Apache Airflow 3 Release](https://www.astronomer.io/press-releases/astronomer-celebrates-the-release-of-apache-airflow-3/)
30. [Amazon Bedrock Knowledge Bases — AWS](https://aws.amazon.com/bedrock/knowledge-bases/)
31. [Implementing RAG with Amazon Bedrock — AWS in Plain English (December 2025)](https://aws.plainenglish.io/implementing-rag-with-amazon-bedrock-knowledge-bases-agents-guardrails-pricing-explained-4c7b7c8ea9a2)
32. [Amazon Bedrock Review 2026 — TrueFoundry](https://www.truefoundry.com/blog/our-honest-review-of-amazon-bedrock-2026-edition)
33. [NVIDIA NIM Inference Microservices Enterprise Deployment Guide — Introl Blog](https://introl.com/blog/nvidia-nim-inference-microservices-enterprise-deployment-guide-2025)
34. [Enterprise RAG Blossoms from Storage Providers — SiliconANGLE (August 2025)](https://siliconangle.com/2025/08/27/enterprise-rag-ai-supermicro-openstoragesummit/)
35. [Best RAG Frameworks 2025 — Latenode](https://latenode.com/blog/ai/frameworks-tech/best-rag-frameworks-2025-complete-enterprise-and-open-source-comparison)
