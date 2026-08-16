# 🚩 Jai Bajrangbali!

# Lesson 10 — Handling API Responses & Errors

> **Production AI app ka quality sirf successful response se decide nahi hota; failure ko kitna safely handle karta hai usse bhi hota hai.**

---

## 🎯 Lesson Goal

Aap samjhoge:

- successful vs failed response
- `raise_for_status()`
- timeout handling
- connection failures
- retryable vs non-retryable errors
- 429 rate limits
- exponential backoff + jitter concept
- malformed/non-JSON response
- logging without leaking secrets
- graceful failure

---

## 1. Happy Path Is Not Enough

Bad application design:

```text
Call API
 ↓
Assume success
 ↓
Parse output
```

Production design:

```text
Call API
 ↓
Timeout?
Connection error?
HTTP error?
Rate limited?
Malformed response?
Schema invalid?
 ↓
Controlled handling
```

---

## 2. HTTP Status Check

Python `requests` example:

```python
response = requests.get(url, timeout=10)
response.raise_for_status()
```

`raise_for_status()` 4xx/5xx response ko exception me convert karta hai, jisse accidental success-path processing avoid hoti hai.

---

## 3. Timeout Handling

```python
import requests

try:
    response = requests.get(url, timeout=10)
except requests.Timeout:
    print("API request timed out")
```

Timeout should not mean:

```text
Wait forever
```

It means application has a defined patience boundary.

---

## 4. Connection Errors

```python
try:
    response = requests.get(url, timeout=10)
except requests.ConnectionError:
    print("Could not connect to API")
```

Possible causes:

```text
DNS
network path
proxy
firewall
server down
wrong host/port
TLS issue
```

Don't label every connection error as "API key problem".

---

## 5. Retryable vs Non-Retryable

Usually pointless to retry unchanged request immediately for:

```text
400 malformed request
401 invalid credential
403 insufficient permission
404 wrong resource
```

Potentially transient cases may include:

```text
429 rate limit
500 internal error
502 bad gateway
503 unavailable
network timeout
```

But retry policy depends on provider and operation semantics.

---

## 6. Exponential Backoff

Concept:

```text
Attempt 1 fails
wait ~1 sec
Attempt 2 fails
wait ~2 sec
Attempt 3 fails
wait ~4 sec
```

Jitter adds a small randomized delay so many clients don't retry at the exact same moment.

Conceptual code:

```python
import random
import time

for attempt in range(3):
    try:
        result = call_api()
        break
    except TransientError:
        delay = (2 ** attempt) + random.random()
        time.sleep(delay)
```

Production libraries/providers may already offer retry behavior; avoid accidentally stacking multiple retry layers without understanding them.

---

## 7. Rate Limit — 429

429 means application is sending more requests/tokens than currently allowed by a limit/quota policy.

Bad:

```text
429 → infinite rapid retry loop
```

Better:

```text
429
 ↓
respect provider guidance / retry-after when available
 ↓
backoff
 ↓
limit retries
 ↓
log metric
 ↓
fail gracefully if exhausted
```

---

## 8. Parse Safely

```python
try:
    data = response.json()
except ValueError:
    raise RuntimeError("API returned non-JSON response")
```

Then validate required fields rather than blindly doing:

```python
print(data["result"]["nested"]["field"])
```

---

## 9. Error Object for Application

Instead of dumping raw exception to user:

```python
error_result = {
    "status": "failed",
    "category": "rate_limit",
    "retryable": True,
    "message": "AI provider rate limit reached"
}
```

This enables UI/pipeline/agent logic to make deterministic decisions.

---

## 10. Logging

Useful log:

```text
request_id
provider
operation
status_code
latency
retry_count
error_category
```

Avoid logging:

```text
full API key
access token
sensitive prompt payload
credentials inside logs
```

---

# 🧪 Practical Error Handler

```python
import requests


def fetch_json(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.Timeout as exc:
        raise RuntimeError("Request timed out") from exc

    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response else None
        raise RuntimeError(f"HTTP request failed: {status}") from exc

    except requests.ConnectionError as exc:
        raise RuntimeError("Connection failed") from exc

    except ValueError as exc:
        raise RuntimeError("Response was not valid JSON") from exc
```

---

# 🛠️ DevOps Example

Incident bot pipeline:

```text
Pipeline failure
 ↓
AI API call
 ↓
429
 ↓
controlled retry
 ↓
still 429
 ↓
return "analysis unavailable: provider rate limited"
 ↓
DO NOT invent RCA
```

This is crucial:

> **AI unavailable should not become fake AI analysis.**

---

# ❌ Common Mistakes

- every error retry karna
- infinite retries
- no timeout
- exception suppress karke empty response treat as valid
- secret/prompt dump in logs
- 429 ko auth error bolna
- provider outage me hallucinated fallback RCA generate karna

---

# 🎤 Interview Point

**Q: What is your API retry strategy?**

Classify failures first. Do not retry deterministic client errors such as invalid credentials or malformed payloads. For transient failures, use bounded retries with exponential backoff and jitter, respect provider guidance, and ensure the operation is safe to retry.

---

# 🔁 Why Next Lesson?

API success bhi ho gaya, but free-form text application ke liye unreliable ho sakta hai. Next:

> **Lesson 11 — Structured AI Responses**
