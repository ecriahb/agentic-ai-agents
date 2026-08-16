# 🚩 Jai Bajrangbali!

# Lesson 14 — Grand Revision + Mini Project

> **AI Engineer = Model + Context + Tools + Guardrails + Human Judgment**

## Why This Final Lesson?

Individual definitions yaad hona enough nahi. Architect ko concepts ko ek system flow me connect karna chahiye.

Module 0 ka purpose tha:

```text
“AI kya hai?”
        ↓
“LLM kaise behave karta hai?”
        ↓
“Useful context kaise dena hai?”
        ↓
“Wrong output ka risk kya hai?”
        ↓
“Prompt kaise control karna hai?”
        ↓
“Safe enterprise system kaise design karna hai?”
```

Ab sab pieces ko ek architecture me connect karte hain.

# Part 1 — Module 0 Grand Revision

## 1. AI Revolution

```text
Internet → Cloud → DevOps → AI
```

AI existing automation ke upar intelligence/decision-support layer add kar sakta hai.

## 2. AI → ML → DL → LLM

```text
AI
└── Machine Learning
    └── Deep Learning
        └── Large Language Models
```

LLM AI ka ek specialized branch hai — AI ka synonym nahi.

## 3. Next Token Prediction

```text
Context
   ↓
Next-token probabilities
   ↓
Token generated
   ↓
Repeat
```

LLM fixed answer database nahi hai.

## 4. Transformer + Attention

```text
Tokens
  ↓
Relationships across context
  ↓
Attention-weighted representations
  ↓
Useful language generation
```

## 5. Context Window

Model current request me finite amount of tokenized information consider karta hai.

Golden rule:

> **Right context > More context.**

## 6. Hallucination

Fluent/confident output unsupported ya wrong ho sakta hai.

```text
Confidence ≠ Correctness
```

## 7. Prompt Engineering

```text
ROLE
+
TASK
+
CONTEXT
+
CONSTRAINTS
+
OUTPUT FORMAT
```

Prompt guides behavior; evidence grounds facts.

## 8. System vs User Prompt

```text
System/Application Rules = How to behave
User Request             = What to do now
```

## 9. Temperature

Controls generation diversity/randomness — not truth or intelligence.

## 10. Role Prompting

Role changes perspective/focus, not underlying model knowledge.

## 11. Zero / One / Few-Shot

Examples demonstrate desired format, style or decision pattern in current context.

## 12. Structured Investigation

```text
Identify → Collect → Analyze → Correlate → Verify → Conclude
```

## 13. Safety

```text
Ground
  ↓
Validate
  ↓
Authorize
  ↓
Human Approval
  ↓
Action
```

# Part 2 — One-Page Cheat Sheet

| Concept | Remember |
|---|---|
| AI → ML → DL → LLM | Technology hierarchy |
| Next Token Prediction | How LLM text is generated |
| Transformer + Attention | Models context relationships |
| Context Window | Finite working context |
| Hallucination | Plausible/confident wrong output |
| Prompt Formula | Role + Task + Context + Constraints + Output |
| System Instructions | Reusable behavior and rules |
| Temperature | Generation randomness/diversity |
| Role Prompting | Response perspective |
| Few-Shot | Examples guide pattern |
| Structured Investigation | Evidence-driven workflow |
| Safety | Ground + validate + least privilege + approval |

# Part 3 — Mini Project: Pipeline Failure Investigation Agent

## Client Requirement

> “We need an AI assistant that investigates CI/CD and AKS deployment failures, generates an evidence-backed RCA, recommends a fix, and keeps an engineer in the approval loop.”

## High-Level Architecture

```text
                 PIPELINE FAILURE
                        ↓
              ┌───────────────────┐
              │ Incident Request  │
              └─────────┬─────────┘
                        ↓
                 Investigation Agent
                        ↓
       ┌────────────────┼────────────────┐
       ↓                ↓                ↓
 Pipeline Logs     Terraform Diff     AKS Evidence
       ↓                ↓                ↓
       └────────────────┼────────────────┘
                        ↓
                Azure Monitor / Metrics
                        ↓
                  Trusted Evidence
                        ↓
                       LLM
                        ↓
                Structured RCA
                        ↓
              Recommended Remediation
                        ↓
                  Policy Validation
                        ↓
                 👨‍💻 Human Approval
                        ↓
                    Safe Action
```

