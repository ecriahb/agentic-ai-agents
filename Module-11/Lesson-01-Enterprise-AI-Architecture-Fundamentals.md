# 🚩 Jai Bajrangbali!

# Lesson 01 — Enterprise AI Architecture Fundamentals

> **A working agent is code. A production agent is a workload with identity, network, state, dependencies, policies, telemetry and recovery behavior.**

---

# 🎯 Lesson Goal

You will learn:

- prototype vs production workload
- functional and non-functional requirements
- control plane, data plane and capability plane
- trust boundaries
- synchronous vs long-running execution
- failure-domain thinking
- how Modules 1–10 map into infrastructure components

---

# PART 1 — English Definition

**Enterprise AI architecture is the structured design of compute, identity, networking, data, model, tool, security, observability and operational controls required to run AI applications reliably at organizational scale.**

---

# PART 2 — Why Local Success Is Not Production Readiness

Local demo:

```text
python app.py
 ↓
Ollama
 ↓
local files
 ↓
print RCA
```

Enterprise workload:

```text
User/API
 ↓
Authentication
 ↓
Rate Limit / WAF
 ↓
Agent Runtime
 ↓
Model + RAG + Tools/MCP
 ↓
State/Evidence/Audit
 ↓
Monitoring + Security Analytics
 ↓
Approval / Policy
```

The model call is only one component.

---

# PART 3 — Functional Requirements

Example DevOps AI Assistant functions:

```text
- accept incident request
- retrieve approved runbooks
- collect pipeline/Terraform/AKS evidence
- produce grounded RCA
- propose remediation
- request approval for write actions
- preserve evidence and audit trail
```

Architecture begins by making these explicit.

---

# PART 4 — Non-Functional Requirements

Production architecture must also answer:

```text
Availability
Latency
Throughput
Security
Data residency
Auditability
Recoverability
Cost
Scalability
Maintainability
Compliance
```

A system can be functionally correct but operationally unusable.

---

# PART 5 — Workload Decomposition

Do not deploy one giant service containing everything.

Logical components:

```text
API / UI Layer
Agent Runtime
Model Gateway
Knowledge/RAG Service
Tool/MCP Gateway
Policy/Authorization Service
State Store
Evidence/Audit Store
Async Queue
Observability Pipeline
```

Learning version may combine them, but architecture should know the boundaries.

---

# PART 6 — Control Plane vs Data Plane

**Control plane** examples:

```text
model configuration
prompt version
tool registry
policy configuration
evaluation thresholds
release metadata
```

**Data plane** examples:

```text
incident request
retrieved chunks
tool evidence
model response
workflow state
```

Why separate?

A compromised request should not be able to rewrite system policy or register arbitrary tools.

---

# PART 7 — Capability Plane

Agentic systems additionally have a capability plane:

```text
MCP servers
Azure/GitHub APIs
kubectl wrappers
Terraform inspection
log/metric query tools
```

Module 7 taught standardized capability discovery. Module 10 taught that discovery is not authorization.

Production rule:

```text
Capability Exists
      !=
Caller Is Authorized
      !=
Agent May Invoke It
      !=
Action Is Approved
```

---

# PART 8 — Trust Boundaries

Classify every input:

```text
USER_INPUT          → untrusted
RAG_DOCUMENT        → untrusted data
MCP_RESOURCE        → external data
TOOL_OUTPUT         → evidence with provenance
MODEL_OUTPUT        → untrusted proposal
POLICY_CONFIGURATION→ trusted control
AUTHORIZATION       → trusted decision
```

Then define which boundary validates each transition.

---

# PART 9 — Request Flow for Our DevOps Assistant

```text
1 User authenticates.
2 API validates request.
3 Runtime creates incident state.
4 Router selects read-only specialists.
5 Tools collect evidence.
6 RAG retrieves reference knowledge.
7 LLM synthesizes RCA.
8 Validator checks structure/citations.
9 Policy decides whether remediation may be proposed.
10 Human approval gates risky action.
11 Audit store records outcome.
```

Every number is an observable stage.

---

# PART 10 — Long-Running Workflows

Incident investigation may exceed normal HTTP request duration.

Unsafe design:

```text
client request waits 15 minutes
```

Better pattern:

```text
POST incident
 ↓
202 / job ID
 ↓
queue/workflow
 ↓
persistent state
 ↓
status/stream updates
```

Stateful agent architecture from Module 8 becomes an infrastructure concern here.

---

# PART 11 — Failure Domains

Dependencies fail independently:

```text
LLM unavailable
vector store slow
MCP server timeout
Azure API throttled
state DB unavailable
queue backlog
DNS failure
Key Vault unavailable
```

Design question is not “can failure happen?” but:

```text
What state is preserved?
What can retry safely?
What should fail closed?
What user status is returned?
```

---

# PART 12 — Modules 1–10 Mapped to Production Components

```text
M1 evidence/tools      → Tool Gateway + Evidence Store
M2 prompts/context     → Prompt Registry + Context Builder
M3 APIs                → API layer + dependency clients
M4/5 embeddings/RAG    → ingestion + vector/search layer
M6 orchestration       → runtime composition
M7 MCP                 → capability integration layer
M8 stateful agents     → persistent workflow runtime
M9 multi-agent         → supervisor/specialist topology
M10 security/evals     → policy + release gates + red-team suite
```

---

# PART 13 — Architecture Decision Record

For every major choice record:

```text
Decision
Context
Options
Chosen option
Trade-offs
Security impact
Operational impact
Exit/migration path
```

Example:

```text
Decision: AKS vs App Service for runtime
Reason: custom networking + multiple services + long-running workers
Trade-off: higher operational complexity
```

---

# PART 14 — Common Mistakes

- architecture diagram shows only LLM and vector DB
- no identity path
- no authorization owner
- model output connected directly to write tool
- no durable state for approval pause
- no async strategy
- no failure-state contract
- one service has broad prod credentials
- logs contain secrets/full prompts

---

# PART 15 — Production Checklist

```text
[ ] functional requirements defined
[ ] SLOs defined
[ ] data classification defined
[ ] trust boundaries documented
[ ] identity per component
[ ] capability scopes documented
[ ] sync/async flows documented
[ ] state persistence chosen
[ ] dependency failure policy defined
[ ] audit trail defined
[ ] release evaluation gate defined
```

---

# PART 16 — Interview Q&A

### Q1. Why is an AI prototype not a production architecture?
Because production adds identity, network, data governance, persistence, reliability, scaling, observability, policy and recovery requirements around the model logic.

### Q2. Why separate control plane and data plane?
To keep runtime requests/data from directly mutating trusted configuration and policy.

### Q3. What is the biggest agent-specific architecture addition?
A controlled capability plane and durable workflow state, because agents can invoke external systems and pause/resume across long-running processes.

### Q4. What should happen when evidence collection fails?
The failure must be preserved as an explicit state; the model should not convert missing evidence into a guessed fact.

---

# 🧠 Revision

```text
Prototype = code works
Production = workload survives reality

Architecture =
Compute + Identity + Network + Data + Capabilities
+ Policy + Observability + Recovery + Cost
```

---

# 📝 Homework

Draw the current DevOps AI Assistant as 8 boxes. For each box specify:

```text
identity
input trust level
output
state owned
failure mode
```

---

# 🔁 Next Lesson Kyu?

Architecture components are clear. Next we decide **where they live organizationally**: subscriptions, environments, landing zones and prod/non-prod boundaries.
