from specialists import pipeline_specialist, terraform_specialist


pipeline_private_state = {
    "raw_log_lines": ["... many internal lines ..."],
    "query_attempts": 3,
}

pipeline_result = pipeline_specialist("production")

handoff = {
    "from_agent": "pipeline_specialist",
    "to_agent": "terraform_specialist",
    "reason": "Pipeline failed during Terraform Apply",
    "evidence_ids": ["E1"],
    "verified_context": {
        "environment": "production",
        "incident_id": "INC-1042",
    },
}

# Notice: pipeline_private_state is NOT sent to Terraform.
terraform_result = terraform_specialist(handoff["verified_context"]["environment"])

print("=== Handoff ===")
print(handoff)
print("\n=== Terraform Result ===")
print(terraform_result)
print("\nPrivate pipeline state stayed local:", pipeline_private_state)
print("\nLearning point: handoffs transfer minimum verified context, not the sender's full scratch state.")
