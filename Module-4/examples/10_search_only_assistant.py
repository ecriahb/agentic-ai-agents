"""Module 4 V10: search-only DevOps knowledge assistant.

This intentionally does NOT call an LLM. Module 4 ends at retrieval.
Usage:
    python 10_search_only_assistant.py "AKS network change troubleshooting"
"""
from pathlib import Path
import sys

import numpy as np
from sentence_transformers import SentenceTransformer

DOCS_DIR = Path(__file__).with_name("sample_docs")
MODEL_NAME = "all-MiniLM-L6-v2"


def load_chunks() -> list[dict]:
    records: list[dict] = []
    for path in sorted(DOCS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        for number, paragraph in enumerate(paragraphs, start=1):
            records.append(
                {
                    "chunk_id": f"{path.stem}-{number:03d}",
                    "source": path.name,
                    "text": paragraph,
                }
            )
    return records


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python 10_search_only_assistant.py "your question"')
        return 2

    query = " ".join(sys.argv[1:]).strip()
    records = load_chunks()
    if not records:
        print("Status: NO_DOCUMENTS")
        return 1

    model = SentenceTransformer(MODEL_NAME)
    doc_vectors = model.encode(
        [record["text"] for record in records],
        normalize_embeddings=True,
    )
    query_vector = model.encode([query], normalize_embeddings=True)[0]
    scores = np.dot(doc_vectors, query_vector)
    order = np.argsort(scores)[::-1][: min(5, len(records))]

    print("Status: SUCCESS")
    print("Query:", query)
    print("Embedding model:", MODEL_NAME)
    print("\n=== RETRIEVED CHUNKS ===")

    for rank, idx in enumerate(order, start=1):
        record = records[int(idx)]
        print(f"\n#{rank} score={scores[idx]:.4f}")
        print("Source:", record["source"])
        print("Chunk ID:", record["chunk_id"])
        print("Text:", record["text"])

    print("\nNo LLM answer was generated. Retrieval is the output of Module 4.")
    print("Similarity score ranks semantic closeness; it is not factual confidence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
