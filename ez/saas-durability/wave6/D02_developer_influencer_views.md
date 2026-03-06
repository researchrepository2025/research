# D02: Developer Influencer Views on SaaS Durability and the Build-vs-Buy Shift

**Research Wave:** Wave 6 — Developer Thought Leader Perspectives
**Date Compiled:** March 6, 2026
**Scope:** Developer influencers, platform leaders, and community discourse on SaaS replacement via agentic coding. AI researchers and enterprise technology leaders are out of scope (see D01 and Wave 3 respectively).

---

## Executive Summary

Prominent developer thought leaders in 2025–2026 are converging on a thesis that AI-assisted and agentic coding meaningfully shifts the build-vs-buy calculus, but their positions diverge sharply on the scope and permanence of that shift. DHH's "post-SaaS" thesis — rooted in his earlier "leave the cloud" parallel — has gained renewed credibility as coding agents matured through 2025, with DHH himself calling agentic coding "the most exciting thing we've made computers do since we connected them to the internet." Pieter Levels personifies the indie-hacker-as-SaaS-replacement narrative, generating ~$3M/year as a solo developer using AI tools. Platform leaders like Guillermo Rauch (Vercel) argue the transition creates opportunity rather than destruction, predicting "kingdoms collapse" among companies that cannot adapt to agentic interfaces. Empirical data from the Retool 2026 Build vs. Buy Report (n=817) shows 35% of enterprise teams have already replaced at least one SaaS tool with a custom build, while Stack Overflow's 2025 Developer Survey finds 77% of professional developers still do not engage in vibe coding for their production work — suggesting the narrative outpaces current enterprise reality. The discourse reveals a genuine repricing and displacement of narrow, commoditized SaaS categories while complex, compliance-heavy, and network-effect software shows durable resistance.

---

## Terminology Glossary

- **Agentic coding:** AI systems that autonomously write, debug, and deploy software beyond autocomplete
- **SaaS replacement:** Thesis that enterprises can build custom apps to replace SaaS subscriptions
- **Enterprise-grade:** Meeting Fortune 500 requirements (security, compliance, reliability, scalability, support SLAs)
- **Vibe coding:** Coined by Andrej Karpathy — fully prompt-driven development where the developer "gives in to the vibes" and accepts AI-generated code without deep review
- **Vibe engineering / Agentic engineering:** Simon Willison's counter-term for disciplined use of AI coding agents by experienced engineers who remain accountable for the output

---

## Section 1: DHH and the "Leave the Cloud" Parallel

David Heinemeier Hansson (DHH), co-founder of 37signals and creator of Ruby on Rails, is the most prominent developer voice constructing an ideological framework linking infrastructure ownership, software ownership, and now AI-assisted custom development as a unified alternative to SaaS dependency.

### The "Over-SaaSed" Thesis [PRE-2025 — included as foundational context for 2025–2026 positions]

[QUOTE]
"I think we're over SaaSed."
— David Heinemeier Hansson, 37signals
URL: https://www.cmcmarkets.com/en-gb/opto/were-over-saased-37signals-david-heinemeier-hansson-on-the-end-of-the-subscription-era
Date: December 2023

[QUOTE]
"In the early 2000s, we were among the early pioneers leading the industry into the SaaS revolution. Now, 20 years later, we intend to help lead the way out. The post–SaaS era is just around the corner."
— 37signals announcement introducing ONCE product line
URL: https://www.webpronews.com/37signals-wants-to-introduce-the-post-saas-era/
Date: December 2023

[FACT]
37signals launched ONCE, a new product line operating on principles including: one-time payments for perpetual ownership; visible/transparent source code; customer ability to self-host. This was positioned as a direct alternative to monthly SaaS subscription models.
URL: https://37signals.com/podcast/37signals-introduces-once/
Date: December 2023

[QUOTE]
DHH described SaaS as entering customers into "a perpetual landlord-tenant agreement where every month you pay for essentially the same thing, and if you stop paying, the software stops working."
— David Heinemeier Hansson, quoted in CMC Markets/Opto
URL: https://www.cmcmarkets.com/en-gb/opto/were-over-saased-37signals-david-heinemeier-hansson-on-the-end-of-the-subscription-era
Date: December 2023

### DHH on Leaving the Cloud — The Infrastructure Parallel

[FACT]
37signals announced a full exit from AWS and cloud infrastructure starting in 2022, citing annual cloud bills exceeding $3.2 million. By transitioning to owned hardware, 37signals estimated $7 million in savings over five years.
URL: https://thenewstack.io/merchants-of-complexity-why-37signals-abandoned-the-cloud/
Date: December 2023

[FACT]
In October 2024, 37signals estimated it had saved $2 million that year by exiting the cloud, with monthly spend reduced by approximately 60% — from ~$180,000 to less than $80,000.
URL: https://www.trgdatacenters.com/resource/37signals-expected-to-make-seven-million-leaving-cloud/
Date: 2024

