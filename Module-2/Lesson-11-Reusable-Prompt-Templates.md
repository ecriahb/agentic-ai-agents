# 🚩 Jai Bajrangbali!

# Lesson 11 — Reusable Prompt Templates

> **Production prompt ko copy-paste paragraph ke bajay parameterized asset ki tarah treat karo.**

## 🎯 Goal
Reusable, versionable aur testable DevOps prompt templates banana.

---

# 1. Template Mental Model

```text
Stable Instructions
      +
Runtime Variables
      +
Evidence Bundle
      =
Final Prompt
```

Example variables:

```text
{environment}
{service}
{incident_time}
{deployment_stage}
{evidence}
```

---

# 2. RCA Template

```text
ROLE
You are a Senior DevOps incident analyst.

CONTEXT
Environment: {environment}
Service: {service}
Incident Time: {incident_time}

EVIDENCE
{evidence}

TASK
Identify the strongest evidence-supported root-cause hypothesis.

CONSTRAINTS
- Use only supplied evidence.
- Separate facts from inference.
- Do not invent customer impact.
- If evidence is insufficient, say so.

OUTPUT
1. Confirmed Evidence
2. Likely Root Cause
3. Confirmed Impact
4. Missing Evidence
5. Validation Steps
6. Recommended Fix
7. Confidence
```

---

# 3. Terraform Review Template

```text
Environment: {environment}
Change Ticket: {change_id}
Plan:
{terraform_plan}

Identify:
- destructive changes
- replacements
- networking/security changes
- dependency risks

Return:
Resource | Planned Change | Risk | Evidence | Required Validation
```

---

# 4. AKS Troubleshooting Template

```text
Cluster: {cluster}
Environment: {environment}
Symptom: {symptom}

Evidence:
{evidence}

Analyze layers:
Cluster → Nodes → Network → Workloads → Service/Ingress → Dependencies
Mark any layer without evidence as Not Verified.
```

---

# 5. Template Versioning

Treat prompts like code:

```text
incident-rca-v1
incident-rca-v2
incident-rca-v3
```

Track:
- what changed
- why changed
- evaluation score before/after
- known limitations

---

# 6. Keep Variables Explicit

Bad:

```python
prompt = f"Analyze {data} and tell me what happened"
```

Better:

```python
prompt = template.format(
    environment=environment,
    service=service,
    evidence=normalized_evidence,
)
```

---

# 7. Separate System Template and Task Template

```text
system_prompt.txt
incident_rca_prompt.txt
terraform_review_prompt.txt
aks_troubleshooting_prompt.txt
```

Stable safety behavior system layer me; runtime task template task layer me.

---

# 8. Template Checklist

Before production use verify:

- role clear
- evidence boundary clear
- task specific
- abstention supported
- output fixed
- unsafe instructions blocked by host
- template tested on multiple fixtures
- version tracked

---

# 🔑 Summary

```text
Reusable Prompt = stable policy + parameters + evidence + output contract
```

# ➡️ Why Next?
Ab saare building blocks ready hain. Final lesson me complete DevOps Incident Analysis Prompt System banayenge.
