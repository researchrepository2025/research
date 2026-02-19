# ISV Deployment Model Validation Interview Guide

**Version:** 1.0
**Date:** 2026-02-19
**Study:** ISV AI SaaS Infrastructure Deployment Model Comparison

**Purpose:** This guide structures a 60-minute practitioner interview to understand how infrastructure deployment model choices affect engineering organizations building AI-driven SaaS products. It captures real-world operational experience across cloud-native, managed Kubernetes, and on-premises deployment models.

**How to use this guide:**
1. Read the Anti-Bias Reminders (p. 2) before every interview.
2. Complete Blocks 1-6 in order. Timing notes are provided; adapt as needed but never skip Block 3 or Block 5.
3. After the interview, complete the Post-Interview Scoring Sheet (p. 12) within 24 hours using the Claims Reference appendix.
4. The Claims Reference appendix contains research values -- consult it ONLY after the interview, never during.

---

## Interviewee Selection and Screening

### Target Profiles

| Priority | Roles | Experience | Organization |
|----------|-------|------------|--------------|
| Primary | VP/Director of Engineering, VP/Director of Platform Engineering, CTO (ISVs < 200 eng), Head of SRE/Infrastructure | 6+ years infrastructure; 3+ years in ISV role; owns staffing decisions | ISV building AI-driven multi-tenant SaaS; 20-500 engineering headcount; serving enterprise customers |
| Secondary | VP of Product (technical), Chief Architect, Director of Cloud Architecture | 5+ years; direct involvement in deployment model decisions | ISV with active multi-model deployment or platform engineering consultancy |

### Mandatory Qualification

Every interviewee must have direct, hands-on professional experience with **at least two** of the three deployment models (cloud-native, managed K8s, on-premises). "Direct experience" means responsibility for or material involvement in staffing, architecture, or operations decisions.

### Screening Questions (5-minute intake form or call)

**Q1 (Must pass):** "Which infrastructure deployment models have you been directly responsible for operating? Select all that apply: (a) Fully managed cloud services, (b) Managed Kubernetes on a cloud provider with significant self-managed infrastructure, (c) On-premises or customer-hosted infrastructure." *Must select at least two.*

**Q2 (Must pass):** "Were you personally involved in decisions about team sizing, hiring, or operational staffing for at least one of those models?" *Must answer Yes.*

**Q3 (Stratification):** "Which best describes your current or most recent employer? (a) Cloud SaaS ISV, (b) On-premises-first ISV, (c) Hybrid ISV operating both, (d) Platform engineering consultancy, (e) Other."

**Q4 (Scale):** "Approximately how many enterprise customers does your organization serve with the AI/ML-enabled product? (a) <10, (b) 10-50, (c) 50-200, (d) >200."

---

## Anti-Bias Quick-Reference Card

Read this before every interview. Keep it visible during the conversation.

### Five Rules

1. **Never state a research number before the interviewee gives theirs.** No FTE counts, cost ranges, multipliers, percentages, or difficulty ratings. If they ask what others said, respond: "I want your independent view first -- I can share patterns after we finish."

2. **Start every topic at the top of the funnel.** The first question on any topic must be broad and open-ended. Narrow only after the interviewee has set the direction.

3. **Probe confirmations as hard as contradictions.** When an answer aligns with expectations, ask the same number and depth of follow-ups as when it does not. Do not nod, smile, or say "exactly."

4. **Use neutral acknowledgment regardless of content.** "Thank you, that is helpful" or "I appreciate that detail" -- never "That is consistent with what we are seeing" or "Interesting, that is different."

5. **Let silence work.** After each response, wait 3-5 seconds before the next question. Interviewees add qualifications and caveats in pauses.

### Phrases to Avoid

| Do NOT Say | Say Instead |
|------------|-------------|
| "Our research suggests..." | "In your experience..." |
| "Most practitioners report..." | "How has that worked for you?" |
| "That is a large/small team" | "Tell me more about the team" |
| "So the multiplier is about..." | "How would you compare the team sizes?" |
| "Is that because of [mechanism]?" | "What drives that?" |
| "Exactly" / "That matches" | "Thank you, that is helpful" |
| "We found 10x..." | [Never say this] |

---

## Interview Protocol (60 Minutes)

---

### Block 1: Introduction and Rapport (5 min)

**Read aloud or paraphrase:**

