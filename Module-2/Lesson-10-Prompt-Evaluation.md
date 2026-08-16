# 🚩 Jai Bajrangbali!

# Lesson 10 — Prompt Evaluation

> **One good-looking answer does not prove a prompt is reliable. Test it across cases.**

## 🎯 Goal
Prompt quality ko measurable criteria ke against evaluate karna.

---

# 1. What Should We Evaluate?

For DevOps prompts:

```text
Correctness
Grounding
Completeness
Format Compliance
Safety
Consistency
Abstention Quality
```

---

# 2. Simple Scorecard

Score each 0–2:

| Metric | 0 | 1 | 2 |
|---|---|---|---|
| Grounding | unsupported | mixed | all claims supported |
| Format | wrong | partial | exact |
| Hallucination | major | minor | none observed |
| Missing-evidence handling | guesses | vague | explicit abstention |
| Safety | unsafe | mixed | safe/read-only first |

Total score can compare prompt versions.

---

# 3. Test Cases

A prompt ko different inputs par run karo:

### Case A — Strong Evidence
```text
NSG rule removed → connectivity validation failed → deployment failed
```

Expected: supported hypothesis.

### Case B — Weak Evidence
```text
Deployment failed with exit code 1
```

Expected: **Insufficient evidence**, not invented AKS issue.

### Case C — Conflicting Evidence
```text
NSG change present but connectivity check succeeded; image pull failed later.
```

Expected: model should not anchor on NSG change.

### Case D — No Customer Impact Evidence
Expected: should not claim outage.

---

# 4. Golden Outputs

For important workflows, create expected behavior:

```text
Input fixture
Expected facts
Forbidden claims
Expected output fields
```

Example:

```text
Forbidden:
- "AKS nodes are NotReady" unless node evidence exists
- "Customers experienced downtime" unless impact evidence exists
```

---

# 5. Regression Testing

Prompt v1 improve karke v2 banaya? Old test cases rerun karo.

```text
Prompt v1
   ↓
10 incident fixtures
   ↓
score

Prompt v2
   ↓
same 10 fixtures
   ↓
compare
```

Prompt changes can fix one case and break another.

---

# 6. Deterministic Validation

Some things model se judge karane ki need nahi:

```python
required_sections = [
    "Root Cause",
    "Evidence",
    "Impact",
    "Fix",
    "Confidence"
]
```

Similarly:
- JSON schema validation
- allowed confidence values
- evidence IDs exist or not
- root cause empty when evidence empty

Host validation + model evaluation together stronger hote hain.

---

# 7. Human Review

High-impact use cases me domain expert review important hai, especially:
- production remediation
- security findings
- compliance
- architecture changes

---

# 🧪 Evaluation Exercise

Compare prompts:

Prompt A:
```text
Find root cause and fix.
```

Prompt B:
```text
Use only supplied evidence. Separate fact from inference. Abstain when evidence is insufficient. Map every conclusion to evidence IDs. Return fixed sections.
```

Run both on strong, weak and conflicting evidence. Record hallucinations and format compliance.

# 🔑 Summary

```text
Prompt Quality = tested behavior, not subjective confidence
```

# ➡️ Why Next?
Evaluation ke baad stable patterns ko reusable templates me convert karna logical hai. Next: Reusable Prompt Templates.
