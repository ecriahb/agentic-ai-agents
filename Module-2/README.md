# 🚩 Module 2 — Prompt & Context Engineering for DevOps AI

> **The single canonical home for deep prompt and context engineering.**

Module 1 built the controlled application. Module 2 teaches how to make its reasoning behavior reliable, evidence-grounded and testable.

## 🎯 Learning Promise

By the end you can:

- design structured prompts
- separate instructions from evidence
- use zero/one/few-shot correctly
- build DevOps RCA/change-review/troubleshooting prompts
- reduce hallucination through evidence boundaries and abstention
- engineer logs/Terraform/AKS context
- build prompt chains
- design agent-loop prompts and guardrails
- version prompt templates
- evaluate prompts with regression data

## 🧠 Core Mental Model

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
Prompt System
```

```text
Prompt guides.
Evidence grounds.
Host validates.
Policy controls.
```

## 🧭 Canonical Lesson Sequence

| Lesson | Topic | Main Outcome |
|---|---|---|
| 01 | [Prompt Engineering Basics](Lesson-01-Prompt-Engineering-Basics.md) | Prompt anatomy and specificity |
| 02 | [Role + Context + Task + Constraints + Output](Lesson-02-Role-Context-Task-Constraints-Output.md) | Instruction contract |
| 03 | [System vs User + Evidence Context](Lesson-03-System-Prompt-vs-User-Prompt.md) | Instruction/data separation |
| 04 | [Zero / One / Few-shot](Lesson-04-Zero-One-Few-Shot.md) | Example-driven behavior |
| 05 | [Structured DevOps Prompts](Lesson-05-Structured-DevOps-Prompts.md) | RCA/change-review/AKS prompts |
| 06 | [Hallucination Reduction + Abstention](Lesson-06-Hallucination-Reduction.md) | Grounded reasoning boundaries |
| 07 | [Context Engineering](Lesson-07-Context-Engineering.md) | Normalize, redact, label, prioritize and budget evidence |
| 08 | [Prompt Chaining](Lesson-08-Prompt-Chaining.md) | Multi-stage prompts with intermediate validation |
| 09 | [Agent Loop Prompts + Guardrails](Lesson-09-Agent-Loop-Prompts-and-Guardrails.md) | Bounded model planning |
| 10 | [Prompt Evaluation](Lesson-10-Prompt-Evaluation.md) | Regression datasets and metrics |
| 11 | [Reusable / Versioned Prompt Templates](Lesson-11-Reusable-Prompt-Templates.md) | Prompt assets as versioned software |
| 12 | [Mini Project — Incident Analysis Prompt System](Lesson-12-Mini-Project-DevOps-Incident-Prompt-System.md) | Full prompt/context/eval system |

These 12 lessons remain because they each introduce a distinct prompt-engineering capability. The repetition is removed by making this the **only module that teaches these concepts deeply**.

## 🧪 Practical Examples

Open: [`examples/README.md`](examples/README.md)

```text
incident RCA prompt
Terraform change-review prompt
AKS troubleshooting prompt
local prompt playground
dual-provider prompt playground
```

## 🔗 Module Boundaries

### Module 0 → Module 2

Module 0 gives only the beginner mental model of prompting. It no longer treats Role Prompting, Temperature and Few-shot as separate mandatory chapters.

### Module 1 → Module 2

Module 1 uses prompts to build the first agent. Module 2 now owns the **deep engineering** of those prompts.

### Module 3 → Module 2

Module 3 teaches API plumbing. It should not reteach prompt engineering.

## 🛡️ Trust Rules

```text
System prompt != authorization
User assertion != trusted evidence
Few-shot example != current evidence
RAG/reference != current incident proof
Structured output != truth
Model confidence != objective confidence
No evidence → no forced RCA
```

## ✅ Completion Checklist

- [ ] rewrite a vague prompt into a structured contract
- [ ] separate instructions from evidence
- [ ] design safe few-shot examples
- [ ] build RCA/change-review/troubleshooting prompts
- [ ] add `INSUFFICIENT_EVIDENCE` behavior
- [ ] normalize/source-label/budget context
- [ ] design validated prompt chains
- [ ] define agent-loop stop conditions
- [ ] build a prompt regression dataset
- [ ] version prompt templates
- [ ] compare the same prompt across providers

> **Outcome:** prompt writing becomes prompt-system engineering.
