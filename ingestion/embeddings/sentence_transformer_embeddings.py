from sentence_transformers import SentenceTransformer
from typing import Iterable
from modulefinder import Module


class SentenceTransformerEmbeddings:
    def __init__(
        self,
        model_name_or_path: str | None = (None,),
        modules: Iterable[Module] | None = (None,),
        device: str | None = (None,),
        cache_folder: str | None = (None,),
        use_auth_token: str | None = (None,),
    ) -> None:
        if not model_name_or_path:
            model_name_or_path = "all-MiniLM-L6-v2"
            self.embedding = SentenceTransformer(
                model_name_or_path,
                modules=modules,
                device=device,
                cache_folder=cache_folder,
                use_auth_token=use_auth_token,
            )

    def get_embedding(self):
        return self.embedding
