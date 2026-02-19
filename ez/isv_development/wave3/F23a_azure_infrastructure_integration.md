# F23a: Azure Per-Service Infrastructure Integration

**Research Agent:** F23a — Azure Per-Service Infrastructure Integration
**Date:** 2026-02-18
**Scope:** Cross-cutting per-service infrastructure integration patterns across Azure compute services (Functions, Container Apps, App Service, AKS, Azure ML). References F16–F23 for per-service depth.

---

## Executive Summary

Azure's five primary compute surfaces — Azure Functions, Container Apps, App Service, AKS, and Azure ML managed endpoints — each expose a distinct operational profile for the eight cross-cutting infrastructure concerns (CI/CD, health checks, service discovery, load balancing, observability, container image lifecycle, secrets management, and alerting). Container Apps offers the highest level of integration density, combining built-in Dapr service discovery, native revision-based traffic splitting, managed OpenTelemetry agents, and Key Vault secret references into a single control plane. AKS provides the most configurability but demands the highest operational expertise, particularly for secrets management via the CSI driver and GitOps-based deployment pipelines. Azure Functions auto-instruments Application Insights by default across all five supported runtimes, while App Service provides portal-toggle autoinstrumentation for .NET, Java, Node.js, and Python on Linux. A critical architectural gap exists in Container Apps structured logging: the service does not natively support structured JSON log parsing, requiring workaround pipelines for teams relying on log-based alerting. Production onboarding for any Azure compute service requires coordinating all eight infrastructure domains before go-live; this file provides a per-service checklist to prevent common integration gaps.

---

## 1. CI/CD Pipeline Patterns Per Service Type

Each Azure compute model requires a distinct pipeline structure reflecting its deployment artifact format, revision model, and identity handshake with ACR.

### 1.1 Azure Functions

[FACT]
"The GitHub Actions workflow triggers when you commit to a specific branch in your repository. When creating the workflow, you decide which branch triggers the workflow."
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-continuous-deployment
Date: Microsoft Learn (current as of 2025)

[FACT]
The canonical Functions pipeline has two jobs: **Build** (package the function app into a zip artifact) and **Deploy** (upload to the Function App using `azure/functions-action`). Deployment slots (`--slot staging`) enable zero-downtime swap via `az functionapp deployment slot swap`.
URL: https://www.mssqltips.com/sqlservertip/8283/building-a-ci-cd-pipeline-for-azure-functions/
Date: 2025

[FACT]
The `azure/functions-action` GitHub Action is the canonical deployment mechanism. Self-hosted runners are supported and GitHub does not charge for them, making them viable for VNet-integrated deployments where public SCM endpoints are disabled.
URL: https://bytegoblin.io/blog/implementing-ci-cd-for-azure-functions-with-github-actions-python-and-windows-self-hosted-runner.mdx
Date: 2025

**Key Differentiator:** Functions deployment is zip-based or container-based; there is no Kubernetes manifest or Helm chart. Slot swaps provide rollback without re-deploying.

### 1.2 Azure Container Apps

[FACT]
"Azure Container Apps allows you to use GitHub Actions to publish revisions to your container app. As commits are pushed to your GitHub repository, a workflow is triggered which updates the container image in the container registry. Azure Container Apps creates a new revision based on the updated container image."
URL: https://learn.microsoft.com/en-us/azure/container-apps/github-actions
Date: 2025-05-14 (updated 2025-10-23)

[FACT]
The `azure/container-apps-deploy-action@v1` action supports three scenarios: (1) build from Dockerfile and deploy, (2) build from source without Dockerfile (supported languages: .NET, Java, Node.js, PHP, Python), and (3) deploy an existing container image.
URL: https://learn.microsoft.com/en-us/azure/container-apps/github-actions
Date: 2025-05-14

[FACT]
"Important: If you're building a container image in a separate step, make sure you use a unique tag such as the commit SHA instead of a stable tag like `latest`."
URL: https://learn.microsoft.com/en-us/azure/container-apps/github-actions
Date: 2025-05-14

[FACT]
Blue-green deployment in Container Apps requires setting `configuration.activeRevisionsMode` to `multiple`. "The default traffic split for each new revision is 0, which ensures that all traffic will continue to be routed to the existing old production revision."
URL: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-blue-green-aca-deployment/
Date: 2025

**Key Differentiator:** Container Apps pipelines produce container images and create immutable revisions; traffic weight assignment is a post-deploy step, not a deploy-time parameter.

### 1.3 App Service

[FACT]
App Service autoinstrumentation and GitHub Actions deployment are configured via `Deploy by Using GitHub Actions` and use the `azure/webapps-deploy` action. Deployment slots (staging → production swap) are the canonical zero-downtime pattern.
URL: https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions
Date: Microsoft Learn (current as of 2025)

**Key Differentiator:** App Service supports both code-publish and container-publish modes; the CI/CD action differs accordingly. Container mode requires an ACR image push step before the deploy step.

### 1.4 AKS

[FACT]
"Two GitOps operators that you can use with AKS are Flux and Argo CD, both of which are graduated Cloud Native Computing Foundation (CNCF) projects and are widely used."
URL: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks
Date: Microsoft Learn (current as of 2025)

[FACT]
The canonical AKS pipeline separates CI from CD: GitHub Actions builds a container image and pushes it to ACR; Flux or ArgoCD watches the Git manifest repository and reconciles changes to the cluster. "Application teams can accomplish deployment goals by packaging their service using Helm and deploying them either through a CI/CD pipeline such as GitHub Actions or a GitOps tool such as Flux or ArgoCD."
URL: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks
Date: Microsoft Learn (current as of 2025)

