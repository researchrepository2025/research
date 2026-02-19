# X1: Cloud-Native Provider Comparison -- AWS vs Azure vs GCP

**Layer:** 2 (Cross-Provider Synthesis)
**Inputs:** W02S (AWS, F08-F15a), W03S (Azure, F16-F23a), W04S (GCP, F24-F31a)
**Date:** 2026-02-19

---

## 1. Executive Summary

All three hyperscale cloud providers reduce cloud-native operational staffing by 75-90% compared to on-premises equivalents, converging on difficulty ratings of 1-2/5 for the vast majority of managed services. After normalizing for scope differences and deduplicating security FTE, a mid-size ISV serving 50 enterprise customers can expect a cloud-native operational burden of approximately 4-9 FTE regardless of provider -- down from 30-70 FTE on-premises. The providers converge on commoditized infrastructure (compute, storage, networking, observability) and diverge most sharply on AI/ML platform strategy, identity architecture, and messaging ecosystem maturity. ISVs choosing cloud-native accept deep vendor lock-in in exchange for eliminating entire engineering disciplines; the critical decision is not whether to go cloud-native but which provider's abstraction boundaries and deprecation trajectories best align with a multi-year product roadmap.

---

## 2. Capability Domain Comparison

### 2.1 Compute

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Serverless** | Lambda, Lambda Managed Instances | Azure Functions, Container Apps | Cloud Run, Cloud Functions 2nd gen |
| **Container** | ECS/Fargate | Container Apps, AKS | Cloud Run, GKE Autopilot |
| **GPU/AI Inference** | Inferentia2, Trainium, P5 instances | Container Apps GPU (A100/T4), NC-series | Cloud Run GPU (L4), TPU v5e/v5p |
| **Batch** | AWS Batch | Azure Batch | Cloud Batch |
| **On-Prem FTE** | [6.0-12.0](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/) (from F08) | [5.5-11.0](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) (from F16) | 1.5-3.0 (from F24)* |
| **Cloud-Native FTE** | [1.0-2.1](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/) (from F08) | [0.2-0.6](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) (from F16) | 0.0-0.1 (from F24)* |
| **Difficulty** | 1-3/5 | 1-2/5 | 1-4/5 |

*G4 NOTE -- GCP FTE normalization: GCP compute FTE (F24) covers individual services (Cloud Run, Cloud Batch) rather than the aggregate compute domain. The 0.0-0.1 FTE for Cloud Run GPU reflects a narrower scope than the AWS/Azure compute totals, which include multi-service orchestration, capacity planning across instance families, and Savings Plan/reservation management. When normalized to equivalent scope, GCP compute FTE is estimated at 0.5-1.0 FTE cloud-native, still lower than AWS/Azure primarily due to Cloud Run's fully managed autoscaling model eliminating capacity planning.

