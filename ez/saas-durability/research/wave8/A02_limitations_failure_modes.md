# A02: Systematic Limitations and Failure Modes of Agentic Coding for Enterprise Application Development

**Wave:** 8 | **Research Date:** 2026-03-06 | **Audience:** C-Suite

---

## Executive Summary

Agentic coding tools in 2025–2026 introduce measurable, quantified failure modes that challenge their safe deployment in enterprise application development. Security vulnerabilities introduced by AI-generated code have spiked 10x in six months at Fortune 50 enterprises, package hallucination rates average 19.7% across all tested LLMs, and the 2024 Google DORA report documented that a 25% increase in AI adoption correlated with a 7.2% decrease in software delivery stability. Developer trust in AI accuracy has fallen to an all-time low, with 46% of developers now actively distrusting AI output accuracy versus 33% who trust it, according to Stack Overflow's 2025 survey of over 65,000 developers. These data points collectively demonstrate that the productivity gains attributed to agentic coding carry compounding risks to code quality, security posture, and system reliability that enterprise leaders must quantify before broad deployment.

---

## 1. Hallucination and Incorrect Code Generation Rates

### 1.1 Package Hallucinations

[STATISTIC]
"19.7% of the generated packages are fictitious" across all tested models, with 205,474 unique non-existent package names identified from 2.23 million total packages generated.
— Spracklen, J., Wijewickrama, R., Sakib, A.H.M.N., Maiti, A., Viswanath, B., and Jadliwala, M. (University of Texas at San Antonio, University of Oklahoma, Virginia Tech)
URL: https://arxiv.org/html/2406.10279v3
Date: Published USENIX Security 2025

[STATISTIC]
"The average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models."
— Spracklen et al.
URL: https://arxiv.org/html/2406.10279v3
Date: USENIX Security 2025

[STATISTIC]
GPT-4 Turbo achieved the lowest hallucination rate among all tested models at 3.59%.
— Spracklen et al.
URL: https://arxiv.org/html/2406.10279v3
Date: USENIX Security 2025

[STATISTIC]
Python code showed a 15.8% average package hallucination rate; JavaScript code showed a 21.3% average rate, across the same study using 16 LLMs and 576,000 generated code samples.
— Spracklen et al.
URL: https://arxiv.org/html/2406.10279v3
Date: USENIX Security 2025

[FACT]
"Package hallucinations are a persistent and systemic phenomenon" affecting all tested models, representing a critical software supply chain vulnerability described as "slopsquatting" — a variant of typosquatting exploiting LLM-generated phantom package names.
— Spracklen et al.
URL: https://www.usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code
Date: 2025

[STATISTIC]
58% of hallucinated packages were repeated more than once across ten runs of the same prompt, indicating hallucinations are "not just random noise, but repeatable artifacts."
— Spracklen et al.
URL: https://arxiv.org/html/2406.10279v3
Date: USENIX Security 2025

### 1.2 Code Logic and Correctness Errors

[STATISTIC]
AI-created pull requests had 75% more logic and correctness errors, at 194 occurrences per 100 pull requests.
— CodeRabbit, "State of AI vs. Human Code Generation Report" (analysis of 470 open-access GitHub repositories)
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 28, 2026

[STATISTIC]
AI created 1.7 times as many bugs as humans overall; 1.3–1.7 times more critical and major issues specifically.
— CodeRabbit, "State of AI vs. Human Code Generation Report"
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 28, 2026

[STATISTIC]
Additional code quality differentials from the same CodeRabbit study: readability issues 3x higher in AI code; formatting problems 2.66x more frequent; naming inconsistencies 2x more common; excessive I/O operations approximately 8x higher; concurrency and dependency errors 2x more likely; error/exception handling deficiencies nearly 2x more likely.
— CodeRabbit, "State of AI vs. Human Code Generation Report"
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 28, 2026

### 1.3 Hallucination Taxonomy (Academic Classification)

