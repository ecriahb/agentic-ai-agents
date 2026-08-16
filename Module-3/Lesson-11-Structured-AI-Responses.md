# 🚩 Jai Bajrangbali!

# Lesson 11 — Structured AI Responses

> **Human ke liye paragraph enough ho sakta hai; application ke liye predictable fields chahiye.**

---

## 🎯 Lesson Goal

Aap samjhoge:

- free-form text vs structured data
- JSON output
- schema kya hota hai
- Pydantic validation
- structure validation vs truth validation
- enum/required fields
- parsing failures
- evidence-grounded RCA contract

---

## 1. Problem with Free-Form Output

Model output 1:

```text
The issue appears to be caused by an NSG rule removal...
```

Model output 2:

```text
Root Cause: NSG rule removal
Impact: Connectivity failed
Fix: Restore rule
```

Human dono samajh lega.

Application ko problem:

```text
Where exactly is root_cause?
Is impact present?
What is severity?
Can pipeline parse this safely?
```

---

## 2. Structured Output

Desired contract:

```json
{
  "root_cause": "...",
  "impact": "...",
  "recommended_fix": ["..."],
  "severity": "high",
  "confidence": "medium"
}
```

Now downstream systems can process fields deterministically.

---

## 3. JSON Is Not Enough

Valid JSON:

```json
{
  "root_cause": 900,
  "severity": "banana"
}
```

Syntactically JSON valid hai, but application contract invalid.

Therefore:

```text
JSON format
   ↓
Schema validation
```

---

## 4. Schema Kya Hai?

**English Definition:**
> A schema defines the expected structure, field types, required values and constraints of data.

Conceptual RCA schema:

```text
root_cause       → required string
impact           → required string
recommended_fix  → list of strings
severity         → low | medium | high | critical
confidence       → low | medium | high
```

---

## 5. Pydantic Example

```python
from typing import Literal
from pydantic import BaseModel


class IncidentRCA(BaseModel):
    root_cause: str
    impact: str
    recommended_fix: list[str]
    severity: Literal["low", "medium", "high", "critical"]
    confidence: Literal["low", "medium", "high"]
```

Validate:

```python
rca = IncidentRCA.model_validate({
    "root_cause": "NSG rule removed",
    "impact": "AKS connectivity validation failed",
    "recommended_fix": ["Restore required NSG rule"],
    "severity": "high",
    "confidence": "medium"
})

print(rca.model_dump())
```

---

## 6. Validation Failure

```python
IncidentRCA.model_validate({
    "root_cause": "NSG rule removed",
    "impact": "Connectivity failed",
    "recommended_fix": [],
    "severity": "banana",
    "confidence": "medium"
})
```

Pydantic rejects invalid enum/type according to schema.

This prevents invalid data from silently entering downstream systems.

---

## 7. Critical Principle: Structure ≠ Truth

This is one of the most important lessons from Module 1.

Model can produce perfectly valid schema:

```json
{
  "root_cause": "Database corruption",
  "impact": "All customer data lost",
  "recommended_fix": ["Restore backup"],
  "severity": "critical",
  "confidence": "high"
}
```

But if evidence never mentioned database corruption, it is hallucination.

Therefore:

```text
Schema Validation
        ↓
Structure is valid
        ≠
Claim is factually supported
```

Need both:

```text
Structured Output Validation
         +
Evidence / Business Validation
```

---

## 8. Evidence-First RCA Contract

Prompt rule:

```text
Use only supplied evidence.
If root cause cannot be supported, state "insufficient evidence".
Do not invent customer impact.
```

Application rule:

```text
No evidence
   ↓
Do not call final RCA reporter
```

Schema rule:

```text
root_cause
impact
recommended_fix
severity
confidence
```

Together:

```text
Prompt Guardrail
 +
Schema Guardrail
 +
Application Guardrail
```

---

## 9. Provider-Side Structured Outputs

Modern LLM APIs may support provider-side structured output/schema features. Where supported, prefer an explicit schema contract rather than asking only "please return JSON".

Current OpenAI documentation distinguishes structured JSON-schema output from older JSON-only mode and recommends schema-based Structured Outputs for supported models.

Even then:

> Provider schema adherence does not prove factual correctness.

---

## 10. Parsing Strategy

Bad:

```python
text = model_response
# regex everything and hope fields exist
```

Better:

```text
Provider structured-output feature (if supported)
        ↓
Parse structured object
        ↓
Pydantic/business validation
        ↓
Use downstream
```

If provider returns plain JSON text:

```python
import json

data = json.loads(raw_text)
rca = IncidentRCA.model_validate(data)
```

---

# 🛠️ DevOps Example

```text
pipeline.log
 ↓
LLM
 ↓
Structured RCA
 ↓
Pydantic
 ↓
Evidence validation
 ↓
Ticket / Slack / Dashboard / Pipeline Gate
```

This is what makes AI output machine-consumable.

---

# ❌ Common Mistakes

- "return JSON" ko sufficient validation samajhna
- schema validation ko hallucination protection samajhna
- missing required fields accept karna
- severity free-form rakhna
- model-generated confidence blindly trust karna
- raw output directly deployment automation me execute karna

---

# 🎤 Interview Point

**Q: What is the difference between structured output and validated truth?**

Structured output ensures the data follows an expected shape. Truth validation separately verifies whether the claims are supported by trusted evidence and business rules.

---

# 🔁 Why Next Lesson?

Ab saare building blocks ready hain. Final lesson me complete app banayenge:

> **Lesson 12 — Mini Project: First AI Application**
