# F03: Agentic Coding Current State (2025–2026)

**Research Question:** What can agentic coding tools actually do today in terms of autonomous software creation?
**Scope:** Capabilities, benchmarks, limitations, and adoption — as of early 2026. No future projections.

---

## Executive Summary

Agentic coding tools have moved well beyond autocomplete: the leading platforms (Cursor, GitHub Copilot coding agent, Devin, Replit Agent 3, Claude Code) can now autonomously plan, write, test, and open pull requests across multi-file, multi-step tasks with minimal human input. On the SWE-bench Verified benchmark — the primary industry yardstick — top agents now resolve approximately 77–79% of real-world GitHub issues, up from single digits in 2023. Enterprise adoption is accelerating sharply: 90% of Fortune 100 companies have deployed GitHub Copilot, and Cursor reached $1.2B ARR with 50,000+ enterprise seats. However, significant failure modes persist: AI-generated code contains security vulnerabilities in 45–62% of cases depending on the study, developers report that 66% spend more time fixing "almost-right" code, and model attention degrades on large codebases that exceed context window limits. The practitioner consensus is that agentic tools reliably handle bounded, verifiable tasks (security patching, test generation, migrations) but require structured human oversight for ambiguous or architectural work.

---

## 1. Major Agentic Coding Tools and Their Capabilities

### 1.1 Cursor

[FACT]
"Enterprise adoption skyrocketed, exceeding 50,000 seats as engineering teams within Fortune 1000 companies standardized on Cursor for their daily development tasks. At companies like OpenAI, Shopify, and Perplexity, engineers use Cursor to automate routine tasks, from boilerplate generation to debugging."
— Opsera/Cursor adoption analysis
URL: https://opsera.ai/blog/cursor-ai-adoption-trends-real-data-from-the-fastest-growing-coding-tool/
Date: 2025

[FACT]
Cursor's agent works in multiple modes (fix, review, refactor) with "strong repo-level reasoning." The multi-agent Cursor 2.0 architecture allows simultaneous editing where "8 agents can modify different files concurrently during large-scale refactoring" with "automatic dependency tracking across import relationships."
— Artezio/Cursor 2.0 analysis
URL: https://www.artezio.com/pressroom/blog/revolutionizes-architecture-proprietary/
Date: 2025

### 1.2 GitHub Copilot (Coding Agent Mode)

[FACT]
GitHub Copilot coding agent "can work independently in the background to complete tasks, just like a human developer." It "automates branch creation, commit message writing and pushing, PR opening, and PR description writing." The agent is available on Copilot Pro, Pro+, Business, and Enterprise plans.
— GitHub Docs
URL: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
Date: 2025

[FACT]
At Microsoft Build 2025, GitHub described the Copilot coding agent as "the most enterprise-ready of its kind — amplifying human developers with trust by design," noting it is "built around an integrated, secure, and fully customizable development environment powered by GitHub Actions."
— GitHub Press Release
URL: https://github.com/newsroom/press-releases/coding-agent-for-github-copilot
Date: 2025

[FACT]
"You can now run Claude and Codex agents directly alongside GitHub Copilot, starting them as local agents when you need fast, interactive help, or delegating async to a cloud agent for longer-running tasks."
— GitHub Blog
URL: https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/
Date: February 2026

### 1.3 Devin (Cognition AI)

[FACT]
Devin's PR merge rate increased from 34% to 67% year-over-year. The platform has processed hundreds of thousands of PRs in 18 months since launch and is "4x faster at problem solving" and "2x more efficient in resource consumption" compared to its prior version.
— Cognition AI, Devin's 2025 Annual Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[FACT]
Devin excels at "tasks with clear, upfront requirements" requiring "4-8 hours of junior engineer work." Documented task categories include: migrating and modernizing repos, fixing vulnerabilities surfaced by static analysis tools (SonarQube, Veracode), writing unit tests, and completing small tickets.
— Cognition AI, Devin's 2025 Annual Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[STATISTIC]
The April 2025 Devin 2.0 release reduced pricing from $500/month to $20/month for the Core plan.
— Trickle, Devin AI Review
URL: https://trickle.so/blog/devin-ai-review
Date: 2025

### 1.4 Replit Agent 3

