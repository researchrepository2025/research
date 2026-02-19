# F18: Azure AI/ML Services

**Research Question:** What managed AI/ML services does Azure provide for LLM inference, embeddings, vector search, and ML pipelines, and what do they abstract away?

**Scope:** Azure AI/ML services only. No compute infrastructure (see F16). No other providers.

---

## Executive Summary

Azure has reorganized its AI service portfolio under the **Microsoft Foundry** umbrella (formerly Azure AI Studio), consolidating LLM access, vector search, document processing, speech/vision/language APIs, and safety tooling into a unified surface. The flagship offering — Azure OpenAI Service, now marketed as "Foundry Models sold directly by Azure" — provides managed access to GPT-4o, GPT-5, o-series reasoning models, and third-party models (DeepSeek, Llama) under Provisioned Throughput Units (PTU), abstracting GPU cluster management, model serving, and capacity scaling entirely from the operator. For ISVs building AI-native SaaS, the aggregate effect of these services is the elimination of an ML infrastructure team: embedding generation, vector indexing, document parsing, content safety, and prompt observability are all available as REST APIs with per-token or per-document billing. The tradeoff is deep Azure lock-in and constrained customization below the API surface.

---

## 1. Azure OpenAI Service (Foundry Models)

### 1.1 Model Access and Deployment Types

[FACT] Azure OpenAI Service is now surfaced through the Microsoft Foundry portal and referred to as "Foundry Models sold directly by Azure." The model portfolio as of February 2026 includes GPT-5.2, GPT-5.1, GPT-5.1 Codex, GPT-5, GPT-5 Mini, GPT-4.1, GPT-4.1 Mini, GPT-4.1 Nano, GPT-4o, GPT-4o Mini, o1, o3, o3 Mini, o4 Mini, DeepSeek-R1, DeepSeek-V3-0324, and DeepSeek-R1-0528.
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

[FACT] Three provisioned deployment types exist: **Global Provisioned Throughput** (`GlobalProvisionedManaged`), **Data Zone Provisioned Throughput** (`DataZoneProvisionedManaged`), and **Regional Provisioned Throughput** (`ProvisionedManaged`). Global provisioned is the first deployment option for new models; Data Zone provisioned is added later.
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

[FACT] Global provisioned throughput is available in 28+ regions including eastus, eastus2, uksouth, australiaeast, japaneast, and swedencentral for GPT-5 family models as of February 2026.
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

### 1.2 Provisioned Throughput Units (PTU)

[FACT] "Provisioned throughput units (PTU) are generic units of model processing capacity that you use to size provisioned deployments to achieve the required throughput for processing prompts and generating completions."
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

[FACT] Spillover is an optional capability on PTU deployments that manages traffic fluctuations. Spillover is available for all GPT-4.1 family models, GPT-5 family models, o-series models (o1, o3, o3 Mini, o4 Mini), and GPT-4o / GPT-4o Mini.
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

[FACT] PTU pricing reported as starting at $2,448/month per independent pricing analysis. Monthly and annual reservations are available to reduce costs further.
URL: https://azure-noob.com/blog/azure-openai-pricing-real-costs/

[FACT] When provisioned capacity is exceeded, the API returns HTTP 429 with `retry-after-ms` and `retry-after` headers. The service continues to return 429 until utilization drops below 100%.
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

[FACT] Utilization is managed using a leaky-bucket algorithm. "Each request is evaluated individually according to its prompt size, expected generation size, and model to determine its expected utilization."
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

[FACT] Quota does not guarantee capacity. "Capacity is allocated at deployment time and is held for as long as the deployment exists. If service capacity isn't available, the deployment fails."
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

[FACT] The Provisioned-Managed Utilization V2 metric in Azure Monitor measures deployment utilization on 1-minute increments.
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic
Date: 2026-02-10

### 1.3 Fine-Tuning

[FACT] Azure OpenAI Service now offers provisioned deployments for fine-tuned models, described as giving "your applications predictable performance with predictable costs."
URL: https://azureaggregator.wordpress.com/2025/02/28/announcing-provisioned-deployment-for-azure-openai-service-fine-tuning/
Date: 2025-02-28

