requirements = {
    "long_running_workers": True,
    "custom_kubernetes_policy": True,
    "many_services": True,
    "gpu_model_in_same_runtime": False,
    "simple_web_api_only": False,
}

score = {"AppService": 0, "ContainerApps": 0, "AKS": 0}

if requirements["simple_web_api_only"]:
    score["AppService"] += 3
if requirements["long_running_workers"]:
    score["ContainerApps"] += 2
    score["AKS"] += 2
if requirements["custom_kubernetes_policy"]:
    score["AKS"] += 4
if requirements["many_services"]:
    score["AKS"] += 2
    score["ContainerApps"] += 1

choice = max(score, key=score.get)
print("Scores:", score)
print("Suggested learning decision:", choice)
print("Reminder: validate against actual organizational requirements and platform standards.")
