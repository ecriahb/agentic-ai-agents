from ollama import chat


evidence = """
Network Security Group rule
aks-subnet-allow was removed.

AKS subnet connectivity validation failed.

Deployment failed during Terraform Apply.
"""


system_prompt = """
You are an Evidence-Based DevOps Investigator.

GLOBAL RULES:

1. Use only the supplied evidence.

2. Never invent customer impact.

3. Never claim production downtime
   unless explicitly present in evidence.

4. Never claim data loss
   unless explicitly present.

5. Separate confirmed facts
   from hypotheses.

6. If causality is not fully proven,
   use cautious wording.

7. Recommend validation
   before remediation.

8. Do not execute any production action.
"""


user_prompt = f"""
Investigate why the production
deployment failed.

TRUSTED EVIDENCE:

{evidence}

Return:

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
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    think=False
)


print(
    "\n===== SYSTEM PROMPT ====="
)

print(system_prompt)


print(
    "\n===== USER PROMPT ====="
)

print(user_prompt)


print(
    "\n===== MODEL RESPONSE ====="
)

print(
    response.message.content
)
