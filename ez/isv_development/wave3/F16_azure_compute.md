# F16: Azure Compute Services

**Research Question:** What managed compute services does Azure provide for running application workloads and AI inference, and what operational burden does each eliminate?

---

## Executive Summary

Azure offers a layered compute portfolio that spans from fully serverless functions (Azure Functions, Azure Container Apps) through PaaS web hosting (Azure App Service) and managed Kubernetes (AKS), to bare-metal-equivalent GPU clusters (ND H100 v5 series) and managed batch computing (Azure Batch). Each service tier transfers a distinct slice of operational responsibility to Microsoft — OS patching, cluster control-plane management, autoscaling logic, and scheduler orchestration — while leaving the ISV in control of application code and container images. For AI inference workloads specifically, Azure has converged its serverless container and GPU capabilities: Azure Container Apps now supports serverless NVIDIA A100 and T4 GPUs with per-second billing and scale-to-zero, while Azure Container Instances GPU support was retired on July 14, 2025. The Flex Consumption plan for Azure Functions reached general availability in 2025 and is now the preferred serverless hosting path, replacing the Linux Consumption plan. ISVs evaluating deployment models will find Azure's managed services eliminate the most significant operational burdens — node provisioning, control-plane upgrades, scheduler management, and GPU driver lifecycle — at the cost of reduced portability compared to self-hosted or on-premises deployments.

---

## 1. Azure Functions

### 1.1 Hosting Plan Overview

Azure Functions is Azure's event-driven, serverless compute service. As of 2025, the available hosting plans are:

| Plan | Status | Scale Limit | Timeout (Default / Max) | Cold Start |
|------|--------|-------------|-------------------------|------------|
| Flex Consumption | GA (Linux only) | 1,000 instances | 30 min / Unbounded | Reduced via always-ready instances |
| Premium | GA (Linux + Windows) | 20–100 Linux / 100 Windows | 30 min / Unbounded | Eliminated via prewarmed workers |
| Dedicated (App Service) | GA | 10–30 (100 on ASE) | 30 min / Unbounded | Not an issue (always-on) |
| Container Apps | GA | 300–1,000 | 30 min / Unbounded | Depends on min replicas |
| Consumption (Windows only) | GA — Linux retiring 2028 | 200 Windows / 100 Linux | 5 min / 10 min | Present when scaled to zero |

[Source: Azure Functions Scale and Hosting — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)
Date: Updated 2025-12-15

### 1.2 Flex Consumption Plan (Preferred Serverless Path)

[FACT] Azure Functions Flex Consumption reached general availability in 2025.
"Azure Functions Flex Consumption is now generally available, providing the highest performance for Azure Functions with concurrency-based scaling for both HTTP and non-HTTP triggers, scale from zero to 1000 instances, and no cold start with the Always Ready feature."
URL: https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-flex-consumption-is-now-generally-available/4298778

[FACT] Flex Consumption instance memory sizes available: 512 MB, 2,048 MB (default), and 4,096 MB.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan

[FACT] Flex Consumption billing includes a monthly free grant of 250,000 executions and 100,000 GB-s of resource consumption per month per subscription.
URL: https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-flex-consumption-is-now-generally-available/4298778

[FACT] Flex Consumption supports virtual network integration for running serverless apps inside a VNet, a capability not available on the classic Consumption plan.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

### 1.3 Premium Plan

[FACT] Premium plan workers are available in three fixed sizes: 1 vCPU/3.5 GB RAM; 2 vCPU/7 GB RAM; 4 vCPU/14 GB RAM.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

[FACT] Premium plan supports up to 20 always-ready instances per app.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan

[FACT] Premium plan billing is "based on the number of core seconds and memory used across needed and prewarmed instances. At least one instance per plan must always be kept warm."
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

[FACT] Premium plan on Linux can scale to 100 instances in some regions.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

### 1.4 Cold Start Behavior

[FACT] On the Consumption plan, "Apps can scale to zero when idle, meaning some requests might have more latencies at startup. The consumption plan does have some optimizations to help decrease cold start time, including pulling from prewarmed placeholder functions that already have the host and language processes running."
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

