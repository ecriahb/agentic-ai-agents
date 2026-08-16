import asyncio
from importlib import util
from pathlib import Path

from mcp import Client

server_path = Path(__file__).with_name("06_devops_mcp_server.py")
spec = util.spec_from_file_location("devops_mcp_server", server_path)
assert spec and spec.loader
module = util.module_from_spec(spec)
spec.loader.exec_module(module)
mcp = module.mcp

READ_ONLY_ALLOWLIST = {
    "get_pipeline_status",
    "get_terraform_changes",
    "get_aks_status",
}

ALLOWED_ENVIRONMENTS = {"dev", "stage", "production"}
ALLOWED_CLUSTERS = {"dev-aks", "prod-aks"}


def validate_request(tool_name: str, arguments: dict) -> dict:
    if tool_name not in READ_ONLY_ALLOWLIST:
        raise ValueError(f"Tool is not allowed in investigation mode: {tool_name}")

    clean = dict(arguments)

    if "environment" in clean:
        env = str(clean["environment"]).strip().lower()
        if env not in ALLOWED_ENVIRONMENTS:
            raise ValueError("Unsupported environment")
        clean["environment"] = env

    if "cluster_name" in clean:
        cluster = str(clean["cluster_name"]).strip().lower()
        if cluster not in ALLOWED_CLUSTERS:
            raise ValueError("Unsupported cluster")
        clean["cluster_name"] = cluster

    return clean


async def safe_call(client: Client, tool_name: str, arguments: dict) -> dict:
    tools_result = await client.list_tools()
    discovered = {tool.name for tool in tools_result.tools}

    if tool_name not in discovered:
        raise RuntimeError(f"Requested tool was not discovered: {tool_name}")

    clean_args = validate_request(tool_name, arguments)
    result = await client.call_tool(tool_name, clean_args)

    if result.is_error:
        return {
            "status": "TOOL_ERROR",
            "tool": tool_name,
            "arguments": clean_args,
            "content": [getattr(block, "text", str(block)) for block in result.content],
        }

    return {
        "status": "SUCCESS",
        "tool": tool_name,
        "arguments": clean_args,
        "result": result.structured_content,
    }


async def main() -> None:
    async with Client(mcp) as client:
        record = await safe_call(
            client,
            "get_terraform_changes",
            {"environment": "production"},
        )
        print(record)

        # Uncomment to verify the host-side allowlist blocks unknown/write-like tools.
        # await safe_call(client, "restart_deployment", {"environment": "production"})


if __name__ == "__main__":
    asyncio.run(main())
