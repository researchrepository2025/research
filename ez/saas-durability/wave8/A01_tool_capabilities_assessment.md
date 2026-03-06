# A01: Agentic Coding Tool Capabilities — Rigorous Benchmarked Assessment

**Research Question:** What is a rigorous, benchmarked assessment of what current agentic coding tools can and cannot build?
**Wave:** 8 — Capability Verification
**Date Compiled:** March 2026

---

## Executive Summary

Agentic coding tools have achieved measurable, documented capability on bounded software engineering tasks: the top SWE-bench Verified score reached 79.2% in early 2026, up from single digits in 2023, and leading agents now autonomously write, test, and merge production pull requests across multi-file codebases. However, independent evaluations consistently reveal a material gap between benchmark performance and real-world task completion: Devin scored 13.86% on SWE-bench at launch yet completed only 3 of 20 real-world tasks in one independent study; METR's randomized controlled trial of experienced developers using Cursor Pro found a 19% productivity slowdown, not speedup; and SWE-bench Pro — a harder, more realistic benchmark — shows top models resolving only 23–46% of tasks, versus 70%+ on the curated verified set. The practical capability envelope as of early 2026 is well-defined: agentic tools reliably handle bounded, verifiable tasks with clear specifications (security patching, migration, test generation, CRUD apps) but break down on ambiguous requirements, cross-repository orchestration, and large-codebase architectural judgment. This document fact-checks and deepens prior wave findings; for enterprise adoption rates see D03, and for projected capability trajectories see A02.

---

## Section 1: Tool-by-Tool Capability Matrix

### 1.1 Cursor

[FACT]
Cursor's coding agent "can understand feature requests, modify multiple files simultaneously, run tests, and iterate on solutions autonomously." The Enterprise plan handles "complex codebases with tens of millions of lines and maintaining performance for thousands of devs."
— Superblocks, Cursor Enterprise Review
URL: https://www.superblocks.com/blog/cursor-enterprise
Date: 2026

[FACT]
Cursor semantically indexes a repository so the AI can reference "any relevant file or symbol when generating code." It supports enforced privacy mode, usage analytics, and SSO.
— Superblocks, Cursor Enterprise Review
URL: https://www.superblocks.com/blog/cursor-enterprise
Date: 2026

[STATISTIC]
In a head-to-head vibe-coding test (build a Next.js URL shortener with PostgreSQL and Docker), Cursor scored 9/10 — "the only agent to successfully create a Docker Compose file with a database, as well as a SQL migration script." It required only 3 follow-up error prompts.
— Render Blog, AI Coding Agents Benchmark 2025
URL: https://render.com/blog/ai-coding-agents-benchmark
Date: 2025

[STATISTIC]
In a production codebase test (Kubernetes pod leader election refactor in Go), Cursor "completed [the] refactor successfully on first attempt; maintained codebase patterns for dependency injection and interfaces."
— Render Blog, AI Coding Agents Benchmark 2025
URL: https://render.com/blog/ai-coding-agents-benchmark
Date: 2025

[STATISTIC]
An independent METR randomized controlled trial involving 16 experienced developers across 246 tasks found that "developers using Cursor Pro took 19% longer to complete coding tasks" than developers not using AI tools. Developers expected a 24% speedup; even after observing the slowdown they believed AI had provided a 20% speedup.
— METR, Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 2025

[FACT]
The METR study methodology: 16 experienced developers from large open-source repositories averaging 22,000+ stars; 246 total tasks averaging 2 hours each; participants compensated at $150/hour; primary tool was Cursor Pro with Claude 3.5/3.7 Sonnet.
— METR, Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 2025

**Capability summary:**

| Dimension | Cursor Capability (2025–2026) |
|---|---|
| Multi-file editing | Yes — concurrent editing with dependency tracking |
| Test generation and execution | Yes |
| Docker / infrastructure scaffolding | Yes — only agent to succeed in Render benchmark test |
| Large codebase (tens of millions of lines) | Claimed; independent data shows 19% slowdown on experienced devs |
| Cross-repository operations | No — single repository per session |
| Architectural judgment | Not verified independently |

Sources: https://www.superblocks.com/blog/cursor-enterprise, https://render.com/blog/ai-coding-agents-benchmark, https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

---

### 1.2 GitHub Copilot (Coding Agent)

[FACT]
GitHub Copilot coding agent can "automate branch creation, commit message writing and pushing, PR opening, and PR description writing." It works asynchronously in GitHub while Agent Mode in VS Code operates synchronously and locally.
— GitHub Docs, About Coding Agent
URL: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
Date: 2025

[FACT]
Documented hard limits of the GitHub Copilot coding agent: "Copilot cannot make changes across multiple repositories in one run." "Copilot can only create and push to branches beginning with copilot/." "Copilot can only open one pull request at a time." "Copilot coding agent cannot mark its pull requests as 'Ready for review' and cannot approve or merge a pull request."
— GitHub Docs, Copilot Coding Agent
URL: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
Date: 2025

[FACT]
When Agent Mode is invoked, Copilot "reads relevant files, runs the code, checks the output, identifies lint errors or test failures, and loops back to fix them — all within a single request. It can install packages, suggest terminal commands, and migrate code across multiple files."
— DevOps.com, GitHub Copilot Agent Mode
URL: https://devops.com/github-copilot-evolves-agent-mode-and-multi-model-support-transform-devops-workflows-2/
Date: 2025

