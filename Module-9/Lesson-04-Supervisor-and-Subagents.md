# 🚩 Jai Bajrangbali!

# Lesson 04 — Supervisor & Subagent Pattern

> **Supervisor ka kaam sab kuch khud solve karna nahi; right specialist ko right context ke saath invoke karna aur results ko control karna hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- supervisor pattern ka mental model
- subagents as tools/nodes
- centralized memory/context
- delegation contract
- parallel vs sequential subagents
- supervisor failure modes
- DevOps implementation pattern

---

# PART 1 — Architecture

```text
User / Incident
      ↓
Supervisor
  ├─ Pipeline Specialist
  ├─ Terraform Specialist
  ├─ AKS Specialist
  └─ Knowledge Specialist
      ↓
Supervisor / Synthesis
```

Subagent typically user se direct baat nahi karta; result supervisor ko return karta hai.

---

# PART 2 — Why Supervisor?

Useful when:
- task spans multiple domains
- repeated delegation needed
- one coordinator should own overall workflow
- subagents are focused and stateless/per-invocation
- centralized conversation state desired

Not useful when:

```text
one deterministic route is enough
```

then router is simpler.

---

# PART 3 — Delegation Contract

Supervisor should not send vague:

```text
"Investigate everything"
```

Better:

```python
{
  "task": "Identify Terraform networking changes around failure window",
  "environment": "production",
  "incident_id": "INC-1042",
  "known_facts": ["Pipeline failed during Terraform Apply [E1]"]
}
```

Focused task produces focused result.

---

# PART 4 — Subagent as Tool Mental Model

```text
Supervisor decision
     ↓
call_terraform_specialist(task)
     ↓
subagent graph/agent
     ↓
normalized result
     ↓
Supervisor state
```

This is similar to Module 1 tool calling, but now the capability itself contains reasoning/workflow.

Still:

```text
subagent invocation request = untrusted proposal
host policy decides what runs
```

---

# PART 5 — Stateless Subagents

For many cases:

```text
Invocation 1 starts fresh
Invocation 2 starts fresh
```

Benefits:
- context isolation
- lower accidental memory contamination
- easier tests
- predictable scope

Supervisor keeps durable incident state.

If a specialist truly needs multi-turn state, use explicit subgraph persistence, not accidental chat history.

---

# PART 6 — Sequential Delegation

```text
Supervisor
 ↓
Pipeline Agent → says failure during terraform_apply
 ↓
Supervisor
 ↓
Terraform Agent → finds NSG deletion
 ↓
Supervisor
 ↓
AKS Agent → validates degraded connectivity
```

This is evidence-driven multi-hop coordination.

---

# PART 7 — Parallel Delegation

If domains independent:

```text
Pipeline Agent ─┐
Terraform Agent ├─→ Supervisor
AKS Agent ──────┘
```

Parallel benefits:
- lower wall-clock latency

But requires:
- deterministic result merge
- stable evidence IDs
- independent tool scopes
- error handling per branch

---

# PART 8 — Supervisor State

Example:

```python
{
  "incident_id": "INC-1042",
  "completed_agents": ["pipeline", "terraform"],
  "findings": [...],
  "evidence_ids": ["E1", "E2"],
  "next_agent": "aks",
  "iteration": 3
}
```

Do not store hidden chain-of-thought.

Store decisions/results needed for workflow.

---

# PART 9 — Supervisor Safety

Supervisor should NOT decide:
- user authorization
- whether prod write access is allowed
- whether evidence source is authentic purely by reasoning

Application policy should enforce:

```text
allowed_subagents
allowed_tools_per_subagent
max_delegations
max_parallel_calls
approval gates
```

---

# PART 10 — Failure Modes

## Infinite delegation

```text
Supervisor → A → Supervisor → A → ...
```

Guard:

```text
max_iterations + duplicate task detection
```

## Delegation ambiguity

Two specialists both investigate same domain.

Guard:

```text
responsibility map
```

## Result trust

Subagent says:

```text
"Root cause definitely NSG"
```

Supervisor must inspect evidence IDs, not trust confidence language.

---

# PART 11 — Practical Pseudocode

```python
def supervisor(state):
    if "E1" not in state["evidence_ids"]:
        return {"next_agent": "pipeline"}
    if "E2" not in state["evidence_ids"]:
        return {"next_agent": "terraform"}
    if "E3" not in state["evidence_ids"]:
        return {"next_agent": "aks"}
    return {"next_agent": "synthesize"}
```

Deterministic supervisor is a great learning baseline before LLM-driven delegation.

---

# PART 12 — Interview Q&A

### Q1. What does a supervisor do?
Coordinates specialist agents, controls delegation/context, tracks state, and integrates results.

### Q2. Why keep subagents stateless by default?
To isolate context and reduce memory contamination when each invocation is independent.

### Q3. Supervisor vs router?
Supervisor can coordinate repeatedly across steps; router usually dispatches once.

### Q4. How do you prevent supervisor loops?
Iteration limits, duplicate-task detection, progress metrics and explicit termination states.

---

# PART 13 — Revision

```text
Supervisor = coordinator
Subagent = focused specialist
Delegation = explicit task contract
Result = structured finding
Policy = outside model reasoning
```

---

# PART 14 — Homework

Design a supervisor decision table for E1/E2/E3 evidence collection. Add conditions for:
- tool timeout
- specialist failure
- duplicate finding
- enough evidence

---

# 🔁 Next Lesson Kyu?

Supervisor handles multi-hop coordination. Next hum **Router + Parallel Agents** dekhenge jahan independent investigations simultaneously execute ho sakte hain.
