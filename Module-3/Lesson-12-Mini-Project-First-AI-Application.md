# 🚩 Jai Bajrangbali!

# Lesson 12 — Mini Project: First AI Application

> **Ab tak ke saare concepts ko ek single end-to-end DevOps AI application me combine karenge.**

---

## 🎯 Project Goal

Build a local DevOps Incident Analyzer that:

1. incident log file read kare
2. evidence validate kare
3. prompt build kare
4. local Ollama API ko call kare
5. API/network errors handle kare
6. model output ko JSON me parse kare
7. Pydantic schema se validate kare
8. safe structured RCA print kare

---

# 🧠 Final Architecture

```text
sample_incident.log
        ↓
Python File Reader
        ↓
Evidence Check
        ↓
Prompt Builder
        ↓
HTTP POST
        ↓
Ollama API
        ↓
Local LLM
        ↓
JSON Response
        ↓
Extract Model Text
        ↓
Parse RCA JSON
        ↓
Pydantic Validation
        ↓
Structured RCA
```

This mini-project deliberately local Ollama use karta hai so API mechanics learn karne ke liye paid cloud dependency mandatory na ho.

## Provider and API Recipe Extension

Keep the application contract unchanged while adding one optional provider adapter for OpenAI or Azure OpenAI. Record the endpoint/deployment, API version, usage metadata, latency, error class, and data policy. The OpenAI Cookbook is useful here as a recipe reference for structured outputs, retries, batch work, and evaluation, but copy only the transport pattern; evidence validation and authorization remain application-owned.

Do not turn this first application into a fine-tuning project. Decide first whether the requirement is current incident grounding (retrieval), stable output shape (schema), bulk offline processing (batch), or learned domain behavior (fine-tuning). The decision and trade-off belong in the project README.

---

# 📁 Project Structure

```text
Module-3/
└── examples/
    ├── 07_first_ai_application.py
    ├── sample_incident.log
    ├── requirements.txt
    └── .env.example
```

---

# 1. Sample Evidence

`sample_incident.log`:

```text
2026-08-16 10:02:11 - Pipeline started
2026-08-16 10:02:45 - Terraform init completed
2026-08-16 10:03:18 - Terraform plan completed
2026-08-16 10:04:01 - Terraform apply started
2026-08-16 10:04:37 - ERROR: Network Security Group rule aks-subnet-allow was removed.
2026-08-16 10:04:41 - ERROR: AKS subnet connectivity validation failed.
2026-08-16 10:04:45 - Deployment failed during Terraform Apply.
```

---

# 2. Output Contract

```python
from typing import Literal
from pydantic import BaseModel


class IncidentRCA(BaseModel):
    root_cause: str
    impact: str
    recommended_fix: list[str]
    severity: Literal["low", "medium", "high", "critical"]
    confidence: Literal["low", "medium", "high"]
```

---

# 3. Prompt Contract

```text
ROLE:
You are a senior Azure DevOps incident analyst.

EVIDENCE:
<incident log>

TASK:
Analyze the incident.

CONSTRAINTS:
- Use only supplied evidence.
- Do not invent customer impact.
- If evidence is insufficient, say so.
- recommended_fix must contain safe investigation/remediation suggestions.

OUTPUT:
Return only valid JSON with:
root_cause, impact, recommended_fix, severity, confidence.
```

Notice Module 2 is directly reused here.

---

# 4. Read Evidence

```python
from pathlib import Path


def read_evidence(path: str) -> str:
    log_path = Path(path)

    if not log_path.exists():
        raise FileNotFoundError(f"Evidence file not found: {path}")

    evidence = log_path.read_text(encoding="utf-8").strip()

    if not evidence:
        raise RuntimeError("Evidence file is empty. RCA blocked.")

    return evidence
```

Important guardrail:

```text
No evidence → No RCA
```

---

# 5. Build Prompt

```python
def build_prompt(evidence: str) -> str:
    return f"""
You are a senior Azure DevOps incident analyst.

Use ONLY the supplied evidence.
Do not invent facts or customer impact.

EVIDENCE:
{evidence}

Return ONLY valid JSON with this shape:
{{
  "root_cause": "string",
  "impact": "string",
  "recommended_fix": ["string"],
  "severity": "low|medium|high|critical",
  "confidence": "low|medium|high"
}}
"""
```

---

# 6. Call Ollama

