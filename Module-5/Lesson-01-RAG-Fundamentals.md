# 🚩 Jai Bajrangbali!

# Lesson 01 — RAG Fundamentals

> **RAG ka simple goal: LLM ko answer dene se pehle trusted external knowledge dhoondhkar dena.**

> Module 4 already established embedding and nearest-neighbor mechanics. This lesson focuses on the grounding contract: reference context must support claims, and missing support must lead to abstention.

---

# 🎯 Lesson Goal

Is lesson ke end tak aap clearly samjhoge:

- RAG kya hai aur kyu bana
- LLM ki internal knowledge aur external knowledge me difference
- RAG model training se kaise different hai
- Retrieval, Augmentation aur Generation teen alag stages kyu hain
- DevOps me RAG ka real use kaha hota hai
- RAG hallucination ko reduce kaise karta hai — aur completely eliminate kyu nahi karta
- RAG vs fine-tuning vs normal prompting
- RAG ke common failure modes
- Module 4 se Module 5 ka exact connection

---

# PART 1 — Problem: LLM Sab Kuch Nahi Jaanta

Suppose user asks:

```text
Yesterday production AKS deployment Terraform Apply ke baad kyu fail hua?
```

General LLM ko ye nahi pata:

```text
- kal ka pipeline log
- aapke Terraform plan ka exact diff
- aapki company ka AKS runbook
- aapka internal NSG naming standard
- latest incident notes
```

Model ke paas mostly training se learned general patterns hote hain.

### Mental Model

```text
LLM Internal Knowledge
        ≠
Your Live / Private / Latest Knowledge
```

Isi gap ko RAG address karta hai.

---

# PART 2 — English Definition

**Retrieval-Augmented Generation (RAG)** is an AI architecture in which relevant external information is retrieved at query time and supplied to a language model as context so that the generated answer can be grounded in that information.

Simple Hinglish:

```text
Question
   ↓
Relevant knowledge search karo
   ↓
LLM ko context do
   ↓
Context ke basis par answer generate karao
```

---

# PART 3 — RAG Naam Ko Break Karo

## R = Retrieval

Question ke liye useful information find karna.

Example:

```text
Query:
AKS subnet connectivity failed after Terraform change

Retrieved:
- aks-networking.md
- terraform-networking.md
- pipeline-failure.md
```

## A = Augmented

Retrieved information ko LLM ke prompt/context me attach karna.

```text
QUESTION
+ RELEVANT EVIDENCE
+ RULES
```

## G = Generation

LLM supplied evidence ko use karke human-readable answer banata hai.

```text
Evidence → Explanation / RCA / Recommended checks
```

Important:

> Retrieval khud answer generation nahi hai. Generation khud retrieval nahi hai.

---

# PART 4 — Module 4 vs Module 5

Module 4 me humne banaya:

```text
Question
   ↓
Embedding
   ↓
Vector Search
   ↓
Relevant Chunks
```

Output:

```text
[S1] AKS networking runbook...
[S2] Terraform NSG guidance...
```

Ye **retrieval system** hai.

Module 5 me:

```text
Question
   ↓
Retrieve Chunks
   ↓
Build Context
   ↓
Grounded Prompt
   ↓
LLM
   ↓
Answer + Sources
```

Ye **RAG system** hai.

---

# PART 5 — Without RAG vs With RAG

## Without RAG

```text
User → LLM → Answer
```

Question:

```text
Why did our production deployment fail?
```

Model may say:

```text
Possible causes include CPU pressure, image pull failure,
DNS issue, NSG rule, Terraform state conflict...
```

Technically plausible, but current incident ke liye evidence nahi.

## With RAG

```text
User
 ↓
Retriever
 ↓
Current Pipeline Evidence
 ↓
LLM
 ↓
Grounded Answer
```

Retrieved evidence:

```text
[S1] Terraform apply changed AKS subnet NSG rules.
[S2] Connectivity validation failed immediately after apply.
```

Then answer can say:

```text
The retrieved evidence points to the networking change as the first area to investigate [S1][S2].
```

Better because claim traceable hai.

---

# PART 6 — RAG Does NOT Retrain the LLM

Common confusion:

```text
Documents Vector DB me daal diye
→ model ne documents learn kar liye
```

Wrong.

Actual flow:

```text
Documents remain outside model
        ↓
Relevant chunks retrieved at runtime
        ↓
Chunks temporary prompt context me jaate hain
        ↓
LLM generates answer
```

Next request me same information automatically yaad rahe, ye guaranteed nahi.

### RAG vs Training

```text
Training/Fine-tuning
Model parameters change

RAG
Model parameters same
External context changes
```

---

# PART 7 — RAG vs Fine-Tuning vs Prompting

## Normal Prompting

Use when knowledge already user provides or model likely knows.

```text
Explain Kubernetes readiness probe.
```

## RAG

Use when answer depends on external, private, large, changing, or source-traceable knowledge.

```text
According to our internal AKS runbook, what should we verify after an NSG change?
```

## Fine-Tuning

Useful when you want model behavior/style/task specialization to change consistently.

Example:

```text
Always classify support tickets into a controlled taxonomy.
```

Fine-tuning is not generally the best mechanism for frequently changing knowledge.

### Quick Rule

```text
Need latest/private facts? → RAG
Need consistent behavior/style? → fine-tuning may help
Need simple instruction? → prompting
```

---

# PART 8 — RAG Pipeline Big Picture

```text
                INDEXING SIDE

Documents
   ↓
Clean
   ↓
Chunk
   ↓
Metadata
   ↓
Embedding
   ↓
Vector Index


                QUERY SIDE

User Question
   ↓
Query Embedding
   ↓
Retrieve Top Candidates
   ↓
Filter / Threshold / Rerank
   ↓
Build Context
   ↓
Grounded Prompt
   ↓
LLM
   ↓
Validate Answer / Citations
```

