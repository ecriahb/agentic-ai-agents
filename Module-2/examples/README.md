# Module 2 — Practical Prompt Examples

These files are copy-paste starting points for the lessons.

## Files

- `incident_rca_prompt.txt` — grounded incident RCA template
- `terraform_change_review_prompt.txt` — Terraform plan/change risk review
- `aks_troubleshooting_prompt.txt` — layered AKS troubleshooting prompt
- `prompt_playground.py` — simple local Ollama prompt runner

## Recommended Practice Order

```text
1. Run a weak prompt
2. Observe vague/unsupported output
3. Add Role + Context + Task + Constraints + Output
4. Add evidence IDs
5. Add abstention rule
6. Compare results
7. Save the improved prompt as a reusable template
```

## Important

Prompt guardrails do not replace application security. Real production tools should still use allowlists, argument validation, read-only RBAC, approval and audit logging.
