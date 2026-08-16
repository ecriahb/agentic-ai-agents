# 🚩 Jai Bajrangbali!

# Lesson 02 — Development Environment & Secret Management

> **Workshop ready karo, phir engine start karenge.**

## Why This Topic Now?

API call se pehle application ko Python, isolated environment, SDK aur secrets ke liye safe place chahiye. Warna package conflicts aur leaked credentials pehla issue ban jayenge.

```text
UI vs API
   ↓
Environment + Secrets
   ↓
OpenAI Cloud API
```

## Core Components

| Component | Simple Meaning | DevOps Analogy |
|---|---|---|
| Python | Labs ki language | Automation runtime |
| venv | Project-specific Python environment | Dependency isolation |
| pip | Package installer | Package manager |
| openai | API client SDK | Provider SDK |
| python-dotenv | `.env` values load karta hai | Local config/secret loader |
| .gitignore | Secret files Git se bachata hai | Repository safety control |

## Create Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install openai python-dotenv
```

### Why `python -m pip`?

Ye pip ko currently active Python interpreter ke saath tie karta hai. Isse confusion kam hota hai ki package kis environment me install hua.

## Safe Local Secret Pattern

### `.env`

```env
OPENAI_API_KEY=YOUR_REAL_SECRET_KEY
```

### `.gitignore`

```gitignore
.env
.venv/
__pycache__/
```

### Test Secret Loading

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key loaded successfully")
else:
    print("API key not found")
```

## ⚠️ Important

Local `.env` learning ke liye convenient hai, final enterprise secret store nahi. Production me **Azure Key Vault** jaise secret manager aur least-privilege access use karna chahiye.

Never commit a real API key to GitHub.

## 🎯 Interview Corner

### Q. Why should API keys not be hardcoded?

**Answer:**
> API keys are credentials. Hardcoding can expose them in source control, logs, screenshots or shared code. Secrets should be injected through secure environment variables or a secret-management system.

## 🧠 Remember This

```text
Code → Git
Secret → Secret Store
Never mix them.
```

## Why the Next Lesson Follows

Environment ready hai. Ab cloud provider ko authenticate karke real model request ka flow samjhenge.

➡️ **Next: Lesson 03 — OpenAI Cloud API Setup**
