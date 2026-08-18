# 🚩 Module 3 — APIs & Minimal Python for AI

> **The canonical home for application plumbing: HTTP, JSON, authentication, Python and reliable LLM API integration.**

Module 1 used APIs and tools. Module 2 engineered prompts/context. Module 3 now explains the plumbing underneath those applications without turning the course into a generic programming course.

## 🎯 Learning Promise

By the end you can explain and debug:

- API/client/server/endpoint contracts
- REST + HTTP + JSON together
- authentication, API keys and bearer tokens
- environment variables and secret management
- the minimum Python needed for AI applications
- LLM API request/response flow
- provider abstraction
- timeout, retry, rate-limit and exception handling
- structured AI responses and validation

## 🧠 Core Mental Model

```text
Python Application
      ↓
HTTP Request + Auth
      ↓
API Endpoint
      ↓
LLM Service
      ↓
HTTP / JSON Response
      ↓
Python Parsing + Validation
      ↓
Application Output
```

> **API is the communication contract; Python is the controller; the LLM is a service.**

## 🧭 Lean Canonical Lesson Sequence

| Unit | Canonical topic | Existing material used |
|---|---|---|
| 01 | [API + REST + HTTP](Lesson-01-API-Fundamentals.md) | Lessons 01–03 |
| 02 | [JSON + API Payloads](Lesson-04-JSON-for-AI-Applications.md) | Lesson 04 |
| 03 | [Authentication + Environment + Secrets](Lesson-05-Authentication-and-API-Keys.md) | Lessons 05–06 |
| 04 | [Minimal Python for AI](Lesson-07-Minimal-Python-for-AI.md) | Lesson 07 |
| 05 | [Calling an LLM through an API](Lesson-08-Calling-an-LLM-through-API.md) | Lesson 08 |
| 06 | [Provider Abstraction: OpenAI / Gemini / Azure OpenAI](Lesson-09-OpenAI-Gemini-Azure-OpenAI.md) | Lesson 09 |
| 07 | [Responses + Errors + Reliability](Lesson-10-API-Responses-and-Errors.md) | Lesson 10 |
| 08 | [Structured AI Responses + Validation](Lesson-11-Structured-AI-Responses.md) | Lesson 11 |
| 09 | [Mini Project — First AI Application](Lesson-12-Mini-Project-First-AI-Application.md) | Lesson 12 |

## 🛠️ Setup

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install only the dependencies required by the lesson/lab. Typical fundamentals use `requests`; provider labs use their official SDK when needed; local LLM labs can use Ollama.

For hosted APIs, configure environment variables rather than hardcoding secrets.

```text
.env → local development only
Secret manager → production pattern
```

## 🧪 Practical Examples

```text
V1 API GET/POST + status handling
V2 JSON request/response parsing
V3 environment/secrets demo
V4 Ollama LLM call
V5 hosted LLM call
V6 401/403/429/5xx error drill
V7 timeout + retry/backoff simulation
V8 provider adapter
V9 structured response + Pydantic validation
V10 final First AI Application
```

### Provider-neutral architecture

```text
Application
    ↓
Internal LLM interface
    ↓
Provider Adapter
 ┌────┼─────────┐
 ↓    ↓         ↓
Ollama OpenAI Azure OpenAI
```

Business logic stays above the adapter. Provider-specific syntax stays inside the adapter/lab.

## 🔗 Module Boundaries

```text
M1 = application mechanics
M2 = prompt/context engineering
M3 = API/application plumbing
M4 = semantic retrieval
```

M1 only teaches enough API usage to build the first agent. M3 owns the deeper HTTP/REST/JSON/auth/error explanations. Later modules reuse them without restarting the basics.

## 🔐 Security Rules

```text
Never hardcode secrets.
Never log secrets.
Never put credentials into model context unnecessarily.
Use least privilege.
Rotate/revoke credentials.
Treat provider responses and errors as untrusted input.
```

## ✅ Completion Test

Explain without notes:

- API vs REST vs HTTP
- JSON request/response flow
- 401 vs 403 vs 429 vs 5xx
- API key vs bearer token
- why `.env` is for local convenience, not a production secret-management strategy
- what the SDK does underneath
- timeout vs retry
- why structured output still needs validation
- how an adapter allows provider switching

## 🔗 Continue

➡️ [Module 4 — Embeddings & Vector Search](../Module-4/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)

> **Outcome:** you can build and debug an API-driven AI application instead of merely copying an SDK example.
