# Build vs. Buy: Enterprise Software Decision Framework

**Research File:** F05 — Build vs. Buy Framework
**Wave:** 1
**Date Compiled:** 2026-03-06
**Audience:** C-Suite / Enterprise Strategy

---

## Executive Summary

For decades the build-vs-buy decision was governed by a relatively stable set of economic rules: buying commercial software was faster and cheaper for commodity functions, while custom development was reserved for activities that created genuine competitive differentiation. Two forces are now compressing the cost side of the "build" option — low-code platforms and, more decisively, agentic coding tools — while simultaneously, the proliferation of SaaS point solutions has driven subscription fatigue and created a parallel pressure to consolidate. Retool's February 2026 survey of 817 enterprise builders found that 35% of enterprises have already replaced at least one SaaS product with a custom-built alternative, and 78% plan to build more in 2026. At the same time, the historical evidence of custom software failure remains severe: McKinsey's large-scale IT project research shows that large projects run 45% over budget and 7% over schedule while delivering 56% less value than predicted. The net effect is not that buying is dead, but that the decision framework itself has been fundamentally restructured: the appropriate unit of analysis is shifting from "application" to "capability," and the viable solution space has expanded from a binary choice to a continuous spectrum of compose, orchestrate, configure, and build.

---

## 1. Classical Build-vs-Buy Decision Frameworks

The build-vs-buy decision has formal roots in the "make-or-buy" analysis that appeared in managerial economics and operations research literature before the age of packaged enterprise software. In its earliest IT form, the question was simply whether to acquire or develop a software system. By the 1990s, as SAP, Oracle, and PeopleSoft offered vertically complete enterprise systems, the dominant advice shifted to "buy where possible."

Gartner formalized the decision space as early as the 2000s, identifying not just two options but a spectrum. A Gartner research document titled "Making a Software Form-Factor Decision: Build, Borrow, Buy, or Rent?" proposed four distinct modes:

[FACT]
"More nuanced options are available beyond a simple binary choice, such as borrow (open-source software [OSS]) or rent (software as a service [SaaS])."
— Gartner, "Making a Software Form-Factor Decision: Build, Borrow, Buy, or Rent?"
URL: https://www.gartner.com/en/documents/1724623
Date: [PRE-2025 — included as foundational framework document]

Forrester Research similarly challenged the binary framing in research led by Senior Analysts Joe Cicman, John Bratincevic, and VP Principal Analyst John R. Rymer:

[QUOTE]
"When clients think about how to meet a business need with software, almost all frame their choices as 'buy vs. build.' We think the better question is, 'What is the best method for delivering a particular software solution within a certain time frame and budget?'"
— Forrester Research, "New Research: Reframing The Buy Vs. Build Choice"
URL: https://go.forrester.com/blogs/new-research-reframing-the-buy-vs-build-choice/
Date: [PRE-2025 — included as foundational framework document]

[FACT]
Forrester identifies "as many as eight distinct approaches" to software delivery, moving beyond a binary build-vs-buy framing.
— Forrester Research, "New Research: Reframing The Buy Vs. Build Choice"
URL: https://go.forrester.com/blogs/new-research-reframing-the-buy-vs-build-choice/
Date: [PRE-2025]

By the mid-2020s, Gartner introduced the "Buy, Build, Blend" paradigm at the Gartner Application Innovation and Business Solutions (AIBS) Summit 2024:

[QUOTE]
"Buy, Build, Blend — an AI strategy that emphasizes composability, adaptability, and intelligence to meet the dynamic demands of modern businesses."
— Denis Torii, VP Analyst, Gartner, as cited by AgilePoint
URL: https://www.agilepoint.com/blog-posts/future-of-enterprise-application
Date: June 25, 2024

[FACT]
Gartner's "Predicts 2024: Composable Modularity Shapes the New Digital Foundation" report predicts that by 2024, 70% of large and medium-sized enterprises will have composability as a key criterion for new application planning.
— Gartner, document 5083331
URL: https://www.gartner.com/en/documents/5083331
Date: 2024

---

## 2. Key Decision Factors: Cost, Time-to-Value, Competitive Advantage, Core vs. Context

### 2a. Cost

The cost dimension of the build decision has historically been the most underestimated. McKinsey's landmark study with the University of Oxford, based on analysis of more than 5,400 large IT projects completed through 2012, established a set of benchmarks that have been frequently cited:

