"""Compare local SentenceTransformer embeddings with OpenAI embeddings.

Choose:
  EMBEDDING_PROVIDER=local
or
  EMBEDDING_PROVIDER=openai

Important: build/search an index with one embedding model at a time.
Do not mix dimensions from different models in the same vector index.
"""

import os
from typing import Callable

import numpy as np
from dotenv import load_dotenv

load_dotenv()

DOCUMENTS = [
    "Terraform removed an AKS subnet NSG allow rule.",
    "A Kubernetes pod is restarting because of an application exception.",
    "The deployment pipeline failed during Terraform Apply.",
]
QUERY = "network security change broke the AKS deployment"


def normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return vectors / norms


def local_embed(texts: list[str]) -> np.ndarray:
    from sentence_transformers import SentenceTransformer

    model_name = os.getenv("LOCAL_EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    model = SentenceTransformer(model_name)
    return np.asarray(model.encode(texts), dtype="float32")


def openai_embed(texts: list[str]) -> np.ndarray:
    from openai import OpenAI

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY_MISSING")

    model_name = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
    client = OpenAI()
    response = client.embeddings.create(model=model_name, input=texts)
    return np.asarray([item.embedding for item in response.data], dtype="float32")


provider = os.getenv("EMBEDDING_PROVIDER", "local").lower().strip()
embedders: dict[str, Callable[[list[str]], np.ndarray]] = {
    "local": local_embed,
    "openai": openai_embed,
}

if provider not in embedders:
    raise ValueError("EMBEDDING_PROVIDER must be 'local' or 'openai'")

embed = embedders[provider]
doc_vectors = normalize(embed(DOCUMENTS))
query_vector = normalize(embed([QUERY]))[0]

scores = doc_vectors @ query_vector
ranking = np.argsort(scores)[::-1]

print("Provider:", provider)
print("Vector dimension:", doc_vectors.shape[1])
print("\nRanked results:")
for rank, index in enumerate(ranking, start=1):
    print(f"{rank}. score={scores[index]:.4f} | {DOCUMENTS[index]}")

print("\nRule: similarity scores are meaningful inside the same embedding space; they are not factual confidence.")
