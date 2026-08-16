import operator
from typing import Annotated, Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from devops_tools import execute_read_only_tool


class State(TypedDict):
    environment: str
    evidence: Annotated[list[dict], operator.add]
    iteration: int
    max_iterations: int
    last_tool: str
    no_progress_count: int
    status: str


def choose_next(state: State) -> dict:
    ids = {item["id"] for item in state["evidence"]}

    if state["iteration"] >= state["max_iterations"]:
        return {"status": "MAX_ITERATIONS_REACHED"}

    if "E1" not in ids:
        return {"last_tool": "get_pipeline_status", "iteration": state["iteration"] + 1}
    if "E2" not in ids:
        return {"last_tool": "get_terraform_changes", "iteration": state["iteration"] + 1}

    return {"status": "SUCCESS"}


def route(state: State) -> Literal["execute", "finish"]:
    return "finish" if state["status"] in {"SUCCESS", "MAX_ITERATIONS_REACHED", "NO_PROGRESS"} else "execute"


def execute(state: State) -> dict:
    tool_name = state["last_tool"]
    arguments = {"environment": state["environment"]}
    evidence_id = "E1" if tool_name == "get_pipeline_status" else "E2"

    existing = {item["id"] for item in state["evidence"]}
    if evidence_id in existing:
        count = state["no_progress_count"] + 1
        if count >= 2:
            return {"no_progress_count": count, "status": "NO_PROGRESS"}
        return {"no_progress_count": count}

    payload = execute_read_only_tool(tool_name, arguments)
    return {
        "evidence": [{"id": evidence_id, "operation": tool_name, "payload": payload}],
        "no_progress_count": 0,
    }


def finish(state: State) -> dict:
    return {}


builder = StateGraph(State)
builder.add_node("choose_next", choose_next)
builder.add_node("execute", execute)
builder.add_node("finish", finish)
builder.add_edge(START, "choose_next")
builder.add_conditional_edges("choose_next", route)
builder.add_edge("execute", "choose_next")
builder.add_edge("finish", END)

graph = builder.compile()

result = graph.invoke(
    {
        "environment": "production",
        "evidence": [],
        "iteration": 0,
        "max_iterations": 4,
        "last_tool": "",
        "no_progress_count": 0,
        "status": "RUNNING",
    }
)

print("Final status:", result["status"])
print("Iterations:", result["iteration"])
print("Evidence IDs:", [item["id"] for item in result["evidence"]])
