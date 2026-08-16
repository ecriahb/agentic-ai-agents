# 🚩 Jai Bajrangbali!

# Lesson 03 — Agent Specialization & Responsibility Boundaries

> **Good multi-agent design agent names se nahi, clear responsibility, input, output, tools and authority boundaries se banta hai.**

---

# 🎯 Lesson Goal

Aap seekhoge:
- specialist boundary kaise choose karein
- responsibility overlap avoid karna
- tool ownership
- input/output contracts
- read vs write authority
- private vs shared context
- domain-specific DevOps agents

---

# PART 1 — Bad Specialization

Bad:

```text
Agent A = Azure Agent
Agent B = Cloud Agent
Agent C = DevOps Agent
```

Responsibilities overlap.

Better:

```text
Pipeline Specialist
Terraform Specialist
AKS Specialist
Knowledge Specialist
Synthesis/Validation layer
```

Each boundary maps to a distinct evidence domain.

---

# PART 2 — Responsibility Contract

Every specialist should answer:

```text
What problem do I own?
What inputs can I receive?
What tools may I call?
What data may I access?
What output schema must I return?
What decisions am I NOT allowed to make?
```

Example:

```text
Terraform Specialist
Owns: plan/apply/change evidence
Tools: read Terraform plan/state/change metadata
Cannot: claim AKS health, execute apply, approve remediation
```

---

# PART 3 — Input Contract

Avoid sending everything.

```python
{
  "incident_id": "INC-1042",
  "environment": "production",
  "task": "Identify network-related Terraform changes",
  "known_evidence_ids": ["E1"]
}
```

Do not automatically send:
- full conversation
- unrelated runbooks
- secret values
- other agents' scratch reasoning

---

# PART 4 — Output Contract

Specialist output should be normalized:

```python
{
  "agent": "terraform_specialist",
  "status": "SUCCESS",
  "findings": [
    {
      "claim": "NSG rule aks-subnet-allow was removed",
      "evidence_id": "E2",
      "source": "terraform_change_record"
    }
  ],
  "gaps": [],
  "recommended_next_checks": ["ask AKS specialist for connectivity validation"]
}
```

Avoid free-form result only.

---

# PART 5 — Tool Ownership

Principle:

```text
least privilege per agent
```

Pipeline specialist:
- pipeline status
- logs
- job metadata

Terraform specialist:
- plan
- state diff
- IaC repo metadata

AKS specialist:
- cluster status
- events
- networking checks

No reason for all three to share all tools.

---

# PART 6 — Knowledge Agent

Reference knowledge may be separate:

```text
Knowledge Specialist
→ vector search / RAG / MCP resources
→ returns runbook references [R*]
```

Important:

```text
R* reference knowledge != E* current evidence
```

Knowledge specialist should not decide current root cause by itself.

---

# PART 7 — Synthesis Responsibility

Do not let each specialist independently write final RCA.

Better:

```text
Specialists → findings
Validator → checks evidence
Synthesizer → combines validated facts
```

This reduces contradiction and duplicated narrative.

---

# PART 8 — Authority Boundary

Investigation agent:

```text
READ_ONLY
```

Remediation proposer:

```text
CAN_PROPOSE
```

Execution component:

```text
REQUIRES_POLICY_AND_APPROVAL
```

Agent name should never imply authority.

---

# PART 9 — Context Isolation

A specialist should usually receive:

```text
required task
relevant incident fields
approved prior findings
its own tool outputs
```

Not:

```text
all internal messages from every agent
```

Benefits:
- lower token cost
- reduced contamination
- easier testing
- reduced sensitive-data spread

---

# PART 10 — Ownership Table

```text
Pipeline Agent
Input: environment, incident
Output: pipeline evidence

Terraform Agent
Input: environment, suspected change window
Output: IaC evidence

AKS Agent
Input: cluster, hypotheses
Output: runtime/network evidence

Knowledge Agent
Input: query
Output: reference documents

Synthesizer
Input: normalized findings
Output: grounded RCA draft
```

---

# PART 11 — Common Mistakes

- overlapping specialist prompts
- duplicate tool access
- every agent allowed to write
- free-form outputs
- hidden reasoning copied to shared state
- reference agent treated as incident authority
- specialist directly decides permissions

---

# PART 12 — Interview Q&A

### Q1. How do you define an agent boundary?
By domain responsibility, inputs, outputs, tools, context and authority—not by arbitrary names.

### Q2. Why give agents separate toolsets?
Least privilege, easier reasoning, reduced accidental misuse and simpler evaluation.

### Q3. Should specialists write final answer?
Usually no; normalized specialist findings should be validated and synthesized centrally.

### Q4. What belongs in shared state?
Source-backed normalized outputs and workflow metadata, not all internal context.

---

# PART 13 — Revision

```text
Specialize by responsibility.
Minimize tools.
Contract inputs/outputs.
Separate evidence from reference.
Separate analysis from authority.
```

---

# PART 14 — Homework

Create contracts for:

```text
Pipeline Specialist
Terraform Specialist
AKS Specialist
```

For each define:
- allowed tools
- forbidden actions
- input schema
- output schema
- evidence IDs

---

# 🔁 Next Lesson Kyu?

Specialists ready hain. Ab unhe centrally coordinate karne ke liye **Supervisor/Subagent pattern** build karenge.
