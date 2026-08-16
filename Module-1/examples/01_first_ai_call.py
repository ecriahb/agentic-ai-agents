"""Module 1 Lab 01: First OpenAI API call.

Requires OPENAI_API_KEY in a local .env file and API billing/credits.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain AKS in two simple lines.",
)

print("ID:", response.id)
print("Model:", response.model)
print("Status:", response.status)
print("Usage:", response.usage)
print("Answer:", response.output_text)
