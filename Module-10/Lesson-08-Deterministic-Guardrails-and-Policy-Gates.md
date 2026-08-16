# 🚩 Jai Bajrangbali!

# Lesson 08 — Deterministic Guardrails & Policy Gates

> **Use the LLM for reasoning where uncertainty is acceptable; use deterministic code/policy for boundaries where uncertainty is not acceptable.**

---

# 🎯 Lesson Goal

You will understand:

- deterministic vs probabilistic controls
- input, retrieval, tool, output and action gates
- policy decision contracts
- deny/allow/approval-required states
- authorization integration
- confidence and evidence gates
- rate/loop budgets
- fail-closed behavior
- policy observability and tests

---

# PART 1 — English Definition

**A deterministic guardrail is application logic that enforces a repeatable rule independently of the LLM's willingness or interpretation.**

---

# PART 2 — Model Rule vs Host Rule

Model rule:

```text
Please do not call dangerous tools.
```

Host rule:

```python
if tool_name not in allowed_tools:
    raise PolicyDenied()
```

The second is enforceable and testable.

---

# PART 3 — Guardrail Stack

```text
Input Gate
 ↓
Identity / Authorization Gate
 ↓
Retrieval ACL/Freshness Gate
 ↓
Tool Selection Gate
 ↓
Argument/Target Gate
 ↓
Execution Risk Gate
 ↓
Output/Citation Gate
 ↓
Approval Gate
 ↓
Post-Action Verification
```

Defense in depth.

---

# PART 4 — Policy Decision Contract

Prefer enum-like outputs:

```text
ALLOW
DENY
APPROVAL_REQUIRED
INSUFFICIENT_EVIDENCE
RETRYABLE_FAILURE
```

Avoid only prose:

```text
"This seems mostly safe."
```

---

# PART 5 — Input Gate

Validate:

```text
request length
supported intent
environment
resource identifiers
encoding/content limits
caller identity
```

Example:

```python
if environment not in {"dev", "stage", "production"}:
    return "INVALID_ENVIRONMENT"
```

---

# PART 6 — Retrieval Gate

Before context:

```text
caller authorized?
source approved?
source current?
classification allowed?
metadata complete?
```

No policy → no document in prompt.

---

# PART 7 — Evidence Gate

Required for current RCA:

```python
required = {"E1", "E2", "E3"}
current = evidence_ids()
if not required.issubset(current):
    return "INSUFFICIENT_EVIDENCE"
```

This prevents model from filling gaps.

---

# PART 8 — Tool Gate

```python
ALLOWED_TOOLS_BY_AGENT = {
  "pipeline": {"get_pipeline_status"},
  "terraform": {"get_terraform_changes"},
  "aks": {"get_aks_status"},
}
```

Tool must be allowed for both caller/agent and task/environment.

---

# PART 9 — Argument Gate

Check:

```text
type
length
format
enum
inventory membership
resource ownership
environment
```

Valid JSON can still be unsafe.

---

# PART 10 — Risk Gate

Example classification:

```text
READ_ONLY          → allow if authorized
LOW_RISK_WRITE     → policy-specific
HIGH_RISK_WRITE    → approval required
DESTRUCTIVE        → deny or special break-glass path
```

Model does not select the risk class.

---

# PART 11 — Output Gate

Validate:

```text
schema
required sections
citation IDs
source class for current facts
forbidden unsupported claims
secret leakage
unsafe executable content
```

Output failure becomes explicit status.

---

# PART 12 — Confidence Gate

Host computes confidence from evidence policy.

Example:

```text
missing evidence → LOW
full sequence, no direct mechanism verification → MEDIUM
direct multi-source verification → HIGH
```

LLM may explain confidence but not override host rubric.

---

# PART 13 — Approval Gate

```text
proposal
 ↓
policy classifies HIGH_RISK
 ↓
authorization check
 ↓
approval request bound to exact action
 ↓
resume
 ↓
revalidate
```

No raw `approved=True` shared forever.

---

# PART 14 — Loop/Cost Gate

```python
if iterations >= max_iterations:
    return "MAX_ITERATIONS"
if tool_calls >= max_tool_calls:
    return "TOOL_BUDGET_EXCEEDED"
```

Also limit:

```text
tokens
runtime
parallel calls
retrieved context size
```

Security and FinOps reinforce each other.

---

# PART 15 — Fail Closed

High-risk dependency failure:

```text
policy service unavailable
```

Result:

```text
DENY / POLICY_UNAVAILABLE
```

Never infer permission.

---

# PART 16 — Policy as Code

Store versioned rules:

```text
policy_version=p7
```

Test in CI.

Audit records include policy version so decisions are reproducible.

---

# PART 17 — Policy Test Examples

```text
P-01 unknown tool → DENY
P-02 read prod status with read role → ALLOW
P-03 Terraform apply from investigator → DENY
P-04 approved exact NSG restore → ALLOW executor
P-05 approval target mismatch → DENY
P-06 missing evidence → no remediation proposal
P-07 cross-tenant retrieval → DENY
P-08 loop budget exceeded → TERMINATE
```

---

# PART 18 — Observability

Track:

```text
policy decision counts
policy version
reason code
denied operation
agent/caller
environment
approval-required rate
policy service failures
```

Do not log raw secrets.

---

# PART 19 — Vulnerable vs Secure Pattern

Vulnerable:

```python
if llm_says_safe:
    execute()
```

Secure:

```python
proposal = parse()
auth = authorize(identity, proposal)
policy = evaluate(proposal, evidence, env)
if policy == APPROVAL_REQUIRED:
    pause()
```

---

# PART 20 — Common Mistakes

- all guardrails implemented in prompt
- no explicit policy status codes
- schema check only
- approval not bound to exact target
- missing policy service fails open
- loop/cost has no limits
- model chooses own confidence/risk class
- policy changes not versioned/tested

---

# PART 21 — Interview Q&A

### Q1. What should be deterministic in an agent?
Authorization, capability allowlists, argument validation, risk policy, approval requirements, budgets and critical output validation.

### Q2. Why not let LLM decide policy?
LLM outputs are probabilistic and vulnerable to prompt manipulation; critical boundaries need repeatable enforcement.

### Q3. What is fail-closed behavior?
When a required security decision cannot be safely made, the action is denied rather than allowed by default.

### Q4. How do you make policy auditable?
Version policy, emit structured reason codes and record decisions with caller/action/request metadata.

---

# 🧠 Revision

```text
LLM = Proposal / Reasoning
Policy Engine = Permission / Safety Decision
```

---

# 📝 Homework

Create 12 policy test cases for the final DevOps AI Assistant and mark which are critical release blockers.

---

# 🔁 Next Lesson Kyu?

We now have controls. Next we measure whether the agent behaves correctly through **agent evaluation fundamentals**.
