# GT5: Cross-Reference Ground Truth
## G1 and S1 Authoritative Aggregates for Three-Phase Ratings Validation

**Date:** 2026-02-19
**Scope:** Extraction of authoritative cross-plane aggregates, scaling models, and synthesis findings from G1 (N-services multiplier) and S1 (four-plane synthesis) for use as validation reference against `analysis/three_phase_on_prem_ratings.md`.
**Agent Role:** Ground truth extraction — no interpretation, no analysis, raw data only.

---

## Executive Summary

G1 establishes a quantified N-services scaling model with per-service marginal FTE midpoints of CN ~0.74, MK8s ~1.24, and OP ~2.49, and two viability thresholds at N=7-8 and N=12 services. S1 synthesizes difficulty averages of 1.6 (CN), 2.7 (MK8s), and 4.2 (OP) across all 38 subsegments, with FTE ratios of 1.0:2.0:4.6 at N=20 and 18 of 38 subsegments rated 5/5 on-premises. Together these two files establish the authoritative quantitative floor against which any aggregate claim in the three-phase ratings file must be checked.

---

## Section 1: G1 Scaling Model

### 1.1 Baseline FTE at N=1 (Single Service)

[DATA POINT]
"Cloud-Native ~16.7 FTE, Managed K8s ~35.9 FTE, On-Premises ~85.1 FTE at N=1"
— G1_n_services_multiplier.md, Scaling Summary table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

| Plane | CN Low | CN High | MK8s Low | MK8s High | OP Low | OP High |
|---|---|---|---|---|---|---|
| P1 Control Plane | 2.50 | 6.50 | 9.00 | 16.00 | 20.00 | 38.00 |
| P2 Application Logic | 5.80 | 13.20 | 9.40 | 19.80 | 19.30 | 38.00 |
| P3 Data Plane | 1.55 | 2.70 | 4.10 | 6.55 | 11.85 | 19.55 |
| P4 AI Model Plane | 0.30 | 0.80 | 2.20 | 4.65 | 8.10 | 15.30 |
| **Total (N=1)** | **10.15** | **23.20** | **24.70** | **47.00** | **59.25** | **110.85** |

[FACT] "The P1–P4 planes were sized for a mid-size ISV serving 50 enterprise customers. The absolute FTE numbers include team overhead, on-call, and management — not just the per-subsegment technical work."
— G1_n_services_multiplier.md, Methodology section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

---

### 1.2 Per-Service Marginal FTE by Plane and Tier

[DATA POINT]
Per-service FTE increment (per additional service beyond the 1st):

| Plane | CN FTE/service | MK8s FTE/service | OP FTE/service |
|---|---|---|---|
| P1 Control Plane | 0.10–0.18 | 0.30–0.55 | 0.75–1.20 |
| P2 Application Logic | 0.35–0.65 | 0.45–0.85 | 0.85–1.55 |
| P3 Data Plane | 0.05–0.10 | 0.08–0.15 | 0.15–0.30 |
| P4 AI Model Plane | 0.01–0.03 | 0.03–0.06 | 0.05–0.12 |
| **Total per service** | **0.51–0.96** | **0.86–1.61** | **1.80–3.17** |
| **Midpoint per service** | **~0.74** | **~1.24** | **~2.49** |

— G1_n_services_multiplier.md, "Per-service increments (combined across all 4 planes)" table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT] "A 10% deduplication factor is applied above N=10 to account for GitOps automation and shared CI tooling maturation."
— G1_n_services_multiplier.md, Deduplication note
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

---

### 1.3 N-Services Scaling Table (Midpoints)

[DATA POINT]

| N | CN FTE (midpoint) | MK8s FTE (midpoint) | OP FTE (midpoint) | OP/CN Ratio |
|---|---|---|---|---|
| 1 | ~16.7 | ~35.9 | ~85.1 | 5.1x |
| 5 | ~19.6 | ~40.8 | ~95.2 | 4.9x |
| 10 | ~23.2 | ~47.1 | ~107.7 | 4.6x |
| 15 | ~26.8 | ~54.0 | ~122.1 | 4.6x |
| 20 | ~30.4 | ~61.4 | ~138.6 | 4.6x |

— G1_n_services_multiplier.md, Scaling Summary table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT] "The On-Prem / Cloud-Native ratio narrows slightly from N=1 to N=5 because some on-premises fixed costs (security operations, compliance infrastructure) are amortized over more services. But it stabilizes at approximately 4.6x from N=10 onward."
— G1_n_services_multiplier.md, Key observation on ratio behavior
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT] "The Managed K8s / Cloud-Native ratio holds near 1.7x–2.0x across all N, confirming that managed K8s scales with approximately the same proportionality as cloud-native but at a structurally higher baseline."
— G1_n_services_multiplier.md, Key observation on ratio behavior
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

---

### 1.4 Annual Personnel Cost at N=20 (Fully Loaded at $175K/FTE)

[STATISTIC]

