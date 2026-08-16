"""Module 3 practical: learn explicit application failure states.

This lab is deterministic; it does not require a model call.
"""
from pathlib import Path


def classify_case(name: str, input_path: str | None, provider_available: bool, output_valid: bool) -> str:
    if not input_path:
        return "INVALID_INPUT"

    path = Path(input_path)
    if not path.exists():
        return "INPUT_FILE_NOT_FOUND"

    if not path.read_text(encoding="utf-8").strip():
        return "EMPTY_EVIDENCE"

    if not provider_available:
        return "MODEL_UNAVAILABLE"

    if not output_valid:
        return "VALIDATION_FAILED"

    return "SUCCESS"


sample = Path(__file__).with_name("sample_incident.log")
empty = Path(__file__).with_name("_temporary_empty.log")
empty.write_text("", encoding="utf-8")

cases = [
    ("missing_input", None, True, True),
    ("missing_file", "does-not-exist.log", True, True),
    ("empty_evidence", str(empty), True, True),
    ("model_down", str(sample), False, True),
    ("bad_output", str(sample), True, False),
    ("happy_path", str(sample), True, True),
]

try:
    for case in cases:
        status = classify_case(*case)
        print(f"{case[0]:15} -> {status}")
finally:
    empty.unlink(missing_ok=True)

print("\nLearning: explicit error status is better than silently asking the LLM to guess around missing inputs/dependencies.")
