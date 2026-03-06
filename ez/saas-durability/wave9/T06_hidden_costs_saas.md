# T06: The Systematically Underestimated Costs and Risks of SaaS

**Research Wave:** Wave 9 — Economic Analysis for Scenario Building
**Audience:** C-Suite
**Scope:** Hidden SaaS costs that shift the build-vs-buy calculus

---

## Executive Summary

Enterprise SaaS spending has become a structurally underestimated liability, with organizations averaging $49 million annually on software while wasting $21 million of it on unused licenses — a 14% year-over-year deterioration according to Zylo's 2025 SaaS Management Index ([https://zylo.com/news/2025-saas-management-index/](https://zylo.com/news/2025-saas-management-index/)). SaaS inflation now runs at 12.2% annually — 4.5 times the G7 general inflation rate of 2.7% — driven primarily by AI feature bundling that customers cannot opt out of ([https://www.vertice.one/insights/saas-inflation-rate](https://www.vertice.one/insights/saas-inflation-rate)). The true cost of SaaS extends well beyond license fees: switching costs, data extraction friction, customization workarounds, and strategic dependency on vendor roadmaps collectively represent an economic exposure that is rarely captured in TCO analyses. As Forrester declared in early 2026, "SaaS as we know it is dead," with a late-2025 Retool survey finding that 35% of enterprises have already replaced at least one SaaS tool with a custom build and 78% expect to build more in 2026 ([https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483](https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483)). These dynamics make the hidden cost stack of SaaS a strategic, not merely operational, concern.

---

## 1. Vendor Lock-In Costs: Switching Cost Estimates by Category

Vendor lock-in is not a binary state — it accumulates across technical, contractual, organizational, and data dimensions. Each layer adds switching friction that inflates the effective cost of change.

### Switching Cost Taxonomy

| Lock-In Layer | Description | Primary Cost Driver |
|---|---|---|
| Technical | Proprietary APIs, data schemas, integrations | Reengineering and retesting |
| Contractual | Multi-year commitments, termination penalties | Early exit fees, deferred price resets |
| Organizational | Trained workflows, embedded processes | Retraining, productivity loss |
| Data | Proprietary formats, export restrictions | Migration, transformation labor |
| Ecosystem | Certified partner dependencies | Resourcing premium (15–30% rate premium) |

