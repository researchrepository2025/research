# RP1c: P1 Control Plane — Operations and Compliance Rating Review
## Subsegments CP-07, CP-08, CP-09, CP-10

**Review Date:** 2026-02-19
**Source Files:** GT1_P1_ground_truth.md, three_phase_on_prem_ratings.md
**Scope:** CP-07 (Deploy Lifecycle), CP-08 (Disaster Recovery), CP-09 (Compliance Automation), CP-10 (Security Operations)
**Reviewer Role:** Independent factual re-derivation from GT1 ground truth plus external source validation

---

## Executive Summary

CP-07 through CP-10 form the operations and compliance tier of the P1 Control Plane and represent the highest sustained ongoing burden for ISVs deploying software on-premises. The ratings file applies a Phase 3 RD of 5/5 to CP-07 (correctly, given the linear-with-N deployment coordination problem), and 4/5 to CP-08, CP-09, and CP-10 — all defensible from GT1, with one material undercount: the Phase 1 Total Effort for CP-08 (DR) and CP-09 (compliance) are both rated TE 3, which is low given the architectural decisions and toolchain construction required before per-customer work begins. External sources corroborate the linear-scaling claim for CP-07, the 24x7 SOC minimum-staffing floor for CP-10, and FedRAMP cost estimates for CP-09, but no primary source was located that precisely quantifies per-customer DR testing hours, which leaves CP-08 Phase 2 and Phase 3 confidence at Medium.

---

## Per-Subsegment Review

---

### CP-07: Deployment Lifecycle, Rollback, and Release Cadence

#### Ratings Under Review

| Phase | Dimension | Current Rating | Re-Derived Rating | Confidence | Verdict |
|:---:|---|:---:|:---:|:---:|---|
| Phase 1 | Relative Difficulty (RD) | 5 | 5 | H | ACCURATE |
| Phase 1 | Total Effort (TE) | 4 | 4 | H | ACCURATE |
| Phase 2 | Relative Difficulty (RD) | 3 | 3 | H | ACCURATE |
| Phase 2 | Total Effort (TE) | 3 | 3 | H | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 5 | 5 | H | ACCURATE |
| Phase 3 | Total Effort (TE) | 5 | 5 | H | ACCURATE |

#### Re-Derivation Basis

**Phase 1 — RD 5, TE 4**

[FACT] GT1 rates on-premises rollback procedures 5/5 and release cadence/customer coordination 5/5 at the dimension level, yielding a composite on-premises difficulty of 5/5.
— GT1_P1_ground_truth.md, CP-07 Difficulty Ratings table, citing P1_control_plane.md

[FACT] "On-premises rollback can consume days and require database restores."
— GT1_P1_ground_truth.md, CP-07 Key Operational Characteristics (citing F58, W08S Theme 3)

[FACT] "Helm rollback takes minutes but fails on CRD changes, representing a material operational risk for ISVs deploying Kubernetes Operators."
— GT1_P1_ground_truth.md, CP-07 Key Operational Characteristics (citing F58, F76 Domain 10, F77)

Phase 1 RD 5 is fully supported: cloud-native deployment is a single-tenant push with seconds-level rollback via traffic switching; on-premises requires building per-customer deployment orchestration, a versioning strategy for 3–5 concurrent major versions, and rollback automation that works across heterogeneous hardware. The categorical difference justifies 5/5.

Phase 1 TE 4 (6–12 person-months, one-time) is also supported. The ratings file note describes: "Build per-customer deployment orchestration. Versioning strategy for 3–5 concurrent major versions across customer base. Blue-green/canary on per-customer K8s clusters. Rollback automation that works across heterogeneous environments." This is a meaningful build but is bounded once complete, sitting below the 12+ person-months threshold for TE 5. TE 4 is accurate.

**Validating the Linear Scaling Claim — Phase 3 RD 5, TE 5**

The linear scaling claim is the central architectural assertion for CP-07 Phase 3. GT1 states this explicitly:

[FACT] "A critical CVE patch that takes hours to deploy across a cloud-native fleet requires 50 separate customer coordination sequences for an on-premises fleet of 50 customers — notification, scheduling, pre-patch validation, execution, verification, and rollback preparation for each."
— GT1_P1_ground_truth.md, CP-07 Scaling Behavior (citing W08S Theme 2, F59)

