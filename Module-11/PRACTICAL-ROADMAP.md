# Module 11 — Zero-to-Hero Practical Roadmap

> Goal: agent code ko enterprise production platform ke lens se validate karna—identity, network, runtime, data, scale, resilience, observability and readiness.

These labs are intentionally local simulations/scorecards first. They teach architecture decisions without requiring an Azure bill on day one.

## V1 — Workload Decomposition
Run `examples/01_workload_decomposition.py`.

Classify components: API, orchestration, model gateway, retriever, state store, evidence connectors, write executor.

## V2 — Environment Boundaries
Run `02_environment_boundaries.py`.

Test dev/stage/prod isolation rules.

## V3 — Identity & RBAC Policy
Run `03_identity_rbac_policy.py`.

Compare read identity vs write identity. Production write should require stronger controls.

## V4 — Network Path Validator
Run `04_network_path_validator.py`.

Model private DNS, private endpoint, firewall/egress path failures.

## V5 — Runtime Decision Matrix
Run `05_runtime_decision_matrix.py`.

Choose between simple service, container platform/AKS and async workers based on workload needs—not fashion.

## V6 — Data Trust Classes
Run `06_data_trust_classes.py`.

Separate:
- conversation/session state
- durable workflow state
- current evidence
- reference knowledge
- secrets
- audit data

## V7 — Backpressure Simulator
Run `07_backpressure_simulator.py`.

Simulate burst load, queue depth and worker capacity. Observe why agent systems need bounded concurrency.

## V8 — HA/DR Scorecard
Run `08_ha_dr_scorecard.py`.

Ask: what survives region/service failure? What state can be reconstructed? What must be durable?

## V9 — Observability + SLO
Run `09_observability_slo.py`.

Track latency, error rate, tool failure, retrieval failure, policy blocks and agent success—not only CPU/memory.

## V10 — Production Readiness Gate
Run `10_production_readiness.py`.

System should fail readiness if critical identity/network/state/security/DR controls are missing.

## Provider Readiness Bonus
Run `11_provider_readiness_matrix.py`.

Compare Ollama/self-hosted and OpenAI/hosted paths across:
- identity/auth
- networking/egress
- data handling
- scaling
- cost
- observability
- failure modes

### Acceptance Criteria
Learner can design the platform around trust boundaries and SLOs, not only around the LLM call.

## Hero Outcome
Learner can explain how a DevOps AI application becomes an operable enterprise workload.
