# W02S: AWS Cloud-Native Managed Services -- Synthesis Summary

**Synthesis Agent:** W02S | **Wave:** 2 (AWS Cloud-Native Managed Services)
**Source Files:** F08, F09, F10, F11, F12, F13, F14, F15, F15a
**Date:** 2026-02-19

---

## Executive Summary

Across nine research agents covering compute, data, AI/ML, security, observability, networking, CI/CD, messaging, and per-service infrastructure integration, AWS cloud-native managed services consistently reduce operational staffing by 75-90% compared to equivalent on-premises deployments. Aggregate on-premises FTE estimates across all domains total approximately 32-69 FTE for a mid-size ISV serving 50 enterprise customers, collapsing to approximately 4-9 FTE on cloud-native AWS. Difficulty ratings cluster at 1-2/5 for the vast majority of cloud-native capabilities, with GPU/AI inference at 3/5 representing the primary exception. The year 2025 was a watershed for AWS service maturity: Lambda Managed Instances, ECS-native blue/green deployments, full IAM policy language in SCPs, GuardDuty Extended Threat Detection across EKS/EC2/ECS, Security Hub OCSF re-architecture, PrivateLink cross-region connectivity, and the mandatory X-Ray-to-OpenTelemetry migration collectively signal that AWS is closing the remaining operational gaps that previously justified third-party tooling. However, cloud-native is not zero-ops: cost governance, security policy engineering, per-service integration wiring, and deprecation-deadline tracking remain non-trivial ISV responsibilities.

**G3 NOTE (FTE overlap):** Security FTE estimates in F11 (0.75-1.65 FTE) include IAM governance, Cognito management, KMS/Secrets Manager configuration, and WAF/GuardDuty tuning. Some of these responsibilities overlap with security-adjacent tasks reported in F12 (CloudTrail audit logging), F13 (security group/NACL configuration within VPC), and F15a (secrets management integration per compute type). When aggregating cross-domain FTE totals, do not sum blindly -- the security engineering function counted in F11 partially absorbs security-adjacent tasks reported in adjacent agents.

---

## Theme 1: Managed Services Eliminate Undifferentiated Infrastructure at Scale

