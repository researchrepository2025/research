# Agentic AI and the SaaS ISV On-Premises Deployment Lifecycle

**A Strategic Assessment for ISV Leadership**

**Research Date:** March 2026
**Corpus:** 80 research agents (F01-F80), 10 wave syntheses (S01-S10), 6 cross-domain integrations (S11-S16), 6 exhibits (S17-S22), 1 comparison matrix (S23)
**Total Research Volume:** ~371,000 words across 97 files with 7,694 inline citation URLs

**Audience:** This document is written for ISV engineering leaders, product executives, and corporate strategy teams evaluating whether to invest in on-premises deployment capability. It assumes familiarity with SaaS business metrics (ACV, gross margin, customer lifetime value), Kubernetes fundamentals (Helm, operators, CRDs), and cloud infrastructure concepts (managed services, observability, CI/CD). Technical details are provided where they materially affect the economic or strategic analysis; purely implementation-level details are left to the referenced exhibits and underlying research files.

---

## Chapter 1: Executive Summary

The question this research addresses is whether agentic AI changes the fundamental economics of ISV on-premises deployment -- and if so, how an ISV should act on that change. The answer, drawn from 80 primary research agents covering 10 investigative waves, is a qualified yes with a structural paradox at its center.

**The paradox:** AI simultaneously makes on-premises deployment more feasible and less attractive. It compresses support costs by [40-60% for diagnostic workloads](https://komodor.com/platform/klaudia-ai-powered-troubleshooting/), enables [distributed agents with 1,000:1 to 10,000:1 data reduction](https://mlcommons.org/2025/09/small-llm-inference-5-1/) that create competitive moats unavailable to open-source self-hosters, and narrows the gap between on-prem and SaaS unit economics from 2-3x to 1.2-1.5x. But it also accelerates the cloud ecosystem advantage through five compounding layers -- data concentration, tooling maturity, financial incentives, provider investment, and iteration velocity -- with [marketplace transactions hitting $30 billion in 2024](https://www.businesswire.com/news/home/20251006925215/en/Omdia-Hyperscaler-Cloud-Marketplace-Sales-to-Hit-$163-Billion-by-2030), [model providers carrying $80 billion+ in cloud spending commitments](https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-set-to-pay-cloud-partners-80-billion-through-2029/), and the [METR autonomous task horizon doubling every 89-131 days](https://metr.org/blog/2026-1-29-time-horizon-1-1/) with gains accruing asymmetrically to cloud -- that widen the gap in product development speed by [30-35% for cloud-first engineering versus 0-10% for on-prem brownfield work](https://softwareengineeringproductivity.stanford.edu/ai-impact).

This paradox does not resolve into a single recommendation. It resolves into a decision framework that segments ISVs by the nature of their demand: regulatory-gated versus preference-driven. For ISVs whose customers legally cannot use SaaS -- defense contractors bound by ITAR, healthcare organizations with HIPAA on-premises requirements, financial institutions under EU data sovereignty mandates, government agencies at IL4-IL6 classification levels -- on-premises deployment is not optional. The revenue is binary: accessible only through on-prem capability. For these ISVs, Model C (Hybrid Split-Plane) with embedded diagnostic agents is economically rational today, [breaking even at 3-4 customers at 25% ACV premium](https://www.getmonetizely.com/articles/the-break-even-analysis-understanding-pricing-thresholds-in-saas). For ISVs whose on-prem demand is purely preference-driven -- customers who prefer on-prem for cost optimization, control, or philosophical reasons but could use SaaS -- the [cloud marketplace channel ($163B projected by 2030](https://www.businesswire.com/news/home/20251006925215/en/Omdia-Hyperscaler-Cloud-Marketplace-Sales-to-Hit-$163-Billion-by-2030) with a [27-point higher win rate](https://tacklecloud.com/resources/state-of-cloud-marketplaces-report-2024/)) is the dominant strategy.

**Five master findings emerge from the cross-domain integration of all 10 waves:**

1. **The lifecycle cost curve is front-loaded and model-dependent.** Total 3-year cost per on-prem customer ranges from $34K (Model C with AI agents at 50+ customer scale) to $340K (Model B without AI agents at fewer than 10 customers) -- a 10x range. The primary driver is deployment model choice (Model C versus Model B), the secondary driver is customer count (amortization of fixed investment), and the tertiary driver is AI automation maturity. The implication is that the ISV's first architectural decision -- which deployment model to implement -- has 4-5x more impact on unit economics than the AI automation strategy.

2. **AI's impact is phase-asymmetric.** Phase 1 (one-time product refactoring): 10-20% net compression -- modest because the highest-difficulty architectural tasks are precisely where [experienced developers using AI on complex codebases took 19% longer](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Phase 2 (per-customer deployment): [80-90% MTTR reduction on recognized failure patterns](https://www.globenewswire.com/news-release/2025/11/05/3181574/0/en/Komodor-Introduces-Autonomous-Self-Healing-Capabilities-for-Cloud-Native-Infrastructure-and-Operations.html) for post-deployment diagnosis, but near-zero reduction in per-customer deployment cost because the binding constraints are customer coordination and environment-specific adaptation. Phase 3 (ongoing support): [40-60% compression for diagnostic workloads](https://komodor.com/platform/klaudia-ai-powered-troubleshooting/), which transforms the support cost curve from linear to sub-linear. The strategic implication is that AI investment should be concentrated in Phase 3, where the recurring cost savings compound over the customer lifetime.

3. **Model C dominates Model B across every dimension except architectural simplicity and air-gap compatibility.** This finding was independently confirmed across all 10 research waves. Model C achieves 30-40% lower fixed investment ($235K-$550K versus $350K-$850K), 1.5-2x lower per-customer support cost, [2x better AI diagnostic effectiveness (70-90% MTTR reduction versus 30-50% for Model B](https://www.globenewswire.com/news-release/2025/11/05/3181574/0/en/Komodor-Introduces-Autonomous-Self-Healing-Capabilities-for-Cloud-Native-Infrastructure-and-Operations.html) due to real-time telemetry versus stale support bundles), sub-linear support scaling (versus linear for Model B), and a structural competitive moat via aggregate telemetry that no self-hosted deployment can replicate. Model B is justified only for air-gapped customers whose compliance frameworks explicitly prohibit any outbound connectivity.

4. **The distributed agent runtime is the strategic differentiator, not a cost optimization.** ISV-authored agents executing in customer Kubernetes environments via [CRD-based operator dispatch](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), processing customer data locally, and returning only structured results create a four-mechanism moat: (a) aggregate telemetry advantage across N customer environments that compounds with count and time, (b) operational AI trained on real customer incidents that outperforms generic models in the ISV's domain, (c) trust infrastructure ([SLSA Level 2+ provenance](https://slsa.dev/spec/v1.2/) + [Cosign-signed images](https://docs.sigstore.dev/cosign/signing/overview/) + [Kyverno admission policies](https://kyverno.io/docs/policy-types/cluster-policy/verify-images/) + OPA) that creates switching cost once integrated into customer security workflows, and (d) regulatory documentation (per-customer BAAs, anonymization assessments) that is ISV-specific and non-portable. The net annual economic impact at 50 customers is $410K-$2.3M, translating to $2.9M-$16M in enterprise value at 7x revenue multiples.

5. **The investment window is 12-24 months.** Three converging factors define a March 2026 - March 2028 optimal window. First, open-weight model capability is at its peak convergence: the [MMLU gap between open and proprietary models collapsed from 17.5 to 0.3 points](https://arxiv.org/abs/2412.04315) in one year, enabling viable on-prem LLM inference today. Second, CNCF agentic tooling ([kagent](https://kagent.dev/), [Agent Sandbox](https://opensource.googleblog.com/2025/11/unleashing-autonomous-ai-agents-why-kubernetes-needs-a-new-standard-for-agent-execution.html)) is maturing from Sandbox/alpha toward production readiness on a 12-18 month trajectory. Third, cloud ecosystem compounding has not yet made the gap unbridgeable -- but every month of delay adds to the [30-35% productivity gap](https://softwareengineeringproductivity.stanford.edu/ai-impact), the [$470B+ in committed cloud provider spend](https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-set-to-pay-cloud-partners-80-billion-through-2029/), and the [marketplace channel advantage](https://tacklecloud.com/resources/state-of-cloud-marketplaces-report-2024/). ISVs that delay beyond 2027-2028 face a materially harder engineering challenge with fewer countervailing forces to offset the cloud advantage.

---

## Chapter 2: ISV Context -- Why This Is Not Enterprise Repatriation

This research is scoped to a specific actor: the SaaS ISV that currently deploys its product exclusively on cloud infrastructure and faces market demand to offer an on-premises deployment option. This framing must be carefully distinguished from the enterprise cloud repatriation narrative, which concerns organizations moving their own workloads between environments. The ISV problem is structurally different in ways that change the economics, architecture, and AI impact calculus.

### The N-Customer Heterogeneity Problem

An enterprise repatriating a workload controls its own infrastructure: one Kubernetes distribution, one storage class, one network topology, one security policy. The ISV deploying to N customers must support N independent infrastructure environments, each with different configurations, constraints, and failure modes.

Wave 4 research quantified this heterogeneity. The cross-distribution permutation space spans [81,920 combinations](https://kubernetes-csi.github.io/docs/drivers.html) across 8 major Kubernetes distributions (OpenShift, RKE2, EKS Anywhere, GKE On-Prem, Tanzu, vanilla kubeadm, k3s, MicroK8s), 139 CSI (Container Storage Interface) drivers, and 5 CNI (Container Networking Interface) plugins. [Replicated's validation matrix](https://www.replicated.com/) has documented 65,981+ tested combinations, yet ISVs still encounter customer environments that fall outside the validated matrix.

The two dominant enterprise Kubernetes distributions both break ISV defaults in ways that require per-customer adaptation. OpenShift, used by approximately 50% of Fortune 100 companies, enforces a `restricted-v2` Security Context Constraint that blocks privileged containers -- a requirement that many ISV Helm charts violate by default. RKE2, used by 22% of organizations with 5,000+ employees, applies CIS benchmark defaults that restrict network policies and pod security contexts. These are not edge cases; they are the primary deployment targets for enterprise ISVs.

### The Observability Gap

In SaaS, the ISV owns its infrastructure and has unrestricted access to application metrics, system logs, distributed traces, database query performance, and customer usage data. This observability enables proactive issue detection, automated remediation, and data-driven product improvement. The ISV's operations team operates in a unilateral model: when an issue is detected, the ISV can investigate and resolve it without customer involvement.

In on-prem Model B, this observability disappears entirely. The ISV has zero access to the customer's infrastructure. Every diagnostic action follows a bilateral model: the ISV requests information, the customer's infrastructure team gathers it (often with internal approval processes), the customer redacts sensitive data, the customer transmits the artifact, and the ISV analyzes the result. Wave 5 research documented that each step in this bilateral chain introduces hours to days of elapsed time, and a typical triage cycle requires 3-5 round trips.

The economic consequence is severe. Wave 5 established that this bilateral support model is the structural root cause of on-prem support costing [18-22% of ACV annually](https://www.connsulting.io/blog/the-on-prem-revenue-trap) -- 2.9x to 5.5x the [SaaS baseline of approximately 5-10% of revenue](https://livechatai.com/blog/customer-support-cost-benchmarks). At $200K ACV, this translates to $36K-$44K per customer per year in support cost alone, compared to approximately $16K for an equivalent SaaS customer. This support cost multiplier is the single largest economic headwind for on-prem deployment and the primary target for AI intervention.

### The Enterprise Repatriation Confusion

A significant body of CIO survey data suggests that cloud repatriation is accelerating: [86% of CIOs report plans for some form of workload repatriation](https://www.citrix.com/blogs/cloud-repatriation-trends/), and [41% of organizations have started repatriating data from cloud to on-premises](https://www.businessresearchinsights.com/market-reports/isv-market-122324). These headlines create pressure on ISV leadership to invest in on-prem deployment capability. However, the ISV problem is categorically different from the enterprise repatriation problem in three ways that the CIO survey data obscures.

First, the enterprise repatriating a workload is moving its own application from one environment to another. The application code does not change; only the infrastructure changes. The ISV offering on-prem deployment must make its product run on infrastructure it does not control, has never tested against, and cannot observe in production. The engineering challenge is fundamentally different.

Second, the enterprise controls the timeline: it can repatriate at its own pace, testing, validating, and rolling back as needed. The ISV must support N customers deploying simultaneously on N different infrastructure configurations, each with their own timeline, change control process, and escalation path.

Third, the enterprise captures the direct economic benefit of repatriation (lower infrastructure cost, improved performance, regulatory compliance). The ISV captures an indirect benefit (access to revenue from customers who require on-prem) while bearing the direct cost (engineering investment, support staffing, operational complexity). The ISV's incentive structure is opposite to the enterprise's: the ISV would prefer all customers use SaaS, but some customers cannot.

This distinction matters because it changes the decision calculus. The ISV is not evaluating whether on-prem is better than cloud (it is not, for the ISV). The ISV is evaluating whether the revenue accessible only through on-prem capability exceeds the incremental cost of providing that capability. This is a marginal economics question, not an architecture question.

### The Managed Service Replacement Surface

The SaaS product relies on AWS managed services that abstract away infrastructure complexity. RDS manages database provisioning, failover, backups, and patching. SQS and SNS provide message queuing and pub/sub without broker management. S3 provides object storage with automatic lifecycle policies. Lambda provides serverless compute without server management. Cognito provides identity federation without SAML/OIDC plumbing. CloudWatch provides observability without log pipeline engineering. Secrets Manager provides secrets rotation without key hierarchy management.

None of these services exist in customer environments. Wave 1 research mapped [12 infrastructure domains requiring replacement](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/core-services.html), with difficulty ratings ranging from 1 (basic Kubernetes operator installation) to 5 (replicating [DynamoDB's serverless auto-scaling model](https://seventhstate.io/rabbitmq-vs-sqs/), SNS+SQS FIFO ordered fan-out semantics, or Lambda@Edge compute at the network edge). The difficulty distribution is heavily skewed: 8 of 12 domains have floor difficulty at 1-2 (operator installation is straightforward) but ceiling difficulty at 4-5 (replicating AWS-proprietary features requires architectural redesign, not configuration mapping).

The licensing landscape has shifted dramatically since 2023, creating legal review gates that the ISV cannot bypass. [MinIO's community edition repository was archived as read-only in February 2026](https://faun.dev/c/news/devopslinks/minio-ends-community-development-positions-aistor-as-the-future/), with all development moving to the commercially licensed AIStor product. [HashiCorp Vault adopted BSL 1.1 in August 2023](https://www.infoq.com/news/2023/08/hashicorp-adopts-bsl/), prohibiting competitive use. [ScyllaDB moved to a source-available license in April 2025](https://www.scylladb.com/2025/04/08/announcing-scylladb-2025-1/), imposing 10TB and 50 vCPU limits without a commercial agreement. [MongoDB Server operates under SSPL v1.0](https://www.mongodb.com/legal/licensing/server-side-public-license), which effectively prohibits ISV redistribution of the Community Edition. These are not theoretical risks -- they are blocking dependencies that require commercial license negotiation before the ISV can ship a product.

The ISV-safe tier consists of Apache 2.0-licensed operators that can be freely bundled: [Percona Operators](https://www.percona.com/software/percona-operators) for PostgreSQL and MongoDB, [CloudNativePG (CNCF Sandbox)](https://www.cncf.io/projects/cloudnativepg/), [External Secrets Operator](https://external-secrets.io/), [KEDA (CNCF Graduated)](https://keda.sh/), [Knative (CNCF Graduated)](https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/), and [CoreDNS (CNCF Graduated)](https://www.cncf.io/projects/coredns/). Building exclusively on Apache 2.0 components is feasible but may sacrifice features available only in commercially licensed alternatives.

---

## Chapter 3: Framework -- Three Deployment Models, Three Lifecycle Phases

### Three Deployment Models

**Model A (Cloud SaaS)** is the status quo. The ISV operates all infrastructure in its own cloud accounts. Customer data resides in the ISV's cloud environment. The ISV controls release cycles, infrastructure scaling, and operational monitoring. Gross margins typically range from [75-85%](https://softwareequity.com/blog/gross-margin-saas/). This is the baseline against which Models B and C are evaluated -- not because it is under consideration for change, but because the ISV must understand the economic delta of adding on-prem capability.

**Model B (Full On-Premises)** places the ISV's entire product in the customer's infrastructure. The ISV ships containerized software (typically via Helm charts and OCI images) and the customer deploys it on their Kubernetes cluster. The ISV has no infrastructure access. All support is bilateral. The ISV controls the software artifact; the customer controls the runtime environment. This model satisfies the strictest data sovereignty requirements, including air-gapped environments, but creates the highest support cost and the lowest ISV observability.

**[Model C (Hybrid Split-Plane)](https://medium.com/bcgontech/latest-trends-in-saas-deployment-models-moving-towards-multi-tenancy-and-split-plane-7110650becdc)** is the architecturally novel model that emerged as the dominant recommendation across all 10 research waves. The ISV retains a cloud-hosted control plane -- [control-plane services representing 50-70% of total microservice count](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/core-services.html) including management UI, analytics dashboards, identity federation, AI model inference, observability aggregation, and fleet management -- while deploying a thin data plane to customer infrastructure. The data plane handles customer-data-touching workloads: data processing, local computation, application logic that must execute within the customer's security boundary. An outbound-only agent connection from the customer cluster to the ISV cloud provides the control-plane communication channel. This connection is initiated from inside the customer's network (outbound only, satisfying most firewall policies), carries control-plane commands and telemetry, and does not require the ISV to initiate inbound connections to the customer.

Wave 3 research validated Model C's technical feasibility. The split-plane architecture follows a four-phase deployment sequence: (1) ISV provisions a cloud tenant for the customer's control plane, (2) customer installs an outbound agent that establishes the control-plane channel, (3) data plane Helm charts deploy to the customer cluster, (4) connectivity validation confirms cross-plane communication. The cross-plane communication layer is rated Difficulty 4 -- not because the individual components are immature, but because the composition of mTLS, gRPC streaming, connection resilience, and split-DNS is novel for most ISV engineering teams, and [AI network configuration correctness is only ~24%](https://arxiv.org/abs/2506.03231).

### Three Lifecycle Phases

**Phase 1 (Refactoring)** is a one-time fixed investment to make the SaaS product deployable on customer Kubernetes infrastructure. This includes replacing managed service dependencies with Kubernetes-native operators, implementing cross-distribution compatibility (OpenShift SCC, RKE2 CIS defaults, CSI driver abstraction), building a portable abstraction layer for dual-target deployment, and (for Model C) engineering the cross-plane communication channel. Fixed cost: $235K-$550K (Model C), $350K-$850K (Model B). The higher Model B cost reflects the larger service replacement scope (12 domains versus 5-7 for Model C).

**Phase 2 (Customer Deployment)** is the per-customer variable cost of deploying the refactored product into each new customer's environment. This includes prerequisite validation (does the customer's cluster meet minimum requirements?), Helm chart installation and configuration, cross-plane connectivity setup (Model C only), post-deployment validation and smoke testing, and customer coordination overhead (scheduling, access grants, change control). Per-customer cost: $8K-$18.5K (Model C), $6.5K-$15.5K (Model B). Note the counterintuitive result: Model C is more expensive per customer in Phase 2 due to the cross-plane connectivity setup, but this one-time investment creates the observability channel that makes Phase 3 dramatically cheaper.

**Phase 3 (Ongoing Support)** is the recurring annual cost of maintaining deployed customers. This includes reactive diagnostic triage (troubleshooting customer-reported issues), proactive health monitoring (detecting issues before customer impact), version fragmentation management (supporting N product versions across M environment configurations), upgrade orchestration (planning, executing, and validating product upgrades in customer environments), customer coordination (all human interactions around the above), and optionally, agent infrastructure cost (for ISVs deploying distributed diagnostic agents). Annual per-customer cost: $5K-$29K (Model C with AI), $9K-$46K (Model B with AI), $18K-$92K (Model B without AI). Phase 3 is the phase where the deployment model choice and AI investment have the most compounding impact.

---

## Chapter 4: Phase 1 Findings -- AI-Assisted Refactoring

Phase 1 is the one-time fixed investment that must be amortized across the on-prem customer base. The smaller this investment and the faster it completes, the sooner the ISV reaches break-even. AI's role in Phase 1 is to compress both the cost and duration -- and the research found that it does so, but modestly: 10-20% net compression. This modest figure reflects a structural anti-correlation between AI capability and task difficulty that recurs across every domain studied.

### The Anti-Correlation Pattern

Across all 12 managed service replacement domains (Wave 1) and all 7 AI capability assessments (Wave 2), the research found a consistent pattern: AI is most effective on the easiest tasks and least effective on the hardest tasks. This is not coincidental -- it reflects the distribution of training data. Mechanical SDK rewrites (renaming boto3 calls, swapping connection strings, translating consumer group patterns) are syntactically regular and well-represented in training data. Architectural decisions (choosing between Percona and CloudNativePG, designing N-customer identity federation, sizing Kafka partitions for customer-specific data volumes) are bespoke and ISV-specific.

The concrete evidence:

**High AI leverage (Difficulty 1-2 tasks):** The boto3 `endpoint_url` pattern covers approximately 80% of S3 refactoring in a grep-and-replace operation (F03). KCL `IRecordProcessor`-to-Kafka consumer group translation follows a bounded pattern (F05). IAM token code removal and connection string replacement are mechanical (F01). Test suite generation for behavioral equivalence validation is well-suited to LLM assistance (F02). [Airbnb migrated 3,500 test files in 6 weeks](https://airbnb.tech/uncategorized/accelerating-large-scale-test-migration-with-llms/) using LLM-assisted refactoring versus an estimated 1.5 years manually (F08). [Google reported 74.45% of new code as LLM-generated](https://arxiv.org/abs/2504.09691) during a major migration, estimating approximately 50% time savings (F13). Salesforce compressed a 2-year migration timeline to 4 months using AI-assisted code transformation (F15).

**Near-zero AI leverage (Difficulty 4-5 tasks):** Partition count and retention sizing decisions for [Kafka via Strimzi](https://strimzi.io/docs/operators/latest/deploying) require understanding the customer's data volume, throughput patterns, and consumer topology (F05). Glacier-to-on-prem tiering strategy design has no Kubernetes-native equivalent and requires architectural invention (F03). N-customer identity federation architecture -- deciding between centralized [Keycloak](https://www.keycloak.org/), per-customer Zitadel instances, or [SPIFFE/SPIRE](https://spiffe.io/) workload identity -- requires domain-specific judgment about tenant isolation, compliance requirements, and operational complexity (F06). [OTel Collector fanout](https://www.cncf.io/blog/2025/12/16/how-to-build-a-cost-effective-observability-platform-with-opentelemetry/) pipeline design for the ISV observability dilemma -- routing product-health metrics to the ISV cloud while keeping customer data local -- is a novel architecture that no training data describes (F10). Storage class selection across heterogeneous customer hardware requires per-environment assessment that cannot be generalized (F01, F02, F04).

The net result: approximately 50% of Phase 1 engineering hours are on tasks where AI provides 40-60% productivity gain (mechanical refactoring), and 50% are on tasks where AI provides 0-5% gain (architectural decisions). The weighted average is 10-20% net compression. At $235K-$550K Phase 1 cost (Model C), this saves $24K-$110K -- meaningful but not transformative.

### The Licensing Clock

Licensing negotiations for commercially licensed dependencies (MinIO AIStor, ScyllaDB commercial, MongoDB Enterprise, or their Apache 2.0 alternatives) add 2-6 months of calendar time to Phase 1 that no AI tool can compress. These negotiations involve legal review, commercial terms, volume pricing, and sometimes architectural concessions (e.g., accepting MinIO's AIStor license terms versus migrating to SeaweedFS or Ceph RGW). The research found that licensing is often the critical path for Phase 1 duration even when engineering work completes faster.

The recommended approach: begin licensing evaluation in Phase 1 month 1 and run it in parallel with engineering work. Adopt an Apache 2.0-only dependency policy where feasible ([ESO](https://external-secrets.io/) instead of Vault, NATS instead of commercial messaging, [Strimzi](https://strimzi.io/) for Kafka, [CoreDNS](https://www.cncf.io/projects/coredns/), [KEDA](https://keda.sh/)). Where commercial dependencies are unavoidable, begin negotiation immediately.

### AI Refactoring: What Works and What Does Not

The research documented specific AI refactoring tools and their measured effectiveness across ISV-relevant tasks:

**Configuration generation** shows the most dramatic improvement trajectory. IaC generation for Helm values files starts at 27% baseline accuracy, improves to 75.3% with RAG augmentation (providing Kubernetes documentation and Helm chart specifications as context), and reaches [94% accuracy by the third iterative refinement](https://arxiv.org/html/2512.14792v1). This trajectory suggests that AI-assisted Helm configuration is viable today with human-in-the-loop validation, and may be fully automated within 12-18 months as models improve.

**Test migration** delivers the largest documented productivity gains. [Airbnb migrated 3,500 test files in 6 weeks](https://airbnb.tech/uncategorized/accelerating-large-scale-test-migration-with-llms/) using LLM-assisted refactoring versus an estimated 1.5 years manually -- a 13x acceleration. [Google reported 74.45% of new code as LLM-generated](https://arxiv.org/abs/2504.09691) during a major migration, estimating approximately 50% time savings. Salesforce compressed a 2-year migration timeline to 4 months using AI-assisted code transformation. These case studies share a common pattern: the tasks being automated are syntactically regular, involve well-defined input/output contracts, and have clear success criteria (tests pass or fail).

**Network configuration** remains the weakest AI capability. Cross-plane connectivity configuration achieves only [24% accuracy](https://arxiv.org/abs/2506.03231) -- worse than random for a multi-step task. Network configuration requires understanding the customer's firewall topology, DNS hierarchy, certificate infrastructure, and load balancer configuration, none of which is available in the AI model's training data. This 24% accuracy figure is the empirical basis for rating cross-plane communication as Difficulty 4: the task is not conceptually hard, but AI cannot meaningfully assist with it.

**Code review quality** for AI-generated code requires careful attention. [AI-generated Kubernetes configurations contain 1.7x more issues and 8x more performance regressions](https://arxiv.org/abs/2502.20825) than human-written equivalents. [14% of 2,268 Kubernetes operators analyzed have security vulnerabilities](https://arxiv.org/abs/2502.20825). These quality gaps mandate that AI-assisted Phase 1 output must pass through rigorous human review -- the AI accelerates production but does not guarantee quality.

### Model C Scope Reduction

Model C reduces the managed service replacement scope by 40-60% because 5-7 of the 12 infrastructure domains remain in the ISV's cloud: observability (ISV retains cloud metrics/logging), CDN (ISV cloud serves the control-plane UI), DNS (ISV cloud handles DNS for the control plane), control-plane identity federation (ISV manages IdP configuration), and control-plane API gateway (ISV cloud handles rate limiting and developer portal). Only the data-plane domains require replacement: database, object storage, message queue, event streaming, data-plane secrets, and data-plane compute scaling.

However, Model C introduces a net-new engineering challenge: the cross-plane communication channel (rated Difficulty 4). This includes mTLS certificate management, gRPC streaming over unreliable WAN connections, connection resilience with automatic reconnection, split-horizon DNS for resolving services differently based on request origin, and outbound-only connection establishment that satisfies enterprise firewall policies. The cross-plane layer costs $75K-$150K in engineering investment and cannot be eliminated by AI because the composition is architecturally novel.

### Parity Drift

Wave 2 research established that cloud-first SaaS feature development runs [12-26x faster than on-prem brownfield adaptation](https://linearb.io/blog/dora-metrics), creating a cumulative parity drift of approximately 42% over 24 months. This means that by the time Phase 1 completes (6-9 months), the SaaS product will have advanced by 21% in features that the on-prem version does not yet have. Model C mitigates parity drift because the control plane carries the highest-velocity features (AI capabilities, analytics, UI improvements) while the data plane carries lower-velocity, more stable components (data processing, local compute). For Model B, parity drift is unmitigated and creates a competitive disadvantage that grows with time.

The maximum acceptable Phase 1 duration is 9-12 months. Beyond 12 months, the parity drift reaches approximately 42%, at which point the on-prem product may be commercially unviable relative to SaaS competitors offering more recent capabilities.

### CNCF Maturity as a Risk Indicator

The CNCF project maturity status of each replacement component provides a meaningful signal about production readiness risk. [CNCF Graduated](https://www.cncf.io/projects/) projects ([CoreDNS](https://www.cncf.io/projects/coredns/), [KEDA](https://keda.sh/), [Knative](https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/), OPA, [OpenTelemetry](https://www.cncf.io/projects/opentelemetry/)) have passed rigorous adoption and governance requirements and carry low substitution risk. CNCF Incubating projects ([Strimzi](https://strimzi.io/), Longhorn, [External Secrets Operator](https://external-secrets.io/)) have demonstrated production adoption but may have governance or feature gaps. CNCF Sandbox projects ([CloudNativePG](https://www.cncf.io/projects/cloudnativepg/), [K8sGPT](https://k8sgpt.ai/), [kagent](https://kagent.dev/)) are early-stage and carry meaningful production risk, though several (CloudNativePG with 132M+ downloads) have achieved de facto production status despite formal maturity classification.

The ISV should weight Phase 1 component selection toward CNCF Graduated and Incubating projects where feasible, accepting feature trade-offs in exchange for lower operational risk. For domains where no CNCF project exists (object storage after MinIO's license change, secrets management after Vault's BSL adoption), the ISV must evaluate commercial licensing terms or accept the governance risk of non-CNCF alternatives.

The aggregate CNCF coverage across the 12 infrastructure domains is strong: 8 of 12 domains have at least one CNCF project at Sandbox or above. The four domains without CNCF coverage (object storage, DNS automation beyond CoreDNS, CDN/edge, and serverless compute beyond Knative) require either commercial licensing or custom engineering, representing the residual irreducible complexity in Phase 1.

---

## Chapter 5: Phase 2 Findings -- AI-Assisted Customer Deployment

Phase 2 is where the per-customer variable cost model begins and where the deployment model choice creates the largest operational divergence between Models B and C. The research found that Phase 2 is the highest-AI-leverage phase for diagnostic tools ([80-90% MTTR reduction on recognized patterns](https://www.globenewswire.com/news-release/2025/11/05/3181574/0/en/Komodor-Introduces-Autonomous-Self-Healing-Capabilities-for-Cloud-Native-Infrastructure-and-Operations.html)) but the lowest-AI-leverage phase for deployment automation ([24% accuracy on network configuration](https://arxiv.org/abs/2506.03231), near-zero reduction in customer coordination overhead).

### The Deployment Cost Paradox

Model C's per-customer deployment cost is higher than Model B's for the initial deployment: $8K-$18.5K versus $6.5K-$15.5K. This is because Model C requires cross-plane connectivity setup ($2K-$5K per customer) that Model B does not -- establishing the outbound agent connection, validating cross-plane communication, configuring split-horizon DNS, and verifying telemetry flow from customer data plane to ISV control plane. All other Phase 2 cost components are identical: prerequisite validation ($2.5K-$5K), Helm installation ($1K-$3K), post-deployment validation ($1K-$2.5K), and customer coordination ($1.5K-$5K).

The paradox resolves over the customer lifetime. The Phase 2 overspend for Model C ($1.5K-$3K per customer) is recovered within 3-6 months of Phase 3 operations through the 1.5-2x support cost advantage. The cross-plane connectivity setup is a one-time cost that creates the observability channel enabling ongoing AI diagnostic benefits.

### AI Diagnostic Tools in Phase 2

AI diagnostic tools are production-ready and deliver measurable value during post-deployment validation and early-life support. The research documented three production-grade tools:

[K8sGPT](https://k8sgpt.ai/), a CNCF Sandbox project with 8,694 contributors, achieves [50% MTTR reduction](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration.html) in CLI and operator modes. It integrates with multiple LLM backends including OpenAI, Azure OpenAI, Amazon Bedrock, and local models via Ollama, making it deployable in both connected and air-gapped environments.

[Komodor Klaudia](https://komodor.com/platform/klaudia-ai-powered-troubleshooting/) delivers [80%+ MTTR reduction](https://www.globenewswire.com/news-release/2025/11/05/3181574/0/en/Komodor-Introduces-Autonomous-Self-Healing-Capabilities-for-Cloud-Native-Infrastructure-and-Operations.html), with root cause analysis in 15-30 seconds. Cisco, one of its enterprise customers, has documented this effectiveness at production scale.

[Datadog Bits AI SRE](https://www.datadoghq.com/blog/datadog-bits-ai/) achieves 90% faster root cause analysis by correlating metrics, logs, and traces with LLM-powered reasoning.

However, these tools' effectiveness is structurally dependent on the deployment model. In Model B, AI diagnostic tools operate on support bundles -- snapshots of cluster state collected by the customer, redacted for sensitive data, and transmitted to the ISV. By the time the ISV receives the bundle, the cluster state may have changed, error conditions may have resolved or worsened, and the diagnostic context is hours to days stale. In Model C, the control-plane telemetry channel provides real-time access to cluster metrics, logs, and agent-returned diagnostic results, enabling AI tools to operate on current state.

The measured effectiveness difference: Model B achieves 30-50% MTTR reduction with AI diagnostic tools (limited by data staleness). Model C achieves 70-90% MTTR reduction (matching vendor benchmarks because the data access model provides real-time telemetry). This 2x effectiveness gap is the strongest operational argument for Model C in Phase 2.

### Fleet Management Scaling

The research identified four distinct fleet management thresholds, each requiring qualitatively different tooling and organizational structure:

At 1-10 customers, deployment is manual: `helm install` from CLI, manual `kubectl` debugging, runbook-driven operations. Each deployment is treated as a project.

At 10-100 customers, GitOps automation becomes necessary: [Argo CD ApplicationSets](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/) or [Rancher Fleet](https://fleet.rancher.io/) provide declarative, version-controlled deployment across multiple clusters. The investment shifts from per-customer engineering to GitOps pipeline engineering.

At 100-1,000 customers, fleet management platforms become necessary: Rancher Fleet or custom fleet controllers manage configurations across hundreds of clusters. Per-customer Helm values files must be managed at scale.

At 1,000+ customers, fleet sharding becomes necessary. Rancher Fleet scaling experiments documented failure at 4,000 clusters x 50 bundles (200,000 total resources), establishing a hard architectural ceiling. No off-the-shelf solution exists for fleet management at this scale; custom sharded controllers are required. However, no ISV in the case study cohort has disclosed operating at 1,000+ self-managed customer environments, suggesting this threshold is theoretical for most ISVs.

AI assists marginally at each threshold (automating configuration generation, diagnosing deployment failures) but does not defer the transition to the next threshold. The staffing model must step-function at each boundary: +3-6.5 FTE for Model C, +5.5-9 FTE for Model B.

### Distribution Tooling Economics

The distribution and deployment tooling market is concentrated around a single mature vendor -- Replicated -- with emerging open-source alternatives that have not yet reached production maturity.

[Replicated](https://www.replicated.com/) serves 70 of the Fortune 100 and has validated 65,981+ environment combinations. Its Forrester Total Economic Impact study documented [$2.8M in avoided costs and 208% ROI](https://www.replicated.com/blog/hashicorp-achieves-208-roi-using-replicated-forrester) for ISVs using the platform. Replicated's pricing follows a base-plus-per-customer model: [$3,000/month base plus $50-$200 per customer per month](https://www.replicated.com/pricing), resulting in $156K/year at 50 customers. This cost is material but justified by the order-of-magnitude reduction in per-customer deployment cost: from $48K-$60K per customer (embedded engineer model, 10-week engagement) to $1K-$6K per customer with standardized Helm charts and distribution platform automation.

Glasskube (YC W24, operating as Distr) offers an open-source alternative at zero licensing cost but is pre-product-market-fit with a 5-person team. Distr is viable for cost-sensitive ISVs willing to accept feature gaps (no preflight checks, no support bundle collection, no embedded Kubernetes cluster) in exchange for eliminating the Replicated per-customer fee.

The ISV's distribution tooling decision has outsized impact on Phase 2 economics because it determines the per-customer deployment cost floor. At 50 customers over 3 years, the difference between the embedded-engineer model ($48K x 50 = $2.4M) and the distribution-platform model ($6K x 50 = $300K) is $2.1M -- larger than the entire Phase 1 fixed investment.

### Air-Gapped Deployment

[34% of software vendors ship air-gapped deployments](https://www.replicated.com/blog/2024-state-of-kots-report), making air-gap a significant market segment rather than an edge case. Air-gap is architecturally incompatible with Model C because the split-plane architecture requires outbound connectivity from the customer cluster to the ISV cloud. Air-gapped customers must use Model B.

Air-gapped deployment requires entirely separate tooling: [Zarf](https://zarf.dev/) for declarative air-gap packaging (converting connected Helm charts into disconnected bundles), physical or network-diode media transfer, in-cluster container registry (typically [Harbor](https://goharbor.io/)), and local LLM inference using quantized 7B-13B models since cloud LLM APIs are inaccessible. Zarf's parent company, [Defense Unicorns, raised $136M in Series B funding](https://www.defenseunicorns.com/blog/series-b-announcement), reflecting the defense/IC demand for this capability.

The ISV strategic implication: if the target market includes significant air-gapped demand (greater than 20% of pipeline), the ISV must maintain two parallel deployment tracks from Phase 2 onward, roughly doubling the deployment engineering investment. If air-gapped demand is less than 20%, the ISV should start with Model C for connected customers and add Model B as a separate track only when specific air-gapped deals justify the investment.

---

## Chapter 6: Phase 3 Findings -- AI-Assisted Ongoing Support

Phase 3 -- ongoing support of deployed on-premises customers -- is the phase that determines whether on-premises deployment is economically sustainable at scale. The central question is whether AI can break the linear cost scaling that historically makes on-prem support structurally margin-dilutive. The integrated answer across Waves 5, 6, and 7 is nuanced: AI compresses the cost curve from linear to sub-linear for diagnostic and monitoring workloads (estimated 40-60% cost reduction at 50+ customers), but cannot break the linear scaling of customer coordination, upgrade consent management, and version fragmentation support.

### The Three Support Cost Drivers

Wave 5 decomposed on-prem support cost into three structural drivers. Waves 6 and 7 provided the technical architecture for AI automation of each. Cross-domain integration revealed sharply different AI leverage by driver.

**Driver 1: Diagnostic Triage (AI leverage: HIGH)**

AI diagnostic capability for Kubernetes is production-ready. [SynergyRCA achieves approximately 0.90 precision](https://arxiv.org/html/2506.02490v1) on root cause analysis. [Komodor Klaudia delivers root cause in 15-30 seconds](https://komodor.com/blog/welcome-to-the-next-frontier-ai-on-kubernetes/). [K8sGPT](https://k8sgpt.ai/) achieves [50% MTTR reduction](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-ai-powered-kubernetes-diagnostics-and-troubleshooting-with-k8sgpt-and-amazon-bedrock-integration.html). Leidos documented [180x MTTR improvement](https://www.moveworks.com/us/en/resources/blog/what-is-incident-management-automation) ([82 hours reduced to minutes](https://www.jitbit.com/news/2266-average-customer-support-metrics-from-1000-companies/)) with diagnostic agents deployed in customer environments.

Wave 7 validated three concrete agent types that target this driver: (1) diagnostic agents achieving 95% accuracy on common failure patterns with 15-30 second root cause delivery, (2) continuous health monitoring agents using [eBPF DaemonSets that recover 40-70% of SaaS-level observability](https://www.groundcover.com/blog/ebpf-observability-agent), and (3) upgrade orchestration agents that reduce per-customer upgrade labor by 75-85%.

The binding constraint is the long tail. K8sGPT cannot troubleshoot intermittent errors -- errors that appear and disappear across diagnostic collection windows. The remaining 5% of failure patterns that AI cannot diagnose are disproportionately the highest-value, most expensive support cases. Moving diagnostic accuracy from 95% to 99% may cost as much as achieving the first 95%.

Net AI compression for diagnostic triage: 60-80% of per-customer diagnostic labor eliminated at 50+ customers.

**Driver 2: Version Fragmentation (AI leverage: MODERATE)**

Version fragmentation is the single largest structural cost driver identified in the research. N product versions times M environment configurations produces an [N x M support permutation matrix consuming 20-30% of IT operational time](https://www.fluiditservices.com/blog/the-integration-trap-why-fragmented-it-systems-cost-more-than-unified-solutions/). Every version-environment combination is a unique support context requiring version-specific runbooks, workarounds, and documentation. [79% of on-prem support issues originate from configuration changes](https://arxiv.org/html/2512.14792v1) rather than software defects, but the ISV must maintain knowledge of how each configuration change interacts with each product version.

Upgrade orchestration agents can compress per-customer upgrade labor by 75-85%. ByteDance's KubeAdmiral handles 30,000 daily operations at 95-98% success rate, demonstrating that large-scale Kubernetes orchestration is automatable. However, agents cannot force customers to upgrade. The fundamental problem is that customers control upgrade timing, and enterprise customers often defer upgrades through lengthy change-control processes. Automatic updates are explicitly not supported in air-gapped environments, meaning the most security-sensitive (and often highest-value) customers contribute most to version fragmentation.

Helm rollback -- the safety net for failed upgrades -- does not protect persistent volume data. This means rollback is the hardest upgrade phase to automate because data corruption during a failed upgrade cannot be undone by reverting the Helm release. The ISV must implement custom backup and restore procedures per database technology, per customer environment.

Net AI compression for version fragmentation: 30-50% of per-upgrade labor eliminated, but the number of supported versions (N) is unchanged. The ISV must still maintain version-specific documentation, runbooks, and workarounds for the installed base.

**Driver 3: Customer Coordination (AI leverage: NEAR-ZERO)**

The bilateral support model requires customer cooperation for every substantive support interaction: scheduling maintenance windows, obtaining cluster access credentials, approving change requests, coordinating artifact delivery, validating remediation actions. Each interaction involves human scheduling latency, internal approval chains, and timezone-dependent availability.

Distributed agents reduce the *need* for some customer coordination events (embedded agents can diagnose locally without customer intervention), but the coordination events themselves -- when they occur -- remain irreducibly human. Furthermore, the ISV's agent deployment introduces a new coordination burden. [96% of organizations plan to expand AI agent use](https://www.companyofagents.ai/blog/en/ai-agent-roi-failure-2026-guide), but over half identify data privacy as the primary obstacle, and [only 6% of companies fully trust AI agents for core processes](https://www.companyofagents.ai/blog/en/ai-agent-roi-failure-2026-guide). Initial agent consent negotiation requires an estimated 4-8 hours per customer for trust model review, security assessment, and deployment authorization.

Net AI compression for customer coordination: 10-20%. Embedded agents reduce the frequency of coordination events but cannot eliminate the per-event cost.

**Driver 4: Compliance and Regulatory Overhead (AI leverage: VERY LOW)**

Beyond the three primary operational cost drivers, Phase 3 includes a compliance maintenance burden that scales linearly with customer count and is essentially immune to AI compression. Each regulated customer requires ongoing maintenance of compliance documentation: HIPAA customers need annual BAA reviews and breach notification procedure updates, GDPR customers require data processing agreement maintenance and anonymization assessment updates per agent version change, FedRAMP customers require continuous monitoring reports, and ITAR customers require export control documentation maintenance.

The per-customer compliance cost varies by regulatory framework: HIPAA compliance maintenance is approximately $2K-$5K per customer per year, GDPR documentation maintenance is approximately $1K-$3K, and FedRAMP continuous monitoring can exceed $10K-$20K. These costs are not compressible by AI because they involve legal review, regulatory interpretation, and customer-specific assessment that cannot be generalized.

For ISVs targeting regulated verticals (the primary demand driver for on-prem investment), compliance overhead is a significant and growing cost component. The [EU Data Act (effective January 2027)](https://digital-strategy.ec.europa.eu/en/policies/data-act), [HIPAA NPRM final rule (expected May 2026)](https://www.hhs.gov/hipaa/for-professionals/regulatory-initiatives/hipaa-security-rule-nprm/index.html), and [DORA enforcement (began January 2025)](https://www.digital-operational-resilience-act.com/) add new compliance requirements that increase this per-customer fixed cost.

### The Sub-Linear Scaling Discovery

Integrating the three drivers reveals that Phase 3 support cost is not a single linear function but a two-part function:

The sub-linear component (approximately 60-70% of total support cost) consists of tasks that benefit from fleet-wide AI improvements: diagnostic triage, drift detection, health monitoring, and routine upgrade execution. When the ISV improves its diagnostic agent's accuracy or adds a new failure pattern to its runbook, the improvement applies to all customers simultaneously. This creates sub-linear scaling: the marginal support cost of the (N+1)th customer is lower than the Nth customer because the diagnostic infrastructure is more mature.

The linear component (approximately 30-40% of total support cost) consists of tasks that are inherently per-customer: coordination scheduling, upgrade consent management, environment-specific edge cases, regulatory compliance maintenance, and trust model negotiation. Each customer is an independent human relationship. Adding the (N+1)th customer adds the full marginal coordination cost.

At enterprise ISV scale (50+ customers), the sub-linear component dominates, meaning AI achieves genuine sub-linear scaling of the aggregate support function. At early-stage scale (5-15 customers), the linear component dominates because per-customer coordination overhead is amortized across fewer customers.

### Model C's Structural Advantage in Phase 3

Model C achieves approximately 1.5-2x the support cost efficiency of Model B, primarily because the control-plane telemetry channel enables real-time AI triage rather than the latency-prone support-bundle analysis that Model B requires. At 50 customers, the annual support cost comparison (with AI):

- Model B: $450K-$2.3M
- Model C: $250K-$1.45M (not including agent infrastructure of $150K-$420K)
- Model C with agents: $400K-$1.87M

Model C's cost advantage widens at scale because the sub-linear component compounds while Model B's linear scaling does not.

---

## Chapter 7: The Distributed Agent Runtime -- Architecture and Economics

The distributed agent runtime -- ISV-authored agents executing inside customer-controlled Kubernetes environments, processing customer data locally, and returning only structured results -- is the most architecturally novel and strategically important component of the agentic on-premises deployment model. The research validates that the pattern is (1) architecturally grounded in two decades of distributed compute precedent ([Trino](https://trino.io/docs/current/overview/concepts.html), [Spark](https://spark.apache.org/docs/latest/tuning.html), [Databricks Lakehouse Federation](https://learn.microsoft.com/en-us/azure/databricks/query-federation/), [federated learning](https://proceedings.mlr.press/v54/mcmahan17a.html)), (2) economically viable at enterprise scale with egress break-even at [25-35 TB/month per customer at $0.09/GB AWS egress](https://www.nops.io/blog/aws-egress-costs-and-how-to-avoid/), (3) transformative for support economics (estimated [40-60% support cost reduction](https://komodor.com/platform/klaudia-ai-powered-troubleshooting/) when combined with Model C telemetry), (4) [legally uncharted with no regulator having adjudicated the result-only transfer pattern](https://www.europeanlawblog.eu/pub/dq249o3c/release/1), and (5) engineering-intensive, requiring a custom trust stack, observability split, and failure resilience architecture that no off-the-shelf framework provides end-to-end.

### The Six-Layer Architecture

**Layer 1 -- Placement and Dispatch:** The ISV cloud writes an `AgentTask` [Custom Resource Definition (CRD)](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) to the customer cluster via the outbound-only channel established in Model C. A pre-installed on-prem controller reconciles the CRD into a running Job or [Agent Sandbox](https://opensource.googleblog.com/2025/11/unleashing-autonomous-ai-agents-why-kubernetes-needs-a-new-standard-for-agent-execution.html) pod. The dispatch channel is the same connection used for control-plane communication -- no additional network plumbing is required. Agent Sandbox's [`SandboxWarmPool` CRD delivers sub-second cold start via pre-warmed pools](https://faun.dev/c/news/kaptain/agent-sandbox-brings-kernel-level-guardrails-to-ai-agents-on-kubernetes/), enabling rapid agent response. For Model B (no control plane channel), dispatch requires a separate per-customer VPN or agent relay, adding $2K-$5K per customer in setup cost.

**Layer 2 -- On-Prem Execution Environment:** [Agent Sandbox (a Kubernetes SIG Apps subproject at v1alpha1)](https://opensource.googleblog.com/2025/11/unleashing-autonomous-ai-agents-why-kubernetes-needs-a-new-standard-for-agent-execution.html) provides kernel-level isolation via gVisor or Kata Containers. Agent images are distributed as OCI artifacts with [SLSA Level 2+ build provenance](https://slsa.dev/spec/v1.2/) and verified at deployment via [Kyverno admission policies](https://kyverno.io/docs/policy-types/cluster-policy/verify-images/) enforcing ISV public key verification. On-prem LLM inference uses 7B-70B open-weight models ([Qwen3 Apache 2.0](https://qwenlm.github.io/blog/qwen3/), [DeepSeek R1 MIT](https://github.com/deepseek-ai/DeepSeek-R1), [Phi-4 MIT](https://huggingface.co/microsoft/phi-4)) served by [vLLM](https://docs.vllm.ai/) or [SGLang](https://sgl-project.github.io/) for data-touching tasks. The hardware floor is a single A6000 GPU (~$5K) for 4-bit quantized 70B models, or a single consumer GPU for 7B models. Reasoning-heavy tasks that do not touch customer data are routed to cloud frontier models via abstracted, anonymized data representations.

**Layer 3 -- Boundary Enforcement:** Three-layer composition ensures only structured results -- never raw customer data -- cross the network boundary. At compile time, schema contracts (Protobuf or JSON Schema) define the exact structure of agent outputs. At runtime, [OPA (CNCF Graduated)](https://www.openpolicyagent.org/) policy engines enforce access rules, and DLP sidecars ([Presidio](https://microsoft.github.io/presidio/) or Skyflow) detect and redact any PII that appears in agent outputs. Where available, [cryptographic attestation via TEE (Intel SGX/TDX, AMD SEV-SNP)](https://www.intel.com/content/www/us/en/developer/tools/trust-domain-extensions/overview.html) provides hardware-rooted verification. Data reduction ratios range from [14:1 for SIEM telemetry to 200,000:1 for OLAP aggregation](https://mlcommons.org/2025/09/small-llm-inference-5-1/), with a geometric mean of 1,000:1 to 10,000:1. These ratios mean that a customer generating 100 GB of raw diagnostic data produces only 10 KB to 10 MB of structured agent output -- comfortably transmissible over 10 Mbps commodity internet.

**Layer 4 -- Observability and Telemetry:** The [OTel Collector](https://www.cncf.io/projects/opentelemetry/) with a redaction processor in fail-closed mode implements a split pipeline. Execution telemetry (timing, token counts, tool names, error types, completion status) is exportable to the ISV cloud. Data telemetry (prompt content, tool arguments, retrieved documents) remains local-only. [OpenTelemetry's GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) explicitly mark data-bearing attributes as opt-in and off-by-default, making this split a configuration rather than an engineering task. [eBPF-based monitoring agents achieve +9% CPU overhead](https://www.groundcover.com/blog/ebpf-observability-agent) above baseline.

**Layer 5 -- Failure Resilience:** Durable execution frameworks (LangGraph or Temporal) provide checkpoint/resume for long-running agent tasks. Saga-pattern compensation handles partial failures. Circuit breakers with adaptive thresholds address AI-specific failure patterns. The research identified a 14-failure taxonomy for AI agents, with the most common being hallucinated API calls (42% of production failures) and GPU memory leaks (23%). Agents default to read-only mode; the `autonomyLevel` CRD field gates escalation from recommend-only to auto-with-rollback to full autonomy, requiring explicit customer consent at each level.

**Layer 6 -- Regulatory Compliance:** The result-only transfer pattern has not been formally adjudicated by any major regulator. [GDPR requires a documented anonymization assessment per Recital 26](https://www.europeanlawblog.eu/pub/dq249o3c/release/1) to demonstrate that agent outputs cannot be re-identified to individual data subjects. HIPAA requires a Business Associate Agreement (BAA) regardless of whether raw Protected Health Information (PHI) crosses the boundary. [CCPA AB 1008](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1008) explicitly covers AI system outputs as personal information, meaning agent results may be subject to California privacy rights even if the raw data remains on-premises. ITAR may classify AI-derived results from controlled technical data as themselves controlled, potentially restricting the transfer of agent outputs from defense contractor environments. These regulatory requirements add per-customer fixed cost that AI cannot compress.

### Agent Type Catalog

The research identified four concrete agent types, sequenced by trust level and autonomous capability:

**Phase A -- Diagnostic Agents (deploy during Phase 2 pilot):** Read-only agents that analyze cluster state, logs, and metrics to diagnose specific failure patterns. Capabilities include pod eviction analysis, OOMKill root cause identification, CrashLoopBackOff diagnosis, storage class mismatch detection, and network policy conflict resolution. Accuracy: 95% on the 50 most common Kubernetes failure patterns. Deployment model: Kubernetes Job triggered by CRD. Customer impact: zero (read-only, no mutations). Leidos documented 180x MTTR improvement (82 hours reduced to minutes) with this agent type.

**Phase B -- Health Monitoring Agents (deploy after Phase A trust established):** Continuous agents that run as eBPF DaemonSets, observing kernel-level events (syscalls, network packets, file operations) to detect anomalies before they become customer-visible incidents. These agents recover 40-70% of the observability that the ISV lost by moving from SaaS to on-prem. CPU overhead: approximately 9% above baseline. Memory overhead: approximately 200 MB per node. [SAP Focused Run operates 4,000+ monitoring agents](https://support.sap.com/en/alm/sap-focused-run.html) across customer environments, demonstrating this pattern at scale. [Netdata achieves less than 5% CPU and approximately 200 MB RAM](https://www.netdata.cloud/) per agent instance.

**Phase C -- Upgrade Orchestration Agents (deploy after 6+ months of Phase B operation):** Semi-autonomous agents that execute multi-step upgrade workflows: pre-upgrade validation, backup creation, rolling upgrade execution, post-upgrade health check, and automatic rollback on failure. ByteDance's KubeAdmiral handles 30,000 daily operations at 95-98% success rate, demonstrating that large-scale Kubernetes orchestration is automatable. The critical constraint is that Helm rollback does not protect persistent volume data, meaning the agent must implement custom backup/restore per database technology before attempting any upgrade.

**Phase D -- Auto-Remediation Agents (deploy only with explicit customer opt-in):** Autonomous agents that detect and remediate specific failure classes without human intervention. Gated by the `autonomyLevel` CRD field at the customer level: `recommend` (default), `auto-with-rollback`, and `full-auto`. The research recommends that ISVs defer Phase D until Phase C agents have operated for 12+ months with a documented track record. [Gartner projects 40% of agentic AI projects will be cancelled](https://fpa-trends.com/article/agentic-ai-projects-fail-2027-how-fpa-succeeds), and [only 6% of companies fully trust AI agents for core processes](https://www.companyofagents.ai/blog/en/ai-agent-roi-failure-2026-guide). Premature autonomy deployment risks customer trust damage that is difficult to reverse.

### Economic Impact

At 50 customers with a realistic tier distribution (30 SMB, 15 mid-market, 5 enterprise):

Support cost savings versus Model B without agents: $250K-$2.4M annually. The range reflects uncertainty in AI diagnostic accuracy at scale and the proportion of support cost addressable by agents.

Egress cost savings: $310K annually. This is concentrated in mid-market and enterprise tiers. SMB customers with less than 10 TB/month of data volume do not generate sufficient egress savings to offset agent infrastructure cost ($400/month agent cost versus $367/month egress savings = -$33/month net).

Agent infrastructure cost: $150K-$420K annually ($250-$700 per customer per month covering CPU/memory, optional GPU for LLM inference, coordination overhead, and security/attestation).

Net annual impact: $410K-$2.3M positive, translating to $2.9M-$16M in enterprise value at 7x revenue multiples for infrastructure software companies.

### The Competitive Moat

The ISV that implements the distributed agent pattern gains a structural moat that open-source self-hosters cannot replicate. This moat operates through four mechanisms:

First, the aggregate telemetry advantage. The ISV accumulates diagnostic patterns, failure signatures, and remediation playbooks across N customer environments. Each new customer adds data points that improve the diagnostic model for all customers. Open-source self-hosters operate in isolation; they see only their own failure patterns and cannot benefit from cross-customer learning.

Second, operational AI trained on production data. Agent models fine-tuned on hundreds of real customer incidents (pod evictions on OpenShift with restricted-v2 SCC, CSI driver failures on RKE2 with CIS defaults, cross-plane connectivity disruptions during K8s upgrades) outperform generic Kubernetes troubleshooting models in the ISV's specific operational domain.

Third, trust infrastructure as switching cost. The [SLSA](https://slsa.dev/spec/v1.2/) + [Cosign](https://docs.sigstore.dev/cosign/signing/overview/) + [Kyverno](https://kyverno.io/) + [OPA](https://www.openpolicyagent.org/) trust stack, once deployed and integrated into the customer's security workflow (security team reviews agent images, compliance team validates boundary enforcement policies), creates switching cost comparable to traditional enterprise software. Ripping out the ISV's agent infrastructure and replacing it with a competitor's requires re-validation through the customer's entire security review process.

Fourth, regulatory documentation as barrier. Per-customer anonymization assessments, BAAs, GDPR data processing agreements, and compliance certifications are ISV-specific and non-portable. A competing ISV cannot inherit these documents; they must create their own from scratch per customer.

Wave 8 research confirms that the durable commercial moat for on-prem ISVs is operational -- support SLAs, Kubernetes operators, automated lifecycle management -- rather than product-based. The distributed agent pattern is the strongest instantiation of this operational moat because it creates a data flywheel that compounds with customer count.

---

## Chapter 8: ISV Economic Model

### Methodology

The economic model uses a differential break-even framework adapted from [SaaS break-even analysis (Yale School of Management, 2024)](https://som.yale.edu/sites/default/files/2025-04/A%20Primer%20on%20Breakeven%20Analysis.pdf). The ISV does not compare on-prem costs against zero; it compares the contribution margin of serving a customer on-premises versus SaaS. The break-even point is the customer count at which the on-prem ACV premium revenue exceeds the incremental cost of on-prem delivery.

The formula:

```
Differential BEP = Fixed Investment (amortized annual)
                   / [(On-Prem ACV - On-Prem Variable Cost) - (SaaS ACV - SaaS Variable Cost)]
```

All input variable ranges are drawn from F80 (Break-Even Model Inputs) and cross-validated against S01-S10 primary research and S11-S15 integration analyses.

### Scenario Results

**Base Case (Mid-Range Inputs, Model C):** At $200K SaaS ACV, 1.5x on-prem premium ($300K), $400K fixed investment amortized over 3 years, 50% AI support reduction, and $13K per-customer deployment cost, the differential contribution margin per customer is $103K in year 1 and $116K in subsequent years. Break-even: 2 customers.

**Conservative (Model C):** At 1.3x premium ($260K), $600K fixed investment, 30% AI support reduction, and $18.5K per-customer deployment cost, the differential contribution margin is $52.4K. Break-even: 4 customers.

**Conservative (Model B):** At 1.3x premium ($260K), $750K fixed investment, 30% AI support reduction, and $15.5K per-customer deployment cost, the differential contribution margin is $44.5K. Break-even: 6 customers.

**Pessimistic (No Premium, No AI):** At 1.0x ACV (parity pricing with SaaS), the differential contribution margin is -$10.5K (Model C) to -$19.5K (Model B) per customer. Break-even: never. On-prem is structurally unprofitable at parity pricing without AI support automation.

### The Minimum Viable Premium

The minimum on-prem ACV premium required for profitability depends on AI support compression:

| AI Compression | Model C Min Premium | Model B Min Premium |
|---------------|-------------------|-------------------|
| 0% (no AI) | 1.06x | 1.10x |
| 30% (conservative) | 1.01x | 1.04x |
| 50% (moderate) | <1.0x (profitable at parity) | 1.00x |
| 70% (aggressive) | <1.0x | <1.0x |

At 50% AI compression (the best-supported scenario per named case studies: [Vodafone 70% resolution rate](https://www.moveworks.com/us/en/resources/case-study/vodafone), [AssemblyAI 50% AI-resolved tickets](https://www.zendesk.com/blog/ai-customer-service-stories/), [Microsoft 31% first-contact resolution improvement](https://blogs.microsoft.com/blog/2025/01/14/how-microsoft-is-transforming-support-with-ai-agents-and-partners/), [Klarna $40M annual savings](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)), Model C becomes profitable even at SaaS-equivalent pricing. This is a significant finding: with moderate AI investment, the ISV does not need to charge a premium for on-prem to make the economics work. The premium becomes pure margin upside rather than a breakeven requirement.

### Margin Projections at Scale

At 50 customers with $200K SaaS ACV and 1.5x on-prem premium:

Model C with 50% AI compression achieves 68% gross margin and generates $5.0M net annual profit versus SaaS. Model B with 50% AI achieves 62% gross margin and $4.5M net annual profit. Model C with 70% AI compression reaches 74% gross margin, approaching SaaS-equivalent economics (75-85%).

At 50 customers with 1.3x premium (conservative) and 30% AI: Model C achieves 63% gross margin, and Model B achieves 57%. These margins are materially lower than SaaS but well above the profitability threshold.

### Sensitivity Analysis

The model is most sensitive to ACV premium and AI support reduction, and least sensitive to fixed investment (which is amortized across the customer base). A [1% improvement in pricing increases profits by 11.1% on average](https://www.priceintelligently.com/blog/bid/181199/you-re-pricing-your-product-wrong-software-pricing). A 5% improvement in customer retention [increases lifetime value by 25-95%](https://hbr.org/2014/10/the-value-of-keeping-the-right-customers). These sensitivities favor the on-prem model: on-prem customers have structurally higher switching costs (installed infrastructure, security integrations, compliance documentation) that reduce churn relative to SaaS.

Per-customer deployment cost has a moderate sensitivity. Moving from $60K (embedded-engineer model, no tooling) to $10K (Replicated or Distr automation) shifts the net annual impact by approximately $2.5M at 50 customers. This underscores the importance of distribution tooling investment.

### On-Prem Customer Lifetime Value

The economic model reveals a counterintuitive finding regarding customer lifetime value (LTV). On-prem customers have structurally higher LTV than SaaS customers despite higher per-customer costs. The mechanism is switching cost: once a customer has deployed the ISV's product on their own infrastructure, integrated it with their security workflows, established compliance documentation, and trained their operations team, the cost of switching to a competitor is substantially higher than cancelling a SaaS subscription. This switching cost manifests as lower churn rates.

The research documented that [on-prem customer LTV is approximately 2.2x cloud SaaS LTV](https://www.wearefounders.uk/saas-churn-rates-and-customer-acquisition-costs-by-industry-2025-data/), driven by lower churn rates and higher ACVs. At a 1.5x ACV premium and an estimated 5% annual churn (versus 8-12% for SaaS), the on-prem LTV is $300K / 0.05 = $6M versus $200K / 0.10 = $2M for SaaS. This LTV advantage partially explains why ISVs like GitLab price on-prem at SaaS parity: the higher LTV compensates for the higher support cost even without a price premium.

However, the LTV advantage is only realized if the ISV achieves sustainable per-customer economics. An ISV losing $19.5K per customer per year on on-prem (the pessimistic scenario) has negative unit economics regardless of customer lifetime. The LTV advantage amplifies both success and failure: a profitable on-prem customer base compounds value rapidly, while an unprofitable one compounds losses.

### Enterprise Value Impact

Using 7x revenue multiples (median for infrastructure software SaaS companies):

At 50 customers with 1.3x premium: $21M incremental enterprise value (conservative). At 1.5x premium: $35M. At 2.0x premium: $70M.

The research documented that [IBM acquired HashiCorp for $6.4B](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform) and [Confluent for $11B](https://www.fool.com/earnings/call-transcripts/2025/10/28/confluent-cflt-q3-2025-earnings-call-transcript/), both deriving substantial revenue from self-managed deployments. These acquisitions validate that hybrid SaaS + on-prem portfolios command premium multiples when the on-prem economics are demonstrably sustainable. For the ISV considering on-prem investment, building Model C capability may increase acquisition enterprise value even if standalone unit economics are marginal.

---

## Chapter 9: Agentic AI Trajectory and Incentive Structure

The trajectory of agentic AI capabilities over the 24-month planning horizon materially affects the ISV's investment decision. The research examined whether current trends favor or disfavor on-prem investment, and found a complex answer: AI capability trajectories favor both cloud and on-prem simultaneously, but the ecosystem trajectories strongly favor cloud.

### Capability Trajectory

AI capabilities are advancing at an accelerating rate. The [Epoch AI Capabilities Index shows a 1.85x acceleration factor post-April 2024](https://epoch.ai/data/notable-ai-models). [METR's measurement of autonomous task horizon doubling time is 89-131 days](https://metr.org/blog/2026-1-29-time-horizon-1-1/). [SWE-bench performance has reached 80.8%](https://www.swebench.com/), up from 12.47% in October 2023. [SRE-Skills-Bench scores on Kubernetes-specific tasks range from 94.5% to 97.3%](https://github.com/isovalent/sre-skills-bench), suggesting near-human performance on standard K8s troubleshooting. The projection from these trends is 8-hour workday autonomy by 2027 -- AI agents capable of performing a full day's work on routine SRE tasks without human intervention.

But capability benchmarks overstate production reliability. [MCPMark](https://mcpmark.com/), which measures multi-step tool-use task completion, shows reliability ranging from only 25% to 52%. The gap between single-step capability (high) and multi-step reliability (moderate) is the primary constraint on autonomous agent deployment. An AI that can diagnose a pod eviction 95% of the time but can execute a 5-step remediation workflow only 40% of the time is not ready for unsupervised autonomous operation.

This reliability gap is the empirical foundation for the research's recommended phased agent deployment: start with diagnostic-only agents (single-step, high reliability), progress to monitoring agents (continuous but read-only), then bounded autonomous agents (multi-step with rollback) only after trust is established.

### Open-Weight Model Convergence

Open-weight models have achieved near-parity with proprietary models on standard benchmarks. The [MMLU gap dropped from 17.5 points to 0.3 points](https://arxiv.org/abs/2412.04315) in approximately one year. [DeepSeek V3](https://github.com/deepseek-ai/DeepSeek-V3) reaches 95%+ of GPT-4o performance. The gpt-oss-120b model runs on a single 80GB GPU, demonstrating that frontier-adjacent capability is achievable on commodity hardware.

This convergence is critical for the distributed agent architecture because on-prem LLM inference requires open-weight models. The ISV cannot deploy proprietary models (GPT-4, Claude) to customer environments without API access. Open-weight convergence means that the quality gap between cloud-hosted reasoning and on-prem data-processing is small enough for production use, enabling the hybrid routing pattern: data-touching tasks on-prem with open-weight models, reasoning-heavy tasks on cloud frontier models via abstracted data.

However, [open-source adoption has paradoxically flattened to 13% of enterprise AI workloads](https://a16z.com/ai-in-the-enterprise-2025/), down from 19% in the prior measurement period. Capability convergence alone does not drive adoption. The missing elements are ecosystem maturity: tooling, fine-tuning infrastructure, support contracts, compliance certifications, and developer experience. These ecosystem elements remain cloud-first.

Permissively licensed models available for on-prem deployment include [Qwen3 (Apache 2.0)](https://qwenlm.github.io/blog/qwen3/), [DeepSeek R1 (MIT)](https://github.com/deepseek-ai/DeepSeek-R1), and [Phi-4 (MIT)](https://huggingface.co/microsoft/phi-4). Production-grade serving infrastructure ([vLLM](https://docs.vllm.ai/), [SGLang](https://sgl-project.github.io/)) is mature. [TGI entered maintenance mode in December 2025](https://huggingface.co/docs/text-generation-inference/en/index) and should be avoided for new deployments.

### The Five-Layer Cloud Compounding Advantage

The research identified five reinforcing layers of cloud ecosystem advantage that compound over time:

**Layer 1 -- Data Concentration:** [82% of Kubernetes workloads run on cloud infrastructure](https://www.cncf.io/reports/cncf-annual-survey-2024/). [66% of AI inference runs on Kubernetes](https://www.cncf.io/reports/cncf-annual-survey-2024/). This concentration means cloud providers accumulate vastly more operational data (failure patterns, configuration distributions, performance characteristics) than any on-prem environment. More data produces better AI models, which attract more workloads, which produce more data. On-prem environments are isolated and cannot pool their operational data without the distributed agent architecture described in Chapter 7.

**Layer 2 -- Tooling Maturity:** [AWS provides 60+ MCP (Model Context Protocol) servers covering 15,000+ APIs](https://www.marktechpost.com/2025/07/20/model-context-protocol-mcp-for-enterprises-secure-integration-with-aws-azure-and-google-cloud-2025-update/). The Kubernetes on-prem MCP ecosystem consists of a Red Hat community server and a containers/kubernetes-mcp-server project, both in early stages. [Terraform has accumulated 5B+ downloads](https://www.hashicorp.com/en/blog/terraform-aws-provider-5-billion-downloads-state-of-cloud-infrastructure) across 29,697 repositories, providing dense training data for infrastructure-as-code AI tools. Kubernetes operator data is sparse and fragmented. Better tools attract more developers, which produce more tool contributions, which improve the tools.

**Layer 3 -- Financial Incentives:** Cloud providers have secured [$470B+ in committed-spend agreements](https://www.platformonomics.com/2024/06/follow-the-capex-the-cloud-hyperscaler-investment-cycle/) through MACC (Microsoft Azure Consumption Commitment) and EDP (Enterprise Discount Program) structures. These agreements explicitly exclude on-prem workloads, creating a financial incentive to run everything in cloud. Credits that can only be spent on cloud services create lock-in that generates more investment, more data, and more ecosystem momentum.

**Layer 4 -- Provider Investment:** Cloud providers have committed [$80B+ in capital expenditure](https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-set-to-pay-cloud-partners-80-billion-through-2029/) for AI infrastructure (GPU clusters, networking, cooling). CNCF project budgets are in the $10M range. This 8,000:1 investment ratio ensures that cloud AI capabilities advance faster than open-source on-prem equivalents, even when the underlying models converge in capability.

**Layer 5 -- Iteration Velocity:** Cloud-first engineering achieves [12-26x faster CI/CD cycles](https://linearb.io/blog/dora-metrics) than on-prem brownfield work. The infrastructure-as-API model (provision a database with a Terraform statement, scale compute with an API call) enables experimentation velocity that per-customer Helm deployments cannot match. Speed enables more experiments, which produce more learnings, which enable more speed.

Each layer reinforces the others, and the compound effect grows over time. The net result is a persistent 20-35% AI productivity gap between cloud-first and on-prem engineering that the research projects will widen, not narrow, over the 24-month planning horizon.

### Countervailing Forces

Four forces push against cloud compounding:

**Open-weight model convergence** narrows the raw capability gap, enabling on-prem LLM inference for data-touching tasks. This is the most powerful countervailing force and the one most likely to persist.

**CNCF agentic standardization** provides emerging infrastructure for on-prem AI agents. [kagent (CNCF Sandbox, May 2025)](https://kagent.dev/) provides a Kubernetes-native agent runtime. [Agent Sandbox (kubernetes-sigs subproject, v1alpha1)](https://opensource.googleblog.com/2025/11/unleashing-autonomous-ai-agents-why-kubernetes-needs-a-new-standard-for-agent-execution.html) provides sandboxed agent execution. The [CNCF AI Conformance Program (November 2025)](https://www.cncf.io/blog/2025/11/13/cncf-launches-ai-conformance-program/) provides certification for AI workloads on Kubernetes, explicitly targeting on-prem deployments. These projects are 12-18 months from production readiness.

**EU regulatory pressure** creates legal requirements for data sovereignty that SaaS cannot satisfy. The GDPR's existing data sovereignty provisions are being strengthened by the EU Data Act (effective January 2027), which prohibits egress fees for data switching. This does not apply to production data transfer but signals a regulatory trajectory toward data localization.

**Defense and intelligence community requirements** create a captive market segment where air-gap is mandatory and SaaS is architecturally impossible. ITAR export controls, IL4-IL6 classification levels, and compartmented information handling requirements ensure durable demand for on-prem deployment in the defense vertical.

These forces do not close the cloud ecosystem gap. They create durable demand pockets where on-prem deployment is required despite the ecosystem disadvantage. The ISV's task is to serve these demand pockets efficiently (via Model C) while minimizing the engineering drag on its SaaS business.

### The Tooling Maturity Gap

The CNCF agentic ecosystem is the most important tooling development for ISVs building distributed agent architectures, but the ecosystem is immature relative to cloud equivalents.

[kagent](https://kagent.dev/), the leading candidate for ISV agent runtime, entered CNCF Sandbox in May 2025 and attracted 100 contributors in 100 days. It is built on [AutoGen](https://microsoft.github.io/autogen/) and [Google ADK](https://google.github.io/adk-docs/), implements both [A2A](https://google.github.io/A2A/) and [MCP](https://modelcontextprotocol.io/) protocols, and supports Ollama for air-gapped LLM inference. [Solo.io has announced an enterprise variant](https://www.solo.io/). However, kagent is at v0.x and is not yet suitable for production ISV deployment. The projected timeline to CNCF Incubating status is Q2 2027.

[Agent Sandbox](https://opensource.googleblog.com/2025/11/unleashing-autonomous-ai-agents-why-kubernetes-needs-a-new-standard-for-agent-execution.html), a Kubernetes SIG Apps subproject, provides the sandboxed execution environment for AI agents. Its five CRDs (Sandbox, SandboxTemplate, SandboxClaim, [SandboxWarmPool](https://faun.dev/c/news/kaptain/agent-sandbox-brings-kernel-level-guardrails-to-ai-agents-on-kubernetes/), SandboxAgentAction) provide a declarative API for agent lifecycle management. Sub-second warm pool startup via pre-warmed containers enables rapid agent dispatch. However, it was released at v1alpha1/v0.1.1 in February 2026 and is projected to reach v1beta1 by Q1 2027.

The Kubernetes MCP server ecosystem is in very early stages. Red Hat has released a community K8s MCP server in Go, and the containers/kubernetes-mcp-server project provides an alternative. Both are expected to reach production readiness by H2 2026. In contrast, AWS provides 60+ MCP servers covering 15,000+ APIs, illustrating the magnitude of the cloud tooling advantage.

The ISV gap analysis identified six unfilled capabilities in the on-prem operations platform: customer-hosted agent runtime (kagent/Agent Sandbox, 12-18 months), cross-distribution automated testing (no vendor provides this), ISV-to-customer trust stack reference architecture (components exist but no integrated reference), federated learning for cross-customer models (gradient inversion risk, no production framework), self-service customer deployment portal (Replicated KOTS only), and agent observability with execution/data split (OTel Collector fills this but requires custom configuration).

ISVs building the distributed agent architecture today must build custom integration on alpha-stage projects, accepting the risk that the API surface may change before v1.0. This is the primary engineering risk of the "invest now" recommendation for regulatory-first ISVs: the early-mover advantage comes with tooling immaturity risk.

---

## Chapter 10: Comparison Matrix

The full comparison matrix (S23) evaluates Model A, Model B, and Model C across more than 40 dimensions in 8 categories. The complete matrix is provided in Exhibit S23; this chapter summarizes the key findings.

### Economics

Model C achieves the best economic balance: 30-40% lower fixed investment than Model B ($235K-$550K versus $350K-$850K), higher gross margin ([75-90%](https://www.cloudzero.com/blog/saas-gross-margin-benchmarks/) versus 55-70% with AI), and [break-even at 2-5 customers](https://www.getmonetizely.com/articles/the-break-even-analysis-understanding-pricing-thresholds-in-saas) versus [5-16 for Model B](https://www.getmonetizely.com/articles/the-break-even-analysis-understanding-pricing-thresholds-in-saas). Model A remains the highest-margin option ([75-85% gross margin](https://softwareequity.com/blog/gross-margin-saas/)) but forfeits regulatory-gated revenue.

The 3-year total cost per customer at 50-customer scale with AI automation: Model A includes support in SaaS operations at no incremental cost. Model B ranges from $57K to $340K. Model C ranges from $34K to $107K. The 3-5x range between Model B and Model C reflects the compounding advantage of Model C's sub-linear support scaling.

### AI Leverage

Model C achieves 70-90% MTTR reduction with AI diagnostic tools versus 30-50% for Model B. The 2x effectiveness gap results entirely from the data access model: real-time telemetry (Model C) versus hours-old support bundles (Model B). Model C also enables distributed agent deployment via the existing control-plane channel at zero additional network cost, while Model B requires a separate per-customer dispatch channel at $2K-$5K per customer.

### Competitive Position

Model C achieves the strongest competitive moat versus open-source self-hosters through the aggregate telemetry flywheel. Model B achieves only operational moat (support SLAs and lifecycle management). Model A achieves limited moat (SaaS is an architecture, not a proprietary technology). The ISV using Model C accumulates a defensible asset -- cross-customer diagnostic intelligence -- that grows with every deployed customer.

### Summary Scorecard

| Criterion | Model A | Model B | Model C |
|-----------|---------|---------|---------|
| Economic efficiency | 5/5 | 2/5 | 4/5 |
| Regulatory reach | 1/5 | 5/5 | 4/5 |
| AI leverage | 5/5 | 2/5 | 4/5 |
| Competitive moat vs. self-hosters | 2/5 | 3/5 | 5/5 |
| Operational simplicity | 5/5 | 2/5 | 3/5 |
| Scalability | 5/5 | 2/5 | 4/5 |
| Risk profile | 3/5 | 2/5 | 3/5 |
| **Total** | **26/35** | **18/35** | **27/35** |

Model C scores highest (27/35) by capturing most of Model A's economic and operational advantages while accessing most of Model B's regulatory reach. Model A scores 26/35 -- one point lower -- because it forfeits regulatory reach (1/5) and competitive moat versus self-hosters (2/5). For ISVs without regulatory-gated demand, Model A remains the rational choice given the one-point scoring difference and zero incremental engineering complexity.

Model B scores 18/35 and is justified only for air-gapped customers or environments where the compliance framework explicitly prohibits any outbound network connectivity from the data processing cluster.

### Architecture and Operational Dimensions

The comparison matrix reveals several dimensions where the deployment model choice creates qualitative, not just quantitative, differences:

**ISV observability** is perhaps the most consequential architectural difference. Model A provides full, unrestricted observability -- the ISV sees everything. Model B provides zero observability -- the ISV sees nothing except what the customer manually provides via support bundles. Model C provides partial observability through the control-plane telemetry channel and agent-returned results. This partial observability is sufficient for AI-assisted diagnostics (70-90% MTTR reduction) but insufficient for the kind of proactive, data-driven product improvement that SaaS observability enables.

**Version fragmentation** follows a similar pattern. Model A has zero fragmentation -- the ISV controls the release cycle and all customers run the same version. Model B has maximum fragmentation -- N product versions across M environment configurations, with the ISV unable to force upgrades. Model C achieves moderate fragmentation by splitting the surface: the control plane (ISV-controlled) can be updated on the ISV's release cycle, while the data plane (customer-gated) fragments across versions. This split means the ISV's highest-velocity components (AI capabilities, analytics, management UI) remain on a single version, while only the lower-velocity data-plane components fragment.

**Regulatory reach** is the dimension where Model B uniquely excels. Model B supports ITAR, IL4-IL6, and air-gapped environments that are architecturally incompatible with Models A and C. Model C achieves most regulatory requirements (GDPR data sovereignty, HIPAA with BAA, FedRAMP with split boundary) but cannot serve the [approximately 34% of software vendors' customers who require air-gap](https://www.replicated.com/blog/on-prem-sales-and-demand-are-rising). For ISVs targeting the defense and intelligence community, Model B is not optional.

**Support cost scaling** is the dimension with the largest long-term economic impact. Model A achieves sub-linear scaling inherently (shared infrastructure, unilateral diagnostics). Model B scales linearly (each customer is an isolated failure domain with bilateral support). Model C achieves sub-linear scaling through the shared telemetry channel and fleet-wide agent improvements, but only after sufficient customer count (approximately 15+) for the sub-linear component to dominate the linear component. Below 15 customers, Model C's support cost scaling behaves more like Model B than Model A.

---

## Chapter 11: ISV Decision Framework

### Decision 1: Invest or Not?

The decision reduces to one variable: the nature of the ISV's on-prem demand.

**Regulatory-gated demand (ITAR, FedRAMP, HIPAA on-prem, EU Data Act, IL4-IL6):** Invest. The revenue is binary -- inaccessible without on-prem capability. No amount of SaaS excellence captures a customer who legally cannot use SaaS. Model C is the deployment model unless the customer is air-gapped. Target 5 enterprise customers within 12 months of Phase 2 launch for financial viability.

**Preference-driven demand (cost optimization, control, repatriation trend):** Evaluate using the scoring matrix (S22). Score the ISV on six weighted factors: ACV (2x weight), [regulated pipeline percentage](https://www.kiteworks.com/gdpr-compliance/european-saas-data-sovereignty-rfps/) (2x), Kubernetes engineering depth (1.5x), existing on-prem customers (1.5x), product architecture (1x), and competitive pressure (1x). Minimum viable score for investment: 15 out of 30. Score 24-30: strong invest. Score 18-23: conditional invest with pilot gate. Score 15-17: marginal, invest only with specific deal pipeline. Score below 15: do not invest.

**No demonstrated demand:** Do not invest. The cloud marketplace channel dominates for ISVs without customer-driven on-prem requirements.

### Decision 2: Which Model?

Model C for all customers with network connectivity. Model B only for air-gapped customers. If air-gapped demand exceeds 20% of pipeline, maintain both tracks. If below 20%, start with Model C and add Model B later when specific air-gapped deals justify the investment.

### Decision 3: When?

The [12-24 month investment window](https://www.useluminix.com/reports/industry-analysis/ai-on-premise-future) (March 2026 - March 2028) is defined by three factors: open-weight model convergence at peak, CNCF tooling maturing to production, and cloud ecosystem compounding not yet unbridgeable. Invest now if demand is regulatory-gated. Invest within 12 months if scoring matrix yields 18+. Monitor and defer if scoring is 15-17.

### Decision 4: How? (Implementation Sequencing)

Six-phase gate model with explicit abandon criteria:

**Phase 0 (Assessment, 4-6 weeks, $25K-$50K):** Run scoring matrix. Secure 2+ warm customer commitments. Abandon if score below 15 or no customer pipeline.

**Phase 1 (Refactoring, 6-9 months, $235K-$550K for Model C):** Product runs on 2+ Kubernetes distributions. Licensing resolved. Apache 2.0-only dependency policy implemented where feasible. Abandon if blocking licensing dependencies cannot be resolved within 9 months.

**Phase 2 (Pilot, 3-6 months, $24K-$55.5K for 3 customers):** Three customers deployed and operational. Support SLA achieved. Begin diagnostic agent deployment (Phase A of agent rollout) in parallel. Abandon if fewer than 2 customers accept deployment or if support cost exceeds 3x estimate.

**Phase 3 (Scale, 6-12 months):** Eight total customers deployed. Deployment playbook documented and repeatable. Abandon if per-customer deployment cost exceeds 2x estimate or if pilot customers churn.

**Phase 4 (Agents, 6-12 months, $150K-$420K/year):** Diagnostic and health monitoring agents deployed. Support cost reduction measurable and positive. Abandon if agent infrastructure cost exceeds support savings or if customer agent deployment acceptance rate drops below 50%.

**Phase 5 (Steady State, ongoing):** Annual review cycle. Assess margin (target 60%+ for Model C), demand pipeline health, competitive position, and parity drift. Evaluate expanding to Model B track for air-gapped customers if demand warrants.

### Decision 5: Pricing

Recommended pricing tiers based on the economic model:

- Standard on-prem (connected, non-regulated): 1.3x-1.5x ACV premium. Includes Model C deployment, standard support, diagnostic agents.
- Regulated on-prem (HIPAA, FedRAMP, EU sovereignty): 1.5x-2.0x premium. Includes Model C + compliance documentation + BAA + per-customer anonymization assessment.
- Air-gapped: 2.0x-2.5x premium. Includes Model B + dedicated support track + Zarf packaging + on-site deployment engineering.

The minimum viable premium at 50% AI compression is below 1.0x for Model C, meaning the ISV can theoretically price on-prem at SaaS parity and still generate positive contribution margin. However, pricing at parity forfeits the margin upside that funds the incremental engineering team. The recommended 1.3x-1.5x range provides margin headroom while remaining competitive with enterprise customer expectations.

### Anti-Patterns

Eight anti-patterns identified by the research, listed in order of economic impact:

1. **No ACV premium.** Without a premium, on-prem is margin-dilutive unless AI support compression exceeds 50%. Even with AI, parity pricing eliminates the margin buffer needed to fund the engineering team.

2. **Model B default.** Deploying full on-prem when the customer has network connectivity. Model C dominates on every metric. Model B should be reserved exclusively for air-gapped environments.

3. **Delaying AI integration.** AI support automation is not a future optimization; it is the economic foundation of on-prem viability. Start diagnostic agent deployment concurrent with Phase 2 customer pilots.

4. **SaaS feature parity goal.** Attempting to ship every SaaS feature to on-prem creates a 42% parity drift over 24 months. Accept a feature subset on the data plane; the control plane carries full features.

5. **Phase 1 scope creep.** Refactoring all 12 AWS managed services when only 5-7 are on Model C's data plane. Identify the Model C boundary first; refactor only data-plane services.

6. **Big-bang agent deployment.** Deploying autonomous agents before establishing trust through diagnostic-only mode. Only 6% of companies fully trust AI agents for core processes. Phased rollout is mandatory.

7. **Ignoring licensing.** MinIO archived, Vault BSL, ScyllaDB source-available, MongoDB SSPL. Legal review must begin in Phase 1 month 1, not when the engineering team discovers the dependency.

8. **Over-investing in air-gap.** Air-gap roughly doubles engineering investment. Justify with 3+ confirmed air-gapped customers before building the parallel track.

---

## Chapter 12: Conclusions and Strategic Implications

### Case Study Validation

The four ISV case studies (Confluent, GitLab, HashiCorp, Elastic) provide empirical validation for several of the research's key findings while revealing one significant caveat.

**Validation 1: Self-managed revenue is durable, not declining.** Across all four ISVs, self-managed revenue continues to grow in absolute terms even as cloud revenue grows 2-3x faster. [Confluent Platform generated approximately $496M in annual subscription revenue and grew 14% year-over-year](https://www.fool.com/earnings/call-transcripts/2025/10/28/confluent-cflt-q3-2025-earnings-call-transcript/). [GitLab derives approximately 70% of its $759M FY2025 revenue from self-managed customers](https://ir.gitlab.com/news/news-details/2025/GitLab-Reports-Fourth-Quarter-and-Full-Fiscal-Year-2025-Financial-Results/default.aspx). [HashiCorp's self-managed revenue comprised approximately 83% of its $583M annual revenue](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001832526&type=10-K) at the time of IBM's acquisition. [Elastic's self-managed revenue implies 9-13% annual growth even as cloud reaches 49% of quarterly revenue](https://ir.elastic.co/news/news-details/2025/Elastic-Reports-Third-Quarter-Fiscal-2025-Financial-Results/default.aspx). The consistent demand driver across all four ISVs is regulated industries: financial services, government, and healthcare.

**Validation 2: The split-plane architecture is converging as the industry standard.** Both Elastic (Cloud Connect for EIS) and GitLab (Cloud Connector and AI Gateway) independently converged on the same hybrid split-plane pattern: customer data stays on-prem, compute-intensive AI operations execute in the ISV's cloud. Elastic's implementation routes raw text payloads to cloud GPU infrastructure for inference, discards the text after processing, and returns only embedding vectors to the customer environment. GitLab's implementation routes self-managed AI requests through a JWT-authenticated bridge to GitLab's cloud LLM backends. Confluent's WarpStream acquisition provides a BYOC (Bring Your Own Cloud) model with similar architectural properties. This independent convergence by three different ISVs provides strong validation for Model C as the preferred architectural pattern.

**Validation 3: Licensing creates a durable but depreciating moat.** BSL, SSPL, and Community License changes protected HashiCorp, Elastic, and Confluent from cloud provider commoditization, but at significant community cost. [OpenTofu garnered 33,000 GitHub stars and 140 corporate backers](https://opentofu.org/blog/opentofu-announces-fork-of-terraform/) within a month of HashiCorp's BSL announcement. Elastic had to reverse course (adding AGPLv3) once the AWS fork was contained. The research estimates that restrictive licensing buys 2-4 years of competitive protection before open-source alternatives mature sufficiently to erode the moat.

**Significant caveat: HashiCorp's failure to achieve profitability.** HashiCorp never achieved GAAP profitability at $583M annual revenue with 83% self-managed revenue share. Its net dollar retention rate declined from 133% to 109% over two years, and its acquisition price represented a 49.65% decline from IPO market cap. This outcome directly challenges the thesis that on-prem deployment is economically viable for standalone ISVs. The reconciliation is that HashiCorp's cost structure -- engineering for 8+ products across N environments without the AI support automation documented in this research -- represents the pre-AI economic model. The research's finding that AI support compression of 30-50% can transform on-prem economics from margin-dilutive to margin-accretive was not available to HashiCorp during its public company period. IBM's acquisition validates that the revenue base is valuable, but the standalone operating model was not sustainable at HashiCorp's cost structure.

**IBM's acquisitions ($17.4B combined for [HashiCorp](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform) and [Confluent](https://www.fool.com/earnings/call-transcripts/2025/10/28/confluent-cflt-q3-2025-earnings-call-transcript/)) validate hybrid portfolio value.** IBM's rationale was embedding Terraform, Vault, and Confluent Platform into Red Hat OpenShift, Ansible, IBM Z, and watsonx -- leveraging IBM's 95% Fortune 500 penetration versus Confluent's 40%. For standalone ISVs without IBM's enterprise distribution, the case studies suggest that on-prem viability requires either (a) AI support automation to compress the cost structure, (b) sufficient ACV premium to offset the higher support costs, or (c) a strategic acquirer who can extract value from the hybrid portfolio that the standalone ISV cannot.

### The Structural Paradox, Resolved

This research began with a question: does agentic AI change the fundamental economics of ISV on-premises deployment? The answer is yes, but the change is bidirectional. AI makes on-prem better (support cost compression, distributed agent moat, margin improvement) while simultaneously making SaaS even better (productivity advantage, ecosystem compounding, marketplace channel growth).

The paradox does not resolve into a universal recommendation. It resolves into a demand-type segmentation:

**For regulatory-gated demand, on-prem investment is clearly rational.** The revenue is binary -- no SaaS alternative exists. Model C with AI agents breaks even at 3-4 customers, achieves 68%+ gross margins at 50 customers, and creates a competitive moat via aggregate telemetry that open-source self-hosters cannot replicate. The ISV that invests now captures a structural revenue stream that grows more defensible over time as the trust stack, regulatory documentation, and diagnostic AI improve.

**For preference-driven demand, SaaS-only is the higher-return strategy.** The cloud compounding advantage makes SaaS engineering 30-35% more productive. The marketplace channel ($163B projected by 2030) provides distribution leverage unavailable to on-prem products. The 1-point scoring difference between Model A (26/35) and Model C (27/35) is within noise for ISVs without regulatory-gated customers. The engineering investment in on-prem ($235K-$550K fixed plus $3-6.5 FTE ongoing) competes directly with SaaS feature velocity.

**For ISVs with mixed demand (some regulatory, some preference), Model C provides a hedge.** The split-plane architecture preserves the SaaS business (control plane continues to evolve at cloud velocity) while adding on-prem capability for the data plane. IBM's acquisitions of HashiCorp ($6.4B) and Confluent ($11B) demonstrate that hybrid portfolios command premium multiples -- the ability to serve both cloud and on-prem customers from a single product platform is a strategic asset.

### The Pricing Paradox

The case study evidence reveals a tension in on-prem pricing strategy that the economic model alone cannot resolve.

[GitLab charges identical per-seat prices](https://about.gitlab.com/pricing/) for self-managed and SaaS ($348/year Premium, $1,188/year Ultimate). This parity pricing contradicts the research's finding that 1.3x-2.0x ACV premiums are needed to offset on-prem support cost differentials. GitLab absorbs the support cost differential rather than pricing it through, which contributes to its margin structure lagging pure SaaS companies. The strategic logic may be that with 70% of revenue from self-managed, any price increase risks triggering competitive switching in the installed base.

[Elastic increased self-managed pricing by 30% in May 2025](https://ir.elastic.co/news/news-details/2025/Elastic-Reports-Third-Quarter-Fiscal-2025-Financial-Results/default.aspx), explicitly creating a price gap between deployment models. This pricing action was possible because Elastic's cloud share has reached 49%, reducing dependence on self-managed revenue and enabling the ISV to use pricing as a migration incentive.

Confluent's pricing structure does not publicly differentiate by deployment model, but the acquisition by IBM at $11B validates that the market valued the combined SaaS + on-prem portfolio at a premium.

[Atlassian provides a precedent for aggressive on-prem premium pricing](https://us.seibert.group/blog/atlassian-data-center-prices-are-increasing-in-2025-what-you-need-to-know): Data Center products carry a significant premium over cloud equivalents, with prices increasing substantially in 2025. Atlassian's approach is explicit: on-prem is priced as a premium offering to fund the engineering investment while incentivizing cloud migration.

The ISV's pricing strategy should be informed by its position in the cloud transition arc. Early in the transition (self-managed >60% of revenue), parity pricing may be necessary to avoid disrupting the installed base. As cloud share grows beyond 50%, the ISV gains pricing power to introduce on-prem premiums that reflect the true cost of delivery. The research recommends starting with a 1.3x-1.5x premium for new on-prem customers while maintaining parity for existing customers, then gradually aligning pricing as the customer base migrates.

### Three Strategic Postures

**Posture 1: Regulatory-First (invest now).** For ISVs where 25%+ of pipeline is regulation-gated. Invest in Model C immediately. Begin Phase 1 refactoring with an Apache 2.0-only dependency policy. Deploy pilot customers in months 6-9. Launch diagnostic agents concurrent with Phase 2. Target 5 enterprise customers within 12 months. The distributed agent runtime is both the economic enabler (AI support compression makes margins work) and the competitive moat (aggregate telemetry, operational AI, trust infrastructure).

**Posture 2: Opportunistic (conditional investment).** For ISVs where 10-25% of pipeline is regulation-gated. Run the scoring matrix. If score >= 18, invest in Model C with a 2-3 customer pilot gate. Structure Phase 0 as a customer co-development program: the first 2-3 customers fund Phase 1 through design-partner agreements or upfront ACV commitments. This de-risks the fixed investment by securing revenue commitments before engineering begins. If score < 18, defer for 12 months and reassess as CNCF tooling matures.

**Posture 3: SaaS-Only (do not invest).** For ISVs with no regulatory-gated demand. Focus engineering investment on SaaS product velocity and cloud marketplace integration. The cloud compounding advantage makes this the highest-return strategy for ISVs whose customers can use SaaS. Monitor the market for shifts in demand type (new regulations, customer requirements changes, competitive moves) that would trigger a re-evaluation.

### Build vs. Buy vs. Partner Decision

The research evaluated each component of the on-prem deployment stack on a build/buy/partner spectrum:

**Build (ISV-specific, no vendor can do this):** Product refactoring (Phase 1), deployment engineering (ISV-specific deployment playbook), support tooling (ISV-specific diagnostic models), cross-distribution testing (no vendor offers automated cross-distro validation), and trust stack composition (SLSA + Cosign + Kyverno integration). These components are inherently ISV-specific because they require deep knowledge of the ISV's product architecture, failure modes, and customer environments.

**Buy (mature vendor solutions exist):** Distribution packaging ([Replicated at $50-$200/customer/month](https://www.replicated.com/pricing), or [Distr](https://glasskube.dev/) open-source), air-gap packaging ([Zarf](https://zarf.dev/)), on-prem LLM inference ([vLLM](https://docs.vllm.ai/)/[SGLang](https://sgl-project.github.io/) with open-weight models), and fleet management ([Rancher Fleet](https://fleet.rancher.io/) or [Argo CD](https://argo-cd.readthedocs.io/en/stable/)). These components are infrastructure-level and not ISV-specific. Buying is strongly preferred over building because the engineering investment to replicate these capabilities is substantially higher than the licensing cost.

**Partner (SI or cloud provider for initial deployments):** Deployment engineering for the first 3-5 customers can be partially outsourced to a systems integrator with Kubernetes expertise. Cloud provider validation programs (EKS Anywhere validation, OpenShift certification) provide structured paths for cross-distribution testing. These partnerships de-risk early deployments when the ISV's internal Kubernetes expertise is limited.

**Track (not yet production-ready):** Agent runtime platform (kagent not production-ready; evaluate Solo Enterprise when it matures), agent sandbox isolation (Agent Sandbox at v1alpha1; integrate when v1beta1 ships), and Kubernetes MCP integration (Red Hat K8s MCP / containers/kubernetes-mcp-server, production expected H2 2026). These components should be tracked and prototyped against but not deployed to production until they reach at least v1beta1.

**Defer (no production framework exists):** Federated learning for cross-customer models (gradient inversion risk, no production framework), autonomous agent orchestration (40% project cancellation predicted by Gartner; start with diagnostic-only), and cross-distribution automated testing (no vendor provides this; build manual validation pipeline first).

The build/buy/partner analysis reveals that the ISV's primary engineering investment should focus on the ISV-specific components (product refactoring, diagnostic models, trust stack) rather than infrastructure components where mature vendor solutions exist. The common mistake is building distribution or fleet management tooling in-house when Replicated and Rancher Fleet provide production-grade solutions at a fraction of the engineering cost.

### The 24-Month Clock

The investment window is defined by the convergence of three temporary conditions:

First, open-weight model capability is at its peak convergence with proprietary models. The [MMLU gap has collapsed to 0.3 points](https://arxiv.org/abs/2412.04315). [DeepSeek V3](https://github.com/deepseek-ai/DeepSeek-V3) reaches 95%+ of GPT-4o performance. [Qwen3](https://qwenlm.github.io/blog/qwen3/), [DeepSeek R1](https://github.com/deepseek-ai/DeepSeek-R1), and [Phi-4](https://huggingface.co/microsoft/phi-4) are all available under permissive licenses. On-prem LLM inference is viable today. This convergence may plateau (as suggested by the flattening of open-source adoption to 13%), but it is unlikely to significantly widen given the competitive dynamics.

Second, CNCF agentic tooling is on a 12-18 month maturity trajectory. kagent is projected to reach CNCF Incubating status by Q2 2027. Agent Sandbox is projected to reach v1beta1 by Q1 2027. The CNCF AI Conformance Program plans v2.0 for 2026. ISVs that start building on these projects today will have production-grade agent infrastructure by the time the projects stabilize. ISVs that wait until v1.0 GA will be 12-18 months behind.

Third, cloud ecosystem compounding has not yet made the on-prem gap unbridgeable. The [$470B+ in committed cloud spend](https://www.platformonomics.com/2024/06/follow-the-capex-the-cloud-hyperscaler-investment-cycle/), the [60+ AWS MCP servers](https://www.marktechpost.com/2025/07/20/model-context-protocol-mcp-for-enterprises-secure-integration-with-aws-azure-and-google-cloud-2025-update/), the [30-35% productivity gap](https://softwareengineeringproductivity.stanford.edu/ai-impact) -- these are significant advantages, but they are not yet so large that a well-funded ISV with Kubernetes expertise cannot build competitive on-prem capability. Every month of delay adds to these compounding advantages. By 2028-2029, the gap may be large enough that on-prem engineering requires fundamentally more investment for fundamentally less return.

For ISVs with regulatory-gated demand, the investment is economically rational today. The clock is a planning consideration, not a blocking concern.

For ISVs with preference-driven demand, the clock is the critical constraint. Investing now captures the window while conditions are favorable. Waiting increases the risk that the gap widens beyond cost-effective closure. But investing without validated demand risks stranding the fixed investment.

The research cannot make this decision for the ISV. It can only provide the framework, the data, and the analysis. The decision is the ISV's.

### What This Research Does Not Address

Several important topics are outside the scope of this research and should not be inferred from its findings:

**Product-market fit.** This research assumes the ISV's SaaS product has demonstrated market demand and that specific customers are requesting on-prem deployment. It does not evaluate whether the product is suitable for on-prem deployment in the first place. Products with deep cloud-native architecture dependencies (real-time collaborative features, multi-tenant data pipelines, serverless compute patterns) may require more fundamental architectural changes than the Phase 1 refactoring scope described here.

**Organizational change management.** The research addresses engineering economics and architecture but does not address the organizational challenges of shifting a SaaS engineering team to support on-prem deployment: hiring Kubernetes expertise, building support operations capability, establishing customer deployment processes, and managing the cultural tension between SaaS velocity and on-prem stability. These organizational factors can be more determinative than the economic analysis.

**Customer acquisition cost for on-prem.** The economic model assumes customers arrive at a specified ACV. It does not model the sales cycle differences between SaaS and on-prem deals, which typically involve longer cycles, more stakeholders, security reviews, and proof-of-concept deployments. The customer acquisition cost for on-prem enterprise deals is typically 2-3x higher than SaaS self-serve, which further shifts the break-even analysis.

**Multi-cloud and edge deployment.** The research focuses on the ISV cloud-to-customer-Kubernetes deployment vector. It does not address multi-cloud strategies (deploying the ISV product across AWS, Azure, and GCP simultaneously), edge deployment patterns (IoT, manufacturing, retail), or bare-metal deployment (non-Kubernetes infrastructure). These deployment targets have different economics and architecture considerations.

**International regulatory variation.** While the research references GDPR, HIPAA, ITAR, and FedRAMP, it does not provide a comprehensive analysis of regulatory requirements by jurisdiction. ISVs targeting specific regulated markets (Chinese cybersecurity law, Japanese APPI, Brazilian LGPD, Indian DPDP) should commission jurisdiction-specific legal analysis.

---

## Appendices

### Appendix A: Research Methodology

This research employed 80 parallel research agents across 10 thematic waves, each producing 3,000-5,000 word analytical files with inline citation URLs. All sources were restricted to 2025-2026 publication dates to ensure recency. Three quality gates were applied per wave:

- **G1 (Structural Completeness):** Every file contains the required sections, meets minimum word count, and includes inline citations.
- **G2 (Citation Quality):** Minimum threshold of inline URLs per file, source recency verification, no hallucinated URLs (verified via sampling).
- **G3 (Content Review):** Each file scored PASS or MINOR_ISSUES against accuracy, specificity, and analytical depth criteria.

All 10 waves passed all three gates. Across the 80 files, 10 received MINOR_ISSUES scores (deferred to synthesis for resolution); the remaining 70 received PASS scores.

Synthesis followed a three-layer structure:
- **Layer 1 (S01-S10):** Per-wave thematic summaries consolidating findings across agents within each wave.
- **Layer 2 (S11-S16):** Cross-domain integrations organized by lifecycle phase (Phase 1: S11; Phase 2: S12; Phase 3: S13; Distributed Agents: S14; Economics: S15; Master: S16).
- **Layer 3 (S17-S24):** Exhibits (S17-S22), comparison matrix (S23), and this final document (S24).

### Appendix B: Source Coverage

| Wave | Focus | Agents | Words | Citations |
|------|-------|--------|-------|-----------|
| 1 | Managed Service Replacements | F01-F12 | ~54,400 | 1,215 |
| 2 | AI Refactoring Capabilities | F13-F19 | ~31,600 | 672 |
| 3 | Split-Plane Architecture | F20-F27 | ~33,000 | 783 |
| 4 | Distribution & Deployment | F28-F36 | ~37,800 | 839 |
| 5 | Support Economics | F37-F44 | ~36,900 | 751 |
| 6 | Distributed Agent Architecture | F45-F53 | ~41,200 | 913 |
| 7 | Agent Implementation | F54-F61 | ~38,700 | 820 |
| 8 | Business & Competitive Economics | F62-F65 | ~20,100 | 442 |
| 9 | AI Trajectory & Ecosystem | F66-F74 | ~39,200 | 812 |
| 10 | Case Studies & Economic Validation | F75-F80 | ~38,500 | 447 |
| **Total** | | **80 agents** | **~371,400** | **7,694** |

### Appendix C: Exhibit Index

| Exhibit | File | Content |
|---------|------|---------|
| S17 | exhibit1_service_replacement_matrix.md | 12-domain managed service replacement maturity matrix with licensing, CNCF status, AI leverage, and cross-domain dependencies |
| S18 | exhibit2_lifecycle_cost_matrix.md | Lifecycle cost by phase and deployment model at 10, 50, and 100 customer thresholds |
| S19 | exhibit3_economic_model.md | Differential break-even analysis with 10 scenarios and sensitivity tables |
| S20 | exhibit4_tooling_landscape.md | Agentic tooling landscape map covering AI development tools, distribution platforms, CNCF infrastructure, and ecosystem asymmetries |
| S21 | exhibit5_distributed_agent_architecture.md | 6-layer agent architecture with data flows, cost model, trust stack, agent catalog, and implementation sequencing |
| S22 | exhibit6_decision_framework.md | ISV decision framework with scoring matrix, phase gates, pricing tiers, build/buy/partner assessment, and anti-patterns |
| S23 | comparison_matrix.md | Model A vs. B vs. C across 40+ dimensions in 8 categories with summary scorecard |

### Appendix D: Key Abbreviations

| Abbreviation | Definition |
|-------------|------------|
| ACV | Annual Contract Value |
| BAA | Business Associate Agreement (HIPAA) |
| BSL | Business Source License |
| CNCF | Cloud Native Computing Foundation |
| CRD | Custom Resource Definition |
| CSI | Container Storage Interface |
| CNI | Container Networking Interface |
| DLP | Data Loss Prevention |
| EDP | Enterprise Discount Program (AWS/Azure) |
| FTE | Full-Time Equivalent |
| ISV | Independent Software Vendor |
| LLM | Large Language Model |
| MACC | Microsoft Azure Consumption Commitment |
| MCP | Model Context Protocol |
| MTTR | Mean Time to Resolve |
| MTTD | Mean Time to Detect |
| OPA | Open Policy Agent |
| OTel | OpenTelemetry |
| SCC | Security Context Constraint (OpenShift) |
| SLSA | Supply chain Levels for Software Artifacts |
| SSPL | Server Side Public License |
| SRE | Site Reliability Engineering |
| TEE | Trusted Execution Environment |
| BYOC | Bring Your Own Cloud |
| GA | General Availability |
| GPU | Graphics Processing Unit |
| RAG | Retrieval Augmented Generation |
| OCI | Open Container Initiative |
| eBPF | Extended Berkeley Packet Filter |
| DPA | Data Processing Agreement |
| NDRR | Net Dollar Retention Rate |