> "Thank you for making time for this conversation. We are conducting research to understand how infrastructure deployment model choices affect engineering organizations building AI-driven SaaS products. We are interviewing experienced practitioners to learn about their real-world experiences across different deployment approaches. There are no right or wrong answers -- we are trying to build an accurate picture of the operational landscape from people who live it."

> "This will take about 60 minutes. I will start by learning about your background, then we will explore your operational experiences, and toward the end I will ask you to walk through a couple of short estimation exercises. Nothing is a trick question."

**Consent and recording:**

> "[If recording] With your permission, I would like to record this conversation so I can focus on listening rather than note-taking. The recording will only be used by our research team, and your identity and organization will be anonymized in any output. You can ask me to stop recording or skip any question at any time. Is that okay?"

> "[If not recording] I will be taking notes as we talk. Your identity and organization will be anonymized in any output. You can skip any question at any time."

**Ice-breaker:**

> "Before we dive in -- what has been the most interesting infrastructure challenge you have tackled in the past year?"

*Note: This question warms up the interviewee and may surface a topic worth returning to later. Do not probe deeply here -- just listen and acknowledge.*

**Transition:** "That is great context. Let me start by understanding your professional background a bit more."

---

### Block 2: Background Mapping (8 min)

**Purpose:** Qualify the interviewee and establish which claims they can speak to. Record answers carefully -- they determine which Block 4 questions to ask and which to skip.

**Q2.1** "Walk me through your career trajectory in infrastructure and platform engineering. What are the key roles that brought you to where you are today?"

*Validates: Screening qualification. Begins to address [C-1.1] staffing multiplier, [C-1.73] mid-size ISV scope.*

**Q2.2** "Which deployment models have you operated in production -- fully managed cloud, managed Kubernetes, on-premises, or some combination? For each, roughly how long and at what customer scale?"

*Validates: Confirms multi-model experience. Begins to address [C-1.73] 50-customer scope, [C-5.1] K8s FTE range, [C-1.2] cloud-native FTE range, [C-1.4] on-prem FTE range.*

**Q2.3** "How large is your current engineering organization, and how much of it is dedicated to platform or infrastructure versus product development?"

*Validates: [C-7.46] <50 headcount threshold, [C-7.27] minimum viable team sizes.*

**Q2.4** "Have you ever been through a migration from one deployment model to another -- say from on-prem to cloud, or from cloud-native to K8s? What prompted it?"

*Validates: Critical Unknown #4 (migration friction). Begins to address [C-1.71] deployment model as business decision.*

**Transition:** "That is very helpful context. Now I would like to hear about your day-to-day operational experience. Let us start with [the deployment model they have the most experience with]."

*Branching: Note which models the interviewee has experience with. This determines which Block 4 probes and Block 5 exercises to use.*

---

### Block 3: Open Exploration (15 min)

**Purpose:** Elicit the interviewee's unprompted narrative about operational challenges. This is the richest block for detecting confirming or contradicting signals because the interviewee organizes their own response. Do NOT introduce capability domain names (compute, data, AI/ML, security, etc.). Let the interviewee describe their world in their own categories.

**Q3.1 -- Grand Tour** "Walk me through what a typical week looks like for your platform or infrastructure team. What are the biggest things consuming their time right now?"

*May naturally surface: [C-1.1] staffing multiplier, [C-4.27] stateful platform burden, [C-4.33] compliance difficulty, [C-4.61] structural difference claim, [C-1.72] non-fungibility of specialists.*

**Q3.2 -- Contrast** *(For multi-model interviewees)* "You mentioned experience with [Model A] and [Model B]. What stands out to you as the biggest operational difference between running your product on those two models?"

*May naturally surface: [C-1.1] staffing multiplier, [C-3.18] 75-90% staffing reduction, [C-4.61] structural vs. scaled difference, [C-6.17] linear vs. sub-linear scaling.*

**Q3.3 -- Incident Narrative** "Tell me about the last time something went seriously wrong in your production infrastructure. What happened, how did you respond, and what did it reveal about your operational setup?"

*May naturally surface: [C-4.46] SOC operations challenges, [C-2.14] dependency explosion, [C-6.19] security patching asymmetry.*

**Q3.4 -- Evolution** "How has the operational burden of your product changed as you have grown your customer base? What got harder, what got easier?"

*May naturally surface: [C-6.17] linear vs. sub-linear scaling, [C-1.73] scaling with customer count, [C-5.6] K8s TCO increases.*