[FACT] Fine-tuned models undergo mandatory safety evaluation before deployment: "After training completes but before the fine-tuned model is available for deployment, the resulting model is evaluated for potentially harmful responses using Azure's built-in risk and safety metrics, simulating a conversation with your fine-tuned model."
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning-safety-evaluation?view=foundry-classic

### 1.4 Content Filtering

[FACT] "Azure OpenAI in Microsoft Foundry Models includes default safety settings applied to all models (excluding audio API models), providing responsible experience by default with content filtering models, blocklists, prompt transformation, content credentials, and others."
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter?view=foundry-classic

[FACT] Default safety categories include: hate and fairness, sexual, violence, self-harm, protected material content, and user prompt injection attacks. Advanced output filters include protected material for text, groundedness detection, and personally identifiable information (PII) detection.
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter?view=foundry-classic

[FACT] "The configurability feature allows customers to adjust settings separately for prompts and completions to filter content for each content category at different severity levels."
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter?view=foundry-classic

### 1.5 What Azure OpenAI Abstracts Away for ISVs

| Abstracted Layer | Operator Responsibility Eliminated |
|---|---|
| GPU provisioning and scheduling | No GPU cluster management |
| Model serving stack (TensorRT, vLLM, etc.) | No inference server configuration |
| Model version lifecycle | Managed automatic version transitions |
| Safety/content filter maintenance | Default filters applied; custom config available |
| Capacity auto-scaling (standard deployments) | Built-in; no HPA/KEDA configuration |
| Monitoring (utilization metrics) | Azure Monitor integration out-of-the-box |

**Operational Profile — Azure OpenAI (Cloud-Native ISV deployment):**
Estimated FTE: 0.1–0.25 FTE for ongoing operations (quota management, model version pin decisions, content filter tuning). No infrastructure FTE required.

---

## 2. Azure Machine Learning

### 2.1 Managed Online Endpoints

[FACT] "Managed online endpoints deploy your machine learning models in a convenient, turnkey manner, and are the recommended way to use Azure Machine Learning online endpoints. Managed online endpoints work with powerful CPU and GPU machines in Azure in a scalable, fully managed way. To free you from the overhead of setting up and managing the underlying infrastructure, these endpoints also take care of serving, scaling, securing, and monitoring your models."
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2

[FACT] Azure Machine Learning supports three endpoint types: Standard Deployments (serverless, quota-less, billed per token), Online Endpoints (real-time synchronous low-latency inference), and Batch Endpoints (long-running asynchronous batch inference).
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints?view=azureml-api-2
Date: 2025-08-13

[FACT] Standard deployments "consume no quota from your subscription. For serverless deployments, you're billed based on usage." Online endpoints provision dedicated compute and are billed per instance running. Batch endpoints are billed per job (compute consumed at job run time, not at deployment time).
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints?view=azureml-api-2
Date: 2025-08-13

[FACT] Online endpoint autoscaling is "based on resource utilization (like CPU, memory, requests, etc.)." Batch endpoint autoscaling is "based on the number of jobs created." Standard deployments have built-in scaling to zero.
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints?view=azureml-api-2
Date: 2025-08-13

[FACT] Online endpoints support traffic split routing across multiple deployments (for canary/shadow deployments). Batch endpoints use switch-to-default routing.
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints?view=azureml-api-2
Date: 2025-08-13

[FACT] Online endpoints support mirror traffic for safe rollout. Batch endpoints do not.
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints?view=azureml-api-2
Date: 2025-08-13

### 2.2 MLflow Integration and No-Code Deployment

[FACT] "Azure Machine Learning workspaces are MLflow-compatible, so you use an Azure Machine Learning workspace the same way you use an MLflow server."
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow?view=azureml-api-2

[FACT] "When you deploy MLflow models to Azure Machine Learning, unlike with custom model deployment, you don't need to provide a scoring script or an environment. Azure Machine Learning automatically generates the scoring script and environment. This functionality is called no-code deployment."
URL: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models-online-endpoints?view=azureml-api-2

[FACT] No-code deployment provides out-of-the-box inferencing for scikit-learn, TensorFlow, PyTorch, and ONNX frameworks via MLflow and Triton.
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints?view=azureml-api-2
Date: 2025-08-13

