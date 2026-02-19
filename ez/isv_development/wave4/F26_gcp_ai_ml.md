# F26 — GCP AI/ML Services: Vertex AI, Gemini API, and Managed ML

**Research Assignment:** F26 — GCP AI/ML Services
**Scope:** GCP AI/ML managed services for LLM inference, embeddings, vector search, and ML pipelines
**Date:** 2026-02-18
**Audience:** C-suite and technical leadership evaluating ISV deployment models

---

## Executive Summary

Google Cloud's AI/ML portfolio is anchored by Vertex AI, a unified platform that consolidates model training, fine-tuning, inference, vector search, pipelines, and agent orchestration under a single managed control plane. The Gemini model family — spanning Gemini 2.5 Pro, 2.5 Flash, and 2.0 Flash — provides tiered LLM inference with context windows up to 1 million tokens and a pricing structure that spans from $0.15/M tokens (2.0 Flash input) to $10/M tokens (2.5 Pro output), with 50% batch discounts available across models. Vertex AI Vector Search 2.0, released December 2025, represents a architectural shift from index-as-a-service to a unified storage-and-retrieval engine that demonstrates 9.6ms P95 latency at 5,000 QPS on one billion vectors. Document AI has deprecated its Human-in-the-Loop capability (as of January 2025) while retaining a broad processor library covering 12+ document types at $0.10 per 10 pages. For ISVs building AI SaaS products, GCP's managed AI services eliminate the need to operate vector databases, embedding pipelines, RAG infrastructure, and ML workflow schedulers — though significant abstraction comes with vendor lock-in and less fine-grained control compared to self-managed Kubernetes deployments.

---

## 1. Vertex AI: Unified ML Platform

### 1.1 Platform Overview

