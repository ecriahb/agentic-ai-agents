"""Module 4 practical: metadata filtering before semantic retrieval.

This lab is deterministic so the metadata concept is easy to see.
"""

records = [
    {
        "chunk_id": "aks-prod-001",
        "text": "Validate production AKS effective NSG rules after network changes.",
        "environment": "production",
        "team": "platform",
        "source": "aks-runbook.md",
    },
    {
        "chunk_id": "aks-dev-001",
        "text": "Developers may restart the dev test deployment after sandbox validation.",
        "environment": "dev",
        "team": "platform",
        "source": "dev-notes.md",
    },
    {
        "chunk_id": "sql-prod-001",
        "text": "Production SQL failover procedure requires DBA approval.",
        "environment": "production",
        "team": "database",
        "source": "sql-runbook.md",
    },
]


def filter_records(environment: str | None = None, team: str | None = None) -> list[dict]:
    result = records
    if environment:
        result = [item for item in result if item["environment"] == environment]
    if team:
        result = [item for item in result if item["team"] == team]
    return result


for label, kwargs in [
    ("NO FILTER", {}),
    ("PRODUCTION", {"environment": "production"}),
    ("PRODUCTION PLATFORM", {"environment": "production", "team": "platform"}),
]:
    print(f"\n=== {label} ===")
    for item in filter_records(**kwargs):
        print(item["chunk_id"], "|", item["source"], "|", item["text"])

print("\nImportant: metadata filtering narrows candidates; it is NOT a substitute for authorization/ACL checks.")
