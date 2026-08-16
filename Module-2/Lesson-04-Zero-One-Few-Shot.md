# 🚩 Jai Bajrangbali!

# Lesson 04 — Zero-Shot, One-Shot & Few-Shot Prompting

> **Examples model ko desired pattern dikhate hain, lekin examples facts prove nahi karte.**

---

# 🎯 Lesson Goal

Is lesson ke end tak aap samjhoge:

- zero-shot kya hai
- one-shot kya hai
- few-shot kya hai
- kab examples dene chahiye
- examples se formatting/classification reliability kaise improve hoti hai
- bad examples model ko kaise bias karte hain
- DevOps RCA examples me invented facts kaise avoid karne hain
- example count aur context budget ka trade-off

---

# 1. English Definitions

**Zero-shot prompting:** Asking the model to perform a task without showing an example of the desired answer.

**One-shot prompting:** Providing one representative example before asking the model to perform the task.

**Few-shot prompting:** Providing a small set of representative examples that demonstrate the desired behavior or output pattern.

Mental model:

```text
Zero-shot → instruction only
One-shot  → instruction + 1 example
Few-shot  → instruction + several examples
```

---

# 2. Why Examples Help

Suppose task is:

```text
Classify deployment risk as LOW / MEDIUM / HIGH.
```

Without examples model must infer what your organization means by those labels.

Few-shot can show:

```text
Read-only tag update → LOW
Replica count reduction in staging → MEDIUM
Production firewall/NSG deletion → HIGH
```

Now classification boundary becomes clearer.

---

# 3. Zero-Shot Example

```text
Classify this change as LOW, MEDIUM or HIGH risk.
Change: remove an NSG rule used by the production AKS subnet.
Return label and reason.
```

Advantages:

- shortest prompt
- lowest context cost
- easy to maintain

Use when task is obvious and output behavior already reliable.

---

# 4. One-Shot Example

```text
Example:
Change: rotate a non-production application label.
Risk: LOW
Reason: metadata-only change with no traffic effect.

Now classify:
Change: remove an NSG rule used by the production AKS subnet.
```

One example teaches output shape and some policy intent.

Risk: one example can over-anchor the model if not representative.

---

# 5. Few-Shot Example

```text
Example 1
Change: documentation text update
Risk: LOW

Example 2
Change: reduce staging deployment replicas from 4 to 2
Risk: MEDIUM

Example 3
Change: remove production AKS subnet allow rule
Risk: HIGH

Now classify:
Change: replace a production route table entry used by AKS egress.
```

Few-shot gives a broader decision surface.

---

# 6. Few-Shot for Structured RCA

Examples can teach desired separation:

```text
Confirmed Evidence:
...

Supported Hypothesis:
...

Unknown:
...
```

Good example explicitly abstains where evidence is missing.

That teaches model:

```text
"unknown" is an acceptable answer
```

which is important for incident analysis.

---

# 7. Dangerous Few-Shot Design

Bad examples:

```text
Incident A: pipeline failed after network change
Root cause: NSG

Incident B: pipeline failed after network change
Root cause: NSG

Incident C: pipeline failed after network change
Root cause: NSG
```

Now model can over-learn:

```text
network change → always NSG
```

Even when current evidence says image pull failure.

Examples should cover different outcomes, including abstention.

---

# 8. Examples Are Not Current Evidence

This is critical.

Example from previous incident:

```text
Example: last month an NSG deletion caused AKS failure.
```

Current incident:

```text
pipeline failed today
```

The example teaches reasoning/format.
It does not prove current root cause.

Rule:

```text
Few-shot example = behavior demonstration
Current evidence = factual support
```

---

# 9. Good Few-Shot Set for DevOps

A useful set may include:

```text
Case A → strong supported root cause
Case B → insufficient evidence
Case C → alternate cause despite similar symptom
Case D → conflicting evidence
```

This reduces anchoring and teaches uncertainty handling.

---

# 10. Context Window Trade-Off

More examples consume context.

```text
Prompt budget
├─ instructions
├─ examples
├─ current evidence
└─ output space
```

Do not sacrifice current evidence just to include many examples.

For production:

```text
small high-quality representative example set
>
large repetitive example dump
```

---

# 11. Provider Comparison

Ollama small models may sometimes benefit more from explicit examples for strict formatting.
Hosted models may follow complex instructions differently.

But do not assume.

Evaluate both using the same test cases:

```text
format adherence
correct abstention
unsupported claims
classification accuracy
```

Provider choice should be measured, not guessed.

---

# 12. Practical Exercise

Take this task:

```text
Classify Terraform changes as SAFE_REVIEW, NEEDS_SENIOR_REVIEW or BLOCK.
```

Run three versions:

1. zero-shot
2. one-shot
3. few-shot with safe + unsafe + ambiguous examples

Record:

```text
output consistency
false blocks
missed risky changes
reason quality
```

---

# 13. Common Mistakes

1. Too many examples.
2. All examples have same answer.
3. Examples contain unsupported factual claims.
4. Example output format differs from requested final format.
5. Using examples as current evidence.
6. Including secrets/real sensitive incident data in examples unnecessarily.
7. Never re-evaluating examples after policy changes.

---

# 14. Production Guidance

Version few-shot examples like code/configuration.

Track:

```text
example_set_version
prompt_version
model_version
eval_result
```

If risk policy changes, old examples may become wrong even if prompt text remains same.

---

# 15. Interview Q&A

### Q1. Zero-shot vs few-shot?
Zero-shot uses only instructions; few-shot additionally demonstrates desired behavior using examples.

### Q2. When is few-shot useful?
When task boundaries, labels or formatting are ambiguous and representative examples improve consistency.

### Q3. Can few-shot examples serve as evidence?
No. They demonstrate behavior; incident-specific facts require current evidence.

### Q4. What is example anchoring?
The model may overgeneralize patterns from examples and force similar conclusions on different inputs.

### Q5. How do you evaluate few-shot prompts?
Use labelled normal, ambiguous and failure cases and compare task accuracy, abstention and format adherence.

---

# 16. Quick Revision

```text
Zero-shot = no example
One-shot  = one example
Few-shot  = several representative examples
```

Best examples teach:

```text
correct answer
uncertainty
alternate outcome
format
```

---

# 🧪 Homework

Create three examples for AKS incident severity classification:

- LOW
- HIGH
- UNKNOWN due to insufficient evidence

Then test a fourth unseen incident on Ollama and OpenAI.

---

# ➡️ Why Next?

Ab examples se behavior guide karna samajh aa gaya. Next hum DevOps-specific **structured prompts** banayenge for RCA, Terraform change review and AKS troubleshooting.
