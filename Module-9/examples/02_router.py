from typing import Literal

from specialists import aks_specialist, pipeline_specialist, terraform_specialist


AgentName = Literal["pipeline", "terraform", "aks"]


def route_incident(incident: str) -> AgentName:
    text = incident.lower()
    if "terraform" in text or "plan" in text or "apply" in text:
        return "terraform"
    if "aks" in text or "pod" in text or "cluster" in text:
        return "aks"
    return "pipeline"


def dispatch(agent: AgentName):
    if agent == "terraform":
        return terraform_specialist("production")
    if agent == "aks":
        return aks_specialist("prod-aks")
    return pipeline_specialist("production")


incident = "Terraform apply failed after a networking change."
selected = route_incident(incident)
result = dispatch(selected)

print("Incident:", incident)
print("Selected agent:", selected)
print("Result:", result)
print("\nLearning point: router performs bounded dispatch; it is not an ongoing supervisor.")
