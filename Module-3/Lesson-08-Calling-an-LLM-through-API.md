# 🚩 Jai Bajrangbali!

# Lesson 08 — Calling an LLM through an API

> **Ab tak ke saare pieces — Python, HTTP, JSON, auth, endpoint — ek real LLM call me connect honge.**

---

## 🎯 Lesson Goal

Aap samjhoge:

- LLM API call ka full lifecycle
- SDK call ke peeche kya hota hai
- local Ollama vs cloud provider
- request payload
- response parsing
- timeout and failure handling
- prompt + context ka request me placement

---

## 1. Full Mental Model

```text
Python Program
    ↓
Build Prompt / Messages
    ↓
SDK or HTTP Client
    ↓
HTTP POST
    ↓
Endpoint
    ↓
Authentication
    ↓
Model Inference
    ↓
HTTP Response
    ↓
SDK Object / JSON
    ↓
Application extracts useful output
```

SDK magic nahi karta. Wo request construction, serialization, auth headers, HTTP call and response parsing ko easier banata hai.

---

## 2. Local Ollama Example

Ollama local server:

```text
Your Python
   ↓
localhost:11434
   ↓
Ollama
   ↓
Local model
```

Conceptual raw HTTP call:

```python
import requests

payload = {
    "model": "qwen2.5:3b",
    "messages": [
        {
            "role": "user",
            "content": "Explain AKS in two simple lines."
        }
    ],
    "stream": False
}

response = requests.post(
    "http://localhost:11434/api/chat",
    json=payload,
    timeout=60
)

response.raise_for_status()
data = response.json()
print(data["message"]["content"])
```

Important:

```python
json=payload
```

means Python client object ko JSON request body ke form me send karta hai and appropriate JSON content type normally set karta hai.

---

## 3. Cloud API via SDK

Current OpenAI Python SDK pattern conceptually:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="YOUR_MODEL",
    input="Explain AKS in two simple lines."
)

print(response.output_text)
```

The SDK reads the configured API key from environment in the standard setup.

Exact model names, endpoint behavior and SDK parameters can evolve, so provider documentation should be the source of truth when implementing a live integration.

---

## 4. What `responses.create()` Means

Important confusion from earlier learning:

```text
create() ≠ create a model
```

It means:

```text
Create an inference response
using an existing model
```

Mental model:

```text
Existing Model
      +
Your Input
      ↓
Generate Response
```

---

## 5. Request Components

Typical LLM request may include:

```text
Model / deployment identifier
Input / messages
Instructions
Output format
Tools
Sampling/config options
Metadata
```

Not every provider exposes the same field names.

---

## 6. System and User Instructions

Conceptually:

```python
instructions = "You are a senior DevOps incident analyst."
user_input = "Analyze this pipeline failure using only supplied evidence."
```

Module 2 ka prompt engineering yahin actual API request me enter hota hai.

So:

```text
Module 2 Prompt Design
       ↓
Module 3 API Payload
       ↓
LLM Behavior
```

---

## 7. Response Is an Object, Not Just Text

SDK response may contain:

```text
ID
status
model metadata
output items
usage information
text helper properties
errors/incomplete state
```

Application ko sirf pretty text nahi, operational metadata bhi matter kar sakti hai.

---

## 8. Timeout

Raw HTTP call me:

```python
requests.post(url, json=payload, timeout=60)
```

No timeout can make an application hang far longer than expected during network/provider issues.

Production clients should define sensible timeout behavior.

---

## 9. Local vs Cloud

| Local LLM | Cloud LLM API |
|---|---|
| runs on your machine/server | hosted by provider |
| local compute required | provider compute |
| no public network needed for local-only use | network connectivity required |
| model quality depends on local model/hardware | broader hosted model options |
| easier private experimentation | enterprise features/scaling depend on provider |

Neither is automatically "better"; use case decides.

---

# 🛠️ DevOps Example

```text
pipeline.log
    ↓
Python reads evidence
    ↓
build_prompt(evidence)
    ↓
LLM API request
    ↓
Model analyzes only supplied context
    ↓
Response
    ↓
Python validates output
```

This is the bridge between our Module 1 trusted-RCA architecture and Module 3 API engineering.

---

# ❌ Common Mistakes

- model name hard-code karke years tak assume karna
- SDK example ko protocol understanding ke bina copy karna
- response shape assume karna
- timeout/error handling skip karna
- prompt me secrets/log credentials include kar dena
- local model API and cloud provider API ko identical assume karna

---

# 🎤 Interview Point

**Q: What happens when an application calls an LLM using an SDK?**

The application prepares input and configuration, the SDK serializes and sends an authenticated HTTP request to the provider endpoint, the model performs inference, and the SDK parses the HTTP response into an application-friendly object.

---

# 🔁 Why Next Lesson?

Ab ek provider ka flow samajh gaya. Real enterprise environment me different providers mil sakte hain.

> **Lesson 09 — OpenAI / Gemini / Azure OpenAI API Concepts**