| Tier | FTE Range | Annual Cost (Low) | Annual Cost (High) |
|---|---|---|---|
| Cloud-Native | 19.4–41.4 | $3.4M | $7.2M |
| Managed K8s | 42.0–80.7 | $7.4M | $14.1M |
| On-Premises | 97.0–180.2 | $17.0M | $31.5M |

— G1_n_services_multiplier.md, "Annual personnel cost at N=20" table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

---

### 1.5 Initial Setup and Steady-State Per-Service Overhead

[DATA POINT]

| Metric | Cloud-Native | Managed K8s | On-Premises |
|---|---|---|---|
| Total initial setup (range, hrs) | 39–92 hrs | 65–142 hrs | 117–250 hrs |
| Total initial setup (FTE-days) | ~5–12 days | ~8–18 days | ~15–31 days |
| Annual steady-state (range, hrs/yr) | 42–84 hrs/yr | 94–184 hrs/yr | 220–432 hrs/yr |
| Annualized FTE per service | 0.021–0.042 FTE | 0.047–0.092 FTE | 0.110–0.216 FTE |

— G1_n_services_multiplier.md, "Initial Setup Work Per New Service" and "Ongoing Annual Steady-State Per Service" tables
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[DATA POINT] Combined (initial setup amortized over 3 years + steady-state):

| Metric | Cloud-Native | Managed K8s | On-Premises |
|---|---|---|---|
| Initial setup (midpoint, hrs) | ~65 hrs | ~104 hrs | ~184 hrs |
| Amortized initial over 3 yrs (hrs/yr) | ~22 hrs/yr | ~35 hrs/yr | ~61 hrs/yr |
| Annual steady-state (midpoint, hrs/yr) | ~63 hrs/yr | ~139 hrs/yr | ~326 hrs/yr |
| **Total annual cost per service** | **~85 hrs/yr** | **~174 hrs/yr** | **~387 hrs/yr** |
| **FTE equivalent per service per year** | **~0.043 FTE** | **~0.087 FTE** | **~0.194 FTE** |

— G1_n_services_multiplier.md, "Combined" table following steady-state data
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

---

### 1.6 Viability Thresholds

[FACT — Threshold 1]
"At N=7–8 services: Control Plane work on-premises exceeds 27–32 FTE. This crosses the threshold where: (1) A single generalist DevOps team cannot manage CI/CD, security operations, observability, AND deployment coordination simultaneously without specialist role bifurcation. (2) Network policy complexity (7×6=42 directed NetworkPolicy rule sets) requires a dedicated network security engineer. (3) Deployment version fragmentation (3–5 major versions × 7 services = 21–35 distinct compatibility combinations) requires dedicated release engineering."
— G1_n_services_multiplier.md, Threshold 1
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Threshold 1 Recommendation]
"Hire a minimum dedicated platform engineering function of 8–12 FTE by N=7 or accept elevated production incident frequency and release cadence slowdowns."
— G1_n_services_multiplier.md, Threshold 1
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Threshold 2]
"At N=12 services (interpolated from the N=10 and N=15 data points), on-premises midpoint FTE reaches approximately 115–120 FTE. At $175K fully loaded: Annual personnel cost: approximately $20M–$21M. Annual infrastructure cost (hardware, licenses, facilities): estimated $3M–$8M additional. Total on-premises annual cost: approximately $23M–$29M."
— G1_n_services_multiplier.md, Threshold 2
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Threshold 2 Gap]
"The on-premises-to-cloud-native cost gap at N=12 exceeds $17M–$23M annually. For an ISV to justify on-premises at this scale, the addressable market premium from sovereign cloud and regulated-industry access must generate at least $17M+ in incremental ARR per year."
— G1_n_services_multiplier.md, Threshold 2
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Threshold 4]
"If on-premises cannot be justified at N=5, it will not become more justifiable at N=20."
— G1_n_services_multiplier.md, Threshold 4
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Threshold 4 Mechanism]
"The per-service marginal cost on-premises (~2.49 FTE) is 3.4x the cloud-native marginal cost (~0.74 FTE), preventing further amortization gains."
— S1_four_plane_synthesis.md, Section 4: Why the Ratio Stabilizes at 4.6x
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

### 1.7 Plane-Level Scaling Characteristics (G1)

[FACT — Control Plane]
"Control Plane scaling is the primary N-amplifier. Each new service requires its own CI/CD pipeline, deployment manifest, monitoring target, and a set of N-1 new network policies — sub-elements that are counted once per service but whose interaction surface grows with O(N) for directed-graph network policies and O(N²) for full-mesh topologies."
— G1_n_services_multiplier.md, Executive Summary, Finding 1
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Application Logic]
"Application Logic scales near-linearly. Nearly all Application Logic subsegments (service decomposition, resilience patterns, test suites, observability instrumentation) scale one-for-one with service count."
— G1_n_services_multiplier.md, Executive Summary, Finding 2
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Data Plane]
"Data Plane scales sublinearly. Services share databases, caches, message queues, and vector stores. Adding the Nth service adds marginal schema, cache namespace, and queue topic overhead — but the stateful infrastructure itself (PostgreSQL HA cluster, Redis Sentinel, Kafka brokers, vector DB) is largely fixed."
— G1_n_services_multiplier.md, Executive Summary, Finding 3
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — AI Model Plane]
"AI Model Plane scales minimally. Inference infrastructure is fundamentally shared. Adding a service that calls the LLM API adds effectively zero AI Model Plane FTE at cloud-native."
— G1_n_services_multiplier.md, Executive Summary, Finding 4
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Critical Threshold]
"At N=10 services, on-premises reaches the minimum viable staffing floor for a dedicated platform engineering team (≥10 FTE in Control Plane alone). At N=15, total on-premises FTE exceeds 100 for the mid-size ISV case — a figure that strains the financial model of any venture-backed or bootstrapped ISV."
— G1_n_services_multiplier.md, Executive Summary, Critical Threshold
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

