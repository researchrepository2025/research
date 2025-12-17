# Palantir Products & Capabilities

## Executive Summary

Palantir Technologies operates three core platforms: Foundry (enterprise operations), Gotham (defense and intelligence), and AIP (Artificial Intelligence Platform), all powered by Apollo (continuous delivery infrastructure). As of Q3 2025, Palantir achieved record financial performance with 63% year-over-year revenue growth to $1.181 billion, driven primarily by AIP adoption. The company's Ontology layer serves as the technical foundation that bridges fragmented data with operational decision-making across all platforms.

## Foundry

### What Foundry Is

Palantir Foundry is described as "The Ontology/AI-powered operating system for the modern enterprise" designed to help organizations "Run your business as code."

**Source**: [Palantir Foundry](https://www.palantir.com/platforms/foundry/)

### Core Capabilities and Features

**Data Integration and Management**:
- Integrates structured and unstructured data from typically disconnected systems
- Features back-end and front-end tools for integrating siloed data
- Supports federated data sources with dynamic updates
- Provides a single workspace for different analytical workflows (geospatial, network, CDR, etc.)

**Source**: [Palantir Gotham Profile](https://www.softwareadvice.com/bi/palantir-gotham-profile/)

**Products and Tools**:
- AIP Agents: Interactive assistants built in AIP Agent Studio equipped with enterprise-specific information and tools
- Media sets, Ontologies, Admin, Connectivity, Datasets, Filesystem
- Orchestration, SQL Queries, and Streams for real-time operational data analysis

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

### 2025 Key Updates

**AI and Machine Learning Enhancements**:
- Bring-your-own-model (BYOM) capability provides first-class support for customers who want to connect their own LLMs to use in AIP with all Palantir developer products, including AIP Logic, Pipeline Builder, Agent Studio, and Workshop
- AIP Logic users can now automatically generate test cases and evaluators for functions using AIP Evals, making it easier to evaluate and improve AI functions

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

**Code Workspaces and Data Analysis** (October 2025):
- Users can write and execute arbitrary code to analyze restricted views directly within Jupyter workspaces
- Users can publish interactive Dash and Streamlit dashboards based on restricted views

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

**Consumer Mode**:
- Enables organizations to deliver secure, scalable applications to external users
- Allows B2C and B2B solutions while containing users within specific applications without broader platform access

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

**Development Tools**:
- TypeScript v2 functions became generally available in July 2025, offering powerful improvements to platform workflows
- Users can develop Python transforms locally inside their own instance of Visual Studio Code
- Foundry Branching provides a unified experience to make changes across multiple applications on a single branch and test changes end-to-end (beta starting May 2025)

**Sources**:
- [Foundry Announcements July 2025](https://www.palantir.com/docs/foundry/announcements/2025-07)
- [Foundry Announcements May 2025](https://www.palantir.com/docs/foundry/announcements/2025-05)

**Marketplace and DevOps**:
- New DevOps packaging experience introduces a fully redesigned packaging experience built for speed, bulk operations, and an intuitive workflow
- Python functions can be deployed through Marketplace, enabling distribution of products within organizations and the Foundry community

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

**Monitoring and Security**:
- Monitoring capabilities for functions and actions are available, allowing users to track resources across the platform and send notifications through multiple channels when alerts are triggered
- Media set scanning helps detect sensitive content in unstructured data, improving data protection posture

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

**Enterprise Integrations**:
- Version 2.35.0 of the Foundry Connector 2.0 for SAP Applications is available, connecting Foundry to SAP systems
- Claude Haiku 4.5 is now available from Anthropic Direct, Amazon Bedrock, and Google Vertex AI for various enrollments

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

### Who Uses Foundry

As of May 2025, four US federal agencies, including the Department of Homeland Security and the Department of Health and Human Services, used Foundry.

**Source**: [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)

Recent enterprise adoption examples include:
- Walgreens deployed AI-powered workflows to 4,000 stores in just eight months
- AIG reported its agentic AI ecosystem with Palantir, Anthropic, and AWS can accelerate the underwriting process up to 5X

**Source**: [Palantir AIP Overview](https://www.palantir.com/docs/foundry/aip/overview)

## Gotham

### What Gotham Is

Palantir Gotham serves as "The Operating System for Defense Decision Making" and "The Operating System for Global Decision Making."

**Source**: [Palantir Gotham](https://www.palantir.com/platforms/gotham/)

### How It Differs from Foundry

While Foundry serves as a general-purpose data platform for analysis and operations across industries, Gotham specifically targets defense and intelligence operations. Gotham is described as an "AI-ready operating system that improves and accelerates decisions for operators across roles and all domains" within defense contexts.

**Source**: [Palantir Gotham](https://www.palantir.com/platforms/gotham/)

Released in 2008, Palantir Gotham is Palantir's defense and intelligence software. It is an evolution of Palantir's longstanding work in the United States Intelligence Community, and is used by intelligence and defense agencies.

**Source**: [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)

### Target Use Cases

**Primary Users**:
- Global defense agencies
- Intelligence community organizations
- Law enforcement and disaster relief organizations
- Decision makers ranging from headquarters to forward-deployed personnel

**Source**: [Palantir Gotham](https://www.palantir.com/platforms/gotham/)

### Key Capabilities

**Data Integration and Visualization**:
- Joins and enriches massive volumes of near-real-time data and presents them in a single view that enables users to make faster, more confident decisions, together
- Handles thousands of users and millions of sensors through a single interface
- Provides decision-makers access to the most recent understanding of the world

**Source**: [Palantir Gotham](https://www.palantir.com/platforms/gotham/)

**Defense & Intelligence Operations**:
- Supports alerts, geospatial analysis, and prediction
- Gotham's targeting offering supports soldiers with an AI-powered kill chain, seamlessly and responsibly integrating target identification and target effector pairing
- Operators experience enhanced situational awareness and effectiveness as Gotham streamlines critical decision-making in the modern battlespace

**Sources**:
- [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)
- [Palantir Gotham Powers Next-Gen Data Intelligence](https://finance.yahoo.com/news/palantir-gotham-powers-next-gen-140500701.html)

**Satellite & Sensor Integration**:
- Allows tasking of satellites anywhere in the world by integrating with existing satellite constellations
- Optimizes hundreds of orbital sensors to answer time-sensitive questions
- Enables precise, dynamic orchestration of models to ensure the right models are processing the right sensor data at the right time and location
- Enables the autonomous tasking of sensors, from drones to satellites, based on AI-driven rules or manual inputs for human-in-the-loop control

**Source**: [Palantir Gotham Powers Next-Gen Data Intelligence](https://finance.yahoo.com/news/palantir-gotham-powers-next-gen-140500701.html)

**Edge & Mixed Reality**:
- Palantir's Mixed Reality capability enables operators and commanders to collaborate in a virtual operations center in edge environments
- Gotham's edge capabilities enable operators to gain critical insights even in the most adverse, disconnected, and distributed environments
- Gotham is configurable to run on everything from remote devices to operations centers powered by government cloud networks

**Source**: [Palantir Gotham Powers Next-Gen Data Intelligence](https://finance.yahoo.com/news/palantir-gotham-powers-next-gen-140500701.html)

**AI Integration**:
- Features built-in feedback loops that train and refine models that augment human analysis and decision making during operations
- Operator actions continuously improve model performance
- The launch of Palantir's Artificial Intelligence Platform (AIP) in April 2023 marked a fundamental shift
- The platform now integrates with large language models from OpenAI, Anthropic, Google, and others, all within military-grade security frameworks
- A groundbreaking partnership with Microsoft in August 2024 brought GPT-4 capabilities to classified networks for the first time

**Sources**:
- [Palantir Gotham](https://www.palantir.com/platforms/gotham/)
- [Palantir Gotham Powers Next-Gen Data Intelligence](https://finance.yahoo.com/news/palantir-gotham-powers-next-gen-140500701.html)

**Security & Compliance**:
- Role-based access control, meaning only users with appropriate authority can access specific features
- Compliant with SSAE18 SOC 2 Type II, ISAE 3000 SOC 2 Type II, FedRamp Moderate, ISO 27001, ISO 27017 and Cyber Essentials
- Maintains certifications including FedRAMP Moderate, IL-5 DoD SRG, SOC 2 Type II, and ISO 27001

**Sources**:
- [Palantir Gotham Profile](https://www.softwareadvice.com/bi/palantir-gotham-profile/)
- [Palantir Gotham](https://www.palantir.com/platforms/gotham/)

**Interoperability**:
- Connects seamlessly with existing government systems
- Maintains granular security controls
- Allows data export with provenance

**Source**: [Palantir Gotham](https://www.palantir.com/platforms/gotham/)

## AIP (Artificial Intelligence Platform)

### What AIP Is and Launch Date

Palantir's Artificial Intelligence Platform (AIP) connects AI with your data and operations. In April 2023, the company launched Artificial Intelligence Platform (AIP), which integrates large language models into privately operated networks.

**Sources**:
- [Palantir AIP Overview](https://www.palantir.com/docs/foundry/aip/overview)
- [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)

### Core Features and Capabilities

**Builder Tools**:
AIP's builder tools like AIP Logic, AIP Agent Studio, and AIP Evals enable the development of production-ready AI-powered workflows, agents, and functions on top of the Ontology and developer toolchain.

**Source**: [Palantir AIP Overview](https://www.palantir.com/docs/foundry/aip/overview)

**Platform Integration**:
Together with Foundry (Palantir's data operations platform) and Apollo (Palantir's mission control for autonomous software deployment), AIP forms an operating system that can deliver a full range of AI-driven products, from LLM-powered web applications to mobile applications using vision-language models.

**Source**: [Palantir AIP Overview](https://www.palantir.com/docs/foundry/aip/overview)

**Model Support**:
AIP provides a comprehensive suite of tools for building, training, and deploying large language models. Supporting a range of different large language models allows data scientists and engineers to work with their preferred tools and pick the models that are best suited for each use case.

**Source**: [Palantir AIP Overview](https://www.palantir.com/docs/foundry/aip/overview)

**Security and Governance**:
- AIP incorporates all of Palantir's advanced security measures for the protection of sensitive data in compliance with industry regulations
- AIP provides robust access controls, encryption, and auditing capabilities to maintain data integrity and transparency
- Built-in governance tools help organizations maintain accountability and historical lineage in AI operations
- AIP Agent Studio is built on the same rigorous security model that governs the rest of the Palantir platform
- These platform security controls grant an LLM access only to what is necessary to complete a task

**Sources**:
- [Unit8 Palantir Foundry AIP](https://unit8.com/resources/palantir-foundry-aip/)
- [AIP Agent Studio Overview](https://www.palantir.com/docs/foundry/agent-studio/overview)

### AI Agents in Palantir's Context

**AIP Agent Studio Overview**:
AIP Agents can be integrated into applications to facilitate dynamic, context-aware read and write workflows that enable you to automate tasks and reduce manual application interactions.

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

**Tool Types Available for Agents**:
- **Action**: Gives your agent the ability to execute an ontology edit. This can be configured to run automatically or to run after confirmation from the user
- **Object query**: Specifies the object types that the LLM can access. You can add multiple object types and specify accessible properties to make queries more token-efficient. The object query tool supports filtering, aggregation, inspection, and traversal of links for configured objects
- **Function**: Allows the LLM to call any Foundry function, including published AIP Logic functions. The latest version of the function is automatically used, but you can also specify a published version for more granular control
- **Update application variable**: Used to update the value of an application variable configured in the Application state tab
- **Command**: These tools enable your agent to trigger operations in other Palantir applications using one or multiple commands

**Source**: [AIP Agent Studio Tools Overview](https://www.palantir.com/docs/foundry/agent-studio/tools)

### Key 2025 Updates and Capabilities

**Native Tool Calling** (August 2025):
- Native tool calling mode is now available in AIP Agent Studio, allowing agents to leverage built-in tool calling capabilities of supported models for improved speed and performance
- Previously, agents with tools were limited to Prompted tool calling mode, which used additional prompt instructions and allowed only one tool call at a time
- Native tool calling uses the built-in capabilities of supported models to provide tools and allow the LLM to call these tools directly
- Offers improved speed and performance over prompted tool calling, due to greater token efficiency and the ability for agents in this mode to call multiple tools in parallel

**Source**: [Foundry Announcements August 2025](https://www.palantir.com/docs/foundry/announcements/2025-08)

**Custom Retrieval Functions** (February 2025):
- AIP Agents now support custom retrieval Functions, a pro-code feature that enables builders to configure their own logic for context retrieval on each query
- Ideal for situations where the retrieval methods provided out-of-the-box through Ontology context or document context do not satisfy a given use case
- Example: If a user wants to run a semantic search over multiple Ontology object types, the user can configure a Function for it even though it is not currently supported in AIP Agent Studio
- You can now use Function-backed context to perform custom retrieval on each query in AIP Agent Studio

**Source**: [Foundry Announcements February 2025](https://www.palantir.com/docs/foundry/announcements/2025-02)

**Conversation Retention** (May 2025):
- Indefinite conversation retention is now supported in AIP Agent Studio and AIP Threads
- Allows users to access conversation history and context past the previous limit of 24 hours
- This feature is optional in AIP Agent Studio, and is on by default for most configurations in AIP Threads

**Source**: [Foundry Announcements May 2025](https://www.palantir.com/docs/foundry/announcements/2025-05)

**Debug View** (October 2025):
- AIP Evals now provides an integrated debug view directly within the Results dialog accessible from the AIP Logic and Agent Studio sidebars
- This new view allows you to access debugging information without opening the separate metrics dashboard, making it easier to analyze evaluation results

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

**Integration Capabilities**:
- You can use AIP Agents in AIP Threads or OSDK applications with platform APIs
- Incorporate AIP Agents into Workshop using the AIP Interactive widget or third-party OSDK applications using Developer Console and platform APIs
- Automate and delegate tasks to your agent, enabling agents to handle complex workflows autonomously
- Start by publishing your agent as a function and pulling it into AIP Automate

**Source**: [AIP Agent Studio Overview](https://www.palantir.com/docs/foundry/agent-studio/overview)

**Model Support in 2025**:
- GPT-5, GPT-5 mini, GPT-5 nano from OpenAI are now available for general use in AIP. GPT-5 is best suited for complex, real-world tasks across coding, writing, health, and multimodal reasoning
- Claude Opus 4.1 is Anthropic's leading hybrid reasoning model, designed for demanding coding, agentic search, and AI agent tasks
- Gemini 2.5 Pro, Gemini 2.5 Flash, and Gemini 2.5 Flash Lite from Google Vertex are now available for general use in AIP

**Source**: [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)

### 2025 Business Performance

- AIP adoption is snowballing, pushing U.S. commercial revenue up 71% year over year and 19% sequentially in the first quarter of 2025, breaking the $1 billion annual run rate barrier for the first time
- The company reported a 45% year-over-year jump in its customer count in Q3, with commercial customers growing at a faster pace of 49%

**Source**: [Palantir AIP Platform Adoption](https://finance.yahoo.com/news/palantirs-aip-platform-sees-soaring-090200252.html)

## Apollo

### What Apollo Is

Palantir Apollo is Palantir's continuous delivery and day 2 operations platform. It's a platform designed to facilitate continuous integration/continuous delivery (CI/CD) across all environments.

**Sources**:
- [Palantir Apollo](https://www.palantir.com/platforms/apollo/)
- [Palantir Apollo Reviews](https://sourceforge.net/software/product/Palantir-Apollo/)

### Role and Purpose

Apollo was conceived alongside Foundry, initially built as the automation and delivery infrastructure for public-cloud SaaS. However, given Palantir's roots in classified and on-prem environments, they knew a traditional SaaS based on a single public cloud provider wouldn't work everywhere. They needed unified tooling to bring the same SaaS platform to all customers, regardless of environment constraints. So they built Apollo to run as its own standalone platform—independent, decoupled from Foundry, running as a layer between applications and the underlying infrastructure.

**Source**: [Palantir Apollo Blog](https://blog.palantir.com/palantir-apollo-powering-saas-where-no-saas-has-gone-before-7be3e565c379)

Apollo is the continuous delivery and deployment platform for Palantir Foundry. It enables delivery teams to manage and promote Foundry applications—Ontologies, Pipelines, Workflows, Code Repositories, and UI tools—across isolated, secure, and cloud-disconnected environments.

**Source**: [Apollo Welcome](https://www.palantir.com/docs/apollo/apollo-getting-started/introduction-welcome)

### Continuous Delivery Capabilities

**Unified Dev, Sec, and Ops**:
Apollo unifies Dev, Sec, and Ops with autonomous software deployment, increasing release speed, supporting full rollbacks, and cutting DevOps costs.

**Source**: [Palantir Apollo](https://www.palantir.com/platforms/apollo/)

**Continuous Automated Updates**:
- Apollo works around the clock to put the latest features in the hands of customers
- Eliminates the tradeoff between stability and speed by delivering continuous, automated updates without disrupting operations
- Performs safe deploys with staged blue-green upgrades and observes the roll-out process
- If it notices an emergent issue, it begins a roll-back process, notifies the relevant development team, and avoids an outage
- If successful, it moves on to the next service, and repeats—continuously delivering incremental, automatic updates

**Sources**:
- [Palantir Apollo](https://www.palantir.com/platforms/apollo/)
- [Palantir Apollo Blog](https://blog.palantir.com/palantir-apollo-powering-saas-where-no-saas-has-gone-before-7be3e565c379)

**Deployment Frequency**:
Apollo continuously delivers incremental, automatic updates for the fleet over 41,000 times a week.

**Source**: [Palantir Apollo Blog](https://blog.palantir.com/palantir-apollo-powering-saas-where-no-saas-has-gone-before-7be3e565c379)

### Multi-Environment Deployment Features

Apollo autonomously deploys software to some of the most complex environments in the world:
- Multi-cloud
- Low to high networks
- Edge devices or assets

**Source**: [Palantir Apollo](https://www.palantir.com/platforms/apollo/)

## Ontology (Foundation Layer)

### What the Ontology Is

The Palantir Ontology is an operational layer for the organization. It sits on top of the digital assets integrated into the Palantir platform (datasets, virtual tables, and models) and connects them to their real-world counterparts, ranging from physical assets like plants, equipment, and products to concepts like customer orders or financial transactions.

**Source**: [Understanding the Palantir Ontology](https://blog.pvmit.com/pvm-blog/palantir-ontology)

An Ontology is a categorization of the world. In Foundry, the Ontology is the digital twin of an organization, a rich semantic layer that sits on top of the digital assets (datasets and models) integrated into Foundry.

**Source**: [Ontology Overview](https://www.palantir.com/docs/foundry/ontology/overview)

### Core Components

The Foundry Ontology creates a complete picture of an organization's world by mapping datasets and models to:
- **Object types**: Define an entity or event in an organization
- **Properties**: Define the object type's characteristics
- **Link types**: Define the relationship between two object types
- **Action types**: Define how an object type can be modified

**Source**: [Ontology Overview](https://www.palantir.com/docs/foundry/ontology/overview)

### Three Core Layers

1. **Semantic Layer**: The core of the ontology. It defines the conceptual model of your domain—what entities exist, how they relate to one another, and what properties they have

2. **Kinetic Layer**: Operationalizes your ontology, ensuring it's fed with up-to-date, accurate information

3. **Dynamic Layer**: Introduces behavior to the ontology. This is where business rules, policies, workflows, and permissions live

**Source**: [Understanding Palantir's Ontology](https://pythonebasta.medium.com/understanding-palantirs-ontology-semantic-kinetic-and-dynamic-layers-explained-c1c25b39ea3c)

### Strategic Importance

Mizuho analysts describe it as a tool "which fragmented data can be unified and transformed into operational knowledge." Goldman analysts call Ontology the "core technical differentiation" that "bridges the gap between the raw data across an organization (structured, unstructured, siloed, etc.) and operational decision-making."

**Source**: [What the heck is Palantir's Ontology](https://sherwood.news/markets/what-the-heck-is-palantirs-ontology/)

Example: In a global manufacturer's ontology, "the 'supplier' represents a business partner, with direct connections to shipments," and "if a shipment is delayed, all affected products, warehouses, and suppliers are automatically updated in the ontology."

**Source**: [What the heck is Palantir's Ontology](https://sherwood.news/markets/what-the-heck-is-palantirs-ontology/)

## 2025 Product Updates

### Q3 2025 Financial Performance

- Palantir delivered its strongest quarter ever, with Q3 revenue up 63% YoY and 18% QoQ to $1.181 billion, far exceeding guidance
- Adjusted operating margin hit a record 51%
- U.S. commercial revenue surged 121% YoY
- Earnings per share (EPS) of $0.21 for Q3 2025, which exceeded analysts' expectations of $0.15 by 40%
- Rule of 40 score of 114, its highest ever, by 20 points
- Third quarter GAAP operating income was $393 million (33% margin), and GAAP net income was $476 million (40% margin)

**Sources**:
- [Palantir Q3 2025 Letter to Shareholders](https://www.palantir.com/q3-2025-letter/en/)
- [Palantir Q3 Earnings 2025](https://www.cnbc.com/2025/11/03/palantir-pltr-q3-earnings-2025.html)

### U.S. Commercial Business Performance

- Palantir's U.S. commercial business more than doubled to $397 million
- Total contract value for U.S. commercial deals closed more than quadrupled to $1.31 billion

**Source**: [Palantir Q3 Earnings 2025](https://www.cnbc.com/2025/11/03/palantir-pltr-q3-earnings-2025.html)

### Strategic Partnerships Announced in 2025

- Partnerships with Snowflake, Lumen, and Nvidia announced in weeks leading up to Q3 earnings
- Palantir AI Platform (AIP) will integrate NVIDIA GPU-accelerated data processing and route optimization libraries, open models and accelerated computing
- This combination of Ontology and NVIDIA AI will support customers by providing the advanced, context-aware reasoning necessary for operational AI
- On November 4, 2025, a joint venture between Palantir and Dubai Holding, the Dubai government's investment arm, was announced

**Sources**:
- [Palantir Q3 Earnings 2025](https://www.cnbc.com/2025/11/03/palantir-pltr-q3-earnings-2025.html)
- [NVIDIA Palantir AI Enterprise Partnership](https://nvidianews.nvidia.com/news/nvidia-palantir-ai-enterprise-data-intelligence)
- [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)

### Major Government Contract (Mid-2025)

In mid-2025, the U.S. Army awarded Palantir an "Enterprise Service Agreement" valued at up to $10 billion over 10 years. This contract consolidates 75 previously separate data and software contracts into a single, massive software contract, allowing the Army to procure Palantir's AI and analytics tools more efficiently and cost-effectively.

**Source**: [Palantir Apollo Reviews](https://sourceforge.net/software/product/Palantir-Apollo/)

### Forward Guidance (Q4 2025)

- Palantir expects revenue of about $1.33 billion for Q4 2025, exceeding the $1.19 billion expected by analysts
- The company is guiding to revenue of $1.329 billion in the fourth quarter, representing 13% growth quarter over quarter and 61% growth year-over-year

**Source**: [Palantir Q3 Earnings 2025](https://www.cnbc.com/2025/11/03/palantir-pltr-q3-earnings-2025.html)

### Stock Performance

Retail investors have helped drive Palantir's skyrocketing stock price. The shares surged more than 170% in 2025, lifting the company's market cap past $490 billion.

**Source**: [Palantir Q3 Earnings 2025](https://www.cnbc.com/2025/11/03/palantir-pltr-q3-earnings-2025.html)

## Sources

### Palantir Official Documentation
- [Palantir Foundry](https://www.palantir.com/platforms/foundry/)
- [Palantir Gotham](https://www.palantir.com/platforms/gotham/)
- [Palantir Artificial Intelligence Platform](https://www.palantir.com/platforms/aip/)
- [Palantir Apollo](https://www.palantir.com/platforms/apollo/)
- [Palantir Ontology](https://www.palantir.com/platforms/ontology/)
- [Ontology Overview - Palantir Docs](https://www.palantir.com/docs/foundry/ontology/overview)
- [AIP Overview - Palantir Docs](https://www.palantir.com/docs/foundry/aip/overview)
- [AIP Agent Studio Overview - Palantir Docs](https://www.palantir.com/docs/foundry/agent-studio/overview)
- [AIP Agent Studio Tools - Palantir Docs](https://www.palantir.com/docs/foundry/agent-studio/tools)
- [Apollo Welcome - Palantir Docs](https://www.palantir.com/docs/apollo/apollo-getting-started/introduction-welcome)

### Palantir Monthly Announcements (2025)
- [Foundry Announcements October 2025](https://www.palantir.com/docs/foundry/announcements/2025-10)
- [Foundry Announcements August 2025](https://www.palantir.com/docs/foundry/announcements/2025-08)
- [Foundry Announcements July 2025](https://www.palantir.com/docs/foundry/announcements/2025-07)
- [Foundry Announcements May 2025](https://www.palantir.com/docs/foundry/announcements/2025-05)
- [Foundry Announcements February 2025](https://www.palantir.com/docs/foundry/announcements/2025-02)

### Financial and Business News
- [Q3 2025 Letter to Shareholders](https://www.palantir.com/q3-2025-letter/en/)
- [Palantir Q3 Earnings 2025 - CNBC](https://www.cnbc.com/2025/11/03/palantir-pltr-q3-earnings-2025.html)
- [Palantir's AIP Platform Sees Soaring Adoption - Yahoo Finance](https://finance.yahoo.com/news/palantirs-aip-platform-sees-soaring-090200252.html)
- [Palantir Gotham Powers Next-Gen Data Intelligence - Yahoo Finance](https://finance.yahoo.com/news/palantir-gotham-powers-next-gen-140500701.html)

### Technical Analysis and Reviews
- [Understanding the Palantir Ontology - PVM Blog](https://blog.pvmit.com/pvm-blog/palantir-ontology)
- [Understanding Palantir's Ontology - Medium](https://pythonebasta.medium.com/understanding-palantirs-ontology-semantic-kinetic-and-dynamic-layers-explained-c1c25b39ea3c)
- [What the heck is Palantir's Ontology - Sherwood News](https://sherwood.news/markets/what-the-heck-is-palantirs-ontology/)
- [Palantir Apollo Blog Post](https://blog.palantir.com/palantir-apollo-powering-saas-where-no-saas-has-gone-before-7be3e565c379)
- [Palantir Foundry AIP - Unit8](https://unit8.com/resources/palantir-foundry-aip/)

### Software Reviews and Directories
- [Palantir Gotham Profile - Software Advice](https://www.softwareadvice.com/bi/palantir-gotham-profile/)
- [Palantir Apollo Reviews - SourceForge](https://sourceforge.net/software/product/Palantir-Apollo/)

### Partnership Announcements
- [NVIDIA and Palantir Partnership - NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-palantir-ai-enterprise-data-intelligence)

### General Reference
- [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)
