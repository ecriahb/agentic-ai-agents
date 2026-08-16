# Module 5 — Zero-to-Hero Practical Roadmap

> Goal: retrieval-only system ko evidence-grounded RAG assistant me evolve karna.

## V1 — Retrieval Only
Run `examples/01_retrieve_only.py`.

**Learn:** relevant chunks milna = answer generate hona nahi.

## V2 — Build Source-Labeled Context
Run `02_build_context.py`.

Check every chunk has source/chunk identity.

## V3 — First Basic RAG
Run `03_basic_rag.py`.

Trace:
`Question → Retrieve → Context → Prompt → LLM → Answer`.

## V4 — RAG With Sources
Run `04_rag_with_sources.py`.

**Pass:** answer source IDs cite kare; learner source map inspect kare.

## V5 — No-Context Guardrail
Run `05_rag_no_context_guardrail.py` with an unrelated question.

Expected: generation forced nahi honi chahiye.

## V6 — Threshold Policy
Run `06_rag_threshold.py`.

Try high/low thresholds and observe false-negative vs noisy-context tradeoff.

## V7 — Safe Query Rewrite
Run `07_query_rewrite.py`.

Rewrite wording, but incident facts invent mat karo.

## V8 — Multi-Query Retrieval
Run `08_multi_query_rag.py`.

Inspect duplicate merge and best-score retention.

## V9 — Citation Validation
Run `09_rag_validation.py`.

Inject fake citation such as `[S99]`; host validator must reject it.

## V10 — Final DevOps RAG Assistant
Run `10_devops_rag_assistant.py`.

Test:
- strong relevant query
- weak query
- irrelevant query
- conflicting/stale-looking context

## Provider Bonus — Same RAG, Two LLMs
Run `11_dual_provider_rag_assistant.py` with Ollama and OpenAI.

**Key observation:** retrieval, threshold, source IDs and citation policy stay host-controlled; only generation provider changes.

### Acceptance Criteria
Learner can explain:
`Retrieved ≠ Relevant ≠ Correct ≠ Authorized` and `No evidence → no forced answer`.

## Hero Outcome
Learner builds a RAG system that is grounded, source-aware, abstention-capable and provider-independent.
