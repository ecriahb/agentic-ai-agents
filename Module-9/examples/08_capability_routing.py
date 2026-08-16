from specialists import aks_specialist, knowledge_specialist, terraform_specialist


AGENT_CAPABILITIES = {
    "terraform_specialist": {"terraform_read", "terraform_runbooks"},
    "aks_specialist": {"aks_read", "aks_runbooks"},
    "knowledge_specialist": {"reference_search"},
}


def check_capability(agent: str, capability: str) -> None:
    allowed = AGENT_CAPABILITIES.get(agent, set())
    if capability not in allowed:
        raise PermissionError(f"{agent} is not allowed to use {capability}")


check_capability("terraform_specialist", "terraform_read")
terraform_result = terraform_specialist("production")

check_capability("aks_specialist", "aks_read")
aks_result = aks_specialist("prod-aks")

check_capability("knowledge_specialist", "reference_search")
knowledge_result = knowledge_specialist("AKS networking after Terraform NSG change")

print("Terraform:", terraform_result["status"])
print("AKS:", aks_result["status"])
print("References:", [r["id"] for r in knowledge_result["references"]])

print("\nLearning point: agent capability access is scoped. MCP discovery or tool existence would still not equal authorization.")