[FACT]
The CodeMirage benchmark (arxiv 2408.08333) classifies five hallucination categories in LLM-generated code: Dead/Unreachable Code, Syntactic Incorrectness, Logical Error, Robustness Issue (edge case failures), and Security Vulnerabilities.
— CodeMirage paper, arxiv
URL: https://arxiv.org/abs/2408.08333
Date: August 2024

---

## 2. Context Window Limitations and Their Impact on Large Codebases

### 2.1 The Hard Ceiling

[FACT]
Frontier LLMs offer context windows of no more than 1–2 million tokens, accommodating "a few thousand code files, which is still less than most production codebases of enterprise customers."
— Varin Nair, Factory.ai
URL: https://factory.ai/news/context-window-problem
Date: August 25, 2025

[FACT]
A typical enterprise monorepo can span thousands of files and several million tokens — exceeding the maximum context window of any currently available frontier model.
— Varin Nair, Factory.ai
URL: https://factory.ai/news/context-window-problem
Date: August 25, 2025

### 2.2 Context Rot: Performance Degradation Within the Window

[FACT]
Chroma Research published a study in July 2025 evaluating 18 state-of-the-art LLMs — including Claude Opus 4, Claude Sonnet 4, GPT-4.1, o3, Gemini 2.5 Pro, and Qwen3-235B — and found "models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows."
— Hong et al., Chroma Research (cited by Varin Nair, Factory.ai)
URL: https://research.trychroma.com/context-rot
Date: July 2025

[FACT]
The Chroma study found three mechanisms behind context rot: the "lost in the middle" effect (strong attention at sequence start and end, poor attention to middle tokens); quadratic attention scaling (token relationship tracking grows exponentially with input length); and semantic distractor interference.
— Chroma Research
URL: https://research.trychroma.com/context-rot
Date: July 2025

[FACT]
Chroma's study found "even a single distractor reduces performance relative to the baseline," with non-uniform degradation effects amplifying at longer contexts.
— Chroma Research
URL: https://research.trychroma.com/context-rot
Date: July 2025

[FACT]
Counterintuitively, Chroma's study found "models perform better on shuffled haystacks than on logically structured ones," suggesting LLM attention mechanisms behave unexpectedly when processing coherent, enterprise-quality codebases.
— Chroma Research
URL: https://research.trychroma.com/context-rot
Date: July 2025

[FACT]
In Chroma's LongMemEval tests, significant performance gaps emerged between focused inputs (~300 tokens) and full inputs (~113,000 tokens). Claude models showed "the most pronounced gap" and exhibited conservative abstention patterns when uncertain.
— Chroma Research
URL: https://research.trychroma.com/context-rot
Date: July 2025

[FACT]
The Chroma researchers note that "in practice, long context applications are often far more complex, requiring synthesis or multi-step reasoning, and based on findings, performance degradation would be expected to be even more severe under those conditions" than measured in their controlled study.
— Chroma Research
URL: https://research.trychroma.com/context-rot
Date: July 2025

---

## 3. Testing and Debugging Limitations of AI-Generated Code

### 3.1 SWE-bench: Real-World Task Performance

[STATISTIC]
On SWE-bench Pro — a more contamination-resistant, enterprise-grade benchmark variant — even GPT-5 (High) scores approximately 23.3% Pass@1, and most widely used coding models remain under 25%.
— SWE-Bench Pro (Public Dataset), Scale AI SEAL leaderboard
URL: https://scale.com/leaderboard/swe_bench_pro_public
Date: January 2026

[STATISTIC]
On SWE-bench Verified (an easier benchmark variant), frontier models as of early 2026 sit in the 76–81% band.
— SWE-bench leaderboard data
URL: https://www.swebench.com/
Date: 2026

### 3.2 Developer Debugging Burden

[STATISTIC]
66% of developers in Stack Overflow's 2025 Developer Survey (65,000+ respondents) cite "AI solutions that are almost right, but not quite" as their biggest frustration, leading to more time-consuming debugging.
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
45.2% of professional developers report that "debugging AI-generated code is more time-consuming."
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
"If 2025 was the year of AI coding speed, 2026 is going to be the year of AI coding quality."
— Stack Overflow Blog
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 28, 2026

