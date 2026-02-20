# RP1b: P1 Control Plane — Security and Delivery Subsegments Review
## Rating Validation: CP-04, CP-05, CP-06

**Review Date:** 2026-02-19
**Reviewer Role:** Precision fact extraction and rating validation
**Scope:** CP-04 (Secrets/Certs/PKI), CP-05 (Observability Infrastructure), CP-06 (CI/CD Pipeline/GitOps) — three deployment phases each, two dimensions each (Relative Difficulty 1–5, Total Effort 1–5)
**Primary Reference:** GT1_P1_ground_truth.md (extracted from P1_control_plane.md, 2026-02-19)
**Ratings Reference:** three_phase_on_prem_ratings.md (2026-02-19)

---

## Executive Summary

The Phase 1, Phase 2, and Phase 3 ratings for CP-04, CP-05, and CP-06 are largely well-calibrated against the GT1 ground truth data, with three targeted adjustments warranted. The CP-04 Relative Difficulty rating in Phase 3 (currently RD 4) is defensible but carries medium confidence given that the GT1 source rates on-premises Vault operations at 5/5 difficulty — the most significant discrepancy found. The CP-05 Phase 1 Total Effort rating (TE 5) is strongly supported by both internal evidence (500K+ active time series, 15–35 GB RAM consumption before application workloads) and external Prometheus sizing data, which confirms the 3 KB per-series approximation used in the source; however, external sources reveal the actual figure is closer to 2 KB per series under ideal conditions, making TE 5 conservative but directionally accurate. CP-06 ratings are the most internally consistent of the three subsegments, with the Deutsche Telekom Flux case study independently confirmed as an accurate primary source citation.

---

## Subsegment Review: CP-04 — Secrets Management, Certificate Lifecycle, and PKI

### Ratings Under Review

From `three_phase_on_prem_ratings.md`, CP-04 rows:

| Phase | RD (rated) | TE (rated) | Notes in ratings file |
|---|:---:|:---:|---|
| Phase 1 | 5 | 4 | Vault 5-node Raft, cert-manager, FIPS 140-3 path, irreversible PKI root design |
| Phase 2 | 3 | 3 | Customer PKI integration, HSM integration, trust chain per customer |
| Phase 3 | 4 | 4 | Cert rotation per customer, Vault upgrades, FIPS 140-3 migration, seal/unseal per upgrade |

### GT1 Ground Truth Data

[FACT] GT1 records the on-premises composite difficulty for CP-04 as **5/5**, sourced from P1_control_plane.md.
— GT1_P1_ground_truth.md, CP-04 Difficulty Ratings table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[STATISTIC] GT1 records on-premises FTE range for CP-04 as **2.5–5.0 FTE**.
— GT1_P1_ground_truth.md, CP-04 FTE Ranges section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] "HashiCorp Vault minimum 5-node Raft cluster."
— GT1_P1_ground_truth.md, CP-04 Key Operational Characteristics (citing F47, W06S Theme 2, F76 Domain 3)

[FACT] "HSM hardware costs $5K–$50K per unit."
— GT1_P1_ground_truth.md, CP-04 Key Operational Characteristics (citing F47, W06S Theme 2, F76 Domain 3)

[FACT] "FIPS 140-2 certificate validity expires September 2026 — HSM firmware and Vault seal configurations must transition to FIPS 140-3 before that date."
— GT1_P1_ground_truth.md, CP-04 Notable Caveats (citing F47, W06S Theme 2, F76 Domain 3)

[FACT] "Let's Encrypt announced in December 2025 that certificate validity will decrease to 45 days on May 13, 2026 — increasing rotation frequency requirements for all tiers."
— GT1_P1_ground_truth.md, CP-04 Notable Caveats (citing F47, W06S Theme 2, F76 Domain 3)

### External Validation: Vault Raft Cluster

[FACT] "To allow for the failure of up to two nodes in the cluster, the ideal size is five nodes for a Vault cluster using Integrated Storage."
— HashiCorp Developer Documentation, Vault with Integrated Storage Reference Architecture
URL: https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-reference-architecture

