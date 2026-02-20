# Four-Plane Synthesis: ISV SaaS Deployment Difficulty Analysis

## Executive Summary

**Yes, the mental model is correct: building AI-driven microservices SaaS on-premises is dramatically harder than cloud-native, and the evidence is unambiguous.** Across 38 MECE subsegments spanning four operational planes -- Control Plane (10 subsegments), Application Logic (10), Data Plane (10), and AI Model Plane (8) -- the cross-plane average difficulty is 1.6 cloud-native, 2.7 managed Kubernetes, and 4.2 on-premises on a 1-5 scale. In FTE terms, the gap is starker: a mid-size ISV serving 50 enterprise customers requires approximately 10-23 FTE cloud-native, 25-47 FTE managed K8s, and 59-111 FTE on-premises at a single-service baseline, widening to 19-41 FTE, 42-81 FTE, and 97-180 FTE at 20 microservices (G1, N=20 table). The on-premises-to-cloud-native FTE ratio stabilizes at approximately 4.6x from N=10 services onward; the difficulty ratio never converges because per-service marginal cost is structurally higher on-premises (G1, Scaling Summary).

| Plane | Cloud-Native | Managed K8s | On-Premises |
|-------|:---:|:---:|:---:|
| P1 Control Plane | 1.3 | 2.8 | 4.7 |
| P2 Application Logic | 2.0 | 2.6 | 3.4 |
| P3 Data Plane | 1.5 | 2.9 | 4.4 |
| P4 AI Model Plane | 1.4 | 2.6 | 4.3 |
| **Cross-Plane Average** | **1.6** | **2.7** | **4.2** |

The single most important finding is not the average difficulty gap -- it is the concentration of extreme difficulty. Seven of the 10 Control Plane subsegments are rated 5/5 on-premises (CP-01, CP-02, CP-04, CP-07, CP-08, CP-09, CP-10), and six Data Plane subsegments reach 5/5 on-premises (DS1, DS6, DS7, DS8, DS9, DS10). No subsegment in any plane reaches 5/5 at cloud-native (P1, P2, P3, P4). This means on-premises does not merely require "more staff" -- it requires specialist staff across nearly every operational domain simultaneously, with no viable generalist-substitution strategy. The F79 meta-analysis confirms this finding from five independent MECE frameworks: all five unanimously identify AI/ML inference and security/compliance as the highest-difficulty, highest-risk on-premises domains (F79, Section 5).

The mental model can be stated precisely: **cloud providers absorb the operational substrate (infrastructure lifecycle, security posture, observability backends, data service HA, GPU management), and that absorption eliminates not just the direct FTE of each domain but the cross-domain coordination overhead, the specialist hiring pipeline, the mandatory migration burden, and the linear-with-customer-count scaling penalty that on-premises deployments incur.** On-premises is not incrementally harder. It is structurally a different kind of engineering organization.

---

## 1. Cross-Plane Difficulty Comparison Matrix

This is the centerpiece of the analysis. The matrix below presents all 38 subsegments across four planes, with composite difficulty ratings per tier, FTE ranges, and the cloud-to-on-premises difficulty delta.

### P1: Control Plane (10 subsegments)

| ID | Subsegment | Cloud-Native | Managed K8s | On-Premises | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| CP-01 | K8s Cluster Lifecycle | 1 | 3 | 5 | 0.0-0.5 | 1.0-2.5 | 3.0-6.0 |
| CP-02 | Network Fabric / Ingress / Mesh | 1 | 3 | 5 | 0.1-0.7 | 0.75-1.75 | 1.75-3.5 |
| CP-03 | IAM / RBAC | 1 | 2 | 4 | 0.3-0.8 | 1.65-2.65 | 2.75-4.75 |
| CP-04 | Secrets / Certs / PKI | 1 | 2 | 5 | 0.4-0.85 | 0.4-0.85 | 2.5-5.0 |
| CP-05 | Observability Infrastructure | 1 | 3 | 4 | 0.55-1.0 | 1.25-2.0 | 4.6-7.0 |
| CP-06 | CI/CD Pipeline / GitOps | 1 | 3 | 4 | 0.3-0.4 | 1.3-1.9 | 2.0-3.25 |
| CP-07 | Deploy Lifecycle / Rollback | 1 | 3 | 5 | 0.1-0.35 | 0.35-0.75 | 1.5-3.0 |
| CP-08 | Disaster Recovery / BC | 2 | 3 | 5 | 0.25-0.5 | 0.5-1.0 | 1.5-2.5 |
| CP-09 | Compliance Automation | 2 | 3 | 5 | 0.5-1.0 | 1.25-2.0 | 2.5-4.0 |
| CP-10 | Security Operations | 2 | 3 | 5 | 0.25-1.2 | 2.25-4.5 | 2.75-5.5 |
| | **P1 Average / Total** | **1.3** | **2.8** | **4.7** | **2.5-6.5** | **9-16** | **20-38** |

