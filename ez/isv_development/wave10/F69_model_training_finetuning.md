# F69 — Model Training, Fine-Tuning & Experiment Tracking: On-Premises

**Research Agent:** F69
**Scope:** On-premises model training, fine-tuning approaches, experiment tracking, data pipelines, model registry, hyperparameter optimization, and cost comparison to managed cloud training services.
**Date:** 2026-02-19

---

## Executive Summary

On-premises model training delivers maximum data sovereignty and, at sustained high GPU utilization, the lowest per-GPU-hour cost of any deployment model — but it imposes the heaviest operational burden of all three deployment options. Full fine-tuning of a 70B-parameter model requires approximately 672 GB of GPU VRAM in FP16 and can cost $50,000 or more in hardware for a single training run; parameter-efficient techniques such as QLoRA reduce this to as little as 46 GB, making on-premises fine-tuning accessible at smaller hardware scales. The complete MLOps stack — covering experiment tracking, data labeling pipelines, model registry, hyperparameter search, and distributed training orchestration — requires coordinated deployment of five to eight discrete open-source systems, each with its own operational surface area. Managed cloud training services (SageMaker, Vertex AI, Azure ML) eliminate all infrastructure management in exchange for significantly higher per-job costs and vendor lock-in. For an ISV serving enterprise customers with strict data residency requirements, on-premises fine-tuning is viable but demands a minimum of 2–4 dedicated MLOps FTEs and a clear hardware lifecycle plan spanning three to five years.

---

## 1. Fine-Tuning Approaches: Compute Requirements and Trade-offs

### 1.1 Full Fine-Tuning

Full fine-tuning updates all model parameters and requires storing model weights, gradients, optimizer states, and activations simultaneously. A rule of thumb of approximately 16 GB of VRAM per 1 billion parameters applies:

| Model Size | Full Fine-Tuning VRAM (FP16) | Minimum Hardware |
|------------|------------------------------|------------------|
| 7B         | ~67 GB                       | 2× A100 40 GB or 1× A100 80 GB |
| 14B        | ~134 GB                      | 2× A100 80 GB |
| 70B        | ~672 GB                      | 8× A100 80 GB (NVLink) |

[FACT] Full fine-tuning of a 7B model requires "100–120 GB of VRAM—roughly $50,000 worth of H100 GPUs for a single training run."
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

[FACT] A 70B parameter model requires eight A100 80 GB GPUs interconnected via NVLink for full fine-tuning.
URL: https://www.runpod.io/blog/llm-fine-tuning-gpu-guide

[FACT] Gradient checkpointing reduces VRAM by up to 50% at the cost of adding 20–30% additional training time.
URL: https://www.runpod.io/blog/llm-fine-tuning-gpu-guide

[FACT] Flash attention saves an additional 10–20% of VRAM during training.
URL: https://www.runpod.io/blog/llm-fine-tuning-gpu-guide

**Training duration (indicative, without citation — [UNVERIFIED]):** A 7B model full fine-tune on a single A100 80 GB can complete in under one day; a 70B model on 8× A100 may require multiple days to weeks depending on dataset size and epochs. No 2025 source with precise duration benchmarks was located for on-premises hardware.

### 1.2 LoRA (Low-Rank Adaptation)

LoRA inserts trainable low-rank matrices into frozen model layers, dramatically reducing the number of trainable parameters while recovering 90–95% of full fine-tuning quality.

| Model Size | LoRA VRAM (FP16) | Minimum Hardware |
|------------|------------------|------------------|
| 7B         | ~15 GB           | RTX 4090 24 GB |
| 14B        | ~30 GB           | 2× RTX 4090 or A100 40 GB |
| 70B        | ~146 GB          | 2× A100 80 GB or 2× H100 80 GB |

[FACT] LoRA configuration uses a trainable rank (r) typically set between 8 and 64, and produces "zero latency compared to the original model" during inference via weight merging.
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

[FACT] LoRA quality recovery is 90–95% compared to full fine-tuning.
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

### 1.3 QLoRA (Quantized LoRA)

QLoRA combines 4-bit quantization of the frozen base model with LoRA adapters, achieving the largest memory reduction of any PEFT approach.

| Model Size | QLoRA 8-bit VRAM | QLoRA 4-bit VRAM | Minimum Hardware (4-bit) |
|------------|------------------|------------------|--------------------------|
| 7B         | ~9 GB            | ~5 GB            | RTX 3090 24 GB |
| 14B        | ~18 GB           | ~10 GB           | RTX 4090 24 GB |
| 70B        | ~88 GB           | ~46 GB           | A100 80 GB |

