# 🚩 Jai Bajrangbali!

# Lesson 08 — Memory vs Application State

> **Conversation history, agent state, evidence and business state are different things. Mixing them creates unsafe AI systems.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- chat memory kya hai
- application state kya hai
- evidence store kya hai
- workflow state kya hai
- LLM-visible memory ko source of truth kyu nahi maana chahiye
- DevOps incident workflow me state boundaries kaise design karni hain

---

# PART 1 — Core Mental Model

```text
Conversation Memory
!=
Workflow State
!=
Evidence Store
!=
Business Database
!=
Authorization State
```

Ye Module 6 ka most important architecture lesson hai.

---

# PART 2 — English Definitions

**Conversation memory** is prior conversational context used to maintain continuity.

**Application state** is trusted program data representing the current workflow or system state.

**Evidence store** is the preserved collection of source-backed observations used to support claims.

---

# PART 3 — Conversation Memory

Example:

```text
User: Production cluster ka naam prod-aks hai.
Later: Is cluster ka status check karo.
```

Conversation memory can help resolve `this cluster`.

But memory can be:
- stale
- incomplete
- user-provided but unverified
- summarized

So memory is context, not automatically truth.

---

# PART 4 — Application State

Application state examples:

```python
state = {
    "incident_id": "INC-1042",
    "environment": "production",
    "allowed_tools": ["get_pipeline_status", "get_aks_status"],
    "iteration": 2,
}
```

This data is controlled by host application.

---

# PART 5 — Evidence Store

Evidence should preserve:

```text
source
timestamp
tool
tool arguments
raw/normalized result
trust classification
```

Example:

```python
evidence_log.append({
  "source": "pipeline.log",
  "fact": "Deployment failed during Terraform Apply"
})
```

This must not exist only in LLM conversation memory.

---

# PART 6 — Authorization State

Example:

```text
User can read prod logs
User cannot restart prod workloads
```

Never ask model:

```text
"Does user have permission?"
```

Authorization should come from trusted identity/policy system.

---

# PART 7 — DevOps Incident Example

```text
Conversation:
"I think NSG caused the issue"

Evidence:
"NSG rule aks-subnet-allow was removed"

Application state:
environment=production
incident_id=INC-1042

Authorization:
read-only
```

Model may use conversation hypothesis, but final root cause must be grounded in evidence.

---

# PART 8 — Memory in RAG

A common mistake:

```text
Previous answer
 ↓
stored in memory
 ↓
next answer treats previous generated claim as fact
```

This can create hallucination amplification.

Safer:

```text
new question
 ↓
trusted state + fresh retrieval
 ↓
answer
```

Use prior model output carefully.

---

# PART 9 — State Expiry

Operational state changes quickly.

Example:

```text
10:00 cluster degraded
10:10 issue fixed
```

Old memory saying degraded is stale.

Production design needs:

```text
timestamps
TTL
refresh policy
fresh tool call for volatile facts
```

---

# PART 10 — Common Mistakes

- model summary as database
- tool result only inside prompt
- permission state inside chat history
- no timestamps
- stale environment data reused
- generated RCA fed back as confirmed evidence

---

# PART 11 — Interview Q&A

### Q1. Why is conversation memory not a source of truth?
Because it may contain stale, user-provided, summarized or model-generated content that has not been independently verified.

### Q2. Where should tool evidence live?
In application-controlled state/evidence storage with source and timestamp metadata.

### Q3. How should authorization be represented?
Through trusted identity and policy systems, not model reasoning.

### Q4. What is hallucination amplification?
When prior generated claims are reused as if they were verified facts, causing later outputs to compound the error.

---

# PART 12 — Revision

```text
Memory = continuity
State = workflow truth
Evidence = claim support
DB = durable business truth
Authorization = policy decision
```

---

# PART 13 — Homework

For DevOps agent create four separate dictionaries/stores:

```text
conversation_context
workflow_state
evidence_log
permissions
```

List 3 fields that belong in each and explain why.

---

# 🔁 Next Lesson Kyu?

Ab state boundaries clear hain. Next lesson me orchestration ko external world se connect karenge using **tools**, while keeping tool requests untrusted and execution controlled.
