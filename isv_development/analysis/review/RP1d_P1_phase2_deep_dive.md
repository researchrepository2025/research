# RP1d: P1 Control Plane — Phase 2 (Per-Customer Customization) Deep Dive

**Review Date:** 2026-02-19
**Scope:** Phase 2 ratings for P1 Control Plane (CP-01 through CP-10) only
**Prior Context:** GT1_P1_ground_truth.md; three_phase_on_prem_ratings.md
**Responsibility Split:** Customer owns hardware, GPUs, and AI models. ISV owns all software and software-to-hardware adaptation.

---

## Executive Summary

Phase 2 P1 averages of RD 3.0 and TE 2.9 are directionally plausible but carry medium-to-low confidence because external empirical data on per-customer ISV deployment effort is sparse and highly variable. The 6–14 person-week per-customer estimate sits at the lower bound of what professional services case study data suggests for complex on-premises Kubernetes deployments in heterogeneous enterprise environments. CP-02 (Network Fabric) is correctly identified as the highest-rated Phase 2 subsegment, supported by multiple independent sources confirming that network topology is the single most variable element across customer sites. The most significant analytical risk in the current ratings is systematic underestimation of CP-01, CP-04, and CP-07, where per-customer hardware diversity creates compounding configuration requirements that the current ratings may not fully capture.

---

## Per-Subsegment Phase 2 Review (CP-01 to CP-10)

---

### CP-01: Kubernetes Cluster Lifecycle Management
**Current Rating: RD=4, TE=4**

#### Re-derived Rating: RD=4, TE=4

[FACT] Each customer's server models, virtualization layer (VMware vs. KVM vs. bare metal), storage controllers, and NIC drivers require Kubernetes configuration adaptation; node pool sizing is based on the customer's available compute.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-01 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[STATISTIC] Replicated's Compatibility Matrix documents 65,981+ unique Kubernetes environment configurations across customer deployments — the surface area of hardware and K8s-version variance that per-customer deployment automation must account for.
— Source: GT1_P1_ground_truth.md, CP-06 Evidence (citing F48, F58, W08S Theme 1)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Shadow-Soft completed a production-ready Kubernetes deployment for an ISV across bare metal, VMware, and EKS environments in under 160 hours (approximately 4 person-weeks), which included cluster sizing assessment, DNS and load balancer configuration, and logging stack integration.
— Source: Shadow-Soft case study, "MSP Deploys a Production-Ready Kubernetes Environment for ISV in Under 160 Hours"
URL: https://shadow-soft.com/content/msp-isv-kubernetes-deployment-160-hours

[FACT] The Spectro Cloud 2025 State of Production Kubernetes report found that enterprises run clusters across five-plus environments on average, and more than 50% admit their clusters are "snowflakes" with highly manual operations.
— Source: Spectro Cloud, "State of Production Kubernetes 2025"
URL: https://www.spectrocloud.com/state-of-kubernetes-2025

**Confidence: M**
The RD=4 rating is well-supported: virtualization heterogeneity (VMware vs. bare metal vs. KVM) alone generates materially different kubeadm/RKE2 configuration paths, and the 65,981+ configuration matrix confirms the breadth of variance. The TE=4 rating (3–6 person-weeks) is plausible but may be slightly high relative to what automation can eliminate once the ISV has 4+ deployments; however, the "snowflake" finding supports that manual effort remains dominant at the industry level.

**Verdict: HOLD.** Both dimensions are defensible. The Shadow-Soft 4 person-week single-customer engagement provides a lower-bound data point that does not contradict TE=4 for a more complex deployment.

**Interview question:** For your most recent on-premises customer deployment, how many engineer-hours did initial Kubernetes cluster configuration take — from first infrastructure access to a healthy control plane — and which virtualization layer was involved?

---

### CP-02: Network Fabric, Ingress, and Service Mesh
**Current Rating: RD=4, TE=4**

#### Re-derived Rating: RD=4–5, TE=4

