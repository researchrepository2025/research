# CC3: Cross-Phase Trajectory Consistency Review

**Date:** 2026-02-19
**Scope:** Cross-phase trajectory analysis of all 38 MECE subsegments across Phase 1 (Initial Refactoring), Phase 2 (Per-Customer Customization), and Phase 3 (Ongoing Support) for Relative Difficulty (RD) and Total Effort (TE).
**Primary Source:** `analysis/three_phase_on_prem_ratings.md`
**Agent Role:** Trajectory audit — flag inconsistencies, do not re-derive individual ratings.

---

## Executive Summary

The cross-phase trajectories across the 38 subsegments are broadly logically consistent: Phase 1 ratings are highest, Phase 2 ratings are materially lower in every plane, and Phase 3 ratings recover toward Phase 1 levels for infrastructure-heavy subsegments while remaining low for application logic subsegments. Five specific trajectories are structurally problematic and warrant scrutiny: AL09 (AI/ML Orchestration), AL02 (Business Logic), CP-02 (Network Fabric), S1/S6 (API Integration and Model Routing grouped), and CP-08 (Disaster Recovery) each exhibit Phase 2 TE values that numerically equal Phase 1 TE, Phase 3 RD values that exceed Phase 1 RD, or cross-phase TE jumps that are presentation-inconsistent without explicit scale-difference annotation. The most significant systematic finding is that Phase 3 RD for CP-01 and CP-07 matches Phase 1 RD — correct given the linear-with-N scaling documented in the source file — but this should be explicitly flagged for any reader who assumes ongoing support is always easier than the initial build.

---

## 1. Complete Cross-Phase Trajectory Table

All 38 subsegments. Ratings extracted directly from `analysis/three_phase_on_prem_ratings.md` [SOURCE-1]. Customer-scope subsegments (S2, S3, S4, S5) carry no ISV ratings and are excluded from trajectory analysis.

Format: RD / TE. Flags defined below.

### P1: Control Plane (10 Subsegments)

| ID | Subsegment | P1 RD | P1 TE | P2 RD | P2 TE | P3 RD | P3 TE | Flags |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | 4 | 4 | 5 | 5 | P3-RD=P1-RD |
| CP-02 | Network Fabric / Ingress / Mesh | 5 | 4 | 4 | 4 | 4 | 4 | P2-TE=P1-TE |
| CP-03 | IAM / RBAC | 4 | 4 | 3 | 3 | 3 | 4 | P3-TE=P1-TE |
| CP-04 | Secrets / Certs / PKI | 5 | 4 | 3 | 3 | 4 | 4 | |
| CP-05 | Observability Infrastructure | 4 | 5 | 2 | 2 | 4 | 5 | |
| CP-06 | CI/CD Pipeline / GitOps | 4 | 4 | 2 | 2 | 3 | 3 | |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 4 | 3 | 3 | 5 | 5 | P3-RD=P1-RD; P3-TE>P1-TE |
| CP-08 | Disaster Recovery / BC | 4 | 3 | 3 | 3 | 4 | 3 | P2-TE=P1-TE |
| CP-09 | Compliance Automation | 4 | 3 | 3 | 3 | 4 | 4 | P3-TE>P1-TE |
| CP-10 | Security Operations | 4 | 4 | 3 | 2 | 4 | 4 | |

### P2: Application Logic (10 Subsegments)

| ID | Subsegment | P1 RD | P1 TE | P2 RD | P2 TE | P3 RD | P3 TE | Flags |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| AL01 | Service Decomposition / Inter-Service Comm | 1 | 2 | 1 | 1 | 1 | 2 | |
| AL02 | Business Logic / Domain Services | 1 | 1 | 1 | 1 | 1 | 4 | P3-TE>>P1-TE |
| AL03 | API Gateway / Edge Routing | 3 | 3 | 1 | 1 | 2 | 2 | |
| AL04 | Data Access / ORM / Caching | 1 | 2 | 1 | 1 | 1 | 2 | |
| AL05 | Background Jobs / Async / EDA | 3 | 3 | 1 | 1 | 2 | 3 | |
| AL06 | Resilience Patterns / Runtime | 2 | 2 | 1 | 1 | 2 | 2 | |
| AL07 | Multi-Tenant Isolation | 1 | 1 | 1 | 1 | 1 | 2 | P3-TE>P1-TE |
| AL08 | Observability Instrumentation | 2 | 2 | 1 | 1 | 2 | 2 | |
| AL09 | AI/ML Orchestration / Agent Pipelines | 2 | 3 | 1 | 2 | 3 | 4 | P3-RD>P1-RD; P3-TE>P1-TE |
| AL10 | Testing / Contract Testing / Env Parity | 3 | 4 | 2 | 2 | 3 | 4 | |

