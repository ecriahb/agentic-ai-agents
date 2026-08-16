from rag_utils import (
    build_context,
    build_grounded_prompt,
    build_index,
    label_results,
    load_chunks,
    load_model,
    merge_results,
    multi_query_variants,
    ollama_generate,
    retrieve,
)


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    question = input("Ask a DevOps question: ").strip()
    variants = multi_query_variants(question)

    print("\n=== QUERY VARIANTS ===")
    for variant in variants:
        print(f"- {variant}")

    result_sets = [retrieve(q, model, index, records, top_k=3) for q in variants]
    merged = merge_results(result_sets, limit=5)

    if not merged:
        print("Insufficient evidence: multi-query retrieval returned no context.")
        return

    labeled = label_results(merged)
    prompt = build_grounded_prompt(question, build_context(labeled))

    print("\n=== V8: MULTI-QUERY RAG ANSWER ===\n")
    print(ollama_generate(prompt))


if __name__ == "__main__":
    main()