[FACT] "Customer's network topology, firewall rules, proxy requirements, DNS architecture, and egress policies are unique per site. CNI configuration, ingress routing, and network policies must be adapted. Most variable P1 subsegment per customer."
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-02 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] On-premises Kubernetes networking requires Calico, Flannel, or Weave configuration tailored to each site's physical network; overlay networks are required when the underlying physical network is managed by a third party or does not support dynamic IP routing between Kubernetes nodes.
— Source: Groundcover, "Kubernetes On-Premises: Benefits, Challenges & Best Practices"
URL: https://www.groundcover.com/blog/kubernetes-on-premises

[FACT] Designing on-premises Kubernetes networks for high availability requires configuring firewall and routing rules in on-premises switches to allow appropriate traffic flow, plus managing hardware-specific switch failures where ECMP and spanning tree convergence times can reach minutes.
— Source: Tigera, "Designing On-Prem Kubernetes Networks for High Availability"
URL: https://www.tigera.io/blog/designing-on-prem-kubernetes-networks-for-high-availability/

[FACT] DNS failures carry "uniquely high blast-radius because resolution is a prerequisite for nearly every service-to-service call" — confirmed as a 2025 EKS incident where a Linux conntrack management bug caused cascading DNS timeouts.
— Source: GT1_P1_ground_truth.md, CP-02 Evidence (citing F76 Domain 2)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] The Ingress NGINX Controller — powering approximately 41% of internet-facing Kubernetes clusters — was officially retired in November 2025, with maintenance ending March 2026, forcing mandatory migration to the Kubernetes Gateway API per customer.
— Source: GT1_P1_ground_truth.md, CP-01/CP-02 Evidence (citing F73 C03, F40)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: H**
Network heterogeneity is the single most empirically supported source of per-customer variance in the research corpus. Multiple independent sources (ground truth, Tigera, Groundcover, Spectro Cloud) confirm that network topology — including VLAN design, firewall rule sets, proxy requirements, and DNS architecture — differs materially per site and requires hands-on configuration work that cannot be fully automated without advance knowledge of the customer's environment. The CP-02 RD=4 rating for Phase 2 is the most defensible rating in the P1 Phase 2 table. A case could be made for RD=5 given the Ingress NGINX EOL forcing a mandatory per-customer migration concurrent with Phase 2 work in 2026.

**Verdict: HOLD (with note that RD may warrant elevation to 5 in 2026 given Ingress NGINX EOL).** This is correctly identified as the highest-rated Phase 2 subsegment. The TE=4 is appropriate given that firewall rule negotiation, proxy bypass configuration, and DNS integration each consume meaningful engineering time per customer.

---

### CP-03: Identity, Access Management, and RBAC
**Current Rating: RD=3, TE=3**

#### Re-derived Rating: RD=3, TE=3

[FACT] Phase 2 CP-03 requires integrating with the customer's existing identity provider (LDAP, SAML, OIDC), mapping customer organizational roles to the ISV's RBAC model, and configuring federation.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-03 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] Configuring an Okta SAML v2.0 integration with Keycloak "is much simpler than OpenID Connect and took less than an hour from start to finish" in a straightforward case, but enterprise deployments with custom role mappings and LDAP directory integration scale substantially beyond that baseline.
— Source: Keycloak/Okta SAML integration community documentation
URL: https://maybeitdepends.com/keycloak-integration-with-okta

[FACT] Self-hosted Keycloak or Authentik requires HA configuration, patch lifecycle, and dedicated identity expertise; IAM is described as "a product line, not an infrastructure dependency" with seven sub-domains each rated 3–4/5 difficulty on-premises.
— Source: GT1_P1_ground_truth.md, CP-03 Evidence (citing F46, W06S Theme 2)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Apple's acquisition of the OPA maintainer team in August 2025 creates policy-engine risk for ISVs dependent on OPA/Gatekeeper, potentially requiring per-customer policy migration to Kyverno during Phase 2 deployments.
— Source: GT1_P1_ground_truth.md, CP-03 Evidence (citing F46, W06S Theme 2)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: M**
The RD=3 rating is appropriate. LDAP/SAML federation configuration is a known, bounded engineering task that experienced platform engineers perform routinely. A single customer's OIDC or SAML integration with Keycloak typically consumes 2–5 days of engineering time depending on directory structure complexity. The TE=3 (1–3 person-weeks) is plausible and consistent with available evidence.

