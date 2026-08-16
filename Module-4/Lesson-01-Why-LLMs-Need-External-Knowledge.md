# Lesson 01 — Why LLMs Need External Knowledge

> **LLM powerful hai, lekin har private, latest ya company-specific fact uske paas automatically nahi hota.**

## 🎯 Lesson Goal

Is lesson me samjhenge ki model knowledge aur external knowledge alag cheezein hain, aur DevOps AI assistant ko runbooks, logs, architecture docs aur incident history se connect karna kyu zaroori hai.

## English Definition

**External knowledge** is information supplied to an AI application from sources outside the model's built-in learned parameters.

## Hinglish Explanation

Agar aap model se poochho:

```text
What is Kubernetes?
```

model general answer de sakta hai.

Lekin agar poochho:

```text
Hamare prod-aks cluster me deployment fail hone ka latest known runbook kya hai?
```

ye company-specific knowledge hai. Model ko ye tabhi pata chalega jab application relevant document retrieve karke context me de.

## Knowledge Categories

```text
LLM Built-in Knowledge
- generic concepts
- language patterns
- public learned information

External Knowledge
- private runbooks
- architecture docs
- latest incidents
- Terraform standards
- pipeline logs
- internal SOPs
```

## DevOps Example

Suppose incident:

```text
Deployment failed during Terraform Apply
```

Possible internal evidence:

```text
runbook-aks-networking.md
incident-2026-nsg-removal.md
terraform-network-policy.md
```

Without these documents, model generic suggestions de sakta hai. With relevant documents, answer environment-specific ho sakta hai.

## Why Not Send Every Document?

Because:

- context window finite hota hai
- irrelevant text model ko distract kar sakta hai
- cost/latency badh sakti hai
- relevant evidence buried ho sakta hai

So problem becomes:

```text
Thousands of documents
        ↓
Which few are relevant to this query?
```

Yahin se embeddings aur vector search ki need aati hai.

## Common Confusion

**Fine-tuning ≠ knowledge retrieval.** Fine-tuning behavior/style/task adaptation ke liye useful ho sakta hai; frequently changing private knowledge ke liye retrieval often better pattern hota hai.

## Interview Point

**Q: Why do enterprise LLM apps need retrieval?**

Because enterprise answers often depend on private, current, source-specific information that should be fetched at query time rather than assumed to exist inside the model.

## Next Lesson Kyu?

Ab hume relevant documents automatically find karne hain. Keyword search ek option hai, lekin meaning-based search ke liye pehle **embeddings** samajhna padega.
