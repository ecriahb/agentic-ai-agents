from pathlib import Path
from ollama import chat

MODEL = "qwen3:0.6b"
LOG_FILE = Path(__file__).parent / "logs" / "pipeline.log"


def read_pipeline_log() -> str:
    """Read the real pipeline log from disk."""
    return LOG_FILE.read_text(encoding="utf-8")


messages = [
    {
        "role": "user",
        "content": (
            "Our AKS deployment started failing after Terraform changes. "
            "Investigate the failure using the available tool and give the likely root cause."
        ),
    }
]

response = chat(model=MODEL, messages=messages, tools=[read_pipeline_log])
messages.append(response.message)

if response.message.tool_calls:
    for tool_call in response.message.tool_calls:
        print("\n===== TOOL REQUESTED =====")
        print(f"Tool: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")

        if tool_call.function.name == "read_pipeline_log":
            tool_result = read_pipeline_log()

            print("\n===== TOOL RESULT =====")
            print(tool_result)

            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_call.function.name,
                    "content": tool_result,
                }
            )

    final_response = chat(model=MODEL, messages=messages)
    print("\n===== FINAL RESPONSE =====")
    print(final_response.message.content)
else:
    print("Model did not request a tool.")