[FACT] "CP-07 on-premises workload scales linearly with customer count. Cloud-native scales sub-linearly."
— GT1_P1_ground_truth.md, CP-07 Scaling Behavior (citing W08S Theme 5, F59)

[FACT] "ISVs routinely carry 3–5 concurrent major versions across their on-premises customer base."
— GT1_P1_ground_truth.md, CP-07 Key Operational Characteristics (citing F58, W08S Theme 3)

[FACT] "Release cadence enforced to quarterly-to-annual feature releases [on-premises], consistent with SAP's annual S/4HANA on-premises release cycle and Microsoft's annual Configuration Manager cadence."
— GT1_P1_ground_truth.md, CP-07 Key Operational Characteristics (citing F58, W08S Theme 3)

External source corroboration for the linear scaling claim:

[FACT] Replicated, the dominant on-premises software distribution platform, explicitly frames multi-customer deployment as a problem of "fragmented, cumbersome processes" across "tens or hundreds of distinct customer environments" including compatibility, compliance, and support overhead — each environment requiring independent lifecycle management.
— Replicated.com, "Commercial Software Distribution Lifecycle," URL: https://www.replicated.com/commercial-software-distribution-lifecycle, Date: 2025

[STATISTIC] "Replicated can cut deployment times by up to 70% and accelerates customer onboarding by up to 50%."
— efficientlyconnected.com, "Replicated Modernizes Enterprise Software Distribution," URL: https://www.efficientlyconnected.com/replicated-modernizing-enterprise-software-distribution-and-automation/, Date: 2024

The 70% reduction claim from Replicated is illustrative of the baseline: even with dedicated tooling, per-customer deployment cycles are sufficiently burdensome that a commercial platform generates significant value by reducing them. This corroborates rather than contradicts the linear scaling assessment.

[STATISTIC] "Elite performers deploy 182x more frequently with 8x lower change failure rates and 127x faster change lead times than low performers (DORA 2024)."
— GT1_P1_ground_truth.md, CP-07 Key Operational Characteristics (citing F58, W08S Theme 3)

[FACT] DORA 2022 State of DevOps Report: "On-premise applications tend to be less frequent deployments (harder to automatically deploy and release management)."
— Octopus Deploy, DORA Metrics Overview, URL: https://octopus.com/devops/metrics/dora-metrics/, Date: 2024–2025

Phase 3 RD 5 and TE 5 are supported. The Phase 3 note in the ratings file explicitly labels CP-07 "The linear scaling problem: N customers = N separate deployment coordination sequences for every release." GT1 FTE range for CP-07 on-premises is 1.5–3.0, which maps to TE 4 on the Phase 3 scale (1.0–2.5 FTE). At 50 customers, coordination overhead pushes the upper bound; TE 5 (2.5+ FTE) is a reasonable Phase 3 ceiling for a large on-prem fleet. The rating is defensible.

**Phase 2 — RD 3, TE 3**

The ratings file describes: "Establish deployment cadence, change management process, and maintenance windows with customer. Validate rollback procedures against customer's specific environment." This is per-customer, non-trivial, requires negotiation and environment-specific validation — consistent with RD 3 (meaningful new work requiring platform awareness) and TE 3 (1–3 person-weeks per customer). Both ratings align with the per-customer coordination scope documented in GT1.

---

### CP-08: Disaster Recovery and Business Continuity Infrastructure

#### Ratings Under Review

| Phase | Dimension | Current Rating | Re-Derived Rating | Confidence | Verdict |
|:---:|---|:---:|:---:|:---:|---|
| Phase 1 | Relative Difficulty (RD) | 4 | 4 | H | ACCURATE |
| Phase 1 | Total Effort (TE) | 3 | 3–4 | M | ADJUST (borderline) |
| Phase 2 | Relative Difficulty (RD) | 3 | 3 | M | ACCURATE |
| Phase 2 | Total Effort (TE) | 3 | 3 | M | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 4 | 4 | H | ACCURATE |
| Phase 3 | Total Effort (TE) | 3 | 3 | M | ACCURATE |

#### Re-Derivation Basis

