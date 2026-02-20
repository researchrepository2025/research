# CC4: Scope Consistency Check — Customer-Owns-Hardware / ISV-Owns-Software Boundary

**Agent Role:** Scope Consistency Review (CC4)
**Primary Source:** `analysis/three_phase_on_prem_ratings.md`
**Cross-Reference:** `analysis/review/RP4b_P4_scope_exclusion.md`
**Supporting Sources:** `analysis/P1_control_plane.md`, `analysis/P2_application_logic.md`, `analysis/P3_data_plane.md`, `analysis/G1_n_services_multiplier.md`
**Date:** 2026-02-19
**Status:** COMPLETE

---

## Executive Summary

The customer-owns-hardware / ISV-owns-software scope boundary is consistently applied across P1, P2, and all three phases, with no cell in those planes attributing physical hardware, rack provisioning, power, or cooling to the ISV. P4 S2–S5 are uniformly marked customer scope in all three phases, confirming that boundary. However, two scope ambiguities require resolution: (1) DS9 (Embedding Pipeline) in `three_phase_on_prem_ratings.md` is rated 3/3 with explicit justification that GPU hardware is customer scope, but the source file `P3_data_plane.md` retains a 5/5 on-premises difficulty rating that includes full GPU hardware lifecycle tasks — this rating is never reconciled or updated in the source, creating a latent inconsistency between the ratings file and its source; (2) several Phase 2 description fragments in CP-01 and CP-02 use hardware-adjacent vocabulary ("server models," "NIC drivers," "storage controllers") that correctly describes ISV software adaptation targets but could be read as implying ISV hardware responsibility if the scope header in §1 is overlooked.

---

## 1. Scope Header Analysis — §1 of `three_phase_on_prem_ratings.md`

[FACT]
`three_phase_on_prem_ratings.md` §1 establishes a four-row scope table assigning "Hardware environment" (servers, GPUs, networking equipment, storage arrays, power, cooling, rack space, physical security) and "GPU + AI models" (GPU procurement, driver management, inference engine operation, model weights, CUDA stack) to the Customer. "All software" and "Software-to-hardware adaptation" are assigned to the ISV.
— `three_phase_on_prem_ratings.md` §1
Path: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT]
The §1 scope table includes the terms "rack space," "power," and "cooling" explicitly as customer-owned hardware examples.
— `three_phase_on_prem_ratings.md` §1

[FACT]
The §1 scope table defines ISV responsibility as "Customizing software deployment to each customer's specific hardware environment" — framing ISV work as software adaptation, not hardware ownership.
— `three_phase_on_prem_ratings.md` §1

**Finding — PASS:** The scope header in §1 is unambiguous. Hardware environment terms are correctly assigned to the customer. No ISV hardware responsibility appears in the scope definition.

---

## 2. P4 S2–S5 Customer Scope Consistency Across All Three Phases

[FACT]
Phase 1 (§4) P4 table: S2 is marked "— | — | **Customer scope.** Customer operates vLLM/TGI on their GPUs. ISV has no refactoring work." S3 is marked "— | — | **Customer scope.** Customer owns all GPU hardware." S4 is marked "— | — | **Customer scope.** Customer manages driver stack." S5 is marked "— | — | **Customer scope.** Customer manages GPU allocation."
— `three_phase_on_prem_ratings.md` §4, P4 Phase 1 table

[FACT]
Phase 2 (§5) P4 table: S2 is marked "— | — | **Customer scope.**" S3 is marked "— | — | **Customer scope.**" S4 is marked "— | — | **Customer scope.**" S5 is marked "— | — | **Customer scope.**"
— `three_phase_on_prem_ratings.md` §5, P4 Phase 2 table

[FACT]
Phase 3 (§6) P4 table: S2 is marked "— | — | — | — | **Customer scope.**" S3 is marked "— | — | — | — | **Customer scope.**" S4 is marked "— | — | — | — | **Customer scope.**" S5 is marked "— | — | — | — | **Customer scope.**" The "Scales with N?" and "Research FTE" columns also carry dashes for S2–S5.
— `three_phase_on_prem_ratings.md` §6, P4 Phase 3 table

