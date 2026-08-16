# 🚩 Jai Bajrangbali!

# Lesson 04 — Zero-Cost Local AI with Ollama

> **Same concepts, model on your laptop.**

## Why This Topic Now?

Cloud API billing blocked ho sakti hai, but API requests, outputs, structured data, tool calling aur agents ki learning continue rehni chahiye. Ollama local machine par models run karta hai aur localhost API expose karta hai.

```text
OpenAI Cloud API
       ↓
Ollama Local Runtime
       ↓
First API Response
```

## Install and Verify on Windows

```powershell
ollama --version
ollama run gemma3:1b
```

First run model download karega. Interactive prompt me test karo:

```text
Explain AKS in two simple lines.
```

Exit:

```text
/bye
```

## What `localhost` Means

```text
http://localhost:11434
```

`localhost` ka matlab current computer. Ollama by default local API ko port `11434` par expose karta hai.

## OpenAI-Compatible Local Client

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)

response = client.responses.create(
    model="gemma3:1b",
    input="Explain AKS in two simple lines."
)

print(response.output_text)
```

## Why `api_key="ollama"`?

OpenAI SDK client key field expect karta hai. Local Ollama ko ye value real secret ke roop me validate karne ki zaroorat nahi hoti; request localhost par route hoti hai.

## Live Hallucination Lesson

Small local model ne ek run me AKS ko **Amazon Kubernetes Service** bola tha. Ye wrong tha:

```text
AKS = Azure Kubernetes Service
EKS = Amazon Elastic Kubernetes Service
```

Isse ek important rule practically prove hua:

> **Fluent output is not proof of correctness.**

## Golden Rule

> **AI confident hoke bhi wrong ho sakta hai. Technical output ko context, evidence aur validation chahiye.**

## Cloud vs Local

| Cloud LLM API | Local Ollama |
|---|---|
| Provider infrastructure | Your laptop/workstation |
| Credentials required | Usually local-only auth pattern |
| Usage billing can apply | No per-call cloud API billing |
| Stronger hosted models available | Hardware/model-size constrained |
| Internet/provider dependency | Can run locally after setup |

## 🎯 Interview Corner

### Q. What is the difference between a cloud LLM API and a local Ollama model?

**Answer:**
> A cloud API runs the model on provider infrastructure and typically requires credentials and usage billing. Ollama can run compatible models locally and expose a localhost API, which is useful for private and low-cost experimentation.

## Why the Next Lesson Follows

Cloud aur local request flow clear ho gaya. Ab dekhna hai API call se actually return kya hota hai.

➡️ **Next: Lesson 05 — First API Call & Response Object**
