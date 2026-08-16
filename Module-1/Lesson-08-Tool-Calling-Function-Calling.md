# Module 1 — Lesson 8: Tool Calling / Function Calling

> **Goal:** Model ko external capability request karna sikhna while keeping actual execution, validation, authorization and evidence handling inside the host application.

---

# 1. English Definition

**Tool calling is a pattern where a model requests a predefined external capability with structured arguments, while the host application validates and executes the actual tool.**

Simple Hinglish:

```text
LLM says: "Mujhe ye tool chahiye"
Host says: "Allowed hai? Args valid hain?"
Python says: "Main actual function execute karta hoon"
```

Golden rule:

> **LLM proposes. Host decides. Tool executes.**

---

# 2. Why This Topic Comes Here

Lesson 7 me model output ko structured contract me laaya.

Ab problem:

```text
Model ke paas current AKS/pipeline/Terraform state nahi hota.
```

To current evidence kaise milega?

```text
Tool calling
```

---

# 3. Basic Mental Model

```text
User Question
     ↓
LLM decides more evidence is needed
     ↓
Tool Request
{name, arguments}
     ↓
HOST VALIDATION
     ↓
Python Function / API Call
     ↓
Tool Result
     ↓
Normalize as Evidence
     ↓
LLM receives evidence
     ↓
Final Answer
```

---

# 4. Tool vs Function vs Tool Contract

A Python function:

```python
def get_aks_status(cluster_name: str) -> dict:
    return {
        "cluster": cluster_name,
        "status": "degraded",
    }
```

The **tool contract** exposes enough information so model/application understand:

```text
Name
Purpose
Arguments
Types
Expected behavior
```

The implementation can later change from fake data to real Azure/Kubernetes API without changing the conceptual contract.

---

# 5. Fake Tool First

Learning version:

```python
def get_pipeline_status(environment: str) -> dict:
    if environment == "production":
        return {
            "status": "failed",
            "stage": "Terraform Apply",
        }
    return {"status": "succeeded"}
```

Why fake first?

```text
No Azure login
No RBAC
No network dependency
No real production risk
Easy repeatable tests
```

This lets us learn tool calling before cloud integration complexity.

---

# 6. Model Does Not Execute Python

This is the most important correction.

Wrong mental model:

```text
LLM directly runs get_aks_status()
```

Correct:

```text
LLM generates a structured tool request
      ↓
Host receives request
      ↓
Host validates request
      ↓
Python calls get_aks_status()
```

The model has no magical access to your Python runtime.

---

# 7. Tool Request Is Untrusted Input

Example model request:

```json
{
  "name": "get_aks_status",
  "arguments": {
    "cluster_name": "prod-aks"
  }
}
```

Do not immediately execute.

Treat it like user-controlled input.

Validate:

```text
Is tool name allowed?
Are required args present?
Are types correct?
Is target allowed?
Is operation read-only?
Is caller authorized?
```

---

# 8. Allowlist Pattern

```python
ALLOWED_TOOLS = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}

if tool_name not in ALLOWED_TOOLS:
    raise ValueError("Tool not allowed")
```

Never use unrestricted dynamic execution such as:

```python
eval(model_generated_text)
```

for tool dispatch.

---

# 9. Argument Validation

```python
ALLOWED_CLUSTERS = {"dev-aks", "prod-aks"}

if cluster_name not in ALLOWED_CLUSTERS:
    raise ValueError("Cluster not allowed")
```

Why?

Model can hallucinate:

```text
prod-west-aks
production
prod-secret-cluster
```

Correct tool + wrong argument = wrong/no evidence.

---

# 10. Canonical Argument Mapping

Your tools may expect different identifiers:

```text
AKS tool:
cluster_name = prod-aks

Pipeline tool:
environment = production

Terraform tool:
environment = production
```

Host can normalize user/model terms:

```text
prod → production
production-cluster → prod-aks
```

Do not force each tool to guess what the model meant.

---

# 11. Tool Result Is Not Just a String

Weak:

```text
"Degraded"
```

Better evidence envelope:

```python
{
    "source": "aks_status_tool",
    "target": "prod-aks",
    "status": "degraded",
    "observed_at": "...",
    "success": True,
}
```

Why?

- provenance
- freshness
- traceability
- conflict handling
- citation

---

# 12. Tool Failure Is Also Structured Information

Bad code:

```python
try:
    return call_azure()
except Exception:
    return "Healthy"
```

Danger:

```text
Tool failed
→ false healthy evidence
→ wrong RCA
```

Better:

```python
{
    "success": False,
    "error_type": "permission_denied",
    "message": "Unable to read AKS status"
}
```

Then model/host can say:

```text
AKS health could not be verified.
```

---

# 13. Read-Only First

Good first tools:

```text
get_pipeline_status
get_terraform_changes
get_aks_status
read_pipeline_log
get_node_status
get_cluster_events
```

Avoid first-stage agent tools like:

```text
terraform_apply
kubectl_delete
restart_production
rotate_secret
```

Why?

```text
Reasoning is probabilistic
Write blast radius is high
```

---

# 14. Real Tool Preview

Fake:

```python
def get_aks_status(cluster_name):
    return {"status": "degraded"}
```

Real conceptual implementation:

```python
def get_aks_status(cluster_name):
    raw = call_kubernetes_or_azure_api(cluster_name)
    return normalize(raw)
```

Tool contract can stay similar while implementation changes.

---

# 15. Authentication vs Authorization

For real tools:

```text
Authentication = Who are you?
Authorization  = What are you allowed to do?
```

Correct architecture:

```text
LLM
 ↓ tool request
Host Application
 ↓ authenticated identity
RBAC / policy
 ↓
Azure / AKS / Pipeline API
```

