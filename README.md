# 🚩 Agentic AI for Azure DevOps Engineers

> **From ChatGPT User → AI Engineer → Agentic DevOps Builder**

This repository is a hands-on learning journey for understanding and building **Agentic AI systems for real DevOps use cases**.

The course does not jump directly into agents. It follows a deliberate progression:

```text
AI Fundamentals
      ↓
LLM Fundamentals
      ↓
Prompting & Safety
      ↓
AI APIs / Local Models
      ↓
Structured Output
      ↓
Tool Calling
      ↓
Agent Loop
      ↓
Evidence Grounding
      ↓
Real Tools
      ↓
Trusted RCA
      ↓
Production-Grade Agentic DevOps Systems
```

---

# 🎯 Repository Goal

The long-term target is to build a **DevOps AI Assistant** that can safely investigate engineering incidents using trusted evidence.

Example target flow:

```text
Pipeline Failure
      ↓
Collect Trusted Evidence
      ↓
Analyze Logs / Terraform / AKS / Metrics
      ↓
Generate Evidence-Grounded RCA
      ↓
Recommend Fix
      ↓
Human Approval
      ↓
Controlled Action
```

The important principle throughout the repository is:

> **LLM reasoning must be grounded in real evidence, validated by application logic, and controlled by safety guardrails.**

---

# 📚 Course Progress

| Module | Focus | Status |
|---|---|---|
| [Module 0](Module-0/README.md) | AI & LLM Foundation | ✅ Completed |
| [Module 1](Module-1/README.md) | APIs, Local Models, Tools & First DevOps Agent | ✅ Completed |

---

# 🧠 Module 0 — AI & LLM Foundation

## [Open Module 0](Module-0/README.md)

> **From ChatGPT User → AI Thinker**

Module 0 builds the conceptual foundation before coding or tool integration.

You learn what an LLM actually is, how it generates text, why context matters, how hallucination happens, how prompts influence behavior, and why safety and verification are mandatory in production AI systems.

### Lesson Map

| No. | Lesson |
|---|---|
| 00 | [Orientation — The Beginning of an AI Engineer](Module-0/Lesson-00-Orientation.md) |
| 01 | [The AI Revolution](Module-0/Lesson-01-AI-Revolution.md) |
| 02 | [AI → ML → DL → LLM](Module-0/Lesson-02-AI-ML-DL-LLM.md) |
| 03 | [Next Token Prediction](Module-0/Lesson-03-Next-Token-Prediction.md) |
| 04 | [Transformer & Attention](Module-0/Lesson-04-Transformer-Attention.md) |
| 05 | [Context Window](Module-0/Lesson-05-Context-Window.md) |
| 06 | [Hallucination](Module-0/Lesson-06-Hallucination.md) |
| 07 | [Prompt Engineering](Module-0/Lesson-07-Prompt-Engineering.md) |
| 08 | [System Prompt vs User Prompt](Module-0/Lesson-08-System-vs-User-Prompt.md) |
| 09 | [Temperature](Module-0/Lesson-09-Temperature.md) |
| 10 | [Role Prompting](Module-0/Lesson-10-Role-Prompting.md) |
| 11 | [Zero-Shot, One-Shot & Few-Shot](Module-0/Lesson-11-Zero-One-Few-Shot.md) |
| 12 | [Structured Reasoning](Module-0/Lesson-12-Structured-Reasoning.md) |
| 13 | [AI Limitations & Safety](Module-0/Lesson-13-AI-Limitations-Safety.md) |
| 14 | [Grand Revision + Mini Project](Module-0/Lesson-14-Grand-Revision-Mini-Project.md) |

### Module 0 Mental Model

```text
AI
 ↓
Machine Learning
 ↓
Deep Learning
 ↓
LLM
 ↓
Next Token Prediction
 ↓
Transformer + Attention
 ↓
Context
 ↓
Prompting
 ↓
Grounding + Verification
 ↓
Safety + Human Approval
```

### Module 0 Outcome

By the end of Module 0, you understand:

- AI vs ML vs Deep Learning vs LLM
- next-token prediction
- Transformer and Attention concepts
- context windows
- hallucination
- prompt engineering
- system vs user prompts
- temperature
- role prompting
- zero-shot / one-shot / few-shot prompting
- structured reasoning
- AI limitations
- safety, verification and human approval

