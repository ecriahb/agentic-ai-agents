# 🚩 Lesson 08 — Chunking Strategies

> **Bad chunking retrieval ko damage karta hai, chahe embedding model kitna bhi achha ho.**

---

## 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- chunking kya hai aur kyu zaruri hai
- fixed-size, overlap, paragraph/section and semantic chunking concepts
- too-small vs too-large chunks
- context boundary problem
- DevOps runbook chunking
- chunk IDs and source traceability
- simple Python practical
- chunk-size evaluation mindset

---

# PART 1 — Why Chunking Exists

Suppose ek runbook 20 pages ka hai.

Agar poora document ek embedding bana diya:

```text
20-page document
      ↓
1 vector
```

Query sirf ek specific NSG troubleshooting step se related ho sakti hai. Whole document representation noisy ho sakta hai.

Better:

```text
Large Document
   ↓
Useful Sections / Chunks
   ↓
One embedding per chunk
```

---

# PART 2 — English Definition

> Chunking is the process of splitting larger source content into smaller retrieval units before embedding and indexing.

Hinglish:

**Document ko aise meaningful pieces me todna ki search sahi context retrieve kar sake.**

---

# PART 3 — Bad Chunking Example

Original:

```text
Step 3: Validate AKS subnet NSG rules.
The required outbound rule must allow traffic to the private endpoint.
If the rule was removed, restore it and rerun connectivity validation.
```

Bad split:

```text
Chunk 1: Step 3: Validate AKS subnet NSG
Chunk 2: rules. The required outbound rule must
Chunk 3: allow traffic to the private endpoint...
```

Meaning unnecessarily split ho gaya.

---

# PART 4 — Too Small vs Too Large

## Too Small

```text
"NSG rule"
```

Problem:
- context missing
- ambiguity high
- many near-duplicate chunks

## Too Large

```text
Entire 50-page operations manual
```

Problem:
- mixed topics
- noisy embedding
- expensive context later

Desired:

```text
One chunk ≈ one useful coherent idea/procedure
```

No universal perfect size exists.

---

# PART 5 — Fixed-Size Chunking

Simple character-based example:

```python
def chunk_text(text, chunk_size=300):
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]
```

Pros:
- simple
- predictable

Cons:
- sentences/steps can split awkwardly

Useful for learning, not automatically best production strategy.

---

# PART 6 — Overlap

Overlap keeps some previous context in next chunk.

Example:

```text
Chunk 1: words 1–200
Chunk 2: words 151–350
```

50-word overlap.

Why?

Important statement boundary par split ho to next chunk me some shared context remain kare.

Tradeoff:

```text
More overlap
   ↓
More context continuity
BUT
More duplicate storage + retrieval redundancy
```

---

# PART 7 — Paragraph / Section-Aware Chunking

Runbooks often naturally structured hote hain:

```text
# Symptoms
# Checks
# Root Cause
# Resolution
# Validation
```

Section-aware chunks can preserve semantic boundaries better than blind character splits.

Example chunk metadata:

```json
{
  "source": "aks-networking.md",
  "section": "Resolution",
  "chunk_id": "aks-networking-resolution-01"
}
```

---

# PART 8 — Semantic Chunking Concept

Semantic chunking attempts to split based on meaning/topic shifts instead of only fixed length.

Mental model:

```text
Topic A text
Topic A text
----- semantic boundary -----
Topic B text
Topic B text
```

It can improve coherence but adds complexity/cost and must be evaluated.

---

# PART 9 — DevOps Runbook Example

Document:

```text
AKS Network Troubleshooting

Symptoms:
Pods cannot reach private SQL endpoint.

Checks:
1. Verify DNS resolution.
2. Check NSG outbound rules.
3. Check UDR and Azure Firewall routes.

Resolution:
Restore required rule, validate connectivity, redeploy.
```

Possible chunks:

```text
Chunk 1 → Symptoms
Chunk 2 → DNS check
Chunk 3 → NSG + route checks
Chunk 4 → Resolution
```

Query:

```text
What should I check after NSG rule removal?
```

Chunk 3/4 should be strong candidates.

---

# PART 10 — Practical Chunker

```python
from pathlib import Path


def chunk_by_paragraph(text, max_chars=500):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current = ""

    for paragraph in paragraphs:
        candidate = f"{current}\n\n{paragraph}".strip()
        if current and len(candidate) > max_chars:
            chunks.append(current)
            current = paragraph
        else:
            current = candidate

    if current:
        chunks.append(current)

    return chunks

text = Path("sample_docs/aks-networking.md").read_text(encoding="utf-8")
chunks = chunk_by_paragraph(text)

for i, chunk in enumerate(chunks):
    print(f"\n--- chunk {i} ---\n{chunk}")
```

Observe boundaries manually.

---

# PART 11 — Chunk Metadata

Every chunk should remain traceable.

```json
{
  "source": "aks-networking.md",
  "chunk_id": 3,
  "service": "aks",
  "environment": "prod",
  "section": "network-checks"
}
```

Without source metadata, retrieved text ka origin lose ho jayega.

---

# PART 12 — How to Choose Chunk Size

No magic number.

Evaluate using real questions:

```text
Question
 ↓
Expected relevant chunk
 ↓
Does Top-K retrieve it?
```

Try multiple strategies and compare retrieval quality.

Factors:

- document type
- model input constraints
- procedure length
- desired answer granularity
- overlap
- retrieval top-k

---

# PART 13 — Common Mistakes

1. Every document type par same chunking blindly use karna.
2. Headings lose kar dena.
3. Source metadata omit karna.
4. Tiny chunks produce karna.
5. Huge chunks se mixed topics retrieve karna.
6. Overlap itna high rakhna ki duplicates flood ho jayein.

---

# PART 14 — Interview Corner

**Q: Why is chunking important in RAG?**  
Because retrieval operates on indexed units; coherent chunks improve the chance that the right evidence is retrieved without excessive irrelevant context.

**Q: Why use overlap?**  
To preserve context across boundaries, though too much overlap causes duplication.

**Q: Is there a universal optimal chunk size?**  
No. It should be evaluated against the document type, embedding model and real retrieval queries.

---

# PART 15 — Revision

```text
Large Document
   ↓
Chunk Strategy
   ↓
Coherent Retrieval Units
   ↓
Embeddings
   ↓
Better Search Candidates
```

---

# PART 16 — Homework

1. `aks-networking.md` ko 2 different chunk sizes se split karo.
2. Compare number of chunks.
3. Identify ek boundary jahan fixed split meaning tod raha hai.
4. Paragraph-aware version try karo.

---

# Next Lesson Kyu?

Chunks mil gaye, but search ko kaise pata chalega kaunsa chunk prod ka hai, source kya hai, version kya hai?

# 👉 Lesson 09 — Metadata & Filtering
