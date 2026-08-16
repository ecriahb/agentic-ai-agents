# Module 1 — Lesson 3: OpenAI Cloud API Setup

> **Goal:** Hosted OpenAI API ko zero se configure karna, credential flow samajhna, first request ke prerequisites verify karna, aur cloud-provider errors ko code errors se alag identify karna.

---

# 1. English Definition

**A cloud AI API lets an application send authenticated programmatic requests to a hosted AI model and receive structured responses over the network.**

Simple Hinglish:

```text
Python App
   ↓ authenticated HTTPS request
OpenAI API
   ↓
Hosted Model
   ↓
Structured Response
```

Hum model train nahi kar rahe. Hum existing hosted model ko software ke through use kar rahe hain.

---

# 2. Why This Topic Comes Here

Lesson 1 me samjha:

```text
ChatGPT UI != API
```

Lesson 2 me ready kiya:

```text
Python + venv + pip + .env + secret hygiene
```

Ab natural next step:

```text
Development Environment
        ↓
Provider Authentication
        ↓
Hosted Model Access
```

First API call Lesson 5 me line-by-line decode karenge. Is lesson ka focus **setup and trust boundary** hai.

---

# 3. Hosted AI Mental Model

```text
Your Python Process
       │
       ├── reads OPENAI_API_KEY from environment
       │
       ↓
OpenAI SDK Client
       │
       ↓ HTTPS
OpenAI API Endpoint
       │
       ↓
Selected Hosted Model
       │
       ↓
Response Object
```

Important separation:

```text
SDK != API
API != Model
API Key != Model Password
Client != Model
```

## SDK
Python helper library jo HTTP/authentication/serialization/error handling ko simplify karta hai.

## API
Programmatic service interface.

## Model
Existing AI model jo input process karta hai.

## Client
Tumhare application ka SDK object jo API se communicate karta hai.

---

# 4. Install the SDK

Activate venv first, then:

```powershell
python -m pip install "openai>=2,<3" python-dotenv
```

Verify:

```powershell
python -c "import openai; print(openai.__version__)"
```

Why `python -m pip`?

```text
python interpreter
      ↓
its own pip
      ↓
correct venv dependency
```

This avoids the classic problem:

```text
pip installed package somewhere
but current python cannot import it
```

---

# 5. API Key Kya Hai?

**English Definition:**

**An API key is a secret credential used by an application to authenticate requests to an API service.**

Simple mental model:

```text
Application
   ↓ credential
Provider Authentication
   ↓
Request accepted or rejected
```

API key model ko smarter nahi banati. It only enables authenticated provider access according to account/project permissions and limits.

## Never do this

```python
client = OpenAI(api_key="sk-real-secret-here")
```

Problems:

- Git history me leak
- screenshot me leak
- logs me leak
- code sharing me leak
- accidental copy/paste

---

# 6. Correct Local Secret Pattern

Create `.env` in your local project:

```env
OPENAI_API_KEY=your-real-key-here
OPENAI_MODEL=your-available-model
```

`.gitignore` must contain:

```gitignore
.env
.venv/
__pycache__/
```

Load:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
```

Why no key argument?

The SDK can read `OPENAI_API_KEY` from the process environment.

Mental model:

```text
.env
 ↓ load_dotenv()
Process Environment
 ↓
OpenAI SDK
```

---

# 7. Safe Credential Verification

Do **not** print the secret.

Safe check:

```python
import os

if os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY loaded")
else:
    print("OPENAI_API_KEY missing")
```

PowerShell quick check after environment loading depends on your setup; the safest course pattern is the Python Boolean check above.

Never do:

```python
print(os.getenv("OPENAI_API_KEY"))
```

---

# 8. Model Configuration

Do not permanently bury a model name deep inside application code.

Better:

```python
import os

model = os.getenv("OPENAI_MODEL")
if not model:
    raise RuntimeError("OPENAI_MODEL is not configured")
