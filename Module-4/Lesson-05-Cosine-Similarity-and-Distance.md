# 🚩 Lesson 05 — Cosine Similarity & Distance Concepts

> **Similarity search ke peeche ek comparison metric hota hai. Metric define karta hai ki do vectors ko kis notion of closeness ke according compare aur rank kiya jayega.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- why vector metrics matter in semantic retrieval
- cosine similarity and its mathematical intuition
- L2 / Euclidean distance and its mathematical intuition
- similarity vs distance semantics
- normalized embeddings and why normalization matters
- how Sentence Transformers, scikit-learn and FAISS interpret metrics
- practical metric configuration and ranking
- threshold selection using evaluation evidence
- common production mistakes

---

# 1. Why Metrics Matter

Embeddings convert text into vectors. Once we have vectors, we need a rule to compare them.

That rule is the **metric** or similarity function.

Conceptually:

```text
Text
  ↓
Embedding Model
  ↓
Vector
  ↓
Comparison Metric
  ↓
Similarity / Distance Score
  ↓
Ranking
```

For a RAG system:

```text
User Query
    ↓
Query Embedding
    ↓
Compare against document embeddings
    ↓
Metric calculates score
    ↓
Rank candidate chunks
    ↓
Retrieve the best candidates
```

### DevOps Example

Suppose the query is:

```text
"AKS network connectivity issue"
```

Candidate documents:

```text
A: Kubernetes subnet blocked by NSG
B: Docker image cleanup procedure
C: Terraform state locking issue
```

After embedding, the metric provides a mathematical basis for comparing the query vector with each document vector.

The metric **ranks candidates; it does not prove the root cause**.

### Metric vs Search

These concepts are related but different:

```text
Metric
  ↓
How do we measure closeness?

Search / Index
  ↓
How do we find the closest vectors efficiently?
```

This distinction becomes important in Lesson 06, where we move from manual comparison to vector indexes and nearest-neighbor search.

---

# 2. Cosine Similarity

## 2.1 English Definition

> Cosine similarity measures the cosine of the angle between two vectors and therefore focuses on their direction in vector space.

Scikit-learn defines cosine similarity as the L2-normalized dot product:

```text
cos(A, B) = (A · B) / (||A|| ||B||)
```

citeturn0search0turn0search8

### Hinglish intuition

Socho do arrows hain:

```text
A  ↗
B  ↗
```

Agar dono almost same direction mein point kar rahe hain, cosine similarity high hogi.

```text
A  ↗
B  ↖
```

Direction different hai, similarity lower hogi.

Cosine similarity therefore answers roughly:

> **"Are these vectors pointing in a similar direction?"**

---

## 2.2 Formula Components

```text
cos(A,B) = (A · B) / (||A|| ||B||)
```

Where:

```text
A · B   → dot product
||A||   → magnitude / L2 norm of A
||B||   → magnitude / L2 norm of B
```

The denominator normalizes the vectors before comparing their direction.

NumPy's `numpy.linalg.norm()` computes vector or matrix norms and can be used to calculate the magnitude required by the formula. citeturn1search9

---

## 2.3 Score Interpretation

Mathematically, cosine similarity is generally in:

```text
[-1, 1]
```

For many text-embedding models, observed scores may occupy a narrower range. Do **not** assume that every model produces only `[0, 1]` scores.

Sentence Transformers' official examples show cosine scores such as `0.8939`, `0.0543`, and `-0.0502`, demonstrating that negative cosine scores are possible. citeturn1search0

General interpretation:

```text
Higher cosine similarity → more similar direction
Lower cosine similarity  → less similar direction
```

The exact score distribution is model- and dataset-dependent.

---

# 3. L2 / Euclidean Distance

## 3.1 English Definition

> Euclidean distance measures the straight-line distance between two points in vector space.

For vectors A and B:

```text
L2(A,B) = sqrt(Σ(Aᵢ - Bᵢ)²)
```

Mental model:

```text
A ●────────────● B
       distance
```

With distance-based retrieval:

```text
smaller distance = closer
```

Scikit-learn describes Euclidean distance as a distance metric where smaller distance means the objects are considered more similar. citeturn0search0

---

## 3.2 Cosine vs L2

The direction of the score is different:

```text
Cosine Similarity
higher → generally more similar

L2 Distance
lower  → generally more similar
```

This sounds simple, but it is one of the most common retrieval bugs:

```text
score = 0.91
```

You cannot interpret `0.91` correctly until you know whether the system returned:

```text
similarity → higher is better
```

or:

```text
distance → lower is better
```

---

# 4. Metrics Comparison Table

