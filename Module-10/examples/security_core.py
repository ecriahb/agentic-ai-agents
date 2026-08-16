from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

APPROVED_TOOLS = {
    "get_pipeline_status": "READ",
    "get_terraform_changes": "READ",
    "get_aks_status": "READ",
    "restart_deployment": "WRITE",
}
ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}
APPROVED_MCP_SERVERS = {"corp-devops-mcp"}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|password|secret)\s*[:=]\s*[^\s,;]+"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)authorization:\s*bearer\s+[^\s]+"),
]

INJECTION_SIGNALS = [
    "ignore previous",
    "ignore all previous",
    "reveal system prompt",
    "bypass approval",
    "disable safety",
    "execute without approval",
]


@dataclass
class Trace:
    events: list[dict[str, Any]] = field(default_factory=list)

    def add(self, event_type: str, **data: Any) -> None:
        self.events.append({"type": event_type, **data})


def detect_injection(text: str) -> list[str]:
    lowered = text.lower()
    return [signal for signal in INJECTION_SIGNALS if signal in lowered]


def redact_secrets(text: str) -> tuple[str, int]:
    redacted = text
    hits = 0
    for pattern in SECRET_PATTERNS:
        redacted, count = pattern.subn("[REDACTED_SECRET]", redacted)
        hits += count
    return redacted, hits


def tool_policy(tool: str, arguments: dict[str, Any], approved: bool = False) -> str:
    risk = APPROVED_TOOLS.get(tool)
    if risk is None:
        return "BLOCKED_UNKNOWN_TOOL"

    environment = arguments.get("environment")
    if environment is not None and environment not in ALLOWED_ENVIRONMENTS:
        return "BLOCKED_SCOPE"

    if risk == "WRITE" and environment == "production" and not approved:
        return "APPROVAL_REQUIRED"

    return "ALLOWED"


def mcp_policy(server: str, tool: str) -> str:
    if server not in APPROVED_MCP_SERVERS:
        return "BLOCKED_UNKNOWN_SERVER"
    if tool not in APPROVED_TOOLS:
        return "BLOCKED_UNKNOWN_TOOL"
    return "ALLOWED"


def validate_citations(text: str, allowed_ids: set[str]) -> tuple[bool, list[str]]:
    cited = set(re.findall(r"\[([ER]\d+)\]", text))
    unknown = sorted(cited - allowed_ids)
    return not unknown, unknown
