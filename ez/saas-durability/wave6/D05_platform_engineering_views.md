# D05: Platform Engineering Views on SaaS vs. Build

**Research Question:** How does the platform engineering community view the SaaS-vs-build debate, and what does internal developer platform adoption signal?

**Wave:** 6 | **Date Compiled:** March 2026 | **Word Count:** ~2,100

---

## Executive Summary

The platform engineering community sits at the operational center of the SaaS-vs-build debate: these are the teams responsible for making custom software buildable at scale. Survey data through late 2025 shows near-universal adoption of internal developer platforms (IDPs) in large enterprises, with Gartner's 2026 prediction of 80% adoption already exceeded a year early. Yet the community's stance is pragmatic rather than ideological — platform engineers overwhelmingly reach for SaaS for complex, compliance-heavy, or high-uptime tooling categories while reserving custom builds for workflow-level friction points that commercial products never fully addressed. The golden path concept — opinionated, pre-approved routes for software delivery embedded in IDPs — does not replace SaaS dependencies; it abstracts and governs how developers reach them. Simultaneously, commercial IDP vendors are themselves SaaS products, with Port raising $100M at an $800M valuation in December 2025, signaling that the infrastructure enabling custom builds is itself a SaaS market.

---

## 1. Internal Developer Platform Adoption: The Numbers

[STATISTIC]
"By 2026, 80% of large software engineering organizations will establish platform engineering teams as internal providers of reusable services, components and tools for application delivery — up from 45% in 2022."
— Gartner
URL: https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering
Date: 2023 (prediction), tracked through 2025

[STATISTIC]
Nearly 90% of enterprises now have internal platforms, surpassing Gartner's 2026 prediction of 80% a full year early.
— State of Platform Engineering Vol. 4 / platformengineering.org
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[STATISTIC]
"55% of surveyed organizations have adopted platform engineering according to Google's latest report."
— Cited in multiple secondary reports
URL: https://dev.to/meena_nukala/platform-engineering-in-2026-the-numbers-behind-the-boom-and-why-its-transforming-devops-381l
Date: 2025–2026

[STATISTIC]
"Over 65% of enterprises have either built or adopted an Internal Developer Platform to improve developer experience and governance, according to a State of Platform Engineering 2024 report."
URL: https://www.cycloid.io/blog/top-11-internal-developer-platforms-idps-in-2025/
Date: 2025

[DATA POINT]
The State of Platform Engineering Vol. 4 report is based on 518 survey responses from practitioners worldwide, covering startups to large enterprises.
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[STATISTIC]
"55.9% of companies operate more than one platform."
— State of Platform Engineering Vol. 4
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[STATISTIC]
"47.4% of platform initiatives are operating with an annual budget between $0 and $1 million."
— State of Platform Engineering Vol. 4
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[STATISTIC]
"29.6% of platform teams do not measure success at all."
— State of Platform Engineering Vol. 4
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[STATISTIC]
"Over 55% of platform teams are less than two years old."
— State of Platform Engineering survey
URL: https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering
Date: 2025

---

## 2. Platform Engineering as an Enabler of Custom Software at Scale

[FACT]
The State of Platform Engineering Vol. 4 introduces "shifting down" as the defining operational concept: embedding responsibilities, controls, and guardrails directly into the platform rather than relying on developer intervention. The report characterizes platform engineering as "the foundational operating system of the modern enterprise."
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[QUOTE]
"Think about your platform like it's a SaaS product. This means thinking about what it would take to get a platform consumed and used by a thousand engineers at a very large or midsized enterprise company."
— State of Platform Engineering Vol. 4
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[STATISTIC]
"94% of organizations now view AI as critical to the future of platform engineering."
— State of Platform Engineering Vol. 4
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 16, 2025

[QUOTE]
"2026 will be the year platform engineering shifts from automation to agent-based and agentic workflows."
— Mitch Ashley, VP and Practice Leader, Futurum
URL: https://futurumgroup.com/press-release/platform-engineers-critical-to-ai-adoption-in-2026/
Date: 2025

