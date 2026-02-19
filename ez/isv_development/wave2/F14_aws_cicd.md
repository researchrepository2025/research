# F14: AWS CI/CD Services
**Agent ID:** F14 | **Scope:** AWS-managed CI/CD pipeline, build, deploy, and artifact services

---

## Executive Summary

AWS provides a fully managed, end-to-end CI/CD toolchain — CodePipeline (orchestration), CodeBuild (build execution), CodeDeploy (deployment automation), ECR (container registry), and CodeArtifact (artifact management) — that collectively eliminates the infrastructure ownership burden that self-hosted alternatives such as Jenkins impose. For an ISV evaluating deployment models, these services shift operational effort from infrastructure management to pipeline configuration: the AWS control plane handles server provisioning, patching, scaling, and availability. CodeDeploy in particular has seen notable 2025 evolution, with Amazon ECS introducing native blue/green deployments that reduce CodeDeploy dependency for ECS workloads, while CodeDeploy continues as the primary choice for canary and linear traffic-shifting strategies across EC2 and Lambda. AWS CodeCommit — briefly deprecated in July 2024 — returned to general availability in November 2025, restoring a fully AWS-native source control option for regulated-industry customers. AWS Proton, the managed delivery service for containerized applications, is scheduled for discontinuation on October 7, 2026, and ISVs currently using it should plan migrations now.

---

## AWS CodePipeline: Managed CI/CD Orchestration

### Overview

