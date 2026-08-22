# Module 1 — Lesson 6: Tokens, Cost & Context Engineering

> **Goal:** Beginner ko samjhana ki LLM text ko tokens me process karta hai, context finite hota hai, hosted usage/cost input-output volume se related hota hai, aur DevOps logs ko blindly dump karne ke bajay relevant evidence select karna chahiye.

---

> **Course boundary:** This lesson introduces context budgeting because it is required to make a first API application reliable. **Module 2** is the canonical deep-dive for prompt/context engineering patterns; **Module 4–5** later apply context selection to embeddings and RAG. Do not treat this lesson as a second Prompt Engineering course.

---

# 1. English Definitions

**Token:** A token is a unit of text that a language model processes internally.

**Context Window:** The context window is the maximum amount of tokenized information a model can consider during a request/conversation state, subject to model/API behavior.

**Context Engineering:** Context engineering is the deliberate selection, preparation, labeling and budgeting of information supplied to a model for a task.

Simple Hinglish:

```text
Prompt + Evidence + History
        ↓ tokenization
Input Tokens
        ↓
Model Context
        ↓
Generated Output Tokens
```

---

# 2. Why This Topic Comes Here

Lesson 5 me request/response samjha.

Ab question:

```text
Request ke andar kitna text bhej sakte hain?
Kitna useful hai?
Kitna waste/noise hai?
Hosted API usage par kya impact hai?
```

DevOps me ye especially important hai because logs and plans can be huge.

---

# 3. Token != Word

One English word may map to one or multiple tokens. Code, punctuation, JSON, paths and identifiers also consume tokens.

So avoid simplistic rule:

```text
1 word = 1 token
```

Exact tokenization model-specific ho sakti hai.

What matters operationally:

```text
More text
→ usually more input tokens
→ more processing
→ more latency/cost/noise potential
```

---

# 4. Input vs Output Tokens

Conceptually:

```text
INPUT TOKENS
= prompt + context + evidence + relevant history

OUTPUT TOKENS
= model-generated response
```

Total request footprint may involve both.

Hosted provider usage often reports token counts/usage metadata. Do not hard-code old price numbers in course logic because pricing changes.

---

# 5. Context Window Mental Model

```text
┌──────────────────────────────┐
│ Model Context Capacity       │
│                              │
│ Instructions                 │
│ Current question             │
│ Evidence                     │
│ Conversation/history         │
│ Tool results                 │
│ Output budget                │
└──────────────────────────────┘
```

If too much information is sent, APIs/models may reject, truncate or handle it according to their current behavior/configuration.

Core lesson:

> **Finite context should be treated as an engineering budget.**

---

# 6. Why DevOps Engineers Must Care

Bad idea:

```text
100 MB pipeline log
+ terraform plan
+ kubectl events
+ all historical incidents
→ send everything to LLM
```

Problems:

- context overflow
- high latency
- hosted usage/cost
- irrelevant noise
- secret leakage risk
- important evidence buried
- poorer reasoning

Better:

```text
Collect
→ Filter
→ Normalize
→ Redact
→ Source-label
→ Prioritize
→ Send relevant context
```

---

# 7. Context Quality > Context Quantity

More context is not automatically better.

Good context properties:

```text
Relevant
Current/fresh
Source-labeled
Minimal but sufficient
Redacted
Structured
Non-duplicative
```

Target:

```text
Evidence density ↑
Noise ↓
```

---

# 8. Prompt Engineering vs Context Engineering

Prompt engineering:

```text
Model ko kya karna hai?
```

Context engineering:

```text
Model ko kaunsi information dekar karwana hai?
```

Example:

```text
Prompt:
Identify the most evidence-supported root cause.

Context:
[E1] Deployment failed during Terraform Apply
[E2] NSG rule removed
[E3] AKS connectivity validation failed
```

Both matter.

For the complete prompt-engineering methodology, continue to **Module 2** rather than expanding this lesson into another prompting curriculum.

---

# 9. Raw Log vs Evidence Context

## Raw

```text
10,000 lines of build output
provider downloads
warnings
success messages
timestamps
stack traces
secret-like values
```

## Better normalized evidence

```text
[E1] Pipeline failed during Terraform Apply.
[E2] Terraform removed aks-subnet-allow.
[E3] AKS subnet connectivity validation failed after change.
```

This is easier to reason over and validate.

---

# 10. Source Labels

Instead of:

```text
NSG rule removed.
```

Use:

```text
[E2][terraform_plan] NSG rule aks-subnet-allow removed.
```

Benefits:

- citations
- traceability
- claim validation
- conflict handling

Later RAG modules use the same principle at larger scale.

---

# 11. Freshness Matters

Current incident evidence and old runbooks are different.

```text
Current evidence:
What is happening now?

Reference knowledge:
What usually should happen?
```

Do not merge blindly.

Example:

```text
[E1] Current AKS status = degraded
[R1] Runbook says verify NSG/UDR/DNS
```

R1 can guide investigation but does not prove current cause.

---

# 12. Context != Memory

Important distinction:

```text
Context
= information actually supplied to model now

Application State
= data preserved by host across workflow steps

Conversation History
= prior messages

Evidence
= validated observations supporting facts
```

