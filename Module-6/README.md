# 🚩 Module 6 — LangChain & AI Application Orchestration for DevOps

> **From manually connected AI components → reusable, testable and observable AI workflows.**

M5 proved that manual RAG works. M6 introduces orchestration abstractions to compose models, prompts, retrievers, parsers and tools without hiding the underlying architecture.

## 🔗 Dependency

```text
M3 API/Python → M4 Retrieval → M5 Manual RAG → M6 Orchestration
```

## 🎯 Learning Promise

- why orchestration frameworks exist
- direct SDK vs framework trade-offs
- LangChain component model
- prompts/models/output parsers
- Runnable/chain composition
- loaders/splitters/retrievers
- RAG chains
- memory vs state vs evidence
- tools and contracts
- retries, fallbacks and observability
- DevOps orchestration

## 📚 Canonical Sequence

| # | Topic | Deep Outcome |
|---|---|---|
| 01 | Why Orchestration Frameworks? | identify glue-code problems |
| 02 | LangChain Fundamentals | understand abstractions |
| 03 | Models, Prompts & Output Parsers | typed pipelines |
| 04 | Runnable & Chain Concepts | compose execution |
| 05 | Document Loaders & Splitters | reusable ingestion |
| 06 | Embeddings & Vector Stores | connect M4 components |
| 07 | Retrievers & RAG Chains | connect M5 components |
| 08 | Memory vs Application State | separate chat state/evidence |
| 09 | Tools & Tool Integration | connect DevOps capabilities |
| 10 | Errors, Retry & Observability | production-aware workflows |
| 11 | LangChain for DevOps | incident orchestration |
| 12 | Orchestrated DevOps RAG Assistant | complete integration |

## 🛠️ Setup

```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate   # Linux/macOS
pip install -r examples/requirements.txt
```

Use the provider/local model configured by the individual lab. Do not install every framework globally.

## 🧠 Deep Architecture

```text
Input
 ↓
Validation
 ↓
Prompt / Retriever / Tool components
 ↓
LLM
 ↓
Structured parser
 ↓
Validation
 ↓
Observable result
```

### Example

```python
chain = prompt | model | structured_parser
result = chain.invoke(context)
```

The operator is not the learning goal. Understand what each component does, what data crosses the boundary and what happens on failure.

## 🧪 Practical Progression

```text
V1 model call
V2 prompt template
V3 structured output
V4 runnable chain
V5 loader + splitter
V6 vector store + retriever
V7 RAG chain
V8 state separation
V9 tool-enabled DevOps workflow
V10 final assistant
```

## 🚫 Canonical Ownership

M4 owns vector mechanics. M5 owns RAG/grounding. M6 **uses** them through reusable components. Do not duplicate their fundamentals here.

## ✅ Exit Gate

You should be able to rebuild the M5 RAG flow with orchestration components, explain each abstraction, validate output, handle a transient failure and trace the workflow.

## 🔗 Continue

➡️ [Module 7 — MCP](../Module-7/README.md)

⬅️ [Module 5 — RAG](../Module-5/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)
