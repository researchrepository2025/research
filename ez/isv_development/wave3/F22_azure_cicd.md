# F22: Azure CI/CD Services

**Research Question:** What managed CI/CD services does Azure provide for build, test, deploy, and artifact management, and what operational burden does each eliminate?

**Scope:** Azure CI/CD services only. No compute coverage (see F16). No other cloud providers.

---

## Executive Summary

Azure operates two parallel, Microsoft-owned CI/CD ecosystems — Azure DevOps Services and GitHub Actions — that together cover the full software delivery lifecycle from source control through deployment and infrastructure provisioning. Azure DevOps Services (Pipelines, Repos, Artifacts, Test Plans) is a mature SaaS platform with deep Azure integration and enterprise features including managed agent pools (Managed DevOps Pools, now GA), while GitHub Actions provides a developer-native workflow engine tightly coupled to open-source tooling and OIDC-based keyless authentication with Azure. Azure Container Registry (ACR) extends both ecosystems with managed image storage, geo-replication, and automated build tasks. For ISVs building AI-driven SaaS applications, the managed nature of both ecosystems eliminates server maintenance, patching, capacity planning, and secrets-rotation work — operational burdens that compound significantly at scale. Bicep and ARM Templates provide the IaC layer that ties deployment pipelines to repeatable, auditable infrastructure provisioning.

---

## 1. Azure DevOps Pipelines

### 1.1 Service Overview

[Azure Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines/) is a fully managed CI/CD service within the Azure DevOps suite. It supports YAML-based pipeline definitions stored in source control, enabling pipeline-as-code workflows.

[FACT]
"Microsoft-hosted agents run on Azure general purpose virtual machines Standard_DS2_v2."
— Microsoft Learn
URL: https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops
Date: Current documentation

[FACT]
"Each running job consumes a parallel job that runs on an agent. In Azure Pipelines, you can run parallel jobs on Microsoft-hosted infrastructure or your own (self-hosted) infrastructure."
— Microsoft Learn
URL: https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops
Date: Current documentation

### 1.2 Microsoft-Hosted Agents

Microsoft-hosted agents are ephemeral VMs provisioned fresh for each pipeline run and destroyed upon completion. The following operating system images are available as of 2025:

[FACT]
"In late 2025, Microsoft added new images like Ubuntu 24.04, Windows Server 2025, and macOS 15 'Sequoia' for use in pipelines. A preview of macOS on Apple Silicon agents is available."
— Dynamics Edge / Azure DevOps Updates September 2025
URL: https://www.dynamicsedge.com/azure-devops-updates-september-2025/
Date: September 2025

[FACT]
"The Windows Server 2025 image is generally available starting June 16, 2025, and starting from September 2, 2025, the 'windows-latest' label refers to Windows 2025 instead of windows-2022."
— Dynamics Edge / Azure DevOps Updates September 2025
URL: https://www.dynamicsedge.com/azure-devops-updates-september-2025/
Date: September 2025

**Operational burden eliminated by Microsoft-hosted agents:**
- No VM provisioning, patching, or lifecycle management
- No agent software updates (handled by Microsoft)
- No capacity planning or scaling decisions
- No disk cleanup between runs (fresh image per job)
- 10 GB of storage for source and build outputs per job

### 1.3 Self-Hosted Agents

Self-hosted agents run on infrastructure controlled by the organization. They are required when pipelines need access to private networks, licensed software installed locally, or custom hardware (e.g., GPU nodes).

[FACT]
"Self-hosted agents give you more control to install dependent software needed for your builds and deployments. Also, machine-level caches and configuration persist from run to run, which can boost speed."
— Microsoft Learn
URL: https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops
Date: Current documentation

**Operational burden added by self-hosted agents:**
- OS patching and security updates (customer responsibility)
- Agent software version management
- Capacity planning and scaling
- Network configuration and firewall rules

### 1.4 Managed DevOps Pools (MDP)

Managed DevOps Pools is a GA service that sits between Microsoft-hosted and self-hosted agents, providing customizable pools backed by Azure compute without manual infrastructure management.

[FACT]
"Managed DevOps Pools for Azure DevOps is now generally available, with this milestone marking a significant advancement in the mission to improve developer productivity in the CI/CD loop, reduce cloud bills for ES infrastructure, and reduce the toil associated with creating and maintaining custom CI/CD infrastructure."
— Azure DevOps Blog
URL: https://devblogs.microsoft.com/devops/managed-devops-pools-ga/
Date: 2025

