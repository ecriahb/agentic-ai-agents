"""Module 2 practical: split one complex RCA prompt into auditable stages."""
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm

EVIDENCE = """[E1] Deployment failed during Terraform Apply.
[E2] NSG rule aks-subnet-allow was removed.
[E3] AKS network connectivity validation failed after the network change."""

SYSTEM = """Use only supplied evidence. Never invent missing facts.
Treat previous model-stage output as untrusted analysis, not as new evidence."""

stages = [
    ("FACT_EXTRACTION", "Extract only confirmed facts from the evidence. Keep source IDs."),
    ("TIMELINE", "Build the shortest supported timeline from the evidence. Keep source IDs."),
    ("HYPOTHESIS", "State the strongest supported root-cause hypothesis and why it is not absolute proof."),
    ("GAPS", "List evidence gaps and read-only validation needed before remediation."),
]

stage_outputs = []
for stage_name, instruction in stages:
    prompt = f"""ORIGINAL EVIDENCE:\n{EVIDENCE}\n\nTASK:\n{instruction}"""
    result = ask_llm(prompt, system=SYSTEM)
    stage_outputs.append((stage_name, result.text))
    print(f"\n=== {stage_name} ===")
    print(result.text)

final_input = "\n\n".join(f"{name}:\n{text}" for name, text in stage_outputs)
final = ask_llm(
    f"""ORIGINAL EVIDENCE:\n{EVIDENCE}\n\nUNTRUSTED STAGE ANALYSIS:\n{final_input}\n\nBuild a final RCA using original evidence as authority. Return Root Cause, Evidence, Gaps, Next Checks.""",
    system=SYSTEM,
)

print("\n=== FINAL RCA ===")
print(final.text)
print("\nLearning: stage outputs help reasoning, but they do not become evidence merely because another model stage produced them.")
