# F68: AI Safety, Guardrails & Content Moderation — On-Premises

**Research Area:** AI Safety Architecture | **Deployment Context:** ISV SaaS on Customer Infrastructure
**Date:** 2026-02-19 | **Audience:** C-Suite and Technical Leadership

---

## Executive Summary

Implementing AI safety guardrails entirely on-premises requires an ISV to operate a parallel AI inference stack — dedicated GPU capacity for safety models running in-line with every production request — alongside the primary LLM inference infrastructure. The two leading self-hosted guardrail models (Llama Guard 3 and NeMo Guardrails) impose measurable latency and cost overhead: NVIDIA's own research documents that robust guardrail implementation can triple both latency and cost relative to an unguarded baseline. Managed cloud safety services (AWS Bedrock Guardrails, Azure AI Content Safety, Google Vertex AI safety filters) eliminate this operational burden entirely but introduce data residency risk, limit policy customizability, and create vendor dependency that may be incompatible with customer regulatory requirements. For ISVs selling into regulated industries or sovereignty-sensitive markets, the on-premises path is often non-negotiable but demands 1.5–3.0 FTE of dedicated MLOps and AI safety engineering to sustain at production quality. Regulatory pressure is intensifying: EU AI Act Article 5 prohibitions entered enforcement in February 2025, with high-risk AI system requirements due August 2026, creating a concrete compliance deadline for guardrail documentation and audit capability.

---

## 1. Guardrail Frameworks: Deployment Requirements and Capabilities

### 1.1 Llama Guard 3

Llama Guard 3 is Meta's purpose-built content safety classifier, fine-tuned on Llama 3.1-8B. It is the most widely adopted open-source safety model for on-premises production deployments as of 2025.

[FACT]
"Llama Guard 3 8B" is fine-tuned on Llama 3.1-8B, uses BF16 tensor type, supports a 128k context window, and covers 8 languages: English, French, German, Hindi, Italian, Portuguese, Spanish, and Thai.
— Meta / Hugging Face Model Card
URL: https://huggingface.co/meta-llama/Llama-Guard-3-8B

[FACT]
Llama Guard 3 classifies content into 14 harm categories (S1–S14): Violent Crimes, Non-Violent Crimes, Sex-Related Crimes, Child Sexual Exploitation, Defamation, Specialized Advice (financial/medical/legal), Privacy Violations, Intellectual Property Infringement, Indiscriminate Weapons (CBRN), Hate Speech, Suicide and Self-Harm, Sexual Content, Elections Misinformation, and Code Interpreter Abuse (DoS, container escapes).
— Meta / Hugging Face Model Card
URL: https://huggingface.co/meta-llama/Llama-Guard-3-8B

**Hardware Requirements (On-Premises):**

[FACT]
Llama Guard 3 8B requires a minimum of 20 GB GPU VRAM for BF16 inference. The recommended production host is an NVIDIA A10G GPU (24 GB VRAM). T4-based instances with 16 GB VRAM are documented as insufficient for the unquantized model.
— ModerationAPI Self-Hosting Guide
URL: https://moderationapi.com/blog/how-to-self-host-use-llama-guard-3/

[FACT]
An INT8 quantized version of Llama Guard 3 is available, reducing checkpoint size by approximately 40% (to ~9–10 GB VRAM) with "very small impact on model performance."
— Meta / Hugging Face Model Card
URL: https://huggingface.co/meta-llama/Llama-Guard-3-8B

[STATISTIC]
Llama Guard 3 achieves an F1 Score of 0.939 on English response classification, compared to 0.877 for Llama Guard 2 and 0.805 for GPT-4. Its false positive rate is 0.040, versus 0.081 for Llama Guard 2 and 0.152 for GPT-4.
— Meta / Hugging Face Model Card
URL: https://huggingface.co/meta-llama/Llama-Guard-3-8B

**Required Software Stack (Self-Hosted):**

[FACT]
A production self-hosted Llama Guard 3 deployment requires: NVIDIA GPU driver, CUDA toolkit, Conda package manager, vLLM serving library, Docker and Docker Compose, and Nginx as a reverse proxy.
— ModerationAPI Self-Hosting Guide
URL: https://moderationapi.com/blog/how-to-self-host-use-llama-guard-3/

**Cost Baseline (Reference Cloud Instance):**

[FACT]
An AWS g5.xlarge instance (NVIDIA A10G, 24 GB VRAM, 4 vCPUs, 16 GB RAM) costs $1.19/hour, or approximately $869/month for continuous 24/7 operation — representing the minimum dedicated per-instance cost for one Llama Guard 3 deployment.
— ModerationAPI Self-Hosting Guide
URL: https://moderationapi.com/blog/how-to-self-host-use-llama-guard-3/

**License:**

[FACT]
Llama Guard 3 is released under the Llama 3.1 Community License Agreement, which is non-exclusive, worldwide, and royalty-free for use cases with fewer than 700 million monthly active users.
— Meta / Hugging Face Model Card
URL: https://huggingface.co/meta-llama/Llama-Guard-3-8B