[STATISTIC]
"Large IT projects run 45 percent over budget and 7 percent over time, while delivering 56 percent less value than predicted."
— McKinsey & Company / University of Oxford, "Delivering Large-Scale IT Projects On Time, On Budget, and On Value," Michael Bloch, Sven Blumberg, Jurgen Laartz
URL: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
Date: 2012 [PRE-2025 — cited as primary quantitative benchmark for build failure economics]

[STATISTIC]
A subsequent McKinsey/Oxford analysis of more than 6,000 public- and private-sector IT projects completed between 2001 and 2017 found that IT projects overall "exceeded their budgets by 75 percent, overran their schedules by 46 percent, and generated 39 percent less value than predicted." Only one in 200 projects delivered the intended benefits on time and within budget.
— McKinsey & Company / Oxford Global Projects
URL: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
Date: 2017 [PRE-2025 — foundational benchmark]

[STATISTIC]
"Every additional year spent on the project increasing cost overruns by 15 percent."
— McKinsey & Company / University of Oxford
URL: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
Date: 2012 [PRE-2025]

On the ongoing cost side:

[STATISTIC]
"Maintenance typically represents 20% of the original development cost each year."
— McKinsey & Company (as cited by industry sources)
URL: https://wifitalents.com/custom-software-development-industry-statistics/
Date: 2026

[STATISTIC]
"CIOs spend 70 to 80% of their budget just maintaining existing systems."
— Cited in "Build vs. Buy is Dead, Start Orchestrating: CIO's Strategy in the AI World"
URL: https://blog.sharmavishal.com/2025/10/build-vs-buy-is-dead-start.html
Date: October 2025

### 2b. Time-to-Value

The time-to-market variable has historically favored buying: commercial SaaS solutions could be deployed in weeks while custom development required months to years. The emergence of agentic coding is now directly compressing this advantage, a shift addressed in Section 6.

[STATISTIC]
A McKinsey-aligned finding: "Enterprise technology spending in the United States has been growing by 8 percent per year on average since 2022, while labor productivity has grown by close to 2 percent over the same period."
— McKinsey & Company, "The New Economics of Enterprise Technology in an AI World"
URL: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-new-economics-of-enterprise-technology-in-an-ai-world
Date: 2025

### 2c. Competitive Advantage and Proprietary Software

The most strategically robust argument for building is competitive differentiation. McKinsey research across enterprise software specifically quantified the relationship between proprietary software and financial performance:

[STATISTIC]
"Nearly 70 percent of top economic performers among all companies use proprietary software to differentiate themselves from their competitors, compared with just 50 percent of their peers."
— McKinsey & Company, "Enterprise Software's Growing Reach"
URL: https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/enterprise-softwares-growing-reach
Date: [PRE-2025 — included as primary quantitative finding on build-for-differentiation]

[FACT]
"Top economic performers" were defined as companies whose survey respondents reported increases of at least 15 percent in their organization's revenue and EBIT over the prior three years.
— McKinsey & Company
URL: https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/enterprise-softwares-growing-reach
Date: [PRE-2025]

[STATISTIC]
Companies building strategic digital assets aligned with core business "can achieve 20-30% higher profit margins."
— McKinsey & Company (as cited in CIO.com analysis)
URL: https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
Date: 2025

### 2d. Core vs. Context (Geoffrey Moore Framework)

Geoffrey Moore's core-vs-context framework, introduced in his 2005 book "Dealing with Darwin," has become one of the most cited analytical foundations for the build decision:

[FACT]
Moore's framework defines "Core" as "any activity that creates sustainable differentiation. It is what a company invests its time and resources in that its competitors do not." "Context" is defined as "any activity that does not create differentiation — it brings in money but is not what makes the company unique."
— Geoffrey Moore, "Dealing with Darwin: How Great Companies Innovate at Every Phase of Their Evolution," 2005
URL: https://geoffreyamoore.com/book/dealing-with-darwin/
Date: 2005 [PRE-2025 — included as canonical strategic framework]

[QUOTE]
"Core represents work that differentiates your enterprise, your claim to fame, the stuff that supports growth by creating customer preference for your offerings."
— Geoffrey Moore
URL: https://strategictoolkits.com/strategic-concepts/core-and-context-strategic-framework/
Date: [PRE-2025]

