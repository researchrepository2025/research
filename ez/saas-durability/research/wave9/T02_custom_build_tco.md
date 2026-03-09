# T02 — True Total Cost of Ownership: Custom Enterprise Software

**Research File:** T02 — Custom Build TCO
**Wave:** 9
**Date Compiled:** 2026-03-06
**Audience:** C-Suite / Enterprise Strategy

---

## Executive Summary

The true total cost of ownership (TCO) of custom enterprise software is structurally underestimated at point-of-decision across every cost category. Initial development contracts represent as little as 20–35% of lifetime system expenditure; maintenance, infrastructure, talent attrition, and technical debt compound over multi-year horizons to produce costs that routinely run 2–3x the original build budget. Agentic coding tools are compressing the initial development cost variable—with credible estimates ranging from 50% to 90% reduction in initial build effort—but do not eliminate the downstream cost categories that account for the majority of lifecycle spend. The hidden iceberg of enterprise software TCO—technical debt, security patching exposure, talent turnover, cloud waste, and opportunity cost of engineering time—remains largely unchanged by agentic tools in their current form, and may introduce new governance and remediation costs. For C-suite decision-makers, the practical implication is that any custom build investment must be sized against the full 5–7 year cost stack, not the initial contract value. See [F05 — Build vs. Buy Framework](../wave1/F05_build_vs_buy_framework.md) for detailed coverage of the strategic decision framework and when building creates defensible competitive advantage.

---

## 1. Development Costs: Traditional Teams vs. Agentic Coding

### 1a. Traditional Team Development Cost Ranges

[DATA POINT]
Enterprise custom software development cost range for design, development, and implementation: $100,000 to $750,000 for mid-market deployments; complex enterprise systems routinely exceed $1,000,000.
URL: https://www.hubifi.com/blog/enterprise-software-pricing-guide
Date: 2025

[STATISTIC]
"Initial development costs represent only 20–50% of the project's lifetime investment."
URL: https://leobit.com/blog/total_cost_of_ownership_for_custom_software_development/
Date: March 27, 2025

[STATISTIC]
Large IT projects run 45% over budget and 7% over schedule while delivering 56% less value than predicted — McKinsey / University of Oxford analysis of 5,400+ large IT projects.
— McKinsey & Company / University of Oxford, "Delivering Large-Scale IT Projects On Time, On Budget, and On Value" (Bloch, Blumberg, Laartz)
URL: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
Date: 2012 (primary quantitative benchmark; see F05 for full citation context)

[STATISTIC]
A subsequent McKinsey/Oxford Global Projects analysis of 6,000+ IT projects (2001–2017) found that IT projects "exceeded their budgets by 75 percent, overran their schedules by 46 percent, and generated 39 percent less value than predicted." Only 1 in 200 projects delivered intended benefits on time and within budget.
— McKinsey & Company / Oxford Global Projects
URL: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
Date: 2017

[STATISTIC]
Standish Group CHAOS Report (2020): Only 31% of software projects are successful; 50% are "challenged" (fail over time); 19% fail completely.
— The Standish Group CHAOS Report 2020
URL: https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes
Date: 2020

[STATISTIC]
Average cost overrun across all company sizes: 178% for large companies, 182% for medium companies, 214% for small companies.
URL: https://en.tigosolutions.com/the-standish-group-report-839-of-it-projects-partially-or-completely-fail
Date: 2025 (citing Standish Group data)

### 1b. Agentic Coding: Development Cost Compression

[STATISTIC]
"Vibe coding is cutting the cost of application development by anywhere from 70% to 95%, opening development to subject matter experts."
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
Agentic coding claimed to cut development costs by up to 90%; more conservative analysis finds "a 50% reduction in human engineering effort, which becomes a 10% savings on total expenditures" when all downstream costs are accounted for.
— Belitsoft, "Agentic AI Coding: What Still Remains Expensive Amid a 90% Drop in Costs"
URL: https://belitsoft.com/agentic-ai-coding
Date: 2026

[STATISTIC]
"AI-centric organizations are achieving 20% to 40% reductions in operating costs and 12–14 point increases in EBITDA margins, driven by automation, faster cycle times and more efficient allocation of talent and infrastructure."
— McKinsey, as cited in CIO article by Lalit Wadhwa
URL: https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html
Date: February 20, 2026

