# Module 5 — RAG Practical Labs

> **Goal: semantic retrieval ko gradually grounded DevOps RAG assistant me convert karna.**

## Setup

```bash
cd Module-5/examples
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Local generation examples assume Ollama is available on:

```text
http://localhost:11434
```

Default model in examples:

```text
qwen3:4b
```

If your local model name differs, update `OLLAMA_MODEL` in `rag_utils.py`.

---

# Practical Progression

| Version | File | What changes? |
|---|---|---|
| V1 | `01_retrieve_only.py` | Query → embedding → FAISS top-k |
| V2 | `02_build_context.py` | Add `[S1]` source-labeled context |
| V3 | `03_basic_rag.py` | Context + question → Ollama answer |
| V4 | `04_rag_with_sources.py` | Require source citations |
| V5 | `05_rag_no_context_guardrail.py` | No retrieved evidence → no generation |
| V6 | `06_rag_threshold.py` | Add minimum relevance score policy |
| V7 | `07_query_rewrite.py` | Safe deterministic query normalization |
| V8 | `08_multi_query_rag.py` | Multiple query variants + dedupe merge |
| V9 | `09_rag_validation.py` | Validate model citations against source map |
| V10 | `10_devops_rag_assistant.py` | Final integrated learning assistant |

Shared helper:

```text
rag_utils.py
```

Sample knowledge:

```text
sample_docs/
├── aks-networking.md
├── terraform-networking.md
├── pipeline-failure.md
└── production-rollback.md
```

---

# Recommended Run Order

```text
V1
↓
inspect retrieved chunks
↓
V2
↓
inspect context labels
↓
V3
↓
first RAG answer
↓
V4
↓
source-aware answer
↓
V5/V6
↓
safe weak-retrieval behavior
↓
V7/V8
↓
better query recall
↓
V9
↓
validate citations
↓
V10
↓
final assistant
```

---

# Test Questions

Use these:

```text
Why can AKS workloads lose connectivity after an NSG change?

What should I inspect when Terraform networking changes break a deployment?

What does the pipeline check after Terraform Apply?

What is the approved production rollback process?

Who approved ticket CHG999999?
```

The last question is intentionally unsupported. A reliable system should not invent the answer.

---

# Failure Tests

1. Stop Ollama and run V3/V10.
2. Ask an unrelated question.
3. Set threshold very high.
4. Change model to a nonexistent name.
5. Empty the docs directory temporarily.
6. Force the LLM to output a fake source ID like `[S99]` and observe V9 validation.

---

# Evaluation Habit

For every change record:

```text
Question
Expected Source
Actual Top-3
Best Score
Correct Source Found?
Answer Grounded?
Unsupported Claim?
Citation Valid?
```

Do not judge RAG quality from one impressive demo response.
