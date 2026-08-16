# 🚩 Jai Bajrangbali!

# Lesson 05 — First API Call & Response Object

> **AI ka parcel kholte hain.**

## Why This Topic Now?

Model answer sirf plain string ke roop me return nahi hota. SDK ek richer response object deta hai jisme text, model metadata, status aur usage jaise fields ho sakte hain.

```text
Cloud / Local API Call
          ↓
Response Object
          ↓
Tokens + Cost
```

## The Key Line, Slowly

```python
response = client.responses.create(
    model="gemma3:1b",
    input="Explain AKS in two simple lines."
)
```

### Meaning

- `client` — SDK ke through provider se communicate karne wala object
- `responses` — Responses API resource
- `create()` — new response generate karne ki request
- `model` — kaunsa existing model use hoga
- `input` — task/context jo model ko diya gaya
- `response =` — complete returned object ko variable me store karna

## Useful Fields

```python
print("ID:", response.id)
print("Model:", response.model)
print("Status:", response.status)
print("Usage:", response.usage)
print("Answer:", response.output_text)
```

| Field | Meaning |
|---|---|
| `response.id` | Unique response identifier |
| `response.model` | Model that produced the response |
| `response.status` | Execution state |
| `response.output` | Structured output items/messages/tool calls |
| `response.output_text` | Generated text ka convenient access |
| `response.usage` | Token/accounting usage information |

## Parcel Analogy

```text
response
   ↓
Complete parcel
   ├── ID
   ├── Model
   ├── Status
   ├── Usage
   └── Output Text
```

> **`response` = complete parcel**
>
> **`response.output_text` = parcel ke andar ka useful answer**

## Example Lab Output

```text
ID: resp_320920
Model: gemma3:1b
Status: completed
Input Tokens: 17
Output Tokens: 41
Total Tokens: 58
Answer: ...
```

## 🎯 Interview Corner

### Q. What is the Response object?

**Answer:**
> The Response object represents the result of a model request. It can contain generated output, identifiers, model and status metadata, token usage, and other structured items required by an application.

## 🧠 Remember This

> **Application ko sirf answer nahi milta; application ko result + metadata + usage mil sakta hai.**

## Why the Next Lesson Follows

Response object me input/output token usage dikha. Ab samajhna hai tokens kya hain aur DevOps application me context, latency aur cost ko kaise affect karte hain.

➡️ **Next: Lesson 06 — Tokens, Cost & Context Engineering**