```python
import requests


def call_ollama(prompt: str) -> str:
    payload = {
        "model": "qwen2.5:3b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "format": "json"
    }

    response = requests.post(
        "http://localhost:11434/api/chat",
        json=payload,
        timeout=120
    )

    response.raise_for_status()
    data = response.json()

    return data["message"]["content"]
```

---

# 7. Parse and Validate

```python
import json


def validate_rca(raw_text: str) -> IncidentRCA:
    parsed = json.loads(raw_text)
    return IncidentRCA.model_validate(parsed)
```

Flow:

```text
Model text
 ↓ json.loads
Python dictionary
 ↓ Pydantic
Validated RCA
```

---

# 8. Main Function

```python
def main():
    evidence = read_evidence("sample_incident.log")
    prompt = build_prompt(evidence)
    raw_output = call_ollama(prompt)
    rca = validate_rca(raw_output)

    print("\n===== VALIDATED RCA =====")
    print(rca.model_dump_json(indent=2))
```

---

# 9. Add Controlled Errors

```python
import requests
from pydantic import ValidationError


if __name__ == "__main__":
    try:
        main()

    except FileNotFoundError as exc:
        print("Evidence error:", exc)

    except requests.Timeout:
        print("Ollama request timed out")

    except requests.ConnectionError:
        print("Cannot connect to Ollama. Is Ollama running?")

    except requests.HTTPError as exc:
        print("Ollama HTTP error:", exc)

    except json.JSONDecodeError:
        print("Model did not return valid JSON")

    except ValidationError as exc:
        print("RCA schema validation failed:")
        print(exc)
```

---

# 10. Setup

Create virtual environment if needed:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install:

```bash
pip install -r requirements.txt
```

Ensure Ollama is running and model is available:

```bash
ollama list
```

If needed, pull the model configured in the script.

Then:

```bash
python 07_first_ai_application.py
```

---

# ✅ Expected Style of Output

Exact wording may vary by model, but structure should be similar:

```json
{
  "root_cause": "The aks-subnet-allow NSG rule was removed before AKS subnet connectivity validation failed.",
  "impact": "AKS subnet connectivity validation failed and the deployment failed during Terraform Apply.",
  "recommended_fix": [
    "Review the Terraform change that removed the NSG rule.",
    "Restore or correct the required AKS subnet traffic rule after validation.",
    "Validate AKS subnet connectivity before redeployment."
  ],
  "severity": "high",
  "confidence": "medium"
}
```

Do not memorize this exact answer. The important thing is the pipeline.

---

# 🧪 Failure Tests You Should Perform

### Test 1 — Ollama stopped

Expected:

```text
Connection failure handled
```

### Test 2 — Wrong endpoint

Expected:

```text
HTTP/connection error
```

### Test 3 — Empty log file

Expected:

```text
RCA blocked before LLM call
```

### Test 4 — Model returns malformed JSON

Expected:

```text
JSON parsing failure
```

### Test 5 — Invalid severity

Expected:

```text
Pydantic validation failure
```

This is how you test an AI application — not only by checking happy path.

---

# 🔒 Production Improvements

This mini-project is educational. Production upgrade path:

```text
Local file
 ↓
Real Azure DevOps / GitHub / AKS evidence API
 ↓
Central configuration
 ↓
Managed identity / secure secret store
 ↓
Provider SDK with retry policy
 ↓
Telemetry + request IDs
 ↓
Structured output feature
 ↓
Evidence-level claim validation
 ↓
Human approval for remediation
```

---

# 🧠 Module 3 Grand Revision

```text
API Fundamentals
      ↓
REST
      ↓
HTTP
      ↓
JSON
      ↓
Authentication
      ↓
Secrets
      ↓
Minimal Python
      ↓
LLM API Call
      ↓
Provider Concepts
      ↓
Error Handling
      ↓
Structured Responses
      ↓
First AI Application
```

---

# 🎓 Final Takeaway

Module 1 me humne AI tools and trusted RCA explore kiya.

Module 2 me prompt behavior control kiya.

Module 3 me humne underlying application mechanics deeply connect ki:

```text
Prompt
 +
Python
 +
HTTP API
 +
Authentication
 +
JSON
 +
Errors
 +
Schema Validation
 =
Reliable AI Application Foundation
```

🚩 **Jai Bajrangbali — Learn • Build • Automate • Impact**
