# 🚩 Jai Bajrangbali!

# Lesson 05 — Fake Tool → Real Tool

> **Agent ka brain same rahega; ab uske fake hands ko real DevOps systems se connect karna hai.**

## 🎯 Learning Goal

Is lesson me hum samjhenge:

- fake tool kya hota hai
- fake tools se learning kyun start ki
- real tool kya hota hai
- tool contract kya hota hai
- same Python function ko mock data se real Azure/AKS/Terraform data tak kaise evolve karte hain
- authentication, permissions aur safety kyun important hain
- read-only tools pehle kyun build karne chahiye
- hallucination ko real evidence se kaise reduce karte hain
- production-grade DevOps agent ka next architecture kya hoga

---

# 1. Fake Tool Kya Hai?

**English Definition:**
> A fake tool is a function that imitates the interface and expected behavior of a real external system but returns controlled or hard-coded data instead of calling the real system.

Example:

```python
def get_aks_status(cluster_name: str):
    if cluster_name == "prod-aks":
        return "Degraded - network connectivity failures detected"
    return "Healthy"
```

Ye Azure ko call nahi kar raha. Ye learning ke liye known response de raha hai.

### Why use it?

Because first hume agent architecture samajhna tha:

```text
LLM
 ↓
chooses tool
 ↓
Python executes function
 ↓
tool result
 ↓
LLM reasons
```

Agar starting se Azure authentication, CLI errors, subscriptions, RBAC, networking aur SDK complexity add kar dete, to core agent concept hide ho jata.

---

# 2. Real Tool Kya Hai?

**English Definition:**
> A real tool is an application function that retrieves data from, or performs an approved action against, an actual external system such as Azure, Kubernetes, GitHub, Terraform, a monitoring platform, or an internal API.

Example mental model:

```text
Fake Tool
return "Degraded"

Real Tool
az / kubectl / Azure SDK / REST API
        ↓
actual environment response
```

Important:

> **LLM still does not directly operate Azure. Python/application code performs the authenticated external call.**

---

# 3. Tool Contract — Most Important Concept

**English Definition:**
> A tool contract defines the tool name, purpose, accepted arguments, returned data, and behavioral expectations that the agent can rely on.

Example contract:

```python
def get_aks_status(cluster_name: str) -> str:
    ...
```

Agent ke perspective se contract same reh sakta hai:

```text
Tool Name: get_aks_status
Input: cluster_name
Output: cluster health/status evidence
```

Implementation change ho sakti hai:

```text
Version A → hard-coded dictionary
Version B → subprocess + az CLI
Version C → Azure SDK
Version D → internal platform API
```

Agent ko har baar redesign karna zaroori nahi hota if contract stable hai.

---

# 4. Fake → Real Evolution

```text
Step 1
Fake Function
known data return karta hai
       ↓
Step 2
Tool schema / arguments stabilize
       ↓
Step 3
Real read-only command connect
       ↓
Step 4
Output normalize
       ↓
Step 5
Error handling + timeout
       ↓
Step 6
Authentication + RBAC
       ↓
Step 7
Logging / audit
       ↓
Step 8
Human approval for risky actions
```

---

# 5. Example — AKS Status Tool

## Fake Version

```python
def get_aks_status(cluster_name: str):
    fake_data = {
        "prod-aks": "Degraded - network connectivity failures detected",
        "stage-aks": "Healthy",
        "dev-aks": "Healthy"
    }

    return fake_data.get(cluster_name, "Cluster not found")
```

## Real-World Direction

A real implementation could call an approved interface such as:

```text
Azure SDK
az CLI
kubectl
Internal Platform API
Monitoring API
```

Pseudo-pattern:

```python
def get_aks_status(cluster_name: str):
    result = call_real_aks_source(cluster_name)
    return normalize_status(result)
```

Important learning point:

> Tool ka **business purpose** same hai; data source real ho gaya.

---

# 6. Example — Pipeline Status Tool

Fake:

```python
def get_pipeline_status(environment: str):
    if environment == "production":
        return "Failed during Terraform Apply"
    return "Succeeded"
```

Real architecture:

```text
Agent
 ↓
get_pipeline_status("production")
 ↓
Python Tool
 ↓
GitHub Actions / Azure DevOps API
 ↓
Latest deployment run
 ↓
Normalized evidence
 ↓
Agent
```