**Verdict: HOLD.**

**Interview question:** When you integrate with a new on-premises customer's identity provider — whether LDAP, SAML, or OIDC — how many engineer-days does the federation configuration and role mapping typically require, and what percentage of integrations require multiple iterations due to customer directory structure complexity?

---

### CP-04: Secrets Management, Certificate Lifecycle, and PKI
**Current Rating: RD=3, TE=3**

#### Re-derived Rating: RD=3–4, TE=3–4

[FACT] Phase 2 CP-04 requires integrating with the customer's PKI infrastructure and certificate authority, possibly integrating with customer HSMs, and configuring trust chain per the customer's security architecture.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-04 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] HSM hardware costs $5K–$50K per unit and requires seat-of-pants configuration expertise that varies significantly per vendor (SafeNet, Thales, nCipher); integrating Vault with a customer's HSM involves a non-trivial PKCS#11 driver configuration that is rarely identical across customers.
— Source: GT1_P1_ground_truth.md, CP-04 Evidence (citing F47, W06S Theme 2, F76 Domain 3)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] FIPS 140-2 certificate validity expires September 2026 — HSM firmware and Vault seal configurations must transition to FIPS 140-3 before that date, creating a mandatory per-customer migration task concurrent with new Phase 2 deployments in 2026.
— Source: GT1_P1_ground_truth.md, CP-04 Evidence (citing F47, W06S Theme 2, F76 Domain 3)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Let's Encrypt announced in December 2025 that certificate validity will decrease to 45 days on May 13, 2026, increasing rotation frequency requirements and the complexity of configuring per-customer cert-manager automation at deployment time.
— Source: GT1_P1_ground_truth.md, CP-04 Evidence (citing F47, W06S Theme 2, F76 Domain 3)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: M**
The RD=3 rating may understate Phase 2 difficulty when customers have their own PKI hierarchies and HSMs. PKI trust chain integration is highly customer-specific — the ISV must import the customer's CA root, configure cert-manager to issue against it, and validate the full trust chain across all internal services. In regulated industries (financial services, federal government), this process can consume a full week of specialist time per customer. The 2026 FIPS 140-3 transition and 45-day Let's Encrypt certificate validity change both add incremental Phase 2 configuration work that did not exist at the time the ratings were calibrated.

**Verdict: CONSIDER RAISING to RD=4, TE=3 for customers in regulated industries with HSMs.** Current RD=3 may be appropriate for the median customer but understates the 95th percentile case.

**Interview question:** For customers with their own PKI infrastructure or HSMs, how many engineer-hours does the certificate authority trust chain integration and Vault-to-HSM seal configuration typically require per customer, and have you encountered customers where PKI integration became a deployment blocker?

---

### CP-05: Observability Infrastructure
**Current Rating: RD=2, TE=2**

#### Re-derived Rating: RD=2, TE=2

[FACT] Phase 2 CP-05 involves tuning storage retention and memory allocation for the customer's disk and memory profile; the observability stack itself is standardized. Integration with the customer's existing monitoring system may be required.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-05 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] The kube-prometheus-stack consumes 15–35 GB of cluster RAM before any application workloads are monitored; at a 100-node cluster this generates 500,000+ active Prometheus time series at approximately 3 KB RAM per series — all requiring per-customer capacity calculation at deployment time.
— Source: GT1_P1_ground_truth.md, CP-05 Evidence (citing F55d, W07S Theme 4, F49)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Jaeger v1 was deprecated January 2026, requiring migration to v2 (OTel Collector-based); MinIO entered maintenance mode late 2025 and was archived by early 2026, affecting on-premises tracing storage backends.
— Source: GT1_P1_ground_truth.md, CP-05 Evidence (citing F51, W06S Theme 3 and Theme 4)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: H**
RD=2 and TE=2 are well-calibrated. Per-customer observability work in Phase 2 is primarily configuration — storage class sizing, memory limit adjustment for Prometheus, and retention policy setting — not architectural work. The observability stack architecture is fixed; the per-customer variable is dimensioning. The Jaeger v2 migration is a one-time event in 2026 that may add a bounded increment of per-customer work but does not change the Phase 2 rating structurally.

