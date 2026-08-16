# Module 12 — Final Capstone Practical Labs

These labs assemble the course incrementally. Run them in order.

## Setup

```bash
cd Module-12/examples
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For V7/V10 LLM generation, ensure Ollama is running and the configured model exists. The shared examples default to `qwen2.5:3b`; change `OLLAMA_MODEL` in your environment if needed.

## Run Order

```text
V1  01_project_contract.py
V2  02_evidence_tools.py
V3  03_reference_knowledge.py
V4  04_source_context.py
V5  05_specialist_team.py
V6  06_conflict_gap_gate.py
V7  07_grounded_rca.py
V8  08_policy_approval.py
V9  09_release_eval.py
V10 10_production_devops_ai_assistant.py
```

## Shared Files

- `capstone_core.py` — evidence tools, references, context, validation and policy helpers.
- `requirements.txt` — LangGraph/LangChain/Ollama dependencies for the integrated graph.

## Safety

The entire capstone is read-only/simulated. `restore_nsg_rule` is represented only as a proposal. No Azure, Kubernetes, Terraform or GitHub write operation is implemented.

## Demo Query

```text
Production AKS deployment failed after a Terraform networking change.
Investigate and provide an evidence-grounded RCA.
```

Expected source map:

```text
E1 → pipeline failure
E2 → Terraform NSG removal
E3 → AKS connectivity degradation
R1 → AKS networking guidance
R2 → Terraform networking guidance
```
