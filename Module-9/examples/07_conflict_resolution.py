from datetime import datetime


observations = [
    {
        "id": "E3",
        "claim": "AKS connectivity degraded",
        "source": "aks_health_check",
        "observed_at": "2026-08-16T10:00:00+05:30",
        "value": "DEGRADED",
    },
    {
        "id": "E4",
        "claim": "AKS connectivity healthy",
        "source": "aks_health_check",
        "observed_at": "2026-08-16T10:20:00+05:30",
        "value": "HEALTHY",
    },
]


def resolve_latest_authoritative(items: list[dict]) -> dict:
    parsed = sorted(items, key=lambda x: datetime.fromisoformat(x["observed_at"]))
    latest = parsed[-1]
    return {
        "status": "RESOLVED_BY_FRESHNESS",
        "selected_evidence_id": latest["id"],
        "selected_value": latest["value"],
        "all_evidence_ids": [item["id"] for item in parsed],
    }


resolution = resolve_latest_authoritative(observations)

print("=== Conflict ===")
for item in observations:
    print(item)

print("\n=== Resolution ===")
print(resolution)
print("\nLearning point: disagreement is resolved by provenance/freshness policy, not majority voting.")
