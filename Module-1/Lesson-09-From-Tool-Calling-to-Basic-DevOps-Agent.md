# Module 1 — Lesson 9: From Tool Calling to a Basic DevOps Agent

> **Goal:** Single tool request ko controlled multi-step DevOps investigation loop me convert karna, explicit state/evidence/stop conditions samajhna, V1→V4 evolution follow karna, aur final RCA ko evidence-grounded banana.

---

# 1. English Definition

**A basic AI agent is an application that repeatedly decides what information it needs, requests allowed tools, observes validated results, updates explicit state and stops when the goal is complete or a safety condition is reached.**

Simple Hinglish:

```text
Decide
  ↓
Request Tool
  ↓
Host Validate + Execute
  ↓
Observe Evidence
  ↓
Update State
  ↓
Decide Again or Stop
```

---

# 2. Why This Topic Comes Here

Lesson 8 me single tool calling samjha.

But real incident:

```text
"Production AKS deployment Terraform change ke baad kyun fail hua?"
```

Ek tool enough nahi.

Need correlation:

```text
Pipeline evidence
+ Terraform evidence
+ AKS evidence
```

This creates the need for an agent loop.

---

# 3. Chatbot vs Tool Call vs Agent

```text
Chatbot
Question → Model → Answer

Single Tool
Question → Model → Tool → Result → Answer

Agent
Goal
 → Decide
 → Tool
 → Observe
 → State
 → Decide again
 → More tool or final answer
```

Agent is not a new model.

```text
Existing LLM
+ Tools
+ State
+ Loop
+ Validation
+ Stop Conditions
= Agent Application
```

---

# 4. Core Agent Components

A basic agent needs:

```text
1. Goal / user request
2. LLM reasoner
3. Tool catalog
4. Host dispatcher
5. Argument validation
6. State
7. Evidence store
8. Loop
9. Stop conditions
10. Final reporting
```

If one of these is missing, behavior becomes fragile.

---

# 5. Recurring DevOps Incident

Question:

```text
Why did production AKS deployment fail after Terraform changes?
```

Available read-only tools:

```text
get_pipeline_status(environment)
get_terraform_changes(environment)
get_aks_status(cluster_name)
```

Expected evidence:

```text
E1: Pipeline failed during Terraform Apply
E2: NSG rule aks-subnet-allow removed
E3: AKS connectivity validation failed/degraded
```

---

# 6. Controlled Investigation Flow

```text
User Incident
     ↓
Agent asks: what evidence first?
     ↓
get_pipeline_status("production")
     ↓
E1 stored
     ↓
Agent asks: what changed?
     ↓
get_terraform_changes("production")
     ↓
E2 stored
     ↓
Agent asks: current AKS impact?
     ↓
get_aks_status("prod-aks")
     ↓
E3 stored
     ↓
Enough evidence?
     ├─ No → allowed next tool
     └─ Yes → RCA
```

---

# 7. State Kya Hai?

**State is information preserved by the host application across workflow steps.**

Simple example:

```python
state = {
    "question": question,
    "evidence": [],
    "called_tools": [],
    "iteration": 0,
}
```

State lets later decisions use earlier observations.

---

# 8. State != Model Memory

Important distinction:

```text
Application State
= explicit host-owned workflow data

Model Context
= what host sends to model in a request

Model Memory
= provider/framework-specific concept if available
```

Do not rely on vague conversational memory for operational evidence.

---

# 9. Evidence Store

Better than free-text accumulation:

```python
state["evidence"].append({
    "id": "E1",
    "source": "pipeline",
    "fact": "Deployment failed during Terraform Apply",
})
```

Then:

```text
E1
E2
E3
```

can be referenced in final RCA.

Benefits:

- traceability
- citations
- deduplication
- conflict checks
- deterministic validation

---

# 10. Decide → Act → Observe Loop

Pseudo-code:

```python
while state["iteration"] < MAX_ITERATIONS:
    decision = ask_model_for_next_step(state)

    if decision.type == "final":
        break

    validated = validate_tool_request(decision)
    result = execute_tool(validated)
    state["evidence"].append(normalize(result))
    state["iteration"] += 1
```

Important:

```text
LLM proposes next step
Host controls loop
```

---

# 11. Why Stop Conditions Are Mandatory

Without bounded loop:

```text
Tool A
→ Tool B
→ Tool A
→ Tool B
→ forever
```

Problems:

- cost
- latency
- rate limits
- resource consumption
- repeated external calls

Stop conditions:

```text
required evidence collected
max iterations reached
same call repeated
no new evidence
invalid tool request
no allowed tools remain
human approval required
insufficient evidence
```

---

# 12. Duplicate Call Protection

Suppose model repeatedly requests:

```text
get_aks_status(prod-aks)
```

Track key:

```python
call_key = (tool_name, tuple(sorted(arguments.items())))
```

If already called and evidence is still fresh:

