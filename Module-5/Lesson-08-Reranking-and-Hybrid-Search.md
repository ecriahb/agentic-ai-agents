# Lesson 08 — Reranking & Hybrid Search Concepts

> **First-stage retrieval candidate laata hai; reranking un candidates ko better relevance order me arrange karta hai.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- retrieval vs reranking
- recall vs precision intuition
- vector search strengths/limits
- keyword search strengths/limits
- hybrid retrieval
- candidate generation → reranking architecture
- DevOps exact error + semantic intent example

---

## English Definition

**Reranking** re-scores an initial set of retrieved candidates using a stronger relevance method. **Hybrid search** combines multiple retrieval signals, commonly semantic vector relevance and lexical/keyword relevance.

---

# PART 1 — Why One Search Signal Is Not Enough

Vector search is strong when wording differs but meaning is similar.

Keyword search is strong for exact literals:

```text
aks-subnet-allow
AuthorizationFailed
CrashLoopBackOff
10.20.4.0/24
```

DevOps has both semantic questions and exact identifiers.

---

# PART 2 — Example

Query:

```text
Terraform Apply failed with AuthorizationFailed on subnet join action
```

Vector search may find:

- Terraform RBAC troubleshooting
- AKS networking permissions

Keyword search may strongly match:

```text
AuthorizationFailed
Microsoft.Network/virtualNetworks/subnets/join/action
```

Hybrid approach can combine both signals.

---

# PART 3 — Candidate Generation + Rerank

```text
User Query
   ↓
Fast Retrieval
   ↓
Top 20 candidates
   ↓
Reranker
   ↓
Top 5 high-quality chunks
   ↓
Context Builder
   ↓
LLM
```

Why?

First stage optimized for **recall**:

```text
Don't miss useful evidence.
```

Reranking optimized for **precision**:

```text
Put truly useful evidence at top.
```

---

# PART 4 — Simple Reranking Mental Model

Initial vector scores:

```text
S1 0.82
S2 0.81
S3 0.79
S4 0.77
```

A stronger relevance model reads query + full chunk together and may reorder:

```text
S3 → best
S1 → second
S4 → third
S2 → fourth
```

The exact implementation can vary; concept is what matters here.

---

# PART 5 — Hybrid Search Mental Model

```text
                  User Query
                      ↓
             ┌────────┴────────┐
             ↓                 ↓
       Vector Search      Keyword Search
             ↓                 ↓
      Semantic Hits        Exact Hits
             └────────┬────────┘
                      ↓
                 Score Fusion
                      ↓
                  Reranking
                      ↓
                    Top-K
```

---

# PART 6 — Exact DevOps Identifiers

Query includes:

```text
aks-subnet-allow
```

Semantic system may understand networking meaning, but exact keyword signal can guarantee that docs containing this specific rule are not overlooked.

Similarly:

```text
exit code 137
OOMKilled
HTTP 429
TF401019
```

literal search matters.

---

# PART 7 — When Hybrid Search Helps Most

- error codes
- resource names
- Kubernetes object names
- Azure action/resource-provider strings
- IPs/CIDRs
- ticket numbers
- exact Terraform resource addresses
- command output

---

# PART 8 — Reranking Cost Tradeoff

Reranking every document is expensive.

Better:

```text
Large Corpus
   ↓
Cheap/Fast First Retrieval
   ↓
Small Candidate Set
   ↓
Expensive/Strong Reranker
```

---

# PART 9 — DevOps Example

Question:

```text
Why does pod billing-api restart with OOMKilled?
```

Hybrid candidates:

- pod memory troubleshooting runbook
- historical `billing-api` incident
- Kubernetes limits guide
- exact OOMKilled RCA

Reranker can push the environment/service-specific incident above generic docs.

---

## Common Mistakes

- vector retrieval treated as universally best
- exact error identifiers ignored
- reranker applied to entire corpus
- candidate set too small before reranking
- fusion logic not evaluated

---

## Interview Corner

**Q: What is the difference between retrieval and reranking?**

Retrieval efficiently finds a candidate set; reranking applies a stronger relevance method to reorder that smaller set.

**Q: Why is hybrid search useful in DevOps RAG?**

Because DevOps questions often contain both semantic intent and exact technical identifiers.

---

## Revision

```text
Vector Search = meaning
Keyword Search = exact terms
Hybrid = both
Reranker = better final ordering
```

---

## Homework

For each query decide whether vector, keyword or hybrid is best:

1. `CrashLoopBackOff after secret rotation`
2. `aks-subnet-allow`
3. `Why can pods not reach SQL?`
4. `Microsoft.Network/virtualNetworks/subnets/join/action`

---

## Next Lesson Kyu?

Retrieval better ho gaya, but model still retrieved evidence ke beyond bol sakta hai.

Next: **RAG Hallucinations & Guardrails**.
