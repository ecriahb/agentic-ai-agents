# Cross-Module Reference Map

> Canonical ownership map for the Agentic AI for DevOps course.
>
> **Rule:** a later module may reuse a concept, but it should teach only the module-specific application unless the concept is explicitly expanded there.

## Canonical ownership

| Concept | Canonical module | Later modules should do |
|---|---|---|
| LLM fundamentals | Module 0 | Reference, then apply |
| Context window / tokens | Module 0 | Use in provider/API/RAG context; do not reteach fundamentals |
| Hallucination fundamentals | Module 0 | Module 2 owns prevention; Module 5 owns RAG grounding; Module 10 owns security/evaluation |
| Prompt engineering fundamentals | Module 0 | Module 2 is the definitive prompting module |
| Prompt engineering advanced patterns | Module 2 | Module 5/6/8 use them in RAG/orchestration contexts |
| REST / HTTP / JSON / authentication | Module 3 | Module 1 demonstrates first call; later modules focus on their protocol/framework |
| Embeddings concepts | Module 4 | Module 5 uses embeddings as a RAG component; Module 6 implements them in LangChain |
| Text → vector implementation | Module 4 | Later modules should link back rather than repeat model mechanics |
| Similarity / distance metrics | Module 4 Lesson 05 | Retrieval systems may configure metrics but should reference Module 4 |
| Vector databases / indexes | Module 4 | Module 5 focuses on retrieval architecture; Module 6 focuses on framework implementation |
| Chunking / metadata / indexing | Module 4 | Module 5 owns RAG-specific strategy; Module 6 owns LangChain implementation |
| RAG architecture | Module 5 | Module 6/8 implement it; do not redefine the full pattern |
| Retrieval quality / Top-K / thresholds / reranking | Module 5 | Module 6 implements retrieval; Module 10 evaluates/security-tests it |
| Tool calling fundamentals | Module 1 | Module 7 owns MCP protocol; Module 8/9 own orchestration patterns |
| MCP protocol | Module 7 | Module 8/9 integrate MCP; Module 10 audits MCP security |
| Agent state machines | Module 8 | Module 9 extends them to multi-agent coordination |
| Multi-agent architecture | Module 9 | Module 10 focuses on threats/evaluation, not architecture fundamentals |
| Secrets / basic API security | Module 1/3 | Module 10 owns comprehensive agent security |
| Agent security | Module 10 | Earlier modules should link to it for advanced controls |
| Evaluation | Module 2 (prompt evaluation) + Module 5 (RAG evaluation) | Module 10 owns cross-system/agent evaluation and red teaming |

## Reinforcement policy

Repetition is acceptable when it changes the **application context**. It is not acceptable when the same definition, diagram, example, and explanation are copied into multiple lessons.

Use this pattern:

```text
Canonical concept
    ↓
Short prerequisite reminder
    ↓
Module-specific application
    ↓
Link back to canonical lesson
```

## Module boundaries

### Module 0 → Module 2
Module 0 introduces prompting vocabulary only. Module 2 is the definitive prompt-engineering course.

### Module 1 → Module 3
Module 1 gets the learner to a working API call/agent. Module 3 teaches provider-neutral API engineering, HTTP, authentication, errors, and integration patterns.

### Module 4 → Module 5
Module 4 explains how vectors, similarity, indexes, and vector stores work. Module 5 explains how those primitives combine into a production RAG pipeline.

### Module 5 → Module 6
Module 5 owns RAG architecture and retrieval strategy. Module 6 owns how to implement that architecture with LangChain.

### Module 7 → Module 8/9
Module 7 owns MCP as a protocol. Modules 8 and 9 consume MCP as an integration capability rather than reteaching protocol internals.

### Module 8 → Module 9
Module 8 owns stateful single-agent graphs and orchestration. Module 9 owns coordination between multiple agents.

### Module 9 → Module 10
Module 9 owns multi-agent design. Module 10 owns threats, guardrails, evaluation, red teaming, and production controls across agents.

## Audit status

- [x] Module 4 Lesson 02/03 ownership clarified
- [x] Module 4 Lesson 05 duplication rewrite completed
- [x] Module 0 lesson-count discrepancy identified and corrected
- [ ] Module 0–3 lesson-level reference links
- [ ] Module 4–6 lesson-level reference links
- [ ] Module 7–10 lesson-level reference links
- [ ] Automated link/code/version verification

This map is intentionally a governance document: lesson content should point here when a boundary question arises.
