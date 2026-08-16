from rag_utils import build_context, build_grounded_prompt, build_index, label_results, load_chunks, load_model, ollama_generate, retrieve


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    question = input("Ask a DevOps question: ").strip()
    results = retrieve(question, model, index, records, top_k=3)

    if not results:
        print("Insufficient evidence: no context was retrieved.")
        return

    labeled = label_results(results)
    context = build_context(labeled)
    prompt = build_grounded_prompt(question, context)

    print("\n=== V5: NO-CONTEXT GUARDED RAG ===\n")
    print(ollama_generate(prompt))


if __name__ == "__main__":
    main()