[DATA POINT]
Futurum Research: Nearly 50% of platform engineering groups are already using AI-assisted tools or task agents. 38% of organizations are standardizing their platform engineering approach; 32% are operationalizing it; 19% have reached the mastering stage.
URL: https://futurumgroup.com/press-release/platform-engineers-critical-to-ai-adoption-in-2026/
Date: 2025

[STATISTIC]
Spotify deploys AI coding agents integrated into its fleet management system, generating over 1,500 pull requests with 60–90% time savings on migrations.
URL: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
Date: December 2025

[STATISTIC]
"Engineering teams spend 40% of their time building and maintaining internal tools."
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

---

## 3. Platform Engineers' Views: Where SaaS Is Essential vs. Replaceable

The platform engineering community does not hold a unified anti-SaaS ideology. Evidence from practitioner writing and survey data shows a bifurcated view: SaaS is preferred for regulated, high-complexity, or high-uptime domains; custom builds target narrow workflow gaps.

### Camp 1: SaaS Remains Structurally Necessary for Certain Categories

[QUOTE]
"Anything that requires very high uptime and SLAs is difficult to replace — getting to four or five 9s is really hard, and you're not going to replace Stripe and all their engineering work on core payments easily with an agent."
— Martin Alderson, Cofounder, catchmetrics.io
URL: https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
Date: 2025

[QUOTE]
"Regulation and compliance is still very important — many industries require regulatory compliance which isn't going to change overnight."
— Martin Alderson, Cofounder, catchmetrics.io
URL: https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
Date: 2025

[FACT]
Categories identified as least replaceable by platform engineering practitioners include: payment processors, high-uptime infrastructure requiring 4–5 nines, high-volume data systems, network-effect products (Slack cited), products with proprietary datasets, and regulatory/compliance-heavy solutions.
URL: https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
Date: 2025

[QUOTE]
"SaaS is the shortest path to agility, continuous innovation, and ongoing operational improvement."
URL: https://www.devopsdigest.com/platform-engineering-and-devops-for-enterprise-saas
Date: 2025

[FACT]
Enterprise-grade authentication (SSO, SAML, OAuth2) must meet standards including assertion signature validation and replay protection, with SOC2 and ISO certification auditors scrutinizing identity data handling. Building compliant flows from scratch requires extensive security hardening and documentation.
URL: https://www.scalekit.com/blog/build-vs-buy-how-to-approach-sso-for-your-saas-app
Date: 2025

### Camp 2: Custom Builds Are Accelerating for Workflow-Level Friction

[STATISTIC]
"35% of respondents have replaced functionality of at least one SaaS tool with a custom build, and 78% expect to build more of their own tools in 2026."
— Retool State of Internal Tools Report, cited in Newsweek
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[STATISTIC]
"60% reported building tools outside IT oversight in the past year."
— Retool State of Internal Tools Report, cited in Newsweek
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[STATISTIC]
"~50% of production software builders report saving six or more hours weekly."
— Retool State of Internal Tools Report, cited in Newsweek
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[QUOTE]
"The cost of building custom software has collapsed. Two years ago, a custom internal tool might take an engineering team weeks and cost six figures. Today, a business operations lead with the right platform can have a working prototype in a day or two."
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[QUOTE]
"That's a structural change, not a cyclical one. When the cost of building drops by an order of magnitude but the cost of buying stays flat, the math changes for every company."
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[QUOTE]
"Nobody's ripping out Salesforce wholesale. What they're doing is replacing the specific piece of a tool that never quite fit."
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[FACT]
Categories identified as most replaceable by platform engineering practitioners include: internal dashboards, simple CRUD-based back-office tools, analytics dashboards on customer data, video encoding services, and presentation/slideware.
URL: https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
Date: 2025

---

## 4. Backstage, Humanitec, Port, and Other IDP Tools as Build Enablers

### Backstage

[STATISTIC]
"Backstage has more than 3,400 adopters, including Airbnb, Booking.com, H&M, HCA Healthcare, LEGO, OVO Energy, Philips, Toyota North America and SeatGeek."
URL: https://www.cncf.io/projects/backstage/
Date: 2025