---

### 1.2 NeMo Guardrails

NVIDIA NeMo Guardrails is an open-source toolkit for adding programmable, dialogue-flow-level guardrails to LLM-based conversational systems. Unlike Llama Guard (which is a classification model), NeMo Guardrails is a policy orchestration layer that can call external classifiers, dialog state machines, and validation models.

[FACT]
NeMo Guardrails system requirements for self-hosted deployment include: Python 3.10, 3.11, 3.12, or 3.13; the C++ compiler and dev tools for compiling the `annoy` library bindings; and optional NVIDIA GPU Operator if nodes have NVIDIA GPUs (not required for CPU-only deployments).
— NVIDIA NeMo Guardrails Documentation
URL: https://docs.nvidia.com/nemo/guardrails/latest/index.html

[FACT]
NeMo Guardrails supports three deployment modes: local API server, Docker containers, and production microservices. For microservice deployments, a persistent volume provisioner using network storage (NFS, S3, vSAN) is required to store guardrail configuration.
— NVIDIA NeMo Guardrails Microservice Deployment Guide
URL: https://docs.nvidia.com/nemo/microservices/latest/set-up/deploy-as-microservices/guardrails.html

[FACT]
Cisco AI Defense has integrated with NVIDIA NeMo Guardrails, indicating enterprise production validation of the self-hosted deployment model.
— Cisco Blog
URL: https://blogs.cisco.com/ai/cisco-ai-defense-integrates-with-nvidia-nemo-guardrails

---

### 1.3 Guardrails AI (Open-Source Framework)

[FACT]
Guardrails AI is a Python framework where "Guardrails Hub is a collection of pre-built measures of specific types of risks (called 'validators'), and multiple validators can be combined together into Input and Output Guards that intercept the inputs and outputs of LLMs."
— Guardrails AI Documentation
URL: https://guardrailsai.com/docs

[FACT]
Guardrails AI's open-source tier (Apache 2.0 license) is free and self-hosted, requiring no licensing costs. Self-hosting requires infrastructure management, validator maintenance, and building custom observability.
— WorkOS Analysis of Guardrails AI
URL: https://workos.com/blog/guardrails-ai-vs-workos-safety-validation-enterprise-authentication

[FACT]
Guardrails AI Pro offers flexible deployment options including "fully hosted and deploy in your own VPC," allowing organizations to maintain data residency while using the vendor's managed control plane.
— Guardrails AI Pro Page
URL: https://www.guardrailsai.com/pro

[FACT]
Guardrails AI natively integrates with OpenTelemetry (OTEL) for monitoring LLM application performance with existing observability tools.
— Guardrails AI Blog
URL: https://www.guardrailsai.com/blog/opentelemetry-llm-performance

---

## 2. Content Filtering: Input/Output Filtering, PII Detection, and Toxicity Detection

### 2.1 Self-Hosted PII Detection: Microsoft Presidio

[FACT]
Microsoft Presidio is an open-source framework for "detecting, redacting, masking, and anonymizing sensitive data (PII) across text, images, and structured data," using Regex matching, Named Entity Recognition (NER via spaCy), and context-aware detection.
— Microsoft Presidio GitHub
URL: https://github.com/microsoft/presidio

[FACT]
Presidio supports deployment as Python native, PySpark, Docker, and Kubernetes. It can run as an HTTP service for polyglot integration across non-Python codebases.
— Microsoft Presidio Documentation
URL: https://microsoft.github.io/presidio/

[FACT]
For guardrail integration, Presidio requires two deployed container services: Presidio Analyzer and Presidio Anonymizer. LiteLLM Proxy supports Presidio as a guardrail backend for real-time PII masking of model responses before they reach the user.
— LiteLLM Documentation
URL: https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2

[FACT]
Presidio is described as "free but requires infrastructure and maintenance," contrasting with managed alternatives that bundle PII detection into per-token API pricing.
— PrivacyProxy vs Presidio Comparison
URL: https://privacyproxy.dev/en/privacyproxy-vs-presidio

---

### 2.2 Latency and Cost Overhead of Self-Hosted Content Filtering

[STATISTIC]
NVIDIA research on NeMo Guardrails found that "implementing robust guardrails can triple both the latency and cost of a standard AI application."
— Dynamo AI Blog (citing NVIDIA)
URL: https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance

[STATISTIC]
"Applying 12 guardrails to 100M requests with prompt engineering can inflate costs by over four times" compared to unguarded inference.
— Dynamo AI Blog
URL: https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance

[FACT]
Each LlamaGuard instance requires a dedicated A10G GPU. "Applying six guardrails with LlamaGuard would require six GPUs" — meaning multi-policy enforcement requires horizontal GPU scaling proportional to the number of simultaneously enforced policies.
— Dynamo AI Blog
URL: https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance

---

## 3. Prompt Injection Defense: On-Premises Implementation Requirements

[FACT]
OWASP has ranked prompt injection as "the number one AI security risk in its 2025 OWASP Top 10 for LLMs."
— OWASP Gen AI Security Project
URL: https://genai.owasp.org/llmrisk/llm01-prompt-injection/

