# 🚩 START HERE — Beginner Guide

> **Zero AI knowledge se Production DevOps AI Assistant tak ka recommended path.**

Agar aap AI/LLM/Agentic AI me bilkul beginner ho, to repo ko random files ki tarah mat padho. Is guide ko pehle follow karo.

---

# 1. Is Repository ka Goal Kya Hai?

Ye repository aapko sirf ChatGPT use karna nahi sikhati. Goal hai:

```text
AI Fundamentals
→ LLM Understanding
→ Prompting
→ APIs
→ Local LLM
→ Tool Calling
→ Evidence Grounding
→ Embeddings
→ RAG
→ LangChain
→ MCP
→ Stateful Agents
→ Multi-Agent Systems
→ Security & Evaluation
→ Enterprise Azure Architecture
→ Production DevOps AI Assistant
```

Final system ka mental model:

```text
Incident
  ↓
Collect trusted evidence
  ↓
Retrieve approved knowledge
  ↓
Coordinate agents
  ↓
Generate grounded RCA
  ↓
Validate claims
  ↓
Recommend safe action
  ↓
Policy / Authorization / Approval
  ↓
Controlled execution
```

---

# 2. Kya Mujhe AI Pehle Se Aana Chahiye?

No.

Minimum prerequisites:

- basic computer usage
- terminal/PowerShell ka basic idea
- Python ka sirf basic syntax later modules me helpful hai
- DevOps knowledge helpful hai but AI concepts ke liye mandatory nahi

Module 0 AI ko zero se explain karta hai.
Module 3 minimal Python/API concepts ko context ke saath explain karta hai.

---

# 3. Do Learning Tracks — Local LLM ya OpenAI

Repo me do provider paths support kiye jaate hain.

## Track A — Local / Ollama

Best when:

- paid API avoid karna ho
- experiments local machine par karne ho
- data machine se bahar nahi bhejna ho
- model quality se zyada concept learning important ho

Recommended learning model:

```powershell
ollama pull qwen3:4b
```

Alternative lightweight model:

```powershell
ollama pull gemma3:1b
```

Default local API:

```text
http://localhost:11434/api
```

## Track B — OpenAI API

Best when:

- stronger hosted model use karna ho
- provider/API integration practice karni ho
- production-style hosted model behavior compare karna ho

Environment variable:

```powershell
$env:OPENAI_API_KEY="your-key"
```

or `.env`:

```env
OPENAI_API_KEY=your-key
OPENAI_MODEL=gpt-5.6-luna
```

> API usage may require billing/credits. Never commit your real API key.

Detailed setup: [`MODEL-PROVIDERS.md`](MODEL-PROVIDERS.md)

---

# 4. Recommended Windows Setup

From PowerShell:

