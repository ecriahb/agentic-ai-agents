# Lesson 12 — Mini Project: Search Your Own DevOps Documents

> **Goal: apne DevOps documents ko local semantic search application me convert karna.**

## 🎯 Project Outcome

User query dega:

```text
AKS deployment Terraform networking change ke baad fail ho raha hai
```

Application relevant local documents retrieve karegi.

## Architecture

```text
sample_docs/*.md
      ↓
Document Loader
      ↓
Chunking
      ↓
Embedding
      ↓
Vector Store / Index
      ↓
User Query
      ↓
Query Embedding
      ↓
Top-K Search
      ↓
Source + Relevant Text
```

## Project Stages

### Stage 1 — Prepare Documents

Create:

```text
sample_docs/
├── aks-networking.md
├── terraform-state.md
├── pipeline-failure.md
└── docker-build.md
```

### Stage 2 — Ingest

For every file:

```text
read
→ split
→ attach source metadata
→ embed
→ index
```

### Stage 3 — Query

```text
query
→ embedding
→ search
→ top 3 chunks
```

### Stage 4 — Display Traceable Results

Output should include:

```text
Rank
Source
Relevant chunk
Score / distance
Metadata
```

Not just anonymous text.

## Example Expected Output

```text
Query: pods lost connectivity after NSG change

#1 aks-networking.md
Validate NSG rules on the AKS subnet...

#2 pipeline-failure.md
When deployment fails during Terraform Apply...
```

## Acceptance Criteria

Project complete tab maana jayega jab:

- local documents load ho rahe hain
- chunks identifiable hain
- embeddings/index create ho raha hai
- arbitrary user query accept hoti hai
- top-k relevant results milte hain
- source shown hota hai
- missing/empty docs safely handle hote hain
- no secrets source docs me included hain

## Production Improvements Later

```text
better embedding model
recursive/semantic chunking
metadata filters
document versioning
incremental indexing
hybrid keyword + vector search
reranking
authorization
retrieval evaluation
observability
```

## Most Important Learning

Module 4 ka goal LLM se answer generate karna nahi hai.

Goal hai:

```text
Question
  ↓
Find the right knowledge
```

Module 5 me isi retrieved knowledge ko LLM context me denge:

```text
Question
  ↓
Retrieve Relevant Knowledge
  ↓
Give Context to LLM
  ↓
Grounded Answer
```

That is the core RAG flow.

## Final Revision

```text
External Knowledge
   ↓
Chunking
   ↓
Embeddings
   ↓
Vectors
   ↓
Vector Index / DB
   ↓
Similarity Search
   ↓
Metadata Filtering
   ↓
Top-K Retrieval
   ↓
Traceable DevOps Context
```

✅ **Module 4 complete → ready for Module 5: Retrieval-Augmented Generation (RAG).**
