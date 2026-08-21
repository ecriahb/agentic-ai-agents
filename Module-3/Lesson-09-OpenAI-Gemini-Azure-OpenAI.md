# 🚩 Jai Bajrangbali!

# Lesson 09 — OpenAI / Gemini / Azure OpenAI API Concepts

> **Provider change ho sakta hai, but application engineering fundamentals largely same rehte hain: endpoint, auth, payload, model/deployment, response and limits.**

---

## 🎯 Lesson Goal

Aap high-level level par samjhoge:

- OpenAI API concept
- Gemini API concept
- Azure OpenAI concept
- public provider vs Azure-hosted enterprise resource pattern
- model name vs deployment/resource configuration
- provider abstraction
- vendor-specific assumptions avoid karna

> **Note:** API syntax, model names and SDK methods change ho sakte hain. Live implementation ke waqt official documentation ko source of truth treat karo.

---

## 1. Common Provider-Agnostic Mental Model

```text
Application
    ↓
Provider SDK / HTTP Client
    ↓
Endpoint
    ↓
Authentication
    ↓
Model or Deployment Selection
    ↓
Input + Configuration
    ↓
Inference
    ↓
Response
```

Whether OpenAI, Gemini or Azure OpenAI — ye skeleton useful rahega.

---

# PART 1 — OpenAI API

OpenAI platform exposes APIs and official SDKs for model inference and related capabilities.

Current official examples use the OpenAI SDK and Responses API pattern such as:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="YOUR_MODEL",
    input="Explain AKS simply."
)

print(response.output_text)
```

Authentication pattern uses API keys, commonly loaded securely from environment variables and sent as bearer authentication by the client.

Mental model:

```text
Python
 ↓ OpenAI SDK
OpenAI API
 ↓
Hosted Model
 ↓
Response
```

---

# PART 2 — Gemini and Anthropic Provider Patterns

Google's Gemini API provides model generation capabilities through Google AI APIs/SDKs.

Conceptual flow:

```text
Python App
   ↓ Google SDK / HTTP API
Gemini API
   ↓
Gemini Model
   ↓
Generated Content
```

Provider-specific terms, payload fields and authentication patterns differ from OpenAI.

Anthropic's messages/tool-use pattern is another useful comparison point for agent applications. Its model-specific features, such as extended reasoning or prompt caching when available, can change latency and cost, but they must stay behind the same internal contract:

```text
incident input + evidence
    -> provider adapter
    -> structured proposal
    -> citation/schema/policy validation
    -> application outcome
```

Use an Anthropic adapter only as an optional parity exercise. Do not let provider-specific reasoning, caching, or tool syntax become the authorization layer. Measure whether a feature improves grounded incident analysis enough to justify its cost and operational dependency.

Important lesson:

> Similar capability does not mean identical SDK syntax.

So don't blindly convert:

```text
OpenAI parameter name
      ↓ copy-paste
Gemini request
```

Read provider docs and map your application's intent to that provider's contract.

---

# PART 3 — Azure OpenAI

Azure-hosted AI services add Azure resource concepts around model access.

Typical enterprise mental model:

```text
Azure Subscription
      ↓
AI Resource / Project / Endpoint
      ↓
Deployment / Model configuration
      ↓
Authentication / Azure Identity or supported credential
      ↓
Application Request
```

Why enterprises may choose Azure-hosted access:

```text
Azure governance alignment
Identity/RBAC integration
Network controls
Azure monitoring/operations integration
Enterprise resource management
```

Exact supported auth mechanisms and resource/deployment patterns should always be checked in current Microsoft documentation.

---

## 4. Model vs Deployment — Important Enterprise Concept

Generic public API may directly ask for a model identifier.

Azure-style environments can introduce a configured deployment/resource name between your application and the underlying model.

Mental model:

```text
Underlying Model
      ↓ deployed/configured as
Enterprise Deployment
      ↓ called by
Application
```

Therefore this mistake is common:

```text
Correct model family
but wrong deployment/resource identifier
        ↓
API call fails
```

---

## 5. Same Business Function, Different Adapter

Suppose business function is:

```python
def analyze_incident(evidence):
    ...
```

Bad architecture:

```text
Business logic everywhere mixed with provider-specific SDK calls
```

Better:

```text
Incident Analyzer
      ↓
LLM Client Interface
      ↓
OpenAI Adapter / Gemini Adapter / Azure Adapter
```

Conceptual Python:

```python
class LLMClient:
    def analyze(self, prompt: str) -> str:
        raise NotImplementedError
```

Then provider adapter implements it.

This becomes important later in enterprise systems and testing.

---

## 6. Provider Comparison Checklist

When selecting/integrating a provider, compare:

```text
Authentication
Endpoint model
Available models/capabilities
Data/privacy requirements
Region availability
Rate/quota limits
Pricing
Latency
Structured output support
Tool/function calling support
Observability
Enterprise network controls
SDK maturity
```

Do not choose only because one code example looks shorter.

### Azure OpenAI Operations Exercise

Azure OpenAI adds an operational layer around inference:

```text
Azure resource
    -> deployment name
    -> pinned API version
    -> region and quota
    -> identity or key authentication
    -> content filtering and network policy
    -> telemetry and cost ownership
```

Do not confuse a model family with an Azure deployment name. A deployment can be unavailable, quota-limited, moved to another region, or governed by a different content policy while application code still looks valid.

Create this provider record using synthetic values; credentials are not required for the exercise:

```yaml
provider: azure-openai
resource: ai-devops-lab
deployment: approved-chat-deployment
api_version: pinned-in-configuration
region: selected-after-capacity-check
data_classification: internal-synthetic-only
fallback: deny-unless-policy-compatible
```

Classify the response before retrying:

| Signal | Correct application behavior |
|---|---|
| 401/403 | fail authentication; do not retry blindly |
| 429/quota | bounded backoff, queue, or approved fallback |
| deployment not found | configuration alert; do not substitute an arbitrary model |
| content filter | return policy status and preserve audit metadata |
| regional outage | use an evaluated region/provider only when data policy permits |

Record deployment, API version, region, correlation ID, usage, latency, and policy result. Never put credentials in prompts or source control.

---

# 🛠️ DevOps Scenario

Company A:

```text
Local Ollama for developer experimentation
       ↓
OpenAI API for selected hosted workloads
```

Company B:

```text
Azure-native enterprise environment
       ↓
Azure identity/network/governance requirements
       ↓
Azure-hosted model endpoint
```

Architecture should keep core RCA logic independent where practical.

---

# ❌ Common Mistakes

- all providers use same endpoint format assume karna
- model name and Azure deployment identifier confuse karna
- provider SDK code ko business logic me tightly couple karna
- auth pattern copy-paste across providers
- current model/version names memory se assume karna
- quota/rate limits ignore karna
- data governance and region constraints ignore karna

---

# 🎤 Interview Point

**Q: How would you design an AI application that may switch providers?**

Separate provider-specific SDK/API code behind a small internal client interface. Keep prompt construction, evidence collection, validation and business logic provider-agnostic as much as possible.

---

# 🔁 Why Next Lesson?

Provider koi bhi ho, failures guaranteed hain: timeout, 401, 429, malformed response, server error.

> **Lesson 10 — Handling API Responses & Errors**
