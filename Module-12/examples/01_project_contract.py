from typing import TypedDict


class IncidentState(TypedDict):
    incident_id: str
    incident: str
    environment: str
    cluster_name: str
    evidence: list[dict]
    references: list[dict]
    conflicts: list[dict]
    gaps: list[str]
    final_status: str


state: IncidentState = {
    "incident_id": "INC-1042",
    "incident": "Production AKS deployment failed after a Terraform networking change.",
    "environment": "production",
    "cluster_name": "prod-aks",
    "evidence": [],
    "references": [],
    "conflicts": [],
    "gaps": [],
    "final_status": "NEW",
}

required = {"incident_id", "incident", "environment", "cluster_name", "evidence", "references", "final_status"}
assert required.issubset(state)
print("Project state contract:", state)
print("PASS: explicit state exists before agent logic.")
