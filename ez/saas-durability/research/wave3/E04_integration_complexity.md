# E04: Integration Complexity and Enterprise Build vs. Buy Decisions

**Research Area:** Enterprise SaaS Durability in the Agentic Coding Era
**Wave:** 3 — Integration Complexity and Platform Sprawl
**Audience:** C-Suite
**Date Compiled:** March 2026

---

## Executive Summary

Enterprise integration complexity has reached a structural inflection point. The average large enterprise now manages nearly 900 applications, yet fewer than 3% of organizations have successfully integrated more than half of them. This integration gap simultaneously makes it harder to replace SaaS (because replacing one node in a tightly coupled mesh is expensive) and harder to stay with SaaS (because per-vendor integration debt accumulates with every renewal). A parallel shift is underway: 35% of enterprise teams have already replaced at least one SaaS product with a custom build, and 78% expect to build more in 2026, driven by AI-assisted development that compresses build timelines. Integration complexity is the single variable that most shapes which path organizations take — and iPaaS and middleware platforms are emerging as the swing factor that can either accelerate or impede both routes.

---

## Section 1: The Scale of Enterprise Integration Complexity

### 1.1 Application and System Counts

[STATISTIC]
"The average number of apps used by respondents is 897 — with 45% reporting using 1,000 applications or more."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers, revenues >$500M, conducted Oct–Nov 2024, in collaboration with Vanson Bourne and Deloitte Digital)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[STATISTIC]
"127 average SaaS subscriptions per enterprise (up from 94 in 2023)"
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[STATISTIC]
"73% of enterprises operate 900+ applications"
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[STATISTIC]
Large enterprises: 250–500+ SaaS applications; mid-market organizations: 150–250; small businesses: 25–70.
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

[STATISTIC]
"SaaS companies globally: 30,000 companies worldwide; 17,000+ in the US. Average company SaaS reliance: 112 SaaS applications per organization."
— Prismatic, 2025 Integration Trends — Mid-Year Perspective
URL: https://prismatic.io/blog/integration-trends/
Date: 2025

### 1.2 The Integration Gap

[STATISTIC]
"Only 2% of businesses have successfully integrated more than half of their applications."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[STATISTIC]
"41% of applications remain unintegrated across the average organization"
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-solutions/
Date: January 2025

[STATISTIC]
"71% of applications remain unintegrated (unchanged 2023–2025)"
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

[STATISTIC]
"Integration project timelines increased 34% compared to 2023"
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[STATISTIC]
"The percentage of projects not delivered on time has risen to 29% in 2024 — up from 26% in 2023."
— MuleSoft 2025 Connectivity Benchmark Report
URL: https://www.salesforce.com/blog/mulesoft-connectivity-benchmark-2025/
Date: January 2025

[STATISTIC]
"89% operate hybrid environments with on-premises and cloud systems. Hybrid integration scenarios take 56% longer to implement than purely cloud-based integrations."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

### 1.3 Data Silos and Business Impact

[STATISTIC]
"On average, 90% of IT leaders say data silos are creating business challenges in their organization."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://www.salesforce.com/blog/mulesoft-connectivity-benchmark-2025/
Date: January 2025

[STATISTIC]
"98% of IT teams report automation issues cause SLA breaches"
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

[STATISTIC]
"3 in 4 enterprises (76%) have experienced at least one negative outcome due to disconnected AI"
— Zapier AI Sprawl Survey, reported December 3, 2025
URL: https://zapier.com/blog/ai-sprawl-survey/
Date: December 2025

---

## Section 2: Integration as a Barrier to Custom-Built Software

### 2.1 Integration Complexity Cited as a Top Build Barrier

[STATISTIC]
"39% face integration challenges" among technical barriers to AI automation in enterprises.
— Retool 2026 Build vs. Buy Report (n=817 builders surveyed late 2025)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
"Integration complexity is cited as a top barrier for scaling by 64% of organizations"
— World Quality Report 2025 (n=2,000+ senior executives in 22 countries)
URL: https://www.prnewswire.com/news-releases/world-quality-report-2025-ai-adoption-surges-in-quality-engineering-but-enterprise-level-scaling-remains-elusive-302614772.html
Date: 2025

[STATISTIC]
"39% of developer time spent on custom integrations"
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