[FACT] The HTTP triggered function maximum response time is 230 seconds regardless of app timeout setting, due to the Azure Load Balancer idle timeout.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

### 1.5 Durable Functions

[FACT] Azure Durable Functions has four function types: activity, orchestrator, entity, and client functions.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-types-features-overview

[FACT] Orchestrator functions require deterministic code. "Orchestrator function code must be deterministic."
URL: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-code-constraints

[FACT] 2025 Durable Functions additions include: Distributed Tracing with App Insights and OpenTelemetry support, Extended Sessions support in .NET isolated, and Orchestration versioning in public preview.
URL: https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-ignite-2025-update/4469815

[FACT] "The Durable Task Scheduler is the preferred managed backend solution for customers who require high performance, enhanced monitoring of stateful orchestrations."
URL: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-task-scheduler/choose-orchestration-framework

### 1.6 Operational Burden Eliminated by Azure Functions

| Operational Task | Eliminated? | Notes |
|-----------------|-------------|-------|
| Server provisioning and OS management | Yes | Fully managed |
| Runtime patching (.NET, Node, Python, Java) | Yes | Managed runtime lifecycle |
| Horizontal scaling logic | Yes | Event-driven autoscale built in |
| Concurrency / queue-depth scaling decisions | Yes | Flex Consumption: per-function scaling |
| Cold start hardware warm-up | Partial | Premium / Flex: always-ready instances; Consumption: present |
| Cluster control plane | N/A | No cluster concept |

**Estimated FTE for Azure Functions (mid-size ISV, ~50 enterprise customers):**
- Developer configuration and trigger management: 0.1–0.25 FTE
- Monitoring, alerting, and cost governance: 0.1–0.2 FTE
- On-call burden: Minimal (platform-managed scaling and restarts)

**Difficulty Rating: 1/5** (Flex Consumption / Premium for standard workloads)

---

## 2. Azure Container Apps

Azure Container Apps is a fully managed serverless container platform built on Kubernetes and KEDA, abstracting cluster management entirely from the operator.

### 2.1 Scaling with KEDA

[FACT] "Azure Container Apps manages automatic horizontal scaling through a set of declarative scaling rules. As a container app revision scales out, new instances of the revision are created on-demand."
URL: https://learn.microsoft.com/en-us/azure/container-apps/scale-app
Date: Updated 2025-11-04

[FACT] Container Apps scaling limits:

| Scale Limit | Default | Min | Max |
|-------------|---------|-----|-----|
| Minimum replicas per revision | 0 | 0 | 1,000 |
| Maximum replicas per revision | 10 | 1 | 1,000 |

URL: https://learn.microsoft.com/en-us/azure/container-apps/scale-app

[FACT] KEDA polling interval default: 30 seconds. Cool-down period default: 300 seconds. Scale-down stabilization window: 300 seconds. Scale-up stabilization window: 0 seconds.
URL: https://learn.microsoft.com/en-us/azure/container-apps/scale-app

[FACT] KEDA supports scaling triggers against: HTTP requests, TCP connections, CPU, memory, Azure Service Bus, Azure Event Hubs, Apache Kafka, and Redis.
URL: https://learn.microsoft.com/en-us/azure/container-apps/scale-app

[FACT] "When you define a scaling rule, KEDA runs automatically in your container app without needing to install KEDA or turn it on."
URL: https://learn.microsoft.com/en-us/azure/container-apps/dapr-keda-scaling

[FACT] Scale-up step sequence: 1, 4, 8, 16, 32, up to configured maximum. Scale-down step: 100% of replicas that need to shut down are removed at once.
URL: https://learn.microsoft.com/en-us/azure/container-apps/scale-app

[FACT] Scaling algorithm: `desiredReplicas = ceil(currentMetricValue / targetMetricValue)`
URL: https://learn.microsoft.com/en-us/azure/container-apps/scale-app

### 2.2 Dapr Integration

[FACT] Azure Container Apps provides built-in Dapr integration, including service discovery, state management, and pub/sub messaging.
URL: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/serverless/microservices-with-container-apps-dapr

