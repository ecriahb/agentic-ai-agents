# 🚩 Jai Bajrangbali!

# Lesson 08 — High Availability & Disaster Recovery

> **HA keeps the service operating through common failures; DR restores acceptable service after a larger failure. Stateful agents need both compute recovery and workflow-state recovery.**

---

# 🎯 Lesson Goal

You will learn:

- availability zones vs regions
- HA vs DR
- RTO and RPO
- active/active vs active/passive
- dependency failover
- state/checkpoint recovery
- vector/search recovery
- model/provider dependency planning
- regional failure runbooks
- failure testing

---

# PART 1 — English Definitions

**High Availability (HA)** designs the system to continue serving through expected component failures.

**Disaster Recovery (DR)** defines how service and data are restored after severe failures.

**RTO** is the target time to restore service.

**RPO** is the acceptable data-loss window.

---

# PART 2 — Availability Is End-to-End

Three API replicas do not create HA if:

```text
single state DB
single queue
single model gateway
single vector store
single MCP server
```

End-to-end path:

```text
Ingress
Runtime
Queue
State
Search
Model
Tools
Audit
```

Each dependency affects availability.

---

# PART 3 — Zone Redundancy

Within one region:

```text
Zone 1 runtime
Zone 2 runtime
Zone 3 runtime
```

Use service capabilities appropriate to the chosen Azure services.

Goals:

```text
avoid single node/rack/zone failure
spread replicas
keep load balancer healthy
maintain quorum/state availability
```

---

# PART 4 — Region Strategy

Options:

```text
Active/Passive
Primary handles traffic
Secondary ready for failover

Active/Active
Multiple regions serve traffic
```

Active/active is more complex for:

```text
workflow state
idempotency
evidence IDs
approval state
vector index consistency
cost
```

---

# PART 5 — Stateful Agent Challenge

Suppose workflow pauses for human approval in Region A.

Region A fails.

Questions:

```text
Is checkpoint replicated?
Can Region B resume same thread?
Is approval token still valid?
Are tool operation IDs preserved?
Will already-completed steps rerun?
```

DR must test the workflow, not only the API endpoint.

---

# PART 6 — RTO/RPO by Data Class

Example:

```text
API service           RTO minutes, no persistent RPO
workflow checkpoints  low RPO
incident evidence     near-zero loss desired
RAG index              can often rebuild, longer RPO acceptable
source documents       authoritative backup required
audit logs             strong retention requirements
```

Different data deserves different recovery strategy.

---

# PART 7 — Model Dependency Failure

Possible strategies:

```text
retry same endpoint
alternate deployment in region
approved fallback model
queue until recovery
read-only degraded mode
```

Fallback model must pass evaluation and policy before being enabled.

Do not dynamically switch to an unknown public model during outage.

---

# PART 8 — Tool/MCP Dependency Failure

If GitHub/AKS/MCP unavailable:

```text
TOOL_UNAVAILABLE
 ↓
preserve partial evidence
 ↓
state evidence gap
 ↓
do not fabricate
 ↓
retry later or finish partial RCA
```

---

# PART 9 — Search/Vector Store Failure

Can the assistant still provide current evidence-only status?

Potential degraded mode:

```text
No reference guidance available
Current evidence remains available
Final answer marks RAG dependency unavailable
```

Architecture should define degraded modes deliberately.

---

# PART 10 — Backup Strategy

Backup/restore test for:

```text
state database
evidence store
configuration/prompt registry
source knowledge documents
vector index if rebuild is expensive
policy configuration
```

Backup that has never been restored is an assumption.

---

# PART 11 — Failover Routing

Ingress layer may route to healthy region.

But ensure:

```text
DNS/front-door health checks
session/thread routing
state availability
identity configuration
private network dependencies
secrets/certificates
```

---

# PART 12 — Disaster Recovery Runbook

```text
1 Declare disaster.
2 Freeze risky writes if state uncertain.
3 Confirm secondary dependencies.
4 Fail traffic.
5 Verify state/evidence integrity.
6 Resume eligible workflows.
7 Refresh volatile evidence.
8 Validate model/tool connectivity.
9 Communicate degraded capabilities.
10 Reconcile when primary returns.
```

---

# PART 13 — Chaos / Failure Testing

Test safely in non-prod:

```text
kill worker mid-tool call
stop state DB connection
block model endpoint
simulate queue outage
remove RAG dependency
force MCP timeout
simulate region-unavailable flag
```

Expected state should be asserted.

---

# PART 14 — Common Mistakes

- HA only at web tier
- active/active without state conflict design
- no idempotency after failover
- backups never restored
- fallback model not evaluated
- stale evidence reused after long outage
- approval automatically replayed after recovery

---

# PART 15 — Interview Q&A

### Q1. Difference between HA and DR?
HA handles expected component failures with minimal interruption; DR restores service after major failure according to RTO/RPO targets.

### Q2. Why is DR harder for agents?
Because workflows carry durable state, tool side effects, evidence history and approvals that must resume consistently.

### Q3. Can vector indexes be rebuilt instead of synchronously replicated?
Often yes if authoritative source data exists and RTO/RPO permit it; the decision depends on rebuild cost and availability requirements.

---

# 🧠 Revision

```text
HA = stay running
DR = recover correctly
Agent DR = compute + state + evidence + approvals + idempotency
```

---

# 📝 Homework

Set RTO/RPO for:

```text
agent API
state DB
evidence store
vector index
audit log
```

Explain why they differ.

---

# 🔁 Next Lesson Kyu?

A reliable platform must prove its behavior continuously. Next we build **agent SRE and observability**.
