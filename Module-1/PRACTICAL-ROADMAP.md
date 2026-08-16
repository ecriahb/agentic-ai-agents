# Module 1 — Zero-to-Hero Practical Roadmap

> Goal: beginner ko first model call se trusted evidence-based DevOps agent tak step-by-step le jana.

## Setup
```powershell
cd Module-1/examples
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Choose one path:
- Local: Ollama running + installed model
- Hosted: `OPENAI_API_KEY` in local `.env`

---

## V1 — First Hosted LLM Call
Run: `01_first_ai_call.py`

**Why first:** API request/response ko simplest possible form me samajhna.

**Observe:** request, model, response object, `output_text`.

**Common errors:** missing key, billing/credits, wrong model name, network failure.

---

## V2 — First Local LLM Call
Run: `02_ollama_ai_call.py`

**Why:** same AI concept without hosted API dependency.

**Observe:** local endpoint, model installed locally, no cloud key required.

**Compare:** latency, privacy, hardware dependency, model quality.

---

## V3 — Structured Output
Run: `03_structured_output.py`

**Goal:** free-text answer ko predictable contract me lana.

**Learning:** JSON/Pydantic shape validate kar sakte hain; factual truth automatically validate nahi hoti.

---

## V4 — Basic Tool Request
Run: `04_tool_call_basic.py`

**Goal:** model ko tool/capability concept introduce karna.

**Critical rule:** LLM tool call = request/proposal, execution authority nahi.

---

## V5 — Real File Tool
Open: `examples/lesson-05-real-tool-practical/`

Start with sample `pipeline.log`.

Build/read a tool that actually reads the file instead of returning fake hard-coded evidence.

**Expected:** learner clearly sees `LLM → tool request → host executes → tool result → model`.

---

## V6 — DevOps Agent V1
Run: `devops_agent_v1.py`

**Goal:** multiple DevOps observations ko one analysis flow me connect karna.

**Check:** evidence and model narrative ko separate print karo.

---

## V7 — DevOps Agent V2
Run: `devops_agent_v2.py`

**Goal:** pipeline + Terraform + AKS evidence combine karna.

**Pass:** model should not fabricate unavailable evidence.

---

## V8 — DevOps Agent V3
Run: `devops_agent_v3.py`

**Goal:** evidence-only RCA discipline.

Add/verify:
- evidence IDs
- no evidence → no RCA
- confirmed facts vs inference
- no invented customer impact

---

## V9 — DevOps Agent V4
Run: `devops_agent_v4.py`

**Goal:** structured schema + validation + safer host control.

Test intentionally bad inputs:
- unknown environment
- invented tool name
- unexpected argument
- missing evidence

**Learning:** schema validates structure; host validates policy/trust.

---

## V10 — Provider-Parity Trusted RCA
Run the same incident using both provider tracks through the shared provider setup from repo root.

Suggested sequence:
```powershell
# Local
$env:LLM_PROVIDER="ollama"
python shared/provider_smoke_test.py

# OpenAI
$env:LLM_PROVIDER="openai"
python shared/provider_smoke_test.py
```

Then compare final RCA quality while keeping **exact same evidence**.

### Acceptance Criteria
Learner can explain:
```text
LLM = reasoner
Host = executor/policy owner
Tool output = evidence
Tool request = untrusted proposal
No evidence = no forced RCA
Structured output = shape, not truth
```

## Hero Outcome
Beginner ab simple LLM consumer nahi; woh first controlled, evidence-grounded DevOps AI application ka mental model samajhta hai.
