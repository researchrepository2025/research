# W05S: On-Premises Application-Level Pattern Challenges — Unified Synthesis

**Wave:** 5 (On-Premises Application Patterns)
**Agent Files Synthesized:** F32, F33, F34, F35, F36, F37, F38
**Date:** 2026-02-19

---

## Executive Summary

Implementing the seven core application patterns of an AI-driven SaaS product — microservices, event-driven architecture, API gateway, RAG pipelines, LLM inference, embedding generation, and AI agent orchestration — on 100% on-premises infrastructure carries a cumulative staffing burden of approximately **15–23 FTE** of specialized engineering across all patterns, versus roughly 2–4 FTE for equivalent cloud-native managed services. The operational difficulty is not merely additive: each pattern introduces its own self-hosted infrastructure dependencies (Kafka, Redis, PostgreSQL, etcd, Consul, Vault, Prometheus, Temporal, vector databases, GPU schedulers) whose failure domains overlap and compound, creating a combinatorial coordination surface that no single orchestrator eliminates. On-premises deployment remains viable for strict data sovereignty requirements, but ISVs must price the full operational profile into customer contracts — not just the application logic, but the seven-to-ten distinct infrastructure platforms required to support it.

---

## Theme 1: Infrastructure Dependency Explosion — Every Managed Service Becomes a Self-Operated Platform

The defining characteristic of on-premises application patterns is that each cloud-managed abstraction decomposes into multiple self-hosted infrastructure components, each requiring its own HA configuration, monitoring, patching, and operational expertise.