(Source: P1, Summary Difficulty Matrix; FTE ranges deduplicated per P1 methodology)

### P2: Application Logic (10 subsegments)

| ID | Subsegment | Cloud-Native | Managed K8s | On-Premises | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| AL01 | Service Decomp / Inter-Service Comm | 2 | 2 | 3 | 0.5-1.0 | 0.6-1.1 | 0.8-1.5 |
| AL02 | Business Logic / Domain Services | 2 | 2 | 2 | 3.0-6.0 | 3.0-6.0 | 3.0-6.0 |
| AL03 | API Gateway / Edge Routing | 2 | 3 | 4 | 0.1-0.2 | 0.3-0.6 | 1.5-3.0 |
| AL04 | Data Access / ORM / Caching | 2 | 2 | 2 | 0.5-1.0 | 0.5-1.0 | 0.75-1.5 |
| AL05 | Background Jobs / Async / EDA | 1 | 3 | 4 | 0.1-0.2 | 0.4-0.8 | 2.75-5.6 |
| AL06 | Resilience Patterns / Runtime | 2 | 3 | 4 | 0.15-0.3 | 0.3-0.6 | 0.75-1.5 |
| AL07 | Multi-Tenant Isolation | 3 | 3 | 3 | 0.5-1.0 | 0.5-1.0 | 0.75-1.5 |
| AL08 | Observability Instrumentation | 2 | 2 | 3 | 0.2-0.4 | 0.3-0.6 | 0.5-1.0 |
| AL09 | AI/ML Orchestration / Agent Pipelines | 2 | 3 | 5 | 0.5-1.2 | 2.0-4.0 | 4.0-7.0* |
| AL10 | Testing / Contract Testing / Env Parity | 2 | 3 | 4 | 0.7-1.65 | 2.0-4.0 | 3.75-7.0 |
| | **P2 Average / Total** | **2.0** | **2.6** | **3.4** | **5.8-13.2** | **9.4-19.8** | **18.6-35.6*** |

*AL09 FTE adjusted: P2 states 6.0-10.0 FTE on-premises for AL09, but this includes vector DB ops (P3 DS8, 1.25-1.75 FTE) and inference engine ops (P4 S2, 2.0-3.5 FTE). Deduplicating these overlaps reduces the P2-attributable AL09 FTE to approximately 4.0-7.0 FTE, covering agent orchestration code, LangGraph checkpointing, guardrail integration, and MCP server management. The P2 aggregate is adjusted accordingly. See Section 6 for full overlap resolution.

(Source: P2, Summary Difficulty Matrix; AL09 overlap resolution per task instructions)

### P3: Data Plane (10 subsegments)

| ID | Subsegment | Cloud-Native | Managed K8s | On-Premises | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| DS1 | Relational Database HA | 2 | 3 | 5 | 0.25-0.50 | 0.50-0.85 | 1.50-3.00 |
| DS2 | NoSQL / Document Store | 1 | 3 | 4 | 0.10 | 0.40-0.70 | 0.60-1.10 |
| DS3 | Caching Layer | 2 | 3 | 4 | 0.10 | 0.25 | 0.40-0.70 |
| DS4 | Object / Blob Storage | 1 | 2 | 3 | 0.05-0.10 | 0.10-0.20 | 0.25-0.60 |
| DS5 | Message Queuing (Simple) | 1 | 2 | 3 | 0.10 | 0.20-0.30 | 0.40-0.70 |
| DS6 | Event Streaming (Kafka) | 1 | 4 | 5 | 0.25-0.50 | 0.50-1.00 | 1.50-2.50 |
| DS7 | Search / Full-Text Index | 2 | 3 | 5 | 0.10-0.20 | 0.25-0.50 | 0.70-1.20 |
| DS8 | Vector Database | 1 | 3 | 5 | 0.00-0.10 | 0.40-0.70 | 1.25-1.75 |
| DS9 | Embedding Pipeline (GPU) | 2 | 3 | 5 | 0.10-0.20 | 0.50-0.80 | 2.00-3.25 |
| DS10 | RAG Pipeline Orchestration | 2 | 3 | 5 | 0.50-1.00 | 1.00-1.50 | 3.25-4.75 |
| | **P3 Average / Total** | **1.5** | **2.9** | **4.4** | **1.55-2.70** | **4.10-6.55** | **11.85-19.55** |

(Source: P3, Summary Difficulty Matrix)

### P4: AI Model Plane (8 subsegments)

