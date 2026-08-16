# Lesson 10 — RAG Evaluation

> **Ek demo question ka sahi answer aana proof nahi hai ki RAG system reliable hai.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- retrieval evaluation vs generation evaluation
- golden test set
- hit rate / recall intuition
- precision intuition
- groundedness / faithfulness
- answer relevance
- citation correctness
- regression testing
- production feedback loop

---

## English Definition

**RAG evaluation** measures both whether the retriever finds the right evidence and whether the generator produces a relevant, evidence-supported answer from that evidence.

---

# PART 1 — Evaluate Two Systems, Not One

RAG has at least two quality layers:

```text
Retriever Quality
      ↓
Context Quality
      ↓
Generator Quality
```

If answer wrong hai, first determine:

```text
Did we retrieve the right evidence?
```

If no → retrieval problem.

If yes but answer wrong → prompt/generation/validation problem.

---

# PART 2 — Golden Test Dataset

Create controlled questions:

```text
Question
Expected Source(s)
Expected Key Fact(s)
Expected Abstention?
```

Example:

```text
Q: What caused the AKS subnet connectivity incident?
Expected Sources: incident-2026-08.md, aks-networking.md
Expected Fact: required NSG rule removal preceded connectivity validation failure
```

A useful test set includes:

- easy questions
- paraphrases
- vague questions
- exact errors
- no-answer questions
- conflicting-doc questions
- security-sensitive questions

---

# PART 3 — Retrieval Metrics Intuition

## Hit@K

Was at least one expected relevant document/chunk present in top-k?

```text
Expected source found in top 3? → yes/no
```

## Recall intuition

Of all relevant evidence we expected, how much did retriever find?

## Precision intuition

Of retrieved chunks, how many were actually relevant?

Tradeoff:

```text
Higher k → often higher recall, lower precision
Lower k → often higher precision, lower recall
```

---

# PART 4 — Generation Metrics

### Groundedness / Faithfulness

Are factual claims supported by retrieved evidence?

### Answer Relevance

Does answer actually address user question?

### Completeness

Did answer include important supported facts?

### Citation Correctness

Do citation IDs exist and support associated claims?

### Abstention Correctness

When evidence absent, did system say it was insufficient rather than inventing?

---

# PART 5 — Manual Evaluation Sheet

```text
Question:
Expected Source:
Retrieved Top-K:
Correct source retrieved? Y/N
Irrelevant chunks count:
Answer correct? Y/N
Unsupported claims? Y/N
Citation valid? Y/N
Should abstain? Y/N
Did abstain? Y/N
Notes:
```

For a learning project this is enough to develop evaluation mindset.

---

# PART 6 — DevOps Test Examples

### Test 1 — Semantic

```text
Pods cannot reach database after network change
```

Expected:

- AKS networking
- SQL/private endpoint docs

### Test 2 — Exact Error

```text
AuthorizationFailed subnet join action
```

Expected:

- RBAC/network permission doc

### Test 3 — No Answer

```text
Who approved CAB ticket CHG999999?
```

If source not indexed:

```text
must abstain
```

### Test 4 — Stale Document

Ensure deprecated runbook is not ranked above active runbook.

---

# PART 7 — Regression Testing

RAG changes frequently:

```text
chunk size changed
embedding model changed
metadata filter changed
query rewrite changed
threshold changed
prompt changed
```

Any change can improve one query and break another.

So maintain a stable test set and compare before/after.

```text
Version A → 82% retrieval hit@3
Version B → 91% retrieval hit@3
```

Also inspect safety failures, not only average score.

---

# PART 8 — Evaluation by Environment/Domain

Overall score can hide weaknesses.

Break down:

```text
AKS queries
Terraform queries
Pipeline queries
Networking queries
Security queries
No-answer queries
```

This tells you where retrieval needs improvement.

---

# PART 9 — User Feedback Is Useful but Not Enough

Signals:

- thumbs up/down
- user opens cited source
- repeated query
- escalated ticket
- corrected answer

But user feedback can be noisy. Combine it with controlled evaluation.

---

# PART 10 — RAG Debugging Checklist

When answer wrong:

```text
1. Was correct source indexed?
2. Was correct chunk created?
3. Was query represented correctly?
4. Did retrieval return it?
5. Did threshold remove it?
6. Did context builder include it?
7. Did prompt force grounding?
8. Did model use it correctly?
9. Were claims/citations validated?
```

---

## Common Mistakes

- evaluate only final prose
- no golden questions
- no no-answer cases
- changing embedding model without regression test
- only average metric, no domain breakdown
- model judging itself without any human/ground-truth checks

---

## Interview Corner

**Q: How do you evaluate a RAG system?**

Evaluate retrieval and generation separately using a labeled test set, measuring relevant evidence retrieval, answer relevance, groundedness, citation correctness and abstention behavior.

**Q: Why is regression testing important in RAG?**

Because changes to chunking, embeddings, retrieval, thresholds or prompts can silently improve some queries while degrading others.

---

## Revision

```text
RAG Evaluation
= Retrieval Quality
+ Generation Quality
+ Citation Quality
+ Abstention Quality
+ Regression Testing
```

---

## Homework

Create a 15-question evaluation set:

- 4 AKS
- 3 Terraform
- 3 pipeline
- 2 exact-error
- 3 no-answer

---

## Next Lesson Kyu?

Lab system ka quality measure karna samajh gaya. Ab production me freshness, RBAC, secrets, monitoring, scaling aur cost handle karna hai.

Next: **Production RAG for DevOps**.