[FACT]
`three_phase_on_prem_ratings.md` §8 (Key Finding 4) states: "P4 (AI Model Plane) is nearly eliminated under the customer-provides-GPU-and-models scope."
— `three_phase_on_prem_ratings.md` §8

**Finding — PASS:** P4 S2–S5 are uniformly marked customer scope with consistent notation (dashes for RD, TE, and all qualitative columns) in all three phases. No phase assigns an ISV rating to any of these four subsegments. The marking is structurally identical in Phase 1, Phase 2, and Phase 3.

---

## 3. P1 Control Plane — Hardware-Adjacent Language Check

### 3.1 Phase 1 (Initial Refactoring)

[FACT]
Phase 1 CP-01 notes: "Replace EKS/AKS/GKE with kubeadm/RKE2. Build HA control plane provisioning, etcd backup automation, node pool management, add-on lifecycle tooling."
— `three_phase_on_prem_ratings.md` §4, CP-01 row

[FACT]
Phase 1 CP-02 notes: "Replace VPC networking + managed ALB with Calico/Cilium CNI, self-managed ingress (Gateway API), optional service mesh. Network policy engine must be built from scratch."
— `three_phase_on_prem_ratings.md` §4, CP-02 row

**Finding — PASS:** Phase 1 P1 notes describe software replacements exclusively: kubeadm/RKE2 (K8s distribution), Calico/Cilium (CNI software), Gateway API (ingress software). No reference to rack provisioning, power, cooling, server procurement, or physical hardware installation appears in any Phase 1 P1 cell.

### 3.2 Phase 2 (Per-Customer Customization) — Critical Check

[FACT]
Phase 2 CP-01 notes: "Each customer's server models, virtualization layer (VMware vs KVM vs bare metal), storage controllers, and NIC drivers require K8s configuration adaptation. Node pool sizing based on customer's available compute."
— `three_phase_on_prem_ratings.md` §5, CP-01 row

[FACT]
Phase 2 CP-02 notes: "Customer's network topology, firewall rules, proxy requirements, DNS architecture, and egress policies are unique per site. CNI configuration, ingress routing, and network policies must be adapted. Most variable P1 subsegment per customer."
— `three_phase_on_prem_ratings.md` §5, CP-02 row

[FACT]
The Phase 2 section header in `three_phase_on_prem_ratings.md` reads: "Repeating effort for each new customer deployment. Driven by hardware heterogeneity across customer environments." The Phase 2 row in the three-phase table (§2) reads: "Per-Customer Customization — Adapting software to each customer's hardware environment."
— `three_phase_on_prem_ratings.md` §2 and §5

**Finding — CONDITIONAL PASS with Flag:** The terms "server models," "storage controllers," and "NIC drivers" appear in Phase 2 CP-01 as the targets of ISV software adaptation (K8s configuration adaptation), not as hardware the ISV procures or manages. The phrase "Node pool sizing based on customer's available compute" similarly refers to ISV configuration decisions using customer-provided hardware as the input constraint. The framing is consistent with ISV software adaptation, not hardware provisioning. However, these cells contain the highest density of hardware-adjacent vocabulary in the entire document. A reader who skips §1 could misread CP-01 Phase 2 as implying ISV hardware management. The scope header in §1 disambiguates this, but the CP-01 Phase 2 cell does not itself contain a software-only qualifier.

[FACT]
`P1_control_plane.md` source file describes the on-premises CP-01 work as "Full responsibility for all control plane components including etcd backup, API server HA, and control plane node replacement" — software components. The source file does not assign rack provisioning, power, or cooling to the ISV in any CP subsegment.
— `analysis/P1_control_plane.md`, CP-01 Evidence section