[FACT]
The multi-layered prompt injection defense approach documented for self-hosted systems includes: heuristics for filtering potentially malicious inputs, an LLM-based detection classifier using a dedicated LLM to analyze incoming prompts, a VectorDB storing embeddings of previous attack patterns, and canary tokens for detecting system prompt leakage.
— ModerationAPI / Lakera Analysis
URL: https://www.lakera.ai/blog/guide-to-prompt-injection

[FACT]
Technical self-hosted approaches include: classifier-based detection systems, data tagging methods that track trusted versus untrusted instruction sources, and reinforcement learning frameworks that train models to distinguish legitimate from adversarial instructions.
— Obsidian Security
URL: https://www.obsidiansecurity.com/blog/prompt-injection

**Self-Hosted Prompt Injection Tools:**

[FACT]
Rebuff is an open-source prompt injection detector (ProtectAI) that requires: Supabase (for state storage), a vector database (Pinecone or Chroma for attack embeddings), and an LLM provider API for classification inference.
— Rebuff GitHub
URL: https://github.com/protectai/rebuff

[FACT]
Lakera Guard offers "full audit logging, SIEM integrations, and flexible deployment options, SaaS or self-hosted, built for production-scale GenAI systems."
— Lakera AI
URL: https://www.lakera.ai/risk/prompt-injection-attacks

[FACT]
Thales AI Application Security monitors for "prompt injection attacks, jailbreaking attempts, system prompt leakage, model denial-of-service attacks, and sensitive information leakage, working across cloud, on-premises and hybrid deployments."
— Cyber Magazine
URL: https://cybermagazine.com/news/thales-ai-security-fabric-targets-prompt-injection-attacks

[FACT]
A 2025 arxiv paper proposes AI multi-agent NLP frameworks for prompt injection detection and mitigation, documenting classification-layer architectures designed for pipeline integration.
— arXiv
URL: https://arxiv.org/html/2503.11517v1

---

## 4. Responsible AI Tooling: Bias Detection, Fairness, Model Cards, Explainability

### 4.1 Self-Hosted Open-Source Tools

[FACT]
IBM AI Fairness 360 (AIF360) is an "open-source toolkit developed by IBM to detect and mitigate bias in machine learning models," available for self-hosted deployment, widely used in academic and enterprise contexts.
— IBM AI Fairness 360
URL: https://aif360.res.ibm.com/

[FACT]
Microsoft Fairlearn is "a Python package that helps developers assess the fairness of their AI systems and mitigate any identified biases, offering both mitigation algorithms and metrics for model evaluation."
— DevOpsSchool Comparison
URL: https://www.devopsschool.com/blog/top-10-ai-bias-detection-tools-in-2025-features-pros-cons-comparison/

[FACT]
Fiddler AI provides "model explainability, bias detection, and performance monitoring," with both cloud-hosted and on-premises licensing options available to enterprise buyers.
— Fiddler AI
URL: https://www.fiddler.ai/responsible-ai

[FACT]
DataRobot provides "end-to-end governance with model management, monitoring, documentation, and bias checks," with SaaS and on-premises licensing options.
— CloudNuro AI
URL: https://www.cloudnuro.ai/blog/top-10-ai-model-governance-tools-for-bias-and-ethics-management-2025-guide

[FACT]
Zeno offers hosted SaaS with "air-gapped availability for bias detection in AI models," enabling on-premises deployment options for air-gapped or classified environments.
— Startup Stash
URL: https://startupstash.com/top-ethical-ai-audit-and-bias-detection-platforms/

### 4.2 Cloud-Native Alternatives (What Disappears with Managed Services)

[FACT]
AWS Bedrock Guardrails "blocks up to 88% of harmful content" and provides six configurable safeguard policies: content filters, denied topics, PII redaction, word filters, contextual grounding checks, and Automated Reasoning checks.
— AWS Bedrock Guardrails
URL: https://aws.amazon.com/bedrock/guardrails/

[FACT]
AWS Bedrock Guardrails reduced pricing in December 2024 by up to 85%: content filters now cost $0.15 per 1,000 text units (down from prior pricing), and certain sensitive information filters are free.
— AWS What's New
URL: https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-guardrails-reduces-pricing-85-percent/

[FACT]
Azure AI Content Safety supports text and image analysis, jailbreak risk detection, protected material text detection (matching against known lyrics, articles, and web content), and protected material code detection (matching against GitHub public repositories). Azure Content Safety does not include PII detection or redaction as a built-in feature.
— Enkrypt AI Comparison
URL: https://www.enkryptai.com/blog/enkrypt-ai-vs-azure-content-safety-vs-amazon-bedrock-guardrails

[FACT]
Azure AI Content Safety response latency for injection attack detection is documented at 0.070 seconds for text-only analysis. Amazon Bedrock Guardrails latency for the equivalent operation is 0.210 seconds. Azure's maximum token limit per request is approximately 1,665 tokens versus Bedrock's approximately 22,000 tokens.
— Enkrypt AI Comparison
URL: https://www.enkryptai.com/blog/enkrypt-ai-vs-azure-content-safety-vs-amazon-bedrock-guardrails