[FACT]
Replit Agent 3, released in September 2025, "runs on its own for up to 200 minutes, handling full tasks autonomously — building, testing and fixing your app, with minimal manual oversight." The agent includes a "proprietary testing system [that] is 3x faster and 10x more cost effective than Computer Use Models."
— Replit Blog
URL: https://blog.replit.com/introducing-agent-3-our-most-autonomous-agent-yet
Date: September 2025

[FACT]
Replit Agent can build "Telegram bots, Slack agents, and time-based automations" and includes "built-in Authentication, Database, Hosting, and Monitoring... ready to go from day one."
— Replit Agent Documentation
URL: https://docs.replit.com/replitai/agent
Date: 2025

### 1.5 Claude Code (Anthropic)

[FACT]
Claude Code "reads your entire repository, understands the architecture, and plans multi-step changes across multiple files, delivering pull-request-ready diffs with a human-in-the-loop review step." Its sub-agent feature lets developers "coordinate parallel sub-agents with shared task lists and dependency tracking."
— Claude Code Documentation / MorphLLM comparison
URL: https://www.morphllm.com/comparisons/claude-code-vs-copilot
Date: 2026

[FACT]
In the 2025 Stack Overflow Developer Survey, Claude Code was cited as an IDE used by 10% of professional developers surveyed, making it the third most-cited AI-native IDE behind Cursor (18%) and ahead of Windsurf (5%).
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: December 2025

### 1.6 Windsurf (Codeium / Cognition AI)

[STATISTIC]
Windsurf reached $100 million ARR by April 2025, up from $12 million in late 2024 — an 8x increase in four months. By January 2025, the platform was processing over 150 billion tokens daily.
— Contrary Research, Windsurf Business Breakdown
URL: https://research.contrary.com/company/windsurf
Date: 2025

[FACT]
In December 2025, Cognition AI (makers of Devin) acquired Windsurf for approximately $250 million — described as "the biggest AI dev tools M&A deal to date." At acquisition, Windsurf had $82M ARR with enterprise revenue doubling quarter-over-quarter.
— Contrary Research
URL: https://research.contrary.com/company/windsurf
Date: 2025

---

## 2. Types of Applications Agentic Tools Can Build Today

[FACT]
Current agentic coding tools are documented as capable of building: full-stack CRUD web applications (authentication, roles, dashboards, deployment pipelines), SaaS and CRM systems, data analysis tools, content management systems, administrative interfaces, Telegram/Slack bots, time-based automation workflows, and single-purpose internal tools.
— Flatlogic Blog, Top 10+ Agentic App Builders in 2025
URL: https://flatlogic.com/blog/top-10-agentic-app-builders/
Date: 2025

[FACT]
"Replit Agent can spin up apps, fix bugs, and deploy — all from natural language." Startups including Loveable, Replit, and Vercel "enable users who have little or no coding experience to build web applications from scratch."
— Superframeworks Blog, Best AI Coding Tools 2025
URL: https://superframeworks.com/blog/best-ai-coding-tools
Date: 2025

[FACT]
Agentic tools are documented as handling software migration tasks with quantified outcomes: one Devin deployment migrated a proprietary ETL framework "in 3-4 hours per file vs. 30-40 hours for humans (10x improvement)" and a Java version migration at "14x faster than human engineers."
— Cognition AI, Devin's 2025 Annual Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[FACT]
Enterprises use agentic tools to create "real SaaS, CRM, and ERP systems that scale." Agentic patterns are documented as "especially well-suited to enterprise applications, data analysis tools, content management systems, and administrative interfaces."
— The New Stack, AI Coding Tools in 2025
URL: https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/
Date: 2025

---

## 3. Benchmark Performance

### 3.1 SWE-bench Verified

SWE-bench Verified is a human-validated subset of 500 real-world GitHub issues used as the primary industry benchmark for autonomous code resolution.

| Agent / Model | SWE-bench Verified Score | Date |
|---|---|---|
| Sonar Foundation Agent (w/ Claude Opus 4.5) | 79.2% | February 19, 2026 |
| Claude 4.5 Opus (high reasoning, bash-only) | 76.8% | February 17, 2026 |
| Gemini 3 Flash (high reasoning) | 75.8% | February 17, 2026 |
| Verdent Agent (pass@1) | 76.1% | 2025 |
| Verdent Agent (pass@3, within 3 attempts) | 81.2% | 2025 |