### 2.3 Responsible AI Dashboard

[FACT] "The Responsible AI dashboard can help you make informed business decisions through data-driven insights, to further understand causal treatment effects on an outcome by using historical data only."
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2

[FACT] "The fairness assessment capabilities of this component come from the Fairlearn package." The Responsible AI dashboard assesses model fairness across sensitive groups including gender, ethnicity, and age.
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml?view=azureml-api-2

[FACT] The Responsible AI dashboard supports two disparity metric classes: "Disparity in model performance" and "Disparity in selection rate" (favorable prediction) among subgroups.
URL: https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2

### 2.4 Operational Comparison Table — Model Serving

| Capability | On-Premises | Managed K8s | Cloud-Native (AzureML) |
|---|---|---|---|
| Model serving infrastructure | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| Key requirements | GPU drivers, CUDA, serving stack (TorchServe/Triton), load balancer | K8s GPU operator, Helm charts, ingress controller | Azure ML endpoint config only |
| Representative tools | NVIDIA Triton, vLLM, Ray Serve | Seldon, KServe, Triton on AKS | Azure ML managed online endpoints |
| Est. FTE (mid-size, 50 enterprise customers) | 1.5–2.5 FTE + 0.5 FTE on-call | 0.75–1.5 FTE + 0.25 FTE on-call | 0.1–0.25 FTE |

---

## 3. Azure AI Search — Vector Search

### 3.1 Vector Index Capabilities

[FACT] "Vector search is available in all regions and on all tiers at no extra charge. However, generating embeddings or using AI enrichment for vectorization might incur charges from the model provider."
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-overview
Date: 2026-01-15

[FACT] "Azure AI Search uses a nearest neighbors algorithm to place similar vectors close together in an index. Internally, it creates vector indexes for each vector field."
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-overview
Date: 2026-01-15

[FACT] Vector search supports: similarity search, hybrid search (vector + keyword in parallel), multimodal search (OpenAI CLIP or GPT-4 Turbo with Vision), multilingual search, filtered vector search, and use as a pure vector database.
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-overview
Date: 2026-01-15

[FACT] "Search services created after April 3, 2024 offer higher quotas for vector indexes."
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-overview
Date: 2026-01-15

### 3.2 Hybrid Search

[FACT] "Azure AI Search defines hybrid search as the execution of vector search and keyword search in the same request." Hybrid search merges results from vector and keyword queries "using Reciprocal Rank Fusion (RRF)."
URL: https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview

[FACT] "Hybrid search runs full-text search and vector search in parallel. Merges results from each query by using Reciprocal Rank Fusion (RRF)."
URL: https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview

### 3.3 Integrated Vectorization

[FACT] "Integrated vectorization is an extension of the indexing and query pipelines in Azure AI Search. Integrated vectorization speeds up the development and minimizes maintenance tasks during data ingestion and query time because there are fewer operations that you have to implement manually."
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization

[FACT] "For internal processing, Azure AI Search offers integrated data chunking and vectorization in an indexer pipeline. Integrated vectorization is available in all regions and tiers."
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization

[FACT] Azure AI Search integrates natively with: Azure OpenAI (text-embedding-ada-002 recommended for text embeddings), Azure Vision Image Retrieval API (for image embeddings), Azure Blob Storage, Azure Cosmos DB, Azure SQL, Azure Data Lake Storage Gen2, Azure Table Storage, and Microsoft OneLake as indexer sources.
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-overview
Date: 2026-01-15

[FACT] Azure AI Search is integrated with LangChain as a vector store via the `@azure/search-documents` SDK and the Python `azure-search-documents` package.
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-overview
Date: 2026-01-15

### 3.4 Operational Comparison Table — Vector Search

| Capability | On-Premises | Managed K8s | Cloud-Native (AI Search) |
|---|---|---|---|
| Vector index management | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| Key requirements | Self-host Qdrant/Weaviate/pgvector; manage storage, compaction | Helm-deployed vector DB, PVC provisioning, resource tuning | REST API configuration only; no index infrastructure |
| Representative tools | Qdrant, Weaviate, Milvus, pgvector | Same, on AKS/EKS | Azure AI Search (HNSW managed internally) |
| Est. FTE | 0.5–1.0 FTE | 0.25–0.5 FTE | 0.05–0.1 FTE |

