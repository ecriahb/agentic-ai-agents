# 🚩 Jai Bajrangbali!

# Lesson 11 — Production RAG for DevOps

> **Local demo me answer mil jana start hai. Production RAG me security, freshness, observability, cost, reliability aur governance equally important hain.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- local RAG vs production RAG
- source governance
- document lifecycle and freshness
- incremental indexing
- authentication and authorization
- tenant/team isolation
- secret handling
- retrieval and LLM observability
- caching
- resilience/timeouts/retries
- cost and latency controls
- auditability
- deployment architecture
- safe DevOps action boundary

---

# PART 1 — Local Demo vs Production System

Local:

```text
Markdown files
→ FAISS
→ Ollama
→ terminal answer
```

Production may need:

```text
Multiple knowledge sources
Identity
ACLs
Versioning
Incremental ingestion
Vector service
Reranker
LLM gateway
Monitoring
Evaluation
Audit logs
High availability
```

Productionization means system behavior operationally trustworthy banana.

---

# PART 2 — Reference Architecture

```text
                    KNOWLEDGE PLANE

Approved Sources
  │
  ├── Runbooks
  ├── Wiki / Docs
  ├── RCAs
  ├── Terraform Standards
  └── Pipeline SOPs
          ↓
     Ingestion Service
          ↓
 Clean / Chunk / Metadata / ACL
          ↓
      Embedding Service
          ↓
      Vector / Search Index


                     QUERY PLANE

User / DevOps Portal
        ↓
 Authentication
        ↓
 Authorization Context
        ↓
 Query Validation
        ↓
 Retrieval Filters
        ↓
 Vector + Keyword Search
        ↓
 Rerank / Threshold
        ↓
 Context Builder
        ↓
 LLM Gateway
        ↓
 Output Validation
        ↓
 Answer + Sources
        ↓
 Audit / Metrics
```

---

# PART 3 — Source Governance

Before a source becomes searchable:

```text
Who owns it?
Who approves it?
What classification?
What retention policy?
What version?
What status?
Who may access it?
When should it expire?
```

Metadata example:

```json
{
  "owner": "platform-team",
  "classification": "internal",
  "status": "approved",
  "version": "2026-08",
  "valid_from": "2026-08-01",
  "environment": "production"
}
```

---

# PART 4 — Freshness & Incremental Indexing

Bad model:

```text
Rebuild entire corpus manually once a year
```

Better:

```text
Source change detected
      ↓
Identify changed document
      ↓
Delete/expire old chunks
      ↓
Re-chunk changed document
      ↓
Re-embed
      ↓
Update index
```

Store content hash:

```text
same hash → no re-index
changed hash → process
```

Freshness is operational correctness.

## Azure AI Search Production Mapping

For an Azure implementation, map the local FAISS/Chroma pipeline to an Azure AI Search index rather than treating the managed service as a magic vector database:

```text
Approved runbook/source
       -> ingestion and enrichment
       -> searchable text + vector fields + ACL metadata
       -> keyword/vector or hybrid query
       -> security filter before model context
       -> citation and freshness validation
```

The index contract must define the embedding model and dimensions, searchable/vector fields, metadata filters, source version, owner, classification, and deletion behavior. Hybrid retrieval is useful when an incident contains exact identifiers such as `aks-subnet-allow`, while vector retrieval helps with paraphrased symptoms.

Exercise the service boundary with a local fixture even without Azure credentials:

1. Index a Terraform diff, an AKS networking runbook, and an unrelated Docker runbook.
2. Query with both an exact rule name and a paraphrased networking symptom.
3. Apply a team/classification filter before constructing model context.
4. Delete the Terraform source and prove that old chunks are not returned.
5. Record query latency, hit@k, freshness, filter decision, and citation IDs.

In Azure, private endpoints, managed identity, index access policy, diagnostic settings, and regional data requirements belong to the deployment design. The model must never be asked to hide a document that the retrieval layer already returned without authorization.

---

# PART 5 — Authentication vs Authorization

Authentication:

```text
Who are you?
```

Authorization:

```text
Which sources/chunks may you retrieve?
```

Wrong:

```text
retrieve all docs
→ ask model to hide unauthorized information
```

Correct:

```text
identity
→ policy/ACL
→ permitted retrieval scope
→ model sees only permitted context
```

---

# PART 6 — Multi-Team / Tenant Isolation

Metadata:

```text
team = payments
team = platform
team = security
```

User from platform team should not automatically retrieve restricted security incident docs.

Possible controls:

```text
separate collections/indexes
ACL metadata filters
data-layer authorization
service identity boundaries
```

Do not rely on prompt instructions for isolation.

---

# PART 7 — Secrets and Sensitive Data

Never casually index:

```text
API keys
passwords
private keys
access tokens
customer secrets
connection strings
```

Ingestion pipeline should support:

```text
classification
secret scanning
redaction/exclusion
approved source allowlist
```

If sensitive data enters context, LLM controls are already too late.

---

# PART 8 — LLM Gateway Pattern

Instead of every service calling model directly:

```text
RAG App
  ↓
LLM Gateway
  ↓
Model Provider / Ollama / Azure OpenAI / etc.
```

Gateway can centralize:

```text
timeouts
retries
model selection
rate limits
logging
cost tracking
redaction
policy
```

---

# PART 9 — Resilience

Possible failures:

```text
embedding service unavailable
vector DB unavailable
LLM timeout
429/rate limit
source connector failure
malformed model output
```

Design explicit behavior:

