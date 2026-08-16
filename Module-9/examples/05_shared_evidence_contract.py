from specialists import (
    aks_specialist,
    flatten_evidence,
    pipeline_specialist,
    terraform_specialist,
)


results = [
    pipeline_specialist("production"),
    terraform_specialist("production"),
    aks_specialist("prod-aks"),
]

evidence = flatten_evidence(results)

shared_state = {
    "incident_id": "INC-1042",
    "agent_results": results,
    "evidence": evidence,
}

print("=== Shared Evidence State ===")
for item in shared_state["evidence"]:
    print(item["id"], item["agent"], item["claim"])

print("\nLearning point: agents communicate through normalized evidence contracts, not copied internal reasoning.")
