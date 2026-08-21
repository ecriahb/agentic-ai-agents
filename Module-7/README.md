# 🚩 Jai Bajrangbali!

# Module 7 — Model Context Protocol (MCP) for DevOps AI

> **From custom tool integrations → standardized AI-to-system connectivity using MCP.**

> **Ownership boundary:** Module 7 owns MCP protocol primitives, capability discovery, schemas, transports, clients and trust boundaries. Earlier tool/evidence concepts are prerequisites, not repeated lessons here.

Module 1 me humne tool contracts, evidence, validation aur read-only execution seekha. Module 2 me prompts/context boundaries, Module 3 me APIs, Module 4–5 me retrieval/RAG, aur Module 6 me orchestration. Module 7 in sab ko ek standardized protocol layer ke through connect karta hai.

---

## 🎯 Module 7 Learning Promise

Module ke end tak aap samjhoge:

- MCP kya hai aur kis problem ko solve karta hai
- Host, Client aur Server architecture
- protocol lifecycle, capability negotiation and discovery
- Tools, Resources and Prompts primitives
- sampling, elicitation and human-in-the-loop concepts
- stdio, Streamable HTTP and SSE transport mental models
- Python MCP SDK v2 ke through server/client banana
- tool schemas and structured outputs
- MCP security boundaries, authorization and prompt-injection risks
- MCP ko LangChain/RAG/DevOps workflows se integrate karna
- final DevOps MCP Server + Client + grounded assistant mini project

> Current course baseline: Python MCP SDK v2 / current MCP specification concepts. API syntax can evolve, but architectural contracts should remain the primary learning target.

---

## 🧠 Core Mental Model

```text
AI Application / Host
        ↓
     MCP Client
        ↓
   MCP Protocol
        ↓
     MCP Server
   ┌────┼─────┐
   │    │     │
 Tools Resources Prompts
   │    │     │
   ↓    ↓     ↓
DevOps systems / knowledge / reusable workflows
```

### One-line definition

**MCP is a standard protocol that lets AI applications discover and use external tools, resources and reusable prompt interfaces without hard-coding every integration into the model-facing application.**

---

# 🔗 How Module 7 Connects to Modules 1–6

```text
Module 1 → Tool contracts, validation, evidence
Module 2 → Prompt/context boundaries
Module 3 → API/client-server mental model
Module 4 → External knowledge representation/retrieval
Module 5 → Grounded RAG + citations
Module 6 → Orchestration + state + tools
                    ↓
Module 7 → Standard protocol boundary for exposing those capabilities
```

Critical principle:

```text
MCP does not make a tool safe.
MCP standardizes how capabilities are exposed/discovered/called.
Safety, auth, validation and business policy still belong to the application/server.
```

---

# 📚 Detailed Lesson Sequence

| Lesson | Topic | Main Outcome |
|---|---|---|
| 01 | [MCP Fundamentals — Why MCP?](Lesson-01-MCP-Fundamentals-and-Why-MCP.md) | Understand the integration problem MCP solves |
| 02 | [Host, Client & Server Architecture](Lesson-02-Host-Client-Server-Architecture.md) | Understand MCP boundaries and responsibilities |
| 03 | [Protocol Lifecycle, Capabilities & Discovery](Lesson-03-Lifecycle-Capabilities-and-Discovery.md) | Understand initialization and capability negotiation |
| 04 | [MCP Tools — Contracts, Schemas & Safety](Lesson-04-MCP-Tools-Contracts-Schemas-and-Safety.md) | Expose DevOps actions safely |
| 05 | [MCP Resources & Resource Templates](Lesson-05-MCP-Resources-and-Resource-Templates.md) | Expose read-only context/data |
| 06 | [Prompts, Sampling & Elicitation](Lesson-06-Prompts-Sampling-and-Elicitation.md) | Understand reusable prompt patterns and host-assisted interactions |
| 07 | [MCP Transports](Lesson-07-MCP-Transports.md) | Compare stdio, Streamable HTTP and SSE |
| 08 | [Build Your First Python MCP Server](Lesson-08-Build-First-Python-MCP-Server.md) | Create a working server using current SDK style |
| 09 | [Build an MCP Client](Lesson-09-Build-an-MCP-Client.md) | Discover and call server capabilities |
| 10 | [Security, Auth & Trust Boundaries](Lesson-10-Security-Auth-and-Trust-Boundaries.md) | Design least-privilege MCP integrations |
| 11 | [MCP with RAG, LangChain & DevOps](Lesson-11-MCP-with-RAG-LangChain-and-DevOps.md) | Integrate MCP into prior modules |
| 12 | [Mini Project — DevOps MCP Investigation Assistant](Lesson-12-Mini-Project-DevOps-MCP-Investigation-Assistant.md) | Build end-to-end standardized DevOps assistant |

---

# 🧪 Practical Progression

All labs live in [`examples/`](examples/README.md).

```text
V1  → First MCP server
V2  → Typed DevOps tool
V3  → Resource endpoint
V4  → Prompt primitive
V5  → First MCP client
V6  → Multi-tool DevOps MCP server
V7  → Streamable HTTP server
V8  → Tool allowlist + argument validation
V9  → DevOps MCP investigation client
V10 → Final MCP-powered DevOps assistant
```

---

# 🏗️ Final Project Architecture

```text
User Incident
      ↓
AI Host / DevOps Assistant
      ↓
MCP Client
      ↓
Capability Discovery
      ↓
┌─────────────────────────────┐
│ DevOps MCP Server           │
│                             │
│ Tools:                      │
│ - get_pipeline_status       │
│ - get_terraform_changes     │
│ - get_aks_status            │
│                             │
│ Resources:                  │
│ - runbook://aks/networking  │
│ - incident://{id}/evidence  │
│                             │
│ Prompts:                    │
│ - incident_rca              │
└─────────────────────────────┘
      ↓
Validated Evidence + Reference Context
      ↓
Grounded Analysis Chain
      ↓
Claim / Citation Validation
      ↓
Read-Only RCA
```

---

# ✅ Module 7 Success Criteria

You should be able to explain and demonstrate:

```text
1. Why MCP exists.
2. Host/client/server responsibilities.
3. Tools vs Resources vs Prompts.
4. Discovery and capability negotiation.
5. stdio vs remote transports.
6. Python MCP server/client basics.
7. Why MCP tool requests are still untrusted.
8. Why authorization cannot be delegated to the LLM.
9. How MCP fits with RAG and orchestration.
10. How to expose DevOps read-only evidence safely.
11. How to validate tool arguments and outputs.
12. How to design an MCP-powered incident assistant without auto-remediation.
```

---

# 🔁 Why Module 7 Comes After Module 6

```text
Module 6
We know how to orchestrate tools/retrievers/models
      ↓
Problem:
Every external integration still has custom wiring/contracts
      ↓
Module 7
Standardized protocol for discovering and invoking external AI capabilities
```

Module 7 ke baad hum more advanced agent architecture me ja sakte hain, where agents can reason over multiple MCP-exposed systems while application-controlled state, policy and approval remain outside model autonomy.
