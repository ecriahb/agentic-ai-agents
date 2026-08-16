from typing import Literal
from pydantic import BaseModel, ValidationError


class IncidentRCA(BaseModel):
    root_cause: str
    impact: str
    recommended_fix: list[str]
    severity: Literal["low", "medium", "high", "critical"]
    confidence: Literal["low", "medium", "high"]


sample = {
    "root_cause": "The aks-subnet-allow NSG rule was removed.",
    "impact": "AKS subnet connectivity validation failed and deployment failed during Terraform Apply.",
    "recommended_fix": [
        "Review the Terraform change that removed the rule.",
        "Restore or correct the required AKS subnet rule after validation.",
        "Validate connectivity before redeployment.",
    ],
    "severity": "high",
    "confidence": "medium",
}

try:
    rca = IncidentRCA.model_validate(sample)
    print(rca.model_dump_json(indent=2))
except ValidationError as exc:
    print("Validation failed:")
    print(exc)
