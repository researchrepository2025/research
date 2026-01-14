# Oracle AI Platform Summary
## August 1, 2025 - January 13, 2026

### Executive Overview
Oracle executed a comprehensive AI platform strategy during this period, transitioning from database vendor to full-stack AI infrastructure titan through three strategic pillars: massive infrastructure investments exceeding $400 billion via the Stargate partnership with OpenAI, database-centric AI architecture with Oracle AI Database 26ai integrating agentic workflows directly into the database, and multi-cloud ubiquity embedding Oracle Database services across AWS, Azure, and Google Cloud. Financial performance reflected exceptional growth with Remaining Performance Obligations surging to $523 billion (438% year-over-year) and Cloud Infrastructure revenue growing 68% to $4.1 billion in Q2 FY26. The company announced over 100 product features, expanded GPU capacity to 96,000+ NVIDIA Blackwell units, and secured major AI customers including OpenAI ($300B partnership), Meta ($20B deal), and NVIDIA.

---

## Products

- **Oracle Stargate Project** - Joint venture with OpenAI, SoftBank, and MGX to invest up to $500 billion in AI infrastructure by 2029, with Oracle building flagship campus in Abilene, Texas featuring approximately 1 gigawatt power capacity designed to eventually house more than 450,000 NVIDIA GB200 GPUs. [1] [Unverified - source inaccessible; details confirmed via secondary sources]

- **Oracle Stargate Expansion (4.5 GW)** - Agreement with OpenAI to develop 4.5 gigawatts of additional data center capacity in the U.S., representing over $300 billion between the two companies over five years. [2] [Unverified - source inaccessible; details confirmed via secondary sources]

- **Oracle Stargate Expansion - Five New Sites** - Five additional U.S. AI data center sites announced (Shackelford County TX, Milam County TX, Doña Ana County NM, Lordstown OH, Midwest location), bringing combined capacity to nearly 7 gigawatts and over $400 billion in investment over three years. [3] [Unverified - source inaccessible; details confirmed via secondary sources]

- **Oracle AI Agent Studio for Fusion Applications** - Comprehensive platform for creating, extending, deploying, and managing AI agents and agent teams across the enterprise, available at no additional cost with agent template libraries, team orchestration, extensibility for 50+ pre-packaged agents, multiple LLM options, native Fusion integration, and validation/testing tools. [4]

- **OCI Generative AI Agents Platform** - Platform with ready-to-use SQL Tool, RAG Tool, and Custom Function Calling Tool; SQL Generation automatically generates SELECT statements with self-correction; RAG Tool includes Hybrid Search combining keyword and vector search; multi-turn chat with context retention; guardrails for content moderation, prompt injection, and PII protection; human-in-the-loop capability. [5]

- **OCI Generative AI Agents - API Endpoint Tool** - API endpoint calling tool to run different API types with suitable authentication method, enabling agents to integrate with external systems and services. [6]

- **Meta Llama 4 Models (Scout and Maverick)** - Meta's Llama 4 models on OCI Generative AI using Mixture of Experts (MoE) architecture; Scout features 17B active parameters within 109B total parameters using 16 experts; Maverick features 17B active parameters within 400B total parameters using 128 experts; optimized for multimodal understanding, multilingual tasks, coding, tool-calling, and agentic systems. [7] [Unverified - source inaccessible; parameter counts confirmed via IBM and Analytics Vidhya sources]

- **Oracle and NVIDIA Partnership Expansion** - NVIDIA AI Enterprise natively available through OCI Console with 160+ AI tools accessible using Oracle Universal Credits; NVIDIA GB200 NVL72 systems generally available on OCI Supercluster scaling to 131,072 NVIDIA Blackwell GPUs with liquid cooling; Oracle integrated with NVIDIA DGX Cloud Lepton; deployed first wave of liquid-cooled NVIDIA GB200 NVL72 racks in April 2025. [8]

- **Google Gemini Models on OCI Generative AI** - Collaboration with Google making Gemini models available on OCI Generative AI, making Oracle the only hyperscaler aside from Google Cloud Platform to offer Gemini as a managed service; General Availability for pretrained Gemini 2.5 Pro, Gemini 2.5 Flash, and Gemini 2.5 Flash-Lite models; accessed through Oracle platform with Oracle Universal Credits while running on Google servers. [9]

- **Oracle AI Database 26ai** - Long-term support release replacing Oracle Database 23ai; integrated AI capabilities throughout core architecture with AI Vector Search at no additional charge; includes Oracle Autonomous AI Lakehouse supporting Apache Iceberg format, Unified Hybrid Vector Search, MCP Server Support for AI agents, built-in data privacy protection with row/column/cell-level controls, quantum-resistant encryption (ML-KEM), in-database AI agent builder with no-code visual platform; no database upgrade or application re-certification required for 23ai users. [10]

- **Oracle Autonomous AI Lakehouse** - Combines Oracle Autonomous AI Database with Apache Iceberg standard for AI and analytics solutions; available on OCI, AWS, Azure, and Google Cloud; interoperable with Databricks and Snowflake; includes Autonomous AI Database Catalog (catalog of catalogs) unifying enterprise data and metadata from other catalogs; Data Lake Accelerator speeds large-scale queries across Iceberg tables by dynamically scaling network and compute capacity. [11]

- **Oracle AI Data Platform** - General availability combining automated data ingestion, semantic enrichment, and vector indexing with built-in generative AI tools; enables organizations to transform raw data into actionable insights, accelerate collaboration across data engineers/scientists/developers, deploy AI agents orchestrating workflows; leading system integrators committed over $1.5 billion collectively including training 8,000+ practitioners and development of 100+ industry-specific use cases. [12]

