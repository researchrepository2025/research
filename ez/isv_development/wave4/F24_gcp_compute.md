# F24 — GCP Compute Services

**Research Question:** What managed compute services does GCP provide for running application workloads and AI inference, and what operational burden does each eliminate?

---

## Executive Summary

Google Cloud Platform offers a layered compute stack that allows ISVs to trade operational responsibility for abstraction at each tier. At the lowest-friction end, Cloud Run functions (formerly Cloud Functions 2nd gen) and Cloud Run serverless containers eliminate all infrastructure management including provisioning, OS patching, and scaling — with Cloud Run now extending GPU support for AI inference at scale from zero. In the middle tier, Compute Engine provides granular control over VM shape, tenancy, and pricing model (including Spot VMs with up to 91% discount), but restores full operational ownership to the ISV or customer. For AI-specific workloads, GCP's accelerator portfolio — TPU v5e/v5p and GPU machine families A3 (H100/H200) and G2 (L4) — spans cost-optimized inference to large-scale foundation model training, with TPU v5p capable of scaling to 18,432 chips in Multislice configuration. Cloud Batch rounds out the portfolio as a fully managed job orchestrator that removes the need for self-managed schedulers for HPC and ML pipeline workloads.

---

## 1. Cloud Run Functions (formerly Cloud Functions 2nd gen)

### 1.1 Product Identity and Naming History

[FACT] On August 21, 2024, Google rebranded Cloud Functions (2nd gen) as "Cloud Run functions," folding it under the Cloud Run umbrella while retaining its event-driven model.
URL: https://cloud.google.com/blog/products/serverless/google-cloud-functions-is-now-cloud-run-functions

[FACT] "A Cloud Function (2nd gen) is a containerized application deployed as a Cloud Run service, with its event triggers managed by Eventarc."
URL: https://sealos.io/blog/what-is-cloud-run

### 1.2 Core Specifications

[STATISTIC] Default request concurrency per instance: 80. Maximum configurable concurrency per instance: 1,000.
URL: https://docs.cloud.google.com/run/docs/about-concurrency

[FACT] "The Cloud Run autoscaler targets to keep instance concurrency at 60% of the maximum concurrency over a one minute window."
URL: https://docs.cloud.google.com/run/docs/about-instance-autoscaling

[FACT] Minimum instances setting keeps a baseline of warm instances to reduce cold starts; pre-warmed instances eliminate bootstrap time impact on application performance.
URL: https://cloudchipr.com/blog/google-cloud-functions

[FACT] Event-driven triggers use Eventarc, Google's implementation of the CloudEvents specification, supporting event-driven architectures across Google Cloud services.
URL: https://docs.cloud.google.com/run/docs/function-triggers

### 1.3 Cold Start Mitigation

[FACT] Google's Startup CPU Boost feature dynamically allocates additional CPU during container startup; for some measured workloads, startup time was cut in half.
URL: https://cloud.google.com/blog/products/serverless/announcing-startup-cpu-boost-for-cloud-run--cloud-functions

[FACT] "On Cloud Run, the size of your container image does not affect cold start or request processing time. Cold starts aren't affected by the size of the image, but by the image system complexity and initialization time."
URL: https://omermahgoub.medium.com/mitigate-cloud-run-cold-startup-strategies-to-improve-response-time-cad5a6aea327

### 1.4 Billing Model

[FACT] "You are only billed for your function's execution time, metered to the nearest 100 milliseconds, with no charges when your function is idle."
URL: https://cloudchipr.com/blog/google-cloud-functions

### 1.5 Operational Burden Eliminated

Cloud Run functions eliminates: server provisioning, OS updates, security patch management, capacity planning, and scaling configuration. The ISV deploys code or a container image; Google manages all infrastructure beneath it.

---

## 2. Cloud Run

### 2.1 Platform Overview

[FACT] "Cloud Run is a fully managed application platform that lets you run containers that are invocable via requests or events, and is serverless by abstracting away all infrastructure management."
URL: https://sealos.io/blog/what-is-cloud-run

[FACT] Cloud Run supports two workload modes: **Services** (HTTP request-driven, long-running) and **Jobs** (batch/run-to-completion, non-HTTP, up to 24 hours per execution).
URL: https://www.pulumi.com/guides/how-to-gcp-cloudrun-job/

### 2.2 Auto-Scaling Behavior

[FACT] "When a revision does not receive any traffic, by default, it is scaled to zero instances."
URL: https://docs.cloud.google.com/run/docs/about-instance-autoscaling

