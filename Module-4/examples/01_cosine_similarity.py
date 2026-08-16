import math


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)


query = [1.0, 0.9, 0.1]

examples = {
    "AKS networking incident": [0.9, 1.0, 0.2],
    "Terraform state lock": [0.5, 0.4, 0.6],
    "Docker image optimization": [0.1, 0.2, 1.0],
}

print("Query vector:", query)
print()

for name, vector in examples.items():
    score = cosine_similarity(query, vector)
    print(f"{name}: {score:.4f}")
