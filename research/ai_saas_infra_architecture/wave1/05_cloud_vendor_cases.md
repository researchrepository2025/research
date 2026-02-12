# Cloud Vendor Case Studies: AI/ML SaaS Infrastructure Architectures

**Research Question:** Which AI SaaS companies are featured in AWS, Azure, and GCP case studies, and what architectures do those case studies describe?

**Date Collected:** 2026-02-12

**Methodology:** Systematic search of AWS Customer Success Stories, Azure Customer Stories, and Google Cloud Customer Stories filtered for AI/ML and SaaS companies. Focus on infrastructure services (EKS/AKS/GKE, Lambda/Fargate/Cloud Run, Bedrock/OpenAI Service/Vertex AI).

---

## BIAS WARNING

**Vendor case studies are marketing materials that systematically overrepresent:**
- Happy customers and successful deployments
- Customers using the vendor's flagship products
- Large, recognizable companies with significant cloud spend
- Recent migrations and modernization success stories

**They systematically underrepresent:**
- Failed deployments or customers who left
- Small startups with minimal cloud spend
- Companies using competing cloud providers
- Customers running legacy or non-flagship infrastructure

**These case studies DO NOT represent the average AI SaaS company.** They represent the vendor's best-case scenarios used for marketing purposes.

---

## Executive Summary

Systematic search of AWS, Azure, and GCP case studies identified 25+ AI/ML SaaS companies with documented infrastructure architectures. Managed Kubernetes (EKS/AKS/GKE) dominates among companies that disclosed specific infrastructure choices. Serverless options (Lambda, Fargate, Cloud Run) appear in fewer case studies despite vendor promotion. Notable pattern: most case studies focus on AI platform services (Bedrock, Azure OpenAI, Vertex AI) rather than underlying compute infrastructure, limiting architectural insights.

---

## Data Points

### AWS Case Studies

#### [CASE STUDY 1]
**Source:** AWS Solutions Case Studies - Flawless
**URL:** https://aws.amazon.com/solutions/case-studies/flawless-case-study/
**Date:** 2025
**Company:** Flawless
**Segment:** AI Entertainment (Video/Film)

[FACT]
"Amazon EKS Hybrid Nodes presented us with a cost-efficient scaling solution"
— James Morgan, Principal Platform Engineer at Flawless
URL: https://aws.amazon.com/solutions/case-studies/flawless-case-study/
Date: 2025

[STATISTIC]
5x improvement in rendering times
— Flawless case study
URL: https://aws.amazon.com/solutions/case-studies/flawless-case-study/
Date: 2025

[FACT]
"That support helped speed up the project. An issue that might have taken weeks of debugging could be solved in a few days"
— Will Ferguson, Director of Platform Engineering at Flawless
URL: https://aws.amazon.com/solutions/case-studies/flawless-case-study/
Date: 2025

**Architecture Category:** Managed Kubernetes (EKS with Hybrid Nodes)
**Services:** Amazon EKS, Amazon EKS Hybrid Nodes, third-party GPU resources
**Scale Indicators:** Serves major studios worldwide, operating across multiple regions
**Geography:** Not specified
**Relevance:** Demonstrates hybrid cloud/on-prem GPU architecture for AI workloads

---

#### [CASE STUDY 2]
**Source:** AWS Solutions Case Studies - Liquid Analytics
**URL:** https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
**Date:** 2025
**Company:** Liquid Analytics
**Segment:** AI Analytics SaaS

[QUOTE]
"We're excited to use AWS so that we can meet our goals of delivering performance, scalability, and quick time to market."
— Lyn Nguyen, CEO, Liquid Analytics
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

[QUOTE]
"Aurora for PostgreSQL just works, and the AWS team helped us optimize how we use it."
— Vish Canaran, Chief AI Officer, Liquid Analytics
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

[STATISTIC]
1,000 Kubernetes pods launched in 1.2 seconds
— Liquid Analytics case study
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

[STATISTIC]
90% reduced CPU waste
— Liquid Analytics case study
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

[STATISTIC]
63% savings on compute costs
— Liquid Analytics case study
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

[STATISTIC]
Processes 1+ million goals within 2-hour SLAs
— Liquid Analytics case study
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

**Architecture Category:** Managed Kubernetes (EKS)
**Services:** Amazon EKS, Amazon FSx for Lustre, Amazon EC2 (Spot Instances), Amazon Aurora PostgreSQL, Amazon Bedrock, Karpenter
**Scale Indicators:** 1M+ goals processed, customer example with 1,000 agents making 90,000 sales decisions monthly
**Geography:** Not specified
**Relevance:** High-performance containerized analytics using Kubernetes with auto-scaling

---

#### [CASE STUDY 3]
**Source:** AWS Solutions Case Studies - Instabase
**URL:** https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/
**Date:** 2025
**Company:** Instabase
**Segment:** GenAI Document Processing SaaS

