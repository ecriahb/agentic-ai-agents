# 🚩 Jai Bajrangbali!

# Lesson 04 — Local AI with Ollama

> **Cloud billing ke bina bhi AI application, structured output, tool calling aur agent loop practice kar sakte hain.**

## 🎯 Learning Goal

Is lesson me hum practical progression follow karte hain:

```text
Local Model
   ↓
First AI Call
   ↓
Structured Output
   ↓
Tool Calling
   ↓
Multiple Tools
   ↓
Agent Loop
   ↓
DevOps Agent V1 → V4
```

Is lesson ke end tak aap samjhoge:

- Ollama kya hai
- local LLM kya hota hai
- `localhost:11434` ka meaning
- OpenAI-compatible local client kaise use hota hai
- simple text response se structured RCA tak ka evolution
- tool calling me LLM aur Python ki responsibility
- agent loop kya hota hai
- `devops_agent_v1.py` se `v4.py` tak humne kya improve kiya

---

## 1. Ollama Kya Hai?

**English Definition:**
> Ollama is a local model runtime that lets you download and run supported language models on your own computer and exposes an API for applications.

**Hinglish:**
Ollama hamare laptop par LLM run karata hai. Isse har learning experiment ke liye paid cloud API call zaroori nahi hoti.

```text
Cloud LLM
Model runs on provider infrastructure

Local Ollama
Model runs on your own laptop/workstation
```

---

## 2. Local LLM

**English Definition:**
> A local LLM is a language model executed on infrastructure controlled by the user instead of being invoked only through a hosted cloud API.

Advantages for learning:

- per-call cloud billing nahi
- localhost par experimentation
- API concepts practice kar sakte hain
- tool calling aur agent loops build kar sakte hain

Limitations:

- laptop RAM/CPU/GPU matter karta hai
- small model reasoning quality hosted large models se lower ho sakti hai
- model confident hoke wrong answer de sakta hai

---

## 3. Install / Verify

Windows terminal:

```powershell
ollama --version
ollama run gemma3:1b
```

Model test:

```text
Explain AKS in two simple lines.
```

Exit:

```text
/bye
```

---

## 4. `localhost:11434` Samjho

```text
http://localhost:11434
```

- `localhost` = current computer
- `11434` = Ollama API port

Mental model:

```text
Python Application
      ↓
localhost:11434
      ↓
Ollama Runtime
      ↓
gemma3:1b
      ↓
Response
```

---

## 5. OpenAI-Compatible Client with Ollama

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

### Why `api_key="ollama"`?

OpenAI SDK client key field expect karta hai. Local Ollama request localhost par route hoti hai; yeh learning client configuration ka placeholder value hai, cloud secret nahi.

---

## 6. First Important Hallucination Lesson

Ek run me small local model ne AKS ko wrong expansion diya tha.

Correct fact:

```text
AKS = Azure Kubernetes Service
EKS = Amazon Elastic Kubernetes Service
```

Lesson:

> **Fluent output correctness ki guarantee nahi hoti.**

Isi problem ki wajah se agent ko real environment evidence chahiye.

---

# PART 2 — Plain Text se Structured Output

## 7. Structured Output Kya Hai?

**English Definition:**
> Structured output is model output constrained to a predictable schema so that software can reliably consume and validate it.

Human-friendly text:

```text
Maybe the network rule caused the issue. You should check NSG and Terraform.
```

Application-friendly structured data:

```json
{
  "root_cause": "NSG rule removed",
  "impact": "AKS network connectivity degraded",
  "fix": "Restore required NSG rule",
  "severity": "critical"
}
```

Why useful:

```text
Free Text → Human reads
Structured Data → Program validates → Pipeline/UI/Database uses
```

Example file:

```text
examples/03_structured_output.py
```

### Pydantic Mental Model

```text
LLM Output
    ↓
Schema
    ↓
Validation
    ↓
Trusted Application Object
```

Schema hallucination ko completely eliminate nahi karta, but **format contract enforce** karta hai.

---

# PART 3 — Tool Calling

## 8. Tool Calling Kya Hai?

**English Definition:**
> Tool calling is a pattern where an LLM selects a predefined function and provides arguments, while the application executes the actual function.

Golden rule:

> **LLM decides; Python executes.**

```text
User Problem
    ↓
LLM decides: I need AKS status
    ↓
Tool Request
    ↓
Python executes get_aks_status()
    ↓
Real / simulated evidence returned
    ↓
LLM reasons over evidence
```

Example tool:

```python
def get_aks_status(cluster_name: str):
    ...
```

Important:

- model function ka description padhta hai
- model tool name + arguments choose karta hai
- Python actual function run karta hai
- tool result model ko wapas diya jata hai

Example file:

```text
examples/04_tool_call_basic.py
```

---

## 9. Fake Tool vs Real Tool Concept

Learning ke start me function hard-coded/fake data return kar sakta hai:

```python
def get_aks_status(cluster_name: str):
    return "Degraded - network connectivity failures detected"
```

Later wahi interface real Azure/Kubernetes command ko wrap kar sakta hai:

```text
Fake Tool
Hard-coded learning data
      ↓
Same Function Contract
      ↓
Real Tool
Azure SDK / az / kubectl / REST API
```

