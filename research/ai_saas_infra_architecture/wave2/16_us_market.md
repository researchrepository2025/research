# Wave 2 Analysis: US-Specific Infrastructure Patterns for AI SaaS Companies

**Analysis Focus:** US cloud vendor market share, regulatory impact, geographic concentration, spending patterns, K8s vs serverless adoption differences, and hyperscaler role in managed K8s adoption

**Date Compiled:** 2026-02-12
**Analyst:** Wave 2 Analysis Agent
**Wave 1 Sources Used:** 01_cncf_survey.md, 02_analyst_reports.md, 03_job_postings.md, 04_tech_blogs.md, 05_cloud_vendor_cases.md, 06_stackshare_github.md, 07_sec_earnings.md, 08_vc_startup_db.md

---

## Executive Summary

The US market dominates global AI SaaS infrastructure adoption, with the Americas accounting for 70% of cloud-native development activity and US-headquartered hyperscalers (AWS, Azure, GCP) controlling over 70% of global IaaS spend. AWS leads US cloud market share at ~38% of global IaaS, followed by Azure at 24% and GCP at 9%. US regulatory requirements (FedRAMP, SOC2, HIPAA) reinforce managed Kubernetes adoption because hyperscaler managed services carry pre-built compliance certifications. Geographic concentration in the SF Bay Area, Seattle, and NYC correlates with cloud provider proximity and GPU availability, though direct causal data linking geography to architecture choice is absent. US infrastructure spending patterns show AI SaaS companies spending 40-50% of revenue on COGS (vs 15-30% for traditional SaaS), with enterprises spending $37B on generative AI in 2025. The US shows higher serverless adoption (~70% of North American enterprises running production serverless loads) compared to the 11% global CNCF figure, suggesting US companies are more aggressive adopters of both managed K8s and cloud-native non-K8s services. US hyperscalers are the primary drivers of managed K8s adoption, collectively hosting 61% of all production Kubernetes clusters and investing hundreds of billions in AI-optimized infrastructure.

---

## Analysis Section 1: US Cloud Vendor Market Share and Architecture Influence

### Finding 1.1: AWS Dominates US Cloud IaaS, Creating EKS Gravitational Pull

Based on [07_sec_earnings.md, Cloud Infrastructure Market Spend Growth 2024], which shows "AWS owned the largest share of the IaaS pie, with nearly 38% of the global market, while Microsoft Azure and Google Cloud captured 24% and 9%, respectively," AWS's market leadership directly shapes US AI SaaS architecture choices.

**Classification:** Direct

This dominance is reinforced by SEC filing evidence. Based on [07_sec_earnings.md, multiple commitment data points], Snowflake committed $2.5B to a single hyperscaler (2024-2028), Palantir committed $1.95B through 2033, Salesforce expanded AWS use via Hyperforce, and Atlassian signed a multi-year Strategic Collaboration Agreement with AWS. All five named large-cap public AI/SaaS companies with disclosed cloud commitments (Snowflake, Palantir, Salesforce, Atlassian, Zoom) reference AWS as a primary or dominant provider.

**Classification:** Direct (for the specific companies named); Inferred (for the broader pattern)

**Implication for Architecture:** AWS's market position means EKS is the most commonly encountered managed Kubernetes service in US AI SaaS companies. Based on [01_cncf_survey.md, Data Point 18], the 2021 CNCF survey showed "Amazon Elastic Container Service for Kubernetes (39%)" as the most popular managed K8s platform, followed by "Azure Kubernetes Service (23%)." While this data is from 2021, the persistence of AWS's market share leadership (still ~38% in 2024) suggests EKS remains the plurality choice for US AI SaaS.

### Finding 1.2: Azure's Enterprise Position Drives AKS Adoption in Regulated Sectors

Based on [06_stackshare_github.md, Managed Kubernetes Services], "AKS maintains a 28% adoption rate among businesses with 5,000 or more employees." This aligns with Azure's strength in enterprise and regulated verticals (financial services, healthcare, government) that are heavily represented in the US market.

**Classification:** Direct (for the 28% figure among large enterprises)

Azure's US AI SaaS influence is amplified by the Microsoft-OpenAI partnership. Based on [05_cloud_vendor_cases.md, OpenAI Partnership], "OpenAI has contracted to purchase an incremental $250 billion of Azure services." This signals to the US AI ecosystem that Azure is a validated platform for frontier AI workloads, indirectly driving AKS adoption among companies that want to align with OpenAI's infrastructure choices.