**Verdict: HOLD.**

---

### CP-06: CI/CD Pipeline Infrastructure and GitOps
**Current Rating: RD=2, TE=2**

#### Re-derived Rating: RD=2, TE=2–3

[FACT] Phase 2 CP-06 adapts the artifact delivery pipeline for the customer's network constraints (air-gap, proxy, artifact mirror) and sets per-customer target-environment configuration in GitOps.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-06 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] Air-gapped delivery requires fully self-contained .airgap bundles with every image and dependency vendored; Replicated's Compatibility Matrix covers 65,981+ unique Kubernetes environment configurations.
— Source: GT1_P1_ground_truth.md, CP-06 Evidence (citing F48, F58, W08S Theme 1)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Replicated's time-to-install data shows that air-gapped installations require approximately 2 weeks versus approximately 2 hours for single-server online installations — a factor of approximately 60x difference in install time driven by network isolation.
— Source: Replicated, "Instance Insights: Time to Install"
URL: https://www.replicated.com/blog/instance-insights-time-to-install

[FACT] Before using Replicated, one ISV reported that setting up a production instance took as much as 90 days; with automation, that time was reduced to under 8 hours.
— Source: Replicated, "Introducing the State of Self-Hosted Survey 2025" (citing vendor testimonial)
URL: https://www.replicated.com/blog/introducing-the-state-of-self-hosted-survey-2025

[STATISTIC] 82% of vendors already support self-hosted deployments; nearly half deliver to self-hosted customers less frequently than to SaaS users.
— Source: Replicated, State of Self-Hosted Software Survey 2025
URL: https://www.replicated.com/blog/introducing-the-state-of-self-hosted-survey-2025

**Confidence: M**
RD=2 is appropriate for customers with standard proxy/registry mirror configurations. However, for air-gapped customers — a non-trivial fraction of regulated enterprise deployments — the Replicated data (2 weeks vs. 2 hours) suggests that TE could reach 3 for that subset. The rating as stated reflects the median customer. Air-gapped customers represent a distinct scenario that may warrant a separate Phase 2 row annotation.

**Verdict: HOLD for the median case. Add annotation: air-gapped customer deployments should be treated as TE=3 (1–3 person-weeks) for CP-06.**

**Interview question:** What percentage of your on-premises customers require air-gapped deployment, and what is the total engineering time consumed by artifact bundle preparation and delivery for an air-gapped customer versus a proxy-accessible customer?

---

### CP-07: Deployment Lifecycle, Rollback, and Release Cadence
**Current Rating: RD=3, TE=3**

#### Re-derived Rating: RD=3, TE=3–4

[FACT] Phase 2 CP-07 requires establishing deployment cadence, change management process, and maintenance windows with the customer; validating rollback procedures against the customer's specific environment.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-07 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[STATISTIC] "79% of Kubernetes production issues originate from a recent system change, and median MTTR exceeds 50 minutes." (Komodor 2025 Enterprise Kubernetes Report)
— Source: GT1_P1_ground_truth.md, CP-07 Evidence (citing F58, F76 Domain 10, F77); confirmed by Komodor 2025 Enterprise Kubernetes Report
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[STATISTIC] Teams lose more than 64 full workdays annually detecting and resolving Kubernetes issues; median MTTD for high-impact outages is nearly 40 minutes; median MTTR exceeds 50 minutes.
— Source: Komodor 2025 Enterprise Kubernetes Report
URL: https://komodor.com/blog/komodor-2025-enterprise-kubernetes-report-finds-nearly-80-of-production-outages/