Detailed transition **Lesson 05** me karenge.

---

# PART 4 — Agent Loop

## 10. Agent Kya Hai?

**English Definition:**
> An AI agent is an application in which a model can reason about a goal, select tools, observe results, maintain state, and continue until it can produce a useful final outcome or must stop.

Simple chatbot:

```text
Prompt → LLM → Answer
```

Agent:

```text
Goal
 ↓
LLM Reasoning
 ↓
Choose Tool
 ↓
Execute Tool
 ↓
Observe Result
 ↓
Need More Evidence?
 ├── Yes → another tool
 └── No  → final answer
```

Important correction:

> Hum naya LLM train nahi kar rahe. Hum **existing LLM ko brain ke roop me use karke agent application bana rahe hain**.

---

# PART 5 — DevOps Agent V1 → V4

## 11. Tools Used in Our Practical

```python
get_aks_status(...)
get_terraform_changes(...)
get_pipeline_status(...)
```

Evidence eventually became:

```text
AKS:
Degraded - network connectivity failures detected

Pipeline:
Failed during Terraform Apply

Terraform:
NSG rule allowing AKS subnet traffic was removed
```

Ab model ko guess karne ki jagah evidence mila.

---

## 12. V1 — Basic Multi-Tool Agent

File:

```text
examples/devops_agent_v1.py
```

Purpose:

- tools define karna
- model ko available tools batana
- requested function execute karna
- result model ko wapas dena
- basic investigation loop banana

Mental model:

```text
Question
 ↓
LLM
 ↓
Tool Call
 ↓
Python Function
 ↓
Tool Result
 ↓
LLM
 ↓
Final RCA
```

---

## 13. V2 — Correct Arguments & Environment Mapping

File:

```text
examples/devops_agent_v2.py
```

V1 se improvement:

- environment vs cluster arguments clear kiye
- `prod-aks` aur `production` mapping issue fix kiya
- typed/controlled arguments use kiye
- evidence consistency improve ki

Why important?

Agar tool ko wrong identifier diya gaya, correct function bhi wrong/no result dega.

> **Agent quality = reasoning quality + tool contract quality + input quality.**

---

## 14. V3 — State, Duplicate Calls & Evidence Grounding

File:

```text
examples/devops_agent_v3.py
```

Improvements:

- collected evidence preserve kiya
- duplicate/repeated tool calls ko handle kiya
- final answer ko tool evidence se ground kiya
- agent ko unnecessary loop se bachaya

**State Definition:**
> State is the information an application preserves across steps so later decisions can use earlier observations.

```text
Step 1: Pipeline evidence
Step 2: Terraform evidence
Step 3: AKS evidence
         ↓
       STATE
         ↓
Final grounded RCA
```

---

## 15. V4 — Investigation Separate from RCA Reporting

File:

```text
examples/devops_agent_v4.py
```

V4 mental model:

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
Human Approval
```

Why better?

Investigation aur reporting alag responsibilities hain:

- agent evidence collect karta hai
- reporting layer evidence ko structured RCA me convert karti hai
- schema output format validate karta hai
- human destructive/remediation action se pehle approve kar sakta hai

---

## 16. Final RCA We Reached

Evidence-based result:

```text
Root Cause:
NSG rule allowing AKS subnet traffic was removed during Terraform changes.

Impact:
AKS network connectivity degraded and deployment failed.

Fix:
Restore the required NSG allow rule and validate related routes/NSG behavior before redeployment.

Severity:
High / Critical
```

Difference dekho:

```text
Before Tools
LLM guesses from prompt

After Tools
LLM reasons from application-provided evidence
```

---

## 17. Interview Corner

### Q1. What is Ollama?
> Ollama is a local model runtime that can run supported LLMs on a user's own machine and expose an API for applications.

### Q2. What is structured output?
> Structured output constrains model output to a predictable schema so software can validate and consume it reliably.

### Q3. What is tool calling?
> Tool calling lets a model choose a predefined function and arguments; the application performs the actual execution.

### Q4. Does the LLM execute Python functions itself?
> No. The model requests a tool call. The application executes the function and returns the result to the model.

### Q5. What is an agent loop?
> It is a repeated decide → act → observe cycle in which the model can call tools, inspect results and continue until it can produce a final outcome.

### Q6. Why preserve state?
> State keeps previously collected evidence available across multi-step reasoning and prevents the agent from losing investigation context.

---

## 🧠 Revision Sheet

```text
Ollama          = Local model runtime
localhost       = This computer
Structured Out  = Predictable validated format
Tool            = Function/API available to application
Tool Calling    = LLM chooses, Python executes
Agent Loop      = Decide → Act → Observe → Repeat
State           = Preserved evidence/context
Grounding       = Answer based on actual evidence
V1              = Basic multi-tool loop
V2              = Better arguments/mapping
V3              = State + duplicate handling + grounding
V4              = Investigation + structured RCA + validation
```

## Why the Next Lesson Follows

Ab hum fake/hard-coded DevOps tools ke saath complete agent behavior samajh chuke hain. Next step hai **same tool contract ko real DevOps system se connect karna**.

➡️ **Next: Lesson 05 — Fake Tool → Real Tool**
