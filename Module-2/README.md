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

## 🛠️ Setup

Recommended shared Python environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Use Ollama for local prompt experiments where supported. Hosted provider testing is optional and must use environment-based credentials.

## 🧪 Practical Examples

Open: [`examples/README.md`](examples/README.md)

Core labs:

```text
01 vague → structured RCA prompt
02 Terraform change-review prompt
03 AKS troubleshooting prompt
04 evidence-only RCA
05 hallucination/abstention test
06 context builder
07 prompt chain
08 reusable/versioned template
09 prompt regression evaluation
10 final incident-analysis prompt system
```

### Canonical Context Builder

This is a key Module 2 practical and should not be repeated as a generic concept later:

```text
LOGS
  +
TERRAFORM
  +
AKS
  ↓
Context Builder
  ↓
Normalize
Redact
Deduplicate
Classify
Prioritize
Budget
  ↓
Source-Labeled Context
  ↓
LLM
  ↓
Trusted RCA
```

## 🔗 Module Boundaries

### M0 → M2
M0 introduces prompting. M2 owns the deep engineering.

### M1 → M2
M1 builds the agent. M2 improves the instructions/context driving it.

### M2 → M3
M2 produces reliable prompts/context. M3 teaches how the application transports those requests and responses.

### M2 → M4/M5
Later retrieval modules supply external context; they should reuse this module's grounding, abstention and context-budget principles rather than reteach them.

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

## 🔗 Continue

➡️ [Module 3 — APIs & Minimal Python for AI](../Module-3/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)

> **Outcome:** prompt writing becomes prompt-system engineering.
