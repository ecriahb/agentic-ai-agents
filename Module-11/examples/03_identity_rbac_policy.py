POLICY = {
    "agent-worker-mi": {"get_pipeline_status", "get_terraform_changes", "get_aks_status"},
    "write-executor-mi": {"restore_approved_nsg_rule"},
}


def authorize(identity: str, operation: str, approved: bool = False) -> tuple[bool, str]:
    if operation not in POLICY.get(identity, set()):
        return False, "RBAC_DENIED"
    if operation.startswith("restore_") and not approved:
        return False, "APPROVAL_REQUIRED"
    return True, "ALLOW"


cases = [
    ("agent-worker-mi", "get_aks_status", False),
    ("agent-worker-mi", "restore_approved_nsg_rule", True),
    ("write-executor-mi", "restore_approved_nsg_rule", False),
    ("write-executor-mi", "restore_approved_nsg_rule", True),
]

for case in cases:
    print(case, "=>", authorize(*case))
