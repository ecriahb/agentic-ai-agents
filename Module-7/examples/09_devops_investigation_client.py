import asyncio
from importlib import util
from pathlib import Path
from typing import Any

from mcp import Client

server_path = Path(__file__).with_name("06_devops_mcp_server.py")
spec = util.spec_from_file_location("devops_mcp_server", server_path)
assert spec and spec.loader
module = util.module_from_spec(spec)
spec.loader.exec_module(module)
mcp = module.mcp

REQUIRED_TOOLS = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}


def evidence_record(
    evidence_id: str,
    operation: str,
    arguments: dict[str, Any],
    payload: Any,
) -> dict[str, Any]:
    return {
        "id": evidence_id,
        "kind": "CURRENT_EVIDENCE",
        "server": "Module7-DevOps-Investigation",
        "operation": operation,
        "arguments": arguments,
        "payload": payload,
    }


def reference_record(reference_id: str, uri: str, text: str) -> dict[str, Any]:
    return {
        "id": reference_id,
        "kind": "REFERENCE",
        "server": "Module7-DevOps-Investigation",
        "uri": uri,
        "payload": text,
    }


async def call_evidence_tool(
    client: Client,
    evidence_id: str,
    tool_name: str,
    arguments: dict[str, Any],
) -> dict[str, Any]:
    result = await client.call_tool(tool_name, arguments)
    if result.is_error:
        return {
            "id": evidence_id,
            "kind": "TOOL_ERROR",
            "operation": tool_name,
            "arguments": arguments,
            "error": [getattr(block, "text", str(block)) for block in result.content],
        }
    return evidence_record(evidence_id, tool_name, arguments, result.structured_content)


async def read_text_resource(client: Client, reference_id: str, uri: str) -> dict[str, Any]:
    result = await client.read_resource(uri)
    texts = [getattr(item, "text", "") for item in result.contents]
    text = "\n".join(part for part in texts if part)
    return reference_record(reference_id, uri, text)


async def main() -> None:
    async with Client(mcp) as client:
        tools_result = await client.list_tools()
        discovered = {tool.name for tool in tools_result.tools}
        missing = REQUIRED_TOOLS - discovered

        if missing:
            raise SystemExit(f"CAPABILITY_MISSING: {sorted(missing)}")

        evidence_store = [
            await call_evidence_tool(
                client,
                "E1",
                "get_pipeline_status",
                {"environment": "production"},
            ),
            await call_evidence_tool(
                client,
                "E2",
                "get_terraform_changes",
                {"environment": "production"},
            ),
            await call_evidence_tool(
                client,
                "E3",
                "get_aks_status",
                {"cluster_name": "prod-aks"},
            ),
        ]

        references = [
            await read_text_resource(client, "R1", "runbook://aks/networking"),
            await read_text_resource(client, "R2", "runbook://terraform/networking"),
        ]

        prompt_result = await client.get_prompt(
            "incident_rca",
            {"incident_id": "INC-1042", "environment": "production"},
        )

        print("=== Protocol ===")
        print(client.protocol_version)

        print("\n=== Current Evidence ===")
        for item in evidence_store:
            print(item)

        print("\n=== Reference Knowledge ===")
        for item in references:
            print(item)

        print("\n=== MCP Prompt ===")
        for message in prompt_result.messages:
            content = getattr(message.content, "text", str(message.content))
            print(f"{message.role}: {content}")


if __name__ == "__main__":
    asyncio.run(main())
