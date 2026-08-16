from datetime import datetime, timezone

ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}
ALLOWED_CLUSTERS = {"dev-aks", "prod-aks"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_pipeline_status(environment: str) -> dict:
    if environment not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"Environment not allowed: {environment}")

    if environment == "production":
        return {
            "source": "pipeline-api",
            "observed_at": _now(),
            "environment": environment,
            "status": "failed",
            "stage": "terraform_apply",
            "message": "Deployment failed during Terraform Apply.",
        }

    return {
        "source": "pipeline-api",
        "observed_at": _now(),
        "environment": environment,
        "status": "success",
        "stage": "completed",
        "message": "Deployment completed successfully.",
    }


def get_terraform_changes(environment: str) -> dict:
    if environment not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"Environment not allowed: {environment}")

    if environment == "production":
        return {
            "source": "terraform-plan",
            "observed_at": _now(),
            "environment": environment,
            "network_changes": [
                {
                    "action": "delete",
                    "resource_type": "azurerm_network_security_rule",
                    "name": "aks-subnet-allow",
                }
            ],
            "message": "NSG rule aks-subnet-allow was removed.",
        }

    return {
        "source": "terraform-plan",
        "observed_at": _now(),
        "environment": environment,
        "network_changes": [],
        "message": "No relevant network changes detected.",
    }


def get_aks_status(cluster_name: str) -> dict:
    if cluster_name not in ALLOWED_CLUSTERS:
        raise ValueError(f"Cluster not allowed: {cluster_name}")

    if cluster_name == "prod-aks":
        return {
            "source": "aks-status-api",
            "observed_at": _now(),
            "cluster_name": cluster_name,
            "status": "degraded",
            "network_connectivity": "failed_validation",
            "message": "AKS network connectivity validation is degraded.",
        }

    return {
        "source": "aks-status-api",
        "observed_at": _now(),
        "cluster_name": cluster_name,
        "status": "healthy",
        "network_connectivity": "healthy",
        "message": "AKS cluster is healthy.",
    }


TOOL_REGISTRY = {
    "get_pipeline_status": get_pipeline_status,
    "get_terraform_changes": get_terraform_changes,
    "get_aks_status": get_aks_status,
}


def execute_read_only_tool(tool_name: str, arguments: dict) -> dict:
    if tool_name not in TOOL_REGISTRY:
        raise ValueError(f"Tool not allowlisted: {tool_name}")

    return TOOL_REGISTRY[tool_name](**arguments)
