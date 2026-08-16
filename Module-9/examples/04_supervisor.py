from specialists import aks_specialist, pipeline_specialist, terraform_specialist


def supervisor(state: dict) -> dict:
    completed = set(state["completed_agents"])

    if "pipeline_specialist" not in completed:
        return {"next_agent": "pipeline_specialist"}
    if "terraform_specialist" not in completed:
        return {"next_agent": "terraform_specialist"}
    if "aks_specialist" not in completed:
        return {"next_agent": "aks_specialist"}
    return {"next_agent": "FINISH"}


def invoke_agent(name: str) -> dict:
    if name == "pipeline_specialist":
        return pipeline_specialist("production")
    if name == "terraform_specialist":
        return terraform_specialist("production")
    if name == "aks_specialist":
        return aks_specialist("prod-aks")
    raise ValueError(f"Unknown agent: {name}")


state = {"completed_agents": [], "results": [], "iterations": 0}
MAX_ITERATIONS = 5

while state["iterations"] < MAX_ITERATIONS:
    state["iterations"] += 1
    decision = supervisor(state)
    next_agent = decision["next_agent"]

    if next_agent == "FINISH":
        break

    result = invoke_agent(next_agent)
    state["results"].append(result)
    state["completed_agents"].append(next_agent)

print("=== Supervisor State ===")
print(state)
print("\nLearning point: supervisor coordinates multiple specialist invocations across steps; max iterations bound the loop.")
