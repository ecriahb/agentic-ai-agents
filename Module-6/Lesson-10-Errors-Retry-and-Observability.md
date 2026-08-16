# 🚩 Jai Bajrangbali!

# Lesson 10 — Errors, Retry & Observability

> **Production orchestration ka quality happy path se nahi, failure behavior aur visibility se judge hota hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- error categories
- retryable vs non-retryable failures
- timeout strategy
- backoff and jitter intuition
- fallback use cases
- tracing and callbacks
- latency/token/cost metrics
- workflow stage observability
- unsafe retry patterns

---

# PART 1 — Failure Taxonomy

AI workflow failures broadly:

```text
INPUT ERROR
DEPENDENCY ERROR
MODEL ERROR
RETRIEVAL ERROR
TOOL ERROR
PARSER ERROR
VALIDATION ERROR
POLICY ERROR
```

A single message `Something went wrong` production debugging ke liye useless hai.

---

# PART 2 — Retry Is a Policy

Retry every exception is dangerous.

### Often retryable

```text
transient network error
HTTP 429
HTTP 5xx
temporary timeout
read-only dependency unavailable
```

### Usually not retryable without change

```text
invalid API key
403 permission denied
invalid tool argument
schema validation failure
unsupported model
policy rejection
```

### Side-effect caution

```text
terraform apply
production restart
resource deletion
```

Never generic automatic retry without idempotency design.

---

# PART 3 — Timeout

Every external call should have bounded waiting.

```text
Retriever timeout
Model timeout
Tool/API timeout
```

Without timeout:

```text
one dependency hangs
→ whole workflow hangs
```

Production timeout policy should consider expected latency and user SLA.

---

# PART 4 — Exponential Backoff + Jitter

Conceptual schedule:

```text
attempt 1 → wait ~1s
attempt 2 → wait ~2s
attempt 3 → wait ~4s
```

Jitter randomizes slightly so many clients do not retry at exact same moment.

But keep maximum attempts bounded.

---

# PART 5 — Framework Retry Concept

Composable frameworks may allow retry behavior around a runnable/component.

Mental model:

```text
Model Runnable
   ↓ failure
Retry policy
   ↓
Model Runnable again
```

Important:

> Attach retries to safe component boundaries, not blindly to entire chain containing side effects.

---

# PART 6 — Fallback

Fallback examples:

```text
Primary model unavailable
→ secondary model

Vector search unavailable
→ keyword search

Structured parser fails
→ one controlled repair attempt
```

Fallback must preserve safety policy.

Bad fallback:

```text
retrieval unavailable
→ let model answer from memory as if grounded
```

Better:

```text
RETRIEVAL_UNAVAILABLE
```

---

# PART 7 — Observability Layers

Track at least:

```text
request ID
incident ID
workflow stage
start/end time
latency
status
retry count
model/provider
retrieval top-k
selected sources
token usage
validation result
error category
```

Do not log secrets or sensitive raw prompts blindly.

---

# PART 8 — Tracing Mental Model

```text
Trace: request-123

├─ input_validation       3 ms
├─ retriever            120 ms
├─ context_builder        5 ms
├─ model_call          2100 ms
├─ parser                12 ms
└─ evidence_validation    4 ms
```

Now latency problem visible hai.

Without trace:

```text
"RAG slow hai"
```

With trace:

```text
model call = 82% latency
```

---

# PART 9 — Token / Context Observability

Monitor:

```text
input tokens
output tokens
number of retrieved chunks
context characters/tokens
model latency
```

Why?

```text
too much retrieval
→ context grows
→ latency/cost grows
→ relevance may drop
```

---

# PART 10 — Retrieval Metrics

At runtime useful telemetry:

```text
retrieval count
best score
source IDs
filter applied
no-context frequency
```

Do not expose sensitive similarity scores/metadata unnecessarily to users, but preserve for internal diagnostics.

---

# PART 11 — DevOps Example

Flow:

```text
get_pipeline_status
→ timeout
→ retry once
→ success

retriever
→ success

LLM
→ 429
→ backoff
→ retry
→ success

parser
→ schema invalid
→ fail explicitly
```

Do not silently convert parser failure into a trusted RCA.

---

# PART 12 — Logging Safety

Never casually log:

```text
API keys
Authorization headers
full secrets
private tokens
sensitive customer documents
```

Use:

```text
redaction
hash/reference IDs
safe summaries
restricted logs
retention policy
```

---

# PART 13 — Error Contract

Instead of random exception text, return structured internal error:

```json
{
  "stage": "retrieval",
  "code": "DEPENDENCY_TIMEOUT",
  "retryable": true,
  "request_id": "req-123"
}
```

User-facing message can be simpler.

---

# PART 14 — Common Mistakes

- retry whole agent loop
- no max attempts
- fallback to ungrounded answer
- raw prompts with secrets logged
- no request correlation ID
- parser errors hidden
- all 4xx treated same
- model timeout infinite

---

# PART 15 — Interview Q&A

### Q1. What should determine retry behavior?
Error type, side effects, idempotency, provider guidance, latency budget and maximum attempts.

### Q2. Why not retry an entire workflow?
Because some earlier stages may have side effects or duplicate actions.

### Q3. What should AI observability capture?
Per-stage latency/status, model usage, retrieval metadata, retries, validation outcomes and correlated errors while protecting sensitive data.

### Q4. What is a safe RAG fallback if retrieval is unavailable?
Return an explicit unavailable/insufficient-evidence state rather than presenting model-memory output as grounded.

---

# PART 16 — Revision

```text
Timeout = bounded waiting
Retry = controlled reattempt
Backoff = increasing delay
Jitter = randomized delay
Fallback = alternate safe path
Trace = stage-by-stage visibility
```

---

# PART 17 — Homework

Create retry matrix:

| Failure | Retry? | Max | Reason |
|---|---|---:|---|
| 429 model API | ? | ? | |
| invalid API key | ? | ? | |
| read-only status timeout | ? | ? | |
| terraform apply timeout | ? | ? | |
| parser invalid JSON | ? | ? | |

Explain each.

---

# 🔁 Next Lesson Kyu?

Ab components, tools, state aur reliability pieces ready hain. Next lesson me इन्हें ek realistic **DevOps incident workflow** me orchestrate karenge.
