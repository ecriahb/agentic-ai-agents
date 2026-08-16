# 🚩 Jai Bajrangbali!

# Lesson 05 — Context Window

> **Context Window = model ki working memory jisme current task ke relevant tokens fit hote hain.**

## Why This Topic Now?

Lesson 4 me samjha ki Transformer context ke relationships process karta hai. Lekin model ek response ke waqt unlimited information consider nahi karta.

```text
Transformer uses context
        ↓
But context is finite
        ↓
Context Window
```

## 🎬 Exam Desk Analogy

Context window ko exam desk samjho.

Tumhare paas library me 100 books hain, lekin exam ke waqt desk par sirf kuch material open hai.

```text
Entire Knowledge / Files / Systems
             ↓
      Selected Information
             ↓
        Context Window
             ↓
           Answer
```

Model ke answer par current prompt, conversation history, supplied code, retrieved documents aur tool results ka effect ho sakta hai — agar wo available context me hain.

## 🇬🇧 English Definition

> **A context window is the amount of tokenized information a language model can consider within a request or conversation while generating a response.**

## Context Me Kya Aa Sakta Hai?

Depending on the application/provider:

```text
System / developer instructions
User prompt
Conversation history
Retrieved documents
Code
Logs
Tool results
Structured data
Generated tokens
```

Exact context accounting model/provider specific hota hai.

## 💼 DevOps Example

Weak context:

```text
AKS is not working. Fix it.
```

Model ko nahi pata:
- which cluster?
- environment?
- what changed?
- error?
- pod status?
- network?

Better context:

```text
Environment: production
Cluster: prod-aks
Failure started after Terraform Apply
Terraform diff: AKS subnet NSG allow rule removed
AKS status: Degraded - network connectivity failures
Pipeline stage: Terraform Apply
```

Ab analysis targeted ho sakta hai.

## More Context ≠ Better Context

Bahut important rule:

> **More data is not automatically better. Relevant data is better.**

Suppose pipeline log me 100,000 lines hain aur actual error last 30 lines me hai.

Bad architecture:

```text
100,000 lines
    ↓
LLM
```

Better architecture:

```text
Logs
 ↓
Filter / Search / Parse
 ↓
Relevant error + surrounding context
 ↓
LLM
```

Benefits:
- less token usage
- less latency
- less noise
- often better focus
- easier auditing

## Context Quality Dimensions

Good context should be:

1. **Relevant** — task se related.
2. **Trusted** — reliable source se.
3. **Recent** — current incident ke liye updated.
4. **Sufficient** — conclusion support karne layak.
5. **Minimal enough** — unnecessary noise avoid karo.

## Context vs Model Knowledge

Question:

```text
What is AKS?
```

General model knowledge enough ho sakti hai.

Question:

```text
Why did MY production deployment fail 5 minutes ago?
```

Model training knowledge enough nahi. Current evidence chahiye:

```text
Pipeline logs
Terraform changes
AKS state
Metrics
```

Ye distinction future tool calling aur RAG ka foundation hai.

## Context Window Limit Hit Ho To?

Architecture options:

```text
Chunk large input
Filter first
Summarize carefully
Retrieve only relevant documents
Use tools to query targeted evidence
Keep concise conversation state
```

But summary bhi information lose kar sakti hai, so critical evidence ko preserve karna important hai.

## Common Mistakes

- Entire logs blindly paste karna. ❌
- Assume model ko project history automatically pata hai. ❌
- Relevant evidence omit karna. ❌
- Stale data ko current fact samajhna. ❌
- More tokens = more intelligence. ❌

## 🎯 Interview Corner

### Q. What is an LLM context window?

**Answer:**
> The context window is the amount of tokenized information the model can consider during a request, including instructions, user input, conversation history, retrieved data, and potentially generated output depending on the model interface.

### Q. Why is context engineering important in DevOps AI systems?

**Answer:**
> Operational problems depend on current evidence. Providing relevant pipeline logs, infrastructure changes, Kubernetes events, and monitoring signals improves grounding while filtering unnecessary data reduces noise, cost, and latency.

## 🧠 Remember This

> **Right context > More context.**

And:

> **For current system state, get evidence from current systems rather than relying on model memory.**

## 📝 Homework

Production AKS incident investigate karne ke liye 10 useful context items list karo.

Then mark each one as:
- Must Have
- Useful
- Optional

## Why the Next Lesson Follows

Ab samajh aa gaya ki context missing/incomplete ho sakta hai.

Natural question:

> **Agar reliable evidence missing ho, kya model simply “I don't know” bolta hai?**

Kabhi-kabhi nahi. Plausible but wrong answer generate ho sakta hai.

➡️ **Next: Lesson 06 — Hallucination**