[FACT] QLoRA uses "4-bit NormalFloat (NF4) format, reducing memory by 75% versus 16-bit."
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

[FACT] QLoRA paged optimizers prevent out-of-memory errors during training.
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

[FACT] QLoRA quality recovery is 80–90% compared to full fine-tuning.
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

[FACT] QLoRA enables fine-tuning of the same 7B model on a "$1,500 RTX 4090."
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

### 1.4 RLHF and DPO

Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) add alignment layers on top of a supervised fine-tuned base model.

[FACT] "RLHF training spends 80% of compute time on sample generation," making throughput optimization the primary infrastructure challenge for language model alignment.
URL: https://introl.com/blog/reinforcement-learning-infrastructure-rlhf-robotics-gpu-clusters-2025

[FACT] Full-scale RLHF at 70B requires four concurrent models (Actor, Reward, Reference, Critic). A 70B Actor plus 70B Reference model plus separate Reward and Critic models requires "8–16 H100 GPUs just for model weights" before accounting for optimizer states and activations.
URL: https://introl.com/blog/reinforcement-learning-infrastructure-rlhf-robotics-gpu-clusters-2025

[FACT] OpenRLHF is the first high-performance open-source framework enabling 70B+ parameter RLHF training, separating Actor, Reward, Reference, and Critic models across different GPUs using Ray distributed task scheduler and vLLM acceleration.
URL: https://github.com/OpenRLHF/OpenRLHF

[FACT] Online DPO training at scale used 8 H100 GPUs for 100,000 episodes.
URL: https://introl.com/blog/reinforcement-learning-infrastructure-rlhf-robotics-gpu-clusters-2025

[FACT] DPO "simplifies the preference learning process by directly optimizing on preference pairs without requiring a separate reward model," making it significantly less compute-intensive than full PPO-based RLHF.
URL: https://www.philschmid.de/rl-with-llms-in-2025-dpo

[FACT] For consumer-scale DPO, consumer GPUs with 24 GB+ such as RTX 4090 or A10G are viable for models up to approximately 7B parameters.
URL: https://www.philschmid.de/rl-with-llms-in-2025-dpo

**Production fine-tuning dataset baseline:** 10,000–50,000 examples; minimum viable: 1,000–5,000 high-quality examples.
URL: https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025

---

## 2. Training Infrastructure: Multi-GPU and Multi-Node

### 2.1 DeepSpeed ZeRO Optimization

[FACT] DeepSpeed's ZeRO-2 "reduces memory by up to 8x relative to the state-of-art."
URL: https://www.deepspeed.ai/training/

[FACT] With standard data parallelism, GPU memory is exhausted at 1.4 billion parameters; DeepSpeed enables a single GPU to handle "models with up to 13 billion parameters" without model parallelism.
URL: https://www.deepspeed.ai/training/

[FACT] DeepSpeed's 1-bit Adam, 0/1 Adam, and 1-bit LAMB optimizers "reduce communication volume by up to 26x" while maintaining convergence efficiency comparable to standard Adam.
URL: https://www.deepspeed.ai/training/

[FACT] ZeRO-3 with ZeRO-Infinity can offload to CPU and NVMe memory, enabling models of arbitrary size to train on limited GPU VRAM.
URL: https://www.deepspeed.ai/tutorials/zero/

**ZeRO Stage Memory Partitioning:**

| Stage | What is Partitioned | Memory Formula (N GPUs) | Approx. Reduction |
|-------|---------------------|-------------------------|-------------------|
| Stage 1 | Optimizer states | 4P + 12P/N → 4P at large N | ~4× |
| Stage 2 | Optimizer states + gradients | 2P + (2P+12P)/N → 2P at large N | ~8× |
| Stage 3 | Optimizer states + gradients + parameters | 16P/N per device | Linear with N |

URL: https://www.deepspeed.ai/tutorials/zero/

### 2.2 FSDP (Fully Sharded Data Parallel)

[FACT] For multi-node training without InfiniBand, FSDP recommends the hybrid sharding strategy (HYBRID_SHARD), treating the within-node NVLink fabric as the high-bandwidth ring and only crossing node boundaries for necessary communication.
URL: https://sumanthrh.com/post/distributed-and-efficient-finetuning/