[STATISTIC]
Accenture randomized controlled trial using GitHub Copilot: 8.69% increase in pull requests per developer; 11% increase in pull request merge rates; 84% increase in successful builds.
URL: https://linearb.io/blog/is-github-copilot-worth-it
Date: 2025

[STATISTIC]
GoTo (formerly LogMeIn): 30% reduction in development time after rolling out GitHub Copilot to approximately 1,000 developers.
URL: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
Date: 2026

[STATISTIC]
TELUS: teams created over 13,000 custom AI solutions while shipping engineering code 30% faster, accumulating 500,000 hours in total time savings.
— Anthropic, "2026 Agentic Coding Trends Report"
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[STATISTIC]
METR study (July 2025), experienced open-source developers: when using AI tools, developers took 19% longer to complete tasks on their own repositories than without. Developers estimated they were sped up by 20%—a perception gap of nearly 40 percentage points.
— METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 2025

[STATISTIC]
Stack Overflow Developer Survey (2025): approximately 70% of agent users agree that agents have reduced time spent on specific development tasks; 69% agree they have increased productivity.
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

### 1c. Development Cost Comparison Table

| Cost Driver | Traditional Team | With Agentic Coding |
|---|---|---|
| Initial build cost (mid-market) | $100K–$750K | $10K–$375K (estimated 50–90% compression) |
| Budget overrun probability | 45–75% over budget (McKinsey/Oxford) | [UNVERIFIED — limited published data on agentic project overruns] |
| Time to first deploy | 6–18+ months | Days to weeks for targeted capabilities |
| AI tool cost per developer/month | N/A | $10–$200 (GitHub Copilot Business: $19/seat; Claude Code: $150/seat) |
| Enterprise agentic coding tools | N/A | $39/user/month (GitHub Copilot Enterprise); $150/month (Claude Code premium) |

URL for tooling pricing: https://northflank.com/blog/claude-rate-limits-claude-code-pricing-cost
Date: 2026

---

## 2. Infrastructure Costs: Cloud Hosting, DevOps, and Monitoring

[STATISTIC]
Organizations estimate 27% of their Infrastructure as a Service (IaaS) and Platform as a Service (PaaS) spending is wasted — the same percentage as in the 2024 study.
— Flexera, "2025 State of the Cloud Report"
URL: https://www.globenewswire.com/news-release/2025/03/19/3045271/0/en/New-Flexera-Report-Finds-that-84-of-Organizations-Struggle-to-Manage-Cloud-Spend
Date: March 19, 2025

[STATISTIC]
"84% of respondents believe that managing cloud spend is the top cloud challenge for organizations today."
— Flexera, "2025 State of the Cloud Report"
URL: https://www.flexera.com/about-us/press-center/new-flexera-report-finds-84-percent-of-organizations-struggle-to-manage-cloud-spend
Date: March 2025

[STATISTIC]
Cloud budgets are already exceeding limits by 17%; cloud spend is expected to increase by 28% in the coming year.
— Flexera, "2025 State of the Cloud Report"
URL: https://www.globenewswire.com/news-release/2025/03/19/3045271/0/en/New-Flexera-Report-Finds-that-84-of-Organizations-Struggle-to-Manage-Cloud-Spend
Date: March 19, 2025

[STATISTIC]
Nearly 33% of organizations spend more than $12 million annually on public cloud alone.
— Flexera, "2025 State of the Cloud Report"
URL: https://www.globenewswire.com/news-release/2025/03/19/3045271/0/en/New-Flexera-Report-Finds-that-84-of-Organizations-Struggle-to-Manage-Cloud-Spend
Date: March 19, 2025

[STATISTIC]
FinOps in Focus 2025 report estimates that 21% of cloud infrastructure spending — approximately US$44.5 billion — is wasted on underutilized resources.
URL: https://byteiota.com/cloud-waste-hits-44-5b-in-2025-the-finops-failure/
Date: 2025

[STATISTIC]
82% of Kubernetes workloads are overprovisioned; 65% use less than half of their requested CPU and memory; only 7% of workloads have accurate resource requests and limits.
URL: https://byteiota.com/cloud-waste-hits-44-5b-in-2025-the-finops-failure/
Date: 2025

[DATA POINT]
Representative monitoring tool pricing: Grafana Cloud Pro at $8/active user/month; enterprise-grade solutions (Datadog, New Relic) at higher per-seat costs with managed overhead premiums.
URL: https://scalr.com/learning-center/the-complete-guide-to-devops-monitoring-tools-in-2025-choosing-the-right-solution-for-your-infrastructure/
Date: 2025

