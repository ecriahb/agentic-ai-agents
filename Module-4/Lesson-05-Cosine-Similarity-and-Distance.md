# Lesson 05 — Cosine Similarity & Distance

> **Vector search me “near” ka meaning metric decide karta hai.**

## 🎯 Lesson Goal

Cosine similarity aur distance ko practical intuition ke saath samajhna.

## Cosine Similarity

Cosine similarity do vectors ke **direction** ko compare karti hai.

```text
same direction      → high similarity
very different      → lower similarity
opposite direction  → very low / negative similarity
```

Conceptual formula:

```text
cosine_similarity(A, B)
= dot(A, B) / (||A|| × ||B||)
```

Math yaad karna objective nahi hai. Important mental model:

> Vector ka direction semantic relationship represent karta hai; cosine un directions ko compare karta hai.

## Tiny Python Practical

```python
import math


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b)

query = [1.0, 0.9, 0.1]
aks_network = [0.9, 1.0, 0.2]
docker_build = [0.1, 0.2, 1.0]

print(cosine_similarity(query, aks_network))
print(cosine_similarity(query, docker_build))
```

## Similarity vs Distance

Different systems may expose:

```text
higher similarity = better match
```

or

```text
lower distance = better match
```

Isliye API result ko interpret karte waqt metric ka contract check karna important hai.

## L2 / Euclidean Distance

Another common idea:

```text
physical straight-line distance between vectors
```

FAISS ka simple `IndexFlatL2` exact L2 search provide karta hai. Cosine-style search ke liye normalized vectors ke saath inner product bhi commonly used approach hai.

## DevOps Example

Query vector network-failure semantics represent karta hai. Stored incident vector agar same semantic direction me hai to similarity high aayegi even if exact words alag ho.

## Common Mistakes

- similarity and distance scores ko same direction me interpret karna
- arbitrary universal threshold assume karna
- embedding model badal ke old threshold reuse karna
- relevance ko only score se decide karna without evaluation

## Interview Point

**Q: Why is cosine similarity popular for embeddings?**

Because it compares vector orientation, making it useful when semantic direction matters more than raw magnitude.

## Next Lesson Kyu?

Small list ko Python loop se compare kar sakte hain. Thousands/millions vectors ko efficiently organize/search karne ke liye **vector index/database** chahiye.
