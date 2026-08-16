from capstone_core import retrieve_references

query = "AKS deployment failed after Terraform NSG networking change"
references = retrieve_references(query)

print("=== Reference Knowledge ===")
for item in references:
    print(f"[{item['id']}] {item['source']} {item['version']}")
    print(item["text"])
    print()

assert all(item["kind"] == "REFERENCE" for item in references)
print("PASS: reference knowledge remains explicitly separate from current evidence.")
