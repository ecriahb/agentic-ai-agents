# 🚩 Jai Bajrangbali!

# Lesson 02 — LangChain Fundamentals

> **LangChain ko library of magic functions nahi, reusable AI application components ka ecosystem samjho.**

---

# 🎯 Lesson Goal

Is lesson ke baad aap:

- LangChain ka role explain kar paoge
- core component categories identify kar paoge
- direct SDK vs LangChain compare kar paoge
- abstraction boundary samajh paoge
- provider wrapper aur application logic ko separate dekh paoge
- common package/version confusion handle kar paoge

---

# PART 1 — English Definition

**LangChain** is a framework/ecosystem for composing language-model applications from reusable components such as model interfaces, prompts, retrievers, tools, parsers and runnables.

Simple mental model:

```text
LangChain = Standard Interfaces + Composition + Integrations + Execution Utilities
```

---

# PART 2 — Why It Exists

Without framework:

```python
load_docs()
split_docs()
embed_docs()
search_index()
build_prompt()
call_model()
parse_output()
validate_output()
```

All fine.

But if every project repeats same integration patterns, standard abstractions useful ho sakti hain.

LangChain roughly ye questions simplify karta hai:

```text
How do I represent a prompt?
How do I call a chat model?
How do I compose steps?
How do I expose retrieval as a standard interface?
How do I parse model output?
How do I attach callbacks/tracing?
```

---

# PART 3 — Core Component Map

A useful simplified map:

```text
                LANGCHAIN APPLICATION

Input
  ↓
PromptTemplate
  ↓
Chat Model
  ↓
Output Parser

Optional side components:

Document Loader
Text Splitter
Embedding Model
Vector Store
Retriever
Tools
State / History
Callbacks / Tracing
```

Every component ka ek input contract aur output contract hota hai.

---

# PART 4 — Model Wrapper

Direct SDK approach:

```python
client = SomeProviderClient(...)
response = client.generate(...)
```

Framework approach conceptually:

```python
llm = ChatModel(...)
response = llm.invoke(messages)
```

Benefit:

```text
application talks to a common model interface
```

But provider-specific capabilities fully identical nahi hoti. Common interface ka matlab feature parity nahi hota.

---

# PART 5 — Integration Packages Matter

Modern orchestration ecosystems frequently separate:

```text
core abstractions
provider integrations
community integrations
```

Conceptual example:

```text
langchain-core          → shared interfaces
provider package        → model-specific integration
community package       → external integrations
```

Exact package names/version APIs change ho sakte hain. Isliye learning principle:

> API syntax ratne se zyada important component contract samajhna hai.

---

# PART 6 — What Is a Component Contract?

Suppose PromptTemplate expects:

```text
{"incident": "AKS deployment failed"}
```

It produces:

```text
formatted prompt/messages
```

Model consumes messages and produces:

```text
AI message
```

Parser consumes AI message and produces:

```text
string / JSON / typed object
```

Chain tab reliable hoti hai jab adjacent contracts compatible hon.

Mental model:

```text
A Output == B Expected Input
```

Exactly CI/CD pipeline artifact contract jaisa.

---

# PART 7 — First Conceptual LangChain Call

Typical pattern:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:3b", temperature=0)

response = llm.invoke("Explain AKS in two lines")
print(response.content)
```

Line-by-line:

### `ChatOllama(...)`
Local Ollama model ko LangChain chat-model interface ke through wrap karta hai.

### `invoke(...)`
One input ko one execution me run karta hai.

### `response.content`
Model-generated text content.

Important:

```text
LangChain → Ollama ko replace nahi kar raha
LangChain → Ollama ko common interface ke through call kar raha
```

---

# PART 8 — Direct API vs Framework

| Area | Direct SDK/API | LangChain-style abstraction |
|---|---|---|
| Transparency | High | Abstraction layer present |
| Boilerplate | More custom | Often less |
| Provider control | Maximum | Depends on integration |
| Composition | Manual | Built-in patterns |
| Tracing hooks | Custom | Framework support possible |
| Dependencies | Lower | Higher |
| Learning curve | API-specific | Framework + provider |

Neither is universally better.

---

# PART 9 — DevOps Analogy

Think Terraform provider abstraction:

```text
Terraform language
      ↓
Provider
      ↓
Azure API
```

Similarly:

```text
LangChain Model Interface
      ↓
Provider Integration
      ↓
OpenAI / Ollama / Azure / Gemini API
```

Terraform abstraction useful hai, but provider-specific behavior still matter karta hai.

Same principle here.

---

# PART 10 — Messages Mental Model

Chat models frequently operate on roles/messages:

```text
System
Human
AI
Tool
```

Framework may represent these as message objects.

Conceptually:

```python
messages = [
    SystemMessage(content="You are a DevOps assistant."),
    HumanMessage(content="Analyze this incident.")
]
```

Why useful?

Role separation explicit rehta hai.

---

# PART 11 — Invoke, Batch, Stream Concepts

Common execution patterns:

### Invoke

```text
1 input → 1 run
```

### Batch

```text
many inputs → many runs
```

### Stream

```text
output tokens/chunks progressively
```

Production design me batch throughput aur streaming UX alag concerns hain.

---

# PART 12 — Common Mistakes

### Mistake 1 — Old tutorial blindly copy karna
Framework APIs evolve kar sakte hain. Version mismatch error aa sakta hai.

### Mistake 2 — Provider wrapper ko provider itself samajhna
Wrapper underlying service ka client abstraction hai.

### Mistake 3 — Framework messages ko evidence samajhna
Messages data containers hain. Factual trust evidence source se aata hai.

### Mistake 4 — Common interface means identical behavior
Different providers may support different structured output/tool capabilities.

---

# PART 13 — Production Questions

Before choosing abstraction ask:

```text
Which provider?
Which model capability?
Do I need streaming?
Do I need structured output?
Do I need tool calling?
How will I trace calls?
How will I pin versions?
What is fallback plan?
```

Package versions lock karna important:

```text
requirements.txt / lock file
```

because orchestration dependencies can change.

---

# PART 14 — Interview Q&A

### Q1. What is LangChain?
A framework ecosystem that provides standard interfaces and composable components for building LLM applications such as prompts, models, retrievers, tools and parsers.

### Q2. Is LangChain an LLM?
No. It calls underlying models/providers.

### Q3. Why use provider integrations?
They adapt provider-specific APIs into framework interfaces while exposing supported capabilities.

### Q4. What is the risk of abstraction?
It can hide provider details, add dependencies and make debugging harder if engineers do not understand underlying requests and contracts.

---

# PART 15 — Revision Sheet

```text
LangChain != Model
LangChain != Agent
LangChain != Vector DB

LangChain connects/wraps:
Models
Prompts
Parsers
Retrievers
Tools
Execution steps
```

---

# PART 16 — Homework

Draw this manually:

```text
Human Input
 ↓
Prompt Component
 ↓
Ollama Model Wrapper
 ↓
Output
```

Then write what underlying technology is responsible for:

1. orchestration
2. inference
3. model hosting
4. application validation

---

# 🔁 Next Lesson Kyu?

Ab components ka map clear hai. Next lesson me teen sabse basic building blocks ko hands-on connect karenge:

```text
PromptTemplate → Model → Output Parser
```

Ye har later chain ka foundation hoga.