[FACT] On-premises rollback "can consume days and require database restores"; Helm rollback fails on CRD changes, representing material operational risk for ISVs deploying Kubernetes Operators.
— Source: GT1_P1_ground_truth.md, CP-07 Evidence (citing F58, W08S Theme 3)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] ISVs routinely carry 3–5 concurrent major versions across their on-premises customer base; each active version multiplies the compatibility matrix, air-gap bundles, rollback procedures, and compliance audit surfaces.
— Source: GT1_P1_ground_truth.md, CP-07 Evidence (citing F58, W08S Theme 3)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: M**
The RD=3 rating accurately captures that Phase 2 deployment lifecycle work is "meaningful new work" relative to cloud-native. The TE=3 may understate effort for customers with complex change management processes (e.g., regulated industries with CAB approval requirements, government customers with maintenance window constraints). The Komodor data confirms that change-driven incidents — which Phase 2 must account for in rollback planning — are the dominant failure mode in production Kubernetes environments, adding validation complexity to each new customer deployment.

**Verdict: HOLD with note.** For customers with formal change management boards or regulated maintenance windows, TE could reach 4.

**Interview question:** When establishing the first deployment and rollback procedures with a new on-premises customer, how much time is consumed negotiating maintenance windows, change management processes, and validating the first rollback drill — and does this differ materially between regulated (government, healthcare) and commercial customers?

---

### CP-08: Disaster Recovery and Business Continuity Infrastructure
**Current Rating: RD=3, TE=3**

#### Re-derived Rating: RD=3, TE=3

[FACT] Phase 2 CP-08 adapts the DR plan to the customer's infrastructure — backup storage targets, recovery time objectives aligned with the customer's SLAs, and failover testing in the customer's environment.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-08 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] On-premises hardware costs $50K–$500K+ for large enterprise DR sites; DR consumes 15–25% of total IT budget on-premises; 68% of organizations experienced data loss from disasters at an average cost of $4.5 million per incident.
— Source: GT1_P1_ground_truth.md, CP-08 Evidence (citing F70, F77 Phase 9)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Ransomware attacks increased 49% in H1 2025, amplifying the stakes of DR gap assessment at each new customer site.
— Source: GT1_P1_ground_truth.md, CP-08 Evidence (citing F70)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: M**
RD=3 and TE=3 are reasonable. Per-customer DR planning involves discovery of the customer's existing backup infrastructure, negotiating RTO/RPO targets against what the ISV's platform can support, and executing a validation test. This is bounded engineering work (1–3 person-weeks) for a platform engineer who has already built the DR tooling in Phase 1. The financial stakes are high (evidenced by the cost-of-incident data) but the per-customer effort itself is procedural rather than architectural at Phase 2.

**Verdict: HOLD.**

---

### CP-09: Compliance and Regulatory Automation Infrastructure
**Current Rating: RD=3, TE=3**

#### Re-derived Rating: RD=3, TE=3

[FACT] Phase 2 CP-09 maps the ISV's compliance framework to the customer's specific regulatory requirements (FedRAMP vs. HIPAA vs. SOC 2 vs. industry-specific) and configures evidence collection for the customer's audit requirements.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-09 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[STATISTIC] FedRAMP costs $250K–$2M+ for initial authorization on-premises; EU AI Act GPAI obligations became active August 2025.
— Source: GT1_P1_ground_truth.md, CP-09 Evidence (citing F67, F60, W08S Theme 3)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Data sovereignty enforcement is rated 1/5 difficulty on-premises (the easiest rating in the entire P1 dataset) because data physically never leaves customer infrastructure — this is a genuine Phase 2 advantage that supports the lower relative difficulty rating for CP-09 compared to CP-01 and CP-02.
— Source: GT1_P1_ground_truth.md, CP-09 Evidence (citing F67); confirmed in Key Takeaways section
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: M**
RD=3 and TE=3 are defensible for the median customer. However, FedRAMP-specific customers represent a meaningful outlier — a new FedRAMP deployment requires that the ISV's specific authorization boundary be re-evaluated against the customer's infrastructure, which can consume weeks to months of compliance engineering time. For non-FedRAMP customers (SOC 2, HIPAA, or no formal framework), RD=3/TE=3 is appropriate.

