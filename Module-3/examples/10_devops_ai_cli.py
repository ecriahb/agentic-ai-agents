"""Module 3 V10: tiny robust DevOps AI CLI.

Usage:
    python 10_devops_ai_cli.py sample_incident.log

Provider:
    LLM_PROVIDER=ollama (default) or openai
"""
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from shared.llm_provider import ask_llm

SYSTEM = """You are a read-only DevOps incident analyst.
Use only supplied evidence. If the evidence does not support a root cause, say UNKNOWN.
Do not invent customer impact, outage duration, actors or completed remediation.
Return Root Cause, Evidence, Missing Evidence, Next Checks."""


def main() -> int:
    if len(sys.argv) != 2:
        print("Status: INVALID_USAGE")
        print("Usage: python 10_devops_ai_cli.py <log-file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists() or not path.is_file():
        print("Status: INPUT_FILE_NOT_FOUND")
        return 2

    evidence = path.read_text(encoding="utf-8").strip()
    if not evidence:
        print("Status: EMPTY_EVIDENCE")
        return 2

    try:
        result = ask_llm(
            f"Analyze this source evidence:\n\n{evidence}",
            system=SYSTEM,
        )
    except Exception as exc:
        print("Status: MODEL_CALL_FAILED")
        print("Error:", exc)
        return 1

    if not result.text.strip():
        print("Status: EMPTY_MODEL_RESPONSE")
        return 1

    print("Status: SUCCESS")
    print("Provider:", result.provider)
    print("Model:", result.model)
    print("\n=== ANALYSIS ===")
    print(result.text)
    print("\nRule: successful API call does not itself prove the answer is factually correct.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
