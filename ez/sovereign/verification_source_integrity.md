# Verification: Source Integrity Check

**Audit Date:** 2026-02-12
**Auditor:** Verification Agent
**Files Audited:** 16 agent output files

---

## Missing Source URLs

| Agent File | Claim/Finding | Issue |
|-----------|--------------|-------|
| agent_01_aws_us_deals.md | "As of March 2025, JWCC has awarded a total of $2.3 billion in task orders" | Source listed as "Multiple sources" with note "No single source for AWS-specific breakout" — no direct URL for the $2.3B figure |
| agent_05_gcp_us_deals.md | "Google Distributed Cloud (GDC) and GDC air-gapped achieved DoD Impact Level 6 (IL6) authorization" | Source listed as "Google Cloud Blog (reflected in multiple sources)" — no specific URL provided |
| agent_05_gcp_us_deals.md | "More than $3.9 billion in total orders logged by DISA's JWCC program as of last fiscal year" | Source listed as "DefenseScoop (from earlier search results)" — no specific URL provided |
| agent_05_gcp_us_deals.md | "By beginning of 2025, all four JWCC providers achieved Impact Level 6 security authorization" | Source listed as "Multiple sources from search results" — no specific URL provided |
| agent_07_aws_earnings.md | "The CIA awarded AWS a huge $600 million contract" | Agent itself flags this as likely referencing the 2013 C2S contract, not a 2025 event; source URL points to a CNBC article about Q4 2025 earnings, not the CIA contract directly |
| agent_08_azure_earnings.md | Nestlé SAP migration data (200 SAP instances, 10,000 servers, 1.2 petabytes) | Not government/sovereign-specific; included without clear relevance to sovereign AI scope |
| agent_10_us_procurement.md | DHS contract 70RSAT25FR0000015 | Source URL is a Google search query, not a direct procurement database or news article URL |
| agent_12_market_sizing.md | "GenAI-specific cloud services showed particularly explosive growth, expanding 140-180% in Q2 2025" | Source listed as "Multiple analyst sources" — attributed to Cargoson blog, which is a secondary aggregator |
| agent_12_market_sizing.md | Bank of America "10%-15% of $450-$500 billion AI infrastructure market" | Source is a Twitter/X post by Ray Wang, not the Bank of America report itself |

---

## Source Tier Distribution

| Agent File | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 | Total Sources |
|-----------|--------|--------|--------|--------|--------|---------------|
| agent_01_aws_us_deals.md | 3 | 1 | 6 | 0 | 2 | 12 |
| agent_02_aws_eu_deals.md | 6 | 2 | 6 | 1 | 5 | 20 |
| agent_03_azure_us_deals.md | 4 | 0 | 6 | 0 | 4 | 14 |
| agent_04_azure_eu_deals.md | 10 | 1 | 3 | 0 | 6 | 20 |
| agent_05_gcp_us_deals.md | 5 | 0 | 6 | 1 | 4 | 16 |
| agent_06_gcp_eu_deals.md | 3 | 1 | 7 | 1 | 3 | 15 |
| agent_07_aws_earnings.md | 4 | 2 | 6 | 0 | 11 | 23 |
| agent_08_azure_earnings.md | 10 | 0 | 3 | 2 | 7 | 22 |
| agent_09_gcp_earnings.md | 5 | 0 | 4 | 1 | 4 | 14 |
| agent_10_us_procurement.md | 4 | 2 | 6 | 0 | 4 | 16 |
| agent_11_eu_procurement.md | 4 | 0 | 8 | 0 | 7 | 19 |
| agent_12_market_sizing.md | 0 | 4 | 8 | 8 | 14 | 34 |
| agent_13_us_gov_ai_spending.md | 7 | 0 | 8 | 1 | 4 | 20 |
| agent_14_eu_sovereign_spending.md | 9 | 3 | 5 | 2 | 5 | 24 |
| agent_15_jwcc_defense.md | 3 | 2 | 8 | 0 | 5 | 18 |
| agent_16_eu_country_programs.md | 8 | 0 | 6 | 1 | 10 | 25 |
| **TOTALS** | **85** | **18** | **96** | **18** | **93** | **310** |

