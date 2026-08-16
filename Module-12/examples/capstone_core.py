from __future__ import annotations

import os
import re
from datetime import datetime, timezone
from typing import Any


ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}
ALLOWED_CLUSTERS = {"dev-aks", "stage-aks", "prod-aks"}
ALLOWED_READ_TOOLS = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}

RUNBOOKS = [
    {
        "id": "R1",
        "kind": "REFERENCE",
        "source": "aks-networking.md",
        "version": "v3",
        "text": (
            "AKS subnet connectivity depends on required network security, routing, DNS and platform traffic paths. "
            "After a network policy change, validate effective NSG rules and routes before retrying deployment."
        ),
    },
    {
        "id": "R2",
        "kind": "REFERENCE",
        "source": "terraform-networking.md",
        "version": "v2",
        "text": (
            "Terraform plans that remove or modify network security rules should be reviewed against the approved baseline. "
            "Correct source configuration and revalidate connectivity before redeployment."
        ),
    },
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def validate_target(environment: str, cluster_name: str) -> None:
    if environment not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"INVALID_ENVIRONMENT: {environment}")
    if cluster_name not in ALLOWED_CLUSTERS:
        raise ValueError(f"INVALID_CLUSTER: {cluster_name}")


def execute_read_only_tool(tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if tool_name not in ALLOWED_READ_TOOLS:
        raise PermissionError(f"POLICY_BLOCKED: {tool_name}")

    if tool_name == "get_pipeline_status":
        environment = arguments.get("environment")
        if environment not in ALLOWED_ENVIRONMENTS:
            raise ValueError("INVALID_ARGUMENT: environment")
        return {
            "status": "FAILED",
            "stage": "terraform_apply",
            "summary": "Deployment failed during Terraform Apply.",
        }

    if tool_name == "get_terraform_changes":
        environment = arguments.get("environment")
        if environment not in ALLOWED_ENVIRONMENTS:
            raise ValueError("INVALID_ARGUMENT: environment")
        return {
            "status": "CHANGE_FOUND",
            "resource": "aks-subnet-allow",
            "change": "removed",
            "summary": "NSG rule aks-subnet-allow was removed.",
        }

    if tool_name == "get_aks_status":
        cluster_name = arguments.get("cluster_name")
        if cluster_name not in ALLOWED_CLUSTERS:
            raise ValueError("INVALID_ARGUMENT: cluster_name")
        return {
            "status": "DEGRADED",
            "check": "network_connectivity",
            "summary": "AKS network connectivity validation is degraded.",
        }

    raise RuntimeError("UNREACHABLE")


def collect_evidence(evidence_id: str, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    try:
        payload = execute_read_only_tool(tool_name, arguments)
        return {
            "id": evidence_id,
            "kind": "CURRENT_EVIDENCE",
            "operation": tool_name,
            "arguments": arguments,
            "observed_at": now_iso(),
            "payload": payload,
        }
    except Exception as exc:
        return {
            "id": evidence_id,
            "kind": "TOOL_ERROR",
            "operation": tool_name,
            "arguments": arguments,
            "observed_at": now_iso(),
            "error": str(exc),
        }


def retrieve_references(query: str) -> list[dict[str, Any]]:
    # Deterministic learning retriever. Replace with Module 5/production retriever later.
    words = set(re.findall(r"[a-z0-9_-]+", query.lower()))
    scored = []
    for doc in RUNBOOKS:
        doc_words = set(re.findall(r"[a-z0-9_-]+", doc["text"].lower()))
        score = len(words.intersection(doc_words))
        scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [dict(doc) for score, doc in scored if score > 0][:2] or [dict(RUNBOOKS[0])]


def build_context(evidence: list[dict[str, Any]], references: list[dict[str, Any]]) -> str:
    lines = ["CURRENT EVIDENCE"]
    for item in evidence:
        lines.append(f"[{item['id']}] Kind: {item['kind']}")
        lines.append(f"Operation: {item['operation']}")
        if item.get("payload"):
            lines.append(f"Payload: {item['payload']}")
        if item.get("error"):
            lines.append(f"Error: {item['error']}")
        lines.append("")

    lines.append("REFERENCE KNOWLEDGE")
    for item in references:
        lines.append(f"[{item['id']}] Source: {item['source']} Version: {item['version']}")
        lines.append(item["text"])
        lines.append("")

    return "\n".join(lines)


def detect_gaps(evidence: list[dict[str, Any]]) -> list[str]:
    current_ids = {e["id"] for e in evidence if e["kind"] == "CURRENT_EVIDENCE"}
    required = {"E1", "E2", "E3"}
    return sorted(required - current_ids)


def detect_conflicts(evidence: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id: dict[str, set[str]] = {}
    for item in evidence:
        if item["kind"] != "CURRENT_EVIDENCE":
            continue
        summary = str(item.get("payload", {}).get("summary", ""))
        by_id.setdefault(item["id"], set()).add(summary)
    return [
        {"evidence_id": evidence_id, "claims": sorted(claims)}
        for evidence_id, claims in by_id.items()
        if len(claims) > 1
    ]


def validate_citations(answer: str, evidence: list[dict[str, Any]], references: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    allowed = {item["id"] for item in evidence + references}
    cited = set(re.findall(r"\[([ER]\d+)\]", answer))
    unknown = sorted(cited - allowed)
    return not unknown, unknown


def deterministic_confidence(evidence: list[dict[str, Any]], conflicts: list[dict[str, Any]]) -> str:
    current = {e["id"] for e in evidence if e["kind"] == "CURRENT_EVIDENCE"}
    if conflicts or not {"E1", "E2", "E3"}.issubset(current):
        return "LOW"
    # The baseline demonstrates a supported sequence but not packet-level causal verification.
    return "MEDIUM"


def evaluate_action_policy(action: dict[str, Any], approved: bool = False) -> tuple[bool, str]:
    if not action:
        return False, "NO_ACTION"
    if action.get("type") != "WRITE_PROPOSAL":
        return False, "INVALID_ACTION_TYPE"
    if action.get("environment") == "production" and not approved:
        return False, "APPROVAL_REQUIRED"
    if action.get("action") != "restore_nsg_rule":
        return False, "POLICY_DENIED"
    return True, "APPROVED_BUT_NOT_EXECUTED_DEMO"


def ollama_model_name() -> str:
    return os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