[FACT] For DeepSpeed without InfiniBand, ZeRO++ with hierarchical partitioning (hpZ) is the recommended configuration to minimize cross-node all-reduce traffic.
URL: https://sumanthrh.com/post/distributed-and-efficient-finetuning/

### 2.3 NCCL and Networking

[FACT] NCCL (NVIDIA Collective Communications Library) supports InfiniBand verbs API instead of sockets and uses GPU Direct RDMA to reach 11 GB/s with an IB EDR or RoCE 100 GbE adapter.
URL: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html

[FACT] DGX2 machines with 8 InfiniBand/RoCE cards achieve transfer rates of 82 GB/s, maintaining consistency with internal NVLink bandwidth.
URL: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html

[FACT] A good result for all_reduce_perf NCCL benchmarks shows bandwidth around "92% of the theoretical maximum of the fabric, such as around 370 GB/s on a 400 GB/s fabric."
URL: https://www.together.ai/blog/a-practitioners-guide-to-testing-and-running-large-gpu-clusters-for-training-generative-ai-models

[FACT] NCCL 2.27 adds SHARP (Scalable Hierarchical Aggregation and Reduction Protocol) support for both NVLink and InfiniBand fabrics, "offloading compute-intensive tasks and improving scalability and performance at the 1,000 GPU level and beyond."
URL: https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/

[FACT] NVLink offers 5–10× higher bandwidth than inter-node communication via InfiniBand or Ethernet.
URL: https://sumanthrh.com/post/distributed-and-efficient-finetuning/

**Multi-node networking minimum requirements for on-premises:**
- Intra-node: NVLink (provided by GPU hardware)
- Inter-node: InfiniBand HDR (200 Gb/s) or HDR100 (100 Gb/s) strongly recommended; RoCE 100 GbE viable with NCCL tuning; standard 25/40 GbE Ethernet introduces significant bottlenecks for all-reduce at scale

URL: https://greennode.ai/blog/distributed-training-for-llm

---

## 3. Experiment Tracking: Self-Hosted Platforms

### 3.1 MLflow

[FACT] As of MLflow 3.7.0, "the default tracking backend has changed from file-based storage to SQLite database for better performance and reliability."
URL: https://mlflow.org/docs/latest/self-hosting/

[FACT] MLflow self-hosting deployment options include: command-line server (personal/small team), Docker Compose with PostgreSQL and MinIO, Kubernetes via Bitnami or Community Helm charts, and managed cloud services.
URL: https://mlflow.org/docs/latest/self-hosting/

[FACT] MLflow 3.0 extended its model registry to "handle generative AI applications and AI agents, connecting models to exact code versions, prompt configurations, evaluation runs, and deployment metadata."
URL: https://mlflow.org/docs/latest/ml/model-registry/

[FACT] Multi-tenant production deployments require a SQL database backend; SQLite is not sufficient for multi-user workspace-level permissions.
URL: https://mlflow.org/docs/latest/self-hosting/

**MLflow Self-Hosted Infrastructure Components:**
- Tracking server: FastAPI process (lightweight, ~512 MB RAM)
- Backend store: PostgreSQL (recommended for production)
- Artifact store: MinIO (self-hosted S3-compatible) or network file system
- Optional: NGINX reverse proxy for TLS termination and authentication

### 3.2 Weights & Biases (Self-Managed)

[FACT] W&B self-managed on-premises deployment requires: "Kubernetes cluster," "MySQL 8 database cluster," "Amazon S3-compatible object storage," and "Redis cache cluster."
URL: https://docs.wandb.ai/platform/hosting/hosting-options/self-managed

[FACT] W&B self-managed includes enterprise features: HIPAA-compliant options, secure private connectivity, customer-managed encryption key, Single Sign On (SSO), automated user provisioning, custom roles, audit logs, and enterprise support.
URL: https://docs.wandb.ai/platform/hosting/hosting-options/self-managed

[FACT] W&B Server releases are "supported for 12 months from their initial release date," and customers using self-managed are "responsible to upgrade to a supported release in time to maintain support."
URL: https://github.com/wandb/server

[FACT] W&B provides Terraform scripts for deploying on AWS, GCP, and Azure; on-premises Kubernetes deployments use the same infrastructure components.
URL: https://docs.wandb.ai/platform/hosting/hosting-options/self-managed

### 3.3 ClearML

