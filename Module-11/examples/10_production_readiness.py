REQUIRED_CONTROLS = {
    "prod_identity_isolated": True,
    "write_executor_isolated": True,
    "private_dependency_paths": True,
    "controlled_egress": True,
    "persistent_state": True,
    "evidence_store_separate": True,
    "rag_acl_enforced": True,
    "backpressure_defined": True,
    "dr_tested": True,
    "end_to_end_tracing": True,
    "security_eval_gate": True,
    "cost_owner_defined": True,
}

CRITICAL = {
    "prod_identity_isolated",
    "write_executor_isolated",
    "persistent_state",
    "rag_acl_enforced",
    "security_eval_gate",
}

failures = [name for name, ok in REQUIRED_CONTROLS.items() if not ok]
critical_failures = sorted(CRITICAL.intersection(failures))

score = (len(REQUIRED_CONTROLS) - len(failures)) / len(REQUIRED_CONTROLS) * 100

print("=== Production Readiness ===")
for name, ok in REQUIRED_CONTROLS.items():
    print(f"{name:30} {'PASS' if ok else 'FAIL'}")

print(f"\nScore: {score:.1f}%")
print("Critical failures:", critical_failures)

release = not failures and not critical_failures
print("Release decision:", "READY_FOR_CAPSTONE" if release else "BLOCKED")
