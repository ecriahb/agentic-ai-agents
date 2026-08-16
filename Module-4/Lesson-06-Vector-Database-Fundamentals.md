# 🚩 Lesson 06 — Vector Database Fundamentals

> **Vector database ka kaam LLM banna nahi hai; uska kaam embeddings ko efficiently store, index aur search karna hai.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- vector database kya hai
- normal database aur vector database me conceptual difference
- vector index kya hai
- exact vs approximate nearest neighbor
- metadata ka role
- persistence, updates aur re-indexing
- Chroma/FAISS ka role
- production design questions

---

# PART 1 — Why We Need It

Small demo:

```text
10 vectors → Python list → compare all
```

Real system:

```text
10,000 / 1,000,000+ chunks
       ↓
Need efficient storage + indexing + search
```

Sirf arrays maintain karna quickly operationally difficult ho jata hai.

---

# PART 2 — English Definition

> A vector database or vector-capable index stores high-dimensional vectors and supports efficient nearest-neighbor search, often together with documents, IDs and metadata.

Hinglish:

```text
Vector DB = embeddings ka searchable system
```

It may manage:

```text
ID
vector
original chunk/document
metadata
index
search
persistence
```

---

# PART 3 — Normal DB vs Vector Search

Traditional lookup:

```sql
SELECT * FROM incidents WHERE environment = 'prod';
```

Exact/filter style query.

Vector search:

```text
"AKS connectivity failed after network rule change"
        ↓ embedding
nearest semantic chunks
```

Both useful hain.

Production retrieval often combines:

```text
metadata filter + semantic vector search
```

Example:

```text
environment = prod
AND
semantic similarity to "AKS network issue"
```

---

# PART 4 — Vector Index

Without optimized index:

```text
Query vector
   ↓
compare with every stored vector
```

Index search ko accelerate karta hai.

Mental model:

```text
Vectors
  ↓
Index Structure
  ↓
Fast Candidate Search
  ↓
Nearest Results
```

Vector DB and vector index same exact thing nahi hote. Database broader lifecycle/features provide kar sakta hai; FAISS primarily vector similarity indexing/search library hai.

---

# PART 5 — Exact vs Approximate Search

## Exact Nearest Neighbor

Every relevant vector accurately compare karne ka goal.

Pros:
- deterministic/exact for chosen metric/index

Cons:
- huge datasets par expensive ho sakta hai

## Approximate Nearest Neighbor (ANN)

Speed ke liye search space intelligently reduce karta hai.

Tradeoff:

```text
Speed / scale ↑
Potential perfect recall ↓
```

Production retrieval is a tradeoff, not magic.

---

# PART 6 — What Gets Stored?

Example chunk record:

```json
{
  "id": "aks-runbook-03",
  "text": "Validate outbound NSG rules for AKS subnet...",
  "metadata": {
    "source": "aks-networking.md",
    "environment": "prod",
    "version": "v4"
  },
  "embedding": [0.12, -0.08, 0.44]
}
```

Real vector has many more dimensions.

---

# PART 7 — Ingestion vs Query Path

## Ingestion

```text
Document
 ↓
Chunk
 ↓
Embedding
 ↓
Vector DB / Index
```

## Query

```text
User query
 ↓
Query embedding
 ↓
Vector search
 ↓
Top-K chunks
```

Do not re-embed entire document collection on every query.

---

# PART 8 — Persistence

Prototype:

```text
process ends → index disappears
```

Persistent system:

```text
Index stored on disk/service
    ↓
application restart
    ↓
index reused
```

But persistence introduces lifecycle questions:

- document changed?
- chunk deleted?
- model changed?
- duplicate ingestion?
- old version stale?

---

# PART 9 — Chroma vs FAISS Mental Model

```text
Chroma
→ developer-friendly collection/store abstraction
→ documents + metadata + embeddings + query workflow

FAISS
→ high-performance vector indexing/search library
→ you usually manage document text/metadata mapping yourself
```

Neither should be treated as the universally best production option. Tool choice depends on scale, deployment, operations, security, filtering and team requirements.

---

# PART 10 — DevOps Knowledge Base Example

```text
AKS runbooks
Terraform docs
pipeline postmortems
Azure networking SOPs
       ↓
chunks + embeddings
       ↓
vector store
       ↓
Query: "pods lost access after NSG change"
       ↓
Top relevant operational knowledge
```

---

# PART 11 — Common Mistakes

1. Vector DB ko LLM memory samajhna.
2. Source text/metadata mapping lose kar dena.
3. Duplicate docs repeatedly ingest karna.
4. Model change ke baad incompatible old vectors use karna.
5. Authorization ko metadata filter se replace karna.
6. Index freshness monitor na karna.

---

# PART 12 — Production Design Checklist

Before choosing a vector solution, ask:

```text
How many vectors?
Required latency?
Metadata filtering?
Persistence?
Backups?
Multi-tenancy?
Access control?
Encryption?
Update/delete frequency?
Hybrid search needed?
Managed vs self-hosted?
```

---

# PART 13 — Interview Corner

**Q: What is a vector database?**  
A system designed to store/index high-dimensional vectors and retrieve nearest items efficiently, often with metadata and source content.

**Q: What is ANN?**  
Approximate nearest-neighbor search trades some exactness/recall for faster scalable retrieval.

**Q: Is FAISS a full database?**  
It is primarily a vector similarity search/indexing library, so broader persistence/metadata/application lifecycle may need separate handling.

---

# PART 14 — Revision

```text
Chunks
 ↓
Embeddings
 ↓
Vector Store / Index
 ↓
Query Embedding
 ↓
Nearest Neighbor Search
 ↓
Top-K
```

---

# PART 15 — Homework

1. Normal SQL filter aur vector similarity search ka difference explain karo.
2. Exact vs approximate nearest neighbor ka tradeoff likho.
3. Vector record me text + metadata preserve kyu karna chahiye?

---

# Next Lesson Kyu?

Concept clear hai. Ab actual local tools use karenge.

# 👉 Lesson 07 — ChromaDB & FAISS Basics
