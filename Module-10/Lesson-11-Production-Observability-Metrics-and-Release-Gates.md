# 🚩 Jai Bajrangbali!

# Lesson 11 — Production Observability, Metrics & Release Gates

> **Security controls become operational only when their decisions are observable and unsafe regressions can block deployment.**

---

# 🎯 Lesson Goal

You will understand:

- production security telemetry
- quality vs trust metrics
- SLOs and invariants
- release scorecards
- canary monitoring
- model/prompt/tool drift
- policy observability
- incident triggers
- kill switches and rollback
- cost/unbounded-consumption metrics

---

# PART 1 — Three Metric Families

```text
Reliability
Quality
Security/Trust
```

Reliability:

```text
latency
availability
queue age
errors
```

Quality:

```text
groundedness
retrieval hit rate
routing accuracy
abstention correctness
```

Security:

```text
policy violations
secret leaks
unauthorized retrieval
approval bypass
unknown tools
```

Do not merge everything into one score.

---

# PART 2 — Security Invariants

Some metrics should be absolute:

```text
prod write without authorization = 0
prod write without approval = 0
cross-tenant retrieval = 0
secret exposure = 0
unknown tool execution = 0
```

One violation can block/rollback release.

---

# PART 3 — Agent Behavioral Metrics

```text
average tools/run
unexpected tool rate
loop-limit rate
no-progress rate
handoffs/run
conflict rate
abstention rate
validation failure rate
```

Large changes can reveal regression or attack.

---

# PART 4 — Prompt Injection Metrics

Possible signals:

```text
injection detector score distribution
policy-denied actions following untrusted content
unknown tool proposals
external-destination proposals
system-prompt extraction attempts
```

Avoid assuming detector score itself proves attack.

---

# PART 5 — RAG Security Metrics

```text
unauthorized candidate blocked
stale source retrieved
no-context rate
source version mismatch
secret-scan ingestion rejects
retrieval ACL denial
```

Correlate with user/team identity.

---

# PART 6 — MCP Metrics

```text
server connection attempts
unknown server denials
auth failures
tool discovery changes
malformed responses
write-tool requests
latency/rate-limit
server version
```

Sudden capability drift should trigger review.

---

# PART 7 — Multi-Agent Metrics

```text
agent routing accuracy
handoff loops
private-to-shared state promotion
conflicts
agent capability denials
specialist failure rate
```

Observe shared-state contamination indicators.

---

# PART 8 — Cost / Unbounded Consumption

Monitor:

```text
tokens/request
model calls/run
tool calls/run
retrieved chunks
workflow duration
parallelism
cost/team
```

Security controls:

```text
budgets
rate limits
max iterations
max context
queue/backpressure
```

---

# PART 9 — Release Scorecard

Example:

```text
Functional suite        PASS
RAG Hit@3               96%
Citation validity       100%
Trajectory subset       99%
Prompt injection suite  100% critical controls
Unknown tool execution  0
Secret leak             0
P95 latency             18s
Cost/request             within budget
```

---

# PART 10 — Critical vs Non-Critical Thresholds

Critical:

```text
security invariant violation
```

→ release blocked.

Non-critical quality metric:

```text
routing accuracy drops 0.5%
```

May trigger investigation depending threshold.

Define in advance.

---

# PART 11 — CI/CD Gate

```text
PR
 ↓
unit/contract
 ↓
eval suite
 ↓
security/red-team regression
 ↓
release scorecard
 ↓
critical failure?
 ├─ yes → BLOCK
 └─ no  → stage/canary
```

Manual approval should not override hidden security test failure without formal exception process.

---

# PART 12 — Canary Monitoring

New model/prompt/version gets limited traffic.

Watch:

```text
validation failures
unexpected tools
policy denials
latency
cost
RAG source mix
abstention
security signals
```

Compare candidate vs baseline.

---

# PART 13 — Drift Detection

Behavior can change because:

```text
model version changed
prompt changed
MCP server changed
RAG corpus/index changed
policy changed
tool schema changed
```

Record configuration versions in every trace/eval.

---

# PART 14 — Kill Switches

Plan how to quickly disable:

```text
write capabilities
specific MCP server
specific model deployment
specific agent
RAG source collection
high-risk workflow
```

Kill switch should not require editing prompt and waiting for model obedience.

---

# PART 15 — Security Incident Triggers

Examples:

```text
secret leak detected
unauthorized data access confirmed
unknown tool execution
approval bypass
sudden suspicious MCP traffic
repeated prompt-injection success
```

Response may include:

```text
disable capability
revoke identity
preserve traces
rollback release
rotate credentials
```

---

# PART 16 — Audit Record

For high-risk decisions store:

```text
request/incident ID
agent/model/prompt version
policy version
source IDs
tool calls
authorization result
approval result
final action/status
```

This supports investigation and compliance.

---

# PART 17 — Privacy-Aware Telemetry

Do not turn observability into data leak.

Use:

```text
redaction
sampling
access-controlled traces
shorter retention for sensitive payloads
IDs/hashes instead of full content
```

---

# PART 18 — Release Rollback

If canary shows unsafe behavior:

```text
stop candidate traffic
rollback code/prompt/model/policy bundle
block affected capability
rerun stable version
capture failing cases
add regression tests
```

---

# PART 19 — Common Mistakes

- uptime green = agent considered safe
- no security metrics
- one average score hides critical failure
- no configuration version in traces
- no kill switch
- canary observes only HTTP errors
- traces log secrets
- release exception process undefined

---

# PART 20 — Interview Q&A

### Q1. What security metrics should be zero-tolerance?
Unauthorized production writes, secret exposure, cross-tenant retrieval and unknown tool execution are common examples.

### Q2. Why track configuration versions in telemetry?
Agent behavior can change with model, prompt, tool, RAG or policy versions even when application code is unchanged.

### Q3. What is a release gate?
A rule that blocks promotion when required tests/metrics do not meet defined thresholds.

### Q4. Why need kill switches?
To disable risky capabilities immediately without depending on model behavior or full redeployment.

---

# 🧠 Revision

```text
Operate Trust =
Observe Controls
+ Measure Behavior
+ Block Unsafe Releases
+ Detect Drift
+ Roll Back Quickly
```

---

# 📝 Homework

Create a production dashboard with 15 metrics and identify 5 alerts plus 5 release-blocking invariants.

---

# 🔁 Next Lesson Kyu?

All security and evaluation components are ready. Final lesson combines them into the **Secure DevOps Agent Evaluation Harness**.
