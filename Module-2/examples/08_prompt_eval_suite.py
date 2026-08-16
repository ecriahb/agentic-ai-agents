"""Module 2 practical: small deterministic prompt-evaluation harness.

This is intentionally simple. It checks output contracts/forbidden claims; it does
not pretend to prove full semantic correctness.
"""
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm

SYSTEM = """You are a grounded DevOps incident analyst.
Use only supplied evidence. If root cause is unsupported, say UNKNOWN.
Do not invent customer impact, outage duration, actor identity or successful remediation.
Return exactly these sections: Root Cause, Evidence, Missing Evidence."""

CASES = [
    {
        "name": "strong_evidence",
        "evidence": "[E1] NSG rule removed. [E2] AKS network validation failed after it. [E3] deployment failed.",
        "must_contain": ["Root Cause", "Evidence", "Missing Evidence"],
        "must_not_contain": ["customer outage", "5 minutes"],
    },
    {
        "name": "weak_evidence",
        "evidence": "[E1] deployment exited with code 1.",
        "must_contain": ["UNKNOWN"],
        "must_not_contain": ["NSG rule was removed"],
    },
]

passed = 0
for case in CASES:
    result = ask_llm(f"Evidence:\n{case['evidence']}", system=SYSTEM)
    text = result.text
    missing = [item for item in case["must_contain"] if item.lower() not in text.lower()]
    forbidden = [item for item in case["must_not_contain"] if item.lower() in text.lower()]
    ok = not missing and not forbidden
    passed += int(ok)

    print(f"\n=== {case['name']} ===")
    print(text)
    print("PASS:", ok)
    print("Missing expected markers:", missing)
    print("Forbidden markers found:", forbidden)

print(f"\nScore: {passed}/{len(CASES)}")
print("Reminder: deterministic checks catch contract regressions; human/semantic review is still needed for nuanced truthfulness.")
