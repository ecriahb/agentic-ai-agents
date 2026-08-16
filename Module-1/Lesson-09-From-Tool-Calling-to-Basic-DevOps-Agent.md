# Module 1 — Lesson 9: From Tool Calling to a Basic DevOps Agent

> **Goal:** Single tool call ko controlled multi-step investigation loop me convert karna.

## English definition
**A basic agent repeatedly decides what information it needs, requests an allowed tool, observes the result, updates state and stops when the task is complete or a safety limit is reached.**

## Tool call vs agent

```text
Tool Calling
Question → one tool → result → answer

Agent Loop
Question
  ↓
Decide
  ↓
Act / Tool Request
  ↓
Host Validation + Execution
  ↓
Observe Evidence
  ↓
Update State
  ↓
Decide Again or Finish
```

## Agent is not magic
An agent is an application pattern built from concepts already learned:

```text
Prompt
+ LLM
+ Tools
+ State
+ Loop
+ Validation
+ Stop Condition
```

## DevOps incident example
Question:

```text
Why did production AKS deployment fail after Terraform change?
```

Possible controlled sequence:

```text
1. get_pipeline_status(production) → E1
2. get_terraform_changes(production) → E2
3. get_aks_status(prod-aks) → E3
4. enough evidence? yes
5. generate evidence-grounded RCA
```

## State
State preserves investigation observations:

```python
state = {
    "question": question,
    "evidence": [],
    "called_tools": [],
    "iteration": 0,
}
```

Important:

```text
State != model memory
State != authorization
State != automatically trusted truth
```

Only validated tool results should enter trusted evidence state.

## Stop conditions
Agent must not loop forever.

Examples:

- required evidence collected
- no useful tool remains
- max iterations reached
- repeated duplicate call
- invalid tool request
- user/human approval required
- insufficient evidence

## No evidence → no forced RCA
If tools fail or useful evidence is absent:

```text
Status: INSUFFICIENT_EVIDENCE
```

is better than invented root cause.

## V1 → V4 learning evolution

```text
V1 Basic multi-tool loop
 ↓
V2 Better environment/cluster arguments
 ↓
V3 State + duplicate-call protection + evidence grounding
 ↓
V4 Investigation separated from structured RCA reporting
```

Then real-tool practical adds:

```text
Hard-coded tool
→ real pipeline.log
→ no-tool guardrail
→ preserved evidence
→ evidence-only reporting
→ Pydantic
→ argument validation
→ deterministic impact
→ confidence policy
```

## Practical
Run in order:

```powershell
python examples/devops_agent_v1.py
python examples/devops_agent_v2.py
python examples/devops_agent_v3.py
python examples/devops_agent_v4.py
```

Then continue to:

```text
examples/lesson-05-real-tool-practical/
```

Do not run V4 first. Difference between versions is the lesson.

## What learner must inspect
For each version answer:

1. What changed?
2. Which new failure is prevented?
3. What is LLM-controlled?
4. What is host-controlled?
5. What counts as evidence?
6. What happens when evidence is missing?

## Production upgrade path
Basic agent is not production agent. Production adds:

- authentication
- authorization/RBAC
- tool allowlists
- typed argument validation
- timeouts/retries
- idempotency for writes
- audit trail
- trace IDs
- loop budgets
- human approval
- post-action verification

## Interview questions
1. Agent aur tool calling me difference?
2. Agent state ka purpose?
3. Infinite loop kaise prevent karoge?
4. Why no-evidence should stop RCA?
5. LLM ko executor kyun nahi banana chahiye?

## Revision

```text
Agent = bounded decide→act→observe loop
State = explicit workflow data
Evidence = validated observations
Host = policy + execution owner
Stop condition = mandatory safety control
```

## Next
Ab concepts complete hain. Section **A — Complete Lab Code** me poora Module 1 ek coherent practical path me assemble hoga.