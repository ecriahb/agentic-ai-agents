import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph


RUNBOOKS = {
    "aks-networking.md": (
        "AKS subnet connectivity depends on approved NSG rules, route configuration "
        "and required platform traffic paths."
    ),
    "terraform-networking.md": (
        "Terraform network changes should be reviewed for deleted or modified NSG "
        "rules before deployment proceeds."
    ),
}


class State(TypedDict):
    current_evidence: Annotated[list[dict], operator.add]
    references: Annotated[list[dict], operator.add]
    query: str
    status: str


def add_current_evidence(state: State) -> dict:
    return {
        "current_evidence": [
            {
                "id": "E2",
                "kind": "CURRENT_EVIDENCE",
                "fact": "NSG rule aks-subnet-allow was removed.",
            }
        ]
    }


def retrieve_reference(state: State) -> dict:
    query = state["query"].lower()
    selected = []

    for source, text in RUNBOOKS.items():
        if "aks" in query or "network" in query or "terraform" in query:
            selected.append(
                {
                    "id": f"R{len(selected) + 1}",
                    "kind": "REFERENCE",
                    "source": source,
                    "text": text,
                }
            )

    return {"references": selected}


def summarize_sources(state: State) -> dict:
    print("CURRENT EVIDENCE")
    for item in state["current_evidence"]:
        print(item["id"], item["fact"])

    print("\nREFERENCE KNOWLEDGE")
    for item in state["references"]:
        print(item["id"], item["source"], "->", item["text"])

    return {"status": "READY_FOR_GROUNDED_ANALYSIS"}


builder = StateGraph(State)
builder.add_node("add_current_evidence", add_current_evidence)
builder.add_node("retrieve_reference", retrieve_reference)
builder.add_node("summarize_sources", summarize_sources)
builder.add_edge(START, "add_current_evidence")
builder.add_edge("add_current_evidence", "retrieve_reference")
builder.add_edge("retrieve_reference", "summarize_sources")
builder.add_edge("summarize_sources", END)

graph = builder.compile()

print(
    graph.invoke(
        {
            "current_evidence": [],
            "references": [],
            "query": "AKS networking issue after Terraform change",
            "status": "NEW",
        }
    )["status"]
)