[FACT] ClearML self-hosted server can be deployed via Docker Compose, AWS EC2 AMI, or Kubernetes, and stores "experiment, model, and workflow data."
URL: https://github.com/clearml/clearml-server

[FACT] ClearML's Infrastructure Control Plane allows connecting and managing GPU clusters "whether on-premises, in the cloud, or both," with built-in security features including multi-tenancy, role-based access control, and billing.
URL: https://clear.ml/why-clearml

[FACT] ClearML captures "every aspect of your ML workflow automatically, including code changes, hyperparameters, datasets, and model artifacts without requiring code modifications."
URL: https://tutorialswithai.com/tools/clearml/

---

## 4. Data Pipeline for Training: Labeling and Preprocessing

### 4.1 Label Studio

[FACT] Label Studio is a flexible data labeling tool supporting "computer vision, natural language processing, speech, voice, and video models."
URL: https://labelstud.io/

[FACT] Label Studio's REST API enables integration into ML pipelines, and its machine learning backend allows automatic pre-labeling of data using models during active learning workflows.
URL: https://labelstud.io/guide/ml.html

[FACT] Label Studio supports online learning — "retrain your model while new annotations are being created."
URL: https://labelstud.io/guide/ml.html

**Self-hosted deployment:** Docker image available; no GPU required for the labeling UI; backend database (PostgreSQL recommended for production) and object storage for media assets are the primary infrastructure requirements.

### 4.2 Argilla

[FACT] Argilla is "an open-source data labeling tool for highly efficient human-in-the-loop and MLOps workflows, composed of a server and web app for data labeling and curation, and a Python library for building data annotation workflows."
URL: https://github.com/argilla-io/argilla

[FACT] Argilla v2 self-hosted deployment uses Docker: `docker run -d --name argilla -p 6900:6900 argilla/argilla-quickstart:latest`.
URL: https://easypanel.io/docs/templates/argilla

[FACT] Argilla 2.4 enables building fine-tuning and evaluation datasets on HuggingFace Hub with no code required, supporting hybrid on-premises/cloud workflows.
URL: https://huggingface.co/blog/argilla-ui-hub

**Data pipeline storage requirement note:** Training datasets for LLMs can range from a few GB (domain-specific fine-tuning) to hundreds of GB (instruction tuning). Shared NFS or object storage (MinIO) accessible by both labeling tools and training nodes is required for cohesive pipeline operation [UNVERIFIED — no 2025 source specifying exact storage requirements for combined pipelines was located; this reflects standard MLOps architecture practice].

---

## 5. Model Registry: Versioning, Promotion, and Rollback

[FACT] "LLMs with hundreds of GB weights require specialized infrastructure beyond Git." Traditional version control cannot efficiently handle model artifacts ranging from megabytes for classical ML to hundreds of gigabytes for large language models.
URL: https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025

[FACT] MLflow Model Registry provides "lineage (i.e., which MLflow experiment and run produced the model), versioning, aliasing, metadata tagging and annotation support" to ensure full spectrum tracking from development to production.
URL: https://mlflow.org/docs/latest/ml/model-registry/

[FACT] If running a self-hosted MLflow server, organizations "must use a database-backed backend store in order to access the model registry via the UI or API."
URL: https://mlflow.org/docs/latest/ml/model-registry/

[FACT] Self-hosted model registry rollback: "If monitoring detects a sharp degradation in latency or a sudden drop in prediction confidence (e.g., data drift is detected), the system automatically kills the new model deployment and reverts all traffic to the last stable, archived model version."
URL: https://www.aiforzero.space/2025/10/model-versioning-and-registry-mlops.html

**Recommended storage tiering for model registry:**
- Hot storage: Recent and actively deployed versions (NVMe SSD or SAN)
- Warm storage: Historical versions and staging candidates (HDD or object storage)
- Cold storage: Archived models with compliance retention requirements (object storage with lifecycle policies)

URL: https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025

**Beyond weights — LLM-specific registry requirements:**
On-premises model registries must version: base model selection, fine-tuned weights and LoRA adapters, prompt templates and system instructions, and RAG configurations including embedding models and retrieval parameters.
URL: https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025

---

## 6. Hyperparameter Optimization: Optuna and Ray Tune

[FACT] Optuna 4.7.0 is the latest release as of January 19, 2026, with recent updates including AutoSampler for Multi-Objective and Constrained Optimization and Gaussian Process-Based Sampler capabilities.
URL: https://optuna.org/