The dominant finding across all nine agents is that AWS managed services systematically replace the most labor-intensive operational tasks -- [patching, hardware provisioning, replication setup, backup orchestration, and failover management](https://aws.amazon.com/rds/) (from F09) -- with configuration-only management via IaC. The data tier shows the most dramatic shift: [self-hosted databases and storage require an estimated 7-12 FTE versus 1-2 FTE cloud-native](https://aws.amazon.com/rds/features/multi-az/) (from F09). Messaging shows a [4-8x staffing premium for on-premises](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html) (from F15), with on-prem totaling 5.3-10.75 FTE versus 0.70-1.35 FTE cloud-native. Networking represents [the largest operational complexity gap between on-premises and cloud-native of any infrastructure domain](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (from F13), estimated at 3.0-6.0 FTE on-prem versus 0.8-1.5 FTE cloud-native. AI/ML services show the most extreme per-capability reduction: [Bedrock LLM inference requires 0.0-0.1 FTE versus 1.0-2.0 FTE self-hosted](https://aws.amazon.com/bedrock/) (from F10), because Bedrock abstracts away all GPU infrastructure, model serving, and scaling.

## Theme 2: 2025 as a Maturity Inflection Point

Every agent identified significant 2025-era service launches or enhancements that reduce ISV operational burden or close previously meaningful gaps. In compute, [Lambda Managed Instances (November 2025) enable EC2-backed Lambda with up to 72% savings via commitment pricing](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/) (from F08), while [P5 GPU prices dropped up to 45% in June 2025](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/) (from F08). In security, [full IAM policy language in SCPs (September 2025)](https://aws.amazon.com/about-aws/whats-new/2025/09/aws-organizations-iam-language-service-control-policies/) (from F11) and [GuardDuty Extended Threat Detection expanding to EKS, EC2, and ECS](https://aws.amazon.com/about-aws/whats-new/2025/12/guardduty-extended-threat-detection-ec2-ecs/) (from F11) close gaps that previously pushed ISVs toward third-party SIEM and posture management tools. In CI/CD, [ECS-native blue/green deployments (July 2025)](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/) (from F14/F15a) consolidate what previously required CodeDeploy orchestration. In networking, [PrivateLink cross-region connectivity (November 2025)](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services/) (from F13) strengthens private API connectivity for globally distributed SaaS.

## Theme 3: Residual ISV Responsibilities -- Cost Governance, Security Engineering, and Integration Wiring

Cloud-native does not mean zero-ops. Three categories of residual ISV responsibility emerged consistently:

**Cost governance:** [CloudWatch custom metrics at $0.30/metric/month](https://aws.amazon.com/cloudwatch/pricing/) (from F12) and Logs Insights scan charges can accumulate substantially in high-cardinality deployments. [Cognito MAU-based pricing ($0.015/MAU for federated users)](https://aws.amazon.com/cognito/pricing/) (from F11) creates direct financial exposure correlated with customer growth -- a compounding risk for B2B SaaS. [AMP ingestion tiering](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-costs.html) (from F12) requires proactive label cardinality management.

**Security engineering shifts, not disappears:** Even at cloud-native difficulty ratings of 1-2/5 per domain, [aggregate security staffing of 0.75-1.65 FTE is still required](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) (from F11) for policy authoring, IAM governance, GuardDuty tuning, and compliance evidence collection. The shift is from infrastructure operations to governance -- higher-leverage work, but still non-trivial.

**Per-service integration complexity:** F15a documents that [a single ECS Fargate service requires coordinated configuration across at least six distinct AWS control planes](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/) (from F15a) -- CI/CD, health checks, service discovery, load balancing, observability, and secrets management. Pipeline templates are not interchangeable across Lambda, ECS, App Runner, and SageMaker; each compute type requires distinct wiring patterns.

## Theme 4: Deprecation Deadlines Requiring ISV Planning

Three hard deprecation deadlines surfaced across agents that ISVs must track:

1. **X-Ray SDK/Daemon end-of-support: February 25, 2027** -- [ISVs must migrate to ADOT-based OpenTelemetry instrumentation](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/) (from F12). The convergence on open standards reduces lock-in risk but requires active migration planning.
2. **AWS App Mesh end-of-life: September 30, 2026** -- [Migrate to VPC Lattice or ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/) (from F13/F15a).
3. **AWS Proton discontinuation: October 7, 2026** -- [Migrate to CodePipeline + CodeBuild or CloudFormation Git Sync](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html) (from F14).

---

## Difficulty & FTE Summary Table

| Domain | Agent | On-Prem FTE | Cloud-Native FTE | Cloud-Native Difficulty | Key Managed Services |
|--------|-------|-------------|------------------|------------------------|---------------------|
| Compute | F08 | 6.0-12.0 | 1.0-2.1 | 1-3/5 | Lambda, ECS/Fargate, Batch, Inferentia |
| Data | F09 | 7.0-12.0 | 1.1-2.0 | 1-2/5 | RDS, DynamoDB, ElastiCache, S3, OpenSearch |
| AI/ML | F10 | 4.5-12.5 | 0.55-1.7 | 1-2/5 | Bedrock, SageMaker, Titan, Kendra |
| Security | F11 | 5.0-9.5 | 0.75-1.65 | 1-2/5 | IAM, Cognito, KMS, WAF, GuardDuty |
| Observability | F12 | 2.0-5.0 | 0.25-0.5 | 1-2/5 | CloudWatch, X-Ray/ADOT, AMP, AMG |
| Networking | F13 | 3.0-6.0+ | 0.8-1.5 | 1-2/5 | ELB, Route 53, API Gateway, CloudFront |
| CI/CD | F14 | 1.5-2.5 | 0.25-0.5 | 1-2/5 | CodePipeline, CodeBuild, ECR |
| Messaging | F15 | 5.3-10.75 | 0.70-1.35 | 1-2/5 | SQS, SNS, EventBridge, Step Functions |
| **Totals** | | **~34-70** | **~5-11** | | |

*FTE totals are indicative ranges. Security FTE (F11) partially overlaps with security-adjacent tasks in F12, F13, and F15a. Most ISVs deploy a subset of services, not the full stack. F15a (integration) is not separately FTE-estimated but adds coordination overhead across all domains.*

---

## Cross-Agent Patterns & Contradictions

**Consistent patterns:**
- All nine agents converge on cloud-native difficulty ratings of 1-2/5 for the majority of capabilities, with the sole exception of GPU/AI inference at 3/5 (from F08).
- On-premises FTE estimates consistently include on-call burden of 0.5-1.0 FTE per operational domain; cloud-native on-call burden drops to 0.05-0.25 FTE per domain.
- Every agent identified cost governance as an ISV responsibility that persists regardless of deployment model.

**Potential tensions:**
- F10 rates Bedrock LLM inference at 0.0-0.1 FTE (difficulty 1/5), but F08 rates GPU/AI inference serving at 0.5-1.0 FTE (difficulty 3/5). These are complementary, not contradictory: Bedrock abstracts all inference infrastructure for API-accessible foundation models, while F08 addresses custom model inference on GPU instances where ISVs need lower-level control. ISVs using Bedrock exclusively experience the F10 profile; ISVs running custom models on EC2/ECS GPU instances experience the F08 profile.
- F14 shows CodeDeploy as the ECS deployment mechanism, but F15a notes that ECS-native blue/green (July 2025) now replaces CodeDeploy for all-at-once deployments. ISVs should default to ECS-native blue/green and retain CodeDeploy only for canary/linear traffic shifting.
- F11 security FTE (0.75-1.65) and F12 observability FTE (0.25-0.5) both partially include CloudTrail audit logging work. The total should not be summed without deducting this overlap.

---

## Open Questions for Downstream Synthesis

1. **How do AWS FTE estimates compare to Azure and GCP equivalents?** Waves 3-4 will provide comparable data; cross-provider synthesis should normalize difficulty ratings and FTE ranges against the same ISV profile.
2. **What is the true aggregate cost of a full AWS cloud-native stack at 50-customer scale?** FTE savings are clear, but consumption-based pricing (Bedrock tokens, CloudWatch metrics, Cognito MAUs, AMP ingestion) introduces variable cost that must be modeled against the FTE savings.
3. **How does the managed K8s (EKS) model compare on total cost of ownership?** EKS sits between on-prem and cloud-native in every agent's difficulty ratings (typically 3/5); the ISV question is whether K8s portability justifies the ~2x FTE premium over cloud-native.
4. **What is the migration cost from existing on-premises deployments?** None of the agents estimated migration effort -- only steady-state operational profiles.
5. **How do the three hard deprecation deadlines (X-Ray Feb 2027, App Mesh Sep 2026, Proton Oct 2026) interact with ISV release planning cycles?**

---

## Sources

### F08: AWS Compute Services
- [Lambda Managed Instances — AWS Blog](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/)
- [Up to 45% Price Reduction for NVIDIA GPU Instances — AWS Blog](https://aws.amazon.com/blogs/aws/announcing-up-to-45-price-reduction-for-amazon-ec2-nvidia-gpu-accelerated-instances/)
- [AWS Inferentia2 vs Trainium vs GPU — Zircon Tech](https://zircon.tech/blog/aws-ai-infrastructure-inferentia2-vs-trainium-vs-gpu-for-production-workloads/)
- [AWS Custom ML Accelerators — CloudOptimo](https://www.cloudoptimo.com/blog/amazons-custom-ml-accelerators-aws-trainium-and-inferentia/)
- [EC2 Trn3 UltraServers — AWS](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)

### F09: AWS Data Services
- [Amazon RDS Multi-AZ Features](https://aws.amazon.com/rds/features/multi-az/)
- [DynamoDB Global Tables](https://aws.amazon.com/dynamodb/global-tables/)
- [Reduce ElastiCache Costs with Valkey — AWS Blog](https://aws.amazon.com/blogs/database/reduce-your-amazon-elasticache-costs-by-up-to-60-with-valkey-and-cudos/)
- [Aurora Serverless v2 Scale-to-Zero — AWS Blog](https://aws.amazon.com/blogs/database/introducing-scaling-to-0-capacity-with-amazon-aurora-serverless-v2/)
- [Amazon S3 Data Protection](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)

### F10: AWS AI/ML Services
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [SageMaker Pipelines](https://aws.amazon.com/sagemaker/ai/pipelines/)
- [Titan Text Embeddings V2 — AWS Blog](https://aws.amazon.com/blogs/machine-learning/get-started-with-amazon-titan-text-embeddings-v2-a-new-state-of-the-art-embeddings-model-on-amazon-bedrock/)

### F11: AWS Security Services
- [AWS Organizations Full IAM Policy Language for SCPs](https://aws.amazon.com/about-aws/whats-new/2025/09/aws-organizations-iam-language-service-control-policies/)
- [GuardDuty Extended Threat Detection for EC2 and ECS](https://aws.amazon.com/about-aws/whats-new/2025/12/guardduty-extended-threat-detection-ec2-ecs/)
- [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing/)
- [ACM Public Certificates Use Anywhere](https://aws.amazon.com/about-aws/whats-new/2025/06/aws-certificate-manager-public-certificates-use-anywhere/)
- [Security Hub Near Real-Time Analytics — AWS Blog](https://aws.amazon.com/blogs/aws/aws-security-hub-now-generally-available-with-near-real-time-analytics-and-risk-prioritization/)

### F12: AWS Observability Services
- [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)
- [X-Ray End-of-Support / ADOT Migration — AWS Blog](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/)
- [CloudWatch Cross-Account Observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)
- [AMP Cost Management](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-costs.html)

### F13: AWS Networking Services
- [AWS PrivateLink Cross-Region Connectivity](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-privatelink-cross-region-connectivity-aws-services/)
- [App Mesh Deprecation / Migration](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/)
- [CloudFront Post-Quantum TLS](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-cloudfront-TLS-policy-post-quantum-support/)
- [Route 53 Global Resolver Preview](https://aws.amazon.com/blogs/aws/introducing-amazon-route-53-global-resolver-for-secure-anycast-dns-resolution-preview/)

### F14: AWS CI/CD Services
- [CodePipeline V2 Pricing](https://aws.amazon.com/codepipeline/pricing/)
- [ECS Native Blue/Green Deployments — AWS DevOps Blog](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/)
- [AWS Proton End-of-Support](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html)
- [CodeCommit Returns to GA — AWS Blog](https://aws.amazon.com/blogs/devops/aws-codecommit-returns-to-general-availability/)

### F15: AWS Messaging Services
- [Amazon SQS Features](https://aws.amazon.com/sqs/features/)
- [Amazon EventBridge Features](https://aws.amazon.com/eventbridge/features/)
- [Kinesis Enhanced Fan-Out 50 Consumers](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-kinesis-data-streams-enhanced-fan-out-consumers/)
- [Step Functions Features](https://aws.amazon.com/step-functions/features/)

### F15a: AWS Infrastructure Integration
- [ECS Native Blue/Green — AWS DevOps Blog](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/)
- [App Mesh to ECS Service Connect Migration](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/)
- [CodeDeploy Deployment Configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
