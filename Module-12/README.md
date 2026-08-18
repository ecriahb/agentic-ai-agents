# 🚩 Module 12 — Final Enterprise Project: Production DevOps AI Assistant

> **Build the complete evidence-grounded, stateful, multi-agent, MCP-enabled, security-gated and production-architected DevOps AI Assistant.**

M12 is not a new technology module. It is the integration and portfolio module for everything learned in M0–M11.

## 🔗 Full Dependency

```text
M0 foundations
 ↓
M1 tools + evidence
 ↓
M2 prompt/context
 ↓
M3 APIs + Python
 ↓
M4 embeddings/search
 ↓
M5 RAG
 ↓
M6 orchestration
 ↓
M7 MCP
 ↓
M8 stateful graph
 ↓
M9 multi-agent
 ↓
M10 security/evaluation
 ↓
M11 enterprise architecture
 ↓
M12 CAPSTONE
```

## 🎯 Final Mission

Build an assistant for an incident such as:

```text
Production AKS deployment started failing after a Terraform networking change.
Investigate, produce an evidence-grounded RCA, recommend the safest next action,
and require approval before any write.
```

The assistant must not guess, execute arbitrary commands or treat model output as authority.

## 📚 12 Capstone Stages

| # | Stage | Output |
|---|---|---|
| 01 | Requirements & Definition of Done | project contract |
| 02 | Repository & Component Architecture | clean boundaries |
| 03 | Trusted Evidence & Tool Layer | read-only tools |
| 04 | Knowledge/RAG Layer | reference retrieval |
| 05 | MCP Integration | standardized capabilities |
| 06 | Stateful Multi-Agent Graph | investigation workflow |
| 07 | Grounded RCA & Validation | claims/citations/confidence |
| 08 | Security, Policy & Approval | controlled authority |
| 09 | Evaluation & Red-Team Suite | release gate |
| 10 | Enterprise Deployment Architecture | Azure blueprint |
| 11 | CI/CD, Operations & Runbooks | operational readiness |
| 12 | Final Demo & Portfolio | interview-ready story |

## 🛠️ Recommended Setup

Start locally with synthetic incident data and read-only tools.

```text
Python venv
  ↓
Local LLM / approved provider
  ↓
Local vector store
  ↓
MCP server/client
  ↓
Stateful graph
  ↓
Evaluation suite
```

Only after the local system is reproducible should you map the design to Azure infrastructure from M11.

## 🧠 Final Architecture

```text
Incident API
   ↓
Auth + Input Policy
   ↓
Supervisor Graph
   ↓
Pipeline / Terraform / AKS specialists
   ↓
Evidence Contract
   ↓
RAG Knowledge Agent
   ↓
Conflict / Gap Gate
   ↓
Grounded Synthesis
   ↓
Claim + Citation Validator
   ↓
Security / Policy Engine
   ↓
Remediation Proposal
   ↓
HUMAN APPROVAL
   ↓
Isolated Write Executor
   ↓
Post-action Verification
   ↓
Final Status + Audit
```

Learning implementation keeps write execution simulated/read-only by default.

## 🧪 Practical Progression

```text
V1 project contract
V2 read-only evidence tools
V3 RAG retrieval
V4 source-labelled context
V5 supervisor + specialists
V6 conflict/gap gate
V7 grounded RCA
V8 policy + approval simulation
V9 security/eval release gate
V10 production architecture + final demo
```

## ✅ Definition of Done

- [ ] current facts come from trusted evidence
- [ ] reference knowledge is labelled separately
- [ ] tools/MCP are allowlisted and arguments validated
- [ ] state supports graph transitions/checkpoint design
- [ ] specialists have scoped responsibilities
- [ ] evidence gaps/conflicts are explicit
- [ ] citations reference known source IDs only
- [ ] unsupported claims cause validation failure/abstention
- [ ] model output cannot directly perform production writes
- [ ] authorization and human approval are separate gates
- [ ] red-team/eval suite can block release
- [ ] Azure identity/network/state/observability design is documented
- [ ] final demo is reproducible locally

## 🎓 Portfolio Story

The final interview narrative should be:

> **I built an evidence-grounded DevOps investigation system—not a chatbot—with controlled tools, RAG, MCP, stateful multi-agent orchestration, deterministic policy, human approval, evaluation/red teaming and enterprise Azure architecture.**

## 🔗 Navigation

⬅️ [Module 11 — Enterprise Architecture](../Module-11/README.md)

📚 [Full Course Curriculum Map](../COURSE-CURRICULUM.md)

🏠 [Course README](../README.md)
