environments = {
    "dev": {"subscription": "ai-dev", "identity": "dev-agent", "prod_access": False},
    "stage": {"subscription": "ai-stage", "identity": "stage-agent", "prod_access": False},
    "prod": {"subscription": "ai-prod", "identity": "prod-agent", "prod_access": True},
}

assert len({v["subscription"] for v in environments.values()}) == 3
assert environments["dev"]["identity"] != environments["prod"]["identity"]
assert environments["stage"]["identity"] != environments["prod"]["identity"]
assert environments["dev"]["prod_access"] is False

for env, config in environments.items():
    print(env, config)

print("PASS: prod/non-prod subscription and identity boundaries are explicit.")
