# F15a — AWS Per-Service Infrastructure Integration

**Research Agent:** F15a — AWS Per-Service Infrastructure Integration
**Date:** 2026-02-18
**Scope:** Cross-cutting per-service infrastructure integration across AWS managed service domains

---

## Executive Summary

AWS provides a layered, per-service integration model in which each compute type — Lambda, ECS/Fargate, App Runner, and SageMaker endpoints — requires a distinct wiring pattern across eight infrastructure domains: CI/CD pipelines, health-check endpoints, service discovery, load balancer ingress, observability instrumentation, container image lifecycle, secrets management, and alerting. In July 2025, AWS launched [ECS-native blue/green deployments](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/), consolidating what previously required CodeDeploy orchestration into a single service — a signal that AWS is actively simplifying per-service operational overhead. Concurrently, AWS App Mesh was deprecated effective September 30, 2026, with [ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/) becoming the recommended service-to-service networking primitive; ISVs must account for this migration in greenfield architectures. The overall integration surface across a production-ready service is non-trivial: a single ECS Fargate service requires coordinated configuration across at least six distinct AWS control planes before it is operationally sound, making a structured onboarding checklist essential for consistent, repeatable deployments.

---

## Section 1 — CI/CD Pipeline Patterns Per Service Type

### 1.1 Lambda: CodeDeploy Traffic-Shifting Model

Lambda deployments differ fundamentally from container-based deployments: the artifact is a function version or container image, and the deployment mechanism is alias-based traffic shifting managed by [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html).

[FACT]
"When you deploy to an AWS Lambda compute platform, the deployment configuration specifies the way traffic is shifted to the new Lambda function versions in your application, with options to shift traffic using a canary, linear, or all-at-once deployment configuration."
— AWS CodeDeploy Documentation
URL: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html

**Predefined CodeDeploy configurations for Lambda:**

| Configuration | Traffic Shift | Use Case |
|---|---|---|
| `LambdaCanary10Percent5Minutes` | 10% for 5 min, then 100% | Low-risk canary |
| `LambdaLinear10PercentEvery1Minute` | 10% per minute | Gradual rollout |
| `LambdaAllAtOnce` | 100% immediate | Dev/test deployments |

[FACT]
"AWS Serverless Application Model (AWS SAM) comes built-in with CodeDeploy to provide gradual AWS Lambda deployments, and with just a few lines of configuration, AWS SAM deploys new versions of your Lambda function while automatically creating aliases that point to the new version."
— AWS SAM Documentation
URL: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html

**Pipeline topology (Lambda):**
`Source (GitHub/CodeCommit) → CodeBuild (build + unit test + package) → CodeDeploy (alias traffic shift) → CloudWatch Alarms (auto-rollback trigger)`

### 1.2 ECS/Fargate: ECS-Native Blue/Green (Post-July 2025)

[FACT]
"In July 2025, Amazon ECS launched built-in blue/green deployments, which allows you to operate directly within the ECS service, without requiring the use of Amazon CodeDeploy. Using ECS-native blue/green deployments is now the recommended default for most teams."
— AWS DevOps Blog
URL: https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/

[FACT]
"ECS-native blue/green provisions a replacement task set registered to a separate target group (blue target group) behind your Elastic Load Balancing listener. When you approve the cutover, ECS performs an all-at-once traffic shift to the green revision, then holds both revisions during a configurable bake period before retiring blue or rolling back if alarms or hooks fail."
— AWS DevOps Blog
URL: https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/

**When to retain CodeDeploy for ECS:**
- Canary or linear traffic shifting is required (ECS-native is all-at-once only)
- Multi-account pipeline integrations that already depend on CodeDeploy event model

**Pipeline topology (ECS/Fargate):**
`Source → CodeBuild (build image + push to ECR) → ECR image push event → CodePipeline → ECS UpdateService (blue/green) → Bake period + CloudWatch alarm gate → Retire old task set`