[STATISTIC]
Cost barriers to integration: "54% cite consulting/implementation costs; 50% cite tool/product costs"
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

[STATISTIC]
"Legacy system dependencies affect 64% of organizations, consuming 16+ hours weekly."
— Integrate.io, Data Integration Adoption Rates in Enterprises: 45 Statistics Every IT Leader Should Know in 2026
URL: https://www.integrate.io/blog/data-integration-adoption-rates-enterprises/
Date: 2026

[STATISTIC]
"Integration with legacy systems alone can extend [project] timelines by 30–50%."
— Scale Up Ally, How Much Do Integrations Cost?
URL: https://scaleupally.io/blog/cost-of-integration/
Date: 2025

### 2.2 The True Cost of Custom Integration

[STATISTIC]
"Custom integrations can add $5,000–$25,000 each to implementation costs, while API development typically bills at $150–$250 per developer hour."
— Scale Up Ally, How Much Do Integrations Cost?
URL: https://scaleupally.io/blog/cost-of-integration/
Date: 2025

[STATISTIC]
"Organizations spend an average of $30 million maintaining each legacy system."
— RecordPoint, The Hidden Costs of Maintaining Legacy Systems
URL: https://www.recordpoint.com/blog/maintaining-legacy-systems-costs
Date: 2025

[STATISTIC]
"By 2025, companies will spend 40% of their IT budgets on maintaining technical debt." (Gartner forecast)
— Devsquad, 12 Costs of Maintaining Legacy Systems
URL: https://devsquad.com/blog/costs-of-maintaining-legacy-systems
Date: 2025

[STATISTIC]
"67% of software projects fail because of wrong build vs. buy choices." (Forrester Research)
— CIO.com, Build vs. Buy: A CIO's Journey Through the Software Decision Maze
URL: https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
Date: 2025

### 2.3 The Shadow IT Signal

[STATISTIC]
"60% of builders created tools outside IT oversight in the past year; 25% report doing so frequently."
— Retool 2026 Build vs. Buy Report (n=817 builders surveyed late 2025)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
Among reasons builders cited for circumventing IT: "10% cited poor integrations" as a driver.
— Retool 2026 Build vs. Buy Report (n=817 builders surveyed late 2025)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
"Nearly 40 percent of deployed apps" in enterprises stem from unapproved shadow IT purchases.
— Krishna Avva, From SaaS Sprawl to Agent Sprawl (citing JumpCloud shadow IT analysis)
URL: https://avva-krishna.com/2026/01/17/from-saas-sprawl-to-agent-sprawl-how-to-architect-the-next-enterprise-era/
Date: January 17, 2026

---

## Section 3: SaaS Platforms as Integration Hubs vs. Integration Headaches

### 3.1 The Hub Argument

[STATISTIC]
Platform selection criteria for enterprise integration tools, ranked by importance: "Connectivity breadth: 78%; Scalability and performance: 71%; Developer experience: 67%; Total cost of ownership: 64%; AI and automation capabilities: 58%."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[STATISTIC]
"Workato connects to over 1,200 applications" as of early 2026; Workato closed FY26 with 35% year-over-year ARR growth and is a Gartner Magic Quadrant Leader in iPaaS for seven consecutive years.
— Workato, Reports Record Momentum (BusinessWire)
URL: https://www.businesswire.com/news/home/20260227618624/en/Workato-Reports-Record-Momentum-Defining-the-Future-of-Orchestration-for-the-Agentic-Era
Date: February 27, 2026

[STATISTIC]
"82% [of enterprises] adopted API-first strategies. Only 29% have comprehensive API governance frameworks. Organizations with mature API governance reduce integration project time by 47%."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[FACT]
"Organizations implementing composable architecture achieve 42% faster time-to-market for new integration projects."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

### 3.2 The Sprawl and Headache Argument

[STATISTIC]
"Up to half of their paid [SaaS] licenses go unused" in many enterprises.
— Krishna Avva, From SaaS Sprawl to Agent Sprawl (citing Zylo SaaS Management Index 2024)
URL: https://avva-krishna.com/2026/01/17/from-saas-sprawl-to-agent-sprawl-how-to-architect-the-next-enterprise-era/
Date: January 17, 2026