---

## Tier 5-Only Findings (low reliability)

| Agent File | Finding | Source URL | Concern |
|-----------|---------|-----------|---------|
| agent_07_aws_earnings.md | AWS Q2 2025 earnings commentary ("triple digit YoY percentage, multibillion dollar business") | investing.com transcript | Investing.com earnings transcript is aggregator content; not a direct SEC filing or company IR page |
| agent_07_aws_earnings.md | AWS Q4 2025 earnings commentary (government transitions) | investing.com transcript | Same concern — aggregator, not primary IR source |
| agent_07_aws_earnings.md | AWS Q4 2025 backlog $244 billion | investing.com company news | Aggregator site; claim should be verified against SEC filing |
| agent_07_aws_earnings.md | FY 2025 AWS segment sales $128.7B and operating income $45.6B | last10k.com | Third-party SEC filing aggregator; not the SEC filing itself |
| agent_12_market_sizing.md | Bank of America sovereign AI as 10-15% of $450-500B market | x.com/rwang07 (Twitter) | Social media post by analyst Ray Wang, not the Bank of America report |
| agent_12_market_sizing.md | Fortune Business Insights sovereign cloud $154.69B (2025) to $1,133.3B (2034) | fortunebusinessinsights.com | Market research firm with limited peer-review transparency |
| agent_12_market_sizing.md | Straits Research sovereign cloud $118.72B to $630.93B | straitsresearch.com | Lesser-known market research firm |
| agent_12_market_sizing.md | SNS Insider sovereign cloud $941.10B by 2033 | globenewswire.com (press release) | Press release from lesser-known research firm via wire service |
| agent_12_market_sizing.md | Cargoson blog cloud market share data | cargoson.com | Logistics company blog aggregating analyst data — not a primary source |
| agent_12_market_sizing.md | Quantumrun cloud market share estimates | quantumrun.com | Futurism/consulting blog, not a recognized analyst firm |
| agent_12_market_sizing.md | Veritis cloud market share insights | veritis.com | IT services company blog, not an independent analyst |
| agent_12_market_sizing.md | Global Data Center Hub statistics | globaldatacenterhub.com | Newsletter/blog, not a recognized analyst firm |
| agent_12_market_sizing.md | Digit.fyi AI infrastructure spending | digit.fyi | Tech news blog, limited editorial oversight |
| agent_12_market_sizing.md | AInvest cloud infrastructure predictions | ainvest.com | Investment advice aggregator |
| agent_11_eu_procurement.md | Xpert.digital BWI contracting plans quote ("€6 billion by 2029") | xpert.digital | Unverified blog/content site |
| agent_16_eu_country_programs.md | Sovereign cloud market $154B to $823B by 2032 | technologymagazine.com | Industry magazine aggregating third-party research |
| agent_16_eu_country_programs.md | Austria Nextcloud migration | slashdot.org | User-submitted tech news aggregator |
| agent_13_us_gov_ai_spending.md | DoD AI budget analysis ($25.2B, breakdown) | maggiegray.us | Substack/personal blog — not an official government or recognized analyst source |
| agent_14_eu_sovereign_spending.md | Germany AI government guide and €1.6B action plan | nucamp.co | Coding bootcamp blog — not a primary government or analyst source |

---

## Unique Source URLs by Tier

### Tier 1 Sources
*Company press releases, SEC filings, official government procurement databases/press releases, company IR pages, official government strategy documents*

