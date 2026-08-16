# Lesson 01 — RAG Fundamentals

> **RAG ka simple goal: LLM ko answer dene se pehle relevant external knowledge dena.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap clearly samjhoge:

- RAG kya hai
- RAG kyu chahiye
- RAG vs normal LLM call
- RAG vs fine-tuning
- retrieval ka exact role
- DevOps me RAG kaha useful hai
- RAG kya solve karta hai aur kya solve nahi karta

---

## English Definition

**Retrieval-Augmented Generation (RAG)** is an architecture in which an application retrieves relevant external information at query time and provides that information to a language model as context before generating an answer.

---

# PART 1 — Problem First

User asks:

```text
What is the rollback procedure for our production AKS deployment?
```

Generic LLM ke paas aapke company ka private runbook nahi hai.

Without RAG:

```text
Question
   ↓
LLM internal knowledge
   ↓
Generic answer
```

Potential problem:

- internal procedure unknown
- wrong commands suggest ho sakte hain
- old assumptions use ho sakti hain
- organization-specific approval steps miss ho sakte hain

With RAG:

```text
Question
   ↓
Search internal runbooks
   ↓
Retrieve rollback section
   ↓
Give section to LLM
   ↓
Generate grounded answer
```

---

# PART 2 — RAG Formula

```text
R = Retrieval
A = Augmented
G = Generation
```

Meaning:

1. **Retrieval** → relevant information find karo.
2. **Augmentation** → retrieved information prompt me add karo.
3. **Generation** → LLM us context ke basis par final response generate kare.

---

# PART 3 — RAG vs Normal LLM

## Normal LLM

```text
User Question
     ↓
LLM
     ↓
Answer
```

## RAG

```text
User Question
     ↓
Retriever
     ↓
Relevant Chunks
     ↓
Context Builder
     ↓
LLM
     ↓
Grounded Answer
```

Important difference:

> RAG me model ke paas answer dene se pehle external evidence aata hai.

---

# PART 4 — RAG vs Fine-Tuning

Common confusion:

```text
RAG = model training?
```

No.

### RAG

- runtime retrieval
- documents easily update ho sakte hain
- sources traceable ho sakte hain
- model weights unchanged

### Fine-Tuning

- model behavior/weights adapt hote hain
- training dataset chahiye
- knowledge freshness problem still exist kar sakti hai
- exact document citation naturally guarantee nahi hota

Mental model:

```text
RAG = Give the model a reference book before answering
Fine-tuning = Teach the model a pattern/style through training
```

---

# PART 5 — DevOps Use Cases

RAG can help with:

```text
Incident Question
   → historical RCA retrieval

AKS Error
   → Kubernetes runbook retrieval

Terraform Failure
   → internal IaC troubleshooting docs

Pipeline Problem
   → deployment SOP + known issue docs

On-call Question
   → relevant operational procedure
```

Example:

```text
Question:
"Pods lost DB connectivity after network change"

Retriever finds:
1. aks-networking.md
2. sql-private-endpoint.md
3. previous-incident-2026-04.md

LLM receives those chunks and explains likely investigation steps.
```

---

# PART 6 — What RAG Does NOT Automatically Fix

RAG does not guarantee truth.

Bad retrieval can still cause bad answer.

```text
Wrong Chunk
   ↓
Wrong Context
   ↓
Confident LLM
   ↓
Wrong Answer
```

Other failures:

- stale documents
- insecure retrieval
- wrong tenant data
- irrelevant top-k
- missing source traceability
- LLM ignores evidence
- answer invents unsupported detail

So production RAG needs:

```text
Good Retrieval
+ Good Context
+ Good Prompt
+ Guardrails
+ Evaluation
```

---

# PART 7 — First DevOps Mental Model

```text
User
 ↓
"Why does AKS deployment fail after NSG change?"
 ↓
Embedding / Retrieval
 ↓
Relevant chunks
 ↓
Context:
- NSG rule removed
- subnet validation failed
- Terraform Apply failed
 ↓
LLM
 ↓
Evidence-grounded RCA explanation
```

---

## Common Mistakes

### Mistake 1
"RAG removes hallucination completely."

No. It reduces risk when retrieval/context/guardrails are good.

### Mistake 2
"RAG means vector database."

Vector DB is one retrieval mechanism. RAG is the full retrieve + context + generation architecture.

### Mistake 3
"Retrieved chunk is automatically true."

Retrieved content can be stale, wrong, malicious or unauthorized.

---

## Interview Corner

**Q: What problem does RAG solve?**

It allows an LLM application to use external, current or private knowledge at runtime without retraining the model.

**Q: Does RAG update model weights?**

No. It augments the prompt context at runtime.

**Q: Is vector search mandatory for RAG?**

No. Retrieval can use vector, keyword, hybrid, database queries, APIs or other search mechanisms.

---

## Revision Cheat Sheet

```text
RAG
= Retrieve relevant knowledge
+ Add knowledge to prompt
+ Generate answer from that context
```

---

## Homework

Explain in your own words:

1. Why can a generic LLM not reliably answer an internal HCL/project runbook question?
2. RAG vs fine-tuning kya difference hai?
3. Wrong retrieval ka final answer par kya impact hoga?

---

## Next Lesson Kyu?

RAG ka idea samajh gaya. Ab hume exact architecture samajhna hai:

```text
Documents kab index hote hain?
Query kab embed hoti hai?
Retrieval kab hota hai?
LLM call kis stage par hota hai?
```

That is Lesson 02 — **RAG Architecture & Data Flow**.
