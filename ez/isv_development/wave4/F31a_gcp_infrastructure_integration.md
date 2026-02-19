# F31a — GCP Per-Service Infrastructure Integration

**Research Assignment:** How the 8 per-service infrastructure components integrate with and apply across all GCP managed service domains, and what a production-ready service onboarding checklist looks like for each service type.

**Scope:** Cross-cutting integration patterns across GCP compute services (Cloud Run, Cloud Functions 2nd gen / Cloud Run functions, GKE Autopilot, Vertex AI endpoints). Excludes deep per-service analysis (covered by F24–F31).

---

## Executive Summary

GCP's managed compute surfaces share a common integration substrate — Artifact Registry, Cloud Build/Cloud Deploy, Secret Manager, Cloud Monitoring, and Cloud Load Balancing — but each compute type exposes this substrate through meaningfully different interfaces that require service-specific onboarding steps. Cloud Run and Cloud Functions (2nd gen, now branded "Cloud Run functions") are architecturally converging: Cloud Functions 2nd gen is now [deployed as a Cloud Run service with Eventarc event triggers](https://cloud.google.com/blog/products/serverless/cloud-functions-2nd-generation-now-generally-available), meaning their CI/CD, observability, and secrets patterns are nearly identical. GKE Autopilot differs most substantially — it is the only compute surface with full Kubernetes-native constructs (CoreDNS, liveness/readiness probes, Workload Identity Federation, CSI driver for secrets), and the only surface with auto-instrumentation via Managed Prometheus and OpenTelemetry Collector sidecars. A critical production gap exists in serverless load balancing: [health checks are not supported for serverless NEG backends](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts), requiring alternative outlier detection strategies for Cloud Run and Cloud Functions behind Application Load Balancers. Vertex AI endpoints follow a separate deployment model entirely (Vertex AI Pipelines, not Cloud Deploy), and their integration with the standard 8-component stack requires explicit bridging work. ISV teams onboarding a new GCP-hosted service should expect 3–6 hours of infrastructure wiring per service type on first deployment, dropping to under 1 hour for subsequent services of the same type via templated `clouddeploy.yaml` and Terraform modules.

---

## 1. CI/CD Pipeline Patterns per Compute Type

### 1.1 Cloud Build + Cloud Deploy Architecture

[Cloud Deploy](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run) is Google's managed continuous delivery platform. The canonical GCP CI/CD pattern uses Cloud Build for the build phase and Cloud Deploy for the delivery phase:

- **Cloud Build** triggers on Git events (push, PR merge) and produces container images pushed to Artifact Registry.
- **Cloud Deploy** manages promotion across a sequence of target environments (dev → staging → prod) defined in a `clouddeploy.yaml` delivery pipeline.

