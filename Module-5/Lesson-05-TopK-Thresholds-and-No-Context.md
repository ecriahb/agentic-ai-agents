# Lesson 05 — Top-K, Thresholds & No-Context Handling

> **Retriever kuch return kar de, iska matlab ye nahi ki result actually relevant hai.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- top-k kya hota hai
- too small vs too large k
- similarity score / distance interpretation
- threshold concept
- no-context guardrail
- weak retrieval detection
- application policy

---

## English Definition

**Top-k retrieval** returns the k highest-ranked candidates, while a **relevance threshold** rejects candidates that do not meet a minimum quality criterion.

---

# PART 1 — Top-K

```text
Top-K = how many candidate chunks should retrieval return?
```

Example:

```text
k = 3
```

Retriever returns three highest-ranked chunks.

But:

```text
Top result can still be irrelevant.
```

Ranking is relative to available data.

---

# PART 2 — Too Small vs Too Large

### k too small

```text
Only 1 chunk
```

Risk:

- supporting evidence miss
- answer incomplete

### k too large

```text
20 chunks
```

Risk:

- noisy context
- irrelevant docs
- duplicate content
- higher token cost

So top-k is an evaluation/tuning parameter, not magic constant.

---

# PART 3 — Score vs Distance

Depending on index/API, result may expose:

```text
similarity score: larger can mean better
```

or

```text
distance: smaller can mean better
```

Never assume all libraries use same interpretation.

Application should normalize/understand its chosen metric.

---

# PART 4 — Why Threshold?

Suppose query:

```text
How to renew production TLS certificate?
```

Knowledge base has no certificate document.

Vector search still returns nearest available chunks:

```text
0.32 docker-build.md
0.29 aks-networking.md
0.25 terraform-state.md
```

If application blindly sends them to LLM, model may produce nonsense.

Threshold policy:

```text
if best_score < MIN_SCORE:
    return NO_CONTEXT
```

---

# PART 5 — No-Context Guardrail

```python
MIN_SCORE = 0.55

if not results or results[0]["score"] < MIN_SCORE:
    return {
        "status": "insufficient_context",
        "answer": "I could not find sufficiently relevant evidence in the knowledge base."
    }
```

Important:

Threshold value should come from testing, not guesswork.

---

# PART 6 — DevOps Example

Question:

```text
Why did Terraform Apply fail yesterday?
```

Case A:

```text
S1 0.86 pipeline-failure.md
S2 0.82 terraform-networking.md
```

Strong retrieval.

Case B:

```text
S1 0.34 docker-build.md
S2 0.31 cpu-alert.md
```

Likely no-context case.

---

# PART 7 — Multiple Policies

Production system can use:

```text
minimum best score
minimum number of strong chunks
source allowlist
metadata match
freshness requirement
```

Example:

```text
Production rollback question
→ only production-approved docs
→ status=active
→ version=current
→ score above threshold
```

---

# PART 8 — Threshold Is Not Universal

Different embedding models/metrics/data produce different score distributions.

So avoid:

```text
0.7 is always good
```

Instead:

1. build test questions
2. label relevant chunks
3. inspect score distributions
4. choose threshold
5. evaluate false accepts/rejects

---

## Common Mistakes

- top-k only, no quality check
- threshold copied from internet
- metric direction misunderstood
- weak chunks still sent to LLM
- no safe "not found" path

---

## Interview Corner

**Q: Why can top-1 be wrong even if it is the nearest result?**

Because nearest is only relative to indexed candidates; the knowledge base may contain no truly relevant content.

**Q: How do you handle no relevant context in RAG?**

Use retrieval-quality checks and return an explicit insufficient-context response instead of forcing generation.

---

## Revision

```text
Top-K = quantity
Threshold = quality gate
No-context = safe fallback
```

---

## Homework

Create a test table with 10 DevOps questions:

```text
Question | Expected Source | Best Score | Relevant? | Threshold Decision
```

---

## Next Lesson Kyu?

Relevant context mil gaya. Ab user ko kaise prove karenge ki answer kis source se aaya?

Next: **Citations & Source Traceability**.
