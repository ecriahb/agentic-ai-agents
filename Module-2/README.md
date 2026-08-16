# 🚩 Jai Bajrangbali!

# Module 2 — Prompt Engineering for DevOps & Agentic AI

> **From “asking AI a question” → designing reliable instructions for DevOps workflows.**

Module 1 me humne LLM APIs, local models, tool calling, real evidence aur trusted RCA flow build kiya. Module 2 me focus hai: **LLM ko exactly kaise instruct karein so that output predictable, grounded, structured aur reusable ho.**

---

## 🎯 Module 2 Learning Promise

Module ke end tak aap samjhoge:

- prompt engineering fundamentals
- Role + Context + Task + Constraints + Output framework
- system prompt vs user prompt
- zero-shot, one-shot, few-shot prompting
- structured DevOps prompts
- hallucination reduction
- context engineering for logs, Terraform and AKS
- prompt chaining
- agent loop prompts and guardrails
- prompt evaluation
- reusable prompt templates
- complete DevOps Incident Analysis Prompt System

---

## 🧠 Core Mental Model

```text
Raw User Request
      ↓
Clear Role
      ↓
Relevant Context / Evidence
      ↓
Specific Task
      ↓
Constraints / Guardrails
      ↓
Output Contract
      ↓
Evaluation
      ↓
Reliable Prompt System
```

> Prompt engineering is not “magic wording”. It is **instruction design + context design + output design + validation**.

---

# 📚 Planned Lesson Sequence

| Lesson | Topic | Main Outcome |
|---|---|---|
| 01 | [Prompt Engineering Basics](Lesson-01-Prompt-Engineering-Basics.md) | Prompt anatomy and specificity |
| 02 | [Role + Context + Task + Constraints + Output](Lesson-02-Role-Context-Task-Constraints-Output.md) | Build a repeatable prompt framework |
| 03 | [System Prompt vs User Prompt](Lesson-03-System-Prompt-vs-User-Prompt.md) | Separate permanent rules from runtime requests |
| 04 | [Zero-shot / One-shot / Few-shot](Lesson-04-Zero-One-Few-Shot.md) | Choose examples strategically |
| 05 | [Structured DevOps Prompts](Lesson-05-Structured-DevOps-Prompts.md) | RCA, change review and deployment prompts |
| 06 | [Hallucination Reduction Techniques](Lesson-06-Hallucination-Reduction.md) | Evidence-first and abstention rules |
| 07 | [Context Engineering for Logs / Terraform / AKS](Lesson-07-Context-Engineering.md) | Feed only useful operational evidence |
| 08 | [Prompt Chaining](Lesson-08-Prompt-Chaining.md) | Split complex investigation into stages |
| 09 | [Agent Loop Prompts & Guardrails](Lesson-09-Agent-Loop-Prompts-and-Guardrails.md) | Control tool use and stopping rules |
| 10 | [Prompt Evaluation](Lesson-10-Prompt-Evaluation.md) | Test reliability instead of trusting one output |
| 11 | [Reusable Prompt Templates](Lesson-11-Reusable-Prompt-Templates.md) | Create production-ready prompt assets |
| 12 | [Mini Project — DevOps Incident Analysis Prompt System](Lesson-12-Mini-Project-DevOps-Incident-Prompt-System.md) | Combine everything into one system |

---

# 🧪 Practical Examples

Copy-paste examples are kept in [`examples/`](examples/README.md).

Key files:

- [`incident_rca_prompt.txt`](examples/incident_rca_prompt.txt)
- [`terraform_change_review_prompt.txt`](examples/terraform_change_review_prompt.txt)
- [`aks_troubleshooting_prompt.txt`](examples/aks_troubleshooting_prompt.txt)
- [`prompt_playground.py`](examples/prompt_playground.py)

---

# 🔁 Why Module 2 Comes After Module 1

```text
Module 1
LLM + API + Tools + Evidence
        ↓
Problem discovered:
The model can still misunderstand instructions,
overclaim, hallucinate, or produce inconsistent output.
        ↓
Module 2
Prompt + Context + Constraints + Evaluation
```

Module 1 ne hume **AI application mechanics** sikhaya. Module 2 hume **AI behavior ko systematically guide aur test karna** sikhata hai.

---

# ✅ Final Outcome

Module 2 complete hone ke baad aap ek DevOps problem ko sirf “AI se puchoge” nahi. Aap:

```text
Evidence select karoge
→ prompt contract define karoge
→ model behavior constrain karoge
→ output structure fix karoge
→ hallucination controls lagaaoge
→ result evaluate karoge
→ reusable prompt system banaoge
```