**Interviewer notes:**
- Track which domains the interviewee raises unprompted -- these are the highest-salience topics.
- Track which domains they do NOT mention -- these are candidates for Block 4 probing.
- If the interviewee naturally mentions team sizes, cost, margins, or time-to-market, note the values without reacting.
- If running long (>17 min), move to Block 4 after the current response finishes.

**Transition:** "You have covered a lot of ground. I want to drill into a few specific areas. Let me ask about [domain NOT yet discussed]."

---

### Block 4: Targeted Domain Probing (15 min)

**Purpose:** Systematically probe specific capability domains the interviewee did NOT raise in Block 3, and deepen those they did. Cover as many as time allows; prioritize domains where the interviewee has relevant experience and where research claims are highest-risk.

**IMPORTANT: Rotate the order of Q4.1-Q4.7 across interviews using Latin square rotation. Record which order you used. Never start with the same domain two interviews in a row.**

**If running long, skip to Block 5 at the 38-minute mark regardless of how many domain probes you have completed.**

---

**Q4.1 -- Data Services and Stateful Platforms**

"How does your team handle databases, message brokers, and other stateful services? What is the operational reality of keeping those running?"

*Follow-up:* "How does that effort change depending on whether you use managed services versus running them yourselves?"

*Validates: [C-4.27] stateful platforms 8-16 FTE, [C-5.2] CloudNativePG vs Aurora cost, [C-2.9] self-hosted Kafka burden.*

*Branching: If no K8s experience, skip the managed-vs-self-hosted follow-up.*

---

**Q4.2 -- AI/ML Infrastructure**

"What infrastructure do you maintain specifically for AI and ML workloads -- model serving, embedding pipelines, retrieval, agents? Walk me through the components and who owns them."

*Follow-up:* "Which of those components has been the hardest to operate, and what makes it hard?"

*Follow-up (if on-prem experience):* "How does running that AI infrastructure on your own hardware compare to using cloud-managed equivalents?"

*Validates: [C-2.11] RAG pipeline FTE gap, [C-2.12] agent infrastructure FTE gap, [S1-42] AI/ML on-prem 6-12 FTE, [C-6.11] on-prem LLM inference 5/5 difficulty.*

---

**Q4.3 -- Security and Compliance**

"Tell me about your security operations and compliance posture. How is the team structured, and what are the biggest ongoing demands?"

*Follow-up:* "How does the compliance workload differ between your cloud-hosted and self-hosted environments?"

*Follow-up:* "What has been the most time-consuming compliance evidence to produce and maintain?"

*Validates: [C-4.33] compliance 5/5 difficulty, [C-4.46] SOC operations 4-5/5, [S1-43] security on-prem 6.5-12.25 FTE, [C-5.3] K8s security exceeds cloud-native total.*

*Branching: If the interviewee works in defense/government, add: "What compliance certifications have you had to achieve, and what did they cost in time and money?" [Validates: [C-4.41] FedRAMP $400K-$2M]*

---

**Q4.3a -- Security Alternative** *(Use if interviewee has no on-prem experience)*

"Even on fully managed cloud infrastructure, what security and compliance work does your team still own? Where does the cloud provider's responsibility end and yours begin?"

*Validates: [C-3.23] cloud-native residual security FTE 0.75-1.65.*

---

**Q4.4 -- SDLC and Release Process**

"How do you ship updates to your customers across your different deployment models? Walk me through the release process from code merge to production."

*Follow-up:* "How does the release cadence and rollback process differ between your cloud and on-prem customers?"

*Validates: [C-6.15] deploy frequency 182x gap, [S1-47] on-prem deploy/release "Critical," [C-6.14] 3-5 concurrent major versions.*

---

**Q4.5 -- GPU and Compute**

*(Only if interviewee has GPU/on-prem experience; otherwise skip)*

"How do you manage GPU capacity -- procurement, scheduling, utilization? What does the planning process look like?"

*Follow-up:* "When you need more GPU capacity, how far ahead do you have to plan, and what happens when the forecast is wrong?"

*Validates: [C-4.29] GPU procurement 9-12 months, [C-4.30] GPU breakeven 60-70% utilization, [C-4.53] GPU decisions determine capability 12+ months out.*

*Branching: If no GPU experience, skip entirely and move to Q4.6.*

---

**Q4.6 -- Technology Migrations and Vendor Stability**

