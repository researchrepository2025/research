# D03: Developer Tool Ecosystem — Enabling or Constraining Enterprise Custom Software Development

**Research Question:** How is the developer tool ecosystem evolving to enable or constrain enterprise custom software development?
**Wave:** 6 — Market Signals
**Date Compiled:** March 2026

---

## Executive Summary

The enterprise developer tool ecosystem has undergone a structural shift in 2025–2026: AI-powered IDEs and coding assistants have moved from experimental to standard infrastructure, with GitHub Copilot deployed at 90% of Fortune 100 companies and Cursor adopted by 64% of Fortune 500 firms. Autonomous coding agents such as Devin have crossed from pilot to production at major financial institutions, with Goldman Sachs deploying hundreds of AI software engineers alongside its 12,000 human developers. The tooling ecosystem unambiguously favors building custom software in more scenarios than at any prior point — Retool's 2026 survey found 35% of enterprises have already replaced at least one SaaS product with a custom build, and 78% plan to build more. However, the same ecosystem introduces material constraints: AI-generated code carries elevated security debt (45% of AI code contains flaws in some studies), core developers absorb a 19% productivity drop from reviewing AI output, and Gartner warns that over 40% of agentic AI projects will be canceled by 2027 due to unclear business value or inadequate risk controls.

---

## Section 1: AI-Powered IDEs — Cursor, Windsurf, and the Agentic IDE Category

### 1.1 Cursor Enterprise Penetration

[STATISTIC]
"64% of Fortune 500 companies use Cursor"
— Cursor Enterprise page
URL: https://cursor.com/enterprise
Date: 2026

[STATISTIC]
"50,000+ enterprises choose to build with Cursor"
— Cursor Enterprise page
URL: https://cursor.com/enterprise
Date: 2026

[STATISTIC]
"100M+ lines of enterprise code written daily with Cursor"
— Cursor Enterprise page
URL: https://cursor.com/enterprise
Date: 2026

[STATISTIC]
"93% of engineers prefer Cursor in head-to-head evaluations"; "39% more PRs merged after Cursor agent became default (University of Chicago study)"
— Cursor Enterprise page
URL: https://cursor.com/enterprise
Date: 2026

[FACT]
Cursor's ARR reached $1 billion by late 2025, and Anysphere (Cursor's parent) reached a $29.3 billion valuation.
— Stocktwits/Market Report
URL: https://stocktwits.com/news-articles/markets/equity/this-ai-coding-startup-backed-by-nvidia-google-is-now-valued-at-29-b-revenue-tops-1-b/cLP9JPMREEc
Date: 2025

[QUOTE]
"Cursor is used in pretty much all product areas and in all aspects of software development. Teams are using Cursor for writing code, code reviews, generating test cases, and QA. Our full SDLC is accelerated by Cursor."
— Wei Luo, VP of Engineering, NVIDIA
URL: https://cursor.com/blog/nvidia
Date: 2025

[QUOTE]
"Before Cursor, NVIDIA had other AI coding tools, both internally built and other external vendors. But after adopting Cursor is when we really started seeing significant increases in development velocity."
— Wei Luo, VP of Engineering, NVIDIA
URL: https://cursor.com/blog/nvidia
Date: 2025

[QUOTE]
"We have built a lot of custom rules in Cursor to fully automate entire workflows. That has unlocked Cursor's true potential."
— Fabian Theuring, Senior Software Architect, NVIDIA
URL: https://cursor.com/blog/nvidia
Date: 2025

[QUOTE]
"Cursor quickly grew from hundreds to thousands of enthusiastic employees. Significant economic outcomes result from making R&D more efficient."
— Patrick Collison, CEO, Stripe
URL: https://cursor.com/enterprise
Date: 2025

[QUOTE]
"Engineers refactor, upgrade, or build codebases in days instead of months."
— Brian Armstrong, CEO, Coinbase
URL: https://cursor.com/enterprise
Date: 2025

[QUOTE]
"Adoption grew from 150 to over 500 engineers (~60% of organization) in weeks."
— Albert Strasheim, CTO, Rippling
URL: https://cursor.com/enterprise
Date: 2025

[QUOTE]
"All 40,000 engineers now have AI assistance, with incredible productivity gains."
— Jensen Huang, President & CEO, NVIDIA
URL: https://cursor.com/enterprise
Date: 2025

