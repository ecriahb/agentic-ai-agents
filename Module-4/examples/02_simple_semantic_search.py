from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

documents = [
    "Validate AKS subnet NSG rules when workloads lose connectivity after a network change.",
    "Check Terraform state locking before attempting a force-unlock.",
    "Use multi-stage Docker builds to reduce final image size.",
    "Inspect Terraform Apply logs when the deployment pipeline fails during infrastructure changes.",
]

query = input("Enter your DevOps query: ").strip()
if not query:
    raise SystemExit("Query cannot be empty.")

# normalize_embeddings=True lets dot product behave like cosine similarity.
doc_vectors = model.encode(documents, normalize_embeddings=True)
query_vector = model.encode([query], normalize_embeddings=True)[0]

scores = doc_vectors @ query_vector
ranking = np.argsort(scores)[::-1]

print("\nTop matches:\n")
for rank, idx in enumerate(ranking[:3], start=1):
    print(f"#{rank} score={scores[idx]:.4f}")
    print(documents[idx])
    print()
