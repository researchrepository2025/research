# F39 — On-Premises Compute Management
## Research File: Self-Managed Compute Infrastructure for AI-SaaS

**Agent:** F39 — On-Prem Compute Management
**Scope:** Hardware procurement, hypervisor management, GPU management, resource scheduling, auto-scaling, high availability, power/cooling, and cost modeling for 100% on-premises AI-SaaS deployments.
**Date:** 2026-02-18

---

## Executive Summary

Self-managing compute infrastructure for an AI-SaaS product on-premises imposes capital, operational, and lead-time burdens that are qualitatively different from cloud alternatives. A single 8-GPU H100 server costs $300,000–$450,000 in hardware alone, with a full deployment serving 50 enterprise tenants requiring $5–15 million in CapEx before the first line of software ships. [GPU procurement lead times have improved from 2023 peaks of 40+ weeks but remain 5–6 months on average in 2025](https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis), creating acute planning risk for organizations without multi-quarter hardware pipelines. Operational staffing benchmarks peg the requirement at approximately one specialized engineer per 100 GPUs, exclusive of on-call burden, which for a mid-size ISV translates to 2–5 FTE dedicated solely to compute infrastructure. Break-even against cloud GPU pricing occurs only above 60–70% sustained utilization over a 3+ year horizon — a threshold that most production AI-SaaS workloads achieve only with careful scheduling discipline. For ISVs whose customers demand on-premises deployment for data sovereignty or regulatory reasons, these constraints are non-negotiable realities that must be engineered around from day one.

---

## 1. Hardware Procurement and Lifecycle

### 1.1 GPU Server Pricing (2025)

Current market pricing for production AI compute hardware:

| Hardware Unit | List Price (2025) |
|--------------|-------------------|
| NVIDIA H100 80GB SXM5 (single GPU) | $25,000–$40,000 |
| NVIDIA DGX H100 (8-GPU system) | $373,000–$450,000 |
| NVIDIA GB200 NVL72 rack | $3,000,000+ |
| 1,000-GPU cluster (fully configured) | $30–50 million |
| 10,000-GPU cluster | $300–500 million |