[FACT]
NVIDIA deployed Cursor to over 30,000 active users, driving a 3x increase in committed code. Bug rates remained flat despite the tripled output.
— Tom's Hardware
URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-now-produces-three-times-as-much-code-as-before-ai-specialized-version-of-cursor-is-being-used-by-over-30-000-nvidia-engineers-internally
Date: 2025

[FACT]
Cursor enterprise security certifications include SOC 2 Type 2, annual penetration testing, GDPR and CCPA compliance, AES-256 encryption at rest, TLS 1.2+ in transit, and zero data retention (no training on customer data). Enterprise features include SAML-based SSO, SCIM user provisioning, and centralized model access controls.
— Cursor Enterprise page
URL: https://cursor.com/enterprise
Date: 2026

Named enterprise customers deploying Cursor as of 2026: Samsung, OpenAI, NVIDIA, Datadog, Adobe, Stripe, PwC, Figma, Carlyle, Sanofi, Deloitte, British Airways, Hilton, Fox, BP, Budweiser, Coinbase, Rippling, Monday.com, Sentry, JetBrains, Upwork.
— Cursor Enterprise page
URL: https://cursor.com/enterprise
Date: 2026

### 1.2 Windsurf

[FACT]
Windsurf's enterprise annual recurring revenue crossed $30 million in early 2025, reflecting 500% year-over-year growth and a 100% customer retention rate. By July 2025, Windsurf had grown to $82 million ARR with over 350 enterprise clients including JPMorgan Chase and Dell.
— Windsurf enterprise coverage / Elephas
URL: https://elephas.app/blog/windsurf-ai-3-billion-collapse-72-hours
Date: 2025

[FACT]
Windsurf achieved FedRAMP High certification — the most stringent federal security authorization level, required for systems processing high-impact government data. Windsurf Enterprise is listed on the AWS Marketplace for FedRAMP-certified deployment.
— AWS Marketplace
URL: https://aws.amazon.com/marketplace/pp/prodview-x4iqsqorbfaj4
Date: 2025

[FACT]
In April 2025, OpenAI announced a $3 billion acquisition of Windsurf. The deal collapsed due to Microsoft IP rights complications. Cognition (makers of Devin) subsequently acquired Windsurf's IP, product, brand, and approximately 210 employees for $250 million.
— DevOps.com
URL: https://devops.com/openai-acquires-windsurf-for-3-billion-2/
Date: 2025

### 1.3 Market Context

[FACT]
The era of the "Copilot" — AI acting as sophisticated autocomplete — is being eclipsed by "Agentic IDEs" functioning as autonomous engineering partners capable of managing entire repositories, refactoring complex architectures, and building production-ready features from simple natural language descriptions.
— Financial Content / Token Ring analysis
URL: https://markets.financialcontent.com/wss/article/tokenring-2026-1-26-the-rise-of-the-agentic-ide-how-cursor-and-windsurf-are-automating-the-art-of-software-engineering
Date: January 2026

---

## Section 2: AI Coding Assistants — GitHub Copilot and Amazon Q Enterprise Penetration

### 2.1 GitHub Copilot

[STATISTIC]
GitHub Copilot surpassed 20 million all-time users in July 2025, up from 15 million in April 2025, adding 5 million users in three months.
— TechCrunch
URL: https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/
Date: July 2025

[STATISTIC]
"GitHub Copilot is used by 90% of the Fortune 100." Enterprise customer growth reached 75% quarter-over-quarter in Q2 2025. More than 50,000 organizations currently use Copilot.
— Second Talent / MLQ.ai
URL: https://mlq.ai/news/github-copilot-surpasses-20-million-all-time-users-accelerates-enterprise-adoption/
Date: 2025

[STATISTIC]
GitHub Copilot holds approximately 42% market share among paid AI coding tools. The AI coding tools market reached $7.37 billion in 2025.
— Faros AI / Visual Studio Magazine
URL: https://www.faros.ai/blog/github-copilot-vs-amazon-q-enterprise-bakeoff
Date: 2025

[STATISTIC]
"GitHub Copilot generates an average of 46% of code written by users, with Java developers reaching 61%." Developers using Copilot complete tasks 55% faster (research involving 4,800 developers). Developers retain 88% of accepted code in final submissions.
— MLQ.ai/GitHub Copilot statistics
URL: https://mlq.ai/news/github-copilot-surpasses-20-million-all-time-users-accelerates-enterprise-adoption/
Date: 2025