```

Why configurable?

```text
model availability changes
account access differs
cost/capability differs
production may use different model than dev
```

Course principle:

> **Architecture should not depend on one forever-hard-coded model name.**

---

# 9. Minimal Setup Test

After Lesson 5 concepts are understood, a minimal request looks like:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

model = os.getenv("OPENAI_MODEL")
if not model:
    raise RuntimeError("OPENAI_MODEL missing")

client = OpenAI()

response = client.responses.create(
    model=model,
    input="Explain AKS in two simple lines.",
)

print(response.output_text)
```

Do not blindly memorize this. Lesson 5 explains every object and field.

---

# 10. Request Flow Step-by-Step

```text
1. Python starts
2. .env values load into process environment
3. OpenAI SDK client is created
4. Application selects configured model
5. Client sends authenticated HTTPS request
6. Provider authenticates credential/project
7. Model processes input
8. API returns structured response
9. SDK converts it into Python response object
10. Application extracts required fields
```

---

# 11. ChatGPT Product vs API

Do not assume:

```text
ChatGPT subscription
=
API entitlement/billing
```

Treat them as separate product contexts.

For API usage, success can depend on:

- valid API credentials
- project/account access
- billing or credits where applicable
- model availability
- organization/project policies
- rate limits

So:

```text
ChatGPT works in browser
```

does not prove:

```text
my Python API project can call every API model
```

---

# 12. Error Taxonomy

Beginner debugging ka golden rule:

> **Exact failing layer identify karo before changing code.**

## A. Missing credential
Symptoms may indicate no API key was provided.

Check:

```text
.env exists?
load_dotenv() called?
correct working directory?
correct variable name?
```

## B. Authentication failure
Credential exists but provider rejects it.

Possible reasons:

```text
invalid key
revoked key
wrong account/project context
copy/paste problem
```

## C. Model access/not found
Code syntax may be correct; configured model may not be available to the account/project.

Fix architecture:

```text
MODEL_NAME = configuration
not magic constant
```

## D. Quota/rate/billing limit
Not the same as invalid Python syntax.

Think:

```text
request identity accepted
but usage not currently permitted/available
```

## E. Network/proxy/TLS
Enterprise laptop may have:

- proxy
- outbound firewall
- TLS inspection
- DNS restriction

Provider failure can therefore be networking rather than code.

---

# 13. Error-Handling Pattern

Learning version:

```python
try:
    response = client.responses.create(
        model=model,
        input="Explain AKS in two simple lines.",
    )
    print(response.output_text)
except Exception as exc:
    print(type(exc).__name__)
    print(str(exc))
```

Production improvement:

```text
Known provider error classes
→ normalized application error
→ safe logging
→ retry only when appropriate
→ no secret leakage
```

Do not convert any provider exception into fake success.

Bad:

```python
except Exception:
    return "Everything is healthy"
```

That creates false evidence.

---

# 14. Secret Management: Local vs Production

## Local learning

```text
.env
```

is convenient.

## Production
Prefer your organization/platform's approved secret mechanism, for example:

```text
Secret Manager / Key Vault
Workload identity
Managed application credentials
CI/CD secret store
```

Core principle:

```text
Secret stays in host/application identity layer
Secret never becomes LLM context
```

Never put API keys in:

- prompt
- tool output
- RCA JSON
- model memory
- debug screenshot
- GitHub commit

---

# 15. DevOps Analogy

OpenAI API setup ko Azure DevOps thinking se relate karo:

```text
Python App             = Pipeline/Automation Client
API Key                = Credential
OpenAI SDK             = Azure SDK-like helper
OpenAI API             = Service API
Model                   = Hosted compute capability
Response                = API result
```

Same engineering habits apply:

```text
configuration
identity
network
error handling
logging
least exposure
```

---

# 16. OpenAI vs Ollama Preview

