# 🚩 Jai Bajrangbali!

# Lesson 01 — Prompt Engineering Basics

> **Prompt engineering ka matlab clever sentence likhna nahi; model ko clear task, useful context, boundaries aur expected output dena hai.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- prompt kya hota hai
- prompt engineering kya solve karta hai
- vague prompt aur engineered prompt me difference
- instruction, context, constraints aur output contract ka role
- DevOps incidents me evidence-first prompt kyu important hai
- same prompt Ollama aur OpenAI dono par kaise test karna hai
- prompt ko security boundary kyu nahi samajhna chahiye

---

# 1. English Definition

**Prompt engineering is the practice of designing instructions, context, constraints and output requirements so that a language model performs a task more reliably and predictably.**

Simple Hinglish:

```text
LLM ko sirf "kya chahiye" nahi,
"kis evidence se",
"kin rules ke andar",
aur "kis format me"
answer dena hai — ye define karna prompt engineering hai.
```

---

# 2. Why This Topic Comes After Module 1

Module 1 me humne seekha:

```text
LLM call
→ tool request
→ host executes tool
→ evidence
→ structured RCA
```

Lekin same evidence par bhi weak instruction ho to model:

- extra assumptions kar sakta hai
- wrong impact invent kar sakta hai
- format change kar sakta hai
- facts aur recommendations mix kar sakta hai

So next engineering question:

```text
Model ko reliable instructions kaise dein?
```

---

# 3. Prompt Anatomy

A useful prompt often contains:

```text
ROLE
  ↓
CONTEXT / EVIDENCE
  ↓
TASK
  ↓
CONSTRAINTS
  ↓
OUTPUT CONTRACT
```

Example:

```text
ROLE:
You are a read-only DevOps incident analyst.

CONTEXT:
[E1] Terraform Apply removed aks-subnet-allow.
[E2] AKS subnet connectivity validation failed.

TASK:
Identify the strongest evidence-supported root-cause hypothesis.

CONSTRAINTS:
Do not invent downtime or customer impact.
If evidence is insufficient, say so.

OUTPUT:
Root Cause
Evidence
Evidence Gaps
Recommended Next Checks
```

---

# 4. Weak Prompt vs Strong Prompt

## Weak

```text
Why did my AKS deployment fail?
```

Problems:

```text
No evidence
No scope
No environment
No output format
No hallucination boundary
```

Model may answer from general knowledge.

## Better

```text
Analyze the supplied production deployment evidence.
Use only evidence for incident-specific factual claims.
Separate facts from inference.
Return Root Cause, Evidence Gaps and Next Checks.
```

Now behavior is more constrained.

---

# 5. Prompt != Context

This distinction important hai:

```text
Prompt = instructions
Context = information/evidence supplied to perform instructions
```

Example:

```text
Instruction:
Identify the failure stage.

Context:
Pipeline failed during Terraform Apply.
```

Do not mix both mentally.

Later Module 5 me context RAG se retrieve hoga.

---

# 6. Prompt != Evidence

A prompt can say:

```text
The NSG rule caused the issue.
```

But if evidence does not prove it, sentence likh dene se fact true nahi ho jata.

Core rule:

```text
Prompt guides reasoning.
Evidence supports claims.
```

---

# 7. Real DevOps Scenario

Incident evidence:

```text
[E1] Deployment failed during Terraform Apply.
[E2] NSG rule aks-subnet-allow was removed.
[E3] AKS subnet connectivity validation failed after the change.
```

Good task:

```text
Using E1-E3 only:
1. list confirmed facts
2. identify strongest supported hypothesis
3. state missing evidence
4. recommend read-only validation
```

Expected safe behavior:

```text
Confirmed:
- rule removed
- connectivity validation failed
- deployment failed

Supported hypothesis:
- NSG removal is strongly associated with the later connectivity failure

Unknown:
- exact customer impact
- node health unless separately checked
- whether restoration has fixed the problem
```

---

# 8. Specificity Without Over-Constraining

Too vague:

```text
Analyze this.
```

Too rigid:

```text
The answer must say NSG is definitely root cause.
```

Better:

```text
Choose the strongest evidence-supported explanation.
If evidence does not support a root cause, return INSUFFICIENT_EVIDENCE.
```

Good prompt engineering guides without forcing false conclusions.

---

# 9. Output Contract

Hum humans prose tolerate kar sakte hain, applications nahi.

Bad:

```text
Tell me what happened.
```

Better:

```text
Return:
- Confirmed Evidence
- Likely Root Cause
- Confirmed Impact
- Evidence Gaps
- Recommended Next Checks
```

Later structured output/Pydantic machine-level shape validate karega.

Remember:

```text
Good format != factual truth
```

---

# 10. Provider Independence

Same prompt ko different providers par run kar sakte ho:

```text
Ollama / qwen3:4b
or
OpenAI API
```

Practical:

```powershell
$env:LLM_PROVIDER="ollama"
python Module-2/examples/dual_provider_prompt_playground.py
```

Then:

```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="your-key"
python Module-2/examples/dual_provider_prompt_playground.py
```

Compare:

- structure adherence
- unsupported assumptions
- evidence citations
- verbosity
- latency

Do not judge only wording.

---

# 11. Prompt is Not a Security Boundary

System prompt me likhna:

```text
Never delete production.
```

useful hai, but sufficient nahi.

Real security:

```text
Tool allowlist
+ argument validation
+ RBAC
+ policy
+ human approval
```

Prompt = behavior guidance.
Host application = enforcement.

---

# 12. Common Beginner Mistakes

1. **Prompt ko question samajhna only** — production prompt is an instruction contract.
2. **Too much irrelevant context** — noise reduces quality.
3. **Desired conclusion prompt me inject kar dena** — confirmation bias.
4. **No abstention rule** — model forced answer de sakta hai.
5. **No output contract** — automation unreliable ho jata hai.
6. **Prompt ko authorization samajhna** — unsafe.
7. **One successful run ko proof samajhna** — prompts need evaluation across cases.

---

# 13. Production Checklist

Before using a prompt in an application, ask:

```text
Is task explicit?
Is evidence scope clear?
Are prohibited assumptions explicit?
Can model abstain?
Is output machine-consumable?
Are dangerous actions host-controlled?
Is prompt versioned?
Is there an eval dataset?
```

---

# 14. Interview Q&A

### Q1. What is prompt engineering?
Designing instructions, context, constraints and output requirements to improve model reliability for a task.

### Q2. Does a better prompt eliminate hallucination?
No. It reduces risk, but factual grounding and application validation are still required.

### Q3. Prompt vs context?
Prompt tells the model what to do; context supplies information/evidence to do it.

### Q4. Why define an output contract?
To make responses predictable and machine-consumable.

### Q5. Is a system prompt a security control?
It is a behavioral control, not an authorization boundary.

---

# 15. Quick Revision

```text
Prompt Engineering
=
Instruction Design
+ Relevant Context
+ Constraints
+ Output Contract
+ Evaluation
```

Core rule:

```text
Prompt guides.
Evidence grounds.
Host validates.
```

---

# 🧪 Homework

Take this weak prompt:

```text
Fix my AKS problem.
```

Rewrite it with:

- Role
- Context
- Task
- Constraints
- Output

Then run it on both Ollama and OpenAI and note three behavior differences.

---

# ➡️ Why Next?

Ab prompt ke pieces samajh aa gaye. Next lesson me hum ek repeatable framework banayenge:

```text
Role + Context + Task + Constraints + Output
```
