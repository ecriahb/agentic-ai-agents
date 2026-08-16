# 🚩 Jai Bajrangbali!

# Lesson 01 — MCP Fundamentals: Why MCP?

> **MCP ka purpose intelligence banana nahi, AI application aur external capabilities ke beech standardized contract banana hai.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- MCP kya hai
- MCP kis problem ko solve karta hai
- normal API/tool integration se difference kya hai
- Module 1–6 ke concepts MCP me kaise map hote hain
- MCP kya **nahi** karta
- DevOps AI architecture me MCP ki position kya hai

---

# PART 1 — English Definition

**Model Context Protocol (MCP)** is a standard protocol for connecting AI applications to external tools, data/resources and reusable interaction capabilities through discoverable, typed interfaces.

Simple Hinglish:

```text
AI app ko har tool ke liye custom integration likhne ke bajay
MCP ek common protocol deta hai.
```

---

# PART 2 — Problem Before MCP

Module 1 me humne custom tool functions banaye:

```python
def get_aks_status(cluster_name):
    ...

def get_pipeline_status(environment):
    ...
```

Then host application ko manually maintain karna pada:

```text
tool name
argument schema
execution function
result shape
error handling
security
```

Agar 3 tools hain, manageable.

Agar enterprise me:

```text
GitHub
Azure DevOps
AKS
Terraform
ServiceNow
Datadog
Azure Monitor
CMDB
Key Vault
Internal APIs
```

har AI app custom connector likhe to duplication hota hai.

---

# PART 3 — MCP Mental Model

Without MCP:

```text
AI App A → custom GitHub integration
AI App A → custom AKS integration
AI App A → custom Terraform integration

AI App B → another GitHub integration
AI App B → another AKS integration
```

With MCP:

```text
             MCP Server — DevOps
            /       |        \
        GitHub     AKS     Terraform
            \       |        /
              MCP Protocol
                   ↓
         Any compatible MCP Client
```

Standardization reduces repeated integration plumbing.

---

# PART 4 — Relation to Module 1

Module 1 taught:

```text
LLM requests tool
      ↓
Host validates
      ↓
Tool executes
      ↓
Evidence returned
```

MCP does **not** replace that trust model.

Instead:

```text
MCP Server advertises tool
      ↓
MCP Client discovers it
      ↓
Host/model may request use
      ↓
Policy/validation still required
      ↓
MCP call executes
```

Important:

```text
MCP tool schema != permission
MCP discovery != approval
MCP result != automatically trusted truth
```

---

# PART 5 — Relation to Module 2

Module 2 taught prompt/context boundaries.

MCP adds standardized primitives that can feed those boundaries:

```text
MCP Resource → context/evidence
MCP Prompt   → reusable interaction template
MCP Tool     → external capability
```

But prompt injection risk still exists.

Retrieved resource content must be treated as data unless explicitly trusted.

---

# PART 6 — Relation to Module 3

Module 3 taught:

```text
Client
 ↓
Request
 ↓
Server/API
 ↓
Response
```

MCP uses a similar client-server mental model, but is purpose-built for AI capability exchange.

API endpoint mindset:

```text
GET /aks/status
POST /incident/analyze
```

MCP mindset:

```text
list tools
call tool
list resources
read resource
list prompts
get prompt
```

The protocol gives standardized AI-facing semantics.

---

# PART 7 — Relation to Module 4 & 5

Module 4/5 built retrieval and RAG.

MCP can expose knowledge as resources or expose a retrieval tool.

Example:

```text
resource:
runbook://aks/networking

or tool:
search_runbooks(query="AKS NSG issue")
```

Then RAG pipeline can consume returned content.

MCP is not a vector database and is not RAG itself.

---

# PART 8 — Relation to Module 6

Module 6 taught orchestration.

LangChain/custom workflow can treat MCP as an integration boundary:

```text
Workflow
 ↓
MCP Client
 ↓
MCP Server
 ↓
External System
```

So:

```text
LangChain = orchestration framework
MCP = capability protocol
LLM = reasoning/generation model
```

Do not mix these roles.

---

# PART 9 — Three Core MCP Primitives

## 1. Tools

Executable capabilities.

Examples:

```text
get_aks_status
get_pipeline_status
search_incidents
```

Can be read-only or side-effecting.

## 2. Resources

Data/context that clients can read.

Examples:

```text
runbook://aks/networking
config://production/platform
incident://INC-1042/evidence
```

## 3. Prompts

Reusable prompt/workflow templates exposed by server.

Example:

```text
incident_rca(environment, incident_id)
```

---

# PART 10 — MCP Is NOT

MCP is not:

```text
an LLM
an agent
RAG
vector DB
RBAC engine
secret manager
business validator
human approval system
```

It is a protocol boundary.

This distinction is interview-important.

---

# PART 11 — DevOps Example

Suppose user asks:

```text
Production deployment kyu fail hua?
```

Host has MCP client.

Server advertises:

```text
Tools:
- get_pipeline_status(environment)
- get_terraform_changes(environment)
- get_aks_status(cluster_name)

Resources:
- runbook://aks/networking

Prompts:
- incident_rca
```

The host can discover capabilities instead of hardcoding every integration schema manually.

But safe flow remains:

```text
User Question
 ↓
Discover capabilities
 ↓
Select read-only evidence calls
 ↓
Validate arguments
 ↓
Call MCP tools
 ↓
Preserve evidence outside LLM memory
 ↓
Grounded analysis
 ↓
Validate claims
```

---

# PART 12 — Common Misconceptions

### Misconception 1

```text
MCP = agent framework
```

Wrong. MCP standardizes connectivity/capabilities.

### Misconception 2

```text
MCP tool is automatically safe
```

Wrong. Tool implementation can still be destructive or insecure.

### Misconception 3

```text
MCP replaces REST APIs
```

Not necessarily. MCP server may internally call REST APIs.

### Misconception 4

```text
MCP resources are trusted facts
```

Not automatically. Source, freshness, access and content integrity still matter.

---

# PART 13 — Production Design Principles

```text
least privilege
read-only first
explicit schemas
input validation
output validation
timeouts
rate limits
audit logs
source traceability
secret redaction
human approval for writes
```

MCP changes integration shape, not these fundamentals.

---

# PART 14 — Interview Q&A

### Q1. Why was MCP created?
To standardize how AI applications discover and interact with external tools, data/resources and reusable prompt capabilities instead of building every integration as custom model-facing glue code.

### Q2. Is MCP an agent framework?
No. It is a protocol for capability/context exchange. Agent orchestration can use MCP.

### Q3. How is MCP related to APIs?
An MCP server may wrap APIs, databases, CLIs or local functions and expose them through standardized MCP primitives.

### Q4. Does MCP solve security automatically?
No. Authentication, authorization, validation, least privilege and approval remain implementation responsibilities.

### Q5. What is the biggest connection to Module 1?
Tool contracts and evidence remain application-controlled; MCP standardizes discovery and invocation but does not change the trust boundary.

---

# PART 15 — Revision Cheat Sheet

```text
MCP = standard AI integration protocol
Tool = action/capability
Resource = readable context/data
Prompt = reusable prompt interface
Host = AI application
Client = MCP connection component
Server = capability provider
```

Most important line:

```text
Standardized does not mean trusted.
```

---

# PART 16 — Homework

For a DevOps MCP server, classify these as Tool, Resource or Prompt:

```text
AKS cluster status
Terraform change history
AKS networking runbook
Restart deployment
Incident RCA template
Pipeline logs
```

Then identify which ones need human approval and why.

---

# 🔁 Next Lesson Kyu?

MCP ka purpose clear ho gaya. Ab next question:

```text
Host kya hai?
Client kya hai?
Server kya hai?
Kaun kis responsibility ka owner hai?
```

Next lesson me exact **Host–Client–Server architecture** deeply samjhenge.