[STATISTIC]
"2 million developers across 3,400+ organizations now use Backstage, including Airbnb, LinkedIn, Twilio and American Airlines."
URL: https://thenewstack.io/five-years-in-backstage-is-just-getting-started/
Date: 2025

[STATISTIC]
"Backstage is the open source framework with 89% market share" in internal developer portals.
URL: https://www.cycloid.io/blog/top-11-internal-developer-platforms-idps-in-2025/
Date: 2025

[FACT]
Backstage reached version 1.42.5 as of mid-2025. It was the fourth most contributed-to CNCF project in 2024, behind only Kubernetes, OpenTelemetry, and Argo.
URL: https://platformengineering.com/social-facebook/backstage-a-mid-year-snapshot/
Date: September 11, 2025

[DATA POINT]
Spotify has launched Spotify Portal, a SaaS solution offering "a no-code UI for installing and managing plugins" for enterprise Backstage adopters.
— Tyson Singer, Spotify Head of Technology and Platforms
URL: https://engineering.atspotify.com/2025/4/celebrating-five-years-of-backstage
Date: April 2025

[QUOTE]
"IDPs are no longer optional. The only question is whether you'll roll your own, buy commercial Backstage, or skip the Backstage route entirely for a turnkey competitor."
— Alan Shimel, Platform Engineering
URL: https://platformengineering.com/social-facebook/backstage-a-mid-year-snapshot/
Date: September 11, 2025

[FACT]
Gartner estimates 2–5 full-time engineers are required for years to build custom Backstage instances; some industry reports suggest up to 20 experts over multi-year horizons.
URL: https://platformengineering.com/social-facebook/backstage-a-mid-year-snapshot/
Date: September 11, 2025

[FACT]
Backstage adoption "often stalls at less than 10% in other organizations" despite high internal adoption at Spotify. Spotify's VP of Engineering has acknowledged the adoption plateau issue.
URL: https://www.cortex.io/post/an-overview-of-spotify-backstage
Date: 2025

[FACT]
Backstage full production deployment typically requires 6–12 months and may need 3–15 full-time engineers for long-term maintenance.
— Mathew Pregasen, Technical Writer, Infisical
URL: https://infisical.com/blog/navigating-internal-developer-platforms
Date: June 21, 2025

### Humanitec

[FACT]
Humanitec is described as "the number one Platform Orchestrator" and was mentioned in nine Gartner Hype Cycles in 2024 across multiple categories. It is characterized as "an established solution for graph-based platform backends across many enterprises and Fortune 500s."
URL: https://platformengineering.org/blog/top-10-platform-engineering-tools-to-use-in-2025
Date: 2025

[DATA POINT]
Humanitec claims performance benefits for enterprise adopters: 4x higher deployment frequency, 75% less Ops overhead, and 30% faster lead time.
URL: https://humanitec.com/products/platform-orchestrator
Date: 2025

[FACT]
Humanitec runs in air-gapped, on-premises, or private cloud environments for regulated industries with full control and no external dependencies.
URL: https://humanitec.com/self-hosted
Date: 2025

### Port

[DATA POINT]
Port raised $100M in Series C funding in December 2025, achieving an $800M valuation. The round was led by General Atlantic with participation from Accel, Bessemer Venture Partners, and Team8. Total funding raised: $158M.
URL: https://www.port.io/blog/port-100m-series-c
Date: December 11, 2025

[FACT]
Port serves "hundreds of customers globally," including GitHub, British Telecom, Visa, Sonar, StubHub, Serko, and Nando's.
URL: https://siliconangle.com/2025/12/11/port-nets-100m-turn-developer-portal-agentic-ai-hub/
Date: December 11, 2025

### IDP SaaS Pricing Comparison

