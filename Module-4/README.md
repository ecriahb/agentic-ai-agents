# 🚩 Module 4 — Embeddings & Vector Search for DevOps AI

> **From manually supplied context → automatically finding semantically relevant knowledge.**

## 🎯 Role in the Course

M3 taught reliable AI application plumbing. M4 introduces the missing retrieval primitive: represent knowledge as vectors and search it by meaning.

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
| 01 | [Why LLMs Need External Knowledge](Lesson-01-Why-LLMs-Need-External-Knowledge.md) | private/current knowledge, model boundary |
| 02 | [What Are Embeddings?](Lesson-02-What-Are-Embeddings.md) | semantic representation, embedding space |
| 03 | [How Text Becomes Vectors](Lesson-03-Text-to-Vectors.md) | ingestion and query embedding pipeline |
| 04 | [Similarity Search Basics](Lesson-04-Similarity-Search-Basics.md) | nearest semantic matches, top-k |
| 05 | [Cosine Similarity & Distance](Lesson-05-Cosine-Similarity-and-Distance.md) | score intuition and limitations |
| 06 | [Vector Database Fundamentals](Lesson-06-Vector-Database-Fundamentals.md) | storage, indexing, metadata |
| 07 | [ChromaDB / FAISS Basics](Lesson-07-ChromaDB-and-FAISS-Basics.md) | practical local implementations |
| 08 | [Chunking Strategies](Lesson-08-Chunking-Strategies.md) | chunk size, overlap, semantic boundaries |
| 09 | [Metadata & Filtering](Lesson-09-Metadata-and-Filtering.md) | environment/service/source filters |
| 10 | [Indexing & Retrieval Flow](Lesson-10-Indexing-and-Retrieval-Flow.md) | ingestion-time vs query-time |
| 11 | [DevOps Knowledge Base Practical](Lesson-11-DevOps-Knowledge-Base-Practical.md) | runbooks/incidents as searchable knowledge |
| 12 | [Mini Project — Search Your DevOps Documents](Lesson-12-Mini-Project-Search-Your-DevOps-Docs.md) | complete semantic search app |

## 🛠️ Setup

Use the module environment and install [`examples/requirements.txt`](examples/requirements.txt). Keep embedding/provider credentials outside source code. Local-only embedding/search labs are preferred for learning.

```text
Documents
  ↓
Chunk
  ↓
Embed
  ↓
Vector index
```

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

Example knowledge:

```text
AKS networking runbook
Terraform troubleshooting
Previous NSG incident
Deployment failure postmortem
```

## 🔐 Trust Boundary

A retrieved document is **reference knowledge**, not proof of current incident state.

```text
Current incident evidence ≠ RAG reference knowledge
```

M5 will combine retrieval with LLM generation and citations.

## 🔗 Continue

➡️ [Module 5 — RAG](../Module-5/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
