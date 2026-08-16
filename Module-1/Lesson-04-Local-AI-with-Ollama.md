# 🚩 Jai Bajrangbali!

# Lesson 04 — Local AI with Ollama

> **Cloud billing ke bina bhi AI application, structured output, tool calling aur agent loop ko practically build kar sakte hain.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap clearly samjhoge:

- Ollama kya hai
- Local LLM kya hota hai
- Cloud model vs local model
- `localhost:11434` ka exact meaning
- OpenAI-compatible local client kaise kaam karta hai
- `api_key="ollama"` kyun diya jata hai
- First local AI call
- Hallucination ka real practical example
- Structured Output kya hai
- Pydantic/schema validation ka role
- Tool Calling kya hai
- LLM aur Python ki responsibilities
- Single tool se multiple tools tak progression
- Agent Loop kya hota hai
- State kya hota hai
- Grounding kya hoti hai
- `devops_agent_v1.py` se `v4.py` tak exact evolution
- Final RCA evidence-based kaise bana
- Common beginner confusions
- Interview-level explanation

---

# 🧠 Big Picture

```text
Cloud API Call
      ↓
Local Ollama Runtime
      ↓
First Local AI Call
      ↓
Hallucination Lesson
      ↓
Structured Output
      ↓
Tool Calling
      ↓
Multiple Tools
      ↓
Agent Loop
      ↓
State + Grounding
      ↓
DevOps Agent V1 → V4
      ↓
Evidence-Based RCA
```

---

# PART 1 — Ollama

## 1. Ollama Kya Hai?

**English Definition:**
> Ollama is a local model runtime that allows supported language models to run on a user's own machine and exposes an API that applications can call.

Simple Hinglish:

Ollama ek runtime hai jo model ko provider ke cloud ki jagah hamare laptop/workstation par run kar sakta hai.

Mental model:

```text
Cloud Model
Application → Internet/API → Provider Model

Local Ollama
Application → localhost API → Local Model
```

---

## 2. Local LLM Kya Hai?

**English Definition:**
> A local LLM is a language model executed on infrastructure controlled by the user rather than accessed only through a hosted cloud service.

Simple Hinglish:

Model hamare apne system par run ho raha hai.

Advantages for learning:

```text
No per-call cloud API billing
Local experimentation
Fast iteration
API concepts practice
Tool calling practice
Agent loop practice
```

Limitations:

```text
RAM/CPU/GPU limits
Small model quality limitations
Slower inference possible
Reasoning may be weaker
Hallucination still possible
```

Important:

> **Local model hone se hallucination automatically khatam nahi hoti.**

---

# PART 2 — Install and Run

## 3. Ollama Verify Karna

```powershell
ollama --version
```

Purpose:

```text
Ollama installed hai?
CLI accessible hai?
```

---

## 4. Model Run Karna

Example:

```powershell
ollama run gemma3:1b
```

Conceptually:

```text
ollama
= runtime

gemma3:1b
= model
```

First time model download ho sakta hai.

Then interactive prompt:

```text
Explain AKS in two simple lines.
```

Exit:

```text
/bye
```

---

# PART 3 — localhost

## 5. `localhost` Kya Hai?

**English Definition:**
> `localhost` is a hostname that refers to the current computer itself.

Simple Hinglish:

```text
localhost = mera current laptop/computer
```

Ollama API address conceptually:

```text
http://localhost:11434
```

Breakdown:

```text
http://
= protocol

localhost
= current machine

11434
= port where Ollama service listens
```

Mental model:

```text
Python Application
       ↓
localhost:11434
       ↓
Ollama Runtime
       ↓
Local Model
```

---

# PART 4 — OpenAI-Compatible Local Client

## 6. Local Client Code

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)

response = client.responses.create(
    model="gemma3:1b",
    input="Explain AKS in two simple lines."
)