[FACT] The autoscaler considers CPU utilization (target: 60% across allocated CPUs), request concurrency (target: 60% of max concurrency limit), and configured min/max instance boundaries.
URL: https://docs.cloud.google.com/run/docs/about-instance-autoscaling

[FACT] When maximum instances is exceeded, "Requests will pend for up to 3.5 times average startup time of container instances of this service, or 10 seconds, whichever is greater." Requests beyond the pending limit receive a `429` error.
URL: https://docs.cloud.google.com/run/docs/about-instance-autoscaling

[FACT] Standard Cloud Run instances remain idle for up to 15 minutes after serving their last request; GPU-enabled instances remain idle for up to 10 minutes.
URL: https://docs.cloud.google.com/run/docs/about-instance-autoscaling

### 2.3 GPU Support

[FACT] Cloud Run GPU support reached general availability for NVIDIA L4 GPUs, with no quota request required. Cloud Run with GPU support is covered by Cloud Run's Service Level Agreement.
URL: https://cloud.google.com/blog/products/serverless/cloud-run-gpus-are-now-generally-available

[FACT] Cloud Run supports two GPU options: **NVIDIA L4** (24 GB VRAM, requires minimum 4 CPU and 16 GiB memory) and **NVIDIA RTX PRO 6000 Blackwell** [Preview] (96 GB VRAM, requires minimum 20 CPU and 80 GiB memory).
URL: https://docs.cloud.google.com/run/docs/configuring/services/gpu

[FACT] "Cloud Run instances with an attached L4 or NVIDIA RTX PRO 6000 Blackwell GPU with drivers pre-installed start in approximately 5 seconds."
URL: https://docs.cloud.google.com/run/docs/configuring/services/gpu

[STATISTIC] For a gemma3:4b model, Time-to-First-Token from a cold start (zero instances) was approximately 19 seconds, including instance startup, model loading, and inference execution.
URL: https://www.infoq.com/news/2025/06/google-cloud-run-nvidia-gpu/

[FACT] GPU is billed for the entire duration of the instance lifecycle; instance-based billing is required (not per-request). Services can still scale to zero when idle.
URL: https://docs.cloud.google.com/run/docs/configuring/services/gpu

[FACT] L4 GPU regional availability: Singapore, Belgium, Netherlands, Iowa (invitation-only), Northern Virginia. RTX PRO 6000 Blackwell regional availability (Preview): Singapore (invitation-only), Delhi India (invitation-only), Netherlands, Iowa.
URL: https://docs.cloud.google.com/run/docs/configuring/services/gpu

### 2.4 Operational Comparison Table

| Capability | On-Premises | Managed K8s | Cloud-Native (Cloud Run) |
|---|---|---|---|
| **Container Runtime** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-managed Docker/containerd | GKE-managed runtime | Fully managed by Google |
| | Requires runtime CVE patching | Minor version management | Zero runtime ops |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **Auto-Scaling** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | HPA, custom metrics, manual tuning | GKE HPA/VPA, node pools | Fully automatic |
| | Prometheus, KEDA required | Cluster Autoscaler | Zero config required |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 | Est. FTE: 0.0 |
| **GPU Driver Management** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Manual CUDA install, version pinning | GKE DaemonSet, driver images | Pre-installed by Google |
| | Kernel compatibility management | Node pool driver management | ~5s instance startup |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0 |

---

## 3. GKE Autopilot (Brief Mention)

[FACT] GKE Autopilot is GCP's fully managed Kubernetes mode where Google manages the control plane, node provisioning, scaling, and security hardening. ISVs interact only at the Pod level.
URL: https://cloud.google.com/kubernetes-engine

See [F52: GKE Autopilot] for detailed coverage of GKE Autopilot operational burden, node management, and cost model.

---

## 4. Compute Engine

### 4.1 Machine Families Overview

[FACT] General-purpose N4 machine series is "powered by the fifth generation Intel Xeon Scalable processor (code-named Emerald Rapids)" with sustained all-core turbo frequency of 2.9 GHz, DDR5 memory up to 640 GB, up to 64 vCPUs, and up to 50 Gbps standard network bandwidth.
URL: https://docs.cloud.google.com/compute/docs/general-purpose-machines

