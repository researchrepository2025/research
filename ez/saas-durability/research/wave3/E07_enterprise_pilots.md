# E07: Enterprise Pilot Programs — Agentic Coding to Replace or Supplement SaaS

**Research Wave:** Wave 3 — Enterprise Pilot Evidence
**Date Compiled:** March 6, 2026
**Audience:** C-suite / Board
**Scope:** Concrete pilot results, named case studies, success metrics, failure modes, and scale-up challenges. Does NOT cover tool capabilities generically (Wave 8) or VC interpretations (Wave 2).

---

## Executive Summary

Enterprise pilots using agentic coding to build custom software in place of SaaS tools have produced a sharply bifurcated record: a small set of well-resourced, technically mature organizations have achieved dramatic results — deploying working applications in days, cutting SaaS spend by hundreds of thousands of dollars, and automating weeks of manual work. The broader pilot population tells a more cautious story. S&P Global found that the share of companies abandoning the majority of their AI initiatives before reaching production surged from 17% in 2024 to 42% in 2025. The gap between a successful pilot and a scalable production system is wide, and the obstacles are organizational and architectural rather than model-quality problems.

---

## Section 1: The Macro Signal — How Far Has Replacement Already Gone?

[STATISTIC]
"35% of enterprises have already replaced at least one SaaS tool with a custom build."
— Retool, "The Build vs. Buy Shift: How Vibe Coding and Shadow IT Have Reshaped Enterprise Software" (2026 Build vs. Buy Report)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026
Survey methodology: 817 Retool customers and builders surveyed in late 2025; respondents span engineering, operations, product management, data, IT, marketing, business analysis, and finance at companies from startups to Fortune 500.

[STATISTIC]
"78% expect to build more custom internal tools in 2026."
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"51% have built production software currently in use; approximately 50% of those report saving 6+ hours weekly."
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"40% of enterprise applications will be integrated with task-specific AI agents by the end of 2026, up from less than 5% in 2025."
— Gartner press release, August 26, 2025
URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
Date: August 26, 2025

---

## Section 2: Named Enterprise Case Studies

### 2a. Rakuten — Developer Productivity at Scale

[FACT]
Rakuten engineers tested Claude Code on implementing an activation vector extraction method in vLLM, a 12.5-million-line, multi-language codebase.
URL: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
Date: 2025

[STATISTIC]
"79% reduction in time-to-market for new features (from 24 working days to 5 days)."
— Rakuten, Claude Code case study
URL: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
Date: 2025

[STATISTIC]
"7 hours of sustained autonomous coding; 99.9% numerical accuracy on the vLLM task."
— Rakuten, Claude Code case study
URL: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
Date: 2025

[QUOTE]
"I didn't write any code during those seven hours."
— Kenta Naruse, Machine Learning Engineer, Rakuten
URL: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
Date: 2025

[QUOTE]
"We want to give all our teams the power to innovate quickly. Speed and ROI are our key metrics."
— Yusuke Kaji, General Manager of AI for Business, Rakuten
URL: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
Date: 2025

[QUOTE]
"Claude Code gives us those super powers to make executions faster."
— Manoj Desai, Manager, AI Empowerment Section, Rakuten
URL: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
Date: 2025

[FACT]
Scale-up plan: Rakuten is building an "ambient agent" that breaks complex tasks into 24 parallel Claude Code sessions, each handling different aspects of updating Rakuten's massive monorepo. Rakuten operates 70+ businesses with thousands of developers serving millions of customers.
URL: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
Date: 2025

### 2b. ClickUp — SaaS Cost Elimination via Custom Tooling

[FACT]
ClickUp built six AI tools connecting Salesforce, Zendesk, and Snowflake data.
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
The ClickUp tools "automated hundreds of hours of weekly work," saved "hundreds of thousands in headcount costs," and cut "$200K per year in automation software."
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[QUOTE]
"We realized we could build these tools ourselves and save on multiple subscriptions."
— Borys Aptekar, GTM AI Product Manager, ClickUp
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### 2c. Harmonic — Replacing a $20,000 SaaS Tool