[QUOTE]
"Whatever tools and architecture we can think of are already available from AWS"
— Shaunak Godbole, Director of Engineering, Instabase
URL: https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/
Date: 2025

[QUOTE]
"Amazon S3 has phenomenal reliability, which is important for Instabase because we are dependent on the usage of our file system"
— Shaunak Godbole, Director of Engineering, Instabase
URL: https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/
Date: 2025

[STATISTIC]
20% performance improvement via M6i Instance migration
— Instabase case study
URL: https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/
Date: 2025

[STATISTIC]
70% cost reduction on development using Spot Instances
— Instabase case study
URL: https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/
Date: 2025

[STATISTIC]
95% faster environment deployment versus on-premises
— Instabase case study
URL: https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/
Date: 2025

**Architecture Category:** Managed Kubernetes (EKS)
**Services:** Amazon EC2 (M6i Instances, Spot Instances), Amazon EKS, Amazon OpenSearch Service, Amazon S3
**Scale Indicators:** Serves multiple top 10 global banks, runs 30-40 development stacks
**Geography:** Not specified
**Relevance:** Enterprise GenAI SaaS using EKS for orchestration with EC2 compute

---

#### [CASE STUDY 4]
**Source:** Bion Consulting - Sonantic (AWS EKS)
**URL:** https://www.bionconsulting.com/case-studies/scaling-ai-driven-voice-technology-with-aws-and-eks
**Date:** 2025
**Company:** Sonantic (acquired by Spotify)
**Segment:** AI Voice Synthesis SaaS

[FACT]
Sonantic transitioned infrastructure to AWS Elastic Kubernetes Service (EKS) with GPU support for optimal AI-driven performance
— Bion Consulting case study
URL: https://www.bionconsulting.com/case-studies/scaling-ai-driven-voice-technology-with-aws-and-eks
Date: 2025

[STATISTIC]
100% compliance score in AWS Security Hub
— Sonantic case study
URL: https://www.bionconsulting.com/case-studies/scaling-ai-driven-voice-technology-with-aws-and-eks
Date: 2025

**Architecture Category:** Managed Kubernetes (EKS with GPU)
**Services:** Amazon EKS with GPU support, KEDA (Kubernetes Event-Driven Autoscaling), Prometheus, Grafana, AWS Security Hub, GuardDuty, CloudTrail, Terragrunt
**Scale Indicators:** Seed-stage startup, hyper-realistic AI voices for video games and leisure industry
**Geography:** Not specified
**Relevance:** GPU-accelerated Kubernetes for AI model inference

---

#### [CASE STUDY 5]
**Source:** AWS Solutions Case Studies - Bynder
**URL:** https://aws.amazon.com/solutions/case-studies/bynder-bedrock-case-study/
**Date:** 2025
**Company:** Bynder
**Segment:** Digital Asset Management SaaS

[STATISTIC]
75% reduction in search time
— Bynder case study
URL: https://aws.amazon.com/solutions/case-studies/bynder-bedrock-case-study/
Date: 2025

[STATISTIC]
Over 4,000 companies globally use Bynder to store, organize, and distribute over 175 million assets
— Bynder case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/bynder-bedrock-case-study/
Date: 2025

[DATA POINT]
18 PB of data managed
— Bynder case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/bynder-bedrock-case-study/
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Amazon Bedrock (Amazon Titan Multimodal Embeddings), Amazon S3 Intelligent-Tiering
**Scale Indicators:** 4,000+ customers, 175M+ assets, 18 PB data
**Geography:** Global
**Relevance:** AI platform service (Bedrock) for SaaS, infrastructure not detailed

---

#### [CASE STUDY 6]
**Source:** AWS Solutions Case Studies - Gong
**URL:** https://aws.amazon.com/solutions/case-studies/gong/
**Date:** 2025
**Company:** Gong
**Segment:** Revenue Intelligence AI SaaS

[FACT]
Gong utilizes AWS Bedrock and Claude to power proprietary LLMs and more than 15 AI agents
— AWS case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/gong/
Date: 2025

[STATISTIC]
More than 4,500 companies around the world rely on Gong
— AWS case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/gong/
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Amazon Bedrock, Claude
**Scale Indicators:** 4,500+ companies
**Geography:** Global
**Relevance:** AI platform service (Bedrock) for SaaS, infrastructure not detailed

---

#### [CASE STUDY 7]
**Source:** AWS Solutions Case Studies - DoorDash Bedrock
**URL:** https://aws.amazon.com/solutions/case-studies/doordash-bedrock-case-study/
**Date:** 2025
**Company:** DoorDash
**Segment:** Delivery Platform (AI Contact Center)

[STATISTIC]
50 percent reduction in generative AI application development time
— DoorDash case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/doordash-bedrock-case-study/
Date: 2025

