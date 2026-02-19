# F8: AWS Compute Services
**Research Agent:** F8 — AWS Compute Services
**Date:** 2026-02-18
**Scope:** AWS compute services only — Lambda, ECS/Fargate, App Runner, EC2 Auto Scaling, Inferentia/Trainium, GPU instances, AWS Batch

---

## Executive Summary

AWS offers a tiered spectrum of compute services that trade operational control for managed convenience, spanning from fully serverless (Lambda, App Runner) to increasingly self-directed tiers (ECS/Fargate, EC2 Auto Scaling, AWS Batch). For ISVs running AI-driven SaaS, AWS's custom silicon — Inferentia2 for inference and Trainium2/3 for training — provides a credible cost-reduction path of 30–50% versus equivalent NVIDIA GPU instances for compatible workloads, following AWS's June 2025 GPU price reductions of up to 45%. Lambda gained significant new capability in November 2025 with the launch of Managed Instances, enabling EC2-backed execution environments while preserving serverless operational simplicity. GPU instances (P5, G5, G6) remain the default for LLM inference and fine-tuning but come with high operational overhead and tight capacity constraints; spot pricing can reduce costs by 60–90% for fault-tolerant training workloads. AWS Batch acts as the glue service that makes large-scale, scheduled ML training and data processing jobs economically viable without custom orchestration.

---

## Section 1: AWS Lambda — Serverless Functions

### Overview

