# 🚩 Jai Bajrangbali!

# Lesson 06 — RAG + MCP + Tool Routing

> **Module 8 ka graph earlier modules ko replace nahi karta; graph un capabilities ko correct state and routing ke saath coordinate karta hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- RAG node, MCP node and local tool node ka role
- current evidence vs reference knowledge routing
- capability discovery ko graph state me kaise represent karein
- retrieval kab use karein aur live tool kab
- tool/resource outputs normalize kaise karein
- missing capability and weak retrieval paths

---

# PART 1 — Course Connection

```text
Module 4 → retrieve similar knowledge
Module 5 → ground LLM with retrieved knowledge
Module 6 → orchestrate retriever/model/tools
Module 7 → standardize external capabilities via MCP
Module 8 → dynamically route between these using state
```

---

# PART 2 — Two Different Information Classes

### Reference Knowledge

```text
runbooks
design docs
past incidents
troubleshooting guides
```

Used for:

```text
what should usually be checked?
what does architecture require?
```

### Current Evidence

```text
current pipeline result
current Terraform plan/apply
current AKS status
current events/metrics
```

Used for:

```text
what actually happened now?
```

Never collapse these classes.

---

# PART 3 — Routing Mental Model

```text
Question / Incident
      ↓
Evidence Gap Classifier
 ┌────┼─────────┐
 │    │         │
Live  Reference Both
 │    │         │
MCP/  RAG      Parallel/Sequential
Tool  Retriever Collection
 └────┴─────────┘
       ↓
Normalize Sources
       ↓
Evidence Gate
```

---

# PART 4 — When to Use RAG

Use retrieval for questions like:

```text
What are expected AKS subnet requirements?
What is our rollback runbook?
What checks are recommended after NSG changes?
```

RAG does **not** prove:

```text
current prod NSG actually changed
current cluster is degraded
current pipeline failed
```

---

# PART 5 — When to Use Live Tools / MCP

Use tools for volatile current facts:

```text
get_pipeline_status
get_terraform_changes
get_aks_status
get_k8s_events
```

MCP connection:

```text
Graph Node
   ↓
MCP Client
   ↓
Approved MCP Server
   ↓
Structured Result
   ↓
Evidence Envelope
```

---

# PART 6 — Capability Discovery State

Module 7 discovery can feed state:

```python
{
  "available_tools": [
      "get_pipeline_status",
      "get_terraform_changes",
      "get_aks_status"
  ],
  "available_resources": [
      "runbook://aks/networking"
  ]
}
```

But critical rule:

```text
discovered != authorized
```

Policy still filters usable capabilities.

---

# PART 7 — Missing Capability Route

If planner asks for:

```text
get_node_network_trace
```

but server does not expose it:

```text
planner
 ↓
capability check
 ↓
missing
 ↓
record evidence gap
 ↓
try safe alternative / ask human / stop
```

Never fabricate result.

---

# PART 8 — Normalize Tool Outputs

Different MCP servers/tools may return different shapes.

Normalize to common envelope:

```python
{
  "id": "E3",
  "kind": "CURRENT_EVIDENCE",
  "source": "aks-mcp",
  "operation": "get_aks_status",
  "arguments": {"cluster_name": "prod-aks"},
  "observed_at": "...",
  "payload": {...},
  "error": None
}
```

Reference result:

```python
{
  "id": "R1",
  "kind": "REFERENCE",
  "source": "vector-kb",
  "document": "aks-networking.md",
  "payload": "..."
}
```

---

# PART 9 — Retrieval Quality Gate

Retriever always returning top-k does not mean results are useful.

Graph route:

```text
retrieve
 ↓
quality check
 ├─ weak → no_reference_context
 └─ good → attach_reference
```

Use evaluated thresholds, metadata eligibility and freshness rules.

---

# PART 10 — Parallel Collection

Some independent reads can run in parallel:

```text
                ┌→ pipeline status ─┐
collect_current ├→ terraform diff ──┼→ merge evidence
                └→ AKS status ──────┘
```

But parallel fan-out should be bounded.

Ask:

```text
Are calls independent?
Are they all necessary?
Do they hit rate limits?
Will partial failure be handled?
```

---

# PART 11 — Current Evidence Must Win on Current Facts

Conflict example:

```text
Runbook: cluster should normally be Healthy.
Live tool: cluster is Degraded.
```

For current incident:

```text
live observation → current fact
runbook → expected/reference state
```

Prompt/context labels must preserve this distinction.

---

# PART 12 — Tool Result Error as Evidence Gap

Tool timeout should not become:

```text
AKS is healthy
```

Store:

```python
{
  "kind": "TOOL_ERROR",
  "operation": "get_aks_status",
  "error": "timeout"
}
```

Route:

```text
retry if transient and policy allows
or
mark UNKNOWN
```

---

# PART 13 — Full DevOps Flow

```text
classify incident
 ↓
collect pipeline E1
 ↓
planner sees Terraform-stage failure
 ↓
collect Terraform E2
 ↓
planner sees network change
 ↓
collect AKS E3
 ↓
retrieve AKS networking R1
 ↓
evidence gate
 ↓
analyze using E* as current truth and R* as guidance
```

---

# PART 14 — Common Mistakes

- RAG chunk treated as current incident evidence
- discovered MCP tool auto-approved
- tool result shape passed raw everywhere
- no source IDs
- no weak-retrieval route
- tool timeout interpreted as negative result
- unbounded parallel calls
- reference/current evidence mixed into one text blob

---

# PART 15 — Interview Q&A

### Q1. What is the difference between RAG context and live tool evidence?
RAG usually provides reference knowledge; live tools provide current observations. Their trust and freshness semantics differ.

### Q2. What does MCP add to a LangGraph workflow?
A standardized way to discover and invoke external capabilities; the graph still controls state and routing.

### Q3. Does capability discovery mean a tool is authorized?
No. Authorization and policy filtering remain host responsibilities.

### Q4. How should tool errors be represented?
As explicit error/evidence-gap states, not fabricated values.

---

# PART 16 — Revision

```text
RAG = reference knowledge
Tool/MCP = live capability/evidence
Graph = decides when each is needed
Normalizer = common source envelope
Policy = decides what is allowed
```

---

# PART 17 — Homework

For the query:

```text
Pods cannot connect to database after today's Terraform deploy
```

List:

```text
3 live tools
2 RAG/reference searches
routing order
what evidence would be enough to stop collection
```

---

# 🔁 Next Lesson Kyu?

Graph can now loop across tools/RAG. That creates a new production risk: **runaway retries and infinite loops**. Next lesson me hard termination and retry policy design karenge.