[STATISTIC]
In a direct enterprise pilot involving 430 engineers, GitHub Copilot delivered 2x adoption rate, 10 hours/week in time savings versus 7 hours/week for Amazon Q, and 12% higher satisfaction.
— Faros AI enterprise bakeoff
URL: https://www.faros.ai/blog/github-copilot-vs-amazon-q-enterprise-bakeoff
Date: 2025

[FACT]
Paid Copilot subscriber base reached 1.3 million users, with Microsoft reporting 30% quarter-over-quarter growth. Satya Nadella stated GitHub Copilot was "a larger business than all of GitHub was when Microsoft acquired it in 2018."
— Quantumrun Foresight / About Chromebooks statistics
URL: https://www.quantumrun.com/consulting/github-copilot-statistics/
Date: 2026

### 2.2 Amazon Q Developer

[STATISTIC]
Amazon Q Developer holds approximately 11% market share among paid AI coding tools, behind GitHub Copilot (42%) and Cursor (18%).
— Faros AI / Visual Studio Magazine
URL: https://visualstudiomagazine.com/articles/2025/07/09/github-copilot-swamps-gemini-code-assist-amazon-q-among-engineers-ai-coding-survey-says.aspx
Date: July 2025

[FACT]
At Epsilon, Amazon Q Developer adoption surged 12x during 2025, representing one of the highest reported single-company adoption rates for the platform.
— AWS / CloudThat
URL: https://www.cloudthat.com/resources/blog/aws-reinvent-2025-announces-amazon-q-developer-transforms-cloud-development
Date: 2025

[FACT]
Amazon Q Developer was positioned at AWS re:Invent 2025 as a generative AI-powered assistant designed to "enhance developer productivity, simplify cloud operations, and accelerate modern software delivery." PwC has formalized a partnership to deploy Amazon Q Developer for enterprise legacy system modernization.
— PwC / AWS
URL: https://www.pwc.com/us/en/technology/alliances/library/amazon-q-developer.html
Date: 2025

---

## Section 3: Autonomous Coding Agents — Devin, Factory, and Category Adoption

### 3.1 Devin (Cognition AI) — Metrics and Enterprise Deployments

[STATISTIC]
Devin's ARR grew from $1 million in September 2024 to $73 million in June 2025. Following Cognition's acquisition of Windsurf, combined ARR reached $155 million in July 2025.
— Sacra / TechCrunch
URL: https://techcrunch.com/2025/09/08/cognition-ai-defies-turbulence-with-a-400m-raise-at-10-2b-valuation/
Date: September 2025

[STATISTIC]
Devin's PR merge rate improved from 34% to 67% in 2025. Problem-solving speed improved 4x. Resource efficiency improved 2x. Vulnerability resolution time: 1.5 minutes per issue versus 30 minutes for human engineers (20x faster).
— Cognition AI / Devin 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[STATISTIC]
Devin completed proprietary ETL file migrations in 3–4 hours versus 30–40 hours for human engineers (10x improvement). Java version migration: 14x faster than human engineers.
— Cognition AI / Devin 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[FACT]
Named enterprise customers using Devin as of 2025: Goldman Sachs, Santander, Nubank, Citi, EightSleep, Litera. Devin has merged hundreds of thousands of PRs across thousands of companies over 18 months.
— Cognition AI / X (Twitter)
URL: https://x.com/cognition/status/1991218551655657748
Date: 2025

[FACT]
Goldman Sachs piloted Devin alongside its 12,000 human developers in July 2025, described as "the first major bank to use Devin" according to Cognition. The deployment initially involved hundreds of Devin instances, with plans to scale to thousands depending on use cases.
— CNBC
URL: https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html
Date: July 2025

[QUOTE]
Goldman Sachs CIO Marco Argenti described the initiative as a "hybrid workforce" with the goal of achieving 20% efficiency gains — equivalent to the output of 14,400 developers from 12,000 people.
— CNBC / IBM Think
URL: https://www.ibm.com/think/news/goldman-sachs-first-ai-employee-devin
Date: July 2025

[FACT]
Devin 2.0 launched in April 2025 with price reduced from $500/month to $20/month (96% reduction) and introduced multi-agent capabilities allowing parallel instances.
— Cognition / Digital Applied
URL: https://www.digitalapplied.com/blog/devin-ai-autonomous-coding-complete-guide
Date: April 2025

