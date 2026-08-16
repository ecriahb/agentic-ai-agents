from devops_tools import get_aks_status, get_pipeline_status, get_terraform_changes


def collect_evidence(environment: str, cluster_name: str):
    evidence = []

    evidence.append({
        "id": "E1",
        "tool": "get_pipeline_status",
        "result": get_pipeline_status(environment),
    })
    evidence.append({
        "id": "E2",
        "tool": "get_terraform_changes",
        "result": get_terraform_changes(environment),
    })
    evidence.append({
        "id": "E3",
        "tool": "get_aks_status",
        "result": get_aks_status(cluster_name),
    })

    return evidence


if __name__ == "__main__":
    evidence_log = collect_evidence("production", "prod-aks")
    print("=== Preserved Read-Only Evidence ===")
    for item in evidence_log:
        print(f"[{item['id']}] {item['tool']}: {item['result']}")

    print("\nNo remediation action was executed.")