They can overlap, but are not identical.

---

# 13. Hosted Cost Thinking

Do not memorize a static price table in the lesson.

Instead understand drivers:

```text
more input
+ more output
+ more calls
+ more expensive model tier
= potentially higher hosted cost
```

Operational strategy:

- log usage metadata
- set request budgets
- reduce duplicate calls
- compress context carefully
- choose model according to task

---

# 14. Local Ollama Cost Thinking

No hosted per-call bill for local inference does not mean resource-free.

You still spend:

```text
CPU/GPU
RAM/VRAM
electricity
latency
hardware capacity
operations
```

So:

```text
Local = different cost model
not zero engineering cost
```

---

# 15. Practical Token/Context Experiment

Use the same question three times.

## Version A — Minimal

```text
Why did the deployment fail?
```

## Version B — Huge noisy context
Include irrelevant lines and warnings.

## Version C — Curated evidence

```text
[E1] Deployment failed during Terraform Apply.
[E2] NSG rule aks-subnet-allow removed.
[E3] AKS connectivity validation failed.
```

Compare:

```text
Relevance
Unsupported claims
Latency
Output length
Hosted usage metadata
```

---

# 16. Example Python Measurement

Hosted path:

```python
response = client.responses.create(
    model=model,
    input=context,
)

print(response.usage)
print(response.output_text)
```

Do not assume exact token values across models/providers.

For Ollama, runtime responses may expose their own evaluation/token-like counters depending on endpoint and version.

---

# 17. Secret Redaction Before Context

Never send secret just because model context has room.

Bad:

```text
AZURE_CLIENT_SECRET=abc123
```

Better:

```text
AZURE_CLIENT_SECRET=[REDACTED]
```

Redaction should happen **before** sending data to model.

---

# 18. Chunking Preview

If knowledge/log data is too large:

```text
Large Document
→ Split into chunks
→ Retrieve relevant chunks
→ Send only top context
```

This is foundation for Module 4/5 embeddings and RAG.

Here we only learn the motivation.

---

# 19. Summarization Risk

Summarization reduces size but can lose detail.

Bad:

```text
LLM summarizes log
→ original source discarded
→ later claim impossible to verify
```

Better:

```text
Original evidence preserved
+ summary generated
+ source IDs retained
```

Never let summary become the only evidence source if auditability matters.

---

# 20. Context Budget Strategy

A simple application policy could be:

```text
1. System instructions
2. Current user question
3. Highest-priority current evidence
4. Limited reference knowledge
5. Output budget
```

Drop:

```text
irrelevant chat
repeated logs
old unrelated incidents
secrets
```

---

# 21. Failure Modes

### Too little context
Model guesses.

### Too much context
Noise and capacity/cost problems.

### Wrong context
Confident wrong answer.

### Stale context
Old state treated as current.

### Untrusted context
Prompt injection or poisoned data risk later.

### Secret-containing context
Security incident.

---

# 22. Production Observability

Track per request:

```text
input size/tokens
output size/tokens
latency
model
request count
context source count
retrieval score later
error status
```

Why?

```text
Cost regression
Latency regression
Prompt/context bloat
Model comparison
```

---

# 23. Common Beginner Mistakes

1. Token = word.
2. More context always better.
3. Context window = permanent memory.
4. Chat history = evidence.
5. Runbook = current incident fact.
6. Large log directly LLM ko dena.
7. Secret redaction ignore karna.
8. Summarization ke baad original source delete karna.
9. Static provider pricing hard-code karna.
10. Local inference ko costless system samajhna.

---

# 24. Interview Q&A

### Q1. What is a token?
A model-processing unit derived from text/code.

### Q2. What is a context window?
The finite amount of tokenized information the model can consider for a request/conversation context, subject to model behavior.

### Q3. Why not send complete logs?
They increase noise, token use, latency, secret risk and can bury relevant evidence.

### Q4. Prompt engineering vs context engineering?
Prompt engineering designs instructions; context engineering selects/prepares the information supplied for the task.

### Q5. Is conversation history evidence?
Not automatically.

### Q6. Why label evidence sources?
For traceability, validation and citations.

### Q7. Is local LLM zero-cost?
No hosted per-call charge for local inference, but hardware and operational resources still cost.

### Q8. How do you reduce context safely?
Filter, normalize, redact, deduplicate, preserve provenance and retrieve only relevant information.

---

# 25. Revision Sheet

```text
Token = processing unit
Input tokens = supplied text/context
Output tokens = generated content
Context window = finite working capacity
Context engineering = select/prepare useful information
More context != more truth
History != evidence
Reference != current proof
```

---

# 26. Homework

1. Take a sample log and create raw, trimmed and evidence-labeled versions.
2. Run same prompt against all three.
3. Compare output quality and latency.
4. If using hosted API, inspect usage metadata.
5. Identify one secret-like field and redact it before model input.
6. Explain why old runbook cannot prove a current incident cause.

---

# 27. Why Next Lesson?

Ab hum relevant context model ko de sakte hain.

But free-text response automation ke liye unreliable ho sakta hai.

Next problem:

```text
Model output ko predictable machine-readable contract me kaise laayein?
```

➡️ **Lesson 7 — Structured Output & Validation**