[FACT] KEDA scalers can scale applications and their Dapr sidecars together based on pending inbound events and messages.
URL: https://learn.microsoft.com/en-us/azure/container-apps/dapr-keda-scaling

### 2.3 Revision Management and Traffic Splitting

[FACT] In single revision mode, Container Apps ensures no downtime when creating a new revision; the existing active revision continues to receive 100% of traffic until the new revision is ready.
URL: https://learn.microsoft.com/en-us/azure/container-apps/revisions

[FACT] In multiple revision mode, traffic is split by percentage across revisions, with combined percentage summing to 100%. Supports blue-green and A/B deployment patterns.
URL: https://learn.microsoft.com/en-us/azure/container-apps/traffic-splitting

[FACT] Deployment labels in Azure Container Apps support environment-based routing and feature testing.
URL: https://techcommunity.microsoft.com/blog/appsonazureblog/leveraging-azure-container-apps-labels-for-environment-based-routing-and-feature/4372249

### 2.4 Serverless GPU (Container Apps)

[FACT] Azure Container Apps provides serverless GPU support for NVIDIA A100 and NVIDIA T4 GPUs with per-second billing and scale-to-zero.
URL: https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview
Date: Updated 2025-11-18

[FACT] "As a serverless feature, you pay only for GPUs in use. When enabled, the number of GPUs used for your app rises and falls to meet the load demands of your application."
URL: https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview

[FACT] Serverless GPUs are supported only for Consumption workload profiles; the feature is not supported for Consumption-only environments.
URL: https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview

[FACT] A100 serverless GPU availability as of 2025: Australia East, Brazil South, East US, Italy North, Sweden Central, West US, West US 3. T4 available in additional regions including France Central, Japan East, North Central US, South East Asia, West Europe, West US 2.
URL: https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview

[FACT] Azure Container Apps serverless GPU supports Azure AI Foundry MLFLOW models in public preview as of 2025.
URL: https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview

[FACT] Limitation: Only one container in an app can use the GPU at a time; multi and fractional GPU replicas are not supported.
URL: https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview

### 2.5 Functions on Container Apps

[FACT] Azure Functions can be deployed on Container Apps, enabling containerized function apps in a fully managed environment alongside other microservices. This path is recommended when GPU compute resources are needed for functions.
URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

### 2.6 Operational Burden Eliminated by Container Apps

| Operational Task | Eliminated? | Notes |
|-----------------|-------------|-------|
| Kubernetes control plane management | Yes | Fully managed |
| KEDA installation and configuration | Yes | Built in |
| Dapr installation and sidecar management | Yes | Built in |
| Node/VM provisioning and OS patching | Yes | Fully managed |
| Ingress controller management | Yes | Built-in ingress |
| Certificate management for ingress | Yes | Managed TLS |
| GPU driver and CUDA lifecycle | Yes | Managed for serverless GPUs |
| Cluster upgrade coordination | Yes | Platform managed |

**Estimated FTE (mid-size ISV, ~50 enterprise customers):**
- App configuration, revision management, and scaling rules: 0.2–0.4 FTE
- Monitoring and observability integration: 0.1–0.2 FTE
- On-call: Low (platform manages node failures and scaling)

**Difficulty Rating: 2/5** for standard container workloads; 2/5 for serverless GPU inference (GPU quota request required)

---

## 3. Azure Container Instances

### 3.1 Status Change: GPU Support Retired

[FACT] Azure Container Instances GPU support was retired on July 14, 2025.
URL: https://azure.microsoft.com/en-us/pricing/details/container-instances/

[FACT] The recommended alternative for containerized GPU workloads is Azure Container Apps serverless GPUs (NVIDIA A100 and T4).
URL: https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview

### 3.2 Current Capabilities (Non-GPU)

[FACT] Azure Container Instances remains available for CPU-only serverless container execution. There is no cluster management required; containers are provisioned directly from a container image.
URL: https://azure.microsoft.com/en-us/pricing/details/container-instances/