[FACT]
"Managed DevOps Pools enables dev teams and platform engineering teams to quickly spin up custom DevOps pools that suit their workload's unique needs, combining the flexibility of Scale Set agents with the ease of maintenance of Microsoft Hosted agents."
— Azure DevOps Blog
URL: https://devblogs.microsoft.com/devops/managed-devops-pools/
Date: 2025

[FACT]
"Notable capabilities include: Creating a pool in any supported Azure region and with any SKU, including ARM64 and GPU; maintaining agent state for up to seven days for faster builds; and running long-running workflows up to two days long."
— Microsoft Learn / Managed DevOps Pools Overview
URL: https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/overview?view=azure-devops
Date: Current documentation

[FACT]
"Many of the Managed DevOps Pool enhancements discussed (like Spot VMs, containerized agents, and custom startup scripts) are slated to arrive in preview or GA in Jan–Feb 2026."
— Dynamics Edge / Azure DevOps Updates September 2025
URL: https://www.dynamicsedge.com/azure-devops-updates-september-2025/
Date: September 2025

### 1.5 Parallel Jobs Pricing

[STATISTIC]
"Extra Microsoft-hosted CI/CD parallel jobs cost $40 per job. Extra self-hosted CI/CD parallel jobs cost $15 per job with unlimited minutes."
— Azure DevOps Services Pricing
URL: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
Date: 2025

[STATISTIC]
"Each Azure DevOps organization gets one parallel job with 1,800 minutes (30 hours) of build time every month using Microsoft-hosted agents."
— Microsoft Learn: Configure and pay for parallel jobs
URL: https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops
Date: Current documentation

[FACT]
"Private projects get one free parallel job that can run for up to 60 minutes each time, until 1,800 minutes (30 hours) per month are used. Paid parallel jobs remove the monthly time limit and allow each job to run for up to 360 minutes (6 hours)."
— Microsoft Learn: Configure and pay for parallel jobs
URL: https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops
Date: Current documentation

### 1.6 Deployment Model Comparison: Pipelines

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| CI/CD Agents | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Self-managed agents on bare metal or VMs; full OS, network, and toolchain responsibility | Self-hosted agents in K8s pods; Helm charts or Karpenter for scaling | Microsoft-hosted or MDP; zero infrastructure management |
| | Jenkins, TeamCity, or Azure DevOps Server self-hosted | Azure DevOps self-hosted in AKS, or MDP with VNET injection | Azure Pipelines Microsoft-hosted or MDP |
| Est. FTE: 1.0-1.5 | Est. FTE: 0.5-0.75 | Est. FTE: 0.1-0.25 |

---

## 2. Azure DevOps Repos

### 2.1 Service Overview

