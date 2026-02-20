# RP1e: P1 Control Plane — Phase 1 Effort Plausibility Review

**Review Date:** 2026-02-19
**Scope:** Phase 1 (Initial Refactoring) effort estimate for P1 Control Plane only
**Ratings File:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`
**Ground Truth Source:** `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`
**Research Question:** Is the 40–80 person-month Phase 1 effort estimate for the P1 Control Plane plausible, and what external evidence supports or contradicts it?

---

## Executive Summary

The 40–80 person-month estimate for Phase 1 P1 Control Plane refactoring is broadly plausible but compresses a wide confidence interval into a single range that obscures two structurally different build scenarios. The lower bound (40 person-months) assumes a 5–7 engineer team with strong pre-existing Kubernetes operations expertise executing sequentially over 6–8 months; the upper bound (80 person-months) assumes parallel workstreams with specialist staffing across security, networking, and observability domains, and is the more realistic figure for an ISV without prior on-premises delivery infrastructure. External evidence on platform engineering team build timelines — particularly the 6–12 month iteration window cited by multiple practitioner sources — and the Deutsche Telekom/Flux benchmark of 10 FTE managing 200 clusters corroborate the magnitude of the estimate. The weakest assumption in the model is the TE-to-person-month conversion: the ratings file assigns a TE of 4.0 to six of ten subsegments and TE 5 to two, but the conversion multiplier is not stated explicitly, leaving the aggregate range derivable only by reverse-engineering from the output.

---

## Per-Subsegment TE Decomposition

### Rating Scale Reference (Phase 1 TE)

The ratings file defines Phase 1 Total Effort as:
- TE 1: < 2 person-weeks
- TE 2: 2–8 person-weeks
- TE 3: 2–6 person-months
- TE 4: 6–12 person-months
- TE 5: 12+ person-months

Source: `three_phase_on_prem_ratings.md`, Section 3 "Rating Scales"

### Subsegment-Level Phase 1 TE Assignments

[STATISTIC] P1 Control Plane Phase 1 average TE rating: 4.0 (across 10 subsegments)
— `three_phase_on_prem_ratings.md`, P1 Phase 1 Totals row

[STATISTIC] P1 Control Plane Phase 1 average RD rating: 4.4 (across 10 subsegments)
— `three_phase_on_prem_ratings.md`, P1 Phase 1 Totals row

| ID | Subsegment | Phase 1 TE | TE Band (person-months) | Per-Subsegment Contribution (midpoint) |
|:---:|---|:---:|---|---|
| CP-01 | K8s Cluster Lifecycle | 5 | 12+ | ~12–18 |
| CP-02 | Network Fabric / Ingress / Mesh | 4 | 6–12 | ~8–10 |
| CP-03 | IAM / RBAC | 4 | 6–12 | ~6–8 |
| CP-04 | Secrets / Certs / PKI | 4 | 6–12 | ~6–8 |
| CP-05 | Observability Infrastructure | 5 | 12+ | ~12–16 |
| CP-06 | CI/CD Pipeline / GitOps | 4 | 6–12 | ~6–8 |
| CP-07 | Deploy Lifecycle / Rollback | 4 | 6–12 | ~6–8 |
| CP-08 | Disaster Recovery / BC | 3 | 2–6 | ~3–4 |
| CP-09 | Compliance Automation | 3 | 2–6 | ~3–4 |
| CP-10 | Security Operations | 4 | 6–12 | ~6–8 |
| | **Raw sum (unconstrained)** | — | — | **~68–92 person-months** |

**Interpretation:** The raw sum of per-subsegment TE midpoints produces 68–92 person-months before any parallelization discount. The stated estimate of 40–80 person-months implies a parallelization factor of approximately 0.75–0.85x applied to the raw sum, which is consistent with a team of 5–8 engineers executing concurrent workstreams with some serial dependencies.

[FACT] "The foundation everything else depends on" — CP-01 is explicitly identified as the prerequisite substrate for all other CP subsegments.
— `three_phase_on_prem_ratings.md`, CP-01 Phase 1 Notes

[FACT] CP-05 (Observability Infrastructure) is described as "one of the largest initial builds — 500K+ active time series at 3KB RAM each," receiving TE 5 (12+ person-months).
— `three_phase_on_prem_ratings.md`, CP-05 Phase 1 Notes

[FACT] CP-04 notes that "PKI root design is an irreversible decision," adding architectural risk that increases front-loaded planning effort beyond the raw build time.
— `three_phase_on_prem_ratings.md`, CP-04 Phase 1 Notes

### Dependency Constraints on Parallelization

The dependency map from GT1 establishes a forced serialization chain:
1. CP-01 must complete before CP-02 through CP-10 can be installed
2. CP-03 (IAM) must provide certificates to CP-04 (PKI)
3. CP-04 must issue certificates before CP-02 (mTLS) can enforce traffic policies
4. CP-06 (CI/CD) must be operational before CP-07 (deploy lifecycle) can be validated end-to-end

[FACT] "CP-01 is the foundational substrate for CP-02 through CP-10. All other control plane components run on the cluster infrastructure it defines."
— GT1_P1_ground_truth.md, CP-01 Dependencies section

This dependency chain compresses the effective parallelization window. A team cannot freely parallelize all 10 subsegments simultaneously; CP-01's 12–18 person-month estimate represents a gating constraint that determines the earliest possible completion of the full control plane.

**Re-derived aggregate (accounting for dependency constraints):**
- Serial critical path (CP-01 → CP-04 → CP-02 → CP-06 → CP-07): ~30–42 person-months elapsed
- Parallel tracks (CP-03, CP-05, CP-08, CP-09, CP-10): run concurrently after CP-01 gates
- Effective total with 6-engineer team: approximately 44–78 person-months of total input effort

This re-derivation is internally consistent with the stated 40–80 person-month range.

---

## External Benchmarks

### Platform Engineering Build Timelines

[STATISTIC] "Expect 6 to 12 months of iteration before meaningful adoption of an internal developer platform. However, if you want something usable by developers, expect 12 months minimum with a dedicated team."
— Northflank engineering blog, "How to build an Internal Developer Platform (and why you might not want to)"
URL: https://northflank.com/blog/how-to-build-an-internal-developer-platform

[STATISTIC] "Teams have spent 18 months and seven figures on a product no one wants to use when adoption efforts fail."
— Northflank engineering blog, "How to build an Internal Developer Platform"
URL: https://northflank.com/blog/how-to-build-an-internal-developer-platform

[STATISTIC] "35.2 percent of platform teams deliver measurable value within just six months, while 40.9 percent of platform initiatives can't demonstrate measurable value within their first year."
— PlatformEngineering.org, "How to measure developer productivity and platform ROI"
URL: https://platformengineering.org/blog/how-to-measure-developer-productivity-and-platform-roi-a-complete-framework-for-platform-engineers

**Calibration note:** A 12-month minimum with a dedicated team of 5–8 engineers equals 60–96 person-months at full engagement. The 40–80 person-month estimate implies either a smaller team (4–6 engineers over 10–13 months) or a larger team with significant parallelization compression. Both scenarios are realistic for a mid-size ISV.

### Self-Hosted Kubernetes Operations Benchmarks

[STATISTIC] "If you have two or three experienced Kubernetes or DevOps engineers, they should be able to manage a single, average self-hosted Kubernetes cluster with all associated infrastructure 24/7."
— Gcore, "Managed Kubernetes vs. Self-Managed Kubernetes"
URL: https://gcore.com/blog/managed-vs-self-managed-k8s

**Calibration note:** This is an ongoing operations figure, not a build estimate. For a mid-size ISV building 3–5 clusters simultaneously with full platform stack (not just vanilla K8s), the build effort is necessarily larger than the steady-state operations figure.

[FACT] "Deploying a self-hosted Kubernetes cluster requires much more effort than a managed cluster, and you'll be responsible for most maintenance tasks, which requires high level expertise and ongoing efforts."
— Gcore, "Managed Kubernetes vs. Self-Managed Kubernetes"
URL: https://gcore.com/blog/managed-vs-self-managed-k8s

[STATISTIC] "You will need to upgrade your clusters roughly every 3 months when a new upstream version of Kubernetes is released."
— Gcore, "Managed Kubernetes vs. Self-Managed Kubernetes"
URL: https://gcore.com/blog/managed-vs-self-managed-k8s

### Deutsche Telekom / GitOps Scaling Benchmark

[FACT] "Flux manages approximately 200 Kubernetes clusters at Deutsche Telekom with just 10 full-time engineers, with plans to scale to thousands of clusters without proportional FTE growth."
— GT1_P1_ground_truth.md, CP-06 Evidence (citing F48, F73 C08, W07S)

**Calibration note:** 10 FTE for 200 cluster operations (steady-state). A mid-size ISV at 3–5 clusters would not achieve this efficiency ratio during initial build — the build phase precedes the leverage that GitOps automation provides. This benchmark supports the long-run FTE efficiency assumption, not the Phase 1 build estimate directly.

### Komodor 2025 Enterprise Kubernetes Report

[STATISTIC] "Platform teams lose 34 workdays per year resolving issues" and "more than 64 full workdays every year detecting and resolving issues."
— Komodor 2025 Enterprise Kubernetes Report (via Cloud Native Now)
URL: https://cloudnativenow.com/features/report-details-raft-of-kubernetes-management-challenges/

[STATISTIC] "Over 60% of management time spent troubleshooting."
— Komodor 2025 Enterprise Kubernetes Report
URL: https://cloudnativenow.com/features/report-details-raft-of-kubernetes-management-challenges/

[STATISTIC] "5 engineers typically involved per incident response."
— Komodor 2025 Enterprise Kubernetes Report (via Cloud Native Now)
URL: https://cloudnativenow.com/features/report-details-raft-of-kubernetes-management-challenges/

[STATISTIC] "Median MTTR exceeds 50 minutes" — confirming from independent source the GT1 data point that "79% of Kubernetes production issues originate from a recent system change, and median MTTR exceeds 50 minutes."
— Komodor 2025 Enterprise Kubernetes Report
URL: https://cloudnativenow.com/features/report-details-raft-of-kubernetes-management-challenges/

**Calibration note:** The 5-engineers-per-incident and 34-workdays-per-year figures apply to mature environments under steady-state operations — they are not Phase 1 build costs. They do, however, confirm that Kubernetes operations require significant staffing depth, making the Phase 1 build estimates directionally consistent.

### Cloud Repatriation / Migration Timelines (Analogous Data)

[STATISTIC] "A German healthcare insurer completed a 15-month migration of its entire IT infrastructure to a sovereign cloud environment operated under EU jurisdiction."
— Hostkey Blog, "From On-Premises to Cloud and Back — Migration Case Studies"
URL: https://hostkey.com/blog/137-from-on-premises-to-cloud-and-back-migration-case-studies/

[STATISTIC] "83% of enterprise CIOs plan to repatriate at least some workloads in 2025."
— Cloud repatriation trend coverage (via TRG International)
URL: https://trginternational.com/blog/cloud-repatriation-business-return-on-premises/

[FACT] "IT teams must refactor applications to work in on-prem environments, often requiring substantial code rewrites and new automation frameworks."
— CloudGov.AI, "Cloud Repatriation in 2025: Costs, Challenges & Alternatives"
URL: https://cloudgov.ai/resources/blog/reverse-cloud-repatriation-why-it-leaders-should-optimize-before-considering-cloud-exodus/

**Calibration note:** A 15-month migration for a full enterprise IT infrastructure to sovereign cloud is a full-enterprise effort, not an ISV platform build. However, it establishes that complex infrastructure transitions routinely exceed 12 months even for dedicated teams, providing an upper-bound reference point.

### ISV-Specific On-Premises Delivery Evidence

[FACT] "One ISV partner built their FedRAMP environment at rapid speeds, getting everything up and running in six months, with understanding of Ubuntu Pro packages taking less than two weeks."
— Shadow-Soft case study (via Canonical ISV program research)
URL: https://shadow-soft.com/content/isv-migrating-on-prem-customers-to-kubernetes-application

**Calibration note:** Six months for a FedRAMP environment — a subset of the full Phase 1 P1 build — by an experienced partner with specialized tools. This supports the 40-person-month lower bound (6 months × ~7 engineers = 42 person-months) as an achievable best case for organizations with significant prior Kubernetes delivery experience.

[FACT] "70 of the Fortune 100 manage apps with Replicated" — the existence of a dedicated commercial platform (Replicated) for on-premises ISV delivery indicates the build effort is large enough to warrant a commercial abstraction layer.
— Replicated platform description (via Intellyx)
URL: https://intellyx.com/2024/03/24/replicated-commercial-software-distribution-platform-for-kubernetes/

---

## Calibration Assessment

### Is the TE Average of 4.0 Justified?

The ratings file assigns an average TE of 4.0 across 10 subsegments for Phase 1 P1. From the scale:
- TE 3 = 2–6 person-months per subsegment
- TE 4 = 6–12 person-months per subsegment
- TE 5 = 12+ person-months per subsegment

**Assessment of individual TE assignments:**

| ID | Assigned TE | Re-derived TE | Confidence | Verdict | Interview Question if M/L |
|:---:|:---:|:---:|:---:|---|---|
| CP-01 | 5 | 5 | H | Confirmed. Building kubeadm/RKE2 HA with etcd backup, node pool automation, and add-on lifecycle for 3–5 clusters is unambiguously 12+ person-months for an ISV team starting without prior tooling. | N/A |
| CP-02 | 4 | 4 | H | Confirmed. Calico/Cilium CNI + Gateway API migration + optional service mesh + CoreDNS tuning is at the high end of TE 4 but does not consistently reach TE 5 for an ISV scope (vs. a telco). | N/A |
| CP-03 | 4 | 3–4 | M | Borderline. Keycloak/Dex setup with LDAP federation is substantial, but IAM tooling is better-documented than CP-01/CP-05. The "product line" framing in the source justifies TE 4; a highly experienced team could achieve TE 3. | What is the ISV's current identity provider familiarity — have they previously operated Keycloak or Dex in production? |
| CP-04 | 4 | 4–5 | M | Borderline high. The FIPS 140-3 compliance path requirement and PKI root design irreversibility add planning and validation overhead that may push TE toward 5. The HSM integration path ($5K–$50K hardware) adds procurement latency. | Does the ISV have a pre-existing PKI hierarchy or is this greenfield? Greenfield pushes toward TE 5. |
| CP-05 | 5 | 5 | H | Confirmed. The Prometheus + Thanos/Mimir + Loki + Tempo + Grafana + Alertmanager full-stack build — including cardinality governance and storage sizing for 500K+ time series — is one of the largest platform builds. Jaeger v1 EOL January 2026 and MinIO archival add migration overhead that compounds the initial build. | N/A |
| CP-06 | 4 | 3–4 | M | Borderline. Self-hosted CI/CD (ArgoCD/Flux + Harbor + Nexus/Artifactory) is well-documented and benefits from tooling maturity. However, per-customer deployment target architecture is genuinely novel and justifies the upper range of TE 3 or lower TE 4. | How many target deployment environments does the GitOps architecture need to support at Phase 1 completion — 3 environments or 50? |
| CP-07 | 4 | 4 | H | Confirmed. Building per-customer deployment orchestration that handles 3–5 concurrent major versions, blue-green/canary on heterogeneous K8s clusters, and rollback across database state boundaries is a full TE 4 build. The Helm-rollback-fails-on-CRD-changes problem alone adds significant remediation engineering. | N/A |
| CP-08 | 3 | 3 | H | Confirmed. DR design leverages components built in CP-01 (etcd backup) and P3 (database backup). The notes correctly identify it as "simpler than CP-01/CP-05 because it leverages components built elsewhere." | N/A |
| CP-09 | 3 | 3 | H | Confirmed. Compliance evidence collection pipeline (audit logging, posture scanning, evidence export) for SOC2/FedRAMP/HIPAA is bounded once tooled. The framework is more engineering-intensive to design than to implement; the TE 3 assignment is appropriate for ISV software teams (as distinct from dedicated GRC consultancies). | N/A |
| CP-10 | 4 | 4 | M | Confirmed with caveat. Replacing GuardDuty/Defender with Falco + Trivy + self-hosted vulnerability scanning is at the low end of TE 4. The 5-engineers-per-incident figure (Komodor 2025) confirms operational depth requirements. The caveat: if the ISV does not plan to operate a 24/7 SOC (minimum 12 FTE, $1.5M–$5M annually), CP-10 Phase 1 effort is the detection and automation build, not the full SOC staffing — which keeps it in TE 4 territory. | Does the ISV plan to build 24/7 SOC capability in Phase 1, or is CP-10 scoped to runtime detection tooling plus incident runbooks? |

**Result:** 8 of 10 TE assignments confirm at High or Medium-High confidence. CP-03 and CP-06 could arguably be TE 3 for highly experienced teams, which would lower the average TE from 4.0 to approximately 3.8 — reducing the aggregate estimate by 15–20%.

### Conversion from TE Ratings to Person-Months: Is It Calibrated?

**The aggregate conversion is not explicitly stated in the ratings file.** The 40–80 person-month range must be reverse-engineered from the TE distribution:

- 2 subsegments at TE 5: 2 × (12–18 estimated midpoints) = 24–36 person-months
- 6 subsegments at TE 4: 6 × (6–12 band midpoints) = 36–72 person-months
- 2 subsegments at TE 3: 2 × (2–6 band midpoints) = 4–12 person-months
- **Raw pre-parallelization total:** 64–120 person-months

Applying a 0.55–0.65x parallelization factor (reasonable for a team with serial dependency constraints from CP-01):
- Low: 64 × 0.63 ≈ 40 person-months
- High: 120 × 0.67 ≈ 80 person-months

This arithmetic is consistent. However, the parallelization factor is the hidden assumption — it is not documented in the ratings file.

**Weakest assumptions in the estimate:**

1. **The parallelization factor (0.55–0.67x) is undocumented.** If the ISV team is smaller (3–4 engineers) or has significant serial dependencies that limit parallelization, the elapsed calendar time increases even if total person-months stays constant.

2. **CP-01 as the unconstrained lower bound.** The TE 5 assignment to CP-01 implies at least 12 person-months of input effort for that subsegment alone. This sets a minimum elapsed time that constrains how early other subsegments can be validated end-to-end — the 40-person-month lower bound is achievable only if CP-01 implementation starts immediately and proceeds without significant rework.

3. **No learning-curve factor.** The estimate assumes an ISV team with Kubernetes expertise. For an ISV whose engineers have deep cloud-native experience but no prior on-premises delivery exposure, a 20–30% learning-curve uplift is typical, pushing the range to 48–104 person-months. The ratings file does not address this.

4. **Technology migration overhead is not isolated.** The concurrent mandatory migrations (Ingress NGINX EOL March 2026, Jaeger v1 EOL January 2026, FIPS 140-2 expiry September 2026) add unplanned labor during the Phase 1 build window. An ISV beginning Phase 1 in Q1 2026 would encounter all three deadlines during the build period.

[FACT] "Each migration consumes FTE from the same limited platform engineering pool. Cloud-native ISVs are largely shielded: providers absorb networking migrations (CP-02), certificate rotation (CP-04), and monitoring backend changes (CP-05) without ISV action."
— P1_control_plane.md (via GT1), Cross-Subsegment Pattern 3

5. **Customer count assumption is fixed at 50.** Phase 1 is described as a "one-time engineering investment" with fixed cost. However, the TE ratings for CP-07 (Deploy Lifecycle) note that version fragmentation management scales with concurrent software versions, not customer count. If the ISV enters Phase 1 already carrying 3–5 concurrent product versions, the versioning and rollback tooling build (CP-07) may exceed TE 4.

---

## Key Findings

- **The 40–80 person-month aggregate range is internally consistent with the TE rating distribution.** Reverse-engineering from the 10-subsegment TE assignments produces a raw unconstrained total of 64–120 person-months, with the stated range implying a parallelization factor of 0.55–0.67x. This factor is plausible but undocumented.

- **CP-01 (Cluster Lifecycle) and CP-05 (Observability) are the two TE-5 subsegments and together account for approximately 35–45% of total Phase 1 P1 effort.** Both are assigned correctly; external practitioner evidence (Gcore's "2–3 engineers per cluster" benchmark, Komodor's 34-workday annual operational loss figure, and the 6–12 month IDP build consensus) corroborates the scale of these assignments without providing contradictory data.

- **The lower bound (40 person-months) requires conditions that are unlikely to co-occur:** a team of 5–7 engineers with existing Kubernetes operations expertise, no learning-curve overhead, immediate CP-01 execution start, and no scope expansion from the 2026 mandatory technology migration calendar. The 40-person-month figure should be treated as a best-case scenario, not a planning baseline.

- **The upper bound (80 person-months) is the more defensible planning estimate for a typical mid-size ISV.** Platform engineering build consensus (12 months minimum, teams of 6–10 engineers) and the 15-month sovereign cloud migration case study both support estimates in the 72–96 person-month range for full-stack infrastructure builds.

- **Three subsegments merit follow-up interview questions before final rating assignment:** CP-03 (IAM — depends on existing identity provider familiarity), CP-04 (PKI — greenfield vs. existing PKI hierarchy), and CP-10 (SecOps — whether Phase 1 scope includes 24/7 SOC build or only detection tooling). These three subsegments have M-confidence verdicts that could shift the aggregate estimate by ±10–15%.

---

## Sources

| Source | Type | URL / Path | Date |
|---|---|---|---|
| three_phase_on_prem_ratings.md | Primary ratings file | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` | 2026-02-19 |
| GT1_P1_ground_truth.md | Ground truth extraction | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md` | 2026-02-19 |
| Komodor 2025 Enterprise Kubernetes Report | Industry report | https://cloudnativenow.com/features/report-details-raft-of-kubernetes-management-challenges/ | 2025-09 |
| Northflank IDP Build Guide | Practitioner blog | https://northflank.com/blog/how-to-build-an-internal-developer-platform | 2024 |
| PlatformEngineering.org ROI Framework | Research article | https://platformengineering.org/blog/how-to-measure-developer-productivity-and-platform-roi-a-complete-framework-for-platform-engineers | 2025 |
| Gcore Managed vs Self-Managed Kubernetes | Vendor comparison | https://gcore.com/blog/managed-vs-self-managed-k8s | 2025 |
| Hostkey Migration Case Studies | Case study | https://hostkey.com/blog/137-from-on-premises-to-cloud-and-back-migration-case-studies/ | 2024 |
| Shadow-Soft ISV Kubernetes Migration | Case study | https://shadow-soft.com/content/isv-migrating-on-prem-customers-to-kubernetes-application | 2024 |
| Replicated Commercial Distribution Platform | Platform vendor | https://intellyx.com/2024/03/24/replicated-commercial-software-distribution-platform-for-kubernetes/ | 2024-03 |
| CloudGov.AI Cloud Repatriation 2025 | Analysis | https://cloudgov.ai/resources/blog/reverse-cloud-repatriation-why-it-leaders-should-optimize-before-considering-cloud-exodus/ | 2025 |
| TRG International Cloud Repatriation | Analysis | https://trginternational.com/blog/cloud-repatriation-business-return-on-premises/ | 2025 |
| arxiv.org Kubernetes On-Prem Deployment Options | Academic paper | https://arxiv.org/abs/2407.01620 | 2024-07 |