[FACT]
Google Vertex AI provides both non-configurable safety filters (blocking CSAM and PII) and configurable content filters across four harm categories: hate speech, harassment, sexually explicit, and dangerous content. A jailbreak classifier is available in Gemini 2.5 Flash (off by default, must be explicitly enabled).
— Google Cloud Documentation
URL: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters

[FACT]
AWS Bedrock Guardrails announced support for coding use cases in November 2025, enabling "safeguards against harmful content introduced within code elements, including comments, variable and function names, and string literals."
— AWS What's New
URL: https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-bedrock-guardrails-coding-use-cases/

[FACT]
AWS Bedrock Guardrails introduced policy-based IAM enforcement in March 2025, including a new condition key `bedrock:GuardrailIdentifier` for enforcing use of specific guardrail configurations via IAM policies.
— AWS What's New
URL: https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-guardrails-policy-based-enforcement-responsible-ai/

[FACT]
Azure AI Content Safety "can be deployed on cloud, on premises and on devices," supporting hybrid and edge deployment scenarios.
— Microsoft Learn
URL: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview

---

## 5. Red Teaming Infrastructure: Adversarial Testing On-Premises

### 5.1 Open-Source Red Teaming Tools

[FACT]
Promptfoo is an open-source AI red teaming tool providing "simple declarative configs with command line and CI/CD integration," supporting test of prompts, agents, and RAGs. It maps findings to OWASP, NIST, MITRE ATLAS, and EU AI Act compliance frameworks.
— Promptfoo GitHub
URL: https://github.com/promptfoo/promptfoo

[FACT]
Promptfoo can be configured with self-hosted LLM providers (e.g., Ollama) so the CLI does not attempt to reach external APIs, enabling fully air-gapped red teaming pipelines.
— Promptfoo FAQ
URL: https://www.promptfoo.dev/docs/faq/

[FACT]
A recommended CI/CD red teaming layering strategy uses: pre-commit/pull request Promptfoo checks running a curated set of security tests in seconds, combined with nightly Garak scans checking for regressions introduced by model updates.
— AI IQ (Attila Rácz-Akácosi)
URL: https://aiq.hu/en/automated-red-teaming-using-pyrit-garak-and-promptfoo-to-uncover-vulnerabilities/

[FACT]
NVIDIA Garak is "an open-source LLM vulnerability scanner" that "tests around 100 different attack vectors using up to 20,000 prompts per run," covering jailbreaks, prompt injection, toxicity, hallucinations, and data leakage. It supports 20+ AI platforms including Hugging Face, OpenAI, AWS Bedrock, and LiteLLM.
— NVIDIA Garak GitHub
URL: https://github.com/NVIDIA/garak

[FACT]
Microsoft PyRIT (Python Risk Identification Tool) is an open-source framework from Microsoft's AI Red Team focused on "multi-turn conversation orchestration with sophisticated attack chains." An AI Red Teaming Agent version was released in Azure AI Foundry as a preview in 2025.
— Promptfoo Comparison Blog
URL: https://www.promptfoo.dev/blog/promptfoo-vs-pyrit/

[FACT]
DeepTeam is an open-source red teaming framework that "simulates over 40 attack types — from prompt injection to PII leakage and jailbreaks."
— Giskard
URL: https://www.giskard.ai/knowledge/best-ai-red-teaming-tools-2025-comparison-features

[STATISTIC]
The AI Red Teaming Services market reached $1.43 billion in 2024 and is projected to grow to $4.8 billion by 2029 at a 28.6% compound annual growth rate.
— Mend.io / Mindgard Research
URL: https://www.mend.io/blog/best-ai-red-teaming-services-top-6-services/

### 5.2 On-Premises Red Teaming Infrastructure Requirements

For a complete on-premises red teaming pipeline, an ISV requires:

- A self-hosted LLM endpoint (local model via Ollama, vLLM, or similar) to serve as the attack orchestrator
- Promptfoo or PyRIT installed in CI/CD runner environment (no external API calls for self-hosted mode)
- Garak installed as a scheduled test job (pip-installable, supports local model endpoints)
- Result storage: a database or artifact store for test reports and AVID-format vulnerability records
- Human review capacity for triaging automated findings before deployment gates

[UNVERIFIED] Estimated FTE for operating a production-grade red teaming pipeline: 0.5–1.0 FTE for a mid-size ISV running weekly automated scans with quarterly human red team exercises. No specific industry benchmark from Gartner or Forrester was located for this specific function as of 2026-02-19. The estimate is derived from published tool documentation complexity and standard MLOps staffing ratios.

---

## 6. Monitoring and Audit: Observability for Guardrails in Production

