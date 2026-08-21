# 🚩 Jai Bajrangbali!

# Module 12 — Final Enterprise Project: Production DevOps AI Assistant

> **Build the complete system: evidence-grounded, stateful, multi-agent, MCP-enabled, security-gated and production-architected DevOps AI Assistant.**

> **Ownership boundary:** Module 12 integrates the earlier contracts into one capstone. It does not re-teach Module 10 security theory or Module 11 platform theory; its lessons keep only integration-specific tests, deployment decisions and runbooks.

This capstone combines every previous module into one engineering project.

---

# 🎯 Final Project Mission

Build an assistant that can safely investigate a production DevOps incident such as:

```text
Production AKS deployment started failing after a Terraform networking change.
Investigate the incident, produce evidence-grounded RCA,
recommend the safest next action, and require approval before any write.
```

The assistant must **not** guess, execute arbitrary commands or treat model output as authority.

---

# 🔗 Full Course Integration

```text
Module 0  AI/LLM foundations
Module 1  Tools + evidence + trusted RCA
Module 2  Prompt/context engineering
Module 3  APIs + Python
Module 4  Embeddings/vector search
Module 5  RAG + citations
Module 6  LangChain orchestration
Module 7  MCP capability layer
Module 8  Stateful LangGraph workflows
Module 9  Multi-agent specialists
Module 10 Security + eval + red teaming
Module 11 Enterprise Azure architecture
                ↓
Module 12
PRODUCTION DEVOPS AI ASSISTANT
```

---

# 🧠 Final Architecture

```text
                         USER / INCIDENT API
                                ↓
                        AuthN + Input Policy
                                ↓
                      Stateful Supervisor Graph
                                ↓
        ┌───────────────────────┼───────────────────────┐
        ↓                       ↓                       ↓
 Pipeline Specialist     Terraform Specialist      AKS Specialist
        ↓                       ↓                       ↓
     Tool/MCP E1              Tool/MCP E2              Tool/MCP E3
        └───────────────────────┼───────────────────────┘
                                ↓
                         Evidence Contract
                                ↓
                        Knowledge/RAG Agent
                              R1/R2
                                ↓
                        Conflict / Gap Gate
                                ↓
                         Grounded Synthesis
                                ↓
                      Citation/Claim Validator
                                ↓
                       Security/Policy Engine
                                ↓
                       Remediation Proposal
                                ↓
                       HUMAN APPROVAL GATE
                                ↓
                        Isolated Write Executor
                                ↓
                      Post-Action Verification
                                ↓
                    Final Status + Audit Record
```

Learning implementation keeps write execution simulated/read-only by default.

---

# 📚 12 Capstone Lessons

| Lesson | Topic |
|---|---|
| 01 | [Project Requirements & Definition of Done](Lesson-01-Project-Requirements-and-Definition-of-Done.md) |
| 02 | [Repository & Component Architecture](Lesson-02-Repository-and-Component-Architecture.md) |
| 03 | [Trusted Evidence & Tool Layer](Lesson-03-Trusted-Evidence-and-Tool-Layer.md) |
| 04 | [Knowledge/RAG Layer](Lesson-04-Knowledge-RAG-Layer.md) |
| 05 | [MCP Capability Integration](Lesson-05-MCP-Capability-Integration.md) |
| 06 | [Stateful Multi-Agent Investigation Graph](Lesson-06-Stateful-Multi-Agent-Investigation-Graph.md) |
| 07 | [Grounded RCA, Validation & Confidence](Lesson-07-Grounded-RCA-Validation-and-Confidence.md) |
| 08 | [Security, Policy & Human Approval](Lesson-08-Security-Policy-and-Human-Approval.md) |
| 09 | [Evaluation & Red-Team Release Suite](Lesson-09-Evaluation-and-Red-Team-Release-Suite.md) |
| 10 | [Enterprise Deployment Architecture](Lesson-10-Enterprise-Deployment-Architecture.md) |
| 11 | [CI/CD, Operations & Incident Runbooks](Lesson-11-CICD-Operations-and-Incident-Runbooks.md) |
| 12 | [Final Demo, Interview Story & Portfolio Checklist](Lesson-12-Final-Demo-Interview-and-Portfolio.md) |

---

# 🧪 Practical Progression

```text
V1  Project contract + state
V2  Read-only evidence tools
V3  Knowledge/RAG retrieval
V4  Source-labelled context
V5  Supervisor + specialists
V6  Conflict/gap validation
V7  Grounded RCA + citations
V8  Policy + approval simulation
V9  Security/eval release gate
V10 Final Production DevOps AI Assistant
```

All labs are under [`examples/`](examples/README.md).

---

# ✅ Definition of Done

The project is complete only when:

- [ ] current incident facts come from evidence, not model memory
- [ ] reference knowledge is labelled separately
- [ ] tool/MCP capabilities are allowlisted and argument validated
- [ ] state survives graph transitions and supports checkpointing design
- [ ] specialists have scoped responsibilities
- [ ] evidence conflicts/gaps are explicit
- [ ] RCA citations use only known source IDs
- [ ] unsupported claims cause validation failure/abstention
- [ ] production write is never performed from raw model output
- [ ] authorization and human approval are separate gates
- [ ] red-team/eval suite can block release
- [ ] enterprise identity/network/state/observability architecture is documented
- [ ] final demo is reproducible locally

---

# 🎓 Portfolio Outcome

After Module 12 you should be able to explain:

```text
I did not build a chatbot.
I built an evidence-grounded DevOps investigation system with:
- controlled tools
- RAG
- MCP
- stateful multi-agent orchestration
- deterministic policy
- human approval
- evaluation/red teaming
- production Azure architecture
```

That is the final course outcome.
