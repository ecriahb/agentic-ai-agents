# Module 8 — Practical Labs

These labs build the stateful agent progressively. Run them in order.

## Setup

```powershell
cd Module-8\examples
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

For V10 LLM analysis, run Ollama separately and make sure the configured local model exists.

```powershell
ollama list
```

Default learning model in the final example:

```text
qwen2.5:3b
```

## V1 → V10

```text
01_first_stategraph.py
    State + Node + START/END

02_conditional_routing.py
    Deterministic conditional edges

03_evidence_reducer.py
    Append/accumulate evidence using reducer semantics

04_controlled_tool_loop.py
    Observe → choose → execute → evidence → repeat

05_rag_evidence_router.py
    Keep CURRENT_EVIDENCE and REFERENCE knowledge separate

06_loop_limit_retry.py
    Max iterations, duplicate detection and no-progress stop

07_human_approval.py
    Interrupt → approve/reject → resume

08_checkpoint_resume.py
    Thread ID and saved graph state

09_supervisor_subgraphs.py
    Bounded Pipeline/Terraform/AKS specialist subgraphs

10_stateful_devops_incident_agent.py
    Final Module 1–8 integrated incident workflow
```

## Safety

All default DevOps tools in these labs are **deterministic read-only learning tools**. The approval lab simulates a write proposal but does not make a real Azure/Kubernetes change.

Core safety rules:

```text
LLM proposal != execution authority
reference knowledge != current incident evidence
checkpoint != evidence archive
approval != authorization
max loop limit = host policy
```

## Failure Tests

Try intentionally:

```text
unknown environment
unknown cluster
missing evidence
max iteration = 1
duplicate tool proposal
human reject
empty reference docs
Ollama stopped (V10)
```

Observe explicit status instead of guessing.