[FACT]
Fully voice-operated self-service generative AI contact center solution ready for live testing in only 2 months
— DoorDash case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/doordash-bedrock-case-study/
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Amazon Bedrock, Amazon Connect, Anthropic Claude
**Scale Indicators:** Not specified
**Geography:** Not specified
**Relevance:** AI platform service (Bedrock) for contact center, infrastructure not detailed

---

#### [CASE STUDY 8]
**Source:** AWS Solutions Case Studies - WRITER
**URL:** https://aws.amazon.com/solutions/case-studies/writer-case-study/
**Date:** 2025
**Company:** WRITER
**Segment:** GenAI Content Platform SaaS

[STATISTIC]
3x accelerated model iteration cycles
— WRITER case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/writer-case-study/
Date: 2025

[STATISTIC]
90% reduction in training pipeline failures
— WRITER case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/writer-case-study/
Date: 2025

[STATISTIC]
0 manual intervention in workload distribution
— WRITER case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/writer-case-study/
Date: 2025

**Architecture Category:** Managed ML Infrastructure
**Services:** Amazon SageMaker HyperPod
**Scale Indicators:** Not specified
**Geography:** Not specified
**Relevance:** Managed ML training infrastructure for GenAI model development

---

#### [CASE STUDY 9]
**Source:** AWS Solutions Case Studies - Workday
**URL:** https://aws.amazon.com/solutions/case-studies/workday-case-study/
**Date:** 2025
**Company:** Workday
**Segment:** Enterprise SaaS (HCM/Finance)

[FACT]
Workday scaled from handling a thousand inference requests to tens of millions that are coming in daily
— AWS case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/workday-case-study/
Date: 2025

**Architecture Category:** Managed ML Infrastructure
**Services:** Amazon SageMaker
**Scale Indicators:** Tens of millions of daily inference requests
**Geography:** Not specified
**Relevance:** Massive scale AI inference using SageMaker

---

#### [CASE STUDY 10]
**Source:** AWS Solutions Case Studies - Autodesk ECS
**URL:** https://aws.amazon.com/solutions/case-studies/autodesk-serverless-case-study/
**Date:** 2025
**Company:** Autodesk
**Segment:** Design Software SaaS

[STATISTIC]
50% improvement in startup performance
— Autodesk case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/autodesk-serverless-case-study/
Date: 2025

**Architecture Category:** Cloud-Native Non-K8s (ECS with Fargate)
**Services:** Amazon ECS with AWS Fargate
**Scale Indicators:** High-scale simulations, enterprise SaaS
**Geography:** Not specified
**Relevance:** Serverless container orchestration (ECS/Fargate) for SaaS

---

#### [CASE STUDY 11]
**Source:** AWS Solutions Case Studies - BILL
**URL:** https://aws.amazon.com/solutions/case-studies/bill-ecs-case-study/
**Date:** 2025
**Company:** BILL
**Segment:** Financial Operations SaaS

[STATISTIC]
150,000–200,000 requests per minute
— BILL case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/bill-ecs-case-study/
Date: 2025

**Architecture Category:** Cloud-Native Non-K8s (ECS with Fargate)
**Services:** Amazon ECS with AWS Fargate
**Scale Indicators:** 150-200K requests/minute
**Geography:** Not specified
**Relevance:** High-scale serverless container orchestration for financial SaaS

---

#### [CASE STUDY 12]
**Source:** AWS Solutions Case Studies - Smartsheet
**URL:** https://aws.amazon.com/solutions/case-studies/smartsheet-ecs-fargate-case-study/
**Date:** 2025
**Company:** Smartsheet
**Segment:** Work Management SaaS

[FACT]
Smartsheet reduced engineering time to deploy from hours to minutes
— AWS case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/smartsheet-ecs-fargate-case-study/
Date: 2025

**Architecture Category:** Cloud-Native Non-K8s (ECS with Fargate)
**Services:** Amazon ECS with AWS Fargate
**Scale Indicators:** Not specified
**Geography:** Not specified
**Relevance:** Serverless container orchestration for collaboration SaaS

---

#### [CASE STUDY 13]
**Source:** AWS Solutions Case Studies - Perplexity
**URL:** https://aws.amazon.com/solutions/case-studies/perplexity-bedrock-case-study/
**Date:** 2025
**Company:** Perplexity AI
**Segment:** AI Search SaaS

[FACT]
Perplexity became an early beta tester of Amazon SageMaker HyperPod in August 2023
— AWS case study (search result)
URL: https://aws.amazon.com/solutions/case-studies/perplexity-bedrock-case-study/
Date: 2025

**Architecture Category:** Managed ML Infrastructure
**Services:** Amazon Bedrock, Amazon SageMaker HyperPod, Amazon EC2 P4de Instances
**Scale Indicators:** Early beta tester, scalable AI training infrastructure
**Geography:** Not specified
**Relevance:** Large-scale AI model training and inference infrastructure

---

