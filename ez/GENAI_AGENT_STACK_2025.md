# Comprehensive GenAI & Agent Development Stack (2024-2025)

A consolidated reference for the complete AI development and deployment technology landscape.

---

## Stack Overview

```

┌─────────────────────────────────────────────────────────────────────────────┐
│                        SECURITY & GOVERNANCE                                 │
│  Guardrails (NeMo, LlamaGuard) │ Governance (Credo AI, Fiddler)             │
│  Prompt Security (Lakera, Rebuff) │ Compliance (GDPR, HIPAA, SOC2)          │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        OBSERVABILITY & EVALUATION                            │
│  LangSmith │ Langfuse │ Arize Phoenix │ WhyLabs │ Helicone                  │
│  Eval: DeepEval │ RAGAS │ TruLens │ Red Team: PyRIT │ Garak │ DeepTeam      │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                           AGENTIC UI & MIDDLEWARE                            │
│  CopilotKit │ AG-UI Protocol │ Vercel AI SDK │ Chainlit │ Streamlit         │
│  MCP Protocol │ A2A Protocol │ Human-in-the-Loop │ HITL Platforms           │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AGENT FRAMEWORKS & ORCHESTRATION                      │
│  LangChain/LangGraph │ CrewAI │ AutoGen │ Semantic Kernel │ DSPy           │
│  RAG: LlamaIndex │ GraphRAG │ Patterns: ReAct, Plan-Execute                │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MEMORY, TOOLS & SANDBOXING                            │
│  Memory: Mem0 │ Zep │ LangMem │ Graphiti │ Buffer/Summary Patterns          │
│  Agent Tools: MCP Servers │ Browserbase │ Firecrawl │ Tavily │ E2B │ Jupyter│
│  Sandboxing: Modal │ Docker │ gVisor │ Firecracker │ AIO Sandbox            │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DATA MANAGEMENT & PIPELINES                           │
│  Pipelines: Airflow 3.0 │ Dagster │ Prefect │ Mage.ai │ dbt                 │
│  Feature Stores: Feast │ Tecton │ Hopsworks │ Databricks                    │
│  Versioning: DVC │ Delta Lake │ Apache Iceberg │ Data Quality              │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DATA & STORAGE                                        │
│  Vector DBs: Pinecone │ Weaviate │ Qdrant │ Milvus │ ChromaDB │ pgvector   │
│  Graph DBs: Neo4j │ Memgraph │ Document: Unstructured.io                    │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AI MODELS & FRAMEWORKS                                │
│  LLMs: GPT-4o/o1/o3 │ Claude 3.5/4 │ Gemini 2 │ Llama 3.x │ Qwen │ DeepSeek│
│  SLMs: Phi-4 │ Gemma │ Training: PyTorch │ DeepSpeed │ LoRA/QLoRA          │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DEPLOYMENT & INFERENCE                                │
│  Runtimes: vLLM │ TensorRT-LLM │ Triton │ TGI │ Ollama │ llama.cpp         │
│  Platforms: HuggingFace │ Replicate │ Modal │ Baseten │ Together │ Anyscale│
│  Gateway: LiteLLM │ OpenRouter │ Portkey │ Semantic Caching                 │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────────────┐
│                        INFRASTRUCTURE & HARDWARE                             │
│  GPUs: NVIDIA H100/H200/Blackwell │ AMD MI300X │ TPU v5/v6                  │
│  Cloud: AWS Bedrock │ Azure OpenAI │ GCP Vertex │ CoreWeave │ Lambda Labs  │
│  Edge: NVIDIA Jetson │ Apple Neural Engine │ WebLLM │ WebGPU               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Agentic UI Layer & Middleware (NEW)

### Agentic UI Frameworks

| Framework | Stars/Users | Key Features | License |
|-----------|-------------|--------------|---------|
| **CopilotKit** | 15K+ GitHub | AG-UI protocol, React-based, CoAgents | MIT |
| **Vercel AI SDK** | SDK 5.0 | AI Elements (July 2025), streaming | Apache 2.0 |
| **Chainlit** | v2.9.3, 6.7M/mo | Conversational AI UIs, Python | Apache 2.0 |
| **Streamlit** | Since 2019 | Python-first prototyping, quick iteration | Apache 2.0 |
| **Gradio** | 6.7M/mo, #1 trending | HuggingFace integrated, components | Apache 2.0 |

### AI Middleware & Protocols

| Protocol | Provider | Purpose | Status |
|----------|----------|---------|--------|
| **AG-UI** | CopilotKit | Agent-User Interface, 16 event types | MIT, 2025 |
| **MCP** | Anthropic | Model Context Protocol, JSON-RPC 2.0 | Nov 2024, 7K+ servers |
| **A2A** | Google → Linux Foundation | Agent-to-Agent, 50+ partners | Production 2025 |
| **ACP** | IBM Research | Structured dialogue, heterogeneous systems | Active |

**MCP Ecosystem**:
- Smithery.ai: 7,000+ first-party and community servers
- Docker MCP Hub: Distributes MCP servers as Docker images
- Native support in Claude Code, Cursor, VSCode

### Human-in-the-Loop (HITL)

| Platform | Type | Strengths |
|----------|------|-----------|
| **Scale AI** | Enterprise | Managed labeled datasets, gov/auto sectors |
| **Labelbox** | ML-focused | 70% cloud integration, data pipelines |
| **HumanLayer SDK** | Dev library | Approval workflows for agents |
| **Permit.io** | Authorization | Policy-based agent permissions |

**HITL Frameworks in Agents**: LangGraph checkpoints, CrewAI approval nodes, AutoGen human proxies

**Market Stats**: 18% CAGR in 2025, 30% legal tech using HITL

### Frontend Integration Patterns

- **React 19 + Zustand**: State management for agent UIs
- **SSE over WebSockets**: Comeback in 2025 for streaming
- **LangGraph Studio**: Visual agent state debugging
- **shadcn/ui**: Component library for AI interfaces

---

## 2. Infrastructure & Hardware Layer

### GPU/Accelerator Hardware

| Vendor | Product | Use Case | Key Specs |
|--------|---------|----------|-----------|
| **NVIDIA** | H100 | Training/Inference | 80GB HBM3, 3TB/s bandwidth |
| **NVIDIA** | H200 | Training/Inference | 141GB HBM3e, 4.8TB/s bandwidth |
| **NVIDIA** | Blackwell (B100/B200) | Next-gen training | FP4 support, 2x H100 perf |
| **AMD** | MI300X | Training/Inference | 192GB HBM3, competitive TCO |
| **Google** | TPU v5/v6 | Cloud training | Optimized for JAX/TensorFlow |
| **Groq** | LPU | Ultra-low latency inference | 500+ tokens/sec |
| **Cerebras** | WSE-3 | Training at scale | Wafer-scale engine |

### Cloud Providers for AI

| Provider | Service | Strengths |
|----------|---------|-----------|
| **AWS** | Bedrock, SageMaker | Broadest model selection, enterprise integration |
| **Azure** | OpenAI Service, ML | GPT-4 access, enterprise security |
| **GCP** | Vertex AI | Gemini access, TPU availability |
| **CoreWeave** | GPU Cloud | High GPU density, competitive pricing |
| **Lambda Labs** | GPU Cloud | Developer-friendly, on-demand H100s |
| **RunPod** | Serverless GPU | Pay-per-second, community models |

### Edge & On-Device AI

| Platform | Type | Performance |
|----------|------|-------------|
| **WebLLM** | Browser inference | 80% native speed, OpenAI API compatible |
| **WebGPU** | Browser API | 65% browser support (2025) |
| **NVIDIA Jetson** | Edge hardware | AGX Thor, AGX Orin, Orin Nano |
| **Apple Neural Engine** | On-device | 16-core, Apple Silicon optimized |
| **Bun 1.3** | JS runtime | Built-in AI server, WebGPU inference |

---

## 3. AI Models & Training Frameworks

### Large Language Models (LLMs)

#### Proprietary Models
| Model | Provider | Context | Strengths |
|-------|----------|---------|-----------|
| **GPT-4o** | OpenAI | 128K | Multimodal, fast |
| **GPT-o1/o3** | OpenAI | 200K | Reasoning, chain-of-thought |
| **GPT-5** | OpenAI | TBD | Latest flagship (Oct 2025) |
| **Claude 3.5 Sonnet** | Anthropic | 200K | Coding, analysis |
| **Claude Sonnet 4** | Anthropic | 1M (beta) | Extended context |
| **Gemini 2.0** | Google | 2M | Multimodal, long context |
| **Grok** | xAI | 128K | Real-time data |

#### Open Models
| Model | Provider | Parameters | License |
|-------|----------|------------|---------|
| **Llama 3.3** | Meta | 70B | Llama License |
| **Llama 3.2** | Meta | 1B-90B | Llama License |
| **Qwen 2.5** | Alibaba | 0.5B-72B | Apache 2.0 |
| **DeepSeek-V3** | DeepSeek | 671B MoE | MIT |
| **DeepSeek-R1** | DeepSeek | 671B | MIT (Reasoning) |
| **Mistral Large** | Mistral | 123B | Commercial |

### Small Language Models (SLMs)
- **Phi-4** (Microsoft): 14B, excellent reasoning
- **Gemma 2** (Google): 2B-27B, open weights
- **Llama 3.2 3B**: Edge-optimized

### Quantization Methods

| Method | Type | Best For |
|--------|------|----------|
| **GPTQ** | INT4/FP16 | GPU inference, 5x faster with Marlin |
| **AWQ** | Activation-aware | Better accuracy than GPTQ |
| **GGUF** | CPU-optimized | llama.cpp, edge devices |
| **bitsandbytes** | 4-bit | QLoRA fine-tuning |

### Fine-Tuning Techniques

| Technique | Memory | Use Case |
|-----------|--------|----------|
| **Full Fine-tuning** | High | Maximum customization |
| **LoRA** | Low | Efficient adaptation, few MB adapters |
| **QLoRA** | Very Low | 65B on 48GB GPU, 4-bit quantized |
| **PEFT** | Low | HuggingFace library, parameter-efficient |

---

## 4. Agent Frameworks & Orchestration

### Agent Frameworks Comparison

| Framework | Strengths | Performance | Best For |
|-----------|-----------|-------------|----------|
| **LangChain/LangGraph** | Ecosystem, $125M raised | 2.2x faster than CrewAI | Complex workflows |
| **CrewAI** | Role-based, simple | Role-focused teams | Multi-agent teams |
| **AutoGen** (Microsoft) | v0.4 rewrite, async | Event-driven | Microsoft ecosystem |
| **Semantic Kernel** | .NET/Python | Enterprise integration | Microsoft shops |
| **DSPy** (Stanford) | Self-optimizing | Programmatic prompts | Research, optimization |
| **Claude Agent SDK** | 85% token reduction | Native Claude | Claude-native apps |

### Orchestration Patterns

1. **ReAct** (Reasoning + Acting): Interleaved thought-action loops
2. **Plan-and-Execute**: Upfront planning, then execution
3. **Reflection**: Self-correction and improvement
4. **Multi-Agent Hierarchies**: Specialized agent teams
5. **Tool Calling**: Function calling with MCP protocol

### RAG Architecture

```
Query → Embedding → Vector Search → Reranking → Context → LLM → Response
                         ↓
              Knowledge Graph (optional)