[FACT]
Key production guardrail metrics identified for LLM monitoring include: guardrail trigger rate (how often safety filters activate), prompt injection detection rate (frequency and types of manipulation attempts), and PII leak rate (instances where sensitive data appears in model outputs).
— Fiddler AI Guardrail Metrics
URL: https://www.fiddler.ai/articles/ai-guardrails-metrics

[FACT]
Fiddler AI's Trust Models evaluate prompts and responses "in under 100 milliseconds" with throughput at "hundreds of prompts per second," providing high-accuracy, low-latency real-time guardrail scoring including hallucination, toxicity, PII leakage, and prompt injection detection.
— Fiddler AI Guardrail Metrics
URL: https://www.fiddler.ai/articles/ai-guardrails-metrics

[FACT]
Guardrails AI provides native OpenTelemetry (OTEL) integration, enabling guardrail telemetry to flow into existing observability stacks (Datadog, Grafana, Jaeger, etc.) without proprietary tooling.
— Guardrails AI Blog
URL: https://www.guardrailsai.com/blog/opentelemetry-llm-performance

[FACT]
Datadog documents LLM guardrail best practices including: establishing trigger rate baselines, monitoring for drift (distinguishing normal variation from genuine degradation), and detecting contradiction/over-blocking patterns that hurt user experience.
— Datadog LLM Guardrails Blog
URL: https://www.datadoghq.com/blog/llm-guardrails-best-practices/

[FACT]
Output guardrails must handle "cases where the LLM has drifted out of its domain due to vague input or hallucinations," requiring filtering and relevancy checks as a drift-detection signal in addition to safety classification.
— orq.ai LLM Guardrails Guide
URL: https://orq.ai/blog/llm-guardrails

**On-Premises Audit Trail Requirements:**

For regulatory compliance (EU AI Act, HIPAA, SOC 2), a self-hosted guardrail deployment must generate structured audit logs including: timestamp, session ID, guardrail policy triggered, classification confidence score, action taken (pass/block/redact), and the sanitized input/output record. These logs must be retained and queryable — a requirement that adds storage infrastructure and log pipeline engineering that managed cloud services handle transparently.

[FACT]
EU AI Act high-risk AI system requirements mandate "Documentation and logging" mechanisms to maintain audit trails of operational processes and decision-making events.
— InfoGuard
URL: https://www.infoguard.ch/en/blog/ai-act-eu-guardrails-secure-ai-deployment

---

## 7. Regulatory Alignment: EU AI Act and Industry-Specific AI Governance

[FACT]
The EU AI Act entered into force August 1, 2024. Article 5 prohibited practices (including manipulation, social scoring, biometric categorization misuse, and emotion recognition) became enforceable February 2025.
— Dynamo AI Blog
URL: https://www.dynamo.ai/blog/foundation-guardrails-for-the-eu-ai-act

[FACT]
EU AI Act penalties for Article 5 violations are "€35 million or 7% of global revenue," whichever is higher.
— Dynamo AI Blog
URL: https://www.dynamo.ai/blog/foundation-guardrails-for-the-eu-ai-act

[FACT]
High-risk AI system requirements under the EU AI Act — including data quality controls, bias mitigation, human oversight mechanisms, and explainability — are due for full implementation by August 2026.
— InfoGuard
URL: https://www.infoguard.ch/en/blog/ai-act-eu-guardrails-secure-ai-deployment

[FACT]
EU AI Act high-risk AI system technical requirements include four mandated controls: (1) traceability of decisions, (2) documentation and logging, (3) human supervision mechanisms preventing autonomous operation in safety-critical contexts, and (4) protection against manipulation and cyber attacks.
— InfoGuard
URL: https://www.infoguard.ch/en/blog/ai-act-eu-guardrails-secure-ai-deployment

[FACT]
The EU AI Act GPAI Code of Practice, confirmed August 1, 2025, includes twenty-five providers (Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI, OpenAI, and others) committed to Transparency, Copyright, and Safety/Security chapters. Adherence is voluntary but considered by the AI Office when assessing fines.
— EU AI Act News
URL: https://artificialintelligenceact.eu/

[FACT]
GPAI providers must: "draw up and maintain technical documentation, provide information to downstream deployers, establish copyright compliance policies, and publish training data summaries," effective August 2, 2025.
— Nemko Digital EU AI Act 2025 Update
URL: https://digital.nemko.com/insights/eu-ai-act-rules-on-gpai-2025-update

[FACT]
Dynamo AI's Foundation Guardrails directly map to EU AI Act Article 5 categories, addressing: Manipulation/Deceptive Language, Social Scoring, Criminal Risk Assessment, Biometric Categorization, and Emotion Recognition as distinct input/output guardrail policies.
— Dynamo AI Blog
URL: https://www.dynamo.ai/blog/foundation-guardrails-for-the-eu-ai-act

[FACT]
Promptfoo red teaming framework maps test findings to EU AI Act compliance requirements, enabling automated compliance evidence generation as part of CI/CD pipeline output.
— Promptfoo
URL: https://www.promptfoo.dev/blog/top-5-open-source-ai-red-teaming-tools-2025/

