"""Run deterministic specialist collection, then switch only the synthesis LLM.

The specialist evidence contract is provider-independent.
"""

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO_ROOT))

from specialists import (
    aks_specialist,
    flatten_evidence,
    pipeline_specialist,
    terraform_specialist,
)
from shared.llm_provider import ask_llm

results = [
    pipeline_specialist("production"),
    terraform_specialist("production"),
    aks_specialist("prod-aks"),
]
evidence = flatten_evidence(results)

context_lines = []
for item in evidence:
    context_lines.append(
        f"[{item['id']}] Agent={item['agent']}\n"
        f"Claim={item['claim']}\n"
        f"Source={item['source']}\n"
        f"Payload={item['payload']}"
    )
context = "\n\n".join(context_lines)

result = ask_llm(
    f"""Incident: Production AKS deployment failed after a Terraform networking change.

CURRENT SPECIALIST EVIDENCE:
{context}
""",
    system="""You synthesize a read-only multi-agent DevOps investigation.
Treat agent messages as analysis unless their E* evidence envelope supports the claim.
Use only supplied E* evidence for incident facts.
Do not use majority voting as truth.
Return Root Cause, Confirmed Evidence, Conflicts/Gaps, Recommended Next Checks, Confidence.
""",
)

print("Provider:", result.provider)
print("Model:", result.model)
print("Specialists:", [item["agent"] for item in results])
print("Evidence IDs:", [item["id"] for item in evidence])
print("\n=== Synthesis ===")
print(result.text)
