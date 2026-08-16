# 🚩 Jai Bajrangbali!

# Module 1 — LLM APIs, Local Models, Tools & First DevOps Agent

> **From ChatGPT User → AI Application Developer**

Module 0 me humne LLM fundamentals samjhe. Module 1 me hum existing LLM ko Python application ke andar use karke **API calls, local AI, structured output, tool calling aur DevOps agent flow** build karte hain.

> **Important:** Ye README ab actual live-class sequence ko follow karta hai. Extra lesson numbering use nahi ki gayi hai.

---

## 🎯 Module 1 Learning Promise

Module ke end tak aap samjhoge:

- ChatGPT UI vs API
- Python AI development environment
- virtual environment aur secret management
- API, SDK, API key, client, request aur response
- first real AI API call
- OpenAI cloud API billing/credential behavior
- Ollama par local zero-cost AI experimentation
- structured output + Pydantic validation
- tool calling / function calling
- `LLM decides; Python executes`
- agent loop
- state and evidence grounding
- basic DevOps investigation agent
- `devops_agent_v1.py` → `v4.py` evolution
- fake tool se real DevOps integration ka architecture
- authentication, authorization, least privilege aur human approval

---

## 🧠 Core Mental Model

```text
LLM = Brain
API = Communication Channel
Python Application = Controller
Tool = Hand
Tool Result = Evidence
State = Collected Investigation Memory
Structured Output = Data Contract
Agent Loop = Decide → Act → Observe → Repeat
```

---

# 📚 Actual Live-Class Lesson Sequence

## 1. [Lesson 01 — ChatGPT UI vs API](Lesson-01-ChatGPT-UI-vs-API.md)

Foundation:

```text
ChatGPT UI
   vs
AI API
```

We understand how an end user talks to ChatGPT versus how a software application talks to an AI model.

---

## 2. [Lesson 02 — AI Development Environment Setup](Lesson-02-Development-Environment-and-Secrets.md)

Hands-on setup:

```text
Python
 ↓
venv
 ↓
pip packages
 ↓
.env
 ↓
secret management
```

---

## 3. [Lesson 03 — Our First Real AI API Call](Lesson-03-Our-First-Real-AI-API-Call.md)

Core concepts:

```text
API
SDK
API Key
OpenAI Client
Request
Response
client.responses.create()
```

Important lesson:

> `create()` model create nahi karta; it asks an existing model to generate a response.

---

## 4. [Lesson 04 — Local AI with Ollama](Lesson-04-Local-AI-with-Ollama.md)

This is the major hands-on lesson.

```text
Ollama Local Model
       ↓
First Local AI Call
       ↓
Structured Output
       ↓
Tool Calling
       ↓
Multiple DevOps Tools
       ↓
Agent Loop
       ↓
DevOps Agent V1 → V4
```

Lesson 4 includes:

- `gemma3:1b`
- localhost API
- hallucination lesson
- structured RCA
- Pydantic/schema validation
- `get_aks_status`
- `get_terraform_changes`
- `get_pipeline_status`
- single/multiple tool calling
- agent loop
- state
- grounding
- V1/V2/V3/V4 evolution

---

## 5. [Lesson 05 — Fake Tool → Real Tool](Lesson-05-Fake-Tool-to-Real-Tool.md)

Final Module-1 transition:

```text
Fake / Hard-coded Tool
        ↓
Stable Tool Contract
        ↓
Real Azure / AKS / Pipeline / Terraform Source
        ↓
Normalized Evidence
        ↓
Grounded Agent Reasoning
```

Production concepts introduced:

- real integrations
- authentication
- authorization/RBAC
- least privilege
- read-only first
- error handling
- timeouts/retries
- audit logging
- human-in-the-loop approval

---

# 🧪 Practical Python Labs

All runnable code is inside [`examples/`](examples/README.md).

| Order | File | What You Learn |
|---|---|---|
| 01 | [`01_first_ai_call.py`](examples/01_first_ai_call.py) | First cloud AI API call |
| 02 | [`02_ollama_ai_call.py`](examples/02_ollama_ai_call.py) | Local Ollama through OpenAI-compatible client |
| 03 | [`03_structured_output.py`](examples/03_structured_output.py) | Schema-constrained / validated RCA output |
| 04 | [`04_tool_call_basic.py`](examples/04_tool_call_basic.py) | First tool request + Python execution |
| V1 | [`devops_agent_v1.py`](examples/devops_agent_v1.py) | Basic multi-tool agent loop |
| V2 | [`devops_agent_v2.py`](examples/devops_agent_v2.py) | Better tool arguments + correct environment/cluster mapping |
| V3 | [`devops_agent_v3.py`](examples/devops_agent_v3.py) | State + duplicate-call handling + evidence grounding |
| V4 | [`devops_agent_v4.py`](examples/devops_agent_v4.py) | Investigation separated from schema-validated RCA reporting |

Setup files:

- [`requirements.txt`](examples/requirements.txt)
- [`.env.example`](examples/.env.example)

---

# 🔁 V1 → V4 Evolution

## V1 — Basic Agent Loop

```text
User Issue
 ↓
LLM
 ↓
Tool Call
 ↓
Python Tool
 ↓
Tool Result
 ↓
LLM
 ↓
Final Answer
```

## V2 — Better Tool Arguments

```text
Correct environment / cluster mapping
+ typed arguments
+ consistent tool inputs
```

## V3 — State & Grounding

```text
Collect Evidence
 ↓
Preserve State
 ↓
Avoid Duplicate Calls
 ↓
Ground Final Answer in Evidence
```

## V4 — Investigation + Structured RCA

```text
Investigation Agent
      ↓
Application Evidence State
      ↓
Structured RCA Generator
      ↓
Schema Validation
      ↓
Human Approval
```

---

# 🔍 Practical DevOps Evidence Used

Our learning scenario converged on:

```text
Pipeline:
Failed during Terraform Apply

Terraform:
NSG rule allowing AKS subnet traffic was removed

AKS:
Degraded - network connectivity failures detected
```

Evidence-based RCA:

```text
Root Cause:
Terraform change removed a required NSG rule for AKS subnet traffic.

Impact:
AKS connectivity degraded and deployment failed.

Fix:
Restore the required NSG allow rule and validate related network configuration before redeployment.
```

---

# 🧠 Most Important Module 1 Principles

```text
1. We are NOT training a new LLM.
2. We use an existing LLM as the brain.
3. Python/application code executes tools.
4. LLM decides which tool is needed.
5. Tool output gives evidence.
6. State preserves evidence across steps.
7. Structured output makes results machine-consumable.
8. Fake tools are useful for learning/testing architecture.
9. Real tools require auth, RBAC, safety and observability.
10. Production remediation should be controlled and approved.
```

---

# ✅ Module 1 Completion Flow

```text
Lesson 1
ChatGPT UI vs API
        ↓
Lesson 2
AI Development Environment
        ↓
Lesson 3
First Real AI API Call
        ↓
Lesson 4
Ollama + Structured Output + Tool Calling + Agent Loop + V1–V4
        ↓
Lesson 5
Fake Tool → Real Tool
```

> **Module 1 outcome:** Aap sirf AI response lena nahi, balki AI ko application logic, tools, evidence aur controlled DevOps workflows ke andar use karna samajh chuke ho.