#### [CASE STUDY 14]
**Source:** Successive Digital - SaaS on AWS Fargate
**URL:** https://successive.tech/case-studies/saas-solution-deployed-on-aws-fargate/
**Date:** 2025
**Company:** Not named
**Segment:** SaaS (unnamed)

[FACT]
SaaS-based application deployed leveraging AWS Fargate, enabling seamless performance monitoring and enhanced collaboration
— Successive Digital case study (search result)
URL: https://successive.tech/case-studies/saas-solution-deployed-on-aws-fargate/
Date: 2025

**Architecture Category:** Cloud-Native Non-K8s (Fargate)
**Services:** AWS Fargate, Python FastAPI, Celery
**Scale Indicators:** Not specified
**Geography:** Not specified
**Relevance:** Serverless container platform for SaaS

---

#### [CASE STUDY 15]
**Source:** AWS Partner Success - Palo Alto Networks, Anthropic, Sourcegraph
**URL:** https://aws.amazon.com/partners/success/palo-alto-networks-anthropic-sourcegraph/
**Date:** 2025
**Company:** Palo Alto Networks
**Segment:** Cybersecurity (AI Dev Tools)

[STATISTIC]
Within three months onboarded 2,000 developers and increased productivity up to 40 percent, with an average of 25 percent
— AWS Partner Success case study (search result)
URL: https://aws.amazon.com/partners/success/palo-alto-networks-anthropic-sourcegraph/
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Amazon Bedrock (Claude 3.5 Sonnet, Claude 3 Haiku), Sourcegraph Cody
**Scale Indicators:** 2,000 developers
**Geography:** Not specified
**Relevance:** Enterprise adoption of AI platform services

---

### Azure Case Studies

#### [CASE STUDY 16]
**Source:** Microsoft Learn - Duck Creek Technologies
**URL:** https://learn.microsoft.com/en-us/azure/aks/windows-aks-customer-stories
**Date:** 2025
**Company:** Duck Creek Technologies
**Segment:** Insurance SaaS

[FACT]
Duck Creek Technologies modernized its insurance software solutions by adopting Windows containers on Azure Kubernetes Service (AKS), significantly enhancing operational efficiency and reducing time to market for new features
— Microsoft Learn (search result)
URL: https://learn.microsoft.com/en-us/azure/aks/windows-aks-customer-stories
Date: 2025

**Architecture Category:** Managed Kubernetes (AKS with Windows Containers)
**Services:** Azure Kubernetes Service (AKS), Windows containers
**Scale Indicators:** Property, Casualty, and General Insurance providers
**Geography:** Not specified
**Relevance:** Windows containerization on managed Kubernetes for enterprise SaaS

---

#### [CASE STUDY 17]
**Source:** Microsoft Customer Stories - PTC
**URL:** https://www.microsoft.com/en/customers/story/22856-ptc-azure-database-for-postgresql
**Date:** 2025
**Company:** PTC
**Segment:** PLM/IoT SaaS

[FACT]
PTC moved from a virtual machine–based infrastructure to Azure Kubernetes Service (AKS), facilitating the process of delivering SaaS services
— Microsoft Customer Stories (search result)
URL: https://www.microsoft.com/en/customers/story/22856-ptc-azure-database-for-postgresql
Date: 2025

[FACT]
PTC migrated data for more than 300 customers to Azure Database for PostgreSQL
— Microsoft Customer Stories (search result)
URL: https://www.microsoft.com/en/customers/story/22856-ptc-azure-database-for-postgresql
Date: 2025

**Architecture Category:** Managed Kubernetes (AKS)
**Services:** Azure Kubernetes Service (AKS), Azure Database for PostgreSQL, Linux VMs
**Scale Indicators:** 300+ customers migrated
**Geography:** Not specified
**Relevance:** Enterprise SaaS migration to managed Kubernetes with managed database

---

#### [CASE STUDY 18]
**Source:** Microsoft Azure Blog - Coca-Cola
**URL:** https://azure.microsoft.com/en-us/blog/from-idea-to-impact-real-world-success-stories-of-building-intelligent-apps-with-azure/
**Date:** 2025
**Company:** The Coca-Cola Company
**Segment:** Consumer Goods (AI Campaign Platform)

[STATISTIC]
Over 1 million consumers engaged in just 60 days with sub-millisecond performance
— Microsoft Azure Blog (search result)
URL: https://azure.microsoft.com/en-us/blog/from-idea-to-impact-real-world-success-stories-of-building-intelligent-apps-with-azure/
Date: 2025

[FACT]
Coca-Cola launched an immersive, AI-powered holiday campaign across 43 markets using Azure Container Apps and Azure AI Foundry
— Microsoft Azure Blog (search result)
URL: https://azure.microsoft.com/en-us/blog/from-idea-to-impact-real-world-success-stories-of-building-intelligent-apps-with-azure/
Date: 2025

