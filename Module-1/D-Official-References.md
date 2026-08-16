# Module 1 — D: Official References

> **Goal:** Version-sensitive APIs/frameworks ke liye learner ko authoritative documentation tak le jana. Course notes concept explain karte hain; current syntax/provider behavior official docs se verify karna chahiye.

## OpenAI
Use official OpenAI documentation for:

- Python SDK installation
- Responses API
- authentication/environment variables
- model availability
- structured outputs
- tool/function calling
- usage/rate limits
- current API pricing

Important: model names, SDK versions, pricing and feature availability change over time. Keep them configurable instead of assuming one permanent name.

## Ollama
Use official Ollama documentation for:

- installation
- model pulling/running
- local API
- OpenAI-compatible endpoint support
- model/runtime requirements

Useful commands to remember:

```powershell
ollama --version
ollama list
ollama pull <model>
ollama run <model>
```

## Python
Use official Python documentation for:

- virtual environments (`venv`)
- exceptions
- typing
- standard library behavior

## Pydantic
Use official Pydantic documentation for:

- `BaseModel`
- field validation
- enums/literals
- validation errors
- model serialization

Remember: Pydantic is a data/schema validation layer, not a factual-truth engine.

## Security references
For production design, also consult authoritative security guidance for:

- secret management
- least privilege
- identity/RBAC
- audit logging
- safe tool execution
- human approval for risky operations

Later modules cover these systematically.

## How to use references while studying

```text
Course lesson
   ↓
Understand concept
   ↓
Run repository practical
   ↓
If API/framework behavior is version-sensitive
   ↓
Verify current official documentation
```

Do not replace understanding with copy-paste from docs.

## Version-sensitive checklist
Before running examples months later, verify:

```text
Python supported version
OpenAI SDK major version
OpenAI model configured for your account
Ollama installed version
Local model actually installed
Pydantic major version
Any framework/module-specific requirements
```

## Repo-local references
Also read:

- `START-HERE.md`
- `MODEL-PROVIDERS.md`
- `DUAL-PROVIDER-LABS.md`
- `PRACTICALS-INDEX.md`
- `Module-1/PRACTICAL-ROADMAP.md`
- `Module-1/B-Troubleshooting-Playbook.md`

## Final reminder

> **For fast-changing SDK/API details, official documentation is the source of truth. For course architecture, keep the stable mental model: Evidence → Context → Model → Validation → Policy.**