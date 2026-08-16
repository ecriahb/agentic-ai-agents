import chromadb

client = chromadb.PersistentClient(path="./chroma_data")
collection = client.get_or_create_collection("devops_docs")

# Add only once for this learning example.
if collection.count() == 0:
    collection.add(
        ids=["aks-001", "tf-001", "docker-001"],
        documents=[
            "Validate AKS subnet NSG rules when workloads lose connectivity after a Terraform network change.",
            "For Terraform state lock errors, verify whether another apply is active before force-unlocking.",
            "Use multi-stage Docker builds and smaller base images to reduce container image size.",
        ],
        metadatas=[
            {"service": "aks", "type": "runbook"},
            {"service": "terraform", "type": "runbook"},
            {"service": "docker", "type": "guide"},
        ],
    )

query = input("Enter your DevOps query: ").strip()
if not query:
    raise SystemExit("Query cannot be empty.")

results = collection.query(
    query_texts=[query],
    n_results=3,
)

print("\nResults:\n")
for i, document in enumerate(results["documents"][0], start=1):
    metadata = results["metadatas"][0][i - 1]
    print(f"#{i} {metadata}")
    print(document)
    print()
