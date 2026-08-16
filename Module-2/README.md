# 🚩 Jai Bajrangbali!

# Module 2 — Prompt & Context Engineering for DevOps AI

> **From “asking AI a question” → designing reliable, evidence-grounded and testable instruction systems.**

Module 1 me humne LLM APIs, local models, tool calling, real evidence aur trusted RCA flow build kiya. Module 2 ka focus hai: **model ko exactly kaise instruct karein, kaunsa context dein, kya unknown rehne dein, aur behavior ko systematically evaluate kaise karein.**

---

# 🎯 Module 2 Learning Promise

Module ke end tak aap samjhoge:

- prompt engineering fundamentals
- Role + Context + Task + Constraints + Output framework
- system prompt vs user prompt vs evidence context
- zero-shot / one-shot / few-shot prompting
- structured RCA, Terraform review and AKS troubleshooting prompts
- hallucination reduction and explicit abstention
- context engineering for logs/Terraform/AKS
- prompt chaining and intermediate validation
- agent-loop prompts, tool proposals and stop conditions
- prompt evaluation and regression datasets
- reusable/versioned prompt templates
- provider-independent prompt design
- same prompt ko Ollama aur OpenAI dono par compare karna
- final DevOps Incident Analysis Prompt System

---

# 🧠 Core Mental Model

```text
ROLE
  +
CONTEXT / EVIDENCE
  +
TASK
  +
CONSTRAINTS
  +
OUTPUT CONTRACT
  +
ABSTENTION
  +
EVALUATION
  =
Reliable Prompt System
```

Important:

```text
Prompt guides.
Evidence grounds.
Host validates.
Policy controls.
```

---

# 📚 Detailed Lesson Sequence

| Lesson | Topic | Main Outcome |
|---|---|---|
| 01 | [Prompt Engineering Basics](Lesson-01-Prompt-Engineering-Basics.md) | Understand prompt anatomy, specificity and provider-independent prompt behavior |
| 02 | [Role + Context + Task + Constraints + Output](Lesson-02-Role-Context-Task-Constraints-Output.md) | Build a repeatable instruction contract |
| 03 | [System Prompt vs User Prompt](Lesson-03-System-Prompt-vs-User-Prompt.md) | Separate stable policy, runtime task and evidence context |
| 04 | [Zero-shot / One-shot / Few-shot](Lesson-04-Zero-One-Few-Shot.md) | Use examples without confusing them with current evidence |
| 05 | [Structured DevOps Prompts](Lesson-05-Structured-DevOps-Prompts.md) | Design RCA, Terraform review and AKS troubleshooting prompts |
| 06 | [Hallucination Reduction & Abstention](Lesson-06-Hallucination-Reduction.md) | Use evidence boundaries, unknown states and validation |
| 07 | [Context Engineering](Lesson-07-Context-Engineering.md) | Select, normalize, label, redact and budget operational evidence |
| 08 | [Prompt Chaining](Lesson-08-Prompt-Chaining.md) | Split complex tasks into validated stages |
| 09 | [Agent Loop Prompts & Guardrails](Lesson-09-Agent-Loop-Prompts-and-Guardrails.md) | Keep planning flexible while execution remains host-controlled |
| 10 | [Prompt Evaluation](Lesson-10-Prompt-Evaluation.md) | Build labelled tests, metrics and regression checks |
| 11 | [Reusable Prompt Templates](Lesson-11-Reusable-Prompt-Templates.md) | Version prompt assets and validate runtime variables |
| 12 | [Mini Project — DevOps Incident Analysis Prompt System](Lesson-12-Mini-Project-DevOps-Incident-Prompt-System.md) | Combine prompt, context, abstention, provider parity and evals |

Every lesson now includes beginner explanation, English definitions, DevOps examples, mental models, common mistakes, production notes, interview Q&A, revision, homework and a next-topic bridge.

---

# 🧪 Practical Examples

Open: [`examples/README.md`](examples/README.md)

Key files:

- [`incident_rca_prompt.txt`](examples/incident_rca_prompt.txt) — grounded RCA template
- [`terraform_change_review_prompt.txt`](examples/terraform_change_review_prompt.txt) — production change-risk review
- [`aks_troubleshooting_prompt.txt`](examples/aks_troubleshooting_prompt.txt) — layered AKS troubleshooting
- [`prompt_playground.py`](examples/prompt_playground.py) — simple Ollama/local prompt runner
- [`dual_provider_prompt_playground.py`](examples/dual_provider_prompt_playground.py) — same grounded prompt on Ollama **or** OpenAI

---

# 🤖 Local LLM and OpenAI Path

## Local / Ollama

```powershell
ollama pull qwen3:4b
$env:LLM_PROVIDER="ollama"
python Module-2/examples/dual_provider_prompt_playground.py
```

## OpenAI

Install shared provider dependencies:

```powershell
pip install -r shared/requirements.txt
```

Then:

```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="your-key"
$env:OPENAI_MODEL="gpt-5.6-luna"
python Module-2/examples/dual_provider_prompt_playground.py
```

Compare engineering properties rather than exact wording:

```text
groundedness
abstention
format adherence
unsupported claims
impact hallucination
latency
```

See root [`MODEL-PROVIDERS.md`](../MODEL-PROVIDERS.md).

---

# 🔗 Module 1 Connection

```text
Module 1
LLM + API + Tools + Evidence
        ↓
Problem discovered:
The model can still misunderstand instructions,
overclaim, hallucinate or produce inconsistent output.
        ↓
Module 2
Prompt + Context + Constraints + Evaluation
```

Module 1 ne AI application mechanics sikhaya.
Module 2 AI behavior ko systematically guide aur test karna sikhata hai.

---

# 🛡️ Important Trust Rules

```text
System prompt != authorization
User assertion != trusted evidence
Few-shot example != current evidence
RAG/reference document != current incident proof
Structured output != truth
Model confidence != objective confidence
No evidence → no forced RCA
```

Prompt guardrails always sit alongside application controls:

```text
Tool allowlist
Argument validation
RBAC
Policy
Human approval
Audit / Evals
```

---

# ✅ Module 2 Completion Checklist

You should be able to:

- [ ] rewrite a vague prompt into a structured contract
- [ ] separate system/user/context responsibilities
- [ ] design useful few-shot examples without anchoring current facts
- [ ] write RCA/change-review/troubleshooting prompts
- [ ] add explicit `INSUFFICIENT_EVIDENCE` behavior
- [ ] normalize and source-label context
- [ ] design a prompt chain with validation between stages
- [ ] define agent-loop stop conditions
- [ ] create a labelled prompt eval dataset
- [ ] version reusable prompt templates
- [ ] run the same prompt on Ollama and OpenAI
- [ ] explain why provider output still needs host validation

---

# ➡️ What Comes Next?

Module 2 designs reliable instructions and context contracts.

Module 3 moves to the application plumbing needed to operationalize them:

```text
HTTP
REST
JSON
Environment Variables
Authentication
Errors
LLM APIs
```

🚩 **Module 2 outcome: prompt writing → prompt-system engineering.**