Based on [08_vc_startup_db.md, Y Combinator data], "58% of Y Combinator startups accepting Azure credits" and a YC founder noted "Azure was the only place where they could find GPUs, with access available within an hour and a half." This indicates Azure's GPU availability is a decisive factor for early-stage US AI startups, potentially leading to AKS adoption as these companies scale.

**Classification:** Inferred (GPU availability driving long-term architecture lock-in)

### Finding 1.3: GCP Leads in Managed K8s Technical Adoption Despite Third-Place Revenue

Based on [06_stackshare_github.md, Managed Kubernetes Services], "GKE remains dominant in the Kubernetes landscape, with a 32% adoption rate among businesses." This is notable because GCP holds only 9% of overall IaaS market share, suggesting GKE punches significantly above its weight in the Kubernetes-specific segment.

**Classification:** Direct (for the 32% figure, though source methodology is unclear)

Based on [01_cncf_survey.md, Data Point 39], "Google Kubernetes Engine (GKE) operates over 500,000 clusters, AWS Elastic Kubernetes Service (EKS) manages more than 400,000 clusters, and Azure Kubernetes Service (AKS) oversees in excess of 130,000 clusters." GKE leads in absolute cluster count despite GCP's smaller overall market share.

**Classification:** Direct

For AI SaaS specifically, based on [04_tech_blogs.md, Anthropic case study], "Anthropic leverages Google Cloud's GKE to manage mega-scale Kubernetes clusters." And based on [04_tech_blogs.md, Contextual AI and others], multiple AI companies (Picterra, Contextual AI, Midjourney) selected GCP/GKE for AI workloads, attracted by TPU access and AI-optimized infrastructure.

**Classification:** Direct (individual companies); Inferred (broader pattern)

### Summary Table: US Cloud Vendor Influence on Architecture

| Vendor | US IaaS Share | Managed K8s Service | K8s-Specific Signal | Primary US AI SaaS Draw |
|--------|--------------|--------------------|--------------------|------------------------|
| AWS | ~38% | EKS | 39% of managed K8s users (2021 CNCF); 400K+ clusters | Market breadth, EKS maturity, Spot/Graviton cost optimization |
| Azure | ~24% | AKS | 28% among 5K+ employee orgs; 130K+ clusters | OpenAI partnership, enterprise compliance, GPU availability for startups |
| GCP | ~9% | GKE | 32% adoption rate; 500K+ clusters (leads by cluster count) | TPU access, AI-native tooling, Kubernetes origin (Google invented K8s) |

---

## Analysis Section 2: US Regulatory Environment Impact on Architecture

### Finding 2.1: Compliance Requirements Favor Managed Services Over Self-Managed

No Wave 1 file contains direct data on FedRAMP, SOC2, or HIPAA compliance rates segmented by architecture type. However, several data points allow inference.

Based on [01_cncf_survey.md, Data Point 13], "40% cite security as the leading container challenge." Based on [06_stackshare_github.md, Security Signals], "87% of Container Images Have High Risk Vulnerabilities" (Sysdig 2023). These security challenges are amplified in US regulated environments (healthcare under HIPAA, financial services under SOC2, government under FedRAMP), where companies face significant legal liability for infrastructure security failures.

**Classification:** Inferred

Managed Kubernetes services (EKS, AKS, GKE) offer pre-configured compliance controls that reduce the security burden. Based on [05_cloud_vendor_cases.md, Case Study 4 - Sonantic], the company achieved "100% compliance score in AWS Security Hub" on EKS with GPU support. Based on [05_cloud_vendor_cases.md, Case Study 16 - Duck Creek Technologies], an insurance SaaS company (heavily regulated under state insurance laws) chose AKS for modernization. Based on [04_tech_blogs.md, Eli Lilly - Enterprise AI on Amazon EKS], a pharmaceutical company (HIPAA-regulated) built its generative AI platform on EKS.

**Classification:** Inferred (individual cases suggest pattern, but not statistically validated)

**Assumption A1:** US-regulated AI SaaS companies default to managed K8s over self-managed K8s because managed services shift compliance responsibility to the cloud provider (shared responsibility model). This assumption is based on the absence of any Wave 1 case study showing a regulated US AI SaaS company choosing self-managed K8s when a managed alternative was available.

