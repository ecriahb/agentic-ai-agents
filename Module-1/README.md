# 🚩 Jai Bajrangbali!

# Module 1 — LLM APIs, Local Models, Tools & First DevOps Agent

> **From ChatGPT User → AI Application Developer**

Module 0 me humne LLM fundamentals samjhe. Module 1 me hum existing LLM ko Python application ke andar use karke **API calls, local AI, structured output, tool calling aur DevOps agent flow** build karte hain.

> **Important:** Ye README actual live-class sequence ko follow karta hai.

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
- fake tool se real tool transition
- real `pipeline.log` evidence collection
- no-evidence/no-RCA guardrail
- evidence-only reporting
- tool allowlist + argument validation
- deterministic impact validation
- confidence policy
- final trusted RCA architecture

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

Lesson 05 starts with the architecture transition:

```text
Fake / Hard-coded Tool
        ↓
Stable Tool Contract
        ↓
Real Evidence Source
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

### ✅ Lesson 05 Live Practical

The exact practical sequence is preserved here:

**[Lesson 05 Real Tool → Trusted RCA Practical](examples/lesson-05-real-tool-practical/README.md)**

```text
pipeline.log
   ↓
real file-reading tool
   ↓
Qwen tool call
   ↓
no-tool guardrail
   ↓
evidence_log / preserved evidence
   ↓
V3 evidence-only reporting
   ↓
V4 Pydantic validation
   ↓
tool-argument hallucination discovered
   ↓
tool allowlist + argument validation
   ↓
deterministic impact extraction
   ↓
confidence policy
   ↓
FINAL TRUSTED RCA
```

This practical is important because it shows that **structured output alone is not enough**. The host application must also validate tool calls, evidence support, business claims and confidence.

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
| Real Tool V1 | [`real_tool_qwen_v1.py`](examples/lesson-05-real-tool-practical/real_tool_qwen_v1.py) | Read actual `pipeline.log` through a Qwen-requested tool |
| Guardrail V2 | [`real_tool_qwen_v2_guardrail.py`](examples/lesson-05-real-tool-practical/real_tool_qwen_v2_guardrail.py) | No-tool/no-evidence RCA block + evidence preservation |
| Real Tool V3 | [`real_tool_qwen_v3.py`](examples/lesson-05-real-tool-practical/real_tool_qwen_v3.py) | Evidence-only final reporting |
| Real Tool V4 | [`real_tool_qwen_v4.py`](examples/lesson-05-real-tool-practical/real_tool_qwen_v4.py) | `FinalRCA` Pydantic validation |
| Final | [`real_tool_qwen_v4_final.py`](examples/lesson-05-real-tool-practical/real_tool_qwen_v4_final.py) | Allowlist, argument validation, evidence validation, deterministic impact, confidence policy |

Setup files:

- [`requirements.txt`](examples/requirements.txt)
- [`.env.example`](examples/.env.example)

---

# 🔁 Agent Evolution

## Earlier V1 → V4

```text
Basic Agent Loop
   ↓
Better Tool Arguments
   ↓
State & Grounding
   ↓
Investigation + Structured RCA
```

## Lesson 05 Real Tool Evolution

```text
Hard-coded evidence
   ↓
Real pipeline.log
   ↓
Tool-request guardrail
   ↓
Preserved evidence
   ↓
Evidence-only reporter
   ↓
Pydantic schema
   ↓
Tool-call contract validation
   ↓
Evidence/business validation
   ↓
Deterministic controls
   ↓
Trusted RCA
```

---

# 🔍 Real Practical Evidence — 16 Aug 2026

```text
2026-08-16 10:02:11 - Pipeline started
2026-08-16 10:02:45 - Terraform init completed
2026-08-16 10:03:18 - Terraform plan completed
2026-08-16 10:04:01 - Terraform apply started
2026-08-16 10:04:37 - ERROR:
Network Security Group rule aks-subnet-allow was removed.
2026-08-16 10:04:41 - ERROR:
AKS subnet connectivity validation failed.
2026-08-16 10:04:45 - Deployment failed during Terraform Apply.
```

Evidence-grounded conclusion:

```text
Likely Root Cause:
The aks-subnet-allow NSG rule was removed and AKS subnet connectivity validation then failed.

Confirmed Impact:
AKS subnet connectivity validation failed and the deployment failed during Terraform Apply.

Recommended Fix:
Restore/correct the required NSG rule, validate subnet connectivity, review the Terraform change, and redeploy after validation.

Confidence:
Medium under the practical policy because the current investigation contains only one evidence source.
```

---

# 🧠 Most Important Module 1 Principles

```text
1. We are NOT training a new LLM.
2. We use an existing LLM as the brain.
3. Python/application code executes tools.
4. LLM decides which tool is needed, but the host validates the request.
5. Tool output gives evidence.
6. State/evidence_log preserves authoritative observations.
7. Structured output makes results machine-consumable.
8. Pydantic validates structure, not factual truth.
9. Tool name and tool arguments both require validation.
10. No evidence should mean no RCA.
11. Final impact should be evidence-supported, not model-invented.
12. Confidence can be controlled by application policy.
13. Real tools require auth, RBAC, safety and observability.
14. Production remediation should be controlled and approved.
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
Fake Tool → Real Tool → Real Evidence → Trusted RCA
```

> **Module 1 outcome:** Aap sirf AI response lena nahi, balki AI ko application logic, tools, real evidence, validation aur controlled DevOps workflows ke andar safely use karna samajh chuke ho.
