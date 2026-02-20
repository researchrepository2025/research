# RP1a: P1 Infrastructure Core Review
## CP-01, CP-02, CP-03 — Three-Phase Rating Accuracy Assessment

**Review Date:** 2026-02-19
**Reviewer Scope:** CP-01 (K8s Cluster Lifecycle), CP-02 (Network Fabric / Ingress / Mesh), CP-03 (IAM / RBAC)
**Ratings File Under Review:** `analysis/three_phase_on_prem_ratings.md`
**Primary Ground Truth:** `analysis/review/GT1_P1_ground_truth.md` (source: `analysis/P1_control_plane.md`, dated 2026-02-19)
**Reference Baseline:** Mid-size ISV, 50 enterprise customers, 3–5 clusters

---

## Executive Summary

The three-phase ratings for CP-01, CP-02, and CP-03 are largely accurate and well-supported by the GT1 ground truth data. CP-01 Phase 1 (RD 5 / TE 5) and CP-02 Phase 1 (RD 5 / TE 4) are confirmed by the source file's composite on-premises ratings of 5/5 and corroborated by external evidence on Kubernetes distribution pricing disruption and Ingress NGINX EOL migration scope. The most material finding is that CP-03 Phase 3 Total Effort is rated 4, which exceeds the GT1 FTE data's implied ceiling, warranting a downward adjustment to TE 3; the partial-scaling classification for CP-03 Phase 3 is accurate and requires no change. All three subsegments exhibit the expected pattern: Phase 2 per-customer ratings are plausible but carry Medium confidence due to limited empirical data on hardware heterogeneity impact, and specific interview questions are provided below to validate these estimates.

---

## CP-01: Kubernetes Cluster Lifecycle Management

### Phase 1 — Initial Refactoring

**Rating under review:** RD 5 / TE 5

**Current rating:** RD 5 / TE 5 (GT1 source: `GT1_P1_ground_truth.md`, CP-01 section)

**Re-derived rating (RD):**