### Finding 2.2: Data Residency Requirements Are a US Differentiator vs Global Markets

Based on [07_sec_earnings.md, ServiceNow], ServiceNow operates a "multi-instance architecture that provides each customer with its own dedicated application logic and databases." Based on [07_sec_earnings.md, Salesforce Hyperforce], "Marketing Cloud Engagement is available on AWS in regions including India, Japan, and Canada (Hyperforce)." These multi-region architectures are partly driven by US customers demanding data residency within US borders and by non-US customers requiring data stay outside the US.

**Classification:** Inferred

The US regulatory environment differs from EU (no federal equivalent to GDPR's strict data localization for general commercial data), meaning US AI SaaS companies face fewer data sovereignty constraints domestically but must architect for them when serving international customers. This favors Kubernetes for its multi-cluster, multi-region portability capabilities. Based on [02_analyst_reports.md, Data Point 30], "65% of organizations run Kubernetes in multiple environments for portability."

**Classification:** Inferred

**Evidence Gap:** No Wave 1 source directly quantifies how FedRAMP, SOC2, or HIPAA adoption rates correlate with managed K8s vs. self-managed K8s vs. serverless choices. This is a significant gap for understanding US-specific architecture drivers.

---

## Analysis Section 3: US AI SaaS Company Geographic Concentration

### Finding 3.1: AI SaaS Is Heavily Concentrated in SF Bay Area, with Secondary Hubs

Based on [08_vc_startup_db.md, Y Combinator data], "the Winter 2024 batch featured approximately 66% of companies integrating AI technologies." Y Combinator is headquartered in San Francisco, and its portfolio is concentrated in the Bay Area. Based on [08_vc_startup_db.md, CB Insights], the top 3 AI funding deals in 2025 went to Anthropic (San Francisco), OpenAI (San Francisco), and Mistral AI (Paris -- the exception).

**Classification:** Direct (for individual company locations); Estimated (for overall concentration)

From the engineering blog evidence in [04_tech_blogs.md], the following US AI SaaS companies with disclosed K8s architectures are geographically distributed:
- **SF Bay Area:** OpenAI (San Francisco), Anthropic (San Francisco), Databricks (San Francisco), Figma (San Francisco), Notion (San Francisco), Jasper AI (San Francisco area)
- **Seattle:** Snowflake (Bozeman MT, but major Seattle presence with AWS alignment)
- **NYC/East Coast:** HubSpot (Cambridge MA), MongoDB (NYC), Elastic (distributed, US HQ in Mountain View)
- **Other:** Grammarly (San Francisco), Salesforce (San Francisco)

**Classification:** Direct (for named companies); Estimated (for the overall geographic distribution)

**Estimated US AI SaaS Geographic Distribution:**
- SF Bay Area: ~50-60% of funded AI SaaS companies (Estimated, based on VC portfolio concentration and named company evidence)
- NYC Metro: ~15-20% (Estimated)
- Seattle: ~10-15% (Estimated)
- Austin, Boston, LA, other: ~15-20% combined (Estimated)

### Finding 3.2: Geography Correlates with Cloud Provider Choice, Not Architecture Category

**Assumption A2:** Geographic location within the US influences which cloud provider a company selects (AWS vs Azure vs GCP) more than whether it uses managed K8s vs serverless vs self-managed K8s.

Evidence for this assumption:
- Seattle-area companies have higher Azure affinity (Microsoft HQ proximity, talent pool)
- SF Bay Area companies show higher GCP/GKE adoption (Google's K8s origins in Mountain View, proximity to GCP engineering)
- Based on [08_vc_startup_db.md], Azure GPU availability was cited by a YC founder (Bay Area) as a driver for Azure adoption, suggesting that even in GCP-friendly SF, GPU scarcity can override geographic loyalty

**Classification:** Estimated (no direct data links US city to cloud provider or architecture choice)

**Evidence Gap:** No Wave 1 source provides data on architecture choices segmented by US metropolitan area. This would require primary research (surveying AI SaaS CTOs by geography).

---

## Analysis Section 4: US-Specific Infrastructure Spending Patterns

### Finding 4.1: US Enterprises Dominate Global AI Infrastructure Spending

Based on [08_vc_startup_db.md, Menlo Ventures 2025 State of Generative AI], "Companies spent $37 billion on generative AI in 2025, a 3.2x year-over-year increase." This survey was conducted among "495 U.S. enterprise AI decision-makers," meaning the $37B figure is US-centric.

**Classification:** Direct

Of that total, "Enterprises spent $18 billion on infrastructure -- foundation models, training, and tooling," representing 49% of total AI spending going to infrastructure.

**Classification:** Direct

Based on [07_sec_earnings.md, AWS Revenue], "AWS reported full-year 2024 revenue of $128.7 billion." Given that AWS holds ~38% of global IaaS and the US is estimated to account for the majority of cloud spending, US enterprises are likely the dominant consumers of cloud infrastructure globally.

### Finding 4.2: AI SaaS Infrastructure Costs 3-5x Higher Than Traditional SaaS in the US

Based on [07_sec_earnings.md, AI SaaS Cost of Revenue], "Instead of 10-20% of revenue going to COGS (as in a typical SaaS), an AI SaaS might see 40-50% (or more) of revenue eaten by COGS."

**Classification:** Direct

Based on [08_vc_startup_db.md, Infrastructure Cost Analysis], "Compute costs for AI companies went from 24% of revenue to 50% of revenue (versus non-AI SaaS where it more or less stayed at about 18% of revenue over the course of a year)."

**Classification:** Direct

Based on [08_vc_startup_db.md, Bessemer analysis], "a cohort of fast-scaling AI SaaS startups had only ~25% gross margin on average in early stages, while even steadier-growth AI companies managed around 60% gross margin."

**Classification:** Direct

These data points are predominantly US-sourced (Bessemer, SaaS Capital, Monetizely are all US firms analyzing US companies). The cost pressure creates strong incentives for US AI SaaS companies to optimize infrastructure, which in turn drives interest in:
1. Managed K8s over self-managed (reducing ops overhead)
2. Spot/preemptible instances (cost optimization)
3. Kubernetes autoscaling (Based on [02_analyst_reports.md, Data Point 41], "64% of Kubernetes organizations use Horizontal Pod Autoscaler")
4. GPU cloud alternatives to hyperscalers (Based on [08_vc_startup_db.md, CoreWeave], "renting an NVIDIA A100 40GB GPU on CoreWeave costs approximately $1.39/hour -- versus $3.67/hour on Azure or Google Cloud -- a 62% cost advantage")

**Classification:** Inferred (cost pressure driving architecture choice)

### Finding 4.3: US Public AI SaaS Companies Commit Billions to Cloud Infrastructure

Based on [07_sec_earnings.md], documented multi-year cloud commitments from US public companies:
- Snowflake: $2.5B over fiscal 2024-2028
- Palantir: $1.95B over 10 years through 2033
- Atlassian: Multi-year SCA with AWS (value not disclosed) for $1B+ Data Center revenue migration

**Classification:** Direct

Based on [07_sec_earnings.md, Hyperscaler Capex], "Amazon projects $100B in capex in 2025, up from $83B in 2024. Microsoft has committed $80B in 2025 to build out AI data centers."

**Classification:** Direct

The vast majority of this capex is invested in US data center regions, reinforcing the US as the center of gravity for AI infrastructure capacity.

---

## Analysis Section 5: US vs Global Differences in K8s vs Serverless Adoption

### Finding 5.1: The US Shows Higher Serverless Adoption Than Global Averages

Based on [06_stackshare_github.md, Serverless Adoption], "Close to 70% of enterprises in North America claimed to operate production loads on serverless systems" from a CNCF 2024 survey. This starkly contrasts with the global figure from the same survey family: based on [01_cncf_survey.md, Data Point 31], "only 11% of respondents are making use of serverless computing frameworks."

**Classification:** Direct (both figures are survey-reported)

The 70% vs 11% discrepancy likely reflects:
1. **Definition differences:** The 70% figure may include serverless containers (Fargate, Cloud Run), while the 11% figure may refer only to FaaS frameworks (Lambda, Cloud Functions)
2. **Sample differences:** North American enterprises vs global CNCF community respondents
3. **US market maturity:** US enterprises have deeper relationships with AWS (where Lambda adoption is highest) and are earlier adopters of managed services generally

Based on [02_analyst_reports.md, Data Point 14], "AWS Lambda: 65% of AWS customers." Based on [02_analyst_reports.md, Data Point 15], "Google Cloud Run: 70% of Google Cloud customers." These Datadog-sourced figures (based on actual telemetry, not surveys) confirm that serverless adoption is extremely high among US-headquartered cloud customers.

**Classification:** Direct

### Finding 5.2: US Companies Use Hybrid Architectures More Than Either/Or

Based on [02_analyst_reports.md, Data Point 17], "66% of organizations using serverless functions also use container orchestration." This indicates that the "K8s vs serverless" framing is misleading -- US companies predominantly use both.

**Classification:** Direct

Based on [03_job_postings.md, Data Point 15], job postings in the US mention "Lambda, ECS, EKS, Fargate, and microservices" together, suggesting hybrid architectures are the norm rather than pure Kubernetes or pure serverless approaches.

**Classification:** Inferred (from job posting co-occurrence)

### Finding 5.3: US Leads Global Cloud-Native Adoption but Europe Leads Cloud-Native Development Intensity

Based on [01_cncf_survey.md, Data Point 15], "Americas: 70% in 'some' or 'much/all' development" compared to "Europe: 82% in 'some' or 'much/all' cloud native development." This is counterintuitive: Europe shows higher cloud-native development intensity despite the US having larger absolute spending.

**Classification:** Direct

**Possible explanations (Estimated):**
- European companies may have smaller infrastructure footprints but more consistently cloud-native architectures
- US companies may have larger legacy estate alongside cloud-native greenfield projects, diluting the percentage
- CNCF survey response bias may differ by region

Based on [01_cncf_survey.md, Data Point 15], "Asia-Pacific: 40% in 'some' or 'much/all' development." The US/Americas sit between Europe and APAC, which aligns with the US having a mix of cloud-native AI startups and large traditional enterprises still modernizing.

**Classification:** Direct

### Summary: US vs Global Architecture Adoption

| Metric | US/Americas | Europe | APAC | Global |
|--------|-------------|--------|------|--------|
| Cloud-native development intensity | 70% | 82% | 40% | ~63% (weighted) |
| Serverless enterprise production | ~70% (N. America) | Not reported | Not reported | 11% (CNCF global) |
| K8s production adoption | Not separately reported | Not separately reported | Not separately reported | 80-82% (global) |
| Multi-cloud usage | Not separately reported | Not separately reported | Not separately reported | 56% (global) |

**Evidence Gap:** No Wave 1 source provides US-specific Kubernetes adoption rates separate from global figures. The CNCF survey does not break down K8s production adoption by region.

---

## Analysis Section 6: Role of US Hyperscalers in Driving Managed K8s Adoption

### Finding 6.1: Hyperscalers Are Investing Massively in AI-Optimized Managed K8s

Based on [04_tech_blogs.md, Google Cloud 130K-Node GKE], Google engineered a "130,000-node GKE cluster" for AI workloads with "API server QPS peaked at 500,000" and "Pod startup latency under 5 seconds cluster-wide."

**Classification:** Direct

Based on [04_tech_blogs.md, Microsoft AKS], Microsoft demonstrated "80 clusters deployed within a single fleet managed by AKS Fleet Manager, with 70,000 nodes distributed across six geographic regions."

**Classification:** Direct

Based on [05_cloud_vendor_cases.md, EKS Ultra-Scale], "Amazon EKS now supports clusters with up to 100,000 nodes, a 10x increase from previous limits" and "EKS can potentially support up to 1.6 million AWS Trainium chips or 800,000 NVIDIA GPUs in a single Kubernetes cluster."

**Classification:** Direct

These investments demonstrate that all three US hyperscalers are building managed K8s services specifically optimized for AI workloads at extreme scale. This drives adoption because:
1. Companies that need GPU scheduling at scale have no viable self-managed alternative at this scale
2. The hyperscalers are making managed K8s the default path for AI workloads
3. CNCF's Kubernetes AI Conformance program (based on [04_tech_blogs.md, CNCF AI Conformance]) formalizes K8s as the standard AI infrastructure layer

### Finding 6.2: Managed K8s Adoption Is 61-73% of All K8s Clusters

Based on [01_cncf_survey.md, Data Point 37], "Managed Kubernetes services (EKS, GKE, AKS) now host 61% of all production clusters."

**Classification:** Direct

Based on [02_analyst_reports.md, Data Point 1], "Most Kubernetes clusters in the cloud (73%) are built on top of managed distributions from the hyperscalers." The 73% figure is cloud-only; the 61% includes on-premises.

**Classification:** Direct

Based on [06_stackshare_github.md], "Two out of every three Kubernetes clusters are now hosted in the cloud, up from just 45% in 2022."

**Classification:** Direct

The trend is clear and directional: managed K8s share is growing. From 45% cloud-hosted in 2022 to 67% in 2025, with the remaining self-managed clusters concentrated in large enterprises with dedicated platform teams (Based on [04_tech_blogs.md], Salesforce runs K8s on bare metal, Databricks runs a hybrid managed/self-managed strategy).

### Finding 6.3: US Hyperscalers Are Crowding Out Self-Managed K8s for AI Workloads

Based on [01_cncf_survey.md, Data Point 25], "30% of AI developers use Machine Learning as a Service (MLaaS) platforms, which abstract away infrastructure management." Combined with the 66% of organizations using K8s for AI inference (Data Point 21) and the growing managed K8s share, the US market is trending toward managed infrastructure for AI workloads.

**Classification:** Inferred

Based on [08_vc_startup_db.md, Infrastructure guide], "Kubernetes should be avoided early unless absolutely necessary due to its high adoption barrier." And at the same time, based on [08_vc_startup_db.md, VC funding], companies like CAST AI ($73M), Spectro Cloud ($143M), and Komodor (200% ARR growth) are building managed K8s optimization layers, suggesting that even self-managed K8s users are layering on managed tooling.

**Classification:** Inferred

The net effect is a US market where:
- **Foundation model companies** (OpenAI, Anthropic) run managed K8s at massive scale (7,500-130,000 nodes)
- **Growth-stage AI SaaS** ($50M+ ARR) use managed K8s (EKS/GKE/AKS) as primary orchestration
- **Early-stage AI SaaS** (seed to Series A) use serverless/PaaS to avoid K8s complexity, migrating to managed K8s as they scale (Figma ECS-to-EKS migration as archetype, per [04_tech_blogs.md])
- **Self-managed K8s** is declining, concentrated in large enterprises with specific requirements (bare metal performance, regulatory control, multi-cloud portability)

**Classification:** Estimated (synthesis across multiple sources)

---

## Assumptions Register

| ID | Assumption | Basis | Impact if Wrong |
|----|-----------|-------|-----------------|
| A1 | US-regulated AI SaaS companies default to managed K8s over self-managed K8s for compliance reasons | No Wave 1 case study shows regulated company choosing self-managed when managed was available | If wrong, self-managed K8s share in regulated sectors would be higher than estimated |
| A2 | Geography within US influences cloud provider choice more than architecture category | Proximity to cloud provider HQs, talent pools, VC network effects | If wrong, architecture choice would vary by city, not just provider choice |
| A3 | The 70% North America serverless figure and the 11% global CNCF figure measure different things | Dramatic discrepancy in same source family suggests definitional differences | If they measure the same thing, one figure is significantly wrong, invalidating either serverless estimate |
| A4 | US AI SaaS infrastructure cost ratios (40-50% of revenue) apply broadly to US AI SaaS companies | Based on US-sourced research (Bessemer, SaaS Capital, Monetizely) analyzing US companies | If wrong, US cost structures differ from reported benchmarks, affecting architecture ROI calculations |
| A5 | AWS EKS remains the plurality managed K8s choice in US AI SaaS | 2021 CNCF data (39% EKS) plus persistent AWS IaaS market share leadership | If GKE or AKS have overtaken EKS since 2021, the provider-architecture linkage shifts |
| A6 | Migration patterns flow from simpler (PaaS/serverless/ECS) toward K8s as companies scale | Figma (ECS to EKS), Grammarly (EC2 to EKS), Salesforce (EC2 to K8s) all moved toward K8s; no reverse cases documented | If companies are migrating away from K8s (undocumented), the managed K8s growth trajectory is overstated |

---

## Evidence Gaps

### Critical Gaps (Would Change Conclusions)

1. **US-specific K8s vs serverless adoption rates:** No Wave 1 source provides K8s or serverless adoption rates broken out for US-only respondents (except the 70% North America serverless figure). The CNCF survey reports regional cloud-native development intensity but NOT regional K8s production adoption.

2. **Architecture choice by US regulatory framework:** No data links FedRAMP/SOC2/HIPAA certification status to managed K8s vs self-managed K8s vs serverless adoption.

3. **US AI SaaS architecture by company stage:** No source provides "what percentage of US Series A AI companies use Kubernetes." Startup infrastructure guidance is prescriptive (recommendations), not descriptive (what companies actually do).

4. **US metro area architecture patterns:** No data on whether SF Bay Area AI SaaS companies differ architecturally from NYC or Austin AI SaaS companies.

### Important Gaps (Would Refine Conclusions)

5. **EKS vs GKE vs AKS share in US AI SaaS specifically:** The 2021 CNCF data (EKS 39%, AKS 23%) has not been updated. Market share data from [01_cncf_survey.md, Data Point 38] (EKS 22%, GKE 18%, AKS 19%) measures cluster counts globally, not US AI SaaS specifically.

6. **Cloud-native non-K8s managed services in the US:** No source quantifies US adoption of ECS/Fargate, Cloud Run, or Azure Container Apps as primary architecture (vs complementary to K8s). The CNCF surveys do not measure these non-K8s container platforms.

7. **US AI SaaS multi-cloud rates:** Based on [01_cncf_survey.md, Data Point 9], 56% of organizations globally use multi-cloud. No US-specific figure exists, though US companies may be more likely to multi-cloud given vendor competition and GPU availability constraints.

8. **GPU infrastructure provider choice in US:** Based on [08_vc_startup_db.md], CoreWeave offers 62% cost advantage over hyperscalers. No data shows what percentage of US AI SaaS companies use specialized GPU clouds (CoreWeave, Lambda Labs) vs hyperscaler GPU instances.

---

## Synthesis: US Market Architecture Distribution Estimate

Based on triangulation across all 8 Wave 1 files, the following estimates represent the US AI SaaS market:

### US AI SaaS Companies Using Managed Kubernetes (EKS/AKS/GKE)

**Estimate: 55-65% of US AI SaaS companies with $10M+ ARR use managed K8s as their primary orchestration layer**

**Classification:** Estimated

**Supporting Evidence:**
- Based on [01_cncf_survey.md, Data Point 1], 80% K8s production adoption globally among CNCF respondents
- Based on [02_analyst_reports.md, Data Point 1], 73% of cloud K8s clusters are managed
- Based on [04_tech_blogs.md], 12+ named US AI/SaaS companies use managed K8s
- Based on [07_sec_earnings.md, CNCF Voice of K8s Experts], "54% of organizations build AI/ML workloads on Kubernetes"
- Discounted by Gartner's lower figure (54% full/partial K8s implementation) and CNCF survey selection bias
- Further narrowed because some AI SaaS companies at $10M+ ARR have not yet migrated to K8s

### US AI SaaS Companies Using Cloud-Native Non-K8s Managed Services

**Estimate: 45-55% of US AI SaaS companies use serverless/PaaS/managed containers (Lambda, Fargate, Cloud Run, App Service) for some production workloads**

**Classification:** Estimated

**Supporting Evidence:**
- Based on [06_stackshare_github.md], "Close to 70% of enterprises in North America claimed to operate production loads on serverless systems"
- Based on [02_analyst_reports.md, Data Point 14], "AWS Lambda: 65% of AWS customers"
- Based on [02_analyst_reports.md, Data Point 17], "66% of organizations using serverless functions also use container orchestration" (hybrid pattern)
- These percentages are non-exclusive with K8s (most companies use both)

### US AI SaaS Companies Using Self-Managed/Open Kubernetes

**Estimate: 10-18% of US AI SaaS companies use self-managed K8s as a significant part of their infrastructure**

**Classification:** Estimated

**Supporting Evidence:**
- Based on [02_analyst_reports.md, Data Point 1], 27% of cloud K8s is self-managed; this is lower in the US where managed adoption runs higher
- Based on [04_tech_blogs.md], only Salesforce (bare metal), Databricks (hybrid), and OpenAI (Azure-based custom) show significant self-managed patterns among US companies
- Based on [01_cncf_survey.md, Data Point 27], smaller companies (which make up most AI SaaS) are less likely to self-manage
- Self-managed K8s requires dedicated platform teams, which most AI SaaS companies under $100M ARR cannot afford

### Important Caveat

These categories are non-exclusive. A company can simultaneously use managed K8s for core services, Lambda for event-driven workloads, and Fargate for batch jobs. Based on [02_analyst_reports.md, Data Point 17], 66% of serverless users also use container orchestration. The percentages above intentionally sum to >100% to reflect this hybrid reality.

---

## Data Quality Assessment

### Completeness: 5/10

**Available:**
- Global K8s adoption rates with limited regional breakout
- US hyperscaler market share (AWS 38%, Azure 24%, GCP 9%)
- US AI SaaS infrastructure cost benchmarks (40-50% of revenue)
- Named US AI SaaS company architectures (15+ companies)
- US enterprise AI spending ($37B in 2025)
- Serverless adoption by cloud provider (Lambda 65%, Cloud Run 70%)

**Missing:**
- US-specific K8s production adoption (only global or Americas figures)
- Architecture choice by US regulatory framework
- Architecture choice by US metro area
- EKS vs AKS vs GKE share among US AI SaaS companies (only 2021 CNCF data)
- Non-K8s cloud-native adoption for AI workloads specifically
- Startup (<500 employee) architecture choices

### Recency: 8/10

Most data points from 2024-2025. The Menlo Ventures US enterprise survey (November 2025) is very recent. Main weakness is the 2021 CNCF managed K8s provider breakdown, which has not been updated.

### Known Biases

1. **US-centric source bias:** Most Wave 1 sources (VC reports, SEC filings, engineering blogs) are US-originated, giving good US coverage but making it difficult to distinguish US-specific patterns from patterns that seem US-specific only because sources are US-based
2. **Large company bias:** SEC filings and engineering blogs over-represent large-cap companies; US early-stage AI SaaS architecture is inferred rather than measured
3. **CNCF survey selection bias:** Over-represents cloud-native adopters, likely inflating K8s adoption figures by 15-25 percentage points vs general enterprise population (based on Gartner's 54% vs CNCF's 80-82%)
4. **Serverless measurement inconsistency:** The 70% North America vs 11% global discrepancy suggests different definitions of "serverless" across sources, making US vs global comparison unreliable

---

## Confidence Score: 5/10

### Justification

**High Confidence (8-9/10):**
- US hyperscaler market share figures (AWS 38%, Azure 24%, GCP 9%) -- from Gartner/Canalys
- US AI SaaS infrastructure costs are 3-5x higher than traditional SaaS -- multiple consistent sources
- All three hyperscalers are investing massively in AI-optimized managed K8s -- direct evidence of 100K+ node clusters
- Named US AI SaaS companies predominantly use managed K8s -- 15+ case studies

**Medium Confidence (5-7/10):**
- Managed K8s at 61-73% of K8s clusters -- two independent sources but global not US-specific
- US serverless adoption higher than global average -- directional signal but measurement inconsistency
- Migration direction is toward K8s -- based on 4 documented cases, zero documented reverse cases
- GKE leads in cluster count despite smaller GCP market share -- single source for cluster counts

**Low Confidence (3-4/10):**
- US-specific architecture distribution estimates (55-65% managed K8s, etc.) -- synthesis of global data with US adjustments, not directly measured
- Regulatory compliance driving managed K8s adoption -- logical inference without direct data
- Geographic concentration affecting architecture choice -- no direct data
- Self-managed K8s at 10-18% in US AI SaaS -- inference from global data

### Why Not Higher

The core challenge is that no Wave 1 source provides US-specific architecture adoption rates for AI SaaS companies. All estimates in this analysis derive from:
1. Global data with US weighting assumptions
2. US-specific data that does not segment by architecture choice
3. Case studies that are not statistically representative

To achieve higher confidence, primary research would be required: a survey of 200+ US AI SaaS CTOs/infrastructure leads, segmented by ARR, geography, and regulatory environment.

---

## Sources (Wave 1 Files Referenced)

All citations reference specific data points within:
- [01_cncf_survey.md] - CNCF Annual Surveys 2021-2024
- [02_analyst_reports.md] - Analyst Reports (Datadog, Gartner, Flexera, CNCF, Red Hat)
- [03_job_postings.md] - Job Posting Analysis (kube.careers, devopscube.com, Stack Overflow)
- [04_tech_blogs.md] - Engineering Blogs & Conference Presentations (OpenAI, Databricks, Figma, Anthropic, etc.)
- [05_cloud_vendor_cases.md] - Cloud Vendor Case Studies (AWS, Azure, GCP)
- [06_stackshare_github.md] - StackShare, GitHub, Technology Profiling Platforms
- [07_sec_earnings.md] - SEC Filings & Earnings Data
- [08_vc_startup_db.md] - VC and Startup Database Research