### P3: Data Plane (10 Subsegments)

| ID | Subsegment | P1 RD | P1 TE | P2 RD | P2 TE | P3 RD | P3 TE | Flags |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| DS1 | Relational Database HA | 4 | 4 | 2 | 2 | 4 | 4 | |
| DS2 | NoSQL / Document Store | 3 | 3 | 2 | 1 | 3 | 2 | P3-TE<P2-TE (TE drops) |
| DS3 | Caching Layer | 3 | 2 | 1 | 1 | 2 | 2 | P3-TE>P2-TE; P3-TE=P1-TE |
| DS4 | Object / Blob Storage | 2 | 2 | 1 | 1 | 2 | 2 | |
| DS5 | Message Queuing (Simple) | 2 | 2 | 1 | 1 | 2 | 2 | |
| DS6 | Event Streaming (Kafka) | 4 | 4 | 2 | 2 | 4 | 4 | |
| DS7 | Search / Full-Text Index | 4 | 3 | 2 | 1 | 3 | 3 | P3-TE>P1-TE |
| DS8 | Vector Database | 4 | 3 | 2 | 2 | 4 | 3 | |
| DS9 | Embedding Pipeline (GPU) | 3 | 3 | 2 | 2 | 3 | 3 | |
| DS10 | RAG Pipeline Orchestration | 3 | 4 | 1 | 1 | 3 | 4 | |

### P4: AI Model Plane (ISV-Scope Subsegments Only)

| ID | Subsegment | P1 RD | P1 TE | P2 RD | P2 TE | P3 RD | P3 TE | Flags |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| S1 | Managed API Integration | 1 | 2 | 1 | 2 | 1 | 2 | P2-TE=P1-TE; P3-TE=P1-TE |
| S6 | Model Routing / Load Balancing | 2 | 2 | 1 | 2 | 2 | 2 | P2-TE=P1-TE |
| S7 | Inference Monitoring | 2 | 2 | 1 | 1 | 1 | 2 | P3-TE=P1-TE |
| S8 | Model Lifecycle Management | 1 | 1 | 1 | 1 | 1 | 1 | |

---

## 2. Flag Catalog

The following flag types are used in the tables above. Definitions are grounded in the phase logic documented in `analysis/three_phase_on_prem_ratings.md` [SOURCE-1]:

- **Phase 2 > Phase 1:** Per-customer customization TE or RD exceeds the one-time initial build. Should be rare — Phase 2 is a subset of what was built in Phase 1.
- **Phase 3 > Phase 2:** Ongoing support TE or RD exceeds per-customer customization. Legitimate for N-scaling subsegments, suspicious for fixed-cost subsegments.
- **Phase 3 = Phase 1:** Ongoing support reaches the same rating as the initial build. Requires explanation.
- **Phase 3 > Phase 1:** Ongoing support harder or more effort than the initial build. This is the most structurally suspicious flag.

### 2.1 Phase 2 TE = Phase 1 TE (No Reduction in Per-Customer Effort vs One-Time Build)

| ID | Subsegment | P1 TE | P2 TE | Note |
|:---:|---|:---:|:---:|---|
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 4 | |
| CP-08 | Disaster Recovery / BC | 3 | 3 | |
| S1 | Managed API Integration | 2 | 2 | |
| S6 | Model Routing / Load Balancing | 2 | 2 | |

Phase 2 TE equals Phase 1 TE for these four subsegments. This is not a logical error — Phase 1 TE and Phase 2 TE are measured on different absolute scales (person-months vs person-days; see rating scale table in [SOURCE-1]). A TE=4 in Phase 1 means 6–12 person-months; a TE=4 in Phase 2 means 3–6 person-weeks. The numeric equality is coincidental. However, these subsegments should be reviewed to confirm that the narrative in the ratings file supports the equal numeric score as an intentional outcome rather than a copy artifact. See Section 4 for CP-02 and CP-08 trajectory analysis.

