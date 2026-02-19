# Validation Interview Methodology Framework

**Purpose:** Primary research methodology for 60-minute structured interviews to validate findings from the ISV AI SaaS Infrastructure Deployment Model study (S1 Comparison Matrix).

**Date:** 2026-02-19

---

## 1. Interview Objectives

### 1.1 What We Are Validating

This interview program tests specific empirical claims from a secondary research synthesis comparing three deployment models for AI-driven SaaS applications built by ISVs: cloud-native (fully managed AWS/Azure/GCP services), managed Kubernetes (EKS/AKS/GKE with portable workloads), and 100% on-premises (customer-hosted, self-managed infrastructure). The claims are organized into three tiers by importance.

**Tier 1 -- Central Claims (must validate or invalidate):**

- C1: The operational staffing multiplier across deployment models is approximately 1x : 2x : 10x (cloud-native : managed K8s : on-premises) for a mid-size ISV serving ~50 enterprise customers.
- C2: Cloud-native operations require 4-9 FTE; managed K8s requires 7.5-13.5 FTE; on-premises requires 38-58 FTE across eight capability domains.
- C3: On-premises operations scale linearly with customer count, while cloud-native operations scale sub-linearly.
- C4: Gross margin compression follows deployment model choice: 70-82% (cloud-native) vs. 60-72% (managed K8s, estimated) vs. 50-65% (on-premises).

**Tier 2 -- Domain-Specific Claims (validate via practitioner experience):**

- C5: Data services represent the highest FTE-density domain for on-premises (8-16 FTE), with self-hosted PostgreSQL HA (Patroni), Kafka, and vector databases (Milvus) as the primary cost drivers.
- C6: AI/ML operations on-premises carry a 6-12 FTE burden, with RAG pipelines and agent orchestration each rated 5/5 difficulty.
- C7: Security and observability together account for 3.25-6.0 FTE on managed K8s, which alone exceeds total cloud-native operational burden.
- C8: The managed K8s data services FTE gap (1.5-3.0 FTE vs. cloud-native) routinely erases compute cost savings.

**Tier 3 -- Business Impact Claims (validate directionally):**

- C9: Time-to-market for new LLM model integration diverges at 1-7 days (cloud-native) vs. 6-16 weeks (on-premises).
- C10: Deployment frequency diverges from daily-to-weekly (cloud-native) to quarterly-to-annual via air-gap bundles (on-premises).
- C11: On-premises ISVs face six simultaneous mandatory technology migrations before end of 2026 (Kafka KRaft, FIPS 140-3, Jaeger v2, Ingress-NGINX EOL, Milvus Woodpecker, Jenkins security).
- C12: GPU infrastructure engineer shortage (~85,000 globally) and SOC analyst attrition (70% within three years) make on-premises hiring at scale a binding constraint.

### 1.2 Signal Definitions

**Confirming signal:** The interviewee independently volunteers information directionally consistent with a claim WITHOUT having been told the claim or its magnitude. For example, if asked "How would you staff an on-premises deployment?" and the answer falls within the 38-58 FTE range without prompting, that is a strong confirming signal. Weaker but still valid: the interviewee describes the same rank ordering (cloud-native < K8s < on-premises) even if specific numbers differ.

**Contradicting signal:** The interviewee provides evidence that inverts the rank ordering, that places values outside the claimed range by more than 50% in either direction, or that identifies a structural mechanism the research did not account for (e.g., "we automated X entirely, so it requires zero FTE"). A single contradiction from a credible practitioner warrants investigation; three or more independent contradictions on the same claim require revision of the finding.

**Ambiguous signal:** The interviewee's experience is directionally consistent but at a different scale (e.g., 5 customers instead of 50), making extrapolation uncertain. Ambiguous signals are coded separately and not counted toward either confirmation or contradiction.

### 1.3 Critical Unknowns Only Primary Research Can Resolve

The following questions cannot be answered by secondary research and represent the highest-priority unknowns:

1. **Actual staffing at the boundaries:** Do ISVs operating at exactly the 50-customer scale described in the research actually maintain staffing levels within the claimed ranges, or does the secondary literature systematically over- or underestimate?
2. **Hidden automation:** Are there operational automation patterns (platform engineering teams, internal developer platforms, AI-assisted ops) that materially reduce FTE requirements below the published figures?
3. **Hybrid model viability:** Do ISVs actually operate "pure" tier models, or do most operate hybrids (e.g., cloud-native control plane with on-prem data plane)? If hybrid, does the FTE burden interpolate linearly between tiers or exhibit non-linear behavior?
4. **Migration friction:** For ISVs that have switched between deployment models, what was the actual transition cost (time, money, organizational disruption) relative to steady-state savings?
5. **Managed K8s economic reality:** The managed K8s tier has the weakest source coverage in the secondary research (some figures are UNVERIFIED interpolations). Do practitioners report costs and staffing consistent with the 2x multiplier, or does the tier cluster closer to 1x or to 10x in practice?
6. **Customer-driven model selection:** How much control does the ISV actually have over deployment model choice, versus having it dictated by customer procurement requirements?

