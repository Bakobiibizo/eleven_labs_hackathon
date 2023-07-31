from openai_embeddings import OpenAIEmbeddings
from sentence_transformer_embeddings import SentenceTransformerEmbeddings


class EmbeddingCaller:
    def __init__(self, embedding_type: str, model_name: str = None, **kwargs):
        embedding_types = {
            "sentence_transformers": SentenceTransformerEmbeddings,
            "openai_embeddings": OpenAIEmbeddings,
        }
        if not embedding_type:
            embedding_type = "sentence_transformers"

        try:
            if embedding_type in embedding_types:
                EmbeddingClass = embedding_types[embedding_type]
                self.embedding = EmbeddingClass(model_name=model_name, **kwargs)
        except KeyError:
            raise ValueError(
                f"Unsupported embedding type: {embedding_type}. Supported types are: {list(embedding_types.keys())}"
            )


def test():
    embedding = EmbeddingCaller("sentence_transformers")
    print(embedding)
