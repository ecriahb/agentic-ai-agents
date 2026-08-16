# 🚩 Jai Bajrangbali!

# Lesson 05 — Document Loaders & Text Splitters

> **RAG quality starts before retrieval: source loading, metadata and chunk boundaries must be correct.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- loader kya karta hai
- document object kya represent karta hai
- metadata preservation kyu important hai
- text splitter/chunking orchestration me kahan fit hota hai
- source-aware ingestion kaise design karte hain
- ingestion failure aur data-quality risks

---

# PART 1 — English Definitions

A **document loader** converts source content into standardized document objects containing text plus metadata.

A **text splitter** divides large documents into smaller chunks while preserving enough context for downstream embedding and retrieval.

---

# PART 2 — Ingestion Mental Model

```text
Files / Pages / Records
        ↓
Document Loader
        ↓
Document(text, metadata)
        ↓
Text Splitter
        ↓
Chunks + inherited metadata
        ↓
Embedding / Indexing
```

---

# PART 3 — Why Standard Document Objects?

Instead of passing random tuples/dicts everywhere, standardized document representation helps downstream components consume:

```text
page_content
metadata
```

Metadata examples:

```text
source
team
environment
version
updated_at
classification
```

Traceability Module 5 se same principle hai.

---

# PART 4 — Loader Practical

Conceptual example:

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample_docs/aks-networking.md", encoding="utf-8")
docs = loader.load()

for doc in docs:
    print(doc.page_content[:200])
    print(doc.metadata)
```

Expected:

```text
content loaded
source metadata preserved
```

---

# PART 5 — Splitter Practical

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=80,
)

chunks = splitter.split_documents(docs)
```

Mental model:

```text
1 document
 ↓
multiple Document chunks
 ↓
source metadata retained
```

---

# PART 6 — Recursive Splitting Intuition

A recursive splitter generally tries meaningful separators before falling back to smaller boundaries.

Conceptually:

```text
paragraph
 ↓ if too large
line
 ↓ if too large
word/character boundary
```

Goal perfect semantics guarantee karna nahi; destructive arbitrary splitting reduce karna hai.

---

# PART 7 — DevOps Chunk Example

Bad split:

```text
Chunk A:
If AKS connectivity fails after NSG change, verify

Chunk B:
the required subnet allow rules and routes.
```

Important instruction split ho gayi.

Better chunk:

```text
If AKS connectivity fails after NSG change,
verify the required subnet allow rules and routes.
```

Retrieval quality improves.

---

# PART 8 — Metadata Enrichment

Loader-provided metadata often enough nahi hota.

Application can enrich:

```python
for doc in docs:
    doc.metadata["environment"] = "production"
    doc.metadata["team"] = "platform"
```

But metadata must come from trusted source/policy—not LLM invention.

---

# PART 9 — Security Boundary

Before indexing:

```text
secret scanning
PII classification
ACL tagging
source validation
staleness/version check
```

Do not assume:

```text
loaded successfully = safe to index
```

---

# PART 10 — Ingestion Failures

Examples:

```text
file missing
unsupported encoding
empty content
duplicate content
huge binary accidentally loaded
stale document
secret included
metadata missing
```

These should be explicit states.

---

# PART 11 — Idempotent Indexing

Production ingestion should think about stable IDs:

```text
source + version + chunk number
```

So re-indexing can update rather than blindly duplicate.

Example:

```text
aks-networking:v3:chunk-004
```

---

# PART 12 — Common Mistakes

- loading every file recursively without allowlist
- metadata lost during splitting
- chunk overlap huge rakhna and creating duplication
- source/version not storing
- secrets index kar dena
- PDF/text extraction quality inspect na karna

---

# PART 13 — Interview Q&A

### Q1. What does a document loader do?
It normalizes source content into document objects containing text and metadata.

### Q2. Why preserve metadata after splitting?
For filtering, source traceability, versioning, ACL decisions and citations.

### Q3. Is chunk size universal?
No. It should be evaluated against source structure, embedding model, retrieval task and context budget.

### Q4. What is the security risk in ingestion?
Sensitive or unauthorized content can become searchable if indexing occurs before classification and access controls.

---

# PART 14 — Revision

```text
Loader = source → documents
Splitter = documents → chunks
Metadata = traceability/filtering context
ACL = authorization, not just metadata display
```

---

# PART 15 — Homework

Take an AKS troubleshooting runbook and design metadata:

```text
source
owner
environment
version
updated_at
access_group
```

Then choose a chunking strategy and explain why.

---

# 🔁 Next Lesson Kyu?

Chunks ready hain. Next unhe **embeddings + vector store** ke through searchable representation me convert karenge.