---

## 4. Azure AI Document Intelligence

### 4.1 Service Overview and Version

[FACT] "Azure Document Intelligence in Foundry Tools is a cloud-based Foundry Tools service that you can use to build intelligent document processing solutions." The service "applies optical character recognition (OCR) based on machine learning along with document understanding technologies to extract text, tables, structure, and key/value pairs from documents."
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0
Date: 2025-11-18

[FACT] Document Intelligence v4.0 (API version 2024-11-30) is the current Generally Available version as of the research date.
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0
Date: 2025-11-18

### 4.2 Prebuilt Models

[FACT] Prebuilt model categories in v4.0 GA include: Financial services and legal (bank statement, check, contract, credit card, invoice, pay stub, receipt); US tax (W-2, 1098 variants, 1099 variants, 1040 variants, unified US tax); US mortgage (1003, 1004, 1005, 1008, closing disclosure); Personal identification (health insurance card, identity document, marriage certificate).
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0
Date: 2025-11-18

[FACT] The Read model OCR engine "runs at a higher resolution than Azure Vision Read and extracts print and handwritten text from PDF documents and scanned images." It is the underlying OCR engine for all other Document Intelligence prebuilt models.
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/read?view=doc-intel-4.0.0

[FACT] Optional add-on capabilities include: `ocr.highResolution`, `ocr.formula` (formula extraction), `ocr.font` (font property extraction), `ocr.barcode` (barcode extraction), searchable PDF, query fields, and key-value pairs. Premium add-ons incur extra costs.
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0
Date: 2025-11-18

### 4.3 Custom Models

[FACT] "Custom models can be trained using template-based, neural, or composite approaches and can be built with as few as five labeled documents of the same document type."
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/train/custom-model?view=doc-intel-4.0.0

[FACT] Three custom model types exist: **Custom Neural** (mixed-type documents; structured, semistructured, unstructured), **Custom Template** (static layouts; highly structured documents), and **Custom Composed** (collection of custom models routed to a single endpoint by document type).
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0
Date: 2025-11-18

[FACT] **Custom Classification Models** identify document types before invoking an extraction model. Example use case: "A loan application package that contains application forms, pay slips, and bank statements."
URL: https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0
Date: 2025-11-18

---

## 5. Azure AI Search (Cognitive Services) — Speech, Vision, Language

### 5.1 Foundry Tools (formerly Azure Cognitive Services)

[FACT] "Foundry Tools is the new name for the product collection previously known as Azure AI Services or Azure Cognitive Services. Foundry Tools are Microsoft's suite of prebuilt AI capabilities—Vision, Speech, Language, Translator, Content Understanding, and Document Intelligence—designed to help organizations quickly add advanced AI features to their apps and agents."
URL: https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services

### 5.2 Speech

[FACT] Azure AI Speech (part of Foundry Tools) provides neural text-to-speech and speech-to-text via REST API. It is distinct from Azure OpenAI audio APIs, offering broader language support and custom voice training.
URL: https://docs.litellm.ai/docs/providers/azure_ai_speech

[FACT] Azure AI Speech supports language and voice enumeration via the REST endpoint `https://{region}.tts.speech.microsoft.com/cognitiveservices/voices/list`.
URL: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech

### 5.3 Vision

[FACT] Azure Vision services "enable applications to understand and analyze visual content such as images, videos, and scanned documents. These services use deep learning models to detect objects, identify faces, extract text, and more."
URL: https://k21academy.com/azure-aiml/azure-ai-services-overview-types-benefits/

[FACT] The Image Retrieval Vectorize Image API (under Foundry Tools/Vision) is the recommended API for generating embeddings for image content in Azure AI Search multimodal scenarios.
URL: https://learn.microsoft.com/en-us/azure/search/vector-search-overview
Date: 2026-01-15

### 5.4 Language

[FACT] Azure AI Language services offer: intelligent comprehension of written texts, emotion/sentiment decoding from text, translation, and bot/chat integrations.
URL: https://www.dev4side.com/en/blog/azure-cognitive-services

---

## 6. Azure AI Foundry (formerly Azure AI Studio)

