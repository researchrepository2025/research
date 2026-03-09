# D01: AI Researcher Views on Software Creation and the SaaS Debate

## Executive Summary

Prominent AI researchers have staked out sharply divergent positions on AI's capacity to create software — and by extension, its implications for the SaaS market. Andrej Karpathy has articulated the most sweeping thesis, framing natural language as the new programming interface ("Software 3.0") and declaring the current period the "Decade of Agents," while simultaneously cautioning that true human-replacement agents remain a decade away. Dario Amodei (Anthropic CEO, not a pure researcher but deeply embedded in the research community) made the boldest near-term prediction: 90% of code written by AI within 3–6 months of March 2025, a claim partially validated internally but contested externally. Yann LeCun, by contrast, argues that LLMs are a dead-end architecture that cannot achieve the reliability, planning, or reasoning required for dependable enterprise software. Independent empirical research (METR, July 2025) has found that AI tools produced a 19% slowdown — not speedup — for experienced developers on complex real-world tasks, underscoring a persistent gap between researcher projections and measured enterprise outcomes. The weight of evidence suggests AI researchers are accurate about the direction of travel but frequently miscalibrated on timelines, and their optimism about software creation capability is substantially more credible for greenfield, well-specified tasks than for the complex, security-critical, multi-system integration work that defines enterprise SaaS.

---

## Andrej Karpathy: The "Software 3.0" Thesis

### The Three Eras of Software

[FACT]
Karpathy presented the "Software 3.0" framework at Y Combinator's AI Startup School, San Francisco, on June 16–19, 2025, in a keynote titled "Software in the Era of AI."
— Y Combinator / Latent Space
URL: https://www.latent.space/p/s3
Date: June 2025

[QUOTE]
"Software 1.0" = explicit code in languages like Python or C++. "Software 2.0" = neural networks trained on data. "Software 3.0" = LLMs programmable in natural language (English).
— Andrej Karpathy, YC AI Startup School keynote
URL: https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again
Date: June 2025

[QUOTE]
"Software 3.0 is eating 1.0/2.0."
— Andrej Karpathy, YC AI Startup School
URL: https://www.latent.space/p/s3
Date: June 2025

[QUOTE]
"A huge amount of software will be rewritten."
— Andrej Karpathy, YC AI Startup School
URL: https://www.latent.space/p/s3
Date: June 2025

### Natural Language as the New Programming Interface

[QUOTE]
"The hottest new programming language is English."
— Andrej Karpathy (@karpathy), X (formerly Twitter)
URL: https://x.com/karpathy/status/1617979122625712128
Date: January 24, 2023 [PRE-2025 — included as the origin point of the thesis that Karpathy expanded upon throughout 2025]

[FACT]
The tweet received nearly 4 million views and was quoted by The New Yorker. Merriam-Webster listed Karpathy's related coinage "vibe coding" as a "slang & trending" expression in March 2025; Collins English Dictionary named it Word of the Year 2025.
— Wikipedia / Quote Investigator
URL: https://en.wikipedia.org/wiki/Vibe_coding
Date: 2025

[QUOTE]
"The hottest new programming language is English" is the distillation of Software 3.0's core thesis: LLMs as "new computers" programmable not with code but with human language, dramatically lowering the entry barrier and enabling anyone with an idea to create software.
— StartupHub.ai summary of Karpathy's YC talk
URL: https://www.startuphub.ai/ai-news/artificial-intelligence/2025/software-3-0-the-english-revolution-in-computing
Date: June 2025

### Vibe Coding

[QUOTE]
"There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good."
— Andrej Karpathy (@karpathy), X
URL: https://x.com/karpathy/status/1886192184808149383
Date: February 2, 2025

[FACT]
Karpathy described vibe coding as: accepting all AI changes automatically without reading diffs, copying and pasting error messages to fix bugs, with code growing beyond his usual comprehension, and sometimes working around bugs or asking for random changes until they disappear.
— Analytics Vidhya / Wikipedia (Vibe Coding)
URL: https://en.wikipedia.org/wiki/Vibe_coding
Date: 2025

[QUOTE]
"Programming is not strictly reserved for highly trained professionals, it is something anyone can do."
— Andrej Karpathy, 2025 LLM Year in Review
URL: https://karpathy.bearblog.dev/year-in-review-2025/
Date: December 2025

[QUOTE]
"Code is suddenly free, ephemeral, malleable, discardable after single use."
— Andrej Karpathy, 2025 LLM Year in Review
URL: https://karpathy.bearblog.dev/year-in-review-2025/
Date: December 2025

### Agentic Engineering and the Decade of Agents

