conversation_context = {
    "last_user_message": "Production AKS deployment failed"
}

workflow_state = {
    "incident_id": "INC-1042",
    "environment": "production",
    "cluster": "prod-aks",
    "iteration": 1,
}

evidence_log = [
    {
        "id": "E1",
        "source": "pipeline",
        "fact": "Deployment failed during Terraform Apply",
    }
]

permissions = {
    "read_pipeline": True,
    "read_aks": True,
    "execute_remediation": False,
}

print("Conversation Context:", conversation_context)
print("Workflow State:", workflow_state)
print("Evidence Log:", evidence_log)
print("Permissions:", permissions)

print("\nKey rule: conversation memory is not evidence and permissions are not decided by the LLM.")
