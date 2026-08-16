"""Same LangChain chain with Ollama or OpenAI.

Requires Module-6/examples/requirements.txt.
Provider is selected by LLM_PROVIDER=ollama|openai.
"""

import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def build_model():
    provider = os.getenv("LLM_PROVIDER", "ollama").strip().lower()

    if provider == "ollama":
        from langchain_ollama import ChatOllama

        return provider, ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "qwen3:4b"),
            temperature=0,
        )

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY_MISSING")
        return provider, ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
            temperature=0,
        )

    raise ValueError("LLM_PROVIDER must be 'ollama' or 'openai'")


provider, model = build_model()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a grounded DevOps incident analyst.
Use only supplied evidence for current-incident factual claims.
If evidence is insufficient, say so.
Do not claim that you executed a remediation.
""",
        ),
        (
            "human",
            """Incident: {incident}

Evidence:
{evidence}

Return Root Cause, Evidence Gaps, Recommended Next Checks.""",
        ),
    ]
)

chain = prompt | model | StrOutputParser()

answer = chain.invoke(
    {
        "incident": "Production AKS deployment failed after a Terraform networking change.",
        "evidence": (
            "[E1] Deployment failed during Terraform Apply.\n"
            "[E2] NSG rule aks-subnet-allow was removed.\n"
            "[E3] AKS subnet connectivity validation failed after the change."
        ),
    }
)

print("Provider:", provider)
print("Model class:", type(model).__name__)
print("\n=== Answer ===")
print(answer)
print("\nArchitecture unchanged: PromptTemplate → Model → Parser")
