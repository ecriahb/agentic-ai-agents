from security_core import redact_secrets

sample = """
Pipeline failed.
api_key=abc123
Authorization: Bearer super-secret-token
Database status=healthy
"""

redacted, hits = redact_secrets(sample)
print("=== Redacted Output ===")
print(redacted)
print("Secret-like values redacted:", hits)