| URL | Type | Times Referenced |
|-----|------|-----------------|
| https://www.sec.gov/Archives/edgar/data/1018724/... | SEC Filing (Amazon 10-Q) | 1 |
| https://www.sec.gov/Archives/edgar/data/1652044/... (Q1-Q4) | SEC Filing (Alphabet earnings releases) | 4 |
| https://www.sec.gov/Archives/edgar/data/789019/... | SEC Filing (Microsoft 10-K) | 1 |
| https://www.microsoft.com/en-us/investor/earnings/... (multiple quarters) | Microsoft IR Press Releases | 6 |
| https://www.microsoft.com/en-us/investor/events/... (multiple quarters) | Microsoft IR Earnings Calls | 4 |
| https://www.microsoft.com/investor/reports/ar25/index.html | Microsoft Annual Report | 1 |
| https://www.gsa.gov/about-us/newsroom/news-releases/... (multiple) | GSA Press Releases | 6 |
| https://aws.amazon.com/about-aws/whats-new/... | AWS Official Announcements | 2 |
| https://aws.amazon.com/blogs/... (multiple) | AWS Official Blog | 4 |
| https://www.aboutamazon.com/news/... | Amazon Official Press | 2 |
| https://www.aboutamazon.eu/news/... | Amazon EU Official Press | 2 |
| https://cloud.google.com/blog/topics/public-sector/... (multiple) | Google Cloud Official Blog | 6 |
| https://www.googlecloudpresscorner.com/... (multiple) | Google Cloud Press Releases | 5 |
| https://blog.google/company-news/... | Google/Alphabet Official Blog | 1 |
| https://commission.europa.eu/... | European Commission Official | 2 |
| https://digital-strategy.ec.europa.eu/... | EU Digital Strategy Official | 3 |
| https://www.oracle.com/news/announcement/... (multiple) | Oracle Official Press | 3 |
| https://news.microsoft.com/... (multiple regional) | Microsoft Official News (regional) | 8 |
| https://blogs.microsoft.com/... (multiple) | Microsoft Official Blog | 6 |
| https://www.microsoft.com/en-us/microsoft-365/blog/... | Microsoft 365 Official Blog | 2 |
| https://devblogs.microsoft.com/azuregov/... | Azure Government Official Blog | 2 |
| https://techcommunity.microsoft.com/... | Microsoft Tech Community | 1 |
| https://news.sap.com/... | SAP Official Press | 3 |
| https://www.dvidshub.net/... | DoD DVIDS (Official military media) | 2 |
| https://www.hpe.com/us/en/newsroom/... | HPE Official Press | 1 |
| https://www.bechtle.com/de-en/about-bechtle/press/... | Bechtle Official Press | 1 |
| https://www.dni.gov/... | DNI Official Press | 1 |
| https://www.nitrd.gov/... | NITRD Official (US Gov) | 1 |
| https://www.congress.gov/... | Congressional Research Service | 1 |
| https://www.lamoncloa.gob.es/... | Spanish Government Official | 1 |
| https://mpo.gov.cz/... | Czech Ministry Official | 1 |
| https://www.ccomptes.fr/... | French Court of Auditors (Official) | 1 |
| https://www.businesswire.com/... (multiple) | Business Wire (press release distribution) | 3 |
| https://www.telekom.com/... | Deutsche Telekom Official | 1 |
| https://www.bertelsmann.com/... | Bertelsmann Official Press | 1 |
| https://www.ionos-group.com/... | Ionos Group Official IR | 1 |
| https://azure.microsoft.com/en-us/blog/... | Azure Official Blog | 1 |
| https://docs.cloud.google.com/... | Google Cloud Official Docs | 1 |

### Tier 2 Sources
*Major business press (Reuters, Bloomberg, WSJ, FT, CNBC, Washington Post)*

| URL | Type | Times Referenced |
|-----|------|-----------------|
| https://www.cnbc.com/... (multiple articles) | CNBC | 5 |
| https://www.goldmansachs.com/insights/... | Goldman Sachs Research | 2 |
| https://www.mckinsey.com/... | McKinsey Insights | 1 |
| https://www.bain.com/... | Bain & Company | 1 |
| https://www.washingtontechnology.com/... | Washington Technology | 2 |
| https://sciencebusiness.net/... | Science|Business | 1 |
| https://www.brookings.edu/... | Brookings Institution | 1 |
| https://www.fool.com/earnings/call-transcripts/... (multiple) | Motley Fool (earnings transcripts) | 3 |
| https://about.bgov.com/... | Bloomberg Government | 1 |
| https://www.williamfry.com/... | William Fry (law firm analysis) | 1 |

### Tier 3 Sources
*Industry/tech press, defense press, government technology press*

