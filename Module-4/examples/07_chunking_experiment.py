"""Module 4 practical: compare giant, paragraph and tiny-line chunking.

No LLM is used. We are evaluating retrieval quality only.
"""
from sentence_transformers import SentenceTransformer
import numpy as np

DOCUMENT = """AKS Networking Runbook

AKS subnet connectivity depends on required NSG rules and routes.

After a Terraform networking change, compare the desired NSG policy with effective rules.

If connectivity validation fails, verify effective routes, DNS resolution and required platform traffic paths before redeployment.
"""

QUERY = "What should I verify after an AKS network policy change?"
MODEL = SentenceTransformer("all-MiniLM-L6-v2")

strategies = {
    "giant": [DOCUMENT.strip()],
    "paragraph": [p.strip() for p in DOCUMENT.split("\n\n") if p.strip()],
    "tiny_lines": [line.strip() for line in DOCUMENT.splitlines() if line.strip()],
}

query_vector = MODEL.encode([QUERY], normalize_embeddings=True)[0]

for name, chunks in strategies.items():
    vectors = MODEL.encode(chunks, normalize_embeddings=True)
    scores = np.dot(vectors, query_vector)
    order = np.argsort(scores)[::-1]

    print(f"\n=== {name.upper()} ===")
    for idx in order[: min(3, len(chunks))]:
        print(f"score={scores[idx]:.4f} | {chunks[int(idx)]}")

print("\nCompare whether the top result contains enough context without unrelated text.")
