# Module 1 — B: Troubleshooting Playbook

> **Goal:** Beginner ko random code changes se bachana aur errors ko category-by-category diagnose karna.

## Troubleshooting mental model

```text
Environment
→ Dependency
→ Credential
→ Provider
→ Network
→ Request
→ Response
→ Tool
→ Evidence
→ Validation
```

Always identify layer first.

## 1. `python` not found
Check:

```powershell
python --version
```

If unavailable, install supported Python and reopen terminal.

## 2. Virtual environment activation issue
Create:

```powershell
python -m venv .venv
```

Activate on Windows:

```powershell
.venv\Scripts\activate
```

If PowerShell policy blocks scripts, follow your machine/organization's approved user-scoped execution-policy process.

## 3. `ModuleNotFoundError`
Verify active interpreter and install requirements:

```powershell
python -m pip install -r Module-1/examples/requirements.txt
```

Prefer `python -m pip` so pip belongs to the same interpreter.

## 4. `OPENAI_API_KEY` missing
Do not hard-code it. Check only existence:

```python
import os
print(bool(os.getenv("OPENAI_API_KEY")))
```

If using `.env`, ensure `load_dotenv()` runs and working directory is correct.

## 5. OpenAI authentication / billing / model error
Separate categories:

```text
Authentication → credential/account
Quota/billing  → API account limits
Rate limit     → request pacing/quota
Model access   → configured model unavailable
Network        → connectivity/proxy/TLS
```

Do not treat all provider errors as Python bugs.

## 6. Ollama command not found

```powershell
ollama --version
```

If installed recently, reopen terminal.

## 7. Ollama model not found

```powershell
ollama list
ollama pull qwen3:4b
```

Or configure a model you actually have.

## 8. Connection refused on port 11434
Ollama runtime/service is unavailable. Verify:

```powershell
ollama list
```

Then retry local API call.

## 9. Local model too slow
Possible reasons:

- model too large
- insufficient RAM
- CPU-only inference
- competing processes

Use a smaller learning model before changing application logic.

## 10. Response exists but `output_text` missing/unexpected
Inspect response structure/provider path. Do not assume every provider-compatible endpoint exposes identical metadata.

Print type/known safe metadata, not secrets.

## 11. Structured output validation fails
Check:

- missing field
- wrong data type
- invalid enum/literal
- malformed JSON/model capability

Important: if schema passes, factual validation can still fail.

## 12. Model did not call a tool
This is not automatically an exception. Host should handle:

```text
NO_TOOL_CALLED
or
INSUFFICIENT_EVIDENCE
```

Do not generate an RCA from nonexistent evidence.

## 13. Model invented tool name
Block via allowlist:

```python
ALLOWED_TOOLS = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}
```

Unknown tool → reject before execution.

## 14. Model invented/wrong arguments
Validate arguments and targets before execution.

Examples:

```text
production vs prod
prod-aks vs production
unknown environment
unexpected extra field
```

Tool schema helps; host validation is still required.

## 15. Duplicate tool loop
Track called operations/arguments and enforce max iterations/no-progress policy.

```text
same call repeatedly
→ no new evidence
→ stop
```

## 16. Tool returns no data
Represent explicitly:

```text
TOOL_ERROR
NO_DATA
NOT_FOUND
```

A failed tool call is not proof that the system is healthy or unhealthy.

## 17. Final RCA invents customer impact
Do not ask model alone to decide impact. Extract deterministic confirmed impact from evidence where possible.

Example supported:

```text
Deployment failed during Terraform Apply
```

Unsupported without evidence:

```text
All customers experienced an outage for 45 minutes
```

## 18. Confidence looks too high
Confidence should be policy/calibration driven, not model emotion.

Possible learning policy:

```text
one evidence source → medium max
multiple independent current sources → can increase
conflicting/missing evidence → lower
```

## Debug worksheet
For every error write:

```text
Stage:
Exact error/status:
Expected behavior:
Actual behavior:
Provider involved?:
Tool involved?:
Evidence available?:
Validation result?:
Smallest reproducible test:
Fix:
What did I learn?:
```

## Final troubleshooting rule

```text
Do not change five things at once.
Find the failing layer.
Make one controlled change.
Rerun.
```