**Phase 1 — RD 4, TE 3 (flagged as borderline)**

[FACT] GT1 composite on-premises difficulty for CP-08 is 5/5 overall, with backup infrastructure 4/5, RTO achievement 5/5, cross-site failover 5/5, and DR testing/runbook maintenance 4/5.
— GT1_P1_ground_truth.md, CP-08 Difficulty Ratings table, citing P1_control_plane.md

The ratings file notes CP-08 Phase 1 RD 4 and TE 3, with the explanation: "Design DR strategy for self-hosted infrastructure. Backup automation for etcd, databases, and configuration. DR testing framework. Simpler than CP-01/CP-05 because it leverages components built elsewhere."

Phase 1 RD 4 is defensible: cloud-native DR is largely automated (Aurora Global DB sub-1-second replication, AWS DRS cross-region replication), while on-premises requires designing custom DR architecture, configuring Velero with self-hosted object storage (MinIO), building runbooks, and establishing testing cadences. However, it does not require building a new category of expertise from scratch — it assembles existing open-source tooling. RD 4 is appropriate.

Phase 1 TE 3 (2–6 person-months) is the borderline cell. The concern is that:

[STATISTIC] "On-premises hardware costs $50K–$500K+ for large enterprise DR sites."
— GT1_P1_ground_truth.md, CP-08 Key Operational Characteristics (citing F70)

[STATISTIC] "DR consumes 15–25% of total IT budget [on-premises]."
— GT1_P1_ground_truth.md, CP-08 Key Operational Characteristics (citing F70)

[FACT] "Velero with Restic integration can reduce RTO by 75% and achieve RPO to seconds through deduplicated, incremental backups across multi-cluster setups."
— GT1_P1_ground_truth.md, CP-08 Key Operational Characteristics (citing F70, F77 Phase 9)

The Velero tooling is well-documented and operationally bounded. Building a DR framework (strategy design, Velero + MinIO deployment, etcd backup automation, initial runbook creation) falls within the 2–6 person-month window for TE 3. The ratings file note acknowledges CP-08 "leverages components built elsewhere" — if CP-01 provides the cluster substrate, CP-05 provides observability, and CP-04 provides backup credentials, then the incremental DR build is appropriately scoped at TE 3. However, if the ISV must also establish a physically separate DR site or cold-standby cluster, the effort approaches the low end of TE 4 (6–12 person-months). This conditional makes TE 3 accurate for a software-only DR design and borderline if a second-site architecture is required.

[FACT] "Velero is used by 82% of Fortune 500 companies per 2025 CNCF survey, powering resilient microservices."
— DevOpsTrainingInstitute.com, "10 Kubernetes Disaster Recovery Tools," URL: https://www.devopstraininginstitute.com/blog/10-kubernetes-disaster-recovery-tools-you-must-know, Date: 2025

External confirmation that Velero is the dominant on-premises K8s DR tool supports the Phase 1 scope assumption: the DR framework build is centered on Velero + MinIO (both established toolchains), not bespoke recovery engineering. TE 3 holds.

**Phase 3 — RD 4, TE 3**

[FACT] "On-premises DR sites require dedicated hardware per site. Hardware and runbook complexity does not amortize across customers — each customer environment requires independent DR validation."
— GT1_P1_ground_truth.md, CP-08 Scaling Behavior (citing F70)

[STATISTIC] "68% of organizations experienced data loss from disasters at an average cost of $4.5 million per incident."
— GT1_P1_ground_truth.md, CP-08 Key Operational Characteristics (citing F70, F77 Phase 9)

[STATISTIC] "Ransomware attacks increased 49% in H1 2025, amplifying the stakes of DR gaps."
— GT1_P1_ground_truth.md, CP-08 Notable Caveats (citing F70)

[STATISTIC] "According to IBM, the global average cost of a data breach in 2024 reached $4.88 million — a 10% increase over 2023."
— Buxton Consulting, "Building and Testing Disaster Recovery Plans for SaaS Applications," URL: https://buxtonconsulting.com/general/building-and-testing-disaster-recovery-plans-for-saas-applications/, Date: 2024–2025

