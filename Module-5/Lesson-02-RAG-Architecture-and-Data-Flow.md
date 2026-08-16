# Lesson 02 — RAG Architecture & Data Flow

> **RAG ko samajhne ka sabse important step: indexing-time aur query-time ko alag samajhna.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- indexing pipeline
- query pipeline
- offline vs runtime work
- document loader, chunker, embedding model, index, retriever, context builder and LLM roles
- where errors can happen
- DevOps knowledge architecture

---

## English Definition

A RAG system usually has two major flows: an **indexing flow**, where source knowledge is prepared for retrieval, and a **query flow**, where relevant knowledge is retrieved and supplied to the LLM.

---

# PART 1 — Full Architecture

```text
                 INDEXING SIDE

Documents / Runbooks / RCA / SOP
              ↓
          Load Content
              ↓
            Clean
              ↓
            Chunk
              ↓
        Add Metadata
              ↓
           Embed
              ↓
       Vector Index / DB


                 QUERY SIDE

User Question
      ↓
Query Embedding
      ↓
Retriever
      ↓
Top Relevant Chunks
      ↓
Context Builder
      ↓
Grounded Prompt
      ↓
LLM
      ↓
Answer + Sources
```

---

# PART 2 — Indexing-Time

Suppose knowledge folder contains:

```text
runbooks/
├── aks-networking.md
├── terraform-state.md
├── deployment-rollback.md
└── sql-private-endpoint.md
```

Indexing pipeline:

```text
Read file
  ↓
Split into chunks
  ↓
Attach source metadata
  ↓
Generate embedding
  ↓
Store vector + text + metadata
```

Example record:

```python
{
    "id": "aks-networking-004",
    "text": "Validate the AKS subnet NSG rules...",
    "source": "aks-networking.md",
    "environment": "production",
    "version": "2026-08"
}
```

---

# PART 3 — Query-Time

User asks:

```text
What should I check if AKS pods lose connectivity after an NSG change?
```

Runtime flow:

```text
Question
 ↓
Question embedding
 ↓
Search index
 ↓
Top 3 chunks
 ↓
Build context block
 ↓
Send question + context to LLM
 ↓
Answer
```

---

# PART 4 — Why Separate the Two?

Imagine 10,000 documents hain.

Har user query ke time 10,000 docs ko dubara chunk + embed karna inefficient hoga.

Better architecture:

```text
Documents change occasionally
        ↓
Index once / incrementally

Questions arrive frequently
        ↓
Only embed query + search
```

---

# PART 5 — Component Responsibilities

### Loader
Source read karta hai.

### Chunker
Large documents ko retrieval-friendly units me todta hai.

### Embedding Model
Text ko vector banata hai.

### Vector Store / Index
Vectors ko searchable structure me store karta hai.

### Retriever
Question ke liye relevant chunks choose karta hai.

### Context Builder
Retrieved chunks ko structured LLM context me convert karta hai.

### LLM
Given context ke basis par natural-language answer generate karta hai.

---

# PART 6 — DevOps RAG Architecture

```text
Git Docs / Runbooks / Incident RCAs / Wiki Export
                    ↓
                 Ingestion
                    ↓
                 Chunking
                    ↓
            Metadata + Version
                    ↓
                Embeddings
                    ↓
               Vector Index
                    ↓
             DevOps Question
                    ↓
                Retrieval
                    ↓
        Authorized Relevant Context
                    ↓
                Local/Cloud LLM
                    ↓
          Answer + Source References
```

---

# PART 7 — Failure Map

A RAG answer can fail at different layers:

```text
Source wrong/stale
       ↓
Chunking bad
       ↓
Embedding mismatch
       ↓
Retriever misses answer
       ↓
Context too noisy
       ↓
Prompt weak
       ↓
LLM overclaims
```

This is why "RAG output wrong" bolna enough nahi hai. Debug layer identify karna hota hai.

---

# PART 8 — Incremental Indexing

Production me whole index rebuild har small change par ideal nahi hota.

Common pattern:

```text
Detect changed document
       ↓
Remove old chunks
       ↓
Create new chunks
       ↓
Re-embed changed content
       ↓
Update index
```

Metadata me useful fields:

```text
source
version
last_updated
team
environment
classification
```

---

## Common Mistakes

- query-time pe documents re-embed karna
- old chunks remove na karna
- embedding model silently change kar dena
- source version track na karna
- retrieval aur generation logs mix kar dena

---

## Interview Corner

**Q: What are the two major pipelines in RAG?**

Indexing/ingestion pipeline and query/retrieval-generation pipeline.

**Q: Why should embedding model consistency be maintained?**

Because stored document vectors and query vectors must live in a compatible vector space.

---

## Revision

```text
INDEXING:
Docs → Chunk → Metadata → Embed → Store

QUERY:
Question → Embed → Retrieve → Context → LLM → Answer
```

---

## Homework

Draw this architecture for an internal DevOps assistant using:

- AKS runbooks
- Terraform docs
- Pipeline RCAs
- user question
- vector index
- Ollama

---

## Next Lesson Kyu?

Retriever ne chunks de diye—but raw chunks ko LLM ko exactly kaise dena hai?

Next: **Building Context for the LLM**.
