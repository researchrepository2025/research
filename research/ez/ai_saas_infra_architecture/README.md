# AI SaaS Infrastructure Architecture Market Sizing

**Date:** 2026-02-12
**Method:** 24-agent research swarm (4 waves)

## Research Question

What percentage of AI SaaS companies use each of three infrastructure architecture patterns?

- **Cloud-native (non-K8s):** Serverless, PaaS, managed containers (ECS/Fargate, Cloud Run)
- **Managed Kubernetes:** AKS, EKS, GKE
- **Open/Self-managed Kubernetes:** Self-hosted K8s on bare metal, VMs, or cloud IaaS

## Key Results

| Architecture | <$10M | $10-50M | $50-200M | $200M+ | US Avg | EU Avg | Overall |
|---|---|---|---|---|---|---|---|
| Cloud-native (non-K8s) | 60-80% (C:4) | 30-45% (C:4) | 20-30% (C:3) | 12-22% (C:4) | 33-45% (C:4) | 15-30% (C:2) | 30-45% (C:3) |
| Managed K8s | 15-28% (C:3) | 50-62% (C:5) | 50-62% (C:5) | 52-63% (C:6) | 45-55% (C:4) | 35-50% (C:2) | 40-53% (C:4) |
| Open K8s | 1-4% (C:4) | 4-10% (C:4) | 7-14% (C:3) | 22-33% (C:5) | 8-16% (C:3) | 18-30% (C:2) | 12-20% (C:3) |

C:N = Confidence score (1-10). Categories are non-exclusive (companies use multiple architectures).

## File Structure

```
wave1/          - Raw data from 8 fact-gathering agents
wave2/          - Cross-cut analysis from 9 analysis agents
consolidated/   - Unified draft report
verification/   - 4 adversarial verification reports
final/          - Confidence scores + FINAL REPORT
```

## Start Here

**Final report:** `final/24_FINAL_REPORT.md`
