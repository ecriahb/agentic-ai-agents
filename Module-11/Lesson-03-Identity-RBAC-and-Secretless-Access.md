# 🚩 Jai Bajrangbali!

# Lesson 03 — Identity, RBAC & Secretless Access

> **An enterprise agent should not carry broad credentials in configuration; every runtime identity should have the smallest permissions required for its role.**

---

# 🎯 Lesson Goal

You will learn:

- authentication vs authorization
- workload identity and managed identity mental models
- per-component identities
- least privilege
- Azure RBAC scope
- Key Vault boundaries
- secretless patterns
- credential rotation and break-glass
- write-action approval vs authorization

---

# PART 1 — English Definitions

**Authentication** proves who or what the caller is.

**Authorization** determines what that identity may access or execute.

**Least privilege** gives only the permissions required for a defined task, scope and duration.

---

# PART 2 — Identity Architecture

Bad design:

```text
One service principal
      ↓
Agent API
RAG ingestion
AKS tools
Terraform tools
Storage
Everything
```

Compromise one component → compromise entire platform.

Better:

```text
Agent API Identity
RAG Ingestion Identity
Read-Only Tool Identity
Write Executor Identity
Observability Identity
CI/CD Identity
```

Each has a different permission contract.

---

# PART 3 — Secretless First

Prefer platform/workload identity mechanisms where supported:

```text
Workload
 ↓
platform-issued identity token
 ↓
Azure resource
```

Instead of:

```text
APP_CLIENT_SECRET=long-lived-secret
```

Benefits:
- fewer static secrets
- simpler rotation
- better attribution
- narrower scopes

---

# PART 4 — AKS Workload Identity Mental Model

```text
Kubernetes Service Account
        ↓
Federated Identity
        ↓
Microsoft Entra workload identity
        ↓
Azure Resource
```

Use separate service accounts/identities for separate workloads rather than one cluster-wide credential.

---

# PART 5 — RBAC Scope

Scopes can be broad or narrow:

```text
Management Group
Subscription
Resource Group
Resource
```

Production rule:

```text
Choose the narrowest practical scope.
```

Example:

```text
AKS status reader
→ read only target cluster/resource group

Evidence storage writer
→ append/write only evidence container
```

---

# PART 6 — Read Identity vs Write Identity

Do not let investigation runtime inherit remediation privileges.

```text
Investigation Agent
   ↓ read-only
Azure/GitHub/MCP

Remediation Executor
   ↓ separate identity
Write API
```

Write executor is invoked only after:

```text
validated proposal
+ authorization
+ policy
+ approval
```

This reduces excessive agency.

---

# PART 7 — Key Vault Role

Key Vault may still be needed for:

```text
third-party API secrets
TLS certificates
legacy credentials
signing keys
```

But:

```text
Secret in Key Vault
!=
Everyone can read it
```

Access should be identity-specific and auditable.

---

# PART 8 — Authentication ≠ Approval

A user may be authorized to request a production action but the workflow may still require an explicit approval step.

```text
Authorized user
      ↓
Agent proposes restart
      ↓
Policy says approval required
      ↓
Approver approves
      ↓
Executor checks authorization again
      ↓
Action
```

Approval is a business/safety gate, not a substitute for RBAC.

---

# PART 9 — Tool Authorization Contract

Every tool call should have:

```text
caller identity
operation
resource scope
arguments
environment
risk class
authorization result
approval state
request/incident ID
```

Model should not decide RBAC.

---

# PART 10 — Example Capability Matrix

```text
Agent Runtime
  get_pipeline_status      ALLOW
  get_terraform_plan       ALLOW
  get_aks_health           ALLOW
  apply_terraform          DENY
  restart_prod_cluster     DENY

Remediation Executor
  restore_approved_nsg     ALLOW_WITH_APPROVAL
```

---

# PART 11 — Credential Failure Behavior

Possible failures:

```text
token expired
federation misconfigured
RBAC denied
Key Vault unavailable
identity endpoint unavailable
```

Safe response:

```text
AUTHORIZATION_FAILED
or
DEPENDENCY_UNAVAILABLE
```

Not:

```text
"probably no issue found"
```

---

# PART 12 — Break-Glass

Production may require emergency privileged access.

Design principles:

```text
not embedded in agent
human-controlled
short-lived
heavily audited
separate path
post-incident review
```

The AI assistant should not hold break-glass credentials.

---

# PART 13 — Identity Observability

Log safely:

```text
principal/object identity
operation
scope
authorization decision
policy decision
approval ID
```

Do not log tokens or credentials.

---

# PART 14 — Common Mistakes

- one identity for every component
- Contributor at subscription scope for read-only assistant
- static secrets in repo/environment files
- model asked “is this user authorized?”
- approval treated as authorization
- write tool and read tool share credentials
- no identity attribution in audit logs

---

# PART 15 — Interview Q&A

### Q1. Why separate read and write identities?
To reduce blast radius and prevent the investigation path from automatically inheriting remediation authority.

### Q2. Why prefer managed/workload identities?
They reduce long-lived secret handling and provide identity-based, auditable access.

### Q3. Is human approval enough to authorize an operation?
No. Authorization must still be enforced by trusted identity and policy systems.

### Q4. Where should authorization checks occur?
At host/policy boundaries and again at the capability/executor boundary for defense in depth.

---

# 🧠 Revision

```text
Identity = Who are you?
RBAC = What may you do?
Approval = Should this risky action proceed now?
```

---

# 📝 Homework

Create RBAC design for:

```text
agent-api
rag-ingestion
read-only-investigator
remediation-executor
ci-cd
```

Give each 3 allowed and 3 denied actions.

---

# 🔁 Next Lesson Kyu?

Identity controls *who* may access something. Next we control **from where and through which network path** those services can communicate.
