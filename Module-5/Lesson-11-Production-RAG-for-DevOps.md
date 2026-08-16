# Lesson 11 — Production RAG for DevOps

> **Production RAG sirf embeddings + LLM nahi hai; knowledge freshness, access control, observability, security and failure handling equally important hain.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- production knowledge lifecycle
- document freshness/versioning
- RBAC and tenant boundaries
- secret handling
- prompt injection risk
- observability
- caching and cost
- failure modes
- safe deployment architecture

---

## English Definition

A **production RAG system** is a retrieval-and-generation application that manages knowledge freshness, authorization, security, reliability, observability and quality controls in addition to retrieval relevance.

---

# PART 1 — Production Architecture

```text
Trusted Knowledge Sources
        ↓
Ingestion Pipeline
        ↓
Validation / Sanitization
        ↓
Chunk + Metadata
        ↓
Embeddings
        ↓
Versioned Index
        ↓
Authorized User Query
        ↓
Identity / RBAC
        ↓
Filtered Retrieval
        ↓
Context Guardrails
        ↓
LLM
        ↓
Schema / Citation Validation
        ↓
Answer + Audit Trail
```

---

# PART 2 — Knowledge Freshness

DevOps procedures change.

Old runbook:

```text
Use pipeline-v1 for rollback.
```

New runbook:

```text
pipeline-v1 retired; use deployment-controller.
```

If stale content remains searchable, RAG can confidently return obsolete instructions.

Useful metadata:

```text
version
status
last_updated
valid_from
valid_until
owner
```

Possible policy:

```text
status=active only
```

---

# PART 3 — Source Governance

Not every document should be indexed automatically.

Potential dangerous sources:

- temporary chat dump
- unreviewed draft
- secrets/config exports
- generated AI notes
- deprecated runbooks
- user-uploaded malicious content

Ingestion should classify source trust.

Example:

```text
Tier 1 → approved runbook
Tier 2 → reviewed incident RCA
Tier 3 → informal troubleshooting note
```

Answer can prefer higher-authority sources.

---

# PART 4 — Authorization Before Retrieval

Critical principle:

```text
Retrieve only what user is allowed to see.
```

Bad architecture:

```text
Search all docs
   ↓
Retrieve secret/private chunk
   ↓
Try to hide it later
```

Better:

```text
User Identity
   ↓
Access Scope
   ↓
Metadata / ACL Filter
   ↓
Authorized Retrieval
```

Security must happen before sensitive content reaches LLM context.

---

# PART 5 — Metadata Filter Is Not Full Authorization

Metadata helps:

```text
team=payments
environment=prod
classification=internal
```

But real security requires trusted identity + policy enforcement.

Never rely on user-supplied metadata alone:

```text
user says team=admin
```

Host application must derive permission from authenticated identity.

---

# PART 6 — Secrets

Never intentionally embed/store secrets such as:

- API keys
- passwords
- connection strings
- tokens
- private keys

Why?

Because vector DB and retrieval context become another sensitive storage/exposure path.

Ingestion pipeline can add:

```text
secret scanning
redaction
source allowlist
classification checks
```

---

# PART 7 — Observability

Log enough to debug quality without leaking secrets.

Useful fields:

```text
request_id
user_scope
original_query
rewritten_query
retrieved_chunk_ids
scores
source_versions
threshold decision
model name
latency
answer status
citation validation result
```

Avoid raw secret-containing prompts in logs.

---

# PART 8 — Latency Breakdown

RAG request latency may include:

```text
query rewrite
embedding
vector search
reranking
context building
LLM generation
validation
```

Measure separately.

Example:

```text
Embedding: 40 ms
Search: 15 ms
Rerank: 120 ms
LLM: 1800 ms
```

Now optimization becomes evidence-based.

---

# PART 9 — Cost Controls

Cloud-based RAG cost may come from:

- embedding calls
- generation tokens
- reranking service
- vector DB
- storage/network

Controls:

```text
incremental indexing
embedding cache
small relevant context
response limits
query/result cache where safe
```

But cache must respect access scopes and freshness.

---

# PART 10 — Failure Handling

What if vector DB unavailable?

```text
Do not silently answer from model memory as if grounded.
```

Return explicit degraded status:

```text
Knowledge retrieval is unavailable; I cannot provide a grounded internal answer right now.
```

Other failures:

- embedding timeout
- LLM timeout
- malformed model output
- stale index
- authorization service failure

Fail safely.

---

# PART 11 — Production DevOps Use Case

```text
On-call Engineer
      ↓
SSO Identity
      ↓
Authorized Project Scope
      ↓
Query: "How do I validate AKS private DNS after PE change?"
      ↓
Retrieve active project runbooks only
      ↓
Rerank
      ↓
Context with source/version
      ↓
Grounded LLM
      ↓
Answer + citations
      ↓
No automatic production changes
```

---

# PART 12 — Read-Only First

Knowledge assistant should initially:

```text
Search
Explain
Summarize
Recommend
```

not automatically:

```text
Delete
Apply
Restart
Rollback
Rotate
```

Later agentic remediation requires separate tool permissions and approval architecture.

---

## Common Mistakes

- index every available document
- stale docs remain active
- authorization after retrieval
- secrets embedded
- retrieval outage falls back to ungrounded answer
- no source/version logs
- cache leaks cross-user results
- RAG answer wired directly to write operations

---

## Interview Corner

**Q: What are the biggest production concerns in RAG?**

Knowledge freshness, access control, source trust, secret protection, retrieval quality, prompt injection, observability, latency, cost and safe failure behavior.

**Q: Where should authorization happen?**

Before or during retrieval so unauthorized content never enters the model context.

---

## Revision

```text
Production RAG
= Retrieval
+ Freshness
+ RBAC
+ Security
+ Observability
+ Evaluation
+ Safe Failure
```

---

## Homework

Design a production policy for internal RAG with:

- Dev / Stage / Prod documents
- two application teams
- deprecated runbooks
- confidential RCA docs

Explain how retrieval filters should work.

---

## Next Lesson Kyu?

All concepts ready hain. Ab complete system build karna hai:

**DevOps RAG Knowledge Assistant**.
