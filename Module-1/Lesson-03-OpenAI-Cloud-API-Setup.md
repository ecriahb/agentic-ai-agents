# Module 1 — Lesson 3: OpenAI Cloud API Setup

> **Goal:** Hosted OpenAI API ko beginner-friendly way me configure karna, without hard-coding secrets.

## English definition
**A cloud AI API lets an application send authenticated requests to a hosted model over the internet.**

## Why this lesson now?
Lesson 1 me UI vs API samjha. Lesson 2 me Python, venv aur secrets setup kiye. Ab actual hosted provider configure karna natural next step hai.

## Mental model

```text
Python App
   ↓ HTTPS
OpenAI API
   ↓
Hosted Model
   ↓
Response
```

Authentication:

```text
OPENAI_API_KEY
      ↓
OpenAI Client
      ↓
Authenticated request
```

## Setup
Install:

```powershell
pip install "openai>=2,<3" python-dotenv
```

Create local `.env`:

```env
OPENAI_API_KEY=your-real-key-here
OPENAI_MODEL=your-available-model
```

Never commit `.env`.

Load safely:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
```

The SDK reads `OPENAI_API_KEY` from environment.

## What is an API key?
API key model ka password nahi; ye application credential hai jo provider ko request identity/account context deta hai.

Bad:

```python
client = OpenAI(api_key="sk-...")
```

Better:

```python
client = OpenAI()
```

with environment variable.

## Billing vs ChatGPT subscription
ChatGPT product subscription aur API billing separate concepts ho sakte hain. API call success depends on API account access, billing/credits, model access and rate limits.

## Beginner verification
Before writing complex code, verify environment:

```powershell
python -c "import os; print('key loaded' if os.getenv('OPENAI_API_KEY') else 'missing')"
```

Do **not** print the actual key.

## Common failures

### Missing key
Typical reason: `.env` not loaded, wrong working directory, env variable absent.

### Authentication error
Key invalid/revoked/wrong project/account context.

### Billing/quota/rate error
Not a Python syntax bug. Account/provider-side access must be checked.

### Model not found / access denied
Configured model name may not be available to the account. Keep model name configurable.

## Production notes
Use secret stores/managed identity patterns where supported by your environment. Avoid:

- secrets in source code
- secrets in prompts
- secrets in logs
- secrets in screenshots
- secrets in Git history

## Practical
Use `examples/01_first_ai_call.py`, but first read Lesson 5 so you understand the response object rather than blindly running it.

## Interview questions
1. Why should API keys not be hard-coded?
2. ChatGPT UI access and API access me kya difference hai?
3. `.env` production secret manager ka replacement kyun nahi hai?
4. Rate limit error aur code error me difference?

## Revision

```text
Cloud API = hosted capability
API key = credential
SDK = client library
.env = local development convenience
Secret management = host responsibility
```

## Why next lesson?
Hosted path clear ho gaya. Ab same AI concept ko **zero-cost/local experimentation** ke liye Ollama par run karenge, so learner provider dependency ko architecture se separate samjhe.