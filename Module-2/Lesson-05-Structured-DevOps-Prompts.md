# 🚩 Jai Bajrangbali!

# Lesson 05 — Structured DevOps Prompts

> **DevOps prompt ko generic chat request nahi, repeatable operational analysis contract ki tarah design karo.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap:

- RCA prompt structure bana paoge
- Terraform change-review prompt design kar paoge
- AKS troubleshooting prompt design kar paoge
- evidence vs recommendation separate rakh paoge
- confirmed impact ko inferred impact se distinguish kar paoge
- output ko review-friendly aur automation-friendly bana paoge

---

# 1. English Definition

**A structured DevOps prompt defines the operational scope, authoritative evidence, analysis task, safety constraints and a fixed response contract for an engineering workflow.**

Mental model:

```text
Operational Request
      ↓
Target / Environment
      ↓
Source-Labeled Evidence
      ↓
Analysis Task
      ↓
Safety Constraints
      ↓
Structured DevOps Output
```

---

# 2. Why DevOps Needs Structure

DevOps questions often involve production systems.

Generic answer may accidentally mix:

```text
facts
best practices
hypotheses
commands
remediation
impact guesses
```

A structured prompt forces separation.

---

# 3. RCA Prompt Contract

A useful incident RCA prompt asks for:

```text
Confirmed Evidence
Timeline
Supported Root-Cause Hypothesis
Confirmed Impact
Evidence Gaps
Validation Steps
Recommended Fix
Confidence
```

Why this ordering?

```text
Evidence first
→ interpretation second
→ recommendation last
```

This reduces premature remediation.

---

# 4. RCA Example

```text
ROLE
You are a read-only Azure DevOps incident analyst.

CURRENT EVIDENCE
[E1] Deployment failed during Terraform Apply.
[E2] NSG rule aks-subnet-allow was removed.
[E3] AKS subnet connectivity validation failed.

TASK
Identify the strongest supported explanation.

RULES
- E* supports incident facts.
- Do not invent customer impact.
- Do not claim remediation was executed.
- If causality is not proven, label it as supported hypothesis.

OUTPUT
Confirmed Evidence
Likely Root Cause
Confirmed Impact
Evidence Gaps
Validation Steps
Recommended Fix
Confidence
```

Expected behavior:

```text
NSG removal is strongest supported hypothesis
but exact causal verification may still require effective NSG/route checks.
```

---

# 5. Terraform Change Review Prompt

Terraform review is not an incident RCA.

Goal is change risk before apply.

Context:

```text
plan diff
resource type
environment
network dependencies
policy rules
```

Output:

```text
Change Summary
Potential Blast Radius
Risk Level
Policy Violations
Required Validation
Rollback Considerations
Approval Recommendation
```

Important:

```text
Risk assessment != proof that failure will occur
```

---

# 6. Terraform Example

```text
Environment: production
Plan:
- delete azurerm_network_security_rule.aks_subnet_allow

Task:
Review this plan for production risk.

Constraints:
- Do not assume the rule is unused.
- State what dependency evidence is missing.
- Do not approve the change automatically.
```

Safer output:

```text
Risk: HIGH
Reason: production network security rule deletion may affect traffic.
Missing: approved network baseline and dependency validation.
Recommendation: senior/network review before apply.
```

---

# 7. AKS Troubleshooting Prompt

Troubleshooting needs observation-driven flow.

Useful output:

```text
Observed Symptoms
Confirmed State
Possible Causes
Evidence Needed Per Cause
Read-Only Checks
Escalation Criteria
```

Do not ask:

```text
Give me all commands to fix AKS.
```

Better:

```text
Based on current evidence, rank next read-only checks that can distinguish network, scheduling and application causes.
```

---

# 8. Different Task → Different Prompt

Do not use one giant prompt for everything.

```text
Incident RCA       → explain what likely happened
Change Review      → assess risk before change
Troubleshooting    → identify next diagnostic evidence
Postmortem         → timeline/learning/action items
Runbook Assistant  → procedure from approved reference
```

Prompt should match workflow semantics.

---

# 9. Current Evidence vs General Knowledge

Model may know:

```text
AKS can fail due to NSG, UDR, DNS, identity, capacity...
```

But current incident evidence may only support one subset.

Prompt should separate:

```text
Confirmed current facts
General possible causes
Recommended next checks
```

This is essential for trusted DevOps output.

---

# 10. Command Safety

Prompt may recommend:

```text
az network nic list-effective-nsg
kubectl get nodes
```

But generated command must not automatically execute.

Architecture:

```text
LLM recommendation
→ host validates command/tool
→ authorization
→ execution if allowed
```

For risky writes:

```text
human approval
```

---

# 11. Provider-Parity Practical

Files in `Module-2/examples/` include reusable prompts plus dual-provider playground.

Run same RCA contract on both providers and inspect:

```text
Did it preserve facts?
Did it overclaim causality?
Did it invent impact?
Did it follow output sections?
```

This turns provider comparison into an engineering test.

---

# 12. Common Mistakes

1. RCA prompt asks for fix before evidence.
2. Change-review prompt assumes every diff is dangerous.
3. Troubleshooting prompt returns writes before diagnostics.
4. Impact is inferred from severity instead of telemetry.
5. Facts and best-practice advice are mixed.
6. Environment/target omitted.
7. Output contains commands without safety classification.
8. No explicit `UNKNOWN` path.

---

# 13. Production Prompt Assets

Store prompt templates as versioned assets:

```text
prompts/
  incident_rca_v3.txt
  terraform_review_v2.txt
  aks_troubleshoot_v4.txt
```

Track:

```text
prompt version
model version
provider
eval dataset version
```

Prompt change can be a behavior change and should be reviewed like code.

---

# 14. Interview Q&A

### Q1. Why not one generic DevOps prompt?
Different workflows have different evidence semantics, risk and output requirements.

### Q2. What should come first in RCA output?
Confirmed evidence, before causal interpretation and remediation.

### Q3. Why separate confirmed impact?
To prevent the model from converting technical failure into unsupported customer/business impact claims.

### Q4. Should generated commands execute automatically?
No. Execution should be host-controlled with validation and authorization.

### Q5. What makes a prompt reusable?
Clear placeholders, stable rules, fixed output contract, versioning and eval coverage.

---

# 15. Quick Revision

```text
RCA          → evidence → hypothesis → gaps → validation → fix
Change review→ diff → blast radius → risk → validation → approval
Troubleshoot → symptom → possible causes → evidence → read-only checks
```

---

# 🧪 Homework

Create three prompts for the same AKS platform:

1. pre-deployment Terraform review
2. failed-deployment RCA
3. post-failure troubleshooting

Compare how task/output changes while evidence policy remains stable.

---

# ➡️ Why Next?

Structured prompt ban gaya, but model still hallucinate kar sakta hai. Next lesson me **hallucination reduction and abstention techniques** deep dive karenge.
