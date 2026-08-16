from rag_utils import build_context, build_index, label_results, load_chunks, load_model, retrieve


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    query = input("Ask a DevOps question: ").strip()
    results = retrieve(query, model, index, records, top_k=3)
    labeled = label_results(results)
    context = build_context(labeled)

    print("\n=== V2: LLM CONTEXT BLOCK ===\n")
    print(context)


if __name__ == "__main__":
    main()