Normalized output example:

```json
{
  "environment": "production",
  "status": "failed",
  "stage": "Terraform Apply",
  "run_id": "12345"
}
```

Structured tool output future agents ke liye plain text se better hota hai.

---

# 7. Example — Terraform Changes Tool

Fake evidence:

```text
NSG rule allowing AKS subnet traffic was removed
```

Real data sources ho sakte hain:

```text
terraform plan output
Git diff
Pull Request patch
Terraform state comparison
CI artifact
```

Agent flow:

```text
Deployment Failed
      ↓
Pipeline tool says:
Terraform Apply failed
      ↓
Terraform tool says:
AKS NSG allow rule removed
      ↓
AKS tool says:
network connectivity degraded
      ↓
Evidence correlation
      ↓
RCA
```

Yahi point agent ko generic chatbot se useful DevOps investigation system banata hai.

---

# 8. Tool Output Ko Normalize Kyun Karein?

Raw command output noisy ho sakta hai:

```text
hundreds of CLI lines
warnings
timestamps
irrelevant metadata
```

Agent ko sirf useful evidence dena better hai.

```text
Raw External Output
       ↓
Parser / Normalizer
       ↓
Small Structured Evidence
       ↓
LLM
```

Example:

```json
{
  "cluster": "prod-aks",
  "health": "degraded",
  "network_issue": true,
  "evidence": "connectivity failures detected"
}
```

Benefits:

- token usage reduce
- irrelevant noise reduce
- reliable reasoning improve
- schema validation possible
- easier testing

---

# 9. Authentication

**English Definition:**
> Authentication verifies who or what is making a request.

Real tools ko identity chahiye.

Examples:

```text
Azure Managed Identity
Service Principal / Workload Identity
GitHub App / Token
Azure DevOps Service Connection
Kubernetes credentials
```

Golden rule:

> **Credentials LLM prompt me nahi dene. Credentials application/tool layer me securely manage karne hain.**

Bad:

```text
Prompt contains client secret
```

Good:

```text
LLM requests tool
     ↓
Application already has approved identity
     ↓
Tool authenticates securely
```

---

# 10. Authorization / RBAC

**English Definition:**
> Authorization determines what an authenticated identity is allowed to do.

Agent ko unnecessary permissions nahi deni chahiye.

Use **least privilege**:

```text
Need only AKS health?
→ Reader permission

Need only pipeline logs?
→ Read-only pipeline permission

Need remediation?
→ Separate controlled action path + approval
```

---

# 11. Read-Only First

Production DevOps agent ke liye safest progression:

```text
Phase 1
Read evidence only

Phase 2
Recommend fix

Phase 3
Generate proposed command/change

Phase 4
Human approval

Phase 5
Controlled execution
```

Directly auto-remediation se start nahi karna chahiye.

Why?

- LLM wrong interpretation kar sakta hai
- tool wrong target receive kar sakta hai
- production blast radius high ho sakta hai
- audit/approval required ho sakta hai

---

# 12. Hallucination vs Grounding

Without tools:

```text
Prompt:
Deployment failed after Terraform change.

LLM:
Maybe NSG issue.
Maybe DNS.
Maybe route table.
Maybe identity.
```

With real tools:

```text
Pipeline evidence:
Failed during Terraform Apply

Terraform evidence:
AKS NSG allow rule removed

AKS evidence:
Network connectivity degraded
```

Now final RCA:

```text
Removed NSG rule disrupted required AKS network traffic.
```

**English Definition:**
> Grounding means basing the model's answer on supplied evidence or authoritative data rather than relying only on model memory or speculation.

---

# 13. Errors Are Also Evidence

Real tools always successful nahi honge.

Possible errors:

```text
401 / authentication failed
403 / permission denied
timeout
cluster not found
API unavailable
CLI command failed
invalid argument
```

Wrong approach:

```python
except Exception:
    return "Healthy"
```

Ye dangerous hai because failure ko fake success bana diya.

Better principle:

```text
Tool failure ≠ system healthy
Tool failure = investigation evidence
```

Normalized example:

```json
{
  "success": false,
  "error_type": "permission_denied",
  "message": "Unable to read AKS resource"
}
```

---

# 14. Timeout and Retry