[STATISTIC]
"Enterprise technology spending in the United States has been growing by 8 percent per year on average since 2022, while labor productivity has grown by close to 2 percent over the same period."
— McKinsey & Company, "The New Economics of Enterprise Technology in an AI World"
URL: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-new-economics-of-enterprise-technology-in-an-ai-world
Date: 2025

---

## 3. Maintenance Costs: Bug Fixes, Security Patches, Dependency Updates

[STATISTIC]
"Maintenance typically represents 20% of the original development cost each year."
— McKinsey & Company (as cited by multiple industry sources)
URL: https://wifitalents.com/custom-software-development-industry-statistics/
Date: 2026 (citing McKinsey)

[STATISTIC]
Annual maintenance cost range by software type: 15–20% of initial development cost per year for a single platform; 20–30% for unified codebases across two platforms; 25–40% for business-critical enterprise systems and SaaS platforms.
URL: https://7t.ai/blog/how-much-does-software-maintenance-cost-what-to-expect-for-apps-and-enterprise-software-maintenance/
Date: 2025

[STATISTIC]
"Continuous maintenance can add 15–25% of the original development cost annually and account for 60–80% of all lifetime costs over five years."
URL: https://leobit.com/blog/total_cost_of_ownership_for_custom_software_development/
Date: March 2025

[STATISTIC]
"In some cases, maintenance can account for as much as 60–90% of the software's total cost of ownership over its lifecycle."
URL: https://www.abbacustechnologies.com/software-maintenance-cost-how-much-does-it-really-cost/
Date: 2025

[STATISTIC]
"Over several years, maintenance can easily cost two to three times the original development budget."
URL: https://www.abbacustechnologies.com/software-maintenance-costs-in-2026-what-you-should-expect/
Date: 2026

[STATISTIC]
Global average data breach cost: $4.44 million (down 9% from $4.88 million in 2024). US organizations face a record $10.22 million average (up 9% year-over-year).
— IBM, "Cost of a Data Breach Report 2025"
URL: https://www.ibm.com/reports/data-breach
Date: 2025

[STATISTIC]
86% of organizations experienced operational disruptions from breaches including delayed sales, interrupted services, or halted production. Only 35% achieved full recovery.
— IBM, "Cost of a Data Breach Report 2025"
URL: https://www.allcovered.com/blog/key-insights-from-ibms-2025-cost-of-a-data-breach-report
Date: 2025

[STATISTIC]
"AI-generated code introduces 15–18% more security vulnerabilities, increasing risk as autonomy expands."
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

[STATISTIC]
"97% of AI-related security breaches involved AI systems that lacked proper access controls." Shadow AI added an average of $670,000 to breach costs.
— IBM, "Cost of a Data Breach Report 2025"
URL: https://www.allcovered.com/blog/key-insights-from-ibms-2025-cost-of-a-data-breach-report
Date: 2025

---

## 4. Talent Costs: Hiring, Retention, and Training

### 4a. Base Compensation

[STATISTIC]
Average enterprise software engineer salary in the United States as of late 2025: $156,904 per year ($75.43/hour).
— ZipRecruiter
URL: https://www.ziprecruiter.com/Salaries/Enterprise-Software-Engineer-Salary
Date: December 2025

[STATISTIC]
Software engineer salary range by experience level (US, 2026): entry-level $70,000–$90,000; mid-level (3–5 years) $100,000–$130,000; principal / technical lead $180,000+. At major tech companies, total compensation including stock and bonuses can be 2–3x the base salary.
URL: https://ravio.com/blog/software-engineer-salary-trends
Date: 2026

[STATISTIC]
AI/ML engineering roles saw 88% year-on-year growth in 2025, with AI Engineers commanding a 12% salary premium over general Software Engineers.
URL: https://ravio.com/blog/software-engineer-salary-trends
Date: 2026

### 4b. Recruitment and Turnover Costs

[STATISTIC]
SHRM estimate: onboarding a new software engineer costs between 6 to 9 months of their salary, factoring in recruitment, training, and lost productivity.
URL: https://www.lingolive.com/blog/cost-of-turnover-for-software-engineers/
Date: 2025

