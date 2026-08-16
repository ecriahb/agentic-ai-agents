# Module 7 — Zero-to-Hero Practical Roadmap

> Goal: external capabilities ko MCP ke through standardize karna, phir discovery, tools, resources, clients, transport, safety and grounded reasoning ko incrementally combine karna.

## V1 — First MCP Server
Run `examples/01_first_mcp_server.py`.

**Learn:** server process, capability exposure, protocol boundary.

## V2 — Typed DevOps Tool
Run `02_devops_tool_server.py`.

Test valid and invalid arguments.

**Rule:** typed schema helpful hai; authorization still host/server responsibility hai.

## V3 — Resources
Run `03_resource_server.py`.

Read a resource and explain why resource content is data/reference, not automatically trusted instruction.

## V4 — MCP Prompt
Run `04_prompt_server.py`.

Inspect prompt discovery separately from tool execution.

## V5 — First MCP Client
Run `05_mcp_client.py`.

Trace:
`Client connects → discovers capabilities → calls/reads → receives result`.

## V6 — Multi-Tool DevOps MCP Server
Run/inspect `06_devops_mcp_server.py`.

Capabilities include pipeline, Terraform and AKS read-only evidence plus runbook resources.

## V7 — Streamable HTTP
Run `07_streamable_http_server.py`.

Compare local stdio-style trust assumptions with deployed HTTP server concerns.

## V8 — Safe Host Dispatch
Run `08_safe_mcp_dispatch.py`.

Attack tests:
- unknown tool
- invalid environment
- invalid cluster
- unexpected argument

Expected: deterministic policy rejection.

## V9 — Investigation Client
Run `09_devops_investigation_client.py`.

Collect E1/E2/E3 and R1/R2. Confirm current evidence vs reference knowledge remain separate.

## V10 — MCP DevOps Assistant
Run `10_mcp_devops_assistant.py`.

Check citation validation and read-only behavior.

## Provider Bonus 1
Run `11_dual_provider_mcp_reasoning.py`.

## Provider Bonus 2 — Real MCP Evidence Path
Run `12_dual_provider_live_mcp_assistant.py` with Ollama and OpenAI.

**Pass:** both providers consume the same MCP-collected evidence; MCP discovery does not change authorization policy.

### Acceptance Criteria
Learner can explain:
```text
MCP server = capability provider
MCP client = protocol consumer
Discovery != permission
Tool result != final truth
Resource != current incident proof
Host policy remains authoritative
```

## Hero Outcome
Learner can connect AI applications to standardized external capabilities without giving the model direct execution authority.
