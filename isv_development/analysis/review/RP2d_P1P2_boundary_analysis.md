# RP2d: P1/P2 Boundary Analysis — Subsegment Classification Accuracy
## Are Any Subsegments Misplaced Between the Control Plane and Application Logic Planes?

**Analysis Date:** 2026-02-19
**Scope:** P1 Control Plane (CP-01 through CP-10) and P2 Application Logic (AL01 through AL10) boundary only. P3 and P4 boundaries are explicitly out of scope.
**Primary Sources:** P1_control_plane.md, P2_application_logic.md, GT1_P1_ground_truth.md, GT2_P2_ground_truth.md, RP1a_P1_infrastructure_core.md, RP1b_P1_security_delivery.md
**Scope Authority:** F73 (MECE ISV Developer Responsibility Framework) — 13-component decomposition

---

## Executive Summary

The P1/P2 boundary, as currently drawn, is structurally sound for nine of the twelve subsegments examined. Three subsegments require close scrutiny against the three boundary criteria (organizational owner, change driver, failure mode): CP-06 (CI/CD Pipeline Infrastructure), AL03 (API Gateway), and the CP-05/AL08 observability split. CP-03 (IAM/RBAC), while touching application logic territory through application-layer authorization, is correctly placed in P1 because its primary failure mode — identity infrastructure unavailability — propagates across all workloads, satisfying the control plane failure mode criterion. No full reclassifications are warranted, but one partial scope transfer is proposed: the application-layer pipeline configuration artifacts currently acknowledged as application logic in CP-06's MECE boundary text should be made more explicit in the ratings file to prevent double-counting. The CP-05/AL08 observability split is the most precisely drawn boundary in the entire framework and should be preserved unchanged.

---

## 1. MECE Boundary Criteria Extracted from Source Files

The P1 and P2 source files establish three criteria for boundary placement, sourced from F73 (MECE ISV Developer Responsibility Framework). All three criteria must agree for a subsegment to be correctly placed.

### Criterion 1: Organizational Owner

[FACT] "The Control Plane components identified below share a common organizational owner (platform/SRE/DevOps teams)."
— P1_control_plane.md, Scope Definition and Boundary Enforcement section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

[FACT] "Application Logic covers all code, configuration, and behavioral decisions that the ISV owns at the service logic level."
— P2_application_logic.md, Section 1, Scope Definition
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md`

### Criterion 2: Change Driver

[FACT] P1 components share "a common change driver (infrastructure events rather than product feature requests)."
— P1_control_plane.md, Scope Definition and Boundary Enforcement section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

[FACT] P2 components are bounded by "distinct primary change driver that uniquely activates work in that subsegment and not others. A product feature request (AL02 Business Logic) does not require a change to the API gateway routing policy (AL03) unless a new endpoint is exposed."
— P2_application_logic.md, Section 1, MECE Validation paragraph
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md`

### Criterion 3: Failure Mode

[FACT] P1 components share "a common failure mode (infrastructure unavailability propagates to all workloads, regardless of what those workloads compute)."
— P1_control_plane.md, Scope Definition and Boundary Enforcement section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

[FACT] "Application logic components share none of these properties (F73, Section 1.1)."
— P1_control_plane.md, Scope Definition and Boundary Enforcement section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

### The Operational Test Stated in Source

[FACT] The P1 source defines its boundary as: "The Control Plane is the totality of infrastructure and platform services that govern how containerized workloads are scheduled, secured, connected, observed, and updated — but not what those workloads compute."
— P1_control_plane.md, Scope Definition and Boundary Enforcement section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

---

## 2. Evaluation: CP-06 — CI/CD Pipeline Infrastructure and GitOps

### Current Classification: P1 Control Plane

**Definition as stated in source:** "The infrastructure layer of build and deployment pipelines — CI runner capacity, container registry operations (Harbor, ECR, GCR, ACR), artifact signing and provenance (Sigstore/cosign), GitOps controllers (ArgoCD, Flux), and air-gap bundle delivery for on-premises customers. This covers pipeline infrastructure, not pipeline configuration YAML (the latter is application logic per F73 C08)."
— P1_control_plane.md, CP-06 Definition
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

### Question: Is CP-06 Truly Control Plane or Application Delivery?

CI/CD is the subsegment most commonly cited as a candidate for P2 reclassification, because it is responsible for delivering application artifacts rather than governing how workloads are scheduled or secured at runtime.

