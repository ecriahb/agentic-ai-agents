# 🚩 Jai Bajrangbali!

# Lesson 11 — CI/CD, Operations & Incident Runbooks

> **The final assistant needs its own deployment pipeline and its own operational runbooks; an AI system can itself become the production incident.**

---

# 🎯 Lesson Goal

You will define:

- build/release pipeline
- environment promotion
- eval/security gates
- rollback strategy
- state-schema compatibility
- operational runbooks
- dependency outage handling
- model/RAG/MCP incident playbooks
- on-call signals
- post-incident learning

---

# PART 1 — Final CI Pipeline

```text
PR
 ↓
Python/unit tests
 ↓
Tool contract tests
 ↓
RAG retrieval tests
 ↓
Graph trajectory tests
 ↓
Security/red-team tests
 ↓
IaC/security scans
 ↓
Build artifact
 ↓
Dev deploy
 ↓
Integration eval
 ↓
Stage load/failure tests
 ↓
Prod approval
 ↓
Canary
 ↓
Full release
```

---

# PART 2 — Version Bundle

Release metadata:

```json
{
  "app_version": "1.0.0",
  "graph_version": "v5",
  "prompt_version": "rca-v7",
  "model_config": "approved-model-a",
  "policy_version": "p4",
  "tool_contract_version": "t3",
  "index_version": "kb-2026-08",
  "eval_dataset": "eval-v6"
}
```

This allows exact reproduction.

---

# PART 3 — Protected Production Release

Production deploy requires:

```text
passing mandatory gates
approved change
immutable artifact digest
prod deployment identity
protected environment
```

No personal credentials in pipeline.

---

# PART 4 — Canary Signals

During canary watch:

```text
HTTP errors
workflow completion
validation failures
unexpected agent routes
tool denials
prompt-injection detections
RAG no-context rate
model cost/latency
```

Rollback if trust metrics regress even when infrastructure looks healthy.

---

# PART 5 — Rollback Strategy

If new version fails:

```text
stop new traffic to version
route new jobs to previous version
preserve running workflow compatibility
rollback prompt/policy/model config bundle
validate health/evals
```

Do not blindly migrate old checkpoints into incompatible graph code.

---

# PART 6 — Runbook: Model Outage

```text
1 detect elevated timeout/error rate
2 open circuit/bound retries
3 use evaluated fallback if policy permits
4 otherwise queue/degrade
5 communicate model dependency state
6 do not switch to unapproved endpoint
7 restore and run smoke eval
```

---

# PART 7 — Runbook: RAG/Search Outage

```text
1 mark REFERENCE_CONTEXT_UNAVAILABLE
2 continue current-evidence collection
3 produce evidence-only partial response if allowed
4 do not invent runbook guidance
5 restore search
6 validate index freshness
```

---

# PART 8 — Runbook: MCP/Tool Outage

```text
1 identify affected capability
2 preserve TOOL_ERROR evidence state
3 retry only transient failure within budget
4 do not replace with hallucinated observation
5 finish partial investigation or queue
```

---

# PART 9 — Runbook: State Store Failure

This is high severity for resumable workflows.

```text
1 stop accepting workflows requiring durable state if unsafe
2 protect against duplicate operations
3 recover store/failover
4 verify checkpoint integrity
5 resume eligible threads
6 refresh volatile evidence
```

---

# PART 10 — Runbook: Security Signal

Example:

```text
unknown MCP server attempts spike
```

Response:

```text
block endpoint
preserve audit evidence
identify caller/version
review recent releases
run security eval suite
rotate affected credentials if needed
```

---

# PART 11 — Runbook: Bad RCA Regression

```text
1 identify model/prompt/index/tool change
2 capture failing case
3 add permanent eval
4 block rollout
5 rollback affected bundle
6 fix
7 rerun full suite
```

---

# PART 12 — Operations Dashboard

```text
Availability
Latency
Queue
State persistence
Model health
RAG health
MCP/tool health
Validation
Security/policy
Approval/write actions
Cost
```

---

# PART 13 — Post-Incident Review

For AI-platform incidents ask:

```text
Was failure infra, model, retrieval, tool, policy or graph?
Did fail-closed behavior work?
Was user impact clear?
Was evidence preserved?
Did alerting detect it?
Which regression test should be added?
```

---

# PART 14 — Common Mistakes

- no rollback for prompt/model config
- same pipeline identity as runtime identity
- no runbook for model outage
- state-store incident treated as ordinary cache issue
- canary checks only HTTP health
- security regression not release-blocking

---

# PART 15 — Interview Q&A

### Q1. What is special about CI/CD for agents?
Behavior depends on prompts, models, tools, retrieval and policies as well as code, so all must be versioned/evaluated together.

### Q2. What should happen during RAG outage?
Expose the reference-context gap and avoid fabricating knowledge; current evidence may still support a partial response.

### Q3. Why is state-store outage critical?
Long-running workflows, approvals and idempotency depend on durable state for correct recovery.

---

# 🧠 Revision

```text
Operate the agent like a production service
AND like a decision system.
```

---

# 📝 Homework

Write one-page runbooks for model outage, MCP outage and state-store outage.

---

# 🔁 Next Lesson Kyu?

Engineering is complete. Final lesson turns the project into a **demo, interview story and portfolio artifact**.
