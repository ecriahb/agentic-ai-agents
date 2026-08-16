import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    evidence: Annotated[list[dict], operator.add]


def pipeline_evidence(state: State) -> dict:
    return {
        "evidence": [
            {"id": "E1", "source": "pipeline", "fact": "Deployment failed during Terraform Apply."}
        ]
    }


def terraform_evidence(state: State) -> dict:
    return {
        "evidence": [
            {"id": "E2", "source": "terraform", "fact": "NSG rule aks-subnet-allow was removed."}
        ]
    }


builder = StateGraph(State)
builder.add_node("pipeline_evidence", pipeline_evidence)
builder.add_node("terraform_evidence", terraform_evidence)
builder.add_edge(START, "pipeline_evidence")
builder.add_edge("pipeline_evidence", "terraform_evidence")
builder.add_edge("terraform_evidence", END)

graph = builder.compile()

result = graph.invoke({"evidence": []})
print(result["evidence"])
