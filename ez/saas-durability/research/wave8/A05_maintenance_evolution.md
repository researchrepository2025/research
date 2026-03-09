# A05: Agentic Coding Tools — Maintenance and Long-Term Software Evolution

**Research Area:** Wave 8 — Lifecycle and Durability
**Date Compiled:** 2026-03-06
**Scope:** Bug fixing, feature iteration, technical debt accumulation, dependency management, code comprehension, and lifecycle cost trajectory for AI-generated codebases. Excludes initial creation capabilities (see A01) and TCO modeling in depth (see Wave 9).

---

## Executive Summary

Agentic coding tools demonstrate measurable capability on isolated, bounded software engineering tasks — autonomous bug resolution on SWE-bench Verified reached 76.8% by February 2026 — yet performance collapses dramatically on the long-horizon, multi-file, and contextually complex tasks that define real enterprise maintenance. On SWE-EVO, a benchmark designed specifically for software evolution rather than one-shot bug fixing, GPT-5 resolved only 21% of tasks versus 65% on SWE-bench Verified, exposing a structural capability gap at the maintenance layer. The code AI tools produce accumulates technical debt at an accelerating rate: GitClear's analysis of 211 million changed lines found code clones increased 4x during 2024 and refactoring activity dropped from 25% to under 10% of all changed lines. A distinct form of organizational liability — comprehension debt, the growing gap between what teams have shipped and what they understand — is emerging as a durability risk that falls outside traditional technical debt accounting. Senior practitioners and analyst firms have coalesced around 2026–2027 as the period when accumulated AI-generated technical debt will reach crisis levels in organizations that did not implement governance controls at the point of generation.

---

## Section 1: Bug Fixing and Patching Capabilities

### 1.1 Benchmark Performance on Isolated Bug Fixing

[STATISTIC]
"Claude 4.5 Opus (high reasoning)" achieved 76.8% on SWE-bench Verified as of the February 2026 leaderboard update; Gemini 3 Flash and MiniMax M2.5 each scored 75.8%; GPT-5.2 (high reasoning) scored 72.8%
— Simon Willison, "SWE-bench February 2026 leaderboard update"
URL: https://simonwillison.net/2026/Feb/19/swe-bench/
Date: February 19, 2026

[DATA POINT]
SWE-bench Verified dataset parameters: 500 manually curated samples drawn from 12 open-source repositories, with Django comprising the largest portion (231 samples); models evaluated on ability to investigate and modify repositories to resolve real GitHub issues
— Epoch AI, "SWE-bench Verified" benchmark page
URL: https://epoch.ai/benchmarks/swe-bench-verified
Date: 2025–2026

[STATISTIC]
"AI bug resolution on SWE-bench improved from 4.4% in 2023 to 69.1% in 2025"
— Cited in: Allstacks, "Comprehension Debt: The Hidden Cost of AI-Generated Code"
URL: https://www.allstacks.com/blog/comprehension-debt-the-hidden-cost-of-ai-generated-code
Date: 2025

[FACT]
Harness AI achieved a top-4 ranking on the SWE-bench Verified leaderboard using an architecture combining Claude 4 Sonnet in "Thinking Mode," a Build & Test Agent, and a Fixing Agent with six core tool types; benchmark evaluated "500 real GitHub issues across production-grade Python repos. No hints. No scaffolding. Just raw code, and a single attempt."
— Harness AI, "Harness Excels in SWE-Bench Verified"
URL: https://www.harness.io/blog/harness-excels-in-swe-bench-verified
Date: 2025

### 1.2 The Benchmark-to-Production Gap in Bug Fixing

[STATISTIC]
On SWE-Bench Pro — designed to reflect enterprise-level complexity with 1,865 problems across 41 repositories — Claude Sonnet 4.5 achieved 43.6% on the public set and only 9.1% on the commercial (proprietary codebase) set; Claude Opus 4.1 achieved 17.8% on the commercial set
— SWE-Bench Pro, Scale AI SEAL Leaderboard; arXiv:2509.16941
URL: https://arxiv.org/html/2509.16941
Date: September 2025

[DATA POINT]
SWE-Bench Pro commercial set composition: 276 instances drawn from 18 startup repositories with proprietary code; problems require "long-horizon tasks that may require hours to days for a professional software engineer to complete, often involving patches across multiple files and substantial code modifications"
— arXiv:2509.16941, "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?"
URL: https://arxiv.org/abs/2509.16941
Date: September 2025