---

## 2. Interviewee Selection Criteria

### 2.1 Target Profiles

| Priority | Role Title(s) | Experience Level | Company Characteristics |
|----------|--------------|------------------|------------------------|
| **Primary** | VP/Director of Engineering, VP/Director of Platform Engineering, CTO (at ISVs < 200 eng) | 8+ years infrastructure experience, 3+ years in current or recent ISV role | ISV building AI-driven multi-tenant SaaS, 20-500 engineering headcount, serving enterprise customers |
| **Primary** | Head of SRE / Head of Infrastructure, Principal Platform Engineer | 6+ years infrastructure experience, direct team management responsibility | Same as above; must own operational staffing decisions |
| **Secondary** | VP of Product (technical), Chief Architect | 8+ years, with direct involvement in deployment model decisions | ISV with active multi-model deployment (cloud + on-prem) |
| **Secondary** | Director of Cloud Architecture, Lead DevOps Engineer | 5+ years, with hands-on experience across deployment models | Platform engineering consultancy or ISV with large-customer deployments |

### 2.2 Mandatory Qualification Criterion

Every interviewee MUST have direct, hands-on professional experience with **at least two** of the three deployment models (cloud-native, managed Kubernetes, on-premises). "Direct experience" means the individual was responsible for or materially involved in staffing, architecture, or operations decisions -- not merely aware of or adjacent to the deployment.

This criterion is non-negotiable because the research's central contribution is the comparative analysis. Interviewees with single-model experience can describe absolute effort but cannot validate relative multipliers.

### 2.3 Stratification Matrix

Target **16-20 interviews** distributed as follows:

| Segment | Target Count | Rationale |
|---------|-------------|-----------|
| **Cloud-native ISV** (primary model is fully managed cloud, may have experimented with or abandoned on-prem) | 4-5 | Validates cloud-native FTE ranges and margin claims; tests whether sub-linear scaling holds |
| **On-premises ISV** (primary model is customer-hosted, may also offer cloud version) | 4-5 | Validates on-prem FTE ranges, linear scaling claim, and mandatory migration burden |
| **Hybrid ISV** (actively operates two or more models simultaneously in production) | 5-6 | Highest priority segment: can directly compare models from within the same organization; validates relative multipliers |
| **Platform engineering leadership** (builds internal developer platforms or consults on deployment model selection across ISVs) | 3-4 | Provides cross-organizational pattern recognition; validates or challenges systemic claims (hiring constraints, migration friction) |

### 2.4 Sample Size Rationale

**Statistical note:** Qualitative research does not achieve statistical validity in the quantitative sense. Instead, we target **theoretical saturation** -- the point at which additional interviews yield no new themes or contradictions. Meta-analyses of qualitative research (Guest, Bunce, and Johnson, 2006) find that saturation typically occurs between 12 and 16 interviews in a reasonably homogeneous population. With four distinct segments, 16-20 interviews provides 4-5 per segment, which is sufficient for within-segment saturation on primary themes while maintaining practical feasibility (each interview requiring approximately 3 hours of total effort: scheduling, conducting, transcribing, and coding).

If resources permit, up to 24 interviews (6 per segment) would strengthen the analysis, but diminishing returns are expected beyond 20.

### 2.5 Screening Questions

Administer the following screening questions via a brief (5-minute) intake form or recruiter call before scheduling. Candidates who fail Q1 or Q2 are disqualified.

**Q1 (Mandatory pass):** "In your professional career, which of the following infrastructure deployment models have you been directly responsible for or materially involved in operating? Select all that apply: (a) Fully managed cloud services (e.g., AWS Lambda/Fargate, Azure Functions/Container Apps, GCP Cloud Run/Autopilot), (b) Managed Kubernetes on a cloud provider (e.g., EKS, AKS, GKE) with significant self-managed infrastructure on top, (c) On-premises or customer-hosted infrastructure (bare metal, private data center, air-gapped environments)." **Must select at least two.**

