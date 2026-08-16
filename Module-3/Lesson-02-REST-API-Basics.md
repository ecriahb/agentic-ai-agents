# 🚩 Jai Bajrangbali!

# Lesson 02 — REST API Basics

> **API communication samajhne ke baad next step hai REST ka pattern samajhna — kyunki Azure, GitHub, monitoring systems aur bahut saare AI platforms REST concepts use karte hain.**

---

## 🎯 Lesson Goal

Aap samjhoge:

- REST kya hai
- Resource kya hota hai
- URL structure
- Stateless communication
- CRUD mapping
- Path parameter vs query parameter
- REST APIs ka DevOps me use

---

## 1. REST Kya Hai?

**English Definition:**
> REST (Representational State Transfer) is an architectural style for designing network APIs around resources and standard HTTP behavior.

REST koi programming language nahi hai.

REST koi tool nahi hai.

REST ek **design style** hai.

---

## 2. Resource Kya Hota Hai?

REST APIs usually kisi resource ke around designed hoti hain.

Examples:

```text
/users
/repos
/pipelines
/builds
/clusters
/deployments
```

DevOps example:

```text
GET /clusters/prod-aks
```

Yahan `prod-aks` ek specific resource identify karta hai.

---

## 3. URL Mental Model

```text
https://api.example.com/v1/clusters/prod-aks
└──── base URL ─────┘ └──── resource path ────┘
```

Possible query:

```text
?status=failed&limit=10
```

Full conceptual URL:

```text
https://api.example.com/v1/pipelines?status=failed&limit=10
```

---

## 4. Path Parameter vs Query Parameter

Path parameter usually ek specific resource identify karta hai:

```text
/pipelines/12345
```

Query parameter filtering, sorting ya options ke liye hota hai:

```text
/pipelines?status=failed
```

Easy rule:

```text
Which exact thing? → path
How should I filter/view it? → query
```

---

## 5. Stateless Kya Hota Hai?

**English Definition:**
> Stateless means each request should contain enough information for the server to understand and process that request independently.

Conceptually:

```text
Request 1 → complete information
Request 2 → complete information
Request 3 → complete information
```

Server ko blindly previous request yaad rakhne par depend nahi karna chahiye.

AI conversation APIs me conversation state application side, message history, thread/session object, or provider-specific mechanism se manage ho sakta hai. Isliye REST statelessness ko "LLM kabhi context retain nahi karta" samajhna wrong hoga.

---

## 6. CRUD and REST

Common mapping:

| CRUD | HTTP Method | Meaning |
|---|---|---|
| Create | POST | New resource create |
| Read | GET | Existing resource fetch |
| Update | PUT/PATCH | Resource modify |
| Delete | DELETE | Resource remove |

Example:

```text
GET    /deployments
POST   /deployments
PATCH  /deployments/123
DELETE /deployments/123
```

---

## 7. Representation

REST resource khud network par physically travel nahi karta.

Uski **representation** travel karti hai, often JSON:

```json
{
  "name": "prod-aks",
  "status": "degraded"
}
```

---

# 🛠️ DevOps Example

Imagine deployment investigation tool:

```text
GET /pipeline-runs/987
        ↓
JSON response
        ↓
status = failed
stage = terraform-apply
```

Then another request:

```text
GET /pipeline-runs/987/logs
```

Agent multiple REST resources se evidence collect kar sakta hai.

---

# ❌ Common Confusions

- REST = HTTP nahi. REST generally HTTP use karta hai, but concepts separate hain.
- JSON = REST nahi. JSON sirf common representation format hai.
- GET ka matlab browser page only nahi; APIs me data fetch karna hota hai.
- URL me secret/API key rakhna generally unsafe pattern hai.

---

# 🎤 Interview Point

**Q: What makes an API RESTful?**

A REST-style API models operations around resources, uses standard HTTP semantics, keeps requests self-contained, and exchanges resource representations such as JSON.

---

# 🔁 Why Next Lesson?

REST me humne resources samjhe. Ab actual request ka behavior samajhne ke liye HTTP ka knowledge chahiye:

> **Lesson 03 — HTTP Methods, Request & Response**