For ECS standard rolling deployments, the [ECS Standard Deployment tutorial](https://docs.aws.amazon.com/codepipeline/latest/userguide/ecs-cd-pipeline.html) with `imagedefinitions.json` artifact remains viable for non-zero-downtime-critical workloads.

### 1.3 App Runner: ECR-Triggered Automatic Deployments

App Runner decouples deployment from CI tooling: the service monitors an ECR repository directly and deploys on new image push.

[FACT]
"App Runner supports continuous integration and deployment from the Amazon ECR repository. When continuous deployment is configured, an update to the container image in the Amazon ECR repository automatically initiates an update in App Runner. To configure automatic deployments, you can set `autoDeploymentsEnabled` to true."
— AWS Containers Blog
URL: https://aws.amazon.com/blogs/containers/build-and-deploy-a-spring-boot-application-to-aws-app-runner-with-a-ci-cd-pipeline-using-terraform/

**Pipeline topology (App Runner):**
`Source → CodeBuild (build + push to ECR) → ECR image push → App Runner auto-deploy (if enabled) OR CodePipeline manual approval gate → App Runner deploy API`

App Runner does not support CodeDeploy traffic shifting or canary rollouts natively; deployments are atomic (all-at-once).

### 1.4 SageMaker Endpoints: SageMaker Pipelines + CodePipeline MLOps Pattern

SageMaker endpoints require a two-stage CI/CD system: a model training pipeline (SageMaker Pipelines) and a model deployment pipeline (CodePipeline + CodeDeploy or EventBridge triggers).

[FACT]
"Amazon SageMaker Pipelines is a purpose-built, easy-to-use continuous integration and continuous delivery (CI/CD) service for machine learning that serves as a native workflow orchestration tool for building ML pipelines with direct Amazon SageMaker integration."
— AWS Machine Learning Blog
URL: https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/

[FACT]
"When a model is approved, an EventBridge rule launches the CodePipeline CI/CD pipeline with model deployment."
— AWS Machine Learning Blog
URL: https://aws.amazon.com/blogs/machine-learning/safely-deploying-and-monitoring-amazon-sagemaker-endpoints-with-aws-codepipeline-and-aws-codedeploy/

**Pipeline topology (SageMaker):**
`Data change / schedule → SageMaker Pipelines (preprocess + train + evaluate) → Model Registry (manual or automatic approval) → EventBridge rule → CodePipeline (deploy endpoint) → SageMaker Endpoint UpdateEndpoint + deployment guardrails`

---

## Section 2 — Health-Check Endpoints Per Compute Model

### 2.1 ALB Target Group Health Checks (All Container Services)

[FACT]
"Health checks can be configured on a per target group basis, and are performed on all targets registered to a target group that is specified in a listener rule for your load balancer."
— AWS ELB Documentation
URL: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html

[FACT]
"For services with tasks using the awsvpc network mode, when you create a target group for your service, you must choose ip as the target type, not instance, because tasks that use the awsvpc network mode are associated with an elastic network interface, not an Amazon EC2 instance."
— AWS ECS Documentation (ALB integration)
URL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb.html

[FACT]
"If a service task fails the load balancer health check criteria, the task is stopped and restarted."
— AWS re:Post Knowledge Center
URL: https://repost.aws/knowledge-center/troubleshoot-unhealthy-checks-ecs

### 2.2 ECS Container Health Checks (Complementary Layer)

ECS supports a separate, container-level health check defined in the task definition, independent of ALB checks:

[FACT]
"The Health Check Grace Period is specific to Amazon ECS and gives your ECS tasks time to start up and initialize before they're subject to ECS health checks, but it does not affect the ALB's health checks on the target group."
— AWS re:Post
URL: https://repost.aws/questions/QUdmR0oMn2Spa61RpKGWyPfg/ecs-should-i-use-alb-healthchecks-container-healthchecks-or-both

**Recommended pattern:** Use both ALB health checks (for traffic routing decisions) AND ECS container health checks (for task replacement decisions). They serve different purposes: ALB removes unhealthy targets from the rotation; ECS container health checks replace the task entirely.

### 2.3 App Runner Health Check Configuration

App Runner performs automatic health monitoring — no ALB or Route 53 health check configuration is required by the operator.

[FACT]
"The default health check protocol is TCP. App Runner pings the domain assigned to your service. You can alternatively set the health check protocol to HTTP. App Runner sends health check HTTP requests to your web application."
— AWS App Runner Documentation
URL: https://docs.aws.amazon.com/apprunner/latest/dg/manage-configure-healthcheck.html

[FACT]
"By default, if there are 5 consecutive health check failures, the instance is considered unhealthy and App Runner will replace it. You can configure the number of health checks that must fail before App Runner decides that the service is unhealthy, from 1 to 20."
— AWS App Runner Documentation
URL: https://docs.aws.amazon.com/apprunner/latest/dg/manage-configure-healthcheck.html

**Configurable App Runner health-check parameters:**

| Parameter | Type | Range | Default |
|---|---|---|---|
| Protocol | HTTP / TCP | — | TCP |
| Path | String | — | `/` (HTTP only) |
| Interval | Seconds | 1–20 | 5 |
| Timeout | Seconds | 1–20 | 2 |
| Healthy threshold | Count | 1–20 | 1 |
| Unhealthy threshold | Count | 1–20 | 5 |

### 2.4 Lambda: No Persistent Health-Check Endpoint

Lambda functions are event-driven and stateless; there is no persistent process to health-check. ALB invokes Lambda functions directly as targets:

[FACT]
"If the target type of your target group is lambda, you can register a single Lambda function, and when the load balancer receives a request for the Lambda function, it invokes the Lambda function."
— AWS ELB Documentation
URL: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html

For Lambda, "health" is determined by invocation success/failure (monitored via CloudWatch `Errors` metric) rather than a polling endpoint.

---

## Section 3 — Service Registry and Discovery

### 3.1 AWS Cloud Map: DNS and API Discovery

[FACT]
"Service discovery uses AWS Cloud Map API actions to manage HTTP and DNS namespaces for your Amazon ECS services. Amazon ECS is tightly integrated with AWS Cloud Map to enable service discovery for compute workloads running in ECS. When you enable service discovery for ECS services, it automatically keeps track of all task instances in AWS Cloud Map."
— AWS ECS Documentation
URL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html

[FACT]
"Both DNS and API service discovery are now supported by the AWS Cloud Map service discovery. Supported DNS record types are A, AAAA, SRV, and CNAME. API discovery lets you filter by custom attributes, which DNS can't do. This is useful for canary deployments where you want to route some traffic to a new version."
— OneUptime Blog
URL: https://oneuptime.com/blog/post/2026-02-12-aws-cloud-map-service-discovery/view

### 3.2 ECS Service Connect (Current Standard — App Mesh Replacement)

[FACT]
"At re:Invent 2022, AWS introduced Amazon ECS Service Connect, a new way to connect microservices within Amazon Elastic Container Service. AWS is clearly signaling that ECS users should move to ECS Service Connect — a native, simpler, and tightly-integrated service networking capability."
— AWS Containers Blog
URL: https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/

[FACT]
"Service Connect improves the reliability of containerized microservices through built-in health checks, outlier detection, and retry mechanisms. It also enhances observability by sending application-level networking metrics to Amazon CloudWatch. By using a managed networking data plane, Service Connect eliminates the undifferentiated heavy lifting associated with managing sidecar proxies."
— AWS Containers Blog
URL: https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/

[FACT]
"The benefit that ECS Service Connect brings over ECS Service Discovery using plain Cloud Map is faster failover when service instances go down."
— CloudKeeper Blog
URL: https://www.cloudkeeper.com/insights/blog/amazon-ecs-service-communication-via-service-discovery-connect

### 3.3 App Mesh Deprecation Notice (Critical ISV Action Item)

[FACT]
"On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources."
— AWS App Mesh Documentation
URL: https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html

[FACT]
"An Amazon ECS Service can't simultaneously be part of both an App Mesh Mesh and a Service Connect Namespace. Therefore, to perform a migration, the Amazon ECS Services must be recreated. To avoid downtime during this process you can implement a blue/green migration strategy."
— AWS Containers Blog
URL: https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/

**Discovery method selection matrix:**

| Use Case | Recommended Discovery Method |
|---|---|
| ECS service-to-service (same cluster) | ECS Service Connect |
| ECS service-to-service (cross-cluster) | Cloud Map API / DNS |
| Canary traffic splitting by attribute | Cloud Map API |
| App Runner inter-service | Cloud Map (HTTP namespace) |
| Lambda invocation | Direct ARN / API Gateway |
| SageMaker endpoint | IAM-authenticated InvokeEndpoint API |

---

## Section 4 — Load Balancer and Ingress Integration

### 4.1 ECS/Fargate → ALB (IP Target Type)

ECS Fargate tasks with `awsvpc` networking register as IP targets in ALB target groups. Path-based and host-based routing rules are configured at the ALB listener level.

[FACT]
"For services with tasks using the awsvpc network mode, you must choose ip as the target type, not instance."
— AWS ECS Documentation
URL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb.html

### 4.2 Lambda → ALB (Direct Target Registration)

[FACT]
"ALB supports Lambda functions as targets, where the load balancer invokes the registered Lambda function when receiving a request."
— AWS ELB Documentation
URL: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html

ALB converts HTTP requests to JSON events before invoking Lambda, and converts the Lambda response JSON back to HTTP. Only one Lambda function per target group; weighted routing across Lambda versions requires Lambda aliases with weighted aliases rather than ALB target groups.

### 4.3 API Gateway Integration Patterns

[FACT]
"HTTP APIs allow connecting a single VPC link to multiple ALBs, NLBs, or resources registered with an AWS Cloud Map service, providing a fan-out approach to connect with multiple backend microservices within the same VPC."
— AWS Compute Blog
URL: https://aws.amazon.com/blogs/compute/configuring-private-integrations-with-amazon-api-gateway-http-apis/

[FACT]
"VPC link v2 now enables direct private ALB integration for REST APIs, eliminating the need for an intermediary NLB, which removes the need for an intermediate NLB and reduces the number of hops between client and services."
— AWS Compute Blog
URL: https://aws.amazon.com/blogs/compute/build-scalable-rest-apis-using-amazon-api-gateway-private-integration-with-application-load-balancer/

### 4.4 App Runner: No Customer-Managed Load Balancer

App Runner manages its own internal load balancing and TLS termination. Customers do not configure ALB target groups for App Runner services. External access is via the App Runner-provisioned HTTPS endpoint or a custom domain.

**Load balancer and ingress integration comparison:**

| Capability | Lambda | ECS/Fargate | App Runner | SageMaker |
|---|---|---|---|---|
| Customer-managed LB | ALB (ip target) | ALB (ip target) / NLB | None (managed) | None (managed API) |
| Target type | lambda | ip | N/A | N/A |
| Weighted routing | Lambda alias weights | ALB weighted target groups | Not supported | Not applicable |
| API Gateway integration | Direct Lambda proxy | VPC Link + ALB/NLB | VPC Link (HTTP API) | Not typical |
| Path-based routing | ALB listener rules | ALB listener rules | App Runner paths | Endpoint URL |
| TLS termination | ALB / API GW | ALB / API GW | Managed by App Runner | Managed |

---

## Section 5 — Observability Instrumentation Per Service

### 5.1 Native CloudWatch Metrics (Zero Configuration)

Each AWS compute service emits a set of CloudWatch metrics without any SDK integration:

- **Lambda:** `Invocations`, `Errors`, `Duration`, `Throttles`, `ConcurrentExecutions`, `IteratorAge` (streams) — [AWS Lambda CloudWatch Metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html)
- **ECS:** `CPUUtilization`, `MemoryUtilization`, `RunningTaskCount`, `ServiceCount` — emitted per service and per cluster
- **App Runner:** Request-level metrics and instance-level CPU/memory via CloudWatch
- **SageMaker Endpoints:** `Invocations`, `Invocations4XXErrors`, `Invocations5XXErrors`, `ModelLatency`, `OverheadLatency`, `CPUUtilization`, `MemoryUtilization` — [AWS SageMaker CloudWatch Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)

[FACT]
"The AWS/SageMaker namespace includes request metrics from calls to InvokeEndpoint, available at a 1-minute frequency. Overall endpoint latency consists of three components: Network latency, Overhead latency, and Model latency."
— AWS SageMaker Documentation
URL: https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html

### 5.2 Distributed Tracing: X-Ray / ADOT Per Compute Type

AWS now recommends OpenTelemetry via AWS Distro for OpenTelemetry (ADOT) as the instrumentation standard, with X-Ray as the backend:

[FACT]
"AWS now recommends adopting OpenTelemetry as the observability solution for instrumenting cloud applications, with X-Ray transitioning to OpenTelemetry through AWS Distro for OpenTelemetry (ADOT) and OpenTelemetry SDKs."
— InfoQ, November 2025
URL: https://www.infoq.com/news/2025/11/aws-opentelemetry/

**Tracing instrumentation patterns by compute type:**

| Compute | ADOT Deployment | Auto-Instrumentation | Manual SDK |
|---|---|---|---|
| Lambda | ADOT Managed Lambda Layer | Yes (Java, Node.js, Python) | Optional |
| ECS/Fargate | ADOT sidecar container | Partial (via SDK) | Required for app code |
| App Runner | ADOT sidecar (co-located) | Partial | Required for app code |
| EC2 | ADOT daemon | No | Required |

[FACT]
"ADOT includes fully managed AWS Lambda Layers, which include an OpenTelemetry SDK and the ADOT Collector to auto-instrument your function for tracing with X-Ray."
— AWS Distro for OpenTelemetry Documentation
URL: https://aws-otel.github.io/docs/getting-started/lambda/

[FACT]
"Since Fargate doesn't support daemonsets, you have to deploy X-Ray as a sidecar container. Setting up a sidecar with X-Ray Daemon is simple — you just need to add a container that would run X-Ray Daemon to the same task."
— GitHub: aws-samples/aws-xray-fargate
URL: https://github.com/aws-samples/aws-xray-fargate

[FACT]
"A blog from March 2025 demonstrates how to employ a single instance of an ADOT Collector to collect X-Ray traces and Prometheus metrics from Amazon ECS services dynamically discovered using AWS Cloud Map."
— AWS Containers Blog
URL: https://aws.amazon.com/blogs/containers/metrics-and-traces-collection-from-amazon-ecs-using-aws-distro-for-opentelemetry-with-dynamic-service-discovery/

### 5.3 Structured Logging and Embedded Metric Format (EMF)

[FACT]
"The CloudWatch embedded metric format is a JSON specification used to instruct CloudWatch Logs to automatically extract metric values embedded in structured log events. Embedded metric format helps you generate actionable custom metrics from ephemeral resources such as Lambda functions and containers."
— AWS CloudWatch Documentation
URL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html

[FACT]
"Amazon CloudWatch supports high resolution metric extraction with up to 1 second granularity from structured logs using Embedded Metric Format (EMF). The maximum number of metric dimensions has been increased from 10 to 30, allowing customers to create custom metrics using EMF logs with up to 30 dimensions."
— AWS CloudWatch EMF Specification
URL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html

[FACT]
"The easiest way to deploy the CloudWatch agent on Amazon ECS is to run it as a sidecar, defining it in the same task definition as your application."
— AWS Observability Best Practices
URL: https://aws-observability.github.io/observability-best-practices/guides/signal-collection/emf/

**EMF is available for:** Lambda (natively, no agent needed), ECS (via CloudWatch Agent sidecar), App Runner (via CloudWatch Agent sidecar), EC2.

---

## Section 6 — Container Image Lifecycle (ECR Integration)

### 6.1 Scanning Tiers: Basic vs. Enhanced

[FACT]
"Amazon Elastic Container Registry (ECR) offers two scanning options: basic scanning and enhanced scanning. Basic scanning uses the open-source project Clair to check images for vulnerabilities and runs automatically on image push. Continuous rescanning of stored images requires enhanced scanning with Amazon Inspector."
— AWS ECR Documentation
URL: https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html

[FACT]
"Enhanced scanning is powered by Amazon Inspector and offers significant advantages, including support for scratch, distroless, and Chainguard base images (announced March 2025). It provides continuous rescanning, supports a wider range of operating systems, and integrates findings directly with AWS Security Hub."
— AWS ECR Enhanced Scanning Documentation
URL: https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-enhanced.html

### 6.2 Inspector: Runtime Container Correlation (2025)

[FACT]
"Amazon Inspector now maps Amazon ECR images to running containers, enabling security teams to prioritize vulnerabilities based on containers currently running in your environment. Inspector now maps ECR images to specific ECS tasks and EKS pods, correlating vulnerabilities found in an image with the exact active containers using that image."
— AWS News Blog
URL: https://aws.amazon.com/blogs/aws/amazon-inspector-enhances-container-security-by-mapping-amazon-ecr-images-to-running-containers/

### 6.3 Pipeline Vulnerability Gating

[FACT]
"AWS CodePipeline introduced the ECRBuildAndPublish action and the AWS InspectorScan action, where the ECRBuildAndPublish action enables building a docker image and publishing it to ECR as part of pipeline execution, and the InspectorScan action enables scanning source code or docker images as part of pipeline execution."
— AWS What's New
URL: https://aws.amazon.com/about-aws/whats-new/2024/11/aws-codepipeline-publishing-ecr-image-aws-inspectorscan-actions/

[FACT]
"Organizations can implement stage-level conditions including an 'On Success' condition that fails if Amazon ECR image scanning detects critical severity findings, using the AWS Lambda Invoke rule provider."
— AWS DevOps Blog
URL: https://noise.getoto.net/2024/10/16/enhance-release-control-with-aws-codepipeline-stage-level-conditions/

### 6.4 Lifecycle Policies and Image Promotion

[FACT]
"Implement ECR lifecycle policies to automatically purge old or unused images. This not only saves storage costs but also reduces clutter and the attack surface. For example, you could configure a lifecycle policy to retain only the last N images or remove images older than 90 days."
— Wiz Academy
URL: https://www.wiz.io/academy/container-security/aws-container-scanning

**Recommended per-environment ECR repository pattern:**

| Environment | Repository | Lifecycle Policy | Scanning |
|---|---|---|---|
| dev | `<service>/dev` | Retain last 5 images | Basic on push |
| staging | `<service>/staging` | Retain last 10 images | Enhanced continuous |
| prod | `<service>/prod` | Retain last 30 images | Enhanced continuous + Security Hub |

**Promotion flow:** Build in dev → Inspector scan gate → tag-copy to staging (no rebuild) → manual approval → tag-copy to prod. Tag-copy (not rebuild) ensures the same binary artifact is promoted.

---

## Section 7 — Secrets Management Integration Per Service Type

### 7.1 ECS Task Definition Secrets Injection

[FACT]
"Amazon ECS enables you to inject sensitive data into your containers stored in either AWS Secrets Manager secrets or AWS Systems Manager Parameter Store parameters. This feature is supported by tasks using both the EC2 and Fargate launch types."
— AWS ECS Documentation
URL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-secrets-manager.html

Secrets are specified in the `secrets` array of a container definition using the full ARN. They are resolved at task launch time and injected as environment variables. Rotation of a secret requires a task restart to pick up new values unless the application uses client-side caching.

### 7.2 Lambda: Parameters and Secrets Lambda Extension

[FACT]
"To use parameters from Parameter Store in AWS Lambda functions without using an SDK, you can use the AWS Parameters and Secrets Lambda Extension. When you use the AWS Parameters and Secrets Lambda Extension, the extension retrieves the parameter value from Parameter Store and stores it in the local cache. The cached value is used for further invocations until it expires."
— AWS Systems Manager Documentation
URL: https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html

The extension runs as a Lambda Layer and exposes a local HTTP endpoint (`http://localhost:2773`) that the function calls to retrieve secrets — avoiding the overhead of a full SDK call on every invocation.

### 7.3 SageMaker Endpoints: IAM Execution Role Pattern

[FACT]
"Amazon SageMaker performs operations on your behalf using other AWS services, and you must grant SageMaker permissions to use these services and resources they act upon using an AWS Identity and Access Management (IAM) execution role."
— AWS SageMaker Documentation
URL: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html

[FACT]
"How Amazon SageMaker AI uses AWS Secrets Manager: You can manage your private repositories credentials using Secrets Manager with SageMaker notebook instances."
— AWS Secrets Manager Documentation
URL: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-sagemaker.html

SageMaker inference containers access secrets via the IAM execution role attached to the endpoint — the role allows `secretsmanager:GetSecretValue`. Environment variables can be passed at endpoint creation time via `ContainerEnvironment` in the model configuration, but secrets should not be passed as plaintext environment variables; the preferred pattern is to grant the execution role Secrets Manager access and have the inference code retrieve secrets at startup.

### 7.4 RDS Credential Rotation: Zero-Downtime Pattern

[FACT]
"AWS Secrets Manager automatically triggers a Lambda function based on a configured rotation schedule, which initiates a secure credential rotation workflow. The process follows four steps: createSecret, setSecret, testSecret, and finishSecret. Secrets Manager maintains two versions during rotation: AWSCURRENT (the active credentials) and AWSPENDING (the new credentials being validated)."
— AWS Security Blog
URL: https://aws.amazon.com/blogs/security/rotate-amazon-rds-database-credentials-automatically-with-aws-secrets-manager/

[FACT]
"A pattern describes how to rotate secrets secured with AWS Secrets Manager within containers without requiring container restart. The approach uses the Secrets Manager client-side caching component to refresh credentials within the application. When the rotation period elapses, the cached credential expires and triggers an authentication error, prompting the Secrets Manager client to refresh the secret and re-establish the connection."
— AWS Prescriptive Guidance
URL: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/rotate-database-credentials-without-restarting-containers.html

**Rotation strategy selection:**

| Strategy | Behavior | Use Case |
|---|---|---|
| Single-user rotation | Updates password for the one user | Simple applications |
| Alternating-users rotation | Two users; swap active user | Zero-downtime, connection-pool-sensitive apps |

### 7.5 Cross-Service Secrets Summary

| Service | Primary Access Method | Rotation Handling | Restart Required? |
|---|---|---|---|
| ECS Fargate | Task definition `secrets` ARN | App must implement client cache | Yes (unless client cache) |
| Lambda | Parameters & Secrets Extension (cached) | Extension handles cache refresh | No |
| App Runner | Environment variable (Secrets Manager ARN) | App must implement client cache | Yes (unless client cache) |
| SageMaker Endpoint | IAM role + SDK call in container | App code handles refresh | No |
| RDS (any compute) | Secrets Manager auto-rotation (Lambda) | Client-side caching library | No (with caching library) |

---

## Section 8 — Service-Level Alerting Patterns

### 8.1 Lambda Alerting

[FACT]
"Key Lambda metrics to monitor include Errors (tracking failed function executions), Invocations (total function calls), Duration (execution time), and Throttles (rejected execution requests)."
— AWS Lambda Documentation
URL: https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html

[FACT]
"For memory monitoring specifically, for critical functions, implement multi-level alerts: set a warning at 70% memory usage and a critical alert at 90%."
— AWS for Engineers Blog
URL: https://awsforengineers.com/blog/lambda-error-monitoring-best-practices/

**Recommended Lambda alarms:**

| Metric | Statistic | Suggested Threshold | Alarm Purpose |
|---|---|---|---|
| `Errors` | Sum > 0 (or error rate %) | 1% of invocations | Error rate SLO |
| `Duration` | p99 | 80% of function timeout | Latency SLO |
| `Throttles` | Sum | > 0 sustained | Concurrency saturation |
| `ConcurrentExecutions` | Max | > 80% of account limit | Capacity ceiling |
| `IteratorAge` | Max | Per SLA | Stream processing lag |

### 8.2 ECS/Fargate Alerting

[FACT]
"The recommended alarms for Amazon ECS include alarms to detect high CPU reservation of the ECS cluster. High CPU reservation might indicate that the cluster is running out of registered CPUs for the task. To troubleshoot, you can add more capacity, scale the cluster, or set up auto scaling."
— AWS CloudWatch Recommended Alarms
URL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html

[FACT]
"An ECS CPU utilization alarm helps detect high CPU utilization of the service, as maxed-out CPU utilization might indicate a resource bottleneck or application performance problems."
— AWS CloudWatch Best Practice Alarms
URL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html

**Recommended ECS alarms:**

| Metric | Dimension | Suggested Threshold | Alarm Purpose |
|---|---|---|---|
| `CPUUtilization` | ServiceName | > 80% sustained | CPU saturation |
| `MemoryUtilization` | ServiceName | > 80% sustained | Memory pressure |
| `RunningTaskCount` | ServiceName | < desired count | Task health |
| `CPUReservation` | ClusterName | > 80% | Cluster capacity |

### 8.3 RDS Alerting

**Recommended RDS alarms:**

| Metric | Suggested Threshold | Alarm Purpose |
|---|---|---|
| `DatabaseConnections` | > 80% of `max_connections` | Connection pool exhaustion |
| `ReplicaLag` | > 30s (per SLA) | Replication health |
| `FreeStorageSpace` | < 20% | Storage capacity |
| `CPUUtilization` | > 80% sustained | CPU saturation |
| `ReadLatency` / `WriteLatency` | Per p99 SLA | Query performance |

### 8.4 SageMaker Endpoint Alerting

[FACT]
"You can create alarms for any metric that SageMaker tracks — error rates, response times, invocation counts, and more."
— SageMaker Monitoring Documentation
URL: https://docs.aws.amazon.com/sagemaker/latest/dg/inference-monitoring.html

[FACT]
"You can set alarms that watch for certain thresholds and send notifications when those thresholds are met. You can create simple static threshold metric alarms where you specify a threshold value for a metric, and if the metric breaches the threshold value, the alarm goes into the ALARM state."
— CodeSignal / SageMaker Learning
URL: https://codesignal.com/learn/courses/managing-ml-resources-in-sagemaker-console/lessons/monitoring-and-alerting-setup

**Recommended SageMaker endpoint alarms:**

| Metric | Suggested Threshold | Alarm Purpose |
|---|---|---|
| `Invocations5XXErrors` | > 0 sustained | Model error rate |
| `ModelLatency` | > p99 SLA (ms) | Inference latency SLO |
| `OverheadLatency` | > 500ms | Sidecar/routing overhead |
| `CPUUtilization` | > 80% | Instance saturation |
| `InvocationsPerInstance` | > throughput limit | Auto-scaling trigger |

### 8.5 SQS Queue Depth Alerting

[FACT]
"For Amazon SQS queues, you can alarm when the total number of visible messages exceeds a threshold using the ApproximateNumberOfMessageVisible metric with the Average statistic."
— AWS SQS Documentation
URL: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/set-cloudwatch-alarms-for-metrics.html

### 8.6 Composite Alarms for Service-Level SLOs

[FACT]
"A composite alarm includes a rule expression that takes into account the alarm states of other alarms you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met. The alarms specified in a composite alarm's rule expression can include metric alarms and other composite alarms, and using composite alarms can reduce alarm noise."
— AWS CloudWatch Documentation
URL: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html

**Example composite alarm pattern for an ECS-based API service SLO:**
```
COMPOSITE: (ECS_CPU_High OR ECS_Memory_High) AND (ALB_5xx_Rate_High OR ALB_Latency_P99_High)
→ SNS → PagerDuty / OpsGenie
```

Using composite alarms prevents false-positive pages for transient single-metric spikes and maps to a service-level availability or latency SLO rather than infrastructure-level thresholds.

---

## Section 9 — Production-Ready Service Onboarding Checklist

The following checklist applies when onboarding a new service in a production AWS environment. Adapt the applicable compute columns for each service type.

### Pre-Onboarding (Architecture Gate)

- [ ] Service compute type selected (Lambda / ECS-Fargate / App Runner / SageMaker)
- [ ] VPC, subnets (private), and security groups defined
- [ ] IAM execution role created with least-privilege policy
- [ ] ECR repository created (if containerized); lifecycle policy configured
- [ ] ECR enhanced scanning (Amazon Inspector) enabled
- [ ] Secrets Manager secrets created for all credentials; rotation schedule configured
- [ ] Parameter Store parameters created for non-secret configuration

### CI/CD Pipeline

- [ ] CodePipeline or GitHub Actions pipeline configured per service type (see Section 1)
- [ ] CodeBuild buildspec.yml produces tagged image with git SHA and environment
- [ ] ECR `InspectorScan` action gate added to pipeline; pipeline fails on Critical findings
- [ ] Deployment strategy configured (Lambda: alias traffic shift; ECS: blue/green bake; App Runner: auto-deploy; SageMaker: UpdateEndpoint + guardrails)
- [ ] Pipeline notification (EventBridge → SNS) configured for pipeline failures

### Health Checks

- [ ] Application exposes `/health` (liveness) and `/ready` (readiness) HTTP endpoints (ECS, App Runner)
- [ ] ALB target group health check path set to `/health` (ECS, Lambda)
- [ ] ECS task definition `healthCheck` command configured with `startPeriod` matching startup time
- [ ] App Runner health-check protocol set to HTTP with correct path
- [ ] Health check grace period (`healthCheckGracePeriodSeconds`) set in ECS service definition

### Service Discovery and Networking

- [ ] ECS Service Connect namespace configured (intra-cluster service-to-service)
- [ ] Cloud Map HTTP or DNS namespace created (cross-cluster or cross-service)
- [ ] App Mesh configuration removed / not used (deprecated September 2026)
- [ ] ALB listener rules created (path-based or host-based routing)
- [ ] API Gateway VPC Link configured if public API layer is required

### Observability

- [ ] ADOT Lambda Layer added (Lambda) OR ADOT sidecar container added to task definition (ECS/App Runner)
- [ ] X-Ray active tracing enabled on Lambda function; sampling rule configured
- [ ] CloudWatch Log Group created with 30-day retention policy (dev), 90-day (prod)
- [ ] EMF library (`aws-embedded-metrics`) integrated for custom business metrics
- [ ] CloudWatch Agent sidecar added to ECS task for EMF metric ingestion (non-Lambda)
- [ ] CloudWatch Container Insights enabled for ECS cluster

### Secrets and Configuration

- [ ] ECS task definition `secrets` stanza references Secrets Manager ARNs (not plaintext values)
- [ ] Lambda: Parameters and Secrets Extension Layer added; TTL configured
- [ ] App Runner environment variable secrets referencing Secrets Manager ARNs
- [ ] SageMaker execution role granted `secretsmanager:GetSecretValue` for required secrets
- [ ] RDS: Secrets Manager automatic rotation enabled (alternating-users for production)
- [ ] Client-side caching library implemented for container workloads that cannot restart on rotation

### Alerting and On-Call

- [ ] Per-service CloudWatch alarms created (see Section 8 tables)
- [ ] Composite alarm created combining infrastructure and application error alarms
- [ ] SNS topic created; PagerDuty or OpsGenie subscription attached
- [ ] Auto-rollback CloudWatch alarm ARN linked to CodeDeploy / ECS deployment (for automated rollback)
- [ ] SageMaker: Deployment guardrails alarm threshold configured for auto-rollback
- [ ] CloudWatch dashboard created with service-level view (not just infrastructure metrics)

### Security and Compliance

- [ ] VPC endpoint (PrivateLink) created for Secrets Manager, ECR, and S3 (prevent public egress)
- [ ] ECR image signed (optional, if container signing policy enforced)
- [ ] AWS Security Hub findings for ECR images reviewed and remediated before production promotion
- [ ] IAM Access Analyzer enabled; no public resource exposure
- [ ] CloudTrail logging enabled for Secrets Manager API calls

---

## Operational Difficulty Summary

| Capability Domain | On-Prem | Managed K8s (EKS) | Cloud-Native (Lambda / App Runner) |
|---|---|---|---|
| **CI/CD pipeline** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Jenkins + custom scripts | CodePipeline + kubectl | CodePipeline + native deploy |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Health checks** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1–2/5 |
| | Custom probes, LB config | K8s liveness/readiness | Managed (App Runner) or ALB rules |
| | Est. FTE: 0.1–0.25 | Est. FTE: 0.1 | Est. FTE: <0.1 |
| **Service discovery** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Consul / custom DNS | CoreDNS + K8s Services | ECS Service Connect / Cloud Map |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.1 |
| **Load balancer / ingress** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | HAProxy / Nginx | ALB Ingress Controller | ALB target groups / App Runner |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.1 |
| **Observability** | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-hosted stack | ADOT + CloudWatch | ADOT layer / native metrics |
| | Est. FTE: 0.5–1.0 | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 |
| **Image lifecycle (ECR)** | Difficulty: 4/5 | Difficulty: 2/5 | Difficulty: 2/5 |
| | Harbor / Quay + custom scan | ECR + Inspector | ECR + Inspector (same) |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1 | Est. FTE: 0.1 |
| **Secrets management** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Vault / custom rotation | Secrets Manager + K8s CSI | Secrets Manager native |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |
| **Alerting** | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Prometheus + Alertmanager | CloudWatch + Prometheus | CloudWatch composite alarms |
| | Est. FTE: 0.25–0.5 | Est. FTE: 0.1–0.25 | Est. FTE: 0.05–0.1 |

*FTE assumptions: mid-size ISV SaaS deployment, 10–50 active services, single AWS region. On-call burden not included — add 0.1–0.2 FTE per domain for production on-call coverage.*

---

## Key Takeaways

- **ECS-native blue/green (July 2025) and App Mesh deprecation (September 2026) are the two most consequential architectural shifts** ISVs must account for in greenfield designs; any architecture referencing App Mesh as a service mesh layer requires a migration plan to ECS Service Connect before mid-2026.
- **Per-service CI/CD pipelines are not interchangeable**: Lambda requires CodeDeploy alias traffic shifting, ECS requires blue/green or rolling update with a bake period, App Runner uses ECR-triggered atomic deployments, and SageMaker requires a two-stage MLOps pipeline (SageMaker Pipelines + CodePipeline); adopting a single pipeline template across all compute types will result in missing deployment safety controls.
- **Observability requires explicit per-service instrumentation choices**: native CloudWatch metrics are free but surface-level; X-Ray distributed tracing requires ADOT Lambda Layers (Lambda) or ADOT sidecar containers (ECS/App Runner); EMF custom metrics require client library integration and a CloudWatch Agent sidecar in ECS task definitions — none of these are on by default.
- **Secrets rotation at scale requires client-side caching**: ECS containers that reference Secrets Manager ARNs in task definitions do not receive automatic updates on rotation — a container restart is required unless the application integrates the Secrets Manager caching SDK; the Lambda Parameters and Secrets Extension handles this automatically for Lambda.
- **The production service onboarding checklist spans at least 6 AWS control planes** (CodePipeline, ECR, ALB, CloudWatch, Secrets Manager, Cloud Map / Service Connect) for a single ECS service; the operational gap between a working development deployment and a production-ready deployment is consistently underestimated by teams new to the AWS managed service model.

---

## Related — Out of Scope

- **Kubernetes-specific manifests and Helm charts for EKS** — covered in the EKS research track; not re-investigated here.
- **AWS WAF and Shield configuration** for public-facing ALB/API Gateway — referenced indirectly through ingress patterns but not researched in depth.
- **SageMaker Model Monitor and drift detection** — mentioned in the SageMaker endpoint pipeline context; detailed coverage belongs in an ML-specific research file.
- **Multi-region active-active deployment patterns** — referenced Route 53 health checks implicitly; full cross-region topology is out of scope for this file.
- **Cost modeling per-service type** — See [F03: Cost Economics] for deployment model cost comparisons.

---

## Sources

- [AWS CodeDeploy — Deployment Configurations](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html)
- [AWS SAM — Automating Updates to Serverless Apps](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html)
- [AWS DevOps Blog — ECS Blue/Green Native vs CodeDeploy in CDK](https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/)
- [AWS CodePipeline — ECS Standard Deployment Tutorial](https://docs.aws.amazon.com/codepipeline/latest/userguide/ecs-cd-pipeline.html)
- [AWS CodePipeline — Lambda Deployment Tutorial](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-lambda-deploy.html)
- [AWS Containers Blog — Spring Boot App Runner CI/CD Pipeline](https://aws.amazon.com/blogs/containers/build-and-deploy-a-spring-boot-application-to-aws-app-runner-with-a-ci-cd-pipeline-using-terraform/)
- [AWS Machine Learning Blog — SageMaker CI/CD Pipeline](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/)
- [AWS Machine Learning Blog — SageMaker CodePipeline + CodeDeploy Safe Deployment](https://aws.amazon.com/blogs/machine-learning/safely-deploying-and-monitoring-amazon-sagemaker-endpoints-with-aws-codepipeline-and-aws-codedeploy/)
- [AWS ELB — Target Group Health Checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)
- [AWS ECS — ALB Integration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb.html)
- [AWS re:Post — ECS vs ALB Health Checks](https://repost.aws/questions/QUdmR0oMn2Spa61RpKGWyPfg/ecs-should-i-use-alb-healthchecks-container-healthchecks-or-both)
- [AWS App Runner — Configuring Health Checks](https://docs.aws.amazon.com/apprunner/latest/dg/manage-configure-healthcheck.html)
- [AWS ELB — Lambda Functions as Targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html)
- [AWS ECS — Service Discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html)
- [OneUptime — AWS Cloud Map Service Discovery](https://oneuptime.com/blog/post/2026-02-12-aws-cloud-map-service-discovery/view)
- [OneUptime — ECS Service Discovery with Cloud Map](https://oneuptime.com/blog/post/2026-02-12-ecs-service-discovery-cloud-map/view)
- [AWS Containers Blog — Migrating App Mesh to ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/)
- [AWS App Mesh — What Is App Mesh (Deprecation Notice)](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html)
- [CloudKeeper — ECS Service Discovery vs Service Connect](https://www.cloudkeeper.com/insights/blog/amazon-ecs-service-communication-via-service-discovery-connect)
- [AWS Compute Blog — API Gateway Private Integrations (HTTP APIs)](https://aws.amazon.com/blogs/compute/configuring-private-integrations-with-amazon-api-gateway-http-apis/)
- [AWS Compute Blog — API Gateway Private ALB Integration](https://aws.amazon.com/blogs/compute/build-scalable-rest-apis-using-amazon-api-gateway-private-integration-with-application-load-balancer/)
- [InfoQ — AWS X-Ray Transitions to OpenTelemetry (November 2025)](https://www.infoq.com/news/2025/11/aws-opentelemetry/)
- [AWS ADOT — Lambda Getting Started](https://aws-otel.github.io/docs/getting-started/lambda/)
- [AWS ADOT — ECS Setup](https://aws-otel.github.io/docs/setup/ecs/)
- [GitHub — aws-samples/aws-xray-fargate](https://github.com/aws-samples/aws-xray-fargate)
- [AWS Containers Blog — ADOT + ECS Dynamic Service Discovery (March 2025)](https://aws.amazon.com/blogs/containers/metrics-and-traces-collection-from-amazon-ecs-using-aws-distro-for-opentelemetry-with-dynamic-service-discovery/)
- [AWS CloudWatch — Embedded Metric Format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html)
- [AWS CloudWatch — EMF Specification](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html)
- [AWS Observability Best Practices — EMF](https://aws-observability.github.io/observability-best-practices/guides/signal-collection/emf/)
- [AWS ECR — Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
- [AWS ECR — Enhanced Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-enhanced.html)
- [AWS News Blog — Inspector ECR Image to Running Container Mapping](https://aws.amazon.com/blogs/aws/amazon-inspector-enhances-container-security-by-mapping-amazon-ecr-images-to-running-containers/)
- [AWS What's New — CodePipeline ECRBuildAndPublish + InspectorScan Actions](https://aws.amazon.com/about-aws/whats-new/2024/11/aws-codepipeline-publishing-ecr-image-aws-inspectorscan-actions/)
- [Wiz Academy — AWS Container Scanning](https://www.wiz.io/academy/container-security/aws-container-scanning)
- [AWS ECS — Secrets Manager Secrets via Environment Variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-secrets-manager.html)
- [AWS Systems Manager — Parameters and Secrets Lambda Extension](https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html)
- [AWS SageMaker — IAM Roles](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html)
- [AWS Secrets Manager — SageMaker Integration](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating-sagemaker.html)
- [AWS Security Blog — RDS Credential Rotation with Secrets Manager](https://aws.amazon.com/blogs/security/rotate-amazon-rds-database-credentials-automatically-with-aws-secrets-manager/)
- [AWS Prescriptive Guidance — Rotate DB Credentials Without Restarting Containers](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/rotate-database-credentials-without-restarting-containers.html)
- [AWS Lambda — CloudWatch Metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html)
- [AWS for Engineers — Lambda Error Monitoring Best Practices](https://awsforengineers.com/blog/lambda-error-monitoring-best-practices/)
- [AWS CloudWatch — Recommended Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html)
- [AWS CloudWatch — Best Practice Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html)
- [AWS SageMaker — CloudWatch Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
- [AWS SageMaker — Monitor Endpoint Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-monitoring.html)
- [AWS SQS — CloudWatch Alarms](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/set-cloudwatch-alarms-for-metrics.html)
- [AWS CloudWatch — Using Alarms (Composite Alarms)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)
- [AWS App Runner — X-Ray Tracing](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-xray.html)
