# 🚩 Jai Bajrangbali!

# Lesson 07 — Scalability, Queues & Backpressure

> **Agent workloads are often I/O-bound, bursty and dependency-limited. Scaling pods faster than downstream models/tools can serve requests can make the system worse.**

---

# 🎯 Lesson Goal

You will learn:

- horizontal scaling for APIs and workers
- queue-based load leveling
- backpressure
- concurrency budgets
- model/tool rate limits
- retry storms
- fair scheduling
- tenant quotas
- load shedding
- capacity planning

---

# PART 1 — English Definition

**Backpressure is a control mechanism that prevents upstream producers from overwhelming downstream components when the system cannot safely process work at the incoming rate.**

---

# PART 2 — Why Agent Load Is Different

One user request may trigger:

```text
1 API request
3 specialist agents
6 tool calls
2 RAG queries
1–3 model calls
1 approval wait
```

So:

```text
User QPS != Dependency QPS
```

You must estimate fan-out amplification.

---

# PART 3 — Queue Pattern

```text
API
 ↓ enqueue
Queue
 ↓
Worker Pool
 ↓
Agent Workflow
```

Benefits:

```text
smooth bursts
independent API/worker scaling
retry control
priority
visibility into backlog
```

---

# PART 4 — Queue Does Not Solve Everything

If workers scale without limit:

```text
queue grows
 ↓
autoscaler creates workers
 ↓
all workers hit model rate limit
 ↓
429s
 ↓
retries
 ↓
retry storm
```

Therefore scaling must respect downstream capacity.

---

# PART 5 — Concurrency Budget

Define per dependency:

```text
model max concurrent requests
tool API rate limit
vector/search QPS
MCP server concurrency
DB connection pool
```

Then calculate safe worker concurrency.

---

# PART 6 — Backpressure Controls

Possible controls:

```text
bounded queue
max active workflows
semaphore per model/tool
tenant quota
request admission control
priority queues
circuit breaker
load shedding
```

---

# PART 7 — Priority

Not every workload is equal:

```text
P1 production outage
P2 deployment investigation
routine documentation query
background ingestion
```

Separate queues or priority classes may be appropriate.

Be careful: starvation of low-priority jobs must be considered.

---

# PART 8 — Retry Storms

Unsafe:

```text
100 workers × 3 retries immediately
```

Safer:

```text
bounded retries
exponential backoff
jitter
retry budget
circuit breaker
```

Only retry errors likely to be transient.

---

# PART 9 — Idempotency

Retrying read tool usually lower risk.

Retrying write tool can duplicate side effects.

Write operation needs:

```text
idempotency key
operation status check
approval binding
exact target/version
```

---

# PART 10 — Tenant Fairness

One team should not consume all model quota.

Potential controls:

```text
per-team concurrency
per-team token budget
per-team queue
rate limits
cost allocation tags
```

---

# PART 11 — Autoscaling Signals

For worker:

```text
queue length
oldest message age
active workflow count
processing latency
```

For API:

```text
request rate
CPU/memory
response latency
```

For model gateway:

```text
requests/sec
tokens/sec
429 rate
backend latency
```

---

# PART 12 — Load Shedding

When system is overloaded, explicit rejection can be safer than indefinite queueing.

Example:

```text
status=BUSY
retry_after=60
request_id=...
```

For critical incidents, reserve capacity.

---

# PART 13 — Capacity Exercise

Suppose:

```text
20 incidents/minute
3 model calls/incident
average 4 seconds/model call
safe model concurrency = 10
```

Approx required model service time:

```text
60 calls/minute × 4 sec = 240 model-seconds/minute
```

With concurrency 10, theoretical capacity ~150 calls/minute at 4 sec average, before overhead/rate limits. This gives headroom but must be validated under real load.

---

# PART 14 — Observability

Monitor:

```text
queue depth
oldest job age
job throughput
worker utilization
429/throttle rate
retry rate
circuit-open time
per-tenant usage
abandoned/cancelled jobs
```

---

# PART 15 — Common Mistakes

- scaling only on CPU
- infinite queue
- infinite retries
- no concurrency limit on model
- no per-tenant quota
- high-priority incidents share capacity with bulk ingestion
- retry write after timeout without status check

---

# PART 16 — Interview Q&A

### Q1. Why use a queue for agent workflows?
To decouple request arrival from long-running processing and provide buffering, retry, priority and scaling control.

### Q2. What is backpressure?
A mechanism that limits upstream work when downstream capacity is constrained.

### Q3. Why can autoscaling make a rate-limit problem worse?
More workers generate more concurrent dependency calls, increasing throttling and retries.

---

# 🧠 Revision

```text
Scale safely =
Queue + Concurrency Budget + Backpressure + Retry Policy + Quotas
```

---

# 📝 Homework

Define safe concurrency for:

```text
LLM
GitHub API
AKS API
vector search
state DB
```

Then design worker scaling around the smallest bottleneck.

---

# 🔁 Next Lesson Kyu?

Scale handles normal demand. Next we design for **component, zone and regional failure**.
