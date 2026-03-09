# D06: Developer Experience Reports — Building Enterprise-Grade Applications with Agentic Coding Tools

**Research Area:** Wave 6 — Developer Ground Truth
**Date Compiled:** 2026-03-06
**Scope:** Developer blog posts, community surveys, and empirical studies on agentic/AI coding tools in enterprise contexts. Excludes enterprise pilot program data (see E07) and tool capability benchmarks (see Wave 8).

---

## Executive Summary

The gap between individual developer enthusiasm and organizational outcomes is the defining story of AI coding tools in 2025. Adoption reached 84–85% of professional developers, yet trust in AI output accuracy fell to a historic low of 29% (Stack Overflow 2025 Developer Survey), and independent studies found that experienced developers actually worked 19% slower with AI assistance despite believing they had worked 20% faster (METR, July 2025). Code quality studies consistently show AI-generated pull requests contain 1.7x more issues than human-only PRs (CodeRabbit, December 2025), with security vulnerabilities up to 2.74x more common. Enterprise-scale analysis by Bain & Company found that while AI-using developers merged 98% more pull requests, company-wide delivery metrics showed no measurable improvement — a pattern attributed to bottlenecks downstream of coding. The practitioner consensus emerging from developer communities is that AI coding tools deliver genuine value on bounded, pattern-rich tasks (boilerplate, tests, documentation) but break down on architecture, security-critical logic, and complex debugging — precisely the work that differentiates enterprise-grade applications.

---

## Section 1: Adoption and Usage Patterns

[STATISTIC]
"85% of developers regularly use AI tools for coding and development"
— JetBrains, State of Developer Ecosystem 2025 (survey of 24,534 developers across 194 countries, April–June 2025)
URL: https://devecosystem-2025.jetbrains.com/artificial-intelligence
Date: October 2025

[STATISTIC]
"84% of developers use or plan to use AI tools (up from 76% in 2024)"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"51% of professional developers use AI tools every day"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"62% [of developers] rely on at least one AI coding assistant, agent, or code editor"
— JetBrains, State of Developer Ecosystem 2025
URL: https://devecosystem-2025.jetbrains.com/artificial-intelligence
Date: October 2025

[STATISTIC]
"41% of All Code Is Now AI-Generated" in real workflows
— index.dev, Top 100 Developer Productivity Statistics with AI Tools 2026
URL: https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
Date: 2026

[STATISTIC]
"Developers now use AI in 60% of their work but fully delegate only 0–20% of tasks"
— Anthropic, 2026 Agentic Coding Trends Report
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[STATISTIC]
"52% [of developers] don't use agents or prefer simpler tools"; "38% have no plans adopting agents"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[FACT]
"72% report 'vibe coding' (generating full apps from prompts) is not part of their professional work"
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 29, 2025

---

## Section 2: Trust and Sentiment — The Declining Confidence Curve

[STATISTIC]
"Trust in the accuracy of AI has fallen from 40% in previous years to just 29% [in 2025]"
— Stack Overflow, Press Release on 2025 Developer Survey
URL: https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
Date: 2025

[STATISTIC]
"More developers actively distrust the accuracy of AI tools (46%) than trust it (33%), and only a fraction (3%) report 'highly trusting' the output"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"Experienced developers show most caution: 20.7% highly distrust accuracy"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"Positive favorability in AI has decreased from 72% to 60% year over year"
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 29, 2025

[STATISTIC]
"99% [of developers] express some concern about AI in coding (only 1% do not)"
— JetBrains, State of Developer Ecosystem 2025
URL: https://devecosystem-2025.jetbrains.com/artificial-intelligence
Date: October 2025

[QUOTE]
"Often, AI use isn't systematized. Developers are just using it ad hoc."
— JetBrains, State of Developer Ecosystem 2025
URL: https://devecosystem-2025.jetbrains.com/artificial-intelligence
Date: October 2025

[FACT]
Stack Overflow's 2025 developer survey headline: "Developers remain willing but reluctant to use AI"
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 29, 2025