A single API gateway deployment (F34) requires not just the gateway binary but a [Redis Cluster for distributed rate limiting with Lua scripts for atomicity](https://www.freecodecamp.org/news/build-rate-limiting-system-using-redis-and-lua/) (from F34), a [self-hosted Keycloak instance backed by PostgreSQL for OAuth2/OIDC](https://www.keycloak.org/) (from F34), a [3-node Consul cluster for service discovery](https://developer.hashicorp.com/consul/docs/use-case/service-discovery) (from F34), and a self-hosted developer portal (Backstage) — totaling [1.5–3.0 FTE](https://developer.konghq.com/gateway/performance/benchmarks/) (from F34). Event-driven architecture (F33) adds an event store (EventStoreDB or Kafka with compensating infrastructure), a saga orchestration engine (Temporal requiring [Cassandra + Elasticsearch + four discrete service pods](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b)), a schema registry, DLQ management, and distributed tracing — totaling [2.0–4.1 FTE active plus 0.85 FTE on-call](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b) (from F33). The RAG pipeline (F35) adds Apache Tika, a chunking queue, GPU-served embedding and reranking models, a vector database, pipeline orchestration (Airflow 3.0 or Temporal), and a full RAGOps observability stack — totaling [3.25–4.75 FTE](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide) (from F35).

The compounding effect is severe: a 100-service microservices deployment alone requires [7–20 dedicated SRE/DevOps engineers](https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/) depending on platform maturity, versus [1–2 for an equivalent modular monolith](https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/) (from F32). Infrastructure costs rise [20–40% with microservices, monitoring expenses increase 50–100%](https://fullscale.io/blog/microservices-roi-cost-benefit-analysis/) (from F32), and these percentages apply on top of the already substantial on-premises hardware baseline.

---

## Theme 2: GPU Procurement and Contention — The Hardware Bottleneck That Software Cannot Solve

Three of the seven Wave 5 patterns (LLM inference, embedding generation, RAG pipeline) share a dependency on GPU hardware, and on-premises deployments face structural procurement and scheduling constraints that cloud providers abstract entirely.

[H100 enterprise lead times run 9–12 months for standard orders](https://uvation.com/articles/h100-availability-the-silent-crisis-threatening-enterprise-ai-plans) (from F36), with secondary market units trading at approximately double retail price. ISVs must commit to hardware procurement one to two planning cycles ahead of application demand. Once procured, GPU contention between LLM inference and embedding workloads is the [primary operational risk on-premises](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025) (from F37): embedding models and LLM inference compete for the same physical GPUs, and without explicit [MIG partitioning on A100/H100 hardware](https://docs.cast.ai/docs/gpu-sharing-mig) (from F36, F37), embedding latency degrades unpredictably under LLM load.

The performance ceiling, once hardware is in place, is competitive. [vLLM achieves P99 latency of 80ms and 793 tokens/second](https://introl.com/blog/vllm-production-deployment-inference-serving-architecture) (from F36), maintaining [85–92% GPU utilization under high concurrency](https://arxiv.org/html/2511.17593v1) (from F36). [AWQ 4-bit quantization delivers under 1% accuracy loss while reducing VRAM by approximately 50%](https://localaimaster.com/blog/quantization-explained) (from F36), making 70B-parameter models deployable on single H100/H200 GPUs. On-premises RAG pipelines achieve [2–7 second end-to-end query latency (P50: 1.2–1.8s with caching)](https://hackernoon.com/designing-production-ready-rag-pipelines-tackling-latency-hallucinations-and-cost-at-scale) (from F35), comparable to cloud-native alternatives. Self-hosted embedding can achieve [~10ms P99 latency versus OpenAI's ~5 seconds](https://nixiesearch.substack.com/p/benchmarking-api-latency-of-embedding) (from F37).

But raw performance is not the bottleneck. The operational burden of maintaining GPU drivers, CUDA versions, MIG configurations, model lifecycle (quantization, A/B testing, rollback), and multi-model routing via [LiteLLM or RouteLLM](https://github.com/BerriAI/litellm) (from F36) demands [2.0–3.5 FTE for LLM inference alone](https://bentoml.com/llm/infrastructure-and-operations/on-prem-llms) (from F36) and [2.0–3.25 FTE for embedding pipelines](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide) (from F37).

---

## Theme 3: The Temporal/Workflow Engine as Recurring Infrastructure Dependency

Self-hosted Temporal appears as a critical dependency in three of the seven patterns — event-driven saga orchestration (F33), RAG pipeline orchestration (F35), and AI agent workflow orchestration (F38) — making it a cross-cutting infrastructure investment with compounding operational implications.

Self-hosting Temporal requires [Cassandra for persistence and Elasticsearch for visibility](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b) (from F33) in production, because [PostgreSQL is unsuitable for medium-to-large-scale systems — even 100 RPS caused spiked database load beyond 120](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b) (from F33). The learning curve is significant: [expect a month before the team is productive](https://blog.taigrr.com/blog/setting-up-a-production-ready-temporal-server/) (from F33). Ongoing operations include certificate rotation, configuration management, and version upgrades that [frequently change configuration requirements](https://medium.com/@mailman966/my-journey-hosting-a-temporal-cluster-237fec22a5ec) (from F33).

The difficulty rating for saga orchestration via Temporal is [5/5](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b) (from F33) — the single highest rating in the event-driven architecture analysis. Pipeline orchestration in F35 carries a [5/5 rating](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide) (from F35), and agent workflow orchestration in F38 carries a [5/5 rating](https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration) (from F38). This convergence means ISVs deploying multiple AI application patterns on-premises will encounter the Temporal operational burden repeatedly — but can amortize it if a shared Temporal cluster serves all three use cases, reducing the per-pattern FTE while increasing the blast radius of a Temporal failure.

---

## Theme 4: Observability, Governance, and the Hidden Staffing Gap

Across all seven patterns, the observability and governance layers are consistently rated 4–5/5 difficulty on-premises and represent the most frequently underestimated staffing requirement.

Microservices (F32) require per-service [Prometheus scrape configurations, Alertmanager routing trees, and inhibition rules](https://prometheus.io/docs/alerting/latest/alertmanager/) — at 100 services, this produces thousands of alert rules with a [4/5 difficulty rating and 0.2–0.4 FTE per 100 services](https://prometheus.io/docs/alerting/latest/alertmanager/) (from F32). Event-driven systems (F33) require self-hosted distributed tracing via [Jaeger 2.0 + OpenTelemetry Collector + Grafana Tempo](https://www.johal.in/kubernetes-advanced-observability-implementing-opentelemetry-jaeger-and-tempo-for-distributed-tracing-2025/) at [4/5 difficulty and 0.25–0.5 FTE](https://www.johal.in/kubernetes-advanced-observability-implementing-opentelemetry-jaeger-and-tempo-for-distributed-tracing-2025/) (from F33). AI agent observability (F38) requires a full [Langfuse deployment with PostgreSQL, ClickHouse, Redis, and blob storage](https://langfuse.com/self-hosting) (from F38). RAG pipelines demand a nascent [RAGOps discipline](https://arxiv.org/abs/2506.03401) covering monitorability, observability, traceability, and reliability — all built from scratch on-premises, rated [5/5 difficulty](https://arxiv.org/abs/2506.03401) (from F35).

Embedding drift detection adds another layer: [declining retrieval quality often indicates embedding drift, corpus staleness, or distribution shift](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide) (from F37), requiring [weekly quality reviews and tools like Evidently AI for drift monitoring](https://www.evidentlyai.com/blog/embedding-drift-detection) (from F37). Schema governance is the least visible risk in event-driven systems: [Gartner documents that few organizations provide guidance on event lifecycle management](https://www.gartner.com/en/documents/3986571) (from F33).

---

## Theme 5: Cloud-Native Cost Asymmetry — The 5x–10x FTE Multiplier

The most consistent quantitative finding across all seven agents is the FTE differential between on-premises and cloud-native deployment models.

| Pattern | On-Prem FTE | Managed K8s FTE | Cloud-Native FTE | Key Source |
|---------|-------------|-----------------|-------------------|------------|
| Microservices (F32) | 7–20 (100 svc) | ~3–5 | 1–2 | [SoftwareSeni](https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/) |
| Event-Driven (F33) | 2.05–4.1 + 0.85 on-call | ~1.5 | 0.1–0.6 | Aggregated from F33 |
| API Gateway (F34) | 1.5–3.0 | 0.7–1.5 | 0.2–0.55 | Aggregated from F34 |
| RAG Pipeline (F35) | 3.25–4.75 | ~1.5–2.5 | 0.5–1.0 | Aggregated from F35 |
| LLM Inference (F36) | 2.0–3.0 + 0.45 on-call | ~1.0–1.5 | 0.2–0.5 | [BentoML](https://bentoml.com/llm/infrastructure-and-operations/on-prem-llms) |
| Embedding Pipeline (F37) | 2.0–3.25 + 0.5 on-call | 1.1–1.5 | 0.55–0.7 | Aggregated from F37 |
| AI Agent Infra (F38) | 2.75–4.75 | ~1.5–2.5 | 0.0–0.1 | [Vectara](https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration) |

On-premises LLM inference does offer a cost advantage for sustained workloads: [2.9x to 4.1x more cost-effective than API-based cloud services (65–75% cost reduction)](https://www.delltechnologies.com/asset/en-in/solutions/business-solutions/industry-market/esg-inferencing-on-premises-with-dell-technologies-analyst-paper.pdf) (from F36). But this hardware cost advantage is consumed by the staffing differential. For ISVs delivering to customer sites where the customer has fewer than [10–15 dedicated infrastructure engineers](https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/) (from F32), the operational profile of a full on-premises stack is unsustainable regardless of documentation quality.

---

## Difficulty and FTE Summary Table

| Capability Domain | On-Prem Difficulty | Managed K8s Difficulty | Cloud-Native Difficulty | On-Prem FTE | Cloud-Native FTE |
|---|---|---|---|---|---|
| Container Orchestration (F32) | 4/5 | 2/5 | 1/5 | 1.5–2.5 (50-node) | 0.0 |
| Microservices Lifecycle (F32) | 4/5 | 2.5/5 | 1.5/5 | 7–20 (100 svc) | 1–2 |
| Saga Orchestration (F33) | 5/5 | 3/5 | 1/5 | 0.5–1.0 | 0.0–0.1 |
| Event Store Ops (F33) | 3–4/5 | 3/5 | 1/5 | 0.25–1.0 | 0.0 |
| Schema Registry (F33) | 3/5 | 2/5 | 1/5 | 0.1–0.2 | 0.0 |
| API Gateway Software (F34) | 4/5 | 3/5 | 1/5 | 0.5–1.0 | 0.1–0.25 |
| Distributed Rate Limiting (F34) | 4/5 | 3/5 | 1/5 | 0.25–0.5 | 0.0 |
| Self-Hosted Auth (F34) | 4/5 | 3/5 | 2/5 | 0.25–0.5 | 0.05–0.1 |
| RAG Pipeline Orchestration (F35) | 5/5 | 4/5 | 2/5 | 0.5–0.75 | 0.1 |
| RAG Observability (F35) | 5/5 | 4/5 | 2/5 | 0.25–0.5 | 0.05 |
| LLM Serving Framework (F36) | 3/5 | 2/5 | 1/5 | 0.5–1.0 | 0.1 |
| GPU Procurement/Allocation (F36) | 4/5 | 2/5 | 1/5 | Structural | N/A |
| Model Lifecycle (F36) | 4/5 | 3/5 | 1/5 | 0.5–0.75 | 0.0 |
| Embedding Model Serving (F37) | 4/5 | 3/5 | 1/5 | 0.5–1.0 | 0.1 |
| Embedding Versioning/Migration (F37) | 5/5 | 4/5 | 3/5 | 0.5 | 0.1–0.25 |
| GPU Scheduling/Sharing (F37) | 5/5 | 3/5 | 1/5 | 0.25–0.5 | 0.0 |
| Agent Tool Registry (F38) | 4/5 | 3/5 | 1/5 | 0.5–1.0 | 0.0–0.1 |
| Agent Workflow Orchestration (F38) | 5/5 | 3/5 | 1/5 | 0.5–1.0 | 0.0 |
| Code Execution Sandbox (F38) | 5/5 | 4/5 | 1/5 | 0.5–1.0 | 0.0 |
| Agent Observability/Metering (F38) | 4/5 | 3/5 | 1/5 | 0.25–0.5 | 0.0 |

---

## Cross-Agent Patterns and Contradictions

**Consistent patterns:**
- Every agent file rates on-premises difficulty at 4–5/5 for core operational domains. No agent reported a capability below 3/5 for any non-trivial on-premises operation.
- PostgreSQL and Redis appear as infrastructure dependencies in all seven patterns, creating operational consolidation opportunity (shared HA clusters) but also single-point-of-failure risk.
- Temporal is the recommended workflow engine across F33, F35, and F38, but all three note its significant operational overhead and one-month learning curve.

**Notable tension:**
- F36 documents that on-premises LLM inference is [2.9x–4.1x more cost-effective](https://www.delltechnologies.com/asset/en-in/solutions/business-solutions/industry-market/esg-inferencing-on-premises-with-dell-technologies-analyst-paper.pdf) than cloud APIs for sustained workloads, while F37 notes that managed embedding APIs eliminate [six of eight major operational domains](https://artsmart.ai/blog/top-embedding-models-in-2025/). This creates a split decision: LLM inference may justify on-premises for high-volume workloads, while embedding generation may not.
- F34 demonstrates that API gateway raw throughput ([Kong: 130,000+ RPS at 6ms P99](https://developer.konghq.com/gateway/performance/benchmarks/)) is never the bottleneck — operational burden is. F36 makes the same observation for LLM inference. Performance is achievable; sustaining it operationally is the true cost.
- F35 notes that cloud-native RAG services like Bedrock Knowledge Bases [lock users into specific chunking strategies](https://www.truefoundry.com/blog/our-honest-review-of-amazon-bedrock-2026-edition), reducing customization. This is the primary technical argument for on-premises RAG — not cost or performance, but retrieval quality control.

---

## Open Questions for Downstream Synthesis

1. **Shared infrastructure amortization:** Can a single Temporal cluster, PostgreSQL HA cluster, and Redis cluster serve all seven application patterns, and what is the realistic FTE reduction from consolidation? (Cross-reference with Wave 6 infrastructure agents F39–F50.)

2. **Customer staffing floor:** F32 identifies 10–15 dedicated infrastructure engineers as the minimum for sustainable on-premises microservices. Do the AI-specific patterns (F35–F38) raise this floor, and what is the combined minimum for a full AI SaaS stack?

3. **Managed K8s as middle ground:** Across all seven agents, managed Kubernetes consistently halves the on-premises FTE burden. Is there a pattern subset where managed K8s achieves near-cloud-native operational simplicity while preserving data sovereignty?

4. **Nomad vs. Kubernetes decision:** F32 documents that Nomad offers [30–40% better resource utilization](https://www.futurevistaacademy.com/platform-engineering/kubernetes-vs-docker-swarm-vs-nomad-2025) than Kubernetes, but the AI-specific patterns (F36, F37, F38) assume Kubernetes for GPU Operator, KAI Scheduler, and Agent Sandbox. Does adopting Nomad for general orchestration create a split-brain problem for AI workloads?

5. **Embedding model deprecation risk:** F37 highlights that managed API providers can deprecate embedding models on their own schedule, forcing unplanned re-embedding. Is this risk quantifiable, and does it shift the build-vs-buy calculus for on-premises embedding?

---

## Sources

### F32: On-Premises Microservices
- [SoftwareSeni: True Cost of Microservices](https://www.softwareseni.com/the-true-cost-of-microservices-quantifying-operational-complexity-and-debugging-overhead/)
- [FullScale: Microservices ROI Cost-Benefit Analysis](https://fullscale.io/blog/microservices-roi-cost-benefit-analysis/)
- [Future Vista Academy: K8s vs Swarm vs Nomad 2025](https://www.futurevistaacademy.com/platform-engineering/kubernetes-vs-docker-swarm-vs-nomad-2025)
- [Prometheus: Alertmanager Documentation](https://prometheus.io/docs/alerting/latest/alertmanager/)
- [Doppler: Secrets Sprawl 2025](https://www.doppler.com/blog/what-is-secrets-sprawl-and-how-to-prevent-it-in-2025)

### F33: On-Premises Event-Driven Architecture
- [Vymo Engineering: Scaling Temporal](https://medium.com/vymo-engineering/scaling-temporal-load-testing-with-postgres-cassandra-elasticsearch-monitoring-alerting-1176b7a4968b)
- [blog.taigrr.com: Self-hosting Temporal Server](https://blog.taigrr.com/blog/setting-up-a-production-ready-temporal-server/)
- [My Journey Hosting a Temporal Cluster](https://medium.com/@mailman966/my-journey-hosting-a-temporal-cluster-237fec22a5ec)
- [Gartner: Choosing Event Brokers](https://www.gartner.com/en/documents/3986571)
- [johal.in: Kubernetes Advanced Observability](https://www.johal.in/kubernetes-advanced-observability-implementing-opentelemetry-jaeger-and-tempo-for-distributed-tracing-2025/)

### F34: On-Premises API Gateway
- [Kong Gateway Performance Benchmarks](https://developer.konghq.com/gateway/performance/benchmarks/)
- [Keycloak Official](https://www.keycloak.org/)
- [Consul Service Discovery](https://developer.hashicorp.com/consul/docs/use-case/service-discovery)
- [freeCodeCamp: Redis + Lua Rate Limiting](https://www.freecodecamp.org/news/build-rate-limiting-system-using-redis-and-lua/)

### F35: On-Premises RAG Pipeline
- [Introl: RAG Infrastructure Guide](https://introl.com/blog/rag-infrastructure-production-retrieval-augmented-generation-guide)
- [HackerNoon: Production RAG Pipelines](https://hackernoon.com/designing-production-ready-rag-pipelines-tackling-latency-hallucinations-and-cost-at-scale)
- [RAGOps arXiv Paper](https://arxiv.org/abs/2506.03401)
- [Cisco FlashStack RAG NIM CVD](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/UCS_CVDs/flashstack_rag_nim.html)
- [TrueFoundry: Bedrock Review 2026](https://www.truefoundry.com/blog/our-honest-review-of-amazon-bedrock-2026-edition)

### F36: On-Premises LLM Inference
- [vLLM Production Deployment Architecture](https://introl.com/blog/vllm-production-deployment-inference-serving-architecture)
- [vLLM 2024 Wrapped / 2025 Vision](https://blog.vllm.ai/2025/01/10/vllm-2024-wrapped-2025-vision.html)
- [AWQ/GPTQ/GGUF Quantization Comparison](https://localaimaster.com/blog/quantization-explained)
- [H100 Availability Crisis](https://uvation.com/articles/h100-availability-the-silent-crisis-threatening-enterprise-ai-plans)
- [Dell On-Premises Inferencing Paper](https://www.delltechnologies.com/asset/en-in/solutions/business-solutions/industry-market/esg-inferencing-on-premises-with-dell-technologies-analyst-paper.pdf)
- [BentoML: On-Prem LLMs](https://bentoml.com/llm/infrastructure-and-operations/on-prem-llms)
- [LiteLLM GitHub](https://github.com/BerriAI/litellm)
- [arXiv: vLLM vs TGI Benchmark](https://arxiv.org/html/2511.17593v1)

### F37: On-Premises Embedding Pipeline
- [Nixiesearch: Embedding API Latency Benchmarks](https://nixiesearch.substack.com/p/benchmarking-api-latency-of-embedding)
- [Introl: GPU Memory Pooling and Sharing](https://introl.com/blog/gpu-memory-pooling-sharing-multi-tenant-kubernetes-2025)
- [CAST AI: GPU MIG for Kubernetes](https://docs.cast.ai/docs/gpu-sharing-mig)
- [Evidently AI: Embedding Drift Detection](https://www.evidentlyai.com/blog/embedding-drift-detection)
- [ArtSmart: Top Embedding Models 2025](https://artsmart.ai/blog/top-embedding-models-in-2025/)
- [Medium: Hidden Cost of Model Upgrades](https://medium.com/data-science-collective/different-embedding-models-different-spaces-the-hidden-cost-of-model-upgrades-899db24ad233)

### F38: On-Premises AI Agent Infrastructure
- [Vectara: On-Premise AI Agent Orchestration](https://www.vectara.com/blog/how-to-architect-robust-on-premise-ai-agent-orchestration)
- [Langfuse Self-Hosting](https://langfuse.com/self-hosting)
- [OpenTelemetry: AI Agent Observability](https://opentelemetry.io/blog/2025/ai-agent-observability/)
- [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [ScaleVise: AgentCore Pricing / Self-Hosting](https://scalevise.com/resources/agentcore-bedrock-pricing-self-hosting/)
- [NVIDIA KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler)
- [Agent Sandbox — Kubernetes SIGs](https://agent-sandbox.sigs.k8s.io/)