- **OCI Zettascale10 Supercomputer** - Largest AI supercomputer in the cloud connecting hundreds of thousands of NVIDIA GPUs across multiple data centers delivering up to 16 zettaFLOPS peak performance; orders open with availability targeted for second half of 2026 supporting deployments up to 800,000 NVIDIA GPUs; OCI Superclusters scale beyond 100,000 NVIDIA Blackwell GPUs. [13]

- **Oracle Autonomous AI Database MCP Server** - Multi-tenant, built-in feature exposing Model Context Protocol (MCP) endpoints for AI agents and clients; Select AI Agent provides in-database framework to build, deploy and manage AI agents within Oracle Autonomous AI Database supporting custom and pre-built PL/SQL tools, external tools via REST, and MCP servers; fully managed with no MCP setup required; enterprise-grade auditing and performance controls with native Oracle Database Identity integration. [14]

- **OCI GPU Scanner** - Generally available dedicated solution providing observability, health checks, and performance monitoring for GPU workloads; vendor-neutral approach supporting current and future GPU models without firewall exceptions; integrates with cloud-native open-source tools for customizable dashboards and automated workflows; tracks temperature, processing power, model flops utilization (MFU); comprehensive active performance and passive health checks for both NVIDIA and AMD GPUs on OCI. [15] [Unverified - source inaccessible]

- **Agent Hub (OCI Generative AI)** - Streamlined platform to build, deploy, and manage advanced AI-powered agents that automate business processes, improve decision-making, and accelerate innovation; abstracts complexity of navigating many agents, interprets requests, invokes the right agents, presents recommendations, enables immediate action; catalog supports wide range of AI agents and tools with open standards including Agent2Agent (A2A) and Model Context Protocol (MCP); beta access begins November. [16] [Unverified - source inaccessible; beta access confirmed but year unclear from secondary sources]

- **Oracle Fusion Applications AI Agent Marketplace** - Marketplace enabling customers to discover and deploy pre-built AI agents directly within Oracle Fusion Cloud Applications; launched with over 100 agents from two dozen partners including Alithya, Apex IT, Apps Associates, Argano, Automus, CLOUDSUFI, GoSaaS, Grant Thornton, Huron, IBM Consulting, Infosys, KNEX, Mastek, Trinamix, Wipro, Accenture, Deloitte, KPMG, and PwC; features one-click, no-code deployment, customizable agent templates, validated security standards, unified Oracle support, built-in industry expertise from 15+ system integrators; ecosystem includes 32,000+ certified experts trained in Oracle AI Agent Studio. [17]

- **Oracle Fusion Applications - New AI Agents** - Finance agents including Payables Agent (automates multi-channel invoice processing from email, portals, EDI/e-invoicing, PDFs), Ledger Agent (continuous insight and action via natural-language monitoring prompts), Planning Agent (real-time trend and variance analysis for FP&A teams), Payments Agent (optimizes cash outflows and expands payment choices); HR Manager Concierge Agent (supports inquiries around compensation, leave, talent management, employment details); Supply Chain Quote to Purchase Requisition Agent (automates supplier quote intake to requisition process) and Fulfillment Processing Assistant Agent (streamlines urgent shipping requests and pick, pack, ship process). [18]

- **OpenAI gpt-oss Models on OCI Generative AI** - Leading open source GPT-style large language models fully managed by Oracle, generally available December 2025 as hosted options within OCI Generative AI. [19] [Unverified - source inaccessible]

- **OCI Generative AI Model Import Feature** - Accelerates AI adoption by letting organizations deploy top open source and third-party language models within OCI's secure, scalable environment; provides option to bring your own LLMs. [20] [Unverified - source inaccessible]

- **Cohere Command A and Rerank on OCI Generative AI** - Cohere's Command A 03-2025 delivers 150% throughput of predecessor while requiring only two GPUs; most performant Cohere chat model for agentic enterprise tasks with significantly improved compute efficiency and 256,000 token context length; Rerank 3.5 designed to enhance accuracy of enterprise search and RAG systems; available in on-demand and dedicated AI cluster modes. [21] [Unverified - source inaccessible]

- **xAI Grok Models on OCI Generative AI** - xAI's Grok models on OCI Generative AI services; supports pretrained Grok 4 model (flagship model with unparalleled performance in natural language, math, reasoning, released July 23, 2025). [22] [Unverified - claims about xAI using OCI for training/inference, Grok Code Fast 1, and Grok 3 with 131,072 token context not found in source]

- **OCI Data Science Updates** - JupyterLab 4.4.6 support; distributed jobs for improved scalability and cost efficiency; burstable VMs support with jobs, notebooks, pipelines; AI Quick Actions multimodel serving and model groups; AI Quick Actions in Government regions; LangChain application deployment as OCI Model Deployment; AI Forecast Operator for time-series forecasting; tight integration with OCI Data Science for training ML models on lakehouse data without data movement. [23]

- **Oracle Database 23ai Release Updates** - Quarterly updates throughout 2025 including Release Update 23.7 (January 2025), Release Update 23.8 (April 2025), Release Update 23.9 (July 2025), each featuring updates to Oracle AI Vector Search capabilities. [10]

- **Oracle Acceleron Network Interconnect** - High-speed Ethernet-based network interconnect designed to support massive GPU clusters with minimal latency. [24]