---

## Section 3: Productivity Claims vs. Measured Reality

### 3.1 Vendor Claims

[STATISTIC]
GitHub reported "55% faster task completion" in controlled experiments
— Orbit Build Blog, "The AI Coding Reality Check: What 2025 Taught Us"
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

[STATISTIC]
Microsoft reported "20–30% improvements" in developer productivity
— Orbit Build Blog, "The AI Coding Reality Check: What 2025 Taught Us"
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

[STATISTIC]
"GitHub Copilot Users Report 81% Productivity Gains, with 55% higher productivity reported"
— index.dev, Top 100 Developer Productivity Statistics with AI Tools 2026
URL: https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
Date: 2026

### 3.2 Independent Research — Controlled Studies

[STATISTIC]
"When experienced developers used AI tools, they took 19% longer to complete issues compared to working without AI assistance"
— METR (Model Evaluation & Threat Research), "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

[DATA POINT]
Study parameters: 16 experienced developers from large open-source repositories (averaging 22,000+ stars and 1M+ lines of code); 246 total issues analyzed; average task duration 2 hours per issue; randomized controlled trial (RCT) design
— METR, July 2025
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

[QUOTE]
"We view this result as a snapshot of early-2025 AI capabilities in one relevant setting."
— METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

### 3.3 The Perception Gap

[STATISTIC]
"Developers expected AI to speed them up by 24%"; "after experiencing the slowdown, developers still believed AI had sped them up by 20%"
— METR, reported by Orbit Build Blog
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

[FACT]
The perception gap between what developers believed (20% faster) and what was measured (19% slower) represents approximately a 40-percentage-point divergence between felt and actual productivity impact
— Orbit Build Blog, citing METR 2025 RCT
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

### 3.4 Enterprise-Level Organizational Metrics

[STATISTIC]
Bain & Company found that "developers using AI complete 21% more tasks and merge 98% more pull requests" but "company-wide delivery metrics for throughput and quality show no improvement — no measurable organizational impact whatsoever"
— Faros AI, "Bain Technology Report 2025: Why AI Gains Are Stalling"
URL: https://www.faros.ai/blog/bain-technology-report-2025-why-ai-gains-are-stalling
Date: 2025

[STATISTIC]
"PR review time jumped 91%" when "PR volume surged 98% among high-AI-adoption teams"
— Faros AI, citing Bain Technology Report 2025
URL: https://www.faros.ai/blog/bain-technology-report-2025-why-ai-gains-are-stalling
Date: 2025

[STATISTIC]
"Average pull request size increased 154% with 9% more bugs per developer"
— Faros AI, citing Bain Technology Report 2025
URL: https://www.faros.ai/blog/bain-technology-report-2025-why-ai-gains-are-stalling
Date: 2025

[STATISTIC]
Bain & Company described real-world enterprise savings from AI coding as "unremarkable"
— The Register, "AI coding hype overblown, Bain shrugs"
URL: https://www.theregister.com/2025/09/23/developers_genai_little_productivity_gains/
Date: September 23, 2025

[STATISTIC]
Bain found "two-thirds of software firms have deployed generative AI tools" yet "teams see only 10–15% productivity boosts"
— Bain & Company, "From Pilots to Payoff: Generative AI in Software Development," Technology Report 2025
URL: https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/
Date: 2025

[STATISTIC]
"Coding and testing represent only 25%–35% of total development lifecycle duration, limiting the impact of code-focused AI solutions alone"
— Bain & Company, "From Pilots to Payoff"
URL: https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/
Date: 2025

[STATISTIC]
"75% of companies cite adoption resistance as the primary challenge" to AI coding ROI
— Bain & Company, "From Pilots to Payoff"
URL: https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/
Date: 2025

[STATISTIC]
"Organizations achieving 25–30% productivity gains are far above the 10% from basic code assistants, because they addressed the entire lifecycle, not just coding"
— Bain & Company, "From Pilots to Payoff"
URL: https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/
Date: 2025

---

