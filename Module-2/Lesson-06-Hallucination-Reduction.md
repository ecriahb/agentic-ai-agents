# 🚩 Jai Bajrangbali!

# Lesson 06 — Hallucination Reduction Techniques

> **Goal model ko “confident sounding” banana nahi; evidence ke bahar jaane se rokna hai.**

## 🎯 Goal
Prompt-level techniques samajhna jo unsupported claims reduce karte hain.

---

# 1. Evidence Boundary

```text
Use only the supplied evidence.
Do not assume Azure, AKS or Terraform state that is not shown.
```

Ye model ko knowledge boundary deta hai.

---

# 2. Fact vs Inference Separation

```text
For every conclusion classify it as:
- Confirmed Fact
- Supported Inference
- Unknown / Not Verified
```

Example:

```text
Fact: NSG rule was removed.
Fact: AKS subnet connectivity validation failed.
Inference: removed rule likely contributed to connectivity failure.
Unknown: whether customer traffic experienced downtime.
```

---

# 3. Abstention Rule

```text
If the evidence is insufficient to identify a root cause,
return "Insufficient evidence" and list the missing evidence required.
```

A reliable model ko “I don't know yet” bolne ki permission dena important hai.

---

# 4. Quote / Evidence Mapping

```text
Every root-cause claim must reference at least one supplied evidence item.
```

Better output:

```text
Claim: Network rule removal likely caused connectivity failure.
Evidence:
E1 - aks-subnet-allow was removed.
E2 - AKS subnet connectivity validation failed.
```

---

# 5. No Invented Tool Results

```text
Never write a kubectl, az, terraform or pipeline result unless it appears
in the provided evidence or was returned by an executed tool.
```

Bad:

```text
kubectl get nodes shows NotReady.
```

if no such command actually ran.

---

# 6. Confidence Policy

Instead of model freely choosing confidence:

```text
High   = multiple independent evidence sources directly support claim
Medium = one strong source or correlated evidence
Low    = incomplete / indirect evidence
```

Module 1 learning:
> Confidence can be application policy, not only LLM opinion.

---

# 7. Ask for Missing Evidence

Prompt:

```text
Before recommending a fix, list the minimum missing evidence needed to validate the hypothesis.
```

For AKS network failure:
- current NSG rules
- subnet effective routes
- failed connectivity test
- Terraform diff/plan

---

# 8. Negative Constraints

Useful:

```text
Do not:
- claim downtime unless confirmed
- fabricate resource names
- invent command output
- assume region/environment
- convert correlation into certainty
```

But overloading with 50 negatives can reduce clarity. Keep them task-specific.

---

# 9. Prompt Guardrail vs Application Guardrail

```text
Prompt: "Do not run destructive commands"
```

Good instruction, but real protection:

```text
read-only credential
+ tool allowlist
+ command parser
+ approval workflow
```

Prompt engineering cannot replace RBAC.

---

# 🧪 Before vs After

Weak:

```text
Find root cause and fix this production AKS issue.
```

Grounded:

```text
Use only Evidence E1-E3.
Separate facts from inference.
If root cause is not sufficiently supported, say Insufficient evidence.
Do not claim customer impact without evidence.
For every hypothesis list supporting evidence and missing validation.
Recommend read-only checks before changes.
```

---

# 🔑 Summary

```text
Hallucination Reduction
= evidence boundary
+ fact/inference separation
+ abstention
+ evidence mapping
+ no fake tool output
+ controlled confidence
```

# ➡️ Why Next?
Even the best prompt fails if context itself noisy, incomplete or badly selected hai. Next: Context Engineering.