- **NVIDIA cuVS Integration** - NVIDIA cuVS library integration enabling accelerated AI vector search in Oracle Database 23ai/26ai, leveraging GPU acceleration for similarity search workloads. [25]

- **NVIDIA NIM Microservices on OCI** - NVIDIA NIM microservices accessible in OCI Data Science for real-time inference, enabling developers to deploy pre-optimized AI models with production-grade performance. [25]

- **OCI Dedicated Region25** - Enables organizations to run complete OCI stack with 200+ AI and cloud services starting with just three racks, expandable to hyperscale without downtime; modular scalability from three racks to hyperscale; hyperconverged, high-density standardized infrastructure; multi-layered security including biometric-locked racks; full parity with public cloud services and AI capabilities; Oracle-managed operational model. [26]

- **Oracle Database@AWS** - General availability in July 2025 in North America (AWS Regions us-east-1 Northern Virginia and us-west-2 Oregon); regional expansion with 20 additional regions over coming year including Frankfurt Germany, Tokyo Japan, and Ohio USA. [27]

- **Oracle Database@Azure** - Generally available in 28 regions worldwide as of 2025 with expansion plans to reach 33 regions; includes Oracle Exadata Database Service, Oracle Autonomous Database, and Oracle Database Zero Data Loss Autonomous Recovery Service running on OCI in Microsoft Azure regions. [28]

- **Oracle Database@Google Cloud** - Available in four Google Cloud regions (N. Virginia, Salt Lake City, Frankfurt, London) with expansion planned across North America, Europe, Middle East, Africa, Asia Pacific, and Latin America. [29]

- **Oracle Multicloud Universal Credits** - Introduced October 2025 enabling customers to procure Oracle AI Database and OCI services across Oracle Database@AWS, Oracle Database@Azure, Oracle Database@Google Cloud, and OCI through unified procurement model. [30]

- **Oracle Alloy for Sovereign Clouds** - Partnership with SoftBank launching sovereign cloud/AI platform in Japan using Oracle's Alloy technology to offer 200+ cloud and AI products under strict data sovereignty controls; 60+ OCI Dedicated Regions and Oracle Alloy regions live or planned globally. [31]

---

## Success Metrics

- **Total Remaining Performance Obligations (RPO) - Q2 FY26** - $523 billion, up 438% year-over-year and 15% sequentially (increased $68 billion in Q2). [32]

- **Total Remaining Performance Obligations (RPO) - Q1 FY26** - $455 billion, up 359% year-over-year. [33]

- **Cloud Infrastructure Revenue - Q2 FY26** - $4.1 billion, up 68% in USD and 66% in constant currency. [32]

- **Cloud Infrastructure Revenue - Q1 FY26** - $3.3 billion, up 55% in USD and 54% in constant currency. [33]

- **Total Cloud Revenue - Q2 FY26** - $8.0 billion, up 34% in USD and 33% in constant currency. [32]

- **Total Cloud Revenue - Q1 FY26** - $7.2 billion, up 28% in USD and 27% in constant currency. [33]

- **Total Revenue - Q2 FY26** - $16.1 billion, up 14% in USD and 13% in constant currency. [32]

- **Total Revenue - Q1 FY26** - $14.9 billion, up 12% in USD and 11% in constant currency. [33]

- **Multicloud Database Revenue Growth - Q2 FY26** - 817% year-over-year. [32]

- **Multicloud Database Revenue Growth - Q1 FY26** - 1,529% year-over-year. [33]

- **Non-GAAP EPS - Q2 FY26** - $2.26, up 54% in USD and 51% in constant currency. [32]

- **Non-GAAP EPS - Q1 FY26** - $1.47, up 6% in USD. [33]

- **Operating Cash Flow (12 months) - Q2 FY26** - $22.3 billion, up 10%. [32]

- **NVIDIA Grace Blackwell GB200 Units Delivered** - More than 96,000 units delivered as of Q2 FY26; Oracle delivered 50% more GPU capacity in Q2 versus Q1. [34]

- **FY 2026 Capital Expenditure Guidance** - $50 billion, up from earlier forecast of $35 billion; Q2 capex was $12.0 billion. [34]

- **Historical Capital Expenditures** - FY 2024: $6.9 billion; FY 2025: $21.2 billion; FY 2026 projected: $50 billion. [35]

- **Five-Year OCI Revenue Projections** - FY 2026: $18 billion (77% growth); Year 2: $32 billion; Year 3: $73 billion; Year 4: $114 billion; Year 5: $144 billion. [33]

- **5,000+ Customers Deployed AI Services** - Over 5,000 Oracle customers deployed AI services over the last two years. [36]

- **400+ AI Features in Fusion Cloud Apps** - Oracle has more than 400 AI features live in its Fusion cloud applications. [36]

- **OpenAI Partnership Value** - $300 billion over five years to develop 4.5 gigawatts of additional Stargate data center capacity. [37]

- **Meta Platforms Partnership Value** - $20 billion multiyear cloud computing deal for training and deploying Meta's AI models. [38] [Unverified - source indicates deal was in negotiation as of September 2025, not confirmed as finalized]

- **AI Data Platform Partner Investment** - Leading system integrators committed over $1.5 billion collectively including training 8,000+ practitioners and development of 100+ industry-specific use cases. [12]

- **Data Center Capacity Delivered - Q2 FY26** - Oracle handed over roughly 400 megawatts of data center capacity in Q2 FY 2026. [34]

- **Global Region Expansion** - Oracle has over 211 live and planned regions worldwide, more than any cloud competitor. [32]