| Metric | Type | Better Result | Main Intuition | Important Note |
|---|---|---|---|---|
| Cosine | Similarity | Higher | Compare direction | Uses normalized dot product |
| Dot Product / Inner Product | Similarity | Higher | Vector interaction | Magnitude affects score unless vectors are normalized |
| L2 / Euclidean | Distance | Lower | Straight-line distance | FAISS commonly uses squared L2 internally |

Scikit-learn defines cosine similarity as the normalized dot product. citeturn0search0

FAISS supports inner-product and L2 metrics across many indexes; its `MetricType` documentation identifies `METRIC_INNER_PRODUCT` as maximum inner-product search and `METRIC_L2` as squared-L2 search. citeturn0search4

Sentence Transformers supports cosine, dot product, Euclidean and Manhattan similarity functions, with cosine as its default similarity function. citeturn1search0turn1search1

### Important Rule

Never write code like:

```text
if score > 0.8:
    relevant = True
```

until you know:

1. which metric is being used
2. whether the returned value is similarity or distance
3. how the embedding model's scores are distributed
4. whether vectors are normalized

---

# 5. Normalized Embeddings & Official Libraries

## 5.1 What Does Normalization Mean?

Normalization converts a vector to unit length:

```text
Raw vector
    ↓
L2 normalization
    ↓
Unit-length vector
```

Conceptually:

```text
||v|| = 1
```

Sentence Transformers exposes this directly through:

```python
normalize_embeddings=True
```

Its official API documents this option as normalizing returned vectors to length 1. citeturn1search6turn1search7

---

## 5.2 Why Normalization Matters

For normalized vectors:

```text
cosine similarity
        ≈
inner product / dot product
```

More precisely, when both vectors have unit norm:

```text
cos(A,B) = A · B
```

Sentence Transformers explicitly notes that dot product on normalized embeddings is equivalent to cosine similarity, and that using dot product can avoid re-normalizing embeddings again. citeturn1search0

This relationship is particularly useful when configuring FAISS:

```text
Normalize vectors
       ↓
FAISS IndexFlatIP
       ↓
Inner-product ranking
       ↓
Cosine-equivalent ranking
```

FAISS itself is a similarity-search and clustering library for dense vectors rather than a complete application database. Its documentation describes both exact and non-exhaustive search structures and supports Python wrappers. citeturn0search2

---

## 5.3 OpenAI Embeddings

OpenAI's embedding models produce numerical representations of text that can be used to measure relatedness between pieces of text. The current API supports embedding models such as `text-embedding-3-small` and `text-embedding-3-large`. citeturn2search1turn2search2turn2search3

Example API call:

```python
from openai import OpenAI

client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[
        "AKS network connectivity issue",
        "Kubernetes subnet blocked by NSG"
    ]
)

vectors = [item.embedding for item in response.data]
print(len(vectors))
```

The important lesson here is:

> **The embedding model creates the vectors; the metric determines how we compare those vectors.**

OpenAI's embedding API also supports a `dimensions` parameter for `text-embedding-3` and later models. citeturn2search1

---

# 6. Practical Implementation with Official Libraries

## 6.1 Sentence Transformers — Semantic Similarity

Hugging Face Sentence Transformers provides a direct API for encoding text and computing similarities. Its official documentation demonstrates `SentenceTransformer.encode()` followed by `model.similarity()`. citeturn1search0turn1search4

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Kubernetes subnet blocked by NSG",
    "Docker image cleanup procedure",
    "Terraform state locking issue",
]

query = "AKS network connectivity issue"

# Encode documents and query
# normalize_embeddings=True makes each vector unit length.
doc_embeddings = model.encode(
    documents,
    normalize_embeddings=True
)
query_embedding = model.encode(
    query,
    normalize_embeddings=True
)

# Compute cosine similarity
similarities = model.similarity(
    query_embedding,
    doc_embeddings
)[0]

for doc, score in zip(documents, similarities):
    print(f"{score:.4f}  {doc}")
```

### Interpretation

```text
Higher score → more similar
```

Do **not** hard-code a universal rule such as:

```text
0.9+ = always relevant
0.5-0.7 = always moderately relevant
<0.3 = always irrelevant
```

Those thresholds are not universal. The official Sentence Transformers examples demonstrate score values, but retrieval thresholds must be validated for the specific model, corpus and task. citeturn1search0

---

## 6.2 scikit-learn — Explicit Cosine Similarity

For transparent experimentation, scikit-learn exposes:

```python
from sklearn.metrics.pairwise import cosine_similarity

query = [[1, 1]]
documents = [
    [2, 2],
    [1, 0],
    [-1, 1],
]

scores = cosine_similarity(query, documents)[0]

for score, document in zip(scores, documents):
    print(f"{score:.4f}  {document}")