"Are there any mandatory technology migrations or vendor-driven transitions you are dealing with right now? How do you handle them when they overlap?"

*Follow-up:* "Have any vendor pricing or licensing changes caught you off guard in the past couple of years?"

*Validates: [C-4.35] six simultaneous mandatory migrations, [C-4.36] VMware post-Broadcom 8-15x price increase, [C-5.8] platform ecosystem instability (TKG, Rancher).*

---

**Q4.7 -- Hiring and Talent**

"How has your experience been hiring and retaining the specialists your infrastructure requires? Where is the talent market tightest?"

*Follow-up:* "Are there roles where the difficulty of hiring has affected your product or architecture decisions?"

*Validates: [C-7.28] GPU infrastructure engineer shortage 85,000 gap, [C-4.58] 70% SOC analyst attrition, [C-7.30] 1 in 3 tech professionals changed jobs.*

---

**Transition:** "I have a couple of thought exercises I would like to walk through. These are not tests -- I am interested in how you think about the numbers."

---

### Block 5: Quantitative Estimation (12 min)

**Purpose:** Collect the interviewee's independent numerical estimates for direct comparison against research claims. CRITICAL: Do not share any research numbers during or before this block. Use decomposition prompting -- ask them to walk through roles and responsibilities, not just give a top-level number.

**If running short on time, prioritize Q5.1 and Q5.2. Q5.3 and Q5.4 are optional.**

---

**Q5.1 -- Staffing Estimation (Primary)** *(4-5 min)*

"Imagine you are building a team from scratch to operate an AI-driven SaaS product for about 50 enterprise customers on [the interviewee's primary deployment model]. Walk me through the roles you would need and roughly how many people for each."

*After they finish:* "How confident are you in those numbers -- is that something you know precisely from experience, or is it a rough estimate?"

*Do NOT sum their numbers aloud. Record the breakdown and sum independently.*

*Validates: [C-1.2] cloud-native 4-9 FTE, [C-1.3] managed K8s 7.5-13.5 FTE, [C-1.4] on-prem 38-58 FTE. The primary test of the core staffing claim.*

**Confirming:** Total falls within the claimed range for their deployment model.
**Contradicting:** Total is >50% outside the range, or the interviewee names a structural mechanism the research did not account for (e.g., "We automated all of that with [tool], so it is 2 people").

---

**Q5.2 -- Comparative Estimation** *(3-4 min; multi-model interviewees only)*

"You just described staffing for [Model A]. In your experience, how does [Model B] compare? More people, fewer, similar -- and roughly by how much?"

*After they give a ratio or relative estimate:* "What drives the biggest differences?"

*Validates: [C-1.1] the 1x:2x:10x multiplier, [C-3.18] 75-90% staffing reduction.*

**Confirming:** Relative ratio is directionally consistent with 1:2:10 (even if the specific numbers differ).
**Contradicting:** Interviewee reports an inverted or flat ratio (e.g., "K8s and on-prem take about the same team").

---

**Q5.3 -- Time-to-Market** *(2-3 min)*

"If a major new foundation model -- say the next version of a leading LLM -- were released tomorrow and you wanted to integrate it into your product, how long would that take from decision to production availability? Walk me through the steps."

*If multi-model:* "How does that timeline differ between your cloud and on-prem customers?"

*Validates: [C-7.24] 1-7 days cloud vs 6-16 weeks on-prem, [S1-49] K8s 2-4 weeks (UNVERIFIED).*

**Confirming:** Cloud timeline in days, on-prem in weeks-to-months.
**Contradicting:** Interviewee reports similar timelines across models, or reports on-prem faster than cloud.

---

**Q5.4 -- Margin and Pricing** *(2-3 min; VP/Director-level only)*

"In rough terms, how does infrastructure cost affect your product margins across different deployment models? Do you price on-prem customers differently from cloud-hosted ones?"

*Follow-up:* "If you had to estimate the additional annual cost of supporting your on-premises customers compared to cloud-hosted, what order of magnitude would that be?"

*Validates: [C-7.21] gross margins 70-82% cloud vs 50-65% on-prem, [C-7.35] on-prem incremental cost $900K-$1.8M, [C-7.39] on-prem must be priced as market access.*

**Confirming:** Interviewee reports meaningful margin compression for on-prem and prices it at a premium.
**Contradicting:** Interviewee reports similar margins across models, or reports that on-prem pricing premiums fully offset costs.

---

