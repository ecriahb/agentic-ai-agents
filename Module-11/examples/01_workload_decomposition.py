components = {
    "api": {"trust": "USER_INPUT", "state": "none", "identity": "agent-api-mi"},
    "worker": {"trust": "MIXED", "state": "workflow", "identity": "agent-worker-mi"},
    "tool_gateway": {"trust": "CAPABILITY", "state": "audit", "identity": "read-tool-mi"},
    "rag": {"trust": "REFERENCE_DATA", "state": "index", "identity": "rag-mi"},
    "write_executor": {"trust": "HIGH_RISK", "state": "operation", "identity": "write-executor-mi"},
}

print("=== Enterprise Workload Decomposition ===")
for name, meta in components.items():
    print(f"{name:15} identity={meta['identity']:20} trust={meta['trust']:14} state={meta['state']}")

assert components["worker"]["identity"] != components["write_executor"]["identity"]
print("\nPASS: investigation and write execution use separate identities.")