[FACT] C3 machine series uses "fourth generation Intel Xeon Scalable processors" delivering "a sustained, all-core turbo frequency of 3.0 GHz" with 8 channels of DDR5 memory and up to 200 Gbps per-VM Tier_1 networking. Primary use cases: high-traffic web/app servers, databases, game servers, data analytics, and CPU-based ML workloads.
URL: https://docs.cloud.google.com/compute/docs/general-purpose-machines

[FACT] E2 machine series targets cost-efficiency for low-traffic web servers, back-office applications, containerized microservices, small databases, virtual desktops, and development/test environments. Custom machine types are supported.
URL: https://docs.cloud.google.com/compute/docs/general-purpose-machines

[FACT] "If your ideal machine shape is in between two predefined types, using a custom machine type could save you as much as 40%."
URL: https://www.cloudzero.com/blog/google-cloud-compute-engine-pricing-guide/

[FACT] Custom machine types are supported on N4, N4D, N4A, N2, N2D, E2, and N1 series. C3 and H3 do not support custom machine types.
URL: https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type

### 4.2 Spot VMs (Successor to Preemptible VMs)

[FACT] "Spot VMs are the latest version of preemptible VMs." Google recommends using Spot VMs instead of preemptible VMs; existing preemptible VMs continue to be available.
URL: https://docs.cloud.google.com/compute/docs/instances/spot

[STATISTIC] Spot VMs offer "up to 91% discounts for many machine types, GPUs, TPUs, and Local SSDs" compared to standard VM pricing.
URL: https://docs.cloud.google.com/compute/docs/instances/spot

[FACT] Spot VM prices "can change up to once every day."
URL: https://docs.cloud.google.com/compute/docs/instances/spot

[FACT] When Compute Engine reclaims a Spot VM, it sends an ACPI signal providing "up to 30 seconds" for graceful shutdown scripts before forcefully stopping or deleting the instance.
URL: https://docs.cloud.google.com/compute/docs/instances/spot

[FACT] "Spot VMs don't have a minimum or maximum runtime unless you specifically limit the runtime." Preemptible VMs could only run for up to 24 hours at a time; Spot VMs do not carry this restriction.
URL: https://docs.cloud.google.com/compute/docs/instances/spot

[FACT] If a Spot VM is preempted within one minute of creation, you are not charged for VM usage during that period.
URL: https://docs.cloud.google.com/compute/docs/instances/spot

[FACT] Spot VMs have no SLA coverage. They are "excess Compute Engine capacity, so their availability varies based on Compute Engine usage." They are best suited for "fault-tolerant workloads," particularly batch processing.
URL: https://docs.cloud.google.com/compute/docs/instances/spot

### 4.3 Sole-Tenant Nodes

[FACT] Sole-tenant nodes provide "exclusive access to a physical Compute Engine server that is dedicated to hosting only your project's VMs," maintaining "a one-to-one mapping to the physical server that is backing the node."
URL: https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes

[STATISTIC] Sole-tenant nodes carry a 10% sole-tenancy premium applied to all vCPU and memory resources.
URL: https://cloud.google.com/compute/sole-tenant-pricing

[FACT] Compliance use cases include: finance and healthcare operations requiring physical isolation, Windows licensing requiring dedicated hardware, and workloads needing increased I/O operations and reduced latency.
URL: https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes

[FACT] Sole-tenant nodes specifically support BYOL scenarios "that require per-core or per-processor licenses." Per-core licensing of Windows Server is only available on sole-tenant nodes.
URL: https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses

[FACT] Available node types exceed 44 configurations spanning: general-purpose (n1, n2, n4 families; 96–224 vCPUs), memory-optimized (m1–m4 families; up to 416 vCPUs, 11,776 GB RAM), compute-optimized (c2–c4d families; 60–384 vCPUs), and GPU-accelerated (a2, a3 families).
URL: https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes

### 4.4 Compute Engine Operational Profile

| Capability | On-Premises (self-hosted) | Compute Engine |
|---|---|---|
| **OS Patching** | Difficulty: 4/5 | Difficulty: 3/5 |
| | Full patch cycle ownership | OS Config, patch management APIs available |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Hardware Refresh** | Difficulty: 5/5 | Difficulty: 1/5 |
| | Procurement, racking, cabling | None — GCP manages hardware |
| | Est. FTE: 0.5+ capital project | Est. FTE: 0.0 |
| **Capacity Planning** | Difficulty: 4/5 | Difficulty: 2/5 |
| | Forecast-driven procurement | On-demand + committed use discounts |
| | Long lead times, CapEx risk | Est. FTE: 0.1 |

---

## 5. TPU v5e and TPU v5p