[FACT] Azure Container Instances can be integrated with AKS as virtual nodes, allowing AKS workloads to burst onto ACI capacity without pre-provisioned node pools.
URL: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-gpu

**ISV Guidance:** For new AI inference workloads requiring containerized GPU, Azure Container Instances is no longer a viable path as of July 2025. Use Azure Container Apps serverless GPUs or dedicated GPU VMs (NC/ND series) instead.

**Difficulty Rating: 1/5** for CPU-only workloads (no cluster management); Not applicable for GPU workloads post-July 2025.

---

## 4. Azure App Service

Azure App Service is a PaaS web hosting platform that manages OS, runtime, TLS, and horizontal scaling, leaving developers to deploy application code or containers.

### 4.1 Pricing Tiers

[FACT] App Service pricing tier categories:

| Category | Tiers | Compute Model |
|----------|-------|---------------|
| Shared compute | Free, Shared | Multi-tenant shared VMs (dev/test only) |
| Dedicated compute | Basic, Standard, Premium, PremiumV2, PremiumV3, PremiumV4 | Dedicated VMs, shared within plan |
| Isolated | IsolatedV2 | Dedicated VMs on dedicated VNet (App Service Environment) |

URL: https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans
Date: Updated 2026-01-29

[FACT] PremiumV3 enables scaling up to 30 instances per plan. PremiumV4 is now available.
URL: https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans

### 4.2 Deployment Slots

[FACT] Deployment slots require Standard tier or above. "When you scale a deployment slot (up or out), you also scale all the other slots of the App Service because all slots share the same App Service Plan."
URL: https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots

[FACT] Number of deployment slots per tier (including production slot):

| Tier | Max Deployment Slots |
|------|---------------------|
| Standard | Up to ~5 slots |
| Premium | 20 slots |
| Isolated (ASE) | 20 slots |

URL: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale (limits table)

[FACT] "Automatic scaling isn't supported for deployment slot traffic."
URL: https://learn.microsoft.com/en-us/azure/app-service/manage-automatic-scaling

### 4.3 Auto-Scaling

[FACT] "Automatic scaling is a scale-out option that automatically handles scaling decisions for your web apps and App Service plans."
URL: https://learn.microsoft.com/en-us/azure/app-service/manage-automatic-scaling

[FACT] Scaling affects all apps in an App Service plan simultaneously. "All apps in an App Service plan scale together, because they share the same underlying compute resources."
URL: https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans

### 4.4 Built-in Authentication (Easy Auth)

[FACT] "Azure App Service provides built-in authentication to secure your applications without writing extensive authentication code."
URL: https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots

[FACT] Built-in authentication (Easy Auth) is not compatible with slot swap with preview when site authentication is enabled in one slot.
URL: https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots

### 4.5 Managed Instance (Preview)

[FACT] App Service Managed Instance is in preview for Windows web apps, limited to Pv4 and Pmv4 SKUs, available in East Asia, West Central US, North Europe, and East US regions as of early 2026.
URL: https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans

[FACT] Managed Instance supports: PowerShell configuration scripts, plan-level VNet integration with private DNS, Azure Key Vault-backed registry adapters, just-in-time RDP access via Azure Bastion, and pre-installed .NET Framework 3.5/4.8.
URL: https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans

### 4.6 Operational Burden Eliminated by App Service

| Operational Task | Eliminated? | Notes |
|-----------------|-------------|-------|
| OS provisioning and patching | Yes | Fully managed |
| Runtime version management | Yes | Managed runtime stack |
| TLS certificate provisioning | Yes | Managed certificates available |
| Load balancer management | Yes | Built-in |
| Blue-green deployments | Yes | Deployment slots handle swap |
| Identity provider integration | Yes | Easy Auth (no code required) |
| Horizontal scaling decisions | Yes | Autoscale rules |
| DDoS protection (basic) | Yes | Platform-level |

**Estimated FTE (mid-size ISV, ~50 enterprise customers):**
- Deployment pipeline, slot management, configuration: 0.25–0.5 FTE
- Monitoring, alerting, capacity planning: 0.1–0.25 FTE
- On-call: Low (platform manages infrastructure)

