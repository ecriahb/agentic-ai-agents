# 🚩 Jai Bajrangbali!

# Lesson 08 — Prompt Chaining

> **Complex investigation ko one giant prompt me force karne ke bajay small, testable stages me split karo.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- prompt chain kya hai
- chain vs agent difference
- stage-specific inputs/outputs
- DevOps investigation decomposition
- error propagation risk
- deterministic gates between stages
- when chaining helps and when it adds unnecessary complexity
- provider-independent chain design

---

# 1. English Definition

**Prompt chaining is a workflow pattern in which a complex task is broken into multiple model or application stages, where the validated output of one stage becomes input to the next.**

Mental model:

```text
Input
 ↓
Stage 1
 ↓ validate
Stage 2
 ↓ validate
Stage 3
 ↓
Final Output
```

---

# 2. Why Chain?

One huge prompt:

```text
Read logs, identify timeline, find root cause, compare runbook, calculate impact,
recommend fix, generate ticket, decide whether to execute remediation...
```

This mixes too many responsibilities.

Better:

```text
Evidence extraction
→ Timeline
→ Hypothesis generation
→ Evidence support check
→ RCA report
```

Each stage is easier to inspect and test.

---

# 3. Chain vs One Prompt

## One prompt

Advantages:

- simple
- lower orchestration code
- sometimes lower latency

Risks:

- harder to debug
- hidden intermediate assumptions
- output may skip steps

## Chain

Advantages:

- explicit stages
- per-stage validation
- easy observability
- different stages can be deterministic

Costs:

- more calls
- more latency/cost
- error propagation
- state management

Use complexity only when justified.

---

# 4. DevOps Incident Chain

```text
Raw Logs
   ↓
Stage 1 — Extract factual events
   ↓
[E1][E2][E3]
   ↓
Stage 2 — Build timeline
   ↓
Stage 3 — Generate hypotheses
   ↓
Stage 4 — Check hypothesis support
   ↓
Stage 5 — Generate final RCA
```

Important:

```text
Stage 3 hypothesis is NOT evidence.
```

Keep trust classes separate.

---

# 5. Stage Contract Example

## Stage 1

Input:

```text
raw pipeline log
```

Output:

```json
{
  "events": [
    {"id":"E1", "type":"terraform_change", "summary":"..."}
  ]
}
```

Host validates schema before Stage 2.

## Stage 2

Input:

```text
validated events
```

Output:

```text
ordered timeline
```

No need to send raw unrelated logs again.

---

# 6. Deterministic Stages

Not every stage needs LLM.

Example:

```text
Timestamp sorting → Python
Citation ID check → Python
Allowed environment validation → Python
Hypothesis prose → LLM
```

Best pattern:

```text
Use deterministic code where rules are deterministic.
Use LLM where language/reasoning flexibility adds value.
```

---

# 7. Error Propagation

If Stage 1 invents:

```text
E4: node NotReady
```

and Stage 2/3 trust it blindly, hallucination gets amplified.

So between stages:

```text
model output
→ validation
→ accepted state
```

Never automatically promote free-form model output to trusted evidence.

---

# 8. Chain Stop Conditions

Example:

```text
if no current evidence:
    stop → INSUFFICIENT_EVIDENCE

if required source failed:
    stop/escalate → EVIDENCE_COLLECTION_FAILED

if hypothesis unsupported:
    request more evidence or final UNKNOWN
```

A chain needs explicit failure states, not only success path.

---

# 9. Prompt Chain vs Agent

Prompt chain:

```text
predetermined stages
A → B → C
```

Agent:

```text
runtime decides next step/tool based on state
```

Do not call every chain an agent.

This distinction prepares you for Module 8.

---

# 10. Provider Independence

A chain can call:

```text
Ollama at Stage 3
or
OpenAI at Stage 3
```

while stages 1/2/4 remain the same.

Provider should be dependency of a node/stage, not owner of application workflow.

This makes provider comparison and migration safer.

---

# 11. Mixed Provider Warning

A production system could theoretically use different models per stage.

But this adds:

- behavior differences
- privacy/egress complexity
- cost tracking
- more eval combinations

Do not introduce multi-provider routing just because it is possible.

---

# 12. Practical Chain Exercise

Create three Python functions:

```python
extract_events(log_text)
build_timeline(events)
build_rca(timeline, evidence)
```

At first, make `extract_events` deterministic using known log patterns.
Use LLM only for RCA prose.

Then test same final LLM stage with Ollama/OpenAI.

Expected learning:

```text
workflow stays stable
model output wording changes
validation remains required
```

---

# 13. Observability

Log per stage:

```text
stage name
input source IDs
output status
latency
provider/model if LLM used
validation result
error category
```

Do not log secrets/full sensitive prompts blindly.

---

# 14. Common Mistakes

1. Every stage uses LLM unnecessarily.
2. Stage output trusted without validation.
3. No stop/failure states.
4. Full raw context repeated at every stage.
5. Hypothesis becomes evidence in later stage.
6. Too many stages increase latency without value.
7. Provider/model changes not regression-tested.

---

# 15. Interview Q&A

### Q1. What is prompt chaining?
Breaking a complex task into sequential validated stages where one stage's output feeds the next.

### Q2. Why use a chain instead of one prompt?
Better decomposition, testability, observability and per-stage validation.

### Q3. Biggest risk?
Error/hallucination propagation if intermediate outputs are trusted blindly.

### Q4. Chain vs agent?
Chain follows predetermined flow; agent can dynamically choose next actions based on state.

### Q5. Should every stage be LLM-based?
No. Deterministic logic should remain deterministic where possible.

---

# 16. Quick Revision

```text
Complex Task
→ Small Stage
→ Validate
→ Next Stage
```

Core rule:

```text
Intermediate model output != automatically trusted state
```

---

# 🧪 Homework

Design a chain for:

```text
Terraform plan → risk review → approval recommendation
```

Mark each stage as:

```text
DETERMINISTIC
or
LLM
```

Explain why.

---

# ➡️ Why Next?

Chains have predetermined flow. But agent loops can dynamically choose tools and repeat steps. Next lesson covers **Agent Loop Prompts & Guardrails**.
