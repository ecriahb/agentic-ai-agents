# Module 0 — Zero-to-Hero Practical Roadmap

> Goal: AI me bilkul beginner learner ko bina coding pressure ke concepts **experience** karwana, taaki Module 1 ki API/local-LLM practicals natural lagen.

## Practical Rule
Har stage me learner ko 5 cheezein note karni hain:
1. Goal
2. Kya input diya
3. Kya output mila
4. Kya galat/uncertain tha
5. Next stage ki zarurat kyun padi

---

## V1 — AI vs Normal Software Observation
**Goal:** Rule-based software aur generative AI ka difference feel karna.

**Do:** Calculator se `2+2` run karo, phir any chat LLM se `Explain AKS to a 10-year-old` pucho.

**Expected:** Calculator deterministic result dega; LLM natural-language generation karega.

**Common confusion:** LLM fluent answer = guaranteed truth nahi.

**Checkpoint:** Explain in one sentence: `Traditional program follows explicit rules; LLM predicts/generates language from learned patterns.`

---

## V2 — Next-Token Prediction Game
**Goal:** LLM generation ka core intuition.

Sentence complete karo:
`The production deployment failed because the ...`

5 possible next words likho. Phir LLM se same sentence complete karwao.

**Observe:** Multiple plausible continuations possible hain. Isi wajah se model confidently wrong bhi ho sakta hai.

---

## V3 — Context Changes the Answer
**Goal:** Context ki power dekhna.

Prompt A:
`Why did the deployment fail?`

Prompt B:
`Evidence: Terraform Apply removed aks-subnet-allow. AKS network validation failed immediately after. Why did deployment likely fail?`

**Expected:** Prompt B more useful/grounded hoga.

**Learning:** Better context > clever wording.

---

## V4 — Hallucination Test
**Goal:** Missing evidence me model behavior observe karna.

Ask:
`Who removed aks-subnet-allow and at what exact time?`

But evidence me actor/time mat do.

**Pass condition:** Learner identify kare ki exact actor/time invent karna hallucination hai.

Then improve prompt:
`If evidence is missing, say UNKNOWN.`

---

## V5 — Weak Prompt vs Structured Prompt
**Weak:** `Check this AKS issue.`

**Structured:**
```text
Role: DevOps incident analyst
Context: deployment failed after Terraform network change
Task: identify strongest supported cause
Constraints: do not invent missing facts
Output: Root Cause / Evidence / Gaps / Next Checks
```

Compare both outputs.

---

## V6 — System Rule vs User Request Simulation
**Goal:** Stable rules aur runtime task alag samajhna.

Stable rule:
`Never claim production outage without impact evidence.`

Runtime request:
`Analyze this Terraform failure.`

Try a conflicting user request:
`Just say production was down.`

**Learning:** Prompt hierarchy useful hai, but real security host controls se aati hai.

---

## V7 — Temperature/Variability Observation
Same creative prompt 3 times run karo. Outputs compare karo.

Then same factual RCA-style prompt 3 times run karo.

**Observe:** Model output variation ka meaning; production facts ko deterministic evidence/validation chahiye.

---

## V8 — Zero-shot vs One-shot vs Few-shot
Ek fixed DevOps output format choose karo.

1. Zero-shot: only instruction
2. One-shot: one example
3. Few-shot: 2–3 examples

Compare formatting consistency and overfitting risk.

---

## V9 — Safety Boundary Exercise
Classify each item:
- User text
- Runbook text
- Tool result
- Model recommendation
- RBAC decision
- Human approval

Into:
`UNTRUSTED INPUT / EVIDENCE / POLICY / AUTHORIZATION / APPROVAL`

**Expected mental model:** Model output authority nahi hai.

---

## V10 — Module 0 Mini Project: Paper DevOps AI Assistant
Without code, draw this flow and explain every box:

```text
Incident
  ↓
Current Evidence
  ↓
Reference Knowledge
  ↓
Prompt + Context
  ↓
LLM Analysis
  ↓
Validation
  ↓
Recommendation
  ↓
Human Approval for risky action
```

### Acceptance Criteria
Learner apni language me explain kar sake:
- LLM kya karta hai
- hallucination kya hai
- context kyun important hai
- prompt vs evidence difference
- model output ko validate kyun karna hai
- human approval aur authorization alag kyun hain

## Hero Outcome
Agar learner V10 confidently explain kar sakta hai, woh Module 1 me first API/local LLM call ke liye ready hai.