- **Multicloud Data Centers** - Oracle building 72 Oracle Multicloud datacenters embedded throughout Amazon, Google, and Microsoft clouds; 23 multicloud data centers live with another 47 under construction as of 2025. [39]

- **Lease Commitments** - $248 billion in additional lease commitments, substantially all related to data centers and cloud capacity arrangements, with 15- to 19-year terms expected to start between Q3 FY2026 and FY2028. [40]

- **NVIDIA GPU Purchase Commitment for OpenAI** - Oracle will purchase around 400,000 NVIDIA GB200s to lease to OpenAI, substantially larger than earlier plans of 64,000 GB200s by end of 2026. [41]

- **OCI Supercluster GPU Scale** - Oracle's GB200 NVL72 systems and OCI Superclusters capable of scaling up to 131,072 NVIDIA GPUs. [42]

- **AMD GPU Partnership** - Oracle and AMD deploying 50,000 AMD Instinct MI450 Series GPUs on OCI starting in Q3 2026. [43]

- **Oracle AI Agent Marketplace Launch** - Over 100 agents from two dozen partners at marketplace launch in October 2025. [17]

- **Oracle AI Agent Studio Certified Experts** - 32,000+ certified experts trained in Oracle AI Agent Studio. [17]

- **AI Agent Deployment Speed** - Clinical AI agent go-lives measured in weeks in highly-regulated healthcare sector, compared to months or years traditionally. [44]

- **Germany AI and Cloud Infrastructure Investment** - $2 billion investment announced expanding Frankfurt region. [45]

- **Stargate Total Investment** - Over $400 billion in investment over three years, on track to secure full $500 billion, 10-gigawatt commitment by end of 2025. [3]

---

## Strategic Intent

- **Full-Stack AI Platform Integration** - Oracle positions itself as the only cloud company providing both scaled AI infrastructure for training models and high-level enterprise applications, differentiating from infrastructure-only competitors; vertical integration from silicon to applications. [46]

- **Private Data as Competitive Moat** - Oracle positioned as by far the world's largest custodian of high-value, private, enterprise data (per Ellison claim); most of the world's high-value data is already in an Oracle database (per Ellison claim); positioning existing Oracle database deployments as strategic assets for AI inference workloads; AI models reasoning on private data will be an even more valuable business than training phase (forward-looking prediction). [47]

- **Infrastructure Scale at Speed** - Building data centers at unprecedented velocity; OpenAI's finance chief stated "No one in the history of man built data centers this fast" regarding Abilene facility; OCI Zettascale10 supporting up to 800,000 NVIDIA GPUs; 1.2-billion-watt AI brain infrastructure. [48]

- **Multi-Cloud Ubiquity Strategy** - Database services embedded in competitor clouds via Oracle Database@AWS, @Azure, @Google Cloud; multicloud revenue growing at 1,529% pace with most growth from Microsoft Azure [33]; Oracle aims to reach $20 billion in revenue within five years through multicloud deployment [49]; Oracle positioned as not believing in building walls or trapping customers (paraphrased from Catz interviews). [49]

- **Database-Centric AI Architecture** - Re-centralizing AI stack around the database rather than separate vector/agent layers; Oracle architected AI and data together to create a next-generation, AI-native database; Select AI Agent provides in-database framework rather than requiring separate vector databases, relational databases, and external Python frameworks; future of enterprise AI isn't in a separate, bolted-on stack but inextricably linked to the data and database. [50]

- **Agentic AI as Enterprise Platform** - In-database AI agents (Select AI Agent) enabling autonomous workflows on private data; quote "AI is going to automatically write the computer programs that will then automate your sales processes and your legal processes and everything else" (Ellison); Oracle has architected Agentic AI directly into the database engine with no-code visual platform including pre-built agents. [51]

- **Cost and Performance Positioning** - OCI positioned as offering more cost-effective AI infrastructure than AWS, Azure, or Google Cloud, particularly for GPU-intensive workloads (Oracle claim); Ellison quote: "Leaders like OpenAI are choosing OCI because it is the world's fastest and most cost-effective AI infrastructure"; Oracle positioned as having "GPU-dense, high-bandwidth 'Supercluster' fabric, optimized for bare-metal performance." [52]

- **AI for Data Vision** - AI-native database with use of AI across entire data and development stack including AI Vector Search, AI for Database Management, AI for Data Development, AI for Application Development, and AI for Analytics; Oracle AI Database 26ai makes AI capabilities "truly simple and intuitive" to work with enterprise data. [53]

- **Sovereignty and Distributed Cloud** - OCI Dedicated Region25 enabling on-premises full-stack deployment in three racks expandable to hyperscale; brings the full power of Oracle Cloud to virtually any data center; 60+ OCI Dedicated Regions and Oracle Alloy regions live or planned globally addressing sovereignty and data locality requirements. [26]

- **NVIDIA Co-innovation Partnership** - Deep integration with NVIDIA AI Enterprise and Blackwell architecture; Oracle and NVIDIA characterized as perfect partners for the age of reasoning—an AI and accelerated computing company working with a key player in processing much of the world's enterprise data; NVIDIA AI Enterprise natively available through OCI Console unlike other offerings through marketplace. [54]

- **AI's Two-Phase Evolution** - Current phase focuses on training models on public data; Phase Two (inference on private data) will be even more valuable business; what will change the world is when we start using these remarkable electronic brains to solve humanity's most difficult problems. [47]

