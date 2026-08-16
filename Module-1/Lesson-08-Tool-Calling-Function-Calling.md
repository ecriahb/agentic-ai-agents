# Module 1 — Lesson 8: Tool Calling / Function Calling

> **Goal:** Samajhna ki model external function directly execute nahi karta; model tool request propose karta hai, host application validate karke function execute karti hai.

## English definition
**Tool calling lets a model request a typed external capability, while the host application remains responsible for validating and executing that request.**

## Core mental model

```text
User asks question
      ↓
LLM decides more data is needed
      ↓
Tool request
{name, arguments}
      ↓
HOST validates
      ↓
Python executes known function
      ↓
Tool result / evidence
      ↓
LLM receives result
      ↓
Final answer
```

## Golden rule

```text
LLM decides what it wants to call.
Host decides whether it is allowed to call it.
Python/tool implementation actually executes it.
```

## Simple tool

```python
def get_aks_status(cluster_name: str) -> dict:
    return {
        "cluster": cluster_name,
        "status": "degraded",
    }
```

Tool schema describes:

- tool name
- purpose
- argument names
- argument types

## Why schema is not authorization
A valid request like:

```json
{
  "tool": "get_aks_status",
  "cluster_name": "prod-secret-cluster"
}
```

can still be unauthorized.

Host must validate:

```text
Tool name allowlisted?
Arguments valid?
Target allowed?
Caller authorized?
Operation read-only or write?
```

## Tool request is untrusted input
Treat model-produced arguments like user input.

```python
ALLOWED_CLUSTERS = {"dev-aks", "prod-aks"}

if cluster_name not in ALLOWED_CLUSTERS:
    raise ValueError("Cluster not allowed")
```

## Tool result becomes evidence only with provenance
Better result:

```python
{
  "source": "aks_health_api",
  "cluster": "prod-aks",
  "timestamp": "...",
  "status": "degraded"
}
```

than:

```text
"AKS is bad"
```

## Read-only first
Beginner tools should start with:

- get status
- read logs
- read Terraform changes
- inspect pipeline

Avoid first-day agent examples that perform:

- terraform apply
- kubectl delete
- production restart
- secret rotation

## Practical
Run:

```powershell
python examples/04_tool_call_basic.py
```

Then modify:

1. allowed tool request
2. unknown tool name
3. invalid environment
4. missing argument
5. extra unexpected argument

Observe whether host rejects bad requests before execution.

## DevOps evidence tools
Module practicals gradually use:

```text
get_pipeline_status
get_terraform_changes
get_aks_status
read_pipeline_log
```

Each should have a clear, narrow contract.

## Common mistakes
- `eval()` on model-generated function name
- arbitrary shell execution
- passing raw model args directly to Azure/CLI
- treating tool description as security policy
- allowing model to invent tool names
- no timeout/error handling
- not preserving tool output as evidence

## Production boundary

```text
Model
 ↓ request
Tool Gateway / Dispatcher
 ↓ validation
Authorization / RBAC
 ↓
Known Implementation
 ↓
Evidence + Audit
```

## Interview questions
1. Function calling actually function execute karta hai kya?
2. Tool schema aur authorization me difference?
3. Tool args untrusted kyun hain?
4. Read-only-first agent design kyun safer hai?
5. Tool result me provenance kyun chahiye?

## Revision

```text
Tool call = proposal
Host = validator/executor
Schema = interface contract
Allowlist = allowed capability set
Tool output = evidence candidate
```

## Why next lesson?
Single tool call samajh gaya. Ab multiple decide→act→observe steps ko combine karke **Basic DevOps Agent** banayenge.