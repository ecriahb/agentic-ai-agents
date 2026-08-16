from openai import OpenAI

# Local Ollama OpenAI-compatible endpoint.
# Start Ollama first and ensure your model is available locally.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

SYSTEM_PROMPT = """
You are a grounded DevOps incident analyst.
Use only the evidence supplied by the user.
Do not invent tool results or customer impact.
Separate confirmed facts from inference.
If evidence is insufficient, say 'Insufficient evidence'.
""".strip()

USER_PROMPT = """
Analyze this production deployment incident.

Evidence:
E1: NSG rule aks-subnet-allow was removed.
E2: AKS subnet connectivity validation failed.
E3: Deployment failed during Terraform Apply.

Return:
1. Confirmed Evidence
2. Likely Root Cause
3. Confirmed Impact
4. Missing Evidence
5. Validation Steps
6. Recommended Fix
7. Confidence
""".strip()

response = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
    temperature=0.2,
)

print(response.choices[0].message.content)