**Architecture Category:** Cloud-Native Non-K8s (Azure Container Apps)
**Services:** Azure Container Apps, Azure AI Foundry
**Scale Indicators:** 1M+ consumers, 43 markets, sub-millisecond performance
**Geography:** Global (43 markets)
**Relevance:** Serverless container platform for AI-powered campaigns

---

#### [CASE STUDY 19]
**Source:** Microsoft Azure Blog - Air India
**URL:** https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/
**Date:** 2025
**Company:** Air India
**Segment:** Aviation (AI Customer Service)

[STATISTIC]
97% of queries with full automation
— Microsoft Azure Blog (search result)
URL: https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/
Date: 2025

[FACT]
Air India updated its virtual assistant's core natural language processing engine to the latest GPT models using Azure OpenAI services, saving millions of dollars on customer support costs
— Microsoft Azure Blog (search result)
URL: https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Azure OpenAI Service (GPT models)
**Scale Indicators:** 97% automation, millions in cost savings
**Geography:** India
**Relevance:** AI platform service (Azure OpenAI) for enterprise automation

---

#### [CASE STUDY 20]
**Source:** Microsoft Azure Blog - Medigold Health
**URL:** https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/
**Date:** 2025
**Company:** Medigold Health
**Segment:** Healthcare SaaS

[STATISTIC]
58% rise in clinician retention
— Microsoft Azure Blog (search result)
URL: https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/
Date: 2025

[FACT]
Medigold Health migrated applications to Azure OpenAI Service to achieve automation of clinician processes including report generation
— Microsoft Azure Blog (search result)
URL: https://azure.microsoft.com/en-us/blog/scaling-generative-ai-in-the-cloud-enterprise-use-cases-for-driving-secure-innovation/
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Azure OpenAI Service
**Scale Indicators:** UK occupational health provider
**Geography:** United Kingdom
**Relevance:** AI platform service for healthcare automation

---

### Google Cloud Case Studies

#### [CASE STUDY 21]
**Source:** Google Cloud Blog - Picterra
**URL:** https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
**Date:** 2025
**Company:** Picterra
**Segment:** Geospatial AI SaaS

[FACT]
Picterra adopted Google Kubernetes Engine to power its platform, providing the ability to quickly scale to meet the demands of geospatial AI workloads
— Google Cloud Blog (search result)
URL: https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
Date: 2025

[FACT]
With GKE, Picterra can model the terrain of entire countries quickly, even at ultra-high resolutions
— Google Cloud Blog (search result)
URL: https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
Date: 2025

**Architecture Category:** Managed Kubernetes (GKE)
**Services:** Google Kubernetes Engine (GKE)
**Scale Indicators:** Entire countries at ultra-high resolution
**Geography:** Not specified
**Relevance:** High-scale geospatial AI on managed Kubernetes

---

#### [CASE STUDY 22]
**Source:** Google Cloud Customer Stories - Stacks
**URL:** https://cloud.google.com/customers/stacks
**Date:** 2025
**Company:** Stacks
**Segment:** Accounting Automation SaaS

[FACT]
Stacks uses Google Kubernetes Engine Autopilot (GKE Autopilot), Cloud SQL, Cloud Spanner, Security Command Center (SCC), Vertex AI, and Gemini models
— Google Cloud (search result)
URL: https://cloud.google.com/customers/stacks
Date: 2025

[FACT]
In 2025, the company raised €10 million to support its growth
— Google Cloud (search result)
URL: https://cloud.google.com/customers/stacks
Date: 2025

**Architecture Category:** Managed Kubernetes (GKE Autopilot)
**Services:** GKE Autopilot, Cloud SQL, Cloud Spanner, Vertex AI, Gemini
**Scale Indicators:** €10M funding (2025), founded 2024
**Geography:** Amsterdam, Netherlands
**Relevance:** Startup using fully managed Kubernetes with AI services

---

#### [CASE STUDY 23]
**Source:** Google Cloud Press Center - Midjourney
**URL:** https://www.googlecloudpresscorner.com/2023-03-14-Midjourney-Selects-Google-Cloud-to-Power-AI-Generated-Creative-Platform
**Date:** 2023-03-14
**Company:** Midjourney
**Segment:** Generative AI (Text-to-Image) SaaS

[FACT]
Midjourney selected Google Cloud as its infrastructure provider of choice to benefit from the company's deep expertise in training large-scale AI models, scalability, and sustainability
— Google Cloud Press Center
URL: https://www.googlecloudpresscorner.com/2023-03-14-Midjourney-Selects-Google-Cloud-to-Power-AI-Generated-Creative-Platform
Date: 2023-03-14

[FACT]
Midjourney has employed Google Cloud's custom-developed AI accelerators, Tensor Processor Units (TPUs), to train its fourth generation AI model
— Google Cloud Press Center (search result)
URL: https://www.googlecloudpresscorner.com/2023-03-14-Midjourney-Selects-Google-Cloud-to-Power-AI-Generated-Creative-Platform
Date: 2023-03-14