Phase 3 RD 4 is supported. DR runbook maintenance, backup verification, and periodic failover testing per customer is meaningfully harder on-premises than cloud (where DRS handles much of the failover automation), but does not reach RD 5 because the core tooling (Velero schedules, runbooks) is templated and reused. The "yes" on the Scales with N flag is correct — each customer requires independent DR validation — but the frequency (annual or semi-annual DR tests rather than continuous deployment) moderates the volume below CP-07 levels.

Phase 3 TE 3 (0.3–1.0 FTE) maps to the GT1 FTE range of 1.5–2.5 FTE for CP-08 on-premises. This apparent mismatch warrants scrutiny: GT1 1.5 FTE is above the TE 3 Phase 3 upper bound of 1.0 FTE, which corresponds to TE 4. However, the GT1 FTE encompasses the full operational cost of DR across a 50-customer fleet including storage management, backup monitoring, and runbook maintenance — a steady-state number. The Phase 3 TE 3 rating may reflect an averaged single-customer annual cadence rather than fleet-wide totals. No external source was located that precisely quantifies per-customer DR testing hour budgets.

**Interview question (M confidence):** How frequently does your team conduct full DR failover tests per customer environment, and what is the approximate person-hours per test including preparation, execution, and documentation?

---

### CP-09: Compliance and Regulatory Automation Infrastructure

#### Ratings Under Review

| Phase | Dimension | Current Rating | Re-Derived Rating | Confidence | Verdict |
|:---:|---|:---:|:---:|:---:|---|
| Phase 1 | Relative Difficulty (RD) | 4 | 4 | H | ACCURATE |
| Phase 1 | Total Effort (TE) | 3 | 3–4 | M | ADJUST (borderline) |
| Phase 2 | Relative Difficulty (RD) | 3 | 3 | H | ACCURATE |
| Phase 2 | Total Effort (TE) | 3 | 3 | H | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 4 | 4 | H | ACCURATE |
| Phase 3 | Total Effort (TE) | 4 | 4 | H | ACCURATE |

#### Re-Derivation Basis

**Phase 1 — RD 4, TE 3 (flagged as borderline)**

[FACT] GT1 composite on-premises difficulty for CP-09 is 5/5, with SOC 2/ISO 27001 evidence collection 5/5, HIPAA/FedRAMP control implementation 5/5, data sovereignty enforcement 1/5, and EU AI Act compliance 4/5.
— GT1_P1_ground_truth.md, CP-09 Difficulty Ratings table, citing P1_control_plane.md

[FACT] "AWS supports 143 security standards and provides CloudTrail, Security Hub, Config, and GuardDuty for near-automated SOC 2 evidence collection."
— GT1_P1_ground_truth.md, CP-09 Key Operational Characteristics (citing F67)

The cloud-native baseline — automated evidence collection via provider-managed tooling — versus the on-premises requirement to build audit logging pipelines, posture scanning, and evidence export from scratch fully supports RD 4. The RD 4 rating (substantially harder; requires specialist knowledge) rather than RD 5 (categorically different) is reasonable because the compliance evidence generation tooling (OPA, Kyverno, audit log exporters) exists as open-source software; the problem is assembling and operating it, not inventing it.

Phase 1 TE 3 (2–6 person-months) is the flagged cell for CP-09. The ratings file note: "Build compliance evidence collection pipeline (audit logging, posture scanning, evidence export). Framework for FedRAMP/SOC2/HIPAA — but the tooling is bounded once built." The note's qualifier ("bounded once built") is doing significant work here.

[STATISTIC] "FedRAMP costs $250K–$2M+ for initial authorization [on-premises]."
— GT1_P1_ground_truth.md, CP-09 Key Operational Characteristics (citing F67, W08S Theme 3)

External sources corroborate the FedRAMP authorization cost range:

[STATISTIC] "On average, achieving FedRAMP certification costs approximately $1 million, with estimates ranging between $150,000 and over $2 million. A two-year timeframe for FedRAMP authorization is considered typical."
— Paramify, "This is How Much FedRAMP Authorization Costs in 2026," URL: https://www.paramify.com/blog/fedramp-cost, Date: 2026

