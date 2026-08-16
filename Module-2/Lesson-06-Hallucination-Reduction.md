# 🚩 Jai Bajrangbali!

# Lesson 06 — Hallucination Reduction & Abstention

> **Hallucination ko sirf “don't hallucinate” likhkar solve nahi kiya ja sakta. Evidence boundaries, unknown states aur host validation design karna padta hai.**

---

# 🎯 Lesson Goal

Aap samjhoge:

- hallucination kya hoti hai
- DevOps me hallucination dangerous kyu hai
- evidence-first prompting
- abstention/insufficient-evidence behavior
- fact vs inference vs recommendation separation
- unsupported impact reduction
- source labels
- deterministic host validation
- provider/model change ke baad re-evaluation

---

# 1. English Definition

**A hallucination is model-generated content presented as if it were supported or true even though the available evidence does not justify it.**

DevOps example:

Evidence:

```text
Deployment failed during Terraform Apply.
```

Hallucination:

```text
All AKS nodes became NotReady and customers experienced 42 minutes of downtime.
```

None of that was supplied.

---

# 2. Why Models Hallucinate

LLM's core job is to generate plausible next text.

It does not automatically know:

```text
which statement came from evidence
which came from prior model knowledge
which is merely plausible
```

So application must create explicit evidence boundaries.

---

# 3. Weak Anti-Hallucination Rule

```text
Do not hallucinate.
```

Useful reminder, but vague.

Better rules:

```text
- Use E* sources for current incident factual claims.
- If a fact is not present, mark it UNKNOWN.
- Do not infer customer impact from deployment failure alone.
- Separate confirmed facts from supported hypotheses.
- Do not claim remediation success without post-action evidence.
```

Specific rules are testable.

---

# 4. Evidence-First Prompting

Instead of:

```text
What caused the deployment failure?
```

Use:

```text
First list confirmed evidence.
Then identify the strongest hypothesis supported by that evidence.
Then list missing evidence that would increase or decrease confidence.
```

This slows premature conclusion formation.

Mental model:

```text
Evidence
  ↓
Facts
  ↓
Inference
  ↓
Gaps
  ↓
Recommendation
```

---

# 5. Abstention is a Feature

Production AI must be allowed to say:

```text
INSUFFICIENT_EVIDENCE
UNKNOWN
UNVERIFIED
```

Example:

```text
[E1] Process exited with code 1.
```

Correct:

```text
Root cause cannot be determined from exit code alone.
```

Bad:

```text
Root cause is an NSG misconfiguration.
```

A forced answer is worse than an honest unknown.

---

# 6. Fact vs Inference vs Recommendation

## Fact

```text
[E2] NSG rule aks-subnet-allow was removed.
```

## Inference

```text
The rule removal is a strong candidate for the later connectivity failure.
```

## Recommendation

```text
Compare effective NSG rules with the approved baseline.
```

Do not present all three as the same trust class.

---

# 7. Impact Hallucination

Technical event:

```text
deployment failed
```

Does not automatically mean:

```text
service outage
customer impact
SLA breach
data loss
```

Prompt should say:

```text
Report only confirmed impact from supplied impact/telemetry evidence.
Otherwise state that customer impact is unknown.
```

---

# 8. Source Labels

Use source IDs:

```text
[E1] Pipeline failure
[E2] Terraform change
[E3] AKS status
```

Ask model to cite them.

Benefits:

- traceability
- easier validation
- easier human review
- unsupported source IDs can be rejected

But:

```text
valid source ID != claim automatically supported
```

Claim-to-source semantic support is a deeper validation problem.

---

# 9. Prompt Alone is Not Enough

Model might still output:

```text
[E99] customers were impacted
```

Host can deterministically check:

```text
allowed IDs = {E1, E2, E3}
E99 → reject
```

Similarly host can calculate confirmed impact from deterministic evidence fields rather than trusting free-form model output.

---

# 10. Grounding Hierarchy

A strong application can distinguish:

```text
CURRENT EVIDENCE [E*]
REFERENCE KNOWLEDGE [R*]
USER ASSERTION
MODEL INFERENCE
```

Highest factual support for incident claims should come from authorized current evidence, not model confidence.

---

# 11. Negative Test Cases

Do not only test strong-evidence cases.

### Case A — no evidence
Expected: abstain.

### Case B — weak evidence
Expected: identify gaps.

### Case C — contradictory evidence
Expected: surface conflict.

### Case D — irrelevant evidence
Expected: do not force root cause.

### Case E — prompt injection inside log
Expected: treat as data.

---

# 12. Provider Comparison

Run same grounded prompt on Ollama and OpenAI.

Evaluate:

```text
unsupported claim count
abstention correctness
source usage
impact hallucination
format adherence
```

A stronger model can still hallucinate.
A smaller model can sometimes follow a simple evidence contract well.

Only evals tell you.

---

# 13. Common Mistakes

1. “Don't hallucinate” as only control.
2. No explicit unknown state.
3. Model allowed to invent impact.
4. General runbook treated as current evidence.
5. Citation validity mistaken for factual support.
6. Structured output mistaken for truth.
7. No negative/adversarial eval cases.
8. Model confidence accepted as objective confidence.

---

# 14. Production Pattern

```text
Authorized Evidence Collection
      ↓
Source IDs / Provenance
      ↓
Grounded Prompt
      ↓
LLM
      ↓
Schema Validation
      ↓
Citation Validation
      ↓
Deterministic Policy Checks
      ↓
Human Review / Response
```

---

# 15. Interview Q&A

### Q1. How do you reduce hallucination in an agent?
Ground it in authoritative evidence, define abstention rules, separate facts/inferences, validate outputs and restrict actions with deterministic host controls.

### Q2. Is RAG enough to eliminate hallucination?
No. Retrieval can be irrelevant, stale, poisoned or misinterpreted.

### Q3. Why allow abstention?
Because insufficient evidence is a legitimate operational state and guessing can lead to unsafe decisions.

### Q4. Is model confidence trustworthy?
Not as an objective factual confidence measure. Confidence policy should be evidence-based where possible.

### Q5. What does citation validation prove?
At minimum that cited IDs exist; deeper validation is needed to prove that each claim is actually supported.

---

# 16. Quick Revision

```text
No evidence → no forced RCA
Fact != inference
Inference != recommendation
Failure != customer impact
Citation != truth
```

---

# 🧪 Homework

Create four incident inputs:

1. full evidence
2. only exit code
3. conflicting network evidence
4. irrelevant database log

Run your grounded prompt on both providers and record whether each correctly abstains or proceeds.

---

# ➡️ Why Next?

Ab hallucination controls clear hain. Next problem: **which evidence should actually enter the context window?** That is context engineering.