[QUOTE]
DHH stated he is "on a mission to break down the misconception that owning your own hardware is exotic and difficult. That is just not true."
— David Heinemeier Hansson
URL: https://summithq.com/why-companies-like-37signals-leaving-cloud/
Date: 2023–2024

### DHH's 2025–2026 Evolution: Embracing AI Agents

DHH's position on AI coding shifted materially through 2025, moving from skepticism to qualified enthusiasm as coding agent capabilities improved.

[QUOTE]
"The code being produced by this new breed of AI is leagues ahead of where their predecessors were at the beginning of 2025."
— David Heinemeier Hansson, hey.com/dhh blog
URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
Date: January 7, 2026

[QUOTE]
"They're fully capable of producing production-grade contributions to real-life code bases."
— David Heinemeier Hansson, on AI coding agents
URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
Date: January 7, 2026

[QUOTE]
"This is the most exciting thing we've made computers do since we connected them to the internet back in the '90s."
— David Heinemeier Hansson
URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
Date: January 7, 2026

[QUOTE]
"It's more like working on a team and less like working with an overly-zealous pair programmer who can't stop stealing the keyboard."
— David Heinemeier Hansson, on AI coding agents in January 2026
URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
Date: January 7, 2026

[QUOTE]
"I'm nowhere close to the claims of having agents write 90%+ of the code, as I see some boast about online. I don't know what code they're writing to hit those rates, but that's way off what I'm able to achieve, if I hold the line on quality and cohesion."
— David Heinemeier Hansson
URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
Date: January 7, 2026

[QUOTE]
"Supervised collaboration, though, is here today. Pure vibe coding remains an aspirational dream for professional work for me, for now."
— David Heinemeier Hansson
URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
Date: January 7, 2026

[QUOTE]
"Right now, we're probably at peak AI future hype."
— David Heinemeier Hansson
URL: https://thenewstack.io/dhh-on-ai-vibe-coding-and-the-future-of-programming/
Date: 2025

[FACT]
DHH described AI agents as gaining capabilities "beyond pure reasoning" in late 2025 — specifically: controlling the terminal, running tests, searching the web for documentation, and using web services.
URL: https://world.hey.com/dhh/promoting-ai-agents-3ee04945
Date: January 7, 2026

[DATA POINT]
37signals went "all-in on Omarchy" — their own Arch-derived Linux distribution — as part of a broader pattern of replacing commercial software dependencies with custom-controlled alternatives, announced August 2025.
URL: https://world.hey.com/dhh
Date: August 9, 2025

**Analyst Note on the Cloud-SaaS Parallel:** DHH's "leave the cloud" move is frequently cited in 2025–2026 developer discourse as a template for the "leave SaaS" movement. The logic is identical: rent vs. own, vendor dependency vs. sovereignty, predictable costs vs. escalating subscriptions. DHH himself draws this parallel explicitly through the ONCE product line and his infrastructure writing.

---

## Section 2: Pieter Levels and the "Indie Hacker Replaces SaaS" Narrative

Pieter Levels (@levelsio) is the most cited solo-developer embodiment of the thesis that AI coding tools enable individuals to build bespoke software in place of SaaS subscriptions.

### Revenue and Scale Data Points

[STATISTIC]
Pieter Levels generates approximately $3 million per year across multiple products with zero employees as of 2025.
URL: https://www.fast-saas.com/blog/pieter-levels-success-story/
Date: 2025

[STATISTIC]
Levels' Photo AI product generates approximately $138,000/month as of November 2025, representing approximately 70% of his total income.
URL: https://buildloop.ai/how-pieter-levels-runs-multiple-1m-ai-products-with-automation-zero-team/
Date: 2025

[FACT]
Levels built fly.pieter.com — an MMO flight simulator — in approximately 30 minutes using AI-assisted tools. The product scaled to hundreds of thousands of users and consistently generates over $50,000/month.
URL: https://www.indiehackers.com/post/tech/pieter-levels-used-ai-to-build-a-viral-flight-simulator-in-3-hours-with-no-background-in-game-development-7CPfMr1yRLEwH6cC8xhE
Date: 2025

[FACT]
Levels announced and ran the 2025 Vibe Code Game Jam, where dozens of indie hackers shipped viral games in hours using AI tools including Claude, Grok 3, and Cursor.
URL: https://www.indiehackers.com/post/tech/pieter-levels-just-announced-the-winners-of-the-2025-vibe-code-game-jam-Uz0wHG4pI3KBOiFhP5YR
Date: 2025

### The Lex Fridman Podcast Context

[FACT]
Pieter Levels appeared on Lex Fridman Podcast #440 ("Programming, Viral AI Startups, and Digital Nomad Life") in August 2024 [PRE-2025 — included as the most-cited public articulation of his indie-hacker-as-SaaS-alternative thesis]. The episode received significant developer community attention through 2025.
URL: https://lexfridman.com/pieter-levels/
Date: August 2024

[QUOTE]
Levels on his approach to funding and independence: founder friends with hundreds of millions in funding have told him "they would do it his way next time because 'it's more fun, it's more indie, it's more chill, it's more creative'."
— Pieter Levels, Lex Fridman Podcast #440
URL: https://lexfridman.com/pieter-levels-transcript/
Date: August 2024