[FACT]
A 2025 Pacific AI governance survey found that "45% of enterprises cite speed-to-market pressure as the single biggest barrier to proper AI governance."
— Skywork AI / Agentic AI Safety Blog
URL: https://skywork.ai/blog/agentic-ai-safety-best-practices-2025-enterprise/

---

## 8. Deployment Model Comparison

The following table applies the standard difficulty rating scale and FTE estimation framework to AI safety and guardrail operations across the three deployment models.

**Assumptions:** Mid-size ISV, 50 enterprise customers, 10M guardrail evaluations/month, 5 active safety policies, one regulated industry (financial services or healthcare).

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|---|---|---|---|
| **Safety Model Inference** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 1/5 |
| | Self-hosted GPU cluster for Llama Guard 3 or equivalent; capacity planning and failover required | Self-hosted safety model pods on managed K8s; GPU node pool management, HPA tuning | Bedrock Guardrails / Azure Content Safety / Vertex AI safety filters; fully managed, per-request billing |
| | vLLM, NVIDIA NIM, Triton Inference Server | vLLM on EKS/AKS/GKE, GPU Operator | AWS Bedrock, Azure AI Content Safety, Google Vertex AI |
| | Est. FTE: 0.75–1.25 | Est. FTE: 0.5–0.75 | Est. FTE: 0.0–0.1 |
| **PII Detection and Redaction** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Presidio (Analyzer + Anonymizer containers); custom entity tuning | Presidio in K8s pods; same complexity as on-prem, managed control plane reduces ops | Azure Purview or Bedrock PII redaction; no Presidio equivalent in Azure Content Safety natively |
| | Microsoft Presidio, spaCy, GLiNER | Microsoft Presidio on K8s | AWS Bedrock PII redaction, custom regex types |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |
| **Prompt Injection Defense** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Multi-layer stack: heuristics + VectorDB embeddings + dedicated classifier + canary tokens; requires ongoing attack signature updates | K8s-deployed injection classifier; managed control plane simplifies ops but attack database still self-maintained | Azure Prompt Shields, Bedrock content filters with injection detection; AWS blocks 88% of harmful content |
| | Rebuff, Lakera Guard self-hosted, Thales AI Security | Same tools on K8s with ingress integration | Azure AI Content Safety jailbreak detection, AWS Bedrock Guardrails |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.2–0.4 | Est. FTE: 0.05–0.1 |
| **Bias Detection and Fairness Monitoring** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | IBM AIF360 or Fairlearn; requires integration with model training pipeline; ongoing monitoring dashboards | Same tools on K8s; managed cluster reduces infrastructure ops | Neither Bedrock nor Azure Content Safety includes bias detection; requires ISV-built layer |
| | IBM AI Fairness 360, Fairlearn, Fiddler AI (on-prem license) | Same, running on K8s | [UNVERIFIED] No major cloud provider offers native bias detection as a managed guardrail API as of 2026-02-19 |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 |
| **Red Teaming Pipeline** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Promptfoo + Garak in CI/CD; self-hosted LLM for adversarial orchestration; result storage and triage process | Same tools containerized on K8s; managed runners simplify scheduling | Promptfoo/Garak still run self-hosted; Azure AI Foundry adds managed AI Red Teaming Agent (2025 preview) |
| | Promptfoo, Garak, PyRIT, DeepTeam | Same tools on K8s | Promptfoo CLI + Azure AI Foundry AI Red Teaming Agent |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |
| **Audit Logging and Compliance Reporting** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Custom log pipeline: structured audit records for each guardrail trigger; retention infrastructure; query tooling for regulatory audit response | Log aggregation on K8s (Loki, ELK); managed control plane reduces ops but log pipeline engineering still required | Cloud-native audit logs (CloudTrail, Azure Monitor); guardrail trigger logs built into managed service; reporting tooling still ISV responsibility |
| | ELK Stack, Loki, custom structured logging, SIEM integration | Loki/ELK on K8s, OpenTelemetry | AWS CloudTrail, Azure Monitor, Google Cloud Logging; OpenTelemetry via Guardrails AI |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.15–0.3 | Est. FTE: 0.1–0.2 |

**Total Estimated FTE (On-Premises AI Safety Stack):**
Aggregating the ranges above: **2.25–3.75 FTE** for the full AI safety operational profile on-premises, for a mid-size ISV at the described scale. This is in addition to general MLOps and infrastructure staffing.

---

## 9. What Operational Burden Disappears with Managed Safety Services

When an ISV moves from on-premises guardrails to cloud-native managed safety services, the following operational burdens are eliminated:

[FACT]
AWS Bedrock Guardrails works "consistently across any foundation model whether you're using models in Amazon Bedrock or self-hosted models including third-party models such as OpenAI and Google Gemini," eliminating the need to deploy a separate safety model inference stack.
— AWS Bedrock Guardrails
URL: https://aws.amazon.com/bedrock/guardrails/