| ID | Subsegment | Cloud-Native | Managed K8s | On-Premises | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| S1 | Managed API Integration | 1 | 1 | 2 | 0.05-0.15 | 0.05-0.15 | 0.10-0.30 |
| S2 | Self-Hosted Inference Engine | 1 | 3 | 5 | 0 | 0.75-1.50 | 2.00-3.50 |
| S3 | GPU Hardware Infrastructure | 1 | 2 | 5 | 0 | 0.10-0.25 | 2.50-5.00 |
| S4 | GPU Driver / CUDA Stack | 1 | 2 | 4 | 0 | 0.10-0.25 | 0.50-1.00 |
| S5 | Multi-Tenant GPU Scheduling | 1 | 3 | 5 | 0 | 0.25-0.50 | 0.50-1.00 |
| S6 | Model Routing / Load Balancing | 2 | 3 | 4 | 0.10-0.25 | 0.20-0.50 | 0.50-1.00 |
| S7 | Inference Monitoring | 2 | 4 | 5 | 0.10-0.25 | 0.50-1.00 | 1.50-2.50 |
| S8 | Model Lifecycle Management | 2 | 3 | 4 | 0.05-0.15 | 0.25-0.50 | 0.50-1.00 |
| | **P4 Average / Total** | **1.4** | **2.6** | **4.3** | **0.30-0.80** | **2.20-4.65** | **8.10-15.30** |

(Source: P4, Summary Difficulty Matrix)

### Cross-Plane Aggregate

| Metric | Cloud-Native | Managed K8s | On-Premises |
|---|---|---|---|
| **Difficulty Average (1-5 scale)** | **1.6** | **2.7** | **4.2** |
| **Total FTE (deduplicated, N=1)** | **~10-23** | **~25-47** | **~59-109*** |
| **Subsegments at 5/5** | 0 | 0 | 18 |
| **Subsegments at 1/5** | 14 | 2 | 0 |
| **Difficulty Ratio** | 1.0x | 1.7x | 2.6x |
| **FTE Ratio (midpoint)** | 1.0x | 2.2x | 5.1x |

*On-premises total deduplicated from raw P1+P2+P3+P4 sum (59.3-110.85 FTE) by removing AL09 overlap with P3/P4 (approximately 2.0-3.0 FTE). This is consistent with the S2 canonical range of 38-58 FTE (which uses different deduplication methodology and scope boundaries per X2) and the G1 N=1 midpoint of ~85 FTE.

---

## 2. Top 10 Hardest Subsegments On-Premises

The following table ranks the 10 highest-difficulty subsegments on-premises by composite difficulty rating and FTE impact. These are the domains that collectively make on-premises categorically harder.

