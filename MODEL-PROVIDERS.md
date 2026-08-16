# LLM Provider Guide — Ollama Local + OpenAI API

This repository teaches **AI application architecture**, not dependence on one model vendor.

Use either:

```text
LLM_PROVIDER=ollama
```

or:

```text
LLM_PROVIDER=openai
```

The application-level rules should remain the same:

```text
Evidence
→ Prompt / Context Contract
→ Model
→ Parser
→ Validation
→ Policy
```

---

# 1. Provider A — Ollama Local LLM

## Why use it?

- no hosted API key required for local models
- useful for learning and experimentation
- data stays on the local machine for the direct local API path
- lets you study tool/RAG/agent concepts without tying them to paid API usage

## Install

Install Ollama for your OS, then verify:

```powershell
ollama --version
```

## Pull a model

Recommended default used by new provider-parity labs:

```powershell
ollama pull qwen3:4b
```

Smaller fallback:

```powershell
ollama pull gemma3:1b
```

See installed models:

```powershell
ollama list
```

## Environment

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=qwen3:4b
OLLAMA_BASE_URL=http://localhost:11434
```

## Local API mental model

```text
Python App
   ↓ HTTP
http://localhost:11434/api/chat
   ↓
Local Ollama Runtime
   ↓
Local Model
```

No local API authentication is normally required for the default localhost endpoint.

---

# 2. Provider B — OpenAI API

## Why use it?

- hosted production API experience
- strong model quality
- useful for provider comparison
- teaches API key, billing, rate-limit and hosted-dependency concerns

## Install SDK

```powershell
pip install openai python-dotenv
```

## Environment

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=replace-with-your-key
OPENAI_MODEL=gpt-5.6-luna
```

Never commit `.env` with a real key.

## Python mental model

```text
Python App
   ↓ HTTPS
OpenAI Responses API
   ↓
Hosted Model
```

The new shared examples use the Responses API pattern:

```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain AKS in two lines.",
)
print(response.output_text)
```

`OPENAI_MODEL` is environment-controlled so the course is not coupled to a hard-coded model forever.

---

# 3. Shared Provider Interface

Use:

```python
from shared.llm_provider import ask_llm

result = ask_llm(
    prompt="Explain why this deployment failed.",
    system="You are a grounded DevOps incident analyst.",
)

print(result.provider)
print(result.model)
print(result.text)
```

The provider is selected from environment variables.

This gives a beginner one stable application contract:

```text
ask_llm(prompt, system)
```

while implementation changes underneath:

```text
Ollama local API
or
OpenAI Responses API
```

---

# 4. Configuration Files

Copy:

```text
shared/.env.example
```

to:

```text
.env
```

Example local setup:

```env
LLM_PROVIDER=ollama
OLLAMA_MODEL=qwen3:4b
OLLAMA_BASE_URL=http://localhost:11434
```

Example hosted setup:

```env
LLM_PROVIDER=openai
OPENAI_MODEL=gpt-5.6-luna
OPENAI_API_KEY=...
```

---

# 5. Provider Selection Rules

Use local Ollama when:

```text
learning
experimentation
offline/private local tests
avoiding hosted API cost
```

Use OpenAI when:

```text
hosted API integration is the lesson
comparing model quality
production-style provider testing
stronger reasoning is useful
```

Do not confuse provider selection with security.

```text
Local model != automatically safe
Hosted model != automatically unsafe
```

Security depends on:

```text
what data is sent
what tools are exposed
identity
authorization
policy
logging
validation
network boundary
```

---

# 6. Provider Parity by Course Area

## Basic generation

Both providers supported.

## Prompt engineering

Same prompt contract can be executed on both providers.

## Structured output

The repository teaches schema validation independently from provider output wording.

## Embeddings

Two distinct paths are demonstrated:

```text
Local: sentence-transformers
Hosted: OpenAI embeddings
```

Never mix vector dimensions from different embedding models inside the same index without rebuilding/migrating the index.

## RAG

Retrieval can stay local while generation is switched between Ollama/OpenAI.

## LangChain

Use a model factory:

```text
ChatOllama
or
ChatOpenAI
```

The chain architecture should not change.

## MCP

MCP server/client design is model-provider independent. Only the reasoning host may use a selected provider.

## LangGraph / Agents

State, routing, loop limits, checkpoints, authorization and approval are host controls. They must not depend on which LLM provider is selected.

## Security/Evals

Run the same eval dataset against both providers. Provider change is a release-relevant change because behavior can change.

---

# 7. Cost and Failure Differences

## Ollama local failures

Common:

```text
Ollama service not running
model not pulled
RAM insufficient
model too slow
localhost port unavailable
```

## OpenAI failures

Common:

```text
missing API key
invalid key
billing/credit issue
rate limit
network failure
timeout
provider-side error
```

Your host application should expose these as explicit failure states rather than hallucinating a normal answer.

---

# 8. Timeout and Retry Rule

A provider timeout means:

```text
MODEL_CALL_FAILED
```

It does **not** mean:

```text
incident healthy
no evidence
root cause confirmed
```

Retry only operations known to be safe to retry.

---

# 9. Model Output Rule

Regardless of provider:

```text
Model output = untrusted analysis
```

It is not:

```text
current evidence
authorization
approval
execution result
```

This rule stays unchanged from Module 1 to Module 12.

---

# 10. Provider Comparison Exercise

Run the same prompt twice:

```powershell
$env:LLM_PROVIDER="ollama"
python shared/provider_smoke_test.py
```

then:

```powershell
$env:LLM_PROVIDER="openai"
python shared/provider_smoke_test.py
```

Compare:

```text
answer quality
latency
format consistency
hallucination behavior
cost/dependency
error behavior
```

Do not compare only wording. Compare whether the application contract and evidence policy remain valid.

---

# 11. Production Provider Abstraction

A production design may look like:

```text
Application
    ↓
Provider Interface
    ↓
Policy / Configuration
    ↓
┌─────────────┬─────────────┐
│ OpenAI      │ Local/Other │
│ Provider    │ Provider    │
└─────────────┴─────────────┘
```

But fallback must be deliberate.

Bad:

```text
OpenAI failed → silently use random local model
```

Better:

```text
provider failure
→ explicit fallback policy
→ compatible model/context rules
→ audit fallback
→ re-run validation
```

---

# 12. Final Rule

The course architecture is intentionally provider-independent:

```text
Provider generates.
Host controls.
Evidence grounds.
Validator checks.
Policy decides.
Executor acts.
```