[FACT]
Litera deployed Devin for QA: test coverage increased 40%, regression cycles ran 93% faster. EightSleep ships 3x as many data features and investigations with Devin. A large bank used Devin to generate documentation across 400,000+ repositories.
— Cognition AI / Devin 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

### 3.2 Devin as Internal Infrastructure Example

[FACT]
"Devin now produces 25% of Cognition's own code." This represents Cognition using Devin for its own software development — cited as evidence of autonomous agent viability for production codebases.
— Financial Content / Token Ring
URL: https://markets.financialcontent.com/wral/article/tokenring-2025-12-30-the-worlds-first-autonomous-ai-software-engineer-devin-now-produces-25-of-cognitions-code
Date: December 2025

---

## Section 4: DevOps and Deployment Tooling for AI-Generated Applications

### 4.1 Market Scale and Adoption Rates

[STATISTIC]
The DevOps market reached $14.95 billion in 2025, with a CAGR of 25.70% projected, forecast to reach $37.33 billion by 2029.
— Softjourn
URL: https://softjourn.com/insights/how-ai-is-transforming-devops
Date: 2026

[STATISTIC]
By end of 2025, AI coding assistants reached a 90% adoption rate across enterprises. 53% of organizations are deploying code at least weekly; 17% do so daily.
— Computer Weekly / DevOps.com
URL: https://www.computerweekly.com/news/366639364/How-AI-code-generation-is-pushing-DevSecOps-to-machine-speed
Date: 2025

### 4.2 AI-Native DevOps Architecture

[FACT]
AI code generation is transforming CI/CD pipeline architecture. Development organizations now build continuous integration and deployment pipelines that generate code at scale and rapidly push it into production — a shift described as moving "DevSecOps to machine speed."
— Computer Weekly
URL: https://www.computerweekly.com/news/366639364/How-AI-code-generation-is-pushing-DevSecOps-to-machine-speed
Date: 2025

[FACT]
Opsera's 2025 report on AI-transformed software delivery documents that "agentic AI" deployment patterns — where agents write code, QA agents catch mistakes, and compliance agents validate — are creating automation chains that bypass traditional human review gates at scale.
— Opsera / PR Newswire
URL: https://www.prnewswire.com/news-releases/new-opsera-report-reveals-how-ai-is-transforming-software-delivery-and-driving-business-outcomes-302673996.html
Date: 2025

### 4.3 Governance Gaps

[STATISTIC]
37% of organizations surveyed by Retool lack any AI productivity metrics despite deploying AI tools in production workflows.
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

[STATISTIC]
75% of surveyed builders work under AI directives from management. Only 44% test thoroughly before deployment. Only 8% use AI-generated code without changes.
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

[FACT]
Forrester predicts that by 2026, "observability as code and governance as code will be adopted by 80% of development teams" — identifying automated governance instrumentation as a mandatory response to AI-generated code at scale.
— Forrester 2026 Predictions / SD Times
URL: https://sdtimes.com/softwaredev/forrester-shares-its-predictions-for-how-ai-will-continue-to-shape-software-development-in-2026/
Date: 2025

---

## Section 5: Testing and Quality Assurance for AI-Generated Code

### 5.1 Scale of the QA Challenge

[STATISTIC]
"46% of all code written by active Copilot users is generated by AI."
— CleanAim / Copilot usage data
URL: https://cleanaim.com/resources/silent-wiring/46-percent-ai-generated-code-quality-challenge/
Date: 2025

[STATISTIC]
AI-generated code was introducing more than 10,000 new security findings per month across repositories in one study — a 10-fold spike in six months.
— Checkmarx 2025 CISO Guide
URL: https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/
Date: 2025

[STATISTIC]
Research reveals that 45% of AI-generated code contains security flaws.
— CleanAim / QA challenge analysis
URL: https://cleanaim.com/resources/silent-wiring/46-percent-ai-generated-code-quality-challenge/
Date: 2025

### 5.2 Academic Research: The Technical Debt Paradox

