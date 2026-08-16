# 🚩 Jai Bajrangbali!

# Lesson 02 — Azure Landing Zones & Environment Separation

> **Production AI safety starts before prompts and tools: the cloud boundary must prevent dev experiments from inheriting production power.**

---

# 🎯 Lesson Goal

You will learn:

- landing-zone thinking
- platform vs workload responsibilities
- management group/subscription/environment separation
- prod vs non-prod identity isolation
- shared AI services vs workload-owned services
- central platform team vs application team boundaries
- policy and network inheritance
- blast-radius control

---

# PART 1 — English Definition

**A landing zone is a governed cloud environment that provides standardized identity, networking, policy, logging, security and subscription foundations for workloads.**

---

# PART 2 — Why Environment Separation Matters More for Agents

Traditional application bug:

```text
wrong response
```

Agent bug with shared credentials:

```text
wrong response
+
wrong tool call
+
production side effect
```

Therefore:

```text
Dev Agent Identity
must not be able to reach
Production Capability Plane
```

---

# PART 3 — Enterprise Hierarchy Mental Model

```text
Tenant
 ↓
Management Groups
 ├─ Platform
 ├─ Non-Production
 └─ Production
       ↓
Subscriptions
       ↓
Resource Groups
       ↓
AI Workload Components
```

Exact hierarchy varies, but separation intent should be explicit.

---

# PART 4 — Platform vs Application Landing Zone

Platform-owned services may include:

```text
Hub network
Firewall
DNS
Central logging
Policy
Shared container registry
Secrets governance
Private DNS resolver
```

Workload-owned services may include:

```text
Agent API
AKS/App Service
Vector/Search service
State DB
Evidence storage
Workload Key Vault
MCP adapters
```

The workload consumes platform controls rather than reimplementing everything.

---

# PART 5 — Environment Model

Recommended learning model:

```text
DEV
- synthetic data
- local/sandbox tools
- low-cost model
- no prod access

STAGE
- production-like topology
- masked/safe test data
- realistic policies
- integration/eval testing

PROD
- real identities
- approved models/tools
- strict network/RBAC
- audit + alerts
- write approval gates
```

Never promote secrets/credentials from dev to prod.

---

# PART 6 — Subscription Separation

Why separate prod subscription?

```text
RBAC scope
Policy scope
Budget scope
Quota scope
Network scope
Incident blast radius
Audit ownership
```

A resource-group-only boundary may be too weak for high-risk enterprise agents.

---

# PART 7 — Shared Model Platform vs Workload-Owned Models

Option A:

```text
Each workload owns model endpoint
```

Advantages:
- independent lifecycle
- clear cost ownership
- workload-specific policies

Option B:

```text
Central AI gateway/platform
     ↓
multiple workloads
```

Advantages:
- centralized quotas
- model governance
- logging/filtering
- consistent authentication

Trade-off:
- platform dependency
- shared blast radius if poorly isolated

---

# PART 8 — Shared RAG Is Dangerous by Default

Do not create one giant enterprise vector index with only prompt-level isolation.

Safer dimensions:

```text
tenant/team
classification
environment
source ACL
version
owner
```

Retrieval authorization must happen before context reaches the model.

---

# PART 9 — Policy Inheritance

Examples:

```text
Prod subscription:
- deny public storage
- require private endpoints where applicable
- require diagnostic settings
- restrict regions
- require tags
- restrict privileged role assignment
```

AI-specific policies can add:

```text
approved model providers
approved MCP servers
data classification limits
mandatory eval gate metadata
```

---

# PART 10 — CI/CD Promotion Path

```text
feature branch
 ↓
unit tests
 ↓
security/eval tests
 ↓
dev deploy
 ↓
integration tests
 ↓
stage deploy
 ↓
red-team/regression suite
 ↓
approval
 ↓
prod deploy
```

Artifacts should be promoted, not rebuilt differently for prod without traceability.

---

# PART 11 — Configuration Separation

Bad:

```python
if env == "prod":
    key = "..."
```

Better:

```text
Same application artifact
+
Environment-specific configuration
+
Environment-specific identity
+
Environment-specific policy
```

---

# PART 12 — DevOps AI Example

```text
DEV Agent
  ↓
Fake pipeline logs
Local runbooks
No Azure writes

STAGE Agent
  ↓
Stage AKS
Stage GitHub repo
Masked incidents

PROD Agent
  ↓
Production read-only APIs
Approved production knowledge
Write proposals behind approval
```

---

# PART 13 — Failure Scenario

Suppose developer accidentally registers `restart_prod_aks` in dev.

If identity/network boundaries are correct:

```text
Dev runtime
 ↓
tries prod capability
 ↓
RBAC/network/policy deny
```

That is defense in depth.

Prompt rules alone are not enough.

---

# PART 14 — Common Mistakes

- same service principal in all environments
- prod and non-prod vector collections mixed
- shared Key Vault without clear access boundaries
- dev can call prod MCP server
- same state DB for stage/prod
- no separate budget/quota
- staging does not resemble prod security model

---

# PART 15 — Interview Q&A

### Q1. Why use separate subscriptions for production?
To create stronger RBAC, policy, budget, network and blast-radius boundaries.

### Q2. What should be identical across dev/stage/prod?
The deployable application behavior and policy model should be as consistent as possible, while identities, data and configuration remain environment-specific.

### Q3. Can RAG metadata filtering replace environment isolation?
No. Metadata helps retrieval policy, but it is not a complete security boundary.

### Q4. Why is stage important for agents?
Because agent behavior depends on external tools, policies, state and models; production-like integration must be tested before release.

---

# 🧠 Revision

```text
Environment Separation =
Identity + Network + Data + Policy + State + Cost
```

---

# 📝 Homework

Design three subscriptions or equivalent boundaries:

```text
ai-dev
ai-stage
ai-prod
```

List what must never be shared between them.

---

# 🔁 Next Lesson Kyu?

Environment boundary is ready. Next question: **who is each component, and exactly what may it do?** That is identity and RBAC.