**Difficulty Rating: 2/5** for standard web app and API workloads; 3/5 if App Service Environment (network-isolated) is required.

---

## 5. Azure Kubernetes Service (Brief)

AKS is Azure's managed Kubernetes service. It eliminates control-plane management (etcd, API server, scheduler) while leaving node pool management, workload configuration, and cluster upgrades to the operator (or automating them via AKS Automatic).

[FACT] "AKS reduces the complexity and operational overhead of managing Kubernetes by offloading much of that responsibility to Azure."
URL: https://learn.microsoft.com/en-us/azure/aks/what-is-aks

[FACT] AKS Automatic "offers an experience that makes the most common tasks on Kubernetes fast and frictionless, while preserving the flexibility, extensibility, and consistency of Kubernetes. Azure takes care of cluster setup, including node management, scaling, and security."
URL: https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic

See [F52: AKS Deep Dive] for detailed coverage of AKS operational profile, node pool management, upgrade strategies, and add-on ecosystem.

**Difficulty Rating: 3/5** (standard AKS); 2/5 (AKS Automatic).

---

## 6. Azure GPU Virtual Machines

For workloads requiring dedicated GPU capacity — large model training, high-throughput batch inference, or multi-GPU parallel workloads — Azure offers purpose-built GPU VM families.

### 6.1 NC Family (Inference and Analytics)

[FACT] NC A100 v4 series: Up to 4 NVIDIA A100 PCIe GPUs with 80 GB memory each; up to 96 non-multithreaded AMD EPYC Milan processor cores; 880 GiB system memory.
URL: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nca100v4-series

[FACT] NCads H100 v5 series: Up to 2 NVIDIA H100 NVL GPUs with 94 GB memory each; up to 96 non-multithreaded AMD EPYC Genoa processor cores; 640 GiB system memory.
URL: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ncadsh100v5-series

[FACT] NCCads H100 v5 series (Confidential Computing): 1 NVIDIA H100 NVL GPU with 94 GB memory; 40 non-multithreaded AMD EPYC Genoa processor cores; 320 GiB system memory.
URL: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nccadsh100v5-series

### 6.2 ND Family (Deep Learning Training and HPC)

[FACT] ND H100 v5 series: 8 NVIDIA H100 Tensor Core GPUs (80 GB each), 96 Intel vCPUs, 1,900 GiB RAM, NVLink 4.0, 3.2 Tbps InfiniBand per VM via dedicated 400 Gb/s NVIDIA Quantum-2 CX7 connections. "ND H100 v5-based deployments can scale up to thousands of GPUs."
URL: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndh100v5-series

[FACT] ND A100 v4 series: 8 NVIDIA Ampere A100 40 GB Tensor Core GPUs; 1.6 TB/s interconnect bandwidth per VM; dedicated 200 GB/s NVIDIA Mellanox HDR InfiniBand connections.
URL: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-family

[FACT] ND MI300X v5 series: 8 AMD Instinct MI300 GPUs; two 4th-gen Intel Xeon Scalable processors (96 physical cores total); 128 GB/s bandwidth per GPU via 4th-gen AMD Infinity Fabric; 896 GB/s aggregate bandwidth; 3.2 Tb/s InfiniBand scale-out.
URL: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-family

### 6.3 Pricing

[FACT] Azure ND96isr H100 v5 (8x H100) on-demand price: approximately $98.32 per hour in U.S. East and Central regions as of 2025.
URL: https://cyfuture.cloud/kb/gpu/azure-nd-h100-v5-pricing-updated-cloud-gpu-costs-2025

[FACT] Azure Spot instances for GPU VMs offer discounts ranging from approximately 20% to 30%, reducing ND H100 v5 to approximately $70–$75 per hour. Reserved instances (1-year or 3-year) can achieve up to 60% discount.
URL: https://cyfuture.cloud/kb/gpu/azure-nd-h100-v5-pricing-updated-cloud-gpu-costs-2025

### 6.4 GPU VM Operational Profile (Comparison to Serverless GPU)