[FACT]
In combination with Google Cloud's GPU VMs, which run on NVIDIA GPUs, Midjourney can render the generated images on the platform with breathtaking speed
— Google Cloud Press Center (search result)
URL: https://www.googlecloudpresscorner.com/2023-03-14-Midjourney-Selects-Google-Cloud-to-Power-AI-Generated-Creative-Platform
Date: 2023-03-14

[FACT]
The latest generation of TPUs operate at 90% carbon-free energy in one of the most efficient data centers in the world
— Google Cloud Press Center (search result)
URL: https://www.googlecloudpresscorner.com/2023-03-14-Midjourney-Selects-Google-Cloud-to-Power-AI-Generated-Creative-Platform
Date: 2023-03-14

**Architecture Category:** Not disclosed (likely custom with TPU/GPU)
**Services:** Google Cloud TPUs (Tensor Processing Units), GPU VMs (NVIDIA)
**Scale Indicators:** Major generative AI platform
**Geography:** Not specified
**Relevance:** Large-scale AI model training on specialized Google hardware (TPUs)

---

#### [CASE STUDY 24]
**Source:** Google Cloud Blog - Juganu
**URL:** https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
**Date:** 2025
**Company:** Juganu
**Segment:** Smart Cities/Retail SaaS

[FACT]
Juganu, a SaaS provider for smart cities and smart stores, is working with Google Cloud to develop digital twins
— Google Cloud Blog (search result)
URL: https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Google Cloud (services not specified)
**Scale Indicators:** Smart cities and stores
**Geography:** Not specified
**Relevance:** IoT/AI SaaS platform, infrastructure details not provided

---

#### [CASE STUDY 25]
**Source:** Google Cloud Blog - Vertex AI Customers
**URL:** https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
**Date:** 2025
**Company:** Multiple (Uber Eats, Ipsos, Jasper, Shutterstock, Quora)
**Segment:** Various AI SaaS

[STATISTIC]
Over 4 million developers are now building with Gemini models on Vertex AI
— Google Cloud Blog (search result)
URL: https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
Date: 2025

[STATISTIC]
20× increase in Vertex AI usage over the past year
— Google Cloud Blog (search result)
URL: https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
Date: 2025

[FACT]
At Next '25 Google shared 500+ customer stories of Google AI in action
— Google Cloud Blog (search result)
URL: https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders
Date: 2025

**Architecture Category:** Not disclosed
**Services:** Vertex AI, Gemini
**Scale Indicators:** 4M+ developers, 500+ customer stories, 20x usage increase
**Geography:** Global
**Relevance:** Platform-level AI adoption metrics, infrastructure not detailed

---

### Additional Infrastructure Signals

#### [DATA POINT]
**Source:** Amazon EKS Announcement - InfoQ
**URL:** https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/
**Date:** 2025-09

[STATISTIC]
Amazon EKS now supports clusters with up to 100,000 nodes, a 10x increase from previous limits
— InfoQ
URL: https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/
Date: 2025-09

[FACT]
EKS can potentially support up to 1.6 million AWS Trainium chips or 800,000 NVIDIA GPUs in a single Kubernetes cluster
— InfoQ (search result)
URL: https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/
Date: 2025-09

**Relevance:** AWS investing heavily in massive-scale Kubernetes for AI workloads

---

#### [DATA POINT]
**Source:** Azure AKS Engineering Blog
**URL:** https://blog.aks.azure.com/2025/12/05/kubernetes-ai-conformance-aks
**Date:** 2025-12-05

[FACT]
Azure Kubernetes Service (AKS) is proud to be among the first platforms certified for Kubernetes AI Conformance
— AKS Engineering Blog
URL: https://blog.aks.azure.com/2025/12/05/kubernetes-ai-conformance-aks
Date: 2025-12-05

**Relevance:** Azure positioning AKS for AI workload standardization

---

#### [DATA POINT]
**Source:** AWS Partner Network Blog
**URL:** https://aws.amazon.com/blogs/apn/powering-partner-success-2026-innovations/
**Date:** 2025

[STATISTIC]
82% of AWS Partners are delivering some form of AI as part of their AWS transformation delivery to end customers
— AWS Partner Network Blog
URL: https://aws.amazon.com/blogs/apn/powering-partner-success-2026-innovations/
Date: 2025

[STATISTIC]
Organizations implementing generative AI solutions on AWS with Partner support achieving 240% ROI and $16.5 million in benefits over three years
— AWS Partner Network Blog (search result)
URL: https://aws.amazon.com/blogs/apn/powering-partner-success-2026-innovations/
Date: 2025

**Relevance:** Ecosystem-wide AI adoption metrics on AWS

---

#### [DATA POINT]
**Source:** Microsoft Azure Blog
**URL:** https://azure.microsoft.com/en-us/blog/from-idea-to-impact-real-world-success-stories-of-building-intelligent-apps-with-azure/
**Date:** 2025

