# 🚩 Jai Bajrangbali!

# Lesson 06 — State, Evidence & Knowledge Data Layer

> **Conversation history, workflow checkpoints, evidence, audit records and RAG knowledge are different data products with different trust and retention rules.**

---

# 🎯 Lesson Goal

You will learn:

- workflow state vs evidence vs knowledge vs audit
- persistent checkpoint stores
- vector/search store lifecycle
- evidence immutability/provenance
- retention and TTL
- schema/versioning
- encryption and access control
- multi-tenant isolation
- stale data and freshness

---

# PART 1 — Core Data Classes

```text
Conversation Context
Workflow State
Evidence Store
Reference Knowledge
Audit Log
Configuration
```

Never collapse all six into chat history.

---

# PART 2 — Workflow State

Contains execution progress:

```text
incident_id
current_node
selected_agents
iteration
approval_status
pending_action
checkpoint_version
```

State supports pause/resume and recovery.

It is not automatically authoritative evidence.

---

# PART 3 — Evidence Store

Evidence records should preserve:

```text
evidence_id
source/tool
arguments
timestamp
payload or normalized claim
raw reference/hash
trust classification
collection status
```

Example:

```text
E2
source=get_terraform_changes
claim=NSG rule removed
timestamp=...
```

Final RCA claims point back to these records.

---

# PART 4 — Knowledge Store

Reference knowledge contains:

```text
runbooks
architecture docs
incident retrospectives
standards
approved procedures
```

It answers:

```text
What normally should happen?
```

Evidence answers:

```text
What happened in this incident?
```

Do not merge those meanings.

---

# PART 5 — Audit Store

Audit answers:

```text
Who requested?
Which agent/tool ran?
What policy decision occurred?
Who approved?
What version/model/prompt was used?
What final status occurred?
```

Audit logs must be protected from secret leakage.

---

# PART 6 — Persistence Design

Learning:

```text
InMemory state
```

Production:

```text
persistent checkpoint/state backend
```

Requirements:

```text
transaction semantics
concurrency
backup
retention
latency
availability
encryption
access control
```

---

# PART 7 — Idempotency and State Version

When a worker retries after crash:

```text
Did tool already run?
Did evidence already append?
Was approval already consumed?
```

Use:

```text
operation IDs
checkpoint versions
idempotency keys
stable evidence IDs
```

Avoid duplicate write or duplicate evidence.

---

# PART 8 — RAG Ingestion Lifecycle

```text
Source
 ↓
validate/classify
 ↓
extract/clean
 ↓
chunk
 ↓
metadata + ACL
 ↓
embed/index
 ↓
active version
```

When source deleted/updated, index must remove or supersede stale chunks.

---

# PART 9 — Data Freshness

Operational facts expire quickly.

```text
AKS health at 10:00
!=
AKS health at 11:00
```

Store:

```text
observed_at
valid_for/TTL if applicable
source freshness
```

On resume after long pause, refresh volatile evidence.

---

# PART 10 — Multi-Tenant Isolation

Possible partition keys:

```text
organization
team
environment
incident_id
classification
```

Enforce authorization at storage/query layer, not only in prompt.

---

# PART 11 — Encryption

Consider:

```text
encryption in transit
encryption at rest
customer-managed keys where required
field-level protection for highly sensitive data
backup encryption
```

But encryption does not solve overly broad application access.

---

# PART 12 — Retention

Different classes need different retention:

```text
conversation cache       short
workflow checkpoint      until workflow + recovery window
incident evidence        per audit/compliance policy
RAG documents            source lifecycle
security audit           longer controlled retention
```

Do not keep everything forever by default.

---

# PART 13 — Schema Evolution

State from version 1 may not match version 2 code.

Production strategies:

```text
version field
migration
backward-compatible readers
controlled draining before incompatible release
```

Long-running workflows make schema evolution especially important.

---

# PART 14 — Data Failure Modes

```text
checkpoint write fails
vector index stale
search unavailable
evidence record duplicate
audit sink unavailable
ACL metadata missing
source deleted but vector remains
```

Each needs explicit state and operational alerting.

---

# PART 15 — Common Mistakes

- model response stored as confirmed evidence
- no source timestamp
- all data in one database/table
- no tenant partition
- no deletion workflow for RAG
- checkpoints contain secrets
- audit logging is best-effort for privileged writes

---

# PART 16 — Interview Q&A

### Q1. Why separate workflow state and evidence?
Workflow state controls execution; evidence supports factual claims. Mixing them can turn generated/control data into false facts.

### Q2. Why does long-running agent state need versioning?
Because a workflow may resume after application code/schema changes.

### Q3. What is a stale vector risk?
Old or unauthorized source content can remain retrievable even after the authoritative document changed or was removed.

---

# 🧠 Revision

```text
State = where am I?
Evidence = what did we observe?
Knowledge = what guidance do we know?
Audit = who/what/when happened?
```

---

# 📝 Homework

Design separate schemas for:

```text
workflow_state
evidence_record
knowledge_chunk
audit_event
```

---

# 🔁 Next Lesson Kyu?

Data persistence is ready. Next we handle **load**: bursts, long-running work, rate limits, queues and backpressure.
