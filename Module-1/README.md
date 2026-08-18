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

### Reference, not mandatory repeats

The detailed troubleshooting, interview and official-reference documents remain available:

- `B-Troubleshooting-Playbook.md`
- `C-Interview-and-Revision-Sheet.md`
- `D-Official-References.md`

Module 3 owns the deeper HTTP/REST/JSON/auth/error-plumbing explanations. Module 1 only teaches enough of those concepts to build the first agent.

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

## 🔥 Recurring DevOps Evidence

```text
Terraform Apply started
      ↓
NSG rule aks-subnet-allow removed
      ↓
AKS connectivity validation failed
      ↓
Deployment failed
```

The model must never be allowed to turn its own confidence into authority.

## 🔐 Non-Negotiable Rules

```text
1. We use an existing LLM; we are not training one.
2. Model output is untrusted analysis.
3. Tool calls are untrusted proposals.
4. Host validates tool name, arguments and target.
5. Tool output needs provenance before becoming evidence.
6. Structured output validates shape, not truth.
7. No evidence → no forced RCA.
8. Agent loops need budgets and stop conditions.
9. Read-only first; risky writes require policy + authorization + approval.
```

## 🔗 Boundary with Module 2

```text
Module 1
Build the controlled application
        ↓
Module 2
Engineer the instructions/context that drive its reasoning
```

Module 1 introduces prompts only as needed for the application. **Module 2 owns deep prompt engineering.**

## ✅ Completion Test

Explain without notes:

- hosted vs local LLM
- structured output vs free text
- tool request vs tool execution
- why tool arguments are untrusted
- evidence vs model inference
- why no evidence should block forced RCA
- where deterministic policy belongs

> **Outcome:** a learner can move from an LLM call to a controlled, evidence-grounded DevOps agent.