[STATISTIC]
"Tool sprawl limits AI integration for 70% of enterprises"
— Zapier AI Sprawl Survey, Dylan Reber
URL: https://zapier.com/blog/ai-sprawl-survey/
Date: December 3, 2025

[STATISTIC]
"Over a quarter of enterprises (28%) now use more than 10 different AI apps."
— Zapier AI Sprawl Survey
URL: https://zapier.com/blog/ai-sprawl-survey/
Date: December 3, 2025

[STATISTIC]
"61% [of enterprises] cannot accurately inventory credentials in integration infrastructure. The average enterprise processes credentials for 340+ systems."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[QUOTE]
"The sprawl creates multiple challenges: Integration debt with brittle connectors and expensive middleware maintenance, security and compliance exposure from more APIs and access surfaces, and operational bloat from vendor management and monitoring."
— Krishna Avva, From SaaS Sprawl to Agent Sprawl
URL: https://avva-krishna.com/2026/01/17/from-saas-sprawl-to-agent-sprawl-how-to-architect-the-next-enterprise-era/
Date: January 17, 2026

[QUOTE]
"There's no way you can go live with a vibe-coded solution. It might work for demos."
— Pierre Yves Calloc'h, Pernod Ricard (on the limits of AI-generated code in enterprise integration contexts)
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

---

## Section 4: How Agentic Coding Handles Integration Challenges

### 4.1 Integration as the Primary Agentic Deployment Barrier

[STATISTIC]
"46% cite integration with existing systems as their primary challenge" for enterprise AI agent deployment.
— Arcade.dev, 2026 State of AI Agents Report (Anthropic Claude team)
URL: https://www.arcade.dev/blog/5-takeaways-2026-state-of-ai-agents-claude/
Date: 2026

[STATISTIC]
"95% of IT leaders report integration as a hurdle to implementing AI effectively."
— MuleSoft 2025 Connectivity Benchmark Report (n=1,050 IT decision-makers)
URL: https://www.salesforce.com/blog/mulesoft-connectivity-benchmark-2025/
Date: January 2025

[STATISTIC]
"More than 4 in 5 IT leaders believe that AI agents will create more complexity than value due to integration challenges and silos."
— Reported in BigDATAwire / HPCwire, The Connectivity Paradox Holding Back Enterprise Agentic AI
URL: https://www.hpcwire.com/bigdatawire/2026/02/10/the-connectivity-paradox-holding-back-enterprise-agentic-ai/
Date: February 10, 2026

[STATISTIC]
"Nearly 60% of AI leaders surveyed by Deloitte [say] their organization's primary challenges in adopting agentic AI are integrating with legacy systems and addressing risk and compliance concerns."
— Deloitte, Agentic AI Strategy (Tech Trends 2026)
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

### 4.2 Emerging Standards Reducing Integration Friction

[FACT]
Model Context Protocol (MCP) was announced by Anthropic in November 2024 as an open standard for connecting AI assistants to data systems including content repositories, business management tools, and development environments.
— Wikipedia, Model Context Protocol
URL: https://en.wikipedia.org/wiki/Model_Context_Protocol
Date: 2025

[STATISTIC]
"One year after launch, MCP has become the universal standard for connecting AI agents to enterprise tools — with 97M+ monthly SDK downloads and backing from Anthropic, OpenAI, Google, and Microsoft. MCP server downloads grew from ~100,000 in November 2024 to over 8 million by April 2025, with over 5,800+ MCP servers and 300+ MCP clients now available."
— Pento AI, A Year of MCP: From Internal Experiment to Industry Standard
URL: https://www.pento.ai/blog/a-year-of-mcp-2025-review
Date: 2025

[STATISTIC]
"Organizations implementing the Model Context Protocol report 40–60% faster agent deployment times."
— Deepak Gupta, Model Context Protocol (MCP) Guide: Enterprise Adoption 2025
URL: https://guptadeepak.com/the-complete-guide-to-model-context-protocol-mcp-enterprise-adoption-market-trends-and-implementation-strategies/
Date: 2025

### 4.3 Deployment Gap Despite Integration Progress

[STATISTIC]
"While 30% of surveyed organizations are exploring agentic options and 38% are piloting solutions, only 14% have solutions that are ready to be deployed and a mere 11% are actively using these systems in production."
— Deloitte, Agentic AI Strategy (Tech Trends 2026)
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

