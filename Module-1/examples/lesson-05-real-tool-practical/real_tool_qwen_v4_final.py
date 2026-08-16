from pathlib import Path
from typing import Literal

from ollama import chat
from pydantic import BaseModel, ValidationError

MODEL = "qwen3:0.6b"
LOG_FILE = Path(__file__).parent / "logs" / "pipeline.log"


class FinalRCA(BaseModel):
    evidence: list[str]
    likely_root_cause: str
    confirmed_impact: list[str]
    recommended_fix: list[str]
    confidence: Literal["low", "medium", "high"]


def read_pipeline_log() -> str:
    """Read the local pipeline.log. This tool accepts no arguments."""
    return LOG_FILE.read_text(encoding="utf-8")


TOOL_REGISTRY = {
    "read_pipeline_log": {
        "function": read_pipeline_log,
        "allowed_arguments": set(),
    }
}


def validate_tool_call(tool_name: str, arguments: dict) -> None:
    """Allow only known tools and the arguments defined by our host contract."""
    if tool_name not in TOOL_REGISTRY:
        raise RuntimeError(f"Blocked tool: {tool_name} is not in the allowlist.")

    allowed_arguments = TOOL_REGISTRY[tool_name]["allowed_arguments"]
    received_arguments = set(arguments.keys())
    unexpected = received_arguments - allowed_arguments

    if unexpected:
        raise RuntimeError(
            f"Blocked invalid arguments for {tool_name}: {sorted(unexpected)}. "
            f"Allowed arguments: {sorted(allowed_arguments)}"
        )


def format_evidence(evidence_log: list[dict[str, str]]) -> str:
    return "\n\n".join(
        f"Tool: {item['tool']}\nObservation:\n{item['observation']}"
        for item in evidence_log
    )


def normalize(text: str) -> str:
    return " ".join(text.lower().replace("-", " ").split())


def evidence_supports_claim(claim: str, evidence_text: str) -> bool:
    """Simple deterministic token-overlap check used after LLM generation."""
    stop_words = {
        "the", "a", "an", "and", "or", "to", "of", "in", "on", "for",
        "was", "were", "is", "are", "be", "been", "with", "during", "after",
        "this", "that", "from", "it", "as", "by",
    }

    claim_tokens = {
        token.strip(".,:;()[]{}")
        for token in normalize(claim).split()
        if len(token.strip(".,:;()[]{}")) >= 4
        and token.strip(".,:;()[]{}") not in stop_words
    }
    evidence_tokens = set(normalize(evidence_text).split())

    if not claim_tokens:
        return False

    matched = claim_tokens & evidence_tokens
    return len(matched) >= min(2, len(claim_tokens))


def extract_confirmed_impacts(evidence_text: str) -> list[str]:
    """Impact is derived from evidence instead of trusting model wording."""
    impact_keywords = (
        "failed", "failure", "degraded", "unavailable", "outage",
        "downtime", "error", "blocked",
    )

    impacts = []
    for raw_line in evidence_text.splitlines():
        line = raw_line.strip()
        if line and any(keyword in line.lower() for keyword in impact_keywords):
            impacts.append(line)

    # Preserve order while removing duplicates.
    return list(dict.fromkeys(impacts))


def filter_confirmed_impacts(
    proposed_impacts: list[str], evidence_text: str
) -> list[str]:
    """Keep only impact claims that are both impact-like and evidence-supported."""
    impact_keywords = (
        "failed", "failure", "degraded", "unavailable", "outage",
        "downtime", "error", "blocked",
    )

    return [
        impact
        for impact in proposed_impacts
        if any(keyword in impact.lower() for keyword in impact_keywords)
        and evidence_supports_claim(impact, evidence_text)
    ]


def enforce_confidence_policy(
    requested_confidence: str,
    evidence_source_count: int,
) -> Literal["low", "medium", "high"]:
    """One evidence source is not enough for 'high' confidence."""
    if requested_confidence == "high" and evidence_source_count < 2:
        return "medium"
    return requested_confidence  # type: ignore[return-value]


def validate_business_claims(rca: FinalRCA, evidence_text: str) -> FinalRCA:
    """Apply deterministic trust rules after schema validation."""
    if not evidence_supports_claim(rca.likely_root_cause, evidence_text):
        raise ValueError(
            "Likely root cause is not sufficiently supported by collected evidence."
        )

    supported_model_impacts = filter_confirmed_impacts(
        rca.confirmed_impact, evidence_text
    )
    deterministic_impacts = extract_confirmed_impacts(evidence_text)

    rca.confirmed_impact = supported_model_impacts or deterministic_impacts
    rca.confidence = enforce_confidence_policy(
        rca.confidence,
        evidence_source_count=1,
    )
    return rca


def request_structured_rca(evidence_log: list[dict[str, str]]) -> FinalRCA:
    schema = FinalRCA.model_json_schema()
    evidence = format_evidence(evidence_log)

    prompt = f"""
Create a DevOps RCA using ONLY the evidence below.

Rules:
1. Do not invent outages, downtime, customer impact, or Azure facts not shown in evidence.
2. 'likely_root_cause' must directly reflect the evidence.
3. 'confirmed_impact' must contain only impacts explicitly supported by evidence.
4. Recommended fixes may be recommendations, but keep them tied to the observed failure.
5. Return JSON only and match this schema exactly:
{schema}

Evidence:
{evidence}
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a strict evidence-grounded DevOps RCA reporter.",
            },
            {"role": "user", "content": prompt},
        ],
        format="json",
    )

    try:
        return FinalRCA.model_validate_json(response.message.content)
    except ValidationError as exc:
        # One controlled repair attempt: repair structure, never add new evidence.
        repair = chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Repair the JSON structure only. Do not add facts. "
                        "Return JSON only."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Schema:\n{schema}\n\nValidation error:\n{exc}\n\n"
                        f"Original output:\n{response.message.content}\n\n"
                        f"Trusted evidence:\n{evidence}"
                    ),
                },
            ],
            format="json",
        )
        return FinalRCA.model_validate_json(repair.message.content)


# -------------------- INVESTIGATION --------------------
messages = [
    {
        "role": "user",
        "content": (
            "Investigate why the AKS deployment started failing after Terraform changes. "
            "Use the available tool before reporting an RCA."
        ),
    }
]

evidence_log: list[dict[str, str]] = []
response = chat(model=MODEL, messages=messages, tools=[read_pipeline_log])

if not response.message.tool_calls:
    raise RuntimeError("RCA blocked: model requested no tool, so no evidence exists.")

for tool_call in response.message.tool_calls:
    tool_name = tool_call.function.name
    arguments = dict(tool_call.function.arguments or {})

    print("\n===== TOOL REQUESTED =====")
    print(f"Tool: {tool_name}")
    print(f"Arguments: {arguments}")

    # This catches the practical hallucination where Qwen may invent arguments
    # such as {"environment": "production"} for a zero-argument tool.
    validate_tool_call(tool_name, arguments)

    observation = TOOL_REGISTRY[tool_name]["function"]()

    print("\n===== TOOL RESULT =====")
    print(observation)

    evidence_log.append(
        {
            "tool": tool_name,
            "observation": observation,
        }
    )

print("\n===== PRESERVED EVIDENCE =====")
print(format_evidence(evidence_log))

# -------------------- REPORTING --------------------
validated_rca = request_structured_rca(evidence_log)
validated_rca = validate_business_claims(
    validated_rca,
    format_evidence(evidence_log),
)

print("\n===== FINAL TRUSTED RCA =====")
print(validated_rca.model_dump_json(indent=2))
