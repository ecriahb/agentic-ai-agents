from mcp.server import MCPServer

mcp = MCPServer("Module7-V7-HTTP")


@mcp.tool()
def get_aks_status(cluster_name: str) -> dict:
    """Return read-only learning AKS status."""
    allowed = {"dev-aks", "prod-aks"}
    cluster = cluster_name.strip().lower()
    if cluster not in allowed:
        raise ValueError("Unsupported cluster")

    return {
        "cluster_name": cluster,
        "status": "degraded" if cluster == "prod-aks" else "healthy",
        "source": "learning-aks-api",
        "read_only": True,
    }


if __name__ == "__main__":
    # Current MCP Python SDK v2 pattern for a deployable HTTP transport.
    # Endpoint defaults to http://127.0.0.1:8000/mcp
    mcp.run(
        transport="streamable-http",
        stateless_http=True,
        json_response=True,
    )