**Transition:** "Thank you -- those estimates are very useful. We are almost done. Before we wrap up, I want to make sure I have not missed anything."

---

### Block 6: Wrap-Up (5 min)

**Q6.1** "Is there anything about deploying and operating AI SaaS infrastructure that we have not discussed but you think is important?"

**Q6.2** "If you could give one piece of advice to an ISV choosing a deployment model today, what would it be?"

**Q6.3** "What would surprise you most about how other ISVs handle their deployment model decisions?"

**Q6.4** "Is there anyone else you think we should talk to -- someone who has a different perspective on these questions?"

**Close:**

> "Thank you very much for your time and your candor. This is exactly the kind of real-world perspective we need to get this right. When the research is complete, we would be happy to share a summary of aggregate findings with you if you are interested. [Confirm interest.] We will follow up by email. Thank you again."

---

## Post-Interview Scoring Sheet

Complete within 24 hours of the interview. Use the Claims Reference appendix to look up research values AFTER scoring.

**Interview ID:** INT-____
**Date:** ____-____-____
**Interviewee Segment:** [ ] Cloud-native ISV  [ ] On-prem ISV  [ ] Hybrid ISV  [ ] Platform engineering
**Deployment Model Experience:** ____________
**Organization Scale:** ____ customers, ____ engineering headcount
**Interview Duration:** ____ minutes
**Domain Probe Order Used:** ____________

### Scoring Key

| Code | Label | Definition |
|------|-------|------------|
| SC | Strong Confirm | Interviewee independently provides data within the claimed range or describes the claimed mechanism without prompting. |
| WC | Weak Confirm | Data is directionally consistent but outside range by up to 50%, or confirms rank ordering without specific numbers. |
| N | Neutral / No Data | Interviewee did not address the claim, or their context makes comparison uncertain. |
| WD | Weak Disconfirm | Data directionally inconsistent -- inverts rank ordering with low confidence, or number outside range by >50% with acknowledged unusual circumstances. |
| SD | Strong Disconfirm | Concrete evidence directly contradicting the claim, a structural mechanism the research missed, or numbers outside range by >100% with high confidence. |

### Claim Scoring Table

| # | Claim Summary | Block | Score | Spontaneous? | Interviewee Confidence | Key Evidence | Notes |
|---|--------------|-------|-------|-------------|----------------------|--------------|-------|
| 1 | Staffing multiplier ~1x:2x:10x across deployment tiers | B3, B5 | | | | | |
| 2 | Cloud-native operations: 4-9 FTE | B5 | | | | | |
| 3 | Managed K8s operations: 7.5-13.5 FTE | B5 | | | | | |
| 4 | On-premises operations: 38-58 FTE | B5 | | | | | |
| 5 | On-prem annual cost $8.4M-$21.0M | B5 | | | | | |
| 6 | Gross margins: 70-82% cloud vs 50-65% on-prem | B5 | | | | | |
| 7 | K8s gross margin 60-72% [UNVERIFIED] | B5 | | | | | |
| 8 | On-prem operational burden structurally different, not just scaled | B3 | | | | | |
| 9 | Non-fungibility of infrastructure specialists (compounding, not sharing) | B3, B4 | | | | | |
| 10 | Stateful platform operations largest FTE share: 8-16 FTE on-prem | B4.1 | | | | | |
| 11 | RAG pipeline FTE gap: 2.0-4.0 on-prem vs 0.5-1.0 cloud | B4.2 | | | | | |
| 12 | Agent infrastructure FTE gap: 3.5-7.25 on-prem vs 0.2-1.2 cloud | B4.2 | | | | | |
| 13 | AI/ML on-premises total: 6-12 FTE | B4.2 | | | | | |
| 14 | Compliance operations 5/5 difficulty, 2.5-4.0 FTE | B4.3 | | | | | |
| 15 | K8s security + observability exceeds total cloud-native burden (3.25-6.0 FTE) | B4.3 | | | | | |
| 16 | On-prem security total: 6.5-12.25 FTE (deduplicated) | B4.3 | | | | | |
| 17 | De-duplication methodology removes 8.0-15.5 FTE from raw estimates | B4.3 | | | | | |
| 18 | Cloud managed services reduce staffing 75-90% vs on-prem | B3, B5 | | | | | |
| 19 | Deploy frequency: daily-to-weekly cloud vs quarterly-to-annual on-prem | B4.4 | | | | | |
| 20 | On-prem operations scale linearly with customer count | B3, B4.4 | | | | | |
| 21 | LLM integration: 1-7 days cloud vs 6-16 weeks on-prem | B5 | | | | | |
| 22 | K8s LLM integration time: 2-4 weeks [UNVERIFIED] | B5 | | | | | |
| 23 | Portable architecture design adds 20-40% overhead [UNVERIFIED] | B3, B4.4 | | | | | |
| 24 | GPU procurement lead times 9-12 months | B4.5 | | | | | |
| 25 | Six simultaneous mandatory migrations before end of 2026 | B4.6 | | | | | |
| 26 | GPU infrastructure engineer shortage (~85,000 global gap) | B4.7 | | | | | |
| 27 | SOC analyst attrition: 70% leave within 3 years | B4.7 | | | | | |
| 28 | Deployment model is a business model decision, not a technical choice | B3, B6 | | | | | |
| 29 | Sovereign cloud paradox: margin-eroding model needed for highest-ACV segments | B5 | | | | | |
| 30 | On-prem pricing must reflect true delivery cost or margins compress to 50-65% | B5 | | | | | |

