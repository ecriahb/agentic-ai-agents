# Course Simplification Plan

**Branch:** `agent/course-deduplication`
**Scope:** Module 0 through Module 12
**Goal:** Reduce unnecessary repetition while preserving the skills required for the final Enterprise DevOps AI capstone.

## Why this change

The current repository is strong but has grown into a very large curriculum. Several foundational concepts are taught more than once across modules, especially:

- prompt engineering
- system vs user prompts
- hallucination reduction
- context engineering
- API/HTTP/JSON fundamentals
- authentication and secrets
- Python basics
- LLM API calls
- structured output and validation
- provider comparisons

The goal is **not** to remove important knowledge. The goal is to establish one canonical home for each concept and make later modules build on it instead of reteaching it.

## Canonical ownership rules

| Concept | Canonical home | Later modules should |
|---|---|---|
| AI/ML/DL/LLM fundamentals | Module 0 | Reference, don't reteach |
| Prompt fundamentals | Module 0 | Use, don't repeat basics |
| Advanced prompt engineering | Module 2 | Own the deep treatment |
| API/HTTP/JSON plumbing | Module 3 | Use in labs |
| Secrets/authentication | Module 3 | Reference platform-specific patterns |
| LLM API integration | Module 3 | Use provider adapters |
| Tool calling + agent loop | Module 1 | Build on it |
| Evidence/validation/trusted RCA | Module 1 | Reuse as the trust boundary |
| Embeddings/vector search | Module 4 | Own embeddings/search |
| RAG | Module 5 | Own retrieval/grounding |
| LangChain | Module 6 | Own framework orchestration |
| MCP | Module 7 | Own tool/resource protocol |
| Stateful agents | Module 8 | Own graph/state orchestration |
| Multi-agent | Module 9 | Own multi-agent patterns |
| Security/evaluation | Module 10 | Own adversarial testing and release gates |
| Enterprise architecture | Module 11 | Own production architecture |
| Final integration | Module 12 | Own capstone |

## Proposed lean path

### Module 0 — AI & LLM Foundation

Keep the conceptual foundation, but merge the many small prompting lessons into a compact progression:

1. Orientation + AI/ML/DL/LLM
2. Tokens, next-token prediction + Transformer intuition
3. Context window + context limits
4. Hallucination + why LLM output is probabilistic
5. Prompting fundamentals + prompt structure
6. System/user + role + zero/one/few-shot as one practical lesson
7. Limitations, safety + prompt-injection intuition
8. Revision + mini-project

**Merge/de-emphasize:** standalone Temperature and Role Prompting lessons as separate chapters; they remain inside the consolidated prompting lesson.

### Module 1 — AI Application Mechanics & First DevOps Agent

Keep this as the first real engineering module:

1. UI vs API + application architecture
2. Environment + secrets setup
3. Local/cloud LLM call
4. Structured output + validation
5. Tool/function calling
6. Agent loop + tool contracts
7. Evidence-first DevOps agent + deterministic guardrails
8. Trusted RCA V1→V4 practical

**Remove duplication:** do not reteach API/secret fundamentals already owned by Module 3; link to Module 3 for deeper plumbing.

### Module 2 — Prompt & Context Engineering

Make this the **only deep prompt-engineering module**:

1. Prompt engineering fundamentals
2. Role + Context + Task + Constraints + Output
3. System vs user/developer instructions
4. Zero/one/few-shot
5. Structured DevOps prompts
6. Hallucination reduction + evidence grounding
7. Context Engineering for Logs/Terraform/AKS
8. Prompt chaining + reusable/versioned templates
9. Agent-loop prompts + guardrails
10. Prompt evaluation
11. Final prompt system / mini-project

This preserves the depth already built while removing the need to repeat the same concepts in Module 0 or Module 3.

### Module 3 — API & Minimal Python for AI

Compress the application-plumbing material into:

1. API + REST + HTTP + JSON (one connected foundation)
2. Authentication + API keys + environment/secrets
3. Minimal Python for AI
4. Calling an LLM through an API
5. OpenAI/Gemini/Azure OpenAI provider abstraction
6. API responses, errors, timeout/retry/rate limits
7. Structured AI responses + validation
8. Final API integration mini-project

**Merge:** REST/HTTP/JSON should be taught together instead of as three mostly independent beginner lessons. Authentication and environment secrets belong together. Provider comparison should stay focused on architecture rather than separate provider tutorials.

### Modules 4–12

These modules remain the specialization path because they introduce genuinely new capabilities:

```text
M4 Embeddings & Vector Search
  ↓
M5 RAG
  ↓
M6 LangChain
  ↓
M7 MCP
  ↓
M8 Stateful Agents / LangGraph
  ↓
M9 Multi-Agent
  ↓
M10 Security + Evaluation + Red Teaming
  ↓
M11 Enterprise Architecture + Production
  ↓
M12 Final Capstone
```

However, repeated explanations should be shortened to a **"Previously learned — apply it here"** bridge. Each module should teach its new abstraction, not restart the course.

## Specific repetition cuts

### Prompting

Do not repeat:

```text
Role prompting
System vs user
Few-shot
Hallucination basics
Prompt structure
```

in every module. Module 0 introduces; Module 2 owns the deep treatment; later modules apply it.

### API plumbing

Do not repeat:

```text
GET/POST
HTTP status codes
JSON basics
API keys
.env
Python requests
```

in multiple modules. Module 3 owns these fundamentals; application modules consume them.

### Validation and trust

Module 1 owns the first evidence/validation/trusted-RCA pattern. Later modules should extend it rather than redefine it.

### Providers

Provider-specific syntax belongs in small adapters/labs. The main curriculum should teach the invariant architecture:

```text
Application
  ↓
LLM interface
  ↓
Provider adapter
  ↓
OpenAI / Ollama / Azure / other provider
```

## What should NOT be removed

The following are intentionally retained because they represent meaningful capability progression:

- Tool calling
- Evidence-first reasoning
- RAG
- Reranking/hybrid retrieval
- LangChain
- MCP
- LangGraph/state
- Multi-agent systems
- Security/red teaming
- Evaluation/release gates
- Enterprise architecture
- Final capstone

## Migration strategy

This branch should be implemented in stages:

1. Establish the canonical ownership map.
2. Update module READMEs/navigation so learners follow the lean path.
3. Merge overlapping lesson content into canonical lessons where necessary.
4. Mark redundant standalone lessons as consolidated/deprecated before deletion.
5. Remove only files that have no unique content or active references.
6. Update root README, roadmap and cross-module links.
7. Validate that the final learner path has no broken links and no duplicated mandatory lessons.

## Target outcome

The course should feel like:

```text
Foundation
  ↓
AI application mechanics
  ↓
Prompt/context engineering
  ↓
API/Python plumbing
  ↓
RAG
  ↓
Orchestration
  ↓
MCP
  ↓
Stateful agents
  ↓
Multi-agent
  ↓
Security + evaluation
  ↓
Enterprise production
  ↓
Capstone
```

rather than a collection of repeated standalone tutorials.
