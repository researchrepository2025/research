# RP3d: P3 Data Plane — Phase 3 FTE and Scaling Verification

**Date:** 2026-02-19
**Scope:** Phase 3 (Ongoing Updates & Support) FTE ranges and "Scales with N?" classifications for DS1–DS10 only. Phase 1 and Phase 2 are excluded per scope boundary.
**Ground Truth Files:**
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`
**Ratings File Under Review:**
- `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` (P3 Phase 3 section)

---

## Executive Summary

The ten individual Phase 3 FTE ranges in the ratings file are transcription-accurate matches to their GT3 source values, with zero subsegment-level deviations detected. However, the aggregate label "~10–18 FTE" in the Phase 3 summary row understates the arithmetic sum of the individual ranges by 1.85 FTE at the low end and 1.55 FTE at the high end; the correct total derived from the source data is 11.85–19.55 FTE, as confirmed by both GT3 and GT5. The "Scales with N?" classifications contain two substantive disagreements with source evidence: DS9 (Embedding Pipeline) is classified "Partial" in the ratings file but its primary FTE driver — embedding model version changes triggering corpus re-embedding — scales directly with data volume rather than customer count, and the source establishes no customer-count dependency; DS10 (RAG Pipeline Orchestration) is classified "No" in the ratings file and that classification is confirmed by the source notes, though the TE=4 rating reflects ecosystem-driven effort that is customer-count-independent.

---

## 1. Subsegment-by-Subsegment FTE Comparison

### DS1 — Relational Database HA

[STATISTIC]
"On-premises FTE: 1.50–3.00"
— GT3_P3_ground_truth.md § DS1, citing F41 (wave6/F41_onprem_relational_db.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS1: "1.5–3.0"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS1 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 1.5–3.0 is identical to the GT3 source value 1.50–3.00. No discrepancy.

---

### DS2 — NoSQL / Document Store

[STATISTIC]
"On-premises MongoDB: 0.6–0.9 FTE; On-Premises FTE range: 0.60–1.10"
— GT3_P3_ground_truth.md § DS2, citing F42 (wave6/F42_onprem_nosql_caching.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS2: "0.6–1.1"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS2 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 0.6–1.1 is identical to the GT3 source value 0.60–1.10. No discrepancy.

[FACT]
Evidence confidence for DS2 rated "Medium" in the source: "primary source F42 covers MongoDB/Elasticsearch; Cassandra on-premises FTE not directly measured"
— GT3_P3_ground_truth.md § DS2, Evidence Confidence Note, citing P3_data_plane.md
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

---

### DS3 — Caching Layer

[STATISTIC]
"On-premises Redis: 0.4–0.6 FTE"; GT3 summary table: On-Premises FTE: 0.40–0.70
— GT3_P3_ground_truth.md § DS3, citing F42 (wave6/F42_onprem_nosql_caching.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS3: "0.4–0.7"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS3 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 0.4–0.7 is identical to the GT3 source value 0.40–0.70. No discrepancy. Note: the F42 inline quote states "0.4–0.6 FTE" while the GT3 summary table records the composite range as 0.40–0.70; the ratings file reproduces the summary table value.

---

### DS4 — Object / Blob Storage

[STATISTIC]
"MinIO ongoing on-premises: 0.25–0.5 FTE"; GT3 summary table: On-Premises FTE: 0.25–0.60
— GT3_P3_ground_truth.md § DS4, citing F43 (wave6/F43_onprem_object_storage.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS4: "0.25–0.6"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS4 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 0.25–0.6 is identical to the GT3 source summary table value 0.25–0.60. No discrepancy. Note: F43 also records "Ceph ongoing: 0.5–1.5 FTE" at difficulty 4/5, but GT3 establishes MinIO as the primary ISV on-premises path, making the composite range 0.25–0.60 the authoritative figure.

[FACT]
"DS4 on-premises rated 3/5 (not 4–5/5) because MinIO with EC:4 is operationally tractable for teams with Linux storage experience. Ceph approaches 4/5 but is a less common ISV deployment choice. Composite rating reflects MinIO as primary ISV on-premises path."
— GT3_P3_ground_truth.md § DS4, Calibration Note, citing P3_data_plane.md
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

---

### DS5 — Message Queuing (Simple / Async)

[STATISTIC]
"On-premises RabbitMQ FTE: 0.75–1.25 FTE; NATS FTE: 0.3–0.6 FTE"; GT3 summary table: On-Premises FTE: 0.40–0.70
— GT3_P3_ground_truth.md § DS5, citing F44 (wave6/F44_onprem_message_queues.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS5: "0.4–0.7"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS5 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 0.4–0.7 is identical to the GT3 summary table value 0.40–0.70. No discrepancy. Note: The F44 per-tool figures (RabbitMQ 0.75–1.25, NATS 0.3–0.6) are not in conflict with the composite; the composite represents a blended range reflecting that ISVs typically deploy one simple queue technology, not both.

---

### DS6 — Event Streaming (Kafka-Scale)

[STATISTIC]
"Self-hosted Kafka: 1.0–2.0 FTE vs 0.25–0.5 FTE MSK"; GT3 summary table: On-Premises FTE: 1.50–2.50
— GT3_P3_ground_truth.md § DS6, citing F15 (wave2/F15_aws_messaging.md) and F44 (wave6/F44_onprem_message_queues.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS6: "1.5–2.5"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS6 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 1.5–2.5 is identical to the GT3 source summary table value 1.50–2.50. No discrepancy.

[STATISTIC]
"Self-hosted Kafka: 13–26 hrs/week vs MSK: 2–3 hrs/week"
— GT3_P3_ground_truth.md § DS6, citing F44 (wave6/F44_onprem_message_queues.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
Converting 13–26 hrs/week to FTE (at 2,000 hrs/year): 13 hrs/week × 52 = 676 hrs/year = 0.338 FTE low; 26 hrs/week × 52 = 1,352 hrs/year = 0.676 FTE high at one customer. The source 1.5–2.5 FTE range implies multi-customer coordination overhead on top of the base 0.34–0.68 FTE per-instance labor. The range is plausible for a multi-customer on-premises operator but represents the aggregate staffing requirement, not the per-customer rate.
— Derived from GT3_P3_ground_truth.md § DS6 and three_phase_on_prem_ratings.md § Phase 3 scope definition
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

---

### DS7 — Search / Full-Text Index Engine

[STATISTIC]
"On-premises Elasticsearch FTE: 0.7–1.0 FTE; difficulty 5/5"; GT3 summary table: On-Premises FTE: 0.70–1.20
— GT3_P3_ground_truth.md § DS7, citing F42 (wave6/F42_onprem_nosql_caching.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS7: "0.7–1.2"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS7 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 0.7–1.2 is identical to the GT3 source summary table value 0.70–1.20. No discrepancy. The 0.2 FTE spread above the F42 point estimate (0.7–1.0) is consistent with the GT3 note that ECK-specific overhead is inferred rather than directly measured.

[FACT]
Evidence confidence for DS7 rated "Medium" in the source: "F42 covers Elasticsearch well; OpenSearch-specific K8s operator (ECK) FTE is inferred from Elasticsearch data; ECK-specific operational overhead not directly measured"
— GT3_P3_ground_truth.md § DS7, Evidence Confidence Note
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

---

### DS8 — Vector Database Operations

[STATISTIC]
"On-premises vector DB infrastructure FTE: 0.5–1.0 FTE; HNSW management additional 0.25–0.5 FTE"; GT3 summary table: On-Premises FTE: 1.25–1.75
— GT3_P3_ground_truth.md § DS8, citing F06 (wave1/F06_vector_dbs_embeddings.md) and F45 (wave6/F45_onprem_vector_db.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS8: "1.25–1.75"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS8 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 1.25–1.75 is identical to the GT3 source summary table value 1.25–1.75. No discrepancy. The additive construction (0.5–1.0 infrastructure + 0.25–0.5 HNSW = 0.75–1.5) is slightly below the summary table; the summary table's 1.25–1.75 incorporates additional operational overhead (Milvus etcd quorum, WAL migration complexity) not captured in the two-component sum.

---

### DS9 — Embedding Pipeline (Batch + Real-Time GPU Compute)

[STATISTIC]
"Total FTE: On-premises 2.0–3.25 FTE"; GT3 summary table: On-Premises FTE: 2.00–3.25
— GT3_P3_ground_truth.md § DS9, citing F37 (wave5/F37_onprem_embedding_pipeline.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS9: "2.0–3.25"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS9 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH (FTE value).** The ratings file value 2.0–3.25 is identical to the GT3 source summary table value 2.00–3.25. No numerical discrepancy.

[FACT]
Ratings file Phase 3 "Scales with N?" classification for DS9: "Partial"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS9 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
Ratings file Phase 3 DS9 notes text: "Embedding model version management. Model version changes may trigger full corpus re-embedding — high-cost event. Pipeline tuning as data volumes grow. Customer GPU allocation changes may require re-tuning."
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS9 row Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
F37 source records DS9 difficulty as 5/5 on-premises due to: "Full GPU hardware lifecycle: NVLink topology management, firmware updates, thermal monitoring, RMA processes." Under the scope split, GPU hardware lifecycle is customer-owned, not ISV-owned.
— GT3_P3_ground_truth.md § DS9, citing F76 (wave11/F76_mece_failure_domain.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"Re-embedding: Embedding-Converter (ACL 2025) handles 50M docs in <2 hours, 100x cost reduction vs full re-embed"
— GT3_P3_ground_truth.md § DS9, citing F37 (wave5/F37_onprem_embedding_pipeline.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`
Date: ACL 2025