### 5.1 TPU v5e — Cost-Optimized Training and Inference

[FACT] "Cloud TPU v5e is a combined training and inference (serving) product, where training jobs are optimized for throughput and availability, while serving jobs are optimized for latency."
URL: https://docs.cloud.google.com/tpu/docs/v5e

[STATISTIC] TPU v5e per-chip performance: 197 TFLOPs (BF16), 393 TOPs (Int8).
URL: https://docs.cloud.google.com/tpu/docs/v5e

[STATISTIC] TPU v5e per-chip HBM: 16 GB. HBM bandwidth per chip: 800 GBps. Inter-chip interconnect bandwidth: 400 GBps per chip.
URL: https://docs.cloud.google.com/tpu/docs/v5e

[FACT] A maximum TPU v5e Pod contains 256 chips arranged in a "2D torus" topology, delivering 50.63 PFLOPs aggregate BF16 compute and 1.6 TB/s bisection bandwidth.
URL: https://docs.cloud.google.com/tpu/docs/v5e

[STATISTIC] TPU v5e delivers "up to 2x higher training performance per dollar and up to 2.5x inference performance per dollar for LLMs and gen AI models compared to Cloud TPU v4."
URL: https://cloud.google.com/blog/products/compute/announcing-cloud-tpu-v5e-and-a3-gpus-in-ga

[FACT] "A TPU v5e pod delivers up to 100 quadrillion int8 operations per second, or 100 petaOps of compute power."
URL: https://docs.cloud.google.com/tpu/docs/v5e

[FACT] VM types support 1, 4, or 8 chips per host with varying vCPU counts (24–224) and RAM (48–384 GB). Each TPU VM in a v5e slice contains 1, 4, or 8 chips.
URL: https://docs.cloud.google.com/tpu/docs/v5e

[FACT] Single-host serving supports configurations up to 8 chips using ct5lp-hightpu machine types. Multi-host serving exceeding 8 chips requires the Sax framework for load distribution.
URL: https://docs.cloud.google.com/tpu/docs/v5e

[FACT] Multi-host training supports up to 256-chip slices with topologies ranging from 4x4 to 16x16.
URL: https://docs.cloud.google.com/tpu/docs/v5e

### 5.2 TPU v5p — Large-Scale Foundation Model Training

[FACT] "Cloud TPU v5p is a next-generation accelerator purpose-built to train some of the largest and most demanding generative AI models."
URL: https://docs.cloud.google.com/tpu/docs/v5p

[STATISTIC] A single TPU v5p Pod contains 8,960 chips. Each chip contains 2 TensorCores and 4 SparseCores.
URL: https://docs.cloud.google.com/tpu/docs/v5p

[STATISTIC] TPU v5p per-chip performance: 459 TFLOPs (BF16) and 459 TFLOPs (FP8). HBM capacity per chip: 95 GiB. HBM bandwidth per chip: 2,765 GBps.
URL: https://docs.cloud.google.com/tpu/docs/v5p

[STATISTIC] Bidirectional inter-chip interconnect (ICI) bandwidth per chip: 1,200 GBps. Data center network (DCN) bandwidth per chip: 50 Gbps. Interconnect topology: 3D torus.
URL: https://docs.cloud.google.com/tpu/docs/v5p

[STATISTIC] Single slice training is supported for up to 6,144 chips (maximum topology: 16x16x24). Multislice training scales to 18,432 chips.
URL: https://docs.cloud.google.com/tpu/docs/v5p

[STATISTIC] TPU v5p delivers "over 2x higher FLOPS and 3x more high-bandwidth memory on a per chip basis" compared to TPU v4. v5p trains large LLM models "2.8X faster than the previous-generation TPU v4."
URL: https://cloud.google.com/blog/products/ai-machine-learning/introducing-cloud-tpu-v5p-and-ai-hypercomputer

[STATISTIC] TPU v5p is "4X more scalable than TPU v4 in terms of total available FLOPs per pod."
URL: https://marktechpost.com/2023/12/10/google-unveils-cloud-tpu-v5p-and-ai-hypercomputer-a-leap-in-ai-processing-power/
Note: [PRE-2025: 2023] for this specific claim, but v5p hardware specifications are confirmed in the current 2025 GCP documentation above.

[FACT] TPU v5p uses the ct5p-hightpu-4t machine type: 4 chips per VM, 208 vCPUs, 448 GB RAM.
URL: https://docs.cloud.google.com/tpu/docs/v5p

