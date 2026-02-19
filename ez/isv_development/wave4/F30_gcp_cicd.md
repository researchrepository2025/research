# F30 — GCP CI/CD Services
## Research File: Managed Build, Test, Deploy, and Artifact Management on Google Cloud Platform

---

## Executive Summary

Google Cloud Platform provides a fully integrated, serverless CI/CD suite spanning source, build, artifact storage, and continuous delivery — all managed at the infrastructure level, eliminating the need for organizations to operate their own build servers, package registries, or deployment orchestrators. Cloud Build executes on-demand build pipelines with no persistent infrastructure, Artifact Registry stores all artifact formats in a single managed service with integrated vulnerability scanning, and Cloud Deploy provides structured continuous delivery with approval gates, rollback, and canary support natively for GKE and Cloud Run targets. For ISVs evaluating deployment models, GCP's native CI/CD stack offers the tightest integration with Kubernetes (GKE) and serverless (Cloud Run) runtimes, with Binary Authorization providing supply-chain enforcement at deploy time. The deprecation of Cloud Source Repositories in mid-2024 signals Google's intent to partner with GitHub and GitLab for source hosting rather than compete, making Workload Identity Federation the recommended keyless authentication bridge between external source platforms and GCP build infrastructure.

---

## 1. Cloud Build: Managed CI/CD

### 1.1 Overview