The practical implication for the build-vs-buy decision is direct: activities classified as "core" warrant internal investment and custom development; activities classified as "context" should be outsourced or addressed with commercial software.

Capgemini Engineering incorporated this framework into their CTO Playbook series (2025), noting that "technological advances and market commoditization can shift the boundary between 'Core' and 'Context,' requiring continuous evaluation."

[FACT]
Capgemini's CTO Playbook series identifies five strategic themes (Organic Engineering, Resource Revolution, Hybrid AI, Digital Fabric, Velocity of Impact) aligned to the core-vs-context prioritization model, noting the dynamic nature of the core/context boundary.
— Capgemini Engineering, "The CTO Playbook for Innovation in Engineering — 3: The Core vs Context Model"
URL: https://www.capgemini.com/insights/expert-perspectives/the-cto-playbook-for-innovation-in-engineering-the-core-vs-context-model/
Date: 2025

---

## 3. How the Decision Framework Has Evolved Over the Past Decade

The period from roughly 2010 to 2022 was characterized by a decisive tilt toward "buy." The SaaS revolution — embodied by Salesforce, Workday, ServiceNow, and hundreds of point-solution providers — changed the default calculus:

[FACT]
"The 2000s brought Software-as-a-Service (SaaS), democratizing access to tools like Salesforce and Workday... [by] 2020, many 'buy' options integrate easier and scale better than what you could build."
— Mind Over Machines, "Enterprise Software: Build vs. Buy 2020"
URL: https://www.mindovermachines.com/enterprise-software-build-vs-buy-2020/
Date: 2020 [PRE-2025 — cited for historical context on the buy-shift]

[FACT]
"Companies aren't building their own CRMs or email systems anymore because there is such a wide variety of quality SaaS products readily available."
— Mind Over Machines, "Enterprise Software: Build vs. Buy 2020"
URL: https://www.mindovermachines.com/enterprise-software-build-vs-buy-2020/
Date: 2020 [PRE-2025]

Forrester documented the inflection point, noting:

[FACT]
Two factors changed the calculus: "Low-code platforms have reduced the costs and risks of custom-developing applications" and "Software-as-a-service has reduced the costs and raised the sustainability of customizing packaged solutions."
— Forrester Research, "New Research: Reframing The Buy Vs. Build Choice"
URL: https://go.forrester.com/blogs/new-research-reframing-the-buy-vs-build-choice/
Date: [PRE-2025]

[FACT]
Forrester observed by its research date: "More clients are choosing the 'build' option than in past years."
— Forrester Research, "New Research: Reframing The Buy Vs. Build Choice"
URL: https://go.forrester.com/blogs/new-research-reframing-the-buy-vs-build-choice/
Date: [PRE-2025]

By 2025-2026, the framework had formally evolved past a binary choice. Gartner's "Buy, Build, Blend" framing at the AIBS Summit 2024 signaled institutional acknowledgment that the question was now about composability:

[QUOTE]
"Composable architecture allows enterprises to combine independent software components like building blocks."
— Denis Torii, VP Analyst, Gartner, as cited in "The Future of Enterprise Apps: Buy, Build & Blend"
URL: https://www.agilepoint.com/blog-posts/future-of-enterprise-application
Date: June 25, 2024

The Gartner composable enterprise framework identifies four facets of modern enterprise applications: composable architecture, autonomous orchestration, embedded intelligence (AI), and adaptive experience.

---

## 4. The "Build Trap" — Historical Failures of Custom Software

The term "build trap" was codified by product management practitioner Melissa Perri in her 2019 book "Escaping the Build Trap." While the book focuses on product management discipline rather than the binary build-vs-buy decision, it crystallized a broader failure mode endemic to organizations that build custom software without validated problem-solution fit:

[QUOTE]
"The build trap is when organizations become stuck measuring their success by outputs rather than outcomes."
— Melissa Perri, "Escaping the Build Trap: How Effective Product Management Creates Real Value," 2019
URL: https://www.goodreads.com/work/quotes/66322411-escaping-the-build-trap-how-effective-product-management-creates-real-v
Date: 2019 [PRE-2025 — included as canonical definition]

[QUOTE]
"'Value' becomes the quantity of features that are delivered, and the number of features shipped becomes the primary metric of success."
— Melissa Perri, "Escaping the Build Trap"
URL: https://www.goodreads.com/work/quotes/66322411-escaping-the-build-trap-how-effective-product-management-creates-real-v
Date: 2019 [PRE-2025]

