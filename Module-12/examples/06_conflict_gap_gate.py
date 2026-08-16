from capstone_core import collect_evidence, detect_conflicts, detect_gaps

evidence = [
    collect_evidence("E1", "get_pipeline_status", {"environment": "production"}),
    collect_evidence("E2", "get_terraform_changes", {"environment": "production"}),
    # E3 intentionally omitted to demonstrate the guardrail.
]

gaps = detect_gaps(evidence)
conflicts = detect_conflicts(evidence)

print("Evidence IDs:", [e["id"] for e in evidence])
print("Gaps:", gaps)
print("Conflicts:", conflicts)

status = "INSUFFICIENT_EVIDENCE" if gaps else "READY_FOR_SYNTHESIS"
print("Status:", status)
assert status == "INSUFFICIENT_EVIDENCE"