**Verdict: HOLD for median customer. FedRAMP customers may warrant TE=4 or a separate rating tier.**

**Interview question:** When deploying for a customer under FedRAMP versus a customer under SOC 2 only, how does the compliance configuration engineering time differ per deployment — and does your team treat FedRAMP as a distinct deployment track with separate per-customer cost accounting?

---

### CP-10: Security Operations Infrastructure
**Current Rating: RD=3, TE=2**

#### Re-derived Rating: RD=3, TE=2–3

[FACT] Phase 2 CP-10 involves adapting security policy to the customer's threat model and existing security tooling, mostly configuration; optional integration with the customer's SIEM.
— Source: three_phase_on_prem_ratings.md, P1 Phase 2 table, CP-10 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] Cloud detection rates for Kubernetes attack techniques range from 24% (GCP SCC) to 66% (Azure Defender) — cloud-native agents cannot substitute for K8s-native tooling (Falco, Trivy); managed K8s deployments still require K8s-specific security tools.
— Source: GT1_P1_ground_truth.md, CP-10 Evidence (citing F71, F55c)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] 73% of security practitioners cite false positives as the top challenge in on-premises SIEM environments; SIEM integration per customer requires custom rule tuning to suppress environment-specific noise while maintaining signal fidelity.
— Source: GT1_P1_ground_truth.md, CP-10 Evidence (citing F71)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[STATISTIC] 28% of CVEs are weaponized within one day of disclosure; 77% of enterprises take more than one week to deploy patches — establishing that Phase 2 security configuration must account for the customer's existing patching velocity, not just the ISV's.
— Source: GT1_P1_ground_truth.md, CP-10 Evidence (citing F60, W08S Theme 2)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Confidence: M**
The RD=3/TE=2 divergence (RD exceeds TE) is the only such divergence in the P1 Phase 2 table. A plausible argument exists that TE should be raised to 3 when customer SIEM integration is required — Falco alert tuning against a customer's existing Splunk or QRadar instance is not trivial. The TE=2 (2–5 person-days) is defensible for customers without SIEM integration requirements; customers with mandatory SIEM integration could push TE to 3.

**Verdict: HOLD for customers without existing SIEM requirements. Consider TE=3 annotation for customers requiring SIEM integration.**

**Interview question:** When integrating with a customer's existing SIEM — Splunk, QRadar, or similar — how many engineer-days does the Falco-to-SIEM integration, alert rule tuning, and false positive suppression require per customer?

---

## The 6–14 Person-Week Per-Customer Estimate: Plausibility Assessment

[STATISTIC] The current Phase 2 P1 total effort estimate is 6–14 person-weeks per customer (derived from the Phase 2 Summary table, P1 row).
— Source: three_phase_on_prem_ratings.md, Phase 2 Summary
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] Shadow-Soft completed a production-ready Kubernetes deployment for a single ISV customer across bare metal, VMware, and EKS environments in under 160 hours (4 person-weeks), covering cluster sizing, DNS, load balancer, logging, CMMC compliance, and zero-downtime upgrade validation.
— Source: Shadow-Soft, "MSP Deploys a Production-Ready Kubernetes Environment for ISV in Under 160 Hours"
URL: https://shadow-soft.com/content/msp-isv-kubernetes-deployment-160-hours

