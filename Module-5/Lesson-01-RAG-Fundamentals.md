# 🚩 Jai Bajrangbali!

# Lesson 01 — RAG Fundamentals

> **RAG ka simple goal: query time par relevant external/reference knowledge retrieve karke usse LLM ke context mein dena, taaki answer available evidence se grounded ho sake.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap clearly samjhoge:

- RAG kya hai aur kyu bana
- LLM ki learned knowledge aur external/reference knowledge me difference
- Retrieval, Augmentation aur Generation teen alag stages kyu hain
- Module 4 retrieval foundation aur Module 5 complete RAG pattern ke beech exact boundary
- RAG vs fine-tuning vs normal prompting
- DevOps me RAG ka real use kaha hota hai
- RAG hallucination ko reduce kaise karta hai — aur completely eliminate kyu nahi karta
- RAG ke common failure modes
- evidence, inference aur recommendation ko alag kaise rakhna hai

> **Prerequisite:** Module 4 mein embeddings, similarity search, vector stores/indexes aur Top-K retrieval complete kiya gaya hai. Is lesson mein un concepts ka sirf short recall hai; unki detailed theory Module 4 mein canonical hai.

---

# PART 1 — Problem: LLM Sab Kuch Nahi Jaanta

Suppose user asks:

```text
Yesterday production AKS deployment Terraform Apply ke baad kyu fail hua?
```

General LLM ko automatically ye private/current information nahi pata ho sakti:

```text
- kal ka pipeline log
- aapke Terraform plan ka exact diff
- aapki company ka AKS runbook
- aapka internal NSG naming standard
- latest incident notes
```

Model ke learned parameters general patterns represent karte hain, lekin aapke live/private operational state ka automatic source of truth nahi hote.

### Mental Model

```text
LLM learned knowledge
        ≠
Your live / private / latest operational knowledge
```

Isi gap ko RAG address karta hai.

---

# PART 2 — English Definition

**Retrieval-Augmented Generation (RAG)** is an AI architecture in which relevant external information is retrieved at query time and supplied to a language model as context so that the generated answer can be grounded in that information.

Simple Hinglish:

```text
Question
   ↓
Relevant reference/evidence search karo
   ↓
LLM ko selected context do
   ↓
Context ke basis par answer generate karao
```

Important boundary:

> **Retrieved content is not automatically trustworthy or authoritative. Retrieval makes information available; grounding and validation determine whether a claim is actually supported.**

---

# PART 3 — RAG Naam Ko Break Karo

## R = Retrieval

Question ke liye potentially useful information find karna.

Module 4 ka recall:

```text
Query
  ↓
Query embedding
  ↓
Similarity / vector search
  ↓
Candidate chunks
```

Detailed embeddings, metrics, vector indexes and Top-K mechanics **Module 4 mein already covered hain**.

## A = Augmentation

Retrieved information ko LLM ke prompt/context me attach karna.

```text
QUESTION
+ SELECTED REFERENCE/EVIDENCE
+ OUTPUT / GROUNDING RULES
```

## G = Generation

LLM supplied context ko use karke answer banata hai.

```text
Context → Explanation / RCA / Recommended checks
```

Important:

> Retrieval khud answer generation nahi hai. Generation khud retrieval nahi hai.

---

# PART 4 — Module 4 vs Module 5

Module 4 ka canonical responsibility:

```text
Question
   ↓
Embedding
   ↓
Vector Search
   ↓
Relevant / ranked chunks
```

Output:

```text
[S1] AKS networking runbook...
[S2] Terraform NSG guidance...
```

Module 5 ka responsibility retrieval ko complete answer-generation pattern mein convert karna hai:

```text
Question
   ↓
Retrieve candidates
   ↓
Select / filter / rerank as required
   ↓
Build context
   ↓
Grounded prompt
   ↓
LLM
   ↓
Answer + source mapping
   ↓
Validation
```

