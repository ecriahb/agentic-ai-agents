records = [
    {"name": "workflow_checkpoint", "class": "STATE", "ttl_days": 7, "authoritative": False},
    {"name": "incident_evidence", "class": "EVIDENCE", "ttl_days": 365, "authoritative": True},
    {"name": "runbook_chunk", "class": "REFERENCE", "ttl_days": 30, "authoritative": False},
    {"name": "audit_event", "class": "AUDIT", "ttl_days": 730, "authoritative": True},
]

classes = {item["class"] for item in records}
assert classes == {"STATE", "EVIDENCE", "REFERENCE", "AUDIT"}

for item in records:
    print(item)

print("PASS: state, evidence, reference knowledge and audit are modeled separately.")
