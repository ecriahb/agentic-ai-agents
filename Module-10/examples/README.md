# Module 10 Practicals — Security, Evaluation & Red Teaming

> Run these labs in order. Each version introduces one security/evaluation concept before V10 combines them.

## Setup

```powershell
cd Module-10\examples
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

These baseline labs intentionally use deterministic/local simulations so security behavior is reproducible and no production mutation occurs.

---

## V1 → V10 Progression

| Version | File | Main Learning |
|---|---|---|
| V1 | `01_threat_model.py` | Assets, actors, boundaries, threats |
| V2 | `02_prompt_injection_lab.py` | Injection detection as signal, not authority |
| V3 | `03_tool_policy_gate.py` | Tool/argument/approval policy |
| V4 | `04_secret_redaction.py` | Sensitive-output redaction |
| V5 | `05_rag_poisoning_lab.py` | Approved-source and malicious-document gate |
| V6 | `06_mcp_trust_policy.py` | MCP server + tool allowlist |
| V7 | `07_multi_agent_isolation.py` | Shared evidence vs untrusted handoff data |
| V8 | `08_policy_engine.py` | Role authorization + environment/risk policy |
| V9 | `09_eval_runner.py` | Deterministic security regression cases |
| V10 | `10_secure_agent_release_harness.py` | Combined red-team trajectory + release gate |

---

## Run Order

```powershell
python 01_threat_model.py
python 02_prompt_injection_lab.py
python 03_tool_policy_gate.py
python 04_secret_redaction.py
python 05_rag_poisoning_lab.py
python 06_mcp_trust_policy.py
python 07_multi_agent_isolation.py
python 08_policy_engine.py
python 09_eval_runner.py
python 10_secure_agent_release_harness.py
```

---

## V10 Expected Concepts

The final harness tests:
```text
normal approved read
prompt injection
prod write without approval
unknown MCP server
secret leakage/redaction
fake evidence citation
```

For every test it records a small trajectory:
```text
INPUT
→ INJECTION SIGNAL (when applicable)
→ MCP POLICY
→ TOOL POLICY
→ SIMULATED EXECUTION (only if allowed)
→ SECRET REDACTION
→ CITATION VALIDATION
→ FINAL TEST STATUS
```

Then release decision:
```text
all security cases pass
+ no critical forbidden execution
= RELEASE_GATE: PASS
```

Any failed invariant blocks the release.

---

## Practical Experiments

After baseline works, add these cases yourself:
1. invalid environment
2. unknown tool
3. malicious RAG resource
4. approval for changed arguments
5. fake agent evidence ID
6. repeated tool calls / max budget
7. cross-tenant document request
8. tool result containing a bearer token
9. MCP server schema drift
10. conflicting specialist evidence

---

## Production Upgrade Direction

```text
Local harness
 ↓
Versioned JSON/YAML dataset
 ↓
pytest / CI job
 ↓
Real agent trace adapter
 ↓
Agent trajectory evaluator
 ↓
Security regression suite
 ↓
Optional LangSmith evaluation/observability
 ↓
Shadow/canary release
 ↓
Production security dashboard
```

Do not replace deterministic critical invariants with an LLM judge. Use LLM-as-judge only where semantic quality genuinely requires fuzzy evaluation.
