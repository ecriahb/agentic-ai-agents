import asyncio

from mcp import Client

from importlib import util
from pathlib import Path


# Import the V3 server by file path so this example remains runnable
# even though the filename starts with a number.
server_path = Path(__file__).with_name("03_resource_server.py")
spec = util.spec_from_file_location("resource_server", server_path)
module = util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)
mcp = module.mcp


async def main() -> None:
    async with Client(mcp) as client:
        print("Protocol:", client.protocol_version)
        print("Server:", client.server_info)

        resources = await client.list_resources()
        templates = await client.list_resource_templates()

        print("\nStatic resources:")
        for resource in resources.resources:
            print("-", resource.uri)

        print("\nResource templates:")
        for template in templates.resource_templates:
            print("-", template.uri_template)

        result = await client.read_resource("runbook://aks/networking")
        print("\nAKS runbook:")
        for item in result.contents:
            text = getattr(item, "text", None)
            if text:
                print(text)

        incident = await client.read_resource("incident://INC-1042/evidence")
        print("\nIncident evidence:")
        for item in incident.contents:
            text = getattr(item, "text", None)
            if text:
                print(text)


if __name__ == "__main__":
    asyncio.run(main())
