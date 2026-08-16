# 🚩 Jai Bajrangbali!

# Lesson 11 — Reusable & Versioned Prompt Templates

> **Production prompt ko copy-paste string nahi, versioned application asset samjho.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- prompt template kya hai
- placeholders ka role
- stable policy vs runtime variables
- prompt versioning
- template validation
- provider-independent templates
- secrets/context injection concerns
- testing and change management
- when template abstraction becomes over-engineering

---

# 1. English Definition

**A prompt template is a reusable, parameterized prompt definition whose stable instructions remain controlled while approved runtime values are inserted for each task.**

Mental model:

```text
Versioned Template
      +
Validated Runtime Variables
      +
Authorized Context
      =
Rendered Prompt
```

---

# 2. Why Templates?

Without templates:

```python
prompt = "Analyze prod..."
```

scattered across many scripts.

Soon:

- one script says abstain
- another forgets it
- one uses old output format
- another leaks extra context

Template centralizes behavior.

---

# 3. Simple Template

```text
ROLE
{role}

INCIDENT
{incident}

CURRENT EVIDENCE
{evidence}

RULES
{rules}

OUTPUT
{output_contract}
```

Runtime only fills approved fields.

---

# 4. Stable vs Runtime Fields

Stable/application-owned:

```text
read-only policy
evidence rules
abstention behavior
output sections
forbidden assumptions
```

Runtime/user/workflow-owned:

```text
incident ID
environment
question
evidence records
```

Do not let user supply the entire system template if application intends stable policy.

---

# 5. Template Injection Concern

Bad:

```python
system_prompt = user_input
```

Better:

```python
system_prompt = APPROVED_TEMPLATE
user_task = validated_user_request
```

Even when variables are inserted, external content remains untrusted data.

---

# 6. Source-Labeled Evidence Placeholder

Instead of:

```text
{all_text}
```

prefer a context builder that produces:

```text
[E1] ...
[E2] ...

REFERENCE
[R1] ...
```

Template should not be responsible for discovering provenance after the fact.

---

# 7. Template Versioning

Example:

```text
incident_rca_v1
incident_rca_v2
incident_rca_v3
```

Changes may include:

```text
new abstention rule
new output field
updated terminology
security hardening
```

Store version with traces/eval results.

---

# 8. Model/Provider Independence

Template should ideally describe task semantics, not vendor-specific quirks.

Same rendered task can go to:

```text
Ollama
OpenAI
```

Provider adapter handles API representation.

If a provider requires special formatting, isolate that in provider integration rather than contaminating business prompt everywhere.

---

# 9. Example Python Renderer

```python
from string import Template

PROMPT = Template("""
INCIDENT:
$incident

EVIDENCE:
$evidence

TASK:
Return confirmed facts and evidence gaps.
""")

rendered = PROMPT.substitute(
    incident="Deployment failed",
    evidence="[E1] Terraform Apply failed",
)
```

For larger applications, LangChain PromptTemplate or another typed/template layer can help, but basic concept is the same.

---

# 10. Validate Runtime Variables

Before render:

```text
environment must be allowed
incident must not be empty
evidence must come from approved collection path
secrets must be redacted
context length must be bounded
```

Template does not sanitize untrusted data automatically.

---

# 11. Prompt Registry Mental Model

Production may have:

```text
Prompt Registry
├─ incident_rca:v3
├─ terraform_review:v2
└─ runbook_answer:v5
```

Each record can track:

```text
owner
version
approved date
eval dataset
model compatibility
release notes
```

This is governance, not just formatting.

---

# 12. Expected Output Contract

Template can include fixed output contract:

```text
Confirmed Evidence
Likely Root Cause
Confirmed Impact
Evidence Gaps
Recommended Next Checks
Confidence
```

Later parser/Pydantic validates shape.

Again:

```text
Template + schema = consistency
not factual proof
```

---

# 13. Regression Workflow

```text
Edit template
   ↓
Run unit/render tests
   ↓
Run prompt eval dataset
   ↓
Compare old/new results
   ↓
Security/adversarial tests
   ↓
Approve version
```

Do not hot-edit production prompt without traceability.

---

# 14. Common Mistakes

1. Prompts duplicated in many files.
2. No version identifier.
3. User controls stable safety rules.
4. Raw secret-bearing context inserted blindly.
5. Template change not regression-tested.
6. Provider-specific hacks spread through business logic.
7. Placeholders missing validation.
8. Giant universal template for unrelated tasks.

---

# 15. When Not to Template Too Much

For a tiny learning script:

```python
prompt = "Explain AKS in two lines"
```

is fine.

Abstraction adds value when:

```text
prompt reused
multiple environments
multiple providers
multiple versions
production evals
team ownership
```

Use simplest design that preserves maintainability.

---

# 16. Interview Q&A

### Q1. Why version prompts?
Because prompt changes can alter application behavior and need traceability/regression testing.

### Q2. What belongs in a template?
Stable task instructions, constraints and output contract, with validated placeholders for runtime values.

### Q3. Should users control system prompt templates?
Not when the application depends on those rules for stable behavior.

### Q4. How do templates help provider portability?
They keep business/task semantics separate from provider-specific API integration.

### Q5. Do templates prevent prompt injection?
No. They help structure instructions, but untrusted runtime content still requires isolation and deterministic security controls.

---

# 17. Quick Revision

```text
Template = stable contract
Variables = validated runtime data
Version = traceability
Eval = confidence in behavior
```

---

# 🧪 Homework

Create two versioned templates:

```text
incident_rca_v1
incident_rca_v2
```

In v2 add:

```text
customer impact must be UNKNOWN unless impact evidence exists
```

Run both against same dataset and record behavior difference.

---

# ➡️ Why Next?

Ab saare pieces ready hain. Lesson 12 me hum unko combine karke **complete DevOps Incident Analysis Prompt System** banayenge.
