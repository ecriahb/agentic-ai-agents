from rag_utils import build_context, build_grounded_prompt, build_index, label_results, load_chunks, load_model, ollama_generate, retrieve

MIN_SCORE = 0.45


def main():
    records = load_chunks()
    model = load_model()
    index = build_index(model, records)

    question = input("Ask a DevOps question: ").strip()
    results = retrieve(question, model, index, records, top_k=3)
    strong_results = [item for item in results if item["score"] >= MIN_SCORE]

    print(f"Best score: {results[0]['score']:.4f}" if results else "No result")
    print(f"Threshold: {MIN_SCORE:.2f}")

    if not strong_results:
        print("Insufficient evidence: retrieval quality did not meet the configured threshold.")
        return

    labeled = label_results(strong_results)
    prompt = build_grounded_prompt(question, build_context(labeled))

    print("\n=== V6: THRESHOLD-GUARDED RAG ===\n")
    print(ollama_generate(prompt))


if __name__ == "__main__":
    main()