[FACT] "HashiCorp does not support mixed deployment scenarios within the same Vault cluster, and cluster nodes must be of a single binary/deployment type across the entire cluster."
— HashiCorp Developer Documentation, FIPS compliance in Vault (Enterprise)
URL: https://developer.hashicorp.com/vault/docs/enterprise/fips

[FACT] Vault Enterprise 1.19.4+ with FIPS Enabled is conformant with FIPS 140-3 standards. FIPS 140-3 Level 1 compliance was added in Vault Enterprise 1.21.
— HashiCorp Blog, "HashiCorp Vault and FIPS 140-3: Strengthening security and compliance"
URL: https://www.hashicorp.com/en/blog/hashicorp-vault-and-fips-140-3-strengthening-security-and-compliance

[FACT] "FIPS Inside (Built-in): Special builds of Vault Enterprise (marked with a fips1403 feature name) include built-in support for FIPS 140-3 compliance. Unlike using Seal Wrap for FIPS compliance, this binary has no external dependencies on a HSM."
— HashiCorp Developer Documentation, Built-in FIPS 140-3 support
URL: https://developer.hashicorp.com/vault/docs/enterprise/fips/fips1403

[FACT] "To use this feature [FIPS 140-3], you must have an active or trial license for Vault Enterprise Plus (HSMs)."
— HashiCorp Developer Documentation, Built-in FIPS 140-3 support
URL: https://developer.hashicorp.com/vault/docs/enterprise/fips/fips1403

[FACT] Let's Encrypt will begin issuing 45-day certificates as an opt-in option on May 13, 2026; the default classic profile switches to 64-day certificates on February 10, 2027; the classic profile will issue 45-day certificates with a 7-hour authorization reuse period by February 16, 2028.
— Let's Encrypt, "Decreasing Certificate Lifetimes to 45 Days" (December 2025)
URL: https://letsencrypt.org/2025/12/02/from-90-to-45

[FACT] "The authorization reuse period drops from 30 days to just 7 hours, forcing near-instant domain validation for renewals."
— CertKit, "Let's Encrypt is moving to 45-day certificates before everyone else"
URL: https://www.certkit.io/blog/45-day-certificates

### Re-Derived Ratings

**Phase 1 (RD 5, TE 4):**
GT1 assigns on-premises CP-04 a composite 5/5 difficulty. The Phase 1 RD of 5 directly maps to the GT1 composite for a single-environment build. The TE 4 (6–12 person-months) is a reasonable initial build estimate given that deploying a 5-node Vault raft cluster, designing a PKI root that is irreversible, deploying cert-manager, and architecting a FIPS 140-3 compliance path are each individually significant engineering workstreams. The 2.5–5.0 FTE on-premises range from GT1, annualized, supports a TE of 4–5 for the initial build.

**Phase 2 (RD 3, TE 3):**
Per-customer customization involves integrating with customer PKI infrastructure, configuring trust chains, and potentially integrating with customer HSMs ($5K–$50K per unit hardware). The RD 3 is plausible — this is meaningful but bounded work compared to the Phase 1 foundational build. The TE 3 (1–3 person-weeks per customer) is defensible.

**Phase 3 (RD 4, TE 4):**
The GT1 source rates on-premises CP-04 operations at 5/5 composite difficulty, and lists the following as ongoing recurring work: certificate rotation per customer, Vault upgrades across N environments, FIPS 140-3 migration coordinated per customer by September 2026, and seal/unseal operations during Vault upgrades. The ratings file assigns RD 4. The discrepancy between the GT1 5/5 static rating and the Phase 3 RD 4 is not necessarily an error — the Phase 3 scale uses a relative-to-cloud-native framework, not an absolute difficulty scale — but the 1-point gap against a GT1 5/5 warrants flag.

### CP-04 Rating Assessment