**Q2 (Mandatory pass):** "In the deployment model(s) selected above, were you personally involved in decisions about team sizing, hiring, or operational staffing? (Yes/No)" **Must answer Yes for at least one model.**

**Q3 (Stratification):** "Which best describes your current or most recent employer? (a) ISV whose primary product is delivered via cloud SaaS, (b) ISV that delivers primarily to on-premises/customer-hosted environments, (c) ISV that actively operates both cloud and on-premises delivery, (d) Platform engineering consultancy or infrastructure vendor, (e) Other."

**Q4 (Scale calibration):** "Approximately how many enterprise customers does (or did) your organization serve with the AI/ML-enabled product in question? (a) Fewer than 10, (b) 10-50, (c) 50-200, (d) More than 200."

---

## 3. Anti-Bias Protocols

### 3.1 Framing the Interview Purpose

The interviewer must frame the study in a way that is honest but does not telegraph expected findings. The approved framing is:

> "We are conducting research to understand how infrastructure deployment model choices affect engineering organizations building AI-driven SaaS products. We are interviewing experienced practitioners to learn about their real-world experiences across different deployment approaches. There are no right or wrong answers -- we are trying to build an accurate picture of the operational landscape from people who live it."

**Do not say:** "We have found that on-premises is 10x harder," "our research shows cloud-native requires fewer people," or any formulation that implies a directional hypothesis. If the interviewee asks what the research has found so far, respond: "We are still in the data-collection phase and want to hear your experience before sharing any preliminary patterns."

### 3.2 Non-Leading Question Design Techniques

**Funnel technique:** Begin each topic with the broadest possible question and progressively narrow. The first question on any topic must be open-ended and non-directional. Example progression: "Tell me about your infrastructure team" (broad) then "How is the team structured across different functions?" (narrower) then "What does the data services sub-team look like?" (specific). Never begin with the specific question.

**Grand tour questions:** Ask the interviewee to narrate a process from their experience rather than evaluate a claim. "Walk me through what happens when a new enterprise customer needs to be onboarded" produces richer and less biased data than "How long does customer onboarding take?"

**Contrast questions:** When the interviewee has experience with multiple models, ask them to compare in their own terms before introducing any research constructs. "You mentioned working with both EKS and fully managed Azure services -- what stands out to you as the biggest operational difference?" lets the interviewee define the axis of comparison.

**Estimation questions with no anchor:** When seeking quantitative data, always ask for the interviewee's estimate before providing any reference numbers. "If you were staffing an on-premises deployment from scratch for a product like yours, how many people would you need?" -- not "Our research suggests 38-58 people; does that seem right?"

### 3.3 Real-Time Confirmation Bias Mitigation

**Devil's advocate probes:** After the interviewee makes a strong claim, probe the opposite direction regardless of whether you agree. "You said cloud-native requires very little operational work -- can you think of a time when that was NOT your experience?" This surfaces nuance and prevents the interviewee from oversimplifying to please the interviewer.

**"What would change your mind" questions:** When an interviewee expresses a strong opinion, ask: "What evidence or experience would make you reconsider that view?" This tests the strength of conviction and surfaces assumptions.

**Disconfirmation probing:** Actively probe for evidence that contradicts the research findings. If an interviewee's experience aligns with the research, push back: "Some practitioners we have spoken with have reported very different numbers -- what do you think could explain that?" (This is legitimate even if no contradicting data exists yet, because it forces the interviewee to consider alternatives.)

**Silence as a tool:** After a response, wait 3-5 seconds before the next question. Interviewees often add qualifications, caveats, or contradictory details during pauses that they would not volunteer if immediately moved to the next question.

### 3.4 Order Effects Mitigation

Question ordering creates two bias risks: primacy effects (early topics receive more elaboration and anchor later responses) and fatigue effects (later topics receive less thoughtful responses). Mitigations:

1. **Rotate domain order across interviews.** The eight capability domains (compute, data, AI/ML, security, observability, networking, CI/CD, messaging) should be probed in a different sequence for each interview. Use a Latin square rotation so each domain appears in each ordinal position approximately equally across the interview set.
2. **Place quantitative estimation exercises in the middle of the interview** (minutes 30-45), when rapport is established but fatigue has not set in.
3. **Never ask about the most critical claims (C1, C2) first.** The staffing multiplier and total FTE estimates should emerge naturally from domain-level discussion, not be asked directly until the interviewee has already provided domain-level estimates that can be summed.
4. **Randomize which deployment model is discussed first** when asking contrast questions. If the interviewee has experience with cloud-native and on-premises, half of interviews should begin with "Tell me about your cloud-native experience" and half with "Tell me about your on-premises experience."