### 3.3 Developer Trust in AI-Generated Code

[STATISTIC]
46% of developers actively distrust AI tool accuracy; 33% trust it. Only 3% report "highly trusting" AI output. Experienced developers show the highest distrust rate: 20% "highly distrust."
— Stack Overflow 2025 Developer Survey (65,000+ respondents)
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[STATISTIC]
Positive developer sentiment toward AI tools dropped from over 70% in 2023–2024 to 60% in 2025.
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

[QUOTE]
"Trust in the accuracy of AI has fallen from 40% in previous years to just 29% this year."
— Stack Overflow, 2025 Developer Survey press release
URL: https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
Date: 2025

[FACT]
75% of developers said they would still ask another human for help when they do not trust AI's answers.
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

See [D06: Developer Experience Reports] for detailed coverage of developer sentiment trends and workflow friction patterns.

---

## 4. Architecture and Design Decision Limitations

### 4.1 Architectural Flaw Escalation

[STATISTIC]
Apiiro's analysis of tens of thousands of repositories across Fortune 50 enterprises (December 2024–June 2025) found that while syntax errors in AI-written code dropped 76% and logic bugs decreased 60%, privilege escalation paths jumped 322% and architectural design flaws spiked 153%.
— Itay Nussbaum, Product Manager, Apiiro
URL: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
Date: September 4, 2025

[FACT]
AI-generated code is described as "highly functional but systematically lacking in architectural judgment" — producing code that passes unit tests but introduces structural risks invisible to surface-level review.
— InfoQ, citing 2025 research
URL: https://www.infoq.com/news/2025/11/ai-code-technical-debt/
Date: November 2025

### 4.2 Enterprise Data Architecture Friction

[STATISTIC]
In a 2025 Deloitte survey, 48% of organizations cited searchability of data and 47% cited reusability of data as challenges to their AI automation strategy.
— Deloitte Insights, Agentic AI Strategy
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2025/2026

[FACT]
Current enterprise data architectures built around extract, transform, load (ETL) processes and data warehouses "create friction for agent deployment," with the fundamental issue being that "most organizational data isn't positioned to be consumed by agents that need to understand business context and make decisions."
— Deloitte Insights
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2025/2026

### 4.3 Technical Debt Compounding

[STATISTIC]
Forrester predicted that by 2025, more than 50% of technology decision-makers would face moderate to severe technical debt from AI-speed development practices, with that number projected to reach 75% by 2026.
— Forrester (cited by multiple sources)
URL: https://www.infoq.com/news/2025/11/ai-code-technical-debt/
Date: November 2025

[STATISTIC]
Analysis of 847 venture-backed startups found 73% of AI-built startups hit critical scaling failures by month 6, with technical debt compounding at 23% monthly.
— [UNVERIFIED — original primary source not identified in search results]
URL: https://medium.com/@ahmadfiazjan/the-30-000-technical-debt-trap-why-73-of-ai-built-startups-fail-to-scale-7c81ce4602f9
Date: September 2025

---

## 5. Security Vulnerability Introduction Rates

### 5.1 Veracode 2025 GenAI Code Security Report

[STATISTIC]
AI-generated code introduced risky security flaws in 45% of tests. The 2025 GenAI Code Security Report analyzed code generated by over 100 LLMs across Java, JavaScript, Python, and C#, using 80 coding tasks designed to expose common software weaknesses.
— Veracode, 2025 GenAI Code Security Report
URL: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
Date: July 30, 2025

[STATISTIC]
Java was the highest-risk language for AI code generation, with a security failure rate exceeding 70%. Python, C#, and JavaScript failure rates ranged between 38% and 45%.
— Veracode, 2025 GenAI Code Security Report
URL: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
Date: July 30, 2025

