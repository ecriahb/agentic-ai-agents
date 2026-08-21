# 🚩 Jai Bajrangbali!

# Module 3 — APIs & Python for AI

> **From prompt designer → AI application engineer who can reliably connect software with LLMs.**

> **Ownership boundary:** Module 1 already teaches the first provider call and response object. Module 3 owns reusable HTTP/REST/JSON/Python plumbing, service failures, retries and production API behavior.

Module 1 me humne API calls, local Ollama, structured output aur tools ka practical taste liya. Module 2 me humne prompts ko reliable banaya. Module 3 me hum un concepts ko systematically deepen karenge so that aap API-based AI application ko samajh, debug aur production-ready design kar sako.

---

## 🎯 Module 3 Learning Promise

Module ke end tak aap clearly samjhoge:

- API fundamentals and client-server thinking
- REST API basics and endpoints
- HTTP methods, headers, status codes, request and response
- JSON as the language of APIs
- authentication, API keys and bearer tokens
- environment variables and secret management
- only the Python needed for AI application development
- how an LLM API call actually travels
- OpenAI, Gemini and Azure OpenAI concepts
- timeout, retry, rate limit and exception handling
- structured AI responses and schema validation
- a complete first AI application for DevOps incident analysis

---

## 🧠 Core Mental Model

```text
User / DevOps Event
        ↓
Python Application
        ↓
HTTP Request
        ↓
API Endpoint
        ↓
Authentication
        ↓
LLM Service
        ↓
HTTP Response
        ↓
JSON / Structured Data
        ↓
Python Validation
        ↓
Useful Application Output
```

> **API is the communication contract; Python is the controller; the LLM is the intelligence service.**

---

# 📚 Lesson Sequence

| Lesson | Topic | Main Outcome |
|---|---|---|
| 01 | [API Fundamentals](Lesson-01-API-Fundamentals.md) | Understand API, client, server, endpoint and contract |
| 02 | [REST API Basics](Lesson-02-REST-API-Basics.md) | Understand resources, URLs and stateless requests |
| 03 | [HTTP Methods, Request & Response](Lesson-03-HTTP-Methods-Request-Response.md) | Read and debug HTTP traffic |
| 04 | [JSON for AI Applications](Lesson-04-JSON-for-AI-Applications.md) | Work with API payloads in Python |
| 05 | [Authentication & API Keys](Lesson-05-Authentication-and-API-Keys.md) | Securely authenticate API calls |
| 06 | [Environment Variables & Secret Management](Lesson-06-Environment-Variables-and-Secrets.md) | Keep secrets outside source code |
| 07 | [Minimal Python for AI Applications](Lesson-07-Minimal-Python-for-AI.md) | Learn only the Python needed for AI apps |
| 08 | [Calling an LLM through an API](Lesson-08-Calling-an-LLM-through-API.md) | Build and understand the complete request flow |
| 09 | [OpenAI / Gemini / Azure OpenAI Concepts](Lesson-09-OpenAI-Gemini-Azure-OpenAI.md) | Compare provider patterns without vendor confusion |
| 10 | [Handling API Responses & Errors](Lesson-10-API-Responses-and-Errors.md) | Handle failures safely and predictably |
| 11 | [Structured AI Responses](Lesson-11-Structured-AI-Responses.md) | Convert text generation into dependable application data |
| 12 | [Mini Project — First AI Application](Lesson-12-Mini-Project-First-AI-Application.md) | Build a DevOps incident analyzer end-to-end |

---

# 🧪 Practical Examples

Runnable and copy-paste examples are stored under [`examples/`](examples/README.md).

```text
01_api_get_request.py
02_json_basics.py
03_env_secret_demo.py
04_ollama_llm_call.py
05_api_error_handling.py
06_structured_rca.py
07_first_ai_application.py
sample_incident.log
.env.example
requirements.txt
```

---

# 🔁 Why Module 3 Comes After Module 2

```text
Module 1 → We used APIs and tools
Module 2 → We learned how to instruct the model reliably
Module 3 → We now understand the application/API plumbing deeply
```

Without Module 3, a learner may know how to copy an SDK example but may not know:

- request kahan ja raha hai
- endpoint kya hai
- auth kyun fail ho rahi hai
- 401 vs 429 vs 500 ka difference
- JSON payload kaise travel karta hai
- retry kab safe hai
- response ko validate kaise karna hai

That gap is what this module closes.

---

# ✅ Module Outcome

By the end:

```text
Incident / Prompt
      ↓
Python
      ↓
API Request + Auth
      ↓
LLM
      ↓
JSON Response
      ↓
Validation + Error Handling
      ↓
Structured DevOps RCA
```

Aap sirf API call copy nahi karoge — aap **API-driven AI application ko reason, debug aur build** kar paoge.
