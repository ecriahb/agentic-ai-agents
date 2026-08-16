"""Module 1 Lab 02: Run an LLM locally with Ollama via OpenAI-compatible API."""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",
)

response = client.responses.create(
    model="gemma3:1b",
    input="Explain AKS in two simple lines.",
)

print("ID:", response.id)
print("Model:", response.model)
print("Status:", response.status)
print("Usage:", response.usage)
print("Answer:", response.output_text)