[STATISTIC]
"GitHub Copilot generates an average of 46% of code written by users, with Java developers reaching 61%." Developers complete tasks 55% faster in GitHub's own research (involving 4,800 developers).
— Second Talent, GitHub Copilot Statistics
URL: https://www.secondtalent.com/resources/github-copilot-statistics/
Date: 2025

[FACT]
The Copilot coding agent "works in a sandbox development environment with internet access controlled by a firewall." Only users with write access to the repository can trigger the agent.
— GitHub Docs
URL: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
Date: 2025

**Capability summary:**

| Dimension | GitHub Copilot Coding Agent Capability |
|---|---|
| Multi-file editing within one repo | Yes |
| Cross-repository operations | No — explicit documented limitation |
| Autonomous PR creation | Yes — but cannot self-approve or merge |
| Branch naming flexibility | No — restricted to copilot/ prefix |
| Parallel PRs | No — one PR per task |
| Code generation rate (user code) | 46% average, 61% in Java |

Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent, https://www.secondtalent.com/resources/github-copilot-statistics/

---

### 1.3 Devin (Cognition AI)

[STATISTIC]
Devin's initial SWE-bench score at launch: 13.86% of issues resolved. This compared to the prior best unassisted baseline of 1.96% and the best "assisted" (given exact files to edit) baseline of 4.80%.
— Cognition AI, SWE-bench Technical Report
URL: https://cognition.ai/blog/swe-bench-technical-report
Date: 2024

[STATISTIC]
Devin's PR merge rate in 2025: 67% of Devin's PRs are now merged, up from 34% in 2024. Problem-solving speed: 4x faster. Resource consumption: 2x more efficient.
— Cognition AI, Devin's 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[STATISTIC]
Devin resolves security vulnerabilities in 1.5 minutes versus a human average of 30 minutes — a 20x efficiency gain. One large organization saved 5–10% of total developer time using Devin for security fixes.
— Cognition AI, Devin's 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[STATISTIC]
Devin migrations: a large bank's proprietary ETL file migration took 3–4 hours per file versus 30–40 hours for humans (10x improvement). An Oracle Java version migration completed 14x faster than human engineers.
— Cognition AI, Devin's 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[STATISTIC]
Devin: test coverage typically increased from 50–60% to 80–90%. Litera deployment: 40% increase in test coverage, 93% faster regression cycles. EightSleep: 3x as many data features shipped.
— Cognition AI, Devin's 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[STATISTIC]
Answer.AI independent evaluation: out of 20 real-world tasks assigned to Devin, results were 3 successes, 14 failures, 3 inconclusive — a 15% success rate.
— Answer.AI, Thoughts On A Month With Devin
URL: https://www.answer.ai/posts/2025-01-08-devin.html
Date: January 2025

[FACT]
Answer.AI task breakdown: Creating new projects — 2 successes, 6 failures, 1 inconclusive. Research tasks — 1 success, 2 failures. Analyzing existing code — 0 successes, 3 failures, 1 inconclusive. Modifying existing projects — 0 successes, 5 failures.
— Answer.AI, Thoughts On A Month With Devin
URL: https://www.answer.ai/posts/2025-01-08-devin.html
Date: January 2025

[QUOTE]
"Tasks it can do are so small and well-defined that I may as well do them myself, faster, my way."
— Johno Whitaker, Answer.AI
URL: https://www.answer.ai/posts/2025-01-08-devin.html
Date: January 2025

[QUOTE]
"I had initial excitement...slowly got frustrated as I had to change more and more."
— Isaac Flath, Answer.AI
URL: https://www.answer.ai/posts/2025-01-08-devin.html
Date: January 2025

[QUOTE]
"Devin struggled to use internal tooling...despite copious documentation."
— Hamel Husain, Answer.AI
URL: https://www.answer.ai/posts/2025-01-08-devin.html
Date: January 2025

[FACT]
Devin's documented best-fit task profile: tasks requiring "4-8 hours of junior engineer work" with "clear, upfront requirements." Documented failure mode: "can't independently tackle an ambiguous coding project end-to-end like a senior engineer could, using its own judgement."
— Cognition AI, Devin's 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

**Capability summary:**

| Dimension | Devin Capability |
|---|---|
| Security vulnerability patching | Strong — 20x speed, 5–10% dev time saved |
| Repository migration | Strong — 10–14x faster |
| Test generation | Strong — coverage 50%→80–90% typical |
| Modifying existing projects | Weak — 0/5 in Answer.AI evaluation |
| Ambiguous / open-ended tasks | Documented failure mode |
| Benchmark vs. production gap | 13.86% SWE-bench; 15% independent real-world |

Sources: https://cognition.ai/blog/devin-annual-performance-review-2025, https://www.answer.ai/posts/2025-01-08-devin.html

---

### 1.4 Replit Agent 3

