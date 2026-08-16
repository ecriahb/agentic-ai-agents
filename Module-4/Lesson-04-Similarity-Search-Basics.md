# Lesson 04 — Similarity Search Basics

> **Semantic search ka goal exact words nahi, relevant meaning ke nearest results find karna hai.**

## 🎯 Lesson Goal

Query vector ko stored document vectors se compare karke top relevant results select karna.

## English Definition

**Similarity search** finds stored vectors that are closest or most similar to a query vector according to a chosen distance/similarity metric.

## Mental Model

```text
User Query
   ↓
Query Embedding
   ↓
Compare against stored vectors
   ↓
Rank by similarity / distance
   ↓
Top-K results
```

## DevOps Example

Knowledge base:

```text
A. AKS subnet NSG troubleshooting
B. Docker image build optimization
C. Terraform state locking
D. Kubernetes network connectivity incident
```

Query:

```text
Pods cannot reach services after subnet rule change
```

Expected semantic ranking:

```text
1. Kubernetes network connectivity incident
2. AKS subnet NSG troubleshooting
3. Terraform state locking
4. Docker build optimization
```

## Top-K

`k` means how many nearest results return karne hain.

```text
Top-1 → one best match
Top-3 → three best matches
Top-5 → five best matches
```

More results always better nahi hote. Too many chunks irrelevant context introduce kar sakte hain.

## Retrieval Quality

Good retrieval depends on multiple things:

```text
Embedding quality
+ chunk quality
+ similarity metric
+ metadata filters
+ index/search settings
+ query quality
```

## Semantic Search vs Keyword Search

Keyword search:

```text
match literal terms
```

Semantic search:

```text
match meaning represented by vectors
```

Production systems often hybrid approaches use kar sakte hain, but Module 4 me pehle vector retrieval foundation build karenge.

## Common Mistake

Highest similarity result ko automatically factual truth mat samjho. It only means **closest indexed content under the search method**. Source validation still matters.

## Interview Point

**Q: What does top-k retrieval mean?**

It means returning the `k` closest indexed vectors/documents for a query according to the selected similarity or distance measure.

## Next Lesson Kyu?

Ab `close` ka matlab mathematically/intuitively samajhna hai. Isliye next lesson: cosine similarity and distance.
