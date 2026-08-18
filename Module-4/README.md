# 🚩 Module 4 — Embeddings & Vector Search for DevOps AI

> **From manually supplied context → automatically finding semantically relevant knowledge.**

## 🎯 Role in the Course

M3 taught reliable AI application plumbing. M4 introduces the retrieval primitive needed when context becomes too large or dynamic to supply manually.

```text
M3: Python + API + LLM
        ↓
Problem: context cannot be manually supplied forever
        ↓
M4: Embeddings + Vector Search
        ↓
M5: RAG = retrieve + augment + generate
```

## 📚 Canonical Lesson Sequence

| # | Topic | Deep points |
|---|---|---|
| 01 | Why LLMs Need External Knowledge | private/current knowledge, model boundary |
| 02 | What Are Embeddings? | semantic representation, embedding space |
| 03 | How Text Becomes Vectors | ingestion and query embedding pipeline |
| 04 | Similarity Search Basics | nearest semantic matches, top-k |
| 05 | Cosine Similarity & Distance | score intuition and limitations |
| 06 | Vector Database Fundamentals | storage, indexing, metadata |
| 07 | ChromaDB / FAISS Basics | practical local implementations |
| 08 | Chunking Strategies | size, overlap, semantic boundaries |
| 09 | Metadata & Filtering | environment/service/source filters |
| 10 | Indexing & Retrieval Flow | ingestion-time vs query-time |
| 11 | DevOps Knowledge Base Practical | runbooks/incidents as searchable knowledge |
| 12 | Mini Project — Search Your DevOps Documents | complete semantic search app |

## 🛠️ Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

Install only the dependencies in this module's `examples/requirements.txt`. Prefer local embedding/search labs first. Keep provider credentials outside source code.

## 🧠 Deep Learning Path

```text
Document
  ↓
Clean / normalize
  ↓
Chunk
  ↓
Embedding model
  ↓
Vector + metadata
  ↓
Index

User query
  ↓
Query embedding
  ↓
Similarity search
  ↓
Top-k candidates
  ↓
Metadata filters
```

### What an embedding is

An embedding maps an item such as a sentence into a numeric vector. Semantically related text should generally occupy nearby regions in embedding space. It is a retrieval representation, **not a truth score**.

### Example

Knowledge base:

```text
D1: AKS subnet NSG rules and required traffic
D2: Terraform state locking procedure
D3: Kubernetes image pull troubleshooting
```

Query:

```text
"AKS deployment cannot reach required network endpoints"
```

The retriever should surface D1 even if the query does not contain the exact phrase `NSG rule`.

## 🧪 Practical Progression

```text
V1 cosine similarity
V2 simple semantic search
V3 ChromaDB
V4 FAISS
V5 metadata filtering
V6 DevOps knowledge base
V7 end-to-end search mini-project
```

## 🔐 Trust Boundary

Retrieved material is **reference knowledge**, not proof of current incident state.

```text
Current incident evidence ≠ RAG reference knowledge
```

This distinction becomes a hard rule in M5 and M10.

## 🚫 Do Not Repeat Later

M4 owns embeddings, vector representation and retrieval mechanics. M5 will not reteach vector mathematics; it will use the retriever to ground generation.

## ✅ Exit Gate

Before moving to M5, you should be able to explain:

1. Why embeddings are useful.
2. What query and document embeddings are.
3. What top-k means.
4. Why chunking changes retrieval quality.
5. Why metadata filters matter.
6. Why a high similarity score does not prove factual truth.
7. The difference between indexing-time and query-time work.

## 🔗 Continue

➡️ [Module 5 — RAG](../Module-5/README.md)

⬅️ [Module 3 — APIs & Minimal Python](../Module-3/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