[FACT] Replicated's Time-to-Install data shows "happy path" single-server online installations at approximately 2 hours and "complex air-gapped installations" at approximately 2 weeks — establishing a wide lower-to-upper range depending on network accessibility.
— Source: Replicated, "Instance Insights: Time to Install"
URL: https://www.replicated.com/blog/instance-insights-time-to-install

[FACT] Connsulting reports that on-premises deployments initially consume 6-month deployment cycles and that 30–40% of engineering team time is consumed by one-off deployments rather than product features during the operational buildout period.
— Source: Connsulting, "The On-Premises Revenue Trap — Why Enterprise SaaS Deployments Kill Engineering Velocity"
URL: https://www.connsulting.io/blog/the-on-prem-revenue-trap

[STATISTIC] Personnel costs represent 50–85% of total on-premises application ownership; 70–80% of total R&D spend is personnel costs (ICONIQ 2024 Engineering Series), making engineering diversions to per-customer deployment tasks a direct drain on product development capacity.
— Source: Connsulting, "The On-Premises Revenue Trap"
URL: https://www.connsulting.io/blog/the-on-prem-revenue-trap

**Assessment:** The 6–14 person-week range sits at the lower-to-middle bound of what external evidence suggests for a complex SaaS platform deployed into a heterogeneous enterprise environment. The Shadow-Soft 4 person-week figure is for a professional services engagement with defined scope and specialized tooling — an ISV without dedicated deployment automation infrastructure would consume more time on initial deployments. The Replicated air-gapped case (2 weeks) aligns with the lower end of the estimate before accounting for the full P1 subsegment surface area. The Connsulting 6-month initial cycle figure suggests that early deployments (customers 1–4) substantially exceed the 6–14 week estimate, with the estimate becoming realistic only after automation investment matures (customers 5+). **The 6–14 person-week estimate is plausible for a mature ISV with 5+ deployments and good automation tooling. It likely understates effort for the first 3–4 customers.**

---

## Which Subsegments Are Most Sensitive to Customer Hardware Diversity

[FACT] Highest sensitivity: CP-02 (Network Fabric) — rated "most variable P1 subsegment per customer" — because network topology, firewall rules, proxy requirements, and DNS architecture are determined by the customer's physical network infrastructure, which is categorically unique per site.
— Source: three_phase_on_prem_ratings.md, CP-02 Phase 2 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

[FACT] High sensitivity: CP-01 (Cluster Lifecycle) — server models, virtualization layer (VMware vs. KVM vs. bare metal), storage controllers, and NIC drivers each generate distinct Kubernetes configuration paths; Replicated's 65,981+ environment matrix documents the combinatorial scope.
— Source: GT1_P1_ground_truth.md, CP-06 Evidence; three_phase_on_prem_ratings.md, CP-01 Phase 2 notes