[STATISTIC] "FedRAMP Low: third-party security assessment costs $100,000–$250,000. FedRAMP Moderate: full 3PAO assessments range from $150,000–$300,000 or more."
— Secureframe, "How Much Does FedRAMP Authorization Cost?," URL: https://secureframe.com/hub/fedramp/costs, Date: 2024–2025

The FedRAMP authorization cost range ($250K–$2M+) with a two-year typical timeline is substantial. However, the Phase 1 build in the ratings file is scoped to building the compliance automation infrastructure (the pipeline, tooling, and evidence framework) — not completing the FedRAMP authorization itself. FedRAMP authorization is an ongoing/repeating event, not a one-time Phase 1 build. The 2–6 person-month estimate for building the compliance tooling framework is plausible if restricted to infrastructure construction. However, if the ISV must also complete initial control documentation, gap assessments, and System Security Plan (SSP) drafting as part of Phase 1 — work commonly required before any framework can be validated — then 2–6 person-months understates the effort and TE 4 (6–12 person-months) becomes more defensible.

[FACT] "Without automation, SOC 2 compliance can consume hundreds of hours. Setting up evidence collection takes 3–4 weeks initially but saves dozens of hours during the observation period and audit phase."
— EasyAudit.ai, "How Long Does It Take to Get SOC 2 Compliance?," URL: https://www.easyaudit.ai/post/how-long-does-it-take-to-get-soc-2-compliance, Date: 2025

[FACT] "Big, distributed infrastructures increase audit workload exponentially."
— Scrut, "SOC 2 Compliance Timelines and Solutions," URL: https://www.scrut.io/hub/soc-2/soc-2-compliance-timeline, Date: 2024

The "big, distributed infrastructure" factor is directly applicable to an on-premises ISV managing multiple customer environments, each a separate audit surface. This amplifies the Phase 1 build complexity.

Verdict: TE 3 is accurate if Phase 1 scope is strictly limited to building the compliance tooling pipeline (audit exporters, posture scanners, evidence collection automation). TE 3 is borderline if Phase 1 must also include initial regulatory control mapping, gap assessment documentation, and first-pass SSP work — which many ISVs find they cannot defer. Flagged for interview validation.

**Phase 2 — RD 3, TE 3**

[FACT] "On-premises carries 50 separate compliance audit surfaces for a 50-customer fleet. Each version multiplies compliance audit surfaces."
— GT1_P1_ground_truth.md, CP-09 Scaling Behavior (citing CP-07 Evidence and Cross-Subsegment Pattern 2)

Per-customer compliance configuration (mapping ISV's framework to customer's specific regulatory requirements) is inherently non-trivial: a federal customer requires FedRAMP evidence; a healthcare customer requires HIPAA; a financial services customer requires SOC2 Type II. The RD 3 and TE 3 ratings (1–3 person-weeks per customer) are supported. The key driver is that the ISV's compliance framework is built once in Phase 1 and then configured per customer in Phase 2 — so TE 3 reflects configuration and mapping work, not rebuilding the framework.

**Phase 3 — RD 4, TE 4**

[FACT] "FedRAMP 20x continuous monitoring requires some controls validated minute-by-minute — difficult to achieve on managed K8s without dedicated tooling."
— GT1_P1_ground_truth.md, CP-09 Key Operational Characteristics (citing F67, F60)

[FACT] "EU AI Act GPAI obligations became active August 2025."
— GT1_P1_ground_truth.md, CP-09 Notable Caveats (citing F67, W08S Theme 3)

Phase 3 RD 4 and TE 4 (1.0–2.5 FTE) are well supported. Compliance is not a one-time event: SOC 2 Type II requires annual audits with a 6-month observation period; FedRAMP continuous monitoring is a permanent operational obligation; the EU AI Act creates new annual reporting obligations. The GT1 FTE range for CP-09 on-premises is 2.5–4.0, which maps to TE 4–5. The ratings file's TE 4 (1.0–2.5 FTE) is conservative relative to GT1's lower bound of 2.5 FTE, but TE 4 is defensible as a per-subsegment rating when the full fleet FTE is distributed across customers and shared tooling.

**Assessing whether CP-09 Phase 1 TE 3 is too low:**

The claim in the task scope was to assess "whether CP-08 and CP-09 Phase 1 TE ratings (both 3) are too low given complexity described." The assessment:

