# 🚩 Jai Bajrangbali!

# Lesson 07 — Minimal Python for AI Applications

> **Goal Python expert banna nahi; goal itna Python samajhna hai ki AI application ko confidently read, modify aur debug kar sako.**

---

## 🎯 Lesson Goal

Aap AI-app context me samjhoge:

- variables and types
- list and dict
- functions
- conditionals and loops
- imports
- exceptions
- file reading
- environment variables
- HTTP/API calls
- simple data validation

---

## 1. Variables

```python
model = "qwen2.5:3b"
temperature = 0.2
max_retries = 3
is_production = False
```

Mental model:

```text
name → value
```

AI apps me variables generally configuration, prompt, response, status ya evidence hold karte hain.

---

## 2. String

```python
prompt = "Analyze this AKS deployment failure"
```

Multiline prompt:

```python
prompt = """
You are a DevOps incident analyst.
Use only supplied evidence.
Return root cause, impact and fix.
"""
```

f-string:

```python
environment = "production"
prompt = f"Analyze the deployment failure in {environment}."
```

---

## 3. List

```python
errors = [
    "Terraform apply failed",
    "AKS connectivity validation failed"
]
```

Loop:

```python
for error in errors:
    print(error)
```

Useful for messages, evidence items, tool results and validation errors.

---

## 4. Dictionary

```python
incident = {
    "environment": "production",
    "status": "failed",
    "severity": "high"
}
```

Access:

```python
print(incident["status"])
print(incident.get("severity"))
```

Dict is especially important because JSON objects naturally become Python dictionaries in many libraries.

---

## 5. Function

```python
def build_prompt(environment, evidence):
    return f"""
Environment: {environment}
Evidence:
{evidence}

Analyze the incident using only evidence.
"""
```

Mental model:

```text
Input
 ↓
Function
 ↓
Output
```

Tools from Module 1 were also Python functions.

---

## 6. Conditions

```python
if not evidence:
    print("No evidence available. RCA blocked.")
else:
    print("Evidence available. Continue analysis.")
```

Guardrails frequently use `if` conditions.

---

## 7. Exceptions

```python
try:
    result = call_api()
except Exception as exc:
    print("API call failed:", exc)
```

But production code me broad `Exception` ko blindly swallow mat karo. Specific exceptions, useful logging and clear failure behavior better hai.

---

## 8. Imports

```python
import os
import json
import requests
```

Third-party package:

```python
from dotenv import load_dotenv
```

---

## 9. Read a Log File

```python
from pathlib import Path

log_path = Path("sample_incident.log")

if not log_path.exists():
    raise FileNotFoundError(log_path)

logs = log_path.read_text(encoding="utf-8")
print(logs)
```

This directly connects to our real-tool evidence flow.

---

## 10. API Call Pattern

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    timeout=10
)

response.raise_for_status()
data = response.json()
print(data)
```

Core pattern:

```text
Build request
 ↓
Call API
 ↓
Check failure
 ↓
Parse response
 ↓
Use data
```

---

## 11. Small AI-App Skeleton

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def read_evidence(path):
    return Path(path).read_text(encoding="utf-8")


def build_prompt(evidence):
    return f"Analyze only this evidence:\n\n{evidence}"


def main():
    evidence = read_evidence("sample_incident.log")

    if not evidence.strip():
        raise RuntimeError("No incident evidence")

    prompt = build_prompt(evidence)
    print(prompt)


if __name__ == "__main__":
    main()
```

Important line:

```python
if __name__ == "__main__":
```

Means: jab file directly run ho, tab `main()` execute karo.

---

# 🧠 What You Do NOT Need Yet

Module 3 ke liye immediately required nahi:

```text
advanced decorators
metaclasses
complex algorithms
advanced generators
low-level concurrency internals
```

Later need aayegi tab seekhenge.

---

# ❌ Common Mistakes

- indentation error
- `=` vs `==`
- dict key misspelling
- file path issue
- package install wrong virtual environment me karna
- exception ko ignore karna
- `None` value ko valid string samajh lena

---

# 🎤 Interview Point

AI application engineer ke liye Python ka practical focus hota hai:

> APIs, JSON, functions, validation, error handling, filesystem, environment/configuration and integration logic.

---

# 🔁 Why Next Lesson?

Ab saare building blocks ready hain. Next me hum complete LLM API call ko line-by-line break karenge:

> **Lesson 08 — Calling an LLM through an API**