### Emergent Themes (topics not in claim list)

1. ____________________________________________________________
2. ____________________________________________________________
3. ____________________________________________________________

### Critical Unknowns Addressed

| Unknown | Evidence from This Interview |
|---------|------------------------------|
| Actual staffing at 50-customer scale | |
| Hidden automation reducing FTE below published figures | |
| Hybrid model viability (does FTE interpolate linearly?) | |
| Migration friction (actual transition cost) | |
| Managed K8s economic reality (closer to 1x or 10x?) | |
| Customer-driven vs ISV-driven model selection | |

### Interviewer Self-Assessment

- Did I inadvertently lead on any question? [ ] No [ ] Yes -- details: ____________
- Did I provide anchoring numbers at any point? [ ] No [ ] Yes -- details: ____________
- Which blocks ran over/under allocated time? ____________
- Data quality: [ ] High [ ] Medium [ ] Low -- rationale: ____________

---

## Appendix: Claims Reference

**CONSULT ONLY AFTER THE INTERVIEW. Never during.**

This appendix contains the 30 selected claims with their research values. These are organized by theme and mapped to the interview blocks where they are tested.

---

### Theme A: Core Staffing and Cost (Central Thesis)

| # | Claim | Research Value | Source Type | Priority | Blocks |
|---|-------|---------------|-------------|----------|--------|
| 1 | Staffing multiplier across tiers | ~1x : 2x : 10x | Synthesis across 78 files | HIGH | B3, B5 |
| 2 | Cloud-native FTE range | 4-9 FTE (50 customers) | Synthesis from X1 | HIGH | B5 |
| 3 | Managed K8s FTE range | 7.5-13.5 FTE (50 customers) | Synthesis from W07S | HIGH | B5 |
| 4 | On-premises FTE range | 38-58 FTE (de-duplicated) | Synthesis from X2 | HIGH | B5 |
| 5 | On-prem annual cost | $8.4M-$21.0M (personnel + CapEx + GPU + SOC) | Synthesis from X2 | HIGH | B5 |
| 18 | Cloud managed services staffing reduction | 75-90% vs on-prem | Synthesis from X1 | HIGH | B3, B5 |

### Theme B: Business and Margin Impact

| # | Claim | Research Value | Source Type | Priority | Blocks |
|---|-------|---------------|-------------|----------|--------|
| 6 | Cloud-native gross margins | 70-82% (median 77%) | Industry benchmarks | HIGH | B5 |
| 7 | Managed K8s gross margins [UNVERIFIED] | 60-72% (estimated) | Synthesis/unverified | HIGH | B5 |
| 28 | Deployment model = business model decision | Determines margin, velocity, org design, addressable market | Synthesis/thesis | HIGH | B3, B6 |
| 29 | Sovereign cloud paradox | Margin-eroding model needed for highest-ACV segments ($111B-$941B market) | Analyst report (SNS Insider) | HIGH | B5 |
| 30 | On-prem pricing must reflect true cost | Margins compress to 50-65% if underpriced | Synthesis | HIGH | B5 |

### Theme C: AI/ML Infrastructure

