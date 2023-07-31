import os
import openai
from dotenv import load_dotenv
from openai import Embedding

load_dotenv()


class OpenAIEmbeddings:
    def __init__(self, engine=None, **kwargs: all) -> None:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        if not engine:
            engine = "text-embedding-ada-002"
        self.embedding = openai.Embedding(engine=engine, **kwargs)

        self.embedding.api_key()
        self.get_embedding()

    def get_embedding(self) -> Embedding:
        return self.embedding
