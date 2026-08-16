# 🚩 Jai Bajrangbali!

# Lesson 02 — Host, Client & Server Architecture

> **MCP samajhne ka sabse important architecture rule: Host, Client aur Server ki responsibilities alag rakho.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- MCP Host kya hota hai
- MCP Client kya karta hai
- MCP Server kya expose karta hai
- ek host multiple servers se kaise connect kar sakta hai
- security boundary kahan hoti hai
- Module 3 client-server aur Module 6 orchestration concepts yahan kaise reuse hote hain

---

# PART 1 — English Definitions

**Host:** The AI application that owns the user experience, model interaction, policy and overall orchestration.

**Client:** The component inside or controlled by the host that maintains an MCP connection to a server and sends protocol requests.

**Server:** A process/service that exposes MCP capabilities such as tools, resources and prompts.

---

# PART 2 — Basic Architecture

```text
User
 ↓
AI Host
 ├─ LLM
 ├─ Workflow / Agent Logic
 ├─ Policy / Approval
 ├─ Evidence Store
 └─ MCP Clients
       ├────────→ MCP Server A → GitHub
       ├────────→ MCP Server B → AKS
       └────────→ MCP Server C → Knowledge Base
```

A single host can manage multiple MCP connections.

---

# PART 3 — Host Responsibilities

Host should generally own:

```text
user identity/context
model selection
conversation state
workflow orchestration
which server is trusted/allowed
approval decisions
what results are shown to model/user
cross-server evidence aggregation
business-level validation
```

Do not push all decision-making into server or model.

DevOps example:

```text
User asks restart prod deployment
```

Host should know:

```text
Is user allowed?
Is action read or write?
Is human approval required?
Which server is allowed for prod?
```

The model should not decide authorization from prose.

---

# PART 4 — Client Responsibilities

Client manages protocol interaction:

```text
connect
initialize
list capabilities
call tool
read resource
get prompt
receive typed results/errors
close connection
```

Think Module 3 API client, but MCP-aware.

Conceptually:

```python
async with Client(server) as client:
    tools = await client.list_tools()
    result = await client.call_tool("get_aks_status", {"cluster_name": "prod-aks"})
```

The client does not magically decide whether the tool should be called.

---

# PART 5 — Server Responsibilities

Server owns exposed capability implementation.

Example DevOps server:

```text
Tools
- get_pipeline_status
- get_terraform_changes
- get_aks_status

Resources
- runbook://aks/networking

Prompts
- incident_rca
```

Server should also own server-side:

```text
input validation
backend authentication
least-privilege credentials
backend error normalization
resource access checks
rate limiting where relevant
safe logging
```

---

# PART 6 — One Client per Server Mental Model

Conceptual connection model:

```text
Host
 ├─ Client A ↔ Server A
 ├─ Client B ↔ Server B
 └─ Client C ↔ Server C
```

This creates isolation advantages:

```text
separate lifecycles
separate trust decisions
separate credentials
separate errors
separate capability sets
```

Do not treat all connected servers as one trusted super-toolbox.

---

# PART 7 — Relation to Module 3

Module 3:

```text
Python Client → REST API → Response
```

Module 7:

```text
MCP Client → MCP Server → Tools/Resources/Prompts
```

Shared concepts:

```text
request/response
schemas
errors
authentication
transport
timeouts
```

Difference:

```text
MCP has AI-oriented discovery and primitives.
```

---

# PART 8 — Relation to Module 6

Module 6 workflow:

```text
Input
 ↓
Retriever / Tool Layer
 ↓
LLM
 ↓
Parser
 ↓
Validation
```

With MCP:

```text
Tool Layer
 ↓
MCP Client
 ↓
MCP Server
```

So MCP can replace custom connector wiring while orchestration remains in the host.

---

# PART 9 — Trust Boundaries

Important trust diagram:

```text
User Input          = untrusted
Retrieved Content   = untrusted data by default
Model Output        = untrusted proposal
MCP Tool Request    = untrusted intent
Server Result       = evidence candidate
Authorization State = trusted policy source
```

Even if server is trusted, backend data may be stale or incomplete.

---

# PART 10 — Cross-Server DevOps Example

Incident investigation:

```text
GitHub MCP Server
  → recent deployment commit

Azure DevOps MCP Server
  → pipeline failure

AKS MCP Server
  → cluster status

Knowledge MCP Server
  → networking runbook
```

Host aggregates:

```text
[E1] deployment commit
[E2] pipeline status
[E3] AKS status
[R1] runbook guidance
```

Then LLM analyzes with labels.

Critical:

```text
cross-server merge must preserve source identity
```

Never flatten everything into anonymous text.

---

# PART 11 — Failure Isolation

Suppose AKS MCP server times out.

Bad design:

```text
whole assistant fails with generic error
```

Better:

```text
GitHub evidence = available
Pipeline evidence = available
AKS evidence = unavailable: timeout
Runbook = available
```

Final analysis should state evidence gap.

This connects directly to Module 6 stage-aware observability.

---

# PART 12 — Security Example

MCP Server A has read-only prod access.
MCP Server B has deployment write permissions.

Do not expose both identically to every workflow.

Host policy can classify:

```text
READ_ONLY
WRITE_LOW_RISK
WRITE_HIGH_RISK
```

High-risk actions require approval.

---

# PART 13 — Common Mistakes

- host/server responsibilities mix karna
- model ko authorization owner banana
- all MCP servers equally trusted assume karna
- source identity lose karna
- one server failure ko complete workflow failure banana
- server credentials client prompt me expose karna
- write-capable servers default-enable karna

---

# PART 14 — Interview Q&A

### Q1. What is an MCP host?
The AI application that manages model interaction, user experience, orchestration, policy and one or more MCP clients.

### Q2. What does the MCP client do?
It establishes and manages a protocol connection to an MCP server and invokes discovered capabilities.

### Q3. What does an MCP server do?
It exposes tools, resources and prompts backed by local or remote systems.

### Q4. Where should authorization live?
In trusted application/server policy and identity systems, not in model reasoning.

### Q5. Why preserve server/source identity?
For auditability, trust classification, error isolation and evidence-grounded claims.

---

# PART 15 — Revision

```text
Host   = owns AI application + policy
Client = speaks MCP to one server
Server = exposes capabilities

Host != Server
Client != Agent
Server != LLM
```

---

# PART 16 — Homework

Design architecture for:

```text
GitHub
AKS
Terraform
ServiceNow
```

For each, define:

```text
MCP server
credentials owner
read/write classification
host approval policy
failure behavior
```

---

# 🔁 Next Lesson Kyu?

Architecture clear hai. Ab connection start hone par protocol kaise decide karta hai:

```text
server kya support karta hai?
client kya support karta hai?
capabilities kaise discover hoti hain?
```

Next lesson: **Lifecycle, Capabilities & Discovery**.