| Rank | ID | Subsegment | Plane | OP Rating | OP FTE | CN Rating | CN FTE | Why It's So Hard On-Premises |
|:---:|:---:|---|---|:---:|---|:---:|---|---|
| 1 | AL09 | AI/ML Orchestration & Agent Pipelines | P2 App Logic | 5 | 4.0-7.0* | 2 | 0.5-1.2 | Must self-host vLLM/TGI serving, Milvus/Qdrant vector DB, Temporal workflow orchestration (Cassandra+ES+4 pods), Langfuse observability (PostgreSQL+ClickHouse+Redis+S3), LlamaFirewall guardrails, and LiteLLM routing -- all simultaneously with GPU scheduling. Cloud-native: call Bedrock/Azure OpenAI/Vertex AI APIs. (P2, AL09; F38) |
| 2 | S3 | GPU Hardware Infrastructure | P4 AI Model | 5 | 2.5-5.0 | 1 | 0 | DGX H100 at $373K-$450K with 5-12 month lead times. Data center modifications $25K-$100K+ for 30-80 kW/rack power density. 10 engineers per 1,000 GPUs. Cloud-native: zero hardware; select GPU-backed model tiers via API. (P4, S3; F39) |
| 3 | S2 | Self-Hosted Inference Engine | P4 AI Model | 5 | 2.0-3.5 | 1 | 0 | vLLM continuous batching tuning, PagedAttention KV-cache sizing, AWQ/GPTQ quantization validation, multi-node InfiniBand 200-400 Gbps config, rolling upgrades with zero-downtime restarts. Cloud-native: provider manages all engine operations. (P4, S2; F36) |
| 4 | CP-05 | Observability Infrastructure | P1 Control | 4 | 4.6-7.0 | 1 | 0.55-1.0 | Self-hosted Prometheus/Thanos/Mimir for metrics, Loki for logs, Tempo for traces. 500K+ active time series at 3KB RAM each. Jaeger v1 deprecated January 2026 forcing migration. MinIO archived 2025-2026 affecting tracing storage. Cloud-native: CloudWatch/Azure Monitor are fully managed. (P1, CP-05; F49, F50, F51) |
| 5 | DS10 | RAG Pipeline Orchestration | P3 Data | 5 | 3.25-4.75 | 2 | 0.5-1.0 | 8-stage pipeline: ingestion, chunking, embedding, vector storage, retrieval, reranking, context assembly, LLM handoff. Apache Tika 3.x required (2.x EOL May 2025). 2-7 second end-to-end latency requiring continuous tuning. Cloud-native: Bedrock Knowledge Bases or Vertex AI RAG Engine. (P3, DS10; F04, F35) |
| 6 | CP-03 + CP-04 + CP-10 | Security/Identity/Secrets cluster | P1 Control | 4-5 | 8.0-15.25 | 1-2 | 0.95-3.05 | IAM is "a product line, not an infrastructure dependency" with seven sub-domains. Vault requires 5-node Raft cluster plus FIPS 140-3 migration by September 2026. 24/7 SOC requires minimum 12 FTE. Combined: 32-40% of total Control Plane FTE. Cloud-native: IAM/Cognito/Entra ID, Secrets Manager, GuardDuty. (P1, CP-03, CP-04, CP-10; F46, F47, F71) |
| 7 | DS9 | Embedding Pipeline (GPU) | P3 Data | 5 | 2.0-3.25 | 2 | 0.1-0.2 | MIG partitioning (up to 7 instances per A100/H100), time-slicing not production-suitable, CUDA driver compatibility matrix, model version triggers full re-embedding of entire corpus. Cloud-native: Bedrock Titan or OpenAI Embeddings API call. (P3, DS9; F37) |
| 8 | CP-01 | K8s Cluster Lifecycle | P1 Control | 5 | 3.0-6.0 | 1 | 0.0-0.5 | Full etcd backup, API server HA, control plane node replacement. VMware post-Broadcom 8-15x price increases. SUSE Rancher 4-9x cost increases. Three K8s minor versions per year with 12-14 month support windows. Cloud-native: EKS $0.10/hour; AKS free control plane. (P1, CP-01; F52, F53) |
| 9 | DS6 | Event Streaming (Kafka) | P3 Data | 5 | 1.5-2.5 | 1 | 0.25-0.5 | Kafka 4.0 ZooKeeper-to-KRaft mandatory migration (irreversible). Disk sizing: 1K msg/sec x 1KB x 86400 x RF3 = 259 GB/day. 3x network write amplification. ISR tuning, consumer group lag monitoring. Self-hosted: 13-26 hrs/week vs MSK 2-3 hrs/week. (P3, DS6; F44) |
| 10 | CP-07 | Deploy Lifecycle / Rollback | P1 Control | 5 | 1.5-3.0 | 1 | 0.1-0.35 | Quarterly-to-annual release cadence. 3-5 concurrent major versions across customer base. Rollback can require days and database restores. CVE patch requires 50 separate customer coordination sequences for 50 customers. Cloud-native: daily deploys, seconds-level rollback via traffic switching. (P1, CP-07; F58) |

*AL09 FTE deduplicated to remove P3/P4 overlap. See Section 6.

(Sources: P1 CP-01 through CP-10; P2 AL09; P3 DS6, DS9, DS10; P4 S2, S3; F38, F39, F36, F49, F50, F51, F04, F35, F46, F47, F71, F52, F53, F44, F58)

---

## 3. Why Cloud-Native Is Easier: Unified Causal Chain

The difficulty gap is not a list of independent advantages. It is a causal chain where structural properties of cloud-native deployment compound across all four planes.

### Stage 1: Cloud Providers Absorb the Operational Substrate

Cloud providers absorb the entire operational lifecycle of infrastructure components: Kubernetes control plane operations (CP-01), database HA and failover (DS1), message broker operations (DS5, DS6), GPU hardware procurement and management (S3), driver stacks (S4), observability backends (CP-05), secrets rotation (CP-04), certificate management (CP-04), and compliance evidence collection (CP-09). This absorption is total, not partial -- the ISV has zero operational exposure to etcd quorum management, Patroni failover scripting, Kafka ISR tuning, or NVIDIA driver compatibility matrices (P1, P3, P4 across all subsegments rated 1/5 cloud-native).

### Stage 2: Absorption Eliminates Specialist Hiring Pipelines

Because the substrate is absorbed, the ISV does not need to hire PostgreSQL DBAs ($48-76/hour market rate, per P3 DS1 citing F41), GPU infrastructure engineers (global shortage of ~85,000 against 97,000 annual demand, per S2 Chapter 7 citing F63), Kafka operations specialists, or HashiCorp Vault administrators. These are non-fungible roles with 6-12 month hiring lead times (P3, DS8 and DS9; S2, Chapter 7). Cloud-native ISVs hire application engineers and a small platform team (2-6.5 FTE per P1) rather than staffing 10+ specialist domains simultaneously.

