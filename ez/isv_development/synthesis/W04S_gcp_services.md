# W04S — GCP Cloud-Native Managed Services: Cross-Agent Synthesis

**Synthesis Date:** 2026-02-19
**Input Files:** F24 (Compute), F25 (Data), F26 (AI/ML), F27 (Security), F28 (Observability), F29 (Networking), F30 (CI/CD), F31 (Messaging), F31a (Infrastructure Integration)
**Scope:** GCP managed services evaluated for ISV deployment model comparison (on-premises vs. managed Kubernetes vs. cloud-native)

---

## 1. Executive Summary

GCP's cloud-native managed service portfolio eliminates the vast majority of undifferentiated infrastructure operations for ISVs building AI-driven SaaS, with aggregate on-premises FTE requirements of [7.25-14.0 FTE for security alone](https://cloud.google.com/security-command-center/pricing) (from F27) collapsing to approximately 1.4 FTE of policy configuration and triage. Across all nine domains, services rated Difficulty 1-2 (Cloud Run, Pub/Sub, Cloud Logging, Secret Manager, Artifact Registry) form a zero-ops foundation, while Difficulty 3-5 services (TPU training, Binary Authorization, SCC Enterprise, Managed Kafka) still require meaningful ISV expertise. Critical deprecations -- [Pub/Sub Lite shutdown March 18, 2026](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) (from F31) and [Document AI HITL removal January 2025](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new) (from F26) -- require active migration planning, while maturity gaps in serverless health checks and OTLP metrics (Preview) demand compensating controls.

---

## 2. Key Themes

### Theme 1: The Serverless Core Eliminates Entire Operational Categories