### 6.1 Unified Platform

[FACT] "Azure AI Foundry (formerly Azure AI Studio) is a broader, unified platform-as-a-service for building, customizing, deploying, and managing AI applications and agents, giving you a unified workspace to build, evaluate, deploy, and manage AI applications at scale with features like prompt flow for designing complex workflows and safety evaluations."
URL: https://learn.microsoft.com/en-us/answers/questions/5572779/azure-openai-or-azure-ai-foundry

[FACT] Azure AI Studio/Foundry is described as "a unified platform designed to guide you through the entire AI lifecycle with an integrated, pro-code environment where teams can explore, build, test, and deploy next-generation AI applications using models from OpenAI, Meta, and Microsoft's Phi family."
URL: https://medium.com/@logicontech/azure-ai-studio-2025-enterprise-genai-apps-94b5f3946168

### 6.2 Prompt Flow

[FACT] "Prompt flow streamlines the entire prompt engineering process, from development and evaluation to deployment and monitoring, allowing you to effortlessly deploy your flows as Azure AI endpoints and monitor their performance in real-time."
URL: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/prompt-flow?view=foundry-classic

[FACT] Azure Prompt Flow is confirmed as a recommended tool in 2025, providing "a comprehensive solution for prototyping, experimenting, iterating, and deploying AI applications."
URL: https://learn.microsoft.com/en-us/answers/questions/2282880/is-azure-prompt-flow-suggested-to-use-in-2025

### 6.3 Evaluation

[FACT] "The evaluation flow is designed for evaluation scenarios and enables you to create a flow that takes the outputs of previous flow runs as inputs, allowing you to evaluate the performance of previous run results and output relevant metrics."
URL: https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow?view=azureml-api-2

---

## 7. Azure AI Content Safety

### 7.1 Prompt Shields

[FACT] "Prompt Shields is a unified API in Azure AI Content Safety that detects and blocks adversarial user input attacks on large language models (LLMs). It helps prevent harmful, unsafe, or policy-violating AI outputs by analyzing prompts and documents before content is generated."
URL: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
Date: 2025-11-21

[FACT] Prompt Shields detects two attack categories: **User Prompt attacks** (users attempting to alter intended LLM behavior via direct manipulation of system prompts or RLHF training) and **Document attacks** (third-party content containing embedded malicious instructions to gain unauthorized control over the LLM session).
URL: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
Date: 2025-11-21

[FACT] User Prompt attack subtypes detected include: Attempt to change system rules, Embedding a conversation mockup to confuse the model, Role-Play (assuming unrestricted persona), and Encoding Attacks (character transformations, ciphers, natural language variations to circumvent rules).
URL: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
Date: 2025-11-21

[FACT] Document attack subtypes detected include: Manipulated Content, system infrastructure intrusion, Information Gathering (data deletion/modification/theft), Availability attacks, Fraud, Malware spreading, system rule changes, conversation mockup embedding, role-play, and encoding attacks.
URL: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
Date: 2025-11-21

[FACT] "The Prompt Shields API and Protected Material for text API are now generally available (GA)."
URL: https://azure.microsoft.com/en-us/blog/enhance-ai-security-with-azure-prompt-shields-and-azure-ai-content-safety/

[FACT] "At Microsoft Build 2025, Microsoft announced Spotlighting, a powerful new capability that enhances Prompt Shields' ability to detect and block indirect prompt injection attacks by distinguishing between trusted and untrusted inputs."
URL: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/whats-new

[FACT] Prompt Shields language availability: "Models are trained and tested on Chinese, English, French, German, Spanish, Italian, Japanese, Portuguese. Other languages might work but with varying quality."
URL: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
Date: 2025-11-21

---

## 8. Aggregate Operational Comparison — All Azure AI/ML Services

The table below summarizes operational difficulty for an ISV adopting the full Azure AI/ML stack, assuming a mid-size deployment serving 50 enterprise customers. Assumptions: ISV owns the application layer; Azure manages infrastructure.

