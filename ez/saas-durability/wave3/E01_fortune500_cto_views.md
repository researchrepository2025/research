# E01: How Fortune 500 Technology Leaders Are Thinking About Build vs. Buy in the Agentic Coding Era

**Research Wave:** Wave 3 — Enterprise Executive Perspectives
**Scope:** Fortune 500 CTO/CIO views only. Mid-market excluded (see E02). Developer-level views excluded (see Wave 6).
**Date Compiled:** 2026-03-06
**Sources:** 2025–2026 only unless marked [PRE-2025]

---

## Executive Summary

Fortune 500 technology leaders are not abandoning SaaS — but they are renegotiating the terms. The build-vs-buy equation is shifting under pressure from three converging forces: AI-assisted development has collapsed custom software build costs, agentic AI is absorbing the business logic that once locked enterprises into SaaS workflows, and shadow IT at scale is surfacing latent demand that packaged software never fully served.

The data as of early 2026 is unambiguous on direction: 35% of enterprises have already replaced at least one SaaS tool with a custom build, and 78% expect to build more in 2026 (Retool, February 2026). Yet Fortune 500 CTOs are proceeding with deliberate risk calibration — not wholesale replacement. Goldman Sachs' CIO is building multi-LLM internal platforms while remaining explicitly "plug-and-play" with vendors. JPMorgan Chase's CIO reports 20% coding efficiency gains and is deploying agents to 230,000 employees — but atop existing vendor infrastructure, not instead of it. Capital One built its own proprietary multi-agentic workflow and cut latency fivefold, but still leverages open-source foundation models.

The dominant posture among Fortune 500 technology leaders is hybrid orchestration: buy the data layer and governance rails from incumbent SaaS vendors, build the intelligence and workflow layer internally or with specialized AI-native third parties. The VC narrative of imminent SaaS obsolescence does not match the risk tolerance on display in enterprise IT budget allocation — but the structural shift in the economics of custom software is real and durable.

---

## Section 1: The Structural Economics Have Changed

[FACT]
"35% of teams have already replaced at least one SaaS tool with a custom build, and 78% expect to build more custom internal tools in 2026."
— Retool 2026 Build vs. Buy Report (817 respondents, surveyed late 2025)
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[QUOTE]
"The cost of building custom software has collapsed. Two years ago, a custom internal tool might take weeks and cost six figures. That's a structural change, not a cyclical one."
— **David Hsu**, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2026

[QUOTE]
"The default question shifts from 'What should we buy?' to 'Can we build this?'"
— **David Hsu**, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2026

[QUOTE]
"Shadow IT at this scale is a demand signal."
— **David Hsu**, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2026

[STATISTIC]
"60% of builders created tools outside IT oversight in the past year; 25% report doing so frequently. 64% of shadow IT creators were senior managers and above."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"51% have built production software using AI. 49% of custom-built production software saves six or more hours weekly."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[DATA POINT]
SaaS categories facing the most replacement pressure from custom builds (Retool 2026 survey, n=817): workflow automations (35%), internal admin tools (33%), BI tools (29%), CRMs/form builders (25%), project management (23%), customer support (21%).
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[QUOTE]
"We realized we could build these tools ourselves and save on multiple subscriptions."
— **Borys Aptekar**, GTM AI Product Manager, ClickUp
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[FACT]
"OpenAI's latest frontier reasoning model (o3) dropped 80% in cost within just two months."
— Bain & Company, "Will Agentic AI Disrupt SaaS?"
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

---

## Section 2: Named Fortune 500 CTO/CIO Positions

### Camp A: Pragmatic Hybrid Builders (Build the Intelligence Layer, Buy the Data Layer)

**Goldman Sachs**

[QUOTE]
"It's really about people and AIs working side by side. Engineers are going to be expected to have the ability to really describe problems in a coherent way and turn it into prompts... and then be able to supervise the work of those agents."
— **Marco Argenti**, Chief Technology Officer, Goldman Sachs
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: July 2025

[QUOTE]
"Those models are basically just as good as any developer. So I think that will serve as a proof point also to expand it to other places."
— **Marco Argenti**, CTO, Goldman Sachs (on autonomous AI coders)
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: July 2025