[Azure Repos](https://azure.microsoft.com/en-us/products/devops/) provides managed Git hosting within Azure DevOps. It supports unlimited private repositories and integrates natively with Azure Pipelines for build triggers and branch-level gate enforcement.

[FACT]
"Pull requests (PRs) are a way to change, review, and merge code in a Git repository on Azure Repos, with teams using PRs to review code and give feedback on changes before merging the code into the main branch."
— Microsoft Learn: About pull requests and permissions
URL: https://learn.microsoft.com/en-us/azure/devops/repos/git/about-pull-requests?view=azure-devops
Date: Current documentation

### 2.2 Branch Policies

Branch policies are server-enforced rules applied at the repository level that gate merges into protected branches.

[FACT]
"Branch policies enforce code quality during the pull request process by establishing requirements that must be performed for every code change. You can set branch policies to require PRs for any changes on protected branches and reject any changes pushed directly to the branches."
— Microsoft Learn: Git branch policies and settings
URL: https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops
Date: Current documentation

Available branch policy types include:

- **Minimum reviewer count**: Require N approvals before merge is allowed
- **Build validation**: Pre-merge build execution against PR changes
- **Work item linking**: Enforce traceability by requiring linked work items
- **Status checks**: Third-party services post status via the PR Status API
- **Comment resolution**: Block merge until all PR comments are resolved

[FACT]
"To set branch policies, be a member of the Project Administrators security group or have repository-level Edit policies permissions."
— Microsoft Learn: Branch policies
URL: https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies-overview?view=azure-devops
Date: Current documentation

### 2.3 Azure Repos vs. GitHub (Strategic Context for ISVs)

Both Azure Repos and GitHub are Microsoft-owned. Key differentiation relevant to ISVs:

[FACT]
"As of 2025, there are no concrete plans to bring Copilot Autofix to Azure DevOps. GitHub has been architected as the home of the 'AI Brain' — hosting the server-side vector indexes, knowledge graphs, and agentic environments required for the AI to reason over the entire repository."
— Pluralsight / Azure DevOps vs GitHub
URL: https://www.pluralsight.com/resources/blog/cloud/azure-devops-vs-github-comparing-microsofts-devops-twins
Date: 2025

[FACT]
"Azure DevOps supports on-premises deployment through Azure DevOps Server, which is particularly valuable for organizations in regulated industries that require strict control over their data and infrastructure."
— Everhour / GitHub vs Azure DevOps
URL: https://everhour.com/blog/azure-devops-vs-github/
Date: 2025

**Operational burden eliminated by managed Git hosting (both platforms):**
- No Git server infrastructure to provision or patch
- No storage capacity planning for repository growth
- No backup or disaster recovery configuration
- No SSH key infrastructure management (handled by the platform)

---

## 3. Azure Container Registry (ACR)

### 3.1 Service Tiers

ACR offers three service tiers with distinct capability sets:

| Feature | Basic | Standard | Premium |
|---------|-------|----------|---------|
| Included Storage | 10 GB | 100 GB | 500 GB |
| Daily Price | ~$0.167/day | ~$0.667/day | ~$1.667/day |
| Webhooks | Limited | 10 | 500 |
| Geo-Replication | No | No | Yes |
| Private Link | No | No | Yes |
| Content Trust (Notary) | No | No | Yes |
| Zone Redundancy | No | No | Yes |

Sources: [Azure Container Registry SKU Features](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus), [ACR Pricing](https://azure.microsoft.com/en-us/pricing/details/container-registry/)

[FACT]
"Premium registries provide the highest amount of included storage and concurrent operations, enabling high-volume scenarios. In addition to higher image throughput, Premium adds features such as geo-replication for managing a single registry across multiple regions, private link with private endpoints to restrict access to the registry, as well as higher API concurrency and bandwidth throughput."
— Microsoft Learn: ACR SKU Features
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus
Date: Current documentation

### 3.2 Geo-Replication

[FACT]
"The geo-replication feature of Premium registries supports advanced replication and container image distribution across geographies. Geo-replication enables network-close access to images from regional deployments, while providing a single management experience."
— Microsoft Learn: Geo-replicate Azure Container Registry
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-geo-replication
Date: Current documentation

### 3.3 ACR Tasks (Automated Builds)

ACR Tasks provide serverless compute for container image build automation triggered by source code commits or base image changes.

[FACT]
"Azure Container Registry Tasks streamlines building, testing, pushing, and deploying images to Azure, and can be configured to automatically rebuild application images when base images are updated, or automate image builds when your team commits code to a Git repository."
— Azure Container Registry Introduction
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro
Date: Current documentation

[FACT]
"ACR Tasks dynamically discovers base image dependencies when it builds a container image and can detect when an application image's base image is updated. With one pre-configured build task, ACR Tasks can automatically rebuild every application image that references the base image."
— Microsoft Learn: Automate Container Builds with ACR Tasks
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-overview
Date: Current documentation

[FACT]
"When you create an ACR task with the az acr task create command, by default the task is enabled for trigger by a base image update (the base-image-trigger-enabled property is set to True)."
— Microsoft Learn: ACR Tasks Base Image Updates
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-base-images
Date: Current documentation

**Operational burden eliminated by ACR Tasks:**
- No self-managed build server for container image construction
- No manual polling logic for base image update detection
- No orchestration of multi-step build/test/push sequences

### 3.4 Content Trust and Notary Project

[FACT]
"Azure Container Registry will retire Docker Content Trust (DCT) on March 31, 2028. As an alternative, Microsoft offers signing and verification solutions based on Notary Project, with encouragement to transition from DCT to Notary Project as soon as possible."
— Azure Container Registry / Microsoft Learn
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-faq
Date: 2025

[FACT]
"Until May 31, 2026, Docker Content Trust can be enabled on new container registries or registries that haven't enabled it previously."
— Azure Container Registry / Microsoft Learn
URL: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-faq
Date: 2025

### 3.5 Deployment Model Comparison: ACR

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| Container Registry | Difficulty: 4/5 | Difficulty: 3/5 | Difficulty: 1/5 |
| | Self-hosted Harbor or Docker Registry; TLS, auth, storage, replication all manual | Harbor on AKS or hybrid ACR; network egress and auth wiring required | ACR Basic/Standard/Premium; fully managed, geo-replicated at Premium tier |
| | Harbor, Docker Registry v2 | Harbor on K8s, or ACR with private endpoint | Azure Container Registry |
| Est. FTE: 0.5-1.0 | Est. FTE: 0.25-0.5 | Est. FTE: 0.05-0.1 |

---

## 4. Azure Artifacts

### 4.1 Service Overview

[Azure Artifacts](https://azure.microsoft.com/en-us/products/devops/artifacts) provides managed package feed hosting within Azure DevOps. A single feed can host multiple package ecosystems simultaneously.

[FACT]
"A single feed can host multiple package types, including npm, NuGet, Maven, Python, Cargo, and Universal Packages."
— Microsoft Learn: What are Azure Artifacts feeds?
URL: https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/feeds?view=azure-devops
Date: Current documentation

### 4.2 Upstream Sources

[FACT]
"Azure Artifacts feeds support saving packages from public registries like nuget.org through upstream sources, ensuring continued access to your packages even if the public source becomes temporarily unavailable."
— Microsoft Learn / Azure Artifacts
URL: https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/feeds?view=azure-devops
Date: Current documentation

### 4.3 Feed Scoping and Access Control

Azure Artifacts feeds can be scoped at the organization level or project level, with role-based permissions (Reader, Contributor, Owner). Integration with Azure Active Directory (now Entra ID) enables identity-based access without per-package token management.

**Operational burden eliminated by Azure Artifacts:**
- No self-hosted package server infrastructure (e.g., Nexus, Artifactory)
- No TLS certificate management for package endpoints
- No storage capacity planning for package archives
- No purge/retention policy enforcement scripting
- No manual upstream proxy configuration

### 4.4 Pricing

[STATISTIC]
"The first 2 GiB of Artifacts storage is free. Additional storage is $2 per GiB per month."
— Azure DevOps Services Pricing
URL: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
Date: 2025

---

## 5. GitHub Actions (Microsoft-Owned)

### 5.1 Azure Integration

GitHub Actions is the workflow automation platform embedded in GitHub, now owned by Microsoft. It is the recommended CI/CD mechanism for teams using GitHub repositories and integrates natively with Azure services.

[FACT]
"OpenID Connect (OIDC) allows your GitHub Actions workflows to access resources in Azure, without needing to store the Azure credentials as long-lived GitHub secrets."
— Microsoft Learn: Authenticate to Azure from GitHub Actions
URL: https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect
Date: Current documentation

[FACT]
"To use Azure Login action with OIDC, you need to configure a federated identity credential on a Microsoft Entra application or a user-assigned managed identity. The job or workflow run requires a permissions setting with id-token: write to allow GitHub's OIDC provider to create a JSON Web Token for every run."
— GitHub Docs: Configuring OpenID Connect in Azure
URL: https://docs.github.com/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-azure
Date: Current documentation

**Security benefit of OIDC vs. stored secrets:**
- Eliminates long-lived service principal keys stored in GitHub Secrets
- Tokens are scoped per-run and expire after job completion
- No secrets rotation schedule required

### 5.2 Larger Runners and Azure Private Networking

GitHub's "larger runners" provide higher-CPU/memory GitHub-hosted compute with optional Azure VNET injection.

[FACT]
"2-64 vCPU Ubuntu and Windows runners are supported with Azure VNET."
— GitHub Docs: Larger runners reference
URL: https://docs.github.com/en/actions/reference/runners/larger-runners
Date: Current documentation

[FACT]
"Starting in November 2025, NICs created by the GitHub Actions service will no longer appear in your Azure subscriptions. Moving forward, NICs are now provisioned in a service subscription and assigned IP addresses from your subnet."
— GitHub Docs: About Azure private networking for GitHub-hosted runners
URL: https://docs.github.com/en/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise
Date: November 2025

[FACT]
"Azure private networking enables larger runners to privately connect to your network and resources through an Azure Virtual Network, without opening ports or enabling access to those resources from the public internet."
— GitHub Docs: Private networking with GitHub-hosted runners
URL: https://docs.github.com/en/actions/concepts/runners/private-networking
Date: Current documentation

[FACT]
"Private networking for GitHub-hosted runners does not support static IP addresses for larger runners. You must use dynamic IP addresses, which is the default configuration for larger runners."
— GitHub Docs
URL: https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization
Date: Current documentation

[FACT]
"Currently Linux x64 and Windows x64 images are officially supported with Azure Private Networking. Networking capabilities such as Azure private networking and assigning static IPs are not currently available for macOS larger runners."
— GitHub Docs
URL: https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization
Date: Current documentation

### 5.3 Deployment Model Comparison: GitHub Actions

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| GitHub Actions Runners | Difficulty: 3/5 | Difficulty: 2/5 | Difficulty: 1/5 |
| | Self-hosted runners on bare metal; manual registration, patching, secret injection | Self-hosted runners in K8s pods (actions-runner-controller); auto-scaling via HPA | GitHub-hosted standard or larger runners; zero infra; Azure VNET for private access |
| | actions-runner-controller, custom VM images | actions-runner-controller (ARC) | GitHub-hosted runners, GitHub larger runners |
| Est. FTE: 0.5-1.0 | Est. FTE: 0.25-0.5 | Est. FTE: 0.05-0.15 |

---

## 6. Azure Deployment Environments

### 6.1 Service Overview

[Azure Deployment Environments](https://azure.microsoft.com/en-us/products/deployment-environments) enables platform engineering teams to create curated infrastructure templates that developers can self-serve without requiring Azure expertise or elevated permissions.

[FACT]
"Azure Deployment Environments is a managed service that enables dev teams to quickly spin up app infrastructure with project-based templates to establish consistency and best practices while maximizing security, compliance, and cost-efficiency."
— Microsoft Learn: What Is Azure Deployment Environments?
URL: https://learn.microsoft.com/en-us/azure/deployment-environments/overview-what-is-azure-deployment-environments
Date: Current documentation

[FACT]
"Development teams can provision complex environments in minutes without waiting for their platform engineering team by choosing from a curated set of templates built specifically for their projects."
— Microsoft Learn: What Is Azure Deployment Environments?
URL: https://learn.microsoft.com/en-us/azure/deployment-environments/overview-what-is-azure-deployment-environments
Date: Current documentation

### 6.2 IaC Framework Support

[FACT]
"Azure Deployment Environments' extensibility model allows customers to leverage their preferred IaC framework, including Azure Resource Manager, Bicep, and popular frameworks such as Terraform, Pulumi, and more."
— Microsoft Learn: Azure Deployment Environments
URL: https://learn.microsoft.com/en-us/azure/deployment-environments/overview-what-is-azure-deployment-environments
Date: Current documentation

### 6.3 Pipeline Integration

[FACT]
"Environments can be automatically deployed as part of existing continuous integration and continuous delivery (CI/CD) pipelines or deployed on demand to test applications and sandbox environments."
— Microsoft Learn: Azure Deployment Environments
URL: https://learn.microsoft.com/en-us/azure/deployment-environments/overview-what-is-azure-deployment-environments
Date: Current documentation

### 6.4 Azure Developer CLI (azd) — 2025 Updates

[FACT]
"azd now supports layered provisioning to solve complex infrastructure dependency scenarios and 'chicken and egg' problems."
— Azure SDK Blog: Announcing the October 2025 Release: Azure Developer CLI (azd)
URL: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-october-2025/
Date: October 2025

[FACT]
"Azure Developer CLI (azd) November 2025 release: Container Apps (GA), Layered Provisioning (Beta), Extension Framework, and Aspire 13."
— Azure SDK Blog
URL: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-november-2025/
Date: November 2025

---

## 7. Azure DevOps Test Plans

### 7.1 Service Overview

[Azure Test Plans](https://azure.microsoft.com/en-us/products/devops/test-plans) is the manual and exploratory testing management component of Azure DevOps. It is distinct from automated testing, which executes through Azure Pipelines.

[FACT]
"Azure Test Plans is a feature for registration of manual test effort; test plans, test suites and test cases can be added, maintained, and executed, and you get reporting over preparation and results."
— Azure Test Plans product page / community documentation
URL: https://azure.microsoft.com/en-us/products/devops/test-plans
Date: 2025

[FACT]
"The rich testing tools include test planning, tracking, browser-based tests with annotations, and centralized reporting."
— Azure DevOps Services Pricing
URL: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
Date: 2025

### 7.2 Pricing

[STATISTIC]
"The 'Basic + Test Plans' license costs approximately $52 per user per month and unlocks the full suite of testing tools."
— Azure DevOps Services Pricing
URL: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
Date: 2025

[FACT]
"Azure Test Plans is primarily focused on manual testing capabilities rather than automated testing, with all of the automated testing taking place in Azure Pipelines."
— Apprecode / Azure DevOps Pricing Explained
URL: https://apprecode.com/blog/azure-devops-pricing-explained-what-you-pay-for-and-what-you-get
Date: 2025

**Operational burden eliminated by Azure Test Plans:**
- No test case management database to operate
- No manual tracking spreadsheets or shared documents
- Centralized reporting without custom BI tooling
- Browser-based test execution without local agent installation

---

## 8. Azure Resource Manager (ARM) and Bicep

### 8.1 Bicep Overview

Bicep is Microsoft's domain-specific language for Azure IaC, designed as a more readable alternative to raw ARM JSON templates. Bicep files are transpiled to ARM JSON at deploy time.

[FACT]
"Bicep is an infrastructure-as-code (IaC) programming language that uses declarative syntax to deploy Azure resources, and in a Bicep file, you define the infrastructure you want to deploy to Azure and then use that file throughout the development lifecycle to repeatedly deploy that infrastructure."
— Microsoft Learn: What is Bicep?
URL: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview
Date: Current documentation

[FACT]
"The Bicep CLI transpiles your .bicep file into a standard ARM Template JSON file, which is then submitted to the Azure Resource Manager (ARM) API to deploy the resource. Both Az CLI (2.20.0+) and the PowerShell Az module (v5.6.0+) have Bicep support built-in."
— Microsoft Learn: What is Bicep?
URL: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview
Date: Current documentation

### 8.2 Deployment Stacks

Deployment Stacks are a Bicep/ARM feature that provides lifecycle management for groups of Azure resources — enabling atomic updates and enforced cleanup of removed resources.

[FACT]
"Deployment Stacks are a logical grouping of Azure resources defined using Bicep or ARM. When you deploy a stack, Azure tracks which resources belong to that stack, you can update or delete resources as a group, governance rules can prevent accidental changes, and environments can be deployed consistently."
— Microsoft Learn: Create and deploy Azure deployment stacks in Bicep
URL: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks
Date: Current documentation

[FACT]
"Azure Deployment Stacks track the resources that should exist based on your templates and automatically clean up anything that's no longer defined. This is similar to Terraform's state management, but native to Azure and built into the platform so you don't have to manage a state file."
— Rios Engineer: Azure Deployment Stacks Zero to Hero
URL: https://rios.engineer/azure-deployment-stacks-zero-to-hero/
Date: 2025

[FACT]
"Azure Deployment Stacks do not currently support what-if operations although it is planned for the near future."
— Rios Engineer: Azure Deployment Stacks Zero to Hero
URL: https://rios.engineer/azure-deployment-stacks-zero-to-hero/
Date: 2025

### 8.3 Microsoft Graph Bicep Extension (2025)

[FACT]
"One of the most significant additions in 2025 was the Microsoft Graph Bicep extension, which brought Entra ID resources into the infrastructure as code world. This unified approach means you can deploy an entire application stack, including Azure resources, Entra ID identities, and RBAC assignments — in a single template."
— Insight Services APAC Blog: Merry Bicep-mas: Sleighing IaC in 2025
URL: https://blog.insight-services-apac.dev/2025/12/05/bicep-2025
Date: December 2025

### 8.4 Azure Verified Modules (AVM)

[FACT]
"The Bicep AVM starter module is composed of 19 separate Azure Verified Modules: 16 resource modules and 3 pattern modules. Each module is independently versioned, tested, and maintained."
— Microsoft Tech Community: Release of Bicep Azure Verified Modules for Platform Landing Zone
URL: https://techcommunity.microsoft.com/blog/azuretoolsblog/release-of-bicep-azure-verified-modules-for-platform-landing-zone/4487932
Date: 2025

### 8.5 Deployment Model Comparison: IaC

| Capability | On-Premises | Managed K8s | Cloud-Native |
|------------|-------------|-------------|--------------|
| IaC / Infra Deployment | Difficulty: 5/5 | Difficulty: 3/5 | Difficulty: 2/5 |
| | Full infra management; no ARM/Bicep benefit; Ansible/Terraform for bare metal | Bicep for Azure resources; Helm/Kustomize for K8s workloads; dual toolchain required | Bicep + Deployment Stacks; ARM-native state management; AVM modules for validated patterns |
| | Ansible, Terraform, custom scripts | Bicep + Helm; or Terraform | Bicep, ARM Templates, Azure Developer CLI (azd) |
| Est. FTE: 1.5-2.0 | Est. FTE: 0.75-1.0 | Est. FTE: 0.25-0.5 |

---

## 9. Consolidated Operational Burden Comparison

The table below summarizes the operational burden across all CI/CD capability domains for an ISV serving approximately 50 enterprise customers on a mid-size deployment.

| Capability Domain | On-Premises | Managed K8s | Cloud-Native |
|-------------------|-------------|-------------|--------------|
| CI/CD Agent Infrastructure | Difficulty: 4/5 / Est. FTE: 1.0-1.5 | Difficulty: 3/5 / Est. FTE: 0.5-0.75 | Difficulty: 2/5 / Est. FTE: 0.1-0.25 |
| Source Control / Git Hosting | Difficulty: 3/5 / Est. FTE: 0.5 | Difficulty: 2/5 / Est. FTE: 0.25 | Difficulty: 1/5 / Est. FTE: 0.05 |
| Container Registry | Difficulty: 4/5 / Est. FTE: 0.5-1.0 | Difficulty: 3/5 / Est. FTE: 0.25-0.5 | Difficulty: 1/5 / Est. FTE: 0.05-0.1 |
| Package / Artifact Management | Difficulty: 4/5 / Est. FTE: 0.5 | Difficulty: 3/5 / Est. FTE: 0.25 | Difficulty: 1/5 / Est. FTE: 0.05 |
| Secrets / Auth (CI/CD) | Difficulty: 4/5 / Est. FTE: 0.25 | Difficulty: 3/5 / Est. FTE: 0.1-0.25 | Difficulty: 2/5 / Est. FTE: 0.05 |
| IaC / Infrastructure Deployment | Difficulty: 5/5 / Est. FTE: 1.5-2.0 | Difficulty: 3/5 / Est. FTE: 0.75-1.0 | Difficulty: 2/5 / Est. FTE: 0.25-0.5 |
| Test Management | Difficulty: 3/5 / Est. FTE: 0.25 | Difficulty: 2/5 / Est. FTE: 0.1 | Difficulty: 1/5 / Est. FTE: 0.05 |
| **Total Estimated FTE** | **4.5-7.5 FTE** | **2.2-3.5 FTE** | **0.6-1.05 FTE** |

**FTE Framework Assumptions:** Mid-size ISV; 50 enterprise customers; 5-20 active developers; 10-30 pipeline runs per day; single-region primary with one DR region. On-call burden estimated at 20-30% of active FTE for on-premises; 5-10% for managed K8s; 1-3% for cloud-native.

---

## Related — Out of Scope

The following topics were encountered during research but are outside the scope of this file:

- **AKS compute integration with Managed DevOps Pools** — covered in F16 (Azure Compute)
- **Azure Monitor integration with pipeline observability** — covered in monitoring-scoped files
- **GitHub Advanced Security / Copilot Autofix** — security tooling outside CI/CD scope boundary
- **Terraform vs. Bicep architectural comparison** — multi-provider IaC comparison outside Azure-only scope
- **GitHub Enterprise Server (self-hosted GitHub)** — on-premises Git hosting outside managed services scope

---

## Key Takeaways

- **Azure provides two parallel, fully managed CI/CD ecosystems** — Azure DevOps Services (Pipelines, Repos, Artifacts, Test Plans) and GitHub Actions — both Microsoft-owned, both integrating natively with Azure, serving different developer personas. ISVs should select based on where their developers already live, not vendor.

- **Managed DevOps Pools (now GA) eliminates the primary pain point of self-hosted agents** — custom pool creation with any Azure SKU (including ARM64 and GPU), agent state persistence for up to seven days, and two-day long-running job support, without the operational overhead of VM Scale Set agent pools.

- **OIDC keyless authentication between GitHub Actions and Azure** eliminates long-lived service principal secrets entirely — replacing secrets rotation with ephemeral per-run JWT tokens scoped to specific Entra ID federated identity credentials.

- **ACR's base-image update automation (ACR Tasks)** removes manual tracking of upstream OS and framework patches — a compounding security risk in ISV SaaS environments where dozens of application images may share a common base layer.

- **The cloud-native path reduces CI/CD operational staffing by an estimated 6-7x compared to on-premises** (0.6-1.05 FTE vs. 4.5-7.5 FTE at mid-scale), with the majority of the savings coming from eliminating agent infrastructure management, container registry operations, and IaC toolchain complexity.

---

## Sources

| # | Source | URL |
|---|--------|-----|
| 1 | Azure Pipelines Product Page — Microsoft Azure | https://azure.microsoft.com/en-us/products/devops/pipelines/ |
| 2 | Microsoft-hosted agents for Azure Pipelines — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops |
| 3 | Azure Pipelines Agents — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops |
| 4 | Azure DevOps Updates September 2025 — Dynamics Edge | https://www.dynamicsedge.com/azure-devops-updates-september-2025/ |
| 5 | Announcing Public Preview of Managed DevOps Pools — Azure DevOps Blog | https://devblogs.microsoft.com/devops/managed-devops-pools/ |
| 6 | Announcing GA of Managed DevOps Pools — Azure DevOps Blog | https://devblogs.microsoft.com/devops/managed-devops-pools-ga/ |
| 7 | Managed DevOps Pools Overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/overview?view=azure-devops |
| 8 | Managed DevOps Pools Pricing — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/pricing?view=azure-devops |
| 9 | Configure and pay for parallel jobs — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs?view=azure-devops |
| 10 | Azure DevOps Services Pricing — Microsoft Azure | https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/ |
| 11 | Git branch policies and settings — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops |
| 12 | Branch policies overview — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies-overview?view=azure-devops |
| 13 | About pull requests and permissions — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/repos/git/about-pull-requests?view=azure-devops |
| 14 | Pull request workflow extensibility — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-request-status?view=azure-devops |
| 15 | Azure DevOps vs GitHub — Pluralsight | https://www.pluralsight.com/resources/blog/cloud/azure-devops-vs-github-comparing-microsofts-devops-twins |
| 16 | GitHub vs Azure DevOps — Everhour | https://everhour.com/blog/azure-devops-vs-github/ |
| 17 | Azure Container Registry — Microsoft Azure | https://azure.microsoft.com/en-us/products/container-registry |
| 18 | ACR SKU Features and Limits — Microsoft Learn | https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus |
| 19 | ACR Pricing — Microsoft Azure | https://azure.microsoft.com/en-us/pricing/details/container-registry/ |
| 20 | Geo-replicate Azure Container Registry — Microsoft Learn | https://learn.microsoft.com/en-us/azure/container-registry/container-registry-geo-replication |
| 21 | Automate Container Builds with ACR Tasks — Microsoft Learn | https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-overview |
| 22 | ACR Tasks Base Image Updates — Microsoft Learn | https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-base-images |
| 23 | Azure Container Registry FAQ — Microsoft Learn | https://learn.microsoft.com/en-us/azure/container-registry/container-registry-faq |
| 24 | What are Azure Artifacts feeds — Microsoft Learn | https://learn.microsoft.com/en-us/azure/devops/artifacts/concepts/feeds?view=azure-devops |
| 25 | Azure Artifacts Product Page — Microsoft Azure | https://azure.microsoft.com/en-us/products/devops/artifacts |
| 26 | Authenticate to Azure from GitHub Actions by OIDC — Microsoft Learn | https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect |
| 27 | Configuring OpenID Connect in Azure — GitHub Docs | https://docs.github.com/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-azure |
| 28 | Larger runners reference — GitHub Docs | https://docs.github.com/en/actions/reference/runners/larger-runners |
| 29 | About Azure private networking for GitHub-hosted runners — GitHub Docs | https://docs.github.com/en/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise |
| 30 | Private networking with GitHub-hosted runners — GitHub Docs | https://docs.github.com/en/actions/concepts/runners/private-networking |
| 31 | About Azure private networking (org level) — GitHub Docs | https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization |
| 32 | What Is Azure Deployment Environments — Microsoft Learn | https://learn.microsoft.com/en-us/azure/deployment-environments/overview-what-is-azure-deployment-environments |
| 33 | Azure Deployment Environments Product Page — Microsoft Azure | https://azure.microsoft.com/en-us/products/deployment-environments |
| 34 | Announcing October 2025 Release: Azure Developer CLI — Azure SDK Blog | https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-october-2025/ |
| 35 | Azure Developer CLI November 2025 — Azure SDK Blog | https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-november-2025/ |
| 36 | Azure Test Plans Product Page — Microsoft Azure | https://azure.microsoft.com/en-us/products/devops/test-plans |
| 37 | Azure DevOps Pricing Explained — Apprecode | https://apprecode.com/blog/azure-devops-pricing-explained-what-you-pay-for-and-what-you-get |
| 38 | What is Bicep — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview |
| 39 | Create and deploy Azure deployment stacks in Bicep — Microsoft Learn | https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deployment-stacks |
| 40 | Azure Deployment Stacks Zero to Hero — Rios Engineer | https://rios.engineer/azure-deployment-stacks-zero-to-hero/ |
| 41 | Merry Bicep-mas: Sleighing IaC in 2025 — Insight Services APAC | https://blog.insight-services-apac.dev/2025/12/05/bicep-2025 |
| 42 | Release of Bicep Azure Verified Modules for Platform Landing Zone — Microsoft Tech Community | https://techcommunity.microsoft.com/blog/azuretoolsblog/release-of-bicep-azure-verified-modules-for-platform-landing-zone/4487932 |
| 43 | Managing Multiple Deployment Stacks — Microsoft Tech Community | https://techcommunity.microsoft.com/blog/azureinfrastructureblog/managing-multiple-deployment-stacks-in-azure-bicep-patterns-and-best-practices/4471392 |
| 44 | Bicep Experimental Features Coming in 2026 — Insight Services APAC | https://blog.insight-services-apac.dev/2025/12/08/bicep-experimental |
| 45 | Hosting Git in GitHub and Azure Repos — Microsoft Learn | https://learn.microsoft.com/en-us/devops/develop/git/hosting-git-repos |
