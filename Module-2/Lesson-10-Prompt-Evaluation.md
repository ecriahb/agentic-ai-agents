# 🚩 Jai Bajrangbali!

# Lesson 10 — Prompt Evaluation

> **Ek prompt ka ek baar achha answer dena proof nahi hai. Reliable prompt ko normal, weak-evidence, conflicting aur adversarial cases par evaluate karo.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- prompt evaluation kya hai
- golden/labelled test cases
- exact-match vs rubric evaluation
- groundedness and unsupported claims
- abstention accuracy
- output-contract adherence
- provider/model comparison
- regression testing
- production release criteria

---

# 1. English Definition

**Prompt evaluation is the systematic testing of model behavior against a defined dataset, expected properties and scoring criteria rather than judging a prompt from one successful response.**

Mental model:

```text
Prompt Version
    ↓
Test Dataset
    ↓
Model/Provider
    ↓
Outputs
    ↓
Evaluators
    ↓
Metrics / Failures
    ↓
Keep / Improve / Block
```

---

# 2. Why Manual “Looks Good” is Weak

A response can sound professional while still:

- inventing impact
- citing fake evidence IDs
- missing an important gap
- recommending unsafe action
- failing on a slightly different incident

So evaluation must test properties, not style only.

---

# 3. Build a Small Golden Dataset

Example test cases:

```text
T1 strong NSG evidence
T2 only exit code 1
T3 image pull failure after unrelated network change
T4 conflicting network observations
T5 prompt injection inside log
T6 normal healthy deployment
```

Each test needs expected behavior.

Example T2 oracle:

```text
must abstain from root-cause claim
must state evidence gap
must not invent NSG issue
```

---

# 4. Evaluation Dimensions

## Groundedness

Are current-incident factual claims supported by supplied evidence?

## Abstention

Does model say insufficient/unknown when evidence is weak?

## Impact correctness

Does it avoid inventing customer impact?

## Output adherence

Are required sections present?

## Safety

Does it avoid claiming/performing unauthorized remediation?

## Relevance

Does answer address the actual question without unnecessary speculation?

---

# 5. Deterministic Evaluators

Some checks should be code-based.

Examples:

```text
required section names exist
citation IDs belong to allowed set
forbidden write tool was not called
iteration count <= limit
secret pattern absent
status == INSUFFICIENT_EVIDENCE for negative fixture
```

These are stronger than asking another LLM for every rule.

---

# 6. Rubric Evaluators

Some properties are semantic:

```text
Does root cause overstate causality?
Is recommendation appropriate to evidence?
Is explanation clear?
```

A human or judge model can score them with a rubric.

But evaluator models also have errors.

For critical security policy prefer deterministic checks wherever possible.

---

# 7. Example Evaluation Table

```text
Case | Grounded | Abstain Correctly | Format | Unsafe Claim
T1   | PASS     | N/A               | PASS   | NO
T2   | PASS     | PASS              | PASS   | NO
T3   | FAIL     | FAIL              | PASS   | NO
```

This tells you where prompt fails instead of “model was bad.”

---

# 8. Provider Comparison

Run same dataset against:

```text
Ollama/qwen3:4b
OpenAI selected model
```

Compare:

```text
groundedness pass rate
abstention accuracy
format adherence
latency
cost where applicable
```

Do not compare only one hand-picked prompt.

A provider change is a regression-test event.

---

# 9. Prompt Versioning

Track:

```text
prompt_v1
prompt_v2
prompt_v3
```

When you add a rule such as:

```text
Do not infer customer impact
```

run full eval dataset again.

Improving one case can degrade another.

---

# 10. Negative Tests Matter

Many demos only test answerable questions.

Production needs:

```text
no evidence
wrong environment
unavailable tool
conflicting evidence
malicious context
irrelevant request
```

Correct refusal/abstention is part of quality.

---

# 11. False Positive vs False Negative

Example security classifier:

```text
False positive → safe request blocked
False negative → unsafe request allowed
```

Both matter.

A prompt that refuses everything is not a good production system.

Include benign cases to measure over-blocking.

---

# 12. Prompt Evaluation vs System Evaluation

Prompt eval tests prompt/model behavior.

Full agent eval later tests:

```text
routing
tool calls
retrieval
state transitions
approval
trajectory
final answer
```

Do not assume good prompt eval means whole agent is safe.

---

# 13. Practical Mini Eval

Create a Python list:

```python
tests = [
    {"id":"strong", "expect_root_cause": True},
    {"id":"weak", "expect_root_cause": False},
]
```

Run `dual_provider_prompt_playground.py` logic for each fixture.

Check required text/properties programmatically.

Then manually inspect semantic support.

---

# 14. Common Mistakes

1. One successful demo treated as validation.
2. Only positive/easy cases.
3. Exact wording used as only oracle.
4. No prompt/model/provider version metadata.
5. Evaluation dataset changes silently.
6. Security failures averaged away by high overall score.
7. Judge LLM used for deterministic policy.
8. No regression suite in CI later.

---

# 15. Release Thinking

Example gate:

```text
Groundedness >= required threshold
Critical hallucination cases = 0
Unknown citation IDs = 0
Unsafe write behavior = 0
Abstention test pass = required
```

Critical failures should block regardless of average quality score.

---

# 16. Interview Q&A

### Q1. How do you evaluate prompts?
Use a versioned labelled dataset, deterministic validators, semantic rubrics and regression comparisons across prompt/model versions.

### Q2. Why not judge one answer manually?
Because model behavior varies across inputs and one response does not measure robustness.

### Q3. What is abstention accuracy?
Whether the system correctly refuses to make unsupported claims when evidence is insufficient.

### Q4. Why include benign cases in security evals?
To detect excessive false blocking.

### Q5. Prompt eval vs agent eval?
Prompt eval focuses on model response behavior; agent eval includes trajectory, tools, retrieval, routing, state and side effects.

---

# 17. Quick Revision

```text
Prompt
+ Dataset
+ Expected Behavior
+ Evaluators
+ Metrics
+ Regression
=
Prompt Engineering You Can Trust More
```

---

# 🧪 Homework

Build five fixtures for the Module 1 NSG incident:

- strong evidence
- weak evidence
- conflicting evidence
- unrelated root cause
- injection in log

Define expected pass/fail properties before running the model.

---

# ➡️ Why Next?

Once a prompt is evaluated, it should become a **reusable versioned prompt template**, not copied strings across scripts. Next lesson covers templates.
