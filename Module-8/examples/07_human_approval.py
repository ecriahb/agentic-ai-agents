from typing import Literal, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class State(TypedDict):
    incident_id: str
    proposed_action: str
    approval_decision: str
    status: str


def propose_action(state: State) -> dict:
    return {
        "proposed_action": "Restore NSG rule aks-subnet-allow (simulation only)",
        "status": "AWAITING_APPROVAL",
    }


def approval_gate(state: State) -> dict:
    decision = interrupt(
        {
            "incident_id": state["incident_id"],
            "action": state["proposed_action"],
            "allowed_decisions": ["approve", "reject"],
        }
    )
    return {"approval_decision": str(decision).lower()}


def route_decision(state: State) -> Literal["approved", "rejected"]:
    return "approved" if state["approval_decision"] == "approve" else "rejected"


def approved(state: State) -> dict:
    return {"status": "APPROVED_SIMULATION_ONLY"}


def rejected(state: State) -> dict:
    return {"status": "HUMAN_REJECTED"}


builder = StateGraph(State)
builder.add_node("propose_action", propose_action)
builder.add_node("approval_gate", approval_gate)
builder.add_node("approved", approved)
builder.add_node("rejected", rejected)
builder.add_edge(START, "propose_action")
builder.add_edge("propose_action", "approval_gate")
builder.add_conditional_edges("approval_gate", route_decision)
builder.add_edge("approved", END)
builder.add_edge("rejected", END)

graph = builder.compile(checkpointer=InMemorySaver())
config = {"configurable": {"thread_id": "INC-1042-approval-demo"}}

first = graph.invoke(
    {
        "incident_id": "INC-1042",
        "proposed_action": "",
        "approval_decision": "",
        "status": "NEW",
    },
    config=config,
)
print("Paused result:", first)

# Simulate an authorized human approving. No real infrastructure write happens.
resumed = graph.invoke(Command(resume="approve"), config=config)
print("Resumed result:", resumed)