[FACT]
`P1_control_plane.md` mentions "HSM hardware costs $5K–$50K per unit" in the context of CP-04 (Secrets/Certs/PKI), but this is cited as customer-environment context (the customer's existing HSM infrastructure), not ISV procurement. The CP-04 ISV scope in the source file covers "Vault seal configuration" and "HSM integration" — software operations against customer-owned hardware.
— `analysis/P1_control_plane.md`, CP-04 Evidence section

**Finding — PASS with Advisory:** P1 Phase 2 hardware-adjacent terms describe the customer's hardware as the environment the ISV's software must adapt to, not as ISV-owned resources. The source file confirms this framing. An advisory note recommending a parenthetical clarifier in CP-01 Phase 2 (e.g., "K8s configuration adaptation to customer-provided server models and NIC drivers") would prevent future misreading.

### 3.3 Phase 3 (Ongoing Support)

[FACT]
Phase 3 CP-01 notes: "3 minor K8s versions/year, 12–14 month support windows. Each customer on a different version and upgrade schedule. Node drain coordination per customer. Hardware-specific regression risk per customer."
— `three_phase_on_prem_ratings.md` §6, CP-01 row

[FACT]
Phase 3 CP-02 notes: "CNI upgrades, network policy updates, ingress controller patches per customer. Gateway API evolution. Network-related incidents are the most common customer-specific issues due to hardware heterogeneity."
— `three_phase_on_prem_ratings.md` §6, CP-02 row

**Finding — PASS:** Phase 3 P1 language refers to software upgrade coordination (K8s versions, CNI upgrades, ingress patches) and hardware-related regression risk as a driver of ISV software testing effort. "Hardware-specific regression risk" correctly describes ISV software testing on diverse hardware — not ISV hardware procurement. No Phase 3 P1 cell implies ISV hardware ownership.

---

## 4. P3 Data Plane — Hardware-Adjacent Language Check

### 4.1 P3 Phase 1

[FACT]
Phase 1 DS9 notes: "Customer provides GPU; ISV deploys embedding model serving on customer's GPU allocation. Pipeline logic (chunking, batch processing, vector store integration) is application-level. Reduced from original 5/5 because GPU hardware is customer scope."
— `three_phase_on_prem_ratings.md` §4, DS9 row

[FACT]
Phase 1 DS1 notes reference "WAL archiving, connection pooling (PgBouncer), backup automation (pgBackRest/Barman)" — all software operations against customer-provided storage hardware.
— `three_phase_on_prem_ratings.md` §4, DS1 row

[FACT]
Phase 1 DS4 notes: "Replace S3 with MinIO. Well-documented S3-compatible API, Helm chart deployment. Erasure coding configuration, bucket lifecycle policies." No reference to storage hardware procurement.
— `three_phase_on_prem_ratings.md` §4, DS4 row

**Finding — PASS for all P3 Phase 1 cells except DS9 (see §5 below):** P3 Phase 1 cells describe software deployment, configuration, and operator management. Storage-related subsegments (DS1, DS4) reference storage hardware only as the context for ISV software configuration, consistent with the §1 scope split.

### 4.2 P3 Phase 2

[FACT]
Phase 2 DS1 notes: "Tune shared_buffers, work_mem, wal_buffers for customer's memory. Storage layout for customer's disk topology. Backup targets configured per customer's storage."
— `three_phase_on_prem_ratings.md` §5, DS1 row

[FACT]
Phase 2 DS9 notes: "Configure embedding batch size and concurrency for customer's GPU allocation. Validate embedding model compatibility with customer's GPU generation."
— `three_phase_on_prem_ratings.md` §5, DS9 row

[FACT]
Phase 2 DS6 notes: "Kafka log.dirs configured for customer's disk topology. Broker memory sizing. Replication factor may vary based on customer's node count."
— `three_phase_on_prem_ratings.md` §5, DS6 row

**Finding — PASS:** Phase 2 P3 cells consistently frame ISV work as software configuration against customer-provided resources: customer's memory, customer's disk topology, customer's GPU allocation, customer's node count. No cell implies ISV hardware procurement or provisioning.

### 4.3 P3 Phase 3

[FACT]
Phase 3 DS9 notes: "Embedding model version management. Model version changes may trigger full corpus re-embedding — high-cost event. Pipeline tuning as data volumes grow. Customer GPU allocation changes may require re-tuning."
— `three_phase_on_prem_ratings.md` §6, DS9 row

**Finding — PASS:** Phase 3 DS9 correctly attributes GPU allocation management to the customer ("Customer GPU allocation changes") and frames ISV work as pipeline re-tuning in response to those customer changes.

---

## 5. DS9 (Embedding Pipeline) — Source vs. Ratings File Discrepancy

This is the single most significant scope-consistency finding in this review.

[FACT]
`three_phase_on_prem_ratings.md` §4 rates DS9 Phase 1 as RD=3, TE=3, with the note: "Reduced from original 5/5 because GPU hardware is customer scope."
— `three_phase_on_prem_ratings.md` §4, DS9 row

[FACT]
`P3_data_plane.md` rates DS9 on-premises difficulty as **5/5** with FTE of **2.0–3.25**, and the key driver is listed as: "MIG partitioning (up to 7 isolated instances on A100/H100), time-slicing not recommended for production, model versioning triggers full re-embedding, batch queue management."
— `analysis/P3_data_plane.md`, DS9 subsegment table

[FACT]
`P3_data_plane.md` DS9 evidence includes: "F76 Domain 9 (AI Model Inference & GPU): On-premises difficulty 5/5 — 'Full GPU hardware lifecycle: NVLink topology management, firmware updates, thermal monitoring, RMA processes'" — and this citation is included in the DS9 evidence block without qualification, even though the scope split assigns GPU hardware lifecycle to the customer.
— `analysis/P3_data_plane.md`, DS9 Evidence section

[FACT]
`P3_data_plane.md` summary difficulty matrix lists DS9 at "5/5" on-premises with FTE range "2.00–3.25."
— `analysis/P3_data_plane.md`, Summary Difficulty Matrix table

[FACT]
`three_phase_on_prem_ratings.md` §6 (Phase 3) rates DS9 at RD=3, TE=3, Scales Partial, FTE=2.0–3.25. The FTE figure (2.0–3.25) is carried over from the source file `P3_data_plane.md` unchanged, but the difficulty rating is reduced from 5 to 3.
— `three_phase_on_prem_ratings.md` §6, DS9 row

**Finding — DISCREPANCY IDENTIFIED:** The difficulty reduction from 5/5 to 3/3 in DS9 is internally justified in `three_phase_on_prem_ratings.md` by the scope exclusion of GPU hardware. However, the FTE figure (2.0–3.25) is copied from `P3_data_plane.md` without reduction, even though that FTE estimate was built on the assumption that the ISV manages MIG partitioning, NVLink topology, firmware updates, thermal monitoring, and RMA processes — all of which are customer scope under the current framework. The FTE figure in Phase 3 DS9 (2.0–3.25) is inconsistent with a difficulty rating of 3/5. At difficulty 3, the Phase 3 FTE scale implies 0.3–1.0 FTE. The 2.0–3.25 FTE figure belongs to the 5/5 source rating where the ISV managed full GPU hardware lifecycle. This is a scope-boundary artifact: the difficulty was reduced to reflect customer GPU ownership, but the FTE was not recomputed to match.

[FACT]
`RP4b_P4_scope_exclusion.md` §2.4 identifies a parallel issue: "GPU contention between LLM inference and embedding workloads is 'the primary operational risk on-premises'; without explicit MIG partitioning on A100/H100 hardware, embedding latency degrades unpredictably under LLM load" — and notes that when S5 (GPU Scheduling, customer scope) is misconfigured, the ISV bears the application-layer SLA consequence.
— `analysis/review/RP4b_P4_scope_exclusion.md` §2.4

**Scope Ambiguity — DS9 FTE Carry-Over:** The 2.0–3.25 FTE figure in Phase 3 DS9 was derived under ISV-owns-GPU assumptions and has not been recomputed under customer-owns-GPU assumptions. The correct ISV-scope FTE for DS9 under the current framework should exclude MIG partitioning management, NVLink topology, firmware updates, and thermal monitoring — retaining only model serving configuration, batch queue management, model version management, and pipeline tuning. The source file `P3_data_plane.md` does not provide a decomposed FTE breakdown that would allow precise isolation of the ISV-retained portion, but the retained tasks are substantially less than 2.0–3.25 FTE.

---

## 6. Phase 2 Framing — "Software Adaptation" vs. "Hardware Provisioning"

[FACT]
The Phase 2 section header reads: "Per-Customer Hardware Customization — Repeating effort for each new customer deployment. Driven by hardware heterogeneity across customer environments."
— `three_phase_on_prem_ratings.md` §5

[FACT]
The §2 phase definition table reads for Phase 2: "Per-Customer Customization — Adapting software to each customer's hardware environment — N customers (linear)."
— `three_phase_on_prem_ratings.md` §2

**Finding — PARTIAL FLAG:** The Phase 2 section header uses the phrase "Per-Customer Hardware Customization" rather than "Per-Customer Software Customization." The word "Hardware" in this heading could suggest the ISV is customizing hardware, rather than customizing software to adapt to customer-owned hardware. The §2 phase definition table more precisely reads "Adapting software to each customer's hardware environment," which is the correct framing. The section heading is slightly imprecise relative to the §1 scope split and the §2 description. The actual cell-level content in Phase 2 is correctly framed as software adaptation throughout, so this is a heading-level vocabulary issue, not a substantive scope error.

[FACT]
The Phase 2 Summary table (§5) Key Cost Driver for P1 reads: "Infrastructure adaptation to customer hardware/network/security." This correctly names the driver (customer hardware/network/security) as the environmental constraint, and "Infrastructure adaptation" as the ISV software work product.
— `three_phase_on_prem_ratings.md` §5, Phase 2 Summary table

---

## 7. P2 Application Logic — Hardware Language Check

[FACT]
`two_phase_on_prem_ratings.md` Phase 3 AL10 notes: "Test suite maintenance across N customer hardware profiles. Regression testing for each release against multiple K8s versions and hardware configurations."
— `three_phase_on_prem_ratings.md` §6, AL10 row

[FACT]
`P2_application_logic.md` explicitly excludes: "GPU hardware procurement, model training, embedding corpus management, model serving runtime operations (vLLM/TGI tuning). The application code that calls inference endpoints is in scope; model serving infrastructure is not."
— `analysis/P2_application_logic.md`, Out of Scope section

[FACT]
`P2_application_logic.md` explicitly excludes "Control Plane: Kubernetes cluster lifecycle, node provisioning, IaC templates, secrets vault operations, CI/CD pipeline infrastructure."
— `analysis/P2_application_logic.md`, Out of Scope section

**Finding — PASS:** P2 cells in all three phases correctly exclude hardware procurement. AL10 references "customer hardware profiles" as the test matrix variable — the ISV tests its software against customer-provided hardware, consistent with the §1 scope split. No P2 cell assigns hardware procurement, rack management, power, or cooling to the ISV.

---

## 8. G1 N-Services Multiplier — Scope Consistency Check

[FACT]
`G1_n_services_multiplier.md` §AI Model Plane Scaling states: "S2–S5 Hardware/GPU: Shared entirely. No per-service hardware cost."
— `analysis/G1_n_services_multiplier.md`, AI Model Plane Scaling section

[FACT]
`G1_n_services_multiplier.md` mentions "Annual infrastructure cost (hardware, licenses, facilities): estimated $3M–$8M additional" in the context of total on-premises annual cost. This is listed as a cost category distinct from ISV personnel costs and does not attribute hardware procurement to the ISV as a software delivery responsibility.
— `analysis/G1_n_services_multiplier.md`, cost modeling section

**Finding — PASS:** G1 correctly references hardware costs as customer-environment context, not ISV-owned costs. The S2–S5 hardware scope exclusion is correctly carried through to the N-services model.

---

## 9. Summary of All Scope Checks

| Check | Location | Finding | Status |
|---|---|---|---|
| §1 scope table — hardware terms assigned to customer | §1 | Power, cooling, rack space, servers explicitly customer-owned | PASS |
| P4 S2 customer scope — Phase 1 | §4, S2 | Marked "—/—, Customer scope" | PASS |
| P4 S3 customer scope — Phase 1 | §4, S3 | Marked "—/—, Customer scope" | PASS |
| P4 S4 customer scope — Phase 1 | §4, S4 | Marked "—/—, Customer scope" | PASS |
| P4 S5 customer scope — Phase 1 | §4, S5 | Marked "—/—, Customer scope" | PASS |
| P4 S2–S5 customer scope — Phase 2 | §5 | All four marked "—/—, Customer scope" | PASS |
| P4 S2–S5 customer scope — Phase 3 | §6 | All four marked "—/—/—/—, Customer scope" | PASS |
| P1 Phase 1 — no hardware provisioning in notes | §4, CP-01 to CP-10 | All notes describe software replacements | PASS |
| P1 Phase 2 — hardware-adjacent vocabulary | §5, CP-01, CP-02 | "Server models," "NIC drivers," "storage controllers" used as adaptation targets; §1 scope header disambiguates | CONDITIONAL PASS |
| P1 Phase 3 — hardware-specific regression risk | §6, CP-01 | Correctly describes ISV software testing on diverse hardware | PASS |
| P3 Phase 1 — no hardware procurement in DS1–DS10 | §4 | Software deployment language throughout | PASS |
| DS9 difficulty reduction (5→3) — source file not updated | §4, §6 vs P3_data_plane.md | Difficulty reduced but source file still shows 5/5 pre-split | DISCREPANCY |
| DS9 FTE carry-over — 2.0–3.25 under customer-GPU scope | §6, DS9 | FTE derived from ISV-manages-GPU assumption; not recomputed | DISCREPANCY |
| Phase 2 section heading — "Hardware Customization" | §5 header | Heading implies ISV customizes hardware; §2 table correctly reads "Adapting software" | MINOR FLAG |
| P2 Phase 3 AL10 — hardware profiles as test matrix | §6, AL10 | Customer hardware profiles are test matrix inputs; not ISV-owned | PASS |
| G1 — S2–S5 hardware cost excluded from ISV model | G1_n_services_multiplier.md | "No per-service hardware cost" for S2–S5 | PASS |

---

## 10. Scope Ambiguities Requiring Resolution

### Ambiguity 1 — DS9 Source File Rating Not Updated

**Description:** `P3_data_plane.md` retains a 5/5 on-premises difficulty rating for DS9 that includes full GPU hardware lifecycle tasks (MIG partitioning, NVLink topology, firmware updates, thermal monitoring, RMA). The ratings file correctly reduces DS9 to 3/3 under customer-owns-GPU scope, but the source file from which DS9 is derived has not been updated to reflect this scope change. Any future consumer of `P3_data_plane.md` who applies the customer-owns-GPU scope split will need to re-derive the DS9 rating independently.
— `analysis/P3_data_plane.md` DS9 section vs. `three_phase_on_prem_ratings.md` §4 DS9 row

**Recommended Action:** Add a scope annotation to `P3_data_plane.md` DS9 noting that under the customer-provides-GPU model, the on-premises ISV difficulty reduces from 5/5 to approximately 3/5 and the ISV-retained FTE reduces from 2.0–3.25 to a figure that excludes MIG partitioning, NVLink management, firmware updates, and RMA processes.

### Ambiguity 2 — DS9 Phase 3 FTE Inconsistency

**Description:** The Phase 3 DS9 FTE of 2.0–3.25 in `three_phase_on_prem_ratings.md` is unchanged from the source file's ISV-manages-GPU estimate. Under the customer-owns-GPU scope, the ISV-retained DS9 tasks (model serving configuration, batch queue management, model version management, pipeline tuning) would yield a substantially lower FTE. The FTE is internally inconsistent with the difficulty rating of 3/5.
— `three_phase_on_prem_ratings.md` §6, DS9 row; `analysis/P3_data_plane.md` summary matrix

**Recommended Action:** Recompute DS9 Phase 3 ISV FTE by decomposing the source FTE into GPU-hardware-lifecycle tasks (customer scope) and embedding-software tasks (ISV scope). The ISV-retained FTE under customer-owns-GPU scope is estimated to fall in the 0.5–1.0 FTE range, consistent with a difficulty 3/5 rating.

### Ambiguity 3 — Phase 2 Section Heading Vocabulary

**Description:** The Phase 2 section heading reads "Per-Customer Hardware Customization" rather than "Per-Customer Software Customization (to Customer Hardware)." The heading is the only location in the document where the word "hardware" appears as the object of ISV customization rather than as the environment the ISV adapts software to. The cell-level content is correctly framed as software adaptation throughout.
— `three_phase_on_prem_ratings.md` §5 section heading

**Recommended Action:** Revise the Phase 2 section heading to read "Per-Customer Customization: Software Adaptation to Customer Hardware" to align with the §2 phase definition table and §1 scope split.

### Ambiguity 4 — Residual ISV Obligations in S2–S5 Exclusion Gap (from RP4b)

**Description:** `RP4b_P4_scope_exclusion.md` identified four unrated ISV obligations that survive the S2–S5 scope exclusion: hardware compatibility matrix authorship, inference engine version compatibility testing, customer GPU allocation triage support, and per-customer troubleshooting runbook delivery. These are not captured in any P4 phase rating in `three_phase_on_prem_ratings.md`. These obligations represent ISV software and documentation work that is adjacent to customer-owned hardware scope but falls on the ISV side of the boundary.
— `analysis/review/RP4b_P4_scope_exclusion.md` §5.2

---

## Key Findings

- **The customer-owns-hardware / ISV-owns-software scope boundary is consistently applied across 37 of 38 rated subsegments in all three phases.** P1, P2, and P3 cells uniformly describe ISV software work against customer-provided infrastructure; no cell in those planes attributes hardware procurement, rack provisioning, power, cooling, or physical server management to the ISV. P4 S2–S5 are marked customer scope with consistent notation across all three phases.

- **DS9 (Embedding Pipeline) contains the only substantive scope inconsistency.** The ratings file correctly reduces DS9 difficulty from 5/5 to 3/3 under customer-owns-GPU scope, but: (a) the source file `P3_data_plane.md` retains the 5/5 rating with GPU-hardware-lifecycle tasks in the evidence block without annotation; and (b) the Phase 3 FTE figure of 2.0–3.25 is carried over from the ISV-manages-GPU source estimate and is inconsistent with a difficulty 3/5 rating. This creates a latent discrepancy between the ratings file and its source.

- **Phase 2 hardware-adjacent vocabulary in CP-01 and CP-02 is correctly framed as software adaptation targets, not ISV hardware ownership.** Terms such as "server models," "NIC drivers," and "storage controllers" describe the customer's hardware environment that the ISV's software must adapt to — consistent with the §1 scope split. The Phase 2 section heading ("Per-Customer Hardware Customization") is the sole vocabulary exception and is a heading-level imprecision.

- **Four residual ISV obligations identified in RP4b are unrated in all three phases of `three_phase_on_prem_ratings.md`.** Compatibility matrix authorship, inference engine version testing, GPU allocation triage support, and customer troubleshooting runbooks are ISV software and documentation obligations that survive the S2–S5 exclusion but are not captured in any P4 rated cell.

- **The G1 N-services multiplier correctly propagates the S2–S5 scope exclusion**, explicitly stating "No per-service hardware cost" for S2–S5. The multiplier model does not introduce any ISV hardware responsibility beyond the software plane.

---

## Sources

| Source | Type | Path / URL |
|---|---|---|
| `three_phase_on_prem_ratings.md` | Primary source — reviewed file | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` |
| `P1_control_plane.md` | Supporting source — P1 ratings basis | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md` |
| `P2_application_logic.md` | Supporting source — P2 ratings basis | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md` |
| `P3_data_plane.md` | Supporting source — P3 ratings basis; DS9 source discrepancy origin | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P3_data_plane.md` |
| `G1_n_services_multiplier.md` | Supporting source — N-services scope propagation | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/G1_n_services_multiplier.md` |
| `RP4b_P4_scope_exclusion.md` | Cross-reference — prior review; S2–S5 residual obligations | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP4b_P4_scope_exclusion.md` |