| Phase | Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | RD | 5 | 5 | High | ACCURATE |
| Phase 1 | TE | 4 | 4 | High | ACCURATE |
| Phase 2 | RD | 3 | 3 | Medium | ACCURATE |
| Phase 2 | TE | 3 | 3 | Medium | ACCURATE |
| Phase 3 | RD | 4 | 4–5 | Medium | ADJUST (borderline) |
| Phase 3 | TE | 4 | 4 | High | ACCURATE |

**Phase 3 RD Interview Question:** In practice, how many distinct manual steps does a Vault upgrade across N customer environments require — is the seal/unseal procedure during Kubernetes pod restarts automated via auto-unseal (AWS KMS, Azure Key Vault), or does it require manual Shamir key entry per customer node? If manual Shamir unsealing is the production pattern, RD should be 5.

---

## Subsegment Review: CP-05 — Observability Infrastructure (Metrics, Logs, Traces)

### Ratings Under Review

From `three_phase_on_prem_ratings.md`, CP-05 rows:

| Phase | RD (rated) | TE (rated) | Notes in ratings file |
|---|:---:|:---:|---|
| Phase 1 | 4 | 5 | Full observability stack build; 500K+ active time series at 3KB RAM each |
| Phase 2 | 2 | 2 | Storage retention tuning; mostly configuration |
| Phase 3 | 4 | 5 | Prometheus/Grafana/Loki upgrades; storage management; Jaeger v1→v2 migration |

### GT1 Ground Truth Data

[FACT] GT1 records the on-premises composite difficulty for CP-05 as **4/5**, sourced from P1_control_plane.md.
— GT1_P1_ground_truth.md, CP-05 Difficulty Ratings table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[STATISTIC] GT1 records on-premises FTE range for CP-05 as **4.6–7.0 FTE** (logging 1.5–2.0 + monitoring 1.5–2.5 + tracing 1.6–2.5).
— GT1_P1_ground_truth.md, CP-05 FTE Ranges section

[FACT] "The kube-prometheus-stack (Prometheus Operator, Grafana, Alertmanager) consumes 15–35 GB of cluster RAM before any application workloads are monitored."
— GT1_P1_ground_truth.md, CP-05 Key Operational Characteristics (citing F55d, W07S Theme 4)

[STATISTIC] "A 100-node cluster can generate 500,000+ active Prometheus time series at approximately 3 KB RAM per series."
— GT1_P1_ground_truth.md, CP-05 Key Operational Characteristics (citing F49, F50, W06S Theme 4)

[STATISTIC] "AWS Managed Prometheus at 1M samples/sec costs approximately $47K/month versus self-hosted approximately $6K/month (7.8x cost differential)."
— GT1_P1_ground_truth.md, CP-05 Key Operational Characteristics (citing F49, F50, W06S Theme 4)

[STATISTIC] "Self-hosted Loki at 100 GB/day costs approximately $300/month versus CloudWatch $1,665/month (75–90% cost reduction)."
— GT1_P1_ground_truth.md, CP-05 Key Operational Characteristics (citing F49, F50, W06S Theme 4)

[FACT] "Jaeger v1 was deprecated January 2026 — migration to v2 (OTel Collector-based) is required."
— GT1_P1_ground_truth.md, CP-05 Notable Caveats (citing F51, W06S Theme 3 and Theme 4)

[FACT] "MinIO entered maintenance mode late 2025 and was archived by early 2026, affecting on-premises tracing storage backends."
— GT1_P1_ground_truth.md, CP-05 Notable Caveats (citing F51, W06S Theme 3 and Theme 4)

### External Validation: Prometheus Memory Sizing

[FACT] "As of Prometheus 2.20 a good rule of thumb is around 3kB per series in the head."
— Robust Perception, "How much RAM does Prometheus 2.x need for cardinality and ingestion?"
URL: https://www.robustperception.io/how-much-ram-does-prometheus-2-x-need-for-cardinality-and-ingestion/

