from capstone_core import build_context, collect_evidence, retrieve_references

evidence = [
    collect_evidence("E1", "get_pipeline_status", {"environment": "production"}),
    collect_evidence("E2", "get_terraform_changes", {"environment": "production"}),
    collect_evidence("E3", "get_aks_status", {"cluster_name": "prod-aks"}),
]
references = retrieve_references("AKS Terraform networking failure")

context = build_context(evidence, references)
print(context)

assert "CURRENT EVIDENCE" in context
assert "REFERENCE KNOWLEDGE" in context
assert "[E2]" in context
assert "[R1]" in context
print("\nPASS: context preserves source classes and labels.")