[FACT]
External customers like Replit, NFL Combine, Coca-Cola, and European Space Agency as well as internal teams like Microsoft Copilot have adopted Azure Container Apps as their compute platform for AI workloads
— Microsoft Azure Blog (search result)
URL: https://azure.microsoft.com/en-us/blog/from-idea-to-impact-real-world-success-stories-of-building-intelligent-apps-with-azure/
Date: 2025

**Relevance:** Azure promoting Container Apps for AI compute

---

#### [DATA POINT]
**Source:** OpenAI Partnership Announcement
**URL:** https://openai.com/index/next-chapter-of-microsoft-openai-partnership/
**Date:** 2025

[FACT]
OpenAI has contracted to purchase an incremental $250 billion of Azure services, with Microsoft no longer having a right of first refusal to be OpenAI's compute provider
— OpenAI/Microsoft (search result)
URL: https://openai.com/index/next-chapter-of-microsoft-openai-partnership/
Date: 2025

**Relevance:** Largest AI company (OpenAI) using Azure infrastructure at massive scale

---

## Preliminary Estimates

### Architecture Distribution (from disclosed case studies only)

**Direct Counts:**
- Managed Kubernetes (EKS/AKS/GKE): 9 companies (Flawless, Liquid Analytics, Instabase, Sonantic, Duck Creek, PTC, Picterra, Stacks, implicitly Midjourney)
- Cloud-Native Non-K8s (Fargate/Container Apps): 5 companies (Autodesk, BILL, Smartsheet, Coca-Cola, unnamed SaaS)
- AI Platform Services Only (Bedrock/Azure OpenAI/Vertex AI): 11 companies (Bynder, Gong, DoorDash, WRITER, Workday, Air India, Medigold, Perplexity, Palo Alto Networks, Juganu, multiple Vertex AI customers)

**CRITICAL CAVEAT:** 11 of 25 case studies did not disclose underlying compute infrastructure, focusing only on AI platform services. True distribution unknown.

### Scale Indicators

[STATISTIC]
150,000–200,000 requests per minute (BILL on ECS/Fargate)
URL: https://aws.amazon.com/solutions/case-studies/bill-ecs-case-study/
Date: 2025

[STATISTIC]
Tens of millions of daily inference requests (Workday on SageMaker)
URL: https://aws.amazon.com/solutions/case-studies/workday-case-study/
Date: 2025

[STATISTIC]
1+ million goals processed within 2-hour SLAs (Liquid Analytics on EKS)
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

[STATISTIC]
Over 1 million consumers in 60 days (Coca-Cola on Container Apps)
URL: https://azure.microsoft.com/en-us/blog/from-idea-to-impact-real-world-success-stories-of-building-intelligent-apps-with-azure/
Date: 2025

### Cost/Performance Metrics

[STATISTIC]
63% compute cost savings via Spot Instances (Liquid Analytics on EKS)
URL: https://aws.amazon.com/solutions/case-studies/liquid-analytics-case-study/
Date: 2025

[STATISTIC]
70% cost reduction on development using Spot Instances (Instabase on EKS)
URL: https://aws.amazon.com/solutions/case-studies/instabase-ec2-case-study/
Date: 2025

[STATISTIC]
40% reduction in generative AI inference costs (Simplismart.ai on AWS)
URL: https://aws.amazon.com/solutions/case-studies/simplismart-ai-case-study/
Date: 2025

[STATISTIC]
50% reduction in generative AI application development time (DoorDash on Bedrock)
URL: https://aws.amazon.com/solutions/case-studies/doordash-bedrock-case-study/
Date: 2025

---

## Data Quality Assessment

### Completeness: 4/10

**What was found:**
- 25 named AI/ML SaaS companies with vendor case studies
- 9 companies with detailed infrastructure architecture disclosure
- Geographic coverage: primarily US, Europe, India
- Company sizes: primarily mid-market to enterprise

**What was missing:**
- 44% of case studies did not disclose underlying compute infrastructure
- Very few early-stage startups represented
- Limited Asia-Pacific representation (except India)
- No failed deployment or migration stories
- No cost breakdowns beyond percentage savings

### Recency: 8/10

Most case studies date from 2025, with one from 2023 (Midjourney). Strong recency for current market snapshot.

### Sample Size: 3/10

25 companies identified from three major cloud vendors (AWS, Azure, GCP). This represents an extremely small fraction of AI/ML SaaS companies globally. Vendor case study libraries likely contain 100-500 total AI/ML customer stories, but most lack infrastructure detail.

### Known Biases

**Selection Bias:**
- Vendors showcase successful deployments only
- Large customers overrepresented due to marketing value
- Companies using flagship services overrepresented
- Failed migrations or departing customers not documented

**Information Bias:**
- Case studies emphasize vendor-specific services
- Infrastructure details often omitted in favor of business outcomes
- Cost savings presented as percentages without absolute figures
- Performance metrics cherry-picked for maximum impact