[STATISTIC]
Replacing a mid-level developer costs up to 2x their annual salary when factoring in recruitment, onboarding, and lost productivity. Exit of a top-performing engineer costs approximately 130% of annual salary.
URL: https://devsu.com/blog/navigating-software-developer-turnover-challenges
Date: 2025

[STATISTIC]
Software engineering has one of the highest employee turnover rates, averaging 23–25% annually — nearly double the cross-industry median.
URL: https://www.allstarsit.com/blog/what-employee-turnover-is-really-costing-your-tech-company
Date: 2025

[STATISTIC]
"Engineering accounts for 21.7% of all turnover studied."
— LinkedIn Talent Blog (as cited)
URL: https://www.lingolive.com/blog/cost-of-turnover-for-software-engineers/
Date: 2025

[STATISTIC]
Software engineering roles have "a 47% higher than average time to fill, at an average of 62 days."
— SHRM (as cited)
URL: https://www.lingolive.com/blog/cost-of-turnover-for-software-engineers/
Date: 2025

[STATISTIC]
New employees take an average of 12 months to reach the proficiency level of tenured employees.
URL: https://www.lingolive.com/blog/cost-of-turnover-for-software-engineers/
Date: 2025

[STATISTIC]
Technical recruiters cost an average of 12% more than non-technical recruiters with equivalent experience.
— Salary.com (as cited)
URL: https://www.lingolive.com/blog/cost-of-turnover-for-software-engineers/
Date: 2025

[STATISTIC]
69% of developers consider career growth the most important factor when evaluating new job opportunities; developers with access to cutting-edge technologies are 48% less likely to leave within a year.
— Stack Overflow Developer Survey 2025
URL: https://survey.stackoverflow.co/2025/ai/
Date: 2025

### 4c. Talent Cost Summary Table

| Cost Component | Estimate / Range | Source |
|---|---|---|
| Average US enterprise engineer salary | $156,904/year | ZipRecruiter, Dec 2025 |
| Full loaded cost (salary + benefits + equity) | ~2–3x base at major tech firms | Ravio, 2026 |
| Cost to replace mid-level engineer | Up to 2x annual salary | Devsu, 2025 |
| Cost to replace top performer | ~130% of annual salary | Devsu, 2025 |
| Annual engineer turnover rate | 23–25% | AllStarsIT, 2025 |
| Average time to fill engineering role | 62 days | SHRM via Lingo Live, 2025 |
| Ramp time to full productivity | ~12 months | Lingo Live, 2025 |

---

## 5. Opportunity Cost: Engineering Time Diverted from Core Business

[STATISTIC]
"CIOs spend 70 to 80% of their budget just maintaining existing systems."
URL: https://blog.sharmavishal.com/2025/10/build-vs-buy-is-dead-start.html
Date: October 2025

[STATISTIC]
McKinsey: CIOs reported that 10 to 20 percent of the technology budget designated for new products is diverted to resolving issues related to tech debt. Approximately 30% of CIOs believe more than 20% of their "new product" budget is absorbed by tech debt remediation.
— McKinsey & Company, "Tech Debt: Reclaiming Tech Equity"
URL: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/tech-debt-reclaiming-tech-equity
Date: 2023

[STATISTIC]
Companies that actively manage their technical debt can free up engineers to spend "up to 50 percent more of their time on innovations that support the organization's business goals."
— McKinsey & Company, "Breaking Technical Debt's Vicious Cycle"
URL: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/breaking-technical-debts-vicious-cycle-to-modernize-your-business
Date: 2023

[STATISTIC]
"By 2025, 40% of IT budgets will be spent simply maintaining tech debt."
— Gartner (as cited in multiple industry sources)
URL: https://securityboulevard.com/2025/12/what-your-technical-debt-is-really-costing-you/
Date: December 2025

[STATISTIC]
McKinsey: technical debt "accounts for about 40 percent of IT balance sheets" and CIOs estimated it "amounts to 20 to 40 percent of the value of their entire technology estate before depreciation."
— McKinsey & Company, "Tech Debt: Reclaiming Tech Equity"
URL: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/tech-debt-reclaiming-tech-equity
Date: 2023

[STATISTIC]
"86% of IT executives report that their companies were impacted by technical debt over the last year; 94% of companies recognize the importance of managing their technical debt; 58% have no formal strategy for doing so."
URL: https://vfunction.com/blog/technical-debt-whos-responsible/
Date: 2025

