from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class State(TypedDict):
    proposed_action: dict
    approval_decision: str
    final_status: str


def propose_action(state: State) -> dict:
    return {
        "proposed_action": {
            "action": "restore_nsg_rule",
            "target": "aks-subnet-allow",
            "evidence_ids": ["E2", "E3"],
            "execution": "NOT_PERFORMED",
        }
    }


def approval_gate(state: State) -> dict:
    decision = interrupt(
        {
            "proposed_action": state["proposed_action"],
            "allowed_decisions": ["approve", "reject"],
        }
    )
    return {"approval_decision": str(decision).lower()}


def finish(state: State) -> dict:
    status = (
        "APPROVED_BUT_NOT_EXECUTED_DEMO"
        if state["approval_decision"] == "approve"
        else "HUMAN_REJECTED"
    )
    return {"final_status": status}


builder = StateGraph(State)
builder.add_node("propose_action", propose_action)
builder.add_node("approval_gate", approval_gate)
builder.add_node("finish", finish)
builder.add_edge(START, "propose_action")
builder.add_edge("propose_action", "approval_gate")
builder.add_edge("approval_gate", "finish")
builder.add_edge("finish", END)

graph = builder.compile(checkpointer=InMemorySaver())
config = {"configurable": {"thread_id": "module9-v9-approval"}}

initial_state: State = {
    "proposed_action": {},
    "approval_decision": "",
    "final_status": "NEW",
}

paused = graph.invoke(initial_state, config=config)
print("Paused for approval.")
print("Proposed action:", paused.get("proposed_action"))

# Safe learning path: reject. No real infrastructure write exists in this example.
resumed = graph.invoke(Command(resume="reject"), config=config)
print("Final status:", resumed["final_status"])
print("Learning point: approval is persisted workflow state, but approval is still not authorization.")