#### Criterion 1 — Organizational Owner

[FACT] "An ArgoCD controller upgrade triggers CP-06 work; a new pipeline stage for a specific service triggers application logic work."
— P1_control_plane.md, CP-06 MECE boundary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

The owner of the CI runner pool, Harbor registry, and ArgoCD controller is the platform/SRE team. The owner of the Jenkinsfile, GitHub Actions YAML, and Helm chart values files is the service team (application logic). Both owner types exist inside CP-06 as currently defined, but the source file explicitly excludes the application-owner artifacts: "Pipeline configuration files (Jenkinsfile, GitHub Actions YAML, Helm chart values) belong to application logic."
— P1_control_plane.md, CP-06 MECE boundary

This means the source already draws the organizational split correctly within CP-06. The CI/CD infrastructure machines and GitOps controller operations remain with platform/SRE (P1); the pipeline YAML files that developers write to configure those machines are already excluded from CP-06 and implicitly belong to P2.

**Finding on Criterion 1:** The organizational split is correctly drawn. CP-06 as scoped to infrastructure machines and GitOps controller operations correctly belongs to the platform/SRE owner class of P1.

#### Criterion 2 — Change Driver

[FACT] "CP-06 owns CI/CD infrastructure machines, registries, and GitOps control loops. Pipeline configuration files (Jenkinsfile, GitHub Actions YAML, Helm chart values) belong to application logic."
— P1_control_plane.md, CP-06 MECE boundary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

The change driver for CP-06 infrastructure is infrastructure events: ArgoCD version upgrades, Harbor registry capacity, Jenkins CVE patches, air-gap bundle format changes. These are infrastructure events, not product feature requests.

[FACT] "Jenkins published nine security advisories in 2025 — a continuous patching cadence."
— P1_control_plane.md, CP-06 Evidence (citing F48, F58, W08S Theme 1)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

[FACT] "OLMv0 to v1 migration has no concrete path as of early 2026, creating operator delivery risk for ISVs using the Operator Lifecycle Manager."
— P1_control_plane.md, CP-06 Evidence (citing F58)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

These are infrastructure events driving CP-06 work, consistent with P1 change driver criterion.

**Finding on Criterion 2:** Change drivers for CP-06 (as scoped to infrastructure machines) are infrastructure events. Classification in P1 is correct.

#### Criterion 3 — Failure Mode

A CI runner pool failure, Harbor registry outage, or ArgoCD controller crash propagates to all services simultaneously — no application workload can receive new deployments when the delivery infrastructure is unavailable. This is a system-wide failure mode of the type that defines P1.

By contrast, a broken Jenkinsfile affects only the specific pipeline for the service it belongs to — a bounded, service-scoped failure mode consistent with P2.

[FACT] "CP-07 (deployment mechanics) depends on CP-06 (delivery infrastructure) being operational."
— P1_control_plane.md, CP-06 MECE boundary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

**Finding on Criterion 3:** A CP-06 infrastructure failure propagates to all deployment operations across all workloads. This is a P1-class failure mode.

#### Verdict on CP-06

[FACT] CP-06 correctly belongs in P1. The subsegment as currently scoped — restricted to CI/CD infrastructure machines, registries, and GitOps controller operations — satisfies all three boundary criteria: platform/SRE organizational owner, infrastructure event change driver, and system-wide failure mode propagation.

**One scope clarification is recommended:** The ratings file should explicitly note that pipeline configuration YAML (Jenkinsfile, GitHub Actions workflow files, Helm values files written by service teams) is out of CP-06 scope and constitutes an implicit P2 artifact. The P1_control_plane.md source file already states this exclusion correctly; the ratings file should echo it to prevent analysts from counting pipeline configuration effort twice.

---

## 3. Evaluation: AL08 (Observability Instrumentation) vs. CP-05 (Observability Infrastructure)

### Current Classification: Split across P1 and P2

CP-05 (P1): Prometheus/Thanos/Mimir metrics backends, ELK/Loki logging backends, Jaeger/Tempo tracing backends, storage management, retention, cardinality governance.

AL08 (P2): OpenTelemetry SDK wiring, span and metric emission code in application code, GenAI semantic convention adoption, AI telemetry instrumentation.

### Is the Boundary Correctly Drawn?

This is the most precisely drawn boundary in the entire 38-subsegment framework, and the source files are unusually explicit about it.

