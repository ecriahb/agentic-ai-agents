from rag_utils import (
    build_context,
    build_grounded_prompt,
    build_index,
    label_results,
    load_chunks,
    load_model,
    ollama_generate,
    retrieve,
    source_map,
)


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    question = input("Ask a DevOps question: ").strip()
    labeled = label_results(retrieve(question, model, index, records, top_k=3))
    answer = ollama_generate(build_grounded_prompt(question, build_context(labeled)))

    print("\n=== V4: SOURCE-AWARE RAG ANSWER ===\n")
    print(answer)
    print("\n=== SOURCE MAP ===")
    for source_id, item in source_map(labeled).items():
        print(f"{source_id}: {item['source']} / {item['chunk_id']} / score={item['score']:.4f}")


if __name__ == "__main__":
    main()
