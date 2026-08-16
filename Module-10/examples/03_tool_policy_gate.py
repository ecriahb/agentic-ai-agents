from security_core import tool_policy

cases = [
    ("get_aks_status", {"environment": "production"}, False),
    ("restart_deployment", {"environment": "production"}, False),
    ("restart_deployment", {"environment": "production"}, True),
    ("delete_cluster", {"environment": "production"}, True),
]

for tool, args, approved in cases:
    print(tool, args, "approved=", approved, "->", tool_policy(tool, args, approved))