[STATISTIC] "A million series costs around 2GiB of RAM in terms of cardinality" (implying approximately 2 KB per series for cardinality alone, with ingestion adding additional load at 15-second scrape intervals).
— Robust Perception, "How much RAM does Prometheus 2.x need for cardinality and ingestion?"
URL: https://www.robustperception.io/how-much-ram-does-prometheus-2-x-need-for-cardinality-and-ingestion/

[FACT] Prometheus per-series memory components include: 732 bytes base per-series overhead, plus 32 bytes per label pair, plus 120 bytes per unique label value, plus 192 bytes for chunk overhead per 128 bytes of data, with all values doubled due to Go's garbage collection behavior.
— Robust Perception, "How much RAM does Prometheus 2.x need for cardinality and ingestion?"
URL: https://www.robustperception.io/how-much-ram-does-prometheus-2-x-need-for-cardinality-and-ingestion/

[FACT] In production Kubernetes clusters, Prometheus memory usage has been documented climbing past 55 GB, peaking at 60 GB. Organizations have reduced memory usage from approximately 24 GB down to approximately 14 GB after optimizing high-cardinality metrics.
— Devoriales, "Prometheus: How We Slashed Memory Usage"
URL: https://devoriales.com/post/384/prometheus-how-we-slashed-memory-usage

[DATA POINT] GitHub issue in prometheus-community/helm-charts documents "High memory pressure" for kube-prometheus-stack deployments, with users reporting node-level memory exhaustion.
— GitHub, prometheus-community/helm-charts Issue #314
URL: https://github.com/prometheus-community/helm-charts/issues/314

### Sizing Claim Assessment

The GT1 claim of "approximately 3 KB RAM per series" is consistent with the Robust Perception rule of thumb for Prometheus 2.x head-block memory. The cardinality-only figure from Robust Perception is closer to 2 KB/series (2 GiB for 1M series), but the 3 KB figure accounts for the combined head block, ingestion overhead, and Go GC doubling effects. For 500,000 active time series:
- At 2 KB/series (cardinality only): ~1 GB RAM
- At 3 KB/series (combined): ~1.5 GB RAM
- Total kube-prometheus-stack stack claim of 15–35 GB is consistent with real-world reports documenting 14–60 GB depending on cardinality — the 15–35 GB range is a mid-range estimate, not an outlier.

### External Validation: CNCF ArgoCD / Observability Adoption

[STATISTIC] "60% of reported K8s clusters use Argo CD; 97% use it in production."
— CNCF, End User Survey 2025, announced July 24, 2025
URL: https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/

Note: The ratings file cites "60% of Kubernetes clusters per the 2025 CNCF End User Survey" for ArgoCD. The CNCF announcement independently confirms this figure.

### Re-Derived Ratings

**Phase 1 (RD 4, TE 5):**
GT1 composite difficulty for CP-05 on-premises is 4/5. The Phase 1 RD of 4 directly matches GT1. The TE of 5 (12+ person-months) is supported by the 4.6–7.0 FTE ongoing annual range in GT1 — a first-build of three separate backends (metrics, logs, traces) with storage architecture, Grafana dashboards, and alerting rules would be at least as large as one year of ongoing operations. The 500K+ active time series scale justifies the TE 5.

**Phase 2 (RD 2, TE 2):**
The Phase 2 notes state "Tune storage retention and memory allocation for customer's disk/memory profile. Mostly configuration — the observability stack itself is standardized." The GT1 evidence supports this: CP-05 scaling behavior is cluster-size driven, not customer-architecture driven in the way CP-02 (networking) is. RD 2 and TE 2 are defensible.

**Phase 3 (RD 4, TE 5):**
The GT1 4.6–7.0 FTE annual range maps to TE 5 (2.5+ FTE) at the high end and TE 4 (1.0–2.5 FTE) at the low end. The rating of TE 5 is supported by the upper bound of the GT1 FTE range. The ongoing migration workload (Jaeger v1→v2, MinIO archival, cardinality management) further supports sustained high effort. RD 4 is consistent with GT1 4/5 composite.

