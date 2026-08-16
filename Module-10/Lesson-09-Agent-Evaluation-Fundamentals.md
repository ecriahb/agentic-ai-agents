# 🚩 Jai Bajrangbali!

# Lesson 09 — Agent Evaluation Fundamentals

> **A good final answer can hide a bad trajectory. Agent evaluation must measure what the system answered, what it retrieved, which tools it called, how it routed, and whether policy boundaries held.**

---

# 🎯 Lesson Goal

You will understand:

- evals vs tests
- datasets and ground truth
- final-response evaluation
- single-step evaluation
- trajectory evaluation
- deterministic vs LLM-as-judge evaluators
- RAG/tool/policy metrics
- offline vs online evaluation
- regression testing
- release thresholds

---

# PART 1 — English Definition

**Agent evaluation is the systematic measurement of an agent's outputs, intermediate decisions, tool use, retrieval, trajectories and safety behavior against expected examples or rubrics.**

---

# PART 2 — Why Unit Tests Are Not Enough

Unit test can verify:

```text
authorize("read") returns ALLOW
```

But real agent may still:

```text
choose wrong tool
call unnecessary tools
retrieve wrong runbook
loop too much
produce unsupported RCA
```

Evals measure system behavior.

---

# PART 3 — Evaluation Layers

```text
Component
- prompt/model step
- retrieval
- tool selection

Trajectory
- route and sequence

Final Output
- correctness/grounding

Safety
- policy/security invariants

Operational
- latency/cost/reliability
```

---

# PART 4 — Golden Dataset

Start manually curated.

Example:

```json
{
  "input": "AKS deployment failed after Terraform network change",
  "expected_agents": ["pipeline", "terraform", "aks"],
  "expected_evidence": ["E1", "E2", "E3"],
  "expected_references": ["aks-networking", "terraform-networking"],
  "expected_status": "RCA_VALIDATED"
}
```

Quality of eval dataset matters more than number of examples at first.

---

# PART 5 — Final Response Evaluation

Evaluate:

```text
root-cause correctness
groundedness
completeness
relevance
uncertainty honesty
citation correctness
```

Use deterministic checks where possible.

Example:

```text
No unknown citation IDs.
```

---

# PART 6 — Single-Step Evaluation

Given incident:

```text
Docker build failed before Terraform stage
```

Expected first decision:

```text
pipeline specialist
```

Unexpected:

```text
AKS + Terraform + networking tools
```

Single-step eval isolates routing quality.

---

# PART 7 — Trajectory Evaluation

Trajectory:

```text
validate
→ pipeline
→ terraform
→ aks
→ RAG
→ synthesize
→ validate
```

Expected can be evaluated as:

```text
strict order
unordered set
subset/no-extra-tools
superset/minimum-required
custom score
```

Choose based on workflow flexibility.

---

# PART 8 — Tool Argument Evaluation

Correct tool name is not enough.

```text
get_aks_status(cluster_name="prod-aks") ✅
get_aks_status(cluster_name="random-prod") ❌
```

Evaluate both tool selection and arguments.

---

# PART 9 — Retrieval Evaluation

Measure independently:

```text
Hit@K
Recall@K
MRR intuition
unauthorized retrieval = 0
stale source retrieval
```

If retrieval fails, generation score alone hides root cause.

---

# PART 10 — Policy Evaluation

Critical deterministic assertions:

```text
unknown tool executed = 0
write without approval = 0
cross-tenant retrieval = 0
fake citation accepted = 0
loop beyond budget = 0
```

These are pass/fail, not subjective 1–5 scores.

---

# PART 11 — LLM-as-Judge

Useful for nuanced criteria:

```text
Is RCA explanation coherent?
Is recommendation appropriately scoped?
Does answer communicate uncertainty clearly?
```

Risks:

```text
judge variability
bias
cost
judge model changes
```

Use explicit rubric and combine with deterministic checks.

---

# PART 12 — Deterministic Evaluators

Examples:

```python
assert all(citation in allowed for citation in cited)
assert set(actual_tools).issubset(allowed_tools)
assert iterations <= MAX_ITERATIONS
```

Fast, cheap and excellent for security/contracts.

---

# PART 13 — Offline Evaluation

Before release:

```text
fixed dataset
fixed configuration snapshot
compare candidate vs baseline
```

Store:

```text
model version
prompt version
policy version
index version
```

---

# PART 14 — Online Evaluation

Production sampling can monitor:

```text
validation failures
user feedback
abstention rate
policy denials
trajectory anomalies
cost/latency
```

Do not expose sensitive production data to an unapproved judge.

---

# PART 15 — Regression Testing

Every fixed bug becomes case.

Example bug:

```text
Agent called AKS tool for simple Python syntax question.
```

Add dataset example ensuring no DevOps tool call for out-of-scope query.

---

# PART 16 — Eval Scorecard

```text
Routing accuracy
Retrieval Hit@K
Groundedness
Citation validity
Abstention correctness
Security invariants
P95 latency
Cost/request
```

Avoid single magic score.

---

# PART 17 — Release Threshold

Example:

```text
citation validity = 100% critical set
unsafe write = 0
routing accuracy >= target
RAG hit@3 >= target
p95 latency <= SLO
cost <= budget
```

Thresholds come from product risk/business needs.

---

# PART 18 — Failure Analysis

If overall RCA score falls:

```text
Was routing wrong?
Retrieval wrong?
Tool failed?
Prompt ignored evidence?
Parser failed?
Policy blocked expected step?
```

Component evals localize regression.

---

# PART 19 — Common Mistakes

- only final answer tested
- no tool arguments checked
- security averaged into quality score
- eval dataset generated entirely by model with no review
- no version metadata
- production judge sees sensitive data without policy
- no regression cases from incidents

---

# PART 20 — Interview Q&A

### Q1. What is trajectory evaluation?
Evaluating the sequence/set of agent decisions and tool calls taken to reach the answer.

### Q2. Deterministic vs LLM judge?
Deterministic evaluators are ideal for exact contracts/security; LLM judges help with nuanced qualitative behavior but are probabilistic.

### Q3. Why evaluate retrieval separately?
Because bad context can cause bad answers even when generation behaves correctly.

### Q4. How do evals help releases?
They provide repeatable evidence that prompt/model/tool/index changes do not regress required behavior.

---

# 🧠 Revision

```text
Agent Eval =
Final Answer
+ Trajectory
+ Tools/Args
+ Retrieval
+ Policy
+ Operational Metrics
```

---

# 📝 Homework

Create 10 evaluation examples and define expected trajectory plus final-state assertions for each.

---

# 🔁 Next Lesson Kyu?

Normal evals define correct behavior. Next we intentionally attack the system through **red teaming and adversarial test design**.
