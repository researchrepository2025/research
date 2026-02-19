# G3 — Cross-Reference Consistency Check

**Quality Gate:** G3 | **Type:** Automated + Manual Audit
**Date:** 2026-02-19 | **Status:** FAIL (3 of 4 checks failed)

---

## Overall Result: FAIL

| Check | Result | Summary |
|-------|--------|---------|
| A. Cross-Reference Format | **FAIL** | 0 of 15 sampled cross-references fully match the required format |
| B. Difficulty Rating Consistency | **PASS (Conditional)** | No discrepancies >1 point found in sampled pairs; some comparisons could not be completed |
| C. FTE Estimate Alignment | **FAIL** | Security operations FTE estimates show >0.5 FTE discrepancies across files |
| D. Terminology Consistency | **FAIL** | Terminology glossary partially violated in file titles/headers |

---

## A. Cross-Reference Format Audit

**Required Format (from research plan, lines 106-109):**
```
"See [F##: Agent Title] for detailed coverage of [topic]."
```

### Sampled Files and Findings

#### F32: On-Premises Microservices (wave5)
**Lines 270-276 — "Related -- Out of Scope" section:**
```
- Covered in F34
- Covered in F48
- Covered in F47
- Covered in F50
- Covered in F39
- Covered in F40
- Covered in Wave 7
```
**Line 256:** `See F48 for CI/CD infrastructure detail`

**Violations:**
- Uses "Covered in F##" instead of "See [F##: Title] for detailed coverage of [topic]" (7 instances)
- Uses "See F48 for CI/CD infrastructure detail" -- missing brackets, missing title (1 instance)
- **Total: 8 violations, 0 compliant**

---

#### F52: Managed Kubernetes Platforms (wave7)
**Lines 512-517 — "Related -- Out of Scope" section:**
```
- See [F53: Portable Kubernetes]
- See [F54: Kubernetes Operators]
- See [F55: Service Mesh Details]
```

**Violations:**
- All three are missing the required suffix "for detailed coverage of [topic]"
- F55 title is incorrect: file title is "Kubernetes Service Mesh & Networking", reference says "Service Mesh Details"
- **Total: 3 violations, 0 compliant**

---

#### F56: Design & Architecture Phase Constraints (wave8)
**Lines 308-317 — "Related -- Out of Scope" section:**
```
- See [F57] for CI/CD and testing constraints
- See [F58]
- See [F59]
- See [F52: Managed K8s Platforms]
- See [F53: Portable K8s ISV Delivery]
- See [F04: RAG Pipelines]
- See [F05: LLM Model Serving]
- See [F06: Vector Databases]
```
**Line 144 (inline):** `See [F06: Vector Databases] for detailed performance benchmarks and selection criteria.`

**Violations:**
- F57, F58, F59: Missing agent titles entirely
- F52, F53, F04, F05, F06 (lines 308-317): Missing "for detailed coverage of [topic]" suffix
- F04, F05, F06: Titles may be abbreviated (plan titles are "RAG Pipelines & Retrieval Augmentation", "LLM Model Serving & Inference Optimization", "Vector Databases & Embedding Infrastructure")
- Line 144: **Closest to correct format** but says "for detailed performance benchmarks and selection criteria" rather than "for detailed coverage of [topic]" -- this is arguably compliant as a reasonable variation
- **Total: 8 violations, 0-1 compliant (line 144 is borderline)**

---

#### F67: Compliance & Regulatory (wave10)
**Lines 536-539 — "Related -- Out of Scope" section:**
```
- see F46-F47
- see F46
- see F65
```

**Violations:**
- Lowercase "see" instead of "See"
- No brackets around references
- No agent titles
- No "for detailed coverage of [topic]" suffix
- Combined reference "F46-F47" instead of separate entries
- **Total: 3 violations, 0 compliant**

---

#### F71: On-Premises Security Operations (wave10)
**Lines 410-413 — "Related -- Out of Scope" section:**
```
- See [F46: IAM and Authentication]
- See [F47: Encryption and Secrets]
- See [F67: Compliance Frameworks]
```

**Violations:**
- All three missing "for detailed coverage of [topic]" suffix
- F46 title mismatch: actual plan title is "On-Prem IAM & Identity", reference says "IAM and Authentication"
- F47 title mismatch: actual plan title is "On-Prem Secrets, Certificates & Encryption", reference says "Encryption and Secrets"
- F67 title mismatch: actual plan title is "Compliance & Regulatory Requirements Across Deployment Models", reference says "Compliance Frameworks"
- **Total: 3 violations, 0 compliant**

