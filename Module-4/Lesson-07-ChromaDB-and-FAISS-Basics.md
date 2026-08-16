# Lesson 07 — ChromaDB / FAISS Basics

> **Same vector-search problem, different abstraction levels.**

## 🎯 Lesson Goal

ChromaDB aur FAISS ka beginner-level difference samajhna aur dono ka basic search flow dekhna.

## FAISS Mental Model

```text
Vectors
  ↓
FAISS Index
  ↓
add()
  ↓
search(query_vector, k)
  ↓
nearest vector IDs + distances
```

FAISS ka `IndexFlatL2` simple exact L2 nearest-neighbor search ke liye useful learning index hai.

```python
import faiss
import numpy as np

vectors = np.array([
    [1.0, 0.9, 0.1],
    [0.1, 0.2, 1.0],
    [0.8, 1.0, 0.2],
], dtype="float32")

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

query = np.array([[0.9, 0.95, 0.1]], dtype="float32")
distances, ids = index.search(query, k=2)

print(ids)
print(distances)
```

FAISS index vector IDs return karta hai, so original documents/metadata ko application side map karna padta hai.

---

## Chroma Mental Model

```text
Documents + IDs + Metadata
          ↓
       Collection
          ↓
         add
          ↓
        query
          ↓
documents + metadata + distances
```

Conceptual example:

```python
import chromadb

client = chromadb.PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection("devops_docs")

collection.add(
    ids=["doc1", "doc2"],
    documents=[
        "AKS subnet NSG troubleshooting steps",
        "Docker image build optimization guide"
    ],
    metadatas=[
        {"service": "aks"},
        {"service": "docker"}
    ]
)

results = collection.query(
    query_texts=["Kubernetes networking issue"],
    n_results=2
)

print(results)
```

A collection can store documents, embeddings and metadata and return matching records.

## Difference for This Course

```text
FAISS
→ learn vector index mechanics clearly
→ you manage document mapping/metadata separately

Chroma
→ higher-level developer experience
→ document + metadata + vector retrieval together
```

Neither is automatically “best”. Choice depends on scale, deployment, persistence, filtering, operations and application requirements.

## Production Warning

Demo defaults are not production architecture. Before production use, evaluate persistence, backup, auth, tenancy, data lifecycle, index behavior and operational support.

## Common Mistakes

- vector DB ko embedding model samajhna
- FAISS ko document database samajhna
- test collection me duplicate IDs blindly insert karna
- local persistent directory ko source-controlled data samajhna

## Interview Point

**Q: Chroma and FAISS me conceptual difference?**

FAISS is primarily a vector similarity search/indexing library, while Chroma exposes a collection-oriented vector-store/database experience with documents and metadata around retrieval.

## Next Lesson Kyu?

Search engine ready hai, but poor document splitting se poor retrieval milega. Next: **chunking strategy**.