**Key Differentiator:** AKS is the only compute model where CD is typically decoupled from CI via a GitOps operator. Helm chart versioning in ACR OCI artifact format is the production-recommended packaging approach.

### 1.5 Azure ML Managed Online Endpoints

[FACT]
For Azure ML managed online endpoints, "the recommended approach involves using Azure CLI (v2) commands. The deployment creation can take up to 15 minutes, depending on whether the underlying environment or image is being built for the first time." The `azure/aml-deploy` GitHub Action is deprecated; teams must use CLI v2 YAML declarative endpoint specifications.
URL: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2
Date: Microsoft Learn (current as of 2025)

[FACT]
"A declarative approach facilitates GitOps: All changes to endpoints and deployments go through the YAML." Blue-green traffic split between ML deployment versions is controlled via the `traffic` map in the endpoint YAML.
URL: https://microsoftlearning.github.io/mslearn-mlops/documentation/06-deploy-model.html
Date: 2025

---

## 2. Health-Check Endpoints Per Compute Service

### 2.1 Azure Container Apps — Built-in Health Probes

[FACT]
"Azure Container Apps supports the following probes: Startup (checks if your application starts successfully, runs during the initial startup phase), Liveness (checks if your application is still running and responsive), Readiness (checks if a replica is ready to handle incoming requests)."
URL: https://learn.microsoft.com/en-us/azure/container-apps/health-probes
Date: 2025-11-06 (updated 2025-11-07)

[FACT]
Default probe values when ingress is enabled and no custom probes are defined:

| Probe Type | Protocol | Timeout | Period | Initial Delay | Failure Threshold |
|------------|----------|---------|--------|---------------|-------------------|
| Startup    | TCP      | 3 sec   | 1 sec  | 1 sec         | 240               |
| Liveness   | TCP      | —       | —      | —             | —                 |
| Readiness  | TCP      | 5 sec   | 5 sec  | 3 sec         | 48                |

URL: https://learn.microsoft.com/en-us/azure/container-apps/health-probes
Date: 2025-11-06

[FACT]
"Configure your health probe endpoints to respond with an HTTP status code greater than or equal to 200 and less than 400 to indicate success." Restrictions: exec probes are not supported; named ports are not supported; gRPC is not supported; only one probe of each type per container.
URL: https://learn.microsoft.com/en-us/azure/container-apps/health-probes
Date: 2025-11-06

[FACT]
"If you run your container app in multiple revision mode, after you deploy a revision, wait until your readiness probes indicate success before you shift traffic to that revision. In single revision mode, traffic shifts automatically once the readiness probe returns a successful state."
URL: https://learn.microsoft.com/en-us/azure/container-apps/health-probes
Date: 2025-11-06

### 2.2 Azure App Service — Health Check Feature

[FACT]
"Health check increases your application's availability by rerouting requests away from unhealthy instances and replacing instances if they remain unhealthy. It does that by pinging your web application every minute, via a path that you choose."
URL: https://learn.microsoft.com/en-us/azure/app-service/monitor-instances-health-check
Date: Microsoft Learn (current as of 2025)

[FACT]
"If an instance returns a status code between 200 and 299, it is considered healthy. If an instance fails to respond (or returns a non-2xx code) for 10 consecutive checks, it is marked as unhealthy."
URL: https://learn.microsoft.com/en-us/azure/app-service/monitor-instances-health-check
Date: Microsoft Learn (current as of 2025)

[FACT]
"Your App Service plan should be scaled to two or more instances to fully utilize Health check." The health check path must allow anonymous access. The health check request can be authenticated by inspecting the `x-ms-auth-internal-token` header and validating it against the SHA256 hash of `WEBSITE_AUTH_ENCRYPTION_KEY`.
URL: https://learn.microsoft.com/en-us/azure/app-service/monitor-instances-health-check
Date: Microsoft Learn (current as of 2025)

### 2.3 AKS — Liveness, Readiness, and Startup Probes

[FACT]
"Best practices recommend configuring readiness, liveness, and startup probes when applicable to improve resiliency for high loads and lower container restarts. Additionally, when you configure a startup probe, readiness and liveness probes don't start until the startup probe succeeds."
URL: https://learn.microsoft.com/en-us/azure/aks/best-practices-app-cluster-reliability
Date: Microsoft Learn (current as of 2025)

[FACT]
An Azure Policy (`b1a9997f-2883-4f12-bdff-2280f99b5915`) enforces that all pods have readiness and/or liveness probes configured. Supported probe types: `tcpSocket`, `httpGet`, and `exec`.
URL: https://www.azadvertizer.net/azpolicyadvertizer/b1a9997f-2883-4f12-bdff-2280f99b5915.html
Date: 2025

[FACT]
The AKS production checklist (the-aks-checklist.com) includes implementing startup probes to protect slow-starting containers as a key production readiness item.
URL: https://www.the-aks-checklist.com/
Date: 2025

### 2.4 Azure Functions

Azure Functions does not expose a user-configurable Kubernetes-style liveness or readiness probe. Application Insights captures invocation failure rates, timeouts, and cold-start durations natively. For Functions deployed as containers on AKS, standard Kubernetes probes apply. For consumption-plan Functions, health is surfaced via Azure Monitor metrics (`FunctionExecutionCount`, `FunctionExecutionUnits`).

[UNVERIFIED] There is no official Microsoft documentation confirming that consumption-plan Azure Functions expose a `/health` HTTP probe endpoint analogous to App Service Health Check. This claim is based on the absence of such documentation in the official Functions health monitoring reference; teams deploying Functions on dedicated plans with custom containers should implement a `/health` route and use App Service Health Check.