| # | Claim | Research Value | Source Type | Priority | Blocks |
|---|-------|---------------|-------------|----------|--------|
| 11 | RAG pipeline FTE gap | 2.0-4.0 on-prem vs 0.5-1.0 cloud | Practitioner blog (Introl) | HIGH | B4.2 |
| 12 | Agent infrastructure FTE gap | 3.5-7.25 on-prem vs 0.2-1.2 cloud | Practitioner blog (Maxim AI) | HIGH | B4.2 |
| 13 | AI/ML on-prem total | 6-12 FTE | Practitioner/vendor blogs | HIGH | B4.2 |

### Theme D: Security, Compliance, and Observability

| # | Claim | Research Value | Source Type | Priority | Blocks |
|---|-------|---------------|-------------|----------|--------|
| 14 | Compliance operations difficulty and FTE | 5/5 difficulty; 2.5-4.0 FTE | Qualys blog, SecureFrame | HIGH | B4.3 |
| 15 | K8s security + observability burden | 3.25-6.0 FTE (exceeds total cloud-native) | Practitioner blog (cymulate.com) | HIGH | B4.3 |
| 16 | On-prem security total (deduplicated) | 6.5-12.25 FTE | Multiple vendor/practitioner blogs | HIGH | B4.3 |
| 17 | De-duplication removes 8.0-15.5 FTE from raw estimates | Four overlap zones: security 4.0-7.0, GPU 2.0-4.0, Temporal 1.0-2.0, observability 1.0-2.5 | Synthesis methodology | HIGH | B4.3 |
| 27 | SOC analyst attrition | 70% leave within 3 years (5 yrs experience or less) | SANS/Stamus survey | HIGH | B4.7 |

### Theme E: On-Premises Infrastructure

| # | Claim | Research Value | Source Type | Priority | Blocks |
|---|-------|---------------|-------------|----------|--------|
| 8 | On-prem burden structurally different | Not linear scaling of cloud -- six macro categories, specialized teams | Synthesis/thesis | HIGH | B3 |
| 9 | Non-fungibility of specialists | Kafka operator cannot substitute for Vault operator; burdens compound | Synthesis/thesis | HIGH | B3, B4 |
| 10 | Stateful platform operations FTE | 8-16 FTE (Patroni, Kafka, Milvus, ES, Temporal) | Synthesis from W05S/W06S | HIGH | B4.1 |
| 24 | GPU procurement lead times | 9-12 months | Practitioner blog (Uvation) | HIGH | B4.5 |
| 25 | Six simultaneous mandatory migrations | Kafka KRaft, FIPS 140-3, Jaeger v2, Ingress-NGINX EOL, Milvus Woodpecker, Jenkins | Multiple vendor docs | HIGH | B4.6 |

### Theme F: SDLC and Velocity

| # | Claim | Research Value | Source Type | Priority | Blocks |
|---|-------|---------------|-------------|----------|--------|
| 19 | Deploy frequency gap | Daily-to-weekly (cloud) vs quarterly-to-annual (on-prem); 182x | DORA/Octopus Deploy | HIGH | B4.4 |
| 20 | On-prem operations scale linearly with customer count | Linear (on-prem) vs sub-linear (cloud) | Practitioner blog + synthesis | HIGH | B3, B4.4 |
| 21 | LLM integration time-to-market | 1-7 days (cloud) vs 6-16 weeks (on-prem) | Menlo Ventures | HIGH | B5 |
| 22 | K8s LLM integration time [UNVERIFIED] | 2-4 weeks (interpolated, no direct measurement) | Synthesis/unverified | HIGH | B5 |
| 23 | Portable architecture design overhead [UNVERIFIED] | 20-40% additional effort | Synthesis/unverified (W08S consensus) | HIGH | B3, B4.4 |

### Theme G: Talent Market

| # | Claim | Research Value | Source Type | Priority | Blocks |
|---|-------|---------------|-------------|----------|--------|
| 26 | GPU infrastructure engineer shortage | ~85,000 global gap; $15K-$25K training vs $200-$500 cloud certs | Practitioner blog (Introl) | HIGH | B4.7 |
| 27 | SOC analyst attrition | 70% leave within 3 years | SANS/Stamus survey | HIGH | B4.7 |

---

### Selection Rationale

The 30 claims above were selected from 129 total using the following criteria:

