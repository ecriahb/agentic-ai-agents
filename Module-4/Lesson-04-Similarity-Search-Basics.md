# 🚩 Lesson 04 — Similarity Search Basics

> **Embeddings bana lena enough nahi; ab query vector ko stored vectors se compare karke relevant knowledge rank karna hai.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- similarity search kya hai
- nearest neighbors kya hote hain
- Top-K retrieval
- semantic search ka full query flow
- brute-force comparison ka idea
- score vs distance confusion
- DevOps retrieval example
- manual Python search practical

---

# PART 1 — Problem

Stored docs:

```text
D1: AKS subnet NSG blocked application traffic
D2: Terraform state lock prevented apply
D3: Docker build disk space exhausted
D4: Kubernetes workload lost database connectivity
```

Query:

```text
Pods cannot connect after network security change
```

Question:

```text
Which documents are most related?
```

Answer ke liye:

```text
Query → embedding
Docs  → embeddings
       ↓
Compare
       ↓
Rank
       ↓
Top results
```

---

# PART 2 — English Definition

> Similarity search retrieves items whose vector representations are closest or most similar to a query vector according to a chosen similarity or distance metric.

Hinglish:

**Query ka vector banao, stored vectors se compare karo, sabse relevant/nearest results return karo.**

---

# PART 3 — Nearest Neighbor Mental Model

Imagine vector map:

```text
                 D3 Docker ●

Query ●
     D1 ●
       D4 ●

                              D2 Terraform state ●
```

Query ke nearest vectors likely D1/D4 honge.

Actual vector space 2D nahi hota; diagram intuition ke liye hai.

---

# PART 4 — Top-K Kya Hai?

`K` = kitne best results chahiye.

```text
Top-K = 1 → best one result
Top-K = 3 → best three results
Top-K = 5 → best five results
```

Example:

```text
Query: AKS connectivity issue

#1 aks-networking.md      0.89
#2 sql-private-link.md    0.81
#3 pipeline-failure.md    0.72
```

Higher score yahan illustrative similarity hai. Different databases/APIs score/distance differently expose kar sakte hain.

---

# PART 5 — Score vs Distance

Very important confusion:

Some systems return:

```text
higher similarity = better
```

Others return:

```text
lower distance = better
```

Never assume blindly.

Always check:

```text
metric
score semantics
normalization
library documentation
```

Example:

```text
Cosine similarity: 0.92 → very similar
L2 distance:       0.12 → close
```

Both may indicate a strong match, but direction is different.

---

# PART 6 — Manual Semantic Search Practical

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "AKS subnet NSG blocked application traffic",
    "Terraform state lock prevented apply",
    "Docker build failed due to disk space",
    "Kubernetes workload lost database connectivity"
]

query = "Pods cannot connect after network security change"

doc_vectors = model.encode(documents)
query_vector = model.encode([query])

scores = cosine_similarity(query_vector, doc_vectors)[0]

ranked = sorted(
    zip(documents, scores),
    key=lambda item: item[1],
    reverse=True
)

for rank, (doc, score) in enumerate(ranked, start=1):
    print(rank, round(float(score), 4), doc)
```

---

# PART 7 — Code Explanation

```python
doc_vectors = model.encode(documents)
```
All docs vectors bante hain.

```python
query_vector = model.encode([query])
```
Query vector banta hai.

```python
cosine_similarity(...)
```
Query ko every document vector se compare karta hai.

```python
sorted(... reverse=True)
```
Highest similarity first.

This is a tiny semantic search engine.

---

# PART 8 — Expected Output

Exact score model/version ke saath vary karega, but expected ranking conceptually:

```text
1  ... AKS subnet NSG blocked application traffic
2  ... Kubernetes workload lost database connectivity
3  ... other less relevant docs
```

Important:

**Exact numeric score se zyada ranking/relevance observe karo.**

---

# PART 9 — Why Brute Force Does Not Scale Forever

Small dataset:

```text
1 query × 10 vectors = easy
```

Large dataset:

```text
1 query × millions of vectors = expensive
```

Naive approach har vector compare karta hai.

Large-scale systems use optimized indexes / approximate nearest neighbor strategies.

Isi liye Vector DB/FAISS later important honge.

---

# PART 10 — Retrieval Quality Problems

Poor result ke possible causes:

```text
bad source docs
bad chunking
weak embedding model
wrong metric
wrong top-k
stale index
irrelevant metadata scope
query ambiguity
```

Important:

```text
Bad retrieval → bad context → bad RAG answer
```

---

# PART 11 — DevOps Example

Query:

```text
Terraform change ke baad AKS deployment fail hua
```

Knowledge base:

```text
AKS NSG troubleshooting
Terraform state locking
CI Terraform Apply failure
Docker registry cleanup
```

Semantic search may retrieve:

```text
#1 AKS NSG troubleshooting
#2 CI Terraform Apply failure
#3 Terraform networking notes
```

This gives investigation candidate knowledge, not automatically proven RCA.

---

# PART 12 — Common Mistakes

1. similarity ko factual proof samajhna
2. arbitrary threshold copy karna
3. score direction assume karna
4. Top-K bahut high rakhkar noise bharna
5. retrieval evaluation na karna
6. duplicate chunks ko ignore karna

---

# PART 13 — Interview Corner

**Q: What is semantic similarity search?**  
It embeds a query and stored items into a comparable vector space and retrieves the nearest items based on a similarity/distance metric.

**Q: What is Top-K retrieval?**  
Returning the K highest-ranked candidate results for a query.

**Q: Does highest similarity guarantee the document is correct?**  
No. Similarity is a relevance signal, not factual validation.

---

# PART 14 — Revision

```text
Documents → Embeddings
Query     → Embedding
             ↓
         Compare
             ↓
           Rank
             ↓
          Top-K
```

---

# PART 15 — Homework

1. Practical me 5 DevOps docs add karo.
2. 3 different queries run karo.
3. Top-3 rankings note karo.
4. Ek example identify karo jahan ranking imperfect thi.

---

# Next Lesson Kyu?

Humne `cosine_similarity()` use kiya, but ye mathematically kya compare kar raha hai?

Next:

# 👉 Lesson 05 — Cosine Similarity & Distance Concepts