So:

```text
Module 4 = retrieval foundation
Module 5 = RAG system pattern
```

---

# PART 5 — Reference Knowledge vs Current Incident Evidence

DevOps RAG mein ek important distinction hai.

### Reference knowledge

Examples:

```text
AKS networking runbook
Terraform module documentation
Security standard
Rollback SOP
```

Ye batata hai ki system **normally kaise work karna chahiye** ya approved process kya hai.

### Current incident evidence

Examples:

```text
Current pipeline log
Current Terraform plan/apply diff
Current NSG configuration
Current deployment event
```

Ye batata hai ki **abhi actually kya hua**.

### Why this matters

RAG retrieval se reference material mil sakta hai, lekin current incident ka fact automatically prove nahi hota.

```text
Reference knowledge
        ≠
Current-state evidence
```

Production RCA mein dono ko clearly label karna chahiye.

---

# PART 6 — Without RAG vs With RAG

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
Selected reference/evidence
 ↓
LLM
 ↓
Grounded Answer
```

Retrieved reference evidence:

```text
[S1] The runbook states that required AKS subnet traffic must be allowed.
[S2] Terraform networking changes can modify NSG rules.
```

A careful answer should say:

```text
The retrieved references make the networking change a reasonable
first investigation area [S1][S2]. The current NSG state still
needs to be checked before claiming that it caused this incident.
```

This is stronger than presenting a plausible hypothesis as a confirmed fact.

---

# PART 7 — RAG Does NOT Retrain the LLM

Common confusion:

```text
Documents Vector DB me daal diye
→ model ne documents learn kar liye
```

Wrong.

Actual flow:

```text
Documents remain outside model parameters
        ↓
Relevant chunks retrieved at runtime
        ↓
Chunks prompt/context me jaate hain
        ↓
LLM generates answer
```

### RAG vs Training

```text
Training/Fine-tuning
→ model parameters/behavior are changed

RAG
→ model parameters remain unchanged
→ external context is supplied at runtime
```

---

# PART 8 — RAG vs Fine-Tuning vs Prompting

## Normal Prompting

Use when the required knowledge is supplied in the prompt/context or the task does not need external retrieval.

```text
Explain Kubernetes readiness probe.
```

## RAG

Use when the answer depends on external, private, changing, large, or source-traceable knowledge.

```text
According to our internal AKS runbook, what should we verify after an NSG change?
```

## Fine-Tuning

Useful when you want model behavior or task specialization to change consistently. It is not generally the first mechanism for frequently changing factual knowledge.

Example:

```text
Always classify support tickets into a controlled taxonomy.
```

### Quick Rule

```text
Need external/current/private facts? → consider RAG
Need consistent behavior/style/task specialization? → consider fine-tuning
Need a direct instruction or supplied context? → prompting
```

These are not mutually exclusive; production systems can combine them.

---

# PART 9 — RAG Pipeline Big Picture

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
Vector Store / Index


                QUERY SIDE

User Question
   ↓
Query Embedding
   ↓
Retrieve Candidates
   ↓
Filter / Threshold / Rerank as required
   ↓
Build Context
   ↓
Grounded Prompt
   ↓
LLM
   ↓
Validate Answer / Source Mapping
```

RAG ek single API call nahi — ek **pipeline** hai.

> **Module 4 owns the embedding/vector retrieval foundation. Module 5 owns what happens after retrieval and how retrieval becomes a grounded generation system.**

---

# PART 10 — Real DevOps Use Cases

## Use Case 1 — Incident Investigation

```text
Alert / Error
   ↓
Retrieve relevant runbooks + historical references
   ↓
Correlate with current incident evidence
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
Compare with current pipeline evidence
   ↓
Explain supported checks
```

## Use Case 4 — Internal Knowledge Assistant

Engineer asks:

```text
How do we perform production rollback for service X?
```