The strongest finding across agents is that GCP's serverless tier -- Cloud Run, Cloud Functions 2nd gen, Pub/Sub, BigQuery, Firestore, Cloud Workflows, and Cloud Tasks -- removes not just individual tasks but entire operational job functions. Cloud Run with [GPU support now GA (NVIDIA L4, ~5-second startup)](https://docs.cloud.google.com/run/docs/configuring/services/gpu) (from F24) eliminates GPU driver management, OS patching, and capacity planning at Difficulty 1/5 versus 5/5 on-premises. [Cloud Pub/Sub's 99.95% SLA](https://cloud.google.com/pubsub/sla) with at-least-once delivery (from F31) replaces self-hosted Kafka clusters that require [a minimum of 2.3 FTE](https://arxiv.org/pdf/2510.04404) (from F31). BigQuery provides ["zero infrastructure management"](https://docs.cloud.google.com/bigquery/docs/introduction) (from F25) for analytics, while [Cloud Workflows at $0.01/1,000 steps](https://cloud.google.com/workflows/pricing) (from F31) replaces self-hosted Airflow requiring 0.5-1.5 FTE.

The CI/CD stack reinforces this pattern: [Cloud Build eliminates all build server operations](https://cloud.google.com/build) (from F30), reducing CI infrastructure FTE from 0.5-1.0 to ~0.1 per engineering team. [Artifact Registry's continuous vulnerability scanning updated multiple times daily](https://docs.cloud.google.com/artifact-registry/docs/analysis) (from F30) with SBOM generation (GA) replaces Harbor or Nexus self-hosting entirely. The observability stack completes the picture: [Cloud Logging at $0.50/GiB after 50 GiB free](https://cloud.google.com/stackdriver/pricing) (from F28) and [Managed Prometheus with 24-month retention at no storage cost](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) (from F28) eliminate ELK clusters, Prometheus servers, and Thanos/Cortex long-term storage.

### Theme 2: Security and Identity Converge on Zero-Trust with Minimal ISV Effort

GCP's security portfolio achieves the largest proportional FTE reduction of any domain. [Workload Identity Federation eliminates the entire service account key lifecycle](https://docs.cloud.google.com/iam/docs/workload-identity-federation) (from F27), replacing static credentials with short-lived federated tokens at zero cost. [Cloud KMS with Cloud HSM delivers FIPS 140-2 Level 3 compliance](https://cloud.google.com/kms/docs/hsm) (from F27) without the [$50K-$200K+ in HSM hardware](https://cloud.google.com/kms/docs/hsm) (from F27) required on-premises. [Security Command Center's GA agentless vulnerability scanning](https://security.googlecloudcommunity.com/news-announcements-9/google-security-command-center-scc-h2-2025-product-release-summary-6574) (from F27) covers both VMs and GKE without agent deployment, while [Cloud Armor's Adaptive Protection uses per-application ML models](https://cloud.google.com/security/products/armor) (from F27) for DDoS defense.

The infrastructure integration file (F31a) confirms that [Secret Manager + Workload Identity is the mandatory secrets pattern across all compute types](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component) (from F31a), with GKE using CSI driver mounts, Cloud Run using environment variable or volume injection, and Cloud Functions using the metadata server -- all eliminating long-lived credentials.

### Theme 3: AI/ML Services Offer Deep Abstraction with Proportional Lock-In

Vertex AI consolidates model training, inference, vector search, pipelines, and agent orchestration under a single managed control plane. [Vector Search 2.0 (December 2025) demonstrates 9.6ms P95 latency at 5,000 QPS on one billion vectors](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931) (from F26), eliminating self-managed vector databases entirely. [Gemini model pricing spans from $0.15/M tokens (2.0 Flash input) to $10/M tokens (2.5 Pro output)](https://cloud.google.com/vertex-ai/generative-ai/pricing) (from F26) with 50% batch discounts. [Vertex AI Pipelines at $0.03/run](https://cloud.google.com/vertex-ai/pricing) (from F26) replaces self-managed Kubeflow at significant FTE savings.

However, lock-in is the steepest here. [Vertex AI endpoints do not use Cloud Deploy, do not support Binary Authorization, and have limited OTEL instrumentation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) (from F31a, F26). ISVs adopting Vertex AI Pipelines (KFP/TFX), RAG Engine, and Agent Builder accept GCP-proprietary managed services with no direct portability path (from F26). TPU workloads (v5e, v5p) remain Difficulty 3-4 regardless of deployment model due to [deep ML framework expertise requirements (JAX, PyTorch/XLA)](https://docs.cloud.google.com/tpu/docs/v5e) (from F24).

### Theme 4: Networking and Observability Provide Structural Advantages That Cannot Be Replicated On-Premises

GCP's networking stack is built on the [same private global infrastructure powering Google Search and YouTube](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) (from F29), operating from [over 80 GFE locations worldwide](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) (from F29). Cloud Load Balancing's single-anycast-IP model with no pre-warming eliminates BGP configuration, SSL lifecycle management, and capacity planning for traffic spikes. [Private Service Connect eliminates CIDR overlap constraints](https://cloud.google.com/private-service-connect) (from F29) that plague VPC peering at scale, while [Traffic Director / Cloud Service Mesh's global control plane](https://cloud.google.com/service-mesh/docs/overview) (from F29) replaces per-cluster istiod management.

Observability gains a structural edge through [native OTLP ingestion via telemetry.googleapis.com](https://www.infoq.com/news/2025/09/gcp-opentelemetry-adoption/) (from F28) enabling vendor-neutral instrumentation, and [Cloud Run providing zero-instrumentation distributed tracing](https://cloud.google.com/run/docs/trace) (from F28) for automatic latency visibility. [Managed Prometheus pricing dropped 60%](https://cloud.google.com/stackdriver/pricing) (from F28), reaching $0.024/million samples at volume with 24-month retention -- a capability that on-premises requires Thanos or Cortex clusters at significant FTE cost.

### Theme 5: Deprecations, Maturity Gaps, and Residual ISV Burden

Several critical deprecations require ISV attention:
- [Pub/Sub Lite shuts down March 18, 2026](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) (from F31) -- ISVs must migrate to Managed Kafka or standard Pub/Sub
- [Document AI HITL deprecated January 2025](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new) (from F26) -- alternatives require partner engagement
- [Cloud Source Repositories closed to new customers June 2024](https://docs.cloud.google.com/source-repositories/docs/migration-guides) (from F30) -- GitHub/GitLab with WIF is the path forward
- [Legacy Binary Authorization CV ends May 2025](https://cloud.google.com/binary-authorization/docs/overview-cv) (from F30) -- migration to check-based policies required
- [Artifact Registry Advanced Vulnerability Insights deprecated, shutdown June 2026](https://docs.cloud.google.com/artifact-registry/docs/analysis) (from F31a)

Maturity gaps that demand compensating controls:
- [Health checks are not supported for serverless NEG backends](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) (from F31a) -- Cloud Monitoring uptime checks required
- [OTLP metrics in Preview](https://cloud.google.com/blog/products/management-tools/otlp-opentelemetry-protocol-for-google-cloud-monitoring-metrics) (from F31a) -- not GA for production use
- [Cloud Functions: no direct metric write supported](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach) (from F31a) -- log-based metrics only
- [Cloud Debugger deprecated May 2023, Snapshot Debugger archived September 2023](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation) (from F28) -- no managed replacement exists

---

## 3. Difficulty and FTE Summary Table

| Domain | Service | On-Prem Difficulty | Cloud-Native Difficulty | On-Prem FTE | Cloud-Native FTE | Source |
|---|---|---|---|---|---|---|
| Compute | Cloud Run (GPU) | 5/5 | 1/5 | 1.0-2.0 | 0.0-0.1 | F24 |
| Compute | Cloud Batch | 4/5 | 1/5 | 0.5-1.0 | 0.0 | F24 |
| Compute | TPU v5p training | 5/5 | 4/5 | N/A | Deep ML FTE | F24 |
| Data | Cloud SQL (Enterprise Plus) | 4/5 | 2/5 | 0.5-1.0 | 0.1-0.2 | F25 |
| Data | Cloud Spanner | 5/5 | 1/5 | 2.0+ | 0.1 | F25 |
| AI/ML | Vertex AI Pipelines | 5/5 | 2/5 | 1.0-2.0 | ~0.1 | F26 |
| AI/ML | Vector Search 2.0 | 4/5 | 1/5 | 0.5-1.0 | 0.0 | F26 |
| Security | Full stack (IAM through BeyondCorp) | N/A | 2-3/5 | 7.25-14.0 | ~1.4 | F27 |
| Observability | Operations Suite (full) | 4/5 | 1-2/5 | 1.5-3.0 | ~0.2 | F28 |
| Networking | LB + DNS + CDN + Mesh | 4-5/5 | 1-2/5 | 3.0-6.0 | ~0.5 | F29 |
| CI/CD | Cloud Build + Deploy + Registry | 4/5 | 1-2/5 | 1.0-2.0 | 0.1-0.2 | F30 |
| Messaging | Pub/Sub + Managed Kafka | 4-5/5 | 1-2/5 | 2.0-3.0 | ~0.1 | F31 |
| Integration | Cross-service wiring | 3-4/5 | 2-3/5 | Included above | 3-6 hrs/service | F31a |

FTE estimates are directional benchmarks. Security FTEs from F27 are marked UNVERIFIED. Messaging FTEs from F31 cite [ArXiv 2510.04404](https://arxiv.org/pdf/2510.04404) for Kafka (2.3 FTE minimum).

---

## 4. Cross-Agent Patterns and Contradictions

**Consistent patterns across all 9 agents:**
- Difficulty ratings uniformly drop 2-4 points when moving from on-premises to cloud-native for commodity infrastructure (networking, compute, data, observability).
- Services built on Google's internal infrastructure (Monarch for metrics, Maglev for load balancing, Spanner for state) provide capabilities that cannot be replicated by ISVs at any FTE investment.
- Workload Identity Federation appears in F27 (security), F30 (CI/CD), and F31a (integration) as the universal authentication primitive, confirming its cross-cutting importance.

**Apparent contradictions or tensions:**
- F26 (AI/ML) highlights Vertex AI as eliminating infrastructure operations, while F31a reveals Vertex AI endpoints sit outside the standard 8-component integration stack (no Cloud Deploy, no Binary Authorization, limited OTEL). The operational simplicity claimed in F26 applies to the ML layer but not to production deployment wiring.
- F28 (Observability) recommends OTLP as the instrumentation standard, but F31a notes OTLP metrics remain in Preview. ISVs face a choice between the recommended path (OTLP) and the production-ready path (Managed Prometheus + native metrics).
- F29 (Networking) estimates 3-6 FTE for on-premises networking equivalents, while individual service agents estimate smaller per-domain FTEs. These are not additive; the networking estimate includes capabilities that overlap with security (Cloud Armor) and observability (uptime checks).

---

## 5. Open Questions for Downstream Synthesis

1. **Cost crossover analysis:** At what ISV scale (monthly spend, number of services, message volume) does the aggregate GCP managed service cost exceed the FTE cost of self-hosting? The per-service pricing data exists across all agents but has not been modeled against headcount economics.

2. **Multi-cloud portability cost:** F26 identifies deep Vertex AI lock-in; F28 notes OTLP reduces observability lock-in. What is the estimated re-engineering cost to exit GCP for each domain, and which domains have viable open-source alternatives (e.g., Apache Beam for Dataflow, KFP for Vertex Pipelines)?

3. **Compliance surface area:** F27 covers GCP security services, but the cross-domain compliance burden (SOC 2, HIPAA, FedRAMP) across data (F25), AI (F26), and messaging (F31) has not been consolidated. Which GCP services carry BAA eligibility, and which require ISV-side compliance work?

4. **Deprecation migration effort:** The five deprecations identified in Theme 5 each require migration work. What is the estimated engineering effort per deprecation, and what is the risk of compounding migrations for ISVs adopting multiple affected services?

5. **Vertex AI integration gap resolution:** F31a identifies that Vertex AI endpoints are outside the standard onboarding stack. Is Google working to integrate Vertex AI endpoints with Cloud Deploy and Binary Authorization, or will this remain a permanent architectural divergence?

---

## 6. Sources

### F24 — GCP Compute
- [Cloud Run GPU support](https://docs.cloud.google.com/run/docs/configuring/services/gpu)
- [Cloud Run autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling)
- [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
- [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e)
- [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)
- [Cloud Batch](https://cloud.google.com/batch)
- [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus)

### F25 — GCP Data
- [Cloud SQL editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro)
- [Cloud Spanner](https://cloud.google.com/spanner)
- [Spanner 2025 SIGMOD Award](https://cloud.google.com/blog/products/databases/spanner-wins-the-2025-acm-sigmod-systems-award)
- [BigQuery overview](https://docs.cloud.google.com/bigquery/docs/introduction)
- [Cloud Storage durability](https://docs.cloud.google.com/storage/docs/availability-durability)
- [Memorystore for Valkey GA](https://cloud.google.com/blog/products/databases/announcing-general-availability-of-memorystore-for-valkey)
- [Firestore MongoDB compatibility](https://www.infoq.com/news/2025/04/google-firestore-mongodb/)

### F26 — GCP AI/ML
- [Vertex AI Pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)
- [Vector Search 2.0](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931)
- [Document AI HITL deprecation](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new)
- [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
- [Vertex AI RAG Engine](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)
- [Gemini 2.5 Pro/Flash GA](https://cloud.google.com/blog/products/ai-machine-learning/gemini-2-5-flash-lite-flash-pro-ga-vertex-ai)

### F27 — GCP Security
- [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)
- [Cloud HSM](https://cloud.google.com/kms/docs/hsm)
- [SCC agentless scanning](https://security.googlecloudcommunity.com/news-announcements-9/google-security-command-center-scc-h2-2025-product-release-summary-6574)
- [Cloud Armor Adaptive Protection](https://cloud.google.com/security/products/armor)
- [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview)
- [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview)
- [SCC pricing](https://cloud.google.com/security-command-center/pricing)
- [Cloud Armor pricing](https://cloud.google.com/armor/pricing)

### F28 — GCP Observability
- [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing)
- [OTLP native ingestion](https://www.infoq.com/news/2025/09/gcp-opentelemetry-adoption/)
- [Managed Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)
- [Cloud Trace auto-collection on Cloud Run](https://cloud.google.com/run/docs/trace)
- [Cloud Debugger deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation)
- [Cloud Profiler](https://cloud.google.com/profiler/docs/about-profiler)

### F29 — GCP Networking
- [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
- [Private Service Connect](https://cloud.google.com/private-service-connect)
- [Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/overview)
- [Cloud DNS SLA](https://cloud.google.com/dns/sla)
- [Apigee overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview)
- [Cloud Interconnect pricing](https://cloud.google.com/network-connectivity/docs/interconnect/pricing)

### F30 — GCP CI/CD
- [Cloud Build](https://cloud.google.com/build)
- [Artifact Registry scanning](https://docs.cloud.google.com/artifact-registry/docs/analysis)
- [Cloud Deploy](https://cloud.google.com/deploy)
- [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)
- [Cloud Source Repositories deprecation](https://docs.cloud.google.com/source-repositories/docs/migration-guides)
- [WIF for deployment pipelines](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)

### F31 — GCP Messaging
- [Cloud Pub/Sub SLA](https://cloud.google.com/pubsub/sla)
- [Pub/Sub Lite deprecation](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite)
- [Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)
- [Cloud Dataflow](https://cloud.google.com/dataflow)
- [Cloud Workflows pricing](https://cloud.google.com/workflows/pricing)
- [ArXiv Kafka FTE estimate](https://arxiv.org/pdf/2510.04404)

### F31a — GCP Infrastructure Integration
- [Serverless NEG health check limitation](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)
- [Secret Manager CSI for GKE](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component)
- [OTLP metrics Preview](https://cloud.google.com/blog/products/management-tools/otlp-opentelemetry-protocol-for-google-cloud-monitoring-metrics)
- [Vertex AI Pipelines SDK v2](https://docs.cloud.google.com/vertex-ai/docs/core-release-notes)
- [Cloud Run health checks](https://docs.cloud.google.com/run/docs/configuring/healthchecks)
- [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview)
