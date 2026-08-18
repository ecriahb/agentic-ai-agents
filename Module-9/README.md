# 🚩 Module 9 — Multi-Agent Systems for DevOps AI

> **From one stateful agent → coordinated specialists with scoped context, evidence contracts and controlled authority.**

M8 taught state and routing. M9 asks when one agent is no longer the right decomposition.

## 🔗 Dependency

```text
M1 tools/evidence → M5 RAG → M7 MCP → M8 stateful graph
                                      ↓
                               M9 multi-agent
```

## 🎯 Learning Promise

- when multi-agent is justified
- supervisor/router/handoff patterns
- specialization boundaries
- shared vs private state
- context isolation
- evidence/result contracts
- conflict detection and deterministic synthesis
- RAG/MCP/tool access per agent
- authority and human approval
- system-level evaluation, observability and cost

## 📚 Canonical Sequence

| # | Topic | Outcome |
|---|---|---|
| 01 | Multi-Agent Fundamentals | justify complexity |
| 02 | Architecture Patterns | supervisor/router/handoff |
| 03 | Specialization & Boundaries | focused agents |
| 04 | Supervisor & Subagents | centralized coordination |
| 05 | Router & Parallel Specialists | fan-out/fan-in |
| 06 | Handoffs & Active State | controlled transfer |
| 07 | Shared/Private State & Context | isolation |
| 08 | Communication & Evidence Contracts | machine-verifiable results |
| 09 | Conflict Resolution & Synthesis | evidence-based merge |
| 10 | RAG/MCP/Tools/Approval | scoped capabilities |
| 11 | Production Evaluation & Observability | system quality |
| 12 | Multi-Agent DevOps Incident Team | full project |

## 🛠️ Setup

Start from M8's graph environment. Use synthetic incidents and read-only tools. Each specialist should have only the tools/context it needs.

## 🧠 Example Team

```text
                 Supervisor
                     ↓
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
   Pipeline       Terraform       AKS
   Specialist     Specialist    Specialist
       ↓             ↓             ↓
      E1            E2            E3
       └─────────────┼─────────────┘
                     ↓
              Evidence Validator
                     ↓
              Knowledge/RAG Agent
                     ↓
                Synthesis
```

### Important

```text
More agents != more intelligence
More agents = more coordination + more failure boundaries
```

If three agents disagree, do not simply vote. First determine whether the evidence is incomplete, stale or conflicting.

## 🧪 Practical Progression

```text
V1 two deterministic specialists
V2 router
V3 parallel specialists
V4 supervisor/subagents
V5 shared evidence contract
V6 private context + handoff
V7 conflict + synthesis
V8 RAG/MCP capability routing
V9 approval/checkpoint flow
V10 final incident team
```

## 🔐 Authority Rules

Agents may propose. Deterministic policy authorizes. Humans approve high-risk writes. A peer agent must never silently transfer privilege to another agent.

## 🚫 Do Not Repeat

M9 owns coordination among multiple agents. M8 owns graph state/checkpoints; M10 owns security/evaluation. Reuse those foundations rather than reteaching them.

## ✅ Exit Gate

You can justify multi-agent use, choose supervisor vs router vs handoff, isolate context, define evidence contracts, merge conflicting results deterministically and keep authority outside model reasoning.

## 🔗 Continue

➡️ [Module 10 — Security, Evaluation & Red Teaming](../Module-10/README.md)

⬅️ [Module 8 — Stateful Agents](../Module-8/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