[FACT]
Academic paper: "AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden"
Authors: Feiyang Xu, Poonacha K. Medappa, Murat M. Tunc, Martijn Vroegindeweij, Jan C. Fransoo
— arXiv preprint 2510.10165
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[STATISTIC]
From the arXiv study: Core developers reviewed 6.5% more code after Copilot's introduction but showed a 19% drop in original code productivity. The study concludes: "productivity gains of AI may mask the growing burden of maintenance on a shrinking pool of experts, together with increased technical debt."
— arXiv 2510.10165
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[QUOTE]
"The increase in productivity is primarily driven by less-experienced (peripheral) developers."
— Xu et al., arXiv 2510.10165
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[QUOTE]
"Code written after the adoption of AI requires more rework to satisfy repository standards."
— Xu et al., arXiv 2510.10165
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

### 5.3 Structural QA Limitations

[FACT]
A GitClear study found that AI coding assistant adoption has led to an 8x increase in duplicated code blocks. Code churn — code added and then quickly modified or removed — doubled between 2021 and 2024 due to AI-generated suggestions.
— InfoQ / AI Technical Debt Report
URL: https://www.infoq.com/news/2025/11/ai-code-technical-debt/
Date: November 2025

[FACT]
AI-generated code is described as "highly functional but systematically lacking in architectural judgment" by a report from Ox Security, which catalogued 10 architecture and security anti-patterns commonly found in AI-generated code.
— InfoQ / AI Technical Debt
URL: https://www.infoq.com/news/2025/11/ai-code-technical-debt/
Date: November 2025

[FACT]
Forrester predicts that by 2026, more than 50% of technology decision-makers will face moderate to severe technical debt attributed to AI code generation. That figure is expected to reach 75% by the following year.
— Forrester / Inclusion Cloud analysis
URL: https://inclusioncloud.com/insights/blog/ai-generated-code-technical-debt/
Date: 2025

### 5.4 Emerging QA Responses

[FACT]
Enterprise organizations are implementing multi-agent validation chains: one agent writes code, a second critiques it, a third tests it, and a fourth validates compliance and architectural alignment. This pattern is described as "reducing cognitive burden on developers while increasing certainty that code entering production is safe."
— Qodo AI / State of AI Code Quality 2025
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: 2025

[FACT]
Traditional SAST and DAST tools are insufficient as standalone measures for AI-generated code, because "AI models can merge pieces of unrelated patterns, leading to new vulnerabilities that signature-based tools usually miss." Recommended augmentations include fuzz testing, runtime instrumentation, and business-logic-aware testing tools.
— Cybersecurity Dive / StackHawk
URL: https://www.cybersecuritydive.com/spons/the-future-of-dast-in-an-ai-first-world-why-runtime-security-testing-remai/811891/
Date: 2025

---

## Section 6: Whether the Tool Ecosystem Favors Building vs. Buying SaaS

### 6.1 Current Build vs. Buy Signals

[STATISTIC]
Retool's 2026 Build vs. Buy Report (n=817 enterprise builders): 35% of teams have already replaced at least one purchased SaaS tool with a custom build. 78% expect to build more custom tools in 2026.
— Retool 2026 Build vs. Buy Report / BusinessWire
URL: https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
Date: February 2026

[STATISTIC]
SaaS categories under replacement pressure (Retool 2026 survey): Workflow automations (35%), internal admin tools (33%), BI tools (29%), CRMs and form builders (25%), project management (23%), customer support (21%).
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

[STATISTIC]
60% of builders created tools outside IT oversight in the past year. 64% of shadow IT creators were senior managers and above. Top reasons for bypassing IT: speed (31%), unmet needs from existing SaaS (25%), IT processes too slow (18%).
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

[STATISTIC]
51% of surveyed builders have built production software using AI. 49% of those shipping production software with AI save 6+ hours weekly.
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

[STATISTIC]
Deployment blockers for custom builds: lack of technical knowledge (23%), lost priority or budget (22%), code hallucination or wrong data structures (22%). Technical barriers: resource/engineering bandwidth (42%), security and compliance concerns (41%), system integration challenges (39%).
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

### 6.2 Named Enterprise Case Studies

[FACT]
ClickUp built six AI tools connecting Salesforce, Zendesk, and Snowflake, saving "hundreds of thousands in headcount costs" and "$200K per year in automation software."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

[FACT]
Harmonic rebuilt a "$20,000-per-year third-party tool" internally using Retool and now operates 33 internal apps with enterprise security controls.
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

### 6.3 Analyst Views on Build vs. Buy Trajectory

[FACT]
Gartner predicts that by 2028, 90% of enterprise software engineers will use AI code assistants, up from less than 14% in early 2024. Developer roles are expected to shift "from implementation to orchestration, focusing on problem solving and system design."
— Gartner press release
URL: https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
Date: April 2024