### 5.3 TPU Roadmap Note

[FACT] "Ironwood TPU will be generally available in Q4, 2025, representing the next generation after v5e and v5p."
URL: https://docs.cloud.google.com/tpu/docs/v5e

### 5.4 TPU Comparative Specifications

| Specification | TPU v5e | TPU v5p |
|---|---|---|
| **Target Use Case** | Cost-optimized training + inference | Large-scale foundation model training |
| **BF16 TFLOPs per chip** | 197 | 459 |
| **HBM per chip** | 16 GB | 95 GiB |
| **HBM Bandwidth per chip** | 800 GBps | 2,765 GBps |
| **Max Pod chips** | 256 | 8,960 |
| **Max Multislice chips** | 256 (single slice only) | 18,432 |
| **Interconnect topology** | 2D torus | 3D torus |
| **VM chips per host** | 1, 4, or 8 | 4 |
| **Cost vs. TPU v4** | 2x training perf/$ | 2.8x faster training |

---

## 6. GPU Instances — A3 and G2 Machine Families

### 6.1 A3 Series — NVIDIA H100 and H200 (Foundation Model Training and Serving)

[FACT] A3 accelerator-optimized machine types have "NVIDIA H100 SXM or NVIDIA H200 SXM GPUs attached" and are "ideal for foundation model training and serving."
URL: https://docs.cloud.google.com/compute/docs/gpus

[FACT] A3 High machine type specifications:

| Machine Type | vCPUs | Memory (GB) | GPU Count | GPU Type | GPU Memory |
|---|---|---|---|---|---|
| a3-highgpu-1g | 26 | 234 | 1 | H100 SXM | 80 GB HBM3 |
| a3-highgpu-2g | 52 | 468 | 2 | H100 SXM | 160 GB HBM3 |
| a3-highgpu-4g | 104 | 936 | 4 | H100 SXM | 320 GB HBM3 |
| a3-highgpu-8g | 208 | 1,872 | 8 | H100 SXM | 640 GB HBM3 |

URL: https://docs.cloud.google.com/compute/docs/gpus

[FACT] A3 Ultra machine type specification: a3-ultragpu-8g — 224 vCPUs, 2,952 GB memory, 8x NVIDIA H200 SXM GPUs, 1,128 GB HBM3e total GPU memory. "Provides the highest network performance in the A3 series."
URL: https://docs.cloud.google.com/compute/docs/gpus

[STATISTIC] A3 High on-demand pricing: approximately $3.00/GPU-hour. Preemptible A3 High: approximately $2.25/GPU-hour. A3 Mega (8-GPU instance in us-central1): approximately $88.49/hour on-demand.
URL: https://cloudprice.net/gcp/compute/instances/a3-highgpu-8g

### 6.2 G2 Series — NVIDIA L4 (Cost-Optimized Inference)

[FACT] "G2 accelerator-optimized machine types have NVIDIA L4 GPUs attached and are ideal for cost-optimized inference, graphics-intensive and high performance computing workloads."
URL: https://docs.cloud.google.com/compute/docs/gpus

[FACT] G2 machine type specifications:

| Machine Type | vCPUs | Memory (GB) | GPU Count | GPU Type | GPU Memory |
|---|---|---|---|---|---|
| g2-standard-4 | 4 | 16 | 1 | L4 | 24 GB GDDR6 |
| g2-standard-8 | 8 | 32 | 1 | L4 | 24 GB GDDR6 |
| g2-standard-24 | 24 | 96 | 2 | L4 | 48 GB GDDR6 |
| g2-standard-48 | 48 | 192 | 4 | L4 | 96 GB GDDR6 |
| g2-standard-96 | 96 | 384 | 8 | L4 | 192 GB GDDR6 |

URL: https://docs.cloud.google.com/compute/docs/gpus

### 6.3 GPU Operational Burden Comparison

| Capability | On-Premises | Managed K8s (GKE) | Cloud Run (GPU) | Compute Engine (GPU) |
|---|---|---|---|---|
| **Driver Management** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 | Difficulty: 2/5 |
| | Manual CUDA install | GKE DaemonSets | Pre-installed; 5s startup | GPU driver attached at boot |
| **Hardware Refresh** | Difficulty: 5/5 | Difficulty: 1/5 | Difficulty: 1/5 | Difficulty: 1/5 |
| | CapEx procurement cycles | GCP managed | GCP managed | GCP managed |
| **Scaling** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 | Difficulty: 3/5 |
| | Manual capacity add | Node pool autoscaling | Zero-to-N automatic | Manual / MIG |
| **Est. Total FTE** | 1.0–2.0 | 0.5–1.0 | 0.0–0.1 | 0.25–0.5 |