Sources:
- Sonar press release: https://www.sonarsource.com/company/press-releases/sonar-claims-top-spot-on-swe-bench-leaderboard/
- SWE-bench official leaderboard: https://www.swebench.com/
- Verdent technical report: https://www.verdent.ai/blog/swe-bench-verified-technical-report
- Epoch AI benchmark tracker: https://epoch.ai/benchmarks/swe-bench-verified

### 3.2 SWE-bench Pro (Harder Benchmark)

[STATISTIC]
On SWE-Bench Pro — a more challenging, previously unseen-codebase variant — top models score substantially lower: OpenAI GPT-5 at 23.3% and Claude Opus 4.1 at 23.1% on the public dataset. On the private (unseen) subset, Claude Opus 4.1 drops to 17.8% and GPT-5 to 14.9%.
— Scale AI SEAL Leaderboard
URL: https://scale.com/leaderboard/swe_bench_pro_public
Date: 2025–2026

### 3.3 Real-World Task Completion

[STATISTIC]
In one independent study assigning Devin 20 real-world development tasks, Devin "completed only three out of 20 assigned tasks," a 15% completion rate. This was contrasted with higher benchmark scores, indicating benchmark-to-production gaps.
— Trickle, Devin AI Review
URL: https://trickle.so/blog/devin-ai-review
Date: 2025

[STATISTIC]
In 10 real-world web development challenges benchmarked by Superframeworks, Cursor "achieved the highest backend and combined score and tied with Kiro Code for perfect frontend performance."
— Superframeworks Blog
URL: https://superframeworks.com/blog/best-ai-coding-tools
Date: 2025

### 3.4 Productivity Metrics

| Metric | Value | Source |
|---|---|---|
| GitHub Copilot: coding speed increase | 51% faster | GitHub / Second Talent |
| GitHub Copilot: code retention rate | 88% | GitHub |
| GitHub Copilot: increase in successful builds | 84% | GitHub Enterprise data |
| Cursor: time savings on debugging/refactoring | 20–25% | Opsera |
| Cursor: reduction in development cycles (complex projects) | 30–50% | Opsera |
| Devin: vulnerability resolution vs. human | 1.5 min vs. 30 min (20x) | Cognition AI |
| Devin: test coverage increase (typical) | 50–60% → 80–90% | Cognition AI |

Sources:
- GitHub / Second Talent: https://www.secondtalent.com/resources/github-copilot-statistics/
- Opsera: https://opsera.ai/blog/cursor-ai-adoption-trends-real-data-from-the-fastest-growing-coding-tool/
- Cognition AI: https://cognition.ai/blog/devin-annual-performance-review-2025

---

## 4. Current Limitations and Failure Modes

### 4.1 Hallucinations and Code Correctness

[STATISTIC]
"Overall, AI created 1.7 times as many bugs as humans. AI created 1.3–1.7 times more critical and major issues. The biggest issues lay in logic and correctness. AI-created PRs had 75% more of these errors, adding up to 194 incidences per hundred PRs."
— Stack Overflow Blog, "Are bugs and incidents inevitable with AI coding agents?"
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 2026

[FACT]
"In SWE-bench, state-of-the-art models invent whole classes, methods, and terminal outputs — never realizing they had lost touch with the real codebase." When "coding models spiral into self-reinforcing hallucinations, small mistakes compound into catastrophic failure."
— Surge HQ
URL: https://surgehq.ai/blog/when-coding-agents-spiral-into-693-lines-of-hallucinations
Date: 2025

[FACT]
"45% of developers cite 'almost right, but not quite' solutions as their top frustration. 66% of developers say they are spending more time fixing 'almost-right' AI-generated code."
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

### 4.2 Security Vulnerabilities

[STATISTIC]
"62% of AI-generated code solutions contain design flaws or known security vulnerabilities, even when developers used the latest foundational AI models."
— Cloud Security Alliance, Understanding Security Risks in AI-Generated Code
URL: https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code
Date: July 2025

[STATISTIC]
"AI introduces security vulnerabilities in 45 percent of cases" per Veracode's 2025 GenAI Code Security Report, which "analyzed code produced by over 100 LLMs across 80 real-world coding tasks."
— Veracode 2025 GenAI Code Security Report
URL: https://www.veracode.com/blog/genai-code-security-report/
Date: 2025