Assistant retrieves approved production runbook and answers with source mapping.

---

# PART 11 — RAG Reduces Hallucination, Not Eliminates It

Even with relevant retrieved context, an LLM can still:

```text
- overstate evidence
- mix two sources incorrectly
- invent an unstated impact
- cite the wrong source ID
- ignore relevant context
- treat malicious document text as an instruction
```

Therefore:

```text
RAG
+
Prompt / grounding rules
+
Retrieval quality
+
Validation
+
Evaluation
=
More reliable system
```

Not:

```text
RAG = No Hallucinations
```

---

# PART 12 — Four Main RAG Failure Categories

## 1. Knowledge Failure

Correct information source me hai hi nahi.

## 2. Retrieval Failure

Correct source exists but retriever wrong or insufficient chunks returns.

## 3. Context Failure

Correct chunks mile, but context badly assembled, prioritized, or truncated.

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

# PART 13 — Evidence-Grounded DevOps Answer

Weak answer:

```text
It looks like a network issue.
```

Better answer:

```text
Reference evidence:
- The runbook states AKS subnet connectivity depends on required NSG rules [S1].
- Terraform networking changes can modify those rules [S2].

Current-state evidence:
- The current NSG configuration has not yet been inspected.

Inference:
- Therefore the Terraform networking change is a reasonable first investigation area.

Next checks:
- Compare Terraform plan/apply diff with the current NSG rules.
```

Notice:

```text
Fact / evidence
       ≠
Inference
       ≠
Recommendation
```

This separation becomes especially important in production RCA agents.

---

# PART 14 — Common Mistakes

### Mistake 1

```text
Vector search bana diya = RAG complete
```

No. Context construction + generation + grounding/validation are still required.

### Mistake 2

```text
Top 5 results aaye = all relevant
```

No. Top-K is a retrieval setting, not a guarantee of relevance.

### Mistake 3

```text
Source cited = claim definitely supported
```

No. Citation presence and citation correctness are different things.

### Mistake 4

```text
RAG knowledge always latest
```

No. A stale or incomplete index can produce stale or incomplete answers.

### Mistake 5

```text
Retrieved docs are trusted instructions
```

Dangerous. Retrieved content should be treated as **data/evidence**, not automatically as instruction authority.

---

# PART 15 — Interview Corner

### Q1. What problem does RAG solve?

RAG gives an LLM query-time access to relevant external knowledge so answers can be grounded in private, current, or domain-specific information.

### Q2. Does RAG train the model?

No. Standard RAG retrieves external content and places it into runtime context; model parameters remain unchanged.

### Q3. Why is retrieval quality important?

Because generation cannot reliably use evidence that was never retrieved or selected into context.

### Q4. Can RAG hallucinate?

Yes. Retrieval reduces knowledge gaps, but the model can still misinterpret, overclaim, or fabricate. Guardrails and validation are still required.

### Q5. RAG vs semantic search?

Semantic search retrieves relevant information. RAG adds context construction and generation so the retrieved information can be used to produce an answer.

---

# PART 16 — Revision Cheat Sheet

```text
RAG = Retrieval + Augmentation + Generation

Retrieval   → Find relevant external information
Augmentation → Put selected information into model context
Generation  → Produce an answer using that context

RAG does not retrain the model.
RAG does not guarantee truth.
RAG does not make retrieved documents automatically trustworthy.
RAG needs retrieval quality + context quality + generation controls.
```

---

# PART 17 — Homework

1. Explain in your own words why a general LLM cannot know yesterday's private pipeline failure.
2. Write one example where normal prompting is enough.
3. Write one example where RAG is required.
4. Explain RAG vs fine-tuning in 3 lines.
5. List four places where a RAG pipeline can fail.
6. DevOps scenario: create one question and identify which reference documents and current-state evidence should ideally be retrieved.
7. For your scenario, label each statement as **evidence, inference, or recommendation**.

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
