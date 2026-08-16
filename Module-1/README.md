# 🚩 Jai Bajrangbali!

# Module 1 — LLM APIs, Local Models, Tools & First DevOps Agent

> **From ChatGPT User → AI Application Developer**

Module 0 me humne samjha tha ki LLM kaise behave karta hai. Module 1 me hum us intelligence ko software aur DevOps workflows ke andar use karna start karte hain.

## 🎯 Learning Promise

Is module ke end tak aap:

- ChatGPT UI aur API ka difference samjhoge
- Python environment aur secrets safely manage karoge
- OpenAI cloud API ka basic flow samjhoge
- Ollama ke through local zero-cost AI run karoge
- API response object aur token usage read karoge
- Structured output ko schema se validate karoge
- LLM tool calling implement karoge
- Basic multi-step DevOps investigation agent build karoge

## 🧠 Core Mental Model

```text
LLM = Brain
API = Communication Channel
Response = Result Parcel
Structured Output = Data Contract
Tool = Hand
Agent Loop = Brain repeatedly deciding what the hands should do
```

## 📚 Lessons

1. [Lesson 01 — ChatGPT UI vs API](Lesson-01-ChatGPT-UI-vs-API.md)
2. [Lesson 02 — Development Environment & Secret Management](Lesson-02-Development-Environment-and-Secrets.md)
3. [Lesson 03 — OpenAI Cloud API Setup](Lesson-03-OpenAI-Cloud-API-Setup.md)
4. [Lesson 04 — Zero-Cost Local AI with Ollama](Lesson-04-Local-AI-with-Ollama.md)
5. [Lesson 05 — First API Call & Response Object](Lesson-05-First-API-Call-and-Response-Object.md)
6. [Lesson 06 — Tokens, Cost & Context Engineering](Lesson-06-Tokens-Cost-and-Context.md)
7. [Lesson 07 — Structured Output & Validation](Lesson-07-Structured-Output-and-Validation.md)
8. [Lesson 08 — Tool Calling / Function Calling](Lesson-08-Tool-Calling.md)
9. [Lesson 09 — From Tool Calling to a Basic DevOps Agent](Lesson-09-Basic-DevOps-Agent.md)

## 🧪 Practical Python Labs

All runnable examples are inside [`examples/`](examples/README.md).

| Order | File | What You Learn |
|---|---|---|
| 01 | [`01_first_ai_call.py`](examples/01_first_ai_call.py) | OpenAI cloud API + Response object |
| 02 | [`02_ollama_ai_call.py`](examples/02_ollama_ai_call.py) | Local Ollama through OpenAI-compatible API |
| 03 | [`03_structured_output.py`](examples/03_structured_output.py) | Pydantic + schema-constrained RCA |
| 04 | [`04_tool_call_basic.py`](examples/04_tool_call_basic.py) | First external tool request/execution |
| V1 | [`devops_agent_v1.py`](examples/devops_agent_v1.py) | Basic multi-tool agent loop |
| V2 | [`devops_agent_v2.py`](examples/devops_agent_v2.py) | Correct environment/cluster mapping + typed arguments |
| V3 | [`devops_agent_v3.py`](examples/devops_agent_v3.py) | State, duplicate-call handling and evidence grounding |
| V4 | [`devops_agent_v4.py`](examples/devops_agent_v4.py) | Investigation separated from schema-validated RCA reporting |

Setup files:

- [`requirements.txt`](examples/requirements.txt)
- [`.env.example`](examples/.env.example)

## V1 → V4 Evolution

```text
V1
Basic Agent Loop
   ↓
V2
Better Tool Arguments + Correct prod Mapping
   ↓
V3
State + Evidence Preservation + Grounding
   ↓
V4
Investigation Agent
   ↓
Application Evidence State
   ↓
Structured RCA Generator
   ↓
Validation + Human Approval
```

## 🧪 What We Build

```text
Cloud API Call
      ↓
Local Ollama Call
      ↓
Response Inspection
      ↓
Structured RCA
      ↓
Single Tool Call
      ↓
Multi-tool DevOps Agent
```

Final learning agent evidence:

```text
Pipeline: Failed during Terraform Apply
Terraform: NSG rule allowing AKS subnet traffic was removed
AKS: Degraded - network connectivity failures detected
```

The goal is not to train a new LLM. We use an existing model as the brain and build an agent around it using **tools, state, validation and rules**.
