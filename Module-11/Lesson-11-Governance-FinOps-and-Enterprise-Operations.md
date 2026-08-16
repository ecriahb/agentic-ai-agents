# 🚩 Jai Bajrangbali!

# Lesson 11 — Governance, FinOps & Enterprise Operations

> **A production agent needs an owner, a budget, approved data/model/tool boundaries, lifecycle rules and an operational support model.**

---

# 🎯 Lesson Goal

You will learn:

- AI workload ownership
- governance roles
- model/tool/data registries
- cost attribution and budgets
- token/context/tool cost optimization
- lifecycle and decommissioning
- change management
- support/on-call model
- compliance/audit evidence
- production readiness reviews

---

# PART 1 — Governance Is Not Only Security

Governance asks:

```text
Who owns this agent?
Who owns the data?
Which models are approved?
Which tools are approved?
Who pays?
Who supports incidents?
Who can change prompts/policies?
When is the system retired?
```

---

# PART 2 — Responsibility Model

Example:

```text
Platform Team
- landing zone
- gateway
- AKS/shared runtime
- observability platform

AI Application Team
- graph/agents
- prompts
- tool selection
- eval suite

Security
- policy baseline
- threat model
- red-team requirements

Data Owners
- RAG source approval/ACL

Operations/SRE
- SLOs
- incidents
- capacity
```

---

# PART 3 — Registries

Maintain inventory of:

```text
models
prompts
agents
tools/MCP servers
knowledge sources
policies
eval datasets
```

Each entry should have:

```text
owner
version
risk class
environment
approval status
last reviewed
```

---

# PART 4 — Cost Model

Agent cost can include:

```text
model input tokens
model output tokens
embedding generation
vector/search queries
compute workers
state DB
storage
egress
MCP/API calls
observability retention
```

Do not optimize only model token price.

---

# PART 5 — Cost Attribution

Tag/record:

```text
team
application
environment
agent/workflow
model
incident/request
```

Then answer:

```text
Which team generated cost?
Which agent version is expensive?
Which workflow loops excessively?
```

---

# PART 6 — Token Optimization

Potential improvements:

```text
retrieve fewer high-quality chunks
summarize safe history
avoid passing duplicate evidence
use specialist context isolation
cache stable reference knowledge carefully
use smaller model for simple routing
```

Never reduce evidence until claims become unsupported.

---

# PART 7 — Model Tiering

Example:

```text
Router → small/cheap deterministic-ish model or rules
Specialist analysis → medium model
Final complex synthesis → stronger model
```

But every chosen model must pass task-specific evaluation.

---

# PART 8 — Cost Guardrails

```text
max tokens/request
max model calls/workflow
max iterations
max retrieved context
per-team budget
rate limit
monthly alerts
```

These also protect against unbounded-consumption attacks.

---

# PART 9 — Data Governance

For each knowledge/evidence source:

```text
classification
owner
allowed consumers
retention
region/residency
PII/secrets handling
source-of-truth status
```

A convenient document is not automatically approved RAG data.

---

# PART 10 — Change Governance

Changes requiring stronger review:

```text
new write tool
new MCP server
new production data source
RBAC expansion
model provider change
prompt that changes action policy
new cross-team shared state
```

---

# PART 11 — Operational Ownership

Define:

```text
service owner
on-call rotation
runbooks
severity model
vendor escalation
model/provider outage playbook
security incident process
```

“AI team” is not an operational plan.

---

# PART 12 — Production Readiness Review

Review categories:

```text
Architecture
Security
Identity/RBAC
Networking
Data
Reliability
Scale
Observability
CI/CD
DR
Cost
Support
Evaluation
```

Document known risks and compensating controls.

---

# PART 13 — Decommissioning

When agent retired:

```text
disable endpoints
remove identities/RBAC
remove tool registrations
archive required audit/evidence
remove stale vector indexes
delete secrets
stop budgets/resources
update inventory
```

Forgotten agents can become unmanaged privileged entry points.

---

# PART 14 — FinOps Example

Metric shows:

```text
30% requests consume 70% tokens
```

Trace reveals:

```text
same 12 runbook chunks attached every turn
```

Fix retrieval/context—not model quality.

---

# PART 15 — Common Mistakes

- no named owner
- no per-team cost attribution
- unlimited context/iterations
- shared RAG sources without data owner
- production MCP server not inventoried
- old agents retain RBAC after retirement
- cost optimization removes grounding evidence

---

# PART 16 — Interview Q&A

### Q1. What is AI FinOps?
Applying cost visibility, allocation, optimization and governance to model, compute, storage, search and agent workflow consumption.

### Q2. Why inventory MCP servers/tools?
They are capabilities that can access external systems and must have ownership, risk classification and lifecycle control.

### Q3. What is a production readiness review?
A structured review that verifies architecture, security, reliability, operations, cost and evaluation requirements before release.

---

# 🧠 Revision

```text
Enterprise AI = Technical system + Operating model + Governance + Cost ownership
```

---

# 📝 Homework

Build a one-page production readiness checklist with named owners for every control area.

---

# 🔁 Next Lesson Kyu?

All production disciplines are covered. Next we combine them into one **Production DevOps AI Platform blueprint**.
