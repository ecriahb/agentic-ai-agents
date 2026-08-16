# 🚩 Jai Bajrangbali!

# Lesson 12 — Structured Reasoning / Structured Investigation

> **Complex problem ko observable, reviewable investigation stages me break karo.**

## Why This Topic Now?

Lesson 11 me examples se output pattern guide karna seekha. But DevOps troubleshooting sirf final format ka problem nahi hai. Correct investigation ke liye systematic evidence collection chahiye.

```text
Examples teach output pattern
          ↓
Complex incident still needs a workflow
          ↓
Structured Investigation
```

## 🎬 Senior Engineer Analogy

Production AKS slow hai.

Junior guess:

```text
“Pod restart kar dete hain.”
```

Senior engineer:

```text
1. Scope impact
2. Check recent changes
3. Check pipeline/deployment
4. Check pods and events
5. Check CPU/memory/HPA
6. Check network/DNS
7. Check dependencies
8. Check metrics/logs/traces
9. Correlate evidence
10. Recommend action
```

Difference: **guess vs investigation**.

## 🇬🇧 English Definition

> **Structured reasoning in an engineering workflow means decomposing a complex task into explicit, reviewable stages that collect and evaluate evidence before producing a conclusion or recommendation.**

Important nuance: goal model ka hidden private chain-of-thought capture karna nahi. Production design me observable steps, tool calls, evidence and decisions chahiye.

## Visual Flow

```text
IDENTIFY
   ↓
COLLECT
   ↓
ANALYZE
   ↓
CORRELATE
   ↓
VERIFY
   ↓
CONCLUDE
```

## DevOps Example — AKS Deployment Failure

### Step 1 — Identify Scope

```text
Environment: production
Cluster: prod-aks
Failure stage: deployment
```

### Step 2 — Recent Change

```text
Was there Terraform / Helm / YAML / image change?
```

### Step 3 — Pipeline Evidence

```text
Which stage failed?
What exact error occurred?
```

### Step 4 — Infrastructure Evidence

```text
Terraform plan/apply
NSG/UDR changes
identity changes
DNS/private endpoint changes
```

### Step 5 — Kubernetes Evidence

```text
kubectl events
pod status
container logs
readiness/liveness
node condition
```

### Step 6 — Observability

```text
Azure Monitor
Application Insights
metrics
traces
```

### Step 7 — Correlate

Does timing match?

```text
Terraform networking change @ 10:04
Connectivity failures start @ 10:05
Deployment failure @ 10:05
```

### Step 8 — Conclusion

Separate:

```text
Confirmed Evidence
Likely Root Cause
Confirmed Impact
Recommended Fix
Unknowns
```

## Why Structured Workflow Helps

### Completeness
Important evidence categories miss hone ka chance reduce hota hai.

### Reviewability
Human reviewer dekh sakta hai agent ne kya check kiya.

### Traceability
Tool calls and observations audit trail ban sakte hain.

### Safer autonomy
Agent ko bounded actions aur stop conditions diye ja sakte hain.

## Future Agent Connection

Later agent loop basically isi pattern ko automate karega:

```text
Goal
 ↓
LLM chooses next tool
 ↓
Application executes tool
 ↓
Observation
 ↓
LLM decides if more evidence needed
 ↓
Final answer
```

But model ko unlimited free-form authority nahi denge.

## Structured Reasoning vs Structured Output

Different concepts:

```text
Structured Investigation
= problem solve karne ka workflow

Structured Output
= final answer ka machine-readable shape
```

Example:

```text
Investigation: Pipeline → Terraform → AKS → Metrics
Output: JSON {evidence, root_cause, impact, fix}
```

## Common Mistakes

- First symptom ko root cause declare karna. ❌
- Tool output collect karna but correlate na karna. ❌
- Missing evidence ko assumption se fill karna. ❌
- Hidden reasoning text ko audit trail samajhna. ❌
- Investigation me no stop condition. ❌
- Same tool repeatedly call karna without freshness reason. ❌

## 🎯 Interview Corner

### Q. Why use a structured troubleshooting workflow with an AI agent?

**Answer:**
> A structured workflow improves completeness, traceability, and reviewability. It allows the system to collect specific evidence from known sources, correlate observations, validate conclusions, and expose an auditable sequence of tool calls rather than relying on an unsupported one-shot guess.

## 🧠 Remember This

> **Complex problem → structured evidence collection → reviewable conclusion.**

## 📝 Homework

“AKS application is slow” ke liye 8–10 step investigation workflow banao.

Each step me mention karo:
- what to check
- which tool/source
- what evidence will be collected

## Why the Next Lesson Follows

Jitna agent more tools use karega aur actions suggest karega, utna risk bhi badhega.

So autonomy se pehle safety samajhna mandatory hai.

➡️ **Next: Lesson 13 — AI Limitations & Safety**