### 3.5 Interviewer Calibration

Before conducting any validation interviews, interviewers must complete the following preparation:

1. **Study the anti-bias protocols** in this document. Understand the difference between a funnel question and a leading question.
2. **Conduct two practice interviews** with colleagues who are not study participants, with a second researcher observing for inadvertent leading.
3. **Review common interviewer pitfalls:**
   - Nodding or expressing approval when answers align with research (maintain neutral acknowledgment: "Thank you, that is helpful" regardless of content).
   - Rephrasing the interviewee's answer using research terminology they did not use ("So you are saying the FTE multiplier is about 10x?" -- never do this).
   - Skipping follow-up probes when an answer confirms the research (confirming answers need the SAME amount of probing as contradicting answers).
   - Showing surprise or hesitation when answers contradict the research.
4. **Use a standardized note-taking template** (Section 6.4) to reduce the temptation to interpret during the interview rather than afterward.

---

## 4. Interview Structure (60 Minutes Total)

### Block 1: Introduction and Rapport Building (5 minutes)

**Purpose:** Establish trust, set expectations, obtain verbal consent, and put the interviewee at ease. No data collection occurs in this block.

**Content:**
- Thank the interviewee for their time.
- Restate the approved framing (Section 3.1).
- Confirm recording consent (if applicable) and confidentiality terms.
- Explain the structure: "We will spend about an hour together. I will start by learning about your background, then we will dive into your infrastructure experiences, and I will ask you to do a couple of short estimation exercises. There are no trick questions."

**Time allocation rationale:** Five minutes is sufficient for framing and consent. Extending rapport-building beyond this risks consuming time needed for substantive probing.

**Transition to Block 2:** "Let me start by understanding your professional background."

---

### Block 2: Background and Experience Mapping (8 minutes)

**Purpose:** Map the interviewee's relevant experience to calibrate which claims can be tested with this individual. Validates screening responses and establishes the interviewee's credibility and scope of knowledge.

**What it validates:** Confirms qualification criteria from screening. Identifies which deployment models the interviewee can speak to with authority, and at what organizational scale. Establishes whether the interviewee's experience maps to the 50-customer mid-size ISV assumption or a different scale.

**Content areas:**
- Career trajectory and current role.
- Which deployment models they have operated, for how long, and at what scale.
- Size of the engineering organization and infrastructure/platform team.
- Whether they have been through a deployment model migration.

**Time allocation rationale:** Eight minutes allows thorough experience mapping without consuming time needed for substantive probing. This block also builds rapport through the interviewee narrating their own story.

**Transition to Block 3:** "That is very helpful context. Now I would like to hear about your day-to-day operational experience. Let us start with [deployment model the interviewee has most experience with]."

---

### Block 3: Open Exploration of Deployment Model Experiences (15 minutes)

**Purpose:** Elicit the interviewee's unprompted, self-organized narrative about operational experience. This is the most important block for detecting confirming or contradicting signals because the interviewee structures their own response without researcher-imposed categories.

**What it validates:** C1 (staffing multiplier, indirectly), C3 (scaling behavior), C9 (time-to-market), C10 (deployment frequency), and any domain-level claims the interviewee spontaneously raises. Also surfaces unknowns: hybrid models, hidden automation, and customer-driven model selection.

**Content areas:**
- Grand tour question(s) about operational responsibilities and challenges.
- Contrast questions if the interviewee has multi-model experience.
- Follow-up probes on any domain the interviewee raises unprompted.
- "Tell me about a time when..." questions to elicit specific incidents rather than generalizations.

**Interviewer discipline:** Do NOT introduce any of the eight capability domain names. Let the interviewee describe their world in their own categories. If they say "the hardest part is keeping the databases running," that is a spontaneous signal about data services difficulty. If they do not mention networking at all, that is also a signal (low perceived difficulty relative to other domains).

**Time allocation rationale:** Fifteen minutes is the longest single block because unstructured narrative is the richest data source and the most resistant to interviewer bias. Cutting this block short to "get to the important questions" would be the single largest methodological error.

**Transition to Block 4:** "You have covered a lot of ground. I want to drill into a few specific areas. Let me ask about [domain NOT yet discussed or discussed only briefly]."

---

### Block 4: Targeted Probing on Specific Domains (15 minutes)