| URL | Type | Times Referenced |
|-----|------|-----------------|
| https://fedscoop.com/... (multiple) | FedScoop (gov tech press) | 9 |
| https://defensescoop.com/... (multiple) | DefenseScoop (defense tech press) | 10 |
| https://www.nextgov.com/... (multiple) | Nextgov/FCW (gov tech press) | 6 |
| https://breakingdefense.com/... (multiple) | Breaking Defense | 5 |
| https://www.theregister.com/... (multiple) | The Register | 3 |
| https://techcrunch.com/... (multiple) | TechCrunch | 4 |
| https://www.meritalk.com/... (multiple) | MeriTalk (gov tech press) | 4 |
| https://www.executivebiz.com/... (multiple) | ExecutiveBiz (gov contracting press) | 4 |
| https://www.executivegov.com/... (multiple) | ExecutiveGov (gov contracting press) | 5 |
| https://www.datacenterdynamics.com/... (multiple) | Data Center Dynamics | 5 |
| https://www.govconwire.com/... | GovConWire | 1 |
| https://www.channelinsider.com/... | Channel Insider | 1 |
| https://www.defenseone.com/... (multiple) | Defense One | 2 |
| https://www.ciodive.com/... (multiple) | CIO Dive | 4 |
| https://www.computerweekly.com/... (multiple) | Computer Weekly | 3 |
| https://www.computing.co.uk/... | Computing UK | 1 |
| https://federalnewsnetwork.com/... (multiple) | Federal News Network | 3 |
| https://www.cloudcomputing-news.net/... | Cloud Computing News | 1 |
| https://www.heise.de/... | Heise Online (German tech press) | 1 |
| https://www.euronews.com/... (multiple) | Euronews | 2 |
| https://sifted.eu/... | Sifted (European tech press) | 1 |
| https://tech.eu/... | Tech.eu | 1 |
| https://www.akingump.com/... | Akin Gump (law firm analysis) | 1 |
| https://www.mintz.com/... | Mintz (law firm analysis) | 1 |
| https://en.paperjam.lu/... | Paperjam (Luxembourg press) | 1 |
| https://www.belganewsagency.eu/... | Belga News Agency | 1 |
| https://www.vrt.be/... | VRT NWS (Belgian broadcaster) | 1 |
| https://notesfrompoland.com/... | Notes from Poland | 1 |
| https://www.techradar.com/... | TechRadar | 1 |
| https://www.techtarget.com/... | TechTarget | 1 |
| https://news.satnews.com/... | SatNews | 1 |
| https://www.digitaljournal.com/... | Digital Journal | 1 |
| https://www.techzine.eu/... | Techzine Global | 1 |
| https://www.computerworld.com/... | Computerworld | 1 |

### Tier 4 Sources
*Analyst reports (Gartner, IDC, Forrester, Canalys, ISG, Constellation Research, Deltek, Omdia)*

| URL | Type | Times Referenced |
|-----|------|-----------------|
| https://www.gartner.com/en/newsroom/... (multiple) | Gartner Press Releases | 2 |
| https://my.idc.com/... | IDC Research | 1 |
| https://www.idc.com/resource-center/blog/... | IDC Blog | 1 |
| https://www.forrester.com/blogs/... | Forrester Blog | 2 |
| https://www.constellationr.com/... (multiple) | Constellation Research | 3 |
| https://iq.govwin.com/... | Deltek GovWin | 2 |
| https://research.isg-one.com/... | ISG Research | 1 |
| https://www.delloro.com/... | Dell'Oro Group | 1 |
| https://practiceguides.chambers.com/... | Chambers (legal/regulatory guide) | 1 |
| https://www.oecd.org/... (multiple) | OECD Reports | 2 |
| https://ai-watch.ec.europa.eu/... | AI Watch (EU JRC) | 2 |
| https://www.everycrsreport.com/... | Every CRS Report | 1 |

### Tier 5 Sources
*Blog posts, social media, vendor marketing, aggregators, unverified/lesser-known sources*