- **Platform of Choice for AI** - Oracle positioned as platform of choice for both AI training and inferencing; Oracle claims all of the top five AI models are in the Oracle Cloud providing advantages over applications competitors (claim requires independent verification as no supporting evidence provided in source). [55]

- **Customer AI Transformation** - CEO Safra Catz messaging: customers in 2025 going all in on cloud moving across infrastructure, database, applications, and vertical applications layers; customers need to be bold and recognize that cloud migration requires operational mindset shifts beyond technology replacement; continuous modernization and adaptation necessary for competitive survival; Catz quote: "Anytime you stop, your competitors are going to pass you." [56]

- **Competitive Market Position Projection** - Oracle Cloud Infrastructure revenue projected to grow from $18 billion (FY2026) to $144 billion (FY2030), positioning for potential parity with AWS by decade's end; analyst prediction that Oracle will surpass Amazon, Microsoft, and Google to become the top cloud for AI by 2031; Oracle characterized as "an AI-first cloud, making it structurally different than the 'big three' cloud providers." [57]

- **IDC MarketScape Leader Recognition** - Named Leader in IDC MarketScape: Worldwide Public Cloud Infrastructure as a Service 2025 Vendor Assessment evaluating 13 providers; recognized for AI infrastructure ("Oracle continues to make significant investments in AI infrastructure—such as with OCI Supercluster") and multicloud strategy ("partnerships with Microsoft, Google, and Amazon are a strong differentiator"). [58]

- **IDC Analytical Database Leader** - Named Leader in IDC MarketScape 2025-2026 Worldwide Analytical Database Assessment for autonomous operations, Exadata infrastructure performance, and broad in-database analytics capabilities supporting machine learning, graph, spatial, JSON, and vector workloads. [59]

- **Forrester Analyst Positioning** - Forrester positioned Oracle as the "central nervous system" of the agentic enterprise; Oracle's integrated platform promises rapid value for existing customers by simplifying integration and data governance; Oracle AI World 2025 marked first annual conference with co-CEOs Clay Magouyrk and Mike Sicilia leading cloud infrastructure and applications respectively. [60]

- **Power-First Campus Model** - Data center strategy employs power-first campus model combining grid PPAs (power purchase agreements), on-site generation, and advanced geothermal to support multi-gigawatt deployments. [61]

- **Liquid Cooling Technology Deployment** - Deploys liquid-cooled NVL72 racks designed for maximum GPU density and thermal efficiency, critical for Blackwell architecture power requirements. [61]

- **Chip Neutrality Policy** - Larry Ellison announced Oracle's commitment to "a policy of chip neutrality where we work closely with all our CPU and GPU suppliers" while continuing to buy latest NVIDIA GPUs and deploying 50,000 AMD AI chips; strategy allows Oracle to "be prepared and able to deploy whatever chips our customers want to buy." [43]

- **U.S. Government Partnership** - Landmark public-private partnership with Department of Energy, Argonne National Laboratory, and NVIDIA to deliver DOE's largest AI supercomputer; Solstice system featuring 100,000 NVIDIA Blackwell GPUs and Equinox system featuring 10,000 NVIDIA Blackwell GPUs. [62]

- **Industry Analyst Validation** - NAND Research: "No one can match Oracle's breadth of integrated AI features combined with its focus on enterprise-grade security, data integrity, and massive scalability"; Constellation Research: "Release of its latest AI Database, 26ai, takes it to a whole new level by significantly accelerating time-to-value while radically reducing complexity." [63]

- **Open Standards Integration** - Agent Hub and AI Agent marketplace support open standards including Agent2Agent (A2A) and Model Context Protocol (MCP) allowing customers to create sophisticated multi-agent systems. [16]

- **Model Access Diversity** - Oracle OCI Generative AI supports multiple leading AI models including Google's Gemini 2.5 family (Pro, Flash, Flash-Lite), xAI's Grok models (Grok 4 and series), Meta's Llama 4 models (Scout and Maverick), Cohere's Command A and Rerank, and OpenAI's gpt-oss open-source models for database analysis and application development. [9][7][22][21][19]

- **Leadership Transition to Co-CEO Structure** - Oracle AI World 2025 marked first annual conference with co-CEOs Clay Magouyrk (Cloud Infrastructure) and Mike Sicilia (Applications) leading their respective divisions. [60][65]

- **Michigan Data Center Economic Impact** - Construction creating 2,500 union construction jobs; once complete providing estimated 450 good-paying jobs on-site and 1,500 across Washtenaw County; Oracle to operate data center and outfit with latest technology for OpenAI. [66]

- **Stargate Site Selection Process** - OpenAI, Oracle, and SoftBank reviewed over 300 proposals from more than 30 states in site-selection contest launched in January 2025 before announcing first batch of five Stargate locations in September 2025. [67]

- **Autonomous AI Lakehouse Competitive Positioning** - Positions Oracle to compete directly with Databricks and Snowflake by supporting open Apache Iceberg format while integrating Oracle's AI-native database capabilities. [68]

- **AI Vector Search Pricing Strategy** - Advanced AI features such as AI Vector Search included at no additional charge, signaling Oracle's commitment to making AI adoption frictionless for existing customer base. [69]

- **Converged Database Unified Platform** - AI Database 26ai adds vectors and AI agents as native, first-class citizens, offering single integrated platform instead of requiring customers to stitch together vector database for RAG, separate relational database for transactions, and external Python framework for agents. [70]

- **Multi-Hyperscaler Database Availability** - Oracle Autonomous AI Lakehouse available on all four major hyperscalers (OCI, AWS, Azure, Google Cloud) with interoperability across Databricks and Snowflake. [11]