**Purpose:** Systematically probe capability domains that the interviewee did NOT raise in Block 3, and deepen discussion of domains they did raise. This block tests domain-specific claims (C5-C8, C11) by asking about each domain without revealing the research's difficulty ratings or FTE estimates.

**What it validates:** C5 (data services FTE), C6 (AI/ML FTE and difficulty), C7 (security + observability K8s burden), C8 (K8s data services FTE gap), C11 (mandatory migrations), C12 (hiring constraints).

**Content areas (rotate order per Section 3.4):**
- For each probed domain: "Tell me about how your team handles [domain area]." Follow with "What makes that hard?" and "How many people does it take?"
- For multi-model interviewees: "How does that compare to how you handled it in [other model]?"
- For on-premises interviewees: probe for awareness of specific mandatory migrations without naming them. "Are there any technology transitions you are being forced to undertake on a specific timeline?"

**Time allocation rationale:** Fifteen minutes at 2-3 minutes per domain allows probing 5-7 domains. Not all eight domains need to be covered with every interviewee; prioritize domains where the interviewee's experience is deepest and where research claims are highest-stakes or weakest-sourced.

**Transition to Block 5:** "I have a couple of thought exercises I would like to walk through. These are not tests -- I am interested in how you think about the numbers."

---

### Block 5: Quantitative Estimation Exercises (12 minutes)

**Purpose:** Collect independent quantitative estimates from the interviewee for direct comparison against research claims. This block provides the most directly testable data but is placed late in the interview so that the interviewee's qualitative narrative (Blocks 3-4) is not anchored by the act of producing numbers.

**What it validates:** C1, C2, C4, C9 directly. Provides the primary data for the confidence scoring analysis (Section 6.2).

**Content areas:**
- **Staffing estimation exercise:** "If you were building a new team from scratch to operate [deployment model the interviewee knows best] for an AI-driven SaaS product serving 50 enterprise customers, how would you structure the team? Walk me through the roles and headcount." Repeat for a second deployment model if the interviewee has dual experience. The interviewer records the total independently; do not ask the interviewee to sum.
- **Comparative estimation exercise (for multi-model interviewees only):** "You have described staffing for [Model A]. In your experience, roughly how does the staffing for [Model B] compare? More people, fewer people, similar -- and by roughly how much?"
- **Time-to-market estimation:** "If a new foundational model -- say a new version of a major LLM -- were released tomorrow and you needed to integrate it into your product, how long would that take from decision to production, given your current infrastructure?"
- **Optional margin probe (if appropriate):** "In rough terms, how does your infrastructure cost structure affect product margins? Do you think about that, and how?" This question is only appropriate for VP/Director-level interviewees who have P&L visibility.

**Critical anti-bias rule:** The interviewer must NOT share any research numbers during or before this block. If the interviewee asks "What are other people saying?" respond: "I would love to share that with you after we finish -- I want your independent estimate first."

**Time allocation rationale:** Twelve minutes allows two staffing exercises (4-5 minutes each) plus one or two shorter estimation questions. The exercises require the interviewee to think concretely, which takes time; rushing produces low-quality guesses.

**Transition to Block 6:** "Thank you -- those estimates are very useful. We are almost done. Before we wrap up, I want to make sure I have not missed anything."

---

### Block 6: Wrap-Up and Open Floor (5 minutes)

**Purpose:** Capture anything the interviewee considers important that the interview structure did not elicit. Interviewees often share their most candid observations when they feel the "formal" part is over.

**What it validates:** All claims, potentially. The open floor surfaces topics the interview structure may have missed entirely, including unknown unknowns.

**Content areas:**
- "Is there anything about deploying and operating AI SaaS infrastructure that we have not discussed but you think is important?"
- "If you could give one piece of advice to an ISV choosing a deployment model today, what would it be?"
- "Is there anyone else you think we should talk to?"
- Thank the interviewee. Confirm whether they would like to receive a summary of findings when the research is complete.

**Time allocation rationale:** Five minutes is sufficient for an open-ended close. If the interviewee is particularly engaged and the conversation runs long, this block can absorb up to 3 minutes of overflow from earlier blocks.

---

### Time Budget Summary

| Block | Duration | % of Total |
|-------|----------|-----------|
| 1. Introduction and rapport | 5 min | 8% |
| 2. Background mapping | 8 min | 13% |
| 3. Open exploration | 15 min | 25% |
| 4. Targeted domain probing | 15 min | 25% |
| 5. Quantitative estimation | 12 min | 20% |
| 6. Wrap-up and open floor | 5 min | 8% |
| **Total** | **60 min** | **100%** |

---

## 5. Question Design Principles

