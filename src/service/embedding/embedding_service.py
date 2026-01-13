import chromadb
from chromadb.utils import embedding_functions
import os

from model.FileMetadata import FileMetadata


class EmbeddingService:
    def __init__(self):

        # Initialize ChromaDB client with persistent storage inside current execution directory
        self.client = chromadb.PersistentClient(path=".glasspilot/db")

        # Using ChromaDB's built-in Sentence Transformer function
        self.sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        print("Local ChromaDB file location:", self.client)

    def embed_file(self, file_metadata: FileMetadata):
        """Read a text file and add it to the ChromaDB collection"""

        file_path = os.path.join(file_metadata.path, file_metadata.file_name)
        print(f"Reading file: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Create or get a collection with the embedding function
            collection = self.client.get_or_create_collection(
                name="documents",
                embedding_function=self.sentence_transformer_ef
            )
            # Add to collection (ChromaDB will automatically embed using the embedding function)
            collection.add(
                documents=[content],
                ids=[file_path],
                metadatas=[{"source": file_path, "type": "file"}]
            )
            print(f"Successfully embedded: {file_path}")
        except Exception as e:
            print(f"Error embedding {file_path}: {e}")

    # Example: Embedding multiple files
    def embed_directory(self, directory_path, collection):
        """Embed all text files in a directory"""
        for filename in os.listdir(directory_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory_path, filename)
                self.embed_file(file_path, collection)

    # Example: Chunking large files before embedding
    def embed_file_chunked(self, file_path, chunk_size=500):
        """Split file into chunks and embed each chunk separately"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Simple chunking by character count
            chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

            # Create unique IDs for each chunk
            ids = [f"{os.path.basename(file_path)}_chunk_{i}" for i in range(len(chunks))]
            metadatas = [{"source": file_path, "chunk": i, "type": "file_chunk"}
                         for i in range(len(chunks))]

            # Create or get a collection with the embedding function
            collection = self.client.get_or_create_collection(
                name="documents",
                embedding_function=self.sentence_transformer_ef
            )
            collection.add(
                documents=chunks,
                ids=ids,
                metadatas=metadatas
            )
            print(f"Successfully embedded {len(chunks)} chunks from: {file_path}")
        except Exception as e:
            print(f"Error embedding {file_path}: {e}")

    # Example: Querying the collection
    def search_documents(self, query_text, collection, n_results=3):
        """Search for similar documents"""

        # Create or get a collection with the embedding function
        collection = self.client.get_or_create_collection(
            name="documents",
            embedding_function=self.sentence_transformer_ef
        )
        results = collection.query(
            query_texts=[query_text],
            n_results=n_results
        )

        print(f"\nTop {n_results} results for: '{query_text}'")
        for i, (doc, metadata, distance) in enumerate(zip(
                results['documents'][0],
                results['metadatas'][0],
                results['distances'][0]
        )):
            print(f"\n--- Result {i + 1} (Distance: {distance:.4f}) ---")
            print(f"Source: {metadata.get('source', 'Unknown')}")
            print(f"Content preview: {doc[:200]}...")


# singleton service
embedding_service = EmbeddingService()