---

#### F50: On-Premises Monitoring & Alerting (wave6)
**Lines 335-337 — "Cross-References" section:**
```
- See F49 (Logging) for log aggregation stack
- See F51 (Distributed Tracing) for Jaeger/Tempo/OpenTelemetry trace pipeline
- See F04 (Infrastructure Compute) for on-premises server sizing
```

**Violations:**
- Uses parenthetical format "F49 (Logging)" instead of bracket format "[F49: Logging]"
- Missing "for detailed coverage of [topic]" suffix (uses custom descriptions)
- F04 title mismatch: "Infrastructure Compute" does not match plan title "RAG Pipelines & Retrieval Augmentation" for F04 (possibly meant F39: On-Prem Compute Management?)
- **Total: 3 violations, 0 compliant; possible wrong F## reference**

---

#### F15a, F23a, F31a: Infrastructure Integration Files (waves 2-4)
**No cross-references found in the sections read.** These files focus on per-service infrastructure integration patterns and do not contain "Related -- Out of Scope" sections referencing other agents in the body text sections examined.

### Cross-Reference Format Summary

| File | Cross-Refs Found | Compliant | Violations | Compliance Rate |
|------|-----------------|-----------|------------|-----------------|
| F32 | 8 | 0 | 8 | 0% |
| F52 | 3 | 0 | 3 | 0% |
| F56 | 9 | 0-1 | 8-9 | 0-11% |
| F67 | 3 | 0 | 3 | 0% |
| F71 | 3 | 0 | 3 | 0% |
| F50 | 3 | 0 | 3 | 0% |
| F15a/F23a/F31a | 0 | N/A | N/A | N/A |
| **Total** | **29** | **0-1** | **28-29** | **0-3%** |

**Result: FAIL.** Essentially zero cross-references match the required format. The standard was never consistently applied.

### Common Violation Patterns
1. **Missing "for detailed coverage of [topic]" suffix** -- universal across all files
2. **Missing or incorrect agent titles** -- frequent (F32, F56, F67)
3. **Wrong bracket syntax** -- F32 uses "Covered in", F50 uses parenthetical, F67 uses bare references
4. **Title mismatches** -- F52 (F55 wrong title), F71 (all three wrong titles), F50 (F04 possibly wrong agent entirely)
5. **Possible wrong F## number** -- F50 references "F04 (Infrastructure Compute)" which does not match F04's actual scope (RAG Pipelines)

---

## B. Difficulty Rating Consistency Check

**Requirement:** Overlapping domain ratings should be within +/-1 point across files.

### B1. On-Prem Networking: F40 vs F32