[QUOTE]
"This is the Decade of Agents." / "2025–2035 is the decade of agents."
— Andrej Karpathy, YC AI Startup School keynote
URL: https://www.techmeme.com/250619/p25
Date: June 2025

[QUOTE]
"We're entering the decade of agents. As LLMs continue to improve and become more accessible, they won't just be tools, they will become agents capable of autonomous actions."
— Andrej Karpathy, YC AI Startup School keynote (as summarized by Orcus4AI)
URL: https://orcus4ai.com/Andrej-Karpathy's-Vision-of-Software-3.0-at-YC-AI-Startup-School_ar=023
Date: June 2025

[FACT]
Karpathy described "vibe coding" as superseded by "agentic engineering" for professional AI-assisted development in later 2025 coverage.
— The New Stack
URL: https://thenewstack.io/vibe-coding-is-passe/
Date: 2025

[QUOTE]
Claude Code "emerged as the first convincing demonstration of what an LLM Agent looks like — something that strings together tool use and reasoning."
— Andrej Karpathy, 2025 LLM Year in Review
URL: https://karpathy.bearblog.dev/year-in-review-2025/
Date: December 2025

### LLM Nature, Limitations, and the Demo-Product Gap

[QUOTE]
Karpathy characterized LLMs as "people spirits" — stochastic simulations of human cognition. "We're building ghosts or spirits or whatever people want to call it, because we're not doing training by evolution. We're doing training by imitation of humans and the data that they've put on the Internet. You end up with these ethereal spirit entities because they're fully digital and they're mimicking humans."
— Andrej Karpathy, Dwarkesh Podcast (October 2025)
URL: https://www.dwarkesh.com/p/andrej-karpathy
Date: October 2025

[QUOTE]
"Some things work extremely well (by human standards) while some things fail catastrophically." [On "Jagged Intelligence"]
— Andrej Karpathy, YC AI Startup School / Latent Space summary
URL: https://www.latent.space/p/s3
Date: June 2025

[QUOTE]
LLMs are "a bit like a coworker with Anterograde amnesia — they don't consolidate or build long-running knowledge."
— Andrej Karpathy, YC AI Startup School / Latent Space summary
URL: https://www.latent.space/p/s3
Date: June 2025

[QUOTE]
"Demo is works.any(), product is works.all()."
— Andrej Karpathy, YC AI Startup School
URL: https://www.latent.space/p/s3
Date: June 2025

[QUOTE]
"Every single nine is the same amount of work." [On reliability from 90% to 99% to 99.9%]
— Andrej Karpathy, as cited in Superagent blog "The March of Nines"
URL: https://www.superagent.sh/blog/the-march-of-nines
Date: 2025

[QUOTE]
"The agents are pretty good, for example, if you're doing boilerplate stuff...they're very good at stuff that occurs very often on the Internet because there are lots of examples of it in the training sets."
— Andrej Karpathy, Dwarkesh Podcast
URL: https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
Date: October 2025

[QUOTE]
"The models have so many cognitive deficits...they kept misunderstanding the code because they have too much memory from all the typical ways of doing things on the Internet."
— Andrej Karpathy, Dwarkesh Podcast
URL: https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
Date: October 2025

[QUOTE]
"They don't have continual learning. You can't just tell them something and they'll remember it."
— Andrej Karpathy, Dwarkesh Podcast
URL: https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
Date: October 2025

### AGI and Agent Timeline

[QUOTE]
"It will take about a decade to work through all of those issues." [Regarding full human-replacement agent capabilities]
— Andrej Karpathy, Dwarkesh Podcast
URL: https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
Date: October 2025

[FACT]
The Dwarkesh Podcast interview was titled "AGI is still a decade away" — Karpathy's own framing for where the technology stands as of October 2025.
— Dwarkesh Podcast
URL: https://www.dwarkesh.com/p/andrej-karpathy
Date: October 2025

---

## Dario Amodei: The Optimist/Practitioner Camp

[QUOTE]
"If I look at coding, programming, which is one area where AI is making the most progress, what we are finding is we are not far from the world — I think we'll be there in three to six months — where AI is writing 90 percent of the code."
— Dario Amodei, CEO Anthropic, Council on Foreign Relations forum
URL: https://finance.yahoo.com/news/anthropic-ceo-says-ai-could-193020957.html
Date: March 10, 2025

[QUOTE]
"Within a year AI might be writing 'essentially all of the code'."
— Dario Amodei, Council on Foreign Relations forum
URL: https://felloai.com/anthropic-ceo-dario-amodei-ai-will-replace-90-of-developers-in-6-months/
Date: March 10, 2025

