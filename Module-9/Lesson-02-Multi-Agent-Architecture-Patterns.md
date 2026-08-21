# 🚩 Jai Bajrangbali!

# Lesson 02 — Multi-Agent Architecture Patterns

> **Right pattern choose karna agent count se zyada important hai. Supervisor, router, handoff aur custom graph alag problems solve karte hain.**

---

# 🎯 Lesson Goal

Aap compare karoge:
- supervisor/subagents
- router
- handoffs
- custom LangGraph workflow
- parallel fan-out/fan-in
- pattern selection for DevOps
- when not to use a pattern

---

# PART 1 — Core Pattern Map

```text
SUPERVISOR
Central coordinator repeatedly delegates work.

ROUTER
Classify once → send to one/more specialists → synthesize.

HANDOFF
Active agent changes and may directly continue user interaction.

CUSTOM GRAPH
Explicit nodes/edges/state combine deterministic + agentic logic.
```

These patterns can be mixed.

---

# PART 2 — Supervisor Pattern

```text
User
 ↓
Supervisor
 ├─ calls Pipeline Agent
 ├─ calls Terraform Agent
 ├─ calls AKS Agent
 └─ combines results
```

Good when:
- multiple domains
- central control required
- multi-hop delegation
- subagents do not need direct user conversation

Risk:

```text
Supervisor becomes bottleneck / single point of reasoning failure.
```

---

# PART 3 — Router Pattern

```text
Incident
 ↓
Classifier/Router
 ├─ pipeline issue → Pipeline Agent
 ├─ infra issue    → Terraform Agent
 └─ runtime issue  → AKS Agent
```

Router can fan-out to several agents.

Good when:
- classification is clear
- tasks mostly independent
- parallel execution useful

Router != supervisor:

```text
Router = dispatch decision
Supervisor = ongoing coordinator across multiple turns/steps
```

### Optional Framework Comparison

The architecture pattern is independent of the library. A role/task/crew framework can make supervisor-style delegation concise; LangGraph makes state, routing, interrupts, and recovery explicit; a direct Python implementation gives maximum control but more plumbing.

Translate the same pipeline/Terraform/AKS team into one optional framework example and compare the contracts, not just line count:

```text
specialist scope -> tool permissions -> evidence contract
                  -> handoff/state -> conflict gate -> audit
```

Reject the translation if the framework hides any of these boundaries. The portable skill is designing the contract; framework syntax is an implementation choice.

---

# PART 4 — Handoff Pattern

```text
General Agent
 ↓ transfer
AKS Specialist
 ↓ transfer
Security Specialist
```

Useful when:
- one active specialist should own interaction
- stages are sequential
- current agent identity matters
- capability set changes with state

State may contain:

```python
{"active_agent": "aks_specialist"}
```

Danger:
- ping-pong handoffs
- context bloat
- invalid message history
- unclear ownership

---

# PART 5 — Custom Graph Pattern

For high-risk DevOps:

```text
Validate
 ↓
Parallel Evidence Collection
 ↓
Evidence Gate
 ↓
Specialist Analysis
 ↓
Conflict Gate
 ↓
Synthesis
 ↓
Human Approval
```

Not every decision should be model-driven.

Use deterministic nodes for:
- auth
- tool allowlists
- evidence validation
- loop limits
- approval checks
- final policy enforcement

---

# PART 6 — Parallel Fan-Out / Fan-In

```text
             START
               ↓
     ┌─────────┼─────────┐
     ↓         ↓         ↓
 Pipeline   Terraform    AKS
     ↓         ↓         ↓
     └─────────┼─────────┘
               ↓
            MERGE
```

Works when agents are independent.

Do not parallelize dependencies:

```text
Terraform change identification
must happen before
specific AKS hypothesis validation
```

unless workflow explicitly supports speculative parallel work.

---

# PART 7 — Pattern Selection Matrix

```text
Need central repeated delegation? → Supervisor
Need one-time classification/fan-out? → Router
Need specialist to take over conversation? → Handoff
Need strict policy/state/approval? → Custom Graph
Need independent investigation speed? → Parallel fan-out
```

---

# PART 8 — DevOps Architecture Example

Incident is unknown initially.

Phase 1:

```text
Router
→ Pipeline + Terraform + AKS checks in parallel
```

Phase 2:

```text
Supervisor
→ asks Terraform specialist to deepen investigation
```

Phase 3:

```text
Custom graph
→ validate RCA → approval gate
```

Patterns can compose.

---

# PART 9 — Context Engineering by Pattern

Supervisor:

```text
subagent receives task-specific context only
```

Router:

```text
each target receives normalized incident input
```

Handoff:

```text
pass minimum valid conversation/context
```

Custom graph:

```text
shared state schema defines exact information flow
```

---

# PART 10 — Common Mistakes

- supervisor for a simple one-shot route
- router when ongoing multi-hop coordination needed
- handoff when subagents should be invisible to user
- passing entire chat history to every agent
- agent-controlled auth decisions
- no termination policy
- no result contract

---

# PART 11 — Interview Q&A

### Q1. Supervisor vs router?
Supervisor maintains ongoing coordination and can delegate repeatedly; router usually classifies and dispatches input in a bounded step.

### Q2. When use handoffs?
When control/user interaction should move between specialized states or agents.

### Q3. Why use custom LangGraph workflow?
To combine agentic decisions with deterministic state, routing, validation, persistence and approval.

### Q4. Can patterns be mixed?
Yes. A custom graph may include a router, supervisor-like node, subgraphs and handoffs.

---

# PART 12 — Revision

```text
Pattern follows interaction shape.
Supervisor = coordinate.
Router = dispatch.
Handoff = transfer control.
Graph = explicit workflow policy.
Parallel = independent work only.
```

---

# PART 13 — Homework

Design architecture for:

```text
"Production deployment failed; cause unknown."
```

Choose router/supervisor/handoff/custom graph and justify each component.

---

# 🔁 Next Lesson Kyu?

Pattern choose kar liya. Ab decide karna hai **specialist agents ki responsibilities exactly kya hongi**.
