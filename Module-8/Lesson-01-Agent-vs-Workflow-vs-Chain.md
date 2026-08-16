# 🚩 Jai Bajrangbali!

# Lesson 01 — Agent vs Workflow vs Chain

> **Har multi-step AI application agent nahi hoti. Pehle fixed workflow, chain aur agent ke difference ko clearly samjho.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- chain kya hoti hai
- workflow kya hota hai
- agent kya hota hai
- deterministic vs dynamic control flow
- agent kab useful hai aur kab unnecessary risk hai
- Module 1–7 ka architecture in categories me kaise map hota hai

---

# PART 1 — English Definitions

A **chain** is a sequence of components where output from one step becomes input to the next.

A **workflow** is an application-controlled process with predefined steps, branches or policies.

An **agent** is a system in which the model can dynamically influence what steps or tools are used to achieve a goal, within application-defined boundaries.

---

# PART 2 — Simple Mental Model

## Chain

```text
Input → Prompt → LLM → Parser → Output
```

## Workflow

```text
Input
 ↓
Validate
 ↓
Retrieve
 ↓
If weak? ──Yes→ Abstain
 ↓ No
LLM
 ↓
Validate
 ↓
Output
```

## Agent

```text
Goal
 ↓
Observe State
 ↓
Choose Next Step
 ↓
Use Tool / Retrieve / Ask / Stop
 ↓
Observe New State
 ↓
Repeat Until Done or Policy Stops It
```

---

# PART 3 — Module 1 Example

Module 1 me hamara trusted RCA flow largely application-controlled tha:

```text
read log
→ preserve evidence
→ build prompt
→ generate RCA
→ validate claims
```

Ye primarily **workflow** tha.

Agar model decide kare:

```text
"Mujhe pehle pipeline log chahiye"
"ab Terraform changes dekhunga"
"ab AKS status chahiye"
"evidence enough hai; stop"
```

then dynamic control appears and system becomes more agent-like.

But host still decides:

```text
which tools exist
which args allowed
max iterations
permissions
approval requirements
```

---

# PART 4 — Module 6 Connection

Module 6 chain:

```python
chain = prompt | model | parser
```

This is not automatically an agent.

LangChain orchestration can build:

```text
fixed chain
conditional workflow
tool-enabled agent
```

Framework name does not define architecture.

---

# PART 5 — Module 7 Connection

MCP server exposes capabilities:

```text
get_pipeline_status
get_terraform_changes
get_aks_status
```

MCP does not decide when they should be called.

That decision belongs to:

```text
host workflow
or
agent control loop
```

So:

```text
MCP = capability protocol
LangGraph = stateful control/orchestration
LLM = reasoning component
```

---

# PART 6 — Deterministic vs Dynamic Decision

Deterministic routing:

```python
if evidence_count < 3:
    return "collect_more_evidence"
return "analyze"
```

Dynamic/model-driven planning:

```text
Given current evidence and available tools,
which information should be collected next?
```

Production systems often combine both:

```text
LLM proposes
 ↓
Host validates
 ↓
Policy decides whether execution is allowed
```

---

# PART 7 — When NOT to Use an Agent

If process is known:

```text
validate → retrieve → summarize → return
```

agent may add unnecessary:

```text
latency
cost
nondeterminism
more failure states
harder testing
loop risk
security risk
```

Use simplest architecture that satisfies the problem.

---

# PART 8 — When Agent Behavior Helps

Agent behavior is useful when:

```text
next step depends on observations
multiple tools may be relevant
information gaps vary per incident
workflow may need to revisit earlier steps
human approval may pause execution
long-running state must be preserved
```

DevOps incident investigation fits this pattern well.

---

# PART 9 — DevOps Comparison

### Fixed Workflow

```text
Always call:
1. pipeline
2. terraform
3. AKS
4. generate RCA
```

### Agentic Workflow

```text
Pipeline says build failed before Terraform
        ↓
No need to query AKS networking
        ↓
Collect build evidence instead
```

Agent can potentially reduce unnecessary calls—but only if routing is reliable and bounded.

---

# PART 10 — Safety Boundary

Never interpret:

```text
agent can choose a tool
```

as:

```text
agent has authority to execute anything
```

Correct model:

```text
Model Proposal
     ↓
Tool Allowlist
     ↓
Argument Validation
     ↓
Authorization
     ↓
Approval Policy
     ↓
Execution
```

This directly reuses Module 1 and Module 7.

---

# PART 11 — Common Mistakes

- every chatbot ko agent bol dena
- fixed pipeline ko unnecessarily agent banana
- tool choice ko execution permission samajhna
- no termination condition
- model-generated state ko trusted state samajhna
- workflow failure ko LLM failure samajhna

---

# PART 12 — Interview Q&A

### Q1. What is the difference between a workflow and an agent?
A workflow follows application-defined paths, while an agent can dynamically influence its next steps or tool usage based on observations and goals.

### Q2. Are all LangGraph applications agents?
No. LangGraph can model deterministic workflows as well as dynamic agent systems.

### Q3. Why prefer workflows when possible?
They are generally easier to reason about, test, secure and operate.

### Q4. Who should enforce permissions in an agent?
The host application and trusted policy/identity systems, not the model.

---

# PART 13 — Revision

```text
Chain = sequential composition
Workflow = application-controlled process
Agent = dynamic decision-making inside bounded policy
MCP = standardized external capability layer
Graph = explicit state + transitions
```

---

# PART 14 — Homework

Classify these as chain, workflow or agent:

```text
1. Prompt → LLM → JSON parser
2. Retrieve → threshold → LLM or abstain
3. Model chooses among 8 investigation tools repeatedly
4. Human must approve remediation before execution
```

For each, explain who controls the next step.

---

# 🔁 Next Lesson Kyu?

Agent dynamic decisions leta hai. Ab question hai: **ye decisions aur progress safely store kahan honge?** Next lesson me stateful graphs aur LangGraph ka purpose samjhenge.
