# 🚩 Jai Bajrangbali!

# Lesson 03 — Protocol Lifecycle, Capabilities & Discovery

> **MCP connection ka first goal tool call karna nahi; pehle dono sides ko protocol/lifecycle aur supported capabilities samajhni hoti hain.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- MCP connection lifecycle ka mental model
- initialization kya establish karta hai
- capability negotiation kyu important hai
- discovery ka role
- list vs call/read/get operations
- capability changes and error handling
- Module 3 API contracts aur Module 6 orchestration se relation

---

# PART 1 — Lifecycle Mental Model

```text
Create connection
      ↓
Initialize
      ↓
Exchange protocol/capability information
      ↓
Discover available primitives
      ↓
Use Tools / Resources / Prompts
      ↓
Handle notifications/errors
      ↓
Close cleanly
```

Do not assume:

```text
connected = all features available
```

---

# PART 2 — Why Initialization Exists

Different servers may expose different functionality.

Server A:

```text
Tools + Resources
```

Server B:

```text
Resources only
```

Server C:

```text
Tools + Prompts
```

A client should discover supported behavior rather than blindly calling methods.

This is similar to feature/capability negotiation in distributed systems.

---

# PART 3 — Capability Negotiation

Conceptually, both sides communicate what they support.

Mental model:

```text
Client:
"I can support these client-side capabilities"

Server:
"I expose these server-side capabilities"
```

Then workflow should adapt.

Example:

```text
If resources unsupported:
  do not build resource-dependent flow
```

---

# PART 4 — Discovery

Discovery means asking server what is available.

Examples:

```text
list_tools()
list_resources()
list_prompts()
```

Then client receives metadata/contracts.

This is one of MCP's major benefits compared with hard-coded tool definitions.

---

# PART 5 — Discovery != Permission

Suppose discovery returns:

```text
restart_deployment(environment)
```

This only means capability is exposed.

It does **not** mean:

```text
user may call it
model should call it
production write is approved
```

Host/server policy must still decide.

Module 1 rule remains:

```text
Tool Request → Validation → Authorization → Execution
```

---

# PART 6 — Tool Discovery Example

Server advertises:

```text
get_pipeline_status(environment: string)
get_aks_status(cluster_name: string)
restart_deployment(environment: string)
```

Host can classify:

```python
READ_ONLY = {"get_pipeline_status", "get_aks_status"}
WRITE = {"restart_deployment"}
```

Then policy:

```text
read-only → allowed in investigation
write → require explicit approval
```

Discovery data feeds policy; it does not replace policy.

---

# PART 7 — Resource Discovery Example

Resources may be static or templated.

Static:

```text
runbook://aks/networking
```

Templated:

```text
incident://{incident_id}/evidence
```

Client can discover what context exists before reading it.

But access control still matters.

---

# PART 8 — Prompt Discovery Example

Server may expose:

```text
incident_rca
terraform_change_review
aks_troubleshooting
```

Client can list prompts and choose one based on workflow.

Important:

```text
server prompt = reusable template
not an unchangeable system policy
```

Host should still apply its own system/security rules.

---

# PART 9 — Lifecycle Failure States

Potential failures:

```text
connection failed
initialization incompatible
server closes unexpectedly
timeout during list/call
capability missing
resource missing
invalid tool arguments
server returns structured error
```

Application should expose stage-specific errors.

Bad:

```text
MCP failed
```

Better:

```text
MCP_DISCOVERY_FAILED
server=devops-prod
operation=list_tools
reason=timeout
```

---

# PART 10 — Capability Drift

Production systems change.

Yesterday:

```text
get_aks_status(cluster_name)
```

Tomorrow:

```text
get_aks_status(subscription_id, cluster_name)
```

If client cached schema forever, calls can fail.

Think about:

```text
schema/version compatibility
connection refresh
capability cache TTL
startup validation
integration tests
```

---

# PART 11 — Relation to Module 3 APIs

REST clients often depend on external documentation/OpenAPI.

MCP supports runtime discovery of AI-facing capabilities.

Shared ideas:

```text
contracts
request/response
versioning
errors
transport
```

MCP-specific advantage:

```text
standardized discovery semantics for AI capabilities
```

---

# PART 12 — Relation to Module 6 Orchestration

Orchestrator should not hardcode assumptions like:

```text
server always has tool X
```

Better startup flow:

```text
connect
 ↓
discover
 ↓
validate required capabilities
 ↓
construct workflow
```

Example:

```python
required = {"get_pipeline_status", "get_terraform_changes"}
available = set(discovered_tools)
missing = required - available

if missing:
    raise RuntimeError(f"Missing required MCP tools: {missing}")
```

This makes failure deterministic before incident analysis begins.

---

# PART 13 — Notifications / Dynamic Changes Concept

Some protocol interactions can notify clients of server-side changes or events depending on capabilities/implementation.

Architectural lesson:

```text
capability set may not be static forever
```

Production clients should avoid brittle one-time assumptions.

---

# PART 14 — Observability

Log lifecycle stages:

```text
server_id
transport
connect_duration
initialize_duration
protocol version
capabilities
list_tools count
list_resources count
errors
reconnect count
```

Do not log credentials or sensitive payloads.

---

# PART 15 — Common Mistakes

- call before initialization/discovery mental model
- discovered tool ko auto-approved samajhna
- capability schemas cache forever
- missing capability ko model se compensate karwana
- generic connection error
- server identity not logged
- version incompatibility ignore karna

---

# PART 16 — Interview Q&A

### Q1. Why does capability negotiation matter?
Because clients and servers may support different protocol features; negotiation lets the workflow know what can safely be used.

### Q2. What is discovery in MCP?
Runtime enumeration of tools, resources, prompts or related exposed capabilities and their metadata/contracts.

### Q3. Does discovering a tool authorize its use?
No. Discovery exposes availability; authorization and approval are separate policy decisions.

### Q4. How would you handle a required tool missing at runtime?
Fail fast or degrade explicitly before analysis rather than letting the model invent an alternative capability.

---

# PART 17 — Revision

```text
Connect
→ Initialize
→ Discover
→ Validate capability set
→ Invoke/read/get
→ Observe errors/changes
→ Close
```

Golden rule:

```text
Available != Allowed
```

---

# PART 18 — Homework

Design startup validation for an incident assistant requiring:

```text
get_pipeline_status
get_terraform_changes
get_aks_status
runbook://aks/networking
```

Define behavior when each one is unavailable.

---

# 🔁 Next Lesson Kyu?

Ab server capabilities discover kar sakte hain. Sabse critical primitive next hai:

```text
Tools
```

Because tools external systems ko actually execute/read karte hain and therefore biggest safety boundary create karte hain.