[FACT]
Replit Agent 3 (released September 2025) "runs on its own for up to 200 minutes, handling full tasks autonomously — building, testing and fixing your app, with minimal manual oversight." It includes a "proprietary testing system [that] is 3x faster and 10x more cost effective than Computer Use Models."
— Replit Blog
URL: https://blog.replit.com/introducing-agent-3-our-most-autonomous-agent-yet
Date: September 2025

[FACT]
Replit Agent 3 capabilities: "Agent creates a plan, edits files across your project, sets up environments, runs code and tests, and can deploy." Supports mobile development via React Native and Expo (iOS and Android). Includes built-in Authentication, Database, Hosting, and Monitoring.
— Replit Agent Documentation
URL: https://docs.replit.com/replitai/agent
Date: 2025

[FACT]
Replit Agent 3 can "build other agents and automations" that integrate with Slack, email, and Telegram. The agent can operate within a single platform end-to-end: code, database, hosting, and deployment are all Replit-managed services.
— InfoQ, Replit Introduces Agent 3
URL: https://www.infoq.com/news/2025/09/replit-agent-3/
Date: September 2025

**Capability summary:**

| Dimension | Replit Agent 3 Capability |
|---|---|
| Full-stack web apps from prompt | Yes — within Replit platform |
| Mobile app scaffolding | Yes — React Native / Expo |
| Autonomous operation duration | Up to 200 minutes continuous |
| Cross-platform deployment | No — Replit-hosted only |
| Enterprise compliance controls | Not documented |
| Multi-repository operations | Not documented |

Sources: https://blog.replit.com/introducing-agent-3-our-most-autonomous-agent-yet, https://docs.replit.com/replitai/agent

---

### 1.5 Factory (Droids)

[STATISTIC]
Factory Droid scored 58.75% on Terminal-Bench at September 2025 launch, reaching #1 on the leaderboard. Factory agents occupied three of the top five positions: Droid (Claude Opus 4.1): 58.8%; Droid (GPT-5): 52.5%; Droid (Sonnet 4): 50.5%. By December 2025, Factory Droid scored 63.1%, ahead of OpenAI Codex CLI at 60.4%.
— Factory.ai, Droid on Terminal-Bench; Terminal-Bench Leaderboard
URL: https://factory.ai/news/terminal-bench
URL: https://www.tbench.ai/leaderboard/terminal-bench/2.0
Date: September–December 2025

[FACT]
Droid outperforms standalone Claude Code on the same underlying models: Droid with Opus (58.8%) beats Claude Code with Opus (43.2%); Droid with GPT-5 (52.5%) beats Codex CLI (42.8%). The performance differential reflects scaffolding and orchestration beyond base model capability.
— Factory.ai, Droid on Terminal-Bench
URL: https://factory.ai/news/terminal-bench
Date: September 2025

[FACT]
Factory Droids are described as "LLM-agnostic and interface-agnostic," storing and retrieving enterprise context from GitHub, Notion, Linear, Slack, Sentry, and other integrated sources.
— NEA / Factory.ai
URL: https://www.nea.com/blog/factory-the-platform-for-agent-native-development
Date: 2025

[STATISTIC]
Factory customer-reported outcomes: 31x faster feature delivery; 96% shorter migration times; 96% reduction in on-call resolution times. Named customers include MongoDB, Ernst & Young, Zapier, Bilt Rewards, Clari, Bayer.
— SiliconANGLE, Factory Droids $50M Funding
URL: https://siliconangle.com/2025/09/25/factory-unleashes-droids-software-agents-50m-fresh-funding/
Date: September 2025

**Capability summary:**