## Section 4: The Demo-to-Production Gap

### 4.1 What Works in Demo Conditions

[FACT]
Developer community consensus identifies effective AI coding use cases as: boilerplate generation, writing tests, unfamiliar syntax learning, and documentation
— Orbit Build Blog, "The AI Coding Reality Check: What 2025 Taught Us"
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

[STATISTIC]
JetBrains survey top five AI benefits reported by developers: increased productivity (74%), faster completion of repetitive tasks (73%), less time spent searching for information (72%), faster coding and development (69%), faster learning of new tools and technologies (65%)
— JetBrains, State of Developer Ecosystem 2025
URL: https://devecosystem-2025.jetbrains.com/artificial-intelligence
Date: October 2025

[STATISTIC]
"88% of AI-using developers save more than one hour per week"; "19% save 8 hours or more per week"
— JetBrains, State of Developer Ecosystem 2025
URL: https://devecosystem-2025.jetbrains.com/artificial-intelligence
Date: October 2025

### 4.2 Where AI-Generated Code Breaks Down at Enterprise Scale

[FACT]
Developer community consensus identifies ineffective/risky AI use cases as: security-critical code, complex debugging, architecture decisions, and performance optimization
— Orbit Build Blog
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

[STATISTIC]
"Only 29% believe AI handles complex tasks effectively"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"Developers show strongest resistance to AI for deployment/monitoring (76% won't use) and project planning (69% won't use)"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"65% say AI misses relevant context during refactoring"; "60% report context gaps in testing and code review tasks"
— Qodo, State of AI Code Quality 2025
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: 2025

[STATISTIC]
"76.4% [of developers] fall into 'high hallucinations, low confidence' category"
— Qodo, State of AI Code Quality 2025
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: 2025

[STATISTIC]
"25% estimate one in five AI suggestions contain factual errors"
— Qodo, State of AI Code Quality 2025
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: 2025

[QUOTE]
"AI doesn't remember your architecture. Every prompt is a fresh start."
— DEV Community, "The Vibe Coding Hangover Is Real: What Nobody Tells You About AI-Generated Code in Production"
URL: https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
Date: 2025

[QUOTE]
"The code worked. That wasn't the problem. The problem was that it worked for now — held together by duct tape, prayers, and whatever hallucination Claude had that Tuesday afternoon."
— DEV Community, "The Vibe Coding Hangover Is Real"
URL: https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
Date: 2025

[QUOTE]
"Debugging AI-generated code is harder than writing it manually."
— DEV Community, "The Vibe Coding Hangover Is Real"
URL: https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
Date: 2025

[FACT]
Enterprise governance gaps in vibe-coded applications include: absent environment separation between development and production, absent role-based access controls, absent audit logging, and secrets management relying on hardcoded credentials
— Retool Blog, "The Risks of Vibe Coding: Security Vulnerabilities and Enterprise Pitfalls"
URL: https://retool.com/blog/vibe-coding-risks
Date: 2025

[FACT]
Healthcare (HIPAA), financial (SOX), and privacy (GDPR) compliance requirements for access controls and audit trails "are rarely included [in vibe-coded applications] without fundamental architectural changes"
— Retool Blog, "The Risks of Vibe Coding"
URL: https://retool.com/blog/vibe-coding-risks
Date: 2025

---

## Section 5: Code Quality and the Defect Problem

### 5.1 Defect Rate Comparisons — CodeRabbit Study

[DATA POINT]
CodeRabbit "State of AI vs Human Code Generation" study: 470 open-source GitHub pull requests analyzed (320 AI-co-authored, 150 human-only)
URL: https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
Date: December 2025

[STATISTIC]
"AI-generated PRs: 10.83 issues per PR"; "Human-only PRs: 6.45 issues per PR"; "AI multiplier: 1.7x more issues overall"
— CodeRabbit, "State of AI vs Human Code Generation" Report
URL: https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
Date: December 2025

