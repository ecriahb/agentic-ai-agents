# 🚩 Jai Bajrangbali!

# Lesson 10 — RAG, MCP, Tools & Human Approval per Agent

> **Multi-agent system me capability access scoped hona chahiye. Har agent ko same RAG corpus, same MCP servers, same tools aur same write authority dena unsafe hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- capability scoping per agent
- RAG access boundaries
- MCP server/tool allowlists
- read vs propose vs execute authority
- human approval
- least privilege
- capability discovery vs authorization

---

# PART 1 — Capability Map

```text
Pipeline Agent
→ pipeline read tools

Terraform Agent
→ Terraform read tools + IaC runbooks

AKS Agent
→ AKS read tools + Kubernetes runbooks

Knowledge Agent
→ vector retrieval / MCP resources

Remediation Planner
→ may propose action

Executor
→ write action only after policy + approval
```

---

# PART 2 — RAG per Agent

Do not expose one giant index blindly.

Terraform specialist may retrieve:

```text
Terraform modules
networking standards
previous IaC incidents
```

AKS specialist may retrieve:

```text
AKS runbooks
network policy docs
cluster troubleshooting guides
```

Benefits:
- higher relevance
- lower context noise
- better ACL control

---

# PART 3 — RAG Still Reference Knowledge

```text
RAG result [R1]
```

can explain expected behavior.

It cannot prove:

```text
current incident definitely followed that pattern
```

Current fact requires current evidence [E*].

---

# PART 4 — MCP Capability Layer

Module 7 MCP can expose:

```text
Pipeline MCP Server
Terraform MCP Server
AKS MCP Server
Knowledge MCP Server
```

Agent gets only approved client/capabilities.

Discovery:

```text
server says tool exists
```

does NOT mean:

```text
current user/agent may execute it
```

---

# PART 5 — Host Allowlist

```python
AGENT_TOOL_POLICY = {
    "pipeline": {"get_pipeline_status", "get_pipeline_logs"},
    "terraform": {"get_terraform_changes"},
    "aks": {"get_aks_status", "get_aks_events"},
}
```

Validate:

```text
agent identity
tool name
arguments
environment
resource scope
user authorization
```

---

# PART 6 — Authority Classes

```text
READ
→ inspect status/evidence

PROPOSE
→ create remediation recommendation

EXECUTE
→ perform change
```

Keep these distinct.

Most course specialists remain READ_ONLY.

---

# PART 7 — Human Approval Gate

Suppose synthesis recommends:

```text
restore NSG rule aks-subnet-allow
```

Flow:

```text
Proposal
 ↓
Policy validation
 ↓
Human approval interrupt
 ├─ reject → stop
 └─ approve → executor path
```

Approval should include exact action, target, evidence and risk.

---

# PART 8 — Approval is Not Authorization

User may approve an action they are not authorized to execute.

Therefore:

```text
Authorization = identity/policy system
Approval = human intent confirmation
```

Both can be required.

---

# PART 9 — Tool Output as Evidence

Specialist tool result should become evidence envelope:

```python
{
  "id": "E3",
  "agent": "aks",
  "tool": "get_aks_status",
  "arguments": {"cluster": "prod-aks"},
  "payload": {...},
  "timestamp": "..."
}
```

The model should not be the only place this result exists.

---

# PART 10 — Cross-Agent Capability Escalation

Terraform agent may need AKS evidence.

Wrong:

```text
Terraform agent directly gets all AKS tools.
```

Better:

```text
request AKS specialist
or supervisor routes task
```

This preserves domain and permission boundaries.

---

# PART 11 — Common Mistakes

- every agent gets every tool
- discovery treated as permission
- RAG docs treated as current facts
- write tool hidden in ordinary specialist toolset
- approval without exact action details
- tool output only stored in message history
- agent asks another agent to bypass policy

---

# PART 12 — Interview Q&A

### Q1. How should tools be scoped in multi-agent systems?
Per agent role, user authorization, environment and task using least privilege.

### Q2. Is MCP discovery authorization?
No. Discovery advertises capabilities; host/server policy still decides whether invocation is allowed.

### Q3. Why separate proposal from execution?
It allows analysis/planning without granting write authority and supports policy/human approval before changes.

### Q4. Why separate RAG from evidence?
RAG provides reference knowledge; current incident claims require current observations.

---

# PART 13 — Revision

```text
Least privilege per agent
RAG = reference
MCP discovery != permission
Read != propose != execute
Approval != authorization
Tool result → evidence store
```

---

# PART 14 — Homework

Create a permission matrix for:
- Pipeline Agent
- Terraform Agent
- AKS Agent
- Knowledge Agent
- Remediation Planner
- Executor

Mark READ / PROPOSE / EXECUTE and approval requirements.

---

# 🔁 Next Lesson Kyu?

Architecture safe lag rahi hai, but production me hume prove karna padega ki team actually reliable hai. Next = **observability, safety and evaluation**.
