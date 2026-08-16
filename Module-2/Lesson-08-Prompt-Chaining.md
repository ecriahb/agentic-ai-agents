# 🚩 Jai Bajrangbali!

# Lesson 08 — Prompt Chaining

> **Complex incident ko ek giant prompt me solve karne ke bajay controlled stages me break karo.**

## 🎯 Goal
Prompt chaining ka use karke DevOps investigation ko deterministic stages me divide karna.

---

# 1. Prompt Chaining Kya Hai?

```text
Prompt 1 → Extract Evidence
Prompt 2 → Build Timeline
Prompt 3 → Generate Hypotheses
Prompt 4 → Validate Against Evidence
Prompt 5 → Produce Final RCA
```

Har stage ka output next stage ka input ban sakta hai.

---

# 2. Why Not One Giant Prompt?

One giant prompt me model simultaneously:
- logs parse karta hai
- relevant events choose karta hai
- cause infer karta hai
- impact likhta hai
- fix recommend karta hai

Isse unsupported leaps ka risk increase hota hai.

Chained flow:

```text
Raw Logs
  ↓
Evidence Extraction
  ↓
Normalized Facts
  ↓
Reasoning
  ↓
Validation
  ↓
Final Report
```

---

# 3. DevOps Chain Example

## Stage 1 — Evidence Extractor

```text
Extract only factual events from these logs.
Return timestamp, source and observation.
Do not diagnose.
```

## Stage 2 — Timeline Builder

```text
Order E1-E10 chronologically.
Mark the first failure and later downstream failures.
Do not infer root cause.
```

## Stage 3 — Hypothesis Generator

```text
Using only the normalized timeline, generate up to 3 plausible root-cause hypotheses.
For each hypothesis list supporting and contradicting evidence.
```

## Stage 4 — Validator

```text
Reject any hypothesis that lacks evidence.
Return the strongest supported hypothesis and missing validation.
```

## Stage 5 — Reporter

```text
Generate Root Cause, Impact, Validation, Fix and Confidence using only validated evidence.
```

---

# 4. Chain Contracts

Har stage ka fixed output helpful hai.

Example:

```json
{
  "evidence_id": "E1",
  "timestamp": "10:04:37",
  "source": "pipeline.log",
  "observation": "NSG rule aks-subnet-allow was removed"
}
```

Next stage free-form raw text ke badle normalized data consume karega.

---

# 5. Failure Handling

Agar Stage 1 evidence find nahi karta:

```text
No evidence → stop chain → no RCA
```

Agar Stage 4 sab hypotheses reject karta:

```text
Insufficient evidence → request next evidence
```

Ye Module 1 ke no-evidence/no-RCA principle se directly connected hai.

---

# 6. Prompt Chain vs Agent Loop

```text
Prompt Chain = predefined sequence
Agent Loop   = model decides next action/tool dynamically
```

Simple predictable workflow → chain useful.
Dynamic investigation → agent loop useful.
Hybrid architecture bhi possible hai.

---

# 🧪 Exercise
Build a chain for:

```text
GitHub Actions pipeline failed during AKS deployment.
```

Recommended stages:
1. extract errors
2. classify stage
3. correlate recent change
4. validate hypothesis
5. final summary

# 🔑 Summary

```text
Decompose → normalize → validate → report
```

# ➡️ Why Next?
Prompt chaining predictable hai. But agent dynamically tool select kare to uske loop ko prompts + guardrails se control karna padega. Next: Agent Loop Prompts & Guardrails.
