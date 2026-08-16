from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    failure_stage: str
    route: str
    result: str


def classify(state: State) -> dict:
    stage = state["failure_stage"].lower()
    if "terraform" in stage:
        return {"route": "terraform"}
    if "aks" in stage:
        return {"route": "aks"}
    return {"route": "pipeline"}


def route(state: State) -> Literal["terraform_node", "aks_node", "pipeline_node"]:
    return {
        "terraform": "terraform_node",
        "aks": "aks_node",
        "pipeline": "pipeline_node",
    }[state["route"]]


def terraform_node(state: State) -> dict:
    return {"result": "Inspect Terraform changes first."}


def aks_node(state: State) -> dict:
    return {"result": "Inspect AKS status first."}


def pipeline_node(state: State) -> dict:
    return {"result": "Inspect pipeline evidence first."}


builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("terraform_node", terraform_node)
builder.add_node("aks_node", aks_node)
builder.add_node("pipeline_node", pipeline_node)
builder.add_edge(START, "classify")
builder.add_conditional_edges("classify", route)
builder.add_edge("terraform_node", END)
builder.add_edge("aks_node", END)
builder.add_edge("pipeline_node", END)

graph = builder.compile()

print(graph.invoke({"failure_stage": "Terraform Apply", "route": "", "result": ""}))
