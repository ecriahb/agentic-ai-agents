from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    incident: str
    status: str


def validate_incident(state: State) -> dict:
    incident = state["incident"].strip()
    if not incident:
        return {"status": "INVALID_INPUT"}
    return {"status": "VALIDATED"}


builder = StateGraph(State)
builder.add_node("validate_incident", validate_incident)
builder.add_edge(START, "validate_incident")
builder.add_edge("validate_incident", END)

graph = builder.compile()

result = graph.invoke(
    {
        "incident": "Production AKS deployment failed after Terraform change",
        "status": "NEW",
    }
)

print(result)
