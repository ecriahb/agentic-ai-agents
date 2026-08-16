# 🚩 Agentic AI for Azure DevOps Engineers

> **From AI foundations → evidence-grounded agents → secure enterprise DevOps AI systems**

This repository is a hands-on, module-by-module course for learning how to design and build **Agentic AI systems for real DevOps use cases**.

The course deliberately does not jump from “LLM” directly to “autonomous agent.” Each module adds one engineering layer and keeps earlier trust/safety principles intact.

---

# 👶 Completely New to AI? Start Here

If you are a complete beginner, do **not** jump directly into LangChain, MCP or agents.

## 👉 [START-HERE.md](START-HERE.md)

Then use these supporting guides:

- [PRACTICALS-INDEX.md](PRACTICALS-INDEX.md) — **the hands-on Zero → Hero spine for every Module 0–12**
- [PREREQUISITES.md](PREREQUISITES.md) — Python 3.10+, virtual environment, Ollama/OpenAI setup checklist
- [MODEL-PROVIDERS.md](MODEL-PROVIDERS.md) — Ollama local vs OpenAI hosted provider guide
- [DUAL-PROVIDER-LABS.md](DUAL-PROVIDER-LABS.md) — exactly where to run the same concepts on both providers
- [COURSE-AUDIT.md](COURSE-AUDIT.md) — detailed Module 0–12 content/practical/provider audit and limitations

Beginner preflight:

```powershell
pip install -r shared/requirements.txt
python shared/preflight.py
python shared/provider_smoke_test.py
```

The repository supports two learning paths:

```text
Track A → Ollama / Local LLM
Track B → OpenAI API
```

The model provider may change, but the engineering contract does not:

```text
Evidence → Context → Model → Validation → Policy
```

---

# 🎯 Final Course Goal

Build a **Production DevOps AI Assistant** that can:

```text
Incident / Pipeline Failure
        ↓
Collect Trusted Current Evidence
        ↓
Retrieve Approved Reference Knowledge
        ↓
Coordinate Specialist Agents
        ↓
Generate Evidence-Grounded RCA
        ↓
Validate Claims / Citations
        ↓
Recommend Safest Next Action
        ↓
Policy + Authorization
        ↓
Human Approval for Risky Write
        ↓
Controlled / Audited Execution Path
```

Core principle:

> **LLM reasoning is never treated as authority. Evidence, authorization, policy, validation and execution remain application-controlled.**

---

# 📚 Complete Course Roadmap — Module 0 to Module 12

> **Status below means repository content is available. It does not imply every module has already been personally studied/completed.**

| Module | Focus | Repository Content |
|---|---|---|
| [Module 0](Module-0/README.md) | AI & LLM Foundation | ✅ Available |
| [Module 1](Module-1/README.md) | APIs, Local Models, Tools & First DevOps Agent | ✅ Available |
| [Module 2](Module-2/README.md) | Prompt & Context Engineering for DevOps AI | ✅ Available |
| [Module 3](Module-3/README.md) | APIs & Python for AI Applications | ✅ Available |
| [Module 4](Module-4/README.md) | Embeddings & Vector Databases | ✅ Available |
| [Module 5](Module-5/README.md) | Retrieval-Augmented Generation (RAG) for DevOps | ✅ Available |
| [Module 6](Module-6/README.md) | LangChain & AI Application Orchestration | ✅ Available |
| [Module 7](Module-7/README.md) | Model Context Protocol (MCP) for DevOps AI | ✅ Available |
| [Module 8](Module-8/README.md) | Stateful Agents & LangGraph Workflows | ✅ Available |
| [Module 9](Module-9/README.md) | Multi-Agent Systems for DevOps AI | ✅ Available |
| [Module 10](Module-10/README.md) | Agent Security, Evaluation & Red Teaming | ✅ Available |
| [Module 11](Module-11/README.md) | Enterprise DevOps AI Architecture & Production Deployment | ✅ Available |
| [Module 12](Module-12/README.md) | Final Enterprise Project — Production DevOps AI Assistant | ✅ Available |

---

# 🧠 Full Learning Progression

```text
Module 0
AI / LLM Fundamentals
        ↓
Module 1
Tools + Evidence + First DevOps Agent
        ↓
Module 2
Prompt + Context Engineering
        ↓
Module 3
APIs + Minimal Python
        ↓
Module 4
Embeddings + Vector Search
        ↓
Module 5
RAG + Grounding + Citations
        ↓
Module 6
LangChain / Orchestration
        ↓
Module 7
MCP / Standardized Capabilities
        ↓
Module 8
Stateful Agents / LangGraph
        ↓
Module 9
Multi-Agent Systems
        ↓
Module 10
Security + Evaluation + Red Teaming
        ↓
Module 11
Enterprise Azure Architecture / Operations
        ↓
Module 12
Production DevOps AI Assistant Capstone
```

---

# 🔥 The Incident That Evolves Through the Course

A recurring practical scenario makes the progression easy to understand:

```text
Pipeline started
      ↓
Terraform Apply started
      ↓
NSG rule `aks-subnet-allow` removed
      ↓
AKS network connectivity validation degraded/failed
      ↓
Deployment failed
```

Early modules teach how to read and reason about this evidence. Later modules progressively add:

```text
Tool Contracts
→ Evidence Preservation
→ Structured RCA
→ Prompt/Context Controls
→ RAG
→ Orchestration
→ MCP
→ Stateful Graph
→ Specialist Agents
→ Security/Evals
→ Enterprise Deployment
```

---

# 🏗️ Final Capstone Architecture