[STATISTIC]
"By June 2025, AI-generated code was introducing over 10,000 new security findings per month across the repositories in our study — a 10x spike in just six months compared to December 2024."
— Apiiro Security Research
URL: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
Date: 2025

[STATISTIC]
Language-specific vulnerability failure rates: "Java had the highest failure rate, with LLM-generated code introducing security flaws more than 70 percent of the time." For cross-site scripting (CWE-80): 86% of samples failed. For log injection (CWE-117): 88% were vulnerable.
— Veracode 2025 GenAI Code Security Report
URL: https://www.veracode.com/blog/ai-generated-code-security-risks/
Date: 2025

[FACT]
A researcher "uncovered 30+ flaws in AI coding tools enabling data theft and RCE attacks." A new class of vulnerability named PromptPwnd "targets AI agents connected to vulnerable GitHub Actions or GitLab CI/CD pipelines with prompt injections to trick them into executing built-in privileged tools that lead to information leak or code execution."
— The Hacker News
URL: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
Date: December 2025

### 4.3 Context Window Constraints

[FACT]
"Current frontier models offer context windows of 1–2 million tokens, which amounts to a few thousand code files — still less than most production codebases of enterprise customers. A typical enterprise monorepo can span thousands of files and several million tokens."
— Factory.ai, The Context Window Problem
URL: https://factory.ai/news/context-window-problem
Date: 2025

[FACT]
"The 3–8 hour task sizing isn't arbitrary — it's the maximum scope that reliably fits in context. Anything bigger and you get hallucinations or incomplete implementations."
— David Lozzi, The Reality Behind the Buzz: The Current State of Agentic Engineering in 2025
URL: https://davidlozzi.com/2025/08/20/the-reality-behind-the-buzz-the-current-state-of-agentic-engineering-in-2025/
Date: August 2025

[FACT]
Research from Chroma (Hong et al., 2025) "measured 18 LLMs and found that 'models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows.'"
— Factory.ai, citing Hong et al. (2025)
URL: https://factory.ai/news/context-window-problem
Date: 2025

### 4.4 Architectural and Orchestration Failures

[FACT]
"The most damaging failures rarely come from the model 'being wrong' in isolation. They come from poor task decomposition, weak orchestration, uncontrolled feedback loops, missing verification, and invisible state mutations."
— David Lozzi
URL: https://davidlozzi.com/2025/08/20/the-reality-behind-the-buzz-the-current-state-of-agentic-engineering-in-2025/
Date: August 2025

[FACT]
Microsoft formally identified failure categories in agentic AI systems including: "bias amplification, hallucinations, misinterpretation of instructions," plus novel categories covering "memory poisoning, cross-domain prompt injection, human-in-the-loop bypass vulnerabilities, and insufficient isolation."
— MarkTechPost, citing Microsoft's Comprehensive Guide to Failure Modes in Agentic AI Systems
URL: https://www.marktechpost.com/2025/04/27/microsoft-releases-a-comprehensive-guide-to-failure-modes-in-agentic-ai-systems/
Date: April 2025

### 4.5 Ambiguity and Architectural Judgment

[FACT]
Devin "can't independently tackle an ambiguous coding project end-to-end like a senior engineer could, using its own judgement." When "tasks are vague or open-ended, it struggles with creative solutions or architectural decisions."
— Cognition AI, Devin's 2025 Annual Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

---

## 5. Developer Adoption Rates and Usage Patterns

### 5.1 Overall Developer Adoption

[STATISTIC]
80% of developers now use AI tools in their workflows per the 2025 Stack Overflow Developer Survey (n = tens of thousands of respondents). 52% report that AI agents have affected how they complete work.
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: December 2025

[STATISTIC]
"47.1% [of developers] use AI tools daily and another 17.7% use them weekly."
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: December 2025

[STATISTIC]
"Trust in the accuracy of AI has fallen from 40% in previous years to just 29% this year." Positive favorability declined "from 72% to 60% year over year."
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

[STATISTIC]
"72% say 'vibe coding' (generating full apps from prompts) is not part of their work" among professional developers.
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

### 5.2 IDE Market Share

| AI-Native IDE | Developer Adoption (2025 SO Survey) |
|---|---|
| Cursor | 18% |
| Claude Code | 10% |
| Windsurf | 5% |

Source: Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: December 2025

### 5.3 LLM Tool Usage Among Developers

