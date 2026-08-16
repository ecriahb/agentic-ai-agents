# Ollama + OpenAI — Dual-Provider Lab Map

> **Course rule: provider can change; evidence, validation, authorization and policy do not.**

This page tells a beginner exactly where to compare the local LLM path with the OpenAI hosted path.

---

# Before You Start

Read:

- [`START-HERE.md`](START-HERE.md)
- [`MODEL-PROVIDERS.md`](MODEL-PROVIDERS.md)

Install shared provider dependencies:

```powershell
pip install -r shared/requirements.txt
```

Check setup:

```powershell
python shared/preflight.py
```

Smoke test:

```powershell
python shared/provider_smoke_test.py
```

---

# Provider Environment

## Ollama

```powershell
$env:LLM_PROVIDER="ollama"
$env:OLLAMA_MODEL="qwen3:4b"
```

If a historical lab explicitly uses `qwen2.5:3b`, that model is also available in Ollama; either pull it for that lab or use the newer provider-parity lab in the same module.

## OpenAI

```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="your-key"
$env:OPENAI_MODEL="gpt-5.6-luna"
```

---

# Course Coverage Matrix

| Module | Local / Provider-Independent Path | OpenAI / Dual Path | What to Compare |
|---|---|---|---|
| 0 | No-code conceptual experiments | Same no-code concepts can be tried in any chat UI | mental models, hallucination, prompting |
| 1 | `02_ollama_ai_call.py` + Ollama agent labs | `01_first_ai_call.py` | API vs local runtime, output behavior |
| 2 | `prompt_playground.py` | `dual_provider_prompt_playground.py` | groundedness, abstention, format |
| 3 | `04_ollama_llm_call.py` | `08_dual_provider_llm_call.py` | HTTP/API/provider abstraction |
| 4 | local SentenceTransformer embeddings | `06_dual_provider_embeddings.py` | vector dimensions, rankings, cost/dependency |
| 5 | existing V1→V10 local RAG | `11_dual_provider_rag_assistant.py` | same retrieval/context, different generator |
| 6 | existing LangChain `ChatOllama` labs | `11_dual_provider_langchain.py` | same chain, `ChatOllama` vs `ChatOpenAI` |
| 7 | V1→V10 MCP server/client labs | `12_dual_provider_live_mcp_assistant.py` | same live MCP evidence, different reasoning provider |
| 8 | V1→V10 LangGraph labs | `11_dual_provider_stateful_rca.py` | same graph state/routing, different model node |
| 9 | V1→V10 multi-agent labs | `11_dual_provider_multi_agent_synthesis.py` | same specialist evidence, different synthesis provider |
| 10 | deterministic security/eval harness | `11_dual_provider_eval_target.py` | same security tests across providers |
| 11 | architecture labs are intentionally provider-independent | `11_provider_readiness_matrix.py` compares provider operational responsibilities | identity/network/data/HA/eval responsibility |
| 12 | V1→V10 capstone local path | `11_dual_provider_capstone_rca.py` | same evidence/RAG/policy, different RCA generator |

---

# Why Modules 0 and 11 Are Different

## Module 0

The goal is AI understanding before coding. Requiring an API key would make the beginner path worse.

Practical path:

```text
concept
→ no-code experiment
→ observation
→ explanation
```

## Module 11

The goal is enterprise architecture:

```text
identity
networking
state
scaling
HA/DR
observability
CI/CD
governance
```

These responsibilities exist regardless of model provider. Therefore the practical compares production-readiness responsibilities rather than forcing a meaningless LLM call into every architecture lesson.

---

# Module 4 — Embedding Provider Warning

Local and OpenAI embeddings are separate vector spaces.

Do not:

```text
index documents with model A
then query with model B
```

without rebuilding/migrating the index.

The vector dimension and geometry can differ.

And:

```text
similarity score != factual confidence
```

---

# Module 5 — Best Provider Comparison Pattern

Keep retrieval fixed:

```text
same documents
same chunks
same local embedding/index
same retrieved S1-S4
```

Then change only generation:

```text
Ollama
vs
OpenAI
```

Now the comparison is meaningful because the evidence input is controlled.

---

# Module 6 — LangChain Pattern

```text
PromptTemplate
      ↓
Model Factory
 ┌────┴────┐
 ↓         ↓
ChatOllama ChatOpenAI
 └────┬────┘
      ↓
Output Parser
```

The chain architecture stays the same.

---

# Module 7 — MCP Pattern

```text
MCP Client
  ↓
MCP Tools / Resources
  ↓
Evidence Context
  ↓
Provider Adapter
  ├─ Ollama
  └─ OpenAI
  ↓
Grounded Analysis
```

MCP does not depend on one model provider.

---

# Modules 8–9 — Agent Pattern

The provider must never own:

```text
state schema
routing policy
loop limit
authorization
approval
```

Only the model-dependent reasoning node changes.

---

# Module 10 — Evaluation Rule

A model/provider upgrade is a behavior change.

Run the same:

```text
normal cases
weak evidence cases
prompt injection cases
tool-abuse cases
secret leakage cases
```

against both providers.

Do not release because a new model “seems smarter.”

---

# Final Provider-Agnostic Mental Model

```text
             MODEL PROVIDER
          ┌───────┴────────┐
          ↓                ↓
       Ollama            OpenAI
          └───────┬────────┘
                  ↓
              Analysis
                  ↓
              Validator
                  ↓
                Policy
                  ↓
              Application
```

The non-negotiable rule is:

```text
Model generates.
Evidence grounds.
Host validates.
Policy decides.
Executor acts.
```