---

## Section 2: S1 Cross-Plane Aggregates

### 2.1 Cross-Plane Difficulty Averages (1–5 Scale)

[DATA POINT]

| Plane | Cloud-Native | Managed K8s | On-Premises |
|---|:---:|:---:|:---:|
| P1 Control Plane | 1.3 | 2.8 | 4.7 |
| P2 Application Logic | 2.0 | 2.6 | 3.4 |
| P3 Data Plane | 1.5 | 2.9 | 4.4 |
| P4 AI Model Plane | 1.4 | 2.6 | 4.3 |
| **Cross-Plane Average** | **1.6** | **2.7** | **4.2** |

— S1_four_plane_synthesis.md, Executive Summary difficulty table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

### 2.2 FTE Aggregate at N=1 (Deduplicated)

[DATA POINT]

| Metric | Cloud-Native | Managed K8s | On-Premises |
|---|---|---|---|
| **Difficulty Average (1-5 scale)** | **1.6** | **2.7** | **4.2** |
| **Total FTE (deduplicated, N=1)** | **~10-23** | **~25-47** | **~59-109*** |
| **Subsegments at 5/5** | 0 | 0 | 18 |
| **Subsegments at 1/5** | 14 | 2 | 0 |
| **Difficulty Ratio** | 1.0x | 1.7x | 2.6x |
| **FTE Ratio (midpoint)** | 1.0x | 2.2x | 5.1x |

*On-premises total deduplicated from raw P1+P2+P3+P4 sum (59.3–110.85 FTE) by removing AL09 overlap with P3/P4 (approximately 2.0–3.0 FTE).

— S1_four_plane_synthesis.md, Section 1: Cross-Plane Aggregate table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

### 2.3 FTE Ratios at N=20

[DATA POINT]
"Ratio at N=20: Cloud-Native : Managed K8s : On-Premises = 1.0 : 2.0 : 4.6"
— S1_four_plane_synthesis.md, Section 4: Scaling Table note
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Ratio Correction Note]
"The G1 executive summary states '1.0:1.9:3.4' but this conflates difficulty ratings with FTE ratios. The table data (1.0:2.0:4.6) is the correct FTE ratio and is used throughout this synthesis."
— S1_four_plane_synthesis.md, Section 4: Scaling Table note, ratio correction
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

### 2.4 FTE at N=20 (from S1 Reproduction of G1 Data)

[DATA POINT]

| Tier | FTE Range | Annual Cost Range |
|---|---|---|
| Cloud-Native | 19–41 | $3.4M–$7.2M |
| Managed K8s | 42–81 | $7.4M–$14.1M |
| On-Premises | 97–180 | $17.0M–$31.5M |

— S1_four_plane_synthesis.md, Section 4: Viability Thresholds, N=20 table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

### 2.5 Subsegment-Level Difficulty Data (All 38 Subsegments)

[DATA POINT — P1 Control Plane, 10 subsegments]

| ID | Subsegment | CN | MK8s | OP | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| CP-01 | K8s Cluster Lifecycle | 1 | 3 | 5 | 0.0–0.5 | 1.0–2.5 | 3.0–6.0 |
| CP-02 | Network Fabric / Ingress / Mesh | 1 | 3 | 5 | 0.1–0.7 | 0.75–1.75 | 1.75–3.5 |
| CP-03 | IAM / RBAC | 1 | 2 | 4 | 0.3–0.8 | 1.65–2.65 | 2.75–4.75 |
| CP-04 | Secrets / Certs / PKI | 1 | 2 | 5 | 0.4–0.85 | 0.4–0.85 | 2.5–5.0 |
| CP-05 | Observability Infrastructure | 1 | 3 | 4 | 0.55–1.0 | 1.25–2.0 | 4.6–7.0 |
| CP-06 | CI/CD Pipeline / GitOps | 1 | 3 | 4 | 0.3–0.4 | 1.3–1.9 | 2.0–3.25 |
| CP-07 | Deploy Lifecycle / Rollback | 1 | 3 | 5 | 0.1–0.35 | 0.35–0.75 | 1.5–3.0 |
| CP-08 | Disaster Recovery / BC | 2 | 3 | 5 | 0.25–0.5 | 0.5–1.0 | 1.5–2.5 |
| CP-09 | Compliance Automation | 2 | 3 | 5 | 0.5–1.0 | 1.25–2.0 | 2.5–4.0 |
| CP-10 | Security Operations | 2 | 3 | 5 | 0.25–1.2 | 2.25–4.5 | 2.75–5.5 |
| | **P1 Average / Total** | **1.3** | **2.8** | **4.7** | **2.5–6.5** | **9–16** | **20–38** |

