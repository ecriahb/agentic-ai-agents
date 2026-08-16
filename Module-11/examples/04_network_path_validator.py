dependencies = [
    {"name": "state-db", "private": True, "dns_private": True, "egress_approved": True},
    {"name": "vector-search", "private": True, "dns_private": True, "egress_approved": True},
    {"name": "model-gateway", "private": False, "dns_private": False, "egress_approved": True},
    {"name": "unknown-mcp", "private": False, "dns_private": False, "egress_approved": False},
]


def validate(dep: dict) -> tuple[bool, list[str]]:
    errors = []
    if dep["private"] and not dep["dns_private"]:
        errors.append("PRIVATE_DNS_MISSING")
    if not dep["private"] and not dep["egress_approved"]:
        errors.append("EGRESS_NOT_APPROVED")
    return not errors, errors


for dep in dependencies:
    ok, errors = validate(dep)
    print(f"{dep['name']:15} ok={ok} errors={errors}")