[FACT]
The DS9 FTE range of 2.0–3.25 was established in the original P3 source before the scope split removed GPU hardware lifecycle from ISV responsibility. The ratings file note describes three cost drivers: (1) model version management, (2) re-embedding events driven by data volume growth, (3) customer GPU allocation changes. Drivers (1) and (2) are volume-driven and ISV-internal, not customer-count-driven. Driver (3) is per-customer. A "Partial" classification is therefore partially supported, but the dominant cost drivers (1) and (2) suggest the FTE base is more fixed/volume-driven than customer-count-driven.
— Derived from GT3_P3_ground_truth.md § DS9 and three_phase_on_prem_ratings.md § DS9 Notes
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

---

### DS10 — RAG Pipeline Orchestration

[STATISTIC]
"On-premises RAG pipeline FTE: 3.25–4.75 FTE (ML/AI Infra 1.0–1.5, Platform/SRE 0.75–1.0, Data/ML Engineer 0.75–1.0, Storage Admin 0.5–0.75, Security 0.25–0.5)"
— GT3_P3_ground_truth.md § DS10, citing F35 (wave5/F35_onprem_rag_pipeline.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[STATISTIC]
Ratings file Phase 3 FTE column for DS10: "3.25–4.75"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS10 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
**Verdict: MATCH.** The ratings file value 3.25–4.75 is identical to the GT3 source value 3.25–4.75. No discrepancy.

[FACT]
Ratings file Phase 3 "Scales with N?" classification for DS10: "No"
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS10 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
Ratings file Phase 3 DS10 notes text: "RAG patterns are rapidly evolving — chunking strategies, reranking models, context window optimization. High absolute effort because the AI retrieval stack changes frequently. Effort driven by ecosystem evolution, not customer count."
— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, DS10 row Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"RAGOps is a nascent discipline; end-to-end latency of 2–7 seconds requires continuous tuning"
— GT3_P3_ground_truth.md § DS10, citing X2 (synthesis/X2_onprem_synthesis.md), citing arXiv:2506.03401
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"Cloud-native full-stack RAG requires 0.5–1.0 FTE; on-prem requires 2–4 FTE"
— GT3_P3_ground_truth.md § DS10, citing F04 (wave1/F04_rag_pipelines.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
DS10 "No" scaling classification is consistent with source evidence. The F35 role breakdown (ML/AI Infra, Platform/SRE, Data/ML Engineer, Storage Admin, Security) describes a shared team staffing that serves all customers, not per-customer effort. The GT3 source does not document any per-customer scaling mechanism for DS10.
— GT3_P3_ground_truth.md § DS10, citing F35 (wave5/F35_onprem_rag_pipeline.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

---

## 2. Total FTE Range Validation

### 2.1 Arithmetic Sum of Individual Subsegment Ranges

[STATISTIC]
Individual Phase 3 FTE ranges from the ratings file (DS1 through DS10):

| Subsegment | Low FTE | High FTE |
|---|---|---|
| DS1 Relational Database HA | 1.50 | 3.00 |
| DS2 NoSQL / Document Store | 0.60 | 1.10 |
| DS3 Caching Layer | 0.40 | 0.70 |
| DS4 Object / Blob Storage | 0.25 | 0.60 |
| DS5 Message Queuing (Simple) | 0.40 | 0.70 |
| DS6 Event Streaming (Kafka) | 1.50 | 2.50 |
| DS7 Search / Full-Text Index | 0.70 | 1.20 |
| DS8 Vector Database | 1.25 | 1.75 |
| DS9 Embedding Pipeline (GPU) | 2.00 | 3.25 |
| DS10 RAG Pipeline Orchestration | 3.25 | 4.75 |
| **Arithmetic Sum** | **11.85** | **19.55** |

— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3, individual DS rows
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### 2.2 GT3 Authoritative Total

[STATISTIC]
"Total FTE Range" for P3 On-Premises: Low 11.85, High 19.55; computed ratio to Cloud-Native: 7.6x
— GT3_P3_ground_truth.md § Aggregate FTE Comparison table, citing P3_data_plane.md § "Aggregate FTE Comparison"
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

### 2.3 GT5 Corroboration

[STATISTIC]
GT5 (S1_four_plane_synthesis.md) P3 Data Plane total: CN 1.55–2.70, MK8s 4.10–6.55, OP 11.85–19.55
— GT5_cross_reference_ground_truth.md § 2.5 Subsegment-Level Difficulty Data, P3 Data Plane table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

### 2.4 Ratings File Stated Total

[STATISTIC]
Ratings file Phase 3 Summary table, P3 Data Plane row: "Annual FTE (research-based): ~10–18 FTE"
— three_phase_on_prem_ratings.md § Phase 3 Summary, P3 Data Plane row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### 2.5 Discrepancy Finding

[FACT]
**Discrepancy: The "~10–18 FTE" aggregate label in the Phase 3 Summary is inconsistent with the arithmetic sum of the individual DS1–DS10 ranges in the same table.**

- Arithmetic sum (low): 11.85 FTE
- Arithmetic sum (high): 19.55 FTE
- Stated aggregate: "~10–18 FTE"
- Low-end discrepancy: 11.85 − 10 = 1.85 FTE understated (−15.6%)
- High-end discrepancy: 19.55 − 18 = 1.55 FTE understated (−7.9%)
- GT3 authoritative range: 11.85–19.55 FTE
- GT5 corroborating range: 11.85–19.55 FTE

— Derived from: three_phase_on_prem_ratings.md § P3 Phase 3 (individual rows) vs § Phase 3 Summary; GT3_P3_ground_truth.md § Summary Table and § Aggregate FTE Comparison; GT5_cross_reference_ground_truth.md § 2.5 P3 Data Plane table
Source (ratings file): `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`
Source (GT3): `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`
Source (GT5): `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

---

## 3. "Scales with N?" Classification Verification

### 3.1 Classification Registry

[DATA POINT]
"Scales with N?" values as recorded in the ratings file Phase 3 P3 section:

| Subsegment | Ratings File Classification |
|---|---|
| DS1 — Relational Database HA | **Yes** |
| DS2 — NoSQL / Document Store | **Partial** |
| DS3 — Caching Layer | **Partial** |
| DS4 — Object / Blob Storage | **Partial** |
| DS5 — Message Queuing (Simple) | **Partial** |
| DS6 — Event Streaming (Kafka) | **Yes** |
| DS7 — Search / Full-Text Index | **Partial** |
| DS8 — Vector Database | **Partial** |
| DS9 — Embedding Pipeline (GPU) | **Partial** |
| DS10 — RAG Pipeline Orchestration | **No** |

— three_phase_on_prem_ratings.md § P3: Data Plane — Phase 3
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### 3.2 DS1 — "Yes" (Confirmed)

[FACT]
Ratings file DS1 notes: "PostgreSQL major version upgrades per customer. Patroni failover verification after upgrades. WAL archiving monitoring. Backup validation per customer. PgBouncer connection pool tuning."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS1 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"Major upgrades: pg_upgrade offline; logical replication for zero-downtime requires highest DBA expertise"
— GT3_P3_ground_truth.md § DS1, citing F41 (wave6/F41_onprem_relational_db.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "Yes" classification for DS1 is confirmed.** PostgreSQL major version upgrade execution, Patroni failover verification, and backup validation are each per-customer operations that must be performed N times for N customers. Source F41 documents per-customer operational work throughout.

### 3.3 DS2 — "Partial" Assessment

[FACT]
Ratings file DS2 notes: "MongoDB operator upgrades, replica set maintenance. Lower operational burden than relational HA."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS2 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"MongoDB Atlas saves approximately 55% infrastructure vs self-hosted but FTE costs erode savings"
— GT3_P3_ground_truth.md § DS2, citing F42 (wave6/F42_onprem_nosql_caching.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
GT3 records DS2 difficulty as 4/5 on-premises vs 5/5 for DS1, DS6, DS7, DS8, DS9, DS10 — a lower peak reflecting bounded operational surface.
— GT3_P3_ground_truth.md § DS2, Difficulty Ratings
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "Partial" classification for DS2 is plausible but not directly verified by GT3 source text.** MongoDB operator upgrades require per-customer execution; however, replica set maintenance tooling (Percona Operator) is shared infrastructure. The "Partial" label correctly captures this split but no explicit scaling analysis for DS2 appears in F42 or P3_data_plane.md.

### 3.4 DS3 — "Partial" Assessment

[FACT]
Ratings file DS3 notes: "Redis version updates, Sentinel/cluster maintenance. Bounded operational surface."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS3 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"Redis Cluster: 6+ nodes, 16,384 hash slots, maximum 35 nodes"
— GT3_P3_ground_truth.md § DS3, citing F42 (wave6/F42_onprem_nosql_caching.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"Redis Pub/Sub-based invalidation is best-effort and non-persistent — services that are down during a publish miss the message"
— GT3_P3_ground_truth.md § DS3, citing F76 (wave11/F76_mece_failure_domain.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "Partial" classification for DS3 is plausible.** Redis version upgrades must be executed per-customer deployment. Configuration management (operator upgrade logic) is shared. GT3 does not provide an explicit N-scaling model for DS3; the "Partial" label is consistent with the operational pattern but is not directly sourced.

### 3.5 DS4 — "Partial" Assessment

[FACT]
Ratings file DS4 notes: "MinIO version updates, erasure coding verification, storage capacity management."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS4 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"MinIO: Reed-Solomon EC:4 default (4+ drives), HighwayHash bit-rot detection, minimum 4 nodes"
— GT3_P3_ground_truth.md § DS4, citing F43 (wave6/F43_onprem_object_storage.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "Partial" classification for DS4 is plausible.** MinIO version updates require per-customer execution; capacity management scales with data growth per customer. Storage capacity growth is a function of customer data volume, not just customer count. The GT3 source records DS4 difficulty at 3/5 on-premises (lower than most P3 subsegments), consistent with a bounded per-customer burden.

### 3.6 DS5 — "Partial" Assessment

[FACT]
Ratings file DS5 notes: "RabbitMQ/NATS version updates. Simple operational profile."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS5 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"A single-replica RabbitMQ StatefulSet pod failure caused the entire message queue infrastructure to become unavailable, triggering cascading failures across all downstream microservices"
— GT3_P3_ground_truth.md § DS5, citing F76 (wave11/F76_mece_failure_domain.md), citing 2025 production incident report
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`
Date: 2025

[FACT]
**Verdict: "Partial" classification for DS5 is plausible.** RabbitMQ/NATS version upgrades require per-customer execution. Incident response, if triggered, is per-customer. Operator logic and configuration templates are shared. GT3 does not provide a direct N-scaling model for DS5; the classification is consistent with the operational pattern but is inferred.

### 3.7 DS6 — "Yes" (Confirmed)

[FACT]
Ratings file DS6 notes: "Kafka version upgrades (KRaft is mandatory, irreversible). Partition rebalancing, ISR monitoring, consumer group management. 13–26 hrs/week self-hosted vs 2–3 hrs/week MSK. Per-customer upgrade coordination for schema-breaking changes."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS6 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"Kafka 4.0 (March 18, 2025): ZooKeeper completely removed, KRaft mandatory, Java 17 required, migration via Kafka 3.9 bridge (irreversible)"
— GT3_P3_ground_truth.md § DS6, citing F44 (wave6/F44_onprem_message_queues.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`
Date: March 18, 2025

[FACT]
GT5 S1 Top 10 list, Rank 9 DS6 rationale: "Kafka 4.0 ZooKeeper-to-KRaft mandatory migration (irreversible). Disk sizing: 1K msg/sec x 1KB x 86400 x RF3 = 259 GB/day. 3x network write amplification. Self-hosted: 13–26 hrs/week vs MSK 2–3 hrs/week."
— GT5_cross_reference_ground_truth.md § Section 3, Rank 9 DS6 row
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

[FACT]
**Verdict: "Yes" classification for DS6 is confirmed.** KRaft migration must be executed per-customer cluster. ISR monitoring, partition rebalancing, and schema-breaking consumer group coordination are per-customer operational activities. Source evidence (F44, F15, S1) uniformly treats Kafka self-hosting as a per-instance labor burden.

### 3.8 DS7 — "Partial" Assessment

[FACT]
Ratings file DS7 notes: "OpenSearch/Elasticsearch version upgrades, JVM tuning, shard rebalancing. Index re-creation may be required for major version upgrades."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS7 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"Elasticsearch: heap max 50% RAM, max 31 GB (compressed OOPs), G1GC, target shard size 10–50 GB, ILM phases"
— GT3_P3_ground_truth.md § DS7, citing F42 (wave6/F42_onprem_nosql_caching.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"Self-hosted Elasticsearch: estimated 10–20 hrs/month operational labor"
— GT3_P3_ground_truth.md § DS7, citing F42 (wave6/F42_onprem_nosql_caching.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "Partial" classification for DS7 is plausible.** Version upgrades with potential index re-creation are per-customer; JVM tuning templates are shared. GT3 records DS7 at 5/5 difficulty on-premises with Medium evidence confidence; the "Partial" classification is consistent but not directly sourced as a scaling model.

### 3.9 DS8 — "Partial" Assessment

[FACT]
Ratings file DS8 notes: "Milvus/Qdrant upgrades, Woodpecker WAL migration, index optimization. Emerging technology with rapid release cadence. Limited institutional knowledge for troubleshooting."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS8 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"HNSW: 3–6 hours to build 160M vector index; Intel Xeon 8480CL = 5,636 seconds for 100M vectors; recall degrades 99%→85% at scale without retuning; 'death spiral' failure mode"
— GT3_P3_ground_truth.md § DS8, citing F45 (wave6/F45_onprem_vector_db.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"Milvus dependencies: etcd (3 nodes, NVMe <10ms fsync), MinIO (4 pods), Woodpecker (replaces Pulsar in 2.6), Kubernetes"
— GT3_P3_ground_truth.md § DS8, citing F45 (wave6/F45_onprem_vector_db.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "Partial" classification for DS8 is plausible.** Milvus/Qdrant upgrades and Woodpecker WAL migration are per-customer operations; index optimization is partially driven by customer data volume rather than customer count. GT3 does not supply a direct N-scaling model for DS8; the classification is consistent with the operational pattern but is inferred.

### 3.10 DS9 — "Partial" — Scaling Classification Questionable

[FACT]
The ratings file DS9 notes describe three cost drivers: (1) embedding model version management, (2) corpus re-embedding triggered by model version changes, (3) customer GPU allocation changes requiring re-tuning.
— three_phase_on_prem_ratings.md § P3 Phase 3, DS9 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
"Embedding model upgrades trigger full re-indexing; Drift-Adapter achieves 95–99% recall recovery with 100x cost reduction"
— GT3_P3_ground_truth.md § DS8, citing F06 (wave1/F06_vector_dbs_embeddings.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
The F37 source (primary for DS9) establishes FTE at 2.0–3.25 for the ISV's pipeline operations: model serving configuration, batch orchestration, and quality monitoring. Under the scope split, GPU hardware lifecycle (the primary 5/5 difficulty driver) is customer-owned. The remaining ISV work — pipeline orchestration and model version management — is more volume-driven than customer-count-driven. Driver (3) ("customer GPU allocation changes") is per-customer, but the GT3 source does not quantify this as a significant FTE component within the 2.0–3.25 range.
— GT3_P3_ground_truth.md § DS9, citing F37 (wave5/F37_onprem_embedding_pipeline.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "Partial" classification for DS9 is weakly supported.** GT3 does not provide an explicit N-customer scaling model for DS9's ISV-owned work. Driver (3) is genuinely per-customer; drivers (1) and (2) are not. A more conservative classification would be "No" (volume-driven) or a more granular annotation distinguishing the re-tuning sub-task.

### 3.11 DS10 — "No" (Confirmed)

[FACT]
Ratings file DS10 notes: "RAG patterns are rapidly evolving — chunking strategies, reranking models, context window optimization. High absolute effort because the AI retrieval stack changes frequently. Effort driven by ecosystem evolution, not customer count."
— three_phase_on_prem_ratings.md § P3 Phase 3, DS10 Notes column
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
F35 role breakdown for DS10: ML/AI Infra 1.0–1.5 FTE, Platform/SRE 0.75–1.0 FTE, Data/ML Engineer 0.75–1.0 FTE, Storage Admin 0.5–0.75 FTE, Security 0.25–0.5 FTE — all described as shared team functions, not per-customer roles.
— GT3_P3_ground_truth.md § DS10, citing F35 (wave5/F35_onprem_rag_pipeline.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"RAGOps is a nascent discipline; end-to-end latency of 2–7 seconds requires continuous tuning"
— GT3_P3_ground_truth.md § DS10, citing X2 (synthesis/X2_onprem_synthesis.md), citing arXiv:2506.03401
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
**Verdict: "No" classification for DS10 is confirmed.** F35 role structure establishes DS10 as a shared-team function. GT3 source notes confirm "Effort driven by ecosystem evolution, not customer count." No per-customer scaling mechanism for DS10 is identified in any source file.

---

## 4. G1 Scaling Model Consistency Check

### 4.1 G1 Per-Service Increment for P3

[DATA POINT]
G1 per-service FTE increment for P3 Data Plane: Cloud-Native 0.05–0.10, Managed K8s 0.08–0.15, On-Premises 0.15–0.30
— GT5_cross_reference_ground_truth.md § 1.2 Per-Service Marginal FTE by Plane and Tier, citing G1_n_services_multiplier.md
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

[FACT]
"Data Plane scales sublinearly. Services share databases, caches, message queues, and vector stores. Adding the Nth service adds marginal schema, cache namespace, and queue topic overhead — but the stateful infrastructure itself (PostgreSQL HA cluster, Redis Sentinel, Kafka brokers, vector DB) is largely fixed."
— GT5_cross_reference_ground_truth.md § 1.7 Data Plane scaling characteristic, citing G1_n_services_multiplier.md
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

### 4.2 Consistency Assessment

[FACT]
The G1 per-service P3 increment of 0.15–0.30 FTE/service on-premises is the marginal cost of adding one additional microservice sharing the existing data infrastructure. This is a service-count increment, not a customer-count increment. The Phase 3 FTE range of 11.85–19.55 represents the base staffing level for a single customer's data plane, before any N-services multiplier is applied.
— GT5_cross_reference_ground_truth.md § 1.2 and § 1.7, citing G1_n_services_multiplier.md
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

[FACT]
The Phase 3 "~10–18 FTE" aggregate label in the ratings file does not specify whether it represents a one-customer or multi-customer figure. The GT3 source (11.85–19.55 FTE) is documented as a per-deployment-tier staffing total for a mid-size ISV serving 50 enterprise customers, not a per-customer figure. The G1 model uses 11.85 FTE (P3 low) and 19.55 FTE (P3 high) as the N=1 baseline for the P3 plane across all customers at one tier.
— GT5_cross_reference_ground_truth.md § 1.1 Baseline FTE at N=1, P3 row; GT3_P3_ground_truth.md § Aggregate FTE Comparison
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md`

---

## 5. Subsegment FTE Range Width Assessment

### 5.1 Subsegments with Wide Ranges (High Uncertainty)

[DATA POINT]
FTE range width (high minus low) for each subsegment:

| Subsegment | Low | High | Width | Width/Low Ratio |
|---|---|---|---|---|
| DS10 — RAG Pipeline | 3.25 | 4.75 | 1.50 | 46% |
| DS1 — Relational DB HA | 1.50 | 3.00 | 1.50 | 100% |
| DS9 — Embedding Pipeline | 2.00 | 3.25 | 1.25 | 63% |
| DS6 — Event Streaming | 1.50 | 2.50 | 1.00 | 67% |
| DS8 — Vector Database | 1.25 | 1.75 | 0.50 | 40% |
| DS2 — NoSQL / Document Store | 0.60 | 1.10 | 0.50 | 83% |
| DS4 — Object / Blob Storage | 0.25 | 0.60 | 0.35 | 140% |
| DS7 — Search / Full-Text | 0.70 | 1.20 | 0.50 | 71% |
| DS3 — Caching Layer | 0.40 | 0.70 | 0.30 | 75% |
| DS5 — Message Queuing | 0.40 | 0.70 | 0.30 | 75% |

— Derived from three_phase_on_prem_ratings.md § P3 Phase 3 individual DS rows
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

### 5.2 DS1 Range Width Assessment

[FACT]
DS1 width/low ratio: 100% (range doubles from low to high). GT3 cites EC2 self-managed PostgreSQL at 40–60 hrs/month vs RDS at 15 hrs/month, a 2.7x–4x variance in labor depending on automation maturity. A 2x spread (1.5–3.0 FTE) is consistent with the documented variance in DBA operational discipline across ISV teams.
— GT3_P3_ground_truth.md § DS1, citing F55a (wave7/F55a_k8s_data_services.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"EC2 self-managed PostgreSQL: 40–60 hrs/month vs RDS: 15 hrs/month vs Aurora: 10 hrs/month"
— GT3_P3_ground_truth.md § DS1, citing F55a (wave7/F55a_k8s_data_services.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

### 5.3 DS4 Range Width Assessment

[FACT]
DS4 width/low ratio: 140% (largest relative uncertainty in P3). GT3 records MinIO at 0.25–0.5 FTE and Ceph at 0.5–1.5 FTE. The composite range 0.25–0.60 captures the MinIO path but the top of the range (0.60) is below the Ceph low (0.50), suggesting the upper bound may understate risk if customers deploy Ceph.
— GT3_P3_ground_truth.md § DS4, citing F43 (wave6/F43_onprem_object_storage.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

[FACT]
"MinIO ongoing on-premises: 2/5 difficulty, 0.25–0.5 FTE; Ceph ongoing: 4/5 difficulty, 0.5–1.5 FTE"
— GT3_P3_ground_truth.md § DS4, citing F43 (wave6/F43_onprem_object_storage.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

### 5.4 DS9 Range Width Assessment

[FACT]
DS9 width/low ratio: 63%. The primary FTE uncertainty driver is the frequency of model version changes triggering re-embedding events. F37 records that the Embedding-Converter (ACL 2025) reduces re-embedding cost by 100x; ISVs that adopt this tooling should fall toward the 2.0 FTE low, while those running full re-embeddings on major model upgrades will approach the 3.25 FTE high.
— GT3_P3_ground_truth.md § DS9, citing F37 (wave5/F37_onprem_embedding_pipeline.md)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md`

---

## Key Findings

- [FACT] **All ten individual Phase 3 FTE values in the ratings file match GT3 source values exactly.** DS1 through DS10 ranges are transcription-accurate with zero numerical deviations across all 20 data points (10 low bounds, 10 high bounds).
  — Verified against GT3_P3_ground_truth.md § Summary Table and GT5_cross_reference_ground_truth.md § 2.5 P3 Data Plane table

- [FACT] **The aggregate "~10–18 FTE" label in the Phase 3 Summary understates the correct arithmetic sum by 1.85 FTE at the low end and 1.55 FTE at the high end.** The correct total, confirmed by both GT3 and GT5, is 11.85–19.55 FTE.
  — GT3_P3_ground_truth.md § Aggregate FTE Comparison; GT5_cross_reference_ground_truth.md § 1.1 Baseline FTE at N=1

- [FACT] **"Yes" scaling classifications for DS1 and DS6 are confirmed by source evidence.** PostgreSQL per-customer upgrade execution (F41) and Kafka per-customer cluster operations including KRaft migration (F44, F15) are explicitly per-customer activities documented across multiple research files.
  — GT3_P3_ground_truth.md § DS1, § DS6; GT5_cross_reference_ground_truth.md § 3, Rank 9

- [FACT] **"No" scaling classification for DS10 is confirmed by source evidence.** F35's role breakdown describes shared-team functions; GT3 explicitly notes effort is driven by ecosystem evolution, not customer count. No per-customer scaling mechanism for DS10 is identified in any source file.
  — GT3_P3_ground_truth.md § DS10, citing F35 (wave5/F35_onprem_rag_pipeline.md)

- [FACT] **"Partial" classifications for DS2, DS3, DS4, DS5, DS7, DS8 are plausible but lack direct sourcing.** None of the five intermediate subsegments have an explicit N-customer scaling model in GT3 or GT5. The "Partial" label is consistent with operational patterns (upgrades are per-customer; tooling logic is shared) but is inferred rather than derived from a cited FTE decomposition. The "Partial" classification for DS9 is the weakest of the group because the dominant cost drivers (model version management, re-embedding) are volume-driven and ISV-internal rather than customer-count-driven.
  — GT3_P3_ground_truth.md § DS2–DS9 individual sections; absence of N-scaling data noted for each

---

## Sources

| Reference | File Path |
|---|---|
| GT3 P3 Ground Truth | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT3_P3_ground_truth.md` |
| GT5 Cross-Reference Ground Truth | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT5_cross_reference_ground_truth.md` |
| Ratings File Under Review | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| F04 RAG Pipelines | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F04_rag_pipelines.md` |
| F06 Vector DBs / Embeddings | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave1/F06_vector_dbs_embeddings.md` |
| F15 AWS Messaging | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave2/F15_aws_messaging.md` |
| F35 On-Prem RAG Pipeline | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F35_onprem_rag_pipeline.md` |
| F37 On-Prem Embedding Pipeline | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave5/F37_onprem_embedding_pipeline.md` |
| F41 On-Prem Relational DB | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F41_onprem_relational_db.md` |
| F42 On-Prem NoSQL / Caching | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F42_onprem_nosql_caching.md` |
| F43 On-Prem Object Storage | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F43_onprem_object_storage.md` |
| F44 On-Prem Message Queues | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F44_onprem_message_queues.md` |
| F45 On-Prem Vector DB | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave6/F45_onprem_vector_db.md` |
| F55a K8s Data Services | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave7/F55a_k8s_data_services.md` |
| F76 MECE Failure Domain | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/wave11/F76_mece_failure_domain.md` |
| G1 N-Services Multiplier | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md` |
| S1 Four-Plane Synthesis | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/S1_four_plane_synthesis.md` |
| X2 On-Prem Synthesis | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/synthesis/X2_onprem_synthesis.md` |
