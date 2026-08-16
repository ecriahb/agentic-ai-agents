from security_core import mcp_policy

cases = [
    ("corp-devops-mcp", "get_aks_status"),
    ("unknown-server", "get_aks_status"),
    ("corp-devops-mcp", "delete_cluster"),
]

for server, tool in cases:
    print(f"server={server} tool={tool} -> {mcp_policy(server, tool)}")

print("\nDiscovery does not imply approval. Server and tool must both satisfy host policy.")