[FACT] Moderate sensitivity: CP-04 (Secrets/PKI) — customers with their own HSMs require PKCS#11 driver integration that varies per HSM vendor (SafeNet vs. Thales vs. nCipher); customers without HSMs follow a standardized Vault path.
— Source: GT1_P1_ground_truth.md, CP-04 Evidence (citing F47)
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] Low sensitivity: CP-05, CP-08 — observability and DR work in Phase 2 is primarily dimensioning (memory allocation, storage class sizing) rather than architectural adaptation; hardware diversity affects these subsegments through resource availability, not configuration topology.
— Source: three_phase_on_prem_ratings.md, CP-05 and CP-08 Phase 2 notes
URL: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md`

---

## Key Findings

- **The 6–14 person-week per-customer P1 estimate is plausible for a mature ISV (5+ deployments) with automation investment but likely understates early-customer (1–4) effort.** Connsulting's 6-month initial deployment cycle data and Replicated's 90-day-to-under-8-hour improvement trajectory both suggest that automation ROI is non-linear and the estimate assumes the mature end of the curve.

- **CP-02 (Network Fabric) is correctly rated as the highest Phase 2 subsegment and is well-supported by external evidence.** Network topology, firewall rules, proxy requirements, and DNS architecture are categorically customer-specific and cannot be fully abstracted through ISV automation. The 2026 Ingress NGINX EOL adds incremental per-customer migration work that further supports this rating and may warrant elevation to RD=5 for 2026 deployments.

- **CP-01 and CP-04 are the subsegments most likely to have underestimated Phase 2 effort at the tail.** The 65,981+ Kubernetes environment configuration matrix (CP-01) and HSM vendor-specific PKCS#11 integration requirements (CP-04) both represent sources of customer-specific variance that the median-case ratings do not fully capture. Both may warrant TE escalation annotations for regulated-industry customers.

- **CP-10's TE=2 is the lone Phase 2 cell where TE is rated below RD.** External evidence on SIEM integration complexity (73% of practitioners cite false positives as the top challenge) suggests that customers requiring Falco-to-SIEM integration could push TE to 3, and the current rating should carry a customer-segment annotation.

- **Air-gapped customers represent a distinct Phase 2 cost tier that is not captured in the current ratings.** Replicated's data shows a 60x time-to-install multiple for air-gapped versus online deployments. For air-gapped customers, CP-06 TE should be treated as 3 rather than 2, and the overall P1 Phase 2 total should be estimated at 9–18 person-weeks rather than 6–14.

---

## Sources

| Source | URL | Data Used |
|---|---|---|
| GT1_P1_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md` | All CP-01–CP-10 ground truth FTE and difficulty data |
| three_phase_on_prem_ratings.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/three_phase_on_prem_ratings.md` | Current Phase 2 ratings and notes |
| Shadow-Soft ISV Kubernetes Deployment Case Study | https://shadow-soft.com/content/msp-isv-kubernetes-deployment-160-hours | 160-hour / 4 person-week deployment data point |
| Shadow-Soft ISV Migration Case Study | https://shadow-soft.com/content/isv-migrating-on-prem-customers-to-kubernetes-application | ISV per-customer migration patterns |
| Spectro Cloud, State of Production Kubernetes 2025 | https://www.spectrocloud.com/state-of-kubernetes-2025 | Snowflake cluster finding (>50% manual), 5+ environment average |
| Komodor 2025 Enterprise Kubernetes Report | https://komodor.com/blog/komodor-2025-enterprise-kubernetes-report-finds-nearly-80-of-production-outages/ | MTTR >50 min, MTTD ~40 min, 64 workdays lost annually, 79% of issues from system changes |
| Replicated, Instance Insights: Time to Install | https://www.replicated.com/blog/instance-insights-time-to-install | Happy path 2 hours vs. air-gap 2 weeks |
| Replicated, State of Self-Hosted Survey 2025 | https://www.replicated.com/blog/introducing-the-state-of-self-hosted-survey-2025 | 82% support self-hosted; 90-day to under-8-hour improvement; 67% use Helm |
| Connsulting, The On-Premises Revenue Trap | https://www.connsulting.io/blog/the-on-prem-revenue-trap | 30–40% engineering time on deployments; 6-month initial cycle; 50–85% personnel cost |
| Tigera, Designing On-Prem Kubernetes Networks for High Availability | https://www.tigera.io/blog/designing-on-prem-kubernetes-networks-for-high-availability/ | Per-site firewall and routing configuration requirement |
| Groundcover, Kubernetes On-Premises: Benefits, Challenges & Best Practices | https://www.groundcover.com/blog/kubernetes-on-premises | Overlay network requirement for third-party physical networks |
| Replicated, Customer Application Deployment Questionnaire | https://docs.replicated.com/vendor/planning-questionnaire | Customer environment discovery requirements |
| Keycloak/Okta SAML integration documentation | https://maybeitdepends.com/keycloak-integration-with-okta | SAML integration baseline effort data point |
| BusinessWire / Komodor press release | https://www.businesswire.com/news/home/20250917424603/en/Komodor-2025-Enterprise-Kubernetes-Report-Finds-Nearly-80-of-Production-Outages-are-Due-to-System-Changes | Report methodology confirmation |
