from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from devops_tools import get_aks_status, get_pipeline_status, get_terraform_changes


class SpecialistState(TypedDict):
    environment: str
    cluster_name: str
    result: dict


def pipeline_specialist(state: SpecialistState) -> dict:
    return {"result": get_pipeline_status(state["environment"])}


def terraform_specialist(state: SpecialistState) -> dict:
    return {"result": get_terraform_changes(state["environment"])}


def aks_specialist(state: SpecialistState) -> dict:
    return {"result": get_aks_status(state["cluster_name"])}


def compile_single_node_graph(name: str, node):
    builder = StateGraph(SpecialistState)
    builder.add_node(name, node)
    builder.add_edge(START, name)
    builder.add_edge(name, END)
    return builder.compile()


pipeline_graph = compile_single_node_graph("pipeline", pipeline_specialist)
terraform_graph = compile_single_node_graph("terraform", terraform_specialist)
aks_graph = compile_single_node_graph("aks", aks_specialist)


class SupervisorState(TypedDict):
    domain: str
    environment: str
    cluster_name: str
    specialist_result: dict
    status: str


def route_domain(state: SupervisorState) -> Literal["pipeline", "terraform", "aks"]:
    if state["domain"] not in {"pipeline", "terraform", "aks"}:
        return "pipeline"
    return state["domain"]  # type: ignore[return-value]


def run_pipeline(state: SupervisorState) -> dict:
    result = pipeline_graph.invoke(
        {"environment": state["environment"], "cluster_name": state["cluster_name"], "result": {}}
    )
    return {"specialist_result": result["result"], "status": "SPECIALIST_COMPLETE"}


def run_terraform(state: SupervisorState) -> dict:
    result = terraform_graph.invoke(
        {"environment": state["environment"], "cluster_name": state["cluster_name"], "result": {}}
    )
    return {"specialist_result": result["result"], "status": "SPECIALIST_COMPLETE"}


def run_aks(state: SupervisorState) -> dict:
    result = aks_graph.invoke(
        {"environment": state["environment"], "cluster_name": state["cluster_name"], "result": {}}
    )
    return {"specialist_result": result["result"], "status": "SPECIALIST_COMPLETE"}


builder = StateGraph(SupervisorState)
builder.add_node("supervisor", lambda state: {})
builder.add_node("pipeline", run_pipeline)
builder.add_node("terraform", run_terraform)
builder.add_node("aks", run_aks)
builder.add_edge(START, "supervisor")
builder.add_conditional_edges("supervisor", route_domain)
builder.add_edge("pipeline", END)
builder.add_edge("terraform", END)
builder.add_edge("aks", END)

graph = builder.compile()

result = graph.invoke(
    {
        "domain": "terraform",
        "environment": "production",
        "cluster_name": "prod-aks",
        "specialist_result": {},
        "status": "NEW",
    }
)
print(result)
