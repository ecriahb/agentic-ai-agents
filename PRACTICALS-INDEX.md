# Course Practicals Index — Zero to Hero

> This is the **hands-on spine** of the repository. If you are a beginner, do not jump directly to the final V10 scripts. Complete each module's practical ladder in order.

## How to Use Every Practical
For every stage, write down:
1. What problem this version solves
2. What changed from the previous version
3. What input/evidence it consumes
4. What output/status it produces
5. What can fail
6. What control prevents unsafe/incorrect behavior
7. Why the next version is needed

A script is not considered “completed” only because it ran successfully.

---

## Five-Phase Practical Spine

The table below is the learner-facing path. The module roadmaps remain detailed instructions underneath it.

| Phase | Project outcome | Modules |
|---|---|---|
| 1. Understand AI | AI mental models, prompting, evidence, and uncertainty | [Modules 0–2](Module-0/PRACTICAL-ROADMAP.md) |
| 2. Build the first AI application | APIs, structured outputs, retrieval, tools, and grounded generation | [Modules 3–5](Module-3/PRACTICAL-ROADMAP.md) |
| 3. Build agent systems | Orchestration, MCP, state, planning, and specialists | [Modules 6–9](Module-6/PRACTICAL-ROADMAP.md) |
| 4. Secure and operate AI | Security, evaluation, identity, observability, and reliability | [Modules 10–11](Module-10/PRACTICAL-ROADMAP.md) |
| 5. Ship the AI platform | Integrated production agent system using a DevOps case study | [Module 12](Module-12/PRACTICAL-ROADMAP.md) |

To inspect each internal step, use the module roadmaps below:

| Module group | Detailed roadmaps |
|---|---|
| Foundation | [Module 0](Module-0/PRACTICAL-ROADMAP.md), [Module 1](Module-1/PRACTICAL-ROADMAP.md), [Module 2](Module-2/PRACTICAL-ROADMAP.md) |
| Application | [Module 3](Module-3/PRACTICAL-ROADMAP.md), [Module 4](Module-4/PRACTICAL-ROADMAP.md), [Module 5](Module-5/PRACTICAL-ROADMAP.md) |
| Agents | [Module 6](Module-6/PRACTICAL-ROADMAP.md), [Module 7](Module-7/PRACTICAL-ROADMAP.md), [Module 8](Module-8/PRACTICAL-ROADMAP.md), [Module 9](Module-9/PRACTICAL-ROADMAP.md) |
| Operations | [Module 10](Module-10/PRACTICAL-ROADMAP.md), [Module 11](Module-11/PRACTICAL-ROADMAP.md), [Module 12](Module-12/PRACTICAL-ROADMAP.md) |

---

# Difficulty Ladder Used Everywhere

```text
ZERO
Understand the problem manually
        ↓
BASIC
Run one isolated concept
        ↓
BUILD
Combine two or three concepts
        ↓
CONTROL
Add validation / evidence / policy
        ↓
FAILURE DRILL
Break it intentionally
        ↓
ADVANCED
Add state / tools / retrieval / coordination
        ↓
PROVIDER PARITY
Run appropriate model-dependent stage with Ollama and OpenAI
        ↓
V10 / HERO
Integrated module project
```

---

# Provider Rule

Not every practical needs an LLM. Deterministic concepts should remain deterministic.

When an LLM is actually required, the repository teaches both:

```text
Ollama / Local LLM
and
OpenAI API
```

Provider switching must not alter:
- evidence rules
- source IDs
- authorization
- tool allowlists
- validation
- approval requirements
- release gates

See [MODEL-PROVIDERS.md](MODEL-PROVIDERS.md) and [DUAL-PROVIDER-LABS.md](DUAL-PROVIDER-LABS.md).

---

# The One Incident That Evolves Through the Course

```text
Terraform Apply starts
       ↓
NSG rule aks-subnet-allow removed
       ↓
AKS network validation degrades/fails
       ↓
Deployment fails
```

The point is not to memorize this root cause. The point is to see the **same incident** evolve through:

```text
Prompt
→ API
→ Tool
→ Evidence
→ Embeddings
→ RAG
→ LangChain
→ MCP
→ StateGraph
→ Multi-Agent
→ Security/Eval
→ Enterprise Architecture
→ Final Capstone
```

---

# Completion Standard

A learner is ready to move to the next module only when they can answer:

- What did I build?
- Why was the previous version insufficient?
- What can this version still get wrong?
- Which part is deterministic and which part uses an LLM?
- What happens when evidence is missing?
- What happens when the model/tool/provider fails?
- Who owns authorization and execution?

That is the repository's meaning of **Zero to Hero**.
