"""DevOps Agent V3

Improvement over V2:
- Track exact tool+argument calls to avoid pointless duplicates in this static lab.
- Preserve evidence separately from the conversation.
- Add stronger grounding instructions for the final answer.
"""

from typing import Literal

from ollama import chat

Environment = Literal["production", "staging", "development"]
ClusterName = Literal["prod-aks", "stage-aks", "dev-aks"]


def get_pipeline_status(environment: Environment) -> str:
    return {
        "production": "Failed during Terraform Apply",
        "staging": "Succeeded",
        "development": "Succeeded",
    }.get(environment, "Environment not found")


def get_terraform_changes(environment: Environment) -> str:
    return {
        "production": "NSG rule allowing AKS subnet traffic was removed",
        "staging": "No risky Terraform changes found",
        "development": "No risky Terraform changes found",
    }.get(environment, "No Terraform information found")


def get_aks_status(cluster_name: ClusterName) -> str:
    return {
        "prod-aks": "Degraded - network connectivity failures detected",
        "stage-aks": "Healthy",
        "dev-aks": "Healthy",
    }.get(cluster_name, "Cluster not found")


tools = [get_pipeline_status, get_terraform_changes, get_aks_status]
available_functions = {tool.__name__: tool for tool in tools}

messages = [
    {
        "role": "system",
        "content": (
            "You are an evidence-grounded DevOps investigator. production is the environment; "
            "prod-aks is the cluster. Use tools. Do not claim customer downtime, data loss, "
            "or any impact not directly observed. Clearly label inference as inference."
        ),
    },
    {
        "role": "user",
        "content": (
            "Investigate the production deployment failure affecting prod-aks after Terraform changes. "
            "Collect pipeline, Terraform and AKS evidence and produce a concise RCA."
        ),
    },
]

executed_calls = set()
evidence = []

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
        call_key = (tool_name, tuple(sorted(arguments.items())))

        if call_key in executed_calls:
            result = "SKIPPED: exact tool call already executed in this static lab"
        else:
            function = available_functions.get(tool_name)
            if function is None:
                result = f"ERROR: Unknown tool {tool_name}"
            else:
                try:
                    result = function(**arguments)
                except Exception as exc:
                    result = f"ERROR: {exc}"

            executed_calls.add(call_key)
            evidence.append(
                {
                    "tool": tool_name,
                    "arguments": arguments,
                    "observation": result,
                }
            )

        print(f"{tool_name}({arguments}) -> {result}")
        messages.append(
            {
                "role": "tool",
                "tool_name": tool_name,
                "content": str(result),
            }
        )
else:
    print("Agent stopped because the maximum step limit was reached.")

print("\n--- EVIDENCE STORED OUTSIDE MODEL CONVERSATION ---")
for item in evidence:
    print(item)

print("\nExpected evidence-based conclusion:")
print(
    "The evidence strongly suggests that removal of the NSG rule allowing AKS subnet traffic "
    "contributed to AKS network connectivity degradation and the observed deployment failure."
)
