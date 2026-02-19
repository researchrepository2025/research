# F71 — On-Premises Security Operations (SOC)

**Research Question:** What are the requirements, operational characteristics, and trade-offs of running security operations (SIEM, IDS/IPS, vulnerability scanning, incident response, runtime security) in a 100% on-premises environment, and how does this compare to cloud-native security operations services?

---

## Executive Summary

Running a full security operations capability on-premises requires assembling and perpetually maintaining a portfolio of distinct tools — SIEM, IDS/IPS, vulnerability scanners, runtime security agents, and threat intelligence platforms — each demanding dedicated tuning, hardware, and staff expertise. According to the [2025 SANS SOC Survey](https://swimlane.com/blog/global-soc-survey-insights/), 73% of organizations cite false positives as their number one detection challenge, and 66% of teams cannot keep pace with incoming alert volumes, a burden that falls disproportionately on self-hosted environments where every rule, feed, and integration must be managed in-house. Staffing a 24/7 on-premises SOC requires a minimum of 12 dedicated professionals at an annual run rate of $1.5M–$5M depending on maturity tier, per [Netsurion's SOC cost analysis](https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center). Cloud-native managed services (AWS GuardDuty, Microsoft Sentinel, GCP Security Command Center) eliminate most infrastructure and rule-management overhead but introduce data residency and customization constraints that may be incompatible with regulated or air-gapped ISV deployments. ISVs serving customers with strict sovereignty or air-gap requirements must plan for on-premises security operations as a sustained operational investment, not a one-time deployment.

---

## 1. SIEM: Self-Hosted Deployment

### 1.1 Tool Landscape

The three dominant self-hosted SIEM options for ISVs are:

- **Wazuh** (open-source XDR/SIEM): [https://wazuh.com/platform/siem/](https://wazuh.com/platform/siem/)
- **ELK Stack** (Elasticsearch, Logstash, Kibana): [https://logz.io/blog/elk-siem/](https://logz.io/blog/elk-siem/)
- **Splunk Enterprise** (commercial): [https://docs.splunk.com/Documentation/Splunk/9.4.2/Capacity/Referencehardware](https://docs.splunk.com/Documentation/Splunk/9.4.2/Capacity/Referencehardware)

### 1.2 Hardware Requirements

[FACT] Wazuh quickstart single-node deployment (up to 100 endpoints, 90-day retention):

| Agents | CPU | RAM | Storage (90 days) |
|--------|-----|-----|-------------------|
| 1–25 | 4 vCPU | 8 GiB | 50 GB |
| 25–50 | 8 vCPU | 8 GiB | 100 GB |
| 50–100 | 8 vCPU | 8 GiB | 200 GB |

Source: [Wazuh Quickstart Documentation](https://documentation.wazuh.com/current/quickstart.html)

[FACT] Wazuh Indexer (Wazuh's OpenSearch layer) recommended production specs: 16 GB RAM, 8 CPU cores.
Source: [Wazuh Installation Guide — Wazuh Server](https://documentation.wazuh.com/current/installation-guide/wazuh-server/index.html)

[FACT] For Splunk Enterprise, the reference hardware specification calls for 16 physical CPU cores (or 32 vCPU at 2 GHz or greater) as the minimum baseline for a production-grade indexer node.
Source: [Splunk Reference Hardware](https://docs.splunk.com/Documentation/Splunk/9.4.2/Capacity/Referencehardware)

### 1.3 Log Storage Sizing

[STATISTIC] A common industry conversion: 1,000 EPS (Events Per Second) ≈ 8.6 GB/day of raw log volume. A single SIEM indexer node can handle up to 250 GB/day; beyond that, a multi-node architecture is required.
Source: [SIEM Hot Storage Requirements Accuracy Analysis — Medium/Ertugrul Akbas](https://drertugrulakbas.medium.com/siem-hot-storage-requirements-accuracy-analysis-c412681155a9)

[FACT] Compliance frameworks (PCI DSS, HIPAA, SOX) require log retention between 1 and 7 years, with common operational architectures splitting into 90-day "hot" queryable storage and 1-year "cold" archival storage.
Source: [SIEM Data Retention Best Practices — ClearNetwork](https://clearnetwork.com/siem-data-retention-best-practices-for-effective-threat-detection/)

[FACT] Organizations should plan for 20–30% annual growth in log volume when sizing initial storage infrastructure.
Source: [How to Correctly Size Your SIEM Investment — LinkedIn/Kerem Ozturk](https://www.linkedin.com/pulse/how-correctly-size-your-siem-investment-kerem-ozturk)

### 1.4 Log Correlation and Alert Tuning

[FACT] Wazuh correlates events from servers, endpoints, and network devices using a decoder-and-rule pipeline: decoders parse raw logs from sources including Cisco, Checkpoint, Palo Alto, and AWS into a standard format before rule-based correlation fires.
Source: [Wazuh SIEM Platform](https://wazuh.com/platform/siem/)

[FACT] ELK Stack SIEM deployments require a baseline period of approximately two weeks to establish normal system behavior before alert thresholds can be tuned effectively to reduce false positives.
Source: [Using the ELK Stack for SIEM — Logz.io](https://logz.io/blog/elk-siem/)

[STATISTIC] Per the [2025 SANS Detection & Response Survey](https://www.stamus-networks.com/blog/what-the-2025-sans-detection-response-survey-reveals-false-positives-alert-fatigue-are-worsening): 73% of organizations identify false positives as their number-one detection challenge — up from the prior year. The proportion reporting "very frequent" false positives rose from 13% to 20% year-over-year.

[STATISTIC] Per [SANS 2025 SOC Survey](https://swimlane.com/blog/global-soc-survey-insights/): 42% of SOCs dump all incoming data into a SIEM without a defined ingestion strategy, directly worsening alert volumes.

### 1.5 Operational Characteristics — SIEM

[FACT] 42% of SOCs dump all incoming data into a SIEM without a defined strategy.
Source: [SANS 2025 SOC Survey — Swimlane](https://swimlane.com/blog/global-soc-survey-insights/)

[FACT] 69% of SOCs rely on manual or mostly manual processes for metrics reporting, adding to analyst burden in self-hosted environments.
Source: [SANS 2025 SOC Survey — Swimlane](https://swimlane.com/blog/global-soc-survey-insights/)

---

## 2. IDS/IPS: Network-Based and Host-Based Intrusion Detection

### 2.1 Tool Landscape

- **Suricata** (open-source, multi-threaded NIDS/NIPS): [https://suricata.io/](https://suricata.io/)
- **Snort 3** (open-source, Cisco-maintained): [https://www.snort.org/](https://www.snort.org/)
- **Wazuh** (host-based IDS component with FIM and log-based detection): [https://documentation.wazuh.com/current/](https://documentation.wazuh.com/current/)

### 2.2 Deployment Modes

[FACT] IDS/IPS can be deployed in two primary modes: (1) passive monitoring via SPAN port or network TAP — provides full visibility without traffic disruption risk; (2) inline IPS mode — drops or resets packets at wire speed but introduces outage risk if rules misfire.
Source: [Implementing IDS/IPS with Snort or Suricata — DoHost](https://dohost.us/index.php/2025/10/18/implementing-intrusion-detection-prevention-systems-ids-ips-with-snort-or-suricata/)

[FACT] Suricata uses native multi-threading to scale across CPU cores. Snort historically favors single-threaded processing, limiting performance on high-throughput links.
Source: [Suricata vs Snort — Stamus Networks](https://www.stamus-networks.com/suricata-vs-snort)

### 2.3 Hardware Sizing (Suricata)

[FACT] Production Suricata hardware requirements by network size:

| Network Size | RAM Requirement |
|--------------|-----------------|
| Small (≤100 Mbps) | 16 GB RAM minimum |
| Medium (100 Mbps – 1 Gbps) | 16–128 GB RAM |
| Large (1–10 Gbps) | 128–256 GB RAM |

Source: [Hardware Requirements — Security Onion Documentation 2.4](https://docs.securityonion.net/en/2.4/hardware.html)

[FACT] A rough performance rule of thumb for Suricata: approximately 200 Mbps per worker thread. A fully saturated 1 Gbps link requires at least 5 Suricata workers, and combined with Zeek for network metadata, a minimum of 10 CPU cores.
Source: [Hardware Recommendations for Suricata — Suricata Forum](https://forum.suricata.io/t/hardware-recommendations-for-suricata-in-a-university-network-environment-with-heavy-traffic/5019)

[FACT] High-performance Suricata configurations achieving 60 Gbps throughput have used dual Intel Xeon E5-2697 v4 processors (36 total cores), paired with Intel x710 or Mellanox MT27800 ConnectX-5 NICs configured with RSS queues and symmetric hashing.
Source: [High-Speed IDS/S Suricata Hardware Tuning — Red Piranha](https://redpiranha.net/news/High-speed-IDP/S-suricata-hardware-tuning-for-60gpbs-throughput)

### 2.4 Rule Management and False Positive Tuning

[FACT] Suricata supports multi-threaded performance, deep packet inspection, protocol decoding, and file extraction. It can act as IDS, IPS, or NSM with inline actions including drop, reset, and rate-limit.
Source: [Install Suricata IDS 2025 — OnlineHashCrack](https://www.onlinehashcrack.com/guides/tutorials/install-suricata-ids-2025-detect-threats.php)

[FACT] Production deployments require ongoing rule lifecycle management: importing community rulesets (Emerging Threats, Snort community rules), suppressing noisy signatures, validating new rules in detection-only mode before promoting to blocking mode, and reviewing rule efficacy after network changes.
Source: [Implementing IDS/IPS with Snort or Suricata — DoHost](https://dohost.us/index.php/2025/10/18/implementing-intrusion-detection-prevention-systems-ids-ips-with-snort-or-suricata/)

### 2.5 Host-Based Intrusion Detection (HIDS) and File Integrity Monitoring

[FACT] Wazuh's FIM module runs periodic scans on specified paths and monitors directories for real-time changes. It stores cryptographic checksums and other attributes of monitored files, firing alerts when a user or process creates, modifies, or deletes a monitored file.
Source: [File Integrity Monitoring — Wazuh Documentation](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/index.html)

[FACT] Wazuh FIM includes built-in support for Windows, Linux, and macOS agents and integrates with Wazuh's threat intelligence modules for enhanced malware detection and response.
Source: [Understanding FIM in Wazuh SIEM — Medium/Pradeepkumaru](https://medium.com/@pradeepkumaru.cyber/understanding-file-integrity-monitoring-fim-in-wazuh-siem-5618be559704)

---

## 3. Vulnerability Scanning: Infrastructure, Container, and Dependency

### 3.1 Infrastructure Scanning

**Tools:** Tenable Nessus Professional, OpenVAS (Greenbone), Qualys (on-premises scanner)

[FACT] OpenVAS core components: GVM Scanner (openvas-scanner), GVM Manager (gvmd), Greenbone Security Assistant web interface (GSA), PostgreSQL database, and Redis caching layer. Recommended memory allocation: at least 20–30 GB for virtual machine deployments to accommodate plugin downloads and scan data storage.
Source: [OpenVAS 2025: Enterprise Vulnerability Scanner — OnlineHashCrack](https://www.onlinehashcrack.com/guides/security-tools/openvas-2025-enterprise-vulnerability-scanner.php)

[FACT] OpenVAS 2025 features a new multi-threaded engine enabling distributed scanning and load balancing across thousands of assets, with RESTful APIs and standardized JSON/XML output for SIEM and ticketing system integration.
Source: [OpenVAS 2025: Enterprise Vulnerability Scanner — OnlineHashCrack](https://www.onlinehashcrack.com/guides/security-tools/openvas-2025-enterprise-vulnerability-scanner.php)

[FACT] Nessus uses a commercial per-asset licensing model. Nessus Professional reduces operational overhead compared to OpenVAS but requires ongoing license management and update subscription maintenance.
Source: [OpenVAS vs Nessus: Which is the Best Choice? 2025 — Beagle Security](https://beaglesecurity.com/blog/article/openvas-vs-nessus-which-is-the-best-choice-for-you-2025.html)

[FACT] Amazon Inspector supports Web-Based (cloud) deployment only; Nessus Professional supports both Web-Based and On-Premises deployment. Nessus offers broader multi-environment scanning across hybrid infrastructure; Inspector is optimized for AWS-native environments.
Source: [Amazon Inspector vs Tenable Nessus (2025) — PeerSpot](https://www.peerspot.com/products/comparisons/amazon-inspector_vs_tenable-nessus)

### 3.2 Container and Dependency Scanning

**Tools:** Trivy (Aqua Security), Grype (Anchore), Clair (Red Hat)

[FACT] Trivy is described as "the Swiss Army knife — one binary that handles vulnerability scanning, IaC misconfigurations, secrets detection, and license compliance across containers, filesystems, git repos, and Kubernetes clusters." Grype is "the sharpened blade — a focused vulnerability scanner with superior risk scoring that combines CVSS, EPSS exploit probability, and KEV catalog status."
Source: [Trivy vs. Grype: Choosing the Right Vulnerability Scanner — OpsDigest](https://opsdigest.com/digests/trivy-vs-grype-choosing-the-right-vulnerability-scanner/)

[FACT] Trivy's Kubernetes operator (trivy-operator) runs continuous scans inside clusters. Grype does not offer an equivalent in-cluster operator.
Source: [Trivy vs. Grype — OpsDigest](https://opsdigest.com/digests/trivy-vs-grype-choosing-the-right-vulnerability-scanner/)

[FACT] Both Trivy and Grype support air-gapped on-premises deployments: Grype supports efficient database updates in restricted networks; Trivy can scan tar archives of container images without Docker daemon access, enabling offline scanning.
Source: [Open-Source Container Security: Trivy, Clair, and Grype — Stakater](https://www.stakater.com/post/open-source-container-security-a-deep-dive-into-trivy-clair-and-grype)

[FACT] Both Trivy and Grype output SARIF format for GitHub and GitLab code scanning and support severity-based exit codes for build-gating in CI/CD pipelines.
Source: [Trivy vs. Grype — OpsDigest](https://opsdigest.com/digests/trivy-vs-grype-choosing-the-right-vulnerability-scanner/)

### 3.3 Scheduling and Remediation Workflows

[FACT] On-premises vulnerability scanning programs require: (1) authenticated credential management for all scanned assets, (2) scan scheduling policies to avoid production disruption, (3) integration with ticketing systems for remediation tracking, and (4) rescan-to-close workflows to verify remediation. OpenVAS's RESTful API and Nessus's API both support automated workflow integration.
Source: [OpenVAS Vulnerability Scanning Guide — Medtrigui/GitHub](https://medtrigui.github.io/vulnerability-scanning/openvas-vulnerability-scanning/)

---

## 4. Runtime Security: Container Runtime Protection

### 4.1 Tool Landscape

- **Falco** (CNCF graduate project, eBPF-based): [https://falco.org/](https://falco.org/)
- **Sysdig Secure** (commercial wrapper around Falco engine): [https://www.sysdig.com/](https://www.sysdig.com/)
- **Wazuh** (process and FIM-based runtime detection)

### 4.2 Falco Deployment

[FACT] Falco is a CNCF graduate project that uses eBPF to monitor system activity for adverse behavior at the Linux kernel level. It is deployable as a DaemonSet in Kubernetes via an official Helm chart, as a standalone container, or directly as a host daemon.
Source: [Falco — Deploy as a Container](https://falco.org/docs/setup/container/)

[FACT] Falco alerts can be forwarded to more than 50 third-party integrations including SIEMs, messaging platforms, and incident management systems.
Source: [Falco Official Site](https://falco.org/)

[FACT] Falco is used for threat detection across every major cloud platform and in large on-premises installations by organizations including big tech and startups alike.
Source: [Sysdig: How Project Falco is Strengthening Cloud Runtime Security — Techzine](https://www.techzine.eu/blogs/security/130526/sysdig-how-project-falco-is-strengthening-cloud-runtime-security/)

### 4.3 Operational Limitations of Self-Hosted Runtime Security

[FACT] Self-hosted Falco: completely free (infrastructure costs only); however, it focuses solely on runtime security events — it lacks vulnerability scanning, compliance management, or configuration management capabilities, demands security expertise for effective rule customization and tuning, and has no official vendor support unless combined with a commercial offering.
Source: [Top 6 Best Container Security Tools for Runtime Protection in 2025 — AccuKnox](https://accuknox.com/blog/best-container-security-tools)

[FACT] Scaling open-source tools like Falco across large enterprises is described as "often difficult due to lack of enterprise-grade support, SLAs, and advanced automation."
Source: [Top 5 Sysdig Alternatives for 2025 Cloud Security — AccuKnox](https://accuknox.com/comparisons/sysdig-alternatives)

### 4.4 Process Monitoring and File Integrity Monitoring

[FACT] Wazuh provides integrated host-based runtime security through: syscall-level process monitoring via auditd integration, FIM with cryptographic baseline comparison, and real-time alerting on unauthorized process execution. Coverage spans Windows, Linux, and macOS endpoints.
Source: [File Integrity Monitoring — Wazuh Documentation](https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/index.html)

---

## 5. Incident Response: Forensics Infrastructure and Chain of Custody

### 5.1 On-Premises DFIR Requirements

[FACT] Digital forensic investigations follow a strict chain of custody — a formal process for tracking how evidence is gathered and handled — allowing investigators to prove that evidence was not tampered with. Best practices include: documenting every action taken with the evidence including collection, transfer, and analysis; assigning unique identifiers to each piece of evidence; and restricting access to authorized personnel only.
Source: [What is DFIR? — IBM](https://www.ibm.com/think/topics/dfir)

[FACT] Chain of custody documentation transforms raw data into evidence that can support internal decisions, regulatory reporting, and legal proceedings.
Source: [What is DFIR? — Wiz Academy](https://www.wiz.io/academy/detection-and-response/digital-forensics-and-incident-response-dfir)

[FACT] DFIR has evolved significantly as infrastructure moved from on-premises data centers to dynamic cloud environments. Physical on-premises forensics — historically meaning physically seizing a server and imaging its hard drive — now must coexist with cloud-native evidence capture workflows for hybrid environments.
Source: [Digital Forensics and Incident Response — SearchInform](https://searchinform.com/articles/cybersecurity/analytics/digital-forensics/digital-forensics-and-incident-response/)

### 5.2 On-Premises Forensics Infrastructure Components

[FACT] On-premises DFIR infrastructure requires: dedicated evidence collection workstations with write-blocking hardware, isolated forensic analysis networks (air-gapped from production), secure evidence storage with access logging, and chain-of-custody management software. The CISA guidance on chain of custody for critical infrastructure systems specifies that documented procedures must cover collection, handling, transportation, storage, and analysis of all digital evidence.
Source: [Chain of Custody and Critical Infrastructure Systems — CISA](https://www.cisa.gov/sites/default/files/publications/cisa-insights_chain-of-custody-and-ci-systems_508.pdf)

### 5.3 Playbooks and Incident Response Tooling

[FACT] On-premises incident response requires pre-built playbooks for common scenarios (ransomware, insider threat, data exfiltration), with tooling including: memory acquisition tools (Volatility, LiME), disk imaging tools (dd, FTK Imager), network packet capture replay systems, and log aggregation pipelines that preserve evidence integrity during collection.
Source: [What is DFIR? — Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/digital-forensics-and-incident-response)

---

## 6. Threat Intelligence: Self-Managed Infrastructure

### 6.1 Threat Intelligence Platforms

**Tool:** MISP (Malware Information Sharing Platform) — [https://www.misp-project.org/](https://www.misp-project.org/)

[FACT] MISP is a complete open-source threat intelligence sharing platform deployable on-premises, in the cloud, or as SaaS. It stores IOCs in a structured manner and provides automated exports for IDS/SIEM consumption in STIX or OpenIOC formats, along with synchronization to other MISP instances.
Source: [MISP Features and Functionalities](https://www.misp-project.org/features/)

[FACT] MISP includes an automatic correlation engine that reveals relationships between attributes and indicators, handling interlinking of matching attributes as well as advanced correlation patterns including fuzzy hashing overlaps and CIDR block matching.
Source: [MISP Features and Functionalities](https://www.misp-project.org/features/)

[FACT] MISP includes default feeds from various community sources that can be enabled with a click, including aggregated community threat intelligence feeds. Feedly TI integration enables automated collection and IOC ingestion with contextual enrichment directly into MISP.
Source: [Scale Up MISP: Automatically Collect and Ingest IoCs with Feedly TI — Feedly](https://feedly.com/new-features/posts/scale-up-misp-automate-ioc-ingestion-with-rich-context-from-feedly)

### 6.2 Standards and Integration

[FACT] STIX (Structured Threat Information eXpression) and TAXII (Trusted Automated eXchange of Intelligence Information) are the widely adopted standards for sharing and transporting cyber threat intelligence. STIX provides a structured language for threat information; TAXII is the transport protocol for secure exchange of STIX-formatted data between organizations and security platforms.
Source: [Complete Guide to Threat Intelligence Feeds 2026 — CyCognito](https://www.cycognito.com/learn/threat-intelligence/threat-intelligence-feeds/)

[FACT] MISP integrates natively with Suricata and Wazuh for automated IOC-to-rule conversion, enabling threat intelligence to flow directly into network and host detection layers.
Source: [Harness the Power of Shared Threat Intelligence with MISP — Stamus Networks](https://www.stamus-networks.com/blog/harness-the-power-of-shared-threat-intelligence-with-misp)

---

## 7. Penetration Testing: Internal Red Team Infrastructure

### 7.1 Tool Landscape

[FACT] The industry-standard self-hosted red team toolkit for 2025 includes: Metasploit Framework (Rapid7, exploit development and post-exploitation automation), Cobalt Strike (commercial, C2 framework for adversary simulation), Sliver (open-source C2 with implants for macOS, Windows, Linux), and PoshC2 (Python3-based proxy-aware C2 framework).
Source: [Top Red Team Tools and C2 Frameworks for 2025 — Bishop Fox](https://bishopfox.com/blog/2025-red-team-tools-c2-frameworks-active-directory-network-exploitation)

[FACT] Metasploit Framework "provides a huge collection of pre-built exploits" and "allows users to automate pen testing tasks, develop custom exploits, and perform various post-exploit activities."
Source: [Penetration Testing Tools 2025: Top 10 Reviewed — OnlineHashCrack](https://www.onlinehashcrack.com/guides/ethical-hacking/penetration-testing-tools-2025-top-10-reviewed.php)

### 7.2 Infrastructure Requirements

[FACT] On-premises red team infrastructure requires: isolated attack simulation networks (physically or logically separated from production), C2 server infrastructure, payload staging servers, target environment replicas for pre-engagement testing, and evidence retention systems for documenting findings in a legally defensible format.
Source: [Top 25 Red Teaming Tools: Automated and Manual Platforms — FireCompass](https://firecompass.com/top-25-red-teaming-tools/)

---

## 8. Cloud-Native Comparison: Operational Burden That Disappears

### 8.1 AWS Managed Security Services

[FACT] Amazon GuardDuty is a fully managed threat detection service — "no additional service configuration is needed, and the agent-less aspect makes it very unique compared to any other third-party vendors." GuardDuty delivers AWS-native threat detection at scale "without the operational burden of building ML pipelines yourself."
Source: [Amazon GuardDuty — Deep Dive 2025 — Ewere.Tech](https://www.ewere.tech/blog/amazon-guardduty-explained-ultimate-2025-deep-dive-into-architecture-detections-playbooks/)

[FACT] AWS Security Hub uses the standardized Open Cybersecurity Schema Framework (OCSF) format, enabling seamless integration with existing SIEM, SOAR, and ticketing systems. It includes automated response workflows to streamline remediation at scale.
Source: [AWS Security Hub FAQ — AWS](https://aws.amazon.com/security-hub/faqs/)

[FACT] Amazon Inspector automatically scans EC2 instances, ECR container images, Lambda functions, and S3 for vulnerabilities. It supports both web-based deployment only; it cannot replace on-premises infrastructure scanning for non-AWS workloads.
Source: [Amazon Inspector vs Tenable Nessus (2025) — PeerSpot](https://www.peerspot.com/products/comparisons/amazon-inspector_vs_tenable-nessus)

### 8.2 Azure Managed Security Services

[FACT] Microsoft Sentinel is a cloud-native SIEM/SOAR described as "67% faster to deploy than an on-premises SIEM system."
Source: [Microsoft Sentinel vs. Microsoft Defender — DigitalXRAID](https://www.digitalxraid.com/blog/microsoft-sentinel-vs-microsoft-defender/)

[FACT] As of July 2025, many new Microsoft Sentinel customers are automatically onboarded to the Defender portal. After March 31, 2027, Microsoft Sentinel will no longer be supported in the Azure portal and will be available exclusively in the Microsoft Defender portal.
Source: [Update: New Timeline for Transitioning Sentinel Experience to Defender Portal — Microsoft Community Hub](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464)

[FACT] Microsoft Sentinel Pay-As-You-Go pricing: approximately $4.30–$5.20 per GB of ingested data depending on region. At 100 GB/day of log ingestion, this equals approximately $500/day or over $15,000/month at PAYG rates. Commitment tiers offer savings up to 52% over PAYG.
Source: [Microsoft Sentinel Pricing 2025 — UnderDefense](https://underdefense.com/industry-pricings/microsoft-sentinel-pricing/)

### 8.3 Google Cloud Security Command Center

[FACT] Google Security Command Center (SCC) Enterprise is described as "the industry's first multi-cloud risk management solution that converges cloud security and enterprise security operations capabilities, powered by Mandiant expertise and AI, delivering 120+ new capabilities."
Source: [Security Command Center Overview — Google Cloud](https://cloud.google.com/security-command-center/docs/security-command-center-overview)

[FACT] Atos's advanced SOC, powered by Google SecOps, operates 24/7 and leverages an AI-driven MDR platform with a Computer Security Incident Response Team (CSIRT) to rapidly detect and mitigate threats — as a managed service requiring no in-house SOC infrastructure.
Source: [Atos Launches Google Cloud Managed Security Services — Atos](https://atos.net/en/2025/news_2025_02_25/atos-launches-comprehensive-google-cloud-managed-security-services-portfolio-and-earns-google-cloud-security-specialization)

### 8.4 Operational Burden Comparison Summary

The table below captures what operational work exists in each model:

| Operational Domain | On-Premises | Managed K8s | Cloud-Native |
|-------------------|-------------|-------------|--------------|
| SIEM infrastructure mgmt | Full (hardware, OS, updates) | Partial (K8s ops, not hardware) | None (PaaS) |
| Rule authoring and tuning | Full (ongoing) | Full (ongoing) | Partial (vendor defaults + custom) |
| Log storage management | Full (capacity planning, tiering) | Partial | None (pay-per-GB) |
| IDS/IPS rule management | Full | Full | None (GuardDuty ML-managed) |
| Vulnerability scan scheduling | Full | Full | Automated (Inspector/SCC) |
| Runtime security agent mgmt | Full (eBPF kernel compat.) | Moderate | None (agentless options) |
| Threat intel feed management | Full (MISP admin) | Full | Partial (vendor-managed feeds) |
| Forensics evidence chain custody | Full | Full | Partial (cloud-managed logs) |
| 24/7 SOC staffing | Required | Required | Optional (MDR services available) |

---

## 9. Staffing and Cost Analysis

### 9.1 SOC Staffing by Maturity Tier

[FACT] A 24/7 on-premises SOC requires a minimum of 12 dedicated employees to account for shift coverage, vacations, sick time, and training.
Source: [The True Cost of Setting Up and Operating a 24×7 SOC — Netsurion](https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center)

[FACT] Annual SOC operating costs by maturity tier (U.S. East Coast labor rates, 5,000-user network):

| Tier | Annual Cost | Technology | Labor | FTE (est.) | Capabilities |
|------|-------------|------------|-------|------------|--------------|
| Basic | $1.5M | $300K | $1.2M | 12 FTE | Detection, limited investigation |
| Intermediate | $2.5M | $400K | $2.1M | ~15 FTE | SIEM + UEBA + network forensics |
| Advanced | $5M | $1.1M | $3.9M | ~20+ FTE | Threat hunting, AI automation, TI feeds |

Source: [The True Cost of Setting Up and Operating a 24×7 SOC — Netsurion](https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center)

[FACT] The optimal events-per-analyst-hour (EPAH) metric is 8–12, giving each analyst sufficient time to triage and escalate events effectively.
Source: [SOC Analyst Career Path and Salary Guide 2026 — Dropzone AI](https://www.dropzone.ai/resource-guide/soc-analyst-career-guide-roles-tiers-salaries-2025-edition)

[STATISTIC] Per [SANS 2025 SOC Survey](https://swimlane.com/blog/global-soc-survey-insights/): 62% of SOC professionals report their organization is not doing enough to retain top staff. 70% of SOC analysts with five years or less of experience leave within three years.
Source: [2025 SANS Detection & Response Survey — Stamus Networks](https://www.stamus-networks.com/blog/what-the-2025-sans-detection-response-survey-reveals-false-positives-alert-fatigue-are-worsening)

[STATISTIC] Per [SANS 2025 SOC Survey](https://swimlane.com/blog/global-soc-survey-insights/): 82% of SOCs operate 24/7. 85% of SOC analysts identify endpoint security tool alerts as their primary response trigger — not the SIEM itself.

### 9.2 FTE Estimates by Sub-Domain (Mid-Size ISV, 50 Enterprise Customers)

Assumptions: 500 monitored endpoints, 10–50 GB/day log volume, hybrid on-premises/Kubernetes workloads.

| Domain | On-Premises FTE | Managed K8s FTE | Cloud-Native FTE |
|--------|-----------------|-----------------|------------------|
| SIEM ops (infra + tuning) | 1.0–2.0 | 0.5–1.0 | 0.0–0.25 |
| IDS/IPS management | 0.5–1.0 | 0.5–1.0 | 0.0 |
| Vulnerability scan mgmt | 0.25–0.5 | 0.25–0.5 | 0.0–0.1 |
| Runtime security (Falco/agents) | 0.25–0.5 | 0.25–0.5 | 0.0–0.1 |
| Threat intel (MISP) | 0.25–0.5 | 0.25–0.5 | 0.0–0.25 |
| IR/forensics readiness | 0.5–1.0 | 0.5–1.0 | 0.25–0.5 |
| **Total SecOps FTE (excl. SOC analysts)** | **2.75–5.5** | **2.25–4.5** | **0.25–1.2** |

[UNVERIFIED — FTE estimates derived from industry cost benchmarks and tool documentation; no T1/T2 source provides exact per-domain FTE norms for mid-size ISV contexts. Estimates are grounded in the Netsurion SOC cost data and SANS survey staffing data cited above, cross-referenced against typical DevOps-to-SecOps ratios observed in public case studies.]

---

## 10. Difficulty Ratings by Deployment Model

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|-------------------|-------------|-------------|--------------|
| **SIEM** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Hardware, OS, Elasticsearch tuning, rule authoring, log pipeline management | K8s ops layer removed; still requires log pipeline and rule tuning | No infrastructure; rule tuning and connector config only |
| | Wazuh, Splunk Enterprise, ELK | Wazuh on K8s, Elastic Cloud on K8s (ECK) | Microsoft Sentinel, Splunk Cloud, Google SecOps |
| | Est. FTE: 1.0–2.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.0–0.25 |
| **IDS/IPS** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Dedicated hardware, SPAN/TAP infra, rule lifecycle, NIC tuning | Sensor pods, node-level network tap | GuardDuty (agentless, ML-managed) |
| | Suricata, Snort 3, Zeek | Suricata in K8s DaemonSet | AWS GuardDuty, Azure Defender for Network |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.0 |
| **Vulnerability Scanning** | Difficulty: 3/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Credential mgmt, scan scheduling, remediation workflow integration | Same as on-prem plus container registry scanning | Automated (Inspector/SCC), no scheduling required |
| | Nessus Professional, OpenVAS, Trivy | Trivy Operator, Grype in pipeline | AWS Inspector, GCP SCC, Azure Defender for Containers |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **Runtime Security** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | eBPF kernel compatibility, Falco rule tuning, agent fleet management | K8s DaemonSet deployment; eBPF kernel compat remains | Agentless CSPM options; reduced kernel compat concerns |
| | Falco, Wazuh agents, Sysdig OSS | Falco via Helm, Sysdig Secure | Sysdig SaaS, Aqua Security, Wiz Runtime |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.1 |
| **Threat Intelligence** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | MISP admin, feed curation, IOC-to-rule pipeline, storage management | Same tooling, K8s deployment adds complexity | Vendor-managed feeds; custom TI possible via API |
| | MISP, OpenCTI, commercial TI feeds | MISP on K8s | AWS GuardDuty TI, Microsoft Threat Intelligence |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.25–0.5 | Est. FTE: 0.0–0.25 |
| **IR / Forensics** | Difficulty: 5/5 | Difficulty: 4/5 | Difficulty: 3/5 |
| | Full evidence chain-of-custody infra, write-blockers, isolated forensic networks, playbook management | Same tooling; K8s adds ephemeral workload complexity | Cloud-managed logs reduce some burden; IR playbooks still required |
| | Volatility, FTK Imager, GRR Rapid Response | Same tools, container-adapted | AWS CloudTrail, Azure Monitor, GCP Cloud Logging |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 |

---

## Key Takeaways

- **On-premises security operations demand sustained, specialized staffing.** A 24/7 on-premises SOC requires a minimum of 12 dedicated professionals at an annual cost ranging from $1.5M (basic detection) to $5M (advanced threat hunting), per [Netsurion's SOC cost analysis](https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center). ISVs should not treat this as a one-time deployment cost.

- **Alert fatigue is the dominant on-premises operational challenge.** The [2025 SANS Detection & Response Survey](https://www.stamus-networks.com/blog/what-the-2025-sans-detection-response-survey-reveals-false-positives-alert-fatigue-are-worsening) reports 73% of organizations identify false positives as their top detection challenge, with "very frequent" false positives rising from 13% to 20% year-over-year. Self-hosted SIEMs and IDS/IPS systems require continuous rule tuning that cloud-native managed services largely automate.

- **Cloud-native security services eliminate infrastructure operational burden but not analytical burden.** AWS GuardDuty, Microsoft Sentinel, and GCP SCC eliminate hardware management, rule-feed updates, and capacity planning — but still require detection engineers to author custom detection logic, integrate custom data sources, and manage incident response playbooks.

- **Container-era security requires a new on-premises toolchain.** Falco (runtime), Trivy/Grype (image scanning), and MISP (threat intelligence) represent the minimum viable self-hosted container security stack, each requiring ongoing maintenance. eBPF kernel compatibility is an additional on-premises constraint with no equivalent in cloud-native deployments.

- **Air-gapped and sovereignty-constrained ISVs have no viable cloud-native alternative.** For ISV deployments serving customers with regulatory data-residency requirements or air-gap mandates, the entire on-premises security operations stack must be planned, staffed, and sustained internally. Cloud-native managed security services are unavailable by definition in these environments.

---

## Related — Out of Scope

The following topics emerged during research but are covered by other agents in this research plan:

- IAM, RBAC, and authentication controls: See [F46: IAM and Authentication]
- Encryption, secrets management, and key management (HSM, Vault): See [F47: Encryption and Secrets]
- Compliance frameworks and audit evidence collection (SOC 2, ISO 27001, HIPAA): See [F67: Compliance Frameworks]
- Network segmentation, firewall policy management, and zero-trust networking architecture: adjacent to F71 scope but not covered here

---

## Sources

| # | Source | URL |
|---|--------|-----|
| 1 | Wazuh SIEM Platform | https://wazuh.com/platform/siem/ |
| 2 | Wazuh Quickstart Documentation | https://documentation.wazuh.com/current/quickstart.html |
| 3 | Wazuh Installation Guide — Server | https://documentation.wazuh.com/current/installation-guide/wazuh-server/index.html |
| 4 | Wazuh File Integrity Monitoring | https://documentation.wazuh.com/current/user-manual/capabilities/file-integrity/index.html |
| 5 | Splunk Reference Hardware | https://docs.splunk.com/Documentation/Splunk/9.4.2/Capacity/Referencehardware |
| 6 | SIEM Hot Storage Requirements — Ertugrul Akbas | https://drertugrulakbas.medium.com/siem-hot-storage-requirements-accuracy-analysis-c412681155a9 |
| 7 | SIEM Data Retention Best Practices — ClearNetwork | https://clearnetwork.com/siem-data-retention-best-practices-for-effective-threat-detection/ |
| 8 | SIEM Sizing — LinkedIn/Kerem Ozturk | https://www.linkedin.com/pulse/how-correctly-size-your-siem-investment-kerem-ozturk |
| 9 | Using the ELK Stack for SIEM — Logz.io | https://logz.io/blog/elk-siem/ |
| 10 | SANS 2025 SOC Survey — Swimlane | https://swimlane.com/blog/global-soc-survey-insights/ |
| 11 | 2025 SANS Detection & Response Survey — Stamus Networks | https://www.stamus-networks.com/blog/what-the-2025-sans-detection-response-survey-reveals-false-positives-alert-fatigue-are-worsening |
| 12 | SANS SOC Survey 2025 — Tines | https://www.tines.com/blog/sans-soc-survey-2025/ |
| 13 | Implementing IDS/IPS with Snort or Suricata — DoHost | https://dohost.us/index.php/2025/10/18/implementing-intrusion-detection-prevention-systems-ids-ips-with-snort-or-suricata/ |
| 14 | Suricata vs Snort — Stamus Networks | https://www.stamus-networks.com/suricata-vs-snort |
| 15 | Hardware Requirements — Security Onion Documentation 2.4 | https://docs.securityonion.net/en/2.4/hardware.html |
| 16 | Suricata Forum — Hardware Recommendations | https://forum.suricata.io/t/hardware-recommendations-for-suricata-in-a-university-network-environment-with-heavy-traffic/5019 |
| 17 | High-Speed Suricata Hardware Tuning 60Gbps — Red Piranha | https://redpiranha.net/news/High-speed-IDP/S-suricata-hardware-tuning-for-60gpbs-throughput |
| 18 | Suricata High Performance Configuration | https://docs.suricata.io/en/latest/performance/high-performance-config.html |
| 19 | OpenVAS 2025: Enterprise Vulnerability Scanner | https://www.onlinehashcrack.com/guides/security-tools/openvas-2025-enterprise-vulnerability-scanner.php |
| 20 | OpenVAS vs Nessus 2025 — Beagle Security | https://beaglesecurity.com/blog/article/openvas-vs-nessus-which-is-the-best-choice-for-you-2025.html |
| 21 | OpenVAS Vulnerability Scanning Guide | https://medtrigui.github.io/vulnerability-scanning/openvas-vulnerability-scanning/ |
| 22 | Amazon Inspector vs Tenable Nessus 2025 — PeerSpot | https://www.peerspot.com/products/comparisons/amazon-inspector_vs_tenable-nessus |
| 23 | Trivy vs. Grype — OpsDigest | https://opsdigest.com/digests/trivy-vs-grype-choosing-the-right-vulnerability-scanner/ |
| 24 | Open-Source Container Security: Trivy, Clair, Grype — Stakater | https://www.stakater.com/post/open-source-container-security-a-deep-dive-into-trivy-clair-and-grype |
| 25 | Falco Official Documentation | https://falco.org/docs/setup/container/ |
| 26 | Falco — Sysdig | https://www.sysdig.com/opensource/falco |
| 27 | Sysdig: How Falco Strengthens Cloud Runtime Security — Techzine | https://www.techzine.eu/blogs/security/130526/sysdig-how-project-falco-is-strengthening-cloud-runtime-security/ |
| 28 | Top Container Security Tools Runtime Protection 2025 — AccuKnox | https://accuknox.com/blog/best-container-security-tools |
| 29 | Top 5 Sysdig Alternatives 2025 — AccuKnox | https://accuknox.com/comparisons/sysdig-alternatives |
| 30 | What is DFIR — IBM | https://www.ibm.com/think/topics/dfir |
| 31 | What is DFIR — Wiz Academy | https://www.wiz.io/academy/detection-and-response/digital-forensics-and-incident-response-dfir |
| 32 | Digital Forensics and Incident Response — SearchInform | https://searchinform.com/articles/cybersecurity/analytics/digital-forensics/digital-forensics-and-incident-response/ |
| 33 | What is DFIR — Palo Alto Networks | https://www.paloaltonetworks.com/cyberpedia/digital-forensics-and-incident-response |
| 34 | Chain of Custody and Critical Infrastructure — CISA | https://www.cisa.gov/sites/default/files/publications/cisa-insights_chain-of-custody-and-ci-systems_508.pdf |
| 35 | MISP Features and Functionalities | https://www.misp-project.org/features/ |
| 36 | Scale Up MISP with Feedly TI — Feedly | https://feedly.com/new-features/posts/scale-up-misp-automate-ioc-ingestion-with-rich-context-from-feedly |
| 37 | Complete Guide to Threat Intelligence Feeds 2026 — CyCognito | https://www.cycognito.com/learn/threat-intelligence/threat-intelligence-feeds/ |
| 38 | Harness Shared Threat Intelligence with MISP — Stamus Networks | https://www.stamus-networks.com/blog/harness-the-power-of-shared-threat-intelligence-with-misp |
| 39 | Top Red Team Tools and C2 Frameworks 2025 — Bishop Fox | https://bishopfox.com/blog/2025-red-team-tools-c2-frameworks-active-directory-network-exploitation |
| 40 | Penetration Testing Tools 2025 — OnlineHashCrack | https://www.onlinehashcrack.com/guides/ethical-hacking/penetration-testing-tools-2025-top-10-reviewed.php |
| 41 | Top 25 Red Teaming Tools — FireCompass | https://firecompass.com/top-25-red-teaming-tools/ |
| 42 | Amazon GuardDuty Deep Dive 2025 — Ewere.Tech | https://www.ewere.tech/blog/amazon-guardduty-explained-ultimate-2025-deep-dive-into-architecture-detections-playbooks/ |
| 43 | AWS Security Hub FAQ | https://aws.amazon.com/security-hub/faqs/ |
| 44 | Microsoft Sentinel vs Microsoft Defender — DigitalXRAID | https://www.digitalxraid.com/blog/microsoft-sentinel-vs-microsoft-defender/ |
| 45 | Microsoft Sentinel Defender Portal Migration — Microsoft Community Hub | https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464 |
| 46 | Microsoft Sentinel Pricing 2025 — UnderDefense | https://underdefense.com/industry-pricings/microsoft-sentinel-pricing/ |
| 47 | Google Security Command Center Overview | https://cloud.google.com/security-command-center/docs/security-command-center-overview |
| 48 | Atos Google Cloud Managed Security Services — Atos | https://atos.net/en/2025/news_2025_02_25/atos-launches-comprehensive-google-cloud-managed-security-services-portfolio-and-earns-google-cloud-security-specialization |
| 49 | The True Cost of a 24×7 SOC — Netsurion | https://www.netsurion.com/articles/true-cost-of-setting-up-and-operating-security-operations-center |
| 50 | SOC Analyst Career Guide 2026 — Dropzone AI | https://www.dropzone.ai/resource-guide/soc-analyst-career-guide-roles-tiers-salaries-2025-edition |
| 51 | Understanding FIM in Wazuh SIEM — Medium/Pradeepkumaru | https://medium.com/@pradeepkumaru.cyber/understanding-file-integrity-monitoring-fim-in-wazuh-siem-5618be559704 |
| 52 | 2025 SANS Detection & Response Survey — Stamus Networks (5 Trends) | https://www.stamus-networks.com/blog/2025-sans-detection-response-survey-5-trends-you-cant-ignore |
