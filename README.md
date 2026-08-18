# 🚩 Agentic AI for DevOps Engineers

> **From Zero to Production-Grade DevOps AI Agents**

This repository is a hands-on, module-by-module course for learning how to design and build **Agentic AI systems for real DevOps use cases**.

The course deliberately does not jump from “LLM” directly to “autonomous agent.” Each module adds one engineering layer and keeps earlier trust/safety principles intact.

---

# 👶 Completely New to AI? Start Here

If you are a complete beginner, start with [`START-HERE.md`](START-HERE.md).

Supporting guides:

- [`PRACTICALS-INDEX.md`](PRACTICALS-INDEX.md) — hands-on spine
- [`PREREQUISITES.md`](PREREQUISITES.md) — setup checklist
- [`MODEL-PROVIDERS.md`](MODEL-PROVIDERS.md) — local vs hosted provider guide
- [`DUAL-PROVIDER-LABS.md`](DUAL-PROVIDER-LABS.md) — provider-parity labs
- [`COURSE-AUDIT.md`](COURSE-AUDIT.md) — repository/content audit
- [`COURSE-SIMPLIFICATION-PLAN.md`](COURSE-SIMPLIFICATION-PLAN.md) — current deduplication plan

## 🧹 New: Lean Learning Spine

The repository has grown substantially. To prevent repeated teaching, the current feature branch establishes **canonical ownership** for each concept.

```text
M0  AI / LLM Foundation
 ↓
M1  LLM Application + Tools + First DevOps Agent
 ↓
M2  Prompt + Context Engineering
 ↓
M3  API + Minimal Python + Reliable LLM Integration
 ↓
M4  Embeddings + Vector Search
 ↓
M5  RAG + Grounding
 ↓
M6  LangChain / Orchestration
 ↓
M7  MCP / Standardized Capabilities
 ↓
M8  Stateful Agents / LangGraph
 ↓
M9  Multi-Agent Systems
 ↓
M10 Security + Evaluation + Red Teaming
 ↓
M11 Enterprise Architecture + Production
 ↓
M12 Final Capstone
```

**Important:** later modules should apply earlier concepts rather than reteach their fundamentals.

The first four modules now explicitly define the canonical learning path in their READMEs. Older standalone lesson files are being retained during migration so existing links do not break; they are not automatically additional mandatory chapters.

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

| Module | Focus |
|---|---|
| [Module 0](Module-0/README.md) | AI & LLM Foundation |
| [Module 1](Module-1/README.md) | LLM APIs, Tools & First DevOps Agent |
| [Module 2](Module-2/README.md) | Prompt & Context Engineering |
| [Module 3](Module-3/README.md) | APIs & Minimal Python for AI |
| [Module 4](Module-4/README.md) | Embeddings & Vector Databases |
| [Module 5](Module-5/README.md) | Retrieval-Augmented Generation (RAG) |
| [Module 6](Module-6/README.md) | LangChain & AI Application Orchestration |
| [Module 7](Module-7/README.md) | Model Context Protocol (MCP) |
| [Module 8](Module-8/README.md) | Stateful Agents & LangGraph |
| [Module 9](Module-9/README.md) | Multi-Agent Systems |
| [Module 10](Module-10/README.md) | Agent Security, Evaluation & Red Teaming |
| [Module 11](Module-11/README.md) | Enterprise Architecture & Production |
| [Module 12](Module-12/README.md) | Final Enterprise Project |

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

Early modules teach how to understand and control this evidence. Later modules add:

```text
Tool Contracts
→ Evidence Preservation
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
Capstone       → integrate everything
```

---

# 🤖 Model Provider Parity

Provider-specific code should never replace application safety.

```text
Local learning route  → Ollama
Hosted API route      → OpenAI
```

The provider can change, but the engineering contract remains:

```text
Evidence → Context → Model → Validation → Policy
```

---

# 🧪 Practical Philosophy — Zero to Hero

Practicals remain the primary learning spine. Use [`PRACTICALS-INDEX.md`](PRACTICALS-INDEX.md) and the relevant module roadmap.

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

A practical is not complete because the script ran. You should be able to explain what changed, what can fail, what is model-driven vs deterministic, what evidence is trusted and what control blocks unsafe behavior.

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

# 🚀 Recommended Study Rule

For every module:

```text
Follow the canonical README sequence
 ↓
Run the matching practical
 ↓
Break one thing intentionally
 ↓
Explain the trust boundary
 ↓
Move on
```

If a later lesson starts explaining an earlier foundation again, treat it as an application example unless the module README explicitly marks it as a new capability.

---

# 🎓 Final Portfolio Statement

After completing the course, the project can be described as:

> **An evidence-grounded DevOps AI incident investigation platform using controlled read-only tools, RAG, MCP, stateful multi-agent orchestration, deterministic security policy, human approval, evaluation/red teaming and an enterprise Azure production architecture.**

🚩 **Jai Bajrangbali — Learn • Build • Break • Validate • Secure • Operate**