Beyond product management failures, the historical record of large custom enterprise IT projects documents catastrophic financial outcomes. The most frequently cited public-sector failure:

[FACT]
The UK's National Programme for IT (NPfIT), launched in 2002 with an initial budget of approximately £6.2 billion, was dismantled in 2011 after costs ballooned to more than £10 billion. The UK Public Accounts Committee described it as one of the "worst and most expensive contracting fiascos" ever.
— UK Public Accounts Committee; reported by multiple sources including Computer Weekly and Panorama Consulting
URL: https://www.computerweekly.com/opinion/Six-reasons-why-the-NHS-National-Programme-for-IT-failed
Date: [PRE-2025 — canonical case study]

[FACT]
Oregon's Cover Oregon healthcare exchange, attempting to implement Oracle software, spent $300 million without taking a single application through the exchange, leading to dueling lawsuits between the state and Oracle.
— Wikipedia, "List of Failed and Overbudget Custom Software Projects"
URL: https://en.wikipedia.org/wiki/List_of_failed_and_overbudget_custom_software_projects
Date: [PRE-2025]

Aggregate failure statistics reinforce the pattern:

[STATISTIC]
The Standish Group CHAOS Report (2020, the most recent published data): only 31% of projects are successful; 50% are "challenged" (fail over time); 19% fail completely.
— The Standish Group CHAOS Report, 2020
URL: https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes
Date: 2020 [PRE-2025 — most recent published version]

[STATISTIC]
"Large IT projects run about 45% over budget and 7% over time." Projects exceeding $10 million are more than ten times more likely to be canceled than those under $1 million.
— McKinsey / Oxford study as cited in IT project management literature
URL: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
Date: 2012 [PRE-2025]

[STATISTIC]
Gartner predicts that at least 30% of generative AI projects will be abandoned after proof of concept by the end of 2025, "due to poor data quality, inadequate risk controls, escalating costs or unclear business value."
— Gartner press release, July 29, 2024
URL: https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
Date: July 29, 2024

[STATISTIC]
McKinsey research reveals that "17% of large-scale digital transformations encounter such severe challenges that they pose an existential threat to the companies undertaking them."
— McKinsey & Company
URL: https://www.hyland.com/en/resources/articles/seventy-percent-not-successful
Date: 2024

Harvard Business Review has noted a structural cognitive bias in the build decision:

[FACT]
Organizations "often overestimate their uniqueness, leading to unnecessary custom development."
— Harvard Business Review, November 2021 (as cited in CIO.com analysis)
URL: https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
Date: 2025

---

## 5. When Building Makes Strategic Sense

Despite the failure statistics, the evidence for building in strategically appropriate contexts is robust.

### 5a. Competitive Differentiation

[STATISTIC]
"Organizations with proprietary core technology see about 2x stronger revenue growth than those relying only on off-the-shelf platforms."
— As cited in enterprise software build-vs-buy analysis
URL: https://appinventiv.com/blog/build-vs-buy-software/
Date: 2026

[STATISTIC]
"Nearly 70 percent of top economic performers... use proprietary software to differentiate themselves from their competitors, compared with just 50 percent of their peers."
— McKinsey & Company, "Enterprise Software's Growing Reach"
URL: https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/enterprise-softwares-growing-reach
Date: [PRE-2025]

### 5b. Unique Workflows Not Addressable by Commercial Software

[FACT]
"Niche sectors often have unique workflows that commercial solutions do not fully support, requiring tailored software. Enterprise businesses often operate within complex environments where software needs to interact with a web of internal systems and workflows, and off-the-shelf tools may not offer the depth or flexibility required."
— HatchWorks, "Build vs Buy Software: The Definitive Framework for 2025"
URL: https://hatchworks.com/blog/software-development/build-vs-buy/
Date: 2025

### 5c. Data and Privacy Constraints

[QUOTE]
"Do we lean on off-the-shelf solutions, or explore building our own using open-source models like Llama? Privacy and data considerations are paramount."
— Matt Paige, VP of Marketing and Strategy, HatchWorks
URL: https://hatchworks.com/blog/software-development/build-vs-buy/
Date: 2025

### 5d. High-Stakes Precision Requirements

