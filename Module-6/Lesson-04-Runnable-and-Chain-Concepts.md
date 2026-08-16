# 🚩 Jai Bajrangbali!

# Lesson 04 — Runnable & Chain Concepts

> **Runnable composition ka goal hai AI workflow ko pipeline ki tarah readable, reusable aur testable banana.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- Runnable kya hota hai
- chain kya hoti hai
- pipe composition ka mental model
- input/output contract importance
- branching, mapping and transformation concepts
- DevOps pipeline analogy
- chain fail hone par debugging kaise karein

---

# PART 1 — English Definition

A **Runnable** is an executable component with a defined input/output behavior that can be invoked independently or composed with other runnables into a workflow.

A **chain** is a composed sequence or graph of such components where the output of one step feeds another.

---

# PART 2 — Simplest Mental Model

```text
Input
 ↓
Step A
 ↓
Step B
 ↓
Step C
 ↓
Output
```

DevOps analogy:

```text
Source
 ↓
Build
 ↓
Test
 ↓
Scan
 ↓
Deploy
```

AI chain:

```text
Question
 ↓
Prompt
 ↓
Model
 ↓
Parser
 ↓
Answer
```

---

# PART 3 — Pipe Composition

Conceptual example:

```python
chain = prompt | llm | parser
result = chain.invoke({"incident": "AKS deployment failed"})
```

Read left-to-right:

```text
input dict
→ prompt formatting
→ model execution
→ parser
→ final value
```

This is not magic syntax. It is component composition.

---

# PART 4 — Contract Thinking

Suppose:

```text
Prompt expects: dict
Prompt returns: messages
Model expects: messages
Model returns: AIMessage
Parser expects: AIMessage
Parser returns: string
```

Then flow works.

If one step outputs wrong type:

```text
Contract mismatch
```

Exactly CI/CD artifact mismatch jaisa.

---

# PART 5 — Why Composition Helps

### Readability

```python
chain = prompt | llm | parser
```

workflow clearly visible.

### Reuse
Same parser with multiple prompts.

### Testing
Prompt and parser individually testable.

### Swapping
Model wrapper replace without rewriting every step.

### Observability
Per-step tracing attach karna easier.

---

# PART 6 — Transformations

Often input directly next component ke format me nahi hota.

Example input:

```python
{
  "question": "Why deployment failed?",
  "documents": [...]
}
```

Prompt may need:

```python
{
  "question": "...",
  "context": "formatted source text"
}
```

A transformation step does:

```text
documents → formatted context
```

This deterministic Python logic should stay deterministic.

---

# PART 7 — Mapping / Parallel Concept

Sometimes same input se multiple values derive karni hoti hain:

```text
Question
 ├─→ Retriever → Context
 └─→ Pass-through → Original Question

Context + Question
      ↓
Prompt
```

RAG chain ka common shape yehi hai.

---

# PART 8 — Branching Concept

Example:

```text
Retrieve
 ↓
Relevant context found?
 ├─ No → Return INSUFFICIENT_EVIDENCE
 └─ Yes → Call LLM
```

Important:

> Har branch LLM decide kare zaroori nahi.

Threshold-based condition deterministic application code se decide ho sakta hai.

---

# PART 9 — DevOps Workflow Example

Incident input:

```python
{
  "environment": "production",
  "incident": "AKS deployment failure"
}
```

Flow:

```text
Validate environment
      ↓
Retrieve runbook
      ↓
Fetch pipeline evidence
      ↓
Combine context
      ↓
RCA prompt
      ↓
LLM
      ↓
Parser
      ↓
Evidence validator
```

Do not make everything one giant prompt.

---

# PART 10 — Error Localization

Manual monolithic function fails:

```text
"AI app failed"
```

Composed workflow can identify:

```text
Retriever failed
Model timeout
Parser failed
Validation failed
```

Production reliability ke liye stage identity important hai.

---

# PART 11 — Idempotency Thinking

Some steps safe to retry:

```text
read-only retrieval
embedding
model inference (depending on cost/idempotency expectations)
```

Some steps dangerous:

```text
kubectl delete
terraform apply
restart production service
```

Chain orchestration does not automatically make retries safe.

---

# PART 12 — Common Mistakes

### Giant chain
20 opaque steps ek line me compose karke debugging impossible banana.

### Hidden side effects
Runnable ke andar production mutation hide karna.

### Type assumptions
Har step ka output manually inspect nahi karna.

### LLM for deterministic transformation
Simple string formatting/model routing LLM ko dena unnecessary.

---

# PART 13 — Practical

Basic chain:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_template(
    "Explain this DevOps incident in 3 bullets: {incident}"
)
llm = ChatOllama(model="qwen2.5:3b", temperature=0)
parser = StrOutputParser()

chain = prompt | llm | parser

print(chain.invoke({"incident": "AKS deployment failed after NSG change"}))
```

Expected mental trace:

```text
dict
→ PromptValue
→ AIMessage
→ str
```

---

# PART 14 — Interview Q&A

### Q1. What is runnable composition?
It is the composition of executable components with compatible input/output contracts into a reusable workflow.

### Q2. Why is contract visibility important?
Because most orchestration bugs occur at boundaries where one step produces data another step does not expect.

### Q3. Should all branching be delegated to an LLM?
No. Deterministic conditions such as validation, thresholds and authorization should usually remain application-controlled.

### Q4. What is the risk of retrying a chain?
If any step has side effects, retry may duplicate or repeat destructive actions.

---

# PART 15 — Revision

```text
Runnable = executable component
Chain = composed flow
Pipe = output → next input
Transform = reshape data
Branch = choose path
Validator = trust gate
```

---

# PART 16 — Homework

Design chain for:

```text
Terraform plan text
→ extract networking changes
→ build review prompt
→ LLM risk review
→ parser
→ policy validation
```

Identify which stages should be deterministic and which should be LLM-based.

---

# 🔁 Next Lesson Kyu?

Ab execution composition clear hai. Next hum ingestion side ko framework components me convert karenge:

```text
Document Loader → Text Splitter
```

Ye RAG orchestration ka data-entry point hai.