```text
retrieval unavailable → do not pretend no evidence exists
LLM unavailable → return retrievable sources without generated answer if useful
validation failure → flag/retry safely
```

---

# PART 10 — Timeout & Retry Policy

Not every failure should be retried.

Potentially retryable:

```text
429
transient 5xx
network timeout
```

Usually not fixed by retry:

```text
401 authentication
403 authorization
invalid request/schema
```

Use:

```text
bounded retries
exponential backoff
jitter
idempotent operations
```

---

# PART 11 — Observability

Trace one query:

```text
request_id
user/team
query hash/text policy
retrieved chunk IDs
scores
filters applied
context size
model
latency
validation status
final source IDs
```

Metrics:

```text
retrieval_latency_ms
llm_latency_ms
no_context_rate
invalid_citation_rate
retrieval_hit_rate from eval
request_error_rate
index_freshness_age
```

---

# PART 12 — Logging Safety

Do not log everything blindly.

Avoid:

```text
raw secrets
full confidential docs
access tokens
complete sensitive prompts
```

Prefer structured safe logs:

```text
request_id
source IDs
status
latency
model name
policy result
```

with controlled access.

---

# PART 13 — Cost & Latency Controls

Cost/latency drivers:

```text
embedding volume
retrieval candidate count
reranker calls
context size
LLM input/output tokens
multi-query count
```

Optimization examples:

```text
incremental indexing
embedding cache
query cache where safe
small retrieval K
rerank only when needed
bounded context
appropriate model tier
```

---

# PART 14 — Caching

Possible caches:

```text
document embeddings
query embeddings
retrieval results
final answers
```

But caching has freshness/security risks.

Never serve cached answer across users if source authorization differs.

Cache key may need:

```text
normalized query
user authorization scope
index version
model/prompt version
```

---

# PART 15 — Prompt & Model Versioning

Store:

```text
prompt_version = rag-v5
embedding_model = ...
reranker_version = ...
generation_model = ...
index_version = ...
```

Why?

When regression appears, you need to know which component changed.

---

# PART 16 — Deployment Strategy

For a service:

```text
Containerized RAG API
        ↓
AKS / App Service
        ↓
Private network where needed
        ↓
Managed identity / workload identity
        ↓
Vector DB + document sources
        ↓
LLM endpoint
```

CI/CD should run:

```text
unit tests
retrieval eval subset
security scans
prompt/schema tests
integration tests
```

before promotion.

---

# PART 17 — Production RAG and Actions

Knowledge assistant:

```text
Read → Retrieve → Analyze → Recommend
```

Agent with actions:

```text
Read → Analyze → Propose Action
             ↓
       Policy Validation
             ↓
       Human Approval
             ↓
       Controlled Tool
```

Do not jump directly from RAG answer to production mutation.

---

# PART 18 — SLO Thinking

Possible service goals:

```text
99.9% API availability
p95 retrieval latency < target
index freshness < 30 minutes
invalid citation rate < threshold
no-context false-positive rate monitored
```

Quality SLOs may be harder than infrastructure SLOs but should still be measured.

---

# PART 19 — Production Checklist

```text
[ ] approved sources only
[ ] secret scanning
[ ] ownership metadata
[ ] document versions
[ ] incremental indexing
[ ] authorization before retrieval
[ ] retrieval evaluation
[ ] grounded prompt
[ ] citation validation
[ ] explicit failure statuses
[ ] safe logs
[ ] metrics/tracing
[ ] model/prompt versioning
[ ] bounded retries/timeouts
[ ] read-only first
[ ] human approval for destructive actions
```

---

# PART 20 — Common Mistakes

1. Local FAISS script ko directly enterprise architecture samajhna.
2. ACL only prompt me define karna.
3. Stale documents never delete karna.
4. Full sensitive context logs me dump karna.
5. Multi-query/reranker without latency measurement.
6. Prompt/model changes version na karna.
7. Cached answers authorization scope ke bina reuse karna.
8. RAG answer se direct production action execute karna.

---

# PART 21 — Interview Corner

### Q1. What is the biggest security rule for enterprise RAG?

Enforce authorization before retrieval so unauthorized content never enters model context.

### Q2. Why is incremental indexing important?

It keeps the knowledge index current without rebuilding the entire corpus for every small change.

### Q3. What should be observable in RAG?

Retrieval sources/scores, context size, component latency, model/prompt versions, validation outcomes and failure states.

### Q4. Why version prompts and indexes?

To reproduce behavior, investigate regressions and safely roll out changes.

### Q5. Why separate RAG from action execution?

RAG produces information/recommendations; operational mutations need additional policy, validation and approval controls.

---

# PART 22 — Revision

```text
Production RAG =
Knowledge Governance
+ Fresh Index
+ Identity/ACL
+ Retrieval Quality
+ Grounding
+ Validation
+ Resilience
+ Observability
+ Safe Operations
```

---

# PART 23 — Homework

Design a production architecture for:

```text
Internal DevOps Knowledge Assistant
```

Include:

1. sources
2. ingestion
3. vector/search store
4. authentication
5. authorization
6. LLM access
7. logging/metrics
8. evaluation
9. failure handling
10. human approval boundary

---

# 🔗 Why Lesson 12 Next?

Ab individual concepts complete hain. Final lesson me hum sab combine karenge:

```text
Documents
→ Retrieval
→ Quality Gate
→ Context
→ Grounded Generation
→ Citations
→ Validation
→ Evaluation
```

into one **DevOps RAG Knowledge Assistant mini-project**.