[FACT]
In-house development typically focuses on high-stakes areas like "risk assessment, fraud prevention, and compliance where precision, security, and customization are essential," while for standardized applications such as customer support automation or reporting tools, pre-built solutions are often adopted.
— Gartner Peer Community discussion, as summarized
URL: https://www.gartner.com/peer-community/post/how-building-enterprise-ai-capabilities-factors-driving-build-versus-buy-versus-partner-decisions
Date: 2024

### 5e. The McKinsey Prescription for AI-Era Building

[FACT]
McKinsey's guidance on the AI-era build decision: "A more resilient approach is to buy standardized capabilities... and reserve custom development for the select areas where domain-specific logic or proprietary workflows create real competitive advantage."
— McKinsey & Company, "Bridging the Great AI Agent and ERP Divide to Unlock Value at Scale"
URL: https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/bridging-the-great-ai-agent-and-erp-divide-to-unlock-value-at-scale
Date: 2025

[FACT]
McKinsey notes that "unlike the traditional software as a service (SaaS) world, AI requires a continuous, deliberate reassessment of what to create and what to consume."
— McKinsey & Company, "Bridging the Great AI Agent and ERP Divide"
URL: https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/bridging-the-great-ai-agent-and-erp-divide-to-unlock-value-at-scale
Date: 2025

### 5f. Shadow IT as Revealed Preference

The scale of unsanctioned building reveals latent demand for custom tooling that commercial SaaS does not satisfy:

[STATISTIC]
Retool's 2026 Build vs. Buy Shift Report (n=817 enterprise builders, surveyed late 2025): "60% of builders across all seniority levels built outside IT oversight in the past year"; 25% report doing so frequently; 64% of shadow IT builders were senior managers and above.
— Retool, "The 2026 Build vs. Buy Shift Report," Kelsey McKeon
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
Top reasons for shadow IT builds: 31% cite speed advantage; 25% cite unmet needs with existing SaaS; 18% say IT process too slow; 10% report official tools don't integrate.
— Retool, "The 2026 Build vs. Buy Shift Report"
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

---

## 6. How Agentic Coding Changes the Variables in the Framework

Agentic coding — AI systems capable of autonomously writing, testing, debugging, and deploying code — is the most significant structural variable introduced into the build-vs-buy decision in decades. It directly attacks the two historical advantages of buying: lower cost and faster deployment.

### 6a. Development Cost Compression

[STATISTIC]
"Vibe coding is cutting the cost of application development by anywhere from 70% to 95%, opening development to subject matter experts."
— Agentic coding industry analysis, 2026
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
Agentic coding is claimed to cut development costs by up to 90%; more conservative analysis suggests "a 50% reduction in human engineering effort, which becomes a 10% savings on total expenditures."
— Belitsoft, "Agentic AI Coding: What Still Remains Expensive Amid a 90% Drop in Costs"
URL: https://belitsoft.com/agentic-ai-coding
Date: 2026

[STATISTIC]
"AI-centric organizations are achieving 20% to 40% reductions in operating costs and 12–14 point increases in EBITDA margins, driven by automation, faster cycle times and more efficient allocation of talent and infrastructure."
— McKinsey, as cited in CIO article by Lalit Wadhwa
URL: https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html
Date: February 20, 2026

### 6b. Velocity and the Fundable Idea Threshold

[QUOTE]
"Work that once took weeks can be done in days, which shifts which ideas get funded and built."
— Summary of Anthropic 2026 Agentic Coding Trends Report (Trend 6), as cited by Tessl.io
URL: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
Date: 2026

[QUOTE]
"Agents increasingly handle writing, testing, debugging, and documentation, while engineers focus on architecture and decision-making. Onboarding time to new codebases drops sharply."
— Summary of Anthropic 2026 Agentic Coding Trends Report (Trend 1)
URL: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
Date: 2026

### 6c. Democratization of Building

[STATISTIC]
Retool (n=817 enterprise builders): 51% have shipped production software using AI; 72% use AI to write discrete code snippets integrated into larger projects; 31% are "prompting their way to complete applications."
— Retool, "The 2026 Build vs. Buy Shift Report"
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
93% of respondents in the Retool survey use LLMs to code, build, or automate. ChatGPT: 70%; Gemini: 56%; Claude: 53%.
— Retool, "The 2026 Build vs. Buy Shift Report"
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### 6d. Measured SaaS Replacement

