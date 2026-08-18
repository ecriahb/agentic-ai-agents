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

To remove repetition, the mandatory path is now **8 learning units**. Follow this table rather than raw filename numbering.

| Unit | Canonical topic | Canonical lesson |
|---|---|---|
| 00 | Orientation | [Lesson 00](Lesson-00-Orientation.md) |
| 01 | AI → ML → DL → LLM | [Lesson 02](Lesson-02-AI-ML-DL-LLM.md) |
| 02 | Tokens + Transformer + Attention | [Lesson 03](Lesson-03-Next-Token-Prediction.md) + [Transformer/Attention](Lesson-04-Transformer-Attention.md) |
| 03 | Context Window | [Lesson 05](Lesson-05-Context-Window.md) |
| 04 | Hallucination + LLM Limitations | [Lesson 06](Lesson-06-Hallucination.md) |
| 05 | Prompting Fundamentals | [Lesson 07](Lesson-07-Prompt-Engineering.md) |
| 06 | Prompt Structure + System/User + Role + Zero/One/Few-shot | [Lesson 08](Lesson-08-System-vs-User-Prompt.md) |
| 07 | Structured Reasoning + Safety | [Lesson 12](Lesson-12-Structured-Reasoning.md) |
| 08 | Revision + Mini Project | [Lesson 14](Lesson-14-Grand-Revision-Mini-Project.md) |

### Consolidation rule

The deleted standalone chapters were redundant with the canonical units:

- AI Revolution → covered by Orientation + AI/ML/DL/LLM
- Temperature → covered as a variability/parameter concept where relevant
- Role Prompting → covered inside Prompt Structure
- Zero/One/Few-shot → covered inside Prompt Structure

They are **not separate mandatory chapters** anymore.

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

## 📚 Lesson Contract

Canonical lessons should follow the repository lesson contract:

[`LESSON-QUALITY-CONTRACT.md`](../LESSON-QUALITY-CONTRACT.md)

## 🔗 Continue

➡️ [Module 1 — LLM APIs, Tools & First DevOps Agent](../Module-1/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)

🚩 **Jai Bajrangbali — Learn • Understand • Build**
