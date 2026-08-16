# 🚩 Jai Bajrangbali!

# Lesson 05 — Authentication & API Keys

> **API reachable hona aur API authorized hona do alag problems hain.**

---

## 🎯 Lesson Goal

Aap samjhoge:

- Authentication vs Authorization
- API key kya hai
- Bearer token kya hai
- headers me credentials ka role
- 401 vs 403
- key rotation and least privilege
- managed identity / workload identity ka higher-level idea
- AI APIs ke secrets safely handle karna

---

## 1. Authentication vs Authorization

**Authentication:** Who are you?

**Authorization:** What are you allowed to do?

```text
Identity prove
    ↓
Authentication
    ↓
Permission check
    ↓
Authorization
```

Example:

```text
Valid Azure identity
      ↓
Authentication successful
      ↓
But no permission on resource
      ↓
Authorization fails
```

---

## 2. API Key Kya Hai?

**English Definition:**
> An API key is a secret credential used by an application to authenticate or identify itself to an API service.

Conceptual flow:

```text
Python App
   ↓ API key
Provider API
   ↓ verify
Request accepted/rejected
```

Important:

> API key password jaisa secret hai. GitHub repo me hard-code nahi karna.

---

## 3. Bearer Token

Many APIs use an HTTP header like:

```http
Authorization: Bearer <secret-token>
```

The word `Bearer` indicates that possession of the token is sufficient to present it for access according to server policy.

Do not log the full token.

---

## 4. API Key in Header

Provider-specific authentication shapes differ. A common pattern is:

```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
```

But never assume every provider uses the same header. Always follow that provider's official documentation.

OpenAI's official API documentation uses API keys with Bearer authentication and explicitly recommends loading keys securely from environment variables or a key management service rather than exposing them in client-side code.

---

## 5. 401 vs 403 Again

```text
401 Unauthorized
→ authentication credential missing/invalid/expired

403 Forbidden
→ authenticated identity lacks required permission
```

Debugging:

```text
401
 ↓
Key/token loaded?
Correct header?
Expired/revoked?
Correct endpoint/provider?

403
 ↓
Role/RBAC correct?
Resource scope correct?
Policy/network restrictions?
```

---

## 6. Least Privilege

**English Definition:**
> Least privilege means granting only the permissions required to perform the intended task.

DevOps AI agent example:

Bad:

```text
Agent gets Owner/Admin access to everything
```

Better:

```text
Read-only access for investigation
Human approval before remediation
Narrow write permissions only where required
```

---

## 7. Rotation

Secrets permanent nahi samajhne chahiye.

Good lifecycle:

```text
Create
 ↓
Store securely
 ↓
Use
 ↓
Monitor
 ↓
Rotate
 ↓
Revoke when unused/compromised
```

If key accidentally GitHub me commit ho gayi:

1. Key immediately revoke/rotate karo.
2. New key create karo.
3. Git history cleanup only secondary action hai — leaked credential ko still compromised treat karo.

---

## 8. Better Than Long-Lived Secrets

Cloud production scenarios me possible ho to identity-based authentication preferable ho sakta hai:

```text
Managed Identity
Workload Identity
Service Principal with controlled secret/certificate
OIDC federation
```

Goal:

```text
Fewer static secrets
+ short-lived credentials
+ auditable identity
```

---

# 🛠️ DevOps Example

AI assistant ko Azure logs read karne hain:

```text
Agent Application
       ↓
Workload Identity / Managed Identity
       ↓
Read permission
       ↓
Log Analytics / Azure resource
       ↓
Evidence
```

Production architecture me ye hard-coded admin API key se safer hai.

---

# ❌ Common Mistakes

- key source code me hard-code karna
- `.env` GitHub par commit karna
- secrets console logs me print karna
- one admin credential sab apps me reuse karna
- 401 aur 403 confuse karna
- old keys rotate na karna
- client-side browser code me server secret expose karna

---

# 🎤 Interview Point

**Q: Authentication vs authorization?**

Authentication verifies identity; authorization determines what that identity is permitted to do.

**Q: How would you secure AI API credentials in production?**

Prefer managed/short-lived identity where supported; otherwise use a centralized secret store, least privilege, rotation, restricted access, and never hard-code or log secrets.

---

# 🔁 Why Next Lesson?

Ab question hai: Python program ko key milegi kaise without code me likhe?

> **Lesson 06 — Environment Variables & Secret Management**
