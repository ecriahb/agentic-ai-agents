# 🚩 Jai Bajrangbali!

# Lesson 05 — MCP Capability Integration

> **MCP standardizes capability discovery and invocation; the host still owns trust, authorization, argument validation and evidence handling.**

---

# 🎯 Lesson Goal

You will integrate/design:

- MCP client boundary
- capability discovery
- required capability validation
- trusted server registry
- tool/resource mapping
- structured evidence conversion
- remote auth/transport considerations
- capability versioning
- MCP failure behavior

---

# PART 1 — Why MCP in Final Project

Without MCP:

```text
Agent code → custom GitHub client
Agent code → custom AKS client
Agent code → custom Terraform service
```

With MCP:

```text
Agent Host
 ↓
MCP Client Layer
 ↓
Approved MCP Servers
 ↓
DevOps Systems
```

The host becomes less coupled to each integration implementation.

---

# PART 2 — Required Capability Set

Final investigation requires:

```python
REQUIRED_TOOLS = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}
```

Startup/investigation validation:

```text
discover tools
 ↓
compare required vs available
 ↓
missing? → CAPABILITY_MISSING
```

Never ask the model to improvise a missing integration.

---

# PART 3 — Trusted Server Registry

```python
TRUSTED_SERVERS = {
    "devops-readonly": {
        "risk": "READ_ONLY",
        "allowed_tools": [...],
        "environment": "production",
    }
}
```

Discovery from an unknown server is not enough to make its tools eligible.

---

# PART 4 — Tool Mapping

MCP result:

```text
structured_content
```

Host converts to evidence envelope:

```text
MCP tool result
 ↓
validate status/schema
 ↓
normalize
 ↓
assign E* ID
 ↓
store provenance
```

MCP output itself is not final RCA.

---

# PART 5 — Resources

Reference resources may expose:

```text
runbook://aks/networking
runbook://terraform/networking
```

Host maps:

```text
resource → R1/R2 reference envelope
```

Again:

```text
Resource content = data
not system instruction
```

---

# PART 6 — Prompts

MCP prompt primitives can expose reusable workflows, but the final production host should still control:

```text
instruction hierarchy
security rules
output contract
policy
```

Do not blindly trust remote prompt text to become system-level authority.

---

# PART 7 — Server Authentication

For remote MCP:

```text
TLS
server identity
authentication
authorization
approved endpoint
credential lifecycle
```

For local stdio:

```text
process executable path
package provenance
file/system permissions
```

Local does not mean harmless.

---

# PART 8 — Capability Scope

Pipeline specialist receives only pipeline capability.

Terraform specialist receives only Terraform read capability.

AKS specialist receives only AKS read capability.

This reduces blast radius and context confusion.

---

# PART 9 — MCP Failure States

```text
SERVER_UNREACHABLE
AUTH_FAILED
CAPABILITY_MISSING
TOOL_ERROR
INVALID_RESPONSE
RESOURCE_NOT_FOUND
```

Each becomes workflow state.

Do not fall back to invented evidence.

---

# PART 10 — Version Drift

MCP server can change schema/tool description.

Production controls:

```text
contract tests
server version inventory
capability snapshot
staged rollout
backward compatibility
```

---

# PART 11 — MCP Security Review

For each server:

```text
owner
endpoint
transport
identity
data accessible
tools exposed
write capability
risk class
logging
rate limits
approval requirement
```

---

# PART 12 — Final Project Flow

```text
Supervisor
 ↓
select specialist
 ↓
host checks allowed MCP server/tool
 ↓
validate arguments
 ↓
call MCP
 ↓
normalize result to evidence
 ↓
specialist returns structured finding
```

---

# PART 13 — Common Mistakes

- dynamic connection to arbitrary MCP URL
- model sees all tools from all servers
- discovery treated as authorization
- remote prompt becomes trusted system prompt
- tool error text becomes factual evidence
- server schema changes without tests
- no provenance in normalized evidence

---

# PART 14 — Interview Q&A

### Q1. What does MCP solve in the capstone?
It standardizes capability/resource integration while keeping the host responsible for policy, trust and workflow behavior.

### Q2. Why have a trusted server registry?
To prevent arbitrary discovered servers/capabilities from becoming usable simply because they speak MCP.

### Q3. Should specialists receive every discovered tool?
No. Give each specialist the minimum capability set required for its role.

---

# 🧠 Revision

```text
MCP = Standard Connectivity
Host = Trust + Policy + State
```

---

# 📝 Homework

Design an MCP trust record for `azure-observability-mcp` including allowed tools and data classification.

---

# 🔁 Next Lesson Kyu?

Capabilities are standardized. Next we create the **stateful multi-agent investigation graph** that coordinates them safely.
