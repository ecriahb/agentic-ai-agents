# Module 1 — Lesson 4: Zero-Cost Local AI with Ollama

> **Goal:** Same AI application concept ko local machine par run karna, without cloud API billing.

## English definition
**Ollama is a local model runtime that lets you run supported LLMs on your own machine and access them through a local API.**

## Why this lesson now?
Lesson 3 me hosted OpenAI path dekha. Ab compare karte hain:

```text
Hosted Model                Local Model
OpenAI API                  Ollama
Internet required           Runs on your machine
API billing possible        No per-call cloud fee
Provider-managed compute    Your CPU/RAM/GPU
Cloud data path              Local data path
```

## Mental model

```text
Python App
   ↓
localhost:11434
   ↓
Ollama Runtime
   ↓
Installed Local Model
   ↓
Response
```

## Setup
Verify:

```powershell
ollama --version
ollama list
```

Pull a model:

```powershell
ollama pull qwen3:4b
```

Lightweight alternative:

```powershell
ollama pull gemma3:1b
```

Run manually:

```powershell
ollama run qwen3:4b
```

## Local API concept
Ollama exposes an HTTP API on localhost. Your Python app still behaves like an API client; only the provider endpoint changes.

Example via OpenAI-compatible client:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",
)
```

Important: `api_key="ollama"` here is only a placeholder expected by the compatible client. It is not a cloud secret.

## Why local model is valuable for learning
- repeatable experiments
- no per-call cloud cost
- privacy for local learning data
- provider comparison
- offline-ish experimentation after model is downloaded

But local does **not** mean automatically secure or production-ready. You still need process isolation, host security, authorization and data controls.

## Hardware reality
Model size affects:

```text
RAM
CPU/GPU usage
startup time
latency
response quality
```

A smaller model may be faster but less capable. Learning goal is architecture, not benchmark chasing.

## Common failures

### `ollama` command not found
Ollama not installed or terminal PATH/session not refreshed.

### Model not found
Run `ollama list`; pull the exact configured model.

### Connection refused on 11434
Ollama service/runtime is not available.

### Very slow response
Model may be too heavy for machine resources.

## Practical
Run:

```powershell
python examples/02_ollama_ai_call.py
```

Then compare with cloud call using the same prompt.

Observe:

- same application concept
- different endpoint/provider
- different latency/output quality
- same need for validation

## Critical lesson

```text
Local LLM != trusted LLM
Cloud LLM != trusted LLM
```

Both model outputs are untrusted reasoning results until application validation/evidence checks happen.

## Interview questions
1. Ollama kya solve karta hai?
2. Local model ka main trade-off kya hai?
3. Local model use karne se authorization problem solve hoti hai kya?
4. Provider switch se host validation kyun nahi badalni chahiye?

## Why next lesson?
Ab cloud aur local provider dono samajh gaye. Next lesson me actual **first API call line-by-line** aur uske **response object** ko decode karenge.