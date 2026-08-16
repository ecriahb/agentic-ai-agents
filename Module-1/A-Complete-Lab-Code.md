# Module 1 — A: Complete Lab Code

> **Goal:** Module 1 ke scattered concepts ko ek complete beginner-to-trusted-RCA practical journey me assemble karna.

## Lab progression

```text
A1 Hosted/OpenAI call
A2 Local/Ollama call
A3 Structured RCA
A4 Basic tool request
A5 DevOps Agent V1
A6 DevOps Agent V2
A7 DevOps Agent V3
A8 DevOps Agent V4
A9 Real pipeline.log tool
A10 Final trusted RCA
```

## Files

### A1 — First cloud call
`examples/01_first_ai_call.py`

Learn:
- OpenAI client
- request
- response object
- output text

### A2 — First local call
`examples/02_ollama_ai_call.py`

Learn:
- local endpoint
- installed model
- cloud/local parity idea

### A3 — Structured output
`examples/03_structured_output.py`

Learn:
- output contract
- validation
- schema != truth

### A4 — Tool call
`examples/04_tool_call_basic.py`

Learn:

```text
LLM request
→ host validation
→ Python execution
→ result
```

### A5–A8 — Agent evolution

```text
examples/devops_agent_v1.py
examples/devops_agent_v2.py
examples/devops_agent_v3.py
examples/devops_agent_v4.py
```

Run sequentially.

### A9–A10 — Real tool practical
Open:

`examples/lesson-05-real-tool-practical/README.md`

Evolution:

```text
pipeline.log
   ↓
real file-reading tool
   ↓
Qwen tool request
   ↓
no-tool guardrail
   ↓
evidence preservation
   ↓
evidence-only reporter
   ↓
Pydantic
   ↓
tool name/arg validation
   ↓
deterministic impact
   ↓
confidence policy
   ↓
Trusted RCA
```

## Evidence fixture

```text
Terraform Apply started
NSG rule aks-subnet-allow removed
AKS subnet connectivity validation failed
Deployment failed during Terraform Apply
```

## Final architecture

```text
User Incident
    ↓
Host App
    ↓
LLM proposes investigation
    ↓
Allowed Read-Only Tool
    ↓
Validated Evidence
    ↓
Evidence Store
    ↓
Grounded RCA Prompt
    ↓
Structured RCA Candidate
    ↓
Schema + Citation + Business Validation
    ↓
Trusted Report
```

## Acceptance criteria
Lab complete tab maana jayega jab learner explain kar sake:

- hosted and local provider difference
- response object anatomy
- structured output limitation
- tool request vs execution
- evidence preservation
- agent state
- no-evidence guardrail
- allowlist/argument validation
- deterministic impact/confidence policy

## Failure drills
Run intentionally:

1. missing API key
2. Ollama stopped
3. unavailable model
4. unknown tool name
5. wrong environment
6. no tool called
7. empty evidence
8. schema-valid but unsupported impact

Every failure ke liye identify karo:

```text
Provider failure?
Tool failure?
Validation failure?
Evidence gap?
Policy block?
```

## Provider parity
Where practical, run same question/evidence against both:

```text
Ollama local
OpenAI hosted
```

Compare wording/quality, but keep evidence and host policy identical.

## Lab rule
Do not copy final code first. Build sequentially. **Difference between versions is the real lesson.**