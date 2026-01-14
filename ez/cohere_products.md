# Cohere AI Building Platform - Product Announcements
## Date Range: August 1, 2025 - January 13, 2026

### Executive Summary
Cohere announced major expansions to its enterprise AI building platform during this period, centered on the general availability of North, its agentic AI workspace platform. The company raised $500M at a $6.8B valuation, launched multiple new building blocks including Command A Vision (multimodal), Command A Reasoning, Command A Translate, and Rerank 4.0. Key platform enhancements included API v2 with improved developer experience, expanded cloud integrations (AWS Bedrock, Azure AI Foundry, Oracle OCI), and enterprise deployment capabilities supporting VPC, on-premises, and air-gapped environments. North for Banking partnership with RBC established vertical-specific platform capabilities.

### Key Statistics
- Total platform announcements: 18+
- New platform features: North Platform GA, API v2, Agent Studio, North for Banking
- New building blocks/APIs: Command A Vision, Command A Reasoning, Command A Translate, Rerank 4.0, Embed v4 multimodal
- Enterprise features: Multi-step tool use, Model Context Protocol support, private deployment options, 100+ connectors
- Cloud integrations: AWS Bedrock, Azure AI Foundry, Oracle OCI, AWS Sagemaker
- Funding: $500M raised (August), additional $100M (September)

---

## Platform Announcements by Date

### August 6, 2025 - Cohere North Platform General Availability
**Category:** North Platform
**Type:** New Platform Feature

**Description:**
Cohere made its North productivity platform generally available after seven months of early access. North is a low-code AI agent building platform enabling enterprises to create custom agents, automate workflows, and integrate with workplace tools (Gmail, Slack, Salesforce, Outlook, SharePoint, Linear). The platform runs on minimal hardware (as few as two GPUs) and supports private deployment including on-premises, VPC, hybrid, and air-gapped environments.

**Platform Building Capabilities:**
- Custom agent creation without requiring technical expertise
- Workflow automation across multiple business functions
- Integration with existing enterprise systems via Model Context Protocol (MCP) servers
- Multi-agent orchestration for complex business processes
- Granular access controls and autonomy policies
- Document drafting and refinement with style guide adherence
- Citation tracking for search and retrieval

**Source Quote:**
> "North enables enterprises to deploy AI agents and automations within their own infrastructure, prioritizing data security. The platform offers custom agent creation without requiring technical expertise, workflow automation across multiple business functions, and integration with existing enterprise systems."