Sources: [GMI Cloud H100 pricing analysis](https://www.gmicloud.ai/blog/how-much-does-the-nvidia-h100-gpu-cost-in-2025-buy-vs-rent-analysis), [Introl GPU financing guide](https://introl.com/blog/ai-infrastructure-financing-capex-opex-gpu-investment-guide-2025), [IntuitionLabs pricing guide](https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide)

Enterprise support contracts for 8-GPU systems run an additional [$20,000–$50,000 annually](https://www.gmicloud.ai/blog/how-much-does-the-nvidia-h100-gpu-cost-in-2025-buy-vs-rent-analysis).

### 1.2 Procurement Lead Times

[GPU procurement lead times have improved from 2023–2024 peaks exceeding 40 weeks but remain at a 5–6 month industry average as of 2025](https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis). [Tom's Hardware reporting confirmed H100 lead times dropped from 4+ months to 8–12 weeks for some configurations](https://www.tomshardware.com/pc-components/gpus/nvidias-h100-ai-gpu-shortages-ease-as-lead-times-drop-from-up-to-four-months-to-8-12-weeks), though these improvements are configuration- and vendor-dependent. Pre-owned H100 and A100 servers are available for shipment within 3 business days as an alternative path, with corresponding trade-offs in warranty coverage.

[A contingency reserve of 30–40% is recommended in procurement budgets to account for budget-cycle misalignment with GPU procurement timelines](https://introl.com/blog/ai-infrastructure-financing-capex-opex-gpu-investment-guide-2025).

### 1.3 Hardware Refresh Cycles and Depreciation

[NVIDIA releases new GPU architectures every 12–18 months, creating tension with accounting depreciation schedules](https://siliconangle.com/2025/11/22/resetting-gpu-depreciation-ai-factories-bend-dont-break-useful-life-assumptions/). Industry positions as of 2025:

- **Hyperscalers (AWS, Google Cloud, Azure):** Settled on 6-year depreciation cycles
- **AI-native providers:** Lambda Labs 5 years; Nebius 4 years; CoreWeave 6 years
- **Amazon reversal (January 2025):** Amazon revised estimates for a subset of servers from 6 to 5 years, citing "increased pace of technology development, particularly in AI and machine learning"

[Practical operational refresh cycles differ from accounting depreciation: training clusters typically require 2–3 year refresh cycles for competitive capability, while production inference workloads support 4–5 year cycles](https://introl.com/blog/gpu-depreciation-strategies-asset-lifecycle-optimization-guide-2025).

[Prior GPU generations lost 40–60% of market value within 18–24 months of successor launch](https://introl.com/blog/ai-infrastructure-financing-capex-opex-gpu-investment-guide-2025), making resale value recovery unpredictable for ISVs that attempt hardware rotation.

---

## 2. Hypervisor Management

### 2.1 Platform Landscape

Three primary hypervisor platforms are relevant for on-premises AI workloads in 2025:

**VMware (now Broadcom-owned)**
Post-acquisition licensing changes have caused significant disruption. [Gartner's Peer Community survey found 74% of IT leaders are currently exploring VMware alternatives, with Gartner predicting 35% of VMware workloads will migrate to alternative platforms by 2028](https://broadcomaudits.com/vmware-licensing-changes-explained-2025-2026-update-for-enterprises/). [Customers have reported 8x–15x price increases, with smaller organizations seeing 350–450% increases due to new core-minimum licensing tiers](https://broadcomaudits.com/vmware-licensing-changes-explained-2025-2026-update-for-enterprises/). [Broadcom consolidated approximately 168 product bundles into 4 SKUs](https://broadcomaudits.com/vmware-licensing-changes-explained-2025-2026-update-for-enterprises/), fundamentally altering the procurement model.

**KVM / Proxmox**
[In 2025–2026, the performance gap between KVM (the Proxmox core) and VMware ESXi has become minimal — approximately 90% of standard scenarios show no measurable difference in application execution speed](https://monovm.com/blog/vmware-vs-proxmox/). Proxmox supports GPU passthrough and PCIe device assignment natively, which are [critical for AI, ML, and high-performance computing workloads](https://www.horizoniq.com/blog/proxmox-vs-hyper-v/). [Proxmox provides approximately 90% of VMware functionality at a fraction of the licensing cost, with built-in clustering, Ceph, ZFS, and backup tools](https://wehaveservers.com/blog/linux-sysadmin/proxmox-vs-vmware-cost-features-and-migration-tips/).

GPU passthrough on Proxmox/KVM requires IOMMU enablement, VT-d/AMD-Vi support in the CPU and motherboard, VFIO driver binding on the host, and q35 machine type configuration — all requiring deliberate engineering effort but well-documented as of [2025 Proxmox community guidance](https://forum.proxmox.com/threads/2025-proxmox-pcie-gpu-passthrough-with-nvidia.169543/).

### 2.2 Hypervisor Operational Requirements

Key hypervisor management tasks for AI workloads:

- **Driver and firmware patching:** Coordinating CUDA driver updates across hypervisor and guest OS layers without breaking model serving (see Section 3.2)
- **Resource allocation:** CPU/memory pinning, NUMA topology alignment for GPU-adjacent memory access, large-page configuration
- **Live migration:** VMware vMotion and KVM live migration both require shared storage; GPU-passthrough VMs cannot live-migrate without specialized vGPU solutions (NVIDIA vGPU on Proxmox requires a commercial license)
- **HA clustering:** Requires shared storage backend and heartbeat networking; GPU-passthrough VMs typically require cold failover rather than live migration

---

## 3. GPU Management

### 3.1 Multi-Tenant GPU Sharing

[NVIDIA Multi-Instance GPU (MIG) expands performance and value of Blackwell and Hopper generation GPUs (including H100 and A100), allowing partition into as many as seven isolated instances, each with its own high-bandwidth memory, cache, and compute cores](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/). [Each instance has separate and isolated paths through the entire memory system — on-chip crossbar ports, L2 cache banks, memory controllers, and DRAM address buses are all assigned uniquely — ensuring predictable throughput and latency](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html).

Three sharing mechanisms available in 2025:

| Mechanism | Isolation Level | Partitions Per GPU | Best For |
|-----------|----------------|-------------------|----------|
| MIG (Multi-Instance GPU) | Hardware-isolated | Up to 7 | Multi-tenant SaaS with QoS guarantees |
| MPS (Multi-Process Service) | Process-level | Configurable | Co-located training jobs with trust |
| Time-slicing | None (temporal) | Configurable | Dev/test, non-production |

[MIG can be used on-premises, in the cloud, and at the edge, with support for containerized applications, Kubernetes pods, and applications running inside virtual machines](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/).

### 3.2 CUDA Version Management

[NVIDIA offers multiple compatibility approaches for enterprise GPU deployments](https://docs.nvidia.com/deploy/cuda-compatibility/):

- **Minor Version Compatibility (CUDA 11+):** Applications compiled with a CUDA Toolkit release within a major release family can run on systems with the minimum required driver version, allowing library upgrades without full driver upgrades
- **Forward Compatibility:** Enables applications built with newer toolkits to run on older base drivers across major release families via a `cuda-compat` package

[The NVIDIA computational stack — CUDA drivers, CUDA libraries, cuDNN, TensorRT — forms the backbone of enterprise AI deployments](https://nstarxinc.com/blog/managing-nvidia-driver-compatibility-across-multi-framework-ai-environments/). On-premises operators must manage the driver-toolkit-framework compatibility matrix across potentially heterogeneous GPU hardware generations, which becomes acutely complex when multiple AI frameworks (PyTorch, TensorFlow, TensorRT) run simultaneously on the same cluster.

[CUDA Toolkit 13.1 is the current release as of late 2025](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html), with forward compatibility allowing older installed drivers to support applications compiled against newer CUDA versions — a critical operational feature for ISVs shipping software to customer-managed on-premises environments.

### 3.3 GPU Failure Rates

[General data center GPU failure rates for enterprise-grade hardware range between 0.1% and 2% per year depending on usage conditions](https://cyfuture.cloud/kb/gpu/what-is-the-failure-rate-of-the-h100-gpu). Estimated annual failure rates by generation:

| GPU Model | Estimated Annual Failure Rate |
|-----------|------------------------------|
| NVIDIA V100 | ~1.5% |
| NVIDIA A100 | 0.8%–1.2% |
| NVIDIA H100 | <0.8% (estimated) |

Note: [NVIDIA does not publicly disclose specific failure rates](https://cyfuture.cloud/kb/gpu/what-is-the-failure-rate-of-the-h100-gpu). These estimates are derived from vendor and operator reporting, not official NVIDIA documentation.

---

## 4. Resource Scheduling

### 4.1 Scheduler Options for On-Premises GPU Workloads

Without a cloud provider's managed scheduler, on-premises operators must choose between three primary approaches:

**Slurm (now NVIDIA-owned)**
[NVIDIA acquired SchedMD, the developer of Slurm, in December 2025](https://www.networkworld.com/article/4106930/nvidia-moves-deeper-into-ai-infrastructure-with-schedmd-acquisition.html). [NVIDIA confirmed Slurm will remain open source and hardware-agnostic](https://developer.nvidia.com/slurm). Slurm supports GPU scheduling as a consumable Generic Resource (GRES), with built-in support for CUDA MPS and MIG partitioning. [Slurm is "built with hardware topology in mind" and understands physical cluster layout, GPU interconnect topology, and can allocate tightly coupled resources for distributed workloads](https://nebius.com/blog/posts/slurm-workload-manager).

[Slurm's core strengths are deterministic scheduling, direct hardware control, and job queuing logic optimized for maximizing utilization in static environments like dedicated GPU clusters or on-premises infrastructure](https://www.whitefiber.com/blog/slurm-vs-kubernetes).

**HashiCorp Nomad**
Nomad provides a general-purpose workload orchestrator capable of scheduling GPU tasks with device plugin support. It bridges bare-metal and containerized workloads, supporting both batch jobs and long-running services — a useful property for ISVs running mixed training and inference workloads. Nomad requires less operational overhead than Kubernetes but less GPU-native sophistication than Slurm.

**Manual / Custom Scheduling**
At small scale (fewer than 50 GPUs), teams sometimes rely on manual queue management or bespoke scripts. This approach is operationally fragile and does not scale beyond single-team usage.

### 4.2 Scheduler Comparison

| Factor | Slurm | Nomad | Manual |
|--------|-------|-------|--------|
| GPU awareness | Native GRES + MIG/MPS | Plugin-based | None |
| Deterministic scheduling | Yes | Partial | N/A |
| Mixed workloads (batch + service) | Batch-primary | Yes | No |
| Operational complexity | Moderate | Low-Moderate | Low (initially) |
| Recommended scale | 100+ GPUs | 20–500 GPUs | <20 GPUs |

---

## 5. Auto-Scaling (or Lack Thereof)

On-premises compute has no native auto-scaling equivalent to cloud elasticity. Three strategies are used in practice:

**Pre-provisioning (static over-provisioning)**
Organizations purchase peak-capacity hardware upfront. [Buffer capacity of 20–30% above average load is typically maintained to handle demand spikes and growth](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030). This directly reduces effective utilization rates (see Section 8) and increases TCO.

**Burst to Cloud (Hybrid)**
[Public cloud handles variable training workloads, burst capacity needs, and experimentation phases](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/ai-infrastructure-compute-strategy.html). ISVs operating on-premises for production inference can route overflow or batch training jobs to cloud GPU providers at $2.10–$8.00/GPU-hour. This requires a unified control plane that spans on-premises systems and cloud APIs.

**Demand Management**
Rather than scaling hardware, on-premises operators implement demand-side controls: request queuing, priority tiers, rate limiting per tenant, and scheduled batch windows. This is operationally effective but surfaces to customers as degraded responsiveness during peak periods.

[Hardware procurement lead times of 5–6 months mean on-premises capacity cannot respond to demand signals the way cloud resources can](https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis). [Meta's infrastructure team underestimated GPU requirements by 400% in 2023, forcing emergency procurement of 50,000 H100s at premium prices that added $800 million to their AI budget](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030) — a cautionary benchmark for ISVs planning on-premises AI capacity.

---

## 6. High Availability

### 6.1 Redundancy Architecture

On-premises HA for GPU compute requires hardware redundancy at multiple layers:

- **Power:** Redundant power supplies per server (N+1 or 2N), UPS systems, generator backup for facility-level outage protection
- **Network:** Dual NIC bonding/LACP for data paths; dedicated out-of-band management (IPMI/iDRAC/iLO) for remote recovery
- **Compute:** Warm standby nodes (idle but powered) or N+1 GPU node pools; GPU-passthrough VMs typically cannot live-migrate and require cold failover
- **Cooling:** Redundant cooling units; monitoring and alerting on thermal thresholds

### 6.2 Failure and Recovery Metrics

[Leading on-premises GPU cluster operators achieve MTTR of 12 minutes or less through end-to-end automation of the recovery process, from early-stage fault diagnosis to spinning up replacement nodes without human intervention](https://www.cudocompute.com/blog/enhance-hardware-reliability-for-ai-acceleration-at-scale). [Redundancy and warm-pooling can reduce median MTTR to under 2 minutes, with p99 latency excursions under 15 ms on 96% of faults](https://www.cudocompute.com/blog/enhance-hardware-reliability-for-ai-acceleration-at-scale) — though these figures represent best-in-class managed environments, not typical ISV self-managed deployments.

For ISV-managed on-premises environments, realistic MTTR targets without dedicated automation engineering are 30–120 minutes for GPU node failures, depending on spare parts availability and staffing coverage.

[Effective capacity must account for 10–15% reduction due to maintenance windows and hardware failures](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030).

### 6.3 Maintenance Windows

Unlike cloud managed services, on-premises infrastructure requires planned maintenance windows for:
- Firmware and BIOS updates (coordinated across hypervisor, BMC, GPU)
- CUDA driver upgrades (requiring workload quiescing on affected nodes)
- Physical hardware inspection, cleaning, and component replacement
- Data center facility maintenance (UPS testing, generator runs, cooling service)

---

## 7. Power, Cooling, and Physical Infrastructure

### 7.1 Power Density Requirements

[Modern AI GPUs consume 700–1,200 watts per chip versus 150–200 watts for traditional CPUs](https://www.hanwhadatacenters.com/blog/what-are-the-power-requirements-for-ai-data-centers/). Rack-level implications:

| Infrastructure Type | Power per Rack |
|--------------------|---------------|
| Traditional data center | 8–15 kW |
| AI GPU server rack | 30–80 kW |
| High-density AI rack (H100 8-GPU server) | 50–150 kW |

[Average power density is anticipated to increase from 36 kW per server rack in 2023 to 50 kW per rack by 2027](https://www.hanwhadatacenters.com/blog/what-are-the-power-requirements-for-ai-data-centers/). Most existing enterprise data center facilities were designed for 8–15 kW/rack and cannot support GPU-dense workloads without significant infrastructure investment.

### 7.2 Cooling Requirements

[Advanced cooling technologies (direct liquid cooling, immersion cooling) reduce cooling energy by 30–40% compared to traditional air cooling](https://www.hanwhadatacenters.com/blog/what-are-the-power-requirements-for-ai-data-centers/). PUE comparison:

| Facility Type | Typical PUE |
|--------------|-------------|
| Traditional enterprise data center | 1.5–1.6 |
| Hyperscale cloud (e.g., AWS 2024) | 1.1–1.2 |
| Well-designed on-premises AI facility | 1.3–1.5 (achievable) |

[The liquid cooling market will expand from $4.5 billion in 2025 to over $21.8 billion by 2032](https://mlq.ai/research/data-center-cooling/), reflecting the industry-wide recognition that air cooling is insufficient for AI-density workloads.

### 7.3 Facility Upgrade Costs

For ISVs deploying GPU infrastructure in existing facilities, capital expenditures beyond hardware include:

- **Electrical infrastructure upgrades:** 3-phase power distribution, PDUs, UPS capacity
- **Cooling upgrades:** Precision air conditioning, CRAC units, or liquid cooling installation
- **Physical security:** Biometric access, CCTV, equipment caging
- **Network cabling:** High-speed InfiniBand or RoCE networking for GPU-to-GPU interconnect (see F40 for networking scope)

[Data center modifications for AI GPU deployments typically cost $25,000–$100,000 for a medium-scale deployment](https://www.swfte.com/blog/private-ai-enterprises-onprem-economics), though larger-scale deployments can require millions in facility upgrades.

---

## 8. Cost Model: CapEx vs. OpEx

### 8.1 Total Cost of Ownership Components

For a medium-scale on-premises deployment (assumptions: 50 enterprise customers, ~200 GPUs, 3-year horizon):

**Initial Capital Investment (CapEx):**

| Component | Cost Range |
|-----------|-----------|
| GPU infrastructure (200 H100s) | $5,000,000–$8,000,000 |
| Networking and storage | $500,000–$1,500,000 |
| Data center modifications | $250,000–$1,000,000 |
| Software licensing (hypervisor, monitoring) | $200,000–$1,000,000 |
| **Total CapEx** | **$5,950,000–$11,500,000** |

Source: Derived from per-unit pricing at [GMI Cloud](https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis) and [Swfte AI medium-scale model](https://www.swfte.com/blog/private-ai-enterprises-onprem-economics)

**Annual Operating Expenses (OpEx):**

| Component | Annual Cost Range |
|-----------|------------------|
| Power and cooling | $300,000–$800,000 |
| Staff (see Section 8.3) | $600,000–$1,200,000 |
| Hardware maintenance | $200,000–$500,000 |
| Software updates and licensing | $100,000–$500,000 |
| **Total Annual OpEx** | **$1,200,000–$3,000,000** |

### 8.2 Break-Even vs. Cloud

[At 80% utilization over a 3-year horizon, owned infrastructure costs approximately $0.48/GPU-hour versus $0.75/GPU-hour for cloud GPU-as-a-service](https://introl.com/blog/ai-infrastructure-financing-capex-opex-gpu-investment-guide-2025). [Break-even occurs at 60–70% sustained utilization](https://www.swfte.com/blog/private-ai-enterprises-onprem-economics).

[For a server with 8x H100 GPUs, the break-even point versus cloud pricing is approximately 8,556 hours (~11.9 months of full utilization)](https://lenovopress.lenovo.com/lp2225-on-premise-vs-cloud-generative-ai-total-cost-of-ownership). [Purchase is only cost-competitive above 10,000 GPU-hours monthly sustained for 3+ years — a threshold most organizations do not reach](https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis).

**5-Year TCO Comparison (medium-scale deployment)**

| Category | Cloud (Annual) | On-Premises (Annual) |
|----------|---------------|----------------------|
| Infrastructure | $0 | $1,500,000–$2,300,000 (amortized CapEx) |
| Compute (GPU-hours) | $3,000,000–$6,000,000 | $400,000–$800,000 (power + ops) |
| Operations staff | $500,000–$1,000,000 | $600,000–$1,200,000 |
| Software licensing | $500,000–$1,000,000 | $100,000–$500,000 |

Source: Adapted from [Swfte AI 5-year comparison model](https://www.swfte.com/blog/private-ai-enterprises-onprem-economics)

### 8.3 Staffing FTE Estimates

Assumptions: Mid-size deployment, 200 GPUs, 50 enterprise customers, production AI-SaaS

[Industry benchmark: approximately 10 specialized engineers per 1,000 GPUs for operations](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030), scaling to approximately 2 FTE per 200 GPUs for baseline operations. [Cost breakdown for typical deployments is 60% hardware, 25% operations, 15% software](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030).

| Function | Est. FTE | Notes |
|----------|----------|-------|
| Hardware operations (racking, cabling, replacement) | 0.5–1.0 FTE | Scales with failure rate and expansion |
| Hypervisor administration | 0.5–1.0 FTE | Patching, provisioning, HA management |
| GPU/CUDA management | 0.5–1.0 FTE | Driver versions, MIG config, monitoring |
| Scheduler operations (Slurm/Nomad) | 0.25–0.5 FTE | Job config, queue management |
| Capacity planning | 0.25–0.5 FTE | Procurement planning, utilization analysis |
| On-call burden (after-hours hardware incidents) | 0.5–1.0 FTE equivalent | Rotation across above staff |
| **Total** | **2.5–5.0 FTE** | Excludes software development and networking |

Comparable cloud-native operational staffing for equivalent compute capacity: 0.5–1.5 FTE (platform configuration and cost optimization only). See F40 and Wave 7 for networking and Kubernetes staffing.

---

## 9. Deployment Model Comparison

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| **Hardware procurement** | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | 5–6 month lead times, CapEx $5M+ | Cloud provider handles; ISV manages nodes | Instant provisioning |
| | Vendor contracts, capacity forecasting | Node pool configuration | API-driven |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **Hypervisor management** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | KVM/Proxmox/VMware; patching, NUMA config | Managed control plane; node OS patching | None |
| | Live migration constraints for GPU VMs | EKS/AKS/GKE node management | Fully managed |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0 |
| **GPU management (MIG/CUDA)** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Full driver stack ownership; MIG config | GPU operator (NVIDIA); MIG via K8s device plugin | Managed GPU instances |
| | CUDA compat matrix management | Operator-managed driver updates | Provider-managed |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Resource scheduling** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Slurm/Nomad; manual queue management | Kubernetes scheduler + custom resource definitions | Managed autoscaler |
| | No elastic scaling | Cluster autoscaler | Built-in |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Burst/auto-scaling** | Difficulty: 5/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Not available; pre-provision or cloud burst | Cluster autoscaler; node pool scaling | Instant; pay-per-use |
| | 5–6 month hardware lead time | Minutes to hours | Seconds to minutes |
| | Est. FTE: 0.25 (planning only) | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **High availability** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Manual redundancy engineering; cold failover for GPU VMs | Managed control plane HA; node pool redundancy | Multi-AZ by default |
| | MTTR 30–120 min (typical ISV) | MTTR 5–15 min | MTTR <5 min (managed SLAs) |
| | Est. FTE: included in hardware ops | Est. FTE: 0.1–0.25 | Est. FTE: 0.0 |
| **Power and cooling** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Facility upgrades required; PUE 1.3–1.5 achievable | Co-lo or cloud DC; included in node cost | Provider-managed |
| | $25K–$100K+ facility CapEx | Included in node pricing | None |
| | Est. FTE: 0.1–0.25 (vendor coordination) | Est. FTE: 0.0 | Est. FTE: 0.0 |
| **Total Est. FTE** | **2.5–5.0 FTE** | **1.0–2.25 FTE** | **0.2–0.5 FTE** |

---

## 10. GPU Utilization: The Critical Variable

[Industry benchmarks target 65–75% average GPU utilization for efficient on-premises operations](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030). Actual utilization by workload type:

- **Inference workloads:** 40–50% typical due to request variability
- **Training workloads:** 90–95% achievable with careful orchestration
- **Mixed production deployments:** 55–70% with good scheduling discipline

[Standardization increased GPU utilization 20% at Salesforce; multi-tenancy raised utilization from 45% to 70% at eBay — both achieved via scheduling optimization, not hardware changes](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030).

[Effective capacity is reduced 10–15% due to maintenance windows and hardware failures](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030), meaning a target of 70% utilization requires achieving 80–82% gross utilization before maintenance deductions.

---

## Key Takeaways

- **Lead times and CapEx create irreversible planning commitments.** GPU server procurement averages 5–6 months lead time with $300,000–$450,000 per 8-GPU system. An ISV serving 50 enterprise customers on-premises should budget $5–15 million in CapEx before production launch, and treat hardware procurement as a 12–18 month continuous planning function, not a one-time purchase event.

- **The 60–70% utilization threshold is the financial pivot point.** On-premises compute achieves a cost advantage over cloud GPU-as-a-service only at sustained 60–70%+ utilization over 3+ years. Below this threshold — which inference-only workloads frequently fail to sustain — cloud is cheaper on a per-GPU-hour basis. ISVs must model their workload utilization patterns before committing to on-premises CapEx.

- **Hypervisor choices carry long-term licensing risk.** VMware's post-acquisition pricing model has delivered 8–15x cost increases for enterprise customers. ISVs building new on-premises deployments in 2025 should default to KVM/Proxmox (which now matches VMware performance in ~90% of scenarios) unless VMware-specific enterprise features are contractually required by customers.

- **Operational staffing of 2.5–5.0 FTE is non-negotiable for a 200-GPU production cluster.** This excludes networking and Kubernetes staffing. The "hidden" operational cost of on-premises compute is frequently underestimated in ISV business cases; staffing at $150,000–$300,000 per engineer represents $375,000–$1,500,000 in annual labor costs that have no cloud equivalent.

- **GPU MIG partitioning is the technical prerequisite for on-premises multi-tenancy.** Hardware-isolated MIG instances on H100 provide the QoS guarantees required to safely serve multiple enterprise tenants from shared physical GPUs. Configuring and maintaining MIG profiles adds operational complexity but is the only mechanism that prevents noisy-neighbor interference at the hardware level in a self-managed environment.

---

## Related — Out of Scope

The following topics surfaced during research but are outside the F39 scope boundary and should not be investigated here:

- **GPU networking (InfiniBand, RoCE, NVLink):** See F40 — On-Prem Networking
- **Persistent storage for model weights and datasets:** See F43 — On-Prem Storage
- **Kubernetes workload orchestration on-premises:** Covered in Wave 7
- **Colocation vs. owned data center trade-offs:** Partially overlaps F39 but primarily an infrastructure strategy question for the broader ISV deployment model analysis

---

## Sources

1. [GMI Cloud — H100 GPU Pricing 2025: Cloud vs. On-Premise Cost Analysis](https://www.gmicloud.ai/blog/h100-gpu-pricing-2025-cloud-vs-on-premise-cost-analysis)
2. [GMI Cloud — How Much Does the NVIDIA H100 GPU Cost in 2025? Buy vs. Rent](https://www.gmicloud.ai/blog/how-much-does-the-nvidia-h100-gpu-cost-in-2025-buy-vs-rent-analysis)
3. [GMI Cloud — 2025 Cost of Renting or Buying NVIDIA H100 GPUs for Data Centers](https://www.gmicloud.ai/blog/2025-cost-of-renting-or-uying-nvidia-h100-gpus-for-data-centers)
4. [Tom's Hardware — NVIDIA H100 Lead Times Drop from 4 Months to 8–12 Weeks](https://www.tomshardware.com/pc-components/gpus/nvidias-h100-ai-gpu-shortages-ease-as-lead-times-drop-from-up-to-four-months-to-8-12-weeks)
5. [Introl — AI Infrastructure Capacity Planning: Forecasting GPU Requirements 2025–2030](https://introl.com/blog/ai-infrastructure-capacity-planning-forecasting-gpu-2025-2030)
6. [Introl — AI Infrastructure Financing: CapEx, OpEx, and GPU Investment Guide 2025](https://introl.com/blog/ai-infrastructure-financing-capex-opex-gpu-investment-guide-2025)
7. [Introl — GPU Depreciation Strategies: Optimizing Asset Lifecycles](https://introl.com/blog/gpu-depreciation-strategies-asset-lifecycle-optimization-guide-2025)
8. [SiliconAngle — Resetting GPU Depreciation: AI Factories Bend, But Don't Break, Useful Life Assumptions](https://siliconangle.com/2025/11/22/resetting-gpu-depreciation-ai-factories-bend-dont-break-useful-life-assumptions/)
9. [NVIDIA — Multi-Instance GPU (MIG) Technology Overview](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/)
10. [NVIDIA — MIG User Guide (Official Documentation)](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/introduction.html)
11. [NVIDIA — CUDA Compatibility Documentation](https://docs.nvidia.com/deploy/cuda-compatibility/)
12. [NVIDIA — CUDA Toolkit Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
13. [NStarX — Managing NVIDIA Driver Compatibility Across Multi-Framework AI Environments](https://nstarxinc.com/blog/managing-nvidia-driver-compatibility-across-multi-framework-ai-environments/)
14. [MonoVM — VMware vs Proxmox: Which Virtualization Platform Should You Choose in 2026?](https://monovm.com/blog/vmware-vs-proxmox/)
15. [WeHaveServers — Proxmox vs VMware: Cost, Features, and Migration Tips](https://wehaveservers.com/blog/linux-sysadmin/proxmox-vs-vmware-cost-features-and-migration-tips/)
16. [HorizonIQ — Proxmox vs Hyper-V: Which Hypervisor is Right for Your Business?](https://www.horizoniq.com/blog/proxmox-vs-hyper-v/)
17. [BroadcomAudits — VMware Licensing Changes Explained: 2025–2026 Update for Enterprises](https://broadcomaudits.com/vmware-licensing-changes-explained-2025-2026-update-for-enterprises/)
18. [Proxmox Forum — 2025: Proxmox PCIe / GPU Passthrough with NVIDIA](https://forum.proxmox.com/threads/2025-proxmox-pcie-gpu-passthrough-with-nvidia.169543/)
19. [WhiteFiber — Slurm vs. Kubernetes for AI/ML Workloads in 2025](https://www.whitefiber.com/blog/slurm-vs-kubernetes)
20. [Network World — NVIDIA Moves Deeper into AI Infrastructure with SchedMD Acquisition](https://www.networkworld.com/article/4106930/nvidia-moves-deeper-into-ai-infrastructure-with-schedmd-acquisition.html)
21. [NVIDIA Developer — Slurm](https://developer.nvidia.com/slurm)
22. [Nebius — Slurm Workload Manager: The Go-To Scheduler for HPC and AI Workloads](https://nebius.com/blog/posts/slurm-workload-manager)
23. [Hanwha Data Centers — What Are the Power Requirements for AI Data Centers?](https://www.hanwhadatacenters.com/blog/what-are-the-power-requirements-for-ai-data-centers/)
24. [MLQ.ai — AI Data Center Cooling Research](https://mlq.ai/research/data-center-cooling/)
25. [Swfte AI — Private AI for Enterprises: On-Prem Economics and the 60% Cost Threshold](https://www.swfte.com/blog/private-ai-enterprises-onprem-economics)
26. [CyfutureCloud — What Is the Failure Rate of the H100 GPU?](https://cyfuture.cloud/kb/gpu/what-is-the-failure-rate-of-the-h100-gpu)
27. [Cudo Compute — Optimizing Hardware Reliability for AI Acceleration](https://www.cudocompute.com/blog/enhance-hardware-reliability-for-ai-acceleration-at-scale)
28. [Lenovo Press — On-Premise vs Cloud: Generative AI Total Cost of Ownership (2025 Edition)](https://lenovopress.lenovo.com/lp2225-on-premise-vs-cloud-generative-ai-total-cost-of-ownership)
29. [Deloitte — The AI Infrastructure Reckoning: Optimizing Compute Strategy in the Age of Inference Economics](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/ai-infrastructure-compute-strategy.html)
30. [IntuitionLabs — NVIDIA AI GPU Prices: H100 and H200 Cost Guide](https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide)