[STATISTIC]
LLMs failed to secure code against cross-site scripting (CWE-80) in 86% of cases and against log injection (CWE-117) in 88% of cases.
— Veracode, 2025 GenAI Code Security Report
URL: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
Date: July 30, 2025

[FACT]
"While models got better at writing functional or syntactically correct code, they were no better at writing secure code, with security performance remaining flat, regardless of model size or training sophistication." GPT-5 Mini achieved the first meaningful improvement, recording a 72% security pass rate in the October 2025 update.
— Veracode, GenAI Code Security Report (October 2025 update)
URL: https://www.veracode.com/blog/ai-code-security-october-update/
Date: October 2025

### 5.2 Apiiro: 10x Vulnerability Spike in Production Repositories

[STATISTIC]
AI-generated code introduced over 10,000 new security findings per month across analyzed repositories by June 2025 — a 10x increase from December 2024 — based on analysis of tens of thousands of repositories across several thousand developers at Fortune 50 enterprises.
— Itay Nussbaum, Apiiro
URL: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
Date: September 4, 2025

[STATISTIC]
AI-assisted developers exposed cloud credentials (Azure Service Principals, Storage Access Keys) nearly twice as often as developers not using AI assistance.
— Itay Nussbaum, Apiiro
URL: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
Date: September 4, 2025

[STATISTIC]
AI-assisted developers produced 3–4x more commits than non-AI peers, but overall PR volume fell by nearly one-third, resulting in fewer, larger pull requests that complicate code review.
— Itay Nussbaum, Apiiro
URL: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
Date: September 4, 2025

[QUOTE]
"It's not clear how you run an AI-coded codebase." — Brian Armstrong, CEO, Coinbase
URL: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
Date: September 4, 2025 (as cited in Apiiro report)

### 5.3 DORA: Systemic Delivery Stability Impact

[STATISTIC]
The 2024 Google DORA report found that a 25% increase in AI adoption correlated with an estimated 1.5% decrease in delivery throughput and a 7.2% decrease in delivery stability.
— Google DORA 2024 State of DevOps Report
URL: https://dora.dev/research/2024/dora-report/
Date: 2024

[FACT]
The 2025 DORA report found that AI adoption no longer correlates with delivery throughput slowdowns, but AI adoption continues to have a negative relationship with software delivery stability — a finding consistent across both the 2024 and 2025 studies.
— Google DORA 2025 Report
URL: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
Date: 2025

---

## 6. The "Works in Demo, Fails in Production" Pattern

### 6.1 Scale of Production Failure

[STATISTIC]
Only 5% of enterprise-grade generative AI systems reach production, meaning 95% fail during evaluation, according to an MIT report cited by multiple industry sources.
— MIT report (cited by Directual and Composio)
URL: https://www.directual.com/blog/ai-agents-in-2025-why-95-of-corporate-projects-fail
Date: 2025

### 6.2 Root Causes of Demo-to-Production Failure

[FACT]
"A demo agent runs one task and exits, while a production agent runs continuously, remembers prior actions, handles interruptions, and coordinates with other agents." — State management gap as root cause of failure pattern.
— Medium, "Why AI Agents Fail in Production"
URL: https://medium.com/@michael.hannecke/why-ai-agents-fail-in-production-what-ive-learned-the-hard-way-05f5df98cbe5
Date: 2025

[FACT]
Composio's 2025 AI Agent Report identifies three leading causes of production failure: "Dumb RAG" (bad memory management), "Brittle Connectors" (broken I/O between agent and external systems), and "Polling Tax" (absence of event-driven architecture). The report concludes "most AI agent failures aren't about model quality — they're about poor context management."
— Composio, "The 2025 AI Agent Report"
URL: https://composio.dev/blog/why-ai-agent-pilots-fail-2026-integration-roadmap
Date: 2025

[FACT]
"In multi-step workflows, the problem is rarely that the agent can't call the right tool — it's that it calls a plausible tool when the correct tool requires contextual reasoning across prior steps." — Characterization of silent failure mode in agentic coding.
— DEV Community, "Why Your AI Agent Works in Demo But Fails in Production"
URL: https://dev.to/dingomanhammer/why-your-ai-agent-works-in-demo-but-fails-in-production-4e51
Date: 2025

