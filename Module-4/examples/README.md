# Module 4 — Practical Examples

These examples move from vector math to a searchable DevOps knowledge base.

## Run Order

```text
01_cosine_similarity.py
        ↓
02_simple_semantic_search.py
        ↓
03_chromadb_search.py
        ↓
04_faiss_search.py
        ↓
05_devops_knowledge_base.py
```

## What Each File Teaches

| File | Learning |
|---|---|
| `01_cosine_similarity.py` | similarity math without a vector DB |
| `02_simple_semantic_search.py` | ranking pre-defined vectors |
| `03_chromadb_search.py` | collection-based local semantic search |
| `04_faiss_search.py` | low-level vector index search |
| `05_devops_knowledge_base.py` | searchable local DevOps markdown files |

## Setup

```powershell
cd Module-4\examples
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

For embedding-based examples, Sentence Transformers downloads the selected model the first time it is used, so internet access may be required once.

## Sample Queries

```text
AKS connectivity failed after subnet security change
Terraform state is locked
Docker image is too large
Deployment failed during Terraform apply
```

## Important

The examples are learning labs. Production systems additionally need access control, document lifecycle, backup/persistence strategy, retrieval evaluation, observability and secret/sensitive-data controls.