[FACT]
AWS Bedrock Guardrails introduced a Standard tier in 2025 that "detects and filters undesirable content with better contextual understanding including modifications such as typographical errors, and support for up to 60 languages" — a capability that would require extensive custom model training to replicate self-hosted.
— AWS What's New
URL: https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-guardrails-safely-build-generative-ai-applications/

**Eliminated on-premises operational tasks with managed services:**

1. GPU capacity planning and failover for safety model inference
2. CUDA/driver stack maintenance and NVIDIA driver version management
3. Safety model version management and update rollouts (Meta Llama Guard releases, etc.)
4. VectorDB infrastructure for attack pattern embeddings (for injection defense)
5. Presidio container deployment and spaCy model updates (for PII)
6. Custom structured audit log pipeline engineering
7. Capacity autoscaling of the safety inference layer under traffic spikes
8. On-call burden for safety model outages (which block production LLM responses)

**What managed services do NOT eliminate (ISV responsibility in all models):**

1. Red teaming pipeline (Promptfoo/Garak remain self-operated regardless of deployment model)
2. Bias detection and fairness monitoring (no major cloud provider offers this as a managed API)
3. Policy design and tuning (denied topics, custom categories, sensitivity thresholds)
4. False positive monitoring and threshold adjustment
5. EU AI Act documentation, model card authorship, and human oversight mechanisms
6. Integration engineering between guardrail API and LLM serving layer

---

## Key Takeaways

- **On-premises guardrails require a dedicated GPU fleet for safety model inference.** Llama Guard 3 8B requires a minimum 20 GB VRAM GPU per instance, and running six simultaneous guardrail policies requires six GPUs. This is an infrastructure cost line distinct from primary LLM serving infrastructure.

- **The latency and cost penalty of self-hosted guardrails is material.** NVIDIA's own documentation indicates that robust guardrail implementations can triple both latency and cost. Twelve-policy configurations at scale can inflate inference costs by more than 4×. Architecture decisions must account for this overhead at the beginning of product design.

- **Managed cloud safety services (Bedrock Guardrails, Azure AI Content Safety, Vertex AI) eliminate GPU infrastructure and model management entirely**, at the cost of data sovereignty and policy customization limits. Neither AWS nor Azure currently offers native bias detection as a managed API — this gap forces ISVs to operate bias tooling regardless of deployment model.

- **EU AI Act Article 5 enforcement began February 2025; high-risk system requirements are due August 2026.** ISVs must implement traceable decision logging, human oversight mechanisms, and manipulation/cyber attack protections as technical guardrail requirements — not optional additions. On-premises deployment gives full auditability control; cloud-native services offer some logging but ISV-side documentation remains mandatory.

- **Total FTE for a full on-premises AI safety stack at mid-scale is 2.25–3.75 FTE**, covering safety model inference operations, PII detection, prompt injection defense, red teaming pipeline, and audit logging. This staffing burden is reduced to approximately 0.5–1.0 FTE with cloud-native managed services, with the residual primarily in policy design, red teaming, and compliance documentation.

---

## Related — Out of Scope

- **General security hardening and network isolation** of the AI inference environment is covered by F46–F47 (Security Architecture). This file addresses only AI-specific safety guardrails and content moderation.
- **Model serving infrastructure** (vLLM, Triton, GPU cluster operations) is covered by F36. This file references model serving only where it intersects safety model deployment requirements.
- **Broad compliance frameworks** (SOC 2, HIPAA, ISO 27001) are covered by F67. This file covers only the EU AI Act requirements that directly map to technical guardrail implementation.
- **Agent-level permission systems and tool-use restrictions** are an emerging guardrail category that intersects with agentic AI architectures. This topic is referenced here but warrants dedicated research.

---

## Sources

