from rag_utils import (
    build_context,
    build_grounded_prompt,
    build_index,
    label_results,
    load_chunks,
    load_model,
    ollama_generate,
    retrieve,
)


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    question = input("Ask a DevOps question: ").strip()
    results = retrieve(question, model, index, records, top_k=3)
    labeled = label_results(results)
    context = build_context(labeled)
    prompt = build_grounded_prompt(question, context)

    print("\n=== V3: BASIC RAG ANSWER ===\n")
    print(ollama_generate(prompt))


if __name__ == "__main__":
    main()