[FACT]
Harmonic, a startup discovery platform, replaced a $20,000-per-year third-party tool by rebuilding it using Retool. The company now runs 33 internal apps connected to Salesforce, Gong, Slack, and internal APIs with audit logs and role-based access.
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[QUOTE]
"Their support was so slow that it was faster for me to rebuild the product inside Retool than wait for support to get back to me."
— Miles Konstantin, Head of Automation and Tooling, Harmonic
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[FACT]
Cultural outcome: "When someone wants new software, the default question is now: 'Why can't we just build this in Retool?'"
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

### 2d. Fountain — Frontline Hiring Platform Built on Agentic AI

[STATISTIC]
Fountain achieved "50% reduction in manual screening effort," "40% quicker onboarding," and "2x candidate conversions" after deploying Claude-powered agentic workflows.
— Anthropic customer story, Fountain
URL: https://claude.com/customers/fountain
Date: 2025

[STATISTIC]
One logistics customer used Fountain's Claude-powered agents to fully staff a new fulfillment center in under 72 hours, a process that previously took over a week.
— Anthropic customer story, Fountain
URL: https://claude.com/customers/fountain
Date: 2025

[STATISTIC]
"Reducing hiring time from two weeks to 22 minutes while cutting I-9 no-shows from 50% to just 2%."
— Fountain, Business Wire press release, August 26, 2025
URL: https://www.businesswire.com/news/home/20250826771016/en/Fountain-Launches-Frontline-OS-to-Cut-New-Hire-Screening-Time-of-Frontline-Workers-by-up-to-98-and-Boost-Retention-by-50-Through-Agentic-AI
Date: August 26, 2025

[STATISTIC]
"The majority of applicants opting to speak with the AI Recruiter instead of a human."
— Fountain, Business Wire press release
URL: https://www.businesswire.com/news/home/20250826771016/en/Fountain-Launches-Frontline-OS-to-Cut-New-Hire-Screening-Time-of-Frontline-Workers-by-up-to-98-and-Boost-Retention-by-50-Through-Agentic-AI
Date: August 26, 2025

### 2e. Walmart — Internal Developer Agent (WIBEY)

[FACT]
Walmart built WIBEY, a developer-focused "super agent" that serves as a unified invocation layer across Walmart's ecosystem of 200+ internal AI agents. Built on Walmart's proprietary Element ML platform. Integrates with Slack, CLI, Visual Studio, and other developer interfaces. Uses MCP and A2A protocols.
— Walmart Global Tech blog
URL: https://tech.walmart.com/content/walmart-global-tech/en_us/blog/post/wibey-announcement.html
Date: August 29, 2025

[QUOTE]
"We're at the point where we are developing Wibey using Wibey."
— Walmart Global Tech blog (bootstrapping technique reference)
URL: https://tech.walmart.com/content/walmart-global-tech/en_us/blog/post/wibey-announcement.html
Date: August 29, 2025

### 2f. High-Growth SaaS Company (Anonymous, a16z Survey)

[FACT]
One CTO at a high-growth SaaS company reported that nearly 90% of their code is now AI-generated through Cursor and Claude Code, up from 10-15% twelve months ago with GitHub Copilot.
— a16z, "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025"
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

### 2g. Unnamed Fintech (a16z Survey)

[FACT]
One public fintech noted that while they had started to build customer support internally, a recent review of third-party solutions on the market convinced them to buy instead of continuing their build.
— a16z, "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025"
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

---

## Section 3: Categories of Applications Being Piloted

[DATA POINT]
SaaS categories most frequently replaced by custom builds, per Retool's 817-respondent survey (late 2025):
1. Workflow automations: 35%
2. Internal admin tools: 33%
3. Business intelligence tools: 29%
4. CRMs and form builders: 25%
5. Project management: 23%
6. Customer support: 21%
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"90%+ of enterprise survey respondents" are testing third-party customer support applications; two years ago, conversations with large companies focused on building AI solutions internally for customer support.
— a16z, "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025"
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

[STATISTIC]
AI agent deployment by department as of Q3 2025 (KPMG, n=130 U.S. C-suite leaders, organizations with $1B+ annual revenue):
- Technology departments: 95% leverage agents
- Operations departments: 89%
- Risk management departments: 66%
— KPMG AI Quarterly Pulse Survey, Q3 2025
URL: https://kpmg.com/us/en/media/news/q3-ai-pulse.html
Date: Q3 2025

