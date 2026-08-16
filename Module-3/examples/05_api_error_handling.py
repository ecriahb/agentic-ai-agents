import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")


def call_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]

    except requests.Timeout as exc:
        raise RuntimeError("Ollama request timed out") from exc

    except requests.ConnectionError as exc:
        raise RuntimeError("Cannot connect to Ollama. Is Ollama running?") from exc

    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else "unknown"
        raise RuntimeError(f"Ollama HTTP error: {status}") from exc

    except (ValueError, KeyError, TypeError) as exc:
        raise RuntimeError("Unexpected Ollama response format") from exc


if __name__ == "__main__":
    try:
        print(call_ollama("Give one reason why an AKS deployment can fail."))
    except RuntimeError as exc:
        print("Application error:", exc)
