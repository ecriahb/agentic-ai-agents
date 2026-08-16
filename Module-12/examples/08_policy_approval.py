from capstone_core import evaluate_action_policy

proposal = {
    "type": "WRITE_PROPOSAL",
    "action": "restore_nsg_rule",
    "target": "aks-subnet-allow",
    "environment": "production",
    "supporting_evidence_ids": ["E2", "E3"],
}

print("Proposal:", proposal)

allowed, reason = evaluate_action_policy(proposal, approved=False)
print("Without approval:", allowed, reason)
assert not allowed and reason == "APPROVAL_REQUIRED"

allowed, reason = evaluate_action_policy(proposal, approved=True)
print("With approval:", allowed, reason)
assert allowed and reason == "APPROVED_BUT_NOT_EXECUTED_DEMO"

print("Safety: approval is demonstrated, but no real cloud write exists.")
