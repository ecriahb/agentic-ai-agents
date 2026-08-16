# Module 1 — C: Interview & Revision Sheet

> **Goal:** Module 1 concepts ko concise but technically correct interview language me revise karna.

## One-line definitions

**API:** A contract/interface through which software systems communicate.

**SDK:** A language-specific library that simplifies calling a provider/service API.

**API Key:** A credential used to authenticate/identify an application request.

**LLM:** A language model that predicts/generates text from context; it is not a guaranteed truth source.

**Ollama:** A local runtime for running supported language models and exposing them through a local API.

**Token:** A model-processing unit derived from text/code.

**Context Window:** The finite token budget a model can consider during a request.

**Structured Output:** A model response constrained to a defined machine-readable shape.

**Tool Calling:** A mechanism where the model requests a typed external capability; the host validates and executes it.

**Agent:** A bounded application loop that decides, acts through allowed tools, observes results, updates state and continues/stops according to policy.

**Evidence:** A validated observation with provenance used to support factual claims.

## Most important distinctions

```text
ChatGPT UI != API
SDK != API itself
API key != model
create response != create model
Local LLM != trusted LLM
Cloud LLM != trusted LLM
Schema-valid != factually correct
Tool request != execution authority
Tool schema != authorization
Agent state != model memory
Tool failure != negative evidence
No evidence != permission to guess
```

## Core architecture answer
If interviewer asks “How would you build a safe DevOps AI agent?”

```text
Incident
→ Host application validates input
→ LLM proposes read-only investigation
→ Host validates tool name/args/target
→ Tools collect current evidence
→ Evidence stored with source/provenance
→ LLM generates grounded RCA
→ Schema/citation/business rules validate result
→ Policy controls next action
→ Risky writes require authorization + approval
```

## Common interview Q&A

### Q1. ChatGPT UI aur API me difference?
UI human-facing product interaction hai. API software-to-software integration hai where application controls prompts, context, tools, validation and workflow.

### Q2. `client.responses.create()` kya karta hai?
Existing model se response generation request create karta hai; new model train/create nahi karta.

### Q3. Ollama ka use kyun?
Local learning/inference, no per-call hosted bill, privacy/control and provider-independence practice. Trade-off is local hardware/capability/operations.

### Q4. Token aur context window kyun important?
They affect how much information model can process, latency, noise and hosted usage/cost.

### Q5. Structured output ka main limitation?
It validates shape/types but does not prove factual correctness.

### Q6. Tool calling me actual function kaun execute karta hai?
Host/application code. Model only produces a request/proposal.

### Q7. Model-generated tool args directly execute kyun nahi karne chahiye?
They are untrusted input and can be invalid, unauthorized, dangerous or hallucinated.

### Q8. Agent aur chain me difference?
A simple chain follows predetermined composition. An agent can dynamically decide next action/tool within explicit state, loop and stop policies.

### Q9. Evidence grounding kya hai?
Final claims ko validated source observations se support karna instead of relying on model memory/confidence.

### Q10. No evidence case me kya karoge?
Return explicit insufficient-evidence status and ask/collect more evidence; do not force an RCA.

### Q11. Read-only first kyun?
Investigation capabilities have lower blast radius. Write/remediation needs stronger authorization, approval, idempotency and audit controls.

### Q12. Confidence model se lena safe hai?
Not by itself. Production confidence should be calibrated/deterministic using evidence quality, source independence, conflicts and evaluation data.

## Rapid revision mental model

```text
Model thinks
Host decides policy
Tool observes/acts
Evidence supports facts
Schema shapes output
Validator checks trust
```

## 10-minute self-test
Without notes explain:

1. UI vs API
2. venv and `.env`
3. OpenAI cloud setup
4. Ollama setup
5. response object
6. tokens/context/cost
7. structured output limitation
8. tool request flow
9. agent loop
10. trusted RCA architecture

## Practical viva
Open `devops_agent_v4.py` or final real-tool lab and point out:

- model call
- tool request
- tool dispatcher
- evidence store
- validation
- stop condition
- final RCA generation

If learner cannot identify these in code, revision is not complete.

## Module 1 final rule

> **LLM reasoning is useful, but authority stays with evidence, host validation, policy and controlled execution.**