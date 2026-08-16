# Module 4 — Practical Labs

> **Goal:** embeddings aur vector search ko black box ki tarah use nahi karna. Har lab previous concept par build karega.

---

## Setup

```powershell
cd Module-4\examples
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

First run par embedding model download ho sakta hai.

---

# Practical Progression

```text
V1  → Vector similarity intuition
V2  → First semantic search
V3  → Multiple DevOps documents ranking
V4  → Chroma collection search
V5  → FAISS vector index
V6  → Real Markdown document loading
V7  → Paragraph-aware chunking
V8  → Source/chunk metadata mapping
V9  → Query validation + Top-K retrieval
V10 → End-to-end DevOps knowledge base
```

The repository scripts combine some adjacent stages so you do not maintain ten artificial files just for tiny differences.

---

## Lab 01 — Cosine Similarity

File:

```text
01_cosine_similarity.py
```

Learn:

- vectors can be compared numerically
- cosine similarity direction intuition
- score is not probability

Run:

```powershell
python .\01_cosine_similarity.py
```

Homework:

- add one unrelated vector/text example
- predict which pair should be most similar before running

---

## Lab 02 — Simple Semantic Search

File:

```text
02_simple_semantic_search.py
```

Learn:

```text
Documents → Embeddings
Query → Embedding
Cosine comparison
Rank results
```

Run:

```powershell
python .\02_simple_semantic_search.py
```

Try queries:

```text
Kubernetes networking problem
Terraform state is locked
Docker runner has no disk space
```

Do not focus only on exact score; inspect ranking quality.

---

## Lab 03 — ChromaDB

File:

```text
03_chromadb_search.py
```

Learn:

- collection
- IDs
- documents
- embeddings
- vector query
- higher-level vector store workflow

Run:

```powershell
python .\03_chromadb_search.py
```

Exercise:

- add metadata such as `service=aks`
- experiment with supported metadata filtering

---

## Lab 04 — FAISS

File:

```text
04_faiss_search.py
```

Learn:

- vector matrix
- dimensions
- `float32`
- `IndexFlatIP`
- normalized embeddings
- `index.add()`
- `index.search()`
- mapping returned indices back to documents

Run:

```powershell
python .\04_faiss_search.py
```

Debug checklist:

```text
vectors.shape
vectors.dtype
index.ntotal
query_vector.shape
k <= number of records
```

---

# Lab 05 — Complete DevOps Knowledge Base

File:

```text
05_devops_knowledge_base.py
```

Source folder:

```text
sample_docs/
├── aks-networking.md
├── terraform-state.md
├── pipeline-failure.md
└── docker-build.md
```

Full flow:

```text
Markdown Files
      ↓
Load + Validate
      ↓
Paragraph-aware Chunking
      ↓
Stable Record Mapping
      ↓
Sentence Embeddings
      ↓
FAISS Index
      ↓
CLI Query
      ↓
Query Embedding
      ↓
Top-K Search
      ↓
Rank + Source + Chunk ID + Score + Text
```

Run:

```powershell
python .\05_devops_knowledge_base.py
```

Recommended test queries:

```text
AKS pods cannot connect after NSG rule change
Terraform state is locked and apply cannot continue
Pipeline deployment failed during Terraform Apply
Docker build runner is out of disk space
```

---

# What You Must Observe

For each query write down:

```text
Expected source
Actual rank 1 source
Was expected source in Top-3?
Any irrelevant result?
Why might retrieval be imperfect?
```

Example evaluation sheet:

| Query | Expected | Top-1 | In Top-3? |
|---|---|---|---|
| NSG blocked pods | aks-networking.md | ... | ... |
| state locked | terraform-state.md | ... | ... |
| apply failed | pipeline-failure.md | ... | ... |
| disk full build | docker-build.md | ... | ... |

This is your first retrieval evaluation dataset.

---

# Failure Tests

Do these intentionally:

1. Submit empty query.
2. Temporarily rename `sample_docs` and observe error.
3. Add an empty Markdown file.
4. Add duplicate content and observe duplicate retrieval.
5. Add an unrelated document and see whether ranking remains sensible.
6. Change query wording while keeping meaning similar.

---

# Key Principle

```text
Retrieved document ≠ proven incident root cause
```

Semantic search finds **relevant knowledge candidates**. Current incident truth still requires live evidence, tool output and validation.

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
How does the final DevOps knowledge-base script work?
```

Then Module 5 will add the missing generation step:

```text
Question
   ↓
Retrieve Knowledge
   ↓
Put Retrieved Knowledge in LLM Context
   ↓
Grounded Answer
```
