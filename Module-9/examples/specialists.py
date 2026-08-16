from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}
ALLOWED_CLUSTERS = {"dev-aks", "prod-aks"}


@dataclass
class Observation:
    evidence_id: str
    claim: str
    source: str
    payload: dict[str, Any]


@dataclass
class SpecialistResult:
    agent: str
    status: str
    observations: list[dict[str, Any]]
    hypotheses: list[dict[str, Any]]
    gaps: list[str]
    recommended_next_agents: list[str]


def _validate_environment(environment: str) -> None:
    if environment not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"Environment not allowed: {environment}")


def pipeline_specialist(environment: str) -> dict[str, Any]:
    _validate_environment(environment)
    observation = Observation(
        evidence_id="E1",
        claim="Deployment failed during Terraform Apply.",
        source="pipeline_status",
        payload={
            "environment": environment,
            "status": "FAILED",
            "failed_stage": "terraform_apply",
        },
    )
    return asdict(
        SpecialistResult(
            agent="pipeline_specialist",
            status="SUCCESS",
            observations=[asdict(observation)],
            hypotheses=[],
            gaps=[],
            recommended_next_agents=["terraform_specialist"],
        )
    )


def terraform_specialist(environment: str) -> dict[str, Any]:
    _validate_environment(environment)
    observation = Observation(
        evidence_id="E2",
        claim="NSG rule aks-subnet-allow was removed in the Terraform networking change.",
        source="terraform_change_record",
        payload={
            "environment": environment,
            "change": "delete",
            "resource": "aks-subnet-allow",
            "resource_type": "nsg_rule",
        },
    )
    return asdict(
        SpecialistResult(
            agent="terraform_specialist",
            status="SUCCESS",
            observations=[asdict(observation)],
            hypotheses=[
                {
                    "text": "The NSG rule removal may explain the AKS connectivity degradation.",
                    "supporting_evidence_ids": ["E2"],
                }
            ],
            gaps=["Current AKS connectivity evidence is still required."],
            recommended_next_agents=["aks_specialist"],
        )
    )


def aks_specialist(cluster_name: str) -> dict[str, Any]:
    if cluster_name not in ALLOWED_CLUSTERS:
        raise ValueError(f"Cluster not allowed: {cluster_name}")
    observation = Observation(
        evidence_id="E3",
        claim="AKS network connectivity validation is degraded.",
        source="aks_health_check",
        payload={
            "cluster": cluster_name,
            "status": "DEGRADED",
            "network_validation": "FAILED",
        },
    )
    return asdict(
        SpecialistResult(
            agent="aks_specialist",
            status="SUCCESS",
            observations=[asdict(observation)],
            hypotheses=[
                {
                    "text": "Networking policy should be investigated before redeployment.",
                    "supporting_evidence_ids": ["E3"],
                }
            ],
            gaps=[],
            recommended_next_agents=["knowledge_specialist"],
        )
    )


def knowledge_specialist(query: str) -> dict[str, Any]:
    # Learning version: deterministic local references.
    references = [
        {
            "id": "R1",
            "kind": "REFERENCE",
            "source": "aks-networking-runbook",
            "text": (
                "AKS subnet connectivity depends on required NSG rules and routes. "
                "After network policy changes, validate effective network configuration."
            ),
        },
        {
            "id": "R2",
            "kind": "REFERENCE",
            "source": "terraform-networking-runbook",
            "text": (
                "Terraform changes that remove subnet security rules should be reviewed carefully, "
                "and post-change connectivity should be validated before redeployment."
            ),
        },
    ]
    return {
        "agent": "knowledge_specialist",
        "status": "SUCCESS",
        "query": query,
        "references": references,
    }


def flatten_evidence(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    evidence: list[dict[str, Any]] = []
    seen: set[str] = set()

    for result in results:
        for observation in result.get("observations", []):
            evidence_id = observation["evidence_id"]
            if evidence_id in seen:
                continue
            seen.add(evidence_id)
            evidence.append(
                {
                    "id": evidence_id,
                    "kind": "CURRENT_EVIDENCE",
                    "agent": result["agent"],
                    "claim": observation["claim"],
                    "source": observation["source"],
                    "payload": observation["payload"],
                }
            )

    return evidence