---

## 7. Cloud Batch

### 7.1 Service Overview

[FACT] "Batch is a fully managed service that lets you schedule, queue, and execute batch processing workloads on Google Cloud resources. It is suitable for high performance computing (HPC), machine learning (ML), and data-processing workloads."
URL: https://cloud.google.com/batch

[FACT] "Batch provisions resources and manages capacity on your behalf, allowing your batch workloads to run at scale without needing to configure and manage third-party job schedulers, provision and deprovision resources, or request resources one zone at a time."
URL: https://cloud.google.com/blog/products/compute/new-batch-service-processes-batch-jobs-on-google-cloud

### 7.2 Job Types and Task Parallelism

[FACT] Cloud Batch supports two primary runnable types: **script-based** (direct command execution) and **container-based** (Docker image execution).
URL: https://docs.cloud.google.com/batch/docs/create-run-job

[FACT] Task scheduling supports two execution modes: "As soon as possible (AS_SOON_AS_POSSIBLE)" enabling parallel task execution, and "In order (IN_ORDER)" for sequential single-task processing.
URL: https://docs.cloud.google.com/batch/docs/create-run-job

[FACT] Jobs progress through defined states: QUEUED → SCHEDULED → RUNNING → completion states. Custom status events and task logging are supported for monitoring.
URL: https://docs.cloud.google.com/batch/docs/create-run-job

[FACT] Job priority is configurable as a number between 0 (lowest) and 99 (highest); higher-priority jobs can run sooner than lower-priority jobs in the same project queue.
URL: https://cloud.google.com/batch/docs/create-run-job-gpus

### 7.3 GPU and Spot VM Integration

[FACT] Cloud Batch supports GPU workloads and can schedule A3 VM GPU jobs through the Dynamic Workload Scheduler via gcloud CLI or the Batch API.
URL: https://cloud.google.com/batch/docs/create-run-job-gpus

[FACT] Cloud Batch integrates with Spot VMs, offering up to 91% savings versus regular compute instances. Automatic task retry is recommended for Spot VM jobs due to preemption risk.
URL: https://docs.cloud.google.com/batch/docs/create-run-job

[FACT] Job dependency scheduling is available as a Preview feature as of the research date.
URL: https://docs.cloud.google.com/batch/docs/create-run-job

### 7.4 Operational Burden Eliminated by Cloud Batch

| Operational Task | Without Cloud Batch | With Cloud Batch |
|---|---|---|
| Job scheduler setup | Install/manage Slurm, PBS, or HTCondor | Eliminated — fully managed |
| Resource provisioning | Manual VM provisioning per job | Automated create/delete per job lifecycle |
| Queue management | Custom queue configuration | Managed priority queue built-in |
| Failed task retry | Custom retry logic required | Native automatic retry configuration |
| Spot VM preemption handling | Custom checkpoint/restart logic | Built-in retry with Spot VM awareness |
| Capacity across zones | Manual multi-zone requests | Automated zonal provisioning |

[FACT] In 2025, Google Cloud Cluster Toolkit simplifies HPC, AI, and ML environment setup using a YAML blueprint, module catalog, and the gcluster engine to deploy and manage clusters with integrated tools including Slurm, Batch, and Cloud Monitoring.
URL: https://cloud.google.com/blog/products/compute/new-batch-service-processes-batch-jobs-on-google-cloud

---

## 8. Cross-Service Operational Difficulty Summary

