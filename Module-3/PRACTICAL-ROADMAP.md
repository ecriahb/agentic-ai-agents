# Module 3 — Zero-to-Hero Practical Roadmap

> Goal: beginner ko HTTP/API/Python basics se ek robust AI application tak le jana—without assuming strong Python knowledge.

## Setup
```powershell
cd Module-3/examples
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## V1 — First HTTP GET
Run: `01_api_get_request.py`

**Learn:** URL, request, status code, response body.

Before AI APIs, normal HTTP request samajhna mandatory hai.

---

## V2 — JSON Basics
Run: `02_json_basics.py`

Change fields, nested values and print selected keys.

**Pass:** learner Python dict vs JSON text ka difference explain kare.

---

## V3 — Environment Variables / Secrets
Run: `03_env_secret_demo.py`

Test:
- variable present
- variable missing

**Rule:** secret code me hard-code nahi karna.

---

## V4 — First Local LLM API Call
Run: `04_ollama_llm_call.py`

Identify:
```text
endpoint
request JSON
model
prompt
HTTP response
generated text
```

---

## V5 — API Error Handling
Run: `05_api_error_handling.py`

Intentionally test:
- wrong endpoint
- Ollama stopped
- timeout
- bad payload

**Learning:** API error ko AI fact/evidence mat samjho.

---

## V6 — Structured RCA
Run: `06_structured_rca.py`

Take one simple incident and force predictable fields.

Then intentionally return malformed content and observe validation behavior.

---

## V7 — First Complete AI Application
Run: `07_first_ai_application.py`

Trace line-by-line:
```text
Input
→ Read evidence
→ Build prompt
→ Call model
→ Parse result
→ Validate
→ Print report
```

---

## V8 — Local vs OpenAI Provider
Run: `08_dual_provider_llm_call.py`

Same prompt, two backends.

Compare:
- response contract
- latency
- configuration
- cost/privacy implications

---

## V9 — Failure Matrix
Create a small table and execute each case:
```text
Missing input file
Empty evidence
Model unavailable
Wrong API key
Timeout
Malformed output
```

Application must show explicit error state rather than silently guess.

---

## V10 — Build Your Own Tiny DevOps AI CLI
Create `my_incident_analyzer.py` using what you learned:

Required behavior:
1. accepts log-file path
2. checks file exists
3. reads evidence
4. rejects empty evidence
5. selects Ollama/OpenAI provider
6. requests grounded analysis
7. catches API/model failures
8. prints explicit status + answer

### Acceptance Criteria
Learner can explain:
```text
Python app
→ HTTP/API
→ LLM provider
→ response
→ parsing
→ validation
→ error state
```

## Hero Outcome
Learner ab AI SDK code copy nahi karta; usko request/response/error lifecycle samajh aata hai.