```

Scikit-learn defines this function as the normalized dot product and documents that on L2-normalized data it is equivalent to the linear kernel. citeturn0search8

### Cosine Distance

Scikit-learn also exposes cosine distance:

```python
from sklearn.metrics.pairwise import cosine_distances

print(cosine_distances(query, documents))
```

Its official definition is:

```text
cosine distance = 1 - cosine similarity
```

Therefore:

```text
higher similarity → better
lower distance     → better
```

citeturn0search6

---

## 6.3 NumPy — Build the Formula Yourself

For learning, implementing the formula manually is useful:

```python
import numpy as np


def cosine_similarity(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

v1 = [1, 1]
v2 = [2, 2]
v3 = [-1, 1]

print(cosine_similarity(v1, v2))
print(cosine_similarity(v1, v3))
```

Expected intuition:

```text
v1 vs v2 → approximately 1.0
v1 vs v3 → much lower
```

`numpy.linalg.norm()` is the official NumPy function for vector/matrix norms. citeturn1search9

### Production Note

This manual implementation is excellent for learning, but production retrieval normally uses optimized vector libraries or vector databases rather than repeatedly implementing pairwise calculations in Python loops.

---

## 6.4 FAISS — Normalized Vectors + Inner Product

FAISS supports inner-product search and L2-based search. citeturn0search2turn0search4

For cosine-equivalent ranking, normalize the vectors and use an inner-product index:

```python
import faiss
import numpy as np

# Example vectors
vectors = np.array(
    [
        [1.0, 1.0],
        [2.0, 0.0],
        [-1.0, 1.0],
    ],
    dtype="float32",
)

query = np.array(
    [[1.0, 1.0]],
    dtype="float32",
)

# L2-normalize vectors
faiss.normalize_L2(vectors)
faiss.normalize_L2(query)

# Inner product on normalized vectors gives cosine-equivalent ranking
index = faiss.IndexFlatIP(vectors.shape[1])
index.add(vectors)

scores, ids = index.search(query, k=2)

print("scores:", scores)
print("ids:", ids)
```

The important configuration relationship is:

```text
Cosine-like retrieval
      ↓
L2-normalize query + documents
      ↓
FAISS inner product
      ↓
Higher score = better match
```

FAISS documentation notes that its flat indexes perform exhaustive search, while other index structures support more scalable/non-exhaustive search. citeturn0search2

---

# 7. Common Mistakes & Fixes

## Mistake 1 — Treating similarity as probability

Wrong:

```text
cosine = 0.82
→ 82% probability that document is correct
```

Correct:

```text
cosine = 0.82
→ a similarity score under this metric/model
```

It is not automatically a calibrated probability.

---

## Mistake 2 — Reversing score semantics

Wrong:

```text
L2 = 0.2 → worse because score is small
```

Correct:

```text
L2 = 0.2 → closer than L2 = 0.8
```

Always verify whether the API returns similarity or distance.

---

## Mistake 3 — Assuming cosine scores are always [0,1]

Cosine similarity is mathematically in:

```text
[-1, 1]
```

Actual model score distributions can be narrower, but you should not assume a universal range without checking the model and data. Sentence Transformers' own examples include a negative cosine score. citeturn1search0

---

## Mistake 4 — Mixing normalized and non-normalized vectors

If documents are normalized but queries are not, your retrieval semantics may not match what you intended.

Fix:

```text
Choose normalization policy
        ↓
Apply it consistently
        ↓
Benchmark retrieval
```

---

## Mistake 5 — Changing the metric without re-evaluating

Suppose the benchmark was created using cosine similarity.

Then someone changes the index to L2.

Do not assume the old threshold and benchmark remain valid.

Fix:

```text
Metric change
   ↓
Re-run evaluation
   ↓
Re-check ranking
   ↓
Re-check threshold
```

---

## Mistake 6 — Copying a threshold from the internet

There is no universal rule like:

```text
cosine > 0.8 → relevant
```

A threshold is meaningful only in the context of a particular model, corpus, query distribution and task.

---

# 8. Thresholds — Evidence-Based Retrieval

A threshold is a decision boundary such as:

```python
if score >= threshold:
    accept_result()
else:
    reject_result()
```

But choosing `0.8`, `0.7` or any other number arbitrarily is unsafe.

### Better approach

Create a small evaluation set:

```text
Real queries
    +
Known relevant documents
    +
Known irrelevant documents
    ↓
Run retrieval
    ↓
Collect scores
    ↓
Inspect precision / recall
    ↓
Choose threshold
```

Example:

```text
Query set: 100 production-like queries

For each query:
- relevant chunks labelled
- irrelevant chunks labelled
- similarity scores collected

Then evaluate:
- Recall@K
- Precision@K
- false positives
- false negatives
```

The threshold should be selected from evidence rather than copied from another model or tutorial.

---

# 9. Interview Questions

### Q1. What is cosine similarity?

Cosine similarity compares the direction of two vectors using the cosine of the angle between them. It is the normalized dot product.

---

### Q2. What is L2 distance?

L2 / Euclidean distance measures straight-line distance between vectors. Smaller distance means the vectors are closer.

---

### Q3. What is the difference between similarity and distance?

```text
Similarity → higher is generally better
Distance   → lower is generally better
```

Always verify the specific library's returned score semantics.

---

### Q4. Why normalize embeddings?

Normalization makes vectors unit length. With unit-normalized vectors, dot product becomes equivalent to cosine similarity, which can simplify and accelerate some retrieval configurations. citeturn1search0

---

### Q5. Is FAISS a vector database?

FAISS is primarily a library for efficient similarity search and clustering of dense vectors. Application-level persistence, metadata management, authorization and other database capabilities may require additional components depending on the architecture. citeturn0search2

---

### Q6. Why can the same query produce different score distributions with different embedding models?

Because embedding models learn different vector spaces and can produce different geometric distributions. Therefore thresholds and benchmarks should be evaluated per model/task rather than copied blindly.

---

### Q7. What happens if you use L2 when your application expects cosine-like ranking?

The ranking can change unless the relationship between the vectors and metrics is properly understood. If cosine-equivalent ranking is required with FAISS inner product, a common approach is to normalize both query and document vectors before indexing/searching.

---

# 10. Homework — Advanced

### Task 1 — Manual Math

Take:

```text
A = [1, 2]
B = [2, 4]
C = [2, 0]
```

Calculate:

1. cosine similarity of A and B
2. cosine similarity of A and C
3. L2 distance of A and B
4. L2 distance of A and C

Explain why the rankings can differ depending on the metric.

---

### Task 2 — Sentence Transformers

Use three DevOps sentences and:

1. encode them
2. calculate cosine similarities
3. repeat with `normalize_embeddings=True`
4. compare the scores
5. explain what changed

---

### Task 3 — FAISS

Create a small FAISS `IndexFlatIP` example.

Then compare:

```text
A. raw vectors + inner product
B. normalized vectors + inner product
```

Explain why normalization changes the interpretation of the score.

---

### Task 4 — Threshold Evaluation

Create at least 20 DevOps queries and manually label retrieved chunks as:

```text
relevant
irrelevant
```

Collect similarity scores and propose a threshold based on your observations.

Do not use a hard-coded internet threshold.

---

# 11. Key Takeaways

```text
Embedding
   ↓
Vector
   ↓
Metric
   ↓
Similarity / Distance
   ↓
Ranking
```

Remember:

```text
Cosine similarity → direction → higher is generally better
L2 distance       → geometric distance → lower is generally better
Dot product       → higher is generally better
```

And the most important production rule:

> **Never interpret a vector score without knowing the model, metric, normalization strategy and library semantics.**

---

# 12. References & Official Links

### OpenAI

- OpenAI Embeddings API Reference: https://developers.openai.com/api/reference/ruby/resources/embeddings/methods/create
- OpenAI Embedding Models: https://developers.openai.com/api/docs/models/text-embedding-3-small
- OpenAI `text-embedding-3-large`: https://developers.openai.com/api/docs/models/text-embedding-3-large

### scikit-learn

- Cosine Similarity: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
- Pairwise Metrics Guide: https://scikit-learn.org/stable/modules/metrics.html
- Cosine Distance: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html

### FAISS — Meta Research

- FAISS Documentation: https://faiss.ai/
- FAISS MetricType: https://faiss.ai/cpp_api/file/MetricType_8h.html

### Sentence Transformers / Hugging Face

- Semantic Textual Similarity: https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html
- SentenceTransformer Usage: https://www.sbert.net/docs/sentence_transformer/usage/usage.html
- SentenceTransformer API: https://www.sbert.net/docs/package_reference/sentence_transformer/model.html

### NumPy

- `numpy.linalg.norm`: https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html

### Stanford NLP

- Stanford CS224N: https://web.stanford.edu/class/cs224n/
- CS224N Evaluation Lecture: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture11-evaluation.pdf

---

# Next Lesson Kyu?

Ab hume pata hai:

```text
Vector
  ↓
Metric
  ↓
Similarity / Distance
  ↓
Ranking
```

Lekin agar corpus mein:

```text
10,000
100,000
1,000,000+
```

vectors hain, to har query par manually sab vectors compare karna practical nahi hai.

Ab hume **efficient indexing, nearest-neighbor search, persistence aur vector storage** chahiye.

# 👉 Lesson 06 — Vector Database Fundamentals
