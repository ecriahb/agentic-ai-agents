"""Module 1 Lab 03: Structured RCA output with Ollama + Pydantic."""

from typing import Literal

from ollama import chat
from pydantic import BaseModel, Field


class RCAResponse(BaseModel):
    root_cause: str = Field(min_length=5)
    impact: str = Field(min_length=5)
    fix: str = Field(min_length=5)
    severity: Literal["low", "medium", "high", "critical"]


messages = [
    {
        "role": "system",
        "content": "Use only provided evidence. Do not invent missing facts.",
    },
    {
        "role": "user",
        "content": (
            "Evidence: AKS deployment failed after a Terraform networking change. "
            "Generate a concise RCA."
        ),
    },
]

response = chat(
    model="gemma3:1b",
    messages=messages,
    format=RCAResponse.model_json_schema(),
)

result = RCAResponse.model_validate_json(response.message.content)

print("Root Cause:", result.root_cause)
print("Impact:", result.impact)
print("Fix:", result.fix)
print("Severity:", result.severity)
