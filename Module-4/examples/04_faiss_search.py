import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

documents = [
    "Validate AKS subnet NSG rules after a network configuration change.",
    "Check Terraform state locking before attempting force-unlock.",
    "Use multi-stage Docker builds to reduce final image size.",
    "Inspect Terraform Apply logs when infrastructure deployment fails.",
]

# Normalized vectors + inner product give cosine-style ranking.
doc_vectors = model.encode(documents, normalize_embeddings=True).astype("float32")

dimension = doc_vectors.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(doc_vectors)

query = input("Enter your DevOps query: ").strip()
if not query:
    raise SystemExit("Query cannot be empty.")

query_vector = model.encode([query], normalize_embeddings=True).astype("float32")

scores, ids = index.search(query_vector, k=min(3, len(documents)))

print("\nTop matches:\n")
for rank, (doc_id, score) in enumerate(zip(ids[0], scores[0]), start=1):
    print(f"#{rank} score={score:.4f}")
    print(documents[doc_id])
    print()
