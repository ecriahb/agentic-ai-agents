# 🚩 Jai Bajrangbali!

# Lesson 03 — State Models, Schemas & Reducers

> **Agar state unclear hai, to agent ka behavior bhi unclear hoga. Good graph design starts with explicit state contracts.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- graph state kya represent karta hai
- state schema kyu important hai
- state fields ko trust classes me kaise divide karein
- nodes state ko kaise update karte hain
- reducers kya problem solve karte hain
- list/evidence accumulation safely kaise hoti hai
- volatile state, durable state and evidence references

---

# PART 1 — English Definition

A **state schema** defines the structure and expected fields of the shared data that flows through a graph.

A **reducer** defines how updates to a state field are combined when new values are produced.

---

# PART 2 — Bad State Design

```python
state = {
    "data": "everything",
    "history": [...],
    "result": "maybe final",
}
```

Problems:

```text
What is trusted?
What is model-generated?
What is current?
What can be overwritten?
What must accumulate?
```

---

# PART 3 — Better DevOps State

```python
class IncidentState(TypedDict):
    incident_id: str
    environment: str
    failure_stage: str | None
    evidence: list[dict]
    reference_docs: list[dict]
    iteration: int
    evidence_quality: str
    proposed_action: dict | None
    approval_status: str
    final_status: str | None
```

Each field has one clear responsibility.

---

# PART 4 — Trust Classes in State

Recommended classification:

```text
REQUEST
- user goal
- incident id

TRUSTED APPLICATION STATE
- environment resolved by host
- iteration count
- allowlisted tools
- approval status

CURRENT EVIDENCE
- tool outputs
- source/timestamp

REFERENCE KNOWLEDGE
- runbooks / RAG chunks

MODEL OUTPUT
- hypotheses
- RCA draft
- proposed next step
```

Do not merge these into one anonymous `context` field.

---

# PART 5 — State Update Mental Model

Node receives state:

```text
State v1
  ↓
Node
  ↓
Partial Update
  ↓
State v2
```

Example:

```python
def classify_node(state):
    return {"failure_stage": "terraform"}
```

Node generally returns the fields it updates instead of mutating unrelated state.

---

# PART 6 — Evidence Accumulation Problem

Suppose three nodes produce:

```text
pipeline node → [E1]
terraform node → [E2]
AKS node → [E3]
```

If normal overwrite semantics are used, later update may replace previous list.

Desired:

```text
[E1] + [E2] + [E3]
```

This is where reducer semantics matter.

---

# PART 7 — Reducer Concept

Conceptual Python:

```python
from typing import Annotated, TypedDict
import operator

class State(TypedDict):
    evidence: Annotated[list[dict], operator.add]
```

Mental model:

```text
old evidence + new evidence → accumulated evidence
```

Important:

```text
Reducer behavior is part of state contract.
```

---

# PART 8 — Duplicate Evidence Risk

Accumulation can also create duplicates.

Example after retry:

```text
E2 added
node retries
E2 added again
```

Production strategy:

```text
stable evidence ID
source + operation + args + observation timestamp
idempotency / deduplication
```

Reducer does not automatically guarantee semantic uniqueness.

---

# PART 9 — Evidence Envelope Reuse from Module 7

```python
{
  "id": "E2",
  "kind": "CURRENT_EVIDENCE",
  "source": "terraform-mcp",
  "operation": "get_terraform_changes",
  "arguments": {"environment": "production"},
  "observed_at": "...",
  "payload": {...}
}
```

Module 8 state may keep this evidence directly for learning, or persist it externally and keep IDs in production.

---

# PART 10 — State Is Not a Database

Do not put everything into state forever.

Large items:

```text
100 MB logs
full PDFs
huge traces
secrets
binary artifacts
```

Better:

```text
state → reference / artifact ID
external store → full payload
```

State should contain what is needed for control and reasoning.

---

# PART 11 — Volatile Facts and Freshness

State:

```text
AKS status = Degraded at 10:00
```

At 10:20 it may be Healthy.

So evidence fields should track:

```text
observed_at
TTL/freshness policy
source
```

Graph routing can then decide:

```text
stale → refresh tool
fresh → reuse
```

---

# PART 12 — Authorization State

Never let model write:

```python
{"can_restart_production": True}
```

Authorization should be derived from trusted identity/policy systems.

Graph state can carry an application-issued decision:

```python
{"write_permission": False}
```

but model should not determine it.

---

# PART 13 — State Validation

Before node execution, validate required assumptions:

```text
incident_id present?
environment allowlisted?
evidence type correct?
iteration within limit?
approval status valid enum?
```

Typed schemas help structure, but business validation is still required.

---

# PART 14 — Common Mistakes

- one giant state dict with unclear meanings
- model outputs mixed into evidence list
- evidence list overwrite
- retry duplicates
- no timestamps
- permissions controlled by model
- huge raw payloads stored in graph state
- secrets copied into checkpoints

---

# PART 15 — Interview Q&A

### Q1. What is graph state?
The shared application data that represents the current execution snapshot and is read/updated by graph nodes.

### Q2. Why use reducers?
Reducers define how concurrent or repeated updates to a state field are merged instead of blindly overwritten.

### Q3. Should model-generated hypotheses be stored as evidence?
No. They should be stored in a separate model-output/hypothesis field unless independently verified.

### Q4. Is a typed schema enough for trust?
No. Type/schema validation checks structure; trust and semantic correctness require source and business validation.

---

# PART 16 — Revision

```text
Schema = what state contains
Reducer = how updates combine
Evidence = source-backed observation
Hypothesis = model reasoning
Authorization = trusted policy output
```

---

# PART 17 — Homework

Design `IncidentState` for the NSG incident with at least these categories:

```text
request
workflow control
evidence
reference knowledge
model hypotheses
approval
final output
```

For every field mark:

```text
who can write it?
can it be overwritten?
does it need timestamp?
```

---

# 🔁 Next Lesson Kyu?

State contract ready hai. Ab graph ko move karne ke liye **nodes, fixed edges aur conditional routing** design karenge.