[QUOTE]
"We have the entire organization that needs to somehow re-tune and re-tool itself for AI. But, I think we've been very, very, very intentional with regards to driving people change management."
— **Marco Argenti**, CIO, Goldman Sachs
URL: https://fortune.com/2025/03/19/goldman-sachs-cio-ai/
Date: March 19, 2025

[QUOTE]
"All of those considerations got us to the point where we want to continue to plug-and-play with those models."
— **Marco Argenti**, CIO, Goldman Sachs (on multi-vendor AI model strategy)
URL: https://fortune.com/2025/03/19/goldman-sachs-cio-ai/
Date: March 19, 2025

[FACT]
Goldman Sachs announced in July 2025 plans to deploy thousands of autonomous AI software engineers working alongside the bank's approximately 12,000 human developers. The firm projects 3–4x productivity gains compared to previous AI tools.
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: July 2025

[FACT]
Goldman Sachs' GS AI Assistant uses large language models from Gemini, OpenAI, and Llama simultaneously. The firm provides AI access to approximately 23,000 of its 46,000 employees as of March 2025, with plans to expand further.
URL: https://fortune.com/2025/03/19/goldman-sachs-cio-ai/
Date: March 19, 2025

[QUOTE]
"The last 5% now matters because the rest is now a commodity." (Referring to IPO prospectus automation where AI now handles 95% of completion in minutes versus a 6-person team over 2 weeks.)
— **David Solomon**, CEO, Goldman Sachs
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: 2025

**JPMorgan Chase**

[QUOTE]
"We've already seen up to 20% efficiency in coding as our engineers utilize coding AI tools."
— **Lori Beer**, Global CIO, JPMorgan Chase
URL: https://www.cio.com/article/3616622/jpmorgan-chase-builds-ambitious-ai-foundation-on-aws.html
Date: 2025

[QUOTE]
"In cybersecurity, we built a threat modeler copilot to help developers better understand the threats of a system's design... It's already making an impact, saving developers hours, streamlining their workflows, and ensuring comprehensive threat coverage."
— **Lori Beer**, Global CIO, JPMorgan Chase
URL: https://www.artificialintelligence-news.com/news/jpmorgan-chase-ai-strategy-2025/
Date: 2025

[FACT]
JPMorgan Chase deployed its internally-built LLM Suite — a multi-model platform integrating OpenAI and Anthropic with updates every eight weeks — to more than 230,000 employees. JPMorgan allocated $18 billion to technology in 2025 with 2,000+ AI specialists working on 450+ use cases.
URL: https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html
Date: September 30, 2025

[FACT]
JPMorgan's stated ambition is to become "the world's first fully AI-connected enterprise." The firm has begun deploying agentic AI to handle complex multistep tasks for employees per an internal road map published September 2025.
URL: https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html
Date: September 30, 2025

**Capital One**

[QUOTE]
"We want to start off at the low end of the risk spectrum, but also find use cases with impact and enough complexity that we can learn from it."
— **Prem Natarajan**, Head of Enterprise AI, Capital One
URL: https://fortune.com/2025/12/15/agentic-artificial-intelligence-automation-capital-one/
Date: December 15, 2025