[STATISTIC]
When human-provided requirements and interface specifications were removed from SWE-Bench Pro inputs, GPT-5 (high) performance declined from 25.9% to 8.4% — a 67% performance drop from the absence of specification context alone
— arXiv:2509.16941, "SWE-Bench Pro"
URL: https://arxiv.org/html/2509.16941
Date: September 2025

[FACT]
SWE-Bench Pro failure analysis found that "frontier models struggle primarily with semantic understanding and problem interpretation rather than syntax or tool usage"
— arXiv:2509.16941
URL: https://arxiv.org/html/2509.16941
Date: September 2025

---

## Section 2: Feature Evolution and Iteration Capabilities

### 2.1 Long-Horizon Software Evolution Benchmarks

[STATISTIC]
On SWE-EVO — a benchmark designed for long-horizon software evolution rather than one-shot bug fixing — GPT-5 achieved only 21% resolution versus 65% on SWE-bench Verified; the authors describe "a striking capability gap between isolated bug-fixing and long-horizon evolution tasks"
— arXiv:2512.18470, "SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios"
URL: https://arxiv.org/html/2512.18470v1
Date: December 2025

[DATA POINT]
SWE-EVO benchmark characteristics: 48 tasks across 7 Python repositories; average gold patch spans 21 files, 610.5 lines of code edited, 874 tests per instance, 2,390.5 words in problem statements — substantially larger scope than single-issue benchmarks
— arXiv:2512.18470
URL: https://arxiv.org/html/2512.18470v1
Date: December 2025

[STATISTIC]
Full SWE-EVO model resolution rates with PR/issue context: GPT-5-08-07 18.75–20.83%; Kimi-K2 16.67–18.75%; GLM-4p5 16.67%; Qwen3-Coder 14.58%; GPT-5-mini 10.42%; Deepseek-R1 8.33–10.42%; GPT-5-nano 4.17%
— arXiv:2512.18470
URL: https://arxiv.org/html/2512.18470v1
Date: December 2025

[FACT]
SWE-EVO failure mode analysis found that for the strongest models (GPT-5 class), "60%+ failures stem from 'Instruction Following' errors"; providing PR/issue context yielded "modest gains" but "agents still struggle to reconstruct correct implementations even with detailed specifications"
— arXiv:2512.18470
URL: https://arxiv.org/html/2512.18470v1
Date: December 2025

### 2.2 Practitioner Evidence on Feature Iteration

[FACT]
Rakuten used Claude Code to complete a complex vLLM implementation across a 12.5 million line codebase in 7 hours with "99.9% numerical accuracy" — cited as an enterprise-scale evidence case for agentic maintenance capability
— Cited in: Augment Code, "AI Tools for Large Codebase Analysis (Enterprise Picks)"
URL: https://www.augmentcode.com/tools/ai-tools-for-large-codebase-analysis-enterprise-picks
Date: 2025–2026

[FACT]
Andrej Karpathy reported transitioning "from 80% manual+autocomplete coding and 20% agents to 80% agent coding and 20% edits+touchups" in late 2025; Boris Cherny noted "100% of our code is written by Claude Code + Opus 4.5" for two-plus months, shipping "22 PRs yesterday and 27 the day before"
— Addy Osmani, "The 80% Problem in Agentic Coding"
URL: https://addyo.substack.com/p/the-80-problem-in-agentic-coding
Date: 2025

[QUOTE]
"The 80% threshold works best in personal/greenfield projects, MVPs prioritizing speed over perfection, and small teams managing comprehension debt. Struggles intensify in mature codebases with complex invariants where agents lack contextual understanding of unwritten rules."
— Addy Osmani, "The 80% Problem in Agentic Coding"
URL: https://addyo.substack.com/p/the-80-problem-in-agentic-coding
Date: 2025

[STATISTIC]
44% of developers now write less than 10% of code manually; 26% write between 10–50% manually; only 16% reported "great" productivity improvements; 50% saw modest gains; remaining saw minimal improvement
— Addy Osmani, "The 80% Problem in Agentic Coding," citing Stack Overflow 2025 data
URL: https://addyo.substack.com/p/the-80-problem-in-agentic-coding
Date: 2025

---

## Section 3: Technical Debt Accumulation in AI-Generated Codebases

### 3.1 Measured Code Quality Degradation Trends