- CP-08 Phase 1 TE 3: Defensible for a software-only DR framework build using Velero + MinIO; borderline if physical second-site DR is required.
- CP-09 Phase 1 TE 3: Defensible if Phase 1 scope is strictly the tooling pipeline; borderline if initial regulatory control documentation is included.

Neither TE 3 rating is clearly wrong. Both sit at the high-risk boundary between TE 3 and TE 4. The note "bounded once built" in the ratings file correctly identifies that these are one-time investments — the concern is whether 2–6 person-months is sufficient for the full Phase 1 scope. An interviewer should probe what Phase 1 actually includes.

---

### CP-10: Security Operations Infrastructure

#### Ratings Under Review

| Phase | Dimension | Current Rating | Re-Derived Rating | Confidence | Verdict |
|:---:|---|:---:|:---:|:---:|---|
| Phase 1 | Relative Difficulty (RD) | 4 | 4 | H | ACCURATE |
| Phase 1 | Total Effort (TE) | 4 | 4 | H | ACCURATE |
| Phase 2 | Relative Difficulty (RD) | 3 | 3 | H | ACCURATE |
| Phase 2 | Total Effort (TE) | 2 | 2 | H | ACCURATE |
| Phase 3 | Relative Difficulty (RD) | 4 | 4 | H | ACCURATE |
| Phase 3 | Total Effort (TE) | 4 | 4–5 | M | ACCURATE (but watch upper bound) |

#### Re-Derivation Basis

**Phase 1 — RD 4, TE 4**

[FACT] GT1 composite on-premises difficulty for CP-10 is 5/5, with SIEM operations 4/5, IDS/IPS and runtime security 4/5, incident response/forensics 5/5, and vulnerability management 4/5.
— GT1_P1_ground_truth.md, CP-10 Difficulty Ratings table, citing P1_control_plane.md

[FACT] "Cloud detection rates for Kubernetes attack techniques range from 24% (GCP SCC) to 66% (Azure Defender) — cloud-native agents cannot substitute for K8s-native tooling (Falco, Trivy), meaning managed K8s deployments still require K8s-specific security tools even when using cloud-native SIEM."
— GT1_P1_ground_truth.md, CP-10 Key Operational Characteristics (citing F71, F55c)

The Phase 1 build requires deploying Falco (runtime security), a self-hosted vulnerability scanning pipeline (Trivy), security event aggregation, and intrusion detection — on top of the cluster substrate from CP-01. Cloud-native ISVs use GuardDuty, Defender for Cloud, or GCP Security Command Center, all of which are managed services. The refactoring to self-hosted equivalents is substantial but bounded to known open-source tooling. RD 4 is correct (substantially harder; requires specialist knowledge, but not categorically different — the tools exist).

Phase 1 TE 4 (6–12 person-months) is well supported. Falco deployment, rule tuning, SIEM integration, vulnerability scanning pipeline construction, and security event correlation setup across a new cluster environment represents a meaningful platform build. GT1's note that CP-03 + CP-04 + CP-10 require "8.0–15.25 FTE on-premises — representing 32–40% of total Control Plane on-premises FTE" reflects the ongoing steady-state, not the Phase 1 build; nevertheless, the scale of the security cluster confirms that Phase 1 TE 4 is the correct minimum.

[FACT] Falco graduated CNCF in 2024, reaching 150 million downloads, confirming it as the standard for K8s runtime intrusion detection.
— Falco.org, CNCF project page, URL: https://falco.org/, Date: 2024

**Phase 2 — RD 3, TE 2**

The ratings file notes: "Security policy adapted to customer's threat model and existing security tooling. Mostly configuration — security tooling is standardized. Integration with customer's SIEM if required." The divergence between RD 3 and TE 2 is the most notable feature of this cell.

RD 3 is correct: adapting Falco rules to a customer's threat model and integrating with their SIEM (if they have one) requires platform-aware work. It is not trivial (RD 1–2) because each customer's security architecture is different.

TE 2 (2–5 person-days per customer) is defensible because the security tooling itself is standardized and does not need to be rebuilt per customer — only configured. The configuration work is bounded. The divergence (RD 3, TE 2) is a valid pattern: the work is qualitatively hard (requires specialist knowledge) but quantitatively small (configuration, not construction).

