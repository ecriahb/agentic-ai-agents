# 🚩 Jai Bajrangbali!

# Lesson 03 — Trusted Evidence & Tool Layer

> **The final assistant may reason freely, but current incident facts must be collected through controlled, source-labelled evidence contracts.**

---

# 🎯 Lesson Goal

You will implement/design:

- read-only tool contracts
- allowlists
- argument validation
- evidence envelopes
- source timestamps
- tool error states
- duplicate protection
- read/write separation
- evidence provenance

---

# PART 1 — Evidence Contract

Every successful observation becomes:

```python
{
    "id": "E2",
    "kind": "CURRENT_EVIDENCE",
    "operation": "get_terraform_changes",
    "arguments": {"environment": "production"},
    "observed_at": "...",
    "source": "terraform-tool",
    "payload": {...}
}
```

Every failure becomes evidence about the tool failure, not about the infrastructure:

```python
{
    "id": "E2",
    "kind": "TOOL_ERROR",
    "operation": "get_terraform_changes",
    "error": "timeout"
}
```

---

# PART 2 — Final Read-Only Tool Set

```text
get_pipeline_status(environment)
get_terraform_changes(environment)
get_aks_status(cluster_name)
```

Optional future tools:

```text
get_azure_monitor_metrics
get_kubernetes_events
get_network_effective_routes
```

But add capability only when it has a clear contract and need.

---

# PART 3 — Allowlist

```python
ALLOWED_TOOLS = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}
```

Anything else:

```text
POLICY_BLOCKED
```

Model cannot invent `delete_namespace` and have host execute it.

---

# PART 4 — Argument Validation

```text
environment ∈ {dev, stage, production}
cluster_name ∈ approved inventory
```

Also validate:

```text
length
characters
resource ownership
caller scope
```

Schema validation prevents malformed input; policy validation prevents unauthorized valid input.

---

# PART 5 — Host + Server Validation

Defense in depth:

```text
Agent proposal
 ↓
Host validation
 ↓
MCP/API request
 ↓
Server validation
 ↓
Backend
```

Never assume client validation is sufficient.

---

# PART 6 — Evidence IDs

Use stable source IDs per investigation:

```text
E1 pipeline
E2 Terraform
E3 AKS
```

If retry occurs, do not create E2/E4 duplicates for the same logical observation unless you intentionally record a new timestamped observation.

---

# PART 7 — Freshness

Evidence contains:

```text
observed_at
```

If graph resumes after an hour, volatile evidence may need refresh.

Example:

```text
E3 at 10:00 degraded
E4 at 11:00 healthy
```

Do not silently overwrite history; preserve versions or latest pointer.

---

# PART 8 — Provenance

Evidence should answer:

```text
Who collected it?
From which system?
Which operation?
Which arguments?
When?
Was collection successful?
```

This enables audit and conflict resolution.

---

# PART 9 — Tool Result Normalization

Backend APIs return different structures.

Normalize to domain objects:

```text
status
summary
resource_id
observed_at
raw_reference/hash
```

Do not lose important raw evidence, but avoid dumping huge raw payloads into every prompt.

---

# PART 10 — Tool Error Policy

```text
TIMEOUT → maybe bounded retry
AUTH_DENIED → do not retry blindly
NOT_FOUND → validate target
RATE_LIMIT → backoff
INVALID_ARGUMENT → fail immediately
```

LLM should not decide retry policy alone.

---

# PART 11 — Read vs Write Layer

Investigation:

```text
read-tool identity
```

Remediation:

```text
write-executor identity
```

The final learning project does not perform real writes. It produces a validated proposal only.

---

# PART 12 — Demo Evidence

```text
[E1]
Pipeline deployment failed during Terraform Apply.

[E2]
Terraform plan/apply removed `aks-subnet-allow`.

[E3]
AKS network connectivity validation is degraded.
```

These are enough to support a medium/high-confidence causal hypothesis depending policy; they do not prove customer impact or actor identity.

---

# PART 13 — Common Mistakes

- tool output sent to model without source ID
- timeout interpreted as “no issue”
- model chooses arbitrary resource ID
- no environment allowlist
- duplicate retries append contradictory copies
- evidence timestamp omitted
- same credential used for writes

---

# PART 14 — Interview Q&A

### Q1. Why normalize tool results?
To give the orchestration and validation layers a stable contract while preserving source/provenance.

### Q2. What is the difference between tool schema validation and authorization?
Schema validates shape/type; authorization determines whether the caller may perform the operation on the target.

### Q3. Why record tool errors in evidence state?
So downstream reasoning knows the evidence gap exists and does not mistake missing data for a negative result.

---

# 🧠 Revision

```text
Tool Call → Validate → Execute → Normalize → Label → Preserve
```

---

# 📝 Homework

Add an evidence contract for `get_effective_nsg_rules(subnet_id)` and list required validation.

---

# 🔁 Next Lesson Kyu?

Current evidence tells what happened. Next we add **reference knowledge/RAG** to explain what the evidence means and what safe checks should follow.
