# 🚩 Jai Bajrangbali!

# Lesson 09 — Observability & SRE for Agents

> **You cannot operate an agent by watching only CPU, memory and HTTP 500s. You must observe decisions, tool calls, evidence quality, model behavior, cost and business outcomes.**

---

# 🎯 Lesson Goal

You will learn:

- metrics, logs and traces for agent systems
- request/incident correlation
- graph/node/tool/model spans
- SLI/SLO design
- security and policy metrics
- RAG and evidence quality metrics
- alert design
- dashboards
- privacy/redaction in telemetry
- incident response for the AI platform itself

---

# PART 1 — English Definition

**Observability is the ability to understand a system's internal behavior from telemetry such as metrics, logs, traces and structured events.**

---

# PART 2 — Four Observability Layers

```text
Infrastructure
Application
Agent Workflow
Business/Trust Outcome
```

Infrastructure:

```text
CPU
memory
pods
network
DB
queue
```

Agent workflow:

```text
selected agent
tool calls
retrieval
model calls
policy decisions
approval pauses
validation failures
```

---

# PART 3 — Correlation ID

One incident should carry one stable correlation identifier across:

```text
API
queue
worker
graph nodes
MCP/tool calls
model calls
state writes
audit events
```

Example:

```text
incident_id=INC-1042
request_id=req-...
thread_id=...
```

This enables end-to-end troubleshooting.

---

# PART 4 — Trace Mental Model

```text
request
 ├─ validate
 ├─ route
 ├─ pipeline_specialist
 │   └─ get_pipeline_status
 ├─ terraform_specialist
 │   └─ get_terraform_changes
 ├─ retrieve_runbook
 ├─ synthesize_llm
 ├─ validate_citations
 └─ approval_gate
```

Each span records duration/status—not secret payloads by default.

---

# PART 5 — Golden Infrastructure/Application Metrics

```text
request rate
error rate
latency
resource saturation
queue depth
dependency availability
```

Still necessary, but not sufficient.

---

# PART 6 — Agent Metrics

```text
workflow completion rate
average nodes/run
tool calls/run
loop count
no-progress terminations
approval wait time
policy-denied calls
validation failures
unsupported citation rate
abstention rate
```

These tell whether the agent is behaving correctly.

---

# PART 7 — RAG Metrics

```text
retrieval latency
no-result rate
source freshness
ACL-filter rejection count
hit@k on eval dataset
citation support rate
context size
```

High LLM quality cannot compensate for poor retrieval.

---

# PART 8 — Model Metrics

```text
latency
input/output tokens
rate-limit rate
timeout rate
model version
fallback usage
cost
structured-output failure rate
```

Track by environment/team/use case.

---

# PART 9 — Tool Metrics

```text
tool name
call count
latency
error class
argument-validation failure
authorization denial
retry count
write proposal count
actual approved execution count
```

Never expose secrets in tool arguments telemetry.

---

# PART 10 — Security Metrics

From Module 10:

```text
prompt-injection detections
unknown tool proposals
secret redactions
policy denials
untrusted MCP attempts
cross-tenant access denials
approval bypass attempts
```

Alert on suspicious trends, not every harmless individual signal.

---

# PART 11 — SLI and SLO

Example SLI:

```text
percentage of eligible read-only investigations completed within 2 minutes
```

Example SLO:

```text
99% monthly
```

Trust SLO:

```text
100% production write executions have authorization + approval + audit event
```

Some security invariants should be zero-tolerance rather than average SLOs.

---

# PART 12 — Error Budget Thinking

If reliability SLO violated:

```text
pause risky feature rollout
prioritize reliability work
reduce model/tool changes
```

AI quality/eval regression can also block release independently of uptime.

---

# PART 13 — Alert Design

High-value alerts:

```text
queue age above threshold
state persistence errors
model failure rate spike
tool auth denial spike
citation validation failures spike
secret redaction spike
production approval audit mismatch
```

Avoid alerting on every LLM response difference.

---

# PART 14 — Dashboard

Suggested dashboard sections:

```text
Traffic & latency
Workflow success
Dependency health
RAG quality
Model usage/cost
Tool calls
Security/policy
Approval/write actions
```

---

# PART 15 — Telemetry Privacy

Do not log full prompts/evidence automatically.

Use:

```text
redaction
sampling
hash/reference IDs
role-based access to traces
retention limits
```

Tracing itself can become a sensitive data store.

---

# PART 16 — AI Platform Incident Example

Symptom:

```text
RCA latency suddenly doubles
```

Trace shows:

```text
API 50ms
RAG 100ms
Tool calls 300ms
LLM 8s → 16s
```

You immediately isolate model dependency instead of blaming AKS.

---

# PART 17 — Common Mistakes

- only infrastructure metrics
- full secrets/prompts logged
- no correlation IDs
- no tool-level spans
- no model version in telemetry
- no business/trust metrics
- alerting on noisy LLM text differences

---

# PART 18 — Interview Q&A

### Q1. What extra observability does an agent need?
Decision routes, state transitions, tool/retrieval/model calls, policy/approval events, validation outcomes and trust/quality metrics.

### Q2. Why is tracing useful?
It shows where latency/error/behavior occurred across a multi-stage workflow.

### Q3. Why can telemetry be a security risk?
Prompts, retrieved documents, tool arguments and model outputs may contain secrets or sensitive operational data.

---

# 🧠 Revision

```text
Observe not only "is it up?"
Observe "what did it decide, use, trust and execute?"
```

---

# 📝 Homework

Create 12 metrics for the DevOps AI Assistant:

```text
4 reliability
4 trust/security
2 cost
2 business outcome
```

---

# 🔁 Next Lesson Kyu?

We can operate the platform. Next we make sure **new versions enter production safely** through CI/CD, IaC and evaluation gates.
