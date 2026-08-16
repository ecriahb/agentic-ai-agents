# 🚩 Jai Bajrangbali!

# Lesson 01 — Prompt Engineering Basics

> **Good model + weak prompt = unreliable result. Good model + clear prompt = much more useful result.**

---

# 🎯 Lesson Goal

Is lesson me hum samjhenge ki prompt kya hota hai, prompt engineering kya hoti hai, aur ek vague DevOps request ko reliable instruction me kaise convert karte hain.

## English Definition

> **Prompt Engineering** is the practice of designing instructions, context, examples and output requirements so an AI model can perform a task more reliably.

---

# 1. Prompt Kya Hai?

Prompt sirf ek question nahi hota. Prompt model ko diya gaya **complete instruction package** hota hai.

```text
Prompt
├── instruction
├── context
├── evidence
├── constraints
└── expected output
```

Bad example:

```text
Why did AKS fail?
```

Problem:
- environment unknown
- evidence missing
- time window missing
- desired output unknown
- model guess kar sakta hai

Better example:

```text
Analyze the following production deployment evidence.
Identify only evidence-supported root causes.
Do not invent missing Azure or Kubernetes facts.
Return: Root Cause, Impact, Fix, Confidence.

Evidence:
Deployment failed during Terraform Apply.
NSG rule aks-subnet-allow was removed.
AKS subnet connectivity validation failed.
```

---

# 2. Prompt Engineering Kyu Chahiye?

LLM natural language ko interpret karta hai. Agar request ambiguous hai, model ko missing assumptions fill karne pad sakte hain.

```text
Vague Prompt
   ↓
More Interpretation Freedom
   ↓
More Variance / Guessing Risk

Clear Prompt
   ↓
Smaller Decision Space
   ↓
More Consistent Output
```

---

# 3. Prompt ke 5 Basic Questions

Har important prompt se pehle pucho:

1. **Who?** AI kis role me kaam kare?
2. **What does it know?** Relevant context/evidence kya hai?
3. **What exactly should it do?** Task kya hai?
4. **What must it not do?** Constraints kya hain?
5. **How should it answer?** Output format kya hai?

Ye Lesson 2 ka formal framework banega.

---

# 4. Specificity vs Over-Prompting

Specific hona useful hai, lekin unnecessary text add karna context ko noisy bana sakta hai.

Bad:

```text
You are the greatest, smartest, most intelligent DevOps architect in the world...
```

Useful:

```text
You are a Senior Azure DevOps incident analyst.
Focus on Terraform, AKS networking and deployment evidence.
```

Prompt ka goal model ko flatter karna nahi; **decision boundaries clear karna** hai.

---

# 5. DevOps Example — Pipeline Failure

### Weak Prompt

```text
Fix my pipeline.
```

### Improved Prompt

```text
Analyze this Azure deployment failure.

Task:
1. Identify the most likely failure stage.
2. Separate confirmed evidence from inference.
3. Suggest read-only validation commands first.
4. Do not recommend production changes unless evidence supports them.

Logs:
<PASTE LOGS>

Output:
- Failure Stage
- Evidence
- Likely Root Cause
- Validation Steps
- Recommended Fix
```

---

# 6. Prompt Is Not a Security Boundary

Important:

```text
Prompt says: "Do not delete resources"
```

Ye alone enough nahi hai.

Production system ko application-side controls bhi chahiye:

```text
Prompt Guardrail
      +
Tool Allowlist
      +
RBAC
      +
Validation
      +
Human Approval
```

Module 1 ka principle yahan continue hota hai: **LLM instruction follows; host application enforces.**

---

# 🧪 Practice

Convert this:

```text
Check Terraform problem.
```

Into a prompt containing:
- environment
- evidence
- exact task
- no-hallucination constraint
- fixed output format

Example answer:

```text
You are reviewing a Terraform deployment failure in production.
Use only the supplied plan and pipeline logs.
Identify the resource change most strongly correlated with the failure.
If evidence is insufficient, say "Insufficient evidence".
Return: Changed Resource, Evidence, Risk, Validation, Recommended Action.
```

---

# 🔑 Lesson Summary

```text
Prompt Engineering ≠ fancy wording
Prompt Engineering = clear instruction design

Weak Prompt → ambiguity
Strong Prompt → role + evidence + task + boundaries + output
```

# ➡️ Why Next Lesson?

Ab hume basic idea clear hai. Next lesson me hum isko ek repeatable production framework me convert karenge:

```text
Role + Context + Task + Constraints + Output
```
