# 🚩 Jai Bajrangbali!

# Lesson 08 — System Prompt vs User Prompt

> **System-level instructions define behavior; user input defines the current task.**

## Why This Topic Now?

Lesson 7 me strong prompt design seekha. Production AI app me har request ke saath same rules repeat karwana practical nahi.

```text
Permanent / Application Behavior
            ↓
      System Instructions
            +
Current User Request
            ↓
        User Prompt
```

Provider/API terminology exactly same nahi hoti everywhere, but mental model useful hai.

## 🎬 Manager Analogy

Company ke permanent rules:

```text
- Production change without approval mat karo.
- Evidence ke bina RCA confirm mat karo.
- Secrets expose mat karo.
```

Ye system-level rules jaise hain.

Daily ticket:

```text
“Production pipeline run 842 investigate karo.”
```

Ye user task jaise hai.

## 🇬🇧 English Definition

> **System-level instructions define the model's role, behavior, rules, and constraints for an application, while the user prompt provides the current request or task.**

## Simple Formula

```text
SYSTEM / APPLICATION RULES
        ↓
“How should you behave?”
        +
USER REQUEST
        ↓
“What should you do now?”
```

## DevOps Agent Example

### System Instructions

```text
You are a Senior Azure DevOps troubleshooting assistant.

Rules:
- Do not invent infrastructure facts.
- Use available evidence.
- Distinguish confirmed facts from likely conclusions.
- Do not execute destructive changes without human approval.
- Never expose secrets.
```

### User Request

```text
Investigate why production deployment failed.
Environment: production
AKS Cluster: prod-aks
```

Same system behavior can serve different incidents:

```text
User 1: Analyze pipeline 842
User 2: Analyze staging AKS incident
User 3: Review Terraform change
```

## Why Separation Matters

### Reusability
Common behavior ek central place par define hota hai.

### Governance
Policies application side se consistently apply ki ja sakti hain.

### Maintainability
Har user prompt me 20 rules repeat nahi karne.

### Security Design
User ko application safety policy define karne ka control nahi dena chahiye.

## But Important: System Prompt Is Not an Unbreakable Security Wall

Even strong system instructions ke bawajood:

- model can make mistakes
- prompt injection attempts ho sakte hain
- tool arguments wrong ho sakte hain
- unsafe recommendation aa sakti hai

So real control:

```text
Instructions
   +
Application Validation
   +
Tool Permissions
   +
Policy Checks
   +
Human Approval
```

## 💼 Practical Architecture

```text
Application starts
      ↓
Load Agent Rules
      ↓
Receive Incident Request
      ↓
Add Current Evidence
      ↓
Call Model
      ↓
Validate Result
```

## Common Mistakes

- System prompt ko secret security mechanism samajhna. ❌
- User task aur permanent policy mix kar dena. ❌
- Every request me same 50-line policy manually repeat karna. ❌
- User-provided text ko trusted instruction samajhna. ❌
- Prompt hierarchy/provider behavior ko universal assume karna. ❌

## 🎯 Interview Corner

### Q. What is the difference between system-level instructions and a user prompt?

**Answer:**
> System-level instructions define reusable application behavior, role, policies, and constraints. The user prompt provides the current task or request. Separating them helps consistency and governance, although code-level safety controls are still required.

### Q. Is a system prompt enough to secure an AI agent?

**Answer:**
> No. Prompts guide model behavior but should not be treated as a hard authorization boundary. Tool permissions, input validation, policy enforcement, least privilege, and approval gates must be implemented in application logic.

## 🧠 Remember This

> **System = how to behave. User = what to do now.**

## 📝 Homework

Write a 10-line system prompt for a Pipeline RCA Assistant.

It should include rules for:
- evidence
- hallucination
- secrets
- destructive actions
- human approval

Then write one separate user request for a production incident.

## Why the Next Lesson Follows

Ab instructions aur current task separate ho gaye.

But same valid prompt ka response wording har run me exactly same kyu nahi hota?

➡️ **Next: Lesson 09 — Temperature**