[FACT] Vertex AI is Google Cloud's unified platform for ML models and generative AI, covering model building, tuning, deployment, and monitoring.
— [Vertex AI Platform | Google Cloud](https://cloud.google.com/vertex-ai)

[FACT] Vertex AI offers two primary model training methods: AutoML (minimal ML expertise required) and custom training (full control over training code and frameworks).
— [AutoML beginner's guide | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide)

[FACT] Vertex AI Prediction Dedicated Endpoints are generally available (GA) as of 2025, offering native streaming inference, gRPC support, customizable request timeouts, and Private Service Connect (PSC) networking.
— [Reliable AI with Vertex AI Prediction Dedicated Endpoints | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/reliable-ai-with-vertex-ai-prediction-dedicated-endpoints)

[FACT] Hex-LLM (High-Efficiency Large Language Model Serving) is available in General Availability on Vertex AI.
— [Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs)

### 1.2 Custom Training

[FACT] Custom training jobs run on managed compute instances that spin up when needed and shut down when finished; infrastructure provisioning, scaling, and teardown are handled entirely by Google Cloud.
— [Vertex AI: Training and serving a custom model | Google Codelabs](https://codelabs.developers.google.com/vertex_custom_training_prediction)

[FACT] Spot VMs are available for training and prediction jobs with significant cost discounts; Compute Engine may preemptively stop Spot VMs to reclaim capacity.
— [Vertex AI Platform | Google Cloud](https://cloud.google.com/vertex-ai)

[FACT] Reservation consumption of VMs with GPUs attached is supported for custom training jobs and prediction jobs.
— [Reliable AI with Vertex AI Prediction Dedicated Endpoints | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/reliable-ai-with-vertex-ai-prediction-dedicated-endpoints)

### 1.3 Prediction Endpoints

[FACT] After training completes, models are deployed to endpoints that serve predictions via REST API; the underlying serving infrastructure is fully managed.
— [Vertex AI Endpoints: From Model Training to Production](https://learn.gcpstudyhub.com/pages/blog/vertex-ai-endpoints-from-model-training-to-production)

[FACT] Vertex AI Prediction supports both Public Dedicated Endpoints and Private Service Connect Endpoints (PSC-E), both of which are generally available (GA).
— [Reliable AI with Vertex AI Prediction Dedicated Endpoints | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/reliable-ai-with-vertex-ai-prediction-dedicated-endpoints)

### 1.4 Vertex AI Pipelines

[FACT] "Vertex AI Pipelines lets you automate, monitor, and govern your machine learning (ML) systems in a serverless manner by using ML pipelines to orchestrate your ML workflows."
— [Serverless machine learning pipelines on Google Cloud | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/serverless-machine-learning-pipelines-on-google-cloud)

[FACT] Vertex AI Pipelines supports ML pipelines defined using the Kubeflow Pipelines (KFP) SDK or the TensorFlow Extended (TFX) SDK, compiled to YAML intermediate representation.
— [Introduction to Vertex AI Pipelines | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)

[FACT] An ML pipeline in Vertex AI Pipelines is a directed acyclic graph (DAG) of containerized pipeline tasks interconnected using input-output dependencies. By default, pipeline tasks run in parallel.
— [Introduction to Vertex AI Pipelines | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)

[STATISTIC] Vertex AI Pipelines charges a run execution fee of $0.03 per pipeline run, plus the cost of Compute Engine resources consumed by pipeline components.
— [Vertex AI pricing | Google Cloud](https://cloud.google.com/vertex-ai/pricing)

[FACT] Vertex AI Pipelines is described as "entirely serverless" — when pipelines are uploaded and run, Vertex AI handles provisioning and scaling the infrastructure to run the pipeline; users pay only for resources used during execution.
— [Serverless machine learning pipelines on Google Cloud | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/serverless-machine-learning-pipelines-on-google-cloud)

[FACT] Pipeline tasks can delegate workloads to external execution engines including BigQuery, Dataflow, and Google Cloud Serverless for Apache Spark.
— [Introduction to Vertex AI Pipelines | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)

**Infrastructure Abstracted by Vertex AI Pipelines:**

| Layer | What GCP Manages |
|---|---|
| Compute provisioning | Auto-scales containerized task runners |
| Orchestration scheduling | DAG execution, parallelism, dependencies |
| State tracking | Pipeline run history, artifact lineage |
| Retry/failure handling | Step-level retry logic |
| Security | IAM, VPC, CMEK integration |

---

## 2. Gemini API: Managed LLM Access

### 2.1 Model Family and Context Windows

[FACT] Gemini 2.5 Pro and Gemini 2.5 Flash are now stable and generally available on Vertex AI, providing stability, reliability, and scalability for mission-critical applications.
— [Gemini 2.5 Updates: Flash/Pro GA, SFT, Flash-Lite on Vertex AI | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-2-5-flash-lite-flash-pro-ga-vertex-ai)

[FACT] Gemini 2.5 Pro and Gemini 2.5 Flash each support a 1 million token context window.
— [Gemini 2.5 Pro | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro)

[FACT] Gemini 2.0 Flash supports a 1 million token context window and includes built-in tool use, multimodal generation, and native streaming inference.
— [Gemini 2.0: Flash, Flash-Lite and Pro - Google Developers Blog](https://developers.googleblog.com/en/gemini-2-family-expands/)

[FACT] Gemini 3 (the most intelligent model) is available for developers via the Gemini API with state-of-the-art reasoning, autonomous coding, multimodal understanding, and powerful agentic capabilities, as of November 2025.
— [New Gemini API updates for Gemini 3 - Google Developers Blog](https://developers.googleblog.com/new-gemini-api-updates-for-gemini-3/)

### 2.2 Pricing (Vertex AI, Standard Tier, as of 2026-02-18)

[STATISTIC] Gemini 2.5 Pro standard pricing on Vertex AI:
- Input tokens (≤200K context): $1.25 per 1M tokens
- Input tokens (>200K context): $2.50 per 1M tokens
- Text output (≤200K context): $10.00 per 1M tokens
- Text output (>200K context): $15.00 per 1M tokens
- Cached input tokens: $0.125 per 1M tokens (≤200K)
- Batch/Flex input: $0.625 per 1M tokens (50% discount)
— [Vertex AI Pricing | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing)

[STATISTIC] Gemini 2.5 Flash standard pricing on Vertex AI:
- Text input: $0.30 per 1M tokens (both context ranges)
- Text output: $2.50 per 1M tokens
- Audio input: $1.00 per 1M tokens
- Cached text input: $0.030 per 1M tokens (10% of standard rate)
- Batch/Flex input: $0.15 per 1M tokens
— [Vertex AI Pricing | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing)

[STATISTIC] Gemini 2.0 Flash standard pricing on Vertex AI:
- Input text tokens: $0.15 per 1M tokens
- Output text tokens: $0.60 per 1M tokens
- Input audio tokens: $1.00 per 1M tokens
- Batch API: 50% discount on all modalities
— [Vertex AI Pricing | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing)

### 2.3 Function Calling

[FACT] "The model intelligently determines if a tool is needed and outputs structured data specifying the tool to call and its parameters, allowing applications to execute the tool and feed results back to the model for dynamic, real-world responses."
— [Function calling with the Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/function-calling)

[FACT] Gemini's multimodal function calling capability processes multimodal inputs (image, audio, PDF) in a single API call to predict the best function to call and its parameters.
— [Introduction to function calling | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)

[FACT] For Gemini 3 Pro and later models, multimodal content can be included in function response parts, enabling the model to process image/audio/document context in the next turn.
— [Introduction to function calling | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)

### 2.4 Grounding

[FACT] Gemini can be connected to external data sources via grounding with search APIs, ensuring responses are based on the latest and most relevant information.
— [Grounding with your search API | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-your-search-api)

[STATISTIC] Grounding with Google Search pricing: 10,000 grounded prompts/day free for Gemini 2.5 Pro; 1,500 grounded prompts/day free for Gemini 2.5 Flash; overage rate is $35 per 1,000 grounded prompts.
— [Vertex AI Pricing | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing)

[STATISTIC] Grounding with Your Data (proprietary data sources): $2.50 per 1,000 requests.
— [Vertex AI Pricing | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing)

### 2.5 Gemini Model Comparison Table

| Model | Context Window | Input (Standard) | Output (Standard) | Batch Discount |
|---|---|---|---|---|
| Gemini 2.5 Pro | 1M tokens | $1.25/M (≤200K) | $10.00/M (≤200K) | 50% |
| Gemini 2.5 Flash | 1M tokens | $0.30/M | $2.50/M | 50% |
| Gemini 2.0 Flash | 1M tokens | $0.15/M | $0.60/M | 50% |

Source: [Vertex AI Pricing | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing)

---

## 3. Vertex AI Vector Search: Managed Similarity Search

### 3.1 Architecture and Scale

[FACT] Vertex AI Vector Search 2.0, announced December 2025, evolves from an index-as-a-service system into a comprehensive storage and retrieval system, with Collections of Data Objects as the primary resource instead of indexes, providing a replicated, scalable storage engine.
— [Introducing Vertex AI Vector Search 2.0: From Zero to Billion Scale | Google Developer Forums](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931)

[FACT] Vector Search 2.0 replaces embedding pipelines, feature stores, ANN indexes, and search engines with one managed service.
— [Vector Search 2.0 | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview)

[STATISTIC] Vertex AI Vector Search demonstrated 9.6ms P95 latency and 0.99 recall while scaling to 5,000 queries per second on a dataset of one billion vectors.
— [Introducing Vertex AI Vector Search 2.0: From Zero to Billion Scale | Google Developer Forums](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931)

[FACT] Vertex AI Vector Search can scale up to support billions of embeddings and hundreds of thousands of queries per second while maintaining ultra-low latency, using Google's ScaNN (Scalable Nearest Neighbors) algorithm.
— [Vector Search | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)

### 3.2 Search Modes

[FACT] Vertex AI Vector Search supports three search modes: dense embeddings (semantic similarity), sparse embeddings (keyword/syntax-based), and hybrid search combining both modes.
— [Vector Search | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)

[FACT] "Vector Search hybrid search and sparse embeddings are generally available (GA), using both dense and sparse embeddings to search based on a combination of keyword search and semantic search."
— [Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs)

### 3.3 Filtering

[FACT] Vector Search supports numeric filtering and text attribute filtering to limit searches to index subsets using Boolean rules. A high number of restricts increases memory usage and causes more shards to be created.
— [Filter vector matches | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/filtering)

[FACT] For each vector's record, filtering is implemented by adding a field called `restricts` containing an array of objects representing namespaces, with each object having a field named `namespace`.
— [Filter vector matches | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/filtering)

### 3.4 Streaming Updates

[FACT] Vertex AI Vector Search supports real-time streaming ingestion for rapidly changing data.
— [Vector Search | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)

### 3.5 Managed Infrastructure Abstractions

[FACT] Vector Search is a fully managed service where Google handles deployment, scaling, and operations. Users configure indexes; underlying compute (VMs hosting indexes) is provisioned automatically.
— [Vector Search | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)

[FACT] Vector Search 2.0 is described as "auto-tuned to maintain high performance while abstracting away underlying infrastructure."
— [Introducing Vertex AI Vector Search 2.0: From Zero to Billion Scale | Google Developer Forums](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931)

| Infrastructure Layer | What GCP Manages |
|---|---|
| Index provisioning | Automatic shard creation, VM allocation |
| Scaling | Horizontal scale based on QPS demand |
| Embedding generation | Auto-embeddings with built-in models (VS 2.0) |
| Algorithm tuning | ScaNN algorithm self-tuning |
| Endpoint management | Public endpoints and PSC endpoints |

---

## 4. Document AI: Managed Document Processing

### 4.1 Processor Library

[FACT] Document AI's Enterprise Document OCR processor is generally available, extracting text including handwritten content from 200+ languages. Maximum pages: 15 (online), 500 (batch).
— [Processor list | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/processors-list)

[FACT] Document AI Form Parser is generally available and handles key-value pairs, checkboxes, tables, and generic entities in 200+ languages. Maximum pages: 15 (online), 100 (batch). This processor requires no training or customization.
— [Processor list | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/processors-list)

[FACT] Document AI Layout Parser is generally available, extracting document content elements (text, tables, and lists) and creating context-aware chunks from PDF, HTML, DOCX, PPTX, and XLSX/XLSM files. Currently limited to EU and US regions.
— [Processor list | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/processors-list)

[FACT] Document AI Custom Extractor is generally available and extracts fields from documents using generative AI or custom models, supporting 80+ languages with normalized data types. Maximum pages: 15 (online), 200 (batch).
— [Processor list | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/processors-list)

**Pretrained Processor Inventory (all GA as of 2026-02-18):**

| Processor | Languages | Max Pages (Online/Batch) |
|---|---|---|
| Invoice Parser | 12 languages | 15 / 100 |
| Expense Parser | 6 languages | 15 / 100 |
| Bank Statement Parser | English | 15 / 100 |
| W2 Parser (2018–2020) | English | 15 / 100 |
| US Passport Parser | English | 15 / 2 |
| US Driver License | All 50 states | 15 / — |
| Utility Parser | English | 15 / 100 |
| Pay Slip Parser | English | 15 / 100 |
| Identity Document Proofing | English | 15 / 100 |

Source: [Processor list | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/processors-list)

[FACT] Document AI Summarizer is in Preview status, supports English only, and is available in the US region only. Maximum pages: 15 (online), 250 (batch).
— [Processor list | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/processors-list)

### 4.2 Pricing

[STATISTIC] Document AI pretrained processor pricing: Invoice Parser at $0.10 per 10 pages; Expense Parser at $0.10 per 10 pages; Utility Parser at $0.10 per 10 pages. Custom processor hosting costs $0.05 per hour per deployed processor version.
— [Pricing | Document AI | Google Cloud](https://cloud.google.com/document-ai/pricing)

### 4.3 Human-in-the-Loop (HITL) — DEPRECATED

[FACT] "Document AI Human-in-the-Loop is deprecated and will no longer be available on Google Cloud after January 16, 2025. New customers are not allowlisted."
— [Release Notes | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new)

[FACT] Google recommends working with a Google Cloud certified partner (Devoteam, Searce, or Quantiphi) to implement alternative human review and correction solutions following the HITL deprecation.
— [Release Notes | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new)

[FACT] Prior to deprecation, HITL enabled human verification and corrections to ensure accuracy of data extracted by Document AI processors before use in critical business applications. Human review results could be used as pre-labeled document files for training custom processors.
— [Human-in-the-Loop Overview | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/hitl)

---

## 5. Vertex AI Agent Builder: RAG, Search, and Conversation Agents

### 5.1 Platform Overview

[FACT] Vertex AI Agent Builder is a managed Google Cloud service for creating conversational and task-oriented AI agents. It combines large language models with tools for conversation design and data integration, enabling teams to deploy agents across websites, mobile apps, and voice interfaces.
— [Vertex AI Agent Builder | Google Cloud](https://cloud.google.com/products/agent-builder)

[FACT] Vertex AI Agent Engine is a set of services that enables developers to deploy, manage, and scale AI agents in production, offering a fully managed runtime, evaluation, Sessions, Memory Bank, and Code Execution.
— [Vertex AI Agent Engine overview | Vertex AI Agent Builder | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview)

[FACT] Agent Engine supports framework-agnostic deployment including ADK (Agent Development Kit), LangChain, LangGraph, and others without rework.
— [Vertex AI Agent Engine overview | Vertex AI Agent Builder | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview)

### 5.2 RAG Engine

[FACT] Vertex AI RAG Engine automates: data ingestion from various sources, data transformation (chunking), embedding generation, index creation and management, retrieval execution, and grounded response generation with an LLM.
— [Vertex AI RAG Engine overview | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)

[FACT] RAG Engine supports flexible vector database backends: RagManagedDb (managed Spanner), Vertex AI Vector Search, Weaviate, Pinecone, and Feature Store.
— [Vertex AI RAG Engine overview | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)

[FACT] RAG data sources include local files, Cloud Storage, Google Drive, Slack, Jira, and BigQuery for grounding agent responses.
— [Vertex AI Agent Builder overview | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/overview)

[FACT] RAG Engine operates across 18+ regions with varying launch stages (GA, Preview, or Allowlist access) and supports CMEK and VPC-SC security controls.
— [Vertex AI RAG Engine overview | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)

### 5.3 Search Capability

[FACT] "Vertex AI Search provides an out-of-the-box RAG solution that gets you started with just a few clicks, while Vector Search supports hybrid techniques that combine vector-based and keyword-based approaches for more relevant responses."
— [Vertex AI Agent Builder overview | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/overview)

### 5.4 Conversation Agents and Memory

[FACT] Agent Engine Sessions stores individual interactions between users and agents, providing definitive sources for conversation context. Memory Bank stores and retrieves information from sessions to personalize agent interactions.
— [Vertex AI Agent Engine overview | Vertex AI Agent Builder | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview)

[FACT] Pre-built agent templates available in Agent Engine include ReAct, RAG, multi-agent, and other templates.
— [Vertex AI Agent Engine overview | Vertex AI Agent Builder | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview)

### 5.5 Infrastructure Managed by Agent Builder / Agent Engine

[FACT] Agent Engine handles infrastructure management, scaling, security, and monitoring. It uses Terraform for resource management, includes automated deployment workflows via Cloud Build, and has built-in support for Cloud Trace and Cloud Logging.
— [Vertex AI Agent Engine overview | Vertex AI Agent Builder | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview)

---

## 6. AutoML: No-Code Model Training

### 6.1 Supported Modalities

[FACT] AutoML in Vertex AI supports model training across four data types: images, text, tabular data, and video. It trains models without writing code.
— [AutoML Solutions - Train models without ML expertise | Google Cloud](https://cloud.google.com/automl)

[FACT] AutoML Vision supports object detection, image classification, and custom image classification. Target industries cited include healthcare, retail, and manufacturing.
— [No-Code Approach to Machine Learning with Vertex AI AutoML](https://www.architech.ca/articles/no-code-approach-to-machine-learning-with-vertex-ai-automl)

[FACT] AutoML Natural Language enables text classification, entity extraction, sentiment analysis, and content categorization.
— [No-Code Approach to Machine Learning with Vertex AI AutoML](https://www.architech.ca/articles/no-code-approach-to-machine-learning-with-vertex-ai-automl)

[FACT] AutoML Tables supports predictive modeling, anomaly detection, and classification for structured/tabular data, including financial forecasting, fraud detection, and inventory management use cases.
— [AutoML in Vertex AI: Understanding the Relationship - K21 Academy](https://k21academy.com/google-cloud/automl-in-vertex-ai-understanding-the-relationship/)

### 6.2 Automated Pipeline Steps

[FACT] Vertex AI AutoML automates the following components in the ML pipeline: data readiness, feature engineering, training and hyperparameter tuning, model serving, model interpretability, and Edge device deployment.
— [Unlock the Power of AutoML with Google's Vertex AI: Revolutionize Your Machine Learning Projects](https://www.encora.com/interface/unlock-the-power-of-automl-with-googles-vertex-ai)

---

## 7. Vertex AI Workbench: Managed Jupyter Notebooks

### 7.1 Instance Configuration

[FACT] Vertex AI Workbench instances are prepackaged with JupyterLab and a preinstalled suite of deep learning packages, including support for TensorFlow and PyTorch frameworks.
— [Introduction to Vertex AI Workbench | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction)

[FACT] Vertex AI Workbench supports CPU-only or GPU-enabled instance configurations. GPU accelerator support is included.
— [Introduction to Vertex AI Workbench | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction)

[FACT] Vertex AI Workbench instances use kernels based on conda environments. Users can add conda environments to instances; each environment appears as a kernel in the JupyterLab interface.
— [Introduction to Vertex AI Workbench | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction)

### 7.2 Managed vs. User-Managed Deprecation

[FACT] "On January 30, 2025, support for user-managed notebooks will end and the ability to create user-managed notebooks instances will be removed. Existing instances will continue to function but patches, updates, and upgrades won't be available."
— [Vertex AI Workbench release notes | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/workbench/release-notes)

### 7.3 Scheduled Execution

[FACT] The Workbench executor allows notebook files to run as one-time or scheduled executions on Vertex AI custom training infrastructure. This enables distributed training, hyperparameter optimization, and continuous training scheduling.
— [Introduction to Vertex AI Workbench | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction)

---

## 8. Vertex AI Model Garden: Pre-Trained Model Deployment

### 8.1 Available Models

[FACT] Model Garden offers 160+ foundation models, including first-party models (Gemini), third-party, and open-source models such as Llama and Gemma.
— [Overview of Model Garden | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)

[FACT] Gemma 3 is available on Vertex AI Model Garden for fine-tuning and deployment via PEFT (LoRA) from Hugging Face in a few steps. The serving infrastructure uses the Vertex AI Model Garden vLLM pre-built Docker image.
— [Use the new Gemma 3 on Vertex AI | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-gemma-3-on-vertex-ai/)

[FACT] Llama (Meta's open model collection) is available for fine-tuning and deployment on Vertex AI, offering pre-trained and instruction-tuned generative text and multimodal models.
— [Self-deployed Llama models | Generative AI on Vertex AI | Google Cloud Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-llama)

### 8.2 Deployment Workflow

[FACT] In Model Garden, users deploy models to GPU-backed Vertex AI endpoints, which associates physical resources with the model to serve online predictions with low latency.
— [Deploy and inference Gemma using Model Garden and Vertex AI GPU-backed endpoints | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-and-inference-tutorial)

[FACT] Gemma models are available in both pretrained versions (not trained on specific tasks) and instruction-tuned versions (trained with human language interactions for conversation).
— [Use Gemma open models | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-gemma)

---

## 9. Text Embeddings API

### 9.1 Models and Specifications

[FACT] `gemini-embedding-001` is the current large embedding model built on the Gemini backbone, designed for superior embedding quality and supporting 100+ languages as well as code.
— [Text embeddings API | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)

[STATISTIC] `gemini-embedding-001` produces 3,072-dimensional vectors. Other Vertex AI embedding models (including text-embedding-004 and Gecko models) produce 768-dimensional vectors.
— [Text embeddings API | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)

[FACT] Users can control embedding vector size using the `output_dimensionality` parameter to reduce storage and computational requirements with minimal quality trade-off.
— [Get text embeddings | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings)

[STATISTIC] Input limit: 5 texts of up to 2,048 tokens per text for all models except `textembedding-gecko@001` (which accepts 3,072 tokens). For `gemini-embedding-001`, each request accepts a single input text.
— [Text embeddings API | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)

---

## 10. ISV Deployment Model Implications

| Capability | On-Premises | Managed Kubernetes (EKS/AKS/GKE) | GCP Cloud-Native (Vertex AI) |
|---|---|---|---|
| LLM Inference | Self-host models, own GPU fleet | Deploy containerized models, manage serving | Gemini API — zero infra, pay per token |
| Embeddings | Run open-source embedding models locally | Deploy embedding model pods | Vertex AI Embeddings API — serverless |
| Vector Search | Deploy Qdrant/Weaviate/pgvector | Managed via Helm charts on K8s | Vertex AI Vector Search — fully managed, billions scale |
| ML Pipelines | Run Airflow/Prefect on own infra | KFP on GKE (manual cluster management) | Vertex AI Pipelines — serverless, $0.03/run |
| RAG | Build chunking + retrieval stack from scratch | Containerized RAG components | Vertex AI RAG Engine — end-to-end managed |
| Document Processing | OCR libraries, custom extraction code | Containerized Document AI alternatives | Document AI — $0.10/10 pages, pretrained |
| Notebook Environment | Self-hosted JupyterHub | JupyterHub on K8s | Vertex AI Workbench — managed, GPU-ready |
| Model Fine-tuning | Full infrastructure ownership | Custom training on K8s (complex) | Vertex AI Custom Training — on-demand, managed |

---

## Key Takeaways

- **Vertex AI provides end-to-end managed abstraction** across the full ML lifecycle: from no-code AutoML training through managed inference endpoints, pipelines, vector search, and agent orchestration — eliminating the need for ISVs to operate any underlying AI infrastructure on GCP.

- **Gemini model pricing spans three tiers** for cost optimization: Gemini 2.5 Pro ($1.25–$10/M tokens) for highest capability, Gemini 2.5 Flash ($0.30–$2.50/M tokens) for price-performance balance, and Gemini 2.0 Flash ($0.15–$0.60/M tokens) for throughput-optimized workloads — all with 50% batch discounts.

- **Vertex AI Vector Search 2.0 (December 2025) is the strongest managed vector database offering evaluated**, demonstrating 9.6ms P95 latency at 5,000 QPS on 1 billion vectors using Google's ScaNN algorithm, with a new architecture that abstracts away index management entirely in favor of Collection-based data objects.

- **Document AI HITL deprecation (January 2025) is a critical risk** for ISVs that planned human-in-the-loop document review workflows on GCP — alternatives require partner engagement with Devoteam, Searce, or Quantiphi, introducing vendor complexity.

- **ISVs adopting GCP cloud-native AI services gain operational simplicity and scale but accept deep platform lock-in**: Vertex AI Pipelines (KFP/TFX), the Gemini API, RAG Engine, and Agent Builder are GCP-proprietary managed services with no direct portability path to on-premises or alternative cloud providers without significant re-engineering.

---

## Sources

1. [Vertex AI Platform | Google Cloud](https://cloud.google.com/vertex-ai)
2. [Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs)
3. [Vertex AI Pricing | Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing)
4. [Overview of Model Garden | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)
5. [Use the new Gemma 3 on Vertex AI | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-gemma-3-on-vertex-ai/)
6. [Self-deployed Llama models | Generative AI on Vertex AI | Google Cloud Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-llama)
7. [Deploy and inference Gemma using Model Garden and Vertex AI GPU-backed endpoints | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-and-inference-tutorial)
8. [Use Gemma open models | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-gemma)
9. [Function calling with the Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/function-calling)
10. [Introduction to function calling | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)
11. [Grounding with your search API | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-your-search-api)
12. [New Gemini API updates for Gemini 3 - Google Developers Blog](https://developers.googleblog.com/new-gemini-api-updates-for-gemini-3/)
13. [Gemini 2.5 Updates: Flash/Pro GA, SFT, Flash-Lite on Vertex AI | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-2-5-flash-lite-flash-pro-ga-vertex-ai)
14. [Gemini 2.5 Pro | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro)
15. [Gemini 2.0: Flash, Flash-Lite and Pro - Google Developers Blog](https://developers.googleblog.com/en/gemini-2-family-expands/)
16. [Vector Search | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)
17. [Filter vector matches | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search/filtering)
18. [Vector Search 2.0 | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview)
19. [Introducing Vertex AI Vector Search 2.0: From Zero to Billion Scale | Google Developer Forums](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931)
20. [Processor list | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/processors-list)
21. [Pricing | Document AI | Google Cloud](https://cloud.google.com/document-ai/pricing)
22. [Human-in-the-Loop Overview | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/hitl)
23. [Release Notes | Document AI | Google Cloud Documentation](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new)
24. [Vertex AI Agent Builder | Google Cloud](https://cloud.google.com/products/agent-builder)
25. [Vertex AI Agent Builder overview | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/overview)
26. [Vertex AI Agent Engine overview | Vertex AI Agent Builder | Google Cloud Documentation](https://docs.cloud.google.com/agent-builder/agent-engine/overview)
27. [Vertex AI RAG Engine overview | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)
28. [Vertex AI RAG Engine: Build & deploy RAG implementations with your data | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/introducing-vertex-ai-rag-engine)
29. [AutoML Solutions - Train models without ML expertise | Google Cloud](https://cloud.google.com/automl)
30. [AutoML beginner's guide | Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide)
31. [AutoML in Vertex AI: Understanding the Relationship - K21 Academy](https://k21academy.com/google-cloud/automl-in-vertex-ai-understanding-the-relationship/)
32. [No-Code Approach to Machine Learning with Vertex AI AutoML](https://www.architech.ca/articles/no-code-approach-to-machine-learning-with-vertex-ai-automl)
33. [Unlock the Power of AutoML with Google's Vertex AI: Revolutionize Your Machine Learning Projects](https://www.encora.com/interface/unlock-the-power-of-automl-with-googles-vertex-ai)
34. [Introduction to Vertex AI Workbench | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction)
35. [Vertex AI Workbench release notes | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/workbench/release-notes)
36. [Introduction to Vertex AI Pipelines | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
37. [Serverless machine learning pipelines on Google Cloud | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/serverless-machine-learning-pipelines-on-google-cloud)
38. [Reliable AI with Vertex AI Prediction Dedicated Endpoints | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/reliable-ai-with-vertex-ai-prediction-dedicated-endpoints)
39. [Text embeddings API | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)
40. [Get text embeddings | Generative AI on Vertex AI | Google Cloud Documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings)
41. [Vertex AI pricing | Google Cloud](https://cloud.google.com/vertex-ai/pricing)
42. [Improve your gen AI app velocity with Inference-as-a-Service | Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/improve-your-gen-ai-app-velocity-with-inference-as-a-service)