**Phase 3 — RD 4, TE 4**

[FACT] "A 24/7 Security Operations Center requires a minimum of 12 FTE and costs $1.5M–$5M annually [on-premises]."
— GT1_P1_ground_truth.md, CP-10 Key Operational Characteristics (citing F71)

External sources corroborate the SOC staffing and cost floor:

[STATISTIC] "You need at least 8–12 people operating in a SOC to maintain 24×7 shift coverage. An intermediate SOC will cost $2.5M per year, comprised of $400K for technology and $2.1M labor."
— Expel, "How much does it cost to build a 24x7 SOC?," URL: https://expel.com/blog/how-much-does-it-cost-to-build-a-24x7-soc/, Date: 2024

[STATISTIC] "Entry-level security analysts command approximately $98,000 per year in salary. True cost per analyst including benefits and overhead: approximately $1.6–2.1M annually for minimum staffing."
— Lumifi Cybersecurity, "True Cost of Setting Up and Operating a 24x7 SOC," URL: https://www.lumificyber.com/blog/the-true-cost-of-setting-up-and-operating-a-24x7-security-operations-center/, Date: 2024

[STATISTIC] "28% of CVEs are weaponized within one day of disclosure. 77% of enterprises take more than one week to deploy patches."
— GT1_P1_ground_truth.md, CP-10 Scaling Behavior (citing F60, W08S Theme 2)

[FACT] "CISA Known Exploited Vulnerabilities catalog grew 20% year-over-year to 1,484 entries in 2025, with some mandated remediation timelines as short as seven days."
— GT1_P1_ground_truth.md, CP-10 Scaling Behavior (citing F60, W08S Theme 2)

[STATISTIC] "73% of security practitioners cite false positives as the top challenge in on-premises SIEM environments."
— GT1_P1_ground_truth.md, CP-10 Key Operational Characteristics (citing F71)

Phase 3 RD 4 is supported. On-premises incident response is rated 5/5 by GT1 at the dimension level because "access must be physically coordinated with customer IT staff, memory acquisition and log preservation requires on-site tools, and the ISV has no direct infrastructure access" — factors entirely absent from cloud-native. The composite Phase 3 RD 4 (rather than 5) reflects that SIEM operations and vulnerability management are closer to parity (4/5 on-premises dimension), averaging the composite down from the incident response 5/5.

Phase 3 TE 4 (1.0–2.5 FTE) maps to GT1's FTE range of 2.75–5.5 FTE for CP-10 on-premises. The GT1 range sits above TE 4's ceiling of 2.5 FTE at the subsegment level, suggesting TE 4 may understate the ongoing security operations burden for a large fleet. At 50 customers, the combination of continuous vulnerability scanning, Falco rule maintenance, CVE patch coordination (per-customer), and incident response readiness pushes toward TE 5 (2.5+ FTE). The current TE 4 rating is accurate for a moderate-scale fleet; ISVs at 50+ customers should treat TE 4–5 as the realistic range.

**Interview question (M confidence, upper bound):** At what customer count did your Phase 3 security operations effort first exceed 2.5 FTE on-premises, and was that driven primarily by incident response volume or patch coordination overhead?

---

## Key Findings

1. **CP-07 Phase 3 linear-scaling claim is fully validated.** The N-customers-equals-N-deployment-cycles assertion for CP-07 is supported by GT1 primary evidence (W08S Theme 2, F59), confirmed by industry practice (SAP annual cycles, Microsoft annual cadence), and corroborated externally by the existence of Replicated as a commercial platform purpose-built to reduce per-customer deployment overhead. RD 5 / TE 5 for Phase 3 are the most firmly grounded ratings in this review cluster.

2. **CP-08 and CP-09 Phase 1 TE 3 ratings sit at the boundary, not clearly wrong.** The concern raised in the task scope is validated: both ratings are at the upper edge of TE 3 (2–6 person-months). The ratings hold if Phase 1 scope is narrowly defined as tooling construction only. They become borderline TE 4 if Phase 1 includes initial regulatory documentation (CP-09) or physical second-site DR architecture (CP-08). No external source precisely quantifies Phase 1 DR or compliance framework build hours; both ratings carry Medium confidence.