[FACT] Ray Tune "offers great parallelization and scalability across clusters of hundreds of machines" and "takes your training function and automatically parallelizes it, takes care of the resource management, and can even distribute it across a cluster of machines."
URL: https://docs.ray.io/en/latest/tune/index.html

[FACT] In Ray Tune, a scheduler decides which trials to pause, stop, or boost with more resources; in Optuna, pruners perform the analogous early-stopping of weak trials.
URL: https://medium.com/optuna/scaling-up-optuna-with-ray-tune-88f6ca87b8c7

[FACT] Recent research enhanced Ray Tune with an Automatic Heterogeneous Resource Allocation Strategy that "dynamically adapts resource distribution based on Node configurations, optimizing utilization while reducing manual setup complexity."
URL: https://link.springer.com/article/10.1007/s11227-025-07798-3

**On-premises scheduling integration:** Ray Tune integrates with Kubernetes (via KubeRay) and SLURM schedulers for on-premises cluster job queuing. Optuna integrates with any compute backend including Ray and can persist study state to PostgreSQL for distributed trial execution [UNVERIFIED — integration specifics cited from general documentation, no 2025-specific on-premises deployment case study was located].

---

## 7. Cost and Time: On-Premises vs. Cloud Training

### 7.1 On-Premises Total Cost of Ownership

[FACT] "High-performance GPUs like NVIDIA A100/H100 can cost $25,000–$40,000 each."
URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs

[FACT] A concrete TCO example for a deployment requiring 1 billion inferences monthly on 8× H100 hardware:

| Cost Category | Monthly Amount |
|---------------|----------------|
| Hardware depreciation (8× H100, 3-year amortization) | ~$9,000 |
| Electricity | ~$4,000 |
| MLOps staff (team of 3) | ~$60,000 |
| Networking, cooling, maintenance | ~$10,000 |
| **Total Monthly** | **~$83,000** |

URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs

[FACT] "A single 8× H100 server can consume over 3 kW," and "running GPUs 24/7 can add six-figure annual electricity costs."
URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs

[FACT] Hardware maintenance budget: "Budget at least 10–15% annually for repairs and upgrades."
URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs

[FACT] "Over the long term, salaries often outstrip infrastructure costs, making people the single largest line item in TCO."
URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs

[FACT] For a modest on-premises setup, "2–3 engineers handling DevOps, MLOps, and security may be sufficient, while an enterprise-scale deployment can require 10+ AI-ops staff with annual payroll exceeding infrastructure spend in many regions."
URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs

[FACT] "On-premises is a fit when workloads are steady and tied to multi-year research or product development, with consistent utilization over two to three years making owned hardware cheaper than cloud."
URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs

### 7.2 Cloud Training Service Pricing (Indicative)

**Training cost ranges by model size (cloud GPU, general market):**

| Model Scale | GPU Config | Approx. Duration | Estimated Cloud Cost Range |
|-------------|------------|------------------|---------------------------|
| Small (1–7B) | 1–2× H100 | 10–50 hours | $50–$500 |
| Medium (13–30B) | 4× H100 | 50–200 hours | $500–$3,000 |
| Large (70B+) | 8× H100 | 300–1,000 hours | $10,000–$50,000 |

URL: https://www.crowdee.com/blog/posts/self-hosting-ai-costs (for H100 hourly rates)

**AWS SageMaker Training — Key Instance Pricing:**

[FACT] SageMaker ml.p4d.24xlarge (8× A100 40 GB): $37.688 per hour on-demand.
URL: https://calculator.holori.com/aws/sagemaker/ml.p5.48xlarge

[FACT] SageMaker ml.p5.48xlarge (8× H100 80 GB): starting at $63.296 per hour on-demand.
URL: https://calculator.holori.com/aws/sagemaker/ml.p5.48xlarge-training

[FACT] SageMaker Machine Learning Savings Plans "can save you up to 64% off SageMaker ML On-Demand pricing."
URL: https://www.nops.io/blog/sagemaker-pricing-the-essential-guide/

**Vertex AI Training — Key GPU Pricing:**

[FACT] Vertex AI custom training on A100 GPUs costs approximately $2.93 per GPU per hour.
URL: https://cloud.google.com/vertex-ai/pricing

[FACT] Vertex AI billing operates "in 30-second increments rather than full-hour blocks."
URL: https://www.pump.co/blog/google-vertex-ai-pricing

