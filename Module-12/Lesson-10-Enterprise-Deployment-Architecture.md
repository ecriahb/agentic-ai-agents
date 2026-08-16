# 🚩 Jai Bajrangbali!

# Lesson 10 — Enterprise Deployment Architecture

> **The capstone application now gets placed into the Module 11 production platform with explicit identity, networking, state, scale and observability boundaries.**

---

# 🎯 Lesson Goal

You will map:

- API layer
- worker/graph runtime
- model gateway
- RAG/search
- MCP/tool gateway
- state/evidence/audit stores
- identities
- private network paths
- queue/autoscaling
- monitoring
- DR

---

# PART 1 — Deployment Diagram

```text
Users / Automation
       ↓
Entra ID
       ↓
WAF / API Gateway
       ↓
Agent API
       ↓
Queue / Job Layer
       ↓
Stateful Agent Workers
       ↓
┌─────────────┬─────────────┬──────────────┐
│ Model GW    │ RAG/Search  │ MCP/Tools    │
└─────────────┴─────────────┴──────────────┘
       ↓
State / Evidence / Audit
       ↓
Azure Monitor / App Insights / SIEM
```

---

# PART 2 — Identity Mapping

```text
Agent API       → api identity
Agent Worker    → read/runtime identity
RAG ingestion   → ingestion identity
MCP adapters    → scoped read identity
Write executor  → separate narrow write identity
CI/CD           → federated deployment identity
```

No shared Contributor identity.

---

# PART 3 — Network Mapping

Public exposure ideally limited to approved ingress boundary.

Internal paths:

```text
API → queue/state
Worker → model gateway
Worker → search
Worker → MCP gateway
```

Private endpoints and DNS are used where service/platform requirements support them.

Outbound internet is controlled.

---

# PART 4 — Runtime Mapping

Possible implementation:

```text
API deployment
workflow worker deployment
MCP adapter deployment
RAG ingestion worker
security/eval jobs
```

AKS may be chosen for complex Kubernetes-centric environments, but the architecture is portable to other managed runtimes.

---

# PART 5 — State Mapping

```text
thread/checkpoint state → persistent state store
evidence → durable evidence store
knowledge source → authoritative storage
vector/search → retrieval index
audit → centralized append/audit sink
```

Backups/recovery policies differ by class.

---

# PART 6 — Model Mapping

```text
Agent Workers
      ↓
Model Gateway
      ↓
Approved deployment(s)
```

Gateway responsibilities may include:

```text
auth
quota
routing
telemetry
cost attribution
approved model catalog
```

Model fallback must be evaluated.

---

# PART 7 — RAG Mapping

```text
Approved Docs
 ↓ ingestion identity
Chunk/Metadata/ACL
 ↓
Search/Vector Index
 ↓ query with caller policy
Agent Context
```

No cross-team retrieval just because documents are in same service.

---

# PART 8 — MCP/Tool Mapping

```text
Agent Worker
 ↓ trusted client adapter
MCP Gateway/Servers
 ↓
GitHub / Azure / AKS / Monitoring
```

Read-only and write servers/identities should be separated when possible.

---

# PART 9 — Async Mapping

```text
POST /incidents
 ↓
job id
 ↓
queue
 ↓
worker
 ↓
checkpoint
 ↓
status/stream endpoint
```

Approval pauses do not consume an HTTP request thread indefinitely.

---

# PART 10 — Scale Mapping

API scales on request load.

Workers scale on:

```text
queue depth
oldest job age
active workflows
```

Concurrency limited by model/tool dependency budgets.

---

# PART 11 — HA/DR Mapping

```text
multiple API/worker replicas
zone strategy
state backup/replication
queue resilience
search recovery
model dependency plan
regional DR runbook
```

After long recovery, volatile evidence is refreshed.

---

# PART 12 — Observability Mapping

Every run records:

```text
incident_id
request_id
thread_id
agent version
model version
prompt version
policy version
source IDs
```

Trace spans for each node/tool/model/retrieval step.

---

# PART 13 — Security Mapping

```text
WAF/input controls
identity/RBAC
private network
egress policy
MCP trust registry
RAG ACL
policy engine
approval gate
secret redaction
security evaluation
```

Defense in depth means failure of one layer does not expose unrestricted writes.

---

# PART 14 — Common Mistakes

- deployment diagram omits queue/state
- public search/storage endpoints without need
- worker and executor share identity
- tool adapters run with broad permissions
- model gateway is single unmonitored dependency
- no workflow recovery strategy
- no environment-specific data isolation

---

# PART 15 — Interview Q&A

### Q1. Why use asynchronous jobs for this assistant?
Investigation and approval can be long-running; queues/workers decouple user request latency from workflow duration.

### Q2. Why use a model gateway?
To centralize model access policy, routing, telemetry, quotas and cost governance, though it must itself be highly available.

### Q3. Why separate state and evidence stores logically?
State coordinates workflow; evidence supports factual claims and often has different retention/audit requirements.

---

# 🧠 Revision

```text
Capstone Deployment =
Ingress + Runtime + Queue + State + Model + RAG + MCP + Policy + Telemetry
```

---

# 📝 Homework

Draw two versions of the deployment: one using AKS and one using managed App/Container services. Explain trade-offs.

---

# 🔁 Next Lesson Kyu?

Deployment architecture is complete. Next we make it operable through **CI/CD, release, incident and rollback runbooks**.
