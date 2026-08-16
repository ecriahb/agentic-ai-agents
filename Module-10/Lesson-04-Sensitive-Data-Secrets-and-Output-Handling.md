# 🚩 Jai Bajrangbali!

# Lesson 04 — Sensitive Data, Secrets & Output Handling

> **Agent security sirf input filtering nahi hai; model context, tool results, logs, traces and final outputs sab data-leak paths ho sakte hain.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- sensitive-data exposure paths
- secrets ko model context se door kyu rakhna hai
- input/output/tool-result redaction
- improper output handling
- logs/traces/checkpoints me secret risk
- downstream command/code execution risk

---

# PART 1 — English Definitions

**Sensitive information disclosure** is unintended exposure of confidential information through model inputs, outputs, logs, tools, memory or connected systems.

**Improper output handling** occurs when model-generated output is used by downstream components without sufficient validation or sanitization.

---

# PART 2 — DevOps Sensitive Data

Examples:
```text
Azure client secrets
GitHub PATs
SSH private keys
Kubeconfig tokens
connection strings
Terraform state secrets
customer IDs/log payloads
internal hostnames
incident attachments
API credentials
```

---

# PART 3 — Secret Flow Analysis

Ask for every secret:
```text
Where is it created?
Where is it stored?
Which process reads it?
Does it enter prompt/context?
Can it appear in tool output?
Can it appear in trace/log/checkpoint?
Can model reproduce it?
```

Best answer for model context is usually: **secret value should not enter it at all**.

---

# PART 4 — Secret Reference vs Secret Value

Bad:
```text
Prompt: use password SuperSecret123 to check SQL
```

Better:
```text
Tool receives secret internally from Key Vault/managed identity.
Model sees only operation result.
```

```text
LLM → check_database_health(database_id)
Tool host → authenticate securely
LLM ← status=healthy
```

---

# PART 5 — Redaction Pipeline

```text
Tool Result
 ↓
Normalizer
 ↓
Secret/PII detector
 ↓
Redact/Mask
 ↓
Evidence Store
 ↓
LLM Context
```

Example:
```text
Authorization: Bearer eyJ...
```
becomes:
```text
Authorization: [REDACTED_TOKEN]
```

---

# PART 6 — Output Handling Risk

Model returns:
```text
kubectl delete namespace production
```

Unsafe:
```text
LLM output → shell
```

Safe:
```text
LLM output → structured proposal
 ↓
parser
 ↓
policy
 ↓
authorization
 ↓
approval
 ↓
controlled executor
```

Never execute free-form model text as shell/SQL/Terraform.

---

# PART 7 — Traces and Checkpoints

Observability can accidentally become a secret store.

Redact before logging:
```text
prompts
headers
tool arguments
tool outputs
MCP resources
checkpoint state
agent messages
```

Store only what is required for audit/debugging.

---

# PART 8 — Data Minimization

Instead of full 20 MB log:
```text
retrieve relevant lines
normalize
redact
label source
send minimum evidence
```

Benefits:
```text
less leakage risk
lower token cost
less prompt injection surface
better relevance
```

---

# PART 9 — Practical Security Tests

```text
secret embedded in pipeline log
secret in exception stack trace
secret in Terraform output
secret in retrieved document
model asked “repeat hidden credentials”
model output sent to shell
HTML/Markdown output rendered unsafely
trace exporter receives raw Authorization header
```

---

# PART 10 — Common Mistakes

- `.env` content placed in prompt
- debug logging full tool payload
- model output passed directly to shell
- redaction only on final answer
- shared checkpoints containing credentials
- screenshots/logs with access tokens indexed into RAG

---

# PART 11 — Interview Q&A

### Q1. Best way to protect a secret from an LLM?
Do not place the secret value in the model context; let trusted tools use managed identity/secret stores internally.

### Q2. Why validate model output?
Because model output is untrusted data and can become dangerous when interpreted by shells, APIs, browsers or automation engines.

### Q3. Where should redaction occur?
As early as practical before data reaches prompts, logs, traces, checkpoints or persistent evidence stores.

---

# PART 12 — Revision

```text
Need-to-know data only
Secret reference > secret value
LLM output = untrusted
Redact before persistence
Structured executor > free-form shell
```

---

# PART 13 — Homework

Design a redaction policy for pipeline logs containing tokens, emails, internal IPs and connection strings. Decide block vs mask vs hash per field.

---

# 🔁 Next Lesson Kyu?

Ab data leakage clear hai. Next dekhenge ki RAG/embedding pipeline khud malicious or poisoned knowledge ko agent context me kaise la sakti hai.
