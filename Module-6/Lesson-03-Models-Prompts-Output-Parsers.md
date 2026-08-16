# 🚩 Jai Bajrangbali!

# Lesson 03 — Models, Prompts & Output Parsers

> **A clean AI pipeline separates instruction design, model execution and output interpretation.**

---

# 🎯 Lesson Goal

Is lesson ke baad aap:

- PromptTemplate ka role explain kar paoge
- chat model wrapper ka input/output samajh paoge
- parser kyu chahiye samajh paoge
- string output vs structured output compare kar paoge
- DevOps RCA prompt ko reusable template me convert kar paoge

---

# PART 1 — Three Building Blocks

```text
Input Data
   ↓
Prompt Template
   ↓
Chat Model
   ↓
Output Parser
   ↓
Application Data
```

### PromptTemplate
Dynamic values ko stable instruction structure me insert karta hai.

### Model
Prompt/messages ko process karke probabilistic output generate karta hai.

### Parser
Raw model output ko application-consumable form me convert karta hai.

---

# PART 2 — Why Templates?

Without template:

```python
prompt = "Analyze " + incident + " and give RCA"
```

Problem:

- inconsistent formatting
- constraints miss ho sakte hain
- evidence boundary weak
- repeated strings

Template:

```text
ROLE: DevOps incident analyst
INCIDENT: {incident}
EVIDENCE: {evidence}
RULES: evidence-only
OUTPUT: root cause, impact, fix, confidence
```

Stable part reusable hai; runtime values change hote hain.

---

# PART 3 — PromptTemplate Practical

Conceptual current-style example:

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an evidence-first DevOps incident analyst."),
    ("human", "Incident: {incident}\nEvidence:\n{evidence}")
])

messages = prompt.invoke({
    "incident": "AKS deployment failed",
    "evidence": "NSG validation failed after Terraform apply"
})

print(messages)
```

What happened?

```text
Python dict
   ↓
Template variables resolved
   ↓
Role-aware messages created
```

---

# PART 4 — Chat Model

Example:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:3b", temperature=0)
response = llm.invoke(messages)
print(response.content)
```

Important:

- template ne inference nahi kiya
- model ne prompt build nahi kiya
- each component has one responsibility

This separation improves testing.

---

# PART 5 — Output Parser

Raw model response typically message object hota hai.

A string parser can extract text:

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
text = parser.invoke(response)
```

Mental model:

```text
AIMessage
   ↓
Parser
   ↓
String
```

---

# PART 6 — Why Parsing Matters

DevOps automation ko usually prose nahi, predictable fields chahiye:

```json
{
  "root_cause": "...",
  "impact": "...",
  "fix": "...",
  "confidence": "medium"
}
```

Application needs:

```text
field exists?
valid confidence?
unsupported impact?
citation valid?
```

Raw text me deterministic checks difficult hote hain.

---

# PART 7 — Structured Output Mental Model

```text
Prompt asks schema
      ↓
Model generates structured response
      ↓
Parser/schema validation
      ↓
Typed Python object
      ↓
Business/evidence validation
```

Very important:

```text
Schema-valid != factually true
```

Module 1 principle remains:

> Pydantic/structured parser validates shape, not truth.

---

# PART 8 — Example Typed RCA

Conceptual Pydantic schema:

```python
from pydantic import BaseModel
from typing import Literal

class RCA(BaseModel):
    root_cause: str
    impact: str
    fix: str
    confidence: Literal["low", "medium", "high"]
```

Then provider/framework structured-output support can be used where available.

Application still separately validates:

```text
root_cause supported by evidence?
impact confirmed?
fix destructive?
```

---

# PART 9 — DevOps Example

Input:

```text
incident = deployment failed

evidence =
- Terraform apply started
- NSG rule removed
- AKS subnet connectivity validation failed
```

Template should enforce:

```text
Do not invent downtime
Do not invent actor
Separate confirmed facts from inference
Use only evidence
```

Parser should ensure:

```text
root_cause present
impact present
fix present
confidence valid
```

Validator should ensure:

```text
claims supported
```

Three different responsibilities.

---

# PART 10 — Testing Each Component Separately

### Prompt test

```text
Are variables inserted correctly?
Are system rules present?
```

### Model integration test

```text
Can provider respond?
Timeout handling?
```

### Parser test

```text
Malformed JSON behavior?
Missing field behavior?
```

Separation gives easier debugging.

---

# PART 11 — Common Mistakes

### Mistake 1 — Prompt parser se truth expect karna
Parser factual validator nahi hai.

### Mistake 2 — Huge f-string everywhere
Reusable templates better.

### Mistake 3 — System/user roles merge kar dena
Stable policy aur runtime data separate rakho.

### Mistake 4 — Model response directly automation me use karna
Validate before action.

---

# PART 12 — Interview Q&A

### Q1. Why use a PromptTemplate?
To separate stable prompt structure from runtime variables and make prompts reusable, testable and consistent.

### Q2. What does an output parser do?
It converts raw model output into a more useful application representation such as text, JSON or typed data.

### Q3. Does structured output eliminate hallucination?
No. It improves shape predictability, not factual grounding.

### Q4. Why separate model and parser?
Because generation and interpretation/validation are different concerns and should fail independently.

---

# PART 13 — Revision

```text
Template = instruction construction
Model = generation
Parser = representation
Validator = trust decision
```

Do not collapse all four into one concept.

---

# PART 14 — Homework

Create a prompt with variables:

```text
{environment}
{incident}
{evidence}
```

Expected output fields:

```text
root_cause
impact
recommended_next_check
confidence
```

Then identify which validations are structural and which are factual.

---

# 🔁 Next Lesson Kyu?

Ab individual components samajh gaye. Next lesson me inhe manually invoke karne ke bajay **Runnable/chain composition** se connect karenge.
