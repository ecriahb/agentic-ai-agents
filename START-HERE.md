# 🚩 START HERE — Beginner Guide

> **Zero AI knowledge se Production DevOps AI Assistant tak ka recommended path.**

Agar aap AI/LLM/Agentic AI me bilkul beginner ho, to repo ko random files ki tarah mat padho. Is guide ko pehle follow karo.

## Five Phases, One Project

Repo ko 13 alag courses ki tarah mat padho. Ye AI engineering ka 5-phase path hai. DevOps incident sirf running case study hai; har phase tumhari AI system capability upgrade karta hai:

```text
Phase 1  Understand AI             Modules 0–2
Phase 2  Build the first assistant Modules 3–5
Phase 3  Build agents              Modules 6–9
Phase 4  Secure and operate        Modules 10–11
Phase 5  Ship the platform         Module 12
```

Phase complete tab maana jayega jab us AI capability ko explain, break, debug aur demonstrate kar sako.

## Most Important Hands-On Guide

Theory read karne ke saath **har phase ka practical outcome mandatory** hai. Phase ke andar modules sirf next engineering layer add karte hain:

👉 [`PRACTICALS-INDEX.md`](PRACTICALS-INDEX.md)

Har internal module ke andar dedicated `PRACTICAL-ROADMAP.md` hai:

```text
ZERO → BASIC → BUILD → CONTROL → FAILURE DRILL → ADVANCED → PROVIDER PARITY → V10/HERO
```

A practical tab complete nahi maana jayega jab script sirf run ho jaye. Learner ko explain karna hoga:
- previous version se kya change hua
- ye version kis problem ko solve karta hai
- kya fail ho sakta hai
- model-driven aur deterministic part kaunsa hai
- evidence/source kya hai
- safety/policy control kaha hai
- next version kyun chahiye

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
OPENAI_MODEL=your-supported-model
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
$env:OPENAI_MODEL="your-supported-model"
```

Run:

```powershell
python shared/provider_smoke_test.py
```

Expected shape:

```text
Provider: openai
Model: <configured-model>
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

Practical: [`Module-0/PRACTICAL-ROADMAP.md`](Module-0/PRACTICAL-ROADMAP.md)

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

Practical: [`Module-1/PRACTICAL-ROADMAP.md`](Module-1/PRACTICAL-ROADMAP.md)

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

Practical: [`Module-2/PRACTICAL-ROADMAP.md`](Module-2/PRACTICAL-ROADMAP.md)

---

## Module 3 — APIs & Minimal Python

You learn HTTP, REST, JSON, secrets, functions/errors and LLM API calls.

Practical: [`Module-3/PRACTICAL-ROADMAP.md`](Module-3/PRACTICAL-ROADMAP.md)

---

## Module 4 — Embeddings & Vector Databases

```text
Text → Embedding → Vector → Similarity → Retrieval
```

Practical: [`Module-4/PRACTICAL-ROADMAP.md`](Module-4/PRACTICAL-ROADMAP.md)

---

## Module 5 — RAG

```text
Question → Retrieve → Context → LLM → Validate → Answer + Sources
```

Practical: [`Module-5/PRACTICAL-ROADMAP.md`](Module-5/PRACTICAL-ROADMAP.md)

---

## Module 6 — LangChain / Orchestration

Practical: [`Module-6/PRACTICAL-ROADMAP.md`](Module-6/PRACTICAL-ROADMAP.md)

---

## Module 7 — MCP

Practical: [`Module-7/PRACTICAL-ROADMAP.md`](Module-7/PRACTICAL-ROADMAP.md)

---

## Module 8 — Stateful Agents / LangGraph

Practical: [`Module-8/PRACTICAL-ROADMAP.md`](Module-8/PRACTICAL-ROADMAP.md)

---

## Module 9 — Multi-Agent Systems

Practical: [`Module-9/PRACTICAL-ROADMAP.md`](Module-9/PRACTICAL-ROADMAP.md)

---

## Module 10 — Security, Evaluation & Red Teaming

Practical: [`Module-10/PRACTICAL-ROADMAP.md`](Module-10/PRACTICAL-ROADMAP.md)

---

## Module 11 — Enterprise Production Architecture

Practical: [`Module-11/PRACTICAL-ROADMAP.md`](Module-11/PRACTICAL-ROADMAP.md)

---

## Module 12 — Final Capstone

Practical: [`Module-12/PRACTICAL-ROADMAP.md`](Module-12/PRACTICAL-ROADMAP.md)

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

# 8. How to Study Every Lesson + Practical

Use this loop:

```text
1. Read lesson goal
2. Understand English definition
3. Read Hinglish explanation
4. Draw mental model yourself
5. Open module PRACTICAL-ROADMAP.md
6. Run/do current practical stage
7. Change one input
8. Break the practical intentionally
9. Predict expected failure
10. Compare actual behavior
11. Explain what control caught the failure
12. Answer interview questions without looking
13. Do homework
14. Move to next stage
```

---

# 9. Never Jump Directly to V10

```text
V1 = simplest concept
V2 = one more feature
V3 = validation / contract
...
V10 = integrated project
```

The **difference between versions is the lesson**.

Every module follows the same learning philosophy even when the exact files differ.

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
```powershell
python --version
```

## `ModuleNotFoundError`
```powershell
pip install -r Module-X/examples/requirements.txt
```

## Ollama connection refused
```powershell
ollama list
```

## Ollama model not found
```powershell
ollama pull qwen3:4b
```

or:
```powershell
$env:OLLAMA_MODEL="your-installed-model"
```

## OpenAI authentication error
Check `OPENAI_API_KEY` in current shell or `.env`. Never paste secrets into code.

## OpenAI billing/rate error
Hosted API access depends on account/billing/rate limits; this is not automatically a Python logic bug.

## Output differs every run
LLMs are probabilistic. Validate evidence/contracts/policies instead of depending on exact wording.

---

# 12. Recommended Provider Learning Sequence

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

Reading Markdown or successfully running scripts is not enough.

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

And you should be able to run/explain the Module 12 capstone safely.

---

# 14. Recommended First Action

```text
Open Module-0/README.md
→ Open Module-0/PRACTICAL-ROADMAP.md
→ Read Lesson 00
→ Do V1
→ Continue sequentially
```

If environment is not ready:

```text
Read PREREQUISITES.md
→ Read MODEL-PROVIDERS.md
→ configure Ollama or OpenAI
→ run shared/preflight.py
→ run shared/provider_smoke_test.py
```

🚩 **Start simple. Run everything. Break it intentionally. Trust evidence, not model confidence.**
