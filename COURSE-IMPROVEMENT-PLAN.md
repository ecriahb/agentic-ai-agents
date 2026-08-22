# Course Improvement Plan — Module 0 to Module 12

## Audit Principle

This plan treats the repository's current files as the source of truth. The original improvement prompt is used as the quality bar, while stale assumptions are corrected from the actual repository.

## Current Repository Corrections

- Module 11 and Module 12 are already populated and documented; they are not empty/future modules.
- Module 0 README lists Lessons 00–14, which is 15 lesson entries, so course counts must be reconciled from actual files rather than copied from an older table.
- Module 4 already owns Top-K and basic similarity-search flow in Lesson 04; Lesson 05 should focus on metrics rather than re-teaching retrieval.
- Module 4 Lesson 02 and Lesson 03 have a real overlap around embedding/vector creation; the target is conceptual separation rather than deleting useful material.

## Priority Order

### P0 — Already completed / verify

- Module 4 Lesson 05: deduplicate metric concepts and add official references.

### P1 — Foundation boundaries

- Audit Modules 0–3 for definitions that should be introduced once and referenced later.
- Build explicit cross-module ownership for context, prompting, APIs, secrets, structured output, and tool calling.
- Reconcile lesson counts in module READMEs and root documentation.

### P2 — Vector/RAG boundaries

- Separate Module 4 Lessons 02/03 responsibilities.
- Keep Lesson 04 as similarity search + Top-K.
- Keep Lesson 05 as metric theory/semantics.
- Keep Lesson 06 as vector database/index fundamentals.
- Keep Lesson 07 as Chroma/FAISS implementation.
- Audit Module 5 so it assumes Module 4 retrieval foundations rather than repeating them.

### P3 — Framework boundaries

- Module 6 = LangChain implementation/orchestration.
- Module 7 = MCP protocol and capability interoperability.
- Module 8 = stateful single-agent/workflow architecture with LangGraph.
- Module 9 = multi-agent coordination patterns.
- Module 10 = cross-cutting security/evaluation/red-team controls.

### P4 — Production/course navigation

- Verify official links and version-sensitive statements.
- Verify runnable examples and dependency declarations.
- Update root README, practical index and audit documentation only where facts are stale.
- Keep Modules 11–12 aligned with actual enterprise architecture/capstone content.

## Official Source Policy

Prefer first-party or primary educational sources for technical claims:

- OpenAI documentation for embeddings/API behavior.
- Sentence Transformers documentation for encoding/similarity behavior.
- scikit-learn documentation for cosine similarity/distance semantics.
- FAISS documentation for index/metric/search semantics.
- NumPy documentation for norm/math primitives.
- Stanford CS224N / Stanford NLP resources for foundational NLP concepts.

When a claim is model- or dataset-dependent, say so explicitly instead of giving a universal threshold or score interpretation.

## Duplication Policy

A repeated topic is acceptable only when the later lesson changes one of:

```text
purpose
abstraction level
implementation context
risk/control context
```

Otherwise prefer a short bridge/reference to the canonical lesson.

## Lesson Quality Bar

Every lesson should make clear:

```text
Why now
→ English definition
→ Hinglish intuition
→ Mental model
→ DevOps example
→ Runnable or deterministic practical
→ Common failure/mistake
→ Production note
→ Interview check
→ Revision
→ Homework
→ Next-lesson bridge
→ Official references
```
