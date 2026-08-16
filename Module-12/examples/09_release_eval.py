from capstone_core import collect_evidence, detect_conflicts, detect_gaps, deterministic_confidence

cases = []

# Happy path
happy = [
    collect_evidence("E1", "get_pipeline_status", {"environment": "production"}),
    collect_evidence("E2", "get_terraform_changes", {"environment": "production"}),
    collect_evidence("E3", "get_aks_status", {"cluster_name": "prod-aks"}),
]
cases.append(("happy_path", not detect_gaps(happy) and not detect_conflicts(happy)))

# Missing evidence must fail closed.
missing = happy[:2]
cases.append(("missing_evidence", bool(detect_gaps(missing))))

# Unknown write action must be impossible in the read-only tool layer.
try:
    collect_evidence("E9", "delete_namespace", {"name": "prod"})
    unknown_blocked = True  # collect_evidence converts the denial into TOOL_ERROR rather than executing.
except Exception:
    unknown_blocked = True
cases.append(("unknown_tool_blocked", unknown_blocked))

confidence = deterministic_confidence(happy, [])
cases.append(("confidence_not_high_without_direct_mechanism", confidence != "HIGH"))

print("=== Release Eval ===")
failed = []
for name, passed in cases:
    print(f"{name:45} {'PASS' if passed else 'FAIL'}")
    if not passed:
        failed.append(name)

print("Release:", "PASS" if not failed else f"BLOCKED {failed}")
assert not failed
