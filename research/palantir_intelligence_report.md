# Palantir Data Platform Intelligence Report

**Date:** December 11, 2025
**Scope:** Platform capabilities, technical architecture, competitive differentiation

---

## Executive Summary

Palantir Technologies operates an **enterprise AI operating system** built around a proprietary **Ontology**—a semantic layer that creates a digital twin of an organization's operations. Unlike traditional data platforms focused on storage (Snowflake), processing (Databricks), or visualization (Tableau/Power BI), Palantir's core value proposition is **operational intelligence**: connecting data analysis directly to action.

**Key 2025 Performance:**
- Q3 2025 revenue: $1.181B (63% YoY growth)
- U.S. commercial revenue: +121% YoY
- Stock price: +170% in 2025 (market cap >$490B)
- Rule of 40 score: 114 (highest ever)
- $10B U.S. Army contract consolidating 75 separate agreements

**Core Products:**
| Product | Purpose | Launch |
|---------|---------|--------|
| **Foundry** | Enterprise data operations platform | 2016 |
| **Gotham** | Defense/intelligence operating system | 2008 |
| **AIP** | AI platform for LLM orchestration | April 2023 |
| **Apollo** | Continuous delivery infrastructure | 2019 |

---

## What Palantir Does

### Product Portfolio

#### 1. Foundry
**"The Operating System for the Modern Enterprise"**

Foundry is Palantir's commercial platform that transforms siloed enterprise data into operational applications. It's not a data warehouse—it sits on top of data infrastructure (Snowflake, Databricks, cloud storage) and operationalizes data through the Ontology.

**Core Capabilities:**
- Data integration from 200+ sources (databases, APIs, streaming)
- Pipeline Builder for visual data transformation
- Workshop for no-code/low-code application building
- Automate for business process automation
- Code Repositories for custom development

**2025 Updates:**
- Bring-your-own-model (BYOM) for custom LLM integration
- TypeScript v2 functions (GA July 2025)
- Consumer Mode for external-facing applications
- Foundry Branching for unified version control

#### 2. Gotham
**"The Operating System for Defense Decision Making"**

Gotham serves defense and intelligence agencies with AI-powered situational awareness and decision support.

**Key Capabilities:**
- AI-powered targeting and kill chain support
- Satellite tasking and sensor integration
- Mixed reality for virtual operations centers
- Edge deployment for disconnected environments
- FedRAMP, IL-5 DoD SRG, ISO 27001 certifications

#### 3. AIP (Artificial Intelligence Platform)
**"Connecting AI with Your Data and Operations"**

Launched April 2023, AIP orchestrates LLMs within the Ontology framework, enabling enterprise AI that understands business context.

**Supported Models (2025):**
- OpenAI: GPT-5, GPT-5 mini, GPT-5 nano
- Anthropic: Claude Opus 4.1, Claude Haiku 4.5
- Google: Gemini 2.5 Pro, Gemini 2.5 Flash
- Meta: Llama
- Open models: Mixtral

**Key Features:**
- **Agent Studio:** Build AI agents with native tool calling
- **AIP Logic:** No-code LLM function development
- **AIP Evals:** Automated testing and evaluation
- **BYOM:** Connect custom LLMs

#### 4. Apollo
**"Mission Control for Software Deployment"**

Apollo manages continuous delivery across all environments—cloud, on-premises, classified networks, and edge devices.

- 41,000 deployments per week
- Blue-green upgrades with automatic rollback
- Air-gapped environment support
- FedRAMP, IL5, IL6 compliance

---

## How It Works: Technical Architecture

### The Ontology (Core Differentiator)

The Ontology is Palantir's foundational technology—a **semantic layer** that transforms raw data into a **digital twin** of an organization's operations.

**Three Layers:**
1. **Semantic Layer:** Defines entities (Object Types), characteristics (Properties), and relationships (Link Types)
2. **Kinetic Layer:** Enables actions, functions, and workflows
3. **Dynamic Layer:** Governs business rules, permissions, and policies

**Core Components:**
| Component | Description | Example |
|-----------|-------------|---------|
| **Object Type** | Entity or event | "Customer Order" |
| **Property** | Characteristics | "order_date", "status" |
| **Link Type** | Relationships | Order → Customer |
| **Action Type** | Modifications | "Approve Order" |
| **Interface** | Polymorphism | Shared shape across types |

**Why It Matters:**
- Users interact with business concepts ("Aircraft", "Orders", "Patients") not tables/columns
- AI agents understand enterprise context through the Ontology
- Applications built on shared data model, not siloed schemas
- Changes propagate across all connected applications

