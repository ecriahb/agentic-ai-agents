# Module 12 — Zero-to-Hero Practical Roadmap

> Goal: Module 1–11 ke concepts ko one final enterprise DevOps AI Assistant me incrementally assemble karna.

## V1 — Project Contract
Run `examples/01_project_contract.py`.

Define what the assistant **can**, **cannot**, **must** and **must never** do.

## V2 — Trusted Evidence Tools
Run `02_evidence_tools.py`.

Collect E1/E2/E3 using allowlisted read-only tools.

## V3 — Reference Knowledge
Run `03_reference_knowledge.py`.

Retrieve R1/R2 and explain why runbook guidance is not proof of current incident state.

## V4 — Source-Labeled Context
Run `04_source_context.py`.

Build explicit `CURRENT EVIDENCE` and `REFERENCE KNOWLEDGE` sections.

## V5 — Specialist Team
Run `05_specialist_team.py`.

Pipeline/Terraform/AKS specialists produce scoped results; do not treat specialist prose as evidence unless backed by source IDs.

## V6 — Conflict + Gap Gate
Run `06_conflict_gap_gate.py`.

Test missing E2 and conflicting observations. Expected: block/low-confidence path rather than forced RCA.

## V7 — Grounded RCA
Run `07_grounded_rca.py`.

Check source IDs, missing-evidence behavior and host-calculated confidence.

## V8 — Policy + Human Approval
Run `08_policy_approval.py`.

Test production write proposal with approval false/true. Learning version remains non-destructive.

## V9 — Release Evaluation
Run `09_release_eval.py`.

Run happy-path and adversarial fixtures. Critical policy/security failures must block release.

## V10 — Production DevOps AI Assistant
Run `10_production_devops_ai_assistant.py`.

Trace every layer:
```text
Input
→ Policy
→ Stateful orchestration
→ Specialists/tools
→ Evidence store
→ RAG references
→ Gap/conflict gate
→ Grounded model
→ Citation validation
→ Action proposal
→ Approval
→ Final status/audit
```

## Provider Bonus
Run `11_dual_provider_capstone_rca.py` with Ollama and OpenAI using the same collected evidence/context.

**Rule:** swapping provider must not bypass evidence, citation, confidence or action policy.

### Final Failure Drills
- E1 missing
- tool error
- unknown citation
- model unavailable
- malicious reference instruction
- production write without approval
- conflict between evidence sources
- max-iteration/no-progress state

### Final Acceptance Criteria
Learner can explain each architecture box and replace one simulated read-only connector with a real safe connector without changing trust rules.

## Hero Outcome
Learner has built the course capstone: an evidence-grounded, provider-flexible, stateful, multi-agent, security-evaluated DevOps AI Assistant architecture.
