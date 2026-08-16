# 🚩 Jai Bajrangbali!

# Lesson 03 — System Prompt vs User Prompt

> **Permanent behavior rules alag rakho; runtime incident request alag.**

## 🎯 Goal
System prompt aur user prompt ka responsibility split samajhna.

## System Prompt
Application-level behavior define karta hai:

```text
You are a DevOps incident analysis assistant.
Use evidence-first reasoning.
Never invent tool results.
Separate facts from hypotheses.
Do not recommend destructive actions without explicit approval.
```

## User Prompt
Current runtime request deta hai:

```text
Analyze today's production AKS deployment failure using the attached pipeline evidence.
Return Root Cause, Impact, Validation and Fix.
```

## Mental Model

```text
System Prompt = operating policy
User Prompt   = current job/request
Evidence      = current facts
```

## Bad Design
Har user request me permanent safety rules repeat karna:

```text
Analyze this log and remember not to hallucinate and never delete...
```

## Better Design

```text
SYSTEM:
You are a read-only DevOps investigation assistant...

USER:
Analyze production pipeline failure for deployment 8421.

EVIDENCE:
<logs>
```

## Conflict Thinking
A production application should treat critical controls as host-enforced rules, not only prompt text.

```text
System instruction
      +
Tool allowlist
      +
Argument validation
      +
RBAC
      +
Approval
```

## DevOps Example

System:
```text
Never claim downtime unless supplied evidence confirms customer impact.
When evidence is incomplete, say "Insufficient evidence".
```

User:
```text
Terraform Apply failed after an NSG change. Analyze the likely cause.
```

Result: user can change the task, but permanent evidence policy remains consistent.

## Python Mental Example

```python
system_prompt = """You are a grounded DevOps incident analyst..."""
user_prompt = """Analyze this pipeline failure..."""
```

## Key Rule
System prompt is **not a security sandbox**. If the model has access to dangerous tools, application-side authorization is mandatory.

## 🔑 Summary

```text
System = stable behavior
User   = dynamic task
Context = dynamic evidence
```

## ➡️ Why Next?
Ab hum dekhenge examples dene se model behavior kaise change hota hai: Zero-shot, One-shot, Few-shot.