**Example:**
> In a global manufacturer's ontology, "supplier" represents a business partner with direct connections to shipments. If a shipment is delayed, all affected products, warehouses, and suppliers are automatically updated.

### Data Integration

**Architecture:**
- **Agent Proxy (Recommended):** Websocket connection from on-premises agent to Foundry workers
- **Streaming:** Apache Flink engine with Kafka, Kinesis, Pub/Sub support
- **Connectors:** 200+ sources including SAP, databases, cloud storage, APIs

**Data Flow:**
```
Raw Data Sources → Data Connection → Pipeline Builder → Ontology → Applications
                   (200+ connectors)   (Spark/Flink)   (Semantic)  (Workshop/APIs)
```

### Deployment Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Cloud** | AWS, Azure, GCP, Oracle Cloud | Standard enterprise |
| **On-Premises** | Customer data center | Data sovereignty |
| **Hybrid** | Cloud control plane + on-prem data | Regulated industries |
| **Air-Gapped** | Fully disconnected | Defense, classified |
| **Edge** | Edge devices, disconnected ops | Field operations |

**Technical Stack:**
- **Orchestration:** Kubernetes
- **Containers:** Docker
- **Compute:** Apache Spark, Apache Flink
- **Storage:** Blob storage, key/value stores, relational databases

### AI/ML Architecture

**Model-Agnostic Design:**
AIP is not tied to any single LLM provider. It supports:
- External models via API (OpenAI, Anthropic, Google)
- Self-hosted models (Llama, Mixtral)
- Customer BYOM integration

**Agent Orchestration:**
- **Native Tool Calling:** LLM directly calls tools (faster than prompted mode)
- **Action Tools:** Execute ontology edits
- **Object Query Tools:** Access configured object types
- **Function Tools:** Call any Foundry function
- **Command Tools:** Trigger operations in other applications

**Capacity Management:**
- TPM (tokens per minute) and RPM (requests per minute) limits
- Model allowlists per project
- Usage monitoring and alerting

### Developer Experience

**Building Applications:**

| Tool | Approach | Best For |
|------|----------|----------|
| **Workshop** | No-code/low-code | Business users, rapid prototyping |
| **Pipeline Builder** | Visual graph-based | Data transformation |
| **Code Repositories** | Full code IDE | Custom logic, complex pipelines |
| **Automate** | Event-driven | Business process automation |

**APIs and SDKs:**
- RESTful Foundry API with OAuth 2.0
- Ontology SDK (OSDK) for code in "business language"
- Python SDK (`foundry_sdk`)
- BI connectors (Power BI, Tableau, Jupyter, RStudio)

---

## Competitive Differentiation

### Key Differentiators

| Differentiator | Description | Competitors Lack |
|----------------|-------------|------------------|
| **The Ontology** | Semantic layer creating digital twin | Databricks, Snowflake operate on raw data |
| **Closed-Loop Operations** | Analytics → Action → Feedback | BI tools stop at dashboards |
| **Military-Grade Security** | FedRAMP High, IL5, air-gapped | Cloud-only platforms can't do air-gapped |
| **Deployment Flexibility** | Any cloud, on-prem, edge, air-gapped | Snowflake is cloud-only |
| **AI Operating System** | LLMs grounded in business context | Generic AI tools lack enterprise context |

### Competitive Matrix

| Capability | Palantir | Databricks | Snowflake | AWS/Azure/GCP | Tableau/Power BI |
|------------|----------|------------|-----------|---------------|------------------|
| **Primary Function** | Operational intelligence | Data processing/ML | Data warehousing | Cloud infrastructure | Visualization |
| **Semantic Layer** | Ontology | Limited | No | Varies | No |
| **Operational Workflows** | Yes | Limited | No | Varies | No |
| **Air-Gapped Deploy** | Yes | No | No | Limited | No |
| **LLM Integration** | Native (AIP) | Mosaic AI | Cortex AI | Native services | Copilot/Pulse |
| **Target User** | All levels | Data engineers | Analysts | Developers | Business users |
| **Open Architecture** | Proprietary | Open-source core | Proprietary | Varies | Proprietary |

### When to Choose Each

**Choose Palantir:**
- Operational intelligence (action, not just insight)
- Mission-critical applications (defense, healthcare, finance)
- Complex data integration across 100s of sources
- Military-grade security and compliance
- Air-gapped or hybrid deployment required
- Building digital twin of organization