[STATISTIC]
35% of enterprises in the Retool survey have already replaced at least one SaaS tool with a custom-built alternative; 78% plan to build more custom tools in 2026.
— David Hsu, CEO and Founder, Retool, press release
URL: https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
Date: February 17, 2026

[STATISTIC]
SaaS categories under the highest replacement pressure: workflow automations (35%), internal admin tools (33%), BI tools (29%), CRMs and form builders (25%), project management (23%), customer support (21%).
— Retool, "The 2026 Build vs. Buy Shift Report"
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[QUOTE]
"The markets are finally catching up to something builders have always known: that enterprise AppGen has become a threat to traditional SaaS."
— David Hsu, CEO and Founder, Retool
URL: https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
Date: February 17, 2026

### 6e. The Klarna Case — Build in Production

Klarna is the most prominent enterprise example of displacing SaaS with a proprietary AI-powered alternative:

[FACT]
Klarna replaced Salesforce's flagship CRM product with a homegrown AI system based on OpenAI's ChatGPT. Bloomberg reported savings of approximately $2 million annually from the Salesforce replacement specifically.
— TipRanks / Bloomberg, as cited
URL: https://www.tipranks.com/news/the-fly/klarna-saved-2m-after-replacing-salesforce-with-in-house-tools-bloomberg-says-thefly
Date: 2024/2025

[QUOTE]
"We did not replace SaaS with an LLM, and storing CRM data in an LLM would have its limitations. But we developed an internal tech stack, using Neo4j and other things, to start bringing data=knowledge together."
— Sebastian Siemiatkowski, CEO, Klarna (correcting media coverage)
URL: https://diginomica.com/those-shutting-down-salesforce-and-workday-rumors-klarna-no-we-didnt-replace-saas-llm-admits-ceo
Date: 2025

[QUOTE]
"I don't think it is the end of Salesforce; might be the opposite."
— Sebastian Siemiatkowski, CEO, Klarna
URL: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/
Date: March 4, 2025

### 6f. Governance and Risk Introduced by Agentic Building

[STATISTIC]
"AI-driven coding reduces time to pull request by up to 58%, but AI-generated pull requests wait 4.6x longer in review without governance."
— Industry analysis of agentic coding impact
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
"AI-generated code introduces 15–18% more security vulnerabilities, increasing risk as autonomy expands."
— Industry analysis of agentic coding impact
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
"Nearly 90% of enterprise teams now use AI in the development lifecycle."
— Industry analysis
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[QUOTE]
"There's no way you can go live with a vibe-coded solution. It might work for demos, but we build enterprise-grade technology that has to scale across 30 countries."
— Pierre Yves Calloc'h, Builder, Pernod Ricard
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### 6g. Gartner Forecast on Agentic Penetration

[STATISTIC]
"Gartner forecasts that by the end of 2026, 40% of enterprise applications will feature task-specific AI agents, up from less than 5% in 2025."
— As cited in 2026 agentic coding industry analysis
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
"By 2030, 35% of point-product SaaS tools will be replaced by AI agents or absorbed within larger agent ecosystems."
— Deloitte, "SaaS Meets AI Agents: Transforming Budgets, Customer Experience, and Workforce Dynamics"
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

[STATISTIC]
"By 2030, at least 40% of enterprise SaaS spend will shift toward usage-, agent-, or outcome-based pricing."
— Deloitte, "SaaS Meets AI Agents"
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

### 6h. Time Horizon for Displacement

[FACT]
Deloitte analysis notes "at least 5+ years required before enterprise applications [are] substantially replaced by agents, despite rapid development pace."
— Deloitte, "SaaS Meets AI Agents"
URL: https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
Date: 2026

---

## Comparative Summary Table: Build vs. Buy Decision Variables, Then vs. Now