| Issue Category | AI vs Human Multiplier |
|---|---|
| Logic and correctness | 1.75x |
| Readability | 3.0x |
| Error handling | 2.0x |
| Security issues | up to 2.74x |
| Concurrency/dependency | 2.0x |
| Formatting | 2.66x |
| Naming inconsistencies | 2.0x |
| Excessive I/O operations | 8.0x |
| Critical/major severity | 1.4–1.7x |

Source: CodeRabbit, December 2025 — URL: https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report

[STATISTIC]
AI-generated code is "2.74x more likely to add XSS vulnerabilities"; "1.88x more likely to introduce improper password handling"; "1.91x more likely to make insecure object references"; "1.82x more likely to implement insecure deserialization"
— CodeRabbit, "State of AI vs Human Code Generation" Report
URL: https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
Date: December 2025

[FACT]
"AI-generated code often omits null checks, early returns, guardrails, and comprehensive exception logic, issues tightly tied to real-world outages"
— CodeRabbit, "State of AI vs Human Code Generation" Report
URL: https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
Date: December 2025

### 5.2 Code Duplication and Technical Debt — GitClear Data

[STATISTIC]
GitClear 2025 AI Copilot Code Quality report: "Code clones increased 4x during 2024"; "copy/paste code rose from 8.3% to 12.3% of changed lines (2021–2024)"
— GitClear, "AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones"
URL: https://www.gitclear.com/ai_assistant_code_quality_2025_research
Date: 2025

[DATA POINT]
GitClear study analyzed 211 million changed code lines from 2020–2024, sourced from repositories owned by Google, Microsoft, Meta, and enterprise corporations
URL: https://www.gitclear.com/ai_assistant_code_quality_2025_research
Date: 2025

[STATISTIC]
"Refactoring-related changes dropped from 25% of changed lines in 2021 to under 10% in 2024"
— GitClear, 2025 AI Copilot Code Quality Report
URL: https://www.gitclear.com/ai_assistant_code_quality_2025_research
Date: 2025

[STATISTIC]
"Code churn" (code added then revised within two weeks): "7.9% of all newly added code was revised within two weeks [in 2024], compared to just 5.5% in 2020"
— Reported by various sources citing GitClear
URL: https://www.jonas.rs/2025/02/09/report-summary-gitclear-ai-code-quality-research-2025.html
Date: February 9, 2025

[STATISTIC]
Projected $1.5 trillion in technical debt from AI-generated code by 2027
— DEV Community, "The Vibe Coding Hangover Is Real"
URL: https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
Date: 2025

### 5.3 Early Security Research — Empirical Vulnerability Rates

[STATISTIC]
"A 2024 empirical study found that 29.5% of Python and 24.2% of JavaScript snippets [from AI tools] contained security weaknesses, including XSS and improper input validation"
— Cited in: getdx.com, "AI code generation: Best practices for enterprise adoption in 2025"
URL: https://getdx.com/blog/ai-code-enterprise-adoption/
Date: 2025

[STATISTIC]
"LLMs failed to secure code against highly common and dangerous attacks like Cross-Site Scripting (CWE-80) and Log Injection (CWE-117) in 86% and 88% of cases respectively"
— Cited in: BayTech Consulting, "AI Vibe Coding: Why 45% of AI-Generated Code Is a Security Risk"
URL: https://www.baytechconsulting.com/blog/ai-vibe-coding-security-risk-2025
Date: 2025

---

## Section 6: The Maintenance Burden — Experienced Developer Impact

[DATA POINT]
arXiv paper title: "AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden"
URL: https://arxiv.org/abs/2510.10165
Date: October 2025 (submitted)