```text
Do not blindly re-execute
```

Possible host action:

```text
reuse result
or
return NO_NEW_EVIDENCE
or
stop
```

---

# 13. No-Progress Detection

Even different calls can produce no useful evidence.

Example:

```text
Tool 1 → no data
Tool 2 → permission denied
Tool 3 → timeout
```

Agent should not hallucinate RCA.

Return:

```text
INSUFFICIENT_EVIDENCE
```

---

# 14. No Evidence → No Forced RCA

This is one of Module 1's most important rules.

Bad:

```text
Tools failed, but model says "probably DNS".
```

Better:

```json
{
  "status": "INSUFFICIENT_EVIDENCE",
  "missing": ["terraform_change", "aks_health"]
}
```

Abstention is a valid successful safety behavior.

---

# 15. V1 — Basic Multi-Tool Loop

File:

```text
examples/devops_agent_v1.py
```

Learning goal:

```text
Model can choose from multiple DevOps tools
Host executes requests
Results return to model
```

Observe:

- tool definitions
- dispatch
- repeated loop
- final response

Limitation:

```text
contracts/arguments can still be loose
state/evidence handling basic
```

---

# 16. V2 — Better Arguments and Mapping

File:

```text
examples/devops_agent_v2.py
```

Real problem encountered:

```text
get_aks_status("prod-aks") → valid
get_pipeline_status("prod-aks") → environment not found
get_terraform_changes("prod-aks") → no data
```

Why?

```text
AKS tool expects cluster name
Pipeline/Terraform expect environment
```

V2 lesson:

> **Correct tool + wrong argument = wrong/no evidence.**

Improvement:

- typed args
- environment/cluster mapping
- clearer contracts

---

# 17. V3 — Explicit State + Grounding

File:

```text
examples/devops_agent_v3.py
```

Problems addressed:

```text
Evidence loss
Repeated tool calls
Weak final grounding
```

Architecture:

```text
Tool 1 ┐
Tool 2 ├→ Evidence State → Final Reasoning
Tool 3 ┘
```

Host now preserves observations instead of relying on model to remember perfectly.

---

# 18. V4 — Investigation vs Reporting Separation

File:

```text
examples/devops_agent_v4.py
```

Better architecture:

```text
Investigation Loop
      ↓
Evidence Store
      ↓
Grounded RCA Generator
      ↓
Structured Output
      ↓
Validation
```

Why separate?

```text
Investigation = collect facts
Reporting = explain facts
```

Different responsibilities are easier to test independently.

---

# 19. Fake Tool → Real Tool Progression

Learning tool:

```python
def get_pipeline_status(environment):
    return "Failed during Terraform Apply"
```

Later real implementation:

```text
Python Tool
→ Azure DevOps/GitHub API
→ actual pipeline status
→ normalize
→ evidence
```

The agent logic can remain similar if tool contracts stay stable.

---

# 20. Real-Tool Practical

Continue after V1–V4:

```text
examples/lesson-05-real-tool-practical/
```

Progression:

```text
pipeline.log
→ real file-reading tool
→ model tool request
→ no-tool guardrail
→ evidence preservation
→ evidence-only reporter
→ Pydantic
→ tool allowlist
→ argument validation
→ deterministic impact
→ confidence policy
→ trusted RCA
```

This is the real Module 1 hero path.

---

# 21. Grounded RCA

Current evidence:

```text
[E1] Deployment failed during Terraform Apply
[E2] NSG rule aks-subnet-allow removed
[E3] AKS connectivity validation failed
```

Supported conclusion:

```text
The NSG rule removal is the strongest evidence-supported cause of the subsequent AKS connectivity failure and deployment failure.
```

Unsupported without evidence:

```text
All customers experienced 45 minutes of downtime.
```

---

# 22. Deterministic Impact

If evidence already explicitly states:

```text
Deployment failed
```

Host can set confirmed impact:

```text
Deployment failure
```

Do not ask model to embellish.

This reduces hallucination.

---

# 23. Confidence Policy

Model saying:

```text
"I am 99% confident"
```

is not enough.

Learning policy:

```text
No evidence → insufficient
One source → medium max
Multiple independent agreeing sources → can increase
Conflicting evidence → reduce
```

Host owns confidence policy.

---

# 24. Tool Failure Handling

Example:

```text
get_aks_status → permission denied
```

Do not treat as:

```text
AKS healthy
```

Represent:

```text
AKS status unverified because tool lacked permission
```

Tool failure is workflow state, not system-state proof.

---

# 25. Human Approval Boundary

Basic Module 1 agent should investigate/read only.

If remediation is suggested:

```text
Agent RCA
→ Proposed Fix
→ Human Review
→ Existing CI/CD Workflow
→ Controlled Apply
```

Not:

```text
LLM
→ unrestricted shell
→ production mutation
```

---

# 26. Authentication and RBAC Preview

Real tools eventually need:

