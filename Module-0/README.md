# 🚩 Module 0 — AI & LLM Foundation

> **Understand AI/LLMs before building AI applications.**

Module 0 is the conceptual foundation. It intentionally has **no API-key or coding prerequisite**.

## 🎯 Goal

By the end, you should understand:

```text
AI → ML → DL → LLM
        ↓
Tokens / Next-token prediction
        ↓
Transformer / Attention intuition
        ↓
Context
        ↓
Prompting
        ↓
Hallucination / Limitations
        ↓
Safety / Verification
```

## 🧭 Lean Canonical Learning Path

To remove repetition, the mandatory path is now **8 learning units**. Some older standalone lesson files remain in the repository temporarily so existing links do not break; their concepts are consolidated into the units below.

| Unit | Canonical topic | Existing material used |
|---|---|---|
| 00 | [Orientation](Lesson-00-Orientation.md) | Lesson 00 |
| 01 | [AI → ML → DL → LLM](Lesson-02-AI-ML-DL-LLM.md) | Lessons 01–02 |
| 02 | [Tokens + Transformer + Attention](Lesson-03-Next-Token-Prediction.md) | Lessons 03–04 |
| 03 | [Context Window](Lesson-05-Context-Window.md) | Lesson 05 |
| 04 | [Hallucination + LLM Limitations](Lesson-06-Hallucination.md) | Lessons 06 + relevant parts of 13 |
| 05 | [Prompting Fundamentals](Lesson-07-Prompt-Engineering.md) | Lesson 07 |
| 06 | [Prompt Structure + System/User + Role + Zero/One/Few-shot](Lesson-08-System-vs-User-Prompt.md) | Lessons 08–11 |
| 07 | [Structured Reasoning + Safety](Lesson-12-Structured-Reasoning.md) | Lessons 12–13 |
| 08 | [Revision + Mini Project](Lesson-14-Grand-Revision-Mini-Project.md) | Lesson 14 |

### De-emphasized standalone lessons

These are still available as reference, but **should not be treated as separate mandatory chapters**:

- `Lesson-01-AI-Revolution.md` — context/background, covered inside the foundation
- `Lesson-09-Temperature.md` — parameter detail belongs with model behavior/API lessons later
- `Lesson-10-Role-Prompting.md` — consolidated into the prompt-structure unit
- `Lesson-11-Zero-One-Few-Shot.md` — consolidated into the prompt-structure unit

This prevents Module 0 from teaching the same prompt concepts again before Module 2.

## 🧪 Beginner Hands-On Experiments

Open: [`examples/README.md`](examples/README.md)

The experiments remain no-code and should be completed alongside the canonical units:

```text
Next-token intuition
Context comparison
Hallucination test
System vs user prompt
Zero-shot vs few-shot
Prompt injection intuition
Fact vs inference
First DevOps AI safety rules
```

## 🔗 Boundary with Module 1 and Module 2

```text
Module 0
Understand what LLMs are and their limitations
        ↓
Module 1
Use an LLM inside a controlled application
        ↓
Module 2
Engineer prompts/context systematically and evaluate behavior
```

**Important:** Module 0 introduces prompting. **Module 2 owns deep prompt engineering.** Later modules should apply these concepts rather than reteach them.

## ✅ Module 0 Completion Test

Before Module 1, explain without notes:

- What is an LLM?
- What is next-token prediction?
- Why does attention matter?
- What is a context window?
- Why can an LLM hallucinate?
- What makes a prompt useful?
- Why is model output not automatically truth?
- Why are verification and host controls required?

🚩 **Jai Bajrangbali — Learn • Understand • Build**
