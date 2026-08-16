# Security Notes for Module 10 Labs

These examples are educational security harnesses. They intentionally avoid real cloud mutation.

## Baseline rules

- Treat user input, retrieved content, MCP resources, tool output and agent messages as untrusted data.
- Never execute free-form LLM output as shell, SQL, Terraform or kubectl.
- Keep production write tools behind deterministic policy, authorization and human approval.
- Keep secrets out of model context whenever possible.
- Redact sensitive values before logging, tracing or checkpointing.
- Preserve evidence provenance and source IDs.
- Fail closed for uncertain high-risk operations.
- Convert discovered red-team failures into permanent regression tests.

## Safe extension

When replacing simulated tools with Azure/GitHub integrations, begin with read-only identities and sandbox environments. Add real write capability only after policy, authorization, approval, audit and recovery paths are independently tested.