**Choose Databricks:**
- Data engineering and ML at scale
- Open-source preference (Spark, Delta Lake)
- Data science teams comfortable with code
- Strong MLOps requirements

**Choose Snowflake:**
- Centralized data warehousing
- Standard analytics and BI workloads
- Accessible, conventional cloud platform
- Cost-sensitive (lower than Palantir)

**Choose Cloud-Native (AWS/Azure/GCP):**
- Already invested in specific ecosystem
- Want tightly integrated services
- Standard analytics requirements
- Minimize vendor count

**Choose Tableau/Power BI:**
- Primary need is dashboards and reports
- Business analysts and executives
- Budget-conscious
- Don't need operational workflows

### 2025 Strategic Partnerships

**Databricks (March 2025):**
- Unity Catalog + Palantir Virtual Tables
- Zero-copy access to Lakehouse data
- Combined governance and security
- NOT competitors—complementary

**NVIDIA (2025):**
- Blackwell GPU integration for AIP
- Accelerated data processing and model inference
- Joint operational AI stack

**Major Cloud Partnerships:**
- AWS (2021): ERP Suite optimized for AWS
- Microsoft Azure (2024): Deployment on Azure Government
- Oracle Cloud: SaaS offering on OCI
- Google Cloud: FedStart program integration

---

## Weaknesses & Considerations

### Legitimate Criticisms

| Concern | Details |
|---------|---------|
| **High Cost** | ~$32-141k per core; millions in annual TCO |
| **Complexity** | Steep learning curve; extensive setup time |
| **Vendor Lock-In** | Proprietary architecture; difficult migration |
| **Limited Python Support** | Some packages unavailable; Databricks preferred for complex data science |
| **Documentation** | Sometimes inadequate; knowledge base limited |
| **NPS Score** | 30 (moderate satisfaction—22% detractors) |

### Gartner 2025 Positioning

**Magic Quadrant for AI Application Development Platforms (Nov 2025):**
- Palantir: Included but NOT in Leaders quadrant
- Leaders: AWS, Google, IBM, Microsoft

**Forrester Wave AI/ML Platforms (Q3 2024):**
- Palantir: Named **Leader**
- Highest ranking for Current Offering

---

## Decision Framework

### Choose Palantir If:

✅ Need operational intelligence connecting analytics to action
✅ Operating in highly regulated industry (defense, healthcare, finance)
✅ Require air-gapped or hybrid deployment
✅ Building digital twin with complex data relationships
✅ Have budget for millions in annual TCO
✅ Have dedicated team for implementation
✅ Need military-grade security and compliance
✅ Want enterprise AI platform (not just models)

### Avoid Palantir If:

❌ Primary need is dashboards and reports
❌ Budget under $1M annually
❌ Need quick time-to-value (weeks, not months)
❌ Want to avoid vendor lock-in
❌ Standard BI needs met by Tableau/Power BI
❌ Data integration is straightforward
❌ Operating in unregulated industry

### Hybrid Approach

Many organizations combine Palantir with complementary tools:

1. **Palantir + Databricks:** Databricks Lakehouse for storage/processing; Palantir Ontology for operations
2. **Palantir + Cloud Provider:** Run Palantir on AWS/Azure/GCP infrastructure
3. **Palantir + BI Tools:** Palantir for operational intelligence; Tableau/Power BI for executive dashboards

---

## Summary: What Makes Palantir Different

**Palantir is NOT:**
- A data warehouse (use Snowflake)
- A data processing platform (use Databricks)
- A BI/visualization tool (use Tableau/Power BI)
- A cloud infrastructure provider (use AWS/Azure/GCP)

**Palantir IS:**
- An **operational intelligence platform** that sits on top of data infrastructure
- A **semantic layer (Ontology)** that creates a digital twin of your organization
- An **AI operating system** that grounds LLMs in business context
- A **deployment-flexible platform** for cloud, on-prem, and air-gapped environments
- A **military-grade** solution for mission-critical, regulated industries

**The Core Insight:**
> Palantir's differentiation is not in storing or processing data—it's in **operationalizing** data. The Ontology transforms raw data into business concepts that both humans and AI can understand and act upon. This "closed-loop" capability—from data to insight to action—is what competitors cannot easily replicate.

---

## Source Files

- [Products Research](/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/research/palantir_products.md)
- [Architecture Research](/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/research/palantir_architecture.md)
- [Competitive Research](/Users/nicholaspate/Documents/01_Active/Corp_Strat/ezAI/research/palantir_competitive.md)

All research conducted December 2025 using 2025 sources only.