### 5.1 The Funnel: Broad to Narrow to Specific

Every topic area must follow the funnel progression:

1. **Broad/open:** "Tell me about your infrastructure operations." -- No presuppositions about what is important.
2. **Narrow/directed:** "You mentioned security is a challenge. What specifically about security is hardest?" -- Follows the interviewee's lead.
3. **Specific/probing:** "When you say you need dedicated people for compliance evidence, how many people are doing that full-time?" -- Extracts testable data.

The funnel MUST proceed top-down. Starting at the specific level (e.g., "How many people do you have on compliance?") anchors the interviewee and may produce a number that does not reflect how they actually think about the problem.

### 5.2 Grand Tour Questions

Grand tour questions ask the interviewee to narrate a process or experience as if giving a guided tour to someone unfamiliar with their environment. They are the single most effective technique for eliciting rich, unbiased data.

**Structure:** "Walk me through [a process/period/event]."

**Examples of effective grand tour questions:**
- "Walk me through what a typical week looks like for your platform engineering team."
- "Walk me through the last time you onboarded a new enterprise customer end to end."
- "Walk me through what happened the last time a critical security vulnerability was disclosed that affected your infrastructure."
- "Walk me through the process of deploying a new version of your product to production."

**Why they work:** Grand tour questions force the interviewee to retrieve actual memories rather than construct post-hoc rationalizations. The sequence of events they describe reveals operational complexity that they may not explicitly recognize as "hard."

### 5.3 Contrast Questions

Contrast questions are the primary tool for testing relative claims (the 1x:2x:10x multiplier) without stating the multiplier.

**Structure:** "How does X compare to Y in your experience?"

**Rules for contrast questions:**
- Let the interviewee define the dimensions of comparison. Do not ask "Is X harder than Y?" (suggests difficulty is the relevant axis). Instead: "How does X compare to Y?" and let them choose what is different.
- If the interviewee says "It is harder," follow up with "In what way?" before asking about magnitude.
- Never supply a ratio or multiplier before the interviewee provides their own.

### 5.4 Estimation Techniques

When the interview requires quantitative estimates (Block 5), use the following techniques:

**Decomposition prompting:** Instead of asking "How many people do you need?" ask the interviewee to decompose: "Walk me through the roles and responsibilities, and for each one, tell me roughly how many people handle it." The sum of decomposed estimates is more accurate and more testable than a single top-level number.

**Relative estimation:** For interviewees with multi-model experience, ask for ratios after absolute estimates: "You said Model A takes about 8 people. How does Model B compare?" This produces independent data points: the absolute estimate for A and the relative estimate for B, which can be cross-checked.

**Confidence self-assessment:** After any estimate, ask: "How confident are you in that number -- is it something you know precisely, or is it a rough guess?" This lets the analyst weight estimates appropriately during coding.

### 5.5 Anchoring Avoidance

Anchoring bias occurs when a number mentioned early in a conversation influences subsequent numerical estimates. This is the most dangerous bias for this study because the research is rich in specific numbers.

**Rules:**
1. The interviewer must NEVER state a number from the research before the interviewee has provided their own estimate.
2. The interviewer must not use qualifying language that implies scale: "a large team," "a small number of people," "significant cost." Use neutral language: "your team," "the cost," "the staffing."
3. If the interviewee asks "Is that a lot?" or "How does that compare to what others said?" defer: "I want to hear your assessment first."
4. Numbers from one interview must not be shared with subsequent interviewees. Each interview is independent.

### 5.6 Memory Retrieval Cues

People recall specific incidents much more accurately than general impressions. General questions ("How is security?") produce satisficing answers. Specific questions ("Tell me about the last security incident your team dealt with") produce detailed, verifiable narratives.

**Effective memory cues:**
- "Tell me about the last time [event occurred]."
- "Think about a specific sprint/week/month when [domain] was the top priority. What was happening?"
- "Can you remember a moment when you realized [deployment model] was either much harder or much easier than you expected?"

**Avoid:**
- "Generally speaking, how does [domain] work?" (produces rehearsed answers)
- "Do you find [domain] challenging?" (yes/no question; produces thin data)

---

## 6. Analysis Framework

### 6.1 Response Coding Schema

Each interview response is coded against the research claims using a structured schema:

**Per-claim coding:**

