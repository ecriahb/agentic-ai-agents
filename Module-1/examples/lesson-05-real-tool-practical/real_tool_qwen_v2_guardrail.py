from pathlib import Path
from ollama import chat

MODEL = "qwen3:0.6b"
LOG_FILE = Path(__file__).parent / "logs" / "pipeline.log"


def read_pipeline_log() -> str:
    return LOG_FILE.read_text(encoding="utf-8")


messages = [
    {
        "role": "user",
        "content": (
            "Investigate why the AKS deployment failed after Terraform changes. "
            "Use the available evidence tool before giving an RCA."
        ),
    }
]

evidence_log: list[dict[str, str]] = []

response = chat(model=MODEL, messages=messages, tools=[read_pipeline_log])
messages.append(response.message)

# Guardrail: no evidence means no RCA.
if not response.message.tool_calls:
    print("===== GUARDRAIL =====")
    print("No tool was requested. RCA blocked because no evidence was collected.")
    raise SystemExit(1)

for tool_call in response.message.tool_calls:
    print("\n===== TOOL REQUESTED =====")
    print(f"Tool: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")

    if tool_call.function.name != "read_pipeline_log":
        print("Unknown tool requested. Execution blocked.")
        raise SystemExit(1)

    tool_result = read_pipeline_log()

    print("\n===== TOOL RESULT =====")
    print(tool_result)

    evidence_log.append(
        {
            "tool": tool_call.function.name,
            "observation": tool_result,
        }
    )

    messages.append(
        {
            "role": "tool",
            "tool_name": tool_call.function.name,
            "content": tool_result,
        }
    )

print("\n===== PRESERVED EVIDENCE =====")
for item in evidence_log:
    print(f"Tool: {item['tool']}")
    print("Observation:")
    print(item["observation"])

final_response = chat(
    model=MODEL,
    messages=messages
    + [
        {
            "role": "user",
            "content": (
                "Give an RCA using only the collected tool evidence. "
                "Do not invent facts that are not present in the evidence."
            ),
        }
    ],
)

print("\n===== GROUNDED RCA =====")
print(final_response.message.content)
