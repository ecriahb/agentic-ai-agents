from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
DOCS_DIR = Path(__file__).parent / "sample_docs"
TOP_K = 3
MAX_CHARS = 600


def chunk_by_paragraph(text: str, max_chars: int = MAX_CHARS):
    """Beginner-friendly paragraph-aware chunker.

    It tries to keep paragraph boundaries intact while preventing chunks
    from growing indefinitely. Production systems should evaluate chunking
    against real retrieval queries instead of assuming one size is best.
    """
    paragraphs = [part.strip() for part in text.split("\n\n") if part.strip()]
    chunks = []
    current = ""

    for paragraph in paragraphs:
        candidate = f"{current}\n\n{paragraph}".strip()

        if current and len(candidate) > max_chars:
            chunks.append(current)
            current = paragraph
        else:
            current = candidate

    if current:
        chunks.append(current)

    return chunks


def load_chunks():
    records = []
    files = sorted(DOCS_DIR.glob("*.md"))

    if not files:
        raise RuntimeError(f"No Markdown documents found in {DOCS_DIR}")

    for path in files:
        text = path.read_text(encoding="utf-8").strip()

        if not text:
            print(f"Skipping empty file: {path.name}")
            continue

        chunks = chunk_by_paragraph(text)

        for chunk_no, chunk in enumerate(chunks):
            records.append(
                {
                    "id": f"{path.name}::{chunk_no:03d}",
                    "source": path.name,
                    "chunk_no": chunk_no,
                    "text": chunk,
                }
            )

    if not records:
        raise RuntimeError("No usable chunks were created from the documents.")

    return records


def build_index(model, records):
    texts = [record["text"] for record in records]

    vectors = model.encode(
        texts,
        normalize_embeddings=True,
    )
    vectors = np.asarray(vectors, dtype="float32")

    if vectors.ndim != 2 or vectors.shape[0] != len(records):
        raise RuntimeError("Unexpected embedding matrix shape.")

    dimension = vectors.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(vectors)

    if index.ntotal != len(records):
        raise RuntimeError("FAISS index count does not match record count.")

    return index, dimension


def retrieve(query, model, index, records, dimension, top_k=TOP_K):
    query = query.strip()
    if not query:
        raise ValueError("Query cannot be empty.")

    query_vector = model.encode(
        [query],
        normalize_embeddings=True,
    )
    query_vector = np.asarray(query_vector, dtype="float32")

    if query_vector.ndim != 2 or query_vector.shape[1] != dimension:
        raise RuntimeError("Query embedding dimension does not match the index.")

    k = min(top_k, len(records))
    scores, indices = index.search(query_vector, k=k)

    results = []

    for rank, (score, idx) in enumerate(zip(scores[0], indices[0]), start=1):
        if idx < 0 or idx >= len(records):
            continue

        record = records[idx]
        results.append(
            {
                "rank": rank,
                "score": float(score),
                "id": record["id"],
                "source": record["source"],
                "chunk_no": record["chunk_no"],
                "text": record["text"],
            }
        )

    return results


def print_results(query, results):
    print("\n=== Semantic DevOps Knowledge Search ===")
    print(f"Query: {query}\n")

    if not results:
        print("No retrieval results were returned.")
        return

    for result in results:
        print(f"#{result['rank']}  score={result['score']:.4f}")
        print(f"Source: {result['source']}")
        print(f"Chunk ID: {result['id']}")
        print(result["text"])
        print("-" * 72)


def main():
    try:
        records = load_chunks()
    except (OSError, RuntimeError) as exc:
        raise SystemExit(f"Knowledge-base loading failed: {exc}") from exc

    print(f"Loaded {len(records)} chunks from {DOCS_DIR.name}/")
    print(f"Embedding model: {MODEL_NAME}")

    model = SentenceTransformer(MODEL_NAME)
    index, dimension = build_index(model, records)

    print(f"Embedding dimension: {dimension}")
    print(f"FAISS vectors: {index.ntotal}")

    query = input("\nAsk a DevOps question: ")

    try:
        results = retrieve(query, model, index, records, dimension)
    except (ValueError, RuntimeError) as exc:
        raise SystemExit(f"Search failed: {exc}") from exc

    print_results(query.strip(), results)


if __name__ == "__main__":
    main()
