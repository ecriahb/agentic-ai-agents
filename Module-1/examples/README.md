# Module 1 — Practical Python Examples

Ye folder Module 1 ke hands-on labs ko runnable files me preserve karta hai.

## Run Order

```text
01_first_ai_call.py
        ↓
02_ollama_ai_call.py
        ↓
03_structured_output.py
        ↓
04_tool_call_basic.py
        ↓
devops_agent_v1.py
        ↓
devops_agent_v2.py
        ↓
devops_agent_v3.py
        ↓
devops_agent_v4.py
```

## Version Progression

| Version | Learning Goal |
|---|---|
| V1 | Basic multi-tool agent loop |
| V2 | Better tool arguments + production evidence |
| V3 | State / duplicate-call protection + grounded wording |
| V4 | Investigation separated from structured RCA reporting |

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

For cloud OpenAI example, create local `.env` from `.env.example` and put your real key there. Never commit the real `.env`.

For local labs:

```powershell
ollama --version
ollama run gemma3:1b
```

Some tool-calling labs use `qwen3:0.6b`; pull it if needed:

```powershell
ollama pull qwen3:0.6b
```

> These tools return simulated DevOps evidence for learning. They do not connect to a real AKS cluster, Terraform backend, or CI/CD system.