[AWS CodePipeline](https://aws.amazon.com/codepipeline/) is a fully managed continuous delivery service that automates build, test, and deploy phases. The core abstraction is a **pipeline** composed of sequential **stages**, each containing one or more serial or parallel **actions**.

### Pipeline Types: V1 vs. V2

CodePipeline offers two pipeline types with distinct capabilities and pricing models:

| Feature | V1 Pipeline | V2 Pipeline |
|---------|------------|------------|
| Pricing model | $1.00/active pipeline/month | $0.002/action execution minute |
| Parallel execution mode | No | Yes |
| Queued execution mode | No | Yes |
| Advanced trigger filters | No | Yes |
| Branch/monorepo triggers | No | Yes |
| Free tier | 1 pipeline/month | 100 action execution minutes/month |

Source: [AWS CodePipeline Pricing](https://aws.amazon.com/codepipeline/pricing/)

### Source Integrations

CodePipeline V2 supports the following source action types via [AWS CodeStar Connections](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html):

- GitHub.com (via CodeStar connection)
- GitHub Enterprise Server
- Bitbucket Cloud
- GitLab.com
- GitLab self-managed
- Amazon S3 (versioned buckets, with EventBridge change detection)
- Amazon ECR (triggers on image push)
- AWS CodeCommit

Source: [CodePipeline Integrations with Action Types](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-action-type.html)

### Advanced Trigger Filters (V2)

V2 pipelines introduced [advanced trigger filtering](https://aws.amazon.com/about-aws/whats-new/2024/02/codepipeline-trigger-filters-execution-modes/) that enables:

- Glob patterns on **branch names** (e.g., `feature/*`) for GitFlow workflows
- Glob patterns on **file paths** for monorepo strategies — only trigger when specific subdirectories change
- Separate triggers on push events vs. pull request events

This eliminates the need for custom Lambda functions or webhook shims to filter pipeline triggers, which was a common workaround in V1 architectures.

### Execution Modes (V2)

[AWS CodePipeline added Parallel and Queued execution modes](https://aws.amazon.com/about-aws/whats-new/2024/02/codepipeline-trigger-filters-execution-modes/) to V2:

- **PARALLEL mode:** Executions run simultaneously and independently. No execution waits for another to complete.
- **QUEUED mode:** Executions queue behind a running execution, ensuring only one execution runs at a time.
- **SUPERSEDED mode (default V1 behavior):** A newer execution can replace a pending execution.

### Operational Burden Eliminated

| Burden Eliminated | Self-Hosted Equivalent |
|------------------|----------------------|
| CI orchestration server provisioning | Jenkins primary + agent nodes |
| Availability and failover | Jenkins HA configuration |
| Plugin version management | Jenkins plugin ecosystem |
| Audit logging | CloudTrail integration included |
| IAM-native access control | Custom authentication layer |
| SNS notifications for pipeline events | Custom notification integrations |

Source: [AWS CodePipeline Features](https://aws.amazon.com/codepipeline/features/)

### Stage-Level Conditions (2024-2025)

AWS added [stage-level conditions to CodePipeline](https://aws.amazon.com/blogs/devops/enhance-release-control-with-aws-codepipeline-stage-level-conditions/) to implement pipeline gates — rules that must pass before a stage proceeds or after a stage completes. This enables automated quality gates without custom Lambda approval logic.

### Operational Difficulty Rating

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| CI/CD Orchestration | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-hosted Jenkins/Tekton; server ops | Tekton on K8s or Jenkins agent pods | CodePipeline V2 fully managed |
| | Jenkins, Tekton, ArgoCD | Tekton, Jenkins X, ArgoCD | CodePipeline, EventBridge |
| Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |

*Assumptions: Mid-size ISV, 10–30 active pipelines, 50 enterprise customers. On-call burden estimated at +0.1 FTE across all models for P1 pipeline failures.*

---

## AWS CodeBuild: Managed Build Service

### Overview

[AWS CodeBuild](https://aws.amazon.com/codebuild/) is a fully managed build service that compiles source code, runs tests, and produces deployable artifacts. AWS manages the build server fleet; ISVs pay only for build minutes consumed.

### Compute Modes

CodeBuild offers two compute modes: [EC2 and Lambda](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html).

**EC2 Compute (On-Demand):**
- Linux ARM (`arm1.small`): 2 vCPU, 3 GB — $0.0034/min
- Linux x86 XLarge (`general1.xlarge`): 36 vCPU, 72 GB — $0.0798/min
- Windows Medium (`general1.medium`): ~$0.018/min
- Windows XLarge (`general1.xlarge`): ~$0.16/min

**Lambda Compute:**
- Billed at $0.00001 per build second (more granular than per-minute EC2 pricing)
- ARM (Graviton) Lambda builds are ~50% cheaper than x86 Lambda builds

Source: [AWS CodeBuild Pricing](https://aws.amazon.com/codebuild/pricing/)

### Reserved Capacity Fleets

In April 2025, [AWS CodeBuild added support for selecting a specific EC2 instance type and configurable storage size for reserved capacity fleets](https://aws.amazon.com/about-aws/whats-new/2025/04/aws-codebuild-ec2-instance-type-configurable-storage-size/). Reserved capacity fleets maintain dedicated instances for build workloads, eliminating cold-start latency and providing consistent, predictable build environments.

Supported instance families for reserved fleets include M5/M6/M7/M8 (General Purpose), C5/C6/C7/C8 (Compute Optimized), and others, giving ISVs fine-grained control over the CPU/memory/storage profile matching their build workload.

Source: [Reserved Capacity Fleet Properties](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.reserved-capacity-fleets.html)

### GPU Build Support

[AWS CodeBuild supports GPU-based build environments](https://aws.amazon.com/about-aws/whats-new/2023/03/aws-codebuild-small-gpu-machine-type/) via a `4vCPU 1GPU` small GPU machine type (`BUILD_GENERAL1_SMALL` with `LINUX_GPU_CONTAINER`). This is relevant for ISVs that build or test ML inference code as part of their CI pipeline.

**Important limitation:** [Local caching is not supported with the `LINUX_GPU_CONTAINER` environment type](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-local.html). GPU builds must use S3 caching or accept full cache misses on each build.

### Caching Options

CodeBuild supports [two caching strategies](https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html):

| Cache Type | Modes Available | GPU Support | Notes |
|-----------|----------------|------------|-------|
| **Local cache** | Source cache, Docker layer cache, Custom cache | No | Sub-second restore; ephemeral per build host |
| **S3 cache** | Any artifact | Yes | Persistent; shared across fleet; adds S3 transfer latency |

- **Source cache:** Caches source files from the last build to reduce SCM fetch time
- **Docker layer cache:** Caches Docker image layers to accelerate image builds
- **Custom cache:** Caches any directory (e.g., `node_modules`, `~/.gradle`)

Source: [Cache Builds to Improve Performance](https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html)

### Custom Build Environments

ISVs can [specify custom Docker images](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) for build environments — sourced from ECR, Docker Hub, or any OCI-compatible registry. This allows ISVs to pre-bake language runtimes, toolchains, and internal certificates, dramatically reducing build-time setup.

### Free Tier

CodeBuild's free tier includes [100 build minutes per month](https://aws.amazon.com/codebuild/pricing/) using `general1.small` or `arm1.small` instance types on EC2 on-demand compute.

### Operational Burden Eliminated

| Self-Hosted Burden | CodeBuild Eliminates |
|-------------------|---------------------|
| Build agent provisioning and scaling | Fully managed; auto-scales to demand |
| OS/runtime patching | AWS manages underlying instances |
| Build environment drift | Immutable ephemeral containers per build |
| Queue management | Managed concurrency across fleet |
| Storage for artifacts | Native S3 integration; no artifact server |

### Operational Difficulty Rating

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Build Execution | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-hosted Jenkins agents or Tekton pods | K8s pod-based build agents | CodeBuild fully managed |
| | Jenkins agents, Buildah, Kaniko | Tekton, Kaniko, BuildKit | CodeBuild (EC2/Lambda) |
| Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.2 |

---

## AWS CodeDeploy: Deployment Automation

### Overview

[AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) is a fully managed deployment service that automates application deployments to EC2 instances, on-premises instances, AWS Lambda functions, and Amazon ECS services. Pricing is [free for EC2, Lambda, and ECS deployments](https://aws.amazon.com/codedeploy/pricing/); on-premises instance updates are charged at $0.02 per instance update.

### Deployment Target Platforms

| Platform | Blue/Green | Canary | Linear | Rollback |
|---------|-----------|--------|--------|---------|
| EC2/On-Premises | Yes | No | No | Yes (automatic or manual) |
| AWS Lambda | Yes | Yes | Yes | Yes (automatic via CloudWatch alarms) |
| Amazon ECS | Yes (via CodeDeploy) | Yes | Yes | Yes |
| Amazon ECS Native (2025) | Yes | No | No | Yes (circuit breaker) |

Source: [Working with Deployment Configurations in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)

### Traffic Shifting Strategies for ECS and Lambda

[CodeDeploy's pre-defined traffic shifting configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html) include:

- `CodeDeployDefault.ECSCanary10Percent5Minutes` — shifts 10% initially, then 100% after 5 minutes
- `CodeDeployDefault.ECSLinear10PercentEvery1Minutes` — increments 10% every 1 minute
- `CodeDeployDefault.ECSLinear10PercentEvery3Minutes` — increments 10% every 3 minutes
- `CodeDeployDefault.LambdaCanary10Percent5Minutes` — Lambda equivalent canary pattern

### Blue/Green Deployment Mechanics

In a CodeDeploy blue/green deployment:
1. A new "green" environment is provisioned alongside the live "blue" environment
2. Traffic is shifted per the configured strategy
3. CloudWatch alarm thresholds can trigger automatic rollback
4. The old "blue" environment is retained for the configured bake period, then terminated

Source: [AWS CodeDeploy Blue-Green Deployment Guide](https://medium.com/@praneethshettyy/aws-codedeploy-blue-green-deployment-rollback-guide-229c8aed7f22)

### 2025 Evolution: ECS Native Blue/Green

In July 2025, [Amazon ECS launched built-in blue/green deployments](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/) that operate directly within ECS without requiring CodeDeploy. Key differences:

| Attribute | CodeDeploy for ECS | ECS Native Blue/Green (2025) |
|----------|-------------------|------------------------------|
| Traffic shifting | Canary, Linear, All-at-once | All-at-once only |
| Lifecycle hook duration | Max 1 hour | Longer (managed by ECS) |
| CloudFormation support | Requires separate AppSpec | Native, no AppSpec needed |
| Circuit breaker | No | Yes |
| Deployment history | Via CodeDeploy console | Via ECS console |

**Recommendation from AWS:** [Use ECS native blue/green for most ECS workloads](https://aws.amazon.com/blogs/containers/migrating-from-aws-codedeploy-to-amazon-ecs-for-blue-green-deployments/); retain CodeDeploy only when canary or linear traffic shifting is required.

### Lifecycle Hooks

CodeDeploy supports [Lambda functions invoked during deployment lifecycle events](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-lambda.html) (e.g., `BeforeAllowTraffic`, `AfterAllowTraffic`) that can run automated tests, emit metrics, or perform custom validation before or after traffic shift.

### Operational Burden Eliminated

| Self-Hosted Burden | CodeDeploy Eliminates |
|-------------------|----------------------|
| Blue/green orchestration scripts | Declarative AppSpec configuration |
| Load balancer rule management | Automated ALB/NLB rule flipping |
| Rollback scripting | Automatic rollback via CloudWatch alarms |
| Deployment state tracking | Managed deployment history and status |
| SSH-based push deployments | Agent-based pull model; no inbound firewall rules |

### Operational Difficulty Rating

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Deployment Automation | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Custom Ansible/scripts; manual rollback | Argo Rollouts or Flux; K8s expertise required | CodeDeploy free for ECS/Lambda/EC2 |
| | Ansible, Fabric, custom shell | Argo Rollouts, Flagger | CodeDeploy, ECS native blue/green |
| Est. FTE: 0.5–0.75 | Est. FTE: 0.25–0.5 | Est. FTE: 0.05–0.1 |

---

## Amazon ECR: Managed Container Registry

### Overview

[Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/pricing/) is a fully managed OCI-compatible container registry. No registry server to provision, patch, or scale. Pricing is $0.10/GB-month for private repository storage and standard AWS data transfer rates for cross-region pulls; same-region pulls from EC2, ECS, Lambda, or Fargate are free.

### Vulnerability Scanning

ECR provides two scanning tiers:

| Scanning Type | Technology | Frequency | Coverage |
|--------------|-----------|-----------|---------|
| **Basic Scanning** | AWS-native CVE scanning | On push + manual (max 1x/24h) | OS packages; 50+ data feeds |
| **Enhanced Scanning** | Amazon Inspector integration | Continuous; updates as new CVEs emerge | OS + programming language packages |

Source: [Scan Images for Software Vulnerabilities in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)

Enhanced scanning via Amazon Inspector emits findings to Amazon EventBridge in real time as new vulnerabilities are published, enabling ISVs to build automated remediation workflows without polling.

### Lifecycle Policies

[ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic.html) automate cleanup of unused or expired images based on:
- Image count (keep only the N most recent tagged images)
- Image age (expire images older than N days)
- Tag status (untagged images are common cleanup targets)
- Tag prefix patterns

This eliminates the operational burden of manual registry hygiene and reduces storage costs without engineering intervention.

### Cross-Region Replication

[ECR supports both cross-Region and cross-account replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html) configured at the private registry level. Key attributes:

- Replication is automatic on image push; if the destination repository does not exist, ECR creates it
- Configuration supports up to 25 unique destinations across up to 10 rules; each rule supports up to 100 filters
- Data transfer is charged at [standard cross-region AWS data transfer rates](https://aws.amazon.com/ecr/pricing/)
- Benefits include reduced pull latency for multi-region deployments and geographic artifact distribution for disaster recovery

Source: [Cross Region Replication in Amazon ECR](https://aws.amazon.com/blogs/containers/cross-region-replication-in-amazon-ecr-has-landed/)

### Pull-Through Cache

ECR supports a [pull-through cache](https://marcincuber.medium.com/aws-ecr-pull-through-cache-cross-region-replication-with-terraform-plus-a-safe-way-to-backfill-91cbab27edea) for upstream public registries (Docker Hub, ECR Public, Quay, GitHub Container Registry), allowing ISVs to cache base images in a private ECR repository and apply lifecycle policies, vulnerability scanning, and IAM controls to third-party base images.

### ECR Public

[Amazon ECR Public](https://aws.amazon.com/blogs/containers/expanding-container-security-and-choice-with-amazon-ecr-public/) provides free public container image hosting with 50 GB/month free storage and 500 GB/month free anonymous pull bandwidth. ISVs distributing public container images benefit from no-cost distribution at scale.

### Operational Burden Eliminated

| Self-Hosted Burden | ECR Eliminates |
|-------------------|---------------|
| Registry server provisioning (Harbor, Nexus, Quay) | Fully managed |
| TLS certificate management | AWS-managed endpoints |
| Registry HA and failover | Built-in redundancy |
| IAM integration for pull access | Native IAM resource policies |
| Vulnerability scanner maintenance | AWS Inspector integration |
| Image GC scripting | Lifecycle policies |

### Operational Difficulty Rating

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Container Registry | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Harbor/Nexus; storage ops, TLS, HA | Harbor on K8s or cloud-hosted registry | ECR fully managed; IAM-native |
| | Harbor, Nexus, Quay | Harbor, JFrog Artifactory | Amazon ECR |
| Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05 |

---

## AWS CodeArtifact: Managed Artifact Repository

### Overview

[AWS CodeArtifact](https://aws.amazon.com/codeartifact/) is a fully managed artifact repository service for storing and sharing software packages across development teams. It eliminates the need to self-host Nexus, Artifactory, or Verdaccio instances.

### Supported Package Formats

[CodeArtifact supports the following package formats](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html):

| Format | Compatible Tools |
|--------|----------------|
| npm | npm CLI, yarn |
| PyPI | pip, twine |
| Maven | Maven, Gradle |
| NuGet | NuGet CLI, dotnet |
| Swift | Swift Package Manager |
| Ruby (Gems) | gem CLI, Bundler |
| Cargo (Rust) | cargo |
| Generic | Any tool supporting HTTP artifact upload |

Repositories are polyglot — a single repository can contain packages of any supported type. There is no limit on the number or total size of packages stored.

### Upstream Repositories and Public Proxy

[CodeArtifact's upstream repository feature](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html) allows a private repository to pull packages on-demand from public registries when requested by a package manager:

- npmjs.com → private npm packages
- PyPI.org → private Python packages
- Maven Central → private Java packages
- NuGet Gallery → private .NET packages

This enables ISVs to use a single package manager endpoint for both internal and open-source dependencies, with CodeArtifact caching and retaining the fetched packages in the private repository. Up to 10 upstream repositories can be chained to a single CodeArtifact repository.

Source: [Connect a CodeArtifact Repository to a Public Repository](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html)

### Domain Architecture

CodeArtifact uses a **domain** as the top-level organizational unit grouping multiple repositories. Domains enable [cross-repository package sharing and governance policies](https://aws.amazon.com/codeartifact/) applied at scale across all repositories within the domain.

### Pricing

[AWS CodeArtifact pricing](https://aws.amazon.com/codeartifact/pricing/) is consumption-based with a permanent free tier:

| Cost Component | Price | Free Tier |
|---------------|-------|-----------|
| Storage | $0.05/GB-month | 2 GB/month (always free) |
| Requests | $0.05/10,000 requests | 100,000 requests/month (always free) |
| Data transfer out | Standard AWS rates | — |
| Data transfer in | Free | — |

No charges for creating domains or repositories — pricing is purely consumption-based.

### Operational Burden Eliminated

| Self-Hosted Burden | CodeArtifact Eliminates |
|-------------------|------------------------|
| Nexus/Artifactory server provisioning | Fully managed |
| Storage management and cleanup | Storage billed as consumed |
| Upstream proxy configuration | Native external connections |
| IAM/LDAP integration for access | Native IAM resource policies |
| TLS and endpoint management | AWS-managed HTTPS endpoints |
| Replication across environments | Domain-level cross-account sharing |

### Operational Difficulty Rating

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Artifact Repository | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Nexus/Artifactory; storage, HA, patching | Nexus on K8s; persistent volume management | CodeArtifact fully managed |
| | Nexus, Artifactory, Verdaccio | Nexus, JFrog Artifactory | AWS CodeArtifact |
| Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05 |

---

## AWS CodeCommit: Status and Migration Path

### Current Status (November 2025)

[AWS CodeCommit returned to full General Availability on November 24, 2025](https://aws.amazon.com/blogs/devops/aws-codecommit-returns-to-general-availability/), reversing its July 2024 de-emphasis. The reversal was driven by customer feedback, particularly from teams in regulated industries that required an AWS-native, IAM-integrated Git repository service.

**Timeline:**
- July 2024: AWS announced plans to de-emphasize CodeCommit; new account sign-ups were closed
- November 2025: CodeCommit returned to full GA; new customers can create repositories immediately
- Early 2026: AWS plans to add Git Large File Storage (Git LFS) support
- 2026: Regional expansion planned, including Spain and Canada

Source: [AWS CodeCommit Returns to General Availability — InfoQ](https://www.infoq.com/news/2025/12/aws-codecommit-ga/)

### Value Proposition for Regulated ISVs

CodeCommit's differentiation relative to GitHub/GitLab:
- Deep AWS IAM integration — no separate user management
- VPC endpoint support — Git over private networking, no public internet egress
- AWS CloudTrail logging of all Git operations
- Seamless native integration with CodePipeline and CodeBuild

Source: [The Future of AWS CodeCommit](https://aws.amazon.com/blogs/devops/aws-codecommit-returns-to-general-availability/)

### Current Availability

[AWS CodeCommit is available in 29 regions](https://www.appgambit.com/blog/aws-codecommit-returns-to-general-availability-2025) as of November 2025.

### Migration Alternatives (for ISVs that migrated away during 2024-2025)

For ISVs that migrated CodeCommit repositories to external providers during the 2024 de-emphasis period, [AWS provides a migration guide](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/) supporting repository migration via Git clone, mirror, or branch-level migration. Recommended alternatives that CodePipeline now natively supports:

- **GitHub / GitHub Enterprise** — market-leading ecosystem; OIDC integration with AWS
- **GitLab.com / GitLab self-managed** — strong for ISVs needing self-hosted SCM
- **Bitbucket Cloud** — Atlassian ecosystem integration

---

## AWS Proton: Managed Delivery Service (End-of-Life Warning)

### Status

**AWS will discontinue AWS Proton on October 7, 2026.** [New customers cannot sign up after October 7, 2025.](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html) Existing customers can use the service until October 7, 2026. **ISVs currently using AWS Proton must plan and execute migrations before that date.**

### What Proton Was

[AWS Proton](https://aws.amazon.com/proton/) was a fully managed application delivery service that allowed platform engineering teams to define standard infrastructure templates (for ECS, Lambda, and EKS workloads) and expose them to developers as a self-service catalog. Platform teams managed template versions; Proton applied updates to deployed services when new versions were released.

### What Happens to Deployed Infrastructure

Per [AWS Proton deprecation guidance](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html): deployed CloudFormation stacks and the underlying resources they manage will remain intact after October 7, 2026. Only the Proton delivery service and console will be discontinued.

### Recommended Migration Paths

[AWS recommends the following alternatives](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html):

| Use Case | Recommended Alternative |
|---------|------------------------|
| GitOps workflow | CloudFormation Git Sync |
| Enterprise developer portal | Harmonix on AWS |
| Maximum flexibility | AWS CodePipeline + AWS CodeBuild |
| IaC-driven platform engineering | AWS Service Catalog + CloudFormation |

---

## GitHub Actions Integration with AWS

### OIDC Federation (Preferred Method)

[GitHub recommends using OpenID Connect (OIDC) to obtain short-lived AWS credentials](https://docs.github.com/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) rather than storing long-lived AWS access keys as GitHub Secrets. This is the current best practice as of 2025.

**How OIDC works:**
1. GitHub Issues a signed JWT for each workflow run via `https://token.actions.githubusercontent.com`
2. The workflow assumes an IAM role by presenting the JWT to AWS STS
3. AWS STS validates the JWT against the registered OIDC provider and returns short-lived credentials
4. Credentials expire automatically at job completion

Source: [Use IAM Roles to Connect GitHub Actions to Actions in AWS](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/)

### Workflow Configuration Requirements

For OIDC-based credential management, [GitHub Actions workflows require](https://docs.github.com/en/actions/concepts/security/openid-connect):

```yaml
permissions:
  id-token: write   # Required for OIDC JWT issuance
  contents: read
```

**IAM Trust Policy configuration:**
- OIDC provider URL: `https://token.actions.githubusercontent.com`
- Audience: `sts.amazonaws.com`
- `token.actions.githubusercontent.com:sub` condition key should be evaluated to restrict which repositories and branches can assume the role

Source: [Configuring OpenID Connect in Amazon Web Services — GitHub Docs](https://docs.github.com/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)

### Trust Policy Restriction Best Practices

[AWS IAM recommends evaluating the `token.actions.githubusercontent.com:sub` condition key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html) to limit which GitHub Actions runs can assume an IAM role. Example restrictions:

| Restriction | `sub` condition value |
|------------|----------------------|
| Specific repo, any branch | `repo:org/repo:*` |
| Specific repo, main branch only | `repo:org/repo:ref:refs/heads/main` |
| Specific repo, any environment | `repo:org/repo:environment:production` |

Source: [GitHub Actions on AWS: How to Implement Identity Federation](https://www.rkon.com/articles/github-actions-on-aws-how-to-implement-identity-federation/)

### aws-actions/configure-aws-credentials Action

The [`aws-actions/configure-aws-credentials` GitHub Action](https://github.com/aws-actions/configure-aws-credentials) handles OIDC token exchange automatically. It:
- Requests the OIDC JWT from GitHub
- Calls `sts:AssumeRoleWithWebIdentity` with the JWT
- Sets `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` as environment variables for subsequent steps

This eliminates the need for ISVs to store static IAM access keys in GitHub Secrets, reducing the blast radius of credential exposure.

### Operational Pattern: GitHub Actions + CodeBuild

ISVs can mix GitHub Actions for CI orchestration with AWS CodeBuild for build execution using the [CodeBuild GitHub source provider](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html), allowing GitHub Actions to trigger CodeBuild projects directly via OIDC-authenticated AWS API calls while retaining the GitHub ecosystem for PR reviews, status checks, and branch rules.

---

## Integrated Toolchain: Operational Profile Comparison

### Summary Difficulty Matrix

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|------------------|-------------|-------------|--------------|
| CI Orchestration | 4/5 | 3/5 | 2/5 |
| Build Execution | 4/5 | 3/5 | 2/5 |
| Deployment Automation | 4/5 | 3/5 | 1/5 |
| Container Registry | 4/5 | 3/5 | 1/5 |
| Artifact Repository | 4/5 | 3/5 | 1/5 |
| Source Control | 3/5 | 3/5 | 1/5 |
| **Aggregate (avg)** | **3.8/5** | **3.0/5** | **1.3/5** |

### Staffing Estimate: Complete AWS CI/CD Toolchain

*Assumptions: Mid-size ISV, 20–40 active pipelines, 50 enterprise customers, 5–15 active developers, production + staging environments.*

| Model | Active FTE | On-Call Burden | Notes |
|-------|-----------|---------------|-------|
| On-Premises (Jenkins + Harbor + Nexus + self-hosted Git) | 1.5–2.5 FTE | +0.25 FTE | Includes server ops, patching, plugin management |
| Managed K8s (Tekton + Harbor on K8s + Nexus on K8s) | 0.75–1.25 FTE | +0.15 FTE | K8s expertise required; persistent volume management |
| Cloud-Native (CodePipeline + CodeBuild + CodeDeploy + ECR + CodeArtifact) | 0.25–0.5 FTE | +0.05 FTE | IAM, pipeline config; no infrastructure ops |

[UNVERIFIED] FTE estimates above are derived from industry convention for managed vs. self-hosted CI/CD toolchain comparison. No 2025 peer-reviewed benchmark with these exact parameters was located. Individual service FTE estimates are calibrated against the self-hosted Jenkins operational cost data found in practitioner sources. The aggregate estimates are consistent with the observed range of practitioner reports that self-hosted Jenkins requires "dedicated engineers or Jenkins specialists" and that managed CI/CD reduces infrastructure overhead materially.

---

## Key Takeaways

- **AWS's managed CI/CD toolchain (CodePipeline + CodeBuild + CodeDeploy + ECR + CodeArtifact) reduces estimated operational staffing from 1.5–2.5 FTE for a fully self-hosted stack to 0.25–0.5 FTE**, with the difference attributable to the elimination of server provisioning, patching, plugin management, and availability engineering for each service.

- **AWS CodeCommit reversed its July 2024 deprecation and returned to full GA on November 24, 2025**, restoring a fully AWS-native, IAM-integrated, VPC-endpoint-accessible Git repository option; ISVs in regulated industries should reassess migration decisions made during 2024–2025.

- **AWS Proton is end-of-life on October 7, 2026** — ISVs using Proton for platform engineering must migrate to alternatives (CloudFormation Git Sync, AWS Service Catalog, or CodePipeline + CodeBuild) before that date; deployed CloudFormation stacks will survive the deprecation intact.

- **GitHub Actions OIDC federation with AWS IAM (via `aws-actions/configure-aws-credentials`) eliminates the need for long-lived IAM access keys in CI/CD workflows**, with short-lived STS credentials scoped to specific repositories and branches via the `token.actions.githubusercontent.com:sub` condition key.

- **ECR's July 2025 Amazon ECS native blue/green deployment feature reduces the operational footprint of CodeDeploy for ECS workloads** — ISVs should use ECS native blue/green for standard deployments and retain CodeDeploy only for canary and linear traffic-shifting strategies that ECS native does not support.

---

## Related — Out of Scope

- **Azure DevOps Pipelines, GitHub Actions compute (F13/F15):** The GitHub Actions runner infrastructure and Azure-equivalent CI/CD services are outside this agent's scope. See F13 (Azure CI/CD) and relevant agents for cross-provider comparison.
- **AWS Compute Services (F8):** CodeBuild build environment integration with ECS, EKS, and Lambda compute is covered in F8.
- **IaC and GitOps (F16/F17):** AWS CDK Pipelines, CloudFormation Git Sync, and Terraform Cloud integrations with CodePipeline are outside this scope.
- **Cost optimization across deployment models:** Aggregate CI/CD cost modeling across deployment scenarios is outside this agent's scope.

---

## Sources

1. [AWS CodePipeline — Product Page](https://aws.amazon.com/codepipeline/)
2. [AWS CodePipeline Features](https://aws.amazon.com/codepipeline/features/)
3. [AWS CodePipeline Pricing](https://aws.amazon.com/codepipeline/pricing/)
4. [Define CI/CD Pipelines with Stages and Actions — AWS Docs](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines.html)
5. [CodePipeline Supports Additional Trigger Filters and New Execution Modes — AWS What's New](https://aws.amazon.com/about-aws/whats-new/2024/02/codepipeline-trigger-filters-execution-modes/)
6. [Enhance Release Control with AWS CodePipeline Stage-Level Conditions — AWS DevOps Blog](https://aws.amazon.com/blogs/devops/enhance-release-control-with-aws-codepipeline-stage-level-conditions/)
7. [AWS CodePipeline Adds Support for Branch-Based Development and Monorepos — AWS DevOps Blog](https://aws.amazon.com/blogs/devops/aws-codepipeline-adds-support-for-branch-based-development-and-monorepos/)
8. [Integrations with CodePipeline Action Types — AWS Docs](https://docs.aws.amazon.com/codepipeline/latest/userguide/integrations-action-type.html)
9. [CodeStarSourceConnection for Bitbucket, GitHub, GitLab — AWS Docs](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html)
10. [AWS CodeBuild — Product Page](https://aws.amazon.com/codebuild/)
11. [AWS CodeBuild Pricing](https://aws.amazon.com/codebuild/pricing/)
12. [Build Environment Compute Modes and Types — AWS CodeBuild Docs](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html)
13. [Cache Builds to Improve Performance — AWS CodeBuild Docs](https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html)
14. [Local Caching — AWS CodeBuild Docs](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-local.html)
15. [AWS CodeBuild Now Supports a Small GPU Machine Type — AWS What's New](https://aws.amazon.com/about-aws/whats-new/2023/03/aws-codebuild-small-gpu-machine-type/)
16. [AWS CodeBuild Adds Support for Specifying EC2 Instance Type and Configurable Storage Size — AWS What's New, April 2025](https://aws.amazon.com/about-aws/whats-new/2025/04/aws-codebuild-ec2-instance-type-configurable-storage-size/)
17. [Run Builds on Reserved Capacity Fleets — AWS CodeBuild Docs](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html)
18. [Reserved Capacity Fleet Properties — AWS CodeBuild Docs](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.reserved-capacity-fleets.html)
19. [What is CodeDeploy? — AWS Docs](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
20. [AWS CodeDeploy Pricing](https://aws.amazon.com/codedeploy/pricing/)
21. [Working with Deployment Configurations in CodeDeploy — AWS Docs](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
22. [Deployments on an AWS Lambda Compute Platform — AWS CodeDeploy Docs](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-lambda.html)
23. [Choosing Between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK — AWS DevOps Blog](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/)
24. [Migrating from AWS CodeDeploy to Amazon ECS for Blue/Green Deployments — AWS Containers Blog](https://aws.amazon.com/blogs/containers/migrating-from-aws-codedeploy-to-amazon-ecs-for-blue-green-deployments/)
25. [CodeDeploy Blue/Green Deployments for Amazon ECS — ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html)
26. [Amazon ECR Pricing](https://aws.amazon.com/ecr/pricing/)
27. [Scan Images for Software Vulnerabilities in Amazon ECR — ECR Docs](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
28. [Scan Images for OS Vulnerabilities in Amazon ECR — ECR Docs](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-basic.html)
29. [Private Image Replication in Amazon ECR — ECR Docs](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html)
30. [Cross Region Replication in Amazon ECR Has Landed — AWS Containers Blog](https://aws.amazon.com/blogs/containers/cross-region-replication-in-amazon-ecr-has-landed/)
31. [Expanding Container Security and Choice with Amazon ECR Public — AWS Containers Blog](https://aws.amazon.com/blogs/containers/expanding-container-security-and-choice-with-amazon-ecr-public/)
32. [Scanning Amazon ECR Container Images with Amazon Inspector — Amazon Inspector Docs](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html)
33. [AWS ECR Pull-Through Cache and Cross-Region Replication with Terraform — Medium/Marcin Cuber](https://marcincuber.medium.com/aws-ecr-pull-through-cache-cross-region-replication-with-terraform-plus-a-safe-way-to-backfill-91cbab27edea)
34. [AWS CodeArtifact — Product Page](https://aws.amazon.com/codeartifact/)
35. [AWS CodeArtifact Pricing](https://aws.amazon.com/codeartifact/pricing/)
36. [What is AWS CodeArtifact? — CodeArtifact Docs](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html)
37. [Working with Upstream Repositories in CodeArtifact — AWS Docs](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html)
38. [Connect a CodeArtifact Repository to a Public Repository — AWS Docs](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html)
39. [The Future of AWS CodeCommit — AWS DevOps Blog](https://aws.amazon.com/blogs/devops/aws-codecommit-returns-to-general-availability/)
40. [AWS CodeCommit Returns to General Availability — InfoQ, December 2025](https://www.infoq.com/news/2025/12/aws-codecommit-ga/)
41. [AWS CodeCommit Returns to GA — APPGAMBiT Blog](https://www.appgambit.com/blog/aws-codecommit-returns-to-general-availability-2025)
42. [How to Migrate Your AWS CodeCommit Repository to Another Git Provider — AWS DevOps Blog](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/)
43. [AWS Proton — Product Page](https://aws.amazon.com/proton/)
44. [AWS Proton Service Deprecation and Migration Guide — AWS Proton Docs](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html)
45. [What is AWS Proton? — AWS Proton Docs](https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html)
46. [Configuring OpenID Connect in Amazon Web Services — GitHub Docs](https://docs.github.com/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
47. [Use IAM Roles to Connect GitHub Actions to Actions in AWS — AWS Security Blog](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/)
48. [OIDC Federation — AWS IAM Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)
49. [OpenID Connect — GitHub Docs](https://docs.github.com/en/actions/concepts/security/openid-connect)
50. [aws-actions/configure-aws-credentials — GitHub](https://github.com/aws-actions/configure-aws-credentials)
51. [GitHub Actions on AWS: How to Implement Identity Federation — RKON](https://www.rkon.com/articles/github-actions-on-aws-how-to-implement-identity-federation/)
52. [Understanding Data Transfer Costs for AWS Container Services — AWS Containers Blog](https://aws.amazon.com/blogs/containers/understanding-data-transfer-costs-for-aws-container-services/)
