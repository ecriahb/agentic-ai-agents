from concurrent.futures import ThreadPoolExecutor

from specialists import aks_specialist, pipeline_specialist, terraform_specialist


def run_pipeline():
    return pipeline_specialist("production")


def run_terraform():
    return terraform_specialist("production")


def run_aks():
    return aks_specialist("prod-aks")


jobs = [run_pipeline, run_terraform, run_aks]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(lambda fn: fn(), jobs))

print("=== Parallel Specialist Results ===")
for result in results:
    print(result["agent"], result["status"], result["observations"])

print("\nLearning point: independent read-only investigations can run in parallel, then fan-in into a merge stage.")
