from mcp.server import MCPServer

mcp = MCPServer("Module7-DevOps-Investigation")

ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}
ALLOWED_CLUSTERS = {"dev-aks", "prod-aks"}


def validate_environment(environment: str) -> str:
    value = environment.strip().lower()
    if value not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"Unsupported environment: {environment}")
    return value


def validate_cluster(cluster_name: str) -> str:
    value = cluster_name.strip().lower()
    if value not in ALLOWED_CLUSTERS:
        raise ValueError(f"Unsupported cluster: {cluster_name}")
    return value


@mcp.tool()
def get_pipeline_status(environment: str) -> dict:
    """Return read-only deployment pipeline status for an allowlisted environment."""
    env = validate_environment(environment)
    if env == "production":
        return {
            "environment": env,
            "status": "failed",
            "stage": "terraform_apply",
            "fact": "Deployment failed during Terraform Apply",
            "source": "learning-pipeline-api",
            "read_only": True,
        }
    return {
        "environment": env,
        "status": "success",
        "stage": "deploy",
        "fact": "Deployment completed successfully",
        "source": "learning-pipeline-api",
        "read_only": True,
    }


@mcp.tool()
def get_terraform_changes(environment: str) -> dict:
    """Return read-only Terraform change evidence for an allowlisted environment."""
    env = validate_environment(environment)
    if env == "production":
        return {
            "environment": env,
            "change_type": "removed",
            "resource_type": "nsg_rule",
            "resource_name": "aks-subnet-allow",
            "fact": "NSG rule aks-subnet-allow was removed",
            "source": "learning-terraform-change-store",
            "read_only": True,
        }
    return {
        "environment": env,
        "change_type": "none",
        "fact": "No relevant Terraform networking change recorded",
        "source": "learning-terraform-change-store",
        "read_only": True,
    }


@mcp.tool()
def get_aks_status(cluster_name: str) -> dict:
    """Return read-only AKS health evidence for an allowlisted learning cluster."""
    cluster = validate_cluster(cluster_name)
    if cluster == "prod-aks":
        return {
            "cluster_name": cluster,
            "status": "degraded",
            "category": "network",
            "fact": "AKS network connectivity validation is degraded",
            "source": "learning-aks-api",
            "read_only": True,
        }
    return {
        "cluster_name": cluster,
        "status": "healthy",
        "category": "general",
        "fact": "AKS cluster health checks are healthy",
        "source": "learning-aks-api",
        "read_only": True,
    }


@mcp.resource("runbook://aks/networking")
def aks_networking_runbook() -> str:
    """Return reference-only AKS networking guidance."""
    return (
        "REFERENCE ONLY: AKS subnet connectivity depends on required NSG rules, "
        "routes, DNS and network dependencies. Validate active rules before redeployment."
    )


@mcp.resource("runbook://terraform/networking")
def terraform_networking_runbook() -> str:
    """Return reference-only Terraform networking review guidance."""
    return (
        "REFERENCE ONLY: Review Terraform plan/state for NSG, UDR, subnet and private "
        "endpoint changes. Compare desired and active network policy before apply/redeploy."
    )


@mcp.prompt()
def incident_rca(incident_id: str, environment: str) -> str:
    """Return an evidence-first DevOps incident analysis template."""
    env = validate_environment(environment)
    incident = incident_id.strip().upper()
    if not incident.startswith("INC-"):
        raise ValueError("incident_id must look like INC-1234")
    return f"""
Analyze incident {incident} in {env}.
Use CURRENT_EVIDENCE for current facts and REFERENCE only for guidance.
If evidence is missing, say UNKNOWN.
Do not claim remediation was executed.
Return Root Cause, Confirmed Impact, Evidence Gaps, Next Checks and Confidence.
""".strip()


if __name__ == "__main__":
    mcp.run()
