# 🚩 Jai Bajrangbali!

# Lesson 04 — JSON for AI Applications

> **AI APIs ke request aur response ko samajhne ke liye JSON padhna almost mandatory skill hai.**

---

## 🎯 Lesson Goal

Aap samjhoge:

- JSON kya hai
- object, array, string, number, boolean, null
- nested JSON
- Python dict/list vs JSON
- serialization/deserialization
- AI request/response payloads
- safe parsing and common errors

---

## 1. JSON Kya Hai?

**English Definition:**
> JSON (JavaScript Object Notation) is a text-based data interchange format used to represent structured data.

JSON human-readable bhi hai aur machines ke liye parse karna easy hai.

Example:

```json
{
  "environment": "production",
  "status": "failed",
  "attempt": 3,
  "healthy": false
}
```

---

## 2. JSON Data Types

```text
Object   → { }
Array    → [ ]
String   → "text"
Number   → 10, 3.14
Boolean  → true / false
Null     → null
```

Nested example:

```json
{
  "cluster": "prod-aks",
  "pods": [
    {"name": "api-1", "status": "Running"},
    {"name": "api-2", "status": "CrashLoopBackOff"}
  ]
}
```

---

## 3. Python Dict vs JSON

Python object:

```python
incident = {
    "service": "payments",
    "failed": True,
    "error": None
}
```

JSON text:

```json
{
  "service": "payments",
  "failed": true,
  "error": null
}
```

Important difference:

```text
Python True  → JSON true
Python False → JSON false
Python None  → JSON null
```

---

## 4. Serialization and Deserialization

**Serialization** = Python object → JSON text.

```python
import json

payload = {"cluster": "prod-aks", "status": "degraded"}
json_text = json.dumps(payload, indent=2)
print(json_text)
```

**Deserialization** = JSON text → Python object.

```python
parsed = json.loads(json_text)
print(parsed["cluster"])
```

With `requests`:

```python
response.json()
```

usually converts JSON response body into Python data structures.

---

## 5. Why JSON Matters for AI

AI request:

```json
{
  "model": "example-model",
  "messages": [
    {"role": "system", "content": "You are a DevOps incident analyst."},
    {"role": "user", "content": "Analyze the failure."}
  ]
}
```

AI response may contain nested structures:

```json
{
  "id": "response-123",
  "output": [
    {
      "type": "message",
      "content": [
        {"type": "output_text", "text": "Likely root cause..."}
      ]
    }
  ]
}
```

Aapko exact provider shape docs se check karna hota hai. Memory se field assume karna reliable nahi.

---

## 6. JSON Is Not Validation

Ye JSON syntactically valid ho sakta hai:

```json
{
  "severity": "banana"
}
```

But business contract ke according invalid ho sakta hai.

So:

```text
Valid JSON
   ≠
Valid Application Data
```

Later structured response lesson me schema validation isi problem ko solve karega.

---

## 7. Safe Parsing

```python
try:
    data = response.json()
except ValueError:
    print("Response body valid JSON nahi hai")
```

Never assume every API error JSON me hi aayega. Proxy/load balancer kabhi HTML/text response de sakta hai.

---

# 🧪 Practical

```python
import json

incident = {
    "environment": "production",
    "pipeline": "deploy-api",
    "errors": [
        "Terraform apply failed",
        "AKS connectivity validation failed"
    ]
}

print("Python object:")
print(incident)

print("\nJSON string:")
print(json.dumps(incident, indent=2))
```

---

# ❌ Common Mistakes

- single quotes ko JSON syntax samajhna
- trailing commas
- Python dict aur raw JSON string ko same treat karna
- nested field path galat access karna
- `response.text` aur `response.json()` difference ignore karna
- syntactically valid JSON ko automatically trustworthy data samajhna

---

# 🎤 Interview Point

**Q: Why is JSON widely used in APIs?**

It is lightweight, human-readable, language-independent in practice, and maps naturally to common programming data structures.

---

# 🔁 Why Next Lesson?

Ab hum request bhej sakte hain aur JSON samajh sakte hain. But protected API puchegi:

```text
Who are you?
Are you allowed?
```

> **Lesson 05 — Authentication & API Keys**