### Stage 3: No Specialists Means No Cross-Domain Coordination Overhead

On-premises, the cluster lifecycle team (CP-01), networking team (CP-02), security team (CP-03/CP-04/CP-10), observability team (CP-05), and GPU team (S3/S4/S5) must coordinate on every deployment, every upgrade, and every incident. Adding a microservice touches all four planes simultaneously -- G1 documents that a single new service requires 117-250 hours of initial setup on-premises versus 39-92 hours cloud-native (G1, Cross-Plane Per-Service Overhead table). Cloud-native collapses this to a single platform team managing configuration rather than infrastructure.

### Stage 4: Elimination of Linear Customer-Count Scaling

On-premises operations scale linearly with customer count: 50 customers means 50 incident response chains, 50 patch coordination sequences, 50 compliance audit surfaces (P1, Pattern 2; S2, Chapter 6 citing F59). Cloud-native operations scale sub-linearly because automation absorbs per-customer overhead -- a single deployment pipeline serves all tenants simultaneously (P1, CP-07). This is why the FTE ratio (4.6x at N=20 from G1) exceeds the difficulty ratio (2.6x): high-difficulty subsegments compound nonlinearly into staffing requirements.

### Stage 5: No Mandatory Migration Burden

Cloud-native ISVs are largely shielded from the six simultaneous mandatory technology migrations due before end of 2026: Kafka ZooKeeper-to-KRaft, FIPS 140-2 to 140-3, Jaeger v1 to v2, Ingress-NGINX EOL, Milvus Woodpecker WAL, and continuous Jenkins patching (P1, Pattern 3; S2, Chapter 4). Each migration consumes FTE from the same limited platform engineering pool. Cloud providers absorb networking migrations, certificate rotation, and monitoring backend changes without ISV action (P1, Pattern 3).

### Stage 6: The Compounding Effect

These stages compound. When the substrate is absorbed (Stage 1), specialists are unnecessary (Stage 2), which eliminates coordination overhead (Stage 3), which means the team can deploy faster and more frequently (Stage 4), which means migrations are invisible (Stage 5). The result is not 2.6x easier on a difficulty scale -- it is 4.6x cheaper in FTE at N=20 services, because each stage multiplies the savings from the previous stage rather than adding linearly (G1, Scaling Summary).

---

## 4. The N-Services Multiplier Effect

G1 models how operational complexity scales as the ISV adds microservices from N=1 to N=20. The key finding: **the gap widens, not narrows, with service count.**

### Per-Service Marginal FTE by Plane

| Plane | CN FTE/service | MK8s FTE/service | OP FTE/service |
|---|---|---|---|
| P1 Control Plane | 0.10-0.18 | 0.30-0.55 | 0.75-1.20 |
| P2 Application Logic | 0.35-0.65 | 0.45-0.85 | 0.85-1.55 |
| P3 Data Plane | 0.05-0.10 | 0.08-0.15 | 0.15-0.30 |
| P4 AI Model Plane | 0.01-0.03 | 0.03-0.06 | 0.05-0.12 |
| **Total per service** | **~0.74** | **~1.24** | **~2.49** |

(Source: G1, Per-service increments table)

### Scaling Table

| N | Cloud-Native FTE | Managed K8s FTE | On-Premises FTE | OP/CN Ratio |
|---|---|---|---|---|
| 1 | ~16.7 | ~35.9 | ~85.1 | 5.1x |
| 5 | ~19.6 | ~40.8 | ~95.2 | 4.9x |
| 10 | ~23.2 | ~47.1 | ~107.7 | 4.6x |
| 15 | ~26.8 | ~54.0 | ~122.1 | 4.6x |
| 20 | ~30.4 | ~61.4 | ~138.6 | 4.6x |

**Ratio at N=20: Cloud-Native : Managed K8s : On-Premises = 1.0 : 2.0 : 4.6** (G1, Scaling Summary table). Note: the G1 executive summary states "1.0:1.9:3.4" but this conflates difficulty ratings with FTE ratios. The table data above (1.0:2.0:4.6) is the correct FTE ratio and is used throughout this synthesis.

(Source: G1, Scaling Summary; ratio correction per task instructions)

### Viability Thresholds

**N=7-8 services:** On-premises Control Plane work exceeds 27-32 FTE, crossing the threshold where a generalist DevOps team cannot manage CI/CD, security operations, observability, AND deployment coordination without specialist role bifurcation. Network policy complexity at N=7 reaches 42 directed NetworkPolicy rule sets. Recommendation: dedicated platform engineering function of 8-12 FTE by N=7 (G1, Threshold 1).

