from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCS_DIR = Path(__file__).parent / "sample_docs"

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)
all_chunks = []

for path in sorted(DOCS_DIR.glob("*.md")):
    docs = TextLoader(str(path), encoding="utf-8").load()
    for doc in docs:
        doc.metadata["source"] = path.name
    all_chunks.extend(splitter.split_documents(docs))

print(f"Loaded {len(all_chunks)} chunks")
for i, chunk in enumerate(all_chunks[:5], 1):
    print(f"\nChunk {i} | source={chunk.metadata.get('source')}")
    print(chunk.page_content)
