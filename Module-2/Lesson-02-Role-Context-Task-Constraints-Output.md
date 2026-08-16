# 🚩 Jai Bajrangbali!

# Lesson 02 — Role + Context + Task + Constraints + Output

> **A reliable prompt should tell the model who it is, what it knows, what it must do, what boundaries apply, and how to answer.**

---

# 🎯 Lesson Goal

Is lesson me hum ek reusable 5-part prompt framework banayenge:

```text
R → Role
C → Context
T → Task
C → Constraints
O → Output
```

Is framework ko aap RCA, Terraform review, AKS troubleshooting, change analysis aur incident summary me reuse kar sakte ho.

---

# 1. Role

Role model ka working perspective set karta hai.

Example:

```text
You are a Senior Azure DevOps incident analyst.
```

Better role scope:

```text
You are a Senior Azure DevOps incident analyst specializing in AKS,
Terraform, Azure networking and CI/CD failures.
```

Role useful hai, but role alone evidence nahi deta.

---

# 2. Context

Context wo information hai jo task solve karne ke liye actually relevant hai.

Example:

```text
Environment: production
Platform: AKS
Deployment method: Terraform through CI/CD
Recent change: NSG rule removed
Observed failure: AKS subnet connectivity validation failed
```

Context should be relevant, not a data dump.

---

# 3. Task

Task exact action define karta hai.

Weak:

```text
Analyze this.
```

Strong:

```text
Determine whether the recent Terraform network change is supported by the evidence as the likely cause of the deployment failure.
```

One prompt me multiple tasks ho sakte hain, but unko numbered steps me break karo.

---

# 4. Constraints

Constraints model ke decision space ko control karte hain.

Examples:

```text
- Use only supplied evidence.
- Do not invent command output.
- Separate confirmed facts from hypotheses.
- If evidence is insufficient, explicitly say so.
- Recommend read-only validation before remediation.
```

Important:

> Constraints reduce hallucination risk, but application controls remain necessary for real tool execution.

---

# 5. Output

Output contract result ko predictable banata hai.

Example:

```text
Return exactly these sections:
1. Root Cause
2. Evidence
3. Impact
4. Validation
5. Fix
6. Confidence
```

Machine workflows ke liye JSON bhi use kar sakte hain:

```json
{
  "root_cause": "",
  "evidence": [],
  "impact": "",
  "fix": [],
  "confidence": "low|medium|high"
}
```

---

# 🧠 Full DevOps Prompt

```text
ROLE
You are a Senior Azure DevOps incident analyst specializing in AKS,
Terraform and Azure networking.

CONTEXT
Environment: production
Deployment stage: Terraform Apply
Evidence:
- NSG rule aks-subnet-allow was removed.
- AKS subnet connectivity validation failed.
- Deployment failed during Terraform Apply.

TASK
Identify the most likely root cause and the next safe validation steps.

CONSTRAINTS
- Use only the evidence above.
- Do not invent Azure resource state.
- Separate confirmed facts from inference.
- Do not claim application downtime unless evidence says so.
- Prefer read-only validation commands before remediation.

OUTPUT
Return:
1. Confirmed Evidence
2. Likely Root Cause
3. Confirmed Impact
4. Validation Steps
5. Recommended Fix
6. Confidence
```

---

# Why This Framework Works

```text
Role        → perspective
Context     → knowledge boundary
Task        → objective
Constraints → behavior boundary
Output      → response contract
```

Agar inme se koi missing ho, uncertainty increase ho sakti hai.

---

# 🧪 Exercise — Terraform Plan Review

Build a prompt for:

```text
Production Terraform plan me route table aur NSG changes aaye hain.
You want AI to identify risky changes before apply.
```

Suggested structure:

```text
ROLE: Senior Terraform reviewer
CONTEXT: prod plan + architecture note
TASK: identify high-risk changes
CONSTRAINTS: no unsupported assumptions, no apply instructions
OUTPUT: resource, change, risk, evidence, validation
```

---

# 🔑 Lesson Summary

```text
Reliable Prompt = Role + Context + Task + Constraints + Output
```

Is framework ko memorize karne se better hai har real prompt me consciously apply karna.

# ➡️ Why Next Lesson?

Ab ek new question aata hai: ye instructions sab har request me repeat karni chahiye ya kuch permanent rules alag hone chahiye?

Next:

```text
System Prompt vs User Prompt
```
