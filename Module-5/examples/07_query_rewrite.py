from rag_utils import build_index, load_chunks, load_model, retrieve, rewrite_query


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    original = input("Ask a DevOps question: ").strip()
    rewritten = rewrite_query(original)

    print(f"\nOriginal : {original}")
    print(f"Rewritten: {rewritten}\n")

    results = retrieve(rewritten, model, index, records, top_k=3)

    print("=== V7: RETRIEVAL AFTER SAFE QUERY REWRITE ===\n")
    for rank, item in enumerate(results, start=1):
        print(f"#{rank} score={item['score']:.4f} source={item['source']} chunk={item['chunk_id']}")
        print(item["text"])
        print("-" * 70)


if __name__ == "__main__":
    main()
