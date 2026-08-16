# Lesson 09 — Metadata & Filtering

> **Semantic similarity batata hai “meaning close hai”; metadata batata hai “ye result allowed/relevant scope me hai ya nahi”.**

## 🎯 Lesson Goal

Metadata ko retrieval control ke liye use karna.

## English Definition

**Metadata** is structured information stored alongside a document or chunk that describes attributes such as source, service, environment, owner, type or timestamp.

## Example

```json
{
  "service": "aks",
  "environment": "production",
  "document_type": "runbook",
  "team": "platform",
  "source": "aks-networking.md"
}
```

## Why Metadata Matters

Query:

```text
AKS deployment connectivity issue
```

Knowledge base me same topic ke docs ho sakte hain:

```text
Dev runbook
Stage experiment
Production approved runbook
Old incident
Current policy
```

Only vector similarity use karoge to semantically close but operationally wrong result aa sakta hai.

Better:

```text
semantic search
+
environment = production
+
service = aks
+
document_type = approved_runbook
```

## Mental Model

```text
Query
 ↓
Metadata Scope
 ↓
Semantic Search
 ↓
Top-K valid results
```

Depending on system, metadata filtering may happen before, during or around vector search.

## Useful DevOps Metadata

```text
service
team
environment
region
source
document_type
severity
incident_id
created_at
updated_at
version
status
```

## Security Important

Metadata filtering **authorization ka replacement nahi hai**.

```text
Filter = relevance/scope control
Authorization = user/service ko data access permission hai ya nahi
```

Sensitive multi-team knowledge base me retrieval layer ko identity/access policy enforce karni chahiye.

## Versioning Example

```text
runbook v1 → deprecated
runbook v2 → active
```

Metadata:

```json
{"version": "2", "status": "active"}
```

Retriever active docs prioritize/filter kar sakta hai.

## Common Mistakes

- inconsistent values: `prod`, `production`, `Prod`
- source/path missing
- old docs ko active status dena
- metadata ko unvalidated free text bana dena
- security boundary ko only metadata where-clause par depend karna

## Interview Point

**Q: Why combine vector search with metadata filtering?**

To retrieve semantically relevant content while restricting results to operationally valid dimensions such as environment, service, document type or version.

## Next Lesson Kyu?

Ab individual building blocks clear hain. Next lesson me full **indexing + retrieval pipeline** connect karenge.