[STATISTIC]
LLM models used by developers: OpenAI GPT models (81%), Claude Sonnet models (43–45%), Gemini Flash models (35%).
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: December 2025

### 5.4 GitHub Copilot User Metrics

[STATISTIC]
GitHub Copilot reached over 15 million users by early 2025, expanding to over 20 million users by July 2025. Over 50,000 organizations use Copilot. Enterprise customer growth "accelerated 75% quarter-over-quarter in Q2 2025."
— Second Talent, GitHub Copilot Statistics; MLQ.ai
URL: https://www.secondtalent.com/resources/github-copilot-statistics/
URL: https://mlq.ai/news/github-copilot-surpasses-20-million-all-time-users-accelerates-enterprise-adoption/
Date: 2025

[STATISTIC]
"81.4% of developers install the IDE extension on their first day receiving a license."
— Worklytics, Benchmark Your Copilot Adoption
URL: https://www.worklytics.co/resources/benchmark-copilot-gemini-adoption-2025-enterprise-averages-dashboard
Date: 2025

### 5.5 Cursor Metrics

[STATISTIC]
Cursor reached $1.2B ARR in 2025, up 1,100% year-over-year from $100M ARR in 2024. Valuation: $29.3 billion as of November 2025, following a $2.3 billion Series D led by Accel and Coatue. Paying customers: 360,000 (36% conversion rate from 1 million total users).
— Sacra / DevGraphIQ Cursor Statistics
URL: https://sacra.com/c/cursor/
URL: https://devgraphiq.com/cursor-statistics/
Date: 2025

---

## 6. Enterprise Adoption of Agentic Coding Tools

### 6.1 Fortune 500 / Enterprise Penetration

[STATISTIC]
"90% of Fortune 100 companies have adopted GitHub Copilot."
— Second Talent, GitHub Copilot Statistics
URL: https://www.secondtalent.com/resources/github-copilot-statistics/
Date: 2025

[STATISTIC]
Gartner predicts "75% of enterprise software engineers will use AI code assistants by 2028, up from less than 14% in early 2024."
— Gartner Press Release (April 2024) [PRE-2025 — included as baseline for comparison with 2025 actuals]
URL: https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028
Date: April 2024

[STATISTIC]
Gartner identifies AI code assistants among the "Top Strategic Trends in Software Engineering for 2025 and Beyond," stating the role of developers will shift "from implementation to orchestration."
— Gartner Press Release
URL: https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond
Date: July 2025

### 6.2 McKinsey Enterprise Scaling Data

[STATISTIC]
"23% of respondents report their organizations are scaling an agentic AI system somewhere in their enterprises." An additional 39% say they "have begun experimenting with AI agents." However, "in any given business function, no more than 10 percent of respondents say their organizations are scaling AI agents."
— McKinsey, The State of AI in 2025: Agents, Innovation, and Transformation
URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
Date: November 2025

[STATISTIC]
"Agent adoption is strongest in IT, knowledge management, and service ops." In product development specifically, "73% of respondents are not using AI agents at all."
— McKinsey, The State of AI in 2025
URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
Date: November 2025

[STATISTIC]
"JPMorgan Chase deployed a coding assistant that boosted the productivity of tens of thousands of engineers by 10% to 20%."
— McKinsey, The State of AI in 2025
URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
Date: November 2025

### 6.3 Corporate Mandates

[QUOTE]
"Reflexive AI usage is now a baseline expectation at Shopify." In an April 2025 internal memo, Shopify CEO Tobi Lütke stated that employees must justify why a task cannot be completed using AI before requesting additional resources, and that AI competency "will become a formal part of performance reviews and hiring decisions."
— TechCrunch, citing Shopify internal memo
URL: https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/
Date: April 2025

[FACT]
Shopify employees have access to a mandated suite including Microsoft Copilot, Anthropic Claude, Cursor, and internal platforms (chat.shopify.io, Proxy).
— Digital Commerce 360
URL: https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/
Date: April 2025

### 6.4 Gartner Agentic AI Caution

[STATISTIC]
"Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027, due to escalating costs, unclear business value, or inadequate risk controls."
— Gartner Press Release
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: June 2025

### 6.5 Practitioner Perspective: Agentic Engineering vs. Vibe Coding

[QUOTE]
Andrej Karpathy, February 2025: "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."
— Andrej Karpathy, cited in Vibe Coding Wikipedia / Klover.ai
URL: https://en.wikipedia.org/wiki/Vibe_coding
Date: February 2025