---

## 3. Service Registry and Discovery

### 3.1 Container Apps — Dapr Service-to-Service Invocation

[FACT]
"Dapr is built-in to Container Apps, enabling you to use the Dapr API building blocks without any manual deployment of the Dapr runtime." Service-to-service invocation (GA) allows services to "discover services and perform reliable, direct service-to-service calls with automatic mTLS authentication and encryption."
URL: https://learn.microsoft.com/en-us/azure/container-apps/dapr-overview
Date: 2026-01-30

[FACT]
"The Dapr APIs can be invoked from your container app via HTTP or gRPC. The Dapr sidecar runs on HTTP port 3500 and gRPC port 50001." Each Dapr-enabled container app is assigned an `appId`; services invoke each other using that `appId` as a logical address — no IP address or DNS lookup required.
URL: https://learn.microsoft.com/en-us/azure/container-apps/dapr-overview
Date: 2026-01-30

[FACT]
Dapr Health API is GA: "Health check probes that monitor readiness or liveness of Dapr and initialization readiness of SDKs. The health API is only available for HTTP. Dapr sidecar health checks are automatically configured when Dapr is enabled on your container app."
URL: https://learn.microsoft.com/en-us/azure/container-apps/dapr-overview
Date: 2026-01-30

### 3.2 AKS — CoreDNS and Kubernetes Service Discovery

[FACT]
"CoreDNS is the default DNS service in Azure Kubernetes Service (AKS), providing internal name resolution and service discovery for workloads running in the cluster." AKS uses CoreDNS for all clusters running Kubernetes 1.12.x and higher. CoreDNS runs as pods in the `kube-system` namespace.
URL: https://learn.microsoft.com/en-us/azure/aks/dns-concepts
Date: Microsoft Learn (current as of 2025)

[FACT]
"LocalDNS is an advanced feature in Azure Kubernetes Service (AKS) that deploys a Domain Name System (DNS) proxy on each node to provide highly resilient, low-latency DNS resolution. By handling DNS queries locally, this proxy reduces traffic to the CoreDNS addon pods." LocalDNS delivers "10x faster queries and improved reliability."
URL: https://blog.aks.azure.com/2025/08/04/accelerate-dns-performance-with-localdns
Date: 2025-08-04

[FACT]
"AKS is a managed service, so you can't modify the main configuration for CoreDNS (a CoreFile). Instead, you use a Kubernetes ConfigMap to override the default settings."
URL: https://learn.microsoft.com/en-us/azure/aks/coredns-custom
Date: Microsoft Learn (current as of 2025)

### 3.3 Azure DNS Private Zones for PaaS Services

[FACT]
"Private Link supports access to a list of Azure services over private endpoints, but it requires that you register those private endpoint records in a corresponding private DNS zone." The client queries for the private endpoint IP address to the Azure-provided DNS service `168.63.129.16`.
URL: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns
Date: Microsoft Learn (current as of 2025)

[FACT]
Best practice: "Create a DNS zone for each Private Endpoint of like services and don't place records for multiple services in the same DNS zone." Azure Policies can be deployed to automate DNS record creation when application teams deploy resources with private endpoints.
URL: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/private-link-and-dns-integration-at-scale
Date: Microsoft Learn (current as of 2025)

### 3.4 APIM as Service Facade

[FACT]
"API Management creates a facade in front of the microservices, enabling centralized management and governance of APIs deployed across distributed infrastructure." For AKS backends, "you need to think about how to map your Services in Kubernetes to APIs in API Management."
URL: https://learn.microsoft.com/en-us/azure/api-management/api-management-kubernetes
Date: Microsoft Learn (current as of 2025)

[FACT]
Azure API Center provides "a single, centralized registry for all APIs and integration with APIM to synchronize visibility, documentation, and onboarding." As of mid-2025, Azure is investing in deeper APIM + API Center integration for API lifecycle and discovery automation.
URL: https://dellenny.com/service-discovery-in-azure-dynamically-finding-service-instances/
Date: 2025

---

## 4. Load Balancer and Ingress Integration

### 4.1 AKS Ingress Options (2025)

[FACT]
"Today's options include: NGINX Ingress Controller (now available as an AKS-managed add-on), Azure Application Gateway Ingress Controller (AGIC, an AKS add-on integrating Azure's native L7 load balancer with WAF), and Kubernetes Gateway API with Application Gateway for Containers (a new approach offering advanced routing)."
URL: https://jreypo.io/2025/09/10/exposing-aks-workloads-on-azure-2025-edition/
Date: 2025-09-10

[FACT]
"Application Gateway for Containers offers an elastic and scalable ingress to AKS clusters and is an application layer (layer 7) load balancing and dynamic traffic management product for workloads running in a Kubernetes cluster."
URL: https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview
Date: Microsoft Learn (current as of 2025)

[FACT]
"AGIC is a Kubernetes application that makes it possible for AKS customers to leverage Azure's native Application Gateway L7 load-balancer, and monitors the Kubernetes cluster continuously to expose selected services to the Internet."
URL: https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-overview
Date: Microsoft Learn (current as of 2025)

### 4.2 Container Apps — Built-in Ingress and Traffic Splitting

[FACT]
Traffic splitting in Container Apps requires `configuration.activeRevisionsMode: multiple`. Traffic is directed to specific revisions by assigning traffic weights. "You can split user traffic evenly (50/50) between old and new revisions for A/B testing, or start with only a small percentage of users on the new version for canary deployments."
URL: https://learn.microsoft.com/en-us/azure/container-apps/revisions
Date: Microsoft Learn (current as of 2025)

### 4.3 Global vs. Regional Routing Architecture

