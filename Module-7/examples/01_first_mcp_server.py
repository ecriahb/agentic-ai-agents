from mcp.server import MCPServer

mcp = MCPServer("Module7-V1")


@mcp.tool()
def hello(name: str) -> dict:
    """Return a simple structured greeting."""
    clean = name.strip()
    if not clean:
        raise ValueError("name cannot be empty")
    return {"message": f"Hello, {clean}!", "source": "module7-v1"}


if __name__ == "__main__":
    mcp.run()
