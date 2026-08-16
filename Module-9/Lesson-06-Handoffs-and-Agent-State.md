# 🚩 Jai Bajrangbali!

# Lesson 06 — Handoffs & Active-Agent State

> **Handoff ka matlab sirf function call nahi; control ownership aur active-agent state ka intentional transition hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- handoff pattern kya hai
- `active_agent` state
- handoff tool/command mental model
- context transfer
- conversation validity
- ping-pong prevention
- DevOps staged specialist interaction

---

# PART 1 — Handoff Mental Model

```text
General Triage Agent
       ↓ transfer
Terraform Specialist
       ↓ transfer
AKS Specialist
       ↓
User / Supervisor
```

Unlike subagents-as-tools, receiving specialist may become the active interaction owner.

---

# PART 2 — State-Driven Behavior

A handoff system commonly tracks:

```python
{
  "active_agent": "terraform_specialist",
  "handoff_count": 1,
  "handoff_reason": "network change detected"
}
```

Router reads state and invokes active specialist.

---

# PART 3 — Handoff vs Delegation

Delegation:

```text
Supervisor remains in control
→ calls specialist
→ specialist returns result
```

Handoff:

```text
Control moves to specialist state/agent
→ specialist may interact directly
→ later transfer elsewhere
```

Choose based on ownership model.

---

# PART 4 — Handoff Contract

A safe handoff should contain:

```text
from_agent
to_agent
reason
incident_id
verified context references
allowed next capabilities
```

Example:

```python
{
  "from": "triage",
  "to": "terraform",
  "reason": "pipeline evidence shows failure during terraform_apply [E1]",
  "evidence_ids": ["E1"]
}
```

---

# PART 5 — Context Transfer

Do not transfer entire internal history automatically.

Better:

```text
Incident summary
Verified facts
Evidence IDs
Open question
Current policy/permissions
```

This is Module 2 context engineering applied between agents.

---

# PART 6 — Message Integrity

In message-based agent systems, tool calls and tool responses must remain structurally valid.

Handoff should not create malformed history such as:

```text
AI tool call
→ no corresponding tool response
→ next agent sees broken sequence
```

Practical frameworks may require an explicit tool-result/acknowledgement message for the handoff.

---

# PART 7 — DevOps Example

User:

```text
Deployment failed. Can you investigate?
```

Triage agent finds:

```text
[E1] failure stage = terraform_apply
```

Handoff:

```text
active_agent = terraform_specialist
```

Terraform specialist finds:

```text
[E2] NSG rule removed
```

Then handoff to AKS specialist with only:

```text
[E1], [E2], cluster=prod-aks, question=validate connectivity impact
```

---

# PART 8 — Handoff Loops

Danger:

```text
Terraform → AKS → Terraform → AKS → ...
```

Guardrails:

```text
max_handoffs
same-pair repetition count
handoff reason hash
evidence progress requirement
```

If no new evidence:

```text
STOP_NO_PROGRESS
```

---

# PART 9 — Capability Changes

Active agent may have different tools:

```text
Triage: broad read-only metadata
Terraform: Terraform read tools
AKS: cluster read tools
```

Handoff should not silently increase permissions.

Authorization still comes from host/policy layer.

---

# PART 10 — User Experience

Handoffs are useful when user should know specialist context changed:

```text
"I’m transferring this investigation to the AKS specialist because current evidence points to cluster connectivity."
```

For invisible backend specialization, supervisor/subagents may be cleaner.

---

# PART 11 — Common Mistakes

- handoff for every tool call
- full context dump to next agent
- no active-agent state
- no handoff limit
- permission escalation on transfer
- user assumption passed as verified fact
- previous agent conclusion treated as evidence

---

# PART 12 — Interview Q&A

### Q1. What is a handoff?
A state transition that transfers active responsibility/behavior to another agent or specialist configuration.

### Q2. Handoff vs subagent call?
In a subagent call, coordinator remains in control; in a handoff, active control moves to another state/agent.

### Q3. What context should be transferred?
Minimal task-relevant verified context, evidence references, open questions and policy—not full internal histories by default.

### Q4. How prevent handoff loops?
Max handoffs, duplicate-pair detection, progress requirements and explicit terminal states.

---

# PART 13 — Revision

```text
Handoff = transfer ownership
State tracks active agent
Context must be filtered
Permissions do not auto-expand
Loops require bounded policy
```

---

# PART 14 — Homework

Design handoff flow:

```text
Triage → Terraform → AKS → Synthesis
```

For each transition define:
- trigger
- transferred evidence
- private data not transferred
- max allowed handoffs

---

# 🔁 Next Lesson Kyu?

Ab multiple agents coordinate kar rahe hain. Sabse critical question: **shared state me kya jaye aur private state me kya rahe?**
