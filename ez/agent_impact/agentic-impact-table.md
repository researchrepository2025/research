# Agentic Coding Impact: Where It Helps vs. Where It Doesn't

**The SaaS-to-on-prem lifecycle has three distinct phases: initial code refactoring, customer deployment across heterogeneous environments, and ongoing operational support.** Agentic coding tools deliver measurable gains in each phase — but the gains are concentrated on mechanical, well-scoped tasks. The architectural decisions, cross-service reasoning, and N-customer heterogeneity that make on-prem delivery fundamentally hard remain outside AI's current capabilities. This table maps the evidence across all three phases.

---

## Phase 1: Initial Refactor

| Where Agentic Coding **Helps** | Where Agentic Coding **Does NOT Help** |
|---|---|
| **Code migration at scale** — Google migrated 5,359 files (149K+ lines) with [80% AI-authored code and 50% total time reduction](https://research.google/blog/accelerating-code-migrations-with-ai/) | **65% of developers say AI misses critical context during refactoring** — AI lacks understanding of [cross-service dependencies, business rules, and architectural history](https://www.qodo.ai/reports/state-of-ai-code-quality/) |
| **Large-scale class migration** — Nubank migrated 100K data classes; [18-month estimate reduced to 2 months (12x efficiency)](https://devin.ai/customers/nubank/) using Devin | **AI-generated code produces 1.7x more critical defects** — [75% increase in logic errors, 1.5-2x security vulnerabilities, 8x performance inefficiencies](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report) (470 GitHub PRs analyzed) |
| **IaC generation with iterative refinement** — First-attempt deployment success is only 27-30%, but [iterative feedback loops achieve 90%+ (100% by 7 iterations)](https://arxiv.org/html/2506.05623v1) | **2.74x more vulnerabilities in AI-generated code** — LLMs introduce security flaws 70% of the time for Java; [AI-generated code now causes 1 in 5 breaches](https://www.veracode.com/blog/genai-code-security-report/) |
| **Helm chart generation** — Reduces chart creation from [4 hours to 45 minutes with zero YAML syntax errors](https://markaicode.com/ai-helm-chart-generation-kubernetes-productivity/) | **Experienced developers are 19% SLOWER with AI tools** — METR randomized controlled trial of [16 developers with 1,500+ commits experience](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); developers *believed* they were 20% faster |
| **Automated test coverage** — Diffblue Cover achieves [65% automated line coverage on enterprise Java](https://www.diffblue.com/resources/diffblue-cover-vs-ai-coding-assistants-benchmark-2025/) (vs. 49% for LLM coding assistants) | **AI cannot make architectural decisions** — Lacks grasp of [business context, regulatory environment, and 10-year architectural history](https://www.sahaj.ai/generative-ai-in-software-architecture-dont-replace-your-architects-yet/) required for storage/CNI/deployment topology selection |
| **Version upgrade acceleration** — Amazon Q Developer delivers [40%+ acceleration on framework version upgrades](https://aws.amazon.com/blogs/devops/dissecting-the-performance-gains-in-amazon-q-developer-agent-for-code-transformation/) | **Multi-file evolution tasks: only 21% success** — Even GPT-5 with OpenHands achieves [only 21% on multi-file code evolution](https://arxiv.org/html/2512.18470v1) (vs. 65% on isolated single-file bugs); 80% of real refactoring effort is evolution, not greenfield |
| **AWS SDK migration** — [70% acceleration on AWS SDK V1-to-V2 Golang migrations](https://aws.amazon.com/transform/custom/) | **30% increase in change failure rates after AI adoption** — Teams using AI broadly in 2025 saw [higher post-deployment failures due to undertested generated code](https://www.augmentcode.com/guides/safe-legacy-refactoring-ai-tools-vs-manual-analysis-in-2025) |

---

## Phase 2: Customer Deployment

| Where Agentic Coding **Helps** | Where Agentic Coding **Does NOT Help** |
|---|---|
| **IaC iterative deployment** — With feedback loops, IaC generation achieves [79.7% pass on first iteration and 100% by 7 iterations](https://arxiv.org/abs/2506.05623) | **First-attempt IaC deployment success is only 27-30%** — Without human-in-the-loop iteration, [AI-generated infrastructure fails to deploy 70% of the time](https://arxiv.org/html/2506.05623v1) |
| **AI-assisted operations cut ticket volume ~40% and MTTR by >80%** — [Cisco demonstrated at KubeCon NA 2025](https://siliconangle.com/2025/11/15/ai-leads-platform-engineering-revival-kubecon-na-2025/) | **93% of K8s organizations have overprivileged service accounts** — AI-generated manifests frequently deploy in [misconfigured states](https://orca.security/resources/blog/kubernetes-security-helm-chart-tracing/); AI cannot assess customer security posture |
| **AI-generated runbooks from natural language** — [Rundeck generates operational runbooks automatically](https://docs.rundeck.com/docs/manual/jobs/ai-generated-runbooks.html) | **Change Advisory Boards require human governance** — [Formal RFC documentation with risk assessment, rollback plan, and testing evidence](https://www.freshworks.com/freshservice/change-advisory-board/) cannot be automated away |
| **ISV distribution platforms** — 70 of Fortune 100 manage on-prem K8s app delivery through [Replicated](https://medium.com/@Kannan91/how-modern-software-vendors-ship-kubernetes-apps-to-on-prem-customers-replicated-kots-air-gap-deec7eb339b0) | **On-prem patching scales non-linearly** — Windows-only patching: 252 hours/year; adding third-party OS patching [jumps to 2,400 hours/year (nearly 10x)](https://www.automox.com/blog/cost-burden-on-prem-patch-management) |
| **Developer productivity boost** — Developers go from [10-15 contributions/day to 25+ with AI tooling](https://blog.marcnuri.com/boosting-developer-productivity-ai-2025) for deployment scripting | **40% of agentic AI projects will be canceled by end of 2027** — [Gartner prediction reflecting real-world failure rates](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) of autonomous agent deployments |
| | **N-customer heterogeneity is non-linear** — Each customer has distinct K8s versions, CNIs, storage backends, network policies; the [deployment matrix explodes combinatorially](https://www.spectrocloud.com/state-of-kubernetes-2025) |

---

## Phase 3: Ongoing Support

| Where Agentic Coding **Helps** | Where Agentic Coding **Does NOT Help** |
|---|---|
| **50% faster incident resolution** — [PagerDuty's end-to-end AI agent suite](https://www.pagerduty.com/newsroom/2025-fall-productlaunch/) (October 2025) | **Operational toil is RISING despite 51% AI deployment** — Toil rose to [30% from 25% (first increase in 5 years)](https://runframe.io/blog/state-of-incident-management-2025); AI handles symptoms, not root causes |
| **Enterprise MTTR reductions of 40-60%** — Across organizations implementing [AI-powered incident management](https://www.ir.com/guides/how-to-reduce-mttr-with-ai-a-2026-guide-for-enterprise-it-teams) | **57% of SREs spend >50% of their week on toil** — [73% experienced outages from ignored alerts](https://www.catchpoint.com/learn/sre-report-2025); AI adds more alerts, not fewer |
| **4.87 hours saved per incident** — [SolarWinds/Cloud Native Now real-world measurement](https://cloudnativenow.com/contributed-content/how-sres-are-using-ai-to-transform-incident-response-in-the-real-world/) | **AI cannot debug cross-service issues** — Clock skew between Service A and B causing auth token expiry is [invisible to AI](https://medium.com/@martin.jordanovski/ai-coding-assistants-debugging-challenges-ais-limitations-4e49d04e8b6a); requires distributed systems reasoning |
| **Automated K8s troubleshooting** — Komodor Klaudia (November 2025) [detects, investigates, and remediates Kubernetes issues autonomously](https://www.helpnetsecurity.com/2025/11/05/komodor-platform-self-healing-and-cost-optimization-capabilities/) | **69% of AI-driven operational decisions still require human verification** — [Autonomous remediation is not yet trusted](https://www.deimos.io/blog-posts/agentic-ais-role-in-modern-it-operations) |
| **Config drift detection** — [40% of Kubernetes users report configuration drift negatively impacts stability](https://komodor.com/blog/drift-away-the-hidden-risk-of-large-scale-kubernetes-environments/); automated detection helps | **11 critical failure patterns in autonomous agents** — Including [unauthorized data sharing, destructive interventions, identity spoofing](https://www.trendingtopics.eu/agents-of-chaos-study-reveals-11-critical-failure-patterns-in-openclaw-agents/); agents lack coherent representation of whom they serve |
| **82.4% reduction in incident response times** — [Comprehensive SRE automation study](https://www.ijsat.org/papers/2025/1/2649.pdf); 47.6% decrease in change failure rate | **On-call at 3am requires cross-team coordination AI cannot replicate** — [High-stakes decision-making under time pressure](https://www.cio.com/article/4058031/how-software-architects-and-project-managers-can-leverage-agentic-ai.html) with incomplete information |
| | **P1 SLA response: 15-30 minutes** — Depends entirely on [human availability, not AI capability](https://www.ibm.com/think/topics/sla-metrics); P2: 1-2 hours, P3: 4-8 hours — all human-gated |

---

## Net Effect: Cloud Accelerates

Agentic coding saves 50-70% on mechanical infrastructure tasks for **both** cloud and on-prem teams. But cloud teams were already free of deployment toil. The savings go to fundamentally different places — and the gap widens.

### Cloud teams reinvest AI savings into feature development

- **79% of a cloud-only 50-person team works on features** vs. only 53% when supporting on-prem — a [32.9% velocity loss](https://www.replicated.com/blog/introducing-the-state-of-self-hosted-survey-2025)
- **Nearly 50% of vendors ship to self-hosted customers LESS frequently than SaaS customers** — Cloud ships continuously; on-prem ships [monthly or quarterly (4-52x faster release cadence)](https://www.replicated.com/blog/introducing-the-state-of-self-hosted-survey-2025)
- **Deployment frequency directly correlates with engineering productivity** — [DORA metrics](https://dora.dev/guides/dora-metrics/) prove that faster shipping = better outcomes; on-prem structurally constrains deployment frequency

### On-prem teams: AI savings absorbed by infrastructure tax

- **Dual cloud+on-prem CI/CD costs 13x more** — Cloud-only CI/CD: ~$550/month; dual pipelines: ~$7,050/month; requires [2.75 additional platform engineers ($550K-$690K/year)](https://circleci.com/blog/ci-cd-cost-optimization-enterprise-teams/)
- **25-40% of total engineering capacity consumed by dual-maintenance tax** — The pure cost of [feature parity, backporting, and cross-environment testing](https://www.cio.com/article/4114170/epicor-sets-timeline-to-sunset-on-prem-erp-as-cloud-becomes-the-only-path-forward.html)
- **Developers spend 23-25% on toil at baseline** — Dual on-prem targets amplify this to 47-57%; AI reduces it but [cannot eliminate the structural overhead](https://survey.stackoverflow.co/2025/)
- **Infrastructure maintenance: 15-20% of development costs annually** — [Doubles to 30-40% for on-prem deployments](https://agileengine.com/software-development-cost-breakdown-in-2025-a-complete-guide/), diverting engineers from features

### AI features are fundamentally cloud-first

- **GitLab Duo Self-Hosted required shipping inference infrastructure** — vLLM, model distribution, GPU configuration, [separate AI Gateway component](https://about.gitlab.com/blog/2025/02/27/gitlab-duo-self-hosted-enterprise-ai-built-for-data-privacy/); multiplicative effect on distribution complexity
- **On-prem feature lag compounds over time** — Q1: 1-2 features behind; Q4: 8-12 features; Q8: 20+ features; Q12+: ISV faces [sunset-or-converge decision](https://erp.today/epicor-sets-final-on-premises-release-dates-as-cloud-strategy-accelerates/)

### The industry is proving it — vendors sunsetting on-prem

- **Epicor: final on-premises releases between 2026-2028** — ["Cloud has become the only path forward"](https://www.cio.com/article/4114170/epicor-sets-timeline-to-sunset-on-prem-erp-as-cloud-becomes-the-only-path-forward.html)
- **Atlassian Data Center EOL March 28, 2029** — After a decade of maintaining dual cloud+on-prem; [30% Data Center price increase in Feb 2025](https://www.atlassian.com/licensing/data-center-end-of-life) to force migration
- **Gitpod ended self-managed entirely** — Forfeited seven figures of revenue; pivoted to ["cloud-prem" (vendor-managed in customer VPC)](https://www.gitpod.io/blog/self-hosted-not-self-managed) because on-prem consumed 30-50% engineering bandwidth while generating <15% revenue
- **Microsoft shifting to cloud management software** — [Raising concerns about on-premises support longevity](https://www.theregister.com/2026/01/23/microsoft_shifting_to_cloud_management/)
- **On-prem TCO is 3-5x the list price of software** — Personnel costs consume [50-85% of total TCO](https://www.automox.com/blog/cost-burden-on-prem-patch-management) for on-prem application systems

---

> **Bottom Line:** Agentic coding is necessary but insufficient for closing the SaaS-to-on-prem gap. It reduces the mechanical tax — code migration, test generation, IaC scaffolding, incident triage — by 40-70% on well-scoped tasks. But the hard problems of on-prem delivery are architectural (multi-tenant to single-tenant decomposition), operational (N-customer heterogeneity across K8s versions, CNIs, and security postures), and organizational (dual-maintenance tax consuming 25-40% of engineering capacity). These structural constraints are immune to AI acceleration. The net effect is that cloud teams reinvest AI productivity gains into feature velocity while on-prem teams reinvest them into surviving the infrastructure tax. Agentic coding doesn't close the gap — it widens cloud's competitive advantage.