### Industry Interpretation of the Levels Model

[QUOTE]
"Indie hacking isn't dead — it's the new normal."
— Attributed to Pieter Levels framing in developer community discourse
URL: https://medium.com/@maxslashwang/pieter-levels-indie-hacking-isnt-dead-it-s-the-new-normal-294182efed96
Date: September 2025

[FACT]
The narrative around Levels in 2025 developer communities centers on his tech stack — Vanilla PHP, jQuery, SQLite — combined with AI coding tools (Cursor, Claude, Grok) as evidence that modern AI tools allow high-output solo development without enterprise-grade engineering teams.
URL: https://www.systemscowboy.com/pieter-levels-indie-hacker-strategy/
Date: 2025

**Scope Caveat:** The "indie hacker replaces SaaS" narrative, as embodied by Levels, applies primarily to consumer-facing and SMB-targeted products. His products (Nomad List, Photo AI, Remote OK) are not enterprise software with compliance, SSO, audit logging, or SLA requirements. The direct applicability to Fortune 500 build-vs-buy decisions is contested in developer discourse (see Section 6).

---

## Section 3: Platform Leaders — Guillermo Rauch (Vercel), Matt Mullenweg (WordPress)

### Guillermo Rauch (Vercel)

Guillermo Rauch, CEO and founder of Vercel, represents the "platform infrastructure" camp: AI doesn't eliminate the need for deployment, observability, and developer tooling — it dramatically expands who builds and what they build.

[QUOTE]
"Every company will have an agentic interface. But it won't just be on your turf, your .com. It'll also be on @slack, @discord, @microsoftteams, @googleworkspace, and more."
— Guillermo Rauch, post on X
URL: https://x.com/rauchg/status/2026379919643848876
Date: 2025

[QUOTE]
"In the next three years we're going to see kingdoms collapse in the sense of, like, you know, companies that were born on the internet that have not been able to make those adjustments fast enough, and the new AI native companies rise to, as we were speaking earlier, like, to unprecedented heights very, very quickly."
— Guillermo Rauch, Sequoia Capital Training Data podcast
URL: https://sequoiacap.com/podcast/training-data-guillermo-rauch/
Date: November 2025

[QUOTE]
"If I was a digital native and I came to market with a SaaS-style dashboard UI, if I came to market with a marketing website and a content website, et cetera, you must be asking yourself the hard question of, like, all right, if I was reinvented today, my interface would probably be agentic."
— Guillermo Rauch, Sequoia Capital Training Data podcast
URL: https://sequoiacap.com/podcast/training-data-guillermo-rauch/
Date: November 2025

[QUOTE]
"Everything will be ephemeral, for that matter...the web as the place where everything will be generative just in time."
— Guillermo Rauch
URL: https://sequoiacap.com/podcast/training-data-guillermo-rauch/
Date: November 2025

[QUOTE]
"I'm Team Fully Generative Software forever."
— Guillermo Rauch
URL: https://sequoiacap.com/podcast/training-data-guillermo-rauch/
Date: November 2025

[QUOTE]
"Your future customers may be AI agents as much as humans. APIs and frameworks need to be agent-friendly."
— Guillermo Rauch
URL: https://sequoiacap.com/podcast/training-data-guillermo-rauch/
Date: November 2025

[QUOTE]
"We have prevented tens of thousands of such vulnerabilities...a thousand vulnerabilities prevented per day."
— Guillermo Rauch, on v0's built-in code quality controls
URL: https://sequoiacap.com/podcast/training-data-guillermo-rauch/
Date: November 2025

[STATISTIC]
Vercel's v0 grew to 3 million users as a platform for AI-assisted web application generation.
URL: https://www.lennysnewsletter.com/p/everyones-an-engineer-now-guillermo-rauch
Date: 2025

[FACT]
Rauch's stated mission for v0 is to expand the pool of potential builders from 5 million professional developers to over 100 million people worldwide.
URL: https://www.lennysnewsletter.com/p/everyones-an-engineer-now-guillermo-rauch
Date: 2025

### Matt Mullenweg (WordPress / Automattic)

Matt Mullenweg, CEO of Automattic and co-founder of WordPress, represents a parallel "democratize building" thesis at the open-source CMS layer.

[QUOTE]
"Things that you used to have to, like, hire developers, do custom software like this would have cost thousands, tens of thousands of dollars to build, even just years ago. We're now able to do in a browser for pennies."
— Matt Mullenweg, WordCamp US 2025 keynote
URL: https://techcrunch.com/2025/09/02/wordpress-shows-off-telex-its-experimental-ai-development-tool/
Date: September 2025

