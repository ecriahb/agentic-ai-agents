# 📚 Canonical Lesson Quality Contract

> **Applies to Module 0 → Module 12 on branch `agent/course-deduplication`.**

Every lesson in the mandatory learning path must behave like a real course chapter, not an isolated Markdown note.

## Mandatory lesson structure

Each canonical lesson should contain, in this order where applicable:

```text
1. Why this topic now
2. Prerequisites / previous lesson
3. English definition
4. Deep Hinglish explanation
5. Mental model / architecture diagram
6. DevOps scenario
7. Step-by-step example or code
8. Failure / edge-case drill
9. Security / trust-boundary note
10. Interview Q&A
11. Revision / key takeaways
12. Practical lab link
13. Completion checkpoint
14. Next lesson / next module link
```

## Canonical lesson rules

- A lesson may reuse earlier concepts, but must **apply** them instead of reteaching them from zero.
- Every lesson must identify the new capability it adds.
- Every code example must map to a practical stage or clearly explain why it is illustrative only.
- Every AI/agent lesson must state what is model-driven vs deterministic.
- Any evidence-related lesson must distinguish **current incident evidence** from **reference knowledge**.
- Any tool/action lesson must distinguish **LLM proposal** from **host authorization/execution**.
- Production-write examples remain simulated/read-only unless explicitly approved as a production-safe lab.
- Every canonical lesson must point forward to the next canonical lesson.

## Module ownership

```text
M0  AI/LLM foundations
M1  Tools + evidence + first controlled DevOps agent
M2  Deep prompt + context engineering
M3  API/HTTP/JSON/auth/Python/LLM integration plumbing
M4  Embeddings + vector search
M5  RAG + grounding + citations
M6  LangChain/application orchestration
M7  MCP
M8  Stateful graphs / LangGraph
M9  Multi-agent coordination
M10 Security + evaluation + red teaming
M11 Enterprise architecture + production
M12 Capstone integration
```

## Lesson status labels

Use one of these labels when a module contains older material:

- **CANONICAL** — part of mandatory sequential learning path.
- **REFERENCE** — useful optional reading; do not count as another mandatory chapter.
- **CONSOLIDATED** — its unique material has been merged into a canonical lesson.
- **LAB SUPPORT** — practical/setup material only.

## Learner rule

Follow the module README and its canonical lesson table. Do not infer the mandatory course path from raw filename numbering alone.