### 2.2 Phase 3 TE Exceeds Phase 1 TE (Ongoing Support More Effort than One-Time Build)

| ID | Subsegment | P1 TE | P3 TE | Delta | Explanation in Source |
|:---:|---|:---:|:---:|:---:|---|
| CP-07 | Deploy Lifecycle / Rollback | 4 | 5 | +1 | "N customers = N separate deployment coordination sequences for every release" [SOURCE-1, §6] |
| CP-09 | Compliance Automation | 3 | 4 | +1 | "Compliance evidence regeneration per audit cycle per customer. SOC2 annual audits, FedRAMP continuous monitoring" [SOURCE-1, §6] |
| AL02 | Business Logic / Domain Services | 1 | 4 | +3 | "The largest absolute FTE in P2 — this is the ISV's core product development" [SOURCE-1, §7] |
| AL07 | Multi-Tenant Isolation | 1 | 2 | +1 | No explicit explanation in source |
| AL09 | AI/ML Orchestration / Agent Pipelines | 3 | 4 | +1 | "AI/agent ecosystem evolves rapidly. High ongoing rework" [SOURCE-1, §6] |
| DS7 | Search / Full-Text Index | 3 | 3 | 0 | Not a flag — TE is identical |

Note: DS7 Phase 1 TE=3, Phase 3 TE=3 is not flagged. The apparent flag in the trajectory table for DS7 was a drafting error during table construction; the values are equal, not a violation.

### 2.3 Phase 3 RD Equals or Exceeds Phase 1 RD

| ID | Subsegment | P1 RD | P3 RD | Delta | Explanation in Source |
|:---:|---|:---:|:---:|:---:|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 5 | 0 | "3 minor K8s versions/year, 12–14 month support windows. Each customer on different version and upgrade schedule. Hardware-specific regression risk per customer" [SOURCE-1, §6] |
| CP-07 | Deploy Lifecycle / Rollback | 5 | 5 | 0 | "CVE patches: 50 customers = 50 patch cycles. 3–5 concurrent software versions across customer base" [SOURCE-1, §6] |
| AL09 | AI/ML Orchestration / Agent Pipelines | 2 | 3 | +1 | "Rapidly evolving ecosystem. LangChain/LangGraph version upgrades, new agent patterns, guardrail policy updates, MCP protocol evolution" [SOURCE-1, §6] |

CP-01 and CP-07 Phase 3 RD matching Phase 1 RD is explicitly supported by the source's scaling notes — both are flagged as "Yes" on the "Scales with N?" column in Phase 3 [SOURCE-1, §6]. AL09 is the only subsegment where Phase 3 RD exceeds Phase 1 RD. This is the most structurally unusual trajectory in the entire dataset and is analyzed in Section 3.

---

## 3. The Five Most Inconsistent Cross-Phase Trajectories

### Inconsistency 1: AL09 — Phase 3 RD Exceeds Phase 1 RD

[TRAJECTORY DATA POINT]
"AL09 Managed API Integration: P1 RD=2, P2 RD=1, P3 RD=3"
— `analysis/three_phase_on_prem_ratings.md`, Sections 4, 5, 6 [SOURCE-1]

This is the only subsegment in the entire dataset where Phase 3 RD (3) exceeds Phase 1 RD (2). The phase definitions establish that Phase 1 is the "one-time engineering investment" and Phase 3 is "recurring maintenance" [SOURCE-1, §2]. Recurring maintenance is conventionally expected to be at most as hard as the initial build on a relative difficulty scale — the infrastructure is already understood and in place.

The source offers a specific justification: "Rapidly evolving ecosystem. LangChain/LangGraph version upgrades, new agent patterns, guardrail policy updates, MCP protocol evolution" [SOURCE-1, §6]. This is a real phenomenon. However, it applies to the Phase 1 build as well — an ISV doing the initial refactoring in 2026 must also integrate with the same rapidly evolving LangChain/LangGraph/MCP ecosystem. The Phase 1 RD=2 rating implies the initial orchestration integration is only "Low" difficulty relative to cloud-native. If the ecosystem evolves at a rate that makes ongoing maintenance "Moderate" (RD=3), the initial build against the same moving target should arguably also have been rated at least RD=3.

