# Module 1 — Lesson 6: Tokens, Cost & Context Engineering

> **Goal:** Beginner ko samjhana ki model text ko tokens me process karta hai, context finite hota hai, aur hosted API usage/cost input-output volume se related hota hai.

## English definition
**Tokens are the units a language model processes, while the context window is the maximum amount of tokenized information the model can consider in a request.**

## Mental model

```text
Prompt + Evidence + History
        ↓ tokenization
Input Tokens
        ↓
LLM Context Window
        ↓
Generated Output Tokens
```

## Token != word
Ek word one token ho sakta hai, multiple tokens ho sakta hai, punctuation/code bhi tokens consume karte hain. Exact tokenization model-dependent hoti hai.

## Why DevOps engineer should care
Agar aap blindly full logs bhej doge:

```text
100 MB log
→ huge context
→ latency/cost/noise
→ important evidence bury
```

Better:

```text
Collect relevant evidence
→ normalize
→ remove noise/secrets
→ label sources
→ send only useful context
```

## Context engineering
Prompt engineering asks: **model ko kya instruction dein?**
Context engineering asks: **model ko kaunsi trusted information dein?**

Example:

```text
Bad context:
Entire pipeline log + unrelated build history + secrets

Better context:
[E1] Terraform Apply failed
[E2] NSG rule removed
[E3] AKS connectivity validation failed
```

## Hosted cost thinking
Hosted providers may meter input/output usage. Never hard-code pricing assumptions in course logic because pricing changes. Instead log usage metadata and consult current provider pricing when estimating cost.

Cost drivers conceptually:

```text
more input tokens
+ more output tokens
+ more requests
+ larger/more capable model tier
= potentially higher cost
```

## Local Ollama cost thinking
No per-call cloud API bill, but resources are not free:

- electricity
- CPU/GPU/RAM
- latency
- operational maintenance
- hardware capacity

## Context quality > context quantity
More context is not always better.

```text
Useful evidence density ↑
Noise ↓
Source labels ↑
Freshness ↑
```

## Practical exercise
Take a long sample incident log and create three versions:

1. full raw log
2. manually trimmed log
3. source-labeled evidence summary

Send same question to model and compare:

- answer relevance
- unsupported claims
- latency
- usage metadata (hosted path)

## Important distinction

```text
Context window != memory
Chat history != evidence
More tokens != more truth
Low token count != automatically better
```

## Production rules
- never send secrets just because context allows it
- cap input sizes
- summarize only when provenance is preserved
- keep current evidence separate from reference knowledge
- collect token/latency usage metrics
- apply request budgets

## Interview questions
1. Token aur word me difference?
2. Context window kya hai?
3. Large logs direct LLM ko dena risky kyun hai?
4. Context engineering prompt engineering se kaise different hai?
5. Local LLM truly zero-cost kyun nahi hai?

## Revision

```text
Tokens = processing units
Context window = finite working input/output space
Cost = provider usage concern
Context engineering = choose relevant trusted information
```

## Why next lesson?
Ab input size/context discipline clear hai. Next problem: free-text answer ko application reliably parse kaise kare? Isliye **Structured Output & Validation**.