| Compute Service | On-Premises Equiv. Difficulty | Managed K8s Equiv. Difficulty | Cloud-Native (GCP Service) Difficulty |
|---|---|---|---|
| **Cloud Run Functions** | 4/5 (custom event infra) | 2/5 (triggers, KEDA) | 1/5 (fully managed) |
| **Cloud Run (containers)** | 4/5 (orchestration, LB) | 2/5 (GKE + ingress) | 1/5 (fully managed) |
| **Cloud Run (GPU)** | 5/5 (CUDA, drivers, scaling) | 3/5 (GKE GPU pools) | 1/5 (pre-installed, ~5s start) |
| **Compute Engine (standard)** | N/A — IS the on-prem analog | 2/5 (node pools) | 2/5 (OS/patch management remains) |
| **Compute Engine (Spot VMs)** | N/A | 2/5 | 2/5 (preemption handling required) |
| **Sole-Tenant Nodes** | 5/5 | N/A (not K8s) | 3/5 (VM-level ops remain; 10% premium) |
| **TPU v5e (serving)** | 5/5 (custom silicon) | 4/5 (GKE + TPU pools) | 3/5 (framework expertise required) |
| **TPU v5p (training)** | 5/5 | 4/5 | 4/5 (deep ML infra expertise) |
| **A3 (H100) GPU VMs** | 5/5 | 3/5 | 3/5 (driver attach, network config) |
| **G2 (L4) GPU VMs** | 4/5 | 3/5 | 2/5 (suitable for inference workloads) |
| **Cloud Batch** | 4/5 (scheduler ops) | 3/5 (Kueue + GKE) | 1/5 (fully managed queue/retry) |

---

## Key Takeaways

- **Cloud Run is GCP's primary zero-ops compute surface for ISVs.** With GPU support now generally available (NVIDIA L4, ~5-second startup) and scale-to-zero billing, Cloud Run eliminates GPU driver management, OS patching, and capacity planning entirely — making it the lowest-friction path for AI inference SaaS deployments with bursty or unpredictable traffic.

- **Spot VMs offer up to 91% cost reduction but require fault-tolerant application design.** With no maximum runtime (unlike legacy preemptible VMs), Spot VMs are viable for long-running batch ML jobs when paired with Cloud Batch's native retry and checkpoint handling — but they provide no SLA and can be reclaimed with only 30-second warning.

- **TPU v5e and v5p serve distinct ISV use cases.** v5e targets cost-optimized inference and smaller-scale training (up to 256 chips, 2x perf/$ over v4), while v5p targets foundation model pre-training at scale (up to 18,432 chips in Multislice, 2.8x faster than v4). Both require deep ML framework expertise (JAX, PyTorch/XLA) regardless of deployment model.

- **Sole-tenant nodes serve a narrow but critical compliance niche.** At a 10% pricing premium, they deliver physical hardware isolation for regulated industries (finance, healthcare) and enable BYOL scenarios that require per-core or per-processor licensing — including Windows Server per-core licensing, which is only available on sole-tenant infrastructure.

- **Cloud Batch eliminates the most operationally expensive aspect of HPC/ML pipelines: the job scheduler.** By managing provisioning, queuing, retries, and deprovisioning automatically — including native Spot VM preemption handling — it removes 0.5–1.0 FTE of infrastructure operations typically required for self-managed Slurm or PBS deployments.

---

## Related — Out of Scope

The following topics were encountered during research but fall outside this file's scope boundary (GCP compute only):

- **Vertex AI:** Managed ML training and serving platform built atop Compute Engine and TPU infrastructure. Covers managed pipelines, model registry, and endpoint serving. Would require separate research.
- **GKE Autopilot detailed specifications:** Covered in detail in F52.
- **GCP networking (VPC, Cloud Load Balancing):** Relevant to Cloud Run and Compute Engine egress design but outside compute scope.
- **Cloud Storage and Filestore:** Used as input/output for Cloud Batch and TPU training jobs; data layer research required separately.
- **Committed Use Discounts (CUDs):** 1-year and 3-year CUDs apply to Compute Engine and some GPU instance types; pricing optimization research outside this scope.

---

## Sources