[STATISTIC]
"Core developers review 6.5% more code after Copilot's introduction, but show a 19% drop in their original code productivity"
— arXiv preprint 2510.10165
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[FACT]
"Productivity gains of AI may mask the growing burden of maintenance on a shrinking pool of experts, together with increased technical debt for the projects"
— arXiv preprint 2510.10165
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[FACT]
The arXiv study identifies a "fundamental tension in AI-assisted software development between short-term productivity gains and long-term system sustainability" and warns that "productivity increases may obscure growing maintenance burdens on a limited pool of expert developers"
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[STATISTIC]
"66% of developers say they are spending more time fixing 'almost-right' AI-generated code"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"45% [of developers] find debugging AI-generated code more time-consuming"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"20% report decreased confidence in their own problem-solving" after using AI tools
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"Projects using excessive AI-generated code experienced a 41% rise in bugs"
— index.dev, Top 100 Developer Productivity Statistics with AI Tools 2026
URL: https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
Date: 2026

[STATISTIC]
"Debugging AI Code Takes 45% More Time" than human-written code
— index.dev, Top 100 Developer Productivity Statistics with AI Tools 2026
URL: https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
Date: 2026

[QUOTE]
"When junior developers use AI, they're outsourcing learning...That's preparation for obsolescence."
— DEV Community, "The Vibe Coding Hangover Is Real"
URL: https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-coding-in-production-399h
Date: 2025

---

## Section 7: Enterprise Security Failure Patterns

### 7.1 IDEsaster — Systematic Vulnerability Discovery

[FACT]
Security researcher Ari Marzouk (MaccariTA) published "IDEsaster" research, December 2025: 30+ vulnerabilities discovered across 10+ AI coding tools; 24 CVEs assigned; "100% of tested AI IDEs vulnerable"
URL: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
Date: December 2025

[DATA POINT]
IDEsaster-affected tools: GitHub Copilot, Cursor, Windsurf, Kiro.dev, Zed.dev, Roo Code, JetBrains Junie, Cline, Gemini CLI, Claude Code. Specific CVEs include: CVE-2025-49150 (Cursor), CVE-2025-53097 (Roo Code), CVE-2025-58335 (JetBrains Junie)
URL: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
Date: December 2025

[QUOTE]
"AI IDEs effectively ignored the base IDE software as part of the threat model, assuming it's inherently safe because it existed for years. However, once you add AI agents that can act autonomously, the same legacy features can be weaponized into data exfiltration and RCE primitives."
— IDEsaster research finding, reported by The Hacker News
URL: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
Date: December 2025

### 7.2 Real-World Exploits in 2025

[FACT]
Amazon Q browser extension for VS Code was compromised: "A hacker compromised the official extension for using the tool inside the ubiquitous VS Code development environment, planting a prompt to direct Q to wipe users' local files and disrupt their AWS cloud infrastructure." The malicious version "passed Amazon's verification and was publicly available to users for two days."
— Fortune, "AI coding tools exploded in 2025. The first security exploits show what could go wrong"
URL: https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/
Date: December 15, 2025

[FACT]
Zak Cole, an Ethereum core developer, "said his crypto wallet was drained after he mistakenly downloaded a malicious extension for the popular AI coding tool Cursor" through typosquatting
— Fortune, December 15, 2025
URL: https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/
Date: December 15, 2025

[QUOTE]
"Agentic coding tools work within the privilege level of the developer executing them," creating systemic risks when tools operate unsupervised
— Fortune, December 15, 2025
URL: https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/
Date: December 15, 2025

[QUOTE]
"It spits out hundreds of lines of code in minutes. And then it comes down to, do they do a security assessment of that code? Do they look at all the libraries the code can pull down, or do they just say, YOLO, and deploy it?"
— Unnamed enterprise security practitioner quoted in Fortune
URL: https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/
Date: December 15, 2025

[QUOTE]
"Supply chain has always been a weak point in security for software developers in particular. It's always been a problem, but it's even more prevalent now with AI tools."
— Fortune, December 15, 2025
URL: https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/
Date: December 15, 2025

### 7.3 Lovable Platform Security Audit

[STATISTIC]
Lovable (Swedish vibe coding platform): "170 out of 1,645 Lovable-created web applications had an issue that would allow personal information to be accessed by anyone" — a 10.3% critical failure rate
— Wikipedia, "Vibe coding" article, citing May 2025 report
URL: https://en.wikipedia.org/wiki/Vibe_coding
Date: May 2025 incident