| Dimension | Factory Droid Capability |
|---|---|
| Terminal / CLI tasks | #1 on Terminal-Bench (63.1% as of Dec 2025) |
| Enterprise context retrieval | Yes — GitHub, Slack, Linear, Sentry, Notion |
| Model agnosticism | Yes — Claude, GPT-5, others |
| Migration workloads | 96% time reduction (vendor claim) |
| Independent benchmark verification | Terminal-Bench (#1), not SWE-bench verified |

Sources: https://factory.ai/news/terminal-bench, https://siliconangle.com/2025/09/25/factory-unleashes-droids-software-agents-50m-fresh-funding/

---

### 1.6 Claude Code (Anthropic)

[STATISTIC]
Claude Sonnet 4.5 achieved 77.2% on SWE-bench Verified. With parallel compute, the score reaches 82.0%.
— InfoQ, Claude Sonnet 4.5 Tops SWE-Bench Verified
URL: https://www.infoq.com/news/2025/10/claude-sonnet-4-5/
Date: October 2025

[FACT]
Claude Code capabilities: "searches and reads code, edits files, writes and runs tests, commits and pushes code to GitHub, and uses command line tools." It supports parallel sub-agents with shared task lists and dependency tracking.
— Anthropic, Claude SWE-Bench Performance
URL: https://www.anthropic.com/research/swe-bench-sonnet
Date: 2025

[STATISTIC]
Claude Code scored 6.8/10 in the Render benchmark's composite evaluation (behind Cursor at 8.0/10). In the Astro blog template frontend test, "Claude Code failed at complex custom data loader implementation; required specific file guidance to succeed."
— Render Blog, AI Coding Agents Benchmark 2025
URL: https://render.com/blog/ai-coding-agents-benchmark
Date: 2025

[FACT]
Anthropic's own SWE-bench evaluation used a Bash Tool (with persistent state across calls, no internet access) and an Edit Tool (string replacement requiring exact text matches). The team noted: "High token costs — many successful runs exceeded 100k tokens."
— Anthropic, Claude SWE-Bench Performance
URL: https://www.anthropic.com/research/swe-bench-sonnet
Date: 2025

**Capability summary:**

| Dimension | Claude Code Capability |
|---|---|
| SWE-bench Verified score | 77.2% (82.0% parallel); state-of-the-art at Oct 2025 |
| Multi-file editing and testing | Yes |
| Large-context tasks (>30 hours) | Yes — sustained reasoning documented |
| Docker / infrastructure generation | Below Cursor in independent test |
| Token cost | High — many runs exceed 100k tokens |

Sources: https://www.infoq.com/news/2025/10/claude-sonnet-4-5/, https://render.com/blog/ai-coding-agents-benchmark, https://www.anthropic.com/research/swe-bench-sonnet

---

## Section 2: Benchmark Results

### 2.1 SWE-bench Verified (Primary Industry Benchmark)

SWE-bench Verified is a human-validated subset of 500 real-world GitHub issues used as the primary industry benchmark for autonomous code resolution.

[FACT]
"SWE-bench evaluates AI agents on resolving real GitHub issues from Python repositories. The assessment involves understanding code, making modifications, and testing solutions against actual pull request unit tests."
— Anthropic, Claude SWE-Bench Performance
URL: https://www.anthropic.com/research/swe-bench-sonnet
Date: 2025

| Agent / Model | SWE-bench Verified Score | Date |
|---|---|---|
| Sonar Foundation Agent (w/ Claude Opus 4.5) | 79.2% | February 2026 |
| Claude Sonnet 4.5 (parallel compute) | 82.0% | October 2025 |
| Claude Sonnet 4.5 (pass@1) | 77.2% | October 2025 |
| Claude 4.5 Opus (bash-only, high reasoning) | 76.8% | February 2026 |
| Gemini 3 Flash (high reasoning) | 75.8% | February 2026 |
| Claude 3.5 Sonnet (upgraded, at release) | 49.0% | 2024 |
| Claude 3 Opus | 22.0% | 2024 |
| Devin (at launch, original SWE-bench) | 13.86% | 2024 |

Sources: https://www.infoq.com/news/2025/10/claude-sonnet-4-5/, https://www.swebench.com/, https://www.anthropic.com/research/swe-bench-sonnet, https://cognition.ai/blog/swe-bench-technical-report

### 2.2 SWE-bench Pro (Harder, Multi-file Benchmark)

[FACT]
SWE-bench Pro contains 731 publicly available problems "aimed to capture realistic, complex, enterprise-level problems." The dataset spans 41 active software engineering repositories, 123 unique programming languages. "The average solution touches 4.1 files and changes 107 lines of code."
— Scale AI SEAL, SWE-Bench Pro Public Dataset
URL: https://scale.com/leaderboard/swe_bench_pro_public
Date: 2025–2026

[STATISTIC]
SWE-bench Pro public dataset top scores (as of December 2025): claude-opus-4-5 at 45.89% (±3.60%); claude-4-5-Sonnet at 43.60%; gemini-3-pro-preview at 43.30%; claude-4-Sonnet at 42.70%; gpt-5 (High reasoning) at 41.78%. Earlier baseline scores (GPT-5, Claude Opus 4.1 without current scaffolding) were 23.3% and 23.1% respectively.
— Scale AI SEAL, SWE-Bench Pro Public Dataset
URL: https://scale.com/leaderboard/swe_bench_pro_public
Date: 2025–2026

[STATISTIC]
"While most top models score over 70% on the verified version, the best-performing models score only 23–46% on SWE-Bench Pro, indicating substantial performance differences across benchmark difficulty levels."
— Scale AI SEAL / LLM Stats
URL: https://scale.com/leaderboard/swe_bench_pro_public
Date: 2025–2026

### 2.3 Terminal-Bench

[FACT]
Terminal-Bench evaluates agents on "complicated tasks in the terminal" beyond code generation, including legacy code modernization, debugging, and real command-line operations.
— arXiv, Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces
URL: https://arxiv.org/html/2601.11868v1
Date: 2025

| Agent | Terminal-Bench Score | Date |
|---|---|---|
| Factory Droid (Claude Opus 4.1) | 63.1% | December 2025 |
| OpenAI Codex CLI | 60.4% | December 2025 |
| Factory Droid (GPT-5) | 52.5% | September 2025 |
| Factory Droid (Sonnet 4) | 50.5% | September 2025 |
| Claude Code (Opus 4.1) | 43.2% | September 2025 |
| Codex CLI (standalone) | 42.8% | September 2025 |

Source: https://factory.ai/news/terminal-bench, https://www.tbench.ai/leaderboard/terminal-bench/2.0

### 2.4 HumanEval / EvalPlus

[STATISTIC]
HumanEval pass@1 scores (2025): OpenAI o1 models: 96.3%; Claude 3.5 Sonnet: 92%; GPT-4o: 91%. On the more rigorous EvalPlus benchmark: Qwen2.5-Coder-32B-Instruct and GPT-4o both at 87.2%; DeepSeek-V3 and GPT-4-Turbo at 86.6%; Claude Sonnet 3.5 at 81.7%.
— LLM Stats, HumanEval Benchmark
URL: https://llm-stats.com/benchmarks/swe-bench-verified
Date: 2025

[FACT]
HumanEval measures single-function code generation from a docstring. EvalPlus adds additional automatically-generated test cases to increase difficulty and reduce overfitting.
— DeepEval / Confident AI, HumanEval Documentation
URL: https://deepeval.com/docs/benchmarks-human-eval
Date: 2025

### 2.5 METR Task-Length Benchmarks

[STATISTIC]
METR task-completion analysis: "Current models achieve almost 100% success rate on tasks taking humans less than 4 minutes" but "succeed less than 10% of the time on tasks taking more than around 4 hours." Claude 3.7 Sonnet achieves a 50% success rate on tasks taking approximately 55 minutes. Claude Opus 4.5 achieves 50% success on tasks of approximately 247 minutes (~4 hours). GPT-5.1 Codex Max achieves 50% success at approximately 162 minutes (~2.7 hours).
— METR, Measuring AI Ability to Complete Long Tasks
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

[FACT]
METR documents a consistent pattern: task-completion length has been "doubling approximately every 7 months for the last 6 years." This was computed across diverse software and reasoning tasks, with human task-completion time as the primary predictor of model success.
— METR, Measuring AI Ability to Complete Long Tasks
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Date: March 2025

---

## Section 3: Types of Applications Successfully Built End-to-End

[FACT]
Agentic coding tools have documented end-to-end build capability for: full-stack CRUD web applications (authentication, roles, dashboards, deployment pipelines), SaaS systems, CRM systems, data analysis tools, content management systems, administrative interfaces, Telegram/Slack bots, time-based automation workflows, and single-purpose internal tools.
— Flatlogic Blog, Top 10+ Agentic App Builders in 2025
URL: https://flatlogic.com/blog/top-10-agentic-app-builders/
Date: 2025

[FACT]
Replit Agent 3 successfully builds "Web Apps — most common full-stack web applications with frontend and backend," mobile apps via React Native and Expo, and automation workflows that integrate with Slack, email, and Telegram.
— Replit Agent Documentation
URL: https://docs.replit.com/replitai/agent
Date: 2025

[STATISTIC]
Cursor scored 9/10 in building a complete URL shortener: Next.js frontend, PostgreSQL backend, Docker Compose infrastructure, SQL migration scripts. Claude Code scored 7/10 on the same task ("well-designed but struggled with Next.js specifics").
— Render Blog, AI Coding Agents Benchmark 2025
URL: https://render.com/blog/ai-coding-agents-benchmark
Date: 2025

[FACT]
Anthropic's 2026 Agentic Coding Trends Report documents end-to-end production deployments: Rakuten achieved "99.9% accuracy on 12.5M-line codebase modifications in 7 autonomous hours." TELUS saved "500,000 hours" using agentic coding. Zapier deployed agents at "97% adoption."
— Anthropic, 2026 Agentic Coding Trends Report
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[FACT]
Devin completed documentation generation "across 400,000+ repositories" for one large bank; handled repositories of "5M lines of COBOL and 500GB" in size.
— Cognition AI, Devin's 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

---

## Section 4: Complexity Ceiling — Where Tools Break Down

### 4.1 Task Duration Ceiling

[STATISTIC]
"Current models have almost 100% success rate on tasks taking humans less than 4 minutes, but succeed less than 10% of the time on tasks taking more than around 4 hours." The 3–8 hour task sizing is described as "the maximum scope that reliably fits in context."
— METR, Measuring AI Ability to Complete Long Tasks; David Lozzi
URL: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
URL: https://davidlozzi.com/2025/08/20/the-reality-behind-the-buzz-the-current-state-of-agentic-engineering-in-2025/
Date: March 2025 / August 2025

### 4.2 Context Window Degradation

[FACT]
"Current frontier models offer context windows of 1–2 million tokens, which amounts to a few thousand code files — still less than most production codebases of enterprise customers. A typical enterprise monorepo can span thousands of files and several million tokens."
— Factory.ai, The Context Window Problem
URL: https://factory.ai/news/context-window-problem
Date: 2025

[FACT]
Research from Chroma (Hong et al., 2025) measuring 18 LLMs found that "models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows."
— Factory.ai, The Context Window Problem (citing Hong et al., 2025)
URL: https://factory.ai/news/context-window-problem
Date: 2025

### 4.3 Ambiguity and Architectural Judgment

[FACT]
Devin's documented limitation: "can't independently tackle an ambiguous coding project end-to-end like a senior engineer could, using its own judgement." When "tasks are vague or open-ended, it struggles with creative solutions or architectural decisions."
— Cognition AI, Devin's 2025 Performance Review
URL: https://cognition.ai/blog/devin-annual-performance-review-2025
Date: 2025

[FACT]
"Early-2025 AI agents often implement functionally correct code that cannot be easily used as-is, because of issues with test coverage, formatting/linting, or general code quality" on real tasks from large open-source repositories.
— METR, Research Update: Algorithmic vs. Holistic Evaluation
URL: https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/
Date: August 2025

### 4.4 Security and Quality Failures

[STATISTIC]
"62% of AI-generated code solutions contain design flaws or known security vulnerabilities, even when developers used the latest foundational AI models."
— Cloud Security Alliance, Understanding Security Risks in AI-Generated Code
URL: https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code
Date: July 2025

[STATISTIC]
"AI introduces security vulnerabilities in 45 percent of cases" per Veracode's 2025 GenAI Code Security Report, which "analyzed code produced by over 100 LLMs across 80 real-world coding tasks." Java had the highest failure rate: LLM-generated code introduced security flaws more than 70% of the time.
— Veracode, 2025 GenAI Code Security Report
URL: https://www.veracode.com/blog/genai-code-security-report/
Date: 2025

[STATISTIC]
"AI-generated code was introducing over 10,000 new security findings per month across the repositories in our study — a 10x spike in just six months compared to December 2024."
— Apiiro Security Research
URL: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
Date: 2025

[STATISTIC]
"AI created 1.7 times as many bugs as humans. AI created 1.3–1.7 times more critical and major issues. AI-created PRs had 75% more logic and correctness errors, adding up to 194 incidences per hundred PRs."
— Stack Overflow Blog, Are Bugs and Incidents Inevitable with AI Coding Agents?
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 2026

[STATISTIC]
"45% of developers cite 'almost right, but not quite' solutions as their top frustration. 66% of developers say they are spending more time fixing 'almost-right' AI-generated code."
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

### 4.5 Architectural and Orchestration Failures

[FACT]
"The most damaging failures rarely come from the model 'being wrong' in isolation. They come from poor task decomposition, weak orchestration, uncontrolled feedback loops, missing verification, and invisible state mutations."
— David Lozzi, The Reality Behind the Buzz: Agentic Engineering 2025
URL: https://davidlozzi.com/2025/08/20/the-reality-behind-the-buzz-the-current-state-of-agentic-engineering-in-2025/
Date: August 2025

[FACT]
Microsoft formally identified failure categories in agentic AI systems: "bias amplification, hallucinations, misinterpretation of instructions," plus novel agentic-specific categories covering "memory poisoning, cross-domain prompt injection, human-in-the-loop bypass vulnerabilities, and insufficient isolation."
— MarkTechPost, Microsoft's Comprehensive Guide to Failure Modes in Agentic AI Systems
URL: https://www.marktechpost.com/2025/04/27/microsoft-releases-a-comprehensive-guide-to-failure-modes-in-agentic-ai-systems/
Date: April 2025

---

## Section 5: Multi-File, Multi-System Project Handling

[FACT]
GitHub Copilot coding agent explicit documentation: "Copilot cannot make changes across multiple repositories in one run." The agent works only in a sandbox environment with firewall-controlled internet access.
— GitHub Docs
URL: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
Date: 2025

[FACT]
Cursor's enterprise documentation claims "multi-agent Cursor 2.0 architecture allows simultaneous editing where 8 agents can modify different files concurrently during large-scale refactoring with automatic dependency tracking across import relationships."
— Artezio, Cursor 2.0 Analysis
URL: https://www.artezio.com/pressroom/blog/revolutionizes-architecture-proprietary/
Date: 2025

[STATISTIC]
In the Render production codebase benchmark, Gemini CLI handled large-context multi-file scenarios well: "leveraged massive context window; loaded entire codebase automatically; succeeded after initial analysis phase" on a Kubernetes Go refactor. Claude Code "struggled with library configuration" on the same task.
— Render Blog, AI Coding Agents Benchmark 2025
URL: https://render.com/blog/ai-coding-agents-benchmark
Date: 2025

[FACT]
"Agents struggle with disorganized codebases, unclear conventions, and missing documentation, and well-structured projects enable better agent performance." Context overload — giving agents too much context — causes "confusion or quality degradation."
— O'Reilly Media, Coding for the Agentic World
URL: https://www.oreilly.com/AgenticWorld/
Date: September 2025

[STATISTIC]
Only 29% of organizations reported being prepared to secure agentic AI deployments. "Gartner predicts over 40% of agentic AI projects will be canceled by the end of 2027 due to escalating costs, unclear business value, or inadequate risk controls."
— Help Net Security, Enterprises Racing to Secure Agentic AI
URL: https://www.helpnetsecurity.com/2026/02/23/ai-agent-security-risks-enterprise/
URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
Date: February 2026 / June 2025

---

## Section 6: Comparison of Tool Claims vs. Independent Evaluations

This section places vendor-published metrics against independently-sourced evaluations. See [F03: Agentic Coding Current State] for detailed coverage of the benchmark-to-production gap across individual tool categories.

| Tool | Vendor Claim | Independent / Third-Party Finding | Source |
|---|---|---|---|
| Devin | "First AI software engineer"; 13.86% SWE-bench at launch | 3/20 tasks (15%) in Answer.AI month-long evaluation; 0/5 on modifying existing projects | https://www.answer.ai/posts/2025-01-08-devin.html |
| Cursor | "Helps complete tasks 2x faster"; 93% of engineers prefer it | 19% productivity slowdown in METR RCT with 16 experienced developers across 246 tasks | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| GitHub Copilot | 55% faster task completion (GitHub's 4,800-developer study) | Core developers reviewed 6.5% more code but showed 19% drop in original code productivity (arXiv 2510.10165) | https://arxiv.org/abs/2510.10165 |
| SWE-bench Verified top agents (~70–79%) | Top-line benchmark score | SWE-bench Pro reduces same models to 23–46%; private/unseen subset: GPT-5 drops to 14.9% | https://scale.com/leaderboard/swe_bench_pro_public |
| Factory Droid | 31x faster feature delivery (customer-reported) | #1 on Terminal-Bench (63.1%) — third-party benchmark, but not SWE-bench verified | https://www.tbench.ai/leaderboard/terminal-bench/2.0 |
| Replit Agent 3 | "Production-ready code" in any language/framework | No identified independent controlled evaluation; platform lock-in limits enterprise applicability | [UNVERIFIED — no independent study located] |

[FACT]
"Benchmark tasks are self-contained, don't require prior context to understand, and use algorithmic evaluation that doesn't capture many important capabilities." METR identified that benchmark-to-real-world gaps persist because real tasks require understanding organizational context, conventions, and non-algorithmic quality standards.
— METR, Research Update: Algorithmic vs. Holistic Evaluation
URL: https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/
Date: August 2025

[FACT]
"The evaluation measures the complete agent system — not just the model — including the prompt design, tool interfaces, and scaffolding that manages the interaction loop." Top SWE-bench Verified scores reflect agent + model + scaffolding combinations, not raw model capability.
— Anthropic, Claude SWE-Bench Performance
URL: https://www.anthropic.com/research/swe-bench-sonnet
Date: 2025

[FACT]
Developer trust in AI accuracy has declined year-over-year: from 40% to 29% in the 2025 Stack Overflow Developer Survey. Positive favorability declined from 72% to 60%.
— Stack Overflow 2025 Developer Survey
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

---

## Composite Capability Matrix

| Tool | Best Benchmark Score | Independent Eval | Autonomous Duration | Multi-repo | Enterprise Compliance |
|---|---|---|---|---|---|
| Claude Code | 82% SWE-bench Verified (parallel) | N/A (Anthropic-run) | 30+ hours documented | No | Anthropic API terms |
| Cursor | 8.0/10 Render test | METR: 19% slowdown on experienced devs | Session-based | No | SOC 2 Type 2, GDPR |
| GitHub Copilot | Not published on SWE-bench | 19% core-dev productivity drop (arXiv) | Async (no time limit) | No — explicit limit | SOC 2, GitHub Enterprise |
| Devin | 13.86% SWE-bench (2024) | Answer.AI: 15% (3/20 tasks) | Continuous (async) | Not documented | Enterprise plan |
| Factory Droid | 63.1% Terminal-Bench | Top-3 on Terminal-Bench | Not specified | Enterprise context retrieval | $50M raised; enterprise-stated |
| Replit Agent 3 | Not published | No independent study located | 200 minutes | No — platform-bound | Not documented |

---

## Key Takeaways

- **The benchmark-to-production gap is the defining reliability issue.** Top SWE-bench Verified scores reach 79–82%, but the same agents score 23–46% on SWE-bench Pro (multi-file, multi-language, enterprise-realistic problems), and independent controlled evaluations show 15% real-world task completion (Devin) and 19% productivity slowdown (Cursor with experienced developers).

- **Tool capability is highly task-type-dependent.** Bounded, verifiable, specification-clear tasks — security patching (20x faster), repository migration (10–14x faster), test generation (coverage 50%→80–90%), and boilerplate CRUD applications — show consistent positive outcomes. Ambiguous requirements, modifying existing codebases, and architectural decisions are documented failure modes across all major tools.

- **No current tool handles cross-repository or multi-system orchestration autonomously.** GitHub Copilot coding agent explicitly documents this as a hard limitation; Cursor operates single-repository per session; Devin's failure rate on modifying existing projects was 100% (0/5) in the Answer.AI evaluation.

- **Security is a structural failure mode, not a scaling problem.** AI-generated code contains security vulnerabilities in 45–62% of cases; Veracode's research found larger models do not perform significantly better than smaller models on security; Java-generated AI code fails security checks more than 70% of the time.

- **Scaffolding and orchestration account for a significant share of benchmark performance.** Factory Droid outperforms standalone Claude Code by 15+ percentage points on Terminal-Bench using the same underlying model, and Anthropic explicitly notes that SWE-bench scores measure "the complete agent system — not just the model." Raw model capability understates what purpose-built agent scaffolding adds.

---

## Sources

| # | Title | URL | Date |
|---|---|---|---|
| 1 | METR — Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | July 2025 |
| 2 | METR — Measuring AI Ability to Complete Long Tasks | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | March 2025 |
| 3 | METR — Research Update: Algorithmic vs. Holistic Evaluation | https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/ | August 2025 |
| 4 | Answer.AI — Thoughts On A Month With Devin | https://www.answer.ai/posts/2025-01-08-devin.html | January 2025 |
| 5 | Cognition AI — Devin's 2025 Performance Review | https://cognition.ai/blog/devin-annual-performance-review-2025 | 2025 |
| 6 | Cognition AI — SWE-bench Technical Report | https://cognition.ai/blog/swe-bench-technical-report | 2024 |
| 7 | Anthropic — Claude SWE-Bench Performance | https://www.anthropic.com/research/swe-bench-sonnet | 2025 |
| 8 | Anthropic — 2026 Agentic Coding Trends Report | https://resources.anthropic.com/2026-agentic-coding-trends-report | 2026 |
| 9 | InfoQ — Claude Sonnet 4.5 Tops SWE-Bench Verified | https://www.infoq.com/news/2025/10/claude-sonnet-4-5/ | October 2025 |
| 10 | Scale AI SEAL — SWE-Bench Pro Public Dataset | https://scale.com/leaderboard/swe_bench_pro_public | 2025–2026 |
| 11 | SWE-bench Official Leaderboard | https://www.swebench.com/ | 2026 |
| 12 | Factory.ai — Droid: #1 on Terminal-Bench | https://factory.ai/news/terminal-bench | September 2025 |
| 13 | Terminal-Bench Leaderboard | https://www.tbench.ai/leaderboard/terminal-bench/2.0 | 2025 |
| 14 | arXiv — Terminal-Bench Paper | https://arxiv.org/html/2601.11868v1 | 2025 |
| 15 | SiliconANGLE — Factory Droids $50M Funding | https://siliconangle.com/2025/09/25/factory-unleashes-droids-software-agents-50m-fresh-funding/ | September 2025 |
| 16 | NEA — Factory: The Platform for Agent-Native Development | https://www.nea.com/blog/factory-the-platform-for-agent-native-development | 2025 |
| 17 | Render Blog — AI Coding Agents Benchmark 2025 | https://render.com/blog/ai-coding-agents-benchmark | 2025 |
| 18 | GitHub Docs — About Copilot Coding Agent | https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | 2025 |
| 19 | GitHub Docs — Copilot Coding Agent How-To | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent | 2025 |
| 20 | DevOps.com — GitHub Copilot Agent Mode | https://devops.com/github-copilot-evolves-agent-mode-and-multi-model-support-transform-devops-workflows-2/ | 2025 |
| 21 | Second Talent — GitHub Copilot Statistics | https://www.secondtalent.com/resources/github-copilot-statistics/ | 2025 |
| 22 | Superblocks — Cursor Enterprise Review | https://www.superblocks.com/blog/cursor-enterprise | 2026 |
| 23 | Artezio — Cursor 2.0 Multi-Agent Architecture | https://www.artezio.com/pressroom/blog/revolutionizes-architecture-proprietary/ | 2025 |
| 24 | InfoQ — Replit Introduces Agent 3 | https://www.infoq.com/news/2025/09/replit-agent-3/ | September 2025 |
| 25 | Replit — Agent Documentation | https://docs.replit.com/replitai/agent | 2025 |
| 26 | Replit Blog — 2025 in Review | https://blog.replit.com/2025-replit-in-review | 2025 |
| 27 | arXiv — AI-Assisted Programming Decreases Productivity (Xu et al.) | https://arxiv.org/abs/2510.10165 | October 2025 |
| 28 | Stack Overflow Blog — Developers Remain Willing but Reluctant | https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/ | December 2025 |
| 29 | Stack Overflow Blog — Are Bugs Inevitable with AI Coding Agents? | https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents | January 2026 |
| 30 | Cloud Security Alliance — AI-Generated Code Security Risks | https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code | July 2025 |
| 31 | Veracode — 2025 GenAI Code Security Report | https://www.veracode.com/blog/genai-code-security-report/ | 2025 |
| 32 | Apiiro — 4x Velocity, 10x Vulnerabilities | https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/ | 2025 |
| 33 | Factory.ai — The Context Window Problem | https://factory.ai/news/context-window-problem | 2025 |
| 34 | David Lozzi — The Reality Behind the Buzz: Agentic Engineering 2025 | https://davidlozzi.com/2025/08/20/the-reality-behind-the-buzz-the-current-state-of-agentic-engineering-in-2025/ | August 2025 |
| 35 | MarkTechPost — Microsoft Failure Modes in Agentic AI | https://www.marktechpost.com/2025/04/27/microsoft-releases-a-comprehensive-guide-to-failure-modes-in-agentic-ai-systems/ | April 2025 |
| 36 | Gartner — 40% of Agentic AI Projects Canceled by 2027 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | June 2025 |
| 37 | Help Net Security — Enterprises Racing to Secure Agentic AI | https://www.helpnetsecurity.com/2026/02/23/ai-agent-security-risks-enterprise/ | February 2026 |
| 38 | O'Reilly — Coding for the Agentic World | https://www.oreilly.com/AgenticWorld/ | September 2025 |
| 39 | Flatlogic — Top 10+ Agentic App Builders 2025 | https://flatlogic.com/blog/top-10-agentic-app-builders/ | 2025 |
| 40 | LLM Stats — HumanEval / SWE-bench Benchmark Scores | https://llm-stats.com/benchmarks/swe-bench-verified | 2025 |
| 41 | DeepEval — HumanEval Documentation | https://deepeval.com/docs/benchmarks-human-eval | 2025 |
