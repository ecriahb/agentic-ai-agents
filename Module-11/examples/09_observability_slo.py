telemetry = {
    "investigations_total": 1000,
    "completed_within_120s": 994,
    "write_executions": 12,
    "write_with_auth_approval_audit": 12,
    "citation_validation_failures": 3,
    "policy_denials": 21,
}

latency_sli = telemetry["completed_within_120s"] / telemetry["investigations_total"] * 100
write_trust_sli = telemetry["write_with_auth_approval_audit"] / max(1, telemetry["write_executions"]) * 100

print(f"Investigation latency SLI: {latency_sli:.2f}%")
print(f"Privileged-write trust SLI: {write_trust_sli:.2f}%")
print("Citation validation failures:", telemetry["citation_validation_failures"])
print("Policy denials:", telemetry["policy_denials"])

assert write_trust_sli == 100.0
print("PASS: privileged writes preserve the required invariant.")