[STATISTIC]
GitClear analysis of 211 million changed code lines (2020–2024): code duplication increased 48% (copy-pasted code rising from 8.3% to 12.3% of changed lines); refactoring activity declined 60% (from 25% to under 10% of changed lines); code churn increased 41%
— GitClear, "AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones"
URL: https://www.gitclear.com/ai_assistant_code_quality_2025_research
Date: 2025

[STATISTIC]
"Code clones increased 4x during 2024" — the single-year acceleration is distinguished from the multi-year trend above
— GitClear, 2025 AI Copilot Code Quality Report
URL: https://www.gitclear.com/ai_assistant_code_quality_2025_research
Date: 2025

[STATISTIC]
"Projects using excessive AI-generated code experienced a 41% rise in bugs"
— index.dev, "Top 100 Developer Productivity Statistics with AI Tools 2026"
URL: https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
Date: 2026

[STATISTIC]
"10-fold increase in security findings: 1,000/month (December 2024) to 10,000+ per month (June 2025)"
— Pixelmojo, "The AI Coding Technical Debt Crisis: What 2026–2027 Holds"
URL: https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027
Date: 2026

[STATISTIC]
256 billion lines of AI code were generated globally in 2024; 41% of all new code is AI-generated
— Pixelmojo, "The AI Coding Technical Debt Crisis: What 2026–2027 Holds"
URL: https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027
Date: 2026

### 3.2 Structural Anti-Patterns in AI-Generated Code

[DATA POINT]
Ox Security "Army of Juniors: The AI Code Security Crisis" study parameters: 300 open-source repositories analyzed; 50 projects wholly or partially AI-generated; evaluated for architectural and security quality
— Ox Security / PR Newswire
URL: https://www.prnewswire.com/news-releases/ox-report-ai-generated-code-violates-engineering-best-practices-undermining-software-security-at-scale-302592642.html
Date: October 2025

[STATISTIC]
Ox Security identified 10 critical anti-patterns with the following prevalence in AI-generated code:

| Anti-Pattern | Prevalence Rate | Maintenance Impact |
|---|---|---|
| Comments Everywhere | 90–100% | Increases computational review burden |
| By-The-Book Fixation | 80–90% | Misses non-standard but correct solutions |
| Avoidance of Refactors | 80–90% | Generates functional code without architectural improvement |
| Over-Specification | 80–90% | Single-use solutions instead of reusable components |
| Bugs Déjà-Vu | 70–80% | Identical bugs recur; no code reuse principle applied |
| "Worked on My Machine" Syndrome | 60–70% | Code fails in production environments |
| Return of Monoliths | 40–50% | Tightly-coupled architectures reversing microservices progress |
| Fake Test Coverage | 40–50% | Tests lack meaningful validation logic |
| Vanilla Style | 40–50% | Reimplements from scratch vs. established libraries |
| Phantom Bugs | 20–30% | Over-engineers for improbable edge cases |

— Ox Security, "Army of Juniors: The AI Code Security Crisis"
URL: https://www.prnewswire.com/news-releases/ox-report-ai-generated-code-violates-engineering-best-practices-undermining-software-security-at-scale-302592642.html
Date: October 2025

[QUOTE]
"Functional applications can now be built faster than humans can properly evaluate them."
— Eyal Paz, VP of Research, Ox Security
URL: https://www.prnewswire.com/news-releases/ox-report-ai-generated-code-violates-engineering-best-practices-undermining-software-security-at-scale-302592642.html
Date: October 2025

[QUOTE]
"Code review simply cannot scale to match the new output velocity."
— Ox Security, "Army of Juniors" report
URL: https://www.prnewswire.com/news-releases/ox-report-ai-generated-code-violates-engineering-best-practices-undermining-software-security-at-scale-302592642.html
Date: October 2025

### 3.3 Compounding Debt Timeline

[QUOTE]
"Traditional technical debt accumulates linearly...AI technical debt is different. It compounds."
— Ana Bildea, "The Hidden Technical Debt Inside Your Generative AI Stack," cited in InfoQ
URL: https://www.infoq.com/news/2025/11/ai-code-technical-debt/
Date: November 2025

[QUOTE]
"I've watched companies go from 'AI is accelerating our development' to 'we can't ship features because we don't understand our own systems' in less than 18 months."
— Ana Bildea, cited in InfoQ, "AI-Generated Code Creates New Wave of Technical Debt"
URL: https://www.infoq.com/news/2025/11/ai-code-technical-debt/
Date: November 2025

