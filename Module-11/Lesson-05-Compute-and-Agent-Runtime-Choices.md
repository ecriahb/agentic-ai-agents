# 🚩 Jai Bajrangbali!

# Lesson 05 — Compute & Agent Runtime Choices

> **Choose runtime based on workload behavior, not because one platform is fashionable.**

---

# 🎯 Lesson Goal

You will learn:

- App Service vs Container Apps vs AKS mental models
- synchronous API vs worker runtime
- long-running stateful agent execution
- autoscaling signals
- cold starts and concurrency
- GPU/model-hosting separation
- container hardening
- when AKS is justified

---

# PART 1 — English Definition

**Runtime architecture is the choice of compute platform, process model, scaling model and deployment boundary used to execute the AI application's APIs, workers and agent workflows.**

---

# PART 2 — Start from Workload Shape

Ask:

```text
Is request short-lived or long-running?
Is runtime stateless between steps?
Does it need custom networking?
Does it need background workers?
Does it need scale-to-zero?
Does it need Kubernetes-native controls?
Does it require GPUs?
How many independent services exist?
```

Then choose platform.

---

# PART 3 — App Service Mental Model

Good fit when:

```text
web/API centric
standard deployment
managed platform preferred
moderate customization
simple autoscaling
```

Potential pattern:

```text
UI/API on App Service
 ↓
queue
 ↓
agent worker elsewhere
```

Do not force long-running workflow execution into a normal request thread if it exceeds request semantics.

---

# PART 4 — Container Apps Mental Model

Useful when:

```text
containerized microservices
managed scaling
event-driven workers
less Kubernetes operational overhead
```

Evaluate networking, persistence, ingress and scaling features against enterprise requirements.

---

# PART 5 — AKS Mental Model

AKS is useful when you need:

```text
custom Kubernetes scheduling
many services/workers
network policy
sidecars/service mesh patterns
fine-grained pod identity
custom autoscaling
specialized node pools
strong platform standardization around Kubernetes
```

Cost:

```text
cluster operations
upgrades
capacity planning
networking
policy
observability
security hardening
```

Use AKS because requirements justify it, not because the team already knows Kubernetes.

---

# PART 6 — API and Worker Separation

Recommended for long-running investigation:

```text
Agent API
  ↓ submit job
Queue / Durable Workflow
  ↓
Agent Worker
  ↓
Persistent State
```

Benefits:

```text
API latency independent of investigation time
worker retries isolated
horizontal scaling
backpressure
pause/resume support
```

---

# PART 7 — Pod/Process Roles

Avoid one pod doing everything.

Possible roles:

```text
api
workflow-worker
rag-ingestion-worker
tool-gateway
mcp-adapter
eval-runner
scheduled-maintenance
```

Each role gets separate identity and resource limits.

---

# PART 8 — Autoscaling Signals

Bad signal:

```text
CPU only
```

Agent systems may be I/O-bound waiting on models/tools.

Useful signals:

```text
queue depth
active workflow count
request rate
pending tool calls
model rate-limit pressure
CPU/memory
latency
```

Scale dependencies and quotas together.

---

# PART 9 — Resource Limits

Container limits protect shared runtime:

```text
CPU requests/limits
memory requests/limits
ephemeral storage
max concurrency
workflow deadline
```

Unbounded prompts or huge retrieved contexts can create memory/cost pressure even when CPU is low.

---

# PART 10 — Model Hosting Separation

Do not assume agent runtime and model runtime belong together.

```text
Agent Runtime
     ↓ API
Model Endpoint / Gateway
```

Benefits:

```text
independent scaling
model lifecycle separation
specialized GPU infrastructure
central governance
```

Local Ollama remains excellent for learning/dev; production architecture may use approved enterprise endpoints.

---

# PART 11 — Availability Zones

For production compute:

```text
multiple instances
zone-aware placement where supported
PDB/availability strategy
anti-affinity when useful
health probes
rolling updates
```

A single replica agent API is not production HA.

---

# PART 12 — Health Checks

Separate:

```text
liveness: process alive?
readiness: can serve new work?
dependency health: model/search/tool available?
```

Do not restart healthy process just because one external dependency is temporarily unavailable.

---

# PART 13 — Container Security

```text
minimal base image
non-root user
read-only filesystem where practical
pinned dependencies
image scanning
signed/provenance-aware artifacts
no secrets baked into image
network policy
resource limits
```

---

# PART 14 — Runtime Decision Matrix

```text
Simple API                    → App Service may fit
Event-driven containers      → Container Apps may fit
Complex Kubernetes platform  → AKS may fit
GPU model serving            → separate specialized model runtime
```

The answer can be hybrid.

---

# PART 15 — Common Mistakes

- choosing AKS without operational need
- one pod has API + ingestion + tools + writes
- CPU-only autoscaling
- no queue for long jobs
- health probe calls expensive model
- no resource limits
- runtime identity has subscription Contributor

---

# PART 16 — Interview Q&A

### Q1. When would you choose AKS for an agent platform?
When Kubernetes-specific requirements such as service decomposition, custom networking, pod identity, specialized scheduling, policy and worker orchestration justify the additional operations burden.

### Q2. Why separate API and workers?
It isolates user-facing latency from long-running investigation and enables independent retry/scaling/backpressure.

### Q3. Should the model run in the same cluster?
Not necessarily. Model runtime has different lifecycle, hardware, scaling and governance needs.

---

# 🧠 Revision

```text
Compute choice follows workload shape.
Long-running agent → async worker + durable state.
```

---

# 📝 Homework

Compare App Service, Container Apps and AKS for the DevOps AI Assistant using:

```text
operations
networking
scaling
state
security
cost
team skill
```

---

# 🔁 Next Lesson Kyu?

Runtime is chosen. Next we design **where state, evidence and knowledge live** without mixing their trust and lifecycle requirements.
