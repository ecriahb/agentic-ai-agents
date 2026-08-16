# Lesson 03 — How Text Becomes Vectors

> **Text directly vector database me useful search object nahi banta; pehle embedding pipeline se guzarta hai.**

## 🎯 Lesson Goal

High-level embedding pipeline ko understand karna without unnecessary neural-network mathematics.

## Pipeline

```text
Raw Text
   ↓
Cleaning / Preparation
   ↓
Chunk
   ↓
Embedding Model
   ↓
Fixed-size Vector
   ↓
Store with original text + metadata
```

## Example

Input:

```text
NSG rule aks-subnet-allow was removed. AKS connectivity validation failed.
```

Application roughly ye store karegi:

```json
{
  "id": "incident-001-chunk-1",
  "text": "NSG rule aks-subnet-allow was removed...",
  "embedding": [0.12, -0.44, 0.91],
  "metadata": {
    "service": "aks",
    "environment": "production"
  }
}
```

Vector sample shortened hai; real vector usually far larger hota hai.

## Query Time

User query:

```text
Why is AKS connectivity failing after a network change?
```

Flow:

```text
Query
 ↓
Same/compatible embedding model
 ↓
Query Vector
 ↓
Compare with stored vectors
 ↓
Nearest chunks
```

## Important Design Rule

Embedding model ko change karna index design decision hai. Existing stored vectors aur new query vectors compatible hone chahiye; otherwise semantic comparison meaningful nahi rahega.

## What Should Be Stored?

Generally useful record:

```text
ID
Original chunk text
Embedding vector
Metadata
Source reference
Optional timestamps/version
```

Embedding alone human investigation ke liye enough nahi hai. Retrieved result ke saath original text/source bhi chahiye.

## DevOps Example

```text
terraform-network-policy.md
        ↓
split into meaningful sections
        ↓
embed each section
        ↓
store vectors + source metadata
```

Then query can return exactly network-related section instead of entire 50-page document.

## Common Mistakes

- whole huge document ko one vector banana
- original source path store na karna
- model/version info track na karna
- query aur documents ke liye incompatible embedding spaces use karna

## Next Lesson Kyu?

Vectors ready hain. Ab question hai: **kaunsa vector query ke sabse close hai?** Isliye similarity search.
