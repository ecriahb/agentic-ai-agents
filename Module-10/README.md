# 🚩 Jai Bajrangbali!

# Module 10 — Agent Security, Evaluation & Red Teaming for DevOps AI

> **From capable agents → trustworthy agents that can be threat-modelled, attacked, measured, gated and safely released.**

Modules 1–9 built the capabilities: evidence tools, prompt/context engineering, APIs, embeddings, RAG, orchestration, MCP, stateful agents and multi-agent systems. Module 10 answers the production-trust question:

```text
The agent can do useful work.
How do we prove it cannot misuse tools,
leak sensitive data,
trust poisoned context,
bypass approval,
or regress after a model/prompt/tool change?
```

---

## 🎯 Module 10 Learning Promise

By the end of this module you will understand and demonstrate:

- agent threat modelling and trust-boundary analysis
- direct and indirect prompt injection
- tool abuse, argument abuse, excessive agency and side effects
- secret minimization, redaction and safe output handling
- RAG poisoning, stale knowledge, ACL and vector/index risks
- MCP server/tool/resource trust boundaries
- multi-agent contamination and privilege propagation
- deterministic policy/guardrail architecture
- final-response, retrieval and trajectory evaluation
- red-team/adversarial test design
- production security metrics, kill switches and release gates
- final secure DevOps agent evaluation harness

Every lesson follows the same classroom-depth structure:

```text
Why the topic matters
→ English definition
→ detailed Hinglish explanation
→ attack architecture
→ vulnerable DevOps scenario
→ secure architecture
→ deterministic controls
→ bypass/edge cases
→ tests and metrics
→ common mistakes
→ interview Q&A
→ revision
→ homework/red-team exercise
→ why next topic
```

---

# 🔗 Module 1–9 Connection

```text
Module 1  → tool contracts + evidence + validation
Module 2  → prompt/context boundaries
Module 3  → APIs + auth + error handling
Module 4  → embeddings/vector stores
Module 5  → RAG + citations + grounding
Module 6  → orchestration + state boundaries
Module 7  → MCP + external capability trust
Module 8  → stateful agents + HITL + checkpoints
Module 9  → multi-agent coordination + shared/private state
                     ↓
Module 10 → SECURITY + EVALUATION + RED TEAMING
```

---

# 🧠 Core Security Mental Model

```text
Untrusted Input / Context
        ↓
Identity + Input Policy
        ↓
Agent / Multi-Agent Runtime
        ↓
Retrieval / MCP / Tool Proposals
        ↓
Deterministic Policy + Authorization
        ↓
Validated Evidence / Context
        ↓
Model Output
        ↓
Schema + Citation + Data-Leak Validation
        ↓
Risk Classification
        ↓
Human Approval for High-Risk Write
        ↓
Isolated Executor
        ↓
Post-Action Verification + Audit
```

Core principle:

```text
System prompt is guidance.
Policy code is enforcement.
```

---

# 📚 Detailed Lesson Sequence

