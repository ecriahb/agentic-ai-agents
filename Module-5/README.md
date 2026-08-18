# 🚩 Module 5 — Retrieval-Augmented Generation (RAG) for DevOps

> **From semantic search → grounded AI answers using your own DevOps knowledge.**

M4 taught how to find relevant knowledge. M5 teaches how to safely place retrieved knowledge into an LLM workflow without confusing reference material with live incident evidence.

## 🎯 Learning Promise

By the end you will understand:

- RAG and why retrieval must precede generation
- indexing-time vs query-time pipelines
- context construction and source labels
- grounded prompting and abstention
- top-k, score thresholds and no-context behavior
- citations and traceability
- query rewriting, multi-query, reranking and hybrid retrieval
- RAG hallucinations and guardrails
- retrieval vs generation evaluation
- freshness, ACLs, security, observability and cost
- complete DevOps RAG assistant

## 🔗 Dependency

```text
M3 Python/API
   ↓
M4 Embeddings + Vector Search
   ↓
M5 RAG
   ↓
M6 Orchestration
```

## 📚 Canonical Lesson Sequence

| Lesson | Topic | Main Outcome |
|---|---|---|
| 01 | RAG Fundamentals | retrieval + augmented context + generation |
| 02 | RAG Architecture & Data Flow | separate indexing/query pipelines |
| 03 | Building Context for the LLM | convert chunks into evidence context |
| 04 | Grounded Prompt Design | evidence-first answers and abstention |
| 05 | Top-K, Thresholds & No-Context | control weak retrieval |
| 06 | Citations & Source Traceability | make answers auditable |
| 07 | Query Rewriting & Multi-Query | improve vague queries |
| 08 | Reranking & Hybrid Search | improve relevance |
| 09 | RAG Hallucinations & Guardrails | separate retrieval from model inference |
| 10 | RAG Evaluation | measure retrieval and answer quality separately |
| 11 | Production RAG for DevOps | freshness, RBAC, monitoring and cost |
| 12 | DevOps RAG Knowledge Assistant | end-to-end project |

## 🛠️ Setup

Use the M4 retrieval environment plus an LLM route from M3. Local LLM inference is preferred for first labs.

```text
M4 retriever
   +
M3 LLM client
   ↓
RAG application
```

Never put API keys, credentials or unrelated secrets into retrieved documents or model context.

## 🧠 Core Architecture

```text
                 INDEXING TIME
Documents → clean → chunk → embed → vector index

                  QUERY TIME
Question → embed → retrieve → filter → rerank
                                  ↓
                         source-labelled context
                                  ↓
                         grounded prompt
                                  ↓
                                 LLM
                                  ↓
                        answer + citations
```

### DevOps example

```text
Question:
"Why did the AKS deployment fail after Terraform changes?"

Retrieved reference:
R1 = AKS networking runbook
R2 = previous NSG troubleshooting guide

Current evidence:
E1 = Terraform removed NSG rule
E2 = AKS network degraded
```

The answer may use R1/R2 to explain the mechanism, but **E1/E2 establish what happened now**.

## 🧪 Practical Progression

```text
V1 → retrieve chunks only
V2 → build context block
V3 → send context + question to local LLM
V4 → add source labels
V5 → add no-context guardrail
V6 → add score threshold
V7 → add query rewrite
V8 → add multi-query merge
V9 → add citation validation
V10 → final DevOps RAG Assistant
```

## 🔐 Hard Rules

```text
RAG reference ≠ current evidence
High similarity ≠ truth
No retrieval ≠ permission to guess
Unknown source ID ≠ valid citation
```

## 🚫 Do Not Repeat Later

M5 owns RAG concepts, grounding and retrieval-quality reasoning. M6 will wrap these components with orchestration; it should not become another RAG fundamentals course.

## ✅ Exit Gate

You should be able to:

1. Draw indexing and query-time pipelines.
2. Explain how retrieved chunks become prompt context.
3. Implement no-context behavior.
4. Add source IDs and citations.
5. Separate retrieval quality from generation quality.
6. Explain why RAG reduces but does not eliminate hallucination.
7. Design freshness and access-control boundaries.

## 🔗 Continue

➡️ [Module 6 — LangChain & Orchestration](../Module-6/README.md)

⬅️ [Module 4 — Embeddings & Vector Search](../Module-4/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