[FACT]
"Front Door is a non-regional service that can load balance between different scale units/clusters across regions, whereas Application Gateway is a regional service for load balancing between VMs/containers within a scale unit."
URL: https://k21academy.com/azure-cloud/azure-front-door-vs-application-gateway-vs-load-balancer/
Date: 2025

[FACT]
Combined architecture pattern: "Front Door can sit at the global level routing users to the nearest region, while Application Gateway within each region provides fine-grained load balancing and additional security."
URL: https://k21academy.com/azure-cloud/azure-front-door-vs-application-gateway-vs-load-balancer/
Date: 2025

---

## 5. Observability Instrumentation Per Service

### 5.1 Auto-Instrumentation Coverage Matrix

[FACT]
Official Microsoft autoinstrumentation support matrix (as of 2025-07-30):

| Environment | .NET Framework | .NET Core/.NET | Java | Node.js | Python |
|---|---|---|---|---|---|
| App Service on Windows (Code) | Yes (default) | Yes (default) | Yes (default) | Yes (default) | No |
| App Service on Linux (Code) | No | Yes (default) | Yes (default) | Yes (default) | Yes |
| App Service (Container) — Linux | No | Yes | Yes | Yes | No |
| Azure Functions — basic | Yes (default) | Yes (default) | Yes (default) | Yes (default) | Yes (default) |
| Azure Functions — dependencies | No | No | Yes | No | No |
| AKS | No | No | Yes (preview) | Yes (preview) | No |

"If your hosting environment or resource provider is not listed in the following table, then autoinstrumentation is not supported. In this case, we recommend manually instrumenting using the Azure Monitor OpenTelemetry Distro."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/codeless-overview
Date: 2025-07-30

[FACT]
Limitation: "Autoinstrumentation only supports single-container applications; for multi-container applications, manual instrumentation is required using the Azure Monitor OpenTelemetry Distro."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/codeless-overview
Date: 2025-07-30

[FACT]
Critical deadline: "On March 31, 2025, support for instrumentation key ingestion will end, though ingestion will continue to work but without updates or support." Teams must migrate to connection string-based Application Insights configuration.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
Date: 2025

### 5.2 Container Apps — OpenTelemetry Agent

[FACT]
"The Azure Container Apps OpenTelemetry agent automatically collects and exports data to any OTLP-supported endpoint and is enabled via environment variable without requiring manual configuration." Destination options include Azure Monitor Application Insights, Datadog, and any OTLP-compatible endpoint.
URL: https://learn.microsoft.com/en-us/azure/container-apps/opentelemetry-agents
Date: Microsoft Learn (current as of 2025)

[FACT]
Structured logging gap: "Azure Container Apps doesn't support structured application logs. If your application logs follow a JSON schema, the full JSON string appears in the `Log_s` column of `ContainerAppConsoleLogs_CL`."
URL: https://learn.microsoft.com/en-us/azure/spring-apps/migration/migrate-to-azure-container-apps-monitoring
Date: Microsoft Learn (current as of 2025)

[FACT]
"Enabling the managed OpenTelemetry agent doesn't automatically mean the agent collects data — agents only send data based on your configuration settings and instrumenting your code correctly."
URL: https://learn.microsoft.com/en-us/azure/container-apps/opentelemetry-agents
Date: Microsoft Learn (current as of 2025)

### 5.3 AKS Observability

[FACT]
AKS autoinstrumentation via Application Insights is in **public preview** for Java and Node.js only; .NET, Python, and Go require manual SDK instrumentation via the Azure Monitor OpenTelemetry Distro.
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/codeless-overview
Date: 2025-07-30

---

## 6. Container Image Lifecycle — ACR Integration Patterns

### 6.1 ACR Tasks for Automated Builds

[FACT]
"ACR Tasks streamline building, testing, pushing, and deploying images, with capabilities to automatically rebuild application images when base images are updated or automate image builds when code is committed to a Git repository."
URL: https://azure.microsoft.com/en-us/products/container-registry
Date: Microsoft Azure product page (current as of 2025)

[FACT]
"Azure Container Registry continuously scans images and discovers known vulnerabilities in packages or other dependencies defined in the container image file. Vulnerability assessments include recommendations with specific remediation guidance."
URL: https://learn.microsoft.com/en-us/troubleshoot/azure/azure-container-registry/image-vulnerability-assessment
Date: Microsoft Learn (current as of 2025)

### 6.2 Content Trust — Docker Trust Deprecated, Notary Project Replaces It

[FACT]
"Starting September 30, 2025, customers will no longer be able to enable Docker Content Trust on Azure Container Registry. Deprecation of Docker Content Trust started on March 31, 2025, and will be completely removed from Azure Container Registry on March 31, 2028."
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-content-trust-deprecation
Date: Microsoft Learn (current as of 2025)

[FACT]
"As an alternative to Docker Content Trust, Microsoft offers signing and verification solutions based on Notary Project. Notary Project signatures adhere to OCI standards and can be stored in OCI-compliant registries like Container Registry, facilitating signature portability and interoperability across cloud environments."
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-content-trust-deprecation
Date: Microsoft Learn (current as of 2025)

### 6.3 ACR Integration Per Compute Service

[FACT]
Container Apps ACR authentication: "To pull images, Azure Container Apps uses either managed identity (recommended) or admin credentials to authenticate with the Azure Container Registry."
URL: https://learn.microsoft.com/en-us/azure/container-apps/github-actions
Date: 2025-05-14

[FACT]
AKS ACR authentication: AKS supports ACR image pull via managed identity by assigning the `AcrPull` role. The `az aks update --attach-acr` command automates role assignment. This is the recommended over static credentials.
URL: https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver
Date: 2025-06-10