AWS Lambda is the foundational serverless compute service on AWS. Functions execute in isolated micro-VM environments ([Firecracker](https://aws.amazon.com/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/)). The developer deploys code; AWS manages all underlying servers, patching, scaling, and availability.

### Cold Start Characteristics

Lambda cold starts occur when a new execution environment must be initialized — downloading code, starting the runtime, and executing initialization logic outside the handler.

[STATISTIC] "For simple functions, this takes 100–200ms. For real-world applications with dependencies, VPC attachments, and complex initialization, you're looking at 1–5 seconds, sometimes more."
URL: [edgedelta.com — AWS Lambda Cold Starts in 2025](https://edgedelta.com/company/knowledge-center/aws-lambda-cold-start-cost)

By runtime, cold start latency varies materially:

| Runtime | Typical Cold Start Range |
|---------|-------------------------|
| Python, Node.js | 200–400 ms |
| Java, .NET | 500–700 ms (without SnapStart) |
| Java (SnapStart enabled) | Sub-100 ms snapshot restore |

Source: [zircon.tech — AWS Lambda Cold Start Optimization in 2025](https://zircon.tech/blog/aws-lambda-cold-start-optimization-in-2025-what-actually-works/)

[FACT] AWS began billing the INIT phase (cold start initialization time) the same as invocation duration beginning August 1, 2025. For functions with heavy startup logic, this shift can increase Lambda spend by 10–50%.
URL: [edgedelta.com — AWS Lambda Cold Starts in 2025](https://edgedelta.com/company/knowledge-center/aws-lambda-cold-start-cost)

**Mitigation options:**
- **Provisioned Concurrency:** Pre-initializes execution environments, eliminating cold starts. Cost is $0.0000041667 per GB-second. URL: [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/)
- **Lambda SnapStart (Java):** Snapshots and restores VM state to reduce Java cold starts to sub-100ms. URL: [AWS SnapStart Blog](https://aws.amazon.com/blogs/compute/optimizing-cold-start-performance-of-aws-lambda-using-advanced-priming-strategies-with-snapstart/)
- **Provisioned Concurrency scheduling via Application Auto Scaling:** Ramps provisioned concurrency on a schedule to avoid cold starts during predictable traffic spikes. URL: [AWS Lambda Provisioned Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

### Concurrency Limits

[FACT] By default, Lambda provides each AWS account a total concurrency limit of 1,000 concurrent executions across all functions in a region. AWS raises this automatically based on usage, and increases can be requested via support.
URL: [AWS Lambda Concurrency Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)

[FACT] Reserved concurrency sets both the maximum and minimum concurrent instances for a specific function. No other function can consume that reserved concurrency. There is no charge for configuring reserved concurrency.
URL: [AWS Lambda Reserved Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)

[FACT] "You can configure up to the unreserved account concurrency in your account, minus 100, with the remaining 100 units of concurrency reserved for functions that aren't using reserved concurrency."
URL: [AWS Lambda Concurrency Docs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)

### Pricing Model

| Pricing Dimension | Rate (US East, x86) |
|-------------------|---------------------|
| Requests | $0.20 per million (first 1M free/month) |
| Duration — first 6B GB-sec/month | $0.0000166667 per GB-second |
| Duration — next 9B GB-sec/month | $0.000015 per GB-second |
| Duration — over 15B GB-sec/month | $0.000013334 per GB-second |
| Duration (Graviton/Arm) — first 7.5B | $0.0000133334 per GB-second |
| Provisioned Concurrency | $0.0000041667 per GB-second |

Source: [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/) | Corroborated: [Wiz — AWS Lambda Cost Breakdown 2026](https://www.wiz.io/academy/cloud-cost/aws-lambda-cost-breakdown)

### GPU Support Status

[FACT] As of 2026, AWS Lambda does NOT natively support GPU acceleration. The Lambda execution environment is CPU-only. Maximum memory is 10 GB; maximum execution duration is 15 minutes.
URL: [AWS re:Post — GPU Serverless Inferencing](https://repost.aws/questions/QUlHAbaJiIRt-eem9gizSmOQ/is-gpu-serverless-inferencing-for-custom-llm-models) | Corroborated: [modal.com — Limitations of AWS Lambda for AI Workloads](https://modal.com/blog/aws-lambda-limitations-article)

[FACT] Lambda is suitable for CPU-based inference with lightweight models that complete within 15 minutes. For GPU-accelerated workloads, AWS directs customers to SageMaker, EC2, or ECS with GPU task definitions.
URL: [cyfuture.cloud — How Does AWS Lambda Support Machine Learning Inference](https://cyfuture.cloud/kb/cloud-providers-tools/how-does-aws-lambda-support-machine-learning-inference)

### Lambda Managed Instances (November 2025 — New)

[FACT] AWS announced Lambda Managed Instances at re:Invent 2025 (November 2025), a capability enabling Lambda functions to run on designated Amazon EC2 instances while maintaining serverless operational simplicity.
URL: [AWS Announcement — Lambda Managed Instances](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-managed-instances/) | [AWS Blog](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)

[FACT] Lambda Managed Instances allows each execution environment to process multiple concurrent requests (multi-concurrency per environment), reducing compute consumption compared to the traditional one-request-per-environment model.
URL: [AWS Blog — Lambda Managed Instances](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)

[FACT] Lambda Managed Instances provides access to EC2 commitment-based pricing: Compute Savings Plans and Reserved Instances, which can provide "up to a 72% discount over Amazon EC2 On-Demand pricing."
URL: [AWS Blog — Lambda Managed Instances](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)

[FACT] Lambda Managed Instances is available as of late 2025 in US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Tokyo), and Europe (Ireland). Supported runtimes: latest Java, Node.js, Python, and .NET.
URL: [AWS Blog — Lambda Managed Instances](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)

---

## Section 2: Amazon ECS + Fargate — Managed Container Orchestration

### Overview

Amazon Elastic Container Service (ECS) is AWS's fully managed container orchestration service. [FACT] "Amazon ECS is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications."
URL: [AWS ECS Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

AWS Fargate is the serverless compute engine for ECS (and EKS): the operator defines the container; Fargate provisions and manages the underlying EC2 fleet.

### Task Definitions

[FACT] "Amazon ECS allows you to define tasks through a JavaScript Object Notation (JSON) template called a Task Definition, where you can specify one or more containers, the Docker repository and image, memory and CPU requirements, shared data volumes, and how the containers are linked."
URL: [AWS ECS Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

Task definitions support:
- Up to 10 container definitions per task
- CPU and memory at task level and per-container level
- IAM task roles for per-task permissions isolation
- EFS volume mounts for persistent shared storage
- Secrets injection via AWS Secrets Manager and Parameter Store

### Service Auto-Scaling

[FACT] "Automatic scaling is the ability to increase or decrease the desired number of tasks in your Amazon ECS service automatically, and Amazon ECS leverages the Application Auto Scaling service to provide this functionality."
URL: [AWS ECS Auto Scaling Docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)

ECS supports four scaling policy types:

| Scaling Type | Trigger Mechanism |
|-------------|------------------|
| Target Tracking | Maintain a specific metric value (e.g., 70% CPU) |
| Step Scaling | Tiered response to CloudWatch alarm breach sizes |
| Scheduled Actions | Time-based scale up/down |
| Predictive Scaling | ML-driven, pattern-based pre-scaling |

Source: [AWS ECS Auto Scaling Docs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)

Available built-in metrics include ECSServiceAverageCPUUtilization, ECSServiceAverageMemoryUtilization, and ALBRequestCountPerTarget.

### Fargate Pricing

[FACT] Fargate charges per second with a one-minute minimum, based on vCPU and memory allocated to tasks.

| Dimension | US East (N. Virginia) Rate |
|-----------|---------------------------|
| vCPU | $0.04048 per vCPU-hour |
| Memory | $0.004445 per GB-hour |
| Ephemeral Storage (>20 GB) | $0.000111 per GB-hour |

Source: [AWS Fargate Pricing](https://aws.amazon.com/fargate/pricing/) | Corroborated: [cloudchipr.com — AWS Fargate Pricing Explained 2025](https://cloudchipr.com/blog/aws-fargate-pricing)

[FACT] Compute Savings Plans are available for Fargate, offering discounts in exchange for 1-year or 3-year usage commitments.
URL: [AWS Fargate Pricing](https://aws.amazon.com/fargate/pricing/)

### Operational Burden Eliminated by Fargate

With Fargate, AWS manages:
- EC2 instance provisioning, patching, and termination
- Kernel and OS-level security updates
- Container instance AMI management
- Bin-packing and placement decisions
- Node-level capacity reservations

The operator retains responsibility for:
- Container images (building, scanning, pushing to ECR)
- Task definitions and ECS service configurations
- IAM roles and security group rules
- Service discovery and load balancer integration
- VPC networking design

---

## Section 3: AWS App Runner — Source-to-URL Deployment

### Overview

[FACT] AWS App Runner is a fully managed service that enables developers to build and run containerized web applications and APIs directly from source code or a container image without infrastructure management knowledge.
URL: [AWS App Runner FAQs](https://aws.amazon.com/apprunner/faqs/)

App Runner's design philosophy: connect a GitHub repository or ECR image → App Runner handles the build pipeline, deployment, TLS certificate, load balancing, and scaling. The operator gets a URL with zero infrastructure configuration.

### Auto-Scaling Model

[FACT] "App Runner monitors the number of concurrent requests and automatically adds instances based on request volume, and scales down to a provisioned CPU-throttled instance when receiving no incoming requests."
URL: [AWS App Runner — Managing Autoscaling](https://docs.aws.amazon.com/apprunner/latest/dg/manage-autoscaling.html)

Auto-scaling configuration parameters:
- **Max concurrency:** Maximum concurrent requests per instance before a new instance is added
- **Max size:** Maximum number of instances
- **Min size:** Minimum number of provisioned (warm, memory-only billed) instances

[FACT] You can have up to 10 unique auto-scaling configuration names and up to 5 revisions for each configuration.
URL: [AWS App Runner Autoscaling API](https://docs.aws.amazon.com/apprunner/latest/api/API_AutoScalingConfiguration.html)

### Pricing

| State | vCPU | Memory |
|-------|------|--------|
| Active (processing requests) | $0.064/vCPU-hour | $0.007/GB-hour |
| Provisioned (idle, warming) | $0.00 | $0.007/GB-hour |
| Paused (fully stopped) | $0.00 | $0.00 |

Additional:
- Automatic deployments: $1.00/application/month
- Source code build minutes: $0.005/build-minute

Source: [AWS App Runner Pricing](https://aws.amazon.com/apprunner/pricing/)

### Limitations vs. ECS

| Dimension | App Runner | ECS + Fargate |
|-----------|-----------|---------------|
| Containers per service | 1 | Up to 10 per task |
| Scaling trigger | Concurrent requests only | CPU, memory, ALB RPS, custom metrics, schedule |
| Background/worker processes | Not suitable (CPU throttled at 0 requests) | Fully supported |
| Networking customization | VPC connector (limited) | Full VPC control |
| IAM granularity | Service-level only | Per-task IAM roles |
| GPU support | No | Yes (EC2 launch type) |
| Max configuration options | Limited | Extensive |

Sources: [AWS App Runner FAQs](https://aws.amazon.com/apprunner/faqs/) | [businesscompassllc.com — App Runner vs. ECS Fargate 2025](https://blogs.businesscompassllc.com/2025/06/aws-container-orchestration-app-runner.html) | [Medium — App Runner vs. ECS vs. Lambda](https://dashankadesilva.medium.com/aws-app-runner-vs-ecs-vs-lambda-choosing-the-right-compute-option-36915d355cd5)

[FACT] App Runner does not scale to zero. At minimum, one provisioned (memory-billed) instance remains warm.
URL: [cloudoptimo.com — AWS App Runner vs Elastic Beanstalk vs ECS](https://www.cloudoptimo.com/blog/aws-app-runner-vs-elastic-beanstalk-vs-ecs-when-to-use-each/)

**ISV guidance:** App Runner is appropriate for simple API services or web frontends where simplicity is valued over control. It is not appropriate for AI inference workloads, background ML processing, or any worker-type services that process queues rather than HTTP requests.

---

## Section 4: EC2 Auto Scaling — Launch Templates, Spot Instances, Predictive Scaling

### Launch Templates

[FACT] "Launch templates are recommended to access the latest features, and you must use a launch template to configure Auto Scaling groups that launch both Spot and On-Demand Instances or specify multiple instance types."
URL: [AWS EC2 Auto Scaling — Launch Templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)

Launch templates encode: AMI ID, instance type(s), key pair, security groups, IAM instance profile, user data scripts, EBS volume configurations, and placement group settings. They support versioning, enabling controlled rollouts of configuration changes.

### Spot Instances

[FACT] EC2 Spot Instances are available at discounts of up to 90% off On-Demand pricing. AWS Spot Instances for GPU workloads typically cost 60–70% less than On-Demand rates.
URL: [Amazon EC2 Spot Instances Pricing](https://aws.amazon.com/ec2/spot/pricing/)

Spot allocation strategies available in Auto Scaling groups:

| Strategy | Description |
|----------|-------------|
| `capacity-optimized` | Launches into most available pools using real-time capacity data |
| `price-capacity-optimized` | Balances price and capacity; recommended for new deployments |
| `lowest-price` | Maximizes savings; higher interruption risk |
| `diversified` | Spreads across all specified pools |

Source: [AWS EC2 Auto Scaling — Allocation Strategies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html)

[FACT] With launch templates, operators can provision capacity across multiple instance types using both Spot Instances and On-Demand Instances to achieve desired scale, performance, and cost optimization.
URL: [AWS EC2 Auto Scaling — Launch Templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)

[FACT] AWS introduced the ability to cancel pending instance refreshes (immediate rollback capability) into EC2 Auto Scaling in late 2025.
URL: [devclass.com — AWS debuts Lambda managed instances on EC2](https://devclass.com/2025/12/01/aws-debuts-lambda-managed-instances-on-ec2-more-control-lower-cost-for-high-volume-users/)

### Predictive Scaling

[FACT] "Predictive scaling uses machine learning to analyze traffic trends and anticipate capacity needs. By leveraging both historical and real-time data, it ensures EC2 instances are prepared to handle sudden demand spikes."
URL: [awsforengineers.com — Predictive Scaling for EC2 Auto Scaling](https://awsforengineers.com/blog/predictive-scaling-for-ec2-auto-scaling/)

[FACT] The forecasting engine looks at up to 14 days of historical CloudWatch metrics. Forecasts are updated every 6 hours using the latest CloudWatch data, maintaining a rolling 48-hour prediction window. Predictive scaling requires at least 24 hours of metric history before it can generate initial forecasts.
URL: [AWS EC2 Auto Scaling — Predictive Scaling Docs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

[FACT] Amazon EC2 Auto Scaling predictive scaling expanded to six additional regions in October 2025.
URL: [AWS — Predictive Scaling in Six More Regions](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-ec2-auto-scaling-predictive-scaling-in-six/)

Operating modes:
- **Forecast Only:** Generates predictions without triggering scaling; useful for validation before enabling
- **Forecast and Scale:** Actively pre-provisions capacity; does not scale in (requires dynamic policies for scale-in)

Source: [AWS EC2 Auto Scaling — Predictive Scaling Docs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

---

## Section 5: AWS Inferentia / Trainium — Custom AI Chips

### Overview

AWS has developed two custom silicon families for AI workloads:
- **AWS Inferentia** (inf1, inf2 instances): Optimized for high-throughput, low-latency model inference
- **AWS Trainium** (trn1, trn2, trn3 instances): Optimized for cost-efficient model training

Both chip families use the **AWS Neuron SDK**, which compiles and runs models on the custom hardware.

### Neuron SDK

[FACT] "Neuron enables developers to build, deploy and explore natively with PyTorch and JAX frameworks and with ML libraries such as HuggingFace, vLLM, PyTorch Lightning, and others without modifying your code."
URL: [AWS Neuron SDK](https://aws.amazon.com/ai/machine-learning/neuron/)

[FACT] Neuron SDK 2.26.0 supports PyTorch 2.8, JAX 0.6.2, and Python 3.11. Llama 4 variants and FLUX.1-dev image generation are in beta as of early 2026.
URL: [introl.com — Amazon Trainium and Inferentia 2025](https://introl.com/blog/aws-trainium-inferentia-silicon-ecosystem-guide-2025)

Supported model families include Llama, Mistral, Falcon, Stable Diffusion, Whisper, and BERT variants through the HuggingFace Optimum Neuron library.
URL: [HuggingFace — aws-neuron](https://huggingface.co/aws-neuron)

### Inferentia2 (Inf2 Instances)

[FACT] Inf2 instances are powered by up to 12 AWS Inferentia2 chips connected with ultra-high-speed NeuronLink, offering "up to 2.3 petaflops of compute, up to 384 GB of shared accelerator memory (32 GB HBM in every Inferentia2 chip) with 9.8 TB/s of total memory bandwidth."
URL: [Amazon EC2 Inf2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/)

[FACT] Inf2 delivers 3x higher compute performance, 4x larger total accelerator memory, up to 4x higher throughput, and up to 10x lower latency compared to Inf1 instances.
URL: [Amazon EC2 Inf2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/)

| Inf2 Instance | vCPUs | Memory | On-Demand Price |
|--------------|-------|--------|-----------------|
| inf2.xlarge | 4 | 16 GiB | $0.7582/hr |
| inf2.24xlarge | 96 | 384 GiB | $6.4906/hr |

Source: [Vantage — inf2.xlarge](https://instances.vantage.sh/aws/ec2/inf2.xlarge) | [Vantage — inf2.24xlarge](https://instances.vantage.sh/aws/ec2/inf2.24xlarge)

### Trainium2 and Trainium3

[FACT] Trainium2 instances (trn2.48xlarge) deliver H100-class performance at approximately $4.80/hr versus p5.48xlarge at approximately $9.80/hr — a 30–40% better price-performance ratio claimed by AWS.
URL: [zircon.tech — AWS AI Infrastructure Inferentia2 vs Trainium vs GPU](https://zircon.tech/blog/aws-ai-infrastructure-inferentia2-vs-trainium-vs-gpu-for-production-workloads/)

[FACT] AWS announced Trainium3 at re:Invent 2025 (December 2025). Trainium3 UltraServers became generally available at that time. Key specifications:
- 3nm fabrication process
- 2.52 petaflops of FP8 compute per chip
- 144 GB HBM3e memory per chip
- 4.9 TB/s memory bandwidth
- Up to 144 chips per integrated UltraServer system
- 362 FP8 petaflops total per UltraServer

URL: [AWS Announcement — EC2 Trn3 UltraServers](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/) | [TechCrunch — Trainium3](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/)

[FACT] Trainium3 delivers "4.4x more compute performance and 4x greater energy efficiency than Trainium2 UltraServers." Customers achieve "3x higher throughput per chip while delivering 4x faster response times, reducing training times from months to weeks."
URL: [interestingengineering.com — Amazon Trainium3 Chip](https://interestingengineering.com/innovation/amazon-new-trainium3-chip)

[FACT] Trainium4 (announced roadmap) will have "at least 3x the FP8 processing power and 4x more memory bandwidth than Trainium3" and will support Nvidia NVLink Fusion interconnect technology.
URL: [TechCrunch — Trainium3](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/)

### Cost vs. GPU Comparison

[FACT] AWS claims Inferentia2 achieves 40% better price-performance for inference. AWS claims up to 4x lower cost for inference compared to GPU instances for NLP and speech models.
URL: [AWS Blog — Navigating GPU Challenges: Cost Optimizing AI Workloads](https://aws.amazon.com/blogs/aws-cloud-financial-management/navigating-gpu-challenges-cost-optimizing-ai-workloads-on-aws/)

[FACT] "For enterprises running large-scale AI workloads on AWS, Trainium and Inferentia offer 30–50% cost reduction on compatible workloads."
URL: [cloudoptimo.com — AWS Custom ML Accelerators](https://www.cloudoptimo.com/blog/amazons-custom-ml-accelerators-aws-trainium-and-inferentia/)

**Ecosystem maturity caveat:** [FACT] "The ecosystem remains less mature than CUDA. Neuron SDK improvements in 2025 closed much of the gap, but NVIDIA's decades of software investment still provide advantages for complex or novel architectures."
URL: [zircon.tech — AWS AI Infrastructure Inferentia2 vs Trainium vs GPU](https://zircon.tech/blog/aws-ai-infrastructure-inferentia2-vs-trainium-vs-gpu-for-production-workloads/)

---

## Section 6: GPU Instances — P5, G5, G6

### Instance Family Overview

| Family | GPU | GPUs per Instance (max) | Key Use Case |
|--------|-----|------------------------|--------------|
| P5 | NVIDIA H100 (80 GB HBM3) | 8 | LLM training, HPC |
| G5 | NVIDIA A10G (24 GB) | 8 | Inference, graphics rendering |
| G6 | NVIDIA L4 (24 GB) | 8 | Inference, real-time graphics |
| G6e | NVIDIA L40S | Up to 8 | High-memory inference |

### P5 Instances (NVIDIA H100)

[FACT] P5 instances provide "up to 8 NVIDIA H100 GPUs with a total of up to 640 GB HBM3 GPU memory per instance." The p5.48xlarge includes 192 vCPUs, 2 TB of system memory, and 30 TB of local NVMe storage.
URL: [Amazon EC2 P5 Instances](https://aws.amazon.com/ec2/instance-types/p5/)

[FACT] AWS announced price reductions of up to 45% for P5 and P5en instances, effective June 1, 2025 for On-Demand and June 4, 2025 for Savings Plan purchases. Specific reductions: P5 up to 45%, P5en up to 26%, P4d and P4de up to 33%.
URL: [AWS Blog — Up to 45% Price Reduction for NVIDIA GPU Instances](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/)

[FACT] Following the June 2025 price reductions, p5.48xlarge On-Demand pricing is approximately $55.04/hour (list price). A new single-GPU p5.4xlarge configuration starts from approximately $5,022/month.
URL: [costcalc.cloudoptimo.com — p5.48xlarge](https://costcalc.cloudoptimo.com/aws-pricing-calculator/ec2/p5.48xlarge)

[FACT] New P5 single-H100 instances (p5.4xlarge) became available in Amazon SageMaker Training and Processing Jobs in August 2025.
URL: [AWS Announcement — P5 Single GPU SageMaker](https://aws.amazon.com/about-aws/whats-new/2025/08/p5-instance-nvidia-h100-gpu-sagemaker-training-processing-jobs/)

### G5 Instances (NVIDIA A10G)

[FACT] Amazon EC2 G5 instances are GPU-based instances for a wide range of graphics-intensive and machine learning inference use cases.
URL: [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/)

G5 instances support configurations from g5.xlarge (1 GPU) to g5.48xlarge (8 GPUs). They are commonly used for cost-effective LLM inference at 7B–70B parameter scale.

### G6 Instances (NVIDIA L4)

[FACT] G6 instances feature up to 8 NVIDIA L4 Tensor Core GPUs with 24 GB of memory per GPU, and are available with "fractionalized GPU sizes with as little as 1/8 of an L4 GPU with 3 GB of GPU memory."
URL: [Amazon EC2 G6 Instances](https://aws.amazon.com/ec2/instance-types/g6/)

[FACT] G6 instances offer "2x better performance for deep learning inference and graphics workloads compared to EC2 G4dn instances." They include third-generation AMD EPYC processors, up to 192 vCPUs, up to 100 Gbps network bandwidth, and up to 7.52 TB local NVMe SSD storage.
URL: [Amazon EC2 G6 Instances](https://aws.amazon.com/ec2/instance-types/g6/)

[FACT] G6 instances became available in AWS GovCloud (US-East) Region in August 2025.
URL: [AWS Announcement — G6 GovCloud](https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-ec2-g6-now-available-govcloud-east-region/)

G6 instance pricing examples:
- g6.xlarge: $0.8048/hr On-Demand
- g6.48xlarge: $13.3504/hr On-Demand

Source: [Vantage — g6.xlarge](https://instances.vantage.sh/aws/ec2/g6.xlarge) | [Vantage — g6.48xlarge](https://instances.vantage.sh/aws/ec2/g6.48xlarge)

### Spot Instance Pricing for GPU Families

[FACT] EC2 Spot Instances are available at discounts of up to 90% off On-Demand for older GPU generations (P2, P3). For current generations (P4, P5, G5, G6), spot discounts typically range 60–70% off On-Demand.
URL: [Amazon EC2 Spot Instances Pricing](https://aws.amazon.com/ec2/spot/pricing/) | Corroborated: [nops.io — Amazon EC2 GPU Instances Complete Guide](https://www.nops.io/blog/amazon-ec2-gpu-instances-the-complete-guide/)

**Note:** Spot GPU capacity is constrained and frequently unavailable for P5 instances at scale. ISVs running training jobs requiring guaranteed capacity should evaluate EC2 Capacity Blocks for ML or On-Demand Reserved Instances.

### June 2025 Pricing Model Changes

[FACT] In June 2025, AWS updated pricing and usage models for NVIDIA GPU-accelerated EC2 instances. This included significant On-Demand price reductions and adjustments to Savings Plan eligibility.
URL: [AWS Announcement — Pricing Updates for NVIDIA GPU Instances](https://aws.amazon.com/about-aws/whats-new/2025/06/pricing-usage-model-ec2-instances-nvidia-gpus/)

---

## Section 7: AWS Batch — Managed Batch Computing

### Overview

[FACT] "AWS Batch provides all of the necessary functionality to run high-scale, compute-intensive workloads on top of AWS managed container orchestration services, Amazon ECS and Amazon EKS."
URL: [AWS Batch](https://aws.amazon.com/batch/)

[FACT] "AWS Batch dynamically provisions the optimal quantity and type of compute resources based on the volume and specific requirements of submitted batch jobs."
URL: [AWS Batch Documentation — What is AWS Batch?](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)

AWS Batch eliminates the need to build or manage custom job schedulers or batch processing frameworks. The service handles: capacity planning, job scheduling, dependency resolution, retry logic, and compute resource allocation.

### Compute Environments: Fargate vs. EC2

[FACT] "The compute environments listed in computeEnvironmentOrder must all be Fargate compute environments (FARGATE or FARGATE_SPOT), as EC2 and Fargate compute environments can't be mixed" within a single job queue.
URL: [AWS Batch — Job Queues on Fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate-job-queues.html)

| Attribute | Fargate Compute Env | EC2 Compute Env |
|-----------|--------------------|--------------------|
| Startup speed | Faster (no instance launch) | Slower first job; faster for subsequent (instance reuse) |
| GPU support | No | Yes (GPU instance types) |
| Resource allocation | Exact vCPU/memory per job | Bin-packing across instances |
| AMI management | Not required | Required (or use managed AMI) |
| Instance type selection | AWS-managed | Operator-configurable |

Source: [AWS Batch FAQs](https://aws.amazon.com/batch/faqs/) | [AWS Batch — Nakivo](https://www.nakivo.com/blog/aws-batch-creating-a-compute-environment/)

### Job Queues and Priority

[FACT] Job queue priority determines the order that job queues are evaluated when multiple queues dispatch jobs within a shared compute environment. "A higher value for priority indicates a higher priority."
URL: [AWS CloudFormation — AWS::Batch::JobQueue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-jobqueue.html)

Priority scheduling enables ISVs to implement patterns such as:
- High-priority queue for customer-triggered inference jobs
- Medium-priority queue for scheduled report generation
- Low-priority queue for background model retraining (Spot-backed)

### ML Training Integration

[FACT] AWS Batch supports SageMaker Training job queuing: "data scientists and ML engineers can submit Training jobs with priorities to configurable queues. This capability ensures that ML workloads run automatically as soon as resources become available, eliminating the need for manual coordination."
URL: [AWS Blog — AWS Batch Support for SageMaker Training Jobs](https://aws.amazon.com/blogs/machine-learning/introducing-aws-batch-support-for-amazon-sagemaker-training-jobs/)

[FACT] Amazon Search increased ML training throughput twofold by leveraging AWS Batch for SageMaker Training jobs, "orchestrating machine learning training workloads on GPU-accelerated instance families like P5, P4, and others."
URL: [AWS Blog — Amazon Search ML Training with AWS Batch](https://aws.amazon.com/blogs/machine-learning/how-amazon-search-increased-ml-training-twofold-using-aws-batch-for-amazon-sagemaker-training-jobs/)

[FACT] AWS Batch supports multi-region serverless distributed training when combined with Amazon SageMaker.
URL: [AWS Blog — Multiregion Serverless Distributed Training](https://aws.amazon.com/blogs/machine-learning/multiregion-serverless-distributed-training-with-aws-batch-and-amazon-sagemaker/)

---

## Section 8: Operational Burden Comparison

The following table applies the standardized Difficulty Rating Scale (1–5) and FTE Estimation Framework defined in the research brief. Assumptions: mid-size ISV deployment, 50 enterprise customers, applications requiring both API serving and periodic ML inference.

| Capability | On-Premises | Managed K8s (EKS) | Cloud-Native (Lambda/Fargate/App Runner) |
|------------|------------|-------------------|------------------------------------------|
| **Serverless Functions** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Custom FaaS platform required | Knative or KEDA required | Lambda fully managed |
| | Kubernetes + Knative/OpenFaaS | Helm charts, autoscaling config | Console/IaC only |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 |
| **Container Orchestration** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-managed K8s or Nomad | EKS control plane managed; node groups self-managed | ECS + Fargate; AWS manages EC2 fleet |
| | kubeadm, etcd, CNI plugins | eksctl, ALB controller, cluster autoscaler | Task definitions, ECS service configs |
| | Est. FTE: 1.5–3.0 | Est. FTE: 0.75–1.5 | Est. FTE: 0.25–0.5 |
| **GPU/AI Inference Serving** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 3/5 |
| | Full GPU driver/CUDA mgmt | GPU node groups + device plugins | EC2 GPU instances (P5/G6) via ECS; or Inferentia via inf2 |
| | NVIDIA drivers, CUDA, MIG config | NVIDIA device plugin, taint/tolerations | GPU task definitions or SageMaker endpoints |
| | Est. FTE: 2.0–4.0 | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 |
| **Batch/ML Training Jobs** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 2/5 |
| | Custom job scheduler (Slurm, Ray) | Volcano or Argo Workflows | AWS Batch manages scheduling, provisioning |
| | Full cluster management | Batch framework installation and tuning | Job definitions and compute environments |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 |
| **Auto-Scaling** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Custom metrics + HPA/VPA or manual | Cluster Autoscaler + HPA + Karpenter | App Auto Scaling managed by AWS; predictive scaling available |
| | Prometheus + custom autoscaler | Karpenter or Cluster Autoscaler | ECS Service Auto Scaling, Lambda concurrency limits |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |

Note: FTE estimates represent active operational work and do not include on-call burden. On-call adds approximately 0.25 FTE per 1.0 FTE of active work for cloud-native, 0.5 FTE for managed K8s, and 0.75–1.0 FTE for on-premises operations.

---

## Key Takeaways

- **Lambda's 2025 evolution changes the calculus for high-volume workloads.** Lambda Managed Instances (November 2025) allows EC2-backed Lambda execution with commitment pricing (up to 72% savings via Savings Plans/Reserved Instances), making Lambda viable for steady-state high-throughput workloads that previously required ECS or EC2 — at substantially lower operational overhead.

- **GPU pricing dropped significantly in mid-2025.** AWS cut P5 (H100) instance On-Demand prices by up to 45% in June 2025. Combined with 60–70% spot discounts, GPU-backed AI inference and training workloads are materially more cost-accessible than in 2024. ISVs should reprice all GPU workload cost models against June 2025 rates.

- **Inferentia2 and Trainium3 are production-ready for mainstream model families.** The Neuron SDK now supports PyTorch, JAX, HuggingFace, and vLLM with Llama 4 and FLUX models. Claimed savings of 30–50% versus NVIDIA GPU instances are credible for compatible workloads, but the CUDA ecosystem gap remains real for cutting-edge or highly customized architectures.

- **AWS Batch is the lowest-friction path to scalable ML training and batch inference.** It eliminates all job scheduler management, integrates natively with SageMaker Training jobs, and supports both Spot (cost-optimized) and On-Demand (reliability-optimized) GPU compute environments with priority queuing — appropriate for ISVs needing scheduled retraining or large-scale data processing without dedicated MLOps infrastructure.

- **App Runner is not suitable for AI workloads.** Its request-based-only scaling, single-container-per-service limitation, and CPU throttling at zero requests make it inappropriate for ML inference, background workers, or any non-HTTP compute pattern. ISVs building AI-driven SaaS should default to ECS + Fargate for containerized workloads requiring more control than App Runner provides.

---

## Related — Out of Scope

The following topics surfaced during research but are outside the F8 scope boundary (AWS compute only):

- **Amazon SageMaker endpoints:** Managed ML model hosting built on top of EC2/GPU infrastructure. See relevant SageMaker research agent.
- **Amazon EKS (Elastic Kubernetes Service):** Managed Kubernetes control plane with self-managed node groups; GPU and Inferentia node group configurations. See managed K8s agent.
- **EC2 Capacity Blocks for ML:** Reserved GPU capacity for defined time windows — relevant for training runs but crosses into reservation/pricing strategy territory.
- **AWS Graviton (ARM) instances:** Graviton4 compute for CPU-bound workloads; available in Lambda, Fargate, and ECS but treated as a pricing/performance variant rather than a distinct compute service.
- **Amazon Bedrock:** Fully managed LLM inference API; runs on AWS custom silicon but abstracts all compute from the caller. See cloud-native AI services agent.

---

## Sources

1. [AWS Lambda Cold Starts in 2025](https://edgedelta.com/company/knowledge-center/aws-lambda-cold-start-cost) — Edge Delta
2. [AWS Lambda Cold Start Optimization in 2025](https://zircon.tech/blog/aws-lambda-cold-start-optimization-in-2025-what-actually-works/) — Zircon Tech
3. [Understanding Lambda Function Scaling](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html) — AWS Documentation
4. [Configuring Reserved Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) — AWS Documentation
5. [Configuring Provisioned Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) — AWS Documentation
6. [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/) — AWS
7. [AWS Lambda Cost Breakdown 2026](https://www.wiz.io/academy/cloud-cost/aws-lambda-cost-breakdown) — Wiz
8. [Lambda Managed Instances Announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-managed-instances/) — AWS
9. [Introducing Lambda Managed Instances Blog](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/) — AWS Blog
10. [Lambda Managed Instances re:Invent 2025 Coverage](https://devclass.com/2025/12/01/aws-debuts-lambda-managed-instances-on-ec2-more-control-lower-cost-for-high-volume-users/) — DevClass
11. [AWS re:Post — GPU Serverless Inferencing](https://repost.aws/questions/QUlHAbaJiIRt-eem9gizSmOQ/is-gpu-serverless-inferencing-for-custom-llm-models) — AWS re:Post
12. [Lambda Limitations for AI Workloads](https://modal.com/blog/aws-lambda-limitations-article) — Modal
13. [AWS ECS Documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) — AWS
14. [ECS Service Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html) — AWS Documentation
15. [AWS Fargate Pricing](https://aws.amazon.com/fargate/pricing/) — AWS
16. [AWS Fargate Pricing Explained 2025](https://cloudchipr.com/blog/aws-fargate-pricing) — CloudChipr
17. [AWS App Runner FAQs](https://aws.amazon.com/apprunner/faqs/) — AWS
18. [App Runner Managing Autoscaling](https://docs.aws.amazon.com/apprunner/latest/dg/manage-autoscaling.html) — AWS Documentation
19. [App Runner Pricing](https://aws.amazon.com/apprunner/pricing/) — AWS
20. [App Runner vs ECS Fargate 2025](https://blogs.businesscompassllc.com/2025/06/aws-container-orchestration-app-runner.html) — Business Compass LLC
21. [App Runner vs ECS vs Lambda](https://dashankadesilva.medium.com/aws-app-runner-vs-ecs-vs-lambda-choosing-the-right-compute-option-36915d355cd5) — Medium
22. [EC2 Auto Scaling — Launch Templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html) — AWS Documentation
23. [EC2 Auto Scaling — Allocation Strategies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/allocation-strategies.html) — AWS Documentation
24. [EC2 Auto Scaling — Predictive Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) — AWS Documentation
25. [Amazon EC2 Spot Instances Pricing](https://aws.amazon.com/ec2/spot/pricing/) — AWS
26. [EC2 Auto Scaling Predictive Scaling — Six More Regions](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-ec2-auto-scaling-predictive-scaling-in-six/) — AWS
27. [Predictive Scaling for EC2 Auto Scaling](https://awsforengineers.com/blog/predictive-scaling-for-ec2-auto-scaling/) — AWS for Engineers
28. [AWS Neuron SDK](https://aws.amazon.com/ai/machine-learning/neuron/) — AWS
29. [Amazon Trainium and Inferentia 2025](https://introl.com/blog/aws-trainium-inferentia-silicon-ecosystem-guide-2025) — Introl
30. [HuggingFace aws-neuron](https://huggingface.co/aws-neuron) — HuggingFace
31. [AWS Inferentia2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/) — AWS
32. [inf2.xlarge Pricing](https://instances.vantage.sh/aws/ec2/inf2.xlarge) — Vantage
33. [inf2.24xlarge Pricing](https://instances.vantage.sh/aws/ec2/inf2.24xlarge) — Vantage
34. [AWS Inferentia2 vs Trainium vs GPU](https://zircon.tech/blog/aws-ai-infrastructure-inferentia2-vs-trainium-vs-gpu-for-production-workloads/) — Zircon Tech
35. [AWS Custom ML Accelerators](https://www.cloudoptimo.com/blog/amazons-custom-ml-accelerators-aws-trainium-and-inferentia/) — CloudOptimo
36. [Cost Optimizing AI Workloads on AWS](https://aws.amazon.com/blogs/aws-cloud-financial-management/navigating-gpu-challenges-cost-optimizing-ai-workloads-on-aws/) — AWS Blog
37. [EC2 Trn3 UltraServers Announcement](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/) — AWS
38. [Amazon Trainium3 Chip](https://interestingengineering.com/innovation/amazon-new-trainium3-chip) — Interesting Engineering
39. [TechCrunch — Amazon Trainium3](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/) — TechCrunch
40. [Amazon EC2 P5 Instances](https://aws.amazon.com/ec2/instance-types/p5/) — AWS
41. [Up to 45% Price Reduction for NVIDIA GPU Instances](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) — AWS Blog
42. [AWS — NVIDIA GPU Pricing and Usage Model Updates](https://aws.amazon.com/about-aws/whats-new/2025/06/pricing-usage-model-ec2-instances-nvidia-gpus/) — AWS
43. [P5 Single GPU SageMaker](https://aws.amazon.com/about-aws/whats-new/2025/08/p5-instance-nvidia-h100-gpu-sagemaker-training-processing-jobs/) — AWS
44. [Amazon EC2 G5 Instances](https://aws.amazon.com/ec2/instance-types/g5/) — AWS
45. [Amazon EC2 G6 Instances](https://aws.amazon.com/ec2/instance-types/g6/) — AWS
46. [G6 GovCloud Availability](https://aws.amazon.com/about-aws/whats-new/2025/08/amazon-ec2-g6-now-available-govcloud-east-region/) — AWS
47. [g6.xlarge Pricing](https://instances.vantage.sh/aws/ec2/g6.xlarge) — Vantage
48. [g6.48xlarge Pricing](https://instances.vantage.sh/aws/ec2/g6.48xlarge) — Vantage
49. [nops.io — EC2 GPU Instances Complete Guide](https://www.nops.io/blog/amazon-ec2-gpu-instances-the-complete-guide/) — nOps
50. [AWS Batch](https://aws.amazon.com/batch/) — AWS
51. [AWS Batch — What is AWS Batch?](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) — AWS Documentation
52. [AWS Batch — Job Queues on Fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate-job-queues.html) — AWS Documentation
53. [AWS Batch FAQs](https://aws.amazon.com/batch/faqs/) — AWS
54. [AWS Batch Support for SageMaker Training Jobs](https://aws.amazon.com/blogs/machine-learning/introducing-aws-batch-support-for-amazon-sagemaker-training-jobs/) — AWS Blog
55. [Amazon Search ML Training with AWS Batch](https://aws.amazon.com/blogs/machine-learning/how-amazon-search-increased-ml-training-twofold-using-aws-batch-for-amazon-sagemaker-training-jobs/) — AWS Blog
56. [Multiregion Serverless Distributed Training](https://aws.amazon.com/blogs/machine-learning/multiregion-serverless-distributed-training-with-aws-batch-and-amazon-sagemaker/) — AWS Blog
57. [AWS Lambda SnapStart Optimization](https://aws.amazon.com/blogs/compute/optimizing-cold-start-performance-of-aws-lambda-using-advanced-priming-strategies-with-snapstart/) — AWS Blog
58. [p5.48xlarge Pricing](https://costcalc.cloudoptimo.com/aws-pricing-calculator/ec2/p5.48xlarge) — CloudOptimo Cost Calc
