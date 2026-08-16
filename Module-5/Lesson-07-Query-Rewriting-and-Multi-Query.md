# 🚩 Jai Bajrangbali!

# Lesson 07 — Query Rewriting & Multi-Query Retrieval

> **User ki language aur knowledge-base ki language same nahi hoti. Query transformation retrieval ko improve kar sakta hai — but original intent ko change nahi karna chahiye.**

---

# 🎯 Lesson Goal

Is lesson me hum cover karenge:

- vague query problem
- query normalization
- safe query rewriting
- query expansion
- multi-query retrieval
- candidate merging and deduplication
- intent drift risk
- LLM-based vs deterministic rewriting
- DevOps examples
- evaluation strategy

---

# PART 1 — User Query Often Messy Hoti Hai

User asks:

```text
prod broken after tf change
```

Knowledge base may contain:

```text
Terraform networking changes can modify AKS subnet NSG rules.
```

Semantic search may still work, but better normalized query ho sakti hai:

```text
production deployment failure after Terraform networking change
```

---

# PART 2 — English Definition

**Query rewriting** transforms a user query into a clearer retrieval-oriented form while preserving the original intent.

**Multi-query retrieval** searches using multiple intent-preserving variants and merges the resulting candidates to improve recall.

---

# PART 3 — Deterministic Normalization

Before LLM rewrite, simple cleanup:

```python
query = "  PROD broken after TF change  "
query = " ".join(query.lower().split())
```

Output:

```text
prod broken after tf change
```

You can also expand known abbreviations with controlled mapping:

```python
ALIASES = {
    "tf": "terraform",
    "aks": "azure kubernetes service",
    "nsg": "network security group",
}
```

Controlled expansion is predictable.

---

# PART 4 — LLM Query Rewrite

Prompt:

```text
Rewrite the following DevOps question for document retrieval.
Preserve meaning.
Do not add facts not present in the query.
Return one concise search query only.

USER QUERY:
prod broken after tf change
```

Possible output:

```text
production deployment failure after Terraform change
```

Risk:

Model could add:

```text
NSG rule removal
```

when user never said NSG. That is **intent drift / evidence injection**.

---

# PART 5 — Safe Rewrite Contract

Rules:

```text
1. Preserve original user intent.
2. Expand abbreviations only when unambiguous.
3. Do not invent suspected root cause.
4. Do not add environment, service, date or impact not supplied.
5. Return retrieval text only.
```

---

# PART 6 — Multi-Query Retrieval

Original:

```text
AKS network issue after Terraform change
```

Variants:

```text
Q1: AKS network issue after Terraform change
Q2: Kubernetes subnet connectivity failure after Terraform networking update
Q3: Terraform NSG or route change affecting AKS connectivity
```

Then:

```text
Search Q1
Search Q2
Search Q3
    ↓
Merge candidates
    ↓
Deduplicate
    ↓
Keep strongest score per chunk
```

---

# PART 7 — Candidate Merge Example

Results:

```text
Q1 → A 0.82, B 0.74
Q2 → B 0.80, C 0.71
Q3 → A 0.84, D 0.69
```

Merged:

```text
A 0.84
B 0.80
C 0.71
D 0.69
```

Pseudo-code:

```python
best = {}

for query in queries:
    for item in retrieve(query):
        cid = item["chunk_id"]
        if cid not in best or item["score"] > best[cid]["score"]:
            best[cid] = item

merged = sorted(best.values(), key=lambda x: x["score"], reverse=True)
```

---

# PART 8 — Why Multi-Query Helps

Single query may emphasize one wording.

Multi-query gives alternative semantic angles:

```text
network issue
connectivity failure
subnet communication
```

This can improve recall when docs use different vocabulary.

But more queries mean:

```text
more embedding/search work
more candidates
more latency
more noise
```

So evaluate before using aggressively.

---

# PART 9 — Query Rewrite vs HyDE Concept

Advanced retrieval sometimes generates a hypothetical answer/document and embeds it. This is often called HyDE-like retrieval.

For our course:

```text
Query Rewrite = safer starting point
HyDE = advanced technique, higher risk of injected assumptions
```

In DevOps incident systems, preserve evidence boundaries carefully.

---

# PART 10 — Original Query Must Be Preserved

Even if rewritten query used for retrieval:

```text
Original user query must remain authoritative for answer intent.
```

Architecture:

```text
Original Question
   ├── used for final prompt
   └── transformed copies used only for retrieval
```

Do not replace user intent with model rewrite.

---

# PART 11 — DevOps Example

User:

```text
pods cant talk after infra deployment
```

Safe variants:

```text
pods cannot communicate after infrastructure deployment
Kubernetes workload connectivity failure after infrastructure change
AKS pod network connectivity issue after Terraform deployment
```

Unsafe variant:

```text
AKS pods failed because the NSG rule was deleted
```

Why unsafe?

Because it invents root cause.

---

# PART 12 — Evaluation

Test:

```text
Original query
Expected source
Single-query retrieved?
Rewrite retrieved?
Multi-query retrieved?
Noise increased?
Intent preserved?
```

Measure both:

```text
recall gain
precision/noise cost
```

---

# PART 13 — Common Mistakes

1. Rewrite ko factual enrichment banana.
2. Original query lose kar dena.
3. Multi-query results duplicate context me bhejna.
4. Unlimited variants generate karna.
5. Query rewrite output blindly trust karna.
6. Abbreviation expansion without domain certainty.
7. Retrieval improvement assume karna without evaluation.

---

# PART 14 — Interview Corner

### Q1. Why rewrite queries in RAG?

To improve retrieval when user phrasing differs from document terminology.

### Q2. What is the main risk?

Intent drift — rewritten query adds or changes meaning.

### Q3. Why preserve original query?

Because the original user request defines the actual task; transformed queries are only retrieval helpers.

### Q4. What is multi-query retrieval?

Search multiple intent-preserving variants, merge candidates, deduplicate, and rank them.

### Q5. Does multi-query always improve RAG?

No. It can increase recall but also latency and noise.

---

# PART 15 — Revision

```text
Original Query
  ↓
Normalize / Rewrite
  ↓
Generate Few Variants
  ↓
Retrieve per Variant
  ↓
Merge + Deduplicate
  ↓
Rank
  ↓
Context

Original question stays authoritative.
```

---

# PART 16 — Homework

1. Write safe rewrites for 5 short DevOps questions.
2. Identify one rewrite that introduces false assumptions.
3. Implement candidate merge by `chunk_id`.
4. Compare single-query vs 3-query retrieval on 10 questions.
5. Record whether recall improved and noise increased.

---

# 🔗 Why Lesson 8 Next?

Multi-query can give us more candidates. But more candidates means ranking becomes even more important.

Next lesson:

```text
Retrieve broad candidates
   ↓
Hybrid signals / reranker
   ↓
Best final evidence
```

Hum **reranking aur hybrid search** samjhenge.
