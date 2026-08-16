# 🚩 Lesson 03 — How Text Becomes Vectors

> **Embedding sirf concept nahi; ab hum dekhenge text se vector banne ka practical pipeline.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- raw text embedding model tak kaise jata hai
- preprocessing/tokenization ka high-level role
- single vs batch encoding
- output shape/dimensions
- document aur query embedding ka relation
- normalization ka basic idea
- actual Python practical
- common implementation mistakes

---

# PART 1 — Big Picture

```text
Raw Text
   ↓
Model Input Preparation
   ↓
Embedding Model
   ↓
Dense Vector
   ↓
Store / Compare
```

Example:

```text
"Terraform apply failed after NSG change"
                ↓
Embedding model
                ↓
[0.031, -0.112, 0.447, ...]
```

---

# PART 2 — Tokenization ka Basic Idea

Embedding model directly human sentence ko magic se vector nahi banata. Internally text ko model-consumable units me convert kiya jata hai.

High-level mental model:

```text
Sentence
  ↓
Tokenizer
  ↓
Token IDs / model inputs
  ↓
Neural network
  ↓
Vector representation
```

Is module me tokenizer mathematics deep dive nahi karna; important point hai ki **model ke input length limits aur preprocessing retrieval quality ko affect kar sakte hain**.

---

# PART 3 — Single Text Encoding

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "AKS deployment failed after subnet rule change"
embedding = model.encode(text)

print(type(embedding))
print(embedding.shape)
print(embedding[:5])
```

Expected pattern:

```text
<class 'numpy.ndarray'>
(384,)
[first five numeric values...]
```

### Meaning

`(384,)` means one 384-dimensional vector.

---

# PART 4 — Batch Encoding

Real application me ek document nahi, hundreds/thousands chunks encode karenge.

```python
texts = [
    "AKS subnet connectivity failed",
    "Terraform state is locked",
    "Docker build ran out of disk space"
]

embeddings = model.encode(texts)
print(embeddings.shape)
```

Expected:

```text
(3, 384)
```

Mental model:

```text
3 texts
  ↓
3 vectors
  ↓
Each vector = 384 dimensions
```

---

# PART 5 — Document Embedding vs Query Embedding

Index time:

```text
Runbook chunk → embedding → store
Incident note → embedding → store
Postmortem chunk → embedding → store
```

Query time:

```text
User question → embedding → compare with stored vectors
```

This compatibility is critical:

```text
Same / compatible embedding approach
        ↓
Comparable vector space
```

---

# PART 6 — Normalization ka Basic Idea

Kuch retrieval setups vectors normalize karte hain so vector length 1 ho jaye. Ye cosine/inner-product based comparison me useful ho sakta hai.

Conceptual:

```text
Raw vector
   ↓
Normalize
   ↓
Same direction, controlled magnitude
```

Example:

```python
embedding = model.encode(text, normalize_embeddings=True)
```

Important: normalization blindly enable nahi karna; chosen metric/index ke contract ke saath align karo.

---

# PART 7 — Practical: Multiple DevOps Incidents

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

incidents = [
    "AKS pods cannot access SQL after NSG change",
    "Terraform apply blocked by state lock",
    "Docker build fails because disk is full",
    "Kubernetes workloads lost database connectivity"
]

vectors = model.encode(incidents, normalize_embeddings=True)

for incident, vector in zip(incidents, vectors):
    print("\nINCIDENT:", incident)
    print("DIMENSIONS:", len(vector))
    print("FIRST 5 VALUES:", vector[:5])
```

### What to observe

- every text ka vector same dimension ka hai
- numeric values human labels nahi hain
- related meaning vectors ko next lessons me similarity metric se compare karenge

---

# PART 8 — Why Chunking Will Matter Later

Embedding model ko agar ek huge 100-page document de diya to retrieval unit poorly defined ho sakta hai.

We eventually want:

```text
Large Document
    ↓
Useful Chunks
    ↓
One embedding per chunk
```

But chunking Lesson 8 me deeply cover karenge.

---

# PART 9 — Common Mistakes

1. **Index ek model se, query dusre incompatible model se.**
2. Model version change kiya but old index reuse kar liya.
3. Input limits ignore kiye.
4. Empty strings/garbage documents embed kar diye.
5. Secrets/log credentials raw knowledge base me push kar diye.
6. Shape/dimension verify nahi ki.

---

# PART 10 — Production Thinking

Embedding pipeline me record karna useful hai:

```text
source
chunk_id
embedding_model
model_version
created_at
document_version
```

Re-indexing strategy bhi chahiye when:

- model changes
- chunking changes
- documents update
- metadata schema changes

---

# PART 11 — Interview Corner

**Q: What happens during document indexing?**  
Documents are loaded, split into retrieval units, embedded and stored/indexed with metadata.

**Q: Why should query and document embeddings be compatible?**  
Because similarity search assumes both representations exist in the same comparable vector space and dimension.

**Q: What is batch embedding?**  
Encoding multiple texts together rather than one at a time, typically for efficient ingestion.

---

# PART 12 — Revision

```text
Text
 ↓
Model Input
 ↓
Embedding Model
 ↓
Vector
 ↓
Store / Compare
```

Remember:

```text
One chunk = one vector
Query = another vector
Similarity = comparison
```

---

# PART 13 — Homework

1. 4 DevOps sentences ka batch embedding script run karo.
2. Output shape note karo.
3. Explain why old index ko blindly reuse nahi karna chahiye after model change.

---

# Next Lesson Kyu?

Ab vectors ban gaye. Lekin relevant document kaise choose hoga?

**Vectors ko compare karke nearest/relevant vectors rank karna hoga.**

# 👉 Lesson 04 — Similarity Search Basics
