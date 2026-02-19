# F55b: Kubernetes GPU & AI Workload Management

**Research Question:** How do GPU scheduling, AI model serving, and ML workloads operate on managed Kubernetes (EKS/AKS/GKE), and what are the requirements, capabilities, and trade-offs compared to cloud-native AI services and on-premises GPU infrastructure?

---

## Executive Summary

Managed Kubernetes has matured into a credible platform for GPU-accelerated AI workloads, driven by the NVIDIA GPU Operator, expanded scheduling primitives, and a rich ecosystem of inference servers (vLLM, KServe, Ray Serve). The Kubernetes v1.34 graduation of Dynamic Resource Allocation (DRA) to General Availability in August 2025 and NVIDIA's open-sourcing of the KAI Scheduler in April 2025 mark a step-change in how clusters handle heterogeneous GPU hardware at scale. Node auto-provisioners — Karpenter on EKS, Node Auto Provisioning (NAP/Karpenter-based) on AKS, and ComputeClasses on GKE — now enable true scale-to-zero GPU economics without manual node-pool management. However, a persistent gap remains versus fully cloud-native AI services: Kubernetes offers deep configurability but imposes 2-4 FTE of dedicated infrastructure expertise to operate GPU workloads in production, compared to near-zero operational overhead for managed endpoints from SageMaker, Vertex AI, or Azure ML. ISVs choosing managed Kubernetes for AI workloads are trading operational complexity for portability, configurability, and cost control over GPU allocation.

---

## 1. NVIDIA GPU Operator: The Foundational Layer

The NVIDIA GPU Operator is the mandatory baseline for GPU workloads on any Kubernetes distribution, automating what would otherwise require manual per-node configuration.

### 1.1 Component Architecture

[FACT] The GPU Operator is composed of multiple cooperating components deployed as DaemonSets:

- **NVIDIA GPU Driver** — enables interaction between the GPU and the operating system
- **NVIDIA Container Toolkit** — allows interaction with GPUs from containerized environments
- **NVIDIA Device Plugin** — exposes GPUs to the kubelet API via the device plugin mechanism
- **GPU Feature Discovery (GFD)** — detects GPUs on nodes and labels them as GPU-enabled
- **DCGM Exporter** — exposes GPU metrics for Prometheus scraping
- **MIG Manager** — partitions A100/H100 GPUs into Multi-Instance GPU slices

Source: [NVIDIA GPU Operator documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/platform-support.html)

### 1.2 Driver Management

[FACT] Installation of GPU Operator v25.10.1 is performed using Helm. The operator manages driver lifecycle, including upgrades, on GPU nodes. If drivers are preinstalled (common on managed node images from EKS/AKS/GKE), the driver component can be disabled with `--set driver.enabled=false`.
URL: [NVIDIA GPU Operator Release Notes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/release-notes.html)

