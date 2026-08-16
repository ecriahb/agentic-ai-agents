# Module 6 Practical — LangChain & DevOps Orchestration

> **Run V1 → V10 in order. Har file sirf ek major concept introduce karta hai.**

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
ollama pull qwen2.5:3b
```

Run Ollama locally before model examples.

## Learning Progression

| Version | File | Main Learning |
|---|---|---|
| V1 | `01_first_langchain_call.py` | ChatOllama wrapper |
| V2 | `02_prompt_template.py` | PromptTemplate + runtime variables |
| V3 | `03_structured_parser.py` | Pydantic/structured result concept |
| V4 | `04_runnable_chain.py` | `prompt | llm | parser` composition |
| V5 | `05_loader_splitter.py` | Documents + chunking |
| V6 | `06_vectorstore_retriever.py` | embeddings + FAISS + retriever |
| V7 | `07_rag_chain.py` | source-aware RAG chain |
| V8 | `08_state_separation.py` | memory/state/evidence separation |
| V9 | `09_tool_workflow.py` | read-only DevOps tools + evidence log |
| V10 | `10_orchestrated_devops_assistant.py` | final integrated assistant |

## Sample Knowledge

`sample_docs/` contains small learning runbooks for AKS, Terraform networking and deployment troubleshooting.

## Important

These examples are intentionally local/read-only. They demonstrate architecture before real Azure/GitHub credentials are introduced.

```text
Model request != tool execution
Retriever result != current incident truth
Structured output != factual validation
Memory != evidence
```

## Failure Tests

Try intentionally:

```text
Ollama stopped
wrong model
empty question
unknown environment
empty docs
invalid tool argument
```

Observe which stage fails.

## Recommended Run Order

```bash
python 01_first_langchain_call.py
python 02_prompt_template.py
python 03_structured_parser.py
python 04_runnable_chain.py
python 05_loader_splitter.py
python 06_vectorstore_retriever.py
python 07_rag_chain.py
python 08_state_separation.py
python 09_tool_workflow.py
python 10_orchestrated_devops_assistant.py
```

The final project remains an educational read-only assistant; production integrations require authentication, RBAC, secret management, observability, evaluation and explicit remediation approval.
