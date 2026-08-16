# Module 1 — Zero-to-Hero Practical Roadmap

> **Canonical lesson alignment:** 0 Roadmap → 1 UI/API → 2 Environment → 3 OpenAI Setup → 4 Ollama → 5 First Call → 6 Tokens/Context → 7 Structured Output → 8 Tools → 9 Basic Agent → A Complete Lab.

## Setup

```powershell
cd Module-1/examples
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Choose provider path:

```text
OpenAI hosted → OPENAI_API_KEY + available model
Ollama local  → Ollama running + installed model
```

---

# Before V1 — Lessons 0–4

Do not start V1 blindly. First complete:

```text
Lesson 0 → understand full architecture
Lesson 1 → UI vs API
Lesson 2 → create venv + secrets
Lesson 3 → configure OpenAI path
Lesson 4 → configure Ollama path
```

Pass condition: both provider architectures can be explained even if only one provider is actually available to you.

---

## V1 — First Hosted/OpenAI LLM Call
**Lesson:** 5 — First API Call & Response Object  
**Run:** `01_first_ai_call.py`

Observe:

- client construction
- `responses.create()`
- model + input
- response ID/status/model/usage
- `output_text`

Failure drills:

- missing key
- unavailable model
- provider/network error

Pass: explain why `create()` creates a response, not a model.

---

## V2 — First Local/Ollama LLM Call
**Lessons:** 4 + 5  
**Run:** `02_ollama_ai_call.py`

Observe:

- local base URL
- installed model
- no cloud API key
- same request/response mental model

Failure drills:

- stop Ollama
- use missing model

Pass: explain local-vs-hosted trade-offs without saying either output is automatically trusted.

---

## V3 — Token / Context Experiment
**Lesson:** 6 — Tokens, Cost & Context Engineering

Use the same incident question with:

1. short evidence
2. noisy long log
3. trimmed source-labeled evidence

On hosted path, inspect usage metadata when available. On local path, compare latency/quality.

Pass: explain why more context is not automatically better.

---

## V4 — Structured Output
**Lesson:** 7  
**Run:** `03_structured_output.py`

Test:

- correct schema
- missing field
- invalid confidence
- schema-valid but unsupported factual claim

Pass: explain `schema-valid != factually true`.

---

## V5 — Basic Tool Request
**Lesson:** 8  
**Run:** `04_tool_call_basic.py`

Observe:

```text
LLM tool request
→ host validates
→ Python executes
→ tool result
```

Failure drills:

- unknown tool
- invalid target
- missing argument

Pass: explain `tool request != execution authority`.

---

## V6 — Basic DevOps Agent V1
**Lesson:** 9  
**Run:** `devops_agent_v1.py`

Goal: first multi-tool decide→act→observe loop.

Pass: identify state, tool selection and stop condition.

---

## V7 — DevOps Agent V2
**Run:** `devops_agent_v2.py`

Goal: better environment/cluster/tool argument mapping.

Failure drill: invalid environment or cluster.

Pass: explain why model-generated args need host validation.

---

## V8 — DevOps Agent V3
**Run:** `devops_agent_v3.py`

Goal:

- explicit state
- duplicate/no-progress protection
- evidence grounding

Pass: evidence must be distinguishable from model narrative.

---

## V9 — DevOps Agent V4
**Run:** `devops_agent_v4.py`

Goal:

- investigation separated from reporting
- structured RCA
- safer validation

Failure drills:

- missing evidence
- invented tool
- unsupported impact

Pass: agent must fail closed rather than fabricate RCA.

---

## V10 — Complete Real-Tool Trusted RCA
**Section:** A — Complete Lab Code  
**Open:** `lesson-05-real-tool-practical/README.md`

Evolution:

```text
pipeline.log
→ real file-reading tool
→ model requests tool
→ no-tool guardrail
→ evidence preservation
→ evidence-only reporter
→ Pydantic
→ tool allowlist + arg validation
→ deterministic impact
→ confidence policy
→ TRUSTED RCA
```

Provider comparison bonus: use same evidence/prompt with Ollama and OpenAI where supported, while keeping host validation identical.

### Hero acceptance criteria
Learner can explain:

```text
LLM = reasoner
Host = executor/policy owner
Tool request = untrusted proposal
Tool result = evidence with provenance
Schema = shape
Evidence validation = factual trust gate
No evidence = no forced RCA
```

---

# After V10

Complete:

- `B-Troubleshooting-Playbook.md`
- `C-Interview-and-Revision-Sheet.md`
- `D-Official-References.md`

Then move to Module 2.