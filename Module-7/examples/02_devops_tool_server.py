from mcp.server import MCPServer

mcp = MCPServer("Module7-V2-DevOps-Tool")

ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}


def validate_environment(environment: str) -> str:
    value = environment.strip().lower()
    if value not in ALLOWED_ENVIRONMENTS:
        raise ValueError(
            f"Unsupported environment '{environment}'. "
            f"Allowed: {sorted(ALLOWED_ENVIRONMENTS)}"
        )
    return value


@mcp.tool()
def get_pipeline_status(environment: str) -> dict:
    """Return read-only deterministic pipeline status for an allowlisted environment."""
    env = validate_environment(environment)
    statuses = {
        "dev": {"status": "success", "stage": "deploy"},
        "stage": {"status": "success", "stage": "validation"},
        "production": {"status": "failed", "stage": "terraform_apply"},
    }
    return {
        "environment": env,
        **statuses[env],
        "source": "learning-pipeline-data",
        "read_only": True,
    }


if __name__ == "__main__":
    mcp.run()
