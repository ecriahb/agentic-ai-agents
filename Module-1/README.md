# 🚩 Module 1 — LLM APIs, Local Models, Tools & First DevOps Agent

> **Canonical live-class sequence restored exactly:** Roadmap → UI/API → environment → OpenAI → Ollama → first call → tokens/context → structured output → tools → basic agent → complete lab → troubleshooting → interview/revision → official references.

Module 0 me LLM fundamentals samjhe. Module 1 me existing LLM ko Python application ke andar use karke cloud/local model calls, validation, tools, evidence aur first controlled DevOps agent build karte hain.

---

# 🎯 Learning Promise

Module ke end tak learner samjhega:

- ChatGPT UI vs API
- Python/venv/secrets
- OpenAI hosted API setup
- Ollama local zero-cost learning path
- first request and response object
- tokens, cost and context engineering
- structured output + Pydantic
- tool/function calling
- host-controlled execution
- agent loop + state
- evidence grounding
- no-evidence/no-RCA guardrail
- tool allowlists and argument validation
- trusted DevOps RCA architecture

---

# 🧠 Core Mental Model

```text
User / Incident
      ↓
Python Host Application
      ↓
Prompt + Context
      ↓
LLM (OpenAI or Ollama)
      ↓
Response / Tool Request
      ↓
Host Validation
      ↓
Known Tool Execution
      ↓
Evidence
      ↓
Grounded RCA
      ↓
Validation / Policy
```

Remember:

```text
LLM = reasoner
Host = controller/executor
Tool = capability
Tool output = evidence
Schema = data contract
Policy = deterministic boundary
```

---

# 📚 Canonical Module 1 Lesson Sequence

## 0 — [Module 1 Roadmap & Mental Model](Lesson-00-Module-1-Roadmap-and-Mental-Model.md)
Why this module exists, full architecture, two provider tracks, recurring DevOps incident and learning order.

## 1 — [ChatGPT UI vs API](Lesson-01-ChatGPT-UI-vs-API.md)
Human-facing product interaction vs software integration.

## 2 — [Development Environment & Secret Management](Lesson-02-Development-Environment-and-Secrets.md)
Python, venv, pip, `.env`, secret hygiene and local setup.

## 3 — [OpenAI Cloud API Setup](Lesson-03-OpenAI-Cloud-API-Setup.md)
Hosted provider setup, API key handling, account/billing/model-access concepts and common failures.

## 4 — [Zero-Cost Local AI with Ollama](Lesson-04-Zero-Cost-Local-AI-with-Ollama.md)
Local models, `localhost:11434`, provider comparison and hardware trade-offs.

## 5 — [First API Call & Response Object](Lesson-05-First-API-Call-and-Response-Object.md)
`client.responses.create()`, request anatomy, response object, metadata and first provider failure drills.

## 6 — [Tokens, Cost & Context Engineering](Lesson-06-Tokens-Cost-and-Context-Engineering.md)
Tokens, context window, hosted usage/cost thinking, log trimming and evidence density.

## 7 — [Structured Output & Validation](Lesson-07-Structured-Output-and-Validation.md)
JSON/schema/Pydantic, layered validation and the crucial rule `schema-valid != factually true`.

## 8 — [Tool Calling / Function Calling](Lesson-08-Tool-Calling-Function-Calling.md)
Model requests tools; host validates and executes. All tool names/arguments/targets are treated as untrusted proposals.

## 9 — [From Tool Calling to a Basic DevOps Agent](Lesson-09-From-Tool-Calling-to-Basic-DevOps-Agent.md)
Bounded decide→act→observe loop, state, evidence, stop conditions and V1→V4 evolution.

## A — [Complete Lab Code](A-Complete-Lab-Code.md)
Cloud + local calls → structured output → tools → V1–V4 → real `pipeline.log` → final trusted RCA.

## B — [Troubleshooting Playbook](B-Troubleshooting-Playbook.md)
Environment, credentials, provider, Ollama, response, schema, tool, evidence and validation failures.

## C — [Interview & Revision Sheet](C-Interview-and-Revision-Sheet.md)
Definitions, core distinctions, architecture answer, Q&A, viva and rapid revision.

## D — [Official References](D-Official-References.md)
Where to verify current OpenAI/Ollama/Python/Pydantic behavior and version-sensitive details.

---

# 🧪 Zero-to-Hero Practical Track

Follow [`PRACTICAL-ROADMAP.md`](PRACTICAL-ROADMAP.md) in parallel with the lessons.

```text
V1  First Hosted/OpenAI Call
 ↓
V2  First Local/Ollama Call
 ↓
V3  Structured Output
 ↓
V4  Basic Tool Request
 ↓
V5  Real File Tool
 ↓
V6  DevOps Agent V1
 ↓
V7  DevOps Agent V2
 ↓
V8  DevOps Agent V3
 ↓
V9  DevOps Agent V4
 ↓
V10 Trusted RCA / Provider Comparison
```

All runnable files: [`examples/`](examples/README.md)

---

# 🔥 Recurring DevOps Evidence

```text
Terraform Apply started
      ↓
NSG rule aks-subnet-allow removed
      ↓
AKS subnet connectivity validation failed
      ↓
Deployment failed during Terraform Apply
```

Safe conclusion should be based on evidence, not model confidence.

---

# 🔐 Most Important Module 1 Rules

```text
1. We use an existing LLM; we are not training a model.
2. Cloud/local model output is untrusted analysis.
3. Tool call is a proposal, not execution authority.
4. Host validates tool name, arguments and target.
5. Tool output becomes evidence only with provenance.
6. Structured output validates shape, not factual truth.
7. No evidence → no forced RCA.
8. Agent loops need stop conditions and budgets.
9. Read-only tools first; risky writes need authorization + approval.
10. Provider can change; evidence/validation/policy rules must not.
```

---

# 📎 Supplementary Deep Dives Preserved

These older expanded files contain useful combined material from the live practical evolution. They are **supplementary**, not the canonical lesson numbering:

- [`Lesson-03-Our-First-Real-AI-API-Call.md`](Lesson-03-Our-First-Real-AI-API-Call.md) — expanded API-call notes
- [`Lesson-04-Local-AI-with-Ollama.md`](Lesson-04-Local-AI-with-Ollama.md) — expanded Ollama + structured/tool/agent experiments
- [`Lesson-05-Fake-Tool-to-Real-Tool.md`](Lesson-05-Fake-Tool-to-Real-Tool.md) — deep real-tool/evidence/trusted-RCA progression

The canonical learning path above should be followed first.

---

# ✅ Module Completion Test

Before Module 2, learner should explain without notes:

```text
Why API instead of only UI?
How are secrets stored safely in development?
How do OpenAI and Ollama differ?
What does client.responses.create() do?
What is a response object?
Why do tokens/context matter?
Why is structured output not truth?
Who actually executes tools?
What makes tool arguments untrusted?
What turns tool calling into an agent?
Why does no evidence mean no forced RCA?
```

> **Module 1 outcome:** Beginner can move from a simple model call to a controlled, evidence-grounded first DevOps AI agent and can explain every layer instead of only running final code.