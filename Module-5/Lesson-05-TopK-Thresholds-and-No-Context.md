# 🚩 Jai Bajrangbali!

# Lesson 05 — Top-K, Relevance Thresholds & No-Context Handling

> **Retriever ka top result hona aur actually useful result hona same baat nahi hai.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- Top-K kya hota hai
- top-ranked result kyu irrelevant ho sakta hai
- similarity score ko confidence kyu nahi samajhna chahiye
- threshold kya karta hai
- threshold tune kaise hota hai
- no-context / insufficient-context state
- false positive vs false negative retrieval
- DevOps RAG me safe fallback
- practical threshold gate
- evaluation se threshold tune karna

---

# PART 1 — Top-K Kya Hai?

Vector search usually bolta hai:

```text
Mujhe query ke sabse close K records do.
```

If:

```python
TOP_K = 3
```

retriever may return:

```text
#1 score 0.82
#2 score 0.74
#3 score 0.63
```

Important:

```text
Top-K = ranking
Top-K ≠ relevance guarantee
```

Even completely unrelated query ke liye index ko top 3 records choose karne hi padte hain.

---

# PART 2 — Unrelated Query Example

Knowledge base only DevOps docs:

```text
AKS networking
Terraform state
Pipeline failures
Production rollback
```

User asks:

```text
What is the capital of Japan?
```

Vector search still may return:

```text
#1 production-rollback.md
#2 pipeline-failure.md
#3 aks-networking.md
```

Why?

Because search answers:

```text
Which indexed vectors are nearest?
```

Not:

```text
Is any result actually relevant enough?
```

Threshold/gating solves this second question.

---

# PART 3 — Similarity Score Kya Batata Hai?

Score means metric-specific closeness.

It does NOT automatically mean:

```text
82% factually correct
82% confidence
82% chance answer true
```

Example:

```text
cosine similarity = 0.78
```

Interpretation depends on:

```text
embedding model
normalization
corpus
query style
chunking
metric
```

Therefore score thresholds cannot be copied blindly from another system.

---

# PART 4 — Relevance Threshold

Simple policy:

```python
MIN_SCORE = 0.45
accepted = [item for item in results if item["score"] >= MIN_SCORE]
```

Then:

```text
accepted results exist
    ↓
continue RAG

no accepted results
    ↓
abstain / ask for more evidence
```

---

# PART 5 — Threshold Too Low vs Too High

## Too Low

```text
0.10
```

Risk:

```text
irrelevant chunks accepted
noise sent to LLM
hallucination pressure increases
```

## Too High

```text
0.90
```

Risk:

```text
useful evidence rejected
false no-context
poor recall
```

Trade-off:

```text
Higher threshold → more precision, possibly lower recall
Lower threshold → more recall, possibly lower precision
```

---

# PART 6 — False Positive vs False Negative

## False Positive Retrieval

Irrelevant chunk accepted.

DevOps risk:

```text
Docker build guide retrieved for AKS network issue
→ model produces wrong troubleshooting path
```

## False Negative Retrieval

Relevant chunk rejected.

Risk:

```text
correct NSG runbook exists
→ threshold rejects it
→ assistant says insufficient evidence
```

In high-stakes operations, abstaining may often be safer than inventing—but excessive abstention also reduces usefulness.

---

# PART 7 — No-Context Is a Valid State

Application should represent:

```text
STATUS = NO_RELEVANT_CONTEXT
```

instead of forcing LLM.

Example:

```python
if not accepted:
    print("No sufficiently relevant knowledge was found.")
    return
```

This is stronger than asking model:

```text
Please don't hallucinate if context is weak.
```

Because host application stops generation entirely.

---

# PART 8 — Strong Gate Design

Possible decision:

```text
Retrieve top 5
   ↓
Apply ACL / metadata filters
   ↓
Check best score
   ↓
Check number of relevant chunks
   ↓
Optional rerank
   ↓
Proceed or abstain
```

Example policy:

```python
MIN_SCORE = 0.45
MIN_RESULTS = 1

accepted = [r for r in results if r["score"] >= MIN_SCORE]

if len(accepted) < MIN_RESULTS:
    return {"status": "NO_RELEVANT_CONTEXT", "results": []}
```

---

# PART 9 — Top-K Tuning

Why not always `k=20`?

Because:

```text
more chunks
→ more recall
→ but more noise/context tokens
```

Why not always `k=1`?

```text
single chunk may miss supporting evidence
single source can be incomplete
```

Typical tuning process:

```text
Test K=1,3,5,10
      ↓
Measure retrieval success
      ↓
Measure context noise
      ↓
Choose per use case
```

---

# PART 10 — DevOps Example

Question:

```text
AKS pods lost connectivity after Terraform applied an NSG change
```

Results:

```text
S1 terraform-networking.md  0.84
S2 aks-networking.md        0.78
S3 docker-build.md          0.31
```

Threshold 0.45:

```text
Accept S1, S2
Reject S3
```

Context becomes smaller and cleaner.

---

# PART 11 — Threshold Should Be Evaluated, Not Guessed

Create test set:

```text
Question
Expected relevant source
Best retrieved score
Relevant source in top-k?
Accepted by threshold?
```

Example:

```text
Q1 AKS NSG issue        expected aks-networking   0.81
Q2 Terraform state lock expected terraform-state 0.73
Q3 Capital of Japan     expected none            0.22
```

Now threshold 0.45 looks useful for this tiny corpus—but production needs more tests.

---

# PART 12 — Advanced Gate Signals

Similarity score alone may not be enough.

Additional signals:

```text
metadata status = approved
freshness
source authority
reranker score
query/source domain match
number of supporting chunks
```

Possible rule:

```text
must be approved
AND score >= threshold
AND user authorized
```

---

# PART 13 — Common Mistakes

1. Score ko confidence percentage bolna.
2. Internet se random threshold copy karna.
3. `top_k=10` ko automatically better samajhna.
4. No-context state ko failure hide karna.
5. Weak context ke baad bhi LLM se mandatory answer lena.
6. Threshold tuning without evaluation dataset.
7. Different embedding model ke score distributions ko same samajhna.

---

# PART 14 — Production Policy Example

```text
IF user unauthorized
→ DENY

ELSE retrieve top 8
→ metadata filter
→ rerank top 8
→ accept top 3 above policy threshold

IF zero accepted
→ NO_RELEVANT_CONTEXT

ELSE
→ build context
→ call LLM
```

---

# PART 15 — Interview Corner

### Q1. What is Top-K retrieval?

Returning the K highest-ranked candidates according to the retrieval metric.

### Q2. Why can the top result still be irrelevant?

Because ranking is relative to the indexed corpus and does not prove an absolute relevance level.

### Q3. What is a relevance threshold?

A policy that rejects candidates whose retrieval score does not meet a tuned minimum criterion.

### Q4. Is similarity score an answer-confidence score?

No. It measures vector closeness under a specific embedding/search setup.

### Q5. Why is no-context handling important?

It prevents the system from forcing generation when retrieval provides insufficient evidence.

---

# PART 16 — Revision

```text
Top-K → candidate count
Score → retrieval similarity
Threshold → quality gate
No-context → safe abstention state

Top result ≠ relevant result
Similarity ≠ truth confidence
Threshold must be evaluated
```

---

# PART 17 — Homework

1. Create 5 queries: 3 relevant, 2 unrelated.
2. Record top-3 scores for each.
3. Try thresholds 0.3, 0.5, 0.7.
4. Note false positives/false negatives.
5. Decide a temporary threshold and explain why.
6. Add explicit `NO_RELEVANT_CONTEXT` state to a RAG script.

---

# 🔗 Why Lesson 6 Next?

Ab relevant evidence filter ho gaya. Next production question:

```text
User kaise verify kare ki answer kis evidence se aaya?
```

Next lesson me hum **citations, source maps aur traceability** build karenge.
