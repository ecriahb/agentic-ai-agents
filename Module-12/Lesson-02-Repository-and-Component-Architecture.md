# 🚩 Jai Bajrangbali!

# Lesson 02 — Repository & Component Architecture

> **Reliable agent systems keep model reasoning, evidence collection, policy, state and execution in separate components with explicit contracts.**

---

# 🎯 Lesson Goal

You will design:

- repository structure
- dependency direction
- domain boundaries
- configuration
- model adapter
- tool adapter
- RAG adapter
- graph/state layer
- policy layer
- evaluation/tests

---

# PART 1 — Proposed Repository Structure

```text
production-devops-ai-assistant/
├── app/
│   ├── api.py
│   ├── config.py
│   ├── state.py
│   ├── graph.py
│   ├── supervisor.py
│   ├── specialists/
│   │   ├── pipeline.py
│   │   ├── terraform.py
│   │   └── aks.py
│   ├── tools/
│   │   ├── contracts.py
│   │   ├── mcp_client.py
│   │   └── validators.py
│   ├── knowledge/
│   │   ├── retriever.py
│   │   └── context.py
│   ├── llm/
│   │   ├── prompts.py
│   │   └── client.py
│   ├── policy/
│   │   ├── authorization.py
│   │   └── action_policy.py
│   └── validation/
│       ├── citations.py
│       └── rca.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── evals/
│   └── security/
├── infra/
│   └── terraform/
├── docs/
│   ├── architecture.md
│   └── runbooks/
└── .github/workflows/
```

---

# PART 2 — Dependency Direction

High-level rule:

```text
Domain contracts
      ↑
Adapters / Integrations
      ↑
Orchestration
      ↑
API/UI
```

Policy should not depend on the LLM to make authorization decisions.

---

# PART 3 — Configuration

Configuration classes:

```text
runtime config
model config
retrieval config
policy config
feature flags
endpoint config
```

Secrets should be injected through secure mechanisms, not stored beside normal config.

---

# PART 4 — State Contract

Example:

```python
class IncidentState(TypedDict):
    incident_id: str
    environment: str
    cluster_name: str
    selected_agents: list[str]
    evidence: list[dict]
    references: list[dict]
    conflicts: list[dict]
    rca: str
    proposed_action: dict
    approval: str
    final_status: str
```

State is shared workflow data, not a dumping ground for all logs.

---

# PART 5 — Tool Adapter Boundary

Agent/specialist should request:

```text
get_aks_status(cluster_name)
```

It should not know whether implementation is:

```text
MCP
Azure SDK
REST API
local simulator
```

This makes testing and migration easier.

---

# PART 6 — Model Adapter

Expose application-level contract:

```text
generate_grounded_rca(context) -> RCAResult
```

Internally model may be:

```text
Ollama
enterprise model gateway
managed model endpoint
```

Framework details should not infect policy/evidence code.

---

# PART 7 — Retriever Adapter

```text
retrieve(question, identity_context) -> SourceDocuments
```

Responsibilities:

```text
authorization/filtering
query normalization
retrieval
source metadata
scores
freshness
```

LLM should not perform authorization filtering.

---

# PART 8 — Validation Boundary

After model output:

```text
schema validation
citation ID validation
required evidence support
forbidden claims
confidence policy
```

Validation result controls workflow branch.

---

# PART 9 — Policy Boundary

```python
policy.evaluate(
    identity=user,
    action=proposal,
    environment="production",
    evidence_ids=["E2", "E3"],
)
```

Output:

```text
ALLOW_READ
DENY
APPROVAL_REQUIRED
```

No prose-only policy decision.

---

# PART 10 — Testability

Because adapters are separated:

```text
real MCP client → FakeToolClient in unit test
real LLM       → DeterministicFakeModel
real retriever → FixtureRetriever
```

This makes evals repeatable.

---

# PART 11 — Versioning

Track:

```text
app version
graph version
state schema version
prompt version
model config version
tool contract version
policy version
retrieval/index version
```

Attach versions to audit/trace.

---

# PART 12 — Common Mistakes

- `main.py` contains everything
- tool implementation embedded in prompt
- model decides authorization
- evidence stored only in conversation
- config and secrets mixed
- tests require real cloud
- graph state stores raw huge documents forever

---

# PART 13 — Interview Q&A

### Q1. Why use adapters?
To isolate external dependencies behind stable application contracts, improving testing and replaceability.

### Q2. Why keep policy outside prompts?
Because prompts are probabilistic instructions; authorization and safety decisions require deterministic enforcement.

### Q3. Why version the graph/state schema?
Long-running workflows may resume after deployment, so compatibility must be controlled.

---

# 🧠 Revision

```text
LLM reasons.
Adapters connect.
State coordinates.
Policy decides.
Validators verify.
Executors act.
```

---

# 📝 Homework

Write interfaces for `ToolClient`, `Retriever`, `ModelClient`, and `PolicyEngine`.

---

# 🔁 Next Lesson Kyu?

Architecture is clean. Next we implement the most important trust foundation: **current evidence collection**.
