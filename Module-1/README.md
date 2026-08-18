# 🚩 Module 1 — LLM APIs, Tools & First DevOps Agent

> **Move from understanding LLMs to building a controlled AI application.**

Module 0 explained the model. Module 1 now builds the first real application around it: provider call → structured output → tools → evidence → bounded agent loop → trusted RCA.

## 🎯 Learning Promise

By the end you can explain and build:

- hosted vs local LLM calls
- Python application setup and secret hygiene
- structured output + Pydantic
- tool/function calling
- host-controlled tool execution
- agent loop and state
- evidence preservation and provenance
- deterministic guardrails
- trusted DevOps RCA

## 🧠 Core Mental Model

```text
Incident
   ↓
Python Host
   ↓
Prompt + Context
   ↓
LLM
   ↓
Response / Tool Proposal
   ↓
Host Validation
   ↓
Known Tool
   ↓
Evidence
   ↓
Validated RCA
```

```text
LLM = reasoner
Host = controller
Tool = capability
Tool output = evidence
Schema = data contract
Policy = deterministic boundary
```

## 🧭 Lean Canonical Learning Path

| Unit | Canonical topic | Existing material used |
|---|---|---|
| 00 | [Roadmap & Mental Model](Lesson-00-Module-1-Roadmap-and-Mental-Model.md) | Roadmap |
| 01 | [UI vs API + application architecture](Lesson-01-ChatGPT-UI-vs-API.md) | Lesson 01 |
| 02 | [Environment + Secrets](Lesson-02-Development-Environment-and-Secrets.md) | Lesson 02 |
| 03 | [Hosted + Local LLM Setup](Lesson-03-OpenAI-Cloud-API-Setup.md) | Lessons 03–04 |
| 04 | [First Call + Tokens/Context](Lesson-05-First-API-Call-and-Response-Object.md) | Lessons 05–06 |
| 05 | [Structured Output + Validation](Lesson-07-Structured-Output-and-Validation.md) | Lesson 07 |
| 06 | [Tool Calling + Contracts](Lesson-08-Tool-Calling-Function-Calling.md) | Lesson 08 |
| 07 | [Bounded DevOps Agent + Evidence](Lesson-09-From-Tool-Calling-to-Basic-DevOps-Agent.md) | Lesson 09 + V1–V4 lab |
| 08 | [Complete Trusted-RCA Lab](A-Complete-Lab-Code.md) | Complete lab |

Reference troubleshooting/interview documents are supplemental, not additional mandatory chapters.

## 🛠️ Setup

Create the shared Python environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

For local LLM labs, install/start Ollama and use the model specified by the lesson. For hosted labs, place the provider credential in an environment variable.

```text
.env          ← local only, never commit
.gitignore    ← must exclude .env
```

Do not put credentials in prompts or evidence context.

## 🧪 Practical Spine

```text
V1 Hosted LLM Call
 ↓
V2 Local/Ollama Call
 ↓
V3 Context Experiment
 ↓
V4 Structured Output
 ↓
V5 Tool Request
 ↓
V6 Agent V1
 ↓
V7 Agent V2
 ↓
V8 Agent V3
 ↓
V9 Agent V4
 ↓
V10 Real Evidence + Trusted RCA
```

Recurring scenario:

```text
Terraform Apply started
      ↓
NSG rule aks-subnet-allow removed
      ↓
AKS connectivity validation failed
      ↓
Deployment failed
```

The model must never turn its confidence into authority.

## 🔐 Non-Negotiable Rules

```text
1. Model output is untrusted analysis.
2. Tool calls are untrusted proposals.
3. Host validates tool name, arguments and target.
4. Tool output needs provenance before becoming evidence.
5. Structured output validates shape, not truth.
6. No evidence → no forced RCA.
7. Agent loops need budgets and stop conditions.
8. Read-only first; risky writes require policy + authorization + approval.
```

## 🔗 Module Boundaries

```text
M0 → What an LLM is and why it is probabilistic
M1 → How to build a controlled AI application
M2 → How to engineer its prompts/context deeply
M3 → How the API/Python plumbing works underneath
```

M1 deliberately does **not** reteach the full REST/HTTP/JSON/auth curriculum. That depth belongs to M3.

## ✅ Completion Test

Explain without notes:

- hosted vs local LLM
- structured output vs free text
- tool request vs tool execution
- why tool arguments are untrusted
- evidence vs model inference
- why no evidence should block forced RCA
- where deterministic policy belongs

## 🔗 Continue

➡️ [Module 2 — Prompt & Context Engineering](../Module-2/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