---

## Sources

[1] OpenAI - Announcing the Stargate Project - https://openai.com/index/announcing-the-stargate-project/ - Published: January 21, 2025

[2] OpenAI - Stargate advances with 4.5 GW partnership with Oracle - https://openai.com/index/stargate-advances-with-partnership-with-oracle/ - Published: July 2025

[3] OpenAI - Five New Stargate Sites - https://openai.com/index/five-new-stargate-sites/ - Published: September 23, 2025

[4] Oracle - Oracle Introduces AI Agent Studio - https://www.oracle.com/news/announcement/oracle-introduces-ai-agent-studio-2025-03-20/ - Published: March 20, 2025

[5] Oracle Docs - OCI Generative AI Agents March 26, 2025 Release - https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai-agents/new-tools.htm - Published: March 26, 2025

[6] Oracle Docs - OCI Generative AI Agents July 2025 Features - https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai-agents/features-2025-july.htm - Published: July 2025

[7] Oracle Blog - Announcing Meta Llama 4 model support on OCI Generative AI - https://blogs.oracle.com/ai-and-datascience/announcing-meta-llama-4-support-oci-generative-ai - Published: May 2025

[8] Oracle - Oracle and NVIDIA Help Enterprises and Developers Accelerate AI Innovation - https://www.oracle.com/news/announcement/oracle-and-nvidia-help-enterprises-and-developers-accelerate-ai-innovation-2025-06-12/ - Published: June 12, 2025

[9] Oracle Docs - Use Google Gemini 2.5 in OCI Generative AI - https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/gemini-2-5-GA.htm - Published: August 2025

[10] Oracle - Oracle AI Database 26ai Powers the AI for Data Revolution - https://www.oracle.com/news/announcement/ai-world-database-26ai-powers-the-ai-for-data-revolution-2025-10-14/ - Published: October 14, 2025

[11] Oracle - Oracle Autonomous AI Lakehouse Enables Open, Interoperable Data Access - https://www.oracle.com/asean/news/announcement/ai-world-oracle-introduces-autonomous-ai-lakehouse-2025-10-14/ - Published: October 14, 2025

[12] Oracle - Oracle Unveils AI Data Platform, Empowering Customers to Innovate in the AI Era - https://www.oracle.com/news/announcement/ai-world-oracle-unveils-ai-data-platform-empowering-customers-to-innovate-in-the-ai-era-2025-10-14/ - Published: October 14, 2025

[13] Oracle - Oracle Unveils Next-Generation OCI Zettascale10 Cluster for AI - https://www.oracle.com/news/announcement/ai-world-oracle-unveils-next-generation-oci-zettascale10-cluster-for-ai-2025-10-14/ - Published: October 14, 2025

[14] Oracle Blog - Announcing the Oracle Autonomous AI Database MCP Server - https://blogs.oracle.com/machinelearning/announcing-the-oracle-autonomous-ai-database-mcp-server - Published: October 14, 2025

[15] Oracle Blog - Oracle AI World: Announcing New Innovations in AI and Data on OCI - https://blogs.oracle.com/cloud-infrastructure/ai-world-2025-artificial-intelligence - Published: October 14, 2025

[16] Oracle Blog - Oracle AI World: Announcing New Innovations in AI and Data on OCI - https://blogs.oracle.com/cloud-infrastructure/ai-world-2025-artificial-intelligence - Published: October 14, 2025

[17] Oracle - Oracle Launches Fusion Applications AI Agent Marketplace - https://www.oracle.com/news/announcement/ai-world-oracle-launches-fusion-applications-ai-agent-marketplace-to-accelerate-enterprise-ai-adoption-2025-10-15/ - Published: October 15, 2025

[18] Oracle - Oracle Advances Enterprise AI with New Agents Across Fusion Applications - https://www.oracle.com/news/announcement/ai-world-oracle-advances-enterprise-ai-with-new-agents-across-fusion-applications-2025-10-15/ - Published: October 15, 2025

[19] Oracle Blog - OCI Generative AI Introduces gpt-oss models and Model Import - https://blogs.oracle.com/ai-and-datascience/oci-introduces-gpt-oss-models-and-model-import - Published: December 2025

[20] Oracle Blog - OCI Generative AI Introduces gpt-oss models and Model Import - https://blogs.oracle.com/ai-and-datascience/oci-introduces-gpt-oss-models-and-model-import - Published: December 2025

[21] Oracle Blog - Announcing Cohere Command A and Rerank models on OCI Generative AI - https://blogs.oracle.com/ai-and-datascience/cohere-command-a-rerank-oci-gen-ai - Published: 2025

[22] Oracle Docs - OCI Generative AI now supports xAI Grok 4 - https://docs.oracle.com/en-us/iaas/releasenotes/generative-ai/grok-4.htm - Published: 2025

[23] Oracle Docs - Data Science Release Notes - https://docs.public.content.oci.oraclecloud.com/en-us/iaas/releasenotes/services/data-science/index.htm - Published: 2025

[24] Futurum Group - Oracle AI World 2025: Is the Database the Center of the AI Universe Again? - https://futurumgroup.com/insights/oracle-ai-world-2025-is-the-database-the-center-of-the-ai-universe-again/ - Published: October 14, 2025

[25] Oracle - Oracle and NVIDIA Collaborate to Help Enterprises Accelerate Agentic AI Inference - https://www.oracle.com/news/announcement/oracle-and-nvidia-collaborate-to-help-enterprises-accelerate-agentic-ai-inference-2025-03-18/ - Published: March 18, 2025