[STATISTIC]
"Gartner predicts over 40% of agentic AI projects will be canceled by the end of 2027 due to escalating costs, unclear business value, or inadequate risk controls." Legacy system integration is cited as a primary failure driver.
— Deloitte, Agentic AI Strategy (Tech Trends 2026), citing Gartner
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

[STATISTIC]
"Pilots built through strategic partnerships are twice as likely to reach full deployment compared to those built internally, with employee usage rates nearly double for externally built tools."
— Deloitte, Agentic AI Strategy (Tech Trends 2026)
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

---

## Section 5: Enterprise Architects' Views on Custom vs. Packaged Integration

### 5.1 The Hybrid Frame Is Dominant

[QUOTE]
"Low-code platforms, API-first commercial solutions and microservices architectures enable hybrid approaches that weren't previously possible."
— Hani Arab, CIO, Seymour Whyte Construction
— CIO.com, Build vs. Buy: A CIO's Journey Through the Software Decision Maze
URL: https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
Date: 2025

[STATISTIC]
"47% combine off-the-shelf agents with custom development; 21% rely entirely on pre-built solutions; 20% build all agents in-house."
— Arcade.dev, 2026 State of AI Agents Report (Anthropic Claude team)
URL: https://www.arcade.dev/blog/5-takeaways-2026-state-of-ai-agents-claude/
Date: 2026

[QUOTE]
"We realized we could build these tools ourselves and save on multiple subscriptions."
— Borys Aptekar, GTM AI Product Manager, ClickUp
— Retool 2026 Build vs. Buy Report (n=817 builders surveyed late 2025)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[QUOTE]
"Their support was so slow that it was faster for me to rebuild the product [inside Retool] than wait for support to get back to me."
— Miles Konstantin, Head of Automation, Harmonic
— Retool 2026 Build vs. Buy Report (n=817 builders surveyed late 2025)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

### 5.2 The Momentum of Custom Builds

[STATISTIC]
"35% of teams have already replaced at least one SaaS tool with a custom build; 78% expect to build more custom internal tools in 2026."
— Retool 2026 Build vs. Buy Report (n=817 builders surveyed late 2025, spanning engineering, ops, product, data, IT, finance at companies from startups to Fortune 500s)
URL: https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
Date: February 17, 2026

