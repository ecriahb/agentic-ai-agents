# 🚩 Jai Bajrangbali!

# Lesson 04 — Nodes, Edges & Conditional Routing

> **Nodes work karte hain; edges decide karte hain next kya chalega. Safe agent design me routing explicit aur testable honi chahiye.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- node kya hota hai
- fixed edge kya hota hai
- conditional edge kya hota hai
- deterministic routing vs model-driven routing
- START and END ka role
- routing functions ko pure/testable kaise rakhein
- DevOps incident branching ka practical architecture

---

# PART 1 — English Definitions

A **node** is a function or executable step that reads graph state, performs work and returns state updates.

An **edge** defines which node executes next.

A **conditional edge** chooses the next node based on current state or routing logic.

---

# PART 2 — Simple Graph

```text
START
  ↓
validate_input
  ↓
collect_pipeline
  ↓
analyze
  ↓
END
```

Conceptual code:

```python
builder.add_edge(START, "validate_input")
builder.add_edge("validate_input", "collect_pipeline")
builder.add_edge("collect_pipeline", "analyze")
builder.add_edge("analyze", END)
```

---

# PART 3 — What Belongs in a Node?

Good node responsibilities:

```text
validate request
call one tool/service
normalize one evidence result
retrieve documents
run one model analysis
validate one output
```

Avoid giant node:

```text
validate + call 5 APIs + LLM + approval + execute remediation
```

Smaller nodes improve:

```text
observability
testing
retry control
failure isolation
```

---

# PART 4 — Conditional Routing

Example state:

```python
{
  "failure_stage": "terraform"
}
```

Router:

```python
def route_failure(state):
    if state["failure_stage"] == "terraform":
        return "collect_terraform"
    if state["failure_stage"] == "aks":
        return "collect_aks"
    return "collect_pipeline"
```

Graph:

```text
classify
   ↓
route_failure
 ├─ terraform → collect_terraform
 ├─ aks       → collect_aks
 └─ other     → collect_pipeline
```

---

# PART 5 — Deterministic Router First

Prefer deterministic logic when condition is known:

```text
evidence_count < minimum
iteration >= max_iterations
approval_status == rejected
validation_status == failed
```

Do not waste LLM call for simple policy logic.

Example:

```python
def evidence_gate(state):
    if state["iteration"] >= 4:
        return "insufficient_evidence"
    if len(state["evidence"]) < 3:
        return "collect_more"
    return "analyze"
```

---

# PART 6 — When Model-Assisted Routing Helps

Model may help when classification is semantic:

```text
Is this primarily networking, IAM, image pull, capacity or application failure?
```

But safer pattern:

```text
LLM returns structured category
      ↓
Schema validation
      ↓
Allowlisted category mapping
      ↓
Deterministic graph edge
```

Never let arbitrary model text become executable node name.

---

# PART 7 — Structured Routing Contract

Model output:

```json
{
  "category": "networking",
  "reason": "Evidence mentions subnet connectivity"
}
```

Host mapping:

```python
ROUTES = {
    "networking": "network_investigation",
    "terraform": "terraform_investigation",
    "pipeline": "pipeline_investigation",
}
```

Unknown category:

```text
→ safe_fallback
```

---

# PART 8 — Current Evidence vs Reference Routing

Suppose:

```text
Current evidence says Terraform Apply failed.
Runbook says NSG problems are common.
```

Routing should not convert runbook guidance into current fact.

Better:

```text
current evidence → choose investigation branch
reference docs → help within branch
```

This reuses Module 5 grounding.

---

# PART 9 — Route to END Explicitly

Every graph should have clear terminal conditions.

Examples:

```text
SUCCESS
INSUFFICIENT_EVIDENCE
VALIDATION_FAILED
REJECTED_BY_HUMAN
MAX_ITERATIONS_REACHED
```

Do not rely on accidental loop exhaustion.

---

# PART 10 — DevOps Graph Example

```text
START
 ↓
validate
 ↓
classify_failure
 ↓
┌───────────────┬────────────────┬─────────────┐
↓               ↓                ↓
pipeline       terraform        aks
↓               ↓                ↓
collect_log    collect_plan     collect_status
└───────────────┴───────┬────────┘
                        ↓
                  evidence_gate
                    │       │
                   weak    enough
                    │       ↓
               collect_more analyze
                    ↑       ↓
                    └──── validate
                              ↓
                             END
```

---

# PART 11 — Routing Tests

Router should be unit-testable without model/tool calls.

Test table:

```text
State                              Expected Route
iteration=5                        max_iterations
validation=failed                  safe_failure
approval=rejected                  end_rejected
evidence_count=0                   collect_more
evidence_count=3, quality=good     analyze
```

---

# PART 12 — Common Mistakes

- arbitrary LLM text as node name
- routing logic mixed with side effects
- no default/fallback route
- no END condition
- using reference docs as current facts
- huge nodes that cannot be retried safely
- business policy hidden inside prompt

---

# PART 13 — Interview Q&A

### Q1. What is the difference between a node and an edge?
A node performs work; an edge determines which step executes next.

### Q2. When should routing be deterministic?
Whenever the decision can be expressed reliably using trusted application state or policy.

### Q3. How should LLM-based routing be made safer?
Use structured outputs, validate against an allowlist and map categories to known nodes in host code.

### Q4. Why keep routing functions side-effect free?
They become easier to test, reason about and replay.

---

# PART 14 — Revision

```text
Node = work
Fixed edge = always next
Conditional edge = choose from known paths
Router = decision function
END = explicit terminal state
```

---

# PART 15 — Homework

Design routing for:

```text
ImagePullBackOff
Terraform Apply failure
AKS networking failure
Unknown failure
```

Use an allowlisted category map and define a safe unknown route.

---

# 🔁 Next Lesson Kyu?

Conditional routing one decision karta hai. Real agent repeatedly **observe → choose → act → observe** kar sakta hai. Next lesson me controlled agent loop aur planning samjhenge.