[FACT]
"Vicki Abraham (Salesforce): '2026 is the year of technical debt...we're producing tech debt on top of tech debt.'"
— Pixelmojo, "The AI Coding Technical Debt Crisis: What 2026–2027 Holds"
URL: https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027
Date: 2026

[STATISTIC]
"Gartner predicts 40% of AI-augmented coding projects will be canceled by 2027 due to escalating costs, unclear business value, and weak risk controls"
— Codebridge, "The Hidden Costs of AI-Generated Software: Why 'It Works' Isn't Enough"
URL: https://www.codebridge.tech/articles/the-hidden-costs-of-ai-generated-software-why-it-works-isnt-enough
Date: 2026

[STATISTIC]
Forrester predicts that "by 2025, more than 50% of technology decision-makers will face moderate to severe technical debt," with that number "expected to hit 75% by 2026"
— Pixelmojo, "The AI Coding Technical Debt Crisis"
URL: https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027
Date: 2026

---

## Section 4: Dependency Management and Updates

### 4.1 Automation Capability

[FACT]
AI systems now continuously monitor repositories and package registries for updates or breaking changes, cross-reference CVE databases and dependency trees to flag risky libraries, predict which updates will likely cause build failures, and automatically generate and test pull requests with changelogs
— Sonatype, "The Future of Dependency Management in an AI-Driven SDLC"
URL: https://www.sonatype.com/blog/the-future-of-dependency-management-in-an-ai-driven-sdlc
Date: February 2026

### 4.2 Model Knowledge Lag Problem

[QUOTE]
"Model knowledge can lag behind current library health, security posture, end-of-life status, and best-practice guidance."
— Sonatype, "The Future of Dependency Management in an AI-Driven SDLC"
URL: https://www.sonatype.com/blog/the-future-of-dependency-management-in-an-ai-driven-sdlc
Date: February 2026

[QUOTE]
"The biggest supply chain shift isn't just that AI generates code. It's that AI can recommend libraries, frameworks, and versions at the moment a developer implements a solution."
— Sonatype, "The Future of Dependency Management in an AI-Driven SDLC"
URL: https://www.sonatype.com/blog/the-future-of-dependency-management-in-an-ai-driven-sdlc
Date: February 2026

[QUOTE]
"Policy, risk management, and control frameworks often follow after adoption, rather than preceding it."
— Sonatype, "The Future of Dependency Management in an AI-Driven SDLC"
URL: https://www.sonatype.com/blog/the-future-of-dependency-management-in-an-ai-driven-sdlc
Date: February 2026

### 4.3 Current Dependency Lag Metrics

[STATISTIC]
"The median dependency now trails its latest major version by 278 days, compared with 215 days last year" — a widening delay in adoption cycles despite AI automation advances
— Help Net Security, "Your dependencies are 278 days out of date and your pipelines aren't protected"
URL: https://www.helpnetsecurity.com/2026/03/02/devsecops-supply-chain-risk-security-debt/
Date: March 2, 2026

[STATISTIC]
"Roughly 20% of package dependencies suggested by AI do not exist in official repositories"
— Codebridge, "The Hidden Costs of AI-Generated Software"
URL: https://www.codebridge.tech/articles/the-hidden-costs-of-ai-generated-software-why-it-works-isnt-enough
Date: 2026

---

## Section 5: Code Comprehension — Can AI Tools Understand and Modify Existing AI-Generated Code?

### 5.1 Comprehension Debt as a Distinct Liability Category

[QUOTE]
"Comprehension debt is the growing gap between the code your team has shipped and the code your team actually understands. Unlike technical debt, comprehension debt is often invisible — until something breaks and nobody knows why."
— Allstacks, "Comprehension Debt: The Hidden Cost of AI-Generated Code"
URL: https://www.allstacks.com/blog/comprehension-debt-the-hidden-cost-of-ai-generated-code
Date: 2025

[QUOTE]
"AI code review currently functions as an advanced linter, but lacks the contextual and architectural understanding of a human reviewer."
— Allstacks, "Comprehension Debt: The Hidden Cost of AI-Generated Code"
URL: https://www.allstacks.com/blog/comprehension-debt-the-hidden-cost-of-ai-generated-code
Date: 2025