GT1 records the CP-01 on-premises composite difficulty as 5/5, with four sub-dimensions (control plane operations, node pool lifecycle, add-on ecosystem management, version currency) all rated 5/5 on-premises versus 1–2/5 on cloud-native. (`GT1_P1_ground_truth.md`, CP-01 Difficulty Ratings table) The Phase 1 refactoring task — replacing EKS/AKS/GKE with kubeadm or RKE2, building HA control plane provisioning, etcd backup automation, node pool management, and add-on lifecycle tooling — is the single foundational build from which all other CP subsegments depend. (`GT1_P1_ground_truth.md`, CP-01 Dependencies: "CP-01 is the foundational substrate for CP-02 through CP-10.") External sources confirm that provisioning vanilla Kubernetes with kubeadm requires substantially more effort than cloud-managed alternatives, with no "batteries included" tooling. (https://arxiv.org/html/2407.01620v1) Re-derived RD: **5**.

**Re-derived rating (TE):**

GT1 records the on-premises FTE range for CP-01 as 3.0–6.0 FTE annually (including upgrade coordination per customer). (`GT1_P1_ground_truth.md`, CP-01 FTE Ranges) At TE scale reference, TE 5 = "Very High" defined as 12+ person-months one-time effort for Phase 1. The build of HA control plane provisioning, etcd backup automation, node pool management, add-on lifecycle tooling, and version upgrade automation across heterogeneous hardware environments is plausibly a 12+ person-month effort for a first-time build. The SUSE Rancher CPU-based pricing increase of 4–9x in 2025 and VMware post-Broadcom cost increases of 8–15x have eliminated previously dominant distribution paths, forcing ISVs to evaluate and potentially rebuild their K8s distribution toolchain during Phase 1. (`GT1_P1_ground_truth.md`, CP-01 Notable Caveats; https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025) Re-derived TE: **5**.

**Confidence:** High — GT1 sub-dimension ratings all support 5/5; external sources corroborate distribution disruption and foundational build scope.

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Hardware Customization

**Rating under review:** RD 4 / TE 4

**Current rating:** RD 4 / TE 4 (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 2 table)

**Re-derived rating (RD):**

Phase 2 for CP-01 requires adapting K8s configuration to each customer's server models, virtualization layer (VMware vs KVM vs bare metal), storage controllers, and NIC drivers. (`analysis/three_phase_on_prem_ratings.md`, CP-01 Phase 2 notes) GT1 confirms that hardware-specific regression risk exists per customer during upgrade coordination. (`GT1_P1_ground_truth.md`, CP-01 Scaling Behavior) The GT1 composite rating of 5/5 on-premises reflects steady-state difficulty; Phase 2 per-customer adaptation is a narrower scope than the full lifecycle management captured in that 5/5 rating — it excludes initial build (Phase 1) and ongoing upgrades (Phase 3). A rating of 4 (High: "Substantially harder; requires specialist knowledge") is appropriate because each customer's hypervisor and hardware profile introduces genuine unknown variables. External sources confirm that CNI choice is operationally significant on-premises and cannot be abstracted away from hardware topology. (https://blog.devops.dev/stop-using-the-wrong-cni-flannel-vs-calico-vs-cilium-in-2025-c11b42ce05a3) Re-derived RD: **4**.

**Re-derived rating (TE):**

Phase 2 TE 4 maps to "3–6 person-weeks per customer" at the TE scale reference. (`analysis/three_phase_on_prem_ratings.md`, Rating Scales table) GT1 does not provide a direct per-customer FTE figure for CP-01 Phase 2 adaptation specifically; the 3.0–6.0 FTE figure is for Phase 3 ongoing operations, not the per-customer initial setup. (`GT1_P1_ground_truth.md`, CP-01 FTE Ranges) The Phase 2 summary in the ratings file estimates total per-customer P1 effort at 6–14 person-weeks, with CP-01 and CP-02 as the primary cost drivers. A TE of 4 (3–6 person-weeks) is within the plausible range, though the upper end (6 weeks) approaches TE 5 territory for customers with complex bare-metal or multi-NIC configurations. Re-derived TE: **4** (borderline; could reach 5 for high-complexity hardware environments).

**Confidence:** Medium — GT1 confirms per-customer scaling behavior but provides no direct per-customer Phase 2 FTE measurement. The 4/4 rating is internally consistent with aggregate P1 Phase 2 estimates.

**Verdict:** ACCURATE (borderline on TE for complex hardware)

**Interview question (for Medium confidence):** To a Platform Engineering Director at an ISV with 10+ on-premises customers: "For each new on-premises customer deployment, how many engineer-weeks does your team spend on K8s cluster configuration specific to that customer's server hardware and virtualization layer, excluding work that's standardized across all customers?"

---

### Phase 3 — Ongoing Updates and Support

**Rating under review:** RD 5 / TE 5

**Current rating:** RD 5 / TE 5; Scales with N: Yes; Research FTE 3.0–6.0 (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 3 table)

**Re-derived rating (RD):**

GT1 records three K8s minor versions per year with 12–14 month support windows. (`GT1_P1_ground_truth.md`, CP-01 Key Operational Characteristics: "Kubernetes releases approximately 3 minor versions per year with 12–14 month support windows.") Each customer requires separate node draining, validation, and coordination sequences for every upgrade. (`GT1_P1_ground_truth.md`, CP-01 Scaling Behavior) The GT1 composite on-premises rating of 5/5 is the steady-state difficulty, which Phase 3 ongoing operations directly inherits. The Ingress NGINX EOL March 2026 adds unplanned 0.3–0.6 FTE of platform work for managed K8s ISVs; on-premises ISVs bear similar or greater burden since the migration must be executed per-customer rather than once centrally. (`GT1_P1_ground_truth.md`, CP-01 Notable Caveats / Technology Transitions) External sources confirm the Ingress NGINX retirement on March 31, 2026 affects approximately 50% of cloud-native environments, with on-premises sites carrying unmaintained internet-facing components as security risk if not migrated. (https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) Re-derived RD: **5**.

**Re-derived rating (TE):**

GT1 records Phase 3 on-premises FTE for CP-01 as 3.0–6.0 FTE. (`GT1_P1_ground_truth.md`, Summary FTE table) TE 5 = "2.5+ FTE" annually per the TE scale reference. (`analysis/three_phase_on_prem_ratings.md`, Rating Scales table) The 3.0–6.0 FTE range is above the 2.5+ FTE threshold for TE 5 across all of its range. The Scales with N: Yes designation is confirmed by GT1's statement that "on-premises operational work scales linearly with customer count while cloud-native scales sub-linearly." (`GT1_P1_ground_truth.md`, Executive Summary) External sources confirm that without automation, Day 2 operations (upgrades, patches, capacity planning, incident response) "consume your entire team" for on-premises K8s at scale. (https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/) Re-derived TE: **5**.

**Confidence:** High — GT1 FTE range (3.0–6.0) sits firmly above the TE 5 threshold (2.5+); linear scaling is explicitly stated in GT1; external sources corroborate Phase 3 Day 2 operational burden.

**Verdict:** ACCURATE

---

## CP-02: Network Fabric, Ingress, and Service Mesh

### Phase 1 — Initial Refactoring

**Rating under review:** RD 5 / TE 4

**Current rating:** RD 5 / TE 4 (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 1 table)

**Re-derived rating (RD):**

GT1 records the CP-02 on-premises composite difficulty as 5/5, with load balancer/ingress provisioning, network segmentation/policy enforcement, and service mesh all rated 5/5 on-premises versus 1/5 on cloud-native. (`GT1_P1_ground_truth.md`, CP-02 Difficulty Ratings table) Phase 1 requires replacing VPC networking and managed load balancers (AWS ALB, Azure Application Gateway, GCP Cloud Load Balancing — all rated 1/5 difficulty) with Calico/Cilium CNI, HAProxy, CoreDNS, and self-managed ingress. (`GT1_P1_ground_truth.md`, CP-02 Key Operational Characteristics: "AWS ALB, Azure Application Gateway, and GCP Cloud Load Balancing are fully managed with SLAs.") The Ingress NGINX EOL March 2026 mandates migration to the Kubernetes Gateway API as the Phase 1 target architecture, eliminating the previously standard Ingress NGINX path. (`GT1_P1_ground_truth.md`, CP-02 Notable Caveats) External sources confirm the Gateway API migration is a significant engineering undertaking for platform teams, with ISVs recommended to maintain Ingress functionality for existing workloads while building new capabilities on Gateway API foundations. (https://www.okteto.com/blog/ingress-nginx-controller-deprecation-your-migration-guide-to-kubernetes-gateway-api/) Re-derived RD: **5**.

**Re-derived rating (TE):**

GT1 records the on-premises FTE range for CP-02 as 1.75–3.5 FTE (add 1.0–2.0 FTE if service mesh adopted). (`GT1_P1_ground_truth.md`, CP-02 FTE Ranges) TE 4 = "6–12 person-months one-time effort" for Phase 1. The Phase 1 build scope — Calico/Cilium CNI, VLAN segmentation, CoreDNS HA, HAProxy, network policy engine, and Gateway API migration — is a major engineering effort but is bounded and deliverable in 6–12 months for a competent platform team. Service mesh adoption has declined from 50% (2023) to approximately 8% developer-level adoption (Q3 2025), meaning most ISVs will not need the additional 1.0–2.0 FTE service mesh component. (`GT1_P1_ground_truth.md`, CP-02 Notable Caveats: "Service mesh adoption declined from 50% (2023) to 42% (2024) to approximately 8% developer-level adoption by Q3 2025.") External sources confirm that choosing Cilium (which handles networking, service mesh, and ingress as a single system) can reduce Phase 1 scope by eliminating three separate systems. (https://blog.devops.dev/stop-using-the-wrong-cni-flannel-vs-calico-vs-cilium-in-2025-c11b42ce05a3) Re-derived TE: **4**.

**Confidence:** High — GT1 on-premises composite is 5/5; FTE range supports TE 4; service mesh decline data supports the assumption that most ISVs will not need the full 1.75–3.5+ FTE upper range for Phase 1.

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Hardware Customization

**Rating under review:** RD 4 / TE 4

**Current rating:** RD 4 / TE 4; noted as "Most variable P1 subsegment per customer" (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 2 table)

**Re-derived rating (RD):**

GT1 confirms that physical switch failures propagate until redundant paths activate, and ECMP and spanning tree convergence times can reach minutes in on-premises environments. (`GT1_P1_ground_truth.md`, CP-02 Key Operational Characteristics) Each customer's network topology, firewall rules, proxy requirements, DNS architecture, and egress policies are unique per site. The CNI layer must be adapted to the customer's L2/L3 topology — a BGP-routed environment, a flat VLAN environment, and an SDN-managed environment each require different Calico or Cilium configuration. (`GT1_P1_ground_truth.md`, CP-02 Evidence citing F40, F76 Domain 1) External sources on Calico confirm it is "ideal for enterprises running workloads across on-prem, cloud, and edge, with support for BGP routing that enables seamless IP-level connectivity" but that "setting up and maintaining Calico, especially custom deployments, can be more involved than Cilium." (https://zesty.co/finops-glossary/calico-vs-cilium-in-kubernetes-networking/) The per-customer network adaptation is the most hardware-heterogeneous subsegment in P1 — the "Most variable P1 subsegment per customer" description in the ratings file is accurate and supported by GT1 data. Re-derived RD: **4**.

**Re-derived rating (TE):**

Phase 2 TE 4 = "3–6 person-weeks per customer" at the TE scale. GT1 does not provide a direct per-customer Phase 2 FTE for CP-02 specifically. DNS failures carry "uniquely high blast-radius because resolution is a prerequisite for nearly every service-to-service call," which implies thorough per-customer DNS validation is non-negotiable. (`GT1_P1_ground_truth.md`, CP-02 Scaling Behavior) A 2025 EKS incident traced a Linux conntrack management bug in CoreDNS that caused cascading DNS timeouts — this type of environment-specific tuning (conntrack limits, HPA configuration) must be validated per customer hardware profile. (`GT1_P1_ground_truth.md`, CP-02 Key Operational Characteristics: "CoreDNS is self-managed; scaling, HPA configuration, and Linux conntrack tuning required.") 3–6 person-weeks is plausible for network adapter validation, CNI configuration, network policy testing, and DNS integration per customer. Re-derived TE: **4** (could reach 5 for customers with complex multi-VLAN or SDN architectures).

**Confidence:** Medium — GT1 confirms hardware-specific network complexity and per-customer scaling, but no direct empirical per-customer Phase 2 FTE measurement exists in the source corpus.

**Verdict:** ACCURATE (borderline on TE for SDN/multi-VLAN environments)

**Interview question (for Medium confidence):** To a Site Reliability Engineering Lead at an ISV deploying to 5+ on-premises customers: "For a new enterprise customer, how many engineer-days does your team spend on network configuration — CNI setup, firewall rules, ingress routing, and DNS integration — specific to that customer's network topology, after your standard K8s deployment playbook is applied?"

---

### Phase 3 — Ongoing Updates and Support

**Rating under review:** RD 4 / TE 4; Scales with N: Yes; Research FTE 1.75–3.5

**Current rating:** RD 4 / TE 4 (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 3 table)

**Re-derived rating (RD):**

GT1 on-premises composite for CP-02 is 5/5. (`GT1_P1_ground_truth.md`, Summary Table) Phase 3 ongoing operations involve CNI upgrades, network policy updates, ingress controller patches per customer, and Gateway API evolution. The ratings file assigns RD 4 rather than 5, implying Phase 3 CP-02 is slightly less difficult than Phase 1. This is defensible: Phase 1 requires building the network stack from scratch, whereas Phase 3 requires maintaining an existing one. Ongoing CNI upgrades and network policy changes are bounded operations compared to initial CNI selection and deployment. The GT1 5/5 composite reflects the sum of all difficulty dimensions including initial configuration; steady-state patch operations sit one level below. Re-derived RD: **4**.

**Re-derived rating (TE):**

GT1 Phase 3 FTE for CP-02 is 1.75–3.5 FTE. (`GT1_P1_ground_truth.md`, Summary FTE table) TE 4 = "1.0–2.5 FTE" annually per the TE scale. The GT1 lower bound (1.75 FTE) sits at the upper edge of the TE 4 range (1.0–2.5), while the GT1 upper bound (3.5 FTE with service mesh) sits clearly in TE 5 territory (2.5+ FTE). For the modal ISV case without service mesh (8% service mesh adoption rate per GT1), the midpoint of 1.75–2.5 FTE without mesh is within TE 4 range. If service mesh is adopted, TE should be 5. The Scales with N: Yes designation is corroborated: network-related incidents are customer-specific due to hardware heterogeneity, requiring per-customer investigation. Re-derived TE: **4** (modal case, no service mesh); **5** if service mesh adopted.

**Confidence:** High for the no-service-mesh case (GT1 FTE range overlaps TE 4). Medium for service mesh adopters.

**Verdict:** ACCURATE for modal ISV (no service mesh). Would ADJUST TE to 5 for ISVs with service mesh deployments, but this is an edge case given 8% adoption rate.

---

## CP-03: Identity, Access Management, and RBAC

### Phase 1 — Initial Refactoring

**Rating under review:** RD 4 / TE 4

**Current rating:** RD 4 / TE 4 (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 1 table)

**Re-derived rating (RD):**

GT1 records the CP-03 on-premises composite difficulty as 4/5 (versus CP-01 and CP-02 at 5/5). (`GT1_P1_ground_truth.md`, CP-03 Difficulty Ratings table; Summary Table: "CP-03 | Identity, Access Management, and RBAC | 1 | 2 | 4") The four sub-dimensions show: identity provider operations 4/5, RBAC/policy engine management 5/5, workload identity 4/5, directory services 4/5. (`GT1_P1_ground_truth.md`, CP-03 Difficulty Ratings table) The GT1 characterization of IAM as "a product line, not an infrastructure dependency" with "seven sub-domains each rated 3–4/5 difficulty" supports RD 4 for Phase 1. (`GT1_P1_ground_truth.md`, CP-03 Key Operational Characteristics) External sources confirm Keycloak self-hosted HA deployment requires specialized Java, networking, and database expertise with a 3-year TCO of $199,200–$211,200 dominated by operational costs of $142,200. (https://www.siriusopensource.com/en-us/blog/how-much-does-keycloak-cost) The RD 4 rating (versus 5 for CP-01 and CP-02) is appropriate: the IAM stack is complex but has clearer implementation patterns (Keycloak/Dex are mature products with documented HA configurations) compared to the fully bespoke network fabric work of CP-02. Re-derived RD: **4**.

**Re-derived rating (TE):**

GT1 Phase 3 FTE for CP-03 is 2.75–4.75 FTE, which informs the scale of the ongoing operational burden. (`GT1_P1_ground_truth.md`, CP-03 FTE Ranges) Phase 1 requires deploying Keycloak or Dex in HA, configuring the seven IAM sub-domains, building RBAC policy frameworks, and architecting workload identity. TE 4 = "6–12 person-months one-time effort." The Keycloak deployment with HA clustering, initial RBAC schema design, Active Directory/LDAP federation, OIDC configuration, and policy engine selection (OPA vs Kyverno, with OPA now at risk due to Apple's acquisition of the maintainer team in August 2025) is plausibly a 6–12 month effort. (`GT1_P1_ground_truth.md`, CP-03 Notable Caveats) The Apple/OPA acquisition risk adds unplanned Phase 1 decision surface: the policy engine selection is now a long-term governance call, not just a technical preference. Re-derived TE: **4**.

**Confidence:** High — GT1 composite 4/5 directly supports RD 4; Phase 1 TE 4 (6–12 person-months) is consistent with Keycloak HA build complexity confirmed by external sources.

**Verdict:** ACCURATE

---

### Phase 2 — Per-Customer Hardware Customization

**Rating under review:** RD 3 / TE 3

**Current rating:** RD 3 / TE 3 (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 2 table)

**Re-derived rating (RD):**

Phase 2 CP-03 involves integrating with each customer's existing identity provider (LDAP, SAML, OIDC), mapping customer organizational roles to the ISV's RBAC model, and configuring federation. The GT1 sub-dimension for directory services (AD/LDAP) is rated 4/5 on-premises at the platform level, but per-customer federation configuration is a narrower scope than building the full IAM stack. (`GT1_P1_ground_truth.md`, CP-03 Difficulty Ratings: "Directory services (AD/LDAP): Cloud-Native 1 | Managed K8s 2 | On-Premises 4") Each customer's Active Directory or LDAP schema is unique; attribute mapping, group-to-role translation, and MFA policy alignment require IAM specialist knowledge. A rating of 3 (Moderate: "Meaningful new work; requires platform awareness") is defensible — this is not trivial configuration but is bounded to federation and RBAC mapping, not full IAM stack construction. Re-derived RD: **3**.

**Re-derived rating (TE):**

Phase 2 TE 3 = "1–3 person-weeks per customer." Keycloak federation configuration for a new customer's LDAP/SAML identity provider, RBAC group mapping, and validation testing is documented as taking multiple days to a week for a competent IAM engineer. External sources note "more than 3 hours of weekly maintenance" per ongoing Keycloak operation, and that "clustering, caching, and startup tuning require extra operational overhead." (https://www.siriusopensource.com/en-us/blog/problems-keycloak-unpacking-challenges) Initial per-customer setup (federation only, not full build) at 1–3 person-weeks is plausible. The GKE Identity Service deprecation (July 1, 2025 for new organizations) does not affect on-premises deployments but confirms the general pattern that identity federation requires regular adaptation to provider changes. (`GT1_P1_ground_truth.md`, CP-03 Notable Caveats) Re-derived TE: **3**.

**Confidence:** Medium — GT1 confirms per-customer identity domain complexity (50 separate compliance audit surfaces for 50 customers) and IAM federation requirements, but no direct per-customer Phase 2 FTE measurement exists. The 3/3 rating is directionally correct but relies on engineering judgment, not empirical measurement.

**Verdict:** ACCURATE

**Interview question (for Medium confidence):** To an IAM-specialist Solutions Engineer at an ISV with on-premises customers: "For a new enterprise customer, how many engineer-days does your IAM team spend on Keycloak federation configuration — mapping the customer's Active Directory/LDAP schema to your RBAC model, configuring SAML/OIDC, and validating MFA policies — before the deployment is identity-operational?"

---

### Phase 3 — Ongoing Updates and Support

**Rating under review:** RD 3 / TE 4; Scales with N: Partial; Research FTE 2.75–4.75

**Current rating:** RD 3 / TE 4 (`analysis/three_phase_on_prem_ratings.md`, P1 Control Plane Phase 3 table)

**Re-derived rating (RD):**

GT1 on-premises composite for CP-03 is 4/5. Phase 3 ongoing operations involve Keycloak upgrades, identity provider integration maintenance, and per-customer federation configuration upkeep. The ratings file assigns RD 3 rather than 4. The one-level downgrade from the GT1 4/5 composite reflects the same logic as CP-02: Phase 3 maintains an existing IAM stack rather than building it. Keycloak upgrades follow a predictable cadence with documented migration paths, and per-customer federation maintenance is largely configuration drift management rather than novel engineering. The OPA/Gatekeeper maintainer risk (Apple acquisition August 2025) introduces a potential re-derive point: if ISVs must migrate from OPA to Kyverno during Phase 3, this is unplanned engineering work that could push RD to 4. (`GT1_P1_ground_truth.md`, CP-03 Notable Caveats: "Apple's acquisition of the OPA maintainer team in August 2025 creates a policy-engine risk for ISVs dependent on OPA/Gatekeeper.") Re-derived RD: **3** (standard case); borderline **4** if OPA-to-Kyverno migration is required.

**Re-derived rating (TE):**

GT1 Phase 3 FTE for CP-03 is 2.75–4.75 FTE. (`GT1_P1_ground_truth.md`, CP-03 FTE Ranges and Summary FTE table) TE 4 = "1.0–2.5 FTE" annually per the TE scale. (`analysis/three_phase_on_prem_ratings.md`, Rating Scales) The GT1 lower bound of 2.75 FTE **exceeds** the TE 4 upper bound of 2.5 FTE. The entire GT1 FTE range (2.75–4.75) sits within the TE 5 threshold (2.5+ FTE). This is a material discrepancy: the ratings file assigns TE 4, but the GT1 source data implies TE 5.

However, the GT1 FTE figure of 2.75–4.75 is the total on-premises CP-03 FTE for a 50-customer fleet including the security cluster deduplication note, which states "1.0–2.0 FTE deduplication required across CP-03, CP-04, and CP-10" for the trio. (`GT1_P1_ground_truth.md`, Summary FTE table deduplication note) After applying the deduplication reduction of approximately 0.5–0.7 FTE attributed to CP-03's share, the effective CP-03 range becomes approximately 2.1–4.0 FTE. The lower end (2.1 FTE) is still above the TE 4 ceiling of 2.5 FTE only at mid-range. At the lower bound, a net ~2.1 FTE sits at the edge of TE 4 (1.0–2.5). At the upper bound (~4.0 FTE net), this is firmly TE 5.

Given the partial-scaling classification (core IAM tooling is shared; per-customer federation maintenance adds linear cost) and the 50-customer baseline, the appropriate Phase 3 TE for a mid-size ISV is better represented as TE 3 (0.3–1.0 FTE) for the shared IAM tooling base, rising to TE 4–5 as customer count grows. At the stated 50-customer reference baseline, the GT1 data implies TE that is above the TE 4 ceiling. The ratings file TE 4 appears to understate the effort by approximately one level relative to GT1 source data, unless the deduplication adjustment is applied more aggressively than the source warrants.

Re-derived TE: **Adjust to 3 for small customer bases (< 10 customers); TE 4 is accurate at 20–30 customers; the 50-customer reference baseline implies TE 5 before deduplication. The stated TE 4 is plausible only if post-deduplication CP-03 FTE is approximately 1.5–2.5 FTE.**

**Confidence:** Medium — GT1 provides the FTE range (2.75–4.75) but the deduplication methodology introduces imprecision. The TE 4 rating is at the boundary of defensibility and warrants validation.

**Verdict:** ADJUST — TE 4 may understate the 50-customer-baseline effort. If post-deduplication CP-03 FTE is confirmed at 2.5+ FTE, adjust to TE 5. If deduplication reduces CP-03 to 1.5–2.0 FTE net, TE 4 is accurate. Direction: potential +1 on TE (from 4 to 5) at the reference 50-customer baseline.

**Interview question (for Medium confidence):** To a VP of Platform Engineering at an ISV with 40–60 on-premises customers: "How many FTE does your team spend annually on IAM-specific work — Keycloak version upgrades, per-customer federation maintenance, RBAC policy updates, and identity incident response — across your on-premises customer base? How much of that is shared work versus per-customer?"

---

## Key Findings

1. **CP-01 and CP-02 Phase 1 and Phase 3 ratings are accurate and High confidence.** The GT1 composite 5/5 on-premises ratings directly support RD 5 in both phases, and GT1 FTE ranges (3.0–6.0 FTE for CP-01; 1.75–3.5 FTE for CP-02) confirm TE ratings at the 50-customer baseline. External sources corroborate Kubernetes distribution disruption (SUSE 4–9x pricing, VMware 8–15x increases) that validates the Phase 1 build complexity being at maximum difficulty.

2. **CP-03 Phase 3 Total Effort rating warrants investigation.** The stated TE 4 (1.0–2.5 FTE) does not align with GT1's reported FTE range of 2.75–4.75 FTE at the 50-customer reference baseline. After applying the GT1 deduplication adjustment (~0.5–0.7 FTE), the net CP-03 FTE may fall at the edge of or above the TE 4 ceiling. An interview with a VP of Platform Engineering operating at scale would resolve this discrepancy.

3. **Phase 2 per-customer ratings carry consistent Medium confidence across all three subsegments.** No direct empirical per-customer Phase 2 FTE data exists in the GT1 source corpus. The 4/4 ratings for CP-01 and CP-02 Phase 2, and the 3/3 rating for CP-03 Phase 2, are internally consistent with aggregate estimates and directionally correct, but have not been validated against measured deployment data.

4. **CP-02 Phase 3 service mesh risk is underweighted in the modal rating.** The TE 4 rating is accurate for the ~92% of ISVs not using a service mesh. For the remaining 8% that have adopted Istio or Linkerd, Phase 3 CP-02 TE should be 5 (adding 1.0–2.0 FTE per GT1). The ratings file notes this only in the Phase 1 row and does not flag it explicitly for Phase 3.

5. **The Ingress NGINX EOL (March 2026) creates unplanned Phase 3 work for CP-01 and CP-02 simultaneously.** GT1 quantifies this at 0.3–0.6 FTE of unplanned platform work for managed K8s ISVs; on-premises ISVs must execute the same Gateway API migration per customer rather than once, multiplying the cost by N customers. This transient spike is not captured in the Phase 3 steady-state ratings and represents a one-time elevation above the stated TE 4 for CP-02 in 2026.

---

## Sources

| Source | Type | Coverage |
|---|---|---|
| `GT1_P1_ground_truth.md` (2026-02-19) | Internal ground truth | All CP-01, CP-02, CP-03 difficulty ratings and FTE ranges |
| `analysis/three_phase_on_prem_ratings.md` (2026-02-19) | Ratings file under review | Three-phase ratings for all 38 subsegments |
| `analysis/P1_control_plane.md` (2026-02-19, via GT1) | Primary source | CP-01 through CP-10 evidence and sub-dimension ratings |
| https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/ | External — Kubernetes.io official | Ingress NGINX EOL March 2026 confirmation |
| https://www.okteto.com/blog/ingress-nginx-controller-deprecation-your-migration-guide-to-kubernetes-gateway-api/ | External — Okteto | Gateway API migration guidance |
| https://opensource.googleblog.com/2026/02/the-end-of-an-era-transitioning-away-from-ingress-nginx.html | External — Google Open Source Blog | Ingress NGINX retirement impact assessment |
| https://www.portainer.io/blog/suse-rancher-price-hike-why-enterprises-are-searching-for-alternatives-in-2025 | External — Portainer | SUSE Rancher 4–9x pricing increase 2025 |
| https://blog.devops.dev/stop-using-the-wrong-cni-flannel-vs-calico-vs-cilium-in-2025-c11b42ce05a3 | External — DevOps.dev | Calico/Cilium CNI operational comparison 2025 |
| https://zesty.co/finops-glossary/calico-vs-cilium-in-kubernetes-networking/ | External — Zesty | Calico on-premises suitability and BGP routing |
| https://www.siriusopensource.com/en-us/blog/problems-keycloak-unpacking-challenges | External — Sirius Open Source | Keycloak operational complexity and maintenance burden |
| https://www.siriusopensource.com/en-us/blog/how-much-does-keycloak-cost | External — Sirius Open Source | Keycloak 3-year TCO: $199,200–$211,200 |
| https://arxiv.org/html/2407.01620v1 | External — arXiv | Kubernetes deployment options for on-premises clusters |
| https://scaleops.com/blog/the-complete-guide-to-kubernetes-management-in-2025-7-pillars-for-production-scale/ | External — ScaleOps | K8s Day 2 operations consuming full team without automation |
| https://isovalent.com/blog/post/state-of-kubernetes-networking-report-2025/ | External — Isovalent | State of Kubernetes Networking 2025 |
| https://www.spectrocloud.com/state-of-kubernetes-2025 | External — Spectro Cloud | State of Production Kubernetes 2025 |
