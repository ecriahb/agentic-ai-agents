# Shared Dual-Provider Helper

This folder exists so course labs can teach one architecture while allowing either:

```text
Ollama local LLM
or
OpenAI hosted API
```

## Setup

```powershell
pip install -r shared/requirements.txt
copy shared\.env.example .env
```

### Local

```powershell
ollama pull qwen3:4b
$env:LLM_PROVIDER="ollama"
python shared/provider_smoke_test.py
```

### OpenAI

```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="your-key"
$env:OPENAI_MODEL="gpt-5.6-luna"
python shared/provider_smoke_test.py
```

## Application Contract

```python
from llm_provider import ask_llm

result = ask_llm(
    "Analyze this DevOps evidence.",
    system="Use only supplied evidence.",
)
```

Returned object:

```text
provider
model
text
```

No truth/safety claim is made by this helper. The calling application must still implement:

```text
input validation
evidence boundaries
schema validation
citation validation
policy
authorization
approval
```

## Why Not Hide Provider Differences Completely?

Provider abstraction is useful, but production systems still need to observe:

- model/version
- latency
- token/cost usage where available
- provider failures
- fallback decisions
- output/eval differences

A model-provider change should be treated as a testable application change.
