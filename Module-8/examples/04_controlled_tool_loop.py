import operator
from typing import Annotated, Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from devops_tools import execute_read_only_tool


class State(TypedDict):
    environment: str
    cluster_name: str
    evidence: Annotated[list[dict], operator.add]
    next_tool: str
    iteration: int
    status: str


def planner(state: State) -> dict:
    ids = {item["id"] for item in state["evidence"]}

    if "E1" not in ids:
        return {"next_tool": "get_pipeline_status", "iteration": state["iteration"] + 1}
    if "E2" not in ids:
        return {"next_tool": "get_terraform_changes", "iteration": state["iteration"] + 1}
    if "E3" not in ids:
        return {"next_tool": "get_aks_status", "iteration": state["iteration"] + 1}

    return {"next_tool": "FINISH", "status": "EVIDENCE_READY"}


def route_plan(state: State) -> Literal["execute_tool", "finish"]:
    return "finish" if state["next_tool"] == "FINISH" else "execute_tool"


def execute_tool(state: State) -> dict:
    tool_name = state["next_tool"]

    if tool_name == "get_pipeline_status":
        arguments = {"environment": state["environment"]}
        evidence_id = "E1"
    elif tool_name == "get_terraform_changes":
        arguments = {"environment": state["environment"]}
        evidence_id = "E2"
    elif tool_name == "get_aks_status":
        arguments = {"cluster_name": state["cluster_name"]}
        evidence_id = "E3"
    else:
        raise ValueError(f"Unexpected tool: {tool_name}")

    payload = execute_read_only_tool(tool_name, arguments)
    return {
        "evidence": [
            {
                "id": evidence_id,
                "kind": "CURRENT_EVIDENCE",
                "operation": tool_name,
                "arguments": arguments,
                "payload": payload,
            }
        ]
    }


def finish(state: State) -> dict:
    return {"status": "SUCCESS"}


builder = StateGraph(State)
builder.add_node("planner", planner)
builder.add_node("execute_tool", execute_tool)
builder.add_node("finish", finish)
builder.add_edge(START, "planner")
builder.add_conditional_edges("planner", route_plan)
builder.add_edge("execute_tool", "planner")
builder.add_edge("finish", END)

graph = builder.compile()

result = graph.invoke(
    {
        "environment": "production",
        "cluster_name": "prod-aks",
        "evidence": [],
        "next_tool": "",
        "iteration": 0,
        "status": "NEW",
    }
)

print("Status:", result["status"])
for item in result["evidence"]:
    print(item["id"], item["payload"]["message"])
