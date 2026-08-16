"""DevOps Agent V1

Goal: Learn the basic multi-tool agent loop.
This version intentionally keeps tool arguments loosely typed so we can observe
how a model may select the right tool but still pass the wrong identifier.
"""

from ollama import chat


def get_aks_status(cluster_name: str) -> str:
    data = {
        "prod-aks": "Degraded - network connectivity failures detected",
        "dev-aks": "Healthy",
    }
    return data.get(cluster_name, "Cluster not found")


def get_pipeline_status(environment: str) -> str:
    data = {
        "production": "Failed during Terraform Apply",
        "staging": "Succeeded",
        "development": "Succeeded",
    }
    return data.get(environment, "Environment not found")


def get_terraform_changes(environment: str) -> str:
    data = {
        "production": "NSG rule allowing AKS subnet traffic was removed",
        "staging": "No risky Terraform changes found",
        "development": "No risky Terraform changes found",
    }
    return data.get(environment, "No Terraform information found")


tools = [get_aks_status, get_pipeline_status, get_terraform_changes]
available_functions = {
    "get_aks_status": get_aks_status,
    "get_pipeline_status": get_pipeline_status,
    "get_terraform_changes": get_terraform_changes,
}

messages = [
    {
        "role": "system",
        "content": (
            "You are a DevOps investigation assistant. Use available tools to investigate. "
            "Do not invent tool results."
        ),
    },
    {
        "role": "user",
        "content": (
            "Investigate why deployment to prod-aks failed after Terraform changes. "
            "Check pipeline, Terraform and AKS status and provide an RCA."
        ),
    },
]

for step in range(1, 8):
    print(f"\n--- Agent Step {step} ---")

    response = chat(
        model="qwen3:0.6b",
        messages=messages,
        tools=tools,
    )
    messages.append(response.message)

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print("Tool:", tool_name)
            print("Arguments:", arguments)

            tool_function = available_functions.get(tool_name)
            if tool_function is None:
                result = f"ERROR: Unknown tool {tool_name}"
            else:
                try:
                    result = tool_function(**arguments)
                except Exception as exc:
                    result = f"ERROR: {exc}"

            print("Observation:", result)
            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": str(result),
                }
            )
    else:
        print("\nFINAL ANSWER")
        print(response.message.content)
        break
else:
    print("Agent stopped because the maximum step limit was reached.")
