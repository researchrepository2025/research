# F38: On-Premises AI Agent Infrastructure

## Executive Summary

Running AI agent frameworks and multi-agent systems entirely on-premises requires assembling and operating a full platform stack that managed cloud services provide as first-class primitives: tool registries, sandboxed execution environments, durable workflow engines, observability pipelines, and GPU schedulers. Unlike cloud-native alternatives — Amazon Bedrock AgentCore, Microsoft Foundry Agent Service, and LangSmith Cloud — which absorb infrastructure complexity behind API surfaces, an on-premises deployment forces an ISV or its customers to stand up and maintain each layer independently. The operational profile is high-to-very-high across most capability domains, demanding dedicated platform engineering talent with deep expertise in Kubernetes, distributed systems, and GPU operations. [Gartner predicts that by 2029, 70% of enterprises will deploy agentic AI as part of IT infrastructure operations](https://www.itential.com/resource/analyst-report/gartner-predicts-2026-ai-agents-will-reshape-infrastructure-operations/), making the build-vs-buy decision on agent infrastructure one of the defining architectural choices of the next three years. The principal benefit of on-premises deployment — complete data sovereignty and air-gap capability — comes at a cost of 2.0–4.0 FTE of platform engineering effort for a mid-size production deployment, plus significant capital expenditure on GPU hardware and storage.

---

## 1. Tool Registry and Execution

### 1.1 Self-Hosted Tool Registries

The Model Context Protocol (MCP), introduced by Anthropic in late 2024 and now the de facto standard for agent tool access, reached its [November 2025 specification release](http://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/) after one year of broad adoption. The [official MCP Registry launched in preview on September 8, 2025](http://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) at `registry.modelcontextprotocol.io`, and the [registry source code is open-source](https://github.com/modelcontextprotocol/registry), enabling enterprises to fork and self-host private sub-registries.

For on-premises deployments, an ISV must operate one or more self-hosted MCP servers that expose internal tools (databases, APIs, code executors) to agent frameworks. Key operational requirements include:

- **Service discovery**: agents must resolve tool endpoints without relying on a centralized cloud registry
- **Authentication**: mutual TLS or token-based auth between agents and tool servers, enforced at the network layer
- **Versioning**: tool schema changes must be backward-compatible or require coordinated agent rollouts
- **Health checking**: tool server availability must be monitored continuously; a failed tool server causes agent task failures

The [MCP ecosystem vision establishes Enterprise Registries](https://modelcontextprotocol.info/tools/registry/) as a tier within the broader registry hierarchy — private sub-registries with curated entries, security scanning, and governance controls. Running this layer on-premises requires a self-managed API server, a metadata store (typically PostgreSQL), and an optional vulnerability scanning pipeline.

### 1.2 Sandboxed Code Execution

When agents execute LLM-generated code (a common capability in data-analysis and automation agents), on-premises deployments must provide their own sandboxed execution environments. Three isolation technologies are in production use as of 2025:

[**Firecracker microVMs**](https://www.codeant.ai/blogs/agentic-rag-shell-sandboxing): Hardware-level isolation where each workload gets its own dedicated Linux kernel running inside KVM. Boots in approximately 125ms, with less than 5 MiB overhead per VM, supporting up to 150 VMs per second per host. Used by AWS Lambda and E2B internally.

[**gVisor**](https://www.codeant.ai/blogs/agentic-rag-shell-sandboxing): A user-space application kernel written in Go (developed at Google). Intercepts syscalls before they reach the host kernel, drastically reducing kernel attack surface. Less isolation than Firecracker but lower overhead; suitable for semi-trusted workloads.

[**Kata Containers**](https://www.codeant.ai/blogs/agentic-rag-shell-sandboxing): Container-compatible microVM runtime combining OCI interface compatibility with hardware-level VM isolation. Integrates natively with Kubernetes via the CRI-O or containerd runtimes.

The [Kubernetes SIG Apps Agent Sandbox project](https://github.com/kubernetes-sigs/agent-sandbox), announced at KubeCon NA 2025 as a CNCF project, provides a declarative Kubernetes controller specifically for agent code execution. It is [foundationally built on gVisor with additional Kata Containers support](https://techinformed.com/google-launches-agent-sandbox-for-secure-ai-agents-on-kubernetes/), and introduces three custom resource definitions: `Sandbox`, `SandboxTemplate`, and `SandboxClaim`. Its Warm Pool Orchestrator maintains pre-warmed pods to [reduce cold startup latency to less than one second](https://agent-sandbox.sigs.k8s.io/).

For teams unwilling to build on Agent Sandbox, [Microsandbox](https://northflank.com/blog/self-hostable-alternatives-to-e2b-for-ai-agents) is an open-source self-hosted platform using libkrun microVM isolation with OCI compatibility. Its initial public release was May 20, 2025. It carries explicit [experimental warnings](https://northflank.com/blog/self-hostable-alternatives-to-e2b-for-ai-agents) with expected breaking changes. [E2B's self-hosting path](https://northflank.com/blog/self-hostable-alternatives-to-e2b-for-ai-agents) uses Terraform and Nomad, requiring Nomad orchestration expertise — a significant operational barrier for Kubernetes-native shops.

> [UNVERIFIED] Operational cost for a production-grade self-hosted sandbox layer (including monitoring, autoscaling, and security patching) is estimated at 0.5–1.0 FTE of platform engineering. No published benchmark was found for this specific scope; estimate is derived from general Kubernetes operator patterns and the Microsandbox and Agent Sandbox documentation complexity.

### 1.3 API Integration Without Managed Function Services

Cloud-native agent platforms provide managed "gateway" services that convert REST APIs and Lambda functions into agent-compatible tools automatically (e.g., [Amazon Bedrock AgentCore Gateway](https://aws.amazon.com/bedrock/agentcore/)). On-premises equivalents require:

- A self-hosted API gateway (Kong, Traefik, or NGINX with custom middleware) with tool-call routing
- Schema registry (OpenAPI spec storage) for tool discovery by agents
- Request/response logging pipeline feeding the observability stack
- Rate limiting and circuit breaker configuration per tool endpoint

---

## 2. State Management

### 2.1 Agent Conversation State and Checkpointing

Long-running agent workflows — particularly those involving human-in-the-loop steps, multi-day tasks, or retryable computation — require durable state storage. LangGraph, the dominant open-source multi-agent orchestration framework, uses a checkpointer abstraction with two production-ready backends:

[**langgraph-checkpoint-postgres**](https://docs.langchain.com/oss/javascript/langgraph/persistence): Recommended for production workloads. Uses PostgreSQL's `AsyncPostgresSaver` with standard connection pooling. Stores full graph state snapshots at every super-step, enabling time-travel debugging and fault recovery.

[**langgraph-checkpoint-redis**](https://redis.io/blog/langgraph-redis-checkpoint-010/): Version 0.1.0 (released 2025) represents a "fundamental redesign — not just optimizations, but a complete rethinking of how to structure checkpoint data for a high-performance in-memory data store." Provides [thread-level persistence](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/) allowing agents to maintain continuity across sessions. Suited for high-frequency, low-latency checkpoint access.

### 2.2 Redis for Active Session State

[Redis provides sub-millisecond read/write operations](https://redis.io/blog/ai-agent-orchestration/) for active session state, supporting thousands of concurrent agent interactions. Specific data structures used in production agent deployments:

- **Redis Streams**: Event-driven agent communication with replay capability for debugging; supports temporal decoupling between agents
- **Vector Search**: Semantic memory retrieval for multi-agent context sharing; [claimed 100% recall accuracy](https://redis.io/blog/ai-agent-orchestration/) in controlled benchmarks
- **Redis LangCache**: Semantic caching layer that [achieves 70% cache hit rates, reducing LLM API costs by up to 70%](https://redis.io/blog/ai-agent-orchestration/) by avoiding redundant inference calls on semantically equivalent queries

### 2.3 PostgreSQL as Authoritative State Store

In production multi-agent deployments, PostgreSQL serves as the authoritative persistence layer for agent workflow state, namespace configuration, and audit records. A [wealth management multi-agent platform case study](https://medium.com/@brianyang/building-a-multi-agent-orchestration-platform-for-wealth-management-ai-what-i-learned-80673357e64c) used PostgreSQL with pgvector for embeddings alongside Redis for session caching — a pattern now common in on-premises agent deployments.

[Temporal](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration), the open-source durable workflow engine (MIT license, self-hostable at no cost), also uses PostgreSQL (or Cassandra) as its persistence layer, storing complete workflow event histories, task queues, and namespace configurations.

---

## 3. Orchestration: Multi-Agent Coordination Without Managed Workflow Services

### 3.1 Task Queues vs. Workflow Engines

On-premises multi-agent orchestration requires a deliberate choice between two architectural patterns:

**Celery + Redis/RabbitMQ**: Appropriate for simple async LLM calls and single-step tool invocations. Celery is a mature distributed task queue suitable for ML jobs; [Celery + RabbitMQ is described as "a great backbone for distributed AI agent workflows"](https://medium.com/@pranavprakash4777/modern-queueing-architectures-celery-rabbitmq-redis-or-temporal-f93ea7c526ec). Lacks durable state — a worker crash loses in-flight task state.

**Temporal**: Explicitly designed for [multi-step AI agent workflows requiring durable state management, long-running processes (days/months), and complex compensation logic](https://medium.com/@pranavprakash4777/modern-queueing-architectures-celery-rabbitmq-redis-or-temporal-f93ea7c526ec). Temporal provides "durable virtual memory" — when any component fails, workflows automatically reconstitute from stored history and continue from their last checkpoint. [PydanticAI documents native Temporal integration](https://ai.pydantic.dev/durable_execution/temporal/) for durable agent execution.

Self-hosting Temporal requires: a Temporal cluster (Go service), PostgreSQL or Cassandra persistence layer, worker processes (built with Temporal SDKs in Python, Go, Java, or TypeScript), and a Temporal Web UI for operational visibility.

### 3.2 Supervisor Patterns and Handoffs

The [Vectara on-premises orchestration architecture guide](https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration) identifies five core layers an on-premises agent platform must implement independently: state management, communication protocols, orchestration patterns, tool integration, and error recovery. Supervisor patterns (one agent routing tasks to specialized sub-agents) require:

- **Message bus**: Kafka, NATS, or RabbitMQ for loosely coupled inter-agent communication with event replay
- **Distributed system patterns**: timeout handling, idempotent operations, circuit breakers — all self-implemented
- **Shared context store**: cross-agent state accessible at sub-millisecond latency (Redis or shared PostgreSQL schema)

The Vectara guide explicitly states prerequisites for on-premises agent orchestration: "Comfort with Kubernetes or similar orchestrators. Basic understanding of MLOps/ModelOps concepts. Familiarity with enterprise security (IAM, network zoning, logging)." And critically: "If none of those are in place, your first architecture decision is staffing."

### 3.3 Scaling Concurrent Agent Sessions

[NVIDIA KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler), open-sourced in January 2025 under the Apache 2.0 license, is the production-ready Kubernetes-native GPU scheduler for concurrent AI workloads. It supports:

- Fractional GPU requests (MIG/MPS partitioning)
- Gang scheduling for multi-GPU agent inference jobs (all GPUs allocated atomically)
- Queue-based quotas and priorities for multi-team governance
- [Topology-aware scheduling](https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler/) to keep co-located agents on fast NVLink or InfiniBand fabric

A [hybrid Kubernetes deployment using HAMi GPU virtualization](https://debugg.ai/resources/kubernetes-gpu-scheduling-2025-kueue-volcano-mig) reported 10,000+ Pods running concurrently with GPU utilization improving from 13% to 37% (approximately 3x) — illustrating the scheduling optimization opportunity on-premises GPU clusters have but must actively manage.

---

## 4. Cost and Usage Tracking: Self-Hosted Metering

Cloud platforms provide per-request metering as a first-class feature. On-premises deployments must build or deploy a metering stack composed of:

### 4.1 OpenTelemetry Semantic Conventions for GenAI

The [OpenTelemetry GenAI SIG](https://opentelemetry.io/blog/2025/ai-agent-observability/) has finalized an "AI agent application semantic convention" based on Google's AI agent white paper. Experimental GenAI semantic conventions are defined at `/docs/specs/semconv/gen-ai/`, covering LLM/model telemetry, vector database operations, and agent execution flows. A common semantic convention for all major agent frameworks (CrewAI, AutoGen, LangGraph) is under active development in [OTel issue #1530](https://opentelemetry.io/blog/2025/ai-agent-observability/).

[OpenTelemetry semantic conventions for generative AI metrics](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/) define standard metric names for token counts, request volume, latency, and error rates — providing a shared vocabulary for cost attribution.

### 4.2 Self-Hosted Observability Stack Options

**Langfuse** (open-source, Apache 2.0): The most complete self-hosted LLM observability platform. [Production deployment requires](https://langfuse.com/self-hosting): PostgreSQL (transactional data), ClickHouse (high-volume traces and feedback — OLAP), Redis/Valkey (queue and cache), and S3/blob storage (trace artifacts). [Kubernetes with Helm is the preferred production deployment path](https://langfuse.com/self-hosting). Tracks token costs across 800+ models with automatic threading of multi-turn agent conversations.

**LangSmith Self-Hosted**: [Enterprise plan add-on](https://docs.langchain.com/langsmith/self-hosted) (requires license key and sales engagement). Requires Kubernetes for the full platform (observability + deployment). Database dependencies mirror Langfuse: PostgreSQL, ClickHouse, Redis, and blob storage. [Explicitly warns](https://docs.langchain.com/langsmith/self-hosted): "Do not run standalone servers in serverless environments. Scale-to-zero may cause task loss and scaling up will not work reliably."

**AI Observer**: [A self-hosted, single-binary, OpenTelemetry-compatible observability backend](https://github.com/tobilg/ai-observer) specifically for monitoring local AI coding tools, with a built-in pricing system for cost calculation. Lower operational complexity than Langfuse but narrower feature scope.

---

## 5. Security Sandboxing

### 5.1 Threat Model: Prompt Injection to Code Execution

[Running AI-generated code directly on application servers without a proper sandbox](https://northflank.com/blog/best-code-execution-sandbox-for-ai-agents) creates attack surface for: secret exfiltration, resource exhaustion, container escape, and malicious operations triggered through prompt injection. The on-premises ISV must implement defense-in-depth at the execution layer, as no managed guardrail service is present.

### 5.2 Isolation Technology Selection Matrix

| Technology | Isolation Level | Startup Time | Overhead | Self-Hosting Complexity |
|---|---|---|---|---|
| Firecracker microVM | Hardware (dedicated kernel) | ~125ms | <5 MiB/VM | High — requires KVM, Nomad or custom orchestration |
| Kata Containers | Hardware (VM-backed) | ~1s (warm pool: <1s) | Moderate | Moderate — Kubernetes CRI plugin |
| gVisor (runsc) | Syscall interception (user-space kernel) | <100ms | Low-moderate | Low — Kubernetes RuntimeClass |
| Standard containers | Namespace/cgroup isolation | <10ms | Minimal | Trivial — but unsuitable for untrusted code |

Sources: [Northflank sandbox guide](https://northflank.com/blog/how-to-sandbox-ai-agents), [Agent Sandbox docs](https://agent-sandbox.sigs.k8s.io/), [CodeAnt sandboxing guide](https://www.codeant.ai/blogs/agentic-rag-shell-sandboxing)

### 5.3 Network and Identity Controls

The [Vectara on-premises architecture guide](https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration) specifies required security controls: zero-trust service meshes with mutual TLS, least-privilege credentials with short-lived tokens and rotation, network segmentation between agent tiers, and immutable audit logs tracking all inputs, tool calls, outputs, and decisions.

[Redis production deployment requirements for agent infrastructure](https://redis.io/blog/ai-agent-orchestration/) include: service-to-service authentication, encryption in transit and at rest, rate limiting for runaway agent loops, and retry policies with exponential backoff.

---

## 6. Observability: Tracing Multi-Step Agent Reasoning

### 6.1 What On-Premises Observability Must Provide

Multi-agent systems produce non-linear execution traces where a single user request may spawn dozens of LLM calls, tool invocations, and sub-agent handoffs. The observability stack must capture:

- **Distributed traces** across agent hops (parent-child span relationships)
- **Decision chain logging**: which tool was chosen and why, at every step
- **Token attribution**: prompt tokens, completion tokens, and model name per span
- **State diffs**: what changed in agent memory/context at each checkpoint
- **Error classification**: LLM refusals, tool failures, timeout events, and prompt injection detections

The [OpenTelemetry GenAI SIG defines observability for agents as covering](https://opentelemetry.io/blog/2025/ai-agent-observability/) LLM/model telemetry, vector database operations, and agent execution flows. Instrumentation libraries focus on "capturing semantics that matter for agents: prompt/response bodies, token counts, model metadata, cost attributes, and relevant tool spans."

### 6.2 Self-Hosted Infrastructure Requirements

A production-grade on-premises agent observability stack (per [Langfuse self-hosting documentation](https://langfuse.com/self-hosting)) requires four independently operated components:

1. **Langfuse Web + Worker containers** — trace ingestion and UI serving
2. **PostgreSQL** — transactional metadata (projects, users, prompts)
3. **ClickHouse** — high-volume OLAP store for traces, observations, and scores; required for any production trace volume
4. **Redis/Valkey** — queue and cache for async event processing
5. **S3-compatible blob storage** — multi-modal inputs and large trace exports

For F51 self-hosted tracing integration, see [F51: Agent Observability and Tracing] for detailed coverage of tracing pipeline architecture.

[VictoriaMetrics](https://victoriametrics.com/blog/ai-agents-observability/) provides a self-hosted OpenTelemetry-compatible metrics backend that pairs with Langfuse for complete agent observability — storing OpenTelemetry metrics, logs, and traces in a single on-premises deployment.

---

## 7. Scaling: Concurrent Agent Sessions and GPU Scheduling

### 7.1 Queue Management for Concurrent Agent Runs

Each concurrent agent session consumes: one or more LLM inference slots (GPU memory), tool execution slots (sandbox capacity), and persistent state in Redis/PostgreSQL. Under load, on-premises deployments must implement:

- **Request queuing** at the agent entry point (preventing GPU memory exhaustion)
- **Session isolation** to prevent one agent's state from polluting another's context
- **Backpressure signaling** from the inference layer to the orchestration layer
- **Priority queues** for SLA-differentiated workloads (interactive vs. batch agents)

[A LangGraph distributed workflow engine design](https://medium.com/@mukshobhit/scaling-ai-powered-agents-building-a-distributed-langgraph-workflow-engine-13e57e368953) uses Celery workers with Redis as broker, with each worker handling one agent session graph execution. Horizontal scaling is achieved by adding worker replicas — straightforward in Kubernetes but requiring careful Redis connection pool sizing.

### 7.2 GPU Scheduling for Agent LLM Calls

[NVIDIA KAI Scheduler](https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/) (open-sourced January 2025, Apache 2.0) supports the full AI lifecycle, from interactive jobs to large inference, in a single cluster. For agent-specific workloads:

- **Fractional GPU requests**: Multiple simultaneous agent LLM calls can share a single GPU via MIG (Multi-Instance GPU) or MPS (Multi-Process Service)
- **Gang scheduling**: Agent sessions requiring multi-GPU inference (large models) receive all GPUs atomically, eliminating partial-allocation deadlocks
- **Queue-based fairness**: Separate queues for interactive agent sessions (low latency SLA) vs. batch agent runs (throughput SLA)

[NVIDIA Grove](https://developer.nvidia.com/blog/streamline-complex-ai-inference-on-kubernetes-with-nvidia-grove/) integrates with KAI's topology-aware scheduling to orchestrate disaggregated serving and agentic pipelines at scale on on-premises Kubernetes clusters.

---

## 8. Comparison: What Managed Platforms Eliminate

The table below itemizes infrastructure components that managed agent platforms absorb versus what an on-premises ISV must self-operate.

| Infrastructure Layer | On-Prem | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Tool Registry** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-host MCP registry on K8s; manage versioning, auth, health | Self-host MCP on managed K8s; cloud storage for schema artifacts | Amazon Bedrock AgentCore Gateway; Azure Foundry MCP Server |
| | MCP server (open-source), PostgreSQL, API gateway | MCP server + managed PostgreSQL (RDS/Cloud SQL) | Fully managed; no user-operated infrastructure |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **State Management** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-host Redis cluster + PostgreSQL HA + backups + patching | Managed Redis (ElastiCache/Memorystore) + managed PostgreSQL | Bedrock session memory; Foundry persistent memory |
| | Redis, PostgreSQL, langgraph-checkpoint-postgres/redis | Managed equivalents with K8s app layer | Fully managed memory service |
| | Est. FTE: 0.5–0.75 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **Workflow Orchestration** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-host Temporal cluster + workers + persistence; or Celery + broker | Self-host Temporal on managed K8s; managed PostgreSQL backend | Bedrock agent runtime (8-hour async); Foundry Agent Service runtime |
| | Temporal (MIT), Celery, RabbitMQ/Redis | Temporal on K8s + managed DB | Fully managed; serverless execution |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0 |
| **Code Execution Sandbox** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Build/operate microVM or gVisor sandbox fleet; security patching of isolation layer | K8s Agent Sandbox (CNCF) or Kata Containers on managed K8s | E2B Cloud; Bedrock code interpreter |
| | Firecracker, Kata Containers, gVisor, K8s Agent Sandbox | K8s Agent Sandbox + managed node groups | Fully managed sandbox service |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0 |
| **Cost/Usage Metering** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Deploy full Langfuse or LangSmith self-hosted stack (PostgreSQL + ClickHouse + Redis + blob storage) | Same app stack; managed cloud databases | LangSmith Cloud; Bedrock CloudWatch dashboards |
| | Langfuse (Apache 2.0), LangSmith Enterprise, VictoriaMetrics | Langfuse on K8s + managed backing stores | Fully managed; OTEL-compatible integrations |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **Security Sandboxing** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Implement isolation runtime, syscall policies, network egress rules, secret scanning | K8s RuntimeClass with gVisor/Kata; managed security groups | Managed guardrails; policy enforcement without infrastructure |
| | gVisor, Kata Containers, Firecracker, OPA, Falco | K8s RuntimeClass + managed network policies | Amazon Bedrock Guardrails; Azure content safety |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **GPU Scheduling** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Deploy NVIDIA GPU Operator + KAI Scheduler; manage MIG partitioning; capacity planning | NVIDIA GPU Operator on managed K8s node pools | Serverless inference; no GPU management |
| | NVIDIA KAI Scheduler (Apache 2.0), NVIDIA GPU Operator, HAMi | GPU Operator + managed node pools | Bedrock/Foundry serverless model invocation |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |

**FTE Assumptions**: Mid-size deployment serving 50 enterprise customers with 10–50 concurrent agent sessions. Excludes LLM inference operations (see F36) and general compute infrastructure (see F39). On-call burden estimated at additional 0.25–0.5 FTE equivalent across all layers.

**Total Estimated On-Premises Platform Engineering FTE**: 2.75–4.75 FTE for the agent infrastructure layer alone (excluding inference and compute infrastructure covered in F36 and F39).

---

## 9. Managed Platform Reference: What Infrastructure Disappears

### 9.1 Amazon Bedrock AgentCore

[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/), generally available since October 2025, provides as fully managed services: serverless agent deployment (no capacity provisioning), session management with complete session isolation for workloads from [low-latency conversations to 8-hour asynchronous jobs](https://aws.amazon.com/bedrock/agentcore/), persistent memory management without infrastructure ownership, Gateway services converting APIs and Lambda functions into agent-compatible tools automatically, real-time policy enforcement, and identity/access with automated authentication and permission delegation.

[Observability is provided through Amazon CloudWatch dashboards](https://aws.amazon.com/bedrock/agentcore/) with OTEL compatibility for third-party providers (Datadog, Dynatrace, LangSmith, Langfuse). VPC and AWS PrivateLink support address data residency requirements without requiring on-premises deployment.

[Self-hosting becomes cost-competitive with AgentCore once traffic passes several hundred thousand turns per month](https://scalevise.com/resources/agentcore-bedrock-pricing-self-hosting/), with payback estimated at 3–6 months for high-traffic deployments. AgentCore charges across six layers: orchestration steps, model inference tokens, retrieval/embeddings, storage, observability logs, and VPC/networking.

### 9.2 Microsoft Foundry Agent Service (formerly Azure AI Agent Service)

[Microsoft Foundry Agent Service at Ignite 2025](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-agent-service-at-ignite-2025-simple-to-build-powerful-to-deploy-trusted-/4469788) provides hosted agents that are "designed to simplify runtime management while preserving developer choice." Foundry handles: autoscaling, monitoring, identity integration, security, Container Registry setup, Application Insights, managed identity, and RBAC — all without requiring customer-operated Kubernetes.

[Hosted agents eliminate containerization or infrastructure setup](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents?view=foundry), supporting custom-code agents built with LangGraph, CrewAI, Microsoft Agent Framework, or other open-source frameworks directly into a fully managed runtime. Built on open standards: MCP, Agent2Agent (A2A), and OpenAPI.

### 9.3 LangSmith Cloud vs. Self-Hosted

[LangSmith self-hosted](https://docs.langchain.com/langsmith/self-hosted) is an Enterprise plan add-on requiring a license key and sales engagement. The full platform deployment requires Kubernetes and operates four backing services: PostgreSQL, ClickHouse, Redis, and blob storage. LangSmith Cloud eliminates all of these, providing observability, evaluation, and agent deployment as a SaaS. The self-hosted path is justified only when data sovereignty requirements prohibit cloud egress of trace data — a common requirement in regulated industries.

---

## Key Takeaways

- **On-premises agent infrastructure requires operating seven distinct platform layers** — tool registry, sandboxed execution, state management, workflow orchestration, metering, security sandboxing, and GPU scheduling — each of which is a fully managed primitive in cloud-native agent platforms like Amazon Bedrock AgentCore and Microsoft Foundry Agent Service.

- **Total engineering burden is 2.75–4.75 FTE** for the agent infrastructure layer alone in a mid-size production deployment (50 enterprise customers, 10–50 concurrent sessions), excluding LLM inference and compute infrastructure covered in F36 and F39. The [Vectara architecture guide](https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration) states explicitly: "If none of those [staffing prerequisites] are in place, your first architecture decision is staffing."

- **The Kubernetes SIG Agent Sandbox (CNCF, KubeCon NA 2025) and NVIDIA KAI Scheduler (Apache 2.0, January 2025) are the leading open-source answers** to the two hardest on-premises agent infrastructure problems — secure code execution isolation and GPU scheduling — but both require dedicated platform engineering expertise to deploy and operate.

- **Cloud-native managed platforms break even at moderate traffic** — [Amazon Bedrock AgentCore's self-hosting payback is 3–6 months once traffic exceeds several hundred thousand agent turns per month](https://scalevise.com/resources/agentcore-bedrock-pricing-self-hosting/) — meaning on-premises deployment is only cost-superior at scale for customers with strict data sovereignty requirements that cloud VPC/PrivateLink options cannot satisfy.

- **Durable workflow orchestration (Temporal) and production observability (Langfuse) are the two self-hosted components with the highest infrastructure dependencies**: Temporal requires PostgreSQL or Cassandra plus self-managed worker clusters; Langfuse requires PostgreSQL, ClickHouse, Redis, and blob storage. ISVs considering partial on-premises deployments should evaluate whether just these two layers can be offloaded to managed services before committing to a full on-premises stack.

---

## Related — Out of Scope

- **F7: Agent Framework Design** — Architectural patterns for LangGraph, AutoGen, CrewAI (selection, supervisor patterns, tool definitions). This file covers the infrastructure layer only.
- **F36: LLM Inference Operations** — GPU memory sizing, inference server configuration (vLLM, TGI), model serving SLAs. This file assumes inference is handled externally.
- **F39: General Compute Infrastructure** — Bare-metal provisioning, Kubernetes cluster lifecycle, network fabric. This file covers agent-specific workloads only.
- **F51: Agent Observability and Tracing** — Detailed tracing pipeline architecture, sampling strategies, and backend selection for agent reasoning chains. Referenced in Section 6.2.

---

## Sources

- [Amazon Bedrock AgentCore — AWS](https://aws.amazon.com/bedrock/agentcore/)
- [AgentCore (Bedrock) Pricing and When Self-Hosting Wins — ScaleVise](https://scalevise.com/resources/agentcore-bedrock-pricing-self-hosting/)
- [Foundry Agent Service at Ignite 2025 — Microsoft Tech Community](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-agent-service-at-ignite-2025-simple-to-build-powerful-to-deploy-trusted-/4469788)
- [Hosted Agents in Foundry Agent Service — Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents?view=foundry)
- [Self-hosted LangSmith — Docs by LangChain](https://docs.langchain.com/langsmith/self-hosted)
- [LangGraph Redis Checkpoint 0.1.0 — Redis](https://redis.io/blog/langgraph-redis-checkpoint-010/)
- [LangGraph & Redis: Build Smarter AI Agents — Redis](https://redis.io/blog/langgraph-redis-build-smarter-ai-agents-with-memory-persistence/)
- [AI Agent Orchestration for Production Systems — Redis](https://redis.io/blog/ai-agent-orchestration/)
- [LangGraph Persistence — Docs by LangChain](https://docs.langchain.com/oss/javascript/langgraph/persistence)
- [Self-host Langfuse (Open Source LLM Observability) — Langfuse](https://langfuse.com/self-hosting)
- [AI Agent Observability: Evolving Standards and Best Practices — OpenTelemetry](https://opentelemetry.io/blog/2025/ai-agent-observability/)
- [Semantic Conventions for Generative AI Metrics — OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/)
- [AI Agents Observability with OpenTelemetry and VictoriaMetrics](https://victoriametrics.com/blog/ai-agents-observability/)
- [One Year of MCP: November 2025 Spec Release — MCP Blog](http://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/)
- [Introducing the MCP Registry — MCP Blog](http://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)
- [MCP Registry — Model Context Protocol](https://modelcontextprotocol.info/tools/registry/)
- [MCP Registry — GitHub](https://github.com/modelcontextprotocol/registry)
- [Agent Sandbox — Kubernetes SIGs](https://github.com/kubernetes-sigs/agent-sandbox)
- [Agent Sandbox Documentation](https://agent-sandbox.sigs.k8s.io/)
- [Open-Source Agent Sandbox Enables Secure Deployment on Kubernetes — InfoQ](https://www.infoq.com/news/2025/12/agent-sandbox-kubernetes/)
- [Google Launches Agent Sandbox for Secure AI Agents on Kubernetes — TechInformed](https://techinformed.com/google-launches-agent-sandbox-for-secure-ai-agents-on-kubernetes/)
- [How to Sandbox AI Agents: Firecracker, gVisor & Isolation Strategies — Northflank](https://northflank.com/blog/how-to-sandbox-ai-agents)
- [Top Self-Hostable Alternatives to E2B for AI Agents — Northflank](https://northflank.com/blog/self-hostable-alternatives-to-e2b-for-ai-agents)
- [What's the Best Code Execution Sandbox for AI Agents — Northflank](https://northflank.com/blog/best-code-execution-sandbox-for-ai-agents)
- [How to Sandbox LLMs & AI Shell Tools: Docker, gVisor, Firecracker — CodeAnt](https://www.codeant.ai/blogs/agentic-rag-shell-sandboxing)
- [How to Architect Robust On-Premise AI Agent Orchestration — Vectara](https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration)
- [Agentic AI Workflows: Why Orchestration with Temporal Is Key — IntuitionLabs](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration)
- [Temporal — Pydantic AI](https://ai.pydantic.dev/durable_execution/temporal/)
- [Modern Queueing Architectures: Celery, RabbitMQ, Redis, or Temporal?](https://medium.com/@pranavprakash4777/modern-queueing-architectures-celery-rabbitmq-redis-or-temporal-f93ea7c526ec)
- [NVIDIA KAI Scheduler — GitHub](https://github.com/NVIDIA/KAI-Scheduler)
- [NVIDIA Open Sources Run:ai Scheduler — NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/)
- [Enable Gang Scheduling with NVIDIA KAI Scheduler — NVIDIA Technical Blog](https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler/)
- [Streamline Complex AI Inference with NVIDIA Grove — NVIDIA Technical Blog](https://developer.nvidia.com/blog/streamline-complex-ai-inference-on-kubernetes-with-nvidia-grove/)
- [Kubernetes GPU Scheduling in 2025: Practical Patterns — Debugg.ai](https://debugg.ai/resources/kubernetes-gpu-scheduling-2025-kueue-volcano-mig)
- [Scaling AI-Powered Agents: Building a Distributed LangGraph Workflow Engine](https://medium.com/@mukshobhit/scaling-ai-powered-agents-building-a-distributed-langgraph-workflow-engine-13e57e368953)
- [AI Observer — GitHub](https://github.com/tobilg/ai-observer)
- [Gartner Predicts 2026: AI Agents Will Reshape Infrastructure & Operations — Itential](https://www.itential.com/resource/analyst-report/gartner-predicts-2026-ai-agents-will-reshape-infrastructure-operations/)
- [Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026 — Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)
- [Building a Multi-Agent Orchestration Platform for Wealth Management AI — Medium](https://medium.com/@brianyang/building-a-multi-agent-orchestration-platform-for-wealth-management-ai-what-i-learned-80673357e64c)
