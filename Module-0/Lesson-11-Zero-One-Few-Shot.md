# 🚩 Jai Bajrangbali!

# Lesson 11 — Zero-Shot, One-Shot & Few-Shot Prompting

> **Examples model ko current task ka desired pattern demonstrate karte hain.**

## Why This Topic Now?

Lesson 10 me role se perspective set kiya. Ab agar hume exact enterprise style, label order ya output pattern guide karna ho to examples useful ho sakte hain.

```text
Role tells perspective
       ↓
Examples demonstrate pattern
       ↓
More consistent task behavior
```

## 🎬 New Engineer Analogy

Manager new engineer ko bolta hai:

```text
“Incident RCA banao.”
```

### Zero-Shot
Koi example nahi diya.

Engineer apni understanding se RCA banayega.

### One-Shot
Ek approved RCA sample diya.

Engineer ko pattern samajh aata hai.

### Few-Shot
2–5 representative approved RCAs diye.

Engineer ko recurring structure aur tone aur clear ho jata hai.

LLM prompting me bhi similar mental model useful hai.

## 🇬🇧 English Definitions

> **Zero-shot prompting asks the model to perform a task without providing an example.**

> **One-shot prompting provides one example of the desired behavior or output before the new task.**

> **Few-shot prompting provides multiple examples to demonstrate the desired pattern.**

## Visual Flow

```text
ZERO-SHOT
Instruction → New Task → Output

ONE-SHOT
Instruction + 1 Example → New Task → Output

FEW-SHOT
Instruction + Multiple Examples → New Task → Output
```

## DevOps Example — RCA Format

### Example 1

```text
Evidence:
Terraform Apply failed after an NSG rule removal.

Root Cause:
The removed rule disrupted required subnet connectivity.

Impact:
Deployment failed.

Fix:
Restore the required NSG rule and validate connectivity.
```

### Example 2

```text
Evidence:
Pod events show ImagePullBackOff after registry credential change.

Root Cause:
The workload could not authenticate to the container registry.

Impact:
New pods could not start.

Fix:
Correct registry authentication and redeploy.
```

Then new task:

```text
Generate an RCA for this new incident using the same structure.
```

Model ko desired labels/pattern demonstrate ho gaya.

## Few-Shot Is Not Fine-Tuning

Very important distinction:

Few-shot examples current prompt/context me diye jaate hain.

```text
Few-Shot
= temporary in-context examples
```

Model ke weights permanently train/update nahi ho rahe.

```text
Fine-Tuning
= model training/customization process
```

Dono ko confuse mat karo.

## Examples Quality Matters

Garbage examples:

```text
Wrong RCA
Poor formatting
Unsupported assumptions
```

Model ko wrong pattern teach kar sakte hain.

Golden rule:

> **Relevant examples teach the pattern; bad examples teach bad patterns.**

## Token Cost Tradeoff

Every example context tokens consume karta hai.

```text
1 Example  → some context
10 Examples → much more context
```

So more examples automatically better nahi.

Choose:
- representative examples
- correct examples
- concise examples
- diverse enough cases

## When to Use Which?

### Zero-Shot
Task straightforward hai aur format simple hai.

### One-Shot
One example se expected pattern clear ho sakta hai.

### Few-Shot
Consistency, labels, classification pattern, company tone ya demonstrated decisions important hain.

## Common Mistakes

- Few-shot = model training. ❌
- Maximum examples = maximum quality. ❌
- Incorrect examples use karna. ❌
- Example me secrets/customer data expose karna. ❌
- Examples ko evidence for current incident samajhna. ❌

## 🎯 Interview Corner

### Q. What is the difference between zero-shot and few-shot prompting?

**Answer:**
> Zero-shot prompting gives the model instructions without examples. Few-shot prompting adds multiple examples in the current context to demonstrate the expected pattern, structure, or behavior.

### Q. Is few-shot prompting the same as fine-tuning?

**Answer:**
> No. Few-shot examples are included at inference time in the prompt or context and do not permanently change the model weights. Fine-tuning is a training process that modifies model behavior through additional training data.

## 🧠 Remember This

> **Examples guide patterns; they do not magically add truth.**

## 📝 Homework

Create a few-shot prompt for a Pipeline Failure Investigation Assistant.

Include:
- system/role instruction
- 2 short approved RCA examples
- one new incident
- expected output structure

## Why the Next Lesson Follows

Examples output format guide karte hain.

Lekin complex incident me format enough nahi — investigation ka **order** bhi important hai.

➡️ **Next: Lesson 12 — Structured Reasoning / Structured Investigation**
