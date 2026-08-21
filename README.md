# 🚩 Agentic AI for DevOps Engineers

> **From Zero to Production-Grade DevOps AI Agents**

This repository is a hands-on, five-phase course for learning how to design and build **production-grade Agentic AI systems**. DevOps is the application domain and running case study; the core subject is AI engineering: models, context, tools, agents, retrieval, evaluation, security, and operations. The 13 modules are internal steps inside those phases, not 13 separate courses.

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

Build a **production AI assistant for DevOps operations** that can:

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

# 📚 Five-Phase Learning Path

Follow the phases in order. Each phase upgrades the same AI system; the DevOps incident is the running case study.

| Phase | Learner outcome | Internal modules |
|---|---|---|
| 1. Understand AI | Models, context, hallucination, prompting, and safe AI mental models | [Modules 0–2](Module-0/README.md) |
| 2. Build the First AI Application | Provider APIs, structured outputs, retrieval, tools, and grounded generation | [Modules 3–5](Module-3/README.md) |
| 3. Build Agent Systems | Orchestration, MCP, state, planning, and multi-agent coordination | [Modules 6–9](Module-6/README.md) |
| 4. Secure and Operate AI | Evaluation, red teaming, identity, observability, governance, and reliability | [Modules 10–11](Module-10/README.md) |
| 5. Ship the AI Platform | An integrated production agent system demonstrated through a DevOps incident | [Module 12](Module-12/README.md) |

Use the module links inside each phase when you need a specific lesson. Do not treat moving from one module to the next as starting a new subject; each one adds a layer to the same assistant.

---

# 🧠 One Assistant, Five Upgrades

```text
Phase 1
Understand AI and evidence
        ↓
Phase 2
Build the first grounded assistant
        ↓
Phase 3
Add tools, state, and agents
        ↓
Phase 4
Secure and operate the platform
        ↓
Phase 5
Ship the production assistant
        ↓
One evolving Enterprise DevOps AI Platform
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
