# 🚩 Jai Bajrangbali!

# Lesson 01 — Project Requirements & Definition of Done

> **A capstone should start with a testable contract, not with code.**

---

# 🎯 Lesson Goal

You will define:

- user stories
- functional requirements
- non-functional requirements
- trust requirements
- safety constraints
- output contract
- failure states
- acceptance criteria
- demo scope
- production vs learning boundaries

---

# PART 1 — Project User Story

```text
As a DevOps engineer,
I want the AI assistant to investigate a failed production deployment,
collect trusted evidence from approved sources,
use runbooks as reference knowledge,
produce a source-backed RCA,
and recommend next checks without making unapproved production changes.
```

---

# PART 2 — Functional Requirements

The assistant must:

```text
FR1 accept incident description
FR2 validate environment/cluster identifiers
FR3 select relevant specialist agents
FR4 collect read-only pipeline evidence
FR5 collect read-only Terraform evidence
FR6 collect read-only AKS evidence
FR7 retrieve approved reference knowledge
FR8 preserve source IDs
FR9 detect missing/conflicting evidence
FR10 generate grounded RCA
FR11 validate citations and required fields
FR12 propose remediation only after RCA validation
FR13 require policy + authorization + human approval before write
FR14 preserve audit/status
```

---

# PART 3 — Non-Functional Requirements

```text
NFR1 traceable execution
NFR2 deterministic safety controls
NFR3 bounded loops
NFR4 dependency timeouts
NFR5 resumable state design
NFR6 secret redaction
NFR7 environment isolation
NFR8 testable release gates
NFR9 cost limits
NFR10 degraded-mode behavior
```

---

# PART 4 — Trust Requirements

Current incident facts may come only from:

```text
CURRENT_EVIDENCE [E*]
```

Reference guidance:

```text
REFERENCE [R*]
```

Model-generated statements:

```text
PROPOSAL / INFERENCE
```

Never silently upgrade inference to evidence.

---

# PART 5 — Output Contract

Final RCA:

```text
Root Cause
Confirmed Impact
Evidence
Evidence Gaps
Conflicts
Recommended Next Checks
Confidence
Sources
```

If evidence insufficient:

```text
status=INSUFFICIENT_EVIDENCE
```

---

# PART 6 — Failure States

Explicit statuses:

```text
INVALID_INPUT
CAPABILITY_MISSING
TOOL_ERROR
AUTHORIZATION_FAILED
INSUFFICIENT_EVIDENCE
UNRESOLVED_CONFLICT
GENERATION_FAILED
VALIDATION_FAILED
APPROVAL_REQUIRED
HUMAN_REJECTED
SUCCESS
```

Do not convert failures into generic text.

---

# PART 7 — Safety Constraints

```text
1 No arbitrary shell execution.
2 No direct kubectl/Terraform string execution from LLM output.
3 Read-only investigation by default.
4 Tool names allowlisted.
5 Arguments validated.
6 Reference docs treated as data, not instructions.
7 Write executor separate from investigator.
8 Approval bound to exact action/target.
9 Secrets redacted.
10 Loop count bounded.
```

---

# PART 8 — Learning vs Production Scope

Learning capstone:

```text
deterministic simulated evidence
local runbooks
local Ollama/Qwen optional
in-memory checkpoint examples
simulated approval
NO real Azure mutation
```

Production upgrade:

```text
authenticated MCP/API tools
persistent state
managed identity
private networking
central telemetry
real approval service
isolated executor
```

---

# PART 9 — Definition of Done

A green demo is not enough.

```text
[ ] happy path passes
[ ] no-evidence path passes
[ ] tool failure path passes
[ ] conflict path passes
[ ] invalid citation path fails safely
[ ] injection test passes
[ ] secret test passes
[ ] unknown tool denied
[ ] write without approval denied
[ ] graph loop bounded
[ ] final output reproducible
[ ] architecture documented
```

---

# PART 10 — Demo Incident

```text
Incident:
Production AKS deployment failed after Terraform networking change.

Expected evidence:
[E1] pipeline failed during Terraform Apply
[E2] NSG rule aks-subnet-allow removed
[E3] AKS connectivity degraded

Reference:
[R1] AKS networking guidance
[R2] Terraform network-change guidance
```

---

# PART 11 — Success Criteria

A strong RCA might say:

```text
Current evidence confirms that the NSG allow rule was removed [E2],
and AKS connectivity validation became degraded [E3].
The deployment failed during Terraform Apply [E1].
This is consistent with the networking guidance [R1].
```

It must not invent:

```text
who removed it
customer outage duration
exact blocked port
successful remediation
```

---

# PART 12 — Interview Q&A

### Q1. Why define failure states before implementation?
Because production systems need deterministic behavior when dependencies/evidence are missing; otherwise the model tends to fill gaps with plausible text.

### Q2. What makes this project different from a chatbot?
It has controlled capabilities, durable state, evidence provenance, validation, policy, approval and release evaluation.

### Q3. Why keep learning write actions simulated?
To validate orchestration and safety without creating unnecessary infrastructure risk during development.

---

# 🧠 Revision

```text
Good Capstone =
Requirements + Trust Contract + Failure Contract + Tests + Architecture
```

---

# 📝 Homework

Write 5 additional negative acceptance tests for the final project.

---

# 🔁 Next Lesson Kyu?

Requirements are locked. Next we create the **repository/component architecture** so responsibilities stay clean instead of becoming one giant Python file.
