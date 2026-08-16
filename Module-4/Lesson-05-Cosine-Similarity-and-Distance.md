# 🚩 Lesson 05 — Cosine Similarity & Distance Concepts

> **Similarity search ke peeche metric hota hai. Metric decide karta hai ki do vectors kitne close ya similar hain.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- cosine similarity ka intuition
- dot product aur magnitude ka high-level role
- L2/Euclidean distance ka idea
- similarity vs distance
- normalized vectors
- FAISS ke metric choice ka effect
- practical calculation
- metric selection ke common mistakes

---

# PART 1 — Why Metric Matters

Embeddings ban gaye. Ab do vectors compare karne hain:

```text
Query Vector
     ↕
Document Vector
```

Comparison ka rule = **metric**.

Different metric different notion of closeness use karta hai.

---

# PART 2 — Cosine Similarity

**English Definition:**
> Cosine similarity measures the cosine of the angle between two vectors and is commonly used to compare their direction in vector space.

Hinglish:

Cosine similarity mostly direction compare karta hai.

2D intuition:

```text
A  ↗
B  ↗   → similar direction
C  ←   → different direction
```

Typical range:

```text
-1 to 1
```

Many embedding use cases me:

```text
closer to 1 = more similar
```

But actual distribution/model behavior dataset-specific hota hai.

---

# PART 3 — Formula Intuition

Formula:

```text
cos(A,B) = (A · B) / (||A|| ||B||)
```

You do not need to memorize derivation.

Know components:

```text
A · B      = dot product
||A||      = magnitude of A
||B||      = magnitude of B
```

Division by magnitudes makes comparison direction-focused.

---

# PART 4 — Manual Python Practical

```python
import numpy as np


def cosine_similarity(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

v1 = [1, 1]
v2 = [2, 2]
v3 = [-1, 1]

print(cosine_similarity(v1, v2))
print(cosine_similarity(v1, v3))
```

Expected intuition:

```text
v1 vs v2 → close to 1 because direction same
v1 vs v3 → much lower because direction differs
```

---

# PART 5 — L2 / Euclidean Distance

**English Definition:**
> Euclidean distance measures the straight-line distance between two points in vector space.

Mental model:

```text
Point A ●--------● Point B
          distance
```

With L2:

```text
smaller distance = closer
```

Very important contrast:

```text
Cosine similarity → higher can mean better
L2 distance       → lower can mean better
```

---

# PART 6 — Normalized Embeddings

If vectors are normalized to unit length, inner product and cosine-related ranking can become closely aligned.

Concept:

```text
Raw vector
   ↓ normalize
Unit vector
```

SentenceTransformer example:

```python
vectors = model.encode(texts, normalize_embeddings=True)
```

FAISS inner-product example often uses normalized vectors when cosine-like behavior is desired.

---

# PART 7 — DevOps Example

Query:

```text
AKS network connectivity issue
```

Candidate docs:

```text
A: Kubernetes subnet blocked by NSG
B: Docker image cleanup
C: Terraform state locking
```

After embeddings:

```text
cos(query, A) → highest
cos(query, C) → medium/low
cos(query, B) → low
```

The metric ranks candidates; it does not prove root cause.

---

# PART 8 — Metric Choice and Vector DB

Vector stores/indexes often ask you to choose or configure a metric:

```text
cosine
inner product
L2
```

Never copy configuration without understanding model/index expectations.

Questions to ask:

- Are embeddings normalized?
- What metric does library use by default?
- Does returned value mean distance or similarity?
- Is lower or higher better?

---

# PART 9 — Thresholds

You may want:

```text
if score < threshold:
    reject result
```

But do **not** blindly use internet threshold like `0.8`.

Correct approach:

```text
real queries
 + labeled relevant docs
 + evaluation
 → choose threshold
```

Different models/domains have different score distributions.

---

# PART 10 — Common Mistakes

1. Cosine similarity and distance ko same direction me interpret karna.
2. Normalization mismatch.
3. Fixed threshold without evaluation.
4. Score ko probability samajhna.
5. Metric change karke old benchmark reuse karna.

---

# PART 11 — Interview Corner

**Q: Cosine similarity kya measure karta hai?**  
It compares vector direction using the angle between vectors.

**Q: L2 distance me better result ka direction kya hai?**  
Smaller distance generally means closer vectors.

**Q: Is cosine score a probability?**  
No. It is a similarity measure, not a calibrated probability.

---

# PART 12 — Revision

```text
Embeddings
   ↓
Metric
   ↓
Similarity / Distance
   ↓
Ranking
```

Remember:

```text
Similarity high can be good
Distance low can be good
Always verify library semantics
```

---

# PART 13 — Homework

1. `01_cosine_similarity.py` run karo.
2. Same meaning ke 3 DevOps sentences compare karo.
3. Cosine score ko probability kyu nahi bolna chahiye?

---

# Next Lesson Kyu?

Ab hum manually vectors compare kar sakte hain. Millions of chunks par manual/brute-force management practical nahi rahega.

# 👉 Lesson 06 — Vector Database Fundamentals