print(response.output_text)
```

---

## 7. `base_url` Kya Kar Raha Hai?

Default cloud endpoint use karne ke instead:

```python
base_url="http://localhost:11434/v1/"
```

SDK ko batata hai:

```text
Request cloud provider ko nahi
Local Ollama API ko bhejo
```

Mental model:

```text
Same SDK-style code
      ↓
Different base URL
      ↓
Different backend
```

---

## 8. `api_key="ollama"` Kyun?

OpenAI SDK client initialization credential field expect kar sakta hai.

Local Ollama learning setup me:

```python
api_key="ollama"
```

placeholder-style value hoti hai.

Important:

```text
This is not your cloud secret key.
```

Request localhost par route ho rahi hai.

---

# PART 5 — First Local AI Call

## 9. Request Flow

```text
Python Script
      ↓
OpenAI-compatible SDK client
      ↓
localhost:11434
      ↓
Ollama
      ↓
gemma3:1b
      ↓
Response
```

This proves an important architecture principle:

> **Application pattern can remain similar even when the model provider/runtime changes.**

---

# PART 6 — Hallucination Practical

## 10. Real Learning Moment

Ek run me small local model ne AKS ka expansion wrong diya.

Correct:

```text
AKS = Azure Kubernetes Service
EKS = Amazon Elastic Kubernetes Service
```

### Why This Matters

Model fluent answer de sakta hai:

```text
Confident tone
Clean grammar
Technical wording
```

but still wrong.

> **Fluency is not evidence of correctness.**

---

## 11. DevOps Impact of Hallucination

Suppose agent guesses:

```text
"The issue is DNS."
```

without evidence.

Engineer wrong direction me troubleshoot kar sakta hai.

So later we add:

```text
Pipeline evidence
Terraform evidence
AKS evidence
```

Then model reasons from supplied evidence.

This is **grounding**.

---

# PART 7 — Structured Output

## 12. Structured Output Kya Hai?

**English Definition:**
> Structured output is model output constrained to a predictable schema so software can reliably validate and consume it.

Free text:

```text
The NSG may be the issue and you should probably restore the rule.
```

Structured output:

```json
{
  "root_cause": "NSG rule removed",
  "impact": "AKS connectivity degraded",
  "fix": "Restore required NSG rule",
  "severity": "critical"
}
```

Difference:

```text
Free Text
→ easy for humans
→ harder for software to parse reliably

Structured Output
→ predictable fields
→ easier for software
```

---

## 13. Why DevOps Needs Structured Output

Example downstream usage:

```text
LLM RCA
  ↓
Structured JSON/Object
  ↓
Incident UI
Database
Teams message
Approval workflow
Dashboard
```

Without structure, application ko brittle text parsing karna pad sakta hai.

---

# PART 8 — Schema and Validation

## 14. Schema Kya Hai?

**English Definition:**
> A schema defines the expected structure, fields, and data types of an output object.

Example expected RCA:

```text
root_cause: string
impact: string
fix: string
severity: enum/string
```

Mental model:

```text
LLM Output
   ↓
Schema
   ↓
Validation
   ↓
Application Object
```

---

## 15. Pydantic ka Role

Pydantic Python me typed data validation ke liye use hota hai.

Conceptual example:

```python
from pydantic import BaseModel

class RCA(BaseModel):
    root_cause: str
    impact: str
    fix: str
    severity: str
```

Important:

> Schema validates structure/type expectations; it does not automatically prove factual correctness.

So:

```text
Schema Validation
≠ Truth Validation
```

Truth ke liye real evidence chahiye.

Example file:

```text
examples/03_structured_output.py
```

---

# PART 9 — Tool Calling

## 16. Tool Calling Kya Hai?

**English Definition:**
> Tool calling is a pattern where an LLM selects a predefined function and provides arguments, while the application executes the actual function.

Golden rule:

> **LLM decides. Python executes.**

Flow:

```text
User asks:
"Why did deployment fail?"
       ↓
LLM decides:
"I need AKS status"
       ↓
Tool Request
       ↓
Python executes get_aks_status()
       ↓
Tool Result
       ↓