[FACT] "Vertex's AutoML reduces tuning cycles by 40%" compared to manual hyperparameter optimization.
URL: https://medium.com/@darkmatter4real/fine-tuning-llms-google-vertex-ai-vs-open-source-models-on-gke-53830c2c0ef3

**Azure ML Training — Key GPU Pricing:**

[FACT] Azure NC24ads A100 v4 (single A100) on-demand: $3.673 per hour; spot: $0.920 per hour.
URL: https://instances.vantage.sh/azure/vm/nc24ads-v4

[FACT] Azure ML compute carries "no additional charge" beyond the underlying Azure VM cost, but separate charges apply for Azure Blob Storage, Azure Key Vault, Azure Container Registry, and Azure Application Insights.
URL: https://azure.microsoft.com/en-us/pricing/details/machine-learning/

---

## 8. Operational Comparison: On-Premises vs. Managed Training Services

### 8.1 What Disappears with Managed Training

Managed cloud training services (SageMaker Training, Vertex AI Training, Azure ML) eliminate the following operational burdens that are present in on-premises environments:

| Operational Layer | On-Premises Burden | SageMaker / Vertex AI / Azure ML |
|-------------------|--------------------|----------------------------------|
| GPU hardware procurement | Full responsibility | None — pay per job |
| CUDA/driver version management | Manual patching | Managed container registry |
| Multi-node networking (NCCL, IB) | Physical cabling + config | Managed fabric |
| Cluster autoscaling | Custom scheduler (SLURM, K8s) | Native autoscaling |
| Spot/preemptible recovery | Manual checkpoint + restart | Built-in spot retry |
| Experiment tracking integration | Deploy MLflow/W&B separately | Integrated UI (SageMaker Studio, Vertex Experiments) |
| Model registry | Deploy MLflow Registry | Native registries with CI/CD hooks |
| Data pipeline tooling | Deploy Label Studio, Argilla separately | Managed labeling (SageMaker Ground Truth) |
| Cost attribution per job | Custom tagging/accounting | Per-job billing built-in |

[FACT] Vertex AI supports "supervised fine-tuning on open models such as Llama 3.1" via its managed OSS tuning service.
URL: https://discuss.google.dev/t/from-research-to-production-a-first-look-at-oss-managed-tuning-on-vertex-ai/258166

[FACT] Organizations including LeBonCoin "reported 30–40% savings after migrating their machine learning workloads from SageMaker to Kubernetes-based EKS," indicating that Managed Kubernetes occupies a middle-cost position between fully managed and on-premises.
URL: https://www.truefoundry.com/blog/cost-comparison-with-sagemaker

[FACT] Vertex AI managed training introduces limitations including "limited control over quantization, pruning, or gradient strategies" and "proprietary checkpoints incompatible with open-source frameworks."
URL: https://medium.com/@darkmatter4real/fine-tuning-llms-google-vertex-ai-vs-open-source-models-on-gke-53830c2c0ef3

[FACT] Self-hosted GKE (vs. Vertex AI managed training) allows "implementing cutting-edge methods (e.g., DoRA)" and provides "full access to gradients, layer outputs, and training logs for compliance."
URL: https://medium.com/@darkmatter4real/fine-tuning-llms-google-vertex-ai-vs-open-source-models-on-gke-53830c2c0ef3

---

## 9. Deployment Model Comparison Table

