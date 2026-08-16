# 🚩 Jai Bajrangbali!

# Lesson 03 — Tool Abuse, Excessive Agency & Side Effects

> **Agent ko tool dena capability dena hai; production me har capability ko scope, policy, approval aur blast-radius controls chahiye.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- excessive agency kya hai
- read vs write vs destructive tools
- why tool schema != permission
- least privilege, allowlists and argument policy
- idempotency, dry-run and approval gates
- side-effect retry danger

---

# PART 1 — English Definition

**Excessive agency** occurs when an AI system is granted more functionality, permissions or autonomy than required for its task, increasing the potential impact of mistakes or attacks.

---

# PART 2 — Capability Classes

```text
READ
get_aks_status
read_pipeline_log
read_terraform_plan

LOW-RISK WRITE
create_draft_ticket
create_draft_comment

HIGH-RISK WRITE
restart_workload
apply_terraform
merge_pr
change_firewall_rule

DESTRUCTIVE
remove_namespace
destroy_infrastructure
rotate/delete secrets
```

Do not put all classes in one unrestricted tool pool.

---

# PART 3 — Module 1 Connection

Module 1 rule:
```text
model requests tool
host validates
host executes
```

Module 10 adds:
```text
model proposal
 ↓
allowlist
 ↓
argument schema
 ↓
identity/RBAC
 ↓
risk classification
 ↓
approval if required
 ↓
idempotency/dry-run controls
 ↓
execute
```

---

# PART 4 — Argument-Level Risk

Same tool can have different risk:
```text
restart_deployment(environment="dev")
restart_deployment(environment="production")
```

Policy should inspect arguments, not only tool name.

Example:
```python
if tool == "restart_deployment" and env == "production":
    return "HUMAN_APPROVAL_REQUIRED"
```

---

# PART 5 — Tool Schema Is Not Authorization

Schema proves shape:
```json
{"environment":"production","deployment":"api"}
```

It does not prove:
```text
user may restart prod
change is within maintenance window
incident approval exists
```

Authorization comes from trusted policy/identity systems.

---

# PART 6 — Retry Danger

Read tool retry:
```text
get_status → timeout → retry
```
Usually safe.

Write tool retry:
```text
create_ticket → timeout after server created it → retry → duplicate ticket
```

Worse:
```text
apply_change → unknown result → automatic retry
```

Use:
```text
idempotency key
operation ID
status lookup
manual review for unknown write outcome
```

---

# PART 7 — Dry Run / Plan First

Safer DevOps pattern:
```text
Propose change
 ↓
terraform plan / kubectl diff / validation
 ↓
human review
 ↓
approved execution identity
 ↓
post-change verification
```

Agents should prefer reversible/read-only investigation before mutation.

---

# PART 8 — Blast Radius

Limit:
```text
subscription
resource group
namespace
environment
repository
branch
API endpoint
```

Avoid global credentials when incident needs one cluster.

---

# PART 9 — Tool Abuse Tests

```text
unknown tool requested
prod write without approval
valid tool + invalid target
valid tool + path traversal argument
repeat destructive call
write tool after timeout
cross-environment access
agent tries to change its own allowlist
```

Each test should have deterministic expected status.

---

# PART 10 — Common Mistakes

- one service principal with Owner permission
- read/write tool names look similar
- model picks approval policy
- automatic retries on side effects
- no operation IDs
- no change audit
- no environment allowlist
- no post-action verification

---

# PART 11 — Interview Q&A

### Q1. How do you reduce excessive agency?
Minimize tools, scope credentials, validate arguments, separate read/write identities, require approval for high-risk operations and enforce execution policies outside the model.

### Q2. Why are write retries dangerous?
Because the previous attempt may have succeeded despite a timeout, so retries can duplicate or compound side effects.

### Q3. What does dry-run provide?
A pre-execution representation of intended changes that can be validated and approved before mutation.

---

# PART 12 — Revision

```text
Capability != permission
Schema != authorization
Proposal != execution
Timeout != failure-to-execute
Approval != identity
```

---

# PART 13 — Homework

Classify 15 DevOps operations into read/low-write/high-write/destructive and define approval + RBAC policy for each.

---

# 🔁 Next Lesson Kyu?

Even read-only agents can cause harm if they leak secrets or produce unsafe outputs consumed by automation. Next: sensitive data and output handling.