Never send cloud credentials inside prompt/context.

---

# 16. One Big Tool vs Focused Tools

Weak:

```text
get_everything_about_production()
```

Better:

```text
get_pipeline_status()
get_terraform_changes()
get_aks_status()
get_cluster_events()
```

Benefits:

- clearer contracts
- lower ambiguity
- easier tests
- least privilege
- better audit

---

# 17. Practical

Run:

```powershell
python examples/04_tool_call_basic.py
```

Observe:

```text
Question
→ model tool request
→ host dispatch
→ Python function
→ result
→ final model response
```

Do not skip the host dispatch code. That is the safety boundary.

---

# 18. Failure Drills

Test these intentionally:

## Unknown tool

```text
delete_prod_cluster
```

Expected: blocked by allowlist.

## Missing argument
Expected: validation failure.

## Invalid target
Expected: blocked before tool execution.

## Extra unexpected argument
Expected: schema/host validation rejects or normalizes according to policy.

## Tool timeout/error
Expected: explicit tool-error evidence, not fake success.

---

# 19. OpenAI vs Ollama Tool Calling

Provider/model APIs may expose tool calling differently and capabilities can vary by current model/runtime.

Stable course architecture:

```text
Provider produces tool request
        ↓
HOST validates same policy
        ↓
Same Python tool layer
```

Provider switch must not bypass:

```text
allowlists
argument validation
RBAC
approval
```

---

# 20. Tool Description Quality

Model uses tool names/descriptions/schemas to choose capabilities.

Ambiguous:

```text
get_status(name)
```

Clearer:

```text
get_aks_status(cluster_name)
get_pipeline_status(environment)
get_terraform_changes(environment)
```

Formula:

```text
Agent Quality
=
Model Reasoning
+ Tool Contract Quality
+ Evidence Quality
+ Host Controls
```

---

# 21. Normalization

Raw tool output can be noisy.

Example:

```text
kubectl get events -A
→ hundreds of lines
```

Normalize to:

```python
{
    "network_error": True,
    "event": "NetworkPluginNotReady",
    "affected_nodes": 2,
}
```

Normalization reduces noise but does not create truth.

---

# 22. Audit Logging

Record:

```text
incident_id
tool_name
validated_arguments
target
start/end time
success/error
source ID
```

Do not log secrets.

This enables later traceability:

```text
Question
→ Tool Request
→ Validation
→ Tool Execution
→ Evidence
→ RCA
```

---

# 23. Tool Calling vs Agent

Single tool flow:

```text
Question
→ Tool Request
→ Tool Result
→ Answer
```

Agent:

```text
Question
→ Tool 1
→ Observe
→ decide again
→ Tool 2
→ Observe
→ decide again
→ Final Answer
```

So tool calling is a building block of an agent, not automatically an agent itself.

---

# 24. Common Beginner Mistakes

1. LLM executes Python directly.
2. Tool schema = authorization.
3. Tool args trusted because JSON-valid.
4. Unknown tool names dynamically executed.
5. Secrets passed to model for API authentication.
6. Tool failure returned as healthy.
7. No provenance/timestamps.
8. One huge tool instead of focused capabilities.
9. Read/write tools mixed from day one.
10. Provider-specific tool behavior treated as security boundary.

---

# 25. Production Boundary

```text
Model
  ↓ tool proposal
Tool Gateway / Dispatcher
  ↓
Name + Args Validation
  ↓
Authorization / RBAC
  ↓
Known Tool Implementation
  ↓
External System
  ↓
Normalized Evidence
  ↓
Audit Store
```

For write tools:

```text
Recommendation
→ Policy
→ Human Approval
→ Controlled Existing Pipeline
```

---

# 26. Interview Q&A

### Q1. What is tool calling?
A model requests a predefined capability and structured arguments; host application validates and executes it.

### Q2. Does LLM execute the function?
No.

### Q3. Why treat tool arguments as untrusted?
They are model-generated and can be invalid, hallucinated or unauthorized.

### Q4. Tool schema vs authorization?
Schema defines interface shape; authorization determines whether an identity may perform the action.

### Q5. Why read-only first?
Lower blast radius while validating agent reasoning and evidence quality.

### Q6. What is a tool contract?
Name, purpose, inputs, output expectations and behavioral contract.

### Q7. Why normalize tool output?
To reduce noise and create consistent evidence structures.

### Q8. Should tool failure be treated as healthy status?
No. Failure is an explicit investigation state.

### Q9. Why focused tools?
Cleaner contracts, least privilege and easier testing.

### Q10. Tool calling vs agent?
Tool calling is one capability request; an agent may perform multiple decide→act→observe steps.

---

# 27. Revision Sheet

```text
Tool Call = model proposal
Host = validator/executor
Tool Contract = interface
Allowlist = allowed capabilities
Args = untrusted input
RBAC = authorization
Tool Result = evidence candidate
Normalization = clean evidence format
Read-only first = safer learning/production progression
```

---

# 28. Homework

1. Create `get_pipeline_status(environment)` fake tool.
2. Add allowlist dispatch.
3. Reject unknown tool name.
4. Reject invalid environment.
5. Return structured evidence with source and timestamp.
6. Simulate a permission-denied tool failure.
7. Explain how same contract could later call Azure DevOps/GitHub Actions API.
8. Draw host validation between LLM and tool.

---

# 29. Why Next Lesson?

Single safe tool request samajh gaya.

Now real investigation needs multiple steps:

```text
Check pipeline
→ observe
→ check Terraform
→ observe
→ check AKS
→ correlate
→ stop
```

➡️ **Lesson 9 — From Tool Calling to a Basic DevOps Agent**