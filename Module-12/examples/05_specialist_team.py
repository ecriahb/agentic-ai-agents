from concurrent.futures import ThreadPoolExecutor

from capstone_core import collect_evidence


def pipeline_specialist() -> dict:
    return {"agent": "pipeline_specialist", "evidence": [collect_evidence("E1", "get_pipeline_status", {"environment": "production"})]}


def terraform_specialist() -> dict:
    return {"agent": "terraform_specialist", "evidence": [collect_evidence("E2", "get_terraform_changes", {"environment": "production"})]}


def aks_specialist() -> dict:
    return {"agent": "aks_specialist", "evidence": [collect_evidence("E3", "get_aks_status", {"cluster_name": "prod-aks"})]}


specialists = [pipeline_specialist, terraform_specialist, aks_specialist]
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [future.result() for future in [pool.submit(fn) for fn in specialists]]

for result in results:
    print(result["agent"], "=>", [e["id"] for e in result["evidence"]])

print("PASS: independent read-only specialists can fan out in parallel.")
