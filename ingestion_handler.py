from ingestion.vectorstore.vectorstore import Vectorstores
from ingestion.splitters.splitter_selector import SplitterSelector
from ingestion.loaders.loader_selector import LoaderSelector
from ingestion.embeddings.embeddings_caller import EmbeddingCaller

class IngestionHandler(Vectorstores):
    def __init__(self):
        super.__init__(self)
        self.splitters = SplitterSelector(splitter=None)
        self.loaders = LoaderSelector(loader_name=None)
        self.emeddings = EmbeddingCaller(embedding_type=None, model_name=None)