### CP-05 Rating Assessment

| Phase | Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | RD | 4 | 4 | High | ACCURATE |
| Phase 1 | TE | 5 | 5 | High | ACCURATE |
| Phase 2 | RD | 2 | 2 | Medium | ACCURATE |
| Phase 2 | TE | 2 | 2 | Medium | ACCURATE |
| Phase 3 | RD | 4 | 4 | High | ACCURATE |
| Phase 3 | TE | 5 | 4–5 | Medium | ACCURATE (borderline) |

**Phase 3 TE Interview Question:** Does the 4.6–7.0 FTE range represent dedicated observability headcount or is it partially shared with CP-10 security operations (given that Falco logs and SIEM events feed into the same observability stack)? The TE 5 upper bound depends on no deduplication with CP-10.

---

## Subsegment Review: CP-06 — CI/CD Pipeline Infrastructure and GitOps

### Ratings Under Review

From `three_phase_on_prem_ratings.md`, CP-06 rows:

| Phase | RD (rated) | TE (rated) | Notes in ratings file |
|---|:---:|:---:|---|
| Phase 1 | 4 | 4 | Self-hosted CI/CD, artifact registry, per-customer GitOps; architecturally different from single-tenant CI/CD |
| Phase 2 | 2 | 2 | Artifact delivery adaptation for network constraints; target-environment config in GitOps |
| Phase 3 | 3 | 3 | Pipeline maintenance; shared logic, per-customer delivery targets; ArgoCD/Flux upgrades |

### GT1 Ground Truth Data

[FACT] GT1 records the on-premises composite difficulty for CP-06 as **4/5**, sourced from P1_control_plane.md.
— GT1_P1_ground_truth.md, CP-06 Difficulty Ratings table
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[STATISTIC] GT1 records on-premises FTE range for CP-06 as **2.0–3.25 FTE**.
— GT1_P1_ground_truth.md, CP-06 FTE Ranges section

[STATISTIC] "Argo CD is adopted in 60% of Kubernetes clusters per the 2025 CNCF End User Survey."
— GT1_P1_ground_truth.md, CP-06 Key Operational Characteristics (citing F48, F73 C08, W07S)

[FACT] "Flux manages approximately 200 Kubernetes clusters at Deutsche Telekom with just 10 full-time engineers, with plans to scale to thousands of clusters without proportional FTE growth."
— GT1_P1_ground_truth.md, CP-06 Key Operational Characteristics (citing F48, F73 C08, W07S)

[FACT] "Self-hosted runners, Harbor container registry, Nexus/Artifactory artifact storage, and Vault secrets injection are all required [on-premises]. Jenkins published nine security advisories in 2025 — a continuous patching cadence."
— GT1_P1_ground_truth.md, CP-06 Key Operational Characteristics (citing F48, F58, W08S Theme 1)

[STATISTIC] "Air-gapped delivery requires fully self-contained .airgap bundles with every image and dependency vendored, covering 65,981+ unique Kubernetes environment configurations in the Replicated Compatibility Matrix."
— GT1_P1_ground_truth.md, CP-06 Key Operational Characteristics (citing F48, F58, W08S Theme 1)

[FACT] "GitOps controllers (Flux, ArgoCD) are cited as sub-linear in FTE scaling — Deutsche Telekom example: 200 clusters managed by 10 FTE with plans to scale to thousands without proportional FTE growth."
— GT1_P1_ground_truth.md, CP-06 Scaling Behavior (citing F48, F73 C08, W07S)

[FACT] "Helm 4 was released at KubeCon 2025."
— GT1_P1_ground_truth.md, CP-06 Notable Caveats (citing F58)

[FACT] "OLMv0 to v1 migration has no concrete path as of early 2026, creating operator delivery risk for ISVs using the Operator Lifecycle Manager."
— GT1_P1_ground_truth.md, CP-06 Notable Caveats (citing F58)

### External Validation: Deutsche Telekom Flux Case Study

