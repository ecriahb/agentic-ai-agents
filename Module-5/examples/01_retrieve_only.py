from rag_utils import build_index, load_chunks, load_model, retrieve


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    query = input("Ask a DevOps question: ").strip()
    results = retrieve(query, model, index, records, top_k=3)

    print("\n=== V1: RETRIEVED CHUNKS ===\n")
    for rank, item in enumerate(results, start=1):
        print(f"#{rank} score={item['score']:.4f}")
        print(f"Source: {item['source']}")
        print(f"Chunk: {item['chunk_id']}")
        print(item["text"])
        print("-" * 70)


if __name__ == "__main__":
    main()