| Code | Label | Definition |
|------|-------|------------|
| **SC** | Strong Confirm | Interviewee independently provides data within the claimed range or describes the claimed mechanism without prompting. |
| **WC** | Weak Confirm | Interviewee's data is directionally consistent but outside the range by up to 50%, or confirms the rank ordering without providing specific numbers. |
| **N** | Neutral / No Data | Interviewee did not address the claim, or their experience is at a different scale/context making comparison uncertain. |
| **WD** | Weak Disconfirm | Interviewee's data is directionally inconsistent -- inverts a rank ordering but with low confidence, or provides a number outside the range by more than 50% but acknowledges unusual circumstances. |
| **SD** | Strong Disconfirm | Interviewee provides concrete evidence that directly contradicts the claim, describes a structural mechanism the research did not account for, or provides numbers outside the range by more than 100% with high confidence. |

**Per-response metadata:**

- **Spontaneous vs. prompted:** Did the interviewee raise this topic unprompted (in Blocks 3 or 6) or in response to a targeted probe (Blocks 4 or 5)? Spontaneous data is weighted higher because it reflects the interviewee's own salience hierarchy.
- **Confidence level:** Self-reported by the interviewee (precise knowledge, educated guess, rough estimate).
- **Scale context:** How many customers, how large the engineering org, which deployment models -- for assessing whether the interviewee's context maps to the research's assumptions.

### 6.2 Confidence Scoring: What Constitutes Validation

Use the following thresholds, recognizing that these are heuristics for qualitative research, not statistical tests:

**Validated (high confidence):** A claim is considered validated when it receives SC or WC codes from at least **10 of 16-20 interviewees** (50%+) who have relevant experience for that claim, AND receives no more than 2 SD codes. This is a high bar intentionally: the research claims are specific and quantitative, so the validation standard should be correspondingly rigorous.

**Provisionally validated (moderate confidence):** SC or WC from 6-9 interviewees with relevant experience, with no more than 3 SD codes. The claim stands but with a noted confidence caveat.

**Unvalidated (insufficient data):** Fewer than 6 SC/WC codes, or more than 3 SD codes. The claim requires either additional interviews or revision.

**Invalidated:** More than 5 SD codes, or SD codes from more than 30% of interviewees with relevant experience. The research claim must be revised or retracted.

**Important:** Validation thresholds apply per-claim, not per-interview. A single interviewee may validate some claims and contradict others.

### 6.3 Handling Contradictory Evidence

**Single outlier:** One interviewee contradicts a claim that 10+ others confirm. Record the outlier's reasoning and context in full. Investigate whether their situation is structurally different (different scale, different industry, exceptional automation). If the outlier can be explained by context, note the boundary condition. If it cannot, flag the claim for further investigation.

**Systematic disagreement (3+ contradictions):** Three or more independent contradictions require substantive response. Options:

1. **Revise the range:** If contradictions cluster on magnitude (e.g., everyone says "yes it is harder, but more like 5x, not 10x"), adjust the claimed range and note the source of the revision.
2. **Add a boundary condition:** If contradictions come from a specific context (e.g., ISVs smaller than 20 customers), add an explicit qualifier to the claim.
3. **Retract the claim:** If contradictions are structural (the mechanism is wrong, not just the magnitude), retract the claim and document why.

**Contradictions are more valuable than confirmations.** A contradiction with a clear explanation improves the research more than a confirmation without context. Interviewers should probe contradictions deeply: "That is different from what some others have described. Help me understand what is different about your situation."

### 6.4 Post-Interview Scoring Template

Complete the following for each interview within 24 hours of conducting it:

```
Interview ID: [INT-###]
Date: [YYYY-MM-DD]
Interviewee Segment: [Cloud-native ISV / On-prem ISV / Hybrid ISV / Platform engineering]
Deployment Model Experience: [Models A, B]
Organization Scale: [# customers, # engineering headcount]
Interview Duration: [actual minutes]

CLAIM SCORING:
| Claim ID | Code (SC/WC/N/WD/SD) | Spontaneous? | Interviewee Confidence | Key Evidence (direct quote or paraphrase) | Context Notes |
|----------|----------------------|--------------|----------------------|------------------------------------------|---------------|
| C1       |                      |              |                      |                                          |               |
| C2       |                      |              |                      |                                          |               |
| ...      |                      |              |                      |                                          |               |
| C12      |                      |              |                      |                                          |               |

EMERGENT THEMES (topics not in claim list):
1. [Theme]: [Brief description and evidence]
2. [Theme]: [Brief description and evidence]

CRITICAL UNKNOWNS ADDRESSED:
[Which of the six critical unknowns from Section 1.3 did this interview shed light on, and what did we learn?]

INTERVIEWER SELF-ASSESSMENT:
- Did I inadvertently lead on any question? [Y/N, details]
- Did I provide anchoring numbers at any point? [Y/N, details]
- Which blocks ran over/under allocated time?
- Quality of data: [High / Medium / Low] with rationale
```