Real external systems slow/unavailable ho sakte hain.

**Timeout:** maximum time application ek external call ke complete hone ka wait karegi.

**Retry:** temporary failure ke baad controlled repeat attempt.

Important:

> Every operation blindly retry nahi karna. Read-only transient calls aur destructive actions ka retry behavior different hona chahiye.

---

# 15. Audit Logging

Production agent me record hona chahiye:

```text
Who requested investigation?
Which tool was called?
Which arguments were used?
What evidence returned?
What recommendation generated?
Was an action approved?
Who approved it?
```

This creates traceability.

---

# 16. Human-in-the-Loop

**English Definition:**
> Human-in-the-loop is a control pattern where a person reviews or approves important AI-generated decisions or actions before execution.

Example:

```text
Agent finds removed NSG rule
       ↓
Agent proposes restore rule
       ↓
Human reviews Terraform diff
       ↓
Approve
       ↓
Pipeline executes change
```

LLM recommendation aur infrastructure mutation ko separate rakhna safer architecture hai.

---

# 17. Target DevOps Agent Architecture

```text
User / Incident Trigger
        ↓
Investigation Agent
        ↓
Tool Router
   ├── AKS Read Tool
   ├── Pipeline Read Tool
   ├── Terraform / Git Diff Tool
   ├── Logs Tool
   └── Monitoring Tool
        ↓
Evidence State
        ↓
Structured RCA Generator
        ↓
Validation
        ↓
Human Review
        ↓
Optional Controlled Remediation
```

---

# 18. Fake Tool vs Real Tool Comparison

| Area | Fake Tool | Real Tool |
|---|---|---|
| Data | Hard-coded | Live external data |
| Authentication | Usually none | Required |
| Permissions | Not relevant | RBAC / least privilege |
| Failure modes | Controlled | Network/API/auth/timeouts |
| Testing | Easy | Needs mocks/integration tests |
| Risk | Low | Can affect production if write-enabled |
| Purpose | Learn architecture | Solve actual operational problem |

---

# 19. What Stays Same?

Most important architecture lesson:

```text
Agent Reasoning Pattern
        SAME

Tool Contract
        MOSTLY SAME

Tool Implementation
        CHANGES

Fake Data Source
        ↓
Real DevOps Source
```

Isliye fake tools waste nahi the. Wo architecture ko safely build/test karne ka first stage the.

---

# 20. Interview Corner

### Q1. Why start with fake tools when building an AI agent?
> Fake tools isolate agent reasoning and tool-calling logic from authentication, networking and external-system complexity, making the architecture easier to learn and test.

### Q2. What changes when a fake tool becomes a real tool?
> The tool implementation starts calling an actual external system, while the tool contract can often remain stable.

### Q3. Does the LLM receive cloud credentials?
> It should not. Credentials should remain in the application or secure execution layer; the LLM only requests an approved tool operation.

### Q4. Why should DevOps agents start read-only?
> Read-only access limits blast radius while the system proves its reasoning, grounding, authorization, logging and approval controls.

### Q5. What is grounding?
> Grounding means generating conclusions from supplied authoritative evidence instead of relying only on the model's internal knowledge or guesses.

### Q6. What is human-in-the-loop?
> It is a control pattern where a human reviews or approves important model-generated decisions or actions before execution.

---

# 🧠 Final Revision Sheet

```text
Fake Tool
= Controlled learning implementation

Real Tool
= Actual external-system integration

Tool Contract
= Name + purpose + arguments + result expectations

Authentication
= Who are you?

Authorization
= What are you allowed to do?

Least Privilege
= Minimum permissions required

Grounding
= Reason from evidence

Read-Only First
= Investigate safely before automating changes

Human-in-the-Loop
= Human approval before high-impact action
```

---

# ✅ Module 1 Completion Mental Model

```text
ChatGPT UI vs API
        ↓
Python Environment + Secrets
        ↓
First Real AI API Call
        ↓
Local Ollama
        ↓
Structured Output
        ↓
Tool Calling
        ↓
Agent Loop
        ↓
DevOps Agent V1 → V4
        ↓
Fake Tool → Real Tool
```

> **Module 1 ka final lesson: AI ko sirf bolna nahi sikhaya; application ko real-world evidence lene ke liye hands dene ka architecture samjha.**