[DATA POINT]
IDP commercial pricing benchmarks (2025):
- Backstage/Roadie (managed): ~$22/developer/month
- OpsLevel: $39/user/month
- Cortex: ~$65–$69/user/month (enterprise)
- Atlassian Compass: ~$7/user/month (Standard plan); free tier available
— Mathew Pregasen, Infisical
URL: https://infisical.com/blog/navigating-internal-developer-platforms
Date: June 21, 2025

### Platform Tooling Category Preferences (State of Platform Engineering Vol. 3 Survey)

| Category | Leading Tool | Share | Type |
|---|---|---|---|
| Infrastructure as Code | Terraform | 71% | Open-source/SaaS |
| IaC (alt) | Crossplane | 13% | Open-source |
| Monitoring | Prometheus | 54.59% | Open-source |
| Security Scanning | Snyk | Leader | SaaS |
| Developer Portals | Backstage | 89% market share | Open-source |
| CD/GitOps | ArgoCD | Leader | Open-source |

URL: https://platformengineering.org/blog/top-10-platform-engineering-tools-to-use-in-2025
Date: 2025

---

## 5. Platform Engineers' Stance: Build or Buy?

[QUOTE]
"The true objective is simple: Make it easier to deliver workloads, enhance the developer experience. Many engineering teams conflate 'building the platform' with the ultimate goal."
— Will Stewart, Co-founder/CEO, Northflank
URL: https://platformengineering.com/editorial-calendar/best-of-2025/build-vs-buy-the-platform-engineers-conundrum-2/
Date: 2025

[FACT]
The article uses game development as an analogy: studios historically built custom engines but now predominantly use Unreal or Unity, reserving in-house development for specialized needs. The implication: building custom IDP infrastructure parallels building a proprietary game engine — possible, but rarely optimal.
URL: https://platformengineering.com/editorial-calendar/best-of-2025/build-vs-buy-the-platform-engineers-conundrum-2/
Date: 2025

[QUOTE]
"Building your own Backstage from scratch is like building your own Linux distribution — you can do it, but most people would rather pay for Ubuntu or Red Hat."
URL: https://www.devopsdigest.com/platform-engineering-and-devops-for-enterprise-saas
Date: 2025

[QUOTE]
"The question is whether it's the best use of your time and resources."
— Will Stewart, Co-founder/CEO, Northflank
URL: https://platformengineering.com/editorial-calendar/best-of-2025/build-vs-buy-the-platform-engineers-conundrum-2/
Date: 2025

[FACT]
The platform engineering community consensus on the build vs. buy decision in 2025 centers on a single operative rule: invest engineering talent in core differentiators; buy SaaS for non-differentiating context (payroll, email marketing, IT procurement). The reverse — building custom software for commodity functions — is described as "allocating scarce resources to a non-differentiating activity."
URL: https://platformengineering.com/editorial-calendar/best-of-2025/build-vs-buy-the-platform-engineers-conundrum-2/
Date: 2025

[QUOTE]
"if your product is just a SQL wrapper on a billing system, you now have thousands of competitors"
— Martin Alderson, Cofounder, catchmetrics.io (on AI-enabled SaaS displacement)
URL: https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
Date: 2025

[QUOTE]
"The bar for purchased software just got permanently higher."
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[QUOTE]
"The default question shifts from 'What should we buy?' to 'Can we build this?'"
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

---

## 6. The Golden Path Concept and Its Implications for SaaS

[FACT]
A "golden path" is defined as a preconfigured, paved road that provides an end-to-end workflow for developers. Golden paths are a key component of IDPs. They are described as "opinionated, well-documented, and supported" ways of building and deploying software within an organization.
— Mallory Haigh, Principal Platform Therapist, Platform Engineering
URL: https://platformengineering.org/blog/what-are-golden-paths-a-guide-to-streamlining-developer-workflows
Date: 2025

[QUOTE]
"IDPs create a self-service 'golden path' for development."
URL: https://infisical.com/blog/navigating-internal-developer-platforms
Date: June 21, 2025

[FACT]
Backstage Scaffolder creates software templates based on golden paths. At Spotify, software templates are described as "fundamental to the concept of Golden Paths at Spotify, representing the opinionated and supported way to build something (for example, a backend service, website, or data pipeline)."
URL: https://backstage.spotify.com/discover/backstage-101
Date: 2025