LLM receives evidence
```

---

## 17. Does LLM Execute Python Function?

No.

This is extremely important.

```text
LLM
= Chooses tool + arguments

Python/Application
= Executes actual function
```

The model may produce something conceptually like:

```text
Call get_aks_status with cluster_name="prod-aks"
```

Application dispatches that function.

---

# PART 10 — Tool Definition

## 18. Simple Tool Example

```python
def get_aks_status(cluster_name: str):
    return "Degraded - network connectivity failures detected"
```

At this stage it can be fake/hard-coded.

Tool purpose:

```text
Input:
cluster_name

Output:
AKS status evidence
```

Later Lesson 5 me same contract real Azure/Kubernetes source se connect hota hai.

---

# PART 11 — Single Tool Call

## 19. First Tool Flow

```text
Question
   ↓
LLM
   ↓
Tool request
   ↓
Python function
   ↓
Tool result
   ↓
LLM final answer
```

Example file:

```text
examples/04_tool_call_basic.py
```

This is a major jump from simple text generation because model now application capabilities choose kar raha hai.

---

# PART 12 — Multiple Tools

## 20. Why One Tool Was Not Enough

AKS deployment failure RCA ke liye sirf cluster status enough nahi.

We used:

```python
get_aks_status(...)
get_terraform_changes(...)
get_pipeline_status(...)
```

Each tool gives one part of reality.

Mental model:

```text
Pipeline Tool
= Where failure occurred

Terraform Tool
= What infra changed

AKS Tool
= Current cluster impact
```

Together:

```text
Evidence Correlation
```

---

# PART 13 — Agent

## 21. Agent Kya Hai?

**English Definition:**
> An AI agent is an application in which a model can reason about a goal, select tools, observe tool results, maintain state, and continue until it can produce a useful outcome or reaches a stopping condition.

Chatbot:

```text
Prompt → Model → Answer
```

Agent:

```text
Goal
 ↓
Model decides
 ↓
Tool
 ↓
Observation
 ↓
Model decides again
 ↓
More tool or final answer
```

---

# PART 14 — Agent Loop

## 22. Agent Loop Kya Hai?

**English Definition:**
> An agent loop is the repeated decide → act → observe cycle that allows an agent to perform multi-step work.

Mental model:

```text
DECIDE
 ↓
ACT
 ↓
OBSERVE
 ↓
DECIDE AGAIN
```

Example:

```text
1. Check pipeline
2. Observe Terraform Apply failed
3. Check Terraform changes
4. Observe NSG rule removed
5. Check AKS health
6. Observe network degraded
7. Enough evidence → RCA
```

---

# PART 15 — We Are Not Training an Agent Model

## 23. Important Clarification

Question:

> "Hum agent bana rahe hain ya bana hua agent use kar rahe hain?"

Correct mental model:

```text
Existing LLM
   ↓
We build application logic around it
   ↓
Tools + state + loop + rules
   ↓
Agent Application
```

We are not training a new LLM.

> **Agent is an application architecture around an existing model.**

---

# PART 16 — State

## 24. State Kya Hai?

**English Definition:**
> State is information preserved by the application across multiple steps so later decisions can use earlier observations.

Without state:

```text
Tool 1 result
→ forgotten
Tool 2 result
→ isolated
```

With state:

```text
Pipeline evidence
Terraform evidence
AKS evidence
      ↓
Preserved together
      ↓
Final reasoning
```

Example:

```python
evidence = {
    "pipeline": "Failed during Terraform Apply",
    "terraform": "AKS NSG rule removed",
    "aks": "Network connectivity degraded"
}
```

---

# PART 17 — Grounding

## 25. Grounding Kya Hai?

**English Definition:**
> Grounding means basing a model's answer on supplied authoritative evidence rather than relying only on internal model knowledge or speculation.

Without grounding:

```text
Maybe DNS
Maybe NSG
Maybe UDR
Maybe identity
```

With grounding:

```text
Pipeline: Terraform Apply failed
Terraform: NSG rule removed
AKS: network degraded
```

Now RCA is evidence-based.

---

# PART 18 — DevOps Agent V1

## 26. V1 — Basic Multi-Tool Agent Loop

File:

```text
examples/devops_agent_v1.py
```

Goal:

```text
Allow model to request multiple DevOps tools
```

Flow:

```text
Question
 ↓
