# 🚩 Jai Bajrangbali!

# Lesson 10 — Subgraphs & Multi-Agent Patterns

> **Multiple agents banana goal nahi hai. Goal hai complex responsibility ko bounded, testable components me divide karna.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- subgraph kya hota hai
- specialist workflow kya hota hai
- supervisor pattern ka mental model
- handoff kaise controlled hota hai
- multi-agent architecture kab useful hai
- multi-agent chaos ke common risks
- Module 9 ke liye foundation

---

# PART 1 — English Definitions

A **subgraph** is a graph or workflow component embedded inside a larger graph to encapsulate a bounded responsibility.

A **multi-agent system** coordinates multiple specialized agent/workflow components that may have different goals, tools, prompts or state scopes.

---

# PART 2 — Why Subgraphs First?

Before saying:

```text
network agent
terraform agent
pipeline agent
security agent
```

ask:

```text
Can these simply be bounded subgraphs/functions?
```

Often yes.

Subgraph advantages:

```text
clear input/output contract
isolated tests
bounded tools
separate retry policy
reusable workflow
less agent-to-agent ambiguity
```

---

# PART 3 — DevOps Subgraph Design

```text
Main Incident Graph
      ↓
Classify Domain
 ┌────┼──────────────┐
 ↓    ↓              ↓
Pipeline Subgraph  Terraform Subgraph  AKS Subgraph
 ↓    ↓              ↓
Normalized Evidence Results
          ↓
      Main Graph
```

Each subgraph returns evidence, not free-form authority.

---

# PART 4 — Specialist Contract

Example input:

```python
{
  "incident_id": "INC-1042",
  "environment": "production",
  "question": "Inspect Terraform networking changes"
}
```

Output:

```python
{
  "status": "SUCCESS",
  "evidence": [E2, E3],
  "gaps": [],
  "summary": "..."
}
```

Main graph should not depend on opaque internal conversation history.

---

# PART 5 — Supervisor Pattern

```text
Supervisor
  ↓
Inspect State / Goal
  ↓
Choose Specialist
  ├─ Pipeline
  ├─ Terraform
  └─ AKS
  ↓
Collect Specialist Result
  ↓
Decide Next Specialist or Finish
```

Supervisor can be deterministic, model-assisted or hybrid.

---

# PART 6 — Bounded Toolsets

Pipeline specialist:

```text
get_pipeline_status
read_pipeline_log
```

Terraform specialist:

```text
get_terraform_changes
read_plan_summary
```

AKS specialist:

```text
get_aks_status
get_k8s_events
```

Least privilege improves reasoning and security.

---

# PART 7 — MCP Connection

Each specialist can consume different MCP servers:

```text
Pipeline Subgraph → CI/CD MCP
Terraform Subgraph → IaC MCP
AKS Subgraph → Kubernetes/Azure MCP
```

Main graph does not need every server-specific implementation detail.

Still:

```text
MCP discovery != authorization
specialist proposal != execution authority
```

---

# PART 8 — Handoff Risks

Bad handoff:

```text
Agent A: "Network is definitely root cause"
Agent B accepts as fact
```

Better handoff:

```text
Agent/Subgraph A returns evidence IDs + status + hypothesis separately
```

Example:

```python
{
  "evidence_ids": ["E2", "E3"],
  "hypothesis": "network change may be causal",
  "confidence": "medium"
}
```

Downstream validates evidence itself.

---

# PART 9 — Shared State vs Private State

Some state should be shared:

```text
incident_id
environment
approved evidence IDs
global loop budget
```

Specialist-private state:

```text
local retry counters
local intermediate plan
specialist-specific messages
```

Avoid giant global state where every agent can overwrite everything.

---

# PART 10 — Multi-Agent Failure Modes

```text
agents call each other forever
same evidence collected repeatedly
contradictory summaries
context explosion
permissions broadened unnecessarily
cost/latency multiplication
unclear final authority
```

Therefore:

```text
bounded specialists
explicit supervisor
shared termination policy
normalized outputs
source-backed evidence
```

---

# PART 11 — When Multi-Agent Is Justified

Useful when responsibilities differ materially:

```text
different tool domains
different security boundaries
different long-running workflows
different specialist prompts/evaluation datasets
parallel independent investigations
```

Not useful just because architecture diagram looks advanced.

---

# PART 12 — Parallel Specialist Pattern

```text
                  ┌→ Pipeline Investigation ─┐
Incident → Fanout ├→ Terraform Investigation ┼→ Evidence Merger
                  └→ AKS Investigation ───────┘
```

Need:

```text
bounded concurrency
partial failure handling
evidence deduplication
consistent source IDs
```

---

# PART 13 — Final Decision Authority

Never let each specialist independently execute remediation.

Safer:

```text
specialists investigate
 ↓
main graph validates evidence
 ↓
main policy proposes action
 ↓
human approval
 ↓
central controlled executor
```

---

# PART 14 — Common Mistakes

- one agent per tool
- free-form agent-to-agent messages as truth
- no supervisor loop limit
- broad tool permissions to every specialist
- no normalized handoff schema
- duplicated evidence
- no final owner for decision

---

# PART 15 — Interview Q&A

### Q1. Subgraph vs multi-agent?
A subgraph is a compositional workflow boundary; multi-agent architecture adds multiple specialized decision-making components. A subgraph can be deterministic and does not need to be an autonomous agent.

### Q2. Why use bounded specialist toolsets?
They reduce security exposure and improve decision relevance.

### Q3. How should agents hand off information?
Prefer structured state/evidence contracts with source IDs, not unverified prose treated as truth.

### Q4. What is supervisor pattern?
A coordinator decides which specialist runs next and when the overall task is complete.

---

# PART 16 — Revision

```text
Subgraph = bounded reusable workflow
Specialist = domain-limited component
Supervisor = coordinator
Handoff = validated structured contract
Shared evidence = source-backed truth layer
```

---

# PART 17 — Homework

Design three specialists for:

```text
CI/CD
Terraform
AKS
```

For each list:

```text
allowed tools
private state
shared state
output contract
termination condition
```

---

# 🔁 Next Lesson Kyu?

Complex graph bana sakte hain, but production me usko **observe, test, evaluate and secure** bhi karna hoga. Next lesson production readiness par hai.