[FACT]
"The most dangerous failure mode produces no errors — the agent just did the wrong thing confidently." — Description of silent failure in production agentic systems.
— DEV Community
URL: https://dev.to/dingomanhammer/why-your-ai-agent-works-in-demo-but-fails-in-production-4e51
Date: 2025

[FACT]
Real production incident documented: Replit's AI coding assistant deleted a production database despite explicit instructions not to do so, described as "not the model selecting an obviously wrong action but rather misinterpreting the scope of a legitimate instruction."
— Directual blog, citing documented incident
URL: https://www.directual.com/blog/ai-agents-in-2025-why-95-of-corporate-projects-fail
Date: 2025

[FACT]
Agents depend on "slow, flaky tools that were not designed for interactive workloads," with systems that "work in demo with mocked data or single-threaded execution failing under real concurrency, timeouts, and rate limits."
— Deloitte Insights, Agentic AI Strategy
URL: https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html
Date: 2025/2026

### 6.3 Developer-Reported Production Quality Issues

[STATISTIC]
57% of organizations agree that AI coding assistants introduce security risks or make security issues harder to detect.
— Enterprise survey data (cited by Stack Overflow blog)
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 28, 2026

[STATISTIC]
60% of organizations lack formal processes for assessing AI-generated code vulnerabilities.
— Survey data cited in enterprise AI adoption research
URL: https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents
Date: January 28, 2026

[STATISTIC]
20% of developers report becoming less confident in their own problem-solving ability as a result of AI tool usage.
— Stack Overflow 2025 Developer Survey
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

---

## Summary Data Table

| Failure Mode | Key Metric | Source | Date |
|---|---|---|---|
| Package hallucinations | 19.7% average rate (all models); 21.7% open-source | Spracklen et al., USENIX Security | 2025 |
| Logic/correctness errors vs. human | 75% more per 100 PRs (AI vs. human) | CodeRabbit (470 repos) | Jan 2026 |
| Security flaws in AI code | 45% of coding tasks | Veracode (100+ LLMs) | Jul 2025 |
| Java security failure rate | >70% | Veracode | Jul 2025 |
| Privilege escalation paths | +322% in AI-assisted repos | Apiiro (Fortune 50 sample) | Sep 2025 |
| Security findings growth | 10x in 6 months | Apiiro | Sep 2025 |
| Delivery stability impact | -7.2% per 25% AI adoption increase | Google DORA 2024 | 2024 |
| Developer trust in AI accuracy | 33% trust vs. 46% distrust | Stack Overflow (65,000+ devs) | 2025 |
| AI agent pilot production rate | ~5% reach production | MIT report (cited) | 2025 |
| SWE-bench Pro Pass@1 (best model) | ~23.3% (GPT-5 High) | Scale AI SEAL | Jan 2026 |

---

## Sources