[STATISTIC]
SaaS categories under highest replacement pressure: "Workflow automations (35%), internal admin tools (33%), BI tools (29%), CRMs and form builders (25%), project management (23%), customer support (21%)."
— Retool 2026 Build vs. Buy Report (n=817 builders)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
"51% have built production software using AI" (among Retool's surveyed builders).
— Retool 2026 Build vs. Buy Report (n=817 builders)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
"49% of production tool builders save 6+ hours per week" using AI-assisted development.
— Retool 2026 Build vs. Buy Report (n=817 builders)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

### 5.3 Enterprise Architects on Governance

[QUOTE]
"Your future edge will not come from how many agents you deploy but from how intelligently you design, monitor, and evolve them."
— Krishna Avva, From SaaS Sprawl to Agent Sprawl
URL: https://avva-krishna.com/2026/01/17/from-saas-sprawl-to-agent-sprawl-how-to-architect-the-next-enterprise-era/
Date: January 17, 2026

[QUOTE]
"Don't simply pave the cow path. Instead, take advantage of this AI evolution to reimagine how agents can best collaborate."
— Brent Collins, VP AI Strategy, Intel
— Deloitte, Agentic AI Strategy (Tech Trends 2026)
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

---

## Section 6: iPaaS and Middleware as Enablers and Barriers

### 6.1 Market Scale

[STATISTIC]
"Global iPaaS market: $12.87 billion (2024) → $15.63 billion (2025) → $78.28 billion (2032), CAGR 25.9%."
— Fortune Business Insights, cited in Albato State of Integrations Report 2025
URL: https://albato.com/blog/publications/state-of-integrations-report
Date: 2025

[STATISTIC]
"Global system integration market: $410.25 billion (2024) → $442.53 billion (2025) → $932.66 billion (2032)."
— Albato, State of Integrations Report 2025
URL: https://albato.com/blog/publications/state-of-integrations-report
Date: 2025

[STATISTIC]
"270 iPaaS solutions available in market; 900+ total integration solutions in market."
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

[STATISTIC]
"System integrators: $863.8 billion revenue (8.9% of IT spending). Top 20 GSIs: $448.7 billion (51.9% of SI market)."
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

[STATISTIC]
"58% of organizations plan to replace legacy middleware with cloud-native integration solutions."
— Industry Research Biz, Integration Platform as a Service (iPaaS) Market report
URL: https://www.industryresearch.biz/market-reports/integration-platform-as-a-service-ipaas-market-104844
Date: 2025

### 6.2 iPaaS as Enabler

[STATISTIC]
"73.2% of companies increased automation spending in the past year; 36.6% of organizations report achieving 25%+ cost reductions; 68.8% of organizations rate automation as mission-critical."
— Enterprise Automation Index 2025, cited in Albato State of Integrations Report 2025
URL: https://albato.com/blog/publications/state-of-integrations-report
Date: 2025

[STATISTIC]
"By 2026, 80% of low-code users will be outside IT departments." (Gartner prediction)
— Albato, State of Integrations Report 2025 (citing Gartner)
URL: https://albato.com/blog/publications/state-of-integrations-report
Date: 2025

[STATISTIC]
"74% of organizations are implementing enterprise orchestration to close the trust gap between AI investment and adoption."
— Workato / Harvard Business Review, 2025 Enterprise Agentic AI Report
URL: https://www.workato.com/full-reports/2025-hbr-enterprise-agentic-ai
Date: 2025

[STATISTIC]
"Forrester Total Economic Impact study [on iPaaS] reveals $2.4 million in developer productivity gains and $3.2 million in incremental revenue growth. Companies report $654,000 in cost reductions from fewer application support requests and $475,000 in cost avoidance through citizen developer enablement. The payback period averages just 6 months."
— Integrate.io, Data Integration Adoption Rates in Enterprises: 45 Statistics Every IT Leader Should Know in 2026 (citing Forrester TEI)
URL: https://www.integrate.io/blog/data-integration-adoption-rates-enterprises/
Date: 2026

### 6.3 iPaaS as Barrier — Fragmentation and Underutilization

[STATISTIC]
"61.3% admit their automation tools are underutilized due to fragmented strategies."
— Enterprise Automation Index 2025, cited in Albato State of Integrations Report 2025
URL: https://albato.com/blog/publications/state-of-integrations-report
Date: 2025

[STATISTIC]
"Only 6% trust AI agents to autonomously handle core end-to-end business processes."
— Workato / Harvard Business Review, 2025 Enterprise Agentic AI Report
URL: https://www.workato.com/full-reports/2025-hbr-enterprise-agentic-ai
Date: 2025

[STATISTIC]
"Nearly half [of organizations] cited searchability of data (48%) and reusability of data (47%) as challenges to AI automation strategies."
— Deloitte, Agentic AI Strategy (Tech Trends 2026)
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

[STATISTIC]
"Only 9% [of organizations have] fully deployed AI use cases (scaling barriers)."
— OneIO Cloud, Integration Solution Trends and Statistics for 2026
URL: https://www.oneio.cloud/blog/state-of-integration-solutions
Date: 2026

---

## Key Takeaways

[FACT]
The average large enterprise manages 897 applications. Only 2% have successfully integrated more than half. Integration failure is the norm, not the exception.
URL: https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
Date: January 2025

[FACT]
35% of enterprise teams have already replaced at least one SaaS product with custom-built software, and 78% plan to build more in 2026, per Retool's survey of 817 builders (late 2025).
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[FACT]
46% of enterprises cite integration with existing systems as their primary barrier to deploying AI agents, per the 2026 State of AI Agents Report.
URL: https://www.arcade.dev/blog/5-takeaways-2026-state-of-ai-agents-claude/
Date: 2026

[FACT]
The iPaaS market is growing at 25.9% CAGR from $15.63 billion in 2025 to a projected $78.28 billion by 2032, signaling that neither the build nor buy path eliminates demand for dedicated integration infrastructure.
URL: https://albato.com/blog/publications/state-of-integrations-report
Date: 2025

[FACT]
MCP reached 97M+ monthly SDK downloads by late 2025 with backing from Anthropic, OpenAI, Google, and Microsoft, emerging as the de facto standard for connecting AI agents to enterprise systems.
URL: https://www.pento.ai/blog/a-year-of-mcp-2025-review
Date: 2025

[FACT]
Gartner predicts over 40% of agentic AI projects will fail by 2027, with legacy system integration cited as the primary driver, indicating that integration complexity is not resolved by adopting agentic approaches alone.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2026

---

## Sources

- MuleSoft 2025 Connectivity Benchmark Report (Sama Integrations summary): https://samaintegrations.com/mulesoft-connectivity-benchmark-report-2025-what-every-integration-professional-must-know-about-the-new-enterprise-reality/
- Salesforce / MuleSoft Connectivity Report Announcement: https://www.salesforce.com/blog/mulesoft-connectivity-benchmark-2025/
- Retool 2026 Build vs. Buy Report (blog): https://retool.com/blog/ai-build-vs-buy-report-2026
- Retool 2026 Build vs. Buy Report (BusinessWire press release): https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
- OneIO Cloud, Integration Solution Trends and Statistics for 2026: https://www.oneio.cloud/blog/state-of-integration-solutions
- Albato, State of Integrations Report 2025: https://albato.com/blog/publications/state-of-integrations-report
- Zapier AI Sprawl Survey (December 2025): https://zapier.com/blog/ai-sprawl-survey/
- Krishna Avva, From SaaS Sprawl to Agent Sprawl (January 2026): https://avva-krishna.com/2026/01/17/from-saas-sprawl-to-agent-sprawl-how-to-architect-the-next-enterprise-era/
- Deloitte, Agentic AI Strategy, Tech Trends 2026: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
- Arcade.dev, 2026 State of AI Agents Report: https://www.arcade.dev/blog/5-takeaways-2026-state-of-ai-agents-claude/
- Workato FY26 Momentum (BusinessWire, February 2026): https://www.businesswire.com/news/home/20260227618624/en/Workato-Reports-Record-Momentum-Defining-the-Future-of-Orchestration-for-the-Agentic-Era
- Workato / HBR, 2025 Enterprise Agentic AI Report: https://www.workato.com/full-reports/2025-hbr-enterprise-agentic-ai
- Pento AI, A Year of MCP: https://www.pento.ai/blog/a-year-of-mcp-2025-review
- Deepak Gupta, MCP Enterprise Adoption Guide 2025: https://guptadeepak.com/the-complete-guide-to-model-context-protocol-mcp-enterprise-adoption-market-trends-and-implementation-strategies/
- CIO.com, Build vs. Buy: A CIO's Journey: https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
- CIO.com, SaaS Isn't Dead, the Market Is Just Becoming More Hybrid: https://www.cio.com/article/4131904/saas-isnt-dead-the-market-is-just-becoming-more-hybrid.html
- Prismatic, 2025 Integration Trends Mid-Year Perspective: https://prismatic.io/blog/integration-trends/
- HPCwire / BigDATAwire, The Connectivity Paradox Holding Back Enterprise Agentic AI (February 2026): https://www.hpcwire.com/bigdatawire/2026/02/10/the-connectivity-paradox-holding-back-enterprise-agentic-ai/
- World Quality Report 2025 (PRNewswire): https://www.prnewswire.com/news-releases/world-quality-report-2025-ai-adoption-surges-in-quality-engineering-but-enterprise-level-scaling-remains-elusive-302614772.html
- Integrate.io, Data Integration Adoption Rates 2026: https://www.integrate.io/blog/data-integration-adoption-rates-enterprises/
- Scale Up Ally, Cost of Integration: https://scaleupally.io/blog/cost-of-integration/
- RecordPoint, Hidden Costs of Maintaining Legacy Systems: https://www.recordpoint.com/blog/maintaining-legacy-systems-costs
- Industry Research Biz, iPaaS Market Report: https://www.industryresearch.biz/market-reports/integration-platform-as-a-service-ipaas-market-104844
- Fortune Business Insights, iPaaS Market: https://www.fortunebusinessinsights.com/integration-platform-as-a-service-ipaas-market-109835
- Wikipedia, Model Context Protocol: https://en.wikipedia.org/wiki/Model_Context_Protocol
