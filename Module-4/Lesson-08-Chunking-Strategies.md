# Lesson 08 — Chunking Strategies

> **Retrieval quality ka ek major factor hai: document ko kis boundary par split kiya gaya.**

## 🎯 Lesson Goal

Chunking ka purpose, chunk size, overlap aur semantic boundaries ko DevOps documents ke context me samajhna.

## English Definition

**Chunking** is the process of splitting source content into smaller retrievable units before creating embeddings.

## Why Chunk?

Suppose 40-page AKS runbook ko ek single embedding bana diya.

Problem:

```text
One huge document
→ multiple unrelated topics mixed
→ one vector represents too much meaning
→ exact useful section hard to retrieve
```

Better:

```text
Runbook
 ↓
Networking section
Authentication section
Node troubleshooting section
Ingress section
 ↓
separate embeddings
```

## Common Strategies

### 1. Fixed-size chunking

```text
Every N characters/tokens
```

Simple but headings/paragraphs cut ho sakte hain.

### 2. Paragraph-based

Natural paragraph boundaries preserve karna.

### 3. Heading / section-aware

Markdown/runbook ke headings ke basis par split.

DevOps docs ke liye often useful:

```text
## AKS Networking
## DNS Troubleshooting
## Terraform State
```

### 4. Sliding overlap

Adjacent chunks me thoda shared context:

```text
Chunk 1: lines 1–20
Chunk 2: lines 16–35
```

Overlap boundary information preserve kar sakta hai, but excessive overlap duplicate retrieval aur storage badhata hai.

## Chunk Size Trade-off

Too small:

- context incomplete
- commands aur explanation separate ho sakte hain
- many fragments

Too large:

- unrelated topics mix
- retrieval less precise
- more context sent downstream

## DevOps Example

Bad chunk:

```text
Entire production operations handbook
```

Better chunks:

```text
AKS subnet connectivity validation
AKS DNS troubleshooting
Terraform state lock recovery
GitHub Actions deployment rollback
```

## Metadata with Chunks

Every chunk ke saath source preserve karo:

```json
{
  "source": "aks-runbook.md",
  "section": "NSG troubleshooting",
  "service": "aks"
}
```

## Evaluation Rule

Best chunk size universal number nahi hai. Apne documents + queries par retrieval evaluate karo.

## Common Mistakes

- random split without preserving headings
- command ka half one chunk aur half next chunk me
- source metadata lose karna
- overlap ko excessively large rakhna
- chunking change ke baad re-index na karna

## Interview Point

**Q: Why does chunking affect RAG quality?**

Because retrieval happens at chunk level; chunks must be small enough to be precise but large enough to preserve the context needed to answer correctly.

## Next Lesson Kyu?

Semantic similarity useful hai, but enterprise query me environment/service restrictions bhi chahiye. Isliye next: **metadata and filtering**.
