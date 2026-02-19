# W06S — On-Premises Infrastructure: Cross-Agent Synthesis

**Synthesis Date:** 2026-02-19
**Input Files:** F39 (Compute), F40 (Networking), F41 (Relational DB), F42 (NoSQL/Caching), F43 (Object Storage), F44 (Message Queues), F45 (Vector DB), F46 (IAM/Identity), F47 (Secrets/Certs), F48 (CI/CD), F49 (Logging), F50 (Monitoring), F51 (Tracing)
**Scope:** On-premises infrastructure domains evaluated for ISV deployment model comparison (on-premises vs. managed Kubernetes vs. cloud-native)

---

## 1. Executive Summary

Operating the full on-premises infrastructure stack for an AI-driven multi-tenant SaaS product requires an estimated 22.05--42.25 FTE in aggregate across 13 domains, compared to 10.70--18.45 FTE on managed Kubernetes and 2.15--4.90 FTE on cloud-native managed services. The labor gap is not merely one of scale; it reflects a qualitative shift in the type of work performed. On-premises teams spend the majority of their capacity on undifferentiated infrastructure maintenance -- [Vault unseal automation](https://developer.hashicorp.com/vault/docs/concepts/seal) (from F47), [Elasticsearch JVM heap tuning at the 32 GB compressed OOP ceiling](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics) (from F49), [Prometheus cardinality governance at 3 kB RAM per active time series](https://signoz.io/guides/why-does-prometheus-consume-so-much-memory/) (from F50) -- while cloud-native teams redirect equivalent capacity toward application logic and customer-facing features. Five cross-cutting themes emerge: (1) hardware economics favor on-premises only at sustained high utilization; (2) security and identity consume disproportionate FTE; (3) mandatory migrations create compounding risk windows; (4) observability stacks achieve the largest cost reduction on-premises but at the highest operational burden; and (5) data services exhibit a clear cost-crossover threshold below which managed services are more economical.

---

## 2. Key Themes

### Theme 1: Hardware Economics Favor On-Premises Only at Sustained High Utilization

The capital expenditure case for on-premises infrastructure is real but narrow. [H100 GPUs cost $25K--$40K per unit, with DGX H100 systems at $373K--$450K](https://gmicloud.ai/resources/how-much-does-a-gpu-server-cost-a-comprehensive-guide/) (from F39), and [break-even against cloud GPU instances requires 60--70% sustained utilization](https://monovm.com/blog/gpu-cloud-vs-on-premise/) (from F39). Procurement lead times of 5--6 months and power/cooling infrastructure at [$5--$15M CapEx for 50 enterprise tenants](https://introl.com/data-center-design-build/how-much-does-it-cost-to-build-a-data-center/) (from F39) create a planning horizon incompatible with startup-stage ISVs. The [VMware post-Broadcom-acquisition price increases of 8--15x](https://www.broadcomaudits.com/broadcom-vmware-price-increase-a-comprehensive-guide/) (from F39) compound the problem by eliminating the previously dominant hypervisor without a frictionless open-source alternative (KVM/Proxmox require deeper Linux expertise). Object storage shows a parallel pattern: [MinIO at $96K/year AIStor licensing](https://min.io/pricing) (from F43) versus Ceph at higher operational complexity (4/5 difficulty) but no license cost -- neither approaches the zero-ops profile of S3 at [eleven nines of durability](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html) (from F43).

### Theme 2: Security and Identity Consume Disproportionate FTE with Double-Counting Risk

IAM and secrets/certificates together require [2.75--4.75 FTE](https://identitymanagementinstitute.org/building-a-robust-iam-team/) (from F46) and [2.5--5.0 FTE](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-reference-architecture) (from F47) respectively -- a combined 5.25--9.75 FTE that represents 24--23% of the total on-premises headcount. F46 explicitly describes IAM as "a product line, not an infrastructure dependency," with seven sub-domains each rated 3--4/5 difficulty. The [OPA uncertainty from Apple's acquisition of the maintainer team](https://www.osohq.com/learn/opa-vs-cedar-vs-zanzibar) (from F46) creates a policy-engine risk that compounds the [FIPS 140-2 certificate expiry deadline of September 2026](https://developer.hashicorp.com/vault/tutorials/archive/seal-wrap) (from F47). HSM procurement at [$5K--$50K per unit](https://developer.hashicorp.com/vault/tutorials/archive/seal-wrap) (from F47) adds capital cost to what is already the most labor-intensive pair of domains.

**G3 Warning -- FTE Double-Counting:** The F46 IAM estimate (2.75--4.75 FTE) and F47 secrets/certs estimate (2.5--5.0 FTE) have overlapping scope in service-to-service mTLS, certificate rotation, and workload identity. Additionally, Wave 10's F71 (Security Operations/SOC) will cover security monitoring that partially overlaps with F46 audit/compliance (0.5--1.0 FTE) and F47 encryption monitoring. Downstream synthesis must de-duplicate by approximately 1.0--2.0 FTE when aggregating security-domain totals to avoid overstating headcount.

### Theme 3: Mandatory Technology Migrations Create Compounding Risk Windows

Multiple technologies covered across these 13 files face simultaneous migration deadlines or deprecations:
- [Kafka 4.0 mandatory ZooKeeper-to-KRaft migration](https://kafka.apache.org/documentation/) (from F44) -- irreversible, requires cluster-wide rolling upgrade
- [FIPS 140-2 certificates expire September 2026](https://developer.hashicorp.com/vault/tutorials/archive/seal-wrap) (from F47) -- HSM firmware and Vault seal configurations must transition to FIPS 140-3
- [Jaeger v1 deprecated January 2026](https://www.cncf.io/blog/2025/09/01/jaeger-at-10-forged-in-community-reborn-in-opentelemetry/) (from F51) -- migration to v2 (OTel Collector-based) required
- [Ingress-NGINX EOL March 2026](https://kubernetes.github.io/ingress-nginx/) (from F40) -- replacement with Gateway API or alternative ingress controller needed
- [Milvus 2.6 Woodpecker WAL replacing Pulsar dependency](https://milvus.io/docs) (from F45) -- architecture change affecting vector DB storage layer
- [Jenkins published nine security advisories in 2025](https://www.jenkins.io/security/advisories/) (from F48) -- continuous patching cadence with no end in sight

ISVs running on-premises infrastructure must plan for these migrations simultaneously. The compounding effect is that each migration consumes FTE from the same limited pool of platform engineers, and several (Kafka KRaft, FIPS 140-3) are irreversible once initiated.

### Theme 4: Observability Achieves the Largest Cost Reduction On-Premises but at the Highest Operational Burden

Self-hosted logging, monitoring, and tracing collectively offer the strongest economic case for on-premises deployment at scale. [Self-hosted Loki at 100 GB/day costs ~$300/month versus $1,665/month for CloudWatch](https://oneuptime.com/blog/post/2026-01-21-loki-vs-cloudwatch/view) (from F49) -- a 75--90% reduction. [Self-hosted Prometheus at 1M samples/sec costs ~$6K/month versus $47K for AWS Managed Prometheus or $327K for GCP Managed Prometheus](https://victoriametrics.com/blog/managed-prometheus-pricing/) (from F50). The [cost crossover point for logging sits at 50--100 GB/day](https://oneuptime.com/blog/post/2026-01-21-loki-vs-cloudwatch/view) (from F49) -- below this threshold, managed services are cost-competitive.

However, the combined observability FTE (logging 1.5--2.0 + monitoring 1.5--2.5 + tracing 1.6--2.5 = 4.6--7.0 FTE on-premises) represents a substantial team that must manage [Elasticsearch shard sizing at 10--50 GB targets](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards) (from F49), [Thanos/Mimir distributed architecture](https://prometheus.io/docs/prometheus/latest/storage/) (from F50), and [Jaeger v2 storage backend migrations](https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/) (from F51) concurrently. The [OpenTelemetry consistent probability sampling specification (October 2025)](https://opentelemetry.io/) (from F51) provides a unifying framework but does not reduce the infrastructure management burden.

### Theme 5: Data Services Exhibit Clear Cost-Crossover Thresholds

Multiple data infrastructure domains show a volume-dependent breakpoint where on-premises ownership becomes economically justified:
- **Vector DB:** [Cost crossover at ~50 million vectors](https://milvus.io/docs) (from F45), below which managed services (Pinecone, Zilliz Cloud) are more economical despite 2--4x per-query pricing
- **Logging:** [Crossover at 50--100 GB/day](https://oneuptime.com/blog/post/2026-01-21-loki-vs-cloudwatch/view) (from F49)
- **NoSQL/Caching:** Self-hosted FTE costs [often eliminate 40--60% of infrastructure savings](https://www.elastic.co/pricing) (from F42) -- Elasticsearch at 5/5 difficulty, MongoDB at 4/5, Redis at 4/5
- **Message Queues:** [Kafka requires 1.5--2.5 FTE on-premises (4x managed)](https://kafka.apache.org/documentation/) (from F44); [NATS at 0.3--0.6 FTE](https://docs.nats.io/) (from F44) provides lowest operational burden but lacks Kafka's ecosystem breadth

Below these thresholds, the labor cost of maintaining on-premises infrastructure exceeds the managed service premium. ISVs must model their expected data volumes against these crossover points before committing to self-hosted infrastructure.

---

## 3. Difficulty and FTE Summary Table

| Domain | Agent | On-Prem Difficulty | On-Prem FTE | Managed K8s FTE | Cloud-Native FTE |
|---|---|---|---|---|---|
| Compute Management | F39 | 4--5/5 | 2.5--5.0 | 1.0--2.25 | 0.2--0.5 |
| Networking | F40 | 3--4/5 | 1.75--3.5 | 0.75--1.75 | 0.1--0.7 |
| Relational DB (PostgreSQL) | F41 | 4/5 | 1.5--3.0 | 0.85--1.25 | 0.25--0.5 |
| NoSQL & Caching | F42 | 4--5/5 | 1.2--2.0 | 0.9--1.3 | 0.2--0.45 |
| Object Storage | F43 | 2--4/5 | 0.5--2.0 | 0.3--0.75 | 0.05--0.1 |
| Message Queues | F44 | 4/5 | 1.5--2.5 | 1.0--1.5 | 0.3--0.5 |
| Vector DB | F45 | 4/5 | 1.25--1.75 | 0.6--0.85 | 0.05--0.1 |
| IAM & Identity | F46 | 3--4/5 | 2.75--4.75 | 1.65--2.65 | 0.30--0.80 |
| Secrets, Certs & Encryption | F47 | 4--5/5 | 2.5--5.0 | 0.4--0.85 | 0.4--0.85 |
| CI/CD Pipelines | F48 | 3--4/5 | 2.0--3.25 | 1.3--1.9 | 0.3--0.4 |
| Logging | F49 | 3--4/5 | 1.5--2.0 | 1.0--1.3 | 0.05--0.1 |
| Monitoring & Alerting | F50 | 3--4/5 | 1.5--2.5 | 1.0--1.7 | 0.3--0.6 |
| Distributed Tracing | F51 | 3--5/5 | 1.6--2.5 | 0.6--1.0 | 0.2--0.3 |
| **TOTALS (raw sum)** | | | **22.05--42.25** | **10.70--18.45** | **2.15--4.90** |
| **Adjusted (de-duplicate security)** | | | **~20--40** | **~10--17** | **~2--5** |

**Notes:** Raw totals are additive sums of per-agent estimates. The adjusted row removes approximately 1.0--2.0 FTE of security domain overlap between F46, F47, and the forthcoming F71 (Wave 10). All FTE estimates assume a mid-sized ISV (10--50 enterprise tenants, 20--50 microservices). FTE ranges across all files are marked UNVERIFIED by their respective agents due to absence of published peer-reviewed staffing benchmarks at this granularity.

---

## 4. Cross-Agent Patterns and Contradictions

**Consistent patterns across all 13 agents:**
- Every agent reports difficulty ratings of 3/5 or higher for on-premises operations, with only object storage (MinIO at 2--3/5) falling below this floor -- confirming that no on-premises infrastructure domain is operationally trivial.
- Managed Kubernetes consistently reduces FTE by 40--60% versus on-premises, while cloud-native reduces by 85--95%. The reduction is not linear: Kubernetes absorbs node lifecycle and scheduling but leaves application-level tuning (cardinality, shard sizing, policy governance) untouched.
- Elasticsearch appears as a dependency in three separate domains -- logging (F49), tracing (F51), and NoSQL (F42) -- making it the single most operationally consequential technology choice. Consolidating Elasticsearch expertise across teams is a staffing efficiency opportunity.

**Apparent contradictions or tensions:**
- F42 (NoSQL) reports that self-hosted FTE costs often eliminate 40--60% of infrastructure savings, while F49 (Logging) reports 75--90% cost reduction for self-hosted Loki versus CloudWatch. The difference is explained by data volume: logging at 100+ GB/day is high-volume commodity storage where hardware costs dominate, while NoSQL workloads require more tuning per GB.
- F50 (Monitoring) reports managed services are 7.8--54x more expensive at very high ingest, while F42 and F45 show managed services being more economical at lower volumes. This reinforces that the on-premises cost case is volume-dependent and no single recommendation applies across all domains.
- F44 (Message Queues) rates Kafka at 4/5 difficulty and 1.5--2.5 FTE, while NATS achieves similar messaging capabilities at 0.3--0.6 FTE. The Kafka ecosystem breadth (Kafka Streams, Connect, Schema Registry) explains the premium, but ISVs not requiring these features may be over-investing in infrastructure complexity.

---

## 5. Open Questions for Downstream Synthesis

1. **Aggregate cost model:** What is the fully loaded annual cost (salary + benefits + infrastructure CapEx + OpEx) for the 20--40 FTE on-premises team versus the cloud-native managed service spend at ISV scale (10--50 tenants)? The per-domain data exists but has not been modeled end-to-end.

2. **Hiring feasibility:** Can an ISV realistically recruit and retain 20--40 infrastructure specialists across all 13 domains, particularly for niche skills (Vault operations, Elasticsearch cluster management, GPU scheduling, Keycloak multi-tenancy)? F63 (Staffing & Expertise, Wave 9) should address this directly.

3. **Migration sequencing:** Given the five simultaneous mandatory migrations (Kafka KRaft, FIPS 140-3, Jaeger v2, Ingress-NGINX EOL, Milvus Woodpecker), what is the optimal sequencing, and what is the aggregate engineering effort?

4. **Kubernetes as universal substrate:** Managed Kubernetes consistently captures 40--60% of the FTE reduction without full cloud lock-in. Is there a viable architecture where managed Kubernetes plus open-source tooling provides 80% of the cloud-native benefit at 50% of the FTE cost?

5. **Security domain de-duplication:** What is the precise overlap between F46 (IAM), F47 (secrets/certs), and Wave 10's F71 (SOC operations), and what is the de-duplicated FTE total for the full security surface?

---

## 6. Sources

### F39 — On-Prem Compute Management
- [GPU server cost guide — GMI Cloud](https://gmicloud.ai/resources/how-much-does-a-gpu-server-cost-a-comprehensive-guide/)
- [Data center build costs — Introl](https://introl.com/data-center-design-build/how-much-does-it-cost-to-build-a-data-center/)
- [Broadcom VMware price increases — BroadcomAudits](https://www.broadcomaudits.com/broadcom-vmware-price-increase-a-comprehensive-guide/)
- [GPU cloud vs on-premise — MonoVM](https://monovm.com/blog/gpu-cloud-vs-on-premise/)

### F40 — On-Prem Networking
- [Ingress-NGINX — Kubernetes](https://kubernetes.github.io/ingress-nginx/)
- [CISA 2025 microsegmentation guidance](https://www.cisa.gov/zero-trust-maturity-model)

### F41 — On-Prem Relational DB
- [Patroni HA for PostgreSQL](https://patroni.readthedocs.io/)
- [PgBouncer connection pooling](https://www.pgbouncer.org/)

### F42 — On-Prem NoSQL & Caching
- [Elasticsearch pricing](https://www.elastic.co/pricing)
- [Redis documentation](https://redis.io/docs/)
- [MongoDB documentation](https://www.mongodb.com/docs/)

### F43 — On-Prem Object Storage
- [MinIO AIStor pricing](https://min.io/pricing)
- [Ceph documentation](https://docs.ceph.com/)
- [AWS S3 durability](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)

### F44 — On-Prem Message Queues
- [Apache Kafka documentation](https://kafka.apache.org/documentation/)
- [NATS documentation](https://docs.nats.io/)

### F45 — On-Prem Vector DB
- [Milvus documentation](https://milvus.io/docs)

### F46 — On-Prem IAM & Identity
- [Identity Management Institute — IAM team building](https://identitymanagementinstitute.org/building-a-robust-iam-team/)
- [OPA vs Cedar vs Zanzibar — Oso](https://www.osohq.com/learn/opa-vs-cedar-vs-zanzibar)
- [IAM TCO analysis — CloudComputing.co](https://cloudcomputing.co/en/insights/total-cost-of-ownership-considerations-for-on-premises-versus-cloud-iam-solutions/)
- [Keycloak official site](https://www.keycloak.org/)

### F47 — On-Prem Secrets, Certs & Encryption
- [Vault Raft reference architecture — HashiCorp](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-reference-architecture)
- [Vault seal/unseal — HashiCorp](https://developer.hashicorp.com/vault/docs/concepts/seal)
- [cert-manager documentation](https://cert-manager.io/docs/)

### F48 — On-Prem CI/CD Pipelines
- [Jenkins security advisories 2025](https://www.jenkins.io/security/advisories/)
- [Harbor — CNCF blog, December 2025](https://www.cncf.io/blog/2025/12/08/harbor-enterprise-grade-container-registry-for-modern-private-cloud/)
- [Woodpecker CI](https://woodpecker-ci.org/)

### F49 — On-Prem Logging
- [Elasticsearch cluster sizing — Elastic Blog](https://www.elastic.co/blog/benchmarking-and-sizing-your-elasticsearch-cluster-for-logs-and-metrics)
- [Elasticsearch shard sizing — Elastic Docs](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards)
- [Loki vs CloudWatch — OneUptime, 2026](https://oneuptime.com/blog/post/2026-01-21-loki-vs-cloudwatch/view)

### F50 — On-Prem Monitoring & Alerting
- [Prometheus storage documentation](https://prometheus.io/docs/prometheus/latest/storage/)
- [Prometheus memory usage — SigNoz](https://signoz.io/guides/why-does-prometheus-consume-so-much-memory/)
- [Managed Prometheus pricing comparison — VictoriaMetrics](https://victoriametrics.com/blog/managed-prometheus-pricing/)
- [SRE Report 2025 — Catchpoint](https://www.catchpoint.com/press-releases/the-sre-report-2025-highlighting-critical-trends-in-site-reliability-engineering)

### F51 — On-Prem Distributed Tracing
- [Jaeger v2 release — CNCF blog](https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/)
- [Jaeger at 10 — CNCF blog](https://www.cncf.io/blog/2025/09/01/jaeger-at-10-forged-in-community-reborn-in-opentelemetry/)
- [Jaeger storage backends — SigNoz](https://signoz.io/guides/what-database-does-jaeger-use/)