| Dimension | GPU VMs (NC/ND) | Container Apps Serverless GPU |
|-----------|-----------------|-------------------------------|
| GPU type | H100, A100, MI300X (configurable) | A100 or T4 (fixed choice) |
| Multi-GPU per instance | Yes (up to 8) | No (single GPU per replica) |
| InfiniBand interconnect | Yes (ND family) | No |
| Scale-to-zero | No (VM is always running when provisioned) | Yes |
| Billing unit | Hourly VM rate | Per-second GPU usage |
| OS/driver management | ISV responsibility | Platform managed |
| Cold start | None (VM pre-provisioned) | Present (mitigated via artifact streaming) |
| Cluster orchestration | ISV responsibility | Platform managed |

**Estimated FTE for GPU VMs (mid-size ISV running persistent inference cluster):**
- VM provisioning, OS configuration, CUDA/driver setup: 0.25–0.5 FTE initial
- Ongoing patching, monitoring, cluster maintenance: 0.5–1.0 FTE
- On-call for GPU failures or capacity issues: Moderate burden

**Difficulty Rating: 4/5** for self-managed GPU VM clusters; 2/5 for serverless GPU via Container Apps.

---

## 7. Azure Batch

Azure Batch is a managed job scheduler and compute pool manager for large-scale parallel and HPC workloads, including ML training preprocessing, rendering, and data ETL at scale.

### 7.1 Core Architecture

[FACT] "There is no cluster or job scheduler software to install, manage, or scale. Instead, you use Batch APIs and tools, command-line scripts, or the Azure portal to configure, manage, and monitor your jobs."
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview
Date: Updated 2025-07-03

[FACT] "There is no additional charge for using Batch. You only pay for the underlying resources consumed, such as the virtual machines, storage, and networking."
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

[FACT] Batch workflow steps: (1) upload input files and applications to Azure Storage; (2) create a pool of compute nodes, a job, and tasks; (3) tasks download input files and execute; (4) monitor task execution over HTTPS; (5) tasks upload results to Azure Storage; (6) client downloads output files.
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

### 7.2 Supported Workloads

[FACT] Intrinsically parallel workloads supported by Azure Batch include: financial risk modeling (Monte Carlo simulations), VFX and 3D rendering (Autodesk Maya, 3ds Max, Arnold, V-Ray), image analysis, media transcoding, genetic sequence analysis, OCR, and ETL operations.
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

[FACT] Tightly coupled workloads supported via Message Passing Interface (MPI): finite element analysis, fluid dynamics, multi-node AI training. Supported via Microsoft MPI or Intel MPI.
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

[FACT] Azure Batch supports GPU-optimized VM sizes for ML workloads.
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

### 7.3 Cost Optimization

[FACT] Azure Batch supports Azure Spot VMs for discounted compute within Batch pools, enabling significant cost reduction for fault-tolerant workloads.
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

[FACT] HPC H-series pay-as-you-go pricing through Batch starts at $659.92/month; NC-series GPU starts at $657.00/month for NC6.
URL: https://azure.microsoft.com/en-us/pricing/details/batch/cloud-services/

[FACT] Azure Batch integrates with Azure Data Factory for managed ETL pipeline orchestration.
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

### 7.4 Data Residency

[FACT] "Azure Batch does not move or store customer data out of the region in which it is deployed."
URL: https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview

### 7.5 Operational Burden Eliminated by Azure Batch

| Operational Task | Eliminated? | Notes |
|-----------------|-------------|-------|
| Job scheduler installation (SLURM, PBS, LSF) | Yes | Batch is the managed scheduler |
| Node pool provisioning | Yes | API-driven pool creation |
| Task queue management | Yes | Built into Batch service |
| Node failure retry and requeue | Yes | Automatic task requeue on node failure |
| Autoscaling compute nodes | Yes | Automatic scaling based on job queue depth |
| OS patching on compute nodes | Yes | Managed image updates |
| Spot instance interruption handling | Partial | Batch retries on Spot eviction; app must be checkpoint-aware |

