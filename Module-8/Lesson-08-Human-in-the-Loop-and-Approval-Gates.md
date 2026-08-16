# 🚩 Jai Bajrangbali!

# Lesson 08 — Human-in-the-Loop & Approval Gates

> **Human approval ek prompt instruction nahi; it is a controlled execution pause backed by persisted state and explicit resume input.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- HITL kya hai
- approval gate kab required hai
- LangGraph interrupt mental model
- pause/resume ka state connection
- approve / reject / edit decisions
- write action ko read-only investigation se kaise separate karein
- approval ko authorization se confuse kyu nahi karna

---

# PART 1 — English Definition

**Human-in-the-loop (HITL)** is a workflow pattern in which execution pauses at a controlled point so a human can inspect context and explicitly approve, reject or modify a pending decision before execution continues.

---

# PART 2 — Why Prompt-Based Approval Is Weak

Unsafe:

```text
System prompt:
"Before production changes, ask user for approval."
```

Model may:

```text
forget
misinterpret
continue in same generation
```

Safer:

```text
Graph reaches approval node
 ↓
Runtime pauses
 ↓
State checkpointed
 ↓
External human decision received
 ↓
Graph resumes
```

---

# PART 3 — Interrupt Mental Model

Conceptual code:

```python
from langgraph.types import interrupt


def approval_node(state):
    decision = interrupt({
        "action": state["proposed_action"],
        "reason": state["action_reason"],
    })
    return {"approval_decision": decision}
```

Interrupt payload should be JSON-serializable and safe to display.

---

# PART 4 — Checkpoint Required

Pause may last:

```text
30 seconds
10 minutes
2 hours
```

Process may restart meanwhile.

Therefore:

```text
interrupt + persistent checkpoint
```

are naturally connected.

In-memory persistence is fine for learning, but production approval needs durable storage.

---

# PART 5 — Approval Is Not Authorization

Authorization asks:

```text
Is this user allowed to approve production rollback?
```

Approval asks:

```text
Does this authorized user approve this exact rollback proposal now?
```

Correct flow:

```text
Identity
 ↓
Authorization Policy
 ↓
Approval Request
 ↓
Human Decision
 ↓
Execution
```

Do not use model to decide authorization.

---

# PART 6 — Approval Payload

Human should see enough evidence:

```json
{
  "incident_id": "INC-1042",
  "action": "rollback_release",
  "target": "production/api:v42",
  "reason": "Current evidence links failure to v42 rollout",
  "evidence_ids": ["E1", "E4"],
  "risk": "medium",
  "rollback_plan": "restore v41"
}
```

Not:

```text
"Approve? yes/no"
```

Context matters.

---

# PART 7 — Decision Types

Useful decisions:

```text
APPROVE
REJECT
EDIT
REQUEST_MORE_EVIDENCE
```

Routing:

```text
approval
 ├─ approve → controlled executor
 ├─ reject → final rejected state
 ├─ edit → validate edited proposal
 └─ more evidence → investigation loop
```

---

# PART 8 — Edit Must Be Revalidated

Human changes:

```text
rollback namespace=prod-a
```

to:

```text
rollback namespace=prod-b
```

Do not assume edited command is safe because human typed it.

Re-run:

```text
schema validation
allowlist
RBAC
policy
```

before execution.

---

# PART 9 — Side Effects Before Interrupt

Critical replay rule:

```text
If node restarts after resume,
code executed before interrupt may run again.
```

Avoid:

```python
perform_change()
decision = interrupt("Was that okay?")
```

Correct order:

```text
prepare proposal
interrupt for approval
then execute in separate node
```

---

# PART 10 — Read vs Write Policy

Example:

```text
get_pipeline_status          → no approval
get_terraform_changes        → no approval
get_aks_status               → no approval
restart_deployment           → approval required
terraform_apply              → approval required
modify_nsg                   → approval required
```

This policy should be application-controlled.

---

# PART 11 — DevOps Graph

```text
investigate
 ↓
generate RCA
 ↓
propose remediation
 ↓
validate proposal
 ↓
approval_gate  ⏸
 ├─ reject → final report
 └─ approve
      ↓
controlled_action
      ↓
verify_action
      ↓
final status
```

---

# PART 12 — Approval Audit Record

Persist:

```text
request_id
incident_id
proposed action
arguments
evidence IDs
request timestamp
approver identity
decision
decision timestamp
edited fields
execution result
```

This is important for enterprise auditability.

---

# PART 13 — Common Mistakes

- approval only in prompt text
- approval without persistent state
- any user allowed to approve
- human edit skips validation
- side effect before interrupt
- generic approval without exact action/target
- approval reused for a different action

---

# PART 14 — Interview Q&A

### Q1. Why is HITL more than asking the model to request confirmation?
Because safe HITL requires actual execution suspension, persisted state and explicit external resume input.

### Q2. Approval vs authorization?
Authorization determines who may approve/execute; approval is a decision for a specific proposed action.

### Q3. Why use a separate execution node after approval?
To avoid side effects being replayed around interrupt/resume semantics and to keep policy boundaries clear.

### Q4. What should happen after a human edits an action?
The edited action should be fully revalidated and re-authorized.

---

# PART 15 — Revision

```text
Interrupt = pause
Checkpoint = remember where
Authorization = who may decide
Approval = decision on exact action
Executor = acts only after policy permits
```

---

# PART 16 — Homework

Design an approval payload for restoring the removed NSG rule `aks-subnet-allow`.

Include:

```text
target
diff/effect
evidence IDs
risk
rollback plan
approver role
```

---

# 🔁 Next Lesson Kyu?

HITL pause/resume kar sakta hai only if progress reliably saved ho. Next lesson me **checkpointing, persistence, threads, recovery and time-travel concepts** cover karenge.
