import chromadb
from embeddings.embeddings_caller import EmbeddingsCaller


class Vectorstores:
    def __init__(self):
        self.persona = self.select_persona()
        self.embeddings = EmbeddingsCaller()
        self.db = chromadb.Client(
            chroma_db_impl="duckdb+parquet",
            persistent_directory=f"static/vectorstores/{self.persona}",
            embedding_function=self.embeddings(),
        )
        self.collection = self.get_or_create_collection(self.persona)

    def select_persona(self, persona="Azure"):
        self.persona = persona
        self.db = chromadb.Client(
            chroma_db_impl="duckdb+parquet",
            persistent_directory=f"static/vectorstores/{self.persona}",
        )

    def create_collection(self, collection_name):
        return chromadb.Client(
            chroma_db_impl="duckdb+parquet",
            persistent_directory=f"static/vectorstores/{collection_name}",
        )

    def delete_collection(self, collection_name):
        self.db.delete_collection(collection_name)
        return "collection deleted"

    def get_or_create_collection(self, collection_name):
        return self.db.get_or_create_collection(collection_name)

    def get_collection(self, collection_name):
        return self.db.get_collection(collection_name)

    def change_name(self, collection_name, new_name):
        self.db.modify(collection_name, new_name)
        return "collection name changed"

    def add_document(self, documents, metadata=None, ids=None):
        self.db.add(documents, metadata, ids)
        return "document added"

    def query(self, query_texts, n_result=5, metadata=None, contains=None):
        return self.db.query(
            query_texts=query_texts,
            n_result=n_result,
            metadata={"metadata_field": metadata},
            contains={"$contains": contains},
        )

    def update_document(self, ids, embeddings, metadatas, documents):
        self.collection.update(ids, embeddings, metadatas, documents)
        return "document updated"

    def delete_document(self, ids):
        self.collection.delete(ids)
        return "document deleted"

    def get_embeddings(self, embeddings="sentence_transformers"):
        return self.embeddings.select_embeddings(embeddings)
