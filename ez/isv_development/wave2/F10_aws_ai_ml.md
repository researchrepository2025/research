# F10: AWS AI/ML Services
**Research Agent:** F10 — AWS AI/ML Services
**Date:** 2026-02-18
**Scope:** AWS managed AI/ML services for LLM inference, embeddings, vector search, and ML pipelines

---

## Executive Summary

AWS operates one of the most comprehensive managed AI/ML portfolios available to ISVs, spanning the full spectrum from raw LLM inference (Amazon Bedrock) to end-to-end ML lifecycle tooling (Amazon SageMaker). Amazon Bedrock abstracts away all GPU infrastructure, model serving, and scaling complexity through a unified API that now provides access to nearly 100 serverless foundation models from more than a dozen providers, including Anthropic, Meta, Mistral, Google, and AWS's own Nova family. For ISVs building AI-driven SaaS products, Bedrock's fully managed character means zero operational overhead for LLM inference — the ISV writes no model-serving code and manages no inference infrastructure. SageMaker occupies a complementary position: it is the managed platform for custom model training, fine-tuning pipelines, and production inference endpoints where the ISV controls more of the model lifecycle. Taken together, these two services — plus adjacent managed services for vector search (OpenSearch), enterprise knowledge retrieval (Kendra), document intelligence (Textract, Comprehend, Rekognition), and developer AI (Amazon Q) — allow a small ISV engineering team to build sophisticated AI-native SaaS capabilities that would otherwise require substantial ML infrastructure expertise to operate self-hosted.

---

## Amazon Bedrock: Managed LLM Access

### Service Overview

