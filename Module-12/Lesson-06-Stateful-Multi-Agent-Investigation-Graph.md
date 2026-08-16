# 🚩 Jai Bajrangbali!

# Lesson 06 — Stateful Multi-Agent Investigation Graph

> **The final assistant coordinates specialists through explicit state and deterministic routing; it does not rely on hidden conversational memory to remember what happened.**

---

# 🎯 Lesson Goal

You will design:

- supervisor state
- specialist fan-out/fan-in
- bounded loops
- evidence reducers
- conflict/gap detection
- retry/no-progress rules
- checkpointing
- human-interrupt branch
- deterministic termination

---

# PART 1 — Final State

```python
class IncidentState(TypedDict):
    incident_id: str
    incident: str
    environment: str
    cluster_name: str
    selected_agents: list[str]
    agent_results: list[dict]
    evidence: list[dict]
    references: list[dict]
    conflicts: list[dict]
    gaps: list[str]
    iteration: int
    max_iterations: int
    rca: str
    validation_status: str
    proposed_action: dict
    approval_decision: str
    final_status: str
```

---

# PART 2 — Graph

```text
START
 ↓
validate_input
 ↓
route_incident
 ↓
run_specialists (parallel where safe)
 ↓
merge_evidence
 ↓
detect_conflicts_and_gaps
 ↓
enough evidence?
 ├─ NO → bounded planner loop
 └─ YES
      ↓
 retrieve_reference
      ↓
 synthesize_rca
      ↓
 validate_rca
      ↓
 propose_action
      ↓
 approval_gate
      ↓
 END
```

---

# PART 3 — Specialist Boundaries

```text
Pipeline Specialist
→ E1 pipeline status

Terraform Specialist
→ E2 IaC/network change evidence

AKS Specialist
→ E3 cluster/network health

Knowledge Specialist
→ R1/R2 references
```

Each specialist returns a structured result, not a long free-form chat.

---

# PART 4 — Parallelism

Safe parallel investigation:

```text
pipeline read
terraform read
AKS read
```

These operations are independent/read-only.

Unsafe parallelism:

```text
multiple remediation writes
```

Do not parallelize side effects casually.

---

# PART 5 — Evidence Reducer

Merge by stable evidence IDs and provenance.

Rules:

```text
same logical E2 retry → update/version, do not blindly duplicate
conflicting E2 claims → conflict state
TOOL_ERROR → preserve error
CURRENT_EVIDENCE → preserve timestamp/source
```

---

# PART 6 — Gap Detection

Required baseline:

```python
REQUIRED = {"E1", "E2", "E3"}
```

If missing:

```text
missing = REQUIRED - current_ids
```

Planner may request only the missing evidence.

---

# PART 7 — Bounded Loop

```text
iteration < max_iterations
no_progress_count < threshold
budget remaining
```

Otherwise:

```text
MAX_ITERATIONS_REACHED
or
NO_PROGRESS
```

Agent loops must always have a deterministic exit.

---

# PART 8 — Retry Policy

Node retry is based on error class:

```text
transient timeout → bounded retry
rate limit → backoff
invalid args → no retry
auth denied → no blind retry
```

Retry state must not duplicate already successful evidence.

---

# PART 9 — Checkpointing

Persist after meaningful transitions:

```text
input validated
specialist results collected
RCA generated
approval requested
```

If worker restarts, resume from durable state—not from model reconstruction.

---

# PART 10 — Human Interrupt

Before any high-risk write proposal:

```text
proposal
 ↓
policy says approval required
 ↓
interrupt/pause
 ↓
human decision
 ↓
resume exact thread
```

Approval payload binds:

```text
action
target
evidence IDs
version/request ID
```

---

# PART 11 — No Hidden Authority

Supervisor/model may propose:

```text
"call Terraform specialist"
```

Host validates agent/tool against allowlist.

Model never gets direct executor object with unrestricted capabilities.

---

# PART 12 — Conflict Example

Terraform specialist:

```text
E2: NSG rule removed
```

Another fresh source:

```text
E2b: rule currently present after rollback
```

Correct behavior:

```text
preserve both timestamps
mark conflict/change-over-time
refresh causal timeline
```

Not majority vote.

---

# PART 13 — State Freshness

After approval wait, refresh volatile facts:

```text
AKS health
pipeline status
resource state
```

Do not execute action based on stale 2-hour-old cluster state without revalidation.

---

# PART 14 — Common Mistakes

- chat history used as state DB
- infinite supervisor loop
- duplicate evidence on retry
- all specialists share every capability
- approval not bound to exact action
- checkpoint contains secrets
- conflict overwritten by “latest answer” without provenance

---

# PART 15 — Interview Q&A

### Q1. Why use a stateful graph instead of a simple chain?
Because investigation includes conditional routing, loops, parallel specialists, pause/resume, conflicts, retries and approval states.

### Q2. Why preserve tool errors in state?
So the workflow knows evidence is unavailable rather than interpreting absence as a negative fact.

### Q3. Why bound loops?
To prevent cost explosions, repeated tool calls and non-terminating workflows.

---

# 🧠 Revision

```text
StateGraph = State + Nodes + Edges + Policy + Termination
```

---

# 📝 Homework

Draw exact graph branches for `TOOL_ERROR`, `INSUFFICIENT_EVIDENCE`, `VALIDATION_FAILED`, and `APPROVAL_REQUIRED`.

---

# 🔁 Next Lesson Kyu?

Graph has evidence and references. Next we make sure the **RCA itself is grounded, valid and confidence-calibrated**.