LLM
 ↓
Tool Call
 ↓
Python Executes
 ↓
Tool Result
 ↓
LLM
 ↓
Maybe Another Tool
 ↓
Final Answer
```

What V1 taught:

```text
Tool definitions
Tool dispatch
Tool result return
Basic loop
```

---

# PART 19 — DevOps Agent V2

## 27. V2 — Correct Arguments and Mapping

File:

```text
examples/devops_agent_v2.py
```

Problem observed:

```text
get_aks_status(prod-aks)
→ worked

get_pipeline_status(prod-aks)
→ Environment not found

get_terraform_changes(prod-aks)
→ No Terraform information found
```

Why?

Because tools expected different identifiers.

```text
AKS tool expects cluster name
→ prod-aks

Pipeline/Terraform tools expect environment
→ production
```

### Lesson

> **Correct tool + wrong argument = wrong/no evidence.**

V2 improved:

```text
Typed arguments
Correct environment mapping
Consistent tool input design
```

---

# PART 20 — Tool Contract Quality

## 28. Tool Description Matters

Model chooses tools based on their exposed name, description and argument schema.

Poor contract:

```text
get_status(name)
```

Ambiguous.

Better:

```text
get_aks_status(cluster_name)
get_pipeline_status(environment)
get_terraform_changes(environment)
```

Clear contract improves tool selection.

Important formula:

```text
Agent Quality
=
Model Reasoning
+
Tool Contract Quality
+
Input Quality
+
Evidence Quality
```

---

# PART 21 — DevOps Agent V3

## 29. V3 — State + Duplicate Call Handling + Grounding

File:

```text
examples/devops_agent_v3.py
```

Problems V3 addresses:

```text
Repeated tool calls
Evidence loss
Unnecessary loop
Weak grounding
```

Improvements:

```text
Preserve evidence
Track already-called tools
Avoid unnecessary duplicates
Use accumulated evidence for final answer
```

Mental model:

```text
Tool 1 Result ┐
Tool 2 Result ├→ STATE → Final Grounded RCA
Tool 3 Result ┘
```

---

# PART 22 — Duplicate Tool Calls

## 30. Why Duplicate Calls Matter

Suppose model repeatedly requests:

```text
get_aks_status(prod-aks)
get_aks_status(prod-aks)
get_aks_status(prod-aks)
```

Problems:

```text
Waste
Latency
Possible cost
Loop risk
No new evidence
```

Application can track:

```text
Tool + arguments already executed?
```

If yes, existing evidence reuse or controlled response possible.

---

# PART 23 — DevOps Agent V4

## 31. V4 — Investigation Separate from RCA Reporting

File:

```text
examples/devops_agent_v4.py
```

V4 architecture:

```text
Investigation Agent
      ↓
Collect Evidence
      ↓
Application Evidence State
      ↓
Structured RCA Generator
      ↓
Schema Validation
      ↓
Human Review
```

Why is this better?

Because two responsibilities are different:

```text
Investigation
= Find relevant evidence

Reporting
= Convert evidence into predictable RCA format
```

Separation gives cleaner design.

---

# PART 24 — Evidence We Reached

## 32. Final Practical Evidence

```text
Pipeline:
Failed during Terraform Apply

Terraform:
NSG rule allowing AKS subnet traffic was removed

AKS:
Degraded - network connectivity failures detected
```

Now correlation:

```text
Terraform apply failed
      +
AKS subnet rule removed
      +
AKS network degraded
      ↓
Strong evidence for NSG-related network issue
```

---

# PART 25 — Final RCA

## 33. Evidence-Based RCA

```text
Root Cause:
A Terraform change removed an NSG rule required for AKS subnet traffic.

Impact:
AKS network connectivity degraded and deployment failed.

