# 🚩 Jai Bajrangbali!

# Lesson 04 — Private Networking, DNS & Egress

> **Private endpoints without correct DNS and egress design do not create a reliable private architecture.**

---

# 🎯 Lesson Goal

You will learn:

- ingress vs east-west vs egress traffic
- hub-spoke mental model
- WAF/API gateway boundary
- private endpoints and private DNS
- AKS/App Service integration concepts
- outbound control and allowlists
- MCP/tool network placement
- DNS and firewall failure modes
- network observability

---

# PART 1 — English Definitions

**Ingress** is traffic entering the workload.

**Egress** is traffic leaving the workload toward external or platform dependencies.

**Private endpoint** maps a supported service into a private network path.

---

# PART 2 — Production Network Mental Model

```text
Internet / Enterprise User
          ↓
WAF / App Gateway / API Gateway
          ↓
Private Workload Network
  ┌──────────────┬───────────────┐
  │ Agent API    │ Worker/Graph  │
  └──────────────┴───────────────┘
          ↓
Private Dependencies
  Search / Storage / Key Vault / State DB
          ↓
Controlled Egress
          ↓
Approved Model / MCP / SaaS APIs
```

---

# PART 3 — Three Traffic Classes

```text
North-South: user ↔ workload
East-West: service ↔ service
Outbound: workload → external dependency
```

Each needs separate controls and observability.

---

# PART 4 — Hub-Spoke

Common enterprise pattern:

```text
Hub VNet
- Azure Firewall
- DNS services
- VPN/ExpressRoute
- shared security

Spoke VNet
- AI workload
- AKS/App Service integration
- private endpoints
```

Peering/route design must be explicit.

---

# PART 5 — Private Endpoint ≠ Private DNS Automatically Understood

Example:

```text
Agent → mystorage.blob.core.windows.net
```

Expected in private architecture:

```text
DNS resolves → private endpoint IP
```

If DNS incorrectly resolves public IP:

```text
network policy may block
or traffic may leave intended boundary
```

So validate:

```text
name resolution
private DNS zone link
route
NSG/firewall
service access policy
```

---

# PART 6 — Controlled Egress

Agent runtimes often need outbound access to:

```text
model endpoint
GitHub API
MCP servers
package/telemetry endpoint
Azure management endpoints
```

Do not default to unrestricted internet egress.

Policy ideas:

```text
approved destinations
proxy/firewall route
FQDN/application rules where appropriate
NAT/static egress when partner allowlisting requires it
logging of denied/allowed flows
```

---

# PART 7 — MCP Network Placement

Local/internal MCP:

```text
Agent Runtime
 ↓ private network
Internal MCP Server
 ↓
Azure/GitHub/Monitoring APIs
```

Remote external MCP requires stronger review:

```text
server identity
TLS
OAuth/auth
allowlist
capability scope
data exfiltration risk
```

---

# PART 8 — Model Gateway

Instead of every service connecting to arbitrary model endpoints:

```text
Agent Services
      ↓
AI/Model Gateway
      ↓
Approved Model Backends
```

Gateway can centralize:

```text
authentication
rate limiting
model routing
telemetry
policy
cost attribution
```

But gateway becomes a dependency requiring HA and isolation.

---

# PART 9 — Network Failure Example

Terraform change removes route/NSG rule.

Symptoms:

```text
Agent API healthy
LLM calls fail
MCP tools time out
RAG search unreachable
```

Application must report dependency-specific failure, not hallucinate an RCA.

---

# PART 10 — Timeout Layering

```text
Client timeout
API timeout
Agent workflow deadline
Tool timeout
Model timeout
Network/firewall idle timeout
```

Set them intentionally.

If tool max timeout is 30s but outer API is 20s, retry logic may never complete.

---

# PART 11 — Private DNS Failure Checklist

```text
1. Resolve FQDN from workload pod/app.
2. Confirm private IP.
3. Confirm private DNS zone link.
4. Confirm custom DNS forwarder behavior.
5. Confirm UDR path.
6. Confirm NSG/firewall rules.
7. Confirm private endpoint approval/state.
8. Check service firewall/public access setting.
```

---

# PART 12 — Network Observability

Capture:

```text
connection failures
DNS resolution errors
firewall denies
SNAT/egress issues
latency by dependency
private endpoint health
```

Correlate with agent request/incident ID.

---

# PART 13 — Security Boundaries

Remember:

```text
Private network != authorization
TLS != permission
Known IP != trusted content
```

Use identity + network + policy together.

---

# PART 14 — Common Mistakes

- public endpoints left enabled “temporarily”
- private endpoint created but DNS not validated
- unrestricted outbound internet
- MCP servers reachable from every subnet
- no dependency-specific timeout
- firewall rules owned manually outside IaC
- shared DNS changes not tested in stage

---

# PART 15 — Interview Q&A

### Q1. Why is private DNS critical with private endpoints?
Because clients must resolve the service name to the private endpoint address for the intended private path to be used.

### Q2. Why control egress for agents?
Agents can access many external capabilities and may process sensitive data; unrestricted egress increases exfiltration and supply-chain risk.

### Q3. Is private networking enough for MCP security?
No. Authentication, authorization, capability allowlisting and content trust controls are still required.

---

# 🧠 Revision

```text
Secure Connectivity =
Identity + Private Path + DNS + Route + Firewall + TLS + Policy
```

---

# 📝 Homework

Draw a hub-spoke network for:

```text
Agent API
AKS workers
Azure AI Search/vector store
Key Vault
Storage
MCP server
Model gateway
```

Label ingress and egress paths.

---

# 🔁 Next Lesson Kyu?

Network paths are clear. Next we choose **where the runtime actually executes** and when AKS is worth its operational complexity.