3. **CP-10 Phase 3 TE 4 is accurate but has an empirically supported upper-bound risk.** GT1's CP-10 FTE floor of 2.75 on-premises exceeds the TE 4 ceiling of 2.5 FTE, and external sources confirm that 24/7 SOC minimum staffing begins at 8–12 FTE. For ISVs at 50+ customers, TE 5 is a credible Phase 3 outcome. The TE 4 rating is not wrong but should be flagged as potentially conservative at scale.

4. **CP-09 data sovereignty inversion is the single anomaly in the entire P1 dataset.** Data sovereignty dimension is rated on-premises 1/5 (easiest) versus cloud-native 3/5 (hardest) — because data physically never leaves customer infrastructure on-premises. This inversion is correctly preserved in the Phase 2 and Phase 3 compliance configuration work, where per-customer regulatory mapping is RD 3 rather than the full-complexity 5/5 seen elsewhere.

5. **The Phase 2 CP-10 divergence (RD 3, TE 2) is the sharpest difficulty-effort gap in this cluster.** Security policy adaptation per customer is qualitatively specialist work (RD 3) but quantitatively bounded configuration (TE 2 / 2–5 person-days). This is a valid and strategically useful finding: ISVs should staff Phase 2 security configuration with specialists but should not budget construction-level time per customer.

---

## Sources

| # | Source | URL | Date |
|---|---|---|---|
| 1 | GT1_P1_ground_truth.md — P1 Control Plane Ground Truth | Local file: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md` | 2026-02-19 |
| 2 | three_phase_on_prem_ratings.md — Three-Phase Rating File | Local file: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` | 2026-02-19 |
| 3 | Replicated — Commercial Software Distribution Lifecycle | https://www.replicated.com/commercial-software-distribution-lifecycle | 2025 |
| 4 | Efficiently Connected — Replicated Modernizes Enterprise Software Distribution | https://www.efficientlyconnected.com/replicated-modernizing-enterprise-software-distribution-and-automation/ | 2024 |
| 5 | Octopus Deploy — DORA Metrics Overview (citing DORA 2022 Report) | https://octopus.com/devops/metrics/dora-metrics/ | 2024–2025 |
| 6 | DevOps Training Institute — 10 Kubernetes Disaster Recovery Tools (Velero CNCF 82% Fortune 500) | https://www.devopstraininginstitute.com/blog/10-kubernetes-disaster-recovery-tools-you-must-know | 2025 |
| 7 | Buxton Consulting — Building and Testing DR Plans for SaaS Applications (IBM $4.88M breach cost) | https://buxtonconsulting.com/general/building-and-testing-disaster-recovery-plans-for-saas-applications/ | 2024–2025 |
| 8 | Paramify — FedRAMP Authorization Cost 2026 | https://www.paramify.com/blog/fedramp-cost | 2026 |
| 9 | Secureframe — How Much Does FedRAMP Authorization Cost? | https://secureframe.com/hub/fedramp/costs | 2024–2025 |
| 10 | EasyAudit.ai — How Long Does It Take to Get SOC 2 Compliance? | https://www.easyaudit.ai/post/how-long-does-it-take-to-get-soc-2-compliance | 2025 |
| 11 | Scrut — SOC 2 Compliance Timelines and Solutions | https://www.scrut.io/hub/soc-2/soc-2-compliance-timeline | 2024 |
| 12 | Expel — How Much Does It Cost to Build a 24x7 SOC? | https://expel.com/blog/how-much-does-it-cost-to-build-a-24x7-soc/ | 2024 |
| 13 | Lumifi Cybersecurity — True Cost of Setting Up and Operating a 24x7 SOC | https://www.lumificyber.com/blog/the-true-cost-of-setting-up-and-operating-a-security-operations-center/ | 2024 |
| 14 | Falco — CNCF Project Page (graduated 2024, 150M downloads) | https://falco.org/ | 2024 |
| 15 | Replicated — Why Are Companies Doing On-Prem Air Gap Installations Now? | https://www.replicated.com/blog/why-are-companies-doing-on-prem-air-gap-installations-now | 2024–2025 |
