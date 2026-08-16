# Module 7 Practicals — MCP for DevOps AI

These labs follow the lesson sequence and are intentionally progressive.

## Prerequisites

- Python 3.10+
- MCP Python SDK v2 current stable line
- Ollama only for V10 generation

Install:

```bash
pip install -r requirements.txt
```

For V10 also ensure Ollama is running and a model such as `qwen2.5:3b` is available.

---

## V1 → V10

```text
V1  01_first_mcp_server.py
    MCPServer + one typed tool

V2  02_devops_tool_server.py
    Read-only DevOps tool + allowlist validation

V3  03_resource_server.py
    Static + templated resources

V4  04_prompt_server.py
    Reusable MCP prompt primitive

V5  05_mcp_client.py
    In-memory client, discovery, tool call, resource read, prompt render

V6  06_devops_mcp_server.py
    Multi-tool DevOps investigation server

V7  07_streamable_http_server.py
    Same idea exposed through Streamable HTTP

V8  08_safe_mcp_dispatch.py
    Host allowlist + argument validation before tool call

V9  09_devops_investigation_client.py
    Collect E1/E2/E3 + R1/R2 into an evidence/source store

V10 10_mcp_devops_assistant.py
    MCP evidence → LangChain/Ollama grounded RCA → citation validation
```

---

## Recommended Learning Order

Do not jump directly to V10.

```text
Server definition
→ schema
→ resources
→ prompts
→ client lifecycle
→ discovery
→ multi-tool evidence
→ transport
→ host policy
→ evidence store
→ grounded AI
```

---

## Current SDK Notes

The examples target the current MCP Python SDK v2 style:

```python
from mcp.server import MCPServer
from mcp import Client
```

Core patterns:

```python
@mcp.tool()
@mcp.resource("scheme://...")
@mcp.prompt()
```

Server development:

```bash
mcp dev 06_devops_mcp_server.py
```

Direct stdio execution:

```bash
python 06_devops_mcp_server.py
```

Streamable HTTP example:

```bash
python 07_streamable_http_server.py
```

Client URL pattern:

```python
Client("http://127.0.0.1:8000/mcp")
```

---

## Security Rule for Labs

All incident tools are read-only deterministic learning tools.

No lab performs:

```text
terraform apply
kubectl delete
restart production
scale production
secret rotation
```

The point is to learn protocol, evidence and safety before remediation.

---

## Expected Evidence

Production scenario intentionally returns:

```text
E1 pipeline:
Deployment failed during Terraform Apply

E2 terraform:
NSG rule aks-subnet-allow was removed

E3 AKS:
Network connectivity degraded
```

Reference resources explain expected AKS/Terraform networking behavior.

This lets Module 7 reuse the trusted RCA case from earlier modules.

---

## Failure Tests

Try intentionally:

```text
unknown environment
unknown cluster
unknown tool
empty incident question
MCP server stopped
wrong HTTP URL
Ollama stopped
model outputs fake citation E99
```

Observe the difference between:

```text
NO_EVIDENCE
vs
TOOL_ERROR
vs
CONNECTION_ERROR
vs
VALIDATION_FAILED
```

---

## Final Learning Goal

```text
MCP gives standardized access.
Host gives policy.
Tools/resources give evidence/context.
LLM gives analysis.
Validator decides whether output is acceptable.
```