| Capability Domain | On-Premises | Managed K8s | Cloud-Native (Azure Managed) |
|---|---|---|---|
| **LLM Inference** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | GPU cluster, CUDA stack, serving framework | GPU operator, pod scheduling, autoscaler | PTU quota selection; zero infra |
| | NVIDIA Triton / vLLM / Ray Serve | Triton/vLLM on K8s | Azure OpenAI / Foundry Models |
| | Est. FTE: 2.0–3.0 | Est. FTE: 0.75–1.5 | Est. FTE: 0.1–0.25 |
| **Embeddings Generation** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-host embedding models; GPU or CPU, batching infra | Containerized embedding service; autoscaling | Azure OpenAI text-embedding-* via API |
| | SentenceTransformers / custom | Same, on K8s | Per-token billing |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05 |
| **Vector Search** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Qdrant/Weaviate/pgvector; manage storage, compaction | Helm-deployed vector DB, PVC, resource tuning | Azure AI Search; HNSW managed internally |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |
| **Document Processing** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Build/train OCR pipeline; manage model lifecycle | Containerized OCR service; scaling | Azure Document Intelligence; per-page billing |
| | Tesseract / custom deep learning | Same, on K8s | REST API; no model training required for prebuilts |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |
| **Content Safety / Guardrails** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Build and maintain classifiers; adversarial red-teaming | Self-hosted safety classifiers | Azure Content Safety + Prompt Shields (GA) |
| | Custom NLP classifiers | Custom containers | Per-request billing |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.05–0.1 |
| **ML Pipeline / Experiment Tracking** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-hosted MLflow; manage artifact store, DB, auth | MLflow on K8s; storage provisioning | Azure ML + AzureML MLflow-compatible workspaces |
| | MLflow, DVC, Weights & Biases | Same, on K8s | Managed workspaces; no MLflow server ops |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Prompt Observability / Eval** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Build logging/eval pipelines; no off-shelf tooling | Same + K8s ops | Azure AI Foundry Prompt Flow + Eval flows |
| | LangSmith / custom | LangSmith / custom | Prompt Flow; built-in metrics |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |

**Aggregate FTE Estimate (Cloud-Native ISV, 50 enterprise customers, full Azure AI stack):**
- Active operations: 0.5–1.0 FTE total across all AI/ML services
- On-call burden: 0.1–0.2 FTE (primarily for quota exhaustion, model deprecation events)
- Comparison — On-Premises equivalent: 6.0–11.0 FTE active + 1.0–2.0 FTE on-call

[UNVERIFIED] The FTE estimates above for on-premises and cloud-native are derived from aggregating per-domain estimates across this research file. No single third-party benchmark covers the precise ISV scenario described. Industry reference points (Gartner, Forrester) covering ML infrastructure staffing typically address enterprise IT teams rather than ISV product teams, and no 2025+ published benchmark was found that matches this specific profile.

---

## 9. Key Takeaways

- **Azure has consolidated its AI portfolio under Microsoft Foundry**, unifying model access (Azure OpenAI), experimentation (Prompt Flow), safety (Content Safety), document intelligence, search, and speech/vision/language under a single control plane — reducing the number of integration surfaces an ISV must manage.

- **Provisioned Throughput Units (PTU) are the production-grade LLM deployment model for ISVs**: PTUs provide deterministic latency, allocated capacity, and a leaky-bucket utilization model. However, quota does not guarantee regional capacity at deployment time, introducing a supply-side risk for high-growth ISVs that must be planned for.

- **Azure AI Search with integrated vectorization eliminates the vector database operations problem**: All regions and all tiers support vector search at no extra charge; ISVs avoid running Qdrant, Weaviate, or pgvector clusters. Reciprocal Rank Fusion (RRF) hybrid search is available out-of-the-box.

- **Prompt Shields (GA) and the Content Safety API provide a managed safety layer that would require 1.0–2.0 FTE to replicate on-premises**: The Spotlighting capability (announced Microsoft Build 2025) extends indirect prompt injection detection, a capability that is extremely difficult to self-build with equivalent coverage.

- **The aggregate FTE burden for operating the Azure AI/ML stack cloud-native is 0.5–1.0 FTE versus 6.0–11.0 FTE for an equivalent on-premises stack**, representing the primary economic rationale for cloud-native ISV deployment. The tradeoff is vendor lock-in at the API contract level and dependency on Microsoft's model deprecation and capacity allocation decisions.