— S1_four_plane_synthesis.md, Section 1: P1 Control Plane table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[DATA POINT — P2 Application Logic, 10 subsegments]

| ID | Subsegment | CN | MK8s | OP | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| AL01 | Service Decomp / Inter-Service Comm | 2 | 2 | 3 | 0.5–1.0 | 0.6–1.1 | 0.8–1.5 |
| AL02 | Business Logic / Domain Services | 2 | 2 | 2 | 3.0–6.0 | 3.0–6.0 | 3.0–6.0 |
| AL03 | API Gateway / Edge Routing | 2 | 3 | 4 | 0.1–0.2 | 0.3–0.6 | 1.5–3.0 |
| AL04 | Data Access / ORM / Caching | 2 | 2 | 2 | 0.5–1.0 | 0.5–1.0 | 0.75–1.5 |
| AL05 | Background Jobs / Async / EDA | 1 | 3 | 4 | 0.1–0.2 | 0.4–0.8 | 2.75–5.6 |
| AL06 | Resilience Patterns / Runtime | 2 | 3 | 4 | 0.15–0.3 | 0.3–0.6 | 0.75–1.5 |
| AL07 | Multi-Tenant Isolation | 3 | 3 | 3 | 0.5–1.0 | 0.5–1.0 | 0.75–1.5 |
| AL08 | Observability Instrumentation | 2 | 2 | 3 | 0.2–0.4 | 0.3–0.6 | 0.5–1.0 |
| AL09 | AI/ML Orchestration / Agent Pipelines | 2 | 3 | 5 | 0.5–1.2 | 2.0–4.0 | 4.0–7.0* |
| AL10 | Testing / Contract Testing / Env Parity | 2 | 3 | 4 | 0.7–1.65 | 2.0–4.0 | 3.75–7.0 |
| | **P2 Average / Total** | **2.0** | **2.6** | **3.4** | **5.8–13.2** | **9.4–19.8** | **18.6–35.6*** |

*AL09 FTE deduplicated; see Section 6 of S1 for overlap resolution.

— S1_four_plane_synthesis.md, Section 1: P2 Application Logic table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[DATA POINT — P3 Data Plane, 10 subsegments]

| ID | Subsegment | CN | MK8s | OP | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| DS1 | Relational Database HA | 2 | 3 | 5 | 0.25–0.50 | 0.50–0.85 | 1.50–3.00 |
| DS2 | NoSQL / Document Store | 1 | 3 | 4 | 0.10 | 0.40–0.70 | 0.60–1.10 |
| DS3 | Caching Layer | 2 | 3 | 4 | 0.10 | 0.25 | 0.40–0.70 |
| DS4 | Object / Blob Storage | 1 | 2 | 3 | 0.05–0.10 | 0.10–0.20 | 0.25–0.60 |
| DS5 | Message Queuing (Simple) | 1 | 2 | 3 | 0.10 | 0.20–0.30 | 0.40–0.70 |
| DS6 | Event Streaming (Kafka) | 1 | 4 | 5 | 0.25–0.50 | 0.50–1.00 | 1.50–2.50 |
| DS7 | Search / Full-Text Index | 2 | 3 | 5 | 0.10–0.20 | 0.25–0.50 | 0.70–1.20 |
| DS8 | Vector Database | 1 | 3 | 5 | 0.00–0.10 | 0.40–0.70 | 1.25–1.75 |
| DS9 | Embedding Pipeline (GPU) | 2 | 3 | 5 | 0.10–0.20 | 0.50–0.80 | 2.00–3.25 |
| DS10 | RAG Pipeline Orchestration | 2 | 3 | 5 | 0.50–1.00 | 1.00–1.50 | 3.25–4.75 |
| | **P3 Average / Total** | **1.5** | **2.9** | **4.4** | **1.55–2.70** | **4.10–6.55** | **11.85–19.55** |

— S1_four_plane_synthesis.md, Section 1: P3 Data Plane table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[DATA POINT — P4 AI Model Plane, 8 subsegments]

| ID | Subsegment | CN | MK8s | OP | CN FTE | MK8s FTE | OP FTE |
|:---:|---|:---:|:---:|:---:|---|---|---|
| S1 | Managed API Integration | 1 | 1 | 2 | 0.05–0.15 | 0.05–0.15 | 0.10–0.30 |
| S2 | Self-Hosted Inference Engine | 1 | 3 | 5 | 0 | 0.75–1.50 | 2.00–3.50 |
| S3 | GPU Hardware Infrastructure | 1 | 2 | 5 | 0 | 0.10–0.25 | 2.50–5.00 |
| S4 | GPU Driver / CUDA Stack | 1 | 2 | 4 | 0 | 0.10–0.25 | 0.50–1.00 |
| S5 | Multi-Tenant GPU Scheduling | 1 | 3 | 5 | 0 | 0.25–0.50 | 0.50–1.00 |
| S6 | Model Routing / Load Balancing | 2 | 3 | 4 | 0.10–0.25 | 0.20–0.50 | 0.50–1.00 |
| S7 | Inference Monitoring | 2 | 4 | 5 | 0.10–0.25 | 0.50–1.00 | 1.50–2.50 |
| S8 | Model Lifecycle Management | 2 | 3 | 4 | 0.05–0.15 | 0.25–0.50 | 0.50–1.00 |
| | **P4 Average / Total** | **1.4** | **2.6** | **4.3** | **0.30–0.80** | **2.20–4.65** | **8.10–15.30** |