[Cloud Deploy provides a serverless continuous delivery platform to run pipelines that automate and codify how you promote versions of a containerized application through isolated pre-prod and production environments.](https://cloud.google.com/blog/products/devops-sre/using-cloud-deploy-to-promote-pre-prod-to-production-in-cloud-run)

### 1.2 Pipeline Patterns by Compute Type

| Compute Type | Build Trigger | Delivery Tool | Deployment Unit | Rollback Mechanism |
|---|---|---|---|---|
| **Cloud Run** | Cloud Build (push to branch) | Cloud Deploy | Container image + revision | Traffic split, instant rollback via `gcloud run services update-traffic` |
| **Cloud Run functions (2nd gen)** | Cloud Build (`gcloud functions deploy`) | Cloud Deploy (Preview) or direct gcloud | Container image (auto-built) or ZIP source | Revision rollback identical to Cloud Run |
| **GKE Autopilot** | Cloud Build | Cloud Deploy (Kubernetes target) | Kubernetes manifests + Helm/Kustomize | `kubectl rollout undo`, Cloud Deploy rollback |
| **Vertex AI endpoint** | Vertex AI Pipelines (`ModelUploadOp`, `EndpointCreateOp`, `ModelDeployOp`) | Vertex AI Pipelines SDK v2 (GA) | Model artifact + endpoint config | Manual redeploy to prior model version |

**Cloud Run deployment:** [A CI/CD pipeline automatically builds a container image from committed code, stores the image in Artifact Registry, and deploys to Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run). Environment promotion uses Cloud Deploy target sequences with substitution variables per environment.

**Cloud Functions 2nd gen / Cloud Run functions:** [In August 2024, Google renamed Cloud Functions (2nd gen) to Cloud Run functions and folded it under the Cloud Run umbrella.](https://cloud.google.com/blog/products/serverless/cloud-functions-2nd-generation-now-generally-available) CI/CD pipelines use `gcloud functions deploy --gen2` or equivalent Terraform. Cloud Deploy support for Cloud Run functions targets is in Preview as of 2025.

**GKE Autopilot:** [GitOps-style pipelines](https://cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build) store manifests in Git, with Cloud Build applying changes via `kubectl apply` or Cloud Deploy Kubernetes targets. Autopilot auto-provisions nodes; the pipeline delivers manifests, not node configurations.

**Vertex AI endpoints:** [Google Cloud Pipeline Components SDK v2 is now generally available](https://cloud.google.com/vertex-ai/docs/core-release-notes), providing `ModelUploadOp`, `EndpointCreateOp`, and `ModelDeployOp` pipeline components. Cloud Deploy is not directly integrated with Vertex AI endpoint deployment; MLOps teams use Vertex AI Pipelines as the delivery mechanism.

**Onboarding checklist — CI/CD:**
- [ ] Create Artifact Registry repository (Docker format, region-matched to deployment target)
- [ ] Configure Cloud Build trigger (branch or tag pattern)
- [ ] Author `cloudbuild.yaml` with build, push, and deploy steps
- [ ] Create Cloud Deploy delivery pipeline (`clouddeploy.yaml`) with target sequence
- [ ] Grant Cloud Build SA `roles/clouddeploy.releaser` on Cloud Deploy pipeline
- [ ] Configure environment substitutions (project IDs, service names, region per target)
- [ ] Validate first release promotion through dev → staging manually before enabling auto-promotion

---

## 2. Health-Check Endpoints per Compute Type

### 2.1 Cloud Run Health Checks

[Cloud Run supports HTTP, TCP, and gRPC probes for startup checks; HTTP and gRPC probes for liveness checks; TCP probe is only supported for startup checks and not liveness.](https://docs.cloud.google.com/run/docs/configuring/healthchecks)

Three probe types are supported:
- **Startup probe:** Determines whether the container has started and is ready to accept traffic. Disables liveness and readiness until startup succeeds.
- **Liveness probe:** Determines whether to restart a container. Helps recover from deadlocks and unrecoverable failures.
- **Readiness probe (Preview):** Determines when an instance should receive traffic. Failed instances stop accepting new requests but are not terminated.

Default probe configuration (TCP startup, if unconfigured): timeout 240s, period 240s, failure threshold 1.

| Probe Parameter | Startup/Liveness Range | Readiness Range | Default |
|---|---|---|---|
| Initial delay | 0–240 s | — | 0 |
| Period | 1–240 s | 1–300 s | 10 |
| Timeout | 1–240 s | 1–300 s | 1 |
| Failure threshold | varies | varies | 3 |

HTTP health check endpoints on Cloud Run are externally accessible. The endpoint path (e.g., `/health`, `/ready`, `/startup`) must match the path in the probe configuration. HTTP/1 (not HTTP/2) is required for HTTP probes.

### 2.2 GKE Health Checks

GKE uses standard [Kubernetes liveness, readiness, and startup probes](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes):
- **Liveness probe:** Kubelet restarts container on failure.
- **Readiness probe:** Kubelet removes pod from Service endpoints on failure; traffic stops flowing.
- **Startup probe:** Delays liveness/readiness evaluation for slow-starting containers.

GKE Autopilot provisions workloads on managed node pools; probe configuration lives in `Pod.spec.containers[*].livenessProbe` / `readinessProbe` / `startupProbe`. Cloud Load Balancing health checks (separate from pod probes) use NEG health checks targeting pod ports directly.

### 2.3 Cloud Functions and Serverless NEGs

Cloud Functions 2nd gen / Cloud Run functions share the Cloud Run health check model (same underlying runtime). [Health checks are not supported for serverless backends; backend services that contain serverless NEG backends cannot be configured with health checks.](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) The load balancer cannot verify if the underlying Cloud Run or Cloud Functions resource is functioning. Outlier detection on the backend service provides the closest available mitigation.

**Cloud Monitoring Uptime Checks** can supplement missing NEG health checks by monitoring an HTTP endpoint on Cloud Run or Cloud Functions services from multiple GCP PoP locations.

**Onboarding checklist — Health checks:**
- [ ] Cloud Run: Implement `/health` (liveness) and `/ready` (readiness) HTTP endpoints returning 2XX
- [ ] Cloud Run: Configure startup probe if init time exceeds 10s (prevents premature liveness failures)
- [ ] GKE: Define `livenessProbe`, `readinessProbe`, and `startupProbe` in pod spec; use `httpGet` or `grpc`
- [ ] For Cloud Run behind ALB (serverless NEG): Configure Cloud Monitoring uptime check as compensating control
- [ ] GKE: Ensure Cloud Load Balancing NEG health check port aligns with container port in pod spec

---

## 3. Service Registry and Discovery

### 3.1 GKE — CoreDNS and Kubernetes Service Discovery

GKE uses [CoreDNS for in-cluster service discovery](https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery). A Kubernetes Service named `my-service` in namespace `my-ns` is resolvable within the cluster at `my-service.my-ns.svc.cluster.local`. CoreDNS runs as a Deployment in `kube-system` and is scaled automatically on GKE Autopilot based on cluster size.

[GKE can optionally use Cloud DNS as the cluster DNS provider](https://cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns), replacing CoreDNS with a managed service, improving resilience and eliminating the need to manage CoreDNS replica count.

### 3.2 Cloud Run — Service URLs and Private Networking

[Cloud Run does not offer DNS service discovery out-of-the-box.](https://ahmet.im/blog/cloud-run-service-discovery/) Service URLs include a random hash and region code: `https://SERVICE-HASH-REGION.a.run.app`. These URLs are not predictable before first deployment.

Options for service-to-service discovery on Cloud Run:
1. **Environment variable injection:** Caller hardcodes or injects the callee's service URL at deploy time via environment variable.
2. **Cloud Service Mesh (Traffic Director):** [Cloud Run services can call other Cloud Run services using a customized URL configured through the Cloud Service Mesh service routing APIs](https://cloud.google.com/service-mesh/docs/configure-cloud-service-mesh-for-cloud-run), providing stable, non-hash names.
3. **Private Service Connect + Cloud DNS Private Zone:** [To call Cloud Run resources using an internal IP address, create a Private Service Connect endpoint and configure a private DNS zone for `run.app`](https://cloud.google.com/run/docs/securing/private-networking). On-premises hosts can reach Cloud Run through the PSC endpoint IP.

### 3.3 Cloud Service Mesh (Traffic Director) — Unified Discovery

[Cloud Service Mesh provides service and endpoint discovery by monitoring VM instances and container instances as endpoints of services, maintaining up-to-date health check information and sharing it with clients.](https://docs.cloud.google.com/service-mesh/docs/traffic-management/service-discovery) Supported client types: Envoy sidecar proxies and proxyless gRPC services (acting as xDS clients). The mesh supports GKE clusters and Cloud Run services via separate routing configuration. Note: [the guide explicitly states it only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs.](https://docs.cloud.google.com/service-mesh/docs/traffic-management/service-discovery)

### 3.4 Cloud DNS Private Zones for Managed Services

Cloud SQL, Memorystore, and other managed services expose private IP addresses routable only within the connected VPC. Cloud DNS Private Zones map human-readable hostnames (e.g., `db.internal.example.com`) to these private IPs, enabling service discovery without hardcoding IP addresses in application configuration.

**Onboarding checklist — Service discovery:**
- [ ] GKE: Confirm CoreDNS (or Cloud DNS cluster DNS) is healthy; validate intra-cluster `nslookup`
- [ ] Cloud Run: Inject callee service URLs as environment variables at deploy time (minimum viable approach)
- [ ] Cloud Run (advanced): Configure Cloud Service Mesh routing for stable internal hostnames
- [ ] Multi-service architecture: Establish Cloud DNS Private Zone naming convention before first deployment
- [ ] Document all service URLs in a service catalog (Apigee API hub or equivalent) immediately post-deploy

---

## 4. Load Balancer and Ingress Integration

### 4.1 Serverless NEGs (Cloud Run and Cloud Functions)

[Serverless NEGs can point to: Cloud Run services, App Engine (standard and flexible), Cloud Run functions (1st and 2nd gen), and API Gateway (Preview).](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)

Serverless NEGs work with **Application Load Balancers only** (global external ALB, regional external ALB, regional internal ALB, cross-region internal ALB). They are not supported by Proxy Network Load Balancers or Passthrough Network Load Balancers.

Key constraints:
- One serverless NEG per region in global backend services.
- Resources must exist in the same region and project as the NEG.
- [You cannot mix serverless NEGs with other types of NEGs in the same backend service.](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) Cloud Run and GKE cannot share a single backend service.
- Default timeout: 60 minutes (not configurable).
- No health check support for serverless backends (see Section 2.3).

**URL masks** enable routing multiple Cloud Run services at the same domain without creating separate NEGs per service.

### 4.2 GKE — NEGs and Ingress

GKE uses container-native load balancing via [zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs). Cloud Load Balancing health checks connect directly to pod IPs, bypassing kube-proxy. GKE Ingress (with the `kubernetes.io/ingress.class: gce` annotation) provisions an Application Load Balancer automatically. GKE Gateway API (generally available) provides a more expressive routing model via `Gateway` and `HTTPRoute` resources.

### 4.3 Traffic Director for Service Mesh Routing

For east-west (service-to-service) routing within GCP, Traffic Director (Cloud Service Mesh) provides mesh-level load balancing without requiring an external load balancer. Envoy sidecars receive routing rules via xDS and apply weighted load balancing, retries, circuit breaking, and fault injection per route.

### 4.4 Apigee as API Gateway

[Apigee is a leader in the 2025 Gartner API Management Magic Quadrant.](https://cloud.google.com/blog/products/ai-machine-learning/apigee-a-leader-in-2025-gartner-api-management-magic-quadrant) The [Apigee Extension Processor](https://developers.googleblog.com/en/apigee-announces-general-availability-of-apim-extension-processor/) (GA) integrates with Cloud Load Balancing to apply Apigee API management policies (rate limiting, auth, transformation) as a traffic extension, without requiring all traffic to route through Apigee's data plane directly. This enables Cloud Run and GKE backends to be exposed through Apigee without changing their internal architecture.

For ISV SaaS products: Apigee provides tenant API key management, plan-based rate limiting, and developer portal capabilities that the lower-level load balancer primitives do not.

**Onboarding checklist — Load balancer and ingress:**
- [ ] Cloud Run: Create serverless NEG in matching region; attach to Application Load Balancer backend service
- [ ] Cloud Run: Configure URL map rules and SSL certificate on the frontend
- [ ] GKE: Use GKE Ingress or Gateway API; verify NEG auto-provisioning annotation on Service object
- [ ] Confirm no serverless NEG and GKE NEG sharing same backend service (architectural constraint)
- [ ] ISV API exposure: Configure Apigee proxy or API Gateway (lightweight) in front of Cloud Run/GKE backends
- [ ] Verify Cloud Armor policies are attached to the load balancer frontend (WAF, DDoS protection)

---

## 5. Observability Instrumentation per Service Type

### 5.1 Native Metrics vs. SDK-Required Metrics

[Direct writing of metrics is not supported in Cloud Run functions. Log-based metrics can be generated.](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach)

| Compute Type | Logs | Metrics | Traces |
|---|---|---|---|
| **Cloud Run** | Automatic (stdout/stderr → Cloud Logging) | Platform metrics native; custom metrics require SDK | Cloud Trace auto-collects; OTEL sidecar for richer spans |
| **Cloud Run functions (2nd gen)** | Automatic (stdout/stderr) | Log-based metrics only (no direct write) | Cloud Trace exporter directly; no collector support |
| **GKE Autopilot** | Automatic (node log collection) | Managed Service for Prometheus recommended; custom OTEL collector | OTEL Collector DaemonSet or sidecar |
| **Compute Engine** | Ops Agent installation required | Ops Agent required | Ops Agent receives OTLP from in-process SDK exporter |
| **Vertex AI** | Managed logging | Native model serving metrics | Not natively instrumented |

### 5.2 OpenTelemetry Patterns

[The Google-Built OpenTelemetry Collector lets you send correlated OTLP traces, metrics, and logs to Google Cloud Observability from applications instrumented by OpenTelemetry SDKs.](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel)

**Cloud Run OTEL pattern:** [Use the Cloud Run multicontainer (sidecar) feature to run the Collector as a sidecar container alongside your workload container.](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke) Sidecar pattern requires instance-based billing (minimum 1 instance to keep sidecar alive).

**GKE OTEL pattern:** [Deploy OpenTelemetry Collector on GKE](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke) as a DaemonSet (one per node) or sidecar. [You can also use Managed OpenTelemetry for GKE to automatically configure and instrument workloads that use the OpenTelemetry SDK. With a single Custom Resource, you can get Golden Signals in Cloud Observability for all your OpenTelemetry-enabled applications.](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel)

**OTLP metrics (Preview):** [OTLP for metrics is currently in preview and supported when using OpenTelemetry versions 0.140.0 and higher.](https://cloud.google.com/blog/products/management-tools/otlp-opentelemetry-protocol-for-google-cloud-monitoring-metrics) Treat as non-GA for production ISV deployments.

### 5.3 Structured Logging

[To collect structured logs, use a framework configured to output serialized JSON objects to stdout or stderr.](https://docs.cloud.google.com/run/docs/monitoring-overview) Cloud Logging automatically parses JSON logs and indexes fields (severity, trace ID, request ID) for filtering. Cloud Run and Cloud Functions emit `httpRequest` structured fields automatically for HTTP-triggered invocations.

**Onboarding checklist — Observability:**
- [ ] All services: Configure logging framework to emit JSON to stdout (e.g., `structlog` for Python, `winston` for Node)
- [ ] Cloud Run: Enable Cloud Trace integration (add `X-Cloud-Trace-Context` header propagation in middleware)
- [ ] Cloud Run (advanced): Deploy OTEL sidecar container for custom spans and metrics; set minimum instances to 1
- [ ] Cloud Functions: Use `cloud-trace-exporter` library directly; no sidecar support
- [ ] GKE: Deploy Google-Built OTEL Collector via DaemonSet; configure Managed Prometheus for metrics
- [ ] All services: Create Cloud Monitoring dashboard with request rate, latency p50/p95/p99, and error rate
- [ ] Verify log correlation: confirm `trace` field in structured logs links to Cloud Trace spans

---

## 6. Container Image Lifecycle

### 6.1 Artifact Registry Integration

Artifact Registry is the central image store for all GCP container-based compute services. [Artifact Registry performs automatic scanning every time you push a new image, and vulnerability information is continuously updated when new vulnerabilities are discovered.](https://docs.cloud.google.com/artifact-registry/docs/analysis) On-demand scanning is also available but results are not updated post-scan.

**Deprecation note:** [Standard tier/container OS vulnerability scanning is deprecated and scheduled for shutdown on July 31, 2025. Advanced Vulnerability Insights is deprecated and scheduled for shutdown on June 16, 2026.](https://docs.cloud.google.com/artifact-registry/docs/analysis) ISV teams should migrate to the current Container Analysis scanning model before these dates.

### 6.2 Binary Authorization

[Binary Authorization is a service on Google Cloud that provides centralized software supply-chain security for applications that run on GKE, Cloud Run, and Google Distributed Cloud.](https://docs.cloud.google.com/binary-authorization/docs/overview) Cloud Functions is not listed as a supported platform.

Binary Authorization works through **attestors** — trusted authorities that verify images have completed required processes (e.g., CI build system, QA sign-off). A policy specifies which attestors must have signed an image before deployment. Non-compliant images are blocked and violations are logged to Cloud Audit Logs.

[Binary Authorization includes a Continuous Validation feature (Preview) that periodically checks the metadata of container images associated with running Pods for continued policy conformance.](https://docs.cloud.google.com/binary-authorization/docs/overview-cv)

### 6.3 Image Promotion Pattern

Standard multi-environment image promotion:
1. Cloud Build produces image tagged `gcr.io/PROJECT/SERVICE:$COMMIT_SHA`
2. Image pushed to `dev` Artifact Registry repository; automatic vulnerability scan triggered
3. Cloud Deploy promotes release to `staging`; image tag is promoted (not rebuilt)
4. Attestor signs image after integration tests pass
5. Cloud Deploy promotes to `prod`; Binary Authorization policy validates attestation at admission

**Onboarding checklist — Container image lifecycle:**
- [ ] Create Artifact Registry repository per region (Docker format); enable automatic scanning
- [ ] Tag images with `$COMMIT_SHA` (not `:latest`) for traceability
- [ ] Configure Cloud Build to push to Artifact Registry (not Container Registry, which is deprecated)
- [ ] Enable Binary Authorization on Cloud Run services and GKE clusters
- [ ] Create at minimum one attestor (e.g., "built-by-cloud-build") and policy requiring its signature
- [ ] Monitor Container Analysis scan results; block deployments with CRITICAL severity CVEs
- [ ] Plan migration away from deprecated scanning tiers before July 31, 2025

---

## 7. Secrets Management Integration

### 7.1 GKE — Workload Identity + CSI Driver

[The Secret Manager add-on for GKE is derived from the open-source Kubernetes Secrets Store CSI Driver.](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component) It uses the driver name `secrets-store-gke.csi.k8s.io` and mounts secrets as files in pod filesystems.

Authentication uses Workload Identity Federation:
- Standard clusters: Workload Identity Federation for GKE must be explicitly enabled.
- Autopilot clusters: Workload Identity Federation is enabled by default.
- Pods authenticate using their Kubernetes ServiceAccount, which maps to an IAM principal requiring `roles/secretmanager.secretAccessor`.

[Auto-rotation is available in GKE version 1.32.2-gke.1059000 or later, allowing secrets updated in Secret Manager to be automatically and periodically pushed to the pod without application restarts.](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component)

Limitation: The GKE add-on does not support Windows Server nodes and lacks the "Sync as Kubernetes Secret" feature available in the open-source CSI driver version.

### 7.2 Cloud Run — Environment Variables and Volume Mounts

[Cloud Run supports two approaches: volume mounts (secrets as files, supports rotation) and environment variables (resolved at instance startup, recommend pinning to specific versions rather than `latest`).](https://docs.cloud.google.com/run/docs/configuring/services/secrets)

IAM roles required for Cloud Run secrets access:
- `roles/run.admin` on the Cloud Run service
- `roles/iam.serviceAccountUser` on the service identity
- `roles/secretmanager.secretAccessor` on the service account

At runtime, environment variable secrets must be successfully retrieved before instance startup. If retrieval fails, the instance will not start. Volume-mounted secrets fail during read attempts (not at startup check).

Limitations: Regional secrets are unsupported; mounting at `/dev`, `/proc`, `/sys` is prohibited; multiple secrets cannot share the same mount path.

### 7.3 Cloud Functions — Metadata Server Pattern

Cloud Run functions running on GCP automatically obtain credentials through the [instance metadata server](https://docs.cloud.google.com/secret-manager/docs/using-other-products), eliminating the need for exported service account keys. Secret Manager client libraries call the metadata server for authentication without explicit credential configuration.

### 7.4 Cloud SQL IAM Authentication

Cloud SQL supports IAM database authentication, eliminating database passwords entirely. GKE workloads use Workload Identity to authenticate to Cloud SQL via the Cloud SQL Auth Proxy sidecar. Cloud Run uses [Cloud SQL connectors](https://docs.cloud.google.com/run/docs/configuring/services/secrets) or the proxy pattern with the service account's IAM identity.

**Onboarding checklist — Secrets management:**
- [ ] Cloud Run: Store all secrets in Secret Manager; mount as volume (preferred for rotation) or env var (simpler)
- [ ] Cloud Run: Grant service account `roles/secretmanager.secretAccessor`; verify during `gcloud run deploy`
- [ ] GKE: Enable Workload Identity Federation; create `SecretProviderClass` YAML for each secret
- [ ] GKE: Enable Secret Manager CSI add-on; verify GKE version >= 1.32.2 for auto-rotation support
- [ ] Cloud Functions: Use Secret Manager client library with metadata server auth (no key files)
- [ ] Cloud SQL: Enable IAM database authentication; replace password-based connection strings
- [ ] Prohibit service account key files in all compute environments; enforce via Org Policy

---

## 8. Service-Level Alerting Patterns

### 8.1 SLO Monitoring in Cloud Monitoring

[Cloud Monitoring's SLO monitoring automatically supports Cloud Service Mesh, Istio on GKE, App Engine, and Cloud Endpoints, and supports custom services for GKE and Cloud Run.](https://docs.cloud.google.com/monitoring/slo-monitoring) [You can create up to 500 SLOs for each service; the maximum configurable SLO target is 99.9%.](https://cloud.google.com/monitoring/slo-monitoring)

[Cloud Monitoring can detect potential GKE- and Cloud Run-based services in a project, providing a list of candidate services for SLO monitoring.](https://cloud.google.com/monitoring/slo-monitoring)

[Alerting policies trigger when a service is on track to violate an SLO, based on the rate of consumption of the error budget.](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)

### 8.2 Alerting Patterns by Service Type

| Service | Key Metric | Recommended Alert Condition | Severity |
|---|---|---|---|
| **Cloud Run** | `run.googleapis.com/request_latencies` | p99 > 2000ms for 5 min | P2 |
| **Cloud Run** | `run.googleapis.com/request_count` (5xx) | Error rate > 1% for 5 min | P1 |
| **Cloud Run** | `run.googleapis.com/container/instance_count` | Instance count = max_instances for 10 min | P2 (scaling ceiling) |
| **Cloud Functions** | `cloudfunctions.googleapis.com/function/execution_count` (error) | Error count > 10 per 5 min | P2 |
| **Cloud Functions** | `cloudfunctions.googleapis.com/function/execution_times` | p95 > function timeout × 0.8 | P2 |
| **Cloud SQL** | `cloudsql.googleapis.com/database/cpu/utilization` | CPU > 80% for 10 min | P2 |
| **Cloud SQL** | `cloudsql.googleapis.com/database/postgresql/num_backends` | Connections > 80% of `max_connections` | P1 |
| **Pub/Sub** | `pubsub.googleapis.com/subscription/num_unacked_messages_by_region` | Backlog > threshold × 3 for 15 min | P2 |
| **Pub/Sub** | `pubsub.googleapis.com/subscription/oldest_unacked_message_age_by_region` | Age > ack deadline × 2 | P1 |
| **BigQuery** | Slot utilization | Slots consumed > purchased cap for 10 min | P3 |

### 8.3 Pub/Sub Alerting Specifics

[The delivery latency health score evaluates five factors over a rolling 10-minute window: negligible seek requests, negligible negatively acknowledged messages, negligible expired acknowledgment deadlines, consistent acknowledgment latency less than 30 seconds, and consistent low utilization with adequate capacity.](https://docs.cloud.google.com/pubsub/docs/monitoring)

[An ack deadline expiration rate exceeding 1% warrants investigation.](https://docs.cloud.google.com/pubsub/docs/monitoring) For push subscriptions, [maintain fewer than 1,000 outstanding messages in most situations and achieve more than 99% acknowledgment rates for higher message limits.](https://docs.cloud.google.com/pubsub/docs/monitoring)

[Set quota alerts when usage reaches 80% of limit.](https://docs.cloud.google.com/pubsub/docs/monitoring)

**Onboarding checklist — Service-level alerting:**
- [ ] Create Cloud Monitoring service definition for each Cloud Run service and GKE workload
- [ ] Define SLI type (request-based availability or latency) and compliance period (rolling 28 days)
- [ ] Set SLO target (start at 99.5% for new services; tune upward as reliability is demonstrated)
- [ ] Create error budget burn rate alert (fast burn: 2% budget consumed in 1 hour; slow burn: 5% in 6 hours)
- [ ] Configure per-metric alerts from table above for each deployed service
- [ ] Route alerts to PagerDuty, Slack webhook, or Pub/Sub via notification channel; test escalation path
- [ ] Cloud Functions: Create log-based metrics for error patterns (no direct metric write available)
- [ ] Pub/Sub: Alert on `oldest_unacked_message_age` > 2× ack deadline as primary backlog signal

---

## 9. Cross-Cutting Gaps and ISV Considerations

| Gap | Affected Services | Mitigation |
|---|---|---|
| No health checks for serverless NEG backends | Cloud Run, Cloud Functions | Cloud Monitoring uptime checks + outlier detection |
| Binary Authorization not supported on Cloud Functions | Cloud Run functions | Accept gap or migrate critical functions to Cloud Run |
| OTLP metrics in Preview (not GA) | All services using OTEL metric export | Use Managed Prometheus (GKE) or log-based metrics (Cloud Functions) |
| Cloud Functions: no direct metric write | Cloud Run functions | Log-based metrics as compensating control |
| No native service discovery for Cloud Run | Cloud Run | Inject service URLs via env vars or use Cloud Service Mesh |
| Advanced Vulnerability Insights deprecated June 2026 | All services using Artifact Registry | Migrate to current Container Analysis scanning; audit timeline |
| Vertex AI endpoints not supported by Cloud Deploy | Vertex AI | Use Vertex AI Pipelines SDK v2 as delivery mechanism |
| Auto-rotation secrets require GKE >= 1.32.2 | GKE (older clusters) | Upgrade cluster or implement application-level secret refresh |

---

## Key Takeaways

- **Compute type determines integration complexity.** GKE Autopilot requires the most per-service wiring (Workload Identity, CoreDNS, pod probes, NEG health checks, OTEL DaemonSet) but provides the most operational control. Cloud Run and Cloud Run functions share 80% of the same integration patterns and are the lowest-overhead onboarding path for ISV microservices.
- **Serverless NEG health check absence is a production risk.** Neither Cloud Run nor Cloud Functions backends behind an Application Load Balancer support health checks. ISV teams must implement Cloud Monitoring uptime checks as a compensating control and design for graceful degradation rather than assuming the load balancer will detect unhealthy backends.
- **Secret Manager + Workload Identity is the mandatory secrets pattern.** Service account key files must be prohibited via Org Policy. GKE uses the CSI driver with Workload Identity Federation; Cloud Run uses environment variable or volume mount injection; Cloud Functions uses the metadata server. All three patterns eliminate long-lived credentials.
- **SLO monitoring is the recommended alerting foundation.** Cloud Monitoring's SLO service with error budget burn rate alerting provides earlier warning than threshold-based alerts on individual metrics. ISV teams should define SLOs before go-live, not retroactively. The 500-SLO-per-service limit is not a practical constraint at typical ISV scale.
- **Vertex AI endpoints are outside the standard 8-component stack.** They do not use Cloud Deploy, do not support Binary Authorization admission control, and have limited OTEL instrumentation. ISV teams building AI-augmented SaaS on GCP should treat Vertex AI endpoint deployment as a separate MLOps track with its own CI/CD pipeline using Vertex AI Pipelines SDK v2 (GA as of 2025).

---

## Sources

- [Cloud Build: Deploying to Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run)
- [Cloud Deploy: Promoting pre-prod to production in Cloud Run](https://cloud.google.com/blog/products/devops-sre/using-cloud-deploy-to-promote-pre-prod-to-production-in-cloud-run)
- [GitOps-style continuous delivery with Cloud Build for GKE](https://cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build)
- [Cloud Run functions (2nd gen) GA announcement](https://cloud.google.com/blog/products/serverless/cloud-functions-2nd-generation-now-generally-available)
- [Vertex AI Pipelines: Build a pipeline](https://docs.cloud.google.com/vertex-ai/docs/pipelines/build-pipeline)
- [Configure container health checks for Cloud Run services](https://docs.cloud.google.com/run/docs/configuring/healthchecks)
- [Kubernetes best practices: health checks with liveness and readiness probes](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes)
- [Serverless NEG concepts — Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)
- [GKE Service discovery and DNS](https://cloud.google.com/kubernetes-engine/docs/concepts/service-discovery)
- [Cloud Run: Private networking](https://cloud.google.com/run/docs/securing/private-networking)
- [Cloud Service Mesh: Service discovery](https://docs.cloud.google.com/service-mesh/docs/traffic-management/service-discovery)
- [Cloud DNS for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns)
- [runsd: Service discovery for Cloud Run](https://ahmet.im/blog/cloud-run-service-discovery/)
- [Apigee: 2025 Gartner API Management Magic Quadrant](https://cloud.google.com/blog/products/ai-machine-learning/apigee-a-leader-in-2025-gartner-api-management-magic-quadrant)
- [Apigee Extension Processor GA](https://developers.googleblog.com/en/apigee-announces-general-availability-of-apim-extension-processor/)
- [Choose an instrumentation approach — Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach)
- [Google-Built OpenTelemetry Collector overview](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel)
- [Deploy Google-Built OpenTelemetry Collector on GKE](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke)
- [OTLP for Google Cloud Monitoring metrics](https://cloud.google.com/blog/products/management-tools/otlp-opentelemetry-protocol-for-google-cloud-monitoring-metrics)
- [Cloud Run: Monitoring and logging overview](https://docs.cloud.google.com/run/docs/monitoring-overview)
- [Artifact Registry: Artifact analysis and vulnerability scanning](https://docs.cloud.google.com/artifact-registry/docs/analysis)
- [Container scanning overview — Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview)
- [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview)
- [Continuous validation — Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview-cv)
- [Configure secrets for Cloud Run services](https://cloud.google.com/run/docs/configuring/services/secrets)
- [Secret Manager managed CSI component for GKE](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component)
- [Secret Manager: Using with other products](https://docs.cloud.google.com/secret-manager/docs/using-other-products)
- [Access secrets outside GKE clusters using Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/workload-identity-secrets)
- [SLO monitoring concepts](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring)
- [Cloud Monitoring SLO monitoring](https://docs.cloud.google.com/monitoring/slo-monitoring)
- [Pub/Sub: Monitor subscriptions in Cloud Monitoring](https://docs.cloud.google.com/pubsub/docs/monitoring)
- [Apigee Operator for Kubernetes and GKE Inference Gateway](https://developers.googleblog.com/en/apigee-operator-for-kubernetes-and-gke-inference-gateway-integration-for-auth-and-aillm-policies/)
- [Getting started with API Gateway and Cloud Run](https://cloud.google.com/api-gateway/docs/get-started-cloud-run)
- [Serverless observability with OpenTelemetry and Grafana Cloud for Cloud Run](https://grafana.com/blog/2024/05/23/serverless-observability-how-to-monitor-google-cloud-run-with-opentelemetry-and-grafana-cloud/)
