"""A tiny StateGraph whose model node can use Ollama or OpenAI.

State/routing remain host-controlled regardless of provider.
"""

from pathlib import Path
import sys
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm


class State(TypedDict):
    incident: str
    evidence: str
    answer: str
    status: str


def validate(state: State) -> dict:
    if not state["incident"].strip() or not state["evidence"].strip():
        return {"status": "INSUFFICIENT_INPUT"}
    return {"status": "READY"}


def analyze(state: State) -> dict:
    if state["status"] != "READY":
        return {"answer": "RCA not generated because required input is missing."}

    result = ask_llm(
        f"Incident:\n{state['incident']}\n\nCurrent Evidence:\n{state['evidence']}",
        system=(
            "You are a grounded read-only DevOps analyst. "
            "Use only supplied current evidence. Return Root Cause, Evidence Gaps, Next Checks."
        ),
    )
    return {"answer": result.text, "status": f"GENERATED_BY_{result.provider.upper()}"}


builder = StateGraph(State)
builder.add_node("validate", validate)
builder.add_node("analyze", analyze)
builder.add_edge(START, "validate")
builder.add_edge("validate", "analyze")
builder.add_edge("analyze", END)
graph = builder.compile()

result = graph.invoke(
    {
        "incident": "Production AKS deployment failed after a Terraform networking change.",
        "evidence": (
            "[E1] Terraform Apply failed.\n"
            "[E2] NSG rule aks-subnet-allow was removed.\n"
            "[E3] AKS subnet connectivity validation failed."
        ),
        "answer": "",
        "status": "NEW",
    }
)

print("Status:", result["status"])
print(result["answer"])
print("\nStateGraph remains the control plane; model provider is only one node dependency.")
