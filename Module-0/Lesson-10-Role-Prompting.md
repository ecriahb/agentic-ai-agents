# 🚩 Jai Bajrangbali!

# Lesson 10 — Role Prompting

> **Role changes the response perspective, not the underlying model.**

## Why This Topic Now?

Lesson 9 me temperature se output diversity samjhi. Ab question hai: same technical problem ko different expert lens se kaise analyze karayein?

```text
Same Model
   ↓
Different Role / Perspective
   ↓
Different Focus, Vocabulary, Depth
```

## 🎬 Simple Example

Prompt 1:

```text
Explain this Terraform module.
```

Prompt 2:

```text
You are a Senior Azure DevOps Architect.
Review this Terraform module for reusability, deployment safety and maintainability.
```

Prompt 3:

```text
You are a Cloud Security Architect.
Review this Terraform module for identity, network exposure, secrets and policy risks.
```

Same underlying model, but expected review lens different.

## 🇬🇧 English Definition

> **Role Prompting assigns the model a specific professional role or persona to guide the style, depth, vocabulary, and perspective of its response.**

## DevOps Role Examples

```text
Senior Azure DevOps Architect
   → architecture, automation, delivery, maintainability

Security Architect
   → RBAC, secrets, network exposure, policy, compliance

SRE
   → reliability, SLOs, observability, failure modes

FinOps Consultant
   → utilization, sizing, waste, cost optimization

Technical Trainer
   → simple explanation, examples, learning sequence
```

## 💼 Same AKS Problem, Different Lenses

Incident:

```text
AKS application latency increased after deployment.
```

### SRE Lens
- latency metrics
- error rate
- saturation
- dependencies
- SLO impact

### DevOps Lens
- recent pipeline
- deployment manifest
- rollout strategy
- image/config changes

### Security Lens
- network policies
- authentication failures
- WAF/firewall/NSG changes

Role prompting useful hai because it narrows attention toward relevant dimensions.

## Role Is Not Knowledge Injection

Very important:

```text
“You are a Kubernetes expert”
```

likhne se model suddenly new knowledge download nahi karta.

Role:
- perspective guide karta hai
- tone guide karta hai
- likely focus areas influence karta hai

Role:
- missing logs create nahi karta
- incorrect model knowledge fix guarantee nahi karta
- current Azure state nahi jaanta without tools

## Role + Context Is Stronger

Weak:

```text
You are an Azure expert. Fix this.
```

Better:

```text
You are a Senior Azure DevOps Architect.
Production AKS deployment failed after Terraform removed an NSG subnet rule.
Use only the supplied evidence and return Evidence, Likely Root Cause and Fix.
```

Role gives lens; context gives facts.

## Role Stacking Carefully

Prompt:

```text
You are a DevOps Architect, Security Architect, FinOps Expert, SRE, DBA, Developer...
```

Overloading roles can make task unfocused.

Better: choose role according to current goal or run separate reviews.

```text
Terraform Change
     ├── DevOps Review
     ├── Security Review
     └── FinOps Review
```

## Common Mistakes

- Role = guaranteed expertise. ❌
- Role = factual grounding. ❌
- 10 unrelated roles ek hi prompt me डालना. ❌
- Role use karna but task/context vague rakhna. ❌
- Role ko evidence verification ka replacement banana. ❌

## 🎯 Interview Corner

### Q. What is role prompting?

**Answer:**
> Role prompting assigns the model a specific professional perspective or persona so that the response better reflects the expected vocabulary, depth, and evaluation lens for the task.

### Q. Does assigning an expert role make the model more accurate?

**Answer:**
> Not necessarily. A role can improve relevance and perspective, but factual accuracy still depends on model capability, trusted context, evidence, tools, and validation.

## 🧠 Remember This

> **Role gives perspective. Evidence gives grounding.**

## 📝 Homework

Daily DevOps work ke liye 5 useful AI roles likho and each role ka one use-case do.

Example:

```text
Role: FinOps Consultant
Use Case: Review Azure resources for cost optimization opportunities.
```

## Why the Next Lesson Follows

Role model ko perspective deta hai.

But company ka exact output pattern — for example your approved RCA format — model ko kaise demonstrate karein?

➡️ **Next: Lesson 11 — Zero-Shot, One-Shot & Few-Shot Prompting**