[FACT]
"Retraining costs for switching to a new cloud platform or SaaS provider can sometimes exceed the savings that motivated the initial move to cloud-based services."
— NEdigital, "Assessing Vendor Lock-in and Exit Costs in SaaS-Centric IT Environments"
URL: [https://www.nedigital.com/en/blog/assessing-vendor-lock-in-and-exit-costs-in-saas-centric-it-environments](https://www.nedigital.com/en/blog/assessing-vendor-lock-in-and-exit-costs-in-saas-centric-it-environments)
Date: 2025

[STATISTIC]
"Developers with expertise in specific enterprise platforms like Salesforce, ServiceNow, or Workday typically charge 15-30% more than general developers."
— GetMonetizely, "How Much Should Custom Enterprise SaaS Modifications Really Cost?"
URL: [https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost](https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost)
Date: 2025

[STATISTIC]
ERP implementation costs average $450,000 according to Panorama Consulting's 2025 benchmark study, with large enterprises exceeding $1 million. Budget frameworks suggest allocating approximately 3% of annual revenue for a 5-year ERP investment; for a $50 million company, this implies a $1.5 million commitment.
— DataFlowMapper, "Data Migration Cost Analysis & Calculator (2025 Analysis)"
URL: [https://dataflowmapper.com/blog/data-migration-costs-quantitative-analysis](https://dataflowmapper.com/blog/data-migration-costs-quantitative-analysis)
Date: 2025

[FACT]
"A representative large-scale migration wave often costs around US$1.2 million when tooling, labor, and refactoring are included. A typical enterprise wave takes about ~8 months end-to-end, from assessment to stabilization."
— Binadox, "SaaS Data Portability: Complete Exit Strategy Guide for 2025"
URL: [https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/](https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/)
Date: 2025

### Contractual Lock-In: The Cumulative Price Reset Trap

[FACT]
"SaaS vendors are sliding a nasty detail into SaaS renewal term price protections: taking a '3–5% cap' and multiplying it by the number of years in your next term (e.g., 3% × 3-year = 9%)."
— UpperEdge, "SaaS Vendors' New Trick: Multiplying Pricing Caps by Term Length"
URL: [https://upperedge.com/knowledge-center/documents/podcasts/saas-vendors-new-trick-multiplying-pricing-caps-by-term-length/](https://upperedge.com/knowledge-center/documents/podcasts/saas-vendors-new-trick-multiplying-pricing-caps-by-term-length/)
Date: 2025

[FACT]
"Cumulative price increases mean that although your costs will stay the same per year during the first 5 years of the deal, the vendor is keeping track of how much the cost SHOULD have increased during that time and will charge you after you renew... At 3% annually, you will pay $4.6M in Year 6 for the same products."
— UpperEdge, "IT Services Contracts: Beware of Cumulative Price Increases"
URL: [https://upperedge.com/contract-negotiations/how-it-services-vendors-pocket-aces-with-cumulative-yearly-price-increases/](https://upperedge.com/contract-negotiations/how-it-services-vendors-pocket-aces-with-cumulative-yearly-price-increases/)
Date: 2025

See E03 (Enterprise Lock-In Views) for detailed coverage of how enterprise buyers currently perceive and underweight lock-in risk at the point of purchase.

---

## 2. Data Portability: Extraction, Migration, and Transformation Costs

Data portability is the most underpriced element of SaaS contracts and the most expensive element of SaaS exits. Vendors profit from data gravity — the longer data resides in a proprietary system, the more expensive removal becomes.

[FACT]
"Some SaaS vendors introduce hidden costs that make it financially impractical for businesses to retrieve their own data, with unexpected charges for bulk exports, API access, or migration support that can significantly inflate costs."
— Binadox, "SaaS Data Portability: Complete Exit Strategy Guide for 2025"
URL: [https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/](https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/)
Date: 2025

[FACT]
"Proprietary formats store data in a format that requires conversion or custom scripting to use elsewhere, with consultants charging $2,000–5,000 to transform and migrate it. API access is locked behind enterprise tier at $500+/month."
— CompareTiers, "7 Hidden Costs of SaaS Pricing Nobody Talks About"
URL: [https://comparetiers.com/blog/hidden-costs-saas-pricing](https://comparetiers.com/blog/hidden-costs-saas-pricing)
Date: 2025

[FACT]
"Enterprise data tolls and API economics are going to be a headache, with connection fees going to be the new cloud egress to move data... Toward the end of 2025, The Information reported that Salesforce was raising prices on apps that tap into its data, and CIO.com noted that these connector fees are likely to trickle down to IT budgets."
— Constellation Research, "Enterprise Technology 2026: 15 AI, SaaS, Data, Business Trends to Watch"
URL: [https://www.constellationr.com/blog-news/insights/enterprise-technology-2026-15-ai-saas-data-business-trends-watch](https://www.constellationr.com/blog-news/insights/enterprise-technology-2026-15-ai-saas-data-business-trends-watch)
Date: 2026

### Data Migration Cost by Project Scope

| Migration Scope | Estimated Cost Range |
|---|---|
| Basic migration, 3–7 years of records | $5,000–$30,000 |
| Heavy migration, 8+ years, multiple legacy systems | Up to $75,000 |
| Full enterprise ERP migration (labor + tooling + refactoring) | ~$1.2 million average |
| Downtime cost during migration (large enterprise) | $9,000+ per minute |

Sources: DataFlowMapper ([https://dataflowmapper.com/blog/data-migration-costs-quantitative-analysis](https://dataflowmapper.com/blog/data-migration-costs-quantitative-analysis)); Binadox ([https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/](https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/))

### Regulatory Backstop (EU Data Act, 2025)

[FACT]
"The EU Data Act 2025 bans providers from charging for data transfer or imposing restrictive migration procedures. By removing exit fees and simplifying termination clauses, the Data Act makes it easier for customers to switch providers."
— Clairfield, "How the 2025 EU Data Act Rewrites the Rules for SaaS Providers"
URL: [https://www.clairfield.com/how-the-2025-eu-data-act-rewrites-the-rules-for-saas-providers/](https://www.clairfield.com/how-the-2025-eu-data-act-rewrites-the-rules-for-saas-providers/)
Date: 2025

Note: The EU Data Act applies only to EU-based operations. Non-EU enterprises remain fully exposed to vendor-imposed extraction costs.

---

## 3. Customization Ceiling: The Cost of Working Around SaaS Limitations

SaaS products are built for the median customer. When enterprise workflows diverge from that median — which they inevitably do — costs accumulate in three vectors: licensed customization fees, third-party middleware, and employee time burned on workarounds.

[FACT]
"The average mid-sized enterprise spends approximately $250,000 annually on SaaS customizations across their technology stack. Maintenance costs typically account for 15-25% of the initial development expense annually."
— GetMonetizely, "How Much Should Custom Enterprise SaaS Modifications Really Cost?"
URL: [https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost](https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost)
Date: 2025

[FACT]
"One freight brokerage's 'customized' Salesforce implementation had 127 configured fields, 34 workflow rules, and 12 integrated apps, but also required 14 manual workarounds, with their sales team spending 23% of their time navigating around Salesforce rather than using it."
— GetMonetizely, "How Much Should Custom Enterprise SaaS Modifications Really Cost?"
URL: [https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost](https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost)
Date: 2025

[QUOTE]
"SaaS solutions offer more limited customization options since multiple organizations share the same underlying software."
— HubFi, "Enterprise SaaS Platform: The Ultimate Guide (2025)"
URL: [https://www.hubifi.com/blog/enterprise-software-vs-saas](https://www.hubifi.com/blog/enterprise-software-vs-saas)
Date: 2025

[FACT]
"Integration testing typically adds 15-20% to development costs. Often-overlooked expenses include user training, performance optimization, and security reviews — compounding the customization cost base."
— GetMonetizely, "How Much Should Custom Enterprise SaaS Modifications Really Cost?"
URL: [https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost](https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost)
Date: 2025

### The Shadow IT Overflow Effect

When SaaS cannot be customized to meet workflow needs, employees route around it — creating shadow IT sprawl that compounds cost and governance risk.

[STATISTIC]
"In 2025, over 40% of SaaS spend is outside the purview of IT and finance teams. Enterprises use 270 to 364 SaaS applications on average, with 52% of these applications being unsanctioned."
— Zluri, "Shadow IT Statistics: Key Facts to Learn in 2025"
URL: [https://www.zluri.com/blog/shadow-it-statistics-key-facts-to-learn-in-2024](https://www.zluri.com/blog/shadow-it-statistics-key-facts-to-learn-in-2024)
Date: 2025

[STATISTIC]
"72% of SaaS spend occurs outside IT's visibility, led by lines of business and individual employees."
— Zylo, 2025 SaaS Management Index
URL: [https://zylo.com/news/2025-saas-management-index/](https://zylo.com/news/2025-saas-management-index/)
Date: 2025

---

## 4. The SaaS Tax: Paying for Features You Don't Use

The SaaS tax is the aggregate cost of licensing features that are bundled into subscription tiers but never used by the purchasing organization. It manifests in two forms: unutilized seats within a used product, and entire feature modules within a tier that enterprise buyers cannot avoid.

[STATISTIC]
"Organizations are wasting an average of $21M annually on unused SaaS licenses, a 14.2% increase year-over-year. 52.7% of purchased licenses go unused."
— Zylo, 2025 SaaS Management Index (analyzed data from 40M+ SaaS licenses and $40B in SaaS spend)
URL: [https://zylo.com/news/2025-saas-management-index/](https://zylo.com/news/2025-saas-management-index/)
Date: 2025

[STATISTIC]
"The average organization spends $49M annually and $4,830 per employee on SaaS — a 21.9% increase year-over-year."
— Zylo, 2025 SaaS Management Index
URL: [https://zylo.com/news/2025-saas-management-index/](https://zylo.com/news/2025-saas-management-index/)
Date: 2025

[STATISTIC]
"Large enterprises lost an average of $127 million on unused SaaS licenses."
— Zylo, 2025 SaaS Management Index
URL: [https://zylo.com/news/2025-saas-management-index/](https://zylo.com/news/2025-saas-management-index/)
Date: 2025

[STATISTIC]
"45% of applications are underutilized — with organizations using less than half of the licenses they're paying for. 23% of licenses show zero usage."
— EZO AssetSonar, "SaaS License Waste: The Hidden Cost in Your IT Budget"
URL: [https://ezo.io/assetsonar/blog/saas-license-waste/](https://ezo.io/assetsonar/blog/saas-license-waste/)
Date: 2025

[QUOTE]
"The SaaS Tax — You're Paying for 100%, Using 12%"
— Appunite (headline)
URL: [https://www.appunite.com/blog/business-paying-for-100-saas-using-12](https://www.appunite.com/blog/business-paying-for-100-saas-using-12)
Date: 2025

### The AI Feature Bundle Tax

A specific and growing subset of the SaaS tax is the forced bundling of AI capabilities — AI features added to standard tiers that customers pay for regardless of adoption.

[STATISTIC]
"60% of vendors deliberately mask rising prices by bundling AI features, with customers paying for AI whether they use it or not, and opting out isn't an option."
— SoftwareSeni, "Why SaaS Prices Are Rising 4x Faster Than Inflation"
URL: [https://www.softwareseni.com/why-saas-prices-are-rising-4x-faster-than-inflation-and-what-you-can-do-about-it/](https://www.softwareseni.com/why-saas-prices-are-rising-4x-faster-than-inflation-and-what-you-can-do-about-it/)
Date: 2025

[STATISTIC]
"AI add-ons can add 30–110% to base costs, with Microsoft Copilot at a 60–70% premium. Gartner reports that AI-related SaaS costs will grow 30–50% annually as companies adopt copilots faster than governance can keep up."
— CloudEagle, "Hidden Cost of Microsoft Copilot: How AI Costs Scale"
URL: [https://www.cloudeagle.ai/blogs/microsoft-copilot-hidden-costs](https://www.cloudeagle.ai/blogs/microsoft-copilot-hidden-costs)
Date: 2025

[FACT]
"This AI tax appears across Microsoft M365, Google Workspace, Salesforce, and other platforms — vendors bundle AI capabilities (Copilot, Gemini, Einstein) into standard subscriptions and use this as justification for 10-20% price increases, regardless of whether organisations actually use AI features."
— SaaStr, "The Great SaaS Price Surge of 2025"
URL: [https://www.saastr.com/the-great-price-surge-of-2025-a-comprehensive-breakdown-of-pricing-increases-and-the-issues-they-have-created-for-all-of-us/](https://www.saastr.com/the-great-price-surge-of-2025-a-comprehensive-breakdown-of-pricing-increases-and-the-issues-they-have-created-for-all-of-us/)
Date: 2025

---

## 5. Price Increase Risk: SaaS Vendor Pricing Power Over Locked-In Customers

Locked-in customers face a structural negotiating disadvantage at renewal: switching costs are sunk, internal workflows are embedded, and the cost of evaluation alone deters serious alternatives analysis. Vendors have learned to exploit this asymmetry systematically.

### Current Price Increase Benchmarks

[STATISTIC]
"SaaS inflation reached 12.2% year-over-year — 4.5 times higher than general inflation in G7 countries at 2.7%."
— Vertice, SaaS Inflation Index
URL: [https://www.vertice.one/insights/saas-inflation-rate](https://www.vertice.one/insights/saas-inflation-rate)
Date: 2025–2026

[STATISTIC]
"SaaS inflation initially peaked at 14% in May 2025, eased slightly over the summer, but soared again in November."
— Vertice, "SaaS Inflation Stats: How to Mitigate in 2025"
URL: [https://www.vertice.one/blog/mitigating-2025-saas-inflation-stats](https://www.vertice.one/blog/mitigating-2025-saas-inflation-stats)
Date: 2025

[STATISTIC]
"SaaS costs per employee reached approximately $9,100 by end of 2025, up from $8,700 in 2024 and $7,900 in 2023 — an increase of almost 15% over two years."
— Vertice, SaaS Inflation Index
URL: [https://www.vertice.one/insights/saas-inflation-rate](https://www.vertice.one/insights/saas-inflation-rate)
Date: 2025

[STATISTIC]
"Price hikes varied across categories: sales software saw the most rapid increases at 10.6%, followed by finance (10.2%) and productivity tools (10.1%)."
— Vertice, "SaaS Inflation Stats: How to Mitigate in 2025"
URL: [https://www.vertice.one/blog/mitigating-2025-saas-inflation-stats](https://www.vertice.one/blog/mitigating-2025-saas-inflation-stats)
Date: 2025

[STATISTIC]
"More than a quarter (28%) of contracts have been impacted by shrinkflation techniques such as bundling of products and features to hide decreases in real value."
— Vertice, SaaS Inflation Index
URL: [https://www.vertice.one/insights/saas-inflation-rate](https://www.vertice.one/insights/saas-inflation-rate)
Date: 2025

### Specific Vendor Price Increases (2025)

| Vendor | Product | 2025 Price Increase |
|---|---|---|
| Adobe | Photo Plan (monthly billing) | +50% |
| Slack | Business+ | +20% ($12.50 → $15/user/mo) |
| Adobe | Creative Cloud Pro | +16.7% |
| Zendesk | Enterprise | +15% |
| Salesforce | Enterprise/Unlimited | +6% (August 2025) |
| Microsoft | M365 (monthly billing) | +5% surcharge |
| HubSpot | — | +5% migration fee |
| Atlassian | — | +7–15% |

Source: SaaStr, "The Great SaaS Price Surge of 2025"
URL: [https://www.saastr.com/the-great-price-surge-of-2025-a-comprehensive-breakdown-of-pricing-increases-and-the-issues-they-have-created-for-all-of-us/](https://www.saastr.com/the-great-price-surge-of-2025-a-comprehensive-breakdown-of-pricing-increases-and-the-issues-they-have-created-for-all-of-us/)

### Pricing as a Revenue Extraction Engine

[STATISTIC]
"In 2025, Salesforce's price increases of 6.3 percentage points vs. 8.7% total ARR growth — that's up to 72% of go-forward growth coming from price increases, not new customers or expansion."
— SaaStr, "Salesforce, Microsoft, Google and Atlassian All Raise Prices Again in 2025"
URL: [https://www.saastr.com/salesforce-microsoft-google-and-atlassian-all-raise-prices-again-in-2025-hooray/](https://www.saastr.com/salesforce-microsoft-google-and-atlassian-all-raise-prices-again-in-2025-hooray/)
Date: 2025

[QUOTE]
"Vendors have learned they can raise prices aggressively and most customers will absorb it rather than switch, as the power has shifted decisively to the vendors."
— SaaStr, "The Great SaaS Price Surge of 2025"
URL: [https://www.saastr.com/the-great-price-surge-of-2025-a-comprehensive-breakdown-of-pricing-increases-and-the-issues-they-have-created-for-all-of-us/](https://www.saastr.com/the-great-price-surge-of-2025-a-comprehensive-breakdown-of-pricing-increases-and-the-issues-they-have-created-for-all-of-us/)
Date: 2025

[STATISTIC]
"Gartner reports that corporate IT budgets are growing at just 2.8% annually, while SaaS vendors are hiking prices by 9-25%."
— CIO.com, "SaaS Price Hikes Put CIOs' Budgets in a Bind"
URL: [https://www.cio.com/article/4104365/saas-price-hikes-put-cios-budgets-in-a-bind.html](https://www.cio.com/article/4104365/saas-price-hikes-put-cios-budgets-in-a-bind.html)
Date: 2025

[FACT]
"The real money is rarely made in year one or two. It is extracted during renewals, when switching costs are high and internal dependency is already locked in."
— SoftwarePricingGuide.com, "SaaS Renewal Shock: Why Enterprise Software Costs Explode After Year 3"
URL: [https://softwarepricingguide.com/saas-renewal-shock-why-enterprise-software-costs-explode-after-year-3-and-how-cfos-stop-it/](https://softwarepricingguide.com/saas-renewal-shock-why-enterprise-software-costs-explode-after-year-3-and-how-cfos-stop-it/)
Date: 2025

---

## 6. Strategic Risk: Dependency on Vendor Roadmap Alignment

SaaS customers are passengers on a vendor's product roadmap. Features get sunsetted, pricing models shift, acquisition restructures product strategy, and AI bundling alters the capability-to-cost ratio — all on the vendor's timeline, not the customer's.

### Vendor Sunset and Forced Migration

[FACT]
"Epicor announced a sunset period for its on-premises releases of Kinetic, Prophet 21, and BisTrack, requiring customers to migrate to its Epicor Cloud SaaS platform if they want access to innovation and long-term support."
— SysGenPro, "ERP SaaS Business Risks and Mitigation"
URL: [https://sysgenpro.com/resources/erp-saas-business-risks-mitigation-2026](https://sysgenpro.com/resources/erp-saas-business-risks-mitigation-2026)
Date: 2026

[FACT]
"Enterprises must accept new dependencies on vendor-managed environments and trust they'll meet security, latency, uptime, and regulatory compliance requirements — sometimes with limited visibility or contractual recourse."
— SysGenPro, "ERP SaaS Business Risks and Mitigation"
URL: [https://sysgenpro.com/resources/erp-saas-business-risks-mitigation-2026](https://sysgenpro.com/resources/erp-saas-business-risks-mitigation-2026)
Date: 2026

[FACT]
"EU regulators have identified 19 'critical ICT providers' including AWS, Google, and Microsoft, highlighting growing concentration risk concerns as enterprises rely on a handful of technology giants for infrastructure."
— Cybersecurity Insiders, "From AWS to Cloudflare: Did 2025 Expose Your Enterprise's IT Dependency Risks?"
URL: [https://www.cybersecurity-insiders.com/from-aws-to-cloudflare-did-2025-expose-your-enterprises-it-dependency-risks/](https://www.cybersecurity-insiders.com/from-aws-to-cloudflare-did-2025-expose-your-enterprises-it-dependency-risks/)
Date: 2025

### Vendor Consolidation Reducing Competition

[FACT]
"SaaS vendors possess significant pricing power due to high customer switching costs, vendor consolidation reducing competition, and AI bundling that justifies premium pricing."
— SoftwareSeni, "Why SaaS Prices Are Rising 4x Faster Than Inflation"
URL: [https://www.softwareseni.com/why-saas-prices-are-rising-4x-faster-than-inflation-and-what-you-can-do-about-it/](https://www.softwareseni.com/why-saas-prices-are-rising-4x-faster-than-inflation-and-what-you-can-do-about-it/)
Date: 2025

[FACT]
"Relying on third-party low-code or no-code platforms can create strong dependency risks, as vendors may change pricing, restrict features, or discontinue services, potentially causing unexpected business disruptions. If exiting a vendor requires rebuilding workflows from scratch, the lock-in risk should materially lower the final score."
— AI SaaS Writer, "AI SaaS Product Classification Criteria Explained (2026)"
URL: [https://aisaaswriter.com/ai-saas-product-classification-criteria-2026/](https://aisaaswriter.com/ai-saas-product-classification-criteria-2026/)
Date: 2026

### The Forrester "SaaS-pocalypse" Signal

[QUOTE]
"SaaS as we know it is dead."
— Forrester, "SaaS As We Know It Is Dead: How To Survive The SaaS-pocalypse!"
URL: [https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/)
Date: 2026

[FACT]
"In early February 2026, SaaS company valuations saw a massive sell-off where over $1 trillion in market capitalization was erased from software stocks, triggered by rapid AI agent innovation."
— Multiple sources including Forrester and SaaStr (2026)
URL: [https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/)
Date: February 2026

[FACT]
"On January 29, 2026, SAP's shares plunged more than 16% after cloud revenue forecast disappointments, while ServiceNow fell 11%, as investors intensify fears that AI-driven automation is eroding traditional SaaS value."
— Tech Buzz AI, "SaaS Faces 'Existential' Crisis as AI Sparks Selloff"
URL: [https://www.techbuzz.ai/articles/saas-faces-existential-crisis-as-ai-sparks-selloff](https://www.techbuzz.ai/articles/saas-faces-existential-crisis-as-ai-sparks-selloff)
Date: 2026

### The Build Trend Signal

[STATISTIC]
"35% of respondents have replaced functionality of at least one SaaS tool with a custom build, and 78% expect to build more of their own tools in 2026. 60% of respondents reported creating tools outside of IT oversight in the past year."
— Retool survey (817 customers and builders across startups to Fortune 500 enterprises), cited in Newsweek
URL: [https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483](https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483)
Date: 2025–2026

[QUOTE]
"The cost of building custom software has collapsed. What used to take weeks of engineering time and six-figure budgets can now be prototyped in days."
— David Hsu, CEO of Retool, cited in Newsweek
URL: [https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483](https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483)
Date: 2025–2026

[QUOTE]
"The pendulum is swinging toward Build, with some AI-native companies reaching $100M ARR in 1–2 years instead of the traditional 5–10."
— Forrester, cited in multiple sources
URL: [https://www.forrester.com/blogs/predictions-2025-enterprise-software/](https://www.forrester.com/blogs/predictions-2025-enterprise-software/)
Date: 2025

---

## Aggregate Hidden Cost Stack: Summary Table

| Cost Category | Typical Enterprise Exposure | Source |
|---|---|---|
| Unused license waste (mid-enterprise) | $21M/year average | Zylo 2025 |
| Unused license waste (large enterprise) | $127M/year average | Zylo 2025 |
| Per-employee SaaS spend growth (YoY) | +21.9% | Zylo 2025 |
| SaaS inflation rate | 12.2% (4.5x CPI) | Vertice 2025–2026 |
| AI feature surcharge (MS Copilot) | +60–70% over base | CloudEagle 2025 |
| ERP migration (single wave) | ~$1.2M average | Binadox 2025 |
| Proprietary data format extraction | $2,000–$5,000/consultant engagement | CompareTiers 2025 |
| Annual SaaS customization spend (mid-enterprise) | ~$250,000 | GetMonetizely 2025 |
| Employee time lost to SaaS workarounds | Up to 23% of role time | GetMonetizely 2025 |
| Shadow IT as % of total SaaS spend | 40%+ | Zluri 2025 |

---

## Sources

- [Zylo, 2025 SaaS Management Index](https://zylo.com/news/2025-saas-management-index/)
- [Vertice, SaaS Inflation Rate Insights](https://www.vertice.one/insights/saas-inflation-rate)
- [Vertice, SaaS Inflation Stats: How to Mitigate in 2025](https://www.vertice.one/blog/mitigating-2025-saas-inflation-stats)
- [SaaStr, The Great SaaS Price Surge of 2025](https://www.saastr.com/the-great-price-surge-of-2025-a-comprehensive-breakdown-of-pricing-increases-and-the-issues-they-have-created-for-all-of-us/)
- [SaaStr, Salesforce, Microsoft, Google and Atlassian All Raise Prices Again in 2025](https://www.saastr.com/salesforce-microsoft-google-and-atlassian-all-raise-prices-again-in-2025-hooray/)
- [Binadox, SaaS Data Portability: Complete Exit Strategy Guide for 2025](https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/)
- [Clairfield, How the 2025 EU Data Act Rewrites the Rules for SaaS Providers](https://www.clairfield.com/how-the-2025-eu-data-act-rewrites-the-rules-for-saas-providers/)
- [NEdigital, Assessing Vendor Lock-in and Exit Costs in SaaS-Centric IT Environments](https://www.nedigital.com/en/blog/assessing-vendor-lock-in-and-exit-costs-in-saas-centric-it-environments)
- [GetMonetizely, How Much Should Custom Enterprise SaaS Modifications Really Cost?](https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost)
- [CompareTiers, 7 Hidden Costs of SaaS Pricing Nobody Talks About](https://comparetiers.com/blog/hidden-costs-saas-pricing)
- [Constellation Research, Enterprise Technology 2026: 15 AI, SaaS, Data, Business Trends to Watch](https://www.constellationr.com/blog-news/insights/enterprise-technology-2026-15-ai-saas-data-business-trends-watch)
- [DataFlowMapper, Data Migration Cost Analysis & Calculator (2025 Analysis)](https://dataflowmapper.com/blog/data-migration-costs-quantitative-analysis)
- [UpperEdge, IT Services Contracts: Beware of Cumulative Price Increases](https://upperedge.com/contract-negotiations/how-it-services-vendors-pocket-aces-with-cumulative-yearly-price-increases/)
- [UpperEdge, SaaS Vendors' New Trick: Multiplying Pricing Caps by Term Length](https://upperedge.com/knowledge-center/documents/podcasts/saas-vendors-new-trick-multiplying-pricing-caps-by-term-length/)
- [UpperEdge, A Hidden Renewal Clause That Could Quietly Inflate Your SaaS Costs](https://upperedge.com/contract-negotiations/hidden-renewal-clause-that-could-inflate-your-saas-costs/)
- [EZO AssetSonar, SaaS License Waste: The Hidden Cost in Your IT Budget](https://ezo.io/assetsonar/blog/saas-license-waste/)
- [Appunite, The SaaS Tax — You're Paying for 100%, Using 12%](https://www.appunite.com/blog/business-paying-for-100-saas-using-12)
- [Zluri, Shadow IT Statistics: Key Facts to Learn in 2025](https://www.zluri.com/blog/shadow-it-statistics-key-facts-to-learn-in-2024)
- [SoftwareSeni, Why SaaS Prices Are Rising 4x Faster Than Inflation](https://www.softwareseni.com/why-saas-prices-are-rising-4x-faster-than-inflation-and-what-you-can-do-about-it/)
- [CIO.com, SaaS Price Hikes Put CIOs' Budgets in a Bind](https://www.cio.com/article/4104365/saas-price-hikes-put-cios-budgets-in-a-bind.html)
- [SoftwarePricingGuide.com, SaaS Renewal Shock: Why Enterprise Software Costs Explode After Year 3](https://softwarepricingguide.com/saas-renewal-shock-why-enterprise-software-costs-explode-after-year-3-and-how-cfos-stop-it/)
- [CloudEagle, Hidden Cost of Microsoft Copilot: How AI Costs Scale](https://www.cloudeagle.ai/blogs/microsoft-copilot-hidden-costs)
- [Newsweek, Enterprises Are Replacing SaaS Faster Than You Think](https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483)
- [Forrester, SaaS As We Know It Is Dead: How To Survive The SaaS-pocalypse!](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/)
- [Forrester, Predictions 2025: A Year of Reckoning for Enterprise Application Vendors](https://www.forrester.com/blogs/predictions-2025-enterprise-software/)
- [Tech Buzz AI, SaaS Faces 'Existential' Crisis as AI Sparks Selloff](https://www.techbuzz.ai/articles/saas-faces-existential-crisis-as-ai-sparks-selloff)
- [SysGenPro, ERP SaaS Business Risks and Mitigation](https://sysgenpro.com/resources/erp-saas-business-risks-mitigation-2026)
- [Cybersecurity Insiders, From AWS to Cloudflare: Did 2025 Expose Your Enterprise's IT Dependency Risks?](https://www.cybersecurity-insiders.com/from-aws-to-cloudflare-did-2025-expose-your-enterprises-it-dependency-risks/)
- [AI SaaS Writer, AI SaaS Product Classification Criteria Explained (2026)](https://aisaaswriter.com/ai-saas-product-classification-criteria-2026/)
- [HubFi, Enterprise SaaS Platform: The Ultimate Guide (2025)](https://www.hubifi.com/blog/enterprise-software-vs-saas)
- [Bain & Company, Will Agentic AI Disrupt SaaS?](https://www.bain.com/insights/will-agentic-ai-disrupt-saas-technology-report-2025/)

---

## Key Takeaways

- **The SaaS waste floor is $21M per average enterprise.** Zylo's 2025 data — drawn from $40B in managed spend — shows 52.7% of licenses go unused, with the problem worsening 14% year-over-year. Large enterprises face $127M in annual waste. This is not a governance failure; it is a structural feature of per-seat, bundled SaaS pricing ([https://zylo.com/news/2025-saas-management-index/](https://zylo.com/news/2025-saas-management-index/)).

- **SaaS inflation at 12.2% (4.5x CPI) is primarily a pricing power story, not a cost structure story.** Salesforce extracted 72% of its 2025 ARR growth from price increases alone. Vendors have explicitly learned that locked-in customers absorb hikes rather than switch — making annual escalation a predictable and exploitable revenue mechanism ([https://www.vertice.one/insights/saas-inflation-rate](https://www.vertice.one/insights/saas-inflation-rate); [https://www.saastr.com/salesforce-microsoft-google-and-atlassian-all-raise-prices-again-in-2025-hooray/](https://www.saastr.com/salesforce-microsoft-google-and-atlassian-all-raise-prices-again-in-2025-hooray/)).

- **Data portability costs are a non-linear exit tax.** A representative large-scale migration costs ~$1.2M and takes ~8 months. Proprietary data formats, API paywalls, and connector fees compound over time — the longer a vendor relationship runs, the higher the effective exit toll becomes ([https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/](https://www.binadox.com/blog/saas-data-portability-planning-your-exit-strategy-before-you-need-it/)).

- **Customization ceilings generate invisible labor costs that never appear in TCO models.** A single documented case shows a sales team spending 23% of their time navigating around SaaS limitations rather than using the product. At enterprise scale, this productivity hemorrhage can exceed the license cost itself ([https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost](https://www.getmonetizely.com/articles/how-much-should-custom-enterprise-saas-modifications-really-cost)).

- **The build signal is accelerating.** 35% of enterprises have already replaced at least one SaaS function with a custom build; 78% plan to build more in 2026. Retool's CEO attributes this directly to the collapse in custom software build costs driven by agentic AI — the same dynamic that erased over $1 trillion in SaaS market cap in February 2026 ([https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483](https://www.newsweek.com/nw-ai/enterprises-are-replacing-saas-faster-than-you-think-11521483)).