[FACT]
Capital One built a proprietary multi-agentic conversational AI assistant (Chat Concierge) for car dealerships using Llama (Meta's open-source LLM) customized with proprietary data. Since launch, Capital One reduced latency fivefold, attributed explicitly to building its own stack.
URL: https://venturebeat.com/ai/how-capital-one-built-production-multi-agent-ai-workflows-to-power-enterprise-use-cases
Date: 2025

[FACT]
Capital One's Chat Concierge is 55% more successful in converting leads into buyers compared to baseline. The system takes autonomous actions on customers' behalf.
URL: https://fortune.com/2025/12/15/agentic-artificial-intelligence-automation-capital-one/
Date: December 15, 2025

**Bank of America**

[QUOTE]
"AI is having a transformative effect on employee efficiency and operational excellence."
— **Aditya Bhasin**, CTO, Bank of America
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: 2025

[FACT]
Bank of America achieved 90% AI tool adoption across the firm by April 2025, with a $4 billion investment. Results include 50%+ reduction in IT service calls and 20%+ developer efficiency gains.
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: 2025

**Citigroup**

[QUOTE]
"You can give the agentic AI a task, and the agentic AI will execute that task for you, so it can act as more of a proactive partner to a developer."
— **David Griffiths**, CTO, Citigroup
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: 2025

[FACT]
Citigroup deployed GitHub Copilot to 40,000 developers with productivity improvements ranging from 2x to 20x for autonomous agent tasks.
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: 2025

### Camp B: Platform Bettors (Buy Into AI-Native SaaS, Don't Build From Scratch)

[FACT]
The a16z 2025 enterprise CIO survey (100 CIOs, 15 industries, May 2025) found "a marked shift towards buying third party applications over the last twelve months as the ecosystem of AI apps has started to mature." Over 90% of respondents were testing third-party applications in customer support.
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

[QUOTE]
"Internally developed tools are difficult to maintain and frequently don't give them a business advantage — which further cements their interest in buying instead of building apps."
— a16z enterprise CIO survey findings
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

[FACT]
Dell Technologies' Global CTO publicly articulated an agent-as-collective-skills strategy rather than internal replacement of SaaS.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[QUOTE]
"If we think of agents as digital skills, their real value emerges when they start operating as a collective."
— **John Roese**, Global CTO and Chief AI Officer, Dell Technologies
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

### Camp C: Cautious Governors (Measured Deployment, Risk-First)

[FACT]
At an EY Center for Executive Leadership event, approximately 30 pre-eminent technology leaders from Fortune 500 companies recognized the agentic AI revolution as a "key catalyst for CIOs and other technology leaders to evaluate as they consider their IT strategy and procurement decisions" — but framed evaluation as a deliberate process.
URL: https://www.ey.com/en_us/ey-center-for-executive-leadership/defining-a-cio-playbook-on-agentic-ai
Date: 2025

[QUOTE]
"We wanted to select an end-to-end process where we could truly transform rather than just solve for a single pain point."
— **Marie Myers**, Executive Vice President and CFO, HPE
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[QUOTE]
"Now is an ideal time to conduct value stream mapping to understand how workflows should work versus the way they do work. Don't simply pave the cow path."
— **Brent Collins**, Head of Global SI Alliances, Intel
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[QUOTE]
"It's hybrid by design. It's not going to substitute for people, but it's going to change what they do today."
— **Maribel Solanas Gonzalez**, Group Chief Data Officer, Mapfre
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

---

## Section 3: Survey Data on Enterprise Build vs. Buy Intentions

### Gartner (2025)

[STATISTIC]
"40% of enterprise applications will include task-specific AI agents by the end of 2026, up from less than 5% in 2025."
— Gartner press release, August 26, 2025
URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
Date: August 26, 2025

[QUOTE]
"AI agents are evolving rapidly, progressing from basic assistants embedded in enterprise applications today to task-specific agents by 2026 and ultimately multiagent ecosystems by 2029."
— **Anushree Verma**, Senior Director Analyst, Gartner
URL: https://www.uctoday.com/unified-communications/gartner-predicts-40-of-enterprise-apps-will-feature-ai-agents-by-2026/
Date: August 2025

[QUOTE]
"Most agentic AI projects right now are early stage experiments or proof of concepts that are mostly driven by hype and are often misapplied. This can blind organizations to the real cost and complexity of deploying AI agents at scale, stalling projects from moving into production."
— **Anushree Verma**, Senior Director Analyst, Gartner
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: June 25, 2025

[STATISTIC]
"Over 40% of agentic AI projects will be canceled by the end of 2027, due to escalating costs, unclear business value, or inadequate risk controls."
— Gartner press release, June 25, 2025
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: June 25, 2025

[STATISTIC]
"By 2035, agentic AI will account for nearly $450 billion in enterprise software revenue, representing 30% of the market."
— Gartner (via UC Today summary of August 2025 press release)
URL: https://www.uctoday.com/unified-communications/gartner-predicts-40-of-enterprise-apps-will-feature-ai-agents-by-2026/
Date: August 2025

[STATISTIC]
"In a January 2025 Gartner poll of 3,412 webinar attendees: 19% said their organization had made significant investments in agentic AI; 42% had made conservative investments; 8% no investments; 31% taking a wait-and-see approach or unsure."
— Gartner poll, January 2025
URL: https://www.klover.ai/ai-agents-in-enterprise-market-survey-mckinsey-pwc-deloitte-gartner/
Date: 2025

### McKinsey (November 2025)

[STATISTIC]
"62% of survey respondents say their organizations are at least experimenting with AI agents. 23% are scaling agentic systems somewhere, though in no business function have more than 10% of companies scaled these agents."
— McKinsey State of AI, November 2025 (n=1,993, 105 nations, surveyed September 29–November 10, 2025)
URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
Date: November 2025

### EY (May 2025)

[STATISTIC]
"48% of tech executives are actively adopting or fully deploying agentic AI; 50% report over 50% of AI deployment will be autonomous within 24 months."
— EY Technology Pulse Poll, April 9–21, 2025 (n=504 U.S. technology industry leaders, director-equivalent and above, companies with 5,000+ employees)
URL: https://www.ey.com/en_us/newsroom/2025/05/ey-survey-reveals-that-technology-companies-are-setting-the-pace-of-agentic-ai-will-others-follow-suit
Date: May 2025

[STATISTIC]
"92% of tech executives expect to increase AI spending over the next year (up 10 percentage points from March 2024). 43% allocate over half their total AI budget to agentic AI."
— EY Technology Pulse Poll, April 2025
URL: https://www.ey.com/en_us/newsroom/2025/05/ey-survey-reveals-that-technology-companies-are-setting-the-pace-of-agentic-ai-will-others-follow-suit
Date: May 2025

[QUOTE]
"Technology companies continue to set the pace for rapid agentic AI adoption" and demonstrate "ambitious AI spending and a move from pilots to production."
— **James Brundage**, EY Global Technology Sector Leader
URL: https://www.ey.com/en_us/newsroom/2025/05/ey-survey-reveals-that-technology-companies-are-setting-the-pace-of-agentic-ai-will-others-follow-suit
Date: May 2025

### Deloitte Tech Trends 2026

[STATISTIC]
"14% of surveyed organizations have agentic solutions ready for deployment; 11% are actively using agentic systems in production; 30% are exploring options; 38% are piloting solutions. 42% are still developing their agentic strategy roadmap; 35% have no formal agentic strategy at all."
— Deloitte Tech Trends 2026
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[STATISTIC]
"Externally-built agentic tools demonstrate nearly double employee usage rates and twice the likelihood of reaching full deployment compared to internally developed solutions."
— Deloitte Tech Trends 2026
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[STATISTIC]
"By the end of 2026, Deloitte predicts as many as 75% of companies may invest in agentic AI, fueling a surge in spending on autonomous AI agents across SaaS platforms."
— Deloitte, State of AI in the Enterprise 2026
URL: https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
Date: 2026

### a16z Enterprise CIO Survey (May 2025)

[STATISTIC]
"Enterprise leaders expect an average of ~75% growth in AI spending over the next year. Innovation budgets dropped from 25% to 7% of LLM spending year-over-year as AI spend moved to centralized IT and business unit budgets."
— a16z "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025" (100 CIOs, 15 industries, May 2025)
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

[STATISTIC]
"81% of enterprise CIOs now use three or more model families in testing or production, up from 68% less than a year ago. 37% use five or more models, up from 29%."
— a16z enterprise CIO survey, 2025
URL: https://a16z.com/ai-enterprise-2025/
Date: 2025

### Retool 2026 Build vs. Buy Report

[STATISTIC]
"Security and compliance concerns are the second-largest barrier to AI automation, cited by 41% of respondents; system integration challenges cited by 39%; lack of engineering resources by 42%."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"72% of builders use AI for discrete code snippets integrated into projects; 57% for debugging; 31% prompt their way to complete applications."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
"75% of builders work under AI directives from leadership; 35% haven't established AI productivity metrics."
— Retool 2026 Build vs. Buy Report
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

---

## Section 4: CTO/CIO Perspectives vs. VC Narratives

### The VC Position

[QUOTE]
"Our AI platform and tools will come together to create agents, and these agents will come together to change every SaaS application category, and building custom applications will be driven by software (i.e. 'service as software')."
— **Satya Nadella**, CEO, Microsoft (BG2 Podcast, December 2024)
URL: https://www.cxtoday.com/data-analytics/microsoft-ceo-ai-agents-will-transform-saas-as-we-know-it/
Date: December 2024 [PRE-2025]

[QUOTE]
"The business logic is all going to these agents. They're not going to discriminate between what the backend is — they'll update multiple databases, and all the logic will be in the AI tier."
— **Satya Nadella**, CEO, Microsoft
URL: https://www.windowscentral.com/microsoft/hey-why-do-i-need-excel-microsoft-ceo-satya-nadella-foresees-a-disruptive-agentic-ai-era-that-could-aggressively-collapse-saas-apps
Date: December 2024 [PRE-2025]

[QUOTE]
"Thirty years of change is being compressed into three years!"
— **Satya Nadella**, CEO, Microsoft
URL: https://startupnews.fyi/2025/01/08/artificial-intelligence-disruption-ai-agents-will-revolutionise-saas-and-productivity-microsoft-ceo-satya-nadella/
Date: January 8, 2025

[QUOTE]
"Disruption is mandatory. Obsolescence is optional."
— Bain & Company, "Will Agentic AI Disrupt SaaS?" (David Crawford, Chris McLaughlin, Purna Doddapaneni, Greg Fiore)
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[QUOTE]
"In three years, any routine, rules-based digital task could move from 'human plus app' to 'AI agent plus application programming interface.'"
— Bain & Company, "Will Agentic AI Disrupt SaaS?"
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[STATISTIC]
"Goldman Sachs Research: AI agents are expected to account for more than 60% of software economics by 2030, with dollars flowing to agentic workloads rather than classic SaaS seats."
URL: https://www.goldmansachs.com/insights/articles/ai-agents-to-boost-productivity-and-size-of-software-market
Date: July 3, 2025

[STATISTIC]
"Goldman Sachs Research estimates the application software market could grow to $780 billion by 2030, a 13% compound annual growth rate. The market for customer service software could expand by an additional 20% to 45% by 2030."
URL: https://www.goldmansachs.com/insights/articles/ai-agents-to-boost-productivity-and-size-of-software-market
Date: July 3, 2025

### The Enterprise CTO Counter-Narrative

[QUOTE]
"Markets are not repricing software because artificial intelligence exists. They are repricing software because control is shifting and a new digital workforce is emerging."
— **Sumeet Chabria**, CEO & Founder, ThoughtLinks (formerly Global COO for Technology and Operations at Bank of America; Global CIO of Banking and Markets at HSBC)
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

[QUOTE]
"The real danger is not that code can be generated. The danger is that it can be generated faster than an enterprise can govern it."
— **Sumeet Chabria**, CEO & Founder, ThoughtLinks
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

[QUOTE]
"The dividing line is almost never the AI. It's everything around the AI."
— **David Hsu**, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2026

[FACT]
Goldman Sachs Chief Economist Jan Hatzius stated that AI contributed "basically zero" growth to the U.S. economy in 2025. "We think there's been a lot of misreporting of the impact that AI investment had on GDP growth in 2025, and it's much smaller than it's often perceived." Goldman forecasts AI beginning to have measurable GDP impact in 2027.
URL: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-boosted-us-economy-by-basically-zero-in-2025-says-goldman-sachs-chief-economist-we-think-theres-been-a-lot-of-misreporting-of-the-impact-that-ai-investment-had-on-gdp-growth
Date: 2026

[FACT]
"From 2024 to 2025, employee data flowing into GenAI services grew 30x, creating a dramatically larger exposure surface almost overnight. Nearly half (47%) of organizations using GenAI experienced problems, from hallucinated outputs to cybersecurity issues, privacy exposure, and IP leakage."
— State of Enterprise AI, 2025 governance survey
URL: https://www.magicmirror.team/blog/latest-adoption-risk-and-governance-insights-in-enterprise-ai
Date: 2025

[STATISTIC]
"Only 1% of organizations consider their AI strategy 'mature,' despite 78% having adopted generative AI."
— Enterprise AI maturity research, 2025
URL: https://www.adopt.ai/blog/the-top-6-enterprise-grade-agent-builder-platforms-in-2025
Date: 2025

---

## Section 5: Pilot Programs — Enterprises Experimenting With Building SaaS Replacements

[FACT]
Goldman Sachs launched a pilot of autonomous AI coders in July 2025. The system is designed to develop entire applications independently, working alongside approximately 12,000 human developers. Goldman projects 3–4x productivity gains.
URL: https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
Date: July 2025

[FACT]
Capital One built production multi-agent AI workflows using Llama and proprietary data to replace manual car dealership CRM workflows. The system is live on dealership websites across the U.S.
URL: https://venturebeat.com/ai/how-capital-one-built-production-multi-agent-ai-workflows-to-power-enterprise-use-cases
Date: 2025

[FACT]
Toyota deployed an agentic AI system that handles pre-shift preparation tasks autonomously before team members arrive.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[QUOTE]
"The agent can do all these things before the team member even comes in in the morning. We've made that critical decision to invest in this area."
— **Jason Ballard**, Vice President of Digital Innovations, Toyota
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[FACT]
Moderna framed its agentic AI deployment as workforce planning for a hybrid human-machine organization.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[QUOTE]
"We need to think about work planning, regardless of if it's a person or a technology."
— **Tracey Franklin**, Chief People and Digital Technology Officer, Moderna
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[FACT]
Bain & Company estimated that as much as half of overall technology spending by companies could shift to AI agents running across the enterprise.
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

---

## Section 6: Risk Tolerance — What Fortune 500 CTOs Will and Will Not Build

[FACT]
Bain & Company's 2025 framework maps enterprise software workflows on two axes: "user automation potential" and "AI penetration potential." Designated "battlegrounds" (high on both axes) include Intercom support, Tipalti invoicing, and ADP time-entry approvals — all considered replaceable. "Core strongholds" (low on both) include Procore project accounting and Medidata clinical-trial randomization — considered durable SaaS.
URL: https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
Date: 2025

[FACT]
Deloitte identified six indicators of AI automation risk for SaaS workflows: task structure/repetition, error risk, contextual knowledge dependency, data availability, process variability, and interface dependency. High scores on all six indicate workflows under near-term build threat.
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

[STATISTIC]
"49% of tech executives cite data privacy and security breaches as biggest AI concern — 19 percentage points higher than 2024."
— EY Technology Pulse Poll, April 2025
URL: https://www.ey.com/en_us/newsroom/2025/05/ey-survey-reveals-that-technology-companies-are-setting-the-pace-of-agentic-ai-will-others-follow-suit
Date: May 2025

[FACT]
"Roughly 90% of vertical, high-impact use cases stall at the pilot stage" in enterprise agentic AI deployments.
URL: https://www.adopt.ai/blog/the-top-6-enterprise-grade-agent-builder-platforms-in-2025
Date: 2025

[QUOTE]
"True agents are already here. You're just not using them. But it's doable today."
— **Ethan Mollick**, Professor, Wharton School
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: December 10, 2025

---

## Section 7: Board-Level Conversations About Software Strategy

[FACT]
Over 57% of Chief AI Officers at Fortune 500 companies report directly to the CEO or Board. The share of organizations with a Chief AI Officer grew from 11% to 26% in two years, with 40% of Fortune 500 companies projected to have a CAIO by 2026.
URL: https://aarondsilva.me/blog/chief-ai-officer-rise-organizational-models/
Date: 2025

[FACT]
92% of Fortune 500 firms have adopted generative AI technology as of 2025.
URL: https://www.plugandplaytechcenter.com/insights/how-fortune-500s-lead-in-generative-ai-and-ai-governance
Date: 2025

[FACT]
The AI governance market reached $197.9 million in 2024 and is projected to reach $3.2 billion by 2034, reflecting boards treating AI governance as a capital expenditure item.
URL: https://axis-intelligence.com/ai-governance-framework-fortune-500-guide/
Date: 2025

[FACT]
"~$285 billion erased in a single-day rout across software and adjacent sectors on February 3, 2026. Approximately $2 trillion lost from the S&P 500 Software & Services index since October 2025 peak." The market repricing has forced board-level reconsideration of software vendor risk.
— ThoughtLinks analysis
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

[STATISTIC]
"The U.S. software loan market stands at $235 billion. 50% of borrowers are rated B- or lower. 30% of those loans mature by 2028." These figures are entering board-level risk conversations about enterprise software vendor stability.
— ThoughtLinks analysis
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

[FACT]
Salesforce introduced consumption-based pricing for its Agentforce product at $0.10 per standard action or $2.00 per conversation, signaling vendor-led repricing of SaaS from seat-based to outcome-based models — a shift boards are evaluating for total cost of ownership impact.
URL: https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
Date: 2026

[FACT]
"Among executive respondents planning to increase AI budgets, 43% say more than half of their total AI budget is currently allocated to agentic AI." (EY, April 2025, n=504 director-level+ technology executives at firms with 5,000+ employees)
URL: https://www.ey.com/en_us/newsroom/2025/05/ey-survey-reveals-that-technology-companies-are-setting-the-pace-of-agentic-ai-will-others-follow-suit
Date: May 2025

---

## Sources

1. Retool 2026 Build vs. Buy Report — https://retool.com/blog/ai-build-vs-buy-report-2026
2. Retool/Newsweek: Enterprises Are Replacing SaaS Faster Than You Think — https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
3. Retool Press Release (BusinessWire) — https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
4. Goldman Sachs CIO (Fortune) — https://fortune.com/2025/03/19/goldman-sachs-cio-ai/
5. Goldman Sachs Autonomous Coder Pilot (Lucidate Substack) — https://lucidate.substack.com/p/goldman-sachs-scales-ai-coding-to
6. Goldman Sachs AI Agents Software Market (Goldman Sachs Insights) — https://www.goldmansachs.com/insights/articles/ai-agents-to-boost-productivity-and-size-of-software-market
7. Goldman Sachs / Jan Hatzius "basically zero" (Tom's Hardware) — https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-boosted-us-economy-by-basically-zero-in-2025-says-goldman-sachs-chief-economist-we-think-theres-been-a-lot-of-misreporting-of-the-impact-that-ai-investment-had-on-gdp-growth
8. JPMorgan Chase AI Blueprint (CNBC) — https://www.cnbc.com/2025/09/30/jpmorgan-chase-fully-ai-connected-megabank.html
9. JPMorgan Chase AI Strategy (AI News) — https://www.artificialintelligence-news.com/news/jpmorgan-chase-ai-strategy-2025/
10. JPMorgan LLM Suite (CIO Dive) — https://www.ciodive.com/news/JPMorgan-Chase-LLM-Suite-generative-ai-employee-tool/726772/
11. Capital One Agentic AI (Fortune) — https://fortune.com/2025/12/15/agentic-artificial-intelligence-automation-capital-one/
12. Capital One Multi-Agent Workflows (VentureBeat) — https://venturebeat.com/ai/how-capital-one-built-production-multi-agent-ai-workflows-to-power-enterprise-use-cases
13. a16z Enterprise CIO Survey 2025 — https://a16z.com/ai-enterprise-2025/
14. Gartner: 40% of Enterprise Apps by 2026 — https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
15. Gartner: 40% Agentic Projects Canceled by 2027 — https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
16. EY CIO Playbook on Agentic AI — https://www.ey.com/en_us/ey-center-for-executive-leadership/defining-a-cio-playbook-on-agentic-ai
17. EY Agentic AI Survey (May 2025) — https://www.ey.com/en_us/newsroom/2025/05/ey-survey-reveals-that-technology-companies-are-setting-the-pace-of-agentic-ai-will-others-follow-suit
18. Deloitte Tech Trends 2026: Agentic AI Strategy — https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
19. Deloitte State of AI in the Enterprise 2026 — https://www.deloitte.com/us/en/about/press-room/state-of-ai-report-2026.html
20. McKinsey State of AI, November 2025 — https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
21. Bain & Company: Will Agentic AI Disrupt SaaS? — https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/
22. ThoughtLinks: Agentic AI SaaS Buy-to-Build Framework — https://www.thoughtlinks.net/insights/agentic-ai-saas-buy-to-build-framework
23. Satya Nadella on AI Agents and SaaS (CX Today) — https://www.cxtoday.com/data-analytics/microsoft-ceo-ai-agents-will-transform-saas-as-we-know-it/
24. Satya Nadella (Windows Central) — https://www.windowscentral.com/microsoft/hey-why-do-i-need-excel-microsoft-ceo-satya-nadella-foresees-a-disruptive-agentic-ai-era-that-could-aggressively-collapse-saas-apps
25. Fortune 500 CAIO Rise — https://aarondsilva.me/blog/chief-ai-officer-rise-organizational-models/
26. Fortune 500 GenAI Adoption — https://www.plugandplaytechcenter.com/insights/how-fortune-500s-lead-in-generative-ai-and-ai-governance
27. AI Governance Market — https://axis-intelligence.com/ai-governance-framework-fortune-500-guide/
28. Enterprise AI Governance Insights — https://www.magicmirror.team/blog/latest-adoption-risk-and-governance-insights-in-enterprise-ai
29. Constellation Research Enterprise Technology 2026 — https://www.constellationr.com/blog-news/insights/enterprise-technology-2026-15-ai-saas-data-business-trends-watch
