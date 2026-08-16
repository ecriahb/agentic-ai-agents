"""Module 2 practical: zero-shot vs one-shot vs few-shot comparison.

Switch provider with LLM_PROVIDER=ollama or openai.
"""
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm

EVIDENCE = """[E1] Deployment failed during Terraform Apply.
[E2] NSG rule aks-subnet-allow was removed.
[E3] AKS network connectivity validation is degraded."""

BASE_RULE = "Use only supplied evidence. If unsupported, say UNKNOWN."

zero_shot = f"""{BASE_RULE}
Evidence:
{EVIDENCE}
Return Root Cause and Evidence."""

one_shot = f"""{BASE_RULE}
Example:
Evidence: [E1] image pull failed because registry authentication returned 401.
Output:
Root Cause: Registry authentication failure [E1]
Evidence: [E1]

Now analyze:
{EVIDENCE}
Return Root Cause and Evidence."""

few_shot = f"""{BASE_RULE}
Example 1:
Evidence: [E1] registry authentication returned 401.
Output: Root Cause: Registry authentication failure [E1]\nEvidence: [E1]

Example 2:
Evidence: [E1] exit code 1 only.
Output: Root Cause: UNKNOWN\nEvidence: [E1]

Now analyze:
{EVIDENCE}
Return Root Cause and Evidence."""

for label, prompt in [
    ("ZERO-SHOT", zero_shot),
    ("ONE-SHOT", one_shot),
    ("FEW-SHOT", few_shot),
]:
    result = ask_llm(prompt)
    print(f"\n=== {label} | {result.provider} | {result.model} ===")
    print(result.text)

print("\nCompare format consistency and unsupported claims—not writing style only.")