— S1_four_plane_synthesis.md, Section 1: P4 AI Model Plane table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

## Section 3: S1 Top 10 Hardest Subsegments On-Premises

[DATA POINT — Ranked list]

| Rank | ID | Subsegment | Plane | OP Rating | OP FTE | CN Rating | CN FTE |
|:---:|:---:|---|---|:---:|---|:---:|---|
| 1 | AL09 | AI/ML Orchestration & Agent Pipelines | P2 App Logic | 5 | 4.0–7.0* | 2 | 0.5–1.2 |
| 2 | S3 | GPU Hardware Infrastructure | P4 AI Model | 5 | 2.5–5.0 | 1 | 0 |
| 3 | S2 | Self-Hosted Inference Engine | P4 AI Model | 5 | 2.0–3.5 | 1 | 0 |
| 4 | CP-05 | Observability Infrastructure | P1 Control | 4 | 4.6–7.0 | 1 | 0.55–1.0 |
| 5 | DS10 | RAG Pipeline Orchestration | P3 Data | 5 | 3.25–4.75 | 2 | 0.5–1.0 |
| 6 | CP-03 + CP-04 + CP-10 | Security/Identity/Secrets cluster | P1 Control | 4–5 | 8.0–15.25 | 1–2 | 0.95–3.05 |
| 7 | DS9 | Embedding Pipeline (GPU) | P3 Data | 5 | 2.0–3.25 | 2 | 0.1–0.2 |
| 8 | CP-01 | K8s Cluster Lifecycle | P1 Control | 5 | 3.0–6.0 | 1 | 0.0–0.5 |
| 9 | DS6 | Event Streaming (Kafka) | P3 Data | 5 | 1.5–2.5 | 1 | 0.25–0.5 |
| 10 | CP-07 | Deploy Lifecycle / Rollback | P1 Control | 5 | 1.5–3.0 | 1 | 0.1–0.35 |

*AL09 FTE deduplicated to remove P3/P4 overlap.

— S1_four_plane_synthesis.md, Section 2: Top 10 Hardest Subsegments On-Premises table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Rank 1 AL09 rationale]
"Must self-host vLLM/TGI serving, Milvus/Qdrant vector DB, Temporal workflow orchestration (Cassandra+ES+4 pods), Langfuse observability (PostgreSQL+ClickHouse+Redis+S3), LlamaFirewall guardrails, and LiteLLM routing -- all simultaneously with GPU scheduling. Cloud-native: call Bedrock/Azure OpenAI/Vertex AI APIs."
— S1_four_plane_synthesis.md, Section 2, Rank 1 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Rank 2 S3 rationale]
"DGX H100 at $373K–$450K with 5–12 month lead times. Data center modifications $25K–$100K+ for 30–80 kW/rack power density. 10 engineers per 1,000 GPUs. Cloud-native: zero hardware; select GPU-backed model tiers via API."
— S1_four_plane_synthesis.md, Section 2, Rank 2 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Rank 4 CP-05 rationale]
"Self-hosted Prometheus/Thanos/Mimir for metrics, Loki for logs, Tempo for traces. 500K+ active time series at 3KB RAM each. Jaeger v1 deprecated January 2026 forcing migration. MinIO archived 2025–2026 affecting tracing storage."
— S1_four_plane_synthesis.md, Section 2, Rank 4 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Rank 9 DS6 rationale]
"Kafka 4.0 ZooKeeper-to-KRaft mandatory migration (irreversible). Disk sizing: 1K msg/sec x 1KB x 86400 x RF3 = 259 GB/day. 3x network write amplification. Self-hosted: 13–26 hrs/week vs MSK 2–3 hrs/week."
— S1_four_plane_synthesis.md, Section 2, Rank 9 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Rank 10 CP-07 rationale]
"Quarterly-to-annual release cadence. 3–5 concurrent major versions across customer base. Rollback can require days and database restores. CVE patch requires 50 separate customer coordination sequences for 50 customers. Cloud-native: daily deploys, seconds-level rollback via traffic switching."
— S1_four_plane_synthesis.md, Section 2, Rank 10 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

## Section 4: S1 Structural Findings — Unified Causal Chain

