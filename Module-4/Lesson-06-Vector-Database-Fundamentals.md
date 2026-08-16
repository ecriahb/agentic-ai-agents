# Lesson 06 — Vector Database Fundamentals

> **Vector database embeddings ko sirf store nahi karta; unko search-friendly structure me manage karta hai.**

## 🎯 Lesson Goal

Vector DB ka role, components, metadata aur retrieval lifecycle samajhna.

## English Definition

A **vector database** stores vector embeddings together with associated records and supports similarity-based retrieval over those vectors.

## Mental Model

```text
Document Chunk
   ↓
Embedding
   ↓
Vector + Text + Metadata
   ↓
Vector Store / Index
   ↓
Similarity Search
   ↓
Relevant Records
```

## Typical Record

```json
{
  "id": "aks-runbook-12",
  "text": "Validate NSG rules on the AKS subnet...",
  "embedding": [0.12, 0.77, -0.18],
  "metadata": {
    "service": "aks",
    "environment": "production",
    "type": "runbook"
  }
}
```

## What Vector DB Solves

- embeddings store karna
- IDs manage karna
- similarity search
- top-k retrieval
- metadata attach/filter karna
- persistence
- large collections me index/search optimize karna

## Vector Database vs Traditional Database

Traditional DB query:

```sql
WHERE service = 'aks'
```

Vector query:

```text
Find chunks semantically closest to:
"pods lost connectivity after subnet change"
```

Best systems dono combine kar sakte hain:

```text
metadata filter + semantic similarity
```

## Index vs Database

Beginner-friendly distinction:

```text
Vector Index
→ optimized structure for nearest-neighbor search

Vector Database
→ vectors + records + metadata + persistence + query/management features
```

FAISS primarily vector similarity search/indexing library hai; Chroma vector database/store style developer experience provide karta hai.

## DevOps Use Case

```text
500 runbooks
300 incident RCAs
100 architecture notes
200 Terraform standards
        ↓
Embed and index
        ↓
Search by incident meaning
```

## Production Concerns

- data freshness
- access control
- tenancy
- backup/persistence
- document deletion/update
- embedding version migration
- metadata quality
- retrieval evaluation

## Interview Point

**Q: Why not store embeddings only in a Python list?**

Small demos me possible hai, but production retrieval needs efficient indexing, persistence, metadata, filtering, lifecycle management and scalable nearest-neighbor search.

## Next Lesson Kyu?

Concept clear hai; ab do practical approaches compare karenge: **ChromaDB and FAISS**.