[QUOTE]
Andrej Karpathy, early 2026: "Programming via LLM agents is increasingly becoming a default workflow for professionals, except with more oversight and scrutiny." He described the shift as "'agentic' because the new default is that you are not writing the code directly 99% of the time, you are orchestrating agents who do and acting as oversight."
— The New Stack, "Vibe Coding is Passé"
URL: https://thenewstack.io/vibe-coding-is-passe/
Date: 2026

---

## Sources

| # | Title | URL | Date |
|---|---|---|---|
| 1 | GitHub Copilot Statistics & Adoption Trends [2025] — Second Talent | https://www.secondtalent.com/resources/github-copilot-statistics/ | 2025 |
| 2 | Copilot Surpasses 20 Million All-Time Users — MLQ.ai | https://mlq.ai/news/github-copilot-surpasses-20-million-all-time-users-accelerates-enterprise-adoption/ | 2025 |
| 3 | Cursor AI Adoption Trends — Opsera | https://opsera.ai/blog/cursor-ai-adoption-trends-real-data-from-the-fastest-growing-coding-tool/ | 2025 |
| 4 | Cursor Statistics 2025 — DevGraphIQ | https://devgraphiq.com/cursor-statistics/ | 2025 |
| 5 | Cursor Revenue & Funding — Sacra | https://sacra.com/c/cursor/ | 2025 |
| 6 | Devin Annual Performance Review 2025 — Cognition AI | https://cognition.ai/blog/devin-annual-performance-review-2025 | 2025 |
| 7 | Devin AI Review — Trickle | https://trickle.so/blog/devin-ai-review | 2025 |
| 8 | Introducing Agent 3 — Replit Blog | https://blog.replit.com/introducing-agent-3-our-most-autonomous-agent-yet | September 2025 |
| 9 | Replit Agent Documentation | https://docs.replit.com/replitai/agent | 2025 |
| 10 | SWE-bench Official Leaderboard | https://www.swebench.com/ | 2026 |
| 11 | SWE-Bench Pro Public — Scale AI SEAL | https://scale.com/leaderboard/swe_bench_pro_public | 2025–2026 |
| 12 | SWE-bench Verified — Epoch AI | https://epoch.ai/benchmarks/swe-bench-verified | 2025–2026 |
| 13 | Verdent SWE-bench Verified Technical Report | https://www.verdent.ai/blog/swe-bench-verified-technical-report | 2025 |
| 14 | Sonar Claims Top Spot on SWE-bench Leaderboard | https://www.sonarsource.com/company/press-releases/sonar-claims-top-spot-on-swe-bench-leaderboard/ | February 2026 |
| 15 | Stack Overflow 2025 Developer Survey — AI Section | https://survey.stackoverflow.co/2025/ai/ | December 2025 |
| 16 | Stack Overflow Blog — Developers Remain Willing but Reluctant | https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/ | December 2025 |
| 17 | Stack Overflow Blog — Are Bugs Inevitable with AI Coding Agents? | https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents | January 2026 |
| 18 | McKinsey State of AI 2025 — Agents, Innovation, and Transformation | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | November 2025 |
| 19 | Gartner: 40% Enterprise Apps Will Feature AI Agents by 2026 | https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025 | August 2025 |
| 20 | Gartner: 75% of Enterprise Engineers Will Use AI Code Assistants by 2028 | https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028 | April 2024 [PRE-2025] |
| 21 | Gartner: Top Strategic Trends in Software Engineering 2025 | https://www.gartner.com/en/newsroom/press-releases/2025-07-01-gartner-identifies-the-top-strategic-trends-in-software-engineering-for-2025-and-beyond | July 2025 |
| 22 | Gartner: 40% of Agentic AI Projects to Be Canceled by 2027 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | June 2025 |
| 23 | Shopify CEO AI Mandate — TechCrunch | https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/ | April 2025 |
| 24 | Shopify CEO Memo — Digital Commerce 360 | https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/ | April 2025 |
| 25 | Veracode 2025 GenAI Code Security Report | https://www.veracode.com/blog/genai-code-security-report/ | 2025 |
| 26 | Cloud Security Alliance — AI-Generated Code Security Risks | https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code | July 2025 |
| 27 | Apiiro — 4x Velocity, 10x Vulnerabilities | https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/ | 2025 |
| 28 | Hacker News — 30+ Flaws in AI Coding Tools | https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html | December 2025 |
| 29 | Factory.ai — The Context Window Problem | https://factory.ai/news/context-window-problem | 2025 |
| 30 | David Lozzi — The Reality Behind the Buzz: Agentic Engineering 2025 | https://davidlozzi.com/2025/08/20/the-reality-behind-the-buzz-the-current-state-of-agentic-engineering-in-2025/ | August 2025 |
| 31 | Microsoft Failure Modes in Agentic AI — MarkTechPost | https://www.marktechpost.com/2025/04/27/microsoft-releases-a-comprehensive-guide-to-failure-modes-in-agentic-ai-systems/ | April 2025 |
| 32 | Surge HQ — Coding Agents Spiral Into Hallucinations | https://surgehq.ai/blog/when-coding-agents-spiral-into-693-lines-of-hallucinations | 2025 |
| 33 | GitHub Blog — Pick Your Agent (Claude and Codex on Agent HQ) | https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/ | February 2026 |
| 34 | GitHub: Introducing Copilot Coding Agent | https://github.com/newsroom/press-releases/coding-agent-for-github-copilot | 2025 |
| 35 | GitHub Copilot Agent Mode — VS Code Blog | https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode | February 2025 |
| 36 | Contrary Research — Windsurf Business Breakdown | https://research.contrary.com/company/windsurf | 2025 |
| 37 | Worklytics — Benchmark Copilot Adoption 2025 | https://www.worklytics.co/resources/benchmark-copilot-gemini-adoption-2025-enterprise-averages-dashboard | 2025 |
| 38 | The New Stack — Vibe Coding is Passé (Karpathy on agentic engineering) | https://thenewstack.io/vibe-coding-is-passe/ | 2026 |
| 39 | Wikipedia — Vibe Coding | https://en.wikipedia.org/wiki/Vibe_coding | 2025–2026 |
| 40 | MorphLLM — Claude Code vs. GitHub Copilot | https://www.morphllm.com/comparisons/claude-code-vs-copilot | 2026 |
| 41 | Flatlogic — Top 10+ Agentic App Builders in 2025 | https://flatlogic.com/blog/top-10-agentic-app-builders/ | 2025 |
| 42 | The New Stack — AI Coding Tools in 2025: Welcome to the Agentic CLI Era | https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/ | 2025 |
| 43 | Superframeworks Blog — Best AI Coding Tools 2025 | https://superframeworks.com/blog/best-ai-coding-tools | 2025 |
| 44 | Cursor 2.0 Multi-Agent Architecture — Artezio | https://www.artezio.com/pressroom/blog/revolutionizes-architecture-proprietary/ | 2025 |

