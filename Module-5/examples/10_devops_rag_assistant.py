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
    source_map,
    validate_citations,
)

TOP_K_PER_QUERY = 3
MERGED_LIMIT = 5
MIN_SCORE = 0.45


def main():
    print("===== DEVOPS RAG KNOWLEDGE ASSISTANT =====")

    try:
        records = load_chunks()
        model = load_model()
        index = build_index(model, records)
    except Exception as exc:
        raise SystemExit(f"Startup failed: {exc}")

    question = input("\nAsk a DevOps question: ").strip()
    if not question:
        raise SystemExit("Question cannot be empty.")

    variants = multi_query_variants(question)
    result_sets = []

    for variant in variants:
        result_sets.append(
            retrieve(
                variant,
                model,
                index,
                records,
                top_k=TOP_K_PER_QUERY,
            )
        )

    merged = merge_results(result_sets, limit=MERGED_LIMIT)
    strong_results = [item for item in merged if item["score"] >= MIN_SCORE]

    if not strong_results:
        print("\nSTATUS: INSUFFICIENT_CONTEXT")
        print("I could not find sufficiently relevant evidence in the indexed DevOps knowledge base.")
        return

    labeled = label_results(strong_results)
    context = build_context(labeled)
    prompt = build_grounded_prompt(question, context)

    try:
        answer = ollama_generate(prompt)
    except Exception as exc:
        print("\nSTATUS: GENERATION_FAILED")
        print(exc)
        return

    citations_valid, unknown = validate_citations(answer, labeled)

    print("\n=== FINAL GROUNDED ANSWER ===\n")
    print(answer)

    print("\n=== VALIDATION ===")
    if citations_valid:
        print("Citation validation: PASS")
    else:
        print(f"Citation validation: FAIL — unknown IDs: {sorted(unknown)}")

    print("\n=== RETRIEVED SOURCE MAP ===")
    for source_id, item in source_map(labeled).items():
        print(
            f"{source_id}: {item['source']} / {item['chunk_id']} "
            f"/ score={item['score']:.4f}"
        )

    print("\nNOTE:")
    print("This learning assistant is read-only. It explains retrieved knowledge and does not execute remediation.")


if __name__ == "__main__":
    main()
