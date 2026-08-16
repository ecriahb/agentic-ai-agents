from pathlib import Path
from ollama import chat

MODEL = "qwen3:0.6b"
LOG_FILE = Path(__file__).parent / "logs" / "pipeline.log"


def read_pipeline_log() -> str:
    return LOG_FILE.read_text(encoding="utf-8")


def format_evidence(evidence_log: list[dict[str, str]]) -> str:
    blocks = []
    for item in evidence_log:
        blocks.append(
            f"Tool: {item['tool']}\n"
            f"Observation:\n{item['observation']}"
        )
    return "\n\n".join(blocks)


messages = [
    {
        "role": "user",
        "content": (
            "Investigate why the AKS deployment failed after Terraform changes. "
            "Use the available tool first."
        ),
    }
]

evidence_log: list[dict[str, str]] = []

response = chat(model=MODEL, messages=messages, tools=[read_pipeline_log])

if not response.message.tool_calls:
    print("No tool call -> no evidence -> no RCA.")
    raise SystemExit(1)

for tool_call in response.message.tool_calls:
    if tool_call.function.name != "read_pipeline_log":
        print(f"Blocked unknown tool: {tool_call.function.name}")
        raise SystemExit(1)

    tool_result = read_pipeline_log()
    evidence_log.append(
        {
            "tool": "read_pipeline_log",
            "observation": tool_result,
        }
    )

    print("\n===== TOOL REQUESTED =====")
    print(f"Tool: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")

    print("\n===== TOOL RESULT =====")
    print(tool_result)

print("\n===== PRESERVED EVIDENCE =====")
print(format_evidence(evidence_log))

# V3 deliberately separates investigation from reporting.
# The reporter gets only trusted evidence, not the investigation conversation.
report_messages = [
    {
        "role": "system",
        "content": (
            "You are an evidence-only DevOps RCA reporter. "
            "Use only the supplied evidence. "
            "If a claim is not supported by evidence, do not state it as fact."
        ),
    },
    {
        "role": "user",
        "content": (
            "Create the final RCA from this evidence only:\n\n"
            + format_evidence(evidence_log)
            + "\n\nReturn: Root Cause, Confirmed Impact, Recommended Fix, Confidence."
        ),
    },
]

final_response = chat(model=MODEL, messages=report_messages)

print("\n===== V3 EVIDENCE-ONLY RCA =====")
print(final_response.message.content)
