# Palantir Technical Architecture

**Research Date**: 2025-12-11
**Scope**: Technical architecture, data model, integration patterns, and deployment options for Palantir's enterprise platform

---

## Executive Summary

Palantir's platform is built around a proprietary **Ontology** - a semantic layer that transforms raw data into a digital twin of an organization's operations. The platform combines data integration tools, a semantic modeling layer, AI orchestration capabilities (AIP), and deployment flexibility across cloud, on-premises, and air-gapped environments. The Ontology enables both humans and AI systems to interact with business concepts (like "Aircraft," "Orders," "Patients") rather than raw tables and columns, creating what Palantir calls an "enterprise operating system."

The platform consists of three core products:
- **Foundry**: Data integration and operations platform
- **AIP**: Artificial Intelligence Platform for LLM-powered workflows and agents
- **Apollo**: Autonomous software deployment and infrastructure management

---

## The Ontology

### What is the Ontology?

The Ontology is Palantir's core differentiator. It is a categorization of the world - in Foundry, the Ontology is the digital twin of an organization, a rich semantic layer that sits on top of the digital assets (datasets and models) integrated into Foundry. It is essentially the "business-aware" representation of an organization's entire data universe, turning raw data into actionable, real-world concepts that both humans and AI systems can understand and reason over.

