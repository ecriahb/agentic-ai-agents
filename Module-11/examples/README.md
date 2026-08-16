# Module 11 — Practical Labs

These labs turn enterprise architecture decisions into small, runnable Python exercises. They do **not** create Azure resources or perform cloud writes.

## Setup

```bash
cd Module-11/examples
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

No external Python packages are required for the core labs.

## Run Order

```text
V1  01_workload_decomposition.py
V2  02_environment_boundaries.py
V3  03_identity_rbac_policy.py
V4  04_network_path_validator.py
V5  05_runtime_decision_matrix.py
V6  06_data_trust_classes.py
V7  07_backpressure_simulator.py
V8  08_ha_dr_scorecard.py
V9  09_observability_slo.py
V10 10_production_readiness.py
```

## Learning Goal

Each lab converts one architecture principle into an explicit machine-checkable contract. By V10, the scorecard validates whether a proposed DevOps AI platform has the minimum enterprise controls expected before the Module 12 final project.

## Safety

- No Azure mutation.
- No credentials required.
- No real production endpoints.
- Replace simulated checks with organization-specific controls only after review.