Fix:
Restore the required NSG allow rule and validate related network configuration before redeployment.

Severity:
High / Critical
```

Difference:

```text
Before Tools
= Model guesses

After Tools
= Model reasons from supplied evidence
```

---

# PART 26 — Structured Output vs Grounding

## 34. Do Not Mix These Concepts

```text
Structured Output
= Answer format predictable hai

Grounding
= Answer evidence-based hai
```

Possible situation:

```text
Perfect JSON
but wrong facts
```

So production quality needs both:

```text
Real Evidence
      ↓
Grounded Reasoning
      ↓
Structured Output
      ↓
Validation
```

---

# PART 27 — Common Beginner Confusions

## Confusion 1

> Local model means no API.

Wrong.

Ollama local API expose kar sakta hai.

## Confusion 2

> Tool calling means LLM executes Python.

Wrong.

```text
LLM chooses
Application executes
```

## Confusion 3

> Structured output eliminates hallucination.

Wrong.

It improves format reliability, not factual truth by itself.

## Confusion 4

> More tools automatically means better agent.

No.

Tool quality, clear contracts and relevant evidence matter.

## Confusion 5

> Agent is a newly trained model.

No.

Agent is application logic around an existing model.

## Confusion 6

> State and context are exactly the same.

Not necessarily.

State is application-preserved workflow information; model context is what is actually supplied to the model for a specific turn/request.

---

# PART 28 — Interview Corner

### Q1. What is Ollama?
> Ollama is a local model runtime that can run supported language models on a user's machine and expose an API for applications.

### Q2. What is a local LLM?
> A local LLM is a language model executed on user-controlled infrastructure rather than accessed only through a hosted cloud service.

### Q3. What does `localhost` mean?
> It refers to the current computer on which the application is running.

### Q4. What is structured output?
> Structured output constrains model output to a predictable schema that software can validate and consume reliably.

### Q5. Does schema validation guarantee factual correctness?
> No. It validates structure and types; factual correctness still requires reliable evidence and grounding.

### Q6. What is tool calling?
> Tool calling allows a model to select a predefined function and provide arguments while the application performs the actual execution.

### Q7. Does the LLM execute the Python function?
> No. The application executes the function and returns the result to the model.

### Q8. What is an agent loop?
> It is the repeated decide → act → observe cycle used for multi-step work.

### Q9. What is state?
> State is information preserved by the application across steps so later decisions can use earlier observations.

### Q10. What is grounding?
> Grounding means basing the model's answer on supplied authoritative evidence rather than unsupported speculation.

### Q11. What improved in DevOps Agent V2?
> V2 improved argument typing and environment/cluster mapping so tools received the correct identifiers.

### Q12. What improved in V3?
> V3 added evidence state, duplicate-call handling, and stronger grounding of the final answer.

### Q13. What improved in V4?
> V4 separated evidence collection from structured RCA generation and validation.

### Q14. Are we training a new LLM in this module?
> No. We are building an agent application around an existing model using tools, state, schemas, and control logic.

---

# 🧠 Revision Sheet

```text
Ollama
= Local model runtime

Local LLM
= Model running on user-controlled machine

localhost
= Current computer

base_url
= Where SDK sends API requests

Structured Output
= Predictable output schema

Schema Validation
= Format/type validation

Tool Calling
= LLM chooses tool; application executes

Agent Loop
= Decide → Act → Observe → Repeat

State
= Preserved workflow evidence/context

Grounding
= Reason from supplied evidence

V1
= Basic multi-tool loop

V2
= Better arguments + mapping

V3
= State + duplicate handling + grounding

V4
= Investigation separated from structured RCA reporting
```

---

# 🔗 Why the Next Lesson Follows

Ab tak tools fake/hard-coded evidence return kar rahe the.

Next logical step:

```text
Same Agent Logic
      ↓
Same Tool Contracts
      ↓
Real Azure / AKS / Terraform / Pipeline Sources
```

➡️ **Next: Lesson 05 — Fake Tool → Real Tool**
