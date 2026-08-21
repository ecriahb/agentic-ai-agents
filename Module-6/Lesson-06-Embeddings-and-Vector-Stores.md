# 🚩 Jai Bajrangbali!

# Lesson 06 — Embeddings & Vector Stores in LangChain

> **Module 4 ke vector-search concepts same rahenge; framework sirf standard interfaces aur integrations provide karega.**

> No new vector theory is introduced here. The learning objective is adapter choice, interface compatibility and framework code that preserves Module 4's indexing/retrieval contract.

---

# 🎯 Lesson Goal

Aap samjhoge:
- embedding abstraction kya karti hai
- vector store abstraction kya karti hai
- indexing vs querying flow
- same embedding model compatibility kyu important hai
- FAISS/Chroma integration ka mental model
- framework abstraction ke peeche actual vector operations kya hain

---

# PART 1 — Mental Model

```text
Chunks
 ↓
Embedding Component
 ↓
Vectors
 ↓
Vector Store
 ↓
Similarity Search
```

Framework version:

```text
Document objects
 ↓
Embeddings wrapper
 ↓
VectorStore integration
 ↓
Retriever/search interface
```

---

# PART 2 — English Definitions

An **embedding integration** provides a standard interface for converting text into numeric vectors.

A **vector store integration** connects LangChain components to a vector index/database used for similarity-based retrieval.

---

# PART 3 — Under the Hood

Even if code becomes:

```python
vectorstore = FAISS.from_documents(chunks, embeddings)
```

underlying conceptual work remains:

```text
for each chunk:
  text → embedding vector
  vector → index
  metadata → mapping/store
```

Framework does not remove vector mathematics.

---

# PART 4 — Example with Local Embeddings

One practical route is a local Hugging Face embedding wrapper.

Conceptual code:

```python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embeddings.embed_query("AKS subnet connectivity issue")
print(len(vector))
```

Expected:

```text
one numeric vector
```

Dimension depends on model.

---

# PART 5 — FAISS Vector Store

Conceptual example:

```python
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(chunks, embeddings)

results = vectorstore.similarity_search(
    "AKS deployment failed after NSG change",
    k=3,
)
```

Returned values are typically documents/chunks, not just raw vector indices.

Benefit:

```text
text + metadata stay associated with vector search result
```

---

# PART 6 — Chroma Concept

Alternative integration:

```text
Documents
 ↓
Embedding function
 ↓
Chroma collection
 ↓
search/query
```

Different stores have different persistence, filtering and scaling characteristics.

Framework common interface does not make them architecturally identical.

---

# PART 7 — Same Embedding Space Rule

Indexing:

```text
all-MiniLM-L6-v2 → document vectors
```

Querying should use compatible same space:

```text
all-MiniLM-L6-v2 → query vector
```

Changing embedding model without rebuilding index can invalidate retrieval assumptions.

Production metadata should record:

```text
embedding_model
embedding_version
dimension
index_version
```

---

# PART 8 — Similarity Search vs Retriever

Vector store can expose direct search:

```text
vectorstore.similarity_search(...)
```

Retriever abstraction turns search into a standardized retrieval component:

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
```

Next lesson me retriever deeply use hoga.

---

# PART 9 — DevOps Example

Knowledge base:

```text
aks-networking.md
terraform-networking.md
pipeline-failure.md
rollback.md
```

Question:

```text
Pods cannot reach internal service after Terraform networking change
```

Expected:

```text
AKS networking + Terraform networking chunks rank high
Docker build doc rank low
```

If not, investigate:

```text
chunking
embedding model
query wording
metadata filters
index freshness
```

---

# PART 10 — Persistence

Learning demo may rebuild index every run.

Production questions:

```text
Where is index persisted?
How is it refreshed?
How are deletions handled?
How are versions rolled back?
How do replicas stay consistent?
```

Framework does not answer all of these automatically.

---

# PART 11 — Filtering

Metadata filters can narrow retrieval:

```text
environment=production
team=platform
status=approved
```

But repeat critical principle:

```text
metadata filtering != authorization
```

Unauthorized documents should be excluded by access-control policy before/within retrieval.

---

# PART 12 — Common Mistakes

- vector store abstraction ko database architecture samajh lena
- embedding model change and no re-index
- `k=3` blindly production constant bana dena
- similarity score meaning universal assume karna
- source metadata discard karna
- vector DB me secrets store karna

---

# PART 13 — Interview Q&A

### Q1. What does LangChain add over raw FAISS?
A document-centric integration and standardized interfaces that connect embeddings, vector stores and retrievers with other application components.

### Q2. Does switching vector stores require no code/architecture changes?
Not necessarily. Common interfaces reduce integration changes, but filtering, persistence, scaling and scoring behavior remain store-specific.

### Q3. Why record embedding model version?
Because indexed and query vectors must share a compatible semantic space, and model changes often require re-indexing.

---

# PART 14 — Revision

```text
Embedding wrapper = text → vector interface
Vector store = vectors + document association + search
Retriever = query → documents interface
```

---

# PART 15 — Homework

Design index metadata for a production DevOps KB:

```text
index_version
embedding_model
source_version
created_at
owner
classification
```

Explain which fields are operational, retrieval-related, and security-related.

---

# 🔁 Next Lesson Kyu?

Ab searchable vector store ready hai. Next direct search ko **Retriever** abstraction me convert karke complete **RAG chain** banayenge.
