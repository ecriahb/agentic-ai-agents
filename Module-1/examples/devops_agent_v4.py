"""DevOps Agent V4

Improvement over V3:
- Separate investigation from reporting.
- Preserve original tool evidence in application state.
- Generate a schema-validated RCA only from preserved evidence.
- Keep risky remediation as a recommendation, not an automatic action.
"""

import json
from typing import Literal

from ollama import chat
from pydantic import BaseModel, Field

Environment = Literal["production", "staging", "development"]
ClusterName = Literal["prod-aks", "stage-aks", "dev-aks"]
Severity = Literal["low", "medium", "high", "critical"]


class RCAResponse(BaseModel):
    root_cause: str = Field(min_length=10)
    impact: str = Field(min_length=5)
    fix: str = Field(min_length=10)
    severity: Severity
    evidence: list[str] = Field(min_length=1)


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

# ------------------------------
# PHASE 1: INVESTIGATION AGENT
# ------------------------------
messages = [
    {
        "role": "system",
        "content": (
            "You are a read-only DevOps investigator. production is the environment and prod-aks "
            "is the cluster. Use the available tools to collect pipeline, Terraform and AKS evidence. "
            "Do not invent observations and do not perform remediation."
        ),
    },
    {
        "role": "user",
        "content": (
            "Investigate why the production deployment affecting prod-aks failed after Terraform changes."
        ),
    },
]

executed_calls = set()
evidence_state = []

for step in range(1, 8):
    print(f"\n--- Investigation Step {step} ---")
    response = chat(model="qwen3:0.6b", messages=messages, tools=tools)
    messages.append(response.message)

    if not response.message.tool_calls:
        print("Investigation agent summary:", response.message.content)
        break

    for tool_call in response.message.tool_calls:
        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments
        call_key = (tool_name, tuple(sorted(arguments.items())))

        if call_key in executed_calls:
            result = "SKIPPED: exact tool call already executed"
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
            evidence_state.append(
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
    print("Investigation stopped at the maximum step limit.")

if not evidence_state:
    raise RuntimeError("No evidence was collected; refusing to generate an RCA.")

print("\n--- PRESERVED APPLICATION EVIDENCE ---")
for item in evidence_state:
    print(item)

# ------------------------------
# PHASE 2: STRUCTURED RCA REPORT
# ------------------------------
rca_messages = [
    {
        "role": "system",
        "content": (
            "You are an RCA report generator. Use ONLY the supplied tool evidence. "
            "Do not invent customer downtime, data loss, revenue impact, or any unobserved fact. "
            "The fix must be a recommendation requiring engineer validation/approval."
        ),
    },
    {
        "role": "user",
        "content": "Generate the RCA from this evidence:\n" + json.dumps(evidence_state, indent=2),
    },
]

rca_response = chat(
    model="gemma3:1b",
    messages=rca_messages,
    format=RCAResponse.model_json_schema(),
)

rca = RCAResponse.model_validate_json(rca_response.message.content)

print("\n=== STRUCTURED RCA ===")
print("Root Cause:", rca.root_cause)
print("Impact:", rca.impact)
print("Fix:", rca.fix)
print("Severity:", rca.severity)
print("Evidence:")
for item in rca.evidence:
    print("-", item)

print("\nHuman approval required before any production-changing remediation.")