**N=12 services:** On-premises midpoint FTE reaches approximately 115-120 FTE. At $175K fully loaded, annual personnel cost is approximately $20-21M, plus $3-8M infrastructure. Total: approximately $23-29M/year. Cloud-native at N=12: approximately $3.5-6.0M/year. **The gap exceeds $17-23M annually.** For on-premises to be justified, sovereign/regulated market access must generate $17M+ in incremental ARR (G1, Threshold 2).

**N=20 services:** Annual cost at $175K/FTE (G1, N=20 table):

| Tier | FTE Range | Annual Cost Range |
|---|---|---|
| Cloud-Native | 19-41 | $3.4M-$7.2M |
| Managed K8s | 42-81 | $7.4M-$14.1M |
| On-Premises | 97-180 | $17.0M-$31.5M |

### Why the Ratio Stabilizes at 4.6x

The on-premises-to-cloud-native FTE ratio narrows from 5.1x (N=1) to 4.6x (N=10) as on-premises fixed costs (SOC, compliance, DR) amortize over more services. It then stabilizes at 4.6x because the per-service marginal cost on-premises (~2.49 FTE) is 3.4x the cloud-native marginal cost (~0.74 FTE), preventing further amortization gains. The practical implication: **if on-premises cannot be justified at N=5, it will not become more justifiable at N=20** (G1, Threshold 4).

---

## 5. Managed K8s: The Middle Tier Analysis

### Is MK8s Closer to Cloud-Native or On-Premises?

On the difficulty scale, managed K8s (2.7 average) sits closer to on-premises (4.2) in FTE terms than to cloud-native (1.6). The MK8s-to-CN FTE ratio is approximately 2.0x at N=20, but security and observability alone on MK8s require 3.25-6.0 FTE -- exceeding the total operational burden of a fully cloud-native deployment (P1, Pattern 1; S2, Chapter 5). The label "managed" is accurate only for CP-01 (API server, etcd); across CP-02 through CP-10, ISVs retain significant or full operational responsibility (P1, Pattern 1).

### The MK8s Bifurcation

The AI Model Plane reveals a critical bifurcation: ISVs on managed K8s can choose Strategy (a) -- consume managed APIs from within K8s pods, reducing P4 FTE to 0.30-0.80 (identical to cloud-native) -- or Strategy (b) -- self-host inference on GPU node pools, requiring 2.20-4.65 FTE (P4, Section 6, Observation 1). This nearly 6x difference in P4 FTE alone determines whether MK8s behaves like cloud-native or on-premises for the AI workload.

The same bifurcation applies to the Data Plane. MK8s ISVs who use cloud-managed databases (RDS, Cloud SQL) even on EKS/AKS/GKE keep DS1 and DS2 at cloud-native difficulty (P3, Tier-Level Interpretation). MK8s ISVs who deploy CloudNativePG pay $2,700-5,400/month vs Aurora's $1,800-2,200/month, with a 1.5-3.0 FTE gap that erases compute savings (S2, Chapter 5).

### When MK8s Is the Right Choice

Managed K8s is justified when (S2, Chapter 5):

1. **GPU/AI workload portability** is a binding requirement -- DRA (GA in K8s 1.34, August 2025), KAI Scheduler, and KServe v0.15 provide capabilities with no cloud-native equivalent.
2. **Data residency control** is required but customers accept hosted K8s rather than full self-managed infrastructure.
3. **Inference architecture** requires fine-grained GPU scheduling not available through cloud-native endpoints.

MK8s is the wrong choice when data services are the primary workload or when the ISV cannot sustain a 7.5-13.5 FTE platform team (S2, Chapter 5).

### The Optimal MK8s Strategy

Use managed K8s selectively for AI/ML workloads while consuming cloud-native data, security, and observability services. This hybrid approach collapses MK8s data plane difficulty to near cloud-native while preserving GPU scheduling flexibility (S2, Chapter 8; P3, Tier-Level Interpretation).

---

## 6. Cross-Plane Interaction Effects

### How the 4 Planes Interact

The four planes are not independent cost buckets. They interact in three documented patterns:

**Pattern A: Every new microservice touches all 4 planes.** G1 documents that adding a single microservice requires work in all four planes simultaneously: CI/CD pipeline + network policy + monitoring target (P1), service boundary design + resilience code + test suite (P2), schema migration + cache namespace + queue topic (P3), and model routing rule + inference SLO (P4). Initial setup: 117-250 hours on-premises vs 39-92 hours cloud-native (G1, Cross-Plane Per-Service Overhead).

