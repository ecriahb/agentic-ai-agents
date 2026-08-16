# 🚩 Jai Bajrangbali!

# Lesson 07 — Retry, Loop Limits & Termination

> **An agent without hard stopping rules is not autonomous intelligence; it is an unbounded failure mode.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- retry aur loop me difference
- transient vs permanent failures
- max iterations kyu host-controlled hona chahiye
- termination states ka design
- duplicate calls and idempotency
- retry backoff and side-effect risk
- recursion/loop limits ko business policy ke saath kaise use karein

---

# PART 1 — Retry vs Loop

**Retry** means same operation ko failure ke baad dubara try karna.

**Loop** means workflow intentionally another reasoning/action cycle me jaana.

Example:

```text
AKS API timeout → retry same call
```

vs

```text
AKS evidence insufficient → choose a different tool → next agent iteration
```

Do not mix these concepts.

---

# PART 2 — Failure Taxonomy

### Transient

```text
timeout
429 / rate limit
temporary 5xx
network reset
```

May be retryable.

### Permanent / Non-retryable

```text
invalid arguments
401 unauthenticated
403 unauthorized
unknown cluster
schema validation failure
policy rejection
```

Blind retry wastes time and may amplify load.

---

# PART 3 — Retry Policy

```text
Attempt 1
 ↓ fail transient
wait
 ↓
Attempt 2
 ↓ fail
wait longer + jitter
 ↓
Attempt 3
 ↓ fail
record TOOL_ERROR / stop or alternate path
```

Policy fields:

```text
max_attempts
base_delay
max_delay
retryable_errors
per-tool timeout
```

---

# PART 4 — Agent Iteration Limit

State:

```python
{
  "iteration": 3,
  "max_iterations": 5
}
```

Router:

```python
def loop_gate(state):
    if state["iteration"] >= state["max_iterations"]:
        return "max_iterations_reached"
    return "continue"
```

Model should not increase its own limit.

---

# PART 5 — Why Infinite Loops Happen

Common pattern:

```text
planner asks tool A
result weak
planner asks tool A again
result same
planner asks tool A again
...
```

Prevent with:

```text
duplicate detection
fresh-result reuse
evidence gap tracking
max iterations
no-progress detection
```

---

# PART 6 — No-Progress Detection

Track useful state changes:

```text
new evidence IDs?
new evidence gap closed?
quality improved?
new route discovered?
```

If N iterations produce no meaningful progress:

```text
→ NO_PROGRESS
→ ask human / return insufficient evidence
```

This is stronger than only counting loops.

---

# PART 7 — Termination States

Use explicit statuses:

```text
SUCCESS
INSUFFICIENT_EVIDENCE
MAX_ITERATIONS_REACHED
NO_PROGRESS
POLICY_BLOCKED
HUMAN_REJECTED
VALIDATION_FAILED
FATAL_TOOL_ERROR
```

Do not collapse everything into `failed=True`.

---

# PART 8 — Side Effects and Retry

Danger:

```text
restart_deployment()
network timeout after request
client retries
restart happens twice
```

For write actions use:

```text
idempotency keys
operation IDs
status checks
human approval
careful retry policy
```

Read-only investigation should come first.

---

# PART 9 — Interrupt Replay Connection

When a graph resumes after an interrupt, node execution semantics matter. Code before an interrupt may run again depending on framework/runtime behavior.

Therefore side effects before pause points should be idempotent or moved to safer nodes.

Core rule:

```text
Pause/resume design must consider replay.
```

---

# PART 10 — Timeouts at Multiple Layers

```text
HTTP timeout
MCP tool timeout
model timeout
node timeout
whole workflow deadline
```

One global timeout is not enough.

Production state can carry:

```python
{
  "started_at": "...",
  "deadline": "..."
}
```

Router can stop if workflow deadline exceeded.

---

# PART 11 — Retry Budget

Instead of independent unlimited retries:

```text
workflow retry budget = 6 total transient retries
```

This prevents 10 tools × 3 retries = 30 hidden calls.

Track:

```text
retry_count_by_tool
total_retry_count
last_error
```

---

# PART 12 — DevOps Example

```text
Iteration 1: pipeline evidence found
Iteration 2: Terraform tool timeout → retry succeeds
Iteration 3: AKS status found
Iteration 4: planner repeats AKS status with same args
           → duplicate blocked
           → no new gap
           → proceed to analysis
```

---

# PART 13 — Common Mistakes

- retry every exception
- no backoff
- model chooses retry count
- no max agent iterations
- write action retried blindly
- no duplicate call detection
- only technical exception, no explicit business status
- no workflow deadline

---

# PART 14 — Interview Q&A

### Q1. Retry vs agent loop?
Retry repeats an operation due to failure; an agent loop intentionally performs another decision/action cycle.

### Q2. Who should control max iterations?
Application policy, not the model.

### Q3. Why are write retries dangerous?
A request may have succeeded even when the response failed, causing duplicate side effects.

### Q4. What is no-progress detection?
A policy that stops/re-routes when repeated iterations do not add useful evidence or state change.

---

# PART 15 — Revision

```text
Retry = same operation after transient failure
Loop = another reasoning/action cycle
Limit = hard application policy
No progress = semantic termination signal
Idempotency = safe replay protection
```

---

# PART 16 — Homework

Create retry/termination policy for:

```text
get_pipeline_status
get_terraform_changes
restart_deployment
```

Explain why each has different retry rules.

---

# 🔁 Next Lesson Kyu?

Loops bounded hain. Ab risky actions ke liye automation ko **pause karke human decision** lena hoga. Next lesson: Human-in-the-Loop and approval gates.