[Cloud Build](https://cloud.google.com/build) is a fully managed, serverless CI/CD platform that executes build, test, and deploy pipelines on Google-managed infrastructure. Builds are defined as a series of steps executed in Docker containers, with each step configurable as any container image.

[FACT] Cloud Build is described as a platform that "automates your software build, test, and deploy processes" with no infrastructure for customers to set up, upgrade, or scale.
URL: https://cloud.google.com/build
Date: 2025

[FACT] Cloud Build supports Docker engine version 20.10.24 and allows customization "including increasing the size of the machine type or allocating more disk space."
URL: https://docs.cloud.google.com/build/docs/overview

**Operational Burden Eliminated:**

| Operational Task | On-Premises/Self-Hosted | Cloud Build |
|---|---|---|
| Build server provisioning | Manual VM or bare metal | None — fully managed |
| OS patching and upgrades | DevOps/SRE team | Google-managed |
| Scaling build queue | Manual horizontal scaling | Auto-scales to demand |
| Jenkins plugin maintenance | Ongoing team effort | N/A |
| Network security for build agents | Customer-managed | Google network perimeter |
| Availability and HA | Customer SLA design | Google SLA |

### 1.2 Build Triggers

[FACT] Cloud Build triggers support integration with Cloud Source Repositories, GitHub, GitHub Enterprise, GitLab, GitLab Enterprise Edition, Bitbucket Server, Bitbucket Data Center, and Bitbucket Cloud as source repositories.
URL: https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers

[FACT] Trigger event types supported: push to a branch, push new tag, and pull request events.
URL: https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers

[FACT] Triggers support branch and tag pattern filtering using RE2 regular expression syntax, included/ignored file path filtering with glob patterns including recursive wildcards (`**`), and the `[skip ci]` commit message directive to suppress build execution.
URL: https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers

[FACT] Build config file formats supported by triggers: YAML, JSON, Dockerfile, and buildpacks.
URL: https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers

### 1.3 Default Pool vs. Private Pools

[FACT] "Private pools are private, dedicated pools of workers that offer greater customization over the build environment, including the ability to access resources in a private network. Private pools, similar to default pools, are hosted and fully-managed by Cloud Build and scale up and down to zero, with no infrastructure to set up, upgrade, or scale."
URL: https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview

| Capability | Default Pool | Private Pool |
|---|---|---|
| Machine types available | 5 | 64 |
| Max concurrent builds | 30 | 100+ |
| VPC peering (private network access) | No | Yes |
| Public IP on workers | Yes (required) | Can be disabled |
| VPC Service Controls | Not supported | Supported |
| Static internal IP ranges | No | Yes |

[FACT] Private pools support 64 different machine types versus 5 in the default pool, enabling significantly more resource flexibility.
URL: https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview

[FACT] Private pools "can create a private VPC peering connection between your VPC network and the service producer network" to access resources in private networks.
URL: https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview

### 1.4 Custom Builders and Community Builders

[FACT] Cloud Build supports three categories of build steps: "build steps provided by Cloud Build," community-contributed steps, and custom build steps written by the user.
URL: https://docs.cloud.google.com/build/docs/overview

### 1.5 Pricing

[FACT] Cloud Build customers receive 2,500 build-minutes free per month, "not charged against your credits."
URL: https://cloud.google.com/build/pricing

[FACT] New Cloud Build pricing for e2 machine types takes effect November 1, 2025.
URL: https://cloud.google.com/build/pricing-update

[FACT] Build-minutes are not incurred for time a build is queued, only for active execution.
URL: https://cloud.google.com/build/pricing

**FTE Estimation (ISV Context):**

| Deployment Model | Operational FTE Burden (CI Infrastructure) | On-Call Burden |
|---|---|---|
| Self-hosted Jenkins (on-prem) | 0.5–1.0 FTE for maintenance, scaling, plugin mgmt | Medium-High |
| Cloud Build (managed) | ~0.1 FTE for pipeline authoring governance | Low |
| Savings | ~0.4–0.9 FTE | Significant reduction |

[FACT] Operational comparison: "Cloud Build requires less manual setup and configuration compared to Jenkins, which offers a highly configurable environment but requires more manual effort for setup and maintenance."
URL: https://knapsackpro.com/ci_comparisons/jenkins/vs/google-cloud-build

---

## 2. Artifact Registry: Managed Artifact and Container Registry

### 2.1 Overview

[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) is Google Cloud's managed, multi-format artifact storage service, replacing the deprecated Container Registry. It provides a single service for all artifact types with per-repository access controls and integrated vulnerability scanning.

### 2.2 Supported Formats

[FACT] Artifact Registry supports the following artifact formats:
- **Docker**: Container images and Helm charts packaged in OCI format
- **Maven**: Java packages built with Maven or Gradle
- **npm**: Node.js packages
- **Python**: Python package distribution
- **Go**: Go modules
- **Ruby**: Ruby gems
- **Apt**: Debian packages
- **Yum**: RPM packages for Red Hat-based systems
- **Kubeflow**: Pipeline templates for ML workflow reuse in Vertex AI
- **Generic**: Versioned, immutable artifacts without specific package format requirements

URL: https://docs.cloud.google.com/artifact-registry/docs/supported-formats

[FACT] The registry supports Docker V2 (Schema 1 & 2) and Open Container Initiative (OCI) Image Format Specifications, enabling multi-architecture and content-addressable images.
URL: https://docs.cloud.google.com/artifact-registry/docs/supported-formats

### 2.3 Vulnerability Scanning

[FACT] "Artifact Analysis scans new images when they're uploaded to Artifact Registry, extracting information about the packages in the container."
URL: https://docs.cloud.google.com/artifact-registry/docs/analysis

[FACT] Automatic scanning covers: OS packages (Debian/APT, RPM), application language packages (Java, Python, Node.js, Go, Ruby, Rust, .NET, PHP), and secrets (API keys and service account keys).
URL: https://docs.cloud.google.com/artifact-registry/docs/analysis

[FACT] "After the initial scan, Artifact Analysis continuously monitors the metadata for scanned images in Artifact Registry for new vulnerabilities, receiving new and updated vulnerability information from vulnerability sources multiple times each day."
URL: https://docs.cloud.google.com/artifact-registry/docs/analysis

[FACT] Layer-based scanning for Artifact Analysis is in Preview, "allowing you to view vulnerability metadata for a specific layer of your image digest in the Google Cloud Console and in the gCloud CLI."
URL: https://docs.cloud.google.com/artifact-registry/docs/analysis

[FACT] The software bill of materials (SBOM) feature in Artifact Analysis is now Generally Available (GA).
URL: https://docs.cloud.google.com/artifact-registry/docs/analysis

[FACT] "Starting on July 23, 2024, standard tier/container OS vulnerability scanning is deprecated and is scheduled for shutdown on July 31, 2025."
URL: https://docs.cloud.google.com/artifact-registry/docs/analysis

[FACT] Google Cloud expanded vulnerability detection for Artifact Registry using OSV (Open Source Vulnerabilities) database in December 2024.
URL: https://security.googleblog.com/2024/12/google-cloud-expands-vulnerability.html
Date: December 2024

### 2.4 Pricing

[FACT] Artifact Registry provides a free tier with 0.5 GB of storage that never expires and allows commercial use.
URL: https://www.freetiers.com/directory/google-artifact-registry

[FACT] On-Demand Scanning API price is $0.26 per scanned container image.
URL: https://cloud.google.com/artifact-analysis/pricing

[FACT] Data transfer pricing applies per GB delivered from Artifact Registry repositories, depending on repository location and destination.
URL: https://cloud.google.com/artifact-registry/pricing

**Operational Burden Eliminated vs. Self-Hosted Registry:**

| Task | Self-Hosted (Harbor, Nexus) | Artifact Registry |
|---|---|---|
| Registry infrastructure management | 0.2–0.3 FTE | None |
| Vulnerability scanner updates | Manual, customer-managed | Auto-updated by Google |
| HA/DR for registry | Customer-designed | Google-managed, regional |
| Access control integration | Custom LDAP/OIDC config | Native IAM |
| Multi-format support | Multiple tools required | Single service |

---

## 3. Cloud Deploy: Managed Continuous Delivery

### 3.1 Overview

[Cloud Deploy](https://cloud.google.com/deploy) is a fully managed continuous delivery service that orchestrates release progression across defined pipeline stages (e.g., dev → staging → production) for GKE, Cloud Run, and custom deployment targets.

[FACT] "Cloud Deploy makes continuous delivery to GKE and Cloud Run services and jobs easy and powerful. You can define releases and progress them through environments, such as test, stage, and production, with easy one-step promotion and rollback of releases via the web console, CLI, or API."
URL: https://cloud.google.com/deploy

### 3.2 Supported Target Types

[FACT] Cloud Deploy supports deployment to: GKE, GKE attached clusters (outside Google Cloud), Cloud Run, and Custom target types.
URL: https://docs.cloud.google.com/deploy/docs/create-pipeline-targets

[FACT] "Within a delivery pipeline, all targets must reference the same runtime type (all GKE, or all Cloud Run, for example)."
URL: https://docs.cloud.google.com/deploy/docs/create-pipeline-targets

### 3.3 Pipeline Configuration

[FACT] Delivery pipelines are defined via YAML configuration files, either as a single `clouddeploy.yaml` combining pipeline and target definitions, or as separate files where the pipeline references externally-defined targets.
URL: https://docs.cloud.google.com/deploy/docs/create-pipeline-targets

[FACT] Pipelines are deployed using: `gcloud deploy apply --file=PIPELINE_CONFIG --region=LOCATION`
URL: https://docs.cloud.google.com/deploy/docs/create-pipeline-targets

### 3.4 Approval Gates

[FACT] "Targets can be configured with a `requireApproval: true` setting that requires approval before a release can be promoted to the cluster. If approval is required, Cloud Deploy creates the `rollout`, but in a pending-release state until approval is given."
URL: https://docs.cloud.google.com/deploy/docs/create-pipeline-targets

[FACT] "Lockdown release progression via IAM, monitor release events with Cloud Logging, and achieve traceability with Cloud Audit Logs."
URL: https://cloud.google.com/deploy

### 3.5 Deployment Strategies

[FACT] Cloud Deploy supports canary deployment strategy for all target types, including custom targets. "For a fully custom canary, you provide all of the traffic-balancing configuration."
URL: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary

[FACT] "For multi-phase rollouts (canary deployments), Cloud Deploy provides environment variables for each phase. Specifically, for canary deployments, the CLOUD_DEPLOY_FEATURES variable value is CANARY, and your render action is invoked for each phase in the canary with the canary percentage provided in the CLOUD_DEPLOY_PERCENTAGE_DEPLOY environment variable."
URL: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary

[FACT] Cloud Deploy supports parallel deployments, "meaning the target you're progressively deploying to can comprise two or more child targets."
URL: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary

[FACT] Cloud Deploy supports canary deployments to Cloud Run via traffic splitting.
URL: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run

[FACT] Cloud Deploy canary deployments to GKE use Gateway API networking for traffic management.
URL: https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api

**Operational Burden Eliminated vs. Custom Deployment Scripts:**

| Capability | Custom Scripts / Helm + ArgoCD | Cloud Deploy |
|---|---|---|
| Promotion workflow UI | None (CLI-only) | Console, CLI, API |
| Audit trail | Custom logging required | Native Cloud Audit Logs |
| Approval gates | Custom webhook integration | Native `requireApproval` |
| Rollback | Manual re-deploy | One-step rollback |
| Canary traffic splitting | Custom Istio/Gateway config | Managed, declarative |

---

## 4. Cloud Source Repositories (Deprecated) and Migration Path

### 4.1 Deprecation Status

[FACT] "Effective June 17, 2024, Cloud Source Repositories isn't available to new customers, and if your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories."
URL: https://docs.cloud.google.com/source-repositories/docs/migration-guides

[FACT] "A shutdown date will be communicated at least one year before the shutdown occurs to provide time for you to successfully migrate to an alternative product."
URL: https://docs.cloud.google.com/source-repositories/docs/migration-guides

### 4.2 Secure Source Manager (Replacement)

[FACT] "Secure Source Manager is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud. It supports Git version control and integrates with Cloud Build, Cloud Deploy, and Artifact Registry."
URL: https://cloud.google.com/secure-source-manager/docs/overview

[FACT] Secure Source Manager features: built-in pull requests, issue tracking, HTTPS and SSH authentication, protected branch rules, and configurable branch protection for different sets of branches.
URL: https://cloud.google.com/secure-source-manager/docs/overview

### 4.3 GitHub and GitLab as Primary Integration Path

[UNVERIFIED] For most ISVs, GitHub or GitLab remain the de facto source repositories, with Cloud Build triggers providing the integration layer rather than Google-hosted source control.

---

## 5. GitHub and GitLab Integration: Workload Identity Federation

### 5.1 Integration Architecture

[FACT] Cloud Build triggers support native integration with GitHub (including GitHub Enterprise), GitLab (including GitLab Enterprise Edition), Bitbucket Cloud, and Bitbucket Server as external source repositories.
URL: https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers

[FACT] "Workload Identity Federation (WIF) is a way to authenticate non-GCP systems such as GitHub Actions and GitLab CI/CD with Google Cloud services without using long-lived service account keys, allowing external platforms to obtain short-lived tokens that Google Cloud verifies at runtime."
URL: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines

[FACT] "The Google Cloud integration uses Workload Identity Federation to grant GitLab workloads access to Google Cloud resources through OpenID Connect (OIDC) by using JSON Web Token (JWT) tokens."
URL: https://docs.gitlab.com/integration/google_cloud_iam/

[FACT] "Configuring GitLab to connect Google Cloud's Workload Identity Federation reduces the need for service accounts and lets the two platforms use short-lived credentials on-demand. This approach eliminates the maintenance and security burden associated with service account keys."
URL: https://medium.com/google-cloud/configure-gcp-workload-identity-federation-for-gitlab-c526e6eb0517

[FACT] Security constraint: "GitHub and GitLab SaaS use a single issuer URL across all organizations and some of the claims embedded in OIDC tokens might not be unique to your organization, so you must use an attribute condition that restricts access to tokens issued by your GitHub organization or GitLab group to help protect against spoofing threats."
URL: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines

### 5.2 Setup Options

[FACT] Workload Identity Federation can be configured "either use the GitLab UI for guided setup or use the Google Cloud CLI to set up the Workload Identity Federation manually."
URL: https://docs.gitlab.com/ci/cloud_services/google_cloud/

---

## 6. Skaffold: Local and CI/CD Development Workflow for Kubernetes

### 6.1 Overview

[FACT] "Skaffold is a command line tool that facilitates continuous development for container-based & Kubernetes applications and handles the workflow for building, pushing, and deploying your application."
URL: https://skaffold.dev/

[FACT] Skaffold "enables you to focus on iterating on your application locally while Skaffold continuously deploys to your local or remote Kubernetes cluster, local Docker environment or Cloud Run project."
URL: https://skaffold.dev/

### 6.2 Key Features

[FACT] Skaffold capabilities include: "policy-based image tagging and highly optimized, fast local workflows," resource port-forwarding and logging, file syncing, and automated build/push/test/deploy pipeline execution.
URL: https://skaffold.dev/docs/

[FACT] Skaffold "as of Mar 2025 supports debugging with Go, Java, Node.js, and Python."
URL: https://oneuptime.com/blog/post/2026-01-19-kubernetes-skaffold-development-workflow/view
Date: January 2026

[FACT] "Skaffold has a pluggable architecture to integrate with any build or deploy tool and is client-side only with no cluster-side component, so there is no overhead or maintenance burden."
URL: https://skaffold.dev/

### 6.3 CI/CD Integration

[FACT] "Use skaffold build, skaffold test and skaffold deploy as part of your CI/CD pipeline, or simply skaffold run end-to-end. Skaffold render outputs hydrated Kubernetes manifests that can be used in GitOps workflows."
URL: https://skaffold.dev/docs/workflows/ci-cd/

**Skaffold Workflow in ISV Context:**

| Phase | Command | Eliminates |
|---|---|---|
| Local dev loop | `skaffold dev` | Manual docker build + kubectl apply iteration |
| CI pipeline | `skaffold build` / `skaffold test` | Custom build script maintenance |
| CD pipeline | `skaffold deploy` | Per-environment kubectl apply scripts |
| GitOps render | `skaffold render` | Manual manifest hydration |

---

## 7. Terraform on GCP: Managed State and Deployment Automation

### 7.1 Terraform State on GCP

[FACT] "Terraform uses a state file to track resource deployments. Storing this state remotely allows collaboration and maintains consistency. Google Cloud Storage is used for managing Terraform state."
URL: https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code

[FACT] The GCS bucket name for Terraform state is typically passed dynamically using a Cloud Build substitution variable `_TF_STATE_BUCKET`. The `-reconfigure` flag ensures the backend configuration is always correctly picked up.
URL: https://harrissolangi.medium.com/automating-terraform-deployments-with-google-cloud-build-a-step-by-step-guide-9e8421a4d8fb

### 7.2 Cloud Build + Terraform GitOps Pipeline

[FACT] "The process starts when you push Terraform code to either the dev or prod branch. In this scenario, Cloud Build triggers and then applies Terraform manifests to achieve the state you want in the respective environment."
URL: https://harrissolangi.medium.com/automating-terraform-deployments-with-google-cloud-build-a-step-by-step-guide-9e8421a4d8fb

[FACT] "Terraform Plan generates an execution plan, showing exactly what infrastructure changes Terraform intends to make. The plan is saved to a file named tfplan, which provides a clear audit trail."
URL: https://harrissolangi.medium.com/automating-terraform-deployments-with-google-cloud-build-a-step-by-step-guide-9e8421a4d8fb

[FACT] Cloud Build supports provisioning Cloud Build resources with Terraform directly via the Google Terraform provider.
URL: https://cloud.google.com/build/docs/terraform

**Terraform Pipeline Pattern on GCP:**

```
Push to branch → Cloud Build Trigger fires
  → terraform init (GCS backend)
  → terraform plan (save to tfplan artifact)
  → [approval gate via manual step or Cloud Deploy]
  → terraform apply -auto-approve
  → Artifact stored in GCS
```

---

## 8. Binary Authorization: Container Image Signature Verification

### 8.1 Overview

[FACT] "Binary Authorization is a deploy-time security control that ensures only trusted container images are deployed on Google Kubernetes Engine (GKE) or Cloud Run."
URL: https://docs.cloud.google.com/binary-authorization/docs/overview

[FACT] Binary Authorization works across four container platforms: Google Kubernetes Engine (GKE), Cloud Run, Cloud Service Mesh, and Google Distributed Cloud.
URL: https://docs.cloud.google.com/binary-authorization/docs/overview

### 8.2 Policy Model

[FACT] Binary Authorization implements two operational modes:
- **Monitoring**: "configure continuous validation (CV) with check-based platform policies to periodically monitor that container images...conform to a policy"
- **Enforcement**: "enforce[s] that images...conform with a policy that you define," blocking non-compliant deployments

URL: https://docs.cloud.google.com/binary-authorization/docs/overview

[FACT] "Rules in a policy provide specific criteria that an image must satisfy before it can be deployed. Each rule can be configured with an evaluation mode and an enforcement mode."
URL: https://cloud.google.com/binary-authorization/docs/key-concepts

### 8.3 Attestation Workflow

[FACT] "An attestor is a Google Cloud resource that Binary Authorization uses to verify the attestation at image deploy time. Attestors contain the public key that corresponds to the private key used by a signer to sign the image digest and create the attestation."
URL: https://cloud.google.com/binary-authorization/docs/key-concepts

[FACT] Attestation workflow: (1) Signers produce attestations "containing the registry path and digest of the image...digitally signed using the signer's private cryptographic key"; (2) At deployment, Binary Authorization verifies attestations against configured policies.
URL: https://docs.cloud.google.com/binary-authorization/docs/overview

### 8.4 SLSA and Sigstore Integration

[FACT] "Cloud Build supports the generation of build provenance that meets Supply-chain Levels for Software Artifacts (SLSA) level 3 assurance based on the specifications for SLSA version 0.1 and 1.0."
URL: https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance

[FACT] Binary Authorization SLSA provenance check "ensures that images are built by a trusted builder using source code from its trusted repositories only. The SLSA check checks the SLSA-specified provenance of Pods' images. The images must have been built by a trusted builder. Cloud Build is the only trusted builder that the SLSA check supports."
URL: https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check

[FACT] "The Sigstore signature check verifies that images have been signed using Sigstore signatures. This check supports only images hosted in Artifact Registry. The check verifies the Sigstore-generated signatures of container images associated with Pods that run in GKE clusters where CV is enabled."
URL: https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check

[FACT] "Legacy continuous validation (legacy CV) with project-singleton policies is deprecated. As of April 15, 2024, you can no longer enable legacy CV with project-singleton policies on new projects, and support for existing projects will be removed on May 1, 2025."
URL: https://cloud.google.com/binary-authorization/docs/overview-cv

[FACT] Cloud Build produces "attestations and provenance that Binary Authorization can use for enforcement and monitoring."
URL: https://docs.cloud.google.com/binary-authorization/docs/overview

### 8.5 End-to-End Supply Chain Security

**Binary Authorization + Cloud Build + Artifact Registry Integration:**

| Step | Service | Action |
|---|---|---|
| 1. Build | Cloud Build | Compiles image, generates SLSA provenance |
| 2. Store | Artifact Registry | Image pushed, vulnerability scan triggered |
| 3. Attest | Cloud Build / Attestor | Attestation signed with private key |
| 4. Deploy | GKE / Cloud Run | Binary Authorization verifies attestation |
| 5. Enforce | Binary Authorization | Block or allow based on policy |

---

## 9. Comparative Operational Summary

### 9.1 CI/CD Stack Comparison by Deployment Model

| Capability | On-Premises | Managed Kubernetes (EKS/AKS/GKE) | Cloud-Native (GCP) |
|---|---|---|---|
| CI build infrastructure | Self-managed Jenkins/Tekton | Cloud Build (managed) or self-managed | Cloud Build (fully managed) |
| Artifact storage | Harbor, Nexus (self-managed) | Artifact Registry or self-managed | Artifact Registry (fully managed) |
| CD orchestration | ArgoCD (self-managed) | Cloud Deploy or ArgoCD | Cloud Deploy (fully managed) |
| Source hosting | Internal GitLab/Gitea | GitHub/GitLab (external) | GitHub/GitLab + WIF |
| Supply chain enforcement | Custom OPA/policy | Binary Authorization (optional) | Binary Authorization (native) |
| Terraform state | S3-compatible (self-managed) | GCS backend | GCS backend (managed) |
| Estimated CI/CD FTE | 1.0–2.0 FTE | 0.3–0.6 FTE | 0.1–0.2 FTE |

### 9.2 Difficulty and Operational Burden by Service

| Service | Difficulty (1-5) | Key Eliminated Burden | FTE Savings vs. Self-Hosted |
|---|---|---|---|
| Cloud Build (default pool) | 2 | Build server mgmt, scaling, patching | 0.4–0.9 FTE |
| Cloud Build (private pools) | 3 | Same + VPC network config simplified | 0.3–0.7 FTE |
| Artifact Registry | 1 | Registry hosting, scanner updates, HA | 0.2–0.3 FTE |
| Cloud Deploy | 2 | Deployment pipeline scripting, approval workflows | 0.2–0.4 FTE |
| Binary Authorization | 4 | Policy enforcement at deploy-time (replaces manual QA gates) | 0.1–0.2 FTE |
| Workload Identity Federation | 3 | Eliminates static service account key rotation | 0.05–0.1 FTE |
| Skaffold | 2 | Dev iteration loop scripting, manifest management | 0.1–0.2 FTE |
| Terraform + Cloud Build | 3 | IaC pipeline scripting, state backend management | 0.1–0.2 FTE |

---

## Sources

- [Cloud Build Overview — Google Cloud Documentation](https://docs.cloud.google.com/build/docs/overview)
- [Cloud Build Product Page — Google Cloud](https://cloud.google.com/build)
- [Cloud Build Pricing — Google Cloud](https://cloud.google.com/build/pricing)
- [Cloud Build Pricing Update — Google Cloud](https://cloud.google.com/build/pricing-update)
- [Cloud Build Private Pools Overview — Google Cloud Documentation](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview)
- [Create and Manage Build Triggers — Google Cloud Documentation](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers)
- [Cloud Build Private Pools for Private Networks — Google Cloud Blog](https://cloud.google.com/blog/products/devops-sre/cloud-build-private-pools-offers-cicd-for-private-networks)
- [Artifact Registry Documentation — Google Cloud](https://docs.cloud.google.com/artifact-registry/docs)
- [Artifact Registry Supported Formats — Google Cloud Documentation](https://docs.cloud.google.com/artifact-registry/docs/supported-formats)
- [Artifact Analysis and Vulnerability Scanning — Google Cloud Documentation](https://docs.cloud.google.com/artifact-registry/docs/analysis)
- [Artifact Registry Pricing — Google Cloud](https://cloud.google.com/artifact-registry/pricing)
- [Artifact Analysis Pricing — Google Cloud](https://cloud.google.com/artifact-analysis/pricing)
- [Google Cloud Expands Vulnerability Detection for Artifact Registry Using OSV — Google Security Blog](https://security.googleblog.com/2024/12/google-cloud-expands-vulnerability.html)
- [Cloud Deploy Product Page — Google Cloud](https://cloud.google.com/deploy)
- [Create Your Delivery Pipeline and Targets — Google Cloud Documentation](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets)
- [Canary Deployment Strategy — Cloud Deploy — Google Cloud Documentation](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary)
- [Canary Deployments to Cloud Run — Google Cloud Documentation](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run)
- [Canary Deployments to GKE with Gateway API — Google Cloud Documentation](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/gke/gateway-api)
- [Custom Targets — Cloud Deploy — Google Cloud](https://cloud.google.com/deploy/docs/custom-targets)
- [Cloud Source Repositories Migration Guides — Google Cloud Documentation](https://docs.cloud.google.com/source-repositories/docs/migration-guides)
- [Migrate to Secure Source Manager — Google Cloud Documentation](https://docs.cloud.google.com/source-repositories/docs/csr-ssm-migration-guide)
- [Secure Source Manager Overview — Google Cloud](https://cloud.google.com/secure-source-manager/docs/overview)
- [Workload Identity Federation with Deployment Pipelines — Google Cloud IAM Documentation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)
- [Google Cloud Workload Identity Federation and IAM Policies — GitLab Docs](https://docs.gitlab.com/integration/google_cloud_iam/)
- [Configure OpenID Connect with GCP Workload Identity Federation — GitLab CI/CD Docs](https://docs.gitlab.com/ci/cloud_services/google_cloud/)
- [Skaffold Documentation](https://skaffold.dev/docs/)
- [Skaffold CI/CD Workflows](https://skaffold.dev/docs/workflows/ci-cd/)
- [Skaffold GitHub Repository — GoogleContainerTools](https://github.com/GoogleContainerTools/skaffold)
- [Managing Infrastructure as Code with Terraform, Cloud Build, and GitOps — Google Cloud Documentation](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code)
- [Provision Cloud Build Resources with Terraform — Google Cloud](https://cloud.google.com/build/docs/terraform)
- [Automating Terraform Deployments with Google Cloud Build — Medium](https://harrissolangi.medium.com/automating-terraform-deployments-with-google-cloud-build-a-step-by-step-guide-9e8421a4d8fb)
- [Binary Authorization Overview — Google Cloud Documentation](https://docs.cloud.google.com/binary-authorization/docs/overview)
- [Binary Authorization Key Concepts — Google Cloud](https://cloud.google.com/binary-authorization/docs/key-concepts)
- [Continuous Validation Overview — Binary Authorization — Google Cloud](https://cloud.google.com/binary-authorization/docs/overview-cv)
- [Sigstore Signature Check — Binary Authorization — Google Cloud Documentation](https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check)
- [Generate and Validate Build Provenance — Cloud Build — Google Cloud Documentation](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance)
- [Jenkins vs Google Cloud Build CI Server Comparison — Knapsack Pro](https://knapsackpro.com/ci_comparisons/jenkins/vs/google-cloud-build)

---

## Key Takeaways

- **Cloud Build eliminates all build infrastructure operations**: private pools extend this to regulated/private-network scenarios with 64 machine types and VPC peering, while remaining fully managed — representing 0.4–0.9 FTE savings versus self-hosted Jenkins per engineering team.

- **Artifact Registry is the single managed registry for the full GCP CI/CD stack**: it stores Docker, Maven, npm, Python, Go, Helm, Apt, Yum, and Generic artifacts with continuous vulnerability scanning (updated multiple times daily), SBOM generation (now GA), and secrets detection — eliminating the operational burden of hosting Harbor or Nexus.

- **Cloud Deploy provides structured, auditable continuous delivery natively**: with approval gates, canary/progressive delivery, one-step rollback, and IAM-gated promotion across GKE and Cloud Run targets — replacing custom deployment scripts and reducing CD pipeline maintenance to near zero.

- **Binary Authorization + Cloud Build achieves SLSA Level 3 supply chain enforcement**: Cloud Build is the only GCP-trusted builder for the SLSA provenance check, meaning the entire build-attest-enforce loop is native GCP with no third-party tooling required; legacy CV policy enforcement ends May 1, 2025 requiring migration to check-based platform policies.

- **Cloud Source Repositories is effectively dead for new ISVs**: the June 2024 deprecation to new customers confirms GitHub and GitLab as the source control layer, with Workload Identity Federation as the recommended keyless authentication bridge — eliminating static service account key management and its associated security risk.
