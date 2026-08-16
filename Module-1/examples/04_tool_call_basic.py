"""Module 1 Lab 04: Basic tool calling with a simulated AKS status tool."""

from ollama import chat


def get_aks_status(cluster_name: str) -> str:
    clusters = {
        "prod-aks": "Degraded",
        "dev-aks": "Healthy",
        "stage-aks": "Healthy",
    }
    return clusters.get(cluster_name, "Cluster not found")


messages = [
    {
        "role": "user",
        "content": "What is the current status of prod-aks? Use the available tool.",
    }
]

response = chat(
    model="qwen3:0.6b",
    messages=messages,
    tools=[get_aks_status],
)

messages.append(response.message)

if not response.message.tool_calls:
    print("Model did not request a tool.")
else:
    tool_call = response.message.tool_calls[0]
    arguments = tool_call.function.arguments

    print("Tool requested:", tool_call.function.name)
    print("Arguments:", arguments)

    result = get_aks_status(**arguments)
    print("Tool result:", result)

    messages.append(
        {
            "role": "tool",
            "tool_name": tool_call.function.name,
            "content": str(result),
        }
    )

    final_response = chat(
        model="qwen3:0.6b",
        messages=messages,
        tools=[get_aks_status],
    )

    print("Final answer:", final_response.message.content)