[FACT]
Gartner predicts 40% of enterprise applications will feature task-specific AI agents by end of 2026, up from less than 5% in 2025. In a best-case scenario, agentic AI could drive approximately 30% of enterprise application software revenue by 2035, surpassing $450 billion.
— Gartner press release
URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
Date: August 2025

[FACT]
Gartner warns that over 40% of agentic AI projects will be canceled by end of 2027 "due to escalating costs, unclear business value or inadequate risk controls." Gartner identifies "agent washing" — rebranding existing products without substantial agentic capabilities — as a market distortion risk.
— Gartner press release
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: June 2025

[FACT]
Forrester's 2026 Technology and Security Predictions state that enterprises will defer 25% of planned AI spend to 2027, as "the gap between inflated vendor promises and the value delivered to enterprises is widening."
— Forrester press release
URL: https://investor.forrester.com/news-releases/news-release-details/forresters-2026-technology-security-predictions-ais-hype-fades-0
Date: 2025

[FACT]
Forrester identifies "agentic software development (ASD)" as the most consequential shift: "a new way of building software in which AI systems do real development work, not just assist humans." Forrester predicts "vibe coding" will evolve into "vibe engineering" in 2026 — encompassing the full SDLC rather than just code generation.
— Forrester blog / SD Times
URL: https://sdtimes.com/softwaredev/forrester-shares-its-predictions-for-how-ai-will-continue-to-shape-software-development-in-2026/
Date: 2025

### 6.4 Persistent Structural Constraints on Building

[STATISTIC]
Technical barriers to automation that constrain custom build efforts: resource/engineering bandwidth (42%), security and compliance concerns (41%), system integration challenges (39%), unclear ROI (33%), budget constraints (30%), maintenance burden (26%).
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: 2026

[STATISTIC]
Annual maintenance for custom software typically consumes 15–25% of initial development investment, a cost not typically modeled in build-vs-buy analyses.
— AgileEngine software cost breakdown
URL: https://agileengine.com/software-development-cost-breakdown-in-2025-a-complete-guide/
Date: 2025

[STATISTIC]
65% of IT leaders report unexpected charges from consumption-based AI pricing models. Average monthly enterprise AI spending reached $85,521 in 2025, a 36% increase from 2024.
— Zylo AI pricing analysis
URL: https://zylo.com/blog/ai-cost/
Date: 2025

[FACT]
Forrester predicts that "the time to fill developer positions will double" as organizations seek candidates with strong system architecture foundations to oversee AI-generated code. This talent constraint limits the speed at which enterprises can build and maintain custom software.
— Forrester 2026 Predictions / SD Times
URL: https://sdtimes.com/softwaredev/forrester-shares-its-predictions-for-how-ai-will-continue-to-shape-software-development-in-2026/
Date: 2025

---

## Comparative Overview: AI Developer Tool Market Share (2025)

| Tool | Market Share (Paid) | User Base | Fortune 100 Presence | Primary Mode |
|---|---|---|---|---|
| GitHub Copilot | 42% | 20M+ users (July 2025) | 90% | Inline assistant + coding agent |
| Cursor | ~35% (enterprise seats) | 2.1M+ users (late 2025) | 64% of Fortune 500 | Agentic IDE |
| Amazon Q Developer | 11% | Not disclosed | AWS-anchored enterprises | Inline assistant + agent |
| Windsurf | Not disclosed | Hundreds of thousands (April 2025) | JPMorgan Chase, Dell + 350 enterprise clients | Agentic IDE |
| Devin (Cognition) | Not disclosed | Thousands of companies | Goldman Sachs, Santander, Citi | Autonomous agent |

