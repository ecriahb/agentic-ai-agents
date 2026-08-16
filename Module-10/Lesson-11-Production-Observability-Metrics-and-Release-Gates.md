# 🚩 Jai Bajrangbali!

# Lesson 11 — Production Observability, Metrics & Release Gates

> **Agent production-ready tab hota hai jab behavior measurable ho, failures traceable hon aur release policy objective gates par based ho.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- security/quality observability
- per-stage traces
- agent-specific production metrics
- release gates
- canary/shadow evaluation
- alerting and incident response for agents

---

# PART 1 — Observe the Whole Trajectory

Capture:
```text
request_id / incident_id
user/identity class
model/version
prompt/version
route decisions
agent/subagent selected
tool calls + normalized args
tool statuses
retrieved source IDs
policy decisions
approval decisions
iterations/retries
validation results
latency/token/cost
final status
```

Redact secrets before telemetry.

---

# PART 2 — Security Metrics

```text
policy_violation_rate
unauthorized_tool_attempt_rate
prompt_injection_block/escalation_rate
secret_leak_rate
unknown_citation_rate
approval_bypass_rate
cross-scope_access_attempts
malformed_tool_result_rate
```

Target for serious safety violations is usually zero or near-zero with immediate investigation.

---

# PART 3 — Quality Metrics

```text
task_success_rate
grounded_claim_rate
citation_validity
abstention_accuracy
routing_accuracy
useful_evidence_rate
conflict_resolution_rate
human_escalation_rate
```

Do not optimize quality metrics by weakening safety controls.

---

# PART 4 — Efficiency Metrics

```text
p50/p95 latency
tokens/request
tool calls/request
agent hops/request
parallel workers
cost/request
retry rate
no-progress termination rate
```

Unbounded consumption is both availability and cost risk.

---

# PART 5 — Release Gate Example

Before releasing model/prompt/tool change:
```text
Security suite pass = 100%
Forbidden tool violations = 0
Secret leakage = 0
Citation validity >= 99%
Normal task success >= baseline - tolerance
p95 latency <= threshold
Cost <= threshold
No critical red-team finding open
```

Exact thresholds depend on environment and risk.

---

# PART 6 — Version Everything

Record:
```text
model version
prompt hash/version
policy version
tool schema version
MCP server version
retriever/index version
eval dataset version
code commit SHA
```

Otherwise regressions cannot be reproduced.

---

# PART 7 — Shadow / Canary

Safer rollout:
```text
new agent version
 ↓
shadow traffic / offline replay
 ↓
eval comparison
 ↓
small canary
 ↓
monitor safety + quality
 ↓
gradual rollout
```

For write-capable systems, start read-only/shadow where possible.

---

# PART 8 — Alerts

Alert on:
```text
forbidden tool request spike
unexpected MCP server/tool
policy service failures
secret detector hits
loop-budget exhaustion
approval anomalies
citation-validation failures
cross-tenant access attempts
```

Alert should include trace ID, not raw secret payload.

---

# PART 9 — Rollback

Rollback target may be:
```text
model
prompt
policy
tool exposure
MCP server
index version
agent graph
```

Keep known-good configuration available.

---

# PART 10 — Common Mistakes

- logging only final answer
- no prompt/model version
- no security KPIs
- release based on demo screenshots
- averages hide critical failures
- production experiments with write permissions
- no rollback of vector index/policy

---

# PART 11 — Interview Q&A

### Q1. What should you trace in an agent?
Routing, tool calls, retrieval sources, policy/approval decisions, state transitions, validation and final outcome, with sensitive data redacted.

### Q2. What is a release gate?
An objective set of quality/security thresholds that must pass before a new agent version is promoted.

### Q3. Why version eval dataset?
So score changes can be attributed to system changes rather than moving test criteria.

---

# PART 12 — Revision

```text
Trace = what happened
Metric = how often/how well
Alert = when behavior crosses risk threshold
Eval = controlled test
Release gate = promotion decision
Rollback = recovery path
```

---

# PART 13 — Homework

Define a release scorecard for your DevOps AI Assistant with 5 security, 5 quality and 5 efficiency metrics plus pass/fail thresholds.

---

# 🔁 Next Lesson Kyu?

Ab threat model, controls, evals, red-team aur metrics sab ready hain. Final lesson me inko ek executable **Secure DevOps Agent Evaluation Harness** me combine karenge.