| Capability | On-Premises | Managed K8s (EKS/AKS/GKE) | Cloud-Native (SageMaker/Vertex AI/Azure ML) |
|------------|-------------|---------------------------|----------------------------------------------|
| **Fine-Tuning** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Full hardware + CUDA + networking control | Self-managed GPU nodes + FSDP/DeepSpeed | Managed containers, auto-scaling, per-job billing |
| | DeepSpeed, FSDP, Megatron | KubeRay, DeepSpeed on K8s | SageMaker Training Jobs, Vertex AI Custom Training |
| | Est. FTE: 2.0–4.0 | Est. FTE: 1.0–2.0 | Est. FTE: 0.25–0.5 |
| **Experiment Tracking** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-deploy MLflow/W&B/ClearML; manage DB + artifact storage | Helm-deployed MLflow; shared object storage | Native (SageMaker Experiments, Vertex Experiments, Azure ML Studio) |
| | MLflow, W&B self-managed, ClearML | MLflow on K8s, W&B self-managed | Built-in experiment logging APIs |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **Data Labeling Pipeline** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-deploy Label Studio/Argilla; manage storage + user access | Containerized labeling tools; K8s RBAC | SageMaker Ground Truth; Vertex Data Labeling |
| | Label Studio, Argilla | Label Studio on K8s | SageMaker Ground Truth |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Model Registry** | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | MLflow Registry with PostgreSQL backend; NFS/MinIO artifact store | MLflow or DVC on K8s; cloud object storage | Native model registries with CI/CD integration |
| | MLflow Registry, DVC | MLflow on K8s | SageMaker Model Registry, Vertex AI Model Registry |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0–0.1 |
| **Hyperparameter Optimization** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | SLURM or custom scheduler; manual GPU queue management | KubeRay for Ray Tune; K8s resource quotas | SageMaker Hyperparameter Tuning, Vertex AI Neural Architecture Search |
| | Optuna, Ray Tune + SLURM | Ray Tune + KubeRay | SageMaker HPO, Vertex AI AutoML |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |

**FTE assumptions:** Mid-size ISV deployment serving 50 enterprise customers, 3–5 fine-tuning runs per month, models in the 7B–70B range. On-call burden estimated at an additional 0.25 FTE per major infrastructure component in the on-premises model. [UNVERIFIED — specific FTE ranges are estimates based on available benchmark data; no 2025 Gartner or Forrester report providing ISV-specific MLOps staffing norms was located].

---

## 10. Key Takeaways

- **QLoRA changes the hardware calculus:** 4-bit QLoRA reduces VRAM requirements by ~75% versus FP16 LoRA, enabling 7B-class model fine-tuning on a single $1,500 consumer GPU and 70B-class fine-tuning on a single A100 80 GB — the primary barrier to on-premises fine-tuning is no longer necessarily hardware cost but operational complexity.

- **Multi-node training demands InfiniBand or equivalent:** Inter-node all-reduce communication is the critical bottleneck for distributed training; without IB HDR (200 Gb/s) or at minimum RoCE 100 GbE with NCCL tuning, multi-node training throughput degrades severely. Standard Ethernet is not viable for production multi-node LLM training.

- **People cost dominates TCO at scale:** For a 3-person MLOps team supporting on-premises training infrastructure, staffing alone costs approximately $60,000/month — dwarfing hardware depreciation (~$9,000/month for 8× H100). This relationship makes cloud training economically competitive for ISVs with unpredictable or bursty training workloads.

- **Self-hosted MLOps requires five to eight discrete systems:** A complete on-premises training stack requires independently deployed and maintained components for experiment tracking, model registry, data labeling, hyperparameter optimization, distributed training coordination, artifact storage, and authentication. Each system has its own upgrade cadence, failure surface, and operational dependency chain.

- **Managed training trades flexibility for speed and simplicity:** Cloud-native training services (SageMaker ml.p5.48xlarge at $63.30/hr, Vertex AI A100 at $2.93/GPU-hr) eliminate networking, scheduling, and tooling burdens but introduce proprietary checkpoint formats, limited access to low-level gradient control, and higher marginal cost per training hour. For compliance-driven ISVs that cannot move training data to cloud, on-premises fine-tuning with QLoRA or LoRA adapters on pre-purchased A100/H100 hardware represents the most viable path, provided sustained GPU utilization exceeds approximately 50–60% to justify amortized hardware cost against cloud alternatives.

---

## Related — Out of Scope

- **GPU hardware procurement, pricing, and lifecycle planning** — covered by F39
- **Model inference and serving infrastructure** — covered by F36
- **RAG pipeline architecture and vector database selection** — covered by F35
- **Kubernetes cluster operations (EKS/AKS/GKE)** for Managed K8s deployment model — covered by other wave agents

---

## Sources

