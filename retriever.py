from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


DOCUMENTS_DIR = Path("data/documents")
CHROMA_DIR = Path("data/chroma_db")

COLLECTION_NAME = "docmind_documents"

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Embedding model loaded successfully!")


def load_chunks():
    chunks = []

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        chunk_size = 500
        overlap = 50

        start = 0
        chunk_id = 0

        while start < len(text):
            chunk = text[start:start + chunk_size]

            if chunk.strip():
                chunks.append({
                    "text": chunk,
                    "source": file_path.name,
                    "chunk_id": chunk_id
                })

            chunk_id += 1
            start += chunk_size - overlap

    return chunks


def create_vector_store():
    client = chromadb.PersistentClient(
        path=str(CHROMA_DIR)
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    chunks = load_chunks()

    # Create the collection only if it is empty.
    if collection.count() == 0:

        print("Creating vector store...")

        texts = [chunk["text"] for chunk in chunks]

        embeddings = model.encode(
            texts,
            normalize_embeddings=True
        ).tolist()

        collection.add(
            ids=[
                f"{chunk['source']}_{chunk['chunk_id']}"
                for chunk in chunks
            ],
            documents=texts,
            embeddings=embeddings,
            metadatas=[
                {
                    "source": chunk["source"],
                    "chunk_id": chunk["chunk_id"]
                }
                for chunk in chunks
            ]
        )

        print("Vector store created successfully!")

    return collection


def retrieve(question, k=3):
    collection = create_vector_store()

    question_embedding = model.encode(
        [question],
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=question_embedding,
        n_results=k
    )

    retrieved = []

    for i in range(len(results["documents"][0])):
        retrieved.append({
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "score": results["distances"][0][i]
        })

    return retrieved


if __name__ == "__main__":

    collection = create_vector_store()

    print(f"Stored documents: {collection.count()}")

    question = input("\nQuestion:\n")

    results = retrieve(question)

    print("\nRetrieved information:")

    for index, result in enumerate(results, start=1):
        print(f"\n--- RESULT {index} ---")
        print(result["text"])
        print(f"Score: {result['score']:.4f}")