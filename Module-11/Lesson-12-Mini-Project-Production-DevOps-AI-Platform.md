# 🚩 Jai Bajrangbali!

# Lesson 12 — Mini Project: Production DevOps AI Platform

> **Final goal: design the Azure production platform that will host the Module 12 enterprise DevOps AI Assistant.**

---

# 🎯 Project Scenario

An enterprise wants a DevOps AI platform that can:

```text
- investigate GitHub/Azure/AKS/Terraform incidents
- retrieve approved runbooks
- call read-only MCP/tool integrations
- run stateful multi-agent workflows
- generate grounded RCA
- propose controlled remediation
- require approval for writes
- preserve evidence/audit
- scale and recover in production
```

---

# PART 1 — Reference Architecture

```text
                        USERS / AUTOMATION
                               ↓
                      Entra ID / AuthN
                               ↓
                     WAF / API Gateway
                               ↓
                    DevOps AI API Layer
                               ↓
                   Async Job / Queue Layer
                               ↓
                 Stateful Agent Worker Pool
                 (AKS/App runtime choice)
        ┌──────────────────────┼──────────────────────┐
        ↓                      ↓                      ↓
   Model Gateway          Knowledge/RAG          Tool/MCP Gateway
        ↓                      ↓                      ↓
 Approved Models      Search/Vector Index      GitHub/Azure/AKS
                               ↓                      ↓
                       Approved Sources          Read-only APIs
        └──────────────────────┼──────────────────────┘
                               ↓
                State + Evidence + Audit Stores
                               ↓
                  Azure Monitor / App Insights
                               ↓
                  SIEM / Policy / Eval Signals
```

Cross-cutting:

```text
Managed/Workload Identity
RBAC
Private Networking
Private DNS
Key Vault
Encryption
Rate Limits
Budgets
Human Approval
```

---

# PART 2 — Subscription / Environment Blueprint

```text
Platform Subscription
- hub network
- firewall
- shared DNS
- central monitoring
- shared AI gateway (optional)

AI-DEV Subscription
- dev runtime
- synthetic data
- sandbox MCP/tools

AI-STAGE Subscription
- production-like topology
- integration/eval testing

AI-PROD Subscription
- prod runtime
- prod state/evidence
- approved knowledge
- prod read tools
- separate write executor
```

---

# PART 3 — Identity Blueprint

```text
agent-api-mi
agent-worker-mi
rag-ingestion-mi
read-tool-mi
write-executor-mi
ci-cd-federated-identity
```

Rules:

```text
agent worker cannot write production infrastructure
write executor cannot be invoked without policy/approval token
rag ingestion cannot read unrelated secrets
CI/CD cannot become runtime identity
```

---

# PART 4 — Network Blueprint

```text
Internet/User
 ↓
WAF/Gateway
 ↓
Private workload subnet
 ↓
Private Endpoints:
- state DB
- storage
- search
- Key Vault

Controlled egress:
- model gateway
- approved MCP servers
- GitHub/Azure APIs
```

Validate DNS from the actual runtime environment.

---

# PART 5 — Runtime Blueprint

Suggested pattern for complex enterprise implementation:

```text
API Deployment
Worker Deployment
Tool/MCP Adapter Deployment
RAG Ingestion Worker
Eval Runner
```

On AKS:

```text
separate service accounts
resource limits
HPA/KEDA-style event scaling as appropriate
PDB/zone spread
network policy
readiness/liveness
```

The exact compute can be App Service/Container Apps/AKS depending requirements.

---

# PART 6 — Data Blueprint

```text
Workflow State
→ persistent state/checkpoint backend

Evidence
→ durable evidence store

Knowledge Sources
→ authoritative document store

Vector/Search Index
→ rebuildable/search-optimized layer

Audit
→ append-oriented security/operations log
```

Never rely on vector index as authoritative source backup.

---

# PART 7 — Reliability Blueprint

```text
API replicas
worker replicas
queue buffering
state HA
search HA
model gateway redundancy
bounded retries
circuit breakers
regional DR runbook
```

Critical workflow status must survive worker restart.

---

# PART 8 — Observability Blueprint

Every request propagates:

```text
request_id
incident_id
thread_id
agent_version
```

Trace stages:

```text
validate
route
specialists
tools
RAG
model
validation
approval
finalize
```

Dashboards:

```text
SLO
queue
model
RAG
tools
security
cost
approval/write actions
```

---

# PART 9 — CI/CD Blueprint

```text
PR
 ↓
Unit + Contract + IaC Tests
 ↓
Security Scan
 ↓
Agent Eval
 ↓
Red-Team Regression
 ↓
Build Artifact
 ↓
Dev
 ↓
Stage Integration + Load + DR Tests
 ↓
Production Approval
 ↓
Canary
 ↓
Full Rollout
```

---

# PART 10 — Production Failure Matrix

| Failure | Expected Behavior |
|---|---|
| Model timeout | retry bounded / explicit degraded state |
| Search unavailable | evidence-only response if policy allows |
| MCP server unavailable | preserve evidence gap |
| State DB unavailable | stop accepting resumable workflows or fail safely |
| Queue backlog | backpressure/load shedding |
| Key Vault failure | no secret fallback from source code |
| Region outage | invoke DR plan |
| Eval regression | block release |
| Approval system unavailable | block write execution |

---

# PART 11 — Architecture Review Questions

```text
1. What is public?
2. What is private?
3. Which identity owns each call?
4. Which component can write prod?
5. Where are approvals enforced?
6. Where is evidence durable?
7. How is RAG authorization enforced?
8. What happens on model outage?
9. How does a paused workflow survive restart?
10. How is an unsafe release blocked?
11. How are costs allocated?
12. What is the DR strategy?
```

---

# PART 12 — Practical V1→V10

The `examples/` labs model architecture decisions without requiring a paid Azure environment:

```text
V1 workload decomposition
V2 environment boundaries
V3 identity policy
V4 network path validation
V5 runtime decision matrix
V6 storage trust classes
V7 queue/backpressure
V8 HA/DR scoring
V9 observability/SLO model
V10 production readiness scorecard
```

These are architecture-as-code learning exercises.

---

# PART 13 — Acceptance Criteria

- [ ] prod and non-prod identities separated
- [ ] production write executor isolated
- [ ] private dependency paths documented
- [ ] state/evidence/knowledge/audit separated
- [ ] async workflow strategy defined
- [ ] concurrency/backpressure defined
- [ ] HA and DR targets documented
- [ ] end-to-end correlation/tracing defined
- [ ] CI/CD includes security + eval gates
- [ ] data/model/tool ownership documented
- [ ] cost budget and attribution defined
- [ ] production readiness review complete

---

# PART 14 — Interview Explanation

**“I would deploy the agent as an enterprise workload rather than a single LLM service. The API and long-running workers are separated, every component uses least-privilege identity, state/evidence/RAG data have separate stores and trust classes, external tools are exposed through controlled MCP/API gateways, production networking is private with governed egress, write execution uses a separate executor behind authorization and human approval, and CI/CD blocks releases unless security and agent evaluations pass. Observability traces every state transition, model/tool call and policy decision.”**

---

# 🧠 Final Module 11 Formula

```text
Production Agent Platform =
Agent Logic
+ Identity
+ Network
+ Durable State
+ Evidence/Data Governance
+ Safe Capabilities
+ Scale
+ HA/DR
+ Observability
+ CI/CD
+ Security/Evals
+ FinOps
```

✅ Module 11 complete → Module 12 builds the capstone application on top of this platform blueprint.