Amazon Bedrock is described by AWS as ["a fully managed service that makes foundation models from leading AI startups and Amazon available through an API, offering a serverless experience where you can privately customize FMs with your own data and integrate them into applications without managing infrastructure."](https://aws.amazon.com/bedrock/) As of December 2025, [Amazon Bedrock provides nearly 100 serverless models](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-fully-managed-open-weight-models/) from providers including Anthropic, Meta, Mistral, Google, OpenAI, NVIDIA, Cohere, and AWS itself.

### Model Families Available

**Anthropic Claude Family:**
[Claude 3.5 Haiku and Claude 3.5 Sonnet are generally available in Amazon Bedrock.](https://www.aboutamazon.com/news/aws/amazon-bedrock-anthropic-ai-claude-3-5-sonnet) The upgraded Claude 3.5 Sonnet V2 is the current recommended version; [Claude 3.5 Sonnet V1 is being sunset in major regions on December 1, 2025.](https://github.com/posit-dev/positron/issues/9339) [Claude 3.5 Sonnet offers computer use capabilities in Amazon Bedrock in public beta.](https://aws.amazon.com/blogs/aws/upgraded-claude-3-5-sonnet-from-anthropic-available-now-computer-use-public-beta-and-claude-3-5-haiku-coming-soon-in-amazon-bedrock/)

**Amazon Nova Family (First-Party):**
[Amazon Nova 2 was announced December 2, 2025, delivering reasoning capabilities with industry-leading price performance.](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/) The Nova family spans:
- Nova Micro: fast text-to-text model
- Nova Lite: multimodal (text, images, video)
- Nova Pro: highest intelligence multimodal
- Nova Canvas: image generation
- Nova Reel: video generation
- [Nova 2 Omni: "the industry's first reasoning model that processes text, images, video, and speech inputs while natively generating both text and images"](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/)

**Nova 2 Extended Context:** [Nova 2 models provide a one-million-token context window, built-in tools including code interpreter and web grounding, and support remote MCP tools.](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/)

**December 2025 Open-Weight Expansion:**
[Amazon Bedrock added 18 fully managed open-weight models](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-fully-managed-open-weight-models/), including:
- Google: Gemma 3 (4B, 12B, 27B)
- Mistral AI: Mistral Large 3, Ministral 3 (3B, 8B, 14B)
- NVIDIA: Nemotron Nano 2 (9B, VL 12B)
- MiniMax AI: MiniMax M2
- Moonshot AI: Kimi K2 Thinking

### Intelligent Routing

[Amazon Bedrock can intelligently route requests between Claude 3.5 Sonnet and Claude 3 Haiku depending on the complexity of the prompt. Similarly, Amazon Bedrock can route requests between Meta Llama 3.3 70B and 3.1 8B, and Nova Pro and Nova Lite.](https://aws.amazon.com/bedrock/)

### Fine-Tuning

[Amazon Bedrock provides the ability to customize leading foundation models such as Anthropic's Claude 3 Haiku and Meta's Llama 3.1 through fine-tuning.](https://aws.amazon.com/blogs/machine-learning/fine-tune-llms-with-synthetic-data-for-context-based-qa-using-amazon-bedrock/) [Meta's Llama 3.2 models became available for fine-tuning in Amazon Bedrock in March 2025.](https://aws.amazon.com/about-aws/whats-new/2025/03/metas-llama-3-2-models-fine-tuning-amazon-bedrock/) Fine-tuned models are immediately available for on-demand inference under token-based pricing. [Reinforcement fine-tuning in Amazon Bedrock improves model accuracy without requiring deep machine learning expertise or large volumes of labeled data.](https://reinvent.awsevents.com/content/dam/reinvent/2024/slides/aim/AIM357_Customizing-models-for-enhanced-results-Fine-tuning-in-Amazon-Bedrock.pdf)

### Knowledge Bases (Managed RAG)

[Amazon Bedrock Knowledge Bases is a fully managed capability that helps you securely connect foundation models to your company data using Retrieval Augmented Generation (RAG), streamlining the entire RAG workflow from ingestion to retrieval and prompt augmentation, eliminating the need for custom data source integrations and data flow management.](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html) [Amazon Kendra GenAI Index is a managed RAG option within Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-kendra-genai-index-enhanced-semantic-search-and-retrieval-capabilities/), allowing customers to use Bedrock tooling such as agents and prompt flows atop Kendra's retrieval layer.

### Agents

[Bedrock Agents retain memory across interactions, offering personalized experiences and improving accuracy of multi-step tasks while recalling prior context when needed. Built-in action groups allow agents to execute Python code, similar to OpenAI's Code Interpreter plugin.](https://aws.plainenglish.io/implementing-rag-with-amazon-bedrock-knowledge-bases-agents-guardrails-pricing-explained-4c7b7c8ea9a2) [Agents include built-in Amazon Bedrock Guardrails for safety and reliability.](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html)

### Guardrails

[Amazon Bedrock Guardrails provides six safeguard policies: content moderation (content and word filters), prompt attack detection, topic classification (denied topics), PII redaction (sensitive information filters), and hallucination detection (contextual grounding and Automated Reasoning checks).](https://aws.amazon.com/bedrock/guardrails/) [Bedrock Guardrails can block up to 88% of harmful content and identify correct model responses with up to 99% accuracy to minimize hallucinations using Automated Reasoning checks.](https://aws.amazon.com/bedrock/guardrails/)

### AgentCore (2025 Platform Addition)

[Amazon Bedrock AgentCore is an agentic platform for building, deploying, and operating effective agents securely at scale — no infrastructure management needed.](https://aws.amazon.com/bedrock/agentcore/) [AgentCore Runtime addresses infrastructure challenges with a secure, serverless hosting environment specifically designed for AI agents and tools, handling container orchestration, session management, scalability, and security isolation.](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/) [Amazon Bedrock AgentCore Gateway is a fully managed service that provides a unified interface where agents can discover, access, and invoke tools, while abstracting away security, infrastructure, and protocol-level complexities.](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)

### Bedrock Pricing

[Amazon Bedrock offers on-demand pricing (pay per token), batch pricing, and provisioned throughput (model units reserved for fixed hourly rate).](https://aws.amazon.com/bedrock/pricing/) [Provisioned throughput options currently cover Amazon Titan, Anthropic, Cohere, Meta Llama, and Stability AI, ranging from $21.18 to $49.86 per hour per model unit for 1-month commitments.](https://www.oreateai.com/blog/navigating-amazon-bedrock-provisioned-throughput-pricing-a-look-towards-2025/42acd888aa61a407a3e29314eeae6a3c)

[New on-demand service tiers introduced in 2025:](https://aws.amazon.com/bedrock/service-tiers/)
- **Priority tier:** 75% premium to Standard — faster response times, prioritized compute
- **Flex tier:** 50% discount to Standard — cost-effective for non-time-critical workloads

**What Bedrock Abstracts Away for ISVs:**
- GPU cluster procurement, provisioning, and maintenance
- Model serving frameworks (vLLM, TGI, TensorRT-LLM)
- Auto-scaling inference infrastructure
- Model version management and deprecation handling
- Multi-region availability and failover
- Safety and guardrail enforcement infrastructure

---

## Amazon SageMaker: ML Training and Hosting Platform

### Service Overview

[Amazon SageMaker AI provides various inference options: real-time endpoints for low-latency inference, serverless endpoints for fully managed infrastructure and auto-scaling, and asynchronous endpoints for batches of requests.](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) SageMaker differs from Bedrock in that it is the managed platform for ISVs who need to train, fine-tune, and deploy their own custom models.

### Inference Endpoint Types

[Amazon SageMaker offers four inference deployment patterns:](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
1. **Real-time endpoints:** Low-latency synchronous inference
2. **Serverless endpoints:** Fully managed auto-scaling with zero idle cost
3. **Asynchronous endpoints:** For large payloads or long-running inference jobs
4. **Batch transform:** For bulk offline inference on datasets

### Inference Pipelines (Serial Chaining)

[An inference pipeline is a SageMaker model composed of a linear sequence of two to fifteen containers that process requests for inferences on data. You can use inference pipelines to define and deploy any combination of pretrained SageMaker built-in algorithms and your own custom algorithms packaged in Docker containers.](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) [Within an inference pipeline, SageMaker handles invocations as a sequence of HTTP requests — the first container processes and dispatches to the second, and so on, with the final response returned to the calling client.](https://aws.amazon.com/blogs/machine-learning/part-4-model-hosting-patterns-in-amazon-sagemaker-design-patterns-for-serial-inference-on-amazon-sagemaker/) [Because the containers are co-located on the same EC2 instance, overall pipeline latency is reduced.](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html)

### SageMaker Pipelines (ML Workflow Automation)

[Amazon SageMaker Pipelines is a serverless workflow orchestration service purpose-built for MLOps and LLMOps automation, enabling you to build, automate, and manage workflows for the complete ML lifecycle spanning data preparation, model training, and model deployment.](https://aws.amazon.com/sagemaker/ai/pipelines/) [A SageMaker pipeline is composed of a series of interconnected steps organized as a directed acyclic graph (DAG), which can be created using the drag-and-drop UI, the Pipelines SDK, or by defining it in a JSON schema.](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/) [Amazon SageMaker Pipelines can scale to run tens of thousands of concurrent ML workflows in production.](https://aws.amazon.com/sagemaker/ai/pipelines/) MLOps components include pipelines, model registry, and projects.

### JumpStart Foundation Models

[Amazon SageMaker JumpStart is a machine learning hub with foundation models, built-in algorithms, and prebuilt ML solutions that you can deploy with just a few clicks.](https://aws.amazon.com/sagemaker/ai/jumpstart/) [JumpStart offers foundation models from providers including AI21 Labs, Cohere, Databricks, Hugging Face, Meta, Mistral AI, Stability AI, and Alexa.](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html) [As of February 2026, SageMaker JumpStart enables one-click deployment of NVIDIA NIMs models for biosciences and physical AI, including ProteinMPNN, Nemotron-3.5B-Instruct, MSA Search NIM, and Cosmos Reason.](https://aws.amazon.com/about-aws/whats-new/2026/02/accelerate-biosciences-and-robotics-with-NVIDIA-NIMs-on-sagemaker-jumpstart/)

### Inference Optimization

[SageMaker provides an inference optimization job that enables techniques such as quantization and speculative decoding to reduce inference latency and cost.](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-create-job.html)

**What SageMaker Abstracts Away for ISVs:**
- Container orchestration for training jobs (distributed training across multi-node clusters)
- Spot instance management and interruption handling for training
- Hyperparameter tuning infrastructure
- Model artifact storage and versioning
- Endpoint scaling policies and capacity management
- MLOps pipeline DAG execution and dependency management

---

## Amazon Titan Embeddings

### Model Specifications

[Amazon Titan Text Embeddings V2 can intake up to 8,192 tokens or 50,000 characters and outputs a configurable vector of 256, 512, or 1,024 dimensions.](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) The default and maximum output dimension is 1,024.

### Pricing

[The Amazon Bedrock on-demand cost for Amazon Titan Text Embeddings V2 is $0.02 per million tokens ($0.00002 per 1,000 tokens).](https://aws.amazon.com/bedrock/pricing/) Pricing is based on the total number of tokens processed, not the number of API calls.

### API Access

[Amazon Titan Text Embeddings V2 is available through the fully managed, serverless experience on Amazon Bedrock via the Amazon Bedrock REST API or AWS SDK.](https://aws.amazon.com/blogs/machine-learning/get-started-with-amazon-titan-text-embeddings-v2-a-new-state-of-the-art-embeddings-model-on-amazon-bedrock/) [The model is optimized for improving RAG retrieval accuracy.](https://aws.amazon.com/blogs/aws/amazon-titan-text-v2-now-available-in-amazon-bedrock-optimized-for-improving-rag/)

**What Titan Embeddings Abstracts Away:**
- Embedding model infrastructure and GPU compute
- Model versioning and embedding dimension consistency
- Batch embedding job management
- Cross-region replication of embedding workloads

---

## Amazon Kendra: Enterprise Search with ML Ranking

### Service Overview

[Amazon Kendra GenAI Index is a new index designed for RAG and intelligent search to help enterprises build digital assistants and intelligent search experiences, offering high retrieval accuracy using advanced semantic models and the latest information retrieval technologies.](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-kendra-genai-index-enhanced-semantic-search-and-retrieval-capabilities/)

### Connectors and Data Sources

[Amazon Kendra GenAI Index supports connectors to 43 enterprise sources such as SharePoint, OneDrive, Google Drive, Salesforce, and others with integrated metadata-based user permissions filtering.](https://aws.amazon.com/kendra/features/) The service delivers [ML-powered instant answers, FAQs, and document ranking as a fully managed service.](https://aws.amazon.com/kendra/)

### ML Ranking and Relevance

[Kendra's Retriever API returns the most relevant passages with optimal granularity needed for LLM answer accuracy, includes user ACL filtering to return only passages the end-user is entitled to see, and provides relevance boosting to improve LLM answers by boosting specific content based on date, source repository, or any metadata.](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-kendra-genai-index-enhanced-semantic-search-and-retrieval-capabilities/) [Amazon Kendra uses ML to continuously optimize search results based on end-user search patterns and feedback, learning from user interactions using incremental learning techniques automatically.](https://www.netcomlearning.com/blog/amazon-kendra)

### RAG Integration

[Amazon Kendra GenAI Index is a managed RAG option within Amazon Bedrock Knowledge Bases, allowing customers to build generative AI assistants using Amazon Bedrock tooling such as agents and prompt flows.](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-kendra-genai-index-enhanced-semantic-search-and-retrieval-capabilities/)

---

## Amazon OpenSearch Service: Vector Search

### Vector Engine and kNN

[The vector engine for Amazon OpenSearch Service offers a scalable, secure, and high-performance vector database that allows storing and searching billions of high-dimensional vectors in milliseconds using advanced k-Nearest Neighbors (k-NN) and Approximate Nearest Neighbors (ANN) algorithms with Hierarchical Navigable Small World (HNSW) and Inverted File (IVF) implementations.](https://aws.amazon.com/opensearch-service/serverless-vector-database/)

### Hybrid Search

[OpenSearch provides hybrid search that blends lexical queries, k-Nearest Neighbor (k-NN) queries, and neural queries using the neural search plugin, implementing three levels of hybrid search: lexical filtering along with vectors, combining lexical and vector scores, and out-of-the-box score normalization and blending.](https://aws.amazon.com/blogs/big-data/hybrid-search-with-amazon-opensearch-service/) [Improvements in OpenSearch 2.17 include parallelization of query processing for hybrid search, delivering up to 25% improvement in latency.](https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-vector-database-capabilities-revisited/)

### GPU-Accelerated Indexing

[Amazon OpenSearch Service introduced GPU-accelerated vector (k-NN) indexing, enabling billion-scale vector databases to be built in under an hour and indexing vectors up to 10 times faster at a quarter of the cost compared to CPU-only indexing. The feature dynamically attaches serverless GPUs to boost domains and collections running CPU-based instances.](https://aws.amazon.com/blogs/big-data/build-billion-scale-vector-databases-in-under-an-hour-with-gpu-acceleration-on-amazon-opensearch-service/)

### Serverless Vector Collections Pricing

[Amazon OpenSearch Serverless charges compute capacity measured in OpenSearch Compute Units (OCUs). One OCU comprises 6 GB of RAM, corresponding vCPU, GP3 storage, and data transfer to S3. The smallest billable unit is 0.5 OCU, billed hourly with second-level granularity. Storage on S3 is billed separately by gigabyte-months.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html) [Vector search collections cannot share OCUs with search or time series collections.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)

---

## Amazon Textract, Comprehend, Rekognition: Document and Content Intelligence

### Amazon Textract (Document Processing)

[Amazon Textract is a machine learning service that automatically extracts text, handwriting, layout elements, and data from scanned documents, going beyond simple OCR to identify, understand, and extract specific data including key-value pairs and table structures from PDFs and image formats (JPEG, PNG, TIFF).](https://aws.amazon.com/textract/) [Textract supports customizable pretrained features to meet business-specific document processing needs.](https://cloudchipr.com/blog/aws-textract)

**Key Textract Capabilities:**
- Text and handwriting recognition (printed and handwritten)
- Form extraction (key-value pairs)
- Table structure extraction
- Layout element identification
- Integration with Comprehend for downstream NLP

### Amazon Comprehend (NLP)

[Amazon Comprehend is a natural language processing service that uses machine learning to discover insights from text, providing custom entity recognition, custom classification, keyphrase extraction, sentiment analysis, entity recognition, and PII detection APIs.](https://aws.amazon.com/comprehend/features/) [Targeted Sentiment, an advanced API, provides more granular sentiment insights by identifying the sentiment (positive, negative, neutral, or mixed) towards specific entities within text.](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html)

[Comprehend's free tier covers 50,000 units of text (5 million characters) per API per month.](https://aws.amazon.com/comprehend/pricing/) APIs eligible for free tier include Key Phrase Extraction, Sentiment, Targeted Sentiment, Entity Recognition, Language Detection, Event Detection, Syntax Analysis, Detect PII, Contains PII, and Prompt Safety Classification.

### Amazon Rekognition (Computer Vision)

[Amazon Rekognition identifies objects, people, text, scenes, and activities in images and videos without requiring deep machine learning expertise.](https://aws.amazon.com/rekognition/) [Rekognition can detect custom objects using automated machine learning (AutoML) with as few as 10 training images.](https://aws.amazon.com/rekognition/image-features/) [Rekognition Face Liveness is a fully managed ML feature to verify that a user is physically present in front of the camera, helping deter fraud during face-based identity verification.](https://aws.amazon.com/rekognition/image-features/)

**Key Rekognition Capabilities:**
- Object and scene detection (hundreds of labels)
- Facial analysis (age, emotions, attributes) and face comparison
- Text detection from images and video (multilingual)
- Unsafe/explicit content moderation
- Celebrity recognition
- Custom Labels for brand-specific object detection

---

## Amazon Q: Enterprise AI Assistant

### Amazon Q Business

[Amazon Q Business is a fully managed, generative-AI powered assistant configured to answer questions, provide summaries, generate content, and complete tasks based on enterprise data.](https://aws.amazon.com/q/business/) [Amazon Q Business provides over 40 fully managed connectors that bring data from popular enterprise applications, document repositories, chat applications, and knowledge management systems into a single index.](https://aws.amazon.com/q/business/connectors/) Connectors can be scheduled to automatically sync your index with your data source for always-current content search.

### Amazon Q Developer (Code Generation)

[Amazon Q Developer generates real-time code suggestions ranging from snippets to full functions based on comments and existing code, supporting over 25 programming languages including Java, Python, and JavaScript.](https://aws.amazon.com/q/developer/) [Amazon Q Developer's agentic capabilities can autonomously perform a range of tasks — implementing features, documenting, testing, reviewing, and refactoring code, and performing software upgrades.](https://aws.amazon.com/q/developer/features/)

[Amazon Q Developer announced a new agentic coding experience within the IDE in May 2025, providing intelligent task execution enabling Q Developer to modify files, generate code diffs, and run commands based on natural language instructions.](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-q-developer-agentic-coding-experience-ide/)

**Industry Adoption Figures:**
[BT Group reported accepting 37% of Amazon Q Developer's code suggestions. National Australia Bank reported a 50% acceptance rate.](https://aws.amazon.com/q/developer/features/) [AWS was named a Leader in the 2025 Gartner Magic Quadrant for AI Code Assistants for the second year in a row.](https://aws.amazon.com/blogs/devops/aws-named-as-a-leader-in-the-2025-gartner-magic-quadrant-for-ai-code-assistants/)

---

## SageMaker Ground Truth: Data Labeling and Human-in-the-Loop

### Overview

[Amazon SageMaker Ground Truth Reinforcement Learning from Human Feedback (RLHF) integrates human feedback into training machine learning models, especially LLMs and generative AI models, to align them better with human preferences.](https://medium.com/@rohithlyadalla/sagemaker-ground-truth-reinforcement-learning-from-human-feedback-42dbdbac202a) [RLHF on SageMaker Ground Truth simplifies managing the complex human annotation needed for fine-tuning foundation models.](https://aws.amazon.com/blogs/machine-learning/improving-your-llms-with-rlhf-on-amazon-sagemaker/)

### Workflow

[Human labelers in RLHF workflows compare different responses generated by the model to the same prompt and provide preferences by ranking or rating them. This preference data is then used to train a reward model that represents human values and quality requirements.](https://aws.amazon.com/sagemaker-ai/groundtruth/features/) [Ground Truth supports audio and video segmentation for RLHF to enhance speech synthesis and video generation models.](https://aws.amazon.com/blogs/machine-learning/enhance-speech-synthesis-and-video-generation-models-with-rlhf-using-audio-and-video-segmentation-in-amazon-sagemaker/)

### Ground Truth Plus (Managed Labeling Service)

[Amazon SageMaker Ground Truth Plus is a fully managed, turnkey data labeling service that uses an expert workforce — either AWS-employed or vetted third-party vendors — to deliver accurate annotations quickly while reducing labeling costs by up to 40%.](https://aws.amazon.com/blogs/machine-learning/high-quality-human-feedback-for-your-generative-ai-applications-from-amazon-sagemaker-ground-truth-plus/) [AWS handles workforce selection, workflow design, and quality assurance, with AWS experts selecting the best labeling workforce based on project requirements.](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp.html) [Lambda functions are now optional when creating custom labeling jobs, reducing workflow complexity.](https://aws.amazon.com/blogs/machine-learning/accelerate-custom-labeling-workflows-in-amazon-sagemaker-ground-truth-without-using-aws-lambda/)

---

## Operational Difficulty Comparison: AWS Managed AI/ML vs. Self-Hosted Equivalents

The table below rates operational difficulty for an ISV using AWS managed AI/ML services versus operating equivalent capabilities self-hosted on-premises or on self-managed Kubernetes. Assumptions: mid-size ISV serving 50 enterprise customers, moderate inference volume (1–10M tokens/day), 3–5 person ML/AI engineering team.

| Capability | On-Premises (Self-Hosted) | Managed K8s (Self-Hosted LLM) | AWS Cloud-Native (Bedrock/SageMaker) |
|---|---|---|---|
| **LLM Inference** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | vLLM/TGI on bare metal, GPU driver mgmt, model sharding | vLLM/TGI on GPU node pools, K8s autoscaling config | Bedrock API call; no GPU, no server, no scaling config |
| | GPU servers, CUDA, vLLM, TGI, Triton | GPU node pools, KServe/Seldon, vLLM | Amazon Bedrock API |
| | Est. FTE: 1.0–2.0 FTE + on-call | Est. FTE: 0.75–1.5 FTE + on-call | Est. FTE: 0.0–0.1 FTE |
| **Embedding Generation** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-host embedding model (e.g., all-MiniLM), GPU needed for speed | Embedding model pod, autoscaling, health checks | Titan Embeddings API ($0.02/M tokens) |
| | GPU server, SentenceTransformers, FastAPI | HuggingFace containers, KServe | Amazon Bedrock Titan Embeddings |
| | Est. FTE: 0.5–1.0 FTE | Est. FTE: 0.25–0.5 FTE | Est. FTE: 0.0 FTE |
| **Vector Search** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-hosted Qdrant/Weaviate/pgvector, capacity planning, backups | K8s deployment, persistent volumes, index rebuilds | OpenSearch Serverless (OCU-based billing) |
| | Qdrant, Weaviate, Milvus, pgvector | Self-hosted vector DB on K8s | Amazon OpenSearch Serverless |
| | Est. FTE: 0.5–1.0 FTE | Est. FTE: 0.25–0.5 FTE | Est. FTE: 0.1–0.25 FTE |
| **ML Training Pipelines** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | MLflow/Airflow self-hosted, GPU cluster mgmt, DVC, distributed training | Kubeflow Pipelines, GPU node provisioning | SageMaker Pipelines (serverless orchestration) |
| | Airflow, MLflow, Kubeflow, Ray | Kubeflow, Argo Workflows, MLflow | Amazon SageMaker Pipelines |
| | Est. FTE: 1.5–2.5 FTE | Est. FTE: 1.0–1.5 FTE | Est. FTE: 0.25–0.5 FTE |
| **Document Intelligence** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Tesseract OCR + custom NLP pipeline | Containerized Tesseract + spaCy + custom models | Textract + Comprehend API calls |
| | Tesseract, Apache Tika, spaCy | Custom containers, model serving | Amazon Textract, Amazon Comprehend |
| | Est. FTE: 0.5–1.0 FTE | Est. FTE: 0.25–0.5 FTE | Est. FTE: 0.0–0.1 FTE |
| **Enterprise Search / RAG** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Self-hosted Elasticsearch + embedding pipeline + reranker | Elasticsearch on K8s, embedding service, reranker pod | Kendra GenAI Index (43 connectors, managed ML ranking) |
| | Elasticsearch, Haystack, custom pipeline | ElasticSearch/OpenSearch on K8s | Amazon Kendra, Bedrock Knowledge Bases |
| | Est. FTE: 1.0–2.0 FTE | Est. FTE: 0.75–1.25 FTE | Est. FTE: 0.1–0.25 FTE |
| **Data Labeling / RLHF** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Build annotation platform, recruit annotators, QA workflow | Self-hosted Label Studio on K8s, workforce management | SageMaker Ground Truth Plus (managed workforce, 40% cost reduction) |
| | Label Studio, Prodigy, CVAT, custom workforce | Label Studio on K8s | SageMaker Ground Truth, Ground Truth Plus |
| | Est. FTE: 1.0–3.0 FTE | Est. FTE: 0.75–2.0 FTE | Est. FTE: 0.1–0.5 FTE |

---

## Key Takeaways

- **Bedrock eliminates LLM infrastructure entirely for ISVs:** An ISV can access Claude 3.5, Llama 3.x, Mistral, and 90+ additional models through a single API without managing any GPU infrastructure, model serving stack, or scaling logic. The operational FTE cost is effectively zero for inference itself; cost management and prompt engineering are the primary engineering tasks.

- **The AWS AI/ML portfolio covers the full ISV application stack:** AWS offers managed services at every layer an AI SaaS product requires — LLM inference (Bedrock), embeddings (Titan), vector search (OpenSearch Serverless), enterprise document retrieval (Kendra), custom ML training (SageMaker), data labeling (Ground Truth), and document/NLP intelligence (Textract, Comprehend, Rekognition). An ISV can build a production AI-native SaaS without operating any AI/ML infrastructure themselves.

- **Guardrails and safety tooling are first-class managed services:** Bedrock Guardrails provides [hallucination detection with up to 99% accuracy and harmful content blocking up to 88% effectiveness](https://aws.amazon.com/bedrock/guardrails/) as a managed, API-configurable layer — capabilities that would require substantial custom engineering in a self-hosted deployment.

- **SageMaker targets ISVs that need model customization control:** For ISVs that need to train proprietary models, manage fine-tuning pipelines, or run multi-step inference pipelines with custom preprocessing, SageMaker provides managed orchestration without requiring Kubernetes expertise. The operational difficulty drops from 4–5/5 self-hosted to approximately 2/5 on SageMaker for equivalent ML pipeline capabilities.

- **The shift to agentic AI is further reducing ISV operational burden:** [AgentCore Runtime and Gateway](https://aws.amazon.com/bedrock/agentcore/) (2025) abstract away agent hosting, session management, and tool invocation infrastructure under consumption-based pricing, extending Bedrock's "zero infrastructure" model to agentic workloads — a significant consideration for ISVs building AI agents as core product capabilities.

---

## Related — Out of Scope

- **AWS compute infrastructure (EC2, EKS, ECS):** GPU instance types, pricing, and Kubernetes node management for self-hosted AI workloads are covered in See [F08: AWS Compute Infrastructure] for detailed coverage of AWS compute options.
- **Azure AI/ML services:** Azure OpenAI Service, Azure ML Studio, and comparable Azure capabilities are covered in See [F11: Azure AI/ML Services] for detailed coverage.
- **GCP AI/ML services:** Google Vertex AI, Gemini API, and Cloud AI services are outside this agent's scope.
- **Cost optimization strategies across providers:** Cross-provider LLM cost benchmarking falls outside the AWS-specific scope of this agent.

---

## Sources

- [Amazon Bedrock Product Page — aws.amazon.com](https://aws.amazon.com/bedrock/)
- [Amazon Bedrock Pricing — aws.amazon.com](https://aws.amazon.com/bedrock/pricing/)
- [Amazon Bedrock Guardrails — aws.amazon.com](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon Bedrock On-Demand Service Tiers — aws.amazon.com](https://aws.amazon.com/bedrock/service-tiers/)
- [Amazon Bedrock AgentCore — aws.amazon.com](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Bedrock adds 18 fully managed open-weight models — aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-fully-managed-open-weight-models/)
- [Amazon Bedrock: 18 open-weight models blog — aws.amazon.com](https://aws.amazon.com/blogs/aws/amazon-bedrock-adds-fully-managed-open-weight-models/)
- [Amazon Nova 2 Foundation Models — aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2025/12/nova-2-foundation-models-amazon-bedrock/)
- [Amazon Nova Models product page — aws.amazon.com](https://aws.amazon.com/nova/models/)
- [Latency-Optimized Inference for Nova Pro — aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2025/03/latency-optimized-inference-amazon-nova-pro-foundation-model-bedrock/)
- [Anthropic Claude on Amazon Bedrock — aws.amazon.com](https://aws.amazon.com/bedrock/anthropic/)
- [Upgraded Claude 3.5 Sonnet + Computer Use — aws.amazon.com](https://aws.amazon.com/blogs/aws/upgraded-claude-3-5-sonnet-from-anthropic-available-now-computer-use-public-beta-and-claude-3-5-haiku-coming-soon-in-amazon-bedrock/)
- [Meta Llama 3.2 Fine-Tuning in Bedrock — aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2025/03/metas-llama-3-2-models-fine-tuning-amazon-bedrock/)
- [Fine-tune Claude 3 Haiku in Amazon Bedrock — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/)
- [Fine-tune LLMs with synthetic data — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/fine-tune-llms-with-synthetic-data-for-context-based-qa-using-amazon-bedrock/)
- [Fine-Tuning in Amazon Bedrock (re:Invent slides) — reinvent.awsevents.com](https://reinvent.awsevents.com/content/dam/reinvent/2024/slides/aim/AIM357_Customizing-models-for-enhanced-results-Fine-tuning-in-Amazon-Bedrock.pdf)
- [Amazon Bedrock Knowledge Bases — docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html)
- [Amazon Bedrock Guardrails — docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Agents Guardrail Integration — docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html)
- [Implementing RAG with Bedrock — aws.plainenglish.io](https://aws.plainenglish.io/implementing-rag-with-amazon-bedrock-knowledge-bases-agents-guardrails-pricing-explained-4c7b7c8ea9a2)
- [AgentCore Runtime Launch — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/)
- [AgentCore Gateway — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Amazon Bedrock Provisioned Throughput Pricing — oreateai.com](https://www.oreateai.com/blog/navigating-amazon-bedrock-provisioned-throughput-pricing-a-look-towards-2025/42acd888aa61a407a3e29314eeae6a3c)
- [Amazon SageMaker Deploy Models — docs.aws.amazon.com](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
- [SageMaker Real-Time Endpoints — docs.aws.amazon.com](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-deploy-models.html)
- [SageMaker Inference Pipelines — docs.aws.amazon.com](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html)
- [SageMaker Serial Inference Design Patterns — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/part-4-model-hosting-patterns-in-amazon-sagemaker-design-patterns-for-serial-inference-on-amazon-sagemaker/)
- [SageMaker Pipelines — aws.amazon.com](https://aws.amazon.com/sagemaker/ai/pipelines/)
- [Building and Scaling ML Workflows with SageMaker Pipelines — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)
- [SageMaker Inference Optimization — docs.aws.amazon.com](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-create-job.html)
- [SageMaker JumpStart — aws.amazon.com](https://aws.amazon.com/sagemaker/ai/jumpstart/)
- [SageMaker JumpStart Foundation Models — docs.aws.amazon.com](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html)
- [NVIDIA NIMs on SageMaker JumpStart — aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2026/02/accelerate-biosciences-and-robotics-with-NVIDIA-NIMs-on-sagemaker-jumpstart/)
- [Amazon Titan Text Embeddings — docs.aws.amazon.com](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html)
- [Titan Text Embeddings V2 Launch Blog — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/get-started-with-amazon-titan-text-embeddings-v2-a-new-state-of-the-art-embeddings-model-on-amazon-bedrock/)
- [Titan Embeddings V2 Optimized for RAG — aws.amazon.com](https://aws.amazon.com/blogs/aws/amazon-titan-text-v2-now-available-in-amazon-bedrock-optimized-for-improving-rag/)
- [Amazon Kendra Product Page — aws.amazon.com](https://aws.amazon.com/kendra/)
- [Amazon Kendra Features — aws.amazon.com](https://aws.amazon.com/kendra/features/)
- [Amazon Kendra GenAI Index — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-kendra-genai-index-enhanced-semantic-search-and-retrieval-capabilities/)
- [Amazon Kendra Explained 2025 — netcomlearning.com](https://www.netcomlearning.com/blog/amazon-kendra)
- [Amazon OpenSearch Vector Database — aws.amazon.com](https://aws.amazon.com/opensearch-service/serverless-vector-database/)
- [OpenSearch Vector Search — docs.aws.amazon.com](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html)
- [OpenSearch kNN — docs.aws.amazon.com](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html)
- [OpenSearch Hybrid Search — aws.amazon.com](https://aws.amazon.com/blogs/big-data/hybrid-search-with-amazon-opensearch-service/)
- [OpenSearch Vector Database Capabilities Revisited — aws.amazon.com](https://aws.amazon.com/blogs/big-data/amazon-opensearch-service-vector-database-capabilities-revisited/)
- [OpenSearch GPU-Accelerated Vector Indexing — aws.amazon.com](https://aws.amazon.com/blogs/big-data/build-billion-scale-vector-databases-in-under-an-hour-with-gpu-acceleration-on-amazon-opensearch-service/)
- [OpenSearch Serverless — docs.aws.amazon.com](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html)
- [OpenSearch Serverless Vector Collections — docs.aws.amazon.com](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)
- [Amazon Textract — aws.amazon.com](https://aws.amazon.com/textract/)
- [Amazon Comprehend Features — aws.amazon.com](https://aws.amazon.com/comprehend/features/)
- [Amazon Comprehend Pricing — aws.amazon.com](https://aws.amazon.com/comprehend/pricing/)
- [Comprehend Targeted Sentiment — docs.aws.amazon.com](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html)
- [Amazon Rekognition — aws.amazon.com](https://aws.amazon.com/rekognition/)
- [Amazon Rekognition Image Features — aws.amazon.com](https://aws.amazon.com/rekognition/image-features/)
- [Amazon Q — aws.amazon.com](https://aws.amazon.com/q/)
- [Amazon Q Business — aws.amazon.com](https://aws.amazon.com/q/business/)
- [Amazon Q Business Connectors — aws.amazon.com](https://aws.amazon.com/q/business/connectors/)
- [Amazon Q Developer — aws.amazon.com](https://aws.amazon.com/q/developer/)
- [Amazon Q Developer Features — aws.amazon.com](https://aws.amazon.com/q/developer/features/)
- [Amazon Q Developer Agentic IDE Experience — aws.amazon.com](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-q-developer-agentic-coding-experience-ide/)
- [AWS Named Leader in 2025 Gartner Magic Quadrant for AI Code Assistants — aws.amazon.com](https://aws.amazon.com/blogs/devops/aws-named-as-a-leader-in-the-2025-gartner-magic-quadrant-for-ai-code-assistants/)
- [SageMaker Ground Truth — aws.amazon.com](https://aws.amazon.com/sagemaker-ai/groundtruth/features/)
- [SageMaker Ground Truth FAQs — aws.amazon.com](https://aws.amazon.com/sagemaker/ai/groundtruth/faqs/)
- [Improving LLMs with RLHF on SageMaker — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/improving-your-llms-with-rlhf-on-amazon-sagemaker/)
- [SageMaker Ground Truth Plus Launch — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/high-quality-human-feedback-for-your-generative-ai-applications-from-amazon-sagemaker-ground-truth-plus/)
- [SageMaker Ground Truth Plus — docs.aws.amazon.com](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp.html)
- [Ground Truth Custom Labeling Without Lambda — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/accelerate-custom-labeling-workflows-in-amazon-sagemaker-ground-truth-without-using-aws-lambda/)
- [SageMaker Ground Truth RLHF (Medium) — medium.com](https://medium.com/@rohithlyadalla/sagemaker-ground-truth-reinforcement-learning-from-human-feedback-42dbdbac202a)
- [RLHF Audio/Video Segmentation — aws.amazon.com](https://aws.amazon.com/blogs/machine-learning/enhance-speech-synthesis-and-video-generation-models-with-rlhf-using-audio-and-video-segmentation-in-amazon-sagemaker/)
