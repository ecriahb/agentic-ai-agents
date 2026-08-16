# 🚩 Jai Bajrangbali!

# Lesson 07 — Structured Output & Validation

> **JSON maangna aur schema enforce karna alag cheezein hain.**

## Why This Topic Now?

Prompt engineering behavior improve kar sakti hai, but exact machine-readable format guarantee nahi karti. Hamare experiment me model ne `fix` ki jagah `fixed` return kiya aur extra `solution` field add kar diya. Python application ko stable contract chahiye.

```text
Tokens + Focused Prompt
          ↓
Structured Schema + Validation
          ↓
Tool Calling
```

## Prompt-Only JSON Problem

Requested fields:

```text
root_cause
impact
fix
severity
```

Model kuch aisa return kar sakta hai:

```json
{
  "root_cause": "...",
  "impact": "Deployment Failure",
  "fixed": null,
  "severity": "critical",
  "solution": null
}
```

Ye valid JSON ho sakta hai, but application ke expected schema ke according invalid hai.

> **Valid JSON != Valid Application Schema**

## Pydantic Schema

```python
from pydantic import BaseModel, Field
from typing import Literal

class RCAResponse(BaseModel):
    root_cause: str = Field(min_length=5)
    impact: str = Field(min_length=5)
    fix: str = Field(min_length=5)
    severity: Literal["low", "medium", "high", "critical"]
```

## Ollama Structured Output Example

```python
from ollama import chat

messages = [
    {
        "role": "system",
        "content": "Use only provided evidence. Do not invent missing facts."
    },
    {
        "role": "user",
        "content": "An AKS deployment failed after a Terraform networking change. Provide RCA."
    }
]

response = chat(
    model="gemma3:1b",
    messages=messages,
    format=RCAResponse.model_json_schema()
)

result = RCAResponse.model_validate_json(
    response.message.content
)

print(result)
```

## Two Validation Layers

### 1. Schema Validation

Checks:

- Required fields present hain?
- Data type correct hai?
- Allowed values follow ho rahe hain?
- Minimum constraints satisfy ho rahi hain?

### 2. Business / Evidence Validation

Checks:

- Claim actual evidence se supported hai?
- Severity justified hai?
- Impact observed hai ya invent hua hai?
- Fix relevant hai?

## Structured Hallucination

Schema ye force kar sakta hai:

```json
{
  "severity": "critical"
}
```

Lekin agar outage ya customer impact ka evidence hi nahi diya gaya, to structurally valid output factual conclusion ko prove nahi karta.

## Senior Rule

> **Structure controls shape. Evidence controls truth. Business rules validate decisions.**

## 💼 DevOps Example

```text
Raw Evidence
   ↓
LLM
   ↓
Schema-constrained RCA
   ↓
Pydantic Validation
   ↓
Business/Evidence Validation
   ↓
Human / System Consumer
```

## 🎯 Interview Corner

### Q. What problem do Structured Outputs solve?

**Answer:**
> Structured outputs constrain the model response to a predefined schema, making results easier to parse and validate in software. They improve structural reliability, but factual correctness still requires grounding and validation.

## 🧠 Remember This

> **Schema validates structure. Evidence validates truth.**

## Why the Next Lesson Follows

Output ab predictable hai, but model ko current `prod-aks` status ya latest Terraform change automatically nahi pata. Live information lane ke liye external functions chahiye.

➡️ **Next: Lesson 08 — Tool Calling / Function Calling**