[QUOTE]
"You can't be responsible for code you don't understand. But you're responsible anyway."
— Allstacks, "Comprehension Debt: The Hidden Cost of AI-Generated Code"
URL: https://www.allstacks.com/blog/comprehension-debt-the-hidden-cost-of-ai-generated-code
Date: 2025

[FACT]
Allstacks identifies 6 organizational warning signs of comprehension debt accumulation: PR review times decreasing (rubber-stamping), tests becoming the sole approval criteria, onboarding difficulty increasing, incident resolution times rising, architecture decisions being attributed to AI, and senior engineers reviewing more than writing
— Allstacks, "Comprehension Debt: The Hidden Cost of AI-Generated Code"
URL: https://www.allstacks.com/blog/comprehension-debt-the-hidden-cost-of-ai-generated-code
Date: 2025

### 5.2 AI Self-Comprehension Limitations

[QUOTE]
"AI doesn't remember your architecture. Every prompt is a fresh start."
— DEV Community, "The Vibe Coding Hangover Is Real: What Nobody Tells You About AI-Generated Code in Production"
URL: https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
Date: 2025

[QUOTE]
"In mature codebases with complex invariants, the agent doesn't know what it doesn't know — it can't intuit the unwritten rules and its confidence scales inversely with context understanding."
— Addy Osmani, "The 80% Problem in Agentic Coding"
URL: https://addyo.substack.com/p/the-80-problem-in-agentic-coding
Date: 2025

[STATISTIC]
"65% say AI misses relevant context during refactoring"; "60% report context gaps in testing and code review tasks"
— Qodo, State of AI Code Quality 2025
URL: https://www.qodo.ai/reports/state-of-ai-code-quality/
Date: 2025

[FACT]
Three specific failure modes identified in agentic maintenance tasks: assumption propagation (models make incorrect early assumptions and build on faulty premises without clarification), comprehension debt (gap between code generation speed and developer comprehension capacity creating rubber-stamping risk), abstraction bloat (agents create unnecessarily complex implementations)
— Addy Osmani, "The 80% Problem in Agentic Coding"
URL: https://addyo.substack.com/p/the-80-problem-in-agentic-coding
Date: 2025

### 5.3 Review Bottlenecks Created by AI Output Volume

[STATISTIC]
"Only 48% of developers consistently check AI-assisted code before committing"; "38% find reviewing AI-generated logic requires more effort than human-written code"
— Addy Osmani, "The 80% Problem in Agentic Coding"
URL: https://addyo.substack.com/p/the-80-problem-in-agentic-coding
Date: 2025

[STATISTIC]
"PR review time jumped 91%" when "PR volume surged 98% among high-AI-adoption teams"; "Average pull request size increased 154%"
— Faros AI, citing Bain & Company Technology Report 2025
URL: https://www.faros.ai/blog/bain-technology-report-2025-why-ai-gains-are-stalling
Date: 2025

See [D06: Developer Experience Reports] for detailed coverage of the code quality defect multipliers and the broader organizational productivity paradox (Bain & Company data on PR volume vs. company-wide delivery metrics).

---

## Section 6: Lifecycle Cost Implications — Creation Cost vs. Maintenance Cost Trajectory

### 6.1 The 18-Month Cost Curve

[FACT]
Codebridge identifies a four-phase lifecycle cost pattern for AI-generated codebases:
- Months 1–3: Feature delivery accelerates
- Months 4–9: Integration challenges; velocity plateau begins
- Months 10–15: Decline acceleration; debugging legacy AI components
- Months 16–18: "Delivery cycles stall because teams no longer fully understand their own systems"
— Codebridge, "The Hidden Costs of AI-Generated Software"
URL: https://www.codebridge.tech/articles/the-hidden-costs-of-ai-generated-software-why-it-works-isnt-enough
Date: 2026

[STATISTIC]
"By year two, unmanaged AI-generated code drives maintenance costs to four times traditional levels as technical debt compounds"
— Codebridge, "The Hidden Costs of AI-Generated Software"
URL: https://www.codebridge.tech/articles/the-hidden-costs-of-ai-generated-software-why-it-works-isnt-enough
Date: 2026

[STATISTIC]
Recommended enterprise allocation to remediate AI-generated technical debt: "20–30% of engineering capacity budgeted for debt remediation"
— Pixelmojo, "The AI Coding Technical Debt Crisis: What 2026–2027 Holds"
URL: https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027
Date: 2026