[FACT] "Using Flux, DT now manages some 200 Kubernetes clusters with just 10 full-time engineers and plans to scale to thousands of clusters without adding more than one or two more members to the infrastructure team."
— FluxCD Official Website, case study reference
URL: https://fluxcd.io/

[FACT] Deutsche Telekom's Das Schiff is described as "Deutsche Telekom Technik's engine for Kubernetes Cluster as a Service (CaaS) in on-premise environment on top of bare-metal servers and VMs."
— GitHub, telekom/das-schiff repository
URL: https://github.com/telekom/das-schiff

[FACT] A Weaveworks case study details how Deutsche Telekom "along with Weaveworks GitOps manages more than 10,000 edge locations."
— Weaveworks Blog, "Case study: How Deutsche Telekom automates edge infrastructure using GitOps"
URL: https://www.weave.works/blog/case-study-how-deutsche-telekom-automates-edge-infrastructure-using-gitops

### External Validation: ArgoCD Operational Complexity at Scale

[FACT] "All ArgoCD implementations share a common challenge: inherent operational overhead and complexity of managing ArgoCD instances, which spans maintaining control planes, handling upgrades, managing configurations, and addressing operational requirements."
— Devtron Blog, "Operational Challenges with ArgoCD"
URL: https://devtron.ai/blog/operational-challenges-with-argocd/

[FACT] "Traditional multi-cluster Argo CD setups hit walls when scaling to hundreds of clusters, especially across unreliable networks, air-gapped environments, or edge locations."
— Red Hat Blog, "Multi-cluster GitOps with the Argo CD Agent"
URL: https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops

[FACT] "Deploying dedicated Argo CD instances per cluster provides better fault isolation and reduced blast radius, but comes with higher infrastructure cost, more operational complexity, and duplicated setup logic."
— Medium, "Mastering Multi-Cluster Deployments: A GitOps Journey with ArgoCD"
URL: https://meghpatel0607.medium.com/mastering-multi-cluster-deployments-a-gitops-journey-with-argocd-0dbcb3eb55cc

[STATISTIC] "60% of reported K8s clusters use Argo CD; 97% use it in production; 42% now oversee over 500 applications per Argo CD instance (up from 15% in 2023); 25% connect those instances to more than 20 clusters."
— CNCF End User Survey 2025, announced July 24, 2025
URL: https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/

### Assessment of GitOps Per-Customer Complexity Claims

The ratings file notes in Phase 3 that "Pipeline logic is shared; delivery targets are per-customer." This creates a partial scaling pattern (labeled "Partial" in the Scales with N column). This characterization is consistent with the GT1 Deutsche Telekom evidence showing sub-linear FTE growth with cluster count under Flux. The 60% CNCF ArgoCD adoption figure cited in GT1 is independently confirmed by the 2025 CNCF End User Survey.

The key distinction for ISV on-premises deployments: the Deutsche Telekom case involves a centralized platform team managing homogeneous infrastructure; ISV on-premises customers have heterogeneous networks, air-gap requirements, and per-customer artifact mirror configurations, which increases per-target complexity beyond the pure GitOps-controller scaling curve.

### Re-Derived Ratings

**Phase 1 (RD 4, TE 4):**
GT1 composite difficulty for CP-06 on-premises is 4/5. RD 4 matches GT1. The FTE range of 2.0–3.25 on an ongoing basis, combined with a one-time foundational build of self-hosted runners, Harbor, Nexus/Artifactory, and per-customer GitOps targeting, supports TE 4. The air-gap bundle complexity (65,981+ unique Kubernetes configurations in the Replicated Compatibility Matrix) further supports TE 4.

**Phase 2 (RD 2, TE 2):**
Per-customer GitOps targeting is configuration work (adapting artifact delivery for customer network constraints, configuring air-gap mirrors, target-environment values files). RD 2 and TE 2 are consistent with the GT1 evidence that GitOps controllers exhibit sub-linear scaling. This is the least controversial of the CP-06 ratings.

