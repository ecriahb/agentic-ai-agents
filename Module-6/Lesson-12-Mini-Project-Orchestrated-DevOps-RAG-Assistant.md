# 🚩 Jai Bajrangbali!

# Lesson 12 — Mini Project: Orchestrated DevOps RAG Assistant

> **Final goal: reusable components ke through DevOps knowledge retrieval, live evidence collection, grounded analysis, parsing and validation ko orchestrate karna.**

---

# 🎯 Final Project Outcome

User asks:

```text
Production AKS deployment Terraform networking change ke baad fail hua. Investigate and provide evidence-grounded RCA.
```

Application:

```text
validate input
→ retrieve runbooks
→ collect read-only evidence
→ label sources
→ build context
→ execute prompt/model/parser chain
→ validate claims
→ return status + RCA + evidence map
```

---

# PART 1 — Final Architecture

```text
                         USER INCIDENT
                              ↓
                      Input Validation
                              ↓
             ┌────────────────┴────────────────┐
             │                                 │
       Knowledge Retriever              Evidence Tools
             │                                 │
       R1/R2 reference docs        E1 pipeline / E2 tf / E3 AKS
             └────────────────┬────────────────┘
                              ↓
                       Context Builder
                              ↓
                       PromptTemplate
                              ↓
                        ChatOllama
                              ↓
                        Output Parser
                              ↓
                    Claim/Citation Validator
                              ↓
                     Confidence / Policy
                              ↓
                    FINAL READ-ONLY RCA
```

---

# PART 2 — Practical Versions

```text
V1  First LangChain model call
V2  PromptTemplate
V3  Structured parser
V4  Runnable chain
V5  Loader + splitter
V6  Vector store + retriever
V7  RAG chain
V8  State separation demo
V9  Tool-enabled incident flow
V10 Final orchestrated assistant
```

Each version introduces one main concept. Do not jump directly to V10 if the objective is learning.

---

# PART 3 — Project Folder

```text
Module-6/examples/
├── README.md
├── requirements.txt
├── 01_first_langchain_call.py
├── 02_prompt_template.py
├── 03_structured_parser.py
├── 04_runnable_chain.py
├── 05_loader_splitter.py
├── 06_vectorstore_retriever.py
├── 07_rag_chain.py
├── 08_state_separation.py
├── 09_tool_workflow.py
├── 10_orchestrated_devops_assistant.py
├── devops_tools.py
└── sample_docs/
    ├── aks-networking.md
    ├── terraform-networking.md
    └── pipeline-troubleshooting.md
```

---

# PART 4 — V1 to V4: Core Chain

### V1
Prove model wrapper works.

```text
Input → ChatOllama → Response
```

### V2
Separate runtime variables from stable instructions.

```text
Dict → PromptTemplate → Model
```

### V3
Add structured/typed output concepts.

```text
Model → Parser → Python data
```

### V4
Compose:

```text
Prompt | Model | Parser
```

---

# PART 5 — V5 to V7: RAG Orchestration

### V5

```text
Markdown
→ Loader
→ Document objects
→ Splitter
→ chunks
```

### V6

```text
chunks
→ embeddings
→ FAISS
→ retriever
```

### V7

```text
question
→ retriever
→ context
→ prompt
→ model
→ grounded answer
```

This should reproduce Module 5 fundamentals using reusable components.

---

# PART 6 — V8: State Separation

Store separately:

```python
conversation_context = {}
workflow_state = {}
evidence_log = []
permissions = {}
```

Do not use chat history as evidence store.

---

# PART 7 — V9: Tool Workflow

Tools:

```text
get_pipeline_status(environment)
get_terraform_changes(environment)
get_aks_status(cluster_name)
```

Learning version can use deterministic fake/local evidence, but tool contract must look like a real read-only integration.

Flow:

```text
incident
→ fixed read-only evidence collection
→ evidence log
→ analysis chain
```

---

# PART 8 — V10 Final Assistant

High-level pseudo-code:

```python
validate_incident()
reference_docs = retriever.invoke(question)
evidence = collect_read_only_tools()
context = build_labeled_context(reference_docs, evidence)
raw_result = analysis_chain.invoke(context)
validated = validate_rca(raw_result, evidence)
return validated
```

Important:

```text
orchestration != trust
validation still required
```

---

# PART 9 — Example Evidence