| Decision Variable | Pre-2020 Assessment | 2025-2026 Assessment |
|---|---|---|
| Build cost (initial) | High; 6-18+ month cycles | Compressed by 50-90% with agentic tools |
| Build cost (maintenance) | 20% of original cost per year | Reduced by AI-assisted maintenance, but governance overhead rising |
| Time to deploy | Months to years for custom | Days to weeks for targeted capabilities |
| Buy time to deploy | Weeks | Unchanged; still the baseline |
| Competitive differentiation | Strong argument for building core | Unchanged; proprietary logic still differentiates |
| Failure rate (large custom) | 45% over budget; 17% existential risk | Still elevated; GenAI POC abandonment rate at 30%+ |
| Framework model | Binary: build or buy | Spectrum: build, borrow, buy, blend, orchestrate |
| Shadow IT prevalence | Significant; IT governance challenge | 60% of enterprises built outside IT oversight in past year |
| SaaS replacement by custom | Rare; mostly greenfield build | 35% of enterprises have replaced at least one SaaS tool |
| Decision reassessment frequency | Project lifecycle (multi-year) | Continuous; AI changes the calculus faster than project cycles |

---

## Key Takeaways

- The historical case against building is anchored in documented cost and schedule overruns: McKinsey/Oxford analysis across 5,400+ large IT projects found a consistent pattern of 45% budget overrun, 7% schedule overrun, and 56% value shortfall. This baseline has not been eliminated by AI tools, but the cost side is being structurally compressed.

- The foundational intellectual framework for the build decision — Geoffrey Moore's core-vs-context model — remains the most cited strategic tool, and its central logic (invest internally in what differentiates you; buy what does not) is intact. McKinsey data shows 70% of top economic performers use proprietary software vs. 50% of peers.

- The binary "build or buy" formulation has been formally superseded. Both Gartner (Buy-Build-Blend, AIBS Summit 2024) and Forrester (eight distinct delivery modes) now articulate a spectrum that includes composable architecture, orchestration, open-source borrowing, low-code configuration, and full custom development.

- Agentic coding is the most consequential new variable since the SaaS revolution. Retool's 2026 survey (n=817) documents that 35% of enterprises have already replaced at least one SaaS tool with custom-built software; 78% plan to build more. The threshold cost for building has crossed below the threshold cost for buying for a growing class of commodity-adjacent internal tooling.

