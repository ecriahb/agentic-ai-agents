# 📚 Agentic AI for DevOps — Final Curriculum Map

> **Canonical learning spine for Module 0 → Module 12.**
>
> This document is the dependency map for the entire course. Each module teaches one new engineering capability, builds on the previous module, and links its setup, lessons, examples and mini-project.

## 🎯 Final Outcome

Build a production-oriented DevOps AI Assistant that can:

```text
Incident
  ↓
Trusted current evidence
  ↓
Approved reference knowledge / RAG
  ↓
Specialist tools + MCP capabilities
  ↓
Stateful orchestration
  ↓
Grounded synthesis
  ↓
Validation + security policy
  ↓
Human approval for risky actions
  ↓
Controlled execution + verification
  ↓
Audit / observability
```

## 🧭 Course Dependency Graph

```text
M0  AI / LLM Foundations
 ↓
M1  AI Application Mechanics + First DevOps Agent
 ↓
M2  Prompt + Context Engineering
 ↓
M3  API + Minimal Python + Reliable LLM Integration
 ↓
M4  Embeddings + Vector Search
 ↓
M5  RAG + Grounding
 ↓
M6  LangChain / Application Orchestration
 ↓
M7  MCP / Standardized Capabilities
 ↓
M8  Stateful Agents / LangGraph
 ↓
M9  Multi-Agent Systems
 ↓
M10 Security + Evaluation + Red Teaming
 ↓
M11 Enterprise Azure Architecture + Production
 ↓
M12 Final Enterprise Capstone
```

## 🔒 Canonical Ownership — No Re-teaching Rule

| Concept | Deep owner | Later modules |
|---|---|---|
| AI/ML/DL/LLM fundamentals | M0 | Apply only |
| Prompt basics | M0 | Apply only |
| Advanced prompting/context | M2 | Apply only |
| APIs/HTTP/JSON/secrets/Python | M3 | Use, do not reteach |
| Tool calling/evidence/trusted RCA | M1 | Extend |
| Embeddings/vector search | M4 | Extend |
| RAG/grounding/citations | M5 | Extend |
| LangChain | M6 | Use where appropriate |
| MCP | M7 | Extend |
| Stateful graph/state/checkpoints | M8 | Extend |
| Multi-agent coordination | M9 | Extend |
| Security/evaluation/red teaming | M10 | Enforce |
| Enterprise architecture | M11 | Apply in capstone |
| Full integration | M12 | Final outcome |

## 🛠️ Global Setup

### Required baseline

```text
Git
Python 3.11+
VS Code or another IDE
A terminal
GitHub account
```

### Recommended local structure

```text
agentic-ai-for-devops/
├── .venv/
├── Module-0/
├── Module-1/
├── ...
├── Module-12/
└── README.md
```

### Python environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install only the requirements required by the module/lab you are running. Do not install every framework globally just to follow the course.

### Local LLM route

Use Ollama for provider-independent local experiments where the module calls for an LLM.

```text
Python application
      ↓
Ollama
      ↓
Local model
```

### Hosted route

Use an approved hosted provider only when the lab requires it. Keep credentials in environment variables or a proper secret manager.

```text
Application
   ↓
Provider adapter
   ↓
Hosted LLM
```

Never commit `.env`, API keys, tokens or passwords.

## 📦 Module-by-Module Deep Path

### M0 — AI & LLM Foundation

**Purpose:** build the mental model before code.

1. Orientation and AI/ML/DL/LLM
2. Tokens and next-token prediction
3. Transformer/attention intuition
4. Context window and information limits
5. Hallucination and probabilistic output
6. Prompt anatomy and instruction/data separation
7. System/user, role and zero/one/few-shot
8. Structured reasoning, safety and verification
9. Revision and mini-project

**Setup:** no API key; no mandatory coding.

**Examples:** token prediction, context-window comparison, hallucination test, prompt injection intuition, fact vs inference.

**Output:** explain why an LLM can produce fluent but unsupported output.

**Next:** M1 turns the model into a controlled application.

### M1 — AI Application Mechanics & First DevOps Agent

**Purpose:** build the first controlled agent.

1. UI vs API and application architecture
2. Development environment and secret hygiene
3. Hosted and local LLM setup
4. First request and response object
5. Structured output and Pydantic validation
6. Tool/function calling and tool contracts
7. Host-controlled execution
8. Evidence preservation and provenance
9. Bounded agent loop and guardrails
10. Trusted RCA V1 → V4

**Setup:** Python venv; Ollama for local labs; provider credential only where required.

**Examples:** pipeline status, Terraform changes, AKS status, allowlist validation, evidence log, deterministic RCA.

**Output:** evidence-grounded read-only DevOps RCA agent.

**Next:** M2 makes its prompts/context reliable.

### M2 — Prompt & Context Engineering

**Purpose:** make reasoning behavior reliable, bounded and testable.