---

## Section 8: Community Consensus — What AI Is Good/Bad At

### 8.1 Camp A: Optimists (Productivity Believers)

[STATISTIC]
"When teams report considerable productivity gains, 70% also report better code quality, and with AI review in the loop, quality improvements soar to 81%"
— Qodo, State of AI Code Quality 2025
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: 2025

[STATISTIC]
"Among [agent] users: 69% report increased productivity"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"78% [of developers] experience productivity gains from AI assistance"
— Qodo, State of AI Code Quality 2025
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: 2025

[STATISTIC]
Anthropic internal study finding: "44% of Claude-assisted work consisted of tasks [engineers] wouldn't have enjoyed doing themselves"
— RedMonk, "10 Things Developers Want from their Agentic IDEs in 2025"
URL: https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/
Date: December 22, 2025

### 8.2 Camp B: Skeptics (Quality and Reliability Critics)

[QUOTE]
"I stopped using Copilot and didn't notice a decrease in productivity"
— Developer quoted in Faros AI, "Best AI Coding Agents for 2026: Real-World Developer Reviews"
URL: https://www.faros.ai/blog/best-ai-coding-agents-2026
Date: 2026

[QUOTE]
Developers report codebases become "messy, filled with unnecessary code, duplicated files, excessive comments, and frequent commits after every single change" when AI is heavily used
— Faros AI, "Best AI Coding Agents for 2026: Real-World Developer Reviews"
URL: https://www.faros.ai/blog/best-ai-coding-agents-2026
Date: 2026

[QUOTE]
"So far, the only people I've heard are using parallel agents successfully are senior+ engineers."
— Gergely Orosz, quoted in RedMonk, "10 Things Developers Want from their Agentic IDEs in 2025"
URL: https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/
Date: December 22, 2025

[FACT]
Open-source project maintainer response to AI-generated submissions: Daniel Stenberg shut down cURL's six-year bug bounty program; Mitchell Hashimoto banned AI-generated code from Ghostty; Steve Ruiz configured tldraw to auto-close all external pull requests
— Search results citing InfoQ, "AI 'Vibe Coding' Threatens Open Source as Maintainers Face Crisis"
URL: https://www.infoq.com/news/2026/02/ai-floods-close-projects/
Date: February 2026

[QUOTE]
"Vibe coding your way to a production codebase is clearly risky. Most of the work we do as software engineers involves evolving existing systems, where the quality and understandability of the underlying code is crucial."
— The New Stack, "Vibe Coding Fails Enterprise Reality Check"
URL: https://thenewstack.io/vibe-coding-fails-enterprise-reality-check/
Date: 2025

### 8.3 Enterprise Tool Evaluation by Practitioners

| Tool | Practitioner-Reported Strength | Practitioner-Reported Limitation |
|---|---|---|
| Cursor | Flow and everyday shipping | Struggles with large, complex refactors |
| Claude Code | Deep reasoning and architecture | Higher cost; rate limit incidents mid-2025 |
| GitHub Copilot | Frictionless enterprise integration | Less impressive on complex reasoning |
| Codex | Multi-step task reliability | Less IDE mindshare; opaque pricing |
| Cline | Control and flexibility | Requires deliberate user expertise |

Source: Faros AI, "Best AI Coding Agents for 2026: Real-World Developer Reviews"
URL: https://www.faros.ai/blog/best-ai-coding-agents-2026
Date: 2026

---

## Section 9: Enterprise Infrastructure Pain Points Reported by Developers

[FACT]
Developer top evaluation criteria for enterprise AI coding tools (in order): token efficiency and cost; real productivity impact; code quality and hallucination control; repository understanding; privacy and data control
— Faros AI, "Best AI Coding Agents for 2026: Real-World Developer Reviews"
URL: https://www.faros.ai/blog/best-ai-coding-agents-2026
Date: 2026

