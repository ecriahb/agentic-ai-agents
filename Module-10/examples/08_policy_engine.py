from dataclasses import dataclass

from security_core import tool_policy


@dataclass
class Request:
    user_role: str
    tool: str
    environment: str
    approved: bool = False


AUTHORIZED_ROLES = {
    "reader": {"get_pipeline_status", "get_terraform_changes", "get_aks_status"},
    "operator": {"get_pipeline_status", "get_terraform_changes", "get_aks_status", "restart_deployment"},
}


def evaluate(req: Request) -> str:
    allowed_for_role = AUTHORIZED_ROLES.get(req.user_role, set())
    if req.tool not in allowed_for_role:
        return "AUTHORIZATION_DENIED"

    return tool_policy(
        req.tool,
        {"environment": req.environment},
        approved=req.approved,
    )


cases = [
    Request("reader", "get_aks_status", "production"),
    Request("reader", "restart_deployment", "production"),
    Request("operator", "restart_deployment", "production", False),
    Request("operator", "restart_deployment", "production", True),
]

for case in cases:
    print(case, "->", evaluate(case))
