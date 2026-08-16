# Module 8 — Zero-to-Hero Practical Roadmap

> Goal: deterministic chain se explicit stateful agent workflow tak evolve karna—state, routing, bounded loops, persistence and human approval ko step-by-step samajhna.

## V1 — First StateGraph
Run `examples/01_first_stategraph.py`.

**Observe:** State + Node + Edge. Draw the graph before running it.

## V2 — Conditional Routing
Run `02_conditional_routing.py`.

Change state values and predict which edge will execute before running.

## V3 — Evidence Reducer
Run `03_evidence_reducer.py`.

Test duplicate evidence and verify merge/reducer behavior.

**Rule:** retries must not silently duplicate evidence.

## V4 — Controlled Tool Loop
Run `04_controlled_tool_loop.py`.

Trace:
`Plan → validate tool → execute read-only tool → append evidence → re-evaluate`.

## V5 — RAG + Evidence Router
Run `05_rag_evidence_router.py`.

Check current evidence and reference knowledge use different state fields.

## V6 — Retry / Loop Limits
Run `06_loop_limit_retry.py`.

Force no-progress and max-iteration conditions.

Expected: explicit stop state, not infinite loop.

## V7 — Human Approval
Run `07_human_approval.py`.

Test both approve and reject branches.

**Important:** approval is a workflow decision; authorization must still be separately enforced.

## V8 — Checkpoint + Resume
Run `08_checkpoint_resume.py`.

Pause/resume same thread and inspect restored state.

Think about which operational evidence may be stale after a long pause.

## V9 — Supervisor + Subgraphs
Run `09_supervisor_subgraphs.py`.

Identify parent state vs subgraph-local responsibility.

## V10 — Stateful DevOps Incident Agent
Run `10_stateful_devops_incident_agent.py`.

Test:
- normal investigation
- tool error
- missing evidence
- max iterations
- approval reject

## Provider Bonus
Run `11_dual_provider_stateful_rca.py` with Ollama and OpenAI.

**Key rule:** state transitions/routing/policy are host-controlled; provider is used for reasoning node only.

### Acceptance Criteria
Learner can explain:
`Workflow state != conversation memory`, `loop must be bounded`, `interrupt != authorization`, and `resume may require evidence refresh`.

## Hero Outcome
Learner can design auditable stateful agents instead of opaque while-loops.