Sources: Faros AI bakeoff ([https://www.faros.ai/blog/github-copilot-vs-amazon-q-enterprise-bakeoff](https://www.faros.ai/blog/github-copilot-vs-amazon-q-enterprise-bakeoff)), Cursor Enterprise ([https://cursor.com/enterprise](https://cursor.com/enterprise)), Visual Studio Magazine ([https://visualstudiomagazine.com/articles/2025/07/09/github-copilot-swamps-gemini-code-assist-amazon-q-among-engineers-ai-coding-survey-says.aspx](https://visualstudiomagazine.com/articles/2025/07/09/github-copilot-swamps-gemini-code-assist-amazon-q-among-engineers-ai-coding-survey-says.aspx)), Cognition ([https://cognition.ai/blog/devin-annual-performance-review-2025](https://cognition.ai/blog/devin-annual-performance-review-2025))

---

## Cross-References

See F03: Agentic Coding Current State for detailed coverage of SWE-bench benchmarks, tool capability comparisons, and specific failure modes of agentic coding tools. This file (D03) focuses on enterprise adoption metrics, deployment patterns, and the build-vs-buy signal, not technical capability depth.

---

## Key Takeaways

- The enterprise developer tool ecosystem has crossed a threshold: AI-powered IDEs (Cursor at 64% of Fortune 500, GitHub Copilot at 90% of Fortune 100) are now standard infrastructure, not experiments, and the cost of building custom software has structurally declined.

- Autonomous agents have moved into production at Tier 1 financial institutions. Goldman Sachs deploying Devin alongside 12,000 engineers — targeting a 20% efficiency gain equivalent to 2,400 additional developers — represents a validated enterprise model for AI-augmented development capacity.

- The build signal is real but concentrated: 35% of enterprises have replaced a SaaS tool with a custom build (Retool 2026), but replacement pressure clusters in workflow automation, internal tooling, and BI — not in regulated, complex, or deeply integrated SaaS categories.

- Quality and security debt are the primary constraints on accelerated building. AI-generated code introduces security flaws in 45% of cases, core developers absorb a 19% productivity drop from reviewing AI output, and Forrester projects 75% of tech decision-makers will face severe technical debt by 2026 — constraining the net speed advantage that tools nominally provide.

- Analyst consensus is bullish on the direction but cautious on pace: Gartner forecasts 40% of agentic AI projects will be canceled by 2027, Forrester projects 25% of planned AI spend will be deferred, and the talent constraint (developer positions taking twice as long to fill) remains a rate-limiter on building at enterprise scale.

---

## Sources

1. Cursor Enterprise page — https://cursor.com/enterprise
2. Cursor / NVIDIA case study — https://cursor.com/blog/nvidia
3. Tom's Hardware — NVIDIA Cursor deployment — https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-now-produces-three-times-as-much-code-as-before-ai-specialized-version-of-cursor-is-being-used-by-over-30-000-nvidia-engineers-internally
4. NVIDIA CEO endorses Cursor — Tech Startups — https://techstartups.com/2025/10/09/nvidias-ceo-endorses-cursor-100-of-our-engineers-now-code-with-ai/
5. Cursor valuation / ARR — Stocktwits — https://stocktwits.com/news-articles/markets/equity/this-ai-coding-startup-backed-by-nvidia-google-is-now-valued-at-29-b-revenue-tops-1-b/cLP9JPMREEc
6. Windsurf enterprise ARR / Cognition acquisition — Elephas — https://elephas.app/blog/windsurf-ai-3-billion-collapse-72-hours
7. Windsurf FedRAMP on AWS Marketplace — https://aws.amazon.com/marketplace/pp/prodview-x4iqsqorbfaj4
8. OpenAI acquires Windsurf — DevOps.com — https://devops.com/openai-acquires-windsurf-for-3-billion-2/
9. Agentic IDE rise — Financial Content / Token Ring — https://markets.financialcontent.com/wss/article/tokenring-2026-1-26-the-rise-of-the-agentic-ide-how-cursor-and-windsurf-are-automating-the-art-of-software-engineering
10. GitHub Copilot crosses 20M users — TechCrunch — https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/
11. GitHub Copilot accelerates enterprise adoption — MLQ.ai — https://mlq.ai/news/github-copilot-surpasses-20-million-all-time-users-accelerates-enterprise-adoption/
12. GitHub Copilot vs Amazon Q enterprise bakeoff — Faros AI — https://www.faros.ai/blog/github-copilot-vs-amazon-q-enterprise-bakeoff
13. GitHub Copilot swamps Amazon Q in survey — Visual Studio Magazine — https://visualstudiomagazine.com/articles/2025/07/09/github-copilot-swamps-gemini-code-assist-amazon-q-among-engineers-ai-coding-survey-says.aspx
14. GitHub Copilot statistics 2026 — Quantumrun — https://www.quantumrun.com/consulting/github-copilot-statistics/
15. Amazon Q Developer at AWS re:Invent 2025 — CloudThat — https://www.cloudthat.com/resources/blog/aws-reinvent-2025-announces-amazon-q-developer-transforms-cloud-development
16. PwC / Amazon Q Developer enterprise partnership — https://www.pwc.com/us/en/technology/alliances/library/amazon-q-developer.html
17. Goldman Sachs Devin pilot — CNBC — https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html
18. Goldman Sachs "hybrid workforce" — IBM Think — https://www.ibm.com/think/news/goldman-sachs-first-ai-employee-devin
19. Devin 2025 Performance Review — Cognition AI — https://cognition.ai/blog/devin-annual-performance-review-2025
20. Cognition raises $400M — TechCrunch — https://techcrunch.com/2025/09/08/cognition-ai-defies-turbulence-with-a-400m-raise-at-10-2b-valuation/
21. Devin produces 25% of Cognition's code — Financial Content — https://markets.financialcontent.com/wral/article/tokenring-2025-12-30-the-worlds-first-autonomous-ai-software-engineer-devin-now-produces-25-of-cognitions-code
22. Cognition on X (Devin enterprise customers) — https://x.com/cognition/status/1991218551655657748
23. Devin 2.0 launch / price reduction — Digital Applied — https://www.digitalapplied.com/blog/devin-ai-autonomous-coding-complete-guide
24. DevOps market size / AIOps transformation — Softjourn — https://softjourn.com/insights/how-ai-is-transforming-devops
25. AI code generation pushing DevSecOps to machine speed — Computer Weekly — https://www.computerweekly.com/news/366639364/How-AI-code-generation-is-pushing-DevSecOps-to-machine-speed
26. Opsera AI software delivery report — PR Newswire — https://www.prnewswire.com/news-releases/new-opsera-report-reveals-how-ai-is-transforming-software-delivery-and-driving-business-outcomes-302673996.html
27. Retool 2026 Build vs. Buy Report — https://retool.com/blog/ai-build-vs-buy-report-2026
28. Retool 2026 Build vs. Buy Report — BusinessWire — https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
29. AI code quality statistics (46% AI-generated) — CleanAim — https://cleanaim.com/resources/silent-wiring/46-percent-ai-generated-code-quality-challenge/
30. CISO Guide to AI-generated code security — Checkmarx — https://checkmarx.com/blog/ai-is-writing-your-code-whos-keeping-it-secure/
31. AI-generated code security risks — Veracode — https://www.veracode.com/blog/ai-generated-code-security-risks/
32. DAST in AI-first world — Cybersecurity Dive — https://www.cybersecuritydive.com/spons/the-future-of-dast-in-an-ai-first-world-why-runtime-security-testing-remai/811891/
33. State of AI Code Quality 2025 — Qodo — https://www.qodo.ai/reports/state-of-ai-code-quality/
34. arXiv: AI-Assisted Programming and Technical Debt — https://arxiv.org/abs/2510.10165
35. AI code technical debt report — InfoQ — https://www.infoq.com/news/2025/11/ai-code-technical-debt/
36. AI-generated code and technical debt — Inclusion Cloud — https://inclusioncloud.com/insights/blog/ai-generated-code-technical-debt/
37. Gartner: 75% of engineers will use AI code assistants by 2028 — https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
38. Gartner: 40% of enterprise apps with task-specific AI agents by 2026 — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
39. Gartner: 40% of agentic AI projects canceled by 2027 — https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
40. Gartner: Top strategic technology trends for 2026 — https://www.gartner.com/en/newsroom/press-releases/2025-10-20-gartner-identifies-the-top-strategic-technology-trends-for-2026
41. Forrester 2026 Technology and Security Predictions — https://investor.forrester.com/news-releases/news-release-details/forresters-2026-technology-security-predictions-ais-hype-fades-0
42. Forrester predictions for AI software development 2026 — SD Times — https://sdtimes.com/softwaredev/forrester-shares-its-predictions-for-how-ai-will-continue-to-shape-software-development-in-2026/
43. Forrester predictions 2026: AI agents and enterprise software — https://www.forrester.com/blogs/predictions-2026-ai-agents-changing-business-models-and-workplace-culture-impact-enterprise-software/
44. Custom software maintenance cost benchmarks — AgileEngine — https://agileengine.com/software-development-cost-breakdown-in-2025-a-complete-guide/
45. Enterprise AI spending / unexpected costs — Zylo — https://zylo.com/blog/ai-cost/