```text
[E1] Pipeline
Deployment failed during Terraform Apply.

[E2] Terraform
NSG rule aks-subnet-allow was removed.

[E3] AKS
Network connectivity validation is degraded.
```

Reference:

```text
[R1] aks-networking.md
AKS subnet traffic depends on required NSG and routing configuration.
```

---

# PART 10 — Expected Grounded Output

```text
Status: SUCCESS

Root Cause:
Current evidence shows that the NSG rule `aks-subnet-allow` was removed [E2], followed by degraded AKS network validation [E3]. This is consistent with the reference networking guidance [R1].

Confirmed Impact:
Deployment failed during Terraform Apply [E1].

Recommended Next Checks:
- Validate current AKS subnet NSG rules.
- Compare Terraform change against expected network policy.
- Re-run connectivity validation before redeployment.

Confidence:
MEDIUM
```

Do not invent:

```text
3-hour outage
customer impact
who removed rule
successful remediation
```

unless evidence confirms.

---

# PART 11 — Validation Rules

At minimum:

```text
1. Required output fields exist.
2. Citation IDs must exist in source map.
3. Confirmed impact must be supported by E* evidence.
4. Current root-cause facts cannot rely only on R* reference docs.
5. No destructive action can be marked executed.
6. Unknown evidence means UNKNOWN, not guess.
```

---

# PART 12 — Failure Tests

Run intentionally:

```text
1. Ollama stopped
2. Wrong model name
3. Empty docs directory
4. Empty incident
5. Unknown environment
6. Retriever returns weak docs
7. Tool returns timeout
8. Tool returns unauthorized
9. Model emits invalid structure
10. Model cites E99
11. Conflicting evidence
12. Prompt-injection text in a runbook
```

For every failure record expected status.

---

# PART 13 — Observability Checklist

Capture:

```text
request_id
workflow stage
duration
retrieved source IDs
tool calls and arguments
retry count
model name
parser result
validation failures
final status
```

Redact secrets and sensitive payloads.

---

# PART 14 — Acceptance Criteria

Project complete only if:

- [ ] core chain runs locally
- [ ] documents load and split
- [ ] retriever returns source metadata
- [ ] reference docs and current evidence remain separate
- [ ] tools validate arguments
- [ ] evidence log preserved outside LLM memory
- [ ] RAG answer can abstain
- [ ] parser has explicit failure behavior
- [ ] citations are validated
- [ ] destructive actions are not executed
- [ ] errors expose stage/status
- [ ] workflow can be traced

---

# PART 15 — Production Upgrade Path

```text
Local fake/read-only tools
      ↓
Authenticated Azure/GitHub integrations
      ↓
Managed identity / RBAC
      ↓
Persistent vector store
      ↓
Incremental indexing
      ↓
Central tracing
      ↓
Evaluation dataset
      ↓
Human approval workflow
      ↓
Controlled remediation
```

---

# PART 16 — Interview Q&A

### Q1. What does LangChain solve in this project?
It standardizes and composes prompts, models, parsers, document/retrieval components and tools into reusable workflows.

### Q2. What does it not solve?
Source trust, authentication, RBAC, business validation, evidence truth, remediation safety and human approval remain application responsibilities.

### Q3. Why preserve evidence outside the chain conversation?
For auditability, deterministic claim validation and protection against model-memory distortion.

### Q4. Why keep investigation read-only?
It reduces blast radius and lets the system prove trustworthy analysis before enabling controlled actions.

### Q5. What would you choose for more stateful branching agent workflows later?
A graph/state-machine style orchestration approach may be more suitable; the key is explicit state and controlled transitions.

---

# PART 17 — Final Module 6 Mental Model

```text
Components
  ↓
Contracts
  ↓
Composition
  ↓
State Boundaries
  ↓
Retrieval + Tools
  ↓
Grounded Model Call
  ↓
Parser
  ↓
Validation
  ↓
Observability
  ↓
Safe Output
```

---

# 🧠 Most Important Principles

```text
1. Framework is orchestration, not intelligence.
2. Direct SDK remains valid.
3. Component contracts matter more than syntax.
4. RAG fundamentals do not change because framework is used.
5. Memory is not evidence.
6. Tool requests are untrusted.
7. Read-only evidence first.
8. Retry side effects carefully.
9. Structured output is not factual validation.
10. Observability must be stage-aware.
11. Authorization is outside model reasoning.
12. Human approval protects remediation.
```

✅ **Module 6 complete → ready for MCP and more advanced stateful/agentic orchestration.**