```text
Identity
→ Authentication
→ Authorization / RBAC
→ Least Privilege
```

Agent should not receive raw secrets.

Credentials stay in tool/application layer.

---

# 27. Audit and Traceability

For each incident record:

```text
incident_id
agent/version
tool name
validated args
tool result/source ID
model/provider
final citations
validation status
approval status
```

This lets you reconstruct:

```text
What did agent know?
Which tools ran?
Why did it conclude this?
```

---

# 28. Local vs OpenAI Provider

You may use Ollama or OpenAI as the reasoning backend.

Architecture must remain:

```text
Provider
→ proposes
Host
→ validates
Tool
→ collects evidence
Host
→ validates final RCA
```

Provider switch must not change execution authority.

---

# 29. Production Upgrade Path

Module 1 basic agent is learning architecture.

Production later adds:

```text
Authentication
RBAC
MCP/tool gateways
timeouts/retries
idempotency
state persistence
RAG
LangGraph
multi-agent coordination
security evals
observability
HA/DR
```

These are covered in later modules.

---

# 30. Common Beginner Mistakes

1. Agent = newly trained model.
2. Tool calling alone = full agent.
3. State = conversation memory only.
4. Every tool result trusted automatically.
5. No max iterations.
6. Duplicate calls allowed forever.
7. Tool failure interpreted as healthy.
8. Final RCA generated without evidence.
9. Model confidence trusted directly.
10. Remediation executed without approval/RBAC.
11. Provider switch changes safety policy.
12. V4 run directly without understanding V1→V3.

---

# 31. Practical Run Order

```powershell
python examples/devops_agent_v1.py
python examples/devops_agent_v2.py
python examples/devops_agent_v3.py
python examples/devops_agent_v4.py
```

Then:

```text
examples/lesson-05-real-tool-practical/README.md
```

For every version answer:

```text
What changed?
Why was change required?
What failure does it prevent?
What is model-controlled?
What is host-controlled?
What is evidence?
What is stop condition?
```

---

# 32. Hero Acceptance Criteria

Module 1 agent practical complete tab maana jayega when learner can explain:

```text
LLM = reasoner
Host = executor + policy owner
Tool request = untrusted proposal
Tool result = evidence candidate
State = explicit workflow data
Loop = bounded decide→act→observe
No evidence = no forced RCA
Schema = shape, not truth
Confidence = host policy
Write action = authorization + approval
```

---

# 33. Interview Q&A

### Q1. What is an AI agent?
An application that uses a model to make bounded decisions, invoke allowed tools through a host, observe results, maintain state and continue until a stop condition.

### Q2. Agent vs chatbot?
Chatbot generally responds directly; agent can perform multi-step tool-based workflows.

### Q3. Agent vs tool calling?
Tool calling is a capability request; agent orchestrates potentially multiple calls/state/decisions.

### Q4. What is state?
Host-preserved workflow information used across steps.

### Q5. How do you stop infinite loops?
Max iterations, duplicate-call detection, no-progress detection and explicit termination policies.

### Q6. Why no evidence → no RCA?
Otherwise model may fabricate incident-specific facts.

### Q7. What improved in V2?
Argument contracts/mapping.

### Q8. What improved in V3?
Explicit evidence state, grounding and duplicate protection.

### Q9. What improved in V4?
Investigation separated from structured RCA reporting/validation.

### Q10. Should AI agent directly execute Terraform Apply?
Not by default; safer pattern is read-only investigation, recommendation, authorization/human approval and controlled existing CI/CD execution.

---

# 34. Revision Sheet

```text
Agent = bounded application loop around existing model
Loop = Decide → Act → Observe → Repeat/Stop
State = explicit host-owned workflow data
Evidence = validated source observation
Grounding = reason from evidence
Stop conditions = mandatory safety control
Tool failure != healthy evidence
No evidence = abstain
Host = execution/policy authority
```

---

# 35. Homework

1. Draw V1→V4 architecture evolution.
2. Add `MAX_ITERATIONS` to a toy loop.
3. Add duplicate-call tracking.
4. Simulate one tool timeout and ensure RCA abstains.
5. Label evidence E1/E2/E3.
6. Write a final RCA that cites only E1-E3.
7. Add one unsupported claim and design a validator to reject it.
8. Explain how fake pipeline tool would become real Azure DevOps/GitHub API tool without changing agent mental model.

---

# 36. What Comes Next?

Module 1 mechanics complete:

```text
API
→ Local/Cloud Model
→ Response
→ Tokens/Context
→ Structured Output
→ Tools
→ Agent
→ Evidence-Grounded RCA
```

Now Module 2 asks:

```text
Model ko reliable instructions, context boundaries,
abstention rules and output contracts kaise design karein?
```

Before Module 2, complete:

- **A — Complete Lab Code**
- **B — Troubleshooting Playbook**
- **C — Interview & Revision Sheet**
- **D — Official References**