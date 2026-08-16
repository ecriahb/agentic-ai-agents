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

## Practical Progression

| Module | Zero-to-Hero Practical Roadmap | End Skill |
|---|---|---|
| 0 | [Module 0 Practical Roadmap](Module-0/PRACTICAL-ROADMAP.md) | Understand AI/LLM behavior, context, hallucination and safety without coding pressure |
| 1 | [Module 1 Practical Roadmap](Module-1/PRACTICAL-ROADMAP.md) | First OpenAI/Ollama calls → evidence-grounded first DevOps agent |
| 2 | [Module 2 Practical Roadmap](Module-2/PRACTICAL-ROADMAP.md) | Weak prompts → testable DevOps prompt system |
| 3 | [Module 3 Practical Roadmap](Module-3/PRACTICAL-ROADMAP.md) | HTTP/JSON/secrets → robust dual-provider AI application |
| 4 | [Module 4 Practical Roadmap](Module-4/PRACTICAL-ROADMAP.md) | Vector intuition → searchable DevOps knowledge base |
| 5 | [Module 5 Practical Roadmap](Module-5/PRACTICAL-ROADMAP.md) | Retrieval → grounded RAG + citations + abstention |
| 6 | [Module 6 Practical Roadmap](Module-6/PRACTICAL-ROADMAP.md) | Raw components → LangChain orchestration |
| 7 | [Module 7 Practical Roadmap](Module-7/PRACTICAL-ROADMAP.md) | First MCP server → live evidence-grounded MCP assistant |
| 8 | [Module 8 Practical Roadmap](Module-8/PRACTICAL-ROADMAP.md) | StateGraph → bounded stateful DevOps agent |
| 9 | [Module 9 Practical Roadmap](Module-9/PRACTICAL-ROADMAP.md) | Specialists → controlled multi-agent DevOps team |
| 10 | [Module 10 Practical Roadmap](Module-10/PRACTICAL-ROADMAP.md) | Threat model → red-team/eval/release gate |
| 11 | [Module 11 Practical Roadmap](Module-11/PRACTICAL-ROADMAP.md) | App code → enterprise production-readiness architecture |
| 12 | [Module 12 Practical Roadmap](Module-12/PRACTICAL-ROADMAP.md) | Individual layers → final Production DevOps AI Assistant |

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
