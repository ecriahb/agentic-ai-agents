"""DevOps Agent V2

Improvement over V1:
- Constrain environment arguments with Literal.
- Give the model explicit mapping: production environment + prod-aks cluster.
- Preserve and display real tool observations before final RCA.
"""

from typing import Literal

from ollama import chat

Environment = Literal["production", "staging", "development"]
ClusterName = Literal["prod-aks", "stage-aks", "dev-aks"]


def get_aks_status(cluster_name: ClusterName) -> str:
    data = {
        "prod-aks": "Degraded - network connectivity failures detected",
        "stage-aks": "Healthy",
        "dev-aks": "Healthy",
    }
    return data.get(cluster_name, "Cluster not found")


def get_pipeline_status(environment: Environment) -> str:
    data = {
        "production": "Failed during Terraform Apply",
        "staging": "Succeeded",
        "development": "Succeeded",
    }
    return data.get(environment, "Environment not found")


def get_terraform_changes(environment: Environment) -> str:
    data = {
        "production": "NSG rule allowing AKS subnet traffic was removed",
        "staging": "No risky Terraform changes found",
        "development": "No risky Terraform changes found",
    }
    return data.get(environment, "No Terraform information found")


tools = [get_pipeline_status, get_terraform_changes, get_aks_status]
available_functions = {tool.__name__: tool for tool in tools}

messages = [
    {
        "role": "system",
        "content": (
            "You are a DevOps investigation assistant. production is the environment and "
            "prod-aks is the AKS cluster. Use tools before concluding. Base the RCA only "
            "on tool observations and clearly separate evidence from inference."
        ),
    },
    {
        "role": "user",
        "content": (
            "Investigate the failed production deployment affecting prod-aks after Terraform changes. "
            "Check pipeline status, Terraform changes and AKS health, then provide root cause, impact and fix."
        ),
    },
]

observations = []

for step in range(1, 8):
    print(f"\n--- Agent Step {step} ---")

    response = chat(model="qwen3:0.6b", messages=messages, tools=tools)
    messages.append(response.message)

    if not response.message.tool_calls:
        print("\nFINAL RCA")
        print(response.message.content)
        break

    for tool_call in response.message.tool_calls:
        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments
        function = available_functions.get(tool_name)

        if function is None:
            result = f"ERROR: Unknown tool {tool_name}"
        else:
            try:
                result = function(**arguments)
            except Exception as exc:
                result = f"ERROR: {exc}"

        observation = f"{tool_name}({arguments}) -> {result}"
        observations.append(observation)
        print(observation)

        messages.append(
            {
                "role": "tool",
                "tool_name": tool_name,
                "content": str(result),
            }
        )
else:
    print("Agent stopped because the maximum step limit was reached.")

print("\n--- PRESERVED EVIDENCE ---")
for item in observations:
    print("-", item)
