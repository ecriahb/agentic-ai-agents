# 🚩 Module 8 — Stateful Agents & LangGraph-Style Workflows for DevOps

> **From fixed orchestration → explicit state, routing, loops, checkpoints, recovery and approval.**

M1–M7 provided tools, evidence, prompts, APIs, retrieval, RAG, orchestration and MCP. M8 combines them into a stateful workflow.

## 🔗 Dependency

```text
M6 orchestration + M7 MCP
        ↓
M8 stateful graph
        ↓
M9 multi-agent coordination
```

## 🎯 Learning Promise

- chain vs workflow vs agent
- state/node/edge mental model
- state schemas and reducers
- conditional routing
- deterministic vs LLM-driven decisions
- controlled agent/tool loops
- RAG + MCP routing
- retry, timeout, loop limits and termination
- human approval interrupts
- checkpoints and recovery
- subgraphs and bounded multi-agent introduction
- production observability and evaluation

## 📚 Canonical Sequence

| # | Topic | Outcome |
|---|---|---|
| 01 | Agent vs Workflow vs Chain | choose the right abstraction |
| 02 | Why Stateful Graphs | understand graph benefits |
| 03 | State Models, Schemas & Reducers | trustworthy state |
| 04 | Nodes, Edges & Conditional Routing | explicit transitions |
| 05 | Agent Loops, Planning & Tool Selection | bounded loops |
| 06 | RAG + MCP + Tool Routing | connect prior capabilities |
| 07 | Retry, Loop Limits & Termination | prevent runaway behavior |
| 08 | Human-in-the-Loop & Approval | safe pauses |
| 09 | Checkpointing & Recovery | resumable execution |
| 10 | Subgraphs & Multi-Agent Patterns | controlled decomposition |
| 11 | Production Safety & Evaluation | operate safely |
| 12 | Stateful DevOps Incident Agent | full graph |

## 🛠️ Setup

Create the module environment and install only the listed requirements. Use a local model for learning where possible. Checkpoint storage can start in-memory and move to persistent storage in the production lesson.

## 🧠 Core Model

```text
Incident
 ↓
State
 ↓
Collect evidence
 ↓
Evidence gate
 ├─ weak → collect more
 └─ enough → retrieve
                 ↓
              analyze
                 ↓
             validate
             ├─ fail → more evidence
             └─ pass → approval if required
                         ↓
                       final
```

### Example state

```python
state = {
    "incident_id": "INC-1001",
    "evidence": [],
    "references": [],
    "claims": [],
    "status": "investigating",
    "approval": None
}
```

State should contain normalized workflow facts—not hidden model reasoning.

## 🧪 Practical Progression

```text
V1 StateGraph
V2 conditional routing
V3 evidence reducer
V4 controlled tool loop
V5 RAG + MCP router
V6 retry + loop limit
V7 approval interrupt
V8 checkpoint + resume
V9 supervisor/subgraph
V10 final incident agent
```

## 🔐 Hard Rules

```text
Every loop has a termination policy.
Every write has an authorization boundary.
Every risky action can pause for approval.
Checkpoint state must not silently mix secrets with evidence.
```

## 🚫 Do Not Repeat

M8 owns state, transitions, persistence and recovery. M9 owns multi-agent coordination. Do not turn M8 into a second multi-agent course.

## ✅ Exit Gate

You can draw the graph, explain state ownership, implement conditional routing, cap loops, pause for approval and resume from a checkpoint after failure.

## 🔗 Continue

➡️ [Module 9 — Multi-Agent Systems](../Module-9/README.md)

⬅️ [Module 7 — MCP](../Module-7/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
