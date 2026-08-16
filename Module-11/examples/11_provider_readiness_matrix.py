"""Production-readiness comparison for local/self-hosted and OpenAI hosted providers.

This is an architecture lab, not a model-quality benchmark.
"""

PROVIDERS = {
    "ollama_local_learning": {
        "identity_defined": True,
        "network_boundary_defined": True,
        "egress_reviewed": True,
        "model_version_pinned": True,
        "capacity_plan_defined": False,
        "ha_dr_defined": False,
        "data_boundary_documented": True,
        "eval_suite_required": True,
    },
    "openai_hosted": {
        "identity_defined": True,
        "network_boundary_defined": True,
        "egress_reviewed": True,
        "model_version_pinned": True,
        "capacity_plan_defined": True,
        "ha_dr_defined": True,
        "data_boundary_documented": True,
        "eval_suite_required": True,
    },
}

CRITICAL = {
    "identity_defined",
    "network_boundary_defined",
    "egress_reviewed",
    "model_version_pinned",
    "data_boundary_documented",
    "eval_suite_required",
}

for name, checks in PROVIDERS.items():
    missing_critical = sorted(key for key in CRITICAL if not checks[key])
    incomplete = sorted(key for key, value in checks.items() if not value)

    print(f"\n=== {name} ===")
    for key, value in checks.items():
        print(f"{key:28} {'PASS' if value else 'GAP'}")

    if missing_critical:
        print("Production gate: BLOCK")
        print("Critical gaps:", missing_critical)
    elif incomplete:
        print("Production gate: REVIEW")
        print("Non-critical/incomplete areas:", incomplete)
    else:
        print("Production gate: READY_FOR_NEXT_GATE")

print("\nArchitecture rule: provider choice changes operational responsibilities, not evidence/policy rules.")
