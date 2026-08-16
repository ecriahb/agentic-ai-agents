from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
DOCS_DIR = Path(__file__).parent / "sample_docs"
TOP_K = 3


def load_chunks():
    records = []

    for path in sorted(DOCS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")

        # Beginner-friendly paragraph chunking.
        chunks = [part.strip() for part in text.split("\n\n") if part.strip()]

        for number, chunk in enumerate(chunks, start=1):
            records.append(
                {
                    "id": f"{path.stem}-{number:03d}",
                    "source": path.name,
                    "text": chunk,
                }
            )

    return records


def build_index(model, records):
    texts = [record["text"] for record in records]
    vectors = model.encode(texts, normalize_embeddings=True).astype("float32")

    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)
    return index


def main():
    records = load_chunks()
    if not records:
        raise SystemExit(f"No markdown documents found in {DOCS_DIR}")

    print(f"Loaded {len(records)} chunks from {DOCS_DIR.name}/")

    model = SentenceTransformer(MODEL_NAME)
    index = build_index(model, records)

    query = input("\nAsk a DevOps question: ").strip()
    if not query:
        raise SystemExit("Query cannot be empty.")

    query_vector = model.encode([query], normalize_embeddings=True).astype("float32")
    k = min(TOP_K, len(records))
    scores, ids = index.search(query_vector, k=k)

    print("\n=== Retrieved DevOps Knowledge ===\n")

    for rank, (record_id, score) in enumerate(zip(ids[0], scores[0]), start=1):
        record = records[record_id]
        print(f"#{rank} score={score:.4f}")
        print(f"Source: {record['source']}")
        print(f"Chunk ID: {record['id']}")
        print(record["text"])
        print("-" * 70)


if __name__ == "__main__":
    main()
