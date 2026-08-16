"""Module 4 practical: evaluate retrieval with a tiny labelled test set.

Metric: Hit@K — did the expected source appear in the top K results?
"""
from sentence_transformers import SentenceTransformer
import numpy as np

DOCS = [
    ("aks-networking.md", "AKS subnet connectivity depends on NSG rules, routes, DNS and platform network paths."),
    ("terraform-networking.md", "Terraform networking changes should be reviewed for NSG, UDR, subnet and private endpoint impact."),
    ("pipeline-failure.md", "A deployment pipeline can fail during Terraform Apply and should preserve stage/error evidence."),
    ("rollback.md", "Production rollback should follow approved change controls and validation steps."),
]

TESTS = [
    ("AKS subnet security and route troubleshooting", "aks-networking.md"),
    ("review Terraform NSG and UDR changes", "terraform-networking.md"),
    ("deployment failed during infrastructure apply", "pipeline-failure.md"),
    ("how to rollback production safely", "rollback.md"),
]

MODEL = SentenceTransformer("all-MiniLM-L6-v2")
texts = [text for _, text in DOCS]
vectors = MODEL.encode(texts, normalize_embeddings=True)

TOP_K = 2
hits = 0

for query, expected_source in TESTS:
    query_vector = MODEL.encode([query], normalize_embeddings=True)[0]
    scores = np.dot(vectors, query_vector)
    order = np.argsort(scores)[::-1][:TOP_K]
    retrieved = [DOCS[int(i)][0] for i in order]
    hit = expected_source in retrieved
    hits += int(hit)

    print(f"\nQuery: {query}")
    print("Expected:", expected_source)
    print("Retrieved:", retrieved)
    print("Hit@K:", hit)

print(f"\nOverall Hit@{TOP_K}: {hits}/{len(TESTS)} = {hits / len(TESTS):.2%}")
print("Learning: tune chunking/model/top-k from labelled failures, not from one impressive demo query.")
