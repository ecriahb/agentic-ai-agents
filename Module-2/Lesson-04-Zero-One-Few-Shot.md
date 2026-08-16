# 🚩 Jai Bajrangbali!

# Lesson 04 — Zero-shot / One-shot / Few-shot

> **Sometimes instruction enough hoti hai; sometimes example output model ko pattern samjhata hai.**

## 🎯 Goal
Zero-shot, one-shot aur few-shot prompting ko DevOps use-cases ke saath samajhna.

---

## 1. Zero-shot
No example. Sirf instruction.

```text
Classify this incident severity as Low, Medium, High or Critical.
Explain the evidence in one sentence.

Incident:
Terraform Apply failed in production before application rollout started.
```

Best when:
- task simple ho
- labels obvious hon
- output format easy ho

---

## 2. One-shot
Ek example diya jata hai.

```text
Example:
Input: Staging deployment failed during unit tests.
Output: Medium — deployment blocked, but production unaffected.

Now classify:
Input: Production deployment failed during Terraform Apply.
```

Useful when desired interpretation ya formatting model ko dikhani ho.

---

## 3. Few-shot
Multiple examples se pattern establish hota hai.

```text
Example 1
Input: Dev lint failed.
Output: Low

Example 2
Input: Staging deployment blocked before release.
Output: Medium

Example 3
Input: Production service unavailable for customers.
Output: Critical

Now classify:
Input: Production Terraform apply failed; customer impact unknown.
```

Expected behavior: model should not jump to Critical just because word production appears.

---

## When Few-shot Helps

- custom severity policy
- organization-specific incident categories
- normalized output wording
- Terraform risk classification
- log/event tagging
- ticket routing

## When Few-shot Hurts
Too many irrelevant examples context consume karte hain aur model ko wrong pattern sikha sakte hain.

```text
More examples ≠ automatically better
Relevant examples > many examples
```

---

## DevOps Example — Terraform Risk

```text
Example:
Change: add tag to resource group
Risk: Low
Reason: metadata-only change

Example:
Change: delete production subnet NSG rule
Risk: High
Reason: may affect network connectivity

Now evaluate:
Change: replace AKS route table association
```

Constraint add karo:

```text
Do not infer outage. Rate the change risk, not actual impact.
```

---

## 🔑 Summary

```text
Zero-shot = instruction only
One-shot  = one example
Few-shot  = several examples
```

Choose based on task ambiguity and output consistency needs.

## ➡️ Why Next?
Ab prompting techniques ko actual DevOps workflows—RCA, Terraform review, pipeline failure—me structure karenge.