- [Spracklen et al., "We Have a Package for You!" — USENIX Security 2025](https://arxiv.org/html/2406.10279v3)
- [USENIX Security 2025 Package Hallucinations Overview](https://www.usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code)
- [Stack Overflow Blog: "Are bugs and incidents inevitable with AI coding agents?" (Jan 28, 2026)](https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents)
- [Stack Overflow 2025 Developer Survey — AI Section](https://survey.stackoverflow.co/2025/ai/)
- [Stack Overflow 2025 Developer Survey — Press Release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/)
- [Veracode 2025 GenAI Code Security Report](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)
- [Veracode GenAI Code Security Report — Blog Post](https://www.veracode.com/blog/genai-code-security-report/)
- [Veracode October 2025 Update — GPT-5 Mini Security Results](https://www.veracode.com/blog/ai-code-security-october-update/)
- [Veracode press release via BusinessWire, July 30, 2025](https://www.businesswire.com/news/home/20250730694951/en/AI-Generated-Code-Poses-Major-Security-Risks-in-Nearly-Half-of-All-Development-Tasks-Veracode-Research-Reveals)
- [Apiiro: "4x Velocity, 10x Vulnerabilities" — Itay Nussbaum, Sep 4, 2025](https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/)
- [Chroma Research: "Context Rot" — Hong et al., Jul 2025](https://research.trychroma.com/context-rot)
- [Factory.ai: "The Context Window Problem" — Varin Nair, Aug 25, 2025](https://factory.ai/news/context-window-problem)
- [Google DORA 2024 State of DevOps Report](https://dora.dev/research/2024/dora-report/)
- [Google DORA 2025 Report Announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- [DORA 2024: "AI and Platform Engineering Fall Short" — The New Stack](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/)
- [CodeMirage: Hallucinations in Code Generated by LLMs — arxiv 2408.08333](https://arxiv.org/abs/2408.08333)
- [Composio: "The 2025 AI Agent Report: Why AI Pilots Fail in Production"](https://composio.dev/blog/why-ai-agent-pilots-fail-2026-integration-roadmap)
- [DEV Community: "Why Your AI Agent Works in Demo But Fails in Production"](https://dev.to/dingomanhammer/why-your-ai-agent-works-in-demo-but-fails-in-production-4e51)
- [Directual: "AI Agents in 2025: Why 95% of Corporate Projects Fail"](https://www.directual.com/blog/ai-agents-in-2025-why-95-of-corporate-projects-fail)
- [Deloitte Insights: Agentic AI Strategy (2026 Tech Trends)](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html)
- [InfoQ: "AI-Generated Code Creates New Wave of Technical Debt" (Nov 2025)](https://www.infoq.com/news/2025/11/ai-code-technical-debt/)
- [Help Net Security: "AI can write your code, but nearly half may be insecure" (Aug 2025)](https://www.helpnetsecurity.com/2025/08/07/create-ai-code-security-risks/)
- [SWE-bench Leaderboard](https://www.swebench.com/)
- [SWE-Bench Pro — Scale AI SEAL](https://scale.com/leaderboard/swe_bench_pro_public)
- [Cloud Security Alliance: "Understanding Security Risks in AI-Generated Code" (Jul 2025)](https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code)
- [The Register: "AI-authored code needs more attention, contains worse bugs" (Dec 2025)](https://www.theregister.com/2025/12/17/ai_code_bugs/)

---

## Key Takeaways

- **Security risk is not improving at scale.** Veracode's test of 100+ LLMs found security performance flat regardless of model size or training sophistication, with AI-generated code failing security checks in 45% of tasks overall and over 70% of Java tasks. Only the October 2025 GPT-5 Mini result showed the first meaningful improvement.

- **Architectural risk is rising even as surface bugs fall.** Apiiro's Fortune 50 enterprise data shows that while syntax errors dropped 76% and logic bugs dropped 60% in AI-assisted code, privilege escalation vulnerabilities jumped 322% and architectural design flaws spiked 153% — risks that are harder to detect and costlier to remediate.

- **Context window constraints remain a hard ceiling for enterprise deployment.** Even frontier LLMs with 1–2 million token windows cannot hold most enterprise monorepos in context, and Chroma Research documented that performance degrades non-uniformly even well before those limits are reached, with the degradation expected to be "even more severe" under multi-step reasoning tasks common in enterprise development.

- **The demo-to-production gap is not a model quality problem.** The 95% enterprise AI pilot failure rate attributed to MIT research is driven primarily by state management failures, brittle integrations, and context engineering gaps — not raw LLM capability. Production environments expose concurrency, timeouts, and scope ambiguity that controlled demos mask.

- **Developer distrust is a leading indicator, not a lagging one.** The Stack Overflow survey of 65,000+ developers documents that distrust (46%) now exceeds trust (33%) in AI accuracy, a reversal from 2023 levels. Experienced developers — those with the highest accountability in enterprise settings — show the highest distrust rates, suggesting the signal is credible and grounded in direct production experience.