- Governance risk from AI-generated code — 15-18% higher security vulnerability rates, 4.6x longer review cycles — is the primary structural constraint on full build-side conversion, and enterprise-scale rollouts (like Pernod Ricard's 30-country deployment) require engineering discipline that "vibe coding" alone does not provide.

---

## Sources

1. Gartner, "Making a Software Form-Factor Decision: Build, Borrow, Buy, or Rent?" — https://www.gartner.com/en/documents/1724623
2. Gartner, "Decision Point for the Build vs. Buy Software Sourcing Decision" — https://www.gartner.com/en/documents/2071619
3. Gartner, "Peer Connect Perspectives: Deciding Between Building or Buying Enterprise Software" — https://www.gartner.com/en/documents/3957047
4. Gartner, "Predicts 2024: Composable Modularity Shapes the New Digital Foundation" — https://www.gartner.com/en/documents/5083331
5. Gartner press release, "Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025" — https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
6. Gartner, "Deploying AI: Should Your Organization Build, Buy or Blend?" — https://www.gartner.com/en/articles/deploying-ai
7. Gartner Peer Community, "How are you building enterprise AI capabilities? Build-vs-buy-vs-partner decisions" — https://www.gartner.com/peer-community/post/how-building-enterprise-ai-capabilities-factors-driving-build-versus-buy-versus-partner-decisions
8. Forrester Research, "New Research: Reframing The Buy Vs. Build Choice" (Cicman, Bratincevic, Rymer) — https://go.forrester.com/blogs/new-research-reframing-the-buy-vs-build-choice/
9. McKinsey & Company, "Delivering Large-Scale IT Projects On Time, On Budget, and On Value" (Bloch, Blumberg, Laartz, 2012) — https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
10. McKinsey & Company, "Enterprise Software's Growing Reach" — https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/enterprise-softwares-growing-reach
11. McKinsey & Company, "The New Economics of Enterprise Technology in an AI World" — https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-new-economics-of-enterprise-technology-in-an-ai-world
12. McKinsey & Company, "Bridging the Great AI Agent and ERP Divide to Unlock Value at Scale" — https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/bridging-the-great-ai-agent-and-erp-divide-to-unlock-value-at-scale
13. McKinsey & Company, "The State of AI in 2025: Agents, Innovation, and Transformation" — https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
14. Deloitte, "SaaS Meets AI Agents: Transforming Budgets, Customer Experience, and Workforce Dynamics" (TMT Predictions 2026) — https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/saas-ai-agents.html
15. Retool, "The 2026 Build vs. Buy Shift Report" (Kelsey McKeon, February 17, 2026) — https://retool.com/blog/ai-build-vs-buy-report-2026
16. Retool / BusinessWire press release, "Retool's 2026 Build vs. Buy Report Reveals 35% of Enterprises Have Already Replaced SaaS With Custom Software" — https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
17. Geoffrey Moore, "Dealing with Darwin: How Great Companies Innovate at Every Phase of Their Evolution," 2005 — https://geoffreyamoore.com/book/dealing-with-darwin/
18. Capgemini Engineering, "The CTO Playbook for Innovation in Engineering — 3: The Core vs Context Model" — https://www.capgemini.com/insights/expert-perspectives/the-cto-playbook-for-innovation-in-engineering-the-core-vs-context-model/
19. Melissa Perri, "Escaping the Build Trap: How Effective Product Management Creates Real Value," O'Reilly, 2019 — https://www.oreilly.com/library/view/escaping-the-build/9781491973783/
20. Melissa Perri quotes (Goodreads) — https://www.goodreads.com/work/quotes/66322411-escaping-the-build-trap-how-effective-product-management-creates-real-v
21. Standish Group CHAOS Report, 2020 (via OpenCommons) — https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes
22. Wikipedia, "List of Failed and Overbudget Custom Software Projects" — https://en.wikipedia.org/wiki/List_of_failed_and_overbudget_custom_software_projects
23. Computer Weekly, "Six Reasons Why the NHS National Programme For IT Failed" — https://www.computerweekly.com/opinion/Six-reasons-why-the-NHS-National-Programme-for-IT-failed
24. CIO.com, "Build vs. Buy: A CIO's Journey Through the Software Decision Maze" — https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
25. CIO.com, "How Agentic AI Will Reshape Engineering Workflows in 2026" (Lalit Wadhwa, February 20, 2026) — https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html
26. AgilePoint, "The Future of Enterprise Apps: Buy, Build & Blend" — https://www.agilepoint.com/blog-posts/future-of-enterprise-application
27. HatchWorks, "Build vs Buy Software: The Definitive Framework for 2025" — https://hatchworks.com/blog/software-development/build-vs-buy/
28. AppInventiv, "Build vs Buy Software in 2026: Cost, ROI and Decision Guide" — https://appinventiv.com/blog/build-vs-buy-software/
29. TechCrunch, "Klarna CEO Doubts That Other Companies Will Replace Salesforce with AI" — https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/
30. Diginomica, "Those shutting down Salesforce and Workday rumors from Klarna" — https://diginomica.com/those-shutting-down-salesforce-and-workday-rumors-klarna-no-we-didnt-replace-saas-llm-admits-ceo
31. TipRanks / Bloomberg, "Klarna saved $2M after replacing Salesforce with in-house tools" — https://www.tipranks.com/news/the-fly/klarna-saved-2m-after-replacing-salesforce-with-in-house-tools-bloomberg-says-thefly
32. Tessl.io, "8 Trends Shaping Software Engineering in 2026 — Anthropic's Agentic Coding Report" — https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
33. Times of AI, "Agentic Coding in 2026: AI's Impact on Software Development" — https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
34. Belitsoft, "Agentic AI Coding: What Still Remains Expensive Amid a 90% Drop in Costs" — https://belitsoft.com/agentic-ai-coding
35. Mind Over Machines, "Enterprise Software: Build vs. Buy 2020" — https://www.mindovermachines.com/enterprise-software-build-vs-buy-2020/
36. MarkTechPost, "Build vs Buy for Enterprise AI (2025): A U.S. Market Decision Framework" — https://www.marktechpost.com/2025/08/24/build-vs-buy-for-enterprise-ai-2025-a-u-s-market-decision-framework-for-vps-of-ai-product/
37. Hyland, "70 Percent of IT Implementations Aren't Successful" — https://www.hyland.com/en/resources/articles/seventy-percent-not-successful
38. StrategicToolkits, "What Is The Concept of Core And Context?" — https://strategictoolkits.com/strategic-concepts/core-and-context-strategic-framework/
39. FullScale.io, "Build vs. Buy Software Development: A Comprehensive Decision Framework for 2025" — https://fullscale.io/blog/build-vs-buy-software-development-decision-guide/
