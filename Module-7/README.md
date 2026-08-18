# 🚩 Module 7 — Model Context Protocol (MCP) for DevOps AI

> **From custom integrations → standardized AI-to-system connectivity.**

M1 taught tool contracts; M3 taught APIs; M5 taught grounded knowledge; M6 taught orchestration. M7 standardizes how capabilities are exposed and discovered.

## 🔗 Dependency

```text
M1 Tools → M3 APIs → M5 RAG → M6 Orchestration → M7 MCP
```

## 🎯 Learning Promise

- MCP purpose and architecture
- Host, Client, Server
- lifecycle, capabilities and discovery
- Tools, Resources and Prompts
- sampling/elicitation concepts
- stdio, Streamable HTTP and SSE mental models
- Python MCP server/client
- schemas and structured outputs
- auth, authorization and trust boundaries
- MCP + RAG + orchestration + DevOps

> MCP standardizes connectivity. It does **not** automatically make a tool safe.

## 📚 Canonical Sequence

| # | Topic | Deep Outcome |
|---|---|---|
| 01 | MCP Fundamentals | integration problem |
| 02 | Host, Client & Server | boundaries |
| 03 | Lifecycle, Capabilities & Discovery | initialization |
| 04 | Tools, Contracts & Safety | typed capability calls |
| 05 | Resources & Templates | read-only context |
| 06 | Prompts, Sampling & Elicitation | reusable interactions |
| 07 | Transports | local vs remote connectivity |
| 08 | Build Python MCP Server | working server |
| 09 | Build MCP Client | discovery/calls |
| 10 | Security, Auth & Trust | least privilege |
| 11 | MCP + RAG + LangChain + DevOps | integration |
| 12 | DevOps MCP Investigation Assistant | capstone |

## 🛠️ Setup

Use a Python venv and the current MCP SDK specified by the lab's requirements. Start with **stdio** locally. Add remote transport only after understanding the protocol boundary.

```text
Host
 ↓
MCP Client
 ↓
MCP protocol
 ↓
MCP Server
 ↓
DevOps APIs / knowledge
```

## 🧪 Practical Progression

```text
V1 server
V2 typed read-only tool
V3 resource
V4 prompt primitive
V5 client
V6 multi-tool server
V7 remote transport
V8 allowlist + argument validation
V9 investigation client
V10 final assistant
```

Example capabilities:

```text
get_pipeline_status
get_terraform_changes
get_aks_status
runbook://aks/networking
incident://{id}/evidence
```

## 🔐 Security Boundary

```text
MCP discovery ≠ authorization
Tool schema ≠ permission
LLM request ≠ trusted instruction
```

Authorization, validation, identity and business policy remain outside model autonomy.

## 🚫 Do Not Repeat

M1 owns generic tool contracts. M7 teaches the MCP protocol boundary and its implementation. M8 will consume MCP capabilities inside a stateful graph rather than reteaching MCP.

## ✅ Exit Gate

You can explain Tools vs Resources vs Prompts, draw Host/Client/Server, build a read-only server/client, validate arguments and explain why MCP does not replace authorization.

## 🔗 Continue

➡️ [Module 8 — Stateful Agents & LangGraph](../Module-8/README.md)

⬅️ [Module 6 — LangChain](../Module-6/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