```

**Advanced Patterns**:
- **GraphRAG** (Microsoft): Community summaries, 70-80% win rate
- **LazyGraphRAG**: 0.1% indexing cost of full GraphRAG
- **Agentic RAG**: Self-correcting retrieval with feedback loops
- **Multi-Modal RAG**: CLIP, Whisper, video understanding

---

## 5. Memory, Agent Tools & Sandboxing (NEW)

### Memory Systems

| System | Funding | Key Metrics | Features |
|--------|---------|-------------|----------|
| **Mem0** | $24M Series A | 26% accuracy boost, 91% lower latency | Graph memory, AWS SDK integration |
| **Zep** | $25M total | 94.8% DMR accuracy | Graphiti temporal KG, 1M+ downloads |
| **LangMem** | LangChain | Feb 2025 release | Semantic/episodic/procedural memory |
| **Graphiti** | Zep (open source) | Bi-temporal model | MCP server, Neo4j integration |

### Memory Types & Patterns

| Type | Implementation | Use Case |
|------|----------------|----------|
| **Short-term** | ConversationBufferMemory | Current conversation |
| **Long-term** | Vector stores, Mem0 | Persistent knowledge |
| **Episodic** | Mem0, Zep | Specific events, user history |
| **Semantic** | LangMem | Facts and knowledge |
| **Procedural** | LangMem | System behavior, response patterns |
| **Graph** | Graphiti, Neo4j | Temporal relationships |

### Agent Tools

#### Tool Frameworks & Registries

| Framework | Provider | Features |
|-----------|----------|----------|
| **LangChain Tools** | LangChain ($1.25B) | 1000+ integrations, Deep Agents |
| **OpenAI AgentKit** | OpenAI (Oct 2025) | Agent Builder, Connector Registry |
| **Claude Skills** | Anthropic (Oct 2025) | Folder-based abilities, on-demand loading |
| **MCP Servers** | Ecosystem | 7,000+ servers on Smithery.ai |

#### Code Execution Tools

| Tool | Type | Key Features |
|------|------|--------------|
| **E2B** | Code Interpreter SDK | Cloud sandbox, LangChain/CrewAI support |
| **Jupyter Kernels** | Notebook execution | RunCell, MCP Jupyter Server, kernel-aware agents |
| **Python REPL** | Local execution | LangChain tool, immediate feedback |

#### Web Browsing & Research Tools

| Tool | Funding/Growth | Capabilities |
|------|----------------|--------------|
| **Browserbase** | $40M Series B | 50M sessions, Director no-code, Stagehand framework |
| **Playwright for Agents** | Microsoft | AI-powered Planner/Generator/Healer, MCP integration |
| **Firecrawl** | 350K devs, 50K stars | Open Agent Builder, 96% web coverage |
| **Tavily** | $25M, 600K+ devs | AI-optimized search, 20 sites per API call |

#### Document & File Tools

| Tool | Type | Capabilities |
|------|------|--------------|
| **LlamaIndex Readers** | Document loaders | LlamaParse, confidence scores, hierarchical parsing |
| **Unstructured.io** | Document parsing | 97.9% table extraction, VLM-based processing |
| **File System Tools** | MCP servers | Read, write, search, Git operations |

### Sandboxing

| Platform | Isolation Type | Key Features |
|----------|---------------|--------------|
| **Modal Sandboxes** | gVisor | 50K+ concurrent, <1s startup, serverless |
| **Docker Sandboxes** | Container | Native Claude Code/Gemini CLI, Desktop 4.50+ |
| **E2B Sandbox** | Cloud VM | Secure isolated environments, E2B Desktop |
| **gVisor** | User-space kernel | Sentry process intercepts syscalls |
| **Firecracker** | microVM | AWS Lambda backend, minimal overhead |
| **AIO Sandbox** | All-in-one | Browser, Shell, File, MCP, VSCode in one container |

**Sandboxing Best Practices**:
- Isolate LLM-generated code from host systems
- Use gVisor or microVMs for defense in depth
- Disable network access for untrusted code
- Bind-mount only necessary directories

---

## 6. Data Management & Pipelines (NEW)

### Data Pipeline Orchestration

| Tool | Key Features | Pricing |
|------|--------------|---------|
| **Apache Airflow 3.0** | Edge Executor, event-driven, asset-centric | Open source |
| **Dagster** | Asset-centric, serverless | $10/mo+, $0.033/min compute |
| **Prefect** | Python-first, durable execution, FastMCP | Open source + Cloud |
| **Mage.ai** | Data-aware AI, 100+ integrations | Free open source |
| **dbt** | 60K teams, $100M ARR, Fusion Engine | Open source + Cloud |

### Feature Stores

| Platform | Type | Strengths |
|----------|------|-----------|
| **Feast** | Open source | Sub-ms latency, Red Hat OpenShift AI 2.20 |
| **Tecton** | Enterprise (→Databricks) | Usage-based ($1-5/credit) |
| **Hopsworks** | Platform | Sub-ms with RonDB, multi-cloud |
| **Databricks Feature Store** | Integrated | Unity Catalog, auto lineage |

### Data Versioning & Lineage

| Tool | Type | Key Features |
|------|------|--------------|
| **DVC** | Open source | Git-compatible, joined lakeFS |
| **Delta Lake 4.0** | Table format | Row tracking, time travel, 30-day retention |
| **Apache Iceberg v3** | Table format | ACID transactions, 50% scan time reduction |
| **Pachyderm** | Platform (→HPE) | Immutable commits, Kubernetes-based |

### ETL/ELT for AI Workloads

| Tool | Connectors | Pricing |
|------|------------|---------|
| **Fivetran** | 700+ | Per-connection MAR (March 2025 change) |
| **Airbyte** | 600+ | Open source, Fast Company's Most Innovative 2025 |
| **Unstructured.io** | 30+ | 15K free pages, $0.03/page, VLM-based |

### Data Quality & Validation

| Tool | Features |
|------|----------|
| **Great Expectations 1.9.2** | Python 3.10-3.13, GX Core/Cloud, Databricks integration |
| **Deequ** | Spark-based, AWS Glue integration, PyDeequ |
| **Soda** | SodaCL (25+ metrics), data contracts, AI-native |

### Streaming Data

| Platform | Performance | Use Case |
|----------|-------------|----------|
| **Apache Kafka 4.0** | MCP integration | ChatGPT backbone, real-time features |
| **Apache Flink 2.2.0** | ML_PREDICT, VECTOR_SEARCH | Real-time ML inference |
| **Spark Streaming Real-Time** | 5ms latency, p99 <300ms | Fraud detection |

---

## 7. Data Infrastructure & Storage

### Vector Databases

| Database | Type | Strengths | Users |
|----------|------|-----------|-------|
| **Pinecone** | Managed | Serverless, <50ms | Microsoft, Notion, Shopify |
| **Weaviate** | Open Source | Hybrid search, 1M+ Docker pulls | GPU acceleration |
| **Qdrant** | Open Source | Rust, 9K stars | Filtering, ACORN algo |
| **Milvus** | Open Source | 25K stars, 100B+ vectors | Salesforce, Walmart |
| **ChromaDB** | Embedded | Simple, lightweight | Prototyping |
| **pgvector** | PostgreSQL ext | SQL integration | Postgres users |

### Graph Databases

| Database | Strengths | Use Case |
|----------|-----------|----------|
| **Neo4j** | GraphRAG, LLM Builder, NODES 2025 | Knowledge graphs |
| **Memgraph** | In-memory, LangGraph + MCP | Sub-ms queries, Agentic GraphRAG |
| **Neptune** (AWS) | Managed, GraphStorm | AWS ecosystem |

### Knowledge Graph Integration

- **Neo4j + LangChain**: GraphCypherQAChain, LLMGraphTransformer
- **Memgraph + Cognee**: AI-driven semantic processing
- **Graphiti**: Temporal knowledge graphs with MCP server

---

## 8. MLOps, Inference & Deployment

### Inference Runtimes

| Runtime | Throughput | Best For |
|---------|------------|----------|
| **vLLM** | 2-4x over FasterTransformer | Production, PagedAttention |
| **TensorRT-LLM** | NVIDIA optimized | H100/Blackwell |
| **TGI v3** | 13x on long prompts | HuggingFace models, 200K+ tokens |
| **Ray Serve LLM** | Multi-node, disaggregated | Enterprise scale |
| **Ollama** | Local first | Development |
| **llama.cpp** | CPU inference | Edge, Apple Silicon |

### LLM Gateway & Routing

| Gateway | Providers | Pricing |
|---------|-----------|---------|
| **LiteLLM** | 100+ APIs | Open source, ~$30K/yr enterprise |
| **OpenRouter** | 300+ models | $500M valuation, `:nitro`/`:floor` routing |
| **Portkey** | 250+ providers | $49/mo+, fallback/load balancing |

### Semantic Caching

- **GPTCache**: LangChain/LlamaIndex integrated
- **MeanCache**: 17% higher F-score than GPTCache
- **Benefits**: 15-30% cost reduction, reduced latency

### Deployment Platforms

| Platform | Strengths | Pricing |
|----------|-----------|---------|
| **HuggingFace Endpoints** | Easy, 60K+ models | $0.03/CPU-hr, $0.50/GPU-hr |
| **Replicate** (→Cloudflare) | 50K+ models | Pay-per-use |
| **Modal** | Serverless, <1s cold start | $30 free/month |
| **Together AI** | 4x faster than vLLM | Low cost |
| **Anyscale** | Ray-based, distributed | Enterprise |

---

## 9. Observability & Evaluation

### LLM Observability

| Tool | Type | Strengths |
|------|------|-----------|
| **LangSmith** | LangChain native | OTel (March 2025), agent tracing |
| **Langfuse** | Open source (MIT) | Self-hostable, prompt management |
| **Arize Phoenix** | Open source | 7.8K stars, OTel native |
| **WhyLabs** | Privacy-focused | whylogs, drift detection |
| **Helicone** | Easy setup | 1-line integration, caching |

### Evaluation Frameworks

| Framework | Type | Key Features |
|-----------|------|--------------|
| **DeepEval** | Open source | 30+ metrics, "Pytest for LLMs" |
| **RAGAS** | RAG-specific | Faithfulness, relevancy, precision |
| **TruLens** | Qualitative | LangChain/LlamaIndex integrated, guardrails |
| **Promptfoo** | Testing | Unit testing, CI/CD integration |

### Red Teaming & Security Testing

| Tool | Provider | Capabilities |
|------|----------|--------------|
| **PyRIT** | Microsoft | Automated red teaming |
| **Garak** | NVIDIA | LLM vulnerability scanning |
| **DeepTeam** | Confident AI | 40+ vulnerabilities, multi-turn attacks |
| **PRISM Eval** | Research | 100% success rate vs 37/41 LLMs |

### Prompt Management

| Platform | Features |
|----------|----------|
| **PromptLayer** | "Git for prompts", versioning, A/B testing |
| **Humanloop** | Shutting down Sept 2025 |
| **Maxim AI** | End-to-end with evaluation, simulation |
| **LangSmith** | Prompt versioning, experimentation |

---

## 10. Security, Safety & Governance

### Guardrails & Safety

| Tool | Type | Capabilities |
|------|------|--------------|
| **NeMo Guardrails** | NVIDIA | Colang, NIM microservices, 50% better protection |
| **Guardrails AI** | Open source | Validators, Hub |
| **LlamaGuard 4** | Meta | 12B multimodal, 23 categories |
| **Nemotron Safety Guard 8B V3** | NVIDIA | 23 categories, 9 languages |

### Prompt Security

| Tool | Approach |
|------|----------|
| **Lakera Guard** | AI Firewall, Gandalf training data |
| **Rebuff** | Heuristics + LLM + VectorDB |
| **InjecGuard** | 30.8% better than baselines |

**2025 Finding**: 15% of organizations reported GenAI security incidents (up from 9% in 2024)

### AI Governance Platforms

| Platform | Recognition |
|----------|-------------|
| **Credo AI** | Forrester Wave Leader Q3 2025 |
| **Fiddler AI** | <100ms guardrails, SageMaker integrated |
| **Arthur AI** | Open-source Engine (March 2025) |
| **TruEra** | Acquired by Snowflake (May 2024) |

### Compliance Landscape

| Regulation | Status | Penalties |
|------------|--------|-----------|
| **EU AI Act** | Enforced Aug 2024 | Up to 7% revenue or €35M |
| **GDPR** | Active | Up to 4% revenue or €20M |
| **HIPAA** | Active | PHI safeguards, BAAs required |
| **SOC 2 Type II** | 8-11 months | 6-month operational period |

---

## 11. Cost Management & Optimization

### Token Usage & Routing

| Tool | Features | Model |
|------|----------|-------|
| **LiteLLM** | 100+ APIs, no markup | Pay provider directly |
| **OpenRouter** | Dynamic routing | `:nitro` (speed), `:floor` (cost) |
| **Portkey** | Load balancing, fallbacks | $49/mo+ |

### Semantic Caching

- **Cost Reduction**: 15-30% typical savings
- **API Pricing Range**: $0.25-$15/M input tokens, $1.25-$75/M output tokens
- **Tools**: GPTCache, MeanCache, ScyllaDB

### Context Compression

| Technique | Savings |
|-----------|---------|
| **Automatic Compression** | 40-60% token reduction |
| **Mem0 Memory Formation** | Selective fact extraction |
| **Cascading KV Cache** | 12% improvement on LongBench |

---

## 12. Multi-Modal AI

### Vision Integration

| Model | Purpose |
|-------|---------|
| **CLIP** | Text-image alignment, zero-shot retrieval |
| **GPT-4o/4.1** | Native multimodal |
| **Gemini 2.0** | Video, audio, text combined |

### Audio/Speech

| Model | Purpose |
|-------|---------|
| **Whisper** | Speech-to-text, high accuracy |
| **OpenAI TTS** | Text-to-speech |
| **Gemini 2.0** | Native audio understanding |

### Multi-Modal RAG

- **Ragie Platform** (July 2025): Visual search for videos
- **Multi-RAG System**: Video + audio + text reasoning
- **15-second chunks**: Optimal for Vision LLM descriptions

---

## Quick Reference: Technology Selection

### By Use Case

| Use Case | Recommended Stack |
|----------|-------------------|
| **RAG Application** | LangChain + Pinecone + GPT-4o |
| **Multi-Agent System** | LangGraph + CrewAI + Claude |
| **Agentic UI** | CopilotKit + Vercel AI SDK + MCP |
| **Local Development** | Ollama + Llama 3.2 + ChromaDB |
| **Enterprise Production** | vLLM + Azure OpenAI + LangSmith |
| **Cost-Optimized** | LiteLLM + Qwen + Langfuse |
| **Edge Deployment** | llama.cpp + Phi-4 + GGUF |
| **Data Pipelines** | Dagster + Feast + Delta Lake |

### By Scale

| Scale | Infrastructure | Models | Monitoring |
|-------|---------------|--------|------------|
| **Prototype** | Local/Modal | Ollama | Langfuse |
| **Startup** | RunPod/Replicate | GPT-4o-mini | Helicone |
| **Growth** | CoreWeave | GPT-4o/Claude | LangSmith |
| **Enterprise** | AWS/Azure | Multi-provider | Full stack |

---

## 2025 Key Trends

1. **Consolidation**: W&B → CoreWeave, Neptune → OpenAI, Replicate → Cloudflare, TruEra → Snowflake, Tecton → Databricks
2. **Agentic UI Explosion**: CopilotKit (15K stars), AG-UI protocol, MCP (7K+ servers)
3. **Memory as Infrastructure**: Mem0 ($24M), Zep ($25M), AWS exclusive integration
4. **Protocol Wars**: MCP (Anthropic) vs A2A (Google/Linux Foundation) vs ACP (IBM)
5. **LazyGraphRAG**: 0.1% cost of full GraphRAG with comparable quality
6. **Reasoning Models**: OpenAI o1/o3/o4, DeepSeek-R1, Claude thinking
7. **Edge AI**: WebLLM at 80% native speed, WebGPU 65% browser support
8. **Code Sandboxing**: Docker native support, Modal 50K concurrent, E2B growth
9. **Data Pipelines for AI**: Airflow 3.0, Dagster asset-centric, Feast/Tecton consolidation
10. **Evaluation Maturity**: DeepEval 30+ metrics, RAGAS, multi-turn red teaming

---

## Research Sources

This document consolidates research from 10 parallel research agents covering:
- Infrastructure & Hardware
- AI Models & Frameworks
- Agent Frameworks & Orchestration
- Data Infrastructure & Storage
- MLOps, Inference & Deployment
- Security, Safety & Governance
- **Agentic UI Layer & Middleware** (NEW)
- **Memory, Agent Tools & Sandboxing** (NEW)
- **Data Management & Pipelines** (NEW)
- **Additional Components** (NEW)

All facts sourced from official documentation, vendor announcements, and industry reports from 2024-2025.

---

*Generated: December 2025 (Updated)*
