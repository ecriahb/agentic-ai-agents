# Lesson 07 — Query Rewriting & Multi-Query Retrieval

> **User ki wording aur knowledge-base ki wording alag ho sakti hai; retrieval ko kabhi-kabhi query ko better form me convert karna padta hai.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- query rewriting kya hai
- vague vs retrieval-friendly query
- domain expansion
- acronym normalization
- multi-query retrieval
- deduplication and merge
- when rewriting can hurt

---

## English Definition

**Query rewriting** transforms a user query into a retrieval-friendly representation, while **multi-query retrieval** searches using multiple related query variants and combines the results.

---

# PART 1 — Why User Query Can Be Weak

User asks:

```text
prod deploy toot gaya network change ke baad
```

Knowledge base uses:

```text
AKS deployment
Terraform Apply
Network Security Group
subnet connectivity
```

Semantic embeddings help, but query can still be underspecified.

A rewritten query:

```text
Production AKS deployment failure after Terraform networking/NSG change
```

may retrieve better operational docs.

---

# PART 2 — Types of Query Rewriting

### Normalization

```text
k8s → Kubernetes
TF → Terraform
prod → production
```

### Clarification

```text
"pipeline failed"
→ "deployment pipeline failed during Terraform Apply"
```

### Domain Expansion

```text
"network rule"
→ "NSG rule, subnet connectivity, UDR, private endpoint"
```

But expansion should not invent facts.

---

# PART 3 — Safe Rewrite Principle

Bad rewrite:

```text
User: deployment failed
Rewrite: AKS failed because NSG rule was deleted
```

This injects an unverified cause.

Better rewrite:

```text
Deployment failure; retrieve documents related to pipeline errors, Terraform Apply and recent infrastructure/network changes.
```

Rewrite should improve search intent, not decide the answer.

---

# PART 4 — Multi-Query Retrieval

Instead of one query:

```text
Q1: AKS deployment failure after networking change
Q2: Terraform Apply failure NSG subnet connectivity
Q3: Kubernetes production deployment network troubleshooting
```

Search each query, then merge results.

```text
Q1 → S1 S3 S5
Q2 → S1 S2 S4
Q3 → S3 S6 S1

Merge + Deduplicate
→ S1 S3 S2 S5 S4 S6
```

---

# PART 5 — Reciprocal / Simple Merge Concept

Beginner approach:

```python
seen = set()
merged = []

for result_list in all_results:
    for item in result_list:
        if item["chunk_id"] not in seen:
            seen.add(item["chunk_id"])
            merged.append(item)
```

Advanced systems may score/fuse rankings instead of simple append.

---

# PART 6 — DevOps Example

User:

```text
App cannot reach DB after infra deployment
```

Potential query variants:

```text
1. application database connectivity failure after Terraform deployment
2. AKS to Azure SQL private endpoint connectivity issue
3. subnet NSG UDR DNS connectivity troubleshooting
```

Retriever may uncover:

- AKS networking runbook
- private DNS troubleshooting
- NSG change RCA

---

# PART 7 — When Rewriting Can Hurt

Rewrite model can:

- add assumptions
- remove important literal identifiers
- replace exact error text
- over-generalize

Example exact error:

```text
AuthorizationFailed: client does not have authorization to perform action
```

For such queries, exact keyword/hybrid retrieval may be better than paraphrasing away the error.

---

# PART 8 — Preserve Original Query

Good architecture:

```text
Original Query
   ↓
Rewrite(s)
   ↓
Retrieval
   ↓
Final Answer uses ORIGINAL user question
```

Never lose original intent.

Store:

```python
{
    "original_query": original,
    "rewritten_queries": rewrites
}
```

for observability/debugging.

---

## Common Mistakes

- rewrite decides root cause
- exact error message discarded
- too many query variants increase noise/cost
- results merged without deduplication
- original query not logged

---

## Interview Corner

**Q: Why use multi-query retrieval?**

To improve recall when one phrasing may not retrieve all relevant evidence.

**Q: What is the risk of LLM-based query rewriting?**

The rewrite can introduce unsupported assumptions or remove important literal terms.

---

## Revision

```text
Original Question
   ↓
Safe Rewrite / Variants
   ↓
Multiple Retrievals
   ↓
Merge + Deduplicate
   ↓
Better Candidate Set
```

---

## Homework

Create 3 retrieval-friendly variants for:

```text
"service down after terraform"
```

without assuming the root cause.

---

## Next Lesson Kyu?

Multi-query zyada candidates la sakta hai. Ab unme se **best evidence ko final top positions me kaise laayen?**

Next: **Reranking & Hybrid Search**.