---

## Key Takeaways

- **Benchmark performance has reached a new plateau**: Top agentic systems now resolve ~77–79% of real-world GitHub issues on SWE-bench Verified, but scores drop sharply (to 14–23%) on harder, previously-unseen codebases (SWE-bench Pro), revealing a significant generalization gap between curated benchmarks and novel enterprise environments.

- **Enterprise tool adoption is broad but agent usage at function-scale remains thin**: 90% of Fortune 100 companies have deployed GitHub Copilot, and 80% of developers use AI tools — but McKinsey data shows that in any given business function, no more than 10% of organizations are scaling AI agents, and 73% of product-development respondents are not using AI agents at all.

- **Agentic tools are reliably productive on bounded, verifiable tasks**: Security vulnerability remediation (20x faster per Cognition), test coverage improvement (50–90% with Devin), and code migration (10–14x faster) have well-documented quantitative outcomes. Ambiguous requirements, architectural decisions, and large-codebase contexts remain high-failure-rate scenarios.

- **Security is a structural, not scaling, problem**: AI-generated code introduces security vulnerabilities in 45–62% of cases, and Veracode's research shows "larger models do not perform significantly better than smaller models" on security — indicating this is a systemic issue that does not self-correct with model scale alone.

- **Developer trust is declining even as usage grows**: The 2025 Stack Overflow survey shows AI trust dropping from 40% to 29% accuracy confidence year-over-year, and 66% of developers spending more time fixing "almost-right" AI code — suggesting that adoption breadth has outpaced practical reliability, creating a quality-oversight burden that practitioners are only beginning to structure.