1. Prompt fundamentals
2. Role + Context + Task + Constraints + Output
3. System/user/developer instruction boundaries
4. Zero/one/few-shot
5. Structured DevOps prompts
6. Hallucination reduction and abstention
7. Context Engineering: normalize, redact, deduplicate, classify, prioritize, budget
8. Prompt chaining
9. Agent-loop prompts and guardrails
10. Prompt evaluation/regression
11. Reusable/versioned prompt templates
12. Incident-analysis prompt system

**Setup:** Python environment; local LLM recommended; optional hosted provider for parity testing.

**Core practical:**

```text
LOGS + TERRAFORM + AKS
        ↓
Context Builder
        ↓
Normalize → Redact → Deduplicate → Classify → Prioritize → Budget
        ↓
Source-labeled Context
        ↓
LLM
        ↓
Trusted RCA
```

**Output:** reusable prompt/context system.

**Next:** M3 explains the application plumbing underneath it.

### M3 — APIs & Minimal Python for AI

**Purpose:** understand and build reliable API-driven AI applications without becoming a generic Python course.

1. API + REST + HTTP
2. JSON and payloads
3. Authentication, API keys, environment variables and secrets
4. Minimal Python: variables, dict/list, functions, exceptions, JSON, typing
5. Calling LLM APIs
6. Provider abstraction: OpenAI/Ollama/Gemini/Azure OpenAI concepts
7. Response handling, errors, timeout, retry, rate limits
8. Structured responses and validation
9. First AI application mini-project

**Setup:** Python venv; `requests`; provider SDK only for the selected lab; Ollama for local route.

**Output:** debug an API-driven AI application and switch providers behind an adapter.

**Next:** M4 introduces semantic retrieval because manually supplying all context does not scale.

### M4 — Embeddings & Vector Search

**Purpose:** automatically find semantically relevant knowledge.

1. Why external/private knowledge is needed
2. Embeddings
3. Text → vectors
4. Similarity search
5. Cosine similarity/distance
6. Vector DB fundamentals
7. ChromaDB/FAISS
8. Chunking
9. Metadata/filtering
10. Indexing vs retrieval
11. DevOps knowledge base
12. Search mini-project

**Setup:** module `requirements.txt`; local embedding model/provider as specified by the lab; ChromaDB/FAISS only when used.

**Examples:** runbooks, incident notes, Terraform/AKS troubleshooting documents.

**Output:** semantic search over a DevOps knowledge base.

**Next:** M5 feeds retrieved chunks into an LLM to produce grounded answers.

### M5 — RAG

**Purpose:** retrieval + context + generation with source traceability.

1. RAG fundamentals
2. Indexing-time vs query-time architecture
3. Context construction
4. Grounded prompt design
5. Top-k, score thresholds and no-context behavior
6. Citations/source traceability
7. Query rewriting/multi-query
8. Reranking/hybrid search
9. RAG hallucinations and guardrails
10. RAG evaluation
11. Production RAG
12. DevOps RAG Assistant

**Setup:** M4 retrieval environment + LLM route from M3; never place secrets inside retrieved context.

**Practical progression:** retrieve → context → LLM → sources → no-context guardrail → threshold → rewrite → rerank → citation validation.

**Output:** grounded DevOps knowledge assistant.

**Next:** M6 introduces orchestration abstractions around the working RAG application.

### M6 — LangChain & Application Orchestration

**Purpose:** compose reusable, testable AI components.

1. Why orchestration
2. LangChain abstractions
3. Models/prompts/output parsers
4. Runnable/chain composition
5. Loaders/splitters
6. Embeddings/vector stores
7. Retrievers/RAG chains
8. Memory vs state vs evidence
9. Tools
10. Retry/fallback/observability
11. DevOps orchestration
12. Orchestrated RAG Assistant

**Setup:** module requirements; Python venv; provider credentials/local model only where required.

**Rule:** framework abstractions must be understood as reusable application plumbing, not magic intelligence.

**Output:** same RAG/agent architecture implemented with reusable components.

**Next:** M7 standardizes capability connectivity through MCP.

### M7 — MCP

**Purpose:** expose tools/resources/prompts through a standardized protocol boundary.

1. MCP fundamentals
2. Host/client/server
3. lifecycle and discovery
4. tools/contracts/schemas
5. resources
6. prompts/sampling/elicitation concepts
7. transports
8. Python MCP server
9. MCP client
10. security/auth/trust boundaries
11. MCP + RAG + LangChain + DevOps
12. DevOps MCP assistant

**Setup:** current Python MCP SDK and module requirements; start with stdio locally, then remote transport only when the lesson requires it.

**Examples:** `get_pipeline_status`, `get_terraform_changes`, `get_aks_status`, runbook resources.

**Output:** standardized, validated, read-only DevOps capability server/client.

**Next:** M8 uses those capabilities inside a persistent stateful workflow.

### M8 — Stateful Agents & LangGraph

**Purpose:** explicit state, routing, loops, checkpointing and approval.