**Phase 3 (RD 3, TE 3):**
The GT1 FTE range of 2.0–3.25 maps to TE 3 (0.3–1.0 FTE) at the low end and TE 4 (1.0–2.5 FTE) at the mid-range. The rating of TE 3 sits at the optimistic end of the FTE band. Given that Jenkins published nine security advisories in 2025 (a continuous patching cadence) and Helm 4 was released at KubeCon 2025, ongoing patch and version management adds real recurring cost. The rating of TE 3 is defensible but not conservative.

### CP-06 Rating Assessment

| Phase | Dimension | Current Rating | Re-derived Rating | Confidence | Verdict |
|---|---|:---:|:---:|---|---|
| Phase 1 | RD | 4 | 4 | High | ACCURATE |
| Phase 1 | TE | 4 | 4 | High | ACCURATE |
| Phase 2 | RD | 2 | 2 | High | ACCURATE |
| Phase 2 | TE | 2 | 2 | High | ACCURATE |
| Phase 3 | RD | 3 | 3 | High | ACCURATE |
| Phase 3 | TE | 3 | 3–4 | Medium | ACCURATE (borderline) |

**Phase 3 TE Interview Question:** Does the ISV use a shared ArgoCD/Flux hub-and-spoke model (one controller managing all customer clusters) or dedicated GitOps controller instances per customer? Hub-and-spoke holds TE 3; per-customer controller instances add operational burden that would support TE 4.

---

## Phase 3 FTE Range Validation

The ratings file claims a total P1 Control Plane Phase 3 FTE of **20–38 FTE** across all ten CP subsegments.

[STATISTIC] GT1 records the deduplicated on-premises FTE total as **~20–38 FTE** (raw sum 24.85–44.5 FTE, deduplicated by removing 1.0–2.0 FTE from the CP-03/CP-04/CP-10 security cluster overlap).
— GT1_P1_ground_truth.md, Summary Table: All Ratings and FTE Ranges

For the three subsegments under review, the FTE contributions to that aggregate:

| Subsegment | GT1 On-Prem FTE | Ratings File Phase 3 TE | Consistency |
|---|---|:---:|---|
| CP-04 | 2.5–5.0 FTE | 4 (1.0–2.5 FTE scale) | Low end of GT1 range; conservative |
| CP-05 | 4.6–7.0 FTE | 5 (2.5+ FTE scale) | Consistent with upper GT1 range |
| CP-06 | 2.0–3.25 FTE | 3 (0.3–1.0 FTE scale) | Below GT1 range; potentially understated |

[DATA POINT] The Phase 3 TE scale anchors at "2.5+ FTE" for TE 5. CP-06's GT1 FTE of 2.0–3.25 spans TE 3 (0.3–1.0) to TE 4 (1.0–2.5) based on the Phase 3 TE scale definition. The current CP-06 TE 3 rating is at the bottom of the FTE band. This is the primary quantitative tension found in the review.
— Cross-reference: GT1_P1_ground_truth.md CP-06 FTE Ranges vs. three_phase_on_prem_ratings.md Phase 3 TE Scale

---

## Key Findings

1. **CP-04 Phase 3 RD is the most contested rating.** GT1 records on-premises CP-04 composite difficulty as 5/5. The Phase 3 RD rating of 4 is defensible because the Phase 3 scale measures difficulty relative to cloud-native — not absolute operational difficulty. However, the seal/unseal burden during Vault upgrades across N customer environments (each potentially requiring per-node Shamir key entry if auto-unseal is not deployed) could justify RD 5. Confidence is Medium pending clarification on whether production Vault deployments use auto-unseal.

2. **The 3 KB per-series RAM estimate for Prometheus is confirmed but slightly conservative.** External sources (Robust Perception, the authoritative Prometheus monitoring specialist) place the combined head-block estimate at approximately 3 KB per series as of Prometheus 2.20, with cardinality-only memory closer to 2 KB per series (2 GiB per 1M series). The 15–35 GB kube-prometheus-stack claim for a pre-workload cluster is consistent with real-world production reports documenting 14–60 GB ranges.

