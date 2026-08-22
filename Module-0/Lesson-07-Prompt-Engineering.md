# 🚩 Jai Bajrangbali!

# Lesson 07 — Prompt Engineering

> **Strong Prompt = Role + Task + Context + Constraints + Output Format**

## Why This Topic Now?

Lesson 6 me samjha ki LLM confident but wrong ya generic answer de sakta hai. Prompt engineering ka purpose model ko magic words dena nahi; task ko clearly specify karna hai.

```text
Vague Request
   ↓
Vague / Generic Output

Clear Task + Context + Format
   ↓
More Controlled Output
```

## 🎬 Office Example

Manager bolta hai:

```text
“AKS fix kar do.”
```

Senior engineer ke paas immediately questions aayenge:

- Which cluster?
- What failed?
- When?
- What changed?
- Logs?
- Expected output?

LLM bhi isi tarah relevant details se benefit karta hai.

## Weak Prompt

```text
Fix AKS.
```

Possible result: generic Kubernetes troubleshooting checklist.

## Stronger Prompt

```text
Role:
You are a Senior Azure DevOps Architect.

Task:
Analyze why the production AKS deployment failed.

Context:
The deployment started failing immediately after a Terraform networking change.
The Terraform diff shows that an NSG rule allowing AKS subnet traffic was removed.
AKS reports network connectivity failures.

Output:
1. Evidence
2. Likely Root Cause
3. Confirmed Impact
4. Recommended Fix

Constraints:
Do not invent customer impact or data loss.
Distinguish facts from inferences.
```

## 🇬🇧 English Definition

> **Prompt Engineering is the practice of designing clear, structured instructions and context to guide an AI model toward useful, relevant, and appropriately formatted output.**

## Prompt Formula

```text
ROLE
  +
TASK
  +
CONTEXT
  +
CONSTRAINTS
  +
OUTPUT FORMAT
```

### Role
Kis perspective se answer chahiye?

```text
Senior Azure DevOps Architect
Security Reviewer
SRE
FinOps Consultant
```

### Task
Exactly kya karna hai?

```text
Analyze deployment failure.
```

### Context
Evidence kya available hai?

```text
Logs
Terraform diff
AKS status
Environment
```

### Constraints
Kya nahi karna?

```text
Do not invent missing evidence.
Do not recommend destructive action without approval.
```

### Output Format
Response kis shape me chahiye?

```text
Evidence
Root Cause
Impact
Fix
Prevention
```

## Live Practical Insight

Simple prompt se local model ne AKS ko kabhi AWS se confuse kiya. Detailed prompt me explicitly Azure context aur “do not confuse AKS with EKS” dene par factual direction improve hui.

But exact “2 lines only” instruction phir bhi perfectly follow nahi hui.

Lesson:

> **Prompt controls behavior probabilistically; it is not a hard software contract.**

Agar machine-readable exact schema chahiye, later structured outputs/schema validation use karenge.

## 💼 DevOps Prompt Template

```text
You are a Senior Azure DevOps Engineer.

Analyze the supplied deployment evidence.

Environment: <environment>
Service/Cluster: <name>
Recent Change: <change>
Logs: <logs>

Return:
- Evidence
- Likely Root Cause
- Confirmed Impact
- Recommended Fix
- Prevention

Rules:
- Use only supplied evidence.
- Mark assumptions explicitly.
- Do not propose destructive action without human approval.
```

## Prompt Engineering Is Not Security

A prompt can say:

```text
Never delete production resources.
```

But if your application exposes unrestricted delete tools, prompt alone is not sufficient security.

Production controls require:

```text
Prompt Rules
   +
Code Validation
   +
Permissions
   +
Allowlists
   +
Human Approval
```

## Common Mistakes

- Very vague prompts. ❌
- Huge irrelevant context. ❌
- No desired output format. ❌
- Role ko accuracy guarantee samajhna. ❌
- Prompt rule ko hard security boundary samajhna. ❌
- “Think harder” ko evidence ka replacement samajhna. ❌

## 🎯 Interview Corner

### Q. What makes a good prompt?

**Answer:**
> A strong prompt clearly defines the task, provides relevant context, sets useful constraints, specifies the desired output format, and optionally assigns an appropriate role or perspective.

### Q. Can prompt engineering eliminate hallucinations?

**Answer:**
> No. Clear prompts can improve model behavior, but factual reliability requires trusted context, tools or retrieval, validation, and human verification where appropriate.

## 🧭 Course Boundary — Where Prompt Engineering Lives

This lesson is an **introduction**, not the complete prompt-engineering reference.

- **Module 0:** vocabulary, mental models, and why structured instructions help.
- **Module 2:** the definitive prompt-engineering module: reusable frameworks, few-shot prompting, structured outputs, hallucination reduction, context engineering, prompt chaining, evaluation, and templates.
- **Module 5:** prompting is applied specifically to grounded RAG context.
- **Module 6:** prompts are implemented and composed through LangChain.
- **Module 8:** prompts become part of stateful agent graphs.

If a later lesson needs advanced prompt design, prefer the canonical Module 2 lesson rather than duplicating this introduction.

## 🧠 Remember This

> **Prompting guides the model; evidence grounds the model.**

## 📝 Homework

Write a professional prompt for:

```text
Production AKS deployment failure after Terraform change
```

Include:
- role
- task
- context
- constraints
- output format

## Why the Next Lesson Follows

Prompt engineering samajh aa gaya. Ab ek production application me question aata hai:

> **Permanent agent behavior/rules aur current user request ko alag kaise rakhen?**

➡️ **Next: Lesson 08 — System Prompt vs User Prompt**