---

# ⚙️ Module 1 — LLM APIs, Local Models, Tools & First DevOps Agent

## [Open Module 1](Module-1/README.md)

> **From AI Thinker → AI Application Developer**

Module 1 turns the concepts from Module 0 into working code.

The progression is:

```text
ChatGPT UI vs API
      ↓
Development Environment
      ↓
First Real AI API Call
      ↓
Local AI with Ollama
      ↓
Structured Output
      ↓
Tool Calling
      ↓
Multiple DevOps Tools
      ↓
Agent Loop
      ↓
State + Grounding
      ↓
Fake Tool → Real Tool
      ↓
Real Evidence
      ↓
Trusted RCA
```

### Lesson Map

| No. | Lesson |
|---|---|
| 01 | [ChatGPT UI vs API](Module-1/Lesson-01-ChatGPT-UI-vs-API.md) |
| 02 | [Development Environment & Secrets](Module-1/Lesson-02-Development-Environment-and-Secrets.md) |
| 03 | [Our First Real AI API Call](Module-1/Lesson-03-Our-First-Real-AI-API-Call.md) |
| 04 | [Local AI with Ollama](Module-1/Lesson-04-Local-AI-with-Ollama.md) |
| 05 | [Fake Tool → Real Tool](Module-1/Lesson-05-Fake-Tool-to-Real-Tool.md) |

---

# 🧪 Module 1 Hands-On Journey

All runnable examples are available in:

## [Module 1 Practical Examples](Module-1/examples/README.md)

The practical progression includes:

```text
First AI Call
   ↓
Local Ollama Call
   ↓
Structured Output
   ↓
Basic Tool Calling
   ↓
DevOps Agent V1
   ↓
DevOps Agent V2
   ↓
DevOps Agent V3
   ↓
DevOps Agent V4
```

Core runnable examples:

| Stage | File |
|---|---|
| First API Call | [01_first_ai_call.py](Module-1/examples/01_first_ai_call.py) |
| Local Ollama | [02_ollama_ai_call.py](Module-1/examples/02_ollama_ai_call.py) |
| Structured Output | [03_structured_output.py](Module-1/examples/03_structured_output.py) |
| Tool Calling | [04_tool_call_basic.py](Module-1/examples/04_tool_call_basic.py) |
| Agent V1 | [devops_agent_v1.py](Module-1/examples/devops_agent_v1.py) |
| Agent V2 | [devops_agent_v2.py](Module-1/examples/devops_agent_v2.py) |
| Agent V3 | [devops_agent_v3.py](Module-1/examples/devops_agent_v3.py) |
| Agent V4 | [devops_agent_v4.py](Module-1/examples/devops_agent_v4.py) |

---

# 🔥 Lesson 05 Real Tool Practical

One of the most important Module 1 practicals is the transition from a fake/hard-coded tool to a real local evidence source.

## [Open Full Real Tool → Trusted RCA Practical](Module-1/examples/lesson-05-real-tool-practical/README.md)

Exact learning sequence:

```text
pipeline.log
   ↓
Real File-Reading Tool
   ↓
Qwen Tool Call
   ↓
No-Tool Guardrail
   ↓
Preserved Evidence
   ↓
V3 Evidence-Only Reporting
   ↓
V4 Pydantic Validation
   ↓
Tool-Argument Hallucination Discovered
   ↓
Tool Allowlist
   ↓
Argument Validation
   ↓
Deterministic Impact Extraction
   ↓
Evidence Support Validation
   ↓
Confidence Policy
   ↓
FINAL TRUSTED RCA
```

### Practical Files

| Stage | File |
|---|---|
| Real Evidence | [pipeline.log](Module-1/examples/lesson-05-real-tool-practical/logs/pipeline.log) |
| Real Tool V1 | [real_tool_qwen_v1.py](Module-1/examples/lesson-05-real-tool-practical/real_tool_qwen_v1.py) |
| No-Tool Guardrail | [real_tool_qwen_v2_guardrail.py](Module-1/examples/lesson-05-real-tool-practical/real_tool_qwen_v2_guardrail.py) |
| Evidence-Only V3 | [real_tool_qwen_v3.py](Module-1/examples/lesson-05-real-tool-practical/real_tool_qwen_v3.py) |
| Pydantic V4 | [real_tool_qwen_v4.py](Module-1/examples/lesson-05-real-tool-practical/real_tool_qwen_v4.py) |
| Final Hardened Version | [real_tool_qwen_v4_final.py](Module-1/examples/lesson-05-real-tool-practical/real_tool_qwen_v4_final.py) |