1. Meta / Hugging Face — Llama Guard 3 8B Model Card: https://huggingface.co/meta-llama/Llama-Guard-3-8B
2. ModerationAPI — How to Self-Host Llama Guard 3: https://moderationapi.com/blog/how-to-self-host-use-llama-guard-3/
3. NVIDIA — NeMo Guardrails Documentation: https://docs.nvidia.com/nemo/guardrails/latest/index.html
4. NVIDIA — NeMo Guardrails Microservice Deployment Guide: https://docs.nvidia.com/nemo/microservices/latest/set-up/deploy-as-microservices/guardrails.html
5. Cisco Blog — Cisco AI Defense + NeMo Guardrails: https://blogs.cisco.com/ai/cisco-ai-defense-integrates-with-nvidia-nemo-guardrails
6. Guardrails AI — Documentation: https://guardrailsai.com/docs
7. Guardrails AI — Pro Deployment Options: https://www.guardrailsai.com/pro
8. Guardrails AI — OpenTelemetry Integration: https://www.guardrailsai.com/blog/opentelemetry-llm-performance
9. WorkOS — Guardrails AI Analysis: https://workos.com/blog/guardrails-ai-vs-workos-safety-validation-enterprise-authentication
10. Microsoft Presidio — GitHub: https://github.com/microsoft/presidio
11. Microsoft Presidio — Documentation: https://microsoft.github.io/presidio/
12. LiteLLM — Presidio PII Masking: https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2
13. PrivacyProxy — Presidio Comparison: https://privacyproxy.dev/en/privacyproxy-vs-presidio
14. Dynamo AI — AI Guardrails Cost Analysis: https://www.dynamo.ai/blog/breaking-the-bank-on-ai-guardrails-heres-how-to-minimize-costs-without-comprising-performance
15. OWASP — LLM Top 10 2025, Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
16. Lakera AI — Prompt Injection Guide: https://www.lakera.ai/blog/guide-to-prompt-injection
17. Lakera AI — Prompt Injection Risk: https://www.lakera.ai/risk/prompt-injection-attacks
18. Obsidian Security — Prompt Injection: https://www.obsidiansecurity.com/blog/prompt-injection
19. Rebuff — GitHub: https://github.com/protectai/rebuff
20. Cyber Magazine — Thales AI Security Fabric: https://cybermagazine.com/news/thales-ai-security-fabric-targets-prompt-injection-attacks
21. arXiv — Prompt Injection Detection via Multi-Agent NLP: https://arxiv.org/html/2503.11517v1
22. IBM AI Fairness 360: https://aif360.res.ibm.com/
23. DevOpsSchool — AI Bias Detection Tools 2025: https://www.devopsschool.com/blog/top-10-ai-bias-detection-tools-in-2025-features-pros-cons-comparison/
24. Fiddler AI — Responsible AI: https://www.fiddler.ai/responsible-ai
25. CloudNuro AI — AI Governance Tools: https://www.cloudnuro.ai/blog/top-10-ai-model-governance-tools-for-bias-and-ethics-management-2025-guide
26. Startup Stash — Ethical AI Audit Platforms: https://startupstash.com/top-ethical-ai-audit-and-bias-detection-platforms/
27. AWS — Bedrock Guardrails Overview: https://aws.amazon.com/bedrock/guardrails/
28. AWS — Bedrock Guardrails Price Reduction (Dec 2024): https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-guardrails-reduces-pricing-85-percent/
29. AWS — Bedrock Guardrails 2025 Capabilities: https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-bedrock-guardrails-safely-build-generative-ai-applications/
30. AWS — Bedrock Guardrails Coding Use Cases (Nov 2025): https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-bedrock-guardrails-coding-use-cases/
31. AWS — Bedrock Guardrails Policy-Based Enforcement (Mar 2025): https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-guardrails-policy-based-enforcement-responsible-ai/
32. Enkrypt AI — Bedrock vs Azure Content Safety Comparison: https://www.enkryptai.com/blog/enkrypt-ai-vs-azure-content-safety-vs-amazon-bedrock-guardrails
33. Microsoft Learn — Azure AI Content Safety Overview: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview
34. Google Cloud — Vertex AI Safety Filters: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters
35. Fiddler AI — Guardrail Metrics: https://www.fiddler.ai/articles/ai-guardrails-metrics
36. Datadog — LLM Guardrails Best Practices: https://www.datadoghq.com/blog/llm-guardrails-best-practices/
37. orq.ai — LLM Guardrails Guide 2025: https://orq.ai/blog/llm-guardrails
38. Dynamo AI — EU AI Act Foundation Guardrails: https://www.dynamo.ai/blog/foundation-guardrails-for-the-eu-ai-act
39. InfoGuard — EU AI Act Technical Requirements: https://www.infoguard.ch/en/blog/ai-act-eu-guardrails-secure-ai-deployment
40. EU AI Act — Official Site: https://artificialintelligenceact.eu/
41. Nemko Digital — EU AI Act GPAI 2025 Update: https://digital.nemko.com/insights/eu-ai-act-rules-on-gpai-2025-update
42. NVIDIA Garak — GitHub: https://github.com/NVIDIA/garak
43. Help Net Security — Garak Open Source: https://www.helpnetsecurity.com/2025/09/10/garak-open-source-llm-vulnerability-scanner/
44. Promptfoo — GitHub: https://github.com/promptfoo/promptfoo
45. Promptfoo — CI/CD Integration: https://www.promptfoo.dev/docs/integrations/ci-cd/
46. Promptfoo — Top Red Teaming Tools 2025: https://www.promptfoo.dev/blog/top-5-open-source-ai-red-teaming-tools-2025/
47. Promptfoo vs PyRIT Comparison: https://www.promptfoo.dev/blog/promptfoo-vs-pyrit/
48. Attila Rácz-Akácosi — Automated Red Teaming (PyRIT/Garak/Promptfoo): https://aiq.hu/en/automated-red-teaming-using-pyrit-garak-and-promptfoo-to-uncover-vulnerabilities/
49. Mend.io — AI Red Teaming Services Market: https://www.mend.io/blog/best-ai-red-teaming-services-top-6-services/
50. Giskard — Red Teaming Tools 2025: https://www.giskard.ai/knowledge/best-ai-red-teaming-tools-2025-comparison-features
51. Skywork AI — Agentic AI Safety 2025: https://skywork.ai/blog/agentic-ai-safety-best-practices-2025-enterprise/