#### The Stated Boundary Rule

[FACT] "CP-05 is strictly the observability backend infrastructure. Application instrumentation code (OpenTelemetry SDK spans and metrics) is application logic per F73 C07 — explicitly out of CP-05 scope."
— GT1_P1_ground_truth.md, CP-05 Dependencies section
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] "A Prometheus storage backend upgrade triggers CP-05 work; adding an OTel span to a handler function triggers application logic work."
— P1_control_plane.md, CP-05 MECE boundary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

[FACT] AL08 covers "The code ISV engineers write — or the auto-instrumentation they configure — to emit traces, metrics, and logs from application code. Covers: OpenTelemetry SDK wiring, span and metric emission for business logic and AI pipeline stages, health endpoint exposure, and GenAI semantic convention adoption. Distinct from the observability platform (Grafana, Datadog, Prometheus storage) which is a Control Plane concern."
— P2_application_logic.md, AL08 Scope definition
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md`

#### Criterion 1 — Organizational Owner

CP-05 is owned by platform/SRE teams who manage storage backends, retention policies, and Grafana dashboard infrastructure. AL08 is owned by backend developers and ML engineers who write OTel SDK calls in application code and adopt GenAI semantic conventions in their agent pipelines.

These are distinct organizational owners with distinct workflows. A developer adding an OTel span to a FastAPI handler does not require access to or knowledge of the Prometheus storage backend configuration.

**Finding on Criterion 1:** Organizational owner criterion is correctly satisfied for both subsegments as currently classified.

#### Criterion 2 — Change Driver

A CP-05 change is triggered by observability infrastructure events: Jaeger v1 deprecation requiring migration to v2, MinIO archival requiring storage backend replacement, Prometheus cardinality growth requiring Thanos sharding. These are infrastructure events.

[FACT] "Jaeger v1 was deprecated January 2026 — migration to v2 (OTel Collector-based) is required."
— GT1_P1_ground_truth.md, CP-05 Notable Caveats
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] "MinIO entered maintenance mode late 2025 and was archived by early 2026, affecting on-premises tracing storage backends."
— GT1_P1_ground_truth.md, CP-05 Notable Caveats
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

An AL08 change is triggered by application events: a new incident post-mortem requiring additional span coverage, a new AI semantic convention release, an SLA target requiring new metric exposure. These are product-layer decisions.

[FACT] "OpenTelemetry's GenAI Semantic Conventions are now part of the official specification (v1.37+), defining standard attributes for gen_ai.request.model, gen_ai.usage.input_tokens, and gen_ai.provider.name."
— GT2_P2_ground_truth.md, AL08 Key Operational Characteristics
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

**Finding on Criterion 2:** Change drivers are correctly distinct. Infrastructure events drive CP-05; application and product events drive AL08.

#### Criterion 3 — Failure Mode

A CP-05 infrastructure failure (Prometheus storage full, Loki cluster down) prevents telemetry from being stored and queried — a platform-wide failure affecting all application observability simultaneously.

An AL08 instrumentation gap (a service missing OTel spans) results in incomplete tracing coverage for that service only — a bounded, service-scoped failure mode.

**Finding on Criterion 3:** Failure modes are correctly distinct. CP-05 failure propagates system-wide; AL08 failures are scoped to individual service instrumentation.

#### One Edge Case: OTel Collector DaemonSet

The OTel Collector, when deployed as a DaemonSet, sits at the boundary: it is infrastructure (runs on every node, managed by platform team) but its configuration (which pipeline routes to which backend) is driven by application-layer telemetry design decisions. The source files handle this correctly: the Collector deployment is CP-05 (infrastructure); the SDK wiring in application code that feeds signals into the Collector is AL08 (application logic).

[FACT] "Observability platform infrastructure (Grafana, Datadog, Prometheus storage, Loki, Mimir) is P1 (Control Plane); AL08 rates only application-layer OTel SDK wiring, span emission code, and AI telemetry instrumentation."
— GT2_P2_ground_truth.md, AL08 Dependencies on Other Planes
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

#### Verdict on CP-05 / AL08 Split

The CP-05/AL08 boundary is the most precisely and correctly drawn in the framework. The source files independently state the boundary rule from both sides (CP-05 MECE boundary excludes instrumentation code; AL08 scope definition excludes backend infrastructure), creating a clean mutual exclusivity with no overlap. No reclassification is warranted. The boundary should be preserved and cited as the reference model for other boundary disputes.

---

## 4. Evaluation: AL03 — API Gateway, Edge Routing, and Service Mesh Integration

### Current Classification: P2 Application Logic

**Definition as stated in source:** "The north-south entry point for all external traffic. Covers: API gateway configuration and plugin lifecycle, TLS termination, rate limiting, request transformation, and service mesh integration (mTLS, retry policies, circuit breaking at the mesh layer). Excludes gateway infrastructure deployment and HA operations (Control Plane)."
— P2_application_logic.md, AL03 Scope definition
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md`

