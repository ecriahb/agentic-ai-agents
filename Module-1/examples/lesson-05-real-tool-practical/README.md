# Lesson 05 Practical — Real Tool → Trusted RCA

Ye folder **16 Aug 2026 ko kiya gaya hands-on practical** exact learning sequence me preserve karta hai.

## Practical Goal

Fake/hard-coded DevOps tool se nikal kar ek real local evidence source (`pipeline.log`) ko Qwen tool calling ke through read karna, evidence preserve karna, hallucination guardrails add karna, aur final trusted RCA produce karna.

## Exact Sequence

```text
pipeline.log
   ↓
real file-reading tool
   ↓
Qwen tool call
   ↓
no-tool guardrail
   ↓
evidence_log / preserved evidence
   ↓
V3 evidence-only reporting
   ↓
V4 Pydantic validation
   ↓
tool-argument hallucination discovered
   ↓
tool allowlist + argument validation
   ↓
deterministic impact extraction
   ↓
confidence policy
   ↓
FINAL TRUSTED RCA
```

---

## 1. Real Evidence — `logs/pipeline.log`

The practical started with an actual file instead of a hard-coded Python return value:

```text
2026-08-16 10:02:11 - Pipeline started
2026-08-16 10:02:45 - Terraform init completed
2026-08-16 10:03:18 - Terraform plan completed
2026-08-16 10:04:01 - Terraform apply started
2026-08-16 10:04:37 - ERROR:
Network Security Group rule aks-subnet-allow was removed.
2026-08-16 10:04:41 - ERROR:
AKS subnet connectivity validation failed.
2026-08-16 10:04:45 - Deployment failed during Terraform Apply.
```

This is why the tool is now a **real local tool**: Python reads evidence from disk at runtime.

---

## 2. V1 — Real Tool + Qwen Tool Calling

File:

```text
real_tool_qwen_v1.py
```

Main learning:

```text
User Goal
   ↓
Qwen decides a tool is needed
   ↓
Qwen REQUESTS read_pipeline_log
   ↓
Python host executes the function
   ↓
Real pipeline.log is returned
   ↓
Qwen receives observation
   ↓
RCA
```

Important:

> The LLM does not execute Python. It only requests the tool. The host program validates and executes it.

Expected tool request shape:

```text
===== TOOL REQUESTED =====
Tool: read_pipeline_log
Arguments: {}
```

---

## 3. No-Tool Guardrail

Problem:

An LLM can sometimes answer directly without using the evidence tool.

Unsafe flow:

```text
Question
  ↓
LLM guesses
  ↓
RCA
```

Guardrail added in `real_tool_qwen_v2_guardrail.py`:

```text
No tool call
   ↓
No evidence
   ↓
RCA BLOCKED
```

Rule:

> **No evidence = no RCA.**

---

## 4. Preserve Evidence Separately

Tool observations are stored in:

```python
evidence_log = [
    {
        "tool": "read_pipeline_log",
        "observation": "...actual log content..."
    }
]
```

Why?

Because chat history is not our source of truth. The actual tool observation must be preserved independently.

Terminal section:

```text
===== PRESERVED EVIDENCE =====
Tool: read_pipeline_log
Observation:
...
```

---

## 5. V3 — Evidence-Only Reporting

File:

```text
real_tool_qwen_v3.py
```

V3 separates two responsibilities:

```text
INVESTIGATION
Qwen → Tool → Evidence

REPORTING
Evidence only → RCA Reporter
```

The final reporter does **not** receive the whole investigation conversation. It receives only the preserved trusted evidence.

This reduces contamination from earlier model guesses.

---

## 6. V4 — Pydantic Structured Validation

File:

```text
real_tool_qwen_v4.py
```

Schema:

```python
class FinalRCA(BaseModel):
    evidence: list[str]
    likely_root_cause: str
    confirmed_impact: list[str]
    recommended_fix: list[str]
    confidence: Literal["low", "medium", "high"]
```

Then:

```python
FinalRCA.model_validate_json(...)
```

What Pydantic guarantees:

- required fields exist
- field types are correct
- confidence uses allowed values
- malformed JSON/schema drift is rejected

What Pydantic does **not** guarantee:

- a sentence is factually supported by evidence
- impact is really confirmed
- tool arguments are legitimate

That gap led to the next practical discovery.

---

## 7. Tool-Argument Hallucination

During the practical, the model could request the correct tool but invent an argument that the tool never defined, for example:

```text
Tool: read_pipeline_log
Arguments: {"environment": "production"}
```

But our contract is:

```python
def read_pipeline_log():
    ...
```