[26] Oracle - OCI Enables More Customers to Rapidly Deploy AI and Cloud Services - https://www.oracle.com/news/announcement/ai-world-oracle-cloud-infrastructure-enables-more-customers-to-rapidly-deploy-ai-and-cloud-services-2025-10-14/ - Published: October 14, 2025

[27] Robust Cloud - Oracle Multicloud Partnership - https://www.robustcloud.com/oracle-multicloud-partnership/ - Published: July 2025

[28] Oracle - Multicloud Strategy - https://www.oracle.com/cloud/multicloud/clay-magouyrk-oracle-cloud-aws-google-azure/ - Published: 2025

[29] Oracle - Multicloud Strategy - https://www.oracle.com/cloud/multicloud/clay-magouyrk-oracle-cloud-aws-google-azure/ - Published: 2025

[30] Oracle - Oracle Introduces Multicloud Universal Credits - https://www.oracle.com/news/announcement/ai-world-oracle-introduces-multicloud-universal-credits-2025-10-14/ - Published: October 14, 2025

[31] Futurum Group - Oracle AI World 2025: Is the Database the Center of the AI Universe Again? - https://futurumgroup.com/insights/oracle-ai-world-2025-is-the-database-the-center-of-the-ai-universe-again/ - Published: October 14, 2025

[32] Oracle - Q2 FY26 Earnings Release - https://www.oracle.com/news/announcement/q2fy26-earnings-release-2025-12-10/ - Published: December 10, 2025

[33] Oracle - Q1 FY26 Earnings Release - https://www.oracle.com/news/announcement/q1fy26-earnings-release-2025-09-09/ - Published: September 9, 2025

[34] Futurum Group - Oracle Q2 FY 2026: Cloud Grows, Capex Rises for AI Buildout - https://futurumgroup.com/insights/oracle-q2-fy-2026-cloud-grows-capex-rises-for-ai-buildout/ - Published: 2025

[35] Data Center Magazine - Oracle's Data Centre Strategy: Cloud, AI and More Capacity - https://datacentremagazine.com/news/oracles-data-centre-strategy-cloud-ai-and-more-capacity - Published: 2025

[36] Oracle - OCI Enables More Customers to Rapidly Deploy AI and Cloud Services - https://www.oracle.com/news/announcement/ai-world-oracle-cloud-infrastructure-enables-more-customers-to-rapidly-deploy-ai-and-cloud-services-2025-10-14/ - Published: October 14, 2025

[37] IntuitionLabs - Oracle OpenAI $300B Deal Analysis - https://intuitionlabs.ai/articles/oracle-openai-300b-deal-analysis - Published: 2025

[38] Data Center Dynamics - Meta signs deal with Oracle Cloud for AI training - https://www.datacenterdynamics.com/en/news/meta-signs-deal-with-oracle-cloud-for-ai-training/ - Published: 2025

[39] CloudWars - Larry Ellison Sees Oracle Multicloud Boom - https://cloudwars.com/cloud/larry-ellison-sees-oracle-multicloud-boom-as-google-amazon-customers-jump-aboard/ - Published: 2025

[40] ERP Today - Oracle loads up on AI infrastructure as OCI backlog, data center commitments surge - https://erp.today/oracle-loads-up-on-ai-infrastructure-as-oci-backlog-data-center-commitments-surge/ - Published: 2025

[41] Data Center Dynamics - Oracle to spend $40bn on Nvidia chips for OpenAI Texas data center - https://www.datacenterdynamics.com/en/news/oracle-to-spend-40bn-on-nvidia-chips-for-openai-texas-data-center/ - Published: 2025

[42] Oracle Blog - Leader in the 2025 IDC MarketScape for Worldwide Public IaaS - https://blogs.oracle.com/cloud-infrastructure/post/leader-2025-idc-marketscape-worldwide-public-iaas - Published: 2025

[43] CIO Dive - Oracle, AMD to deploy 50K AI accelerators - https://www.ciodive.com/news/oracle-amd-nvidia-AI-infrastructure/802772/ - Published: 2025

[44] CX Today - Oracle reports faster AI agent rollouts - https://www.cxtoday.com/ai-automation-in-cx/oracle-reports-faster-ai-agent-rollouts-in-weeks-not-years-but-investor-doubts-linger/ - Published: 2025

[45] Oracle - Oracle Invests Two Billion Dollars in AI and Cloud Infrastructure - https://www.oracle.com/news/announcement/oracle-invests-two-billion-dollars-in-ai-and-cloud-infrastructure-2025-07-15/ - Published: July 15, 2025

[46] The Neuron - Larry Ellison's Keynote on Oracle's Vision and Strategy from Oracle AI World 2025 Explained - https://www.theneuron.ai/explainer-articles/larry-ellisons-keynote-on-oracles-vision-and-strategy-from-oracle-ai-world-2025-explained - Published: October 14, 2025

[47] The Neuron - Larry Ellison's Keynote on Oracle's Vision and Strategy from Oracle AI World 2025 Explained - https://www.theneuron.ai/explainer-articles/larry-ellisons-keynote-on-oracles-vision-and-strategy-from-oracle-ai-world-2025-explained - Published: October 14, 2025

[48] The Neuron - Larry Ellison's Keynote on Oracle's Vision and Strategy from Oracle AI World 2025 Explained - https://www.theneuron.ai/explainer-articles/larry-ellisons-keynote-on-oracles-vision-and-strategy-from-oracle-ai-world-2025-explained - Published: October 14, 2025