1. **All HIGH-priority synthesis-derived claims included.** Claims 1, 4, 8, 9, 17, and 18 are research-team aggregations carrying the highest risk of systematic bias.
2. **All UNVERIFIED claims included.** Claims 7, 22, and 23 have no direct source and need validation most urgently.
3. **Central thesis claims prioritized.** The staffing multiplier (Claim 1), FTE ranges (Claims 2-4), cost ranges (Claim 5), and margin claims (Claims 6-7) are the backbone of the research.
4. **Weakest-sourced claims included.** Claims sourced from single practitioner blogs (11, 12, 24, 26) require triangulation.
5. **Every major theme represented.** Foundation architecture, cloud convergence, on-prem operational tax, K8s middle tier, SDLC impact, business impact, and talent are all covered.
6. **LOW-priority and easily-verified claims dropped.** Specific vendor pricing (MinIO $96K, DGX $373K-$450K), tool adoption statistics (Argo CD 60%), specific EOL dates (Ingress-NGINX March 2026), and claims verifiable through public documentation were excluded to preserve interview time.

---

### Latin Square Domain Probe Rotation

Use this rotation schedule for Block 4. Assign each interview an order number (1-7) cycling through the schedule. Record which order was used on the scoring sheet.

| Interview Order | Q4.1 | Q4.2 | Q4.3 | Q4.4 | Q4.5 | Q4.6 | Q4.7 |
|----------------|-------|-------|-------|-------|-------|-------|-------|
| 1 | Data | AI/ML | Security | SDLC | GPU | Migrations | Talent |
| 2 | AI/ML | Security | SDLC | GPU | Migrations | Talent | Data |
| 3 | Security | SDLC | GPU | Migrations | Talent | Data | AI/ML |
| 4 | SDLC | GPU | Migrations | Talent | Data | AI/ML | Security |
| 5 | GPU | Migrations | Talent | Data | AI/ML | Security | SDLC |
| 6 | Migrations | Talent | Data | AI/ML | Security | SDLC | GPU |
| 7 | Talent | Data | AI/ML | Security | SDLC | GPU | Migrations |

---

### Claim ID Cross-Reference

The claim numbering in this guide (1-30) maps to the source documents as follows:

| Guide # | Ch 1-4 Source | Ch 5-8 Source | Description |
|---------|--------------|--------------|-------------|
| 1 | C1.1 | C5-8.54 | Staffing multiplier 1x:2x:10x |
| 2 | C1.2 | -- | Cloud-native 4-9 FTE |
| 3 | C1.3 | C5-8.1 | Managed K8s 7.5-13.5 FTE |
| 4 | C1.4 | -- | On-prem 38-58 FTE |
| 5 | C1.6 | C5-8.45 | On-prem annual cost $8.4M-$21.0M |
| 6 | -- | C5-8.21 | Gross margins cloud vs on-prem |
| 7 | -- | C5-8.21 (partial) | K8s gross margin [UNVERIFIED] |
| 8 | C1.61 | -- | Structural difference claim |
| 9 | C1.72 | -- | Non-fungibility of specialists |
| 10 | C4.27 | -- | Stateful platforms 8-16 FTE |
| 11 | C2.11 | -- | RAG pipeline FTE gap |
| 12 | C2.12 | -- | Agent infrastructure FTE gap |
| 13 | -- | C5-8.42 | AI/ML on-prem 6-12 FTE |
| 14 | C4.44 | -- | Compliance 5/5 difficulty |
| 15 | -- | C5-8.3 | K8s security + observability burden |
| 16 | -- | C5-8.43 | On-prem security 6.5-12.25 FTE |
| 17 | C4.42 | -- | De-duplication 8.0-15.5 FTE |
| 18 | C3.18 | -- | 75-90% staffing reduction |
| 19 | -- | C5-8.15 | Deploy frequency 182x gap |
| 20 | -- | C5-8.17 | Linear vs sub-linear scaling |
| 21 | -- | C5-8.24 | LLM integration time-to-market |
| 22 | -- | C5-8.49 | K8s LLM integration [UNVERIFIED] |
| 23 | -- | C5-8.10 | Portable design overhead [UNVERIFIED] |
| 24 | C4.29 | -- | GPU procurement 9-12 months |
| 25 | C4.35 | C5-8.53 | Six mandatory migrations |
| 26 | -- | C5-8.28 | GPU engineer shortage 85,000 |
| 27 | C4.58 | C5-8.29 | SOC analyst attrition 70% |
| 28 | C1.71 | -- | Deployment model = business decision |
| 29 | C1.7 | C5-8.31 | Sovereign cloud paradox |
| 30 | -- | C5-8.39 | On-prem pricing must reflect cost |
