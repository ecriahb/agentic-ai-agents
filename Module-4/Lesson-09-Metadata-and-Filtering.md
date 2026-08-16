# 🚩 Lesson 09 — Metadata & Filtering

> **Semantic similarity batata hai “meaning close hai”; metadata batata hai “ye result kis source, environment, version aur scope ka hai.”**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- metadata kya hai
- chunk metadata kyu important hai
- semantic search + metadata filter ka combination
- environment/service/version/source filters
- traceability and citations
- metadata filtering vs authorization
- practical filtering patterns
- stale version problems

---

# PART 1 — Metadata Definition

**English Definition:**
> Metadata is structured information that describes a document or chunk, such as its source, environment, service, version, owner, date or access scope.

Example:

```json
{
  "source": "aks-networking.md",
  "service": "aks",
  "environment": "prod",
  "version": "v4",
  "section": "nsg-checks"
}
```

Text = knowledge. Metadata = knowledge ke baare me structured information.

---

# PART 2 — Why Similarity Alone Is Not Enough

Suppose query:

```text
How do I fix AKS network connectivity?
```

Search returns:

```text
1. dev AKS old runbook v1
2. prod AKS current runbook v4
3. retired cluster migration notes
```

All semantically similar ho sakte hain.

But you may want:

```text
environment = prod
status = current
service = aks
```

Then search scope becomes safer and more relevant.

---

# PART 3 — Filter + Vector Search

Mental model:

```text
All Chunks
   ↓
Metadata Filter
   ↓
Eligible Chunks
   ↓
Vector Similarity Search
   ↓
Top-K
```

Or implementation may combine these internally.

Example intent:

```text
Find semantically similar chunks
WHERE environment = prod
AND service = aks
```

---

# PART 4 — Useful DevOps Metadata

Possible fields:

```text
source
service
environment
region
team
document_type
version
status
created_at
updated_at
incident_id
repository
path
section
confidentiality
```

Do not add metadata just because possible hai. Add fields that support retrieval, governance and traceability.

---

# PART 5 — Source Traceability

Retrieved answer candidate:

```text
Validate outbound NSG rule before redeployment.
```

Without metadata:

```text
Where did this come from? Unknown.
```

With metadata:

```text
source: aks-networking.md
section: Network Validation
version: v4
```

Now later RAG system source references show kar sakta hai.

---

# PART 6 — Chroma-Style Filter Example

Conceptual example:

```python
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3,
    where={"environment": "prod"}
)
```

Then only matching metadata scope ke records candidates banenge, subject to library behavior/configuration.

Multiple field logic depends on the vector store's supported filter syntax, so current docs verify karna important hai.

---

# PART 7 — Versioning Example

Suppose same runbook:

```text
v1 → old firewall route
v2 → temporary workaround
v4 → current approved process
```

If all indexed without status/version strategy:

```text
semantic search → old solution may rank first
```

Better metadata:

```json
{
  "version": "v4",
  "status": "current"
}
```

And ingestion lifecycle should remove/deprecate stale content deliberately.

---

# PART 8 — Metadata Is NOT Authorization

Very important production principle:

```text
where={"team": "payments"}
```

is a retrieval filter.

It is **not automatically a security boundary**.

Authorization must be enforced by trusted application/system logic based on authenticated identity and permissions.

Mental model:

```text
Identity
 ↓
Authorization Policy
 ↓
Allowed corpus / tenant
 ↓
Metadata filter + vector search
```

Never trust user-provided metadata alone for access control.

---

# PART 9 — Multi-Tenant Example

Bad:

```text
User says tenant=A
→ app trusts string
→ searches tenant A
```

Better:

```text
Authenticated user
 ↓
Application resolves allowed tenant IDs
 ↓
Server-side enforced filter
 ↓
Vector search
```

This becomes critical for enterprise RAG.

---

# PART 10 — Practical Data Structure

```python
chunks = [
    {
        "text": "Validate AKS NSG rules...",
        "metadata": {
            "source": "aks-networking.md",
            "service": "aks",
            "environment": "prod",
            "status": "current"
        }
    },
    {
        "text": "Clear Terraform state lock...",
        "metadata": {
            "source": "terraform-state.md",
            "service": "terraform",
            "environment": "prod",
            "status": "current"
        }
    }
]

filtered = [
    c for c in chunks
    if c["metadata"]["service"] == "aks"
]

print(filtered)
```

First Python-side filtering samjho; vector DB filtering iska scalable/managed version ho sakta hai.

---

# PART 11 — Common Mistakes

1. source filename store na karna
2. unstable/meaningless IDs
3. old and current docs mix karna
4. environment metadata inconsistent (`Prod`, `production`, `PROD`)
5. arbitrary free-text metadata without schema
6. metadata filter ko authorization samajhna
7. deleted source ka stale vector retain karna

---

# PART 12 — Metadata Schema Thinking

Define controlled vocabulary:

```text
environment: dev | stage | prod
status: draft | current | deprecated
service: aks | terraform | pipeline | networking
```

This reduces filter bugs.

Useful validation:

```text
required source
required chunk_id
allowed environment values
version format
```

---

# PART 13 — Interview Corner

**Q: Why add metadata to vector records?**  
For filtering, source traceability, versioning, governance and better retrieval scope.

**Q: Is metadata filtering enough for security?**  
No. Authorization must be enforced separately by trusted application/platform controls.

**Q: How can stale documents harm RAG?**  
They can be retrieved as semantically relevant even though their operational guidance is outdated.

---

# PART 14 — Revision

```text
Chunk Text
   +
Metadata
   ↓
Searchable + Traceable Knowledge
```

Remember:

```text
Similarity = relevance signal
Metadata   = scope/context
Authorization = security decision
```

---

# PART 15 — Homework

1. 4 sample docs ke liye metadata schema design karo.
2. `prod + aks + current` filter ka pseudo-code likho.
3. Explain why `environment` filter security control nahi hai.

---

# Next Lesson Kyu?

Ab hum documents ko chunk, embed aur tag kar sakte hain. Ab full lifecycle connect karna hai:

**index kaise build hota hai aur user query ka retrieval flow end-to-end kaise chalta hai?**

# 👉 Lesson 10 — Indexing & Retrieval Flow