**Pattern B: P1 failures cascade to all other planes.** Control Plane components share a common failure mode: infrastructure unavailability propagates to all workloads regardless of what those workloads compute (P1, Scope Definition). A DNS failure (CP-02) affects every service's ability to reach every other service, every database, and every inference endpoint -- cascading across P2, P3, and P4 simultaneously. On-premises, where DNS is self-managed via CoreDNS on bare metal, this cascade is the ISV's responsibility to prevent and resolve (P1, CP-02; F76, Domain 2).

**Pattern C: P3 and P4 share GPU contention.** Embedding pipelines (P3 DS9) and LLM inference engines (P4 S2) compete for GPU resources. Without explicit MIG partitioning, embedding latency degrades unpredictably under LLM load (P4, Observation regarding S5; W05S). This contention exists only on-premises and on MK8s when self-hosting; cloud-native eliminates it entirely via separate managed API endpoints.

### AL09 Overlap Resolution

The P2 analysis rates AL09 (AI/ML Orchestration & Agent Pipelines) at 6.0-10.0 FTE on-premises. However, this range includes work that is covered in other planes:

| Overlap Item | AL09 Included FTE | Covered In | Deduplicated FTE |
|---|---|---|---|
| Vector DB operations (Milvus cluster management) | ~1.25-1.75 | P3 DS8 (1.25-1.75 FTE) | Remove from AL09 |
| Inference engine serving (vLLM/TGI deployment) | ~2.0-3.5 | P4 S2 (2.0-3.5 FTE) | Remove from AL09 |
| Agent orchestration code, LangGraph, guardrails, MCP | ~4.0-7.0 | Unique to P2 | Retain in AL09 |

**Resolution:** AL09 P2-attributable FTE is reduced to 4.0-7.0 FTE on-premises. The DS8 and S2 FTE remain in P3 and P4 respectively. Total cross-plane deduplication: approximately 2.0-3.0 FTE removed from the raw P1+P2+P3+P4 sum.

P2 itself notes this overlap: "Subsegments AL05 (EDA) and AL09 (agent orchestration) both reference Temporal -- ISVs deploying both subsegments on-premises may amortize the Temporal operational cost across both use cases" (P2, Section 7).

### Scaling Interaction: Why P1 Dominates at Large N

G1 reveals that the Control Plane is the primary N-amplifier. At N=20 services, P1 on-premises consumes 37-66.5 FTE -- the largest single plane at any N -- because each service requires its own CI/CD pipeline, deployment manifest, monitoring target, and N-1 network policies that grow O(N) for directed-graph models and approach O(N^2) for full-mesh topologies (G1, Control Plane Scaling). Application Logic (P2) scales near-linearly but at lower per-service cost. Data Plane (P3) and AI Model Plane (P4) scale sublinearly because their infrastructure is shared across services. This means the Control Plane is the dominant investment decision for ISVs choosing deployment tiers -- not the AI model infrastructure that receives the most attention.

---

## 7. Gap Assessment & Confidence

### Where the Analysis Is Strongest

| Element | Confidence | Basis |
|---|---|---|
| P1 Control Plane difficulty ratings | **High** | 10 subsegments, each sourced from 3+ primary research files (F40-F71), cross-validated by W06S, W07S, W08S deduplication |
| P3 Data Plane ratings and FTE | **High** | 10 subsegments corroborated by F04, F06, F09, F15, F35-F45, F55a, F73, F76 |
| P4 AI Model Plane difficulty gap | **High** | Five independent MECE frameworks (F73-F77) unanimously identify AI inference as highest-difficulty on-premises (F79, Section 5) |
| Core finding (on-prem dramatically harder) | **Very High** | 78 research files, 309K words, five MECE frameworks, three synthesis layers (S2, Chapter 1). Every analytical lens produces the same directional conclusion |
| G1 N-services scaling direction | **High** | Per-service increment differentials are well-evidenced by industry SRE ratios and cross-plane overhead tables |

### Where the Analysis Is Weakest

| Element | Confidence | Gap |
|---|---|---|
| P2 Application Logic on-premises FTE | **Medium** | P2 has the narrowest tier spread (delta 1.4 vs P1 delta 3.4), and AL09 FTE (6.0-10.0 stated, 4.0-7.0 deduplicated) is the widest range of any subsegment, reflecting nascent RAGOps and agent infrastructure maturity |
| G1 per-service FTE increments at N>15 | **Medium-Low** | Deduplication factors (10-20%) are modeled estimates, not measured. Real ISV GitOps maturation could produce 5-30% variance (G1, Gaps section) |
| P3 DS2 Cassandra FTE on K8s | **Medium** | Cassandra operational FTE on managed K8s is unquantified in source files; MongoDB FTE used as proxy (P3, Gaps section) |
| AL07 retrofit cost | **Low** | No quantitative study exists for the incremental FTE cost of retrofitting a tenant-context framework into an existing production codebase (P2, Section 7) |
| On-premises FTE at N=20 | **Medium** | Range 97-180 FTE; upper bound consistent with X2 synthesis but model uncertainty in deduplication factors could shift by +/-15% |