It accepts **zero arguments**.

Important lesson:

> Correct tool name does not mean the complete tool call is trustworthy.

The host must validate both:

```text
Tool name
AND
Tool arguments
```

---

## 8. Tool Allowlist + Argument Validation

Implemented in:

```text
real_tool_qwen_v4_final.py
```

Allowlist:

```python
TOOL_REGISTRY = {
    "read_pipeline_log": {
        "function": read_pipeline_log,
        "allowed_arguments": set(),
    }
}
```

Validation blocks:

- unknown tool names
- invented arguments
- parameters outside the tool contract

Flow:

```text
LLM tool request
   ↓
Allowlisted tool?
   ↓
Arguments valid?
   ↓
YES → execute
NO  → block
```

---

## 9. Deterministic Impact Extraction

An LLM can infer unsupported production/customer impact even when the log only proves deployment failure.

So final hardening does not blindly trust generated `confirmed_impact`.

Impact terms are filtered against actual evidence and the code can deterministically extract lines containing terms such as:

```text
failed
failure
degraded
unavailable
outage
downtime
error
blocked
```

For this log, the directly supported impact is the deployment/connectivity failure shown in the evidence. We should not automatically claim customer downtime when the log does not prove it.

---

## 10. Evidence Support Check

Final version includes `evidence_supports_claim()`.

Purpose:

```text
Generated claim
   ↓
Compare important tokens with trusted evidence
   ↓
Supported?
   ├─ YES → keep/check further
   └─ NO  → reject/block
```

This is a simple deterministic safety layer for the practical—not a complete semantic verification engine.

---

## 11. Confidence Policy

Only one evidence source is currently collected:

```text
read_pipeline_log
```

Therefore the final policy does not allow the model to self-award `high` confidence from a single source.

Rule used in the practical:

```text
requested confidence = high
AND evidence_source_count < 2
        ↓
confidence = medium
```

This teaches a key production pattern:

> Confidence should be policy-controlled, not only model-generated.

---

## 12. Controlled Repair Attempt

If Pydantic rejects the generated JSON, the final version allows one repair attempt.

But repair is restricted to:

```text
JSON / schema structure repair
```

It must not introduce new evidence or facts.

---

## 13. Final Trusted RCA Architecture

```text
                    USER GOAL
                        │
                        ▼
                  Qwen Investigator
                        │
                requests tool call
                        │
                        ▼
             Tool Allowlist Validation
                        │
             Argument Contract Validation
                        │
                        ▼
                Python Tool Execution
                        │
                        ▼
                  pipeline.log
                        │
                        ▼
                 evidence_log
                        │
                        ▼
               Evidence-Only Reporter
                        │
                        ▼
                 Pydantic Schema
                        │
                        ▼
             Evidence Support Validation
                        │
                        ▼
          Deterministic Impact Validation
                        │
                        ▼
               Confidence Policy
                        │
                        ▼
                 TRUSTED RCA
```

---

## Confirmed Evidence from This Practical

```text
1. Terraform apply started.
2. NSG rule aks-subnet-allow was removed.
3. AKS subnet connectivity validation failed.
4. Deployment failed during Terraform Apply.
```

### Evidence-grounded root cause

The strongest evidence points to removal of the `aks-subnet-allow` NSG rule causing AKS subnet connectivity validation to fail during Terraform Apply.

### Confirmed impact

The deployment failed during Terraform Apply and AKS subnet connectivity validation failed.

### Recommended fix

Restore/correct the required NSG rule, validate AKS subnet connectivity, review the Terraform change/plan, and rerun the deployment after validation.

### Confidence

`medium` under the practical confidence policy because only one evidence source (`pipeline.log`) has been collected.

---

## Run Order

From this folder:

```powershell
python .\real_tool_qwen_v1.py
python .\real_tool_qwen_v2_guardrail.py
python .\real_tool_qwen_v3.py
python .\real_tool_qwen_v4.py
python .\real_tool_qwen_v4_final.py
```

Required local model:

```powershell
ollama pull qwen3:0.6b
```

Dependencies are already included in the Module-1 `examples/requirements.txt`:

```text
ollama
pydantic
```

---

## Final Learning

We did **not** jump directly from fake tool to a production-safe agent.

The actual progression was:

```text
Real data source
→ Real tool
→ Tool calling
→ Evidence
→ Guardrail
→ Evidence-only reasoning
→ Schema validation
→ Tool contract validation
→ Business/evidence validation
→ Deterministic controls
→ Confidence policy
→ Trusted RCA
```

That progression is the main practical lesson.
