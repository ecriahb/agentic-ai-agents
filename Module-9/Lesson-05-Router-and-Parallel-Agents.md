# 🚩 Jai Bajrangbali!

# Lesson 05 — Router & Parallel Specialist Pattern

> **Router ka kaam input ko classify karke right specialist(s) tak bhejna hai; parallelism tabhi useful hai jab branches truly independent hon.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- router vs supervisor
- single-target vs multi-target routing
- parallel fan-out/fan-in
- deterministic merge
- partial failure handling
- DevOps triage use case

---

# PART 1 — Router Definition

A **router** is a bounded decision component that classifies an input and dispatches it to one or more specialized processing paths.

```text
Input → Router → Selected Agent(s)
```

Router usually ongoing conversation coordinator nahi hota.

---

# PART 2 — Single-Target Routing

Example:

```text
"Terraform plan failed"
        ↓
      Router
        ↓
Terraform Specialist
```

Good when domain is obvious and one specialist enough.

---

# PART 3 — Multi-Target Routing

Incident:

```text
"Deployment failed after network change"
```

Router may choose:

```text
Pipeline + Terraform + AKS
```

Output:

```python
{"targets": ["pipeline", "terraform", "aks"]}
```

Application validates target names against allowlist.

---

# PART 4 — Parallel Fan-Out

```text
                Router
        ┌─────────┼─────────┐
        ↓         ↓         ↓
   Pipeline   Terraform     AKS
        ↓         ↓         ↓
        └─────────┼─────────┘
                  ↓
                Merge
```

Parallelism reduces wall-clock time when branches do not depend on each other.

---

# PART 5 — When NOT to Parallelize

If Agent B needs Agent A result:

```text
Pipeline confirms terraform_apply stage
                ↓
Terraform specialist checks exact change window
```

then sequential dependency may be better.

Parallel speculative work can waste cost.

---

# PART 6 — Fan-In Merge Contract

Each agent returns same outer structure:

```python
{
  "agent": "aks",
  "status": "SUCCESS",
  "evidence": [...],
  "gaps": [...]
}
```

Merge node:

```text
collect all outputs
→ validate schemas
→ deduplicate evidence IDs
→ record failed branches
→ continue only if minimum evidence policy satisfied
```

---

# PART 7 — Partial Failure

Suppose:

```text
Pipeline = SUCCESS
Terraform = SUCCESS
AKS = TIMEOUT
```

Wrong:

```text
Assume AKS is healthy.
```

Correct:

```text
AKS evidence unavailable.
```

Timeout = missing evidence, not negative evidence.

---

# PART 8 — Router Confidence

Do not blindly use model confidence.

Safer route policy can combine:

```text
keyword/rule hints
known incident stage
tool availability
model classification
fallback broad read-only triage
```

For high-risk tasks, deterministic routing may be preferable.

---

# PART 9 — DevOps Example

Input:

```text
Pods fail after Terraform apply and deployment job is red.
```

Router output:

```python
{
  "targets": ["pipeline", "terraform", "aks"],
  "reason_codes": ["pipeline_failure", "iac_change", "runtime_connectivity"]
}
```

Each specialist only gets relevant fields.

---

# PART 10 — Cost Controls

Parallel agents can multiply cost.

Track:

```text
agents_selected
agents_completed
model_calls
wall_clock_ms
aggregate_tokens
useful_findings_count
```

A route that invokes 5 agents and yields one useful fact is inefficient.

---

# PART 11 — Common Mistakes

- routing to every agent always
- no target allowlist
- parallel branches modifying same state unsafely
- no merge schema
- treating timeout as proof
- duplicate evidence appended repeatedly
- no branch-level tracing

---

# PART 12 — Interview Q&A

### Q1. Router vs supervisor?
Router performs bounded dispatch; supervisor coordinates ongoing multi-step delegation.

### Q2. When is parallel execution appropriate?
When tasks are independent, side-effect safe and results can be merged deterministically.

### Q3. How handle one failed parallel agent?
Record explicit failure/missing evidence and apply a minimum-evidence policy rather than guessing.

### Q4. What is fan-in?
The merge stage that collects and normalizes results from parallel branches.

---

# PART 13 — Revision

```text
Router = classify/dispatch
Parallel = independent work
Fan-in = validate/merge
Timeout = missing evidence
More branches = more cost
```

---

# PART 14 — Homework

Create routing rules for:
1. pipeline syntax failure
2. Terraform apply failure
3. AKS CrashLoopBackOff
4. unknown deployment failure

Specify single or multi-agent route for each.

---

# 🔁 Next Lesson Kyu?

Router dispatches tasks, but sometimes one specialist should **take control of the interaction/state**. Next lesson = Handoffs.
