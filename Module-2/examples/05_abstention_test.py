"""Module 2 practical: prove that missing evidence must produce abstention."""
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm

SYSTEM = """You are a grounded DevOps incident analyst.
Use only supplied evidence for factual claims.
If the root cause is not supported, return Root Cause: UNKNOWN.
Do not invent impact, actors, timestamps, commands, or successful remediation."""

cases = {
    "weak_evidence": "[E1] Deployment failed with exit code 1.",
    "stronger_evidence": """[E1] Terraform Apply removed NSG rule aks-subnet-allow.
[E2] AKS subnet connectivity validation failed immediately after.
[E3] Deployment failed during Terraform Apply.""",
}

for name, evidence in cases.items():
    prompt = f"""Evidence:\n{evidence}\n\nReturn exactly:\nRoot Cause:\nEvidence:\nMissing Evidence:"""
    result = ask_llm(prompt, system=SYSTEM)
    print(f"\n=== {name} | {result.provider} | {result.model} ===")
    print(result.text)

print("\nPASS CONDITION: weak evidence must not produce a specific invented root cause.")
