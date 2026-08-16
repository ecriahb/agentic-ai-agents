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
        ↓
lesson-05-real-tool-practical/
```

## Version Progression

| Version | Learning Goal |
|---|---|
| V1 | Basic multi-tool agent loop |
| V2 | Better tool arguments + production evidence |
| V3 | State / duplicate-call protection + grounded wording |
| V4 | Investigation separated from structured RCA reporting |
| Lesson-05 Real Tool Practical | Real `pipeline.log` → Qwen → evidence guardrails → trusted RCA |

## Lesson 05 — Real Tool Practical

The complete live practical is preserved here:

[`lesson-05-real-tool-practical/README.md`](lesson-05-real-tool-practical/README.md)

Exact progression:

```text
pipeline.log
   ↓
real tool
   ↓
Qwen tool call
   ↓
no-tool guardrail
   ↓
evidence_log
   ↓
V3 evidence-only reporting
   ↓
V4 Pydantic
   ↓
tool-argument hallucination
   ↓
allowlist + argument validation
   ↓
deterministic impact extraction
   ↓
confidence policy
   ↓
final trusted RCA
```

Runnable files:

```text
lesson-05-real-tool-practical/logs/pipeline.log
lesson-05-real-tool-practical/real_tool_qwen_v1.py
lesson-05-real-tool-practical/real_tool_qwen_v2_guardrail.py
lesson-05-real-tool-practical/real_tool_qwen_v3.py
lesson-05-real-tool-practical/real_tool_qwen_v4.py
lesson-05-real-tool-practical/real_tool_qwen_v4_final.py
```

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

> Earlier DevOps-agent files use simulated evidence for learning. The Lesson-05 real-tool practical reads the actual local `pipeline.log` file at runtime, so the evidence is no longer hard-coded inside the tool function.
