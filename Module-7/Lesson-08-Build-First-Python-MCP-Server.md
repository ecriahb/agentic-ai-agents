# 🚩 Jai Bajrangbali!

# Lesson 08 — Build Your First Python MCP Server

> **Ab theory ko code me convert karte hain: ek small MCP server jo typed Tool + Resource expose kare.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- current Python MCP SDK v2 setup
- `MCPServer` basic structure
- `@mcp.tool()` decorator
- `@mcp.resource()` decorator
- typed arguments se schema generation
- server ko Inspector/dev mode me run karna
- Module 1 tool contract concepts ko MCP implementation me map karna

---

# PART 1 — Prerequisites

Python MCP SDK v2 ke current stable line ke liye Python 3.10+ use karo.

Install:

```bash
pip install "mcp[cli]"
```

or with uv:

```bash
uv add "mcp[cli]"
```

The CLI extra gives development commands such as MCP dev tooling.

---

# PART 2 — First Server

Create:

```text
01_first_mcp_server.py
```

Code:

```python
from mcp.server import MCPServer

mcp = MCPServer("DevOps Learning Server")


@mcp.tool()
def get_pipeline_status(environment: str) -> dict:
    """Return read-only pipeline status for a learning environment."""
    allowed = {"dev", "stage", "production"}
    env = environment.strip().lower()

    if env not in allowed:
        raise ValueError(f"Unsupported environment: {environment}")

    data = {
        "dev": {"status": "success", "stage": "deploy"},
        "stage": {"status": "success", "stage": "validation"},
        "production": {"status": "failed", "stage": "terraform_apply"},
    }

    return {
        "environment": env,
        **data[env],
        "source": "learning-pipeline-data",
    }


@mcp.resource("runbook://aks/networking")
def aks_networking_runbook() -> str:
    """Return a small AKS networking troubleshooting reference."""
    return (
        "Check AKS subnet NSG rules, UDRs, private DNS dependencies, "
        "and required connectivity before redeployment."
    )
```

This is already a valid server definition with one tool and one resource.

---

# PART 3 — Line-by-Line Explanation

```python
from mcp.server import MCPServer
```

Imports server abstraction.

```python
mcp = MCPServer("DevOps Learning Server")
```

Creates server object and gives it identity/name.

```python
@mcp.tool()
```

Registers function as discoverable MCP tool.

```python
def get_pipeline_status(environment: str) -> dict:
```

Type hint contributes to input/output contract.

Important:

```text
Typed schema = structural contract
allowlist = business validation
```

Both are needed.

---

# PART 4 — Why Docstring Matters

Tool description helps client/model understand what capability does.

Bad:

```python
"""Status."""
```

Better:

```python
"""Return read-only pipeline status for a learning environment."""
```

It communicates:

```text
read-only
scope
purpose
```

Still not an enforcement mechanism.

---

# PART 5 — Why We Validate Environment

Schema says:

```text
environment = string
```

But our business contract says:

```text
dev | stage | production only
```

Hence:

```python
if env not in allowed:
    raise ValueError(...)
```

This is exactly Module 1 argument validation.

---

# PART 6 — Why Return a Dict

We could return:

```text
"Failed"
```

But structured output is better:

```json
{
  "environment": "production",
  "status": "failed",
  "stage": "terraform_apply",
  "source": "learning-pipeline-data"
}
```

Benefits:

```text
machine-readable
traceable
easier validation
```

But remember:

```text
structured != verified truth
```

In learning server data is deterministic fake/local evidence.

---

# PART 7 — Resource Explanation

```python
@mcp.resource("runbook://aks/networking")
```

Registers a readable resource.

This is reference knowledge, not current incident evidence.

```text
Resource = guidance
Tool = current status lookup
```

Do not merge semantics.

---

# PART 8 — Running with MCP Development Tooling

Current SDK CLI supports development inspection flow such as:

```bash
mcp dev 01_first_mcp_server.py
```

or if using uv:

```bash
uv run mcp dev 01_first_mcp_server.py
```

The development/Inspector flow lets you inspect exposed capabilities and call them manually.

---

# PART 9 — Test Cases

### Test 1

```text
get_pipeline_status(environment="production")
```

Expected structured meaning:

```text
status=failed
stage=terraform_apply
```

### Test 2

```text
get_pipeline_status(environment="qa")
```

Expected:

```text
explicit validation error
```

### Test 3

Read:

```text
runbook://aks/networking
```

Expected reference text.

---

# PART 10 — Add Second Tool

```python
@mcp.tool()
def get_aks_status(cluster_name: str) -> dict:
    """Return read-only learning AKS status for an allowlisted cluster."""
    clusters = {
        "dev-aks": "healthy",
        "prod-aks": "degraded",
    }

    if cluster_name not in clusters:
        raise ValueError("Unknown cluster")

    return {
        "cluster_name": cluster_name,
        "status": clusters[cluster_name],
        "source": "learning-aks-data",
    }
```

Now server exposes two tools + one resource.

---

# PART 11 — Tool Discovery Mental Model

Client will not need to know Python source code.

It discovers something like:

```text
Tool: get_pipeline_status
Input: environment:string

Tool: get_aks_status
Input: cluster_name:string
```

This is the standardization benefit.

---

# PART 12 — Module 1 vs MCP Version

Module 1:

```python
tool_registry = {
  "get_aks_status": get_aks_status
}
```

Module 7:

```text
MCP server registers and exposes typed capability
client discovers it through protocol
```

But validation remains same.

---

# PART 13 — Production Changes

Learning fake data should later become backend adapters:

```text
Azure DevOps REST API
Kubernetes Python client / Azure API
Terraform state/change source
```

Server-side code should include:

```text
credentials
RBAC
timeout
retry policy
normalization
audit
```

Do not put cloud tokens into model/tool arguments.

---

# PART 14 — Server Testing

Before connecting an LLM, test server independently.

```text
Does list show correct tools?
Does valid input succeed?
Does invalid input fail?
Does resource return correct source?
Are write side effects absent?
```

This follows Module 1 principle:

```text
Test tool before agent.
```

---

# PART 15 — Common Errors

```text
ModuleNotFoundError: mcp
→ install current SDK

Python version too old
→ use supported Python 3.10+

Tool visible but invalid result
→ test function directly

Unknown environment accepted
→ missing business validation
```

---

# PART 16 — Interview Q&A

### Q1. How does Python MCP SDK derive a tool schema?
Typed function signatures and metadata/docstrings are used by the SDK to expose a protocol-level tool contract.

### Q2. Does that replace business validation?
No. Type correctness and domain validity are separate.

### Q3. Why build read-only tool first?
It reduces blast radius while testing protocol, auth, evidence and orchestration behavior.

### Q4. Why test server without LLM?
To separate integration/tool bugs from model/tool-selection behavior.

---

# PART 17 — Revision

```text
MCPServer
  ↓
@mcp.tool
@mcp.resource
  ↓
Typed contracts
  ↓
Discovery
```

Golden rule:

```text
First prove server capabilities independently.
Then connect AI.
```

---

# PART 18 — Homework

Add:

```text
get_terraform_changes(environment)
resource: runbook://terraform/networking
```

Requirements:

```text
allowlisted input
structured result
source field
read-only behavior
explicit invalid-input error
```

---

# 🔁 Next Lesson Kyu?

Server ready hai. Ab doosri side build karenge:

```text
MCP Client
```

Client capability discover karega, tool call karega aur resource read karega.
