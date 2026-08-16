# 🚩 Jai Bajrangbali!

# Lesson 08 — Deterministic Guardrails & Policy Gates

> **Critical safety decisions ko probabilistic model se deterministic application policy me shift karo.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- model guardrail vs deterministic guardrail
- policy engine mental model
- allowlist/denylist/schema/risk gates
- authorization + approval separation
- input/output/tool/result guards
- fail-open vs fail-closed

---

# PART 1 — English Definition

A **deterministic guardrail** is application-controlled logic that enforces a rule predictably regardless of the LLM's preference or output.

---

# PART 2 — Model Rule vs Policy Rule

Prompt rule:
```text
Never restart production without approval.
```
Useful, but probabilistic.

Policy rule:
```python
if env == "production" and operation == "restart":
    return "HUMAN_APPROVAL_REQUIRED"
```
Enforceable.

Use both, but trust policy for safety.

---

# PART 3 — Guardrail Locations

```text
Input Guard
 ↓
Planner/Model
 ↓
Tool Proposal Guard
 ↓
Tool Executor
 ↓
Tool Result Guard
 ↓
Model/Synthesis
 ↓
Output Guard
 ↓
Downstream Consumer
```

Security is not one middleware call.

---

# PART 4 — Policy Inputs

Policy may inspect:
```text
user identity
role/team
environment
tool name
tool arguments
resource scope
incident/change ID
risk class
maintenance window
approval token
current workflow state
```

Do not ask LLM to infer trusted identity or permission.

---

# PART 5 — Example Policy

```python
WRITE_TOOLS = {"restart_deployment", "apply_terraform"}
PROD = {"production"}

if tool not in APPROVED_TOOLS:
    return "BLOCKED_UNKNOWN_TOOL"

if environment not in ALLOWED_ENVIRONMENTS:
    return "BLOCKED_SCOPE"

if tool in WRITE_TOOLS and environment in PROD:
    return "APPROVAL_REQUIRED"

return "ALLOWED"
```

Then separate authorization check should validate caller permission.

---

# PART 6 — Fail Closed

If policy service fails:
```text
unknown policy result + prod write
```
Safer default:
```text
BLOCK / REVIEW
```
not:
```text
allow because policy unavailable
```

For low-risk read operations, availability trade-offs may differ.

---

# PART 7 — Structured Output Guard

Model proposal:
```json
{
  "action":"restart_deployment",
  "environment":"production",
  "reason":"network issue"
}
```

Validation sequence:
```text
schema
→ allowed enum
→ target exists
→ evidence references valid
→ caller authorization
→ risk policy
→ approval
```

Pydantic validates shape, not permission or factual support.

---

# PART 8 — Result Guard

Tool can return unexpected content:
```text
status + secret
status + malicious instruction
massive payload
```

Normalize:
```text
expected fields only
size limit
secret redaction
source/provenance
error classification
```

---

# PART 9 — Human Approval Is Not Authorization

Human clicks Approve.
Still verify:
```text
who approved?
are they authorized?
what exact arguments were approved?
has proposal changed since approval?
is approval expired?
```

Bind approval to exact action hash/version.

---

# PART 10 — Guardrail Test Matrix

```text
unknown tool → blocked
prod read → allowed if authorized
prod write → approval required
invalid environment → blocked
approval for old args → blocked
secret in output → redacted/block
policy unavailable + destructive action → blocked
```

---

# PART 11 — Interview Q&A

### Q1. Why deterministic guardrails?
They provide predictable enforcement for critical rules that should not depend on model compliance.

### Q2. Model-based guardrails useful kaha hain?
For fuzzy detection/classification signals such as suspicious content, but high-impact execution policy should be deterministic where possible.

### Q3. Fail-open vs fail-closed?
Fail-open allows operation when control fails; fail-closed blocks. High-risk actions should generally fail closed.

---

# PART 12 — Revision

```text
Prompt = behavior guidance
Guardrail = enforcement
Auth = permission
Approval = decision
Schema = shape
Evidence = support
```

---

# PART 13 — Homework

Create policy rules for 10 tools across dev/stage/prod, with read/write risk, auth requirement, approval rule and failure behavior.

---

# 🔁 Next Lesson Kyu?

Controls ban gaye. Ab prove karna hai ki agent expected behavior consistently follow karta hai. Next: agent evaluation fundamentals.
