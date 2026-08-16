"""Deterministic read-only learning tools for Module 6.

Replace with authenticated real integrations only after adding RBAC, secret management,
timeouts, audit logging and approval boundaries.
"""

ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}
ALLOWED_CLUSTERS = {"dev-aks", "stage-aks", "prod-aks"}


def _validate_environment(environment: str) -> None:
    if environment not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f"Unsupported environment: {environment}")


def get_pipeline_status(environment: str) -> str:
    _validate_environment(environment)
    values = {
        "dev": "Succeeded",
        "stage": "Succeeded",
        "production": "Failed during Terraform Apply",
    }
    return values[environment]


def get_terraform_changes(environment: str) -> str:
    _validate_environment(environment)
    values = {
        "dev": "No risky networking change detected",
        "stage": "No risky networking change detected",
        "production": "NSG rule aks-subnet-allow was removed",
    }
    return values[environment]


def get_aks_status(cluster_name: str) -> str:
    if cluster_name not in ALLOWED_CLUSTERS:
        raise ValueError(f"Unsupported cluster: {cluster_name}")
    values = {
        "dev-aks": "Healthy",
        "stage-aks": "Healthy",
        "prod-aks": "Degraded - network connectivity validation failed",
    }
    return values[cluster_name]