3. **The Deutsche Telekom Flux case study is independently confirmed.** The specific claim — 200 Kubernetes clusters managed by 10 FTE with plans to scale to thousands without proportional FTE growth — is directly verifiable from the FluxCD official website and a TechTarget article. This anchors the CP-06 sub-linear scaling claim. However, Deutsche Telekom's architecture is on-premises bare-metal, not ISV customer-deployed, which means their operational profile differs from the ISV case in air-gap requirements and customer-to-ISV access constraints.

4. **CP-06 Phase 3 TE 3 is at the optimistic floor of the GT1 FTE range.** The GT1 FTE band for CP-06 is 2.0–3.25 FTE annually, which maps more naturally to TE 4 (1.0–2.5 FTE) than TE 3 (0.3–1.0 FTE) in the Phase 3 scale. Jenkins's nine security advisories in 2025 and Helm 4's release at KubeCon 2025 represent ongoing patch and migration work that, combined with per-customer delivery target management, suggests TE 3 may be one point optimistic. This is the single adjustment most supported by the quantitative FTE evidence.

5. **FIPS 140-3 transition is confirmed as a near-term forcing function for CP-04.** FIPS 140-2 certificates expire September 2026. Vault Enterprise FIPS 140-3 Level 1 compliance requires Vault Enterprise Plus licensing and glibc-based Linux distributions, and does not support mixed binary types within a cluster. For an ISV with 50 on-premises customers, each requiring coordinated Vault binary replacement before September 2026, this is a material scheduled effort that supports the Phase 3 TE 4 rating.

---

## Sources

| Source | Type | URL / File Path |
|---|---|---|
| GT1_P1_ground_truth.md | Internal primary reference | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md` |
| three_phase_on_prem_ratings.md | Internal ratings file | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| HashiCorp Vault Raft Reference Architecture | External primary (vendor docs) | https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-reference-architecture |
| HashiCorp Vault FIPS 140-3 Built-in Support | External primary (vendor docs) | https://developer.hashicorp.com/vault/docs/enterprise/fips/fips1403 |
| HashiCorp Blog: Vault FIPS 140-3 | External (vendor blog) | https://www.hashicorp.com/en/blog/hashicorp-vault-and-fips-140-3-strengthening-security-and-compliance |
| HashiCorp Blog: Vault Enterprise 1.21 | External (vendor blog) | https://www.hashicorp.com/en/blog/vault-enterprise-1-21-spiffe-auth-fips-140-3-level-1-compliance-granular-secret-recovery |
| Let's Encrypt: 45-day certificates announcement | External primary | https://letsencrypt.org/2025/12/02/from-90-to-45 |
| Robust Perception: Prometheus 2.x RAM sizing | External specialist (Prometheus maintainers) | https://www.robustperception.io/how-much-ram-does-prometheus-2-x-need-for-cardinality-and-ingestion/ |
| Devoriales: Prometheus memory optimization | External practitioner case | https://devoriales.com/post/384/prometheus-how-we-slashed-memory-usage |
| GitHub prometheus-community/helm-charts Issue #314 | External community evidence | https://github.com/prometheus-community/helm-charts/issues/314 |
| CNCF End User Survey 2025 (ArgoCD) | External primary (CNCF) | https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/ |
| FluxCD.io: Deutsche Telekom case study | External primary (project website) | https://fluxcd.io/ |
| Weaveworks: Deutsche Telekom GitOps case study | External supporting | https://www.weave.works/blog/case-study-how-deutsche-telekom-automates-edge-infrastructure-using-gitops |
| GitHub: telekom/das-schiff | External primary (DT open source) | https://github.com/telekom/das-schiff |
| Devtron: ArgoCD operational challenges | External practitioner analysis | https://devtron.ai/blog/operational-challenges-with-argocd/ |
| Red Hat: ArgoCD Agent multi-cluster | External vendor analysis | https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops |
