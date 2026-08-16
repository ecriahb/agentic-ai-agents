# 🚩 Jai Bajrangbali!

# Lesson 09 — Conflict Resolution & Evidence-Grounded Synthesis

> **Agent disagreement ko majority vote se solve karna unsafe hai. Conflict ka answer stronger evidence, provenance aur explicit uncertainty se aana chahiye.**

---

# 🎯 Lesson Goal

Aap samjhoge:
- agent conflicts kya hote hain
- fact conflict vs interpretation conflict
- source precedence
- conflict matrix
- deterministic synthesis
- uncertainty and abstention
- final RCA construction

---

# PART 1 — Example Conflict

Terraform specialist:

```text
[E2] NSG rule was removed.
Hypothesis: removal caused AKS issue.
```

AKS specialist:

```text
[E3] network validation is degraded.
Hypothesis: connectivity failure may be due to route or NSG policy.
```

These do not truly conflict.

They are complementary evidence.

---

# PART 2 — Real Conflict Types

## Type 1 — Source conflict

```text
Agent A: deployment status = failed
Agent B: deployment status = succeeded
```

Need timestamps/source systems.

## Type 2 — Interpretation conflict

```text
A: NSG is root cause
B: UDR is root cause
```

Need more evidence.

## Type 3 — Freshness conflict

```text
10:00 degraded
10:20 healthy
```

Both may be correct at different times.

## Type 4 — Scope conflict

```text
Pipeline failed
but application runtime was healthy
```

Different system layers.

---

# PART 3 — Never Use Blind Majority Voting

Three agents repeating same unsupported claim does not make it true.

```text
3 hallucinations > 1 evidence-backed specialist ?
```

No.

Trust should depend on:

```text
source authority
freshness
provenance
claim support
scope
```

---

# PART 4 — Source Precedence

Example policy:

```text
Current API/tool observation
> stale cached observation
> approved runbook
> model inference
```

But precedence is domain-specific.

For deployment status:

```text
pipeline system-of-record
```

For Kubernetes runtime:

```text
cluster control-plane observation
```

---

# PART 5 — Conflict Record

```python
{
  "conflict_id": "C1",
  "claim": "AKS connectivity is healthy",
  "supporting": ["E4"],
  "contradicting": ["E3"],
  "reason": "different timestamps",
  "resolution": "REFRESH_REQUIRED"
}
```

Conflict should become first-class state, not hidden inside prose.

---

# PART 6 — Resolution Strategies

```text
1. Refresh volatile evidence
2. Ask another authoritative source
3. Compare timestamps/scope
4. Re-run deterministic validation
5. Mark unresolved
6. Escalate to human when necessary
```

---

# PART 7 — Synthesis Contract

Synthesizer receives:

```text
validated observations
reference knowledge
unresolved conflicts
known gaps
```

Not:

```text
all raw internal agent conversations
```

Final answer should separate:

```text
Confirmed Facts
Likely Interpretation
Evidence Gaps
Conflicts
Recommended Checks
Confidence
```

---

# PART 8 — DevOps RCA Example

Confirmed:

```text
[E1] deployment failed during Terraform Apply
[E2] NSG rule was removed
[E3] AKS network validation degraded
```

Reasonable synthesis:

```text
Evidence strongly links the Terraform networking change with the observed connectivity degradation.
```

Unsafe synthesis:

```text
A specific engineer accidentally removed the rule and caused a 3-hour customer outage.
```

No evidence for actor/duration/customer impact.

---

# PART 9 — Confidence Policy

Confidence should reflect evidence policy, not model emotion.

Example:

```text
HIGH   = multiple authoritative current observations align
MEDIUM = plausible causal link but incomplete verification
LOW    = weak/indirect evidence
UNKNOWN = insufficient/conflicting evidence
```

---

# PART 10 — Synthesis Validator

Check:

```text
all current factual claims cite E*/approved H*
reference claims cite R*
no unknown IDs
conflicts are disclosed
unsupported impact removed
action execution not claimed
```

---

# PART 11 — Common Mistakes

- majority vote
- latest agent wins
- confidence from model self-report only
- stale/current evidence merged silently
- unresolved conflict hidden
- synthesis agent allowed to invent missing facts

---

# PART 12 — Interview Q&A

### Q1. How should multi-agent disagreement be resolved?
By evidence provenance, source authority, freshness, scope and additional verification—not majority voting.

### Q2. What if conflict cannot be resolved?
Preserve it explicitly, lower confidence, abstain on the disputed claim and request more evidence/human review.

### Q3. Why separate synthesis from specialists?
It centralizes final claim construction and makes evidence validation consistent.

### Q4. What is a freshness conflict?
Two observations differ because they were taken at different times rather than because one is false.

---

# PART 13 — Revision

```text
Disagreement = investigate
Votes != truth
Source authority matters
Freshness matters
Unresolved conflicts stay visible
Synthesis must cite evidence
```

---

# PART 14 — Homework

Create three conflict scenarios:
1. stale vs current AKS status
2. Terraform vs manual portal config
3. pipeline status mismatch

For each define resolution policy.

---

# 🔁 Next Lesson Kyu?

Ab multi-agent reasoning reliable hai. Next hum har agent ke **RAG, MCP, tools aur approval authority** ko scope karenge.