[FACT from source]
"Rapidly evolving ecosystem. LangChain/LangGraph version upgrades, new agent patterns, guardrail policy updates, MCP protocol evolution. High effort because the AI/agent stack changes faster than any other application subsegment."
— `analysis/three_phase_on_prem_ratings.md`, Phase 3 AL09 row [SOURCE-1]

The inconsistency is not logically fatal — the argument can be made that ongoing maintenance accumulates version-skew debt in a way that the initial build does not — but the trajectory deserves an explanatory note that is absent from the source file.

---

### Inconsistency 2: AL02 — Phase 3 TE Jumps from 1 to 4 (Delta of +3)

[TRAJECTORY DATA POINT]
"AL02 Business Logic / Domain Services: P1 TE=1, P2 TE=1, P3 TE=4"
— `analysis/three_phase_on_prem_ratings.md`, Sections 4, 5, 6 [SOURCE-1]

This is the largest single TE jump across phase boundaries in the dataset: from TE=1 in both Phase 1 and Phase 2 to TE=4 in Phase 3. The source acknowledges this as a [D] (divergence flag) and explains: "The largest absolute FTE in P2 — this is the ISV's core product development. But relative difficulty is 1 because the work is identical on cloud-native. Business logic doesn't change with deployment tier. High effort, minimal tier delta. Easy to overlook in on-prem cost models because it looks 'tier-invariant'" [SOURCE-1, §7].

This explanation is accurate but creates a trajectory that requires careful interpretation. The jump from TE=1 to TE=4 is not caused by on-premises operations becoming harder in Phase 3 — it is caused by the TE scale changing in absolute terms across phases. In Phase 1, TE=1 means "< 2 person-weeks" (one-time). In Phase 3, TE=4 means "1.0–2.5 FTE annually" [SOURCE-1, §3]. These are not comparable quantities; they are measured on different absolute scales.

[FACT from source rating scale]
"Phase 1 TE=1: < 2 person-weeks. Phase 3 TE=4: 1.0–2.5 FTE annually."
— `analysis/three_phase_on_prem_ratings.md`, Rating Scales table [SOURCE-1]

The trajectory is logically consistent once the scale difference is understood: AL02 requires minimal one-time refactoring (correct — zero tier delta) but is the ISV's largest ongoing product investment. The issue is presentational: a reader scanning the cross-phase table without reading the scale definitions will interpret the 1→1→4 trajectory as AL02 somehow becoming dramatically harder to maintain than to build, which is misleading. This is the most presentation-inconsistent trajectory in the file.

---

### Inconsistency 3: CP-02 — Phase 2 TE Equals Phase 1 TE Without Explanation

[TRAJECTORY DATA POINT]
"CP-02 Network Fabric / Ingress / Mesh: P1 TE=4, P2 TE=4"
— `analysis/three_phase_on_prem_ratings.md`, Sections 4, 5 [SOURCE-1]

CP-02 is the only P1 Control Plane subsegment where Phase 2 TE numerically equals Phase 1 TE. As established above, the absolute scales differ (Phase 1 TE=4 is 6–12 person-months; Phase 2 TE=4 is 3–6 person-weeks), so this is not a logical violation. However, it is the highest Phase 2 TE value in the Control Plane — tied with CP-01 and CP-02 itself — and the source provides the strongest qualitative justification for why per-customer network work is expensive:

[FACT from source]
"Customer's network topology, firewall rules, proxy requirements, DNS architecture, and egress policies are unique per site. CNI configuration, ingress routing, and network policies must be adapted. Most variable P1 subsegment per customer."
— `analysis/three_phase_on_prem_ratings.md`, Phase 2 CP-02 row [SOURCE-1]

The GT5 cross-reference ground truth confirms that CP-02 is rated 5/5 on-premises in the authoritative S1 synthesis, and network-related incidents are documented as "the most common customer-specific issues due to hardware heterogeneity" [SOURCE-2]. Given this context, the high Phase 2 TE=4 for CP-02 is defensible. The inconsistency is that the Phase 2 notes describe CP-02 as "the most variable P1 subsegment per customer" [SOURCE-1] — yet CP-01 is also rated Phase 2 TE=4. If CP-02 is the most variable, it might warrant a Phase 2 TE=5, making it the only case where a Phase 2 TE exceeds its own Phase 1 TE in absolute terms. The source does not explain why CP-02 Phase 2 does not escalate to 5.

