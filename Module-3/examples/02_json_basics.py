import json

incident = {
    "environment": "production",
    "pipeline": "deploy-api",
    "failed": True,
    "errors": [
        "Terraform apply failed",
        "AKS connectivity validation failed",
    ],
}

json_text = json.dumps(incident, indent=2)
print(json_text)

parsed = json.loads(json_text)
print("\nEnvironment:", parsed["environment"])
print("First error:", parsed["errors"][0])
