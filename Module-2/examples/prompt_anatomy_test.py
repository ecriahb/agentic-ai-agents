from ollama import chat


evidence = """
Environment: Production

Pipeline Stage:
Terraform Apply

Observed Evidence:

Network Security Group rule
aks-subnet-allow was removed.

AKS subnet connectivity validation failed.

Deployment failed during Terraform Apply.
"""


prompt = f"""
ROLE:

You are a Senior Azure DevOps Engineer
specializing in Terraform and AKS.


TASK:

Analyze why the production deployment failed.


CONTEXT:

{evidence}


CONSTRAINTS:

- Use only the supplied evidence.
- Do not invent missing facts.
- Do not claim customer impact.
- Do not claim production downtime.
- Do not claim data loss.
- Do not assume pod failures.
- If causality is not fully proven,
  use cautious wording.
- Recommend validation before remediation.


OUTPUT FORMAT:

Return exactly these sections:

1. Observed Evidence

2. Likely Root Cause

3. Confirmed Impact

4. Recommended Fix

5. Validation Steps
"""


response = chat(
    model="qwen3:0.6b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    think=False
)


print(
    "\n===== PRODUCTION PROMPT ====="
)

print(prompt)


print(
    "\n===== MODEL RESPONSE ====="
)

print(
    response.message.content
)
