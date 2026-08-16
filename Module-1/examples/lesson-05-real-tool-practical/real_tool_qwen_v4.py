from pathlib import Path
from typing import Literal

from ollama import chat
from pydantic import BaseModel

MODEL = "qwen3:0.6b"
LOG_FILE = Path(__file__).parent / "logs" / "pipeline.log"


class FinalRCA(BaseModel):
    evidence: list[str]
    likely_root_cause: str
    confirmed_impact: list[str]
    recommended_fix: list[str]
    confidence: Literal["low", "medium", "high"]


def read_pipeline_log() -> str:
    return LOG_FILE.read_text(encoding="utf-8")


def format_evidence(evidence_log: list[dict[str, str]]) -> str:
    return "\n\n".join(
        f"Tool: {item['tool']}\nObservation:\n{item['observation']}"
        for item in evidence_log
    )


messages = [
    {
        "role": "user",
        "content": (
            "Investigate the AKS deployment failure after Terraform changes. "
            "Use the available evidence tool."
        ),
    }
]

evidence_log: list[dict[str, str]] = []
response = chat(model=MODEL, messages=messages, tools=[read_pipeline_log])

if not response.message.tool_calls:
    raise RuntimeError("RCA blocked: no tool call and therefore no evidence.")

for tool_call in response.message.tool_calls:
    if tool_call.function.name != "read_pipeline_log":
        raise RuntimeError(f"Blocked unknown tool: {tool_call.function.name}")

    observation = read_pipeline_log()
    evidence_log.append(
        {"tool": tool_call.function.name, "observation": observation}
    )

    print("\n===== TOOL REQUESTED =====")
    print(f"Tool: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")
    print("\n===== TOOL RESULT =====")
    print(observation)

print("\n===== PRESERVED EVIDENCE =====")
print(format_evidence(evidence_log))

schema = FinalRCA.model_json_schema()
report_prompt = f"""
Use only the evidence below.
Do not add unsupported facts.
Return JSON only and match this schema exactly:
{schema}

Evidence:
{format_evidence(evidence_log)}
"""

report_response = chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a strict evidence-only DevOps RCA reporter.",
        },
        {"role": "user", "content": report_prompt},
    ],
    format="json",
)

validated_rca = FinalRCA.model_validate_json(report_response.message.content)

print("\n===== V4 PYDANTIC-VALIDATED RCA =====")
print(validated_rca.model_dump_json(indent=2))
