# Module 1 — Lesson 5: First API Call & Response Object

> **Goal:** `client.responses.create()` ko line-by-line samajhna aur response object se useful fields safely read karna.

## English definition
**An API call sends a request to a model endpoint and receives a structured response object containing generated output plus request metadata.**

## Minimal OpenAI example

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="your-available-model",
    input="Explain AKS in two simple lines.",
)

print(response.output_text)
```

## What `create()` means

```text
client.responses.create(...)
```

does **not** create/train a new AI model. It creates a **response request/result** using an existing model.

## Request anatomy

```text
client
  ↓
responses
  ↓
create(
  model=...,
  input=...
)
```

### `model`
Which existing provider model should handle the request.

### `input`
What information/instruction is sent to the model.

## Response object mental model

```text
response
├─ id
├─ model
├─ status
├─ usage
├─ output
└─ output_text  ← convenient final text
```

Example inspection:

```python
print("ID:", response.id)
print("Model:", response.model)
print("Status:", response.status)
print("Usage:", response.usage)
print("Answer:", response.output_text)
```

Do not assume every provider/library has identical response fields. The application should depend on a stable internal contract where possible.

## Local equivalent
Ollama can be called through its native API or an OpenAI-compatible interface. Learning point is the same:

```text
Request
→ provider/runtime
→ response object/payload
→ host extracts needed data
```

## Why response object matters in DevOps
A production app needs more than pretty text:

- request ID for tracing
- model identity
- status/error handling
- usage/cost metrics
- structured output/tool requests
- audit metadata

## Common beginner mistake

Bad mental model:

```text
response = answer string
```

Better mental model:

```text
response = structured API result
answer = one useful field inside it
```

## Practical
Run both:

```powershell
python examples/01_first_ai_call.py
python examples/02_ollama_ai_call.py
```

Write down:

- provider
- model
- response type
- text field
- status
- usage if available
- error if provider unavailable

## Failure drill
1. Temporarily use an unavailable model name.
2. Remove cloud key and observe hosted failure.
3. Stop Ollama and observe local connection failure.
4. Restore configuration and rerun.

Goal: error category identify karna, random code changes nahi.

## Interview questions
1. `client.responses.create()` kya karta hai?
2. Response object aur output text me kya difference hai?
3. Request ID observability me useful kyun hai?
4. Model name hard-code karna kab problematic ho sakta hai?

## Revision

```text
API call = request + provider execution + structured response
create() = create a response, not a model
response object = text + metadata/status/usage
```

## Why next lesson?
Ab request/response samajh gaya. Next question: **LLM input/output kitna consume karta hai, context kitna fit hota hai aur hosted usage cost kaise affect hota hai?**