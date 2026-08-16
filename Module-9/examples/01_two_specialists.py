from specialists import pipeline_specialist, terraform_specialist


incident = "Production deployment failed during Terraform Apply."

pipeline_result = pipeline_specialist("production")
terraform_result = terraform_specialist("production")

print("=== Incident ===")
print(incident)

print("\n=== Pipeline Specialist ===")
print(pipeline_result)

print("\n=== Terraform Specialist ===")
print(terraform_result)

print("\nLearning point: specialists have separate responsibilities and structured outputs.")
