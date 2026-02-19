# W10S — Cross-Cutting Gaps: Compliance, AI Safety, Training, DR, and Security Operations

**Wave:** 10 | **Scope:** Cross-cutting domains that span multiple infrastructure layers
**Date:** 2026-02-19 | **Inputs:** F67, F68, F69, F70, F71

---

## 1. Executive Summary

Wave 10 examines five domains -- compliance/regulatory, AI safety guardrails, model training/fine-tuning, disaster recovery, and security operations -- that do not sit neatly within any single infrastructure layer but instead compound across the entire deployment stack. The central finding is that on-premises deployment creates a multiplicative burden: each cross-cutting domain demands its own parallel infrastructure, specialized staff, and tooling portfolio, and the interactions between domains (e.g., compliance audit logs depending on security operations SIEM, DR requiring GPU-specific checkpoint strategies that intersect training infrastructure) generate complexity that grows faster than the sum of its parts. Cloud-native managed services collapse much of this operational surface area into pay-per-use APIs, but at the cost of data sovereignty control and vendor dependency that may be non-negotiable for regulated ISV deployments.

---

## 2. Key Themes

### Theme 1: The On-Premises Staffing Multiplier -- Specialized FTE Demands Compound Across Domains

The most consistent signal across all five Wave 10 agents is that on-premises deployment does not merely require more staff -- it requires more categories of specialized staff. Compliance operations alone demand [2.5-4.0 FTE](https://facit.ai/insights/cloud-based-vs-on-premises-security-and-compliance) (from F67). AI safety guardrails -- operating a parallel GPU inference stack for content filtering, PII detection, and prompt injection defense -- require [2.25-3.75 FTE](https://moderationapi.com/blog/how-to-self-host-use-llama-guard-3/) (from F68). Model training and fine-tuning demand [2-4 dedicated MLOps FTEs](https://www.crowdee.com/blog/posts/self-hosting-ai-costs) (from F69). Disaster recovery requires [1.5-2.5 FTE active plus 0.5-1.0 FTE on-call](https://secureframe.com/blog/disaster-recovery-cost) (from F70). Security operations require [2.75-5.5 FTE excluding SOC analysts](https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center), with a basic 24/7 SOC adding [12 FTE at $1.5M annually](https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center) (from F71).

A naive sum of on-premises FTE across Wave 10 yields approximately 11-20 FTE (excluding SOC analysts). However, this aggregate must be treated with caution due to overlap between domains -- see Section 4 on double-counting. Cloud-native deployment reduces each domain's FTE by 60-80%, collapsing the aggregate to approximately 2-4 FTE plus policy and documentation work that remains ISV-owned regardless of model.

### Theme 2: GPU Infrastructure as the Hidden Tax on AI-Specific Cross-Cutting Functions

Three of the five Wave 10 domains require dedicated GPU capacity on-premises, creating an infrastructure tax that has no parallel in traditional enterprise software. AI safety guardrails require [dedicated A10G GPUs per Llama Guard 3 instance (20 GB VRAM minimum)](https://huggingface.co/meta-llama/Llama-Guard-3-8B), and running six simultaneous guardrail policies requires [six GPUs](https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance) (from F68). Model fine-tuning on a 70B-parameter model requires [eight A100 80 GB GPUs for full fine-tuning](https://www.runpod.io/blog/llm-fine-tuning-gpu-guide), though [QLoRA reduces a 70B model to a single H100](https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025) (from F69). Disaster recovery for GPU clusters demands [5% overprovisioning to handle failures](https://newsletter.semianalysis.com/p/100000-h100-clusters-power-network), with H100 units costing [$25-40K each](https://introl.com/blog/disaster-recovery-ai-infrastructure-rpo-rto-strategies-gpu-clusters) (from F70). NVIDIA research documents that robust guardrail implementation can [triple both latency and cost](https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance) relative to unguarded inference (from F68). The compounding effect is clear: an on-premises ISV must procure, manage, and provide DR for separate GPU pools serving inference, safety, and training workloads.

### Theme 3: Regulatory Pressure Creates Compliance Obligations That Are Deployment-Model-Agnostic but Operationally Deployment-Model-Dependent

The EU AI Act, GDPR, HIPAA, and FedRAMP impose obligations regardless of where workloads run, but the operational cost of meeting those obligations varies dramatically by deployment model. [FedRAMP authorization costs $400K-$2M](https://secureframe.com/hub/fedramp/costs) for cloud-deployed ISVs targeting the US federal market (from F67), while on-premises deployments enter via the FISMA path. The [EU AI Act GPAI transparency obligations became mandatory August 2, 2025](https://www.dlapiper.com/en-us/insights/publications/2025/08/latest-wave-of-obligations-under-the-eu-ai-act-take-effect), with high-risk system requirements phasing in by 2027 (from F67). These requirements demand technical documentation, audit trails, and human oversight mechanisms that F68 identifies as requiring [dedicated guardrail audit logging infrastructure](https://www.infoguard.ch/en/blog/ai-act-eu-guardrails-secure-ai-deployment) on-premises. Cloud-native deployments inherit [143 security standards and compliance certifications from AWS alone](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/security-and-compliance.html) (from F67), reducing audit evidence collection from a [5/5 difficulty task to 2/5](https://blog.qualys.com/product-tech/2026/01/29/top-10-cloud-compliance-tools-for-enterprise-security-and-audit-readiness-in-2026) (from F67). Yet even with cloud-native, ISVs still own all application-layer controls, EU AI Act obligations, and legal basis for data processing (from F67).

### Theme 4: Disaster Recovery for AI Workloads Demands Domain-Specific Planning That Compounds Standard DR Complexity

DR for AI-enabled SaaS is not a single problem. F70 documents that [AI workloads require disaggregated DR planning](https://introl.com/blog/disaster-recovery-ai-infrastructure-rpo-rto-strategies-gpu-clusters) with distinct RPO/RTO profiles: production inference at 5-minute RPO / 15-minute RTO, training jobs at 2-4 hour RPO / 4-8 hour RTO, and model registries at 24-hour RPO / 1-hour RTO (from F70). On-premises DR [consumes 15-25% of total IT budget](https://www.serverion.com/uncategorized/cloud-vs-on-premises-disaster-recovery-differences/) (from F70). Modern 70B model checkpoints are [150-200 GB each](https://introl.com/blog/disaster-recovery-ai-infrastructure-rpo-rto-strategies-gpu-clusters), and checkpoint corruption has caused [multi-million-dollar training loss events](https://introl.com/blog/disaster-recovery-ai-infrastructure-rpo-rto-strategies-gpu-clusters) (from F70). This DR burden interacts directly with F69's training infrastructure (checkpoint management), F68's safety model versioning (guardrail model failover), and F71's SIEM/forensics infrastructure (evidence preservation during incidents). Cloud-native DR tools like [Aurora Global Database with sub-1-second replication and sub-1-minute promotion](https://aws.amazon.com/rds/aurora/global-database/) (from F70) collapse much of the data-tier DR difficulty, but GPU cluster failover remains difficult (3/5) even in cloud-native environments (from F70).

### Theme 5: Security Operations and Compliance Form an Inseparable Operational Loop That Is Most Expensive On-Premises

F67 and F71 reveal that compliance and security operations are not independent domains but a tightly coupled loop: compliance requires continuous audit logs, evidence collection, and monitoring (F67), which are produced by SIEM, IDS/IPS, and runtime security systems (F71). The [2025 SANS SOC Survey reports 73% of organizations cite false positives as their top detection challenge](https://www.stamus-networks.com/blog/what-the-2025-sans-detection-response-survey-reveals-false-positives-alert-fatigue-are-worsening) (from F71), and [42% of SOCs ingest all data without a defined strategy](https://swimlane.com/blog/global-soc-survey-insights/) (from F71) -- a problem that directly undermines the compliance evidence quality F67 requires. On-premises, this loop demands its own toolchain: Wazuh or Splunk for SIEM, Suricata for IDS/IPS, Falco for runtime security, MISP for threat intelligence, and Trivy/Grype for container scanning (from F71), alongside OPA/Gatekeeper and GRC platforms for policy enforcement (from F67). Microsoft Sentinel is cited as [67% faster to deploy than on-premises SIEM](https://www.digitalxraid.com/blog/microsoft-sentinel-vs-microsoft-defender/) (from F71), illustrating the operational gap.

---

## 3. Difficulty and FTE Summary Table

| Domain | On-Premises Difficulty | On-Premises FTE | Managed K8s Difficulty | Managed K8s FTE | Cloud-Native Difficulty | Cloud-Native FTE |
|---|---|---|---|---|---|---|
| Compliance operations (F67) | 5/5 | 2.5-4.0 | 3/5 | 1.25-2.0 | 2/5 | 0.5-1.0 |
| AI safety guardrails (F68) | 4-5/5 | 2.25-3.75 | 3-4/5 | 1.5-2.5 | 1-2/5 | 0.5-1.0 |
| Model training/fine-tuning (F69) | 4-5/5 | 3.75-7.5 | 2-3/5 | 1.85-3.75 | 1-2/5 | 0.35-1.05 |
| Disaster recovery (F70) | 5/5 | 2.0-3.5 | 3/5 | 0.75-1.25 | 2/5 | 0.5-0.75 |
| Security operations (F71) | 4-5/5 | 2.75-5.5 | 3/5 | 2.25-4.5 | 1-2/5 | 0.25-1.2 |
| **Gross Total** | | **13.25-24.25** | | **7.6-14.0** | | **2.1-5.0** |
| **Cautioned Total (see G3 warning)** | | **~10-19** | | **~6-11** | | **~2-4.5** |

**G3 Warning -- FTE Double-Counting:** The gross totals above contain overlap. F71 security operations FTE includes SIEM log management, IDS/IPS rule tuning, and incident response, which overlap with F67 compliance FTE in the areas of audit logging (0.5-1.0 FTE), evidence collection (0.5-0.75 FTE), and continuous monitoring (0.5-1.0 FTE). Additionally, F68 AI safety audit logging overlaps with F67 audit readiness. The cautioned total reduces the gross by approximately 3-5 FTE on-premises to account for shared personnel across compliance, security operations, and AI safety audit functions.

---

## 4. Cross-Agent Patterns and Contradictions

**Consistent patterns across agents:**

- All five agents confirm the 3-5x FTE multiplier between on-premises and cloud-native deployment for their respective domains, with managed Kubernetes occupying a middle position at roughly 50-60% of on-premises burden.
- On-premises deployment is rated 4/5 or 5/5 difficulty in every cross-cutting domain. No Wave 10 domain rated on-premises below 3/5 for any sub-capability.
- [People cost dominates TCO at scale](https://www.crowdee.com/blog/posts/self-hosting-ai-costs) (from F69) -- this pattern is confirmed across all five domains, where staffing consistently outweighs infrastructure cost.

**Tensions and contradictions:**

- **Data sovereignty advantage vs. operational burden:** F67 rates on-premises data sovereignty at 1/5 difficulty (guaranteed by architecture) while every other domain rates on-premises at 4-5/5. The sovereignty advantage is real but narrow -- it solves one regulatory problem while creating many operational ones.
- **QLoRA as a counter-narrative to GPU cost barriers:** F69 documents that [QLoRA enables 70B-class fine-tuning on a single A100 80 GB](https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025) with 80-90% quality recovery, while F68 documents that safety guardrails can [triple inference cost](https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance). The hardware barrier to on-premises training has dropped significantly, but the safety and operational overhead has not.
- **Bias detection gap persists across all models:** F68 notes that [no major cloud provider offers native bias detection as a managed guardrail API](https://www.enkryptai.com/blog/enkrypt-ai-vs-azure-content-safety-vs-amazon-bedrock-guardrails) (from F68) -- this is one domain where cloud-native offers no advantage, and ISVs must operate bias tooling (IBM AIF360, Fairlearn) regardless of deployment model.

---

## 5. Open Questions for Downstream Synthesis

1. **Total on-premises FTE across all waves:** Wave 10 alone produces a cautioned estimate of 10-19 FTE for on-premises cross-cutting operations. How does this aggregate with infrastructure FTE from earlier waves (compute, storage, networking, observability), and does the combined total exceed what a mid-size ISV can realistically staff?

2. **Sovereign cloud as a middle path:** F67 documents the [sovereign cloud market growing from $154B (2025) to $823B by 2032](https://introl.com/blog/sovereign-cloud-ai-infrastructure-data-residency-requirements-2025), with AWS and Microsoft launching EU sovereign offerings. Does sovereign cloud offer a viable path that captures on-premises data sovereignty benefits while avoiding the full on-premises operational burden?

3. **Guardrail cost trajectory:** F68 documents that [Bedrock Guardrails pricing was reduced by up to 85% in December 2024](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-guardrails-reduces-pricing-85-percent/). If managed safety service costs continue to decline, at what point does the economic case for self-hosted guardrails collapse entirely?

4. **DR testing automation as force multiplier:** F70 documents [60-95% improvements in recovery time from DR automation](https://introl.com/blog/disaster-recovery-ai-infrastructure-rpo-rto-strategies-gpu-clusters). Can similar automation approaches be applied to compliance evidence collection and security operations rule tuning to reduce the staffing burden identified in F67 and F71?

5. **SOC analyst retention crisis:** F71 reports [70% of SOC analysts with five years or less experience leave within three years](https://www.stamus-networks.com/blog/what-the-2025-sans-detection-response-survey-reveals-false-positives-alert-fatigue-are-worsening). For an ISV choosing on-premises, is sustained SOC staffing even feasible given labor market dynamics?

---

## 6. Sources

### F67 -- Compliance and Regulatory
- https://facit.ai/insights/cloud-based-vs-on-premises-security-and-compliance
- https://secureframe.com/hub/fedramp/costs
- https://docs.aws.amazon.com/whitepapers/latest/aws-overview/security-and-compliance.html
- https://blog.qualys.com/product-tech/2026/01/29/top-10-cloud-compliance-tools-for-enterprise-security-and-audit-readiness-in-2026
- https://www.dlapiper.com/en-us/insights/publications/2025/08/latest-wave-of-obligations-under-the-eu-ai-act-take-effect
- https://introl.com/blog/sovereign-cloud-ai-infrastructure-data-residency-requirements-2025
- https://incountry.com/blog/ai-data-residency-regulations-and-challenges/
- https://secureprivacy.ai/blog/gdpr-compliance-2026
- https://www.hipaajournal.com/hipaa-business-associate-agreement/
- https://www.gsa.gov/about-us/newsroom/news-releases/gsa-fedramp-prioritize-20x-authorizations-for-ai-08252025
- https://artificialintelligenceact.eu/high-level-summary/
- https://www.scalepad.com/blog/what-is-soc-2-a-2025-introduction-to-understanding-and-achieving-soc-2-compliance/
- https://hightable.io/iso-27001-for-ai-companies/
- https://www.openpolicyagent.org/docs

### F68 -- AI Safety and Guardrails
- https://huggingface.co/meta-llama/Llama-Guard-3-8B
- https://moderationapi.com/blog/how-to-self-host-use-llama-guard-3/
- https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance
- https://www.infoguard.ch/en/blog/ai-act-eu-guardrails-secure-ai-deployment
- https://www.enkryptai.com/blog/enkrypt-ai-vs-azure-content-safety-vs-amazon-bedrock-guardrails
- https://aws.amazon.com/bedrock/guardrails/
- https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-guardrails-reduces-pricing-85-percent/
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- https://github.com/microsoft/presidio
- https://www.dynamo.ai/blog/foundation-guardrails-for-the-eu-ai-act
- https://www.fiddler.ai/articles/ai-guardrails-metrics
- https://github.com/promptfoo/promptfoo

### F69 -- Model Training and Fine-Tuning
- https://introl.com/blog/fine-tuning-infrastructure-lora-qlora-peft-scale-guide-2025
- https://www.runpod.io/blog/llm-fine-tuning-gpu-guide
- https://www.crowdee.com/blog/posts/self-hosting-ai-costs
- https://www.deepspeed.ai/training/
- https://mlflow.org/docs/latest/self-hosting/
- https://docs.wandb.ai/platform/hosting/hosting-options/self-managed
- https://labelstud.io/
- https://optuna.org/
- https://docs.ray.io/en/latest/tune/index.html
- https://cloud.google.com/vertex-ai/pricing

### F70 -- Disaster Recovery and Business Continuity
- https://introl.com/blog/disaster-recovery-ai-infrastructure-rpo-rto-strategies-gpu-clusters
- https://secureframe.com/blog/disaster-recovery-cost
- https://www.serverion.com/uncategorized/cloud-vs-on-premises-disaster-recovery-differences/
- https://aws.amazon.com/rds/aurora/global-database/
- https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html
- https://velero.io/
- https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-backup-and-recovery
- https://arxiv.org/html/2503.11901v4
- https://newsletter.semianalysis.com/p/100000-h100-clusters-power-network
- https://zilliz.com/blog/zilliz-cloud-oct-2025-update

### F71 -- On-Premises Security Operations
- https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center
- https://swimlane.com/blog/global-soc-survey-insights/
- https://www.stamus-networks.com/blog/what-the-2025-sans-detection-response-survey-reveals-false-positives-alert-fatigue-are-worsening
- https://www.digitalxraid.com/blog/microsoft-sentinel-vs-microsoft-defender/
- https://wazuh.com/platform/siem/
- https://falco.org/
- https://www.misp-project.org/features/
- https://www.ibm.com/think/topics/dfir
- https://www.cisa.gov/sites/default/files/publications/cisa-insights_chain-of-custody-and-ci-systems_508.pdf
- https://opsdigest.com/digests/trivy-vs-grype-choosing-the-right-vulnerability-scanner/
