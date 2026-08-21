# Module 2 — Zero-to-Hero Practical Roadmap

> Goal: beginner ko random prompting se reliable, testable DevOps prompt system tak le jana.

## Setup
Use either Ollama or OpenAI through the repo provider guide. Start with `examples/prompt_playground.py` and `examples/dual_provider_prompt_playground.py`.

---

## V1 — Weak Prompt Baseline
Prompt:
`Why did my AKS deployment fail?`

Save the answer. Mark every unsupported claim.

**Purpose:** baseline ke bina improvement measure nahi kar sakte.

---

## V2 — Prompt Anatomy in a DevOps Task
Review the canonical anatomy and role/example boundaries in [Module 0 Lesson 07](../Module-0/Lesson-07-Prompt-Engineering.md), then apply them here.
Run: `examples/prompt_anatomy_test.py`

Build prompt with:
```text
Role
Context
Task
Constraints
Output Contract
```

**Expected:** output more focused and easier to review.

---

## V3 — System vs User Prompt Boundary
The foundational system/user distinction is covered in [Module 0 Lesson 08](../Module-0/Lesson-08-System-vs-User-Prompt.md). This stage applies it to a provider-backed prompt test.
Run: `examples/system_vs_user_test.py`

Test stable system rule:
`Do not invent missing evidence.`

Then runtime user request change karo.

**Learning:** stable behavior and runtime task separate responsibilities hain.

---

## V4 — Zero / One / Few Shot
Take one RCA format and test:
1. zero-shot
2. one-shot
3. few-shot

Record:
- format consistency
- extra tokens/context
- wrong pattern imitation risk

---

## V5 — Structured DevOps Prompt
Use: `incident_rca_prompt.txt`

Then use: `terraform_change_review_prompt.txt`

Compare how task-specific contracts reduce vague answers.

---

## V6 — Hallucination / Abstention Test
Evidence only:
`Terraform Apply failed with exit code 1.`

Ask for exact root cause.

Expected safe behavior:
`Insufficient evidence` / `UNKNOWN`.

Then add real evidence and compare.

---

## V7 — Context Engineering
Use mixed data:
- relevant pipeline lines
- unrelated old logs
- Terraform diff
- AKS observation

First send everything. Then send only normalized source-labelled evidence.

**Observe:** more context is not always better context.

---

## V8 — Prompt Chaining
Split one RCA into stages:
```text
Extract facts
→ build timeline
→ generate hypotheses
→ test hypotheses against evidence
→ final RCA
```

Store each stage output separately. Do not let one stage silently overwrite evidence.

---

## V9 — Prompt Evaluation
Create at least 5 fixtures:
- strong evidence
- weak evidence
- irrelevant evidence
- conflicting evidence
- prompt injection inside a log

Score:
- unsupported claims
- correct abstention
- required sections
- evidence citations

---

## V10 — Dual-Provider Incident Prompt System
Run: `examples/dual_provider_prompt_playground.py`

Use exact same system prompt, evidence and output contract on:
- Ollama
- OpenAI

**Do not compare only writing style. Compare:**
- grounding
- abstention
- format adherence
- unsupported claims

### Acceptance Criteria
Learner can build a reusable prompt asset that includes:
```text
Stable system rules
+ runtime task
+ source-labelled evidence
+ explicit abstention
+ output contract
+ evaluation fixtures
```

## Hero Outcome
Learner prompt likhna nahi, **prompt system design + test** karna samajhta hai.
