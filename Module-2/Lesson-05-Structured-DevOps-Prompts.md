# 🚩 Jai Bajrangbali!

# Lesson 05 — Structured DevOps Prompts

> **Operational prompt ka output predictable hona chahiye, especially jab result ticket, report ya automation me use hoga.**

## 🎯 Goal
RCA, deployment failure, Terraform review aur AKS troubleshooting ke liye structured prompts banana.

---

# 1. RCA Prompt Pattern

```text
ROLE
Senior DevOps incident analyst

CONTEXT
Environment, service, timestamps, deployment stage, evidence

TASK
Identify likely root cause and safe next checks

CONSTRAINTS
Use only evidence; separate fact/inference; no invented impact

OUTPUT
Root Cause / Evidence / Impact / Validation / Fix / Confidence
```

## Example

```text
Analyze the following production deployment evidence.

Evidence:
- Terraform Apply started.
- NSG rule aks-subnet-allow was removed.
- AKS subnet connectivity validation failed.
- Deployment failed.

Return exactly:
1. Confirmed Evidence
2. Likely Root Cause
3. Confirmed Impact
4. Validation Steps
5. Recommended Fix
6. Confidence
```

---

# 2. Terraform Change Review Prompt

```text
You are reviewing a Terraform plan before production apply.

Task:
- identify destructive/replacement/network/security changes
- explain why each is risky
- identify dependencies to validate

Constraints:
- do not claim actual outage
- distinguish planned change from observed state
- do not recommend apply until high-risk items are validated

Output table:
Resource | Change | Risk | Evidence | Validation
```

---

# 3. AKS Troubleshooting Prompt

```text
Analyze AKS evidence in this order:
1. control-plane/cluster state
2. node state
3. networking
4. workload/pod state
5. ingress/service path

Use only supplied kubectl/Azure outputs.
For every conclusion cite the exact evidence line.
If a layer has no evidence, mark it "Not verified".
```

---

# 4. Pipeline Failure Prompt

```text
Find the first meaningful failure, not the final generic error.
Build a timeline from the logs.
Separate primary failure from downstream failures.
Return:
- Failure Stage
- First Error
- Downstream Errors
- Likely Cause
- Next Validation
```

This avoids model focusing only on:

```text
Process exited with code 1
```

when actual root evidence appears earlier.

---

# 5. Structured Text vs JSON

Human review:

```text
Root Cause:
Evidence:
Impact:
Fix:
```

Automation/API:

```json
{
  "root_cause": "",
  "evidence": [],
  "impact": "",
  "validation_steps": [],
  "fix": [],
  "confidence": "medium"
}
```

Remember Module 1:

> Schema validation verifies shape, not factual truth.

---

# 🧪 Exercise
Create a prompt for GitHub Actions failure where Terraform plan succeeded but apply failed. Require timeline, first causal error, evidence and read-only validation.

# 🔑 Summary

```text
Structured Prompt
→ predictable investigation
→ predictable output
→ easier validation
→ easier automation
```

# ➡️ Why Next?
Structure aa gaya, but model ab bhi unsupported details generate kar sakta hai. Next: Hallucination Reduction.
