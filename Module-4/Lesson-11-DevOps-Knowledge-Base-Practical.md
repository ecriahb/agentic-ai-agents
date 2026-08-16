# Lesson 11 — DevOps Knowledge Base Practical

> **Ab embeddings ko generic demo se nikal kar actual DevOps knowledge retrieval me use karte hain.**

## 🎯 Lesson Goal

Small local DevOps knowledge base design karna jisme runbooks, incidents aur Terraform guidance searchable ho.

## Sample Knowledge Base

```text
sample_docs/
├── aks-networking.md
├── terraform-state.md
├── pipeline-failure.md
└── docker-build.md
```

## Example Content

`aks-networking.md`

```text
If AKS workloads lose connectivity after a Terraform networking change,
validate NSG rules on the AKS subnet, route tables and required outbound paths.
```

`terraform-state.md`

```text
For Terraform state lock errors, verify whether another apply is active before force-unlocking.
```

## Practical Architecture

```text
Markdown Files
    ↓
Load Text
    ↓
Chunk by paragraphs/sections
    ↓
Embedding Model
    ↓
Vector Store
    ↓
Query
    ↓
Top-K DevOps Chunks
```

## What We Store Per Chunk

```python
record = {
    "id": "aks-networking-001",
    "text": "Validate NSG rules...",
    "metadata": {
        "service": "aks",
        "source": "aks-networking.md",
        "type": "runbook"
    }
}
```

## Query Examples

```text
Why can AKS connectivity break after Terraform changes?

How should I handle a Terraform state lock?

What should I inspect when a deployment pipeline fails during apply?
```

## Expected Behavior

Query 1 should prefer AKS/networking content.

Query 2 should prefer Terraform state content.

Query 3 should prefer deployment/Terraform failure content.

## Important Evaluation

Sirf “result aa gaya” success nahi hai.

Create a tiny test set:

| Query | Expected Source |
|---|---|
| AKS connectivity after NSG change | `aks-networking.md` |
| Terraform lock | `terraform-state.md` |
| Docker image is huge | `docker-build.md` |

Then check whether expected source top results me hai.

## Retrieval Debugging Checklist

If wrong result comes:

```text
1. Query meaningful hai?
2. Correct docs indexed hain?
3. Chunk too large/small to nahi?
4. Metadata correct hai?
5. Same compatible embedding model used hai?
6. Top-k suitable hai?
7. Score/distance interpretation correct hai?
8. Duplicate/stale documents to nahi?
```

## Security Mindset

Real company knowledge-base me:

- secrets/token files index mat karo
- credentials redact karo
- sensitive logs sanitize karo
- access scope enforce karo
- source permissions respect karo
- retrieved text ko untrusted content ki tarah safely process karo

## Module 1 Connection

Module 1 me evidence agent manually tool call karke evidence collect karta tha.

Ab ek new source possible hai:

```text
Agent
 ↓
Search Knowledge Base Tool
 ↓
Vector Retrieval
 ↓
Relevant Runbook / Incident Evidence
```

## Next Lesson Kyu?

Ab components understood hain. Lesson 12 me ek complete local application banayenge: **Search Your Own DevOps Documents**.