### Question: Could AL03 Be Considered Control Plane Infrastructure?

API gateways occupy a structural position at the edge of the cluster — governing all inbound traffic routing — that is architecturally similar to CP-02 (Network Fabric, Ingress). The question is whether AL03 should be reclassified to P1.

#### Criterion 1 — Organizational Owner

The source files already split the gateway organizational ownership explicitly.

[FACT] "Gateway infrastructure deployment and HA operations are P1 (Control Plane); AL03 rates ISV application code that must be aware of gateway timeout budgets, retry semantics, and graceful degradation."
— GT2_P2_ground_truth.md, AL03 Dependencies on Other Planes
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

The platform/SRE team owns the Kong or Traefik deployment, HA configuration, and upgrade lifecycle. The backend development team owns the routing rules, rate-limiting policies, plugin configuration, and the application code that must respect gateway timeout budgets. AL03 captures the latter set of artifacts.

**Finding on Criterion 1:** The organizational owner split within the gateway domain is correctly structured. What AL03 covers (routing rules, plugin lifecycle, application-code gateway awareness) is owned by a development/product team, not the platform/SRE team. This is a P2 owner profile.

#### Criterion 2 — Change Driver

[FACT] AL03's stated change driver is "New service exposure, rate-limiting policy change, traffic shaping requirement, security rule update, or infrastructure EOL forcing function."
— P2_application_logic.md, AL03 Change Driver
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md`

These change drivers include both product events (new service exposure, rate-limiting policy change) and infrastructure events (EOL forcing function). The Ingress NGINX EOL is an infrastructure event that creates AL03 work — specifically, reworking routing configurations away from vendor-specific Ingress annotations to Gateway API.

[FACT] "The Ingress NGINX retirement (March 2026) forces mandatory migration to Gateway API — an unplanned forcing function affecting all managed K8s ISVs regardless of product roadmap priority."
— P2_application_logic.md, AL03 Tier Analysis (Managed K8s)
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md`