```text
OpenAI Hosted                 Ollama Local
-------------                 ------------
Remote provider               Local runtime
Internet/network path         localhost path
API credential                no auth required for local API
Cloud compute                 your hardware
Hosted usage limits/cost      local resource cost
Provider model access         installed local model
```

But common engineering contract stays:

```text
Input
→ Model
→ Response
→ Validation
```

---

# 17. Common Beginner Mistakes

1. `OpenAI()` ko model samajhna.
2. API key ko source code me paste karna.
3. `.env` Git me commit karna.
4. API key print karke debug karna.
5. ChatGPT subscription ko API balance/access samajhna.
6. Every error ko Python bug samajhna.
7. Model name permanently hard-code karna.
8. Network/proxy issue ko ignore karna.
9. Provider exception ko success me convert kar dena.
10. Secret ko prompt me bhejna.

---

# 18. Hands-On Practical

Before first request:

```powershell
python --version
python -m pip show openai
```

Create `.env`, then safe verification script run karo.

After Lesson 5 read karne ke baad:

```powershell
python examples/01_first_ai_call.py
```

Record:

```text
Was key loaded?
Which model configured?
Did authentication succeed?
Did model access succeed?
What exact response/error category appeared?
```

---

# 19. Failure Drill

Intentionally test in learning environment:

### Test 1 — Missing model configuration
Expected: host validation should fail before model request.

### Test 2 — Missing credential
Expected: authentication/setup error, not mysterious generic failure.

### Test 3 — Invalid model name
Expected: provider/model-access failure.

### Test 4 — Restore correct configuration
Expected: request reaches model and returns response.

Goal is not failure itself. Goal is **layer diagnosis**.

---

# 20. Production Checklist

```text
[ ] API key not in code
[ ] .env ignored by Git
[ ] model configurable
[ ] credential not logged
[ ] provider errors categorized
[ ] timeout/retry policy defined
[ ] request IDs logged where useful
[ ] usage/latency observable
[ ] production secret store used
[ ] model output treated as untrusted
```

---

# 21. Interview Q&A

### Q1. What is an API key?
A secret application credential used to authenticate API requests.

### Q2. What does `OpenAI()` create?
An SDK client object, not an AI model.

### Q3. Why use environment variables?
To keep secrets/configuration outside source code and make environments configurable.

### Q4. Is `.env` enough for enterprise production?
No. It is a local-development convenience; production should use approved secret-management and workload identity patterns.

### Q5. ChatGPT subscription and API billing/access same hai?
They should be treated as separate product/account contexts rather than assumed equivalent.

### Q6. Why keep model name configurable?
Availability, cost, capability and organization access can change.

### Q7. Why should provider errors be normalized?
So application logic can distinguish auth, rate, network, model and transient failures and react safely.

### Q8. Should secrets be sent to an LLM for convenience?
No. Credentials belong in the application/tool identity layer.

---

# 22. Revision Sheet

```text
Hosted API
= remote model capability through programmatic interface

SDK
= Python helper library

API Key
= application credential

Client
= API communication object

.env
= local secret/config convenience

Model
= existing hosted AI model

Provider Error
!= automatically a Python bug

Secret
= host-side concern, never model context
```

---

# 23. Homework

1. Draw the full `.env → environment → SDK client → API → model → response` flow.
2. Explain API key, SDK, API, model and client in one English line each.
3. Write a safe script that prints only whether `OPENAI_API_KEY` exists.
4. List five places where API keys must never appear.
5. Explain why model name should be configuration.
6. Create an error table with: missing key, invalid key, model unavailable, network failure, rate/quota issue.

---

# 24. Why Next Lesson?

Hosted provider setup clear ho gaya. Ab ek beginner-friendly question naturally aata hai:

```text
Kya main same AI application concepts
cloud billing par depend kiye bina practice kar sakta hoon?
```

Yes. Next:

➡️ **Lesson 4 — Zero-Cost Local AI with Ollama**