[FACT]
Anthropic's rate limits in mid-2025 "sparked significant backlash when developers hit caps mid-workstream"; cost predictability has become "a major decision factor" for enterprise tool selection
— Faros AI, "Best AI Coding Agents for 2026: Real-World Developer Reviews"
URL: https://www.faros.ai/blog/best-ai-coding-agents-2026
Date: 2026

[FACT]
Cursor's shift to usage-based pricing and Replit's effort-based model caused "unexpected cost overruns" that became a reported enterprise adoption barrier
— RedMonk, "10 Things Developers Want from their Agentic IDEs in 2025"
URL: https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/
Date: December 22, 2025

[FACT]
"Daily incidents reported across major platforms; latency and crashes during extended agent sequences" in 2025
— RedMonk, "10 Things Developers Want from their Agentic IDEs in 2025"
URL: https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/
Date: December 22, 2025

[FACT]
"Multi-agent orchestration currently limited to experienced senior engineers" according to practitioner reports
— RedMonk, "10 Things Developers Want from their Agentic IDEs in 2025"
URL: https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/
Date: December 22, 2025

[QUOTE]
"Human-in-the-loop controls and checkpoint/rollback functionality emerged as critical safety mechanisms developers demand before trusting autonomous agents with production workflows"
— RedMonk, "10 Things Developers Want from their Agentic IDEs in 2025"
URL: https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/
Date: December 22, 2025

[STATISTIC]
"75% [of developers] would still ask another person for help when they don't trust AI's answers, even when coding stakes are high"
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 29, 2025

---

## Section 10: Employment and Workforce Distribution Effects

[STATISTIC]
Stanford Digital Economy Lab analysis of ADP payroll data: "Entry-level dev jobs (ages 22–25): -20% since late 2022"; "Senior dev jobs (ages 35–49): +9% same period"
— Orbit Build Blog, citing Stanford Digital Economy Lab
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

[STATISTIC]
"AI-exposed entry roles: -13% vs. less-exposed roles"
— Orbit Build Blog, citing Stanford Digital Economy Lab
URL: https://www.orbit.build/blog/ai-coding-hype-vs-evidence
Date: 2025

---

## Key Takeaways

- **The productivity paradox is empirically documented.** The most rigorous independent study available (METR RCT, July 2025, n=246 issues, 16 experienced developers) found a 19% slowdown for experienced developers on real open-source issues — while those same developers reported a 20% perceived speedup. Vendor claims of 20–55% gains come exclusively from vendor-controlled studies on representative tasks, not production codebases.

- **AI code quality deficits are quantified and large.** CodeRabbit's December 2025 analysis of 470 PRs found AI-generated code produces 1.7x more total issues, 2.74x more XSS vulnerabilities, 3x more readability problems, and 8x more excessive I/O operations than human-authored code. GitClear's 211-million-line analysis found code clones increased 4x during 2024 and refactoring dropped from 25% to under 10% of changed lines.

- **Organizational productivity gains do not follow individual gains.** Bain & Company's analysis of 10,000+ developers found that 98% more merged PRs translated to no measurable improvement in company-wide delivery metrics. PR review time jumped 91% to absorb the AI-generated PR surge, making bottleneck migration — not net gain — the dominant enterprise pattern.

- **Enterprise-grade requirements remain the hard ceiling.** Security, compliance (HIPAA, SOX, GDPR), architecture integrity, and complex debugging are identified by developer communities as AI's worst categories. 100% of tested AI IDEs were vulnerable to IDEsaster prompt injection attacks. Real-world exploits occurred in 2025 against Amazon Q and Cursor users. These are not theoretical risks — they are documented failures at the layer that matters most for enterprise-grade applications.

- **The skills bifurcation is measurable.** Senior developer hiring is up 9% while entry-level is down 20% (Stanford/ADP data). The arXiv preprint 2510.10165 documents a 19% drop in experienced developer original code productivity alongside a 6.5% increase in their review workload — suggesting AI is concentrating maintenance burden on the most expensive and scarce engineering talent rather than distributing work more broadly.

---

## Sources