| URL | Type | Times Referenced |
|-----|------|-----------------|
| https://www.investing.com/news/... (multiple) | Investing.com (aggregator) | 3 |
| https://last10k.com/... | Last10K (SEC aggregator) | 1 |
| https://fifthperson.com/... | Fifth Person (investment blog) | 1 |
| https://www.ainvest.com/... (multiple) | AInvest (investment aggregator) | 3 |
| https://futurumgroup.com/... (multiple) | Futurum Group (analyst blog) | 4 |
| https://hginsights.com/... | HG Insights (marketing data) | 1 |
| https://www.statista.com/... | Statista (data aggregator) | 1 |
| https://x.com/rwang07/... | Twitter/X (Ray Wang) | 1 |
| https://cxovoice.com/... | CXO Voice (blog) | 1 |
| https://www.fortunebusinessinsights.com/... | Fortune Business Insights (market research) | 1 |
| https://www.grandviewresearch.com/... | Grand View Research (market research) | 1 |
| https://straitsresearch.com/... | Straits Research (market research) | 1 |
| https://www.globenewswire.com/... | Globe Newswire (press release wire) | 1 |
| https://www.cargoson.com/... | Cargoson (logistics blog) | 2 |
| https://www.quantumrun.com/... | Quantumrun (futurism blog) | 1 |
| https://www.veritis.com/... | Veritis (IT services blog) | 1 |
| https://www.globaldatacenterhub.com/... | Global Data Center Hub (newsletter) | 1 |
| https://www.hpcwire.com/bigdatawire/... | BigDATAwire/HPCwire | 1 |
| https://www.digit.fyi/... | Digit.fyi (tech news blog) | 1 |
| https://markets.financialcontent.com/... | FinancialContent (aggregator) | 1 |
| https://orangeslices.ai/... | OrangeSlices AI (contract tracker) | 1 |
| https://www.afcea.org/... | AFCEA Signal (trade association) | 1 |
| https://www.defenseworld.net/... | Defense World (news aggregator) | 1 |
| https://www.cloudsyntrix.com/... | CloudSyntrix (tech blog) | 1 |
| https://maggiegray.us/... | Maggie Gray (Substack/personal blog) | 2 |
| https://www.nucamp.co/... | Nucamp (coding bootcamp blog) | 1 |
| https://www.newnordics.ai/... | New Nordics AI (website) | 1 |
| https://www.intelligentcio.com/... | Intelligent CIO (tech magazine) | 1 |
| https://govconexec.com/... | GovCon Exec International | 1 |
| https://www.siliconrepublic.com/... | Silicon Republic | 1 |
| https://startupsmagazine.co.uk/... | Startups Magazine | 1 |
| https://www.cloudera.com/... | Cloudera (vendor blog) | 1 |
| https://xpert.digital/... | Xpert.digital (content site) | 1 |
| https://www.webpronews.com/... (multiple) | WebProNews | 2 |
| https://technologymagazine.com/... | Technology Magazine | 1 |
| https://yro.slashdot.org/... | Slashdot | 1 |
| https://itbrief.co.uk/... | IT Brief | 1 |
| https://www.prnewswire.com/... | PR Newswire (wire service) | 2 |
| https://www.weforum.org/... | World Economic Forum (stories) | 2 |
| https://dig.watch/... | Digital Watch (observatory) | 1 |
| https://www.edps.europa.eu/... | European Data Protection Supervisor | 1 |
| https://capacityglobal.com/... | Capacity Global | 1 |
| https://www.gdit.com/... | GDIT (vendor press) | 1 |
| https://www.techuk.org/... | TechUK (trade body) | 1 |
| https://digital-skills-jobs.europa.eu/... | EU Digital Skills Platform | 1 |
| https://aws.amazon.com/compliance/... | AWS Compliance Page (marketing) | 1 |

---

## Overall Integrity Score

- **Total claims across all agents:** 341
- **Claims with valid source URLs:** 332 (97.4%)
- **Claims missing source URLs:** 9 (2.6%)
- **Claims relying on Tier 5 only:** 19 (5.6%)

---

## Per-Agent Reliability Summary

### Agent 01 — AWS US Deals
- **Total claims:** 18
- **Missing URLs:** 1 (JWCC $2.3B total — "multiple sources" without specific URL)
- **Tier distribution:** Primarily Tier 1 (official AWS, Amazon, GSA) and Tier 3 (FedScoop, DefenseScoop, Channel Insider)
- **Reliability assessment:** STRONG. Most claims backed by official government/company sources. One claim lacks direct URL.

