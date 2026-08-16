"""Run the same grounded DevOps prompt on Ollama or OpenAI.

PowerShell examples:
  $env:LLM_PROVIDER="ollama"
  python Module-2/examples/dual_provider_prompt_playground.py

  $env:LLM_PROVIDER="openai"
  $env:OPENAI_API_KEY="..."
  python Module-2/examples/dual_provider_prompt_playground.py
"""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm

SYSTEM = """You are a read-only DevOps incident analyst.
Use only the evidence supplied by the user for current-incident factual claims.
Separate confirmed facts from hypotheses.
If evidence is insufficient, say so.
Do not invent outage duration, customer impact, actor identity, or successful remediation.
Return: Root Cause, Evidence, Impact, Recommended Next Checks, Confidence.
"""

EVIDENCE = """[E1] Deployment failed during Terraform Apply.
[E2] Terraform Apply removed NSG rule aks-subnet-allow.
[E3] AKS subnet connectivity validation failed after the change.
"""

PROMPT = f"""Analyze this production AKS deployment failure.

CURRENT EVIDENCE:
{EVIDENCE}
"""

result = ask_llm(PROMPT, system=SYSTEM)

print("Provider:", result.provider)
print("Model:", result.model)
print("\n=== Answer ===")
print(result.text)
