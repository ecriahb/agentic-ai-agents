from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    incident_id: str
    step: str
    evidence_count: int


def collect_pipeline(state: State) -> dict:
    return {"step": "pipeline_collected", "evidence_count": state["evidence_count"] + 1}


def collect_terraform(state: State) -> dict:
    return {"step": "terraform_collected", "evidence_count": state["evidence_count"] + 1}


builder = StateGraph(State)
builder.add_node("collect_pipeline", collect_pipeline)
builder.add_node("collect_terraform", collect_terraform)
builder.add_edge(START, "collect_pipeline")
builder.add_edge("collect_pipeline", "collect_terraform")
builder.add_edge("collect_terraform", END)

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)
config = {"configurable": {"thread_id": "INC-1042-checkpoint-demo"}}

result = graph.invoke(
    {"incident_id": "INC-1042", "step": "new", "evidence_count": 0},
    config=config,
)
print("Final result:", result)

snapshot = graph.get_state(config)
print("Saved state values:", snapshot.values)
print("Next nodes:", snapshot.next)