| Lesson | Topic | Main Outcome |
|---|---|---|
| 01 | [Agent Security Fundamentals & Threat Modeling](Lesson-01-Agent-Security-Fundamentals-and-Threat-Modeling.md) | Map assets, actors, entry points, trust boundaries and invariants |
| 02 | [Prompt Injection & Instruction Hierarchy](Lesson-02-Prompt-Injection-and-Instruction-Hierarchy.md) | Defend against direct/indirect instruction attacks |
| 03 | [Tool Abuse, Excessive Agency & Side Effects](Lesson-03-Tool-Abuse-Excessive-Agency-and-Side-Effects.md) | Bound capabilities, arguments, writes, retries and blast radius |
| 04 | [Sensitive Data, Secrets & Output Handling](Lesson-04-Sensitive-Data-Secrets-and-Output-Handling.md) | Prevent prompt/state/trace/output leakage and unsafe sinks |
| 05 | [RAG, Vector & Knowledge-Base Attacks](Lesson-05-RAG-Vector-and-Knowledge-Base-Attacks.md) | Secure ingestion, ACL, freshness, provenance and retrieval |
| 06 | [MCP & External Capability Security](Lesson-06-MCP-and-External-Capability-Security.md) | Secure server registry, auth, tool/resource trust and tokens |
| 07 | [Multi-Agent Security & Attack Propagation](Lesson-07-Multi-Agent-Security-and-Attack-Propagation.md) | Stop compromised agents contaminating peers/shared state |
| 08 | [Deterministic Guardrails & Policy Gates](Lesson-08-Deterministic-Guardrails-and-Policy-Gates.md) | Move critical decisions outside probabilistic model reasoning |
| 09 | [Agent Evaluation Fundamentals](Lesson-09-Agent-Evaluation-Fundamentals.md) | Evaluate final output, retrieval, tools, arguments and trajectories |
| 10 | [Red Teaming & Adversarial Test Design](Lesson-10-Red-Teaming-and-Adversarial-Test-Design.md) | Attack prompt/RAG/MCP/tools/state/multi-agent surfaces systematically |
| 11 | [Production Observability, Metrics & Release Gates](Lesson-11-Production-Observability-Metrics-and-Release-Gates.md) | Turn security/evals into measurable production controls |
| 12 | [Mini Project — Secure DevOps Agent Evaluation Harness](Lesson-12-Mini-Project-Secure-DevOps-Agent-Evaluation-Harness.md) | Combine attack datasets, trajectories, evaluators and release decisions |

---

# 🧪 Practical V1 → V10

All runnable labs are in [`examples/`](examples/README.md).

```text
V1  Threat model a DevOps agent
 ↓
V2  Direct/indirect prompt-injection lab
 ↓
V3  Tool policy gate / excessive-agency prevention
 ↓
V4  Secret & sensitive-output redaction
 ↓
V5  Malicious RAG document / retrieval trust lab
 ↓
V6  MCP server/tool trust policy
 ↓
V7  Multi-agent contamination isolation
 ↓
V8  Deterministic policy engine
 ↓
V9  Evaluation dataset + trajectory/security scoring
 ↓
V10 Secure agent red-team & release harness
```

The practical folder also contains a security test matrix and security notes for safe extension.

---

# 🏗️ Final Project Architecture

```text
Normal / Failure / Attack Test
            ↓
        Agent Runner
            ↓
     Trajectory Recorder
            ↓
┌───────────┼────────────┬──────────────┐
↓           ↓            ↓              ↓
Tool Eval  RAG Eval   MCP Eval    Multi-Agent Eval
↓           ↓            ↓              ↓
Policy    Evidence     Trust         Provenance
↓           ↓            ↓              ↓
Approval  Citations    Auth         Shared-State Rules
└───────────┼────────────┴──────────────┘
            ↓
       Secret / Output Scan
            ↓
        Budget Evaluator
            ↓
          Scorecard
            ↓
     PASS / FAIL / REVIEW
            ↓
        Release Gate
```

---

# 🔐 Critical Invariants

These should be deterministic and release-blocking:

```text
Unknown tool execution = 0
Production write without authorization = 0
Production write without exact approval = 0
Cross-tenant unauthorized retrieval = 0
Secret leakage = 0
Unknown citation accepted = 0
Unbounded loop = 0
Peer-agent privilege transfer = 0
```

---

# ✅ Module 10 Success Criteria

You should be able to explain and demonstrate:

```text
1. Why agent threat models differ from chatbot threat models.
2. Direct vs indirect prompt injection.
3. Why a system prompt is not a security boundary.
4. Tool allowlists, argument validation and target authorization.
5. Excessive agency and side-effect isolation.
6. Secret minimization and safe output handling.
7. RAG poisoning, stale-index and cross-scope retrieval risks.
8. MCP server/tool/resource trust and authorization boundaries.
9. Multi-agent contamination and shared/private state controls.
10. Deterministic policy gates and fail-closed behavior.
11. Final-answer vs trajectory evaluation.
12. Red-team test design and regression conversion.
13. Production metrics, kill switches and release gates.
14. Why critical security failures cannot be averaged away.
```

---

# 🔁 Why Module 11 Comes Next

```text
Module 10
We can test and secure the agent logic
        ↓
Next production question:
Where does this system run?
How is identity/network/state/HA/DR/observability governed?
        ↓
Module 11
Enterprise DevOps AI Architecture & Production Deployment
```