**Estimated FTE (mid-size ISV, batch ML preprocessing or rendering):**
- Job definition, pool configuration, API integration: 0.25–0.5 FTE initial
- Ongoing monitoring, cost governance, pool tuning: 0.1–0.25 FTE
- On-call: Low (platform manages node failures; tasks auto-retry)

**Difficulty Rating: 2/5** for standard embarrassingly parallel workloads; 3/5 for tightly coupled MPI workloads requiring specific topology.

---

## 8. Deployment Model Comparison

The following table compares the Azure compute services across the three deployment models relevant to the ISV evaluation. "Cloud-native" here means using these Azure managed services directly. "Managed Kubernetes" means AKS. "On-premises" means self-hosted equivalents.

| Service Domain | On-Premises (Self-Hosted) | Managed K8s (AKS) | Cloud-Native (Azure Managed) |
|----------------|--------------------------|--------------------|-----------------------------|
| **Serverless Functions** | Difficulty: 4/5 — OpenFaaS, Knative; requires K8s cluster + operator expertise | Difficulty: 3/5 — KEDA + Knative on AKS; operational overhead for K8s layer | Difficulty: 1/5 — Azure Functions Flex Consumption; no cluster, pay-per-execution |
| | Self-manage: runtime, scaling, HA | Self-manage: K8s cluster, KEDA, ingress | Est. FTE: 0.2–0.45 |
| **Container Orchestration** | Difficulty: 5/5 — Self-managed K8s: etcd, control plane, node pool | Difficulty: 3/5 — AKS: control plane managed; node pools, upgrades, add-ons remain | Difficulty: 2/5 — Container Apps: no cluster concept |
| | Est. FTE: 1.5–3.0 | Est. FTE: 0.5–1.5 | Est. FTE: 0.3–0.6 |
| **AI Inference (GPU)** | Difficulty: 5/5 — GPU server procurement, CUDA, drivers, scheduler | Difficulty: 4/5 — AKS GPU node pools; device plugin, driver daemonset | Difficulty: 2/5 — Container Apps serverless GPU (A100/T4) |
| | Est. FTE: 2.0–4.0 | Est. FTE: 1.0–2.0 | Est. FTE: 0.2–0.5 |
| **PaaS Web Hosting** | Difficulty: 4/5 — Nginx/Apache + cert-manager + autoscaler | Difficulty: 3/5 — AKS + Ingress + HPA; cert-manager | Difficulty: 1/5 — App Service; slots, Easy Auth, managed certs |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.15–0.35 |
| **Batch / HPC** | Difficulty: 5/5 — SLURM/PBS cluster; node lifecycle, queue management | Difficulty: 4/5 — K8s Jobs + Volcano/Kueue for HPC scheduling | Difficulty: 2/5 — Azure Batch; managed scheduler, pool autoscale |
| | Est. FTE: 1.5–3.0 | Est. FTE: 0.75–1.5 | Est. FTE: 0.25–0.5 |

---

## Key Takeaways

- **Serverless GPU is now the preferred entry point for containerized AI inference on Azure.** With the retirement of Azure Container Instances GPU support on July 14, 2025, Azure Container Apps serverless GPUs (A100/T4, per-second billing, scale-to-zero) is the managed path for ISVs who need GPU capacity without cluster management.

- **Flex Consumption is the replacement for the classic Consumption plan.** Now generally available, it adds per-function concurrency-based scaling, VNet integration, configurable instance memory (512 MB–4 GB), and scale-to-1,000 instances — eliminating the 10-minute timeout cap and the Linux retirement risk of the classic Consumption plan.

- **Azure Batch eliminates the entire HPC scheduler operational layer at no additional service cost.** ISVs building preprocessing pipelines, batch inference jobs, or ML training workflows can use Azure Batch with Spot VMs to achieve significant cost reduction while offloading node provisioning, task scheduling, and retry logic entirely to the platform.

- **App Service deployment slots enable zero-downtime deployments without Kubernetes.** For ISVs building API-heavy SaaS products where Kubernetes is operational overkill, App Service's managed PaaS with slot-based blue-green deployments, built-in Easy Auth, and autoscaling provides 80% of the operational benefit of a full K8s stack at 20–30% of the operational burden.

