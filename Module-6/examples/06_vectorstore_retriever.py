from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCS_DIR = Path(__file__).parent / "sample_docs"


def load_chunks():
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)
    chunks = []
    for path in sorted(DOCS_DIR.glob("*.md")):
        docs = TextLoader(str(path), encoding="utf-8").load()
        for doc in docs:
            doc.metadata["source"] = path.name
        chunks.extend(splitter.split_documents(docs))
    return chunks


chunks = load_chunks()
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

question = "AKS deployment failed after Terraform networking change"
results = retriever.invoke(question)

for i, doc in enumerate(results, 1):
    print(f"\n#{i} source={doc.metadata.get('source')}")
    print(doc.page_content)