---

## 7. Secrets Management Integration Per Service

### 7.1 Azure Functions and App Service — Key Vault References

[FACT]
"Azure App Service and Azure Functions can use Azure Key Vault references to make Key Vault secrets available to your application code." Key Vault references use the format `@Microsoft.KeyVault(SecretUri={SECRET IDENTIFIER URL FROM KEY VAULT})` in application settings.
URL: https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references
Date: Microsoft Learn (current as of 2025)

[FACT]
"Key Vault references use the app's system-assigned identity by default, but you can specify a user-assigned identity." Required role: `Key Vault Secrets User` on the managed identity.
URL: https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references
Date: Microsoft Learn (current as of 2025)

[FACT]
Refresh behavior: "When your application's code reads an environment variable, the variable holds a value from the Key Vault that can be as much as 24 hours old (or from whenever the App Service was last restarted, whichever is sooner)."
URL: https://blog.joaograssi.com/using-azure-key-vault-references-with-azure-functions-appservice/
Date: 2025

### 7.2 Azure Container Apps — Key Vault Secret References

[FACT]
Container Apps Key Vault reference syntax in CLI: `--secrets "queue-connection-string=keyvaultref:<KEY_VAULT_SECRET_URI>,identityref:<USER_ASSIGNED_IDENTITY_ID>"`. Secrets are scoped to the application level, not individual revisions.
URL: https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets
Date: 2025-02-28 (updated 2025-10-29)

[FACT]
Auto-rotation: "If a version isn't specified in the URI, then the app uses the latest version that exists in the key vault. When newer versions become available, the app automatically retrieves the latest version within 30 minutes. Any active revisions that reference the secret in an environment variable is automatically restarted to pick up the new value."
URL: https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets
Date: 2025-02-28 (updated 2025-10-29)

[FACT]
Secrets can be exposed to containers as environment variables (`secretRef: <secret-name>`) or mounted as files in a volume (`storageType: Secret`). Volume-mounted secrets appear as individual files named after the secret.
URL: https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets
Date: 2025-02-28

[FACT]
"Secrets are scoped to an application, outside of any specific revision of an application. New revisions don't get generated through adding, removing, or changing secrets."
URL: https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets
Date: 2025-02-28

### 7.3 AKS — Secrets Store CSI Driver

[FACT]
"The Azure Key Vault provider for Secrets Store CSI Driver allows for the integration of an Azure Key Vault as a secret store with an Azure Kubernetes Service (AKS) cluster via a CSI volume." Features: mounts secrets/keys/certificates as CSI volumes; syncs with Kubernetes secrets; supports autorotation.
URL: https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver
Date: 2025-06-10 (updated 2025-10-10)

[FACT]
"After enabling this feature, AKS creates a managed identity named `azurekeyvaultsecretsprovider-xxx` in the node resource group and assigns it to the Virtual Machine Scale Sets (VMSS) automatically." The add-on enables the `azure-keyvault-secrets-provider` addon.
URL: https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver
Date: 2025-06-10

[FACT]
Required RBAC roles for CSI Driver: `Key Vault Certificate User` to access keys or certificates; `Key Vault Secrets User` to access secrets. Microsoft Entra Workload ID is the recommended identity method for production; requires `--enable-oidc-issuer` and `--enable-workload-identity` flags at cluster creation.
URL: https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver
Date: 2025-06-10

[FACT]
Limitation: "A container using a ConfigMap or Secret as a subPath volume mount does not receive automated updates when the secret is rotated. This is a Kubernetes limitation. To have the changes take effect, the application needs to reload the changed file."
URL: https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver
Date: 2025-06-10

### 7.4 Event Hubs and Service Bus — RBAC vs. Connection String

[FACT]
"Many Azure services support passwordless connections through Microsoft Entra ID and Role Based Access Control (RBAC), and these techniques provide robust security features and can be implemented using DefaultAzureCredential from the Azure Identity client libraries." Azure provides built-in roles: `Azure Event Hubs Data Owner` (complete access) and `Azure Event Hubs Data Sender` (send only).
URL: https://learn.microsoft.com/en-us/azure/event-hubs/authenticate-managed-identity
Date: Microsoft Learn (current as of 2025)

[FACT]
Passwordless connection string pattern for Service Bus with managed identity: `Endpoint=sb://{namespace}.servicebus.windows.net/;Authentication=Managed Identity`. For user-assigned managed identities, `AzureServicesAuthConnectionString` must be set to `RunAs=App;AppId={ClientId}`.
URL: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-migrate-azure-credentials
Date: Microsoft Learn (current as of 2025)

---

## 8. Service-Level Alerting Patterns Per Service Type

### 8.1 Azure Functions

[FACT]
"Application Insights provides insights into function execution time, invocation count, failure rates, and detailed telemetry data such as logs, traces, and exceptions." Alert rules can trigger webhooks, automation runbooks, Functions, Logic Apps, etc.
URL: https://turbo360.com/blog/azure-function-alert-on-failure
Date: 2025

Key alert metrics for Functions:
- `FunctionExecutionCount` — total invocations
- `FunctionExecutionUnits` — resource consumption (consumption plan billing signal)
- Application Insights: `requests/failed`, `exceptions/count`, `performanceCounters/processCpuPercentage`

### 8.2 Azure Cosmos DB

[FACT]
"Alerts can be triggered when the normalized RU/s consumption is greater than a certain percentage. The normalized RU consumption metric gives the maximum throughput utilization within a replica set."
URL: https://learn.microsoft.com/en-us/azure/cosmos-db/create-alerts
Date: Microsoft Learn (current as of 2025)