### 6.5 Cross-Interview Analysis

After all interviews are completed, produce a claim-by-claim summary matrix:

| Claim | SC Count | WC Count | N Count | WD Count | SD Count | Validation Status | Confidence Notes |
|-------|----------|----------|---------|----------|----------|-------------------|------------------|

And a domain-level summary comparing average interviewee-estimated FTE against research-claimed FTE ranges, disaggregated by interviewee segment.

---

## 7. Ethical Considerations

### 7.1 Informed Consent

Before each interview begins, the interviewee must be informed of and consent to:

1. **Purpose of the study:** Research into infrastructure deployment models for AI-driven SaaS products.
2. **Use of data:** Their responses will contribute to a comparative analysis. Individual responses will not be attributed by name or organization.
3. **Recording:** If the interview will be recorded (audio or video), explicit consent must be obtained. The interviewee may decline recording and still participate; the interviewer will take written notes instead.
4. **Voluntary participation:** Participation is voluntary, and the interviewee may decline to answer any question or terminate the interview at any time without consequence.
5. **Data retention:** How long interview recordings and transcripts will be retained, and who will have access.

Consent should be documented either via a signed consent form (for formal research contexts) or via recorded verbal consent at the start of the interview (for less formal contexts).

### 7.2 Confidentiality and Anonymization

- **Individual anonymization:** No interviewee will be identified by name, job title, or organization in any output document. Interviewees are referenced by anonymous identifiers (e.g., INT-001 through INT-020).
- **Organization anonymization:** Company names will not appear in analysis outputs. Where organizational context is relevant (e.g., "a cloud-native ISV with 200 engineers"), descriptions will be sufficiently generalized that the organization cannot be identified.
- **Segment-level reporting only:** Quantitative results (FTE estimates, margin figures) will be reported at the segment level (e.g., "hybrid ISV interviewees estimated an average of X FTE") rather than as individual data points.
- **Quote clearance:** If a direct quote is particularly illuminating and the researcher wishes to include it in a report, the interviewee will be contacted for approval before publication. Quotes will be attributed to "[Segment] practitioner" rather than by name.

### 7.3 Handling Proprietary Information

Interviewees may inadvertently or intentionally share proprietary information about their organization's infrastructure, staffing, or finances. Protocols:

1. **No solicitation of trade secrets.** The interview questions ask for professional judgment and general experience, not proprietary architecture diagrams or exact financial figures.
2. **Redaction upon request.** If the interviewee realizes they have shared something proprietary, they may request that specific information be struck from the record at any point during or after the interview.
3. **Aggregation as protection.** All proprietary details are aggregated with other responses before analysis. No individual organization's data will be presented in isolation.
4. **Secure storage.** Interview recordings and transcripts will be stored in an encrypted location accessible only to the research team. They will not be shared with third parties.

### 7.4 Right to Withdraw

- The interviewee may withdraw from the study at any time, including after the interview has been conducted.
- Upon withdrawal, all of that interviewee's data (recordings, transcripts, coded responses) will be deleted within 7 business days. If the withdrawal occurs after analysis has begun, the interviewee's data will be removed and the analysis re-run without it.
- Withdrawal will not affect any professional or business relationship between the interviewee and the research organization.

### 7.5 Reciprocity

Interviewees are contributing their time and expertise. In return:

- Offer to share a summary of aggregate findings upon study completion (not individual responses from other participants).
- Where appropriate, offer a copy of the final published research.
- Respect the interviewee's time: start on time, end on time, do not follow up with excessive additional questions unless the interviewee has explicitly offered.

---

## Appendix A: Methodological References

- Guest, G., Bunce, A., & Johnson, L. (2006). How many interviews are enough? An experiment with data saturation and variability. *Field Methods, 18*(1), 59-82.
- Spradley, J. P. (1979). *The Ethnographic Interview.* Harcourt Brace Jovanovich. (Source of grand tour and contrast question techniques.)
- Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124-1131. (Source of anchoring bias framework.)
- Kvale, S., & Brinkmann, S. (2009). *InterViews: Learning the Craft of Qualitative Research Interviewing.* Sage. (Source of funnel technique and interviewer calibration guidance.)
- Corbin, J., & Strauss, A. (2015). *Basics of Qualitative Research.* Sage. (Source of theoretical saturation concept and coding methodology.)
