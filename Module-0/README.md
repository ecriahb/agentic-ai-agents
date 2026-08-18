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

These remain available as reference, but **are not separate mandatory chapters**:

- `Lesson-01-AI-Revolution.md`
- `Lesson-09-Temperature.md`
- `Lesson-10-Role-Prompting.md`
- `Lesson-11-Zero-One-Few-Shot.md`

## 🛠️ Setup

No API key is required.

```text
Git + editor + browser
```

Optional: create the course Python environment now so M1 can reuse it.

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

## 🧪 Beginner Hands-On Experiments

Open: [`examples/README.md`](examples/README.md)

Complete these in order:

```text
1. Next-token intuition
2. Context comparison
3. Hallucination test
4. System vs user prompt
5. Zero-shot vs few-shot
6. Prompt-injection intuition
7. Fact vs inference
8. First DevOps AI safety rules
```

## 🔗 Module Boundary

```text
M0: Understand the model
       ↓
M1: Build a controlled AI application
       ↓
M2: Engineer prompts/context deeply
```

M0 introduces prompting only. **M2 owns deep prompt engineering.** M3 owns API/Python plumbing.

## ✅ Completion Test

Before M1, explain without notes:

- What is an LLM?
- What is next-token prediction?
- Why does attention matter?
- What is a context window?
- Why can an LLM hallucinate?
- What makes a prompt useful?
- Why is model output not automatically truth?
- Why are verification and host controls required?

## 🔗 Continue

➡️ [Module 1 — LLM APIs, Tools & First DevOps Agent](../Module-1/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)

🚩 **Jai Bajrangbali — Learn • Understand • Build**
