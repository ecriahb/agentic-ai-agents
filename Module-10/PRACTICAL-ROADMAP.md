# Module 10 — Zero-to-Hero Practical Roadmap

> Goal: security theory ko executable attack/control/evaluation exercises me convert karna.

## V1 — Threat Model
Run `examples/01_threat_model.py`.

Identify assets, trust boundaries, attackers, capabilities and blast radius.

## V2 — Prompt Injection Lab
Run `02_prompt_injection_lab.py`.

Test malicious instruction inside user/log/reference text.

**Pass:** application treats data as data; prompt text alone is not the only defense.

## V3 — Tool Policy Gate
Run `03_tool_policy_gate.py`.

Try unknown/destructive tools and invalid targets. Expected deterministic deny.

## V4 — Secret Redaction
Run `04_secret_redaction.py`.

Seed fake secret/token patterns and verify redaction before model/log output.

## V5 — RAG Poisoning
Run `05_rag_poisoning_lab.py`.

Add malicious/incorrect reference content and observe why retrieval trust/source governance matter.

## V6 — MCP Trust Policy
Run `06_mcp_trust_policy.py`.

Test unknown/unapproved MCP server/capability.

**Rule:** discovery != trust/authorization.

## V7 — Multi-Agent Isolation
Run `07_multi_agent_isolation.py`.

Simulate one compromised specialist response; verify it does not become trusted shared evidence automatically.

## V8 — Deterministic Policy Engine
Run `08_policy_engine.py`.

Build explicit allow/deny decisions for environment, action, target, evidence and approval state.

## V9 — Eval Runner
Run `09_eval_runner.py`.

Score safe/unsafe fixtures and inspect failures rather than only average score.

## V10 — Secure Release Harness
Run `10_secure_agent_release_harness.py`.

Expected pipeline:
`Test case → Agent → Trajectory → Policy/Secret/Citation checks → Scorecard → PASS/FAIL`.

## Provider Bonus
Run `11_dual_provider_eval_target.py` on Ollama and OpenAI using the same security fixtures.

Compare **safety behavior**, not writing quality only.

### Required Red-Team Cases
- direct prompt injection
- indirect injection in retrieved text
- unknown tool
- production write without approval
- fake evidence/citation ID
- secret leakage
- multi-agent contamination
- loop exhaustion

### Acceptance Criteria
Learner understands:
`System prompt != security boundary`, `Good final answer != safe trajectory`, `Critical failure must block release`.

## Hero Outcome
Learner can prove an agent is safer through tests and policy gates instead of trusting demos.