Recommended Cosmos DB alert thresholds:
- `NormalizedRUConsumption` > 80% — throughput pressure
- `TotalRequestUnits` — absolute RU consumption
- `ServerSideLatency` > SLO target — latency degradation

### 8.3 Azure SQL Database

[FACT]
"Alert rules periodically evaluate aggregated metric values over a lookback period, comparing them to a threshold value. You can configure the threshold value, evaluation frequency, and lookback period."
URL: https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-metrics-alerts?view=azuresql
Date: Microsoft Learn (current as of 2025)

Key SQL alert metrics:
- `dtu_consumption_percent` / `cpu_percent` (vCore) — compute saturation
- `storage_percent` — disk capacity
- `deadlock` — application-layer conflict signal
- `connection_failed` — connectivity errors

### 8.4 Container Apps

[FACT]
"An alert rule monitors your data and captures a signal that indicates something is happening on the specified resource. The alert rule captures the signal and checks to see if the signal meets the criteria of the condition."
URL: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview
Date: Microsoft Learn (current as of 2025)

Key Container Apps alert metrics:
- `Replicas` — replica count (alert on sudden drop)
- `RequestCount` — ingress request rate
- `Requests` with `StatusCodeClass=5xx` — error rate for SLO alerting
- Revision-scoped metrics via `RevisionName` dimension filter

### 8.5 Service Bus Queue Depth

Key Service Bus alert metrics (standard Azure Monitor signals):
- `ActiveMessages` — queue backlog (KEDA autoscaler trigger and alerting source)
- `DeadLetteredMessages` — poison message accumulation
- `IncomingMessages` / `OutgoingMessages` — throughput health

[UNVERIFIED] A specific Microsoft source for recommended `ActiveMessages` alert thresholds by tier (Standard vs. Premium) was not located in 2025 sources. The above metric names are drawn from the Azure Monitor metrics reference for Service Bus; the specific thresholds are implementation-dependent and not standardized by Microsoft documentation.

---

## 9. Production Onboarding Checklist Per Service Type

The following checklist synthesizes the eight infrastructure domains into a per-service go-live gate. All items must be completed before a service is considered production-ready.

### 9.1 Azure Functions — Production Checklist

| Domain | Checklist Item | Status Gate |
|--------|---------------|-------------|
| CI/CD | Deployment slot configured (staging → production swap) | Required |
| CI/CD | GitHub Actions workflow uses commit SHA image tag | Required |
| Health | Application Insights connection string set (not instrumentation key) | Required |
| Health | App Service Health Check path enabled (`/health`) — dedicated plan only | Required |
| Service Discovery | Function URL registered in APIM or consuming service config | Required |
| Load Balancer | App Gateway or Front Door backend pool target if externally exposed | Conditional |
| Observability | Application Insights resource linked; sampling rate configured | Required |
| Observability | Log Analytics workspace linked for diagnostic logs | Required |
| Secrets | All secrets use Key Vault references (`@Microsoft.KeyVault(...)` syntax) | Required |
| Secrets | Managed identity has `Key Vault Secrets User` RBAC role | Required |
| Alerting | Alert rule on `requests/failed` > threshold → Action Group | Required |
| Alerting | Alert rule on function execution duration > SLO → Action Group | Required |
| Image | Container-mode only: ACR vulnerability scan gate in pipeline | Conditional |
| Image | Container-mode only: Notary Project signing (Docker Content Trust deprecated March 2025) | Required if container |

### 9.2 Azure Container Apps — Production Checklist

| Domain | Checklist Item | Status Gate |
|--------|---------------|-------------|
| CI/CD | `azure/container-apps-deploy-action@v1` used in pipeline | Required |
| CI/CD | Active revision mode set to `multiple` for traffic splitting | Required for blue/green |
| CI/CD | Image tagged with commit SHA (not `latest`) | Required |
| Health | Startup probe configured for slow-starting containers | Required |
| Health | Readiness probe configured; traffic shift blocked until probe passes | Required |
| Service Discovery | Dapr `appId` assigned if using service-to-service invocation | Conditional |
| Service Discovery | Private DNS Zone linked if using private endpoints for PaaS backends | Required if VNet |
| Load Balancer | Ingress enabled; external/internal mode set per requirement | Required |
| Load Balancer | Traffic weights configured per revision for canary/blue-green | Required for multi-revision |
| Observability | OpenTelemetry agent environment variable configured | Required |
| Observability | Application Insights connection string set | Required |
| Observability | Structured logging limitation acknowledged; JSON parsing workaround in place | Required |
| Secrets | Key Vault reference URI used (not raw value in production) | Required |
| Secrets | Managed identity granted `Key Vault Secrets User` role | Required |
| Secrets | Secret version pinned or auto-rotation behavior documented | Required |
| Alerting | Alert on replica count drop → Action Group | Required |
| Alerting | Alert on `5xx` error rate → Action Group | Required |
| Image | ACR managed identity pull configured (`AcrPull` role) | Required |
| Image | ACR vulnerability scan gate in pipeline | Required |
| Image | Notary Project signing enabled (Docker Content Trust not available from Sept 2025) | Required |

### 9.3 AKS — Production Checklist