[FACT — Stage 1]
"Cloud providers absorb the entire operational lifecycle of infrastructure components: Kubernetes control plane operations (CP-01), database HA and failover (DS1), message broker operations (DS5, DS6), GPU hardware procurement and management (S3), driver stacks (S4), observability backends (CP-05), secrets rotation (CP-04), certificate management (CP-04), and compliance evidence collection (CP-09). This absorption is total, not partial."
— S1_four_plane_synthesis.md, Section 3, Stage 1
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Stage 2]
"Because the substrate is absorbed, the ISV does not need to hire PostgreSQL DBAs ($48–76/hour market rate), GPU infrastructure engineers (global shortage of ~85,000 against 97,000 annual demand), Kafka operations specialists, or HashiCorp Vault administrators. These are non-fungible roles with 6–12 month hiring lead times."
— S1_four_plane_synthesis.md, Section 3, Stage 2
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Stage 3]
"On-premises, the cluster lifecycle team (CP-01), networking team (CP-02), security team (CP-03/CP-04/CP-10), observability team (CP-05), and GPU team (S3/S4/S5) must coordinate on every deployment, every upgrade, and every incident. Adding a microservice touches all four planes simultaneously -- G1 documents that a single new service requires 117–250 hours of initial setup on-premises versus 39–92 hours cloud-native."
— S1_four_plane_synthesis.md, Section 3, Stage 3
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Stage 4]
"On-premises operations scale linearly with customer count: 50 customers means 50 incident response chains, 50 patch coordination sequences, 50 compliance audit surfaces. Cloud-native operations scale sub-linearly because automation absorbs per-customer overhead -- a single deployment pipeline serves all tenants simultaneously. This is why the FTE ratio (4.6x at N=20) exceeds the difficulty ratio (2.6x): high-difficulty subsegments compound nonlinearly into staffing requirements."
— S1_four_plane_synthesis.md, Section 3, Stage 4
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Stage 5 — Six Mandatory Migrations]
"Cloud-native ISVs are largely shielded from the six simultaneous mandatory technology migrations due before end of 2026: Kafka ZooKeeper-to-KRaft, FIPS 140-2 to 140-3, Jaeger v1 to v2, Ingress-NGINX EOL, Milvus Woodpecker WAL, and continuous Jenkins patching."
— S1_four_plane_synthesis.md, Section 3, Stage 5
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Stage 6 — Compounding Effect]
"When the substrate is absorbed (Stage 1), specialists are unnecessary (Stage 2), which eliminates coordination overhead (Stage 3), which means the team can deploy faster and more frequently (Stage 4), which means migrations are invisible (Stage 5). The result is not 2.6x easier on a difficulty scale -- it is 4.6x cheaper in FTE at N=20 services, because each stage multiplies the savings from the previous stage rather than adding linearly."
— S1_four_plane_synthesis.md, Section 3, Stage 6
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Core Structural Statement]
"Cloud providers absorb the operational substrate (infrastructure lifecycle, security posture, observability backends, data service HA, GPU management), and that absorption eliminates not just the direct FTE of each domain but the cross-domain coordination overhead, the specialist hiring pipeline, the mandatory migration burden, and the linear-with-customer-count scaling penalty that on-premises deployments incur. On-premises is not incrementally harder. It is structurally a different kind of engineering organization."
— S1_four_plane_synthesis.md, Executive Summary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Concentration of Extreme Difficulty]
"Seven of the 10 Control Plane subsegments are rated 5/5 on-premises (CP-01, CP-02, CP-04, CP-07, CP-08, CP-09, CP-10), and six Data Plane subsegments reach 5/5 on-premises (DS1, DS6, DS7, DS8, DS9, DS10). No subsegment in any plane reaches 5/5 at cloud-native."
— S1_four_plane_synthesis.md, Executive Summary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — MK8s Bifurcation]
"ISVs on managed K8s can choose Strategy (a) -- consume managed APIs from within K8s pods, reducing P4 FTE to 0.30–0.80 (identical to cloud-native) -- or Strategy (b) -- self-host inference on GPU node pools, requiring 2.20–4.65 FTE. This nearly 6x difference in P4 FTE alone determines whether MK8s behaves like cloud-native or on-premises for the AI workload."
— S1_four_plane_synthesis.md, Section 5: The MK8s Bifurcation
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — AL09 Overlap Resolution]

| Overlap Item | AL09 Stated FTE | Covered In | Resolution |
|---|---|---|---|
| Vector DB operations (Milvus cluster management) | ~1.25–1.75 | P3 DS8 (1.25–1.75 FTE) | Remove from AL09 |
| Inference engine serving (vLLM/TGI deployment) | ~2.0–3.5 | P4 S2 (2.0–3.5 FTE) | Remove from AL09 |
| Agent orchestration code, LangGraph, guardrails, MCP | ~4.0–7.0 | Unique to P2 | Retain in AL09 |

— S1_four_plane_synthesis.md, Section 6: AL09 Overlap Resolution table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Key Takeaway: Control Plane FTE at N=20]
"Security, identity, and secrets alone (CP-03+CP-04+CP-10) require 8–15 FTE on-premises, exceeding the entire cloud-native deployment."
— S1_four_plane_synthesis.md, Section 8, Key Takeaway 3
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Five MECE Frameworks Convergence]
"AI/ML inference and security/compliance are unanimously identified by all five MECE frameworks as the two highest-difficulty, highest-risk on-premises domains, requiring dedicated specialist teams that have no generalist substitution path."
— S1_four_plane_synthesis.md, Section 8, Key Takeaway 4; citing F79_mece_meta_analysis.md, Section 5
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

