# 🚩 Jai Bajrangbali!

# Lesson 08 — Reranking & Hybrid Search

> **Retriever candidates dhoondhta hai; reranker decide karta hai ki final context me sabse useful evidence kaunsa jaana chahiye.**

---

# 🎯 Lesson Goal

Is lesson me hum cover karenge:

- first-stage retrieval vs second-stage reranking
- vector search ki limitations
- keyword/BM25 style exact-match value
- hybrid search mental model
- reranker kya karta hai
- candidate count vs final context count
- DevOps exact identifiers ka importance
- fusion strategies
- latency/cost trade-offs
- practical ranking pipeline

---

# PART 1 — Vector Search Kab Weak Ho Sakta Hai?

Vector search semantic meaning ke liye strong hai.

Query:

```text
pods cannot reach database after network change
```

Semantic search useful docs find kar sakta hai.

But DevOps me exact identifiers bhi bahut important hote hain:

```text
aks-subnet-allow
Error 403
TF_LOCK_ID_29A
CrashLoopBackOff
10.20.4.0/24
```

Semantic vector sometimes exact token importance ko dilute kar sakta hai.

---

# PART 2 — Keyword Search Strength

Keyword/BM25-like retrieval exact terms ko strong weight de sakta hai.

Query:

```text
aks-subnet-allow
```

Exact-match search can immediately surface:

```text
Terraform change removed aks-subnet-allow.
```

So:

```text
Vector search → semantic similarity
Keyword search → lexical/exact matching
```

Both have value.

---

# PART 3 — Hybrid Search

**Hybrid search** combines semantic/vector retrieval with lexical/keyword retrieval.

Mental model:

```text
User Query
   ├── Vector Search
   └── Keyword Search
          ↓
     Merge Results
          ↓
       Rerank
          ↓
     Final Evidence
```

---

# PART 4 — Why Hybrid Is Useful in DevOps

Query:

```text
Deployment failed with aks-subnet-allow missing
```

Vector search finds:

```text
AKS subnet network security guidance
```

Keyword search finds:

```text
incident record containing exact aks-subnet-allow string
```

Together they can provide both:

```text
specific incident evidence + general technical context
```

---

# PART 5 — What Is Reranking?

First-stage retriever optimizes speed and recall.

Example:

```text
Retrieve top 20 candidates quickly
```

Reranker evaluates candidates more deeply and reorders them:

```text
20 candidates
   ↓
Reranker
   ↓
Best 3-5 evidence chunks
```

English definition:

**Reranking is a second-stage retrieval process that re-scores an initial candidate set using a more precise relevance model or scoring method.**

---

# PART 6 — Bi-Encoder vs Cross-Encoder Mental Model

Embedding retrieval often behaves like:

```text
Query → vector
Document → vector
Compare vectors
```

Fast because document vectors can be precomputed.

Cross-encoder-like reranker:

```text
(Query + Candidate Chunk) together
      ↓
Relevance Model
      ↓
Single relevance score
```

Usually more expensive but potentially more precise.

---

# PART 7 — Candidate Count vs Context Count

Do not confuse:

```text
RETRIEVAL_K = 20
CONTEXT_K = 4
```

Possible pipeline:

```text
retrieve 20 broad candidates
→ dedupe/filter
→ rerank 10
→ use top 4 in prompt
```

This gives recall without flooding LLM context.

---

# PART 8 — Simple Hybrid Fusion

Suppose vector rank:

```text
A rank 1
B rank 2
C rank 3
```

Keyword rank:

```text
C rank 1
A rank 2
D rank 3
```

One simple fusion idea is Reciprocal Rank Fusion (RRF):

```text
score(doc) += 1 / (k + rank)
```

You do not need deep math initially; concept is:

```text
documents appearing high in multiple rankings receive stronger combined priority
```

---

# PART 9 — Simple Practical Pseudo-Code

```python
vector_results = vector_search(query, k=10)
keyword_results = keyword_search(query, k=10)

merged = fuse(vector_results, keyword_results)
reranked = rerank(query, merged[:10])
final_context = reranked[:4]
```

Each stage can be measured independently.

---

# PART 10 — Metadata + Hybrid Search

Production pipeline may be:

```text
Authorization Filter
      ↓
Metadata Filter
      ↓
Vector + Keyword Retrieval
      ↓
Fusion
      ↓
Reranking
      ↓
Threshold
      ↓
Context
```

Important:

> Security filtering must not be postponed until after LLM generation.

---

# PART 11 — DevOps Example

Question:

```text
Why did pipeline run 8452 fail after aks-subnet-allow changed?
```

Keyword signals:

```text
8452
aks-subnet-allow
```

Semantic signals:

```text
pipeline failure
AKS subnet connectivity
networking change
```

Hybrid retrieval can exploit both.

---

# PART 12 — Reranking Does Not Fix Missing Knowledge

If correct document was never indexed:

```text
reranker cannot invent it
```

If first-stage retrieval never includes correct chunk:

```text
reranker cannot rank unseen candidate
```

So:

```text
Good Indexing
+ Good First-Stage Recall
+ Good Reranking
```

all matter.

---

# PART 13 — Latency & Cost Trade-Off

Pipeline complexity increases:

```text
vector search
+ keyword search
+ reranker
+ LLM generation
```

Measure:

```text
retrieval latency
fusion latency
rerank latency
LLM latency
```

Do not add reranker because it sounds advanced. Add it if evaluation shows benefit.

---

# PART 14 — Common Mistakes

1. Vector search ko universally superior samajhna.
2. Exact error codes/IDs ignore karna.
3. Retrieve top 50 and all context me bhejna.
4. Reranker ko security filter samajhna.
5. Reranking without baseline evaluation.
6. Correct source absent hone par reranker se miracle expect karna.
7. Different scoring scales ko directly add kar dena without normalization/fusion strategy.

---

# PART 15 — Interview Corner

### Q1. What is hybrid search?

Combining semantic/vector retrieval with lexical/keyword retrieval to use both meaning and exact-term signals.

### Q2. Why is hybrid search useful in DevOps?

DevOps queries often contain exact identifiers such as error codes, resource names and rule names alongside semantic intent.

### Q3. What is reranking?

A second-stage process that more precisely re-scores an initial candidate set before final context selection.

### Q4. Why retrieve more candidates than you send to the LLM?

To improve recall first, then use filtering/reranking to keep only the strongest evidence within context budget.

### Q5. Can reranking recover a document not retrieved initially?

No. It can only reorder the candidate set it receives.

---

# PART 16 — Revision

```text
Vector → meaning
Keyword → exact words/IDs
Hybrid → combine both
Rerank → improve final ordering

Retrieve broad
→ Filter
→ Rerank
→ Send narrow context
```

---

# PART 17 — Homework

1. List 10 DevOps terms where exact keyword matching matters.
2. Create vector and keyword result lists and manually fuse them.
3. Explain why `Error 403` may benefit from lexical search.
4. Test retrieval_k=10 and context_k=3.
5. Record whether reranking improves expected-source position.

---

# 🔗 Why Lesson 9 Next?

Ab retrieval pipeline kaafi strong hai. But even strong retrieval ke baad generation layer unsafe ho sakti hai.

Next lesson me hum specifically **RAG hallucinations, prompt injection, unsupported claims aur guardrails** ko deep dive karenge.