**Temporal Bias:**
- Recent migrations and modernizations overrepresented
- Stable, long-running workloads underrepresented
- Cutting-edge features highlighted over mature services

---

## Limitations — What This Source CANNOT Tell Us

1. **True Market Distribution**
   - Case studies cannot reveal what percentage of AI SaaS companies use Kubernetes vs serverless vs VMs
   - No data on companies that chose competing cloud providers
   - No visibility into hybrid or multi-cloud architectures (vendors have no incentive to document this)

2. **Actual Infrastructure Costs**
   - Percentage savings presented without baseline figures
   - No monthly/annual cloud spend figures disclosed
   - Deep discounts for case study participants likely, not representative of standard pricing

3. **Technical Challenges**
   - Failed deployments not documented
   - Migration difficulties and workarounds not disclosed
   - Operational complexity hidden behind polished narratives

4. **Small/Early-Stage Companies**
   - Startups with <$1M cloud spend unlikely to get case studies
   - Pre-revenue companies not represented
   - Companies using free tiers or minimal services not featured

5. **Architectural Evolution**
   - Case studies show post-migration state, not ongoing architectural changes
   - No visibility into companies that migrated away from featured architectures
   - Architectural regrets and refactoring not discussed

6. **Comparative Analysis**
   - Cannot determine why companies chose one cloud over another (beyond marketing claims)
   - No data on companies that evaluated but rejected featured services
   - Multi-cloud strategies hidden or minimized

7. **Representative Geography**
   - Heavy US/Europe bias
   - Limited visibility into China, Southeast Asia, Latin America, Africa
   - Data sovereignty requirements may push companies to regional clouds not featured

8. **Infrastructure vs Platform Services**
   - 44% of case studies focus on AI platform services (Bedrock, Azure OpenAI, Vertex AI) without disclosing underlying compute infrastructure
   - Cannot determine if companies using Bedrock/Vertex AI are running on Kubernetes, serverless, or VMs beneath the abstraction layer
   - Platform service adoption does not equal infrastructure architecture insight

---

## Confidence Score: 3/10

**Justification:**

This data source provides **high-confidence factual data** about the specific companies featured in case studies (names, services used, quoted metrics). However, it provides **very low confidence** as a basis for understanding the broader AI SaaS infrastructure market.

**Why Low Confidence for Market Understanding:**
- Extreme selection bias makes generalization impossible
- 44% of case studies omit infrastructure architecture details
- Sample size (25 companies) is negligible relative to thousands of AI SaaS companies globally
- Marketing materials systematically exclude negative data points
- No statistical validity for extrapolating to market trends

**Appropriate Use of This Data:**
- Identifying real-world examples of specific architecture patterns (EKS with GPUs, ECS/Fargate for SaaS)
- Gathering direct quotes from named companies for reference
- Understanding vendor positioning and messaging strategies
- Validating that certain architectures exist and work at scale

**Inappropriate Use of This Data:**
- Claiming "X% of AI SaaS companies use Kubernetes" based on case study counts
- Inferring cost structures for typical AI SaaS companies
- Determining market leader in AI infrastructure
- Predicting what architecture a given AI SaaS company likely uses

**To increase confidence, this data must be triangulated with:**
- Third-party market research (Gartner, Forrester, IDC)
- Developer surveys (Stack Overflow, State of DevOps)
- Job posting analysis (infrastructure roles at AI SaaS companies)
- GitHub repository analysis (infrastructure-as-code patterns)
- Direct outreach to AI SaaS companies not featured in vendor case studies

---

## Sources

- [AWS Customer Success Stories](https://aws.amazon.com/solutions/case-studies/)
- [AWS Generative AI Customers](https://aws.amazon.com/ai/generative-ai/customers/)
- [Azure Customer Stories](https://www.microsoft.com/en/customers)
- [Azure AKS Customer Stories](https://learn.microsoft.com/en-us/azure/aks/windows-aks-customer-stories)
- [Google Cloud Customers](https://cloud.google.com/customers)
- [Google Cloud Real-world GenAI Use Cases](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- [InfoQ: Amazon EKS Ultra-Scale](https://www.infoq.com/news/2025/09/aws-eks-kubernetes-ultrascale/)
- [AKS Engineering Blog: Kubernetes AI Conformance](https://blog.aks.azure.com/2025/12/05/kubernetes-ai-conformance-aks)
- [Google Cloud Press Center: Midjourney](https://www.googlecloudpresscorner.com/2023-03-14-Midjourney-Selects-Google-Cloud-to-Power-AI-Generated-Creative-Platform)
- [Bion Consulting: Sonantic Case Study](https://www.bionconsulting.com/case-studies/scaling-ai-driven-voice-technology-with-aws-and-eks)
- [OpenAI Partnership Announcement](https://openai.com/index/next-chapter-of-microsoft-openai-partnership/)