```powershell
git clone https://github.com/ecriahb/agentic-ai-agents.git
cd agentic-ai-agents

python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

For shared dual-provider examples:

```powershell
pip install -r shared/requirements.txt
```

For a module practical, install that module's requirements too:

```powershell
pip install -r Module-5/examples/requirements.txt
```

---

# 5. Verify Your Local LLM Before Course Labs

Check Ollama:

```powershell
ollama --version
ollama list
```

Run a model manually:

```powershell
ollama run qwen3:4b
```

Then verify API:

```powershell
python shared/provider_smoke_test.py
```

Default provider is Ollama unless `LLM_PROVIDER=openai` is set.

---

# 6. Verify OpenAI Before Course Labs

Install dependencies:

```powershell
pip install -r shared/requirements.txt
```

Set variables:

```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="your-key"
$env:OPENAI_MODEL="gpt-5.6-luna"
```

Run:

```powershell
python shared/provider_smoke_test.py
```

Expected shape:

```text
Provider: openai
Model: gpt-5.6-luna
Answer: ...
```

Never print or log the API key.

---

# 7. Module-by-Module Learning Path

## Module 0 — AI & LLM Foundation

Start here if you do not know:

- AI vs ML vs Deep Learning vs LLM
- token prediction
- transformer/attention
- context window
- hallucination
- prompts

No API required.

---

## Module 1 — APIs, Local Models, Tools & First DevOps Agent

You learn:

- ChatGPT UI vs API
- OpenAI API basics
- Ollama/local model
- structured output
- tool calling
- agent loop
- real evidence
- trusted RCA

This module deliberately shows both hosted and local model paths.

---

## Module 2 — Prompt & Context Engineering

You learn how to design:

```text
Role
+ Context
+ Task
+ Constraints
+ Output Contract
+ Evaluation
```

Run the same prompt against both providers to understand that prompt design is provider-independent.

---

## Module 3 — APIs & Minimal Python

You learn:

- HTTP
- REST
- JSON
- environment variables
- authentication
- Python functions/errors
- LLM API calls

Do not try to become a Python expert here. Learn only what the AI application needs.

---

## Module 4 — Embeddings & Vector Databases

You learn:

```text
Text → Embedding → Vector → Similarity → Retrieval
```

Local path uses Sentence Transformers.
OpenAI path demonstrates hosted embeddings separately.

Important:

```text
Embedding model != LLM
Vector DB != LLM
Similarity score != factual confidence
```

---

## Module 5 — RAG

You combine retrieval with generation:

```text
Question
→ Retrieve evidence/reference
→ Build context
→ LLM
→ Validate
→ Answer + Sources
```

Compare the same retrieved context with Ollama and OpenAI generation.

---

## Module 6 — LangChain / Orchestration

You learn reusable composition:

```text
Prompt → Retriever → LLM → Parser → Validator
```

Framework does not create intelligence. It orchestrates components.

---

## Module 7 — MCP

You learn standardized capability connectivity:

```text
Host → MCP Client → MCP Server → Tools/Resources
```

MCP is provider-independent. The final reasoning step can use either local or hosted LLM.

---

## Module 8 — Stateful Agents / LangGraph

You learn:

- explicit state
- nodes and edges
- conditional routing
- loops
- checkpoints
- human approval

State machine behavior must remain safe regardless of model provider.

---

## Module 9 — Multi-Agent Systems

You build specialist agents:

```text
Supervisor
├─ Pipeline Specialist
├─ Terraform Specialist
└─ AKS Specialist
```

Agent count does not create truth. Evidence contracts do.

---

## Module 10 — Security, Evaluation & Red Teaming

You learn to attack your own agent safely:

- prompt injection
- tool abuse
- secret leakage
- RAG poisoning
- MCP trust
- multi-agent contamination
- deterministic policy
- trajectory evaluation
- release gates

---

## Module 11 — Enterprise Production Architecture

You move from local app to enterprise design:

- identity
- RBAC
- networking
- private endpoints
- DNS
- egress
- runtime choice
- state/data layer
- scaling
- HA/DR
- observability
- CI/CD
- governance

---

## Module 12 — Final Capstone

Everything is combined:

```text
Trusted Evidence
+ RAG
+ MCP
+ Stateful Graph
+ Multi-Agent Team
+ Grounded RCA
+ Security Policy
+ Evals
+ Approval
+ Production Architecture
```

---

# 8. How to Study Every Lesson

Do not only read Markdown.

Use this loop:

```text
1. Read lesson goal
2. Understand English definition
3. Read Hinglish explanation
4. Draw mental model yourself
5. Run practical
6. Change one input
7. Break the practical intentionally
8. Understand the error
9. Read common mistakes
10. Answer interview questions without looking
11. Do homework
12. Move to next lesson
```

---

# 9. How to Use V1 → V10 Labs

Later modules use incremental versions.

Do not jump directly to V10.

Example:

```text
V1 = simplest concept
V2 = one more feature
V3 = validation
V4 = evidence
...
V10 = integrated project
```

The difference between versions is the lesson.

---

# 10. Core Trust Rules — Memorize These

```text
LLM output != truth
Tool request != permission
Tool schema != authorization
Retrieved document != current incident fact
Memory != evidence
Structured output != factual validation
Similarity score != confidence
MCP discovery != approval
Agent message != evidence
Human approval != identity/RBAC
```

Production rule:

```text
No evidence → no forced RCA
```

---

# 11. Beginner Troubleshooting

## `python` not found

Install Python and restart terminal.

Check:

```powershell
python --version
```

## Virtual environment activation blocked

PowerShell may require execution-policy adjustment. Prefer a user-scoped safe policy based on your organization rules.

## `ModuleNotFoundError`

Install the module requirements:

```powershell
pip install -r Module-X/examples/requirements.txt
```

## Ollama connection refused

Check:

```powershell
ollama list
```

Start/run Ollama and confirm port `11434` is available locally.

## Ollama model not found

```powershell
ollama pull qwen3:4b
```

or set:

```powershell
$env:OLLAMA_MODEL="your-installed-model"
```

## OpenAI authentication error

Check that `OPENAI_API_KEY` exists in your current shell or `.env`.

Do not paste secrets into code.

## OpenAI billing/rate error

This is not a Python logic error. Hosted API access depends on your account/billing/rate limits.

## Output is different every run

LLMs are probabilistic. The course validates contracts/evidence/policies instead of depending on exact wording.

---

# 12. Local vs OpenAI — What Should a Beginner Choose?

Recommended sequence:

```text
First learn with Ollama
        ↓
Understand concepts without API cost
        ↓
Run provider-parity examples
        ↓
Switch to OpenAI
        ↓
Compare quality / latency / behavior
        ↓
Keep application contracts provider-independent
```

---

# 13. What "Course Complete" Means

Reading all Markdown files is not enough.

You should be able to explain:

```text
Why hallucination happens
Why evidence is external to the model
Why tool execution belongs to host code
Why RAG does not prove current incident facts
Why state must be explicit
Why agents need loop limits
Why multi-agent majority vote is unsafe
Why MCP needs authorization
Why writes need approval
Why security evals inspect trajectories
Why production architecture needs identity/network/state/observability
```

And you should be able to run the Module 12 capstone safely.

---

# 14. Recommended First Action

If you are completely new:

```text
Open Module-0/README.md
→ Read Lesson 00
→ Continue sequentially
```

If your environment is not ready:

```text
Read MODEL-PROVIDERS.md
→ configure Ollama or OpenAI
→ run shared/provider_smoke_test.py
```

🚩 **Start simple. Run everything. Trust evidence, not model confidence.**