[QUOTE]
Mullenweg described Telex (WordPress's AI development tool) as "a V0 or Lovable, but specifically for WordPress."
— Matt Mullenweg, State of the Word 2025
URL: https://techcrunch.com/2025/12/03/wordpresss-vibe-coding-experiment-telex-has-already-been-put-to-real-world-use/
Date: December 2025

[QUOTE]
"When we think about democratized publishing, like embedded in that, is very core to WordPress' mission, has been taking things that were difficult to do, that required knowledge of coding or anything else, and…made it accessible to people."
— Matt Mullenweg
URL: https://techcrunch.com/2025/09/02/wordpress-shows-off-telex-its-experimental-ai-development-tool/
Date: September 2025

[QUOTE]
"As writing code is becoming easier, designing software becomes more important than ever."
— Endorsed by Matt Mullenweg (attributed to Chris Lattner), from WordPress AI blog post
URL: https://ma.tt/2026/02/wp-ai/
Date: February 2026

[QUOTE]
"As custom software becomes cheaper to create, the real challenge becomes choosing the right problems and managing the resulting complexity."
— Matt Mullenweg's blog (ma.tt)
URL: https://ma.tt/2026/02/wp-ai/
Date: February 2026

[FACT]
In 2026, WordPress planned to introduce benchmarks and evaluations that AI models can use to test on WordPress tasks (changing plugins, editing text, manipulating the WordPress interface using browser agents) — positioning WordPress as an agentic-web-ready platform.
URL: https://ma.tt/2026/02/wp-ai/
Date: February 2026

[FACT]
WordPress's Telex tool was described by early testers as still needing significant work, with "several test projects" failing or requiring additional fixes before production use.
URL: https://techcrunch.com/2025/12/03/wordpresss-vibe-coding-experiment-telex-has-already-been-put-to-real-world-use/
Date: December 2025

---

## Section 4: Developer Twitter/X Discourse Patterns on SaaS Replacement

### The "I Can Build That" Pattern

[QUOTE]
"Demand is starting to evaporate for simpler SaaS tools, as many software engineers are realizing they can get an agent to solve in a few minutes what they would previously find a freemium or paid service for."
— Martin Alderson, Cofounder of catchmetrics.io
URL: https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
Date: 2025

[QUOTE]
"Software ate the world. Agents are going to eat SaaS."
— Martin Alderson
URL: https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
Date: 2025

[QUOTE]
"If a product is just a SQL wrapper on a billing system, companies now have thousands of competitors: engineers at customers with a spare Friday afternoon with an agent."
— Hacker News discussion on AI agents and SaaS, paraphrased from thread
URL: https://news.ycombinator.com/item?id=46268452
Date: 2025

### The Counter-Position: "Enterprise Can't Build That"

[QUOTE]
"The threat model assumes customers can build their own tools, but many end users can't — their current 'system' is Excel."
— Hacker News commenter, "AI agents are starting to eat SaaS" thread
URL: https://news.ycombinator.com/item?id=46268452
Date: 2025

[QUOTE]
"Agents are a multiplier on existing velocity rather than an equalizer."
— Hacker News commenter
URL: https://news.ycombinator.com/item?id=46268452
Date: 2025

### The Repricing Narrative

[QUOTE]
"The 'repricing mechanism' is more useful than a 'SaaS apocalypse' narrative — some developers report running AI agents that handle tasks they used to do manually or pay for, but the agent itself costs around $400/month in API fees, compressing individual tool spending while increasing inference costs."
— Developer community synthesis, Hacker News
URL: https://news.ycombinator.com/item?id=46268452
Date: 2025

### Products Identified as Durable vs. Replaceable (Developer Community Consensus)

| Category | Developer Consensus | Source |
|---|---|---|
| Back-office CRUD / simple admin tools | High replacement risk | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |
| Simple analytics dashboards | High replacement risk | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |
| High-uptime payments (e.g. Stripe) | Durable moat | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |
| Network-effect software (e.g. Slack) | Durable moat | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |
| High-volume data infrastructure | Durable moat | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |
| Proprietary-dataset products | Durable moat | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |
| Regulatory/compliance-heavy tools | Durable moat | https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/ |

### Build vs. Buy Survey Data — Retool 2026

[STATISTIC]
35% of enterprise teams have already replaced at least one SaaS tool with a custom build, per the Retool 2026 Build vs. Buy Report (n=817 builders surveyed in late 2025).
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
78% of enterprise respondents expect to build more custom internal tools in 2026.
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
SaaS categories with highest replacement pressure: workflow automations (35%), internal admin tools (33%), BI tools (29%).
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
60% of builders created tools outside IT oversight in the past year; 25% report doing so frequently.
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
Reasons for shadow IT build activity: 31% can build faster than IT approval; 25% cite existing SaaS as insufficient; 18% cite IT processes as too slow.
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
93% of survey respondents use LLMs for coding or building. ChatGPT: 70%; Gemini: 56%; Claude: 53%; GitHub Copilot: 39%; Cursor: 35%.
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[STATISTIC]
51% of respondents have built production software currently in use with AI assistance; 49% of those save 6+ hours weekly.
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[QUOTE]
"We realized we could build these tools ourselves and save on multiple subscriptions."
— Borys Aptekar, GTM AI Product Manager at ClickUp
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[QUOTE]
"Their support was so slow that it was faster for me to rebuild the product inside Retool than wait."
— Miles Konstantin, Head of Automation at Harmonic
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

[QUOTE]
"There's no way you can go live with a vibe-coded solution. It might work for demos, but we build enterprise-grade technology that has to scale across 30 countries."
— Pierre Yves Calloc'h, Pernod Ricard
URL: https://retool.com/blog/ai-build-vs-buy-report-2026
Date: February 2026

---

## Section 5: YouTube and Podcast Thought Leaders

### Fireship (Jeff Delaney)

[FACT]
Jeff Delaney's Fireship channel reached 4.06 million subscribers as of December 2025, making it one of the largest developer-focused YouTube channels. Fireship produced a video titled "How AI is breaking the SaaS business model..." as of early 2026, directly addressing the thesis.
URL: https://read.engineerscodex.com/p/how-fireship-became-youtubes-favorite
Date: December 2025

### ThePrimeagen (Michael Paulson)

[FACT]
ThePrimeagen (former Netflix engineer, prominent developer influencer) built "99," a Neovim AI agent plugin that trended at #1 on GitHub with 542 stars in a single day on January 31, 2026. The project was described as "for people without skill issues" — a deliberate counter-positioning against tools that remove developer agency.
URL: https://byteiota.com/theprimeagens-99-hits-542-stars-day-ai-for-skilled-devs/
Date: January 2026

[FACT]
ThePrimeagen's "The Standup" podcast covered topics including: "How WE Use AI," "What even is an AI Agent?!", "Why building a real agent isn't just weekend work," and security tradeoffs in early AI-assisted development through 2025–2026.
URL: https://creators.spotify.com/pod/profile/thestanduppod/episodes/How-WE-Use-AI-e3504eg
Date: 2025–2026

### Theo Browne (t3dotgg)

[QUOTE]
Theo Browne on the post-vibe-coding landscape: "Building is no longer the moat. Taste is" and "Distribution is still a superpower. Maybe the only one."
— Theo Browne, developer influencer (t3dotgg)
URL: https://t3.gg/
Date: 2025

[FACT]
Browne has noted that "niches are shifting with people vibe-coding their own tools on Bolt, Lovable, etc." and that tools like Claude, o3, Devin, Cursor, Lovable, bolt.new, and Replit enable "From idea → prototype → launch in a weekend."
URL: https://gitnation.com/person/theo_browne
Date: 2025

### Acquired Podcast / Sequoia Training Data

[FACT]
Guillermo Rauch appeared on the Acquired podcast ("Building Web Apps with Just English and AI") — a top-ranked technology podcast — as well as Sequoia Capital's Training Data podcast, both in 2025, where his "kingdoms collapse" and "agentic interface" theses received wide developer and investor community amplification.
URL: https://www.acquired.fm/episodes/building-web-apps-with-just-english-and-ai-with-vercel-ceo-guillermo-rauch
Date: 2025

---

## Section 6: The "Vibe Coding" Meme and Its Enterprise Implications

### Origin and Cultural Reach

[QUOTE]
"There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."
— Andrej Karpathy, co-founder of OpenAI, post on X
URL: https://x.com/karpathy/status/1886192184808149383
Date: February 2, 2025

[QUOTE]
Karpathy elaborated: "I 'Accept All' always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it...Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away."
— Andrej Karpathy
URL: https://x.com/karpathy/status/1886192184808149383
Date: February 2, 2025

[FACT]
"Vibe coding" was selected as Collins Dictionary's Word of the Year 2025 in November 2025, described as having "resonated far beyond Silicon Valley, speaking to a broader cultural shift toward AI-assisted everything in everyday life."
URL: https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/
Date: November 2025

[FACT]
Collins Dictionary defined "vibe coding" as: "software development that turns natural language into computer code using AI."
URL: https://www.cnn.com/2025/11/06/tech/vibe-coding-collins-word-year-scli-intl
Date: November 2025

### Developer Community Pushback on Vibe Coding for Enterprise

[QUOTE]
Simon Willison, prominent developer and creator of Datasette: "Vibe coding your way to a production codebase is clearly risky. Most of the work we do as software engineers involves evolving existing systems, where the quality and understandability of the underlying code is crucial."
— Simon Willison, simonwillison.net
URL: https://simonwillison.net/2025/Mar/19/vibe-coding/
Date: March 2025

[QUOTE]
Willison on the distinction: "If an LLM wrote every line of your code, but you've reviewed, tested, and understood it all, that's not vibe coding in my book—that's using an LLM as a typing assistant."
— Simon Willison
URL: https://simonwillison.net/2025/Mar/19/vibe-coding/
Date: March 2025

[QUOTE]
Willison on vibe engineering (his counter-term): "The fast, loose and irresponsible way of building software with AI—entirely prompt-driven" [describing vibe coding], versus vibe engineering where "seasoned professionals accelerate their work with LLMs while staying proudly and confidently accountable for the software they produce."
— Simon Willison, simonwillison.net
URL: https://simonwillison.net/2025/Oct/7/vibe-engineering/
Date: October 2025

[QUOTE]
Willison: "AI tools amplify existing expertise — skilled engineers gain the most value from LLM integration, making these tools fundamentally different from commodified automation."
— Simon Willison
URL: https://simonwillison.net/2025/Oct/7/vibe-engineering/
Date: October 2025

[FACT]
Simon Willison noted in late 2025 that the term "Agentic Engineering" was emerging to supersede "vibe engineering" as the descriptor for disciplined AI-assisted professional development.
URL: https://simonwillison.net/2025/Oct/7/vibe-engineering/
Date: October 2025

### Expert Position Camps on Vibe Coding and Enterprise

#### "Vibe Coding Enables SaaS Replacement" Camp

**Andrej Karpathy**, co-founder OpenAI — Coined the term; advocates fully prompt-driven development as a legitimate methodology, enabling software creation without traditional programming expertise. ([Source](https://x.com/karpathy/status/1886192184808149383), February 2025)

**Pieter Levels**, serial indie hacker / founder of Nomad List, Photo AI — Personifies the model: solo developer generating ~$3M/year, building complete products in hours using AI coding tools, with no engineering team. ([Source](https://buildloop.ai/how-pieter-levels-runs-multiple-1m-ai-products-with-automation-zero-team/), 2025)

**Theo Browne (t3dotgg)**, developer influencer — Acknowledges vibe coding enables rapid prototyping to production, but repositions the competitive moat as "taste" and "distribution" rather than coding ability. ([Source](https://t3.gg/), 2025)

#### "Vibe Coding Is Not Enterprise-Grade" Camp

**Simon Willison**, creator of Datasette, co-creator of Django — Coined "vibe engineering" as the disciplined alternative; argues production codebases require maintainability and accountability that vibe coding structurally undermines. ([Source](https://simonwillison.net/2025/Oct/7/vibe-engineering/), October 2025)

**Pierre Yves Calloc'h**, Pernod Ricard — "There's no way you can go live with a vibe-coded solution. It might work for demos, but we build enterprise-grade technology that has to scale across 30 countries." ([Source](https://retool.com/blog/ai-build-vs-buy-report-2026), February 2026)

**DHH**, 37signals — "Pure vibe coding remains an aspirational dream for professional work for me, for now." Maintains that quality and cohesion require supervised collaboration, not full AI autonomy. ([Source](https://world.hey.com/dhh/promoting-ai-agents-3ee04945), January 2026)

#### "Qualified Enthusiasm / Platform Transformation" Camp

**Guillermo Rauch**, CEO Vercel — Argues traditional SaaS UI is being displaced by agentic interfaces, creating "kingdoms collapse" among non-adaptive incumbents, but positions platform infrastructure as more important than ever. ([Source](https://sequoiacap.com/podcast/training-data-guillermo-rauch/), November 2025)

**Matt Mullenweg**, CEO Automattic / WordPress — Frames AI coding democratization as an extension of WordPress's core mission; acknowledges enterprise complexity ("managing the resulting complexity") while championing accessibility gains. ([Source](https://ma.tt/2026/02/wp-ai/), February 2026)

### Stack Overflow 2025 Survey: Gap Between Discourse and Practice

[STATISTIC]
72% of professional developers report that vibe coding — generating entire applications from prompts — is "not part of their professional work." An additional 5% "emphatically" reject it. Combined: 77% of developers do not engage in production vibe coding.
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

[STATISTIC]
80% of developers now use AI tools in their workflows, but only approximately 15% have adopted vibe coding (full prompt-to-app) to any degree.
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

[STATISTIC]
Trust in AI coding accuracy declined year-over-year: from 40% to 29%. Positive favorability toward AI tools dropped from 72% to 60%.
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

[STATISTIC]
45% of developers cite frustration with "AI solutions that are almost right, but not quite." 66% spend more time fixing flawed AI-generated code.
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

[STATISTIC]
52% of developers say AI agents have affected how they complete their work; 69% of those using agents report increased personal productivity.
URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
Date: December 2025

### Security Concerns in Vibe-Coded Enterprise Applications

[STATISTIC]
45% of AI-generated code contains security vulnerabilities; 40% has exploitable bugs, per security analysis of vibe-coded applications.
URL: https://www.baytechconsulting.com/blog/ai-vibe-coding-security-risk-2025
Date: 2025

[STATISTIC]
Vibe-coded applications show 41% higher code churn rates versus traditionally developed applications.
URL: https://www.secondtalent.com/resources/vibe-coding-statistics/
Date: 2026

[STATISTIC]
Industry adoption of vibe coding by sector: Tech startups 73%; Digital agencies 61%; E-commerce 57%. Regulated industries significantly lower: Financial services 34%; Healthcare 28%.
URL: https://www.secondtalent.com/resources/vibe-coding-statistics/
Date: 2026

---

## Section 7: The Sam Altman "One-Person Unicorn" Meme in Developer Discourse

[QUOTE]
"We're going to see 10-person companies with billion-dollar valuations pretty soon…in my little group chat with my tech CEO friends there's this betting pool for the first year there is a one-person billion-dollar company, which would've been unimaginable without AI. And now [it] will happen."
— Sam Altman, CEO OpenAI, in interview with Reddit co-founder Alexis Ohanian
URL: https://techcrunch.com/2025/02/01/ai-agents-could-birth-the-first-one-person-unicorn-but-at-what-societal-cost/
Date: February 2025

[FACT]
Altman's "one-person unicorn" prediction became a reference point in developer community discussions throughout 2025, amplified by Pieter Levels' actual solo-developer revenue milestones as partial validation.
URL: https://medium.com/practice-in-public/why-sam-altman-believes-gpt5-will-create-the-first-1-billion-one-person-business-5d7205061288
Date: 2025

---

## Key Takeaways

- **The vibe coding meme has cultural traction but limited enterprise production adoption.** Collins Word of the Year 2025, yet 77% of professional developers report it is not part of their production work (Stack Overflow 2025 Developer Survey). The discourse narrative significantly outpaces current enterprise practice.

- **DHH's "leave the cloud" parallel is the closest ideological template for "leave the SaaS" movements.** DHH's January 2026 post signals he now considers AI agents mature enough for "production-grade contributions" — this matters because he was previously the most prominent skeptic. His adoption of agentic coding (while cautioning against "pure vibe coding") gives the build-vs-buy shift intellectual legitimacy in the developer community.

- **The Retool 2026 Build vs. Buy Report provides the most concrete enterprise data point:** 35% of teams have already replaced at least one SaaS tool with a custom build (n=817, late 2025). Categories most at risk — workflow automations, internal admin tools, BI dashboards — align precisely with what developer influencers identify as "SQL wrappers" and "CRUD apps."

- **Platform leaders (Rauch, Mullenweg) frame AI coding as expanding the builder pool, not eliminating software.** Rauch's "kingdoms collapse" quote targets SaaS incumbents that fail to adapt their UI paradigm from dashboard to agentic interface — not a claim that all SaaS is replaceable. This is a qualitatively different thesis from Levels' or DHH's ownership arguments.

- **Security, compliance, and complexity create a durable floor for enterprise SaaS.** Developer community consensus (Hacker News, Simon Willison, Pernod Ricard's Calloc'h) identifies network-effect software, high-uptime payment infrastructure, compliance-heavy tools, and proprietary-dataset products as resistant to the build-vs-buy shift. The regulated industry adoption gap (financial services 34%, healthcare 28% versus tech startups 73%) is the empirical signal.

---

## Sources

1. DHH hey.com blog — "Promoting AI agents" (January 7, 2026): https://world.hey.com/dhh/promoting-ai-agents-3ee04945
2. DHH hey.com main blog: https://world.hey.com/dhh
3. 37signals ONCE announcement (December 2023): https://37signals.com/podcast/37signals-introduces-once/
4. WebProNews — "37signals Wants to Introduce the 'Post–SaaS' Era": https://www.webpronews.com/37signals-wants-to-introduce-the-post-saas-era/
5. CMC Markets/Opto — "We're over-SaaSed": https://www.cmcmarkets.com/en-gb/opto/were-over-saased-37signals-david-heinemeier-hansson-on-the-end-of-the-subscription-era
6. The New Stack — "Merchants of Complexity: Why 37Signals Abandoned the Cloud": https://thenewstack.io/merchants-of-complexity-why-37signals-abandoned-the-cloud/
7. TRG Datacenters — "37signals Expected to Save $7 Million Leaving the Cloud": https://www.trgdatacenters.com/resource/37signals-expected-to-make-seven-million-leaving-cloud/
8. Summit HQ — "Why companies like 37signals are leaving the cloud": https://summithq.com/why-companies-like-37signals-leaving-cloud/
9. This Week in Startups — DHH on "Post-SaaS era" (E1856): https://thisweekinstartups.com/episodes/K1UDZBzSDXY
10. Dexa.ai — DHH Episode 1856 summary: https://dexa.ai/thisweekinstartups/d/4787137a-9096-11ee-a7e4-5bed01e93b40
11. Retool 2026 Build vs. Buy Report blog: https://retool.com/blog/ai-build-vs-buy-report-2026
12. BusinessWire — Retool 2026 Build vs. Buy press release: https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
13. Andrej Karpathy on X — vibe coding original post: https://x.com/karpathy/status/1886192184808149383
14. Simon Willison — "Vibe coding" post: https://simonwillison.net/2025/Mar/19/vibe-coding/
15. Simon Willison — "Vibe engineering" post (October 2025): https://simonwillison.net/2025/Oct/7/vibe-engineering/
16. Simon Willison Substack: https://simonw.substack.com/p/vibe-engineering
17. Collins Dictionary — Word of the Year 2025 (vibe coding): https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/
18. CNN — "Vibe coding named Collins Dictionary's Word of the Year": https://www.cnn.com/2025/11/06/tech/vibe-coding-collins-word-year-scli-intl
19. The Register — "Vibe coding named word of the year. Developers faceplant": https://www.theregister.com/2025/11/06/vibe_coding_escape_the_clutches/
20. Sequoia Capital — "Vercel's Guillermo Rauch: Building the Generative Web with AI" (November 2025): https://sequoiacap.com/podcast/training-data-guillermo-rauch/
21. Sequoia Inference Substack — Guillermo Rauch podcast summary: https://inferencebysequoia.substack.com/p/vercel-ceo-guillermo-rauch-building
22. Guillermo Rauch on X — "Every company will have an agentic interface": https://x.com/rauchg/status/2026379919643848876
23. Lenny's Newsletter — "Everyone's an engineer now: Guillermo Rauch" (2025): https://www.lennysnewsletter.com/p/everyones-an-engineer-now-guillermo-rauch
24. Acquired podcast — "Building Web Apps with Just English and AI" (Guillermo Rauch): https://www.acquired.fm/episodes/building-web-apps-with-just-english-and-ai-with-vercel-ceo-guillermo-rauch
25. Matt Mullenweg blog — "wp-ai" (February 2026): https://ma.tt/2026/02/wp-ai/
26. TechCrunch — "WordPress shows off Telex" (September 2025): https://techcrunch.com/2025/09/02/wordpress-shows-off-telex-its-experimental-ai-development-tool/
27. TechCrunch — "WordPress's vibe-coding experiment, Telex, has already been put to real-world use" (December 2025): https://techcrunch.com/2025/12/03/wordpresss-vibe-coding-experiment-telex-has-already-been-put-to-real-world-use/
28. WordPress State of the Word 2025: https://wordpress.org/news/2025/12/sotw-2025/
29. Martin Alderson — "AI agents are starting to eat SaaS": https://martinalderson.com/posts/ai-agents-are-starting-to-eat-saas/
30. Hacker News — "AI agents are starting to eat SaaS" discussion: https://news.ycombinator.com/item?id=46268452
31. Hacker News — "AI is killing B2B SaaS" discussion: https://news.ycombinator.com/item?id=46888441
32. Pieter Levels — Fast SaaS blog ($3M/year story): https://www.fast-saas.com/blog/pieter-levels-success-story/
33. Pieter Levels — Buildloop AI analysis: https://buildloop.ai/how-pieter-levels-runs-multiple-1m-ai-products-with-automation-zero-team/
34. Pieter Levels — Indie Hackers (flight simulator): https://www.indiehackers.com/post/tech/pieter-levels-used-ai-to-build-a-viral-flight-simulator-in-3-hours-with-no-background-in-game-development-7CPfMr1yRLEwH6cC8xhE
35. Pieter Levels — Vibe Code Game Jam 2025: https://www.indiehackers.com/post/tech/pieter-levels-just-announced-the-winners-of-the-2025-vibe-code-game-jam-Uz0wHG4pI3KBOiFhP5YR
36. Lex Fridman Podcast #440 — Pieter Levels transcript: https://lexfridman.com/pieter-levels-transcript/
37. Medium — "Pieter Levels: Indie hacking isn't dead" (September 2025): https://medium.com/@maxslashwang/pieter-levels-indie-hacking-isnt-dead-it-s-the-new-normal-294182efed96
38. Stack Overflow Blog — 2025 Developer Survey results (December 2025): https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
39. Stack Overflow — 2025 Developer Survey main: https://survey.stackoverflow.co/2025/
40. Bay Tech Consulting — "AI Vibe Coding: Why 45% of AI-Generated Code is a Security Risk": https://www.baytechconsulting.com/blog/ai-vibe-coding-security-risk-2025
41. Second Talent — "Top Vibe Coding Statistics & Trends [2026]": https://www.secondtalent.com/resources/vibe-coding-statistics/
42. TechCrunch — "SaaS in, SaaS out: Here's what's driving the SaaSpocalypse" (March 1, 2026): https://techcrunch.com/2026/03/01/saas-in-saas-out-heres-whats-driving-the-saaspocalypse/
43. TechCrunch — "AI agents could birth the first one-person unicorn" (February 2025): https://techcrunch.com/2025/02/01/ai-agents-could-birth-the-first-one-person-unicorn-but-at-what-societal-cost/
44. ByteIota — ThePrimeagen "99" plugin (January 2026): https://byteiota.com/theprimeagens-99-hits-542-stars-day-ai-for-skilled-devs/
45. ThePrimeagen "99" GitHub repo: https://github.com/ThePrimeagen/99
46. Engineers Codex — "How Fireship became YouTube's favorite programmer": https://read.engineerscodex.com/p/how-fireship-became-youtubes-favorite
47. Theo Browne / t3.gg: https://t3.gg/
48. Belitsoft — "Enterprise Vibe Coding vs SaaS": https://belitsoft.com/vibe-coding-enterprise-saas
49. CIO.inc — "Enterprises Shift to Personal Software Through Vibe Coding": https://www.cio.inc/enterprises-shift-to-personal-software-through-vibe-coding-a-30291
50. Genpact — "Turning vibe-coding into enterprise value": https://www.genpact.com/insight/turning-vibe-coding-into-enterprise-value