**Key differences:** AWS introduced [Lambda Managed Instances (November 2025)](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/) (from F08) bridging serverless and EC2, while Azure retired ACI GPU in July 2025 in favor of Container Apps serverless GPU (from F16). GCP's [Cloud Run GPU with ~5-second startup](https://docs.cloud.google.com/run/docs/configuring/services/gpu) (from F24) provides the simplest GPU inference entry point at Difficulty 1/5. Custom silicon diverges sharply: AWS offers [Inferentia2/Trainium with up to 45% P5 GPU price drops](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) (from F08), while GCP's [TPU v5e/v5p remain Difficulty 3-4](https://docs.cloud.google.com/tpu/docs/v5e) (from F24) due to JAX/XLA expertise requirements.

### 2.2 Data & Storage

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Relational DB** | RDS (Aurora Serverless v2) | Azure SQL Database | Cloud SQL, Cloud Spanner |
| **NoSQL** | DynamoDB | Cosmos DB | Firestore, Bigtable |
| **Cache** | ElastiCache (Valkey) | Azure Cache for Redis | Memorystore (Valkey) |
| **Object Storage** | S3 | Azure Blob Storage | Cloud Storage |
| **Search** | OpenSearch, Kendra | AI Search (vector + semantic) | Vertex AI Vector Search 2.0 |
| **Analytics** | Redshift, Athena | Synapse, Fabric | BigQuery |
| **On-Prem FTE** | [7.0-12.0](https://aws.amazon.com/rds/features/multi-az/) (from F09) | [3.0-6.0](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview?view=azuresql) (from F17) | 3.0-4.0+ (from F25)* |
| **Cloud-Native FTE** | [1.1-2.0](https://aws.amazon.com/rds/features/multi-az/) (from F09) | [0.3-0.8](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview?view=azuresql) (from F17) | 0.2-0.3 (from F25)* |
| **Difficulty** | 1-2/5 | 1-2/5 | 1-2/5 |

*G4 NOTE: GCP data FTE (F25) is reported per-service (Cloud SQL 0.1-0.2, Spanner 0.1, etc.) rather than as a domain aggregate. Normalized estimate: 0.5-1.0 cloud-native FTE when including all data services at comparable scope to AWS F09.

**Convergence:** All three offer managed relational databases with automated failover, backup, and patching at Difficulty 1-2/5. AWS and GCP both migrated to [Valkey as an open-source Redis alternative](https://aws.amazon.com/blogs/database/reduce-your-amazon-elasticache-costs-by-up-to-60-with-valkey-and-cudos/) (from F09), reducing cache costs by up to 60%. **Divergence:** GCP's [Cloud Spanner provides globally consistent transactions at Difficulty 1/5](https://cloud.google.com/spanner) (from F25) -- a capability with no direct equivalent in AWS or Azure at comparable simplicity. Azure's [AI Search collapses full-text, vector, and semantic re-ranking into one service](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview?view=azuresql) (from F17), while GCP's [Vector Search 2.0 achieves 9.6ms P95 at billion-vector scale](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931) (from F26).

### 2.3 AI/ML

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **LLM API** | Bedrock (multi-model) | Azure OpenAI / Foundry | Vertex AI (Gemini) |
| **Guardrails/Safety** | Bedrock Guardrails | Content Safety + Prompt Shields | Vertex AI content filtering |
| **Agent Framework** | Bedrock AgentCore | Azure AI Foundry | Vertex AI Agent Builder |
| **Embeddings/Vector** | Titan Embeddings, Kendra | Azure AI Search | Vector Search 2.0 |
| **Training Pipelines** | SageMaker Pipelines | Azure ML Pipelines | Vertex AI Pipelines |
| **On-Prem FTE** | [4.5-12.5](https://aws.amazon.com/bedrock/) (from F10) | [6.0-11.0](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic) (from F18) | 1.5-3.0+ (from F26)* |
| **Cloud-Native FTE** | [0.55-1.7](https://aws.amazon.com/bedrock/) (from F10) | [0.5-1.0](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic) (from F18) | ~0.1 (from F26)* |
| **Difficulty** | 1-2/5 (Bedrock), 3/5 (custom GPU) | 1-2/5 | 1-2/5 (Vertex), 3-4/5 (TPU) |

*G4 NOTE: GCP AI/ML FTE (F26) reports per-service (Vertex AI Pipelines ~0.1, Vector Search 0.0, etc.) rather than domain aggregate. Normalized estimate: 0.4-1.0 cloud-native FTE including model management, pipeline orchestration, and content safety configuration at comparable scope.

**Key divergence:** This is the domain of greatest provider differentiation. AWS Bedrock provides [multi-model access (Claude, Llama, Titan) with 0.0-0.1 FTE for API inference](https://aws.amazon.com/bedrock/) (from F10). Azure locks ISVs into the OpenAI model family but with tight M365/Copilot integration. GCP bets on Gemini with [pricing from $0.15/M tokens (Flash input) to $10/M tokens (Pro output)](https://cloud.google.com/vertex-ai/generative-ai/pricing) (from F26). Azure faces a unique capacity risk: [PTU quota does not guarantee deployment-time capacity](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic) (from F18), meaning high-growth ISVs may face supply-side deployment failures. Lock-in is steepest at GCP, where [Vertex AI endpoints sit outside standard deployment and security tooling](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) (from F31a, F26).

### 2.4 Security

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Identity** | IAM + Cognito | Entra ID (P1 included in M365 E3) | Workload Identity Federation |
| **Secrets** | KMS + Secrets Manager | Key Vault + Managed HSM | Cloud KMS + Secret Manager + Cloud HSM |
| **Posture** | GuardDuty, Security Hub | Defender for Cloud (free CSPM) | Security Command Center |
| **WAF/DDoS** | WAF + Shield | Azure DDoS + WAF | Cloud Armor Adaptive Protection |
| **Confidential** | Nitro Enclaves | Confidential VMs + GPU TEEs | Confidential VMs |
| **On-Prem FTE** | [5.0-9.5](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) (from F11) | [4.5-10.5](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) (from F19) | [7.25-14.0](https://cloud.google.com/security-command-center/pricing) (from F27) |
| **Cloud-Native FTE** | [0.75-1.65](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) (from F11) | [0.75-1.75](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) (from F19) | [~1.4](https://cloud.google.com/security-command-center/pricing) (from F27) |
| **Difficulty** | 1-2/5 | 1-2/5 | 2-3/5 |

**G4 NOTE -- Security FTE deduplication:** All three wave summaries warn that security FTE overlaps with security-adjacent tasks in other domains (from F11, F19, F27). After deduplication: security-specific FTE (policy authoring, posture management, identity governance, SIEM triage) should be counted at 0.5-1.25 FTE across all providers, with the remaining 0.25-0.5 FTE absorbed into adjacent domains (observability audit logging, networking ACLs, CI/CD secrets management). The deduplicated security FTE is remarkably consistent across providers.

**Convergence:** Cloud-native security FTE converges tightly at 0.75-1.75 FTE across all three providers -- the most consistent domain. All three offer managed HSM at a fraction of on-premises hardware costs. **Divergence:** Azure's [free CSPM covers Azure, AWS, and GCP simultaneously](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) (from F19), providing multi-cloud posture management at zero incremental cost. GCP's [Workload Identity Federation eliminates service account keys entirely](https://docs.google.com/iam/docs/workload-identity-federation) (from F27), the strongest zero-trust credential story. Azure's [confidential computing with GPU TEEs (NCCadsH100v5)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) (from F19) enables cryptographic isolation for regulated AI workloads with no practical equivalent elsewhere.

### 2.5 Observability

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Metrics** | CloudWatch, AMP | Azure Monitor, Managed Prometheus | Cloud Monitoring, Managed Prometheus |
| **Logs** | CloudWatch Logs | Log Analytics | Cloud Logging |
| **Tracing** | X-Ray/ADOT (migrating to OTEL) | Application Insights (OTEL-native 2025) | Cloud Trace (OTLP native ingestion) |
| **Dashboards** | AMG (Grafana) | Grafana GA at Ignite 2025 (free) | Grafana via Managed Prometheus |
| **On-Prem FTE** | [2.0-5.0](https://aws.amazon.com/cloudwatch/pricing/) (from F12) | [2.5-5.0](https://learn.microsoft.com/en-us/azure/azure-monitor/overview) (from F20) | [1.5-3.0](https://cloud.google.com/stackdriver/pricing) (from F28) |
| **Cloud-Native FTE** | [0.25-0.5](https://aws.amazon.com/cloudwatch/pricing/) (from F12) | [0.1-0.5](https://learn.microsoft.com/en-us/azure/azure-monitor/overview) (from F20) | [~0.2](https://cloud.google.com/stackdriver/pricing) (from F28) |
| **Difficulty** | 1-2/5 | 1/5 | 1-2/5 |

**Convergence:** All three providers are converging on OpenTelemetry as the instrumentation standard. AWS mandates migration via [X-Ray SDK end-of-support February 2027](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/) (from F12), Azure's [Application Insights went OTEL-native in 2025](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) (from F20), and GCP offers [native OTLP ingestion](https://www.infoq.com/news/2025/09/gcp-opentelemetry-adoption/) (from F28). All three now offer managed Prometheus with Grafana integration. **Divergence:** GCP's [Cloud Run provides zero-instrumentation distributed tracing](https://cloud.google.com/run/docs/trace) (from F28), the lowest-friction tracing entry point. GCP's [OTLP metrics remain in Preview](https://cloud.google.com/blog/products/management-tools/otlp-opentelemetry-protocol-for-google-cloud-monitoring-metrics) (from F31a), creating a gap between recommended and production-ready paths.

### 2.6 Networking

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Load Balancing** | ALB/NLB/GLB | Azure LB, App Gateway | Cloud Load Balancing (single anycast IP) |
| **CDN** | CloudFront | Azure Front Door | Cloud CDN |
| **DNS** | Route 53 | Azure DNS | Cloud DNS |
| **API Gateway** | API Gateway | APIM | Apigee |
| **Private Connectivity** | PrivateLink (cross-region 2025) | Private Link | Private Service Connect |
| **Service Mesh** | VPC Lattice / ECS Service Connect | N/A (AKS-native) | Cloud Service Mesh / Traffic Director |
| **On-Prem FTE** | [3.0-6.0+](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (from F13) | [3.0-6.0](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) (from F21) | [3.0-6.0](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) (from F29) |
| **Cloud-Native FTE** | [0.8-1.5](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (from F13) | [0.5-1.5](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) (from F21) | [~0.5](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) (from F29) |
| **Difficulty** | 1-2/5 | 1-3/5 | 1-2/5 |

**Convergence:** On-premises networking FTE is identical across all three at 3.0-6.0 FTE (from F13, F21, F29). Hybrid connectivity remains the hardest networking problem at 3/5 difficulty regardless of provider. **Divergence:** GCP's networking runs on [the same global infrastructure as Google Search](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) (from F29), with single-anycast-IP load balancing that eliminates pre-warming. GCP's [Private Service Connect eliminates CIDR overlap constraints](https://cloud.google.com/private-service-connect) (from F29) that affect VPC peering at scale. AWS expanded [PrivateLink with cross-region connectivity in November 2025](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services/) (from F13). Azure's [APIM V2 tiers lack multi-region deployment](https://learn.microsoft.com/en-us/azure/application-gateway/overview) (from F21), a notable gap for global ISVs.

### 2.7 CI/CD

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Pipeline** | CodePipeline V2 | Azure Pipelines, GitHub Actions | Cloud Build |
| **Deployment** | CodeDeploy, ECS-native B/G | Managed DevOps Pools (GA) | Cloud Deploy |
| **Registry** | ECR | ACR | Artifact Registry |
| **IaC** | CloudFormation, CDK | Bicep, ARM | Terraform (no native IaC) |
| **Image Signing** | N/A (ECR scanning) | Notary Project (post-DCT deprecation) | Binary Authorization |
| **On-Prem FTE** | [1.5-2.5](https://aws.amazon.com/codepipeline/pricing/) (from F14) | [4.5-7.5](https://devblogs.microsoft.com/devops/managed-devops-pools-ga/) (from F22) | [1.0-2.0](https://cloud.google.com/build) (from F30) |
| **Cloud-Native FTE** | [0.25-0.5](https://aws.amazon.com/codepipeline/pricing/) (from F14) | [0.6-1.05](https://devblogs.microsoft.com/devops/managed-devops-pools-ga/) (from F22) | [0.1-0.2](https://cloud.google.com/build) (from F30) |
| **Difficulty** | 1-2/5 | 1-2/5 | 1-2/5 |

**Convergence:** All three achieve Difficulty 1-2/5 for standard CI/CD pipelines. Container vulnerability scanning is now table stakes across all registries. **Divergence:** Azure provides the richest CI/CD ecosystem with [Managed DevOps Pools (GA)](https://devblogs.microsoft.com/devops/managed-devops-pools-ga/) (from F22) and tight GitHub Actions integration, but at the highest FTE cost. GCP's [Artifact Registry provides continuous vulnerability scanning with SBOM generation (GA)](https://docs.cloud.google.com/artifact-registry/docs/analysis) (from F30). AWS faces the most deprecation churn in this domain: [Proton (October 2026)](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html) (from F14) and the ECS-native B/G vs. CodeDeploy rationalization (from F15a).

### 2.8 Messaging & Event-Driven

| Dimension | AWS | Azure | GCP |
|-----------|-----|-------|-----|
| **Queue** | SQS | Service Bus | Pub/Sub |
| **Event Bus** | EventBridge | Event Grid | Eventarc |
| **Stream** | Kinesis | Event Hubs (Kafka-compatible) | Managed Kafka, Dataflow |
| **Orchestration** | Step Functions | Durable Functions | Cloud Workflows |
| **On-Prem FTE** | [5.3-10.75](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html) (from F15) | [3.0-6.0](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) (from F23) | [2.0-3.0](https://cloud.google.com/pubsub/sla) (from F31) |
| **Cloud-Native FTE** | [0.70-1.35](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html) (from F15) | [0.7-1.7](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) (from F23) | [~0.1](https://cloud.google.com/pubsub/sla) (from F31)* |
| **Difficulty** | 1-2/5 | 1-2/5 | 1-2/5 |

*G4 NOTE: GCP messaging FTE (~0.1 from F31) covers Pub/Sub and Cloud Workflows individually. AWS and Azure aggregate across full messaging stacks (queues + events + streams + orchestration). Normalized GCP estimate: 0.3-0.7 FTE when including Managed Kafka, Dataflow, and Eventarc at comparable scope.

**Convergence:** All three achieve near-zero operational friction for basic pub/sub and event-driven patterns. **Divergence:** Azure's [Event Hubs provides full Kafka wire-protocol compatibility](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview) (from F23), enabling zero-code migration from self-hosted Kafka. AWS offers the broadest range of orchestration primitives with [Step Functions](https://aws.amazon.com/step-functions/features/) (from F15) supporting visual workflows. GCP's [Cloud Workflows at $0.01/1,000 steps](https://cloud.google.com/workflows/pricing) (from F31) is the lowest-cost orchestration option.

---

## 3. Provider Convergence vs Divergence Analysis

**Commoditized (provider choice has minimal impact):**
- Basic compute (serverless functions, containers): All at Difficulty 1-2/5
- Managed relational databases: Automated failover, patching, backup across all three
- Object storage: Effectively identical durability and pricing models
- Observability instrumentation: OpenTelemetry convergence across all providers (from F12, F20, F28)
- Container registries and vulnerability scanning: Table stakes across ECR, ACR, Artifact Registry
- Managed Prometheus + Grafana: Available on all three with comparable pricing

**Differentiated (provider choice matters significantly):**
- AI/ML platform: Bedrock (multi-model) vs Azure OpenAI (GPT family + Copilot) vs Vertex AI (Gemini + TPU) -- fundamentally different model ecosystems and lock-in profiles (from F10, F18, F26)
- Identity architecture: Cognito (MAU-priced) vs Entra ID (bundled with M365) vs Workload Identity Federation (free, keyless) -- different cost models and zero-trust maturity (from F11, F19, F27)
- Global networking: GCP's anycast infrastructure vs AWS PrivateLink cross-region vs Azure Front Door -- structural architecture differences (from F13, F21, F29)
- Confidential computing for AI: Azure leads with GPU TEEs (NCCadsH100v5) (from F19)

---

## 4. Deprecation Risk Register

| Deprecation | Provider | Deadline | Migration Path | Source |
|-------------|----------|----------|---------------|--------|
| X-Ray SDK/Daemon EOL | AWS | [Feb 25, 2027](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/) | ADOT-based OpenTelemetry | F12 |
| AWS App Mesh EOL | AWS | [Sep 30, 2026](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/) | VPC Lattice or ECS Service Connect | F13, F15a |
| AWS Proton EOL | AWS | [Oct 7, 2026](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html) | CodePipeline + CodeBuild | F14 |
| Docker Content Trust deprecation | Azure | [Sep 2025](https://learn.microsoft.com/en-us/azure/container-apps/github-actions) | Notary Project | F23a |
| APIM V2 multi-region gap | Azure | Ongoing | V1 or multi-instance V2 | F21 |
| Pub/Sub Lite shutdown | GCP | [Mar 18, 2026](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) | Standard Pub/Sub or Managed Kafka | F31 |
| Document AI HITL removal | GCP | [Jan 2025 (already deprecated)](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new) | Partner engagement | F26 |
| Cloud Source Repos closure | GCP | [Jun 2024 (closed to new customers)](https://docs.cloud.google.com/source-repositories/docs/migration-guides) | GitHub/GitLab with WIF | F30 |
| Binary Authorization legacy CV | GCP | [May 2025](https://docs.cloud.google.com/binary-authorization/docs/overview-cv) | Check-based policies | F30 |
| Artifact Registry Advanced Vuln Insights | GCP | [Jun 2026](https://docs.cloud.google.com/artifact-registry/docs/analysis) | Standard scanning | F31a |
| Cloud Debugger | GCP | [May 2023 (deprecated, no replacement)](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation) | None | F28 |

AWS has three hard deadlines concentrated in 2026-2027. GCP has the most deprecations by count but several are already past. Azure has the fewest hard deprecation deadlines but faces structural gaps (APIM V2 multi-region, Container Apps structured logging).

---

## 5. Provider-Neutral Capabilities Profile

Regardless of which cloud provider an ISV selects, the following capabilities can be assumed available at Difficulty 1-2/5 with comparable FTE burden:

- **Serverless compute** with automatic scaling, pay-per-invocation pricing, and cold-start times under 1 second
- **Managed relational databases** with automated failover, point-in-time recovery, and read replicas
- **Managed NoSQL** with global replication and single-digit-millisecond latency
- **Object storage** at 11 9s durability with lifecycle management
- **Managed cache** (all three now support Valkey/Redis-compatible in-memory stores)
- **LLM inference APIs** with per-token billing and built-in content safety
- **Managed Prometheus + Grafana** for metrics and dashboards
- **OpenTelemetry-based distributed tracing** (native or migrating)
- **Managed container registries** with integrated vulnerability scanning
- **CI/CD pipelines** with managed build agents and IaC-driven deployment
- **Managed pub/sub messaging** with at-least-once delivery and 99.95%+ SLAs
- **Managed secrets and key management** with HSM backing
- **DDoS protection and WAF** with managed rulesets
- **Private connectivity** eliminating public internet traversal for service-to-service communication

---

## 6. Normalized FTE Summary Table

The following table reconciles FTE estimates across providers after applying G4 quality gate adjustments: normalizing GCP scope, deduplicating security, and establishing canonical ranges.

| Domain | AWS Cloud-Native FTE | Azure Cloud-Native FTE | GCP Cloud-Native FTE (Normalized) | Canonical Range |
|--------|---------------------|----------------------|----------------------------------|----------------|
| Compute | 1.0-2.1 (F08) | 0.2-0.6 (F16) | 0.5-1.0* | 0.5-1.5 |
| Data/Storage | 1.1-2.0 (F09) | 0.3-0.8 (F17) | 0.5-1.0* | 0.5-1.5 |
| AI/ML | 0.55-1.7 (F10) | 0.5-1.0 (F18) | 0.4-1.0* | 0.5-1.2 |
| Security (deduplicated) | 0.5-1.25 (F11) | 0.5-1.25 (F19) | 0.5-1.25 (F27) | 0.5-1.25 |
| Observability | 0.25-0.5 (F12) | 0.1-0.5 (F20) | ~0.2 (F28) | 0.15-0.5 |
| Networking | 0.8-1.5 (F13) | 0.5-1.5 (F21) | ~0.5 (F29) | 0.5-1.5 |
| CI/CD | 0.25-0.5 (F14) | 0.6-1.05 (F22) | 0.1-0.2 (F30) | 0.2-0.6 |
| Messaging | 0.70-1.35 (F15) | 0.7-1.7 (F23) | 0.3-0.7* | 0.5-1.2 |
| **Total (deduplicated)** | **~5-11** | **~3.4-8.4** | **~3.0-5.9** | **~3.5-9.0** |

*Normalized GCP estimates adjust for narrower per-service reporting scope in F24-F31 compared to domain-aggregate reporting in AWS F08-F15 and Azure F16-F23.

**Canonical cloud-native FTE range: 4-9 FTE** for a mid-size ISV serving 50 enterprise customers across all eight domains. The range reflects: (a) ISVs deploying a subset of services cluster toward the low end; (b) ISVs using the full stack including custom ML training, complex event processing, and multi-region networking trend toward the high end; (c) security FTE counted once at 0.5-1.25 FTE regardless of provider.

---

## 7. Open Questions for Downstream Synthesis

Consolidated from all three wave summaries, deduplicated:

1. **Total Cost of Ownership modeling:** FTE savings are documented, but consumption-based pricing (Bedrock tokens, Cognito MAUs, CloudWatch metrics, PTU reservations, Pub/Sub message volume) introduces variable cost that must be modeled against FTE savings. What is the cost crossover point where managed service spend exceeds FTE savings? (from W02S Q2, W04S Q1)

2. **Managed K8s comparison:** EKS, AKS, and GKE Autopilot sit between on-premises and cloud-native at Difficulty 2-3/5 with ~2x the FTE of cloud-native. Is K8s portability worth the FTE premium? (from W02S Q3)

3. **Migration effort estimation:** None of the 27 agent files estimated migration effort from existing on-premises deployments -- only steady-state operational profiles. What is the one-time engineering cost to move? (from W02S Q4)

4. **AI capacity risk mitigation:** Azure PTU quota does not guarantee deployment-time capacity. AWS and GCP have not disclosed equivalent limitations. How should ISVs architect for inference capacity availability across providers? (from W03S Q2)

5. **Multi-cloud portability cost by domain:** Which domains have viable open-source exit paths (e.g., Apache Beam for Dataflow, KFP for Vertex Pipelines, OTEL for observability) and which are effectively irreversible? (from W04S Q2)

6. **Compliance surface area:** Cross-domain compliance burden (SOC 2, HIPAA, FedRAMP) across data, AI, and messaging has not been consolidated. Which services carry BAA eligibility by provider? (from W04S Q3)

7. **Deprecation compounding risk:** ISVs adopting multiple services with concurrent deprecation deadlines (especially AWS with three in 2026-2027 and GCP with five total) face migration effort that may temporarily exceed steady-state FTE estimates. What is the surge staffing model? (from W02S Q5, W04S Q4)

---

## 8. Sources

### AWS (Wave 2: F08-F15a)
- [Lambda Managed Instances](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/) (F08)
- [GPU Price Reductions](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) (F08)
- [RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/) (F09)
- [ElastiCache Valkey Cost Reduction](https://aws.amazon.com/blogs/database/reduce-your-amazon-elasticache-costs-by-up-to-60-with-valkey-and-cudos/) (F09)
- [Aurora Serverless v2 Scale-to-Zero](https://aws.amazon.com/blogs/database/introducing-scaling-to-0-capacity-with-amazon-aurora-serverless-v2/) (F09)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) (F10)
- [Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) (F10)
- [Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) (F10)
- [SageMaker Pipelines](https://aws.amazon.com/sagemaker/ai/pipelines/) (F10)
- [IAM Full Policy Language for SCPs](https://aws.amazon.com/about-aws/whats-new/2025/09/aws-organizations-iam-language-service-control-policies/) (F11)
- [GuardDuty Extended Threat Detection](https://aws.amazon.com/about-aws/whats-new/2025/12/guardduty-extended-threat-detection-ec2-ecs/) (F11)
- [Cognito Pricing](https://aws.amazon.com/cognito/pricing/) (F11)
- [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) (F12)
- [X-Ray to ADOT Migration](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/) (F12)
- [AMP Costs](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-costs.html) (F12)
- [PrivateLink Cross-Region](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services/) (F13)
- [App Mesh to ECS Service Connect Migration](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/) (F13)
- [CloudFront Post-Quantum TLS](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-cloudfront-TLS-policy-post-quantum-support/) (F13)
- [CodePipeline V2 Pricing](https://aws.amazon.com/codepipeline/pricing/) (F14)
- [ECS Native Blue/Green](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/) (F14, F15a)
- [Proton End-of-Support](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html) (F14)
- [SQS Features](https://aws.amazon.com/sqs/features/) (F15)
- [EventBridge Features](https://aws.amazon.com/eventbridge/features/) (F15)
- [Step Functions Features](https://aws.amazon.com/step-functions/features/) (F15)
- [Kinesis Enhanced Fan-Out](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-kinesis-data-streams-enhanced-fan-out-consumers/) (F15)

### Azure (Wave 3: F16-F23a)
- [Azure Functions Scale](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) (F16)
- [Azure SQL Auto-Tuning](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview?view=azuresql) (F17)
- [Azure OpenAI Provisioned Throughput](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput?view=foundry-classic) (F18)
- [Content Safety Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) (F18)
- [Defender for Cloud CSPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) (F19)
- [Managed HSM](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview) (F19)
- [Azure Monitor / Managed Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview) (F20)
- [Application Insights OTEL-native](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) (F20)
- [Grafana GA at Ignite 2025](https://techcommunity.microsoft.com/blog/azureobservabilityblog/advancing-full-stack-observability-with-azure-monitor-at-ignite-2025/4469041) (F20)
- [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction) (F21)
- [APIM / App Gateway](https://learn.microsoft.com/en-us/azure/application-gateway/overview) (F21)
- [Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) (F21)
- [Managed DevOps Pools GA](https://devblogs.microsoft.com/devops/managed-devops-pools-ga/) (F22)
- [Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) (F23)
- [Event Hubs Kafka Compatibility](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview) (F23)
- [Container Apps Integration](https://learn.microsoft.com/en-us/azure/container-apps/github-actions) (F23a)

### GCP (Wave 4: F24-F31a)
- [Cloud Run GPU](https://docs.cloud.google.com/run/docs/configuring/services/gpu) (F24)
- [TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e) (F24)
- [Cloud SQL Editions](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) (F25)
- [Cloud Spanner](https://cloud.google.com/spanner) (F25)
- [BigQuery Overview](https://docs.cloud.google.com/bigquery/docs/introduction) (F25)
- [Memorystore Valkey GA](https://cloud.google.com/blog/products/databases/announcing-general-availability-of-memorystore-for-valkey) (F25)
- [Vertex AI Pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing) (F26)
- [Vector Search 2.0](https://discuss.google.dev/t/introducing-vertex-ai-vector-search-2-0-from-zero-to-billion-scale/317931) (F26)
- [Document AI HITL Deprecation](https://docs.cloud.google.com/document-ai/docs/hitl/whats-new) (F26)
- [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) (F26)
- [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) (F27)
- [Cloud HSM](https://cloud.google.com/kms/docs/hsm) (F27)
- [SCC Agentless Scanning](https://security.googlecloudcommunity.com/news-announcements-9/google-security-command-center-scc-h2-2025-product-release-summary-6574) (F27)
- [Cloud Armor](https://cloud.google.com/security/products/armor) (F27)
- [Cloud Logging Pricing](https://cloud.google.com/stackdriver/pricing) (F28)
- [OTLP Native Ingestion](https://www.infoq.com/news/2025/09/gcp-opentelemetry-adoption/) (F28)
- [Managed Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) (F28)
- [Cloud Trace on Cloud Run](https://cloud.google.com/run/docs/trace) (F28)
- [Cloud Debugger Deprecation](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation) (F28)
- [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) (F29)
- [Private Service Connect](https://cloud.google.com/private-service-connect) (F29)
- [Cloud Service Mesh](https://cloud.google.com/service-mesh/docs/overview) (F29)
- [Cloud Build](https://cloud.google.com/build) (F30)
- [Artifact Registry Scanning](https://docs.cloud.google.com/artifact-registry/docs/analysis) (F30)
- [Cloud Source Repos Deprecation](https://docs.cloud.google.com/source-repositories/docs/migration-guides) (F30)
- [Pub/Sub SLA](https://cloud.google.com/pubsub/sla) (F31)
- [Pub/Sub Lite Deprecation](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) (F31)
- [Cloud Workflows Pricing](https://cloud.google.com/workflows/pricing) (F31)
- [Kafka FTE Estimate (ArXiv)](https://arxiv.org/pdf/2510.04404) (F31)
- [Serverless NEG Health Check Limitation](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) (F31a)
- [Secret Manager CSI](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component) (F31a)
- [OTLP Metrics Preview](https://cloud.google.com/blog/products/management-tools/otlp-opentelemetry-protocol-for-google-cloud-monitoring-metrics) (F31a)
