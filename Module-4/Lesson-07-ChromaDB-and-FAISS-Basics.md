# 🚩 Lesson 07 — ChromaDB & FAISS Basics

> **Ab manual vector comparison se real local vector tooling par move karenge.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- Chroma aur FAISS ka practical role
- collection/index concept
- add vs query/search
- IDs, documents, metadata mapping
- FAISS dimension requirement
- Chroma practical
- FAISS practical
- kab kaunsa tool useful ho sakta hai
- common errors

---

# PART 1 — Why Two Tools?

Hum deliberately do approaches dekh rahe hain:

```text
Chroma → higher-level developer experience
FAISS  → lower-level vector index/search
```

Goal kisi ek product ko memorize karna nahi. Goal vector retrieval mechanics samajhna hai.

---

# PART 2 — Chroma Mental Model

```text
Client
 ↓
Collection
 ↓
IDs + Documents + Metadata + Embeddings
 ↓
Query
 ↓
Nearest Results
```

A collection ko DevOps knowledge namespace samajh sakte ho.

Example:

```text
collection = devops_knowledge
```

---

# PART 3 — Chroma Practical

```python
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("devops_knowledge")

documents = [
    "AKS subnet NSG blocked required traffic",
    "Terraform state lock prevented apply",
    "Docker build failed because disk was full"
]

ids = ["aks-1", "tf-1", "docker-1"]
metadatas = [
    {"service": "aks"},
    {"service": "terraform"},
    {"service": "docker"}
]

embeddings = model.encode(documents).tolist()

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

query = "Kubernetes networking issue"
query_embedding = model.encode([query]).tolist()

result = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

print(result)
```

---

# PART 4 — Chroma Code Explanation

```python
chromadb.Client()
```
Creates local client for the demo.

```python
get_or_create_collection(...)
```
Logical collection gets created/reused.

```python
collection.add(...)
```
Stores IDs, text, metadata and embeddings.

```python
collection.query(...)
```
Searches nearest vectors for query embedding.

### Important

Production configuration/persistence depends on how Chroma is deployed. Demo client ko production architecture assume mat karo.

---

# PART 5 — FAISS Mental Model

FAISS typically focuses on vectors + nearest-neighbor index.

```text
Documents
 ↓ embedding
NumPy vectors
 ↓
FAISS Index
 ↓
search(query_vector, k)
 ↓
indices + distances/scores
 ↓
map index position back to document
```

Document/metadata mapping app ko manage karni pad sakti hai.

---

# PART 6 — FAISS Practical

```python
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "AKS subnet NSG blocked required traffic",
    "Terraform state lock prevented apply",
    "Docker build failed because disk was full"
]

vectors = model.encode(documents, normalize_embeddings=True)
vectors = np.asarray(vectors, dtype="float32")

dimension = vectors.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(vectors)

query = "Kubernetes networking issue"
query_vector = model.encode([query], normalize_embeddings=True)
query_vector = np.asarray(query_vector, dtype="float32")

scores, indices = index.search(query_vector, k=2)

for score, idx in zip(scores[0], indices[0]):
    print(float(score), documents[idx])
```

---

# PART 7 — Why `float32`?

FAISS commonly expects arrays in compatible numeric format such as `float32`.

```python
np.asarray(vectors, dtype="float32")
```

Avoid mysterious type/shape bugs by checking:

```python
print(vectors.dtype)
print(vectors.shape)
```

---

# PART 8 — Why `dimension = vectors.shape[1]`?

FAISS index dimension must match embedding dimension.

```text
Embedding shape = (3, 384)
                    ↑
             dimension = 384
```

If query vector dimension differs, search cannot work correctly.

---

# PART 9 — `IndexFlatIP` vs `IndexFlatL2`

Simplified:

```text
IndexFlatIP → inner product
IndexFlatL2 → L2 distance
```

If using normalized vectors with inner product, ranking can be used for cosine-like similarity behavior.

Do not mix metric interpretation:

```text
IP score: higher often better
L2 distance: lower better
```

---

# PART 10 — Chroma vs FAISS Comparison

| Area | Chroma | FAISS |
|---|---|---|
| Abstraction | Higher | Lower |
| Documents | Built into collection workflow | App mapping often needed |
| Metadata | Convenient | Usually app-side/separate |
| Vector indexing | Yes | Core strength |
| Learning goal | End-to-end store/query | Understand vector index mechanics |

This table is conceptual, not a universal product benchmark.

---

# PART 11 — DevOps Practical

Query:

```text
production pods cannot connect after security rule update
```

Expected relevant record:

```text
AKS subnet NSG blocked required traffic
```

Now semantic search is no longer manually sorting cosine scores; index/store is doing retrieval.

---

# PART 12 — Common Errors

### Error: dimension mismatch

Fix: same embedding model/compatible vectors.

### Error: wrong dtype in FAISS

Fix: inspect/convert to `float32`.

### Error: duplicates in collection

Use stable IDs and deliberate ingestion strategy.

### Error: documents returned but no source

Always store useful metadata.

### Error: model changed

Re-index; do not assume old embeddings compatible.

---

# PART 13 — Production Thinking

Prototype tool selection se pehle think about:

- persistent storage
- backups
- update/delete
- metadata filtering
- authorization
- scale
- latency
- multi-tenancy
- observability
- deployment model

---

# PART 14 — Interview Corner

**Q: Difference between Chroma and FAISS at a high level?**  
Chroma provides a higher-level vector collection workflow including documents/metadata, while FAISS is primarily a vector similarity indexing/search library.

**Q: Why must FAISS index dimension match embeddings?**  
Because all indexed and query vectors must share the dimensionality expected by the index.

---

# PART 15 — Revision

```text
Embedding Model
   ↓
Vectors
   ↓
Chroma Collection OR FAISS Index
   ↓
Query Vector
   ↓
Top-K Search
```

---

# PART 16 — Homework

1. `03_chromadb_search.py` run karo.
2. `04_faiss_search.py` run karo.
3. Dono me 5 same DevOps documents use karo.
4. Top-3 result compare karo.

---

# Next Lesson Kyu?

Ab tool ready hai. Lekin real runbook ek single sentence nahi hota—wo pages long hota hai.

**Large document ko searchable units me kaise split karein?**

# 👉 Lesson 08 — Chunking Strategies
