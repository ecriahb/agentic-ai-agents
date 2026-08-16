# 🚩 Jai Bajrangbali!

# Lesson 08 — Tool Calling / Function Calling

> **LLM decides; Python executes.**

## Why This Topic Now?

Model concepts explain kar sakta hai, but live cluster status ya Terraform changes automatically nahi jaan sakta. Hume external functions chahiye jinko model request kare aur application execute kare.

```text
Structured Output
       ↓
Tool Calling
       ↓
Agent Loop
```

## 🇬🇧 English Definition

> **Tool calling is a capability that allows an LLM to select and request external functions or tools; the application executes the tool and returns the result to the model.**

## First Fake DevOps Tool

```python
def get_aks_status(cluster_name: str) -> str:
    clusters = {
        "prod-aks": "Degraded",
        "dev-aks": "Healthy",
        "stage-aks": "Healthy"
    }

    return clusters.get(cluster_name, "Cluster not found")
```

## Ask the Model to Use the Tool

```python
from ollama import chat

response = chat(
    model="qwen3:0.6b",
    messages=[{
        "role": "user",
        "content": "What is the current status of prod-aks?"
    }],
    tools=[get_aks_status]
)
```

Model ka response conceptually:

```text
tool_calls = [
    get_aks_status(
        cluster_name="prod-aks"
    )
]
```

## Key Insight

> **Model ne `get_aks_status()` execute nahi kiya.**

Usne structured request diya:

```text
Tool name: get_aks_status
Argument: cluster_name = prod-aks
```

Actual function Python application execute karegi.

## Execute the Tool

```python
tool_call = response.message.tool_calls[0]

result = get_aks_status(
    **tool_call.function.arguments
)
```

Agar arguments ye hain:

```python
{"cluster_name": "prod-aks"}
```

To `**` unko unpack karke ye call banata hai:

```python
get_aks_status(cluster_name="prod-aks")
```

## Return Observation to the Model

```python
messages.append({
    "role": "tool",
    "tool_name": tool_call.function.name,
    "content": str(result)
})
```

Phir model ko final answer generate karne ke liye updated messages bheje ja sakte hain.

## Full Mental Model

```text
User Goal
   ↓
LLM decides tool needed
   ↓
LLM requests tool + arguments
   ↓
Application validates request
   ↓
Python executes function
   ↓
Tool returns observation
   ↓
Observation sent to LLM
   ↓
LLM generates answer
```

## Important Security Rule

Tool calling ka matlab ye nahi ki model ko unrestricted production access de diya jaye.

Host application ko control karna chahiye:

- Allowed tools
- Argument validation
- Permissions
- Timeouts
- Audit logs
- Human approval for risky actions

## 🎯 Interview Corner

### Q. Does the LLM execute the function itself?

**Answer:**
> No. The LLM chooses or requests a tool and supplies arguments. The host application validates and executes the function, then returns the tool observation to the model.

## 🧠 Remember This

> **LLM decides. Application validates. Python executes. Tool returns evidence.**

## Why the Next Lesson Follows

Single tool call ek focused question answer karta hai. Real incident investigation me pipeline, Terraform aur AKS evidence multiple steps me collect karna padta hai.

➡️ **Next: Lesson 09 — From Tool Calling to a Basic DevOps Agent**