[QUOTE]
"6 months ago I made this prediction that, you know, in 6 months 90% of code would be written by AI models. Some people think that prediction is wrong, but within Anthropic and within a number of companies that we work with, that is absolutely true."
— Dario Amodei, conversation with Marc Benioff (September 2025)
URL: https://officechai.com/ai/dario-amodei-had-predicted-90-of-code-would-be-written-by-ai-but-now-at-anthropic-its-effectively-100-anthropic-cpo/
Date: September 2025

[FACT]
Anthropic's CPO stated that internally, AI-written code had reached "effectively 100%" by late 2025.
— OfficeChai
URL: https://officechai.com/ai/dario-amodei-had-predicted-90-of-code-would-be-written-by-ai-but-now-at-anthropic-its-effectively-100-anthropic-cpo/
Date: 2025

[FACT]
IT Pro reported that Amodei's prediction "is nowhere nearly to becoming a reality" in external enterprise settings as of mid-2025.
— IT Pro
URL: https://www.itpro.com/technology/artificial-intelligence/anthropic-ceo-dario-amodei-ai-generated-code
Date: 2025

[QUOTE]
Amodei, writing in "Machines of Loving Grace" (October 2024 [PRE-2025] — included because it is the foundational text for his worldview, widely cited through 2025): AI will be able to "write extremely good novels, write difficult codebases from scratch" and "can be given tasks that take hours, days, or weeks to complete, and then goes off and does those tasks autonomously."
— Dario Amodei, darioamodei.com
URL: https://darioamodei.com/essay/machines-of-loving-grace
Date: October 2024 [PRE-2025]

---

## Geoffrey Hinton: The "Godfather" Warning Camp

[QUOTE]
"On a coding project, for example, AI can do in minutes what used to take an hour."
— Geoffrey Hinton, CNN State of the Union interview
URL: https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
Date: December 28, 2025

[QUOTE]
"AI's progression is such that after every seven months or so, it is able to complete tasks that took twice as long as before."
— Geoffrey Hinton, CNN State of the Union interview
URL: https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
Date: December 28, 2025

[QUOTE]
"In a few years, AI will be able to perform software engineering tasks that now need a month's worth of labor. And then there'll be very few people needed for software engineering projects."
— Geoffrey Hinton, CNN State of the Union interview
URL: https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
Date: December 28, 2025

[QUOTE]
"I think we're going to see AI get even better. It's already extremely good. We're going to see it having the capabilities to replace many, many jobs."
— Geoffrey Hinton, CNN State of the Union interview
URL: https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
Date: December 28, 2025

[QUOTE]
"I'm probably more worried. It's progressed even faster than I thought."
— Geoffrey Hinton, CNN State of the Union interview
URL: https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/
Date: December 28, 2025

[FACT]
Hinton warned specifically that AI could soon replace mid-level programmers, while maintaining that the underlying math, statistics, and systems thinking from a CS degree "will remain valuable for quite a long time."
— ts2.tech summary of Hinton's statements
URL: https://ts2.tech/en/godfather-of-ai-geoffrey-hinton-why-computer-science-degrees-still-matter-in-the-age-of-ai-and-vibe-coding/
Date: 2025

---

## Demis Hassabis: The Measured Optimist Camp

[QUOTE]
"A year from now, we will have agents that are 'close' to reliably accepting and completing entire delegated tasks."
— Demis Hassabis, Google DeepMind CEO, interview with Axios' Mike Allen
URL: https://dev.to/aniruddhaadak/the-future-according-to-demis-hassabis-key-predictions-on-agi-agents-and-the-ferocious-race-4313
Date: December 7, 2025

[QUOTE]
"The whole industry has talked a lot about agents and more autonomous systems and delegating whole tasks to them. But I think maybe by the end of this year, we'll really start seeing that."
— Demis Hassabis, Fortune interview
URL: https://fortune.com/article/fortune-500-titans-and-disruptors-google-deepmind-demis-hassabis-isomorphic-artificial-intelligence/
Date: Early 2026

[FACT]
Hassabis predicted AI models are "very close" to being able to "one-shot" commercial-grade games, and that users would soon be able to "vibe code" games in a few hours that previously took years to develop.
— DEV Community summary of Axios interview
URL: https://dev.to/aniruddhaadak/the-future-according-to-demis-hassabis-key-predictions-on-agi-agents-and-the-ferocious-race-4313
Date: December 7, 2025

[FACT]
Hassabis defines AGI as a system that demonstrates "consistent, cross-domain brilliance in reasoning, creativity, planning, and problem-solving" and gives it a 50% probability of arriving by 2030.
— Marketing AI Institute / CNBC
URL: https://www.cnbc.com/2025/03/17/human-level-ai-will-be-here-in-5-to-10-years-deepmind-ceo-says.html
Date: March 17, 2025

---

## Yann LeCun: The Structural Skeptic Camp

