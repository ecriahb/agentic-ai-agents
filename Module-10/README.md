# 🚩 Module 10 — Agent Security, Evaluation & Red Teaming for DevOps AI

> **From capable agents → trustworthy agents that can be attacked, measured, gated and safely released.**

M10 consumes every previous capability and turns safety/evaluation into deterministic engineering controls.

## 🔗 Dependency

```text
M1 tools → M2 context → M3 APIs → M4 vectors → M5 RAG
→ M6 orchestration → M7 MCP → M8 state → M9 multi-agent
                                  ↓
                         M10 Security + Eval
```

## 🎯 Learning Promise

- threat modelling and trust boundaries
- direct/indirect prompt injection
- tool abuse and excessive agency
- secrets and sensitive output handling
- RAG poisoning, stale data and ACL risks
- MCP capability security
- multi-agent contamination
- deterministic policy gates
- final-answer/retrieval/trajectory evaluation
- red-team regression tests
- metrics, kill switches and release gates

## 📚 Canonical Sequence

| # | Topic | Outcome |
|---|---|---|
| 01 | Threat Modeling | assets, actors, trust boundaries |
| 02 | Prompt Injection | direct/indirect attacks |
| 03 | Tool Abuse & Excessive Agency | capability/argument/side-effect controls |
| 04 | Secrets & Output Handling | prevent leakage |
| 05 | RAG & Knowledge Attacks | provenance/ACL/freshness |
| 06 | MCP Capability Security | server/tool/resource trust |
| 07 | Multi-Agent Attack Propagation | isolate compromised context |
| 08 | Deterministic Guardrails & Policy | fail-closed enforcement |
| 09 | Agent Evaluation | answer/retrieval/tool/trajectory metrics |
| 10 | Red Teaming | adversarial regression suite |
| 11 | Production Metrics & Release Gates | measurable safety |
| 12 | Secure Evaluation Harness | integrated project |

## 🛠️ Setup

No production credentials are required for attack labs. Use synthetic/sanitized incidents and read-only tools. Keep malicious test cases in dedicated fixtures.

## 🧠 Core Security Model

```text
Untrusted input/context
        ↓
Identity + input policy
        ↓
Agent runtime
        ↓
Tool/RAG/MCP proposals
        ↓
Deterministic authorization/policy
        ↓
Validated output
        ↓
Risk classification
        ↓
Human approval for high-risk writes
        ↓
Isolated executor
        ↓
Verification + audit
```

Golden rule:

```text
System prompt = guidance
Policy code = enforcement
```

## 🧪 Practical Progression

```text
V1 threat model
V2 injection lab
V3 tool policy gate
V4 secret/output redaction
V5 malicious RAG lab
V6 MCP trust policy
V7 multi-agent isolation
V8 deterministic policy engine
V9 evaluation + trajectory scoring
V10 red-team release harness
```

## 🔐 Release-blocking invariants

```text
Unknown tool execution = 0
Unauthorized production write = 0
Secret leakage = 0
Unknown citation accepted = 0
Unbounded loop = 0
Cross-scope unauthorized retrieval = 0
```

Critical security failures should not be averaged away by a good overall score.

## 🚫 Do Not Repeat

M10 consolidates security across previous modules. M11 will place those controls into Azure infrastructure; it will not reteach prompt injection or tool validation from scratch.

## ✅ Exit Gate

You can threat-model the capstone, construct direct/indirect injection tests, gate tool calls, test RAG/MCP boundaries, evaluate trajectories and make a release PASS/FAIL decision.

## 🔗 Continue

➡️ [Module 11 — Enterprise Architecture](../Module-11/README.md)

⬅️ [Module 9 — Multi-Agent Systems](../Module-9/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