---

# 🔍 DevOps Incident Used in the Practical

The real-tool lab reads evidence from `pipeline.log`:

```text
Pipeline started
      ↓
Terraform init completed
      ↓
Terraform plan completed
      ↓
Terraform apply started
      ↓
NSG rule aks-subnet-allow was removed
      ↓
AKS subnet connectivity validation failed
      ↓
Deployment failed during Terraform Apply
```

The important learning is not merely producing an RCA.

The application must distinguish between:

```text
What the model thinks
        vs
What the evidence proves
```

So the final architecture uses application-level validation before trusting the result.

---

# 🏗️ Current Agent Architecture

```text
                    USER / INCIDENT
                          │
                          ▼
                       LLM
                  Investigation Brain
                          │
                    requests tool
                          │
                          ▼
                 Tool Contract Check
                          │
                 Tool Allowlist Check
                          │
                Argument Validation
                          │
                          ▼
                  Python Application
                          │
                    executes tool
                          │
                          ▼
                  Trusted Evidence
                          │
                          ▼
                    evidence_log
                          │
                          ▼
               Evidence-Only Reporter
                          │
                          ▼
                  Pydantic Schema
                          │
                          ▼
              Evidence Claim Validation
                          │
                          ▼
           Deterministic Impact Validation
                          │
                          ▼
                 Confidence Policy
                          │
                          ▼
                    TRUSTED RCA
```

---

# 🧠 Core Principles Learned So Far

```text
1. LLM is the brain, not the executor.
2. Python/application code executes tools.
3. A tool request from an LLM is untrusted input.
4. Tool name and tool arguments must both be validated.
5. Tool output is evidence.
6. Evidence must be preserved outside model memory.
7. No evidence should mean no RCA.
8. Structured output makes responses machine-consumable.
9. Pydantic validates structure, not factual truth.
10. Final claims must be checked against evidence.
11. Confirmed impact must not be invented by the model.
12. Confidence can be controlled by application policy.
13. Real integrations require authentication and authorization.
14. Least privilege and read-only-first reduce risk.
15. Human approval should protect destructive/remediation actions.
```

---

# 🛠️ Technologies Used So Far

```text
Python
OpenAI API concepts
Ollama
Gemma
Qwen
Pydantic
Tool / Function Calling
Agent Loops
Structured Output
Local Log Files
DevOps Incident Investigation
AKS concepts
Terraform concepts
Azure Networking / NSG concepts
```

---

# 🎓 Learning Style

The course is maintained lesson-by-lesson with a practical DevOps focus.

Each topic aims to include:

- simple Hinglish explanation
- concise English definition
- mental model / architecture flow
- DevOps or office example
- practical code
- common confusion / mistakes
- interview-oriented points
- revision-friendly notes
- connection to the next topic

---

# 🚀 Repository Learning Path

If you are starting from the beginning, follow this order:

```text
START
  │
  ▼
Module 0
AI & LLM Foundation
  │
  ▼
Prompting + Hallucination + Safety
  │
  ▼
Module 1
AI APIs + Local Models
  │
  ▼
Structured Output
  │
  ▼
Tool Calling
  │
  ▼
Agent Loop
  │
  ▼
Evidence Grounding
  │
  ▼
Real Tools
  │
  ▼
Guardrails + Validation
  │
  ▼
Trusted DevOps RCA
```

---

# ✅ Current Repository Milestone

At the end of Module 1, the repository has progressed from:

```text
"Ask an LLM a question"
```

to:

```text
Incident
  ↓
LLM decides what evidence is needed
  ↓
Application validates the tool request
  ↓
Python collects real evidence
  ↓
Evidence is preserved
  ↓
LLM creates structured analysis
  ↓
Application validates claims
  ↓
Trusted RCA
```

This is the foundation required before moving toward larger multi-tool, multi-step and production-grade Agentic AI systems.

---

🚩 **Jai Bajrangbali — Learn • Build • Automate • Impact**
