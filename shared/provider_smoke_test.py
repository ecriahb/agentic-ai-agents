from llm_provider import ask_llm

SYSTEM = (
    "You are a beginner-friendly DevOps AI tutor. "
    "Be concise and do not invent facts."
)

PROMPT = "Explain AKS in exactly two simple lines."

result = ask_llm(PROMPT, system=SYSTEM)

print("Provider:", result.provider)
print("Model:", result.model)
print("Answer:")
print(result.text)