## Section 5: Confidence Limitations

### 5.1 G1 Confidence Assessment

[DATA POINT]

| Element | Confidence | Known Gap |
|---|---|---|
| P1–P4 baseline FTE ranges | High | Assumes 50-customer mid-size ISV; smaller ISVs may have lower fixed FTE |
| Per-service CP-02 NetworkPolicy increment | Medium | No direct study of FTE hours per NetworkPolicy rule set at each tier |
| Per-service CP-06 CI/CD increment | Medium-High | ISV-specific CI/CD pipeline cost per service is not directly published |
| Per-service AL10 Test suite increment | Medium | No published breakdown of test suite cost per service at each tier |
| Per-service P3 Data Plane increment | Medium | Direct FTE measurement of per-schema operational cost not found |
| Per-service P4 AI Model Plane increment | High | Assumes 50% AI-enabled services; actual AI-enabling rate varies significantly |
| Deduplication factors at N>10 | Low-Medium | 10–20% deduplication applied; no quantitative study of deduplication rate |
| SRE-to-service ratio validation | Medium | Published ratio represents hyperscale organizations; ISV-specific ratios at 5–20 service scale not found in peer-reviewed literature |
| On-premises FTE total at N=20 | Medium | Range 97–180 FTE; P1–P4 planes may include some overlap not fully resolved |

— G1_n_services_multiplier.md, Gaps and Confidence Assessment table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

[FACT — Primary Model Uncertainty]
"The N-services model presented here represents a theoretical additive construction. Real ISV operations exhibit two properties that partially offset the linear growth: (1) GitOps-managed service onboarding through ArgoCD/Flux templates significantly reduces per-service setup time at cloud-native and managed K8s tiers; (2) mature internal developer platforms (IDPs) shift per-service onboarding from SRE/DevOps to product engineers, reducing visible operational FTE even if total engineering effort is similar. On-premises has no equivalent absorber for these effects."
— G1_n_services_multiplier.md, Model limitation note
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md`

---

### 5.2 S1 Confidence Assessment

[DATA POINT — Where Analysis Is Strongest]

| Element | Confidence | Basis |
|---|---|---|
| P1 Control Plane difficulty ratings | High | 10 subsegments, each sourced from 3+ primary research files (F40–F71), cross-validated by W06S, W07S, W08S |
| P3 Data Plane ratings and FTE | High | 10 subsegments corroborated by F04, F06, F09, F15, F35–F45, F55a, F73, F76 |
| P4 AI Model Plane difficulty gap | High | Five independent MECE frameworks (F73–F77) unanimously identify AI inference as highest-difficulty on-premises |
| Core finding (on-prem dramatically harder) | Very High | 78 research files, 309K words, five MECE frameworks, three synthesis layers |
| G1 N-services scaling direction | High | Per-service increment differentials well-evidenced by industry SRE ratios and cross-plane overhead tables |

— S1_four_plane_synthesis.md, Section 7: Where the Analysis Is Strongest table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[DATA POINT — Where Analysis Is Weakest]

| Element | Confidence | Gap |
|---|---|---|
| P2 Application Logic on-premises FTE | Medium | AL09 FTE (6.0–10.0 stated, 4.0–7.0 deduplicated) is the widest range of any subsegment, reflecting nascent RAGOps and agent infrastructure maturity |
| G1 per-service FTE increments at N>15 | Medium-Low | Deduplication factors (10–20%) are modeled estimates, not measured; real ISV GitOps maturation could produce 5–30% variance |
| P3 DS2 Cassandra FTE on K8s | Medium | Cassandra operational FTE on managed K8s is unquantified; MongoDB FTE used as proxy |
| AL07 retrofit cost | Low | No quantitative study exists for incremental FTE cost of retrofitting a tenant-context framework into an existing production codebase |
| On-premises FTE at N=20 | Medium | Range 97–180 FTE; model uncertainty in deduplication factors could shift by +/-15% |

— S1_four_plane_synthesis.md, Section 7: Where the Analysis Is Weakest table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Aggregate Confidence Statement]
"High confidence (>90% certainty) that on-premises is 3–5x harder than cloud-native in FTE terms for an AI-driven SaaS ISV. The finding is robust across multiple analytical methods, frameworks, and evidence sources. The remaining uncertainty is in the precise ratio (4.6x from G1 vs 10x from S2's broader scope), not in the direction or magnitude class."
— S1_four_plane_synthesis.md, Section 7: Aggregate Confidence for Core Finding
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

[FACT — Data Gaps Requiring Future Work]
"(1) Empirical FTE measurement at ISVs operating at all three tiers. The current analysis is derived from 78 research files and industry benchmarks, not from direct observation of ISV engineering teams. (2) Per-service FTE measurement at N=10–20. (3) MK8s bifurcation quantification across P1+P3+P4 compound effect. (4) Gartner agent cancellation rate by tier: the 40% agentic AI project cancellation prediction is not segmented by deployment tier."
— S1_four_plane_synthesis.md, Section 7: What Would Strengthen the Conclusions
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md`