### 6.2 Maintenance Burden Falls on Expert Developers

[STATISTIC]
"Core developers review 6.5% more code after Copilot's introduction, but show a 19% drop in their original code productivity"
— arXiv preprint 2510.10165, "AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden"
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[FACT]
arXiv preprint 2510.10165 identifies a "fundamental tension in AI-assisted software development between short-term productivity gains and long-term system sustainability" and warns that "productivity increases may obscure growing maintenance burdens on a limited pool of expert developers"
— arXiv:2510.10165
URL: https://arxiv.org/abs/2510.10165
Date: October 2025

[STATISTIC]
"66% of developers say they are spending more time fixing 'almost-right' AI-generated code"; "45% find debugging AI-generated code more time-consuming"
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"Debugging AI Code Takes 45% More Time" than human-written code
— index.dev, "Top 100 Developer Productivity Statistics with AI Tools 2026"
URL: https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
Date: 2026

### 6.3 Projected Debt Accumulation

[STATISTIC]
Projected $1.5 trillion in technical debt from AI-generated code by 2027
— DEV Community, "The Vibe Coding Hangover Is Real"
URL: https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
Date: 2025

[STATISTIC]
"54% of engineering leaders plan to hire fewer junior developers" in response to AI coding adoption
— Pixelmojo, "The AI Coding Technical Debt Crisis: What 2026–2027 Holds"
URL: https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027
Date: 2026

[QUOTE]
"Most companies are optimizing for the wrong metrics. They're measuring AI adoption rates and feature velocity while ignoring technical debt accumulation."
— Ana Bildea, cited in InfoQ, "AI-Generated Code Creates New Wave of Technical Debt"
URL: https://www.infoq.com/news/2025/11/ai-code-technical-debt/
Date: November 2025

---

## Benchmark Performance Summary Table

| Benchmark | Design Focus | Top Model Score | Key Limitation Exposed |
|---|---|---|---|
| SWE-bench Verified | Single-issue bug fixes, curated repos | 76.8% (Claude 4.5 Opus, Feb 2026) | Does not reflect proprietary codebases |
| SWE-Bench Pro (Public) | Enterprise-complexity, 1,865 problems | 43.6% (Claude Sonnet 4.5) | 41 repos, long-horizon patches |
| SWE-Bench Pro (Commercial) | Proprietary startup codebases | 17.8% (Claude Opus 4.1) | Real enterprise codebase opacity |
| SWE-EVO | Long-horizon software evolution, 48 tasks | 20.83% (GPT-5) | Multi-file, multi-test evolution tasks |
| FeatureBench | End-to-end feature development | 11.0% (Claude 4.5 Opus) | Feature creation vs. isolated fixes |

Sources: arXiv:2509.16941; arXiv:2512.18470v1; simonwillison.net (Feb 2026); cited in Allstacks (2025)

---

## Key Takeaways

- **Benchmark capability does not translate to maintenance capability.** AI agents resolve over 70% of isolated bug-fixing tasks on curated benchmarks (SWE-bench Verified, February 2026), but performance drops to 9–18% on proprietary codebases (SWE-Bench Pro commercial set) and 21% on long-horizon evolution tasks (SWE-EVO). The architecture that enables rapid single-issue resolution — context-free, stateless prompting — is structurally misaligned with iterative software maintenance, which requires sustained architectural memory across sessions.

- **Technical debt accumulation is accelerating, not decelerating, with AI adoption.** GitClear's analysis of 211 million changed lines found code duplication up 4x in a single year (2024) while refactoring activity fell from 25% to under 10% of changed lines. Ox Security found 9 of 10 structural anti-patterns present in 70–100% of AI-generated code, with avoidance of refactors appearing in 80–90% of cases — directly blocking the maintenance activity that keeps codebases evolvable.

- **A new liability category — comprehension debt — is not captured in standard technical debt accounting.** AI-generated code can pass automated tests while remaining opaque to the humans responsible for it. The 18-month failure pattern documented by Codebridge (acceleration → plateau → stall) maps to organizational comprehension collapse, not code functionality. By year two, unmanaged AI-generated codebases are projected to drive maintenance costs to four times traditional levels.

- **Dependency management automation is advancing but introduces new model-knowledge failure modes.** AI tools can now auto-generate dependency update PRs with changelogs, yet model training lag means AI recommendations may reference libraries with stale security posture or end-of-life status. The median dependency trails its latest major version by 278 days as of March 2026 — a figure that has grown, not shrunk, despite automation.

