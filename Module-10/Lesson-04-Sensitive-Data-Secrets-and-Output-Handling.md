# 🚩 Jai Bajrangbali!

# Lesson 04 — Sensitive Data, Secrets & Output Handling

> **The safest secret is the one that never enters the model context, trace, checkpoint or final response.**

---

# 🎯 Lesson Goal

You will understand:

- sensitive-data flow through agents
- secret minimization
- Key Vault/identity mental model
- prompt/log/checkpoint leakage
- output handling risks
- data classification and redaction
- structured output validation
- downstream command/SQL/HTML risks
- retention and audit boundaries
- DevOps practical examples

---

# PART 1 — English Definition

**Sensitive information disclosure occurs when confidential data such as credentials, tokens, private source content or regulated information is exposed to unauthorized users, systems or model contexts.**

---

# PART 2 — Where Secrets Can Leak

Agent data path:

```text
Environment / Secret Store
      ↓
Tool
      ↓
Tool Output
      ↓
Prompt Context
      ↓
Model Output
      ↓
Trace / Log / Checkpoint
      ↓
User / Other Agent
```

Every stage needs minimization.

---

# PART 3 — Secret Inventory

DevOps examples:

```text
Azure client secrets
tokens
GitHub PATs
Kubeconfigs
connection strings
private keys
Terraform credentials
SAS tokens
API keys
internal endpoint credentials
```

Do not index these in RAG.

---

# PART 4 — Secretless First

Prefer:

```text
managed identity
workload identity
federated/OIDC credentials
short-lived tokens
```

over:

```text
long-lived secret in .env
```

Secret management is still needed for third-party/legacy systems, but model should not see raw secret when only backend connector needs it.

---

# PART 5 — Principle of Data Minimization

If model needs:

```text
"API authentication failed"
```

it does not need:

```text
Authorization: Bearer eyJ...
```

Normalize tool results before context construction.

---

# PART 6 — Vulnerable Logging

```python
logger.info("Tool response: %s", raw_response)
```

Raw response may contain:

```text
headers
tokens
connection strings
user data
```

Safer:

```text
log status + source ID + redacted metadata
```

---

# PART 7 — Checkpoint Leakage

Stateful agents persist data.

Danger:

```text
workflow state contains raw token
 ↓
checkpoint database retains it
 ↓
backup retains it
 ↓
trace/debug output exposes it
```

State schema should avoid secrets by design.

---

# PART 8 — Redaction

Redaction examples:

```text
Bearer <REDACTED>
password=<REDACTED>
client_secret=<REDACTED>
```

Regex helps for known formats, but classification/minimization should happen earlier.

Redaction is not perfect secret detection.

---

# PART 9 — Output Handling Risk

LLM output is untrusted data.

Do not directly use as:

```text
shell command
SQL query
HTML
Terraform HCL apply input
kubectl command
file path
HTTP URL
```

without domain-specific validation/escaping/allowlisting.

---

# PART 10 — Improper Output Handling Example

Unsafe:

```python
command = llm.invoke(prompt)
subprocess.run(command, shell=True)
```

Safe:

```text
LLM → structured proposal
Host → validate operation enum + args
Executor → known API call
```

---

# PART 11 — Structured Output Is Not Automatically Safe

Model returns:

```json
{
  "action": "get_logs",
  "namespace": "../../secret"
}
```

JSON shape can be valid while argument is unsafe.

Validate:

```text
enum
target inventory
path/name pattern
authorization
risk policy
```

---

# PART 12 — Data Classification

Example classes:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
SECRET
```

For each define:

```text
Can model see it?
Can it enter RAG?
Can it be logged?
Can it cross region/provider?
Retention?
Who can retrieve it?
```

---

# PART 13 — RAG and Sensitive Data

Before ingestion:

```text
source authorization
secret scan
classification
ACL tagging
retention policy
```

At query:

```text
identity → ACL filter → retrieval
```

Do not retrieve sensitive chunk and then ask model not to disclose it.

---

# PART 14 — Multi-Agent Leakage

Private context for Terraform specialist may contain infrastructure details not needed by communication/reporting agent.

Share:

```text
minimum structured finding
source IDs
```

not full private prompt/context.

---

# PART 15 — Model Provider Boundary

Before sending data to any model endpoint ask:

```text
Is provider approved?
What data classification is allowed?
What region/data handling applies?
Is logging/training policy acceptable?
```

Architecture/governance owns this—not individual prompt code.

---

# PART 16 — Telemetry Strategy

Safer trace record:

```json
{
  "request_id": "req-123",
  "tool": "get_aks_status",
  "source_id": "E3",
  "status": "SUCCESS",
  "payload_logged": false,
  "redaction_count": 0
}
```

Full payload can be stored separately with tighter access if required.

---

# PART 17 — Security Test Cases

```text
SD-01 secret in user prompt
SD-02 secret in tool output
SD-03 token in RAG document
SD-04 secret in agent private state
SD-05 malicious model echoes hidden value
SD-06 output contains shell metacharacters
SD-07 sensitive trace exported
```

Expected outcome is policy/redaction/block, not just a model refusal.

---

# PART 18 — Common Mistakes

- full environment dumped into prompt
- raw HTTP headers logged
- RAG indexes `.env`/tfstate
- checkpoint persists credentials
- model output executed directly
- redaction applied only at UI
- all agents share same private context
- no data classification policy

---

# PART 19 — Interview Q&A

### Q1. Best way to protect secrets from LLM leakage?
Avoid putting secrets into model-visible context whenever possible; use workload identities and backend connectors.

### Q2. Why is structured output still untrusted?
Structure validates format, not authorization, semantic safety or target validity.

### Q3. Why is tracing risky?
Agent traces can contain prompts, source documents, tool arguments and outputs that include confidential data.

### Q4. How should RAG protect sensitive documents?
Enforce source governance and authorization before retrieval, with metadata/ACLs and secret scanning at ingestion.

---

# 🧠 Revision

```text
Sensitive Data Safety =
Minimize → Classify → Authorize → Redact → Validate Output → Limit Retention
```

---

# 📝 Homework

Map each of these to allowed storage/model/log behavior:

```text
GitHub PAT
AKS event
Terraform plan
customer incident text
internal runbook
private key
```

---

# 🔁 Next Lesson Kyu?

Data leakage is controlled. Next we protect the knowledge layer itself against **RAG poisoning, stale content and vector/embedding weaknesses**.