1. [Google Cloud Functions is now Cloud Run functions](https://cloud.google.com/blog/products/serverless/google-cloud-functions-is-now-cloud-run-functions)
2. [Cloud Run functions (formerly Cloud Functions) — Official Product Page](https://cloud.google.com/functions)
3. [Cloud Run functions Release Notes](https://docs.cloud.google.com/functions/docs/release-notes)
4. [About instance autoscaling in Cloud Run services](https://docs.cloud.google.com/run/docs/about-instance-autoscaling)
5. [Maximum concurrent requests for services — Cloud Run Documentation](https://docs.cloud.google.com/run/docs/about-concurrency)
6. [Set maximum concurrent requests per instance](https://docs.cloud.google.com/run/docs/configuring/concurrency)
7. [Cloud Run Quotas and Limits](https://docs.cloud.google.com/run/quotas)
8. [Startup CPU Boost for Cloud Run and Cloud Functions](https://cloud.google.com/blog/products/serverless/announcing-startup-cpu-boost-for-cloud-run--cloud-functions)
9. [GPU support for services — Cloud Run Documentation](https://docs.cloud.google.com/run/docs/configuring/services/gpu)
10. [GPU support for worker pools — Cloud Run Documentation](https://docs.cloud.google.com/run/docs/configuring/workerpools/gpu)
11. [Cloud Run GPUs are now generally available — Google Cloud Blog](https://cloud.google.com/blog/products/serverless/cloud-run-gpus-are-now-generally-available)
12. [Google Cloud Run Now Offers Serverless GPUs for AI and Batch Processing — InfoQ](https://www.infoq.com/news/2025/06/google-cloud-run-nvidia-gpu/)
13. [Cloud Run function triggers](https://docs.cloud.google.com/run/docs/function-triggers)
14. [Cloud Run Release Notes](https://docs.cloud.google.com/run/docs/release-notes)
15. [Google Cloud Functions in 2025: What Teams Should Know — Cloudchipr](https://cloudchipr.com/blog/google-cloud-functions)
16. [Google Cloud Run Pricing in 2025 — Cloudchipr](https://cloudchipr.com/blog/cloud-run-pricing)
17. [Decoding GCP Serverless: 2025 Guide to Cloud Functions and Cloud Run Timeout Limits](https://systemwatchers.com/decoding-gcp-serverless-your-2025-guide-to-cloud-functions-cloud-run-timeout-limits/)
18. [What Is Google Cloud Run? — Sealos Blog](https://sealos.io/blog/what-is-cloud-run)
19. [Spot VMs — Compute Engine Documentation](https://docs.cloud.google.com/compute/docs/instances/spot)
20. [Preemptible VM instances — Compute Engine Documentation](https://cloud.google.com/compute/docs/instances/preemptible)
21. [Sole-tenancy overview — Compute Engine Documentation](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
22. [Provision VMs on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms)
23. [Sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing)
24. [Bringing your own licenses — Compute Engine Documentation](https://cloud.google.com/compute/docs/nodes/bringing-your-own-licenses)
25. [General-purpose machine family for Compute Engine](https://docs.cloud.google.com/compute/docs/general-purpose-machines)
26. [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource)
27. [Create a VM with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)
28. [GPU machine types — Compute Engine Documentation](https://docs.cloud.google.com/compute/docs/gpus)
29. [Create an A3 High or A2 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized)
30. [GPU pricing — Google Cloud](https://cloud.google.com/compute/gpus-pricing)
31. [a3-highgpu-8g specs and pricing — CloudPrice](https://cloudprice.net/gcp/compute/instances/a3-highgpu-8g)
32. [TPU v5e — Google Cloud Documentation](https://docs.cloud.google.com/tpu/docs/v5e)
33. [TPU v5p — Google Cloud Documentation](https://docs.cloud.google.com/tpu/docs/v5p)
34. [Announcing Cloud TPU v5e and A3 GPUs in GA — Google Cloud Blog](https://cloud.google.com/blog/products/compute/announcing-cloud-tpu-v5e-and-a3-gpus-in-ga)
35. [Introducing Cloud TPU v5p and AI Hypercomputer — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/introducing-cloud-tpu-v5p-and-ai-hypercomputer)
36. [What's new with Google Cloud's AI Hypercomputer architecture](https://cloud.google.com/blog/products/compute/whats-new-with-google-clouds-ai-hypercomputer-architecture)
37. [Cloud Batch — Official Product Page](https://cloud.google.com/batch)
38. [Get started with Batch — Google Cloud Documentation](https://docs.cloud.google.com/batch/docs/get-started)
39. [Job creation and execution overview — Batch Documentation](https://docs.cloud.google.com/batch/docs/create-run-job)
40. [Create and run a job that uses GPUs — Batch Documentation](https://cloud.google.com/batch/docs/create-run-job-gpus)
41. [New Batch service processes batch jobs on Google Cloud — Google Cloud Blog](https://cloud.google.com/blog/products/compute/new-batch-service-processes-batch-jobs-on-google-cloud)
42. [GCP Batch: What It Is, Features and Pricing — Pump.co](https://www.pump.co/blog/gcp-batch)
43. [Tensor Processing Units (TPUs) — Google Cloud](https://cloud.google.com/tpu)
44. [Google Cloud Run Adds Support for NVIDIA L4 GPUs, NVIDIA NIM — NVIDIA Technical Blog](https://developer.nvidia.com/blog/google-cloud-run-adds-support-for-nvidia-l4-gpus-nvidia-nim-and-serverless-ai-inference-deployments-at-scale/)