## Inputs

Agent may eventually collect:

- GitHub Actions / Azure DevOps pipeline logs
- Terraform plan/apply output
- recent infrastructure changes
- AKS events
- pod/container logs
- node/cluster status
- Azure Monitor metrics
- Application Insights signals
- last successful deployment
- incident metadata

## Example Incident

```text
Environment: production
AKS Cluster: prod-aks

Pipeline Result:
Failed during Terraform Apply

Terraform Change:
NSG rule allowing AKS subnet traffic was removed.

AKS Status:
Degraded - network connectivity failures detected.
```

## Correct Evidence-Based Output

```text
Evidence:
- Production pipeline failed during Terraform Apply.
- An NSG rule allowing AKS subnet traffic was removed.
- prod-aks is degraded with network connectivity failures.

Likely Root Cause:
- Available evidence strongly suggests the removed NSG rule disrupted required AKS network connectivity.

Confirmed Impact:
- Production deployment failed.
- prod-aks is degraded.

Recommended Fix:
- Review and restore the required NSG rule.
- Validate AKS network connectivity.
- Retry deployment after verification.
```

Notice what we **did not** claim without evidence:

```text
❌ Customer outage
❌ Data loss
❌ Revenue impact
❌ Security compromise
```

# Part 4 — Guardrails for the Mini Project

```text
No secret leakage
No destructive action by default
Read-only investigation first
Tool allowlist
Tool argument validation
Evidence log / audit trail
Structured RCA output
No unsupported impact claims
Human approval before high-risk change
```

# Part 5 — How Every Module 0 Concept Fits the Project

### Next Token Prediction
Explains why LLM output is probabilistic.

### Transformer + Attention
Explains why relevant context relationships matter.

### Context Window
Forces us to select useful logs instead of dumping everything.

### Hallucination
Forces evidence validation.

### Prompt Engineering
Defines task, constraints and expected RCA format.

### System Instructions
Defines reusable agent behavior and safety policies.

### Temperature
Helps tune generation consistency where supported.

### Role Prompting
Can give the model a DevOps/SRE review lens.

### Few-Shot Examples
Can demonstrate company-approved RCA style.

### Structured Investigation
Defines what evidence to collect and in what logical stages.

### Safety
Controls permissions, tool execution and human approval.

# 🎯 Interview Corner

### Q. How would you design an AI-based DevOps RCA assistant?

**Answer:**
> I would collect trusted operational signals such as pipeline logs, infrastructure changes, Kubernetes events and monitoring data; provide only relevant evidence to the language model; use a structured investigation workflow and structured RCA output; validate tool arguments and model output; enforce least privilege and tool allowlists; and require human approval before any high-impact remediation.

### Q. What is the most important lesson from Module 0?

**Answer:**
> An enterprise AI system is not just an LLM. Reliable systems combine a model with trusted context, tools, validation, guardrails, application logic, and human judgment.

# 🧠 Final Golden Rules

> **LLM is the brain, not the whole system.**

> **Prompt guides behavior; context provides information; evidence supports truth.**

> **Schema validates structure. Evidence validates facts. Business rules validate decisions.**

> **Model output is not authorization.**

> **Human approval stays before destructive production action.**

# 📝 Final Homework / Architect Task

Draw your own architecture with these sections:

```text
INPUTS
  ↓
TOOLS
  ↓
EVIDENCE / STATE
  ↓
LLM / ANALYSIS
  ↓
STRUCTURED OUTPUT
  ↓
VALIDATION
  ↓
HUMAN APPROVAL
  ↓
ACTION
```

Then answer:

1. Which tools should be read-only?
2. Which actions need approval?
3. Where will secrets be stored?
4. How will tool calls be audited?
5. How will you stop unsupported RCA claims?

# 🚀 Why Module 1 Follows

Module 0 answered:

> **“AI works and behaves how?”**

Module 1 asks:

> **“Ab AI ko code/application ke andar kaise use karein?”**

Next journey:

```text
ChatGPT UI vs API
      ↓
Local / Cloud Model Setup
      ↓
First API Call
      ↓
Response + Tokens
      ↓
Structured Output
      ↓
Tool Calling
      ↓
Agent Loop
      ↓
First Working DevOps AI Agent
```

🚩 **Module 0 Complete — Jai Bajrangbali!**