---

## Section 4: Success Metrics — Time to Deploy, Cost Savings, Productivity

[STATISTIC]
"Developers on teams with high AI adoption complete 21% more tasks and merge 98% more pull requests."
— Faros AI, "The AI Productivity Paradox Research Report" (telemetry from 1,255 teams and 10,000+ developers)
URL: https://www.faros.ai/blog/ai-software-engineering
Date: July 23, 2025

[STATISTIC]
"Developers save 38 minutes per day on average" with AI coding assistants; "workers using AI intensively" report 40-60 minutes saved.
— Faros AI / various sources cited in ROI of AI Code Generation 2025
URL: https://zencoder.ai/blog/roi-of-ai-code-generation-in-2025-metrics-budgets-and-time-saved
Date: 2025

[STATISTIC]
"49% of builders with production software in place save 6+ hours per week; 33% save 1-5 hours weekly."
— Retool, 2026 Build vs. Buy Report (n=817)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[QUOTE]
"Eight in 10 organizations believe AI agents have already delivered measurable ROI, with another 1 in 10 saying they expect them to deliver more economic impact in the future."
— Anthropic, 2026 Agentic Coding Trends Report
URL: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
Date: January 21, 2026

[STATISTIC]
AI agent deployment nearly quadrupled: "42% of organizations have deployed at least some agents, up from 11% two quarters prior" (as of Q3 2025).
— KPMG AI Quarterly Pulse Survey, Q3 2025
URL: https://kpmg.com/us/en/media/news/q3-ai-pulse.html
Date: Q3 2025

[QUOTE]
"Results are visible, tangible, and compounding quickly."
— Steve Chase, U.S. Vice Chair and Global Head of AI and Digital Innovation, KPMG
URL: https://kpmg.com/us/en/media/news/q3-ai-pulse.html
Date: Q3 2025

[STATISTIC]
Average enterprise AI investment climbed from $114 million in Q1 2025 to $130 million in Q3 2025; "67% of leaders say they will maintain spending even if a recession occurs."
— KPMG AI Quarterly Pulse Survey, Q3 2025
URL: https://kpmg.com/us/en/media/news/q3-ai-pulse.html
Date: Q3 2025

---

## Section 5: Failure Cases and Reasons for Abandonment

[STATISTIC]
"The percentage of companies abandoning the majority of their AI initiatives before they reach production has surged from 17% in 2024 to 42% in 2025."
— S&P Global Market Intelligence, "Voice of the Enterprise: AI & Machine Learning, Use Cases 2025" (n=1,006 midlevel and senior IT and line-of-business professionals, North America and Europe)
URL: https://www.spglobal.com/market-intelligence/en/news-insights/research/ai-experiences-rapid-adoption-but-with-mixed-outcomes-highlights-from-vote-ai-machine-learning
Date: 2025

[STATISTIC]
"Organizations on average report that 46% of projects are scrapped between proof of concept and broad adoption."
— S&P Global Market Intelligence, Voice of the Enterprise 2025
URL: https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/
Date: 2025

[STATISTIC]
"95% of enterprise gen-AI implementations have had no measurable P&L impact."
— MIT study, cited in CIO.com
URL: https://www.cio.com/article/4102506/how-you-can-turn-2025-ai-pilots-into-an-enterprise-platform.html
Date: 2025

[STATISTIC]
"Gartner predicts that over 40% of agentic AI projects will be canceled by the end of 2027 due to escalating costs, security risks, or a failure to demonstrate clear business value."
— Gartner press release
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: June 25, 2025