| Domain | Checklist Item | Status Gate |
|--------|---------------|-------------|
| CI/CD | GitOps operator (Flux or ArgoCD) deployed and syncing from Git repository | Required |
| CI/CD | Helm chart versioned and stored in ACR OCI artifact format | Required |
| CI/CD | GitHub Actions CI job pushes image to ACR with commit SHA tag | Required |
| Health | Startup, liveness, and readiness probes defined on all pods | Required |
| Health | Azure Policy `b1a9997f-2883-4f12-bdff-2280f99b5915` enforced for probe compliance | Required |
| Service Discovery | CoreDNS ConfigMap customized if split-horizon DNS required | Conditional |
| Service Discovery | LocalDNS feature evaluated for high-throughput DNS resolution | Recommended |
| Load Balancer | Ingress controller selected (NGINX add-on, AGIC, or App Gateway for Containers) | Required |
| Load Balancer | WAF policy attached to App Gateway if public-facing | Required if public |
| Observability | Azure Monitor Container Insights enabled | Required |
| Observability | Application Insights SDK added to application code (autoinstrumentation preview only for Java/Node.js) | Required |
| Observability | Log Analytics workspace receiving cluster diagnostic logs | Required |
| Secrets | CSI Driver add-on enabled (`--enable-addons azure-keyvault-secrets-provider`) | Required |
| Secrets | Workload Identity enabled (`--enable-oidc-issuer --enable-workload-identity`) | Required |
| Secrets | `SecretProviderClass` CRD deployed per secret bundle | Required |
| Alerting | Alert on node CPU/memory saturation → Action Group | Required |
| Alerting | Alert on pod restart count > threshold → Action Group | Required |
| Image | ACR `AcrPull` role assigned to kubelet managed identity | Required |
| Image | ACR vulnerability scan gate in pipeline | Required |
| Image | Notary Project signing in pipeline (Docker Content Trust deprecated) | Required |

### 9.4 Azure ML Managed Online Endpoints — Production Checklist

| Domain | Checklist Item | Status Gate |
|--------|---------------|-------------|
| CI/CD | Azure CLI v2 YAML endpoint spec in Git (aml-deploy action deprecated) | Required |
| CI/CD | Deployment pipeline allows up to 15 minutes for first-time environment build | Required |
| CI/CD | Traffic split `traffic` map in endpoint YAML controls blue-green promotion | Required |
| Health | Liveness and readiness probe stability tested under AI Foundry inference config | Required |
| Secrets | Managed identity assigned to endpoint for Key Vault secret access | Required |
| Observability | Application Insights linked to ML workspace | Required |
| Alerting | Alert on endpoint latency P95 > SLO → Action Group | Required |
| Alerting | Alert on `RequestsFailed` metric → Action Group | Required |

---

## 10. Comparative Difficulty Rating

| Capability Domain | On-Premises | Managed K8s (AKS) | Cloud-Native (Container Apps / Functions) |
|---|---|---|---|
| CI/CD Pipeline | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Custom build servers, artifact management, SSH deployment | GitOps operator, Helm chart versioning, ACR OCI artifacts | Pre-built GitHub Actions; revision model handles rollback |
| | Jenkins/GitLab self-hosted | GitHub Actions + ArgoCD/Flux | `azure/container-apps-deploy-action`, `azure/functions-action` |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| Health Checks | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Custom load balancer health probes; no managed replacement | Kubernetes startup/liveness/readiness; policy enforcement | Built-in defaults; App Service health check portal toggle |
| | HAProxy/NGINX config | kubectl + Azure Policy | Portal or ARM template |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |
| Service Discovery | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 (Container Apps w/ Dapr) |
| | Consul, custom DNS, service mesh | CoreDNS + Kubernetes Service objects | Dapr `appId`-based invocation; no DNS config required |
| | Consul/etcd/DNS servers | CoreDNS ConfigMap | Dapr sidecar (managed) |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |
| Secrets Management | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | HashiCorp Vault self-hosted or KMS; no managed rotation | CSI Driver + Workload Identity; rotation with subPath limitation | Key Vault reference URIs; 30-minute auto-rotation |
| | Vault, KMS, custom rotation scripts | CSI Driver, SecretProviderClass CRD | Key Vault references in ARM/CLI |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |
| Observability | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Full stack: metrics, logs, traces require separate tooling and storage | Container Insights + SDK instrumentation; limited autoinstrumentation | App Service / Functions: autoinstrumentation by default; Container Apps: OTel agent |
| | Prometheus, Grafana, ELK, Jaeger | Azure Monitor Container Insights + Application Insights SDK | Application Insights auto + Log Analytics |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 |

*FTE estimates assume a mid-size ISV deployment serving 50 enterprise customers with production + staging environments. On-call burden adds 0.1–0.2 FTE across all models for incident response.*

---

## Key Takeaways

- **Secrets management is the highest-risk integration domain across all compute models.** Functions and App Service teams must migrate from instrumentation keys to connection strings (deadline: March 31, 2025) and must use Key Vault references — not raw secret values — in App Settings. AKS teams must enable Workload Identity and the CSI Driver add-on before go-live; the `subPath` autorotation limitation requires explicit application-level handling.

- **Docker Content Trust is deprecated.** Starting September 30, 2025, new ACR instances cannot enable Docker Content Trust. All image signing pipelines must migrate to Notary Project (OCI-standard signatures) before this date. This applies to all compute models that pull from ACR: Functions (container mode), Container Apps, App Service (container), and AKS.

- **Container Apps offers the highest integration density for microservices.** The combination of built-in Dapr service discovery, native revision-based traffic splitting, managed OpenTelemetry agent, and Key Vault secret reference auto-rotation reduces operational complexity to Difficulty 1–2/5 across most domains — significantly below AKS (3/5) and on-premises (4–5/5).

- **Structured logging is a Container Apps gap requiring explicit workaround.** JSON application logs are stored as raw strings in `ContainerAppConsoleLogs_CL.Log_s`, preventing log-based parsing and alerting without preprocessing. Teams relying on structured logs for SLO alerting must route logs through an external OpenTelemetry collector or Application Insights SDK.

