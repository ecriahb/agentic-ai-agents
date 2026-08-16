from mcp.server import MCPServer

mcp = MCPServer("Module7-V3-Resources")

RUNBOOKS = {
    "aks-networking": (
        "Validate AKS subnet NSG rules, UDRs, DNS/private endpoint dependencies, "
        "and required connectivity before redeployment."
    ),
    "terraform-networking": (
        "Review Terraform plan/state for NSG, route, subnet and private endpoint "
        "changes before applying production networking changes."
    ),
}

INCIDENTS = {
    "INC-1042": (
        "Pipeline failed during Terraform Apply. "
        "NSG rule aks-subnet-allow was removed. "
        "AKS connectivity validation is degraded."
    )
}


@mcp.resource("runbook://aks/networking")
def aks_networking() -> str:
    """Return approved AKS networking reference guidance."""
    return RUNBOOKS["aks-networking"]


@mcp.resource("runbook://terraform/networking")
def terraform_networking() -> str:
    """Return approved Terraform networking reference guidance."""
    return RUNBOOKS["terraform-networking"]


@mcp.resource("incident://{incident_id}/evidence")
def incident_evidence(incident_id: str) -> str:
    """Return deterministic learning incident evidence by incident ID."""
    key = incident_id.strip().upper()
    if key not in INCIDENTS:
        raise ValueError("Unknown incident ID")
    return INCIDENTS[key]


if __name__ == "__main__":
    mcp.run()
