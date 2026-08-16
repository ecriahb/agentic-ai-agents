from capstone_core import collect_evidence, validate_target

validate_target("production", "prod-aks")

evidence = [
    collect_evidence("E1", "get_pipeline_status", {"environment": "production"}),
    collect_evidence("E2", "get_terraform_changes", {"environment": "production"}),
    collect_evidence("E3", "get_aks_status", {"cluster_name": "prod-aks"}),
]

print("=== Current Evidence ===")
for item in evidence:
    print(item)

assert all(item["kind"] == "CURRENT_EVIDENCE" for item in evidence)
print("PASS: all baseline observations were collected through read-only tool contracts.")