[FACT] A July 2025 security bulletin was issued for the NVIDIA Container Toolkit, demonstrating that the operator's centralized driver management creates a single patching surface for GPU-related CVEs.
URL: [Security Bulletin: NVIDIA Container Toolkit — July 2025](https://nvidia.custhelp.com/app/answers/detail/a_id/5659/~/security-bulletin:-nvidia-container-toolkit---july-2025)

### 1.3 MIG (Multi-Instance GPU) Support

[FACT] MIG Manager watches for changes to the `nvidia.com/mig.config` label on a node and applies the requested MIG configuration. When the label changes, MIG Manager: (1) stops all GPU pods including device plugin, GFD, and DCGM Exporter; (2) stops all host GPU clients listed in `clients.yaml`; (3) applies the MIG reconfiguration; and (4) restarts the GPU pods.
URL: [GPU Operator with MIG — NVIDIA documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-mig.html)

[FACT] As of 2025, when using NVIDIA vGPU with KubeVirt or OpenShift Virtualization, on GPUs that support MIG, administrators can select MIG-backed vGPU instances instead of time-sliced vGPU instances by labeling the node with the name of the MIG-backed vGPU profile.
URL: [GPU Operator with MIG — NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/gpu-operator-mig.html)

[FACT] The Red Hat Developer blog documented MIG for GPU efficiency on Kubernetes in May 2025, confirming MIG is production-supported for A100 and H100 GPUs on Kubernetes clusters.
URL: [Boost GPU efficiency in Kubernetes with NVIDIA Multi-Instance GPU](https://developers.redhat.com/articles/2025/05/27/boost-gpu-efficiency-kubernetes-nvidia-mig)

---

## 2. GPU Scheduling: Resource Primitives and Advanced Strategies

### 2.1 Core Kubernetes GPU Resource Model

[FACT] Standard Kubernetes GPU scheduling uses `resource.limits` with `nvidia.com/gpu` as the resource key. GPUs are not overcommittable under the default device plugin model — every pod must declare an integer number of GPUs.
URL: [GPU Scheduling in Kubernetes: Resource Management Guide — Collabnix](https://collabnix.com/gpu-scheduling-resource-management-in-kubernetes/)

### 2.2 Time-Slicing

[FACT] The NVIDIA GPU Operator enables oversubscription of GPUs through extended options for the NVIDIA Kubernetes Device Plugin, allowing workloads scheduled on oversubscribed GPUs to interleave with one another. A system administrator defines a set of replicas for a GPU, each of which can be handed out independently to a pod.
URL: [Time-Slicing GPUs in Kubernetes — NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)

[FACT] Time-slicing does not provide memory isolation between pods sharing a GPU — all pods on a time-sliced GPU share the full GPU memory address space, creating a risk of memory-related failures in multi-tenant clusters.
URL: [Fractional GPUs in Kubernetes: MIG, Time Slicing & Custom Scheduling — Rafay](https://rafay.co/ai-and-cloud-native-blog/demystifying-fractional-gpus-in-kubernetes-mig-time-slicing-and-custom-schedulers)

### 2.3 Dynamic Resource Allocation (DRA) — GA in 2025

[FACT] Starting with Kubernetes 1.34 (released August 2025), Dynamic Resource Allocation (DRA) has graduated to General Availability and is enabled by default. DRA provides a flexible framework for managing specialized hardware including GPUs and FPGAs, with APIs enabling workloads to specify device properties while the scheduler allocates actual devices.
URL: [Kubernetes v1.34: DRA has graduated to GA — kubernetes.io](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/)

[FACT] Key DRA features in the v1.34 GA release include:
- **Alternative Device Selection** — workloads can specify that they may run on one high-performance GPU or two mid-level GPUs, with the scheduler attempting alternatives in order
- **Consumable Capacity** — a flexible device sharing model where multiple independent resource claims from unrelated pods can each be allocated a share of the same underlying physical device
- **Resource Health Status** — exposes device health via Pod Status for both DRA and device plugin allocations
- **Binding Conditions** — allows the scheduler to delay pod binding until required external resources are fully prepared

URL: [What's new for scheduling and resource management in Kubernetes v1.34? — Datadog](https://www.datadoghq.com/blog/kubernetes-release-august-2025/)

[FACT] The NVIDIA DRA Driver for GPUs manages two resource types — GPUs and ComputeDomains — via two DRA kubelet plugins: `gpu-kubelet-plugin` and `compute-domain-kubelet-plugin`.
URL: [GitHub — NVIDIA/k8s-dra-driver-gpu](https://github.com/NVIDIA/k8s-dra-driver-gpu)

[FACT] AWS documented the use of DRA on EKS with Amazon EC2 P6e-GB200 instances in 2025, confirming cloud-provider support for DRA-based GPU allocation on managed clusters.
URL: [Unlocking next-generation AI performance with Dynamic Resource Allocation on Amazon EKS — AWS](https://aws.amazon.com/blogs/containers/unlocking-next-generation-ai-performance-with-dynamic-resource-allocation-on-amazon-eks-and-amazon-ec2-p6e-gb200/)

### 2.4 Topology-Aware Scheduling

[FACT] For multi-GPU workloads, topology awareness is critical for performance because GPUs connected via NVLink or within the same PCIe tree communicate significantly faster. The topology-aware scheduler plugin enables intelligent GPU placement.
URL: [Kubernetes GPU Scheduling in 2025: Practical Patterns — debugg.ai](https://debugg.ai/resources/kubernetes-gpu-scheduling-2025-kueue-volcano-mig)

### 2.5 NVIDIA KAI Scheduler

[FACT] NVIDIA open-sourced the KAI Scheduler (Kubernetes AI Scheduler) in April 2025 under the Apache 2.0 license. KAI is a Kubernetes-native GPU scheduling solution derived from the Run:ai acquisition.
URL: [NVIDIA Open Sources Run:ai Scheduler — NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/)

[FACT] KAI Scheduler v0.10.0 (October 2025) introduced major features including Topology-Aware Scheduling (TAS), Hierarchical PodGroups, and Time-based Fairshare.
URL: [GitHub — NVIDIA/KAI-Scheduler](https://github.com/NVIDIA/KAI-Scheduler)

[FACT] KAI Scheduler includes a built-in PodGrouper for automatic gang scheduling. PodGroups are atomic scheduling units representing one or more interdependent pods that the scheduler executes as a single unit — vital for distributed training workloads.
URL: [Enable Gang Scheduling and Workload Prioritization in Ray with NVIDIA KAI Scheduler — NVIDIA Technical Blog](https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler/)

---

## 3. KServe and Seldon: Model Serving on Managed Kubernetes

### 3.1 KServe

[FACT] KServe is a CNCF incubating project described as a "standardized distributed generative and predictive AI inference platform for scalable, multi-framework deployment on Kubernetes."
URL: [KServe — GitHub](https://github.com/kserve/kserve)

[FACT] KServe v0.15 (announced June 2025 via CNCF) introduced: enhanced support for generative AI workloads, advanced LLM serving features, improved model and KV caching mechanisms, and integration with Envoy AI Gateway.
URL: [Announcing KServe v0.15: Advancing Generative AI Model Serving — CNCF](https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/)

[FACT] KServe v0.15 upgraded the vLLM backend to vLLM 0.8.5 with support for Qwen3 and Llama4 models, reranking models, and OpenAI-compatible embeddings API.
URL: [KServe 0.15 Release — KServe Documentation](https://kserve.github.io/website/0.15/blog/articles/2025-05-27-KServe-0.15-release/)

[FACT] KServe now integrates with KEDA (Kubernetes Event-Driven Autoscaling) to solve LLM autoscaling challenges. KEDA monitors custom metrics exposed by LLM inference servers to scale based on workload-specific indicators.
URL: [LLM Autoscaler — KServe Documentation](https://kserve.github.io/archive/0.15/modelserving/autoscaling/keda/autoscaling_llm/)

[FACT] Red Hat Developer published a guide for setting up KServe autoscaling for vLLM with KEDA in September 2025, confirming production viability of the KEDA + KServe integration.
URL: [How to set up KServe autoscaling for vLLM with KEDA — Red Hat Developer](https://developers.redhat.com/articles/2025/09/23/how-set-kserve-autoscaling-vllm-keda)

### 3.2 Seldon Core v2

[FACT] Seldon Core 2 is described as "an MLOps and LLMOps framework for deploying, managing and scaling AI systems in Kubernetes — from singular models, to modular and data-centric applications."
URL: [About — Seldon Core 2](https://docs.seldon.io/projects/seldon-core/en/v2/contents/about/index.html)

[FACT] Seldon Core 2 leverages multi-model serving by design, making it the default deployment option. Multi-model serving allows one ML inference server to host multiple models simultaneously, reducing infrastructure hardware requirements including expensive GPUs.
URL: [Multi-Model Serving — Seldon Core 2](https://docs.seldon.ai/seldon-core-2/user-guide/models/mms)

[FACT] Seldon Core 2.9 introduced a new autoscaling implementation using HPA, enabling users to scale model server replicas based on Kubernetes-native or custom metrics.
URL: [Introducing Seldon Core 2.9 and MLServer 1.7 — Seldon](https://www.seldon.io/introducing-core-2-9-and-mlserver-1-7/)

### 3.3 Comparison: KServe/Seldon on Managed K8s vs. Cloud-Native Managed Endpoints

| Capability | KServe/Seldon on Managed K8s | SageMaker Endpoints | Vertex AI Prediction | Azure ML Endpoints |
|---|---|---|---|---|
| Model framework support | Broad (via MLServer, Triton, vLLM) | Broad (built-in containers + custom) | Broad (built-in + custom) | Broad (built-in + custom) |
| LLM serving | Yes (vLLM 0.8.5 backend in v0.15) | Yes (JumpStart, custom) | Yes (via Model Garden) | Yes (via Managed Online Endpoints) |
| Autoscaling trigger | KEDA custom metrics, HPA | Request-based (automatic) | Request-based (automatic) | Request-based (automatic) |
| Serverless GPU | No (nodes must be provisioned) | No (Lambda-based, no GPU) | Yes (limited) | Yes (limited, via ACI) |
| Operational overhead | High — K8s expertise required | Low — managed by AWS | Low — managed by Google | Low — managed by Azure |
| Multi-cloud portability | Yes — runs on any K8s | No — AWS-specific | No — GCP-specific | No — Azure-specific |
| Cost model | Pay for provisioned GPU nodes | Pay per endpoint-hour + inference | Pay per node + prediction requests | Pay per endpoint + compute |

---

## 4. Ray on Kubernetes (KubeRay): Distributed Training and Inference

### 4.1 KubeRay Overview

[FACT] KubeRay is described as "a powerful, open-source Kubernetes operator that simplifies the deployment and management of Ray applications on Kubernetes." Each Ray cluster consists of a head node pod and a collection of worker node pods.
URL: [Ray on Kubernetes — Ray 2.53.0 documentation](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)

[FACT] KubeRay introduces three Kubernetes Custom Resource Definitions (CRDs): `RayCluster`, `RayJob`, and `RayService`, each tailored to different use cases.
URL: [Getting Started with KubeRay — Ray 2.53.0 documentation](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html)

### 4.2 KubeRay v1.4 (2025)

[FACT] KubeRay v1.4 was released with over 400 commits contributed by approximately 30 contributors. Key highlights include the KubeRay API Server V2 and the Ray Autoscaler V2, delivering significant improvements in reliability and observability.
URL: [Introducing KubeRay v1.4 — Anyscale](https://www.anyscale.com/blog/kuberay-v1-4)

[FACT] The NVIDIA KAI Scheduler is natively integrated with KubeRay, enabling gang scheduling, workload autoscaling, and workload prioritization for Ray environments on Kubernetes.
URL: [Gang scheduling, queue priority, and GPU sharing for RayClusters using KAI Scheduler — Ray 2.53.0](https://docs.ray.io/en/latest/cluster/kubernetes/k8s-ecosystem/kai-scheduler.html)

### 4.3 Google Cloud and GKE Integration

[FACT] Google Cloud and Anyscale have integrated Anyscale RayTurbo — a high-performance runtime for Ray — with Google Kubernetes Engine (GKE), creating a unified platform described as "a distributed operating system for AI."
URL: [Google Cloud Integrates Anyscale's RayTurbo with GKE — Anyscale](https://www.anyscale.com/blog/google-cloud-integrates-anyscales-rayturbo)

### 4.4 Ray Serve Autoscaling (2025)

[FACT] Ray Serve in 2025 supports async inference, custom request routing, and custom autoscaling, providing flexibility for advanced LLM serving patterns beyond what standard HPA can offer.
URL: [Ray Serve: Advancing Flexibility with Async Inference, Custom Request Routing, and Custom Autoscaling — Anyscale](https://www.anyscale.com/blog/ray-serve-autoscaling-async-inference-custom-routing)

---

## 5. vLLM and TGI on Kubernetes: LLM Inference at Scale

### 5.1 vLLM Kubernetes Architecture

[FACT] Kubernetes provides GPU-targeted scheduling for vLLM pods via node selectors, taints/tolerations, and affinity labels, ensuring vLLM pods get scheduled on GPU-enabled nodes while preventing non-GPU pods from consuming expensive GPU resources.
URL: [Using Kubernetes — vLLM documentation](https://docs.vllm.ai/en/stable/deployment/k8s/)

[FACT] vLLM supports a prefill/decode disaggregated architecture in production, where the vLLM Head Deployment coordinates with separate vLLM Prefill and vLLM Decoding Deployments. This allows each phase to be optimized and scaled independently based on workload characteristics.
URL: [vLLM Production Deployment: Building High-Throughput Inference Serving Architecture — Introl Blog](https://introl.com/blog/vllm-production-deployment-inference-serving-architecture)

### 5.2 vLLM Router (December 2025)

[FACT] vLLM introduced the vLLM Router in December 2025, a high-performance load balancer built in Rust for minimal overhead. The router operates in a Kubernetes-native mode, automatically discovering, monitoring, and routing to vLLM worker pods using label selectors.
URL: [vLLM Router: A High-Performance and Prefill/Decode Aware Load Balancer — vLLM Blog](https://blog.vllm.ai/2025/12/13/vllm-router-release.html)

### 5.3 Prefill/Decode Disaggregation Performance

[FACT] The llm-d v0.4 release (December 2025) — a Kubernetes-native distributed inferencing project from Red Hat — demonstrated a 40% reduction in per-output-token latency for DeepSeek V3.1 on H200 GPUs using prefill/decode disaggregation with Intel XPU and Google TPU support.
URL: [llm-d: Kubernetes-native distributed inferencing — Red Hat Developer](https://developers.redhat.com/articles/2025/05/20/llm-d-kubernetes-native-distributed-inferencing)

[FACT] P/D disaggregation achieves lower inter-token latency (ITL) by eliminating prefill interference with the decode phase, and can improve overall throughput by specializing prefill workers (compute-bound) and decode workers (latency-bound) separately.
URL: [Disaggregated Prefilling — vLLM documentation](https://docs.vllm.ai/en/latest/features/disagg_prefill/)

### 5.4 TGI vs. vLLM

[FACT] Text Generation Inference (TGI) from Hugging Face "prioritizes production readiness, operational maturity, and ecosystem integration over raw performance" and "while it may not achieve the highest throughput in synthetic benchmarks, its comprehensive feature set and battle-tested reliability make it preferred for large-scale deployments requiring robust operation."
URL: [vLLM vs Ollama vs llama.cpp vs TGI vs TensorRT-LLM: 2025 Guide — ITECS](https://itecsonline.com/post/vllm-vs-ollama-vs-llama.cpp-vs-tgi-vs-tensort)

### 5.5 Red Hat vLLM Benchmarking on Kubernetes (December 2025)

[FACT] Red Hat published a deployment and benchmarking guide for vLLM with GuideLLM on Kubernetes in December 2025, confirming production viability of vLLM as a Kubernetes-deployed inference server.
URL: [How to deploy and benchmark vLLM with GuideLLM on Kubernetes — Red Hat Developer](https://developers.redhat.com/articles/2025/12/24/how-deploy-and-benchmark-vllm-guidellm-kubernetes)

---

## 6. Node Auto-Provisioning: GPU Nodes On Demand

### 6.1 Karpenter on EKS

[FACT] Karpenter is an open-source Kubernetes autoscaler created by AWS that automatically provisions compute capacity in response to unschedulable pods. It manages Spot instances with advanced consolidation by specifying capacity type as "spot" in NodePool configuration.
URL: [Compute and Autoscaling — Amazon EKS Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html)

[FACT] For GPU support on EKS with Karpenter, workload manifests must include a GPU resource requirement, and the NVIDIA device plugin DaemonSet must be deployed before Karpenter can properly advertise GPU capacity.
URL: [Karpenter — Amazon EKS Best Practices Guides](https://aws.github.io/aws-eks-best-practices/karpenter/)

[FACT] Karpenter + KEDA integration on EKS enables event-driven GPU provisioning: KEDA scales pods based on queue depth or custom metrics, and Karpenter provisions GPU nodes in response to pending pods. A published AWS blog post documents this pattern.
URL: [Scalable and Cost-Effective Event-Driven Workloads with KEDA and Karpenter on Amazon EKS — AWS](https://aws.amazon.com/blogs/containers/scalable-and-cost-effective-event-driven-workloads-with-keda-and-karpenter-on-amazon-eks/)

[FACT] AWS documented a scale-to-zero GPU pattern for EKS using OpenFaaS, Karpenter, and GPU nodes, enabling cold-start GPU inference where nodes are fully deprovisioned between requests.
URL: [Scale to zero GPUs with OpenFaaS, Karpenter and AWS EKS — OpenFaaS](https://www.openfaas.com/blog/scale-to-zero-gpus/)

### 6.2 Node Auto Provisioning (NAP) on AKS

[FACT] Node Auto Provisioning on AKS is "based on the open-source Karpenter" and automatically deploys, configures, and manages Karpenter on AKS clusters. NAP provisions, scales, and manages VMs in response to pending pod pressure.
URL: [Overview of Node Auto-Provisioning (NAP) in Azure Kubernetes Service — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/node-auto-provisioning)

[FACT] NAP reached General Availability on AKS in mid-July 2025 with documentation refreshed in late September/October 2025.
URL: [Azure AKS goes just-in-time on nodes (Powered by Karpenter) — Medium](https://medium.com/h7w/azure-aks-goes-just-in-time-on-nodes-powered-by-karpenter-927957d0821c)

[FACT] AKS in November 2025 published documentation on fully managed GPU workloads with Azure Linux on AKS, confirming first-party GPU node pool support for AI workloads.
URL: [Fully Managed GPU workloads with Azure Linux on Azure Kubernetes Service (AKS) — AKS Engineering Blog](https://blog.aks.azure.com/2025/11/18/azure-linux-gpu-on-aks)

### 6.3 GKE Autopilot and ComputeClasses

[FACT] GKE Autopilot uses specialized Accelerator compute classes to run GPU pods, automatically provisioning GPU-enabled nodes matching workload requirements, including any required NVIDIA driver setup. Autopilot automatically taints GPU nodes to prevent non-GPU pods from running on them.
URL: [Deploy GPU workloads in Autopilot — GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)

[FACT] GKE now provisions fast-starting nodes for G2 nodes with NVIDIA L4 GPUs in Autopilot mode, with significantly lower startup time compared to standard node provisioning.
URL: [Run GPU workloads on GKE Autopilot — Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/run-gpu-workloads-on-gke-autopilot)

[FACT] GKE introduced a provisioning mode for ComputeClasses that automatically provisions resources without changing how other workloads are scheduled on existing node pools, enabling incremental adoption.
URL: [About GPUs in Google Kubernetes Engine (GKE) — GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)

[FACT] AWS is the only cloud provider officially supported by the Karpenter maintainers, while Azure (NAP/AKS) and GKE support exists through cloud-provider-specific implementations of the Karpenter API.
URL: [A Complete Guide to Karpenter — DevZero](https://www.devzero.io/blog/karpenter-guide)

---

## 7. Cost Management: GPU Node Economics

### 7.1 Spot and Preemptible GPU Instances

[FACT] Spot instances on AWS offer discounts of up to 90% compared to On-Demand pricing. Spot capacity is available for many P-family GPU instances, especially older generations like P3 and P2.
URL: [Amazon EC2 Spot Instances Pricing — AWS](https://aws.amazon.com/ec2/spot/pricing/)

[FACT] In June 2025, AWS announced price reductions of up to 33% for P4d and P4de instances, effective on On-Demand purchases beginning June 1, 2025, and on Savings Plan purchases after June 4, 2025.
URL: [Pricing and usage model updates for Amazon EC2 instances accelerated by NVIDIA GPUs — AWS](https://aws.amazon.com/about-aws/whats-new/2025/06/pricing-usage-model-ec2-instances-nvidia-gpus/)

[FACT] Azure Spot VMs provide up to 90% savings compared to pay-as-you-go prices. AKS Spot node pools are suitable for interruptible batch jobs like ML training or CI builds, but are unsuitable for production workloads requiring constant uptime.
URL: [Scaling Safely with Azure AKS Spot Node Pools Using Cluster Autoscaler Priority Expander — AKS Engineering Blog](https://blog.aks.azure.com/2025/07/17/Scaling-safely-with-spot-on-aks)

[FACT] GKE Spot VMs are documented as supporting GPU workloads with both the cluster autoscaler and node auto-provisioning.
URL: [Spot VMs — Google Kubernetes Engine documentation](https://cloud.google.com/kubernetes-engine/docs/concepts/spot-vms)

### 7.2 GPU Utilization Gap

[FACT] "GPUs sit reserved and underutilized 60-80% of the time, with teams paying $3-4/hour per GPU for capacity that only gets meaningful use for a few hours every day."
URL: [Kubernetes GPU Optimization for Real-Time AI Inference — ScaleOps](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/)

[FACT] Kubernetes provides limited visibility into actual GPU resource consumption: "you can see that a GPU is 'allocated', but not which container is using how much memory, what actual compute utilization looks like over time, or whether that allocation is justified."
URL: [Kubernetes GPU Optimization for Real-Time AI Inference — ScaleOps](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/)

### 7.3 Resilience Strategies for Cost-Optimized GPU Pools

[FACT] AWS EKS best practices documentation requires that a cluster have at least one existing non-GPU node pool using standard VMs before creating a GPU node pool using Spot VMs.
URL: [Compute and Autoscaling — Amazon EKS Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html)

[FACT] Recommended spot GPU resilience pattern: create multiple node pools of different VM families and SKUs, use node selectors/affinity/taints to schedule tolerant workloads onto spot nodes, and distribute node pools across multiple availability zones to minimize simultaneous spot interruptions.
URL: [Spot Instances in Kubernetes: Architecture & Cost Guide — Sedai](https://sedai.io/blog/spot-instances-in-k8s-strategy)

---

## 8. CNCF AI Conformance: Emerging Standardization

[FACT] CNCF launched the Certified Kubernetes AI Conformance Program on November 11, 2025 at KubeCon + CloudNativeCon North America in Atlanta. The program creates open, community-defined standards for running AI workloads on Kubernetes.
URL: [CNCF Launches Kubernetes AI Conformance Program — CNCF](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/)

[FACT] The AI Conformance program scope includes defining a reference architecture, framework support requirements, and test criteria for key capabilities such as GPU integration, volume handling, and job-level networking.
URL: [KubeCon 2025: CNCF to Standardize AI Workloads — Intellyx](https://intellyx.com/2025/11/18/kubecon-2025-cncf-to-standardize-ai-workloads/)

[FACT] Certification is based on self-assessment. A platform must already be Kubernetes Conformant, and AI conformance builds on top of base Kubernetes conformance. The program reached v1.0 and began work on a v2.0 roadmap.
URL: [GitHub — cncf/k8s-ai-conformance](https://github.com/cncf/k8s-ai-conformance)

[FACT] AKS achieved Kubernetes AI Conformance certification, documented December 2025.
URL: [AI Conformant Azure Kubernetes Service (AKS) clusters — AKS Engineering Blog](https://blog.aks.azure.com/2025/12/05/kubernetes-ai-conformance-aks)

---

## 9. Gap Analysis: Managed Kubernetes vs. Cloud-Native AI Services

### 9.1 Capability Comparison Table

| Capability | On-Prem (Self-Hosted) | Managed K8s (EKS/AKS/GKE) | Cloud-Native AI Services |
|---|---|---|---|
| **GPU Driver Management** | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
|  | Full manual management | GPU Operator automates; driver updates may require node drains | Fully managed by cloud provider |
|  | Custom scripts, reboots | Helm-deployed operator | No user action required |
|  | Est. FTE: 0.5-1.0 | Est. FTE: 0.1-0.25 | Est. FTE: 0 |
| **GPU Scheduling & Allocation** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
|  | SLURM or custom schedulers | K8s device plugin, DRA, KAI Scheduler, time-slicing | Managed endpoint auto-routes |
|  | Manual topology awareness | KAI TAS, gang scheduling | No scheduler access |
|  | Est. FTE: 0.5 | Est. FTE: 0.25-0.5 | Est. FTE: 0 |
| **Model Serving** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
|  | Custom deployment pipelines | KServe, Seldon, vLLM, TGI as K8s workloads | SageMaker, Vertex AI, Azure ML |
|  | Full control, no abstractions | KEDA + custom metrics for scaling | Framework-specific abstractions |
|  | Est. FTE: 1.0-2.0 | Est. FTE: 0.5-1.0 | Est. FTE: 0.1-0.25 |
| **Node Auto-Provisioning** | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
|  | Manual hardware provisioning | Karpenter/NAP/GKE ComputeClasses | Automatic, provider-managed |
|  | Days-to-weeks lead time | Sub-minute provisioning | Sub-minute provisioning |
|  | Est. FTE: 1.0+ | Est. FTE: 0.1-0.25 | Est. FTE: 0 |
| **Cost Optimization** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
|  | Capital expense + power costs | Spot/preemptible GPU nodes (60-90% savings) | Reserved capacity pricing, spot for batch |
|  | Long hardware refresh cycles | Cluster autoscaler + Karpenter consolidation | Provider-managed bin-packing |
|  | Est. FTE: 0.5 | Est. FTE: 0.25-0.5 | Est. FTE: 0.1 |

*FTE estimates assume a mid-size deployment serving 50 enterprise customers on a single cluster. On-call burden is excluded from active work estimates.*

### 9.2 Persistent Gaps in Managed Kubernetes vs. Cloud-Native

**[FACT — SageMaker serverless GPU limitation]** "GPU based inference isn't currently supported on SageMaker Serverless Inference. Serverless GPU is not supported in SageMaker since it is based on Lambda technology, which currently doesn't support GPU." This means that serverless cold-start economics, which cloud-native proponents cite as an advantage, do not extend to GPU inference on SageMaker.
URL: [Is GPU Serverless inferencing for custom LLM models? — AWS re:Post](https://repost.aws/questions/QUlHAbaJiIRt-eem9gizSmOQ/is-gpu-serverless-inferencing-for-custom-llm-models)

**[FACT — Utilization observability gap]** Kubernetes offers no native workload-level visibility into per-container GPU memory consumption or compute utilization over time — only coarse "allocated vs. not allocated" status. DCGM Exporter (from NVIDIA GPU Operator) partially addresses this via Prometheus metrics, but requires additional tooling to operationalize.
URL: [Kubernetes GPU Optimization for Real-Time AI Inference — ScaleOps](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/)

**[UNVERIFIED — Auto-optimization gap]** Cloud-native managed endpoints (SageMaker, Vertex AI, Azure ML) apply proprietary compiler optimizations (TensorRT, XLA, etc.) to user models automatically at deployment time. Managed Kubernetes does not perform equivalent optimizations unless the ISV explicitly configures TensorRT or similar in their inference server container image. This claim reflects common practitioner understanding but no single authoritative 2025 source was found that directly compares automatic optimization coverage across all three providers.

**[FACT — Expertise barrier]** "Kubernetes clusters management often involves continuous monitoring, upgrading and scaling — tasks that may take a lot of resources and require a dedicated operations team. Additionally, ensuring high availability and effectively managing GPU resources, security and networking are critical within a Kubernetes cluster."
URL: [Why Kubernetes is Great for Running AI/MLOps Workloads — Cloud Native Now](https://cloudnativenow.com/contributed-content/why-kubernetes-is-great-for-running-ai-mlops-workloads/)

**[FACT — Multi-cloud portability advantage]** KServe, vLLM, and Ray can be deployed on any CNCF-conformant Kubernetes distribution (including on-premises). Cloud-native AI services (SageMaker, Vertex AI, Azure ML) are provider-specific, creating vendor lock-in that managed Kubernetes avoids.
URL: [Running AI/ML on Kubernetes: From Prototype to Production — DZone](https://dzone.com/articles/ai-ml-kubernetes-mlflow-kserve-vllm)

---

## Key Takeaways

- **DRA is now the GPU allocation primitive of choice.** Kubernetes v1.34's graduation of Dynamic Resource Allocation (DRA) to GA in August 2025 replaces the coarse integer-GPU device plugin model with fine-grained, hardware-topology-aware allocation — a fundamental shift that brings K8s GPU scheduling materially closer to what bare-metal schedulers (SLURM) have offered. ISVs evaluating managed Kubernetes for AI workloads should plan against DRA-native APIs rather than legacy device plugin patterns.

- **The NVIDIA GPU Operator + KAI Scheduler + KServe/vLLM stack is the 2025 production reference architecture.** These three layers — driver/device management, gang-scheduling with topology awareness, and model serving with KEDA-based autoscaling — are all generally available and production-validated by Red Hat, Google Cloud, and AWS in 2025. The stack is deployable on EKS, AKS, and GKE with comparable capabilities.

- **Node auto-provisioners (Karpenter, NAP, GKE ComputeClasses) eliminate the manual GPU node management bottleneck.** Scale-to-zero GPU economics are achievable on all three major managed Kubernetes providers in 2025, closing a gap that previously required cloud-native services to achieve. Spot/preemptible GPU instances can reduce compute costs by 60-90% for batch and training workloads.

- **Managed Kubernetes requires 2-4 FTE of dedicated GPU infrastructure expertise vs. near-zero for cloud-native managed endpoints.** The operational gap is real and persistent. Cloud-native services (SageMaker Endpoints, Vertex AI Prediction, Azure ML Managed Online Endpoints) absorb driver management, scheduling, autoscaling, and observability. ISVs choosing managed Kubernetes must staff and fund this operational burden explicitly.

- **The CNCF AI Conformance Program (v1.0, November 2025) signals maturing standardization but does not eliminate fragmentation.** Certification is self-assessed and builds on base K8s conformance, meaning GPU integration specifics still vary by cloud provider. ISVs should validate each managed K8s provider against the CNCF AI Conformance criteria before committing to a multi-cloud K8s GPU strategy.

---

## Related — Out of Scope

- **On-premises GPU hardware procurement and data center design** (F39): GPU node pool cost comparisons in this file assume cloud-hosted VMs. On-prem CAPEX economics, cooling requirements, and interconnect (InfiniBand vs. Ethernet) are covered separately.
- **Cloud-native AI services in depth** (Waves 2-4): SageMaker, Vertex AI, and Azure ML are referenced in this file only as comparison points. Detailed feature coverage, pricing, and ISV integration patterns are out of scope here.
- **Model serving architecture and model registry design** (F5): vLLM and KServe are covered here only as K8s workload patterns; model versioning, A/B testing, and shadow deployment architectures belong to F5.

---

## Sources

1. [NVIDIA GPU Operator — Platform Support](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/platform-support.html)
2. [GPU Operator with MIG — NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-mig.html)
3. [GPU Operator with MIG — NVIDIA Cloud Native Technologies](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/gpu-operator-mig.html)
4. [NVIDIA GPU Operator Release Notes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/release-notes.html)
5. [Security Bulletin: NVIDIA Container Toolkit — July 2025](https://nvidia.custhelp.com/app/answers/detail/a_id/5659/~/security-bulletin:-nvidia-container-toolkit---july-2025)
6. [Boost GPU efficiency in Kubernetes with NVIDIA Multi-Instance GPU — Red Hat Developer](https://developers.redhat.com/articles/2025/05/27/boost-gpu-efficiency-kubernetes-nvidia-mig)
7. [MIG Support in Kubernetes — NVIDIA Cloud Native Technologies](https://docs.nvidia.com/datacenter/cloud-native/kubernetes/latest/index.html)
8. [GitHub — NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)
9. [Time-Slicing GPUs in Kubernetes — NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)
10. [Fractional GPUs in Kubernetes: MIG, Time Slicing & Custom Scheduling — Rafay](https://rafay.co/ai-and-cloud-native-blog/demystifying-fractional-gpus-in-kubernetes-mig-time-slicing-and-custom-schedulers)
11. [GPU Scheduling in Kubernetes: Resource Management Guide — Collabnix](https://collabnix.com/gpu-scheduling-resource-management-in-kubernetes/)
12. [Kubernetes GPU Scheduling in 2025: Practical Patterns — debugg.ai](https://debugg.ai/resources/kubernetes-gpu-scheduling-2025-kueue-volcano-mig)
13. [Kubernetes v1.34: DRA has graduated to GA — kubernetes.io](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/)
14. [Dynamic Resource Allocation — Kubernetes documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
15. [What's new for scheduling and resource management in Kubernetes v1.34? — Datadog](https://www.datadoghq.com/blog/kubernetes-release-august-2025/)
16. [GitHub — NVIDIA/k8s-dra-driver-gpu](https://github.com/NVIDIA/k8s-dra-driver-gpu)
17. [Unlocking next-generation AI performance with DRA on Amazon EKS — AWS](https://aws.amazon.com/blogs/containers/unlocking-next-generation-ai-performance-with-dynamic-resource-allocation-on-amazon-eks-and-amazon-ec2-p6e-gb200/)
18. [About dynamic resource allocation in GKE — Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation)
19. [Delve into Dynamic Resource Allocation on Kubernetes — AKS Engineering Blog](https://blog.aks.azure.com/2025/11/17/dra-devices-and-drivers-on-kubernetes)
20. [Kubernetes Primer: Dynamic Resource Allocation (DRA) for GPU Workloads — The New Stack](https://thenewstack.io/kubernetes-primer-dynamic-resource-allocation-dra-for-gpu-workloads/)
21. [NVIDIA Open Sources Run:ai Scheduler — NVIDIA Technical Blog](https://developer.nvidia.com/blog/nvidia-open-sources-runai-scheduler-to-foster-community-collaboration/)
22. [GitHub — NVIDIA/KAI-Scheduler](https://github.com/NVIDIA/KAI-Scheduler)
23. [Enable Gang Scheduling and Workload Prioritization in Ray with NVIDIA KAI Scheduler — NVIDIA Technical Blog](https://developer.nvidia.com/blog/enable-gang-scheduling-and-workload-prioritization-in-ray-with-nvidia-kai-scheduler/)
24. [GPU Sharing and Time-Slicing — NVIDIA/KAI-Scheduler DeepWiki](https://deepwiki.com/NVIDIA/KAI-Scheduler/6.2-gpu-sharing-and-time-slicing)
25. [Optimizing GPU Scheduling in Kubernetes with NVIDIA KAI and vCluster](https://www.vcluster.com/blog/gpu-scheduling-with-nvidia-kai-and-vcluster)
26. [Announcing KServe v0.15: Advancing Generative AI Model Serving — CNCF](https://www.cncf.io/blog/2025/06/18/announcing-kserve-v0-15-advancing-generative-ai-model-serving/)
27. [KServe 0.15 Release — KServe Documentation](https://kserve.github.io/website/0.15/blog/articles/2025-05-27-KServe-0.15-release/)
28. [LLM Autoscaler — KServe Documentation](https://kserve.github.io/archive/0.15/modelserving/autoscaling/keda/autoscaling_llm/)
29. [GitHub — kserve/kserve](https://github.com/kserve/kserve)
30. [How to set up KServe autoscaling for vLLM with KEDA — Red Hat Developer](https://developers.redhat.com/articles/2025/09/23/how-set-kserve-autoscaling-vllm-keda)
31. [About — Seldon Core 2](https://docs.seldon.io/projects/seldon-core/en/v2/contents/about/index.html)
32. [Multi-Model Serving — Seldon Core 2](https://docs.seldon.ai/seldon-core-2/user-guide/models/mms)
33. [Introducing Seldon Core 2.9 and MLServer 1.7 — Seldon](https://www.seldon.io/introducing-core-2-9-and-mlserver-1-7/)
34. [Ray on Kubernetes — Ray 2.53.0 documentation](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)
35. [Getting Started with KubeRay — Ray 2.53.0 documentation](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html)
36. [Introducing KubeRay v1.4 — Anyscale](https://www.anyscale.com/blog/kuberay-v1-4)
37. [Gang scheduling, queue priority, and GPU sharing for RayClusters using KAI Scheduler — Ray 2.53.0](https://docs.ray.io/en/latest/cluster/kubernetes/k8s-ecosystem/kai-scheduler.html)
38. [Google Cloud Integrates Anyscale's RayTurbo with GKE — Anyscale](https://www.anyscale.com/blog/google-cloud-integrates-anyscales-rayturbo)
39. [Ray Serve: Advancing Flexibility with Async Inference, Custom Request Routing, and Custom Autoscaling — Anyscale](https://www.anyscale.com/blog/ray-serve-autoscaling-async-inference-custom-routing)
40. [Using Kubernetes — vLLM documentation](https://docs.vllm.ai/en/stable/deployment/k8s/)
41. [Scalable LLMs With vLLM on Kubernetes — DZone](https://dzone.com/articles/vllm-kubernetes-scalable-llm-infrastructure)
42. [vLLM Production Deployment: Building High-Throughput Inference Serving Architecture — Introl Blog](https://introl.com/blog/vllm-production-deployment-inference-serving-architecture)
43. [vLLM Router: A High-Performance and Prefill/Decode Aware Load Balancer — vLLM Blog](https://blog.vllm.ai/2025/12/13/vllm-router-release.html)
44. [Disaggregated Prefilling — vLLM documentation](https://docs.vllm.ai/en/latest/features/disagg_prefill/)
45. [llm-d: Kubernetes-native distributed inferencing — Red Hat Developer](https://developers.redhat.com/articles/2025/05/20/llm-d-kubernetes-native-distributed-inferencing/)
46. [How to deploy and benchmark vLLM with GuideLLM on Kubernetes — Red Hat Developer](https://developers.redhat.com/articles/2025/12/24/how-deploy-and-benchmark-vllm-guidellm-kubernetes)
47. [vLLM vs Ollama vs llama.cpp vs TGI vs TensorRT-LLM: 2025 Guide — ITECS](https://itecsonline.com/post/vllm-vs-ollama-vs-llama.cpp-vs-tgi-vs-tensort)
48. [Compute and Autoscaling — Amazon EKS Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html)
49. [Karpenter — Amazon EKS Best Practices Guides](https://aws.github.io/aws-eks-best-practices/karpenter/)
50. [Scalable and Cost-Effective Event-Driven Workloads with KEDA and Karpenter on Amazon EKS — AWS](https://aws.amazon.com/blogs/containers/scalable-and-cost-effective-event-driven-workloads-with-keda-and-karpenter-on-amazon-eks/)
51. [Scale to zero GPUs with OpenFaaS, Karpenter and AWS EKS — OpenFaaS](https://www.openfaas.com/blog/scale-to-zero-gpus/)
52. [A Complete Guide to Karpenter — DevZero](https://www.devzero.io/blog/karpenter-guide)
53. [Overview of Node Auto-Provisioning (NAP) in Azure Kubernetes Service — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/node-auto-provisioning)
54. [Azure AKS goes just-in-time on nodes (Powered by Karpenter) — Medium](https://medium.com/h7w/azure-aks-goes-just-in-time-on-nodes-powered-by-karpenter-927957d0821c)
55. [Fully Managed GPU workloads with Azure Linux on AKS — AKS Engineering Blog](https://blog.aks.azure.com/2025/11/18/azure-linux-gpu-on-aks)
56. [Deploy GPU workloads in Autopilot — GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)
57. [Run GPU workloads on GKE Autopilot — Google Cloud Blog](https://cloud.google.com/blog/products/containers-kubernetes/run-gpu-workloads-on-gke-autopilot)
58. [About GPUs in Google Kubernetes Engine (GKE) — GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
59. [Amazon EC2 Spot Instances Pricing — AWS](https://aws.amazon.com/ec2/spot/pricing/)
60. [Pricing and usage model updates for Amazon EC2 instances accelerated by NVIDIA GPUs — AWS](https://aws.amazon.com/about-aws/whats-new/2025/06/pricing-usage-model-ec2-instances-nvidia-gpus/)
61. [Scaling Safely with Azure AKS Spot Node Pools — AKS Engineering Blog](https://blog.aks.azure.com/2025/07/17/Scaling-safely-with-spot-on-aks)
62. [Spot VMs — Google Kubernetes Engine documentation](https://cloud.google.com/kubernetes-engine/docs/concepts/spot-vms)
63. [Kubernetes GPU Optimization for Real-Time AI Inference — ScaleOps](https://scaleops.com/blog/ai-infra-for-production-why-gpu-resource-management-in-kubernetes-demands-a-new-approach/)
64. [Spot Instances in Kubernetes: Architecture & Cost Guide — Sedai](https://sedai.io/blog/spot-instances-in-k8s-strategy)
65. [CNCF Launches Kubernetes AI Conformance Program — CNCF](https://www.cncf.io/announcements/2025/11/11/cncf-launches-certified-kubernetes-ai-conformance-program-to-standardize-ai-workloads-on-kubernetes/)
66. [KubeCon 2025: CNCF to Standardize AI Workloads — Intellyx](https://intellyx.com/2025/11/18/kubecon-2025-cncf-to-standardize-ai-workloads/)
67. [GitHub — cncf/k8s-ai-conformance](https://github.com/cncf/k8s-ai-conformance)
68. [AI Conformant Azure Kubernetes Service (AKS) clusters — AKS Engineering Blog](https://blog.aks.azure.com/2025/12/05/kubernetes-ai-conformance-aks)
69. [Is GPU Serverless inferencing for custom LLM models? — AWS re:Post](https://repost.aws/questions/QUlHAbaJiIRt-eem9gizSmOQ/is-gpu-serverless-inferencing-for-custom-llm-models)
70. [Why Kubernetes is Great for Running AI/MLOps Workloads — Cloud Native Now](https://cloudnativenow.com/contributed-content/why-kubernetes-is-great-for-running-ai-mlops-workloads/)
71. [Running AI/ML on Kubernetes: From Prototype to Production — DZone](https://dzone.com/articles/ai-ml-kubernetes-mlflow-kserve-vllm)
72. [AWS GPU Pricing Explained — TRG Datacenters](https://www.trgdatacenters.com/resource/aws-gpu-pricing/)
73. [GPU sharing on Amazon EKS with NVIDIA time-slicing — AWS Containers Blog](https://aws.amazon.com/blogs/containers/gpu-sharing-on-amazon-eks-with-nvidia-time-slicing-and-accelerated-ec2-instances/)
74. [Use GPUs on Azure Kubernetes Service (AKS) — Microsoft Learn](https://learn.microsoft.com/en-us/azure/aks/use-nvidia-gpu)
75. [Run GPUs in GKE Standard node pools — Google Cloud documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus)