**Source:** [Cohere North GA Blog](https://cohere.com/blog/north-ga) | Published: August 6, 2025

---

### August 14, 2025 - $500M Funding Round at $6.8B Valuation
**Category:** Enterprise
**Type:** Funding Announcement

**Description:**
Cohere announced an oversubscribed $500M funding round at $6.8B valuation to accelerate development of frontier enterprise AI technology. The round was led by Radical Ventures and Inovia Capital, with participation from AMD Ventures, NVIDIA, PSP Investments, Salesforce Ventures, and new investor Healthcare of Ontario Pension Plan (HOOPP). The capital targets acceleration of global operations and agentic AI solutions for businesses and governments.

**Source Quote:**
> "Cohere announced it had raised an oversubscribed $500 million round, bringing its valuation to $6.8 billion. The new capital was aimed at accelerating efforts to make businesses and governments around the world more efficient through agentic AI solutions."

**Source:** [TechCrunch](https://techcrunch.com/2025/08/14/cohere-hits-a-6-8b-valuation-as-investors-amd-nvidia-and-salesforce-double-down/) | Published: August 14, 2025

---

### August 21, 2025 - Command A Reasoning Model
**Category:** APIs | Developer Tools
**Type:** New Model with Platform Capabilities

**Description:**
Cohere launched Command A Reasoning, its first reasoning model optimized for enterprise tool use, agentic workflows, and multilingual applications. At 111B parameters with 256K context length, the model runs on 1-2 GPUs (A100s/H100s). Command A Reasoning supports 23 languages and includes multi-step tool use capabilities for complex agentic tasks. The model can be used with reasoning enabled for increased performance or disabled for lower latency responses, providing building flexibility for different enterprise use cases.

**Platform Building Capabilities:**
- Multi-step tool use and function calling
- REACT agent framework support
- Sequential reasoning for complex workflows
- Conversational tool use API integration
- Support for both read and write operations on external systems

**Source Quote:**
> "Command A Reasoning is Cohere's first reasoning model to date, excelling at real world enterprise tasks including tool use, retrieval augmented generation (RAG), agents, and multilingual use cases. The model can be used both with reasoning on for increased performance or with reasoning off for lower latency responses."

**Source:** [Cohere Command A Reasoning Documentation](https://docs.cohere.com/docs/command-a-reasoning) | Published: August 21, 2025

---

### August 28, 2025 - Command A Translate Model
**Category:** APIs
**Type:** New Building Block

**Description:**
Cohere released Command A Translate, its first machine translation model achieving state-of-the-art performance across 23 languages. The model features 111B parameters, 16K token context length (8K input + 8K output), and is optimized for deployment on 1-2 GPUs, enabling private enterprise deployment for translation workflows.

**Source Quote:**
> "Cohere announced the release of Command A Translate, Cohere's first machine translation model, which achieves state-of-the-art performance at producing accurate, fluent translations across 23 languages. The model features 111 billion parameters, a 16K token context length (8K input + 8K output), and is optimized for deployment on 1-2 GPUs."

**Source:** [Cohere Release Notes](https://docs.cohere.com/changelog/2025-08-28-command-a-translate) | Published: August 28, 2025

---

### September 2025 - Additional $100M Funding
**Category:** Enterprise
**Type:** Funding Announcement

**Description:**
Cohere announced additional $100M in funding during a second close to support growing global operations and development of frontier enterprise AI technology, bringing attention to the company's focus on security-first enterprise AI deployments.

**Source Quote:**
> "In September 2025, Cohere announced additional funding of $100M in a second close to support growing global operations and development of frontier enterprise AI technology."

**Source:** [Cohere Blog](https://cohere.com/blog/september-2025-funding-round) | Published: September 2025

---

### API v2 Major Update (2025)
**Category:** Developer Tools | APIs
**Type:** Platform Upgrade

**Description:**
Cohere introduced API v2 with major improvements to Chat, Classify, Embed, and Rerank APIs, making it easier and faster to build enterprise applications. The update includes required model version specification to prevent unexpected behavior, consolidated messages array structure, JSON schema-based tool definitions with unique IDs for proper matching, Server Sent Events (SSE) for streaming, and new SDKs for Python, TypeScript, Java, and Go featuring ClientV2 for improved developer experience.

**Platform Building Capabilities:**
- Improved tool integration with JSON schema definitions
- Enhanced citation options with mode parameter
- Better streaming with SSE instead of JSON-stream events
- Backward compatible with V1 APIs
- Simplified migration path for existing applications

**Source Quote:**
> "Cohere introduced improvements to their Chat, Classify, Embed, and Rerank APIs in a major version upgrade, with the goal of making it easier and faster to build with their platform. Developers must now specify the model version in API calls - previously optional, which sometimes led to unexpected behavior when new models were released and defaults changed."

**Source:** [Cohere Blog - New API v2](https://cohere.com/blog/new-api-v2) | Published: 2025

---

### October 2025 - Cohere Embed v4 on Amazon Bedrock
**Category:** Cloud Integration | APIs
**Type:** Platform Integration

**Description:**
Amazon Bedrock launched support for Cohere Embed v4, a state-of-the-art multimodal embedding model for text, images, and complex business documents. The model supports over 100 languages and is fine-tuned for industries including finance, healthcare, and manufacturing. Available through serverless API endpoints with pay-as-you-go billing in US East (N. Virginia), Europe (Ireland), and Asia Pacific (Tokyo), with cross-region inference capabilities.

**Platform Building Capabilities:**
- Multimodal embeddings (text and images)
- 100+ language support
- Industry-specific fine-tuning
- Semantic retrieval for RAG architectures
- Integration with AWS enterprise security and compliance

**Source Quote:**
> "Amazon Bedrock now offers Cohere Embed v4, a state-of-the-art multimodal embedding model for text, images, and complex business documents. With support for over 100 languages, including Arabic, English, French, Japanese, and Korean, Embed v4 enables global organizations to seamlessly search for information, breaking language barriers."

**Source:** [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/10/coheres-embed-v4-multimodal-embeddings-bedrock/) | Published: October 2025

---

### November 2025 - Cohere Models on Azure AI Foundry (Microsoft Ignite)
**Category:** Cloud Integration | Enterprise
**Type:** Platform Integration

**Description:**
At Microsoft Ignite 2025, Cohere's leading models joined Azure AI Foundry's first-party model lineup, providing serverless API endpoints with pay-as-you-go billing and Managed Compute deployment options. This integration brings Command A, Embed 4, Rerank 4.0 Fast, and Rerank 4.0 Pro to Azure, enabling enterprises to deploy instantly with their own Azure quota using per-hour GPU pricing while maintaining governance, security, and operational tooling.

**Platform Building Capabilities:**
- Instant deployment with Azure quota
- Enterprise governance and security integration
- Serverless and Managed Compute deployment options
- High-performance retrieval, classification, and generation workflows at enterprise scale
- First-party integration benefits

**Source Quote:**
> "In November 2025 at Microsoft Ignite, Cohere's leading models joined Foundry's first-party model lineup, providing ultimate model choice and flexibility. The Managed Compute launch allows enterprises and developers to deploy Cohere models instantly with their own Azure quota, with per-hour GPU pricing that compensates the model provider."

**Source:** [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-models-at-ignite-2025-why-integration-wins-in-enterprise-ai/4470776) | Published: November 2025

---

### December 11, 2025 - Rerank 4.0 Release
**Category:** RAG/Retrieval | APIs
**Type:** New Building Block

**Description:**
Cohere announced Rerank 4.0, a milestone in search and retrieval for enterprise applications. The model offers two variants: rerank-v4.0-pro for state-of-the-art quality and complex use-cases, and rerank-v4.0-fast for low latency and high throughput. Key improvements include 4x larger context window (32K tokens), multilingual support for 100+ languages, semi-structured data support (JSON documents), self-learning capability for customization without additional annotated data, and cross-encoder architecture for subtle semantic relationships.

**Platform Building Capabilities:**
- Dramatically improved search quality
- Reduced hallucinations in RAG applications
- Strengthened AI agent reasoning capabilities
- Evaluation of multiple passages simultaneously
- JSON document reranking for semi-structured data
- Self-learning customization without annotation

**Source Quote:**
> "Cohere announced the release of Rerank 4.0 on December 11, 2025, describing it as 'a milestone in search and retrieval, offering unmatched accuracy and speed for enterprise applications.' Rerank 4 has a 32K context window, representing a four-fold increase compared to 3.5. With Rerank 4.0, customers can dramatically improve the quality of search, reduce hallucinations in RAG applications, and strengthen the reasoning capabilities of their AI agents, all with just a few lines of code."

**Source:** [Cohere Blog - Rerank 4](https://cohere.com/blog/rerank-4) | Published: December 11, 2025

---

### December 2025 - Aya Expanse Multilingual Models
**Category:** APIs
**Type:** Open-Weight Building Blocks

**Description:**
Cohere for AI introduced Aya Expanse 8B and 32B, massively multilingual large language models optimized for 23 languages. The models combine curated open-source datasets with compute-efficient pretraining to achieve performance advantages over competitors while reducing infrastructure costs by up to 30%. Released as open-weight models through HuggingFace, enabling enterprises to build multilingual applications with state-of-the-art performance across low- and high-resource languages.

**Source Quote:**
> "Cohere for AI has introduced two new large language models (LLMs) — Aya Expanse 8B and 32B — as part of its ongoing project aimed at closing language divides in foundational AI datasets and models. By combining a curated open-source dataset with compute-efficient pretraining, it achieves unparalleled performance across low- and high-resource languages while reducing infrastructure costs by up to 30%."

**Source:** [Cohere Blog - Aya Expanse](https://cohere.com/blog/aya-expanse-connecting-our-world) | Published: December 2025

---

### December 16, 2025 - AfriAya Vision-Language Dataset
**Category:** Developer Tools
**Type:** Open Research Release

**Description:**
Cohere Labs announced AfriAya, a new vision-language dataset aimed at improving how AI models understand African languages and cultural contexts. This open research release supports enterprises building applications for African markets and multilingual use cases.

**Source Quote:**
> "Cohere Labs announced the release of AfriAya, a new vision-language dataset aimed at improving how AI models understand African languages and cultural contexts."

**Source:** [Slator](https://slator.com/cohere-labs-launches-vision-language-dataset-for-african-languages/) | Published: December 16, 2025

---

### July 31, 2025 - Command A Vision Model
**Category:** APIs
**Type:** New Building Block

**Description:**
Cohere announced Command A Vision, its first commercial multimodal model capable of understanding and interpreting visual data alongside text. The 112B dense model supports up to 20 images per request (or 20MB total), 128K token context length, and 8K maximum output tokens. Requires two or fewer GPUs for deployment. Officially supports English, Portuguese, Italian, French, German, and Spanish, enabling enterprises to build document OCR, image analysis, and visual reasoning applications.

**Platform Building Capabilities:**
- Document OCR and analysis
- Image understanding and interpretation
- Multi-image processing (up to 20 per request)
- Visual reasoning for enterprise applications
- Integration with existing Command A tool use and RAG capabilities

**Source Quote:**
> "Cohere announced the release of Command A Vision on July 31, 2025, describing it as Cohere's first commercial model capable of understanding and interpreting visual data alongside text. The model empowers businesses to automate tedious tasks, unlock valuable insights from visual data, and make highly accurate, data-driven decisions through document OCR and image analysis."

**Source:** [Cohere Command A Vision Announcement](https://docs.cohere.com/v1/changelog/2025-07-31-command-a-vision) | Published: July 31, 2025

---

### January 2025 - North for Banking with RBC Partnership
**Category:** North Platform | Enterprise
**Type:** Vertical-Specific Platform

**Description:**
RBC partnered with Cohere to co-develop and securely deploy North for Banking, an enterprise generative AI solution optimized for financial services. The platform integrates with RBC's and Cohere's proprietary foundation models and RBC's internal platforms, enabling employees to complete tasks, find information, and search for customer-specific solutions. All data is powered and stored internally within the bank's systems, with focus on risk and security features specific to financial services.

**Platform Building Capabilities:**
- Vertical-specific platform customization for banking
- Integration with internal banking systems
- Customer-service workflow optimization
- Advice center support for advisors
- Capital Markets research analyst productivity tools
- Financial services-specific security and risk features

**Source Quote:**
> "In January 2025, RBC partnered with Cohere to co-develop and securely deploy an enterprise generative AI solution optimized for financial services. The platform, called North for Banking, will integrate with RBC's and Cohere's own proprietary foundation models, as well as RBC's internal platforms. North for Banking will help employees complete tasks and find information, including searching for answers and solutions specific to customers' needs."

**Source:** [RBC Newsroom](https://www.rbc.com/newsroom/news/article.html?article=125967) | Published: January 2025

---

### Cohere Toolkit - RAG Building Platform (Ongoing)
**Category:** Developer Tools | RAG/Retrieval
**Type:** Open-Source Platform

**Description:**
Cohere Toolkit is a collection of pre-built components enabling developers to quickly build and deploy RAG applications, cutting time-to-launch from months to weeks. The toolkit includes a Next.js front-end with SQL database for conversation history, documents, and citations, plus a back-end with preconfigured data sources and retrieval chains. Supports deployment via Docker and Poetry with 100+ pre-built connectors for popular cloud services (Asana, Slack, GitHub) and databases.

**Platform Building Capabilities:**
- Pre-built RAG components and retrieval chains
- 100+ connectors for data sources
- Conversation history and citation management
- Model selection (Cohere native, Azure, AWS Sagemaker)
- Local and cloud deployment options
- Open-source customization via GitHub

**Source Quote:**
> "Cohere Toolkit is a collection of pre-built components enabling developers to quickly build and deploy retrieval augmented generation (RAG) applications. With it, you can cut time-to-launch down from months to weeks, and deploy in as little as a few minutes. The toolkit contains the tools to ensure that personalized knowledge assistants are capable of understanding conversation intent, remembering conversation history, fulfilling RAG-based tasks, adding fine-grained, relevant citations from private data sources to support their answers, and are endlessly customizable using Cohere's 100+ pre-built connectors."

**Source:** [GitHub - Cohere Toolkit](https://github.com/cohere-ai/cohere-toolkit) | Published: 2025

---

### Multi-Step Tool Use and Agent Capabilities (Ongoing)
**Category:** Developer Tools | APIs
**Type:** Platform Feature

**Description:**
Cohere's Chat endpoint supports multi-step tool use, enabling models to perform sequential reasoning and call multiple tools in sequence. Compatible with Command R7B and newer models, the feature enables planning, execution, and reflection cycles where the model determines which tools to use, in what order, and adapts based on results. Command A Reasoning has been specifically trained with conversational tool use capabilities for interacting with external APIs, databases, or search engines.

**Platform Building Capabilities:**
- Sequential tool calling and reasoning
- Parallel tool execution when needed
- Planning and execution frameworks
- Reflection and adaptation based on results
- Integration with external APIs and databases
- REACT agent pattern support

**Source Quote:**
> "The Chat endpoint supports multi-step tool use, which enables the model to perform sequential reasoning. Multi-step tool use allows the model to call more than one tool in a sequence of steps, using the results from one tool call in a subsequent step. Given a user request, the model comes up with a plan to solve the problem which answers questions such as 'Which tools should be used,' and 'In what order should they be used.'"

**Source:** [Cohere Multi-Step Tool Use Documentation](https://docs.cohere.com/docs/multi-step-tool-use) | Published: 2025

---

### Cohere Quick-Start Connectors Framework (Ongoing)
**Category:** RAG/Retrieval | Developer Tools
**Type:** Open-Source Framework

**Description:**
Cohere's Build-Your-Own-Connector framework allows integration of Command LLM via Chat API endpoint to any datastore or software with a search endpoint exposed in its API. The open-source repository offers reference code for integrating workplace datastores with Cohere's LLMs for seamless RAG. Approximately 100 prebuilt connectors available on GitHub for popular services (Asana, Slack, GitHub) and open-source databases. Requires Python 3.11+ and Poetry, connectors must implement specific interface and expose data source as HTTP REST API.

**Platform Building Capabilities:**
- Custom data source integration
- 100+ prebuilt connectors
- HTTP REST API interface
- Grounded generations with citations
- Integration with internal company documentation
- Knowledge work and research applications

**Source Quote:**
> "This open-source repository offers reference code for integrating workplace datastores with Cohere's LLMs, enabling developers and businesses to perform seamless retrieval-augmented generation (RAG) on their own data. A connector allows you to integrate data sources with the '/chat' endpoint to create grounded generations with citations to the data source."

**Source:** [GitHub - Quick Start Connectors](https://github.com/cohere-ai/quick-start-connectors) | Published: 2025

---

### Security and Compliance Features (Ongoing)
**Category:** Enterprise
**Type:** Platform Features

**Description:**
Cohere's platform includes comprehensive security protocols including granular access control, agent autonomy policies, continuous red-teaming, and third-party security tests. Meets international compliance standards including GDPR, SOC 2 Type II, ISO 27001, and ISO 42001. All data sent to or from Cohere is encrypted using TLS, with customer data encrypted using AES-256. Logged prompts and generations automatically deleted after 30 days. Platform implements just-in-time (JIT) access management and role-based access with least privilege principle.

**Platform Building Capabilities:**
- VPC and on-premises private deployment
- Air-gapped environment support
- Pass-through identity and native IdP integrations
- Role-based access control
- Data lineage tracking for training data
- Privacy-by-Design implementation
- Continuous adversarial testing

**Source Quote:**
> "Cohere's North platform includes security protocols like granular access control, agent autonomy policies, continuous red-teaming, and third-party security tests. Cohere meets international compliance standards like GDPR, SOC-2, and ISO 27001. More specifically, Cohere offers certifications including ISO 27001 and ISO 42001, as well as SOC 2 Type II Report."

**Source:** [Cohere Security](https://cohere.com/security) | Published: 2025

---

### Oracle OCI Platform Integration (Ongoing)
**Category:** Cloud Integration | Enterprise
**Type:** Cloud Platform Partnership

**Description:**
Cohere trains and deploys its generative AI models on Oracle Cloud Infrastructure (OCI), with Cohere AI technology integrated into Oracle Fusion Applications. Oracle OCI Generative AI service supports Command A (03-2025), Rerank v3.5, and Embed models. Command A on OCI delivers 150% of the throughput of its predecessor while requiring only two GPUs. Cohere leverages OCI Kubernetes Engine (OKE) and AMD Instinct MI355X GPUs to deliver secure, efficient, and scalable AI solutions. Over 100 generative AI use cases deployed with Oracle.

**Platform Building Capabilities:**
- Native OCI integration for Oracle customers
- Kubernetes-based deployment via OKE
- AMD GPU optimization for training and inference
- Integration with Oracle Fusion Applications
- Enterprise-scale deployment options
- Sovereign AI deployment capabilities

**Source Quote:**
> "Through its partnership with Cohere—a leader in secure, enterprise-grade LLMs—Oracle provides customers with access to powerful, cost-efficient AI capabilities designed for impactful business outcomes. Cohere's Command A 03-2025 is the most performant Command model to date, delivering 150% of the throughput of its predecessor (Command R+08-2024) while requiring only two GPUs. Cohere used Oracle Cloud Infrastructure Kubernetes Engine (OKE) and GPUs hosted on Oracle Cloud Infrastructure (OCI) to ensure that its world-class AI solution was leveraged at the enterprise level, across the world."

**Source:** [Oracle Cohere Partnership](https://www.oracle.com/cloud/technical-case-studies/cohere/) | Published: 2025

---

### Fine-Tuning Platform Updates (2025)
**Category:** Developer Tools | Enterprise
**Type:** Platform Feature

**Description:**
Cohere's fine-tuning service allows customization of Command R model (command-r-08-2024) with LoRA-based fine-tuning, with training context length extended to 16,384 tokens. Custom models designed for specialized use cases requiring proprietary model trained on deep domain expertise. Organizations can fine-tune models on proprietary data while maintaining complete data ownership and privacy. Fine-tuning typically improves task-specific performance by 20-40% compared to base models. Supported models include Command R, Command R+, Command R7B, Command A, Aya Expanse 8B and 32B.

**Platform Building Capabilities:**
- LoRA-based fine-tuning for efficiency
- Extended context length (16,384 tokens)
- Proprietary data training with privacy preservation
- 20-40% performance improvement for specialized tasks
- Support for multiple model families
- Open-source fine-tuning tools available

**Source Quote:**
> "Custom models are designed for specialized use cases that require a proprietary model trained on deep domain expertise, allowing alignment with specific user expectations like tone, voice, and ethics. Cohere allows organizations to fine-tune models on proprietary data while maintaining complete data ownership and privacy, with the fine-tuning process typically improving task-specific performance by 20-40% compared to base models."

**Source:** [Cohere Fine-Tuning](https://cohere.com/fine-tuning) | Published: 2025

---

### Dashboard UI and Production Key Updates (2025)
**Category:** Developer Tools
**Type:** Platform Improvement

**Description:**
Cohere released dashboard improvements including enhanced UI, production API keys, flat-rate pricing options, and improved team collaboration and model insights capabilities. The updates include better user interface design, enhanced team collaboration features, and improved model insights for tracking usage and performance.

**Source Quote:**
> "Cohere has released updates that include improved UI, along with production keys, flat-rate pricing, and enhanced team collaboration and model insights."

**Source:** [Cohere Changelog - Pricing Update and New Dashboard UI](https://docs.cohere.com/changelog/pricing-update-and-new-dashboard-ui) | Published: 2025

---

### January 2026 - Defense and Government Partnerships
**Category:** Enterprise
**Type:** Vertical Expansion

**Description:**
TKMS and Cohere signed a Teaming Agreement to integrate advanced AI technologies into the Canadian Patrol Submarine Program (CPSP), exploring applications of language and data-driven models for decision-support workflows, onboard information management, training environments, and secure naval interfaces. This builds on December 2025 partnership with Thales Canada using North agentic AI platform to enhance defense operational efficiency and readiness.

**Source Quote:**
> "TKMS and Cohere signed a Teaming Agreement to jointly explore the integration of advanced AI technologies into the Canadian Patrol Submarine Program (CPSP). The companies will assess opportunities to apply language and data-driven models to support decision-support workflows, onboard information management, training environments, and secure naval interfaces."

**Source:** [Cantech Letter](https://www.cantechletter.com/newswires/tkms-and-cohere-sign-teaming-agreement-to-advance-ai-enabled-capabilities-for-the-canadian-patrol-submarine-project/) | Published: January 2026

---

## Summary by Platform Category

### North Platform (Cohere's Core Building Platform)
- General availability (August 2025)
- Low-code agent building without technical expertise
- Multi-agent orchestration capabilities
- Model Context Protocol (MCP) server support
- Private deployment (on-premises, VPC, hybrid, air-gapped)
- Minimal hardware requirements (2 GPUs)
- North for Banking vertical (RBC partnership)
- Agent Studio for custom agent creation
- Granular access controls and autonomy policies

### RAG & Retrieval Stack
- Cohere Toolkit (open-source RAG components)
- 100+ prebuilt connectors (Asana, Slack, GitHub, databases)
- Build-your-own-connector framework
- Quick-start connectors repository
- Rerank 4.0 (32K context, multilingual, semi-structured data)
- Embed v4 (multimodal, 100+ languages, industry-specific)

### Building Block APIs
- Command A (111B params, 256K context, tool use)
- Command A Vision (multimodal, 128K context, 20 images)
- Command A Reasoning (111B params, multi-step reasoning)
- Command A Translate (23 languages, 16K context)
- Aya Expanse 8B/32B (multilingual, open weights)
- Embed v4 (multimodal embeddings)
- Rerank 4.0 Pro and Fast (search optimization)

### Enterprise Deployment
- Private deployments (VPC, on-premises, air-gapped)
- Cloud integrations (AWS Bedrock, Azure AI Foundry, Oracle OCI, AWS Sagemaker)
- 85% of revenue from private deployments
- Security: GDPR, SOC 2, ISO 27001, ISO 42001
- TLS encryption, AES-256 data encryption
- Pass-through identity, role-based access
- Continuous red-teaming

### Developer Experience
- API v2 with improved structure and SSE streaming
- New SDKs: Python, TypeScript, Java, Go (ClientV2)
- Multi-step tool use and sequential reasoning
- JSON schema-based tool definitions
- Enhanced citation options
- Production API keys
- Improved dashboard UI
- Comprehensive documentation

### Cloud Platform Integrations
- AWS Bedrock (serverless, pay-as-you-go)
- Azure AI Foundry (first-party models, Managed Compute)
- Oracle OCI (Kubernetes Engine integration, AMD GPU optimization)
- Cross-region inference capabilities
- Sovereign AI deployment options

### Notable Customers and Use Cases
- RBC (North for Banking)
- Dell (North enterprise deployment)
- LG CNS (South Korea deployment)
- Ensemble Health Partners (healthcare agentic AI)
- Second Front (defense)
- Palantir (enterprise)
- Oracle (100+ generative AI use cases)

---

## Sources

- [Cohere North GA Blog](https://cohere.com/blog/north-ga)
- [TechCrunch - North Launch](https://techcrunch.com/2025/08/06/coheres-new-ai-agent-platform-north-promises-to-keep-enterprise-data-secure/)
- [BetaKit - North GA](https://betakit.com/cohere-pitches-security-and-productivity-with-general-release-of-north-enterprise-ai-platform/)
- [TechCrunch - Funding Round](https://techcrunch.com/2025/08/14/cohere-hits-a-6-8b-valuation-as-investors-amd-nvidia-and-salesforce-double-down/)
- [Cohere Blog - September Funding](https://cohere.com/blog/september-2025-funding-round)
- [Cohere Release Notes](https://docs.cohere.com/changelog)
- [Cohere Command A Reasoning Documentation](https://docs.cohere.com/docs/command-a-reasoning)
- [VentureBeat - Command A Reasoning](https://venturebeat.com/ai/dont-sleep-on-cohere-command-a-reasoning-its-first-reasoning-model-is-built-for-enterprise-customer-service-and-more)
- [Cohere Blog - Rerank 4](https://cohere.com/blog/rerank-4)
- [Microsoft Tech Community - Rerank 4.0](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-cohere-rerank-4-0-in-microsoft-foundry/4477076)
- [AWS What's New - Embed v4](https://aws.amazon.com/about-aws/whats-new/2025/10/coheres-embed-v4-multimodal-embeddings-bedrock/)
- [AWS Blog - Embed 4 Enterprise Search](https://aws.amazon.com/blogs/machine-learning/powering-enterprise-search-with-the-cohere-embed-4-multimodal-embeddings-model-in-amazon-bedrock/)
- [Microsoft Tech Community - Foundry Models](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-models-at-ignite-2025-why-integration-wins-in-enterprise-ai/4470776)
- [Cohere Command A Vision Announcement](https://docs.cohere.com/v1/changelog/2025-07-31-command-a-vision)
- [HuggingFace - Command A Vision](https://huggingface.co/blog/CohereLabs/introducing-command-a-vision-07-2025)
- [Cohere Blog - Aya Expanse](https://cohere.com/blog/aya-expanse-connecting-our-world)
- [MultiLingual - Aya Expanse](https://multilingual.com/cohere-releases-aya-expanse-multilingual-ai-models/)
- [GitHub - Cohere Toolkit](https://github.com/cohere-ai/cohere-toolkit)
- [Cohere Toolkit Documentation](https://docs.cohere.com/v2/docs/cohere-toolkit)
- [GitHub - Quick Start Connectors](https://github.com/cohere-ai/quick-start-connectors)
- [Cohere Blog - New API v2](https://cohere.com/blog/new-api-v2)
- [Cohere Multi-Step Tool Use Documentation](https://docs.cohere.com/docs/multi-step-tool-use)
- [RBC Newsroom](https://www.rbc.com/newsroom/news/article.html?article=125967)
- [Oracle Cohere Partnership](https://www.oracle.com/cloud/technical-case-studies/cohere/)
- [Oracle Blog - Command A Rerank OCI](https://blogs.oracle.com/ai-and-datascience/cohere-command-a-rerank-oci-gen-ai)
- [Cohere Security](https://cohere.com/security)
- [Cohere Enterprise Data Commitments](https://cohere.com/enterprise-data-commitments)
- [Cohere Deployment Options](https://cohere.com/deployment-options)
- [Cohere Fine-Tuning](https://cohere.com/fine-tuning)
- [Cohere Pricing](https://cohere.com/pricing)
- [Slator - AfriAya Dataset](https://slator.com/cohere-labs-launches-vision-language-dataset-for-african-languages/)
- [Cantech Letter - TKMS Partnership](https://www.cantechletter.com/newswires/tkms-and-cohere-sign-teaming-agreement-to-advance-ai-enabled-capabilities-for-the-canadian-patrol-submarine-project/)
- [BetaKit - Thales Partnership](https://betakit.com/cohere-announces-partnership-with-thales-canada-amid-defence-tech-push/)
- [Cohere North Agent Studio](https://cohere.com/north/agent-studio)
- [InfoWorld - North Agentic AI](https://www.infoworld.com/article/3757962/cohere-goes-north-with-agentic-ai.html)
