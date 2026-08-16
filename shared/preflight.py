"""Beginner-friendly local environment preflight.

Run from repository root:
    python shared/preflight.py

This does not send a model request. It only checks local configuration/imports
and, for Ollama, whether the local API is reachable.
"""

from __future__ import annotations

import importlib.util
import os
import platform
import sys


MIN_PYTHON = (3, 10)


def status(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


print("=== Agentic AI Course Preflight ===")
print("Python:", sys.version.split()[0])
print("OS:", platform.platform())

python_ok = sys.version_info >= MIN_PYTHON
print("Python >= 3.10:", status(python_ok))

packages = ["requests", "dotenv", "openai"]
print("\nShared provider packages:")
for package in packages:
    found = importlib.util.find_spec(package) is not None
    print(f"- {package:10} {status(found)}")

provider = os.getenv("LLM_PROVIDER", "ollama").strip().lower()
print("\nLLM_PROVIDER:", provider)

if provider == "ollama":
    model = os.getenv("OLLAMA_MODEL", "qwen3:4b")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
    print("OLLAMA_MODEL:", model)
    print("OLLAMA_BASE_URL:", base_url)

    try:
        import requests

        response = requests.get(f"{base_url}/api/tags", timeout=3)
        response.raise_for_status()
        names = [item.get("name", "") for item in response.json().get("models", [])]
        print("Ollama API reachable: PASS")
        if any(name == model or name.startswith(f"{model}:") for name in names):
            print("Configured model installed: PASS")
        else:
            print("Configured model installed: FAIL")
            print("Installed models:", names or "none")
            print(f"Suggested command: ollama pull {model}")
    except Exception as exc:
        print("Ollama API reachable: FAIL")
        print("Reason:", type(exc).__name__)
        print("Check that Ollama is installed/running before local model labs.")

elif provider == "openai":
    key_present = bool(os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    print("OPENAI_API_KEY present:", status(key_present))
    print("OPENAI_MODEL:", model)
    print("No API request was made by preflight.")

else:
    print("Provider configuration: FAIL")
    print("Use LLM_PROVIDER=ollama or LLM_PROVIDER=openai")

print("\nModule-specific packages are installed from each Module-X/examples/requirements.txt.")
print("Preflight does not prove model quality, cloud authorization, or production readiness.")