RAG ek single API call nahi — ek **pipeline** hai.

---

# PART 9 — Real DevOps Use Cases

## Use Case 1 — Incident Investigation

```text
Alert / Error
   ↓
Search previous incidents + runbooks
   ↓
Relevant evidence
   ↓
Suggested investigation path
```

## Use Case 2 — Terraform Change Review

```text
Question:
What risks exist when changing AKS subnet NSG rules?

Retrieve:
- networking standards
- previous outage RCA
- Terraform module docs
```

## Use Case 3 — CI/CD Troubleshooting

```text
Pipeline error
   ↓
Retrieve pipeline runbooks
   ↓
Find known error signature
   ↓
Explain likely checks
```

## Use Case 4 — Internal Knowledge Assistant

Engineer asks:

```text
How do we perform production rollback for service X?
```

Assistant retrieves only approved production runbook and answers with sources.

---

# PART 10 — RAG Reduces Hallucination, Not Eliminates It

Even with correct retrieved context, LLM can still:

```text
- overstate evidence
- mix two sources incorrectly
- invent an unstated impact
- cite wrong source ID
- ignore context
- treat malicious document text as instruction
```

Therefore:

```text
RAG
+
Prompt Guardrails
+
Retrieval Quality
+
Validation
+
Evaluation
=
More Reliable System
```

Not:

```text
RAG = No Hallucinations
```

---

# PART 11 — Four Main RAG Failure Categories

## 1. Knowledge Failure

Correct information source me hai hi nahi.

## 2. Retrieval Failure

Correct source exists but retriever wrong chunks returns.

## 3. Context Failure

Correct chunks mile, but context badly assembled or truncated.

## 4. Generation Failure

Correct context mila but LLM unsupported statement generate kar deta hai.

Mental model:

```text
Bad Answer
   ↓
Ask where failure occurred
   ↓
Knowledge?
Retrieval?
Context?
Generation?
```

Ye debugging mindset bahut important hai.

---

# PART 12 — First Practical Thought Experiment

Documents:

```text
Doc A: AKS subnet NSG must allow required cluster traffic.
Doc B: Terraform apply can modify NSG rules.
Doc C: Docker image build uses a multi-stage Dockerfile.
```

Question:

```text
Why should I review Terraform networking changes when AKS loses connectivity?
```

Expected retrieval:

```text
Doc A + Doc B
```

Not:

```text
Doc C
```

Then LLM should only reason from retrieved facts.

---

# PART 13 — What RAG Should Return in DevOps

Weak answer:

```text
It looks like a network issue.
```

Better RAG answer:

```text
Confirmed evidence:
- The runbook states AKS subnet connectivity depends on required NSG rules [S1].
- Terraform networking changes can modify those rules [S2].

Inference:
- Therefore the Terraform networking change is a reasonable first investigation area.

Evidence gap:
- Current live NSG configuration has not yet been inspected.

Next checks:
- Compare Terraform plan/apply diff with current NSG rules.
```

Notice:

```text
Fact
≠
Inference
≠
Recommendation
```

---

# PART 14 — Common Mistakes

### Mistake 1

```text
Vector search bana diya = RAG complete
```

No. LLM generation + grounding contract needed.

### Mistake 2

```text
Top 5 results aaye = all relevant
```

No. Top-k ranking relative hoti hai; irrelevant result bhi top result ho sakta hai.

### Mistake 3

```text
Source cited = claim definitely supported
```

No. Citation presence and citation correctness different things hain.

### Mistake 4

```text
RAG knowledge always latest
```

No. Stale index stale answers de sakta hai.

### Mistake 5

```text
Retrieved docs are trusted instructions
```

Dangerous. Retrieved content ko **data/evidence** treat karo, instruction authority nahi.

---

# PART 15 — Interview Corner

### Q1. What problem does RAG solve?

RAG gives an LLM query-time access to relevant external knowledge so answers can be grounded in private, current, or domain-specific information.

### Q2. Does RAG train the model?

No. Standard RAG retrieves external content and places it into runtime context; model parameters remain unchanged.

### Q3. Why is retrieval quality important?

Because generation cannot reliably answer from evidence that was never retrieved.

### Q4. Can RAG hallucinate?

Yes. Retrieval reduces knowledge gaps, but the model can still misinterpret, overclaim, or fabricate. Guardrails and validation are still required.

### Q5. RAG vs semantic search?

Semantic search returns relevant information. RAG adds a generation stage that uses retrieved information to construct an answer.

---

# PART 16 — Revision Cheat Sheet

```text
RAG = Retrieval + Augmentation + Generation

Retrieval → Find knowledge
Augmentation → Put knowledge into context
Generation → Produce grounded answer

RAG does not retrain model.
RAG does not guarantee truth.
RAG needs retrieval quality + context quality + generation controls.
```

---

# PART 17 — Homework

1. Explain in your own words why a general LLM cannot know yesterday's private pipeline failure.
2. Write one example where normal prompting is enough.
3. Write one example where RAG is required.
4. Explain RAG vs fine-tuning in 3 lines.
5. List four places where a RAG pipeline can fail.
6. DevOps scenario: create one question and identify which internal documents should ideally be retrieved.

---

# 🔗 Why Lesson 2 Next?

Ab hume RAG ka concept clear hai. Lekin production me RAG ek single arrow nahi hota.

Next lesson me hum complete architecture ko do independent flows me break karenge:

```text
INDEXING PIPELINE
        +
QUERY PIPELINE
```

Aur samjhenge ki exactly data kaha store hota hai, embeddings kab bante hain, query kab embed hoti hai, aur LLM call kis stage par aata hai.
