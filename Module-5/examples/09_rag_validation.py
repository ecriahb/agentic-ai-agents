from rag_utils import (
    build_context,
    build_grounded_prompt,
    build_index,
    label_results,
    load_chunks,
    load_model,
    ollama_generate,
    retrieve,
    validate_citations,
)


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    question = input("Ask a DevOps question: ").strip()
    labeled = label_results(retrieve(question, model, index, records, top_k=3))

    if not labeled:
        print("Insufficient evidence: no context was retrieved.")
        return

    answer = ollama_generate(build_grounded_prompt(question, build_context(labeled)))
    valid, unknown = validate_citations(answer, labeled)

    print("\n=== V9: RAG ANSWER ===\n")
    print(answer)

    print("\n=== CITATION VALIDATION ===")
    if valid:
        print("PASS: all cited source IDs came from retrieved context.")
    else:
        print(f"FAIL: model cited unknown source IDs: {sorted(unknown)}")


if __name__ == "__main__":
    main()
