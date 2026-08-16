# 🚩 Jai Bajrangbali!

# Lesson 06 — Citations & Source Traceability

> **RAG answer tab zyada useful hota hai jab engineer dekh sake: ye claim kis source se aaya?**

---

# 🎯 Lesson Goal

Is lesson me hum cover karenge:

- citation aur source traceability ka difference
- application-controlled source IDs
- source map architecture
- claim-level citations
- citation hallucination
- citation validation
- source version/freshness metadata
- current incident evidence vs reference source
- UI/display considerations
- audit/debugging value

---

# PART 1 — Why Citations Matter

Without citations:

```text
The Terraform networking change likely caused the AKS connectivity issue.
```

User asks:

```text
Based on what?
```

With citations:

```text
Terraform networking changes can modify NSG rules [S1], and AKS subnet communication depends on required network rules [S2].
```

Now user can inspect S1/S2.

---

# PART 2 — English Definition

**Citation** is a reference in the generated answer to a supplied evidence identifier.

**Source traceability** is the system capability to map that identifier back to the exact source document, chunk, version, and relevant metadata.

```text
Citation = [S2]
Traceability = S2 → document → chunk → version → metadata
```

---

# PART 3 — Application-Controlled Source Map

```python
source_map = {
    "S1": {
        "source": "terraform-networking.md",
        "chunk_id": "tf-net-004",
        "version": "2026-08",
        "status": "approved",
    },
    "S2": {
        "source": "aks-networking.md",
        "chunk_id": "aks-net-002",
        "version": "2026-07",
        "status": "approved",
    },
}
```

LLM receives labels; application owns mapping.

Why?

```text
LLM output is probabilistic
source identity should be deterministic
```

---

# PART 4 — Citation Hallucination

Allowed:

```text
S1, S2, S3
```

Model outputs:

```text
This is confirmed by [S7].
```

Problem:

```text
S7 does not exist
```

Validator should catch this.

Example:

```python
import re

used = set(re.findall(r"\[(S\d+)\]", answer))
allowed = set(source_map)
invalid = used - allowed

if invalid:
    print("Invalid citations:", invalid)
```

---

# PART 5 — Citation Presence Is Not Citation Correctness

Answer:

```text
The outage lasted 2 hours [S1].
```

S1 says only:

```text
AKS subnet connectivity validation failed.
```

Citation ID valid hai, but claim unsupported.

So two checks:

```text
1. Citation validity
2. Citation entailment/support
```

Second one harder hai and evaluation/claim validation may be required.

---

# PART 6 — Claim-Level vs Paragraph-Level Citations

Weak:

```text
Several things happened during the incident. [S1][S2][S3]
```

Better:

```text
Terraform Apply removed the subnet allow rule [S1].
Connectivity validation then failed [S2].
The deployment failed during Terraform Apply [S3].
```

Claim-level citations improve reviewability.

---

# PART 7 — Source Metadata to Preserve

Useful fields:

```text
source
chunk_id
section
version
updated_at
status
owner
environment
content_type
```

For incident evidence:

```text
timestamp
pipeline_run_id
cluster
subscription
```

Traceability means source is not just a filename.

---

# PART 8 — Current Evidence vs Reference Documentation

Source map can include:

```python
"evidence_type": "current_incident"
```

or:

```python
"evidence_type": "reference_runbook"
```

This allows answer to say:

```text
Current evidence confirms X [S1].
The runbook states Y is a known failure mode [S2].
```

instead of pretending Y happened now.

---

# PART 9 — Source Display

Useful final output:

```text
Sources:
[S1] terraform-networking.md — NSG Changes — version 2026-08
[S2] aks-networking.md — Network Requirements — version 2026-07
```

For production UI, source link may point to authorized internal document location.

Never expose a source user is not authorized to access.

---

# PART 10 — Traceability for Debugging

Wrong answer investigation:

```text
Answer claim
   ↓
Citation [S2]
   ↓
Chunk ID
   ↓
Original document section
   ↓
Was retrieval wrong or generation wrong?
```

Without traceability, debugging becomes guesswork.

---

# PART 11 — Citation Validation Flow

```text
LLM Answer
   ↓
Extract citation IDs
   ↓
Compare against allowed source map
   ↓
Invalid ID?
   ├── yes → reject/retry/flag
   └── no  → continue
   ↓
Optional claim-support validation
```

---

# PART 12 — Missing Citations

If prompt requires citations but answer contains none:

```text
status = CITATION_MISSING
```

Possible handling:

```text
retry once with strict prompt
or
return answer with validation warning
```

Do not silently claim fully grounded output.

---

# PART 13 — DevOps Example

Evidence:

```text
[S1] Current pipeline log: Terraform Apply failed.
[S2] Terraform diff: aks-subnet-allow removed.
[S3] Runbook: removing required AKS subnet rules can break connectivity.
```

Good answer:

```text
Confirmed facts:
- The pipeline failed during Terraform Apply [S1].
- The Terraform change removed `aks-subnet-allow` [S2].

Inference:
- The removed rule is a strong candidate for the connectivity issue because the runbook identifies required subnet rules as necessary for AKS communication [S3].
```

This clearly separates current evidence and reference knowledge.

---

# PART 14 — Common Mistakes

1. Letting model invent source labels.
2. Showing filename only, no chunk/section/version.
3. Assuming valid citation means supported claim.
4. Returning inaccessible source links.
5. Losing source IDs during context truncation.
6. Using stale document without version metadata.
7. One citation at end of huge paragraph with many unrelated claims.

---

# PART 15 — Interview Corner

### Q1. Why are citations useful in RAG?

They make answers reviewable and connect generated claims to retrieved evidence.

### Q2. What is citation hallucination?

The model references a source identifier that was never supplied.

### Q3. How do you prevent it?

Create source IDs in application code, keep an allowed source map, and validate generated citation IDs.

### Q4. Does a valid source ID prove the claim is supported?

No. Citation validity and semantic claim support are separate checks.

### Q5. Why preserve version metadata?

To detect and avoid stale or superseded knowledge.

---

# PART 16 — Revision

```text
Context block → application creates S1/S2
LLM → cites S1/S2
Validator → checks allowed IDs
Source map → resolves exact chunk/version

Citation = reference
Traceability = full mapping
```

---

# PART 17 — Homework

1. Build a `source_map` for 3 DevOps chunks.
2. Write regex validation for `[S99]`.
3. Create one valid citation but unsupported claim example.
4. Add `version`, `status`, and `evidence_type` to source metadata.
5. Design final Sources section for an incident assistant.

---

# 🔗 Why Lesson 7 Next?

Traceable output ready hai. But users often ask vague questions:

```text
prod broken after change
```

Retriever may perform better if query is normalized or expanded safely.

Next lesson me hum **query rewriting aur multi-query retrieval** samjhenge.