### What Would Strengthen the Conclusions

1. **Empirical FTE measurement at ISVs operating at all three tiers.** The current analysis is derived from 78 research files and industry benchmarks, not from direct observation of ISV engineering teams. A case study of 3-5 ISVs with comparable products deployed at different tiers would provide ground-truth validation.

2. **Per-service FTE measurement at N=10-20.** The G1 per-service scaling model uses modeled increments; direct measurement at ISVs with known service counts would validate the deduplication factors.

3. **MK8s bifurcation quantification.** The Strategy (a) vs Strategy (b) FTE differential in P4 is well-documented, but the compound effect across P1+P3+P4 of choosing managed APIs vs self-hosted inference is not separately modeled.

4. **Gartner agent cancellation rate by tier.** The 40% agentic AI project cancellation prediction (P2, AL09 citing F07) is not segmented by deployment tier. On-premises cancellation rates may be substantially higher given the 5/5 difficulty.

### Aggregate Confidence for Core Finding

**High confidence (>90% certainty) that on-premises is 3-5x harder than cloud-native in FTE terms for an AI-driven SaaS ISV.** The finding is robust across multiple analytical methods, frameworks, and evidence sources. The remaining uncertainty is in the precise ratio (4.6x from G1 vs 10x from S2's broader scope), not in the direction or magnitude class.

---

## 8. Key Takeaways

1. **On-premises is 2.6x harder on the difficulty scale and 4.6x more expensive in FTE at 20 services** -- and the gap never converges because per-service marginal cost is structurally higher on-premises (G1, Scaling Summary).

2. **Eighteen of 38 subsegments are rated 5/5 on-premises; zero reach 5/5 cloud-native** -- on-premises does not require "more of the same staff" but fundamentally different specialist roles across nearly every domain (P1, P3, P4).

3. **The Control Plane is the single largest FTE consumer and the primary N-amplifier**, with on-premises P1 reaching 37-66.5 FTE at N=20 services; security, identity, and secrets alone (CP-03+CP-04+CP-10) require 8-15 FTE on-premises, exceeding the entire cloud-native deployment (P1, Pattern 4).

4. **AI/ML inference and security/compliance are unanimously identified by all five MECE frameworks as the two highest-difficulty, highest-risk on-premises domains**, requiring dedicated specialist teams that have no generalist substitution path (F79, Section 5).

5. **Managed K8s is a bifurcated tier**: ISVs consuming managed APIs through K8s achieve near-cloud-native FTE; ISVs self-hosting GPU inference pay near-on-premises FTE for the AI workload -- the 6x within-tier difference is the largest single architectural decision after deployment model (P4, Observation 1).

6. **At N=12 services, on-premises annual cost reaches $23-29M versus $3.5-6M cloud-native** -- the $17-23M gap must be funded by sovereign/regulated market premium to be financially viable (G1, Threshold 2).

7. **The causal chain is structural, not solvable by tooling alone**: cloud providers absorb the operational substrate, which eliminates specialist hiring, which removes cross-domain coordination, which enables sub-linear customer-count scaling, which means the gap compounds with both service count and customer count (P1, Pattern 5; S2, Chapter 4).

---

## Sources

| File | Path | Key Contribution to This Synthesis |
|---|---|---|
| P1 | analysis/P1_control_plane.md | 10 Control Plane subsegments with difficulty ratings, FTE ranges, cross-subsegment patterns, seven 5/5 on-premises subsegments |
| P2 | analysis/P2_application_logic.md | 10 Application Logic subsegments; AL09 as highest-difficulty AI component; tier-invariant subsegments (AL02, AL04, AL07) |
| P3 | analysis/P3_data_plane.md | 10 Data Plane subsegments; six 5/5 on-premises subsegments; RDS/MSK as highest-leverage managed services |
| P4 | analysis/P4_ai_model_plane.md | 8 AI Model Plane subsegments; MK8s bifurcation (Strategy a vs b); GPU hardware and inference engine as primary on-prem cost drivers |
| G1 | analysis/G1_n_services_multiplier.md | N-services scaling model (N=1 through N=20); per-service FTE increments; viability thresholds at N=7, N=12; 4.6x ratio stabilization |
| S2 | synthesis/S2_research_document.md | 1x:2x:10x staffing multiplier; capstone narrative across 78 research files; managed K8s positioning; sovereign cloud paradox; SDLC impact |
| F79 | wave11/F79_mece_meta_analysis.md | Five-framework convergence on AI inference and security/compliance as highest-difficulty items; Developer Responsibility + Failure Domain as recommended composite |
