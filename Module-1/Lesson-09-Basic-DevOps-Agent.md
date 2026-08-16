# 🚩 Jai Bajrangbali!

# Lesson 09 — From Tool Calling to a Basic DevOps Agent

> **Goal → decide → tool → observe → decide again.**

## Why This Topic Now?

Single tool calling ek evidence point ke liye useful hai. Real incident investigation multi-step hoti hai: pipeline check karo, Terraform changes inspect karo, AKS health dekho, phir evidence ke basis par RCA banao.

```text
Single Tool Calling
        ↓
Agent Loop + State + Guardrails
        ↓
Production Agent Architecture
```

## Agent Formula

> **Goal + LLM + Tools + Loop + Rules = Basic AI Agent**

Production-grade agent ko additionally chahiye:

- Validation
- State
- Permissions
- Observability
- Human approval for risky actions

## Our Three Learning Tools

```text
get_pipeline_status(environment)
get_terraform_changes(environment)
get_aks_status(cluster_name)
```

## Argument Mistake We Learned From

Initial agent ne `prod-aks` ko pipeline aur Terraform tools ke `environment` argument ke roop me pass kar diya.

Isse ek important agent risk samne aaya:

> **Tool selection correct ho sakta hai, but arguments wrong ho sakte hain.**

## Constrain Arguments

```python
from typing import Literal

def get_pipeline_status(
    environment: Literal[
        "production",
        "staging",
        "development"
    ]
) -> str:
    ...
```

`Literal` model/tool schema ko valid choices clearly dikhata hai aur invented values ko reduce karta hai.

## Basic Agent Loop

```python
for step in range(1, 8):
    response = chat(
        model="qwen3:0.6b",
        messages=messages,
        tools=tools
    )

    messages.append(response.message)

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            result = available_functions[tool_name](
                **arguments
            )

            messages.append({
                "role": "tool",
                "tool_name": tool_name,
                "content": str(result)
            })
    else:
        print(response.message.content)
        break
```

## What Our DevOps Agent Discovered

| Tool | Observed Evidence |
|---|---|
| `get_pipeline_status(production)` | Failed during Terraform Apply |
| `get_terraform_changes(production)` | NSG rule allowing AKS subnet traffic was removed |
| `get_aks_status(prod-aks)` | Degraded — network connectivity failures detected |

## Evidence-Based RCA

Strong wording:

> **The evidence strongly suggests that removal of the NSG rule allowing AKS subnet traffic contributed to the observed AKS network connectivity degradation and deployment failure.**

Avoid unsupported claims like:

- Customer downtime definitely happened ❌
- Data loss occurred ❌
- Revenue impact occurred ❌

unless a tool/evidence source actually observed them.

## Why State Matters

Agent same tool repeatedly call kar sakta hai. Simple lab me executed tool+argument combinations track kiye ja sakte hain.

```python
executed_calls = set()

call_key = (
    tool_name,
    tuple(sorted(arguments.items()))
)

if call_key in executed_calls:
    result = "SKIPPED: already executed"
else:
    result = available_functions[tool_name](**arguments)
    executed_calls.add(call_key)
```

Production me blind duplicate blocking ki jagah freshness/TTL policy better ho sakti hai, kyunki fix ke baad re-check valid hota hai.

## Stronger Architecture

```text
Incident Goal
    ↓
Investigation Agent
    ↓
Tools collect exact evidence
    ↓
Application State preserves observations
    ↓
Structured RCA Generator
    ↓
Pydantic / Schema Validation
    ↓
Human Approval for risky actions
```

| Layer | Responsibility |
|---|---|
| Investigation agent | Tools choose karke observations collect karna |
| Application state | Exact evidence + execution history preserve karna |
| RCA generator | Evidence ko structured report me transform karna |
| Pydantic/schema | Required output shape validate karna |
| Human approval | Production-changing/destructive action gate karna |

## 🎯 Interview Corner

### Q. What is an agent loop?

**Answer:**
> An agent loop repeatedly lets the model decide whether to call tools, observe their results, and continue until it can complete the goal or reaches a safety or step limit.

### Q. Are we training our own LLM here?

**Answer:**
> No. We are using an existing model as the intelligence engine and building an agent around it using code, tools, state, validation and rules.

## 🧠 Remember This

> **A model is the brain. An agent is the system around the brain that can use tools, preserve state, follow rules and pursue a goal.**

## Module 1 Complete

Ab aap:

```text
Call Models
   ↓
Understand Responses
   ↓
Manage Context/Tokens
   ↓
Validate Structured Output
   ↓
Expose Tools
   ↓
Build a Multi-step Agent Loop
```

Next direction me retrieval, RAG, richer tool integrations, MCP, memory, guardrails aur enterprise DevOps agents aayenge.
