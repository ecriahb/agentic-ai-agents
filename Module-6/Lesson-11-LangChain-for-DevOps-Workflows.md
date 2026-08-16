# 🚩 Jai Bajrangbali!

# Lesson 11 — LangChain for DevOps Workflows

> **Goal framework demo banana nahi; evidence-grounded DevOps workflow ko clear components me orchestrate karna hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- real incident workflow ko components me break karna
- retrieval knowledge vs live evidence separate karna
- tool + RAG + prompt + parser combine karna
- deterministic validation boundaries
- read-only-first investigation
- human approval placement
- framework vs application responsibility

---

# PART 1 — Target Scenario

Incident:

```text
Production AKS deployment failed after Terraform networking change.
```

We need:

```text
knowledge
current evidence
analysis
validation
safe output
```

---

# PART 2 — Architecture

```text
Incident Input
      ↓
Input Validation
      ↓
┌───────────────┬─────────────────┐
│               │                 │
Retriever       Pipeline Tool     Terraform Tool
│               │                 │
Runbooks        Live Evidence     Change Evidence
└───────────────┴─────────────────┘
      ↓
Evidence/Context Builder
      ↓
RCA PromptTemplate
      ↓
Chat Model
      ↓
Structured Parser
      ↓
Evidence Claim Validator
      ↓
Policy / Confidence
      ↓
Final Read-Only RCA
```

---

# PART 3 — Two Knowledge Classes

Do not mix labels.

### Reference Knowledge

```text
runbooks
architecture docs
past troubleshooting guidance
```

### Current Incident Evidence

```text
current pipeline logs
current Terraform change
current AKS status
```

Prompt should say:

```text
REFERENCE = explains what may happen
EVIDENCE = supports what happened now
```

A runbook cannot prove current cause.

---

# PART 4 — Component Boundaries

### Input Validator
Checks environment/incident format.

### Retriever
Returns relevant reference docs.

### Tools
Collect current read-only evidence.

### Context Builder
Labels source and trust class.

### Prompt
Defines reasoning/output contract.

### Model
Generates analysis.

### Parser
Converts to structured form.

### Validator
Checks claims against evidence.

---

# PART 5 — Deterministic Evidence Record

```python
{
  "id": "E1",
  "type": "current_evidence",
  "source": "pipeline",
  "tool": "get_pipeline_status",
  "result": "Failed during Terraform Apply"
}
```

Reference:

```python
{
  "id": "R1",
  "type": "reference",
  "source": "aks-networking.md",
  "content": "NSG changes can affect subnet connectivity"
}
```

Now LLM can cite categories explicitly.

---

# PART 6 — Prompt Contract

```text
ROLE: Evidence-first DevOps incident analyst.

RULES:
- Current facts require E* evidence.
- R* reference sources may explain mechanisms but do not prove current facts.
- Never invent downtime, actor, commands executed or business impact.
- If current evidence is insufficient, state UNKNOWN.
- Do not claim to execute remediation.

RETURN:
Root Cause
Confirmed Evidence
Reference Explanation
Impact
Recommended Next Checks
Confidence
```

---

# PART 7 — Tool Selection Strategy

For this module, simplest safe strategy:

```text
application decides fixed investigation tools
```

Example:

```text
pipeline status
terraform changes
AKS health
```

Later advanced agents can choose tools dynamically.

Why fixed first?

```text
more deterministic
simpler to test
easier authorization
clear evidence coverage
```

---

# PART 8 — Read-Only First

Allowed:

```text
read logs
read plan/change summary
read cluster health
retrieve runbooks
```

Not automatically allowed:

```text
restore NSG
restart cluster
run Terraform apply
kubectl delete
```

Final assistant recommends; human/operator acts.

---

# PART 9 — Validation Examples

Model output:

```text
Impact: 3 hours of customer downtime
```

Evidence has no duration.

Validator:

```text
REJECT / downgrade claim
```

Model output:

```text
Deployment failed during Terraform Apply [E1]
```

Evidence E1 supports it.

```text
ACCEPT
```

---

# PART 10 — Confidence Policy

Do not let confidence be pure model feeling.

Example deterministic policy:

```text
0 current evidence → low
1 supporting source → low/medium
2+ independent current evidence sources aligned → medium/high according to policy
conflicting evidence → cap confidence
```

Exact policy organization-specific.

---

# PART 11 — Workflow Error States

Possible statuses:

```text
INVALID_INPUT
RETRIEVAL_FAILED
TOOL_TIMEOUT
TOOL_UNAUTHORIZED
INSUFFICIENT_EVIDENCE
MODEL_FAILED
PARSE_FAILED
VALIDATION_FAILED
SUCCESS
```

This is much better than always returning prose.

---

# PART 12 — Observability

For incident run preserve:

```text
request_id
incident_id
tool calls
retrieved sources
model/version
latency per stage
parser status
validation findings
final confidence
```

Sensitive data should be redacted.

---

# PART 13 — Framework Responsibility vs Our Responsibility

### Framework helps

```text
component interfaces
composition
model wrappers
retriever wrappers
parsers
callbacks/tracing hooks
```

### We still own

```text
RBAC
source trust
business validation
side-effect policy
human approval
secret management
freshness
SLOs
```

---

# PART 14 — Common Mistakes

- reference docs presented as current evidence
- model decides confidence without policy
- tool errors swallowed
- entire workflow one giant agent
- mutation mixed into investigation
- no evidence IDs
- parser success treated as truth

---

# PART 15 — Interview Q&A

### Q1. How would you use LangChain in a DevOps incident assistant?
I would use it to compose retrievers, read-only evidence tools, prompt templates, model calls and parsers while keeping authorization, evidence validation and remediation policy in application-controlled layers.

### Q2. Why distinguish reference knowledge from current evidence?
Reference docs explain possible mechanisms, while only current evidence can support factual claims about the active incident.

### Q3. Where should confidence be calculated?
Preferably through an application policy informed by evidence quality, quantity and conflicts rather than model self-assessment alone.

### Q4. Would you allow automatic remediation in the same chain?
Not initially. Investigation should be read-only-first, with remediation behind explicit policy and human approval.

---

# PART 16 — Revision

```text
Reference = guidance
Evidence = current observation
LLM = analyst
Parser = structure
Validator = trust gate
Human approval = action gate
```

---

# PART 17 — Homework

Design an incident workflow for:

```text
GitHub Actions deployment failed to AKS
```

Include:

- 2 reference sources
- 3 live read-only tools
- evidence IDs
- structured output
- 3 validation rules
- one human approval boundary

---

# 🔁 Next Lesson Kyu?

Ab saare individual concepts connect ho gaye. Next lesson me **V1→V10 final mini-project** ke through end-to-end Orchestrated DevOps RAG Assistant build karenge.
