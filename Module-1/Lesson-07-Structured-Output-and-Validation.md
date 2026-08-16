# Module 1 — Lesson 7: Structured Output & Validation

> **Goal:** LLM free-text ko predictable application contract me convert karna aur samajhna ki schema validation factual validation nahi hoti.

## English definition
**Structured output constrains model responses into a defined data shape so applications can parse and validate them reliably.**

## Why this lesson now?
Free-text useful hai humans ke liye, but automation ko predictable fields chahiye.

```text
Free Text
"Looks like networking issue..."

vs

Structured RCA
{
  "root_cause": "...",
  "impact": "...",
  "recommended_fix": "...",
  "confidence": "medium"
}
```

## Mental model

```text
Prompt
  ↓
LLM
  ↓
Structured Candidate
  ↓
Schema Validation
  ↓
Business/Evidence Validation
  ↓
Trusted Application State
```

## Pydantic example

```python
from pydantic import BaseModel
from typing import Literal

class RCA(BaseModel):
    root_cause: str
    impact: str
    recommended_fix: str
    confidence: Literal["low", "medium", "high"]
```

Pydantic checks:

- required fields
- data types
- allowed literal values

Pydantic does **not** prove:

- root cause actually happened
- impact is supported by evidence
- confidence is justified
- recommended action is safe

## Critical distinction

```text
Schema-valid != Factually true
JSON-valid != Evidence-supported
```

Example:

```json
{
  "root_cause": "Database outage",
  "impact": "All customers affected",
  "recommended_fix": "Restart production DB",
  "confidence": "high"
}
```

This can be perfectly schema-valid and completely unsupported.

## Layered validation

```text
Layer 1 → JSON/schema
Layer 2 → required source IDs
Layer 3 → evidence support
Layer 4 → policy/authorization
Layer 5 → approval for risky action
```

## Practical
Run:

```powershell
python examples/03_structured_output.py
```

Then intentionally create/test:

1. missing field
2. invalid confidence value
3. valid schema but invented impact
4. valid schema with supported evidence

Write down which layer catches each problem.

## DevOps example
Evidence:

```text
[E1] Deployment failed during Terraform Apply
[E2] NSG rule aks-subnet-allow removed
[E3] AKS connectivity validation failed
```

Safe structured output should distinguish confirmed facts from inference.

## Common mistakes
- treating parser success as truth
- forcing confidence from model only
- no `UNKNOWN`/abstention path
- including destructive action directly in output contract without policy gate
- trusting model-generated source IDs without validating them

## Production pattern

```text
Model structured output
      ↓
Pydantic/schema
      ↓
Source/citation validator
      ↓
Evidence claim validator
      ↓
Deterministic confidence/policy
```

## Interview questions
1. Structured output kyun useful hai?
2. Pydantic kya validate karta hai?
3. Schema-valid output still unsafe kaise ho sakta hai?
4. Factual validation host layer me kyun honi chahiye?

## Revision

```text
Structure = machine readability
Validation = layered trust checks
Pydantic = shape/type validation
Evidence = factual grounding
```

## Why next lesson?
Ab model structured data de sakta hai. Next step me model ko external capability **request** karna sikhayenge: Tool Calling / Function Calling.