"""Small provider abstraction used by beginner parity labs.

Supported providers:
- ollama: local /api/chat endpoint
- openai: official OpenAI Python SDK + Responses API

This helper intentionally returns plain text plus provider metadata.
Application-specific validation must happen outside this module.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class LLMResult:
    provider: str
    model: str
    text: str


def _ask_ollama(prompt: str, system: Optional[str]) -> LLMResult:
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
    model = os.getenv("OLLAMA_MODEL", "qwen3:4b")

    messages: list[dict[str, str]] = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        response = requests.post(
            f"{base_url}/api/chat",
            json={
                "model": model,
                "messages": messages,
                "stream": False,
            },
            timeout=180,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(
            "OLLAMA_CALL_FAILED: verify Ollama is running and OLLAMA_MODEL is installed"
        ) from exc

    payload = response.json()
    text = payload.get("message", {}).get("content", "").strip()
    if not text:
        raise RuntimeError("OLLAMA_EMPTY_RESPONSE")

    return LLMResult(provider="ollama", model=model, text=text)


def _ask_openai(prompt: str, system: Optional[str]) -> LLMResult:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "OPENAI_SDK_MISSING: pip install openai"
        ) from exc

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY_MISSING")

    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    client = OpenAI()

    kwargs: dict[str, object] = {
        "model": model,
        "input": prompt,
    }
    if system:
        kwargs["instructions"] = system

    try:
        response = client.responses.create(**kwargs)
    except Exception as exc:
        # Provider exceptions are converted to an explicit application failure.
        # The caller should log sanitized metadata, not secrets.
        raise RuntimeError("OPENAI_CALL_FAILED") from exc

    text = response.output_text.strip()
    if not text:
        raise RuntimeError("OPENAI_EMPTY_RESPONSE")

    return LLMResult(provider="openai", model=model, text=text)


def ask_llm(
    prompt: str,
    *,
    system: Optional[str] = None,
    provider: Optional[str] = None,
) -> LLMResult:
    """Call the selected model provider.

    Provider resolution:
      explicit provider argument
      → LLM_PROVIDER environment variable
      → ollama default
    """

    selected = (provider or os.getenv("LLM_PROVIDER", "ollama")).strip().lower()

    if not prompt or not prompt.strip():
        raise ValueError("prompt must not be empty")

    if selected == "ollama":
        return _ask_ollama(prompt.strip(), system)
    if selected == "openai":
        return _ask_openai(prompt.strip(), system)

    raise ValueError(
        f"Unsupported LLM_PROVIDER={selected!r}. Use 'ollama' or 'openai'."
    )
