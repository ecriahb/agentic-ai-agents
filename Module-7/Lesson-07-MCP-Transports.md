# 🚩 Jai Bajrangbali!

# Lesson 07 — MCP Transports: stdio, Streamable HTTP & SSE

> **MCP protocol capability contract alag cheez hai; transport sirf ye decide karta hai ki client aur server messages kaise exchange karenge.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- transport kya hota hai
- stdio transport kab use hota hai
- Streamable HTTP kab useful hai
- SSE ka role aur compatibility perspective
- local vs remote trust boundary
- network security concerns
- DevOps deployment architecture me transport choice

---

# PART 1 — Protocol vs Transport

Mental model:

```text
MCP semantics
Tools / Resources / Prompts
        ↓
Protocol messages
        ↓
Transport
        ↓
Process / Network
```

Do not confuse:

```text
MCP = protocol
HTTP = transport mechanism
```

---

# PART 2 — stdio Transport

`stdio` means host/client launches or connects to a local subprocess and communicates through standard input/output streams.

Mental model:

```text
Host Process
   ↓ starts
MCP Server Process
   ↕ stdin/stdout
MCP Client
```

Use cases:

```text
local developer tools
CLI wrappers
local filesystem tools
single-user desktop integrations
learning labs
```

---

# PART 3 — Why stdio Is Useful

Advantages:

```text
no network port
simple local lifecycle
server can start/stop with host
reduced remote attack surface
```

But not automatically safe.

Local server may still access:

```text
filesystem
credentials
kubectl context
cloud CLI sessions
SSH keys
```

So subprocess trust matters.

---

# PART 4 — stdio Security Risks

If user installs malicious MCP server package:

```text
Host launches package
 ↓
Package inherits local execution context
 ↓
Can potentially access local files/env/network based on OS permissions
```

Therefore:

```text
pin dependencies
review source
restrict filesystem
minimize environment variables
use sandbox/container where appropriate
avoid passing secrets unnecessarily
```

---

# PART 5 — Streamable HTTP

Remote/network-oriented transport allows client to communicate with MCP server through HTTP-based endpoint.

Mental model:

```text
AI Host
  ↓ HTTPS
Remote MCP Server
  ↓
Backend systems
```

Useful for:

```text
shared enterprise services
central DevOps integrations
multi-user hosts
managed deployment
remote authentication
```

---

# PART 6 — Remote Server Concerns

Once network involved, think Module 3 production API concerns:

```text
TLS
authentication
authorization
rate limits
timeouts
retries
load balancing
health checks
observability
network policy
```

MCP does not remove distributed-system reality.

---

# PART 7 — SSE Perspective

Current SDK supports SSE alongside stdio and Streamable HTTP for compatibility/use cases.

Architectural lesson:

```text
transport choice may evolve with protocol/SDK versions
```

So course focus should be:

```text
connection lifecycle
security model
local vs remote tradeoff
```

not memorizing one transport as eternal default.

---

# PART 8 — Choosing Transport

Simple decision table:

```text
Local single-user CLI integration
→ stdio

Central organization service
→ Streamable HTTP

Existing compatibility requirement
→ evaluate SSE/support matrix
```

Do not select transport only because example code is shorter.

---

# PART 9 — DevOps Example: Local Lab

Learning lab:

```text
VS Code / Python Host
      ↓ stdio
Local DevOps MCP Server
      ↓
Fake/local pipeline evidence
```

Benefits:

```text
no Azure credentials needed
safe deterministic practice
easy debugging
```

---

# PART 10 — DevOps Example: Enterprise

Production architecture:

```text
Internal AI Assistant
      ↓ HTTPS / Streamable HTTP
Central DevOps MCP Service
      ↓ Managed Identity / Workload Identity
Azure DevOps / AKS / GitHub / Monitor
```

Server can centralize:

```text
RBAC
audit
rate limits
backend credentials
approved tool set
```

---

# PART 11 — Transport Does Not Define Authorization

`stdio` does not mean trusted.
`HTTPS` does not mean authorized.

Separate concepts:

```text
Transport security
Authentication
Authorization
Tool approval
Business validation
```

All are different layers.

---

# PART 12 — Timeouts and Retries

Remote calls fail.

Read-only tool:

```text
timeout → retry may be safe with backoff
```

Write tool:

```text
timeout after backend success → retry may duplicate action
```

Module 6 rule continues:

```text
retry based on side-effect semantics
```

---

# PART 13 — Server Lifecycle

stdio:

```text
host starts server
host tracks process
host closes → server exits
```

remote:

```text
server independently deployed
health monitored separately
multiple clients connect
```

This changes operational ownership.

---

# PART 14 — Observability by Transport

stdio logs:

```text
process start
exit code
stderr
startup duration
```

remote logs:

```text
HTTP status
request latency
connection/session IDs
TLS/auth failure
rate limiting
server saturation
```

Keep protocol operation name too:

```text
call_tool / read_resource / list_tools
```

---

# PART 15 — Common Mistakes

- stdio package blindly trusted
- remote server exposed publicly without auth
- transport security confused with RBAC
- infinite retries
- write calls retried blindly
- secrets passed through command line
- server stdout polluted with debug output in stdio designs
- no lifecycle monitoring

---

# PART 16 — Interview Q&A

### Q1. What is the role of an MCP transport?
It carries MCP protocol messages between client and server; it does not define tool semantics or authorization policy.

### Q2. When would you choose stdio?
For local subprocess-based integrations where the host can manage server lifecycle and no network service is needed.

### Q3. When would Streamable HTTP be preferred?
For shared or remote MCP services requiring network deployment, centralized auth, scaling and multi-client access.

### Q4. Is stdio inherently secure?
No. The local server still executes with OS/process permissions and may access sensitive resources.

---

# PART 17 — Revision

```text
Protocol = what MCP messages mean
Transport = how messages move
stdio = local subprocess channel
Streamable HTTP = network/remote channel
SSE = supported compatibility transport
```

Golden rule:

```text
Transport choice changes operational/security concerns, not trust fundamentals.
```

---

# PART 18 — Homework

Choose transport for:

```text
1. Local laptop runbook server
2. Enterprise AKS status service
3. Shared GitHub read-only server
4. Production remediation server
```

Explain lifecycle, auth and audit requirements for each.

---

# 🔁 Next Lesson Kyu?

Ab protocol + primitives + transport samajh gaye. Next hum **actual Python MCP server** banayenge using current SDK style.
