import json
import os
from pathlib import Path
from typing import Literal

import requests
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")


class IncidentRCA(BaseModel):
    root_cause: str
    impact: str
    recommended_fix: list[str]
    severity: Literal["low", "medium", "high", "critical"]
    confidence: Literal["low", "medium", "high"]


def read_evidence(path: str) -> str:
    log_path = Path(path)

    if not log_path.exists():
        raise FileNotFoundError(f"Evidence file not found: {path}")

    evidence = log_path.read_text(encoding="utf-8").strip()

    if not evidence:
        raise RuntimeError("Evidence file is empty. RCA blocked.")

    return evidence


def build_prompt(evidence: str) -> str:
    return f"""
You are a senior Azure DevOps incident analyst.

Use ONLY the supplied evidence.
Do not invent facts or customer impact.
If the evidence does not support a definite claim, clearly keep the claim cautious.

EVIDENCE:
{evidence}

Return ONLY valid JSON with this exact shape:
{{
  "root_cause": "string",
  "impact": "string",
  "recommended_fix": ["string"],
  "severity": "low|medium|high|critical",
  "confidence": "low|medium|high"
}}
""".strip()


def call_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": "json",
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]


def validate_rca(raw_text: str) -> IncidentRCA:
    parsed = json.loads(raw_text)
    return IncidentRCA.model_validate(parsed)


def main():
    evidence_path = Path(__file__).with_name("sample_incident.log")
    evidence = read_evidence(str(evidence_path))
    prompt = build_prompt(evidence)
    raw_output = call_ollama(prompt)
    rca = validate_rca(raw_output)

    print("\n===== VALIDATED RCA =====")
    print(rca.model_dump_json(indent=2))


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as exc:
        print("Evidence error:", exc)
    except requests.Timeout:
        print("Ollama request timed out")
    except requests.ConnectionError:
        print("Cannot connect to Ollama. Is Ollama running?")
    except requests.HTTPError as exc:
        print("Ollama HTTP error:", exc)
    except json.JSONDecodeError:
        print("Model did not return valid JSON")
    except ValidationError as exc:
        print("RCA schema validation failed:")
        print(exc)
    except (KeyError, TypeError, ValueError, RuntimeError) as exc:
        print("Application error:", exc)