[QUOTE]
"LLMs are useful, but they are an off ramp on the road to human-level AI. If you are a PhD student, don't work on LLMs. Try to discover methods that would lift the limitations of LLMs."
— Yann LeCun (@ylecun), X
URL: https://x.com/ylecun/status/1796982509567180927
Date: 2024 [PRE-2025 — included as the canonical statement of LeCun's structural position, elaborated throughout 2025]

[QUOTE]
"I'm not interested in LLMs anymore — they're the past. The future is in four more interesting areas: machines that understand the physical world, persistent memory, reasoning, and planning."
— Yann LeCun, as cited on X
URL: https://x.com/ylecun/status/1911604721267114206
Date: April 2025

[FACT]
LeCun identifies four key limitations of current LLMs for enterprise software: "a lack of understanding of the physical world; a lack of persistent memory; a lack of reasoning; and a lack of complex planning capabilities."
— Newsweek / Analytics India Magazine
URL: https://www.newsweek.com/nw-ai/ai-impact-interview-yann-lecun-llm-limitations-analysis-2054255
Date: 2025

[QUOTE]
LeCun acknowledges LLMs are useful for coding assistants but warns: "when it comes time to actually deploy a system that's reliable enough that you put it in the hands of people and they use it on a daily basis, there's a big distance. It's much harder to make those systems reliable enough."
— Yann LeCun, as cited in Newsweek
URL: https://www.newsweek.com/nw-ai/ai-impact-interview-yann-lecun-llm-limitations-analysis-2054255
Date: 2025

[FACT]
LeCun stated he is no longer interested in large language models, calling them "a product-driven technology that is reaching its limits." He predicts a "new paradigm of AI architectures" within 3–5 years and a "decade of robotics."
— TechCrunch
URL: https://techcrunch.com/2025/01/23/metas-yann-lecun-predicts-a-new-ai-architectures-paradigm-within-5-years-and-decade-of-robotics/
Date: January 23, 2025

[FACT]
LeCun founded Advanced Machine Intelligence (AMI) in late 2025 after leaving Meta, targeting a €3 billion valuation and seeking €500 million to pursue "world model" AI as an alternative to LLMs.
— Fortune / AI Business Weekly
URL: https://fortune.com/2025/12/19/yann-lecun-ami-labs-ai-startup-valuation-meta-departure/
Date: December 2025

---

## Ilya Sutskever: The Post-Scaling Skeptic Camp

[QUOTE]
"We're moving from the age of scaling to the age of research."
— Ilya Sutskever, CEO Safe Superintelligence (SSI), Dwarkesh Podcast
URL: https://www.dwarkesh.com/p/ilya-sutskever-2
Date: November 2025

[QUOTE]
"We are squarely an 'age of research' company. We are making progress."
— Ilya Sutskever, Dwarkesh Podcast
URL: https://www.dwarkesh.com/p/ilya-sutskever-2
Date: November 2025

[QUOTE]
On AI coding specifically: "And it introduces a second bug. Then you tell it, 'You have this new second bug,' and it tells you, 'Oh my God, how could I have done it?'" [Describing the failure mode of LLMs iterating on code]
— Ilya Sutskever, Dwarkesh Podcast
URL: https://www.dwarkesh.com/p/ilya-sutskever-2
Date: November 2025

[QUOTE]
"These models somehow just generalize dramatically worse than people. It's a very fundamental thing."
— Ilya Sutskever, Dwarkesh Podcast
URL: https://www.dwarkesh.com/p/ilya-sutskever-2
Date: November 2025

[FACT]
Safe Superintelligence Inc. raised $2 billion and reached a $32 billion valuation in March 2025. Sutskever's stated mission is "safe superintelligent AI" as a single, undiluted goal.
— Wikipedia (Safe Superintelligence Inc.)
URL: https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc.
Date: 2025

---

## The "Natural Language is the New Programming Language" Thesis: Comparative Positions

| Researcher | Position on NL-as-Programming | Timescale | Key Qualification |
|---|---|---|---|
| Andrej Karpathy | Strong endorsement — "Software 3.0" era | Decade of agents (2025–2035) | Jagged intelligence; demo vs. product gap |
| Dario Amodei | Very strong — 90% of code by AI now | Already true internally | External enterprise data contested |
| Geoffrey Hinton | Agrees capability advancing rapidly | "Few years" for SE replacement | CS fundamentals remain valuable |
| Demis Hassabis | Measured — agents close to reliable delegation | By end of 2026 | Currently "close" but not there yet |
| Yann LeCun | Disagrees — LLMs structural dead-end | New architectures needed (3–5 yrs) | Reliability gap is fundamental, not incremental |
| Ilya Sutskever | Partial skeptic — scaling plateau reached | Research era, no timeline given | Generalization failure is fundamental |

---

## Benchmark Data: What the Numbers Actually Show

[STATISTIC]
On SWE-bench (industry-standard software engineering benchmark): AI systems solved 4.4% of coding problems in 2023; the figure jumped to 71.7% in 2024.
— Stanford HAI AI Index 2025
URL: https://hai.stanford.edu/ai-index/2025-ai-index-report
Date: 2025

[STATISTIC]
On BigCodeBench: AI systems achieve a 35.5% success rate, well below the human standard of 97%.
— Stanford HAI AI Index 2025
URL: https://hai.stanford.edu/ai-index/2025-ai-index-report
Date: 2025

[STATISTIC]
In short time-horizon settings (2 hours), top AI systems score four times higher than human experts on programming tasks; at 32-hour time horizons, humans outperform AI 2-to-1.
— Stanford HAI AI Index 2025
URL: https://hai.stanford.edu/ai-index/2025-ai-index-report
Date: 2025

[STATISTIC]
METR randomized controlled trial (July 2025): 16 experienced developers, 246 issues, averaging ~2 hours each, on large open-source repositories (22,000+ GitHub stars, 1M+ lines of code). Using Cursor Pro with Claude 3.5/3.7 Sonnet. Result: developers using AI tools took **19% longer** to complete issues compared to working without AI.
— METR Research Blog
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

[QUOTE]
"When developers are allowed to use AI tools, they take 19% longer to complete issues — a significant slowdown that goes against developer beliefs and expert forecasts."
— METR Research Blog
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

[STATISTIC]
Perception gap: In the METR study, developers expected AI to speed them up by 24%. After experiencing a slowdown, they still believed AI had helped by 20%.
— METR Research Blog
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
Date: July 10, 2025

---

## How AI Researchers' Views Differ from Practitioners and Enterprise Leaders

### The Researcher-Practitioner Gap

[STATISTIC]
73% of VPs said they have considered replacing people resources with AI; only 18% of Managers said the same — illustrating the hierarchy-level divergence between abstract optimism and operational reality.
— Enterprise AI survey data cited in Solutions Review
URL: https://solutionsreview.com/ai-and-enterprise-technology-predictions-from-industry-experts-for-2026/
Date: 2025/2026

[STATISTIC]
Only 19% of enterprise respondents described their organizations as having "advanced AI automation maturity."
— Glean / Enterprise AI survey
URL: https://www.glean.com/perspectives/will-ai-agents-replace-saas-tools-as-the-new-operating-layer-of-work
Date: 2025

[FACT]
A study by Upwork researchers found that agents powered by top LLMs from OpenAI, Google DeepMind, and Anthropic "failed to complete many straightforward workplace tasks by themselves," contrasting with researcher predictions about agents joining the workforce in 2025.
— Solutions Review
URL: https://solutionsreview.com/ai-and-enterprise-technology-predictions-from-industry-experts-for-2026/
Date: 2025/2026

[STATISTIC]
More than 80% of AI projects fail — twice the rate of failure for IT projects that do not involve AI; 42% of companies abandoned most of their AI initiatives in 2024–2025, up from 17% a year earlier.
— WebProNews, citing various enterprise reports
URL: https://www.webpronews.com/gary-marcus-calls-the-ai-boom-a-scam-and-the-numbers-are-starting-to-back-him-up/
Date: 2025

[FACT]
67% of enterprises admit they don't have complete visibility into which AI tools their employees are using; only 31% report having comprehensive AI governance frameworks in place.
— Enterprise AI survey data (Techreviewer.co)
URL: https://techreviewer.co/blog/ai-in-software-development-2025-from-exploration-to-accountability-a-global-survey-analysis
Date: 2025

### Gary Marcus: The Empirical Skeptic

[FACT]
Gary Marcus, cognitive scientist and AI critic, authored "AI Agents have, so far, mostly been a dud" and argued that today's agents remain unreliable and overhyped outside narrow domains.
— Gary Marcus Substack
URL: https://garymarcus.substack.com/p/ai-agents-have-so-far-mostly-been
Date: 2025

[FACT]
Marcus's mathematical critique of agent reliability: even at 95% per-step success rate, a 20-step agentic workflow has only a ~36% chance of completing without error. Production enterprise systems typically require 99.9%+ overall reliability.
— Project Syndicate / WebProNews summary of Marcus's arguments
URL: https://www.project-syndicate.org/magazine/generative-ai-fundamentally-unreliable-and-with-no-apparent-solution-by-gary-marcus-2025-06
Date: June 2025

[QUOTE]
Marcus predicts: "Companies will continue to experiment with AI, but adoption to production-grade systems scaled out in the real-world will continue to be tentative."
— Gary Marcus, 25 AI Predictions for 2025
URL: https://garymarcus.substack.com/p/25-ai-predictions-for-2025-from-marcus
Date: January 2025

---

## Credibility and Limitations of Researcher Predictions for Enterprise Outcomes

### Where Researcher Predictions Have Proven Accurate

[FACT]
SWE-bench performance jumped from 4.4% (2023) to 71.7% (2024), validating researcher optimism about benchmark trajectory.
— Stanford HAI AI Index 2025
URL: https://hai.stanford.edu/ai-index/2025-ai-index-report
Date: 2025

[FACT]
Sam Altman (OpenAI CEO) stated in March 2025 that AI already writes past 50% of code "in many companies."
— Entrepreneur / Window Central
URL: https://www.entrepreneur.com/business-news/sam-altman-mastering-ai-tools-is-the-new-learn-to-code/488885
Date: March 2025

[QUOTE]
Sam Altman: "My basic assumption is that each software engineer will just do much, much more for a while. And then at some point, yeah, maybe we do need less software engineers."
— Sam Altman, interview with Stratechery's Ben Thompson
URL: https://developers.slashdot.org/story/25/03/25/1428259/openai-ceo-altman-says-ai-will-lead-to-fewer-software-engineers
Date: March 2025

### Where Researcher Predictions Have Diverged from Enterprise Reality

[FACT]
Amodei's March 2025 prediction — "90% of code written by AI in 3–6 months" — was contested by mid-2025 data. IT Pro reported the prediction was "nowhere nearly to becoming a reality" in external enterprise settings at the 6-month mark.
— IT Pro
URL: https://www.itpro.com/technology/artificial-intelligence/anthropic-ceo-dario-amodei-ai-generated-code
Date: 2025

[FACT]
Karpathy himself acknowledged in October 2025 (Dwarkesh Podcast) that agents are limited to "boilerplate stuff" and tasks common on the internet, and that complex codebases cause systematic misunderstanding — qualifying his own "decade of agents" optimism.
— Simon Willison's notes on Dwarkesh Podcast
URL: https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
Date: October 2025

[FACT]
Sutskever, who was one of OpenAI's most influential researchers and key architect of GPT models, stated in November 2025 that "pretraining results have flattened" and current models "excel on benchmarks yet falter in real-world settings."
— Brief/Bismarck Analysis
URL: https://brief.bismarckanalysis.com/p/ai-2026-ilya-sutskever-and-the-end
Date: 2025

### The Structural Credibility Limitation

[FACT]
Nearly 90% of notable AI models in 2024 came from industry (up from 60% in 2023), while academia remains the top source of highly cited research — creating a gap between those who control frontier capabilities and those who evaluate them rigorously.
— Solutions Review / Stanford HAI AI Index 2025
URL: https://solutionsreview.com/ai-and-enterprise-technology-predictions-from-industry-experts-for-2026/
Date: 2025/2026

[FACT]
Karpathy's self-awareness about prediction quality: in January 2026, on the 1-year anniversary of his "vibe coding" tweet, he noted "I still can't predict my tweet engagement basically at all. This was a shower of thoughts throwaway tweet that I just fired off."
— Andrej Karpathy (@karpathy), X
URL: https://x.com/karpathy/status/2019137879310836075
Date: February 2026

---

## Implications for the SaaS Debate: What Researcher Views Do and Do Not Tell Us

[FACT]
Karpathy's own framing contains an implicit SaaS defense: he emphasizes "partial autonomy" — humans and AI in "fast feedback loops" — rather than full automation. His "autonomy slider" metaphor suggests AI-augmented SaaS (e.g., Cursor) rather than pure AI replacement.
— Latent Space summary of YC Startup School keynote
URL: https://www.latent.space/p/s3
Date: June 2025

[FACT]
Karpathy explicitly named a "new category of consumer/manipulator of digital information": humans (GUIs), computers (APIs), and agents (computers that are human-like). This taxonomy implies SaaS must serve all three, not that it disappears.
— Latent Space summary of YC Startup School keynote
URL: https://www.latent.space/p/s3
Date: June 2025

[STATISTIC]
35% of enterprise respondents said they have replaced functionality of at least one SaaS tool with a custom build; 78% expect to build more of their own tools in 2026. However, only 51% of builders have shipped production tools currently in use by their teams.
— Glean enterprise survey
URL: https://www.glean.com/perspectives/will-ai-agents-replace-saas-tools-as-the-new-operating-layer-of-work
Date: 2025

[FACT]
LeCun's critique directly undercuts the SaaS-replacement thesis for enterprise-grade applications: his argument is that LLMs cannot reliably plan, reason, or maintain persistent memory — precisely the capabilities needed to autonomously build and maintain complex enterprise software equivalents.
— Newsweek / HPCwire / Analytics India Magazine
URL: https://www.newsweek.com/nw-ai/ai-impact-interview-yann-lecun-llm-limitations-analysis-2054255
Date: 2025

See [F03_agentic_coding_current_state.md] for detailed coverage of specific agentic coding tools and their measured capabilities. See [F04_agentic_coding_projections.md] for detailed coverage of coding agent capability trajectories and market projections.

---

## Key Takeaways

- **Karpathy's "Software 3.0" thesis is directionally accepted across the researcher community** — natural language is becoming a valid programming interface — but his own October 2025 interview reveals critical caveats: agents fail on complex, rare, or highly specific codebases, and he places full human-replacement agent capabilities a decade out, not months.

- **The Amodei "90% of code" prediction is internally validated at Anthropic but has not generalized to the broader enterprise.** The METR study (July 2025, n=246 tasks) found a 19% productivity slowdown for experienced developers on large real-world codebases using frontier models — the opposite of Amodei's claim, though on a different population and task type.

- **LeCun's structural critique (LLMs lack planning, reasoning, persistent memory) maps directly onto the capabilities required for reliable enterprise software creation.** If he is correct, the SaaS-replacement thesis via AI coding is severely constrained for at least the next 3–5 years.

- **Researcher predictions are most credible on benchmark trajectories and least credible on enterprise deployment timelines.** The gap between lab performance (SWE-bench: 71.7% success) and real-world complex tasks (METR: 19% slowdown) is the defining credibility boundary of current researcher projections.

- **No prominent AI researcher argues that SaaS becomes strategically irrelevant in the 2–5 year window.** Even Karpathy's most bullish framing ("a huge amount of software will be rewritten") spans a decade, and his own product-reliability analysis ("demo is works.any(), product is works.all()") implicitly defends the continued value of enterprise-grade, proven SaaS for mission-critical functions.

---

## Sources

1. https://www.latent.space/p/s3 — Andrej Karpathy on Software 3.0: Software in the Age of AI (Latent Space, June 2025)
2. https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again — Andrej Karpathy: Software Is Changing (Again) (Y Combinator Library, June 2025)
3. https://x.com/karpathy/status/1617979122625712128 — Karpathy "hottest new programming language is English" tweet (X, January 24, 2023)
4. https://x.com/karpathy/status/1886192184808149383 — Karpathy "vibe coding" tweet (X, February 2, 2025)
5. https://karpathy.bearblog.dev/year-in-review-2025/ — Karpathy 2025 LLM Year in Review (December 2025)
6. https://www.dwarkesh.com/p/andrej-karpathy — Dwarkesh Podcast: "AGI is still a decade away" with Karpathy (October 2025)
7. https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/ — Simon Willison's notes on Karpathy/Dwarkesh interview (October 18, 2025)
8. https://www.techmeme.com/250619/p25 — Techmeme: Karpathy Software 3.0 YC AI Startup School coverage (June 19, 2025)
9. https://en.wikipedia.org/wiki/Vibe_coding — Vibe Coding (Wikipedia, 2025)
10. https://x.com/karpathy/status/2019137879310836075 — Karpathy 1-year anniversary reflection on "vibe coding" tweet (X, February 2026)
11. https://www.startuphub.ai/ai-news/artificial-intelligence/2025/software-3-0-the-english-revolution-in-computing — Software 3.0: The English Revolution in Computing (StartupHub.ai, 2025)
12. https://www.superagent.sh/blog/the-march-of-nines — The March of Nines (Superagent blog, 2025)
13. https://orcus4ai.com/Andrej-Karpathy's-Vision-of-Software-3.0-at-YC-AI-Startup-School_ar=023 — Karpathy's Vision of Software 3.0 (Orcus4AI, June 2025)
14. https://finance.yahoo.com/news/anthropic-ceo-says-ai-could-193020957.html — Anthropic CEO Says AI Could Write 90% of Code in 3–6 Months (Yahoo Finance, March 2025)
15. https://felloai.com/anthropic-ceo-dario-amodei-ai-will-replace-90-of-developers-in-6-months/ — Dario Amodei: AI Will Replace 90% of Developers in 6 Months (FelloAI, March 2025)
16. https://officechai.com/ai/dario-amodei-had-predicted-90-of-code-would-be-written-by-ai-but-now-at-anthropic-its-effectively-100-anthropic-cpo/ — Anthropic CPO: AI writing effectively 100% of code internally (OfficeChai, September 2025)
17. https://www.itpro.com/technology/artificial-intelligence/anthropic-ceo-dario-amodei-ai-generated-code — Amodei prediction "nowhere nearly to becoming a reality" in enterprise (IT Pro, 2025)
18. https://darioamodei.com/essay/machines-of-loving-grace — Dario Amodei, Machines of Loving Grace (October 2024)
19. https://fortune.com/2025/12/28/geoffrey-hinton-godfather-of-ai-2026-prediction-human-worker-replacement/ — Geoffrey Hinton 2026 prediction (Fortune, December 28, 2025)
20. https://ts2.tech/en/godfather-of-ai-geoffrey-hinton-why-computer-science-degrees-still-matter-in-the-age-of-ai-and-vibe-coding/ — Hinton on CS degrees and vibe coding (ts2.tech, 2025)
21. https://dev.to/aniruddhaadak/the-future-according-to-demis-hassabis-key-predictions-on-agi-agents-and-the-ferocious-race-4313 — Demis Hassabis predictions on AGI and agents (DEV Community, December 7, 2025)
22. https://www.cnbc.com/2025/03/17/human-level-ai-will-be-here-in-5-to-10-years-deepmind-ceo-says.html — Hassabis: Human-level AI in 5–10 years (CNBC, March 17, 2025)
23. https://fortune.com/article/fortune-500-titans-and-disruptors-google-deepmind-demis-hassabis-isomorphic-artificial-intelligence/ — Hassabis on delegating tasks to agents (Fortune, 2026)
24. https://www.newsweek.com/nw-ai/ai-impact-interview-yann-lecun-llm-limitations-analysis-2054255 — Yann LeCun: LLMs on their way out (Newsweek, 2025)
25. https://x.com/ylecun/status/1796982509567180927 — LeCun "LLMs are useful but an off ramp" tweet (X)
26. https://x.com/ylecun/status/1911604721267114206 — LeCun "not interested in LLMs anymore" tweet (X, April 2025)
27. https://techcrunch.com/2025/01/23/metas-yann-lecun-predicts-a-new-ai-architectures-paradigm-within-5-years-and-decade-of-robotics/ — LeCun: new AI architectures paradigm within 5 years (TechCrunch, January 23, 2025)
28. https://fortune.com/2025/12/19/yann-lecun-ami-labs-ai-startup-valuation-meta-departure/ — LeCun leaves Meta, founds AMI Labs (Fortune, December 2025)
29. https://www.dwarkesh.com/p/ilya-sutskever-2 — Dwarkesh Podcast with Ilya Sutskever (November 2025)
30. https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc. — Safe Superintelligence Inc. Wikipedia article
31. https://brief.bismarckanalysis.com/p/ai-2026-ilya-sutskever-and-the-end — AI 2026: Ilya Sutskever and the End of the Age of Scaling (Bismarck Analysis, 2025)
32. https://hai.stanford.edu/ai-index/2025-ai-index-report — Stanford HAI AI Index Report 2025
33. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ — METR: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity (July 10, 2025)
34. https://www.glean.com/perspectives/will-ai-agents-replace-saas-tools-as-the-new-operating-layer-of-work — Glean: Will AI Agents Replace SaaS? (2025)
35. https://garymarcus.substack.com/p/ai-agents-have-so-far-mostly-been — Gary Marcus: AI Agents have mostly been a dud (Substack, 2025)
36. https://www.project-syndicate.org/magazine/generative-ai-fundamentally-unreliable-and-with-no-apparent-solution-by-gary-marcus-2025-06 — Gary Marcus: AI's Reliability Crisis (Project Syndicate, June 2025)
37. https://garymarcus.substack.com/p/25-ai-predictions-for-2025-from-marcus — Gary Marcus: 25 AI Predictions for 2025 (Substack, January 2025)
38. https://www.entrepreneur.com/business-news/sam-altman-mastering-ai-tools-is-the-new-learn-to-code/488885 — Sam Altman on software engineers and AI (Entrepreneur, 2025)
39. https://developers.slashdot.org/story/25/03/25/1428259/openai-ceo-altman-says-ai-will-lead-to-fewer-software-engineers — Altman: AI will lead to fewer software engineers (Slashdot, March 2025)
40. https://solutionsreview.com/ai-and-enterprise-technology-predictions-from-industry-experts-for-2026/ — AI and Enterprise Technology Predictions for 2026 (Solutions Review, 2025/2026)
41. https://techreviewer.co/blog/ai-in-software-development-2025-from-exploration-to-accountability-a-global-survey-analysis — AI in Software Development 2025 survey (Techreviewer, 2025)
42. https://www.webpronews.com/gary-marcus-calls-the-ai-boom-a-scam-and-the-numbers-are-starting-to-back-him-up/ — Gary Marcus: AI Boom a Scam (WebProNews, 2025)
