# Module 4 — Zero-to-Hero Practical Roadmap

> Goal: raw text se semantic search/knowledge base tak complete retrieval pipeline samajhna, before RAG generation is introduced in Module 5.

## Setup
```powershell
cd Module-4/examples
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## V1 — Vector Intuition Without Database
Create 3 tiny numeric vectors manually and compare dot products/cosine intuition.

Then run: `01_cosine_similarity.py`

**Goal:** similarity number ko magic confidence score na samajhna.

---

## V2 — First Semantic Search
Run: `02_simple_semantic_search.py`

Change query wording while keeping meaning same.

Example:
- `AKS network problem`
- `Kubernetes subnet connectivity issue`

Observe semantic retrieval behavior.

---

## V3 — ChromaDB Search
Run: `03_chromadb_search.py`

Understand:
```text
Document
→ Embedding
→ Store
→ Query embedding
→ Similarity lookup
```

---

## V4 — FAISS Search
Run: `04_faiss_search.py`

Compare Chroma vs FAISS responsibilities. Do not treat index and embedding model as same component.

---

## V5 — Chunking Experiment
Take one long runbook and index it as:
1. one giant chunk
2. paragraph chunks
3. very tiny line chunks

Ask same query.

Record which version retrieves enough context without noise.

---

## V6 — Metadata / Filtering Experiment
Add fields such as:
```text
environment=production
team=platform
source=aks-runbook
version=v3
```

Retrieve with and without filter.

**Critical rule:** metadata filter is not authorization.

---

## V7 — DevOps Knowledge Base
Run: `05_devops_knowledge_base.py`

Use sample docs and test at least 5 questions:
- AKS networking
- Terraform networking
- pipeline failure
- unrelated question
- exact identifier lookup

---

## V8 — Local vs Hosted Embeddings
Run: `06_dual_provider_embeddings.py`

Compare local SentenceTransformer route vs OpenAI embeddings route.

**Important:** embedding dimensions/models differ; never mix vectors from different models in one unchanged index.

---

## V9 — Retrieval Quality Test Set
Create 10 labelled questions with expected source documents.

Measure simple Hit@K manually:
```text
Did expected source appear in top K? yes/no
```

Tune chunking/top-k only after looking at failures.

---

## V10 — Search-Only DevOps Knowledge Assistant
Build a small CLI that:
1. loads docs
2. chunks them
3. embeds/indexes them
4. accepts a question
5. retrieves top results
6. prints score + source + chunk ID
7. does **not** call an LLM yet

### Acceptance Criteria
Learner can explain:
```text
Embedding != database
Vector DB/index != LLM
Similarity != confidence
Retrieval != generation
Metadata filter != authorization
```

## Hero Outcome
Learner Module 5 me RAG start karte waqt already knows how trustworthy context is retrieved.