[STATISTIC]
"Maintenance consumes 50–75% of total software costs, with enhancements and modifications after initial deployment typically costing 3–4 times the original development."
URL: https://idealink.tech/blog/software-development-maintenance-true-cost-equation
Date: 2025

[QUOTE]
"Re-implementing well-traversed engineering problems in-house, instead of using IaaS, SaaS or PaaS vendors, can often push back development on services that make your startup unique."
URL: https://www.raypold.com/post/opportunity-cost-in-startups/
Date: 2025

---

## 6. The Hidden Iceberg: Costs Enterprises Consistently Underestimate

The categories below represent the submerged mass of custom software TCO — the costs not captured in initial build contracts, vendor quotes, or initial infrastructure estimates.

### 6a. Technical Debt Accumulation

[STATISTIC]
"It's predicted that by 2025, 40% of IT budgets will be spent simply maintaining tech debt."
— Gartner (as cited)
URL: https://securityboulevard.com/2025/12/what-your-technical-debt-is-really-costing-you/
Date: December 2025

[STATISTIC]
"Hidden costs [of custom software development] can add 30–50% to your initial software development budget."
URL: https://www.unifiedinfotech.net/blog/7-hidden-costs-of-custom-software-development-how-to-avoid-them/
Date: 2025

[QUOTE]
"If technical debt is allowed to build up, eventually the product becomes brittle and very expensive to change or extend."
URL: https://dockyard.com/blog/2025/05/13/the-long-term-cost-of-technical-debt-and-how-to-avoid-it
Date: May 2025

### 6b. Security Debt and Patch Exposure Windows

[STATISTIC]
Supply chain compromise: average breach cost of $4.91 million; average 267 days to resolve.
— IBM, "Cost of a Data Breach Report 2025"
URL: https://www.allcovered.com/blog/key-insights-from-ibms-2025-cost-of-a-data-breach-report
Date: 2025

[STATISTIC]
Average recovery time from a breach: over 100 days for most organizations; 25% required over 150 days.
— IBM, "Cost of a Data Breach Report 2025"
URL: https://www.allcovered.com/blog/key-insights-from-ibms-2025-cost-of-a-data-breach-report
Date: 2025

[STATISTIC]
"AI-driven coding reduces time to pull request by up to 58%, but AI-generated pull requests wait 4.6x longer in review without governance."
URL: https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
Date: 2026

### 6c. Scope Creep and Requirements Drift

[STATISTIC]
"Every additional year spent on the project increasing cost overruns by 15 percent."
— McKinsey & Company / University of Oxford
URL: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
Date: 2012

[STATISTIC]
Gartner predicts that at least 30% of generative AI projects will be abandoned after proof of concept by the end of 2025, "due to poor data quality, inadequate risk controls, escalating costs or unclear business value."
— Gartner press release
URL: https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
Date: July 29, 2024

### 6d. Integration and Dependency Costs

[DATA POINT]
Connecting enterprise platforms to HR systems, cloud apps, ticketing tools, or asset inventories: $5,000 to $50,000 per integration, depending on complexity, API limitations, and vendor participation during implementation.
URL: https://www.uprootsecurity.com/blog/grc-software-pricing-guide
Date: 2025

[DATA POINT]
"Implementation fees, data migration, training, certifications, consulting, and ongoing maintenance often add 17–22% of license cost" annually beyond base infrastructure costs.
URL: https://www.uprootsecurity.com/blog/grc-software-pricing-guide
Date: 2025

### 6e. Cloud Overprovisioning and Waste

[STATISTIC]
27% of cloud IaaS/PaaS spend is wasted — unchanged from the prior year despite FinOps adoption growth.
— Flexera, "2025 State of the Cloud Report"
URL: https://www.flexera.com/blog/finops/the-latest-cloud-computing-trends-flexera-2025-state-of-the-cloud-report/
Date: 2025

### 6f. Cognitive Bias in Build Decisions

[FACT]
Organizations "often overestimate their uniqueness, leading to unnecessary custom development."
— Harvard Business Review, November 2021 (as cited in CIO.com analysis)
URL: https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
Date: 2025

[QUOTE]
"The build trap is when organizations become stuck measuring their success by outputs rather than outcomes."
— Melissa Perri, "Escaping the Build Trap: How Effective Product Management Creates Real Value," O'Reilly, 2019
URL: https://www.goodreads.com/work/quotes/66322411-escaping-the-build-trap-how-effective-product-management-creates-real-v
Date: 2019