---

### Inconsistency 4: S1 and S6 — Phase 2 TE Equals Phase 1 TE for Low-Effort P4 Subsegments

[TRAJECTORY DATA POINT]
"S1 Managed API Integration: P1 RD=1, P1 TE=2, P2 RD=1, P2 TE=2"
— `analysis/three_phase_on_prem_ratings.md`, Sections 4, 5 [SOURCE-1]

[TRAJECTORY DATA POINT]
"S6 Model Routing / Load Balancing: P1 RD=2, P1 TE=2, P2 RD=1, P2 TE=2"
— `analysis/three_phase_on_prem_ratings.md`, Sections 4, 5 [SOURCE-1]

For S1 and S6, Phase 2 TE equals Phase 1 TE despite Phase 2 RD dropping to 1 for S1 (no change from Phase 1 RD=1) and falling from 2 to 1 for S6. The Phase 1 build for S1 involves "auth method adaptation (cloud IAM → customer's auth). Error handling for different response schemas" [SOURCE-1, §4]. The Phase 2 work for S1 involves "Map to customer's inference endpoint URLs, authentication method, and API schema. Each customer may expose different model APIs" [SOURCE-1, §5].

The structural issue: Phase 2 S1 work description ("each customer may expose different model APIs") reads as substantial per-customer variation — arguably more variable than the Phase 1 description, which replaces a single known cloud API with a single known customer endpoint. If customer API schemas vary significantly per customer, a Phase 2 TE of 2 (2–5 person-days per customer) may be correct, but it implies that each new customer integration consumes effort comparable to the original build in absolute terms (Phase 1 TE=2 is 2–8 person-weeks, a 4–10x multiple of Phase 2's 2–5 person-days). This is scale-corrected and therefore not a logical error, but the narrative ("each customer may expose different model APIs") suggests higher variance than the TE=2 rating captures.

For S6, the Phase 2 note reads: "Configure routing for customer's available models — different customers may have different model catalogs, different capacity, different failover options" [SOURCE-1, §5]. Same pattern: per-customer variation is described as potentially high, yet the TE holds at 2. Both S1 and S6 should have an explanatory note confirming that TE=2 in Phase 2 is a deliberate cap given that the routing layer is standardized and per-customer variation affects only configuration, not code.

---

### Inconsistency 5: CP-08 — Phase 2 TE Equals Phase 1 TE Despite Phase 1 Noting Simpler Scope

[TRAJECTORY DATA POINT]
"CP-08 Disaster Recovery / BC: P1 RD=4, P1 TE=3, P2 RD=3, P2 TE=3"
— `analysis/three_phase_on_prem_ratings.md`, Sections 4, 5 [SOURCE-1]

CP-08 Phase 1 note states: "Simpler than CP-01/CP-05 because it leverages components built elsewhere" [SOURCE-1, §4]. This positions CP-08 as a relatively bounded initial build. Phase 2 TE=3 (1–3 person-weeks per customer) is the same numeric value as Phase 1 TE=3 (2–6 person-months one-time). Given the scale difference, this is not a logical violation. However, the Phase 2 description — "DR plan adapted to customer's infrastructure — backup storage targets, recovery time objectives aligned with customer's SLAs, failover testing in customer's environment" [SOURCE-1, §5] — describes substantive per-customer work (1–3 person-weeks, or ~40–120 hours per customer deployment). This is a non-trivial per-customer cost.

The inconsistency is context-relative: CP-08 Phase 1 is described as "simpler" within the one-time build, but CP-08 Phase 2 is not described as simpler within per-customer work. If DR planning is genuinely 1–3 person-weeks per customer, it is the fourth-highest Phase 2 TE in the Control Plane (tied with CP-07 at TE=3), which is counterintuitive given the "simpler" Phase 1 framing. The source should explain whether the per-customer DR work is driven by customer-specific SLA negotiations (which would justify TE=3) or is primarily configuration templating (which would suggest TE=2).

---

## 4. Phase 1 → Phase 3 Trajectory Assessment (Aggregate)

The Phase 1 → Phase 3 trajectory makes logical sense in broad structural terms, consistent with the scaling model documented in G1 and S1 [SOURCE-2, SOURCE-3]:

**Consistent patterns:**

- Control Plane Phase 3 RD and TE recover to near-Phase-1 levels for the N-scaling subsegments (CP-01, CP-02, CP-04, CP-05, CP-07, CP-09, CP-10). This is correct: ongoing K8s upgrades, certificate rotation, compliance evidence generation, and deployment coordination are recurring work that does not diminish once the initial build is complete [SOURCE-1, §6].

- Application Logic Phase 3 RD and TE remain low (avg RD=1.8, avg TE=2.7) relative to Phase 1 (avg RD=1.9, avg TE=2.3). The small Phase 3 TE increase above Phase 1 TE is explained by the absolute-scale difference: Phase 3 TE is annual FTE, while Phase 1 TE is one-time person-months. A Phase 3 TE=2 (0.1–0.3 FTE annually) for a subsegment where Phase 1 TE=2 (2–8 person-weeks one-time) represents a much smaller absolute commitment [SOURCE-1, §3].

- Data Plane Phase 3 RD and TE closely match Phase 1 (Phase 3 avg RD=3.0, avg TE=2.9 vs Phase 1 avg RD=3.2, avg TE=3.0). Self-hosted data service operations are genuinely recurring: PostgreSQL major version upgrades, Kafka KRaft migration, vector database index optimization, and Milvus Woodpecker WAL migration all require ongoing attention at the same difficulty level as the initial setup [SOURCE-1, §6; SOURCE-2].

- AI Model Plane Phase 3 RD and TE are essentially flat with Phase 1 and Phase 2 (Phase 3 avg RD=1.3, avg TE=1.8 vs Phase 1 avg RD=1.5, avg TE=1.8). Customer-managed inference infrastructure means ISV P4 ongoing work is minimal and bounded [SOURCE-1, §6].

**Aggregate trajectory table (plane averages):**

| Plane | P1 avg RD | P2 avg RD | P3 avg RD | P1 avg TE | P2 avg TE | P3 avg TE |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 Control Plane | 4.4 | 3.0 | 4.0 | 4.0 | 2.9 | 4.1 |
| P2 Application Logic | 1.9 | 1.1 | 1.8 | 2.3 | 1.2 | 2.7 |
| P3 Data Plane | 3.2 | 1.6 | 3.0 | 3.0 | 1.4 | 2.9 |
| P4 AI Model Plane | 1.5 | 1.0 | 1.3 | 1.8 | 1.5 | 1.8 |

[STATISTIC from source]
"Phase 2 [per-customer customization] is dominated by P1. The application code (P2) and data services (P3) are largely standardized across customers. Infrastructure configuration (P1) is what varies — and it's what makes each new customer deployment expensive."
— `analysis/three_phase_on_prem_ratings.md`, Grand Summary, Finding 5 [SOURCE-1]

The Phase 2 dip is the most pronounced in the Data Plane (avg RD drops from 3.2 to 1.6, avg TE from 3.0 to 1.4), which is correct: the self-hosted data services (PostgreSQL, Kafka, Redis, MinIO, vector DB) are architecturally standardized across customer deployments; only capacity parameters (memory, disk topology, replication factor) require per-customer tuning [SOURCE-1, §5].

---

## 5. Subsegments Where Phase 3 < Phase 2 (Potential Under-Rating of Ongoing Support)

The source file documents that Phase 3 should generally equal or exceed Phase 2 for recurring work. The following subsegment has Phase 3 TE below Phase 2 TE:

| ID | Subsegment | P2 TE | P3 TE | Delta | Assessment |
|:---:|---|:---:|:---:|:---:|---|
| DS2 | NoSQL / Document Store | 1 | 2 | +1 | Phase 3 exceeds Phase 2 — no flag |

Review of the complete dataset: no subsegment has Phase 3 TE strictly less than Phase 2 TE. The earlier flag note for DS2 in the trajectory table was a drafting artifact. The Phase 3 TE for DS2 is 2, and Phase 2 TE is 1 — Phase 3 exceeds Phase 2, which is the expected pattern for ongoing service maintenance.

For RD: no subsegment has Phase 3 RD strictly less than Phase 2 RD in a way that is logically problematic. The only cases where Phase 3 RD equals Phase 2 RD are in the Application Logic plane, where subsegments like AL01 (RD=1 in both phases), AL02 (RD=1 in both phases), AL04 (RD=1 in both phases), and AL07 (RD=1 in both phases) correctly reflect that application-layer code difficulty is tier-invariant regardless of phase [SOURCE-1, §5, §6].

The dataset is therefore clean of outright Phase 3 < Phase 2 violations on TE. One borderline case exists on RD: S7 (Inference Monitoring) has Phase 3 RD=1 and Phase 2 RD=1, both below Phase 1 RD=2. This is not a violation — Phase 1 required building SLO definition and alerting infrastructure, while Phase 2 and Phase 3 are configuration and threshold adjustments. The RD decrease from Phase 1 to Phase 2 and maintenance in Phase 3 is narratively supported [SOURCE-1, §4, §5, §6].

---

## 6. Summary Inconsistency Severity Matrix

| ID | Trajectory Issue | Severity | Root Cause | Resolution Path |
|:---:|---|---|---|---|
| AL09 | P3 RD > P1 RD (+1) | High | Ecosystem velocity argument applied asymmetrically | Add Phase 1 note explaining why ecosystem velocity does not equally inflate Phase 1 RD |
| AL02 | P3 TE > P1 TE (+3) | Medium | Scale-difference between phase TE definitions not surfaced in trajectory | Add cross-phase note explaining absolute-scale non-comparability |
| CP-02 | P2 TE = P1 TE (numeric) | Low | Scale difference makes this acceptable; "most variable" framing not reflected in TE floor | Confirm whether TE=4 is a cap or whether TE=5 was considered for highly variable customers |
| S1, S6 | P2 TE = P1 TE (numeric) | Low | Per-customer variation described as high but TE held flat | Add note confirming TE=2 is configuration-only, not code-change work |
| CP-08 | P2 TE = P1 TE (numeric); "simpler" framing not carried forward | Low | Phase 1 "simpler" framing not reconciled with non-trivial Phase 2 per-customer DR work | Clarify whether Phase 2 DR is templated (TE should drop) or bespoke (TE=3 is correct) |

---

## Key Findings

- **AL09 is the only subsegment in the dataset where Phase 3 RD strictly exceeds Phase 1 RD** (P1 RD=2, P3 RD=3). The source attributes this to AI ecosystem velocity (LangChain, LangGraph, MCP protocol evolution), but the same velocity argument should apply to Phase 1 if the initial build occurs against the same moving target [SOURCE-1, §6].

- **AL02 exhibits the largest cross-phase TE jump in the dataset** (P1 TE=1 to P3 TE=4, delta +3). This is a legitimate rating — Phase 1 requires near-zero business logic refactoring while Phase 3 captures the ISV's full ongoing product development FTE — but the trajectory is presentation-inconsistent and will mislead readers who compare numeric TE values across phases without consulting the phase-specific absolute scale definitions [SOURCE-1, §3, §7].

- **No subsegment has Phase 3 TE strictly below Phase 2 TE**, confirming that the file does not contain the most common type of rating contradiction (ongoing support rated lower than per-customer customization). The dataset passes this fundamental consistency check.

- **Five subsegments have Phase 2 TE numerically equal to Phase 1 TE** (CP-02, CP-08, S1, S6, and DS3 on TE only). All are explained by the phase-specific absolute scale difference: a TE score of 2 or 3 or 4 means categorically different absolute work volumes depending on the phase column it appears in. None constitute logical violations, but all require explanatory annotation to avoid reader misinterpretation [SOURCE-1, §3].

- **Phase 1 → Phase 3 trajectories are structurally sound for the three infrastructure-heavy planes** (P1 Control, P3 Data Plane, P4 AI Model). The Phase 2 dip and Phase 3 recovery pattern is most pronounced in the Data Plane (P3 avg TE: 3.0 → 1.4 → 2.9), which is correct given that self-hosted data services require per-customer capacity tuning but standardized architectures [SOURCE-1, §5, §6].

---

## Sources

| ID | File | Absolute Path |
|---|---|---|
| SOURCE-1 | three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| SOURCE-2 | GT5_cross_reference_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` |
| SOURCE-3 | G1_n_services_multiplier.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md` |
| SOURCE-4 | S1_four_plane_synthesis.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md` |