1. JetBrains, State of Developer Ecosystem 2025 — AI section: https://devecosystem-2025.jetbrains.com/artificial-intelligence
2. Stack Overflow 2025 Developer Survey — AI section: https://survey.stackoverflow.co/2025/ai/
3. Stack Overflow blog, "Developers remain willing but reluctant to use AI": https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
4. Stack Overflow press release on 2025 Developer Survey: https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
5. METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity": https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
6. arXiv preprint 2510.10165, "AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden": https://arxiv.org/abs/2510.10165
7. Orbit Build Blog, "The AI Coding Reality Check: What 2025 Taught Us About Hype vs. Evidence": https://www.orbit.build/blog/ai-coding-hype-vs-evidence
8. Bain & Company, "From Pilots to Payoff: Generative AI in Software Development," Technology Report 2025: https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/
9. Faros AI, "Bain Technology Report 2025: Why AI Gains Are Stalling": https://www.faros.ai/blog/bain-technology-report-2025-why-ai-gains-are-stalling
10. The Register, "AI coding hype overblown, Bain shrugs": https://www.theregister.com/2025/09/23/developers_genai_little_productivity_gains/
11. CodeRabbit, "State of AI vs Human Code Generation" Report: https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
12. Business Wire, CodeRabbit report press release: https://www.businesswire.com/news/home/20251217666881/en/CodeRabbits-State-of-AI-vs-Human-Code-Generation-Report-Finds-That-AI-Written-Code-Produces-1.7x-More-Issues-Than-Human-Code
13. GitClear, "AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones": https://www.gitclear.com/ai_assistant_code_quality_2025_research
14. GitClear 2025 report summary (jonas.rs): https://www.jonas.rs/2025/02/09/report-summary-gitclear-ai-code-quality-research-2025.html
15. Qodo, "State of AI Code Quality" 2025: https://www.qodo.ai/reports/state-of-ai-code-quality/
16. Fortune, "AI coding tools exploded in 2025. The first security exploits show what could go wrong": https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/
17. The Hacker News, "Researcher Uncovers 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE Attacks" (IDEsaster): https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
18. Retool Blog, "The Risks of Vibe Coding: Security Vulnerabilities and Enterprise Pitfalls": https://retool.com/blog/vibe-coding-risks
19. DEV Community (paulthedev), "The Vibe Coding Hangover Is Real: What Nobody Tells You About AI-Generated Code in Production": https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
20. RedMonk (Kara Holterhoff), "10 Things Developers Want from their Agentic IDEs in 2025": https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/
21. Faros AI, "Best AI Coding Agents for 2026: Real-World Developer Reviews": https://www.faros.ai/blog/best-ai-coding-agents-2026
22. index.dev, "Top 100 Developer Productivity Statistics with AI Tools 2026": https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
23. getdx.com, "AI code generation: Best practices for enterprise adoption in 2025": https://getdx.com/blog/ai-code-enterprise-adoption/
24. BayTech Consulting, "AI Vibe Coding: Why 45% of AI-Generated Code Is a Security Risk for Your Business": https://www.baytechconsulting.com/blog/ai-vibe-coding-security-risk-2025
25. The New Stack, "Vibe Coding Fails Enterprise Reality Check": https://thenewstack.io/vibe-coding-fails-enterprise-reality-check/
26. InfoQ, "AI 'Vibe Coding' Threatens Open Source as Maintainers Face Crisis": https://www.infoq.com/news/2026/02/ai-floods-close-projects/
27. Wikipedia, "Vibe coding" (for Lovable platform statistics): https://en.wikipedia.org/wiki/Vibe_coding
28. Anthropic, 2026 Agentic Coding Trends Report (landing page): https://resources.anthropic.com/2026-agentic-coding-trends-report
29. Stack Overflow blog, "Mind the gap: Closing the AI trust gap for developers": https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/
30. getpanto.ai, "AI Coding Productivity Statistics 2026: Gains, Tradeoffs, and Metrics": https://www.getpanto.ai/blog/ai-coding-productivity-statistics