```text
                         USER / INCIDENT API
                                ↓
                        AuthN + Input Policy
                                ↓
                      Stateful Supervisor Graph
                                ↓
        ┌───────────────────────┼───────────────────────┐
        ↓                       ↓                       ↓
 Pipeline Specialist     Terraform Specialist      AKS Specialist
        ↓                       ↓                       ↓
      [E1]                    [E2]                    [E3]
        └───────────────────────┼───────────────────────┘
                                ↓
                         Evidence Contract
                                ↓
                       Knowledge / RAG [R*]
                                ↓
                      Conflict + Evidence Gate
                                ↓
                         Grounded LLM RCA
                                ↓
                    Citation / Claim Validation
                                ↓
                       Security / Policy Gate
                                ↓
                     Remediation Action Proposal
                                ↓
                       HUMAN APPROVAL GATE
                                ↓
                      Isolated Write Executor
                                ↓
                     Post-Action Verification
                                ↓
                      Final Audit / Observability
```

The learning implementation keeps production writes simulated/read-only by default.

---

# 🔐 Trust Model Used Throughout the Repository

```text
USER INPUT              = untrusted
RAG DOCUMENT             = untrusted reference data
MCP RESOURCE             = external data
TOOL REQUEST FROM LLM    = untrusted proposal
TOOL OUTPUT              = evidence only with provenance
MODEL OUTPUT             = untrusted analysis/proposal
AUTHORIZATION            = trusted external decision
POLICY                    = deterministic host control
HUMAN APPROVAL            = explicit risk gate
EXECUTOR                  = isolated known implementation
```

---

# 🧩 What Each Major Layer Solves

```text
Tools          → obtain current evidence
Prompting      → guide reasoning
APIs           → connect systems
Embeddings     → semantic representation
RAG            → retrieve approved reference knowledge
LangChain      → compose reusable application components
MCP            → standardize capability connectivity
LangGraph      → explicit state, routing, loops and pause/resume
Multi-Agent    → specialist decomposition and coordination
Security/Evals → prove boundaries and prevent regression
Enterprise Arch→ identity, network, state, scale, HA/DR, operations
Capstone       → integrate everything into one system
```

---

# 🤖 Model Provider Parity

Provider-specific code should never replace application safety.

The course therefore treats providers as swappable components:

```text
Local learning route  → Ollama
Hosted API route      → OpenAI
```

Provider-parity examples are added to the relevant modules so the learner can run the same concept on both paths.

Important:

```text
OpenAI/Ollama = generation provider
Evidence      = source of current facts
Host code     = policy/execution owner
```

See [DUAL-PROVIDER-LABS.md](DUAL-PROVIDER-LABS.md).

---

# 🧪 Practical Philosophy — Zero to Hero

**Practicals are the primary learning spine of this repository.** Use [PRACTICALS-INDEX.md](PRACTICALS-INDEX.md) and complete every module's `PRACTICAL-ROADMAP.md` sequentially.

```text
ZERO
Understand manually
   ↓
BASIC
Run one isolated concept
   ↓
BUILD
Combine concepts
   ↓
CONTROL
Add validation/evidence/policy
   ↓
FAILURE DRILL
Break it intentionally
   ↓
ADVANCED
Add retrieval/tools/state/coordination
   ↓
PROVIDER PARITY
Use Ollama and OpenAI where an LLM is actually required
   ↓
V10 / HERO
Integrated module project
```

A practical is **not complete because the script ran**. The learner must be able to explain:
- what changed from the previous version
- what can fail
- what is model-driven vs deterministic
- what evidence is trusted
- what control blocks unsafe behavior
- why the next version exists

Module 0 uses no-code experiments because the learner should understand the mental model before coding. Module 11 uses architecture simulations/checkers because identity, network, state, HA/DR and governance are provider-independent engineering concerns.

---

# 🛡️ Core Engineering Principles

```text
1. LLM is a reasoner, not an authority.
2. Application code executes capabilities.
3. Model tool calls are untrusted requests.
4. Tool names, arguments and targets must be validated.
5. Tool output becomes evidence only with provenance.
6. No evidence should mean no forced RCA.
7. RAG reference knowledge is not current incident evidence.
8. Structured output validates shape, not truth.
9. Conversation memory is not workflow state or authorization.
10. MCP discovery is not permission.
11. Agent-to-agent messages are not trusted evidence.
12. Agent loops must be bounded.
13. High-risk writes require deterministic policy + authorization + approval.
14. Secrets should remain outside model context whenever possible.
15. Evaluate trajectories, retrieval, tools and final answers.
16. Red-team findings become permanent regression tests.
17. Critical security failures block releases.
18. Production agents require identity, private networking, durable state, observability, HA/DR and FinOps.
```

---

# 🚀 Recommended Study Order

Follow the modules sequentially. Even if you already know Azure/DevOps, avoid skipping the trust foundations in Modules 1–5; Modules 7–12 assume you understand evidence, grounding and host-controlled execution.

For each module:

```text
Read lesson
 ↓
Open that module's PRACTICAL-ROADMAP.md
 ↓
Run/perform current practical stage
 ↓
Change one input
 ↓
Break it intentionally
 ↓
Explain expected vs actual behavior
 ↓
Continue lesson-by-lesson
 ↓
Complete V10 / module project
 ↓
Revision + interview questions
```

---

# 🎓 Final Portfolio Statement

After completing the course, the project can be described as:

> **An evidence-grounded DevOps AI incident investigation platform using controlled read-only tools, RAG, MCP, stateful multi-agent orchestration, deterministic security policy, human approval, evaluation/red teaming and an enterprise Azure production architecture.**

---

🚩 **Jai Bajrangbali — Learn • Build • Break • Validate • Secure • Operate**
