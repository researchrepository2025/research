# Simplified On-Prem AI Architecture Framework

*Research compiled from 2025 sources | Last Updated: December 3, 2025*

---

## Executive Summary

This framework consolidates enterprise AI deployment options into **4 architecture types** for organizations requiring physical on-premises infrastructure. Edge/distributed deployment is treated as a **modifier** that applies to any architecture, not a separate category.

**Key assumptions:**
- Proprietary LLMs can be licensed for on-prem deployment (licensing not a blocker)
- On-prem LLM deployments require high encryption at rest and in transit
- Kubernetes (K8s) is an orchestration tool available across all architectures

---

## Architecture Comparison Table

| | **1. Fully On-Prem** | **2. Cloud-Managed Hybrid** | **3. Hybrid-Managed** | **4. Self-Managed Hybrid** |
|---|---|---|---|---|
| **Description** | All hardware and software on-prem; can be air-gapped (no connectivity) or connected; maximum data sovereignty | Physical on-prem hardware managed by cloud control planes (AWS Outposts, Azure Arc, Google Anthos); cloud vendor manages entire software stack | On-prem hardware + cloud burst; strategic software split - sensitive workloads on-prem, operational tools in cloud | On-prem hardware + cloud IaaS (raw VMs/GPUs); you manage entire software stack across both environments |
| **Example 1** | **Microsoft US Intelligence**: GPT-4/GPT-4o deployed to air-gapped Azure Government Top Secret cloud for classified defense workloads ([CyberSecurityNews](https://cybersecuritynews.com/microsoft-air-gapped-gpt-4/)) | **Mercado Livre**: AWS Outposts for latency-sensitive automation in distribution centers serving 100M+ users ([AWS Case Study](https://aws.amazon.com/solutions/case-studies/mercado-livre-outposts/)) | **AWS AI Factories**: Full-stack AI infrastructure (NVIDIA GPUs, Trainium, SageMaker, Bedrock) installed in customer data centers with cloud management ([TechCrunch](https://techcrunch.com/2025/12/02/amazon-challenges-competitors-with-on-premises-nvidia-ai-factories/)) | **OpenAI**: 7,500 K8s nodes across physical on-prem GPU clusters + Azure cloud; self-managed K8s spanning both environments ([Kubernetes.io](https://kubernetes.io/case-studies/openai/)) |
| **Example 2** | **NATO NCIA**: Google Distributed Cloud air-gapped deployment for classified JATEC workloads; Vertex AI enabled ([Google Cloud Press](https://www.googlecloudpresscorner.com/2025-11-24-NATO-and-Google-Cloud-Sign-Multi-Million-Dollar-Deal-for-AI-Enabled-Sovereign-Cloud)) | **O2 Telefónica Germany**: Physical AWS Outposts racks for 5G core data plane serving 1M+ subscribers ([Telefónica Press](https://www.telefonica.de/news/press-releases-telefonica-germany/2025/03/o2-telefonica-selects-amazon-web-services-for-its-cloud-native-ims-voice-and-5g-core-networks.html)) | **Azure Stack Edge Healthcare**: Physical appliances with NVIDIA T4 GPUs at hospital facilities; <1 sec inference for X-ray/CT with cloud MLOps ([Digital Thought Disruption](https://digitalthoughtdisruption.com/2025/07/17/azure-local-gpu-on-prem-ai-regulated-industries/)) | **Walmart WCNP**: 545,000+ pods on 93,000+ nodes; self-managed platform spanning 6,000+ stores/DCs + Azure/GCP ([SiliconANGLE](https://siliconangle.com/2025/09/30/walmart-leverages-developer-focused-ai-agents-boost-software-innovation-aifactoriesdatacenters/)) |
| **Example 3** | **Singapore Government**: Three agencies (GovTech, CSIT, HTSTA) deploying Google Gemini on air-gapped Google Distributed Cloud for national security ([Google Cloud Press](https://www.googlecloudpresscorner.com/2025-08-28-Google-Cloud-Makes-Gemini-Everywhere-Vision-a-Reality,-Doubles-Down-on-Enterprise-AI-Commitment-to-Singapore)) | **Walmart Edge**: 1,500 cameras across 1,000+ stores with cloud orchestration for inventory and shelf scanning ([Future Stores WBR](https://futurestores.wbresearch.com/blog/walmart-ai-powered-store-strategy-future-amazon-go)) | *No additional verified example found in 2025 sources* | *No additional verified example found in 2025 sources* |
| **Tech Stack** | NVIDIA H100/B200 GPUs; InfiniBand 400 Gbps; self-hosted K8s (OpenShift/Rancher); on-prem MLOps (Kubeflow, MLflow); encrypted LLM weights; offline model management | AWS Outposts racks / Azure Stack HCI / Google Anthos; managed K8s (EKS Anywhere, AKS Arc, GKE Anthos); vendor MLOps integration; LLM encrypted on vendor-managed nodes | On-prem GPU clusters for inference; self-hosted or managed K8s; on-prem: LLM weights, inference, data processing; cloud: SageMaker/Vertex AI, Datadog, dev environments | Self-hosted K8s spanning on-prem + cloud IaaS; all software self-managed (MLflow, Prometheus, Grafana); cloud = raw EC2/GCE VMs only; full LLM encryption responsibility |
| **On-Prem Intensity** | **5/5** - All compute, storage, networking on-prem; no cloud dependency | **2-4/5** - Varies by LLM placement: 4/5 if LLM on-prem, 2-3/5 if LLM in cloud (API calls) | **4/5** - On-prem GPU clusters for inference; cloud for training/burst and operational tools | **4/5** - On-prem primary; cloud IaaS for burst compute only |
| **Ease of Implementation** | **2/5** - All infrastructure self-managed; no hybrid complexity but full operational burden; LLM encryption your responsibility; 12-24 months typical | **4/5** - Cloud vendor handles orchestration, updates, monitoring; fastest hybrid deployment; LLM encryption handled by vendor tooling; 3-6 months typical | **3/5** - Must make strategic software placement decisions; integration complexity between environments; LLM encryption on-prem; 6-12 months typical | **1/5** - You manage entire stack across TWO environments; no vendor support; highest operational burden; all LLM security your responsibility; 12+ months typical |
| **Key Observations** | Best for maximum sovereignty (defense, classified); can operate fully disconnected; no vendor lock-in; requires deep in-house expertise; economical at scale after 3-5 years | "Sweet spot" for most enterprises wanting hybrid; single pane of glass management; vendor lock-in risk; fastest time-to-value for hybrid deployments | Optimizes for both sovereignty AND operational ease; keeps "crown jewels" on-prem while offloading complexity; requires clear decision framework for software placement | Maximum control and flexibility; avoids vendor lock-in for software; highest expertise requirements; best for organizations with strong platform engineering teams |

---

## Quick Reference Matrix

| # | Architecture | Hardware | Software | On-Prem Intensity | Ease | Timeline |
|---|--------------|----------|----------|:-----------------:|:----:|----------|
| 1 | **Fully On-Prem** | On-prem only | On-prem managed | 5/5 | 2/5 | 12-24 mo |
| 2 | **Cloud-Managed Hybrid** | On-prem + Cloud | Cloud managed | 2-4/5* | 4/5 | 3-6 mo |
| 3 | **Hybrid-Managed** | On-prem + Cloud | Strategic split | 4/5 | 3/5 | 6-12 mo |
| 4 | **Self-Managed Hybrid** | On-prem + Cloud | On-prem managed | 4/5 | 1/5 | 12+ mo |

*\*Architecture 2 intensity varies by LLM placement: 4/5 if LLM runs on-prem, 2-3/5 if LLM accessed via cloud API*

---

## Architecture 1: Fully On-Prem

### Characteristics

| Aspect | Details |
|--------|---------|
| **Hardware** | On-prem only (GPU clusters, storage, networking) |
| **Software** | All on-prem (LLM weights, inference, MLOps, monitoring) |
| **Cloud usage** | None |
| **Connectivity** | Can be air-gapped OR connected (your choice) |
| **K8s option** | Self-hosted only (OpenShift, Rancher, vanilla K8s) |

### When to Use

- Maximum data sovereignty required (defense, intelligence, classified)
- Regulatory requirements mandate no cloud connectivity
- Organization has deep infrastructure expertise
- Long-term cost optimization at scale (3-5+ year horizon)
- Complete control over all components required

### LLM Deployment

Licensed proprietary LLM downloaded and deployed on-prem with high encryption at rest and in transit. All model updates handled via secure offline transfer mechanisms.

### Example Companies

1. **Microsoft US Intelligence** - Air-gapped GPT-4/GPT-4o for classified workloads
2. **NATO NCIA** - Google Distributed Cloud air-gapped for JATEC
3. **Singapore Government** - Gemini on air-gapped GDC for national security

---

## Architecture 2: Cloud-Managed Hybrid

### Characteristics

| Aspect | Details |
|--------|---------|
| **Hardware** | On-prem + Cloud (burst capacity) |
| **Software** | Cloud vendor manages entire stack |
| **Cloud usage** | Control plane, MLOps, monitoring, orchestration |
| **Products** | AWS Outposts, Azure Arc/Stack, Google Anthos |
| **K8s option** | Managed K8s (EKS Anywhere, AKS Arc, GKE Anthos) |

### When to Use

- Want hybrid benefits with minimal operational burden
- Comfortable with cloud vendor managing infrastructure
- Need fastest time-to-value for hybrid deployment
- Existing cloud relationship/expertise
- Willing to accept vendor lock-in for operational ease

### LLM Deployment & Infrastructure Intensity

LLM placement significantly affects on-prem infrastructure intensity:

| LLM Placement | On-Prem Intensity | On-Prem Infrastructure | Data Flow |
|---------------|:-----------------:|------------------------|-----------|
| **LLM on-prem** (pinned to on-prem nodes) | **4/5** | GPU clusters required | Data stays on-prem |
| **LLM in cloud** (API calls) | **2-3/5** | Lighter compute (no GPUs) | Data sent to cloud for inference |

**LLM on-prem**: Licensed proprietary LLM deployed via cloud vendor's management plane, encrypted, pinned to on-prem nodes. Vendor tooling assists with encryption and key management. Requires substantial GPU infrastructure.

**LLM in cloud**: On-prem handles application logic, data preprocessing, and orchestration. LLM inference via cloud API (e.g., Azure OpenAI, Bedrock). Significantly reduces on-prem hardware requirements but data leaves premises for inference.

### Example Companies

1. **Mercado Livre** - AWS Outposts for distribution center automation
2. **O2 Telefónica Germany** - AWS Outposts for 5G core
3. **Walmart Edge** - Cloud-orchestrated cameras across 1,000+ stores

---

## Architecture 3: Hybrid-Managed

### Characteristics

| Aspect | Details |
|--------|---------|
| **Hardware** | On-prem + Cloud (burst capacity) |
| **Software** | Strategic split based on requirements |
| **Cloud usage** | Selected services (MLOps, monitoring, dev tools) |
| **On-prem software** | LLM weights, inference runtime, sensitive data processing |
| **K8s option** | Either self-hosted OR managed (part of strategic decision) |

### Strategic Software Split Framework

**Decision criteria for software placement:**

| Question | If Yes → |
|----------|----------|
| Does it process sensitive data? | On-prem |
| Does it contain IP (LLM weights)? | On-prem (encrypted) |
| Does it drive hardware utilization? | On-prem |
| Does it add operational complexity? | Cloud |
| Does it need elastic scaling? | Cloud |

**Typical split:**

| On-Prem (Required/High-Value) | Cloud (Ease of Implementation) |
|-------------------------------|-------------------------------|
| LLM weights & inference runtime (encrypted) | MLOps platform (experiment tracking, pipelines) |
| Sensitive data & IP | Monitoring & observability dashboards |
| Data processing pipelines | Development environments & notebooks |
| Security/access controls | Model registry & versioning |
| Compliance audit logs | CI/CD for model deployment |

### When to Use

- Need balance of sovereignty AND operational ease
- Clear distinction between sensitive and operational workloads
- Want to keep "crown jewels" on-prem while offloading complexity
- Have capability to make and maintain strategic architecture decisions

### LLM Deployment

Licensed proprietary LLM deployed on-prem with high encryption. Inference runs on-prem; training and experimentation may use cloud resources with appropriate data handling.

### Example Companies

1. **AWS AI Factories** - Full AI stack in customer data centers with cloud management
2. **Azure Stack Edge Healthcare** - On-prem inference with cloud MLOps

---

## Architecture 4: Self-Managed Hybrid

### Characteristics

| Aspect | Details |
|--------|---------|
| **Hardware** | On-prem + Cloud IaaS (raw VMs/GPUs) |
| **Software** | All self-managed (you own entire stack) |
| **Cloud usage** | IaaS only - raw compute, no managed services |
| **On-prem software** | Everything (LLM, MLOps, monitoring, K8s control plane) |
| **K8s option** | Self-hosted only, spanning on-prem + cloud nodes |

### When to Use

- Maximum control required over entire stack
- Want to avoid ALL vendor lock-in (including managed services)
- Strong platform engineering team available
- Need cloud burst capacity but won't use managed services
- Cost optimization through self-management at scale

### LLM Deployment

Licensed proprietary LLM deployed on self-managed infrastructure across on-prem and cloud nodes. You handle all encryption, security, updates, and key management.

### Example Companies

1. **OpenAI** - 7,500 K8s nodes spanning on-prem GPU clusters + Azure
2. **Walmart WCNP** - 545,000+ pods across self-managed infrastructure

---

## Deployment Patterns: Centralized vs Edge

Edge is **NOT a separate architecture** - it's a deployment pattern that applies to any of the 4 architectures.

| Pattern | Description | Hardware Distribution |
|---------|-------------|----------------------|
| **Centralized** | Single or few data center locations | Concentrated GPU clusters |
| **Distributed/Edge** | Many locations (stores, factories, field sites) | Distributed edge devices |

### Edge Applied to Each Architecture

| Architecture | + Centralized | + Edge/Distributed |
|--------------|---------------|-------------------|
| **1. Fully On-Prem** | Air-gapped data center | Air-gapped field units (military) |
| **2. Cloud-Managed** | Outposts in corporate DC | AWS IoT Greengrass at stores |
| **3. Hybrid-Managed** | Strategic split in DC | Edge inference + cloud MLOps |
| **4. Self-Managed** | Self-hosted K8s in DC | K8s spanning edge locations |

### Edge Examples

- **Walmart**: 1,500 cameras across 1,000+ stores (Cloud-Managed + Edge)
- **BMW**: 1,000+ AIQX units across all plants (Cloud-Managed + Edge)
- **Starbucks China**: 7,500+ stores with edge computing (Cloud-Managed + Edge)
- **US Air Force RSO**: Ruggedized edge units in field (Fully On-Prem + Edge)

---

## Kubernetes Across All Architectures

K8s is an **orchestration tool**, not tied to any architecture. Each architecture can use K8s differently:

| Architecture | K8s Type | Control Plane Location | Examples |
|--------------|----------|------------------------|----------|
| **1. Fully On-Prem** | Self-hosted | On-prem | OpenShift, Rancher, vanilla K8s |
| **2. Cloud-Managed** | Managed | Cloud | EKS Anywhere, GKE Anthos, AKS Arc |
| **3. Hybrid-Managed** | Either | Your choice | Part of strategic split decision |
| **4. Self-Managed** | Self-hosted | On-prem | Spans on-prem + cloud IaaS nodes |

---

## Decision Framework

### Key Questions to Select Architecture

```
Q1: Can ANY data leave your premises?
    ├─ NO → Architecture 1 (Fully On-Prem)
    └─ YES → Continue to Q2

Q2: Do you want cloud vendor to manage infrastructure?
    ├─ YES, fully → Architecture 2 (Cloud-Managed Hybrid)
    └─ NO or PARTIALLY → Continue to Q3

Q3: Do you want to use cloud managed services (SageMaker, managed K8s, etc.)?
    ├─ YES, selectively → Architecture 3 (Hybrid-Managed)
    └─ NO, IaaS only → Architecture 4 (Self-Managed Hybrid)
```

### Decision Matrix

| If you need... | Choose |
|----------------|--------|
| Maximum sovereignty, air-gap capability | **1. Fully On-Prem** |
| Fastest deployment, vendor support | **2. Cloud-Managed Hybrid** |
| Balance of control and ease | **3. Hybrid-Managed** |
| Maximum control, avoid all lock-in | **4. Self-Managed Hybrid** |

---

## Key Differentiators Summary

| Factor | Arch 1 | Arch 2 | Arch 3 | Arch 4 |
|--------|--------|--------|--------|--------|
| On-prem intensity | 5/5 | 2-4/5 (varies by LLM) | 4/5 | 4/5 |
| Internet required | No (optional) | Yes | Yes | Yes |
| Cloud vendor dependency | None | High | Medium | Low (IaaS only) |
| Operational burden | High | Low | Medium | Very High |
| Control level | Maximum | Limited | High | Maximum |
| Scalability | Fixed | Elastic | Elastic | Elastic |
| LLM encryption responsibility | You | Vendor assists | You (on-prem) | You (all) |
| Vendor lock-in risk | None | High | Medium | Low |
| Best for | Max sovereignty | Ease + hybrid | Balance | Max control + scale |

---

## Relationship to Detailed Framework

This simplified framework consolidates the 7 architectures documented in [05_consolidation.md](./05_consolidation.md):

| Simplified Architecture | Original Architectures |
|------------------------|----------------------|
| 1. Fully On-Prem | Air-Gapped (1) |
| 2. Cloud-Managed Hybrid | Cloud Control Plane (2), Edge-Extended (6) |
| 3. Hybrid-Managed | Data-Sovereign Hybrid (3) |
| 4. Self-Managed Hybrid | Multi-Cloud K8s Hybrid (5) |

**Not included in this framework:**
- Federated/Confidential (4): Primary compute is IN cloud (TEEs)
- Cloud-Native (7): No on-prem hardware

See 05_consolidation.md for detailed analysis of each original architecture with additional company examples and technical specifications.

---

*Document compiled from verified 2025 research sources.*