[49] CloudWars - CEO Outlook 2025: Oracle's Safra Catz - https://cloudwars.com/innovation-leadership/ceo-outlook-2025-oracles-safra-catz-customers-all-in-on-cloud/ - Published: January 6, 2025

[50] Futurum Group - Oracle AI World 2025: Is the Database the Center of the AI Universe Again? - https://futurumgroup.com/insights/oracle-ai-world-2025-is-the-database-the-center-of-the-ai-universe-again/ - Published: October 14, 2025

[51] The Next Platform - Oracle Cloud Can Be As Big As AWS This Decade - http://www.nextplatform.com/2025/09/14/oracle-cloud-can-be-as-big-as-aws-this-decade/ - Published: September 14, 2025

[52] Data Center Frontier - OpenAI and Oracle's $300B Stargate Deal: Building AI's National Scale Infrastructure - https://www.datacenterfrontier.com/machine-learning/article/55316610/openai-and-oracles-300b-stargate-deal-building-ais-national-scale-infrastructure - Published: September 18, 2025

[53] Oracle Database 26ai Product Page - https://www.oracle.com/database/ai-native-database-26ai/ - Published: October 14, 2025

[54] NVIDIA Newsroom - Oracle and NVIDIA Collaborate to Help Enterprises Accelerate Agentic AI Inference - https://nvidianews.nvidia.com/news/oracle-and-nvidia-collaborate-to-help-enterprises-accelerate-agentic-ai-inference - Published: March 18, 2025

[55] Oracle - Q2 FY26 Earnings Release - https://www.oracle.com/news/announcement/q2fy26-earnings-release-2025-12-10/ - Published: December 10, 2025

[56] CloudWars - Oracle CEO Safra Catz Exclusive Interview: Innovation Drives Civilizations Not Just Companies - https://cloudwars.com/innovation-leadership/oracle-ceo-safra-catz-exclusive-interview-innovation-drives-civilizations-not-just-companies/ - Published: 2025

[57] The Motley Fool - Prediction: Oracle Will Surpass Amazon, Microsoft, and Google to Become the Top Cloud for AI By 2031 - https://www.fool.com/investing/2025/09/16/prediction-oracle-will-surpass-amazon-microsoft-an/ - Published: September 16, 2025

[58] Oracle - Oracle recognized as a Leader in the 2025 IDC MarketScape Report for Worldwide Public Cloud Infrastructure as a Service - https://www.oracle.com/news/announcement/oracle-recognized-as-a-leader-in-the-2025-idc-marketscape-report-for-worldwide-public-cloud-infrastructure-as-a-service-2025-02-06/ - Published: February 6, 2025

[59] Oracle Database - IDC MarketScape Analytical Databases - https://www.oracle.com/database/idc-marketscape-analytical-databases/ - Published: 2025

[60] Forrester - Oracle AI World 2025: The First Look Under New Command - https://www.forrester.com/blogs/oracle-ai-world-2025-the-first-look-under-new-command/ - Published: October 2025

[61] Data Center Frontier - OpenAI and Oracle's $300B Stargate Deal: Building AI's National Scale Infrastructure - https://www.datacenterfrontier.com/machine-learning/article/55316610/openai-and-oracles-300b-stargate-deal-building-ais-national-scale-infrastructure - Published: September 18, 2025

[62] U.S. Department of Energy - Energy Department Announces New Partnership with NVIDIA and Oracle to Build Largest DOE AI - https://www.energy.gov/articles/energy-department-announces-new-partnership-nvidia-and-oracle-build-largest-doe-ai - Published: October 2025

[63] Oracle Database Blog - Industry Analyst Quotes on Oracle AI Database News at AI World 2025 - https://blogs.oracle.com/database/industry-analyst-quotes-on-oracle-ai-database-news-at-ai-world-2025 - Published: October 14, 2025

[64] The Software Report - Oracle Unveils OCI Generative AI Service Pioneering Enterprise Adoption - https://www.thesoftwarereport.com/oracle-unveils-oci-generative-ai-service-pioneering-enterprise-adoption/ - Published: 2025

[65] Forrester - Oracle AI World 2025: The First Look Under New Command - https://www.forrester.com/blogs/oracle-ai-world-2025-the-first-look-under-new-command/ - Published: October 2025

[66] Oracle - Oracle is set to power on new data center in Michigan - https://www.oracle.com/news/announcement/blog/oracle-is-set-to-power-on-new-data-center-in-michigan-2025-1018/ - Published: October 18, 2025

[67] Axios - Stargate Five Sites - https://www.axios.com/2025/09/23/openai-stargate-oracle-softbank-texas - Published: September 23, 2025

[68] Futurum Group - Oracle AI World 2025: Is the Database the Center of the AI Universe Again? - https://futurumgroup.com/insights/oracle-ai-world-2025-is-the-database-the-center-of-the-ai-universe-again/ - Published: October 14, 2025

[69] Oracle - Oracle AI Database 26ai Powers the AI for Data Revolution - https://www.oracle.com/news/announcement/ai-world-database-26ai-powers-the-ai-for-data-revolution-2025-10-14/ - Published: October 14, 2025

[70] Futurum Group - Oracle AI World 2025: Is the Database the Center of the AI Universe Again? - https://futurumgroup.com/insights/oracle-ai-world-2025-is-the-database-the-center-of-the-ai-universe-again/ - Published: October 14, 2025
