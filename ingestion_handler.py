#from ingestion.splitters.splitter_selector import SplitterSelector
#from ingestion.embeddings.embeddings_caller import EmbeddingCaller
#from ingestion.loaders.loader_selector import LoaderSelector
#from ingestion.vectorstore.vectorstore import Vectorstores
#
#class IngestionHandler(Vectorstores):
#    def __init__(self):
#        super.__init__(self)
#        self.splitters = SplitterSelector(splitter=None)
#        self.loaders = LoaderSelector(loader_name=None)
#        self.emeddings = EmbeddingCaller(embedding_type=None, model_name=None)
#
#def test():
#    document_path = "D:/papers/orca.pdf"
#    ingestion = IngestionHandler()
#    vectorstore = ingestion.vectorstore
#    loader = ingestion.loaders.pdf_loader()
#    splitter = ingestion.splitters.create_nltk_splitter(separators=["."])
#    data = loader.load(document_path)
#    docs = splitter.split(data)
#    print(docs)
#    embeddings = ingestion.get_embeddings(docs)
#    with open("ingest/docs/embeddings.txt", "w") as f:
#        f.write(str(embeddings))
#    print(embeddings)
#    vectorstore.add(embeddings)
#    
#test()
#    
#    