1. https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025 — Fine-Tuning Infrastructure: LoRA, QLoRA, and PEFT at Scale
2. https://www.runpod.io/blog/llm-fine-tuning-gpu-guide — The Complete Guide to GPU Requirements for LLM Fine-Tuning (RunPod)
3. https://introl.com/blog/reinforcement-learning-infrastructure-rlhf-robotics-gpu-clusters-2025 — Reinforcement Learning Infrastructure: GPU Clusters for RLHF
4. https://github.com/OpenRLHF/OpenRLHF — OpenRLHF GitHub Repository
5. https://www.philschmid.de/rl-with-llms-in-2025-dpo — How to align open LLMs in 2025 with DPO & synthetic data (Phil Schmid)
6. https://www.deepspeed.ai/training/ — DeepSpeed Training Overview and Features
7. https://www.deepspeed.ai/tutorials/zero/ — ZeRO Redundancy Optimizer (DeepSpeed)
8. https://sumanthrh.com/post/distributed-and-efficient-finetuning/ — Everything about Distributed Training and Efficient Finetuning
9. https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html — NCCL Overview (NVIDIA)
10. https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/ — Enabling Fast Inference and Resilient Training with NCCL 2.27
11. https://www.together.ai/blog/a-practitioners-guide-to-testing-and-running-large-gpu-clusters-for-training-generative-ai-models — A Practitioner's Guide to Testing and Running Large GPU Clusters
12. https://greennode.ai/blog/distributed-training-for-llm — Harnessing Distributed Training for LLMs with UCX on InfiniBand
13. https://mlflow.org/docs/latest/self-hosting/ — MLflow Self-Hosting Overview
14. https://mlflow.org/docs/latest/ml/model-registry/ — MLflow Model Registry
15. https://docs.wandb.ai/platform/hosting/hosting-options/self-managed — W&B Self-Managed Deployment Documentation
16. https://github.com/wandb/server — W&B Server GitHub Repository
17. https://github.com/clearml/clearml-server — ClearML Server GitHub Repository
18. https://clear.ml/why-clearml — ClearML Platform Overview
19. https://tutorialswithai.com/tools/clearml/ — ClearML MLOps Platform Review
20. https://labelstud.io/ — Label Studio Official Site
21. https://labelstud.io/guide/ml.html — Label Studio ML Pipeline Integration
22. https://github.com/argilla-io/argilla — Argilla GitHub Repository
23. https://easypanel.io/docs/templates/argilla — Argilla Self-Host on Easypanel
24. https://huggingface.co/blog/argilla-ui-hub — Argilla 2.4 Announcement
25. https://introl.com/blog/model-versioning-infrastructure-mlops-artifact-management-guide-2025 — Model Versioning Infrastructure: Managing ML Artifacts at Scale
26. https://www.aiforzero.space/2025/10/model-versioning-and-registry-mlops.html — Model Versioning and Registry: The MLOps Guide
27. https://optuna.org/ — Optuna Official Site
28. https://docs.ray.io/en/latest/tune/index.html — Ray Tune Documentation
29. https://medium.com/optuna/scaling-up-optuna-with-ray-tune-88f6ca87b8c7 — Scaling up Optuna with Ray Tune
30. https://link.springer.com/article/10.1007/s11227-025-07798-3 — Efficient Configuration of Heterogeneous Resources in Deep Learning Auto-Tuning Systems (Springer, 2025)
31. https://www.crowdee.com/blog/posts/self-hosting-ai-costs — The True Cost of Self-Hosting AI
32. https://calculator.holori.com/aws/sagemaker/ml.p5.48xlarge — SageMaker ml.p5.48xlarge Pricing (Holori)
33. https://calculator.holori.com/aws/sagemaker/ml.p5.48xlarge-training — SageMaker ml.p5.48xlarge Training Pricing (Holori)
34. https://www.nops.io/blog/sagemaker-pricing-the-essential-guide/ — SageMaker Pricing: The Essential Guide (nOps)
35. https://cloud.google.com/vertex-ai/pricing — Vertex AI Pricing (Google Cloud)
36. https://www.pump.co/blog/google-vertex-ai-pricing — Google Vertex AI Pricing Guide
37. https://instances.vantage.sh/azure/vm/nc24ads-v4 — Azure NC24ads A100 v4 Pricing (Vantage)
38. https://azure.microsoft.com/en-us/pricing/details/machine-learning/ — Azure Machine Learning Pricing
39. https://medium.com/@darkmatter4real/fine-tuning-llms-google-vertex-ai-vs-open-source-models-on-gke-53830c2c0ef3 — Fine-Tuning LLMs: Google Vertex AI vs. Open-Source Models on GKE
40. https://discuss.google.dev/t/from-research-to-production-a-first-look-at-oss-managed-tuning-on-vertex-ai/258166 — OSS Managed Tuning on Vertex AI (Google Developer Forums)
41. https://www.truefoundry.com/blog/cost-comparison-with-sagemaker — Cost Comparison with SageMaker (TrueFoundry)
