# Module 4 — Practical Labs

> **Goal:** embeddings aur vector search ko black box ki tarah use nahi karna. Har lab previous concept par build karega.

Full practical sequence: [`../PRACTICAL-ROADMAP.md`](../PRACTICAL-ROADMAP.md)

---

## Setup

```powershell
cd Module-4\examples
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

First run par local embedding model download ho sakta hai.

---

# Zero-to-Hero Runnable Progression

```text
V1  01_cosine_similarity.py
    Vector similarity intuition
      ↓
V2  02_simple_semantic_search.py
    First semantic search
      ↓
V3  03_chromadb_search.py
    Vector store workflow
      ↓
V4  04_faiss_search.py
    Explicit FAISS index/search
      ↓
V5  05_devops_knowledge_base.py
    Real Markdown knowledge base
      ↓
V6  06_dual_provider_embeddings.py
    Local vs OpenAI embeddings
      ↓
V7  07_chunking_experiment.py
    Giant vs paragraph vs tiny chunks
      ↓
V8  08_metadata_filtering.py
    Metadata/filtering boundary
      ↓
V9  09_retrieval_eval.py
    Labelled Hit@K evaluation
      ↓
V10 10_search_only_assistant.py
    Final search-only DevOps assistant
```

---

# What Each Stage Must Teach

## V1 — Cosine Similarity
Learn:
- vectors can be compared numerically
- score is not probability/confidence

## V2 — Semantic Search
Change query wording while preserving meaning and inspect ranking.

## V3 — ChromaDB
Learn collection, IDs, documents, embeddings and vector queries.

## V4 — FAISS
Inspect dimensions, normalized `float32` vectors, `IndexFlatIP`, `index.add()` and `index.search()`.

## V5 — DevOps Knowledge Base
Load real Markdown docs, chunk them, attach source/chunk IDs and query them.

## V6 — Provider Embedding Comparison
Compare SentenceTransformer/local embeddings and OpenAI hosted embeddings.

Important:
```text
Different embedding model/dimension
→ different vector space
→ re-embed/re-index required
```

## V7 — Chunking Experiment
Compare giant, paragraph and tiny chunks. Decide which result gives enough context with least noise.

## V8 — Metadata Filtering
Filter by environment/team/source and remember:
```text
metadata filter != authorization
```

## V9 — Retrieval Evaluation
Use a labelled test set and measure Hit@K instead of judging one impressive query.

## V10 — Search-Only Assistant
Final Module 4 system must:
1. load docs
2. chunk
3. embed
4. accept query
5. rank results
6. print source + chunk ID + score + text
7. **not call an LLM yet**

Module 4 intentionally stops at retrieval.

---

# Failure Tests

Do these intentionally:

1. Submit empty query.
2. Temporarily rename `sample_docs` and observe error.
3. Add an empty Markdown file.
4. Add duplicate content and observe duplicate retrieval.
5. Add an unrelated document and see whether ranking remains sensible.
6. Change query wording while keeping meaning similar.
7. Use a bad metadata filter and observe zero candidates.
8. Try mixing embeddings from different models and explain why dimensions/vector spaces matter.

---

# Key Principles

```text
Embedding != LLM
Vector index != embedding model
Retrieved document != proven incident root cause
Similarity score != factual confidence
Metadata filter != authorization
Retrieval != generation
```

---

# Module 4 Completion Check

You are ready for Module 5 when you can explain without notes:

```text
Why external knowledge?
What is an embedding?
What is a vector?
How is similarity calculated conceptually?
What does Top-K mean?
Why use a vector index?
What is chunking?
Why attach metadata?
What is indexing vs retrieval?
How do we evaluate retrieval?
Why does Module 4 intentionally avoid LLM generation?
```

Then Module 5 adds the missing generation step:

```text
Question
   ↓
Retrieve Knowledge
   ↓
Build Grounded Context
   ↓
LLM
   ↓
Validate Answer + Sources
```
