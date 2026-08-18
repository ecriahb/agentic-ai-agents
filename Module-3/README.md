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

### What was intentionally merged

```text
API Fundamentals + REST + HTTP
        → one connected foundation

Authentication + API Keys + Environment Variables + Secrets
        → one security/configuration unit

Provider comparison
        → architecture/adapter concept, not vendor tutorial
```

The original standalone lesson files are retained as reference during this migration. The canonical path above is what a learner should follow.

## 🧪 Practical Examples

```text
API GET request
JSON basics
environment/secret demo
Ollama LLM call
API error handling
structured RCA
first AI application
```

## 🔗 Module Boundaries

### Module 1

Module 1 teaches **what an AI application does**: LLM call → structured output → tools → agent → evidence → trusted RCA.

### Module 2

Module 2 teaches **how to instruct the model reliably**.

### Module 3

Module 3 teaches **how the software communication underneath those applications actually works**.

Therefore:

```text
M1 = application mechanics
M2 = prompt/context engineering
M3 = API/application plumbing
```

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

> **Outcome:** you can build and debug an API-driven AI application instead of merely copying an SDK example.