### 6g. Hidden Costs Summary Table

| Hidden Cost Category | Estimated Magnitude | Source |
|---|---|---|
| Technical debt as % of IT balance sheet | 20–40% of total tech estate value | McKinsey, 2023 |
| IT budget consumed by tech debt maintenance | Up to 40% | Gartner, 2024/2025 |
| Hidden costs added to initial build budget | 30–50% | UnifiedInfotech, 2025 |
| Integration costs per system connection | $5,000–$50,000 each | UprootSecurity, 2025 |
| Cloud spend wasted (IaaS/PaaS) | 27% | Flexera, 2025 |
| Average data breach cost (US) | $10.22 million | IBM, 2025 |
| GenAI POC abandonment rate | 30%+ | Gartner, 2024 |

---

## 7. Illustrative TCO Model: $500,000 Custom Build Over 5 Years

The following model is a structural illustration using the published ranges above. Actual figures will vary by organization, sector, and technical choices.

| Year | Cost Category | Estimated Range | Notes |
|---|---|---|---|
| Year 0 | Initial build (contract) | $500,000 | Baseline assumption |
| Year 0 | Scope creep / overrun (45–75% probability) | $225,000–$375,000 | McKinsey/Oxford averages |
| Year 1–5 | Annual maintenance (20% of build/year) | $100,000/year = $500,000 | McKinsey benchmark |
| Year 1–5 | Cloud infrastructure (est. mid-market) | $120,000–$480,000 total | Flexera: 27% typically wasted |
| Year 1–5 | Talent carrying cost (2 engineers × $200K loaded) | $2,000,000 total | ZipRecruiter + benefits loading |
| Year 1–5 | Turnover (23–25% annual rate, 2-person team) | $200,000–$400,000 | Replacement = 2x salary estimate |
| Year 1–5 | Security patching and incident response | $50,000–$200,000+ | IBM data breach baseline |
| Year 1–5 | Technical debt remediation | $100,000–$300,000 | Gartner 40% IT budget figure |
| **Total 5-Year TCO** | | **$3.7M–$5.75M** | **7.4x–11.5x the initial contract** |

[UNVERIFIED] — This illustrative model is a structural synthesis of published ranges, not a primary empirical study. It is provided to demonstrate order-of-magnitude magnitude, not as a precise TCO calculation for any specific organization.

---

## 8. How Agentic Coding Reshapes — But Does Not Eliminate — the TCO Stack

[STATISTIC]
"Work that once took weeks can be done in days, which shifts which ideas get funded and built."
— Anthropic, "2026 Agentic Coding Trends Report" (Trend 6), as summarized
URL: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
Date: 2026

[STATISTIC]
"Agents increasingly handle writing, testing, debugging, and documentation, while engineers focus on architecture and decision-making. Onboarding time to new codebases drops sharply."
— Anthropic, "2026 Agentic Coding Trends Report" (Trend 1)
URL: https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
Date: 2026

[STATISTIC]
Developers now use AI in 60% of their work but fully delegate only 0–20% of tasks.
— Anthropic, "2026 Agentic Coding Trends Report"
URL: https://resources.anthropic.com/2026-agentic-coding-trends-report
Date: 2026

[QUOTE]
"There's no way you can go live with a vibe-coded solution. It might work for demos, but we build enterprise-grade technology that has to scale across 30 countries."
— Pierre Yves Calloc'h, Builder, Pernod Ricard
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 17, 2026

[STATISTIC]
State-of-the-art agentic model performance: Claude 4.5 Opus achieves 74.4% resolved rate on SWE-bench (standard coding tasks), but succeeds on only 11.0% of complex feature development tasks (FeatureBench).
— FeatureBench benchmark study
URL: https://arxiv.org/html/2602.10975v1
Date: 2026

| TCO Category | Impact from Agentic Coding | Remaining Risk |
|---|---|---|
| Initial development cost | Reduced 50–90% (vendor claims); 10–50% (conservative enterprise analysis) | Overrun risk and governance overhead remain |
| Infrastructure / cloud waste | Minimal direct impact | 27% cloud waste unchanged (Flexera 2025) |
| Annual maintenance cost | Potential reduction through AI-assisted patching [UNVERIFIED] | Security vulnerability rate increases 15–18% with AI-generated code |
| Talent carrying cost | Fewer engineers needed per project (productivity gains of 20–30%) | Top engineers still required; compensation premiums rising |
| Turnover cost | Improved retention for developers with access to AI tools (48% lower attrition) | AI-skilled engineer salary premium growing |
| Technical debt accumulation | Agents may reduce initial debt if properly governed | Rapid generation of untested code can accelerate debt |
| Security patch exposure | No published reduction in patch frequency requirements | AI-generated code introduces new vulnerability classes |

