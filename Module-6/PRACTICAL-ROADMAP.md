# Module 6 — Zero-to-Hero Practical Roadmap

> Goal: raw Python/LLM/RAG pieces ko reusable LangChain orchestration me convert karna, without hiding trust boundaries.

## V1 — First LangChain Model Call
Run `examples/01_first_langchain_call.py`.

**Observe:** direct SDK vs framework wrapper difference.

## V2 — PromptTemplate
Run `02_prompt_template.py`.

Change variables and verify prompt rendering before model invocation.

## V3 — Structured Parser
Run `03_structured_parser.py`.

Test malformed output.

**Rule:** parser validates shape; host still validates truth/policy.

## V4 — Runnable Chain
Run `04_runnable_chain.py`.

Trace component-by-component:
`Input → Prompt → Model → Parser`.

## V5 — Loader + Splitter
Run `05_loader_splitter.py`.

Try large vs small chunks and inspect metadata preservation.

## V6 — Vector Store + Retriever
Run `06_vectorstore_retriever.py`.

Confirm retrieval works independently of answer generation.

## V7 — RAG Chain
Run `07_rag_chain.py`.

Test relevant and irrelevant questions. Do not force generation when evidence is poor.

## V8 — Memory vs Application State
Run `08_state_separation.py`.

Classify values into:
- conversation memory
- current evidence
- workflow state
- authorization/policy

## V9 — Tool Workflow
Run `09_tool_workflow.py`.

Check tool allowlist, argument validation and read-only behavior.

## V10 — Orchestrated DevOps Assistant
Run `10_orchestrated_devops_assistant.py`.

Trace full pipeline and identify exactly which component owns:
- retrieval
- model reasoning
- parsing
- validation
- tool execution

## Provider Bonus
Run `11_dual_provider_langchain.py` using `ChatOllama` and `ChatOpenAI`.

**Pass:** same orchestration contract works while model provider changes.

### Failure Drills
- model unavailable
- retriever empty
- parser failure
- tool failure
- malformed tool arguments

### Acceptance Criteria
Learner can explain: `LangChain orchestrates components; it does not make an agent truthful or authorized.`

## Hero Outcome
Learner can build modular AI application pipelines and knows where framework abstraction must stop and host controls must begin.
