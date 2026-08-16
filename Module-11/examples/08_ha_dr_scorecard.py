controls = {
    "multi_instance_api": True,
    "worker_redundancy": True,
    "persistent_state": True,
    "state_backup_tested": True,
    "vector_rebuild_plan": True,
    "model_fallback_evaluated": False,
    "regional_dr_runbook": True,
    "approval_replay_protection": True,
}

passed = sum(controls.values())
total = len(controls)
score = passed / total * 100

for name, value in controls.items():
    print(f"{name:30} {'PASS' if value else 'GAP'}")

print(f"\nHA/DR readiness: {score:.1f}%")
if not controls["model_fallback_evaluated"]:
    print("BLOCKER: fallback model must be evaluated before production use.")
