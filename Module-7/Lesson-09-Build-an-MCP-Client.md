# 🚩 Jai Bajrangbali!

# Lesson 09 — Build an MCP Client

> **Server capability expose karta hai; client discovery aur invocation ka protocol-side bridge hota hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- Python MCP `Client` mental model
- in-memory client for testing
- remote client concept
- tool discovery
- tool invocation
- resource reading
- typed/structured result handling
- host policy layer client ke upar kyu chahiye

---

# PART 1 — English Definition

An **MCP client** is the protocol component that connects to one MCP server, performs lifecycle/discovery operations and invokes exposed capabilities on behalf of the host application.

---

# PART 2 — Official-Style Minimal Client

Current Python SDK v2 exposes a high-level `Client` abstraction.

For learning/testing, client server object se in-memory connect kar sakta hai:

```python
import asyncio
from mcp import Client
from first_server import mcp


async def main() -> None:
    async with Client(mcp) as client:
        result = await client.call_tool(
            "get_pipeline_status",
            {"environment": "production"},
        )
        print(result.structured_content)


asyncio.run(main())
```

No subprocess/network required for this test mode.

---

# PART 3 — Why In-Memory Testing Is Valuable

It isolates protocol/application behavior:

```text
No port
No subprocess
No TLS
No remote auth
```

You can first test:

```text
schema
call behavior
result parsing
policy layer
```

Then move to stdio/remote transport.

This is similar to unit testing Module 6 components independently.

---

# PART 4 — Client Lifecycle

```python
async with Client(mcp) as client:
    ...
```

Mental model:

```text
enter context
 ↓
connect + initialize
 ↓
perform operations
 ↓
exit context
 ↓
close lifecycle cleanly
```

Avoid manual connection leaks.

---

# PART 5 — Discover Tools Before Calling

Conceptually:

```python
tools = await client.list_tools()
```

Then host extracts names/schemas.

Policy logic:

```python
allowed = {"get_pipeline_status", "get_aks_status"}

discovered_names = {...}
usable = discovered_names & allowed
```

Important:

```text
discovered ≠ usable
usable ≠ approved write
```

---

# PART 6 — Call Tool

```python
result = await client.call_tool(
    "get_pipeline_status",
    {"environment": "production"},
)
```

Client sends name + arguments to server.

Host should validate before this call:

```text
tool allowlist
arguments
user permission
workflow stage
approval if needed
```

---

# PART 7 — Structured Results

Current SDK client result can expose structured content for typed results.

Example:

```python
print(result.structured_content)
```

Expected learning result:

```python
{
    "environment": "production",
    "status": "failed",
    "stage": "terraform_apply",
    "source": "learning-pipeline-data",
}
```

Do not directly convert this to root cause.

It is one evidence item.

---

# PART 8 — Evidence Wrapping

Host should normalize:

```python
evidence = {
    "evidence_id": "E1",
    "server": "devops-learning",
    "tool": "get_pipeline_status",
    "arguments": {"environment": "production"},
    "result": result.structured_content,
}
```

This preserves source identity outside LLM memory.

---

# PART 9 — Reading Resources

Conceptually client can read exposed resource:

```text
runbook://aks/networking
```

Then host labels as reference:

```text
[R1]
URI: runbook://aks/networking
Type: REFERENCE
```

Never label it `E1` current evidence unless it truly represents incident-specific evidence.

---

# PART 10 — Remote Client

Current SDK supports URL-based client usage for remote server patterns.

Conceptual transition:

```python
Client(mcp)
```

in-memory test

→

```python
Client("http://localhost:8000/mcp")
```

remote endpoint pattern.

Same high-level client operations, different transport/deployment concerns.

---

# PART 11 — Client Is Not the Agent

Client does not decide:

```text
which tool should solve incident
whether evidence is enough
whether write is safe
what final RCA is
```

Those belong to host/orchestrator/policy/LLM combination.

Mental model:

```text
Agent/Workflow
   ↓
Policy
   ↓
MCP Client
   ↓
MCP Server
```

---

# PART 12 — Failure Handling

Handle separately:

```text
CONNECT_ERROR
DISCOVERY_ERROR
TOOL_NOT_FOUND
INVALID_ARGUMENT
SERVER_ERROR
TOOL_TIMEOUT
UNAUTHORIZED
RESOURCE_NOT_FOUND
```

Do not catch all and return:

```text
"No evidence found"
```

because server failure is not equivalent to absence of evidence.

---

# PART 13 — Multi-Server Host

Host may create:

```text
client_github
client_aks
client_pipeline
client_knowledge
```

Then source IDs:

```text
G1
A1
P1
R1
```

or normalized evidence IDs with server metadata.

Cross-server results must preserve origin.

---

# PART 14 — Caching Discovery

Discovery can be cached for performance, but think about capability drift.

Policy:

```text
cache with TTL
refresh on reconnect
validate required tools at startup
fail if critical contract changed
```

Do not persist stale schema forever.

---

# PART 15 — Client-Side Security

Host/client should restrict:

```text
allowed server URLs/processes
allowed tools
allowed resource schemes
max result size
timeouts
write operations
```

This is defense in depth with server-side security.

---

# PART 16 — DevOps Investigation Example

```text
client.list_tools()
      ↓
verify get_pipeline_status/get_terraform_changes/get_aks_status
      ↓
call three read-only tools
      ↓
wrap as E1/E2/E3
      ↓
read runbook resource as R1
      ↓
pass labeled context to Module 6 chain
```

This is Module 1 + 5 + 6 connected through MCP.

---

# PART 17 — Common Mistakes

- client = agent assume karna
- tool call before allowlist validation
- MCP exception ko no-evidence state banana
- structured content blindly trusted
- server identity drop karna
- resource/current evidence mix karna
- discovery cache forever
- remote endpoint allowlist missing

---

# PART 18 — Interview Q&A

### Q1. What does an MCP client own?
Connection lifecycle, discovery and protocol operations against one server.

### Q2. Can the MCP client decide tool authorization?
The host can implement policy around the client, but the client protocol abstraction itself should not be treated as the business authorization engine.

### Q3. Why wrap results into an evidence record?
To preserve provenance, arguments and auditability before model reasoning.

### Q4. Why use in-memory client tests?
They isolate MCP behavior from transport/network complexity.

---

# PART 19 — Revision

```text
Client connects
→ discovers
→ host validates
→ client invokes
→ result normalized
→ evidence preserved
```

Golden rule:

```text
MCP Client is transport/protocol capability access, not autonomous decision authority.
```

---

# PART 20 — Homework

Write pseudo-code for a client that:

```text
1. connects
2. discovers required read-only tools
3. fails if one is missing
4. calls them
5. preserves E1/E2/E3
6. reads R1 runbook
7. prints source map
```

---

# 🔁 Next Lesson Kyu?

Server/client working hai. Ab production question:

```text
Kaun connect kar sakta hai?
Kaun kaunsa tool call kar sakta hai?
Data leak kaise rokna hai?
Prompt injection se kaise bachna hai?
```

Next: **Security, Auth & Trust Boundaries**.
