# Module 3 — Practical Examples

These examples follow the lesson sequence and are intentionally small enough to understand line-by-line.

| File | Purpose |
|---|---|
| `01_api_get_request.py` | First plain HTTP GET request |
| `02_json_basics.py` | Python dict ↔ JSON basics |
| `03_env_secret_demo.py` | Environment variable and `.env` loading |
| `04_ollama_llm_call.py` | Raw HTTP call to a local Ollama LLM |
| `05_api_error_handling.py` | Timeout, HTTP and connection error handling |
| `06_structured_rca.py` | Pydantic RCA schema validation |
| `07_first_ai_application.py` | Complete local DevOps incident analyzer |
| `sample_incident.log` | Evidence used by the final mini-project |
| `.env.example` | Safe configuration template |
| `requirements.txt` | Python dependencies |

## Suggested order

```text
01 → HTTP request
02 → JSON
03 → environment/secrets
04 → LLM API call
05 → error handling
06 → schema validation
07 → full AI application
```

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

For Ollama examples, ensure Ollama is running locally and update the model name in `.env` if your installed model differs.