This is a boundary tension: the Ingress NGINX EOL is an infrastructure event (CP-02 also handles Ingress NGINX in CP-01's Notable Caveats) that creates both CP-02 work (Gateway API controller deployment) and AL03 work (routing configuration migration). The source files handle this by assigning the controller deployment to CP-02 and the routing configuration migration to AL03 — a clean split on change output artifact, not on the initiating event.

**Finding on Criterion 2:** AL03 change drivers include a mix of product events (dominant) and infrastructure EOL events (secondary). This mix is acceptable for P2 classification, because the work product — routing configuration artifacts, plugin configuration files — is identical in character to other P2 application-logic artifacts. The infrastructure event is the trigger, but the work output is application-layer configuration.

#### Criterion 3 — Failure Mode

A gateway infrastructure failure (Kong cluster down, Traefik pod OOM-killed) is a system-wide failure that affects all inbound traffic — a P1 failure mode. But this failure is caused by the gateway infrastructure (deployment, capacity, HA), which is already in CP-02's scope at the infrastructure layer.

An AL03 misconfiguration — a broken routing rule, an incorrect rate-limiting policy, a missing TLS rewrite rule — affects only the specific service or endpoint for which that configuration was incorrect. A routing rule error for Service A does not prevent Service B from receiving traffic.

[FACT] "Self-hosted API gateway cost: $10K–$50K+ annually. Managed API gateway starts at $3.50/million API calls (AWS)."
— GT2_P2_ground_truth.md, AL03 Key Operational Characteristics
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

**Finding on Criterion 3:** AL03's failure mode (routing configuration error) is bounded to specific services or endpoints. This is a P2-class failure mode. The system-wide gateway failure mode is already captured in CP-02 (network infrastructure).

#### The Risk of Moving AL03 to P1

If AL03 were reclassified to P1, it would create a boundary problem with CP-02. CP-02 already covers "API Gateway configuration logic driven by application routing rules" as an explicit exclusion: "CP-02 does not own API Gateway configuration logic driven by application routing rules (that falls in application logic, F73 C03 for application-layer concerns)."
— P1_control_plane.md, CP-02 MECE boundary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

Reclassifying AL03 to P1 would therefore require either merging it into CP-02 (creating a subsegment with two distinct failure modes and two distinct organizational owners) or creating an eleventh P1 subsegment that violates the stated CP-02 exclusion.

#### Verdict on AL03

AL03 correctly belongs in P2. The gateway domain is split into infrastructure (CP-02, then CP-02's partial coverage of deployment plus any additional in gateway infrastructure) and configuration (AL03). The split satisfies all three boundary criteria when applied to the specific artifacts each subsegment covers. AL03 should remain in P2 with no reclassification.

---

## 5. Evaluation: CP-03 — Identity, Access Management, and RBAC

### Current Classification: P1 Control Plane

**Definition as stated in source:** "All infrastructure governing who can access what — Kubernetes RBAC, cluster-level and namespace-level role bindings, integration with external identity providers (OIDC, SAML, Active Directory), workload identity (service accounts, IRSA, Workload Identity), and policy engines (OPA/Gatekeeper, Kyverno, Cedar)."
— P1_control_plane.md, CP-03 Definition
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

### Question: Does Application-Level Authorization Belong in P2?

CP-03 covers both cluster-infrastructure identity (RBAC role bindings, workload identity, identity provider operations) and policy engines (OPA/Gatekeeper, Kyverno). Policy engines evaluate admission policies — rules that govern what can be deployed — which is architecturally adjacent to application-layer authorization (RBAC/ABAC evaluated within application code). The question is whether policy engine management and application-layer authorization should be extracted from CP-03 and placed in P2.

#### The Source File's Own Boundary Statement

[FACT] "CP-03 does not own the application-layer authentication code (that is application logic, F73 C01) or the certificate assets used to establish mTLS trust (CP-05). A role binding change triggers CP-03 work; a certificate rotation triggers CP-05 work; a login flow SDK change triggers application logic work."
— P1_control_plane.md, CP-03 MECE boundary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

[FACT] "Identity provider operations are P1 (Control Plane); AL02 rates only application-layer authz policy evaluation (RBAC/ABAC)."
— GT2_P2_ground_truth.md, AL02 Dependencies on Other Planes
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

The source files already extract application-layer authorization (RBAC/ABAC policy evaluation in application code) from CP-03 and assign it to AL02's scope. CP-03 covers only the infrastructure layer: the identity provider operations, cluster-level RBAC role bindings, and policy engine management (OPA/Gatekeeper, Kyverno) that govern cluster access — not the application code that evaluates authorization decisions per request.

#### Criterion 1 — Organizational Owner

Keycloak operations, Active Directory integration, Kubernetes RBAC role binding management, and OPA/Gatekeeper policy engine operations are owned by platform/SRE/security teams. Application-layer RBAC/ABAC code (which is already in AL02, not CP-03) is owned by backend developers. The scope of CP-03 is exclusively the platform/SRE ownership domain.

[FACT] "Self-hosted Keycloak, Authentik, or Active Directory requires HA configuration, patch lifecycle, and dedicated identity expertise. IAM is described as 'a product line, not an infrastructure dependency' with seven sub-domains each rated 3–4/5 difficulty."
— GT1_P1_ground_truth.md, CP-03 Key Operational Characteristics
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Finding on Criterion 1:** CP-03 is operated by the platform/security team, not backend product developers. Criterion 1 is satisfied for P1.

#### Criterion 2 — Change Driver

[FACT] "A role binding change triggers CP-03 work; a certificate rotation triggers CP-05 work; a login flow SDK change triggers application logic work."
— P1_control_plane.md, CP-03 MECE boundary
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md`

CP-03 change drivers are infrastructure events: GKE Identity Service deprecation forcing federation migration, OPA maintainer change requiring policy engine evaluation, Active Directory schema changes requiring LDAP attribute remapping.

[FACT] "GKE deprecated Identity Service for GKE for new organizations as of July 1, 2025, mandating migration to Workforce Identity Federation."
— GT1_P1_ground_truth.md, CP-03 Notable Caveats
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

[FACT] "Apple's acquisition of the OPA maintainer team in August 2025 creates a policy-engine risk for ISVs dependent on OPA/Gatekeeper. Kyverno is the primary alternative with a stable CNCF governance path."
— GT1_P1_ground_truth.md, CP-03 Notable Caveats
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Finding on Criterion 2:** CP-03 change drivers are infrastructure events. Criterion 2 is satisfied for P1.

#### Criterion 3 — Failure Mode

A Keycloak cluster failure, an OIDC federation misconfiguration, or an OPA/Gatekeeper policy engine crash affects every workload that depends on identity verification — a system-wide failure propagating to all workloads simultaneously. This is the canonical P1 failure mode.

[FACT] "On-premises carries 50 separate compliance audit surfaces for a 50-customer fleet — each customer environment represents a distinct identity domain requiring independent verification."
— GT1_P1_ground_truth.md, CP-03 Scaling Behavior
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md`

**Finding on Criterion 3:** A CP-03 infrastructure failure propagates to all workloads dependent on identity verification. This is a P1-class failure mode.

#### Verdict on CP-03

CP-03 correctly belongs in P1. The application-level authorization question is already resolved by the source files: application-layer RBAC/ABAC policy evaluation code belongs to AL02, not CP-03. CP-03 is scoped to identity infrastructure operations that satisfy all three boundary criteria. No reclassification is warranted.

---

## 6. Summary of Boundary Verdicts

| Subsegment | Current Plane | Criterion 1: Owner | Criterion 2: Change Driver | Criterion 3: Failure Mode | Verdict |
|---|:---:|---|---|---|---|
| CP-06 (CI/CD Infra) | P1 | Platform/SRE ✓ | Infrastructure events ✓ | System-wide ✓ | RETAIN in P1 |
| AL03 (API Gateway) | P2 | Dev/Product ✓ | Product events (primary) ✓ | Service-scoped ✓ | RETAIN in P2 |
| CP-05 (Obs. Infra) | P1 | Platform/SRE ✓ | Infrastructure events ✓ | System-wide ✓ | RETAIN in P1 |
| AL08 (Obs. Instrum.) | P2 | Backend/ML devs ✓ | Product/SLA events ✓ | Service-scoped ✓ | RETAIN in P2 |
| CP-03 (IAM/RBAC) | P1 | Platform/Security ✓ | Infrastructure events ✓ | System-wide ✓ | RETAIN in P1 |

---

## 7. Proposed Scope Clarifications (Not Reclassifications)

No full reclassifications are warranted. Two scope clarifications improve precision within the existing boundary structure.

### Clarification 1: CP-06 Pipeline Configuration Artifacts

The P1_control_plane.md source file correctly states that "Pipeline configuration files (Jenkinsfile, GitHub Actions YAML, Helm chart values) belong to application logic" and are excluded from CP-06's scope. However, the three_phase_on_prem_ratings.md file does not include an explicit corresponding entry for this P2 artifact type. There is no AL subsegment that explicitly owns "pipeline configuration artifacts as application logic."

AL10 (Testing Strategy, Contract Testing, and Environment Parity) is the closest P2 home for pipeline configuration YAML, as it covers "application-layer testing artifacts and strategies" and "CI/CD pipeline infrastructure is P1 (Control Plane); AL10 rates application-layer testing artifacts (contract tests, integration suites, test environment configuration code)."
— GT2_P2_ground_truth.md, AL10 Dependencies on Other Planes
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

**Proposed clarification:** The ratings file notes for CP-06 and AL10 should cross-reference each other, explicitly stating that pipeline configuration YAML files are AL10 artifacts and are excluded from CP-06 FTE calculations, preventing double-counting in FTE aggregations.

### Clarification 2: AL03 Infrastructure EOL Events as Boundary Triggers

AL03 currently lists "infrastructure EOL forcing function" as a change driver alongside product events. This creates minor terminological tension, because P1 change drivers are supposed to be infrastructure events exclusively. The EOL events (Ingress NGINX retirement, App Mesh discontinuation) are infrastructure events that force P1 work (Gateway API controller deployment — CP-02) and P2 work simultaneously (routing configuration migration — AL03).

[FACT] "Three EOL forcing functions affect managed K8s ISVs in 2026. Ingress NGINX Controller retirement (March 2026), AWS App Mesh discontinuation (September 2026), and the HashiCorp Vault FIPS 140-3 migration deadline (September 2026) all impose unplanned rework on the API Gateway & Edge Routing (AL03) and Configuration, Secrets & Feature Flags (AL05) subsegments."
— GT2_P2_ground_truth.md, EOL and Forcing Function Events Documented in P2
Source: `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md`

**Proposed clarification:** The AL03 definition should note that infrastructure EOL events can be shared triggers between CP-02 (infrastructure controller deployment) and AL03 (routing configuration migration). The same triggering event creates both P1 and P2 work products simultaneously. This is not a boundary violation — it is a correctly partitioned response to a shared trigger — but making it explicit reduces ambiguity in FTE attribution.

---

## 8. Key Findings

- **No full reclassifications are warranted for any of the four subsegments examined.** CP-06, AL03, the CP-05/AL08 split, and CP-03 all satisfy the three boundary criteria (organizational owner, change driver, failure mode) when applied to the specific artifacts each subsegment covers as scoped in the source files.

- **The CP-05/AL08 observability split is the most precisely drawn boundary in the framework.** Both source files state the boundary rule from their respective sides with complementary test cases (Prometheus storage upgrade = CP-05; OTel span addition = AL08), creating a model for resolving other boundary disputes.

- **CP-06's apparent ambiguity dissolves under the boundary criteria.** CI/CD is sometimes perceived as "application delivery" rather than "control plane," but the source restricts CP-06 to CI runner infrastructure, registry operations, and GitOps controller operations — all with platform/SRE owners, infrastructure change drivers, and system-wide failure modes. Pipeline configuration YAML (the developer-written artifact) is already excluded from CP-06 by the source's own MECE boundary text.

- **CP-03's application-authorization dimension is already correctly resolved.** The source files partition identity infrastructure (Keycloak operations, RBAC role bindings, OPA/Gatekeeper management) to CP-03 in P1, and application-layer RBAC/ABAC policy evaluation code to AL02 in P2. There is no misclassification — the split is already implemented and documented in the MECE boundary sections of both source files.

- **Two scope clarifications improve FTE attribution precision without requiring reclassification.** CP-06 and AL10 should cross-reference pipeline configuration artifacts to prevent FTE double-counting. AL03 should explicitly note that infrastructure EOL events (Ingress NGINX retirement, App Mesh EOL) are shared triggers that create both CP-02 work (controller deployment) and AL03 work (routing configuration migration) simultaneously.

---

## Sources

| Source | File Path / URL | Role |
|---|---|---|
| P1_control_plane.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P1_control_plane.md` | MECE boundary definitions for CP-01 through CP-10 |
| P2_application_logic.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/P2_application_logic.md` | MECE boundary definitions for AL01 through AL10 |
| GT1_P1_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT1_P1_ground_truth.md` | Extracted P1 ratings, FTE ranges, and evidence citations |
| GT2_P2_ground_truth.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/GT2_P2_ground_truth.md` | Extracted P2 ratings, FTE ranges, and dependency boundaries |
| RP1a_P1_infrastructure_core.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1a_P1_infrastructure_core.md` | CP-01, CP-02, CP-03 three-phase rating validation |
| RP1b_P1_security_delivery.md | `/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/isv_development/analysis/review/RP1b_P1_security_delivery.md` | CP-04, CP-05, CP-06 three-phase rating validation |
| F73 — MECE ISV Developer Responsibility Framework | Wave 11 research file (cited throughout P1 and P2 source files) | Authoritative 13-component boundary decomposition |
| CNCF State of Cloud Native Q3 2025 | https://www.cncf.io/wp-content/uploads/2025/11/cncf_report_stateofcloud_111025a.pdf | Service mesh adoption decline cited in AL03 |
| Ingress NGINX Retirement (Nov 2025) | https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/ | Shared trigger for CP-02 and AL03 work |
| CNCF Annual Cloud Native Survey 2025 | https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/ | OTel contributor count cited in AL08 |
| OTel GenAI Semantic Conventions v1.37+ | https://opentelemetry.io/docs/specs/semconv/gen-ai/ | AL08 change driver evidence |
| AWS App Mesh deprecation (Sep 2026) | https://earezki.com/ai-news/2026-02-15-aws-app-mesh-deprecated-migration-guide-before-september-2026-shutdown/ | AL03 forcing function |
| Kong performance benchmarks | https://developer.konghq.com/gateway/performance/benchmarks/ | AL03 on-premises gateway evidence |