---

## Key Takeaways

- The initial build contract is the smallest component of custom software TCO. Published maintenance benchmarks consistently show that 60–80% of lifetime system costs accumulate post-launch over a 5-year horizon, with annual maintenance running 15–25% of original build cost per year (McKinsey; 7T.ai, 2025).

- Agentic coding tools compress initial development cost by a published range of 50–90%, but this is the smallest share of lifetime spend. The dominant cost categories — talent carrying costs, cloud infrastructure, technical debt remediation, and security exposure — are not materially reduced by current agentic tools.

- The technical debt iceberg is the most underestimated enterprise software cost. Gartner estimates 40% of IT budgets are consumed by technical debt maintenance by 2025; McKinsey documents that CIOs see 10–40% of "new product" budgets diverted to debt remediation. Companies that actively manage tech debt can reclaim "up to 50% more" engineer time for value-generating work.

- Talent is the largest single recurring cost in a custom build. With US enterprise engineer loaded compensation at $200,000+ annually, 23–25% industry turnover rates, and replacement costs of up to 2x salary, a two-engineer maintenance team alone adds $2M+ over five years to a $500,000 build — before any infrastructure, security, or incident response costs.

- Agentic coding introduces new TCO risks that partially offset productivity gains: AI-generated code introduces 15–18% more security vulnerabilities; AI-generated pull requests wait 4.6x longer in review without governance frameworks in place; and 30%+ of GenAI proof-of-concept projects are abandoned before reaching production (Gartner, 2024).

---

## Sources