[STATISTIC]
"14% of AI software built using AI-assisted methods tried but failed to reach production."
— Retool, 2026 Build vs. Buy Report (among 817 respondents: 51% shipped, 17% experimented but did not ship, 18% haven't tried, 14% tried but did not reach production)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[DATA POINT]
Reasons AI-built software fails to ship (Retool survey, n=817):
- Lack of technical knowledge: 23%
- Lost priority or budget: 22%
- Code hallucination or wrong data structures: 22%
- Other: 16%
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
Veracode tested 100+ large language models across 80 coding tasks. "AI-generated code introduced risky security flaws in 45% of tests." Java had a 72% security failure rate; Python, C#, and JavaScript ranged from 38% to 45%.
— Veracode, 2025 GenAI Code Security Report
URL: https://www.businesswire.com/news/home/20250730694951/en/AI-Generated-Code-Poses-Major-Security-Risks-in-Nearly-Half-of-All-Development-Tasks-Veracode-Research-Reveals
Date: July 30, 2025

[QUOTE]
"There's no way you can go live with a vibe-coded solution. It might work for demos, but we build enterprise-grade technology that has to scale across 30 countries."
— Pierre Yves Calloc'h, Pernod Ricard (enterprise tools builder)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[FACT]
The "Lovable" incident (May 2025): Lovable, a Swedish startup that marketed itself as the "fastest-growing company in Europe," allowed users with little to no technical training to create web applications via natural language prompts. The incident served as a widely-cited example of security vulnerabilities in AI-generated production applications.
— "The Reality of Vibe Coding: AI Agents and the Security Debt Crisis," Towards Data Science
URL: https://towardsdatascience.com/the-reality-of-vibe-coding-ai-agents-and-the-security-debt-crisis/
Date: 2025

---

## Section 6: The Productivity Paradox — A Critical Counter-Finding

[STATISTIC]
METR randomized controlled trial (n=16 experienced developers, 246 tasks averaging 2 hours each, from open-source repositories averaging 22,000+ stars and 1M+ lines of code): "Developers using AI tools took 19% longer to complete tasks compared to working without AI."
— Joel Becker, Nate Rush, Elizabeth Barnes, David Rein; METR
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

[STATISTIC]
"Developers forecast before starting that allowing AI will reduce completion time by 24%. After completing the study, developers estimate allowing AI reduced completion time by 20%. Actual result: 19% slowdown."
— METR study
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

[STATISTIC]
"PR review time increases 91%" on high-adoption teams, even as they merge 98% more pull requests.
— Faros AI, "The AI Productivity Paradox Research Report" (1,255 teams, 10,000+ developers)
URL: https://www.faros.ai/blog/ai-software-engineering
Date: July 23, 2025

[STATISTIC]
AI adoption is "consistently associated with a 9% increase in bugs per developer and a 154% increase in average PR size."
— Faros AI, "The AI Productivity Paradox Research Report"
URL: https://www.faros.ai/blog/ai-software-engineering
Date: July 23, 2025

[STATISTIC]
"No significant correlation between AI adoption and improvements at the company level. Across overall throughput, DORA metrics, and quality KPIs, the gains observed in team behavior do not scale when aggregated."
— Faros AI, "The AI Productivity Paradox Research Report"
URL: https://www.faros.ai/blog/ai-software-engineering
Date: July 23, 2025

---

## Section 7: Scale-Up Challenges from Pilot to Production

[STATISTIC]
"Only 25% of organizations have moved 40%+ of AI pilots into production."
— Deloitte, "State of AI in the Enterprise: The Untapped Edge" (n=3,235 business and IT leaders across 24 countries, surveyed August-September 2025)
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: January 21, 2026

[STATISTIC]
"Only 21% have mature governance models for agents" (Deloitte, same survey).
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: January 21, 2026

[QUOTE]
"Across enterprise, we're seeing massive ambition around AI, with organizations starting to pivot from experimentation to integrating AI into core business with focus on scale and impact."
— Nitin Mittal, Deloitte Global AI Leader
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: January 21, 2026

[STATISTIC]
Technical blockers to AI automation scaling (Retool survey, n=817):
- Lack of tech resources/engineering bandwidth: 42%
- Security and compliance concerns: 41%
- System integration challenges: 39%
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
Organizational blockers to scaling (Retool survey, n=817):
- Unclear ROI: 33%
- Budget constraints: 30%
- Maintenance burdens: 26%
- Fragile existing automations: 21%
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"70-85% of all AI project failures stem directly from issues with data architecture."
— Beam.ai / EPAM enterprise AI deployment analysis
URL: https://beam.ai/agentic-insights/agentic-ai-in-2025-why-90-of-implementations-fail-(and-how-to-be-the-10-)
Date: 2025

[STATISTIC]
"Only 59% of companies are moving from pilots to production, yet only 43% of organizations have formal AI governance policies in place."
— cited in Medium/@EnterpriseToolingInsights, "AI Coding Adoption at Enterprise Scale Is Harder Than Anyone Admits"
URL: https://medium.com/@EnterpriseToolingInsights/ai-coding-adoption-at-enterprise-scale-is-harder-than-anyone-admits-90cd5f3e7db3
Date: March 2026

[STATISTIC]
"46% of developers actively distrust the accuracy of AI tools, compared with 33% who trust them, with only 3.1% saying they highly trust the output."
— cited in enterprise AI deployment analysis
URL: https://www.epam.com/insights/ai/blogs/enterprise-ai-deployment-challenges
Date: 2025

[STATISTIC]
"Nearly half (47%) of organizations using GenAI experienced problems from hallucinated outputs to cybersecurity issues, privacy exposure, and IP leakage."
— cited in enterprise AI deployment analysis
URL: https://www.epam.com/insights/ai/blogs/enterprise-ai-deployment-challenges
Date: 2025

[STATISTIC]
"35% of organizations haven't established any AI productivity metrics; only 19% describe themselves as 'Advanced' in AI automation maturity."
— Retool, 2026 Build vs. Buy Report (n=817)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

---

## Section 8: Shadow IT — Pilots Bypassing Governance

[STATISTIC]
"60% of builders have created tools outside IT oversight in the past year; 25% report doing so frequently."
— Retool, 2026 Build vs. Buy Report (n=817)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"64% of shadow IT creators were senior managers or above."
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[DATA POINT]
Reasons for building outside IT oversight (Retool, n=817):
- Speed to build: 31%
- Unmet needs from existing SaaS: 25%
- IT processes too slow: 18%
- Missing integrations: 10%
- Insufficient IT bandwidth: 10%
— Retool, 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"90% of IT directors and executives at enterprises with over 1,000 employees are concerned about shadow AI from a privacy and security standpoint; nearly 80% have already experienced negative AI-related data incidents, and 13% report those incidents caused financial, customer or reputational harm."
— 2025 IT Survey, cited in ISACA "From Shadow IT to Shadow AI"
URL: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2025/volume-19/from-shadow-it-to-shadow-ai-navigating-the-new-frontier-of-enterprise-risk
Date: 2025

[STATISTIC]
"By 2030, more than 40% of enterprises will experience security or compliance incidents linked to unauthorized shadow AI."
— Gartner, November 2025 analysis
URL: https://www.cio.com/article/4083473/shadow-ai-the-hidden-agents-beyond-traditional-governance.html
Date: November 2025

---

## Section 9: Enterprise Leaders' Assessments

[QUOTE]
"The thing with agentic systems is now you can have agents just read your business policies and generate the software. This is going to disintermediate these SaaS vendors and these ERP vendors."
— Bill Vass, CTO, Booz Allen Hamilton
URL: https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas
Date: March 2, 2026

[QUOTE]
"SaaS products force you to work their way. Now that vibe coding's gone mainstream, businesses that can custom-build their value drivers will have a competitive edge."
— David Hsu, CEO and Founder, Retool
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[QUOTE]
"SaaS isn't disappearing. Organizations still need software and communication tools."
— Tamar Yehoshua, Chief Product Officer, Atlassian
URL: https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas
Date: March 2, 2026

[QUOTE]
"SaaS pricing was completely out of bounds for economic buyers. Everything was expensive."
— Faisal Masud, EVP Digital Services, HP
URL: https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas
Date: March 2, 2026

[QUOTE]
"Building dashboards takes an hour, but scaling with features and bug fixes requires team resources."
— Alexey Korotich, Chief Product Officer, Wrike
URL: https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas
Date: March 2, 2026

[FACT]
Tatyana Mamut, Former VP at Salesforce, expects the SaaS market to "majorly shrink" within five years.
URL: https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas
Date: March 2, 2026

[QUOTE]
"Across enterprise, we're seeing massive ambition around AI, with organizations starting to pivot from experimentation to integrating AI into core business with focus on scale and impact."
— Nitin Mittal, Global AI Leader, Deloitte
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: January 21, 2026

---

## Section 10: The Accenture-Anthropic Joint Offering as Pilot Infrastructure

[FACT]
Accenture and Anthropic announced a multi-year partnership expansion in December 2025 to help enterprises move from AI pilots to full-scale deployment. Approximately 30,000 Accenture professionals are to receive training. The joint offering puts Claude Code at the center of the enterprise software development lifecycle, combined with a framework to quantify productivity gains and ROI, workflow redesign for AI-first development teams, and change management.
— Accenture newsroom
URL: https://newsroom.accenture.com/news/2025/accenture-and-anthropic-launch-multi-year-partnership-to-drive-enterprise-ai-innovation-and-value-across-industries
Date: December 2025

[QUOTE]
"Claude Code had taken coding use cases from assisting on tiny tasks to AI writing 90 or sometimes even 100% of the code, with enterprises shipping in weeks what once took many quarters."
— Anthropic, via VentureBeat
URL: https://venturebeat.com/orchestration/anthropic-says-claude-code-transformed-programming-now-claude-cowork-is
Date: 2025/2026

---

## Sources Index

- Retool 2026 Build vs. Buy Report: https://retool.com/blog/ai-build-vs-buy-report-2026
- Retool Business Wire press release: https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
- Rakuten Claude Code case study: https://rakuten.today/blog/rakuten-accelerates-development-with-claude-code%EF%BF%BC.html
- Anthropic / Fountain customer story: https://claude.com/customers/fountain
- Fountain Business Wire: https://www.businesswire.com/news/home/20250826771016/en/Fountain-Launches-Frontline-OS-to-Cut-New-Hire-Screening-Time-of-Frontline-Workers-by-up-to-98-and-Boost-Retention-by-50-Through-Agentic-AI
- Walmart WIBEY blog: https://tech.walmart.com/content/walmart-global-tech/en_us/blog/post/wibey-announcement.html
- a16z Enterprise CIO Survey 2025: https://a16z.com/ai-enterprise-2025/
- Faros AI Productivity Paradox Report: https://www.faros.ai/blog/ai-software-engineering
- METR Developer Productivity RCT: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Deloitte State of AI 2026: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
- KPMG AI Quarterly Pulse Survey Q3 2025: https://kpmg.com/us/en/media/news/q3-ai-pulse.html
- S&P Global Voice of the Enterprise 2025: https://www.spglobal.com/market-intelligence/en/news-insights/research/ai-experiences-rapid-adoption-but-with-mixed-outcomes-highlights-from-vote-ai-machine-learning
- Gartner: 40% enterprise apps AI agents by 2026: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- Gartner: 40% agentic AI projects canceled by 2027: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- Veracode 2025 GenAI Code Security Report: https://www.businesswire.com/news/home/20250730694951/en/AI-Generated-Code-Poses-Major-Security-Risks-in-Nearly-Half-of-All-Development-Tasks-Veracode-Research-Reveals
- TechBrew "Is it really the end of SaaS": https://www.techbrew.com/stories/2026/03/02/is-ai-killing-saas
- Anthropic 2026 Agentic Coding Trends Report (PDF): https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
- Accenture-Anthropic partnership: https://newsroom.accenture.com/news/2025/accenture-and-anthropic-launch-multi-year-partnership-to-drive-enterprise-ai-innovation-and-value-across-industries
- ISACA Shadow IT to Shadow AI: https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2025/volume-19/from-shadow-it-to-shadow-ai-navigating-the-new-frontier-of-enterprise-risk
- CIO.com Shadow AI governance: https://www.cio.com/article/4083473/shadow-ai-the-hidden-agents-beyond-traditional-governance.html
- CIO.com Turning 2025 pilots into platform: https://www.cio.com/article/4102506/how-you-can-turn-2025-ai-pilots-into-an-enterprise-platform.html
- Bain "Will Agentic AI Disrupt SaaS": https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
