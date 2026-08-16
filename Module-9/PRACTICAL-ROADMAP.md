# Module 9 — Zero-to-Hero Practical Roadmap

> Goal: single-agent workflow ko multiple bounded specialists me split karna without turning agent opinions into truth.

## V1 — Two Specialists
Run `examples/01_two_specialists.py`.

Compare specialist scope and outputs.

## V2 — Router
Run `02_router.py`.

Change incident wording and predict selected specialist before running.

## V3 — Parallel Specialists
Run `03_parallel_specialists.py`.

Measure conceptual benefit: independent evidence collection can run in parallel; final merge still needs validation.

## V4 — Supervisor
Run `04_supervisor.py`.

Trace who chooses the next specialist and what context is shared.

## V5 — Shared Evidence Contract
Run `05_shared_evidence_contract.py`.

Inspect required fields such as evidence ID, source, claim and payload.

**Rule:** agent narrative alone is not evidence.

## V6 — Private Context + Handoff
Run `06_private_context_handoff.py`.

Observe what should stay specialist-private vs what is safe to hand off.

## V7 — Conflict Resolution
Run `07_conflict_resolution.py`.

Create disagreement between specialists.

Expected: inspect source/freshness/authority; do not majority-vote the root cause.

## V8 — Capability Routing
Run `08_capability_routing.py`.

Try requesting an out-of-scope capability from a specialist. Expected: policy block.

## V9 — Approval + Checkpoint
Run `09_approval_checkpoint.py`.

Test pause, reject and approve states. No real production write should happen.

## V10 — Multi-Agent DevOps Team
Run `10_multi_agent_devops_team.py`.

Trace:
`Router/Supervisor → Specialists → Evidence Merge → Conflict Gate → Knowledge → Synthesis → Validation → Approval`.

## Provider Bonus
Run `11_dual_provider_multi_agent_synthesis.py` with Ollama and OpenAI.

**Pass:** specialist evidence stays identical; only synthesis model changes.

### Failure Drills
- one specialist unavailable
- contradictory evidence
- duplicated evidence IDs
- wrong specialist routing
- unauthorized capability request

### Acceptance Criteria
Learner can explain why `More agents != more truth` and why evidence contracts + scoped capabilities matter.

## Hero Outcome
Learner can design a multi-agent DevOps team whose coordination is explicit, testable and evidence-driven.
