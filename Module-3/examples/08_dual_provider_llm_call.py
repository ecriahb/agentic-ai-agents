"""Module 3 provider-parity API example.

The application code calls one helper while the provider changes through environment config.
"""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm

prompt = """A deployment failed after a Terraform network change.
Explain in beginner-friendly language what evidence you would collect before claiming a root cause.
"""

result = ask_llm(
    prompt,
    system="You are a careful DevOps AI tutor. Do not invent tool results.",
)

print(f"Provider: {result.provider}")
print(f"Model: {result.model}")
print(result.text)