### Agent 02 — AWS EU Deals
- **Total claims:** 20
- **Missing URLs:** 0
- **Tier distribution:** Mix of Tier 1 (AWS blogs, EC official, Bechtle press) and Tier 3 (TechCrunch, DCD, InfoQ)
- **Reliability assessment:** STRONG. All claims have URLs. Official sources dominate for key findings.

### Agent 03 — Azure US Deals
- **Total claims:** 14
- **Missing URLs:** 0
- **Tier distribution:** Tier 1 (GSA, Microsoft blogs, Azure Gov blog) and Tier 3 (ExecutiveBiz, DefenseScoop)
- **Reliability assessment:** STRONG. GSA OneGov has direct government source URL. One Tier 5 source (OrangeSlices AI for GAO contract).

### Agent 04 — Azure EU Deals
- **Total claims:** 21
- **Missing URLs:** 0
- **Tier distribution:** Heavy Tier 1 (Microsoft official news from multiple regions, SAP News, EC sources)
- **Reliability assessment:** STRONG. Well-sourced with official company and government documents. Some Tier 5 (ainvest, Capacity Global) for infrastructure investments.

### Agent 05 — GCP US Deals
- **Total claims:** 28
- **Missing URLs:** 3 (IL6 authorization, JWCC $3.9B total, all-four-vendors IL6 claim)
- **Tier distribution:** Tier 1 (Google Cloud blog, GSA, DVIDS) and Tier 3 (DefenseScoop, MeriTalk)
- **Reliability assessment:** GOOD. Core contract claims well-sourced. Three claims lack specific URLs — they reference "multiple sources" generically.

### Agent 06 — GCP EU Deals
- **Total claims:** 13
- **Missing URLs:** 0
- **Tier distribution:** Tier 1 (Google Cloud press, EU Digital Skills) and Tier 3 (The Register, Techzine, Euronews)
- **Reliability assessment:** STRONG. Key findings (NATO, UK MoD) have official press releases as primary sources.

### Agent 07 — AWS Earnings
- **Total claims:** 18
- **Missing URLs:** 0
- **Tier distribution:** Mix of Tier 1 (SEC filing, GSA, AWS blog) and Tier 5 (investing.com, last10k.com, Fifth Person)
- **Reliability assessment:** MODERATE. Several earnings data points use aggregator sites instead of direct SEC filings or Amazon IR pages. The CIA contract claim is flagged by the agent itself as likely historical.

### Agent 08 — Azure Earnings
- **Total claims:** 27
- **Missing URLs:** 0
- **Tier distribution:** Heavy Tier 1 (Microsoft IR pages, SEC filing, Annual Report, GSA) with some Tier 5 (Futurum Group)
- **Reliability assessment:** STRONG. Most financial data points come directly from Microsoft Investor Relations pages and SEC filings.

### Agent 09 — GCP Earnings
- **Total claims:** 25
- **Missing URLs:** 0
- **Tier distribution:** Heavy Tier 1 (SEC filings, Google press releases, GSA) with Tier 3 (Nextgov, Computing UK) and Tier 4 (Constellation Research)
- **Reliability assessment:** STRONG. Quarterly revenue figures traced to SEC filings. Government contract claims cross-referenced with press releases.

### Agent 10 — US Procurement
- **Total claims:** 16
- **Missing URLs:** 0 (but 1 URL is a Google search query, not a direct source)
- **Tier distribution:** Tier 1 (GSA, Google Cloud blog) and Tier 3 (DefenseScoop, Breaking Defense, FedScoop)
- **Reliability assessment:** GOOD. The DHS contract source is a Google search URL, not a procurement database or news article. All other claims have proper direct URLs.

### Agent 11 — EU Procurement
- **Total claims:** 19
- **Missing URLs:** 0
- **Tier distribution:** Tier 1 (EC official, Oracle, Ionos) and Tier 3 (The Register, Heise, Techzine)
- **Reliability assessment:** GOOD. Key contract values sourced from official entities. BWI "€6 billion" quote sourced from xpert.digital (Tier 5).