| Domain | F40 Rating | F32 Rating | Delta | Status |
|--------|-----------|-----------|-------|--------|
| On-prem networking (overall) | 3-5/5 (per F40 exec summary) | N/A (F32 doesn't rate networking) | N/A | Not comparable |

F32 does not separately rate networking -- it rates "Container Orchestration" at 4/5 which includes some networking aspects but is not directly comparable. **No discrepancy detected** but domains do not overlap cleanly.

### B2. On-Prem Compute/Containers: F39 vs F32

| Domain | F39 | F32 | Delta | Status |
|--------|-----|-----|-------|--------|
| On-prem compute infrastructure | Not rated in standard scale (FTE-focused) | Container Orchestration: 4/5 | N/A | Not comparable |

F39 focuses on hardware/GPU infrastructure and uses FTE/cost metrics rather than the standard difficulty rating table. F32 rates container orchestration at 4/5. The domains are adjacent but not identical -- F39 covers hardware procurement and GPU management while F32 covers application-level orchestration. **No direct discrepancy**, but F39 does not use the standard comparison table format for all domains.

### B3. On-Prem Security: F71 vs F46 vs F47

| Security Domain | F71 Rating | F46 Rating | F47 FTE-Implied | Delta | Status |
|-----------------|-----------|-----------|-----------------|-------|--------|
| SIEM (on-prem) | 4/5 | N/A | N/A | N/A | F71 scope only |
| IDS/IPS (on-prem) | 4/5 | N/A | N/A | N/A | F71 scope only |
| IAM/Identity (on-prem) | N/A | 4/5 (Directory) | N/A | N/A | F46 scope only |
| Multi-tenant Auth (on-prem) | N/A | 4/5 | N/A | N/A | F46 scope only |
| Secrets/certs (on-prem) | N/A | N/A | FTE 2.5-5.0 (implied 4-5/5) | N/A | F47 scope only |

F71, F46, and F47 have non-overlapping scope boundaries (SecOps, IAM, Secrets respectively). There is no domain where the same capability is rated in multiple files. **No discrepancy detected** -- clean scope separation.

### B4. Managed K8s vs Cloud-Native: F52 vs F08/F16/F24

F52 provides FTE estimates (1.0-2.5 FTE for managed K8s platform engineering) but does not provide a standard difficulty rating comparison table against cloud-native. F08, F16, F24 (cloud compute services) focus on cloud-native capabilities and do not rate managed K8s. These files serve different purposes in the research plan and are not designed to overlap. **No discrepancy detected** but cross-file comparison was not built into these agents' scope.

### B5. Cross-File Security Difficulty Ratings: F11 vs F19 vs F27

| Security Domain | F11 (AWS) On-Prem | F19 (Azure) On-Prem | F27 (GCP) On-Prem | Max Delta | Status |
|-----------------|-------------------|---------------------|-------------------|-----------|--------|
| Identity/IAM | 1.0-1.5 FTE | 4/5 difficulty | 0.5-1.0 FTE | N/A | Different metrics |
| Key/Secrets Mgmt | 0.5-1.0 FTE | 5/5 difficulty | 0.5-1.0 FTE | N/A | Different metrics |
| SIEM/Threat Detection | 1.0-2.0 FTE | 5/5 difficulty | 2.0-4.0 FTE | N/A | Different metrics |
| Total On-Prem FTE | 5.0-9.5 FTE | 4.5-10.5 FTE | 7.25-14.0 FTE | Varies | See below |

**Notable observation:** Total on-prem security FTE estimates vary substantially:
- F11 (AWS perspective): 5.0-9.5 FTE
- F19 (Azure perspective): 4.5-10.5 FTE
- F27 (GCP perspective): 7.25-14.0 FTE

The GCP file (F27) estimates significantly higher on-prem FTE (7.25-14.0) compared to AWS (5.0-9.5) and Azure (4.5-10.5). However, F27 includes BeyondCorp/Zero Trust (1.0-2.0 FTE on-prem) as a security domain that F11 and F19 do not include equivalently, partially explaining the higher total. The ranges overlap at the high end. **Within acceptable tolerance** given different scope boundaries, but the variation should be noted for synthesis agents.

### Difficulty Rating Consistency Summary

**Result: PASS (Conditional).** No direct discrepancies >1 point were found in overlapping domains. However, the audit is limited by:
1. Many files do not rate identical domains, making cross-file comparison difficult
2. Some files use FTE estimates without difficulty ratings, and vice versa
3. F39 (compute) does not use the standard comparison table format consistently

---

## C. FTE Estimate Alignment Check

**Requirement:** FTE estimates for the same domain should not differ by >0.5 FTE without explanation.

### C1. Monitoring/Observability: F50 vs F12/F20/F28

| Model | F50 (On-Prem Monitoring) | F12 (AWS Observability) | F20 (Azure Observability) | F28 (GCP Observability) |
|-------|-------------------------|------------------------|--------------------------|------------------------|
| On-Premises (Medium) | 1.5-2.5 FTE | N/A (cloud-only scope) | N/A | N/A |
| On-Premises (Large) | 2.5-4.0 FTE | N/A | N/A | N/A |
| Cloud-Native | 0.3-0.6 FTE (medium) | Not explicitly stated | Not explicitly stated | Not explicitly stated |

F12, F20, F28 focus on cloud-native services and do not provide on-prem FTE estimates for monitoring. F50 is the sole source for on-prem monitoring FTE. **No overlap to compare** -- clean scope separation.

### C2. Security Operations: F71 vs F67 vs F11/F19/F27

| Domain | F71 (SecOps) | F67 (Compliance) | F11 (AWS Security) | F19 (Azure Security) | F27 (GCP Security) |
|--------|-------------|-----------------|-------------------|---------------------|-------------------|
| On-Prem Total SecOps FTE | 2.75-5.5 (excl. SOC analysts) | N/A | 5.0-9.5 | 4.5-10.5 | 7.25-14.0 |
| On-Prem SIEM FTE | 1.0-2.0 | N/A | N/A (no breakdown) | 1.5-2.0 | 2.0-4.0 |
| On-Prem Compliance FTE | N/A | 2.5-4.0 | N/A | N/A | N/A |

**SIEM FTE discrepancy detected:**
- F71: SIEM ops = 1.0-2.0 FTE (on-prem)
- F19: SIEM (Sentinel vs on-prem) = 1.5-2.0 FTE (on-prem)
- F27: SCC equivalent = 2.0-4.0 FTE (on-prem)

F27's on-prem SIEM estimate (2.0-4.0 FTE) exceeds F71's (1.0-2.0 FTE) by 1.0-2.0 FTE -- **exceeds the 0.5 FTE threshold**. F27 labels this as "CSPM + SIEM + vuln scanner + compliance" which bundles multiple domains that F71 separates. This is a scope-definition difference, not a true data conflict, but it creates confusion for synthesis agents.

**Total on-prem security FTE discrepancy:**
- F71: 2.75-5.5 FTE (SecOps tools only, excluding SOC analysts)
- F11: 5.0-9.5 FTE (all security domains including IAM, CIAM, KMS, WAF, SIEM, CSPM)
- F19: 4.5-10.5 FTE (all security domains)
- F27: 7.25-14.0 FTE (all security domains including Zero Trust)

These are not directly comparable because F71 explicitly excludes IAM (F46), secrets (F47), and compliance (F67), while F11/F19/F27 include all security domains. However, no file clearly explains the aggregation relationship. A synthesis agent summing F46 (2.75-4.75) + F47 (2.5-5.0) + F71 (2.75-5.5) + F67 compliance (2.5-4.0) would get 10.5-19.25 FTE, which is substantially higher than any individual cloud file's on-prem total. **This indicates potential double-counting risk** for synthesis agents.

### C3. CI/CD: F48 vs F14/F22/F30

| Model | F48 (On-Prem CI/CD) | F14 (AWS CI/CD) | F22 (Azure CI/CD) | F30 (GCP CI/CD) |
|-------|---------------------|-----------------|-------------------|-----------------|
| On-Prem | 2.0-3.5 FTE | Not stated | Not stated | Not stated |

Cloud CI/CD files do not provide on-prem FTE estimates. F48 is the sole source. **No overlap to compare.**

### C4. IAM: F46 vs F11/F19/F27

| Domain | F46 (On-Prem IAM) | F11 (AWS) | F19 (Azure) | F27 (GCP) |
|--------|-------------------|-----------|-------------|-----------|
| On-Prem IAM Total | 2.75-4.75 FTE | IAM workforce 1.0-1.5 + CIAM 1.0-2.0 = 2.0-3.5 FTE | Identity 4/5 difficulty (no FTE) | IAM 0.5-1.0 + Identity Platform 1.0-2.0 = 1.5-3.0 FTE |

**IAM FTE discrepancy detected:**
- F46: 2.75-4.75 FTE (dedicated on-prem IAM file)
- F11: 2.0-3.5 FTE (IAM workforce + CIAM, from AWS security file)
- F27: 1.5-3.0 FTE (IAM + Identity Platform, from GCP security file)

F46 vs F27 low-end: 2.75 vs 1.5 = **1.25 FTE delta, exceeds 0.5 threshold.**
F46 vs F11 low-end: 2.75 vs 2.0 = **0.75 FTE delta, exceeds 0.5 threshold.**

F46 is a dedicated, deep-dive IAM file covering directory services, SSO, multi-tenant auth, RBAC, token management, and audit -- it provides more granular estimates. F11 and F27 estimate IAM as one of 8 security domains with less granularity. The higher F46 estimate is expected given deeper analysis, but the discrepancy is not explicitly reconciled in any file.

### FTE Estimate Alignment Summary

**Result: FAIL.** Multiple discrepancies exceed the 0.5 FTE threshold:

| Comparison | Delta | Explanation Provided? |
|------------|-------|-----------------------|
| SIEM: F71 vs F27 | 1.0-2.0 FTE | No (scope bundling difference) |
| IAM: F46 vs F27 | 1.25 FTE | No |
| IAM: F46 vs F11 | 0.75 FTE | No |
| Aggregate Security: wave6 sum vs F11/F19/F27 | Potential double-counting | No reconciliation guidance |

---

## D. Terminology Consistency Spot-Check

**Required terminology (from plan lines 62-67):**
- "On-premises" (not "on-premise"; "on-prem" acceptable in tables/headers only)
- "Managed Kubernetes" (not just "K8s" in body text)
- "Cloud-native" (hyphenated)
- "Self-hosted" (hyphenated)

### Files Checked: F32, F39, F46, F52, F67

| File | "On-premises" | "On-prem" in headers | "Managed Kubernetes" | "Cloud-native" | Issues |
|------|--------------|---------------------|---------------------|----------------|--------|
| F32 | Yes (body) | "On-Premises" (title) | "Managed K8s" in table header | "Cloud-Native" in table | "Managed K8s" used in table header -- acceptable per glossary exception for tables |
| F39 | "On-Premises" (title), "on-premises" (body) | "On-Prem" in agent header | N/A | N/A | Compliant |
| F46 | "On-Premises" (title), "on-premises" (body) | N/A | "Managed Kubernetes" used correctly | "cloud-native" used | Compliant |
| F52 | "Managed Kubernetes" in title | N/A | Correct | "cloud-native" used | Compliant |
| F67 | "on-premises" (body) | N/A | "Managed Kubernetes" | "Cloud-Native" | Compliant |

**Additional observation from file naming convention:**
All wave 6 files use "onprem" in their filenames (e.g., F39_onprem_compute.md, F46_onprem_iam_identity.md). This is acceptable as filenames are technical identifiers, not body text.

**Specific violations found:**
1. The glossary says `"On-premises" (not "on-prem" in body text; "on-prem" acceptable in tables/headers only)`. All five files appear to comply with this rule in their body text, using "on-premises" consistently. However, this check was limited because Grep was unavailable -- a comprehensive regex scan across all 78 files could not be performed.

2. The glossary says `"Managed Kubernetes"` should be used, not just "K8s". In several files (F32, F56), "Managed K8s" is used in table headers, which is within the acceptable exception. However, some files use "K8s" as shorthand in body text (e.g., F56 line 308: "See [F52: Managed K8s Platforms]") -- this is a cross-reference context, which is a gray area.

**Result: FAIL (Marginal).** While the five files checked are substantially compliant in body text, the terminology check could not be exhaustively performed across all 78 files due to tool limitations (Grep unavailable). Two marginal issues were identified:
1. "Managed K8s" used in table headers (permissible but inconsistent with the "Managed Kubernetes" standard)
2. Abbreviated titles in cross-references use "K8s" shorthand

---

## Recommendations for Layer 1 Synthesis Agents

### Priority 1: Cross-Reference Standardization
Before synthesis begins, a normalization pass should be applied to all 78 files to:
1. Rewrite all cross-references to the standard format: `"See [F##: Agent Title] for detailed coverage of [topic]."`
2. Verify every F## number points to the correct agent
3. Verify every title matches the research plan's agent title exactly
4. Flag and fix the F50 reference to "F04 (Infrastructure Compute)" which appears to be a wrong agent number (likely should be F39)

### Priority 2: FTE Aggregation Guidance
Synthesis agents need explicit guidance on how to aggregate FTE estimates across files to avoid double-counting. Specifically:
1. **Security FTE aggregation:** F46 (IAM) + F47 (Secrets) + F71 (SecOps) + F67 (Compliance) should be summed, but this total will exceed F11/F19/F27 individual estimates because the cloud files estimate all security domains in a single file. The synthesis layer should use the wave 6/10 detailed files as the primary source for on-prem estimates and the wave 2/3/4 files for cloud-native estimates.
2. **SIEM FTE bundling:** F27 (GCP) bundles CSPM + SIEM + vuln scanning + compliance into a single 2.0-4.0 FTE estimate, while F71 separates these into individual domains. Synthesis agents should use F71's granular breakdown as the primary source for on-prem SIEM estimates.

### Priority 3: Difficulty Rating Gap
F39 (On-Prem Compute) does not use the standard comparison table format. A normalization step should add a standard difficulty rating table to F39 for consistency with all other files.

### Priority 4: Title Consistency
Cross-references use informal or abbreviated titles (e.g., "IAM and Authentication" for F46, "Compliance Frameworks" for F67, "Service Mesh Details" for F55). These should be standardized to match the research plan's official agent titles before synthesis.

---

## Audit Limitations

1. **Tool availability:** Bash, Glob, and Grep tools were non-functional during this audit (ENOENT error on sandbox binary). All file discovery and content searches were performed using Read tool with manual filename guessing, which limits completeness.
2. **File discovery:** Two files (F41: On-Prem Relational Databases, F59: Operate & Monitor Phase Differences) could not be located despite multiple filename attempts. Their data could not be included in the difficulty rating or FTE comparisons.
3. **Terminology check depth:** Without Grep, the terminology check was limited to manual reading of five files rather than a comprehensive regex scan across all 78 files. The FAIL rating for terminology is conservative -- the five files checked were substantially compliant.
4. **Cross-reference sample:** 7 files were sampled for cross-reference format (F32, F50, F52, F56, F67, F71, and F15a/F23a/F31a). The remaining 68+ files were not checked. Given the 0-3% compliance rate in the sample, it is highly likely that cross-reference format violations are pervasive.
