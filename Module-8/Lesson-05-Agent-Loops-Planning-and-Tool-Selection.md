# 🚩 Jai Bajrangbali!

# Lesson 05 — Agent Loops, Planning & Tool Selection

> **Agent ka core loop simple lagta hai: observe → decide → act → observe. Production safety isi loop ko bounded banane me hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- agent loop kya hota hai
- observation, plan, action and result ka separation
- model tool selection ka role
- tool request ko untrusted proposal kyu treat karna hai
- loop state kaise preserve hota hai
- deterministic controls model planning ko kaise bound karte hain

---

# PART 1 — English Definition

An **agent loop** is a repeated control cycle in which a system observes its current state, selects or proposes a next action, executes an allowed action, incorporates the result, and decides whether to continue or terminate.

---

# PART 2 — Core Loop

```text
Goal
 ↓
Observe State
 ↓
Decide Next Step
 ↓
Validate Proposal
 ↓
Execute Allowed Tool
 ↓
Preserve Evidence
 ↓
Update State
 ↓
Enough Evidence?
 ├─ No → loop
 └─ Yes → analyze/finish
```

---

# PART 3 — Reuse Module 1 Principle

Module 1 ka core rule:

```text
LLM tool request = untrusted input
```

Module 8 me bhi same:

```text
Planner proposes:
get_terraform_changes(environment="production")

Host validates:
- tool allowlisted?
- args schema valid?
- environment allowed?
- caller authorized?
- read-only or approval needed?
```

Only then execute.

---

# PART 4 — Planning Does Not Mean Full Autonomy

Planning options:

### Deterministic plan

```text
If Terraform failed → inspect Terraform evidence
```

### Model-assisted plan

```text
Given evidence E1 and available read-only tools,
which single evidence gap should be investigated next?
```

### Hybrid plan

```text
Model proposes category/tool
Host policy validates and limits execution
```

Hybrid is usually better for production learning.

---

# PART 5 — Plan Contract

Do not ask model for prose:

```text
"I think we should maybe check networking..."
```

Use structured proposal:

```json
{
  "action": "call_tool",
  "tool": "get_aks_status",
  "arguments": {"cluster_name": "prod-aks"},
  "reason": "Need current connectivity status"
}
```

Or:

```json
{
  "action": "finish",
  "reason": "Required current evidence is available"
}
```

---

# PART 6 — Planner vs Executor Separation

```text
Planner
= proposes what might be useful

Executor
= enforces what is allowed
```

Never combine model reasoning and privileged execution into one opaque step.

Architecture:

```text
Planner Node
    ↓
Policy Node
 ├─ reject → Safe Stop / Replan
 └─ allow
      ↓
Executor Node
      ↓
Evidence Normalizer
```

---

# PART 7 — Tool Selection Quality

Available tools:

```text
get_pipeline_status
get_terraform_changes
get_aks_status
get_k8s_events
get_recent_deployments
```

Incident:

```text
Terraform Apply failed before deployment reached AKS rollout
```

Good plan:

```text
inspect Terraform/pipeline evidence first
```

Poor plan:

```text
call all tools blindly
```

Agentic behavior should improve relevance, not create random API fan-out.

---

# PART 8 — Evidence Gap Thinking

State can maintain:

```python
{
  "known_facts": [...],
  "evidence_gaps": [
      "current AKS connectivity status",
      "exact Terraform network change"
  ]
}
```

Planner task:

```text
Choose one allowed action that closes the highest-priority gap.
```

This is better than vague "solve incident" planning.

---

# PART 9 — Duplicate Tool Calls

Agent may repeatedly request same call.

Track:

```text
(tool_name, normalized_args, evidence_freshness)
```

Policy:

```text
same tool + same args + fresh successful result
→ do not call again
```

Unless explicit refresh reason exists.

---

# PART 10 — Side Effects

Read-only tools:

```text
get status
read logs
read plan
```

Write tools:

```text
restart deployment
apply Terraform
modify NSG
rollback release
```

Planning node may suggest write action, but execution path should route to **human approval**, not direct tool execution.

---

# PART 11 — Stopping Criteria

Agent should stop when:

```text
goal satisfied
minimum evidence policy satisfied
no useful allowed action remains
max iterations reached
human rejected action
fatal/non-retryable error
```

Stop is a first-class action.

---

# PART 12 — DevOps Example

```text
Iteration 1
E1: Pipeline failed during Terraform Apply
Planner → get_terraform_changes

Iteration 2
E2: NSG rule removed
Planner → get_aks_status

Iteration 3
E3: connectivity degraded
Evidence Gate → enough
Planner → finish collection

Analyze → RCA
```

Notice:

```text
model did not execute remediation
```

---

# PART 13 — Common Mistakes

- model plan as authorization
- call every tool in parallel without need
- no duplicate detection
- no evidence-gap state
- no max loop count
- planner and executor same opaque node
- write tools in same auto-approved path as reads

---

# PART 14 — Interview Q&A

### Q1. What is an agent loop?
A repeated observe-decide-act-observe cycle that continues until a goal or termination condition is reached.

### Q2. Why separate planner and executor?
To keep model reasoning separate from policy, authorization and side-effect execution.

### Q3. What should happen to repeated tool calls?
The host should detect duplicates and reuse fresh evidence where appropriate.

### Q4. Should an agent decide its own loop limit?
No. Loop limits should be application-controlled policy.

---

# PART 15 — Revision

```text
Observe = inspect state
Plan = propose next step
Policy = decide allowed/not allowed
Execute = perform approved operation
Evidence = preserve result
Stop = explicit terminal decision
```

---

# PART 16 — Homework

Design a structured planner output with actions:

```text
CALL_TOOL
RETRIEVE_KNOWLEDGE
ASK_HUMAN
FINISH
```

Define validation rules for each.

---

# 🔁 Next Lesson Kyu?

Ab loop tool choose kar sakta hai. Next hume Modules 4–7 ko graph me connect karna hai: **RAG retrieval, MCP tools/resources and local tool nodes** ko correct trust boundaries ke saath route karenge.