---

## Related — Out of Scope

- **Azure compute infrastructure (VMs, AKS, GPU SKU selection)**: Covered in F16. The services documented here consume Azure compute but abstract it from the ISV operator.
- **Azure Networking and Private Endpoints for AI services**: Relevant to security posture (F04 scope) but not investigated here.
- **AWS and GCP equivalents to these services**: Covered in F17 (AWS) and F19 (GCP) respectively.
- **Pricing calculators and TCO models**: Not within F18 scope; referenced in F03 (Cost Economics).

---

## Sources

1. [Azure OpenAI / Foundry Models Provisioned Throughput Concepts](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic) — Microsoft Learn, updated 2026-02-10
2. [Azure OpenAI Service Pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/) — Microsoft Azure
3. [Azure OpenAI PTU Pricing Analysis](https://azure-noob.com/blog/azure-openai-pricing-real-costs/) — Azure Noob
4. [Provisioned Deployment for Fine-Tuning](https://azureaggregator.wordpress.com/2025/02/28/announcing-provisioned-deployment-for-azure-openai-service-fine-tuning/) — Azure Aggregator, 2025-02-28
5. [Azure OpenAI Content Filtering](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter?view=foundry-classic) — Microsoft Learn
6. [Fine-Tuning Safety Evaluation](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning-safety-evaluation?view=foundry-classic) — Microsoft Learn
7. [Azure ML Endpoints for Inference](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints?view=azureml-api-2) — Microsoft Learn, updated 2025-08-13
8. [Azure ML Online Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2) — Microsoft Learn
9. [MLflow and Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow?view=azureml-api-2) — Microsoft Learn
10. [Deploy MLflow Models to Online Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models-online-endpoints?view=azureml-api-2) — Microsoft Learn
11. [Responsible AI Dashboard](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2) — Microsoft Learn
12. [Machine Learning Fairness (Fairlearn)](https://learn.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml?view=azureml-api-2) — Microsoft Learn
13. [Vector Search Overview — Azure AI Search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) — Microsoft Learn, updated 2026-01-15
14. [Hybrid Search — Azure AI Search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview) — Microsoft Learn
15. [Integrated Vectorization — Azure AI Search](https://learn.microsoft.com/en-us/azure/search/vector-search-integrated-vectorization) — Microsoft Learn
16. [Azure AI Document Intelligence Overview v4.0](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0) — Microsoft Learn, updated 2025-11-18
17. [Document Intelligence Custom Models](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/train/custom-model?view=doc-intel-4.0.0) — Microsoft Learn
18. [Document Intelligence Read Model](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/read?view=doc-intel-4.0.0) — Microsoft Learn
19. [Azure AI Foundry Tools (Cognitive Services Overview)](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services) — Microsoft Learn
20. [Azure AI Speech REST API](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech) — Microsoft Learn
21. [Azure AI Foundry — Prompt Flow Concepts](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/prompt-flow?view=foundry-classic) — Microsoft Learn
22. [Is Azure Prompt Flow Suggested in 2025?](https://learn.microsoft.com/en-us/answers/questions/2282880/is-azure-prompt-flow-suggested-to-use-in-2025) — Microsoft Q&A
23. [Azure AI Studio 2025 Enterprise GenAI](https://medium.com/@logicontech/azure-ai-studio-2025-enterprise-genai-apps-94b5f3946168) — Medium / Logicontech
24. [Prompt Shields — Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) — Microsoft Learn, updated 2025-11-21
25. [What's New in Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/whats-new) — Microsoft Learn
26. [Enhance AI Security with Azure Prompt Shields](https://azure.microsoft.com/en-us/blog/enhance-ai-security-with-azure-prompt-shields-and-azure-ai-content-safety/) — Microsoft Azure Blog
27. [Content Safety in Foundry Control Plane](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) — Microsoft Azure
28. [Azure OpenAI or Azure AI Foundry](https://learn.microsoft.com/en-us/answers/questions/5572779/azure-openai-or-azure-ai-foundry) — Microsoft Q&A
29. [Azure AI Foundry Tools Products](https://azure.microsoft.com/en-us/products/ai-foundry/tools) — Microsoft Azure