**Source**: [Palantir Ontology Overview](https://www.palantir.com/docs/foundry/ontology/overview)

The Ontology is not just a buzzword - it's the foundational concept that brings clarity, structure, and meaning to vast, complex data ecosystems. In many settings, the Ontology serves as a digital twin of the organization, containing both the semantic elements (objects, properties, links) and kinetic elements (actions, functions, dynamic security) needed to enable use cases of all types.

**Source**: [Core Concepts - Palantir](https://www.palantir.com/docs/foundry/ontology/core-concepts)

### Three Core Layers

The Palantir Ontology operates across three distinct layers:

1. **Semantic Layer**: The semantic layer is the core of the ontology. It defines the conceptual model of your domain—what entities exist, how they relate to one another, and what properties they have.

2. **Kinetic Layer**: This layer introduces behavior to the ontology through actions, functions, workflows, and business rules that allow users to modify and interact with data.

3. **Dynamic Layer**: The dynamic layer handles business rules, policies, workflows, and permissions that govern how data is accessed and used.

**Source**: [Understanding Palantir's Ontology: Semantic, Kinetic, and Dynamic Layers](https://pythonebasta.medium.com/understanding-palantirs-ontology-semantic-kinetic-and-dynamic-layers-explained-c1c25b39ea3c)

### Core Components

An object type defines an entity or event in an organization. A property defines the object type's characteristics. A link type defines the relationship between two object types. An action type defines how an object type can be modified. A Function is a piece of code-based logic that takes in input parameters and returns an output. Functions are natively integrated with the Ontology: they can take objects and object sets as input, read property values of objects, and be used across action types and applications that build on the Ontology.

**Source**: [Core Concepts - Palantir](https://www.palantir.com/docs/foundry/ontology/core-concepts)

#### Object Types

An object type defines an entity or event in an organization. You can think of each object type as analogous to a dataset; an object is an instance of an object type, just as a row is one entry in a dataset. The columns in a dataset are analogous to properties of an object, as they provide additional information for a given row.

**Source**: [Object and Link Types - Palantir](https://www.palantir.com/docs/foundry/object-link-types/type-reference)

For example, if you have an "Airports" object type, LHR (London Heathrow) would be an individual object instance.

#### Properties

A property of an object type is the schema definition of a characteristic of a real-world entity or event. For example, if LHR is an object type of Airports, "name" and "country" are properties of Airports.

**Source**: [Properties Overview - Palantir](https://www.palantir.com/docs/foundry/object-link-types/properties-overview)

Property base types include:
- Media reference (images, videos, audio, documents)
- Struct (schema-based properties with multiple fields)
- Value types (semantic wrappers with metadata and constraints like email addresses, URLs, UUIDs, and enumerations)

**Shared Properties**: A shared property is a property that can be used on multiple object types in your ontology. Shared properties allow for consistent data modeling across object types and centralized management of property metadata.

**Source**: [Shared Properties - Palantir](https://www.palantir.com/docs/foundry/object-link-types/shared-property-overview/index.html)

#### Link Types

A link type is the schema definition of a relationship between two object types. A link refers to a single instance of that relationship between two objects.

Link types support different cardinalities:
- **Object type foreign keys**: Supports "one-to-one" and "many-to-one" cardinality link types using foreign key and primary key properties
- **Join table dataset**: For "many-to-many" cardinality link types using a join table dataset
- **Backing object type**: Object-backed link types expand on many-to-one cardinality, providing first-class support for object types as a link type storage solution

**Source**: [Link Types - Palantir](https://www.palantir.com/docs/foundry/object-link-types/create-link-type)

#### Interfaces

An interface is an Ontology type that describes the shape of an object type and its capabilities. Interfaces provide object type polymorphism, allowing for consistent modeling of and interaction with object types that share a common shape.

**Source**: [Object and Link Types - Palantir](https://www.palantir.com/docs/foundry/object-link-types/type-reference)

### Ontology SDK (OSDK)

The Ontology SDK (OSDK) makes it possible to defragment the enterprise by integrating isolated components into a holistic system. The programmer interacts with these business concepts using the OSDK and writes code in the language of the business — not in terms of rows and columns, but in terms of Airplanes, Flight Schedules, and Airports. The OSDK isn't providing a generic API for our product — it's providing a toolkit for building APIs for your business, in the language of your business.

**Source**: [Ontology-Oriented Software Development](https://blog.palantir.com/ontology-oriented-software-development-68d7353fdb12)

### Evolution Timeline

- **2021–2022**: Formal "Ontology" introduced as a first-class product in Foundry
- **2023–2025**: Massive push with Palantir AIP — the ontology is now the backbone for enterprise AI agents
- **2024–2025**: Introduction of Interfaces, derived properties, better SDKs, and Ontology-Backed Objects in AIP

**Source**: [Understanding Palantir's Ontology](https://pythonebasta.medium.com/understanding-palantirs-ontology-semantic-kinetic-and-dynamic-layers-explained-c1c25b39ea3c)

---

## Backend Architecture

### Object Storage V2

The Foundry platform uses a microservices architecture in which multiple services together comprise the Ontology backend. As Foundry gained more capabilities and evolved to meet the complex operational needs and growing scale of Palantir's customers, Object Storage V2 was built from first principles to enable the next generation of Ontology-driven use cases and workflows.

The new architecture separates dimensions of concern that had been consolidated in Object Storage V1 (Phonograph) and decouples responsibilities within the system design. By separating the subsystems responsible for indexing and querying data, Object Storage V2 can scale horizontally more easily.

Key features include:
- Significantly improved performance for Ontology data indexing through incremental object indexing (enabled by default) for all object types
- Low-latency data indexing into the Ontology through support of streaming datasources
- Supports a maximum of 2000 properties per object type
- Higher-scale Search Arounds and more accurate aggregations through a Spark-based query execution layer
- By default, the Search Around limit is 100,000 objects

**Source**: [Ontology Architecture - Palantir](https://www.palantir.com/docs/foundry/object-backend/overview)

### Object Data Funnel

The Object Data Funnel ("Funnel") is a microservice in the Object Storage V2 architecture responsible for orchestrating data writes into the Ontology. Funnel reads data from Foundry datasources (such as datasets, restricted views, and streaming datasources) and user edits (from Actions) and indexes these data into object databases. Funnel also ensures that indexed data is kept up-to-date as the underlying datasources update.

**Source**: [Ontology Architecture - Palantir](https://www.palantir.com/docs/foundry/object-backend/overview)

---

## Data Model & Semantic Layer

### Difference from Traditional Data Warehouses

Palantir's Ontology abstracts complex technical data into operational objects—aircraft, supply chains, financial entities—that mirror how the business itself operates. This differs from traditional data warehouses where users interact with tables, columns, and SQL queries. The Ontology sits on top of the digital assets integrated into Foundry (datasets and models) and connects them to their real-world counterparts, ranging from physical assets like plants, equipment, and products to concepts like customer orders or financial transactions.

**Source**: [Palantir's Ontology, Kimball's Star Schema, and Model-Driven Data Engineering](https://medium.com/business-friendly-data-modeling/palantirs-ontology-kimball-s-star-schema-and-model-driven-data-engineering-a-comparative-view-8b175464c42a)

### Relationship Between Raw Data and Ontology

The Ontology is a rich semantic layer that sits on top of digital assets (datasets and models) integrated into Foundry. Raw data flows through data integration pipelines, gets transformed via Pipeline Builder or Code Repositories, and then gets mapped to the Ontology layer where it becomes accessible as business objects.

Business logic can be authored directly within the Palantir platform using:
- **Rules and Pipeline Builder**: For logic in data pipelines
- **Automate and Functions**: For logic that will be executed live
- **External Functions and Webhooks**: For connecting to external systems

**Source**: [Automate Overview - Palantir](https://www.palantir.com/docs/foundry/automate/overview)

### Closed vs. Open Architecture

Palantir's Foundry platform popularized the concept of an ontology-centric enterprise OS. However, this model comes at a cost: it is proprietary and closed by design. Foundry's ontologies are defined within its own object framework, supported by ingestion-based pipelines and custom APIs. While powerful, this approach creates dependencies that bind customers to the Palantir ecosystem.

**Source**: [Closed or Open Architectured Ontologies](https://medium.com/timbr-ai/palantir-timbr-the-enterprise-race-to-make-data-ai-ready-4b26a1efe89c)

---

## Integration Architecture

### Data Connection Framework

Palantir's integration begins with an extensible data connection framework that establishes connections with all types of source systems - structured, unstructured, or semi-structured – and with all key data transfer approaches, such as batch, micro-batch, or streaming. This functionality is integrated with the platform's data transformation and data management functionality, which includes full lineage of data versions, granular security for collaborative management of data extraction, and branching of data sync configurations.

**Source**: [Data Connection Architecture - Palantir](https://www.palantir.com/docs/foundry/data-connection/architecture)

### Data Sources Supported

Palantir can connect data from 200+ sources to inform operations. Foundry's tools for connecting to data support the full range of standard enterprise data sources, ranging from cloud-based object stores, file systems, and databases and data warehouses. Foundry provides out-of-the-box integration with well-known system types (e.g., relational databases, FTPS, HDFS, S3, SFTP, and local directories) as well as the flexibility to connect and sync data from new system types.

**Source**: [Data Integration Overview - Palantir](https://www.palantir.com/docs/foundry/data-integration/overview)

For systems without a dedicated connector, the generic connector or REST API source may be used with code-based connectivity options such as external transforms, external functions, and compute modules.

**Source**: [Data Connection Overview - Palantir](https://www.palantir.com/docs/foundry/data-connection/overview)

### Agent Architecture

Palantir uses two primary agent architectures for accessing data on private networks:

#### Agent Proxy (Recommended)

Foundry worker with agent proxy policies is the recommended architecture to access external systems hosted on private networks. It requires the use of a data connection agent. In this scenario, the agent acts as a simple network tunnel without performing any data processing itself. All data connection and computation capabilities are executed by a Foundry worker, an isolated container with scalable compute resources that processes data and communicates with external systems via the provided websocket.

#### Agent Worker (Historical)

Agent worker connection is the historical architecture used to access external systems hosted on private networks from Foundry. Except for specific file-based syncs filtering large amounts of data or micro-batching workflows, agent proxy connections are recommended for accessing on-premise or privately hosted systems.

**Source**: [Data Connection Core Concepts - Palantir](https://www.palantir.com/docs/foundry/data-connection/core-concepts)

### Streaming Data Integration

#### Architecture

Palantir's data streaming architecture stores data in a clustered and highly-available data storage solution such as Kafka. A Compute Engine such as Apache Flink is used to run distributed streaming transformations and computations on the stored data. The Flink engine is comprised of a Job Manager to coordinate work done in the cluster and a Task Manager to execute the transformations directly on the data.

**Source**: [Flink Fundamentals - Palantir](https://www.palantir.com/docs/foundry/data-integration/flink-streaming)

#### Supported Streaming Sources

Palantir Foundry supports multiple streaming data sources including:
- Apache Kafka
- ActiveMQ
- Amazon Kinesis
- Amazon SNS
- Amazon SQS
- Aveva PI
- Google Pub/Sub
- IBM MQ
- RabbitMQ
- MQTT (Beta)
- Solace

**Source**: [Streaming Guide - Palantir](https://www.palantir.com/docs/foundry/data-integration/streaming-guide)

#### Apache Flink in Foundry

Apache Flink is a distributed computation engine capable of handling unbounded datasets with low latency, allowing it to handle common streaming workflows. Foundry streaming uses Flink as the underlying engine to execute user code and other in-platform streaming applications such as hydrating the Ontology in real time and streaming time series ingestion.

While some Flink operations only need to look at single events in isolation, others need to remember information across multiple events. These are stateful operations. Examples include aggregations (like counting events over a rolling five minute window or calculating running averages) and joins (where the execution engine needs to know about previously-seen events to join them with events being ingested).

**Source**: [Data Streaming: Real-time data for real-time decisions](https://blog.palantir.com/data-streaming-real-time-data-for-real-time-decisions-palantir-rfx-blog-series-8-58a68fbc5a72)

### BI Tool and External System Connectors

The Palantir platform provides a full range of analytical tools but can also seamlessly interoperate with existing investments such as BI and data science tools. Out-of-the-box connectors are available for common systems such as:
- Power BI
- Tableau
- Jupyter
- RStudio

These connectors enable a broad range of users to tap into integrated data, while taking advantage of best-in-class data management, model management, and governance.

**Source**: [Platform Overview - Interoperability](https://www.palantir.com/docs/foundry/platform-overview/interoperability)

### Software-Defined Data Integration (SDDI)

Palantir HyperAuto implements support for Software-Defined Data Integration (SDDI). This toolset allows organizations to not only connect to common ERP and CRM systems, but also to programmatically generate data pipelines that clean, normalize, and harmonize datasets into a cohesive data asset at unprecedented speed. This data asset can then feed into the Ontology to translate data into operational value.

**Source**: [Data Integration Overview - Palantir](https://www.palantir.com/docs/foundry/data-integration/overview)

### API Integration and External Functions

#### REST API Integration

Foundry can integrate with external systems that expose a REST (representational state transfer) API. The REST API source may be used for workflows requiring interactive HTTP requests to external systems directly from Foundry applications via Actions. For example, you can create a Workshop application with a button that uses a webhook to call a REST endpoint when clicked, connecting that application to existing workflows and source systems.

**Source**: [REST APIs - Palantir](https://www.palantir.com/docs/foundry/data-integration/rest-apis/index.html)

#### External Functions and Webhooks

To use a webhook in a Function, you must first configure a Data Connection source that supports the webhooks capability. Normally this will be a REST API source. Once you have a source with webhooks configured, you can import the source into your Functions repository and create Functions that call webhooks and other logic.

External functions may not currently be used to make arbitrary API calls from TypeScript code without first defining the request as a webhook in Data Connection.

**Source**: [External Functions - Palantir](https://www.palantir.com/docs/foundry/data-connection/external-functions)

---

## Deployment Patterns

### Deployment Flexibility

Palantir offers an enterprise data platform supporting multi-cloud, hybrid cloud, and on-premises data management environments. Enterprises increasingly demand solutions that span on-premises, edge and multi-cloud environments, and Palantir's architecture is primed for this hybrid reality.

**Source**: [Enterprise AI Operating System 2025](https://ai2.work/business/ai-business-palantir-os-2025/)

### Apollo - Palantir's Deployment Platform

Apollo supports all major cloud, on-premises, and disconnected (air-gapped) environments. Palantir Apollo is an extensible, scalable platform for managing and deploying software that encodes operational best practices refined during Palantir's history of running mission-critical software platforms.

Apollo centrally manages software across independent environments, regardless of their location or level of consistent connectivity. With Apollo's compliance-aware change management engine, organizations can automatically orchestrate software upgrades and changes safely across connected and disconnected, air-gapped environments. Apollo manages this with built-in controls required for strict accreditation frameworks including FedRAMP, IL5, and IL6.

**Source**: [Introduction to Apollo - Palantir](https://www.palantir.com/docs/apollo/core/introduction)

### Cloud Provider Support

Connectors for AWS, Azure, GCP and on-premises environments allow enterprises to keep sensitive workloads in private clouds while leveraging public cloud scale. Palantir platforms are designed to be cloud-agnostic. They operate on commercial cloud providers like AWS and Azure, as well as highly secure government and air-gapped environments.

**Source**: [Breaking Down Palantir Tech Stack in 2025](https://slashdev.io/-breaking-down-notions-palantir-stack-in-2025)

#### Key Cloud Partnerships

- **AWS Partnership** (March 5, 2021): Palantir announced its partnership with Amazon AWS. Palantir's ERP Suite was optimized to run on Amazon Web Services.

- **Microsoft Azure Partnership** (August 8, 2024): Palantir and Microsoft announced a partnership whereby Palantir will deploy its suite of products on Microsoft Azure Government clouds.

- **Oracle Cloud Partnership**: Palantir Foundry and AIP is a software-as-a-service (SaaS) offering that runs on OCI. Customer data is ingested into Foundry from a variety of data sources using Palantir's standard data integration patterns, whether those be public data sources (public APIs, 3rd party SaaS), private sources running in OCI such as MySQL HeatWave or Oracle Autonomous Database, or private sources running in on-premises networks or in other clouds through Palantir's on-premises agent.

**Sources**:
- [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)
- [Run Palantir Foundry and AIP on OCI](https://docs.oracle.com/en/solutions/palantir-foundry-ai-platform-on-oci/index.html)

### Technical Infrastructure

Kubernetes is at the heart of Palantir's deployment model, orchestrating containerized workloads across cloud, hybrid, and on-prem environments. Docker packages every component, from microservices to data pipelines, ensuring portability and consistency. Palantir's proprietary DevOps platform, Apollo, enables continuous delivery of software across secure and air-gapped environments, allowing for precise version control, rollback, and remote updates—even in offline or battlefield settings.

**Source**: [Breaking Down Palantir Tech Stack in 2025](https://slashdev.io/-breaking-down-notions-palantir-stack-in-2025)

### High Availability and Zero-Downtime Upgrades

Each of the hundreds of services within the platform run in a highly-available, redundant configuration. Beyond core backend services, this also includes front-end application services, analytics tools, application builders, and each constituent service used by each type of user. All service upgrades are performed in a zero-downtime capacity, with granular monitoring that informs how upgrade strategies are deployed, monitored, and potentially rolled back.

**Source**: [Platform Overview - Architecture](https://www.palantir.com/docs/foundry/platform-overview/architecture)

---

## AI/ML Architecture (AIP)

### Overview

Palantir's Artificial Intelligence Platform (AIP) connects AI with your data and operations. AIP is designed to drive automation across operational processes, providing a comprehensive suite of tools that can be used by everyone in an organization, from developers to frontline users.

Together with Foundry (Palantir's data operations platform) and Apollo (Palantir's mission control for autonomous software deployment), AIP forms an operating system that can deliver a full range of AI-driven products, from LLM-powered web applications to mobile applications using vision-language models.

**Source**: [AIP Overview - Palantir](https://www.palantir.com/docs/foundry/aip/overview)

### Core Architecture

Palantir AIP is designed to scale across all types of end users, the world's most demanding data-driven workloads, and myriad infrastructure substrates. The underlying service mesh operates atop a set of software-defined principles that are enforced by Palantir Apollo.

**Source**: [Platform Overview - Architecture](https://www.palantir.com/docs/foundry/platform-overview/architecture)

### Ontology as AI Foundation

Palantir AIP's Ontology binds data, logic, and actions together into a high-fidelity representation of enterprise operations that is intelligible across humans and AI. Ontology building within Palantir's AIP is crucial for creating an intelligent system that supports human and AI decision-making. It connects Data, Logic, and Action into a business-specific representation, allowing both humans and AI to interact with business operations without needing deep knowledge of data technologies or programming languages.

**Source**: [Palantir Foundry AIP - Unit8](https://unit8.com/resources/palantir-foundry-aip/)

### LLM Integration

#### Supported Models

Palantir AIP supports a wide range of LLMs (large language models) and text embedding models from leading providers, including:
- xAI
- OpenAI (GPT-5, GPT-5 mini, GPT-5 nano)
- Anthropic (Claude Opus 4.1)
- Meta (Llama)
- Google (Gemini)
- Mixtral

AIP is model-agnostic and supports a diverse selection of models for LLM-powered use cases. The model catalog is an AIP application that allows you to access and use most of the popular LLMs.

**Sources**:
- [Supported LLMs - Palantir](https://www.palantir.com/docs/foundry/aip/supported-llms)
- [August 2025 Announcements - Palantir](https://www.palantir.com/docs/foundry/announcements)

#### Latest Model Support (2025)

GPT-5, GPT-5 mini, GPT-5 nano from OpenAI are now available for general use in AIP for enrollments with Azure and/or Direct OpenAI enabled in the US, EU, or non geo-restricted regions. Claude Opus 4.1 is Anthropic's leading hybrid reasoning model, designed for demanding coding, agentic search, and AI agent tasks.

**Source**: [August 2025 Announcements - Palantir](https://www.palantir.com/docs/foundry/announcements)

#### Bring Your Own Model

Bring your own model is a capability that provides first-class support for customers that would like to connect their own LLMs or accounts to use in AIP with all Palantir developer products - AIP Logic, Pipeline Builder, Agent Studio, Workshop, etc.

**Source**: [Palantir Foundry AIP - Unit8](https://unit8.com/resources/palantir-foundry-aip/)

### AI Agent Orchestration

#### Agent Studio

AIP's builder tools like AIP Logic, AIP Agent Studio, and AIP Evals enable the development of production-ready AI-powered workflows, agents, and functions on top of the Ontology and developer toolchain. Additionally, AIP transforms the application environment by allowing sandboxed, autoscaling applications to integrate generative AI seamlessly within existing security, audit, and resource management frameworks.

**Source**: [AIP Overview - Palantir](https://www.palantir.com/docs/foundry/aip/overview)

#### Native Tool Calling

Native tool calling mode is now available in AIP Agent Studio, allowing agents to leverage built-in tool calling capabilities of supported models for improved speed and performance. Agents in native tool calling mode can access tool calls from earlier exchanges in a conversation, enabling them to reuse previous results for more efficient responses.

**Source**: [August 2025 Announcements - Palantir](https://www.palantir.com/docs/foundry/announcements)

#### AIP Logic

AIP Logic is a no-code development environment for building, testing, and releasing functions powered by LLMs. AIP logic reduces the complexity coming from API calls and the development environment and makes it easy for your LLM to interact with your ontology.

**Source**: [Palantir Foundry AIP - Unit8](https://unit8.com/resources/palantir-foundry-aip/)

### LLM Capacity Management

LLM capacity is measured per model using TPM (tokens per minute) and RPM (requests per minute), and includes all models of all providers enabled on your enrollment, including GPT, Claude, Gemini, Llama, Mixtral, and more.

The model override feature enables more granular capacity management so you can create model "allowlists". For example, you can restrict projects to only use Claude 4 Sonnet and GPT-4.1 by setting the base Max limit per project to 0% and using model overrides.

**Sources**:
- [LLM Capacity Management - Palantir](https://www.palantir.com/docs/foundry/aip/llm-capacity-management)
- [Resource Management - Palantir](https://www.palantir.com/docs/foundry/resource-management/llm-capacity-management)

### Security and Governance

Security and Lineage are core to every operation in AIP, and are consistently enforced at every tier of the platform's architecture. This ensures that no single service (or end user) is responsible for enforcing the enterprise's existing security policies, or implementing the "bookkeeping" required to maintain provenance.

AIP incorporates all of Palantir's advanced security measures for the protection of sensitive data in compliance with industry regulations. AIP provides robust access controls, encryption, and auditing capabilities to maintain data integrity and transparency. Moreover, built-in governance tools help organizations maintain accountability and historical lineage in AI operations.

**Source**: [Palantir Foundry AIP - Unit8](https://unit8.com/resources/palantir-foundry-aip/)

### NVIDIA Partnership (2025)

Palantir is integrating NVIDIA Blackwell architecture into Palantir AIP. This will accelerate the end-to-end AI pipeline, from data processing and analytics to model development and fine-tuning to production AI, using long-thinking, reasoning agents.

Palantir AI Platform (AIP) will integrate NVIDIA GPU-accelerated data processing and route optimization libraries, open models and accelerated computing. This combination of Ontology and NVIDIA AI will support customers by providing the advanced, context-aware reasoning necessary for operational AI. Enterprises using the customizable technology stack will be able to tap into their data to power domain-specific automations and AI agents.

**Source**: [Palantir and NVIDIA Team Up](https://nvidianews.nvidia.com/news/nvidia-palantir-ai-enterprise-data-intelligence)

---

## Developer Experience

### Building Applications

#### Workshop (Low-Code/No-Code)

Workshop is a flexible, object-oriented application building tool that leverages the semantic primitives (e.g., objects, links) and the kinetic primitives (e.g., Actions, Functions) within the Ontology to enable the rapid delivery of highly interactive desktop and mobile applications.

The application building experience in Workshop empowers users to create powerful applications out of no-code, low-code, and code-based widgets. No technical expertise is required to start building with widgets and weaving objects, links, and actions into user-driven workflows that go far beyond dashboards or passive visualizations.

**Source**: [Workshop Overview - Palantir](https://www.palantir.com/docs/foundry/workshop/overview)

Workshop reduces the barrier to entry for application builders by using the Object layer as the primary building block. All data in a Workshop Application is read from the Object Data Layer, allowing application creators to take advantage of rich characteristics such as links between object types.

Workshop does not compete with BI tools or low-code platforms because it starts with a different assumption: your operational system already exists. Workshop reads directly from your Ontology, Palantir's semantic layer that unifies your data landscape.

**Source**: [Palantir Workshop: The Control Tower That Closes the Last-Mile Gap](https://blog.dataengineerthings.org/palantir-workshop-the-control-tower-that-closes-the-last-mile-gap-8b0d7ec83def)

#### Example Application Templates

You can create ready-to-use applications using your own data directly from the Workshop home page. Common application types include:
- **Guided Creation Form**: Build a seamless creation form to walk your users through a defined workflow
- **Metrics Dashboard**: Create dynamic executive overview and drill-down metric dashboards to monitor performance
- **Common Operating Picture**: Visualize geographical metrics contextualized on a map

**Source**: [Workshop Example Applications - Palantir](https://www.palantir.com/docs/foundry/workshop/example-applications)

#### 2025 Workshop Updates

- **Data Freshness Widget**: Workshop users can now easily track the freshness of data directly within their application
- **Branch Protection**: You can now protect the main branch of your Workshop modules and define custom approval policies
- **Custom Widgets**: Custom widgets allow technical users to write custom frontend code to be securely rendered into Workshop
- **Palantir Model Context Protocol (MCP)**: Now available across all enrollments as of the week of July 14. Palantir MCP enables AI IDEs and AI agents to autonomously design, build, edit, and review end-to-end applications within the Palantir platform

**Sources**:
- [July 2025 Announcements - Palantir](https://www.palantir.com/docs/foundry/announcements/2025-07)
- [August 2025 Announcements - Palantir](https://www.palantir.com/docs/foundry/announcements/2025-08)

### Data Transformation

#### Pipeline Builder

Pipeline Builder is Foundry's primary application for fast, flexible, and scalable delivery of data pipelines while providing robustness and security. With Pipeline Builder, end users and data engineers can collaborate in a graph and form-based environment to integrate data, create business logic transformation, and define a rigorous release process for production pipelines.

Key features include:
- Intuitive user interface with graph and form-based interfaces that provide feedback, including join keys and column casting suggestions
- Functions are strongly typed and can flag errors immediately instead of at build time
- Independent pipeline logic that can connect to different logic execution engines, including Spark, Flink, Azure instances, and more
- Large Language Models (LLMs): Leverage the power of LLMs and AIP to transform your data
- Geospatial transformations and streaming capability for pipelines that execute with real-time latencies

**Source**: [Pipeline Builder Overview - Palantir](https://www.palantir.com/docs/foundry/pipeline-builder/overview)

With Pipeline Builder and a robust backend model, users who code and users who do not code can collaborate jointly on a pipeline workflow.

**Source**: [Pipeline Builder Transforms - Palantir](https://www.palantir.com/docs/foundry/pipeline-builder/transforms-transform-data)

#### Code Repositories

Code Repositories provides a web-based integrated development environment (IDE) for writing and collaborating on production-ready code in Foundry. The application provides a user-friendly way to interact with the underlying Git repository. The Code Repository application contains a fully integrated suite of tools that let you write, publish, and build data transformations as part of a production pipeline.

**Source**: [Building Pipelines - Considerations](https://www.palantir.com/docs/foundry/building-pipelines/considerations-pb-cr)

#### When to Use Each Tool

Safeguard pipeline health by utilizing Pipeline Builder's rails for safe and usage-efficient data transformations and pipeline management. In cases where users require specialized code-based logic not available in Pipeline Builder, Code Repositories should be used to create those stages to add to the main pipeline.

Since both Pipeline Builder and Code Repositories use Foundry datasets as inputs and outputs, a pipeline input built in Code Repositories can be added before, after, and in the middle of a pipeline in Pipeline Builder.

**Source**: [Building Pipelines - Considerations](https://www.palantir.com/docs/foundry/building-pipelines/considerations-pb-cr)

### Workflow Automation

#### Automate Platform

Automate is an application for setting up business automation. The Automate application allows users to define conditions and effects. Conditions are checked continuously, and effects are executed automatically when the specified conditions are met.

Conditions can be either:
- Static time conditions ("trigger every Monday at 9am")
- Object data conditions built on top of the Foundry ontology ("trigger when a new alert object with priority high is added")
- A combination of static and object data conditions

Configurable effects include submitting Foundry Actions as well as sending platform and email notifications with attachments to users.

**Source**: [Automate Overview - Palantir](https://www.palantir.com/docs/foundry/automate/overview)

#### Actions Effect

The Actions effect allows you to automatically run Actions when an automation triggers or recovers. Workflow automation can be used to automatically perform Actions on object data meeting specified criteria, including:
- Checking for data anomalies and automatically passing those objects into an Action with logic to remediate the issue
- Watching for suggestions or potential Actions and automatically applying them when preconfigured event and time conditions are met

Such Actions could include making an API call to an external system via Webhooks.

**Source**: [Automate Actions Effect - Palantir](https://www.palantir.com/docs/foundry/automate/effect-actions)

#### Machinery (2025 Update)

Implementing a process in the Palantir platform involves many individual resources, such as object types, actions, and automations. Machinery now provides a comprehensive view for all these components and lets you define an ordered flow of automations and manual actions. Its unique state-centric perspective allows you to make incremental progress towards desired outcomes while handling and resolving the edge cases of your organization.

To operationalize your process in the Palantir platform, you can quickly bootstrap a Workshop module ("Machinery Express application") with a single click to initiate your application development. The express application serves as a dynamic playground where you can conduct analysis and intervene with your agentic workflows in real-time.

**Source**: [February 2025 Announcements - Palantir](https://www.palantir.com/docs/foundry/announcements/2025-02)

#### Fallback Effects for Resilience

Fallback effects allow you to execute an alternative action when another effect (such as an Actions effect or AIP Logic effect) fails, providing robust error handling for your automations. With fallback effects, you can implement contingency plans, capture error information, and ensure your workflows remain resilient even when primary actions encounter problems.

**Source**: [Automate Fallback Effect - Palantir](https://www.palantir.com/docs/foundry/automate/effect-fallback)

### APIs and SDKs

#### Foundry API

The Foundry API is a developer-friendly REST API for interacting with Palantir's Foundry platform. It can be used to build applications on top of Palantir's products. The Foundry API is a Representational State Transfer (REST) API consisting of HTTP endpoints. The endpoints use the OAuth 2.0 protocol for authentication and are designed in a common pattern, largely using JSON requests and responses.

**Source**: [API Reference Introduction - Palantir](https://www.palantir.com/docs/foundry/api/general/overview/introduction)

#### Software Development Kits

To simplify the process of making API calls, use the Foundry platform SDKs for supported languages. The platform provides SDKs including Python (`foundry_sdk`) for interacting with the Ontology, including authentication via `UserTokenAuth` and making API calls to list objects and apply actions.

**Source**: [Software Development Kit - Palantir](https://www.palantir.com/docs/foundry/api/general/overview/sdks)

### Foundry Branching (2025 Update)

With the new support for transforms code repositories, Foundry Branching adds to its additional support for Pipeline Builder, the Ontology, and Workshop. Through Foundry Branching, you can now modify your data pipeline in Code Repositories, edit Ontology definitions, and build on those changes in your Workshop modules from one branch.

Branch creation and branch selector allows you to create a branch in transform code repositories, Pipeline Builder, Ontology Manager, or Workshop, and access the branch in all supported applications.

**Source**: [April 2025 Announcements - Palantir](https://www.palantir.com/docs/foundry/announcements/2025-04)

---

## Security and Data Governance

### Core Security Model

The Palantir security model encompasses both authentication and authorization. Authentication verifies the identity of a user, while authorization grants access based on a user's attributes and permissions. Data security in the Palantir platform is guaranteed through a combination of mandatory and discretionary controls.

Discretionary permissions are granted to users on individual resources, in the form of roles with different operations (for example, view or edit). In addition, granular row or column-level controls based on a user's attributes can be put in place on resources too.

**Source**: [Security Overview - Palantir](https://www.palantir.com/docs/foundry/security/overview)

### Access Control Models

#### Role-Based Access Control (RBAC)

Apollo uses role-based access controls (RBAC) to determine what operations a user is authorized to perform. RBAC is a flexible authorization model where Teams can gain permissions to a set of operations based on their assigned roles. These roles can be granted for all resources in Apollo of a given type, like Release Channels, or for a specific resource of that type.

**Source**: [Apollo Authorization - Palantir](https://www.palantir.com/docs/apollo/core/authorization)

#### Purpose-Based Access Control (PBAC)

The solution must support purpose-based access control lists (PBAC), in addition to role-based access controls (RBAC) and classification-based controls (CBAC). With PBAC, instead of applying for blanket access to data sets and applications without the further context that allows data governance users to evaluate the legitimacy of the request, users apply for access to a purpose.

Purpose-based access controls are used in governance tools such as Palantir Foundry, but the concept applies more generally.

**Sources**:
- [Operational Security: Enabling transparency, collaboration, and privacy](https://blog.palantir.com/operational-security-enabling-transparency-collaboration-and-privacy-palantir-rfx-blog-series-28062c37bea6)
- [Purpose-based Access Controls at Palantir](https://blog.palantir.com/purpose-based-access-controls-at-palantir-f419faa400b3)

### Data Protection and Governance

Data protection and data governance are central concepts to using Foundry. Data protection refers to the range of technical and organizational means available to ensure that the processing of personal data is at all times limited to that which is necessary and proportional to achieve a legitimate processing outcome. Data governance refers to the management of enterprise data across the entire lifecycle of processing, from ingestion to access to deletion.

**Source**: [Data Protection and Governance - Palantir](https://www.palantir.com/docs/foundry/security/data-protection-and-governance)

#### Checkpoints

Checkpoints is a Foundry application that facilitates accountability and purpose limits by enabling data governance teams to request justifications before certain sensitive data actions can be performed.

**Source**: [Data Protection and Governance - Palantir](https://www.palantir.com/docs/foundry/security/data-protection-and-governance)

#### Sensitive Data Scanner

When Sensitive Data Scanner detects that a dataset contains information that corresponds to a pre-specified definition of sensitive data, the application will trigger a configured response, such as alerting administrators by creating a Foundry-generated Issue or proactively locking down the dataset by applying a Security Marking.

**Source**: [Data Protection and Governance - Palantir](https://www.palantir.com/docs/foundry/security/data-protection-and-governance)

### Organizational Controls

Users belong to Organizations, and are organized in groups managed within the platform or through external identity providers. Organizations are one form of mandatory controls applied to Projects that enforce strict silos between groups of users and resources. Therefore, users of one Organization cannot access the resources of another Organization unless sharing protocols have explicitly been configured.

For highly sensitive data, markings are another form of mandatory controls that can be applied to data or resources that require special protection (for example, PII or financially sensitive data). Users must have special permission to discover or access such data, in addition to Organization membership.

**Source**: [Data Protection and Governance - Palantir](https://www.palantir.com/docs/foundry/security/data-protection-and-governance)

### Compliance Framework Alignment

The Palantir platform is used by healthcare providers, financial institutions, utility providers, manufacturers, telecoms, airlines, and pharmaceutical companies around the globe to handle their most sensitive workflows. The Palantir platform was built for security-conscious customers who need the capability to handle financial data, Personally Identifiable Information (PII), Protected Health Information (PHI), Controlled Unclassified Information (CUI), and even classified government data in a secure and compliant manner.

Palantir's security infrastructure meets regulatory requirements across industries and continents by aligning with frameworks like:
- HIPAA (Healthcare)
- GDPR (European Data Protection)
- ITAR (International Traffic in Arms Regulations)
- FedRAMP, IL5, IL6 (Government security levels)

**Sources**:
- [Data Protection and Governance - Palantir](https://www.palantir.com/docs/foundry/security/data-protection-and-governance)
- [Introduction to Apollo - Palantir](https://www.palantir.com/docs/apollo/core/introduction)

---

## Platform Architecture

### Compute Runtimes

Common runtimes for data integration include Apache Spark and Apache Flink, but external transformation engines can be used if desired. Palantir-authored engines power the Ontology and other capability sets that do not cleanly map to existing compute modalities.

**Source**: [Platform Overview - Architecture](https://www.palantir.com/docs/foundry/platform-overview/architecture)

### Storage Technologies

The platform makes use of several storage technologies at different tiers of the architecture. This includes:
- Blob storage (or HDFS)
- Horizontally scalable key/value stores
- Horizontally scalable relational databases
- Multi-modal time series subsystems

**Source**: [Platform Overview - Architecture](https://www.palantir.com/docs/foundry/platform-overview/architecture)

### Microservices Architecture

The Foundry platform uses a microservices architecture in which multiple services together comprise the Ontology backend and other platform capabilities. This architecture allows for horizontal scaling and separation of concerns.

**Source**: [Ontology Architecture - Palantir](https://www.palantir.com/docs/foundry/object-backend/overview)

---

## Sources

### Official Palantir Documentation

1. [Palantir Ontology Overview](https://www.palantir.com/docs/foundry/ontology/overview)
2. [Core Concepts - Palantir](https://www.palantir.com/docs/foundry/ontology/core-concepts)
3. [Ontology Architecture](https://www.palantir.com/docs/foundry/object-backend/overview)
4. [Object and Link Types - Type Reference](https://www.palantir.com/docs/foundry/object-link-types/type-reference)
5. [Properties Overview](https://www.palantir.com/docs/foundry/object-link-types/properties-overview)
6. [Shared Properties Overview](https://www.palantir.com/docs/foundry/object-link-types/shared-property-overview/index.html)
7. [Link Types - Create a Link Type](https://www.palantir.com/docs/foundry/object-link-types/create-link-type)
8. [Data Connection Architecture](https://www.palantir.com/docs/foundry/data-connection/architecture)
9. [Data Integration Overview](https://www.palantir.com/docs/foundry/data-integration/overview)
10. [Data Connection Overview](https://www.palantir.com/docs/foundry/data-connection/overview)
11. [Data Connection Core Concepts](https://www.palantir.com/docs/foundry/data-connection/core-concepts)
12. [Streaming Guide](https://www.palantir.com/docs/foundry/data-integration/streaming-guide)
13. [Flink Fundamentals](https://www.palantir.com/docs/foundry/data-integration/flink-streaming)
14. [REST APIs](https://www.palantir.com/docs/foundry/data-integration/rest-apis/index.html)
15. [External Functions](https://www.palantir.com/docs/foundry/data-connection/external-functions)
16. [Platform Overview - Interoperability](https://www.palantir.com/docs/foundry/platform-overview/interoperability)
17. [Platform Overview - Architecture](https://www.palantir.com/docs/foundry/platform-overview/architecture)
18. [Introduction to Apollo](https://www.palantir.com/docs/apollo/core/introduction)
19. [AIP Overview](https://www.palantir.com/docs/foundry/aip/overview)
20. [Supported LLMs](https://www.palantir.com/docs/foundry/aip/supported-llms)
21. [LLM Capacity Management](https://www.palantir.com/docs/foundry/aip/llm-capacity-management)
22. [Resource Management - LLM Capacity](https://www.palantir.com/docs/foundry/resource-management/llm-capacity-management)
23. [Workshop Overview](https://www.palantir.com/docs/foundry/workshop/overview)
24. [Workshop Example Applications](https://www.palantir.com/docs/foundry/workshop/example-applications)
25. [Pipeline Builder Overview](https://www.palantir.com/docs/foundry/pipeline-builder/overview)
26. [Pipeline Builder Transforms](https://www.palantir.com/docs/foundry/pipeline-builder/transforms-transform-data)
27. [Building Pipelines - Considerations](https://www.palantir.com/docs/foundry/building-pipelines/considerations-pb-cr)
28. [Automate Overview](https://www.palantir.com/docs/foundry/automate/overview)
29. [Automate Actions Effect](https://www.palantir.com/docs/foundry/automate/effect-actions)
30. [Automate Fallback Effect](https://www.palantir.com/docs/foundry/automate/effect-fallback)
31. [API Reference Introduction](https://www.palantir.com/docs/foundry/api/general/overview/introduction)
32. [Software Development Kit](https://www.palantir.com/docs/foundry/api/general/overview/sdks)
33. [Security Overview](https://www.palantir.com/docs/foundry/security/overview)
34. [Data Protection and Governance](https://www.palantir.com/docs/foundry/security/data-protection-and-governance)
35. [Apollo Authorization](https://www.palantir.com/docs/apollo/core/authorization)
36. [February 2025 Announcements](https://www.palantir.com/docs/foundry/announcements/2025-02)
37. [April 2025 Announcements](https://www.palantir.com/docs/foundry/announcements/2025-04)
38. [July 2025 Announcements](https://www.palantir.com/docs/foundry/announcements/2025-07)
39. [August 2025 Announcements](https://www.palantir.com/docs/foundry/announcements/2025-08)

### Blog Posts and Articles

40. [Ontology-Oriented Software Development](https://blog.palantir.com/ontology-oriented-software-development-68d7353fdb12)
41. [Understanding Palantir's Ontology: Semantic, Kinetic, and Dynamic Layers](https://pythonebasta.medium.com/understanding-palantirs-ontology-semantic-kinetic-and-dynamic-layers-explained-c1c25b39ea3c)
42. [Palantir's Ontology, Kimball's Star Schema, and Model-Driven Data Engineering](https://medium.com/business-friendly-data-modeling/palantirs-ontology-kimball-s-star-schema-and-model-driven-data-engineering-a-comparative-view-8b175464c42a)
43. [Closed or Open Architectured Ontologies: The Enterprise Race to Make Data AI-Ready](https://medium.com/timbr-ai/palantir-timbr-the-enterprise-race-to-make-data-ai-ready-4b26a1efe89c)
44. [Data Streaming: Real-time data for real-time decisions](https://blog.palantir.com/data-streaming-real-time-data-for-real-time-decisions-palantir-rfx-blog-series-8-58a68fbc5a72)
45. [Operational Security: Enabling transparency, collaboration, and privacy](https://blog.palantir.com/operational-security-enabling-transparency-collaboration-and-privacy-palantir-rfx-blog-series-28062c37bea6)
46. [Purpose-based Access Controls at Palantir](https://blog.palantir.com/purpose-based-access-controls-at-palantir-f419faa400b3)
47. [Palantir Workshop: The Control Tower That Closes the Last-Mile Gap](https://blog.dataengineerthings.org/palantir-workshop-the-control-tower-that-closes-the-last-mile-gap-8b0d7ec83def)

### Partner and Third-Party Sources

48. [Palantir Foundry AIP - Unit8](https://unit8.com/resources/palantir-foundry-aip/)
49. [Palantir and NVIDIA Team Up to Operationalize AI](https://nvidianews.nvidia.com/news/nvidia-palantir-ai-enterprise-data-intelligence)
50. [Run Palantir Foundry and AIP on OCI](https://docs.oracle.com/en/solutions/palantir-foundry-ai-platform-on-oci/index.html)
51. [Enterprise AI Operating System 2025: Palantir's Pivot](https://ai2.work/business/ai-business-palantir-os-2025/)
52. [Breaking Down Palantir Tech Stack in 2025](https://slashdev.io/-breaking-down-notions-palantir-stack-in-2025)
53. [Palantir Technologies - Wikipedia](https://en.wikipedia.org/wiki/Palantir_Technologies)

---

**End of Research Document**

*This research provides factual information about Palantir's technical architecture based on official documentation, blog posts, and third-party technical analysis available as of December 2025. All claims are sourced and linked to their original references.*
