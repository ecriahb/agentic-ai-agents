# Module 3 — Practical Examples

These examples follow the lesson sequence and are intentionally small enough to understand line-by-line.

> Full practical sequence: [`../PRACTICAL-ROADMAP.md`](../PRACTICAL-ROADMAP.md)

| File | Purpose |
|---|---|
| `01_api_get_request.py` | First plain HTTP GET request |
| `02_json_basics.py` | Python dict ↔ JSON basics |
| `03_env_secret_demo.py` | Environment variable and `.env` loading |
| `04_ollama_llm_call.py` | Raw HTTP call to a local Ollama LLM |
| `05_api_error_handling.py` | Timeout, HTTP and connection error handling |
| `06_structured_rca.py` | Pydantic RCA schema validation |
| `07_first_ai_application.py` | Complete first local DevOps incident analyzer |
| `08_dual_provider_llm_call.py` | Same LLM concept using Ollama or OpenAI |
| `09_failure_matrix.py` | Explicit application failure-state practice |
| `10_devops_ai_cli.py` | Final robust dual-provider DevOps AI CLI |
| `sample_incident.log` | Evidence used by application labs |
| `.env.example` | Safe configuration template |
| `requirements.txt` | Python dependencies |

## Zero-to-Hero order

```text
01 HTTP
 ↓
02 JSON
 ↓
03 Secrets
 ↓
04 Local LLM API
 ↓
05 Error Handling
 ↓
06 Structured Validation
 ↓
07 Complete AI App
 ↓
08 Provider Parity
 ↓
09 Failure Matrix
 ↓
10 Robust CLI
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r ../../shared/requirements.txt
```

For Ollama:
```powershell
$env:LLM_PROVIDER="ollama"
$env:OLLAMA_MODEL="qwen3:4b"
```

For OpenAI:
```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="your-key"
```

Never commit a real API key.

## Learning rule
Every lab should be run at least twice:
1. happy path
2. one intentional failure/change

The goal is to understand the API/application lifecycle—not to memorize Python syntax.