- **AKS production onboarding requires the most pre-deployment coordination.** Eight checklist domains, each with 2–4 items, must be completed before go-live — including GitOps operator deployment, CSI Driver configuration, CoreDNS customization, Workload Identity enablement, and ingress controller selection. The AKS production checklist in Section 9.3 provides the minimum viable gate for enterprise deployments.

---

## Related — Out of Scope

- **GCP and AWS equivalents** of the per-service infrastructure integration patterns described here (e.g., GKE Workload Identity, EKS Pod Identity, Cloud Run health probes) — covered by separate agent assignments.
- **Individual Azure service deep-dives** for Functions (F16), Data Services (F17), Container Apps (F18), Security (F19), Observability (F20), Networking (F21), CI/CD Services (F22), and Messaging Services (F23) — see those files for service-specific depth.
- **Cost modeling** for the operational staffing FTE estimates provided in Section 10 — see F03: Cost Economics for detailed financial analysis.
- **Multi-region failover patterns** using Front Door + Traffic Manager for the load balancer tier — out of scope for per-service integration; covered in networking research.

---

## Sources

- [Health probes in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/health-probes)
- [Publish revisions with GitHub Actions in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/github-actions)
- [Manage secrets in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets)
- [Microservice APIs Powered by Dapr — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/dapr-overview)
- [Collect and read OpenTelemetry data in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/opentelemetry-agents)
- [Autoinstrumentation for Azure Monitor Application Insights — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/app/codeless-overview)
- [Monitor the Health of App Service Instances — Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/monitor-instances-health-check)
- [Use Key Vault References as App Settings — Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references)
- [Use the Azure Key Vault provider for Secrets Store CSI Driver for AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)
- [Access Azure Key Vault with the CSI Driver Identity Provider — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-identity-access)
- [DNS in Azure Kubernetes Service — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/dns-concepts)
- [Customize CoreDNS for AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/coredns-custom)
- [Accelerate DNS Performance with LocalDNS — AKS Engineering Blog](https://blog.aks.azure.com/2025/08/04/accelerate-dns-performance-with-localdns)
- [Azure Private Endpoint private DNS zone values — Microsoft Learn](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)
- [Private Link and DNS Integration at Scale — Microsoft Learn (CAF)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/private-link-and-dns-integration-at-scale)
- [Use API Management with Microservices Deployed in AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/api-management-kubernetes)
- [Deployment and cluster reliability best practices for AKS — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/best-practices-app-cluster-reliability)
- [GitOps for Azure Kubernetes Service — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/gitops-aks/gitops-blueprint-aks)
- [Continuous Deployment for Azure Functions — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-continuous-deployment)
- [Deploy by Using GitHub Actions — Azure App Service Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions)
- [Transition from Docker Content Trust to Notary Project — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-content-trust-deprecation)
- [Find Azure Container Registry image vulnerability scanning results — Microsoft Learn](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-container-registry/image-vulnerability-assessment)
- [Application Gateway for Containers Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview)
- [What is Azure Application Gateway Ingress Controller — Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/ingress-controller-overview)
- [Authenticate using managed identity — Azure Event Hubs Microsoft Learn](https://learn.microsoft.com/en-us/azure/event-hubs/authenticate-managed-identity)
- [Migrate to passwordless connections with Azure Service Bus — Microsoft Learn](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-migrate-azure-credentials)
- [Create Alerts for Using Azure Monitor — Azure Cosmos DB Microsoft Learn](https://learn.microsoft.com/en-us/azure/cosmos-db/create-alerts)
- [Monitoring Azure SQL Database with metrics and alerts — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-metrics-alerts?view=azuresql)
- [Overview of Azure Monitor alerts — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
- [Azure Function Alert on Failure — Turbo360](https://turbo360.com/blog/azure-function-alert-on-failure)
- [Exposing AKS Workloads on Azure — 2025 Edition (Juanma's Blog)](https://jreypo.io/2025/09/10/exposing-aks-workloads-on-azure-2025-edition/)
- [Azure Load Balancer: Front Door vs. Application Gateway — K21 Academy](https://k21academy.com/azure-cloud/azure-front-door-vs-application-gateway-vs-load-balancer/)
- [AKS Checklist — Production Readiness](https://www.the-aks-checklist.com/)
- [Azure Policy — Ensure cluster containers have readiness or liveness probes](https://www.azadvertizer.net/azpolicyadvertizer/b1a9997f-2883-4f12-bdff-2280f99b5915.html)
- [Deploy Machine Learning Models to Online Endpoints — Microsoft Learn](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-online-endpoints?view=azureml-api-2)
- [Blue-green deployment in Azure Container Apps using Azure Developer CLI — Azure SDK Blog](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-blue-green-aca-deployment/)
- [Update and deploy changes in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/revisions)
- [Service discovery resiliency (preview) — Azure Container Apps Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/service-discovery-resiliency)
- [Log and Metrics in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/spring-apps/migration/migrate-to-azure-container-apps-monitoring)
- [Using Azure Key Vault references with Azure Functions or App Service — Joao Grassi's blog](https://blog.joaograssi.com/using-azure-key-vault-references-with-azure-functions-appservice/)
- [How to Configure Health Check Endpoints for Azure App Service — OneUptime](https://oneuptime.com/blog/post/2026-02-16-how-to-configure-health-check-endpoints-for-azure-app-service/view)
- [CI/CD for Python Azure Functions using GitHub Actions in 2025 — Medium](https://medium.com/@ifilimon26/ci-cd-for-python-azure-functions-using-github-actions-in-2025-610450955fa2)