[FACT]
Portal (Spotify's SaaS product) allows creation of standardized templates for building backend services and websites, enabling developers to "spin up new projects that follow Golden Paths in seconds."
URL: https://backstage.spotify.com/products/portal/
Date: 2025

[FACT]
Golden paths in IDPs abstract away infrastructure complexity, but they do not eliminate SaaS dependencies — they govern how developers reach them. Pre-approved templates and automation make compliant defaults the easiest choice, incorporating security and compliance controls from the underlying SaaS layer (cloud providers, identity providers, observability vendors).
URL: https://infisical.com/blog/navigating-internal-developer-platforms
Date: June 21, 2025

[DATA POINT]
Red Hat characterizes golden paths as delivering five primary benefits: reducing cognitive load by abstracting infrastructure complexity; improving consistency and reliability; accelerating development cycles via self-service; enhancing security and compliance with pre-approved paths; and increasing developer satisfaction.
URL: https://www.redhat.com/en/topics/platform-engineering/golden-paths
Date: March 10, 2025

[QUOTE]
"The goal is not to create a 'golden cage,' but rather to provide a 'golden path'."
URL: https://platformengineering.org/blog/what-are-golden-paths-a-guide-to-streamlining-developer-workflows
Date: 2025

[FACT]
Platform engineers earn up to 27% more than DevOps professionals, according to compensation data cited alongside golden path tooling documentation.
URL: https://platformengineering.org/blog/what-are-golden-paths-a-guide-to-streamlining-developer-workflows
Date: 2025

---

## 7. The Paradox: IDP Tools Are Themselves SaaS

[DATA POINT]
The leading IDP tools — Port ($100M Series C, $800M valuation), Humanitec, OpsLevel, Cortex, Roadie, Atlassian Compass — are all SaaS or commercially licensed products. The infrastructure enabling enterprises to build custom software is itself a SaaS market.
URL: https://techcrunch.com/2025/12/11/port-raises-100m-at-800m-valuation-to-take-on-spotifys-backstage/
Date: December 11, 2025

[QUOTE]
"Shadow IT at this scale is a demand signal."
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[QUOTE]
"The most underestimated risk is what happens after deployment. The real risk isn't the individual tool, but the ungoverned sprawl."
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[QUOTE]
"Advanced maturity means building is the default, not the exception. It happens inside a governed environment with full visibility."
— David Hsu, CEO, Retool
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

[FACT]
37% of organizations lack established AI productivity metrics.
— Retool State of Internal Tools Report, cited in Newsweek
URL: https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
Date: 2025

---

## Key Takeaways

- **IDP adoption has exceeded Gartner's 2026 prediction early**: Nearly 90% of enterprises now have internal platforms, driven by the need to standardize software delivery and govern AI adoption — not primarily to replace SaaS subscriptions.

- **Golden paths govern SaaS access, not replace it**: The golden path abstraction layer in IDPs enforces pre-approved tooling choices (often SaaS), manages compliance, and reduces cognitive load — but does not eliminate underlying SaaS dependencies for security, identity, observability, or payment infrastructure.

- **Build is accelerating only at the workflow layer**: 35% of enterprises have replaced at least one SaaS tool's functionality with custom builds, but the replacements target narrow friction points — approval flows, dashboards, administrative panels — not core systems. "Nobody's ripping out Salesforce wholesale."

- **The IDP tooling market is itself a SaaS market**: Port's $100M Series C at an $800M valuation, Humanitec's enterprise deployments, Roadie's managed Backstage service, and Spotify Portal all represent significant SaaS investment enabling custom software creation — a recursive dependency on SaaS that complicates any pure "build replaces buy" narrative.

- **Compliance, high-uptime, and network-effect categories retain structural SaaS moats**: Platform engineering practitioners consistently identify payment processors, regulatory compliance tooling, identity/authentication, and high-volume infrastructure as categories where SaaS cannot be cost-effectively replicated, regardless of agentic coding capability.

---

## Sources

1. Gartner — Platform Engineering topic page: https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering
2. State of Platform Engineering Vol. 4 announcement: https://platformengineering.org/blog/announcing-the-state-of-platform-engineering-vol-4
3. State of Platform Engineering Vol. 4 report page: https://platformengineering.org/reports/state-of-platform-engineering-volume-4
4. Meena Nukala, DEV Community — "Platform Engineering in 2026": https://dev.to/meena_nukala/platform-engineering-in-2026-the-numbers-behind-the-boom-and-why-its-transforming-devops-381l
5. Cycloid — "Top 11 Internal Developer Platforms in 2025": https://www.cycloid.io/blog/top-11-internal-developer-platforms-idps-in-2025/
6. Futurum Research — "Platform Engineers Critical To AI Adoption In 2026": https://futurumgroup.com/press-release/platform-engineers-critical-to-ai-adoption-in-2026/
7. Newsweek / Adam Mills — "Enterprises Are Replacing SaaS Faster Than You Think": https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483
8. Platform Engineering.com — "Build vs. Buy: The Platform Engineer's Conundrum": https://platformengineering.com/editorial-calendar/best-of-2025/build-vs-buy-the-platform-engineers-conundrum-2/
9. Martin Alderson — "AI agents are starting to eat SaaS": https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
10. Alan Shimel, Platform Engineering — "Backstage, a Mid-Year Snapshot": https://platformengineering.com/social-facebook/backstage-a-mid-year-snapshot/
11. Tyson Singer, Spotify Engineering — "Celebrating Five Years of Backstage": https://engineering.atspotify.com/2025/4/celebrating-five-years-of-backstage
12. CNCF — Backstage project page: https://www.cncf.io/projects/backstage/
13. The New Stack — "Five Years In, Backstage Is Just Getting Started": https://thenewstack.io/five-years-in-backstage-is-just-getting-started/
14. Cortex — "An Overview of Spotify Backstage": https://www.cortex.io/post/an-overview-of-spotify-backstage
15. Mathew Pregasen, Infisical — "Navigating Internal Developer Platforms in 2025": https://infisical.com/blog/navigating-internal-developer-platforms
16. Humanitec — Platform Orchestrator: https://humanitec.com/products/platform-orchestrator
17. Humanitec — Self-Hosted: https://humanitec.com/self-hosted
18. Port — $100M Series C announcement: https://www.port.io/blog/port-100m-series-c
19. SiliconANGLE — "Port nets $100M to turn its developer portal into an agentic AI hub": https://siliconangle.com/2025/12/11/port-nets-100m-turn-developer-portal-agentic-ai-hub/
20. TechCrunch — "Port raises $100M at $800M valuation": https://techcrunch.com/2025/12/11/port-raises-100m-at-800m-valuation-to-take-on-spotifys-backstage/
21. Mallory Haigh, Platform Engineering — "What are golden paths": https://platformengineering.org/blog/what-are-golden-paths-a-guide-to-streamlining-developer-workflows
22. Red Hat — "What is a Golden Path for software development": https://www.redhat.com/en/topics/platform-engineering/golden-paths
23. Spotify for Backstage — Backstage 101: https://backstage.spotify.com/discover/backstage-101
24. Spotify Portal: https://backstage.spotify.com/products/portal/
25. Sam Barlien, Platform Engineering — "Top 10 platform engineering tools to use in 2025": https://platformengineering.org/blog/top-10-platform-engineering-tools-to-use-in-2025
26. DEVOPSdigest — "Platform Engineering and DevOps for Enterprise SaaS": https://www.devopsdigest.com/platform-engineering-and-devops-for-enterprise-saas
27. Scalekit — "Build vs. Buy: SSO strategies for B2B SaaS apps": https://www.scalekit.com/blog/build-vs-buy-how-to-approach-sso-for-your-saas-app
28. Red Hat — "Designing Golden Paths": https://www.redhat.com/en/blog/designing-golden-paths
