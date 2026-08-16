# 🚩 Jai Bajrangbali!

# Lesson 06 — Environment Variables & Secret Management

> **Secret ko code se separate karna basic hygiene hai; production secret management usse ek step aage hai.**

---

## 🎯 Lesson Goal

Aap samjhoge:

- environment variable kya hai
- `.env` file ka role
- `python-dotenv`
- `.gitignore`
- local vs production secret handling
- Azure Key Vault / secret manager concept
- missing-secret validation
- secure logging habits

---

## 1. Problem: Hard-Coded Secret

Bad:

```python
api_key = "sk-real-secret-here"
```

Risk:

```text
Code pushed to GitHub
       ↓
Secret exposed
       ↓
Unauthorized API usage / cost / data risk
```

Even private repository ko secret vault samajhna safe design nahi hai.

---

## 2. Environment Variable Kya Hai?

**English Definition:**
> An environment variable is a key-value value supplied to a process by its runtime environment instead of being embedded in source code.

Example conceptual value:

```text
OPENAI_API_KEY=<secret>
```

Python:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

---

## 3. `.env` File for Local Development

Local file:

```text
OPENAI_API_KEY=replace_me
OLLAMA_BASE_URL=http://localhost:11434/v1
```

Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```

Install:

```bash
pip install python-dotenv
```

---

## 4. `.env` Must Not Go to Git

`.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```

Safe repo pattern:

```text
.env          → local real values, ignored
.env.example  → placeholder names, committed
```

`.env.example`:

```text
OPENAI_API_KEY=your_key_here
OLLAMA_BASE_URL=http://localhost:11434/v1
```

Never put a real secret in `.env.example`.

---

## 5. Validate Early

Bad:

```python
api_key = os.getenv("OPENAI_API_KEY")
# failure happens much later
```

Better:

```python
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured")
```

Fail fast gives clearer debugging.

---

## 6. Local vs Production

`.env` is convenient for learning/local development.

Production mental model:

```text
Application
    ↓ authenticated access
Secret Manager / Key Vault
    ↓
Secret / Token
```

Azure example:

```text
AKS / App Service / VM
       ↓ Managed Identity
Azure Key Vault
       ↓ Secret
Application
```

Goal: secret file ko manually server par scatter na karo.

---

## 7. Don't Print Secrets

Bad:

```python
print(api_key)
```

Better debug:

```python
print("API key configured:", bool(api_key))
```

Or masked display only when absolutely needed:

```python
print(api_key[:4] + "..." if api_key else "missing")
```

Even masking should be used carefully in shared logs.

---

## 8. CI/CD Secret Handling

Pipeline flow:

```text
GitHub Actions / Azure DevOps
       ↓ secret store / federated identity
Runtime environment variable
       ↓
Application
```

Avoid:

```text
Secret in YAML plaintext
Secret in Terraform output
Secret echoed in pipeline logs
```

---

# 🧪 Practical

`.env`:

```text
APP_ENV=dev
DEMO_API_KEY=super-secret-demo
```

Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()

app_env = os.getenv("APP_ENV", "local")
api_key = os.getenv("DEMO_API_KEY")

if not api_key:
    raise RuntimeError("DEMO_API_KEY missing")

print("Environment:", app_env)
print("Secret configured:", True)
```

---

# ❌ Common Mistakes

- `.env` ko commit kar dena
- key ko README/code screenshot me expose karna
- secret ko Terraform output me `sensitive` controls ke bina show karna
- production me unmanaged `.env` files spread karna
- secret missing hone par unclear error
- logs me token print karna

---

# 🎤 Interview Point

**Q: Is `.env` a production secret manager?**

No. It is mainly a convenient local-development pattern. Production systems should prefer managed secret stores or workload identity mechanisms with controlled access and auditing.

---

# 🔁 Why Next Lesson?

Ab API, HTTP, JSON aur secrets samajh gaye. In sab ko glue karne ke liye hume minimal Python chahiye — full Python course nahi.

> **Lesson 07 — Minimal Python for AI Applications**
