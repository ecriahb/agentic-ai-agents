# Course-Wide Content Audit Status

## Scope

This audit follows the full-course improvement brief for Modules 0–12. It prioritizes **content ownership, duplication control, official references, runnable examples, versioning, and navigation**.

## Important baseline correction

The supplied planning table described Modules 11 and 12 as empty/future. The repository is ahead of that plan: those modules already contain course content. Therefore the repository state—not the stale planning table—is the source of truth for final counts and module status.

## Current verified work

### Module 4 — Priority

- [x] Lesson 05 rewritten to remove repeated metric explanations and consolidate theory/practical/revision.
- [x] Lesson 02 clarified as embedding concepts and representation.
- [x] Lesson 03 clarified as the text-to-vector implementation pipeline.
- [x] Lesson ownership map added.
- [x] Module README boundaries clarified.

### Course architecture

- [x] Cross-module ownership map created in `CROSS-MODULE-REFERENCE-MAP.md`.
- [x] Canonical ownership defined for prompting, APIs, embeddings, RAG, MCP, LangGraph, multi-agent systems, and security/evaluation.
- [x] Reinforcement policy defined: short prerequisite reminder + module-specific application + reference to canonical lesson.

### Documentation reconciliation

- [x] Module 0 lesson-count discrepancy corrected from 14 to the actual Lesson-00 through Lesson-14 sequence.
- [x] Modules 11/12 marked as existing content in the audit baseline rather than future placeholders.

## Priority backlog

### P0 — Content duplication

- [ ] Audit Module 0 prompting lessons against Module 2; keep Module 0 introductory and Module 2 definitive.
- [ ] Audit Module 1 context/tool-calling lessons against Modules 2, 7, and 8.
- [ ] Audit Module 3 provider/API lessons against Module 1.
- [ ] Audit Module 5 RAG fundamentals against Module 4 and make boundaries explicit.

### P1 — Modules 4–10

- [ ] Verify Module 4 Lessons 6/7 separation: fundamentals vs hands-on.
- [ ] Verify Module 4 Lessons 11/12 use distinct DevOps scenarios.
- [ ] Verify Module 5 owns retrieval strategy while Module 6 owns LangChain implementation.
- [ ] Verify Module 7 MCP security is protocol-specific and Module 10 owns cross-system security.
- [ ] Verify Module 8 single-agent stateful orchestration vs Module 9 multi-agent coordination.

### P1 — Official sources

- [ ] Verify every official URL is live/current.
- [ ] Prefer first-party documentation over blogs when documenting API/library semantics.
- [ ] Add version/date notes where behavior is version-sensitive.
- [ ] Mark custom code as custom rather than presenting it as copied official code.

### P1 — Code quality

- [ ] Run/verify Python examples where execution is available.
- [ ] Pin dependencies for practical projects.
- [ ] Check error handling and secret hygiene.
- [ ] Remove hard-coded credentials or provider-specific assumptions.

### P2 — Navigation

- [ ] Verify every lesson's Previous/Next links.
- [ ] Verify module READMEs list every lesson exactly once.
- [ ] Reconcile root README counts from actual repository files.
- [ ] Reconcile `PRACTICALS-INDEX.md` and each `PRACTICAL-ROADMAP`.

## Quality gate

A lesson is considered audit-complete only when:

1. Its concept has a clear owner.
2. Repeated material is either removed or explicitly contextualized.
3. Official sources are used for library/protocol semantics.
4. Code is runnable or clearly marked as illustrative.
5. Prerequisites and next lesson are accurate.
6. DevOps examples add domain value rather than merely renaming generic examples.

## Branch

All audit changes in this phase are being made on:

```text
feature/full-course-content-audit
```

The default branch is intentionally left untouched until the audit is reviewed.
