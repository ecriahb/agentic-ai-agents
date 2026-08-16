# 🚩 Jai Bajrangbali!

# Lesson 03 — OpenAI Cloud API Setup

> **Real cloud path: key, billing, SDK, Responses API.**

## Why This Topic Now?

SDK install ho gaya, but cloud model anonymous requests accept nahi karta. API use karne ke liye valid credentials aur available API billing/credits chahiye.

```text
Environment + Secrets
        ↓
OpenAI Cloud API
        ↓
Local Ollama Fallback
```

## Cloud Flow

```text
Python Application
       ↓
OpenAI SDK Client
       ↓
API Authentication
       ↓
Responses API
       ↓
Existing Model
       ↓
Response Object
```

## API Key Setup — Conceptual Steps

1. OpenAI API Platform me sign in karo.
2. Correct organization/project select karo.
3. API Keys section open karo.
4. New secret key create karo.
5. Meaningful name use karo, for example `Agentic-AI-Learning`.
6. Secret ko safely `.env` ya enterprise secret manager me store karo.
7. Real key ko code, screenshots, GitHub ya chat me expose mat karo.

## Billing Reality

> **ChatGPT subscription billing and OpenAI API billing are separate.**

Valid API key ke baad bhi project me API credits/billing unavailable ho to quota/credit error aa sakta hai.

## Cloud Sample

```python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="YOUR_AVAILABLE_MODEL",
    input="Explain AKS in two simple lines."
)

print(response.output_text)
```

## How to Read `client.responses.create()`

```text
client
  ↓
API client object

responses
  ↓
Responses API resource

create()
  ↓
Generate a new model response

model
  ↓
Which existing model to use

input
  ↓
Task/context sent to the model

response
  ↓
Returned result object
```

`create()` **response create karta hai, model nahi**.

## Common Errors We Learned From

| Error | Meaning | Fix |
|---|---|---|
| Missing credentials | API credential load nahi hua | `.env` / environment variable check karo |
| 401 invalid_api_key | Invalid/placeholder key send hui | Valid secret key use karo |
| 429 insufficient quota / no credits | Authentication succeeded but billing unavailable | API billing add karo or Ollama labs continue karo |

## 🎯 Interview Corner

### Q. What does `client.responses.create()` do?

**Answer:**
> It uses the API client to send a request to the Responses API and generate a new response with the selected model and supplied input.

## 🧠 Remember This

> **SDK connects your code to the API. API key authenticates the application. `responses.create()` asks an existing model to generate a response.**

## Why the Next Lesson Follows

Cloud billing unavailable ho to learning stop nahi honi chahiye. Local model runtime same request/response concepts ko without per-call cloud credits practice karne deta hai.

➡️ **Next: Lesson 04 — Zero-Cost Local AI with Ollama**