1. Flexera, "2025 State of the Cloud Report" (press release) — https://www.globenewswire.com/news-release/2025/03/19/3045271/0/en/New-Flexera-Report-Finds-that-84-of-Organizations-Struggle-to-Manage-Cloud-Spend
2. Flexera, "2025 State of the Cloud Report" (blog) — https://www.flexera.com/blog/finops/the-latest-cloud-computing-trends-flexera-2025-state-of-the-cloud-report/
3. IBM, "Cost of a Data Breach Report 2025" — https://www.ibm.com/reports/data-breach
4. IBM 2025 Data Breach Report (summary) — https://www.allcovered.com/blog/key-insights-from-ibms-2025-cost-of-a-data-breach-report
5. McKinsey & Company, "Delivering Large-Scale IT Projects On Time, On Budget, and On Value" (Bloch, Blumberg, Laartz) — https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value
6. McKinsey & Company, "Tech Debt: Reclaiming Tech Equity" — https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/tech-debt-reclaiming-tech-equity
7. McKinsey & Company, "Breaking Technical Debt's Vicious Cycle" — https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/breaking-technical-debts-vicious-cycle-to-modernize-your-business
8. McKinsey & Company, "The New Economics of Enterprise Technology in an AI World" — https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-new-economics-of-enterprise-technology-in-an-ai-world
9. McKinsey & Company, via CIO.com (Lalit Wadhwa), "How Agentic AI Will Reshape Engineering Workflows in 2026" — https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html
10. Anthropic, "2026 Agentic Coding Trends Report" — https://resources.anthropic.com/2026-agentic-coding-trends-report
11. Anthropic, "2026 Agentic Coding Trends Report" (PDF) — https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
12. Tessl.io, "8 Trends Shaping Software Engineering in 2026" (Anthropic report summary) — https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
13. Retool, "The 2026 Build vs. Buy Shift Report" — https://retool.com/blog/ai-build-vs-buy-report-2026
14. Standish Group CHAOS Report 2020 (via OpenCommons) — https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes
15. Gartner, "Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025" — https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025
16. ZipRecruiter, "Enterprise Software Engineer Salary" — https://www.ziprecruiter.com/Salaries/Enterprise-Software-Engineer-Salary
17. Ravio, "Software Engineer Salary Trends 2026" — https://ravio.com/blog/software-engineer-salary-trends
18. Lingo Live, "Cost of Turnover for Software Engineers" — https://www.lingolive.com/blog/cost-of-turnover-for-software-engineers/
19. Devsu, "Software Developer Turnover Challenges" — https://devsu.com/blog/navigating-software-developer-turnover-challenges
20. AllStarsIT, "What Employee Turnover Is Really Costing Your Tech Company" — https://www.allstarsit.com/blog/what-employee-turnover-is-really-costing-your-tech-company
21. 7T.ai, "How Much Does Software Maintenance Cost?" — https://7t.ai/blog/how-much-does-software-maintenance-cost-what-to-expect-for-apps-and-enterprise-software-maintenance/
22. AbbacusTechnologies, "Software Maintenance Costs in 2026" — https://www.abbacustechnologies.com/software-maintenance-costs-in-2026-what-you-should-expect/
23. AbbacusTechnologies, "Software Maintenance Cost" — https://www.abbacustechnologies.com/software-maintenance-cost-how-much-does-it-really-cost/
24. Leobit, "Total Cost of Ownership for Custom Software Projects" — https://leobit.com/blog/total_cost_of_ownership_for_custom_software_development/
25. METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
26. Stack Overflow Developer Survey 2025 (AI section) — https://survey.stackoverflow.co/2025/ai/
27. Times of AI, "Agentic Coding in 2026: AI's Impact on Software Development" — https://www.timesofai.com/industry-insights/agentic-coding-in-software-development/
28. Belitsoft, "Agentic AI Coding: What Still Remains Expensive" — https://belitsoft.com/agentic-ai-coding
29. FeatureBench, "Benchmarking Agentic Coding for Complex Feature Development" — https://arxiv.org/html/2602.10975v1
30. LinearB, "Is GitHub Copilot Worth It?" — https://linearb.io/blog/is-github-copilot-worth-it
31. Security Boulevard, "What Your Technical Debt Is Really Costing You" — https://securityboulevard.com/2025/12/what-your-technical-debt-is-really-costing-you/
32. Dockyard, "The Long-Term Cost of Technical Debt" — https://dockyard.com/blog/2025/05/13/the-long-term-cost-of-technical-debt-and-how-to-avoid-it
33. vFunction, "Technical Debt — Who's Responsible?" — https://vfunction.com/blog/technical-debt-whos-responsible/
34. IdeaLink, "Software Development vs Maintenance: The True Cost Equation" — https://idealink.tech/blog/software-development-maintenance-true-cost-equation
35. UnifiedInfotech, "7 Hidden Costs of Custom Software Development" — https://www.unifiedinfotech.net/blog/7-hidden-costs-of-custom-software-development-how-to-avoid-them/
36. UprootSecurity, "GRC Software Pricing Guide" — https://www.uprootsecurity.com/blog/grc-software-pricing-guide
37. ByteIota, "Cloud Waste Hits $44.5B in 2025" — https://byteiota.com/cloud-waste-hits-44-5b-in-2025-the-finops-failure/
38. Scalr, "Complete Guide to DevOps Monitoring Tools in 2025" — https://scalr.com/learning-center/the-complete-guide-to-devops-monitoring-tools-in-2025-choosing-the-right-solution-for-your-infrastructure/
39. Northflank, "Claude Code Pricing and Rate Limits" — https://northflank.com/blog/claude-rate-limits-claude-code-pricing-cost
40. Melissa Perri, "Escaping the Build Trap" (O'Reilly, 2019) — https://www.oreilly.com/library/view/escaping-the-build/9781491973783/
41. Sharma Vishal (blog), "Build vs. Buy is Dead, Start Orchestrating" — https://blog.sharmavishal.com/2025/10/build-vs-buy-is-dead-start.html
42. Raypold, "Software Development and Opportunity Cost in a Startup" — https://www.raypold.com/post/opportunity-cost-in-startups/
43. CIO.com, "Build vs. Buy: A CIO's Journey Through the Software Decision Maze" — https://www.cio.com/article/4056428/build-vs-buy-a-cios-journey-through-the-software-decision-maze.html
44. WifaTalents, "Custom Software Development Industry Statistics" — https://wifitalents.com/custom-software-development-industry-statistics/

---

*Cross-reference: See [F05 — Build vs. Buy Framework](../wave1/F05_build_vs_buy_framework.md) for detailed coverage of the strategic decision framework, competitive differentiation analysis, agentic coding's impact on the build-vs-buy calculus, and the Klarna case study.*
