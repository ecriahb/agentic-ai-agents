ASSETS = [
    "Azure credentials",
    "Terraform state",
    "AKS production access",
    "pipeline logs",
    "approval decisions",
]

TRUST_BOUNDARIES = [
    "user -> agent",
    "agent -> tool host",
    "agent -> RAG",
    "host -> MCP server",
    "agent -> human approval",
]

THREATS = [
    ("prompt injection", "user/RAG input", "host-side policy"),
    ("secret leakage", "tool result/output", "redaction + minimization"),
    ("excessive agency", "tool execution", "least privilege + approval"),
    ("fake evidence", "agent messages", "provenance validation"),
]

print("=== DevOps Agent Threat Model ===")
print("Assets:")
for item in ASSETS:
    print(" -", item)

print("\nTrust boundaries:")
for item in TRUST_BOUNDARIES:
    print(" -", item)

print("\nThreats:")
for threat, entry, control in THREATS:
    print(f" - {threat}: entry={entry}; control={control}")