---

## Quick Reference Summary Tables

### Table A: Key Numerical Anchors for Validation

| Metric | Value | Source |
|---|---|---|
| Cross-plane difficulty CN | 1.6 (1–5 scale) | S1, Executive Summary |
| Cross-plane difficulty MK8s | 2.7 (1–5 scale) | S1, Executive Summary |
| Cross-plane difficulty OP | 4.2 (1–5 scale) | S1, Executive Summary |
| P1 average difficulty OP | 4.7 | S1, Section 1 |
| P2 average difficulty OP | 3.4 | S1, Section 1 |
| P3 average difficulty OP | 4.4 | S1, Section 1 |
| P4 average difficulty OP | 4.3 | S1, Section 1 |
| OP subsegments at 5/5 | 18 of 38 | S1, Section 1 aggregate |
| CN subsegments at 5/5 | 0 | S1, Section 1 aggregate |
| FTE ratio at N=20 (CN:MK8s:OP) | 1.0 : 2.0 : 4.6 | S1, Section 4; G1, Scaling Summary |
| Per-service marginal FTE CN | ~0.74 | G1, Per-service increments table |
| Per-service marginal FTE MK8s | ~1.24 | G1, Per-service increments table |
| Per-service marginal FTE OP | ~2.49 | G1, Per-service increments table |
| Viability threshold T1 | N=7–8 (specialist bifurcation required) | G1, Threshold 1 |
| Viability threshold T2 | N=12 ($23–29M/yr OP cost) | G1, Threshold 2 |
| OP annual cost gap at N=12 | $17–23M vs CN | G1, Threshold 2 |
| OP total FTE at N=20 | 97–180 FTE | G1, N=20 table |
| CN total FTE at N=20 | 19–41 FTE | G1, N=20 table |

### Table B: Viability Thresholds Summary

| Threshold | N | Trigger | Recommended Response |
|---|---|---|---|
| T1 | N=7–8 | OP Control Plane exceeds 27–32 FTE; network policies reach 42 directed rule sets | Hire 8–12 FTE dedicated platform engineering function |
| T2 | N=12 | OP annual cost reaches $23–29M; gap to CN exceeds $17–23M | Sovereign/regulated market must generate $17M+ incremental ARR |
| T3 | N=15 | MK8s ~$4.8M/yr premium over CN justified only with GPU portability requirement | Evaluate managed API vs self-hosted bifurcation decision |
| T4 | N=any | No N exists where OP amortizes to near-CN cost; ratio stabilizes at 4.6x | Decision is architectural, not economic scaling |

### Table C: Top 10 Hardest Subsegments — OP Rating Summary

| Rank | ID | OP Rating | OP FTE | Delta from CN |
|---|---|:---:|---|---|
| 1 | AL09 | 5 | 4.0–7.0 | +3 difficulty pts; CN 0.5–1.2 FTE |
| 2 | S3 | 5 | 2.5–5.0 | +4 difficulty pts; CN 0 FTE |
| 3 | S2 | 5 | 2.0–3.5 | +4 difficulty pts; CN 0 FTE |
| 4 | CP-05 | 4 | 4.6–7.0 | +3 difficulty pts; CN 0.55–1.0 FTE |
| 5 | DS10 | 5 | 3.25–4.75 | +3 difficulty pts; CN 0.5–1.0 FTE |
| 6 | CP-03+04+10 | 4–5 | 8.0–15.25 | +2–4 difficulty pts; CN 0.95–3.05 FTE |
| 7 | DS9 | 5 | 2.0–3.25 | +3 difficulty pts; CN 0.1–0.2 FTE |
| 8 | CP-01 | 5 | 3.0–6.0 | +4 difficulty pts; CN 0.0–0.5 FTE |
| 9 | DS6 | 5 | 1.5–2.5 | +4 difficulty pts; CN 0.25–0.5 FTE |
| 10 | CP-07 | 5 | 1.5–3.0 | +4 difficulty pts; CN 0.1–0.35 FTE |

---

## Sources

| File | Absolute Path | Sections Extracted |
|---|---|---|
| G1_n_services_multiplier.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md` | Executive Summary; Per-Plane Scaling Model; Quantified N-Services Model; Scaling Summary; Cross-Plane Per-Service Overhead; Viability Thresholds (T1–T4); Gaps and Confidence Assessment |
| S1_four_plane_synthesis.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md` | Executive Summary; Section 1 (all four plane tables, cross-plane aggregate); Section 2 (Top 10 Hardest Subsegments); Section 3 (Unified Causal Chain, Stages 1–6); Section 4 (N-Services Multiplier, Scaling Table, Viability Thresholds); Section 5 (MK8s Bifurcation); Section 6 (AL09 Overlap Resolution); Section 7 (Gap Assessment and Confidence); Section 8 (Key Takeaways) |