- **GPU VM families (NC/ND series) remain necessary for training and multi-GPU inference at scale.** At $98.32/hour on-demand for 8x H100 (ND H100 v5), with Spot discounts of 20–30% and Reserved discounts up to 60%, dedicated GPU VMs are the right choice for sustained training workloads where Container Apps serverless GPU's single-GPU-per-replica and absence of InfiniBand interconnect are limiting constraints.

---

## Sources

1. [Azure Functions Scale and Hosting — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)
2. [Azure Functions Premium Plan — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)
3. [Azure Functions Flex Consumption Plan — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)
4. [Azure Functions Flex Consumption GA Announcement — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-flex-consumption-is-now-generally-available/4298778)
5. [Azure Functions Ignite 2025 Update — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-ignite-2025-update/4469815)
6. [Azure Functions Build 2025 — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-%E2%80%93-build-2025/4414655)
7. [Durable Functions Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview)
8. [Durable Functions Types and Features — Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-types-features-overview)
9. [Durable Task Scheduler — Choose Orchestration Framework](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-task-scheduler/choose-orchestration-framework)
10. [Scaling in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/scale-app)
11. [Scale Dapr Applications with KEDA Scalers — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/dapr-keda-scaling)
12. [Traffic Splitting in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/traffic-splitting)
13. [Revision Management in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/revisions)
14. [Deployment Labels in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/deployment-labels)
15. [Microservices with Container Apps and Dapr — Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/serverless/microservices-with-container-apps-dapr)
16. [Using Serverless GPUs in Azure Container Apps — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/gpu-serverless-overview)
17. [Azure Functions on Container Apps Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)
18. [Deploy GPU-Enabled Container Instance — Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-gpu)
19. [Azure Container Instances Pricing — Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/container-instances/)
20. [Azure App Service Plans — Microsoft Learn](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans)
21. [Deploy Staging Slots — Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/deploy-staging-slots)
22. [Enable Automatic Scaling — Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/manage-automatic-scaling)
23. [What is Azure Kubernetes Service — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/what-is-aks)
24. [AKS Automatic Introduction — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic)
25. [NC Family VM Size Series — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nc-family)
26. [NC A100 v4 Series — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nca100v4-series)
27. [NCads H100 v5 Series — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ncadsh100v5-series)
28. [NCCads H100 v5 Series — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nccadsh100v5-series)
29. [ND Family VM Size Series — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-family)
30. [ND H100 v5 Series — Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/ndh100v5-series)
31. [Azure ND H100 v5 Pricing 2025 — Cyfuture Cloud](https://cyfuture.cloud/kb/gpu/azure-nd-h100-v5-pricing-updated-cloud-gpu-costs-2025)
32. [ND96isr H100 v5 Pricing and Specs — Vantage](https://instances.vantage.sh/azure/vm/nd96isrh100-v5)
33. [Azure Batch Technical Overview — Microsoft Learn](https://learn.microsoft.com/en-us/azure/batch/batch-technical-overview)
34. [Azure Batch Pricing — Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/batch/cloud-services/)
35. [App Service Pricing — Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/app-service/windows/)
36. [Azure Container Apps Pricing — Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/container-apps/)

---

## Related — Out of Scope

- **Azure AI Foundry and Model Catalog**: Azure Container Apps serverless GPU now supports deploying Azure AI Foundry MLFLOW models directly; full Foundry service evaluation is out of scope for this file. See F-series files covering Azure AI services.
- **Azure Machine Learning Compute**: AML provides managed training compute clusters (AML Compute) that sit above Azure Batch and GPU VMs; covered separately.
- **Azure NetApp Files and Storage for GPU Workloads**: High-throughput NFS storage for HPC/ML checkpoint storage is a data services topic, out of scope here.
- **AKS Node Pool GPU Configuration**: GPU node pool setup, NVIDIA device plugin daemonsets, and MIG partitioning on AKS are covered in F52: AKS Deep Dive.