1. Chain vs workflow vs agent
2. Stateful graph mental model
3. State schemas/reducers
4. Nodes/edges/conditional routing
5. Agent loops/planning/tool selection
6. RAG + MCP routing
7. retry/loop limits/termination
8. human approval interrupts
9. checkpoint/persistence/recovery
10. subgraphs/multi-agent introduction
11. production safety/observability/evaluation
12. stateful incident-response agent

**Setup:** module requirements and a local Python environment; checkpoint/storage choice follows the lab.

**Output:** resumable, bounded incident workflow.

**Next:** M9 splits specialized responsibilities across agents.

### M9 — Multi-Agent Systems

**Purpose:** coordinate specialists without creating uncontrolled agent-to-agent behavior.

1. Multi-agent fundamentals
2. supervisor/router/handoff patterns
3. specialization boundaries
4. supervisor + subagents
5. router + parallel specialists
6. handoffs
7. shared/private state and context isolation
8. result/evidence contracts
9. conflict resolution/synthesis
10. RAG/MCP/tools/approval per agent
11. system-level evaluation/observability/cost
12. DevOps incident team

**Setup:** M8 graph environment; multiple specialist prompts/tools; keep writes disabled.

**Example team:** Pipeline Specialist + Terraform Specialist + AKS Specialist + Knowledge/RAG Specialist + Synthesis.

**Output:** coordinated evidence-grounded specialist team.

**Next:** M10 attacks and measures the entire system.

### M10 — Security, Evaluation & Red Teaming

**Purpose:** prove that useful behavior is also bounded and releasable.

1. Threat modelling
2. direct/indirect prompt injection
3. tool abuse/excessive agency
4. sensitive data/secrets/output handling
5. RAG/vector/knowledge attacks
6. MCP capability security
7. multi-agent attack propagation
8. deterministic policy gates
9. evaluation fundamentals
10. adversarial/red-team tests
11. production metrics/release gates
12. secure evaluation harness

**Setup:** no production credentials required for attack labs; use synthetic/sanitized data and read-only tools.

**Output:** repeatable security/evaluation gate with regression tests.

**Next:** M11 maps these controls onto enterprise infrastructure.

### M11 — Enterprise Architecture & Production

**Purpose:** turn the agent into an enterprise platform.

1. enterprise workload architecture
2. Azure landing zones/environment separation
3. identity/RBAC/managed/workload identity
4. private networking/DNS/egress
5. AKS/App Service/Container Apps trade-offs
6. state/evidence/knowledge data layer
7. scale/queues/backpressure
8. HA/DR
9. observability/SRE
10. CI/CD/IaC/promotion
11. governance/FinOps/operations
12. production platform blueprint

**Setup:** architecture labs can be design-only; Azure hands-on should use an approved subscription and least-privilege identities. Never use production credentials in learning labs.

**Output:** production-ready Azure reference architecture.

**Next:** M12 integrates every layer.

### M12 — Final Enterprise Capstone

**Purpose:** build and explain the complete Production DevOps AI Assistant.

1. requirements/definition of done
2. repository/component architecture
3. trusted evidence/tool layer
4. knowledge/RAG layer
5. MCP integration
6. stateful multi-agent graph
7. grounded RCA/validation/confidence
8. security/policy/human approval
9. evaluation/red-team release suite
10. enterprise deployment architecture
11. CI/CD/operations/runbooks
12. final demo/interview/portfolio

**Setup:** begin from the repository's capstone environment; default all writes to simulation/read-only; use synthetic incident data first.

**Final scenario:**

```text
Production AKS deployment fails after Terraform networking change
        ↓
Pipeline + Terraform + AKS evidence
        ↓
RAG reference knowledge
        ↓
MCP capabilities
        ↓
Stateful specialist agents
        ↓
Conflict/gap gate
        ↓
Grounded RCA + citations
        ↓
Security/policy gate
        ↓
Human approval
        ↓
Controlled remediation simulation
        ↓
Post-action verification + audit
```

## 🧪 Practical Standard for Every Module

Every module follows:

```text
1. Read the module README
2. Complete lessons in order
3. Run the matching V1 → V10/V12 practicals
4. Intentionally break one component
5. Inspect logs/evidence/state
6. Identify model-driven vs deterministic behavior
7. Complete the module mini-project
8. Pass the completion checklist
9. Follow the README link into the next module
```

## 🚫 What We Will Not Do

- no unnecessary generic Python detour
- no repeated API/HTTP/JSON tutorials in later modules
- no repeated prompt-engineering basics after M2
- no automatic production writes from model output
- no treating RAG documents as current incident evidence
- no treating structured output as proof of truth
- no unbounded agent loops
- no secret values in prompts, logs or committed files

## 🎓 Completion Standard

The learner should be able to explain not just **what** component is used, but:

```text
Why is it here?
What problem did the previous module leave unsolved?
What trust boundary does it introduce?
What can fail?
What is deterministic?
What is model-driven?
How is it tested?
How does it connect to the capstone?
```

That is the definition of a complete course—not simply finishing 12 modules.