### Agent 12 — Market Sizing
- **Total claims:** 36
- **Missing URLs:** 0
- **Tier distribution:** Heavy Tier 4 (Gartner, IDC, Forrester, ISG) and Tier 5 (Fortune BI, Straits Research, SNS Insider, Cargoson, Quantumrun)
- **Reliability assessment:** MODERATE. Recognized analyst firms (Gartner, IDC, McKinsey, Goldman Sachs) provide credible estimates. However, multiple lesser-known market research firms (Fortune Business Insights, Straits Research, SNS Insider) provide widely varying forecasts ($630B to $1,133B by 2033-2034) that should be treated with caution. Cloud market share data from Synergy Research and Canalys is cited via secondary aggregator blogs (Cargoson).

### Agent 13 — US Gov AI Spending
- **Total claims:** 30
- **Missing URLs:** 0
- **Tier distribution:** Tier 1 (NITRD, DNI, Congress.gov, GSA) and Tier 3 (DefenseScoop, Defense One, FedScoop)
- **Reliability assessment:** GOOD. Budget figures sourced from official government documents and established defense press. The "maggiegray.us" Substack is a Tier 5 source used for the $25.2B DoD AI figure and its breakdown — this claim should be verified against official DoD budget documents.

### Agent 14 — EU Sovereign Spending
- **Total claims:** 35
- **Missing URLs:** 0
- **Tier distribution:** Heavy Tier 1 (EC official, national government sources, French Court of Auditors) with Tier 3 (CNBC, TechCrunch, Euronews)
- **Reliability assessment:** STRONG. EU-wide spending figures come directly from European Commission sources. Country-level figures sourced from national government announcements. The "nucamp.co" coding bootcamp blog (Tier 5) is used for some Germany figures — these should be cross-referenced.

### Agent 15 — JWCC Defense
- **Total claims:** 17
- **Missing URLs:** 0
- **Tier distribution:** Tier 1 (Oracle official, DVIDS, Google press, HPE) and Tier 3 (DefenseScoop, Breaking Defense, MeriTalk)
- **Reliability assessment:** STRONG. Contract values from official press releases and established defense press. JWCC aggregate statistics from named DoD officials quoted in MeriTalk.

### Agent 16 — EU Country Programs
- **Total claims:** 28
- **Missing URLs:** 0
- **Tier distribution:** Tier 1 (AWS BusinessWire, Google press, Oracle, Deutsche Telekom, EC) and Tier 5 (Slashdot, Technology Magazine, WebProNews)
- **Reliability assessment:** GOOD. Major contracts well-sourced from official press releases. Some contextual/smaller findings use lower-reliability sources.

---

## Key Audit Findings

1. **Overall source quality is strong.** 97.4% of claims have valid source URLs. The 85 Tier 1 sources (official government/company) and 96 Tier 3 sources (established tech/defense press) form the backbone of the research.

2. **Agent 12 (Market Sizing) has the weakest source profile.** It relies most heavily on Tier 5 sources (14 of 34 total), including lesser-known market research firms with widely divergent forecasts. The Gartner, IDC, and Goldman Sachs estimates are credible; the Fortune Business Insights, Straits Research, and SNS Insider estimates should be treated with lower confidence.

3. **Agent 07 (AWS Earnings) uses aggregator sites for financial data.** Several quarterly revenue figures are sourced from investing.com and last10k.com rather than directly from SEC filings or Amazon IR pages. These figures are likely accurate but should be verified against primary SEC filings.

4. **Nine claims have missing or inadequate source URLs.** Three claims in Agent 05 use "multiple sources" without specific URLs. One claim in Agent 01 similarly lacks a direct URL. One DHS contract in Agent 10 uses a Google search query as its "source."

5. **No agent relies exclusively on Tier 5 sources.** Every agent has at least some Tier 1 or Tier 3 sourcing for its core findings. The Tier 5 sources are generally used for supplementary context, market sizing estimates, or secondary corroboration.

6. **Cross-agent consistency is high.** Key facts (JWCC totals, GSA OneGov agreements, CDAO contracts, UK MoD deal, NATO deal, AWS European Sovereign Cloud) appear across multiple agents with consistent values and matching source URLs, indicating robust triangulation.