- **Maintenance burden concentrates on the most expensive and scarce talent.** arXiv:2510.10165 documents a 19% drop in experienced developer original code productivity alongside a 6.5% increase in their review load. Combined with Bain's finding of a 91% jump in PR review time among high-AI-adoption teams and Stack Overflow data showing 66% of developers spending more time fixing AI-generated code, the evidence indicates agentic tools have shifted work from generation to review and remediation — a transfer that falls disproportionately on senior engineers.

---

## Sources

1. Simon Willison, "SWE-bench February 2026 leaderboard update": https://simonwillison.net/2026/Feb/19/swe-bench/
2. Epoch AI, "SWE-bench Verified" benchmark: https://epoch.ai/benchmarks/swe-bench-verified
3. arXiv:2509.16941, "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?": https://arxiv.org/abs/2509.16941
4. arXiv:2509.16941 HTML full text: https://arxiv.org/html/2509.16941
5. arXiv:2512.18470, "SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios": https://arxiv.org/html/2512.18470v1
6. Harness AI, "Harness Excels in SWE-Bench Verified": https://www.harness.io/blog/harness-excels-in-swe-bench-verified
7. GitClear, "AI Copilot Code Quality: 2025 Data Suggests 4x Growth in Code Clones": https://www.gitclear.com/ai_assistant_code_quality_2025_research
8. Ox Security / PR Newswire, "OX Report: AI-Generated Code Violates Engineering Best Practices": https://www.prnewswire.com/news-releases/ox-report-ai-generated-code-violates-engineering-best-practices-undermining-software-security-at-scale-302592642.html
9. Ox Security, "Army of Juniors: The AI Code Security Crisis" (full report PDF): https://www.ox.security/wp-content/uploads/2025/10/Army-of-Juniors-The-AI-Code-Security-Crisis.pdf
10. InfoQ, "AI-Generated Code Creates New Wave of Technical Debt": https://www.infoq.com/news/2025/11/ai-code-technical-debt/
11. Pixelmojo, "The AI Coding Technical Debt Crisis: What 2026–2027 Holds": https://www.pixelmojo.io/blogs/vibe-coding-technical-debt-crisis-2026-2027
12. Codebridge, "The Hidden Costs of AI-Generated Software: Why 'It Works' Isn't Enough": https://www.codebridge.tech/articles/the-hidden-costs-of-ai-generated-software-why-it-works-isnt-enough
13. Allstacks, "Comprehension Debt: The Hidden Cost of AI-Generated Code": https://www.allstacks.com/blog/comprehension-debt-the-hidden-cost-of-ai-generated-code
14. Addy Osmani, "The 80% Problem in Agentic Coding": https://addyo.substack.com/p/the-80-problem-in-agentic-coding
15. Sonatype, "The Future of Dependency Management in an AI-Driven SDLC": https://www.sonatype.com/blog/the-future-of-dependency-management-in-an-ai-driven-sdlc
16. Help Net Security, "Your dependencies are 278 days out of date and your pipelines aren't protected": https://www.helpnetsecurity.com/2026/03/02/devsecops-supply-chain-risk-security-debt/
17. Faros AI, "Bain Technology Report 2025: Why AI Gains Are Stalling": https://www.faros.ai/blog/bain-technology-report-2025-why-ai-gains-are-stalling
18. arXiv:2510.10165, "AI-Assisted Programming Decreases the Productivity of Experienced Developers": https://arxiv.org/abs/2510.10165
19. Stack Overflow 2025 Developer Survey — AI section: https://survey.stackoverflow.co/2025/ai/
20. index.dev, "Top 100 Developer Productivity Statistics with AI Tools 2026": https://www.index.dev/blog/developer-productivity-statistics-with-ai-tools
21. Qodo, "State of AI Code Quality 2025": https://www.qodo.ai/reports/state-of-ai-code-quality/
22. DEV Community (paulthedev), "The Vibe Coding Hangover Is Real": https://dev.to/paulthedev/the-vibe-coding-hangover-is-real-what-nobody-tells-you-about-ai-generated-code-in-production-399h
23. Augment Code, "AI Tools for Large Codebase Analysis (Enterprise Picks)": https://www.augmentcode.com/tools/ai-tools-for-large-codebase-analysis-enterprise-picks
