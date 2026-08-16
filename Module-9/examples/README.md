# Module 9 Practicals — Multi-Agent Systems for DevOps AI

These labs intentionally grow one concept at a time. Run V1→V10 in order.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For V10, start local Ollama and make sure the course model is available:

```bash
ollama run qwen2.5:3b
```

## Practical Progression

| Version | File | Concept |
|---|---|---|
| V1 | `01_two_specialists.py` | Separate specialist responsibilities |
| V2 | `02_router.py` | Bounded router dispatch |
| V3 | `03_parallel_specialists.py` | Parallel fan-out/fan-in |
| V4 | `04_supervisor.py` | Multi-step supervisor coordination |
| V5 | `05_shared_evidence_contract.py` | Shared normalized evidence |
| V6 | `06_private_context_handoff.py` | Minimal-context handoff |
| V7 | `07_conflict_resolution.py` | Provenance/freshness-based conflict handling |
| V8 | `08_capability_routing.py` | Per-agent capability policy |
| V9 | `09_approval_checkpoint.py` | Human approval + checkpoint/resume |
| V10 | `10_multi_agent_devops_team.py` | Full multi-agent incident team |

## V1 → V10 Mental Model

```text
Specialists
  ↓
Router
  ↓
Parallel Agents
  ↓
Supervisor
  ↓
Evidence Contract
  ↓
Private Context / Handoff
  ↓
Conflict Resolution
  ↓
Capability Scoping
  ↓
Approval + Persistence
  ↓
Final Multi-Agent DevOps Team
```

## Final V10 Flow

```text
Incident
 ↓
Input Validation
 ↓
Agent Selection
 ↓
Pipeline / Terraform / AKS Specialists
 ↓
Evidence Merge
 ↓
Conflict Gate
 ↓
Reference Knowledge
 ↓
Ollama/Qwen Synthesis
 ↓
Citation Validation
 ↓
Remediation Proposal
 ↓
Human Approval Interrupt
 ↓
Safe Final Status
```

## Expected Learning Evidence

```text
E1 → Deployment failed during Terraform Apply
E2 → NSG rule aks-subnet-allow was removed
E3 → AKS network connectivity validation degraded
R1 → AKS networking reference
R2 → Terraform networking reference
```

## Safety Design

All specialist integrations in this module are deterministic local/read-only simulations.

```text
READ evidence → allowed
PROPOSE remediation → allowed after validation
EXECUTE real Azure change → not implemented
```

Even the final approval path returns a demonstration status rather than changing infrastructure.

## Failure Tests

Modify/test intentionally:

```text
1. Unknown environment
2. Unknown cluster
3. Router selects no known domain
4. Duplicate evidence IDs
5. Specialist raises exception
6. Conflicting observation timestamps
7. Remove E3 before synthesis
8. LLM returns unknown citation [E99]
9. Stop Ollama
10. Reject approval
```

Record expected vs actual state for every test.

## Suggested Evaluation Sheet

```text
Case
Expected agents
Actual agents
Expected evidence
Actual evidence
Conflict status
RCA grounded?
Citation valid?
Approval required?
Final status
```

## Key Principle

```text
Multi-agent reliability does not come from agents agreeing.
It comes from scoped capabilities, explicit state, source-backed evidence,
conflict policy, deterministic validation and controlled authority.
```
